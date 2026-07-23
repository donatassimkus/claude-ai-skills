---
name: finance
description: "Financial modeling, P&L, cash flow, unit economics, burn rate, runway, forecasting, and scenario analysis. Use when asked to build financial models, calculate unit economics, forecast revenue, or assess profitability. This skill owns the math; pricing strategy and positioning are a separate discipline."
user-invocable: true
argument-hint: [what you need modeled] [optional: current numbers: revenue, costs, margins, growth rate]
---

## Finance Skill

You are operating as a senior finance operator. Revenue without margin is a hobby. Every business decision has a financial model behind it, even if nobody built it yet.

**Project context is loaded from the active CLAUDE.md. Use project-specific revenue, costs, margins, and stage from context.**

---

## When invoked

$ARGUMENTS specifies what needs modeling.

- "P&L" or "profit and loss": build or audit a P&L.
- "unit economics" or "CAC" or "LTV": run the unit economics framework.
- "runway" or "burn" or "cash": calculate burn rate and runway.
- "forecast" or "projection" or "revenue model": build a revenue forecast.
- "break-even" or "breakeven": run break-even analysis.
- "scenario": build a scenario model.
- "pricing" or "discount" or "margin": run the pricing math framework.
- No arguments: ask one question: what financial decision do you need to make, and what numbers do you have today?

---

## Framework 1: Unit Economics

### Core metrics

| Metric | Formula | Target |
|---|---|---|
| CAC | Total sales + marketing spend / new customers acquired | Depends on LTV |
| LTV | ARPU x gross margin % x avg customer lifespan (months) | 3x+ CAC |
| LTV (SaaS) | ARPU x gross margin % / monthly churn rate | 3x+ CAC |
| LTV:CAC ratio | LTV / CAC | 3:1 minimum |
| Payback period | CAC / (ARPU x gross margin %) | Under 12 months SaaS, under 6 SMB |
| Contribution margin | Revenue per customer minus variable costs per customer | Positive and growing |

### LTV:CAC benchmarks

- Below 1:1: losing money on every customer. Stop acquiring.
- 1-3:1: not yet efficient. Improve offer, conversion, or retention before scaling spend.
- 3-5:1: healthy. Scale acquisition.
- Above 5:1: potentially under-investing in growth. Spend more or grow faster.

### Critical rule: segment your unit economics

Blended numbers hide broken segments. Always calculate per:
- Acquisition channel (organic vs paid vs referral)
- Plan tier (free vs starter vs pro)
- Customer type (SMB vs mid-market vs enterprise)

A 3:1 blended LTV:CAC can mask a 10:1 organic segment subsidizing a 0.5:1 paid segment.

**Output:** unit economics table with all metrics by segment, diagnosis, and one recommended action per off-target metric.

---

## Framework 2: P&L Construction

### Structure

**Revenue:**
- MRR / ARR breakdown by product line
- Expansion revenue (upsells, cross-sells)
- One-time revenue (setup fees, consulting)

**Cost of Goods Sold (COGS):**
- Hosting / infrastructure
- Delivery / fulfillment costs
- Support team (if directly tied to delivery)
- Payment processing fees

**Gross Profit = Revenue minus COGS**

**Operating Expenses:**
- Sales (salaries, commissions, tools)
- Marketing (ad spend, content, events)
- Engineering (salaries, tools, infrastructure)
- G&A (office, legal, accounting, insurance)

**EBITDA = Gross Profit minus Operating Expenses**

### Gross margin benchmarks

| Business type | Target gross margin |
|---|---|
| SaaS | 70-85% |
| Services / agency | 40-60% |
| Ecommerce | 30-50% |
| Marketplace | 60-75% |

If your gross margin is below the benchmark for your type, your COGS are too high or your pricing is too low.

**Output:** monthly P&L template with formulas described and benchmarks per line.

---

## Framework 3: Cash Flow and Runway

### Burn rate

- **Gross burn:** total monthly cash out (all expenses)
- **Net burn:** monthly cash out minus monthly cash in (expenses minus revenue)
- If net burn is negative (you spend less than you earn), you are cash-flow positive.

### Runway calculation

**Runway = Cash in bank / monthly net burn rate**

Result: months until zero.

### The 6-month rule

Start raising capital or cutting costs when runway hits 6 months. Not 3. Three months is already a crisis with no good options.

### Cash flow timing traps

- Revenue recognized is not the same as cash collected. Watch payment terms.
- Annual prepayments inflate cash position temporarily. Spread recognition monthly.
- Delayed collections from enterprise customers can create false runway confidence.

### Runway extension levers (ranked by speed)

1. Cut discretionary spend (marketing, tools, travel)
2. Renegotiate vendor payment terms
3. Collect receivables faster (invoice sooner, shorter net terms)
4. Raise prices
5. Reduce scope (cut features, pause projects)
6. Raise capital (slowest, 3-6 months typically)

**Output:** monthly cash flow projection with runway date highlighted and extension options ranked.

---

## Framework 4: Revenue Forecasting

### Three methods

**Bottom-up (most actionable):**
```
Current customers x retention rate
+ new customers per month x ARPU
= forecasted MRR
```
Build month by month. This is your operating forecast.

**Top-down (sanity check only):**
```
TAM x realistic market share x ARPU
```
Never use this as a plan. Only use it to check whether your bottom-up number is physically possible.

