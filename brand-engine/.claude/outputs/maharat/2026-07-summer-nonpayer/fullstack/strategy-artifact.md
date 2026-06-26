# Strategy Artifact: Summer of Skills, full-stack non-payer campaign

## Envelope

- campaign_id: 2026-07-summer-nonpayer
- produced_by: strategy-lead
- stream: 2 strategy and planning
- status: qa-passed
- qa:
  - skill_eval: passed (structure and completeness)
  - arabic_qa: na (artifact internal; illustrative lines flagged, not final copy)
  - english_qa: na (artifact internal; illustrative lines flagged, not final copy)
  - design_qa: na (no visual asset produced in this artifact)
  - web_design_qa: na (no web surface produced in this artifact)
  - compliance: na (artifact internal; nothing collects, sends, or publishes here)
  - brand_qa: na (artifact internal; advances to brand-qa when customer-facing copy is authored)
- entry_points: B owned audience (primary, email plus app push), A paid acquisition, C organic
  social, plus the SEO, ASO, content, and PR acquisition channels. Full stack.
- open_items: see section 6 (all carried to the human gate, none buried)
- brief_refs: campaign_id, name, owner, why_now, business_problem, prior_results, entry_points,
  objective, success_metric, key_message, audience, segments, suppression, audience_size,
  product, plan, price, promotion, offer_framing_notes, instructor roster (nameable and
  not-nameable), channels, signup_gate, gate_platform, budget, target_cpa_or_roas, start_date,
  end_date, send_window, reporting_cadence, creative_direction, tone_descriptors,
  assets_available, mandatories, constraints, open_items
- grounding_refs: CLAUDE.md; context/brand-voice.md; context/01-company-brief.md;
  context/instructors/_CATALOG.md; context/instructors/ragheb-alama/profile.md;
  context/instructors/salam-dakkak/profile.md; context/instructors/kosai-khauli/profile.md;
  context/instructors/bassam-fattouh/profile.md; context/instructors/toufic-kreidieh/profile.md;
  context/instructors/cedric-haddad/profile.md; context/instructors/elda-choucair/profile.md;
  runtime/handoff-contract.md

Locked decisions this artifact is built to (requester, session 2026-06-12):
1. Creative spine is the breadth of the instructor roster, not a single instructor. The summer
   hook is "build a real skill this summer, taught by the people who set the standard,"
   showcasing many fields on one platform.
2. Offer posture is value-led: lead with the transformation, not a discount. Any summer promo is
   ASSUMPTION; the angle works with or without one.

---

## 1. Objective

Over the summer, convert and re-engage the roughly 18,000 owned non-payers into paying Maharat
subscribers, and acquire new subscribers across paid and organic, using the breadth of the
instructor roster as the lead hook. The masterclasses are the hook, not the product sold. The
conversion is to a paid Maharat subscription that unlocks them.

The strategy reads on a single promise the offer can actually deliver: this summer you can build
a real skill, in a field you choose, taught by people who set the standard in that field, on one
platform. The promise is grounded in real, published masterclasses with cleared, page-sourced
facts, so every downstream stream can lean on it without inventing a title, a lesson, a count, or
a quote. The breadth itself is the proof: many fields, one platform, one summer.

---

## 2. Success metric

The target value is unset in the brief, so the primary target NUMBER and date are flagged
ASSUMPTION for Ahmed. The metric definition itself is proposed and stable; only the number and
the dates need confirmation.

- Primary (proposed, stable definition): paid subscription conversions attributable to the
  campaign within the confirmed flight window, counted across both engines, the owned flow
  (email plus app push) and new acquisition (paid plus organic). Attribution by signup-gate or
  owned-contact lineage to a subscription_start or purchase event. Target NUMBER and date are
  ASSUMPTION, confirm with Ahmed. This is what stream 8 measures against.
- Measurable secondaries (readable from the moment tracking is wired):
  - Owned-flow engagement: open rate and click rate on the non-payer email sequence; push open
    and tap rate on the app sequence.
  - Signup-gate completions on new acquisition (email or WhatsApp capture before the paid step).
  - Masterclass intro plays, with each class chapter 1 "The Talent" free intro as the natural
    first-touch play across fields.
  - Reactivation rate of the owned list: share of never-engaged and lapsed-engaged contacts that
    take any tracked action in the flight.
  - Cost per subscription on paid, as an efficiency read only. It becomes a hard target only once
    the budget OPEN ITEM is resolved; no absolute cost target is set here.
- Guardrail metrics: unsubscribe and spam-complaint rate on owned sends; paid frequency and
  negative-feedback rate; app-push opt-out rate.

