# Lifecycle package: Skill Paths first-time soft launch

Stream 7 lifecycle messaging. Owned by lifecycle-architect. This document is a design and
flow artifact. Nothing here sends, publishes, or spends. The send is a gated action and
requires explicit approval from Ahmed, per send and per campaign.

No em dashes. Western numerals. Arabic-first spirit. Every open item is listed, none buried.

---

## Envelope

- campaign_id: 2026-07-skill-paths-soft-launch
- produced_by: lifecycle-architect
- stream: 7 lifecycle messaging
- status: gated-pending (design complete, send blocked on platform open item and human-gate approval)
- qa:
  - skill_eval: passed (flow structure, suppression, platform open item surfaced, no invented
    specifics, brand mechanical rules, gate stack)
  - arabic_qa: blocked (copy-package from copywriter-ar not yet produced; every referenced
    copy variant id below must carry arabic-copy-qa: pass and brand-qa: pass before the
    lifecycle-package advances to approved. On delivery, each variant is checked against those
    gate results and the package status updates accordingly.)
  - english_qa: blocked (same condition for any EN variants from copywriter-en)
  - brand_qa: blocked (pending copy-package delivery and brand-qa-reviewer sign-off on each
    referenced variant)
  - compliance: to be run by compliance-privacy-reviewer at send time, covering the send list,
    consent records, and Saudi PDPL data-residency status of the sending platform
- open_items:
  - send-platform-unconfirmed: the email and WhatsApp sending platform is not named. Design
    is complete. Actual send wiring is blocked until the platform is confirmed and the
    Saudi PDPL data-residency decision is resolved. This is a hard stop before any send.
  - app-push-platform-unconfirmed: the app push platform is also unconfirmed. Push flow
    design is complete. Push wiring and send are blocked by the same condition.
  - copy-package-pending: copy-package.ar.md and copy-package.en.md have not been produced
    by copywriter-ar and copywriter-en. Every copy_ref in this package is a reserved variant
    id. On delivery, each must show arabic-copy-qa: pass and brand-qa: pass before this
    package advances from gated-pending to approved.
  - audience-size-to-resolve-at-send: the planning estimate is about 18,000 non-paying email
    contacts (from about 23,000 total in the company brief). The exact live figure resolves
    at send time from the owned-audience data source.
  - app-audience-size-open: the app user count is an open item from the brief (brief sec 3).
    Resolve at send time before sizing the push sequence.
  - recency-thresholds-to-confirm: the exact cut for "recently engaged" vs "dormant" depends
    on live engagement data (last-open and last-click timestamps). Thresholds below are
    design-time proposals; confirm against live data before send.
  - existing-early-access-members-source: the suppression list of any existing Skill Paths
    early-access members must be confirmed and sourced before send. If the source is empty,
    that is also a confirmation.
  - success-metric-target-unset: the numeric primary target (early-access signups plus app
    installs) and acceptable cost per signup are not confirmed. Strategy-lead flagged this
    as a stop for Ahmed. This does not block flow design but must be resolved before the
    analytics-reporter (stream 8) can run.
  - seat-cap-unconfirmed: whether a real early-access seat cap exists. Governs whether
    "limited seats" framing is truthful in the referenced copy. Copywriter-ar must not use
    that framing unless Ahmed confirms a real cap.
  - launch-announcement-authorization: the soft-launch framing is authorized by Ahmed in
    session 2026-06-05. The human gate must surface this authorization explicitly before
    any send.
  - saudi-pdpl-data-residency: pending. Blocks platform wiring.
- brief_refs:
  - objective and framing: brief sec 2
  - audience and segments: brief sec 3, strategy-artifact segment 1
  - offer in market (early access, no price): brief sec 4
  - send window (2026-07-01 to 2026-07-14): brief sec 6
  - suppression rules: brief sec 3, strategy-artifact open items
  - channel assignment (lifecycle email, entry point B; app push, existing app users): brief
    sec 5, strategy-artifact channel plan

---

## Pattern selection

Audience: owned non-payers. Objective: early-access signups (cohort and priming, not revenue).

This is a hybrid pattern. The primary segment is owned, registered, never purchased, which maps
to NON-PAYER in the selector. The campaign's objective is not a paid subscription purchase but
an early-access signup, which is a free gate completion. The arc therefore draws on the
NON-PAYER pattern structure (entry, value, offer, engagement branch, last call) but the
"offer" step is the early-access invitation, not a price point. No price is in market.

