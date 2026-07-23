# /marketing-hacks, AI marketing hacks distilled from 2025-2026 practitioner content

The 2025-2026 wave of marketing hacks is AI-stack-heavy. These tactics use Claude Code, Claude Agents, Open Claw (or similar agentic layers), Manus, vibe-code tools, and AI avatars to replace or compound marketing headcount. The pattern across multiple operators is consistent: the stack replaces 60-95% of repeatable knowledge work, and the remaining 10-20% is human taste on top.

Source attribution below uses `?t=<seconds>` URLs so each claim is traceable to the original minute in the source video.

---

## Named frameworks

### Search Everywhere Optimization (SXO)

**What it is.** Ranking #1 on Google no longer guarantees visibility. The convergent playbook from AI-marketing practitioners is to show up everywhere your buyer looks: Google + ChatGPT + Perplexity + Gemini + Claude + Reddit + YouTube + LinkedIn + TikTok + Amazon + App Store + podcast directories. Each LLM cites different sources, so a single-channel strategy leaves citations on the table.

**How to apply.** List your priority topics. For each, audit presence on the top 5 channels that matter for that topic (usually Reddit + YouTube + Wikipedia + LinkedIn + a niche community). Fill gaps systematically. ChatGPT most cites Reddit, YouTube, Wikipedia. Gemini leans on YouTube. Claude leans on Yelp for local. Perplexity leans on YouTube.

**Why it wins.** LLMs build citation consensus from multiple sources. Being present in 5+ relevant places locks in the citation, not a single #1 ranking.

