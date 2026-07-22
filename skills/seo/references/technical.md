# Technical SEO Reference

### 2. Canonical Tags

Every page must have a self-referencing canonical tag pointing to its own URL.

```html
<link rel="canonical" href="https://example.com/service/sub-service" />
```

**Rules:**
- Always use the full absolute URL with https
- Use the production domain, not dev domains
- No trailing slashes (be consistent)
- For paginated content, canonical points to page 1

**Issues to watch for:**
- Noindex tags on important pages
- Canonicals pointing the wrong direction
- Redirect chains/loops
- Soft 404s
- Duplicate content without canonicals
- HTTP vs HTTPS inconsistency
- www vs non-www inconsistency

### 3. JSON-LD Structured Data

#### Schema Markup Detection Warning

`curl` and other static fetch tools cannot reliably detect structured data. Many CMS plugins inject JSON-LD via client-side JavaScript, which won't appear in static HTML output.

**To accurately check for schema markup:**
1. Browser: `document.querySelectorAll('script[type="application/ld+json"]')`
2. Google Rich Results Test: https://search.google.com/test/rich-results

Never report "no schema found" based solely on `curl` or any static fetch.

#### LocalBusiness (Homepage only)

```json
{
  "@context": "https://schema.org",
  "@type": "LocalBusiness",
  "name": "Business Name",
  "url": "https://example.com",
  "telephone": "[+country-code-phone-number]",
  "email": "info@example.com",
  "address": {
    "@type": "PostalAddress",
    "addressRegion": "Region Name",
    "addressCountry": "[ISO country code]"
  },
  "areaServed": [
    { "@type": "City", "name": "City 1" },
    { "@type": "City", "name": "City 2" }
  ],
  "openingHoursSpecification": {
    "@type": "OpeningHoursSpecification",
    "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday"],
    "opens": "09:00",
    "closes": "17:00"
  },
  "priceRange": "[price range symbol]",
  "image": "https://example.com/og-image.png",
  "description": "Short description including primary keyword and region."
}
```

Use the most specific `@type` available (e.g., `Plumber`, `DentalClinic`, `AutoRepair`) rather than the generic `LocalBusiness` when schema.org provides a match.

#### Service (Each service page)

```json
{
  "@context": "https://schema.org",
  "@type": "Service",
  "name": "Service Name",
  "description": "Brief description of the service.",
  "provider": {
    "@type": "LocalBusiness",
    "name": "Business Name",
    "telephone": "[+country-code-phone-number]"
  },
  "areaServed": {
    "@type": "Place",
    "name": "Region Name"
  },
  "hasOfferCatalog": {
    "@type": "OfferCatalog",
    "name": "Service Name Catalog",
    "itemListElement": [
      { "@type": "Offer", "itemOffered": { "@type": "Service", "name": "Sub-service 1" } },
      { "@type": "Offer", "itemOffered": { "@type": "Service", "name": "Sub-service 2" } }
    ]
  }
}
```

#### BreadcrumbList (Service, sector, and location pages)

```json
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    { "@type": "ListItem", "position": 1, "name": "Home", "item": "https://example.com" },
    { "@type": "ListItem", "position": 2, "name": "Hub Category", "item": "https://example.com/hub-category" },
    { "@type": "ListItem", "position": 3, "name": "Specific Service", "item": "https://example.com/hub-category/specific-service" }
  ]
}
```

#### WebSite (Homepage)

```json
{
  "@context": "https://schema.org",
  "@type": "WebSite",
  "name": "Business Name",
  "url": "https://example.com"
}
```

#### FAQPage (Service pages with FAQ sections)

```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Question text?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Full answer text."
      }
    }
  ]
}
```

#### HowTo (Blog posts with step-by-step content)

```json
{
  "@context": "https://schema.org",
  "@type": "HowTo",
  "name": "How to [Do Something]",
  "step": [
    {
      "@type": "HowToStep",
      "name": "Step name",
      "text": "Detailed instruction for this step."
    }
  ]
}
```

#### VideoObject (Pages with embedded video)

