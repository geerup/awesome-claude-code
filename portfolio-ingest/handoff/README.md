# Portfolio Project - Read Me First
Produced 2026-07-14 · Claude Code session (portfolio import + rebuild)

## Start here

| What | Where |
|------|-------|
| **The new site, draft R3** | `rebuild/index.html` - open this first |
| **The Numbers page (50 verified stats)** | `rebuild/stats.html` - linked from the site nav |
| Full-page renders of both | `rebuild/screens/` |
| Proof imagery used by the site | `rebuild/assets/` |

Draft R3 implements the editorial spine: hero with three fully-sourced
numbers + portrait, five ranked case studies (each with inline charts,
outcome tables carrying baseline/window/source, and real proof imagery),
a nine-item archive, a deliberately held /lab wing, six on-record
recommendations, speaking and press, contact. 26 visible NEEDS_HUMAN
chips mark exactly what still needs the owner.

## The evidence layers (in order of authority)

1. `handoff/adjudications-2026-07-14.md` - owner-supplied verified stats
   sheet + role brief (master.json 2026-04-18); overrides everything below.
2. `handoff/projects.json` - the content model: 14 cases, every metric
   with provenance and confidence. Source of truth for site copy.
3. `uploads/*.md` + `cases-data.js` - the original source documents.
4. `handoff/live/` - the live asanhoury.com (WordPress) scrape: 24 pages
   of copy, 57 media files, drift report. NOTE: files marked .ILLUSTRATIVE
   are generated mockup charts, not analytics - never use as proof.

## The audit trail

- `handoff/GAPS.md` - the skeptical-hiring-manager audit (read §0 first)
- `handoff/live/live-drift-report.md` - live site vs sources, 10
  contradictions L1-L10, and the standing decision
- `handoff/EXTRACTION_LOG.md` - how everything was acquired and verified
- `handoff/design-brief.md` + `handoff/narrative/` - the spine and 14
  case narratives feeding the build
- `handoff/canonical-role-job-listing.md` - the Canonical role restated
  as a JD (internal framing artifact; not a real listing)

## Open decisions for the owner

1. Positioning: draft ships "social, content, organic growth"; the
   AI-native/agentic thesis is held until /lab has a showable artifact
   (the Maharat agentic-systems documentation is the named seed).
2. LinkedIn URL: /in/ahmed-el-sanhoury (stats sheet) vs /in/asanhoury
   (site) - confirm one.
3. The NEEDS_HUMAN chips on the canvas - mostly proof links and a few
   unstated baselines.

## Legacy files (pre-dating this run, kept as-is)

`Portfolio.html`, `Work Highlight.html`, `Case Study.html`, `Apple Style
Portfolio.html`, `Portfolio-standalone.html`, `portfolio.css`,
`case-study.css`, `cases-data.js`, `image-slot.js`, `screenshots/` - the
earlier build iterations. The rebuild supersedes them but they remain the
verbatim source record alongside `uploads/`.
