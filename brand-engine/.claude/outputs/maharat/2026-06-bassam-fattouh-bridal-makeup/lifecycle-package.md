# lifecycle-package: Bassam Fattouh bridal makeup, non-payer lifecycle

v2 update notes: regenerated through the upgraded engine (2026-06-03). Changes from v1: (1)
flow now references v2 copy variant ids with preheader and mobile-subject refs explicitly
noted per message; (2) segmentation-logic block upgraded with the sunset rule and
engagement-decay suppression from the updated segmentation-logic skill (decay condition,
1 to 3 sunset messages, then suppress, framed as deliverability plus PDPL and consent
hygiene); (3) winback branch added for beauty-interested-lapsed and dormant-nonpayers, per
the new winback-flow sub-skill, proportionate to those segments and kept inside the existing
copy branch rather than adding net-new messages (the v2 copy-package already carries the
winback posture in email-nonpayer-m4-nonopener for these segments); (4) send and engagement
events updated with explicit revenue events (purchase and subscription_start) and event_id
dedup as the conversion signal the success_metric depends on, coordinated with
data-tracking-engineer, to-wire and gated; (5) suppression source, consent basis, PDPL,
and data-flow disclosure carried as explicit open items; (6) package remains NOT SENDABLE:
the email and WhatsApp vendor is still an OPEN ITEM and Saudi PDPL data-residency is pending,
even though the platform slot is adopted in settings.json. Post-v2 compliance fix (2026-06-03):
two new BLOCKING SEND open items added in response to the upgraded compliance gate FAIL verdict
(checks 8 and 9): retention-stance (open item 18) and data-subject-rights (open item 19).
Package resubmitted to compliance-privacy-reviewer.

Stream 7 artifact. Produced by lifecycle-architect from the qa-passed strategy-artifact and
the v2 draft copy-package (Arabic email copy and subject lines from copywriter-ar). The flow
sequences copy variants by id. No copy is written here. Nothing sends.

No em dashes, no tatweel, Western numerals only, Arabic-first, empowering framing, no
accreditation claims.

---

## Common envelope

- campaign_id: 2026-06-bassam-fattouh-bridal-makeup
- produced_by: lifecycle-architect
- stream: 7 lifecycle messaging
- status: draft (design-only, NOT SENDABLE: gate platform vendor unconfirmed, Saudi PDPL
  data-residency pending, copy-package compliance and brand_qa gates still pending; status
  advances to qa-passed only after all gates below clear and blocking open items are resolved)
- qa:
  - skill_eval: pass (07-lifecycle-messaging hub checks, nonpayer-email-flow sub-skill checks,
    segmentation-logic checks including sunset rule and engagement-decay suppression, and
    winback-flow sub-skill checks applied; all pass)
  - arabic_qa: na (this artifact is the flow structure, not customer copy; referenced copy
    variants carry their own arabic_qa result from the copy-package; v2 copy-package arabic_qa
    self-check is pass per copy-package envelope)
  - english_qa: na
  - design_qa: na (no visual asset in this package; approved imagery is open item 8 from the
    strategy-artifact)
  - compliance: fail-pending-rereview (compliance-privacy-reviewer returned a FAIL on
    2026-06-02 on three checks: suppression-correct, pdpl-residency-surfaced, and
    data-flows-disclosed. A second upgraded-gate FAIL was returned on 2026-06-03 on two
    additional checks: retention-stance (check 8) and data-subject-rights (check 9). All
    five fix items are now carried in this package in the open_items below and in the Data
    and compliance section. Package resubmitted to compliance-privacy-reviewer for a re-run
    of all 10 checks. The send remains blocked until compliance-privacy-reviewer issues a
    pass verdict.)
  - brand_qa: pass (flow structure file checked against v2: no em dash glyph, no tatweel,
    Western numerals only, no invented offer or instructor name, no accreditation claim,
    empowering framing throughout, v2 preheader refs and mobile-subject refs are structural
    pointers only, no new copy written here)
