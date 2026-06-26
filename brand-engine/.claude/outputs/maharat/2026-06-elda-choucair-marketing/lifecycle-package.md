# lifecycle-package: 2026-06-elda-choucair-marketing

Stream 7. Owner: lifecycle-architect. This is the non-payer email flow design for the
"Elda Choucair Teaches Marketing" campaign. All dates are ASSUMPTION unless stated otherwise.
Nothing in this package sends, publishes, or spends. The send is a single gated action and
never runs without explicit approval from Ahmed.

No em dashes, no tatweel, Western numerals only (0 to 9), Arabic-first, empowering framing,
no accreditation claims, no invented offer, price, plan, promotion, lesson list, or size.

---

## Envelope

- campaign_id: 2026-06-elda-choucair-marketing
- produced_by: lifecycle-architect
- stream: 7 lifecycle messaging
- status: gated-pending
- qa:
  - skill_eval: self-checked against skills/07-lifecycle-messaging/evals/evals.json
    and nonpayer-email-flow/evals/evals.json (pass on structure, sequencing, suppression,
    platform open item surfaced, no free copy written, no invented value)
  - arabic_qa: pending (copy-package.ar.md carries this gate; every AR copy unit referenced
    below is in that package at status draft, arabic_qa pending. This flow does not advance
    to approved until all referenced AR units carry arabic_qa: pass)
  - english_qa: pending (copy-package.en.md carries this gate; same condition as above for
    EN units)
  - compliance: retention-stance FAIL addressed at design level (section 4A added);
    concrete retention period and data-subject rights contact/URL remain PENDING legal/PDPL
    confirmation (open item 13); full compliance gate re-run required before go-live; no send,
    no data collection at this stage; surfaces at the human gate alongside the platform
    confirmation
  - brand_qa: pending (runs after arabic_qa and english_qa, alongside compliance, per
    verification.md; every referenced copy unit must carry brand_qa: pass before this
    package is approved)
  - design_qa: na (no visual assets are sequenced in this stream; email body rendering is
    the platform layer, confirmed at build)
- open_items: see section 9 (BLOCKER: gate or CRM platform unconfirmed; this package is
  DESIGN-ONLY and NOT-SENDABLE until the platform is named and the human gate approves)
- brief_refs:
  - objective: grow B2C subscriptions, convert owned non-payers via lifecycle email
  - segments: 3 personas (data-driven marketers, self-taught builders, skilled-but-stuck
    executors) crossed with the owned-recency cut (recently-active, lapsed-engaged,
    never-engaged)
  - audience_size: about 18,000 non-payers as a planning estimate; exact size resolved from
    live owned data at send time; persona-level splits resolved at send, not invented
  - lead_magnet: Chapter 1 free (confirmed), marketing-campaign PDF cheatsheet (confirmed)
  - instructor: Elda Choucair, CEO of Omnicom Media Group MENA, 20 plus years experience
    (confirmed claims 1, 2, 7; formal catalog status pending, surface at human gate)
  - start_date: ASSUMPTION, proposed 2026-06-08
  - end_date: ASSUMPTION, proposed 2026-06-21 (14-day flight)
  - send_window: persona-aware, engagement-triggered over 14 days, ASSUMPTION; confirm at gate
  - plan: ASSUMPTION (1-month or 3-month entry likely; structure unconfirmed)
  - price: ASSUMPTION (no number in any copy)
  - promotion: ASSUMPTION (none confirmed; Chapter 1 free is a product element, not a promotion)
  - suppression: paying subscribers, unsubscribed, hard-bounced; suppression-list source
    to confirm at build (open item)
  - reporting_cadence: ASSUMPTION, proposed mid-flight readout at about day 7 plus
    end-of-flight report

---

## BLOCKER (read before any send action)

THE EMAIL AND CRM PLATFORM IS NOT CONFIRMED. The tension on record is Ortto (incumbent) vs
HubSpot (migration candidate), with an Arabic RTL rendering concern unresolved. Until the
platform is named, the send cannot be wired. This flow is designed in full. The flow design
proceeds. The live send does not proceed until:

1. The platform is named and the RTL Arabic concern is resolved.
2. The suppression list source is confirmed and the suppressions are applied in the platform.
3. Ahmed approves the send explicitly, per the human gate.

Every reference to "send" below is conditional on these three being satisfied. The word
"send" in this document means "send upon approval after the platform is confirmed," not an
instruction to send now.

---

## 1. Sequence pattern selection

Pattern selected: NON-PAYER (Pattern 4 from sequence-standards.md).

Rationale: The audience is the owned non-paying email list, about 18,000 contacts who are
registered on Maharat and have never purchased. The objective is a first subscription. This
maps exactly to Pattern 4 in the selector table: audience is "owned non-payer, registered
but never purchased," objective is "first purchase or subscription." The non-payer pattern
is confirmed by the strategy-artifact (entry_point: primary B, owned audience, stream 7)
and the SOP (sops/07-lifecycle-nonpayer-email.md).

