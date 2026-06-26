# Measurement Plan: Bassam Fattouh Teaches Makeup, full funnel

## Envelope

- campaign_id: 2026-06-bassam-fattouh-makeup
- produced_by: analytics-reporter
- stream: 8 performance monitoring and 9 reporting and learning
- status: draft
- qa:
  - skill_eval: passed (structure and completeness reviewed against the strategy-artifact)
  - arabic_qa: na (this artifact is internal, no customer-facing copy)
  - brand_qa: na (internal artifact)
- open_items:
  - success_metric target number: flagged ASSUMPTION in the strategy-artifact and the brief.
    The metric definition is confirmed (subscription conversions attributable to the campaign).
    The target number must be set by Ahmed before the campaign window opens. Stream 8 has no
    bar to measure against until that number is confirmed. This is the single highest-priority
    open item for this plan.
  - tracking-plan.md: not yet produced by data-tracking-engineer. Every event reference in
    this plan names the expected event; confirmation that each one is wired and flowing belongs
    to data-tracking-engineer. Metrics marked with (PENDING EVENT) are blocked until the
    tracking plan is delivered and events are confirmed live.
  - gate_platform: unconfirmed. Email and push send events cannot be confirmed until the
    platform is named and wired.
  - budget: unconfirmed. Cost per subscription is a reportable efficiency read; the hard
    target waits on the budget confirmation.
  - app audience size: unconfirmed. App push segment size and push-specific metrics are
    estimated from the owned list; exact figure resolves at send.
- brief_refs:
  - objective: grow B2C subscriptions using the Masterclass as the lead hook.
  - success_metric: subscription conversions attributable to the campaign within the send and
    flight window. Target number pending Ahmed's confirmation.
  - window: proposed 2026-06-08 to 2026-06-28, ASSUMPTION, confirm.

---

## 1. What this plan does and does not do

This plan defines how the campaign is measured, monitored, and reported. It does not change
any live campaign, pause any ad set, shift any budget, or trigger any send. Every optimization
move is framed as a proposal that goes to the human gate. The event and warehouse layer is
owned by data-tracking-engineer; this plan reads from that layer, it does not wire it.

---

## 2. The success metric this plan measures against

The strategy-artifact sets the primary success metric as: subscription conversions attributable
to the campaign within the send and flight window.

That definition is fixed. The target number is ASSUMPTION and must be confirmed by Ahmed before
the campaign opens. This plan will not invent a number. Until the target is confirmed, stream 8
can report the absolute conversion count and the conversion rate, but cannot render a verdict
on whether the campaign hit its goal.

Secondary metrics the strategy sets (all measurable from day 1 once tracking is wired):
- Masterclass plays, with chapter 1 "The Talent" as the natural first-touch play event.
- Signup-gate completions (email or WhatsApp capture before the paid step).
- Cost per subscription on paid (efficiency read; hard target waits on budget confirmation).
- Owned-flow engagement: email open rate and click rate on the 4-message non-payer flow, push
  open rate and tap rate on the 5-touch app sequence.

Guardrail metrics the strategy flags (monitored for risk, not for goal-setting):
- Unsubscribe rate and complaint rate on owned sends.
- Paid ad frequency and negative feedback rate.

---

## 3. Event foundation (grounded in the defined funnel, pending tracking-plan.md)

The full-funnel map from the strategy-artifact defines four stages: reach and interest, capture,
nurture, and convert. Each stage has a corresponding event type this plan reads. Until
data-tracking-engineer delivers tracking-plan.md and confirms each event is live, all events
below are named as expected; none are assumed to be flowing.

### 3.1 Top of funnel, reach and interest

| Event (expected) | Source | What it measures |
|---|---|---|
| page_view on class page (EN and AR) | GA4, on-site | Class page reach, entry into the funnel |
| page_view on plans page | GA4, on-site | Intent to subscribe, pre-gate step |
| ad impression and click | Meta Ads Manager, Google Ads, TikTok | Paid reach and click-through |
| organic social reach and engagement | Platform native (Meta, IG, TikTok) | Organic reach and engagement |
| video play, chapter 1 "The Talent" | On-site or app player event | First-touch class engagement |

### 3.2 Capture (signup gate)

| Event (expected) | Source | What it measures |
|---|---|---|
| gate_view | GA4 or gate platform | Users reaching the gate |
| submit on gate form | GA4 or gate platform | Gate completion, email or WhatsApp capture |
| gate completion rate | Derived: submit divided by gate_view | Conversion from gate view to capture |

