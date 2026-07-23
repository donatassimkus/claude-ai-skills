---
name: growth
description: "Growth strategy through marketing channels: funnel analysis, channel prioritization, offer design, MRR planning, weekly planning, acquisition strategy, the Marketing Machine (customer-generated ad system), and objection-to-content mapping. Use when asked for a growth plan, channel strategy, weekly priorities, or why a specific marketing channel is underperforming."
user-invocable: true
argument-hint: [project or goal] [optional: timeframe or focus]
---

## Growth Skill

Growth work filters through one question: does this move revenue? If not, cut it or deprioritize it.

**Project context is loaded from the active CLAUDE.md. Use project-specific goals, MRR targets, current numbers, and constraints from that context.**

**Companion tactics (always pair with strategy).** This skill gives the framework. For execution, also pull specific named tactics from whatever tactics library the human has available, covering marketing, SEO, distribution, virality, pricing, sales, and ops, and surface them alongside the strategy, risk-tagged white / grey / black. Never answer a strategy question from frameworks alone when a matching tactics library exists.

---

## When invoked

The human's request specifies the project and/or focus.
If no project is named, default to the primary project defined in the active CLAUDE.md.

---

## Frameworks

### Funnel-first model

Before proposing any tactic, model the funnel:

```
Traffic x Signup Rate x Paid Conversion x ARPU = MRR
```

1. Define current state for each stage
2. Define target state
3. Identify the biggest leak (lowest performing stage)
4. All tactics attack the biggest leak first

Never propose tactics in isolation. Every tactic gets attributed to a funnel stage and an MRR impact estimate.

For page-level conversion optimisation (landing pages, A/B tests, UX heuristics), run a dedicated conversion-optimisation pass; it is out of scope here.

### MRR estimation

- Use the funnel model, not flat guesses
- Chain related tasks: keyword research + content + distribution = content engine. Estimate the engine's output, then distribute MRR attribution across tasks proportionally
- Infrastructure tasks carry downstream revenue attribution
- Every estimate includes the assumption behind it

### Offer design (Hormozi framework)

Every offer must answer:
- Dream outcome: what does the customer get?
- Time to result: how fast do they see value?
- Effort required: how easy is it?
- Risk reversal: what removes the buying objection?

If the offer does not feel like a no-brainer, it is not ready.

### Prioritization

Rank all initiatives by:
1. Revenue impact (use funnel model)
2. Time to impact (weeks, not months, is better)
3. Effort required (hours to ship)
4. Dependencies (does it block or enable other work?)

Kill anything with no clear revenue attribution and no downstream value.

---

## Output formats

### Weekly plan ([available hours per week from context] max)
Set the hours cap from the project context. Default to whatever constraint exists for the user's situation.

**A) This week**
- 3-6 actions
- Each includes: goal, steps, hours estimate, metric, definition of done
- Total hours must not exceed the weekly cap

**B) Next 30 days**
- 3-5 initiatives
- Each includes: why, expected MRR impact, dependencies, risk level, metric

**C) What to measure**
- 5-10 metrics
- Include: target direction, where to measure (billing system such as Stripe, analytics such as GA4, Search Console, [CRM], etc.)

**D) Questions (only if needed)**
- Ask only what is required to avoid a wrong plan

### Growth strategy

1. Funnel snapshot: current state at each stage
2. Biggest leak: where the most revenue is being lost
3. Top 3 initiatives: ranked by revenue impact
4. Channel recommendation: one primary channel, one test
5. 30/60/90 day milestones

### Channel evaluation

For each channel:
- Fit score: does the audience actually live here?
- Speed: how long to see signal?
- Cost: time and money
- Scalability: can this become a system?
- Verdict: test, build, or ignore

---

## Principles that apply to all growth work

- Ship the smallest version that can go live now. No big redesigns.
- Weekly hours cap applies. Every plan fits the constraint from context.
- Automate anything repeatable. Manual work is a last resort.
- Paid is on the table when the math works. Always include: channel, offer, landing page concept, break-even logic, success threshold.
- White hat, grey hat, and black hat tactics are all on the table. Label risk level (low/medium/high).
- One primary project per week. No scatter.
- If a plan does not contribute to the revenue target, kill it.

---

## The Marketing Machine

A system for generating a continuous flow of customer-generated ad content without relying on the founder's face or camera time.

Source: Alex Hormozi's Marketing Machine material. The node structure and the 6-point testimonial script below are his; what follows is condensed for growth planning.

