---
name: kickoff-scope
description: Scopes a validated campaign by choosing the entry point (paid acquisition vs owned audience), deciding which of the 9 streams run, and laying out the funnel path through them. Use after brief-validate passes, to set the run plan before stream 2 strategy. Triggers on "scope this campaign," "which streams run," "what is the funnel path," "paid or owned," "where do we start the pipeline."
---

# Kickoff Scope (stream 1 sub-skill)

Turns a validated brief into a run plan: the entry point, the active streams, and the funnel
path. This is the map the orchestrator dispatches against. It is reasoning, not execution.

Owner: strategy-lead. Mode: reasoning. Gate: skill eval only (internal artifact).

## When to use

After `brief-validate` returns ready to scope (or ready with flagged assumptions). Run it to
set which streams are in this campaign and the order they execute.

## Inputs

- The brief validation report from `brief-validate`.
- The active `briefs/` file (entry_point and channels; the Background and context section,
  key_message, and reporting_cadence carry forward as context for the scope, even when only
  entry_point and channels drive the path choice).
- `runtime/stream-ownership.md` (the two entry-point pipelines and the stream owners).

## Steps

1. Read the entry point from the brief. Confirm it with the orchestrator. Two paths exist:
   - Entry point A, paid acquisition: full pipeline, streams 1 to 2, then 3 and 4 in
     parallel, then 5, 6, 7, 8, 9.
   - Entry point B, owned audience: starts at stream 7 logic, no paid build. Pipeline is
     stream 1, then 2 (segment the non-payers), then 4 (email copy and subject lines), then
     7 (the flow), then 6 (the page or gate the email points to, if any), then 8, then 9.
2. Decide which streams actually run for this campaign. Stream 3 creative runs only if a
   message needs a visual asset. Stream 5 paid build is skipped for owned audience.
3. Lay out the funnel path: from entry through the signup gate (email or whatsapp) into
   lifecycle, then monitoring and reporting. Name the owner of each active stream from
   `runtime/stream-ownership.md`.
4. Carry forward the ASSUMPTION and OPEN ITEM lists so the scope inherits them. A scope built
   on an OPEN ITEM (for example an unconfirmed gate platform) names what it blocks.
5. Record the result in the kickoff scope template.

## Output

A completed `templates/kickoff-scope.md`: entry point, active streams with owners, the
funnel path, what is out of scope, and the inherited open items.

## How this connects to the contract and gates

- Handoff: the entry point chosen here becomes the entry point in the `channel_plan` field of
  the `strategy-artifact` (see `runtime/handoff-contract.md`). The active-streams list is what
  stream 2 frames the channel plan around.
- Verification: internal artifact, skill eval only, per `runtime/verification.md`.

## Hard rules

- Do not invent a budget, target, or schedule to make a path look complete. A path blocked on
  a MISSING needed variable stays flagged.
- Pick the entry point with the orchestrator. Do not silently assume paid vs owned.
- No em dashes, no tatweel, Western numerals only. Empowering framing, no accreditation claims.