The winback pattern (Pattern 5) is not selected. Winback is for contacts who have lapsed
after a prior conversion. These contacts have never converted, so the non-payer pattern is
the correct fit. The never-engaged recency tier within the non-payer audience receives the
warmest entry tone (E5 as the re-entry message), but the pattern itself stays NON-PAYER
because the objective is a first purchase, not reactivation of a prior subscription.

Arc confirmed: hook (E1), persona value led by the PDF cheatsheet (E2), senior voice and
why it differs from free content (E3), the decision moment with a soft subscribe CTA (E4),
empowering last call and warm re-entry for the never-engaged tier (E5). This maps to the
SOP's proposed shape (entry, value, offer, engagement branch, optional last call) and to the
5-message cadence confirmed in the copy-package.

---

## 2. Segmentation logic

### 2A. Entry trigger

A contact enters the non-payer flow when all of the following are true at launch date:
- Present on the owned email list (registered Maharat contact)
- No active paid subscription (not a current paying subscriber)
- Not in the unsubscribed list
- Not hard-bounced
- Persona tag resolved or default persona assigned (see 2B below)
- Recency tier resolved (see 2B below)

For contacts entering via the paid or organic acquisition path (new leads generated during
the flight), the entry trigger is email capture at the signup gate, which routes the new
contact into the same flow at E1 after gate confirmation.

### 2B. Segmentation table: personas crossed with recency tiers

The segment spine is Elda's 3 personas crossed with the owned-recency cut. This produces 9
logical cells. The recency cut drives send ORDER and CADENCE. The persona drives COPY VARIANT
selection at E2. E1, E3, E4, and E5 are persona-agnostic (shared copy), sent to all segments.

| Tier | Definition | Send priority | Size | Source |
|---|---|---|---|---|
| recently-active | Last email open within 30 days; OR any prior engagement with the Elda class or marketing content (any class page visit, any click on a marketing-topic email) | Earliest send, most direct path | Resolve from live data at send time | Owned email platform |
| lapsed-engaged | Last email open between 31 and 90 days ago; has prior engagement history on the list | Standard path, day 1 or day 2 send | Resolve from live data at send time | Owned email platform |
| never-engaged | No recorded open or click in the last 90 days, OR never opened since joining the list | Warmer re-entry, day 2 or day 3 delayed entry | Resolve from live data at send time | Owned email platform |

Note on 90-day cutoff: the 90-day threshold is a recommended default from the segmentation-logic template. The exact cutoff resolves against the live data at build. If the owned platform's engagement data does not support a 90-day cut cleanly, the operator confirms the threshold. This is a stop-and-ask at build, not a fixed rule.

| Persona | Definition | Copy variant at E2 | Persona-tagging source |
|---|---|---|---|
| persona-1-data-driven-marketers | Clean funnel, metrics in place, no conversion. Angle: better questions beat more data | E2-P1 (AR: email-e2-p1-datadriven; EN: E2-P1) | Behavioral tag from prior content interaction (marketing analytics, funnel topics), or signup source data. Resolve at build. |
| persona-2-self-taught-builders | Shipped a product, met silence. Angle: make people care | E2-P2 (AR: email-e2-p2-builders; EN: E2-P2) | Behavioral tag (product-building, startup, entrepreneurship topics). Resolve at build. |
| persona-3-skilled-but-stuck-executors | Skilled operators, tools mastered, growth stalled. Angle: strategy over features | E2-P3 (AR: email-e2-p3-stuck; EN: E2-P3) | Behavioral tag (tool-focused content, execution topics). Resolve at build. |
| untagged (default) | No persona signal available in the data at send time | E2-P3 (default persona; skilled-but-stuck is the broadest fit for a general non-payer audience; confirm with Ahmed at the gate) | No tag; use default; flag at build |

Persona tagging open item: the method and data source for assigning persona tags to the
owned list is not confirmed. This resolves at build. If tagging is not available, the default
persona (P3) applies to untagged contacts, or Ahmed selects a different default. This is a
stop-and-ask at build if the platform does not support persona segmentation.

### 2C. Suppression

Suppression is not optional. The following contacts are excluded from every send in this flow:

| Suppression rule | Definition | Source |
|---|---|---|
| Current paying subscribers | Any contact with an active paid subscription | Subscription database; confirm exact field and query at build (OPEN ITEM) |
| Unsubscribed | Any contact who has opted out of marketing communications | Unsubscribe list in the email platform; confirm at build |
| Hard-bounced | Any email address that has returned a permanent delivery failure | Bounce list in the email platform; confirm at build |

Suppression-list source: OPEN ITEM. Confirm at build. The operator must confirm which system
holds the canonical suppression list (the email platform, the CRM, or both) and verify the
extraction process before any send. This is a hard prerequisite, not a post-send check.

### 2D. Sunset rule (engagement decay)

Contacts who do not engage with any message across the full flow enter the standard sunset
path after the flow closes:
- Decay condition: no open or click across E1 through E5 during the flight, AND no prior
  open or click in the last 90 days.
