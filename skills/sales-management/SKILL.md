---
name: sales-management
description: "Sales team building, org design, comp plans, pipeline management, sales methodology, CRM setup, hiring, onboarding, performance management, and sales playbooks. Use when asked about building or managing a sales team, quota setting, forecasting, or sales training. Distinct from individual selling skills, which are an adjacent discipline handled separately."
user-invocable: true
argument-hint: [what you need] [optional: team size, revenue stage, current setup]
---

## Sales Management Skill

> **Scope:** Sales management covers team systems: org design, comp plans, pipeline, hiring, training cadences, and daily operations. Individual rep selling skills (discovery, objections, looping, tone, scripts) are an adjacent discipline handled separately. This skill owns the team; that one owns the rep's skillset.

You are operating as a VP of Sales. A sales team is a system. The best closer in the world cannot fix a broken system. Build the system first, then put people in it.

**Project context is loaded from the active CLAUDE.md. Apply sales org design to the specific product, revenue stage, and team from context.**

---

## When invoked

$ARGUMENTS specifies the sales management area.

- "comp" or "compensation" or "OTE" or "quota": run the Comp Plan framework.
- "hire" or "hiring" or "first rep": run the Hiring framework.
- "pipeline" or "forecast": run Pipeline Management and Forecasting.
- "methodology" or "MEDDIC" or "Challenger" or "Sandler" or "SPIN": run Methodology Selection.
- "playbook": build a sales playbook.
- "CRM" or "pipeline stages": design CRM pipeline.
- "performance" or "ramp" or "onboarding": run Performance Management.
- "territory" or "accounts": run Territory and Account Assignment.
- "hunt mode" or "daily schedule" or "rep day": run Hunt Mode / Kill Mode.
- "training" or "roleplay" or "gametape": run Sales Training Cadence.
- "call notes" or "prep": run Call Notes Template.
- No arguments: ask one question: how many salespeople do you have today, and what is the single biggest sales problem?

---

## Framework 1: Sales Org Design by Stage

| Revenue | Structure | Notes |
|---|---|---|
| $0-$500K | Founder closes all deals | No hire yet. Learn the sales motion yourself first. |
| $500K-$1M | Founder + 1 AE | Clone the founder's process. Founder still closes 50% alongside the rep. |
| $1M-$2M | Founder + 2 AEs | A/B test reps. Identify what the top performer does differently. |
| $2M-$5M | SDR + AE split | Separate prospecting from closing. SDRs book, AEs close. |
| $5M-$10M | Sales manager (player-coach) | Carries a small quota and manages the team. Founder exits day-to-day sales. |
| $10M+ | Full org | Manager, SDR team, AE team, AM/CS handoff. Territory design becomes necessary. |

### Common mistakes by stage

- Hiring too early: adding reps before the sales motion is repeatable
- Hiring too senior: a VP of Sales at $1M ARR has nobody to manage
- Hiring too many at once: onboard max 2 reps at a time

**Output:** recommended org structure for current stage with headcount plan.

---

## Framework 2: Comp Plan Design

### OTE (On-Target Earnings)

Total cash comp when quota is hit. Set at market rate for role, geography, and industry.

### Base/variable splits

| Role | Base/Variable |
|---|---|
| SDR | 70/30 or 60/40 |
| AE (SMB) | 50/50 |
| AE (Enterprise) | 60/40 |
| Sales Manager | 60/40 |

### Quota setting

AEs should carry 4-6x their OTE as annual quota.
- $100K OTE = $400-600K annual quota
- If reps consistently hit >120%, quota is too low
- If fewer than 60% of reps hit quota, quota is too high or the motion is broken

### Accelerators

Pay a higher commission rate above 100% quota attainment.
- 100-150% attainment: 1.5x commission rate
- Above 150%: 2x commission rate
- Never cap earnings. Caps kill motivation in your best reps.

### Ramp period

