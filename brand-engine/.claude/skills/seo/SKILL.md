---
name: seo
description: Hub for the SEO stream, owned by seo-specialist. Use when a campaign needs search visibility across Arabic and English, triggers on "SEO," "keyword research," "search intent," "on-page optimization," "meta tags," "schema markup," "technical SEO," "hreflang," "crawlability," "sitemaps." Routes to keyword-and-intent-research, on-page-optimization, and technical-seo, and assembles the seo-package that hands content briefs to content-marketer and copywriters.
---

# SEO (stream hub)

The entry point for organic search work. Owned by `seo-specialist`. This hub does not do the
research, write the specs, or run the audit itself. It reads the inputs, routes to the right
sub-skill, and assembles the `seo-package` that downstream content and copy streams consume.
English-first, with English handled in parallel and correct RTL and hreflang throughout.

## Purpose

Turn a strategy-artifact (segments, angle, offer framing) into an approval-ready search plan:
a keyword and intent map, per-page on-page specs, technical findings, and SEO-informed content
briefs the content-marketer and copywriters build from. One machine, any campaign. Targets,
offers, and prices are read from the brief, never invented.

## When to use

- A campaign needs keyword and search-intent research in Arabic and English.
- A page or set of pages needs on-page specs: titles, meta descriptions, headings, internal
  links, schema markup, one clear intent per page.
- A site or section needs a technical audit: crawlability, speed, indexation, sitemaps,
  hreflang for ar and en, RTL correctness, canonicalization.

Route by need:
- Keyword and search-intent research, clusters, priority: `keyword-and-intent-research`.
- Per-page on-page specs with one clear intent and no invented claims: `on-page-optimization`.
- Technical crawl, indexation, sitemaps, hreflang, RTL, canonicalization: `technical-seo`.

## Inputs

- The `strategy-artifact`: segments, angle, offer_framing.
- The active `briefs/` file: objective, target pages or URLs, offer details only when a page
  shows them.
- `context/brand-voice.md`: voice and the hard mechanical rules.
- Any existing site data: current URLs, analytics, search console exports, when available.

If a needed variable is absent from both brief and context, stop and ask. Do not fill the gap
with an invented value, claim, offer title, or an unverified claim.

## Steps

1. Validate the incoming envelope: right campaign_id, status at least qa-passed, required
   strategy fields present, open_items read. If incomplete, return it, do not start.
2. Route keyword and intent work to `keyword-and-intent-research`, producing the keyword_map.
3. Route page specs to `on-page-optimization`, producing on_page_specs[], one intent per page.
4. Route the crawl and indexation audit to `technical-seo`, producing technical_findings[].
5. Derive content_briefs[] from the keyword clusters and page intents, and hand them to the
   content-marketer and copywriters (copywriter-ar, copywriter-en) for authoring.
6. Collect every unresolved variable into open_items.
7. Run the gate stack in order: skill eval, then `arabic-copy-qa` (Arabic copy in specs or
   briefs) and `english-copy-qa` (English copy), then `brand-qa-reviewer`. A fail is a hard
   stop that returns to the author with exact fixes.
8. On pass, set status to qa-passed and hand the seo-package downstream.

## Output: the seo-package

```
keyword_map         clusters of Arabic and English keywords, intent, and priority
on_page_specs[]     per page: title, meta description, headings, internal links, schema
technical_findings[] crawlability, speed, indexation, sitemaps, hreflang, RTL, canonical
content_briefs[]    SEO-informed briefs handed to content-marketer and copywriters
open_items          anything the producer could not resolve
```

Wrapped in the common envelope (campaign_id, produced_by, stream, status, qa, open_items,
brief_refs), per `runtime/handoff-contract.md`. See `templates/` in each sub-skill for shape.

## How it connects

- Consumes: `strategy-artifact` (stream 2), the active brief, existing site data.
- Produces: the `seo-package`, and routes content_briefs[] to the content-marketer and to
  copywriter-ar and copywriter-en for authoring. The seo-specialist does not write final copy.
- Gate before advance: skill eval + `arabic-copy-qa` / `english-copy-qa` + `brand-qa-reviewer`,
  in that order, per `runtime/verification.md`. Only qa-passed work crosses the boundary.
