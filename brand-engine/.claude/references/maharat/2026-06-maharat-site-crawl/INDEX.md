# Maharat site crawl, 2026-06-04

Raw research archive of https://www.maharat.com captured with the Firecrawl MCP.
Owner: research-scout (Firecrawl is its tool). This is reference material for streams 2 and
8, not customer-facing output. Nothing here is approved copy. Any reuse of this content in a
campaign asset still runs the quality gates and the human gate.

## Envelope

- source: https://www.maharat.com
- captured: 2026-06-04
- method: firecrawl_map to discover URLs, then firecrawl_scrape per page (markdown, main content only)
- tool: Firecrawl MCP, owner research-scout, listed in settings.json enabledMcpjsonServers
- status: raw-capture. Not qa-passed, does not cross a stream boundary as-is.
- locales: en and ar. Arabic pages are RTL.
- scope: page text only. Video, audio, and image assets are referenced in the text, not downloaded.

## Guardrail notes

- Instructor names here are already public on the live site. This archive is not a
  confirmation source for new claims. The catalog status check in
  context/instructors/_CATALOG.md still governs any instructor marketing.
- Legal pages (privacy, terms, cookies) are captured as reference. They are the live site's
  own text, not legal advice.

## Structure

pages/<locale>/<path>.md mirrors the live URL path. Each home page is pages/<locale>/index.md.
The captured-files tree and per-page status are listed at the end of this file after the run.

## Planned inventory (from firecrawl_map)

### English
- /en (home)
- /en/plans
- /en/about-us
- /en/get-in-touch
- /en/library
- /en/library/acting
- /en/library/business
- /en/library/cooking
- /en/library/music
- /en/library/design-style
- /en/class
- /en/class/acting
- /en/class/business
- /en/class/cooking
- /en/class/design-style
- /en/class/music
- /en/class/acting/kosai-khauli-teaches-acting
- /en/class/business/rahma-riad-teaches-building-a-career-in-the-digital-age
- /en/class/business/toufic-kreidieh-teaches-building-and-growing-your-business
- /en/class/cooking/salam-dakkak-teaches-levantine-cooking
- /en/class/design-style/bassam-fattouh-teaches-makeup
- /en/class/music/ragheb-alama-teaches-music-and-performance
- /en/library/music/ragheb-alama-teaches-music-and-performance
- /en/library/acting/kosai-khauli-teaches-acting
- /en/library/acting/ragheb-alama-teaches-music-and-performance
- /en/library/acting/rahma-riad-teaches-building-a-career-in-the-digital-age
- /en/library/business/toufic-kreidieh-teaches-building-and-growing-your-business
- /en/library/business/rahma-riad-teaches-building-a-career-in-the-digital-age
- /en/library/cooking/salam-dakkak-teaches-levantine-cooking
- /en/library/design-style/bassam-fattouh-teaches-makeup
- /en/library/design-style/bassam-fattouh-teaches-bridal-makeup
- /en/library/design-style/cedric-haddad-teaches-personal-styling
- /en/playlist/the-making-of/the-story-behind-rahmas-biggest-hits
- /en/cookies-policy
- /en/privacy-policy
- /en/terms-and-conditions

### Arabic
- /ar (home)
- /ar/plans
- /ar/about-us
- /ar/get-in-touch
- /ar/class
- /ar/class/acting
- /ar/class/business
- /ar/class/cooking
- /ar/class/design-style
- /ar/class/music
- /ar/class/acting/kosai-khauli-teaches-acting
- /ar/class/business/rahma-riad-teaches-building-a-career-in-the-digital-age
- /ar/class/business/toufic-kreidieh-teaches-building-and-growing-your-business
- /ar/class/cooking/salam-dakkak-teaches-levantine-cooking
- /ar/class/design-style/bassam-fattouh-teaches-makeup
- /ar/class/music/ragheb-alama-teaches-music-and-performance
- /ar/library/cooking
- /ar/library/music/ragheb-alama-teaches-music-and-performance
- /ar/library/acting/kosai-khauli-teaches-acting
- /ar/library/acting/ragheb-alama-teaches-music-and-performance
- /ar/library/acting/rahma-riad-teaches-building-a-career-in-the-digital-age
- /ar/library/business/toufic-kreidieh-teaches-building-and-growing-your-business
- /ar/library/business/rahma-riad-teaches-building-a-career-in-the-digital-age
- /ar/library/cooking/salam-dakkak-teaches-levantine-cooking
- /ar/library/design-style/bassam-fattouh-teaches-makeup
- /ar/library/design-style/bassam-fattouh-teaches-bridal-makeup
- /ar/library/design-style/cedric-haddad-teaches-personal-styling
- /ar/playlist/facing-challenges/fear-is-the-greatest-source-of-strength
- /ar/cookies-policy
- /ar/privacy-policy
- /ar/terms-and-conditions

