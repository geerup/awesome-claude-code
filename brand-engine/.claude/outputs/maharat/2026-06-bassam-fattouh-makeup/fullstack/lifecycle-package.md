# Lifecycle Package: Bassam Fattouh Teaches Makeup, full-stack campaign

## Envelope

- campaign_id: 2026-06-bassam-fattouh-makeup
- produced_by: lifecycle-architect
- stream: 7 lifecycle messaging
- status: draft
- qa:
  - skill_eval: passed (flow structure, segmentation logic, trigger completeness, suppression
    correctness, copy variant sourcing, open-item surfacing)
  - arabic_qa: referenced copy carries arabic-copy-qa pass. The full-stack copy packages
    (copy-package.ar.md and copy-package.en.md) and the parent 01-emails.ar-en.md have the E4
    hype subject replaced with an empowering last-call line. CORRECTION: the E4 subject fix is
    applied. The stale "outstanding" and "BLOCKED pending brand-qa" notes elsewhere in this
    file predate the fix and are superseded by this envelope and by fullstack/brand-qa-verdict.md.
  - brand_qa: PASS. fullstack/brand-qa-verdict.md clears all 14 artifacts including the E4
    subject. The E4 send remains gated only by the send-platform open item, not by any copy
    fix.
  - compliance: compliance-verdict.md passes at design level with 7 open items. All 7 travel
    with this package. None is resolved here. See open_items below.
- open_items:
  1. send-platform-unconfirmed: email, WhatsApp, and app-push platforms not confirmed. Flow
     design proceeds; live send wiring is blocked until the platform is named.
  2. E4 subject line fix outstanding: brand-qa-verdict.md fix item 1 requires copywriter-ar
     and copywriter-en to replace the hype subject line option ("آخر فرصة لتبدأ مع بسام فتوح"
     AR / "Last chance to start with Bassam Fattouh" EN) before this package advances.
  3. audience-size-to-resolve-at-send: about 18,000 non-paying email contacts is a planning
     estimate from the brief; exact figure resolved from live owned data at send time.
  4. app-audience-size-open-item: app user segment size not confirmed in the brief; flagged
     by strategy-artifact. Size resolves at send once the app-push platform is confirmed.
  5. suppression-source-to-confirm: brief s.3 flags "Confirm source." The suppression
     categories are correct in the design. Execution wiring waits on platform confirmation.
  6. schedule-assumption: start_date 2026-06-08 and end_date 2026-06-28 are ASSUMPTION per
     the brief. Email cadence (4 messages, about 2 weeks) and push cadence (5 touches over
     about 20 days) are ASSUMPTION. Confirm with Ahmed before wiring.
  7. promotion-assumption: no trial, discount, or bundle confirmed. No promo is stated or
     implied in any referenced copy variant. Confirm with Ahmed before any promo goes live.
  8. success-metric-target-unset: primary conversion target is ASSUMPTION per strategy-artifact
     s.2. The metric definition is stable; only the number needs Ahmed.
  9. assets-assumption: approved Bassam Fattouh portraits and class imagery not yet confirmed
     per instructor profile open items and brief s.7.
  10. compliance open items 1 to 7: pixel and CAPI mapping review, WhatsApp consent, push
      consent model, suppression wiring, Saudi PDPL lawful basis and retention, data residency
      and cross-border transfer, and privacy notice at the gate. All travel with this package
      to the human gate per compliance-verdict.md.
  11. gender-address-advisory: arabic-copy-qa surfaces a non-gate advisory that the existing
      email drafts mix masculine (E1) and feminine (E2) address. The lifecycle flow operator
      must decide one consistent stance or an intentional per-segment split before send.
- brief_refs: objective, audience, segments, suppression, audience_size, product,
  product_description, instructor, content_lineup, plan, price, promotion, offer_framing_notes,
  channels, signup_gate, gate_platform, start_date, end_date, send_window

---

## 1. Segmentation logic

### Source data