The app push sequence runs as a coordinated, lighter parallel arc for existing app users. Push
principles from `skills/07-lifecycle-messaging/templates/push-notification-principles.md` apply:
one goal per push, micro-storytelling, thumb-stop first line, mindset timing, no urgency theater
without a real deadline from the brief. The 14-day window is confirmed in the brief; the push
arc is compressed inside it.

---

## Segmentation logic

### Entry trigger: email flow

A contact enters the email flow on 2026-07-01 (campaign launch date, from brief sec 6) if all
of the following are true:

- Is on Maharat user lists 2 or 3 (non-paying account or non-paying newsletter member), per
  `skills/07-lifecycle-messaging/segmentation-logic/templates/maharat-user-lists.md`.
- Has not purchased any plan (list 5 exclusion is automatic).
- Has not failed a payment awaiting recovery (list 1 contacts are in their own recovery flow;
  they do not enter this flow concurrently).
- Is not unsubscribed and not hard-bounced.
- Is not a confirmed existing Skill Paths early-access member (suppression source to confirm,
  open item above).

### Recency sub-segments: email

| Sub-segment | Definition | Planning size | Source |
|---|---|---|---|
| Recently engaged | Opened or clicked any Maharat email within the last 90 days before 2026-07-01 | Resolve at send | Live engagement data, timestamps on user lists 2 and 3 |
| Dormant | No open or click in the 90 days before 2026-07-01 but within 365 days | Resolve at send | Same source |
| Deep dormant | No open or click in more than 365 days | Resolve at send | Same source; these contacts are candidates for the sunset flow before the campaign flow, not the main flow |

Design-time note: 90 days is the proposed recency threshold, carried from the strategy-artifact.
Confirm against the live distribution of last-open timestamps before send. If the data shows a
different natural break point, use the data. Do not invent a threshold.

Total email audience: planning estimate about 18,000 non-paying contacts. Exact figure resolves
at send time from live owned-audience data.

### Entry trigger: app push

A contact enters the push sequence on 2026-07-01 if all of the following are true:

- Has the Maharat app installed.
- Has not opted out of push notifications.
- Is not a confirmed existing Skill Paths early-access member (same suppression source).
- Is not already in the email flow on the same day (to avoid same-day double-touch on day 1;
  see coordination note in the flow section).

App audience size: OPEN ITEM. Resolve at send.

### Suppression set (both email and push, not optional)

| Exclusion | Reason |
|---|---|
| Active subscribers, list 5 (about 5,000 contacts) | Already paying; acquisition ask is not relevant |
| Failed-payment contacts, list 1 | In their own recovery flow; concurrent send conflicts |
| Unsubscribed contacts | Consent withdrawn; send is unlawful |
| Hard-bounced addresses | Non-deliverable; sending damages sender reputation |
| Existing Skill Paths early-access members | Already in the cohort; acquisition ask is redundant and potentially confusing |
| Push opt-outs | Consent not granted for push |

Source: Maharat CRM and email platform. Confirm the suppression pull is automated and that the
existing-early-access-members list is available at the time of the send. If the suppression
pull is manual, it must be verified within 24 hours before send, not at design time.

### Engagement branches

| After | Condition | Next step |
|---|---|---|
| Email msg-1 | Opened or clicked | Proceed to msg-2 on schedule |
| Email msg-1 | Not opened within 2 days of send | msg-1 subject-line retry (msg-1-retry), alternate subject only, same body, same copy variant; then wait 2 more days |
| Email msg-1-retry | Opened or clicked | Proceed to msg-2 on schedule |
| Email msg-1-retry | Still not opened | Dormant branch: hold, do not send msg-2 to a non-opener; reassess at msg-3 window; recently-engaged sub-segment may still receive msg-3 (last call) after the window |
| Email msg-2 | Opened or clicked | Proceed to msg-3 on schedule |
| Email msg-2 | Not opened within 2 days | msg-3 (last call) still sends; do not send a msg-2 retry in this compressed window |
| Email msg-3 | Opened or clicked | No further email needed unless a 4th message (last call push) is approved |
| Email msg-3 | Not opened | No further email; contact enters normal cadence after the flight closes |
| Push push-1 | Tapped | No further push needed until push-2 window; user is active |
| Push push-1 | Not tapped within 24 hours | push-2 still sends on its scheduled day regardless |
| Push push-2 | Tapped | No further push in this flight |
| Push push-2 | Not tapped within 24 hours | push-3 (last call) sends on its scheduled day |

