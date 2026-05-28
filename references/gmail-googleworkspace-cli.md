# Gmail via `googleworkspace/cli`

Google's official Workspace CLI provides the `gws` command. It reads Google's Discovery service at runtime and builds its command surface dynamically, so Gmail is accessed through the standard `users.messages` methods.

- Repo: https://github.com/googleworkspace/cli
- Binary: `gws`
- Best for: users who want the full, official Workspace API surface, or who are scripting in CI.

> The `--params` payloads below mirror the Gmail REST API. Run `gws gmail --help` to confirm the command shape for your installed version.

## Install

```bash
# Pre-built binary (recommended): download from GitHub Releases
# https://github.com/googleworkspace/cli/releases

# npm
npm install -g @googleworkspace/cli

# Homebrew
brew install googleworkspace-cli

# Cargo
cargo install --git https://github.com/googleworkspace/cli --locked

# Nix
nix run github:googleworkspace/cli
```

## Authenticate

```bash
# Interactive desktop setup: creates a Cloud project, enables APIs, logs you in
gws auth setup

# Subsequent logins / scope selection
gws auth login
```

Headless / CI: export credentials from an authenticated machine and point the CLI at them:

```bash
gws auth export --unmasked > credentials.json
export GOOGLE_WORKSPACE_CLI_CREDENTIALS_FILE=/path/to/credentials.json
```

A service-account key works the same way via `GOOGLE_WORKSPACE_CLI_CREDENTIALS_FILE`.

## Pull sent mail

Use the Gmail `users.messages.list` method with `q: "in:sent"` plus a date range, then `get` each message. Output is structured JSON by default.

```bash
# List sent message IDs from the past year
gws gmail users messages list \
  --params '{"userId": "me", "q": "in:sent newer_than:1y", "maxResults": 500}'

# Narrower window
gws gmail users messages list \
  --params '{"userId": "me", "q": "in:sent newer_than:90d", "maxResults": 200}'

# Read a specific message (full body)
gws gmail users messages get \
  --params '{"userId": "me", "id": "MESSAGE_ID", "format": "full"}'
```

Use `--dry-run` to preview a request without executing it.

Loop over IDs (shell example):

```bash
gws gmail users messages list \
  --params '{"userId":"me","q":"in:sent newer_than:1y","maxResults":500}' \
  > sent-list.json

for id in $(jq -r '.messages[].id' sent-list.json); do
  gws gmail users messages get \
    --params "{\"userId\":\"me\",\"id\":\"$id\",\"format\":\"full\"}" >> sent-messages.jsonl
done
```

Gmail returns bodies as base64url; decode the `payload` parts before analysis (the `scripts/parse_mbox.py` helper has decoding logic you can reuse, or decode inline with `base64 --decode` after URL-safe substitution).

## What to keep / drop

Same as any email source — keep only newly composed text, drop forwards, quoted history, transactional mail, signatures, and boilerplate. Then proceed to `references/analysis-framework.md`.

## Troubleshooting

- `gws` not found → not installed; offer `openclaw/gogcli` (`references/gmail-gogcli.md`) or a local export (`references/local-email-exports.md`).
- Scope errors → re-run `gws auth login` and grant the Gmail read scope.
- Base64 bodies look garbled → you're reading the raw `payload.body.data`; decode URL-safe base64 first.
