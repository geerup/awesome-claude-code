# Tracking Plan: Bassam Fattouh Teaches Makeup, Full Funnel

## Envelope

- campaign_id: 2026-06-bassam-fattouh-makeup
- produced_by: data-tracking-engineer
- stream: 6 conversion path (plumbing) / 8 warehouse queries
- status: draft
- qa:
  - skill_eval: pending
  - arabic_qa: na (plumbing artifact, no customer-facing copy)
  - brand_qa: na (plumbing artifact)
  - compliance: pending (routes to compliance-privacy-reviewer before go-live)
- open_items:
  - platform-not-confirmed: gate_platform (email, WhatsApp, app push) is OPEN ITEM. Gate-side
    event wiring (submit, confirm on the gate surface) is planned; the actual platform SDK or
    API calls are blocked until the vendor is named and the Saudi PDPL data-residency decision
    is confirmed.
  - mobile-mapping-to-confirm: Apple IAP and Google Play event mapping is flagged to-confirm.
    It is not guessed here.
  - success-metric-target-unset: the primary conversion count is ASSUMPTION (see brief). The
    BigQuery queries are wired to the metric definition; the absolute target awaits Ahmed.
  - credential-not-issued: EMAIL_WHATSAPP_API_KEY is not yet issued. No gate-side write is
    possible until both the credential and the vendor are confirmed.
  - prod-write-gated: writing tracking to production is a human-gate action. This is the plan
    only. Nothing fires in production until the human gate clears it.
- brief_refs:
  - objective: grow B2C subscriptions using the Masterclass as the hook
  - success_metric: subscription conversions attributable to the campaign (primary); Masterclass
    plays, signup-gate completions, cost per subscription (secondary)
  - campaign_id: 2026-06-bassam-fattouh-makeup
  - channels: paid (Meta, Instagram, Google, YouTube, TikTok), organic social, email, app push
  - signup_gate: email or WhatsApp (platform OPEN ITEM)
  - start_date: ASSUMPTION 2026-06-08 (confirm)
  - end_date: ASSUMPTION 2026-06-28 (confirm)

---

## 1. Surfaces and fire conditions

The four core funnel events plus one post-signup revenue event are defined here. Fire conditions
are tied to surfaces that the conversion-engineer owns. This plan assumes those surfaces exist
and are reachable; if a surface changes, the fire condition here must be updated before go-live.

### 1.1 page_view

- Description: the campaign landing page (Masterclass class page or a dedicated campaign page)
  has loaded and is visible to the user.
- Fire condition: fires once per page session on DOMContentLoaded (or equivalent page-load
  signal) on the campaign landing page URL. Does not re-fire on navigation within a SPA without
  a full page transition.
- Surfaces owned by conversion-engineer: the class page at
  maharat.com/[en|ar]/class/design-style/bassam-fattouh-teaches-makeup, or a campaign-specific
  landing page if one is built.

### 1.2 gate_view

- Description: the signup gate (the email or WhatsApp capture step) is visible to the user.
- Fire condition: fires once per session when the gate element enters the viewport or the gate
  modal/panel renders. Does not fire again if the gate is scrolled out and back in within the
  same session.
- Dependency: gate_platform OPEN ITEM. The gate surface is planned by conversion-engineer; this
  event is planned regardless of platform. The gate-side SDK wiring waits on platform
  confirmation.

### 1.3 submit

- Description: the user has submitted their contact information at the signup gate (the opt-in
  form is submitted).
- Fire condition: fires once on successful form submission (no client-side validation error
  outstanding). Fires on the submit action, not on the downstream server confirmation.
- Note: this event captures a funnel step, not the contact data itself. No email address,
  phone number, name, or any other personal value is placed in any event parameter. The event
  signals that a submission occurred; the contact value stays in the backend only.

### 1.4 confirm

- Description: the signup is confirmed (the server has accepted the submission and the user
  has reached the confirmation state, for example a success message or a redirect to the
  plans page).
- Fire condition: fires once per session on receipt of the server success signal for the gate
  submission. In a server-side flow, this is the Conversions API call from the backend; in a
  client-side flow, it fires on the success callback after the server returns 200.
- Note: same PII rule as submit. No personal data in any parameter.

### 1.5 subscription_start

