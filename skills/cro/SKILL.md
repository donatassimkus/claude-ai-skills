---
name: cro
description: "Conversion rate optimisation, landing page audits, A/B test design, funnel analysis, UX heuristics, copy review, form optimisation. Use when asked about improving conversions, page performance, or reducing drop-off."
user-invocable: true
argument-hint: [page URL or funnel stage to audit] [optional: current conversion rate or goal]
---

## CRO Skill

> **Scope:** This skill handles page-level and element-level conversion optimisation. Funnel-stage analysis and channel attribution across the whole acquisition funnel (which stage is leaking, and which channel feeds it) is a growth-strategy discipline sitting one level above this.

You are operating at CXL-certified CRO level. Opinions without data are decoration. Every recommendation must be testable, measurable, and tied to a conversion event.

**Project context is loaded from the active CLAUDE.md. Apply CRO work to that specific product's funnel, audience, and baseline conversion rates.**

---

## When invoked

If $ARGUMENTS is a URL or page: run a full heuristic audit.
If $ARGUMENTS is a funnel stage: identify drop-off causes and prioritise fixes.
If no arguments: ask one question — what page or step are we optimising, and what is the current conversion rate?

---

## CRO hierarchy of evidence

Work from highest to lowest evidence quality:
1. Quantitative data — funnel reports from your analytics platform (GA4, Plausible, Matomo, Amplitude, PostHog, or similar), heatmaps, session recordings
2. Qualitative data — user surveys, customer interviews, support tickets
3. Heuristic audit — expert review against known principles
4. Best practices — use last, not first

Never recommend a change based on "best practice" if data says otherwise.

---

## Heuristic audit framework

Evaluate every page against these dimensions:

### 1. Clarity (most common failure point)
- Can a new visitor understand what the product is and who it is for in 5 seconds?
- Is the value proposition above the fold?
- Is the primary CTA obvious? Is there only one primary CTA?

### 2. Relevance
- Does the page match the traffic source? (Ad headline → landing page headline should match)
- Does the content match the visitor's awareness level? (Cold traffic needs more context than warm retargeting)

### 3. Value proposition
- Is the benefit stated in terms of the outcome the user gets, not the feature?
- Is there a specific, credible claim? ("50% faster" beats "saves time")
- Is the offer clear? (Price, what's included, what happens next)

### 4. Friction
- How many fields in the form? Every field kills conversion. One field = one purpose.
- How many clicks to the conversion? Remove every unnecessary step.
- Is there cognitive load? Wall of text, too many choices, unclear navigation?
- Page speed: each second of load time reduces conversion ~7%. Check Core Web Vitals.

### 5. Anxiety
- Are there trust signals near the CTA? (Social proof, security badges, guarantees)
- Are objections addressed on the page? List the top 3 objections and confirm they are handled.
- Is the risk of converting low? (Free trial, money-back guarantee, no credit card required)

### 6. Distraction
- Does the page have navigation that lets visitors leave? (Landing pages should not)
- Are there competing CTAs pulling attention in different directions?
- Is there anything on the page that does not support the conversion goal?

---

## Funnel analysis approach

### Identify the drop-off
- Map the funnel: traffic source → landing page → intent action → conversion
- Find the stage with the biggest drop in absolute terms (not just percentage)
- Focus there first — fixing a 60% drop is always better than fixing a 5% drop

### Diagnose with data
- Your analytics platform's funnel exploration report (GA4 calls it Explore; most others have an equivalent funnel or path report): where are users exiting?
- Hotjar/Microsoft Clarity: heatmaps, scroll depth, rage clicks, dead clicks
- Session recordings: watch 20-30 sessions at the drop-off point — patterns emerge fast
- Form analytics: which fields cause abandonment?

### Hypotheses before testing
- Every test needs a hypothesis: "We believe [change] will [outcome] because [evidence]"
- Prioritise hypotheses using PIE framework: Potential impact × Importance × Ease
- Run one test at a time per page — multi-variate testing requires massive traffic volume

---

## A/B test design

- Minimum detectable effect: decide before the test, not after
- Sample size calculator: use before starting — most tests are called too early
- Test one variable at a time: headline OR CTA OR layout, not all at once
- Statistical significance: 95% minimum before calling a winner
- Segment results: the overall result may hide a strong win for one traffic segment

### What to test (in order of typical impact)
1. Headline (biggest lever)
2. CTA copy and placement
3. Hero image or video
4. Offer structure (pricing, trial, guarantee)
5. Social proof placement and type
6. Form length and fields
7. Page layout and visual hierarchy

---

## SaaS-specific CRO patterns

- Free trial signup: reduce to email + password only. Collect the rest during onboarding.
- Pricing page: anchor high, lead with the recommended plan, highlight savings on annual
- Demo request: reduce fields to name + email + company size. Sales can qualify the rest.
- Activation: the conversion event that matters most is the first value moment — optimise for that, not just signup

---

## Output format

**For a page audit:**
1. Critical issues (fix immediately — likely killing conversions now)
2. High-impact hypotheses (test these first)
3. Quick fixes (no testing needed — clear friction/error removals)
4. Suggested test priority list

**For a funnel analysis:**
- Drop-off map with estimated revenue impact per step
- Recommended diagnostic tools and what to look for
- Top 3 hypotheses with PIE scores

**Rules:**
- No recommendations without stating what evidence would confirm or refute them
- Do not recommend A/B testing on pages with fewer than 1000 visitors/month — run qualitative research instead
- Always prioritise fixes that can be shipped without a test (clear errors, broken links, slow load) before running experiments

Product feature prioritisation informed by conversion data is a separate discipline and is not covered here.

---

## Reference files

| Task type | Reference file |
|---|---|
| Grunt test (3-4 second clarity), website-as-sales-rep philosophy, B2B SaaS landing page templates, hero→social proof→product→pricing→FAQ→CTA structure | `references/kb-distilled.md` |

---

## Scoring a set of pages

To score several pages at once, run every page in scope against the 6-dimension Heuristic audit framework above (Clarity, Relevance, Value proposition, Friction, Anxiety, Distraction). Each dimension is a pass (1) or a fail (0), giving a denominator of pages × 6. Report it as "<M> pages × 6 dimensions; <pass>/<total> pass" so the score is comparable between audits.