```json
{
  "@context": "https://schema.org",
  "@type": "VideoObject",
  "name": "Video Title",
  "description": "Brief description of the video content.",
  "thumbnailUrl": "https://example.com/thumbnails/video-thumbnail.jpg",
  "uploadDate": "2025-01-01",
  "duration": "PT5M30S",
  "contentUrl": "https://www.youtube.com/watch?v=example",
  "embedUrl": "https://www.youtube.com/embed/example"
}
```

- Add VideoObject schema to every page with an embedded video
- Use ISO 8601 duration format (e.g., `PT5M30S` for 5 minutes 30 seconds)
- Include `thumbnailUrl`, `uploadDate`, `duration`, and `description` for rich result eligibility

### 4. On-Page Focus Keyword Placement Checklist

Run this checklist for every indexable page before publishing. Each item is a pass/fail check.

- [ ] Focus keyword in SEO title, within the first 50 characters
- [ ] Focus keyword in meta description, within the first 160 characters
- [ ] Focus keyword in URL slug
- [ ] Focus keyword in first 10% of body content (or first 300 words for short pages)
- [ ] Focus keyword in at least one H2 or H3 subheading
- [ ] Focus keyword in at least one image alt attribute
- [ ] Focus keyword appears naturally throughout body content, not clustered
- [ ] Focus keyword uniqueness: no other page on the site targets this exact primary focus keyword

### 5. Heading Hierarchy

Every page must have exactly one `<h1>` tag containing the primary keyword.

**H1 patterns by page type:**
- **Home**: tagline with primary keyword
- **Service**: exact service name
- **Location**: "{Service} in {Location}"
- **Hub**: "{Category} Services"
- **Sector**: "{Service} for {Sector}"
- **Blog**: post title

**Subheadings:**
- H2 for major sections
- H3 for items within sections
- Never skip levels (no H1 to H3 without an H2)

**Common issues:**
- Multiple H1s on a page
- Skipped levels
- Headings used for styling only
- No H1 on page

### 6. Title Tag: Brand Name

Include brand/company name in the title tag only on brand-related pages:
- **Homepage**: lead with brand: `Brand Name | Primary Tagline`
- **About, Contact, Careers, and similar company pages**: append brand: `About Us | Brand Name`

Do NOT include brand name on:
- Service pages
- Product pages
- Blog posts
- Location pages
- Any keyword-targeted page

Every character in the title should go to the target keyword. Brand names in titles add no ranking value on keyword-focused pages and waste the 60 character budget.

**Exception:** If the brand name is very short (3-4 characters) and fits within 60 characters without pushing out keywords, it can be appended. When in doubt, skip it.

### 9. Image SEO

**Image file naming (before upload):**
- Use descriptive, keyword-relevant words: `plumber-drain-inspection.webp` not `IMG_20240315_001.jpg`
- Separate words with hyphens (not underscores or spaces)
- All lowercase
- Include focus keyword in the featured image filename where natural
- Name files before uploading. Renaming after upload does not change the URL on most platforms.

**Alt text:**
- All `<img>` tags must have descriptive `alt` text
- Alt text should include relevant keywords naturally
- CSS `background-image` has no alt text. Use `<img>` tags for important content images.

**Technical optimisation:**
- Use modern formats (WebP) where possible
- Lazy load images below the fold: `loading="lazy"`
- Set explicit `width` and `height` to prevent layout shift (CLS)

**Blog image guidelines:**
- Featured image: photorealistic, documentary style, 16:9 widescreen format
- Clean negative space on one side for headline overlay
- No readable text, logos, or watermarks in the image
- Convert to WebP format, max dimensions 1536x1024
- 1-2 inline images per blog post for posts over 1,000 words
- Each inline image needs: descriptive filename, alt text with relevant keywords, caption

### 10. Video SEO

**Embedding best practices:**
- Embed videos directly in relevant content pages where they add value
- Place the video near the top of the page or after the introductory section
- Only embed one primary video per page to avoid diluting the signal
- Host on YouTube for discoverability, then embed on your site for engagement

