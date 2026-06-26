# Measurement Plan: Summer of Skills, full-stack non-payer campaign

## Envelope

- campaign_id: 2026-07-summer-nonpayer
- produced_by: analytics-reporter
- streams: 8 performance monitoring and 9 reporting and learning
- status: qa-passed
- qa:
  - skill_eval: passed (structure and completeness reviewed against strategy-artifact, handoff-contract,
    and the 08 and 09 skill definitions; every required section present; no vanity metric in the
    success readout; all optimization moves are proposals; A/B tests each have one variable, one
    hypothesis, one stop rule; report-artifact shape matches handoff-contract.md; no invented
    numbers, no em dashes, no tatweel, Western numerals throughout)
  - arabic_qa: na (internal artifact, no customer-facing copy)
  - brand_qa: na (internal artifact)
- open_items:
  - OI-1: success_metric primary target NUMBER and confirmed flight dates are ASSUMPTION (flagged
    in both the brief and the strategy-artifact). The metric definition is stable. The target
    number and the measurement window dates must be confirmed by Ahmed before the campaign window
    opens. Stream 8 can report absolute conversion counts; it cannot render a pass-or-fail verdict
    against the goal until the number is set. Routed to Ahmed via the human gate.
  - OI-2: tracking-plan.md not yet produced by data-tracking-engineer (status: pending in
    00-orchestration.md). Every event reference in this plan names the expected event and its
    expected source. Confirmation that each is wired and flowing belongs to data-tracking-engineer.
    Metrics marked PENDING EVENT are blocked until the tracking plan is delivered and each event is
    confirmed live. Routed to data-tracking-engineer.
  - OI-3: gate_platform unconfirmed. Email and push send, open, click, and tap events cannot be
    confirmed until the platform is named and wired. Blocks all owned-channel metric reads. Routed
    to Ahmed via the human gate.
  - OI-4: budget and currency unconfirmed. Cost per subscription is an efficiency read only; the
    hard target waits on budget confirmation. Routed to Ahmed via the human gate.
  - OI-5: app audience size unconfirmed. App-push segment size and push-specific metrics resolve
    at send. Routed to data-tracking-engineer and lifecycle-architect.
  - OI-6: BigQuery, GA4, and Stripe access not yet granted. All warehouse and analytics queries
    in this plan are described and gated. Access is added on Ahmed's approval via settings.json.
    Routed to Ahmed.
  - OI-7: per-instructor public-naming confirmation pending at the human gate for all seven
    nameable candidates. Referenced in this plan only in the segment labels and the A/B test
    creative descriptions, consistent with the strategy-artifact's confirm-at-gate discipline.
  - OI-8: Saudi PDPL and data residency posture unconfirmed. No data collection, send, or wiring
    until compliance-privacy-reviewer clears the data-touching assets.
- brief_refs:
  - objective: convert and re-engage roughly 18,000 owned non-payers into paying Maharat
    subscribers over the summer, and acquire new subscribers across paid and organic, using the
    breadth of the instructor roster as the lead hook.
  - success_metric: paid subscription conversions attributable to the campaign within the
    confirmed flight window (owned flow plus new acquisition). Target NUMBER: ASSUMPTION, confirm
    with Ahmed. Primary measurement dates: ASSUMPTION, proposed 2026-07-01 to 2026-08-31, confirm.
  - window: proposed 2026-07-01 to 2026-08-31, ASSUMPTION, confirm.
  - reporting_cadence: proposed weekly readout to Ahmed against the success_metric, ASSUMPTION,
    confirm.

---

## 1. What this plan does and does not do

This plan defines how campaign 2026-07-summer-nonpayer is monitored during flight (stream 8)
and reported at close (stream 9). It does not change any live campaign, pause any ad set, shift
any budget, or trigger any send. Every optimization move is framed as a proposal for the human
gate. The event and warehouse layer is owned by data-tracking-engineer; this plan reads from
that layer, it does not define or wire it.

The dashboard spec in section 4 describes what to show and why. It does not build a BI tool or
adopt a platform; any tool adoption runs through build-vs-buy and requires Ahmed's approval.

---

## 2. The success metric this plan measures against

Source: strategy-artifact section 2.

Primary metric (definition stable, target NUMBER is ASSUMPTION):
Paid subscription conversions attributable to campaign 2026-07-summer-nonpayer within the
confirmed flight window, counted across both engines: the owned flow (email plus app push) and
new acquisition (paid plus organic). Attribution by signup-gate or owned-contact lineage to a
subscription_start or purchase event. Target NUMBER and date: ASSUMPTION, confirm with Ahmed.

This is the only primary metric. Stream 8 measures against it. Stream 9 reports against it.
No secondary metric replaces it and no vanity metric stands in for it.

Measurable secondaries from the strategy-artifact (section 2, stable definitions, readable
once tracking is wired):