Note on the subject-line retry: the retry carries an alternate subject and preheader from the
copy-package (variant id to include a "-b" suffix, see copy_ref notes below). Body and CTA are
identical. This is a light retry, not an escalation or a louder pitch.

### Sunset rule (applies before flow entry for deep-dormant contacts)

Contacts who have not opened or clicked in more than 365 days, or who have gone through 3 or
more prior Maharat flow attempts without re-engaging, should receive a 1-email sunset touch
(a warm, non-pressuring farewell and preference-update prompt) before 2026-07-01, not as part
of this campaign flow. If they re-engage in response, they become eligible for the main flow.
If they do not, they are suppressed from this campaign. This protects sender reputation,
deliverability, and PDPL consent hygiene.

The exact 365-day threshold is a design proposal; confirm against the live engagement
distribution and the brief. Do not invent it.

### Timing (email)

All times are approximate and in Saudi Arabia local time (AST, UTC+3). Morning local sends
are the default per sequence standards, roughly 8 AM to 10 AM, unless a different window is
confirmed by the brief or by live send-time data for this list.

| Message | Send day (relative to 2026-07-01) | Absolute date | Notes |
|---|---|---|---|
| msg-1 | Day 1 | 2026-07-01 | Campaign open; recently-engaged sub-segment first |
| msg-1-retry | Day 3 | 2026-07-03 | Only to non-openers of msg-1; alternate subject |
| msg-2 | Day 5 | 2026-07-05 | To openers and clickers of msg-1 or msg-1-retry |
| msg-3 | Day 12 | 2026-07-12 | Last call; full eligible audience (opened any prior or not); inside the 2026-07-14 window |

Dormant sub-segment: receives msg-1, the subject-line retry if non-opener, and msg-3 (last
call). It does not receive msg-2 if it never opened msg-1 or msg-1-retry. The dormant path
is intentionally lighter to protect list health and sender reputation.

### Timing (app push)

| Message | Send day | Absolute date | Time (AST) | Notes |
|---|---|---|---|---|
| push-1 | Day 1 | 2026-07-01 | Evening, ~7 PM to 8 PM | Mindset: after-work or wind-down window. Not the same hour as email msg-1 to avoid same-moment double-touch |
| push-2 | Day 6 | 2026-07-06 | Morning, ~9 AM | Habit-start frame; mid-flight reinforcement |
| push-3 | Day 13 | 2026-07-13 | Evening, ~7 PM | Last call push; one day before window closes |

Push timing follows mindset timing principles from the push-notification-principles reference.
These are proposals. Confirm against any live send-time performance data for this app audience
if available at build time.

---

## Email flow

### Overview

A 3-message core flow (with a subject-line retry for non-openers) compressed into the
2026-07-01 to 2026-07-14 window. Every message references a QA-passed copy variant by
reserved id. No copy is written here. Each copy_ref is a placeholder that resolves to the
actual copy-package variant id when copywriter-ar and copywriter-en deliver and their work
passes the gate stack (skill eval, arabic-copy-qa, brand-qa-reviewer).

The arc:

1. Invite: early-access invitation, value of building a skill one step a day. One CTA: join
   the early access.
2. Value: why a small step a day works. Reinforce the format benefit and the streak motif.
   Not a pitch. One CTA: still open, join now.
3. Last call: the window closes soon. Reminder and light urgency grounded in the real
   2026-07-14 end date (no invented deadline). One CTA: join before the window closes.

### Message specifications

---

#### msg-1: early-access invite

- id: msg-1-invite
- trigger: 2026-07-01, campaign launch; contacts meet entry trigger criteria
- segment: all eligible non-payers (recently-engaged and dormant sub-segments, after deep-dormant
  sunset step is run)
- channel: email
- language: Arabic primary (AR variant required); English variant optional if an EN-language
  sub-segment exists in the list (confirm at send)
