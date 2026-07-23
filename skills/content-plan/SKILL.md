---
name: content-plan
argument-hint: [site-slug] [source: keyword | skill <name> | research | blend | seed <id>]
description: Plan a blog content program for a registered site. Turn a broad keyword, or one or more skills, into a validated pillar-and-cluster map and a seeded keyword queue that the blog batch writes from. Each row carries volume, difficulty, search intent, a content format, secondary keywords, People Also Ask questions, SERP features, competitor entities, internal-link targets, and a priority score. Researches demand and SERP intelligence with your keyword and SERP tools, gates against cannibalization and competitor coverage gaps, and ranks by demand x winnability so a low-authority site builds the winnable posts first. Use when the user says /content-plan, "plan blog content for <site>", "build a content map", "turn this skill into blog posts", "what should we write for <site>", "seed the keyword queue", or wants a content or keyword plan before batching. Plans only: it never writes, publishes, or builds engine adapters. Writing a single post, running the batch that writes many, general SEO frameworks, and market research are each a separate step or skill, not this one.
---

## Content Plan skill

The strategy layer in front of the blog engine. That engine, whatever writes and publishes the posts downstream, works from a keyword queue but does no keyword strategy itself. This skill produces that queue: it researches demand and SERP intelligence, clusters by intent, removes cannibalization, checks competitor coverage, prioritizes, and emits the queue CSV the batch reads.

Plans only. It never writes posts, publishes, or builds platform adapters. The queue is the handoff to whatever writes the posts.

**Pipeline note.** The method assumes a downstream writing step that consumes the queue: a person writing from the CSV, an attended AI session per post, or an automated batch. Three things below are written against that step rather than against the strategy itself: the row status lifecycle (`idea` to `planned` to `scheduled` to `published`), the `template` component-parity tier, and the exclusion of playbook rows from any automated run. Substitute your own writing step for each, and leave a field blank when nothing downstream consumes it. The planning method, the gates, and the scoring stand on their own: the queue is worth producing even when the writing step is one person with a spreadsheet.

**Site record and standing defaults.** Two different sources feed this skill and keeping them apart matters. Site-operational values come from that site's OWN record, wherever it is kept: a multi-site registry file, one config file per site, or a single file for a one-site setup. Standing defaults that apply across every site (the demand-volume floor, and the sourcing default when a site's record has none) come from whatever standing-preferences file is in play. The six steps below are the universal content-strategy method and do not change either way. If neither file exists yet, run the method with the in-skill defaults stated at each step, and ask rather than assuming.

**Project and site context is loaded from the project's own instructions file and the site record.** Apply all planning to the specific site, audience, and goals.

SEO frameworks (cluster theory, cannibalization, topical authority), market and competitor research, and the writing of an individual post are each their own discipline. Where you carry a dedicated skill or process for one, that is where the depth belongs, and this skill calls on it rather than restating it.

## When invoked

Resolve two things before planning:

1. **The site.** An identifier for the site being planned, resolved against wherever the site records are kept. It resolves platform, paths, the voice and taxonomy config, the existing queue, and the site's default content sourcing mode. If no site is given or it does not resolve, ask which site.
2. **The source.** What the plan is built from (see Source modes). A `--from-seed <id>` flag sets the source to seed-first (promote an idea-board seed by id). Otherwise, if not stated, use the site's `content_sourcing_default`; if that is absent, use the standing default where one is set for that site; else ask.

Then run the six steps. Stop at the gate in step 6 for approval before seeding the queue.

## Source modes

Honor the site's default; allow a per-run override. The site record's `content_sourcing_default` stores one of three values: `research-first`, `knowledge-first`, or `blend`. `skill-first` is the run name for `knowledge-first`; `keyword-first` is a run-only mode and is never a stored default. If the default is absent, ask.

- **keyword-first:** one or a few broad seed keywords. Expand into the full demand space around them.
- **skill-first (knowledge-first):** mine one or more named skills' knowledge bases for angles (for example a tactical hacks skill or a framework skill). The substance is the operator's own material; research is demoted to a demand and winnability scan. Best for expertise and personal-brand sites.
- **research-first:** discover demand from SERP gaps and competitor coverage. Best for directory, local, and broad SEO sites.
- **blend:** the operator's material as the spine, research to fill the gaps.
- **seed-first (`--from-seed <id>`):** promote one idea-board seed into the plan. Read the seed by id from whatever idea backlog is kept (a board, a notes database, a file of captured angles); use its angle/summary as the keyword-first seed text and its board pillar as a clustering HINT only (a brand-theme taxonomy, NOT a site SEO `pillar_primary`, so never copy it verbatim). The seed supplies the angle; steps 3 to 5 still validate demand and winnability, so an unvalidated seed can still FOLD or drop. On emit, stamp the seed id into `seed_id`. Run-only, never a stored default. Where no idea backlog exists, seed-first is unavailable and the other four modes cover every case.

