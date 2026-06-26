# Tracking Plan: Summer of Skills, full-stack non-payer campaign

## Envelope

- campaign_id: 2026-07-summer-nonpayer
- produced_by: data-tracking-engineer
- streams: 6 events + 8 warehouse
- status: draft
- qa:
  - skill_eval: passed (structure, no-personal-data rule, mobile open item, platform open item, test plan, warehouse anchored to success_metric)
  - arabic_qa: na (plumbing artifact, no customer-facing copy)
  - english_qa: na (plumbing artifact, no customer-facing copy)
  - design_qa: na (no visual asset)
  - web_design_qa: na (no web surface)
  - compliance: pending (routes to compliance-privacy-reviewer before go-live; Saudi PDPL and data-residency for any hashed signal or gate-side send are open items)
  - brand_qa: na (plumbing artifact)
- open_items:
  - platform-not-confirmed: gate_platform (email and WhatsApp platform vendor) is OPEN ITEM. Gate-side submit and confirm CAPI wiring, and any lifecycle engagement-event wiring that depends on the platform SDK or API, are blocked until the vendor is named and the Saudi PDPL data-residency decision is confirmed.
  - mobile-mapping-to-confirm: Apple IAP and Google Play event mapping is flagged to-confirm for every event in this plan. Not guessed anywhere in this document.
  - access-not-granted: BigQuery MCP access is not confirmed. All warehouse queries are specified and gated; they are added and run only on approval.
  - Saudi-PDPL-data-residency: compliance and residency posture for gate-side sends, any hashed match-key upload, and CAPI server-side signals must be confirmed by compliance-privacy-reviewer before go-live. This open item applies to the confirm and subscription_start CAPI calls in particular.
  - EMAIL_WHATSAPP_API_KEY-not-issued: the runtime credential for the gate and push platform is not yet issued. Gate-side send wiring is blocked.
  - success-metric-target-unset: the primary conversion target NUMBER and dates are ASSUMPTION (see brief and strategy-artifact section 2). The warehouse queries are anchored to the metric definition; the absolute target awaits Ahmed.
  - paid-spend-data-pipeline: the pipeline and table schema for paid spend (Meta, Google, TikTok) needed for the cost-per-subscription query are not confirmed.
  - prod-write-gated: writing tracking to production is a human-gate action. This document is the plan only. Nothing fires in production until the human gate clears each write.
- brief_refs:
  - objective: convert and re-engage roughly 18,000 owned non-paying contacts into paying Maharat subscribers, and acquire new subscribers across paid and organic, using the breadth of the instructor roster as the lead hook
  - success_metric: paid subscription conversions attributable to the campaign within the confirmed flight window (primary, target NUMBER is ASSUMPTION); signup-gate completions, masterclass intro plays, owned-flow open and click rates, cost per subscription on paid (secondaries)
  - campaign_id: 2026-07-summer-nonpayer
  - channels: email and app push (owned, primary), paid (Meta and Instagram primary, TikTok, Google and YouTube secondary), organic social, SEO, ASO, content, PR
  - signup_gate: email or WhatsApp capture for new acquisition (platform OPEN ITEM); for owned non-payers the contact exists and the gate is the subscription step
  - gate_platform: OPEN ITEM
  - start_date: ASSUMPTION 2026-07-01 (confirm)
  - end_date: ASSUMPTION 2026-08-31 (confirm)

---

## 1. Surfaces and fire conditions

