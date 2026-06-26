# Tracking plan: Skill Paths first-time soft launch

Tracking package. Owned by data-tracking-engineer. This is a plan only. Nothing in this file
writes to production, fires an event, or instructs any platform. All production writes are
gated actions that run only after the human gate clears. No em dashes. Western numerals.

---

## Envelope

- campaign_id: 2026-07-skill-paths-soft-launch
- produced_by: data-tracking-engineer
- stream: 6 conversion path (plumbing) and 8 warehouse queries
- status: draft
- qa:
  - skill_eval: pending
  - arabic_qa: na (plumbing, not customer copy)
  - brand_qa: na (plumbing, not customer copy)
  - compliance: pending (routes to compliance-privacy-reviewer before go-live)
- open_items:
  - platform-not-confirmed: gate platform (email or WhatsApp) not named; gate-side send and
    engagement event wiring stays blocked until platform is confirmed and residency decision
    (Saudi PDPL) is resolved.
  - mobile-attribution-to-confirm: Apple Search Ads and Google Play attribution wiring, plus MMP
    selection, are flagged to-confirm. See section 5. Do not guess.
  - mmp-selection-open: no MMP (AppsFlyer, Adjust, Branch, or similar) has been named. This
    blocks the app-install attribution wiring. Stop for Ahmed.
  - email-whatsapp-api-key-missing: EMAIL_WHATSAPP_API_KEY credential not yet set; gate-side
    event wiring blocked even after platform is confirmed.
  - success-metric-target-unset: numeric target for primary metric (signups plus installs) not
    set. The brief flags this as ASSUMPTION, stop for Ahmed. The BigQuery queries in section 7
    measure the shape; the target threshold populates once Ahmed confirms it.
  - app-audience-size-open: app user base size is OPEN ITEM (brief sec 3). Affects retargeting
    audience assembly, not the event definitions here.
  - currency-open: SAR or USD not confirmed. Cost-per-signup column in the warehouse query
    is a placeholder until currency and spend figures are confirmed.
- brief_refs:
  - objective and conversion: brief sec 2 (early-access signups plus app installs)
  - success_metric: brief sec 2 (gate completions plus campaign-attributable app installs;
    secondary: activation rate, cost per signup, owned-flow engagement)
  - gate: brief sec 5 (email or WhatsApp signup, app install where app surfaces Skill Paths)
  - flight: brief sec 6 (2026-07-01 to 2026-07-14)
  - constraints: brief sec 8 (no personal or sensitive data in parameters; no invented titles)

---

## 1. Surfaces this plan fires on

Three surface families. The conversion-engineer spec for the landing page and gate is pending
(conversion-package not yet received). This plan defines the events and fire conditions so
the two packages can be merged once the page spec arrives. If the page spec arrives with a
surface not listed here, this plan must be updated before go-live.

| Surface ID | Description |
|---|---|
| SURFACE-WEB-LP | Campaign landing page (early-access gate). |
| SURFACE-APP | Maharat mobile app (iOS and Android), Skill Paths in-app surface. |
| SURFACE-APP-STORE | App store install (Apple App Store, Google Play). Attributed via MMP. |

---

## 2. Event definitions: web funnel (early-access signup)

Four events cover the web conversion funnel. Each event carries a fire condition. The platform
that delivers the gate (email or WhatsApp) is an open item; when it is confirmed, the submit
and confirm fire conditions may need a platform-specific trigger added. The web events are
defined regardless.

### 2.1 page_view

- event name (canonical): maharat_page_view
- fire condition: fires once when the campaign landing page (SURFACE-WEB-LP) has loaded and
  is visible. Fires on load, not on scroll. One fire per page session.
- trigger type: page load (DOM ready or equivalent tag-manager trigger).
- dedup: not applicable (not a conversion event; dedup is only required on submit and confirm).

### 2.2 gate_view

- event name (canonical): maharat_gate_view
- fire condition: fires once when the signup gate element (the email or WhatsApp input form)
  is visible in the viewport. If the gate is below the fold, fires on scroll-into-view, not on
  page load. One fire per page session.
- trigger type: element visibility trigger (tag manager intersection observer or equivalent).
- dedup: not applicable.

