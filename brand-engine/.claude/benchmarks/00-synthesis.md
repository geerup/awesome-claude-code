# Benchmark synthesis: the engine against the field

Nine domain benchmarks (docs 01 to 09) compared the engine to authoritative, current (June
2026) templates and frameworks pulled from the web. This doc consolidates them into one
prioritized list. Nothing here is applied. Each item is a reviewed, optional edit, approved by
Ahmed like any other change.

A note on method: most external pages bot-blocked direct fetch, so the comparisons are grounded
in search-result summaries of the same authoritative sources, cross-checked across several per
claim. Each benchmark doc lists its sources.

## The headline: the engine is structurally ahead, the gaps are additive

Across all nine areas the same pattern held. On the things that make an agentic,
campaign-agnostic engine trustworthy, we already beat the generic templates:

- Campaign-agnostic briefs with first-class ASSUMPTION and OPEN ITEM flagging, and stop-and-ask
  instead of invented values.
- English-first voice with hard mechanical rules (no em dash, no tatweel, Western numerals, RTL),
  and Arabic capability as a disqualifying filter for any generative tool.
- The success_metric fixed before measurement, which blocks after-the-fact metric cherry-picking.
- A binary gate stack with quoted-span fix lists, stricter than the pass-with-comments review
  the QA sources describe.
- The human gate before any send, publish, or spend, with silence never read as approval.
- Suppression, consent, no-PII-in-URLs, and the not-sendable design state, which the
  conversion and lifecycle sources do not even address.

The gaps the benchmark found are almost all additive fields or parameters, not structural
weaknesses. None requires dropping a guardrail. Where an external norm conflicts with a Maharat
rule, the rule wins.

## Priority 1: highest leverage, lowest risk, do first

Status: APPLIED on 2026-06-02. All 5 items below are now in the engine (additive edits, every
guardrail preserved). Priority 2 and 3 remain open for a future approved pass.

| # | Recommendation | Target files | From |
|---|---|---|---|
| 1 | Extend the compliance gate with data-minimization, a retention or deletion stance, and data-subject-rights (access and deletion) checks. PDPL is a live open item and Saudi is the primary market, so this is the most consequential gap. | `skills/compliance-privacy-check/SKILL.md` and its eval | 09 |
| 2 | Add a winback and reactivation flow sub-skill to stream 7 (RFM recency, 30/60/90-day triggers, copy by id, human-gated), plus a sunset rule and engagement-decay suppression in `segmentation-logic`. Protects deliverability and works the lapsed base. | new `skills/07-lifecycle-messaging/winback-flow/`, `skills/07-lifecycle-messaging/segmentation-logic/` | 04 |
| 3 | Make the success_metric measurable: require a number and a date in the brief, add a SMART and leading-vs-lagging quality check at intake and strategy, and raise a weak metric as an open item. | `briefs/_TEMPLATE-campaign-brief.md`, `skills/01-brief-intake/brief-validate/*`, `sops/02-strategy-planning.md` | 01, 02 |
| 4 | Add a sample-size and method block to the A/B test plan (baseline rate, minimum detectable effect, per-arm sample size, significance level or named method, chosen before launch), and an owner plus due date on each `what_to_change` item in the campaign report. | `skills/08-monitoring-optimization/ab-test-plan/*`, `skills/09-reporting-learning/campaign-report/*` | 09 |
| 5 | Extend the conversion event model past `confirm` with a post-signup revenue event (purchase or subscription start) mapped to GA4 and Meta, with an event_id deduplication line for dual Pixel and CAPI. | `skills/06-conversion-path/event-tracking/*`, `runtime/handoff-contract.md` (tracking-package) | 04 |

## Priority 2: clear value, channel-specific

Status: APPLIED on 2026-06-02. All 12 items below are now in the engine (additive edits, every
guardrail preserved).

| # | Recommendation | Target files | From |
|---|---|---|---|
| 6 | Add background and context plus a provisional key_message field to the campaign brief, so strategy has a rationale anchor and the objective and message check against each other. | `briefs/_TEMPLATE-campaign-brief.md`, `skills/01-brief-intake/*` | 01 |
| 7 | Add a per-segment pains-and-gains or jobs-to-be-done step before the angle, and a competitive-alternative field to the offer framing. | `skills/02-strategy-planning/offer-and-angle/*` | 02 |
| 8 | Add optional named copy frameworks (4 Us, PAS, AIDA, 4 Cs) as checklists, a mobile-justified subject length (about 30 to 40 characters, key word first), and a deliberate preheader field. | `skills/04-copywriting/*` (ad-copy, email-copy, subject-lines) | 03 |
| 9 | Name the funnel-stage budget split and the CBO versus ABO decision in the media plan, and expand the pre-launch checklist (live test event, geo, bid, captions, negatives, match types). | `skills/paid-performance/media-plan/*`, `skills/05-build-launch/paid-campaign-build/*`, `sops/05-build-launch-paid.md` | 05 |
| 10 | Add generative AI and answer-engine intent as a recognized search intent, Core Web Vitals thresholds (LCP 2.5s, INP 200ms, CLS 0.1 at the 75th percentile), and an indexation baseline and gap heuristic. | `skills/seo/keyword-and-intent-research/*`, `skills/seo/on-page-optimization/*`, `skills/seo/technical-seo/*` | 06 |
| 11 | Add Apple Custom Product Pages and the PPO-then-CPP workflow, experiment read-windows and treatment limits, and tighter App Store keyword-field mechanics (stop words, no cross-field repetition, singular and plural). | `skills/aso/store-listing-optimization/*`, `skills/aso/store-creative-and-experiments/*` | 07 |
| 12 | Add an embargo opt-in step (ask the journalist first, record the agreement), a news-hook field to the announcement plan, and a pitch shape spec (under about 100 words, beat-specific, one ask). | `skills/pr-comms/media-list-outreach/*`, `skills/pr-comms/announcement-plan/*` | 08 |

## Priority 3: refinements

Status: APPLIED on 2026-06-02. All items below are now in the engine.

- Add a default reporting cadence to the monitoring and reporting SOPs (monthly report, weekly
  paid check-ins), keeping the event-driven triggers. (09)
- Add weights and a must-have versus nice-to-have flag to the build-vs-buy scorecard, keeping
  Arabic capability as the existing hard gate. (09)
- Add an optional supporting-cuts section (funnel-stage and per-segment) to the readout and
  report, anchored to the success_metric and never replacing it. (09)
- Split brief mandatories (logos, legal, colors) and add tone descriptors and a reporting
  cadence field to the brief. (01)

## What any edit must preserve

Every recommendation above is additive. Applying it must not weaken: the four non-negotiable
principles, the no-invented-values rule, the English-first and RTL rules, the hard mechanical
rules, the binary gates, or the human gate. Where a benchmark norm and a Maharat rule disagree,
the rule wins and the edit is dropped or reshaped to fit.