## Captured files

- captured: 2026-06-04
- pages saved: 67 of 75 attempted, markdown with main content only, under pages/
- total size: about 880 KB
- layout: pages/<locale>/<path>.md, section hubs as .../index.md, site root as pages/index.md
- full per-URL status: crawl-manifest.csv
- method: scripted firecrawl v2 scrape (the same adopted Firecrawl tool, run in bulk against the API so page content went straight to disk, not through chat). First pass basic proxy, retry pass stealth proxy plus AE location and an 8s render wait.

### Not captured (8), with the live response Firecrawl received

These are the site's own responses to the crawler across basic, stealth, US and AE proxies. They are recorded, not faked:

- /en/about-us, /ar/about-us: HTTP 500 every attempt. Real pages in the sitemap, the route returns a server error to the crawler. Capture via an in-region or authenticated browser session if the text is needed.
- /en/get-in-touch, /ar/get-in-touch: HTTP 500, same pattern.
- /en/playlist/the-making-of/the-story-behind-rahmas-biggest-hits, /ar/playlist/facing-challenges/fear-is-the-greatest-source-of-strength: HTTP 500. The playlist hub links resolve, the individual playlist-detail route errors for the crawler.
- /en/class, /ar/class: HTTP 404. The bare class hub is not a page. The live taxonomy is /<locale>/library and /<locale>/class/<category>/<instructor>, both captured.

### Notes on captured content

- The library hub pages (pages/<locale>/library/index.md) carry the full current class catalog and the full playlist catalog (about 25 playlists), the richest single inventory on the site.
- Listing and category hubs include the site's repeated playlist carousel markup, kept as-is per the raw-archive principle.
- Pricing shown on /plans at capture time, recorded as live-site reference and not a brief input: 6-month membership $50 (about $8.33/mo), 12-month $75 (about $6.25/mo), single classes $30, bridal makeup $40, certificates of completion included.
- Instructors visible on the live site beyond the older roster include Elda Choucair (Teaches Marketing) and Cedric Haddad (Teaches Personal Styling). Names are public on the site, the catalog status check in context/instructors/_CATALOG.md still governs any instructor marketing.

## Follow-up crawl (the rest), 2026-06-04

A second pass mapped the site (firecrawl map plus links found inside the saved pages) and
found 133 unique in-site paths. After subtracting the 67 already saved, 66 remained. All 66
were attempted. Per-URL detail: crawl-manifest-rest.csv.

Result: 4 saved, 62 not retrievable by the crawler. Total archive is now 71 pages.

- Saved (4): the EN and AR class pages for bassam-fattouh-teaches-bridal-makeup and
  cedric-haddad-teaches-personal-styling.
- HTTP 500, systematic (53): every playlist page, EN and AR, both the playlist hub pages and
  the playlist detail pages, plus about-us and get-in-touch. Tried basic proxy, stealth proxy,
  AE location, and an 8s render wait. A 500 is the origin returning an error to an anonymous
  crawler, not a render timeout, so render and wait options do not change it. The likeliest
  cause is that these routes are member-gated or error server-side for non-browser clients.
- HTTP 404 (9): the four coming-soon library categories per locale (science-tech, sports,
  wellness, writing) and the bare /class hubs. Not real pages.

Note on coverage: the playlist catalog itself (every playlist title, lesson count, duration,
and link, about 25 playlists) is already captured inside the library hub pages
(pages/<locale>/library/index.md). What is missing is each playlist's own detail page, the
lessons inside it, which is what returns 500. To capture those, the realistic path is an
authenticated or in-browser session, not anonymous scraping. Flag if you want that pursued.