**Core insight:** The bottom of the business (sales calls, support, events, community) is already generating proof. The machine captures and uses it. 80% of top-performing ads typically do not feature the founder. Customer-generated content outperforms polished founder content for most direct response goals.

**Why it matters for growth:** A business dependent on the founder's face is less scalable and less saleable. The Marketing Machine breaks that dependency while producing more, better ads at lower cost.

### The 7 Nodes

Turn on nodes in this order when starting from scratch:

1. **Testimonial Competition** — fastest influx. Announce a competition, judge winners by actual ad conversion over 30 days, award a meaningful prize. Run 1-2x per year max (audiences fatigue).

2. **Chat/Messaging Scrape** — capture screenshot wins from support/account rep chats. Create a keyword list (e.g. "sales," "revenue," "closed," "profit," "win"). Reps save screenshots to a shared folder weekly. Manager rewards for contributions.

3. **Community Scrape** — screenshot posts from communities you manage. Run a Friday "wins of the week" prompt. Screen record scrolling through win threads for yet another ad format.

4. **Reviews Scrape** — pull from all external review platforms (Google, Trustpilot, Yelp, Facebook, etc.). Sort by newest. Screenshot the best. Set calendar reminders to do this weekly.

5. **Social Media Scrape** — monitor your brand hashtag and customer tags across all platforms. Save before stories disappear (24-hour window). Best organic performers correlate directly with best ad performers.

6. **Bonus Unlocks** — create a desirable training, resource, or access tier. Price it. Tell customers they can buy it or unlock it free by sending a testimonial video hitting the 6-point script to a dedicated proof inbox (proof@[your-domain]).

7. **Award Unlocks** — create an aspirational milestone for customers (a trophy, recognition, status). To claim it, they must submit 4 forms of proof: community post with results, testimonial video by email, unboxing video, on-stage or on-camera presentation. One award = 4 usable ad assets per customer.

**Lifecycle Ads (highest production, highest payoff):** Record all customer calls (sales, onboarding, support, upsell, milestone). Clip 3 moments per customer: before (sales call), during (support call), after (ascension/milestone call). This shows the full journey in one ad, before you can "see" it rather than just hear it described.

**In-Person Events (if applicable):** Capture 3 ad types: stage photos/videos (you on stage with audience behind you), professional testimonials (dedicated side room, 2-camera team, use the 6-point script), and man-in-the-street (rapid 10-question soundbite compilations, 10+ responses per question).

### The 6-Point Testimonial Script

Use for all recorded testimonials — events, bonus unlocks, award unlocks, competitions:

1. Internal struggle: "What was rock bottom before? What did you hate doing? What were you unable to do?"
2. External struggle: "What were your objective numbers/metrics before?"
3. Skepticism: "What were your main concerns before joining/buying?"
4. Overcome: "What made you do it anyway?"
5. External victory: "What are your objective numbers/metrics now?"
6. Internal victory: "What's been the best moment since? What can you now do that you couldn't before?"

The hook is the most important part. Have them record a few different hook variations before telling their story.

### Weekly Marketing Machine Checklist

Every week, marketing team collects:
- Names of customers who got results that week
- Scraped social media (tags, stories, images, videos)
- Chat screenshots from account reps
- Community win posts and comments (screenshots + screen recordings)
- New 5-star reviews from external sites
- Bonus unlock submissions
- Award delivery content
- Customer reaction videos (unboxing, first-use, demonstrations)

Every 6 months (from events + competitions): large proof influx. Sequence your competition between events so you get a proof spike every 12 weeks.

### When to Build the Marketing Machine

Start as soon as you have customers with results. The first step (competition) works with even a handful of customers. If you have no customers yet, do warm outreach, work for free, and get testimonials before spending on ads.

---

## The 5 Stages of Entrepreneur: Valley of Despair Model

The full framework — the stage table and the Valley of Despair curve — belongs to business-model strategy rather than growth, and is out of scope here.

**The short version for growth planning:** growth tactics must account for stage. Stage 2 businesses need acquisition consistency above all. Stage 3 businesses need retention and systems before more acquisition. Stage 4 businesses need margin recovery before scale. Misdiagnosing the stage leads to the wrong tactics applied with the right effort.

---

## Business Diagnostic (Full Audit Mode)

Use this when auditing a business from scratch — new client, acquisition target, or your own business with fresh eyes. Works through the constraint sequence Hormozi uses in live consulting.

**Step 1: Baseline**
- Annual revenue and monthly run rate
- Gross margin and net margin
- Revenue trend (growing, flat, declining — and for how long)
- Number of active customers and average transaction value