**VideoObject schema:** See JSON-LD section above.

**Video sitemaps:**
- Create a video sitemap or add video entries to the existing XML sitemap
- Include `<video:title>`, `<video:description>`, `<video:thumbnail_loc>`, and `<video:content_loc>` or `<video:player_loc>`
- Submit the video sitemap in Google Search Console

**YouTube repurposing:**
- Repurpose written content (guides, tutorials, FAQs) as video content on YouTube
- Link back to the corresponding page on your website in the video description
- Use consistent branding and keywords across written and video content

### 11. Sitemap and Robots

- `/sitemap.xml` must include every indexable page with `<lastmod>` dates
- `/robots.txt` must reference the sitemap URL
- Exclude admin/API routes from sitemap
- Blog posts should be added to sitemap dynamically as they are published
- Use production domain in sitemap URLs
- Ping Google/Bing when sitemap is updated for near-instant re-crawl
- Consider an HTML sitemap page with links to deep or hard-to-discover pages

### 12. Favicon

Every page must have a favicon. Check for `<link rel="icon">` in the `<head>`.
- Provide at least a 32x32 `.ico` or `.png` favicon
- Consider a 180x180 Apple touch icon (`<link rel="apple-touch-icon">`)
- Missing favicon causes 404 errors in server logs and looks unprofessional in browser tabs

### 13. Open Graph Tags

Every page should have:
```html
<meta property="og:title" content="{Page Title}" />
<meta property="og:description" content="{Page Description}" />
<meta property="og:url" content="{Canonical URL}" />
<meta property="og:type" content="website" />
<meta property="og:image" content="{OG Image URL}" />
<meta property="og:site_name" content="{Site Name}" />
```

**OG image requirements:**
- Dimensions: 1200x630 (16:9 ratio)
- Safe zone: all text and faces must fit within a 1:1 square centered in the image (630x630 center area). Platforms like WhatsApp, LinkedIn, and Slack crop to square in some views. Background imagery can extend outside the safe zone, but no readable text or faces should be cut off when cropped to 1:1.
- Every page needs an OG image. Pages without one display a blank or broken preview when shared.

### 14. URL Structure

- Readable, descriptive URLs
- Keywords in URLs where natural
- Consistent structure
- No unnecessary parameters
- Lowercase and hyphen-separated
- Subfolders preferred over subdomains for SEO (subfolders share domain authority more effectively)
- **Maximum URL length: 75 characters** (including protocol and domain). Shorter URLs correlate with higher rankings and are easier to read, share, and remember.

### 14. Noindex Strategy for Low-Value Pages

Noindexing prevents search engines from including thin or low-value pages in their index, preserving crawl budget for pages that matter.

**Page types to consider noindexing:**
- Tag archive pages: usually thin, duplicate content already covered by category or service pages
- Category archive pages: only if they contain no unique content beyond a list of post titles
- Author archive pages: on single-author sites, these duplicate the blog listing page
- Search results pages: internal site search results should never be indexed
- Media attachment pages: WordPress creates a dedicated page for every uploaded image. Almost always thin.
- Paginated archive pages: pages 2, 3, 4+ of paginated listings
- Login, admin, and utility pages

**Rules:**
- Always audit existing traffic before noindexing pages on a live site
- Use `<meta name="robots" content="noindex, follow">` to noindex while still allowing link equity to flow through internal links
- Periodically review noindexed pages to ensure no important pages are accidentally blocked

### 15. 404 Monitoring and Broken Link Management

**Monitoring process:**
- Check Google Search Console "Pages" report for 404 and soft 404 errors at least monthly
- Use crawl tools (Screaming Frog, Ahrefs Site Audit) quarterly to detect broken internal and outbound links

**Remediation rules:**
- **301 redirect**: use when a page has permanently moved. Passes link equity to the new destination.
- **302 redirect**: use only for temporary moves. Does not pass full link equity.
- **Fix the link**: if a broken internal link points to a page that still exists at a different URL, update the link directly
- **Remove the link**: if no suitable replacement exists, remove the link
- **Custom 404 page**: always have a helpful 404 page with search bar, popular pages, and contact information

