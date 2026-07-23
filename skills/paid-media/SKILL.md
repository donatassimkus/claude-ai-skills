---
name: paid-media
description: "Google Ads, Meta Ads, LinkedIn Ads: campaign structure, targeting, bidding, creative testing, budget, attribution. GOATed Ads framework, Ad Kaleidoscope, 19 ad archetypes. Use for PPC, media buying, ad hooks, scaling creative."
user-invocable: true
argument-hint: [platform and goal] [optional: budget or current performance context]
---

## Paid Media Skill

The strategic role of paid ads inside a full lead generation system (which acquisition channels to run at all, the lifetime-gross-profit-to-CAC ratio that decides whether paid is viable, and when to start paid) sits upstream of this skill and is out of scope here.

You are operating as a senior performance marketer. Paid media is a tax on weak organic — use it to accelerate what is already working, not to replace what does not exist.

**Project context is loaded from the active CLAUDE.md. Apply all paid media work to that specific product, audience, and unit economics.**

---

## When invoked

If the human's request describes a goal or platform: design the strategy or audit the current setup.
If it describes a performance problem: diagnose root cause first.
If nothing is specified: ask one question — what platform, what goal, and what is the monthly budget?

---

## Before spending anything

Always answer these first:
1. What is the CPA target? (reverse from LTV or deal size)
2. What is the conversion event being tracked? Is it firing correctly?
3. Is the landing page converting on organic/direct traffic? If not, paid will not fix it.
4. What is the minimum daily budget to get statistically meaningful data? (Rule of thumb: 10x target CPA per day)

---

## Google Ads

### Campaign types by goal
- **Search** — high intent, bottom of funnel, best for direct response
- **Performance Max** — automated, Google-optimised across all placements. Use with caution — limited control.
- **Display** — brand awareness and retargeting. Do not use for cold conversion.
- **Demand Gen** — YouTube, Discover, Gmail. Upper funnel.
- **YouTube** — video awareness and consideration

### Search campaign structure
- One campaign per product/service line or audience type
- Ad groups: tight thematic clusters — 5-15 keywords per group
- Keyword match types: start with broad match + smart bidding only if conversion data is mature. Otherwise phrase + exact.
- Negative keywords: build list before launch — brand, competitor, informational queries
- Ad copy: 3 RSAs per ad group minimum, pin headlines 1-2 to control message
- Extensions: sitelinks, callouts, structured snippets minimum. Call extension for phone-driven businesses.

### Bidding strategy progression
1. Manual CPC → establish baseline conversion data (50+ conversions)
2. Target CPA → once conversion data is mature
3. Target ROAS → once revenue data is reliable
Never jump to smart bidding without conversion history — it will optimise for nothing.

### Quality Score levers
- Ad relevance: keywords in headline
- Landing page experience: keyword on page, fast load, clear CTA
- Expected CTR: test headlines aggressively

---

## Meta Ads (Facebook/Instagram)

### Campaign structure (2024+ approach)
- Advantage+ Shopping Campaigns for ecommerce
- Manual campaigns for lead gen and B2B
- Campaign → Ad Set (audience + budget) → Ads (creative variants)
- Consolidate ad sets — Meta's algorithm needs volume to optimise (50+ conversions per week per ad set)

### Targeting
- Broad targeting + strong creative is now more effective than narrow interest targeting for most accounts
- Lookalikes: still valuable for cold audiences, build from best customers (not all leads)
- Retargeting: separate campaign, website visitors + video viewers + engagement audiences
- Exclusions: always exclude current customers from acquisition campaigns

### Creative strategy
- Creative is the primary lever on Meta. Audience is secondary.
- Test format before testing message: video vs static vs carousel
- Hook in first 3 seconds determines everything on video
- UGC-style outperforms polished production for most direct response objectives
- Test 3-5 creative concepts, kill losers at statistical significance (95%+), scale winners
- Creative fatigue: monitor frequency. Above 3.0 on a winning ad = refresh creative.

### Meta attribution
- 7-day click, 1-day view is standard — align with your actual sales cycle
- MER (Marketing Efficiency Ratio = total revenue / total ad spend) as a sanity check alongside ROAS
- Compare Meta-reported conversions vs actual CRM/backend conversions — there is always a gap

---

## LinkedIn Ads

### When to use LinkedIn
- B2B only, with specific job title / company size / industry targeting
- LTV must justify the CPL ($50-150+ CPL is normal)
- Enterprise B2B example: decision makers are CMOs, CTOs, and digital transformation leads

### Campaign types
- Sponsored Content (single image, video, carousel) — most used
- Message Ads — high CPL but high intent, use for events/demos
- Lead Gen Forms — reduces friction vs external landing page, lower quality leads
- Conversation Ads — branching message sequences