- Description: the user has completed a paid subscription purchase (the revenue event).
- Fire condition: fires once per transaction on the order confirmation page or on the
  server-side purchase confirmation webhook. This is the primary conversion event tied to the
  campaign success_metric.
- Note: this event carries a non-identifying event_id and the value and currency fields for
  conversion value reporting. No user-identifiable fields in any parameter passed to any
  analytics or ad platform. The backend may use hashed signals for CAPI matching; that is a
  server-side operation and must be reviewed by compliance-privacy-reviewer before go-live.

---

## 2. Meta Pixel and Conversions API mapping

All five events have a Pixel-side name and a CAPI-side name. The two names must match on every
event so Meta's deduplication logic can pair them. The event_id dedup approach is described
in section 3.

| Funnel event      | Meta Pixel event name | Meta CAPI event name | Notes                                      |
|-------------------|-----------------------|----------------------|--------------------------------------------|
| page_view         | PageView              | PageView             | Standard Meta event. Fire on page load.    |
| gate_view         | ViewContent           | ViewContent          | content_name: "signup-gate", no user data. |
| submit            | Lead                  | Lead                 | Standard lead event. No PII in params.     |
| confirm           | CompleteRegistration  | CompleteRegistration | Server-side preferred for reliability.     |
| subscription_start| Purchase              | Purchase             | Revenue event. value and currency required.|

Notes on the mapping:
- gate_view uses ViewContent because there is no standard Meta event for "gate visible." The
  content_name parameter identifies it as the signup gate. No user data.
- confirm maps to CompleteRegistration, which is the closest standard Meta event for a
  completed opt-in before purchase. If the gate-platform sends a confirmation signal
  server-side, that signal is what triggers the CAPI call; do not double-fire with both Pixel
  and CAPI without the dedup approach in section 3.
- subscription_start maps to Meta Purchase. The value field carries the subscription price
  (public reference: the annual plan price). The currency field is the transaction currency.
  These are non-identifying order values, not user data.

---

## 3. Event_id deduplication approach

Any event that is fired by both the Meta Pixel (browser-side) and Conversions API (server-side)
must carry a shared, non-identifying event_id so Meta can deduplicate it and avoid
double-counting. This applies most critically to subscription_start (Purchase) and confirm
(CompleteRegistration), which are the events most likely to have both a client-side fire and a
server-side CAPI call.

### How the dedup event_id is generated

- The event_id is a randomly generated UUID (version 4) or an equivalent non-sequential,
  non-guessable identifier.
- It is generated once per event occurrence, on the server side, before the page renders the
  client-side Pixel call.
- The server passes the event_id to the page (for example in a data layer push or a page
  variable) so the Pixel call and the CAPI call carry the same value.
- The event_id must not contain or encode any user identifier, session token that maps to a
  user, or any personal data. It is opaque.

### What carries the event_id

- Pixel-side: fbq('track', 'Purchase', { ... }, { eventID: '<uuid>' }) or the equivalent
  for each deduped event.
- CAPI-side: the event_id field in the Conversions API payload.
- Both must match exactly for Meta to deduplicate. A mismatch results in double-counting.

### Events requiring dedup

| Event              | Pixel fires? | CAPI fires? | Dedup required? |
|--------------------|-------------|-------------|-----------------|
| page_view          | yes         | no          | no              |
| gate_view          | yes         | no          | no              |
| submit             | yes         | recommended | yes if both     |
| confirm            | yes         | yes         | yes             |
| subscription_start | yes         | yes         | yes             |

Recommendation: for confirm and subscription_start, prefer the CAPI call as the source of truth
and use the Pixel call with the matching event_id as the browser-side signal only. If the
browser-side Pixel call fails (for example due to an ad blocker), the CAPI call still fires.

---

## 4. GA4 mapping

| Funnel event      | GA4 event name     | GA4 parameters (non-identifying only)                                      |
|-------------------|--------------------|----------------------------------------------------------------------------|
| page_view         | page_view          | page_location (URL, no user data in query params), campaign_id             |
| gate_view         | bf_gate_view       | campaign_id, content_group: "signup-gate"                                  |
| submit            | generate_lead      | campaign_id, method: "email" or "whatsapp" (once platform confirmed)       |
| confirm           | sign_up            | campaign_id                                                                 |
| subscription_start| purchase           | transaction_id (non-identifying order id), value, currency, campaign_id,   |
|                   |                    | items[]: item_id "bf-makeup-subscription", item_name "maharat-subscription"|