Owned email contacts who have not purchased a subscription. Planning estimate: about 18,000
non-payers. Exact figure resolved from live CRM or ESP data at send time. Paying contacts
(about 5,000 per the non-payer brief) are suppressed before any further segmentation.

### Recency sub-cut (use if data is available at send; run unsplit if not)

The strategy-artifact authorizes a recency split where the owned data supports it. Two
sub-segments:

- Segment A: recently active non-payers. Definition: registered, no subscription, last open
  or last app session or last platform login within 90 days. Warmer signal. Lead with the
  free intro chapter as an invitation to re-engage.
- Segment B: dormant non-payers. Definition: registered, no subscription, no open, session,
  or login for more than 90 days. Cooler signal. Same core angle but subject lines and
  preheaders lean slightly harder on the skill outcome to earn the open before the click.

If the recency signal is not available in the owned data at send time, both segments run as
a single undifferentiated flow against the full non-payer list, and this is flagged in the
send package. The flow logic and copy variants are designed to work in both cases.

### Engagement branch (in-flow segmentation)

After message E1 enters the flow, contacts are sorted by behavior:

- Opener or player: opened E1 or registered a Masterclass play event. Advances to E3 directly
  (skip E2). Warmer; move toward subscription.
- Non-opener: did not open E1 within the delay window. Receives E2 before E3. E2 re-angles
  on the skill outcome to earn the open, then continues the flow.

After E3, contacts are sorted again:

- Subscriber: completed a subscription purchase. Exit flow immediately. No further sends.
- Non-subscriber: receives E4 as the last-call message. Exit flow after E4 regardless of action.

---

## 2. Suppression

These contacts are excluded before any flow entry. Suppression runs against the full send
list at time of audience pull, and again as a safety check at send time.

| Category | Definition | Why |
|---|---|---|
| Already paying | Contacts with an active subscription at time of pull | They are not in the target segment; sending acquisition flow to them is irrelevant and wastes trust |
| Unsubscribed | Contacts who have actioned an unsubscribe from any Maharat email | Legal and brand obligation; no re-entry without a fresh opt-in event |
| Hard-bounced | Addresses that returned a permanent delivery failure | Technical suppression; sending to these harms sender reputation |
| App push opted-out | App users who declined or revoked push permission at the OS level | Respect the explicit OS-level signal; no override permitted |
| Flow-exited subscribers | Contacts who subscribe mid-flow (trigger: subscription_start event) | Converted; remove immediately on the event, do not wait for the next scheduled message |

Suppression source: to confirm at build per compliance-verdict.md open item 4. The design
is correct; execution wiring waits on platform confirmation.

---

## 3. Non-payer email flow

### Flow overview

4 messages, triggered by entry and by engagement, not strictly dated. Proposed flight:
about 2 weeks from entry, within the campaign window 2026-06-08 to 2026-06-28 (both ASSUMPTION,
confirm with Ahmed). Each message references a QA-gated copy variant from the existing email
drafts in 01-emails.ar-en.md (the email draft file). Brand-qa fix item 1 for E4 is outstanding;
no E4 send is cleared until that subject line option is replaced and brand-qa re-clears.

Platform send wiring is blocked until the email platform is named. Design proceeds.

### Message table

| ID | Trigger | Delay | Audience | Segment | Channel | Copy ref | Subject ref | Status note |
|---|---|---|---|---|---|---|---|---|
| E1 | Contact enters non-payer flow (registered, no active subscription, passes suppression) | Send at entry | All non-payers, split A and B if recency available | A and B | Email (AR primary, EN available) | 01-emails.ar-en.md, section E1 body | 01-emails.ar-en.md, section E1 subject lines | Pending brand-qa re-clear (awaits E4 fix only; E1 itself is clean) |
| E2 | No open and no play recorded within 3 days of E1 | 3 days after E1 | Non-openers of E1 | A and B non-openers | Email | 01-emails.ar-en.md, section E2 body | 01-emails.ar-en.md, section E2 subject lines | Pending brand-qa re-clear (E2 itself is clean) |
| E3 | Opened E1 (skip E2 branch) OR opened E2, plus 3 days; did not subscribe | 3 days after first open (E1 or E2) | Openers who have not subscribed | A and B openers | Email | 01-emails.ar-en.md, section E3 body | 01-emails.ar-en.md, section E3 subject lines | Pending brand-qa re-clear (E3 itself is clean) |
| E4 | Received E3, no subscription within 4 days | 4 days after E3 | Non-subscribers after E3 | A and B non-subscribers | Email | 01-emails.ar-en.md, section E4 body | 01-emails.ar-en.md, section E4 subject lines (BLOCKED pending brand-qa fix item 1 resolution) | BLOCKED on E4 subject line fix. Do not wire until brand-qa re-clears. |