| Secondary metric | Definition | Source event |
|---|---|---|
| Owned open rate | Email opens divided by emails delivered, per message in the non-payer sequence | Email platform (PENDING EVENT: OI-3) |
| Owned click rate | Email link clicks divided by emails delivered, per message | Email platform (PENDING EVENT: OI-3) |
| Push open rate | Push opens divided by push sends, per message in the app sequence | App push platform (PENDING EVENT: OI-3, OI-5) |
| Push tap rate | Push deep-link taps divided by push sends, per message | App push platform (PENDING EVENT: OI-3, OI-5) |
| Signup-gate completions | Unique form submits at the acquisition gate | gate submit event, GA4 or gate platform (PENDING EVENT: OI-2, OI-3) |
| Free intro-chapter plays | Unique plays of chapter 1 across featured classes | chapter_1_play event, on-site or in-app player (PENDING EVENT: OI-2) |
| Owned reactivation rate | Share of never-engaged and lapsed-engaged contacts that take any tracked action in the flight (open, click, tap, play, or gate submit) | Email platform plus GA4, joined on contact ID (PENDING EVENT: OI-2, OI-3) |
| Cost per subscription on paid | Paid spend divided by attributed subscription conversions from paid channels | Ads Manager plus subscription_start event (PENDING EVENT: OI-2, OI-4) |

Guardrail metrics (monitored for risk, not goal-setting):

| Guardrail metric | Threshold to surface as a risk flag |
|---|---|
| Email unsubscribe rate | Above 0.5 percent on any single send |
| Email spam-complaint rate | Above 0.1 percent on any single send |
| App-push opt-out rate | Any material single-send spike vs the preceding send |
| Paid ad frequency | Above 4 on any ad set within a 7-day window |
| Paid negative-feedback rate | Above category benchmark, to be confirmed with performance-marketer |

Guardrail thresholds above are proposed defaults. The performance-marketer and lifecycle-architect
confirm the live thresholds relevant to each channel at campaign start.

---

## 3. Event foundation (pending tracking-plan.md from data-tracking-engineer)

The strategy-artifact defines five funnel stages for this campaign: reach and interest, capture
(signup gate), nurture (owned email and push), convert (subscription), and retargeting. Each
stage has corresponding events this plan reads. All events below are named as expected. None are
assumed to be flowing until data-tracking-engineer delivers tracking-plan.md and confirms each
event is live.

### 3.1 Reach and interest (top of funnel)

| Event (expected) | Source | Metric served |
|---|---|---|
| page_view on class pages | GA4, on-site | Class page reach and entry to funnel |
| page_view on plans page | GA4, on-site | Intent to subscribe, pre-gate |
| ad impression and click | Meta Ads Manager, Google Ads, TikTok Ads | Paid reach and CTR (supporting cut, not primary) |
| organic social reach and engagement | Platform native (Meta, Instagram, TikTok) | Organic reach signal (supporting cut, not primary) |
| chapter_1_play (intro play per class) | On-site or in-app player event | Free intro-chapter plays (secondary metric) |

The per-field interest cuts from the strategy-artifact (music, cooking, acting, makeup, business,
styling, marketing) are the segments this top-of-funnel data is cut against. Constructing and
sizing those cuts from GA4 and Ads Manager belongs to data-tracking-engineer and the
performance-marketer once tracking is wired.

### 3.2 Capture (signup gate)

| Event (expected) | Source | Metric served |
|---|---|---|
| gate_view | GA4 or gate platform | Users reaching the gate |
| gate_submit | GA4 or gate platform | Signup-gate completions (secondary metric) |
| gate_completion_rate | Derived: gate_submit divided by gate_view | Funnel efficiency at capture |

Gate platform is an OPEN ITEM (OI-3). Gate events are PENDING EVENT until the platform is
confirmed and wired by data-tracking-engineer.

### 3.3 Nurture (owned email and app push)

| Event (expected) | Source | Metric served |
|---|---|---|
| email_send | Email platform | Volume sent per message, suppression confirmed |
| email_open | Email platform | Open rate per message (secondary metric) |
| email_click | Email platform | Click rate per message (secondary metric) |
| email_unsubscribe | Email platform | Guardrail: list health |
| email_complaint | Email platform | Guardrail: deliverability risk |
| push_send | App push platform | Volume sent to app segment |
| push_open | App push platform | Push open rate per message (secondary metric) |
| push_tap | App push platform | Push tap rate, deep-link click (secondary metric) |
| push_optout | App push platform | Guardrail: opt-out rate |

All email and push events are PENDING EVENT (OI-3, OI-5). The owned email sequence (proposed
4 to 5 messages) and the app-push sequence cadence are ASSUMPTION; the lifecycle-architect
confirms the message calendar at build.

The two recency segments from the strategy-artifact (never-engaged vs lapsed-engaged) are read
separately where the send platform supports a segment tag on events. If the platform cannot tag
by segment at event level, the open and click cuts are flagged as unresolvable and the note goes
to data-tracking-engineer.

### 3.4 Convert (subscription)

| Event (expected) | Source | Metric served |
|---|---|---|
| subscription_start | Stripe, Apple IAP, Google Play Billing | Primary success metric: subscription conversions |
| purchase | Stripe, Apple IAP, Google Play Billing | Revenue confirmation for attribution |
| campaign attribution | UTM parameters on all owned and paid links, platform attribution | Attributing conversions to campaign 2026-07-summer-nonpayer |

