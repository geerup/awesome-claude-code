# 00-start-here: orientation

Read this first if you are new to the engine. It points you at the rest. It is background and
orientation, not the build spec. The build spec is `runtime/` plus the skills and SOPs.

## What this is

A reusable, profile-parameterized engine for building a personal brand and career, run with
Claude. Hand it a brief and the same workflows produce approval-ready assets, copy, websites,
visuals, content, and outreach, behind a human gate (you). It was adapted from a campaign-agnostic
marketing engine built for Maharat, which is preserved intact as the archived `maharat` profile.

## The map of this folder

- `CLAUDE.md` (root of `.claude/`): the always-loaded operating rules. Start there.
- `context/`: stable facts, the single source of truth for the active profile. Not run data.
  - `00-start-here.md`: this file.
  - `active-profile.md`: which profile is active (me). `profiles/`: the profile bundles.
  - `01-brand-brief.md`: who the brand is, the audience, the offers, the goals.
  - `02-objective-and-design.md`: what we build and the design principles.
  - `03-workflow-map.md`: the 9 streams along one funnel and how they hand off.
  - `04-tools-and-access.md`: the solo stack and the MCP strategy.
  - `brand-voice.md`: how the brand sounds and looks. A gate checks against it.
  - `subjects/`: the marketable entities (you = `me`, services, ventures, research targets),
    each with a verified-claims fact file. The asset library is `subjects/_IMAGE-CATALOG.md`.
- `.agents/brand-context.md`: the brand foundation the 29 brand-building skills read first.
- `briefs/`: runtime inputs, one file per run. `_TEMPLATE-personal-brief.md` and `starters/`.
- `agents/`: the team. `_AGENTS-INDEX.md` is the roster.
- `skills/`: the knowledge. The 29 brand-foundation skills (`_BRAND-FOUNDATION.md`), the 9 funnel
  hubs, the channel hubs, the QA gates, plus `asset-ingest`, `career-narrative`, `subject-marketing`.
- `runtime/`: the conductor layer. How the agents and skills run together as a swarm.
- `sops/`: the long-form standard operating procedures for the deepest streams.
- `commands/`: slash commands (see below).
- `references/`, `outputs/`: research and generated artifacts (the Maharat history is under `*/maharat/`).

## The first build

Start with the foundation, then a first asset:
1. `/brand-context` and `/ingest` (mine your own material) to fill the foundation.
2. `personal-brand`, then a starter brief from `briefs/starters/` matching your emphasis
   (career, services, creator, or founder).
3. Run it: a LinkedIn profile + posts, a Substack post (`/substack-post`), a portfolio
   (`/build-portfolio`), or a site (`/build-website`).

## Slash commands

`/brand-context`, `/ingest`, `/mine-subject`, `/new-campaign` (a.k.a. new asset), `/build-visual`,
`/build-website`, `/build-portfolio`, `/manage-site`, `/substack-post`, `/research`.

## How to run

The orchestrator reads the active brief, loads `runtime/SWARM.md` and the roster, resolves what
streams the run needs, and dispatches each to its owner. Every customer-facing asset passes the
quality gate. Every execution path ends at the human gate. Nothing sends or publishes without you.

House rule, everywhere: English-first, no em dashes, verified claims only; Western numerals / no
tatweel only when Arabic is in scope.
