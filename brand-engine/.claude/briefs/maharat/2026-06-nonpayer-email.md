# Campaign Brief: non-payer email flow (first build)

The first-build brief. Owned audience, the roughly 18,000 non-paying email contacts. Zero
media cost, fast, low-risk. Entry point is stream 7 lifecycle, not acquisition.

Fields marked ASSUMPTION are placeholders. The engine drafts against them so the structure
is ready, but it does not send and the human gate package must surface every ASSUMPTION so
Ahmed replaces them with real values before approval.

No em dashes, Western numerals, Arabic-first.

---

## 1. Identity

- campaign_id: 2026-06-nonpayer-email
- name: Non-payer reactivation email flow
- owner: Ahmed
- created: 2026-06-02

## 2. Entry point and objective

- entry_point: owned audience
- objective: Convert non-paying email contacts into paying subscribers, or at minimum
  reactivate engagement and move them toward a first purchase.
- success_metric: ASSUMPTION. Proposed primary: subscription conversion rate from the
  flow, with a secondary on click-through and reactivation. Confirm the primary target.

## 3. Audience

- audience: Owned email contacts who have not paid. Arabic-speaking adults, GCC, primary
  Saudi Arabia.
- segments: To be defined by strategy-lead from the owned data. Likely cuts: never-engaged
  vs lapsed-engaged, single-class interest vs none, recency of last open.
- suppression: Exclude all paying contacts (about 5,000), and anyone unsubscribed or in a
  hard-bounce state. Confirm suppression list source at build.
- audience_size: About 18,000 non-paying contacts (planning estimate). Resolved exactly at
  send time from live data and recorded in the lifecycle package.

## 4. Offer (never invented, supplied here)

- product: Subscription (B2C). Possibly anchored on a Masterclass as the hook.
- plan: ASSUMPTION. Likely the 1-month or 3-month plan as the entry. Confirm.
- price: ASSUMPTION. Confirm the price and currency before any send.
- promotion: ASSUMPTION. Confirm whether there is a first-time discount, trial, or bundle.
  Do not invent one.
- offer_framing_notes: Empowering, never deficit-framed. Lead with what the reader can build,
  not with what they are missing.

## 5. Channels and gate

- channels: email (primary). WhatsApp is a later layer, out of scope for this first build
  unless the platform is confirmed.
- signup_gate: email (the contact already exists; the conversion is to a paid plan).
- gate_platform: OPEN ITEM. The email and WhatsApp platform is not yet confirmed. Block any
  actual send wiring until it is named. See `references/2026-06-email-whatsapp-platform-research.md`.

## 6. Budget and schedule

- budget: n/a (owned audience, zero media cost).
- target_cpa_or_roas: n/a for media. Track cost per conversion as effectively zero-media.
- start_date: ASSUMPTION. Confirm.
- end_date: ASSUMPTION. Confirm.
- send_window: ASSUMPTION. Proposed: a 3 to 5 message flow over 2 to 3 weeks, triggered by
  entry and by engagement. Confirm cadence.

## 7. Creative direction (optional, brief-level)

- creative_direction: Email-first, minimal imagery. Stream 3 creative runs only if a message
  needs a visual asset. Brand visual constants apply: #141414, #1A1A1A, emerald #009975.
- assets_available: ASSUMPTION. Confirm whether existing email templates or imagery exist.

## 8. Constraints and notes

- constraints: Owned audience only. No paid build (stream 5 paid path skipped). RTL-correct
  Arabic email. No accreditation claims. No invented Skill Path titles or instructor names.
- open_items: Email platform not confirmed (blocks send wiring). Offer price and promotion
  not confirmed. Success metric target not confirmed. Schedule not confirmed.

## 9. Approvals

- approval_owner: Ahmed
- approval_status: pending. Nothing sends. The swarm assembles an approval-ready package and
  stops at the human gate. Approval is per send.