**Redirect best practices:**
- Avoid redirect chains (A > B > C). Each redirect should point directly to the final destination.
- Avoid redirect loops (A > B > A).
- After implementing redirects, verify they work and update internal links to point directly to the new URL.
- Maintain a redirect log tracking old URL, new URL, date, and reason.

**Maintenance cadence:**
- Monthly: review GSC for new 404 errors
- Quarterly: full crawl audit for broken internal and outbound links
- After any major site restructure: comprehensive redirect mapping before going live

### 16. Instant Indexing (Google Indexing API)

The Google Indexing API enables near-instant indexing of new or updated content, compared to days or weeks via normal discovery.

**When to use:**
- Publishing time-sensitive content (blog posts, news, seasonal offers)
- After significant content updates
- New pages on sites with lower domain authority where natural discovery is slow

**Implementation:**
- Set up a Google Cloud project with the Indexing API enabled
- Create a service account and grant it Owner permissions in Google Search Console
- Submit URLs via the API using `URL_UPDATED` for new or updated pages, or `URL_DELETED` for removed pages
- Rate limits apply: batch submissions and respect Google's quota (typically 200 requests per day)

The Indexing API does not replace XML sitemaps. Continue maintaining sitemaps for comprehensive coverage.


## Crawlability and Indexation

### Crawlability Checks

**Robots.txt**
- Check for unintentional blocks
- Verify important pages are allowed
- Check sitemap reference

**XML Sitemap**
- Exists and accessible
- Contains only canonical, indexable URLs
- Updated regularly
- Proper formatting

**Site Architecture**
- Logical hierarchy with flat internal linking

### Indexation Checks

**Index Status**
- `site:domain.com` check
- Compare indexed vs. expected page count

**Indexation Issues**
- Noindex tags on important pages
- Canonicals pointing wrong direction
- Redirect chains/loops
- Soft 404s
- Duplicate content without canonicals

### Crawl Budget

Crawl budget is the number of pages Google will crawl on your site in a given timeframe.

**Optimise crawl budget by:**
- Excluding low-value pages via robots.txt or noindex
- Fixing redirect chains (each redirect wastes a crawl request)
- Ensuring important pages are easily discoverable via internal links
- Keeping sitemaps clean (only canonical, indexable URLs)

Crawl depth = how many clicks to reach a page. Crawl budget = how many pages get crawled at all. Both matter.

---

## Site Speed and Core Web Vitals

**Core Web Vitals Targets:**
- LCP (Largest Contentful Paint): < 2.5s
- INP (Interaction to Next Paint): < 200ms
- CLS (Cumulative Layout Shift): < 0.1

**Speed Factors:**
- Server response time (TTFB)
- Image optimisation
- JavaScript execution
- CSS delivery
- Caching headers
- Font loading

**Mobile-Friendliness:**
- Responsive design (not separate m. site)
- Tap target sizes (44x44px minimum)
- Viewport configured
- No horizontal scroll
- Same content as desktop

---

## HTTPS/SSL Verification

HTTPS has been a confirmed Google ranking signal since 2014. Every page must be served over HTTPS.

**Checklist:**
- [ ] SSL certificate is installed and valid (not expired)
- [ ] All pages redirect from HTTP to HTTPS (301 redirect)
- [ ] No mixed content warnings (HTTP resources loaded on HTTPS pages)
- [ ] Canonical tags, sitemap URLs, and internal links all use HTTPS
- [ ] HSTS (HTTP Strict Transport Security) header is set
- [ ] SSL certificate covers all subdomains if applicable

**Verification:**
- Use browser dev tools or an SSL checker tool to verify the certificate
- Test for mixed content using browser console
- Ensure www and non-www versions both redirect correctly to the canonical version

---


## Technical SEO Checklist