### Targeting approach
- Job title + seniority (not just title — seniority filter matters)
- Company size: enterprise vs SMB behave differently
- Company list targeting: upload CRM accounts for account-based marketing
- Audience size: 50k-500k for cold. Below 50k = limited delivery.

### LinkedIn benchmarks
- CTR: 0.4-0.6% is decent, above 1% is strong
- CPL: $50-150 depending on offer and audience
- Conversion rate landing page: 5-15% for a gated asset, 1-3% for demo request

---

## Ad Creative Framework (GOATed Ads)

This framework applies across all platforms. Creative is the primary variable in performance advertising. Targeting is secondary. Better creative is what lets you scale past any ceiling.

### Why Ads Hit a Wall

Ads start profitably targeting warm, aware audiences. As spend scales to larger, colder audiences, the creative must work harder to convert them. Most businesses hit a ceiling not from market saturation, but from running weak creative against progressively colder traffic.

The solution: make more, better ads. Not find new platforms.

### The 5 Levels of Audience Awareness

Eugene Schwartz's framework, adapted for ad creative strategy. Knowing where your audience sits determines what the hook should say.

| Level | Who They Are | Hook Type |
|---|---|---|
| **Most Aware** | Know your brand, just need the deal | Offer-driven |
| **Product Aware** | Know what you sell, unsure if it's for them | Proof-driven |
| **Solution Aware** | Know the outcome they want, don't know you deliver it | Promise-driven |
| **Problem Aware** | Sense a problem, unaware solutions exist | Pain-driven |
| **Completely Unaware** | Don't know they have a problem | Curiosity-driven |

**Why this matters for scaling:** Early campaigns work because they reach warm, high-awareness audiences. As budgets scale, you reach colder audiences — hooks must shift from offer-driven to pain-driven or curiosity-driven to convert them.

**Default:** If 90% of your hooks target the warmest tier, spread them across awareness levels. When in doubt, write broader.

### The Ad Assembly Formula

Ads are assembled, not created.

**Formula:** 50 Hooks × 3–5 Meats × 1–3 CTAs = 150–750 ads per week (recording session)

**Time allocation in prep:**
- 80% on hooks
- 20% on meat
- ~0% on CTAs

Rationale: if the hook does not work, nobody sees the rest. The hook is the gate. Invest accordingly.

**Side benefit:** Volume of creative variants makes it impossible for competitors to identify and copy your winners.

### Writing Hooks

**Sources (in order of reliability):**
1. Your own previous winning ads — reuse hooks that converted before
2. Your organic content — posts, shorts, or emails with high engagement contain proven hooks
3. Competitor ads — extract hooks from ads in adjacent industries, not just your own
4. High-performing content from other creators in your category
5. Platform ad libraries — last resort; most advertisers do not know what works

**Hook types by awareness level:**

| Awareness Level | Hook Strategy | Example Structure |
|---|---|---|
| Most Aware | Lead with the offer | "[Discount or deal] on [product] this [time period]" |
| Product Aware | Lead with proof at scale | "[N] customers got [result] last month using [product]" |
| Solution Aware | Lead with the fastest path to the outcome | "The fastest way to [outcome] — introducing [mechanism]" |
| Problem Aware | Name the pain, imply a solution exists | "Tired of [specific frustration]? There is a better way." |
| Completely Unaware | Open a curiosity gap | "The hidden [thing] that is costing [them] [loss] every [period]" |

**Pro tip:** Memes and meme-like content (culturally resonant for your specific audience) function as awareness-level-agnostic hooks. They get attention from everyone and filter to the relevant. A relevant meme works like a moth to a flame.

### 5 Ad Formats (the Meat)

The body of an ad. Rotate less often than hooks — fewer people see it, so 3–5 variations per recording session is sufficient.

**Format 1: Demonstration**
Live use, reactions, unboxing, before/after comparisons, high-production hero ads.
- Product or service in action
- Comparison (old way vs. new way)
- High-production lifestyle demo (fast cuts, product + results throughout)

**Format 2: Testimonial**
Real results from real people. Most credible format.
- UGC (user-generated content, raw footage)
- Direct-to-camera testimonial
- Podcast-style interview
- Group testimonials / parade of proof (multiple people holding up results — most effective)
- Walk-and-talk
- Influencer collaboration

**Format 3: Education**
Teach something useful. Builds trust with cold audiences.
- How-to / tutorial
- Whiteboard explainer
- Listicle video
- Repurposed high-performing organic content

**Format 4: Story**
Narrative that connects emotionally.
- Problem → Solution arc
- Lifestyle or aspirational
- Founder origin story
- Brand manifesto
- Humour or comedy