Note: the gate platform is an OPEN ITEM. Email and WhatsApp gate events are PENDING EVENT
until the platform is confirmed and wired.

### 3.3 Nurture (lifecycle email and app push)

| Event (expected) | Source | What it measures |
|---|---|---|
| email send | Email platform | Volume sent, suppression applied |
| email open | Email platform | Open rate per message (E1 to E4) |
| email click | Email platform | Click rate per message, link-level breakdown |
| email unsubscribe | Email platform | Guardrail: list health |
| email complaint | Email platform | Guardrail: deliverability risk |
| push send | App push platform | Volume sent to app segment |
| push open | App push platform | Open rate per push (P1 to P5) |
| push tap | App push platform | Tap rate, deep-link click |

All email and push events are PENDING EVENT: gate_platform is unconfirmed.

### 3.4 Convert (subscription)

| Event (expected) | Source | What it measures |
|---|---|---|
| subscription start | Stripe, Apple IAP, Google Play Billing | The primary success metric event |
| subscription attribution | UTM parameters, platform attribution | Attributing conversions to the campaign |
| cost per subscription | Derived: paid spend divided by attributed conversions | Paid efficiency read |

Attribution logic (to confirm with data-tracking-engineer): UTM parameters on all paid and
owned-channel links trace conversions back to the campaign. No personal or sensitive data in
URL parameters per CLAUDE.md. Attribution window to match the campaign flight window.

### 3.5 Retargeting signals (built from the above events)

Class-page and plans-page visitors who did not subscribe, gate completers who did not buy,
and video players who did not convert all feed the retargeting pool. The construction and
sizing of these audiences belongs to data-tracking-engineer and the performance-marketer. This
plan reads the retargeting conversion rate as a secondary readout; it does not build the audience.

---

## 4. Monitoring cadence (stream 8)

The proposed flight window is 2026-06-08 to 2026-06-28, 3 weeks. Cadence below is a proposal;
all review points are read-only monitoring, not live actions. Any optimization move surfaced
here is a proposal that goes to the human gate.

### 4.1 Day 1 to 3, launch check (2026-06-08 to 2026-06-10)

Goal: confirm tracking is live and baseline data is flowing. This check is about signal quality,
not optimization.

Read the following:
- Are page_view events hitting the class page and plans page? (GA4)
- Are paid impressions and clicks registering? (Ads Manager)
- Did E1 send and P1 push fire? Did open and click events come back?
- Are gate_view and submit events firing?
- Are any paid guardrail metrics (frequency, negative feedback rate) already elevated?

If any event is not flowing, route to data-tracking-engineer with the specific event name and
expected source. Do not read from a metric that is not confirmed flowing. Do not fabricate a
number for a missing event.

### 4.2 Mid-flight review (around 2026-06-15, day 7 to 8)

Goal: surface what is working and what is not, grounded in data. Propose optimizations.

Read the following:
- Subscription conversions attributed to the campaign so far. Compare to the confirmed target
  (once set). If target is still unset, report the absolute count with a note.
- Masterclass plays, chapter 1 specifically. Play rate from the class page.
- Gate completion rate (submit divided by gate_view).
- Email open and click rates for E1 and E2 (E3 not yet sent at this point per the calendar).
- Push open and tap rates for P1 and P2.
- Paid: CTR, cost per click, and any attributed conversions from paid by this point.
- Organic: reach and engagement rate on Posts 1 to 4.
- Guardrail check: unsubscribe and complaint rate, paid frequency and negative feedback.

Optimization proposals surfaced at this point, all routed to the human gate:
- If paid CTR is low, propose a creative variant test (one variable, see Section 5).
- If email open rate on E1 is materially below benchmark, propose a subject line test for E3.
- If gate completion rate is low, propose a gate copy or layout test.
- If a paid ad set is accumulating spend with no attributed conversions, propose a pause.
  This is a proposal to the human gate, not an action.

### 4.3 Final-week review (around 2026-06-22 to 2026-06-23)

Goal: confirm pacing toward the success metric and prepare the close.

Read the following:
- Subscription conversions to date vs confirmed target.
- Email E3 and E4 performance, open and click.
- Push P3 and P4 performance.
- Retargeting conversion rate from the paid retargeting layer.
- Organic reach cumulative.
- Paid cumulative cost per subscription.
- Guardrail metrics: unsubscribe, complaint, frequency.

