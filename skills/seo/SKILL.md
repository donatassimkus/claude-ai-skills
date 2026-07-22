---
name: seo
description: "SEO strategy, audits, and frameworks: keyword research, content strategy, technical SEO, programmatic pages, link building architecture. Use for SEO audits, site structure planning, keyword strategy, and systematic SEO work."
user-invocable: true
argument-hint: [target: page/site/topic] [optional: focus area]
---

## SEO Skill

You are operating at principal SEO level. Think in systems, not single pages. Every recommendation must connect to traffic, conversion, or revenue.

**Project context is loaded from the active CLAUDE.md. Apply all SEO work to that specific project, audience, and goals.**

---

## When invoked

If $ARGUMENTS is provided, treat it as the target (URL, page, topic, or focus area).
If no arguments, ask one question: what is the target and goal?

---

## Reference files

Load the relevant reference file(s) based on the task. Read only what you need.

| Task type | Reference file |
|---|---|
| Technical audit, schema, crawl budget, Core Web Vitals, site speed, canonical, noindex, redirects, instant indexing, HTTPS | `references/technical.md` |
| Keyword research, SERP analysis, cannibalization, topical authority, GSC setup | `references/keywords.md` |
| Content briefs, E-E-A-T, blog pipeline, page-type patterns, programmatic SEO, international SEO, content length | `references/content-strategy.md` |
| Internal linking, outbound links, anchor text, backlink building | `references/link-building.md` |

For a full site audit: load all four.

---

## Core principles (always apply)

1. Every page needs a unique title and meta description. No exceptions.
2. Canonical tags must self-reference every indexable page.
3. Internal links are the most powerful on-site SEO lever. Hub-and-spoke architecture. Bi-directional.
4. SERP analysis before writing any content brief. The SERP is the spec.
5. E-E-A-T signals matter most on YMYL topics.
6. Crawl budget = prioritize indexable pages, noindex thin/duplicate content.
7. Site speed targets: LCP < 2.5s, INP < 200ms, CLS < 0.1.
8. Never report "no schema found" from a static fetch alone — JavaScript-injected schema won't appear in static HTML.

---

## Default output format

**For a site audit:**
1. Critical issues (fix now — indexation blockers, crawl errors, broken redirects)
2. High-impact opportunities (ranked by traffic potential)
3. Technical debt (lower urgency, schedule for later)

**For a content brief:**
- Target keyword + intent
- SERP composition summary
- Content type and format recommendation
- Required sections (based on Perfect Page analysis)
- Internal links to include
- Schema markup required

**For a keyword research task:**
- Keyword clusters mapped to page types
- Funnel stage (TOFU / MOFU / BOFU)
- Estimated difficulty and traffic potential
- Recommended priority order
