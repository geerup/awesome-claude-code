---
name: on-page-optimization
description: Per-page on-page SEO specs in Arabic and English, one clear intent per page. Use when a page needs its title, meta description, headings, internal links, and schema markup set, triggers on "on-page SEO," "meta tags," "title tag," "meta description," "headings," "internal links," "schema markup," "structured data." Produces the seo-package on_page_specs[] for build and content.
---

# On-page optimization (sub-skill of seo)

Writes the on-page spec for a single page: title, meta description, heading structure,
internal links, and schema markup, all serving one clear search intent. English-first, with
the English equivalent in parallel and correct RTL. Assembled into the `seo-package` by the
seo hub. The page copy itself is authored later by the copywriters, not here.

## Purpose

Give each page one job and the on-page elements to win it: a clear primary query, a title and
meta that earn the click, a clean heading outline, supporting internal links, and valid schema.
One page, one intent. One machine, any campaign.

## When to use

- A page or set of pages needs on-page specs derived from the keyword_map.
- A page targets more than one intent and needs to be split or focused to one.

## Inputs

- The `seo-package` keyword_map: the cluster and primary query this page serves.
- The `strategy-artifact`: angle and offer_framing for how the page positions.
- The brief: page URL, offer details only when the page shows them.
- `context/brand-voice.md`: voice and the hard mechanical rules.

## Steps

1. Assign the page one cluster and one primary query. One clear intent per page, no overlap.
2. Draft the title tag: primary query led, within the length search results show, on brand.
3. Draft the meta description: plain, empowering, one clear value, no hype, no accreditation
   implication. English-first, English in parallel.
4. Outline the headings: one H1 that matches intent, H2 and H3 that structure the answer.
5. List internal links in and out, with anchor text, tied to related clusters and pages.
6. Specify schema markup (for example Organization, Course, FAQ, Breadcrumb) only where the
   page content truly supports it, with no invented claims or unconfirmed titles in the data.
   When the page serves generative (answer-engine) intent, structure it to be cited: lead with
   a clear definitional or direct answer near the top, use FAQ schema and question-led headings,
   and keep claims self-contained so an answer engine can quote the page accurately.
7. Flag any element that would need an unconfirmed offer, price, or Skill Path title, and stop
   and ask rather than inventing one.

## Output

The `seo-package` on_page_specs[], one per page:

```
url            the page this spec governs
primary_query  ar and en, the single intent this page serves
title          title tag (ar, en), query-led, on brand
meta           meta description (ar, en), plain and empowering
headings       h1, h2[], h3[] outline matching intent
internal_links each: anchor_text, target_url, why
schema         schema types and the fields, no invented claims
notes          intent conflicts resolved, values blocked on the brief
```

See `templates/on-page-spec.md`.

## Hard rules

- One clear intent per page. English-first, English in parallel, correct RTL. No em dashes.
  No tatweel. Western numerals only.
- Never invent an offer, price, Skill Path title, or instructor name in a title, meta, or
  schema field. If the page needs one and the brief is silent, stop and ask.
- Never imply certificate accreditation in any on-page element or schema field.

## How it connects

Feeds the seo hub's on_page_specs[], consumed by build (stream 6) and the content briefs. The
final page copy is authored by copywriter-ar and copywriter-en. Runs the gate stack: skill
eval, then `arabic-copy-qa` / `english-copy-qa` for the title and meta, then
`brand-qa-reviewer`, per `runtime/verification.md`.
