# Sequence standards (stream 7 lifecycle messaging)

The reusable, audience-and-objective-focused standards library for every lifecycle sequence
the engine designs. It is a design reference, not a license to send. Every actual send still
passes the gate stack (skill eval, arabic-copy-qa or english-copy-qa, brand-qa-reviewer, and
compliance-privacy-check for the send), the suppression and consent rules, and the human gate,
per `runtime/verification.md` and `sops/07-lifecycle-nonpayer-email.md`.

These standards are synthesized from canonical webinar, onboarding, and welcome sequence
frameworks, drawn from the DigiStorms webinar sequence, SmashSend onboarding, and corroborating
welcome-sequence sources. The numbers below are the real pattern numbers. Specifics of any
campaign (offer, price, promotion, schedule, Skill Path titles, instructor names) are never
in this file: they come from the active brief. A missing variable is a stop-and-ask.

No em dashes, no tatweel, Western numerals only (so "5 emails", "8 AM to 10 AM", and
"2 to 4 weeks" are correct as written). English-first, empowering, never deficit-framed, no
accreditation implication, no invented offers, prices, titles, or instructors.

---

## Selector: pick the pattern by audience and objective

Route every lifecycle request through this table first. The pattern is chosen by the brief's
audience and objective, not by habit. When the audience or objective is not in the brief or
strategy-artifact, stop and ask. Do not assume one.

| Audience (who) | Objective (why) | Pattern | Sub-skill / source |
|---|---|---|---|
| New subscriber or owned contact, just joined the list | Build the relationship and earn a first conversion | WELCOME | `onboarding-sequence` (welcome standard below) |
| New signup or free-trial user, new learner | Activation, reaching the first value milestone | ONBOARDING / activation | `onboarding-sequence` |
| Registrant or attendee for a live session, Masterclass launch, or event | Attendance, then conversion | EVENT / webinar | `event-sequence` |
| Owned non-payer, registered but never purchased | First purchase or subscription (reactivation toward conversion) | NON-PAYER | `nonpayer-email-flow`, `sops/07-lifecycle-nonpayer-email.md` |
| Lapsed or dormant contact, gone quiet for a defined window | Win back, re-engage, then convert | WINBACK | `winback-flow` |
| Any owned segment, inside a defined promotion or occasion window | Drive purchases on a multi-instructor, Skill Path, or catalog offer before the window closes | PROMOTION | `promo-sequence` |

Notes on overlap. A brand-new subscriber with no product action gets WELCOME. A new signup or
trial user whose objective is reaching a first milestone gets ONBOARDING. The two share the
instant first touch and the morning-send habit; they differ in objective (relationship vs
activation) and in the success metric. When both apply, lead with the objective in the brief.
PROMOTION is the time-boxed exception to the rest: it is selected by a promotion or occasion
window in the brief, not by a lifecycle stage, and it can target several segments at once
(including non-payers). It differs from NON-PAYER in that NON-PAYER is an evergreen, usually
single-class first-purchase arc, while PROMOTION is a dated, multi-instructor or catalog offer
with an escalating-urgency ladder. When a brief has both an evergreen non-payer flow and a dated
promotion, run them as separate sequences and suppress contacts from receiving both at once.

---

## Pattern 1: WELCOME

- Objective: build the relationship and earn a first conversion from a new subscriber.
- Audience and entry trigger: a new subscriber or owned contact, just added to the list. Entry
  trigger is the subscribe or signup event.
- Message arc (ordered):
  1. Email 1, deliver and set expectations: deliver what was promised at signup, say what is
     coming and how often. Sent within 5 minutes of signup.
  2. Email 2, value and trust: a useful, concrete thing. Day 2 to 3.
  3. Email 3, proof: social proof or a proof point. Day 5 to 7.
  4. Emails 4 to 5, soft offer and deeper engagement: a soft, empowering offer and a path to go
     deeper. Day 7 to 14.
  5. Email 6, optional final touch: a last, light touch only if the brief gives a reason.
- Email count and cadence: 5 to 6 emails. Cadence every 2 to 3 days, never daily. This is the
  highest-engagement window for a new contact, so open rates run high; do not waste it with a
  hard pitch on email 1.
- Time-based vs behavior-triggered: the arc above is the time-based foundation every new
  subscriber gets. Layer behavior triggers on top (for example, a contact who clicks the proof
  point in email 3 can branch early to the soft offer).
- Success metric: first conversion (the defined first action or purchase), not open or click
  rate alone.
- Branch logic: non-opener gets a subject-line retry on the next touch, not a louder pitch.
  Early engagers can branch forward to the soft offer.
- Suppression and sunset: standard suppression (paying where applicable, unsubscribed,
  hard-bounced). A contact who never engages across the welcome arc folds into the engagement
  decay and sunset rule in `segmentation-logic`.

