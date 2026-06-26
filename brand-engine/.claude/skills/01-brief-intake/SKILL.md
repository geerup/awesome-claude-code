---
name: 01-brief-intake
description: Hub for stream 1 brief intake, owned by strategy-lead. Use at the very start of a campaign run to turn a raw brief into a validated, scoped starting point before any strategy work. Routes to brief-validate (check the brief against the template, flag every ASSUMPTION and OPEN ITEM) and kickoff-scope (decide entry point, which streams run, and the funnel path). Triggers on "validate the brief," "is the brief complete," "scope this campaign," "which streams run," "where do we start."
---

# 01 Brief Intake (hub)

Stream 1. The front door of every run. It takes the active `briefs/` file and produces a
clean, validated, scoped starting point so stream 2 strategy never builds on a brief with
silent gaps. This is internal reasoning work. Nothing here is customer-facing.

Owner: strategy-lead. Mode: reasoning. Gate: skill eval only (internal artifact, no
arabic-copy-qa or brand-qa unless customer copy appears).

## When to use

Run this first, before stream 2, on any new or changed brief. If the brief changes
mid-run, run it again. The two sub-skills are sequential: validate first, then scope.

## Sub-skills (routing)

- `brief-validate`: validates the active brief against `briefs/_TEMPLATE-campaign-brief.md`,
  field by field. Flags every ASSUMPTION and every OPEN ITEM, and stops-and-asks on any
  missing variable the campaign needs. Use when you need to know whether the brief is safe
  to act on. This is the first step, always.
- `kickoff-scope`: scopes the campaign once the brief is validated. Decides the entry point
  (paid acquisition vs owned audience), which of the 9 streams run, and the funnel path
  through them. Use after brief-validate passes, to set the run plan.

Route: a fresh brief goes to `brief-validate`. Once validated (or validated with flagged
ASSUMPTIONs the brief explicitly allows drafting against), it goes to `kickoff-scope`.

## Inputs

- The active `briefs/` file (the only per-campaign input).
- `context/01-brand-brief.md` and `context/brand-voice.md` for stable facts.
- `runtime/stream-ownership.md` for the entry-point pipelines.

## Output

Two internal artifacts that feed strategy-lead's stream 2 work:
- a brief validation report (from brief-validate),
- a kickoff scope (from kickoff-scope).

Neither crosses a stream boundary as a handoff-contract artifact on its own. They are the
grounding strategy-lead carries into the `strategy-artifact` it produces in stream 2.

## How this connects to the contract and gates

- Handoff: this stream feeds stream 2 (`02-strategy-planning`), which emits the
  `strategy-artifact` defined in `runtime/handoff-contract.md`. The entry point chosen here
  becomes the `channel_plan` entry point there.
- Verification: per `runtime/verification.md`, stream 1 is internal, so each sub-skill runs
  its own skill eval for structure and completeness only. No brand or Arabic gate applies
  unless a sub-skill output carries customer-facing copy.

## Hard rules

- Never invent an offer, price, target, segment size, or schedule. A missing variable the
  campaign needs is a stop-and-ask, not an invention.
- Empowering framing, never deficit-framed. English-first for any drafted customer text.
- No em dashes, no tatweel, Western numerals only, no accreditation claims.