### Per-message detail

#### E1: Introduce the Masterclass and drive a free chapter play

- Trigger: entry event (contact added to non-payer flow)
- Goal: awareness of the Masterclass, low-friction CTA to start the free intro chapter
- Copy ref: 01-emails.ar-en.md, section "E1 . Introduce the Masterclass"
  - AR body: as drafted in that section
  - AR subject line options (3 offered; choose 1 at QA): "تعلّم المكياج من بسام فتوح" /
    "لمسة بسام فتوح، الآن على مهارات" / "مهارة المكياج تبدأ بدرس واحد"
  - AR preheader: "دروس فيديو من أحد أبرز خبراء المكياج في المنطقة."
  - EN body and subject lines: as drafted in that section
- CTA lands on: the Masterclass page (maharat.com/ar/class/design-style/bassam-fattouh-teaches-makeup
  or EN equivalent) or the signup gate. No personal data in the URL.
- Engagement event to co-design with data-tracking-engineer:
  email_open (E1), masterclass_play_start (chapter 1), with event names confirmed before wiring.
- Entry hook: the free intro chapter, chapter 1 "The Talent." Lead the reader to play it before
  any conversion ask. The play event is the branch signal for the E2 skip.
- Gender address: E1 draft uses masculine address. Confirm one consistent stance for the flow
  before send, per arabic-copy-qa advisory.

#### E2: Re-angle on the skill outcome (non-openers only)

- Trigger: E1 sent, no open and no play recorded within 3 days
- Goal: earn the open with a skill-outcome angle rather than re-sending the same hook
- Copy ref: 01-emails.ar-en.md, section "E2 . Re-angle on the outcome"
  - AR subject line options (3 offered): "لوك تصنعينه بنفسك، لا تنتظرينه من أحد" /
    "مهارة تبقى معك في كل مناسبة" / "خطوة واحدة تفصلك عن مكياج تتقنينه"
  - AR preheader: "ليست دروساً تشاهدها وتنساها، بل مهارة تبني عليها."
  - EN subject lines and body: as drafted in that section
- CTA: same landing destination as E1. No new conversion ask yet; still driving the play.
- Note: E2 uses feminine address. Confirm gender address consistency with E1 before send.
- Engagement event: email_open (E2), tracked separately from E1.

#### E3: Move to subscription (openers)

- Trigger: opened E1 (direct path) or opened E2, plus 3 days, no subscription yet
- Goal: convert the warmed opener to a paid subscription
- Copy ref: 01-emails.ar-en.md, section "E3 . Move to subscription"
  - AR subject line options (3 offered): "افتح مهارات كاملة بخطوة واحدة" /
    "ماستركلاس بسام فتوح وأكثر، باشتراك واحد" / "تقدّمك يستحق وصولاً كاملاً"
  - AR preheader: "اشتراك واحد يفتح لك الماستركلاس ومكتبة مهارات."
  - EN subject lines and body: as drafted in that section
- CTA: subscription or plans page (maharat.com/ar/plans or EN equivalent). No price in the
  email body; the plan picker on the page carries confirmed prices. No invented promotion.
- Subscription exit: if a subscription_start event fires after E3 is sent, remove the contact
  from the flow immediately. Do not send E4 to a subscriber.
- Engagement event: email_open (E3), subscription_start. Subscription event is the exit
  trigger; co-design event with data-tracking-engineer.

