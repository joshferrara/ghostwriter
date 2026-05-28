# Local sent email exports (`.mbox` / `.eml`)

No API or auth required. Works when the user can export their mail to disk — the most private option, since nothing leaves the machine.

## Getting an export

### Gmail / Google (Takeout)
1. Go to https://takeout.google.com
2. Deselect all, then select **Mail**.
3. Optionally use "All Mail data included" → choose only the **Sent** label.
4. Export and download. You get an `.mbox` file (often `Sent.mbox` or `All mail Including Spam and Trash.mbox`).

### Apple Mail
- Select the **Sent** mailbox → **Mailbox ▸ Export Mailbox…** → produces an `.mbox` package.

### Outlook / Thunderbird
- Thunderbird with the ImportExportTools NG add-on can export a folder to `.mbox` or individual `.eml` files.
- Outlook exports to `.pst`; convert to `.mbox` with a converter, or export individual messages as `.eml`.

## Parse it

Use the included helper to extract clean, newly-composed sent text and drop quoted history, forwards, and boilerplate:

```bash
python3 scripts/parse_mbox.py /path/to/Sent.mbox --out sent-messages.jsonl

# Apple Mail export packages are directories that contain an mbox file
python3 scripts/parse_mbox.py /path/to/AppleExport.mbox --out sent-messages.jsonl

# Bound by date and cap volume
python3 scripts/parse_mbox.py /path/to/Sent.mbox \
  --since 2024-05-01 --max 800 --out sent-messages.jsonl

# Filter to messages you sent from a specific address (useful for combined mailboxes)
python3 scripts/parse_mbox.py /path/to/All.mbox \
  --from you@gmail.com --out sent-messages.jsonl
```

The script accepts Google Takeout-style `.mbox` files, Apple Mail `.mbox` package directories, or loose `.eml` folders. It outputs one JSON object per line with `date`, `to`, `subject`, and `body` (quoted text and signatures stripped where detectable). See `scripts/parse_mbox.py` for the exact filters.

For loose `.eml` files, point the script at the directory:

```bash
python3 scripts/parse_mbox.py /path/to/eml-folder/ --out sent-messages.jsonl
```

## What to keep / drop

The script already removes the common noise; spot-check the output and additionally drop:

- Pure forwards with no added text
- Auto-replies / out-of-office
- One-line transactional confirmations

Then proceed to `references/analysis-framework.md`.

## Troubleshooting

- No Python available → the agent can parse the `.mbox` directly (it's plain text with `From ` separators) without the script.
- Huge mailbox → use `--since` and `--max` to sample a recent, representative slice rather than the whole archive.
- Encodings look wrong → the script handles quoted-printable and base64 transfer encodings; if a message still looks garbled, it's likely an attachment-only mail and can be skipped.
