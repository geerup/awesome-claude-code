# strategy-artifact: Bassam Fattouh bridal makeup, non-payer lifecycle

Internal artifact, stream 2. Produced by strategy-lead from the validated brief and the
stream 1 kickoff scope. No customer-facing copy ships from here. The Arabic line below is an
illustrative angle line, not final copy. It runs the full gate stack when copywriter-ar
builds the real emails in stream 4. No em dashes, Western numerals only, no accreditation
claims, empowering framing.

v2 update notes: regenerated through the upgraded engine. Changes from v1: (1) added
per-segment pains and gains with a JTBD job story for each of the four non-payer segments,
each tied to that segment "why"; (2) added a competitive alternative to offer_framing (free
makeup tutorials on social, another beauty or learning app, or nothing) and why the
Masterclass-led subscription beats it; (3) restated success_metric with a proposed numeric
target and date as a clearly flagged ASSUMPTION, with leading versus lagging noted; (4)
recorded that Firecrawl could not enrich the published course page because this environment
blocks its egress, so lesson lineup, duration, price, and promotion stay OPEN ITEMS, not
invented. Confirmed facts unchanged: title and instructor Bassam Fattouh (published course
page), design-and-style category.

---

## Common envelope

- campaign_id: 2026-06-bassam-fattouh-bridal-makeup
- produced_by: strategy-lead
- stream: 2 strategy and planning
- status: qa-passed
- qa:
  - skill_eval: pass
  - arabic_qa: na (internal artifact, no customer copy ships here)
  - english_qa: na
  - design_qa: na
  - compliance: na
  - brand_qa: na
