---
name: editorial-calendar
description: Plan an editorial calendar that maps content themes to the strategy angle and SEO clusters, with cadence and owners. Use when a campaign needs a content schedule, triggers on "editorial calendar," "content calendar," "content schedule," "what should we publish," "content themes," "publishing cadence." Produces the content-package editorial_calendar for article briefs and distribution.
---

# Editorial calendar (sub-skill of content-marketing)

Builds the calendar that decides what content gets made, when, and by whom. Every theme maps
to the strategy angle and an SEO cluster, so the calendar serves real demand and a real
message instead of filler. English-first, English in parallel. Assembled into the
`content-package` by the content-marketing hub.

## Purpose

Give the content stream a clear, prioritized schedule: themes tied to the angle and the SEO
clusters, a realistic cadence, and a named owner per item. One machine, any campaign.

## When to use

- A campaign needs a content schedule before article briefs are written.
- Themes need to be sequenced and prioritized against the strategy and the SEO clusters.

## Inputs

- The `strategy-artifact`: segments, angle, offer_framing.
- The `seo-package`: keyword_map clusters and priorities, content_briefs[].
- The brief: objective, key dates, any campaign window.
- `context/brand-voice.md`: voice and the hard mechanical rules.

## Steps

1. List candidate themes from the strategy angle and the high-priority SEO clusters.
2. Map each theme to its angle rationale and the SEO cluster it serves. No orphan themes.
3. Sequence themes across the campaign window, with a cadence the team can actually hold.
4. Assign each item an owner and a target format (article, then its repurposed formats later).
5. Flag any theme that would need an unconfirmed offer, price, or Skill Path title, and stop
   and ask rather than inventing one.
6. Mark each item ready to brief, so `article-brief` can pick it up.

## Output

The `content-package` editorial_calendar:

```
items[]   each: theme, angle_link, seo_cluster, primary_query (ar, en), format,
          target_date, owner, status (planned | briefed | in-progress | published)
cadence   the publishing rhythm and why it is realistic
notes     gaps, dependencies, items blocked on a missing brief value
```

See `templates/editorial-calendar.md`.

## Hard rules

- Every theme maps to the angle and an SEO cluster. No orphan content.
- English-first, English in parallel. No em dashes. No tatweel. Western numerals only.
- Never invent an offer, price, Skill Path title, or instructor name to justify a theme. If a
  theme needs one and the brief is silent, stop and ask.
- Never imply certificate accreditation in any theme framing.

## How it connects

Feeds the content-marketing hub's editorial_calendar, which `article-brief` and
`content-distribution` build from. Internal planning, so it runs its skill eval for structure;
any customer-facing string still runs the copy and brand gates, per `runtime/verification.md`.