- open_items:
  1. BLOCKING SEND: Gate platform vendor not confirmed (brief section 5, OPEN ITEM). The
     email and WhatsApp sending platform vendor is not named. The platform slot is adopted in
     settings.json and .mcp.json, but the concrete vendor and the EMAIL_WHATSAPP_API_KEY
     credential are unfilled. All send wiring is blocked. Design proceeds. The package is
     design-only and not-sendable until the vendor is confirmed and Ahmed approves. See
     references/2026-06-email-whatsapp-platform-research.md.
  2. BLOCKING SEND: Copy-package status is draft, not qa-passed. The v2 copy-package from
     copywriter-ar has compliance: pending and brand_qa: pending. The lifecycle-package
     references those variants and cannot advance to qa-passed until the copy-package carries
     qa-passed status on all required gates. Routes back to copywriter-ar for formal
     arabic-copy-qa, compliance-privacy-reviewer, and brand-qa-reviewer gates.
  3. BLOCKING SEND: Suppression source not confirmed (brief section 3, compliance check
     suppression-correct). The suppression groups are correctly defined (paying subscribers,
     unsubscribed contacts, hard-bounced addresses). The data source for all three groups is
     not yet confirmed. Suppression cannot be verified as applied until the source is named and
     the list is built. Tied to open item 13 (Saudi PDPL and data-residency): the platform
     decision cannot be made until PDPL is answered. Both route to Ahmed at the human gate.
  4. BLOCKING SEND: Saudi PDPL and data-residency requirement unconfirmed (compliance check
     pdpl-residency-surfaced). Audience is GCC, primary Saudi Arabia. Whether Saudi data
     residency is a hard requirement under the Saudi PDPL is unresolved, per
     context/04-tools-and-access.md. Must be answered before the platform vendor is selected
     and before any send goes out. If data residency is a hard requirement, a Saudi-residency
     bulk sending provider such as Unifonic may be required. Routes to Ahmed at the human gate.
  5. BLOCKING SEND: Data-flow disclosure incomplete (compliance check data-flows-disclosed).
     Until the sending platform vendor is confirmed (open item 1), the data-flow disclosure
     cannot be confirmed complete. Once the platform is named, this package will be updated to
     list the platform receiving contact data, the data fields transmitted (email address and
     engagement signals), and the events fired with their destination. Explicitly flagged as
     unresolved for the human gate.
  6. BLOCKING SEND: Revenue event and event_id dedup not wired (to-wire, gated). The
     purchase and subscription_start revenue events, and the event_id dedup required for
     conversion attribution and success_metric measurement, are named and co-noted with
     data-tracking-engineer but are not wired. Wire depends on the platform vendor (open item
     1) and the conversion page (stream 6). No revenue event fires until both are confirmed
     and Ahmed approves.
  7. Price and currency not confirmed (brief section 4, ASSUMPTION). Message 3 copy carries
     a marked placeholder slot [PRICE / PLACEHOLDER from brief]. No number is in the flow.
     Blocks any send that must show a price. Confirm with Ahmed before send.
  8. Plan not confirmed (1-month or 3-month entry, brief section 4, ASSUMPTION). Message 3
     copy carries a slot [PLAN if named from brief]. Flow references the offer as a Maharat
     subscription without naming the plan. Confirm before send.
  9. Promotion not confirmed (trial, first-time discount, or bundle, brief section 4,
     ASSUMPTION). Message 3 copy carries a slot [PROMO if any from brief]. None invented.
     If absent at send, the slot line is removed cleanly. Confirm before send.
  10. Schedule not confirmed (start_date, end_date, send_window, brief section 6, ASSUMPTION).
      The proposed cadence is a 4-message primary flow over about 2 weeks, triggered by entry
      and by engagement, with the winback branch inside the existing message 4 non-opener
      variant. Confirm with Ahmed before send. No date appears in any copy.
  11. Audience segment sizes below the about 18,000 total are planning splits, not confirmed
      counts. Each segment resolves from live data at send time and is recorded in the final
      package before the send.
  12. Sunset window to resolve against live data and confirmed brief. The decay condition
      (no open or click in roughly 90 to 180 days, or 3 to 4 flow attempts) and the
      1 to 3 sunset message count are set by the segmentation-logic rule. The exact window
      boundary resolves against the brief and the data at send; it is not invented here.
  13. Winback segment sizes resolve at send. The beauty-interested-lapsed and dormant-nonpayers
      recency splits are planning-only. Exact counts come from live data.
  14. Success-metric target not confirmed (brief section 2, ASSUMPTION). The proposed primary
      metric is subscription conversion rate from the flow, now grounded in the
      subscription_start revenue event and event_id dedup (open item 6). The numeric target is
      not set. Ahmed confirms the target at the human gate.
  15. Content lineup not confirmed (brief section 4). No lesson count, module, or duration is
      stated anywhere in the flow or referenced copy. Copy leads with the artist and the craft
      only. If any asset in a later build needs a specific, it must come from the brief.
  16. Approved imagery not confirmed (brief section 7, ASSUMPTION). This package is text-only.
      If a visual is added at build it must be a real, rights-cleared supplied asset, never
      generated. Confirm with Maharat before stream 3 runs.
  17. Consent basis to confirm at send. The consent basis for emailing owned non-paying contacts
      must be confirmed (opt-in, legitimate interest, or other lawful basis under Saudi PDPL and
      applicable GCC law) before the send proceeds. This is tied to open items 4 and 3. Routes
      to Ahmed and the compliance-privacy-reviewer.
  18. BLOCKING SEND: Retention and deletion stance not confirmed. How long contact data
      (email address, engagement signals, and revenue event data) is kept and when it is
      deleted has not been confirmed. Saudi PDPL and GDPR both require that personal data not
      be retained beyond the period necessary for the purpose for which it was collected. A
      retention period and a deletion path must be confirmed before any send proceeds. This
      package does not set the period. Routes to Ahmed at the human gate for a decision.
  19. BLOCKING SEND: Data-subject rights route not confirmed. The route by which a contact
      can request access to, correction of, or deletion of the data held about them under
      the Saudi PDPL has not been confirmed or documented. Saudi PDPL grants data subjects
      these rights, and a process to receive and action such requests must be in place before
      any send proceeds. This package does not stand up the process. Routes to Ahmed at the
      human gate for a decision.
- brief_refs:
  - entry_point: owned audience (brief section 2)
  - objective: convert non-paying contacts to paying subscribers, Bassam Fattouh bridal
    makeup Masterclass as the hook (brief section 2)
  - product: Masterclass "Bassam Fattouh Teaches Bridal Makeup" (brief section 4)
  - instructor: Bassam Fattouh, confirmed via the published Maharat course page (brief
    section 4), naming allowed in copy for this class
  - audience: owned non-paying email contacts, GCC, primary Saudi Arabia (brief section 3)
  - audience_size: about 18,000 non-paying contacts, planning estimate (brief section 3)
  - channels: email primary, WhatsApp out of scope here (brief section 5)
  - signup_gate: email, conversion to a paid plan (brief section 5)
  - gate_platform: OPEN ITEM, vendor not confirmed (brief section 5)
  - budget: n/a, owned audience, zero media cost (brief section 6)
  - send_window: ASSUMPTION, proposed 4-message primary flow over about 2 weeks (brief
    section 6)
  - start_date: ASSUMPTION, not confirmed (brief section 6)
  - end_date: ASSUMPTION, not confirmed (brief section 6)
  - price: ASSUMPTION, not confirmed (brief section 4)
  - plan: ASSUMPTION, not confirmed (brief section 4)
  - promotion: ASSUMPTION, not confirmed (brief section 4)
  - suppression_source: to confirm (brief section 3)
  - consent_basis: to confirm (PDPL and applicable GCC law)
  - constraints: owned only, no paid build, RTL-correct Arabic, no accreditation, real
    Masterclass title only, no invented lineup (brief section 8)

---

## Envelope validation log

Inbound artifact checks before design began:

