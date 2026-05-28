#!/usr/bin/env python3
"""Extract clean, newly-composed SENT messages from an .mbox file or a folder of .eml files.

Outputs one JSON object per line (JSONL) with: date, to, subject, body.
Quoted reply history, forwarded blocks, and common signature/boilerplate are
stripped where detectable, so the analysis step sees only what the user actually typed.

Usage:
    python3 parse_mbox.py /path/to/Sent.mbox --out sent-messages.jsonl
    python3 parse_mbox.py /path/to/AppleExport.mbox --out sent-messages.jsonl
    python3 parse_mbox.py /path/to/Sent.mbox --since 2024-05-01 --max 800 --out out.jsonl
    python3 parse_mbox.py /path/to/All.mbox --from you@gmail.com --out out.jsonl
    python3 parse_mbox.py /path/to/eml-folder/ --out out.jsonl

Standard library only. No third-party dependencies.
"""
from __future__ import annotations

import argparse
import json
import mailbox
import re
import sys
from datetime import datetime
from email import policy
from email.message import EmailMessage
from email.utils import getaddresses, parsedate_to_datetime
from pathlib import Path

# Lines at/after which the rest of the message is quoted history or a forward.
QUOTE_MARKERS = [
    re.compile(r"^\s*On .+ wrote:\s*$"),
    re.compile(r"^\s*-{2,}\s*Original Message\s*-{2,}", re.I),
    re.compile(r"^\s*-{2,}\s*Forwarded message\s*-{2,}", re.I),
    re.compile(r"^\s*From:\s.+", re.I),  # forwarded header block
    re.compile(r"^_{5,}\s*$"),
]
# Signature delimiters / common boilerplate openers.
SIG_MARKERS = [
    re.compile(r"^\s*--\s*$"),                       # standard sig delimiter
    re.compile(r"^\s*Sent from my (iPhone|iPad|Android|phone)", re.I),
    re.compile(r"^\s*Get Outlook for", re.I),
]


def strip_html(text: str) -> str:
    text = re.sub(r"(?is)<(script|style).*?>.*?</\1>", " ", text)
    text = re.sub(r"(?is)<br\s*/?>", "\n", text)
    text = re.sub(r"(?is)</p>", "\n\n", text)
    text = re.sub(r"(?s)<[^>]+>", " ", text)
    # minimal entity decode
    for a, b in (("&nbsp;", " "), ("&amp;", "&"), ("&lt;", "<"),
                 ("&gt;", ">"), ("&quot;", '"'), ("&#39;", "'")):
        text = text.replace(a, b)
    return text


def get_body(msg: EmailMessage) -> str:
    """Prefer text/plain; fall back to stripped text/html."""
    plain, html = None, None
    if msg.is_multipart():
        for part in msg.walk():
            if part.get_content_maintype() != "text":
                continue
            if part.get("Content-Disposition", "").lower().startswith("attachment"):
                continue
            try:
                content = part.get_content()
            except Exception:
                payload = part.get_payload(decode=True)
                if payload is None:
                    continue
                charset = part.get_content_charset() or "utf-8"
                content = payload.decode(charset, errors="replace")
            if part.get_content_subtype() == "plain" and plain is None:
                plain = content
            elif part.get_content_subtype() == "html" and html is None:
                html = content
    else:
        try:
            content = msg.get_content()
        except Exception:
            payload = msg.get_payload(decode=True)
            charset = msg.get_content_charset() or "utf-8"
            content = payload.decode(charset, errors="replace") if payload else ""
        if msg.get_content_subtype() == "html":
            html = content
        else:
            plain = content
    body = plain if plain is not None else (strip_html(html) if html else "")
    return body or ""


