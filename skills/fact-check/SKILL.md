---
name: fact-check
description: "Verify every checkable claim in a draft before it ships: statistics, dates, prices, quotes, attributions, named entities, superlatives and 'studies show' assertions. Fetches sources and confirms each one actually says what the draft claims. Never invents a citation to rescue a claim. Use before publishing anything with a number, a quote, or a factual assertion in it, or when asked to fact-check, verify claims, or check sources."
disable-model-invocation: false
user-invocable: true
argument-hint: [paste or path to a draft] OR [strict: cut anything unverifiable]
---

## Fact-check skill

You are verifying claims, not improving prose. Do not rewrite for style here. Another layer owns that.

**This skill is verification only and applies across all contexts.**

---

## The one rule

**Never invent, guess, or reconstruct a source.** A plausible-looking citation for an unverified claim is worse than no citation, because it survives review and fails in public. If a claim cannot be verified, it gets cut, softened to what is actually known, or labelled as the author's own estimate. Those are the only three outcomes.

A URL that looks right is not verification. Fetch it and confirm the page contains the claim.

---

## When invoked

If $ARGUMENTS contains a draft or a path: run the full pass and return the claim table plus a corrected draft.
If $ARGUMENTS starts with "strict": same, but cut every claim that fails verification rather than proposing a softer version.
If no arguments: ask for the draft.

---

## Step 1: extract every checkable claim

Read the draft and pull out anything that could be true or false. Be greedy here: it is cheaper to clear a claim than to miss one.

| Claim type | What to catch |
|---|---|
| Statistics | Any number presented as fact: percentages, counts, growth rates, benchmarks, "3x", "40% of" |
| Money | Prices, revenue, funding, salaries, costs, market size |
| Dates and sequence | "since 2019", "last year", "the first to", "before X launched" |
| Quotes | Anything in quotation marks attributed to a person or organisation |
| Attributions | "according to", "X says", "research from" |
| Vague sourcing | "studies show", "experts agree", "research suggests", "it is well known" |
| Named entities | Product names, features, company facts, job titles, who owns what |
| Superlatives | "the largest", "the only", "the first", "the fastest", "nobody else" |
| Capability claims | "X integrates with Y", "the free plan includes Z", "it cannot do W" |
| Implied currency | Anything stated in the present tense about a fast-moving product or market |

Ignore: opinions, predictions clearly framed as such, hypotheticals, the author's own experience, and obvious rhetorical figures.

## Step 2: classify before verifying

Sort each claim into one of four buckets. This decides the work.

1. **Verifiable and load-bearing.** The argument breaks if it is wrong. Verify properly.
2. **Verifiable and decorative.** True or false, the piece survives. Verify cheaply, or cut it as filler.
3. **The author's own experience or data.** Cannot be externally verified. Confirm with the author that the number is real, then mark it as first-party in the text ("in my own testing", "across the accounts I manage").
4. **Opinion or prediction.** Not a fact. Confirm the wording actually frames it as opinion rather than smuggling it in as fact.

## Step 3: verify

Use the real tools, in this order of preference:

1. **The primary source.** The study itself, the company's own docs, the pricing page, the filing, the original post. Fetch it.
2. **Search** for the primary source when the draft cites second-hand. Use whatever web search this environment has: a built-in search tool, a search API, or a scraping service.
3. **Fetch and read** the page. Use whatever fetch tool this environment has: a built-in page fetcher, a scraping API, or a browser. Confirm the page contains the specific figure or wording, not merely the topic.

For each claim record: the verdict, the source URL, the exact supporting line from the source, and the date the source was published.

**Verdicts:**

- **Confirmed.** The source states it. Record the URL and the supporting line.
- **Confirmed but stale.** True when published, and the source is old enough to doubt for a fast-moving subject. Record both dates.
- **Directionally right, wrong number.** Common with statistics passed between blogs. Give the real figure from the primary source.
- **Unsupported.** No source found. Not proven false, just nobody backs it.
- **False.** The source contradicts it.
- **Circular.** Every result tracing the claim leads back to blogs citing each other with no primary source. Treat as unsupported, and say so explicitly, because this is the most common failure for a widely-repeated statistic.

## Step 4: fix

| Verdict | What to do |
|---|---|
| Confirmed | Keep. Add the named source in the text where it carries weight. |
| Confirmed but stale | Keep with the date attached ("as of [year]"), or find current data. |
| Wrong number | Replace with the real figure and cite the primary source. |
| Unsupported, load-bearing | Cut it, or rewrite the sentence so the argument stands without it. |
| Unsupported, decorative | Cut it. It was filler. |
| False | Cut it. Then check whether anything downstream in the draft depended on it. |
| Author's own data | Keep, and mark it as first-party so a reader knows it is not published research. |

**The vague-sourcing rule.** "Studies show" and "experts agree" are either replaced with the actual named source, or deleted. There is no third option. This overlaps with the structural pass, which flags the same phrases as a specificity tell; here the fix is a real citation rather than a rephrase.

## Step 5: output

Return two things.

**The claim table**, most severe first:

```
| Claim (as written) | Type | Verdict | Source | Fix |
```

**The corrected draft**, with every fix applied. Then one line stating what was cut and why, so the author can push back on a specific call.

If nothing failed, say so plainly: "N claims checked, all confirmed." Do not manufacture concerns to look thorough.

---

## What this skill does not own

Style, banned words, sentence patterns, structure, voice. An anti-AI pass and a voice pass own those, and they run separately. A draft can be entirely accurate and still read as machine-made; a draft can read beautifully and be entirely wrong. These are different failure modes and different passes.

## Where it sits

Run it **before** the writing chain, not after. Verification changes what the sentences say, and there is no point polishing a sentence that is about to be cut for being false.

---

## What sits around this skill

This skill is self-contained and needs none of the below. They are the passes that pair with it, if you have them or build them later. This one always runs FIRST.

- **An anti-AI pass:** banned words, sentence patterns, and the structural shape of the piece. Runs after this one.
- **A voice pass:** the personal layer that makes writing sound like a specific author. Runs last, because it ADDS signal where the anti-AI pass removes it.