### 2.3 submit

- event name (canonical): maharat_ea_submit
- fire condition: fires once when the user submits the early-access signup form (taps or clicks
  the submit control and the form passes client-side validation). Fires before server-side
  confirmation. One fire per submission attempt.
- trigger type: form submit event on the gate element.
- dedup: carries event_id (see section 4). Both Pixel browser-side and CAPI must use the same
  event_id for the same submission. The event_id is generated client-side at fire time, passed
  to CAPI in the server payload, and is never a personal identifier.

### 2.4 confirm

- event name (canonical): maharat_ea_confirm
- fire condition: fires once when the platform confirms the signup (server-side confirmation
  received: the user is in the early-access list). This is the primary conversion event.
  Gate-side trigger depends on the gate platform (OPEN ITEM). For email: fires on confirmed
  opt-in or on server-side confirmation callback. For WhatsApp: fires on platform-confirmed
  delivery or opt-in confirmation. Exact trigger to be finalized once platform is named.
- trigger type: server-side (CAPI preferred for confirm; browser Pixel as backup).
- dedup: carries event_id matched to the submit event_id for the same user session. See
  section 4.

---

## 3. Event definitions: app activation

Three activation events cover the post-install funnel inside the Maharat app. These are
in-app events, not web events. They feed the activation rate secondary metric.

### 3.1 app_install

- event name (canonical): maharat_app_install
- fire condition: fires once when the app is installed and first opened following a
  campaign-attributed click. Attribution is via the MMP (OPEN ITEM, see section 5). The MMP
  fires this postback to Meta and GA4.
- trigger: MMP install postback. Not a direct SDK event from this plan; the MMP handles it.

### 3.2 app_open

- event name (canonical): maharat_app_open
- fire condition: fires on the first app open after install (day-0 open). Distinct from
  subsequent session opens. Can be the standard MMP or Firebase first_open event, mapped to
  this canonical name in the reporting layer.
- trigger: MMP or Firebase first_open, mapped via the MMP postback configuration.

### 3.3 first_lesson (or first_streak_day)

- event name (canonical): maharat_activation
- fire condition: fires once when the user completes their first lesson unit or earns their
  first streak day within Skill Paths. "First lesson" and "first streak day" are both valid
  activation signals per the brief; the product team must confirm which event the app SDK
  emits and under what exact condition. Flagged to-confirm.
- trigger: in-app SDK event. The exact event name in the app SDK is to-confirm with the
  product/engineering team before go-live.
- note: this is the brief's activation secondary metric. The warehouse query in section 7
  uses maharat_activation as the canonical name; map from the SDK event name once confirmed.

---

## 4. Deduplication approach

Any event sent by both the Meta browser Pixel and the Meta Conversions API (CAPI) must carry
a shared, non-identifying event_id so Meta deduplicates correctly and does not double-count.
This applies primarily to submit and confirm.

Rules:

- The event_id is a random or hash-based token generated at the time the client-side event
  fires. It identifies the event instance, not the person.
- The event_id must not encode, derive from, or be traceable to any personal data (no email
  hash, no phone hash, no user ID, no session ID that links to a person).
- The browser Pixel sends the event_id in the eventID field of the fbq call.
- The CAPI payload for the same event sends the identical event_id in the event_id field.
- For confirm, if the CAPI send is delayed (server-side confirmation is async), the event_id
  must be persisted server-side from the submit event and passed into the CAPI confirm payload.
  The mechanism for this persistence is an engineering implementation detail; it is flagged
  here so the implementation does not drop it.
- GA4 does not require cross-source dedup in the same way; the GA4 event is fired once,
  browser-side for page_view and gate_view, and ideally server-side (via Measurement Protocol)
  for confirm.

---

## 5. Meta Pixel and CAPI mapping

Platform not confirmed for the gate send; web event mapping is defined regardless. Gate-side
event wiring remains blocked until the platform is named.

