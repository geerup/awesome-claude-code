# 00-start-here: orientation

Read this first if you are new to the engine. It points you at the rest. It is background
and orientation, not the build spec. The build spec is `runtime/` plus the skills and SOPs.

## What this is

A reusable, campaign-agnostic agentic marketing engine, run with Claude. Hand it a campaign
brief and the same workflows produce approval-ready marketing output, behind a human gate.

## The map of this folder

- `CLAUDE.md` (root of `.claude/`): the always-loaded operating rules. Start there.
- `context/`: stable facts, the single source of truth. Not campaign data.
  - `00-start-here.md`: this file.
  - `01-company-brief.md`: who Maharat is, the audience, the money model, the owned audience.
  - `02-objective-and-design.md`: what we are building and the design principles.
  - `03-workflow-map.md`: the 9 streams along one funnel and how they hand off.
  - `04-tools-and-access.md`: the existing stack and the MCP strategy.
  - `brand-voice.md`: how Maharat sounds and looks. A gate checks against it.
- `briefs/`: runtime inputs, one file per campaign. The only per-campaign input.
- `agents/`: the team. `_AGENTS-INDEX.md` is the roster.
- `skills/`: the knowledge, grouped by stream. Each stream is a hub skill that routes to
  sub-skills. Every skill has a SKILL.md, an `evals/evals.json`, and `templates/`.
- `runtime/`: the conductor layer. How the agents and skills run together as a swarm.
- `sops/`: the long-form standard operating procedures for the deepest streams.
- `commands/`: slash commands, `/new-campaign` and `/research`.
- `references/`: research readouts (for example the email and WhatsApp platform research).
- `outputs/`: generated artifacts per campaign.

## The first build

The non-payer email flow to the roughly 18,000 owned non-paying contacts. Owned audience,
zero media cost, fast and low-risk. It enters the funnel at stream 7 (lifecycle), not at
acquisition. The active brief is `briefs/2026-06-nonpayer-email.md`.

## How to run

The orchestrator reads the active brief, loads `runtime/SWARM.md` and the roster, resolves
the entry point, and dispatches each stream to its owner. Every customer-facing asset passes
the quality gate. Every execution path ends at the human gate. Nothing sends without Ahmed.

House rule, everywhere: no em dashes, no tatweel, Western numerals, empowering framing,
Arabic-first, no accreditation claims.