### strategy-artifact (v2)
- campaign_id: 2026-06-bassam-fattouh-bridal-makeup. Match: pass.
- produced_by: strategy-lead. Expected producer: pass.
- status: qa-passed. Meets the qa-passed threshold required to cross the boundary: pass.
- Required body fields present: segments (4 defined with JTBD job stories), angle,
  offer_framing (with competitive alternative), channel_plan, success_metric (with proposed
  numeric target flagged ASSUMPTION). Pass.
- open_items read and accounted for: 11 open items carried from the v2 strategy-artifact,
  all reflected in this package's open_items above. Pass.
- Verdict: valid. The v2 strategy-artifact may be consumed.

### copy-package (v2)
- campaign_id: 2026-06-bassam-fattouh-bridal-makeup. Match: pass.
- produced_by: copywriter-ar. Expected producer: pass.
- status: draft. Below the qa-passed threshold. Flag raised (open item 2 above).
- skill_eval: pass. arabic_qa: pass (self-applied on v2, including preheader, mobile-subject,
  and framework checks; formal gate pending). compliance: pending. brand_qa: pending.
- v2 changes confirmed present: deliberate preheaders on every message in the 40 to 90
  character band, mobile-tuned subjects toward the 30 to 40 character band with key word
  front-loaded inside the first 30, frameworks applied per funnel stage, winback posture on
  email-nonpayer-m4-nonopener for beauty-interested-lapsed and dormant-nonpayers.
- Required variant ids present for all 4 flow messages plus the engagement branch:
  email-nonpayer-m1-entry, email-nonpayer-m2-proof, email-nonpayer-m3-offer,
  email-nonpayer-m4-nonopener, email-nonpayer-m4-engaged. All 5 variants and all 6 subject
  line blocks (subj-nonpayer-m1, subj-nonpayer-m2, subj-nonpayer-m3, subj-nonpayer-m4-nonopener,
  subj-nonpayer-m4-engaged) present, each with a preheader and primary subject. Pass.
- Verdict: variant ids are present and the flow can be designed against them. The
  lifecycle-package is blocked from advancing to qa-passed status until the copy-package
  reaches qa-passed. The flow design proceeds; the send is blocked.

---

## Body

### Segmentation logic (upgraded, including sunset rule and engagement-decay suppression)

Entry trigger: the contact is in the owned non-paying email list, has not started a paid plan,
has not unsubscribed, and has not hard-bounced. The contact may enter the flow only from the
point the send is approved by Ahmed, not before. Consent basis must be confirmed before entry
(open item 17).

Segments (from v2 strategy-artifact, sizes resolve from live data at send time):

```
segment:     beauty-interested-engaged
definition:  Non-paying contacts with beauty, makeup, or design-and-style interest signal
             (browsed or opened beauty content, or carry a beauty interest tag) and who
             have opened or clicked an email within about the last 90 days.
size:        Resolve from live data at send time (planning split of the about 18,000 estimate).
priority:    Primary. Warmest fit and reachable now. Receives the full 4-message flow.
winback:     Not in scope for the winback branch. These contacts are currently engaged.
```

```
segment:     beauty-interested-lapsed
definition:  Non-paying contacts with the same beauty or design-and-style interest signal,
             but whose last open or click was more than about 90 days ago.
size:        Resolve from live data at send time (planning split of the about 18,000 estimate).
priority:    Secondary. Strong interest fit, lower inbox reach. Enters at message 1 with a
             re-engagement posture. Receives the winback branch at message 4 via the
             email-nonpayer-m4-nonopener variant, which carries the winback posture for
             this segment per the v2 copy-package winback_note.
winback:     YES. This segment enters the winback branch at message 4. The winback posture
             (warm, low-pressure, leads with the draw of the class before any offer) is
             embedded in copy-package/email-nonpayer-m4-nonopener per the v2 winback_note.
             Segment routing to that variant is the trigger-logic call resolved at send.
```

```
segment:     general-engaged-nonpayers
definition:  Non-paying contacts with no specific beauty interest signal, but who have opened
             or clicked an email within about the last 90 days.
size:        Resolve from live data at send time (planning split of the about 18,000 estimate).
priority:    Secondary. Reachable and active. The angle broadens from bridal to learning a
             real skill from a leading expert. Enters at message 1 and receives the offer at
             message 3 and the engagement branch at message 4.
winback:     Not in scope for the winback branch in this flow. These contacts are currently
             engaged. If they exit without converting they enter the sunset rule.
```

```
segment:     dormant-nonpayers
definition:  Non-paying contacts with no recent open or click beyond about 90 days and no
             specific beauty interest signal.
size:        Resolve from live data at send time (planning split of the about 18,000 estimate).
priority:    Lowest. Light re-engagement only via the message 4 non-opener variant, which also
             carries the winback posture for this segment per the v2 copy-package winback_note.
             Heavy sends to this segment risk deliverability for the whole list.
             Does not receive messages 1, 2, or 3 in the primary flow.
winback:     YES. This segment enters the winback branch at message 4 (email-nonpayer-m4-nonopener).
             The winback posture (light, low-pressure, no price or promotion) is embedded in
             that variant for this segment. Contacts still silent after message 4 enter the
             sunset rule immediately.
```

Engagement branch conditions:

```
branch:      engaged (opener or clicker)
condition:   The contact opened or clicked any message in the flow (message 1, 2, or 3).
action:      Receives email-nonpayer-m4-engaged. Stronger close toward the subscription.
```

```
branch:      non-opener or winback
condition:   The contact did not open message 3 within the engagement window (proposed: 3
             days after message 3 sends, confirm against the confirmed send window).
             For beauty-interested-lapsed and dormant-nonpayers this branch carries the
             winback posture. For all other non-openers it carries the subject-line retry.
             Segment routing within this branch resolves from live data at send time.
action:      Receives email-nonpayer-m4-nonopener. Subject-line retry with a lighter nudge
             and, for the lapsed and dormant segments, the winback re-engagement posture.
             Not a louder pitch. Not a pressure close.
```

Inter-message timing (proposed cadence, ASSUMPTION, confirm with Ahmed per brief section 6):

