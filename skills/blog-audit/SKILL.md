---
name: blog-audit
description: "AUDIT: did the blog pipeline's published posts hold up on the live site? Registry-scoped (sites with a blog-pipeline-config), not run-anywhere. Comprehensive audit of published blog posts on any CMS-backed project — the verification counterpart to generation (writing one post) and batch orchestration (running many). RE-VERIFIES every generation-time rule on the LIVE post (the full generation checklist 1-37 + the batch corpus/consistency/component/factual checks) AND adds the 2026 SEO/technical layer the pipeline cannot cover: indexability/canonical/robots, schema VALIDITY, image LCP/lazy/format/dims, broken-link + redirect sweep, OG/Twitter, soft-404, near-duplicate corpus detection, Core Web Vitals, GSC index-status + striking-distance + low-CTR, content decay. Plus the existing factual-tracker + ranking passes. Project-specific paths/rules/floors come from the active project's blog-pipeline-config.md."
user-invocable: true
argument-hint: [post-slug] [--project slug] [--deep] [--seo] [--cannibal] [--maintenance] [--claims-only] [--rankings-only] [--cluster-graph] [--gsc] [--psi] [--all] [--age-days N]
---

# /blog-audit skill

The verification counterpart to the generation pipeline. Generation and batch orchestration ENFORCE quality at write time; this audit RE-VERIFIES it on the LIVE published post (double-checking every rule actually held end-to-end) AND adds the SEO / technical / performance / indexability checks that can only be done post-publish or need live + field data.

Generic pipeline — all project paths, rules, editorial constraints, quality floors, tier reference posts, and the shortcode prefix come from the active project's `blog-pipeline-config.md`. Nothing project-specific is hardcoded here.

**Site config.** The per-SITE audit facts (paths, floors, reference posts) come from each site's own `blog-pipeline-config.md`, resolved from a site registry: one JSON file listing every site you audit, keyed by a short slug, holding that site's base URL, working directory, and config location. The method below is universal; site values come THROUGH the config. If a site has no config yet, build one from the fields listed under "Project config discovery" before auditing it.

Invoke as `/blog-audit` (triage), `/blog-audit <post-slug>` (one post, deep), or with a mode flag below.

## The two halves

1. **Inherit + double-check** (was it actually done right?). Re-apply, against the LIVE post:
   - The full end-of-run checklist your generation step enforces at write time (per-post checks 1-37, visual G1-G5, corpus C1-C6). If you keep no such checklist, the rules re-verified in `--deep` step 2 below ARE the substance of it: run them directly.
   - The batch/corpus layer: cross-corpus consistency (check 31), component parity (check 30), count trust-floor (14/34), factual gate, link-knit no-orphans.
2. **Add** the 2026 SEO best-practice layer the generation pipeline does NOT cover (it only exists post-publish or needs live/field data): indexability + canonical + robots, schema *validity* (not just presence), image LCP/lazy/format/dims/alt, broken-link + redirect-chain sweep, OG/Twitter cards, soft-404, near-duplicate detection across the corpus, Core Web Vitals (field), GSC index-status + striking-distance + low-CTR + decay.

## 2026 alerts (baked into the checks)

- **FAQ rich results were retired by Google** (no display May 2026; Rich Results Test + GSC support removed mid-2026). FAQPage markup is checked for **validity only** and reported as INFO — never a rich-result "win", never a FAIL. Keep the markup: it is still valid Schema.org and feeds AI Overviews / LLM parsing.
- **LCP "good" threshold tightened to 2.0s** (March 2026 core update; was 2.5s). The featured/hero image must be **eager** (not `loading="lazy"`), ideally `fetchpriority="high"`. Any CWV check hard-coded at 2.5s under-reports.

## Project config discovery

Same pattern the generation step uses:
1. Detect the active project from whatever tells you which site is in scope OR `--project <slug>`.
2. Load `blog-pipeline-config.md` from that project's working folder.
3. Abort with a template pointer if config is missing.

Pull from config: shortcode prefix, tier reference posts (the parity benchmarks), entity-mention rule + quality floors, YMYL/medical track, canonical authorities, currency/geography, internal-link indexability rule, count-token convention, author/reviewer IDs, factual + posts tracker paths.

## Data sources (paths from config / registry)

- `{config.factual_tracker_path}` — pending factual claims (appended at generation time when a post makes a checkable claim).
- `{config.posts_tracker_path}` — published posts with last-checked + position.
- `{config.seo_pages_catalog}` — indexable internal-link targets.
- `{site.dir}/link-knit-ledger.json` — inbound-link state (note: undercounts; the live count is truth).
- The site registry — one JSON file listing every site by slug, so every check below can be pointed at a site with `--site <slug>`.

