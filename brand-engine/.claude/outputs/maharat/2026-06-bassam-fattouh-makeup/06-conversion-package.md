# conversion-package: Bassam Fattouh Teaches Makeup

Produced by conversion-engineer (page and gate) plus data-tracking-engineer (events and warehouse). The
page realizes the web-designer's design_spec, it does not re-originate the design. Execution and gated:
nothing goes live or writes to production without the human gate. Never put personal or sensitive data in
URL parameters or tracking.

## Common envelope

- campaign_id: 2026-06-bassam-fattouh-makeup
- produced_by: conversion-engineer, data-tracking-engineer
- stream: 6 conversion path
- status: gated-pending (design and event plan ready; live wiring blocked on the platform)
- qa: { skill_eval: pass, arabic_qa: pass (page copy bound from QA-passed variants), web_design_qa: pass, compliance: pass (design-only), brand_qa: pass }
- open_items: gate platform not confirmed (Ortto flagged), mobile IAP and Google Play mapping to-confirm,
  rights-cleared assets to confirm. Live send and go-live blocked until the platform is named and approved.

## page

- The landing surface realizing `05-web-design-package.md` design_spec: RTL-correct, on the visual constants,
  fast, uncluttered, one primary action per view. Every text region binds to a QA-passed copy-package variant
  id (no free copy). The free intro chapter is the qualifying micro-conversion; subscription is the primary
  conversion; an email capture catches non-converters for lifecycle.

## gate

- Primary: the Maharat subscription signup or plans flow (the paid conversion).
- Secondary: an email capture for non-converters, with a clear consent line, feeding the lifecycle layer.
- Platform wiring: blocked on the gate-platform open item. ManyChat captures Instagram leads but does not send
  email, so the email handoff to the engine is an open integration item. No live send is wired until the
  platform is named and approved.

## event_plan (data-tracking-engineer)

```
events            page_view, gate_view, free_intro_play (the qualifying micro-conversion),
                  email_submit (non-converter capture), subscribe_start (revenue: subscription_start)
pixel_capi_map    Meta Pixel and Conversions API: subscribe_start maps to Meta Purchase or Subscribe;
                  free_intro_play and email_submit map to custom events for optimization signal
ga4_map           GA4: subscribe_start maps to GA4 purchase or subscription_start; others as custom events
event_id_dedup    any event sent by both Pixel and CAPI carries one shared, non-identifying event_id, the
                  revenue event in particular, so Meta deduplicates and does not double-count
mobile_map        Apple IAP and Google Play subscription mapping, flagged to-confirm, never guessed
warehouse_refs    BigQuery views for signups, free-intro plays, and subscription starts, for the readout
open_items        platform-not-confirmed, mobile-mapping-to-confirm, access-not-granted
```

- Privacy: no personal or sensitive data in URL parameters or tracking. UTMs carry campaign, source, medium,
  content only, never an email, name, or any identifier. Consent precedes any marketing event where required.

## Operational verification (before the gate)

- The page renders RTL-correct in test at sm, md, lg (web-design-qa passed on the design).
- The gate submits to the right destination once the platform is named (currently blocked).
- The event plan is reviewed by compliance for consent and data minimization (design-only pass).

## Handoff

Carries the event_plan from data-tracking-engineer, attaches the compliance and brand-qa verdicts, and routes
the go-live decision to the human gate. Tracking results feed analytics-reporter. Publishing the page and
wiring a live send happen only after the gate clears, and only what was approved.
