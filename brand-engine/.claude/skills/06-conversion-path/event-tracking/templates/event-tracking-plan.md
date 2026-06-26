# Event tracking plan

Fills the `event_plan` field of the `conversion-package`. Defines the funnel events, through
the opt-in and on to the post-signup revenue event, and maps each to Meta Pixel or CAPI and to
GA4. No personal or sensitive data in any URL or parameter. Mobile mapping is a to-confirm open
item, never guessed.

## Envelope reference

```
campaign_id   <from the active brief filename>
produced_by   conversion-engineer
stream        6 conversion path
status        draft | qa-passed | gated-pending | approved
brief_refs    <the conversion the campaign optimizes toward>
```

## The events

| Event | Fire condition | Pixel or CAPI name | GA4 name |
|---|---|---|---|
| page_view | landing page loads | <destination name> | <destination name> |
| gate_view | signup gate becomes visible | <destination name> | <destination name> |
| submit | visitor submits the gate (email or WhatsApp opt-in) | <destination name> | <destination name> |
| confirm | signup confirmed (double opt-in or gate confirmation) | <destination name> | <destination name> |
| purchase or subscription_start | revenue moment after signup: visitor buys or starts a subscription | Purchase | purchase |

The last row is the post-signup revenue event, the value moment paid optimization and CAPI
need. Pick one name per campaign: `purchase` for a one-time buy, `subscription_start` for a
subscription. It maps to GA4 `purchase` and Meta `Purchase`. The funnel does not stop at the
lead.

## Event_id deduplication (dual Pixel and CAPI sending)

- When an event is sent by both the Meta Pixel (browser) and the Conversions API (CAPI,
  server), both copies must carry one shared `event_id` so Meta deduplicates them and the
  action is not double-counted.
- This applies to the post-signup revenue event in particular, and to any event sent on both
  paths.
- The `event_id` is a non-identifying value. Never derive it from, or pair it with, email,
  phone, name, or any personal or sensitive value.

## Parameters

- Non-identifying values only: event id, campaign, content group, source and medium.
- Never put email, phone, name, or any personal or sensitive value in a URL parameter.

## Mobile mapping (open item, to confirm)

- Apple IAP: mapping to confirm. Do not guess.
- Google Play: mapping to confirm. Do not guess.
- The post-signup revenue event on mobile (a purchase or subscription start through Apple IAP
  or Google Play) is part of this open item. Web maps to GA4 purchase and Meta Purchase now;
  the mobile store equivalent is to-confirm.
- Carried forward as an open item until confirmed.

## Test plan

- Each event fires once, in order, in a test session.
- page_view, then gate_view, then submit, then confirm, then the post-signup revenue event.
- For any event sent by both Pixel and CAPI, verify both copies share one `event_id` and
  Meta deduplicates them, so the action is counted once.
- Verify before go-live at the human gate. A failing event-firing check blocks the package.

## Open items

- Gate platform not confirmed: web events are planned regardless, gate-side wiring is blocked
  until the email or WhatsApp platform is named and approved.
- Mobile mapping (Apple IAP, Google Play) to confirm.

## Guardrails check before handing up

- No personal or sensitive data in any URL or parameter.
- Western numerals only (0 to 9). No em dashes, no tatweel.
- Mobile mapping flagged to-confirm, never guessed.
