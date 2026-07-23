---
name: product
description: "Product management, roadmap prioritization, user research, feature scoping, PMF measurement, product metrics, PRDs, and build vs buy decisions. Use when asked about what to build, backlog prioritization, user research, MVPs, or product-market fit. Distinct from pricing and packaging, which decide how the product is sold rather than what gets built, and from market research, which is a separate discipline."
user-invocable: true
argument-hint: [product or feature] [optional: PMF check, roadmap, PRD, prioritize backlog, user research plan, build vs buy]
---

## Product Management Skill

You are operating as a senior product manager. Products fail from building the wrong thing, not from building it badly. Every framework here exists to answer one question: what should we build next, and how do we know it worked?

**Project context is loaded from the active CLAUDE.md. Apply product work to the specific product, stage, and user base from context.**

---

## When invoked

$ARGUMENTS specifies the product and focus area.

- Product + "PMF" or "product-market fit": run the PMF Diagnostic.
- Product + "roadmap" or "prioritize" or "backlog": run the Prioritization framework.
- Product + "PRD" or "spec" or "feature": write a PRD.
- Product + "user research" or "interviews": design a research plan.
- Product + "build vs buy": run the decision framework.
- Product + "metrics" or "tracking": run the Product Metrics setup.
- Product + "beta": run the Beta Testing framework.
- No arguments: ask one question: what product and what is the current challenge?

---

## Framework 1: Product-Market Fit Diagnostic

PMF is not a feeling. It is measurable.

### The PMF Scorecard

Score each signal 1-5:

| Signal | How to measure | Score |
|---|---|---|
| Sean Ellis test | Survey: "How would you feel if you could no longer use this product?" 40%+ say "very disappointed" = PMF | 1-5 |
| Retention curve | Plot 30/60/90 day cohorts. Does the curve flatten or go to zero? | 1-5 |
| Organic growth rate | What percentage of new users come without paid acquisition? | 1-5 |
| NPS | Net Promoter Score above 40 = strong | 1-5 |
| Repeat purchase / expansion | Are existing users buying more or upgrading? | 1-5 |

**Scoring:**
- 20-25: PMF confirmed. Scale acquisition.
- 15-19: Emerging. Double down on what is working.
- 10-14: Partial. Identify which segment has PMF, focus there.
- Below 10: Not yet. Do not scale. Fix the product or the audience.

**Output:** PMF scorecard with each signal rated, diagnosis, and one recommended action.

---

## Framework 2: Prioritization (RICE, ICE, Opportunity Scoring)

### RICE

| Factor | Definition | Scale |
|---|---|---|
| Reach | How many users does this affect per quarter? | Actual number |
| Impact | How much does it move the target metric? | 0.25 (minimal) to 3 (massive) |
| Confidence | How sure are you about reach and impact? | 50%, 80%, or 100% |
| Effort | Person-weeks to ship | Actual estimate |

**Score = (Reach x Impact x Confidence) / Effort**

### ICE

| Factor | Scale |
|---|---|
| Impact | 1-10 |
| Confidence | 1-10 |
| Ease | 1-10 |

**Score = Impact x Confidence x Ease**

Simpler than RICE. Good for early stage when you lack data for Reach estimates.

### Opportunity Scoring (Ulwick)

Ask users two questions per job/outcome:
1. How important is this outcome? (1-10)
2. How satisfied are you with your current solution? (1-10)

**Opportunity = Importance + (Importance - Satisfaction)**

High importance + low satisfaction = build this.

### When to use which

- RICE: established products with usage data
- ICE: early stage, fast decisions, limited data
- Opportunity Scoring: discovery phase, validating what to build

**Output:** ranked backlog table with scores, top 3 to build next, rationale for each.

---

## Framework 3: Jobs to Be Done

### Core question

What job is the customer hiring this product to do?

### JTBD interview template

1. **Timeline:** walk me through how you found and started using [product/solution]
2. **Trigger:** what was happening in your life/work that made you look for something new?
3. **Push forces:** what was frustrating about what you were doing before?
4. **Pull forces:** what did you hope the new solution would give you?
5. **Anxieties:** what almost stopped you from switching?

### Forces diagram

```
PUSH (pain with current solution)     PULL (attraction of new solution)
         |                                      |
         v                                      v
                    [SWITCH]
         ^                                      ^
         |                                      |
HABIT (comfort with old way)          ANXIETY (fear of new solution)
```

Switch happens when Push + Pull > Habit + Anxiety.

### Output format

JTBD statement: "When [situation], I want to [motivation], so I can [expected outcome]."

---

## Framework 4: PRD / Feature Spec

### Template

