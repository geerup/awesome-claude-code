---
name: 06-conversion-path
description: Hub for stream 6 conversion path, owned by conversion-engineer, execution and gated. Use when a campaign lands traffic and needs a page, a signup gate, or event tracking between the click and the entry to lifecycle. Routes to landing-page and event-tracking, and assembles the conversion-package that streams 7 and 8 and the human gate consume. Triggers on "build the landing page," "set up event tracking," "wire the conversion path," "map the signup gate."
---

# 06 Conversion Path (hub)

Stream 6. Owns everything between the click and the entry to lifecycle: the landing page,
the signup gate (email or WhatsApp), and the event tracking that proves the funnel works.
This hub does not build the artifacts itself. It validates inputs, routes to the right
sub-skill, and assembles the `conversion-package` defined in `runtime/handoff-contract.md`.

Owner: conversion-engineer. Mode: execution (gated). Follows `sops/06-conversion-path.md`.

## When to use

- A campaign acquires traffic and needs a landing page, a signup gate, or tracking.
- For the owned-audience non-payer flow, this runs only if the emails point to a page or a
  gated offer.
- The orchestrator dispatches stream 6 (per `runtime/stream-ownership.md`).

## Sub-skills (routing)

- `landing-page`: specifies the landing page. On brand, RTL-correct, fast, uncluttered.
  Visual constants #141414, #1A1A1A, emerald #009975. One clear CTA. Copy comes from the
  QA-passed copy-package, never invented here. Use when you need the page spec.
- `event-tracking`: plans the events page_view, gate_view, submit, confirm, and maps each to
  Pixel or CAPI and to GA4. Mobile (Apple IAP, Google Play) mapping is a to-confirm open
  item. No personal data in URLs. Use when you need the measurement plan.

Route: the page goes to `landing-page`, the measurement goes to `event-tracking`. Both feed
the same `conversion-package`.

## Inputs

- Approved creative and copy for the page (streams 3, 4), the QA-passed `copy-package`.
- The active `briefs/` file: offer, gate type (email or WhatsApp), price and promotion only
  when the page shows them.
- The platform decision for the gate (OPEN ITEM until the email and WhatsApp platform is
  named). Design proceeds without it; the gate go-live does not.

If a needed variable is absent from both brief and context, stop and ask. Do not fill the
gap with an invented value.

## Steps

1. Validate the incoming envelope: right campaign_id, status at least qa-passed on the
   copy-package, required fields present, open_items read. If incomplete, return it.
2. Route the page to `landing-page` and the measurement to `event-tracking`.
3. Run the operational verification: the page renders RTL-correct, the events fire in test,
   the gate submits to the right destination. A failing check blocks the package from the gate.
4. Surface every open item. Carry platform-not-confirmed and mobile-mapping-to-confirm
   forward; never silently close them.
5. Assemble the `conversion-package` and route go-live to the human gate.

## Output: the conversion-package

The body shape, exactly as `runtime/handoff-contract.md` defines it:

```
page          landing page spec or build ref, RTL-correct
gate          signup gate type (email | whatsapp) and platform wiring
event_plan    events: page_view, gate_view, submit, confirm; pixel/capi and ga4 mapping
open_items    platform-not-confirmed, mobile-mapping-to-confirm, etc.
```

Wrapped in the common envelope (campaign_id, produced_by, stream, status, qa, open_items,
brief_refs).

## How this connects to the contract and gates

- Consumes: `copy-package` (stream 4), `creative-package` (stream 3) when the page needs art.
- Produces: `conversion-package` (stream 6 -> 7, 8, human gate).
- Gate before advance: skill eval + `brand-qa-reviewer` on the page (arabic-copy-qa on AR
  page copy), then the human gate for go-live, per `runtime/verification.md`.

## Hard rules

- Never put personal or sensitive data in URL parameters or tracking.
- Confirm the gate platform before wiring sends. Block on the open platform item if unresolved.
- RTL must render correctly. Western numerals. No em dashes, no tatweel.
- Never imply certificates are accredited.