- copy_ref: copy-package.ar / SP-EA-EMAIL-AR-01-INVITE
- subject_ref: copy-package.ar / SP-EA-EMAIL-AR-01-SUBJECT-A (primary subject)
- preheader_ref: copy-package.ar / SP-EA-EMAIL-AR-01-PREHEADER-A
- copy_ref_en (if EN sub-segment confirmed): copy-package.en / SP-EA-EMAIL-EN-01-INVITE
- subject_ref_en: copy-package.en / SP-EA-EMAIL-EN-01-SUBJECT-A
- send_time: 2026-07-01, 8 AM to 10 AM AST
- cta: one CTA to the early-access signup gate (URL placeholder; resolve when platform is
  confirmed; do not put user identity or preference data in URL parameters)
- angle notes for copywriter-ar (not final copy): early-access invitation, warm insider tone,
  empowering. The hero is the learner who finally has a format that fits their day. Format and
  benefit only; no Skill Path titles, no content lineup, no price, no accreditation. Reference:
  strategy-artifact segment 1 angle, "you already know us, here is the easiest way yet to start."
- brand rules: Arabic-first, MSA Gulf-familiar, Thmanyah tone, no em dashes, no tatweel,
  Western numerals, empowering never deficit-framed, no accreditation claim, no invented titles
- qa_required: arabic-copy-qa: pass, brand-qa: pass (before this message can advance to send)

---

#### msg-1-retry: subject-line retry for non-openers

- id: msg-1-retry
- trigger: msg-1 not opened within 48 hours of send (by ~2026-07-03, 8 AM to 10 AM AST)
- segment: non-openers of msg-1, same eligibility rules
- channel: email
- language: matches the language of the original msg-1 for each contact
- copy_ref (body): same as msg-1 (SP-EA-EMAIL-AR-01-INVITE); body is unchanged
- subject_ref: copy-package.ar / SP-EA-EMAIL-AR-01-SUBJECT-B (alternate subject line)
- preheader_ref: copy-package.ar / SP-EA-EMAIL-AR-01-PREHEADER-B (alternate preheader)
- subject_ref_en (if applicable): copy-package.en / SP-EA-EMAIL-EN-01-SUBJECT-B
- send_time: 2026-07-03, 8 AM to 10 AM AST
- note: alternate subject and preheader only. Body and CTA are identical to msg-1. This is a
  light retry, not an escalation or a more aggressive pitch. The subject-line variant should
  approach the same invitation from a different angle without adding pressure or deficit framing.
- qa_required: arabic-copy-qa: pass on the alternate subject and preheader, brand-qa: pass

---

#### msg-2: value reinforcement

- id: msg-2-value
- trigger: 2026-07-05 (day 5), contact opened or clicked msg-1 or msg-1-retry
- segment: openers and clickers of msg-1 or msg-1-retry (recently-engaged sub-segment primarily;
  dormant sub-segment only if they opened or clicked the retry)
- channel: email
- language: Arabic primary; English if EN sub-segment confirmed
- copy_ref: copy-package.ar / SP-EA-EMAIL-AR-02-VALUE
- subject_ref: copy-package.ar / SP-EA-EMAIL-AR-02-SUBJECT-A
- preheader_ref: copy-package.ar / SP-EA-EMAIL-AR-02-PREHEADER-A
- copy_ref_en (if applicable): copy-package.en / SP-EA-EMAIL-EN-02-VALUE
- send_time: 2026-07-05, 8 AM to 10 AM AST
- cta: one CTA to the early-access signup gate (same URL placeholder as msg-1)
- angle notes for copywriter-ar: the value message. Why a small step a day works. The streak
  and habit-forming benefit of the format, spoken concretely and without inventing titles or
  content details. Reinforce the angle from msg-1. The reader opened once; reward that with
  something genuinely useful, not a repeat pitch. Empowering. The hero is still the learner.
- brand rules: same as msg-1
- qa_required: arabic-copy-qa: pass, brand-qa: pass

---

#### msg-3: last call

- id: msg-3-lastcall
- trigger: 2026-07-12 (day 12); eligible audience is all contacts who received msg-1 or
  msg-1-retry and have not yet signed up for early access, regardless of open status. The
  window closes 2026-07-14 (from brief). This is a real deadline: no invented urgency.