**Step 2: Pricing audit**
- Are prices set based on value to the buyer, or based on the founder's own comfort level?
- Is there a premium/high-ticket version of the offer that could exist but doesn't?
- What would happen to volume if price increased 20%? If the answer is "not much," raise the price.
- Red flag: founders who say "my market can't afford more" almost always mean "I am uncomfortable charging more."

**Step 3: Offer audit**
- Does the offer clearly solve one specific problem for one specific person?
- Is the dream outcome concrete and believable?
- Is there a risk reversal (guarantee)?
- Is this a commodity offer or a Grand Slam Offer? A full offer-design audit is a separate pass.

**Step 4: Lead generation audit**
- Which of the Core Four (warm outreach, content, cold outreach, paid ads) are active?
- What is the primary lead source? What percentage of leads come from it?
- Is there a referral system or affiliate system running?
- Is lead flow consistent or feast-and-famine?
- Red flag: single-source lead dependency above 70% of volume.

**Step 5: Conversion audit**
- What is the lead-to-booked rate?
- What is the close rate on sales calls?
- Where do most leads drop off?
- Red flag: high lead volume but low conversion = offer or sales problem, not a leads problem.

**Step 6: Constraint identification**
- Where is the single biggest bottleneck? (Most businesses have one clear constraint — fix that first.)
- Common constraints by stage:
  - Early stage: no consistent lead source
  - Growth stage: offer doesn't convert at scale or fulfilment breaks
  - Scale stage: owner dependency, no systems, margin compression

**Step 7: Priority sequence**
Fix constraints in this order (highest ROI first):
1. Pricing — fastest margin improvement, no new customers required
2. Offer — improves conversion on existing lead flow
3. Lead generation — only scale acquisition once offer and conversion work
4. Operations/fulfilment — don't optimise delivery before the front end works

**Output format for a full business diagnostic:**
1. Baseline snapshot (one paragraph: numbers, trend, stage)
2. Biggest constraint (one sentence, direct)
3. Priority fix list (ranked, with rationale for each)
4. Quick wins (things that can move in 30 days with no new spend)
5. Red flags (things that will kill the business if not addressed)

---

## Arm Your Salespeople With Content: Objection Mapping

Content is not only a lead generation tool. It is a sales enablement tool. Every objection a salesperson hears represents a piece of content that should exist.

**The principle:** If a prospect voices an objection on a call, there is a near-zero chance they are the first person to have it. That objection is shared by a percentage of your entire audience, most of whom will never get on a call to raise it. A piece of content that directly addresses it converts cold audiences who self-disqualify before ever contacting you.

**The objection-to-content mapping process:**

1. Collect all objections from sales calls (by category: time, money, authority, trust, self-doubt)
2. For each objection, identify the specific fear or belief driving it
3. Create a piece of content that addresses that fear or belief directly — without the context of a sales conversation
4. Distribute that content via the channels the audience uses (organic social, YouTube, email, ads)
5. Route that content back to sales as a "send before the call" or "send after the objection" asset

**Examples:**
- Objection: "I don't have time right now" → Content: "How to get [result] in [time] per week even if you're already stretched"
- Objection: "This is too expensive" → Content: "What [result] is worth / what it costs to not fix this"
- Objection: "It won't work for me / my situation is different" → Content: case study featuring a customer whose situation exactly matches the objection

**Feedback loop:** Sales calls feed the content calendar. Content converts cold audiences who never get on calls. Content also arms sales to send proof at the exact moment of hesitation. Same content, two distribution channels.

**Tracking:** Log objections by frequency. The most common objection gets addressed first. Prioritise by volume, not by what's easiest to address.

For objection handling frameworks and sales call structure, run a dedicated sales-conversation pass.



---

## Events Strategy

Events are a channel, not a tactic. Used correctly, they generate pipeline, accelerate deals, build brand authority, and produce content. Used incorrectly, they consume budget with no attribution.

### Event Types and Goals

| Type | Goal | Best for |
|---|---|---|
| **Conference sponsorship** | Brand awareness + lead capture in a target market | Reaching an audience that already attends; early-stage market presence |
| **Speaking slot** | Authority + inbound interest from the session audience | Thought leadership; warming cold markets; accelerating deals with people who attend |
| **Webinar (hosted)** | Pipeline generation; educating warm leads | Mid-funnel nurture; reactivating dormant leads; product education |
| **Owned flagship event** | Community building; media; brand moat | Later stage; when you have enough audience to fill seats |
| **Partner / co-hosted event** | Shared lead gen; cost split | When a co-marketing partner has a complementary audience |