```
message 1 to message 2:  Day 3 after message 1 sends (3-day delay)
message 2 to message 3:  Day 4 after message 2 sends (4-day delay, cumulative day 7)
message 3 to message 4:  Day 4 after message 3 sends (4-day delay, cumulative day 11)
total window:            About 11 to 14 days across the full flow
```

Note: these timing figures derive from the v2 strategy-artifact proposed cadence of about
2 weeks for 4 messages. They are an ASSUMPTION until Ahmed confirms the schedule (open item
10). No date appears in any copy. The engagement window for the message 4 branch is proposed
at 3 days after message 3 sends and is likewise an ASSUMPTION.

Suppression set:

```
exclude:     All contacts who have started a paid Maharat plan (paying subscribers, about
             5,000 per context/01-company-brief.md planning estimate).
exclude:     All contacts who have unsubscribed from Maharat email.
exclude:     All contacts with a hard-bounced email address.
source:      To confirm before send (open item 3). The suppression data source must be named
             and the list built before any send goes out. Suppression is not optional. Tied to
             open item 4 (Saudi PDPL and data-residency).
apply:       Before audience sizing. Audience size resolves after suppression is applied.
```

Sunset rule and engagement-decay suppression (not optional, upgraded):

```
sunset_rule:
  decay_condition: A contact who has not opened or clicked in roughly 90 to 180 days, OR who
                   has gone through 3 to 4 flow attempts across campaigns without re-engaging,
                   enters the sunset flow. For dormant-nonpayers who arrive at this flow
                   already beyond the 90-day threshold, the message 4 non-opener variant is
                   effectively the start of their sunset sequence.
  sunset_flow:     1 to 3 emails (no more than 3), a short final attempt. Copy for sunset
                   messages is not in the current copy-package and must be commissioned from
                   copywriter-ar before a standalone sunset send. For this campaign the
                   dormant-nonpayers message 4 non-opener is a proportionate equivalent for
                   the first sunset touch; a second and third would require new copy.
  then:            Suppress. A contact who completes the sunset flow without re-engaging is
                   suppressed from the owned list. Suppression is applied before any future send.
  window_source:   Resolve the 90 to 180 day window against the confirmed brief schedule and
                   the live last-open or last-click data at send time. Do not invent the
                   window boundary (open item 12).
  rationale:       Sunsetting protects sender reputation and deliverability by removing
                   chronically non-engaged addresses from active sends. It also keeps the list
                   to contacts who have demonstrated recent consent through engagement, which
                   is sound PDPL and consent hygiene under Saudi and GCC data law. A smaller,
                   engaged list is a healthier and more compliant list.
```

---

### flow

The ordered messages. Each message references a copy variant from the v2 copy-package by id.
No copy is written here. The copy variants are from the copy-package produced by copywriter-ar.
Every message now also carries a preheader_ref and mobile_subject_note, reflecting the v2
copy-package additions.

Note on copy-package status: the v2 copy-package is currently draft. The status of referenced
variants reflects that the skill eval and arabic_qa self-check (including v2 preheader,
mobile-subject, and framework checks) have passed, and that formal arabic-copy-qa,
compliance-privacy-reviewer, and brand-qa-reviewer gates are pending. The flow is designed
against the variant ids; the referenced copy carries the gate results once those gates clear.

```
id:              msg-1-entry
trigger:         Contact enters the non-payer flow (approved send date, from brief once
                 confirmed). Eligible segments: beauty-interested-engaged,
                 beauty-interested-lapsed, general-engaged-nonpayers.
                 (dormant-nonpayers do not receive this message in the primary flow.)
segment:         beauty-interested-engaged (primary), beauty-interested-lapsed (secondary),
                 general-engaged-nonpayers (secondary)
channel:         email
copy_ref:        copy-package/email-nonpayer-m1-entry
subject_ref:     copy-package/subj-nonpayer-m1
                 primary subject: "إطلالة عروس تصنعينها بنفسك مع بسام فتوح"
                 mobile_subject_note: 38 characters, in the 30 to 40 band, key word
                 "إطلالة عروس" front-loaded inside the first 30
preheader_ref:   copy-package/subj-nonpayer-m1 preheader field
                 preheader: "بسام فتوح يشرح فن مكياج العرائس خطوة بخطوة على مهارات، وأنت من يصنع الإطلالة"
                 (set deliberately in the 40 to 90 character band per v2 copy-package spec)
framework_note:  AIDA, opened with a 4 Us useful and ultra-specific lead line (v2 copy-package)
purpose:         Lead with what the reader can create. The angle, one clear CTA. No pressure,
                 no deficit framing. Establishes the Bassam Fattouh bridal makeup Masterclass
                 as the draw.
delay:           Entry trigger. No prior message in the flow.
```

```
id:              msg-2-proof
trigger:         3 days after msg-1 sends, regardless of open status (all segments who received
                 msg-1 and have not converted).
segment:         beauty-interested-engaged, beauty-interested-lapsed, general-engaged-nonpayers
channel:         email
copy_ref:        copy-package/email-nonpayer-m2-proof
subject_ref:     copy-package/subj-nonpayer-m2
                 primary subject: "تعلمي إطلالة العروس من فنان مكياج رائد"
                 mobile_subject_note: 37 characters, in the 30 to 40 band, key words
                 "تعلمي" and "إطلالة العروس" inside the first 30
preheader_ref:   copy-package/subj-nonpayer-m2 preheader field
                 preheader: "ترين كيف يفكر فنان محترف، وكيف يبني إطلالة عروس متكاملة تبقى مهارتها معك"
                 (set deliberately in the 40 to 90 character band per v2 copy-package spec)
framework_note:  AIDA interest and desire, 4 Us unique and credible on the proof line (v2)
purpose:         Concrete proof point: the artist's craft and how learning it is a real,
                 usable skill. Reinforces the angle. Confirmed instructor name and real
                 Masterclass title only; no invented lesson count, duration, or client names.
delay:           Day 3 after msg-1.
```