- segment: full eligible non-payer list, minus those who already completed the early-access
  signup (suppress converted contacts before send)
- channel: email
- language: Arabic primary; English if EN sub-segment confirmed
- copy_ref: copy-package.ar / SP-EA-EMAIL-AR-03-LASTCALL
- subject_ref: copy-package.ar / SP-EA-EMAIL-AR-03-SUBJECT-A
- preheader_ref: copy-package.ar / SP-EA-EMAIL-AR-03-PREHEADER-A
- copy_ref_en (if applicable): copy-package.en / SP-EA-EMAIL-EN-03-LASTCALL
- send_time: 2026-07-12, 8 AM to 10 AM AST (2 days before the 2026-07-14 window close)
- cta: one CTA to the early-access signup gate
- angle notes for copywriter-ar: last call, light urgency grounded only in the real 2026-07-14
  window end. Do not invent a seat count, a countdown to an unconfirmed date, or a price.
  The "limited seats" frame may only be used if Ahmed confirms a real seat cap (see open items).
  Until confirmed, omit it entirely. The tone is warm, not pressuring. One clear reason to act.
- brand rules: same as msg-1; special check: no invented seat cap, no countdown to an
  unconfirmed date, no price
- qa_required: arabic-copy-qa: pass, brand-qa: pass; special brand-qa check for the last-call
  message: confirm no invented seat limit is present, no firm date beyond 2026-07-14

---

### Converted-contact suppression before msg-3

Before msg-3 sends on 2026-07-12, pull a fresh conversion list of contacts who completed
the early-access signup during the flight (2026-07-01 to 2026-07-11). Suppress them from
msg-3. This requires a live data pull from the signup gate platform at send time. Coordinate
with data-tracking-engineer to confirm the `gate_submit_confirm` event is queryable before
this pull date.

---

## App push sequence

Three pushes coordinated with the email flow. Push and email do not fire on the same day for
the same contact. Each push carries one goal and one tap target. No urgency theater without
a real deadline.

### Push message specifications

---

#### push-1: early-access reveal

- id: push-1-reveal
- trigger: 2026-07-01, campaign launch day, evening (~7 PM to 8 PM AST)
- segment: all eligible app users (push-opted-in, not existing early-access members, not
  already in email flow at the same hour; the email sends in the morning, push sends in
  the evening, same day is acceptable under this time separation)
- channel: app push notification
- language: Arabic primary; the app platform must support Arabic RTL push rendering; confirm
  at build
- copy_ref: copy-package.ar / SP-EA-PUSH-AR-01-REVEAL
- cta_tap_target: deep link to Skill Paths early-access signup or the early-access gate;
  URL placeholder, resolves when platform is confirmed
- angle notes for copywriter-ar: reveal and invite. One hook. The product is here, it fits
  your day, you are in early. Micro-storytelling: a one-line story with a hook, not a system
  message. Thumb-stop standard: the first 3 words must stop the scroll. No deficit framing.
  No invented titles. Soft-launch, early-access only.
- brand rules: no em dashes, no tatweel, Western numerals, empowering
- qa_required: arabic-copy-qa: pass, brand-qa: pass

---

#### push-2: habit reinforcement

- id: push-2-habit
- trigger: 2026-07-06 (day 6), 9 AM AST
- segment: app users who received push-1 and have not yet tapped through to the signup gate
  (suppress converted app users; requires conversion event queryability, coordinate with
  data-tracking-engineer)
- channel: app push notification
- language: Arabic primary
- copy_ref: copy-package.ar / SP-EA-PUSH-AR-02-HABIT
- cta_tap_target: same deep link as push-1
- angle notes for copywriter-ar: the small-step and streak motif. A concrete, positive reason
  to build a habit now. One line, one goal. No repeat of push-1's hook verbatim; approach
  the benefit from a different angle. Morning mindset: starting the day.
- brand rules: same as push-1
- qa_required: arabic-copy-qa: pass, brand-qa: pass

---

#### push-3: last call

- id: push-3-lastcall
- trigger: 2026-07-13 (day 13), 7 PM to 8 PM AST
- segment: app users who received push-1 and push-2 and have not yet signed up; suppress
  converted contacts (same fresh pull as the email msg-3 suppression, coordinate with
  data-tracking-engineer)
