# Pass 1 rules library: words, sentences, formats

The reading layer of pass 1. `scripts/banned-pattern-scan.py` catches what a regex can catch; this file covers what it cannot. Read it during pass 1 step 3.

Two things live elsewhere and are not repeated here. The banned WORDS are in `scripts/banned-words.txt`, which the scanner reads directly, so there is one list and no second copy to drift. The banned PATTERNS are in the `PATTERNS` list inside the scanner. This file adds the before-and-after examples for the patterns, the soft guidance no scanner can judge, the positive principles, and the per-format rules.

---

## Banned sentence patterns, with the fix

The scanner flags most of these. The examples are what tell you how to fix one, and the fix is always a rewrite of the sentence, never a synonym swap.

### 1. "Not just X, but Y"
Straining to sound bigger than the thing is. State what it actually does.
- Bad: "Not just a CRM, but a revenue engine."
- Good: "Closes deals in half the steps."

### 2. "More than X" constructions
Defines by comparison to something vague. State what it is.
- Bad: "More than a platform: it's a growth partner."
- Good: "Runs your outreach, tracks your pipeline, and flags deals going cold."

### 3. Defining by negation
Saying what something is not, to imply what it is.
- Bad: "This isn't your typical agency."
- Good: "We build paid campaigns, run them, and hand you the playbook when we leave."

### 4. "That" relative clauses
Do not write "a tool that does X" or "a platform that connects to Y". State the action.
- Bad: "A platform that connects your entire stack."
- Good: "Connects your entire stack."
- Exception: keep "that" when removing it makes the sentence awkward.

### 5. Self-congratulatory claims without proof
No claim of being best, leading, trusted, or innovative without a number or a name attached.
- Bad: "Trusted by thousands of businesses."
- Good: "Used by 4,200 teams across 30 countries."
- Bad: "Industry-leading support."
- Good: "Median response time: 4 minutes."

### 6. Aspirational filler
Every sentence describes something concrete and real. Delete any sentence whose removal would not change the meaning around it.
- Bad: "We believe in building tools that make work feel human again."
- Good: delete it, or replace it with a specific product claim.

### 7. Em dashes as connectors
Restructure, or use a colon or a period.
- Bad: "It's fast — and it's free."
- Good: "It's fast and free." Or: "Fast. Free."

---

## Patterns to minimise (soft guidance, no scanner covers these)

Not hard bans. Each appears in good writing occasionally. The problem is frequency and default reach: AI uses them constantly. Prefer the alternative, and use the original only when it genuinely serves the sentence.

### 1. Transition word bloat
Words that pretend to connect ideas and usually add padding: "Furthermore", "Moreover", "Additionally", "In addition", "It's worth noting", "That said", "With that in mind".
- Prefer: a period. Let the next sentence stand on its own.
- Fine when: sequence or contrast genuinely needs signposting. Once per piece, not once per paragraph.

### 2. Question hook openers
"Have you ever wondered...?", "What if there was a better way?", "Did you know...?"
- Prefer: state the insight. "Most X fail because of Y" is stronger than any question.
- Fine when: the piece is conversational and the question is genuine and specific, not rhetorical.

### 3. "In today's X" openers
"In today's competitive landscape...", "In today's fast-moving world..."
- Prefer: start with the specific problem or observation. Skip the scene-setting.
- Fine when: the time context is genuinely the point of the sentence. Rare.

### 4. Fake intimacy phrases
"The truth is...", "Here's the thing...", "I'll be honest with you...", "Let me tell you something...", "Real talk:"
- Prefer: say the thing. If it is true, the words carry it without an announcement.
- Fine when: genuinely shifting tone in a piece where warmth fits.

### 5. "Simply" and "just" as minimizers
"Simply follow these steps", "Just click the button", "It's that simple."
- Prefer: remove the word. The instruction is cleaner without it.
- Fine when: the thing genuinely is simple and the word reassures rather than condescends.

### 6. "Whether you're X or Y"
"Whether you're a startup or an enterprise...", "Whether you're a beginner or an expert..."
- Prefer: pick one audience and speak to them. Specificity beats inclusivity.
- Fine when: you genuinely need to address two distinct segments in one piece.

