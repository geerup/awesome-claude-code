# SOP: Paid performance

Paid performance stream. Owners: performance-marketer (strategy and plan) plus
paid-build-engineer (execution, gated). Mode: reasoning for the plan, execution (gated) for
the build. The strategist turns a validated brief and strategy into an approval-ready media
plan across Meta, Google, TikTok, and YouTube. The builder stages the campaign paused. A
human flips it live. The engine never spends.

Budgets, targets, and schedules are brief inputs. They are never assumed. This stream does
not run for the owned-audience lapsed-contact flow (no paid build).

No em dashes, Western numerals in any in-platform copy, no accreditation claims.

---

## Trigger

A brief with `entry_point: paid acquisition` (or a channel_plan that includes paid), with a
QA-passed strategy-artifact, creative, and copy.

## Inputs

- The `strategy-artifact` (stream 2): segments, the angle, offer framing, channel_plan,
  success_metric.
- The brief: total budget, target CPA or ROAS, schedule, geo (GCC, primary Saudi Arabia), the
  offer. If any is missing, stop and ask. Never assume a budget or a target.
- Approved `creative-package` (stream 3) and `copy-package` (stream 4), both QA-passed.
- The tracking plan from conversion-engineer (Pixel or CAPI events, stream 6).

## Steps

1. Confirm the budget, target, schedule, and geo from the brief. If any is missing, stop and
   ask. Nothing in the plan is invented to fill a gap.
2. performance-marketer plans the channel mix across Meta, Google, TikTok, and YouTube, mapped
   to the segments and the angle. Each channel carries its role in the funnel and the share of
   the budget it serves.
3. Split the budget from the brief across channels and phases. The split traces to the brief
   total; it never exceeds or invents it.
4. Set the audience and bid strategy per channel: targeting, placements, and the bid approach
   that serves the brief target CPA or ROAS. Plan the in-flight optimization rules (scale or
   cut conditions) that monitoring (stream 8) will read.
5. Assemble the `media-plan-package` and hand it to paid-build-engineer. The strategist plans;
   it does not stage or spend.
6. paid-build-engineer stages the campaign per `sops/05-build-launch-paid.md`: campaign, ad
   sets, ads, targeting, placements, budget, schedule, all paused. Map each ad set to a
   creative and a copy variant. Apply the tracking plan, UTMs, and naming convention.
7. Run the pre-launch checklist: pixel firing, UTMs, naming, budget cap, end date. A failing
   check blocks the package from the gate.
8. Assemble the `paid-launch-package` and route to the human gate. State the maximum spend if
   approved and one plain sentence of what going live does.

## Output

A `media-plan-package` (channel mix, budget split, audience and bid strategy, optimization
rules), then the `paid-launch-package` (see `runtime/handoff-contract.md`):
- staged_structure: campaign, ad sets, ads, targeting, placements, budget, schedule (paused).
- checklist: the pre-launch checks and their pass state.
- spend_on_approval: the maximum spend this incurs if approved, with currency and window.
- flips_live: one plain sentence of what going live does.

## Quality bar

- Every budget, split, bid, and target traces to the brief. Nothing assumed.
- The media plan maps to the strategy-artifact segments, angle, and success_metric.
- The structure is staged paused. No spend, no publish, no go-live before the gate.
- Pre-launch checklist fully passes: pixel fires, UTMs and naming consistent, budget cap and
  end date set (pre-launch checklist plus human gate, per `runtime/verification.md`).
- In-platform copy is QA-passed, uses Western numerals, and has no em dashes or accreditation
  implication.

## Example output (shape, not real values)

```
media-plan-package:
  channel_mix: [ {channel, role, budget_share}, ... ]   shares sum to the brief total
  budget_split: per channel and phase, traced to the brief total
  audience_and_bidding: per channel targeting, placements, bid strategy to the brief target
  optimization_rules: scale or cut conditions for stream 8
paid-launch-package:
  staged_structure: campaign / ad sets / ads, all paused
  checklist: pixel PASS, UTMs PASS, naming PASS, budget cap PASS, end date PASS
  spend_on_approval: "Up to [brief budget] over [brief window] if approved."
  flips_live: "Sets the staged campaign live to the brief geo and audience."
```

## Review owner

Ahmed, at the human gate. Approval is per launch and authorizes exactly the stated spend and
go-live, nothing more. A human flips the campaign live. The engine never does.

House rule: facts come from `context/`, variables come from the active brief. When both are
silent on something needed, stop and ask. Do not invent a value.