- channel: app push notification
- language: Arabic primary
- copy_ref: copy-package.ar / SP-EA-PUSH-AR-03-LASTCALL
- cta_tap_target: same deep link
- angle notes for copywriter-ar: last call, one day before the window closes (2026-07-14).
  Light, genuine urgency. The real deadline is the brief's end date. No invented seat cap
  unless Ahmed confirms one. One line, warm tone, one goal.
- brand rules: same as push-1; special check: no invented deadline or seat count
- qa_required: arabic-copy-qa: pass, brand-qa: pass

---

## Coordination with data-tracking-engineer

The following send and engagement events must be co-designed and confirmed with
data-tracking-engineer before the flow can wire to any platform. This agent owns the flow
logic; data-tracking-engineer owns the event definitions, the warehouse plumbing, and the
tracking plan.

| Event id | What it marks | Where it fires | Needed by this flow for |
|---|---|---|---|
| lifecycle_email_send | Email dispatched to a contact | Email platform | Delivery confirmation, volume audit |
| lifecycle_email_open | Contact opened the email | Email platform | Engagement branch trigger (msg-1 opener vs non-opener) |
| lifecycle_email_click | Contact clicked any link in the email | Email platform | Engagement branch trigger |
| lifecycle_ea_signup_complete | Contact completed the early-access gate | Signup gate platform | Suppression of converted contacts before msg-3 and push-3; feeds stream 8 primary metric |
| lifecycle_push_send | Push dispatched to a device | App push platform | Delivery audit |
| lifecycle_push_tap | Contact tapped the push | App push platform | Engagement signal; suppression of converted app users before push-2 and push-3 |
| lifecycle_push_ea_signup_complete | App-push-attributed gate completion | App push platform or gate | Disambiguation of email-attributed vs push-attributed conversions for analytics-reporter |

Note on event design: no personal or sensitive data is to be included in any event parameter
or tracking URL. Event ids are flow-level, not contact-level identifiers. Contact-level
resolution happens inside the email or push platform's own send log, not in URL parameters.

The `lifecycle_ea_signup_complete` event must be queryable from a data warehouse view by
2026-07-11 at the latest, to power the converted-contact suppression pull before msg-3 and
push-3 send.

Carry forward to data-tracking-engineer: this flow needs the above seven events wired in the
tracking plan before platform wiring begins. The tracking plan (data-tracking-engineer's
artifact) must show these events mapped and their source confirmed before the lifecycle-package
can advance beyond gated-pending.

---

## Audience size

- email audience (planning estimate): about 18,000 non-paying contacts. Exact figure resolves
  from live owned-audience data at send time. Record the exact suppressed-out and eligible
  counts in the send log before triggering.
- app push audience: OPEN ITEM (brief sec 3). Resolve before push-1 sends. If the app audience
  size is not available before 2026-07-01, the push sequence must be held until it is resolved.
  Do not send push without a confirmed audience count.
- recently-engaged sub-segment vs dormant sub-segment split: resolve at send from live
  engagement data. The split governs which contacts receive msg-2 (openers only).

---

## Suppression (consolidated)

Who is excluded from this campaign's sends, and why:

| Group | Excluded from | Reason |
|---|---|---|
| Active subscribers, list 5, about 5,000 contacts | All email and push sends | Already paying; acquisition ask is not relevant; sending wastes budget and risks irritating a paying customer |
| Failed-payment contacts, list 1 | All sends | In their own urgency-window recovery flow; concurrent send creates conflicting messaging |
| Unsubscribed contacts | All email sends | Consent withdrawn; send is unlawful |
| Hard-bounced addresses | All email sends | Non-deliverable; repeated sends to hard bounces damage sender reputation and deliverability |
| Push opt-outs | All push sends | Consent not granted |
| Existing Skill Paths early-access members | All email and push sends | Already in the cohort; redundant acquisition ask (suppression source to confirm before send) |
| Contacts who completed the signup during the flight | msg-3 and push-3 only | Converted; last-call message is irrelevant and adds noise |
| Deep-dormant contacts (no open or click in more than 365 days) not yet through the sunset flow | Main email flow | Protect sender reputation and PDPL consent hygiene; sunset flow runs first |