Attribution logic: UTM parameters on all paid and owned-channel links trace subscription_start
and purchase events back to the campaign. No personal or sensitive data in URL parameters, per
CLAUDE.md. Attribution window matches the flight window once confirmed. Stripe, Apple IAP, and
Google Play access are PENDING (OI-6). UTM scheme to confirm with data-tracking-engineer at
build. Mobile attribution (Apple IAP, Google Play) is flagged to-confirm with data-tracking-engineer,
never guessed.

### 3.5 Retargeting signals

Class-page and plans-page visitors who did not subscribe, gate completers who did not convert,
and chapter-1 players who did not convert all feed the retargeting pool. The construction and
sizing of those audiences belong to data-tracking-engineer and the performance-marketer. This
plan reads the retargeting conversion rate as a supporting cut; it does not define or build the
retargeting audience.

---

## 4. Dashboard spec (stream 8, recurring performance view)

This section specifies what the recurring performance dashboard shows and why. It does not build
a BI tool or warehouse layer, and any tool adoption runs through build-vs-buy with Ahmed's
approval. The spec describes what to show, grounded in the event data from data-tracking-engineer.

### 4.1 Purpose and cadence

The dashboard is the weekly readout to Ahmed against the primary success_metric. It shows the
few metrics that track the strategy's success_metric and the defined secondaries. It does not
show vanity counts. The proposed cadence is weekly (ASSUMPTION, confirm: OI per brief section 8).

### 4.2 Primary panel: conversions against the target

What to show: subscription conversions attributed to campaign 2026-07-summer-nonpayer,
cumulative from campaign start to the current date, plotted as a line against the flight window.
If the target NUMBER has been confirmed, show a target line. If it has not, show the absolute
count only and note that the bar is unset.

Why: this is the primary success metric. Every other panel supports it; none replace it.

Segment cuts to show:
- Owned channel conversions vs acquisition channel conversions (owned flow vs paid plus organic)
- Per-entry-point breakdown: B owned email, B app push, A paid (Meta, TikTok, Google), C organic

Each cut traces to the attribution events in section 3.4.

### 4.3 Owned-channel panel: email and push health

What to show: open rate and click rate per email message in the non-payer sequence, and push
open rate and tap rate per push message, both split by the two recency segments (never-engaged
vs lapsed-engaged) where the send platform tags the segments.

Why: the owned audience (roughly 18,000 non-payers) is the primary engine. Open and click rate
are the leading indicators for owned-channel conversions. Reading them per message shows which
step in the sequence is the bottleneck. Reading them per segment shows whether the never-engaged
and lapsed-engaged cuts respond differently, which feeds the optimization proposals and the next
campaign's sequence design.

### 4.4 Acquisition panel: gate completions and chapter plays

What to show: signup-gate completions (total and gate completion rate: submit divided by gate_view)
and chapter-1 play counts per featured class, broken down by the per-field acquisition segments
where GA4 or the send platform supports it.

Why: gate completions and chapter plays are the two leading indicators from the acquisition engine
(paid and organic) before a conversion lands. If gate completion rate drops, the conversion
engine stalls upstream of any subscription decision. If chapter plays are high but gate completions
are low, the funnel bottleneck is at the gate, not at interest. Per-field breakdown shows which
instructor domains are driving engagement, which feeds the budget allocation proposals.

### 4.5 Paid-efficiency panel: cost per subscription

What to show: cost per subscription on paid (derived: confirmed paid spend divided by attributed
subscription conversions from paid channels), by channel (Meta, TikTok, Google) and by
acquisition segment (per-field interest cut).

Why: cost per subscription is the paid-channel efficiency read. It is not a primary success
metric, but it is the input to any budget-shift proposal. Reading it by channel and by field
shows where paid is efficient and where it is not, which is the ground for any reallocation
proposal to the human gate.

Note: this panel is blocked until budget is confirmed (OI-4) and Stripe plus Ads Manager access
is granted (OI-6).

### 4.6 Guardrail panel: risk flags

What to show: email unsubscribe rate, email spam-complaint rate, app-push opt-out rate, paid
ad frequency, and paid negative-feedback rate, each plotted against the guardrail thresholds
from section 2. A metric that crosses its threshold appears as a flag in the weekly readout.

Why: guardrail metrics do not measure success; they measure risk. A spike in unsubscribe rate or
complaint rate is a deliverability risk that must surface immediately, not wait for the next
weekly read. Paid frequency above threshold is an audience fatigue signal that can damage the
retargeting pool if unchecked.

### 4.7 Segment cuts: never-engaged vs lapsed-engaged

Across all panels that include owned-channel data, the two recency segments from the
strategy-artifact (never-engaged and lapsed-engaged) are shown as separate lines or bars where
the send platform can tag the segment at event level. If the platform cannot tag by segment,
this cut is marked unavailable for the campaign and flagged to data-tracking-engineer for the
next campaign.

Why: the strategy-artifact identifies this as the primary owned-audience cut because the two
groups need different messages and different pacing. Reading them separately shows whether the
never-engaged group responds to the re-introduction angle and whether the lapsed-engaged group
converts faster on the more direct path. This comparison is the most actionable insight the
owned engine will produce.

