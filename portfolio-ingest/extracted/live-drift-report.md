# Live Site Drift Report + Decision
Run date: 2026-07-14 (network policy opened for asanhoury.com mid-session)

## Headline finding

**The live asanhoury.com is NOT the asanhoury-2026.html snapshot.** It is a
WordPress site (Certy theme, All in One SEO, Elementor-era markup) with a
different design, different positioning, different copy, and content the
design-project sources do not contain. The Phase 1 caveat ("assumes the
snapshot matches production") is now resolved: it does not. The design
project holds the NEXT site (in progress); the live WP site is the CURRENT
public site.

Everything scraped: 24 pages (raw/live/), 61 of 62 media originals
(raw/live/media/, 153MB; one 246MB video skipped, URL in media-urls.json),
per-page text copy (extracted/live-copy/), media-to-page map
(raw/live/media-map.json).

## What the live site adds (new evidence)

1. **Real proof assets that resolve NEEDS_HUMAN items:**
   - YouTube Gold Play Button award photo (team holding Gold + Silver buttons)
   - Genuine YouTube analytics screenshots: flagship Jim Kwik video at
     12,679,453 views, channel at 1.1M subscribers, "Up Next" domination
   - Mindvalley 1M-subscriber celebration video (28MB mp4)
   - Foundr article screenshots (6) - capture filename encodes the URL:
     foundr.com/how-to-get-subscribers-on-youtube (confirm live)
   - Ubuntu Summit photos (DSC00016/DSC00461) + Summit 2024 key visual
   - Ubuntu Mascots film (27MB), Summit 2024 highlight reel (246MB, not
     downloaded - URL preserved)
   - Falcon-era campaign artifacts: 4 Motul Facebook creatives, Heinz
     Doy-Pack launch video, Behance case images, DrawIt iOS app-store video
   - Goodwall campaign creatives + Instagram install ads
   - Mindvalley SEO team photo; GrowthHackers logo; TEDx/Reuters/ITC/
     Forward Leading client logos
2. **New cases not in the design project:** Cybersecurity Awareness Month
   (Canonical, 7-part video series, 2024), Ubuntu Desktop Evolution, Motul
   Moments, Draw It with Heinz, plus a Goodwall page variant.
3. **A new on-record testimonial:** Gloria Quintanilla Manzanares, Head of
   Communications, Canonical (live Summit page) - not in testimonials.md.
   Also different Thibaut and Mauro quotes than the LinkedIn set.
4. **New Summit metrics:** Reddit mentions 4x (2022-2024), LinkedIn carousel
   10.2% avg ER, 75 content assets per cycle, "trended in Latvia".
5. **Contact details:** phone +372 5360 1193 public; languages incl. Estonian.

## Caution: illustrative charts

The four "Visual Highlights" charts on the Summit page
(engagement_rate_growth, video_views_growth, reddit_mentions_growth,
format_performance_mock) are GENERATED illustrations, not analytics exports -
one is titled "Illustrative of 2023-2024 Trends" and one filename says
"mock". They must not be presented as proof. Real exports exist in the
design-project sources for the same claims.

## New contradictions (added to the GAPS ledger)

| # | Item | Live WP site | Design-project sources |
|---|------|--------------|------------------------|
| L1 | YouTube baseline | 125,000 ("built over eight years"); "tripled in six months" | case md: 300K; cases-data.js: 300K → 1M |
| L2 | SEO result | "870% (110K) in 11 months" | 14K → 122K |
| L3 | MQL growth | "5x MQL growth" (hero Key Results) | Salesforce 36 → 785 = 21.8x |
| L4 | Mindvalley followers | "5M+ followers" (CV) | 7M+ (case sources and site) |
| L5 | Launches | "23+ product launches" | 20+ |
| L6 | Agency era | 2013 - 2017 | 2014 - 2017 |
| L7 | Media era | 2008 - 2013 (Insight, Cairo West, TPA Media) | 2010 - 2014 |
| L8 | Canonical engagement | "47% engagement rate growth; 14% YoY video view increase" | 1.3% → 5.18% ER; +188% video views YoY (Summit) |
| L9 | Goodwall | "churn -15%" (new claim) | not in any source |
| L10 | Agiliux | "20% quarterly sales growth" (new claim) | not in any source |

## DECISION (per run instruction: "decide once you have them")

1. **Numbers:** the analytics-backed projects.json remains the single source
   of truth for the rebuild. The live WP copy is the least reliable of the
   three copy variants - it contradicts named exports in both directions
   (understates 21.8x as "5x", overstates 122K as... uses 110K, keeps the
   125K YouTube baseline the sources dispute). Where live contradicts an
   export, the export wins; the ten contradictions above are logged for the
   owner to adjudicate, not silently resolved.
2. **Images:** adopt the live media as the rebuild's proof layer -
   REAL artifacts only (award photo, platform screenshots, event photos,
   campaign creatives, Foundr captures). The four illustrative charts are
   excluded from proof use. Wired into rebuild R2: hero portrait, Summit
   photo + key visual (case 02), Gold Play Button + channel screenshot
   (Mindvalley archive row), Foundr article title updated with probable URL.
3. **New cases:** Cybersecurity Awareness Month and Ubuntu Desktop Evolution
   are archive candidates (Canonical era); Motul and Heinz DrawIt fold into
   the Falcon-era row as linkable artifacts. Not promoted to top-5 - none
   carries an outcome metric that survives the GAPS floor test.
4. **Testimonial:** Gloria Quintanilla Manzanares quote (already public on
   the live site) added to the rotation candidates.
5. **Positioning:** unchanged - the live site's "Strategic Marketing Leader |
   Growth Architect" line is a third variant; the rebuild keeps the
   evidence-backed "social, content, organic growth" until the owner rules.
