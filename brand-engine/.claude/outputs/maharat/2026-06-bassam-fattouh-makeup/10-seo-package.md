# seo-package: Bassam Fattouh Teaches Makeup

Produced by seo-specialist from the strategy-artifact. Reasoning only. It specs and briefs; it never publishes
site changes or writes final copy. Arabic and English, RTL-correct, hreflang-aware. Technical findings draw on
the live site crawl captured this session (`references/2026-06-maharat-site-crawl/`).

## Common envelope

- campaign_id: 2026-06-bassam-fattouh-makeup
- produced_by: seo-specialist
- stream: SEO (acquisition channel)
- status: qa-passed (specs and briefs; no site change published)
- open_items: some class and playlist detail routes return server errors to crawlers (see technical findings),
  which suppresses their indexation. Owner and fix to confirm with the site team.

## keyword_map (clusters and intent, AR primary and EN, priority)

| Cluster | Intent | Sample queries (AR / EN) | Priority |
|---|---|---|---|
| Learn makeup step by step | how-to, learning | تعلم المكياج خطوة بخطوة / learn makeup step by step | high |
| No-makeup-makeup and natural look | how-to | مكياج طبيعي بدون مكياج / no makeup makeup tutorial | high |
| Foundation for veiled women and mature skin | how-to, inclusive | فاونديشن للمحجبات / foundation for mature skin | medium |
| Smokey and color makeup | how-to, advanced | مكياج سموكي / smokey eye tutorial | medium |
| Bassam Fattouh class | branded, high-intent | صف بسام فتوح / Bassam Fattouh masterclass | high |
| Online makeup course Arabic | commercial | كورس مكياج اونلاين / online makeup course arabic | high |

Branded queries are subject to the instructor confirmation at the gate before any public optimization ships.

## on_page_specs

- The landing surface (from the web-design-package): one H1 bound to the makeup-class promise, descriptive title
  and meta in AR and EN, semantic headings per section, internal links to the plans page and related classes,
  Video and Course-style structured data limited to true, published facts (20 chapters, 2h 53m, free intro
  chapter). No accreditation or rating claim that is not real.
- hreflang: AR and EN reciprocal tags on the class and landing routes; RTL correctness verified for AR.

## technical_findings (from the live crawl, 2026-06-05)

- The class detail pages for this campaign return 200 and are indexable (AR and EN captured cleanly).
- However, the broader crawl found systematic server errors (HTTP 500) on every playlist detail route and on
  about-us and get-in-touch, and 404s on the bare /class hubs and the coming-soon library categories
  (`references/2026-06-maharat-site-crawl/`). Server-error routes do not index and waste crawl budget. This is a
  real technical-SEO issue for the site, surfaced here for the site team. It does not block the campaign landing
  page, which is healthy.
- Recommendation: fix or correctly redirect the 500 and 404 routes; confirm the class and landing routes are in
  the sitemap with valid hreflang and RTL. Owner to confirm.

## content_briefs (handed to content-marketer and the copywriters)

- One pillar plus a small cluster around the high-priority intents (learn makeup step by step, no-makeup-makeup,
  foundation for veiled women and mature skin), Arabic-first, each linking to the free intro and the plans page.
  Briefs only; copy is written by copywriter-ar and copywriter-en and runs the gates.

## Handoff

Hands content briefs to content-marketer and the on-page and hreflang specs to conversion-engineer and the
web-design layer. No site change is published without the human gate.
