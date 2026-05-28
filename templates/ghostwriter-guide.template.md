<!--
GHOSTWRITER GUIDE TEMPLATE

This is the output template for Generate mode. Fill every section with concrete,
user-specific patterns drawn from analysis (see references/analysis-framework.md).
Replace the [bracketed guidance] with real content and delete these HTML comments
and any sections that don't apply.

Rules for filling this in:
- Use observed wording patterns: recurring greetings, sign-offs, favorite phrases.
- Quantify where you can (median length, how often exclamation points appear).
- Use SYNTHETIC examples written in the user's voice. Do NOT paste the user's
  real private messages unless they explicitly asked you to.
- Keep short-form (texts/Slack) and long-form (email/client) voices distinct.
- The finished file is a STANDALONE artifact: it must be usable when pasted into
  any agent, with no other files from this skill.
Default filename: ghostwriter-guide.md
-->

# [Name]'s Writing Style Guide

Use this as a practical reference for writing in [Name]'s voice. It is based on analysis of [their sent email / sent iMessages / Slack messages / other sources — list what was actually used] from [rough time period]. Forwarded messages, automated/transactional messages, tapbacks, signatures, quoted threads, and obvious boilerplate were excluded where practical.

> This guide is the **primary authority** on [Name]'s voice. Where any generic writing advice (including AI "humanizing" rules) conflicts with this guide, **follow this guide.** See "Humanizer compatibility" at the end.

## High-level voice

[3–5 sentences: who this person sounds like when they write. The default register. The balance of warmth, directness, precision, and play. Make it specific enough that someone could pick this voice out of a lineup.]

The tone usually lands here:

- [trait — e.g. "Friendly and approachable, especially at the open and close."]
- [trait]
- [trait]
- [trait]

## Default shape & length

[Typical and median length by context. Paragraph length. When lists appear. How long before they get to the point.]

- **Long-form (email / client):** [median ~N words; range; paragraph habits; when bullets/numbers appear]
- **Short-form (texts / chat):** [much shorter; typical word count; multi-send habits; don't force long-form structure here]

Common structure for a longer message:

1. [e.g. Greeting]
2. [e.g. Quick warmth or acknowledgement]
3. [e.g. Main point in plain language]
4. [e.g. Details in bullets / numbered list]
5. [e.g. Clear next step or offer to help]
6. [e.g. Casual thanks]

## Openings

[Exact greetings they use and when to use each.]

- "[greeting]" — [when]
- "[greeting]" — [when]

[Do they add a warmth line after the greeting? Give recurring patterns or synthetic examples, not private quotes.]

## Closings

[Exact sign-offs and closing habits. Do they offer help, sign a name, thank?]

- "[closing]"
- "[closing]"

## Sentence style

[Contractions, rhythm, transitions. The softeners they use when making asks.]

Softeners they reach for:

- "[softener]", "[softener]", "[softener]"

Plain transitions they use:

- "[transition]", "[transition]"

## Tone mechanics

[How warmth shows up. Be specific and bounded.]

Use:

- [e.g. exclamation points — how often, how many at once]
- [e.g. smileys/emoji — which, in what contexts]
- [e.g. "haha" vs "lol"; elongated words; standalone reactions]

Avoid:

- [things that are NOT this voice — corporate polish, salesy excitement, etc.]

## Formatting habits

[Bullets vs prose, numbered lists, bold labels, link handling, how scannable, ornate vs plain markdown.]

## Technical specificity

[How they handle technical detail. Do they name tools/APIs then translate to practical impact? How deep before zooming out to the reader's concern? Include a synthetic example pattern.]

> Example pattern, not a quote:
> [A short synthetic example in the user's voice showing how they explain something technical and tie it to what the reader cares about.]

## Giving feedback or raising concerns

[How they critique. Framing (cleanup/clarity/risk?). Issue → reason → suggested fix? Phrases they use.]

- "[phrase]"
- "[phrase]"

## Asking for help

[How asks are made — specific, courteous, with the reason. Recurring phrasing patterns.]

- "[ask phrasing]"
- "[ask phrasing]"

## Context-specific differences

[How the voice shifts across personal / work / client-facing / family. Where it loosens or tightens.]

- **Personal / family:** [notes]
- **Work / team:** [notes]
- **Client-facing:** [notes]

## Text-message behavior

[If a short-form source was analyzed: reaction openers, fragments, multi-send, punctuation drops, emoji. Keep this clearly separate from email voice.]

- Reaction openers: "[word]", "[word]"
- [punctuation / emoji / length habits]
- Do not overcorrect texts into polished prose. A natural [Name] text can be as short as "[example]".

## Word choice

Words and phrases [Name] reaches for:

- "[phrase]"
- "[phrase]"
- "[phrase]"

[Note any group/audience words like "y'all", "team", "guys" and when each applies.]

## What to avoid

Do not write [Name] as:

- [failure mode — e.g. stiff/executive]
- [failure mode — e.g. salesy]
- [failure mode]

Do not overuse:

- [tic to not lean on]
- [tic]

## Quick prompt for an agent

[One dense paragraph an agent can act on directly. Capture the whole voice: how to open and close per channel, getting to the point, formatting, softeners, warmth markers, and what to avoid. This paragraph alone should let an agent produce a believable draft.]

## Humanizer compatibility

This guide is the **primary** source of voice. Use it first and let it override generic writing advice.

After drafting in [Name]'s voice, run a **secondary** cleanup pass for common AI-writing artifacts (inflated significance, chatbot framing like "I hope this helps!", fake "-ing" depth, forced rule-of-three, copula avoidance, mechanical boldface, signposting, sycophantic tone). Apply that pass **only where it does not conflict with this guide.**

Specifically, **keep** these even though generic "humanizing" rules might flag them, because they are [Name]'s real voice:

- [e.g. exclamation points, smileys, "y'all", em dashes — list whichever apply to this user]

The goal is to remove slop [Name] wouldn't write — not to make every message sound generically "human." When the cleanup pass and this guide disagree, **this guide wins.**

<!-- Humanizer cleanup ideas adapted from blader/humanizer (MIT, (c) 2025 Siqi Chen): https://github.com/blader/humanizer -->