### 4.8 Visualisation note

Each panel is a time-series line chart (conversion count, open rate, or cost per subscription
over the flight) or a segment comparison bar chart (per-field, per-message, or per-segment
breakdown). Labels are Western numerals. No design or BI tool is specified here; the spec
describes what to show and why. Tool selection goes through build-vs-buy.

---

## 5. Monitoring cadence (stream 8)

The proposed flight window is 2026-07-01 to 2026-08-31 (ASSUMPTION, confirm). The cadence
below is the proposed weekly monitoring schedule. All review points are read-only; any
optimization move surfaced is a proposal for the human gate, never an action taken here.

### 5.1 Day 1 to 3: launch check (proposed 2026-07-01 to 2026-07-03)

Goal: confirm tracking is live and baseline data is flowing. This is a signal-quality check,
not an optimization pass.

Read the following (data-tracking-engineer confirms each event is live before this check runs):
- Are page_view events hitting the class pages and the plans page in GA4?
- Are paid impressions and clicks registering in Ads Manager?
- Did the first email send (E1) fire? Did open and click events return?
- Did the first app-push send (P1) fire? Did push_open and push_tap events return?
- Are gate_view and gate_submit events firing at the signup gate?
- Are any guardrail metrics (email complaint rate, paid negative-feedback rate) already elevated?

If any event is not flowing, route to data-tracking-engineer with the specific event name and
expected source. Do not read from a metric that is not confirmed flowing. Do not fabricate a
number for a missing event.

### 5.2 Week 2: mid-flight read (proposed around 2026-07-08)

Goal: surface what is working and what is not across all channels, grounded in data. Propose
optimizations.

Read the following:
- Subscription conversions attributed to the campaign to date (absolute count; compare to the
  confirmed target once set).
- Chapter-1 play counts and play rate from class pages, total and per featured field.
- Gate completion rate (gate_submit divided by gate_view).
- Email open and click rates for the messages sent to date (E1 and E2 at minimum), per
  recency segment where the platform tags segments.
- Push open and tap rates for the push messages sent to date (P1 and P2 at minimum).
- Paid: click-through rate, cost per click, and attributed conversions by channel and by
  per-field acquisition segment.
- Organic: reach and engagement rate on posts published to date.
- Guardrail check: unsubscribe rate, complaint rate, push opt-out rate, paid frequency,
  paid negative-feedback rate.

Optimization proposals surfaced at this point, all routed to the human gate:
- If owned open rate on E1 is below the lapsed-engaged segment benchmark, propose a subject
  line test on the next send (see A/B test backlog, section 6.2).
- If paid CTR is low on a field-specific ad set, propose a creative variant test on that
  field's set (see section 6.1).
- If gate completion rate is materially low, propose a gate headline test (see section 6.3).
- If a paid ad set is accumulating spend with no attributed conversions after 7 days, propose
  a pause. Proposal to the human gate, not an action.

### 5.3 Weeks 3 to 4: pacing read (proposed around 2026-07-15 and 2026-07-22)

Goal: confirm pacing toward the success metric and read any in-flight A/B test results.

Read the following:
- Cumulative subscription conversions vs confirmed target.
- Per-channel conversion split (owned vs paid vs organic).
- Email performance for messages sent in weeks 2 and 3, per recency segment.
- Push performance for the corresponding push messages.
- Paid cost per subscription by channel and by field, updated with current spend.
- Any in-flight A/B test: if one was approved after the mid-flight read, read it against the
  stop rule defined in section 6.
- Guardrail metrics.

Optimization proposals at this point, all routed to the human gate:
- If pacing is strong on a specific field's paid ad sets, propose shifting budget allocation
  toward the converting field. No spend change without approval.
- If a per-field paid set is consistently below the CTR and conversion benchmarks and has been
  running more than 2 weeks, propose pausing it and redirecting to the top-performing fields.
- If the lapsed-engaged segment is converting at a materially higher rate than never-engaged,
  propose a lighter send cadence for never-engaged in the remaining flight to reduce complaint
  risk, and concentrate conversion-oriented messages on lapsed-engaged.

### 5.4 Weeks 5 to 9: weekly cadence (proposed 2026-07-29 to 2026-08-26)

Goal: maintain the weekly readout across the full summer flight. Read the same metrics as
section 5.3 on each weekly cycle. Surface any new proposals for the human gate as they emerge.

The owned email sequence and app-push sequence are likely shorter than the full flight window.
Once the non-payer flow has completed for a given contact, that contact exits the owned sequence.
The weekly monitoring reads the cumulative conversion count and any retargeting layer performance
from the paid channel through the remainder of the flight.

### 5.5 Final week: close window (proposed 2026-08-24 to 2026-08-31)

Goal: confirm pacing to close, prepare the stream 9 report.

Read the following:
- Subscription conversions to date vs confirmed target. State the gap or beat plainly.
- Final email sequence performance (all messages), per recency segment.
- Final push sequence performance.
- Retargeting conversion rate from the paid retargeting layer.
- Paid cumulative cost per subscription.
- Organic cumulative reach.
- Guardrail metrics: final unsubscribe, complaint, push opt-out, paid frequency.

