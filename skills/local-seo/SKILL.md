---
name: local-seo
description: Local SEO for service-area businesses, GMB optimisation, local citations, map pack rankings, multi-location strategy. Use when asked about local search, Google Business Profile, map rankings, or location-based visibility.
disable-model-invocation: true
user-invocable: true
argument-hint: [business name or location] [optional: focus area]
---

## Local SEO Skill

You are operating at principal local SEO level. Local search is winner-take-most. The map pack gets 40-60% of clicks. Every recommendation must connect to calls, form fills, or foot traffic.

**Project context is loaded from the active CLAUDE.md. Apply all local SEO work to that specific business, location, and goals.**

---

## When invoked

If $ARGUMENTS is provided, treat it as the business or location target.
If no arguments, ask one question: which business and location are we working on?

---

## Local SEO frameworks

### 1. Google Business Profile (GBP): highest leverage

Google Business Profile is the most important local SEO factor for service businesses. It drives the Local Pack (map results) which appears above organic results for location-based searches.

**Setup and verification:**
- Claim and verify the listing at business.google.com
- Primary category: use the most specific category available. This is the most important GBP ranking signal. Research competitors.
- Secondary categories: add all relevant ones
- Service area business (no shopfront): hide address, set service area radius
- NAP must match the website exactly (see NAP Consistency section)

**Optimisation:**
- Name: exact legal business name, no keyword stuffing
- Description: first 250 characters matter most, include primary keyword naturally. Include primary keywords (service type, region, services offered).
- Services: add every service with descriptions. These create additional keyword surface area.
- Photos: minimum 10 total, add weekly, include exterior, team, branded vehicles (if applicable), and work in progress. Geo-tag images before uploading.
- Google Posts: publish offers, seasonal tips, and updates at least monthly. Posts do not directly rank but drive conversions.
- Q&A: seed your own questions with keyword-rich, detailed answers
- Reviews: see Reviews Strategy section below
- Attributes: set any applicable attributes

**GBP Checklist:**
- [ ] Listing claimed and verified
- [ ] Primary and secondary categories set correctly. Primary category is correct for the main service.
- [ ] Service areas configured for all target locations
- [ ] NAP matches website exactly
- [ ] Business description includes primary keywords, first 250 chars optimised
- [ ] At least 10 photos uploaded
- [ ] Google Posts published monthly
- [ ] Q&A seeded with common questions and detailed answers
- [ ] All services listed with descriptions
- [ ] Responding to all reviews within 48 hours

### 2. Local Pack Ranking Factors (in priority order)

1. GBP relevance: categories, services, description keywords
2. Proximity: physical address relative to searcher (cannot be changed, only targeted)
3. Prominence: review count, review rating, citation volume, domain authority
4. Behavioural signals: click-through rate, calls, direction requests

Work the factors you can control. Proximity is fixed.

### 3. NAP Consistency

NAP = Name, Address, Phone. Must be identical everywhere.

Ensure the business NAP appears identically in: website footer, contact page, JSON-LD structured data, all citation listings, and any mentions in body copy.

**Rules:**
- Same format, spelling, and phone number across every listing
- Even small differences (Street vs St, or phone format variations, e.g. +44 vs 0 in UK context) create inconsistency signals
- Audit existing citations before building new ones
- Remove or correct any outdated or duplicate listings

### 4. On-Page Local SEO

**Location pages:**
One page per service area location minimum.

- H1: "{Service} in {Location}"
- Title tag: "{Service} in {Location}, {Region}"
- Unique content per page. No spinning or near-duplicate templates.
- Body copy mentioning the location naturally 3-5 times
- List of services available in that location
- Nearby locations linked
- Local knowledge: mention landmarks, areas, local context
- Embed Google Map on each page
- JSON-LD: LocalBusiness schema with address, phone, openingHours, geo coordinates (see LocalBusiness schema example below)

**Homepage:**
- City + primary service in H1
- NAP in footer
- JSON-LD LocalBusiness schema

**Title tag formula:**
- Location page: `{Primary Service} in {Location} | {Business Name}`
- Service page: `Professional {Service Name} in {Region}`
- Homepage: `{Primary Service} Across {Region}`

### 5. LocalBusiness JSON-LD Schema