This plan covers seven events: the four core funnel events (page_view, gate_view, submit, confirm), one post-signup revenue event (subscription_start), and two engagement events this campaign specifically needs: masterclass_play_start (the free chapter 1 intro play that the strategy-artifact names as a secondary metric and the campaign's low-friction top-of-funnel try) and interest_field_select (the per-field interest signal from the new-acquisition interest-cut flow). Fire conditions are tied to surfaces owned by conversion-engineer. If a surface changes, the fire condition here must be updated before go-live.

### 1.1 page_view

- Description: the campaign landing page (the summer campaign hub page, or a per-field or per-instructor class page used as a campaign entry point) has loaded and is visible to the user.
- Fire condition: fires once per page session on DOMContentLoaded (or equivalent page-load signal) on any campaign entry-point URL. Does not re-fire on navigation within a SPA without a full page transition.
- Surfaces: the summer campaign hub page and any per-field masterclass page used as a campaign landing point (e.g. maharat.com/[en|ar]/class/[domain]/[instructor]-teaches-[field]). Exact URL set is conversion-engineer's to define.

### 1.2 gate_view

- Description: the signup gate (the email or WhatsApp capture step for new acquisition) is visible to the user.
- Fire condition: fires once per session when the gate element enters the viewport or the gate modal or panel renders. Does not fire again if the gate is scrolled out and back in within the same session.
- Dependency: gate_platform is OPEN ITEM. The gate surface is defined by conversion-engineer. This event fires on the web surface regardless of platform. Gate-side SDK wiring (i.e. the platform's own tracking calls) blocks on platform confirmation.

### 1.3 submit

- Description: the user has submitted their contact information at the signup gate (the opt-in form is submitted).
- Fire condition: fires once on successful form submission (no client-side validation error outstanding). Fires on the submit action, not on the downstream server confirmation.
- PII rule: no email address, phone number, name, or any personal value in any event parameter. The event signals that a submission occurred; the contact value stays in the backend only.

### 1.4 confirm

- Description: the signup is confirmed (the server has accepted the submission and the user has reached the confirmation state, for example a success message or a redirect to the plans page).
- Fire condition: fires once per session on receipt of the server success signal for the gate submission. In a server-side flow this is the Conversions API call from the backend; in a client-side flow it fires on the success callback after the server returns 200.
- PII rule: same as submit. No personal data in any parameter.

### 1.5 subscription_start

- Description: the user has completed a paid subscription purchase. This is the primary revenue event and the event tied to the campaign primary success_metric.
- Fire condition: fires once per transaction on the order confirmation page or on the server-side purchase confirmation webhook.
- PII rule: this event carries a non-identifying event_id and the value and currency fields for conversion-value reporting. No user-identifiable fields in any parameter passed to any analytics or ad platform. Any hashed match-key signals for CAPI (for example hashed email for matching) are a server-side backend operation and must be reviewed by compliance-privacy-reviewer before go-live, subject to the Saudi PDPL data-residency open item.

### 1.6 masterclass_play_start

- Description: the user has started playing any masterclass chapter, and specifically chapter 1 (the free intro chapter, titled "الماهر" or "الماهرة" or equivalent on the class page) which is the strategy-artifact's stated top-of-funnel engagement signal and a secondary success metric.
- Fire condition: fires once per chapter-play initiation per session (i.e. when video playback begins, not on pause or seek). For chapter 1 specifically, the chapter_number parameter carries the value 1 so the warehouse can filter intro plays separately from subsequent chapter plays.
- Parameters: campaign_id, chapter_number (integer, 1 for the free intro), class_id (non-identifying class identifier, for example "ragheb-alama-music" or equivalent slug). No user-identifiable values.
- Surfaces dependency: the video player surface on the class page must expose a play-start event hook. Conversion-engineer defines the exact surface hook; data-tracking-engineer wires the event fire against it.

### 1.7 interest_field_select

- Description: the user has indicated a per-field interest signal in the new-acquisition flow, for example by clicking on a field or instructor domain card on the campaign hub, by tapping a per-field CTA, or by engaging with a field-specific interest selector if one is built. This is the signal the strategy-artifact's interest-cut segmentation (music, cooking, acting, makeup, business, styling, marketing) can read back from the event stream.
- Fire condition: fires once per distinct field selection interaction per session. If the user selects multiple fields in a session, one event fires per selection with the field_id parameter distinguishing them. Does not fire on passive scroll past a card; fires only on an active interaction (click or tap).
- Parameters: campaign_id, field_id (non-identifying slug, for example "music", "cooking", "acting", "makeup", "business", "styling", "marketing"). No user-identifiable values. No instructor name is embedded in the event parameter; field_id is a category slug only.
- PII rule: field_id is a category label, not a user identifier. Never log a user account ID, email, or any personal identifier alongside this event parameter.
- Surfaces dependency: conversion-engineer defines whether a field-selector surface exists on the campaign hub. If no such surface is built, this event is not fired. Flag to conversion-engineer at handoff.

---

## 2. Meta Pixel and Conversions API mapping

All seven events have a Pixel-side name and, where server-side firing is warranted, a CAPI-side name. Names on both sides must match on every deduped event. Events that fire only on the browser (page_view, gate_view, masterclass_play_start, interest_field_select) do not require CAPI calls; the remaining events benefit from or require CAPI for reliability.

| Funnel event           | Meta Pixel event name  | Meta CAPI event name   | Notes                                                                       |
|------------------------|------------------------|------------------------|-----------------------------------------------------------------------------|
| page_view              | PageView               | (not required)         | Standard Meta event. Fire on page load. Browser-only.                       |
| gate_view              | ViewContent            | (not required)         | content_name: "signup-gate". No user data. Browser-only.                    |
| submit                 | Lead                   | Lead                   | Standard lead event. CAPI recommended for reliability. No PII in params.    |
| confirm                | CompleteRegistration   | CompleteRegistration   | Server-side CAPI preferred as source of truth. Dedup required (section 3).  |
| subscription_start     | Purchase               | Purchase               | Revenue event. value and currency required. Dedup required (section 3).     |
| masterclass_play_start | ViewContent            | (not required)         | content_name: "masterclass-play", content_type: "video". Browser-only.      |
| interest_field_select  | ViewContent            | (not required)         | content_name: field_id value (e.g. "field-music"). Browser-only.            |

Notes on the mapping:

- gate_view uses ViewContent because Meta has no standard gate-visible event. The content_name parameter identifies it as the signup gate.
- masterclass_play_start also uses ViewContent with a distinct content_name and content_type to distinguish it from gate_view in the Pixel event stream. If a custom Meta event name is preferred for this campaign, that is a decision for conversion-engineer and data-tracking-engineer to align on at handoff; the table above shows the standard-event path.
- interest_field_select uses ViewContent with content_name set to the field slug (e.g. "field-music"). This distinguishes per-field interest signals in Meta's reporting without encoding any user identifier.
- confirm maps to CompleteRegistration, the closest standard Meta event for a completed opt-in before purchase. The CAPI call is the source of truth for this event; the Pixel call uses the matching event_id for dedup.
- subscription_start maps to Meta Purchase. The value field carries the subscription price (the confirmed public price once Ahmed confirms it; it is ASSUMPTION and must not be guessed or invented here). The currency field is the transaction currency. These are non-identifying order values, not user data.

---

## 3. Event_id deduplication approach

Any event fired by both the Meta Pixel (browser-side) and the Conversions API (server-side) must carry a shared, non-identifying event_id so Meta deduplicates it and avoids double-counting. This applies most critically to subscription_start (Purchase) and confirm (CompleteRegistration), and conditionally to submit (Lead) if CAPI is wired for it.

### Generation rule

- The event_id is a randomly generated UUID version 4 or equivalent non-sequential, non-guessable identifier.
- It is generated once per event occurrence, server-side, before the page renders the client-side Pixel call.
- The server passes the event_id to the page (e.g. in a data layer push or a page variable) so the Pixel call and the CAPI call carry the same value.
- The event_id must not contain or encode any user identifier, session token that maps to a user, or any personal data. It is opaque.

### Pixel-side syntax

```
fbq('track', 'Purchase', { value: <price>, currency: '<ISO-code>', ... }, { eventID: '<uuid>' })
```

### CAPI-side syntax

The event_id field in the Conversions API payload carries the same uuid. Both must match exactly for Meta to deduplicate. A mismatch results in double-counting.

### Events requiring dedup

| Event                  | Pixel fires? | CAPI fires?      | Dedup required?                  |
|------------------------|-------------|------------------|----------------------------------|
| page_view              | yes         | no               | no                               |
| gate_view              | yes         | no               | no                               |
| submit                 | yes         | recommended      | yes if both paths fire           |
| confirm                | yes         | yes              | yes                              |
| subscription_start     | yes         | yes              | yes                              |
| masterclass_play_start | yes         | no               | no                               |
| interest_field_select  | yes         | no               | no                               |

Recommendation: for confirm and subscription_start, treat the CAPI call as the source of truth and use the Pixel call with the matching event_id as the browser-side signal only. If the browser-side Pixel call fails (e.g. due to an ad blocker), the CAPI call still fires and the conversion is captured.

---

## 4. GA4 mapping

| Funnel event           | GA4 event name             | GA4 parameters (non-identifying only)                                                                     |
|------------------------|----------------------------|-----------------------------------------------------------------------------------------------------------|
| page_view              | page_view                  | page_location (URL, no user data in query params), campaign_id                                            |
| gate_view              | snp_gate_view              | campaign_id, content_group: "signup-gate"                                                                 |
| submit                 | generate_lead              | campaign_id, method: "email" or "whatsapp" (once platform confirmed)                                      |
| confirm                | sign_up                    | campaign_id                                                                                               |
| subscription_start     | purchase                   | transaction_id (non-identifying order UUID), value, currency, campaign_id, items[]: item_id "maharat-subscription-[plan]", item_name "maharat-subscription" |
| masterclass_play_start | snp_masterclass_play_start | campaign_id, chapter_number (integer), class_id (non-identifying slug)                                    |
| interest_field_select  | snp_interest_field_select  | campaign_id, field_id (category slug, e.g. "music", "cooking", "acting")                                  |

Notes on the GA4 mapping:

- page_view is the GA4 automatic event but is listed here to confirm that campaign_id is appended via the data layer. Use the GA4 config or a gtag data layer push to attach campaign_id to every event on campaign-entry-point page sessions.
- snp_gate_view and other snp_ prefixed events are custom events using the "snp" prefix for this campaign (Summer of Skills Non-Payer). This keeps them distinct from GA4 recommended event names and from any other campaign's custom events in the same GA4 property.
- generate_lead is the GA4 recommended event for a lead capture.
- sign_up is the GA4 recommended event for a completed registration.
- purchase is the GA4 standard e-commerce event for the revenue conversion. transaction_id must be a non-identifying order identifier (e.g. a UUID or an auto-incremented order ID). The items array carries item_id and item_name as non-identifying product identifiers. item_id should include the plan slug (e.g. "maharat-subscription-1month") once the plan type is confirmed; it is ASSUMPTION until Ahmed confirms the plan(s) the campaign leads with.
- snp_masterclass_play_start is a custom event. chapter_number carries 1 for the free intro chapter so the warehouse can isolate intro plays. class_id is a non-identifying slug (e.g. "ragheb-alama-music"), not a user identifier.
- snp_interest_field_select is a custom event. field_id carries a category slug only, never an instructor name or a user identifier.
- campaign_id is attached to all events so the BigQuery export can filter by campaign without relying solely on UTM parameters.

### UTM parameters

All paid, owned email, and organic traffic to campaign entry-point pages must carry UTM parameters. The utm_campaign value must be "2026-07-summer-nonpayer" consistently across all paid, email, app-push, and organic links. utm_source and utm_medium follow the channel. UTM values are non-identifying; they describe the traffic source, not the user.

No personal data (no email address, no phone number, no name, no user ID or subscriber ID of any kind) is ever placed in a UTM parameter or any URL query string that fires into a tracking call.

If the email or app-push platform appends subscriber-identifying parameters to URLs (e.g. some platforms append a subscriber ID or encoded email to links for click tracking), those parameters must be stripped before the GA4 event fires. This is a hard stop; confirm with compliance-privacy-reviewer before go-live.

---

## 5. Parameters (full list, annotated for PII status)

Every parameter used across all events is listed here with its PII status. Any parameter not on this list must be reviewed before being added to any event or URL.

| Parameter       | Events used in                           | Value type                                        | PII status                                      |
|-----------------|------------------------------------------|---------------------------------------------------|-------------------------------------------------|
| campaign_id     | all events                               | "2026-07-summer-nonpayer"                         | non-identifying                                 |
| event_id        | confirm, subscription_start (+ submit if CAPI wired) | UUID v4, generated server-side         | non-identifying                                 |
| content_group   | gate_view (GA4)                          | "signup-gate"                                     | non-identifying                                 |
| content_name    | gate_view (Pixel), masterclass_play_start (Pixel), interest_field_select (Pixel) | string descriptor (see mapping) | non-identifying |
| content_type    | masterclass_play_start (Pixel)           | "video"                                           | non-identifying                                 |
| method          | submit (GA4)                             | "email" or "whatsapp" (once platform confirmed)   | non-identifying                                 |
| transaction_id  | subscription_start (GA4 purchase)        | non-identifying order UUID                        | non-identifying                                 |
| value           | subscription_start                       | numeric subscription price (confirmed public price only) | non-identifying order value               |
| currency        | subscription_start                       | ISO 4217 currency code                            | non-identifying                                 |
| item_id         | subscription_start (GA4 items array)     | "maharat-subscription-[plan]" slug                | non-identifying                                 |
| item_name       | subscription_start (GA4 items array)     | "maharat-subscription"                            | non-identifying                                 |
| chapter_number  | masterclass_play_start                   | integer (1 for free intro chapter)                | non-identifying                                 |
| class_id        | masterclass_play_start                   | non-identifying class slug (e.g. "ragheb-alama-music") | non-identifying                            |
| field_id        | interest_field_select                    | category slug (e.g. "music", "cooking", "acting") | non-identifying                                 |
| page_location   | page_view (GA4)                          | page URL, no user data in query params            | non-identifying (see note)                      |

Note on page_location: the URL logged in page_location must never contain an email address, phone number, session token, or any user identifier in query parameters. If the platform appends user-identifying parameters to URLs, those parameters must be stripped before the GA4 event fires. Hard stop; confirm with compliance-privacy-reviewer before go-live.

Note on value: the value parameter carries the subscription price. This is an order-level value, not a user identifier. It must match the confirmed public price only once Ahmed confirms price and currency. Until confirmed, value is left as a placeholder and must not be guessed or invented.

Explicitly prohibited in all parameters and tracking calls:
- Email address (in any form, including partial or encoded)
- Phone number
- Full name or partial name
- User account ID or internal subscriber ID in any form that links to an individual
- Device identifier or advertising ID in parameters (these belong in CAPI match key fields only, server-side, never in URL query strings)
- Any value that can re-identify a user when combined with other logged fields

---

## 6. Mobile mapping (Apple IAP and Google Play)

The mobile event mapping for Apple In-App Purchase (IAP) and Google Play In-App Billing is flagged as a to-confirm open item for every event in this plan. It is not guessed here.

This open item requires confirmation of:
- Which Maharat app builds (iOS, Android, or both) are in scope for the summer campaign traffic.
- The subscription product ID(s) in the App Store and Google Play consoles for each plan the campaign leads with (1, 3, and 12 month plans; plan selection is ASSUMPTION, confirm with Ahmed).
- How the in-app purchase event is passed to Meta CAPI and GA4 (e.g. via server-to-server using a Firebase SDK, Adjust, or a direct webhook from the payment backend).
- That the same event_id dedup approach from section 3 is applied to mobile purchase events so Pixel and CAPI dedup works for in-app conversions, not only for web.
- The masterclass_play_start and interest_field_select events: whether the in-app equivalents of these interactions are tracked via the same GA4 property (Firebase/GA4 integration) or a separate mobile analytics tool, and whether CAPI matching is in scope for mobile.

This open item must be resolved before any go-live that drives traffic to the app install or in-app purchase flow. Web events are planned and ready regardless.

---

## 7. Warehouse references (BigQuery queries for monitoring)

All queries below are anchored to the primary success_metric from the strategy-artifact: paid subscription conversions attributable to the campaign within the confirmed flight window. Secondary metrics (gate completions, masterclass intro plays, interest-field signals, cost per subscription) are described as supplementary reads.

The queries assume a standard GA4 BigQuery export schema: events_YYYYMMDD tables in the analytics dataset, with event_name, event_params, user_pseudo_id, and event_date fields. Table names and dataset identifiers are placeholders (your_project.your_ga4_dataset); replace with the actual project and dataset before running. Access is via the BigQuery MCP, which is not yet approved; these queries are specified and gated and are added on approval. They are not run in this document.

The flight date range uses the ASSUMPTION start and end dates. Replace with the confirmed dates.

The absolute conversion target number is ASSUMPTION (see brief and strategy-artifact section 2). These queries return actual counts; the target is compared manually or in a monitoring view once Ahmed confirms the number.

---

### Q1. Daily subscription conversions attributable to the campaign (primary success_metric)

Monitoring question: how many subscription_start (purchase) events fired each day where the session was attributed to this campaign?

```sql
SELECT
  event_date,
  COUNT(*) AS subscription_starts
FROM
  `your_project.your_ga4_dataset.events_*`
WHERE
  _TABLE_SUFFIX BETWEEN '20260701' AND '20260831'
  AND event_name = 'purchase'
  AND (
    SELECT value.string_value
    FROM UNNEST(event_params)
    WHERE key = 'campaign_id'
  ) = '2026-07-summer-nonpayer'
GROUP BY
  event_date
ORDER BY
  event_date ASC
```

Note: this counts purchase events tagged with campaign_id. For cross-channel attribution, supplement with a UTM-based session filter or apply a first-touch or last-touch attribution model at the session level.

---

### Q2. Cumulative subscription conversions over the flight (primary success_metric, progress read)

Monitoring question: how many total subscription_start events have fired since campaign start, as a running total?

```sql
SELECT
  event_date,
  COUNT(*) AS daily_subscription_starts,
  SUM(COUNT(*)) OVER (ORDER BY event_date ASC) AS cumulative_subscription_starts
FROM
  `your_project.your_ga4_dataset.events_*`
WHERE
  _TABLE_SUFFIX BETWEEN '20260701' AND '20260831'
  AND event_name = 'purchase'
  AND (
    SELECT value.string_value
    FROM UNNEST(event_params)
    WHERE key = 'campaign_id'
  ) = '2026-07-summer-nonpayer'
GROUP BY
  event_date
ORDER BY
  event_date ASC
```

This is the read analytics-reporter uses to track progress against the confirmed target number over the summer flight window.

---

### Q3. Full funnel counts by day (all seven events)

Monitoring question: how many events fired at each funnel stage per day, and where do users drop off?

```sql
SELECT
  event_date,
  COUNTIF(event_name = 'page_view') AS page_views,
  COUNTIF(event_name = 'snp_gate_view') AS gate_views,
  COUNTIF(event_name = 'generate_lead') AS submits,
  COUNTIF(event_name = 'sign_up') AS confirms,
  COUNTIF(
    event_name = 'purchase'
    AND (
      SELECT value.string_value
      FROM UNNEST(event_params)
      WHERE key = 'campaign_id'
    ) = '2026-07-summer-nonpayer'
  ) AS subscription_starts,
  COUNTIF(event_name = 'snp_masterclass_play_start') AS masterclass_plays,
  COUNTIF(
    event_name = 'snp_masterclass_play_start'
    AND (
      SELECT value.int_value
      FROM UNNEST(event_params)
      WHERE key = 'chapter_number'
    ) = 1
  ) AS chapter_1_intro_plays,
  COUNTIF(event_name = 'snp_interest_field_select') AS interest_field_selections
FROM
  `your_project.your_ga4_dataset.events_*`
WHERE
  _TABLE_SUFFIX BETWEEN '20260701' AND '20260831'
  AND (
    SELECT value.string_value
    FROM UNNEST(event_params)
    WHERE key = 'campaign_id'
  ) = '2026-07-summer-nonpayer'
GROUP BY
  event_date
ORDER BY
  event_date ASC
```

---

### Q4. Signup-gate completions by day (secondary metric)

Monitoring question: how many users completed the signup gate (reached the confirm step) each day?

```sql
SELECT
  event_date,
  COUNT(*) AS gate_completions
FROM
  `your_project.your_ga4_dataset.events_*`
WHERE
  _TABLE_SUFFIX BETWEEN '20260701' AND '20260831'
  AND event_name = 'sign_up'
  AND (
    SELECT value.string_value
    FROM UNNEST(event_params)
    WHERE key = 'campaign_id'
  ) = '2026-07-summer-nonpayer'
GROUP BY
  event_date
ORDER BY
  event_date ASC
```

---

### Q5. Masterclass chapter 1 intro plays by class and by day (secondary metric)

Monitoring question: how many times did users start the free chapter 1 intro of each class, by class, per day?

```sql
SELECT
  event_date,
  (
    SELECT value.string_value
    FROM UNNEST(event_params)
    WHERE key = 'class_id'
  ) AS class_id,
  COUNT(*) AS chapter_1_intro_plays
FROM
  `your_project.your_ga4_dataset.events_*`
WHERE
  _TABLE_SUFFIX BETWEEN '20260701' AND '20260831'
  AND event_name = 'snp_masterclass_play_start'
  AND (
    SELECT value.int_value
    FROM UNNEST(event_params)
    WHERE key = 'chapter_number'
  ) = 1
  AND (
    SELECT value.string_value
    FROM UNNEST(event_params)
    WHERE key = 'campaign_id'
  ) = '2026-07-summer-nonpayer'
GROUP BY
  event_date,
  class_id
ORDER BY
  event_date ASC,
  chapter_1_intro_plays DESC
```

This query supports the secondary metric (masterclass intro plays) from the strategy-artifact and enables analytics-reporter to see which fields and classes pull the most top-of-funnel engagement.

---

### Q6. Interest-field signals by field and by day (secondary metric, new-acquisition interest cut)

Monitoring question: which field categories are users selecting most in the new-acquisition interest cut, per day?

```sql
SELECT
  event_date,
  (
    SELECT value.string_value
    FROM UNNEST(event_params)
    WHERE key = 'field_id'
  ) AS field_id,
  COUNT(*) AS field_selections
FROM
  `your_project.your_ga4_dataset.events_*`
WHERE
  _TABLE_SUFFIX BETWEEN '20260701' AND '20260831'
  AND event_name = 'snp_interest_field_select'
  AND (
    SELECT value.string_value
    FROM UNNEST(event_params)
    WHERE key = 'campaign_id'
  ) = '2026-07-summer-nonpayer'
GROUP BY
  event_date,
  field_id
ORDER BY
  event_date ASC,
  field_selections DESC
```

Data-access note: this query is only useful if the interest_field_select surface is built by conversion-engineer. If the surface does not exist, this query returns no rows.

---

### Q7. Funnel conversion rates, whole-flight summary (drop-off view for monitoring)

Monitoring question: what percentage of page_view sessions reached each subsequent funnel step across the whole flight?

```sql
WITH funnel AS (
  SELECT
    SUM(CASE WHEN event_name = 'page_view' THEN 1 ELSE 0 END) AS page_views,
    SUM(CASE WHEN event_name = 'snp_gate_view' THEN 1 ELSE 0 END) AS gate_views,
    SUM(CASE WHEN event_name = 'generate_lead' THEN 1 ELSE 0 END) AS submits,
    SUM(CASE WHEN event_name = 'sign_up' THEN 1 ELSE 0 END) AS confirms,
    SUM(CASE WHEN event_name = 'purchase' THEN 1 ELSE 0 END) AS subscription_starts
  FROM
    `your_project.your_ga4_dataset.events_*`
  WHERE
    _TABLE_SUFFIX BETWEEN '20260701' AND '20260831'
    AND (
      SELECT value.string_value
      FROM UNNEST(event_params)
      WHERE key = 'campaign_id'
    ) = '2026-07-summer-nonpayer'
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

### Q8. Cost per subscription by day (secondary metric, requires paid spend data join)

Monitoring question: what was the cost per subscription from paid channels each day?

Natural language: join daily paid spend (from Meta, Google, TikTok) against daily subscription_start counts for this campaign, divide spend by conversions. The paid spend table is a separate data source, not a GA4 export table.

```sql
-- Pattern query. Replace your_project.your_spend_dataset.spend_table with the actual spend table.
-- The spend table schema (date, campaign_id, spend) must be confirmed before this query runs.
SELECT
  s.event_date,
  s.total_spend,
  c.subscription_starts,
  ROUND(SAFE_DIVIDE(s.total_spend, c.subscription_starts), 2) AS cost_per_subscription
FROM
  (
    SELECT
      date AS event_date,
      SUM(spend) AS total_spend
    FROM `your_project.your_spend_dataset.spend_table`
    WHERE campaign_id = '2026-07-summer-nonpayer'
    GROUP BY date
  ) s
JOIN
  (
    SELECT
      event_date,
      COUNT(*) AS subscription_starts
    FROM `your_project.your_ga4_dataset.events_*`
    WHERE
      _TABLE_SUFFIX BETWEEN '20260701' AND '20260831'
      AND event_name = 'purchase'
      AND (
        SELECT value.string_value
        FROM UNNEST(event_params)
        WHERE key = 'campaign_id'
      ) = '2026-07-summer-nonpayer'
    GROUP BY event_date
  ) c
ON s.event_date = c.event_date
ORDER BY s.event_date ASC
```

Open items: the paid spend data pipeline and table schema must be confirmed before this query runs. The budget is also OPEN ITEM in the brief, so the absolute cost-per-subscription target is not set; this query will return a number but has nothing confirmed to compare against until Ahmed sets the target.

---

### Privacy note on all warehouse queries

All queries select only the fields the metric needs. No personal data (no email address, no phone number, no name, no user account ID or subscriber ID) appears in any query output. user_pseudo_id from the GA4 export is a pseudonymous identifier and is not selected in any of the queries above; if it is needed for session-level deduplication in a future iteration, that use case must be reviewed by compliance-privacy-reviewer before the query runs. No query output is exported or shared in a format that could re-identify individual users.

---

## 8. Test plan

Every event must fire once, in order, in a test session, before any production go-live. The test session is run in a staging or QA environment with the BigQuery export in debug mode and a Meta Pixel Helper or Meta Test Events tool active. Test events must be tagged and excluded from production monitoring queries.

Test sequence, in order:

1. Load a campaign entry-point page (the summer hub page or a per-field class page). Verify page_view fires in GA4 DebugView and in Meta Pixel Helper. Confirm campaign_id parameter is present. Confirm page_location contains no personal data in query parameters. Confirm the event fires once per page load and does not re-fire on in-page navigation.

2. Scroll to or trigger the signup gate. Verify gate_view fires once: snp_gate_view in GA4 (content_group: "signup-gate"), ViewContent in Meta Pixel (content_name: "signup-gate"). Confirm no personal data in any parameter. Confirm the event does not re-fire if the gate is scrolled out and back in.

3. Start playing a masterclass chapter 1 intro. Verify masterclass_play_start fires once: snp_masterclass_play_start in GA4 with chapter_number = 1 and a valid class_id slug; ViewContent in Meta Pixel with content_name matching the class slug and content_type: "video". Confirm no personal data in any parameter.

4. Interact with a field interest selector (if the surface is built). Verify interest_field_select fires once per field selection: snp_interest_field_select in GA4 with a valid field_id slug; ViewContent in Meta Pixel with content_name matching the field slug. Confirm no personal data in any parameter.

5. Complete the signup gate form and submit. Verify submit fires: generate_lead in GA4 (campaign_id present), Lead in Meta Pixel and CAPI (if CAPI is wired for this event). Confirm no email address, phone number, or name appears in any parameter. If CAPI is wired for submit, verify the event_id in the Pixel call matches the event_id in the CAPI payload.

6. Reach the confirmation state. Verify confirm fires: sign_up in GA4 (campaign_id present), CompleteRegistration in Meta Pixel and CAPI. Verify event_id dedup: the Pixel event_id and the CAPI event_id are identical. Confirm no personal data in any parameter.

7. Complete a test subscription purchase. Verify subscription_start fires: purchase in GA4 with transaction_id (a non-identifying order UUID), value, currency, campaign_id, and items[] populated; Purchase in Meta Pixel and CAPI with value, currency, and matching event_id. Verify event_id dedup for this event. Confirm transaction_id is not a user identifier. Confirm value matches the confirmed public price (blocked on price confirmation). Confirm no personal data in any parameter.

Pass criteria for each step:
- The event fires exactly once per action.
- The event name matches the mapping in sections 2 and 4.
- All required parameters are present and non-empty.
- No personal or sensitive data appears in any parameter, URL, or logged value.
- For deduped events, the event_id on the Pixel call and the CAPI call match exactly.
- The event appears in the BigQuery debug export within the expected latency window.

Fail criteria: if any event fires more than once per action, fires with a mismatched event_id, contains a personal data value in any parameter, or is missing a required parameter, the test is a hard stop. Fix and retest the specific event before advancing. Do not proceed to go-live with a failing test event.

Gate-side events (submit, confirm) cannot be fully tested for the CAPI server-side call until gate_platform is confirmed. The web surface test covers the client-side Pixel and GA4 fires; the CAPI call test is blocked on platform confirmation.

Mobile events (Apple IAP, Google Play) cannot be tested until the mobile mapping is resolved (section 6, open item). Web events are testable and are the go-live blocker. Mobile testing runs as a separate track once the mapping is confirmed.

---

## 9. Handoff routing

- event_plan: this document fills the event_plan field of the conversion-package owned by conversion-engineer. Surfaces (page, gate, video player, field selector) are conversion-engineer's to define and build; event definitions and mappings here are data-tracking-engineer's.
- compliance-privacy-reviewer: this document routes to compliance-privacy-reviewer before any go-live. The reviewer must confirm no personal data risk in any parameter, that the server-side hashed signal approach for CAPI matching (if used) meets Saudi PDPL requirements, and that any URL-level subscriber-ID stripping required by the email or push platform is in place. The Saudi PDPL data-residency open item blocks the CAPI server-side wiring until confirmed.
- analytics-reporter: the warehouse queries in section 7 feed analytics-reporter for campaign monitoring. Q1 and Q2 are the primary reads (daily and cumulative subscription_start conversions, measured against the success_metric target Ahmed confirms). Q3 through Q7 are supplementary.
- human-gate: writing tracking to production, including Pixel code deployment, CAPI endpoint wiring, GA4 event configuration, and any BigQuery production query or view creation, is a gated action. The human gate (Ahmed) clears each action. This document is the plan only. Nothing has been written to production.

---

## 10. Open items summary (carry to the human gate)

| Item                                     | Blocks                                                               | Owner                                            |
|------------------------------------------|----------------------------------------------------------------------|--------------------------------------------------|
| gate_platform not confirmed              | submit/confirm CAPI wiring, gate-side SDK calls, platform engagement-event wiring | Ahmed (brief)                       |
| Saudi PDPL data-residency                | CAPI hashed signals, any server-side data send or match-key upload   | Ahmed + compliance-privacy-reviewer              |
| EMAIL_WHATSAPP_API_KEY not issued        | gate-side send wiring, platform credential                           | Ahmed (credential)                               |
| mobile mapping to-confirm                | Apple IAP and Google Play event wiring for all 7 events              | data-tracking-engineer once platform confirmed   |
| BigQuery MCP access not granted          | all warehouse queries (specified and gated, run on approval)         | Ahmed + engineering                              |
| paid spend data pipeline not confirmed   | Q8 cost-per-subscription query                                       | performance-marketer                             |
| success_metric target number unset       | absolute monitoring threshold for Q1 and Q2                         | Ahmed (brief)                                    |
| price and currency ASSUMPTION            | value parameter in subscription_start, item_id plan slug             | Ahmed (brief)                                    |
| plan type ASSUMPTION                     | item_id plan slug in subscription_start GA4 items[]                  | Ahmed (brief)                                    |
| start_date and end_date ASSUMPTION       | all query date range parameters                                      | Ahmed (brief)                                    |
| interest_field_select surface dependency | snp_interest_field_select event and Q6 query (only useful if surface built) | conversion-engineer                          |
| URL subscriber-ID stripping              | page_location PII risk from email or push platform link parameters   | conversion-engineer + compliance-privacy-reviewer|
| prod write gated                         | all production tracking writes                                       | human-gate (Ahmed)                               |
