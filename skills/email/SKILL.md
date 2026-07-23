---
name: email
description: Email marketing strategy, sequences, deliverability, segmentation, broadcast campaigns, drip automations, marketing-platform email, and cold email deliverability and sending infrastructure setup. Use when asked about email campaigns, sequences, deliverability, domain warmup, or cold email technical setup. Writing the cold outreach messages and follow-up copy themselves is an adjacent discipline handled separately; this skill owns the infrastructure, the sequence architecture, and the marketing email.
user-invocable: true
argument-hint: [sequence type or campaign goal] [optional: list size or current open rate]
---

## Email Skill

You are operating as a senior email marketer. Email is the highest-ROI channel when done correctly. Every email must earn its place in the inbox.

**Project context is loaded from the active CLAUDE.md. Apply email work to that specific product's audience, funnel stage, and sending infrastructure.**

---

## When invoked

If $ARGUMENTS describes a sequence: write the full sequence with subject lines, send timing, and logic.
If $ARGUMENTS describes a deliverability problem: diagnose root cause first.
If $ARGUMENTS describes a campaign: write the email with subject line variants.
If no arguments: ask one question — what is the goal and what triggered this email or sequence?

---

## Email types

- **Transactional** — triggered by a user action (signup confirmation, purchase receipt, password reset). Highest deliverability, do not abuse with marketing content.
- **Automated sequences** — triggered by behaviour or time (onboarding, nurture, re-engagement). Set and forget, but review performance quarterly.
- **Broadcasts** — one-time sends to a segment. Newsletters, announcements, promotions.
- **Cold outreach** — prospecting to people who have not opted in. Different infrastructure and rules. Writing the outreach copy and sequences themselves is an adjacent discipline; this skill owns the sending infrastructure and deliverability side of it.

---

## Sequence frameworks

### Onboarding sequence (SaaS)
Goal: get the user to the first value moment as fast as possible.

- Email 1 (immediately): Welcome + single next action. Do not overwhelm.
- Email 2 (day 1): The one thing they should do first. Link to it directly.
- Email 3 (day 3): Social proof or case study from a similar user.
- Email 4 (day 5): Common mistake or missed feature.
- Email 5 (day 7): Check-in. Are they stuck? Offer help.
- Email 6 (day 14): Upgrade prompt if on free plan, upsell if on entry plan.

Each email: one goal, one CTA, short.

### Lead nurture sequence (post-signup, pre-sale)
Goal: build enough trust and demonstrate enough value to convert.

- Email 1: Deliver what they signed up for + one insight
- Email 2: Problem they face + how you solve it (no pitch yet)
- Email 3: Case study or result (social proof)
- Email 4: Address the main objection
- Email 5: Soft pitch with clear offer
- Email 6: Urgency or last call

### Re-engagement sequence
Goal: win back inactive subscribers or trigger churn.

- Email 1: "We've noticed you've been quiet" — simple, human
- Email 2: Best content or offer — remind them why they signed up
- Email 3: Direct question — "Is this still relevant to you?"
- If no engagement after 3: suppress or unsubscribe to protect deliverability

---

## Writing emails that get read

### Subject lines
- Short: 30-50 characters, previews cleanly on mobile
- Curiosity gap: "Why I stopped doing X" beats "Our monthly newsletter"
- Specificity: "3 ways to..." beats "Some ways to..."
- Personalisation: first name in subject line still works for warm lists
- Avoid spam triggers: excessive caps, multiple exclamation marks, "free", "guarantee"
- Test 2-3 variants on every broadcast

### Email body
- First line is the pre-header — it appears in inbox preview. Write it intentionally.
- One idea per email. If you have three points, send three emails.
- Plain text outperforms HTML for personal/nurture emails. Use HTML templates only for newsletters and promotional emails.
- Short paragraphs: 1-3 lines. Whitespace is not wasted.
- CTA: one per email, specific, above the fold if possible.

