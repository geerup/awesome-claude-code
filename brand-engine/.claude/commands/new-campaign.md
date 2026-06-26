---
description: Start a new run (asset or campaign). Creates a brief from the template, then hands it to the orchestrator to compose and run the swarm up to the human gate.
---

# /new-campaign (also /new-asset)

Stand up a new run, whether it is a single asset (a post set, a page, a CV) or a full campaign.
The brief is the only per-run input; everything else is the reusable engine. This command
creates the brief, then starts the run. Nothing sends or publishes.

## What to do

1. Ask for the essentials if not given: run name, the goal emphasis (career, services, creator,
   or founder), the objective, the surface (the concrete asset), and the offer or ask if any. If
   a value is unknown, mark it ASSUMPTION. Never invent it. Confirm `primary_language` (default
   English; set Arabic only if this run needs it).
2. Copy `briefs/_TEMPLATE-personal-brief.md` to `briefs/YYYY-MM-short-name.md` (or start from a
   `briefs/starters/` file matching the emphasis). The filename is the run_id. Fill every field
   you have; flag the rest ASSUMPTION or OPEN ITEM.
3. Make sure the brand foundation exists: if `.agents/brand-context.md` is still TODO, run
   `/brand-context` (and `/ingest`) first so strategy and copy have a real brand to work from.
4. Load `CLAUDE.md`, `context/brand-voice.md`, `agents/_AGENTS-INDEX.md`, `runtime/SWARM.md`,
   and `runtime/stream-ownership.md`.
5. Hand the brief to the orchestrator. It resolves the entry point and composes the run:
   - A single asset: just the streams that asset needs (e.g. strategy -> copy -> QA -> gate).
   - A full campaign: the pipeline across the streams in scope.
6. The swarm runs each stream through its owner, wraps every generation step in the quality
   gate, and assembles an approval-ready package. It stops at the human gate (you).

## Rules

- Never hard-code or invent an offer, price, target, or a claim about yourself. Those are brief
  inputs or verified claims (context/subjects/me.md).
- Every customer-facing asset passes its skill eval, then english-copy-qa (arabic-copy-qa only
  when Arabic is in scope), then brand-qa.
- Nothing sends, publishes, or spends. The run ends at the human gate with a package for you.
- No em dashes; Western numerals / no tatweel only when Arabic is in scope.

$ARGUMENTS
