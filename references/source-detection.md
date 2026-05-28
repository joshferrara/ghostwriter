# Source detection: check existing access first

**Rule: before suggesting any new setup, inventory what the current agent environment can already reach.** Existing access (a connector, MCP server, plugin, app integration, or built-in tool) requires the least work and should be recommended first. Only fall back to setup-based options when nothing is connected.

This file is agent-agnostic. Use whichever probe fits the agent you're running inside; skip the ones that don't apply.

## What to look for

You want read access to **sent** messages from one or more of:

- Email (Gmail, Outlook, IMAP, etc.)
- Slack or other team chat
- Local messages (iMessage on macOS)
- Any document/notes store that holds the user's own prose

## How to probe each environment

### Any agent
1. List your own available tools / functions and scan names for: `gmail`, `mail`, `email`, `outlook`, `slack`, `message`, `imessage`, `drive`, `docs`, `notion`.
2. List connected MCP servers and their tools. A server named or namespaced `gmail`, `slack`, `google`, `outlook`, etc. is a ready-made source.
3. Check for already-installed CLIs on PATH: `gog`, `gws`, `imsg`, `himalaya`, `mbsync`, `notmuch`.
4. Ask the user directly what they've already connected — they often know faster than any probe.

### Claude Code / Claude
- Look for connectors/MCP tools such as a Gmail connector, Slack connector, or Google Drive connector exposed as `mcp__...` tools.
- These are the preferred path when present — no CLI auth needed.

### Codex / OpenAI-style agents
- Check configured tools and any MCP servers wired into the session.
- Check for shell access; if present, installed CLIs (`gog`, `gws`) become options.

### OpenCode / OpenClaw-style and Hermes / local agents
- These usually have shell access. Check PATH for `gog` (openclaw/gogcli) and `gws` (googleworkspace/cli) first — they may already be installed.
- Check for any configured MCP servers.

## Decision flow

```
Existing email/Slack/messages access detected?
├── Yes → recommend it first. Confirm scope, go to collection.
└── No  → offer setup options (ranked by least effort for this user):
          • Gmail via gogcli      (references/gmail-gogcli.md)
          • Gmail via gws          (references/gmail-googleworkspace-cli.md)
          • Local email export     (references/local-email-exports.md)
          • Local iMessage (macOS) (references/imessage-macos.md)
          • Slack MCP/API          (references/slack.md)
          • Other local corpora    (references/generic-corpora.md)
```

## When access is partial or missing

- If only one source is reachable, use it — a single-source guide is still useful and can be refreshed later.
- If a tool exists but isn't authenticated, offer to walk the user through auth (see the relevant reference file) rather than abandoning the path.
- Never block on a single vendor. There is always a fallback: the user can paste samples directly (`references/generic-corpora.md`).
