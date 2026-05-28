# Analysis framework

How to turn a cleaned set of sent messages into a high-quality, immediately usable style guide. The goal is **concrete, reusable patterns** an agent can act on — not vague adjectives.

## Mindset

- Describe what the user *does*, with their actual words, not what their writing is "like."
- "Opens emails with 'Hey [Name]!' and a one-line warmth note" beats "friendly and approachable."
- Quantify where you can: median length, how often they use exclamation points, typical number of bullets.
- Separate contexts. Long-form (email, client updates) and short-form (texts, Slack) are different voices. Keep them distinct.
- Prefer **synthetic examples written in the user's style** over quoting their private messages. Quote real messages only if the user explicitly asks.

## Dimensions to extract

Work through each. Skip any a source can't support, and note where contexts differ.

1. **High-level voice** — the 3–5 sentence personality of the writing. Warm? Direct? Playful? Precise? Who does this person sound like at their desk?
2. **Default shape & length** — median and typical range of message length, by context. Paragraph length. When do they use lists?
3. **Openings** — exact greetings they use, and when ("Hey [Name]!" for warm/internal, "Hi all," for broader). Do they add a warmth line after the greeting?
4. **Closings** — exact sign-offs and their gratitude/openness habits. Do they offer help? Sign with a name?
5. **Sentence style** — contractions, sentence rhythm, favored transitions, softeners ("I wanted to check", "could we", "just want to make sure").
6. **Tone mechanics** — exclamation points (how often, how many at once), smileys/emoji (which, in what contexts), "haha" vs "lol", elongated words, standalone reaction words.
7. **Formatting habits** — bullets vs. prose, numbered lists, bold labels, links, how scannable. Ornate markdown or plain?
8. **Humor & personality** — where humor appears (aside, smiley, phrase), how often, what kind. What they never do (sarcasm? forced jokes?).
9. **Technical specificity** — how they handle technical detail. Do they name tools/APIs, then translate to practical impact? How deep before they zoom out to the reader's concern?
10. **Warmth & directness** — how quickly they get to the point; how much relational padding; the balance of courtesy and precision.
11. **Uncertainty / hedging** — how they express not knowing ("I'm not really sure", "it seems like maybe"). Honest hedging vs. confident.
12. **How they make asks** — specific and courteous? Do they explain why the ask matters? What phrasings recur?
13. **Feedback style** — how they raise concerns or critique. Gentle framing? Issue → reason → suggested fix?
14. **Text-message behavior** — reaction openers, fragments, multi-send habits, punctuation drops, emoji. (From iMessage/Slack sources.)
15. **Context-specific differences** — personal vs. work vs. client-facing vs. family/school. Where does the voice shift, and how?
16. **Word choice** — a concrete list of words and phrases the user reaches for repeatedly. These are gold for an agent.
17. **What to avoid** — the failure modes: ways the user does NOT sound (stiff, salesy, snarky, academic, buzzword-heavy), and tics to not overuse.

## Method

1. Read a representative sample across contexts. Don't skim — patterns hide in specifics.
2. Tally recurring openings, closings, softeners, and favorite words. Frequency matters more than presence.
3. Estimate lengths (median + typical range) per context.
4. Note the failure modes — what's conspicuously absent (no corporate-speak? no semicolons in texts?).
5. Draft each section of the guide from the patterns, writing **synthetic examples** in the user's voice to illustrate. Mark examples as patterns, not quotes (e.g. "Example pattern, not a quote:").
6. Add the **Quick prompt for an agent** — one dense paragraph capturing the whole voice, written so an agent could draft a believable message from that paragraph alone.
7. Add the **Humanizer compatibility** section (personal voice primary, Humanizer secondary). Use the boilerplate in `templates/ghostwriter-guide.template.md`.

## Quality bar

A good guide:

- lets an agent draft a believable message in each context without further questions,
- names specific words, greetings, and sign-offs rather than describing them abstractly,
- distinguishes short-form from long-form voice,
- includes a usable "Quick prompt for an agent",
- states clearly that the personal voice overrides generic humanizing rules,
- contains no raw private quotes unless the user asked for them.