| Canonical event | Meta standard event name | Send method | Notes |
|---|---|---|---|
| maharat_page_view | PageView | Browser Pixel | Standard Pixel PageView on LP load. |
| maharat_gate_view | ViewContent | Browser Pixel | content_name: early_access_gate. No personal data. |
| maharat_ea_submit | Lead | Browser Pixel plus CAPI | Pixel fires client-side; CAPI fires server-side on form submit. Both carry matching event_id. |
| maharat_ea_confirm | Lead (deduplicated) or CompleteRegistration | CAPI preferred, Pixel backup | CAPI fires on server-side confirmation. event_id matches the submit event_id. Platform trigger is an open item. CompleteRegistration may be used if Meta recommends it for signup completions; confirm naming before go-live. |
| maharat_app_install | MobileAppInstall | MMP postback to Meta | Wired via MMP (to-confirm). Not a direct Pixel event. |
| maharat_app_open | (no standard Meta event for first_open; map to custom event app_first_open or skip) | MMP postback | Meta does not have a standard first_open event. Either map to a custom conversion or omit and rely on app_install. Confirm with Meta setup. |
| maharat_activation | CustomEvent: SkillPathsActivation | MMP postback to Meta | Custom conversion event. Name must be registered in the Meta Events Manager before go-live. |

CAPI requirements: hashed user data (email or phone) may be sent in CAPI payloads for match
rate improvement only if the legal basis under Saudi PDPL is confirmed and the user has
consented. Until the residency and consent framework is confirmed, send CAPI payloads with
event_id, event_name, event_time, action_source, and event_source_url only. No hashed PII
in CAPI until compliance-privacy-reviewer clears it.

---

## 6. GA4 mapping

| Canonical event | GA4 event name | Method | Parameters sent |
|---|---|---|---|
| maharat_page_view | page_view (auto-collected) | GA4 auto or gtag | campaign_id, content_group (early_access_lp). No personal data. |
| maharat_gate_view | view_item | gtag or GTM event | campaign_id, item_id: early_access_gate, content_group. No personal data. |
| maharat_ea_submit | generate_lead | gtag or GTM event | campaign_id, form_id: early_access_gate. No personal data. |
| maharat_ea_confirm | sign_up | gtag server-side (Measurement Protocol) preferred | campaign_id, method: early_access. No personal data. |
| maharat_app_install | app_install (Firebase auto) | Firebase SDK or MMP-to-GA4 postback | campaign_id if attributable via UTM. |
| maharat_app_open | first_open (Firebase auto-collected) | Firebase SDK | campaign_id if attributable. |
| maharat_activation | tutorial_complete (or custom: skill_paths_activation) | Firebase SDK in-app event | campaign_id, content_group: skill_paths. |

GA4 stream configuration note: confirm that the web GA4 stream and the Firebase app stream
are linked in the same GA4 property so the funnel can be read across web and app in one
place. If they are not linked, the warehouse query must join two separate export datasets.
This is flagged to the engineering/analytics team for confirmation before go-live.

---

## 7. Parameters: non-identifying only

Every event carries only the parameters in this list. No email address, phone number, name,
user ID, hashed identifier, session ID traceable to a person, or any other personal or
sensitive value appears in any URL parameter, tag payload, or tracking call. This is a hard
stop. If an implementation passes personal data in a parameter, the go-live gate must not
clear until it is removed.

| Parameter | Value format | Example | Personal data? |
|---|---|---|---|
| campaign_id | string, from brief | 2026-07-skill-paths-soft-launch | No |
| content_group | string, surface label | early_access_lp, early_access_gate | No |
| item_id | string, gate identifier | early_access_gate | No |
| form_id | string, form identifier | early_access_gate | No |
| method | string, signup method | early_access | No |
| event_id | random token, event instance | uuid-v4 or equivalent | No (must not encode personal data; see section 4) |

UTM parameters on inbound URLs (utm_source, utm_medium, utm_campaign, utm_content,
utm_term) are standard and non-identifying. They must not carry any personal value.
If the gate platform or lifecycle system appends subscriber identifiers to URLs, those must
be removed from any tracking call. Flag to conversion-engineer and lifecycle-architect.

---

## 8. Mobile app-install attribution (TO-CONFIRM, OPEN ITEM)

This section is a to-confirm open item. Do not wire anything here until both items below
are confirmed by Ahmed and the engineering team.

### 8.1 MMP selection