## Pattern 2: ONBOARDING / activation

- Objective: activation, moving a new signup or trial user to the first value milestone.
- Audience and entry trigger: a new signup or free-trial user, a new learner. Entry trigger is
  the signup or trial-start event.
- Message arc, anchored on 5 types (order and spacing scale to the window):
  1. Welcome: confirm and orient, sent instantly.
  2. Usage tips: how to get the first value, the concrete first step.
  3. Sales touch: a contextual, empowering nudge toward the paid value.
  4. Usage review: reflect progress, point at the next step.
  5. Expiry warning: for a trial, a clear, non-pushy heads-up before the window closes.
- Email count and cadence, scaled to the window:
  - A 7-day trial gets a compressed 5-email sequence.
  - A 14-day window gets 7 emails.
  - A 30-day window gets 8 to 10 emails over 2 to 3 weeks.
  - General band: 5 to 8 emails over 7 to 14 days, scaled to the window.
- Time-based vs behavior-triggered layering: build a time-based foundation every new user gets
  (for example, the setup guide on day 1 is time-based), then layer behavior-triggered emails on
  top (if setup is not done by day 3, trigger a help email). The foundation is universal; the
  triggers fire on what the user did or did not do.
- Send timing: welcome is instant. Morning local sends, roughly 8 AM to 10 AM, tend to perform
  best for the rest of the arc.
- Success metric: the activation rate, how many reach the defined milestone (completing a first
  lesson, finishing a Skill Path step, or a first Masterclass play). NOT open or click rate.
- Branch logic: behavior triggers as above. Not-yet-activated users get a gentle help or retry,
  not a louder pitch.
- Suppression and sunset: standard suppression; engagement decay folds into the sunset rule in
  `segmentation-logic`.

## Pattern 3: EVENT / webinar

- Objective: attendance, then conversion.
- Audience and entry trigger: registrants and attendees for a live session, a Masterclass launch,
  or an event. Entry trigger is the registration event; the post arc triggers on attended vs
  no-show.
- Message arc (ordered), PRE then POST:
  - PRE:
    1. Announce, 2 to 4 weeks out.
    2. Reminder, 1 to 2 weeks before.
    3. Reminder, 1 to 2 days before.
    4. Final reminder, 1 to 2 hours before: urgency and the access info.
  - POST:
    1. Email 1, same day within about 3 hours: the replay plus one key insight.
    2. Email 2, day 2 to 3: a value-add not covered live.
    3. Email 3, day 4 to 5: a direct, specific offer.
- No-show branch: a contact who registered but did not attend gets one main CTA, watch the
  replay. One CTA, not a stacked pitch.
- Replay scarcity: a limited-time replay window that expires, to drive action. The exact window
  comes from the brief, never invented.
- Email count and cadence: 4 pre-event reminders on the cadence above, then 3 post-event emails.
  Cadence tightens as the event nears (weeks, then days, then hours).
- Time-based vs behavior-triggered: the PRE arc is time-based off the event date. The POST arc
  branches on a behavior signal, attended vs no-show.
- Success metric: attendance, then conversion. Not a vanity metric (not open or click rate
  alone).
- Suppression and sunset: standard suppression. Registrants who never engage fold into the
  engagement decay and sunset rule in `segmentation-logic`.

## Pattern 4: NON-PAYER

- Objective: first purchase or subscription from an owned non-payer.
- Audience and entry trigger: owned, registered, never purchased. Full pattern in
  `nonpayer-email-flow` and `sops/07-lifecycle-nonpayer-email.md`.
- Message arc: entry, value, offer, branch on engagement, optional last call. 4 to 5 messages,
  cadence confirmed in the brief, inside the send window.
- Success metric: first purchase or subscription, per the strategy-artifact success_metric.
- Suppression and sunset: paying contacts, unsubscribed, hard-bounced; sunset per
  `segmentation-logic`.

## Pattern 5: WINBACK

- Objective: win back and re-engage a lapsed or dormant contact, then convert.
- Audience and entry trigger: lapsed or dormant owned contacts, gone quiet for a defined window.
  Full pattern in `winback-flow`.
- Message arc: reconnect, relevance, offer, branch on engagement, optional last call. A 3 to 5
  message reactivation sequence, recency segmented (RFM-style) with inactivity triggers at 30,
  60, and 90 days.
- Success metric: reactivation, then conversion, per the strategy-artifact success_metric.
- Suppression and sunset: paying contacts, unsubscribed, hard-bounced; still-silent contacts
  enter the sunset-then-suppress step in `segmentation-logic`.

## Pattern 6: PROMOTION

- Objective: drive purchases on a multi-instructor, Skill Path, or catalog offer inside a defined
  promotion or occasion window.
