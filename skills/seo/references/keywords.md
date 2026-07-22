# Keyword Research Reference

### Topical Authority

Topical authority is the depth and breadth of your website's coverage and reputation on a given topic. More pages covering subtopics + more depth per page + more backlinks on the topic = more authority in Google's eyes.

A hub-and-spoke architecture builds topical authority across a topic. Each hub page with its spoke pages signals deep expertise on that topic cluster.

### Keyword Density

Keyword density is the percentage of times the focus keyword appears relative to total word count.

**Guidelines:**
- Target 0.5-1.5% density for the primary focus keyword (roughly 5-15 mentions per 1,000 words)
- Density below 0.3% suggests the keyword is underused
- Density above 2.5% risks keyword stuffing penalties
- Count includes exact match and very close variations
- Distribute keyword mentions throughout: intro, body sections, and conclusion, not clustered in one area
- Use keyword variations and semantically related terms (LSI keywords) alongside the focus keyword
- Never sacrifice readability for density

## SERP Analysis Framework

Run this before creating any content brief. The SERP is the spec. Everything else is guesswork.

### Step 1: Read the SERP for intent signals

Search incognito. Look at what Google is showing, not just what ranks.

**Signals to read:**
- Featured Snippet present? That tells you Google wants a direct, factual answer.
- People Also Ask (PAA)? Shows adjacent questions your content should answer.
- Knowledge Panel? Indicates an entity-heavy topic.
- Ads? Signals commercial intent — calibrate how aggressively transactional your page should be.

**Adjacent intent sources:**
- Google auto-suggest (type the keyword, stop typing, read the suggestions)
- Related searches at the bottom of the SERP
- Title tags of the top 10 results
- PAA questions

**Common SERP compositions (helps set content type):**
- High-level guide / "what is" pages
- Brand homepages (navigational intent — often not worth competing on)
- Best-of listicles
- Wiki or reference content
- KWR tool pages (indicates informational, low commercial value)

### Step 2: Assess competitiveness

Before investing time in a brief and page, decide whether the keyword is worth pursuing.

- **Domain authority**: How does your DA compare to the top 10? Competing against DA 80+ sites on a low-DA domain is rarely worth it.
- **Brand strength**: Are the top results all recognizable brands? Brand results are harder to displace.
- **Topical authority**: Does your site have meaningful depth on this topic already?
- **Search intent alignment**: Does what Google is ranking match what your business can genuinely deliver?
- **Funnel stage**: TOFU, MOFU, or BOFU? Prioritize BOFU first.

### Step 3: Perfect Page analysis

For each of the top 3-5 ranking URLs, catalog what's on the page. Build a list of content elements that appear across all top results — these are table stakes. Then identify what's missing across all of them — that's your information gain opportunity.

**Elements to check per URL:**
- Jump links / table of contents
- Breadcrumbs
- TL;DR or summary at top
- Comparison tables
- Visual diagrams or infographics
- Short explanatory video
- Author bio at the bottom
- Related articles section
- Internal link modules
- CTA placement and type
- Featured snippet-optimized answer block
- Structured data (check source for JSON-LD)

**The differentiator question:** After cataloging what everyone has, ask: what is nobody doing that would be genuinely more useful?

**Ways to achieve information gain over top-ranking pages:**
- Incorporate proprietary data or original research
- Find an angle in the search intent that others are not addressing (hidden intent)
- More curated examples, case studies, or user-generated content
- A calculator, tool, checklist, or template embedded on the page
- Clearer, more actionable step-by-step instructions
- Deeper historical or technical context

---

## Keyword Research Methodology

- Start with buying intent. Informational only when it feeds conversion.
- Cluster by intent, not just topic.
- Prioritize: search volume x conversion probability x competition.
- Identify quick wins: existing pages ranking 5-20 that need optimisation.
- Programmatic opportunities: patterns that can generate 10-100 pages from a template.
- Bottom-up content strategy: prioritise BOFU (bottom of funnel) content before MOFU and TOFU.

---


## Keyword Cannibalization

Keyword cannibalization occurs when multiple pages on your site target the same primary keyword, causing them to compete against each other. Google cannot determine which page to rank, often resulting in neither page ranking well.

### How to Detect Cannibalization

1. **Search Console query report**: Filter by query and check if multiple URLs appear for the same search term.
2. **Site search**: Run `site:yourdomain.com "focus keyword"` in Google. If multiple pages appear, check whether they target the same intent.
3. **Keyword tracking**: Maintain a focus keyword register, a spreadsheet mapping each page to its primary focus keyword. Check before publishing new content.

### Prevention

- Assign one unique primary focus keyword per page before writing content
- Check the focus keyword register before creating new pages or blog posts
- Differentiate pages by search intent: a service page for "[keyword]" (transactional) and a blog post for "how to [identify or fix] [problem]" (informational) can coexist because they serve different intents

### Resolution Strategies

- **Merge**: Combine two pages targeting the same keyword into one stronger page. Redirect the weaker URL (301) to the consolidated page.
- **Differentiate**: Rewrite one page to target a different keyword or a more specific long-tail variation.
- **Canonical**: If you must keep both URLs live, set a canonical tag on the less important page pointing to the primary page.
- **Noindex**: If a page adds UX value but should not compete in search, add a noindex tag.

---


## Google Search Console and Bing Webmaster Tools Setup

**Google Search Console:**
- [ ] Property created and verified (HTML tag, DNS record, or Google Analytics verification)
- [ ] All versions of the site verified (www and non-www, HTTP and HTTPS) or use Domain property
- [ ] XML sitemap submitted
- [ ] Coverage/Pages report reviewed for errors (404s, noindex issues, crawl anomalies)
- [ ] Performance report reviewed for top queries, CTR, and average position
- [ ] Core Web Vitals report reviewed for mobile and desktop

**Bing Webmaster Tools:**
- [ ] Account created
- [ ] Site verified (can import from Google Search Console for quick setup)
- [ ] XML sitemap submitted
- [ ] SEO reports reviewed

**Monitoring cadence:**
- Weekly: check Performance report for traffic trends and ranking changes
- Monthly: review Pages/Coverage report for new errors, check Core Web Vitals
- After publishing new content: submit URL for indexing via URL Inspection tool

---