Optimization proposals at this point, routed to the human gate only:
- If the final-sequence email would benefit from a different offer framing for the segment
  that has not clicked through earlier messages, propose the copy change. Any live-send change
  goes to the human gate first.
- If paid budget remains and one field's ad sets are converting efficiently, propose
  concentrating remaining budget there. No spend change without approval.

### 5.6 Attribution close (proposed 2026-09-01 to 2026-09-05)

Allow 3 to 5 days past the flight end for in-flight conversions to register before freezing
the numbers. Exact window to confirm with data-tracking-engineer. Once the window closes, pull
the final figures and begin the stream 9 campaign report. Do not state final numbers before the
attribution window closes.

---

## 6. A/B test backlog (stream 8, proposals for the human gate)

Each test below changes one variable and has one hypothesis and one stop rule. No test runs
without human gate approval. These are proposals, not launched tests.

### 6.1 Test 1: breadth-led vs field-led creative on paid prospecting

Variable under test: the primary visual and headline concept on one paid prospecting ad set.
Variant A (control): breadth-led creative. The visual and headline showcase the platform
breadth: many fields, one platform, this summer. An example headline direction (not final copy):
"7 fields, 7 experts, one summer." Variant B: field-led creative. The visual and headline focus
on one specific field and its instructor's credential. Each active field ad set is tested with
its own field-led variant; the test is run on one field's ad set at a time to isolate the
variable.
Everything else held constant: audience, placement, bid strategy, CTA, copy body.

Success metric (from strategy-artifact section 2): paid subscription conversions attributable
to the campaign within the flight window.

Hypothesis: field-led creative will produce a higher paid subscription conversion rate for
cold prospecting audiences than breadth-led creative, because a single concrete field and a
recognizable expert in it gives a cold audience a clearer and more motivating entry point than
a platform-breadth message that requires familiarity with the roster.

Variants:

| Variant | Description | The one thing that differs |
|---|---|---|
| A (control) | Breadth-led: "many fields, one platform" visual and headline | Baseline: platform-breadth creative |
| B | Field-led: one field, one instructor credential as the headline hook | Lead message is a single field and instructor credential |

Split: 50/50 within the ad set.
Audience: cold prospecting segment for the field in test, as defined in the strategy-artifact
acquisition cuts. New-acquisition adults, Arabic-speaking, GCC, Saudi Arabia primary.
Window: 7 days in-flight, starting from the day the test is approved and wired.

Sample size and method:
- Baseline rate: unknown pre-flight (no prior summer campaign; no number invented). Read from
  the first 3 days of flight once tracking is confirmed live. The baseline is the conversion
  rate on the control variant during days 1 to 3.
- Minimum detectable effect: a 30 percent relative increase in paid subscription conversion
  rate (absolute lift will depend on the baseline; the 30 percent relative threshold ensures
  the detected difference is operationally meaningful, not just statistically detectable noise).
- Derived per-arm sample size: calculated once the baseline rate is read from the first 3 days.
  Using a fixed-horizon test at 95 percent significance and 80 percent power, the per-arm
  sample size formula is n equals (2 multiplied by (z_alpha/2 plus z_beta) squared multiplied
  by p multiplied by (1 minus p)) divided by d squared, where p is the baseline conversion rate
  and d is the absolute MDE. This is computed at baseline-read time, not before baseline is
  known.
- Method: fixed-horizon two-proportion z-test, 95 percent significance (two-tailed), 80 percent
  power. Method chosen before the test runs. No peeking before the derived sample size is reached.

Stop rule: read once each arm reaches the derived per-arm sample size from the baseline
calculation, or at day 7, whichever comes first. If neither arm has reached the minimum sample
at day 7, report the directional signal and flag it as underpowered; do not declare a winner.
Decision threshold: if Variant B achieves a statistically significant higher conversion rate at
the 95 percent confidence level, propose scaling Variant B and retiring Variant A for this field.
If the result is inconclusive, keep the control and log the test as underpowered for the next
campaign's brief.

Human-gate note: this test is a proposal. The performance-marketer executes the structural split
once the human gate approves it. No spend changes without approval.
Spend on approval: the test uses budget already allocated to the paid field ad set, split 50/50.
No incremental spend is incurred; the existing ad set budget is reallocated, not increased.
Incremental budget would require a separate approval.
Open items: baseline rate not yet available (pre-flight); derived sample size to be computed at
baseline-read time. Naming of the specific instructor in Variant B is confirm-at-gate per the
strategy-artifact naming discipline.

### 6.2 Test 2: subject line variable on owned email, skill-outcome framing vs instructor-credential framing

Variable under test: the subject line wording on one email in the non-payer sequence (proposed
on the third message in the sequence, once the engagement baseline from E1 and E2 is readable).
Variant A (control): subject line leads with the instructor credential (the expert angle). The
instructor's name and their field are the opening hook.
Variant B: subject line leads with the skill outcome (what the learner can build this summer in
that field). The instructor name may appear in the preview text, not in the subject line itself.
Everything else in the email (body, CTA, visual) is identical.