[source: https://youtu.be/SgK9lgxWPzs?t=625]

### Six-level progression of Claude use (learning path)

**What it is.** A staged progression for non-technical operators adopting the agentic AI stack:
1. Claude chat (basic prompting)
2. Claude Co-work (built on Claude Code, guided)
3. Claude Code (CLI, sub-agents, MCPs)
4. Claude Code with MCP integrations (Ahrefs, GA4, HubSpot, Gong, Zapier)
5. Open Claw (autonomous local execution on a dedicated Mac Mini)
6. Multi-agent squads with shared memory

**How to apply.** Start with Claude chat to build prompting instinct. Move to Co-work or Cursor IDE for structured workflows. Add MCPs one at a time when they map to a real weekly workflow. Graduate to Open Claw only after you can describe a repeatable workflow you'd delegate to a junior.

**Why it wins.** Skipping levels produces chaos: running too many MCPs slows the system, and Open Claw without discipline becomes a security risk.

[source: https://youtu.be/AzCrjjcW82c?t=1220]

### A-player vs C-player agent evaluation

**What it is.** A mental model for judging AI agents by analogy to employees. An A-player takes one prompt and runs with it end-to-end. A C-player needs heavy hand-holding, iterative prompts, and constant correction. Default to tools that act like A-players. Downgrade anything that feels like a C-player.

**How to apply.** Give a candidate agent a single meaty brief (e.g. "produce a phased content strategy versus competitor X"). If you have to iterate more than twice to get a usable draft, it's a C-player for that task. Use it for narrower jobs, or swap.

**Why it wins.** Cuts evaluation time. If you're babysitting, you're not delegating.

[source: https://youtu.be/Th4b2cjA38A?t=58]

### 5-phase AI marketing strategy build

**What it is.** A sequential model for designing a marketing strategy in the AI era. Don't skip research just because agents tempt you to jump to execution.
1. Research (audience, hangouts, jobs-to-be-done)
2. Competitive and own-channel analysis
3. Channel selection (pick one, not all)
4. Content cadence (calendar and rhythm)
5. Test and experiment (culture and measurement)

**How to apply.** Run sequentially. Phase 2 is where Manus shines: autonomous competitor website deep-dives in 30 minutes. Phase 4 uses Asana/Airtable + Metricool (or your own stack) for cadence. Phase 5 accepts the 1-in-8 rule: one in eight experiments works, so volume matters.

[source: https://youtu.be/cjWGvYbGMT8?t=20]

### Revenue agent squad architecture

**What it is.** Multiple specialized AI agents working as a team rather than one monolithic agent. Roles cover: deal sourcer (scans CRM + calls for warm opportunities), content repurposer (long-form to multi-channel), SEO researcher (keyword + competitive), programmatic page builder, AB test orchestrator, standup accountability bot. Each has its own context window and scope. A shared "brain" coordinates to avoid duplicate work.

**How to apply.** Set up a CLAUDE.md file with company goals (1, 2, 3-year horizons), ICP, and brand voice. Spawn each sub-agent with a narrow job description and access to the right MCPs. Schedule cron runs for the recurring ones (deal of the day, SEO Slack bot, daily standup). Keep a mission-control dashboard so you don't lose track of what each agent is doing.

**Why it wins.** One sub-agent covers ~2-3 minutes to set up. Three task-specific sub-agents can replace 80-90% of manual SEO grunt work. Named combined stack: reported 60:1 ROI replacing 9 agency roles.

[source: https://youtu.be/UWHcOQCw4NU?t=585]

### Where to use humans vs AI agents in the sales funnel

**What it is.** Allocation framework: humans for ambiguity and high-value accounts; AI agents for repeatable templated outcomes.
- Top of funnel (varied inbound questions): humans win (click-to-call to a real rep).
- No-show recovery and churn re-engagement: AI voice agents win (consent exists).
- Outbound to small accounts at scale: AI agents.
- Outbound to high-value key accounts: humans (customization wins).
- Discovery and demo calls: humans (qualification).

**How to apply.** Map your funnel stage by stage. At each stage ask: high ambiguity or repeatable template? Ambiguity = humans. Template = AI.

**Why it wins.** Fully-automated sales funnels fail on enterprise (6-figure deals, 6+ month cycles). Fully-manual funnels are too slow for high-velocity transactional. The blend is the answer.

[source: https://youtu.be/aCbYQe9FR4A?t=435]

### Three-step YouTube SEO strategy

**What it is.** Three-pillar methodology for building compounding YouTube search traffic rather than chasing one-off virality.
1. Search-first topic selection (target keywords with monthly search volume on both YouTube and Google)
2. Ranking checklist (title, description, timestamps, title-thumbnail teamwork, saying the keyword on camera)
3. AI search optimization (find AI-cited topics for your niche, get cited across AI Overviews)

**Why it wins.** YouTube is the most-cited source inside AI Overviews for many niches. A channel can get a few thousand week-one views but millions over time from search. Teacher's Tech: 16M views/month with 456K from Google search alone across 507 videos.

[source: https://youtu.be/lgUrHqaPrhU?t=30]

---

## Playbooks

### Generate 21 longtail blog posts via Manus in 30 minutes (2x mention)

**Goal.** Produce 21 on-brand, high-intent blog posts from a single prompt session.
**Time.** 30 minutes of agent time, plus human edit pass.
**Success metric.** 21 posts shipped versus a multi-week traditional timeline.

Steps.
1. Point Manus at your blog URL. Tell it to learn your writer guidelines (length, tone, links, stats, table usage).
2. Provide 3-5 seed longtail high-intent keywords from your business. Ask for 50-100 similar phrases.
3. Approve the keyword list.
4. Have Manus draft 21 posts following the learned style.
5. Human edit pass before shipping.

Caveat. Output is 95-99% there, not 100%. Editorial review is still required. Aim for ~33% AI-detector probability or lower; fact-check, link-check, and voice-check before publish.

[source: https://youtu.be/PmKPtCUZlCE?t=140, https://youtu.be/ZjHIslqkbLI?t=20]

### Manus blog factory and 156 pages in 20 minutes

**Goal.** Produce 156 programmatic SEO pages (listicle + service templates) in parallel.
**Time.** 20 minutes for Manus to parallel-generate. Pages average 8-10K words.
**Success metric.** Bottleneck shifts from drafting to editorial throughput.

Steps.
1. Identify a base keyword (e.g. "personalized LinkedIn ads").
2. Provide two templates: listicle and service page.
3. Provide writer guidelines and brand voice document.
4. Provide audience definition.
5. Run with parallel processing flag.
6. Route output through editorial review (aim for ~33% AI probability).

[source: https://youtu.be/-sFYOnv_DAs?t=2700]

### Build a Claude Code deal sourcer from network data

**Goal.** Continuously surface ranked outbound opportunities across your network with personalized angles and draft messages.
**Time.** Setup ~2 hours. Ongoing automated.
**Success metric.** Named case: two trillion-dollar-company meetings booked; $10M+ in surfaced pipeline from stale CRM.

Steps.
1. Export LinkedIn connections via data privacy download (connections.csv).
2. Connect Gmail and Google Calendar OAuth to Claude Code.
3. Set up a real-time news-scanning API (Exa or similar) for ICP-fit signals: funding rounds, hires, leadership changes.
4. Author CLAUDE.md with company goals (1, 2, 3-year), ICP, and individual goals.
5. Optional: pipe in CRM (HubSpot MCP), Gong call transcripts, Granola notes.
6. Ask natural-language queries: "top 10 companies I should target based on my LinkedIn, calendar, goals." Agent returns network score, meeting count, estimated deal size, suggested angle.
7. Daily cron: surface "deal of the day" with full context. One-line approval to send drafted outreach.

**Why it wins.** Agent has context the human forgot. Even a generic check-in message works because the relationship existed. Named outcome: one unedited generic message landed a next-day call with a multi-trillion dollar company.

[source: https://youtu.be/M0cT-baxOtU?t=180]

### AI avatar daily content stack (HeyGen + ElevenLabs + Opus + Gemini)

**Goal.** Publish daily avatar videos with b-roll using a chained tool stack.
**Time.** 30 minutes per video once stack is in place.
**Success metric.** Named case: 100K Instagram followers in one week, 1M email list from daily-cadence AI avatar content.

Steps.
1. Use Gemini to extract key points from a long-form video and generate a 60-second short script.
2. Drop script into HeyGen with your avatar. HeyGen pulls voice from ElevenLabs via API.
3. Send raw video to Opus for AI b-roll or stock b-roll.
4. Publish. Pair with ManyChat to capture emails from Instagram comments.

Caveat. Authenticity backlash is possible as audiences detect AI avatars. Platforms may add AI verification. Mixing avatar content with some real-face content de-risks this.

[source: https://youtu.be/akThARvH6gY?t=455]

### Cut AI agent costs by 84%

**Goal.** Reduce monthly AI token spend by ~84% without losing capability (named case: $5,000/mo to $800/mo).
**Time.** Hours of audit; ongoing weekly cron.
**Success metric.** Cron reliability up from 50% to 85%.

Steps.
1. Pay for Claude Max ($200/mo) and ChatGPT Pro ($200/mo) so you can use OAuth instead of API tokens. Expected saving: $1,000-1,700/mo.
2. Plug Open Claw into ChatGPT with OAuth so you stop burning API tokens.
3. Switch cron jobs from Opus to Sonnet. Current Sonnet matches last-gen Opus quality. Expected saving: cron drops from $2.50/run to $0.40/run, ~$630/mo.
4. Run a weekly cron-audit job that kills dead jobs and cuts compaction frequency in half.
5. Move browser automation off expensive API endpoints.

[source: https://youtu.be/PvVrRIYko4w?t=0]

### Open Claw setup for non-coders (secure local agent in a weekend)

**Goal.** Get Open Claw running locally with security guardrails and business context for revenue use.
**Time.** ~10 hours across a weekend.
**Success metric.** Named case: 27:1 ROI ($1K infrastructure replacing $27K/mo of work).

Steps.
1. Buy a Mac Mini (~$600). Local hardware, not VPS, because VPS security risks compound fast.
2. Set up a dedicated Apple ID and Gmail just for the Mac Mini. Isolated identity.
3. Create a dedicated 1Password vault. Only share that vault with Open Claw. Limited credential scope.
4. Install Open Claw via CLI. Connect to Telegram as the chat interface.
5. Set up Telegram topics (SEO, social, product, personal) for parallel work streams.
6. Author a soul.md file (the agent's personality and decision priorities).
7. Use Claude Code on desktop to plan complex prompts. Telegram loses context fast; desktop planning plus Telegram execution combines the strengths of both.

Caveat. Only let it run autonomously after you've tested the credential scope and guardrails.

[source: https://youtu.be/OdZj4NY2ibU?t=0]

### Three sub-agents for SEO acceleration

**Goal.** Replace 80-90% of manual SEO grunt work with three task-specific sub-agents.
**Time.** 2-3 minutes per sub-agent to spin up.
**Success metric.** 10x output with the same headcount.

Steps.
1. Content repurposer. Feeds in long-form (podcast, YouTube, articles). Outputs 20 short-form clips, 10 social posts, 5 email ideas, virality scores 1-100. From one 80-min podcast: 35+ pieces of content.
2. SEO keyword researcher. Hooks into Ahrefs MCP + GSC + GA4 + HubSpot. Finds trending low-volume keywords with high future potential, B2B transactional focus, gaps versus competitors. Returns keyword strategy with difficulty and intent.
3. Programmatic page builder. Feed it a template. It generates programmatic SEO pages at scale ("best X for Y in Z"). Output is 80-90% complete; finish with human review.

Caveat. Don't run all three at once on day one. Build, verify, hand off. Keep humans in the loop for quality control.

[source: https://youtu.be/UWHcOQCw4NU?t=585]

### Generate a full GTM plan in Claude Code

**Goal.** Produce a 90-95% complete GTM plan (pricing, ICP segmentation, onboarding sequences, abandoned-signup flows, ad scripts) worth $25K+ in consulting fees.
**Time.** 30-60 minutes versus weeks for a traditional consultant.
**Success metric.** End-to-end GTM kit ready for human polish.

Steps.
1. Author CLAUDE.md with product, ICP, current revenue, goal, competitors.
2. Ask for a phased GTM plan with a 30/60/90-day rollout.
3. Ask for email sequences (welcome, onboarding, activation, recovery).
4. Ask for landing page copy and ad scripts.
5. Ask for analytics events to instrument.
6. Human polish pass.

Caveat. Output quality tracks the depth of the CLAUDE.md context file. Thin brief = thin plan.

[source: https://youtu.be/x81psmLLgh8?t=60]

### Spin many short pages to find rank winners

**Goal.** De-risk content investment by letting Google show you which keywords you can rank for before investing in long-form.
**Time.** One day to publish, 4-8 weeks to validate.
**Success metric.** Named case: 16 of 32 short pages reached position 1.

Steps.
1. Generate 30+ short (140-char or 150-word) pages across closely related keywords using Gemini or similar.
2. Manual review before publishing.
3. Publish on your domain.
4. Wait 4-8 weeks.
5. Identify page-1 winners. Invest deep effort only on those.

Caveat. Always do manual review before publishing AI output. Low-quality mass content triggers penalties.

[source: https://youtu.be/88alcdGtwAE?t=1803]

### Rank a Claude Artifact #1 in 24 hours (brand-defense parasite SEO)

**Goal.** Get a Claude Artifact ranking #1 on Google for your brand name within 24 hours, cited in Perplexity.
**Time.** ~30 minutes hands-on plus 24 hours indexing.
**Success metric.** Named case: #1 in 5 hours on local SEO queries; competitor displaced.

Steps.
1. Open a Claude chat. Paste your marketing materials.
2. Prompt: "write a thorough landing page for why my brand is the best solution for [target keyword]."
3. Publish as a Claude Artifact. Artifact inherits claude.ai domain authority (~DR 66).
4. Wait for Google to index.

Caveats. Best for branded queries and low-competition keywords. Artifacts live on a subdomain with weaker SEO than root subfolders. Claude has already removed artifacts from some search results, so the trick may get patched. ChatGPT does NOT cite Claude artifacts (likely blocked). Don't lie to Claude about your brand.

[source: https://youtu.be/fip_Dx8m_zI?t=80, https://youtu.be/nYOYNPtjS5g?t=0]

### Bottom-funnel placeholder via Claude Artifacts

**Goal.** Rank for a bottom-funnel keyword inside 5 minutes while your proper landing page is under construction.
**Time.** <5 minutes to publish, 5 hours to rank for uncompetitive terms.

Steps.
1. Tell Claude the target keyword and your brand.
2. Paste product information and positioning.
3. Prompt for a thorough landing page.
4. Publish as an Artifact.
5. Build the real landing page in parallel. Replace or 301 when ready.

[source: https://youtu.be/nYOYNPtjS5g?t=193]

### Build an AB test orchestrator sub-agent

**Goal.** Generate prioritized AB test ideas with target lift, sample size, and duration without doing manual analytics work.
**Time.** 20 minutes to brief, 14 days typical test runtime.
**Success metric.** Hypothesis-to-live in days versus weeks.

Steps.
1. Spin up a CRO sub-agent with access to GA4 and GSC MCPs.
2. Brief it with the page to test and the revenue goal.
3. Agent scans for underperforming elements, generates hypotheses with ICE (Impact/Confidence/Ease) scoring.
4. Human reviews priority list. Approves top 3.
5. Agent outputs sample size and duration calculations. Engineer deploys.

Caveat. Keep human in the loop before deploy. Agent's prioritization is opinion, not gospel.

[source: https://youtu.be/RviV6igjqDA?t=94]

### Track LLM referral traffic with Looker Studio

**Goal.** Measure clicks and conversions coming from each LLM, by landing page, in one dashboard.
**Time.** 20 minutes. Or $20 on Fiverr.
**Success metric.** Clear attribution of ChatGPT, Perplexity, Gemini, Claude to landing pages and conversions.

Steps.
1. Pull GA4 referral source data.
2. Build a Looker Studio dashboard combining ChatGPT, Perplexity, Gemini, Claude referral sources.
3. Tie to GA4 goals (signups, demos, conversions).
4. Add monthly traffic graphs, top landing pages, conversion attribution.

Caveat. GA4 stamps source=chatgpt on only 10-15% of traffic. Use referral source for the fuller picture.

[source: https://youtu.be/ZXR1HvUU1kI?t=905]

### Create a content repurposing sub-agent (live build)

**Goal.** Turn any long-form input into multi-channel-ready content.
**Time.** 10-15 minutes per video once the agent exists.
**Success metric.** 4+ hooks per scored concept, ready-to-post drafts for 4+ channels per source video.

Steps.
1. Brief sub-agent: input = long-form podcast or YouTube video URL, output = 20 short-form clip ideas with virality scores, 4 X threads, 4 LinkedIn posts, short-form captions, newsletter post.
2. Agent scores each concept 1-100.
3. Human picks top 3 per channel. Publishes.

Caveat. First runs may pick the wrong video or misfire on concept. Refine the prompt iteratively.

[source: https://youtu.be/RviV6igjqDA?t=435]

### Carrot LinkedIn ABM ad in under an hour

**Goal.** Get LinkedIn ABM ads live when the creative team is backed up.
**Time.** <1 hour versus 2-week wait.

Steps.
1. Pick 20-100 ICP accounts.
2. Prompt Claude Code to generate personalized ad copy and landing page variants per account.
3. Export and push into LinkedIn Campaign Manager.
4. Refine weekly based on performance data.

Named outcome. 800 leads, 100 enterprise-qualified, 200K views from a single LinkedIn organic post announcing a Carrot feature LinkedIn didn't have.

[source: https://youtu.be/-sFYOnv_DAs?t=3070]

### Competitor content strategy reverse-engineering with Manus

**Goal.** Get a phased content strategy with gaps, keyword opportunities, and prioritized actions versus a high-traffic competitor.
**Time.** 30-60 minutes versus days or weeks manually.
**Success metric.** 90-day phased content strategy plus prioritized opportunity list.

Steps.
1. Provide Manus with competitor URL and your own URL.
2. Ask for content audit, gap analysis, and phased roadmap.
3. Review output (~7/10 quality first iteration).
4. Human edit pass.

[source: https://youtu.be/Th4b2cjA38A?t=92]

### Free outreach manager via VS Code + Roo Code

**Goal.** Run influencer or B2B outreach using a free local stack without Manus context-window limits.
**Time.** Setup ~1 hour.
**Success metric.** Reported: 7 meetings booked in 3 days.

Steps.
1. Install VS Code.
2. Install Roo Code extension. Bring your own Claude or Gemini API keys.
3. Brief the agent on ICP, angle, and target list.
4. Agent drafts, you review and send.

Caveat. Free stack needs more configuration and monitoring than Manus.

[source: https://youtu.be/TU32CVI7Mj8?t=145]

### Daily standup accountability bot in Lindy

**Goal.** Push the team toward high-impact prioritization without a manager in every standup.
**Time.** 1 day to build. Ongoing automation.
**Success metric.** Noticeable performance lift within a week.

Steps.
1. Create a Lindy agent scheduled daily.
2. Collect team's top priorities for the day via Slack.
3. Agent grades the list against OKRs.
4. Agent flags late submissions publicly.
5. Agent summarizes for the manager weekly.

Caveat. Public coaching only works if it fits the team culture.

[source: https://youtu.be/ifuOFXaeIp4?t=525]

### Synthesize meeting transcripts into a slide deck via NotebookLM

**Goal.** Turn hours of meeting transcripts into reusable strategic deliverables.
**Time.** <1 hour end to end.
**Success metric.** Deck + podcast + infographic from 8 hours of transcripts.

Steps.
1. Dump meeting transcripts (Granola, Gong, Fireflies) into NotebookLM.
2. Ask for an audio podcast summary.
3. Ask for a slide deck of strategic takeaways.
4. Ask for an infographic.
5. Review before sharing widely.

Caveat. Honest feedback in transcripts means brutal feedback in outputs. Read before sending to the board.

[source: https://youtu.be/SgK9lgxWPzs?t=120]

### Vibe code free SEO tools with Replit (2x mention on Replit)

**Goal.** Ship free utility tools (calculators, generators) that rank for high-intent queries and convert traffic to signups.
**Time.** 1-2 weeks to launch.

Steps.
1. Identify a calculation or utility your ICP searches for.
2. Vibe code a simple version with Replit, Bolt.new, Lovable, or Cursor.
3. Publish on your domain (not a subdomain).
4. Add an email capture as the core conversion.
5. Promote via niche communities (Reddit, Indie Hackers, LinkedIn).

Caveat. Vibe code is great for prototype; production polish still needs an engineer.

[source: https://youtu.be/Ymh3zlIdL5o?t=1490, https://youtu.be/2zetGpqz2yE?t=830]

### UGC ad creative scaler (Open Claw + Gemini)

**Goal.** Generate UGC ad concepts at scale by having an agent research the brand and ideate.
**Time.** 30-60 minutes per concept batch versus weeks manually.

Steps.
1. Open Claw scans prospect's Facebook Ads Library, website, competitor ads.
2. Gemini generates mockups for each concept.
3. Agent returns concept, script, visual mockup, expected performance angle.
4. Human picks top 3 for production.

[source: https://youtu.be/BFiylHLypLE?t=185]

### Industry/competitor stock analysis via Manus

**Goal.** Understand where your industry's biggest players are heading financially and strategically.
**Time.** 30 minutes versus days of analyst work.

Steps.
1. Name the target companies.
2. Manus pulls SEC filings, earnings calls, news feeds.
3. Returns 5-year performance benchmark and 5-10 year strategic outlook.
4. Verify financials against source SEC files Manus cites.

[source: https://youtu.be/U6_cg9bVz5U?t=85]

### Audit your LinkedIn content with Cursor + ChatGPT

**Goal.** Identify the format/topic combinations that consistently outperform so you can do more of them.
**Time.** ~1 hour.
**Success metric.** Average post engagement lifts as you bias toward proven winners.

Steps.
1. Export LinkedIn content and analytics (impressions, engagement, comments).
2. Feed into Cursor or ChatGPT.
3. Ask: "cluster my top 20% of posts by format, hook, topic. What repeats?"
4. Double down on the winning clusters. Reserve 20-30% of posts for experimentation.

[source: https://youtu.be/1F4LfbPJU_g?t=295]

### Hire a Cursor/Claude coach via Upwork

**Goal.** Skip the learning curve for Cursor + Claude Code + MCPs.
**Time.** 3-4 hours total across 1-2 weeks.
**Success metric.** After 3-4 Zoom sessions you can spin up new sub-agents unaided.

Steps.
1. Post an Upwork job for a Cursor/Claude coach at ~$50/hour.
2. Send the candidate a reference video as briefing material.
3. Book 3-4 Zoom sessions covering setup, first sub-agent, MCP integration, advanced workflows.

[source: https://youtu.be/Ymh3zlIdL5o?t=755]

### Voice AI agent use cases (inbound + churn + no-show)

**Goal.** Recover revenue and farm insight from existing/past customers without burning real reps.
**Time.** Setup 1-2 weeks. Ongoing automated.
**Caveat.** Consent-based flows only. Cold calling is illegal in EU/US without prior opt-in. Growth hack: drive paid ads to an opt-in resource (checklist), enrich email with mobile, then call with consent.

Three use cases.
1. Trial signup with no app or CRM activity in X days. AI calls: "Hi Sam, this is Frank from [company]. I saw you signed up a week ago, how was the experience?" Insight on why not buying + offer of onboarding demo.
2. Churned accounts (cancelled X months ago). AI calls: "I saw you were a customer a year ago. Is [problem] still relevant to you?" Win-back conversations.
3. Demo no-shows. AI calls to reschedule instead of a rep chasing manually.

Voice ideally uses a cloned founder voice for authenticity.

[source: https://youtu.be/aCbYQe9FR4A?t=494]

### Programmatic SEO blog generation with Manus

**Goal.** Produce 50+ keyword-targeted blog posts end-to-end.
**Time.** 1 day for 50 posts versus weeks manually.
**Success metric.** 10+ posts published per batch matching your writer guidelines and >1500 words.

Steps.
1. Seed with 3-5 example high-intent keywords.
2. Ask for keyword research + intent classification.
3. Writer guideline analysis from your existing blog.
4. Template generation.
5. Full drafts in batches of 10-20.
6. Human editing for facts, links, case studies.
7. Publish.

Caveat. Aim for ~33% AI detector probability or lower. Humans must edit before publish.

[source: https://youtu.be/Th4b2cjA38A?t=337]

---

## Tactics

### Search Everywhere tactical moves
- Listicle guest posts to manipulate AI citation. Place yourself #1 in "best [service] in [city]" listicles across 5 high-quality guest post sites (DR 40+, 2K+ monthly organic). Five sources = AI citation lock. [source: https://youtu.be/SDYzINt4ezo?t=4488]
- Track LLM citation sources per LLM and replicate placement there. ChatGPT → Wikipedia. Gemini → YouTube. Claude → Yelp (local). Perplexity → YouTube. [source: https://youtu.be/f9o_ch6Iiaw?t=3160]
- Listicles for AI visibility quick wins. Build listicle pages on your own site. Named case: Mark Vision saw ChatGPT and Gemini mentions inside 6 weeks. [source: https://youtu.be/yqN3ZO4pvoU?t=210]
- Own a category by language association. Repeatedly pair your brand with a defined category term across podcasts, blog posts, press, and social over years. Named case: SparkToro and "audience research" linked for 6-7 years. [source: https://youtu.be/5JQvdLYvGZI?t=480]
- Monitor AI citation sources with a tracker (Profound, Amplitude free LLM tracker). [source: https://youtu.be/BQRiw7VtabU?t=602]

### Claude Code tactical moves
- Run sub-agents in parallel for bulk SEO research. Named case: 200-ATS API documentation extraction overnight in ~10 hours. Replaces what used to require offshore mechanical Turk. [source: https://youtu.be/8wImHWoQ7C4?t=2200]
- Use natural language to query your network. "Top 10 companies I should target based on my LinkedIn, calendar, goals." Agent returns network score, meeting count, estimated deal size, suggested angle. [source: https://youtu.be/M0cT-baxOtU?t=120]
- Use Claude Code's planning mode for complex tasks. [source: https://youtu.be/x81psmLLgh8?t=580]
- Claude Code can teach you Claude Code. When stuck, ask it how to use itself. Self-debugging and file-system reorganization work. [source: https://youtu.be/xiDpFVY0CVo?t=895]
- Use Claude Code for personal data too (calendar audits, goals review, daily impact rating).

### Open Claw tactical moves
- Mac Mini army. Multiple Mac Minis, one Open Claw each, scoped per role or per client. People running 12+. [source: https://youtu.be/BQRiw7VtabU?t=1605]
- Cloudflare Mol Worker for self-hosted sandboxed Open Claw. Middleware for multiple agents, one per team (SEO, paid, sales, ops). [source: https://youtu.be/OdZj4NY2ibU?t=1130]
- Use Claude Code on desktop to plan better Open Claw prompts. Telegram loses context fast; plan in desktop, execute via Telegram. [source: https://youtu.be/BFiylHLypLE?t=666]
- Long-form podcast clip finder via Open Claw. Send video URL. Get clips with timestamps, hooks, angle. Cheaper than dedicated tools. [source: https://youtu.be/BFiylHLypLE?t=247]

### Manus tactical moves
- Manus full competitor deep-dive. End-to-end strategy breakdown in one prompt.
- Connect Manus to Ahrefs for backlink work. Ahrefs integration via MCP. [source: https://youtu.be/Th4b2cjA38A?t=275]
- Automate internal linking with autonomous agents (Manus or Genspark). Provide positioning + priority keywords. [source: https://youtu.be/PmKPtCUZlCE?t=308]
- Manus carries context across sessions via link copy. Hits context window limits? Copy the link, start a new session.
- Use Manus high-effort mode for serious tasks. Lower modes are faster but shallow.

### MCP tactical moves
- MCPs unify GA, GSC, HubSpot, Ahrefs into one natural-language interface from inside Cursor or Claude Code.
- Scrape competitor Google Ads via Apify MCP. Returns keyword count, monthly visit estimate, monthly spend estimate, # landing pages. Example output: "Tinuity 42 keywords, 4,300 visits/mo, $1,700 spend, 9 landing pages." [source: https://youtu.be/RviV6igjqDA?t=560]
- SEO opportunity Slack bot. Hook GSC MCP into Claude Code. Daily: position gains/losses, top converters, BOFU gaps, internal link adds. Output to Slack as task assignments. [source: https://youtu.be/_31Sgdnsjfo?t=620]
- ChatGPT as time audit coach via Calendar MCP. Monthly time-allocation audits versus goals. Daily impact rating against strategic goals. [source: https://youtu.be/ifuOFXaeIp4?t=200]
- Use HubSpot MCP for natural-language CRM analytics queries.

### Ad creative tactical moves
- Ad creative with Veo 3 + Nano Banana for $100. Google Veo 3 for video, Nano Banana for character consistency, ElevenLabs for voice. Cost $100 versus $100K+ for traditional production. [source: https://youtu.be/Ymh3zlIdL5o?t=1085]
- AI trend hacker via HeyGen + ElevenLabs APIs. Monitor trend feed, auto-generate avatar video responses via API. [source: https://youtu.be/TU32CVI7Mj8?t=085]
- Carrot LinkedIn ad formula: screenshot your unique feature + novelty hook + engage in first 4 hours. Expect 100-200K views if novelty is real. [source: https://youtu.be/Ymh3zlIdL5o?t=1685]

### SOP and team tactical moves
- AI-powered SOPs as Gemini Gems. Upload SOP docs to a Gem. Hiring rubric Gem auto-evaluates candidate transcripts. Brand-style Gem enforces voice. [source: https://youtu.be/SgK9lgxWPzs?t=435]
- AI fluency hiring filter. Two screening questions: (1) how much do you spend monthly on AI tools? (2) what have you built that moved a KPI? $0/mo = out. [source: https://youtu.be/xiDpFVY0CVo?t=170]
- Multiplier math for internal selling. Non-coder = infinite multiplier. Engineer = 10-20x. Prototype time 30 days → 0.2 days = 150x, halve to be conservative = 75x. [source: https://youtu.be/x81psmLLgh8?t=480]
- Default to mockups over PRDs. Mock the prototype in Vzero, Replit, or Cursor. Discuss off the working artifact. [source: https://youtu.be/8ktEWz0HX3s?t=807]

### Prompt engineering tactical moves
- Soul.md file is the agent's personality. Pins decision priorities, brand voice, risk tolerance.
- AI sycophancy is real. Push back on confident-sounding output. Ask for the opposing view.
- Skill installation via GitHub. Install packaged marketing skills (e.g. Corey Haynes' marketing skills). Invoke with slash commands like /page-cro.
- Super Whisper for stream-of-consciousness briefs. Voice dictation that doesn't save audio to cloud; faster than typing long prompts.

### Vibe code tactical moves
- Vibe code linkable assets. Build calculators, configurators, downloadable templates, research reports in hours with Replit or Claude. People share them with language related to your niche, building backlinks and topical authority. [source: https://youtu.be/8DuIlUdfY_w?t=325]
- Use Mobbin to clone competitor screens. Screenshot library of real product UIs as prompt input.

---

## Tools (AI marketing stack)

| Tool | What for | Cost | Notes |
|---|---|---|---|
| Claude Code | Agent orchestration, sub-agents, marketing automation, deal sourcing, GTM drafting, ABM ad copy | Claude Max $200/mo OR API metered | Core of the 2026 stack. OAuth route beats API tokens for cost. [src](https://youtu.be/RviV6igjqDA?t=0) |
| Claude Artifacts | Parasite SEO publishing, branded landing pages, rapid landing-page demos | Free with Claude account; Pro/Max for more usage | Publishes instantly on claude.ai subdomain. Google indexes; Perplexity cites. ChatGPT does not. [src](https://youtu.be/fip_Dx8m_zI?t=120) |
| Open Claw | Autonomous local agent runtime on dedicated hardware | ~$1K infrastructure (Mac Mini + setup) | 27:1 ROI case. Self-hosted. Requires Mac Mini + 1Password + Telegram setup. [src](https://youtu.be/MaH6_I4NP0k?t=0) |
| Manus AI | Autonomous super-agent: keyword research, content drafting, competitor breakdowns, programmatic SEO, stock analysis | ~$50-600/year tier | Operates as A-player. 21 blog posts in 30 min. 156 pages in 20 min. Loom-driven execution. [src](https://youtu.be/PmKPtCUZlCE?t=140) |
| Cursor IDE | Marketing workbench for non-engineers; host for Claude Code + MCPs | $20-200/mo | 5-10x velocity per CTO verdict. Not optional for engineering teams. [src](https://youtu.be/ifuOFXaeIp4?t=632) |
| Replit | Non-technical MVPs, linkable assets, free SEO tools, rapid prototypes | Freemium | 3-5 minute prototypes. Named 2x in KB. Alternatives: Bolt.new, Windsurf, Cursor. [src](https://youtu.be/2zetGpqz2yE?t=830) |
| Bolt.new | Working app front-end via natural-language prompts | Freemium | 50-70% of a working app before engineering. [src](https://youtu.be/HCqjQxmOAGk?t=1455) |
| HeyGen | AI avatars for face-to-camera content at scale | Paid tiers | Named case: 100K followers in 1 week + 1M email list. [src](https://youtu.be/ifuOFXaeIp4?t=763) |
| ElevenLabs | AI voice cloning for content, avatar video, chatbots, voice AI agents | Paid tiers | Used with HeyGen for avatar pipelines. Cloned founder voice for voice AI. [src](https://youtu.be/ifuOFXaeIp4?t=763) |
| Opus | Short-form video cutting from long-form | Paid | Podcast → 10 clips. Use Open Claw as a cheaper alternative. |
| Veo 3 | AI video generation for ads | Paid | $100 ads stack with Nano Banana + ElevenLabs. [src](https://youtu.be/Ymh3zlIdL5o?t=1085) |
| Nano Banana | Character consistency across generated video shots | Paid | Pairs with Veo 3. [src](https://youtu.be/Ymh3zlIdL5o?t=1085) |
| Granola | AI meeting note-taker that feeds downstream content workflows | Freemium | Transcripts feed NotebookLM + content repurposer. [src](https://youtu.be/_31Sgdnsjfo?t=500) |
| Lindy.ai | Agentic workflows: standup bot, recruiter sourcing, coaching | Freemium with paid tiers | Good for recurring scheduled agents. Doesn't compound like Claude Code. [src](https://youtu.be/ifuOFXaeIp4?t=465) |
| GenSpark.ai | Autonomous phone calls, trip planning, content repurposing | ~$17/month | Operator agent; execute miscellaneous logistics. [src](https://youtu.be/8ktEWz0HX3s?t=1390) |
| Gemini (Pro, Flow, Gems) | Pre-configured AI assistants, SOPs, deep research, slides | Part of Google Workspace AI tier | Gems for SOPs + brand voice. Flow for cross-tool wiring. Deep research for strategy input. |
| NotebookLM | Document synthesis, audio podcast summaries, infographics, slides | Free | 8 hours of transcripts to deliverables in <1 hour. [src](https://youtu.be/SgK9lgxWPzs?t=120) |
| Roo Code | Free agentic runtime inside VS Code; bring-your-own-API | Free (you pay LLM costs) | 7 meetings in 3 days case. No Manus context limits. [src](https://youtu.be/TU32CVI7Mj8?t=145) |
| Profound (tryprofound.com) | Generative engine optimization tracking (brand mentions across ChatGPT, Gemini) | Paid SaaS | Tracks how brands appear across LLMs. [src](https://youtu.be/eHvXtwGTxLQ?t=1170) |
| Amplitude (free LLM tracker) | Track AEO results and LLM rankings | Free tier | Feeds your citation-source tracking. [src](https://youtu.be/BQRiw7VtabU?t=602) |
| Looker Studio | LLM referral traffic dashboarding tied to GA4 | Free | 20 min setup; $20 Fiverr alternative. [src](https://youtu.be/ZXR1HvUU1kI?t=900) |
| Pinecone | Vector database for content agents semantically search | Free tier + paid | Brand corpus and knowledge base for agents. [src](https://youtu.be/8wImHWoQ7C4?t=2280) |
| Super Whisper | Voice dictation for briefing agents | Paid app | Doesn't save audio to cloud. Faster than typing long prompts. [src](https://youtu.be/RviV6igjqDA?t=146) |
| Mac Mini | Local hardware for Open Claw | ~$600 per unit | Prefer over VPS for security. People running 12+. [src](https://youtu.be/BQRiw7VtabU?t=1605) |
| Cloudflare Mol Worker | Middleware for multiple sandboxed Open Claw instances | Developer platform | Self-host agents per team. [src](https://youtu.be/OdZj4NY2ibU?t=1130) |
| Exa API (or similar news API) | Real-time ICP news scanning (funding, hires, CMO changes) | Paid API | Feeds deal sourcer with live triggers. [src](https://youtu.be/M0cT-baxOtU?t=255) |
| Carrot.ai | Account-based marketing: personalized LinkedIn ads with matching personalized landing pages | Paid SaaS | 100 enterprise accounts in minutes vs weeks. [src](https://youtu.be/HCqjQxmOAGk?t=465) |
| Apify MCP | Scrape competitor Google Ads, Meta Ads, LinkedIn Ads from inside Cursor | Paid | Returns keyword count, spend estimate, landing pages. [src](https://youtu.be/RviV6igjqDA?t=560) |
| HubSpot MCP | Natural-language CRM analytics queries | HubSpot plan | Ask Claude Code your CRM questions in plain English. |
| Ahrefs MCP | SEO keyword research, backlink data inside Claude Code | Ahrefs plan | Essential for the SEO keyword research sub-agent. |
| GSC MCP | Position tracking, top queries, opportunity gaps | Free (GSC account) | Powers the SEO opportunity Slack bot. |
| ManyChat | Convert Instagram comments to email list via DM flow | Freemium with paid tiers | Backbone of AI avatar email-capture flywheel. |
| Mobbin | Screenshot library of real product UIs | Paid | Clone competitor screens as prompt input. |
| Grok (xAI) | AI coding for black-hat SEO scripts (PHP/JS hidden redirects, cloaking) | Free or paid | Use-at-own-risk. Included for completeness. [src](https://youtu.be/q-fwxKK50yM?t=600) |

---

## Anti-patterns (AI marketing failures)

### AI marketing without KPIs
Spending a year deploying AI tools without attaching them to specific KPIs (traffic, leads, sales, revenue). AI is the means, not the end. Without a target metric you cannot evaluate whether the work was worth the investment.
Fix. Define the KPI before building. Measure against it weekly.
[source: https://youtu.be/HCqjQxmOAGk?t=796]

### Defaulting to AI agents for B2B marketing
Producing a million blog posts that don't rank. Agentic SDRs generating terrible Gmail leads. Expecting AI agents to replace strategy.
Fix. Build a real B2B strategy: bottom-funnel SEO/AEO, founder brand on LinkedIn/YouTube, demand-capture content. Use AI as execution speed on top of strategy, not as the strategy.
[source: https://youtu.be/lKKO9pwI7wM?t=20]

### AI agents for enterprise sales
AI SDR agents fail on 6-figure deals, 6+ month sales cycles, Fortune 500 targets. Five AI SDR companies died recently. Big agentic SaaS players aren't orchestrating agents the way real salespeople do.
Fix. Reserve AI agents for high-velocity transactional sales on email and LinkedIn. Use voice AI agents only on consent-based inbound flows. Humans handle enterprise.
[source: https://youtu.be/aCbYQe9FR4A?t=215]

### Blocking all AI crawlers before you have brand
Blocking AI crawlers without a strong existing brand makes your site invisible to people who don't already know you. Early-stage brands lose AI discoverability without the brand awareness to compensate.
Fix. Allow AI crawlers until your brand search volume is meaningful. Then reconsider.
[source: https://youtu.be/wWAoKVov6uk?t=685]

### Running too many MCPs at once
Enabling every MCP because they sound powerful slows the IDE and the agent's reasoning loop.
Fix. Curate to MCPs that map to weekly workflows. Typical set: Ahrefs, GA4, HubSpot, Apify, Gong, Zapier.
[source: https://youtu.be/RviV6igjqDA?t=345]

### Engineers not on Cursor (or equivalent)
5-10x velocity loss per CTO verdict. Non-adopters cost the business money in opportunity terms.
Fix. Mandate Cursor (or Claude Code) for all engineers. Treat AI fluency as a hiring requirement.
[source: https://youtu.be/8ktEWz0HX3s?t=755]

### Treating AI tools as a course to complete
Signing up for a Claude Code course and treating completion as the milestone. Courses are theater; the learning happens when you wrestle with your own workflows.
Fix. Pick one workflow you do every week. Sit with Claude Code. Rebuild it. Break things. Learn by doing.
[source: https://youtu.be/x81psmLLgh8?t=580]

### Diversify off paid search before AI dries it up
Paid search is getting more expensive and less effective as buyers move to AI tools that aren't yet ad-monetized. Over-reliance on a single channel is fragile.
Fix. Keep paid search running while it works. Layer in SEO and AEO (AI search) to balance the portfolio. Don't wait until PPC collapses.
[source: https://youtu.be/b358esP7dm8?t=375]

### Asking AI agents too many clarifying questions (C-player usage)
ChatGPT Operator and similar C-player tools stall on basic execution, forcing you to babysit.
Fix. Use A-player tools (Manus, Open Claw, Claude Code) for delegable work. Save C-player tools for narrow tasks you're co-piloting.
[source: https://youtu.be/ifuOFXaeIp4?t=434]

### Building everything because AI lets you
Compounding AI output without creative vision produces mediocre volume. When execution scales infinitely, the bottleneck is creativity and taste.
Fix. Invest in creative input quality: reading, conversations with smart people, frontiers exploration. Ship less but higher-signal.
[source: https://youtu.be/2zetGpqz2yE?t=805]

### Shipping AI content with no review loop
Publishing 95-99% complete AI drafts as-is. AI text has tells (banned words, generic structure, wrong facts, no personality).
Fix. 80-20 rule. AI does 80%, human finishes the 20%. Fact check, link check, voice check, AI-detector probability <33% before publish.
[source: https://youtu.be/U6_cg9bVz5U?t=345]

---

## Examples (real results, named)

- **Open Claw 27:1 ROI.** Eric Siu / Single Grain. $1K infrastructure replaced $27K/month of work. Articles average 65K-100K views versus 6.6K when written manually. [source: https://youtu.be/MaH6_I4NP0k?t=0]
- **Single Grain 60:1 combined ROI.** Claude Code alone replaces 6/9 agency roles ($40-74K/mo) at $500-800/mo cost. Combined with Open Claw replaces 9/9 roles at $800-1,300/mo cost. [source: https://youtu.be/AzCrjjcW82c?t=296]
- **800 LinkedIn leads from one feature post.** Carrot. Single screenshot + novelty hook ("here's a feature LinkedIn doesn't have"). 200K views, 800 leads, 100 enterprise-qualified. [source: https://youtu.be/X9CRC3HJZbY?t=765]
- **100K Instagram followers in 1 week, 1M email list.** Rowan Chung. HeyGen + ElevenLabs + daily AI trend avatar content + ManyChat comment-to-email flow. [source: https://youtu.be/q7PLrreN29Q?t=20]
- **Two trillion-dollar-company meetings booked.** Eric Siu via Open Claw daily deal of the day. Generic check-in message, unedited, to stale CRM contact. Next-day call. [source: https://youtu.be/OdZj4NY2ibU?t=655]
- **$10M+ in pipeline surfaced.** Claude Code deal sourcer scanning HubSpot + call transcripts + network data. [source: https://youtu.be/AzCrjjcW82c?t=549]
- **156 SEO pages in 20 minutes.** Manus parallel-generation. Listicle + service templates, 8-10K words per page. [source: https://youtu.be/-sFYOnv_DAs?t=2700]
- **21 blog posts in 30 minutes.** Manus blog factory. One prompt. Writer guideline learning + keyword research + drafts. [source: https://youtu.be/PmKPtCUZlCE?t=140]
- **AI-written X article 101K views.** Eric Siu via Open Claw + Flash agent. Eric only contributed graphic + title + opening hook. Manual articles hit 6.6K views. [source: https://youtu.be/MaH6_I4NP0k?t=58]
- **7 meetings booked in 3 days.** VS Code + Roo Code free outreach stack. [source: https://youtu.be/TU32CVI7Mj8?t=145]
- **Teal: 1M Google clicks/month.** Resume builder SaaS. 893K ranking keywords. DR ~72-73. 3M-job job board. Heavy AI automation across SERP analysis, internal linking, content review. ChatGPT-resume post hit 20% conversion to free signups. [source: https://youtu.be/8wImHWoQ7C4?t=15]
- **Mark Vision AI search citations in 6 weeks.** Legal tech SaaS. Bottom-of-funnel SEO listicles + competitor keyword targeting. ChatGPT and Gemini brand mentions within 6 weeks; demo requests up. [source: https://youtu.be/yqN3ZO4pvoU?t=0]
- **Claude Artifact #1 in 5 hours (local SEO).** Competitor displaced on a local SERP. Anonymous YouTube commenter + Jesper Nissan. [source: https://youtu.be/nYOYNPtjS5g?t=151]
- **Jason Calacanis editor releases 60% of work.** Podcast editor expected to offload 60% of tasks to Open Claw + Claude Code within 4 weeks. [source: https://youtu.be/AzCrjjcW82c?t=429]
- **Karpathy Auto-Research repo.** Open-source AI experiment runner. ~36,000 experiments per year possible versus typical business running 50. Sample run: 83 experiments, 15 kept (18% success rate). [source: https://youtu.be/zgHoahKoqBg?t=0]
- **Ahrefs AI marketing bot time savings.** ChatGPT project trained on 12 months of blog posts and a year of video scripts. Week of work compressed to 3 days. CMO graded output 60-70%. [source: https://youtu.be/3iNJeArrUu4?t=678]
- **AI agent monthly spend cut 84%.** $5,000/mo to $800/mo via OAuth, Sonnet for cron, weekly audit, browser automation off-API. [source: https://youtu.be/PvVrRIYko4w?t=0]

---

## Key tips (worth pinning)

- **Get to 80% with AI, then human-finish.** Applies to content, strategy reports, programmatic pages, outreach drafts. Budget for the last 20%.
- **Creativity is the new constraint.** When agents scale execution infinitely, the bottleneck is creative vision. Most creative operators will command thousands of agents.
- **Compounding products beat one-off automations.** Claude Code wins over Lindy/Zapier for anything you iterate monthly. Memory, leaderboards, version history compound; one-shot workflows reset each run.
- **Marketers without Claude Code will be left behind.** Agentic output compounds across the team. Leaders not training their teams on it are losing ground.
- **AI sycophancy is real.** Push back on confident-sounding output. Ask for the opposing view before acting.
- **Hire for AI fluency.** Ask how much they spend on AI monthly and what they've built that moved a KPI. $0/mo = out.
- **Pick one Gemini area and use it daily for a week.** Deep research, Flow, Gems, deep learning. Mastery beats breadth.
- **Train team via X/Twitter for AI fluency.** The frontier is on social, not in courses.
- **Acquire taste through conversation.** Taste is the compounding moat when execution is free.
- **YouTube is the most-cited source in AI Overviews.** Long-form video isn't optional in 2026.
- **Don't believe ChatGPT killed Google.** Google still owns the majority of queries. Play both.
- **AEO extends beyond your site.** Third-party listicles, G2/Capterra reviews, Reddit, podcast transcripts, niche industry blogs all feed LLM citation.
- **Bottom-of-funnel pages rank in LLMs too.** Don't write off your money pages because they're "commercial."
- **LLMs.txt file helps where coverage is spotty.** Publish one for docs-heavy products; LLMs parse it as a table of contents.

---

## Sources cited

All URLs carry `?t=<seconds>` timestamps for traceability.

Leveling Up (Eric Siu) sources. https://youtu.be/RviV6igjqDA?t=0 https://youtu.be/OdZj4NY2ibU?t=0 https://youtu.be/MaH6_I4NP0k?t=0 https://youtu.be/AzCrjjcW82c?t=0 https://youtu.be/M0cT-baxOtU?t=180 https://youtu.be/akThARvH6gY?t=455 https://youtu.be/Th4b2cjA38A?t=30 https://youtu.be/U6_cg9bVz5U?t=33 https://youtu.be/ifuOFXaeIp4?t=200 https://youtu.be/UWHcOQCw4NU?t=585 https://youtu.be/PvVrRIYko4w?t=0 https://youtu.be/x81psmLLgh8?t=60 https://youtu.be/SgK9lgxWPzs?t=120 https://youtu.be/-sFYOnv_DAs?t=2200 https://youtu.be/Ymh3zlIdL5o?t=755 https://youtu.be/8ktEWz0HX3s?t=755 https://youtu.be/xiDpFVY0CVo?t=170 https://youtu.be/BFiylHLypLE?t=0 https://youtu.be/BQRiw7VtabU?t=602 https://youtu.be/zgHoahKoqBg?t=0 https://youtu.be/cjWGvYbGMT8?t=20 https://youtu.be/TU32CVI7Mj8?t=20 https://youtu.be/XKqNdX0qNRI?t=60 https://youtu.be/_31Sgdnsjfo?t=500 https://youtu.be/2zetGpqz2yE?t=805 https://youtu.be/ZjHIslqkbLI?t=110 https://youtu.be/q7PLrreN29Q?t=20 https://youtu.be/UT10uggffps?t=315 https://youtu.be/88alcdGtwAE?t=1803 https://youtu.be/HCqjQxmOAGk?t=1455 https://youtu.be/X9CRC3HJZbY?t=765 https://youtu.be/lKKO9pwI7wM?t=20

Sam Dunning sources. https://youtu.be/yqN3ZO4pvoU?t=0 https://youtu.be/aCbYQe9FR4A?t=435 https://youtu.be/FleBW6QOToc?t=372 https://youtu.be/b358esP7dm8?t=375

Ahrefs sources. https://youtu.be/3iNJeArrUu4?t=678 https://youtu.be/_s2h7X-c2jE?t=0 https://youtu.be/lgUrHqaPrhU?t=30

Build in Public sources. https://youtu.be/nYOYNPtjS5g?t=0 https://youtu.be/fip_Dx8m_zI?t=80 https://youtu.be/ZXR1HvUU1kI?t=900 https://youtu.be/SDYzINt4ezo?t=4488 https://youtu.be/f9o_ch6Iiaw?t=3160 https://youtu.be/8wImHWoQ7C4?t=15 https://youtu.be/wWAoKVov6uk?t=685 https://youtu.be/2htSIT0HLjs?t=2966 https://youtu.be/8DuIlUdfY_w?t=325 https://youtu.be/q-fwxKK50yM?t=600 https://youtu.be/5JQvdLYvGZI?t=480

Convergent playbook attribution. Multiple agency operators cited this stack; the patterns (six-level Claude progression, three-sub-agent SEO kit, daily deal sourcer, AI avatar flywheel, 60:1 ROI combined stack) recur across practitioner content from late 2025 and early 2026. Use these as a starting architecture, then adapt to your ICP, budget, and risk tolerance.