A Mobile Measurement Partner (MMP) is required to attribute app installs to the paid
campaign (Meta, Google, TikTok). No MMP has been named. Candidates include AppsFlyer,
Adjust, and Branch. The selection must account for:
- Saudi PDPL data-residency requirements (data processing location).
- SDK integration effort on iOS and Android.
- Postback compatibility with Meta, Google, and TikTok.
- Cost relative to the campaign scale.

This is a stop for Ahmed. No MMP wiring proceeds until the tool is named and approved.

### 8.2 Apple Search Ads attribution

Apple Search Ads attribution is handled via the AdServices framework (iOS 14.3 and later)
or the iAd framework (legacy). The MMP handles the integration. The specific attribution
token handling, the postback configuration, and any SKAdNetwork setup are to-confirm once
the MMP is named. Do not guess the mapping.

### 8.3 Google Play attribution

Google Play attribution flows through the Google Play Install Referrer API and the MMP
SDK. Campaign parameters are passed in the install referrer string. The exact postback
configuration to GA4 and Meta is to-confirm once the MMP is named.

### 8.4 SKAdNetwork and privacy thresholds (iOS)

For iOS campaigns on Meta and other paid channels, SKAdNetwork conversion value mapping
must be configured. The mapping of conversion values to campaign events (install, first_open,
activation) is to-confirm with the MMP and the paid-build-engineer. This affects how
app_install and maharat_activation are reported on iOS. Do not configure this without the
MMP selected and the conversion schema agreed.

---

## 9. Test plan

Each event must fire once, in order, in a test session before any go-live. The test session
uses a dedicated test property (GA4 debug view or Meta Test Events) and must not contaminate
production data. Production write requires the human gate to clear first.

| Step | Action | Expected event | Verify on |
|---|---|---|---|
| 1 | Load the campaign landing page URL in a test browser with debug tag active. | maharat_page_view fires once. | GA4 DebugView, Meta Test Events tool. |
| 2 | Scroll until the signup gate is visible (if below fold). | maharat_gate_view fires once. | GA4 DebugView, Meta Test Events tool. |
| 3 | Enter a test value in the gate form and submit. | maharat_ea_submit fires once. Browser Pixel event_id matches CAPI event_id in the test payload log. | GA4 DebugView, Meta Test Events tool, CAPI test event log. |
| 4 | Confirm the test signup from the server side (simulate platform confirmation callback). | maharat_ea_confirm fires once via CAPI. event_id matches step 3. | CAPI test event log, GA4 Measurement Protocol validation. |
| 5 | Install the app on a test device via a test campaign link. | maharat_app_install fires via MMP postback. | MMP dashboard test mode, GA4 DebugView (Firebase). |
| 6 | Open the app for the first time on the test device. | maharat_app_open fires once. | Firebase DebugView. |
| 7 | Complete a test lesson or trigger the streak event in the test app build. | maharat_activation fires once. | Firebase DebugView, GA4 DebugView. |

Additional checks before go-live:
- Confirm no personal data appears in any parameter in any of the above payloads. Check the
  raw event payload in the debug tools, not just the event name.
- Confirm the event_id in step 3 and step 4 are identical in the Meta dedup log.
- Confirm UTM parameters on the landing page URL are captured in GA4 session_traffic_source
  and do not contain personal values.
- Steps 5 through 7 are blocked until the MMP is confirmed (open item, section 8).

---

## 10. BigQuery warehouse queries

The BigQuery dataset is assumed to be the GA4 BigQuery export (events_ table, partitioned by
event_date) for web events, and the Firebase BigQuery export for app events. If the GA4 web
stream and Firebase app stream are in the same GA4 property and exported to the same BigQuery
project, the queries below can be written against a single dataset. If they are separate, the
app-events query must reference the Firebase export dataset. This is flagged for confirmation
before the queries are deployed.

The queries below are plans. They are not deployed. Deploying to production BigQuery is a
gated action that requires the human gate to clear.

Table name placeholders:
- `{project}.{dataset}.events_*` for GA4 web export.
- `{project}.{firebase_dataset}.events_*` for Firebase app export (may be the same dataset
  if streams are linked).
- `{flight_start}` = 20260701, `{flight_end}` = 20260714.