## The six steps

### 1. Resolve and load
From the site's record, resolve the operational fields: `dir`, `platform`, `queue_csv`, `config_md`, `content_sourcing_default`, `reference_posts` (the template tiers), and `status`. From the editorial config that record points at, load the editorial specifics: voice, taxonomy, templates, and the category set. Pull the existing published corpus and the current queue. Everything downstream dedups against these, so the plan never cannibalizes a live post.

### 2. Extract candidate angles
From the source, generate candidate post angles, then classify each on TWO orthogonal axes (below); do not collapse them into one tier.

**Mine the keyword tool for the idea universe (keyword-first, seed-first, blend).** Before clustering, expand the seed keyword (or a seed's angle text) through the keyword tool's research API (Semrush, Ahrefs, Moz, or whichever keyword tool is connected): pull related keywords, phrase-match variants, and the questions report, plus the SERP tool's People Also Ask and related searches. This is idea GENERATION, not the per-candidate validation in step 3; it surfaces sub-topics and angles the source alone would miss. Budget it (the keyword tool bills per returned row): one broad expansion per seed is usually enough. For skill-first the operator's KB is the spine and this is a supporting scan; for keyword-first / seed-first it is the primary idea source.

- **Role (topology):** the post's place in the hub-and-spoke graph. Drives internal linking and build order.
  - **Pillar (hub):** a broad head term that genuinely has children: multiple sub-queries each worth their own URL, and a page-one SERP that rewards a long multi-section guide. The has-children test: if a term's sub-topics would each be searched on their own, it is a pillar; if it would be one H2 inside a bigger page, it is a spoke.
  - **Cluster (spoke):** one specific intent that rolls up under a pillar. Platform-specific posts where the mechanism differs, single-tactic deep dives, audience or use-case cuts.
  - **Standalone:** has demand and unique content but no parent hub and no children. Do not force it into a cluster.
- **Format (content type):** what the post IS, read from the SERP (what ranks is the format the engine rewards) and from intent. One of: `playbook` (a comprehensive executable system, the flagship format a pillar usually takes), `how-to` (single-task steps), `comparison` (ranked options, best-of, X vs Y), `definition` (answer-box-led, single question), `opinion` (POV or take), `case-study` (worked example), `trend` (timely analysis). Role and format are independent: a spoke can be a how-to, a comparison, an opinion, or a definition.

**Demand-gate for opinion.** Opinion enters this queue only when it has search demand (then it is a row with `format=opinion`). A pure POV or timely take with no search demand does NOT belong here: park it back on the idea backlog instead of dropping it, through that backlog's own single writer, using its field mapping and its parked marker. Keep the seed as an idea (it only failed the SEARCH gate, not a rejection). Surface this at the step-6 gate ("parked N opinion angles to the board"), opt-in, never a silent mid-run write. Where no idea backlog exists, note the parked angles in the plan output instead. Do not fabricate demand to force it into the queue.

Expand, do not self-curate. Set a floor count tied to the source size. Fewer-but-unique is the wrong instinct at this step; the data gate in step 4 does the cutting.

### 3. Validate with data and pull SERP intelligence
For every candidate, pull the fields below. Batch calls to control cost. For large candidate sets (roughly 20+), fan the validation out across parallel subagents: split the candidates into batches, validate each batch concurrently, then merge.

**Demand and difficulty (keyword tool: Semrush, Ahrefs, Moz, or equivalent):**
- **Volume** and a true **difficulty** score. If no true difficulty is available, use a competition-index proxy and write it to `kd_proxy` (e.g. `Co 0.16`); leave `kd` blank. A blank `kd` then always means "no true score pulled yet", never "missing data". Re-pull a clean `kd` when the row is promoted to write.
- **Intent.** Most keyword tools classify each term natively as informational, commercial, transactional, or navigational. Take that native value into `intent`. If the tool has no intent field, infer intent from the SERP read below. Intent sets the `click_potential` band in step 5, so never assign `click_potential` from phrasing alone.

**Secondary keywords (merge from both tools into `secondary_keywords`):**
- From the keyword tool: related and phrase-match terms, plus the questions report.
- From the SERP tool: related searches and the People Also Ask box.
- Merge, dedupe against the primary, keep 8 to 12 that support the topic without competing for the same intent (same-intent near-synonyms would cannibalize as separate posts; fold those instead). This sub-step is mandatory: `secondary_keywords` is never emitted empty for a KEEP row.

**SERP read (a SERP API such as SerpApi or DataForSEO, or a manual read of the live results page), recorded per row:**
- **Winnability** bucket from page one: hard = mostly high-authority or high-DA publishers; medium = a mixed page one; easy = forums, UGC, thin or mid-authority sites dominate. Maps to the multiplier in step 5.
- **SERP features** present (featured snippet, People Also Ask, video, image pack, etc.) into `serp_features`. Most keyword tools also report per-keyword SERP features; use that where available and confirm against the live SERP. A row whose SERP shows a featured snippet is a snippet target: flag it so the writer opens with a 40 to 60 word direct answer.
- **People Also Ask** question strings into `paa_questions` (semicolon-separated). These are direct H2 and FAQ candidates, and the FAQ feeds the FAQPage schema on sites that emit it.
- **Entities:** the three tools, brands, or named concepts the page-one competitors cover, into `entities`. The writer must mention these or the post reads as thin to both search engines and AI answer engines.
- **SERP observation text** (who ranks, how locked the page is) into `serp_notes`. This is context for the writer. It does NOT go in `avoid_notes`; `avoid_notes` is reserved for cannibalization rules (step 4).

### 4. Cluster, cannibalization, and competitor gap
- Group the candidates by intent into the pillar and cluster map.
- Dedup in two passes:
  - **Candidate vs candidate:** a skill-level reasoning step over the angle list (title, intent, head-noun overlap). Collapse true duplicates here; no script does this.
  - **Candidate vs live corpus:** stage the candidates into the site's queue CSV as `idea`, then check each one against every published post whose topic looks close. The check is a SERP top-10 URL overlap: search the candidate's primary keyword and the live post's primary keyword, take the top ten result URLs for each, and compute the fraction they share. Band it: ABSORB at or above 0.50, DIFFERENTIATE 0.30 to 0.49, DISTINCT below 0.30. Get the live corpus from wherever the site actually publishes it: the CMS or its API, a content export, the site's own post-data file, or the sitemap. Reading the sitemap works on any platform and is the fallback that always exists. Script the overlap check when the volume justifies it, but the bands and the comparison ARE the method: never skip the check because no script is wired, because an unchecked corpus silently passes every candidate as DISTINCT, and cannibalization is the exact failure this gate exists to catch.
- **`avoid_notes` content (cannibalization rules only).** When a candidate conflicts with an existing or earlier-ordered post, `avoid_notes` records exactly three things: (1) the conflicting post (its `post_key` or slug), (2) the SERP URL-overlap band, (3) a one-sentence scope restriction for the writer (what this post owns, what it must not restate). On a greenfield site with no live corpus, `avoid_notes` is usually empty; that is correct. SERP difficulty observations never go here; they live in `serp_notes`.
- **Competitor semantic gap (top candidates by priority_score).** For the highest-priority KEEP rows, read the page-one ranking pages' section structure (SERP snippets, or a scrape of the top URLs) and list angles competitors cover that the planned post does not. Record the gap in `keyword-clusters.md` and feed any missing must-cover terms into `entities` or `paa_questions`. This is the difference between a post that matches the SERP and one that only matches the keyword.
- Apply the two-test gate to every angle. Volume floor: the standing default where one is set, else the site's own editorial config, else ask; overridable per run:
  - **Own demand?** Volume at or above the floor OR autocomplete and winnability show clear emerging demand.
  - **Own content?** It answers something no other post does, and the cannibalization band is DISTINCT or DIFFERENTIATE, not ABSORB.
  - Pass both = KEEP as its own post. Fail either = FOLD as a section inside the relevant pillar (an ABSORB band folds into the post it overlaps), no standalone URL. Record where each fold goes.

### 5. Prioritize
Compute `priority_score` for every KEEP row:

`priority_score = round( volume x (click_potential / 100) x winnability_multiplier )`

- `winnability_multiplier`: easy 1.0, medium 0.5, hard 0.1. A low-authority site should weight winnability hard; raise the multipliers toward 1.0 only once the domain can win competitive SERPs.
- `click_potential` (0 to 100), set from the SERP-confirmed `intent`, not from phrasing: transactional or commercial 80 to 100, comparison or best-of 60 to 80, informational how-to 40 to 60, definitional or answer-box-owned 10 to 30. If the SERP is informational while the phrasing looked commercial, the SERP wins.
- The effect: a high-volume but locked term ranks BELOW a winnable mid-volume one. For a low-authority site, winnability is the deciding axis, not raw volume.

Then set the structural fields:
- **Cluster density (build-order rule).** When two rows tie on `priority_score`, promote the one that deepens a cluster already started (an existing live post or an earlier-ordered planned row in the same cluster) above the one that opens a brand-new cluster. Topical depth per cluster compounds; isolated one-off posts do not earn authority.
- **`internal_links`.** Assign 2 to 3 link targets per KEEP row: slugs of existing posts or earlier-ordered planned rows in the same pillar or cluster. The parent pillar is always one target once it exists. The writing step wires these bidirectionally at write time, so this is the plan-time seed of the internal-link graph, not the whole graph.
- **`format` and role.** Set `format` per the step-2 axis (read from the SERP and intent). Role is expressed by the pillar/cluster map: a hub carries `cluster = "Pillar"`, a standalone `cluster = "Standalone"`, a spoke its cluster name. A pillar's `format` is usually `playbook`; spoke formats vary.
- **Playbook = operator-owned (gate).** A row with `format = playbook` is the operator's flagship content. It is never auto-written: it is excluded from any autonomous batch (whatever selects rows for that batch must drop it) and is produced only in an attended writing session where the operator shapes the angle and approves before publish. Surface every candidate playbook distinctly at the step-6 gate for explicit operator confirmation; the operator may also declare a playbook directly ("playbook about X") rather than waiting for the skill to propose one.
- Assign `pillar_primary`, `cluster`, `template`, `format`, `category`, and `write_order`. `template` values must match the site's own post-template tier keys as its record names them (a hub tier, a geo tier, a specialist tier, and so on); any downstream component-parity audit keys on them, so an invented tier key matches nothing and silently breaks that audit. Where the site defines no template set, leave `template` blank rather than inventing a tier. `template` is the component-parity tier (role-aligned) and `format` is the content type; they are different axes, so do not infer one from the other. `category` must be a value from the site's taxonomy in `config_md`. Build order: winnable spokes first; ship one anchor pillar early so clusters have an internal-link target; leave locked-head pillars last, as consolidation rather than near-term ranking plays.

### 6. Emit (gate first)
- Present the plan for approval: the pillar list, the KEEP table sorted by `priority_score`, the FOLD list with destinations, the recommended build order, the competitor-gap notes, and what was dropped or proxied. If any opinion angles were parked back to the idea board (step 2 demand-gate), list them here ("parked N to the board") so that board write is surfaced, not silent. Do NOT seed the queue before approval.
- On approval, write:
  - **The queue CSV** at the site's `queue_csv` path; if that field is unset, write it to the site `dir` as `keyword-final-writing-list.csv` and offer to record the path in the site's record. Use the 24-column schema below, in that exact order. New rows get status `idea` (or `planned` if the operator says go). Only `planned` rows feed the autonomous batch; downstream sets `scheduled`, then `published` or `merged`. When the run came from `--from-seed`, stamp the originating seed id into `seed_id` on every KEEP row it produced; blank otherwise. Stamp `campaign_id` on every KEEP row (default: the row's slug) as the lineage join key carried unchanged to the published post and its social drafts.
  - **A clusters map** at the site `dir` as `keyword-clusters.md`: pillars, clusters, folds, build order, and the per-cluster competitor-gap notes.
- Optionally set the site record's `queue_csv` path (if it was unset) and flip the site-level `status` (for example `onboarding` to `live`). The site record has no per-row queue-status field; row status lives only in the CSV.

## Output schema (queue CSV, 24 columns)

Exact column order. Every cell is plain text; quote any cell containing a comma. The SERP-intelligence columns (16-21) may be filled at plan time, or left for the row's promotion-to-write pass; the writing step reads each by name and tolerates an empty cell.

1. `write_order`: integer build order.
2. `status`: idea | planned | scheduled | published | merged.
3. `post_key`: short stable id (e.g. P1, L3).
4. `primary_keyword`: the focus keyword.
5. `volume`: monthly search volume.
6. `kd`: true keyword difficulty; blank only if no true score is pulled yet.
7. `kd_proxy`: competition-index proxy when `kd` is blank (e.g. `Co 0.16`); distinguishes "not yet scored" from "missing".
8. `click_potential`: 0 to 100, set from confirmed intent.
9. `intent`: informational | commercial | transactional | navigational.
10. `priority_score`: `round(volume x click_potential/100 x winnability_multiplier)`.
11. `template`: one of the site's own post-template tier keys (component-parity tier; role-aligned). Blank where the site defines no template set.
12. `format`: content type: playbook | how-to | comparison | definition | opinion | case-study | trend. Orthogonal to `template`. `playbook` is operator-owned (gated; never auto-written).
13. `pillar_primary`: the parent pillar.
14. `category`: one value from the site taxonomy.
15. `cluster`: the cluster name; `Pillar` marks a hub, `Standalone` a no-parent post.
16. `secondary_keywords`: 8 to 12 supporting terms, comma-separated; never empty for a KEEP row.
17. `paa_questions`: People Also Ask strings, semicolon-separated; H2 and FAQ candidates.
18. `serp_features`: featured_snippet | paa | video | image_pack | none (combine as needed).
19. `entities`: top 3 must-mention tools, brands, or concepts page-one covers.
20. `internal_links`: 2 to 3 slugs to interlink (parent pillar plus relevant siblings).
21. `serp_notes`: SERP observation context (who ranks, how locked). Not for conflict rules.
22. `avoid_notes`: cannibalization rules only: conflicting post + overlap band + one-line scope restriction. Empty when there is no conflict.
23. `seed_id`: provenance. The idea-board seed id this row was promoted from (`--from-seed`), else blank. Additive and optional; the writing step reads by name and tolerates empty.
24. `campaign_id`: the lineage join key threading this row across artifacts (idea seed, this queue row, the published post, its social drafts). Defaults to the row's slug; set once at plan time and carried downstream unchanged. Additive and optional.

## Guardrails
- Plan only for the queue and clusters map. Never write posts, publish, or build engine adapters. The one allowed side-write is parking a rejected opinion back to the idea backlog (step 2), through that backlog's own single writer, opt-in and surfaced at the step-6 gate, never silent.
- Validate-at-gate: present the map before seeding the queue (step 6).
- `secondary_keywords` is mandatory for every KEEP row; never emit it empty.
- `format` is mandatory for every KEEP row; set it from the SERP and intent, never blank.
- Playbook is operator-owned: a `format=playbook` row is gated (flagged for explicit operator confirmation at the step-6 gate) and is never auto-written by the batch (whatever selects batch rows excludes it). The operator may also declare a playbook directly.
- Opinion demand-gate: an opinion angle enters the queue only with real search demand (`format=opinion`); a no-demand POV is parked back to the idea board (step 2), not dropped.
- Any idea-board write goes through that board's single writer only; set board fields from the board's own option sets, never a raw site slug; keep the board pillar (brand-theme) separate from a site `pillar_primary` (SEO).
- Keep `serp_notes` and `avoid_notes` distinct: observation context vs cannibalization rules. Do not put SERP difficulty text in `avoid_notes`.
- Dedup against the live corpus and the existing queue, not just the candidate set.
- Difficulty integrity: label proxy values in `kd_proxy`, leave `kd` blank; re-pull a clean difficulty score on promotion.
- Intent integrity: set `click_potential` from the SERP-confirmed `intent`, not from keyword phrasing.
- Winnability overrides are allowed for emerging, on-brand, low-volume angles, but log them as overrides.
- Stay generic. Read the active site config; never hardcode a site, tool, currency, or geography.

## Default output format
1. **Plan summary:** N candidates becomes K keep + F fold, across P pillars. Source mode used. Data coverage (terms with a true difficulty score versus a proxy; rows with full SERP intelligence versus deferred to promotion).
2. **Pillars:** each with head term, volume, difficulty, intent, winnability, format, and the clusters under it. Mark playbook pillars as operator-owned (they need operator sign-off and are excluded from the autonomous batch).
3. **KEEP table** sorted by `priority_score` (columns match the queue schema).
4. **FOLD table:** angle, reason, destination.
5. **Competitor-gap notes:** per top cluster, the angles page-one covers that the planned posts must add.
6. **Build order:** numbered, with a one-line rationale each.
7. **Files written** (after approval): queue CSV path and clusters map path.
