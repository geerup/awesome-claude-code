# Lifecycle Package: Summer of Skills, full-stack non-payer campaign

## Envelope

- campaign_id: 2026-07-summer-nonpayer
- produced_by: lifecycle-architect
- stream: 7 lifecycle messaging
- status: draft
- qa:
  - skill_eval: passed (flow structure, segmentation logic, trigger completeness, suppression
    correctness, copy variant id referencing, open-item surfacing, brand mechanical rules)
  - arabic_qa: ref. Awaiting copy-package.ar.md (status pending per 00-orchestration.md).
    All email and push copy variants EMAIL-E1..EMAIL-E5 and PUSH-P1..P5 must carry
    arabic-copy-qa pass before this package advances to qa-passed.
  - brand_qa: ref. Awaiting copy-package.ar.md and copy-package.en.md. All referenced
    variants must carry brand-qa-reviewer pass before this package advances to qa-passed.
  - compliance: ref. Awaiting compliance-verdict.md. This package names 9 open items
    with compliance implications (send platform, PDPL, suppression source, push consent,
    data residency). compliance-privacy-reviewer must run on the full package before
    any send wiring or data collection.
- open_items:
  1. copy-packages-pending: copy-package.ar.md and copy-package.en.md are status pending
     per 00-orchestration.md. The flow references variant ids EMAIL-E1..EMAIL-E5 and
     PUSH-P1..P5 by the id scheme agreed in the brief. The flow design is complete; it does
     not advance to qa-passed until those packages are produced and all referenced variants
     carry arabic-copy-qa pass and brand-qa pass.
  2. send-platform-unconfirmed: email, WhatsApp, and app-push platforms not confirmed per
     brief s.7 and strategy-artifact s.6. Flow design proceeds; live send wiring is blocked
     until the platform is named. Saudi PDPL data-residency decision is also pending and
     blocks send wiring independently.
  3. audience-size-to-resolve-at-send: about 18,000 non-paying email contacts is a planning
     estimate from the brief and company brief. Exact figure resolved from live owned data
     at send time after suppression is applied, and recorded in the final send package.
  4. app-audience-size-open-item: app user segment size not confirmed in the brief or
     strategy-artifact. Size resolves when the app-push platform is confirmed and the segment
     pull is run.
  5. recency-signal-to-confirm: the never-engaged vs lapsed-engaged recency cut requires a
     last-open or last-activity signal in the owned data. If that signal is absent at send
     time, the flow runs unsplit (all non-payers, one undifferentiated flow) and this is
     flagged in the send package before approval.
  6. suppression-source-to-confirm: brief s.4 flags "Confirm suppression list source at
     build." The suppression categories are correct in this design. Execution wiring waits on
     platform confirmation and source identification.
  7. schedule-assumption: start_date 2026-07-01 and end_date 2026-08-31 are ASSUMPTION per
     brief s.8. Email sequence cadence (5 messages, proposed over 3 to 4 weeks from entry)
     and push cadence (5 touches, light spacing) are ASSUMPTION. Confirm with Ahmed before
     wiring.
  8. promotion-assumption: no trial, discount, or bundle confirmed per brief s.5. No promo
     is stated or implied in this flow design or in the copy ids referenced. Confirm with
     Ahmed before any promo copy is authored or any promo appears in any asset.
  9. success-metric-target-unset: primary subscription conversion target number and date are
     ASSUMPTION per brief s.3 and strategy-artifact s.2. The metric definition is stable;
     only the number and dates need Ahmed.
  10. plan-assumption: which plan(s) the campaign leads with (1, 3, or 12 month) is ASSUMPTION
      per brief s.5. Copy variants must not specify a plan until this is confirmed.
  11. instructor-naming-confirm-at-gate: the seven nameable instructors (Ragheb Alama, Salam
      Dakkak, Kosai Khauli, Bassam Fattouh, Toufic Kreidieh, Cedric Haddad, Elda Choucair)
      each carry public_naming_cleared: yes with Ahmed sign-off but catalog public-status
      reads unconfirmed. Every per-instructor reference in copy is confirm-at-gate. The four
      non-nameable instructors (Rahma Riad, Sami Al Jaber, Mona Ataya, Mo Islam) are never
      named and appear only inside an unnamed "and more" breadth.
  12. verify-before-public-use: Toufic Kreidieh's Brands For Less name and the $10,000-garage
      detail; Elda Choucair's Omnicom, Forbes, Cannes, and the 900-plus and 1000-plus figures
      must not appear until verified, even if Kreidieh and Choucair are named.
  13. PDPL-and-data-residency-open-item: Saudi PDPL compliance and data residency posture for
      owned sends, push, and tracking are OPEN ITEM per brief s.10 and strategy-artifact s.6.
      compliance-privacy-reviewer runs on every data-touching asset before any wiring.
  14. approved-instructor-imagery-open-item: rights-cleared instructor photography and class
      stills are ASSUMPTION per brief s.9. Until confirmed, abstract brand-constant creative
      only in email headers and push. Generated instructor likeness is never permitted.
  15. gender-address-advisory: Arabic email copy for a breadth-led multi-field campaign
      must decide one consistent gender address stance or an intentional per-segment split
      before send, given the roster spans feminine-coded fields (makeup, styling) and
      masculine-or-plural-default fields. This decision is for copywriter-ar at copy authoring
      time, and must be confirmed with Ahmed before any Arabic copy is QA-passed for send.
