# Ghostwriter

**Teach your agent how to write like you.**

Your agent already writes well. It just doesn't write like *you*. Ghostwriter fixes that. It studies the messages you've actually sent and turns them into a style guide your agent uses to draft in your voice.

```
Generic AI                          You, via Ghostwriter
──────────                          ────────────────────
"I hope this email finds you        "hey, quick one. did the
well! I wanted to circle back        contract ever get signed?
regarding the contract. Please       no rush, just closing tabs."
let me know at your earliest
convenience. Thanks so much!"
```

Same intent. One of them is yours. Once your guide is in place, agent-written drafts should feel spooky good.

## Quickstart

```bash
# 1. Install (one clone covers most agents; see "Install" below)
git clone https://github.com/joshferrara/ghostwriter.git ~/.claude/skills/ghostwriter
```

```
# 2. Build your guide (just talk to your agent)
"Build my Ghostwriter guide from my sent email."

# 3. Use it
"Draft a reply to this client in my voice."
```

That's it. Step 2 walks you through picking a source and confirming privacy; step 3 reads the guide and drafts. The rest of this README is the details behind those three lines.

## Why

Most AI writing has the same tells: inflated significance, "I hope this helps!", forced rule-of-three, and a flat, sourceless cadence. You can spot it in a second, and so can everyone you write to.

Generic "humanizing" advice strips those tells, but it pushes everything toward the *same* neutral human voice. That's not you either. You have specific habits: the way you open, the sign-off you actually use, whether you reach for em dashes or emoji, how blunt you get when you're in a hurry.

Ghostwriter inverts the priority. It learns your voice from your sent messages and writes that first. Only then does it run a light cleanup pass for AI artifacts, and that pass never overwrites what makes your writing yours.

## How it works

Point it at your sent messages → it writes a style guide → your agent drafts as you. Two modes do the work:

- **Generate mode** analyzes writing you've actually sent (email, texts, Slack, exports) and produces a standalone style guide, usually `ghostwriter-guide.md`.
- **Use mode** loads that guide and drafts or edits in your voice, treating your personal style as the primary authority.

```
GENERATE                                   USE
─────────                                  ───
detect existing access  ─┐                 find your guide
select source(s)         │                 read it
confirm privacy          ├─► ghostwriter-   gather missing context
collect SENT messages    │    guide.md  ──► draft in your voice
analyze 17 dimensions    │                 humanizer cleanup (secondary)
write the guide         ─┘                 deliver
```

### Generate mode

Triggers when you ask to **create, generate, build, update, refresh, or improve** your Ghostwriter guide. The agent walks you through:

1. **Source detection.** Checks what your agent environment can already reach (connectors, MCP servers, plugins, built-in tools) *before* suggesting new setup.
2. **Source selection.** You pick one or more sources; tradeoffs explained briefly.
3. **Privacy confirmation.** You approve exactly what gets read (sent messages only).
4. **Collection.** Pulls your sent writing and filters out forwards, transactional mail, signatures, tapbacks, and boilerplate.
5. **Analysis.** Characterizes your voice across 17 dimensions (see below).
6. **Guide creation.** Writes `ghostwriter-guide.md`, a standalone artifact you can paste into any agent.

The 17 dimensions group roughly into:

- **Voice:** high-level personality, warmth vs. directness, humor, hedging.
- **Structure:** default shape and length, openings, closings, formatting habits.
- **Mechanics:** sentence style, tone markers (exclamation points, emoji, "haha" vs "lol"), word choice.
- **Situations:** how you make asks, give feedback, handle technical detail, text vs. email, and shift across personal/work/client contexts.
- **Guardrails:** the failure modes — ways you *don't* sound, and tics not to overuse.

### Use mode

Triggers when you ask the agent to **write, draft, reply, rewrite, edit, polish, or humanize** something in your voice. The agent:

1. Finds your guide (`ghostwriter-guide.md`, `write-like-me.md`, `style-guide.md`, or a path you give it).
2. Reads it before drafting.
3. Asks only for missing audience/context details.
4. Drafts in your voice first.
5. Runs a secondary Humanizer cleanup pass, but only where it doesn't conflict with your guide.
6. Delivers, preserving your normal polish, warmth, brevity, punctuation, and formatting.

If no guide is found, it offers to run Generate mode or use one you paste in.

## What you get

The output is a single readable markdown file: your voice, written down. A slice of one looks like:

```markdown
# Alex's Writing Style Guide

## Openings
- "Hey [Name]!" — warm, internal, the default
- "Hi all," — broader or more formal threads
Usually adds a one-line warmth note before the ask.

## Tone mechanics
- Exclamation points: frequent, but one at a time. Never "!!".
- Emoji: 🙏 and 😅 in chat; almost never in client email.

## What to avoid
Do not write Alex as stiff, salesy, or buzzword-heavy.
Don't open with "I hope this finds you well."
```

It ends with a dense **"Quick prompt for an agent"** paragraph. Drop that one paragraph into any tool and it can draft a believable message with nothing else.

## Data sources it can work with

Ghostwriter never requires a single vendor. It uses whatever fits:

| Source | Setup | Reference |
| --- | --- | --- |
| Existing connector / MCP / plugin / built-in tool | none (preferred) | [`references/source-detection.md`](references/source-detection.md) |
| Gmail via `openclaw/gogcli` | `gog` CLI | [`references/gmail-gogcli.md`](references/gmail-gogcli.md) |
| Gmail via `googleworkspace/cli` | `gws` CLI | [`references/gmail-googleworkspace-cli.md`](references/gmail-googleworkspace-cli.md) |
| Local sent email export (`.mbox` / `.eml`) | export to disk | [`references/local-email-exports.md`](references/local-email-exports.md) |
| Local iMessage (macOS) | Full Disk Access | [`references/imessage-macos.md`](references/imessage-macos.md) |
| Slack (MCP or API) | connector or token | [`references/slack.md`](references/slack.md) |
| Text / JSON / CSV / pasted samples | none | [`references/generic-corpora.md`](references/generic-corpora.md) |

For Gmail, both `openclaw/gogcli` and `googleworkspace/cli` are first-class options. Pick whichever you prefer.

## Install

Ghostwriter follows the open [Agent Skills](https://agentskills.io) standard: a folder with a `SKILL.md`. Most agents install a skill by cloning the repo into their skills directory. **Keep the folder named `ghostwriter`**, since the standard requires the folder name to match the skill's `name`.

### Per agent

**Claude Code.** Clone into your personal (or project) skills directory:
```bash
git clone https://github.com/joshferrara/ghostwriter.git ~/.claude/skills/ghostwriter
```

**Codex**
```bash
git clone https://github.com/joshferrara/ghostwriter.git ~/.agents/skills/ghostwriter
```

**Cursor.** Open Settings → Rules → Add Rule → **Remote Rule (GitHub)** and paste the repo URL. Or clone manually:
```bash
git clone https://github.com/joshferrara/ghostwriter.git ~/.cursor/skills/ghostwriter
```

**OpenCode**
```bash
git clone https://github.com/joshferrara/ghostwriter.git ~/.config/opencode/skills/ghostwriter
```

**OpenClaw** has a first-class GitHub installer:
```bash
openclaw skills install git:joshferrara/ghostwriter
```

**Hermes**
```bash
git clone https://github.com/joshferrara/ghostwriter.git ~/.hermes/skills/ghostwriter
```

> **One clone, many agents.** Claude Code, Cursor, and OpenCode all also scan `~/.claude/skills/`, and Codex, Cursor, OpenCode, and OpenClaw all scan `~/.agents/skills/`. Cloning into one of those two paths covers several agents at once.

### Universal fallback (any agent)

If your agent doesn't have a skills system, clone the repo anywhere and tell the agent:

> "Read `SKILL.md` in this repo and follow it."

It's plain markdown with progressive disclosure, so the agent reads the reference files it needs.

### No skill needed at all

If you already have a `ghostwriter-guide.md`, you don't need the skill. Paste the guide into any agent and ask it to write in your voice. That's the whole point of the standalone artifact.

## Use

Once installed, just talk to your agent:

> "Build my Ghostwriter guide from my sent email." *(Generate)*
>
> "Draft a reply to this client in my voice." *(Use)*

## What's in the repo

```
ghostwriter/
├── SKILL.md                              # the portable two-mode skill
├── agents/
│   └── openai.yaml                       # optional Codex/OpenAI UI metadata
├── README.md                             # this file
├── templates/
│   └── ghostwriter-guide.template.md     # output template for the personal guide
├── references/                           # 9 source- and task-specific guides
│   │                                     #   (source detection, Gmail, iMessage,
│   │                                     #    Slack, exports, analysis, humanizer…)
│   └── …
├── scripts/                              # optional, for repeatable local parsing
│   ├── parse_mbox.py                     # extract clean sent text from .mbox/.eml
│   └── sample_corpus.py                  # normalize text/json/csv corpora
└── LICENSE · NOTICE.md · THIRD_PARTY_NOTICES.md · VALIDATION.md
```

## Privacy

- The agent reads only the sources you confirm, and only your sent messages.
- Your generated guide stores patterns, summaries, and synthetic examples written in your style, not your raw private messages, unless you explicitly ask to include real quotes.
- Local sources (exports, iMessage, pasted samples) are not uploaded anywhere else by this skill, but they are still processed by the current agent/runtime. CLI and connector sources may contact their normal service to fetch messages. Hosted agents process prompts/files according to that provider's privacy terms.

## Personal voice vs. Humanizer

Your guide is the primary authority. [Humanizer](https://github.com/blader/humanizer) is incorporated only as a secondary cleanup pass to remove common AI-writing artifacts, and only where it doesn't conflict with your guide. If your guide says you use em dashes, exclamation points, or emoji, those stay. Ghostwriter removes slop you wouldn't write; it doesn't flatten you into a generic "human" voice.

## Attribution & license

- Ghostwriter is released under the [MIT License](LICENSE).
- The Humanizer cleanup pass adapts ideas from [`blader/humanizer`](https://github.com/blader/humanizer) (MIT, Copyright (c) 2025 Siqi Chen). See [`THIRD_PARTY_NOTICES.md`](THIRD_PARTY_NOTICES.md).