**Format 5: Faceless**
No spokesperson needed. Useful for testing quickly or when talent is unavailable.
- Screenshots of customer messages or reviews
- Text-only with motion
- Slideshow
- Animation or cartoon
- Screen recordings

### CTA (Call to Action)

**Principle: Clear beats clever.**

If the hook and meat worked, the prospect has maximum motivation for minimum time. Tell them exactly what to do next. Do not make them infer it.

**CTA structure (tell AND show):**
1. What to do: "Click the button below"
2. How to do it: "Tap the button at the bottom of your screen"
3. When to do it: "Before [deadline]"
4. What they get: "And get [offer/result]"
5. What happens next (optional): "You'll be taken to a short form"

Show the next step visually if possible — demonstrate clicking, filling in a form, or calling. Congruence between ad and landing page increases follow-through.

**Make 1–3 CTAs per session.** A sound CTA has never broken a campaign. No CTA has.

### Scaling Process

1. Launch many creative variants — you do not know which will win
2. Different hooks appeal to different awareness levels and audience segments
3. Monitor which combinations outperform
4. Double down on winning hooks — reuse them to make more winning variants
5. Kill losers at statistical significance. Do not average the budget across all variants.
6. Repeat weekly

**The scaling ceiling is always creative.** The business with the best creative can outspend every competitor profitably. Better creative = lower CPM + higher CTR + higher conversion = more customers at lower cost.

### The Ad Kaleidoscope: Multiplying Winners

You will tire of your ads before your prospects even know your name. When an ad works, keep running it until it stops working, never until you get bored.

80% of ad results come from 20% of winners. The Kaleidoscope puts 80% of your effort into making permutations of proven winners, and 20% into testing totally new ideas.

**4-Step Process:**

1. **Identify Winners:** Find your top performers (top 20%, 10%, 5%). The more ads you make, the more winners you have to Kaleidoscope.
2. **Remix Winners (80% of effort):** Post-production variations using the same raw footage. Fast to produce. Fatigue faster.
3. **Remake Winners:** Re-film with real-world changes. Takes more effort but keeps a winner performing for months or years.
4. **Try New Ideas (20% of effort):** Test completely new concepts. When a new winner emerges, put it through the Kaleidoscope. Repeat.

**Remix Checklist (post-production, easiest to hardest):**

| Variation | What to change |
|---|---|
| New Speed | Play at 1.1x or 1.2x (voice must still sound natural) |
| New Filters | Black and white, sepia, higher contrast |
| New Background/Border | Swap background colour, add a coloured border/trim |
| New Fonts/Captions | Change text styling, font weight, caption format |
| New Headline | Replace text overlay with different copy |
| New Medium | Extract video frame as standalone static image |
| New Format | Resize for different placements (square, vertical, horizontal) |
| New Meat | Keep winning hook, splice in a different body section |
| New Effects | Add motion graphics, stickers, animations |

**Remake Checklist (re-filming, easiest to hardest):**

| Variation | What to change |
|---|---|
| New Clone | Same script, same setting. Re-record. Micro-differences (lighting, energy, timing) make it fresh. |
| New Props | Swap objects, costumes, hairstyles, accessories. Same script. |
| New Examples | Change names, numbers, or case study details in the same script. |
| New Setting | Same script in a different location (office, outdoors, studio, car). |
| New Talent | Different spokesperson matching the target avatar's demographics. Wildly underused. |
| New Combination | Multiple changes at once (new prop + new setting + new filter). |

**Key insight:** Remixes are instant but fatigue fast (days to weeks). Remakes take recording time but last months to years. Do both simultaneously. When one remix or remake outperforms the original, it becomes the new baseline.

For 19 specific ad framework blueprints with step-by-step production instructions, see `references/ad-frameworks.md`.

### Ad Production Checklist

Use this before every ad recording session.

**Visual Elements:**
- Must: Paired verbal and visual hooks, movement (toward camera outperforms static), avatar-matching spokesperson, show what you tell, captions, platform-native format
- Nice: Aspirational setting, trending visual formats, real-world demonstrations, props

**Verbal Delivery:**
- Must: Simple words, clear enunciation
- Nice: Specific details and numbers, continuous open-looped curiosity, benefits and pains described through prospect's real life experiences

**Ad Script:**
- Must: Call out prospects, compelling reason why, comparisons (old way vs new way), dream outcome and nightmare of staying the same, speed to result and delay of inaction, certainty of new path and risk of current path, ease of result and difficulty of current path, as many proof points as possible
- Nice: Damaging admissions, stakes/struggles/investment

**CTA:**
- Must: One clear verbal and visual next step
- Nice: Reasons to act now, CTA congruent with hook, scarcity and urgency, bonus or incentive