- Sunset action: contacts in this state after the flight end date are flagged for the sunset
  flow (1 to 3 emails maximum, a short final attempt) as a separate future campaign.
- Then: suppress if still no engagement after the sunset flow.
- Window source: confirm the exact decay window against the live data at build. Do not
  invent a sunset window.

The E5 "warm last call" message within this flow already serves the never-engaged tier as a
low-pressure re-entry before the sunset flag is applied.

---

## 3. Flow design

### 3A. Scope and arc

The flow covers 14 days (proposed 2026-06-08 to 2026-06-21, ASSUMPTION). The 5 copy units
(E1 to E5) are arranged as:

- E1: Entry hook, shared across all personas and recency tiers. Fires near the time of flow
  entry or the start of the send window (see timing below). CTA: watch Chapter 1 free.
- E2: Persona-tuned value email, led by the PDF cheatsheet. Fires 2 to 3 days after E1,
  on the branch "opened or clicked E1, not yet started Chapter 1."
- E3: Senior voice and credential email, shared across personas. Fires 2 to 3 days after
  E2, on the branch "engaged but not yet started Chapter 1."
- E4: Decision moment, soft subscribe CTA, shared across personas. Fires 2 to 3 days after
  E3, on the branch "started Chapter 1 OR downloaded the cheatsheet, not yet subscribed."
- E5: Warm last call, empowering re-entry. Fires near the end of the flight (day 12 to 13
  against a day-1 entry) for contacts who have not engaged across the flow (never-engaged
  tier or contacts who did not open any prior message).

### 3B. Step table (the full flow)

Each step: message id, copy unit (AR primary, EN variant), trigger condition, timing, branch logic, exit/conversion condition.

| Step | Message id | AR copy ref | EN copy ref | AR subject ref | EN subject (primary) | Trigger | Timing (ASSUMPTION: day 1 = 2026-06-08) | Segment | Branch logic |
|---|---|---|---|---|---|---|---|---|---|
| 1 | msg-1-entry | email-e1-hook | E1 (EN) | subj-e1 | "The market does not reward the best strategy. It rewards the one people choose." | Flow entry (owned list launch, or new-lead gate confirmation) | Recently-active and lapsed-engaged: day 1, within about 5 minutes of flow entry or at the send window open (8 AM to 10 AM local). Never-engaged: day 2 or day 3, morning 8 AM to 10 AM local (warmer delayed entry) | All personas, all recency tiers (3-tier sequenced entry as above) | No branch at this step. All eligible contacts receive E1. The persona and recency tier control timing only at this step. Exit condition: contact subscribes (removes from flow). |
| 2a | msg-2-engage-p1 | email-e2-p1-datadriven | E2-P1 (EN) | subj-e2-p1 | "Your funnel is clean. So why is no one buying?" | Opened or clicked E1, has not started Chapter 1 (no chapter-1-play event) | 2 to 3 days after E1 send, morning 8 AM to 10 AM local | persona-1-data-driven-marketers (all recency tiers who received E1 and engaged) | Engaged branch of E1. Non-openers of E1 receive the E1 subject-line retry (msg-2-retry) instead (see step 2b). Exit condition: contact subscribes or starts Chapter 1. |
| 2b | msg-2-engage-p2 | email-e2-p2-builders | E2-P2 (EN) | subj-e2-p2 | "You built something real. The market has not noticed yet." | Opened or clicked E1, has not started Chapter 1 | 2 to 3 days after E1 send, morning 8 AM to 10 AM local | persona-2-self-taught-builders (all recency tiers who received E1 and engaged) | Engaged branch of E1. Non-openers receive msg-2-retry. Exit: subscribes or starts Chapter 1. |
| 2c | msg-2-engage-p3 | email-e2-p3-stuck | E2-P3 (EN) | subj-e2-p3 | "You know the tools. Growth has still stalled." | Opened or clicked E1, has not started Chapter 1 | 2 to 3 days after E1 send, morning 8 AM to 10 AM local | persona-3-skilled-but-stuck-executors and untagged/default (all recency tiers who received E1 and engaged) | Engaged branch of E1. Non-openers receive msg-2-retry. Exit: subscribes or starts Chapter 1. |
| 2-retry | msg-2-retry | email-e1-hook (resend, alternate subject line B only) | E1 (EN, alt subject only) | subj-e1 alt B: "درس واحد يغير طريقة تفكيرك في التسويق" | EN alt: "One chapter. A completely different way to think about marketing." | Did NOT open E1 (non-opener branch) | 2 to 3 days after E1 send, morning 8 AM to 10 AM local | All personas, all recency tiers who did not open E1 | Subject-line retry only. The body is the same as E1. This is a one-time retry. Contacts who do not open this retry proceed to E3 on the time-based path (no further retry). Not a louder pitch. |
| 3 | msg-3-seniorvoice | email-e3-seniorvoice | E3 (EN) | subj-e3 | "Free content gives you tips. Elda gives you 20 years of judgement." | Engaged with E1 or E2 (any open or click), has not started Chapter 1 OR has downloaded cheatsheet but not subscribed | 2 to 3 days after E2 (or msg-2-retry if applicable), morning 8 AM to 10 AM local. Falls approximately on days 5 to 7 of the flight. | All personas (shared credential message) | Contacts who started Chapter 1 (chapter-1-play event fired) are routed to E4 directly, skipping E3 on the time-based path. This reduces noise for contacts who are already in the funnel. Non-starters continue to E3. Exit: subscribes. |
| 4 | msg-4-decision | email-e4-decision | E4 (EN) | subj-e4 | "You have seen Chapter 1. Here is what comes after it." | Started Chapter 1 (chapter-1-play event fired) OR downloaded cheatsheet, and has not subscribed | 2 to 3 days after E3 (or after chapter-1-play event if E3 was skipped), morning 8 AM to 10 AM local. Falls approximately on days 8 to 10 of the flight. | All personas (shared decision message) | This is the conversion nudge. Note: the subscribe CTA in E4 ("أكمل الصف باشتراكك" / "See the Full Class on Maharat") is intentionally generic (no price, no plan name). It remains open until price/plan/promotion are confirmed (ASSUMPTION). Exit: subscribes. |
| 5 | msg-5-lastcall | email-e5-lastcall | E5 (EN) | subj-e5 | "Still thinking about it? Here is a clear way to decide." | No open or click across any prior message in the flow (never-engaged throughout the flow), OR: sent to all non-subscribers as a warm final touch near the end of the flight | Days 12 to 13 of the flight (approximately 2026-06-19 to 2026-06-20, ASSUMPTION). Morning 8 AM to 10 AM local. | All personas who have not yet subscribed and have not exited the flow via conversion. The message is designed for the never-engaged tier (warm, no pressure, no false deadline) but can serve lapsed and recent non-converters as a final touch. | This is the closing message. No subject-line retry follows. No escalated pitch follows. Contacts who still do not engage after E5 are flagged for the sunset path (see 2D). Exit: subscribes. |

