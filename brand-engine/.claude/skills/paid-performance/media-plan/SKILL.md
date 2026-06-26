---
name: media-plan
description: Plan the paid channel mix and budget split for paid performance. Use to set the channel mix across Meta, Google, TikTok, and YouTube, allocate the brief budget across channels, and lay out the flighting and schedule across the campaign window. Triggers on "media plan," "channel mix," "budget split," "budget allocation," "flighting," "paid schedule." Sub-skill of paid-performance, owned by performance-marketer.
---

# Media Plan (paid-performance sub-skill)

Produces the channel mix, the budget split, and the flighting that fill the `channels`,
`budget_split`, and `flighting` fields of the `media-plan-package`. It decides where the
brief's budget goes across Meta, Google, TikTok, and YouTube, and when. It never invents the
budget total, and it never spends.

Owner: performance-marketer. Mode: reasoning. The build is handed to `paid-build-engineer`
(stream 5), who stages it paused for the human gate.

## When to use

- A media plan is needed before any campaign is built or any budget is committed.
- The orchestrator dispatches paid performance and the channel mix is not yet fixed.

## Inputs

- The `strategy-artifact` (stream 2): segments, the angle, channel_plan, success_metric.
- The active `briefs/` file: the total budget, the campaign window and schedule, geo (GCC,
  primary Saudi), the objective, and the offer.

If the total budget or the campaign window is absent from the brief, stop and ask. Do not
invent a budget total, a per-channel amount, or a date. The budget is split from the brief
total, never assumed.

## The channel set

Plan across these four, selecting only those that fit the objective and the audience:

1. Meta (Instagram focus, Facebook secondary): primary for the GCC audience and retargeting.
2. Google (Search and Demand Gen): intent capture and broad prospecting.
3. TikTok: short-form reach to the younger end of the 18 to 35 audience.
4. YouTube: video reach and consideration.

A channel is included only when its role is justified against the angle and the
success_metric. An excluded channel is recorded with the reason, not dropped silently.

## Steps

1. Confirm the total budget, the campaign window, the schedule, and geo from the brief. If any
   is missing, stop and ask.
2. Select the channels that fit the objective and audience. State each channel's role.
3. Allocate the budget across the selected channels as a split of the brief total. Show each
   channel's amount and its share. The shares sum to the brief total, no more.
   State the funnel-stage allocation explicitly: the awareness, consideration, and conversion
   share of the budget, sourced from or confirmed against the brief objective. A common field
   split of about 20 percent awareness, 30 percent consideration, 50 percent conversion is a
   reasoning anchor only, never an assumed value: growth objectives tilt the split upper funnel,
   efficiency objectives tilt it lower funnel. The funnel-stage shares still sum to the brief
   total. If the brief objective does not imply a tilt, state the assumption as an open item and
   confirm it, do not invent one.
4. Name the budget-level decision per channel: whether the budget sits at the campaign level
   (CBO, campaign budget optimization) or the ad-set level (ABO, ad-set budget optimization),
   with the reason. Tie it to the test-then-scale path: ABO for controlled testing, where each
   ad set holds its own budget, then CBO to scale once a winner is proven. Record the chosen
   level so the build template can carry it. The amounts still trace to the brief total.
5. Lay out the flighting: the schedule and pacing across the campaign window, including any
   ramp, sustain, or pulse phases, and a learning phase allowance per channel.
6. Tie every channel and every split to the success_metric and the brief target.
7. Hand the channel mix, the budget split, and the flighting to the hub for the
   `media-plan-package`, and on to `paid-build-engineer` for the paused build.

## Output

Fills three fields of the `media-plan-package`:

```
channels       the selected channels, each with its role and the excluded ones with reasons
budget_split   per-channel amount and share, summing to the brief total
flighting      the schedule, pacing, and phases across the campaign window
```

## Verification gates

- Skill eval (this file's `evals/evals.json`) for structure, the budget-from-brief rule, and
  the four-channel coverage.
- The plan advances through the hub: `brand-qa-reviewer` on any in-platform copy, then the
  human gate authorizes spend, per `runtime/verification.md`.

## Hard rules

- The budget total and every per-channel amount trace to the brief. Missing, stop and ask.
  Never invent a budget.
- The plan never spends and never launches. The build is staged paused by paid-build-engineer.
- Spend is authorized only at the human gate, per launch and per campaign.
- No accreditation claims, no fundraising, roadmap, or unannounced plans.
- No em dashes, no tatweel, Western numerals only.