### Visual Performance Principles

- **Movement outperforms static.** Ads where the talent walks, moves toward camera, or gestures almost always beat talking-head delivery.
- **People in unison stop the scroll.** Groups doing the same thing at the same time (synchronized action, lines, crowds) command attention better than any narration.
- **Show the opt-in flow.** Screenshare the landing page or demonstrate clicking through the form. Reducing uncertainty about the next step removes the final conversion barrier.
- **Non-verbal ads get more organic reach.** If the proof is visual enough to need no explanation, cut the narration. Non-verbal clips also perform better as organic content.

---

## Budget allocation principles

- 70% to proven channels, 20% to testing, 10% to experimental (this applies to channel budget allocation; the same ratio works for creative variation within a single channel)
- Do not spread budget too thin — concentration wins over diversification at early stage
- Minimum viable budget per channel to get signal (adjust to local currency): Google Search [local currency]500-1000/mo, Meta [local currency]1000-2000/mo, LinkedIn [local currency]2000-3000/mo
- Cut channels that cannot hit CPA target within 90 days of proper testing

---

## Tracking and attribution

- Conversion tracking: Google Tag via GTM for Google Ads, Meta Pixel for Meta, LinkedIn Insight Tag for LinkedIn
- Server-side tracking: implement where possible — iOS restrictions have degraded browser-side accuracy
- UTM parameters: mandatory on every paid link. Standard: source/medium/campaign/content/term
- Weekly reporting: spend, impressions, clicks, CTR, conversions, CPA, ROAS

---

## Output format

**For a campaign build:**
- Account structure (campaigns, ad sets, targeting)
- Bidding strategy and budget allocation
- Creative brief (formats, hooks, angles)
- Tracking setup checklist

**For a performance audit:**
1. Conversion tracking — is it accurate?
2. Biggest waste (keywords, audiences, placements)
3. Quick wins (bid adjustments, negative keywords, creative refresh)
4. Structural changes needed

**Rules:**
- Never recommend a channel without stating the minimum budget for meaningful data
- CPA target must be established before any recommendations
- Attribution is always broken — always triangulate with backend data

---

## Advertising vs. Optimization: The BOOM Principle

Advertising is a Business Order of Magnitude change. A strong campaign can 100x a business. Optimizations (conversion rate, close rate, delivery improvements) are capped at 100% improvement by definition.

Most businesses cycle through optimization loops — tweaking the funnel, closing process, or delivery — when the correct move is increasing advertising volume. Optimization improves what exists. Advertising multiplies reach.

**When to advertise vs. optimize:**
- Optimize first when conversion rate is below baseline (page, offer, or sales process is broken)
- Advertise when the core funnel converts and the bottleneck is reach, not conversion
- If CPL is rising but CPM is flat: the offer or creative is the problem, not the audience size

**Volume solves apparent volatility:** What looks like inconsistent results is usually insufficient volume. A business closing one customer per week has 1/52nd of the data needed to produce statistically meaningful signal. Fix: calculate annual goals, convert to daily targets, reverse-engineer required daily ad activity.

**The only metric that justifies pausing:** Negative ROAS after sufficient data volume (minimum 3x target CPA in spend). Pausing early because of day-to-day variance kills campaigns that would have become profitable.

---

## High-Info vs. Low-Info Buyers

Buyers exist on a spectrum of information required before purchasing, not a simple emotional/rational binary.

**Low-info buyers:** Make fast decisions with minimal content consumption. Competed for by every advertiser. Short-form ads, direct response, and strong offers capture them.

**High-info buyers:** Require multiple touchpoints, longer content, proof accumulation, and time. They represent the majority of the market. Mostly ignored because they do not respond to short-form ads.

**Strategic implication:**
- A full funnel serves both: short-form content and direct ads capture low-info buyers; long-form content, email, and video nurture high-info buyers over time
- When scaling hits a wall after targeting only low-info buyers, the answer is not a better hook — it is nurture infrastructure for high-info buyers
- High-info buyers tend to have better LTV, lower churn, and higher referral rates

**Audience-channel alignment:**
- Low-info buyers: direct response ads, strong offers, retargeting
- High-info buyers: content, email nurture, YouTube, podcasts, case studies, webinars

For the unit economics and CAC math behind budget allocation decisions, run a dedicated finance pass.

---

## Out of scope

The full hook taxonomy and hook-testing framework is a separate discipline. This skill carries the hook guidance that paid creative needs; a dedicated hooks pass goes deeper.

---

## Reference files

| Task type | Reference file |
|---|---|
| $100M+ ad spend lessons, LinkedIn Ads 2026 playbook, Five Stages framework, Three Cs of media buying, AI creative stack | `references/kb-distilled.md` |
