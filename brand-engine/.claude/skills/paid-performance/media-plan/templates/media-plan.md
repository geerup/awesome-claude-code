# Media Plan

Internal artifact. Owned by performance-marketer. Fills the channels, budget_split, and
flighting fields of the media-plan-package. Every channel and split traces to the brief and
the success_metric. The plan never spends; the build is staged paused by paid-build-engineer.

## Envelope

- campaign_id:
- produced_by: performance-marketer
- stream: paid-performance (plans for stream 5 build)
- status: draft | qa-passed
- brief_refs: (budget total, schedule, geo, offer consumed from the brief)

## Brief inputs (confirm before planning, stop and ask if any is missing)

- total budget:
- currency:
- campaign window (start to end):
- schedule or cadence:
- geo (GCC, primary Saudi):
- objective:
- success_metric (from the strategy-artifact):
- target (CPA, ROAS, or as the brief sets it):

If the total budget or the campaign window is missing, stop and ask. Do not invent a value.

## Channel mix

Select only the channels that fit the objective and audience. State each channel's role.
Record excluded channels with the reason.

| Channel | In or out | Role | Primary segment served | Why (tied to angle / success_metric) |
|---|---|---|---|---|
| Meta (Instagram focus) |  |  |  |  |
| Google (Search, Demand Gen) |  |  |  |  |
| TikTok |  |  |  |  |
| YouTube |  |  |  |  |

## Budget split (sums to the brief total, nothing invented)

| Channel | Amount | Share of total | Pacing (daily or lifetime) |
|---|---|---|---|
|  |  |  |  |
|  |  |  |  |
| Total |  | 100% |  |

The total equals the brief budget. No channel amount is assumed.

## Funnel-stage allocation (sourced from or confirmed against the brief objective)

State the awareness, consideration, and conversion share of the budget. A field default of
about 20 percent awareness, 30 percent consideration, 50 percent conversion is a reasoning
anchor only, never an assumed value: growth tilts upper funnel, efficiency tilts lower funnel.
The shares sum to the brief total. If the objective does not imply a tilt, record it as an open
item and confirm it.

| Funnel stage | Share | Amount | Channels mapped | Tied to objective |
|---|---|---|---|---|
| Awareness |  |  |  |  |
| Consideration |  |  |  |  |
| Conversion |  |  |  |  |
| Total | 100% |  |  |  |

## Budget-level structure (CBO vs ABO, per channel)

Record whether the budget sits at the campaign level (CBO, campaign budget optimization) or the
ad-set level (ABO, ad-set budget optimization), with the reason. Tie it to the test-then-scale
path: ABO for controlled testing, CBO to scale a proven winner. The build template carries this.

| Channel | Budget level (CBO or ABO) | Stage (test or scale) | Why |
|---|---|---|---|
|  |  |  |  |

## Flighting and schedule

| Phase | Window | Channels active | Pacing note (ramp, sustain, pulse) |
|---|---|---|---|
| Learning |  |  |  |
| Sustain |  |  |  |
|  |  |  |  |

Note any learning-phase allowance per channel and any blackout or peak dates from the brief.

## Open items

- Anything unresolved (target not set, platform access not granted, mobile mapping to confirm).

## Handoff

This plan hands to paid-build-engineer (stream 5), who stages the structure paused. Spend is
authorized only at the human gate, per launch and per campaign.