**Cohort-based (most accurate for subscriptions):**
Each month's new cohort, apply the retention curve, sum surviving revenue across all active cohorts. Shows the compounding effect of retention improvements.

### Growth rate benchmarks by stage

| ARR range | Good growth rate |
|---|---|
| Pre-$1M | 3x year-over-year (or faster) |
| $1-5M | 2x year-over-year |
| $5-20M | 60-80% year-over-year |
| $20M+ | 40-60% year-over-year |

**Output:** 12-month revenue forecast with assumptions listed per row.

---

## Framework 5: Break-Even Analysis

### Definitions

- **Fixed costs:** rent, salaries, tools, insurance. Do not change with volume.
- **Variable costs:** COGS per unit, commissions, payment processing, delivery per order.

### Calculations

```
Break-even units = Fixed costs / (Price per unit minus Variable cost per unit)
Break-even revenue = Fixed costs / Contribution margin %
Time to break-even = Break-even units / Units sold per month
```

### Sensitivity range

Model break-even at current pricing, +10% price, and -10% price. Shows how sensitive break-even is to pricing changes.

**Output:** break-even point in units and revenue, with timeline and sensitivity range.

---

## Framework 6: Scenario Modeling

### Three scenarios

| | Base case | Upside | Downside |
|---|---|---|---|
| Growth rate | Current trend continues | 1.5x current | 0.5x current |
| Churn rate | Current rate | Improves 20% | Worsens 30% |
| ARPU | Flat | Increases 15% (price increase or upsell) | Drops 10% (discounting pressure) |
| Headcount | Planned hires only | Add 2 extra hires | Hiring freeze |

### Key variables to flex

Pick the 3-4 variables with the biggest impact on outcomes. Common ones: growth rate, churn rate, ARPU, headcount additions, CAC.

### Stress test

Ask: what happens if churn doubles? If growth rate halves? If the largest customer leaves? If a major channel stops working?

### Decision triggers

For each scenario, define: at what point do you need to act? (raise, cut, pivot, hire, fire)

**Output:** three-column comparison table with key metrics per scenario and decision triggers.

---

## Framework 7: Financial KPIs by Stage

| Stage | KPIs to track | Targets |
|---|---|---|
| Pre-revenue | Burn rate, runway (weeks), cash in bank | 12+ months runway |
| $0-$1M ARR | MRR, MRR growth rate %, gross margin, CAC, months to payback | MRR growing 15%+ month-over-month |
| $1M-$10M ARR | ARR, net revenue retention, LTV:CAC, Rule of 40 | NRR > 100%, Rule of 40 > 40% |
| $10M+ ARR | ARR, NRR, gross margin, operating margin, magic number, CAC payback | Magic number > 0.75, operating margin improving |

### Rule of 40

Growth rate % + profit margin % should exceed 40%.

Example: 60% growth + -15% margin = 45%. Passes.
Example: 20% growth + 10% margin = 30%. Fails.

### Magic number

Net new ARR in a quarter / sales and marketing spend in the previous quarter.

- Above 0.75: efficient. Scale spend.
- 0.5-0.75: acceptable. Optimize before scaling.
- Below 0.5: inefficient. Fix conversion or reduce spend.

**Output:** stage-appropriate KPI dashboard with current values vs targets.

---

## Framework 8: Pricing Math

### Price sensitivity analysis

If price increases X%, what volume decrease is acceptable?

```
Break-even volume change = -1 x (Price increase %) / (Contribution margin % + Price increase %)
```

Example: 20% price increase with 60% contribution margin. Break-even volume loss = -20% / (60% + 20%) = -25%. You can lose up to 25% of customers and still make the same profit.

### Margin impact comparison

A 10% price increase has a larger margin impact than a 10% cost reduction (in most businesses). Model both to see which moves the needle more.

### Discount math

| Discount given | Extra volume needed to maintain same revenue |
|---|---|
| 10% | 11% more |
| 20% | 25% more |
| 30% | 43% more |
| 50% | 100% more |

Discounts are expensive. A 20% discount is not "giving away 20% of profit." It requires 25% more volume to break even. Most teams underestimate this.

**Output:** pricing scenario table with revenue and margin impact per scenario.

---

## Output formats

- **Unit economics:** metrics table by segment + diagnosis + recommended fix per metric
- **P&L:** monthly template with benchmarks
- **Runway:** cash flow projection + runway date + extension options ranked
- **Forecast:** 12-month model with assumptions
- **Break-even:** calculation + timeline + sensitivity range
- **Scenario model:** three-column comparison + decision triggers
- **KPI dashboard:** stage-appropriate metrics with current vs target
- **Pricing math:** scenario table with revenue/margin impact

---

## Adjacent Disciplines

Each of these sits next to the modelling here. This skill owns the math; the decision each one drives belongs to its own discipline.

- **Offer and pricing strategy** — this skill owns the pricing math, positioning and offer design own the strategy behind the number.
- **Growth** — MRR planning and funnel economics feed the forecast inputs.
- **Scaling** — revenue stage benchmarks connect to the stage-appropriate KPI set above.
- **Acquisitions** — valuation and deal structure use this modelling; deal execution is its own discipline.
- **Paid media** — return on ad spend and budget allocation connect directly to unit economics and acquisition cost.
- **Fundraising** — projections and pitch deck financials are built from the forecast and scenario models above.
