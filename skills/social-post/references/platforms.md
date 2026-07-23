# Platform adapters and angle variations

Loaded at Step 5 + 6 of the social-post skill.

## Step 5: Hashtags and tags

| Platform | Rule |
|---|---|
| LinkedIn | No hashtags by default. Minimal reach impact. Optional: 1-2 if directly relevant. |
| Twitter/X | No hashtags by default. Declining value. Optional: 1 if it adds discovery. |
| Instagram | 3-5 targeted. In first comment or separate block. No spam. |
| Facebook | No hashtags. |
| YouTube (community) | No hashtags. |
| YouTube (video description) | 3-5 tags for SEO discovery. |

If no hashtags are warranted, omit the HASHTAGS section from the output entirely.

---

## Step 5b: LinkedIn angle variations

After writing the original LinkedIn caption, auto-generate 2-3 additional LinkedIn caption variations from different angles. These are for reposting the same content weeks later with a fresh hook. Each variation is a complete, standalone caption (not a remix of the original).

### Angle detection table (auto-select based on brief content)

| Angle | Triggers when | What it leads with |
|---|---|---|
| Original | Always | The primary hook from the brief |
| Value-first | Post has a takeaway, resource, or actionable insight | What the reader gets. No story, no process. |
| Credit angle | Post mentions a person, tool, or source | The credited person/source. Tags them. |
| Opinion | Post has a methodology or stance that contrasts with norms | A contrarian statement or strong take |
| Numbers | Post has metrics or data | The biggest number front and centre |
| Personal | Post has a personal story or context | "I used to..." or "I needed this because..." |

### Rules

- Minimum 2 variations beyond the original. Maximum 4.
- Each variation must have a completely different hook (not a rephrased version of the original).
- Each variation gets its own matching first-comment file.
- Variations are LinkedIn-only. Other platforms only get the original adapted.
- Apply the same self-check to every variation.
- Apply the correct polish level to every variation (same as original).
- If the "Comment X" CTA pattern may underperform, at least one variation should use a softer CTA: "Link in the first comment" or "Drop a comment if you want the link" instead of "Comment [keyword]".
- Not every post triggers all angles. A post with no credited source skips credit angle. A post with no strong numbers skips numbers angle. Auto-select only what applies.

### Naming convention

```
caption-linkedin.txt                 (original, always generated)
caption-linkedin-value-first.txt     (if applicable)
caption-linkedin-credit-angle.txt    (if applicable)
caption-linkedin-opinion.txt         (if applicable)
caption-linkedin-numbers.txt         (if applicable)
caption-linkedin-personal.txt        (if applicable)
first-comment.txt                    (matches original)
first-comment-value-first.txt        (matches value-first)
first-comment-credit-angle.txt       (matches credit-angle)
first-comment-numbers.txt            (matches numbers)
first-comment-personal.txt           (matches personal)
dm-reply.txt                         (one version, works for all angles)
posting-schedule.txt                 (suggested repost timing)
```

### Posting schedule (auto-generated with every post)

- Original: post now
- Variation 1: 10-14 days later
- Variation 2: 21-28 days later
- Variation 3: 35-42 days later
- Best times: Tuesday-Thursday, 8-10am local time

---

## Step 6: Platform adapters

**Channel selection:** Read `references/channel-strategy.md` to determine which channels this post should go to. Not every post goes everywhere. The channel strategy file defines which content types map to which channels, posting times per channel, and format adaptations.

### LinkedIn (default)

- Hook must work above the "see more" fold (first ~210 characters on mobile).
- One sentence per line. Blank line between lines. No paragraphs.
- No link in main post body (kills reach). Link goes in first comment if needed.
- Tag people only when genuinely relevant.

### Twitter/X

- Single tweet only. Under 280 characters. No threads.
- Punchier. More opinionated. Fewer qualifiers than LinkedIn.
- Attach a single image (use single-image-a, a stat highlight, or a quote card).
- The tweet + image must work as one unit. No "swipe through" or carousel references.

### Instagram

- Front-load the hook before the "more" cutoff (~125 characters).
- Pair with strong visual direction (carousel or image).
- CTA: "Save this for later" (drives saves, strong algorithm signal).
- Shorter than LinkedIn. 5-10 lines max. Visual does the heavy lifting.

### Facebook

- Shorter than LinkedIn. 5-10 lines.
- Include the link directly in the post body (no reach penalty on Facebook, unlike LinkedIn).
- Visual-first. Pair with image or carousel.
- No hashtags.

### YouTube (community post)

- Shortest caption. 3-5 lines max.
- End with a question to drive comments. YouTube community posts live on engagement.
- Pair with a single image (stat highlight or quote card works well).

### YouTube (video description)

- SEO-focused. Primary keyword in first sentence.
- Structure: 1-2 sentence summary, timestamps, links, tags.
- 3-5 SEO tags at the end.
- Not the same as a social caption. This is metadata for search discovery.
