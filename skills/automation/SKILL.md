---
name: automation
description: "Workflow architecture and design across automation tools. Use for cross-tool decisions, multi-system integrations, and automation strategy. For deep, single-platform builds, use that tool's own dedicated skill or documentation."
user-invocable: true
argument-hint: [tool or platform] [workflow goal or problem]
---

## Automation Skill

This skill handles cross-tool architecture and design decisions. For deep, single-platform work (node config, workflow recipes, funnel setup within one tool such as n8n or GoHighLevel), use that tool's own dedicated skill or documentation.

Automation work defaults to deterministic, simple architectures. AI is a last resort inside workflows, not a default. Every automation should be auditable, debuggable, and maintainable.

**Project context is loaded from the active CLAUDE.md. Use the tech stack and tools defined in that context.**

---

## When invoked

$ARGUMENTS specifies the tool and the workflow goal or problem.
If not specified, ask one question to clarify before proceeding.

---

## Design principles

1. **Deterministic inputs over AI guessing.** If the data needed is structured and predictable, do not use an AI node. Use a formula, lookup, or conditional.
2. **Warn about downstream breakage.** Every workflow has failure modes. Call them out before they happen.
3. **Simpler is better.** If a 3-step workflow solves the problem, do not build a 10-step workflow.
4. **One job per workflow.** Monolithic automations break and are hard to debug. Keep scope narrow.
5. **Error handling is not optional.** Every workflow that touches external APIs needs error paths.
6. **Test before shipping.** Define the test case before building. What input produces what output?

---

## Should you automate this?

Before building anything, run this check.

**Automate when:**
- The task takes 15+ minutes AND happens weekly or more frequently
- The process is error-prone when done manually (wrong data, missed steps, inconsistent execution)
- It requires combining data from multiple sources before making a decision
- A non-obvious automation could remove an entire category of work, not just speed up one instance

**Skip automation when:**
- It's a one-off or happens less than monthly
- Manual effort is under 10 minutes per occurrence
- The setup cost exceeds 3 months of manual time saved
- A CSV export/import or copy-paste gets the job done in one sitting

**Think creatively when:**
- You're making the same judgment call repeatedly (the pattern itself can become a rule)
- Data lives in one system but decisions happen in another (bridge them)
- You're doing manual QA or checks against known thresholds (rule-based automation)
- A human is acting as the "glue" between two systems (that glue is the automation)

**Quick math:** (minutes per occurrence × occurrences per month) vs. (hours to build + hours to maintain per month). If the ratio does not pay back in 3 months, skip it or simplify.

---

## Tool-specific guidance

### n8n

- Prefer Code nodes over complex node chains when logic is conditional.
- Use Set node for data normalization before passing to external services.
- HTTP Request node for APIs without native integrations.
- Webhook triggers for real-time flows; Cron for scheduled jobs.
- Always test with real data, not mock data. Edge cases appear in production, not in samples.
- For example, an SEO blog pipeline: keyword list input node → content QA checklist node → internal linking targets check → publish.

### Make.com (Integromat)

- Routers over separate scenarios when flows share a trigger.
- Use data stores for state that needs to persist between runs.
- Watch the operation count. Loops inside loops kill your quota.
- Error handlers on every module that calls an external API.
- Filters at the router level, not inside individual modules.

### GoHighLevel

- Pipeline stages should map 1:1 to a real buying stage, not internal team stages.
- Automation triggers: be explicit about what fires them. Ambiguous triggers cause duplicate actions.
- Workflow branching: test every branch. Default paths should handle the unexpected case.
- CRM segmentation: tag-based systems break at scale. Use contact fields for permanent attributes, tags for temporary states.
- Sub-accounts: keep automations at the sub-account level unless there is a clear reason to use agency-level triggers.

### Claude (API + MCP)

Claude can act as an automation layer by calling APIs directly, using MCP connections, or receiving webhooks. Use this when the automation requires judgment, analysis, or context-aware decisions rather than simple data movement.

**When to use over n8n/Make.com:**
- The "what to do" decision requires analyzing the data, not just routing it
- One-off or low-frequency tasks where building a full workflow is overkill
- No native integration exists and you would otherwise write custom code
- Chaining multiple API calls with conditional logic based on returned data

