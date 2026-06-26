# Store Creative and Experiments

Internal and customer-facing artifact. Owned by aso-specialist. Fills the creatives, experiments,
and reviews_response_policy parts of the aso-package. Generated images stay text-free; Arabic and
English overlays are added in the build. Each experiment changes one variable. Publishing and
experiment launches are gated behind the human gate.

## Envelope

- campaign_id:
- produced_by: aso-specialist
- stream: aso
- status: draft | qa-passed
- brief_refs: (markets, store locales, campaign window consumed from the brief)
- success_metric (from the strategy-artifact):

## Screenshot and preview video direction (text-free generation)

| Asset | Store | Locale | Benefit shown | Segment served | Overlay slot (added in build) | Dimensions / safe area |
|---|---|---|---|---|---|---|
| Screenshot 1 |  |  |  |  |  |  |
| Screenshot 2 |  |  |  |  |  |  |
| Preview video |  |  |  |  |  |  |

Generated frames are text-free. Overlays (Arabic primary, English) are added in the build by the
designer. Visual constants: #141414, #1A1A1A, emerald #009975. Premium, uncluttered. Western
numerals only in any rendered text.

## Store A/B experiments (one variable each)

| Experiment | Store | Hypothesis | Single variable changed | Metric (tied to success_metric) | Read window | Decision rule |
|---|---|---|---|---|---|---|
|  | App Store (PPO) |  |  |  | up to 90 days, up to 3 treatments |  |
|  | Google Play |  |  |  | minimum 7 days (full weekly cycle) |  |

Read window: Google Play store listing experiments run a minimum of 7 days to cover a full weekly
cycle. Apple PPO runs up to 90 days and tests up to 3 treatments against the original. One asset
per test. Do not read a result before the window closes. Launching an experiment is a gated action
behind the human gate.

## Custom Product Pages (App Store, up to 70)

| CPP | Segment served | Screenshots / previews (text-free, overlay in build) | Promotional text (Arabic primary, English, up to 170 chars) | Assigned keywords | Traffic served (organic / paid) |
|---|---|---|---|---|---|
|  |  |  |  |  |  |

Workflow: run PPO to find the winning creative, then deploy the winner as a CPP for the segment
that responded best, with its assigned keyword set. Each CPP follows the text-free generation and
overlay-in-build rule, the visual constants, and Western numerals. Publishing or assigning a CPP is
a gated action behind the human gate.

## Reviews and ratings response policy

| Review theme | On-brand response (Arabic primary, English) | Action |
|---|---|---|
| Positive |  | Templated reply |
| Feature request |  | Templated reply, log |
| Bug |  | Escalate to owner |
| Refund or billing |  | Escalate to owner |
| Data or privacy concern |  | Escalate to owner |
| Safety or legal |  | Escalate to owner |

Never expose a reviewer's personal data in a public reply. Never imply accreditation. Never name an
instructor without confirmation. Plain, empowering, never defensive.

## Open items

- Anything unresolved (locale not confirmed, store access not granted, asset awaiting design-qa,
  experiment tool not approved, CPP keyword set or segment mapping unconfirmed).

## Handoff

Route creative to creative-director and the designer for execution and design-qa. Hand the
direction, experiment plan, and reviews policy to the hub for the aso-package. Nothing publishes or
launches without the human gate.