Notes on the GA4 mapping:
- page_view is the GA4 automatic event but is listed here for completeness and to confirm the
  campaign_id parameter is appended. Use the GA4 data layer push or gtag config to attach
  campaign_id to every event on the campaign page session.
- bf_gate_view is a custom event (prefixed bf for Bassam Fattouh) because GA4 has no
  standard gate_view event. The content_group parameter identifies it as the signup gate.
- generate_lead is the recommended GA4 event for a lead capture (equivalent to Meta Lead).
- sign_up is the recommended GA4 event for a completed registration.
- purchase is the GA4 standard e-commerce event for the revenue conversion. transaction_id
  must be a non-identifying order identifier (for example an auto-incremented order ID or a
  UUID). No user-identifying value in transaction_id or any other parameter.
- campaign_id is attached to all events so the BigQuery export can filter by campaign without
  relying solely on UTM parameters (which can be dropped if a user navigates internally).

### UTM parameters

Paid and owned traffic to the campaign page must carry UTM parameters so GA4 can attribute
sessions correctly. The utm_campaign value must be "2026-06-bassam-fattouh-makeup" consistently
across all paid, email, and organic links. utm_source and utm_medium follow the channel. UTM
values are non-identifying; they describe the traffic source, not the user.

No personal data (no email address, no phone number, no name, no user ID) is ever placed in
a UTM parameter or any URL query string that fires into a tracking call.

---

## 5. Parameters (full list, annotated for PII status)

The complete set of parameters in use across all events is listed here. Every parameter is
annotated with its PII status. Any parameter not on this list must be reviewed before
being added.

| Parameter        | Used in events                  | Value type                     | PII status |
|------------------|---------------------------------|--------------------------------|------------|
| campaign_id      | all                             | "2026-06-bassam-fattouh-makeup"| non-identifying |
| event_id         | confirm, subscription_start     | UUID v4, generated server-side | non-identifying |
| content_group    | gate_view                       | "signup-gate"                  | non-identifying |
| content_name     | gate_view (Pixel)               | "signup-gate"                  | non-identifying |
| method           | submit (GA4, post-confirm)      | "email" or "whatsapp"          | non-identifying |
| transaction_id   | subscription_start (GA4)        | non-identifying order UUID     | non-identifying |
| value            | subscription_start              | numeric subscription price     | non-identifying |
| currency         | subscription_start              | ISO 4217 currency code         | non-identifying |
| item_id          | subscription_start (GA4 items)  | "bf-makeup-subscription"       | non-identifying |
| item_name        | subscription_start (GA4 items)  | "maharat-subscription"         | non-identifying |
| page_location    | page_view (GA4)                 | page URL, no user data         | non-identifying (see note) |

Note on page_location: the URL logged in page_location must never contain an email address,
phone number, session token, or any user identifier in query parameters. If the platform
appends user-identifying parameters to URLs (for example some email platforms append
subscriber IDs), those parameters must be stripped before the GA4 event fires. This is a hard
stop; confirm with compliance-privacy-reviewer before go-live.

Explicitly prohibited in all parameters and tracking calls:
- Email address
- Phone number
- Full name or partial name
- User account ID or internal subscriber ID in any form that links to an individual
- Device identifier or advertising ID in parameters (these belong in the Pixel/CAPI match
  key fields only, server-side, not in URL query strings)
- Any value that can re-identify a user when combined with other logged fields

---

## 6. Mobile mapping (Apple IAP and Google Play)

The mobile event mapping for Apple In-App Purchase (IAP) and Google Play In-App Billing is
flagged as a to-confirm open item. It is not guessed here.

The mapping requires:
- Confirmation of which Maharat app (iOS, Android, or both) is in scope for this campaign.
- Confirmation of the subscription product ID(s) in the App Store and Google Play consoles.
- Confirmation of how the mobile purchase event is passed to Meta CAPI and GA4 (for example
  via server-to-server using the Firebase SDK, Adjust, or a direct webhook).
- Confirmation that the same event_id dedup approach from section 3 is applied to mobile
  purchase events so Pixel/CAPI dedup works for in-app conversions as well.

This open item must be resolved before go-live if the campaign drives any traffic to the app
install or in-app purchase flow. Web subscription events are planned and ready regardless.

---

## 7. Warehouse (BigQuery) queries for monitoring