Success metric (from strategy-artifact section 2): paid subscription conversions attributable
to the campaign within the flight window.

Hypothesis: a subject line leading with the skill outcome will produce a higher email open rate
for the lapsed-engaged segment than a subject line leading with the instructor credential,
because the lapsed-engaged contacts have already seen the instructor-credential framing in the
earlier emails and need a new hook to re-engage; the skill-outcome framing speaks to their
original intent (to build a skill) rather than repeating the instructor's name.

Variants:

| Variant | Description | The one thing that differs |
|---|---|---|
| A (control) | Subject line leads with instructor name and field credential | Subject line anchor: instructor credential |
| B | Subject line leads with the skill outcome (what you can build this summer) | Subject line anchor: skill outcome for the learner |

Split: 50/50 within the email send to the lapsed-engaged segment.
Audience: lapsed-engaged owned email contacts from the non-payer sequence (strategy-artifact
section 3.1, lapsed-engaged cut). Size is a share of roughly 18,000; exact at send.
Window: the send date of the third email message in the non-payer sequence, to be confirmed
with lifecycle-architect.

Sample size and method:
- Baseline rate: open rate on E1 and E2 for the lapsed-engaged segment. Read from the email
  platform once E1 and E2 have sent and events are confirmed flowing.
- Minimum detectable effect: a 5 percentage point absolute increase in open rate (for example
  from 25 percent to 30 percent), chosen as the threshold above which a subject-line change is
  worth carrying forward to the next campaign.
- Derived per-arm sample size: at 95 percent significance and 80 percent power, for a baseline
  of p and MDE of 5 percentage points, the per-arm sample size is calculated at baseline-read
  time. If the lapsed-engaged segment is below the minimum per-arm sample size needed, the test
  is flagged as underpowered and the directional signal is reported only.
- Method: fixed-horizon two-proportion z-test, 95 percent significance (two-tailed), 80 percent
  power. Method chosen before the test runs. No peeking before the derived sample size is reached.

Stop rule: read once both arms have reached the derived per-arm sample size, or at the campaign
close window (proposed 2026-08-31), whichever comes first. If total lapsed-engaged list size
produces fewer than the required per-arm sample per arm, report the directional signal and flag
it as underpowered; do not declare a winner and carry the test design to the next campaign.
Decision threshold: if Variant B achieves a statistically significant higher open rate at 95
percent confidence, carry the skill-outcome subject-line framing to the next campaign's email
sequence design and record it in the learnings log.

Human-gate note: this test is a proposal. The send platform split is wired only after the human
gate approves it. Any change to a live send goes through approval first.
Open items: baseline open rate not available until E1 and E2 send events are confirmed flowing
(blocked on OI-2 and OI-3); derived sample size to be computed at baseline-read time.

### 6.3 Test 3: landing-page hero framing, skill-outcome vs breadth-roster

