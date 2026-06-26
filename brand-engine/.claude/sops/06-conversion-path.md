# SOP 06: Conversion path

Stream 6. Owner: conversion-engineer. Mode: execution (gated). Owns everything between the
click and the entry to lifecycle: the landing page, the signup gate (email or WhatsApp), and
the event tracking that proves the funnel works.

No em dashes, no tatweel, Western numerals, English-first, RTL-correct, no accreditation claims.

---

## Trigger

A campaign that lands traffic and needs a page, a gate, or tracking. For the owned-audience
non-payer flow, this runs only if the emails point to a page or a gated offer.

## Inputs

- Approved creative and copy for the page (streams 3, 4), QA-passed.
- The brief: offer, gate type (email or WhatsApp), price and promotion if shown on the page.
- The platform decision for the gate (OPEN ITEM until the email and WhatsApp platform is named).

## Steps

1. Specify the landing page: on brand, RTL-correct, fast, uncluttered. Visual constants
   #141414, #1A1A1A, emerald #009975. One clear CTA. Copy comes from the QA-passed
   copy-package, not invented here.
2. Wire the signup gate: email or WhatsApp per the brief. Note that ManyChat captures
   Instagram leads but does not send email; the email handoff to the engine is an open
   integration item. Block on the platform open item before wiring an actual send.
3. Plan the events: page_view, gate_view, submit, confirm. Map each to Pixel or CAPI and to
   GA4. Never put personal or sensitive data in URL parameters.
4. Map mobile events (Apple IAP, Google Play) as a to-confirm open item. Never guess the
   mapping.
5. Run the operational verification: the page renders RTL-correct, the events fire in test,
   the gate submits to the right destination. A failing check blocks the package from the gate.
6. Assemble the `conversion-package` and route go-live to the human gate.

## Output

A `conversion-package` (see `runtime/handoff-contract.md`):
- page: spec or build ref, RTL-correct.
- gate: signup gate type and platform wiring.
- event_plan: events with Pixel or CAPI and GA4 mapping.
- open_items: platform-not-confirmed, mobile-mapping-to-confirm, and any other.

## Quality bar

- Page copy is QA-passed (skill eval, arabic-copy-qa, brand-qa). RTL renders correctly.
- Events fire correctly in test before go-live. UTMs and naming are consistent.
- No personal or sensitive data in URLs. No accreditation implication on the page.
- The platform open item is surfaced; the gate go-live is blocked until it is confirmed.

## Review owner

Ahmed, at the human gate, for go-live and for any tracking written to production. Approval is
per action. The conversion-engineer publishes or writes to prod only after the gate clears,
and only what was approved.
