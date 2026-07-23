---
name: ux
argument-hint: what you want to audit or improve (e.g. "signup flow", "empty state", "is this form too long")
description: User experience design and audit. Covers user flows, Nielsen's 10 heuristics, cognitive load (Hick's Law, Miller's Law), Fitts's Law, information scent, affordances and signifiers, microinteractions, error prevention and recovery, progressive disclosure, empty states, loading states, onboarding, feedback loops, accessibility beyond WCAG (perceived performance, motor/cognitive accessibility), task success rate, and UX research frameworks (jobs-to-be-done, user interviews, usability testing, heatmap and session replay analysis). Invoke when the user asks about user experience, usability, interaction design, user flows, ease of use, microinteractions, empty states, error states, loading states, onboarding, or says "UX audit", "usability review", "user journey", "how easy is this to use", or "what's the user thinking when they land here". Visual design and layout, and conversion rate optimisation, are adjacent disciplines handled separately. This skill is the knowledge lens for how an experience feels to use; running a full cross-surface audit of a live project (fields, flows, PDFs, emails, consistency against the agreed model) is a separate exercise built on top of it.
user-invocable: true
---

# UX: user experience design and audit

The skill that sits between visual design (how it looks) and conversion optimisation (what it converts). Focuses on how it feels to use.

## Core frameworks

### Nielsen's 10 usability heuristics

Every audited surface should pass or fail each of these explicitly. Never score "UX" as one number; score against the 10 heuristics and aggregate.

1. **Visibility of system status** — the user always knows what's happening. Loading states, progress bars, success / error confirmations, unread counts, sync indicators.
2. **Match between system and real world** — labels, icons, and flow match the user's mental model, not internal engineering terms.
3. **User control and freedom** — easy undo, cancel, back, close. No dead-end modals. Confirm on destructive actions.
4. **Consistency and standards** — same word for the same thing across the product. Platform conventions respected (search top-right, login top-right, logo top-left on web).
5. **Error prevention** — prevent errors where possible. Disable unavailable options, confirm risky actions, use correct input types (email, tel, number), validate before submit.
6. **Recognition rather than recall** — show options rather than make users remember them. Autocomplete, recently-used, saved preferences, breadcrumbs.
7. **Flexibility and efficiency of use** — power shortcuts for experts. Keyboard shortcuts, bulk actions, saved filters, keyboard-first navigation.
8. **Aesthetic and minimalist design** — every element earns its place. Remove decoration that doesn't support the task.
9. **Help users recognize, diagnose, and recover from errors** — plain-language error messages, suggest a fix, never blame the user.
10. **Help and documentation** — in-context help where needed. Tooltips, empty-state guidance, zero-state tutorials, accessible docs.

### Cognitive load laws

- **Hick's Law**: choice time grows logarithmically with the number of options. Cut options above the fold. Group and progressively disclose.
- **Miller's Law**: working memory holds about 7 (plus or minus 2) chunks. Break long forms, menus, and lists into chunks of 5 to 9.
- **Fitts's Law**: target acquisition time depends on distance and size. Primary CTAs should be large and close to the user's attention or cursor.
- **Gestalt laws** (proximity, similarity, closure, continuity): visual grouping communicates relationship. Use consistent spacing to signal groups.

### Jakob's Law

Users spend most of their time on other sites and expect yours to work the same way. Patterns are not original: they are recognizable.

### Peak-end rule

Users judge an experience by its peak emotional point and its end. Design for a strong final moment (success confirmation, thank-you screen, first-win micro-celebration) and a memorable delightful moment somewhere in the middle.

## Surface-by-surface UX audit checklist

### Homepage

- Above the fold: is the single most important action obvious within 5 seconds?
- Is the value proposition one readable sentence?
- Is the next step (primary CTA) clearly more prominent than secondary actions?
- Does the page load without layout shift?
- Is there a loading state for any content that needs to fetch?
- Can the user quickly understand what this product does for whom?

### Pricing page

- Can the user compare tiers in a single glance?
- Is the recommended tier visually highlighted?
- Are tier differences parseable (not cryptic feature names)?
- Is there a way to contact sales or ask questions?
- Are the CTAs action-verbs (`Get started`, `Try free`), not vague (`Learn more`)?

### Signup / checkout

- How many fields? Every field has to earn its place.
- Can the user sign up with one click (SSO options)?
- Is the submit button label action-verbed (`Create account`) not `Submit`?
- Does the form validate inline, not only on submit?
- Is there a visible password strength meter?
- Is the next step after submit clear?

### Empty states

- When a user has no data yet, does the empty state teach the next step?
- Does it include a visual (illustration, icon) plus a single clear CTA?
- Does it avoid sounding like an error?

### Error states

