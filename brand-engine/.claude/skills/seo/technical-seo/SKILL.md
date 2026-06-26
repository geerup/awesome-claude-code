---
name: technical-seo
description: Technical SEO audit across crawlability, speed, indexation, sitemaps, hreflang for ar and en, RTL correctness, and canonicalization. Use when a site or section needs its technical search health checked, triggers on "technical SEO," "crawlability," "indexation," "sitemaps," "hreflang," "canonical," "page speed," "RTL rendering." Produces the seo-package technical_findings[] for build and on-page work.
---

# Technical SEO (sub-skill of seo)

Audits the technical health that decides whether search engines can crawl, render, and index
the site correctly, in Arabic and English. Covers crawlability, speed, indexation, sitemaps,
hreflang, RTL correctness, and canonicalization. Assembled into the `seo-package` by the seo
hub. This skill finds and specifies fixes, the build stream implements them.

## Purpose

Make sure the English-first site is fully crawlable, correctly indexed, and serves the right
language version to the right user, with RTL rendering intact. A perfect page spec is wasted
if the page cannot be crawled or the Arabic version is mislabeled. One machine, any campaign.

## When to use

- A site or section needs a technical crawl and indexation audit before or during a campaign.
- Arabic and English versions exist and hreflang and canonical handling must be verified.
- RTL rendering, sitemaps, or page speed are suspected to be holding back search visibility.

## Inputs

- The brief: the site, section, or URLs in scope, and the objective.
- The `seo-package` keyword_map and on_page_specs[], to know which pages matter most.
- Existing site data when available: crawl exports, search console, analytics, server logs.
- `context/brand-voice.md`: the hard mechanical rules, including RTL and Western numerals.

If a needed access or data source is absent, flag it as an open item. Do not assume a finding
you could not verify, and do not adopt a crawl tool without approval.

## Steps

1. Crawlability: check robots rules, crawl traps, broken links, redirect chains, orphan pages.
2. Speed: measure core load and rendering, flag what slows the priority pages. Score Core Web
   Vitals against the 2026 field thresholds at the 75th percentile: LCP at or under 2.5s, INP
   at or under 200ms, CLS at or under 0.1. INP has replaced FID, do not report FID.
3. Indexation: compare crawlable pages to indexed pages, flag noindex and accidental exclusion.
   Baseline for a key template is index,follow plus a self-canonical plus a 200 status.
   Investigate when the indexed-versus-canonical gap exceeds roughly 30 percent.
4. Sitemaps: verify an accurate XML sitemap exists, covers ar and en, is submitted, and carries
   only canonical 200 URLs (no redirects, noindex, or non-canonical entries).
5. Hreflang: verify each page declares ar and en alternates correctly and reciprocally, with
   the right language and region codes, so the right version serves the right searcher.
6. RTL correctness: verify Arabic pages render right-to-left, with mixed AR, EN, and numerals
   not breaking direction, and Western numerals shown.
7. Canonicalization: verify one canonical per page, no duplicate-content splits, ar and en not
   canonicalizing to each other.
8. Record each finding with severity and a concrete fix, and collect access gaps as open items.
9. Cadence: run the technical audit on a quarterly cadence to catch regressions.

## Output

The `seo-package` technical_findings[]:

```
findings[]   each: area (crawlability | speed | indexation | sitemaps | hreflang | rtl |
             canonical), issue, severity (high | medium | low), affected_urls[], fix
hreflang_map ar and en alternates per priority page, reciprocity confirmed
rtl_checks   per priority page: direction correct, numerals Western, mixed content safe
open_items   access not granted, data source missing, finding could not be verified
```

See `templates/technical-seo-audit.md`.

## Hard rules

- Western numerals only in any reported value. No em dashes. No tatweel.
- Score speed against the Core Web Vitals field thresholds (LCP 2.5s, INP 200ms, CLS 0.1, at
  the 75th percentile), not a judgment. Report INP, never the retired FID.
- Indexation baseline is index,follow plus self-canonical plus 200, sitemaps carry only
  canonical 200 URLs, and an indexed-versus-canonical gap above roughly 30 percent is flagged.
- Verify hreflang for both ar and en, reciprocal and correctly coded. RTL must render correctly.
- Do not assume a finding you could not verify. Flag missing access as an open item.
- Do not adopt or wire a crawl or speed tool without approval, per CLAUDE.md principle 3.

## How it connects

Feeds the seo hub's technical_findings[], consumed by build (stream 6) and read alongside the
on_page_specs[]. Internal and technical, so it runs its skill eval for completeness; any
customer-facing string it touches (for example a rendered title) still runs the copy and brand
gates, per `runtime/verification.md`.