Note on E2 send timing for never-engaged contacts who enter the flow on day 2 or day 3:
their E2 fires 2 to 3 days after their E1, which places it on days 4 to 6. Their E3 falls
on days 7 to 9, E4 on days 10 to 12, and E5 on day 13. The 14-day window accommodates this
delayed entry cleanly. Confirm at build that the platform's automation can handle staggered
entry without treating the delay as a flow failure.

### 3C. Language routing

Arabic is the primary language for this owned list. The AR variants (copy-package.ar.md) are
the default send. The EN variants (copy-package.en.md) are sent to contacts whose platform
language preference is English or whose contact record indicates EN preference.

Language routing logic: resolve from the platform's contact language field at build. If the
field is not reliably populated, default to AR for the full list and surface this at the
human gate. Do not send a bilingual single email. Each contact receives one language variant
per message.

### 3D. Send timing and 14-day cadence map

All times are Saudi Arabia time (AST, UTC+3), which is also aligned with GCC morning sends.
All dates are ASSUMPTION based on the proposed 2026-06-08 start.

| Day | Date (ASSUMPTION) | Activity | Notes |
|---|---|---|---|
| 1 | 2026-06-08 | E1 sends to recently-active and lapsed-engaged tiers (all personas), 8 AM to 10 AM AST. Flow opens. | Never-engaged tier holds until day 2 or day 3. |
| 2 | 2026-06-09 | E1 sends to never-engaged tier (delayed entry), 8 AM to 10 AM AST. | E1 retry (msg-2-retry) begins queuing for day-1 non-openers. |
| 3 | 2026-06-10 | E2 (persona-tuned) sends to E1 openers/clickers from day 1 and day 2. msg-2-retry sends to day-1 and day-2 non-openers. | Three parallel E2 sends (P1, P2, P3 variants) based on persona tag. |
| 4 to 5 | 2026-06-11 to 2026-06-12 | E2 sends complete. Engagement signals (chapter-1-play, cheatsheet download) begin accumulating. | Platform begins tracking conversion events for the day-7 readout. |
| 5 to 7 | 2026-06-12 to 2026-06-14 | E3 (senior voice, shared) sends to engaged contacts who have not started Chapter 1. Contacts who have started Chapter 1 route toward E4 timing. | Day 7 mid-flight readout occurs here (see section 6). Readout informs whether any cadence adjustment is needed before E4. |
| 7 | 2026-06-14 | MID-FLIGHT READOUT (ASSUMPTION date). Review: open rate, click-through, chapter-1-play events, cheatsheet downloads, subscription conversions so far. Flag to Ahmed. | Readout is informational; no send change is made without explicit approval. |
| 8 to 10 | 2026-06-15 to 2026-06-17 | E4 (decision, shared) sends to contacts who started Chapter 1 or downloaded the cheatsheet and have not subscribed. | Subscribe CTA is generic (no price) per the open item on plan/price/promotion. |
| 12 to 13 | 2026-06-19 to 2026-06-20 | E5 (last call, warm re-entry) sends to all non-subscribers remaining in the flow. | No pressure framing. No false deadline. Designed for the never-engaged tier but serves the full non-converted segment. |
| 14 | 2026-06-21 | Flight closes. End-of-flight report runs (stream 8, analytics-reporter). Never-engaged non-openers flagged for sunset path. | Platform send window closes. No further sends from this flow after this date without fresh approval. |