No success-metric number is invented. Every secondary is a definition, not a value.

---

## 3. Audience segments

Owned sizes are planning estimates from the brief and the company brief; they resolve to exact
figures at send time from live data and are recorded in the lifecycle package. No size is
invented; where the brief is silent the size is marked OPEN ITEM, not guessed. Segment only on
signals the owned data actually carries; if a signal is not present at send, the relevant cut
collapses and that is flagged rather than assumed.

### 3.1 Owned non-payers, email (entry B, primary)

- Definition: registered Maharat contacts who have not purchased a subscription, reachable by
  email. Planning estimate roughly 18,000 (exact at send). Suppress all paying contacts (roughly
  5,000), unsubscribed, and hard-bounced. Suppression source to confirm (OPEN ITEM).
- Recency cut, on the signal the list carries (last-open or last-activity recency):
  - Never-engaged: registered but no recorded open or engagement since signup. The colder cut.
    Needs a re-introduction to the breadth and the format, lower-friction asks, the free intro
    chapter as the first step. Size is a share of the roughly 18,000, exact at send, not invented.
  - Lapsed-engaged: previously opened or engaged, then went quiet. The warmer cut. Can carry a
    more direct path-to-subscription message and a field-of-interest nudge where prior interest
    is known. Size is a share of the roughly 18,000, exact at send, not invented.
  - If recency is not resolvable at send, the flow runs unsplit and that is flagged to
    lifecycle-architect rather than assumed.
- Pains and gains:
  - Pain: signed up with intent to grow, never crossed into paying; "I will get to it" inertia,
    and uncertainty about which field or where to start.
  - Gain: a season with the time to actually build something, a field they choose, a recognizable
    expert in that field, and a free first chapter to try before any commitment.
- Message angle: warm re-entry, breadth-led. You are already here. This summer, pick a field and
  build a real skill, taught by the people who set the standard, starting with a free first
  lesson. Empowering, never "you stalled" or "you wasted your signup."
  Illustrative AR line (not final copy): "هذا الصيف، اختر مجالك وابدأ مهارتك الحقيقية مع نخبة من
  يصنعون المعيار. الدرس الأول مجاني."

### 3.2 Owned non-payers, app cut (entry B, app push)

- Definition: owned app users who have not purchased a subscription, reachable by app push. App
  audience size is OPEN ITEM (not in the brief or company brief). Same suppression logic as the
  email cut. Where a user maps to both email and app, lifecycle-architect dedupes and paces so
  the two channels reinforce rather than collide.
- Pains and gains: as the owned email cut, with the added gain that the app is already installed,
  so the path to the free intro chapter and to a plan is short.
- Message angle: short, timely nudges that reinforce the email flow and surface a field and its
  free intro chapter. App-push cadence is light and is ASSUMPTION (see section 6).

### 3.3 New acquisition by interest, cut by instructor domain (entry A paid, entry C organic)

- Definition: new Arabic-speaking adults, roughly 18 to 35, GCC with Saudi Arabia primary,
  reached cold on paid and organic. The breadth lets us run parallel interest cuts, each mapped
  to a real, published, cleared masterclass domain, so the creative and copy can speak to a
  specific aspiration while the platform-level promise stays "many fields, one platform":
  - Music: grounded in Ragheb Alama, 40 years in the music industry, teaching for the first time
    how to pursue a career in music (page-sourced, cleared). 14 chapters, chapter 1 free.
  - Cooking: grounded in Salam Dakkak, named Best Female Chef in MENA, chef and owner of the
    Michelin award winning restaurant Bait Maryam (page-sourced, cleared). 15 chapters, chapter 1
    free.
  - Acting: grounded in Kosai Khauli, one of the biggest names in the Arab world, teaching the
    fundamentals of acting and expression (page-sourced, cleared). 17 chapters, chapter 1 free.
  - Makeup: grounded in Bassam Fattouh, a leading and most sought-after regional makeup artist
    (page-sourced, cleared). 20 chapters, chapter 1 "The Talent" free.
  - Business: grounded in Toufic Kreidieh, who built a billion-dollar business from scratch
    (page-sourced, cleared). 11 chapters, chapter 1 free. The Brands For Less name and the
    $10,000-garage detail are verify-before-public-use and must not appear until verified.
  - Styling: grounded in Cedric Haddad, a celebrity stylist trusted by the Arab world's biggest
    stars (page-sourced, cleared). 15 chapters, chapter 1 free.
  - Marketing: grounded in Elda Choucair, one of the Arab world's most respected marketing
    leaders, with decades shaping iconic brands (page-sourced, cleared). 11 chapters, chapter 1
    free. The Omnicom, Forbes, Cannes, and the 900-plus and 1000-plus figures are
    verify-before-public-use and must not appear until verified.
  - And-more breadth: additional fields exist on the platform and may be referenced only as an
    unnamed "and more across many fields." The four non-nameable instructors (Rahma Riad, Sami Al
    Jaber, Mona Ataya, Mo Islam) sit only inside this unnamed breadth and are never named.