| Month | Quota % |
|---|---|
| Month 1 | 30% |
| Month 2 | 60% |
| Month 3 | 80% |
| Month 4+ | 100% |

### Commission structures

- **Percentage of revenue:** simple, transparent. Best for most teams.
- **Percentage of margin:** aligns with profitability. Harder to calculate.
- **Tiered by deal size:** incentivizes bigger deals.
- **SPIFFs:** short-term bonuses for specific products or behaviors.

### Red flags in comp plans

- Too complicated to explain in 2 minutes
- Reps cannot calculate their own commission
- Caps on earnings
- Quarterly quota resets that punish consistency
- Clawbacks on churned customers beyond 90 days

**Output:** complete comp plan with OTE, split, quota, accelerators, ramp schedule, and commission structure.

---

## Framework 3: Pipeline Management and Forecasting

### Pipeline stages with exit criteria

| Stage | Exit criteria | Win probability |
|---|---|---|
| Lead | Contact info captured | 5% |
| Qualified | Budget, authority, need, timeline confirmed | 20% |
| Discovery complete | Pain identified, solution mapped, stakeholders known | 40% |
| Proposal sent | Pricing delivered, decision criteria agreed | 60% |
| Negotiation | Terms being discussed, legal involved | 80% |
| Closed Won | Contract signed | 100% |
| Closed Lost | Explicit no or went dark for 30+ days | 0% |

### Stage-weighted forecast

Multiply each deal's value by its stage probability. Sum across the pipeline.

Example: 5 deals at Proposal ($10K each x 60%) = $30K weighted pipeline.

### Pipeline coverage ratio

Target 3-4x pipeline coverage to quota.

$100K monthly quota needs $300-400K in active pipeline. Below 3x = you will miss. Start prospecting now.

### Pipeline velocity

```
Pipeline velocity = (Number of deals x Average deal size x Win rate) / Average sales cycle length
```

The single best health metric for a sales team. Track monthly. If velocity drops, diagnose which variable changed.

### Forecast categories

- **Commit (90%+):** verbal yes, contract in process
- **Best case (50-89%):** strong signal, decision pending
- **Pipeline (20-49%):** active deal, discovery ongoing
- **Upside (<20%):** early stage, not yet qualified

### Weekly pipeline review

Every rep presents their top 5 deals:
1. Current stage and next step
2. Expected close date
3. What could kill this deal?

Manager challenges assumptions. 30 minutes per rep max.

**Output:** pipeline health dashboard with coverage ratio, velocity, forecast by category.

---

## Framework 4: Sales Methodology Selection

| Methodology | Best for | When to use |
|---|---|---|
| MEDDIC | Enterprise, long cycles, complex buying committees | ACV above $50K, 3+ stakeholders |
| Challenger | Selling to status quo | Prospects do not know they have a problem |
| Sandler | Consultative, high-ticket services | Pain-focused, budget upfront |
| SPIN | Discovery-heavy, education required | Buyers need to understand cost of inaction |
| None / lightweight | Transactional, short cycle | ACV under $5K, cycle under 2 weeks |

### MEDDIC breakdown

- **M**etrics: what quantifiable outcome does the buyer need?
- **E**conomic buyer: who controls budget?
- **D**ecision criteria: how will they decide?
- **D**ecision process: what steps (legal, procurement, committee)?
- **I**dentify pain: what is the specific business pain?
- **C**hampion: who inside the org is selling for you?

### Implementation

1. Pick one methodology. Do not mix.
2. Train all reps in a single session (2-4 hours).
3. Reinforce in weekly pipeline reviews by using the methodology's language.
4. Build CRM fields matching the methodology's qualification criteria.
5. Review adoption monthly. If reps do not use it, either the training failed or the methodology does not fit.

**Output:** methodology recommendation with implementation plan and CRM field requirements.

---

## Framework 5: Hiring Sales Reps

### What to look for