## Run modes

### Default (no args) — triage
1. Parse factual-tracker: list `pending` claims; surface any Open + High-severity (the factual gate's blocking set).
2. Parse posts-tracker: posts last-checked ≥ 60 days (or `--age-days N`).
3. Run the corpus health snapshot + the consistency sweep + the cannibalization snapshot (cache-only, zero API) read-only and summarize. All three are specified under `--maintenance` below.
4. Summarize: "N claims pending, M posts due for re-audit, K corpus findings, J consistency WARNs, P cannibalization FAILs." Then `AskUserQuestion`: Deep per-post / SEO-only / Maintenance / Cannibalization / Claims / Rankings / Cluster-graph.

### `--deep <slug>` or `--deep --all` — comprehensive per-post re-audit (THE core mode)
The full inherit-and-verify pass on a live post. Run in order; assemble one scorecard:

1. **Technical / SEO scorecard (deterministic, no API keys):**

   Write this as a real script and run it, rather than eyeballing the page: fetch the live URL, parse the HTML and the JSON-LD, and follow every link. Hand-checking does not scale past one post and silently drifts. It takes the site slug, one post slug or all posts, the shortcode prefix from config, the primary keyword, and a link-sweep cap (80 is a sane default); have it emit JSON so runs are diffable.

   ~25 checks against the live page, body-scoped to the rendered post body only (the CMS's main content region, no header/footer/popover/nav chrome): HTTP + breakage, robots header + meta (noindex leak), self-referencing canonical, `<html lang>` + viewport, single-H1 + heading-hierarchy, title + meta-description length, primary-keyword placement (H1 + first-150 + ≥1 H2), JSON-LD parses + Article required-props (author/datePublished/image) + BreadcrumbList present + FAQPage validity-only + no duplicate Article node, content-image alt + dims (CLS) + below-fold-lazy + featured-image-eager (LCP) + WebP/AVIF format, broken internal+external link sweep + redirect chains + bot-block tolerance + anchor quality, unrendered-shortcode leak, OG completeness + og:image resolves + Twitter card, sitemap inclusion.

2. **Inherited generation-checklist re-verification (the rules the technical scorecard doesn't cover):** re-apply your generation-time checklist to the LIVE post, using a dedicated verification pass plus scripted checks:
   - Forbidden words + banned sentence patterns across ALL 9 authored fields (checks 20/21): pull each rendered field and scan it against your own banned-word list and banned-sentence-pattern list; em/en-dashes too.
   - Keyword density + per-paragraph cap (22) and each secondary 1-5x across H2s (23).
   - Canonical-entity coverage ≥1x each (26) and intent alignment (tone/CTA-density/title-pattern/FAQ-skew vs `intent_lock.label`) (25).
   - Style fingerprint (27): compare the post's style signature against your house baseline and flag drift.
   - Featured-entity quality floor (28): every recommended entity clears the config rating AND review-count AND non-placeholder-image floor.
   - Count trust-floor + scope-match (14/34): every count token renders ≥ floor, no bare 0, scope-correct (single-axis vs compound `loc=`), no raw token leak.
   - Source rows: every URL HEAD-200 (17), deep-linked where the citation supports it (18), and `Article.citation` URLs match the rendered sources block (19).
   - Component parity (30): render the post AND its tier's canonical reference (from config); grep every theme marker + schema string; return the full parity matrix. Missing component = flag with the tier's required-component list.
   - Category single-best-fit + tags complete/correct (32).

3. **Editorial-rule re-checks (from config):** entity-mention compliance (no hand-named entities outside an allowed round-up; quality floor honored); YMYL/medical track — required disclaimer rendered, `Article.reviewedBy` emitted, reviewer truthfully scoped and ≠ author, dedicated category; canonical-authority citation present and correctly framed; count-token convention (DB numbers via shortcodes, no hardcoded numbers).

4. **Cluster consistency for this post:** run the consistency sweep scoped to this post's cluster (its primary tag) — disjoint-band price enclosure, licensing framing, banned words, count-token drift vs same-cluster siblings.

5. **Optional API layers:** `--gsc` and/or `--psi` (below).

**Output:** a per-post scorecard grouped by category (INDEXABILITY / ON-PAGE / SCHEMA / IMAGES / LINKS / CONTENT / EDITORIAL / CONSISTENCY / [GSC] / [CWV]) with PASS / REVIEW / FAIL per group + a prioritized fix list (P0 first). For `--all`, a corpus roll-up (clean / review / fail counts + the worst offenders). Apply approved fixes via the Update mechanics; every live edit follows the live-write protocol below (backup → edit → smoke test → CDN purge → verify).

### `--seo <slug>` or `--seo --all` — fast technical/SEO hygiene
Just step 1 above (the technical scorecard). The cheap, no-API pass for "is anything technically broken on the live page(s)."

### `--cannibal [--all]` — keyword/intent cannibalization (SERP-overlap)
Catches the gap the near-duplicate sweep misses: two posts with DIFFERENT text competing for the SAME query (modifier splits like "X" vs "X cost", or same-intent siblings). The authoritative signal is Google top-10 organic SERP overlap, pulled from a SERP data provider (SerpApi, DataForSEO, Serper, or any API returning top-10 organic URLs for a keyword), not text similarity.

Run it as a script, per site, with: a mode selector (all posts / one post / named clusters), a `--gate-only` zero-API cost preview and a `--no-serp` cache-only pass, a `--max-searches` hard cap (default 300), and JSON output.
- **Bands** (overlap coefficient = shared / min on top-10 organic URLs): **≥0.50 ABSORB** (FAIL — merge/canonical/redirect; one canonical should own the query), **0.30-0.49 DIFFERENTIATE** (WARN — keep both, deliberately differentiate / add an `avoid_note`), **<0.30 DISTINCT** (OK). Hub→own-spoke, cross-vertical geo (same area / different service), and SERP-confirmed informational-vs-commercial splits are SUPPRESSED (logged with reason, never flagged). Scheduled-vs-live FAILs are tagged so a draft can be fixed before it drips.
- **Always run `--gate-only` first** (token gate + FP suppression, ZERO API) for the cost preview; the 30-day per-keyword SERP cache makes re-runs ~$0. Hard-capped at `--max-searches` (default 300); spends highest-volume pairs first, marks the rest `DEFERRED`.
- **Records** every pair to `<site.dir>/cannibalization/latest.csv` (triage snapshot, sorted FAIL-first; a `recommended_action` names the lower→higher-volume merge direction) + `history.csv` (append-only; `delta_state` = NEW / WORSENING / IMPROVING / RESOLVED / UNCHANGED, so risk is comparable across runs; a pair whose post leaves the corpus auto-marks RESOLVED). The tool is READ-ONLY on the site AND the register — it writes only its own CSVs + SERP cache. Act on a FAIL manually: apply the merge/canonical/redirect via the Update mechanics protocol below, or add the `avoid_note` to the register by hand.
- Reusable at generation time: a ">30% cannibalization with an adjacent post" pre-publish check calls `--pair "<a>,<b>"` for the one new keyword vs same-cluster siblings (same engine + thresholds), reusing the cache.

### `--maintenance` — corpus pass (post-batching backstop)
The supervised home for the cross-corpus maintenance a batch run would otherwise do per batch, decoupled from generation. Run once after the drip queue drains, then monthly.
1. **Link-knit orphan sweep:** knit inbound links to under-linked live posts (re-process posts whose LIVE inbound count is below floor, using the live count not the ledger), capped at `--max-insertions <N>`. If the site has a publish-hook that auto-links on the publish transition, future drips self-knit; this is the backlog handler + backstop. Always offer a `--dry-run` preview.
2. **Consistency sweep:** across the corpus — detector only; surface each WARN for an approved live fix.
3. **Corpus health:** archive link-graph, pagination canonical, taxonomy-token resolution, sitemap freshness. A FAIL is a directory/platform regression.
4. **Factual-gate held posts:** list posts the scheduler holds (Open + High-severity claim in `factual-tracker.md`); surface claim + fix so they can be verified and scheduled.
5. **Cannibalization sweep:** SERP-overlap keyword/intent cannibalization the near-duplicate sweep can't see; the 30-day cache makes the monthly re-run near-free. Review FAIL (ABSORB) pairs for merge/canonical, WARN (DIFFERENTIATE) pairs for an `avoid_note`. `--gate-only` first for the cost preview.

### `--gsc` — Search Console layer (optional, API-gated; highest ROI)
Needs Google Search Console API credentials configured for the property. If absent, the skill says so and SKIPS this layer (never fails the run). When available, per audited URL:
- **Index status** (`urlInspection.index.inspect`): flag any verdict that is not "Submitted and indexed" (Crawled-not-indexed / Discovered-not-indexed / Excluded). Published ≠ indexed is the single highest-leverage blind spot.
- **Google-chosen vs declared canonical** mismatch (`userCanonical` vs `googleCanonical`).
- **Striking-distance queries** (avg position 5-20 with impressions) — the highest-ROI optimisation targets.
- **High-impression / low-CTR** (title-CTR problem → rewrite title/meta).
- **Coverage / enhancement errors**; **click/impression decay** (last-28 vs prior-28 negative slope).

### `--psi` — PageSpeed Insights / Core Web Vitals (optional, API-gated)
Needs a PSI API key. Per URL: field CWV at p75 against 2026 thresholds (**LCP < 2.0s**, INP < 200ms, CLS < 0.1) + top lab opportunities (render-blocking shortcode CSS/JS, unused CSS) + CDN cache-HIT on the post HTML (Cloudflare, Fastly, or whatever fronts the site). Degrade gracefully if no key.

### `--claims-only` / `--rankings-only` / `--cluster-graph` / post-by-post
Existing focused passes (see below). `post-by-post` = `--deep` on one post with the operator stepping through fixes.

## The full check matrix (what "comprehensive" covers)

Grouped reference. **Inherited** = re-verified from the generation checklist; **New** = added by this skill. Mode: `seo`=post audit, `deep`=full per-post, `maint`=corpus, `gsc`/`psi`=API.

| Group | Checks | Source | Mode | Tool |
|---|---|---|---|---|
| Indexability & canonical | HTTP/breakage, robots header+meta noindex, self-canonical, Google-chosen canonical, soft-404, trailing-slash/www consistency, sitemap inclusion | New (+1,2,29 inherited) | seo, gsc | post audit, GSC |
| On-page SEO | single-H1 + hierarchy, title+meta length, primary-kw placement, title≠H1, meta-desc uniqueness | New (+3,4 inherited) | seo, deep | post audit |
| Structured data | JSON-LD validity, Article required props, BreadcrumbList, FAQ validity-only, no duplicate type, @id/sameAs entity linking | New (+9,10,19 inherited) | seo, deep | post audit + validator |
| Images | alt, width+height (CLS), featured eager (LCP), below-fold lazy, WebP/AVIF, og:image resolves | New (+11,12 inherited) | seo, deep | post audit |
| Links | broken internal+external, redirect chains, anchor quality, indexable targets, inbound no-orphans, in-content inbound count | New (+15,16,17,18 inherited) | seo, deep, maint | post audit, link-knit |
| Content quality | forbidden words/em-dash (9 fields), keyword density, secondary distribution, canonical entities, style fingerprint, intent, near-duplicate corpus, word-count vs SERP, decay | Inherited 20-27 + New | deep, gsc | audit-checklist scripts, n-gram similarity, GSC |
| Consistency (corpus) | price enclosure, licensing, count-token drift, cluster reads as one | Inherited 31 + sweep | deep, maint | consistency sweep |
| Cannibalization | SERP top-10 overlap (keyword/intent competition across DIFFERENT text), split-degradation over runs, own-domain equity split | New | cannibal, maint | cannibalization audit |
| Component parity | full component + schema set vs tier reference | Inherited 30 | deep | render + grep both |
| Editorial / compliance | entity-mention + quality floor, YMYL disclaimer + reviewedBy + reviewer≠author, category/tags, count-token convention | Inherited 28,32 + config | deep | wp-cli + config |
| Corpus health | archive link-graph, pagination canonical, taxonomy tokens, sitemap freshness | Inherited C1-C6 | maint | corpus audit |
| Performance / CWV | field LCP(<2.0s)/INP/CLS, lab opportunities, CF cache HIT, TTFB | New | psi | PSI API |
| Social | OG complete + image + twitter card | New | seo, deep | post audit |
| E-E-A-T | author entity + bio + sameAs, first-hand markers, outbound authority citations | New | deep | parse + agent |
| Rankings & GSC | index status, striking-distance, low-CTR, coverage errors, decay | New | gsc | GSC API |

## Tooling backbone

Build these as five reusable scripts, all registry-driven and taking `--site <slug>`, so every mode above is one command and results are diffable run to run:

- **Post audit** — deterministic per-post live technical/SEO scorecard (no API keys). The workhorse.
- **Corpus audit**, **consistency sweep**, **link-knit**, **cannibalization audit** — corpus / cross-post / link-graph / SERP-overlap cannibalization (the cannibalization one is SERP-cached + cost-capped and writes its own history/latest spreadsheet).
- A verification pass + your generation checklist + text-analysis helpers (banned-pattern scan, style fingerprint, n-gram similarity) — the inherited per-post checklist + near-duplicate.
- Optional API layers: Google Search Console API (`--gsc`), PageSpeed Insights API (`--psi`). Opt-in; the skill degrades gracefully and says so when creds are absent.
- Near-duplicate corpus sweep (directory-site P0): pairwise 5-gram Jaccard similarity within each cluster catches DUPLICATE TEXT (pairs > ~0.8). KEYWORD/INTENT cannibalization across DIFFERENT text (the harder, more common case) is covered separately by the cannibalization audit (`--cannibal`) via SERP top-10 overlap — the two are complementary, not redundant.

## Update mechanics

For a fix applied during the audit, every live write follows this protocol. The commands below are the WordPress form; on another CMS substitute its equivalent read and update call (its API, CLI, or admin endpoint) and keep the five steps and their order exactly as they are — the order is what makes the write reversible.
1. Pull current content (`wp post get <id> --field=post_content` or REST).
2. Targeted exact-string replacement (or shortcode-invocation fix); back up off-webroot first.
3. Update via `wp post update` / REST; re-assert `post_status=publish` (legacy bug guard).
4. Cache flush + CDN purge per config.
5. Smoke test the live URL (HTTP + breakage + error-log delta) as a separate verification pass, then changelog entry.

For content refreshes: re-run the generation research phases for the keyword (fresh SERP gap), propose edits via an interactive question, apply approved, the modified timestamp auto-touches, submit to the GSC Indexing API if configured.

**Quotation exemption:** before "fixing" a forbidden-word / em-dash hit, confirm it is not inside a quoted testimonial/source — verbatim third-party text is exempt from your style rules; surface the conflict instead of silently rewriting.

## Cluster link-graph audit (`--cluster-graph`)

Corpus-level orphan + weak-cluster detection across all published posts (complements the per-post no-orphans rule). Builds the internal-link adjacency graph, flags hard orphans (in-degree 0), one-way pairs, and weak topical clusters (share ≥2 tags, not linked); proposes edge additions. The actual inbound-link INSERTION is done by `link-knit` (the `--maintenance` step); this mode is the analysis/surfacing layer. Run after the corpus crosses ~10 posts.

## Tracker formats (standardized)

### factual-tracker.md
`| date | post-slug | claim | source | confidence | status | verified-by |` — statuses: `pending`, `verified`, `wrong`, `updated`, `skipped`. The scheduler's factual gate blocks any `## <slug> (post <ID>)` block with `Status: Open ... Severity: High` on one line.

### posts-tracker.md
`| post-id | url | keyword | published | last-checked | position | status |` — statuses: `new`, `rising`, `flat`, `dropped`, `refreshed`, `deprecated`.

## Claims-only pass
Group `pending` claims by post; surface 5 at a time via `AskUserQuestion` (claim + source + confidence; Correct / Wrong+correction / Needs-research / Skip). On Wrong: apply correction via Update mechanics; mark `verified`/`corrected`; re-check the live page to confirm.

## Rankings-only pass
Per stale post: fetch current position (GSC API if configured, else paste from dashboard) for target keyword + 2 variants. Classify Rising / Flat / Dropped (>2 lost → refresh: re-run the generation research phases, propose update) / Never-ranked (>16wk, pos>20 → deprecate or rewrite). Update posts-tracker.

## Cadence

- **Per-post `--deep`** at publish/drip time for a spot-check, or on any post you suspect.
- **`--seo --all`** monthly (fast hygiene; catches dead links as the directory rots).
- **`--maintenance`** once after the drip queue drains, then monthly.
- **`--gsc`** monthly once configured (turns the audit into ranking gains, not just hygiene).
- Optionally put the monthly passes on a scheduler so they run unattended.

## Load before running
- Your editorial / writing-style rules (they still apply to any edit made during the audit).
- Your generation-time per-post checklist (the inherited checks re-verified above).
- Whatever project-specific context tells you which site is in scope and what its rules are.

## What this skill does NOT do
- Generate new posts (that is the generation step's job, not this one's).
- Bulk delete posts.
- Override the entity-mention rule or any config quality floor when editing.
- Auto-fix live posts without surfacing the change (every live edit is approved + follows the Update mechanics protocol above); the only autonomous live writes are the `--maintenance` link-knit sweep (snapshot+verify+revert) and the publish-hook, both with built-in safety.