- Does the error say what went wrong in plain language?
- Does it tell the user how to fix it?
- Does it preserve the user's input so they don't retype?
- Is the error message positioned next to the problem field?

### Loading states

- For anything over 200ms, is there a loading indicator?
- For anything over 1 second, is there a skeleton or progress indicator?
- For anything over 10 seconds, is there an estimated time remaining?
- Is there a failure path if the load times out?

### Onboarding

- What does the user need to see in the first 60 seconds to get their first win?
- Is there a guided first-run tour or a "try one example" path?
- Does the onboarding respect skipping for returning users?

## Microinteractions

A microinteraction is a contained product moment that revolves around a single use case. They make a product feel considered.

Elements:
- **Trigger**: what sets it in motion (click, hover, scroll, time)
- **Rules**: what happens next
- **Feedback**: what the user sees / hears / feels
- **Loops and modes**: state over time

Examples to audit on every feature:
- Button hover / active / focus / disabled states
- Form field focus, valid, invalid, success states
- Toggle switches with on / off feedback
- Copy-to-clipboard with "copied" confirmation
- Delete with undo toast
- Favorite / like with haptic + visual pulse
- Upload with progress, success animation, error retry

## Information scent

Users scan, they don't read. Every label, link, and CTA must smell like the content it leads to. If a visitor clicks `Pricing` and lands on a page labelled `Plans`, that's a scent break. Audit: do all link labels match their destination's H1?

## Affordances and signifiers

- **Affordance**: what an element lets you do (a button affords clicking).
- **Signifier**: the visual cue that communicates the affordance (underline, shadow, hover state).

Every interactive element needs a signifier. Common failures:
- Ghost buttons without borders that look like text
- Clickable cards without hover cues
- Expandable sections without chevron or "+" indicator
- Links without underline or color change

## Progressive disclosure

Don't dump everything at once. Show the most important thing first, the next layer on demand.

Patterns:
- Tabs
- Accordions
- "Show more" links
- Modal / drawer for detailed actions
- Hover reveals for secondary info
- Step-by-step wizards for multi-part tasks

## UX research frameworks

### Jobs-to-be-done (JTBD)

Every page should answer: what job is the user hiring this product to do? Example: "help me [primary outcome] without [the friction I usually face]".

### User interviews

When heuristics aren't enough, interview 5 users. 5 users surface ~80% of usability issues. Record sessions, code for repeated patterns.

### Usability testing

Classic task-based test: give a user a realistic goal specific to the product's primary use case, observe them complete it, measure:
- Task completion rate
- Time on task
- Error count
- Perceived effort (SUS, NPS, or custom 1-5 rating)

### Session replay / heatmaps

Hotjar, Microsoft Clarity, FullStory, LogRocket. Look for:
- Rage clicks (repeated click on same spot = broken)
- Dead clicks (click with no response = unclear)
- U-turns (user navigates away and back quickly = wrong place)
- Long mouse paths (user scanning, didn't find what they expected)
- Form abandonment at specific fields

## UX scoring rubric (0 to 100)

When auditing a surface, score each of the 10 Nielsen heuristics as 0 / 5 / 10 (fail / partial / pass), then sum. Adjust by:
- +5 for strong information scent across the surface
- +5 for well-designed empty / error / loading states
- +5 for thoughtful microinteractions (at least 3 on the surface)
- -10 for any missing affordance (interactive element without a signifier)
- -10 for any dead-end (user has no obvious next step)

Cap at 100. Scores under 60 signal an unusable surface. 60-75 signal workable but friction-heavy. 75-90 signal good. 90+ signal excellent.

## Accessibility beyond WCAG

WCAG covers basics. UX accessibility also covers:
- **Perceived performance**: does the page feel fast even if it technically isn't? (Optimistic UI, skeleton screens, progressive image loading.)
- **Motor accessibility**: tap targets 44x44 px minimum, generous click hitboxes, no tiny X close buttons.
- **Cognitive accessibility**: plain language (8th-grade reading level default), consistent vocabulary, predictable structures, avoid idioms.
- **Neurodivergent considerations**: reduce motion option, dark mode option, avoid pure red / green as only signifier, provide focus modes for distraction-heavy pages.

## Adjacent disciplines (where this skill stops)

- Visual layout and section structure: visual design
- Conversion rate specifically: conversion optimisation
- Copy style and tone: writing and editing
- Hook structure in headlines: hook craft
- Form design and email UX: email marketing when the surface is an email, else this skill
- Onboarding product flow: product management for the roadmap side, this skill for the interaction side

## Output format when audited

For every surface: scorecard (10 heuristics + adjustments), top 3 friction points, top 3 improvement recommendations, each tagged with estimated user-impact (high / medium / low) and effort (S / M / L).
