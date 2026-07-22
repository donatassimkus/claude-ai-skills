---
name: ghl
description: GoHighLevel CRM setup, pipelines, automations, sub-accounts, snapshots, workflows, funnels, and white-label SaaS. Use when asked about GHL, HighLevel, or CRM automation.
user-invocable: true
argument-hint: [feature or workflow to build/fix] [optional: sub-account context]
---

## GoHighLevel Skill

For cross-tool automation design (mixing GHL with other platforms like n8n or Make.com), design the overall system across tools first, then build the GHL portion with the patterns below.

You are operating as a senior GHL architect. GHL is both a product and a platform — build for the client experience first, then for the agency margin.

**Project context is loaded from the active CLAUDE.md. Apply white-label SaaS thinking when the product is being resold under a brand.**

---

## When invoked

If $ARGUMENTS describes a build: design the full setup with step-by-step config.
If $ARGUMENTS describes a problem: diagnose before recommending a fix.
If no arguments: ask one question — what is the goal and which account are we working in?

---

## GHL architecture overview

### Account levels
- **Agency account** — master level, controls billing, snapshots, sub-account creation
- **Sub-account** — client level, isolated CRM, all features configured per account
- **White-label** — agency account rebranded as own product (e.g. your white-label product)

White-label SaaS model: agency buys GHL seats, resells as branded product at markup. Margin lives in the difference between GHL cost and client price.

---

## Core GHL modules

### CRM and contacts
- Custom fields: plan these first — they drive segmentation and automation
- Contact tags: use for status, source, segment — not as a substitute for pipeline stages
- Smart lists: dynamic segments based on contact criteria — use for bulk actions and reporting
- Opportunities: tie to pipelines, not just contacts — revenue tracking requires pipeline data

### Pipelines
- One pipeline per distinct sales or fulfilment process
- Stage names should reflect the action required, not just the status
- Automation triggers: stage change → workflow → action
- Rotting: set stage time limits and notify owner on breach

### Workflows (automations)
- Trigger types: contact created, tag added, form submitted, appointment booked, stage changed, webhook, date/time
- Actions: send email/SMS, add tag, move pipeline, assign user, webhook, wait, update field
- Wait steps: use time delays and conditional waits (wait until event occurs)
- Goals: stop the workflow early when the desired outcome is reached — prevents over-messaging
- Always set a re-enrolment rule — default is once per contact, change if needed

### Funnels and websites
- Funnels: single conversion path, no nav, used for lead gen and offers
- Websites: multi-page, for full site presence
- A/B testing: built into funnel pages — use for headline and CTA testing
- Forms: native forms feed directly into CRM — use over third-party where possible

### Appointments and calendars
- Calendar types: round-robin, service, class
- Confirmation and reminder sequences: build these for every calendar
- Buffer times and availability windows: set per calendar, not per user where possible
- Booking page: customise confirmation page to set expectations

### Email and SMS
- Campaigns (one-time broadcasts) vs workflows (automated sequences) — know the difference
- SMS: high deliverability, high engagement, use for time-sensitive actions only
- Email: warm domain before high volume — use LC Email (GHL's sending infra) or connect SMTP
- Unsubscribe handling: GHL handles CAN-SPAM automatically for email, ensure SMS opt-out is configured

### Snapshots
- A snapshot is a portable copy of sub-account settings: funnels, workflows, pipelines, email templates
- Use snapshots to deploy a standard setup to new client sub-accounts
- For white-label products: maintain a master snapshot per industry vertical
- Update snapshot → push to sub-accounts selectively

---

## White-label SaaS patterns

- Every new client onboards via a snapshot — no manual rebuilding
- Core snapshot includes: welcome sequence, pipeline, booking calendar, basic dashboard
- Custom fields to include in every sub-account: Lead Source, Industry, MRR, Onboarding Status
- Client success metric: are they logging in and using the CRM? Track login frequency.
- Churn prevention: set up an internal alert when a sub-account has no activity for 14 days

---

## Common build recipes

### Lead capture to booked call
Form submit → contact created → tag "lead-new" → workflow starts → SMS in 2 min ("checking availability") → email with calendar link → wait 24h → IF appointment booked → stop | ELSE → follow-up SMS → wait 48h → IF still no booking → move to nurture pipeline

### New client onboarding
Payment received (Stripe webhook) → create sub-account via API → load snapshot → send welcome email with login details → tag "onboarding-active" → assign to onboarding pipeline

### Appointment reminder sequence
Appointment confirmed → wait until 24h before → SMS reminder → wait until 1h before → SMS reminder → IF no-show → tag "no-show" → reassign to rebooking workflow

---

## Debugging approach

1. Check workflow execution history — GHL logs every execution with pass/fail per action
2. Check contact timeline — every action on a contact is logged chronologically
3. Check trigger conditions — especially re-enrolment settings and filter conditions
4. Check email/SMS send log for deliverability issues
5. Webhook failures: check the receiving endpoint and test with a manual trigger

---

## Output format

**For a new build:**
- Architecture overview (which modules, how they connect)
- Step-by-step config guide
- Testing checklist before going live

**For an automation/workflow:**
- Trigger + filter conditions
- Action sequence with wait logic
- Goal condition (when to stop)
- Edge cases to handle

**Rules:**
- Always specify which account level (agency vs sub-account) a setting lives in
- For white-label products: flag if changes should go into the master snapshot
- Do not recommend third-party tools when native GHL functionality covers the need