def clean_body(body: str) -> str:
    """Drop quoted history, forwards, and signatures; normalize whitespace."""
    lines = body.replace("\r\n", "\n").split("\n")
    kept: list[str] = []
    for line in lines:
        if any(m.match(line) for m in QUOTE_MARKERS):
            break  # everything below is quoted/forwarded
        if any(m.match(line) for m in SIG_MARKERS):
            break  # signature; stop here
        if line.lstrip().startswith(">"):
            continue  # quoted line
        kept.append(line)
    text = "\n".join(kept)
    text = re.sub(r"\n{3,}", "\n\n", text).strip()
    return text


def is_noise(body: str) -> bool:
    if not body or len(body.strip()) < 3:
        return True
    words = body.split()
    if len(words) <= 1:
        return True
    # link-only message
    if re.fullmatch(r"\s*https?://\S+\s*", body):
        return True
    return False


def iter_messages(path: Path):
    if path.is_dir():
        # Apple Mail exports a mailbox as a directory package containing an
        # mbox file. Loose .eml directories are handled below.
        package_mbox = path / "mbox"
        if package_mbox.is_file():
            box = mailbox.mbox(str(package_mbox), factory=None)
            for key in box.iterkeys():
                yield box[key]
            return

        eml_paths = sorted(path.glob("**/*.eml"))
        if not eml_paths:
            raise FileNotFoundError(
                f"{path} is a directory, but contains no 'mbox' file or .eml files"
            )
        for p in eml_paths:
            with p.open("rb") as fh:
                yield mailbox.mboxMessage(fh.read())
    else:
        box = mailbox.mbox(str(path), factory=None)
        for key in box.iterkeys():
            yield box[key]


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("source", help=".mbox file or folder of .eml files")
    ap.add_argument("--out", default="sent-messages.jsonl", help="output JSONL path")
    ap.add_argument("--since", help="only messages on/after this date (YYYY-MM-DD)")
    ap.add_argument("--max", type=int, default=0, help="cap number of messages (0 = no cap)")
    ap.add_argument("--from", dest="from_addr",
                    help="only messages sent from this address (for combined mailboxes)")
    args = ap.parse_args()

    src = Path(args.source).expanduser()
    if not src.exists():
        print(f"error: {src} not found", file=sys.stderr)
        return 1

    since = None
    if args.since:
        try:
            since = datetime.strptime(args.since, "%Y-%m-%d")
        except ValueError:
            print("error: --since must be YYYY-MM-DD", file=sys.stderr)
            return 1

    written = 0
    out_path = Path(args.out).expanduser()
    try:
        messages = iter_messages(src)
        with out_path.open("w", encoding="utf-8") as out:
            for raw in messages:
                # Re-parse with the modern policy for robust content handling.
                try:
                    msg: EmailMessage = mailbox.message_from_bytes(
                        raw.as_bytes(), policy=policy.default)  # type: ignore[attr-defined]
                except Exception:
                    try:
                        from email import message_from_bytes
                        msg = message_from_bytes(raw.as_bytes(), policy=policy.default)
                    except Exception:
                        continue

                if args.from_addr:
                    senders = [a.lower() for _, a in getaddresses([str(msg.get("From", ""))])]
                    if args.from_addr.lower() not in senders:
                        continue

                dt = None
                date_hdr = msg.get("Date")
                if date_hdr:
                    try:
                        dt = parsedate_to_datetime(date_hdr)
                    except Exception:
                        dt = None
                if since and dt and dt.replace(tzinfo=None) < since:
                    continue

                body = clean_body(get_body(msg))
                if is_noise(body):
                    continue

                to_addrs = ", ".join(a for _, a in getaddresses(
                    [str(msg.get("To", "")), str(msg.get("Cc", ""))]) if a)
                record = {
                    "date": dt.isoformat() if dt else None,
                    "to": to_addrs,
                    "subject": str(msg.get("Subject", "")).strip(),
                    "body": body,
                }
                out.write(json.dumps(record, ensure_ascii=False) + "\n")
                written += 1
                if args.max and written >= args.max:
                    break
    except FileNotFoundError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    print(f"wrote {written} messages to {out_path}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