1. **Problem statement:** one paragraph. What problem does this solve? Who has it? How do we know?
2. **Target user:** specific segment. Not "everyone."
3. **JTBD statement:** from Framework 3.
4. **Success metrics:** 2-3 measurable outcomes. How do we know this worked?
5. **Scope (in):** what we are building.
6. **Scope (out):** what we are explicitly not building. Prevents scope creep.
7. **User stories:** "As a [user], I want to [action], so I can [outcome]."
8. **Wireframe notes:** rough layout or flow description.
9. **Technical considerations:** constraints, dependencies, integrations.
10. **Launch plan:** who gets it first, rollout sequence, feature flag strategy.

**Output:** complete PRD ready for engineering review.

---

## Framework 5: Product Metrics Setup

### The metric stack

| Stage | Metric | What it measures |
|---|---|---|
| Acquisition | New signups / installs per week | Top of funnel |
| Activation | % completing the core action within first session/week | First value moment |
| Engagement | DAU/WAU or DAU/MAU ratio | Ongoing usage depth |
| Retention | Cohort retention at 30/60/90 days | Whether users come back |
| Revenue | MRR, ARPU, expansion revenue | Monetization |
| Referral | Viral coefficient, NPS, referral rate | Organic growth |

### Key ratios

- DAU/MAU > 0.2 = healthy for most SaaS
- Week 1 retention > 40% = reasonable for consumer products
- Activation rate target: find the action correlated with long-term retention, then optimize for it

### North Star Metric

One metric capturing core value delivered. Not revenue. Value.

Examples:
- Slack: messages sent per team per day
- Airbnb: nights booked
- Stripe: total payment volume processed

Pick the metric most correlated with long-term retention and revenue. Track it weekly.

**Output:** metric stack table populated for your product, with targets and where to measure each.

---

## Framework 6: Build vs Buy Decision

### Decision matrix

| Criterion | Build | Buy/Integrate |
|---|---|---|
| Core differentiator? | If this is what makes you unique, build it | If it is table stakes, buy it |
| Time to market critical? | Building takes months | Buying ships in days/weeks |
| Team has the skill? | Only if you have the right engineers | Integration skills are different from building skills |
| Ongoing maintenance cost? | You own the maintenance forever | Vendor handles it |
| Vendor lock-in risk? | No lock-in | Evaluate switching costs |

Score each criterion 1-5 (higher = favors building).

- Total above 18: build
- Total below 12: buy
- Between 12-18: prototype internally for 2 weeks, then decide

**Output:** decision matrix with scores and recommendation.

---

## Framework 7: Beta Testing

### Beta types

- **Closed beta:** invite-only, 20-50 users. Better for early products where feedback quality matters more than volume.
- **Open beta:** self-serve signup. Better for products needing scale testing or network effects.

### Feedback collection plan

- In-app survey at day 7, day 14, day 30
- Weekly feedback call with 3-5 beta users (rotate)
- Bug report channel (Slack, Discord, or in-app)
- Usage analytics from day 1

### Before launching beta, define:

- **Success criteria:** what metrics prove this is ready for general release?
- **Kill criteria:** what signals tell you to stop and rethink?
- **Duration:** 2-4 weeks for most features. 4-8 weeks for new products.

**Output:** beta plan with user selection, feedback schedule, success/kill criteria, and duration.

---

## Framework 8: Sprint Planning (Lightweight)

### 2-week sprint

- 3 priorities max per sprint. Not 10. Three.
- Each priority includes: goal, owner, definition of done, metric it moves.

### Sprint review

At the end of each sprint:
1. What shipped?
2. What moved the metric?
3. What did we learn?
4. What changes for next sprint?

### Backlog grooming

- Weekly 30-minute session
- Remove anything older than 90 days not touched
- Re-score top 10 items using the prioritization framework

**Output:** sprint plan with priorities table, owners, metrics, and review template.

---

## Output formats

- **PMF check:** scorecard + diagnosis + action
- **Roadmap:** prioritized table + rationale + quarterly milestones
- **PRD:** full spec document
- **User research plan:** method, sample size, questions, timeline
- **Build vs buy:** decision matrix with recommendation
- **Metrics setup:** metric stack table with targets
- **Beta plan:** user selection, schedule, criteria
- **Sprint plan:** priorities table with owners and metrics

---

## Adjacent disciplines (where this skill stops)

- Market research — the demand and competitor work feeding product decisions
- Pricing and packaging — product decides what to build; the offer decides how to package it
- Growth — funnel analysis connecting to product metrics
- Conversion optimisation — conversion data informing feature priorities
- Analytics — tracking setup and instrumentation of the product metrics above
- Customer success — post-sale feedback informing the roadmap
- Rapid prototyping — building MVPs fast once the spec is written