- Owned social base for organic is the roughly 180,000 followers (planning estimate). Paid
  interest-targeting detail and per-cut sizing are built by performance-marketer against these
  segment definitions; exact targeting and audience sizes are theirs to construct once tracking
  is wired, not invented here.
- Pains and gains:
  - Pain: wants to grow in a field they care about, currently piecing it together from scattered,
    untrusted sources with no structure and no single home.
  - Gain: a trusted, recognizable expert per field and a clear progression, all on one platform
    that fits a busy adult's summer, with a free first chapter to start.
- Message angle: aspiration plus credibility, per field, under one platform promise. Learn from
  the person who set the standard in the field you choose, and actually build the skill this
  summer. The free intro chapter is the low-friction entry to plays.

### 3.4 Retargeting (entry A paid, reinforced by lifecycle and push)

- Definition: people who engaged but did not subscribe. Includes class-page and plans-page
  visitors who did not purchase, masterclass intro players who did not convert, signup-gate
  completers (email or WhatsApp captured) who did not buy, and ad and organic engagers. Built
  from on-site and platform signals; exact audience construction and sizing belong to
  performance-marketer and data-tracking-engineer once tracking is wired. No size invented here.
- Pains and gains:
  - Pain: interested enough to look, held back at the paid step by uncertainty about value or
    about whether this is the right field for them.
  - Gain: a reminder of the concrete summer payoff and the low-risk entry, the free first chapter,
    and the breadth as reassurance that whichever field they choose, the standard is high.
- Message angle: close the loop. Reinforce the field they showed interest in, reassure on the
  free try, and surface the breadth so the choice feels safe. No price stated unless Ahmed
  confirms one and the asset requires it. No promo claimed unless Ahmed confirms one.

---

## 4. Core summer angle and offer framing

### 4.1 Core angle

"This summer, build a real skill, taught by the people who set the standard." The campaign sells
capability and choice, not correction and not a discount. The learner is not behind; they have a
season and a platform where, in whatever field they pick, the teacher is someone who set the
standard in it. Credibility comes from recognizable regional experts, each named only with
clearance and only on cleared, page-sourced facts. Proof comes from the breadth itself and from
real, published masterclasses, never from claims. Empowering throughout, never deficit-framed.

Why this angle works for this audience and this offer:
- It fits the season: summer in the GCC is a high-intent, time-rich window, a natural "use this
  season to build something" moment (brief why_now). The angle turns that latent intent into a
  concrete first step.
- It fits the owned non-payer: they already know the brand and chose not to pay. A breadth-led,
  pick-your-field re-entry answers "where do I even start" better than any single-class push, and
  it is value-led, so it does not depend on a promo the brief has not confirmed.
- It is deliverable: every field in the angle maps to a real, published class with a free first
  chapter, so the promise is honest and downstream copy never has to invent.

Cleared anchor facts the angle leans on (each from a published class page, naming
confirm-at-gate per instructor):
- Breadth across at least seven fields: music, cooking, acting, makeup, business, styling,
  marketing, each a real published masterclass.
- Every featured class opens with a free intro chapter 1 ("The Talent" where the page names it),
  a genuine, consistent low-friction try across the whole roster.
- Per-field credibility, page-sourced: Ragheb Alama, 40 years in music; Salam Dakkak, Best Female
  Chef in MENA and owner of the Michelin award winning Bait Maryam; Kosai Khauli, one of the
  biggest names in the Arab world in acting; Bassam Fattouh, a most sought-after regional makeup
  artist; Toufic Kreidieh, built a billion-dollar business from scratch; Cedric Haddad, a
  celebrity stylist trusted by the region's biggest stars; Elda Choucair, one of the Arab world's
  most respected marketing leaders.

### 4.2 Offer framing (value-led)

- The product is a Maharat subscription, with the masterclass roster as the hook. Framing leads
  with the transformation (the skill you build this summer and the field you choose), then the
  breadth and credibility, then the path, then the access. Price and promo are never the lead.