Suppression source: Maharat CRM and email platform automated lists as defined in
`skills/07-lifecycle-messaging/segmentation-logic/templates/maharat-user-lists.md`. The
pull must be confirmed automated and verified within 24 hours of each send date.

---

## Send on approval

Sends a 3-message early-access email flow plus a subject-line retry for non-openers, to the
eligible non-paying owned audience (planning estimate about 18,000 contacts, exact figure at
send), across 2026-07-01 to 2026-07-12, plus a 3-push app-push sequence on 2026-07-01,
2026-07-06, and 2026-07-13, to the eligible app-push-opted-in app user audience (size to
confirm), with suppression applied as specified above. Nothing sends without explicit approval
from Ahmed at the human gate, and the send is additionally blocked on the platform open item
and the Saudi PDPL data-residency decision.

---

## Platform open item (hard stop)

The email, WhatsApp, and app push platforms are not confirmed (brief sec 5, sec 8, strategy-artifact
open items). Flow design is complete and does not require a platform name. Actual send wiring
requires:

1. A named platform vendor (email and WhatsApp send platform).
2. A named app push platform vendor.
3. The Saudi PDPL data-residency decision for each platform.
4. The API credential (EMAIL_WHATSAPP_API_KEY and the equivalent for push) on the allowlist
   and in the MCP server configuration.

Until all four are confirmed, this package is design-only and not-sendable. The human gate
must surface the platform open item explicitly. No send action is taken without both the
platform being confirmed and Ahmed's approval for this specific send.

---

## Quality gate status and required copy variants

The following copy variant ids are reserved for this flow. They are not yet produced.
Copywriter-ar and copywriter-en must produce the copy-package, which then passes the full
gate stack (skill eval, arabic-copy-qa, brand-qa-reviewer). This lifecycle-package advances
to approved only after every referenced variant shows arabic-copy-qa: pass and brand-qa: pass
in the copy-package envelope.

| Variant id | Type | Language | Message | Gate required |
|---|---|---|---|---|
| SP-EA-EMAIL-AR-01-INVITE | Email body | AR | msg-1 | arabic-copy-qa, brand-qa |
| SP-EA-EMAIL-AR-01-SUBJECT-A | Subject line (primary) | AR | msg-1 | arabic-copy-qa, brand-qa |
| SP-EA-EMAIL-AR-01-PREHEADER-A | Preheader (primary) | AR | msg-1 | arabic-copy-qa, brand-qa |
| SP-EA-EMAIL-AR-01-SUBJECT-B | Subject line (retry alternate) | AR | msg-1-retry | arabic-copy-qa, brand-qa |
| SP-EA-EMAIL-AR-01-PREHEADER-B | Preheader (retry alternate) | AR | msg-1-retry | arabic-copy-qa, brand-qa |
| SP-EA-EMAIL-AR-02-VALUE | Email body | AR | msg-2 | arabic-copy-qa, brand-qa |
| SP-EA-EMAIL-AR-02-SUBJECT-A | Subject line | AR | msg-2 | arabic-copy-qa, brand-qa |
| SP-EA-EMAIL-AR-02-PREHEADER-A | Preheader | AR | msg-2 | arabic-copy-qa, brand-qa |
| SP-EA-EMAIL-AR-03-LASTCALL | Email body | AR | msg-3 | arabic-copy-qa, brand-qa; special: no invented seat cap, no countdown to unconfirmed date |
| SP-EA-EMAIL-AR-03-SUBJECT-A | Subject line | AR | msg-3 | arabic-copy-qa, brand-qa |
| SP-EA-EMAIL-AR-03-PREHEADER-A | Preheader | AR | msg-3 | arabic-copy-qa, brand-qa |
| SP-EA-EMAIL-EN-01-INVITE | Email body | EN | msg-1 | english-copy-qa, brand-qa (only if EN sub-segment confirmed) |
| SP-EA-EMAIL-EN-01-SUBJECT-A | Subject line (primary) | EN | msg-1 | english-copy-qa, brand-qa |
| SP-EA-EMAIL-EN-01-SUBJECT-B | Subject line (retry alternate) | EN | msg-1-retry | english-copy-qa, brand-qa |
| SP-EA-EMAIL-EN-02-VALUE | Email body | EN | msg-2 | english-copy-qa, brand-qa |
| SP-EA-EMAIL-EN-03-LASTCALL | Email body | EN | msg-3 | english-copy-qa, brand-qa |
| SP-EA-PUSH-AR-01-REVEAL | Push notification | AR | push-1 | arabic-copy-qa, brand-qa |
| SP-EA-PUSH-AR-02-HABIT | Push notification | AR | push-2 | arabic-copy-qa, brand-qa |
| SP-EA-PUSH-AR-03-LASTCALL | Push notification | AR | push-3 | arabic-copy-qa, brand-qa; special: no invented seat cap or deadline |

