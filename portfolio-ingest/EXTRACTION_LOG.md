# EXTRACTION_LOG.md — Verification Pass
Run date: 2026-07-14

## Page-level extraction

| source | tier used | body chars | assets found | visible in screenshot but missing from text | confidence |
|--------|-----------|-----------|--------------|---------------------------------------------|------------|
| uploads/asanhoury-2026.html (site snapshot) | Import via Design MCP + local Playwright render | 15,431 | 0 external images (all-CSS design; one "Add portrait →" placeholder slot) | none found — screenshot content matches DOM text 1:1 | 95 |
| uploads/ahmed-portfolio.html (earlier build) | Import via Design MCP + local Playwright render | 16,025 | 0 external images | none found | 95 |
| asanhoury.com (live) | NONE — blocked by environment network policy (403 CONNECT) | — | — | — | 0 (not acquired) |

## Screenshot verification notes

- First screenshot attempt (no scrolling) produced blank sections below the
  hero: the site uses IntersectionObserver reveal animations. Re-ran one rung
  higher with a scripted scroll-to-bottom pass before capture. Second pass
  rendered all 8 sections. This was an extraction bug, now fixed — logged per
  Phase 2 instructions.
- Full-page desktop (1440x900) and mobile (390x844) captures exist for both
  builds under raw/screens/.
- Google Fonts (Instrument Serif / Geist; Inter / Fraunces) could not load in
  the sandboxed render, so screenshots show fallback serif/sans faces. Layout,
  color, and copy are unaffected. Live typography tokens are captured
  verbatim in extracted/design-tokens.json from the CSS source.
- Marquee proof strip ("2.81M Organic Audience * 21× MQL Growth * ...") is
  duplicated in the DOM for the CSS loop — text extract shows it twice;
  counted once for content purposes.
- No numbers are baked into images anywhere in either build (all metrics are
  DOM text), so Tier 4 vision transcription was not needed for any field.

## Data-file extraction (via Design MCP get_file, verbatim, confidence 100 unless noted)

| file | role in run |
|------|-------------|
| cases-data.js | Declared "source of truth" for 14 case studies (client, years, numbers, challenge, what, results, quote) |
| uploads/testimonials.md | 12 recommendations w/ names, dates, relationships; site rotation table |
| uploads/canonical-social-from-scratch.md | Canonical social/demand-gen case |
| uploads/canonical-ubuntu-summit.md | Summit earned-media case (Meltwater + Sprout tables) |
| uploads/canonical-20-years-ubuntu.md | 20 Years of Ubuntu campaign case |
| uploads/canonical-data-ai-masters.md | Data & AI Masters event case |
| uploads/canonical-analytics-extract.md | Month-by-month audience trackers, platform YoY tables (Sprout exports) |
| uploads/mindvalley-social-7m-followers.md | Mindvalley social growth case |
| uploads/mindvalley-influencer-zero-cost.md | Influencer/KOL programme case |
| uploads/mindvalley-pr-2-8m.md | PR case ($2.8M EMV, 69% reply rate) |
| uploads/mindvalley-seo-870-percent.md | SEO case (14K→122K) |
| uploads/goodwall-growth-machine.md | Goodwall growth case |
| uploads/payd-fintech-growth.md | PAYD FinTech case |
| uploads/agiliux-organic-pipeline.md | Agiliux InsurTech case |
| uploads/falcon-agency-40-brands.md | Falcon agency era (client snapshots) |
| uploads/early-career-foundation.md | 2010-2014 foundation era |
| uploads/all-projects-names-extract.md | Complete named-entity extract (campaigns, clients, tools, speaking) |
| uploads/full-folder-scan-extract.json | Metric-level provenance: maps headline numbers to original PPTX/XLSX source files |

Not fetched (machine-generated duplicates of the above, low value):
`uploads/*.md-extract.json`, `uploads/*-extract.json-extract.json`.
Not fetched (superseded site builds): `Portfolio.html`, `Portfolio-standalone.html`,
`Apple Style Portfolio.html`, `Case Study.html`, `Work Highlight.html`,
`portfolio.css`, `case-study.css`, `tweaks-*.jsx`, `image-slot.js`,
`screenshots/0*-check.png` (project's own render checks).

## Cross-source mismatch hunt (Phase 2 requirement)

Mismatches found between site copy and underlying data files — carried into
GAPS.md for adjudication rather than silently fixed (per rule 4):

1. Mindvalley YouTube baseline: site says "125K → 1M"; case sources say
   "300K → 1M".
2. Canonical audience: site hero "2.81M (Sprout · Apr 2025)" vs CV entry
   "3M+ audience" on the same page; analytics extract shows end-2024 at
   2,709,827 and Apr 2025 at 2,813,262; cases-data.js still says "2.58M".
3. PAYD "−28% CAC" appears only on the site CV — no source file contains it.
4. "$5M+ enterprise pipeline influenced" (hero + CV) — no source file
   contains it.
5. "100M+ annual cross-platform impressions (2024)" — plausible from platform
   tables (FB alone 162M in 2024) but no source file states the aggregate.
6. Canonical end date: site CV "2022 — 2024" vs recommendations dated May-Jul
   2025 saying "3 years, 2022 until 2025" and analytics tracked through
   April 2025.
7. "Etisalat" in site CV brand list — absent from the named-clients extract.
8. Falcon-era conflations: site "+22% ROAS" matches sources; but site omits
   that "45% CAC reduction" and "+38% conversion" are agency-aggregate
   claims, not personally attributed campaigns (source: falcon md "Falcon
   Agency — Aggregate Scale").
