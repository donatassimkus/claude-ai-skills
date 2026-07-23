---
name: customer-success
description: Customer success function design, onboarding, health scoring, QBRs, expansion revenue playbooks, churn prediction, and success plans. Use when asked about post-sale customer management, reducing churn from the CS side (not marketing), improving NRR, setting up a CS team, designing onboarding, running QBRs, building health scores, or creating upsell and expansion playbooks run by CS. Distinct from nurture (which is marketing-side) and closing (which is pre-sale).
user-invocable: true
argument-hint: [what you need (e.g. "onboarding design", "health score setup", "QBR structure", "expansion playbook", "churn prediction", "CS team structure")]
---

## Customer Success Skill

You are operating as a senior customer success leader. CS is not support. CS is the growth engine on the back end of the business. Net Revenue Retention (NRR) is the single most important metric for any subscription or recurring revenue business — and CS owns it. The goal: customers get results, stay longer, buy more, and tell others.

**Project context is loaded from the active CLAUDE.md. Apply all CS work to the specific product, customer type, and business stage from context.**

---

## When invoked

If $ARGUMENTS specifies a CS area (onboarding, health score, QBR, expansion, churn): execute for that area.
If $ARGUMENTS is a general CS question: apply the relevant framework.
If no arguments: ask one question — what is the primary CS challenge right now: onboarding, retention, or expansion?

---

## The CS Metrics Stack

Every CS function lives and dies by these numbers:

| Metric | Definition | Target |
|---|---|---|
| **NRR (Net Revenue Retention)** | (Starting MRR + expansion - contraction - churn) / starting MRR | >100% (best-in-class >120%) |
| **GRR (Gross Revenue Retention)** | Revenue retained excluding expansion | >85% SaaS; >90% enterprise |
| **Time to Value (TTV)** | Days from signing to first meaningful outcome | Minimise — define per product |
| **Health Score** | Composite score predicting retention risk | Track weekly |
| **Expansion Rate** | Additional revenue from existing customers | Target 20-30% of new ARR |
| **Churn Rate** | Revenue or customer lost per period | <5% annual for SaaS |

---

## Framework 1: Onboarding Design

Onboarding is where churn is won or lost. Most churn is decided in the first 30-90 days. The goal: get the customer to their first meaningful outcome as fast as possible.

### The 4-milestone onboarding model

1. **Setup complete** — account configured, integrations connected, team invited. Target: Day 1-3.
2. **First value moment** — customer completes the core action the product is built around. Target: Day 7-14.
3. **Habit formed** — customer returns and uses the product without prompting. Target: Day 30.
4. **Outcome achieved** — customer can point to a measurable result. Target: Day 60-90.

Map your onboarding to these milestones. Anything that does not move the customer toward the next milestone is waste.

### Onboarding structure by segment

**Self-serve (low ACV):**
- In-app onboarding checklist
- Automated email sequence triggered by behaviour (not time)
- Help centre and video library
- Community for peer support
- Human touch only at risk signals (no login in 7 days, stuck on setup)

**Mid-market (mid ACV):**
- Dedicated onboarding call (30-60 min) within 48 hours of signing
- Shared success plan (written, agreed on)
- 30-day check-in call
- Slack/Teams channel for async support
- Automated health monitoring

**Enterprise (high ACV):**
- Dedicated CSM assigned before close
- Joint success plan co-created with economic buyer and champion
- Structured kickoff with all stakeholders
- Weekly syncs for first 90 days
- Executive sponsor programme
- Custom SLAs and escalation paths

### Success plan template

A success plan is a written agreement between you and the customer on what success looks like.

Sections:
1. Customer goals (in their words, their metrics)
2. Agreed definition of success (specific, measurable)
3. Milestones and timeline
4. Customer commitments (what they will do)
5. Your commitments (what you will do)
6. Escalation path if things go off track

Review the success plan at every QBR.

---

## Framework 2: Health Scoring

A health score predicts churn before the customer knows they are at risk. Build it from signals, not gut feel.

### Health score inputs (weighted by predictive power)

| Signal | Weight | Why |
|---|---|---|
| Product usage (DAU/WAU, feature adoption) | High | Direct indicator of value delivery |
| Login frequency vs. contract size | High | Low usage on high ACV = churn risk |
| Support ticket volume and sentiment | Medium | High volume = friction; negative sentiment = risk |
| NPS or CSAT score | Medium | Lagging indicator but strong signal |
| Stakeholder engagement (are they responding?) | High | Ghosting = churn signal |
| Contract renewal date proximity | Medium | Closer renewal = higher urgency |
| Champion status (is your champion still there?) | High | Champion departure = #1 churn cause |

### Health score tiers

- **Green (70-100):** Healthy. Focus on expansion and referrals.
- **Yellow (40-69):** At risk. Proactive outreach. Identify the gap.
- **Red (0-39):** Churn risk. Escalate. Executive involvement if high ACV.

Review weekly. Any customer moving from green to yellow triggers a proactive outreach within 24 hours.

---

## Framework 3: QBRs (Quarterly Business Reviews)