Note to copywriter-ar and copywriter-en: the variant ids above are reserved ids for this
package. Produce the copy-package with these ids populated. Each variant must carry the brief
angle (format and benefit, empowering, no Skill Path titles, no price, no accreditation, no
firm launch date, soft-launch early-access only). Push variants are short-form; apply the
thumb-stop standard. Subject lines are 20 to 60 characters, front-loaded; mobile band is
roughly 30 to 40 characters.

---

## Pre-handoff checklist

- [x] Skill eval (07-lifecycle-messaging): passed. Flow structure complete, sub-skills applied,
  sequence pattern selected and justified, copy is referenced not written, suppression stated,
  platform open item surfaced, send blocked, no invented specifics, brand mechanical rules met.
- [ ] arabic-copy-qa: blocked, pending copy-package delivery from copywriter-ar.
- [ ] english-copy-qa: blocked, pending copy-package delivery from copywriter-en.
- [ ] brand-qa: blocked, pending copy-package delivery and brand-qa-reviewer sign-off on each
  variant.
- [x] Envelope complete: campaign_id, produced_by, stream, status, qa block, open_items list,
  brief_refs present.
- [x] Audience size: planning estimate about 18,000 non-payers stated; exact figure flagged for
  resolution at send. App audience size flagged as open item.
- [x] Suppression set: stated with sources and reasons. Exclusion of existing early-access
  members flagged as source-to-confirm.
- [x] Send-platform open item surfaced: both email/WhatsApp and app push platforms unconfirmed.
  Live send blocked.
- [x] Saudi PDPL data-residency open item surfaced.
- [x] No invented offer, schedule, window, Skill Path title, instructor, seat count, or price.
- [x] Brand rules: no em dashes, no tatweel, Western numerals throughout. Empowering framing in
  all angle notes.
- [x] Engagement branches defined and grounded in real signals only, not guessed ones.
- [x] Converted-contact suppression before msg-3 and push-3 specified, with data dependency
  on data-tracking-engineer's event wiring.
- [x] Event co-design table for data-tracking-engineer included.
- [x] Copy variant ids reserved and the gate requirement for each stated.
- [x] Send-on-approval sentence present.
- [x] Human gate: package routes to human gate; send requires explicit per-send approval from
  Ahmed. Silence is not approval.

---

## Handoff routing

- To data-tracking-engineer: the seven events in the coordination table above must be wired
  and confirmed in the tracking plan before platform wiring begins. Flag the
  `lifecycle_ea_signup_complete` event queryability requirement by 2026-07-11.
- To copywriter-ar: produce the Arabic copy variants at the ids above. Brief angle, segment
  1 framing, push variant length constraints, all guardrails. Gate each through arabic-copy-qa
  and brand-qa-reviewer before returning ids to this package.
- To copywriter-en: if an English-language sub-segment is confirmed in the owned list, produce
  the EN variants at the EN ids above. Gate through english-copy-qa and brand-qa-reviewer.
- To human-gate: this package routes to the human gate for Ahmed's sign-off. The gate must
  surface (a) the platform open item, (b) the Saudi PDPL open item, (c) the launch-announcement
  authorization, (d) the success-metric target, and (e) the seat-cap question before
  approving any send.
- To analytics-reporter (streams 8 and 9): the success metric for this flow is
  early-access signups (gate completions) attributable to the email and push flow, plus the
  owned-flow engagement metrics (open rate, click rate, signup rate). The measurement plan
  must reference the `lifecycle_ea_signup_complete` event and the `lifecycle_push_ea_signup_complete`
  disambiguation event.

---

## Status

Design complete. Send blocked on: platform open item, Saudi PDPL data-residency decision,
copy-package delivery and gate results, and human-gate approval. Nothing sends. The swarm
pauses at the human gate.
