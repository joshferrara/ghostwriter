#!/usr/bin/env python3
"""Normalize a generic writing corpus (text / JSONL / JSON / CSV) into clean JSONL.

Trims whitespace, drops empty / link-only entries, de-duplicates, and optionally
drops one-word entries for long-form corpora. Output is one JSON object per line:
{"body": "..."}.
Feed the result to the analysis step (see references/analysis-framework.md).

Usage:
    python3 sample_corpus.py messages.txt   --format text  --out clean.jsonl
    python3 sample_corpus.py texts.txt      --format text  --keep-short --out clean.jsonl
    python3 sample_corpus.py export.jsonl    --format jsonl --field text   --max 500 --out clean.jsonl
    python3 sample_corpus.py export.json     --format json  --field content --out clean.jsonl
    python3 sample_corpus.py export.csv      --format csv   --field message --out clean.jsonl

Text format: messages are separated by blank lines (one block = one message).
Use --keep-short for texts/chat, where one-word reactions and fragments can be
part of the user's real voice.
Standard library only.
"""
from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from pathlib import Path

LINK_ONLY = re.compile(r"^\s*https?://\S+\s*$")


def is_noise(text: str, keep_short: bool = False) -> bool:
    t = (text or "").strip()
    if not t:
        return True
    if keep_short and len(t) < 2:
        return True
    if not keep_short and len(t) < 3:
        return True
    if not keep_short and len(t.split()) <= 1:
        return True
    if LINK_ONLY.match(t):
        return True
    return False


def load_text(path: Path):
    blocks = re.split(r"\n\s*\n", path.read_text(encoding="utf-8", errors="replace"))
    for b in blocks:
        yield b.strip()


def load_jsonl(path: Path, field: str):
    with path.open(encoding="utf-8", errors="replace") as fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue
            try:
                obj = json.loads(line)
            except json.JSONDecodeError:
                continue
            yield extract_field(obj, field)


def load_json(path: Path, field: str):
    data = json.loads(path.read_text(encoding="utf-8", errors="replace"))
    if isinstance(data, dict):
        # common containers: {"messages": [...]} etc. — take the first list value
        for v in data.values():
            if isinstance(v, list):
                data = v
                break
    if not isinstance(data, list):
        return
    for obj in data:
        yield extract_field(obj, field)


def load_csv(path: Path, field: str):
    with path.open(encoding="utf-8", errors="replace", newline="") as fh:
        reader = csv.DictReader(fh)
        if reader.fieldnames is None:
            return
        col = field if field in (reader.fieldnames or []) else None
        if col is None:
            print(f"error: column '{field}' not found. Available: {reader.fieldnames}",
                  file=sys.stderr)
            raise SystemExit(1)
        for row in reader:
            yield (row.get(col) or "").strip()


def extract_field(obj, field: str) -> str:
    if isinstance(obj, str):
        return obj.strip()
    if isinstance(obj, dict):
        val = obj.get(field)
        if val is None:
            return ""
        return str(val).strip()
    return str(obj).strip()


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("source", help="input file")
    ap.add_argument("--format", required=True, choices=["text", "jsonl", "json", "csv"])
    ap.add_argument("--field", default="text",
                    help="field/column holding the message body (jsonl/json/csv)")
    ap.add_argument("--out", default="clean.jsonl", help="output JSONL path")
    ap.add_argument("--max", type=int, default=0, help="cap number of messages (0 = no cap)")
    ap.add_argument("--keep-short", action="store_true",
                    help="keep one-word/short reactions for text or chat corpora")
    args = ap.parse_args()

    src = Path(args.source).expanduser()
    if not src.exists():
        print(f"error: {src} not found", file=sys.stderr)
        return 1

    loaders = {
        "text": lambda: load_text(src),
        "jsonl": lambda: load_jsonl(src, args.field),
        "json": lambda: load_json(src, args.field),
        "csv": lambda: load_csv(src, args.field),
    }

    seen: set[str] = set()
    written = 0
    out_path = Path(args.out).expanduser()
    with out_path.open("w", encoding="utf-8") as out:
        for body in loaders[args.format]():
            body = (body or "").strip()
            if is_noise(body, keep_short=args.keep_short):
                continue
            key = body.lower()
            if key in seen:
                continue
            seen.add(key)
            out.write(json.dumps({"body": body}, ensure_ascii=False) + "\n")
            written += 1
            if args.max and written >= args.max:
                break

    print(f"wrote {written} messages to {out_path}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