- open_items:
  1. Price and currency not confirmed (brief section 4, ASSUMPTION). Strategy frames the
     offer with no number. Blocks any asset that must show a price. Confirm before send.
  2. Plan not confirmed (1-month or 3-month entry, brief section 4, ASSUMPTION). Confirm
     which plan is the entry the flow drives to.
  3. Promotion not confirmed (trial, first-time discount, or bundle, brief section 4,
     ASSUMPTION). None invented. Confirm whether one exists.
  4. Success-metric target not confirmed (brief section 2, ASSUMPTION). A proposed number and
     date are carried below as a clearly flagged ASSUMPTION for Ahmed to confirm. No
     confirmed figure is invented.
  5. Gate platform not confirmed (brief section 5, OPEN ITEM). Email and WhatsApp platform
     not named. Blocks send wiring in streams 6 and 7. See
     references/2026-06-email-whatsapp-platform-research.md.
  6. Schedule not confirmed: start_date, end_date, send_window (brief section 6,
     ASSUMPTION). Proposed cadence carried below, confirm before send.
  7. Content lineup not confirmed (brief section 4). Lessons, modules, duration, and lesson
     count are not invented. Firecrawl could not enrich these from the published course page
     because this environment blocks its egress, so they remain OPEN ITEMS. If copy needs a
     specific, it is flagged an OPEN ITEM in stream 4.
  8. Approved imagery not confirmed (brief section 7, ASSUMPTION). Whether rights-cleared
     Bassam Fattouh or class imagery exists is unknown. Affects whether stream 3 creative
     runs. Any portrait or class imagery must be a real supplied asset, never generated.
  9. Suppression source not confirmed (brief section 3). Exclusion list (paying,
     unsubscribed, hard-bounced) logic is clear, the data source must be confirmed.
  10. Segment sizes below the about 18,000 total are planning splits, not confirmed counts.
      Each segment size resolves from live data at send time and is recorded in the
      lifecycle-package.
  11. Page-fact enrichment blocked. Firecrawl could not reach the published course page
      (https://www.maharat.com/en/library/design-style/bassam-fattouh-teaches-bridal-makeup)
      because this environment blocks its egress. Only the facts already confirmed in the
      brief are used: title, instructor Bassam Fattouh, design-and-style category. Price,
      promotion, duration, and lesson lineup are not read from the page and not invented.
- brief_refs:
  - entry_point: owned audience (brief section 2)
  - objective: convert non-paying contacts to paying subscribers, Bassam Fattouh bridal
    makeup Masterclass as the hook (brief section 2)
  - product: Masterclass "Bassam Fattouh Teaches Bridal Makeup" (brief section 4)
  - category: design and style (brief section 4, published course page path)
  - instructor: Bassam Fattouh, confirmed via the published Maharat course page (brief
    section 4), naming allowed in copy for this class
  - audience: owned non-paying email contacts, GCC, primary Saudi Arabia (brief section 3)
  - audience_size: about 18,000 non-paying contacts, planning estimate (brief section 3 and
    context/01-company-brief.md)
  - channels: email primary, WhatsApp out of scope here (brief section 5)
  - signup_gate: email, conversion to a paid plan (brief section 5)
  - budget: n/a, owned audience, zero media cost (brief section 6)
  - success_metric: subscription conversion rate from the flow, target an ASSUMPTION to
    confirm (brief section 2)
  - offer_framing_notes: empowering, lead with what the learner can create (brief section 4)
  - constraints: owned only, no paid build, RTL-correct Arabic, no accreditation, real
    Masterclass title only, do not invent the lineup (brief section 8)

---

## Stream 1 readiness summary (brief intake)

Carried into this artifact from brief-validate and kickoff-scope.

### Field status against the template

- PRESENT (confirmed, safe to act on): campaign_id, name, owner, created, entry_point,
  objective, audience, product, category (design and style), instructor (Bassam Fattouh, via
  the published course page), channels (email primary), signup_gate (email), budget (n/a),
  creative_direction rules, constraints, approval_owner, approval_status.
- PRESENT as planning estimate (not a confirmed send size): audience_size about 18,000
  non-payers. Exact figure resolves from live data at send.
- ASSUMPTION (flagged, not acted on as a real value): success_metric target, plan, price,
  promotion, start_date, end_date, send_window, assets_available.
- OPEN ITEM (unresolved, carried forward): gate_platform (blocks send wiring), content_lineup
  (do not invent, page enrichment blocked), suppression source, approved imagery, page-fact
  enrichment (Firecrawl egress blocked).
- MISSING that blocks the whole run: none. The brief explicitly authorizes drafting against
  the flagged ASSUMPTIONs so the package is approval-ready, with nothing sending.

### Stop-and-ask check

No field that blocks strategy work is silently missing. The strategy proceeds where it can
and flags every dependent choice. The one true hard block, the gate platform, blocks send
wiring downstream (streams 6 and 7), not strategy. The blocked page enrichment does not block
strategy either: the strategy uses only confirmed facts and leaves the unread specifics as
open items. Readiness: ready to scope with flagged assumptions.

### Entry point and active streams (kickoff scope)

- Entry point: B, owned audience. Confirmed with the orchestrator. No paid build, stream 5
  paid path is skipped. Zero media cost.
- Streams that run:
  - 1 brief intake, strategy-lead. Done.
  - 2 strategy and planning, strategy-lead. This artifact.
  - 4 copywriting, copywriter-ar (primary) and copywriter-en. Email copy and subject lines.
  - 7 lifecycle messaging, lifecycle-architect. The flow.
  - 6 conversion path, conversion-engineer and data-tracking-engineer. Runs only if the
    email points to a Maharat page or signup gate. The Masterclass is on a published
    maharat.com page and the conversion is to a paid plan, so a destination page or gate is
    in the path. Confirm at gate wiring.
  - 8 monitoring and optimization, analytics-reporter.
  - 9 reporting and learning, analytics-reporter.
- Stream 3 creative: runs only if the emails need a visual asset, and only against a real,
  rights-cleared supplied asset. Conditional on open item 8 (approved imagery). No generated
  portrait or class imagery.
- Out of scope: stream 5 paid build, WhatsApp layer (later), any generated likeness.

---

## Body

### segments[]

Segmentation axes for this campaign:

- Prior interest, beauty and self-presentation: bridal and special-occasion looks are a
  narrow interest. Contacts who have shown beauty or design-and-style interest are the
  warmest fit for this hook.
- Engagement state and recency of last open: separates contacts the email can actually reach
  and move from contacts who need a re-engagement posture first.
- Life-stage proxy where data supports it: bridal intent is occasion-driven. Treated as a
  soft signal only, never assumed, and only if the data carries it.

Sizes below are planning splits of the about 18,000 non-payer estimate, not confirmed counts.
Each resolves from live data at send time and is recorded in the lifecycle-package.

```
name:       beauty-interested-engaged
size:       resolved from live data at send time (planning split of the about 18,000 estimate)
definition: Non-paying contacts who have shown beauty, makeup, or design-and-style interest
            (browsed or opened beauty content, or sit in a beauty interest tag), and have
            opened or clicked an email within about the last 90 days.
why:        Warmest fit for a bridal makeup hook and reachable now. The angle can lead
            directly with what they can create. Highest expected conversion, so this segment
            carries the primary send and the sharpest offer framing.
pains:      They love makeup and self-presentation but lack a trusted, structured way to learn
            a professional bridal look. Free content they have tried is scattered and leaves
            them unsure which steps are right.
gains:      The confidence and skill to create a polished bridal look themselves, learning the
            craft from a leading regional artist they recognize and trust.
job_story:  When I have a wedding or special occasion coming up, I want to learn a professional
            bridal look from someone I trust, so that I can create it confidently myself
            without guessing.
```

```
name:       beauty-interested-lapsed
size:       resolved from live data at send time (planning split of the about 18,000 estimate)
definition: Non-paying contacts with the same beauty or design-and-style interest signal,
            but whose last open or click was more than about 90 days ago.
why:        Strong interest fit, weaker reach. A leading regional artist as the hook is a
            credible reason to re-open. Angle leads with the draw of the class itself to earn
            the re-engagement before the offer.
pains:      The interest is still there, but nothing recent gave them a strong enough reason to
            come back and act. Generic emails do not stand out from everything else competing
            for their attention.
gains:      A reason worth their time again, a standout class from a name they respect that
            reconnects them to a skill they wanted to build.
job_story:  When something genuinely worth my time appears, I want a clear reason to come back,
            so that I can pick up the beauty skill I was interested in before.
```

```
name:       general-engaged-nonpayers
size:       resolved from live data at send time (planning split of the about 18,000 estimate)
definition: Non-paying contacts with no specific beauty interest signal, but engaged
            (opened or clicked within about the last 90 days).
why:        Reachable and active, but the bridal hook is narrower than their interest. Angle
            broadens to learning a real, usable skill from a leading expert, with bridal
            makeup as the concrete example, so it lands beyond a strict bridal audience.
pains:      They want to keep growing and learning, but they have not yet found a class on the
            platform compelling enough to pay for. They are not sure a subscription is worth
            it for them.
gains:      Proof that the platform offers premium, expert-led learning worth paying for, with
            a concrete, high-quality example they can see and judge.
job_story:  When I am deciding whether a learning subscription is worth it, I want to see real
            premium teaching from a leading expert, so that I can judge whether it is for me.
```

```
name:       dormant-nonpayers
size:       resolved from live data at send time (planning split of the about 18,000 estimate)
definition: Non-paying contacts with no recent open or click (beyond about 90 days), no
            specific beauty interest signal.
why:        Lowest reach and fit. Lowest priority for this flow. Include only as a light
            re-engagement touch if cadence allows, never as the primary target. Heavy sends
            here risk deliverability for the whole list.
pains:      They have drifted away and a typical email no longer reaches them. Anything heavy
            or salesy makes them tune out further or unsubscribe.
gains:      A light, genuinely interesting reminder of what the platform now offers, with no
            pressure, that earns back a little attention.
job_story:  When a platform I once signed up for reaches out, I want it to be light and worth
            a glance, so that I can decide on my own terms whether to look again.
```

Sizing notes: the only confirmed planning figure is about 18,000 non-paying contacts
(context/01-company-brief.md). The four splits above are not separately confirmed and are not
invented as numbers. Interest tags, last-open recency, and any life-stage signal must come
from live data at send. Suppression (paying, unsubscribed, hard-bounced) is applied before
sizing, source to confirm (open item 9). Pains and gains above are drawn only from each
segment "why" and from context, never invented.

### angle

Core message: you can create a confident bridal look yourself, learning the craft directly
from a leading regional makeup artist on Maharat.

Serves: leads with the beauty-interested-engaged gain (the confidence and skill to create a
polished bridal look themselves) and relieves its pain (no trusted, structured way to learn).
It tunes to relieve the named pain of each other segment, see per-segment tuning below.

Rationale:
- Empowering, never deficit-framed. It leads with what the learner can make and become, a
  look they can do with their own hands, not with anything they lack or are behind on. This
  matches the brand voice and the brief's offer_framing_notes.
- It is true to the offer. The hook is a premium Masterclass from a named, publicly confirmed
  expert (Bassam Fattouh), which is exactly the kind of credible draw that earns an open and
  a play from a non-payer who has never paid before. It directly answers the
  beauty-interested pain of scattered, untrustworthy free content.
- It works across segments with one through-line. For beauty-interested segments the bridal
  look is the direct promise. For general-engaged contacts the same idea broadens to learning
  a real skill from a leading expert, with bridal makeup as the concrete proof, so the core
  idea stays single while the emphasis tunes per segment.
- It does not overclaim. No lesson count, no duration, no accreditation, no promise the
  content lineup has not confirmed. The draw is the artist and the craft, both of which are
  confirmed.

Per-segment tuning (the core idea stays one):
- beauty-interested-engaged: lead directly with creating the bridal look themselves, the
  sharpest offer framing. Relieves the pain of scattered free content with a trusted,
  structured class.
- beauty-interested-lapsed: lead with the draw of the class and the artist to earn the
  re-open first. Relieves the pain of having no strong reason to come back.
- general-engaged-nonpayers: broaden to learning a real, usable skill from a leading expert,
  with bridal makeup as the concrete proof. Relieves the doubt that the subscription is worth
  it by showing premium teaching.
- dormant-nonpayers: a light, low-pressure reminder only, the class as a single interesting
  signal of what the platform now offers. Relieves the pain that heavy or salesy contact
  pushes them further away.

Illustrative customer-facing line (not final copy, for direction only):
"اصنعي إطلالة عروس واثقة بنفسك، وتعلمي الفن من فنان مكياج رائد في المنطقة."

### offer_framing

How the brief's offer is positioned, with no price and no invented promotion:

- The hook: the Masterclass "Bassam Fattouh Teaches Bridal Makeup", named exactly as
  published, from a named regional expert, in the design and style category. The artist and
  the craft are the draw.
- The value: a real, usable skill the learner can apply to her own and others' bridal looks,
  framed as something she creates, not a gap she fixes.
- The path to a paid plan: the Masterclass is the entry point into a Maharat subscription.
  The flow positions subscribing as the way to keep learning beyond this one class, access
  to premium regional expertise on one platform. The specific plan is framed as the entry
  plan without naming which one until confirmed (open item 2).
- Competitive alternative (what the reader does today instead): the most common alternatives
  are free makeup tutorials on social platforms (YouTube, Instagram, TikTok), a separate
  beauty or generic learning app, or simply nothing, putting the bridal look off or paying a
  makeup artist on the day. These are real alternatives, not straw men.
  - Why the Masterclass-led subscription beats free social tutorials: free content is
    scattered, inconsistent in quality, and rarely from a recognized regional authority. It
    leaves the learner guessing which steps are right (the named beauty-interested pain). A
    structured Masterclass from Bassam Fattouh gives one trusted, coherent path from a leading
    artist, and the subscription keeps that quality available beyond a single video.
  - Why it beats another app: the draw is named, confirmed regional expertise and an
    Arabic-first platform built for this audience, not a generic catalog. One subscription
    opens premium expert-led learning across skills, not a single-purpose tool.
  - Why it beats nothing: it turns an occasion-driven wish into a skill the learner owns and
    can reuse, on her own terms and timeline, rather than depending on someone else on the day.
- Price: not shown. The brief marks price as an ASSUMPTION, so no number appears anywhere in
  framing or copy (open item 1). Firecrawl could not read a price from the published page
  because egress is blocked (open item 11), so none is taken from there either. When the price
  and plan are confirmed, the asset can carry the number if it calls for one.
- Promotion: none framed. No trial, discount, or bundle is implied, because none is confirmed
  (open item 3). If a promotion is confirmed, it becomes a sharpening layer on this frame, not
  a new angle.
- Guardrails honored in the frame: no completion-certificate or accreditation claim, no
  invented lessons or duration, the real title only, the instructor named only because the
  published course page confirms him.

### channel_plan

- Entry point: owned (B). Owned non-paying email contacts, no paid acquisition, zero media
  cost.
- Streams in this campaign: 1, 2, 4, 7, 8, 9, plus 6 because the email points to a Maharat
  destination page or signup gate and the conversion is to a paid plan. Stream 3 creative is
  conditional, it runs only if an email needs a visual and only against a real supplied,
  rights-cleared asset (open item 8). No stream 5 paid build.
- Funnel path: brief intake (1) and this strategy (2) feed copywriting (4, Arabic-first email
  copy and subject lines) and lifecycle messaging (7, the segmented flow). The flow points to
  a conversion path (6, the page or gate). Monitoring (8) reads the results, reporting (9)
  feeds the next campaign.
- Channel: email primary. WhatsApp is a later layer, out of scope here until the platform is
  confirmed.
- Cadence (proposed, ASSUMPTION, open item 6): a 4-message flow over about 2 weeks, triggered
  by entry and by engagement, primary effort on the beauty-interested segments. Confirm
  start_date, end_date, and send_window before any send.
- Hard send block: the gate and send platform is not confirmed (open item 5). Strategy and
  copy can be built and assembled, but send wiring stays blocked until the platform is named.
  Nothing sends without the human gate and Ahmed's per-send approval.

### success_metric

- Primary (proposed): paid subscription conversion rate from the flow, measured as the share
  of contacts entering the flow who start a paid plan within the send window. This is what
  stream 8 measures the campaign against, tied directly to the brief's objective of
  converting non-payers to paying subscribers. This is a lagging metric: it is the end
  outcome the flow drives toward, confirmed only after a contact subscribes.
- Proposed target (ASSUMPTION, not confirmed): a measurable target needs a number and a date.
  Proposed for Ahmed to confirm: 2 percent paid subscription conversion from contacts who
  enter the flow, measured by 2026-07-15 (about 4 weeks after a proposed late-June start and
  the 2-week send window). This number and date are an ASSUMPTION carried for review, not a
  confirmed figure (open item 4). No confirmed target is invented. Stream 8 measures against
  the number only once Ahmed confirms it at the human gate, and the date moves with the
  confirmed schedule (open item 6).
- Leading indicators (movable in flight): Masterclass plays (the hook is working) and email
  click-through (the message is earning the click). These are leading metrics the campaign can
  read and act on between send and conversion, before the lagging conversion number lands.
  Proposed leading checkpoints, also ASSUMPTION to confirm: email click-through and Masterclass
  play rate reviewed at the mid-flow point (about day 7 of the 2-week window) so the flow can
  be tuned before it closes. No confirmed leading target is invented.
- Measurement note: conversion attribution depends on the gate platform and event tracking,
  both of which depend on open item 5 (platform not confirmed). Stream 6 and the
  data-tracking-engineer resolve the event plan once the platform is named.

---

## Handoff

Emits this strategy-artifact, via the orchestrator, to copywriter-ar and copywriter-en (4)
and lifecycle-architect (7), and to creative-director (3) only if open item 8 confirms a real
supplied asset and an email needs a visual. Every downstream agent reads the open_items before
starting. status is qa-passed, the artifact may cross the boundary. Nothing sends. The human
gate surfaces all 11 open items for Ahmed before any approval.
