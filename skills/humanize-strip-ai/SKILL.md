---
name: humanize-strip-ai
description: "Humanize writing by stripping the AI out of it. The single entry point for the anti-AI pass: runs the surface layer (banned words, em dashes, banned sentence patterns, assistant register) then the structural layer (where the point lands, emotion mode, reference specificity, tidy endings, shape repeated across recent pieces). Universal and reusable across everything. Use when asked to humanize, strip AI, de-AI, clean up, or fix writing that reads as machine-made, and before publishing anything outward-facing. Does NOT add personal voice: a voice pass runs after this."
disable-model-invocation: false
user-invocable: true
argument-hint: [paste or path to a draft] OR [surface: pass 1 only] OR [structure: pass 2 only]
---

## Humanize by stripping AI

The one skill for "this reads like AI". It removes machine signal. It does not add voice, and it does not check facts. Those are separate passes that run around it.

**This skill is universal and applies across all contexts and all people.**

---

## Where this sits

```
fact-check   -> is it true?                    (run first: no point polishing a false sentence)
THIS SKILL   -> does it read as AI?            (pass 1 surface, pass 2 structure)
voice        -> does it sound like the author? (runs last: it ADDS signal)
```

Layers 1 and 2 remove signal. The voice layer adds it. Run voice first and this pass strips out the author's real habits. The fact-check and voice passes are separate capabilities; this skill works on its own without either, and the only thing that matters is that a voice pass, if you run one, runs AFTER this.

---

## When invoked

If $ARGUMENTS contains a draft or a path: run both passes and return the corrected draft plus notes.
If $ARGUMENTS starts with "surface": pass 1 only.
If $ARGUMENTS starts with "structure": pass 2 only.
If no arguments: ask for the draft and the channel it is for.

---

## Why both passes exist

Word-level cleanup is the cheap half and the half decaying fastest. StoryScope (Russell et al. 2026, arXiv:2604.03136; 61,608 stories, 10,272 human plus five LLMs) detected AI text at **93.2% macro F1 from narrative structure alone**, with every style feature withheld. Running AI text through a professional span-level rewriter, a very good surface pass, moved detection by **1.6 points**.

The mechanism is convergence. All five models occupy one tight region of structural space while humans are dispersed. **Rarity itself is the signal.** Which produces the central constraint: applying every fix on every piece creates a new detectable cluster. One or two interventions per piece, varied across pieces.

---

# PASS 1: surface

Words, sentences, punctuation. Mechanical and cheap, so it runs first and clears the noise before the structural read.

## Sources of truth (do not copy these lists into other files)

| What | Lives in | Notes |
|---|---|---|
| Banned words (49) | `scripts/banned-words.txt` | One term per line. Edit here, nowhere else, so every scanner reads one list. |
| Banned sentence patterns (25) | `scripts/banned-pattern-scan.py`, `PATTERNS` list | Includes 6 negative-parallelism shapes and 8 assistant-register phrases. |
| Style rules, soft patterns, format rules | your own style guide, if you keep one | Optional. The essentials are inlined in step 3 below, so this skill runs without one. |

## Procedure

1. Run the scanner. It is deterministic and catches what reading misses:
   ```bash
   python3 scripts/banned-pattern-scan.py <file>
   ```
2. Fix every hit by **rephrasing the sentence**, never by swapping a synonym. The pattern flags a structural cliche; a synonym leaves the cliche in place.
3. Apply the baseline style rules: no em dashes, no hype vocabulary, no filler, active voice, one idea per sentence. If you keep your own style guide, apply that too.
4. Check the things a scanner cannot see:
   - **Uniform sentence rhythm.** Real writing varies hard: a three-word sentence next to a thirty-word one. AI holds a steady mid-length everywhere.
   - **Symmetrical structure.** Three bullets of equal length, parallel openings, every section the same shape.
   - **Hedging stacked on hedging.** "It may sometimes be worth considering."

## Quotations are immutable

Verbatim third-party text (testimonials, quotes, reviews, transcripts) is exempt from every rule in this pass. Never rewrite someone's words to fit a style guide. If a quote contains a banned word, keep the quote or cut it entirely, and surface the conflict rather than silently editing it.

---

# PASS 2: structure

The shape of the piece. This is the half that actually carries the detection signal.

## Step 1: extract the skeleton first

Never audit the prose. Audit an outline pulled from it. Comparing raw prose surfaces style-heavy features; comparing structure surfaces structural ones, and the two sets barely overlap.

Write the skeleton out before judging anything:

1. The beats, in order, one line each.
2. Where the central point is stated, and how many times it is restated.
3. What resolves by the end, and what is left open.
4. Tangent count: how many passages do not serve the main line.
5. Every emotional moment, and whether it is named plainly or performed through the body.
6. Every reference, marked checkable (a name, number, date, version, place) or vague.

## Step 2: the six audits, one at a time

Run them separately, never as one combined pass. Aspect-based checking covered 95.4% of issues against 68.4% for a single mega-pass. Each carries the human against AI rate so you know how hard to push.

**1. Theme explicitness** (narrator states the theme: 77% AI, 52% human)
State the point once, where it lands hardest. Cut every restatement. Leave at least one example uninterpreted. The section-ending moral is the most common form.