The queries below are expressed in natural language and as SQL patterns. They measure the
brief's stated success_metric: subscription conversions attributable to the campaign (primary),
plus Masterclass plays, signup-gate completions, and cost per subscription (secondary).

The queries assume a standard GA4 BigQuery export schema: events_YYYYMMDD tables in the
analytics dataset, with event_name, event_params, user_pseudo_id, and event_date fields.
Table names and dataset identifiers are placeholders (your_project.your_ga4_dataset); replace
with the actual project and dataset before running.

The absolute conversion target is ASSUMPTION (see brief). These queries return the actual
count; the target is compared manually or in a monitoring view once Ahmed confirms the number.

---

### Q1. Daily subscription conversions attributable to the campaign (primary success_metric)

Natural language: how many subscription_start events fired each day where the session was
attributed to the campaign? This is the primary conversion count.

```sql
SELECT
  event_date,
  COUNT(*) AS subscription_starts
FROM
  `your_project.your_ga4_dataset.events_*`
WHERE
  _TABLE_SUFFIX BETWEEN '20260608' AND '20260628'
  AND event_name = 'purchase'
  AND (
    SELECT value.string_value
    FROM UNNEST(event_params) WHERE key = 'campaign_id'
  ) = '2026-06-bassam-fattouh-makeup'
GROUP BY
  event_date
ORDER BY
  event_date ASC
```

Note: this counts purchase events tagged with the campaign_id parameter. For cross-channel
attribution, supplement with a UTM-based session filter or a first-touch / last-touch
attribution model applied at the session level.

---

### Q2. Full funnel counts by day (all five events)

Natural language: show each funnel stage count per day so we can see where users drop off.

```sql
SELECT
  event_date,
  COUNTIF(event_name = 'page_view') AS page_views,
  COUNTIF(event_name = 'bf_gate_view') AS gate_views,
  COUNTIF(event_name = 'generate_lead') AS submits,
  COUNTIF(event_name = 'sign_up') AS confirms,
  COUNTIF(event_name = 'purchase'
    AND (
      SELECT value.string_value
      FROM UNNEST(event_params) WHERE key = 'campaign_id'
    ) = '2026-06-bassam-fattouh-makeup'
  ) AS subscription_starts
FROM
  `your_project.your_ga4_dataset.events_*`
WHERE
  _TABLE_SUFFIX BETWEEN '20260608' AND '20260628'
  AND (
    SELECT value.string_value
    FROM UNNEST(event_params) WHERE key = 'campaign_id'
  ) = '2026-06-bassam-fattouh-makeup'
GROUP BY
  event_date
ORDER BY
  event_date ASC
```

---

### Q3. Signup-gate completions (secondary metric: gate completions)

Natural language: how many users completed the signup gate (reached the confirm step) each day?

```sql
SELECT
  event_date,
  COUNT(*) AS gate_completions
FROM
  `your_project.your_ga4_dataset.events_*`
WHERE
  _TABLE_SUFFIX BETWEEN '20260608' AND '20260628'
  AND event_name = 'sign_up'
  AND (
    SELECT value.string_value
    FROM UNNEST(event_params) WHERE key = 'campaign_id'
  ) = '2026-06-bassam-fattouh-makeup'
GROUP BY
  event_date
ORDER BY
  event_date ASC
```

---

### Q4. Masterclass plays (secondary metric: chapter 1 free intro play as first-touch signal)

Natural language: how many times did users play the Masterclass (or specifically chapter 1
"The Talent") during the campaign window, attributable to the campaign?

Note: this query requires a video_play or class_play event to be defined and fired when a user
starts watching a chapter. That event is not in the four core funnel events above; it must be
added to the tracking plan if Masterclass plays are to be measured in the warehouse. The query
shape is provided as a pattern; the actual event_name must match what conversion-engineer
defines for the video play action.

```sql
-- Pattern query: replace 'video_start' with the actual event name for a chapter play
SELECT
  event_date,
  COUNT(*) AS masterclass_plays,
  COUNTIF(
    (
      SELECT value.string_value
      FROM UNNEST(event_params) WHERE key = 'chapter_id'
    ) = '1'
  ) AS chapter_1_plays
FROM
  `your_project.your_ga4_dataset.events_*`
WHERE
  _TABLE_SUFFIX BETWEEN '20260608' AND '20260628'
  AND event_name = 'video_start'
  AND (
    SELECT value.string_value
    FROM UNNEST(event_params) WHERE key = 'campaign_id'
  ) = '2026-06-bassam-fattouh-makeup'
GROUP BY
  event_date
ORDER BY
  event_date ASC
```