### 7. Symmetrical bullet structure
Every bullet the same length, same grammatical form, same rhythm. It reads as machine-generated.
- Prefer: vary length deliberately. Some bullets are one word. Some are two sentences. Let the content drive the form.

### 8. Recap and restate
Summarising what was just said at the end of a section: "Key takeaway:", "In summary:", "To recap:".
- Prefer: end where the content ends. If the point landed, repeating it adds nothing.
- Fine when: long educational content where signposting genuinely helps navigation.

### 9. Gerund headline openers
"Introducing...", "Building...", "Delivering...", "Helping businesses..."
- Prefer: state the outcome or the subject. "Cuts your reporting time in half" beats "Delivering faster reporting."
- Fine when: the gerund is genuinely the most direct form. Rare.

### 10. Exclamation marks in professional copy
"We're thrilled to announce!", "Get started today!"
- Prefer: if the thing is genuinely exciting, the words carry the energy.
- Fine when: consumer-facing, social, or high-energy short-form copy where the tone matches the medium.

---

## Positive writing principles

What to do, not only what to avoid.

**Lead with the outcome, not the feature.**
- Bad: "Real-time sync across all your devices."
- Good: "Pick up where you left off on any device, instantly."

**One sentence, one idea.** Long sentences with stacked clauses are harder to read and easier to skip. Break them.

**Short is not lazy, it is skilled.** If a sentence can be cut without losing meaning, cut it. If a paragraph can be one sentence, make it one sentence.

**Concrete beats abstract, every time.** Replace abstract claims with specific numbers, names, or actions.
- Abstract: "Saves you time."
- Concrete: "Cuts reporting from 2 hours to 15 minutes."

**Active voice.**
- Bad: "Results are tracked automatically."
- Good: "Tracks results automatically."

**Grade 8 reading level or below for consumer copy, Grade 10 for B2B.** Short words, short sentences, real words over jargon.

**Show the before and after.** The most persuasive copy describes the world before the product, then after. Make the contrast visible.

---

## Format-specific rules

### Social post
- The first line is the hook and has to earn the scroll stop. No "I'm excited to share."
- Use line breaks. Do not thread everything into one block.
- One idea per post. End on a point, not a question fishing for engagement.
- No hashtag spam. Two at most, at the end, only when relevant.
- Direct, first person, specific. Write as if talking to one person.

### Email, cold or nurture
- Subject line specific, not clever. "Question about X" beats "The future of marketing."
- First sentence about them, not about you.
- One ask per email. One call to action, never two.
- Plain text outperforms HTML for cold outreach.
- Cold: under 100 words. Nurture: under 200 unless it is a deep educational piece.

### Landing page
- Hero headline: what it does and who it is for. Eight words maximum.
- Subheadline: the single strongest proof or benefit. One sentence.
- Above the fold: one call to action, no secondary options.
- Social proof as close to the call to action as possible.
- Every section answers one objection. Know the objection before writing the section.

### Blog post
- Title: specific, useful, searchable. Not clever. Says exactly what the reader gets.
- Intro: the problem, then what this post solves. Two sentences. No scene-setting.
- H2s as signposts: someone reading only the H2s should understand the structure.
- Ending: one takeaway and one action, not a summary.

### Ad copy
- Headline: the promise or the problem. Nothing else.
- Body: proof or mechanism. One sentence.
- Call to action: verb plus outcome. "Start free", not "Learn more".

---

## Self-check before returning any draft

1. Any word from `scripts/banned-words.txt`. Replace every instance.
2. Any banned sentence pattern. Rewrite every instance.
3. Any sentence over 25 words. Break it.
4. Any abstract claim with no specific proof point. Replace or delete.
5. Any em dash. Remove.
6. Any sentence that could be deleted without changing meaning. Delete it.

Fix, then recheck. Return only when all six pass.

---

## Quotations are immutable

Everything above applies to first-person original writing. Verbatim third-party text is exempt: testimonials, quotes, reviews, transcripts, press blurbs. Never rewrite someone's words to fit a style guide, even when they contain a banned word. Keep the quote as written, or cut it entirely, and surface the conflict rather than silently editing it. Swapping synonyms inside a quote puts words in the source's mouth they did not say.
