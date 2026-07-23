# /blog-post end-of-run audit checklist

Single source of truth for the Phase 10 audit. Whoever runs the audit (a delegated sub-agent, or the main thread inline) loads this file at run-time. SKILL.md references this file rather than duplicating the rules.

When this checklist changes, every future `/blog-post` invocation inherits the change automatically. Keep a dated version note at the bottom when materially editing, so a check's origin stays traceable.

**Selectors and field names are site-specific.** Many checks below grep for a marker in the rendered HTML (a byline wrapper, a takeaways aside, a sources block, a table-of-contents list) or read a named meta field. Those names belong to YOUR theme and YOUR SEO plugin, not to this checklist. Record them once in the site's `blog-pipeline-config.md` under a `selectors` and a `meta_fields` section, and read them from there. Where a check below writes a marker like `<byline-marker>`, substitute your recorded selector. A check that greps a selector your theme does not use passes vacuously and hides a real defect.

---

## How to run

1. The auditor reads this file.
2. For each row, runs the test, records PASS / FAIL with evidence.
3. Buckets fails into FIXABLE (per the row's fix recipe) vs ESCALATE.
4. Returns the scorecard (template at the bottom) to the caller.
5. The caller applies all FIXABLE auto-fixes, re-runs the audit on impacted checks, then surfaces a single end-of-run verdict pop-up to the operator.

Inputs the auditor needs from the caller:
- `post_id` + `url`
- `primary_keyword`
- `secondary_keywords[]` (parsed from the keyword queue row)
- `template` (which content-template tier this post is)
- `sibling_urls[]` (adjacent published posts in the same project for cannibalization check)
- The site's access method + CMS root path
- Project config path (for shortcode prefix, selectors, meta field names, taxonomy term inventory, banned-words list)

### Rendering a not-yet-public post (draft / scheduled / future) — "deferred" is NOT a pass

Render-dependent checks (5–12, 14, 19, 30, G1–G5, all schema checks) need the REAL theme-rendered page. A draft or scheduled post is NOT publicly fetchable, and a CMS admin Preview of a scheduled post commonly renders only the body, NOT the theme-native asides (byline, takeaways, reviewer, sources). So a render-dependent check that is skipped because the post is not yet public is an OPEN check, never a clean one. **Reporting "deferred" as a pass is the single most common way this whole audit gets silently defeated: do not do it.** Either render the post by the method below, or escalate the check as unverified — never mark it green.

The most reliable render method for a not-yet-public post is an atomic publish-fetch-revert (template-rendering harnesses run from the CLI give false positives AND false negatives; an admin-preview loopback usually fails on auth). The shape, in the idiom of a CLI-driven self-hosted CMS:

```
<remote-shell> '<cd to CMS root> && \
  ORIG=$(<read the post publish date>) && \
  <set status to published, with a PAST date> >/dev/null && <flush cache> >/dev/null && \
  <fetch the now-public URL server-side; grep components + schema> && \
  <restore the original status and the exact original date> >/dev/null && <flush cache> >/dev/null && \
  echo "restored: $(<read status>) $(<read date>)"'
```

Rules: (a) flip → fetch → revert MUST be ONE command so the post can never be left publicly visible if a step errors midway; (b) use a PAST publish date for the flip (many CMSs coerce a published post back to scheduled when its date is in the future); (c) restore the EXACT original date + status and verify the restore, do not assume it; (d) detect schema by case-insensitive substring search for `"FAQPage"` / `"Article"` / `"BreadcrumbList"` rather than a strict `ld+json">` regex — SEO plugins commonly add their own attributes to the script tag, and a strict regex then matches zero blocks and reports every schema as missing. Lowest-risk alternative for a scheduled post: run the render-dependent checks against the real public URL the day AFTER it auto-publishes (post-publish gate, zero flip).

---

## Sections

- **A.** Server health (checks 1–2)
- **B.** Content + structure (checks 3–13, 25, 32, 37)
- **B2.** Component parity vs canonical reference (check 30)
- **C.** SEO + schema (checks 14–19)
- **C2.** Sitemap (check 29)
- **D.** Editorial quality (checks 20–23, 27)
- **D2.** Featured-entity quality floor (check 28)
- **E.** Cannibalization (check 24)
- **F.** Topical completeness (check 26)
- **G.** Visual QA (checks G1–G5, Phase 11 main-thread)

---

## A. Server health

| # | Check | How to test | Pass criteria | Fixable | Fix recipe |
|---|---|---|---|---|---|
| 1 | HTTP 200 + response time <3s on new URL + homepage + 1 sibling post | `curl -s -o /dev/null -w "%{http_code} %{time_total}"` for each | All three return 200 in <3s | Server-level | If fail: escalate to user with diagnostic. Re-test after cache flush + CF purge before declaring fail. |
| 2 | No breakage strings in rendered HTML of new URL | `grep -ciE "Fatal error\|Parse error\|There has been a critical error\|database error\|500 Internal\|Warning:"` on fetched HTML | 0 hits | Server-level | If fail: read error log, identify cause, escalate or fix the underlying issue. Page-level breakage indicates a Red-risk regression. |

## B. Content + structure

| # | Check | How to test | Pass criteria | Fixable | Fix recipe |
|---|---|---|---|---|---|
| 3 | Title and H1 present | grep `<title>` + `<h1>` in rendered HTML | Both non-empty | Y | If empty: read post via wp eval, set `post_title` and confirm theme renders H1 from it. |
| 4 | Meta description set + within pixel-width window | Read the SEO description meta (the config's `seo_description_field`). Compute Arial 13px pixel width (target 700–920px, char floor ≤150) | In window | Y | Generate 3 in-range variants via LLM; pick the one with the closest match to the post's intent; update the SEO description meta. |
| 5 | Native byline + author popover renders | grep the site's byline marker + author-popover marker (from the config `selectors` section) in the HTML | Both present | Y | If missing: confirm `post_author` is set and theme template-part is current; refresh cache. |
| 6 | Takeaways aside renders 4–6 LIs | grep the site's takeaways-aside marker and count `<li>` inside it | 4–6 items rendered | Y | If 0: the `key_takeaways` structured field is not set; populate it via the platform's field-write call. If <4 or >6: trim/expand takeaways to fit window. |
| 7 | Sources section renders + own-source first + Show More toggle | grep the site's sources-block marker; check the first `<li>` matches the own-domain pattern; check the show-more toggle element | All three present | Y | Reorder the `sources` field array if the own-source row is not at index 0. Add Show More toggle requires theme-level (escalate). |
| 8 | TOC scroll-spy markup present (desktop only) | grep the site's table-of-contents marker in the HTML | Present | Y | If missing: confirm theme template-part is current; H2/H3 hierarchy clean (no skipped levels). |
| 9 | FAQPage schema emitted | parse JSON-LD blocks; look for `"@type": "FAQPage"` | Present with `mainEntity` array of length ≥4 | Y | If missing: confirm `[<prefix>_faq]` shortcode is in body. |
| 10 | Article schema enriched with `citation` + `about` | parse JSON-LD; check `Article`/`BlogPosting` node has both fields | Both present, citation array length matches sources | Y | If missing: the `sources` field may be empty (populate it); or the primary tag may be missing (set it via the platform's taxonomy call). |
| 11 | Featured image rendered, attached, alt text follows pattern | check `_thumbnail_id` + `og:image` + alt attribute on hero img | All present; alt = `<primary kw>: <one-sentence scene>` | Y | If alt is wrong: update via wp eval `update_post_meta` on the attachment's `_wp_attachment_image_alt`. If thumbnail missing: re-import + set `_thumbnail_id`. |
| 12 | 2–3 inline images present after the right H2s, alt text follows pattern | grep `<img>` tags inside `<article>`; locate position relative to H2 anchors | Min 2, max 3 inlines, alt = descriptive scene + secondary kw or context word | Y | If positioned wrong: rewrite body HTML to move `<figure>` block. If alt off-pattern: rewrite alt. |
| 13 | No unprocessed `[<prefix>_*]` shortcode strings in HTML | grep raw `\[(<prefix>)_` in rendered HTML | 0 hits | N | If hit: shortcode prefix mismatch OR shortcode not registered; escalate (theme/plugin issue). |
| 37 | Every inline body `<img src>` resolves (own-host upload URLs carry the date-based subfolder, no bare path) | List all own-host upload `src`s in the body and confirm each carries a `/YYYY/MM/` segment: `grep -oiE 'src="https?://<own-host>[^"]*/wp-content/uploads/[^"]+"' rendered.html \| grep -vcE '/uploads/[0-9]{4}/[0-9]{2}/'` | 0 (every inline upload URL contains `/uploads/YYYY/MM/`; a bare `/wp-content/uploads/<file>` path 404s and the image fails to render) | Y | Resolve each offending image's real URL via `wp_get_attachment_url(<attachment_id>)` and replace the hand-built path in the body `<img src>`. Root cause is a body `src` built by hand from the filename instead of read from the CMS — fix it at source per SKILL.md Phase 7b + Phase 8 step 1 and the project config's "Body `<img src>` = resolved attachment URL" rule, not just here. The featured image is out of scope (it renders from `_thumbnail_id` via `wp_get_attachment_image()`, not a body `src`). |
| 25 | Intent-aligned tone, CTA density, title pattern match the locked `intent_lock.label` | Read `intent_lock.label` from Phase 4 plan output. Count CTAs in body (`[<prefix>_cta_filter]` shortcodes + explicit "Book"/"Browse"/"Get started" anchors). Check H1 against the per-intent title pattern table in SKILL.md Phase 4. Check FAQ skew (definition vs comparison vs pricing focus). | All four match the row for `intent_lock.label`: CTA count within window, H1 follows pattern, FAQ skew matches, tone matches (no editorial-listicle voice on informational posts). | Y | If CTA count off: add or remove a `[<prefix>_cta_filter]` per intent table. If H1 pattern off: regenerate via Phase 4 with intent locked (one of the 3 H1 candidates usually fits the pattern). If FAQ skew off: rewrite 2-3 FAQ rows to match (e.g. swap a "How much does X cost" question for "What is X" on informational posts). If tone off: structural rewrite, escalate. |
| 32 | Category is the single best-fit PREDEFINED category + tags are complete and correct | Read the post's category + tags. **Category:** confirm it is the most-appropriate category from the project's PREDEFINED map for the post's intent/template, never a blind default, never a new category. **Tags:** confirm at least 1 primary service/topic tag PLUS every genuinely-relevant secondary tag. | Category follows the project config's category rule: if the config defines a topic/service-hub axis, the category is the single best-fit hub for the post's TOPIC (one per post, derived by topic not by format); otherwise the content-type mapping below applies, where the round-up category is used ONLY on ranking/round-up posts (T2 Best-of) and informational posts use `guides` (or `tips`/`reviews`/`trends`). Tags: primary present + all relevant secondaries; geography tag present on every area-scoped post; no forced or irrelevant tag. | Y (autonomous, no user question) | **Wrong category:** re-assign to the best predefined match via `wp post term set <id> category <slug>`; NEVER create a new category. **Tags:** add the primary + relevant secondaries via `wp post term set <id> post_tag <slugs...>`; geography tags only for area-scoped posts; for a clearly-relevant tag that does not exist, CREATE a sensible one (tags are flexible) rather than asking, but reuse existing tags first and never proliferate near-duplicates. |

**Intent → category mapping (a DEFAULT content-type axis; a project's config may override the slugs OR replace this axis entirely with a topic/service-hub axis — if the config defines its own category rule, follow the config; this mapping is only the fallback when the config is silent):** The round-up category = the post's PRIMARY job is ranking or curating "the best" (T2 Best-of, "Best/Top X in {Geo}" titles). `guides` = informational/educational, which is most posts (T1 Hub umbrella, T3 Geo "what to book" guides, T4 Pricing, T5 Specialist complete-guides) even when they contain a few editor picks. `tips` = pure how-to/advice. `reviews` = single-entity review. `trends` = trend piece. Pick ONE; the round-up category is special, not the default.

## B2. Component parity vs canonical reference (render-verified)

This is the consolidated gate that catches "a post is missing a component the rest of the corpus has." It runs on the REAL rendered page (use the publish-fetch-revert protocol above for not-yet-public posts). It does NOT replace checks 5–12; it is the single diff-against-reference that makes silent drift impossible.

| # | Check | How to test | Pass criteria | Fixable | Fix recipe |
|---|---|---|---|---|---|
| 30 | New post's rendered component + schema set matches the canonical reference for its template tier | Render the new post AND the canonical reference post for its template tier (nominate one known-good published post per tier ONCE and record it in the project config; every later post in that tier diffs against it). On BOTH, case-insensitively grep every theme-native marker from the config `selectors` list: the byline marker, `Written by`, the reviewer line, the takeaways-aside marker + its heading, the sources-block marker + its heading, the author-popover marker, the table-of-contents marker, `min read`, the FAQ accordion, the breadcrumb marker, the related-content row. And every schema string: `"FAQPage"`, `"Article"` (or `BlogPosting`), `"BreadcrumbList"`, `citation`, `"about"`. | Every marker present on the reference is ALSO present on the new post. Zero components the reference has are missing on the new post. | Y | A missing component means its driving input is unset: set the structured field (`reviewer` -> reviewer byline; `key_takeaways` -> takeaways aside; `sources` -> sources section + `citation`), set the primary tag (-> schema `about`), add the FAQ shortcode (-> FAQPage), or set the featured image. Re-render and re-diff. **The scorecard MUST return the full parity matrix (each component × {reference present?, new-post present?}) — a prose summary of counts is not acceptable and a prose summary is exactly how a missing component ships unnoticed.** **If a component the reference has is INTENTIONALLY omitted on this post for a valid reason (e.g. no FAQ on a thin glossary post, no listing block on a sensitivity-omit post), the scorecard MUST list it as an explicit omission WITH a one-line justification — never silently drop it, and never auto-add a component that does not belong. The end-of-run summary surfaces every such justified omission so the operator can sanity-check the call (do the component check every time; if a component is absent, justify it).** |

## C. SEO + schema

| # | Check | How to test | Pass criteria | Fixable | Fix recipe |
|---|---|---|---|---|---|
| 14 | Every dynamic-count shortcode renders a TRUSTWORTHY value on LIVE (trust-floor honoured) | grep rendered HTML for each count invocation + render check | No bare "0" anywhere (a 0 count must render empty / drop its clause, never "0"); every count is either >= its trust floor OR carries `below=` / the `[<prefix>_count_claim]` wrapper so a sub-floor value renders as a qualitative phrase, never a bare low digit. No raw `[..._service_stats` / `[..._count_claim` token leaks. **SCOPE-MATCH: the count's filter matches the article's actual subject** — a single-axis article (geo-only or type-only) uses a single-axis token; a COMPOUND article (a type/service IN a location) uses a compound `loc=` token (counts both axes, AND); when the compound count is below floor it FALLS BACK by keeping the type and broadening the location to citywide (e.g. "166 <type> across <city>"), via the `[<prefix>_count_claim ... fallback="..."]` wrapper, and only omits if even the citywide type is below floor. A service/type article must NEVER fall back to a location-only / all-types count (an article about one type must never count entities of another), and the inline count must share the type scope of the post's listing block. (Geo-generic "listings in X" articles legitimately use the location-only count.) | Y | Wrong taxonomy → run `wp term list <tax> --slug=X --field=count` across the taxonomies to find the right one. Low/zero count -> switch the area to its dense canonical slug (canonical-area-slug map) if a denser variant exists; else add the minimum-count argument (typical floors: area 5 / type 8) + a qualitative below-floor mode, or wrap a mid-sentence claim in `[<prefix>_count_claim]` so it degrades to a phrase / drops the clause. Re-render to confirm. |
| 34 | No HARDCODED directory/listing count anywhere (counts must be dynamic + evergreen) | Across body + the `key_takeaways` field + the `sources` field + the post excerpt + the meta description + FAQ answers, grep for a literal integer (incl. comma-grouped, e.g. `1,300`) immediately followed by a directory-listing noun (listings, providers, venues, businesses, verified). | 0 literal directory counts. Every count of directory listings is written as the site's dynamic-count token (e.g. `[<prefix>_service_stats slug=X stat=total taxonomy=Y]`), which the platform resolves in ALL those fields, not just the body. | Y | Replace each literal with the correct dynamic-count token — first verify the slug+taxonomy resolves to the right number (`wp eval 'echo do_shortcode("[...]");'`), then write the token, never the number. A count that legitimately has no matching taxonomy term (a true citywide total with no term) may stay static, but ONLY with an explicit one-line justification in the scorecard.Directory counts are always dynamic so the content stays evergreen. |
| 15 | Internal anchor count = config target window (8–12 total / 8–12 unique) | **Read the RAW stored post content from the database** (not the rendered URL — a render-time link guard can unwrap anchors to plain text for targets that are not published yet, making the live URL appear under-floor when the stored content is correct). Read it via the platform's content-read call, then count unique own-host hrefs excluding the homepage and the current-post URL. | 8 ≤ unique ≤ 12 AND sub-caps respected (max 2 hub, 2 tool, 1 generic, 2 blog-to-blog). A live-URL count below 8 is only a FAIL if the raw stored count is also below 8; if the stored content has ≥8 and the guard is unwrapping them for not-yet-published targets, those links self-heal when targets publish. | Y | If the stored content is <8: add anchors inline at natural editorial sentences (not headings, not the first 3 paragraphs, not the first paragraph under any H2/H3), pointing to indexable targets from the internal-link catalog, and write the patched body back via the platform's content-update call. If >12: remove the lowest-utility duplicate (usually the FAQ-section repeat). **Keep a deterministic backstop that reads the raw stored content and fails loud for any post below floor — the whole point is that it does not depend on the render.** |
| 16 | At least 1 back-link from a related published post | grep prior posts' content for `<a href="<new URL>"` | ≥1 anchor found | Y | Inject one sentence into the most relevant published post (per project's no-orphans rule). Verify post_status remained `publish` after `wp post update`. |
| 17 | Every source-row URL HEAD-200 (re-tested live, not just at write time) | curl -I each parenthesised URL in `sources[].source_description` | All HEAD 200 | Y | If fail: run a SERP query for `site:domain.com <topic>` to find a HEAD-200 alternative on the same source. Update the sources field. |
| 18 | Every source-row URL is deep-linked where the citation supports it | Compare each URL's path depth to the citation specificity. Homepages OK only for genuinely broad cross-references (e.g. multi-brand category citation) | Each citation either deep-linked OR explicitly broad | Y | Replace homepage URLs with deep URLs (a `site:domain.com <topic>` SERP query finds them); update the sources field. The theme's parens-URL regex supports `(domain.com/path)` form. |
| 19 | JSON-LD `Article.citation` URLs match the deep URLs in the rendered sources block | Parse JSON-LD; extract `citation[].url`; compare to anchor href in sources block | All match | Y | If schema URLs are still homepages while rendered are deep: stale schema cache or mu-plugin extractor mismatch. Re-flush cache; if still wrong, escalate (mu-plugin regex issue). |

| 33 | SEO-plugin focus keyword set (drives the on-page SEO score) | If the project uses an SEO plugin with a focus-keyword field (the config's `seo_focus_keyword_field`), read it. | Non-empty; the PRIMARY keyword is the first entry; comma-separated; the keywords match the post's primary + secondary keywords FROM THE KEYWORD QUEUE (spreadsheet) verbatim (the same set the post was written for). | Y | If empty or wrong: set it via the platform's meta-update call on the config's `seo_focus_keyword_field`, valued `"primary, sec1, sec2, ..."` = the post's primary first + ALL its secondary keywords from the keyword queue, verbatim. Do NOT derive keywords and do NOT body-filter (the spreadsheet is the source of truth). If the queue has no secondaries for the post, primary only. The visible SEO score recomputes when the post is opened or saved in the editor; setting this field is the enabler. |

## C2. Sitemap

| # | Check | How to test | Pass criteria | Fixable | Fix recipe |
|---|---|---|---|---|---|
| 29 | Post is present in the XML sitemap | Fetch the project's post sitemap (e.g. `/post-sitemap.xml` for Rank Math / Yoast) and grep for the new slug | New post URL present in the sitemap | Y | If absent after publish: confirm the post is `publish` and indexable (not noindex); flush the SEO plugin's sitemap cache; re-check. Transient absence right after publish is normal, re-check after a few minutes. |

## D. Editorial quality

| # | Check | How to test | Pass criteria | Fixable | Fix recipe |
|---|---|---|---|---|---|
| 20 | Forbidden words + banned sentence patterns count = 0 across all 9 authored fields | TWO scans across the same 9 fields: (a) a scan for every single word on the operator's forbidden-words list. (b) a regex scan for the operator's banned multi-word sentence patterns (the LLM-tell cliches). Both lists come from the house style guide named in the site config; run them over the field values read straight from the CMS, not over the rendered page. Fields: `post_title`, `post_excerpt`, `post_content`, the SEO title meta, the SEO description meta, the `key_takeaways[].takeaway` rows, the `sources[].source_name` rows, the `sources[].source_description` rows, plus any literal strings in the temporary publish script from this run. | 0 hits per scan per field | Y | For forbidden words: replace with non-banned synonym OR rephrase. For banned patterns: rephrase the offending sentence (synonym substitution does not address the structural cliche). Re-scan after fix. |
| 21 | Em-dashes (—, U+2014) + en-dashes (–, U+2013) count = 0 across all 9 authored fields | Same scanner as check 20, looking for U+2014 / U+2013 | 0 hits per field. Theme-emitted `<script>` developer comments are out of scope. | Y | Replace each with `:` (colon), `,` (comma), or restructure. Re-scan after fix. |
| 22 | Primary keyword density correct + per-paragraph cap | Count exact-match occurrences of primary in body. Count head-of-primary substring occurrences. Combine. Compute density vs body word count. Per `<p>`/`<li>`/`<td>` count exact-match occurrences. | Combined density 0.5–2.0% (entity) or 0.3–1.5% (broad); hard ceiling 3.0%; never 2x exact-match in the same paragraph | Y | If <floor: add 1–2 natural exact-match mentions in H2 prose. If >ceiling: rephrase down using "the ritual"/"this treatment"/pronoun. If 2x-in-paragraph: rephrase one of the pair. |
| 23 | Each secondary keyword appears 1–5 times in body, distributed across H2s | Parse `secondary_keywords` CSV. For each, check if it's a strict substring of primary → EXEMPT (covered by check 22). Otherwise count occurrences in body prose. | Each non-exempt secondary 1–5 occurrences, spread across ≥2 H2 sections | Y | If 0: add 1 natural occurrence in the most relevant H2 (FAQ Q+A or "How it works" usually accept it). If >5: rephrase surplus. If clustered in one H2: redistribute one occurrence to a different H2. |
| 27 | Style fingerprint (5 quantitative metrics) within target window | Compute 5 readability metrics over the body text directly (strip HTML first): average sentence length, sentence-length standard deviation, average sentences per paragraph, Flesch-Kincaid grade level, and passive-voice ratio. Grade each PASS / SOFT_FAIL / HARD_FAIL against the windows below (use the B2B window for B2B-audience projects). | All 5 PASS or SOFT_FAIL. Any HARD_FAIL blocks publish. Targets (general profile): avg sentence length 12–22 words; sentence-length std dev 5–9; avg paragraph 1–4 sentences; Flesch-Kincaid grade 7–9; passive voice ratio <15%. B2B profile: FK 10–12. Hard-fail thresholds: avg sl <8 or >28; std dev <3 or >12; paragraph >6 sentences; FK <6 or >13; passive >25%. | Y | Per metric: avg sl too high → split 2-3 long sentences; avg sl too low → combine 2-3 short sentences; std dev too low → vary sentence length deliberately (mix short and long); std dev too high → rebalance toward the mean; paragraph too long → split at natural break; FK too high → simplify vocabulary in 1-2 paragraphs; FK too low → accept (rarely an issue for entity articles); passive >15% → convert 2-3 passive constructions to active voice. Recompute after each fix until PASS or SOFT_FAIL. SOFT_FAIL is acceptable to ship; HARD_FAIL must be cleared. |

## D2. Featured-entity quality floor

| # | Check | How to test | Pass criteria | Fixable | Fix recipe |
|---|---|---|---|---|---|
| 28 | Every featured/recommended entity clears the project's configured quality floor | For each entity rendered via the project's per-entity card shortcode or named as a recommendation: read its rating, review/popularity count, and featured image. Compare to the project config's floor (rating threshold, minimum review count, non-placeholder image). | Every featured entity meets ALL configured thresholds (rating AND review count AND real image). Count is quality-gated, never padded to fill template slots. | Y | Drop any entity below any threshold and re-pick a qualifying alternative, or shorten the list / cover in prose. Never lower a threshold to fill a slot. |
| 36 | Featured listing matches the article's venue TYPE (no cross-category) | Render the post's dynamic listing block and read each returned entity's TYPE taxonomy. Confirm every entity's type belongs to the article's topic family. The listing block's filter argument MUST be an entity-TYPE family/preset, never a bare service-level term, which cross-categories. | Zero off-topic-type entities. An article about one service type shows only entities of that type, never entities of an adjacent type that merely offer the service as a sideline. The filter argument resolves to the entity-TYPE taxonomy (preset or slug), never the service taxonomy. | Y | Change the filter argument to the entity-type preset for the topic. Verify: render the block server-side and read back each returned entity's type taxonomy. |

## E. Cannibalization

| # | Check | How to test | Pass criteria | Fixable | Fix recipe |
|---|---|---|---|---|---|
| 24 | URL overlap <30% with each adjacent published post's primary keyword SERP | Run `mcp__serpapi__google` for new post's primary + each sibling's primary in same geo. Compare top-10 organic URLs. Overlap = shared URL count / 10. | Each pair <30% | Y (per project delegation) | Routing is set per site in the active context's config (`config/<ctx>`, delegation section). For a site the config DELEGATES: auto-resolve, do NOT escalate. ≥30% → pick the best fix yourself: narrow this post's angle, narrow the sibling's, differentiate scope, or merge the unique value into the stronger/older post and trash the weaker (reversible trash, never `--force`). Update CSV `avoid_notes` + record in the end-of-run summary (highlights + why, no assets). For sites WITHOUT this delegation, fall back to escalate (N). |

## E2. Cross-corpus consistency (batch-level, runs AFTER all posts in a batch are drafted)

Per-post audits (A–G) catch nothing about whether posts AGREE with each other. This batch-level pass does. Run it once per batch across the new cohort PLUS the existing same-topic cluster (siblings sharing the primary pillar). Best run as a fan-out workflow: one agent per post extracts structured claims (price ranges, legality statement, named entities + ratings/review counts, directory counts, durations), then one synthesis agent flags contradictions, duplications, and editorial drift. (A single cross-check of this kind routinely catches a regulatory contradiction repeated across a whole cluster, and an umbrella post whose price floor fails to enclose its cheapest child — both invisible to per-post audits.)

| # | Check | How to test | Pass criteria | Fixable | Fix recipe |
|---|---|---|---|---|---|
| 31 | The topic cluster reads as ONE consistent resource | Extract claims from every post in the cluster; cross-check for: (a) **price enclosure** — an umbrella/hub post's range must ENCLOSE every dedicated child's range, never contradict it; (b) **entity agreement** — the same named entity must carry the same rating/review-count wherever cited (distinct branches are OK if named/located distinctly); (c) **regulatory/legality consistency** — one canonical licensing statement across all posts; (d) **near-duplicate passages** — no verbatim boilerplate repeated across siblings; (e) **format consistency** — review counts, durations, thresholds stated the same way. | No contradictions; umbrella ranges enclose children; one canonical legality line; no verbatim cross-post duplication | Y (auto-resolve where the project delegates overlap/consistency decisions; else escalate) | Pick the canonical value (the dedicated/most-authoritative post wins for its topic; the umbrella widens to enclose). Apply it across every affected post (future posts freely; LIVE posts only with a backup taken first and a post-edit smoke test after). Reword duplicated passages in each post's own voice. For a site the active context's config DELEGATES (`config/<ctx>`, delegation section), this is AUTO-RESOLVE; summarize what changed + why, no assets. Otherwise escalate. |
| 35 | Uniqueness floor + H2-skeleton variance vs same-cluster siblings (anti-doorway / scaled-content defense) | Identify same-cluster siblings (by `pillar_primary`/`cluster`). Fetch the new post body + each sibling body, then compute two similarity measures directly for each sibling pair: (a) 5-gram Jaccard similarity over the normalized body text, with the site's place names stripped first so a geo-series does not self-flag; (b) shared-H2 ratio, comparing the normalized H2 sets. Also count sentences that appear identically in both bodies. | No sibling exceeds: 12% geo-normalized 5-gram Jaccard, 8 identical sentences, or 60% shared H2 set. | Y (**HARD-FAIL blocks publish**) | Rephrase the overlapping 5-grams / identical sentences in the post's own voice; reorder + replace H2s (variable section order, 2+ SERP/PAA-driven H2s, ≥1 section no sibling has) until under all three thresholds. Recompute all three. This is the dominant duplicate signal at 1,000 posts, so it is a hard gate, not advisory. |

## F. Topical completeness

| # | Check | How to test | Pass criteria | Fixable | Fix recipe |
|---|---|---|---|---|---|
| 26 | All canonical entities (from Phase 3 `entities_canonical[]` / Phase 4 `entities_and_terms.must_mention[]`) appear ≥1x in body prose | For each canonical entity in the must-mention list, case-insensitive grep the body (excluding nav/footer). Count occurrences. | Every must-mention entity has ≥1 body occurrence | Y | If ≥1 entity missing: add 1 natural mention to the most relevant H2 (the entity's `type` field hints — "process" entities go in How-it-works section, "product/ingredient" entities go in What-is or Cultural-authenticity sections, "people/institutions" go in Vetting or Sources, "tools/equipment" go in How-it-works or What-to-expect, "named places" go in Top-Areas or Cultural-origin). If 3+ entities missing: section-level rewrite likely needed → flag for user (not a 1-sentence fix). Re-grep after each insertion. |

## G. Visual QA (run in Phase 11 wherever a browser is available, NOT by a text-only auditor — requires browser rendering)

A text-only auditor (read + grep + shell, no browser) cannot render a page, so these checks are executed wherever a browser IS available, in Phase 11, after the text audit (A-F) passes. The text audit can confirm an `<img>` tag exists; only a render confirms it loaded, is the right shape, and that the layout did not break. Mechanic ladder, in order of preference:

1. **A browser-automation tool** that can navigate and evaluate JS in the page (Playwright, Puppeteer, or an equivalent) — preferred.
2. **Headless Chrome from the shell** (`chrome --headless` or a small script) — if no browser-automation tool is wired up (e.g. an unattended cron run).
3. **curl-subset** — if no browser at all: run the curl-checkable checks (G2 placeholder grep, G4, G5) and FLAG G1 + G3 as "skipped — no browser, manual spot-check advised" in the scorecard. Never silently pass a skipped check.

Project-specific selectors, placeholder filename, breakpoints, and the linkable-entity rule come from the project's `blog-pipeline-config.md` "Visual QA config" section. If the project config has no Visual QA section, run only G1 + G4 (generic) and note the rest as not-configured.

| # | Check | How to test | Pass criteria | Fixable | Fix recipe |
|---|---|---|---|---|---|
| G1 | No horizontal overflow at each configured breakpoint | At each width (default 390 / 768 / 1280), evaluate `document.documentElement.scrollWidth <= document.documentElement.clientWidth + 2` | No overflow at any width | Y | Find the widest offending element (compare child `getBoundingClientRect` to viewport); constrain with `max-width:100%` / `overflow-x:clip`. If it lives in shared header/footer chrome, escalate (theme-level). |
| G2 | Every content image is loaded, and none is the placeholder | For each `<img>` inside the article body: `naturalWidth > 0` AND `src` does NOT contain the project's placeholder filename. curl fallback: grep rendered HTML for the placeholder filename (fail if present) + HEAD each `<img src>` for 200 | All loaded; 0 placeholders | Y | A featured-entity card showing the placeholder → generate a real image via the project's image provider and set it, OR if the entity is below the project's quality floor, drop it and re-pick a qualifying one. Broken image (naturalWidth 0) → fix `src` or re-import the media. |
| G3 | Repeated card components render uniform media dimensions within each breakpoint | Measure every instance of the project's card-media selector; assert width and height are equal (±1px) across all instances at each breakpoint | Uniform per breakpoint | Y | Inconsistency = conflicting CSS accretion. Consolidate with ONE authoritative, scoped, last-in-cascade block whose selector specificity STRICTLY beats the winning rule. Grep the stylesheet for the literal property value (e.g. `grep -n "min-height: ?216"`) to find the rule that's actually winning; do NOT append another equal-specificity `!important`. Article-scope the override so the same component on other page types is untouched. |
| G4 | Every internal body anchor resolves HTTP 200 | Extract `<a href>` pointing at the own host from the body; HEAD each | All 200 (no 404 / redirect loop) | Y | Correct the URL or remove the anchor. |
| G5 | Link-target completeness: every linkable entity named in a table/list is hyperlinked when its page exists | Per the project's linkable-entity rule: for each entity name in a table cell / list item that matches a known taxonomy slug, confirm a live `/{slug}` page (HTTP 200) and that the cell is wrapped in `<a href>` | Every entity with a live page is linked | Y | Add the missing link to the existing page. If the page does not resolve, leave the entity as plain text (never invent a target). |

---

## E3. Periodic CORPUS-level audit (NOT per-post — runs post-batch / monthly)

The per-post audit above is structurally blind to cross-post and directory health: broken archive pagination, count drift, dead taxonomy slugs, stale sitemaps, sibling undercount, and orphan posts all ship silently because no per-post check looks across posts or at the directory. Run the corpus audit on a cadence (after each batch and/or monthly), NOT for every post:

Run it as a standalone pass over the site (sample the archives, then run C1-C6 below). Worth scripting once the corpus is large enough that a manual pass is slow.

| # | Check | Pass criteria | Fix recipe |
|---|---|---|---|
| C1 | Archive link-graph | Every sampled type/location/service archive exposes ≥8 server-side entity links in its rendered HTML (not injected client-side). | The archive template stopped server-rendering its entity links — restore the server-side render. |
| C2 | Pagination canonical | `/{archive}/page/N` returns 200 with a self-referential canonical (never the blog index). | The pagination rewrite rule or its canonical filter is missing/broken — ship or repair it. |
| C3 | Taxonomy integrity | Every `(slug, taxonomy)` used in a `[<prefix>_service_stats]` token across published/future posts resolves to a real, non-zero term. | Dead/zero slug: switch to the dense canonical slug or correct the taxonomy; fix every post using it. |
| C4 | Sitemap freshness | The directory sitemap's newest `lastmod` is within 30 days. | Entity edits are not bumping the modified date or flushing the sitemap cache — wire the invalidation hook. |
| C5 | Count trust-floor sweep (deeper pass) | No published post renders a bare `0`/sub-floor directory count or a raw `[..._service_stats` / `[..._count_claim` token. | Apply the trust-floor / canonical slug / compound fallback per checks 14 + 34. |
| C6 | Orphan-inbound + sibling-undercount (deeper pass) | Every published post has ≥1 inbound internal link; no post uses a thin area slug when a denser canonical sibling exists. | Inject a back-link from the most relevant sibling; switch the undercounting post to the dense canonical. |

C1-C4 are cheap enough to automate first; C5-C6 are deeper passes worth adding as the corpus grows. Surface the corpus audit's verdict (and any FAIL) in whatever batch or maintenance summary the operator already reads.

---

## Scorecard format (the auditor returns this)

```
POST: <slug>
URL: https://<host>/<slug>
POST_ID: <id>
PRIMARY_KEYWORD: "<primary>"
SECONDARY_KEYWORDS: ["<sec1>", "<sec2>", ...]
TIMESTAMP: <ISO 8601 UTC>

CHECKS:
  1. <PASS|FAIL> — <one-line evidence>
  2. <PASS|FAIL> — <one-line evidence>
  ...
  24. <PASS|FAIL> — <one-line evidence>

FINDINGS:
  fixable:
    - check_id: <N>
      reason: <one sentence>
      fix: <recipe from this checklist>
    - ...
  unfixable:
    - check_id: <N>
      reason: <one sentence>
      escalation: <what user must decide>
    - ...

VERDICT: <PASS|FAIL>
SUMMARY: <one paragraph>
```

The parent processes the scorecard:
- For each fixable: apply the recipe, log the before/after to changelog.
- For each unfixable: bundle into ONE `AskUserQuestion` (multiSelect=true) so user resolves all blockers in a single prompt. In batch/autopilot posture, do NOT surface an `AskUserQuestion`: record unfixable findings as draft-plus-flag (the post stays an unscheduled draft, blockers listed in the batch summary). The single-multiSelect prompt and the end-of-run verdict pop-up are SINGULAR interactive mode only. An unverifiable render-dependent check routes to draft-plus-flag (listed as unverified), never a pop-up and never a green pass.
- Re-run the audit on impacted checks after fixes land.
- After the text audit (A–F) is clean, run **Phase 11 (Visual QA / Section G)** on the main thread, apply its fixes the same way, then surface a single end-of-run verdict pop-up that reflects BOTH the text and visual audits.

---

## Versioning

Every check below was added because something shipped broken and nobody noticed until later. Keep that discipline: when you add a check, log it here with the date and the ONE-LINE failure that motivated it. A checklist whose rows have no recorded cause slowly fills with cargo-culted checks nobody dares delete, and the genuinely load-bearing rows become indistinguishable from the decorative ones.

| Version | Date | Change |
|---|---|---|
| v1 | <date you install this> | Adopted as-is. |
