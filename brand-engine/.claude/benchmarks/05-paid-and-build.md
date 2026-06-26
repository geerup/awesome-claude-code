# Benchmark: paid performance and build

Internet benchmark for the Maharat Marketing Engine streams that plan paid acquisition and
build the launch: `skills/paid-performance/` (media-plan, audience-and-bidding,
paid-optimization) and `skills/05-build-launch/` (paid-campaign-build, email-sequence-build).
This doc compares our skills to current, reputable real-world frameworks and lists prioritized
recommendations. It edits no skill file. It is a reference only.

Reviewed June 2026. All recommendations are proposals for the human gate, not adopted changes.

## Sources reviewed (web)

Media plan templates and the planning framework (the 5 Ms):

- [Improvado, Media Planning: Complete Guide to Strategy, Process and Best Practices 2026](https://improvado.io/blog/media-planning-strategy)
- [Oktopost, 7 essentials for a paid media plan with examples](https://www.oktopost.com/blog/paid-media-plan-essentials/)
- [GaleForce Digital, the 5 Ms of a Marketing Media Plan](https://galeforcedigital.com/mastering-the-5-ms-of-a-marketing-media-plan/)
- [Medialister, Free Media Plan Templates](https://medialister.com/blog/media-plan-templates)

Campaign structure (campaign / ad set / ad hierarchy) and naming conventions:

- [Improvado, Marketing Campaign Naming Conventions 2026](https://improvado.io/blog/marketing-campaign-naming-conventions)
- [PPC Hero, The Complete Guide To PPC Naming Conventions](https://ppchero.com/the-complete-guide-to-ppc-naming-conventions/)
- [Supermetrics, Campaign Naming Conventions](https://supermetrics.com/blog/campaign-naming-conventions)
- [AdStellar, Meta Ads Campaign Structure Guide 2026](https://www.adstellar.ai/blog/meta-ads-campaign-structure-guide)

Bidding, budget allocation, learning phase, full-funnel channel mix:

- [Search Engine Journal, How Much Of Your Paid Media Budget For Upper Funnel](https://www.searchenginejournal.com/how-much-of-your-paid-media-budget-should-be-allocated-to-upper-funnel/561581/)
- [SERT Media, Paid Media Budget Allocation Framework](https://sertmedia.com/paid-media-budget-allocation-framework/)
- [Stackmatix, Meta Ads Funnel Strategy: The Complete Guide 2026](https://www.stackmatix.com/blog/meta-ads-funnel-strategy)
- [AGrowth, ABO vs CBO Facebook Ads 2026](https://agrowth.io/blogs/facebook-ads/abo-vs-cbo-facebook-ads)
- [Modern Marketing Institute, Exit the Meta Ads Learning Phase 2026](https://www.modernmarketinginstitute.com/blog/how-to-exit-the-meta-ads-learning-phase-fast-and-start-scaling-profitably-in-2026)

Pre-launch QA and measurement:

- [PPC Hero, The Ultimate Campaign Quality Assurance Checklist 2026](https://ppchero.com/the-ultimate-campaign-qa-checklist/)
- [Pearmill, The ultimate Meta QA checklist for campaign launches](https://pearmill.com/blog/the-ultimate-meta-qa-checklist-for-campaign-launches)
- [WonderAds, Google Ads Campaign Launch Checklist 2026](https://www.wonderads.org/knowledge-base/google-ads-campaign-launch-checklist)
- [Amsive, Designing Defensible Geo Holdout Tests for Incrementality](https://www.amsive.com/insights/data-intelligence/designing-defensible-geo-holdout-tests-for-incrementality-measurement/)

## Best-in-class elements

What strong real-world paid and build practice converges on.

1. Define the work before the channel. The 5 Ms (Mission, Money, Message, Media, Measurement)
   force objective, audience, and message before channel selection, and explicitly name
   Measurement as a first-class plan input, not an afterthought (GaleForce, Improvado).

2. A media plan documents flighting (continuity, flighting, pulsing) and a learning-phase
   allowance per channel, not just a flat split (Improvado, Medialister, Modern Marketing
   Institute).

3. Full-funnel budget allocation by stage. A common starting split is roughly 20 percent
   awareness, 30 percent consideration, 50 percent conversion, tuned by objective (growth tilts
   upper funnel, efficiency tilts lower funnel). Channels are mapped to funnel stage, not chosen
   in isolation (SERT Media, Search Engine Journal, Stackmatix).

4. Explicit hierarchy: Google uses Campaign > Ad Group > Ad, Meta uses Campaign > Ad Set > Ad.
   Plans and builds state which level holds the budget (campaign-level CBO vs ad-set-level ABO)
   (AdStellar, AGrowth).

5. ABO for testing, CBO for scaling. Use ad-set budgets for controlled testing, then move proven
   winners to campaign budgets. Exit the learning phase (about 50 conversions per ad set in 7
   days) before scaling, and raise budgets in small steps (20 to 30 percent every 2 to 3 days)
   to avoid resetting learning (AGrowth, Modern Marketing Institute).

6. Bid-strategy progression. Start on the algorithm-led lowest-cost or maximize-conversions while
   in learning, move to cost cap or target CPA / ROAS once a stable target is established, set
   roughly 10 to 20 percent above the real average CPA (Stackmatix).

7. A structured naming convention across every level: objective, audience, platform, geo,
   product, campaign type, date, in a fixed order with one separator, coded so audience and
   budget names are not exposed (they often leak into UTMs visible in the browser) (Improvado,
   PPC Hero, Supermetrics).

8. A real pre-launch QA checklist that goes beyond ours: conversion tracking firing verified by a
   live test event, budget and bid set as intended, audience geo and demographics correct,
   conversion event and conversion location correct, negative keywords and match types for
   search, ad extensions / assets (sitelinks, callouts, structured snippets) for search, creative
   spell-check and captions on video (PPC Hero, Pearmill, WonderAds).

9. Measurement designed in. Sophisticated advertisers reserve 10 to 15 percent of budget for
   measurement (geo holdout / incrementality, MMM calibration) and design a test (control vs
   holdout geos, 2 to 4 weeks) rather than reading platform-reported conversions alone (Amsive,
   Measured).

## Our coverage

Where our skills already meet the bar, with the files that carry it.

- 5 Ms equivalents are present and brief-driven. Mission and Money map to objective, budget, and
  target confirmed from the brief (`media-plan/SKILL.md` steps 1 to 3,
  `media-plan/templates/media-plan.md` Brief inputs). Message maps to the angle and copy variants
  routed in, never written in this stream (`paid-performance/SKILL.md` Inputs). Media is the
  four-channel mix. Measurement maps to `success_metric_link` and `paid-optimization`.

- Channel mix across Meta, Google, TikTok, YouTube, each included only with a justified role and
  excluded channels recorded with a reason (`media-plan/SKILL.md` The channel set,
  `media-plan/templates/media-plan.md` Channel mix table).

- Budget split that sums to the brief total and never exceeds or invents it, with a per-channel
  share and pacing column (`media-plan/templates/media-plan.md` Budget split table;
  `paid-performance/SKILL.md` Hard rules).

- Flighting with explicit learning, sustain, and pulse phases, plus a learning-phase allowance
  per channel (`media-plan/SKILL.md` step 4, `media-plan/templates/media-plan.md` Flighting).

- Audience strategy in prospecting / retargeting / lookalike layers, each mapped to a segment and
  funnel stage, with retargeting and lookalikes gated on conversion-path events being live
  (`audience-and-bidding/SKILL.md`, `audience-and-bidding/templates/audience-and-bidding.md`).

- Bid strategy per channel chosen to chase the brief target, with the optimization event aligned
  to conversion-path events and never optimizing toward an event the tracking plan does not fire
  (`audience-and-bidding/SKILL.md` steps 3 to 4, Hard rules).

- Campaign / ad set / ad hierarchy is staged in the build, each ad set mapped to one creative and
  one copy variant by id, everything PAUSED
  (`paid-campaign-build/templates/paid-campaign-structure.md`, `paid-campaign-build/SKILL.md`
  step 4).

- A pre-launch checklist exists: pixel firing, UTMs consistent, naming applied, budget cap set,
  end date set, and a failing check blocks the package from the gate
  (`paid-campaign-build/SKILL.md` step 6, `sops/05-build-launch-paid.md` step 4,
  `runtime/handoff-contract.md` paid-launch-package).

- A naming convention is referenced and applied across campaign, ad sets, and ads, with no
  personal or sensitive data in UTMs (`paid-campaign-build/templates/paid-campaign-structure.md`
  Tracking block).

- In-flight optimization (scale, cut, creative rotation) measured against the success_metric,
  every move a proposal for the human gate, with vanity metrics excluded as a result bar
  (`paid-optimization/SKILL.md`, `paid-optimization/templates/paid-optimization-plan.md`).

- Email sequence build with triggers, delays, audience, suppression, assembled not sending,
  blocked on the platform open item (`email-sequence-build/SKILL.md`,
  `email-sequence-build/templates/email-sequence-structure.md`).

## Gaps and missing elements (prioritized)

P1, highest value.

1. Full-funnel allocation guidance is implicit. We map channels to funnel stage in
   `audience-and-bidding`, but `media-plan` does not give the strategist a default
   awareness / consideration / conversion split to reason from (the field benchmark is roughly
   20 / 30 / 50, tuned by objective). The split must still come from the brief, but the skill
   could prompt the strategist to state the funnel-stage allocation explicitly. (Search Engine
   Journal, SERT Media, Stackmatix)

2. The pre-launch checklist is thinner than best practice. Ours covers pixel, UTMs, naming,
   budget cap, end date. Missing, and standard in 2026 launch QA: a verified live test event in
   Events Manager (not just "pixel firing"), conversion event and conversion location correct,
   audience geo and demographics confirmed, bid strategy and bid amount confirmed, creative
   spell-check, captions on any video, and for search: negative keywords, match types, and ad
   assets / extensions. (PPC Hero, Pearmill, WonderAds)

3. Budget-level structure (CBO vs ABO) is unstated. Neither `media-plan` nor `audience-and-bidding`
   names whether budget sits at campaign or ad-set level, which is the central 2026 structural
   decision and drives the test-then-scale path. (AGrowth, AdStellar)

P2, meaningful.

4. Bid-strategy progression and the learning phase as a gate on scaling are not spelled out.
   `paid-optimization` proposes scale and cut but does not tie scaling to exiting the learning
   phase (about 50 conversions / ad set / 7 days) or cap step size (20 to 30 percent every 2 to 3
   days). Adding these as named conditions would sharpen scale proposals. (Modern Marketing
   Institute, AGrowth)

5. The naming convention is referenced but not specified. Best practice fixes the element order
   (objective, audience, platform, geo, product, type, date), one separator, and a coded scheme
   so audience and budget names do not leak into UTMs. We say "naming-convention name" without
   defining it, which risks inconsistent, unanalyzable names across runs. (Improvado, PPC Hero,
   Supermetrics)

6. Measurement / incrementality is reactive only. `paid-optimization` reads platform-reported
   performance against the success_metric. There is no provision to design an incrementality or
   geo-holdout read, which the field treats as the trustworthy signal and budgets 10 to 15
   percent for. This connects to stream 8 (ab-test-plan) but is not referenced from paid.
   (Amsive, Measured)

P3, polish.

7. Search-specific structure is under-served. Our channel set names Google but the build template
   and audience skill are Meta-shaped (ad sets, placements). Google's ad group, keyword,
   match-type, and negative-keyword constructs have no explicit slot. (WonderAds, PPC Hero)

## Where ours is stronger

These are deliberate design choices in our engine that exceed the typical public framework, which
mostly assumes an in-house team that can spend at will.

- Budgets and targets are brief inputs, never assumed. Every public template asks you to "set a
  budget"; ours refuses to invent one and stops and asks if the brief is silent
  (`media-plan/SKILL.md` Inputs and Hard rules, `audience-and-bidding/SKILL.md` Hard rules).
  This is a guardrail almost no external guide enforces.

- Staged-paused build that never spends. The build assembles a full campaign in a PAUSED state and
  cannot flip itself live (`05-build-launch/SKILL.md` Hard rules,
  `paid-campaign-build/templates/paid-campaign-structure.md` every block PAUSED). External QA
  checklists assume a human who can launch at the end; ours makes launch structurally impossible
  without the gate.

- Strategist / builder split. `performance-marketer` decides what the spend should buy and why,
  `paid-build-engineer` assembles it paused, and neither can authorize spend
  (`paid-performance/SKILL.md` the split is deliberate). Public frameworks blur planning and
  execution into one role.

- Human gate before any spend, per launch and per campaign, with silence never read as approval
  (`paid-performance/SKILL.md` Hard rules, `sops/paid-performance.md` Review owner). No external
  source builds an explicit anti-silence approval rule.

- `spend_on_approval` disclosure. Every package states the maximum spend it would incur if
  approved, with currency and window, plus a one-sentence `flips_live`
  (`runtime/handoff-contract.md` media-plan-package and paid-launch-package). This costed,
  no-hidden-spend disclosure has no equivalent in the public templates.

- Optimization as proposal, not action. `paid-optimization` never pauses an ad set, shifts a
  budget, or rotates a creative on the live campaign; every move is evidence-backed and routed to
  the human gate (`paid-optimization/SKILL.md` Hard rules). Public scaling playbooks assume the
  operator acts directly.

- Privacy in tracking. No personal or sensitive data in any URL parameter or UTM is a hard rule
  across the build (`paid-campaign-build/SKILL.md` step 5). The naming-convention sources reach
  the same conclusion only as a side note about UTM leakage.

## Recommendations (prioritized, tied to sources)

Each is a proposed edit to the named skill or template, for the human gate. None is adopted here.

1. P1. Add a funnel-stage allocation line to `media-plan`. In `media-plan/SKILL.md` step 3 and the
   `media-plan/templates/media-plan.md` Budget split, ask the strategist to state the
   awareness / consideration / conversion share explicitly, sourced from or confirmed against the
   brief objective, with the field default (about 20 / 30 / 50, growth tilts upper, efficiency
   tilts lower) offered as a reasoning anchor only, never an assumed value. Keep the brief-total
   rule intact. (Search Engine Journal, SERT Media, Stackmatix)

2. P1. Expand the pre-launch checklist in `paid-campaign-build/templates/paid-campaign-structure.md`
   and `sops/05-build-launch-paid.md` step 4. Add: live test event confirmed in Events Manager,
   conversion event and conversion location correct, audience geo and demographics confirmed, bid
   strategy and amount confirmed, creative spell-check, video captions present, and for search:
   negative keywords present, match types set, ad assets / extensions added. Keep each as
   pass / fail and keep the "a failing check blocks the package from the gate" rule. (PPC Hero,
   Pearmill, WonderAds)

3. P1. Name the budget-level decision (CBO vs ABO) in `media-plan` or `audience-and-bidding`. Add a
   field to record whether budget sits at campaign or ad-set level and why, tied to the
   test-then-scale stage, so the build template can carry it. (AGrowth, AdStellar)

4. P2. Specify the naming convention rather than referencing it. Add a short convention block (fixed
   element order: objective, audience, platform, geo, product, type, date; one separator; coded
   audience and budget tokens so they do not leak into UTMs) to
   `paid-campaign-build/templates/paid-campaign-structure.md`, reinforcing the existing no-PII-in-
   UTMs rule. (Improvado, PPC Hero, Supermetrics)

5. P2. Add learning-phase and step-size conditions to `paid-optimization`. In the proposed-moves
   logic, gate a scale proposal on the ad set having exited the learning phase (about 50
   conversions in 7 days) and cap proposed increases at roughly 20 to 30 percent per step, all
   still within the brief budget and window. This sharpens the existing scale / cut moves without
   changing the proposal-not-action rule. (Modern Marketing Institute, AGrowth)

6. P3. Reference an incrementality / geo-holdout read from paid. In `paid-optimization` and the link
   to stream 8 ab-test-plan, allow the strategist to propose a geo-holdout or incrementality test
   (control vs holdout geos, 2 to 4 weeks) as a human-gate proposal, so the success_metric read is
   not platform-reported numbers alone. (Amsive, Measured)
