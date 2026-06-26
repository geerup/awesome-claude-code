---
name: event-tracking
description: Plan the conversion event tracking for stream 6. Use to define the events page_view, gate_view, submit, confirm, and the post-signup revenue event (purchase or subscription_start) and map each to Meta Pixel or CAPI and to GA4, with event_id deduplication for dual Pixel-plus-CAPI sending, mobile (Apple IAP, Google Play) mapping flagged as a to-confirm open item, and no personal data in URLs. Triggers on "set up event tracking," "the measurement plan," "pixel and GA4 mapping," "wire the conversion events." Sub-skill of 06-conversion-path, owned by conversion-engineer.
---

# Event Tracking (stream 6 sub-skill)

Produces the measurement plan that fills the `event_plan` field of the `conversion-package`.
It defines the funnel events, through the opt-in and on to the post-signup revenue event, and
maps them to the ad platform and to analytics, so the funnel is provable end to end. It never
writes personal or sensitive data into a URL or a parameter.

Owner: conversion-engineer. Mode: execution (gated). Follows `sops/06-conversion-path.md`.

## When to use

- A page or gate is being built and the funnel must be measurable.
- The orchestrator needs the tracking plan before any go-live writes to production.

## Inputs

- The page and gate spec (which surfaces exist to fire events on).
- The active `briefs/` file: the conversion the campaign optimizes toward.
- The platform decision for the gate (OPEN ITEM until the email and WhatsApp platform is
  named). The web events are planned regardless; gate-side wiring blocks on it.

## The events

1. `page_view`: the landing page loads.
2. `gate_view`: the signup gate becomes visible to the visitor.
3. `submit`: the visitor submits the gate (email or WhatsApp opt-in).
4. `confirm`: the signup is confirmed (double opt-in or gate confirmation).
5. Post-signup revenue event (`purchase` or `subscription_start`): the revenue moment after
   signup, when the visitor buys or starts a subscription. This is the value event paid
   optimization and CAPI actually need; the funnel must not stop at the lead. Use one name
   consistently per campaign: `purchase` for a one-time buy, `subscription_start` for a
   subscription. It maps to GA4 `purchase` and Meta `Purchase`.

## Steps

1. Define each event with its fire condition, through `confirm` and on to the post-signup
   revenue event.
2. Map each event to Meta Pixel or CAPI and to GA4. Record the destination event name on
   each side. Keep naming consistent with the campaign convention. The revenue event maps to
   GA4 `purchase` and Meta `Purchase`.
3. When the same event is sent by both the Meta Pixel (browser) and the Conversions API
   (CAPI, server), give both copies one shared `event_id` so Meta deduplicates them and the
   action is not double-counted. This applies to the revenue event in particular, and to any
   event sent on both paths. The `event_id` is a non-identifying value, never a personal one.
4. Define parameters: only non-identifying values (event id, campaign, content group). Never
   put email, phone, name, or any personal or sensitive value in a URL parameter.
5. Mark mobile mapping (Apple IAP, Google Play) as a to-confirm open item. Do not guess the
   mapping; record it as open and carry it forward.
6. Specify the test plan: each event fires once, in order, in a test session, before go-live,
   and confirm the dual-sent events share one `event_id` and deduplicate correctly.
7. Hand the plan to the hub for the `event_plan` field and for operational verification.

## Output

A tracking plan for the `event_plan` field of the `conversion-package`:

```
events         page_view, gate_view, submit, confirm, purchase or subscription_start, with fire conditions
pixel_capi     destination event names on Meta Pixel or CAPI; revenue event maps to Meta Purchase
ga4            destination event names on GA4; revenue event maps to GA4 purchase
event_id       shared event_id for any event sent by both Pixel and CAPI, so it is not double-counted
parameters     non-identifying only; no personal or sensitive data
mobile         Apple IAP, Google Play mapping flagged to-confirm (open item)
test_plan      each event fires once, in order, in a test session; dual-sent events deduplicate
```

## Verification gates

- Skill eval (this file's `evals/evals.json`) for structure and the no-personal-data rule.
- Operational: events fire correctly in test before go-live at the human gate, per
  `runtime/verification.md`. A failing event-firing check blocks the package from the gate.

## Hard rules

- No personal or sensitive data in URL parameters or tracking. This is a hard stop.
- Mobile mapping is to-confirm, never guessed.
- Western numerals. No em dashes, no tatweel.