- Price: ASSUMPTION, not stated. If a price appears at all it appears only where Ahmed confirms
  the price and currency and the asset requires it. Where a public price reference already exists
  for a featured class, only that public reference may be used, and only where required.
- Promotion: ASSUMPTION. Posture is value-led by requester decision. Whether any summer trial,
  discount, or bundle exists is a separate confirmation. No promo invented or implied. All copy is
  written to work with or without a promo; the transformation carries the message either way.
- Plan: which plan(s) the campaign leads with (1, 3, or 12 month) is ASSUMPTION, confirm. Likely a
  1 or 3 month entry per the brief, but not stated until confirmed.
- The free intro chapter is the framing pivot for the top of funnel: try a free first lesson in
  the field you choose, then subscribe to keep going across all fields.
- Accreditation: never implied. Maharat completion certificates are not accredited.

Illustrative customer-facing direction, not final copy:
- AR: "صيف المهارات: اختر مجالك، وابنِ مهارة حقيقية مع نخبة من يصنعون المعيار. ابدأ بدرس أول مجاني."
- EN: "Summer of Skills: choose your field and build a real skill with the people who set the
  standard. Start with a free first lesson."

(Customer-facing copy is Arabic-first; the EN line is a parallel, not a translation afterthought.
Both are illustrative direction for stream 4, not approved copy, and pass through arabic-copy-qa
or english-copy-qa then brand-qa before any use.)

---

## 5. Channel plan and entry-point sequencing

All channels draft to approval-ready and stop. Nothing sends, publishes, or spends. The paid
split below is an allocation shape only; absolute numbers and any spend wait on the budget OPEN
ITEM. Every stream owner builds against this scope via the orchestrator.

- Owned email (entry B, primary; lifecycle-architect, stream 7): the non-payer sequence against
  the owned email segment, split by the never-engaged and lapsed-engaged recency cuts where the
  data supports it. Brief proposes a 4 to 5 message sequence over the flight, triggered by entry
  and engagement; cadence is ASSUMPTION, confirm. Suppress payers, unsubscribed, hard-bounced.
- App push (entry B, owned app users; lifecycle-architect, stream 7): a light push sequence that
  reinforces the email flow and surfaces a field and its free intro chapter. Cadence ASSUMPTION.
  App audience size OPEN ITEM. Deduped against the email cut.
- Paid (entry A; performance-marketer plans, paid-build-engineer stages): Meta and Instagram
  primary, TikTok in the mix, Google and YouTube secondary. Prospecting against the
  new-acquisition-by-interest cuts (per instructor domain) plus a retargeting layer. Owns cost
  per subscription as its efficiency read. Allocation is shape-only with no absolute numbers and
  no spend until the budget and currency are confirmed. The per-domain breakdown lets paid test
  which fields pull hardest without changing the platform-level promise.
- Organic social (entry C; organic-social): the roughly 180,000-follower base. Top-of-funnel
  reach and credibility, heroing the breadth and the free intro chapters across fields, feeding
  retargeting pools and the signup gate.
- SEO (seo-specialist): support the class and plans pages and intent around learning each field
  and the cleared instructor names, plus a "summer of skills" and seasonal-learning intent.
  Organic discovery, no spend.
- ASO (aso-specialist): align the app store listing and keywords to the breadth and to
  self-development and per-field intent, so paid and organic traffic that lands on the app
  converts. Gated publish.
- Content (content-marketer): editorial calendar mapped to the angle, the per-field cuts, and the
  SEO clusters, routed to copywriter-ar and copywriter-en. Receives the trend and seasonal signal
  (summer high-intent window) from this artifact for timing.
- PR and comms (pr-comms): earned visibility for the breadth and the cleared, named regional
  experts. No fundraising, no roadmap, no unannounced plans, no accreditation claim. Per-instructor
  naming confirm-at-gate.

Entry-point sequencing:
1. Owned first and primary. The roughly 18,000 non-payers are the warmest and lowest-cost engine;
   the email and app-push flow opens the campaign and carries it, because re-engaging known
   contacts is where the campaign's core problem sits.
2. Paid and organic open the cold funnel alongside, per-field, and build retargeting pools.
3. Retargeting and lifecycle close the loop on engagers and owned non-payers who looked but did
   not subscribe.
4. SEO, ASO, content, and PR run as always-on support that compounds the owned, paid, and organic
   push across the flight.

Entry point for the artifact envelope: B owned audience (primary), with A paid and C organic and
the acquisition channels running alongside. Full stack.

---

## 6. Open items (all carried to the human gate, none buried)

