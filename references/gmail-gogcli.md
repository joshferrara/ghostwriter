# Gmail via `openclaw/gogcli`

`gogcli` provides the `gog` command — a script-friendly CLI for Google Workspace, including Gmail. Use it to pull your **sent** mail for analysis.

- Repo: https://github.com/openclaw/gogcli
- Binary: `gog`
- Best for: quick, scriptable local pulls when you don't already have an email connector.

> Command flags below reflect gogcli's documented surface. Run `gog gmail --help` and `gog gmail search --help` to confirm exact flags for your installed version, since CLIs change.

## Install

```bash
# Homebrew (macOS / Linux)
brew install openclaw/tap/gogcli
gog --version

# Docker
docker run --rm ghcr.io/openclaw/gogcli:latest version

# From source
git clone https://github.com/openclaw/gogcli.git
cd gogcli && make && ./bin/gog --version
```

Windows: download `gogcli_<version>_windows_amd64.zip` from the latest release, extract `gog.exe`, add to PATH.

## Authenticate

```bash
# Point gog at your OAuth client secret (downloaded from Google Cloud Console)
gog auth credentials ~/Downloads/client_secret_....json

# Add your account with the Gmail scope (read-only is enough for analysis)
gog auth add you@gmail.com --services gmail

# Verify auth
gog auth doctor --check

# Select the active account for subsequent commands
export GOG_ACCOUNT=you@gmail.com
```

## Pull sent mail

Gmail search uses standard Gmail query syntax. `in:sent` is the key filter; add a date range to bound the corpus.

```bash
# List sent message IDs from the past year (adjust --max as needed)
gog gmail search 'in:sent newer_than:1y' --max 500 --json > sent-ids.json

# Narrower window
gog gmail search 'in:sent newer_than:90d' --max 200 --json

# Exclude obvious noise up front where the query allows
gog gmail search 'in:sent newer_than:1y -in:chats' --max 500 --json
```

Fetch the body of each message. `--sanitize-content` strips tracking/markup; `--json` gives structured output:

```bash
gog gmail get <messageId> --sanitize-content --json
```

Loop over the IDs you collected (shell example):

```bash
for id in $(jq -r '.[].id' sent-ids.json); do
  gog gmail get "$id" --sanitize-content --json >> sent-messages.jsonl
done
```

`--plain` produces TSV instead of JSON if you prefer line-oriented output.

## What to keep / drop

Keep only writing the user actually composed. Drop, where practical:

- Forwarded messages and quoted reply history (analyze only the newly typed portion)
- Transactional/automated mail that slipped through (receipts, calendar, notifications)
- Link-only or one-line transactional replies
- Signature blocks and legal boilerplate

Then hand the cleaned set to the analysis step (`references/analysis-framework.md`).

## Troubleshooting

- `gog` not found → not installed; offer `googleworkspace/cli` (`references/gmail-googleworkspace-cli.md`) or a local export (`references/local-email-exports.md`).
- Auth fails → re-run `gog auth doctor --check`; confirm the Gmail API is enabled in the Cloud project tied to your client secret.
- Empty results → confirm `in:sent` returns mail in the Gmail web UI for the same query, and widen the date range.
