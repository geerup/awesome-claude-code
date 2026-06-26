# Audience and Bidding

Internal artifact. Owned by performance-marketer. Fills the audiences and bid_strategy fields
of the media-plan-package. The target comes from the brief and is never assumed. The plan never
spends; the build is staged paused by paid-build-engineer.

## Envelope

- campaign_id:
- produced_by: performance-marketer
- stream: paid-performance (plans for stream 5 build)
- status: draft | qa-passed
- brief_refs: (target, geo, offer consumed from the brief)

## Brief inputs (confirm before planning, stop and ask if any is missing)

- target (CPA, ROAS, or as the brief sets it):
- geo (GCC, primary Saudi):
- success_metric (from the strategy-artifact):
- conversion-path optimization events available (from stream 6, e.g. submit, confirm):

If the target is missing, stop and ask. Never assume a target CPA or ROAS.

## Audience strategy (per channel, mapped to segments)

| Channel | Layer | Audience definition | Segment served | Funnel stage | Data dependency |
|---|---|---|---|---|---|
|  | Prospecting |  |  | Cold |  |
|  | Retargeting |  |  | Warm |  |
|  | Lookalike or similar |  |  | Cold |  |

Retargeting and lookalike layers depend on the conversion-path events being live. Any audience
the data cannot yet support is recorded as an open item, never invented. No audience derives
from personal or sensitive data exposed in a URL parameter.

## Bid strategy (per channel, chosen to chase the brief target)

| Channel | Bid strategy | Optimization event | Why (tied to the target and success_metric) |
|---|---|---|---|
|  |  |  |  |

The optimization event aligns to the conversion-path events. Never optimize toward an event the
tracking plan does not fire.

## Open items

- Anything unresolved (target not set, retargeting audience not yet sized, optimization event
  not yet firing, platform access not granted).

## Handoff

This plan hands to the hub for the media-plan-package, then to paid-build-engineer (stream 5),
who stages the structure paused. Spend is authorized only at the human gate, per launch and per
campaign.