```
id:              msg-3-offer
trigger:         4 days after msg-2 sends (cumulative day 7 after entry), for all segments
                 who received msg-2 and have not converted.
segment:         beauty-interested-engaged, beauty-interested-lapsed, general-engaged-nonpayers
channel:         email
copy_ref:        copy-package/email-nonpayer-m3-offer
subject_ref:     copy-package/subj-nonpayer-m3
                 primary subject: "ابدئي اشتراكك وتعلمي بلا توقف على مهارات"
                 mobile_subject_note: 38 characters, in the 30 to 40 band, key word
                 "ابدئي اشتراكك" inside the first 30, front-loaded
preheader_ref:   copy-package/subj-nonpayer-m3 preheader field
                 preheader: "خطة واحدة تفتح لك تعلما متواصلا من خبراء المنطقة، والماستر كلاس بدايتك"
                 (set deliberately in the 40 to 90 character band per v2 copy-package spec)
framework_note:  AIDA action, 4 Cs final pass for a clear single offer line (v2)
purpose:         The offer made plain. Subscription to Maharat as the path beyond the one
                 class. Price slot [PRICE / PLACEHOLDER from brief], plan slot [PLAN if named
                 from brief], and promotion slot [PROMO if any from brief] are all left as
                 copy-package placeholders to be filled from confirmed brief values before
                 send. One CTA. No invented discount, no invented plan name.
delay:           Day 4 after msg-2 (cumulative day 7 after entry).
note:            This message carries the three unconfirmed slots. Before the send the slots
                 must be resolved from the confirmed brief values (open items 7, 8, 9). If no
                 promotion exists, the slot line is removed cleanly from the copy.
```

```
id:              msg-4-branch
trigger:         4 days after msg-3 sends (cumulative day 11 after entry), branching on
                 engagement and segment.
segment:         See branch rules below.
channel:         email
branch_engaged:
  condition:       Contact opened or clicked any message in the flow (msg-1, msg-2, or msg-3).
  segment:         beauty-interested-engaged, general-engaged-nonpayers (primary engaged pool)
  copy_ref:        copy-package/email-nonpayer-m4-engaged
  subject_ref:     copy-package/subj-nonpayer-m4-engaged
                   primary subject: "آخر دعوة لتبدئي رحلتك مع مهارات"
                   mobile_subject_note: 30 characters, at the band floor, key word "آخر دعوة"
                   front-loaded inside the first 30
  preheader_ref:   copy-package/subj-nonpayer-m4-engaged preheader field
                   preheader: "اشتراك واحد يمنحك الماستر كلاس وتعلما متواصلا، وخطوتك الأخيرة تبدأ اليوم"
                   (set deliberately in the 40 to 90 character band per v2 copy-package spec)
  framework_note:  AIDA action close, 4 Cs final pass, compelling and concise (v2)
  purpose:         Stronger close toward the subscription for contacts who have shown interest
                   but have not yet converted. Empowering, not pressuring.
branch_nonopener_and_winback:
  condition:       Contact did not open msg-3 within 3 days of its send (non-openers). Also
                   the winback entry point for beauty-interested-lapsed and dormant-nonpayers
                   contacts in the flow regardless of open status.
  segment:         beauty-interested-lapsed (winback), dormant-nonpayers (winback), and
                   any non-opener from the primary segments
  copy_ref:        copy-package/email-nonpayer-m4-nonopener
  subject_ref:     copy-package/subj-nonpayer-m4-nonopener
                   primary subject: "ما زالت إطلالة العروس بانتظارك"
                   mobile_subject_note: 29 characters, deliberately just under the band for
                   a soft winback line per v2 copy-package spec
  preheader_ref:   copy-package/subj-nonpayer-m4-nonopener preheader field
                   preheader: "ماستر كلاس بسام فتوح لمكياج العرائس ما زال متاحا وقت ما تجهزين، بلا ضغط"
                   (set deliberately in the 40 to 90 character band per v2 copy-package spec)
  framework_note:  PAS without shame, winback posture (v2). Problem named as life getting
                   busy, never as the contact's fault.
  winback_note:    For beauty-interested-lapsed and dormant-nonpayers this is the winback and
                   reactivation touch per the winback-flow sub-skill. It leads with the draw
                   of the class and the artist to earn the re-open before any offer, and keeps
                   a light, low-pressure posture (no price, no promotion, one soft CTA only)
                   so a dormant contact is not pushed further away. Segment routing within this
                   branch (lapsed vs dormant vs general non-opener) resolves from live data at
                   send time; the copy handles all three with a single warm, low-pressure line.
  purpose:         Subject-line retry with a light nudge. Not a louder pitch. Normalizes a
                   missed email without shame or deficit framing.
delay:           Day 4 after msg-3 (cumulative day 11 after entry).
post_flow:       Contacts who receive msg-4-branch and still do not open or click enter the
                 sunset rule. See sunset_rule in the segmentation logic block above.
                 Dormant-nonpayers who remain silent after this message enter suppress
                 immediately (they have already met the decay condition on arrival).
```

Optional message 5 (last call): NOT included. The brief does not confirm a send window end
date or a real reason for a final-call message. Per SOP 07 and the brief, a message 5 is
included only if the brief defines a window and a real reason. Until Ahmed confirms a window
and a reason, this message does not exist in the flow. If confirmed, it would require a new
copy variant from copywriter-ar and a new subject line and preheader before being added.

Winback branch proportionality note: the winback branch is kept proportionate to the segments
it serves (beauty-interested-lapsed and dormant-nonpayers). It is embedded inside the existing
message 4 non-opener variant, not a separate flow or additional messages, because the v2
copy-package already delivers the winback posture in email-nonpayer-m4-nonopener with a
winback_note specifically for these segments. This avoids flow bloat and is consistent with
the winback-flow sub-skill guidance that the lapsed base is a real channel treated with the
same care as the non-payer flow, with a proportionate sequence.

---

### Send and engagement events (co-designed with data-tracking-engineer)

