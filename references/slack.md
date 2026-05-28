# Slack (MCP or API)

Slack captures the user's **workplace chat voice** — usually more casual than client email, more structured than texts, often with team-specific shorthand. Use it when the user works primarily in Slack.

## Preferred: existing Slack access

If `references/source-detection.md` found a Slack connector, MCP server, or app integration already wired into the agent, use it. That's the least setup. You typically want a tool that can:

- search or list messages **authored by the user** (their own sent messages)
- read message text from channels and DMs the user chooses

Filter to the user's own messages only. With a Slack MCP, that usually means searching with a `from:@me` / `from:<userID>` filter or reading the user's profile ID first and filtering client-side.

## Setup option: Slack Web API

If nothing is connected, the user can create a token:

1. Create a Slack app at https://api.slack.com/apps (or use a user token from an existing app).
2. Add user-token scopes: `search:read` (search own messages), `channels:history`, `groups:history`, `im:history`, `users:read`.
3. Install to the workspace and copy the **User OAuth Token** (`xoxp-...`).

```bash
export SLACK_TOKEN=xoxp-...

# Find your own user ID
curl -s -H "Authorization: Bearer $SLACK_TOKEN" \
  "https://slack.com/api/auth.test" | jq '.user_id'

# Search your own recent messages (search.messages requires a user token)
curl -s -H "Authorization: Bearer $SLACK_TOKEN" \
  "https://slack.com/api/search.messages?query=from:@me&count=100&sort=timestamp" \
  | jq '.messages.matches[] | {ts, text, channel: .channel.name}'
```

`search.messages` is only available with a user token (not bot tokens) and on paid plans. If it isn't available, fall back to reading specific channels with `conversations.history` and filtering to `"user" == <your id>`.

## What to keep / drop

- Keep only messages authored by the user.
- Drop link-only posts, `/command` invocations, and bot-triggered messages.
- Strip Slack markup where it's noise (`<@U123>` mentions → "@name" or omit; `<http://…|text>` → `text`).
- Threaded replies count — they often show the user's quick-response voice.

## How this feeds the guide

Treat Slack as its own context in `references/analysis-framework.md`: greeting habits (or lack of them), emoji/reaction use, thread etiquette, how the user gives quick feedback or status updates, and how formal they get when a message is cross-team vs. within their own squad. Keep it distinct from email and texting voice in the final guide.

## Troubleshooting

- `not_allowed_token_type` on search → you're using a bot token; `search.messages` needs a user token.
- `missing_scope` → add the scope listed in the error and reinstall the app.
- No API access possible → ask the user to paste 30–50 representative Slack messages (`references/generic-corpora.md`).