Optimization proposals surfaced at this point, all routed to the human gate:
- If pacing is strong, propose increasing paid budget allocation to the converting ad set.
- If the non-payer flow conversion rate is low on E3, propose an angle change for E4.
- If P5 (last call push, 2026-06-27) would benefit from a different offer framing based on
  the segment that has not tapped P1 to P4, propose the copy change. Any change to a live
  send goes to the human gate first.

### 4.4 Post-flight window (after 2026-06-28)

Goal: close the measurement window and begin the campaign report.

Attribution window: allow 3 to 5 days past the flight end for in-flight conversions to
register before freezing the numbers. Exact window to confirm with data-tracking-engineer.
Once the window closes, pull the final figures and begin the campaign report (stream 9).

---

## 5. A/B test plan candidates

Each candidate below proposes one variable and one hypothesis. No test runs without human gate
approval. These are proposals.

All test candidates follow the same structure:
- One variable changed. Everything else held constant.
- A clear hypothesis: if X then Y because Z.
- A stop rule: when to read the result and stop, regardless of which variant leads.
- A proposed minimum detectable effect to avoid reading a noise signal as a win.

### 5.1 Email subject line test (E3, the engagement-to-conversion step)

Rationale: E3 moves the engaged (opened or played) segment to subscription. Subject line is
the highest-leverage variable before the email body and CTA, and it is the easiest single
change to isolate.

Variable: subject line wording on E3 only. One version leads with the skill outcome
(what the learner can do). One version leads with the instructor credential (who teaches it).
Everything else in E3 (body, CTA, design) is identical.

Hypothesis: a subject line leading with the skill outcome will produce a higher open rate for
the engaged segment than a subject line leading with the instructor credential, because this
segment has already seen the instructor angle in E1 and E2 and needs a new hook.

Stop rule: read after both variants have reached a minimum of 200 opens per arm, or at the
campaign close (2026-06-28), whichever comes first. If the owned non-payer list is smaller
than 400 opens total, the test will be underpowered and should not be read as statistically
meaningful; report the directional signal only and flag it as such.

Gate: proposal to human gate before any split is wired in the send platform.

### 5.2 Paid ad creative test (prospecting, top of funnel)

Rationale: paid creative is the first impression for the new-acquisition segment. The class
offers two strong proof points: the instructor's name and credibility, and the specific named
lessons (Foundation 101, Smokey Eyes, etc.). These two angles have not been tested against
each other.

Variable: primary visual and headline concept on one prospecting ad set. Variant A leads with
the instructor (hero the person). Variant B leads with a specific named lesson as the hook
(hero the skill). All other variables (audience, placement, CTA, bid strategy) held constant.

Hypothesis: the lesson-led variant will produce a higher click-through rate from the target
interest segment, because a specific achievable skill (Smokey Eyes, Foundation 101) is more
concrete than a name-led credential for a cold audience that does not yet know the instructor.

Stop rule: read after 7 days in-flight or after each variant has reached 500 link clicks,
whichever comes first. Stop early if one variant accumulates 3 times the negative feedback
rate of the other.

Gate: proposal to human gate. The performance-marketer executes the structural split if
approved; no spend changes without approval.

### 5.3 Gate copy test (signup gate, capture step)

Rationale: the gate is the funnel step between ad click and owned-contact acquisition. A low
gate completion rate is a direct drag on downstream conversion volume. The single variable
worth testing at the gate is the value proposition framing in the gate headline.