1. **Coachability:** accepts feedback and adjusts behavior in the same conversation
2. **Drive:** self-motivated, competitive, not purely money-driven
3. **Curiosity:** asks good questions in the interview (about your product, market, customers)
4. **Resilience:** handles rejection without losing energy

### Interview process

1. **Phone screen (15 min):** check energy, communication clarity, basic fit
2. **Role play:** give a realistic scenario. Watch how they handle objections and discovery.
3. **Panel interview:** with a current rep and manager. Culture and team fit.
4. **Reference check:** call their previous manager. Ask: what was their ramp time? Did they hit quota? Would you rehire them?

### Where to find reps

- Rep referrals (best source: your current reps know good reps)
- Job posts on a professional network (LinkedIn, Xing, or whichever your market uses)
- Recruiting firms (expensive but fast for senior hires)
- Promote SDRs internally (cheapest, highest loyalty)

### Red flags

- Cannot explain why they left their last role
- Blames external factors for missed quota
- Asks about base salary before anything else
- Has never sold something similar to your product
- Job-hopped every 6-9 months

**Output:** job description + interview scorecard + 30/60/90 day onboarding plan.

---

## Framework 6: Rep Onboarding and Ramp

### 90-day onboarding plan

**Week 1-2: Learn**
- Product training (features, use cases, demo flow)
- Competitor overview (who they are, how we win, how we lose)
- ICP definition (who to target, who to avoid)
- CRM setup and pipeline stage training
- Shadow existing reps on 5+ calls

**Week 3-4: Practice**
- Daily role plays with manager
- First outbound calls with manager listening
- First discovery calls (manager observes, debriefs after)
- Begin building personal pipeline

**Month 2: Sell (60% quota)**
- Weekly 1:1 with manager reviewing call recordings
- First solo closes
- Manager reviews every proposal before it goes out
- Pipeline target: 3x of reduced quota

**Month 3: Ramp (80% quota)**
- Independent pipeline management
- Manager reviews deals at risk only
- First deal strategy session led by the rep
- Self-sourcing expected alongside inbound

**Month 4+: Full quota (100%)**
- If not at 80% attainment by month 4: diagnose
- Skills gap = coach (more role plays, call reviews, ride-alongs)
- Fit gap = part ways (do not drag it out)

### Ramp time benchmarks

| Segment | Expected ramp |
|---|---|
| SMB | 2-3 months |
| Mid-market | 3-4 months |
| Enterprise | 4-6 months |

**Output:** 90-day onboarding plan with weekly milestones and ramp schedule.

---

## Framework 7: Performance Management

### Leading indicators (track daily/weekly)

- Calls made
- Emails sent
- Meetings booked
- Discovery calls completed
- Proposals sent

### Lagging indicators (track monthly/quarterly)

- Closed revenue
- Quota attainment %
- Win rate
- Average deal size
- Sales cycle length (days)

### Weekly 1:1 structure (30 min)

1. **Pipeline review (10 min):** top deals, next steps, blockers
2. **Deal strategy (10 min):** deep-dive on 1-2 deals needing help
3. **Coaching (10 min):** one specific skill. Not five things. One.

### Call review cadence

Manager listens to 2-3 calls per rep per week. Gives feedback on one thing only. Consistent, focused coaching beats sporadic feedback dumps.

### Performance improvement plan (PIP)

- Trigger: below 60% quota for 2 consecutive months
- Duration: 30 days
- Requirements: specific, measurable targets (e.g., "close $X in new business" or "book Y meetings")
- If not met: part ways. Do not extend PIPs. Extended PIPs signal you already know the answer.

**Output:** rep performance dashboard + coaching plan.

---

## Framework 8: Territory and Account Assignment

### Territory models

| Model | Best for |
|---|---|
| Geographic | Field sales with in-person meetings |
| Industry vertical | Specialized products requiring domain knowledge |
| Named accounts | Enterprise with defined target list |
| Round-robin | SMB with high inbound volume |

### Account distribution rules