**How it works:**
- Direct API calls to any REST API (ad platforms, CRMs, analytics, etc.)
- MCP connections to pull and push data from connected services
- Webhook receivers to process inbound data and act on it
- The pattern: pull data → analyze → decide → push changes back

**Where it fits in the stack:**
- n8n/Make.com: scheduled, high-frequency, deterministic workflows (move data A to B on a timer)
- GHL: CRM-triggered automations (contact enters stage → fire sequence)
- Claude via API/MCP: analysis-heavy tasks, irregular cadences, decisions requiring context or judgment

**Non-obvious opportunities:**
- When analyzing data from any platform, flag repeatable judgment calls that could become automated rules
- Look for patterns across data sources the user may not have connected yet (e.g. ad spend data + CRM close rates = automated budget reallocation logic)
- If a manual review process follows the same decision tree every time, propose turning it into an automation

**Constraints:**
- Auth tokens and API keys must be managed securely. Do not store credentials in plain text.
- Rate limits apply to every API. Build in handling for 429 responses.
- For high-frequency scheduled jobs (every 5 min, every hour), n8n or Make.com is still the better choice. Claude is better for on-demand or weekly cadence tasks.

---

## Output formats

### Workflow design

1. Goal: what problem does this solve?
2. Trigger: what starts the workflow?
3. Steps: numbered, one action per step
4. Data: what goes in, what comes out at each step
5. Error handling: what happens when a step fails?
6. Test case: input example and expected output
7. Edge cases to handle

### Workflow review

1. What it does (confirm understanding)
2. Failure modes identified
3. Simplification opportunities
4. Missing error handling
5. Recommended changes, prioritized

### Architecture recommendation

When choosing between automation approaches:
- State the options clearly, including Claude via API/MCP when analysis or judgment is required
- Give a verdict with reasoning
- Flag cost implications (API calls, operations, time, token usage for Claude-based automations)
- Prefer the option that is easiest to debug when it breaks
- Default to n8n/Make.com for deterministic, scheduled data movement. Default to Claude for tasks where the action depends on interpreting the data.

---

## Common automation patterns

**Content publishing pipeline**
Keyword input → content brief generation → draft creation → QA checklist → internal link injection → CMS publish → tracking setup

**Lead intake and routing**
Form/ad submit → dedup check → lead scoring → pipeline stage assignment → owner assignment → follow-up sequence trigger → notification

**Reporting pipeline**
Data pull from source → transformation → aggregation → push to spreadsheet or dashboard → notification (Slack, email, etc.)

**Outreach sequence**
Lead list import → dedup → sequence enrollment → touchpoint 1 → wait → reply check → touchpoint 2 or remove → conversion tracking

**API-driven performance optimization**
Pull platform report via API (ad spend, search terms, pipeline data) → analyze against targets → flag anomalies or waste → push changes back (negative keywords, bid adjustments, status updates) → log actions taken

**Cross-platform data sync with analysis**
Pull data from source API → compare against second source (e.g. ad platform vs CRM) → identify discrepancies → reconcile or flag → push corrections

**Ad creative production line (Claude Code as orchestrator)**
Performance data import (CSV or API/MCP pull from Meta, Google Ads) → analyze against targets (CTR, CPA, ROAS, frequency) → flag underperformers → sub-agent 1 generates headline variants (matched to the audience's awareness level) → sub-agent 2 generates description/body copy variants → output structured creative brief (CSV, JSON, or direct push to design tool API like Figma) → optional: MCP connection pulls live platform data to close the feedback loop → log all variants and performance deltas for next iteration

Why this works: Claude Code runs sub-agents in parallel, so headline and description generation happen simultaneously. One person can produce 10x the creative volume in a fraction of the time. The loop closes when live platform data feeds back into the next analysis cycle.

Requirements: ad platform API credentials (or CSV exports as a simpler start), MCP server for live data pull (optional), design tool API or template system for final asset production (optional). Start with CSV in, CSV out. Add MCP and design tool connections as the workflow proves value.
