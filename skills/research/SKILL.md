---
name: research
description: "Market research, competitor analysis, audience research, trend analysis, product research, pricing research. Invoke when: sizing a market, mapping competitors, building an ICP, analyzing industry trends, doing pricing research, mystery shopping a competitor, building a competitive intelligence report, or finding out what an audience actually wants before building or spending. Product-specific user research and feature decisions are an adjacent discipline handled separately."
user-invocable: true
argument-hint: [research type] [subject]
---

## Research Skill

Research with a bias toward actionable findings. No academic reports. Every output should answer: so what do I do with this?

**Project context is loaded from the active CLAUDE.md. Frame all research findings in terms of that project's goals and competitive position.**

---

## When invoked

$ARGUMENTS defines the research type and subject.
If unclear, ask one question to clarify scope before proceeding.

---

## Research types

### Competitor analysis

For each competitor:
1. Product: what they offer, pricing tiers, positioning, differentiators
2. Acquisition: how they get customers (SEO, paid, social, partnerships, viral)
3. Retention: what keeps customers (features, community, lock-in)
4. Weaknesses: what they do badly, where reviews complain, what they are missing
5. Opportunity: where they are vulnerable and you can win

Output: comparison table + "where to attack" summary.

### Market research

1. Market size and growth direction
2. Key segments and who is underserved
3. Buying triggers: what causes someone to buy in this category?
4. Objections: what stops people from buying?
5. Pricing norms: what does the market expect to pay?
6. Distribution channels that work in this market

Output: market snapshot + top 3 opportunities.

### Audience research

1. Who they are: demographics, job, situation
2. Pain: what problem are they trying to solve right now?
3. Language: how do they describe the problem in their own words?
4. Watering holes: where do they hang out online?
5. Buying behavior: how do they evaluate and decide?
6. Triggers: what causes them to act now vs later?

Output: audience profile + messaging implications.

### Pricing research

1. Competitor pricing tiers and what each tier includes
2. Where the market anchors value
3. Price sensitivity signals (free trial vs freemium vs demo)
4. Packaging patterns (per seat, per usage, flat, tiered)
5. Upsell and expansion revenue patterns

Output: pricing benchmark + recommended positioning.

### Keyword / SEO research

Full SEO research is a separate discipline; hand it off there rather than half-running it here. This section covers only:
- Quick competitive keyword gap analysis
- Identifying what competitors rank for that you do not
- Finding uncontested long-tail opportunities

---

## Output format

**Standard structure:**
1. Key findings (3-7 bullets, most important first)
2. Evidence or source for each finding
3. Implications: what this means for the project
4. Recommended action: one or two concrete next steps

**Rules:**
- Label assumptions clearly.
- Do not invent facts. If data is not available, say so and proceed with labeled estimates.
- Prioritize findings by revenue or strategic impact.
- No padding. If there are only 3 meaningful findings, deliver 3.

---

## Adjacent disciplines (where this skill stops)

- Product decisions informed by market research: product-market fit, roadmap, feature prioritization.
- Market sizing feeding investor narratives and pitch decks.
- Full SEO and keyword research, beyond the quick competitive gap analysis above.
