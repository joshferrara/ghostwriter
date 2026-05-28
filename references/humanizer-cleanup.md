# Humanizer cleanup pass (secondary)

A final review pass that strips common **AI-writing artifacts** from a draft. It runs *after* the draft already sounds like the user.

> **This is a guardrail, not a voice.** The user's personal Ghostwriter guide is the primary authority. Apply any rule here **only where it does not conflict with the guide.** If the guide says the user uses em dashes, exclamation points, emoji, the rule of three, or any other pattern below, that is their voice — keep it. Never flatten a specific personal style into generic "human" prose.
>
> Adapted from [`blader/humanizer`](https://github.com/blader/humanizer) (MIT, Copyright (c) 2025 Siqi Chen), which is based on [Wikipedia: Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing). See `THIRD_PARTY_NOTICES.md`.

## Contents

- How to run the pass
- Content patterns (1–6)
- Language & grammar patterns (7–13)
- Style patterns (14–19)
- Communication patterns (20–22)
- Filler & hedging (23–30)
- What NOT to "fix" (false positives & signs of real human writing)

## How to run the pass

1. Confirm the draft already matches the personal guide (voice, openings, length, formatting).
2. Scan for the patterns below. They are most damning in **clusters** — one em dash means nothing; em dashes + rule-of-three + "vibrant tapestry" + a "Conclusion" section is a confession.
3. For each hit, check the guide. If the user genuinely writes that way, leave it. Otherwise rewrite into the user's natural phrasing — not a generic neutral one.
4. Audit: ask "what still makes this sound AI-generated?" and fix what remains.
5. Re-read once. The draft should still sound like the user, just without the tells.

## Content patterns

**1. Inflated significance, legacy, broader trends.** "stands/serves as a testament", "plays a pivotal/crucial/vital role", "marks a pivotal moment", "underscores its importance", "reflects a broader", "in today's evolving landscape", "setting the stage for". Puffing up importance by tying an ordinary detail to some grand trend. Cut it; state the plain fact.

**2. Undue emphasis on notability/media coverage.** "has been featured in", "garnered widespread attention", "maintains an active social media presence", listing outlets without context. Replace with one specific, sourced fact.

**3. Superficial "-ing" analyses.** Trailing present-participle clauses that fake depth: "…, highlighting its significance", "…, ensuring seamless integration", "…, reflecting the community's deep connection", "…, showcasing how…". Delete the clause or turn it into a concrete statement.

**4. Promotional / advertisement language.** "boasts a", "vibrant", "rich (figurative)", "nestled", "in the heart of", "breathtaking", "must-visit", "renowned", "stunning", "commitment to". Neutralize to plain description.

**5. Vague attributions & weasel words.** "industry reports", "observers have noted", "experts argue", "some critics say", "several sources" (when none are named). Name the source or drop the claim.

**6. Formulaic "Challenges and Future Prospects" sections.** "Despite its… faces several challenges…", "Despite these challenges…", "Future Outlook". Replace with specific facts, or cut the section.

## Language & grammar patterns

**7. Overused AI vocabulary.** delve, intricate/intricacies, crucial, pivotal, underscore, tapestry, testament, landscape (abstract), realm, foster, garner, showcase, enhance, leverage, robust, seamless, vibrant, interplay, align with, additionally, moreover. These cluster together. Swap for plain words the user would actually use.

**8. Copula avoidance.** "serves as", "stands as", "boasts", "features", "represents" where "is/are/has" is truer. Prefer the simple copula.

**9. Negative parallelism & tailing negations.** "It's not just X, it's Y", "not only… but also…", and clipped fragments tacked on the end ("no guessing", "no wasted motion"). Rewrite as a real clause.

**10. Rule-of-three overuse.** Forcing ideas into groups of three to sound comprehensive ("innovation, inspiration, and insight"). Keep only the items that are real; two or four is fine.

**11. Elegant variation (synonym cycling).** Renaming the same thing every sentence (the protagonist → the main character → the central figure → the hero). Pick one term and repeat it.

**12. False ranges.** "from X to Y" where X and Y aren't on a real scale ("from the Big Bang to dark matter"). Replace with a plain list.

**13. Passive voice / subjectless fragments.** "No configuration needed.", "The results are preserved automatically." Name the actor when active voice is clearer ("You don't need a config file.").

## Style patterns

**14. Em dashes and en dashes.** A reliable AI tell when stacked with other tells. **If the personal guide says the user uses them, keep them.** Otherwise replace, in rough order of preference: period, comma, colon, parentheses, or restructure. Also catch spaced em dashes (` — `) and double hyphens (` -- `).

**15. Mechanical boldface.** Bolding phrases for no reason. Remove unless the bold genuinely aids scanning (and the guide allows it).

**16. Inline-header vertical lists.** `- **Thing:** sentence restating Thing.` Flatten into prose or plain bullets unless the user really writes this way.

**17. Title Case In Headings.** Use sentence case unless the guide says otherwise.

**18. Decorative emoji on headings/bullets.** Remove emoji used as ornaments. **Keep emoji the user actually uses** in chat/texts per the guide.

**19. Curly quotes.** If the user types straight quotes, normalize curly quotes to straight (and vice versa). Alone, this is a weak signal — many editors auto-curl.

## Communication patterns

**20. Collaborative chatbot artifacts.** "I hope this helps!", "Certainly!", "Of course!", "Great question!", "Would you like…", "Let me know if…", "Here is a…" pasted into content. Remove.

**21. Knowledge-cutoff disclaimers & speculative gap-filling.** "as of my last update", "while specific details are limited", "based on available information", "maintains a low profile", "keeps personal details private", "it is believed that", "likely grew up…". Say what isn't known, or cut the sentence — don't dress a guess as fact.

**22. Sycophantic / servile tone.** "You're absolutely right!", "That's an excellent point", over-eager agreement. Strip it back to substance.

## Filler & hedging

**23. Filler phrases.** "in order to" → "to"; "due to the fact that" → "because"; "at this point in time" → "now"; "in the event that" → "if"; "has the ability to" → "can"; "it is important to note that the data shows" → "the data shows".

**24. Excessive hedging.** "it could potentially possibly be argued that it might…" → say it plainly. (Keep the user's *genuine* hedging if the guide notes they hedge — honest uncertainty is a real voice trait.)

**25. Generic positive conclusions.** "The future looks bright.", "Exciting times lie ahead.", "a major step in the right direction." Replace with a concrete next fact, or end where the content ends.

**26. Hyphenated word-pair overuse.** "third-party", "data-driven", "cross-functional", "high-quality", "real-time", "end-to-end". Keep the hyphen in attributive position ("a high-quality report"); drop it after the noun ("the report is high quality"). Humans hyphenate inconsistently; AI does it uniformly.

**27. Persuasive-authority tropes.** "the real question is", "at its core", "what really matters", "fundamentally", "the deeper issue". Ceremony in front of an ordinary point. Cut to the point.

**28. Signposting / announcements.** "Let's dive in", "let's explore", "here's what you need to know", "without further ado". Just do the thing instead of announcing it.

**29. Fragmented headers.** A heading followed by a one-line sentence that just restates the heading before the real content. Delete the restatement.

**30. Diff-anchored writing.** Docs/comments written as if narrating a change ("This was added to replace the old approach…") in a document that isn't a changelog. Describe the thing as it is.

## What NOT to "fix"

Check the guide before touching any of these — they are often the user's real voice or signs of genuine human writing, and over-editing destroys what makes the writing theirs.

**Likely the user's voice (keep if the guide lists them):**
- Exclamation points, smileys, "haha", "y'all", elongated words, standalone reactions.
- Em dashes, if the user uses them.
- Sentence fragments and dropped end punctuation in texts — that's the short-form voice.
- Domain vocabulary the user genuinely uses (tool names, APIs, scopes). Don't dumb it down.

**Signs of real human writing (preserve):**
- Specific, hard-to-fabricate detail (a real address, an odd quote). LLMs round specifics off; humans hoard them.
- Mixed feelings and unresolved tension ("mostly good, but it bugs me and I can't say why").
- Dated, era-bound references and in-jokes.
- Genuine asides, parentheticals, and self-corrections.
- Natural variety in sentence length.

**Weak signals — don't flag alone:** perfect grammar, formal vocabulary, a single "however", curly quotes, one em dash, an unsourced claim. Only act when tells **cluster**.

When in doubt, the personal guide wins. The point of this pass is to remove slop the user wouldn't write — not to make every output sound generically "human."
