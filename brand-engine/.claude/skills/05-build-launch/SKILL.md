---
name: 05-build-launch
description: Hub for stream 5 build and launch, owned by paid-build-engineer, execution mode and gated. Use to assemble a paid campaign or email sequence into an approval-ready, staged-and-paused launch package, triggers on "build the campaign," "stage the ads," "build the email sequence," "prepare the launch." Routes to paid-campaign-build and email-sequence-build and produces the paid-launch-package, following sops/05-build-launch-paid.md. Everything is staged paused and never spends or sends; going live is a human-gate decision.
---

# 05 Build and Launch (stream 5 hub)

The entry point for turning approved copy and creative into a built, staged, paused launch.
Owned by `paid-build-engineer`, execution mode and gated. This hub assembles the
`paid-launch-package` defined in `runtime/handoff-contract.md` and stops at the human gate.

## What it routes to

- `paid-campaign-build`: stage the Meta or Google campaign, ad sets, ads, targeting,
  placements, budget, and schedule, all paused. Each ad set maps to one creative variant and
  one copy variant by id. Budgets, bids, targets, schedule, and geo trace to the brief, never
  assumed. Follows `sops/05-build-launch-paid.md`. Fills `staged_structure` and `checklist`.
- `email-sequence-build`: assemble a QA-passed lifecycle flow into the sending platform
  structure: messages, triggers, delays, audience, suppression. Assembled, not sending. Blocked
  on the email and WhatsApp platform OPEN ITEM until the platform is confirmed and approved.

The orchestrator dispatches whichever sub-skill the entry point needs: `paid-campaign-build`
for paid acquisition, `email-sequence-build` for the owned-audience lifecycle flow. The hub
assembles the result into the `paid-launch-package` and states spend_on_approval and flips_live.

## Inputs

- The `copy-package` (stream 4) and `creative-package` (stream 3), both qa-passed.
- The active `briefs/` file: budget, schedule, targeting, the campaign objective.
- `sops/05-build-launch-paid.md`: the build and pre-launch procedure.

## Output: the paid-launch-package

The body shape, exactly as `runtime/handoff-contract.md` defines it:

```
staged_structure  campaign, ad sets, ads, targeting, placements, budget, schedule (paused)
checklist         pre-launch checks and their pass state
spend_on_approval the maximum spend this incurs if approved, with currency and window
flips_live        one plain sentence of what going live does
```

Wrapped in the common envelope (campaign_id, produced_by, stream, status, qa, open_items,
brief_refs).

## How it connects

- Consumes: `copy-package` (stream 4), `creative-package` (stream 3), `lifecycle-package`
  (stream 7) for the email sequence path.
- Produces: `paid-launch-package` (stream 5 -> human gate).
- Gate before advance: the pre-launch checklist (operational verification per
  `runtime/verification.md`), `compliance-privacy-check` on tracking and suppression, then the
  human gate. A failing operational check blocks the package from reaching the gate.

## Hard rules

- Everything is staged paused or assembled-not-sending. The build never spends, never sends,
  and never flips anything live on its own.
- Going live is a human-gate decision, per `CLAUDE.md` and `agents/human-gate.md`. Approval is
  per action and per campaign, never inferred from silence.
- spend_on_approval states the maximum spend if approved, with currency and window. flips_live
  is one plain sentence of what going live does. No hidden spend or send.
- Never invent budget, schedule, targeting, audience, or the sending platform. A missing
  variable is a stop-and-ask. The email and WhatsApp platform OPEN ITEM blocks the sequence
  build until confirmed.
- No personal or sensitive data in URL parameters or tracking. Never imply a credential or
  accreditation you do not hold.
- No em dashes, no tatweel, Western numerals only.