Variable under test: the hero headline and supporting subhead on the campaign landing page (or
the above-the-fold section of the plans page if a dedicated landing page is not built). Variant
A (control): hero leads with the platform breadth and the roster ("many fields, one platform,
this summer"). Variant B: hero leads with the skill-outcome and the free intro chapter ("this
summer, build a real skill, starting free").
Everything else on the page is identical: navigation, class cards, plan options, CTA buttons.

Success metric (from strategy-artifact section 2): paid subscription conversions attributable
to the campaign within the flight window.

Hypothesis: a hero leading with the skill-outcome-and-free-entry framing will produce a higher
page-to-subscription conversion rate than a hero leading with the roster-breadth framing, because
for a visitor arriving from a paid or organic click the most useful reassurance is that the first
step is free and the payoff is concrete, rather than a catalogue statement about how many fields
the platform covers.

Variants:

| Variant | Description | The one thing that differs |
|---|---|---|
| A (control) | Hero: breadth-roster statement (many fields, one platform) | Headline anchor: roster breadth |
| B | Hero: skill-outcome plus free-intro-chapter entry (build a real skill, start free) | Headline anchor: skill outcome and free entry |

Split: 50/50, rotating by session on the landing or plans page.
Audience: all paid and organic traffic arriving at the campaign landing page during the flight.
Window: from landing-page launch through the end of the flight (proposed 2026-07-01 to
2026-08-31).

Sample size and method:
- Baseline rate: page-to-subscription conversion rate on the control variant. Read from GA4
  once the page is live and page_view and subscription_start events are confirmed flowing.
- Minimum detectable effect: a 25 percent relative increase in page-to-subscription conversion
  rate, chosen as the threshold above which the hero framing change is operationally meaningful.
- Derived per-arm sample size: calculated at baseline-read time using fixed-horizon z-test at
  95 percent significance, 80 percent power.
- Method: fixed-horizon two-proportion z-test, 95 percent significance (two-tailed), 80 percent
  power. Method chosen before the test runs. No peeking before the derived sample size is reached.

Stop rule: read once both arms have reached the derived per-arm sample size, or at the campaign
close (2026-08-31), whichever comes first. If traffic volume does not produce the minimum per-arm
sample by close, report the directional signal and flag it as underpowered.
Decision threshold: if Variant B achieves a statistically significant higher conversion rate at
95 percent confidence, carry the skill-outcome-and-free-entry hero framing to the next campaign's
landing-page design and record it in the learnings log.

Human-gate note: this test is a proposal. The landing-page variant split is wired only after
the human gate approves it, and only after the conversion-engineer builds the page per the
web-design-package. Any live-page change goes through approval first.
Open items: baseline conversion rate not available pre-flight (blocked on OI-2, OI-6);
page build depends on web-design-package and conversion-package (both pending per the
orchestration log).

---

## 7. Qualitative signal: feedback readout

Alongside the quantitative monitoring, this plan specifies a feedback readout from qualitative
sources. The output is a feedback-readout that travels with the stream 8 and 9 outputs and
hands forward to the strategy-lead for the next campaign. The analysis mines themes, not
identities. Every verbatim quoted in the readout has personal data removed first: no names,
handles, or contact details.

### 7.1 Sources

- App store reviews (coordinated with aso-specialist, which owns the store reviews response
  policy). Mine reviews published during the campaign flight window. Separate pre-campaign
  baseline from in-flight new reviews.
- Social comments on campaign posts (coordinated with organic-social). Mine the comment threads
  on posts tagged to the 2026-07-summer-nonpayer campaign.
- Support or survey text where it exists and is made available by Ahmed. If no support or
  survey data is provided, this source is marked not available and the readout proceeds on the
  app store and social comment sources only.

### 7.2 Method

1. Collect verbatims from each source within the campaign flight window.
2. Cluster verbatims into named themes by the topic they address, not by sentiment alone.
3. Size each theme by the number of verbatims that map to it. A theme that appears in fewer
   than 3 verbatims across the full flight is flagged as a one-off signal, not a pattern.
4. For each recurring theme, select the one verbatim that most clearly represents the theme,
   strip all personal data (names, handles, contact details, identifiers), and quote it.
5. Separate real signal (a theme recurring across sources and in volume) from one-off noise
   (an isolated comment with no supporting cluster).
6. Never fabricate a theme to fit the campaign narrative. If the qualitative signal does not
   support a proposed story, say so.

### 7.3 Output shape

The feedback-readout is appended to the stream 8 performance readouts and the stream 9
campaign report:

| Theme name | Source(s) | Verbatim count | Representative verbatim (personal data removed) | Signal or noise | Feeds what_to_change |
|---|---|---|---|---|---|
| (populated at close, from real data only) | | | | | |

No theme is stated until the flight data exists. Pre-flight, this table is empty and marked
pending.

---

## 8. Report-artifact shape (stream 9, campaign close)

At campaign close, after the attribution window closes (proposed 2026-09-01 to 2026-09-05),
the analytics-reporter produces the campaign report as the report-artifact. The structure below
is fixed per the handoff-contract. It does not change based on whether results were good or bad.
The report is honest: misses are stated plainly with the data behind them.

### 8.1 Common envelope (at report time)

```
campaign_id:     2026-07-summer-nonpayer
produced_by:     analytics-reporter
stream:          9 reporting and learning
status:          (draft at production, advances to qa-passed after skill eval)
qa:
  skill_eval:    (run at report time)
  arabic_qa:     na (internal artifact)
  brand_qa:      na (internal artifact)
open_items:      (any metric blocked on event data not yet flowing, stated as gaps not zeros)
brief_refs:
  objective:     convert and re-engage owned non-payers and acquire new subscribers over the summer
  success_metric: paid subscription conversions attributable to the campaign within the flight window
  window:        confirmed flight dates (to be filled at report time)
```

### 8.2 Results section

Structure:
- Primary: subscription conversions attributed to campaign 2026-07-summer-nonpayer, stated as
  an absolute count and as a rate against the confirmed target. If the target was never confirmed
  (OI-1), the result is stated as an absolute count and the gap is noted as an unresolved open
  item, not fabricated.
- Secondary readout in order: chapter-1 play counts (total and per featured field),
  gate completions and gate completion rate, email open and click rates per message (per recency
  segment where the platform tags them), push open and tap rates per message, owned reactivation
  rate (share of never-engaged and lapsed-engaged that took any tracked action), paid cost per
  subscription by channel (if budget was confirmed).
- Guardrail readout: peak unsubscribe rate, peak complaint rate, push opt-out rate, paid
  frequency high point, paid negative-feedback rate.
- A/B test results: one paragraph per test that ran, stating the variable, the result at the
  stop rule, and the decision.
- Any metric not confirmed flowing from data-tracking-engineer is listed as a measurement gap,
  not stated as a zero.

### 8.3 What-worked section

Each claim requires an evidence line. Structure: "[Finding], supported by [metric], [figure],
[source], [date range]." No assertion without a number behind it. The what-worked section feeds
the qualitative feedback themes from section 7 as a supporting signal alongside the quantitative
evidence.

### 8.4 What-to-change section

Concrete, campaign-variable level. Each item names the change, the owner, and the target brief
or date:

- Channel or segment to weight differently next campaign, with owner and target brief.
- Message in the flow to rewrite or resequence, with owner (lifecycle-architect or copywriter)
  and target brief.
- Paid creative angle to retire or scale based on the A/B test result, with owner
  (performance-marketer) and target brief.
- Landing-page hero to carry forward if the page test produced a clear winner, with owner
  (web-design-director or conversion-engineer) and target brief.
- Any confirmed ASSUMPTION from the brief that must be resolved before the next campaign starts:
  the success-metric target number, budget, platform, send cadence, per-instructor public-naming
  confirmation. Each carries its owner and a note that it blocked a specific measurement.

### 8.5 Learnings log reference

At report time, append a structured entry to:
/home/user/claude/.claude/context/learnings-log.md
(created if it does not exist).

Entry format:
- campaign_id: 2026-07-summer-nonpayer
- date_appended: (date of report production)
- primary_result: (number) subscription conversions vs (target) target, or "OPEN ITEM: target
  never confirmed" if OI-1 was not resolved.
- what_worked: bullet list, each with the evidence metric and figure.
- what_to_change: bullet list, concrete, each with the owner and the target brief.
- open_items_carried_forward: list of OI items that were never resolved during the flight and
  must be resolved before the next summer campaign.
- ab_test_results: summary of each test, the variable, the outcome, and whether the finding
  was carried forward.
- feedback_themes: the named themes from the qualitative feedback readout, sized by verbatim
  count, with one representative sanitised verbatim each.

This entry feeds the next campaign's strategy-lead brief review.

---

## 9. Optimization-move proposal format (stream 8)

Any observation surfaced in the monitoring cadence that suggests a campaign change is written
as a proposal in this format and routed to the human gate. This agent never acts on a live
campaign.

Proposal format:
- observation: what the data shows (event name, figure, date range)
- hypothesis: why this is happening
- proposed move: specific action (pause ad set X, shift budget from Y to Z, change send time
  of E3, deploy A/B test candidate from section 6)
- expected effect: what should improve and how it is measured
- gate: approval required from Ahmed before any action is taken

No move is taken by this agent. No budget is shifted. No send is changed. No ad set is paused.
Every proposal stops at the human gate.

---

## 10. Metrics excluded from the success readout (vanity list)

These metrics are readable from the event layer but are excluded from the primary readout
because they do not connect to subscription conversions and can create a false impression of
campaign health:

- Total paid ad impressions. Volume without downstream conversion tells nothing about campaign
  performance against the success metric.
- Organic social follower count growth. Easy to move with amplification; does not reflect
  subscription intent.
- Email list size. Addresses that never click or convert are not a win.
- Video completion rate on chapter 1 beyond the initial play event. A full play is a positive
  signal but does not predict conversion; reporting it as a primary metric replaces the goal
  with a proxy.
- Social post likes and shares on their own. Engagement without a downstream conversion is a
  vanity read for a conversion-objective campaign.
- App install count. Installs that do not result in a subscription are not the success metric.
- Paid CTR in isolation. Click-through rate without conversion data measures creative appeal,
  not campaign performance against the success metric.
- Page views on their own. Page views without a conversion signal are reach, not performance.

Any of these may appear in supporting tables for context, but none replace the primary metric
or the defined secondaries in the readout.

---

## 11. Pre-handoff checklist

- [x] Success metric is the one the strategy-artifact set (section 2), not invented for this plan.
- [x] Target number flagged as ASSUMPTION and as OI-1 routed to Ahmed; not invented.
- [x] Every event referenced is named and sourced; all unconfirmed events are flagged PENDING
  EVENT, pending tracking-plan.md from data-tracking-engineer (OI-2).
- [x] No vanity metrics in the success readout structure. Vanity list in section 10.
- [x] Dashboard spec describes what to show and why; does not build a BI tool.
- [x] No optimization move is an action; all are proposals to the human gate.
- [x] A/B test backlog: each of the three tests has exactly one variable, one hypothesis, one
  stop rule, and a human-gate note. Sample sizes are derived from baseline rate and MDE, not
  guessed; baseline is read from the first days of flight, not invented pre-flight.
- [x] Report-artifact shape matches handoff-contract.md section on report-artifact.
- [x] Qualitative feedback readout specifies source, method, and output shape; no theme is
  fabricated; personal data is stripped before any verbatim is quoted.
- [x] Learnings-log reference points to a persistent location for next-campaign use.
- [x] Weekly reporting cadence flagged as ASSUMPTION, confirmed with Ahmed per OI per brief
  section 8.
- [x] No em dashes anywhere in this file. Western numerals throughout. No tatweel.
- [x] brand_qa and arabic_qa: na for this internal artifact.
- [x] Open items are surfaced in the envelope, not buried: OI-1 through OI-8 each carry a
  clear blocker description and a routing note.

---

## 12. Handoff

This plan is available to data-tracking-engineer for the event list it depends on (the full
event set names are in section 3 and the open items in OI-2). It is available to the
performance-marketer for the paid monitoring cadence and the A/B test proposals in section 6.
It emits the report-artifact at campaign close (stream 9) to the next campaign's strategy-lead.
Open items requiring human resolution are listed in the envelope.

Nothing in this plan sends, publishes, or spends. The plan is approval-ready at the human gate.
Approval is Ahmed's, per action and per campaign.