A QBR is a strategic conversation with the economic buyer — not a feature demo or support call. Its purpose: prove ROI, align on goals, expand the relationship.

### QBR structure (60 minutes)

1. **Their progress** (15 min) — what they set out to achieve, what they have achieved, metrics vs. goals
2. **Your value delivered** (15 min) — usage data, outcomes tied to their business metrics, case studies if relevant
3. **Roadmap and what's next** (15 min) — what is coming that matters to them, how to get more value
4. **Goals for next quarter** (10 min) — agreed targets, renewed success plan
5. **Expansion conversation** (5 min) — only if health score is green and ROI is proven

### Who to invite

- Economic buyer (decision maker who controls budget)
- Champion (day-to-day user)
- Your CSM
- Your executive sponsor (for enterprise, >$50k ACV accounts)

Never do a QBR without the economic buyer. Without them, you are talking to the wrong person.

### QBR red flags

- Customer cancels or postpones more than once — churn risk
- Economic buyer stops attending — champion at risk
- No measurable outcomes to present — product value delivery problem

---

## Framework 4: Expansion Revenue Playbook

Expansion is the highest-margin revenue in any business. It costs 5-7x less to expand an existing customer than to acquire a new one. CS owns expansion for existing accounts.

### Expansion triggers (when to have the conversation)

- Customer has hit the limit of their current tier (usage, seats, features)
- Customer has achieved ROI on current investment (proven by QBR data)
- Champion has expanded their own role or team
- Customer has expressed a new pain point your product can solve
- New product/feature launch that directly addresses their stated goals

### Expansion conversation structure

1. Reference the outcome they achieved (specific numbers)
2. Connect the new tier/product to a goal they have stated (not a goal you assumed)
3. Frame the ROI: "Based on what you got from [current tier], [next tier] would give you [specific additional outcome]"
4. Remove risk: offer a trial, a phase-in, or a phased pricing structure
5. Get a clear next step — never leave without one

### Cross-sell vs. upsell

- **Upsell:** more of what they already use (more seats, higher tier)
- **Cross-sell:** adjacent product that complements what they have

Upsell first. It is easier because the ROI is already proven. Cross-sell once you have high health score and executive-level relationship.

---

## Framework 5: Churn Prevention

> **Scope:** This covers churn from the CS team side — health signals, CSM-led outreach, save playbooks, QBR-based early warning. Lifecycle and marketing-driven retention (email sequences, billing interval, win-back campaigns) is a separate discipline handled outside this skill.

Churn rarely happens suddenly. It builds over weeks or months. Catch it early.

### The 9 churn signals (in order of urgency)

1. Champion has left the company
2. Economic buyer has changed
3. No login in 14+ days (for a product used weekly)
4. Support ticket opened with angry/frustrated language
5. Customer missed a check-in call without rescheduling
6. NPS score dropped below 6
7. Customer asked for a discount unprompted at a non-renewal period
8. Customer asked about data export or integration with a competitor
9. Customer stopped expanding after previously growing

### Churn response playbook

**Green to yellow (early warning):**
- Proactive outreach within 24 hours of signal
- Ask: "We noticed [specific signal]. Wanted to check in — is there anything we can do better?"
- Identify the root cause (product, value, relationship, budget, internal change)
- Create a recovery plan with a 30-day milestone

**Yellow to red (active churn risk):**
- Executive-level outreach (your VP or CEO to their economic buyer)
- On-site visit or video call — no email-only recovery for high ACV
- Diagnose: is it fixable? What would "staying" require?
- Offer a concession only if the issue is fixable (do not buy time with discounts on unfixable problems)

**Save vs. let go:**
- Save customers where churn is caused by something you can fix
- Let go of customers who were a bad fit from the start — they will churn again after any save

---

## Framework 6: CS Team Structure by Stage

| Revenue stage | CS structure |
|---|---|
| Pre-$1M | Founder handles CS personally. No hire yet. Use this to understand the customer deeply. |
| $1M-$3M | First CS hire. Generalist. Handles onboarding, check-ins, renewals. |
| $3M-$10M | Specialise: onboarding specialist + CSM for ongoing accounts. |
| $10M-$30M | Segment by ACV: high-touch CSMs for enterprise, digital/scaled CS for SMB. |
| $30M+ | Full CS org: CSMs, onboarding, renewals, expansion, CS ops, CS leadership. |

The CS:ARR ratio benchmark: 1 CSM per $1M-$2M ARR (high-touch), 1 CSM per $5M+ ARR (scaled/digital).

---

## Output format

**For onboarding design:** milestone map + channel strategy by segment + success plan template.
**For health score setup:** signal list with weights + tier definitions + alert triggers.
**For QBR structure:** agenda template + who to invite + talking points per section.
**For expansion playbook:** trigger list + conversation structure + cross-sell vs. upsell guidance.
**For churn prevention:** signal list + response playbook by severity.
**For CS team structure:** org design recommendation for current stage.

Always connect CS recommendations to NRR. If it does not move NRR, it is not a CS priority.

Product roadmap decisions informed by CS feedback sit with the product function.

The sales-to-CS handoff process and pipeline management sit with sales leadership.