The data-tracking-engineer owns the event and warehouse plumbing. This section names the
events the lifecycle flow depends on, including the revenue events and event_id dedup added
in v2. They are co-noted here so the data-tracking-engineer can design the event schema.
All events below are to-wire and gated: they depend on the platform vendor (open item 1)
and the conversion page (stream 6), and they do not fire until both are confirmed and Ahmed
approves.

The conversion signal for the success_metric (subscription conversion rate from the flow)
depends on the subscription_start revenue event with event_id dedup. Without that event
wired, the primary metric cannot be measured. This is a hard dependency on open item 6.

```
event:           email_send
fires:           When each message in the flow is dispatched to a contact.
used_by:         Audience-size confirmation per message, deliverability monitoring.
owner:           data-tracking-engineer (platform-level, to-wire once platform vendor named).
status:          to-wire, gated.
```

```
event:           email_open
fires:           When a contact opens any message in the flow.
used_by:         Engagement branch condition for msg-4 (opened triggers the engaged branch;
                 not opened within the engagement window triggers the non-opener branch).
owner:           data-tracking-engineer.
note:            Open tracking depends on image pixel loading and may undercount on Apple
                 Mail Privacy Protection. Click is the more reliable engagement signal.
                 Confirm with data-tracking-engineer at build.
status:          to-wire, gated.
```

```
event:           email_click
fires:           When a contact clicks the CTA in any message.
used_by:         Engagement branch condition for msg-4 (click is the stronger and more
                 reliable signal). Leading indicator for the success metric (click-through
                 rate). Revenue event attribution chain starts with click.
owner:           data-tracking-engineer.
status:          to-wire, gated.
```

```
event:           masterclass_play (or page_view on the Masterclass page)
fires:           When a contact plays the Masterclass or views its page after clicking through.
used_by:         Leading indicator for the success metric (Masterclass plays). Confirms the
                 hook is working. Sits between email_click and subscription_start in the
                 attribution chain.
owner:           data-tracking-engineer. Confirm event name and trigger point with
                 data-tracking-engineer and with the conversion-engineer who owns the
                 destination page (stream 6).
status:          to-wire, gated.
```

```
event:           purchase
fires:           When a contact completes a paid transaction (single-class purchase, if
                 applicable per the confirmed plan structure).
used_by:         Conversion attribution to the specific message and segment. Maps to Meta
                 Purchase and GA4 purchase per the tracking-package (stream 6 and 8).
owner:           data-tracking-engineer and conversion-engineer (stream 6).
event_id_dedup:  Required. Any purchase event sent by both platform pixel and CAPI must carry
                 one shared, non-identifying event_id so Meta deduplicates it and no
                 double-counting occurs. The event_id must not contain personal or sensitive
                 data (no email address, no contact id). Schema owned by data-tracking-engineer.
status:          to-wire, gated. Depends on platform vendor (open item 1) and conversion page
                 (stream 6).
```

```
event:           subscription_start
fires:           When a contact completes a paid subscription start after clicking through
                 the flow. This is the PRIMARY CONVERSION SIGNAL for the success_metric
                 (subscription conversion rate from the flow).
used_by:         Primary success metric measurement. Attribution back to the specific message,
                 segment, and the entry point of the flow. This is the revenue event the
                 lifecycle-package success depends on.
owner:           data-tracking-engineer and conversion-engineer (stream 6). The event and
                 attribution logic must be co-designed with both. Confirm at build, once the
                 platform vendor and the conversion page are confirmed.
event_id_dedup:  Required. Same dedup rule as the purchase event: one shared, non-identifying
                 event_id per event sent by both pixel and CAPI. No personal or sensitive data
                 in the event_id. This is the dedup that the success_metric measurement
                 depends on to avoid double-counting conversions. Schema owned by
                 data-tracking-engineer.
status:          to-wire, gated. Hard dependency on open item 6 (BLOCKING SEND for metric
                 measurement). Blocks meaningful success_metric reporting until wired.
note:            Without this event wired and deduplicated, the primary metric (subscription
                 conversion rate from the flow) cannot be measured accurately. All reported
                 conversion figures before this event is wired are incomplete.
```

Note: all event definitions, final event names, warehouse queries, pixel and CAPI mapping,
and GA4 mapping belong to the data-tracking-engineer (tracking-package, streams 6 and 8).
The event names above are working names for the co-design. The final schema is the
data-tracking-engineer's artifact.

---

### audience_size

```
audience_size: About 18,000 non-paying contacts as the planning estimate. Exact figure
               resolved from live owned-audience data at send time, after suppression is
               applied (paying contacts excluded, unsubscribed excluded, hard-bounced
               excluded). Segment-level sizes (beauty-interested-engaged,
               beauty-interested-lapsed, general-engaged-nonpayers, dormant-nonpayers)
               also resolve from live data at send time and are recorded in the final
               package before the send.
               Suppression source must be confirmed before sizing (open item 3).
               Consent basis must be confirmed before entry (open item 17).
```

---

### send_on_approval

Sends a 4-message Arabic email flow (with a winback branch at message 4 for the lapsed and
dormant segments) to the resolved non-payer segment (about 18,000 contacts as the planning
estimate, exact figure at send) over about 2 weeks, starting on the confirmed start date,
after Ahmed's explicit approval of this package and after all open items blocking the send
are resolved.

---

### suppression

```
suppression:
  - group: paying subscribers
    reason: They are already paying customers. The flow is for non-payers only.
    estimated_size: about 5,000 (planning estimate; confirmed count at send)
    source: to confirm. BLOCKING SEND open item 3. The suppression data source must be
            named and the list built before any send goes out. Tied to open item 4
            (Saudi PDPL and data-residency): the platform vendor decision cannot be made
            until the PDPL residency question is answered by Ahmed.
  - group: unsubscribed contacts
    reason: They have opted out of Maharat email. Sending to them is non-compliant.
    source: to confirm. BLOCKING SEND open item 3 (same dependency as above).
  - group: hard-bounced addresses
    reason: The address is invalid. Sending to hard bounces damages deliverability.
    source: to confirm. BLOCKING SEND open item 3 (same dependency as above).
  - group: sunset-suppressed contacts
    reason: Contacts who have completed a prior sunset flow without re-engaging have been
            suppressed. They must not re-enter this or any flow until suppression is reviewed
            and a new lawful consent basis is established. This is a deliverability and PDPL
            hygiene rule, not optional.
    source: Maintained by data-tracking-engineer in the owned-audience data layer. Source
            to confirm alongside the main suppression source (open item 3).
  apply: All four groups are excluded before audience sizing and before any send.
         Suppression is not optional. No contact in these groups receives any message
         in this flow. Source confirmation (open item 3) and PDPL resolution (open item 4)
         are both required before the suppression list can be verified as built.
```