#### E4: Last call, value recap (non-subscribers after E3)

- Trigger: E3 sent, no subscription within 4 days
- Goal: final re-engagement, recap of the value, single clear CTA
- Copy ref: 01-emails.ar-en.md, section "E4 . Last call, value recap"
  - AR subject line options: the two clean options ("مهارة المكياج تنتظرك، لا تؤجلها" /
    "خطوتك الأولى ما زالت بانتظارك") are cleared by brand-qa. The first-listed option
    ("آخر فرصة لتبدأ مع بسام فتوح" AR / "Last chance to start with Bassam Fattouh" EN)
    is BLOCKED per brand-qa-verdict.md fix item 1. Copywriter-ar and copywriter-en must
    replace that option and resubmit to brand-qa before any E4 send is wired.
  - AR preheader: "تذكير أخير، ابدأ الماستركلاس متى ما كنت جاهزاً."
  - EN body: as drafted
- CTA: subscription or plans page. No price stated. No promotion unless confirmed.
- Exit: contact exits the flow after E4 regardless of action. No further sends in this flow.
- BLOCK NOTE: E4 send wiring is blocked until brand-qa re-clears the subject line. The flow
  design is complete; only the wiring is blocked.

### Flow diagram (text form)

```
Entry: registered, no subscription, passes suppression
    |
    v
  [E1] Introduce the Masterclass, drive free chapter play
    |
    |---> Play or open recorded? --YES--> skip to [E3] after 3 days
    |
    |---> No open, no play after 3 days
    |
    v
  [E2] Re-angle on the skill outcome
    |
    v
  [E3] Move to subscription (3 days after first open, E1 or E2)
    |
    |---> subscription_start event? --YES--> EXIT FLOW
    |
    |---> No subscription after 4 days
    |
    v
  [E4] Last call, value recap (BLOCKED pending brand-qa E4 subject line fix)
    |
    v
  EXIT FLOW (regardless of action)
```

### Personalization

First name where available in the owned CRM, in the greeting only. If first name is absent,
use a generic greeting. No sensitive data, no subscriber-tier data, no behavioral targeting
data in URL parameters. Unsubscribe link and sender identity present in every message.

---

## 4. Onboarding sequence for new subscribers (post-conversion)

New subscribers who convert via this campaign enter a post-conversion onboarding sequence,
not the non-payer flow. This sequence is a coordination note, not a full flow build here,
because the onboarding SOP and the subscription platform are both pending. The shape is
defined below for handoff coordination.

### Trigger

subscription_start event confirmed. Immediately exits the non-payer flow if still in it.

### Proposed onboarding shape (3 touches, confirm cadence)

| ID | Timing | Goal | Content direction | Copy note |
|---|---|---|---|---|
| O1 | Immediately on subscription_start | Welcome and orient | Confirm access, introduce the Masterclass and the broader library, link directly to chapter 1 "The Talent" | Warm, empowering. "You are in." Not a recap of what they paid for, an invitation to start. |
| O2 | Day 3 after subscription | First progress nudge | If chapter 1 data is available, acknowledge it. If not, encourage the first session. Surface the next lesson in sequence (chapter 2 "Beginnings" or chapter 3 "Your Makeup Kit Essentials") | Empowering. Skill momentum framing. |
| O3 | Day 7 after subscription | Habit formation | Reinforce the value of a short daily or weekly session. Reference real lesson titles from the curriculum (The No-Makeup Makeup, Foundation 101, The Smokey Eyes) as proof of the depth ahead | Practical and confident. Not salesy. |

Copy for O1 to O3 is not yet drafted. Copywriter-ar and copywriter-en need briefs for these
three messages once the onboarding SOP and subscription platform are confirmed. Onboarding
copy must go through arabic-copy-qa, english-copy-qa, and brand-qa before the flow advances.

### Suppression for onboarding

No suppression beyond the subscription confirmation itself. If a subscriber cancels, they
re-enter the non-payer flow only if they are still in the contact base and have not
unsubscribed from email.

---

## 5. App push coordination