- [ ] Every page has unique `<title>` tag (max 60 chars)
- [ ] Every page has unique `<meta name="description">` (max 155 chars)
- [ ] Every page has `<link rel="canonical">`
- [ ] Every page has exactly one `<h1>`
- [ ] JSON-LD LocalBusiness on homepage
- [ ] JSON-LD Service on each service page
- [ ] JSON-LD BreadcrumbList on service/sector pages
- [ ] JSON-LD FAQPage on service pages with FAQ sections
- [ ] All images have alt text
- [ ] Sitemap includes all indexable pages
- [ ] Robots.txt allows crawling and references sitemap
- [ ] Brand name in title only on brand pages (homepage, about, contact). Not on service/product/blog pages.
- [ ] Favicon present on every page
- [ ] OG tags on every page
- [ ] OG image is 1200x630 with text/faces inside 1:1 center safe zone
- [ ] No duplicate content (canonical tags prevent this)
- [ ] Mobile responsive (Google mobile-first indexing)
- [ ] Fast load times (lazy images, minimal JS)
- [ ] HTTPS across entire site
- [ ] No mixed content
- [ ] LCP < 2.5s, INP < 200ms, CLS < 0.1
- [ ] No orphan pages (every page has at least one internal link pointing to it)
- [ ] Crawl depth: important pages within 3 clicks of homepage
- [ ] Bi-directional hub-spoke linking verified
- [ ] Blog posts include contextual links to service pages
- [ ] Crawl budget optimised (low-value pages excluded via robots.txt or noindex)
- [ ] Low-value pages noindexed (tag archives, media attachments, search results pages, thin category pages)
- [ ] HTML sitemap exists for deep/orphan pages if applicable
- [ ] URL length under 75 characters where possible
- [ ] Image filenames are descriptive, hyphenated, lowercase, and keyword-relevant
- [ ] Outbound links to authoritative non-competitor sources where appropriate
- [ ] Link attributes (nofollow, sponsored, UGC) used correctly on all outbound links
- [ ] No broken internal or outbound links (404s remediated with redirects or link removal)
- [ ] Redirect chains eliminated (each redirect points directly to final destination)
- [ ] Video content has VideoObject schema where embedded
- [ ] Google Search Console verified and sitemap submitted
- [ ] Bing Webmaster Tools verified and sitemap submitted
- [ ] SSL certificate valid, all pages served over HTTPS, no mixed content
- [ ] Paragraphs do not exceed 120 words
- [ ] Content incorporates related entities for relevancy
- [ ] Content adds information gain beyond competitor pages
- [ ] Blog posts over 1,000 words include a Table of Contents
- [ ] Title tags include sentiment words, power words, or numbers where appropriate (especially blog posts)
- [ ] Focus keyword density is between 0.5-1.5% per page
- [ ] Each page targets a unique primary focus keyword (no cannibalization)
- [ ] Focus keyword register maintained and checked before publishing new content
- [ ] On-page focus keyword placement checklist passed for every indexable page

---

## SEO Frameworks to Apply

### Foundation check (run first on any site)

- Crawlability: robots.txt, sitemap, noindex issues
- Indexation: coverage report, crawl errors, duplicate content
- Core Web Vitals: LCP, CLS, INP
- Mobile: mobile-first issues, viewport, tap targets
- Internal linking: orphan pages, link depth, anchor text
- Schema: missing structured data for content type

Do not add content on top of a broken foundation. Fix blockers first.

### Content strategy

- Every page needs one clear conversion goal. No page without a CTA.
- Internal linking targets must be defined before publishing.
- Content QA checklist before any post goes live:
  - Does it match search intent exactly?
  - Is there a clear CTA tied to the funnel stage?
  - Are internal links to related pages included?
  - Is the title tag optimised for the primary keyword?
  - Does it beat the top 3 ranking results on depth or usefulness?

---


## Tools

**Free Tools**
- Google Search Console (essential)
- Google PageSpeed Insights
- Rich Results Test (use this for schema validation; it renders JavaScript)
- Mobile-Friendly Test
- Schema Validator

**Paid Tools (if available)**
- Screaming Frog
- Ahrefs / Semrush
- Sitebulb
- BrightLocal (for local SEO specifically)
- TubeBuddy / VidIQ (for video SEO)
