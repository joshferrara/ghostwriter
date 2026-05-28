# Local iMessage (macOS)

iMessage adds the user's **short-form / texting voice**, which is usually looser and more reactive than email. On macOS, sent messages live in a local SQLite database. This source never leaves the machine.

## Where the data is

```
~/Library/Messages/chat.db
```

Reading it requires **Full Disk Access** for your terminal/agent app:
System Settings ▸ Privacy & Security ▸ Full Disk Access ▸ enable your terminal (e.g. Terminal, iTerm, the app running the agent). Quit and reopen the app after granting.

## Pull sent texts

Sent messages are rows where `is_from_me = 1`. Tapbacks and system rows must be excluded.

```bash
# Copy the db first so you never touch the live file
cp ~/Library/Messages/chat.db /tmp/chat.db

sqlite3 /tmp/chat.db <<'SQL'
.mode json
.once sent-texts.json
SELECT
  datetime(message.date/1000000000 + 978307200, 'unixepoch', 'localtime') AS sent_at,
  message.text AS body
FROM message
WHERE message.is_from_me = 1
  AND message.text IS NOT NULL
  AND length(trim(message.text)) > 0
  AND message.associated_message_type = 0   -- exclude tapbacks/reactions
  AND message.item_type = 0                 -- exclude system/group-event rows
ORDER BY message.date DESC
LIMIT 2000;
SQL
```

Notes:
- Apple stores `date` as nanoseconds since 2001-01-01; the `+ 978307200` offset converts to Unix epoch.
- On newer macOS the message text may live in `attributedBody` (a binary blob) rather than `text`. If `text` is empty for many rows, the agent should decode `attributedBody` or fall back to asking the user to paste a sample.
- `associated_message_type = 0` drops tapbacks (likes, hearts, emphasis). `item_type = 0` drops "X named the conversation", "Y joined", etc.

## What to keep / drop

- Drop link-only messages and one-character sends.
- Drop tapback/system rows (the query already does).
- Keep short reactions and fragments — they ARE the texting voice ("Yep!", "Oh nice!", "Haha amazing"). Do not upgrade them into prose.

## How this feeds the guide

Text-message behavior is its own dimension in `references/analysis-framework.md`. Capture: typical length (often a handful of words), reaction openers, use of emoji, elongated words ("Yesss", "Ohhh"), punctuation habits (often no trailing period), and how the user splits thoughts across multiple quick sends. Keep this clearly separate from the long-form email voice in the final guide.

## Troubleshooting

- `unable to open database file` → Full Disk Access not granted, or you're reading the live file while Messages holds a lock; copy it to `/tmp` first.
- Mostly empty `text` column → decode `attributedBody`, or ask the user to paste 30–50 representative texts instead (`references/generic-corpora.md`).
- Not on macOS → there is no local iMessage DB; use another source.