---

### Data and compliance

This section was first added on 2026-06-02 in response to the compliance-privacy-reviewer
FAIL verdict (three checks: suppression-correct, pdpl-residency-surfaced, data-flows-disclosed).
Updated in v2 to add consent basis and data-flow disclosure for the new revenue events and
event_id dedup. The flow, the copy refs, and the suppression groups are unchanged from v1.
Four compliance items remain open and BLOCKING SEND.

#### Suppression source (compliance check: suppression-correct)

Status: BLOCKING SEND. Open item 3.

The suppression groups are correctly defined: paying subscribers, unsubscribed contacts,
hard-bounced addresses, and sunset-suppressed contacts. None of the four groups is changed.
The data source for all groups is not yet confirmed. The suppression list cannot be verified
as built and applied until the source is named. Tied to open item 4 (PDPL and data-residency).
Both route to Ahmed at the human gate.

#### Saudi PDPL and data-residency requirement (compliance check: pdpl-residency-surfaced)

Status: BLOCKING SEND. Open item 4.

The audience is GCC, primary Saudi Arabia. Whether Saudi data residency is a hard requirement
under the Saudi PDPL is unresolved, per context/04-tools-and-access.md. Must be answered
before the platform vendor is selected and before any send goes out. If data residency is a
hard requirement, a Saudi-residency bulk sending provider such as Unifonic may be required.
This package does not guess the answer. Routes to Ahmed at the human gate.

#### Consent basis (compliance check: consent basis under Saudi PDPL and GCC law)

Status: BLOCKING SEND. Open item 17.

The consent basis for emailing owned non-paying contacts must be confirmed before any send
proceeds. Saudi PDPL requires a lawful basis for processing and for sending commercial
communications. Whether the owned list was collected under opt-in, legitimate interest, or
another lawful basis is not stated in the brief and must be confirmed. This routes to Ahmed
and the compliance-privacy-reviewer at the human gate.

#### Data-flow disclosure (compliance check: data-flows-disclosed)

Status: BLOCKING SEND. Open item 5.

Until the sending platform vendor is confirmed (open item 1), the data-flow disclosure cannot
be confirmed complete. Once the platform is named, this package will be updated to list: the
platform vendor receiving contact data for the send, the data fields transmitted (email address
and engagement signals), the events fired (email_send, email_open, email_click, masterclass_play,
purchase, subscription_start) and their destination, and the event_id dedup schema. The v2 revenue
events (purchase, subscription_start) and event_id dedup are named above but their data-flow
disclosure is also incomplete until the platform and the tracking-package are wired. The
compliance-privacy-reviewer will rerun the data-flows-disclosed check at that point.

#### Retention and deletion stance (compliance check: retention-stance)

Status: BLOCKING SEND. Open item 18.

How long contact data (email address, engagement signals, and revenue event data) is kept
and when it is deleted has not been confirmed. Saudi PDPL requires that personal data not
be retained beyond the period necessary for the purpose for which it was collected. GDPR
imposes the same storage-limitation principle. A retention period and a deletion path must
be confirmed and documented before any send proceeds. This package does not set the period
and does not specify the deletion path. The question is routed to Ahmed at the human gate.
The compliance-privacy-reviewer will re-run check 8 once the stance is confirmed and recorded.

#### Data-subject rights route (compliance check: data-subject-rights)

Status: BLOCKING SEND. Open item 19.

The route by which a contact can request access to, correction of, or deletion of the data
held about them under the Saudi PDPL has not been confirmed or documented. Saudi PDPL grants
data subjects these rights. A process to receive and action such requests must be in place
before any send proceeds. This package does not stand up that process. The question is routed
to Ahmed at the human gate. The compliance-privacy-reviewer will re-run check 9 once the
route is confirmed and documented.

---

## Skill eval results (07-lifecycle-messaging, v2)

Checks applied against the hub SKILL.md evals and the nonpayer-email-flow, segmentation-logic,
and winback-flow sub-skill evals before this package was assembled.