Place on the homepage. Use the most specific `@type` available on schema.org.

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
    "streetAddress": "123 Example Street",
    "addressLocality": "City Name",
    "addressRegion": "Region Name",
    "postalCode": "[postal code]",
    "addressCountry": "[ISO country code]"
  },
  "geo": {
    "@type": "GeoCoordinates",
    "latitude": "[latitude]",
    "longitude": "[longitude]"
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

For location pages, use a local variant of the schema with that location's address and geo coordinates.

### 6. Citations and Directories

Local citations are consistent business listings across online directories. They reinforce NAP signals and build local authority.

**Priority tier 1 (do these first):**
- Google Business Profile (most important)
- Bing Places for Business
- Apple Maps Connect
- Facebook Business Page
- Yelp

**Priority tier 2 (market and industry-specific):**
- (UK) UK trades: Checkatrade, TrustATrader, Bark, FreeIndex, Yell.com, Thomson Local
- (US) US home services: Angi, HomeAdvisor, Thumbtack, BBB, Houzz (for home/design trades)
- For all other markets: find the top 5-10 directories used by competitors in that sector and country

**Priority tier 3:**
- Local chambers of commerce
- Local news sites
- Business association membership directories

**Rules:**
- NAP must be identical across every listing (same format, spelling, phone number)
- Prioritise authoritative, relevant directories over quantity
- Remove or correct any outdated or duplicate listings
- Monitor citations periodically for accuracy
- Use BrightLocal or Whitespark for citation audits and builds at scale

### 7. Reviews Strategy

Reviews are one of the strongest local ranking signals and the primary conversion driver for local businesses.

**Acquisition:**
- Ask at the moment of maximum satisfaction: right after job completion
- SMS outreach converts better than email for review requests
- Review velocity matters: 5 reviews per month beats 50 reviews in one month then nothing for months
- Never incentivise reviews with discounts or gifts. This violates Google policy.
- Build a review acquisition system (automated follow-up), not one-off asks

**Management:**
- Respond to every review (positive and negative) within 48 hours
- Keep responses professional and take disputes offline
- Do not argue with negative reviews publicly
- Fake reviews from competitors: flag via GBP dashboard and document evidence

### 8. Multi-Location Strategy

- Separate GBP per location. Never combine locations into one profile.
- Separate location page per city on the website
- Do not use a P.O. box or virtual office as a GBP address. Google will suspend it.
- Service-area businesses (no shopfront): hide address in GBP, set service area radius

**Templated approach for new locations:**
1. Create GBP listing and verify
2. Build location page (unique content, not spun)
3. Set up citations in tier 1 directories
4. Begin review acquisition for that location
5. Build local links (local press, sponsorships, chamber membership)

### 9. Local Link Building

Local links build prominence signals and domain authority for local searches.

- Local press and news sites: digital PR around community stories
- Sponsorships with local clubs, charities, events
- Chamber of commerce and business association membership
- Supplier and partner pages: ask for a link alongside the logo
- Local blogger and influencer coverage
- Local council and government resource pages where relevant

### 10. Tracking and Measurement

- Google Search Console: filter by location queries, track map vs organic splits
- GBP Insights: track search queries, profile views, calls, direction requests
- BrightLocal rank tracker or similar: weekly local pack position per keyword per location
- Key metrics: map pack position, GBP call volume, direction requests, review count and rating

**Calls and form fills are the only metrics that matter at the local level.**

---

## Output format

**For a GBP audit:**
1. Critical issues (suspension risk or major ranking blockers)
2. Quick wins (fix this week)
3. 30-day priorities
4. Review acquisition plan

**For a new location setup:**
- GBP setup checklist
- On-page requirements
- Citation build list (tiered)
- Review acquisition system outline

**For a multi-location rollout:**
- Location prioritisation by search volume and competition
- Templated approach with unique elements per location
- Tracking setup

**Rules:**
- Calls and form fills are the only metrics that matter at the local level
- If the GBP is incomplete or has inconsistent NAP, fix that before anything else
- Label UK-specific vs universal advice. Regulations and directories differ by market.

---

## Reference files

| Task type | Reference file |
|---|---|
| GBP optimization playbook, 100-phone driving directions test, Whitespark workflows, $24K→$2.8M auto repair case study, $100K/mo local SEO playbook | `references/kb-distilled.md` |