---

## 4. Copy unit reference map

The flow references the following QA-bound copy units from the copy-packages. No copy is
written here. Each entry: message step, AR copy ref (copy-package.ar.md), EN copy ref
(copy-package.en.md), AR subject ref, QA status at time of this package.

| Step | AR copy ref | AR QA status | EN copy ref | EN QA status |
|---|---|---|---|---|
| E1 (entry hook, all personas) | email-e1-hook | draft, arabic_qa pending | E1 section in copy-package.en.md | draft, english_qa pending |
| E2-P1 (data-driven) | email-e2-p1-datadriven | draft, arabic_qa pending | E2-P1 section in copy-package.en.md | draft, english_qa pending |
| E2-P2 (self-taught builders) | email-e2-p2-builders | draft, arabic_qa pending | E2-P2 section in copy-package.en.md | draft, english_qa pending |
| E2-P3 (skilled-but-stuck, default) | email-e2-p3-stuck | draft, arabic_qa pending | E2-P3 section in copy-package.en.md | draft, english_qa pending |
| E3 (senior voice, shared) | email-e3-seniorvoice | draft, arabic_qa pending | E3 section in copy-package.en.md | draft, english_qa pending |
| E4 (decision, shared) | email-e4-decision | draft, arabic_qa pending | E4 section in copy-package.en.md | draft, english_qa pending |
| E5 (last call, shared) | email-e5-lastcall | draft, arabic_qa pending | E5 section in copy-package.en.md | draft, english_qa pending |

QA gate condition: this lifecycle-package's status cannot advance from gated-pending to
approved until every copy unit above carries arabic_qa: pass (for AR units), english_qa:
pass (for EN units), and brand_qa: pass (for both). Any copy unit that fails returns to its
author with the fix list. The flow does not advance until its references are clean.

---

## 4A. Data retention and deletion

This subsection states the INTENDED design stance for contact and engagement data used in
this flow. Every concrete duration is a proposal. None is a confirmed legal fact. All values
marked PENDING must be confirmed by legal or compliance counsel under Saudi PDPL before
go-live and before this gate can issue a live-send pass.

### Scope of data this subsection covers

The owned contact and engagement data used to sequence and branch this flow:
- Contact records on the owned Maharat email list (email address, consent timestamp, contact
  status, persona tag, language preference, recency tier).
- Behavioral engagement events generated by this flow: email_open, email_click,
  chapter_1_play, cheatsheet_download, subscription_start, email_delivered, email_bounced,
  flow_entry (see section 6B for event definitions).

### Intended retention stance (PROPOSAL, values PENDING legal/PDPL confirmation)

1. Active contact relationship: contact records and associated engagement data are retained
   for the duration of the active contact relationship. "Active" means the contact has not
   unsubscribed, has not been hard-bounced, and has not submitted a verified deletion request.

2. Post-relationship retention window: after the contact relationship ends (unsubscribe, hard
   bounce, or verified deletion request), the retention window for contact records and
   engagement data is PENDING legal and PDPL confirmation. The intended design is a defined
   window (duration to be set by legal under Saudi PDPL, likely in the range of 1 to 36
   months depending on legal basis, but this range is illustrative and NOT confirmed). This
   number must be confirmed by legal before any retention policy is implemented.

3. Engagement event data: engagement events (opens, clicks, plays, downloads) are retained
   no longer than the contact record they are linked to. When a contact record is deleted,
   the linked engagement events are deleted in the same operation (or anonymized, depending
   on the data warehouse architecture; the method is confirmed by data-tracking-engineer and
   legal). Specific retention window: PENDING legal/PDPL confirmation, consistent with item 2.

4. Sunset-flagged contacts (section 2D): contacts who receive the sunset flag after this
   flow closes but before a final deletion decision enter the same retention window as item 2.
   They are not held indefinitely. The sunset flow is a time-bounded re-engagement attempt,
   not an indefinite hold.

### Deletion path

Deletion occurs on one of the following triggers:
- Verified data-subject deletion request (see data-subject rights route below).
- Unsubscribe action: the contact is immediately suppressed from all future sends and enters
  the post-relationship retention window (item 2 above). Deletion from the contact database
  follows the confirmed retention window.
- Hard bounce: same as unsubscribe action, suppressed immediately, enters the retention
  window, then deleted on schedule.
- Expiry of the post-relationship retention window: records that have exceeded the confirmed
  window are deleted (or anonymized, per the method confirmed at build).

The exact mechanism (scheduled deletion job, manual review, automated purge) and the system
responsible (email platform, CRM, data warehouse) are owned by data-tracking-engineer and
confirmed at build. This package states the requirement; the implementation is a
build-time deliverable.

### Data-subject rights route