### 10.1 Primary metric: daily signup funnel (web)

Counts the web conversion funnel by day across the flight. Feeds the primary success metric
(gate completions).

```sql
-- Daily web funnel: page_view -> gate_view -> submit -> confirm
-- Campaign: 2026-07-skill-paths-soft-launch
-- Flight: 2026-07-01 to 2026-07-14
-- Source: GA4 BigQuery export
-- Status: PLAN ONLY. Not deployed. Human gate required before production run.

SELECT
  event_date,
  COUNTIF(event_name = 'page_view')     AS page_views,
  COUNTIF(event_name = 'view_item'
    AND EXISTS (
      SELECT 1
      FROM UNNEST(event_params) AS p
      WHERE p.key = 'item_id'
        AND p.value.string_value = 'early_access_gate'
    ))                                   AS gate_views,
  COUNTIF(event_name = 'generate_lead') AS submits,
  COUNTIF(event_name = 'sign_up')       AS confirms
FROM
  `{project}.{dataset}.events_*`
WHERE
  _TABLE_SUFFIX BETWEEN '{flight_start}' AND '{flight_end}'
  AND (
    SELECT value.string_value
    FROM UNNEST(event_params) AS p
    WHERE p.key = 'campaign_id'
  ) = '2026-07-skill-paths-soft-launch'
GROUP BY
  event_date
ORDER BY
  event_date;
```

### 10.2 Primary metric: daily app installs (app)

Counts app installs attributed to the campaign across the flight. Feeds the primary success
metric (campaign-attributable app installs). Requires the Firebase BigQuery export and MMP
postback confirmation. The campaign_id parameter must be passed through the install referrer
or deep link for attribution.

```sql
-- Daily app installs: campaign-attributed
-- Campaign: 2026-07-skill-paths-soft-launch
-- Flight: 2026-07-01 to 2026-07-14
-- Source: Firebase BigQuery export (app events)
-- Status: PLAN ONLY. Not deployed. Human gate required before production run.
-- BLOCKED: MMP must be confirmed before this query can be validated against real data.

SELECT
  event_date,
  COUNT(*)  AS app_installs
FROM
  `{project}.{firebase_dataset}.events_*`
WHERE
  _TABLE_SUFFIX BETWEEN '{flight_start}' AND '{flight_end}'
  AND event_name = 'app_install'
  AND (
    SELECT value.string_value
    FROM UNNEST(event_params) AS p
    WHERE p.key = 'campaign_id'
  ) = '2026-07-skill-paths-soft-launch'
GROUP BY
  event_date
ORDER BY
  event_date;
```

### 10.3 Secondary metric: activation funnel (app, post-install)

Measures the activation rate: share of installs that reach first_open and maharat_activation.
Feeds the activation secondary metric.

```sql
-- Activation funnel: install -> first_open -> activation
-- Campaign: 2026-07-skill-paths-soft-launch
-- Flight: 2026-07-01 to 2026-07-14 (and a short tail window post-flight for activation lag)
-- Source: Firebase BigQuery export
-- Status: PLAN ONLY. Not deployed. Human gate required before production run.
-- BLOCKED: MMP confirmation and SDK event name confirmation required.

SELECT
  event_date,
  COUNTIF(event_name = 'app_install')                       AS installs,
  COUNTIF(event_name = 'first_open')                        AS first_opens,
  COUNTIF(event_name = 'tutorial_complete')                 AS activations,
  SAFE_DIVIDE(
    COUNTIF(event_name = 'first_open'),
    COUNTIF(event_name = 'app_install')
  )                                                         AS first_open_rate,
  SAFE_DIVIDE(
    COUNTIF(event_name = 'tutorial_complete'),
    COUNTIF(event_name = 'app_install')
  )                                                         AS activation_rate
FROM
  `{project}.{firebase_dataset}.events_*`
WHERE
  _TABLE_SUFFIX BETWEEN '{flight_start}' AND '{flight_end}'
  AND (
    SELECT value.string_value
    FROM UNNEST(event_params) AS p
    WHERE p.key = 'campaign_id'
  ) = '2026-07-skill-paths-soft-launch'
GROUP BY
  event_date
ORDER BY
  event_date;
```