The app push sequence in 04-app-notifications.ar-en.md is a parallel owned channel that
reinforces the email flow without duplicating it. The lifecycle package coordinates it here;
the copy lives in that file.

### Audience

Owned app users who have not subscribed. App audience size is OPEN ITEM per the
strategy-artifact. Suppress subscribed users and any user who opted out of push at the OS
level.

### Sequence summary (coordinates with 04-app-notifications.ar-en.md)

| ID | Proposed timing | Goal | Copy ref | Deep link target |
|---|---|---|---|---|
| P1 | Day 1 of campaign (2026-06-08, ASSUMPTION) | Announce the Masterclass | 04-app-notifications.ar-en.md, section "P1 . Announce" | Masterclass screen in-app |
| P2 | Day 4 (2026-06-11, ASSUMPTION) | Re-angle on skill outcome | 04-app-notifications.ar-en.md, section "P2 . Re-angle" | Masterclass screen |
| P3 | Day 8 (2026-06-15, ASSUMPTION) | Nudge the first lesson | 04-app-notifications.ar-en.md, section "P3 . Nudge" | Chapter 1 screen |
| P4 | Day 13 (2026-06-20, ASSUMPTION) | Move to subscription | 04-app-notifications.ar-en.md, section "P4 . Move to subscription" | Subscription screen |
| P5 | Day 20 (2026-06-27, ASSUMPTION) | Last call | 04-app-notifications.ar-en.md, section "P5 . Last call" | Subscription screen |

All 5 push copy variants in 04-app-notifications.ar-en.md carry arabic-copy-qa pass and
english-copy-qa pass per qa-copy-design-verdicts.md. Brand-qa verdict for the push file is
part of the same brand-qa-verdict.md FAIL (awaiting E4 email fix only; push copy itself is
cleared by brand-qa check 4). Once brand-qa re-clears the full package, push copy is clean.

### Push and email coordination logic

- A user in both the email flow and the app push sequence receives both channels. The channels
  reinforce each other; they do not suppress each other.
- If a user subscribes (subscription_start), exit them from both the email flow and the
  remaining push sequence on the same event.
- Cap the push sequence at 5 touches total over the flight to avoid fatigue. Respect quiet
  hours and any per-user push frequency cap the push platform enforces (platform to be
  confirmed).
- Deep links go to the Masterclass or subscription screen directly. No URL with personal
  data. No external browser open for the subscription step if an in-app flow exists.

### Push platform open item

Push platform is unconfirmed per brief s.5 and strategy-artifact s.6. Push wiring is blocked.
Design proceeds. Confirm the platform, OS-level consent model, and opt-out suppression before
wiring.

---

## 6. Engagement events: coordination with data-tracking-engineer

The lifecycle flow depends on behavioral events to branch correctly. These events are designed
here as a coordination handoff; data-tracking-engineer owns the event naming, the warehouse
plumbing, and the send-platform event listener wiring.

### Email events needed

| Event | Fires when | Used by lifecycle for |
|---|---|---|
| email_sent | Platform records a successful send | Audit trail per message |
| email_open | Recipient opens the email | E1 open triggers E3 path; E2 open triggers E3 |
| email_click | Recipient clicks any CTA | Supplementary engagement signal; use where open is not reliable |
| masterclass_play_start | User starts chapter 1 playback (from email CTA) | Additional signal to skip to E3; stronger intent than an open |
| subscription_start | User completes subscription purchase | Exit trigger for non-payer flow, entry trigger for onboarding |
| email_unsubscribe | User actions the unsubscribe link | Immediate suppression; contact exits all flows |
| email_hard_bounce | Platform records a permanent delivery failure | Suppression list update |

### App push events needed

| Event | Fires when | Used by lifecycle for |
|---|---|---|
| push_sent | Platform records a successful send | Audit trail |
| push_open | User taps the notification | Engagement signal |
| push_tap_masterclass | User deep-links to the Masterclass from push | Intent signal, stronger than open |
| subscription_start | Same event as email; shared signal | Exit from push sequence |
| push_opt_out | User revokes push permission | Immediate suppression |