Open item: a video_start (or equivalent) event with a chapter_id parameter must be defined and
added to the tracking plan before this query is useful. Flagged for conversion-engineer and
data-tracking-engineer to align on.

---

### Q5. Funnel conversion rates (drop-off view, for monitoring)

Natural language: what percentage of page_view sessions reached each subsequent funnel step?
This is the read analytics-reporter uses to identify where to optimize.

```sql
WITH funnel AS (
  SELECT
    SUM(CASE WHEN event_name = 'page_view' THEN 1 ELSE 0 END) AS page_views,
    SUM(CASE WHEN event_name = 'bf_gate_view' THEN 1 ELSE 0 END) AS gate_views,
    SUM(CASE WHEN event_name = 'generate_lead' THEN 1 ELSE 0 END) AS submits,
    SUM(CASE WHEN event_name = 'sign_up' THEN 1 ELSE 0 END) AS confirms,
    SUM(CASE WHEN event_name = 'purchase' THEN 1 ELSE 0 END) AS subscription_starts
  FROM
    `your_project.your_ga4_dataset.events_*`
  WHERE
    _TABLE_SUFFIX BETWEEN '20260608' AND '20260628'
    AND (
      SELECT value.string_value
      FROM UNNEST(event_params) WHERE key = 'campaign_id'
    ) = '2026-06-bassam-fattouh-makeup'
)
SELECT
  page_views,
  gate_views,
  submits,
  confirms,
  subscription_starts,
  ROUND(SAFE_DIVIDE(gate_views, page_views) * 100, 2) AS pct_page_to_gate,
  ROUND(SAFE_DIVIDE(submits, gate_views) * 100, 2) AS pct_gate_to_submit,
  ROUND(SAFE_DIVIDE(confirms, submits) * 100, 2) AS pct_submit_to_confirm,
  ROUND(SAFE_DIVIDE(subscription_starts, confirms) * 100, 2) AS pct_confirm_to_sub,
  ROUND(SAFE_DIVIDE(subscription_starts, page_views) * 100, 2) AS overall_conversion_rate
FROM funnel
```

---

### Q6. Cost per subscription (secondary metric, requires paid spend data join)

Natural language: what was the cost per subscription from paid channels? This metric requires
the paid spend data (from Meta, Google, TikTok) to be loaded into a separate table or view.
The query shape below assumes a spend table is available; the actual table name and schema are
OPEN ITEM until the paid data pipeline is confirmed.

```sql
-- Pattern query: replace spend_table with the actual paid spend table
SELECT
  s.event_date,
  s.total_spend,
  c.subscription_starts,
  ROUND(SAFE_DIVIDE(s.total_spend, c.subscription_starts), 2) AS cost_per_subscription
FROM
  (
    SELECT date AS event_date, SUM(spend) AS total_spend
    FROM `your_project.your_spend_dataset.spend_table`
    WHERE campaign_id = '2026-06-bassam-fattouh-makeup'
    GROUP BY date
  ) s
JOIN
  (
    SELECT
      event_date,
      COUNT(*) AS subscription_starts
    FROM `your_project.your_ga4_dataset.events_*`
    WHERE
      _TABLE_SUFFIX BETWEEN '20260608' AND '20260628'
      AND event_name = 'purchase'
      AND (
        SELECT value.string_value
        FROM UNNEST(event_params) WHERE key = 'campaign_id'
      ) = '2026-06-bassam-fattouh-makeup'
    GROUP BY event_date
  ) c
ON s.event_date = c.event_date
ORDER BY s.event_date ASC
```

Open item: paid spend data pipeline and table schema must be confirmed before this query runs.
The budget is also OPEN ITEM in the brief, so the absolute cost-per-subscription target is not
set yet.

---

## 8. Test plan

Every event must fire once, in order, in a test session, before any go-live. The test session
is run in a staging or QA environment with the BigQuery export and a Meta test event tool
active. No test events are allowed to fire against production data streams unless the test
is explicitly tagged and excluded from monitoring queries.

Test sequence, in order:

1. Load the campaign landing page. Verify page_view fires in the GA4 DebugView and in the Meta
   Pixel Helper. Confirm campaign_id parameter is present. Confirm no personal data in any
   parameter.
2. Scroll to or trigger the signup gate. Verify gate_view (bf_gate_view in GA4, ViewContent in
   Meta Pixel) fires once. Confirm content_group or content_name is "signup-gate". Confirm no
   personal data in any parameter.
3. Complete the signup gate form and submit. Verify submit fires (generate_lead in GA4, Lead in
   Meta Pixel). Confirm no email address, phone number, or name appears in any parameter. If
   CAPI is wired for this event, verify the event_id in the Pixel call matches the event_id in
   the CAPI payload.
4. Reach the confirmation state. Verify confirm fires (sign_up in GA4, CompleteRegistration in
   Meta Pixel and CAPI). Verify event_id dedup: the Pixel event_id and the CAPI event_id are
   identical. Confirm no personal data in any parameter.
5. Complete a test subscription purchase. Verify subscription_start fires (purchase in GA4 and
   Meta Pixel/CAPI). Verify event_id dedup for this event. Verify value and currency fields are
   present and correct. Confirm transaction_id is a non-identifying order UUID. Confirm no
   personal data in any parameter.

Pass criteria for each step:
- The event fires exactly once per action.
- The event name matches the mapping in sections 2 and 4.
- All required parameters are present and non-empty.
- No personal or sensitive data appears in any parameter, URL, or logged value.
- For deduped events, the event_id on the Pixel call and the CAPI call match exactly.
- The event appears in the BigQuery test export within the expected latency window (typically
  24 hours for GA4 standard export; confirm with the GA4 MCP configuration).

Fail criteria: if any event fires more than once per action, fires with a mismatched event_id,
or contains a personal data value in any parameter, the test is a hard stop. Fix and retest the
specific event before advancing. Do not proceed to go-live with a failing test event.

Gate-side events (submit, confirm) cannot be fully tested until the gate_platform is confirmed.
The web surface test covers the client-side Pixel and GA4 fires; the CAPI server-side call test
is blocked on the platform until the credential and vendor are confirmed.

Mobile events (Apple IAP, Google Play) cannot be tested until the mobile mapping is resolved
(see section 6, open item). Web events are testable and are the go-live blocker; mobile testing
runs as a separate track once the mapping is confirmed.

---

## 9. Handoff routing

- event_plan: this document feeds the event_plan field of the conversion-package owned by
  conversion-engineer. The surfaces (page, gate) are conversion-engineer's; the event
  definitions and mappings here are data-tracking-engineer's.
- compliance-privacy-reviewer: this document routes to compliance-privacy-reviewer before any
  go-live. The reviewer must confirm no personal data risk in any parameter and that the
  server-side hashed signal approach for CAPI matching (if used) meets Saudi PDPL requirements.
  The data-residency decision is an open item and blocks the gate-side CAPI wiring.
- analytics-reporter: the BigQuery queries in section 7 feed analytics-reporter for campaign
  monitoring. The primary query is Q1 (daily subscription conversions) measured against the
  success_metric target that Ahmed confirms.
- human-gate: writing tracking to production, including Pixel code deployment, CAPI endpoint
  wiring, GA4 event configuration, and any BigQuery production query or view creation, is a
  gated action. The human gate (Ahmed) clears each action. This document is the plan only.
  Nothing has been written to production.

---

## 10. Open items summary (carry to the human gate)

| Item                          | Blocks                                           | Owner                   |
|-------------------------------|--------------------------------------------------|-------------------------|
| gate_platform not confirmed   | submit/confirm CAPI wiring, gate-side SDK calls  | Ahmed (brief)           |
| Saudi PDPL data-residency     | CAPI hashed signals, any server-side data send   | Ahmed + compliance      |
| EMAIL_WHATSAPP_API_KEY        | gate-side send wiring                            | Ahmed (credential)      |
| mobile mapping to-confirm     | Apple IAP and Google Play event wiring           | data-tracking-engineer once platform confirmed |
| video_start event definition  | Masterclass plays warehouse query (Q4)           | conversion-engineer     |
| paid spend data pipeline      | cost per subscription warehouse query (Q6)       | performance-marketer    |
| success_metric target number  | absolute monitoring threshold                    | Ahmed (brief)           |
| prod write gated              | all production tracking writes                   | human-gate (Ahmed)      |
