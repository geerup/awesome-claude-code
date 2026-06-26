---
name: paid-campaign-build
description: Stage a paid acquisition campaign for stream 5, paused and approval-ready. Use when QA-passed creative and copy must be assembled into a campaign, ad sets, ads, targeting, placements, budget, and schedule, all staged paused with each ad set mapped to a creative and copy variant. Triggers on "build the campaign," "stage the ads," "prepare the paid launch," "assemble the ad sets." Sub-skill of 05-build-launch, owned by paid-build-engineer, execution mode and gated.
---

# Paid Campaign Build (stream 5 sub-skill)

Assembles a QA-passed `creative-package` and `copy-package` into a staged, paused paid campaign
structure that fills the `staged_structure` and `checklist` fields of the `paid-launch-package`.
Meta and Instagram focus, Google and YouTube secondary. Everything is built paused. It never
spends and never flips anything live. Follows `sops/05-build-launch-paid.md`.

Owner: paid-build-engineer. Mode: execution (gated).

## When to use

- The brief is paid acquisition and creative and copy are QA-passed.
- You need a build-ready, paused campaign structure before the human gate.

## Inputs

- The QA-passed `creative-package` (stream 3) and `copy-package` (stream 4).
- The active `briefs/` file: budget, bid strategy, target CPA or ROAS, schedule, geo, objective.
- The tracking plan from conversion-engineer (Pixel or CAPI events, UTMs), stream 6.

If the budget, target, schedule, or geo is missing from the brief, stop and ask. Never assume a
budget, a bid, or a target. If the creative-package or copy-package is not qa-passed, return it.

## Steps

1. Validate both package envelopes: right campaign_id, status at least qa-passed, required
   fields present. If incomplete, return.
2. Confirm budget, bid strategy, target, schedule, and geo from the brief. A missing variable is
   a stop-and-ask, not an assumption.
3. Build the structure: campaign, ad sets, ads, targeting, placements, budget, schedule. Build
   everything paused.
4. Map each ad set to one creative variant and one copy variant by id, so the read is clean
   later. No ad set carries free copy written here.
5. Apply the tracking plan: Pixel or CAPI events, UTMs, naming convention. No personal or
   sensitive data in any URL parameter.
6. Run the pre-launch checklist: pixel firing, UTMs, naming, budget cap, end date. A failing
   check blocks the package from the gate.
7. Hand the structure and checklist to the hub for assembly into the `paid-launch-package`.

## Output

Fills the `staged_structure` and `checklist` fields of the `paid-launch-package` (see
`runtime/handoff-contract.md`):

```
staged_structure  campaign, ad sets, ads, targeting, placements, budget, schedule (paused)
checklist         pre-launch checks and their pass state
```

The hub adds spend_on_approval and flips_live. Wrapped in the common envelope (campaign_id,
produced_by, stream, status, qa, open_items, brief_refs). See
`templates/paid-campaign-structure.md`.

## How it connects to the verification gates

- Skill eval (this file's `evals/evals.json`) for structure, the paused state, and the variant
  mapping.
- Operational verification per `runtime/verification.md`: the pre-launch checklist must fully
  pass before the package can reach the gate. A failing operational check blocks it.
- `compliance-privacy-check` on the tracking and UTMs.
- The human gate is the only thing that authorizes spend and go-live. A human flips it live.

## Hard rules

- Everything is staged paused. The build never spends and never flips anything live on its own.
- Every budget, bid, target, schedule, and geo traces to the brief. Nothing assumed. Missing
  means stop and ask.
- Each ad set maps to one creative variant and one copy variant by id. Copy is never invented
  here.
- No personal or sensitive data in URL parameters or tracking. Never imply accreditation.
- In-platform copy uses Western numerals and no em dashes. No tatweel.