Note: tutorial_complete is the GA4 canonical name used here for maharat_activation.
If the SDK emits a different event name, substitute it in the WHERE clause. This is
to-confirm (open item, section 3.3).

### 10.4 Combined summary view: primary metric total

A single summary row for analytics-reporter to read against the success metric target.

```sql
-- Summary: total signups + total installs across full flight
-- Campaign: 2026-07-skill-paths-soft-launch
-- Flight: 2026-07-01 to 2026-07-14
-- Status: PLAN ONLY. Not deployed. Human gate required before production run.

WITH web_confirms AS (
  SELECT COUNT(*) AS total_confirms
  FROM `{project}.{dataset}.events_*`
  WHERE
    _TABLE_SUFFIX BETWEEN '{flight_start}' AND '{flight_end}'
    AND event_name = 'sign_up'
    AND (
      SELECT value.string_value
      FROM UNNEST(event_params) AS p
      WHERE p.key = 'campaign_id'
    ) = '2026-07-skill-paths-soft-launch'
),
app_installs AS (
  SELECT COUNT(*) AS total_installs
  FROM `{project}.{firebase_dataset}.events_*`
  WHERE
    _TABLE_SUFFIX BETWEEN '{flight_start}' AND '{flight_end}'
    AND event_name = 'app_install'
    AND (
      SELECT value.string_value
      FROM UNNEST(event_params) AS p
      WHERE p.key = 'campaign_id'
    ) = '2026-07-skill-paths-soft-launch'
)
SELECT
  w.total_confirms                             AS early_access_signups,
  a.total_installs                             AS campaign_app_installs,
  w.total_confirms + a.total_installs          AS primary_metric_total,
  NULL                                         AS target  -- populate once Ahmed confirms
FROM web_confirms w, app_installs a;
```

### 10.5 Secondary metric: cost per signup (placeholder)

This query cannot be completed until the currency is confirmed (open item) and the spend
data is available in BigQuery (either via a spend export from Meta or Google, or manually
entered). The shape is provided so analytics-reporter knows what feeds it.

```sql
-- Cost per signup: placeholder
-- BLOCKED until currency confirmed and spend data loaded into BigQuery.
-- Shape only. Not a deployable query in its current form.

SELECT
  total_spend_in_confirmed_currency    / NULLIF(early_access_signups, 0) AS cost_per_signup,
  total_spend_in_confirmed_currency    / NULLIF(campaign_app_installs, 0) AS cost_per_install
FROM
  -- join the summary view above with a spend_actuals table once currency and spend are confirmed
  spend_actuals  -- placeholder table, to-confirm
  CROSS JOIN summary_view;
```

---

## 11. Handoff routing

- event_plan body above feeds conversion-engineer for the conversion-package (stream 6).
- warehouse queries (section 10) feed analytics-reporter for monitoring (stream 8).
- this full package routes to compliance-privacy-reviewer before go-live. The reviewer must
  confirm: (a) no personal data in any parameter, (b) CAPI PII-field policy (section 5),
  (c) gate-platform data residency once the platform is named.
- production write (deploying tags, wiring CAPI, deploying BigQuery queries to production)
  is a gated action. It does not happen until the human gate clears, per action.

---

## 12. Pre-handoff checklist

- [x] All four web funnel events defined with fire conditions (page_view, gate_view, submit, confirm).
- [x] All three app activation events defined (app_install, app_open, first_lesson/first_streak_day).
- [x] All events mapped to both Meta Pixel/CAPI and GA4 with destination event names.
- [x] Parameters list is strictly non-identifying. No email, phone, name, user ID, or hashed
      personal value appears in any parameter definition.
- [x] Dedup approach defined: shared event_id on submit and confirm, not traceable to a person.
- [x] Mobile attribution (Apple Search Ads, Google Play, MMP selection) flagged to-confirm.
- [x] Test plan covers all events in order, in a test session, before go-live.
- [x] BigQuery queries tied to the brief's success_metric (signups plus installs, activation rate).
- [x] All open items surfaced (platform, MMP, currency, target, residency).
- [x] Production write is gated. This document is the plan only.
