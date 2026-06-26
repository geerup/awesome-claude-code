# Technical SEO audit template

One findings list per audit, plus an hreflang map and RTL checks for the priority pages. All
example values are illustrative only. Replace them. Do not assume a finding you could not
verify. Flag missing access as an open item. Western numerals only, no em dash, no tatweel.

## Findings

```
- area:          crawlability | speed | indexation | sitemaps | hreflang | rtl | canonical
  issue:         <what is wrong, in one plain line>
  severity:      high | medium | low
  affected_urls: [<url>, <url>]
  fix:           <the concrete change the build stream implements>
```

## Core Web Vitals thresholds (field data, 75th percentile)

Score each priority page against these. INP has replaced FID, do not report FID.

```
- metric: LCP   target: at or under 2.5s     measured: <value>   pass | fail
- metric: INP   target: at or under 200ms    measured: <value>   pass | fail
- metric: CLS   target: at or under 0.1       measured: <value>   pass | fail
```

## Indexation baseline and gap

```
baseline:        index,follow + self-canonical + 200 status for each key template
sitemap_rule:    sitemaps carry only canonical 200 URLs (no redirects, noindex, non-canonical)
indexed_count:   <indexed URLs>
canonical_count: <canonical 200 URLs>
gap:             <percent difference>   investigate when above roughly 30 percent
cadence:         quarterly audit
```

## Hreflang map (priority pages)

```
- page:          <url>
  alternates:
    - lang: ar   href: <ar url>
    - lang: en   href: <en url>
  reciprocal:    yes | no
  notes:         <coding issue, missing alternate, region code check>
```

## RTL checks (priority pages)

```
- page:          <url>
  direction:     correct | broken
  numerals:      western | eastern-found
  mixed_content: safe | breaks (AR + EN + numerals)
  notes:         <where direction or numerals break, if any>
```

## Open items

```
- <access not granted, data source missing, or finding not verifiable>
```

## Illustrative example (replace before use)

```
findings:
  - area:          hreflang
    issue:         Arabic pages declare no en alternate, reciprocity broken.
    severity:      high
    affected_urls: [/skills-guide, /skill-paths]
    fix:           Add reciprocal ar and en hreflang tags with correct language codes.

hreflang_map:
  - page:          /skills-guide
    alternates:
      - lang: ar   href: /ar/skills-guide
      - lang: en   href: /en/skills-guide
    reciprocal:    no
    notes:         en alternate missing on the ar page.

rtl_checks:
  - page:          /ar/skills-guide
    direction:     correct
    numerals:      western
    mixed_content: safe
    notes:         none

open_items:
  - Search console access not granted, indexation count unverified.
```

## Checklist before handoff

- Crawlability, speed, indexation, sitemaps, hreflang, RTL, canonical all checked.
- Core Web Vitals scored against LCP 2.5s, INP 200ms, CLS 0.1 at the 75th percentile. No FID.
- Indexation baseline (index,follow, self-canonical, 200) stated, sitemaps only canonical 200
  URLs, indexed-versus-canonical gap above roughly 30 percent flagged, quarterly cadence noted.
- Hreflang verified for ar and en, reciprocal and correctly coded.
- RTL direction and Western numerals verified on priority Arabic pages.
- Every finding has a severity and a concrete fix.
- No assumed findings. Missing access is an open item.
- No em dash, no tatweel, Western numerals only.
- No crawl or speed tool adopted without approval.
