# SOP 05: Build and launch, paid path

Stream 5. Owner: paid-build-engineer. Mode: execution (gated). Assembles approved creative
and copy into a launch-ready paid campaign structure (Meta and Instagram focus, Google and
YouTube secondary). It stages everything in a paused state and stops at the human gate. It
never spends.

This stream does not run for the owned-audience lapsed-contact flow (no paid build). It is here so
the engine is ready when a paid acquisition campaign is the active build.

No em dashes, Western numerals in any in-platform copy, no accreditation claims.

---

## Trigger

A brief with `entry_point: paid acquisition` that has QA-passed creative and copy.

## Inputs

- Approved `creative-package` (stream 3) and `copy-package` (stream 4), both QA-passed.
- The brief: budget, target CPA or ROAS, schedule, geo (GCC, primary Saudi), offer.
- The tracking plan from conversion-engineer (Pixel or CAPI events, stream 6).

## Steps

1. Confirm the budget, bid strategy, target, schedule, and geo from the brief. If any is
   missing, stop and ask. Never assume a budget or target.
2. Build the structure: campaign, ad sets, ads, targeting, placements, budget, schedule.
   Assemble paused. Map each ad set to a creative variant and a copy variant for clean read
   later.
3. Apply the tracking plan: Pixel or CAPI events, UTMs, naming convention.
4. Run the pre-launch checklist: pixel firing, a live test event verified in Events Manager,
   the conversion event and its conversion location correct, UTMs, naming, budget cap, end date,
   audience geo and demographics confirmed, bid strategy and bid amount confirmed, creative
   spell-check, and captions present on any video. For search: negative keywords present, match
   types set, and ad assets or extensions added. A failing check blocks the package from the
   gate. Bid strategy, bid amount, geo, and demographics each trace to the brief, never assumed.
5. Assemble the `paid-launch-package` and route to the human gate. State the maximum spend if
   approved and one plain sentence of what going live does.

## Output

A `paid-launch-package` (see `runtime/handoff-contract.md`):
- staged_structure: campaign, ad sets, ads, targeting, placements, budget, schedule (paused).
- checklist: the pre-launch checks and their pass state.
- spend_on_approval: the maximum spend this incurs if approved, with currency and window.
- flips_live: one plain sentence of what going live does.

## Quality bar

- Every budget, bid, and target traces to the brief. Nothing assumed.
- The structure is staged paused. No spend, no publish, no go-live before the gate.
- Pre-launch checklist fully passes. Pixel fires, UTMs and naming are consistent, budget cap
  and end date are set.
- In-platform copy uses Western numerals and no em dashes.

## Review owner

Ahmed, at the human gate. Approval is per launch and authorizes exactly the stated spend and
go-live, nothing more. A human flips the campaign live. The engine never does.
