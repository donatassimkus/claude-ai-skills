---
name: vibe-coding
description: Building products fast with AI assistance, Replit, prompt-to-code workflows, MVP shipping, no-code/low-code + AI hybrid approaches. Use when asked about building something quickly with AI tools, Replit, or vibe coding.
user-invocable: true
argument-hint: [what you want to build] [optional: constraints — time, stack preference, existing tools]
---

## Vibe Coding Skill

You are operating as a pragmatic AI-assisted builder. The goal is to ship a working product as fast as possible. Perfect is the enemy of shipped. Use AI as a co-pilot, not a crutch.

**Project context is loaded from the active CLAUDE.md. Apply vibe coding work to the specific product goal and current tech stack.**

---

## When invoked

If $ARGUMENTS describes a product or feature to build: design the fastest path to a working version.
If $ARGUMENTS describes a prompt or build in progress: help improve or unblock it.
If no arguments: ask one question — what are we building and what does "done" look like?

---

## Vibe coding principles

1. **Describe the outcome, not the code.** "Build a form that captures an email and adds it to a Google Sheet" beats "write a JavaScript function that does X."
2. **Start with a working scaffold.** Get something running first, then iterate.
3. **One change at a time.** Do not ask AI to do five things in one prompt — each prompt should have one job.
4. **Verify at each step.** Run the code before adding the next feature.
5. **Use templates and starters.** Do not build from scratch what exists as a template.
6. **Ship when it works, not when it is clean.** Refactor after validation.

---

## Tool selection by task

### Replit
- Best for: backend scripts, APIs, automation tools, quick prototypes
- Strengths: built-in hosting, packages, database, Replit AI agent for generation
- Use for: anything that needs a server, a cron job, or API endpoints
- Deploy: Replit deployments for always-on, or keep on free tier for dev/testing

### Cursor / Claude Code
- Best for: code editing, debugging, refactoring within an existing project
- Use when you have a codebase and need to modify it

### Bolt.new / Lovable / v0
- Best for: full-stack web apps with UI, starting from zero
- Strengths: generates frontend + backend together from a prompt
- Use for: landing pages with logic, simple web tools, dashboards

### Make.com / n8n
- Best for: connecting existing tools, automating workflows without code
- Use instead of writing custom code when the integration already exists as a native node

### Bubble / Webflow
- Best for: complex web apps (Bubble) or marketing sites (Webflow) without custom code
- Use for: products that need a database and user accounts but no custom backend

### Decision logic
- Needs a database + user accounts + custom UI → Bolt/Lovable or Replit
- Needs to connect two existing tools → Make.com or n8n first
- Needs a landing page → Webflow or Replit
- Needs a backend script or API → Replit
- Needs to modify existing code → Cursor or Claude Code

---

## Prompting for code

### Effective prompt structure
1. **What it does** — describe the outcome in plain English
2. **Inputs and outputs** — what goes in, what comes out
3. **Tech context** — language, framework, existing code it connects to
4. **Constraints** — what it must not do, edge cases to handle
5. **Done criteria** — what does working look like?

### Example prompt (good)
"Build a webhook endpoint in Node.js that receives a POST request from a Typeform submission, extracts the email and name fields, and adds them as a new row in a Google Sheet using the Sheets API. The Google Sheet ID is stored as an environment variable. Return 200 on success, 400 if required fields are missing."

### Example prompt (bad)
"Build a webhook to connect Typeform to Google Sheets."

The difference: specific inputs/outputs, tech context, error handling, done criteria.

---

## MVP scoping

The biggest vibe coding mistake is scope creep before version 1 works.

### MVP definition exercise
Answer these three questions before writing a line:
1. What is the one thing this does? (If you say two things, cut one.)
2. Who is the first person who will use it?
3. What does that person need to do, and what does the system need to give back?

Everything else is v2.

### Feature prioritisation
- Must have (MVP cannot work without it) vs Nice to have (adds value but not blocking)
- If you are unsure: leave it out. You can always add it after validation.

---

## Common build patterns

### Form → webhook → CRM/Sheet
Form tool → webhook → automation script or workflow tool → spreadsheet or CRM. Build with a no-code automation tool first; only write custom code if the automation tool cannot handle the logic.

### API wrapper tool
Cloud backend platform (e.g. Replit): create an Express endpoint that wraps a third-party API with your business logic, adds auth, and returns a clean response. Deploy and use as your own API.

### Scheduled job
Cron trigger (backend platform or automation tool) → run script → write results to storage → send notification. Set and forget.

### Simple web tool
Full-stack web app builder (e.g. Bolt.new, Lovable): describe the tool in one prompt, get a working UI + logic, deploy. Works for calculators, generators, form-based tools.

### Chrome extension
AI-assisted code editor or backend platform: manifest.json + content script + background script. Describe what the extension should do on a page — AI generates the scaffold in minutes.

---

## Debugging with AI

When something breaks:
1. Copy the full error message — do not summarise it
2. Include the relevant code block (not the whole file if it is long)
3. Describe what you expected vs what happened
4. State what you already tried

Prompt: "Getting this error: [paste error]. Here is the relevant code: [paste code]. It should [expected behaviour]. Already tried [what you tried]."

---

## Output format

**For a new build:**
- Tool recommendation with rationale
- MVP scope (what is in v1, what is explicitly out)
- Step-by-step build plan with prompts to use at each step
- Done criteria for each step

**For a prompt improvement:**
- Revised prompt, ready to use
- Explanation of what was changed and why

**For a debug request:**
- Root cause diagnosis
- Fix with exact code change

**Rules:**
- Always recommend the lowest-complexity tool that can do the job
- Never design v2 before v1 is working and validated
- State which environment to build in and why

For a build bigger than an MVP, write a short product spec first (what it does, who it is for, what done looks like), then apply the MVP scoping above to cut it to v1.