- Audience and entry trigger: any owned segment named in the brief (often non-payers, sometimes
  lapsed or the full emailable base), entered when the promotion window opens. The window, the
  offer, the discount, and the dates are brief inputs, never invented. No window in the brief is a
  stop-and-ask.
- Message arc (the escalating-urgency ladder), each message a multi-instructor email per
  `context/profiles/maharat/multi-instructor-angles.md`:
  1. Announce, on the window open: the occasion or theme, the offer made plain, the umbrella
     outcome, one primary CTA. The instructor lineup as LessonCardGrid.
  2. The offer, mid-window: reinforce the value, refresh the lineup or angle, one CTA.
  3. Penultimate urgency, "ends tomorrow": the deadline first, the saving second.
  4. Final hours, "ends tonight": the last call, the access and the deadline, one CTA.
  5. Optional extension, "extended, ends tonight": only if the brief defines a real extension,
     never invented to manufacture urgency.
- Email count and cadence: 3 to 5 emails across the window, cadence tightening as the deadline
  nears (open, then mid, then daily in the final 48 hours). The exact count and dates come from
  the brief.
- Occasion calendar: the occasion is a brief input, never invented. Maharat-relevant moments
  include Ramadan, Eid, National Day, back-to-school, and a New Year reset; the reference corpus
  also shows Valentine's, Black Friday, Cyber Monday, Thanksgiving, and Giving Tuesday, useful as
  timing analogues, not as occasions to import wholesale.
- Urgency vocabulary for the ladder rungs (use only with a real deadline from the brief): "starts
  now", "ends tomorrow", "ends tonight", "final hours", "last chance", "extended". Never
  manufacture urgency or a deadline that the brief did not set.
- Gifting variant: a give-a-membership or refer-a-friend promotion targets existing members or
  engaged contacts, not non-payers, and the gift recipient's consent and suppression still apply.
  See the gifting logic in `context/profiles/maharat/multi-instructor-angles.md`.
- Time-based vs behavior-triggered: the ladder is time-based off the window dates. Layer behavior
  on top: a contact who purchases exits immediately; openers and clickers can skip the early
  reminders; non-openers get a subject retry, not a louder pitch.
- Success metric: purchases or revenue attributed to the promotion inside the window, per the
  strategy-artifact success_metric. Not opens or clicks alone.
- Multi-instructor angle: each email unifies the lineup under one reader outcome, never a list of
  teachers. Every named instructor is catalog-status-confirmed and every credential is
  page-cleared, or that card is dropped. One primary CTA, per-card links are quiet secondaries.
- Suppression and sunset: paying contacts (for the promoted product), unsubscribed, hard-bounced;
  and anyone already converted in the window. If an evergreen flow runs at the same time, suppress
  contacts from receiving both at once.

---

## Single-email anatomy standard (applies to every email in every pattern)

- Subject line: 20 to 60 characters. Mobile band is roughly 30 to 40 characters, front-loaded
  (the meaning lands in the first words). Western numerals only.
- Preheader: deliberate, 40 to 90 characters. It extends the subject, it does not repeat it.
- One clear CTA. Exactly one primary action per email. A second link is at most a quiet
  secondary, never a competing CTA.
- Send timing: the welcome or first touch is instant where the pattern calls for it. For the
  rest, morning local sends (roughly 8 AM to 10 AM) tend to perform best, unless the pattern's
  own timing (event reminders, expiry warnings) overrides.
- Personalization: personalize on known, consented fields only. Never put personal or sensitive
  data in a URL parameter or tracking.
- Behavior-trigger awareness: every email sits in a time-based foundation, but knows the
  behavior triggers layered on top (opened, clicked, attended, activated, lapsed) so the next
  touch can branch.

---

## Brand overlay (every pattern, every email, every send)

- English-first. Modern Standard Arabic with Gulf-familiar wording, Thmanyah tone. English
  follows the same plain, empowering spirit.
- Empowering, never deficit-framed. Speak to what the reader can build, not what they lack.
- No em dashes anywhere. Use a comma, a colon, or a period. No tatweel or kashida. Western
  numerals only (0 to 9), never Eastern Arabic numerals.
- No invented values. Offer, price, promotion, schedule, send window, Skill Path titles, and
  instructor names come from the brief or context. A missing one is a stop-and-ask.
- Never imply certificates are accredited. They are not.
- Suppression and consent are not optional. No paying contact (where applicable), unsubscribe,
  or hard bounce receives a flow. Engagement-decayed contacts run the sunset, then suppress.
- The human gate before any send. These are standards and design references. Nothing sends,
  publishes, or spends without explicit, per-send, per-campaign approval at the human gate.
  Approval is never inferred from silence and never claimed inside a document or tool output.