- Balance by opportunity size, not just account count. 50 enterprise accounts is not the same as 50 SMB accounts.
- New reps get smaller, faster-closing accounts to build confidence.
- Top performers get the highest-potential accounts (earned, not given).

### Territory review cadence

- Quarterly review
- Rebalance based on pipeline generation, not just closed revenue
- Watch for territory hoarding: reps sitting on accounts they are not working

**Output:** territory map with assignment rationale and review schedule.

---

## Framework 9: Hunt Mode / Kill Mode

A sales rep's day operates in two modes. If they are not in one, they are in the other.

**Hunt Mode:** Everything a rep does to get prospects on the phone. Sharpening tools, laying snares, tracking targets. Hunting maximizes opportunities and increases conversion through preparation.

**Kill Mode:** Everything a rep does while on the phone to get the sale. Bringing the pain, making the offer, looping objections, going for the close. Kill Mode maximizes conversion and increases future opportunities through referrals.

**The formula:** Max Opportunities x Max Conversion = Maximum Sales

Hunting is more important than killing because you cannot kill without something to shoot. If a rep is not on a close call, they should be getting prospects on close calls.

### Lead Priority System

Reps work prospects in the order they are most likely to buy:

**Priority 1: Inbound Sets**
- Prospects who booked an appointment but have not spoken to a closer yet
- Newest, freshest, highest value appointments
- If you get an inbound notification, call immediately
- Objective: pull the close call forward to right now. If not now, later that day.
- Double dial before texting

**Priority 2: BAMFAMs (Book A Meeting From A Meeting)**
- Already spoken to a closer, have not bought yet, have another call scheduled
- Objective: keep them engaged so they show up to the next call
- Send value messages between meetings

**Priority 3: Pipeline**
- No-showed or declined but you still have permission to contact
- Work newest to oldest
- Start with people who declined or no-showed today
- Continue going back in time up to 60 days
- Objective: book them for a close call

**Color code system for lead tracking:**

| Color | Status | Action |
|---|---|---|
| Yellow | Unclosed, no response | Pipeline text sent |
| Green | Unclosed, responded | Lead responded to pipeline text |
| Purple | Closed | Referral text sent |
| Grey | BAMFAM | BAMFAM nurture sent |
| Red | Deliberate opt out | Remove from list |

### Outbound Block and Pickup Primetime

Every rep does outbound after working their list. The end of the day has the highest pickup rates, so that block is sacred.

**Outbound Priority 1: Referrals.** Reach back out to existing customers. Double dial and text, pay a compliment, ask for people like them. Referrals are the best leads you can get.

**Outbound Priority 2: Opt-ins.** Double dial and text unscheduled leads who opted into your marketing list, newest to oldest.

**Targets:** Two sets per hour from outbound. Four total in a two-hour block. Four sets should produce at least one close. Plus referrals, every closer should generate two additional deals per day from outbound alone.

### Call Notes Template

Call notes increase conversion. If you know your prospect, you know what offer is best and how to prepare for objections ahead of time. Review night before and morning of each call.

| Field | Purpose |
|---|---|
| Owner Name | Personalization |
| Business Name | Context |
| Business Industry | Relevance |
| Years in Business | Stage |
| Revenue | Qualification |
| Profit | Qualification |
| What They Sell | Offer mapping |
| How They Get Customers | Current state |
| Needs Help With (Constraint) | Discovery prep |
| Potential Objections | Looping prep |

### End of Day Checklist

You win tomorrow today. Reps close out every day with this:

1. **Record call outcomes:** Mark in CRM as Closed, BAMFAM, Pipeline, or Opt-Out. This sorts leads by priority automatically.
2. **Update call notes:** Add any new information learned about prospects.
3. **Update opt-outs:** If someone explicitly asks to stop contact, opt them out.
4. **Submit worst call for review:** The call with the most trouble that day. Manager uses it for training and 1-on-1s. Five calls per week total.
5. **Inbox zero:** Respond to all lead messages across all channels that built up during the day.

---

## Framework 10: Sales Training Cadence

