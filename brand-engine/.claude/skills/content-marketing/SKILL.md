---
name: content-marketing
description: Hub for the content-marketing stream, owned by content-marketer. Use when a campaign needs an editorial plan, article briefs, and a distribution plan built on the SEO and strategy work, triggers on "content marketing," "editorial calendar," "content calendar," "article brief," "blog plan," "content distribution," "repurpose the article." Routes to editorial-calendar, article-brief, and content-distribution, and assembles the content-package. Briefs and routes copy to copywriter-ar and copywriter-en, does not write final copy.
---

# Content marketing (stream hub)

The entry point for owned content planning. Owned by `content-marketer`. This hub does not
write articles itself. It reads the inputs, routes to the right sub-skill, and assembles the
`content-package` that copywriters author from and other owned streams distribute. English-first,
with Arabic only when a brief sets it in scope, built on the SEO clusters and the strategy angle.

## Purpose

Turn the `strategy-artifact` and the `seo-package` into an approval-ready content plan: an
editorial calendar, SEO-informed article briefs, and a distribution plan. The content-marketer
plans and briefs, the copywriters write. One machine, any campaign. Targets, offers, and prices
are read from the brief, never invented.

## When to use

- A campaign needs an editorial calendar mapping themes to the strategy angle and SEO clusters.
- A topic needs an SEO-informed article brief before copy is written.
- A published article needs a plan to repurpose it into email, organic social, and other formats.

Route by need:
- Themes, cadence, owners, mapped to angle and clusters: `editorial-calendar`.
- An SEO-informed English-first brief for one article: `article-brief`.
- Repurpose one article into email, organic-social, and other formats: `content-distribution`.

## Inputs

- The `strategy-artifact`: segments, angle, offer_framing.
- The `seo-package`: keyword_map, content_briefs[], on_page_specs[].
- The active `briefs/` file: objective, offer details only when content shows them.
- `context/brand-voice.md`: voice and the hard mechanical rules.

If a needed variable is absent from both brief and context, stop and ask. Do not fill the gap
with an invented value, claim, offer title, or subject name (context/subjects/).

## Steps

1. Validate the incoming envelope: right campaign_id, status at least qa-passed, required
   strategy and seo fields present, open_items read. If incomplete, return it, do not start.
2. Route theme and cadence planning to `editorial-calendar`, producing the editorial_calendar.
3. Route each planned article to `article-brief`, producing article_briefs[] for the copywriters.
4. Route repurposing to `content-distribution`, producing the distribution_plan.
5. Hand article_briefs[] to copywriter-ar and copywriter-en for authoring. Do not write the
   final copy here.
6. Collect every unresolved variable into open_items.
7. Run the gate stack in order: skill eval, then `arabic-copy-qa` (Arabic) and
   `english-copy-qa` (English) on any customer-facing string, then `brand-qa-reviewer`. A fail
   is a hard stop that returns to the author with exact fixes.
8. On pass, set status to qa-passed and hand the content-package downstream.

## Output: the content-package

```
editorial_calendar  themes mapped to the strategy angle and SEO clusters, cadence, owners
article_briefs[]    SEO-informed English-first briefs handed to copywriter-ar and copywriter-en
distribution_plan   how each article is repurposed and routed to owned channels
open_items          anything the producer could not resolve
```

Wrapped in the common envelope (campaign_id, produced_by, stream, status, qa, open_items,
brief_refs), per `runtime/handoff-contract.md`. See `templates/` in each sub-skill for shape.

## How it connects

- Consumes: `strategy-artifact` (stream 2) and `seo-package` (the SEO stream).
- Produces: the `content-package`, and routes article_briefs[] to copywriter-ar and
  copywriter-en for authoring, and distribution items to organic-social and lifecycle owners.
  The content-marketer does not write final copy.
- Gate before advance: skill eval + `arabic-copy-qa` / `english-copy-qa` + `brand-qa-reviewer`,
  in that order, per `runtime/verification.md`. Only qa-passed work crosses the boundary.