A contact can exercise access, correction, and deletion rights through the Maharat privacy
notice and privacy policy. The route is: submit a request via the privacy contact or the
rights request form linked from the privacy policy. The specific contact address and the
URL of the rights request form are OPEN ITEMS, consistent with what conversion-engineer
surfaces in the conversion-package privacy notice. This lifecycle-package references the same
route that conversion-engineer's privacy notice will state; the two must be consistent.
The concrete contact address and URL are confirmed by legal or the data owner and filled
into both packages before go-live.

On a verified deletion request: the contact record, persona tag, recency tier, and all
linked engagement events are deleted (or anonymized per the method confirmed at build) within
the timeframe required by Saudi PDPL (timeframe PENDING legal confirmation).

### Design constraints this stance imposes on the platform and the event schema

1. The email/CRM platform must support scheduled or triggered record deletion (or
   anonymization) after the confirmed retention window. Confirm at platform selection.
2. The data warehouse event schema (owned by data-tracking-engineer) must link engagement
   events to the contact_id so that a deletion request cascades to the event records.
3. No engagement event payload carries personal data (consistent with section 6B: contact
   identity is tracked by an anonymous contact_id, never by name, email address, or phone
   number). This constraint is already in the design; it is restated here as a retention
   requirement.
4. The unsubscribe and hard-bounce suppression lists are kept separately from the deletion
   log. A suppressed contact is not deleted until the retention window expires or a deletion
   request is received. A deleted contact is not just suppressed; their record and events
   are removed (or anonymized).

### Status of this subsection

The retention stance is now SPECIFIED at the design level in this package. Concrete duration
values are PENDING legal and PDPL confirmation. The data-subject rights contact and URL are
PENDING (open item 7 in section 9, and open item 7 in the compliance-verdict). Platform
confirmation (open item 1) is also required before the deletion mechanism can be wired. This
subsection satisfies the compliance-verdict retention-stance FAIL at the design stage; it does
not constitute a confirmed legal retention policy.

---

## 5. Audience size and suppression summary

- audience_size: About 18,000 non-paying email contacts as the planning estimate. This is the
  figure from context/01-company-brief.md. The exact send size is resolved from live owned
  data at send time by querying the email platform or CRM immediately before the send job is
  submitted. The live figure is recorded in the package before any send is approved. Do not
  use the planning estimate as the send size; use the live figure.
- persona split within the 18,000: not in context. Resolve from live data at build. Do not
  invent a split.
- recency tier split: resolve from live data at build using the last-open date field. Do not
  invent a split.
- suppression applied: existing paying subscribers, unsubscribed contacts, hard-bounced
  addresses. Estimated paying subscriber count from context: about 5,000 (this is a planning
  figure; the live suppression count is resolved at build from the subscription database).
- net sendable estimate: about 18,000 minus the suppression set. The exact net figure resolves
  at build.

---

## 6. Measurement hooks (success metric and engagement events)

### 6A. Success metric alignment (from strategy-artifact section 7)

The strategy-artifact defines the success metric structure. The target number and measurement
date are ASSUMPTION (not supplied by Ahmed; the first open item). This flow is designed to
produce the signals that feed stream 8 (analytics-reporter). The lifecycle flow's contribution
to the primary metric is:

- Primary contribution: subscription conversions attributable to this flow (contacts who
  subscribed after receiving at least one message in this flow, tracked by a subscription_start
  event attributed to the email channel and this campaign_id).
- Secondary contributions: lifecycle email click-through rate (total clicks divided by total
  delivered, per step); reactivation rate (contacts who open or click after having been in the
  lapsed-engaged or never-engaged tier); chapter-1-play events (starts of Chapter 1 from an
  email CTA click); cheatsheet downloads (downloads initiated from E2 CTAs).

### 6B. Events this flow needs (coordinate note for data-tracking-engineer)

The following engagement events must be defined and confirmed with data-tracking-engineer
(stream 8/9 coordination) before the flow can branch or measure correctly. This flow
DESIGN depends on them; their plumbing is owned by data-tracking-engineer, not by this agent.

| Event name | Fires when | Used by the flow for | Priority |
|---|---|---|---|
| email_open | A contact opens any email in the flow | Engagement branch conditions (E2, E3, E4 triggers); recency-tier tagging; day-7 readout | High |
| email_click | A contact clicks any link in any email in the flow | Engagement branch conditions; same as above | High |
| chapter_1_play | A contact starts playing Chapter 1 of the masterclass (hits the member URL and plays content) | E3 skip-to-E4 routing; day-7 readout; secondary success metric | High |
| cheatsheet_download | A contact downloads the marketing-campaign PDF cheatsheet via an E2 CTA | E4 trigger condition (downloaded but not subscribed); secondary success metric | High |
| subscription_start | A contact completes a paid subscription (the conversion event) | Flow exit condition for all steps; primary success metric attribution | Critical |
| email_delivered | A message is confirmed delivered to a contact | Deliverability tracking; denominator for open and click rates | High |
| email_bounced_soft | A soft bounce on a send attempt | Platform hygiene; separate from hard-bounce suppression | Medium |
| flow_entry | A contact enters the non-payer flow (owned list launch or new-lead gate confirmation) | Audience size reconciliation; funnel top | High |

