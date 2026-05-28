# Other local writing corpora (text / JSON / CSV / mailbox / pasted)

The universal fallback. Whenever a connector or CLI isn't available, the user can hand over their own writing directly. This always works and needs no auth.

## Accepted inputs

- **Pasted samples** — the user pastes 30–100 messages straight into the conversation. Fastest path; great for a first guide.
- **Plain text** (`.txt`, `.md`) — one message per blank-line-separated block, or any readable dump.
- **JSON / JSONL** — arrays or line-delimited objects; tell the agent which field holds the message body (e.g. `body`, `text`, `content`).
- **CSV / TSV** — name the column that holds the message text (and optionally a date/recipient column).
- **Mailbox** (`.mbox`, `.eml`) — see `references/local-email-exports.md` and `scripts/parse_mbox.py`.
- **Other exports** — WhatsApp `.txt` export, Discord data export, Notes, blog post archives, etc. Any prose the user actually wrote.

## Sampling and cleaning

Use the helper to normalize a text/JSON/CSV corpus into one-message-per-line JSONL and drop obvious noise:

```bash
# Plain text, blocks separated by blank lines
python3 scripts/sample_corpus.py messages.txt --format text --out clean.jsonl

# Texts/chat, preserving short reactions and fragments
python3 scripts/sample_corpus.py texts.txt --format text --keep-short --out clean.jsonl

# JSONL, body in the "text" field, sample 500
python3 scripts/sample_corpus.py export.jsonl --format jsonl --field text --max 500 --out clean.jsonl

# CSV, message in the "message" column
python3 scripts/sample_corpus.py export.csv --format csv --field message --out clean.jsonl
```

The script trims whitespace, drops empty / link-only entries, de-duplicates, and can cap volume with `--max`. By default it drops one-word entries for long-form corpora; use `--keep-short` for texts/chat so reactions and fragments remain available for short-form voice analysis. See `scripts/sample_corpus.py`.

If no Python is available, the agent can read the file directly and apply the same filtering by hand — the script just makes it repeatable.

## What to keep / drop

- Keep only writing the user composed (not quotes, forwards, or pasted articles).
- Drop link-only entries. Drop one-word/no-context entries for long-form corpora, but keep short reactions and fragments for texts/chat when they reveal the user's short-form voice.
- For mixed corpora, note which context each batch came from (email vs. chat vs. blog) so the guide can keep voices distinct.

## How this feeds the guide

Send the cleaned set to `references/analysis-framework.md`. If the corpus is small (say, under ~50 messages), still produce a guide but mark it as a **first pass** the user can refine later by adding another source and re-running Generate mode.