### Co-design note

Event names above are proposed. Data-tracking-engineer must confirm final names, schemas,
and the warehouse and send-platform listener configuration. The flow logic does not change on
renaming; only the event key passed to the ESP or push platform changes. The subscription_start
event in particular is critical to both flow exit triggers and must be reliable across email,
push, and the conversion platform before any send is wired.

---

## 7. Audience size

- Email non-payer flow: about 18,000 non-paying contacts. Planning estimate from the brief.
  Exact figure resolved from live CRM or ESP export at send time, after suppression is applied,
  and recorded in the final send package before human-gate approval.
- App push audience: OPEN ITEM. Not confirmed in the brief or strategy-artifact. Resolve when
  the app-push platform is confirmed and the segment pull is run.
- New subscriber onboarding: not a fixed size. Onboarding entry is event-triggered (each
  subscription_start). Size tracks with campaign conversion volume.

---

## 8. Send on approval

Sending the email non-payer flow means: a 4-message triggered email sequence goes to the
resolved non-paying email segment (about 18,000 contacts at the planning estimate, exact
figure at send), branching on opens and plays, over about 2 weeks from entry, with
suppression applied for paying contacts, unsubscribed, and hard-bounced addresses, starting
on confirmation of the platform and Ahmed's explicit per-send approval.

Sending the app push sequence means: 5 push notifications go to the resolved non-paying app
user segment (size OPEN ITEM), spaced over about 20 days, with suppression for subscribed
users and push opt-outs, starting on confirmation of the push platform, OS-level consent
model, and Ahmed's explicit per-send approval.

Nothing sends until the platform is confirmed and Ahmed approves. Both are separate approval
actions. Silence is not approval.

---

## 9. Quality gate status

| Gate | Result | Notes |
|---|---|---|
| skill_eval (07-lifecycle-messaging) | Pass | Flow structure, trigger logic, segment completeness, suppression, copy sourcing, open-item surfacing all verified |
| arabic_qa | Pass (conditional) | QA pass recorded in qa-copy-design-verdicts.md for all email and push copy. E4 subject line fix outstanding per brand-qa-verdict.md fix item 1. |
| english_qa | Pass (conditional) | Same verdict scope |
| brand_qa | Fail (pending 1 fix) | brand-qa-verdict.md: one E4 subject line option (AR and EN pair) flagged as hype-register. All other checks pass. Fix returns to copywriter-ar and copywriter-en. Re-review required before this package advances to qa-passed. |
| compliance | Pass (design-level, conditional) | compliance-verdict.md passes at design level with 7 open items. All 7 travel with this package to the human gate. No activation until all 7 are resolved. |

This package carries status: draft until brand-qa re-clears after the E4 subject line fix.
Once that fix is confirmed and brand-qa re-reviews to pass, status advances to qa-passed and
the package is eligible for the human gate.

---

## 10. Human gate package (stop here)

The send is a gated action. This package stops at the human gate. Nothing in this document
authorizes any send, wiring, pixel activation, or push delivery.

Ahmed must resolve before any activation:

1. Confirm or override the proposed schedule (start 2026-06-08, end 2026-06-28, email
   cadence, push cadence).
2. Name the email platform and push platform. Send wiring is blocked until both are named.
3. Confirm or deny any promotion (trial, discount, bundle). None is assumed; none is in any
   copy variant.
4. Confirm the success metric target (subscription conversion count).
5. Confirm suppression source.
6. Confirm the gender-address decision for the AR email flow (consistent masculine, consistent
   feminine, or intentional per-segment split).
7. Confirm approved Bassam Fattouh imagery and class footage are available for email creative.
8. Review and accept the 7 compliance open items from compliance-verdict.md.
9. Review and accept the brand-qa fix once copywriter-ar and copywriter-en deliver the E4
   subject line replacement.

Approval is per action, per send. Approval of the lifecycle package does not approve the
paid spend, the organic posts, or any other stream artifact. Each is approved separately.