Variable: the headline above the gate form. Variant A frames the ask around the free chapter
("Start chapter 1 free today"). Variant B frames the ask around the learning outcome ("Get
one step closer to mastering the look"). Body copy, form fields, and CTA button are identical.

Hypothesis: the free-chapter framing will produce a higher gate completion rate because it
reduces the commitment signal: the user is entering to get something free, not making a
purchase decision.

Stop rule: read after 300 gate views per variant, or at day 10 of the flight, whichever comes
first. If total gate views are below 600 by day 10, report the directional signal and flag it
as underpowered.

Gate: proposal to human gate. Any live gate change goes through approval first.

---

## 6. Metrics to exclude (vanity list)

These metrics are readable from the event layer but are excluded from the success readout
because they do not connect to subscription conversions and can create a false impression of
campaign health.

- Follower count growth on organic social. Easy to move with paid amplification; does not
  reflect intent to subscribe.
- Total impressions. Volume without click-through tells nothing about funnel progress.
- Email list size. Acquiring addresses that never click is not a win.
- Video completion rate on chapter 1 (beyond the initial play event). A full play is a
  positive signal but does not predict conversion; reporting it as a primary metric would
  replace the actual goal with a proxy.
- Social post likes and shares. Engagement without conversion is a vanity read for a
  conversion-objective campaign.
- App install count. Installs that do not result in a subscription are not the success metric.
- Paid CTR in isolation. CTR without downstream conversion data measures creative appeal, not
  campaign performance.

Any of these may appear in supporting tables for context, but none replace the primary metric
or the defined secondaries in the readout.

---

## 7. Report structure (stream 9, campaign-close artifact)

At campaign close (after the attribution window, proposed 2026-07-01 to 2026-07-03), the
analytics-reporter produces the campaign report as the report-artifact. The structure below is
fixed; it does not change based on whether results were good or bad.

### 7.1 Results section

- Primary: subscription conversions attributed to the campaign. Stated as a number and as a
  rate against the confirmed target. If the target was never confirmed, the result is stated
  as an absolute number and the gap is noted as an open item that was never resolved.
- Secondary readout in order: Masterclass plays (total and chapter 1 specifically),
  gate completions and gate completion rate, email open and click rates per message,
  push open and tap rates per push, paid cost per subscription (if budget was confirmed).
- Guardrail readout: peak unsubscribe and complaint rate, paid frequency high point.
- Any metric that was not confirmed flowing from data-tracking-engineer is listed as a gap,
  not stated as a zero.

### 7.2 What worked section

Each claim requires an evidence line. No assertion without a number. Example structure: "The
engaged-segment branch (E3 to conversion) showed a higher click rate than the cold send (E1),
with [figure] vs [figure], suggesting that the play event is a meaningful engagement signal
for segment pacing." Numbers filled from actual event data; no illustrative figures in the
final report.

### 7.3 What to change section

Concrete, campaign-variable level. Example categories:
- Channel or segment to weight differently next run.
- Message in the flow to rewrite or resequence based on the open and click pattern.
- Paid creative angle to retire or scale based on the A/B test result.
- Gate copy to carry forward if the gate test produced a clear winner.
- Any confirmed ASSUMPTION from the brief that should be resolved before the next campaign
  starts (target number, budget, platform, send cadence).

### 7.4 Learnings log reference

Append a structured entry to the campaign learnings log at:
/home/user/claude/.claude/context/learnings-log.md (to be created if it does not exist).

Entry format:
- campaign_id
- date_appended
- primary_result: [number] subscriptions vs [target] target (or OPEN ITEM: target never set)
- what_worked: bullet list, evidence-tagged
- what_to_change: bullet list, concrete
- open_items_carried_forward: any metric that was never instrumented, any assumption never
  resolved

This entry feeds the next campaign's strategy-lead brief review.

---

## 8. Optimization moves: proposal format

Any observation surfaced in the monitoring cadence that suggests a campaign change is written
as a proposal in this format and routed to the human gate. This agent never acts on a live
campaign.

Proposal format:
- observation: what the data shows (event name, figure, date range)
- hypothesis: why this is happening
- proposed move: specific action (pause ad set X, shift budget from Y to Z, change send time
  of E3 by 1 day, deploy A/B test candidate 5.1)
- expected effect: what should improve and how it is measured
- gate: approval required from Ahmed before any action

No move is taken by this agent. No budget is shifted. No send is changed. No ad set is paused.
Every proposal stops at the human gate.

---

## 9. Pre-handoff checklist

Before this plan advances to the human gate:

- [x] Success metric is the one the strategy-artifact set, not one invented for this plan.
- [x] Target number flagged as ASSUMPTION and open item routed to Ahmed, not invented.
- [x] Every event referenced is named and sourced; all unconfirmed events are flagged PENDING
  EVENT pending tracking-plan.md from data-tracking-engineer.
- [x] No vanity metrics in the success readout structure.
- [x] No optimization move is an action; all are proposals to the human gate.
- [x] A/B test candidates each have one variable, one hypothesis, and a stop rule.
- [x] Report structure locks results to the defined success metric and secondaries.
- [x] Learnings log reference points to a persistent location for next-campaign use.
- [x] No em dashes. Western numerals throughout. No tatweel.
- [x] brand_qa: na for this internal artifact.

---

## 10. Handoff

This plan is available to data-tracking-engineer for the event list it depends on, and to the
performance-marketer for the paid monitoring cadence and A/B test proposals. It emits the
report-artifact at campaign close to the next campaign's strategy-lead. Open items requiring
human resolution are listed in the envelope at the top of this file.

Nothing in this plan sends, publishes, or spends. The plan is approval-ready at the human gate.
Approval is Ahmed's, per action and per campaign.