### Roleplay 5-Step Framework

Roleplay is the best training after real-world experience. Use this structure every time:

1. **Frame it:** Manager explains what to practice, how to do it, and why.
2. **Model it:** Manager demonstrates the technique.
3. **Copy it:** Rep copies the manager's demonstration.
4. **Practice it:** Rep roleplays until they get it right. Expect lots of feedback. Do not get frustrated. Be grateful you get as many reps as you need to master it.
5. **Recap it:** Manager recaps the roleplay and moves to the next one.

### Daily Team Training (30 minutes, Mon-Fri)

1. **Shoutouts and testimonials:** Recognize wins. Share positive customer feedback. Build conviction.
2. **Script training (rotated by section):**
   - Monday: Introduction
   - Tuesday: Discovery
   - Wednesday: Offer
   - Thursday: Looping / Objection handling
   - Friday: Hot topic (the highest-impact area that week)
3. **Roleplay:** Using the 5-step framework above on that day's script section.

### Weekly Team Training (60 minutes, once per week)

1. **Shoutouts:** Highlight wins from the week.
2. **Gametape Review:**
   - Manager selects 3 to 5 recent calls
   - Tells the team what to look for and why
   - Team observes the recording
   - Manager models proper technique
   - Manager roleplays with team members until they nail it
   - Manager recaps
3. **Roleplay:** Practice on the skills surfaced from gametape.

### Weekly 1-on-1 (30 minutes)

1. **Pulse check:** "How are you feeling, 1 to 10?" If 7 or above, move on. Below 7, focus on that first. If their life is on fire, nothing else matters.
2. **Short-term goals:** One skill focus for the week based on current performance. Sticky note on screen as a reminder.
3. **Long-term goals:** What to focus on this week to advance their career goals. Skip this if current performance is below standard. Fix today before building tomorrow.

### Intensive 14-Day Sales Onboarding

For teams running a script-based sales process. This supplements the 90-day plan in Framework 6 by front-loading the first two weeks.

**Phase I (Days 1-2):** Memorize the script. Two manager check-ins per day. Shadow existing reps. Pass test: deliver the full script from memory.

**Phase II (Days 2-3):** Perfect script delivery. Focus on tone and recaps. Review gametape. Pass test: deliver script with correct tone and natural recaps.

**Phase III (Days 3-4):** Memorize objection loops. Roleplay with skill focus. Pass test: handle all objection types using the looping framework.

**Phase IV (Days 4-14):** Live calls. One manager check-in per day. Solo rehearsals. Gametape review. Pass: meet live call performance standards.

After passing Phase IV, the rep transitions to the ongoing training cadence above.

**Script memorization:** Phase I does not pass until the rep can deliver the full script from memory, so pick a memorization drill and hold that bar. The script content and templates themselves belong to the adjacent individual-selling discipline, not to this skill: source or write them there first, then run this training cadence on top of them.

---

## Output formats

- **Org design:** recommended structure for current stage + headcount plan
- **Comp plan:** OTE, split, quota, accelerators, ramp, commission structure
- **Pipeline:** stage definitions, forecast model, coverage calculation
- **Methodology:** recommendation with implementation steps and CRM fields
- **Hiring:** JD + interview scorecard + onboarding plan
- **Onboarding:** 90-day plan with weekly milestones
- **Performance:** dashboard + coaching focus areas
- **Territory:** assignment map with rationale

---

## Adjacent disciplines (where this skill stops)

- Individual selling skills: discovery process, objection looping, tone, and the script content itself. This skill owns the team and the training delivery; that one owns the rep's skillset and the scripts.
- Lead generation feeding the pipeline.
- The handoff from sales to customer success after close.
- CRM pipeline setup and workflow automation, in whichever CRM you run (HubSpot, Salesforce, Pipedrive, GoHighLevel, or similar).
- Company-wide org design and hiring sequences at each stage, beyond the sales org.
- Content created from sales objection mapping.