**2. Structural tidiness** (no subplots: 79% AI, 57% human)
Everything serving one line is a machine habit. Pick one fix: an oblique tangent never tied back, a question raised and explicitly not answered, or stopping before full resolution.

**3. Emotion mode** (embodied: 81% AI, 38% human. Named plainly: 29% human, 8% AI)
The largest single gap. Replace performed emotion with named emotion. "My chest tightened" becomes "honestly, that one stung". Reserve one embodied moment for where it is earned. This contradicts show-don't-tell, and that is the point: classic writing advice is now a machine signature.

**4. Reference specificity** (named references: 47% human, 24% AI)
Every vague allusion becomes checkable. "A popular productivity book" gets its title. "An expert" gets a name. "Recently" gets a date. Add the price, the version, the place. Where the vague reference is a factual claim, a fact-check pass owns the verification; this pass owns only the specificity.

**5. Reader engagement** (direct address: 28% human, 7% AI)
Acknowledge the reader or the act of writing, sparingly. Once in a piece, not as a habit.

**6. Shape convergence**
Compare this piece's skeleton against the last two or three in the same channel. The only audit that looks outside the current document, and the one nothing else catches, because each piece passes every other check on its own.

```bash
python3 scripts/shape-convergence.py <draft> --against-dir <recent pieces dir>
```

Scores 0 to 1, flags at 0.85, weighting the opening and closing move because that is the repetition a reader notices first. Exits 1 on a repeat, so it works as a pre-publish gate.

## Step 3: choose one or two interventions, not all

Rotate through this menu. Never repeat the last piece's choice.

Outcome first. Cold open mid-scene. Delayed reveal, withholding the key number until two thirds through. A callback that recontextualises. The oblique tangent, left untied. An open thread. Genuine ambivalence. The named thing. Plain emotion. Acknowledged reader. Ending hot, stopping at the spike rather than the quiet coda.

## Step 4: rewrite structurally

Move sections. Cut codas. Delete restatements. Section-level surgery, which is why it runs after the cheap surface pass and before voice.

## Step 5: run the structural scanner

```bash
python3 scripts/structural-scan.py <file>
```

Advisory by default, exits 0. `--strict` exits 1 when a category reaches two hits, for a pre-publish gate on outward-facing content. Four categories (embodied emotion, stated lesson, vague allusion, tidy closer matched only in the closing paragraphs) plus two metrics (paragraph-length variance, numbers per 100 words). Put `structural-ignore` on a line to suppress a deliberate usage.

The scanner catches roughly half. Cadence, formulaic shape and polished-but-empty filler are visible only to a reader. A clean scan is not a pass.

## Step 6: check for the trap

If the fix looks like the last fix, vary it. Uniform application of this skill produces its own cluster, which defeats the point.

---

## Model fingerprints

Useful when you know which model drafted the text.

**Claude** was the most structurally distinctive of the five tested. Flat event escalation (uniform intensity, no real peak). The epilogue habit: a wrap-up coda after the natural ending. Reverent quiet endings. Fixes: vary stakes across the piece, cut the coda, sometimes end on the spike.

**GPT**: distant retrospective framing ("years later, I understood"), gossip mechanics.
**Gemini**: the tidiest endings. Remove the bow.

---

## Genre calibration

Short pieces under roughly 400 words: run audits 1, 3, 4 and 6 only. The others need length to matter.

| Format | What applies |
|---|---|
| Social post | State the insight once, and in roughly a third of posts do not state it at all. Rotate skeletons; never the same shape twice running. |
| Blog or essay | The full menu. One deliberate structural choice per post. No epilogue coda. |
| Email or newsletter | The lesson once, not twice. A PS is a natural slot for the oblique tangent. Skip nonlinearity. |
| Teaching or course content | Teaching demands explicitness, so audit 1 relaxes. The tell is restating the moral at every section end. Cap summary sections at roughly one in three. |
| Internal doc, plan, spec | Pass 1 only. Skip pass 2 entirely: clarity beats rarity and nobody needs a spec to sound human. |

---

## Scope

**Both passes:** outward-facing content. Posts, articles, emails, landing pages, scripts, anything published under a name.
**Pass 1 only:** everything else. Internal docs, plans, specs, memories, changelogs.

## The failure mode to avoid

Removing signal without adding any produces text that is clean and dead. Copy that passes every scanner and still says nothing has not been humanised, it has been sanded. This skill takes the machine smell out. It does not make the piece worth reading, and it cannot tell the difference. That judgment stays with the author.

---

## What sits around this skill

This skill is self-contained and needs none of the below. They are the passes that pair with it, if you have them or build them later.

- **A fact-check pass:** claim verification. Runs BEFORE this one, because there is no point polishing a false sentence.
- **A voice pass:** the personal layer that makes writing sound like a specific author. Runs AFTER this one. The order is load-bearing: this skill REMOVES signal and a voice pass ADDS it, so running voice first means this pass strips the very habits that make the writing theirs.
- **A style-rules reference:** your own banned-word list, soft patterns and format rules. The essentials are already inlined in pass 1, and `scripts/banned-words.txt` is the editable list this kit ships with.
- **Evidence:** the research this skill is built on is cited inline in "Why both passes exist" and in the header comments of `scripts/structural-scan.py` and `scripts/shape-convergence.py`.
