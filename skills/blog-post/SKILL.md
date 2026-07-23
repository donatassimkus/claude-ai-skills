---
name: blog-post
description: "Create an SEO blog post from a primary keyword on a CMS-backed site. Runs end-to-end autonomously by default (no in-process gates): keyword intake → SERP data pull → competitor page scrape → gap analysis → outline → draft → image generation → publish → comprehensive end-of-run self-audit. Auto-fixes known failure modes (zero counts, em-dashes in structured fields, source URL rot, keyword density drift) without prompting the user. Escalates only what genuinely needs human judgement (cannibalization >30% with adjacent post, factual claim that can't be sourced). Opt-in gates via --review-outline / --review-images / --review flags. Loads a per-site pipeline config for shortcodes, author, paths, taxonomy, geography, currency, editorial rules. Enforces forbidden-words ban + zero em-dashes across EVERY authored field (body, title, excerpt, structured-field rows, meta) + keyword-density rules (primary 1-2% for entity articles, never 2x per paragraph; each secondary 1-3x distributed across H2s, never >5x). Supports batch mode with daily schedule."
user-invocable: true
argument-hint: <site> <topic-or-keyword> [--from <skill-or-material>] [--research full|positioning] [--no-gate] [--review-outline] [--length N] [--category X] [--project slug] [--skip-competitor] [--dry-run] [--featured-entities \"ID1,ID2\"]
---

# /blog-post skill

Create an SEO blog post from a primary keyword on a project's CMS-backed site. Generic pipeline — all project-specific detail (site URL, deploy/access method, author, shortcode library, currency, geography, category IDs, banned entity-mention rules) lives in a per-project `blog-pipeline-config.md` file.

Invoke as `/blog-post <site> <topic-or-keyword>` (singular). The first argument is the SITE (slug, domain, or natural-language name); the rest is the topic or primary keyword. The same engine is also called per-keyword by a BATCH RUNNER (an unattended multi-post run over a keyword queue) in batch posture.

**Platform scope (read this before Phases 7-9).** Phases 1-6 (keyword intel, competitor scrape, gap analysis, planner, draft, pre-publish audit) are platform-agnostic and correct on ANY stack. Phases 7-9 are written in the concrete idiom of a **self-hosted WordPress site driven over a command-line interface**, because that is where the publish mechanics (media import, structured fields, meta keys, taxonomy assignment, cache flush) are specific enough to be worth stating exactly. A static-site branch is given further down. On any OTHER CMS (a headless CMS, a hosted blog platform, a different self-hosted CMS, a git-backed site), the RULES in Phases 7-9 all still hold — substitute your platform's equivalent for each mechanism and keep the rule: its media upload API for the media import, its structured/custom fields for the repeater fields, its SEO plugin or native meta fields for the title/description/focus-keyword meta, its taxonomy or tag API for categories and tags, and its own cache invalidation. Where a step names a specific plugin's meta key, that key is an EXAMPLE of the mechanism, never the mechanism itself: writing another plugin's key silently sets a value nothing reads. Confirm your platform's real field names once, record them in the site config, and use those throughout.

**Site config + escalation policy.** The per-SITE facts (URL, access method, author, shortcodes, currency, geography, taxonomy, editorial rules) live in each site's `blog-pipeline-config.md`, whose contract is defined below. When you run more than one site, keep a small registry (a JSON or YAML file listing each site slug and the path to its config) and resolve the `<site>` argument against it. Two policy decisions are NOT hardcoded in this engine and belong in the site config: which sites publish autonomously versus hold for review, and whether the cannibalization/consistency checks (24/31) auto-resolve or escalate to the operator. If the site config is silent on those, default both to ESCALATE — the safe direction. The steps below are the universal engine; site values come THROUGH the config.

## Two postures (same engine, different command)

This skill is the per-post ENGINE (Phases 1-11 below). Two invocation modes wrap it with OPPOSITE postures; the posture is set by HOW the engine was called, never baked into the phases:

- **Singular (the operator invokes `/blog-post <site> <topic>` directly): interactive + publish-now.** A hand-picked topic on a specific site. Resolve the site, write end-to-end to a DRAFT, show a report, let the operator approve / redirect / change, then publish LIVE immediately on approval. More care, because it is the operator's own topic.
- **Batch (the engine is called per-keyword by an unattended multi-post run): autonomous + scheduled.** Publish as a DRAFT, no gate, fully autonomous; the batch runner schedules it later. The batch brief sets this posture explicitly and overrides the singular default. In batch posture, EVERY mid-run escalation is handled exactly as `--autopilot` (the draft-plus-flag rule): record it as draft-plus-flag and carry it to the batch summary, NEVER a blocking interactive question. A post that fails or cannot be verified is left as an UNSCHEDULED draft (never silently shipped, never scheduled). So batch posture equals autopilot posture for ALL gating: no per-post verdict pop-up, no intent-disagreement gate, no component-buffet ask, no meta-variant pick, no missing-tag ask, no ambiguous-back-link ask, no Phase-10/11 unfixable pop-up. Auto-pick the `(Recommended)` in-range option, default the buffet to its table state, create a sensible tag, pick the highest-confidence anchor, and log each non-default choice in the summary. The mid-run pop-ups described elsewhere in this file apply to SINGULAR interactive mode only.

The "Autonomous mode" section further down describes the no-gate engine run, which is what the BATCH uses. The SINGULAR command wraps the same engine with the pre-publish gate below. The "never interrupt mid-write" rule still holds for both: the singular gate is AFTER the full draft + audit, never during writing.

**Publish gate is caller-owned (site `gate_level`).** Singular always gates (publish on the operator's approval). In batch posture the publish/schedule gate is owned by the batch runner per the site's `gate_level`: `autonomous` schedules directly; `review-batch` or `review-all` hold every post as a draft for the operator to approve before anything publishes. The engine always produces a DRAFT in batch posture regardless; whether that draft publishes is the caller's decision, not the engine's.

**Flagship-format exception (operator-owned content).** A post whose queue `format` is `playbook` is never written in batch posture. Playbooks are the operator's flagship content: they run in singular/attended mode only. The operator shapes the angle first (use `--review-outline` so the angle/outline gate fires BEFORE drafting), the engine drafts, the operator approves at the pre-publish gate, and it publishes immediately on approval. A batch runner should exclude `format=playbook` rows when it builds its queue, so the batch only ever handles spokes (all other formats). If a `format=playbook` row somehow reaches the engine in batch posture, STOP and flag it as a misroute; do not auto-write it.

## Singular mode (when invoked directly)

1. **Resolve the site (fuzzy, confirm on ambiguity).** Match the `<site>` argument against the site registry (slug, domain, or natural-language name). MATCHED -> use that slug. AMBIGUOUS or NONE -> ask which site (the ONLY routine question; writing to the wrong domain is costly). NONE -> offer to onboard it.
2. **Preflight (singular).** Before writing, confirm the site is reachable, its `blog-pipeline-config.md` exists and parses, and its trackers are readable. A missing keyword queue is fine (the topic is the input). Stop on blockers (missing config, site unreachable), continue past warnings (static platform, no reference post) but carry them into the report. **Cold topic (no prior plan): research first, confirm the angle, then write.** When the topic has no matching queue row (it did not come through a prior content-planning pass), no prior plan vouches for the angle or demand, so: (a) in Phase 1 add a keyword-tool demand pull (a keyword research tool such as Semrush, Ahrefs, or Keyword Planner: volume, related terms, and the questions report for the topic) on top of the SERP + scrape research, since no queue-provided keyword data exists; (b) treat `--review-outline` as ON by default, presenting the research + demand read + proposed angle and outline for the operator to steer BEFORE drafting. A topic that DID come from a queue row already carries the plan's keyword + angle work, so it drafts straight through unless `--review-outline` is passed.
3. **Content sourcing mode** (where the SUBSTANCE comes from). Read the site's `content_sourcing_default` from the registry; override per post with `--research` / `--from`:
   - **research-first** (default for SEO/directory sites): substance from SERP data + competitor page scrape + gap analysis. Phases 1-3 as written.
   - **knowledge-first** (default for personal-brand / expertise sites): substance from the operator's own material -- a named body of their own expertise (`--from <source>`: a knowledge base, a skill they maintain, a folder of notes) and/or a path to their notes. Research is DEMOTED to a positioning scan: still run a light SERP pass to see what ranks, which angles exist, what to differentiate against, and which keywords to target, but the CONTENT is the operator's expertise and POV, not SERP-derived. Phase 3 flips from "fill content gaps" to "position my take distinctly"; E-E-A-T is naturally stronger.
   - **blend**: the operator's material as the spine + research to fill specific gaps and fact-check.
   - `--from <skill-or-path>` names the source; `--research positioning|full` overrides the depth.
4. **Voice + E-E-A-T per the site config** (first person + the operator's real experience on a personal-brand site).
5. **Run the engine to a DRAFT** (Phases 1-7), not live. CMS -> unpublished/draft status. Static -> produce the draft entry.
6. **Pre-publish review gate (default ON).** Present the single-post report: title, angle, the draft (or a tight summary + preview link), primary keyword + density, sources, cannibalization check vs the live corpus, and the listing/CTA decision. Operator approves / redirects ("change the angle to X") / stops. A redirect re-drafts and re-reports. `--review-outline` adds an earlier gate on the angle/outline BEFORE the full draft (cheap steering). `--no-gate` skips the gate and publishes live end-to-end (the fully autonomous behavior) for when the operator trusts it blind.
7. **Publish immediately on approval.** CMS -> set status to published NOW (live), run the full Phase 10 + 11 audit on the live post, auto-fix. Static -> publish via the static-site branch (see the static-site platform branch under the phases): insert the entry into the data file, run the local build, then STOP for the operator to commit + deploy; do NOT push or claim it is live unattended.
8. **Record + no-orphans.** Append to the site's trackers + the keyword queue as `status=published` (so the corpus consistency + cannibalization checks see it and future batches never duplicate it); add 1-2 back-links per the no-orphans rule.
9. **Social repurpose (opt-in, `--social`).** When invoked with `--social` on a published post, after step 8 generate social drafts from the published article (one per network the operator uses). Drafts only, never auto-posted. On a static site, run this only AFTER the operator has deployed the post, since its URL must resolve first. Without `--social`, singular publish does not touch social.

## Project config discovery

On invocation:

1. Determine the active project from the `<site>` argument (resolved against the site registry), OR from the `--project <slug>` flag.
2. Load that project's `blog-pipeline-config.md` from wherever the project keeps its working docs.
3. If config is missing: abort with instructions to create it (contract below).
4. If multiple projects could match: ask the operator via an interactive question.

## Config file contract

Every project using this skill provides `blog-pipeline-config.md` with these sections:

```markdown
# Blog pipeline config — <project-name>

## Site + infra
- Site URL: https://example.com
- Access method: <how this machine reaches the site: an SSH host alias, an API base URL, a local repo path>
- CMS root path: /home/user/public_html
- Publish method: cli | rest-api
- Cache flush command: <the platform's cache-clear command, or "none">
- CDN purge helper: <shell snippet or "none">

## Authors
- Default author ID: 3
- Author display name: Jane Doe
- Author bio hint: <one-line>

## Post taxonomy
- Default category slug: guides
- Category ID map:
    - guides: 12
    - reviews: 15
    - tips: 18
    [...]

## Geography + currency
- Primary geography: <city, country>
- Currency symbol: <currency symbol>
- Banned phrases specific to this project: <extends global ban list>

## Shortcode library
- Prefix: <prefix>_      (a short namespace unique to this site, e.g. `acme_`)
- Shortcodes available (name → purpose):
    - <prefix>_freshness_stamp → "last updated · reviewed by" header
    - <prefix>_key_takeaways → TL;DR blockquote
    - <prefix>_pricing_tiers → comparison table
    - [etc.]
- Pricing config file path: /path/to/theme/inc/blog-config.json

## Trackers + data
- Keyword queue folder: /path/to/keyword-queue/
- Posts tracker: /path/to/posts-tracker.md          (one row per published post: id, URL, keyword, dates, status, inbound links)
- Factual tracker: /path/to/factual-tracker.md      (claims extracted at Phase 6, each pending until sourced)
- Changelog: /path/to/changelog.md                  (append-only record of every publish and every auto-fix)
- Internal-link catalog: /path/to/seo-pages.json    (every URL on the site + `is_indexable` + `page_type`; the indexability gate for internal links)
- Catalog refresh script: /path/to/scripts/build-seo-pages-catalog.php

## Content templates + link plan
- Content templates: /path/to/content-templates.md
    Defines this site's template TIERS (e.g. T1 Hub, T2 Best-of, T3 Geo, T4 Pricing, T5 Specialist — name your own) and, per tier: the word-count range, the required vs optional components ("component buffet" table with each optional defaulting ON or OFF), which components the theme renders natively versus which the body must emit, and the per-template internal-link plan (how many anchors, of which types).
- Internal-linking plan: /path/to/internal-linking-plan.md
    Optional. A curated per-post list of preferred link targets. When present it takes priority over generic catalog selection; the catalog still gates every choice on indexability.

## Editorial rules (project-specific)
- Entity-mention rule: <e.g. "no individual listed businesses named in editorial unless the operator hand-selects them">
- Required links: <e.g. methodology page, editorial team page>
- FAQ format: <accordion shortcode | plain H3+p>

## Image generation
- Provider: fal.ai | openai | unsplash | none
- API key env var: FAL_API_KEY
- Post-processor script: /path/to/scripts/process-image.py   (resize + convert to the output format below)
- Output format: webp
- Max dimensions: 1536x1024
- Quality: 82
```

The block above IS the template: copy it, fill every field for the site, and save it as that site's `blog-pipeline-config.md`.

## Autonomous mode (default)

Default behaviour: zero in-process interrupts. The skill runs Phase 1 → 9 end-to-end + the end-of-run self-audit (§ "End-of-run self-audit + auto-fix" below) and only stops at:

1. **A single end-of-run verdict pop-up** after all phases + audit pass. The pop-up confirms the post is live and clean; the user marks Works / Broken / Needs more time.
2. **An unfixable escalation** during audit (cannibalization ≥30% with an adjacent published post, factual claim that has no resolving HTTP-200 source, image safety rejection, slug collision the slug-disambiguator can't resolve cleanly). These pop up mid-run with the specific decision needed.

Fixable issues caught by the audit (zero counts, em-dashes in structured-field rows, source URL rot, keyword stuffing or under-use, missing back-links, wrong taxonomy parameter, etc.) are auto-fixed without surfacing. Each auto-fix is logged in the changelog with risk + before/after, but no user prompt.

**Opt-in gates.** Pass any combination to add review checkpoints:

| Flag | Effect |
|---|---|
| `--review-outline` | Pop up the 3 H1 candidates + outline + 3 info-gain points after Phase 4 (the historical Gate 1) |
| `--review-images` | Pop up the 4 featured variants + 2 inline previews after Phase 7 (the historical Gate 2) |
| `--review` | Pop up before Phase 8 publish for final approval (additive, can combine with the others) |
| `--dry-run` | Stop after Phase 4 — generates outline + draft + audit-plan but does not publish |

**Voice.** When running autonomously, do not narrate every phase. Surface progress in 1-line status updates only when something meaningful changes (e.g. "draft complete, 1857 words" / "fixed taxonomy on row 0 (was 0, now 1,621)" / "all green, post live"). The user does not need a play-by-play.

## Platform-bug fix policy

If the end-of-run audit reveals a defect that lives in shared code (theme template, mu-plugin, project script, content-templates buffet, blog-pipeline-config), fix it at the SOURCE so the next post inherits the fix automatically. Never patch only the current post if a regex / template / config change would prevent recurrence across the corpus.

Examples of this class:
- Wrong `taxonomy` default on `[<prefix>_service_stats]` → patch the doc + add a pre-publish render check.
- Em-dash audit only scanning body HTML → extended scan to all 9 authored fields (body, title, excerpt, takeaways, source_name, source_description, the SEO title meta, the SEO description meta, and any publish-script literals).
- Parens-URL regex only matching naked domains → extended to `(domain.com/path?query=val)` form + html_entity_decode on captured path so query-string URLs survive `esc_html`.

When applying a platform fix during autonomous mode:
1. Backup affected file(s) with `.bak-YYYYMMDD-<reason>` suffix.
2. Apply change. PHP-lint via `php -l` if PHP. Smoke-test homepage + sample post + the post just published (3 URLs minimum).
3. If any URL drops out of HTTP 200 OR error log gains a Fatal/Parse, auto-revert from backup, abort the platform fix, and escalate to the user with diagnosis.
4. If the fix involves a tracked memory or doc, update those too in the same commit-equivalent batch (config file + memory file + lesson file).

## Hardcoded rules (all projects, no exceptions)

1. **Zero forbidden words**. Load the operator's banned-words + banned-sentence-patterns list (recorded once in the site config, or in a house style guide the config points at) and scan before publish. Fail audit if any appear. If no list has been established yet, ask the operator for one at first run rather than inventing one — a banned-words list is a house style decision, not a default.
2. **Zero em dashes** — use colons, periods, commas, or restructure.
3. **Entity-mention rule**: follow the active project's config for when individual named entities (listed businesses, products, providers) can appear in editorial. Default: not unless user hand-selects via `--featured-entities`. **If the project config defines a minimum quality floor for featured entities (e.g. a star-rating threshold), enforce it as a hard gate**: every entity featured or recommended must meet the floor; verify the entity's stored rating before including it, drop any below the floor, and re-pick a qualifying alternative. The floor overrides coverage goals — never lower it to fill a slot. **If the config defines multiple thresholds (e.g. a minimum rating AND a minimum review/popularity count AND a non-placeholder image), enforce ALL of them as hard gates.** Listing count is quality-gated, never a target: feature only entities you are confident clear every gate; a short list, or zero named entities with the topic covered generically, is acceptable and preferred over padding with weaker entities. **For DYNAMIC listing blocks (the project's auto-query featured block, e.g. `[<prefix>_featured]`): the listing MUST match the article's entity TYPE, never a service-level term.** Drive it by the entity-type family/preset that matches the topic; a service-level taxonomy term cross-categories and surfaces off-type entities (a provider of an adjacent service showing up on an article about a different one, because they happen to share a service tag). The inline directory count and the listing block share the same type scope. See the project config's listing-block type-preset table (audit check 36 enforces).
4. **No inline visual HTML** for reusable components. Use the project's shortcode library. No manual `<blockquote>`, `<table>`, accordion markup in post content.
5. **All DB-derived numbers via shortcodes** (if the project exposes such shortcodes). Hardcoded numbers fail the audit.
6. **Internal links must hit indexable pages**. Pre-flight check via HTTP 200 + robots check, OR via the project's `seo-pages.json` filter (`is_indexable=true`, page_type NOT IN the excluded list per config).
7. **The entity-mention rule** is the #1 reason to respect the config. Never invent "featured" picks via a random-order database query.

## The 9 phases

### Phase 1 — Keyword intel
- Read the keyword queue from the config's queue folder (CSVs or markdown).
- Extract Volume, KD, CPC, Intent, SERP Features, Competitors for the primary keyword.
- If user provided `--variants`, use them; otherwise auto-generate 2 semantic variants from the queue.
- Run a SERP query (via whatever SERP API is connected: SerpApi, Serper, DataForSEO, or an equivalent) on primary + variants with `location` set to the project's primary geography.
- Output: SERP snapshot (top 10 organic, PAA, related searches, featured snippet, AI Overview presence).

### Phase 2 — Competitor intel
- Scrape the top 5 content-y results (via whatever page-scraping tool is connected: Firecrawl, Jina Reader, a headless browser, or an equivalent); skip deal aggregators, social, forums.
- Extract: title, word count, H2/H3 structure, price/stat mentions, unique angles, CTA type, FAQ presence.

### Phase 3 — Gap analysis + project facts + canonical entity extraction
- Build competitor matrix from Phase 2 top-5 scrape.
- Identify 3+ information-gain angles that ≥6/10 competitors miss.
- Query project DB via its shortcode library if applicable (example: `[<prefix>_service_stats slug=X stat=total]` — actual prefix from config).
- Classify source domains: Primary (standards bodies, official docs), Neutral (edu, gov, reputable media), Vendor, Community.
- **Extract canonical entity set** (E-E-A-T topical-completeness signal). For each top-5 competitor body:
    - Run light NER for: named places (countries, cities, regions, specific venues), products / ingredients (named compounds, branded materials), processes (named techniques, ritual steps), people / institutions (regulators, professional bodies), tools / equipment (named instruments).
    - Aggregate counts across the 5 competitor pages.
    - **Canonical entity** = appears in body of ≥3 of 5 competitors. Cap at 15 total to avoid over-fitting.
    - Output `entities_canonical[]` (list of {entity_name, type, competitor_hit_count}) feeding Phase 4 planner.
    - The writer (Phase 5) MUST mention each canonical entity ≥1x in body. Phase 10 audit Check 26 enforces.

### Phase 4 — Structured Planner output [GATE 1, default OFF]

Generate full structured plan (JSON) with these top-level keys:
- `target_and_purpose` (primary_keyword, search_intent, funnel_stage, user_job, secondary_keywords, secondary_keyword_map, terminology_map)
- `serp_reality_check` (dominant_page_type, common_promise, serp_features, top_competing_urls)
- `intent_lock` (intent_statement, not_intent_boundaries, **`label`** ∈ `informational | commercial | transactional | navigational`, **`justification`** one sentence, **`derived_from`** SerpApi signals used)
- `uniqueness_gate` (decision, reason, canonical_slug_candidate). **Slug-collision pre-check (HARD): verify the candidate slug collides with NO existing entity — not just a blog post, but any page, any directory/listing post type, or any taxonomy term that owns a public `/{slug}` URL. On collision, choose a DIFFERENT slug for the article; never remove, redirect, or claim the existing URL (whatever exists stays as-is, the article yields). Prevents the article-vs-directory URL-hijack class.** **H2-skeleton variance (anti-doorway, enforced by audit check 35): the outline's H2 set MUST NOT replicate a same-cluster sibling's — vary the section order, include at least 2 H2s driven by THIS post's own SERP/PAA, and at least one section no sibling has; keep the shared H2 set under 60% (compute it directly: normalize each H2 to lowercase words, then shared-H2 count / target-H2 count). Body prose likewise carries no near-verbatim sibling passages (compute directly: 5-gram Jaccard similarity <12% after normalizing away place names, and <8 sentences identical between the two bodies). A geo-by-service combinatorial content plan is exactly the scaled-content pattern search engines target, so uniqueness is a hard gate, not a nicety.**
- `scope_boundaries` (in/out of scope, audience_for/not_for)
- `required_topical_coverage` (must_cover_subtopics, paa_questions, snippet_target, **`entities_and_terms.canonical[]`** = list of {name, type} sourced from Phase 3, **`entities_and_terms.must_mention[]`** = subset enforced at Phase 5)
- `information_gain_plan` (what_we_add, unique_angle, depends_on_notes)
- `eeat_notes` (writer_profile, examples_needed, author_bio_hint, expert_review_suggestion)
- `facts_and_sources` (standard_facts, tool_dependent_facts, claims_needing_citations)
- `ymyl_safety_check` (**YMYL-track detection:** if the primary topic falls in a Your-Money-Your-Life category per the site config's YMYL list (medical and cosmetic-medical procedures, health claims, financial or legal advice), set `ymyl_track=true` -> route to the dedicated YMYL category, REQUIRE the appropriate disclaimer component immediately after the direct-answer intro, name the REAL regulator and licence regime that applies in the site's jurisdiction (the site config records which bodies license this activity locally — a general trade licence and a sector-specific professional licence are usually distinct, and conflating them is a factual error), keep the reviewer TRUTHFULLY scoped (no fabricated professional credential), and ensure every safety/efficacy/price claim is sourced (the pre-publish factual gate blocks an unresolved High-severity claim before it auto-publishes).)
- `page_lock` (slug, titles, h1, meta_description, opening_promise, outline with h2/must_deliver/include arrays). Planner MUST include `title_pixel_width` and `meta_description_pixel_width` integers for every emitted option (measured as Arial 20px for title, Arial 13px for description — matches Google SERP rendering and Yoast/Screaming Frog tooling). Target: title ≤ 580px, description ≤ 920px (desktop SERP budgets). Floor: title ≥ 380px, description ≥ 700px (avoid SERP-waste). Character counts can be emitted as a secondary field but pixel width is the enforcement metric. Options that miss the window must be regenerated before Gate 1.
- `formatting_requirements` (tldr, tables, visuals, examples, quick_checks)
- `shortcodes_planned` (list of shortcode invocations, pulled from the config's library)
- `internal_link_targets` (URLs from the project's seo-pages.json filtered for indexability)
- `source_audit` + `safe_external_links`

**Queue-seed inputs (batch mode).** When the post comes from a keyword-queue row produced by a prior content-planning pass, that row may already carry SERP intelligence computed at plan time. Treat each as the authoritative SEED for the matching planner key, then confirm and enrich with fresh Phase 2/3 data. Prefer fresh SERP data on a conflict, but never drop a queued must-mention `entities` term or a queued `paa_questions` item:
- queue `secondary_keywords` -> `target_and_purpose.secondary_keywords`.
- queue `intent` -> seeds `intent_lock.label` (the Phase 4 classifier confirms it against fresh SERP; the queued value was SERP-confirmed at plan time, so a disagreement is a flag, not a silent overwrite).
- queue `paa_questions` -> merge into `required_topical_coverage.paa_questions`.
- queue `serp_features` -> `serp_reality_check.serp_features`; if it includes `featured_snippet`, set `required_topical_coverage.snippet_target` and open the body with a 40 to 60 word direct answer.
- queue `entities` -> merge into `required_topical_coverage.entities_and_terms.must_mention[]` (union with the Phase 3 canonical set; Check 26 enforces each at Phase 5).
- queue `internal_links` -> seed `internal_link_targets` (union with the indexable seo-pages set).
- queue `campaign_id` and `seed_id` -> carry into the post's tracker record unchanged (lineage). The social drafts generated from this post inherit the same `campaign_id`, so one idea threads seed -> queue -> post -> social.
- queue `format` -> the content type. Drives angle, structure, and CTA emphasis: `playbook` = comprehensive executable guide; `how-to` = single-task steps; `comparison` = ranked options / best-of; `definition` = answer-box-led, open with the 40 to 60 word direct answer; `opinion` = POV; `case-study` = worked example; `trend` = timely analysis. Confirm against the SERP, same as intent. **`format == playbook` is operator-owned: never write it in batch posture (see the Flagship-format exception under "Two postures"); it runs only in an attended singular session with `--review-outline` plus the pre-publish gate, and publishes immediately on approval.**
On a static site with no `seo-pages.json`, queue `internal_links` IS the internal-link plan; resolve each slug against the existing data-file entries and drop any that do not yet exist.

**Default (autonomous mode):** auto-pick the strongest H1 by SERP-feature alignment + pixel width target + primary-keyword placement. Auto-approve outline and proceed to Phase 5. Log the H1 choice and the rejected candidates in the changelog so the decision is reviewable after the fact.

**With `--review-outline`:** present 3 title options + outline + 3 info-gain points via `AskUserQuestion`. Wait for user approval before Phase 5.

#### Search-intent classifier (locks downstream tone, CTA density, title pattern)

Phase 4 derives the post's `intent_lock.label` from Phase 2 SerpApi output using these signals (first match wins, evaluated in order):

1. **Navigational** — single brand domain dominates top-3 organic results (≥2 of top-3 from the same root domain).
2. **Transactional** — ≥3 of top-10 results are booking platforms / aggregators / marketplaces for this vertical, per the project's `transactional_domains[]` config list (populate that list once per site with the aggregators that actually rank in your market).
3. **Commercial** — ≥6 of top-10 results are listicles ("Best/Top X" in titles), OR Featured Snippet hosts a listicle.
4. **Informational** (default fallback) — Featured Snippet present + PAA present, Reddit/Quora in top-10, encyclopedic dominators (Wikipedia, .gov, .edu).

Per-intent writing rules locked to the chosen label:

| Intent | Tone | CTA density | Title pattern (Phase 4 H1) | FAQ skew |
|---|---|---|---|---|
| Informational | Educational, neutral | 1 CTA at end (filter or related-services) | `What Is X? A {Geo} Guide for {Year}` or `X in {Geo}: A Complete Guide for {Year}` | Definitions, mechanics, "how it works" |
| Commercial | Editorial, ranking-driven | 2 CTAs (filter + premium tier) | `Best X in {Geo} for {Year}: {Currency} Y to Z` or `Top X {Geo}: {N} {Vetted/Editorial-Picked} Options` | Comparison, when-to-pick, vs alternatives |
| Transactional | Action-oriented, conversion-leaning | 3+ CTAs throughout body (filter + tier + final) | `Book X in {Geo} (From {Currency} Y)` or `X in {Geo}: Pricing, Booking & {Locations}` | Pricing, availability, booking flow, what to expect |
| Navigational | Brand-focused, factual | 1 CTA to brand listing page | `{Brand} ({Geo}): Reviews, Prices, Booking` (rare in editorial; often a profile page handles it) | Brand-specific operational questions |

If the classifier output and the post's primary keyword strongly disagree (e.g. classifier says navigational but primary kw is generic), surface to the parent for a single-question gate before proceeding. The classifier's `justification` field must cite the SerpApi evidence used.

**Component buffet (when project's content template defines required vs optional components):**

If the project's `content-templates.md` contains a "Component buffet" table for the active template (T1 / T2 / etc.), Phase 4 ALSO asks the user which optional components to include for THIS post. Default each optional component to its `default ON | OFF` state per the table. Required components are always included; user cannot deselect them.

Example for T1 Hub: required components include direct-answer intro, methodology + callout, cost + pricing tiers, areas + neighborhood table, tier H3s, what-to-expect, vetting, mistakes, FAQ, related services. Optional components include legality H2, types-of-{service}, where-to-book apps list, article sources, final recommendation. The skill asks the user to confirm or deselect optionals via a single `AskUserQuestion` (multiSelect=true).

### Phase 5 — Draft (writer hard rules)

Follow plan exactly. 25 hard rules:
1. Structure = plan's H2s verbatim, exact order.
2. **Primary keyword density and placement.**
    - In H1 (exact match).
    - In the first 100 words of body (exact match acceptable; head-of-primary substring acceptable if the full primary appears in H1 and meta).
    - In at least one H2 (exact match OR a clear near-match using the head-of-primary substring).
    - **Topic density (combined):** count exact-match occurrences AND head-of-primary substrings (e.g. for primary "office cleaning manchester", the substring "office cleaning" counts; for "best sourdough course berlin", "sourdough course" counts; for "emergency plumber austin", "emergency plumber" counts). Combined topic density target: **0.5%–2.0%** for entity-defining articles, **0.3%–1.5%** for broad topics. **HARD CEILING 3.0%** (the keyword-stuffing threshold). For a 1,800-word entity article that means 9–36 combined occurrences.
    - **Per-paragraph cap:** never 2 exact-match (full primary) occurrences in the same paragraph. The substring form is uncapped per paragraph because it reads naturally. Rephrase to a natural stand-in ("the service", "this process", "the session") or a pronoun when the full primary repeats.
    - The legacy "3–6 total exact-match" rule was too tight for entity-name articles and is superseded by combined topic density.
3. **Secondary keywords distribution.**
    - Pull the list from the project's keyword queue (`secondary_keywords` field, semicolon-delimited) for the post being written.
    - **Substring-of-primary exemption.** Any secondary that is a strict substring of the primary keyword (e.g. "office cleaning" when primary is "office cleaning manchester", "sourdough course" when primary is "best sourdough course berlin") is EXEMPT from the per-secondary cap below. It counts toward the primary's combined topic density (rule 2) instead. This prevents the perverse outcome where natural short-form prose ("the office cleaning option") gets flagged as secondary-keyword stuffing.
    - **Truly distinct secondaries.** For each secondary that is NOT a substring of the primary (e.g. "commercial cleaning" alongside primary "office cleaning"; "sourdough workshop" alongside primary "sourdough course"):
        - MUST appear at least once in body prose (not just in image alt text or source descriptions).
        - Aim for 1–3 occurrences each, distributed across different H2 sections (no clustering inside one section).
        - Hard cap: no single secondary appears more than 5 times in body. Above 5 reads as stuffing.
        - Land them in H2/H3 text, FAQ Q+A, table cells, prose. Never force-fit; if a secondary cannot land naturally, drop it from the post and surface in the audit log.
4. Snippet-ready direct answer 40-60 words after H1.
5. TLDR 2-3 sentences, one paragraph, no bullets (if `formatting_requirements.tldr = "yes"`).
6. PAA format: `**Question** Answer. <2-4 sentences or 3-5 bullets>`. Max ~120 words per PAA block.
7. **Every entity from `entities_and_terms.must_mention[]` (canonical set extracted at Phase 3) MUST appear ≥1x in body prose.** The writer cannot drop one. If a canonical entity does not fit naturally anywhere, restructure the affected H2 section to make room — entity coverage is a hard E-E-A-T signal. Phase 10 audit Check 26 enforces.
8. Only state facts present in `facts_and_sources`. Tool-dependent facts start with "This varies by tool."
9. Information gain assets placed in the most relevant H2.
10. Examples from the plan, or labeled "Hypothetical example". No brand names in hypotheticals.
11. Tables where plan asks. Max 8 rows. Takeaway sentence after each.
12. Lists over paragraphs when 3+ items. TLDR stays plain sentences.
13. Paragraphs max 90 words.
14. Zero URLs in article body.
15. Zero CTA closers.
16. Entity-mention rule enforced (per project config).
17. **Zero forbidden words across EVERY authored field.** Scan body, post title, post excerpt, the `key_takeaways[].takeaway` rows, the `sources[].source_name` rows, the `sources[].source_description` rows, the SEO title meta, the SEO description meta, AND any literal strings in the publish script before publish. Body-only scan misses the 8 other fields where authored copy lives.
18. **Zero em-dashes (—) and en-dashes (–) across the same 9 authored fields.** Same scope as rule 17. Theme-emitted inline `<script>` developer comments are out of scope (not article copy).
19. Shortcodes for every visual component (never inline HTML for components that have a shortcode).
20. Respect the project's deprecated-shortcode list (from `blog-pipeline-config.md`). Do NOT emit deprecated shortcodes in new posts even if older posts use them. Common pattern on directory sites: native theme byline + author popover + a structured-field-driven takeaways aside replace `[<prefix>_freshness_stamp]`, `[<prefix>_key_takeaways]`, `[<prefix>_author_card]`. Set the structured / native fields at Phase 8 instead.
21. Native theme components: when the project's theme natively renders byline / author / takeaways / TOC / breadcrumbs (check `content-single.php` or equivalent), do NOT duplicate them in body shortcodes. The buffet table in `content-templates.md` lists which components are theme-native vs body-rendered.
22. **Tables for information gain.** When a section's content has clear column structure (brand/provider listings, tier comparisons, areas + counts, methodology criteria, vs-comparisons), render as an HTML `<table>` not a `<ul>`. Mobile-readable: 3-4 columns max; consolidate context into single cells when needed. Tables work as featured-snippet candidates and reinforce info-gain perception.
23. **External links to commercial brands or competitors** carry `rel="nofollow noopener"`. The 2-max editorial external-link budget (gov, journals, regulatory bodies) is SEPARATE from the nofollow brand-list budget (no cap on nofollow links to home-service brands / competitor platforms when the project authorises an entity-mention carve-out). Confirm rel attribute on every outbound brand link before publish.
24. **Per-entity card shortcode (when the project config defines one).** If the project's `blog-pipeline-config.md` shortcode library exposes a per-entity card shortcode (e.g. `[<entity> id="POST_ID"]` for directory-style sites where each entity has its own profile page), use it for the FIRST mention of every named entity in the post body — never a plain `<a href="/{slug}">{Name}</a>` anchor for the first mention. The card renders the entity's canonical info row (image, name, location, rating, price, badge) at a glance; a plain anchor hides all of that. Subsequent in-paragraph references to the same entity by name can stay as plain text. Pre-publish: look up each named entity's record ID via the project's entity-list query, then smoke-test that the card shortcode renders non-empty against the live site before pasting into the body. Project configs without a per-entity card shortcode are exempt from this rule.
25. **Directory/listing counts (HARD RULE — generic; the site config carries the specifics).** NEVER type a directory listing count as a literal number (it goes stale and drifts). Emit it via the site's dynamic-count component WITH the trust-floor, and SCOPE-MATCH the count's filter to the article's actual subject:
    - **Geo-generic article** ("listings in {area}") -> location-axis token (all listings in the area).
    - **Type/service article** ("best {type} in {city}") -> type/service-axis token (that type citywide).
    - **Compound article** (a type/service IN a location, e.g. "{type} in {area}") -> the COMPOUND token (type AND location) via the clause wrapper, with a TYPE-PRESERVING fallback: at/above floor render the exact compound count; below floor KEEP THE TYPE and broaden the location to citywide; NEVER drop the type to a location-only count (an article about one service type must never count or surface entities of other types).
    - Apply the trust-floor: a 0 count never renders ("0 listings" is a false claim); a sub-floor count renders a qualitative phrase or drops the clause, never a low bare digit. Use the dense CANONICAL area slug (not a fragmented thin variant) and the correct taxonomy. The inline count and the post's listing block MUST share the same scope. Floor values, the token/wrapper names, the taxonomy map, and the canonical-slug map all live in `blog-pipeline-config.md`. Phase 10 audit checks 14 + 34 enforce this.

### Phase 6 — Pre-publish audit

Hard-fail stops the pipeline (cannot publish until clean).

Checks (body draft + planned structured fields + planned meta):
1. Word count in template range.
2. Forbidden words count = 0 across all 9 authored fields (rule 17).
3. Em-dashes + en-dashes count = 0 across all 9 authored fields (rule 18).
4. **Internal link count.** Total anchors: 8–12 in body (8 floor, 12 ceiling). Unique targets: 8 minimum, 12 maximum. Duplicating an anchor across two H2 sections (e.g. Types section + FAQ) is acceptable when both placements serve navigation, but the duplicate must serve a distinct user-intent: re-pointing from a "decision" section AND a "what-is" section is fine; pointing twice in adjacent paragraphs is not. **The "injector" is NOT a script.** It is the writer/LLM placing in-content `<a href>` anchors during Phase 5 draft per the project's `content-templates.md` per-template link plan, with the project's `internal-linking-plan.md` (when one exists) as the curated per-post target list and `seo-pages.json` as the indexability gate. If writer placement is below 8 at this Phase 6 check, the WRITER (not a script) tops up to 8 using the same selection rules. Writer-placed anchors above 8 stay unless they exceed 12 or violate a sub-cap (max 2 hub, max 2 tool, max 1 generic, max 2 blog-to-blog). The Phase 8 self-grep gate (step 2) and the Phase 10 deterministic anchor-floor check are the two backstops that fail-loud if this step is silently skipped.
5. Every internal link target returns HTTP 200 + `is_indexable=true` in `seo-pages.json`.
6. Every shortcode referenced is registered in the project's library.
7. Factual claims extracted → appended to the project's `factual-tracker.md` as `pending`.
8. **Primary keyword density:** count exact-match occurrences in body. Confirm density falls in the 1.0%–2.0% (entity) or 0.5%–1.5% (broad) window. Fail above 3.0%.
9. **Per-paragraph primary keyword cap:** scan each `<p>`, `<li>`, table cell. Fail any with ≥2 exact-match occurrences.
10. **Secondary keyword presence:** for each item in the post's `secondary_keywords` CSV field, count occurrences in body. Fail if any secondary appears 0 times OR >5 times.
11. **Pre-publish dynamic-count render:** for every `[<prefix>_service_stats slug="X" stat="..." taxonomy="..."]` in body OR in the structured `sources` descriptions, run `wp eval "echo do_shortcode('[<prefix>_service_stats ...]');"` against the live server. Fail if any returns 0 or empty. (Picks up wrong-taxonomy errors before they ship.)
12. **Source URL HEAD-test:** every parenthesised URL in `sources[].source_description` returns HTTP 200. Fail any DNS error, 4xx, or 5xx.
13. **Named-entity plain-anchor check (rule 24 enforcement).** If the project config defines a per-entity card shortcode, grep the body for `<a href="<site_url>/{entity-slug-pattern}">{Name}</a>` patterns referencing entity profile pages. Each match where the same entity has no preceding `[<entity> id="X"]` card on first mention is an audit failure. Fix: replace the first-mention anchor with the card shortcode (look up POST_ID via project's post-list query); subsequent mentions of the same entity by name remain plain text and are allowed.
14. **Featured-entity quality floor (rule 3 enforcement).** If the project config defines a minimum rating (or equivalent quality) floor for featured entities, query the stored rating of every featured/recommended entity in the post (every `[<entity> id="X"]` card and every named recommendation). Fail the audit if any entity is below the floor. Fix: remove the sub-floor entity and re-pick a qualifying alternative that preserves the post's category / sub-area coverage; never lower the floor to keep a slot filled.

### Phase 7 — Images (featured + 2-3 inline) via configured provider

Read the image provider from project config. Any current text-to-image API works (Google's Gemini image models, fal.ai's Flux models, OpenAI's image endpoint, Replicate, and equivalents); pick one as the default and one as the fallback, and record both in the config. What follows shows the shape of the call against one provider — substitute your provider's endpoint, auth header, and response field, and keep everything else (the prompt clauses, the variant count, the QA rules), which is provider-independent. Re-benchmark providers occasionally on photorealism, cost, and latency rather than treating any default as permanent.

**7a. Featured image (primary provider path).**
1. Compose prompt (separate LLM call). Include anti-anatomy clause verbatim when a person is present:
   > "single person, framed above waist, face out of frame, anatomically correct hands, exactly two hands visible, five fingers on each hand, natural finger lengths, no extra fingers, no missing fingers, no duplicated hands, no extra limbs"
   **Glove / partial-coverage clause (MANDATORY whenever a worker, technician, or practitioner appears in a hands-on service scene):** gloves and worn items are ALL-OR-NOTHING. Add verbatim: "if gloves are worn, both hands fully gloved with every finger covered to the fingertip; otherwise both hands fully bare; never a partial glove, never a glove that ends mid-finger or mid-hand, never one gloved hand and one bare hand; sleeves, cuffs and jewellery rendered consistently, no object fading into skin." When a clean result is hard to guarantee (close-up service shots), PREFER bare hands in the prompt: it removes the glove-boundary failure mode entirely.
   Always include: "editorial documentary style, photorealistic, natural lighting, realistic textures, shallow depth of field, organized background, no readable text anywhere, no logos, no watermarks, no brand marks, no labels."
   **Also avoid concept-collision props:** depict ONE coherent service per image. Do not combine signals from two different services in one frame (e.g. hair-colour foils on the client AND a makeup brush on the face; a barber cape AND nail tools). Name the single service and its matching props only.
   **Match the subject's real-world tier and locale: do not default to luxury or modern interiors. If the project config specifies a location or market tier for the post (a budget or older district versus a premium area), bake it into the prompt so the image reflects reality: authentic and modest where the area is modest, polished where it is premium. Realistic, not cheap.**
2. The image provider's API key is read from the environment. Keep it in your own secret store (a git-ignored env file loaded by your shell profile, or your OS keychain) and never inline it in a config file, a script, or a post. Reference it only by variable name.
3. Generate 4 variants. If the provider exposes a variant/batch count, request 4 in one call; if it returns one image per call, POST 4 times in parallel. Shape of the call (substitute your provider's endpoint, auth header, and body schema):
   ```
   curl -sS -X POST "<PROVIDER_IMAGE_ENDPOINT>" \
     -H "<AUTH_HEADER_NAME>: $IMAGE_API_KEY" \
     -H "Content-Type: application/json" \
     -d '{ "prompt": "<prompt>", "aspect_ratio": "16:9", "n": 4 }'
   ```
4. Read the image bytes out of the provider's response (usually a base64 field or a signed URL to download) and save each variant to disk.
5. **Auto-mode (default):** the parent picks the strongest variant by visual heuristic (no readable text, anatomy-clean, well-composed). The Phase 10 audit re-checks the choice. **Anatomy QA is a boundary scan, not just a finger count:** explicitly trace where one material meets another (glove cuff to skin, glove fingertip, sleeve end, ring/bracelet, towel edge) and reject any variant where an object fades, ends mid-finger, or is present on one hand but not the other. Finger-count-correct is necessary, not sufficient. Reject any concept-collision (two services' props in one frame).
   **`--review-images` flag:** present 4 variants via `AskUserQuestion` for user pick.
6. Run the project's post-processor: `python3 <post-processor-script> <input.jpg> <output.webp>`.
7. Upload to WP media (POST `<site>/wp-json/wp/v2/media` with binary body, OR `wp media import` via SSH).
   **Attachment-slug guard (HARD — stops the pipeline colliding with its own image).** WordPress derives an attachment's `post_name` from its `--title` via `sanitize_title()` (or from the filename when no `--title` is passed). If that derived slug equals the article's intended slug, the imported image claims `/{slug}`, and Phase 8's slug-collision pre-check then fires on the pipeline's OWN attachment, blocking the publish. So immediately after EVERY media import, force the attachment's `post_name` to a suffixed value that can never equal the post slug — `<slug>-featured` for the featured image, `<slug>-inline-<N>` for each inline (matches the filename convention the project config sets):
   ```
   FEAT_ID=$(wp media import /tmp/<slug>-featured.webp --title="<title>" --porcelain)
   wp post update "$FEAT_ID" --post_name="<slug>-featured"
   ```
   Do this BEFORE Phase 8. Verify with `wp post list --post_type=attachment --name=<slug> --field=ID` returning empty.
8. Update metadata (title, alt, caption, description per the project's alt-text pattern).

**7b. Inline images (2-3).** Same pipeline, 1 generation per inline. Place after specific H2s chosen at Phase 4 outline (project config defines which H2s). Apply the same attachment-slug guard from 7a to every inline (`<slug>-inline-<N>`).

   **Resolved-URL capture (HARD — stops inline-image 404s).** WordPress does NOT serve uploads from a bare `/wp-content/uploads/<filename>` path: it stores every media file under a date-based subfolder (`/wp-content/uploads/YYYY/MM/<filename>`). A body `<img src>` built by hand from the filename therefore 404s and the inline image silently fails to render. So immediately after importing each inline image, read its REAL public URL from the CMS and carry it forward to Phase 8 — never reconstruct the path:
   ```
   INLINE_ID=$(wp media import /tmp/<slug>-inline-<N>.webp --title="<inline alt summary>" --porcelain)
   wp post update "$INLINE_ID" --post_name="<slug>-inline-<N>"
   INLINE_URL=$(wp eval "echo wp_get_attachment_url($INLINE_ID);")   # the ONLY value allowed in the body <img src>
   ```
   Record `($INLINE_ID, $INLINE_URL)` per inline. Phase 8 step 1 injects `$INLINE_URL` verbatim into `src` and `$INLINE_ID` into the `wp-image-<ID>` class. The featured image needs no such capture — it is set via `_thumbnail_id` and the theme renders it through `wp_get_attachment_image()`, which resolves the dated URL itself; it never appears as a body `<img src>`.

**7c. Fallback provider path.** If the primary provider's key is missing or rate-limited, fall back to the config's second provider. Same prompt + anti-anatomy clause, same 16:9 landscape sizing, same 4 variants. Note: some image models hallucinate fake stock-photo watermarks despite a negative prompt — flag and regenerate any output with visible text or marks, whichever provider produced it.

**7d. Skip conditions.** No image provider configured → skip image generation, flag "needs images" in post meta at Phase 9, continue. The post still publishes (text-only) — image gap surfaces at Phase 10 audit Check 11.

### Phase 8 — Publish live

1. Assemble final content: draft markdown + inline images injected. **Inline `<img>` `src` = the resolved attachment URL captured in Phase 7b (`$INLINE_URL` from `wp_get_attachment_url`), NEVER a hand-built `/wp-content/uploads/<filename>` path** — a bare path skips WordPress's date-based `/YYYY/MM/` subfolder and 404s, so the inline image silently fails to render. Set the `wp-image-<ID>` class from the real attachment ID. **Pre-publish self-grep (HARD):** scan the assembled body for any own-host upload URL missing the date segment — `grep -oiE 'src="https?://<own-host>[^"]*/wp-content/uploads/[^"]+"' body.html \| grep -vE '/uploads/[0-9]{4}/[0-9]{2}/'` — any hit means a hand-built path slipped in; replace it with the resolved attachment URL before publishing. (Audit Check 37 is the post-publish backstop.)
2. **Internal-link gate — MANUAL writer/LLM step, no script exists.** No executable "injector" lives in the pipeline. In-content `<a href>` anchors are placed by the LLM during Phase 5 draft per the per-template link plan in the project's `content-templates.md`, drawing targets from the project's `internal-linking-plan.md` (when present) gated by `seo-pages.json` indexability. Phase 8 is the **hard self-grep gate** that catches silent under-placement BEFORE `wp post create`. Run this against the assembled body file, never the live URL:
   ```bash
   ANCHORS=$(grep -oiE '<a [^>]*href="https?://<own-host>[^"#]+"' /tmp/<slug>-body.html \
     | sed -E 's/.*href="([^"]+)".*/\1/' \
     | grep -viE '^https?://<own-host>/?$' \
     | grep -viE "^https?://<own-host>/<planned-slug>/?$" \
     | sort -u | wc -l)
   ```
   If `ANCHORS` is below the project's floor from `blog-pipeline-config.md` (typical: 8), the writer adds anchors until it clears the floor, THEN `wp post create`. Every chosen target must pass:
   - `http_status = 200`
   - `is_indexable = true`
   - URL is not homepage; URL is not the current post URL
   - Exclude `page_types` listed in config under `excluded_page_types` (typical: legal, utility, support)
   - Respect the per-type sub-caps from config (typical: 2 hub, 2 tool, 1 generic, 2 blog-to-blog)
   - No links inside headings; no links in first 3 paragraphs or first paragraph under any H2/H3

   **Render vs DB caveat.** If the project ships a render-time future-link guard mu-plugin (e.g. one that unwraps an `<a>` to plain text when its target post is not yet `publish`), the LIVE URL can show fewer anchors than the DB stores. Always self-grep the assembled body FILE (the same string about to go into `wp post create`), never the rendered URL. The Phase 10 deterministic backstop reads the RAW stored post content from the database, so it catches under-floor posts regardless of the render-time guard.

   **Disambiguation from the inbound link-knitter.** This step is the OUTBOUND direction (new post → other pages). It has nothing to do with an inbound link-knitting pass (existing sibling posts → this post), which runs at BATCH level after posts go live, never per-post around the publish call, and is the no-orphans cure, not the in-content anchor source. Keep the two apart: conflating them produces posts that link out correctly and are still orphaned.
3. Run external-link injector using only URLs from Planner `safe_external_links`. No vendor/competitor domains. Max 1-2 outbound links.
4. Slug + meta title + meta description LLM call. **Slug-collision pre-check (HARD):** verify the planned slug does not already exist as ANY entity (published post, page, directory/listing post type, or any taxonomy term owning a public `/{slug}` URL), not just a blog post. On collision, the article takes a different slug; NEVER remove, redirect, or claim the existing URL. **Exclude the pipeline's OWN just-imported attachments from this result:** Phase 7 already suffixed their slugs to `<slug>-featured` / `<slug>-inline-<N>`, so a bare-`<slug>` match should never be one of them — but a `--post_type=any` query still over-matches attachments (the attachment post type registers `public=true`, so `exclude_from_search` resolves to false and `any` includes it — do NOT "optimize away" this guard on the assumption that `any` skips attachments), and an attachment does not own the editorial `/{slug}` the article competes for, so an attachment-only match is a FALSE collision, not a reason to yield the slug. Collide only on URL-owning entities (post, page, the project's directory/listing post type, and public taxonomy terms). Then confirm final uniqueness against `seo-pages.json`.
5. **Meta length validation (hard gate, no publish until resolved):**
   - Measurement metric: **pixel width** in Arial (matches what Google SERP actually truncates and what Yoast / Screaming Frog / Mangools / Semrush report). Character count is a secondary metric only.
   - SEO TITLE meta pixel width at Arial 20px: **380–580px** (target 480–560). Character floor: ≤ 60c to stay green in SEO-plugin admin previews.
   - SEO DESCRIPTION meta pixel width at Arial 13px: **700–920px** (target 820–910). Character floor: ≤ 150c. Char-count SEO tools flag 155c+ red even when pixel width is fine. Targeting ≤150c lands green across all tools AND inside the actual SERP pixel budget.
   - **Which meta field these are is platform-specific and MUST be read from the site config, never assumed.** Every SEO plugin stores the title/description override under its OWN key, and writing the wrong plugin's key sets a value nothing reads: the meta silently stays whatever the theme generated, with no error anywhere. Confirm the site's actual keys once and record them in `blog-pipeline-config.md` as `seo_title_field` / `seo_description_field` / `seo_focus_keyword_field`, then use those names throughout Phases 8-10.
   - Helper to compute pixel width: if the site's theme or a plugin exposes a width helper, use it. If not, compute it directly — sum the per-character Arial em-unit advance widths for the string and scale by `font_size/1000`. Fallback if no width table is available: char-count window 48–58 title / 140–155 desc (approximate).
   - If out of range: generate 3 in-range variants via LLM, surface via `AskUserQuestion`. First option `(Recommended)` is the strongest of the three. Do not publish until the user picks one.
   - Forbidden-words scan runs on both title and description (same ban list as body).
   - If the target project has a length-guard mu-plugin, over-budget values are auto-truncated at publish time; the skill still blocks to keep authorial control of the truncation point.
6. Category auto-assign from the project's category ID map.
7. Markdown → HTML. Tighten `<li><p>X</p></li>` → `<li>X</li>`.
8. Publish via the config's method:
   - wp-cli: `wp post create ... --post_status=publish --porcelain`
   - REST: `POST <site>/wp-json/wp/v2/posts` with Authorization header
9. Set the SEO title meta, the SEO description meta, and the featured-image reference (the site config's `seo_title_field` / `seo_description_field` / the platform's thumbnail field). Also set the SEO plugin's **focus keyword** field if the project uses one (`seo_focus_keyword_field`, comma-separated, PRIMARY first then the post's secondary keywords FROM THE KEYWORD QUEUE that the post was written to target). Use the queue verbatim: do not derive new keywords and do not body-filter. This drives the plugin's on-page SEO score.
10. Set the structured / custom fields when the project's content template uses them (whatever the platform provides: a custom-fields plugin, native custom fields, or a headless CMS's typed fields). Write them via the platform's CLI or API. Common fields on directory-style sites: `key_takeaways` (repeater of `takeaway` strings, drives the takeaways aside) and `sources` (repeater of `source_name` + `source_description`, drives the collapsible Article Source section). Skip the corresponding body shortcodes / static blocks when these fields are set — the theme renders them in the right slots automatically. **Own-source first in `sources` array:** when one of the sources is the project's own directory / database (own data the post references), put that row at index 0 of the array — ahead of regulatory bodies and external citations. Positions the project as the primary source; supporting authorities follow. **Every `sources` row must contain at least one resolving HTTP 200 URL** in `(domain.com)` form (theme regex wraps it in `<a href>` automatically). HEAD-test every URL referenced in source descriptions pre-publish; drop any row whose URL returns DNS failure, 403, 404, or 5xx. No name-only citations in the sources block. **Dynamic counts via shortcode in `source_description`:** if the project's theme runs `do_shortcode()` on source descriptions before escaping (a per-site theme capability; confirm it in the site's `blog-pipeline-config.md`), embed live-stat shortcodes for own-source rows, e.g. `"[<prefix>_service_stats slug='X' stat='total' taxonomy='<own-taxonomy>'] verified listings (own-domain.com) ..."`. The count refreshes on cache rotation. **Own-domain auto-nofollow:** if the theme auto-detects own-host links and adds `rel="nofollow noopener"` to them in the sources regex, no per-link configuration needed; external sources stay `rel="noopener"` and dofollow. Confirm both behaviours exist in the project's theme before relying on them; otherwise hardcode the values manually.
11. Cache flush + CF purge (commands from config).
12. Smoke-test the live URL — includes meta length re-check after server filters run (catches mu-plugin truncation), AND spot-check 1-2 sample category/type/listing pages outside the post itself (a cache purge at publish time is what makes a latent theme-template or routing bug visible, so the post can be perfect while an archive page 500s).

### Phase 9 — Register in trackers + back-links + schedule

1. **Apply tags** per the project's tagging rule (in `blog-pipeline-config.md`). Set at least 1 primary topic tag via `wp post term set <id> post_tag <slug>`. Geography tags only for posts scoped to specific areas, not site-wide pillars. If the relevant tag is missing from the project's predefined list, surface via `AskUserQuestion` rather than skipping.

2. **Inject back-links from existing editorial posts** (no-orphans rule). Scan the project's `posts-tracker.md` for existing posts with body content >2KB and at least one section semantically related to the new post. For each high-confidence match, identify a clean anchor text (existing sentence that names the service or topic), append a single sentence with an anchor link to the new post, save via `wp post update <id>`. Verify `wp post get <id> --field=post_status` returns `publish` after each update — wp-cli has occasionally been observed to trash a post on update; if status comes back as `trash`, recover with `wp post update <id> --post_status=publish --post_name=<original-slug>`. For ambiguous matches (borderline relevance, multiple candidate anchors), surface via `AskUserQuestion` with the specific proposed anchor + target rather than skipping.

3. Append to project's `posts-tracker.md`: post ID, URL, keyword, published date, last-checked, position, status, list of incoming back-links added.

4. Append to project's `changelog.md` (full publish entry + each back-link injection logged).

5. Update `keyword-queue.md`: mark as published with link.

6. If `--batch N --schedule daily`: create cron for the next `/blog-post <next-keyword>`.

### Static-site platform branch (platform == static)

When the site's registry `platform` is `static` (a git-backed static-site repo whose posts are structured entries in a data file or content collection — any static site generator, any host that builds on push), Phases 7-9 publish into the repo instead of over a CMS API. Everything earlier (Phases 1-6: keyword intel, scrape, gap, planner, draft, pre-publish audit) is platform-agnostic and unchanged. Registry fields used: `code_repo`, `blog_data_file`, `build_url_pattern`.

**Phase 7 (Images) static.** Generate images the same way, but do NOT upload to a CMS. Save to disk (`/tmp/<slug>-cover.<ext>`, `/tmp/<slug>-inline-<N>.<ext>`), then copy them into the repo's public asset tree. The body uses site-relative paths: cover `/blog-covers/<slug>-cover.png`, inline `/blog-images/<slug>-inline-<N>.png`. No media import, no attachment-slug guard, no resolved-URL capture (those are CMS-specific concerns).

**Phase 8 (Publish) static.** Steps 1-7 stay (assemble body, internal-link self-grep gate, external links, slug + meta, category, markdown), with these differences: meta is the description field on the post object itself (no SEO-plugin meta keys); the slug-collision check runs against existing slugs in `blog_data_file`, not a CMS query. Then insert the entry into the repo:
  1. Build the post entry in the exact shape the data file already uses (read an existing entry and match its field names and types; a static build fails loud on a shape mismatch, which is the point).
  2. Serialize it and preview the diff WITHOUT writing — confirm the new entry parses and nothing else in the file moved.
  3. **Back up the data file, insert the entry, then run the local build. If the build fails, restore the backup automatically and report the build error.** A half-inserted entry that breaks the build is the one failure mode that can block every future post on this site, so the backup-and-auto-restore is mandatory, not optional.
  No CMS CLI, no structured-field writes, no SEO-plugin meta, no cache flush. The post is now in the working tree, NOT deployed.

**Phase 9 (Register / back-links) static.** Append the trackers (`posts-tracker.md`, `changelog.md`, `keyword-queue.md`) the same way. SKIP the CMS-only steps: no taxonomy API call for tags (tags live in the post object), no back-link injection via a CMS update call (a static post is not live until committed + built; inbound links are a later data-file pass, the static analog of the batch link-knit step). Mark the tracker row `inserted-pending-commit`.

**Deploy is separate and gated.** Committing the data file + pushing the repo default branch triggers the host's build (live). The engine does NOT push unattended; deploy is an explicit operator step (or a preview-branch push where the host builds previews). Verify a deployed post against the live URL built from `build_url_pattern`.

### Phase 10 — End-of-run self-audit + auto-fix (autonomous)

After Phase 9 publishes and registers, run the full audit on the LIVE post. Auto-fix everything fixable, escalate everything unfixable in one focused interactive question, then surface a single end-of-run verdict pop-up.

**Single source of truth: the `audit-checklist.md` file shipped beside this one.** That file holds the checklist, the per-check fix recipes, and the scorecard template the audit returns. SKILL.md does NOT duplicate the rules here — editing the checklist file is enough for every future invocation to inherit the change.

**Auto-fix protocol:**

1. Run the audit. If your host supports delegating to a sub-agent, delegate it to one with read + shell access; if not, run it inline. Inputs it needs: `post_id`, `url`, `primary_keyword`, `secondary_keywords[]` (parsed from the project's keyword queue), `template`, `sibling_urls[]` (adjacent published posts for the cannibalization check), the site's access method + CMS root path, project config path.
2. The audit loads `audit-checklist.md`, runs every check against the live URL, and returns the scorecard in the format defined at the bottom of that file.
3. Parent buckets `findings.fixable` vs `findings.unfixable`.
4. For each fixable: apply the recipe from the checklist's "Fix recipe" column. Log before/after to changelog.
5. After all fixable are applied: re-run the audit ON IMPACTED CHECKS only (don't re-run the whole checklist). Confirm those flip to PASS.
6. If `findings.unfixable` is non-empty: surface ONE interactive question with all blockers in a single multi-select prompt.
7. Run Phase 11 (Visual QA) next — the text audit above cannot see layout/image/link-target defects. Only after Phase 11's fixes land, surface the final end-of-run verdict pop-up: Works / Broken / One-more-tweak / Stop.

**Audit brief (whether delegated or inline):**

> Run the audit defined in `audit-checklist.md` against post `<id>` at `<url>`. Inputs: primary_keyword, secondary_keywords, template, sibling_urls, site access method. Return the scorecard in the format at the bottom of the checklist file. Do NOT auto-fix — the caller applies the fixes.

Keep AUDITING and FIXING in separate hands: the auditor reports, the caller fixes. An auditor that fixes as it goes cannot be trusted to report what it changed, and the audit logic stops being separately reviewable. Where a sub-agent is available, delegating the audit also keeps the main context window clean on a long run.

### Phase 11 — Visual QA (render + assert, main thread)

The Phase 10 audit is text-only (HTML grep + JSON-LD parse): it can confirm an `<img>` tag exists, but not that the image loaded, is the right shape, or that the layout did not break, and it cannot tell whether a linkable entity actually links. Phase 11 closes that blind spot. A text-only auditor has no browser, so Phase 11 runs wherever a browser IS available, after Phase 10's text audit passes.

1. Render the LIVE published post in a real browser at the project's configured breakpoints (default mobile 390 / tablet 768 / desktop 1280).
2. Run `audit-checklist.md` **Section G (Visual QA)**: no horizontal overflow; every content image loaded and none is the placeholder; repeated card components uniform per breakpoint; every internal anchor HTTP 200; link-target completeness for entities whose pages exist.
3. **Mechanic ladder:** a browser-automation tool that can navigate and evaluate JS in the page (Playwright, Puppeteer, or an equivalent) → headless Chrome driven from the shell → curl-only subset. If a check cannot run in the available mechanic, flag it "skipped" in the scorecard — never silently pass it.
4. Auto-fix per Section G recipes (constrain the overflowing element; generate or replace a placeholder/broken image; consolidate conflicting card CSS via ONE higher-specificity scoped block — grep the stylesheet for the literal value to find the winning rule; add missing entity links). Escalate theme-level issues that can't be safely auto-fixed.
5. Re-render the impacted checks to confirm each fix landed.

The final end-of-run verdict pop-up fires AFTER Phase 11, so the verdict reflects both the text and visual audits. Any live CSS/content edits Phase 11 makes follow the standard live-write discipline: back up the file being changed first, apply the change, smoke-test the affected URLs plus the homepage, auto-revert from the backup if anything drops out of HTTP 200 or a new fatal appears in the error log, and log the change with its before/after.

**Parent's role after the scorecard returns:**

The parent reads the scorecard and applies fixes by acting on the recipe, NOT by re-deriving fix logic. If a recipe is unclear or the fix doesn't land cleanly after one attempt, escalate to the user rather than improvising — improvisation is how regressions slip in.

## Flags

| Flag | Default | Meaning |
|---|---|---|
| `<site>` (arg 1) | — | Singular mode: site slug / domain / natural-language name, fuzzy-resolved against the site registry |
| `--from <source-or-path>` | — | Knowledge-first source: a body of the operator's own expertise, or a path to their material; substance comes from here, research becomes positioning-only |
| `--research full\|positioning` | site default | Override the content-sourcing depth (positioning = light scan, substance from `--from`; full = SERP-derived) |
| `--no-gate` | false | Singular mode: skip the pre-publish review gate and publish live end-to-end (the old autonomous behavior) |
| `--project <slug>` | auto-detect | Which project's config to load (legacy; prefer the `<site>` arg, which resolves via the registry) |
| `--length N` | 2000 | Target word count |
| `--category X` | from config | WP category slug |
| `--author ID` | from config | WP user ID |
| `--variants "a,b"` | auto | Secondary keywords |
| `--skip-competitor` | false | Skip Phase 2 Firecrawl |
| `--dry-run` | false | Stop after Phase 4 |
| `--batch N` | — | Queue N posts sequentially |
| `--schedule daily\|weekly` | — | Cron cadence |
| `--autopilot` | false | Run the project's autopilot runbook unattended (batch + maintenance + scheduling) |
| `--schedule-publish` | false | Set each post to the CMS scheduled/future status at the project's publish window instead of publishing immediately |
| `--featured-entities "ID1,ID2"` | — | Only way to include hand-selected entities (per entity-mention rule) |
| `--review` | false | Add gate before Phase 8 publish |

**Autopilot.** `--autopilot` runs the project's autopilot runbook if the project config defines one: it batches generation, runs the corpus-maintenance pass (link integrity, interlink re-knit, cannibalization, ranking refresh), audits each post (Phase 10 + 11), and schedules survivors — fully unattended. In autopilot, every escalation becomes draft-plus-flag, never a blocking prompt, and a failed audit is never published or scheduled. `--schedule-publish` sets each post to the CMS's scheduled/future status at a project-configured publish window (the project config defines the window, timezone, and queue source) instead of publishing immediately; pair it with the CMS's native scheduler so posts drip out without a per-post run. All project specifics (cadence, window, timezone, keyword queue, runbook steps) live in the project config + runbook, never in this skill.

## Gate summary

**Autonomous mode (default): zero in-process gates.** Only one stop:
- After Phase 10 (text audit) + Phase 11 (visual QA): single end-of-run verdict pop-up (Works / Broken / One-more-tweak / Stop). Plus a focused `AskUserQuestion` mid-run if any unfixable escalation surfaces (cannibalization ≥30%, unsourced factual claim, image safety failure, slug collision, schema injection failure, theme-level layout defect Phase 11 can't safely auto-fix).

**Opt-in (additive flags):**
- `--review-outline` → pop-up after Phase 4 (3 H1 + outline + info-gain).
- `--review-images` → pop-up after Phase 7 (4 featured + 2 inline previews).
- `--review` → pop-up before Phase 8 publish.

## Error handling

- Phase 1-3 failure: stop, surface, ask user.
- Phase 5 draft failure (word count, info-gain): stop, ask user to adjust outline.
- Phase 6 audit failure: stop, do not publish.
- Phase 8 publish failure: attempt rollback (delete the created post) if the post was created but its meta failed, so a half-built post never sits live.

## Context loaded on invocation

- The operator's banned-words + banned-sentence-pattern list (forbidden words, em-dash ban), from wherever the house style guide lives.
- The site's `blog-pipeline-config.md` (every per-site fact the phases reference).
- The site's trackers: posts tracker, factual tracker, keyword queue, changelog.

## What this skill does NOT do

- Generate images when no provider is configured (flags instead).
- Measure post performance after publication (that is a separate ranking/traffic audit pass).
- Hand-select specific entities (requires `--featured-entities` flag).
- Social distribution.
- Factual verification beyond audit extraction (the operator resolves flagged claims).