### Conference Sponsorship: Decision Framework

Before sponsoring, answer these:

1. Does your ICP attend this event in material numbers? (Check last year's attendee breakdown if available.)
2. What is the cost per lead at this event based on typical attendance and your expected engagement rate?
3. Do competitors sponsor here? If yes, is this a table-stakes channel or one where you can differentiate?
4. What is your plan to stand out on the floor? A booth alone produces mediocre leads.

**Sponsorship activation checklist:**
- Pre-event: email your existing leads/customers attending; schedule meetings before the floor opens
- At event: capture badge scans or business cards; run an activity that draws a crowd (demo, game, giveaway tied to your value prop)
- Post-event: follow up within 48 hours while the interaction is fresh; personalise by referencing the conversation
- Attribution: tag all contacts met at the event in your CRM with source and event name

### Speaking Strategy

Speaking generates inbound. The goal of a talk is not applause — it is making the right people in the room want to speak to you after.

**Getting on stages:**
1. Build a speaker one-pager: talk title, description, what the audience will learn, your bio, past speaking evidence
2. Apply to events 3 to 6 months in advance; most event CFPs close early
3. Start with smaller events; use recordings to get larger ones
4. Podcast appearances count as speaking inventory and are easier to get

**Talk structure that converts:**
- Open with a specific claim or result (not a story about yourself)
- Teach one framework or insight that is genuinely useful without buying anything
- Use one case study with real numbers — generic claims produce no trust
- Close with a clear next step: URL, QR code, offer, or invitation to talk

### Webinar Production

Webinars work for mid-funnel leads who need education before they buy.

**Webinar formula:**
1. Topic: address one specific problem your ICP is struggling with right now
2. Title: outcome-first ("How to [result] without [common obstacle]")
3. Registration page: keep it to one field beyond email at most
4. Promotion: email list + LinkedIn + partner co-promotion; minimum 2 weeks of promotion
5. Show rate: industry average is 30-40% of registrants. Improve with reminder sequence: 1 week before, 1 day before, 1 hour before, 10 min before.
6. Structure: 40 min teach, 20 min Q&A. No more than 5 slides before you get to the actual content.
7. CTA: make one ask at the end, not three

**Repurpose every webinar:**
- Record and upload to YouTube
- Cut 3 to 5 short clips for social
- Send the recording to registrants who did not show up (opens the conversation)
- Extract the transcript for a blog post or email sequence

### Owned Flagship Event

An owned event is a brand asset. It takes 12 to 24 months to build the first one worth running. Do not attempt until you have:
- An existing audience of 5,000+ (email list, social following, or customer base)
- A team member who can own logistics full-time
- Budget for venue, production, and promotion without it being a bet-the-company decision

**Why it works at scale:** The attendee list becomes your CRM. Speakers become brand advocates. Media coverage compounds. Sponsors fund the production. The event becomes the annual anchor for the community.

### Event Pipeline Attribution

Events are frequently over-credited or under-credited in attribution models because most CRMs do not capture event touchpoints well.

**Tracking protocol:**
1. Create a campaign or source tag for each event in your CRM before it happens
2. Log every contact met or engaged at the event under that campaign
3. Track pipeline influenced (contact touched the event AND was in a deal) separately from pipeline sourced (first touch was the event)
4. Measure: cost per meeting booked, cost per opportunity created, cost per closed deal
5. Compare to your CAC benchmark across other channels before deciding to renew

**Red flags:**
- Sponsoring the same event year after year without measuring cost per closed deal
- Counting booth scans as leads without a qualification step
- No follow-up system — leads from events decay faster than any other source

For product metrics connecting to funnel analysis (activation, retention curves, North Star), run a dedicated product-metrics pass.

For financial forecasting and MRR modeling, run a dedicated finance pass.

For building and managing the sales team that uses objection-mapped content, run a dedicated sales-management pass.

Two things sit in offer-design territory rather than here:
- Money model sequencing (Attraction, Upsell, Downsell, Continuity)
- The full Value Equation (this skill carries the abbreviated version)

---

## Reference files

| Task type | Reference file |
|---|---|
| 95/5 rule, deadly trio (SEO+YouTube+LinkedIn), six-pillar B2B framework, 90-day pipeline sprint, AI agent squads, named B2B SaaS examples | `references/kb-distilled.md` |