### CTA structure
- Be specific: "Book a 20-minute call" beats "Get started"
- One link: multiple links dilute click-through and confuse intent
- Repeat the CTA at the bottom for long emails

---

## Deliverability

### Technical setup (must-have)
- SPF record: authorises your sending domain
- DKIM: signs outgoing emails cryptographically
- DMARC: tells receiving servers what to do with unauthenticated mail
- Custom sending domain: never send from your marketing platform's shared domain (most all-in-one platforms and ESPs give you one by default, e.g. a `mail.<platform>.com` sender). Always use your own domain.

### Sending reputation
- Warm new domains: start at 50 emails/day, double weekly over 4-6 weeks
- Engagement rate matters: low open rates signal low relevance to inbox providers
- Hard bounces: remove immediately. Above 2% bounce rate = deliverability damage.
- Spam complaints: above 0.1% is dangerous. Keep below 0.08%.
- List hygiene: clean inactive subscribers every 90 days — suppress, do not delete

### Platform-specific notes (all-in-one marketing platforms):
The following applies when sending runs through an all-in-one marketing or CRM platform (GoHighLevel, HubSpot, ActiveCampaign, Keap, or similar) rather than a dedicated ESP. Adjust for your actual platform.
- Use the platform's built-in sending, or connect a dedicated SMTP (SendGrid, Mailgun, Postmark)
- Built-in sending on these platforms is usually shared infrastructure — clean your list, or you damage others on the same IP
- For cold outreach: do not use shared platform infrastructure. Use a separate tool with dedicated IPs.

---

## Cold outreach (prospecting)

This is a different game to marketing email:
- Use a separate subdomain (e.g. hello.yourdomain.com) — never your main domain
- Warmup the sending domain for 4-6 weeks before sending volume (use a dedicated warmup tool)
- Personalisation is mandatory — generic blasts get marked as spam
- Volume: start at 20-30 emails/day per mailbox
- Sequence: 3-4 touchpoints max. More than that damages reputation.
- Always have an easy opt-out — legal requirement (GDPR, CAN-SPAM)

---

## Segmentation

The right email to the right person beats the best email to everyone.

- Segment by: acquisition source, product/feature used, engagement level, plan/tier, industry
- Behavioural triggers beat time-based triggers: send when they take an action, not on a fixed schedule where possible
- Suppress paid customers from acquisition sequences, suppress inactive from product sequences

---

## Key metrics

- Open rate: 20-40% for warm lists (lower since Apple Mail Privacy, treat as directional only)
- Click rate: 2-5% of sends (more reliable than open rate post-MPP)
- Click-to-open rate (CTOR): clicks / opens. Better measure of content quality.
- Unsubscribe rate: below 0.3% per send is healthy
- Revenue per email: most important metric for commercial sequences

---

## Output format

**For a sequence:**
- Email count and cadence
- Each email: subject line, pre-header, body, CTA, send trigger

**For a single email/broadcast:**
- 2-3 subject line variants
- Full email body ready to copy-paste
- Recommended send segment

**For a deliverability issue:**
- Root cause diagnosis
- Fix steps with priority order
- Prevention going forward

**Rules:**
- Plain text by default for nurture and personal emails. Flag when HTML is appropriate.
- Every sequence needs an exit condition — what stops someone from receiving more emails?
- Never recommend sending to a list that has not been cleaned in the last 6 months without a re-engagement campaign first

---

## Adjacent disciplines (where this skill stops)

- Hook writing — subject line craft and hook type taxonomy
- Cold outreach copywriting — the outreach messages and follow-up sequences themselves

---

## Reference files

| Task type | Reference file |
|---|---|
| Cold email systems, the short-opener formula, current deliverability practice (SPF/DKIM/DMARC, warmup, multi-inbox), the video + short text combo, personalization sources, anti-patterns | `references/kb-distilled.md` |
