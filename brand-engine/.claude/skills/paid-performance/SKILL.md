---
name: paid-performance
description: Hub for paid performance, owned by performance-marketer, the reasoning layer that turns a validated brief and strategy into an approval-ready media plan across Meta, Google, TikTok, and YouTube. Use to plan the channel mix, split the budget from the brief, set the audience and bid strategy, and plan in-flight optimization. Routes to media-plan, audience-and-bidding, and paid-optimization, and assembles the media-plan-package, then hands the build to paid-build-engineer. Triggers on "plan the paid campaign," "media plan," "channel mix," "budget split," "audience and bidding," "bid strategy," "scale or cut," "paid optimization."
---

# Paid Performance (hub)

Owns the planning of paid acquisition: the media plan, the audience and bid strategy, and the
in-flight optimization plan. Owner: `performance-marketer`. Mode: reasoning. This hub does not
build campaigns, does not launch, and never spends. It validates inputs, routes to the right
sub-skill, assembles the `media-plan-package`, and hands the build to `paid-build-engineer`
(stream 5), who stages everything paused for the human gate.

The split is deliberate. Performance-marketer decides what the spend should buy and why,
grounded in the brief. Paid-build-engineer assembles it in-platform, paused. Ahmed at the
human gate authorizes the spend. No agent spends on its own.

## When to use

- A brief with `entry_point: paid acquisition` (or a channel_plan that includes paid).
- The campaign needs a media plan, a budget split, an audience and bid strategy, or an
  in-flight optimization plan.
- The orchestrator dispatches paid performance (per `runtime/stream-ownership.md`).

## Sub-skills (routing)

- `media-plan`: the channel mix across Meta, Google, TikTok, and YouTube, the budget
  allocation taken from the brief, and the flighting and schedule. Use first; it sets where
  the budget goes and when.
- `audience-and-bidding`: the audience strategy and targeting per channel, and the bid
  strategy and optimization event. Use after the channel mix is fixed; it sets who each
  channel reaches and how it bids. Never assumes a target.
- `paid-optimization`: reads live performance against the success_metric and proposes scale,
  cut, and creative-rotation moves. Use once a campaign is live. Every move is a proposal for
  the human gate, never a live action.

Route: media-plan first to fix the channel mix and budget split, then audience-and-bidding
for who and how each channel bids, then paid-optimization once the campaign is live. All three
feed the same `media-plan-package`.

## Inputs

- The `strategy-artifact` (stream 2): segments, the angle, offer framing, channel_plan,
  success_metric.
- The active `briefs/` file: objective, total budget, target CPA or ROAS, schedule, geo
  (the markets the brief sets), the offer, and the campaign window.
- The `creative-package` (stream 3) and `copy-package` (stream 4) when ready, for channel
  routing of variants. Captions and copy are never written here.

If a needed variable is absent from both brief and context, stop and ask. Do not fill the gap
with an invented value. Budget, target CPA or ROAS, and the schedule are brief inputs, never
assumed. Never invent an offer title, the content lineup, a subject name, an offer, a
price, or a target.

## Steps

1. Validate the incoming envelope: right campaign_id, strategy-artifact present with the
   angle, segments, success_metric, and channel_plan, open_items read. If incomplete, return it.
2. Confirm the total budget, target CPA or ROAS, schedule, and geo from the brief. If any is
   missing, stop and ask. Never assume a budget or a target.
3. Route to `media-plan` for the channel mix, the budget split, and the flighting.
4. Route to `audience-and-bidding` for the audience strategy, targeting, and bid strategy per
   channel.
5. Route to `paid-optimization` once the campaign is live, for the read against the
   success_metric and the proposed scale, cut, and creative-rotation moves.
6. Set `success_metric_link`: every channel, budget split, and bid choice traces to the
   strategy-artifact success_metric and the brief target.
7. Assemble the `media-plan-package` and hand the build to `paid-build-engineer` (stream 5).
   The plan authorizes nothing. Spend is gated at the human gate.

## Output: the media-plan-package

```
channels             the channel mix across Meta, Google, TikTok, YouTube, each with its role
budget_split         allocation per channel, taken from the brief total, never invented
audiences            the audience strategy and targeting per channel
bid_strategy         the bid strategy and optimization event per channel
flighting            the schedule and pacing across the campaign window
success_metric_link  how each choice traces to the strategy-artifact success_metric and target
spend_on_approval    the maximum spend the plan implies if approved, with currency and window
open_items           anything unresolved (target missing, platform access, mobile mapping)
```

Wrapped in the common envelope (campaign_id, produced_by, stream, status, qa, open_items,
brief_refs), per `runtime/handoff-contract.md`.

## How this connects to the contract and gates

- Consumes: `strategy-artifact` (stream 2), and `creative-package` plus `copy-package` for
  channel routing.
- Produces: the `media-plan-package`. It hands the build to `paid-build-engineer` (stream 5),
  who stages the structure paused and assembles the `paid-launch-package` for the human gate.
- Gate before advance: skill eval, then `english-copy-qa` or `arabic-copy-qa` on any
  customer-facing copy referenced, then `brand-qa-reviewer`, then the human gate authorizes
  any spend, per `runtime/verification.md` and `sops/05-build-launch-paid.md`.

## Hard rules

- The hub plans and routes; it never builds, never launches, and never spends. The build is
  handed to `paid-build-engineer`, who stages everything paused.
- Spend is a gated action. Nothing spends without the human gate. Approval is per launch and
  per campaign and authorizes exactly the stated spend. Silence is not approval.
- Budget, target CPA or ROAS, schedule, and geo are brief inputs. Missing, stop and ask.
  Never assume a budget or a target.
- Never invent an offer title, the content lineup, a subject name, an offer, a price,
  or a target.
- Never imply a credential or accreditation you do not hold, no fundraising, roadmap, or unannounced plans in any in-platform copy.
- Never put personal or sensitive data in a tracking URL parameter.
- No em dashes, no tatweel, Western numerals only, empowering framing never deficit-framed.
