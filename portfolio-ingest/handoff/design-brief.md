# Design Brief - Claude Design Handoff (Phase 6, pending approval)

Target project: "portfolio" (debb232a-fc2f-4599-b1c5-5c236ad2b840) - existing,
user-owned, canEdit confirmed.

## What gets attached

- narrative/00-portfolio-spine.md (structure + ranked cases)
- narrative/canonical-social.md, canonical-ubuntu-summit.md,
  canonical-20-years.md, canonical-data-ai.md, mindvalley-influencer.md
  (ranked top five) + 9 supporting narratives
- extracted/projects.json (single source of truth for every number)
- extracted/design-tokens.json (verbatim tokens from both existing builds)
- raw/screens/*.png (4 full-page renders, desktop + mobile, both builds)

## Design system seed (from extracted/design-tokens.json)

Current build (asanhoury-2026): paper #EFE9DC / ink #17140F / vermilion
accent #D2401E / moss #2E4A2F / night #0E0C08; Instrument Serif (display),
Geist (sans), Geist Mono; editorial-print aesthetic, 1240px max width.
Earlier build (ahmed-portfolio): dark navy #070C1B with teal #10CFAA and
gold #FFB800; Inter + Fraunces. The 2026 paper/vermilion direction is the
newer and stronger of the two. [Inference: confirm which direction to keep.]

## Build order (per spine)

1. Hero: positioning line + three-number proof strip + single CTA
2. Ranked case studies (5), each in hook → context → tension → mandate →
   decisions → execution → outcome → proof → reflection order
3. /work archive (9 remaining projects, compact)
4. /lab wing: HOLD - zero qualifying artifacts in source (see GAPS.md §1);
   render a visible NEEDS_HUMAN placeholder, not filler
5. Recommendations (6 on-record, rotation per testimonials.md)
6. Speaking & press (links NEEDS_HUMAN)
7. Contact

## Hard rules carried into the canvas

- Every word traces to projects.json or user-approved lines
- Numbers ship with baseline + window inline
- Unsourced site metrics ($5M+ pipeline, -28% CAC, six-figure ARR, 100M+
  impressions) do NOT ship until the user sources them - GAPS.md §2
- Visible NEEDS_HUMAN placeholders instead of confident invented copy
- Hyphens only; no em or en dashes
- Show the user the canvas before polishing
