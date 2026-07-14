# TOOLING.md — Capability Probe Results
Run date: 2026-07-14 · Environment: Claude Code remote session (managed container)

## Probe results

| Tool | Status |
|------|--------|
| node | v22.22.2 |
| python3 | 3.11.15 |
| curl | 8.5.0 |
| ripgrep | present |
| bs4 / requests / lxml | installed during run |
| playwright | 1.56.1 + pre-installed Chromium at /opt/pw-browsers/chromium |
| FIRECRAWL_API_KEY | MISSING - Tier 3 unavailable |

## Network constraint (material to this run)

Direct HTTPS to `asanhoury.com` is **blocked by this environment's outbound
network policy** (proxy answers 403 to CONNECT; WebFetch also returns 403).
Tier 1 (curl) and Tier 2 (headless render of the live site) were therefore
impossible against the live domain. This is an environment policy limit, not
a site problem.

## Acquisition route actually used

The Claude Design project `portfolio` (debb232a-fc2f-4599-b1c5-5c236ad2b840),
owned by the user, was imported via the Claude Design MCP (DesignSync tool):

- `uploads/asanhoury-2026.html` — full snapshot of the current site build
  (71,555 chars). Saved to `raw/html/asanhoury-2026.import.html`.
- `uploads/ahmed-portfolio.html` — earlier dark-theme site build
  (59,228 chars). Saved to `raw/html/ahmed-portfolio.import.html`.
- `cases-data.js` — the project's own declared "source of truth" for case
  study data (14 case studies).
- 15 case-study / extract markdowns under `uploads/` (Canonical, Mindvalley,
  Goodwall, PAYD, Agiliux, Falcon, early career, testimonials, analytics
  extracts, full-folder-scan JSON).

Both HTML snapshots were rendered locally with Playwright + Chromium
(file:// URLs, scripted scroll to fire reveal animations) for screenshots and
text extraction — Tier 2 equivalent, applied to the imported snapshots.

## Tier ladder disposition

| Tier | Status | Note |
|------|--------|------|
| 1 — static fetch | BLOCKED | proxy policy 403 on asanhoury.com |
| 2 — headless render | ADAPTED | run against imported HTML snapshots, not live URL |
| 3 — Firecrawl | UNAVAILABLE | no API key (moot — domain blocked anyway) |
| 4 — vision | USED for verification only | screenshots compared against DOM text |

## Caveat

Because the live site could not be fetched, this run assumes
`uploads/asanhoury-2026.html` in the design project is the same build that is
deployed at asanhoury.com. Its meta description and content match the site's
stated positioning. If the live site has drifted from this snapshot,
re-verify against production when network access permits.

## Raw source custody

Verbatim originals of all `uploads/*.md` sources remain in the Claude Design
project itself (which is the canonical archive for this run); they were read
via DesignSync `get_file` and are re-fetchable at any time. Local copies:
the two HTML builds (raw/html/), 4 screenshots (raw/screens/), and extracted
text + tokens (extracted/).
