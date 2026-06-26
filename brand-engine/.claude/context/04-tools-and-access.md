# 04-tools-and-access: the solo stack and the MCP strategy

Stable reference. No tool is adopted without a build-vs-buy pass (`skills/build-vs-buy-eval`)
and your approval. Approved tools are reflected in `settings.json`. Open items are flagged,
not guessed. Reasoning is always allowed; any send, publish, write, or spend is a human-gate
action (you), governed by `runtime/send-safeguards.md`.

## The solo stack (session-provided MCPs)

Connected through the Claude Code harness, not spun up by `.mcp.json`. This is the default
toolset for a one-person brand. Each maps to the agents and streams that use it:

| Tool | Used by | What it does | Streams / commands |
|---|---|---|---|
| Canva | creative-director, designer, web-designer | generate designs, brand templates, export, brand kits | 3 creative, 6 web, `/build-visual` |
| Descript | creative-director, organic-social | edit video/audio by text, transcripts, repurpose clips | 3 creative, creator content, feeds `/ingest` |
| Gmail | lifecycle-architect, pr-comms | email and outreach as drafts (you review), email-to-Substack publish | 7 lifecycle, `/substack-post` |
| Google Drive | all | read source material, store outputs | `/ingest`, outputs |
| Google Calendar | organic-social, content-marketer | content calendar and cadence | organic, creator |
| GitHub | web-designer, conversion-engineer | ship/manage a static site or portfolio (Pages), version the engine | 6, `/build-website`, `/build-portfolio` |
| WebSearch / WebFetch (built-in) | research-scout, competitor-analyst | web research and page fetch | 2 strategy, 8 monitoring |

Firecrawl stays available as an optional `.mcp.json` server for heavier crawls (set
`FIRECRAWL_API_KEY`); the built-in WebSearch/WebFetch are the default.

## Stream-to-tool map (how a solo run executes)

- 1 brief intake, 2 strategy: reasoning + WebSearch/WebFetch (research, competitor scan).
- 3 creative: creative-director briefs, designer executes in Canva; video via Descript.
- 4 copywriting: reasoning only (copywriter-en primary).
- 5 build/launch (paid): deferred. `paid-build-engineer` and `performance-marketer` stay
  reasoning-only (plans, not spend) until you opt into paid ads.
- 6 conversion path: web-designer + conversion-engineer build to WordPress (REST API) or
  GitHub Pages. Event tracking is light (GA4 via WebFetch or manual) until you adopt analytics.
- 7 lifecycle: lifecycle-architect drafts in Gmail (and email-to-Substack); WhatsApp deferred.
- 8 monitoring, 9 reporting: reasoning + WebFetch (pull analytics); no warehouse needed solo.

## Candidates to adopt (build-vs-buy first, then your sign-off)

- WordPress (REST API or an MCP) for `/manage-site` write access: needs the site URL and an
  application password; writes stay human-gated.
- An image-generation MCP and a video-generation MCP for `/build-visual` and creator content.
  Higgsfield is already researched: `references/maharat/2026-06-higgsfield-generative-tool-research.md`.
- A Substack API path (the default is email-to-Substack via Gmail).
- Scale-later: meta-ads, google-ads, GA4, BigQuery, Stripe, Search Console, Ahrefs/Semrush,
  ASO tools. All preserved as candidates; adopt when the brand needs paid, a store, or a warehouse.

## Maharat-profile tools (preserved, not enabled)

The original engine adopted Firecrawl, Blotato, Ortto (email send), an email/WhatsApp platform,
and a read-only Meta Ads wrapper (`scripts/meta_ads_mcp.py`). These are preserved for the
archived maharat profile and documented in `settings.json` `_maharat_profile_tools`. For solo
use, Descript supersedes Blotato and Gmail supersedes Ortto. Re-enable them only to run a
maharat-profile campaign. Research lives under `references/maharat/`.