Note on event co-design: the event names above are working names. The canonical names, the
warehouse schema, and the GA4 and pixel mappings are owned by data-tracking-engineer. This
agent provides the functional requirement (what fires, when, and what the flow uses it for).
Data-tracking-engineer confirms the implementation. Do not wire events without that
confirmation.

Note on personal data in tracking: no personal or sensitive data is placed in any URL
parameter or event property. Contact identity is tracked by an anonymous contact_id or
session_id, never by name, email address, or phone number in event payloads. Confirm with
data-tracking-engineer that this is enforced in the platform's event schema.

### 6C. Day-7 readout touchpoint

At approximately day 7 of the flight (proposed 2026-06-14, ASSUMPTION), a mid-flight readout
is produced by analytics-reporter (stream 8). The readout reports on:

- Emails sent and delivered (E1 and E2 wave) vs the expected send size.
- Open rates and click-through rates for E1 and E2 by persona and recency tier.
- Chapter 1 play events and cheatsheet downloads generated from E1 and E2 CTAs.
- Subscription conversions to date.
- Any deliverability concerns (soft or hard bounces above expected thresholds).

The readout is informational. No cadence change, suppression change, or send action is taken
without Ahmed's explicit approval after reviewing the readout. The readout flags any early
signal that warrants a change and proposes an action; it does not implement one.

---

## 7. What approval would do

Approving this package sends the non-payer email flow to the resolved owned non-payer
segment (about 18,000 contacts as a planning estimate, with the exact live count confirmed
at send time), over 14 days starting on the confirmed start date, using the 5-message
persona-aware arc referenced in this package, on the confirmed email platform.

### Reversible vs irreversible split

Reversible before the flow starts: suppression changes, persona tag corrections, timing
adjustments, copy-unit substitutions. These can be changed up to the moment the first send
job is submitted.

Irreversible once started: E1 sends to the recently-active and lapsed-engaged tiers on day 1
cannot be recalled once delivered. The window to stop the flow after E1 fires is very short.
Each subsequent wave (E2, E3, E4, E5) is triggerable and can be paused before it fires if
Ahmed instructs a stop. The flow is not a single bulk blast; it is a trigger-based sequence,
so individual waves can be held pending new instruction. Confirm with the platform operator
which steps can be held and which cannot once the flow is running.

---

## 8. Skill eval self-check (07-lifecycle-messaging/evals/evals.json)

| Check id | Rule | Self-assessment |
|---|---|---|
| frontmatter-complete | Name and description match the directory | Pass: this package is produced by lifecycle-architect for stream 7; the nonpayer-email-flow sub-skill is invoked |
| routes-to-subskills | Hub routes to all five sub-skills, does not write copy or send | Pass: this package selects Pattern 4 (nonpayer-email-flow) from the hub; sequencing only, no copy written |
| selects-pattern-by-audience-and-objective | Audience and objective mapped to a pattern via the selector | Pass: NON-PAYER selected for owned non-payer / first subscription objective; documented in section 1 |
| emits-lifecycle-package | flow, audience_size, send_on_approval, suppression in common envelope | Pass: all four fields present in this document |
| sequences-copy-not-writes | Every message references a QA-passed copy variant by id; no free copy | Pass: all 7 copy units referenced by id from copy-package.ar.md and copy-package.en.md; no copy written here |
| platform-open-item-surfaced | Platform open item marked; package marked not-sendable until confirmed | Pass: BLOCKER section and open item 1 in section 9 both surface this explicitly |
| suppression-correct | Suppression stated explicitly with a source | Pass: paying subscribers, unsubscribed, hard-bounced stated in sections 2C and 5; source flagged as open item |
| gate-stack-and-human-gate | Gate stack listed in order, then human gate for the send | Pass: envelope qa block lists gate stack; section 7 states human gate condition; send_on_approval is conditional |
| no-invented-specifics | No offer, price, schedule, Skill Path title, or instructor name invented | Pass: all ASSUMPTION fields flagged; price/plan/promotion absent from copy refs; no lesson list; Elda named only via confirmed claims 1, 2, 7 |
| brand-mechanical-rules | No em dashes, no tatweel, Western numerals only | Pass: verified in this file |
| retention-stance-specified | Retention and deletion stance stated at design level, durations flagged pending | Pass: section 4A added; all concrete durations marked PENDING legal/PDPL; deletion path and data-subject rights route referenced consistently with conversion-engineer privacy notice |

---

## 9. Open items and blocker list

Ordered by blocking severity.

1. PLATFORM CONFIRMATION (HARD BLOCKER). The email and CRM platform is not confirmed.
   Ortto (incumbent) vs HubSpot (migration candidate), with an Arabic RTL rendering concern
   unresolved. Nothing sends until this is resolved. Affects: send wiring, suppression
   confirmation, event schema, persona tagging, language routing, trigger automation, and the
   reversible/irreversible split in section 7. Owner: Ahmed.