- success_metric target: the metric definition is proposed and stable; the primary target NUMBER
  and the dates are ASSUMPTION. Confirm the number and the measurement window with Ahmed.
- budget and currency: OPEN ITEM. No paid budget supplied. The paid path is an allocation shape
  only, with no absolute numbers and no spend, until Ahmed supplies a budget and currency.
- target cost per subscription or ROAS: ASSUMPTION. Not set; blocks any paid cost cap. Cost per
  subscription stays an efficiency read only until set.
- gate and push platforms: OPEN ITEM. Email, WhatsApp, and app-push platforms not confirmed.
  Block any actual send or wiring until named. See
  references/2026-06-email-whatsapp-platform-research.md.
- price and currency: ASSUMPTION. Confirm before any price appears in any asset. Only an existing
  public price reference may be used, and only where the asset requires it.
- promotion: ASSUMPTION. Confirm whether any summer trial, discount, or bundle exists. Posture is
  value-led; no promo assumed, invented, or implied. Copy works with or without one.
- plan: ASSUMPTION. Confirm which plan(s) the campaign leads with (1, 3, or 12 month).
- schedule: start_date 2026-07-01 and end_date 2026-08-31 are proposed, ASSUMPTION. Confirm.
  All dated artifacts sit inside the window once confirmed.
- cadence: owned email sequence (proposed 4 to 5 messages) and the app-push sequence cadence are
  ASSUMPTION. Confirm. Reporting cadence proposed weekly to Ahmed against the success_metric,
  ASSUMPTION, confirm.
- approved instructor imagery and assets: ASSUMPTION and OPEN ITEM per instructor. Confirm whether
  approved, rights-cleared instructor photography, class stills, and footage exist for each named
  candidate. Until confirmed, abstract brand-constant creative only. Generated instructor likeness
  is never allowed.
- app audience size: OPEN ITEM. Needed to size the app-push segment. Not in the brief or company
  brief.
- suppression source: OPEN ITEM. Confirm the source for owned-send suppression (payers,
  unsubscribed, hard-bounced) at build.
- owned email size: roughly 18,000 is a planning estimate; the exact figure resolves at send.
  Owned social roughly 180,000 is likewise a planning estimate.
- per-instructor public-naming confirmation (confirm-at-gate for each of the seven): Ragheb Alama,
  Salam Dakkak, Kosai Khauli, Bassam Fattouh, Toufic Kreidieh, Cedric Haddad, Elda Choucair. Each
  profile carries public_naming_cleared: yes with Ahmed sign-off on file (2026-06-05) and the
  catalog records "strong" launch evidence, but the catalog public-status column still reads
  unconfirmed, so every name is carried as a confirm-at-gate item and only cleared, page-sourced
  facts are referenced. The four non-nameable instructors (Rahma Riad, Sami Al Jaber, Mona Ataya,
  Mo Islam) are never named and appear only inside the unnamed "and more across many fields"
  breadth.
- verify-before-public-use facts (must not appear until verified, even where the instructor is
  nameable): Toufic Kreidieh's Brands For Less name and the $10,000-garage detail; Elda Choucair's
  Omnicom, Forbes, Cannes, and the 900-plus and 1000-plus figures.
- Saudi PDPL and data residency: OPEN ITEM. Confirm compliance and residency posture for owned
  sends, the signup gate, and tracking before any data collection, send, or wiring.
  compliance-privacy-reviewer runs on every data-touching asset.

---

## 7. Handoff note

Emitted to creative-director (3), copywriter-ar and copywriter-en (4), and lifecycle-architect
(7) via the orchestrator, and available to the paid, organic, SEO, ASO, content, and PR streams
that build on this scope. For the owned-audience flow, creative runs only where the emails and
push need visual assets. A trend and seasonal signal (summer as a high-intent, time-rich
self-development window in the GCC) is handed to content-marketer for the editorial calendar and
to lifecycle-architect for timing; it informs the angle and the timing only and licenses no
invented offer, title, instructor, or accreditation claim.

Downstream agents validate this envelope before starting: correct campaign_id, status at least
qa-passed, required body fields present, open_items read and accounted for. The instructor-naming
discipline travels with the artifact: nameable set is fixed to the seven with cleared, page-sourced
facts and a per-instructor confirm-at-gate note; the four non-nameable instructors are never named;
nothing invents a Skill Path title, a lesson, a count, a quote, a price, a promo, or a
success-metric number. On a failed skill eval this artifact returns to the strategy step with the
exact gaps before advancing. Nothing in this run sends, publishes, or spends; the swarm assembles
an approval-ready package and stops at the human gate for Ahmed.