- brief_refs: objective, audience, segments, suppression, audience_size, product,
  plan, price, promotion, offer_framing_notes, channels, signup_gate, gate_platform,
  start_date, end_date, send_window, instructor_roster, creative_direction

---

## 1. Sequence pattern selection

Audience: owned, registered, never purchased (non-payers, about 18,000).
Objective: first subscription from a contact who knows the brand and never paid.
Pattern selected: NON-PAYER, per the selector in
skills/07-lifecycle-messaging/templates/sequence-standards.md (row: "owned non-payer,
registered but never purchased, first purchase or subscription").
Sub-skills used: segmentation-logic (section 2 below), nonpayer-email-flow (section 3),
push-notification-principles (section 4), onboarding-sequence (section 5 coordination note).

---

## 2. Segmentation logic

### Source data

Owned email contacts who have not purchased a subscription. Planning estimate: about 18,000
non-payers (brief s.4; company brief). Paying contacts (about 5,000 per the company brief)
are suppressed before any further segmentation. Exact figures resolve from live CRM or ESP
data at send time.

### Recency cut (run split if signal is present; collapse to unsplit if absent, and flag it)

The strategy-artifact (s.3.1) authorizes and defines a recency split where the owned data
carries the signal. The owned data signal needed is: last email open, last app session, or
last platform login.

- Segment NP-A, lapsed-engaged: registered, no active subscription, last open or last activity
  within 90 days. Warmer signal. Has shown prior intent. Lead with the breadth and the free
  first lesson as a re-entry invitation. Can carry a more direct path-to-subscription message
  sooner. Size: share of about 18,000, resolved from live data at send time. Not invented.
- Segment NP-B, never-engaged: registered, no active subscription, no recorded open or activity
  since signup (or last activity beyond 90 days). Cooler signal. Needs a re-introduction to the
  breadth and the format. Subject lines lean on the skill outcome to earn the open. Lower-friction
  asks, with the free first lesson as the first step. Size: share of about 18,000, resolved from
  live data at send time. Not invented.

Collapse rule: if the recency signal (last open, last activity) is not available in the owned
data at send time, NP-A and NP-B run as a single undifferentiated flow against the full
non-payer list. This is flagged in the send package before approval, not silently absorbed.

### Engagement branches (in-flow)

After E1 enters:

| After | Condition | Next step |
|---|---|---|
| E1 | Opened E1 or play event recorded (masterclass_play_start) within 3 days | Skip E2, advance to E3 after 4 days from the open or play event |
| E1 | No open and no play within 3 days | Send E2 (re-angle, non-openers) |
| E2 | Opened E2 | Advance to E3 after 4 days from the open |
| E3 | subscription_start event fires at any point | Exit flow immediately, enter onboarding |
| E3 | No subscription within 5 days of E3 | Send E4 (breadth and experts spotlight, drive free play) |
| E4 | subscription_start event fires | Exit flow immediately |
| E4 | No subscription within 5 days of E4 | Send E5 (last call) |
| E5 | subscription_start event fires | Exit flow immediately |
| E5 | No subscription | Exit flow; contact enters sunset tracking |

Non-openers of E1 receive E2 as a re-angle, not a louder pitch. Subject line and angle differ
from E1; the body does not escalate pressure.

### Inter-message timing

Proposed cadence (ASSUMPTION, confirm with Ahmed per brief s.8):

- E1: sent at entry (contact qualifies and passes suppression check)
- E2 (non-opener path): 3 days after E1 if no open or play recorded
- E3: 4 days after first open or play (via E1 direct or E2 open)
- E4: 5 days after E3, if no subscription_start
- E5: 5 days after E4, if no subscription_start

Total spread from entry to E5: approximately 17 days on the main path. Within the proposed
2026-07-01 to 2026-08-31 window (ASSUMPTION, both dates to confirm with Ahmed). All inter-message
delays are inside the send window and must be confirmed once the window is confirmed.

### Suppression set (not optional)

| Category | Definition | Why |
|---|---|---|
| Already paying | Contacts with an active subscription or prior single-class purchase at the time of audience pull | Not the target segment; acquisition flow to paying contacts wastes trust and is irrelevant |
| Unsubscribed | Contacts who have actioned an unsubscribe from any Maharat email list | Legal and brand obligation; no re-entry without a fresh opt-in |
| Hard-bounced | Addresses that returned a permanent delivery failure | Technical suppression; sending to these degrades sender reputation |
| Push opt-outs | App users who declined or revoked push permission at the OS level | Respect the explicit OS-level signal; no override |
| Mid-flow converters | Contacts who trigger subscription_start at any point during the flow | Converted; exit immediately on the event, do not wait for the next scheduled message |

Suppression source: OPEN ITEM, confirm at build per brief s.4. Suppression categories are
correct in this design. Execution wiring waits on platform and source confirmation.

### Sunset rule and engagement-decay suppression (not optional)

A contact who completes the full 5-message email flow (E1 to E5) without any open, click,
or play event, or who has had no open or activity for roughly 90 days or more before flow
entry, runs a short sunset sequence (1 to 3 emails maximum, confirmed against the data and
brief) and is then suppressed from further owned sends. The exact decay window (90 to 180
days) resolves against the owned data at send time; it is not invented here. Sunsetting
protects sender reputation, preserves deliverability, and is sound consent and PDPL hygiene.

### Dedupe: email and app push overlap

A contact who is in both the email flow and the app push sequence receives both channels.
The two channels reinforce each other and do not suppress each other, but they do not fire
on the same day (see section 4, push coordination logic). If a contact subscribes
(subscription_start), exit them from both flows on that same event simultaneously.

---

## 3. Non-payer email flow (E1..E5)

### Overview

5 messages, triggered by entry and engagement, not strictly dated. Proposed flight: about
3 to 4 weeks from entry, within the campaign window 2026-07-01 to 2026-08-31 (both ASSUMPTION,
confirm with Ahmed). Each message references a copy variant from copy-package.ar.md (Arabic,
primary) and copy-package.en.md (English variant) by the id scheme EMAIL-E1..EMAIL-E5.

Copy packages are status pending per 00-orchestration.md. The flow design is complete. The
lifecycle package does not advance to qa-passed until all referenced variants carry arabic-copy-qa
pass and brand-qa pass.

Platform send wiring is blocked until the email platform is named. Design proceeds.

### Message table

| ID | Purpose | Trigger | Delay | Audience | Channel | Copy ref (AR) | Copy ref (EN) | Subject ref |
|---|---|---|---|---|---|---|---|---|
| E1 | Breadth re-intro and free first lesson | Entry: registered, no subscription, passes suppression | At entry | All non-payers (NP-A and NP-B, split if recency signal present) | Email | copy-package.ar.md variant EMAIL-E1 | copy-package.en.md variant EMAIL-E1 | copy-package.ar.md subject EMAIL-E1-SUBJECT |
| E2 | Re-angle for non-openers | No open or play within 3 days of E1 | 3 days after E1 | NP-A and NP-B non-openers | Email | copy-package.ar.md variant EMAIL-E2 | copy-package.en.md variant EMAIL-E2 | copy-package.ar.md subject EMAIL-E2-SUBJECT |
| E3 | Breadth and experts spotlight, drive free play | Open or play recorded (E1 direct or E2 open), plus 4 days, no subscription | 4 days after first open or play | Openers who have not subscribed | Email | copy-package.ar.md variant EMAIL-E3 | copy-package.en.md variant EMAIL-E3 | copy-package.ar.md subject EMAIL-E3-SUBJECT |
| E4 | Move to subscription (one unlocks all fields) | No subscription within 5 days of E3 | 5 days after E3 | Non-subscribers after E3 | Email | copy-package.ar.md variant EMAIL-E4 | copy-package.en.md variant EMAIL-E4 | copy-package.ar.md subject EMAIL-E4-SUBJECT |
| E5 | Last call | No subscription within 5 days of E4 | 5 days after E4 | Non-subscribers after E4 | Email | copy-package.ar.md variant EMAIL-E5 | copy-package.en.md variant EMAIL-E5 | copy-package.ar.md subject EMAIL-E5-SUBJECT |

### Per-message detail

#### E1: Breadth re-intro and free first lesson

- Purpose: warm re-entry. The reader knows the brand and never paid. The angle is breadth-led:
  this summer, many fields, one platform, one free first lesson in the field you choose. No
  deficit framing ("you stalled," "you wasted your signup"). Empowering: you are already here,
  summer is the window, pick a field and build a real skill.
- Trigger: contact enters the non-payer flow (registered, no active subscription, passes
  suppression check).
- Audience: all non-payers. Split NP-A (lapsed-engaged) and NP-B (never-engaged) if the
  recency signal is present in owned data. If absent, run unsplit.
- Copy ref: copy-package.ar.md variant EMAIL-E1 (AR body and subject); copy-package.en.md
  variant EMAIL-E1 (EN variant). Subject lines to be authored by copywriter-ar and
  copywriter-en under EMAIL-E1-SUBJECT. Three subject line options to be offered; one primary
  flagged at QA.
- CTA direction (for copywriter-ar): one clear CTA, driving to the platform's browse or field
  discovery page, or to a free first lesson of a featured class. No price in the body. No
  promotion unless confirmed. No personal or sensitive data in the URL. Deep link to the
  relevant in-app screen if the push platform supports it.
- Engagement event: email_open (E1), masterclass_play_start (chapter 1 or field intro).
  The play event is a stronger intent signal than an open; if play_start fires, treat as an
  opener for branching purposes.

#### E2: Re-angle for non-openers

- Purpose: earn the open with a different angle. The re-angle shifts toward the skill outcome,
  not the platform breadth. The body does not escalate urgency or repeat E1's hook; it takes
  a genuinely different angle (what you will be able to do, not what is available to you).
- Trigger: no email_open and no masterclass_play_start recorded within 3 days of E1.
- Audience: non-openers of E1 from NP-A and NP-B.
- Copy ref: copy-package.ar.md variant EMAIL-E2 (AR); copy-package.en.md variant EMAIL-E2
  (EN). Subject EMAIL-E2-SUBJECT: a fresh subject line, not a resend of E1's subject.
- CTA direction: same low-friction destination as E1. Still driving the free first lesson,
  not yet a subscription ask.
- Engagement event: email_open (E2), tracked separately from E1.

#### E3: Breadth and experts spotlight, drive free play

- Purpose: the warmed opener (who opened E1 or E2 but has not subscribed) gets a deeper
  look at the breadth: multiple fields, multiple recognized experts, each with a free first
  lesson. The goal is a masterclass_play_start on a second or third field visit, reinforcing
  that the platform has depth across fields, not just the one first touched.
- Trigger: email_open or masterclass_play_start recorded (from E1 direct path or from E2
  open), plus 4 days, no subscription_start yet.
- Audience: openers who have not subscribed.
- Copy ref: copy-package.ar.md variant EMAIL-E3 (AR); copy-package.en.md variant EMAIL-E3
  (EN). Subject EMAIL-E3-SUBJECT.
- CTA direction: drive to the platform's multi-field browse or to a second featured free
  lesson in a different field from E1. One CTA. No price in the body. No promotion unless
  confirmed. Named instructors in copy are confirm-at-gate; only cleared, page-sourced facts
  may be referenced.
- Exit branch: if subscription_start fires after E3 is sent, exit the contact from the flow
  immediately. Do not send E4 to a subscriber.
- Engagement event: email_open (E3), masterclass_play_start (second or further field),
  subscription_start (exit trigger).

#### E4: Move to subscription (one unlocks all fields)

- Purpose: make the subscription ask directly and plainly. The message frames the subscription
  as the thing that turns the breadth (already experienced via free first lessons) into full
  access across all fields. One subscription, all fields, all the instructors sampled and more.
  Value-led: lead with the transformation and the breadth, not with a price or a countdown.
- Trigger: no subscription_start within 5 days of E3.
- Audience: non-subscribers after E3.
- Copy ref: copy-package.ar.md variant EMAIL-E4 (AR); copy-package.en.md variant EMAIL-E4
  (EN). Subject EMAIL-E4-SUBJECT.
- CTA direction: subscription or plans page (no price in the body unless Ahmed confirms one
  and the asset requires it; no invented promotion). One clear CTA. No em dash. No
  accreditation implication.
- Exit branch: if subscription_start fires, exit immediately.
- Engagement event: email_open (E4), subscription_start (exit trigger).

#### E5: Last call

- Purpose: the final message in the flow. A last, plain, non-hyped last call. The message
  does not raise urgency beyond what is true: the summer window is real, the offer is still
  there. No manufactured scarcity. One reason, one CTA. After E5, contact exits the flow
  regardless of action and enters the sunset tracking window.
- Trigger: no subscription_start within 5 days of E4.
- Audience: non-subscribers after E4.
- Copy ref: copy-package.ar.md variant EMAIL-E5 (AR); copy-package.en.md variant EMAIL-E5
  (EN). Subject EMAIL-E5-SUBJECT.
- CTA direction: same destination as E4 (subscription or plans page). One CTA. No price
  unless confirmed. No promotion unless confirmed. Empowering, never deficit-framed.
- Exit: contact exits the flow after E5 regardless of action. No further sends in this flow.
  Contact enters the sunset tracking window per segmentation-logic.
- Engagement event: email_open (E5), subscription_start (exit trigger, still active during E5
  send window).

### Personalization

First name where available in the owned CRM, used in the greeting only. If first name is
absent, use a generic greeting. No sensitive data, no subscription-tier data, no behavioral
targeting data in URL parameters. Unsubscribe link and Maharat sender identity present in
every message. No personal or sensitive data in any tracking URL parameter.

### Flow diagram (text form)

```
Entry: registered, no active subscription, passes suppression check
    |
    v
[E1] Breadth re-intro and free first lesson
(all non-payers; split NP-A / NP-B on recency if signal present, unsplit if absent)
    |
    |-- Open or play within 3 days? --YES----+
    |                                        |
    |-- No open, no play at 3 days           |
    |                                        |
    v                                        |
[E2] Re-angle for non-openers               |
    |                                        |
    |-- Open E2?                             |
    |                                        |
    +----------------------------------------+
                                             |
                                         4 days after first open or play
                                             |
                                             v
                                    [E3] Breadth and experts spotlight, drive free play
                                             |
                                   subscription_start fires? --YES--> EXIT, enter onboarding
                                             |
                                     No subscription at 5 days
                                             |
                                             v
                                    [E4] Move to subscription (one unlocks all fields)
                                             |
                                   subscription_start fires? --YES--> EXIT, enter onboarding
                                             |
                                     No subscription at 5 days
                                             |
                                             v
                                    [E5] Last call
                                             |
                                   subscription_start fires? --YES--> EXIT, enter onboarding
                                             |
                                     No subscription
                                             |
                                             v
                                    EXIT FLOW, enter sunset tracking
```

---

## 4. App push sequence (P1..P5)

### Audience

Owned app users who have not subscribed. App audience size is OPEN ITEM per brief s.4 and
strategy-artifact s.3.2. Suppress subscribed users and any user who has revoked push
permission at the OS level. Confirm the OS-level consent model and opt-out suppression when
the push platform is named.

### Sequence (references PUSH-P1..P5 from copy-package.ar.md and copy-package.en.md)

The push sequence is a light reinforcement layer alongside the email flow, not a duplicate.
Push and email do not fire on the same day (coordination logic below). Copy packages are
pending; the flow references variant ids as agreed.

| ID | Proposed timing from entry | Goal | Copy ref (AR) | Copy ref (EN) | Deep link target |
|---|---|---|---|---|---|
| P1 | Day 1 (at entry) | Breadth re-intro, surface a free first lesson | copy-package.ar.md variant PUSH-P1 | copy-package.en.md variant PUSH-P1 | Field browse or free first lesson screen in-app |
| P2 | Day 5 | Re-angle on skill outcome (if no E2 email open yet) | copy-package.ar.md variant PUSH-P2 | copy-package.en.md variant PUSH-P2 | Field browse or free first lesson screen |
| P3 | Day 10 | Breadth spotlight, drive a second free lesson play | copy-package.ar.md variant PUSH-P3 | copy-package.en.md variant PUSH-P3 | Featured class or chapter 1 screen for a second field |
| P4 | Day 16 | Move to subscription (one unlocks all fields) | copy-package.ar.md variant PUSH-P4 | copy-package.en.md variant PUSH-P4 | Subscription or plans screen in-app |
| P5 | Day 22 | Last call | copy-package.ar.md variant PUSH-P5 | copy-package.en.md variant PUSH-P5 | Subscription or plans screen |

All timing is ASSUMPTION (cadence not confirmed in the brief; proposed light cadence per
strategy-artifact s.3.2 and push-notification-principles.md). Confirm with Ahmed.

### Push craft principles (from push-notification-principles.md, applied here)

- One goal per push. Each of P1..P5 carries exactly one job and one tap target.
- Micro-storytelling: each push is a one-line story with a hook, not a system message.
- Thumb-stop standard: copywriter-ar and copywriter-en must ensure the first three words
  stop the scroll.
- Mindset timing: proposed timing above targets mid-day or early-evening sends (ASSUMPTION).
  Confirm local send times per market (Saudi Arabia primary) once the push platform is named.
- Weekly rhythm: P1..P5 over about 22 days is a planned cadence, not ad-hoc.
- Arabic-first. Western numerals. Empowering, not deficit-framed. One CTA per push.

### Push and email coordination logic

- P1 fires on day 1 alongside E1 entry. Both fire at entry; this is the campaign open and
  is by design. On subsequent days, push and email do not fire on the same calendar day to
  avoid channel collision. (The proposed timing above already separates them: E2 at 3 days,
  P2 at 5 days; E3 at 7 days from entry on the opener path, P3 at 10 days; E4 around day 12,
  P4 at 16; E5 around day 17, P5 at 22.)
- If a user subscribes (subscription_start), exit them from both the email flow and the
  remaining push sequence on the same event. Do not send further messages to a subscriber.
- Cap the push sequence at 5 touches over the flight. Respect quiet hours and any per-user
  push frequency cap the push platform enforces (platform to confirm).
- Deep links go directly to the relevant in-app screen. No URL with personal data. No
  personal or sensitive data in any push tracking parameter. If a subscription step requires
  an in-app flow, route to the in-app subscription screen rather than an external browser.

### Push platform open item

Push platform is unconfirmed per brief s.7 and strategy-artifact s.6. Push wiring is blocked.
Design proceeds. Confirm the platform, OS-level consent model, opt-out suppression mechanism,
and quiet-hours enforcement before wiring.

---

## 5. Onboarding shape for new subscribers (post-conversion coordination note)

New contacts who subscribe during this campaign exit the non-payer flow and enter a
post-conversion onboarding sequence. This section is a coordination note only, not a full
flow build: the copy for these messages is not yet briefed, and the onboarding SOP and
subscription platform are both pending. The shape is defined here for handoff coordination
with copywriter-ar, copywriter-en, and the onboarding sequence sub-skill.

### Entry trigger

subscription_start event confirmed. Contact exits the non-payer email flow and the push
sequence immediately on this event.

### Proposed shape (3 touches, cadence ASSUMPTION, confirm with Ahmed)

| ID | Timing | Goal | Content direction | Copy status |
|---|---|---|---|---|
| O1 | Immediately on subscription_start | Welcome and orient the new subscriber | Confirm access, orient to the breadth of fields and instructors, invite the first session in the field of their choice, link to chapter 1 of a featured class. Warm, empowering: "you are in." Not a receipt. | To be briefed to copywriter-ar and copywriter-en after onboarding SOP and platform are confirmed |
| O2 | Day 3 after subscription | First progress nudge | If first-session data is available from the platform, acknowledge progress. If not, encourage the first session in a field of their choice. Surface the next chapter in a featured class as the natural next step. Empowering, skill-momentum framing. | To be briefed |
| O3 | Day 7 after subscription | Habit and breadth | Reinforce the value of a short regular session. Reference real, cleared class content from copy-package to show the depth ahead. Surface a second field as a discovery prompt. Not salesy. Practical and confident. | To be briefed |

These three messages (O1, O2, O3) are not yet authored. Briefs for O1..O3 are created once
the onboarding SOP is confirmed and the subscription platform is named. All onboarding copy
must pass arabic-copy-qa, english-copy-qa, and brand-qa before the onboarding flow advances.

### Suppression for onboarding

No suppression beyond the subscription confirmation itself. If a subscriber cancels, they
re-enter the non-payer flow only if they are still on the contact base and have not
unsubscribed from email.

---

## 6. Engagement events: coordination with data-tracking-engineer

The lifecycle flow depends on behavioral signals to branch correctly. These events are designed
here as a coordination handoff. Data-tracking-engineer owns the event naming, the schema
definitions, the warehouse plumbing, and the send-platform event listener wiring. This agent
owns the flow logic that consumes those events, not the data layer.

Event names below are proposed. Data-tracking-engineer must confirm final names, schemas, and
the send-platform and warehouse listener configuration. The flow logic does not change on
renaming; only the event key passed to the ESP or push platform changes.

### Email events needed

| Event (proposed name) | Fires when | Used by lifecycle flow for |
|---|---|---|
| email_sent | Platform records a successful delivery | Audit trail per message; inter-message delay timer starts |
| email_open | Recipient opens the email | E1 open triggers E3 direct path; E2 open triggers E3; branch condition for all messages |
| email_click | Recipient clicks any CTA link | Supplementary engagement signal; use where open tracking is unreliable (image blocking) |
| masterclass_play_start | User starts chapter 1 or any free-lesson playback (from email CTA) | Additional branch signal stronger than an open; treated as an opener for E1 and E2 branching |
| subscription_start | User completes a paid subscription purchase | Exit trigger from the non-payer flow at any message; entry trigger for onboarding |
| email_unsubscribe | User actions the unsubscribe link | Immediate suppression; contact exits all flows and the list |
| email_hard_bounce | Platform records a permanent delivery failure | Suppression list update; do not retry |

### App push events needed

| Event (proposed name) | Fires when | Used by lifecycle flow for |
|---|---|---|
| push_sent | Platform records a successful send | Audit trail |
| push_open | User taps the push notification | Engagement signal; informs push sequence branch and sunset logic |
| push_tap_field | User deep-links to a field or free lesson from push | Stronger intent signal than a raw open |
| subscription_start | Same event as email; shared signal across platforms | Exit from push sequence; must be reliable across both channels |
| push_opt_out | User revokes push permission at OS level | Immediate suppression from push sequence; no override |

### Privacy and data rules for event design (co-design note)

- No personal or sensitive data in any event URL parameter or tracking string.
- The subscription_start event in particular is the critical exit and entry trigger across
  email, push, and the conversion platform. It must be reliable and consistent before any
  send is wired.
- All event data flowing to the warehouse must be scoped to what PDPL and the confirmed legal
  basis allow. Data-tracking-engineer and compliance-privacy-reviewer must align on the event
  schema before any tracking is wired, per brief s.10 and strategy-artifact s.6
  (PDPL-and-data-residency-open-item).

---

## 7. Audience size

- Email non-payer flow: about 18,000 non-paying contacts. Planning estimate from brief s.4
  and company brief. Exact figure resolved from live CRM or ESP export at send time, after
  suppression is applied. Recorded in the final send package before human-gate approval.
- App push audience: OPEN ITEM. App user segment size not confirmed in the brief or
  strategy-artifact. Resolves when the push platform is confirmed and the segment pull is run.
- New subscriber onboarding: not a fixed size. Onboarding entry is event-triggered per
  subscription_start. Size tracks with campaign conversion volume, not predetermined.

---

## 8. Send on approval

Sending the email non-payer flow (E1..E5) means: a 5-message triggered email sequence goes
to the resolved non-paying email segment (about 18,000 contacts at planning estimate, exact
figure confirmed at send after suppression), branching on opens and plays, over approximately
3 to 4 weeks from entry, within the confirmed campaign window, with suppression applied for
paying contacts, unsubscribed, and hard-bounced addresses, starting only on confirmation
of the email platform, Saudi PDPL compliance posture, and Ahmed's explicit per-send approval.

Sending the app push sequence (P1..P5) means: 5 push notifications go to the resolved
non-paying app user segment (size OPEN ITEM), spaced over approximately 22 days from entry,
with suppression for subscribed users and push opt-outs, starting only on confirmation of the
push platform, OS-level consent model, and Ahmed's explicit per-send approval.

Onboarding (O1..O3) does not send until copy is authored, QA-passed, and Ahmed approves the
onboarding sequence separately.

Nothing sends until the platform is confirmed and Ahmed approves. The email flow, the push
sequence, and the onboarding sequence are three separate approval actions. Silence is not
approval.

---

## 9. Quality gate status

| Gate | Result | Notes |
|---|---|---|
| skill_eval (07-lifecycle-messaging) | Pass | Flow structure, segmentation logic, trigger logic, engagement branches, suppression, sunset rule, copy id referencing, open-item surfacing, brand mechanical rules all verified against evals.json |
| arabic_qa | Ref (pending copy) | copy-package.ar.md is pending. All EMAIL-E1..E5 and PUSH-P1..P5 AR variants must carry arabic-copy-qa pass before this package advances |
| english_qa | Ref (pending copy) | copy-package.en.md is pending. All EN variants must carry english-copy-qa pass |
| brand_qa | Ref (pending copy) | All referenced variants must carry brand-qa-reviewer pass. This package carries status draft until all referenced copy variants are produced and QA-passed |
| compliance | Ref (pending) | compliance-privacy-reviewer must run on the full send package. 13 open items (items 2 through 14 above) carry compliance implications. No activation until all are resolved |

This package carries status: draft. It advances to qa-passed when all referenced copy
variants are produced, QA-passed, and the compliance review is complete.

---

## 10. Human gate package (stop here)

The send is a gated action. This package stops at the human gate. Nothing in this document
authorizes any send, push delivery, pixel activation, or wiring.

Ahmed must resolve before any activation:

1. Confirm copy-package.ar.md and copy-package.en.md production and QA status. The flow
   cannot advance until all referenced variants (EMAIL-E1..E5, PUSH-P1..P5) carry
   arabic-copy-qa pass, english-copy-qa pass, and brand-qa pass.
2. Name the email platform and push platform. Send wiring is blocked until both are named.
   Saudi PDPL data-residency decision is also independently blocking.
3. Confirm or override the proposed schedule (start 2026-07-01, end 2026-08-31, email
   sequence cadence, push sequence cadence).
4. Confirm or deny any promotion (trial, discount, bundle). None is assumed; none is in any
   copy variant.
5. Confirm which plan(s) the campaign leads with (1, 3, or 12 month).
6. Confirm the success metric target number and measurement date.
7. Confirm the suppression source (the CRM or ESP list that will be pulled for paying
   contacts, unsubscribed, and hard-bounced at send time).
8. Confirm whether the recency signal (last open or last activity) is available in the owned
   data to support the NP-A/NP-B split. If absent, the flow runs unsplit and Ahmed must
   acknowledge that.
9. Confirm the gender address decision for all Arabic email and push copy (consistent address,
   or intentional per-segment split by field). This decision must be made with copywriter-ar
   before any Arabic copy goes to QA.
10. Confirm approved instructor photography and class imagery for each named instructor before
    any such imagery appears in email headers or push visuals.
11. Confirm per-instructor public-naming clearance at gate for each of the seven nameable
    instructors (Ragheb Alama, Salam Dakkak, Kosai Khauli, Bassam Fattouh, Toufic Kreidieh,
    Cedric Haddad, Elda Choucair).
12. Confirm Saudi PDPL compliance and data-residency posture. compliance-privacy-reviewer
    runs on the full package; no wiring until their verdict is clean.
13. Review and accept all 15 open items listed in the envelope above.

Approval is per action, per send, per channel. Approval of this lifecycle package does not
approve the paid spend, the organic posts, the web conversion page, or any other stream
artifact. Each stream is approved separately. Silence is not approval.