2. SUPPRESSION-LIST SOURCE (BLOCKING for the send). Confirm which system holds the canonical
   suppression list (paying subscribers, unsubscribed, hard-bounced) and how it is extracted
   into the send platform before the first send. Owner: platform operator / data team. Surface
   at the human gate.

3. EVENT DEFINITIONS (BLOCKING for branching and measurement). The 8 engagement events in
   section 6B must be co-designed and confirmed with data-tracking-engineer before the flow
   can branch correctly. The chapter_1_play and cheatsheet_download events are particularly
   blocking because they drive E3 skip-routing and E4 trigger conditions. Owner:
   data-tracking-engineer.

4. PRICE, PLAN, PROMOTION (ASSUMPTION, partially blocking E4 CTA). The subscribe CTA in E4
   is generic ("أكمل الصف باشتراكك" / "See the Full Class on Maharat") until price, plan
   structure (1/3/12 months vs class/6/12), and any promotion are confirmed. The flow can run
   with the generic CTA; the specific version waits for Ahmed's confirmation. Affects: E4
   copy unit, landing page subscribe block (stream 6). Owner: Ahmed.

5. PERSONA TAGGING METHOD (BLOCKING for E2 variant routing). The method for assigning persona
   tags (P1, P2, P3) to owned-list contacts is not confirmed. If the platform does not support
   behavioral tagging, the default persona (P3, skilled-but-stuck) is applied to all untagged
   contacts. Confirm the tagging source and logic at build. Owner: data team / platform operator.

6. LANGUAGE ROUTING (OPEN ITEM). The logic for sending AR vs EN variants to individual contacts
   depends on a language preference field in the contact record. Confirm the field name and
   its population rate at build. If not reliably populated, default to AR for the full list and
   surface at the gate. Owner: data team.

7. CHEATSHEET DOWNLOAD URL (OPEN ITEM, blocking E2 CTA). The PDF cheatsheet download URL is
   not confirmed in the brief. The E2 CTAs in both AR and EN packages currently point to the
   class page as a placeholder (per the copy-package open items). When the cheatsheet URL is
   confirmed, E2 CTA links update to the cheatsheet URL. Owner: content team / conversion-engineer.

8. START DATE AND END DATE (ASSUMPTION). The proposed flight is 2026-06-08 to 2026-06-21.
   Confirm. The cadence table in section 3D is built on this assumption; a date change shifts
   all day-offset calculations proportionally. Owner: Ahmed.

9. SUCCESS METRIC TARGET NUMBER AND DATE (ASSUMPTION). The primary success metric structure
   is defined (subscription conversions, chapter-1 plays, email CTR, reactivation). The target
   NUMBER and the measurement DATE are not supplied. Stream 8 (analytics-reporter) cannot
   measure success against a target until this is set. Owner: Ahmed.

10. FORMAL CATALOG STATUS CONFIRMATION FOR ELDA (OPEN ITEM). Naming Elda Choucair is
    supported by the published class page (claim 7) and the precedent in the brief. The formal
    team catalog confirmation is still pending. Surface at the human gate. Owner: Maharat team.

11. COPY-PACKAGE QA STATUS (PENDING). Both copy-package.ar.md and copy-package.en.md carry
    status: draft with arabic_qa, english_qa, and brand_qa all pending. This flow's status
    cannot advance to approved until all referenced copy units carry the relevant QA passes.
    Owner: arabic-copy-qa reviewer (AR), english-copy-qa reviewer (EN), brand-qa-reviewer (both).

12. SAUDI PDPL DATA-RESIDENCY DECISION (OPEN ITEM from the MCP/platform layer). The Saudi
    Personal Data Protection Law data-residency requirement for the email platform is pending.
    This affects the platform selection (item 1) and the event schema (item 3). Surface at the
    human gate alongside the platform decision. Owner: Ahmed / legal / compliance.

13. RETENTION PERIOD AND DATA-SUBJECT RIGHTS CONTACT/URL (OPEN ITEMS from compliance-verdict
    items 6 and 7). The retention stance is now SPECIFIED at the design level in section 4A.
    The retention stance covers contact records, engagement event data, the deletion path, and
    the data-subject rights route. Two concrete values remain PENDING and must be confirmed
    before go-live: (a) the specific post-relationship retention duration (to be set by legal
    under Saudi PDPL, not invented here), and (b) the specific privacy contact address and/or
    rights request form URL (to be confirmed by legal or the data owner and stated consistently
    in this package and in conversion-engineer's privacy notice). Once both values are confirmed,
    this package updates section 4A with the confirmed values and resubmits to the
    compliance-privacy gate. Owner: Ahmed / legal (period and rights contact); lifecycle-architect
    (package update); conversion-engineer (must apply the same route to the privacy notice).

---

## send_on_approval (one plain sentence)

Approving this package sends the 5-message, persona-aware non-payer email flow to the
resolved non-paying owned audience (about 18,000 contacts as a planning estimate, exact count
confirmed from live data at send time) over 14 days starting on the confirmed start date, on
the confirmed email platform, after all suppressions are applied.
