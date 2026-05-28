# Validation checklist

A short way to confirm both modes work, end to end. Run these against any agent that can load `SKILL.md`. No real private data is required — the corpus/paste steps work with sample text.

## Setup

- [ ] The agent can see `SKILL.md` (placed in its skills directory, or pointed at it directly).
- [ ] The agent loads Ghostwriter when you use a trigger word (see below).

## Generate mode

1. **Trigger & routing**
   - [ ] Say: *"Build my Ghostwriter guide."* The agent enters **Generate mode** (not Use mode).
2. **Source detection first**
   - [ ] The agent first checks for existing access (connector / MCP / plugin / built-in tool) **before** proposing new setup. (See `references/source-detection.md`.)
3. **Source selection**
   - [ ] The agent offers source options and, for Gmail, names **both** `openclaw/gogcli` and `googleworkspace/cli`.
   - [ ] If a tool/source is unavailable, it offers an alternative instead of dead-ending.
4. **Privacy**
   - [ ] The agent states privacy expectations and asks you to confirm which sources to analyze before reading anything.
5. **Collection (sample path)**
   - [ ] Provide a small corpus (paste ~20–40 sample messages, or run `scripts/sample_corpus.py` / `scripts/parse_mbox.py` on a test file).
   - [ ] The agent filters out forwards, transactional/automated messages, signatures, tapbacks, link-only, and boilerplate.
6. **Analysis & guide creation**
   - [ ] The agent produces `ghostwriter-guide.md` modeled on `templates/ghostwriter-guide.template.md`.
   - [ ] The guide covers tone, length, openings, closings, formatting, humor, technical specificity, warmth, directness, hedging, asks, feedback, texting behavior, and context differences.
   - [ ] It ends with a **"Quick prompt for an agent"** paragraph.
   - [ ] It has a **Humanizer compatibility** section stating the personal voice is primary and Humanizer is a secondary pass.
   - [ ] It contains **no raw private quotes** (only synthetic examples) unless you explicitly asked otherwise.
7. **Standalone check**
   - [ ] Paste `ghostwriter-guide.md` alone into a fresh agent session (no skill loaded) and confirm it can draft a believable message from the guide by itself.

## Use mode

1. **Trigger & routing**
   - [ ] With a `ghostwriter-guide.md` present, say: *"Draft a reply to this in my voice: …"* The agent enters **Use mode**.
2. **Guide discovery & read**
   - [ ] The agent finds the guide (`ghostwriter-guide.md` / `write-like-me.md` / `style-guide.md` / a path you give) and reads it before drafting.
   - [ ] With **no** guide present, the agent says so and offers to run Generate mode or use one you paste — it does **not** silently write generically.
3. **Context gathering**
   - [ ] The agent asks only for missing audience/context details, not things the guide already covers.
4. **Draft in voice first**
   - [ ] The draft matches the guide's openings, closings, length, punctuation, and formatting for the right channel (e.g. it doesn't force email structure into a text).
5. **Secondary Humanizer pass**
   - [ ] The agent removes AI artifacts (e.g. "I hope this helps!", inflated significance) **without** stripping voice markers the guide says you use (em dashes, exclamation points, emoji, etc.).
   - [ ] Where the cleanup pass and the guide conflict, the **guide wins**.
6. **Delivery**
   - [ ] Output preserves your normal level of polish, warmth, brevity, and directness — not a generically "human" flattening.

## Scripts (optional)

- [ ] `python3 scripts/parse_mbox.py <fixture.mbox> --out out.jsonl` extracts clean sent text (quoted history / signatures / link-only dropped).
- [ ] `python3 scripts/parse_mbox.py <Apple Mail export .mbox package> --out out.jsonl` extracts messages from the package's internal `mbox` file instead of returning zero rows.
- [ ] `python3 scripts/sample_corpus.py <fixture> --format text|jsonl|json|csv --out out.jsonl` normalizes and de-duplicates a corpus.
- [ ] `python3 scripts/sample_corpus.py <chat fixture> --format text --keep-short --out out.jsonl` preserves short reactions/fragments used for text/chat voice analysis.

## Licensing / attribution

- [ ] `LICENSE` (MIT) is present for Ghostwriter.
- [ ] `THIRD_PARTY_NOTICES.md` includes Humanizer's MIT license, URL, and copyright (Siqi Chen, 2025).
- [ ] The repo states Humanizer is a secondary guardrail, not the primary voice source.