```
check:                   frontmatter-complete
result:                  pass (hub, nonpayer-email-flow, segmentation-logic, and winback-flow
                          SKILL.md files have correct frontmatter)

check:                   routes-to-subskills
result:                  pass (hub routes through segmentation-logic, nonpayer-email-flow, and
                          winback-flow; flow design follows all three sub-skills)

check:                   emits-lifecycle-package
result:                  pass (this package has flow, audience_size, send_on_approval,
                          suppression wrapped in the common envelope)

check:                   sequences-copy-not-writes
result:                  pass (every message references a v2 copy-package variant id with
                          explicit preheader_ref and mobile_subject_note; no copy is written
                          in this file)

check:                   platform-open-item-surfaced
result:                  pass (open item 1 above; package marked not-sendable; vendor
                          unconfirmed even though platform slot is adopted in settings)

check:                   suppression-correct
result:                  pass (paying, unsubscribed, hard-bounced, and sunset-suppressed
                          excluded; stated explicitly; source flagged as to-confirm BLOCKING SEND)

check:                   sunset-rule-present
result:                  pass (decay condition, 1 to 3 sunset messages, then suppress,
                          window to resolve against brief and data, rationale stated as
                          deliverability plus PDPL and consent hygiene)

check:                   engagement-decay-suppression
result:                  pass (contacts who complete the flow without re-engaging enter the
                          sunset rule; dormant-nonpayers enter suppress immediately after msg-4
                          if still silent, as they already meet the decay condition on arrival)

check:                   winback-branch-present
result:                  pass (winback branch added at msg-4 for beauty-interested-lapsed and
                          dormant-nonpayers, using email-nonpayer-m4-nonopener with the v2
                          winback posture, kept proportionate inside the existing branch
                          rather than adding net-new messages)

check:                   gate-stack-and-human-gate
result:                  pass (gate stack: skill eval, arabic-copy-qa on copy-package,
                          brand-qa-reviewer, compliance-privacy-reviewer, then human gate for
                          the send, per verification.md)

check:                   no-invented-specifics
result:                  pass (no price, promotion, plan name, lesson count, duration, or
                          instructor name beyond the confirmed Bassam Fattouh from the brief;
                          no sunset window number invented; no segment sizes invented;
                          missing variables flagged in open_items, not guessed)

check:                   brand-mechanical-rules
result:                  pass (no em dash glyph, no tatweel, Western numerals only across
                          this file; any Arabic in the file is empowering and RTL-safe;
                          grep for em dash character confirmed clean)

check:                   revenue-events-and-dedup (v2)
result:                  pass (purchase and subscription_start revenue events named and
                          co-noted with data-tracking-engineer; event_id dedup requirement
                          stated for both; all to-wire and gated; success_metric dependency
                          on subscription_start stated explicitly; open item 6 blocks metric
                          measurement until wired)

check:                   ordered-flow-fields (nonpayer-email-flow sub-skill)
result:                  pass (each message has id, trigger, segment, channel, copy_ref,
                          subject_ref, preheader_ref, mobile_subject_note)

check:                   references-copy-by-id-not-writes (nonpayer-email-flow sub-skill)
result:                  pass

check:                   offer-traces-to-brief (nonpayer-email-flow sub-skill)
result:                  pass (offer, price slots, promotion slot, and plan slot all trace to
                          the brief; nothing invented)

check:                   audience-size-resolved-at-send (nonpayer-email-flow sub-skill)
result:                  pass

check:                   send-on-approval-sentence (nonpayer-email-flow sub-skill)
result:                  pass

check:                   suppression-correct (nonpayer-email-flow sub-skill)
result:                  pass

check:                   platform-open-item-not-sendable (nonpayer-email-flow sub-skill)
result:                  pass

check:                   winback-recency-segments (winback-flow sub-skill)
result:                  pass (beauty-interested-lapsed and dormant-nonpayers treated as the
                          recency-based lapsed segments; sizes resolve at send; thresholds
                          are the 90-day patterns from the strategy-artifact, not invented)

check:                   winback-sunset-step (winback-flow sub-skill)
result:                  pass (contacts silent through the winback branch enter the
                          sunset-then-suppress step; stated in the flow)

check:                   winback-proportionate (winback-flow sub-skill)
result:                  pass (winback is embedded inside the existing msg-4 non-opener
                          variant, not a separate flow or additional messages; proportionate
                          to the segments it serves)

check:                   pdpl-and-consent-surfaced (v2)
result:                  pass (Saudi PDPL data-residency open item 4, consent basis open item
                          17, and data-flow disclosure open item 5 all surfaced explicitly
                          and marked BLOCKING SEND)
```

All skill eval checks: pass.

---

## Pre-handoff checklist

- 07-lifecycle-messaging skill eval (v2): pass (all checks above including sunset rule,
  winback-flow, revenue events, and PDPL and consent items)
- Referenced copy variants QA status: copy-package v2 arabic_qa self-check pass (including
  v2 preheader, mobile-subject, and framework checks); formal arabic-copy-qa, compliance,
  and brand_qa gates pending (open item 2). Package cannot advance to qa-passed until the
  copy-package clears all gates.
- Compliance gate: fail-pending-rereview. Three original fix items from the 2026-06-02
  FAIL verdict carried forward. v2 adds consent basis as a fourth compliance open item.
  Post-v2 upgraded gate FAIL (2026-06-03) adds two further items: retention-stance
  (open item 18, BLOCKING SEND) and data-subject-rights (open item 19, BLOCKING SEND).
  All items are carried in the open_items block and the Data and compliance section.
  Package resubmitted to compliance-privacy-reviewer for a re-run of all 10 checks.
  Send remains blocked until a pass verdict is issued.
- Envelope complete: yes
- Status: draft, design-only, NOT SENDABLE (blocking open items: platform vendor unconfirmed,
  copy gates pending, suppression source unconfirmed, Saudi PDPL unresolved, consent basis
  unconfirmed, data-flow disclosure incomplete, revenue events not wired; see open items 1,
  2, 3, 4, 5, 6)
- brief_refs list every variable used: yes (above)
- Audience size resolved or flagged: flagged for resolution at send, planning estimate noted
- Suppression set and stated: yes (paying, unsubscribed, hard-bounced, sunset-suppressed;
  groups correct, source to confirm, open item 3, tied to PDPL open item 4)
- Sunset rule present: yes (decay condition, 1 to 3 sunset messages, then suppress,
  rationale stated as deliverability plus PDPL and consent hygiene)
- Winback branch present: yes (msg-4 non-opener branch for beauty-interested-lapsed and
  dormant-nonpayers, proportionate, using v2 copy-package winback posture)
- Revenue events and event_id dedup: named and co-noted with data-tracking-engineer; to-wire
  and gated; success_metric dependency stated; open item 6
- Send-platform open item surfaced: yes (open item 1, vendor unconfirmed, live send blocked)
- Saudi PDPL and data-residency open item surfaced: yes (open item 4, routes to Ahmed)
- Consent basis open item surfaced: yes (open item 17, routes to Ahmed and compliance)
- Data-flow disclosure status surfaced: yes (open item 5, incomplete until platform named)
- No invented offer, price, schedule, title, or size: confirmed
- Brand rules clean: no em dash glyph, no tatweel, Western numerals only, empowering framing,
  no accreditation claims
- Emits to: human gate, after all blocking open items are resolved and after Ahmed's explicit
  approval per send. Nothing sends on silence.
