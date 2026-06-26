# Additional English copy: Summer of Skills, full-stack non-payer campaign
# Deferred deliverables: onboarding, organic gaps, gate consent, press release

## Envelope

- campaign_id: 2026-07-summer-nonpayer
- produced_by: copywriter-en
- stream: 4 copywriting (English variants)
- status: draft
- qa:
  - skill_eval: self-run pass. Structure, completeness, all four deferred sections authored.
    All ids match the brief and the organic-package gap table. No invented values.
  - arabic_qa: na (English copy only; arabic-copy-qa owns the AR canonical)
  - english_qa: pass (re-run post brand-qa fix, 2026-06-12). Mechanical checks: no em
    dashes; Western numerals only; one CTA per asset; no invented value; empowering
    throughout. Fix applied: SOCIAL-S11 Slide 2 on-screen text rewritten from
    deficit-framed "The problem is never motivation" to capability-led "You already know
    what you want to build" per brand-qa fix list. Organic gap caption ids reconciled to
    AR canonical: SOCIAL-S-ACT to SOCIAL-S9, SOCIAL-S-POLL to SOCIAL-S10,
    SOCIAL-S-FREE to SOCIAL-S11. All references and fills updated. No other failures.
  - brand_qa: pending (submit after english_qa pass recorded here; routes to brand-qa-reviewer)
  - compliance: pending for gate-consent sections (GATE-CONSENT-EMAIL-EN and
    GATE-CONSENT-WHATSAPP-EN must pass compliance-privacy-reviewer before any live gate
    deploys; routes to compliance-privacy-reviewer alongside copywriter-ar consent drafts)
- open_items:
  - AR canonical not yet written: additional-copy.ar.md does not exist as of 2026-06-12.
    This EN file mirrors the structure and ids established in the pr-package.md brief and
    the organic-package.md gap table. When copywriter-ar produces additional-copy.ar.md,
    the ids and section structure here must be cross-checked for alignment. AR is canonical.
  - Onboarding copy (O1, O2, O3): the lifecycle-package.md section 5 notes these are not
    yet briefed and will be briefed once the onboarding SOP and subscription platform are
    confirmed. The EN copy here is drafted to the direction in that section. It is not
    executional until the onboarding SOP, platform, and Ahmed's per-sequence approval are
    confirmed.
  - Organic gap captions (acting post, interactive-poll story, free-chapter story):
    organic-package.md flags these three slots as OPEN ITEM and blocks ORG-S-05, ORG-S-18
    (acting), and the T3 and T7 story posts. The EN captions here unblock the EN side.
    The AR canonical acting variant and the poll and story-sequence AR variants must also
    be produced by copywriter-ar and cleared through arabic-copy-qa and brand-qa before
    these posts are executional.
  - Gate consent, compliance: GATE-CONSENT-EMAIL-EN and GATE-CONSENT-WHATSAPP-EN are
    authored here per the direction in conversion-package.md sections 3.2 and 3.3 and the
    compliance-verdict.md open items 2 and 5. Both must pass compliance-privacy-reviewer
    and english-copy-qa before the live gate deploys. Saudi PDPL lawful basis and the live
    Maharat privacy policy URL are OPEN ITEM (compliance-verdict.md open items 7 and 9);
    the consent line carries a placeholder URL until confirmed.
  - WhatsApp consent logging mechanism: compliance-verdict.md open item 2 flags this as
    not yet designed. The consent text here is correct in intent; the logging and timestamp
    record mechanism must be designed and reviewed by compliance-privacy-reviewer separately.
  - Press release (PR-RELEASE-EN): quote placeholder included per pr-package.md brief.
    No quote is authored or attributed. The placeholder must be replaced with an
    approved quote before distribution. Co-founder naming (Arman Khederlarian and Bassem
    Jamaleddine) is included but flagged confirm-at-gate per pr-package.md open item 8.
    Media contact line is a placeholder; must be replaced before distribution.
    Platform facts (200,000-plus social followers, 1.5 million-plus unique site visitors,
    users in 100-plus countries) are sourced from the catalog (Entrepreneur, August 2025)
    and marked confirm-at-gate per strategy-artifact section 6.
  - All seven instructor names across all four sections: confirm-at-gate.
  - Price, plan, promotion: not stated anywhere in this package. All ASSUMPTION.
  - Rights-cleared instructor photography: OPEN ITEM per instructor.
  - Campaign start date 2026-07-01, end date 2026-08-31: ASSUMPTION.
- brief_refs: campaign_id, objective, audience (segments per strategy-artifact 3.1 to 3.4),
  product, plan (ASSUMPTION), price (ASSUMPTION, not stated), promotion (ASSUMPTION, not
  stated), offer_framing_notes, instructor roster (nameable 7 confirm-at-gate, non-nameable
  4 never named), channels, start_date (ASSUMPTION), end_date (ASSUMPTION),
  lifecycle-package.md section 5 (onboarding direction), organic-package.md section 4 and
  6 (caption gaps), conversion-package.md sections 3.2 and 3.3 (consent direction),
  compliance-verdict.md open items 2 and 5, pr-package.md section 3 (press release brief),
  context/instructors/_CATALOG.md (public press facts), context/instructors/kosai-khauli/
  profile.md (acting field cleared facts)

---

## How to read this file

This file contains four sections, each covering one deferred copy deliverable. Each section
is structured to match the common copy-package envelope and to align with the AR canonical
ids. The AR canonical (additional-copy.ar.md) is the structural reference; this EN file is
the English author, not a translation.

No em dashes anywhere. Western numerals only. One clear CTA per asset. No invented price,
promo, plan, lesson title, chapter count, quote, or instructor claim beyond cleared
page-sourced facts.

---

## Section 1: Onboarding sequence EN (ONBOARD-O1, ONBOARD-O2, ONBOARD-O3)

Audience: new Maharat subscribers who converted during the Summer of Skills campaign.
These contacts exited the non-payer flow on subscription_start and enter the post-conversion
onboarding sequence. Timing, platform, and cadence are ASSUMPTION per lifecycle-package.md
section 5. These messages are not executional until the onboarding SOP and subscription
platform are confirmed and Ahmed approves the sequence.

All three messages: no price in body, no promo assumed, no accreditation. Empowering,
skills-momentum framing. No em dashes.

---

### ONBOARD-O1: Welcome and orient (immediate on subscription_start)

- id: ONBOARD-O1
- segment: new Summer of Skills subscribers
- trigger: subscription_start event confirmed
- timing: immediate on subscription_start
- language: en
- fills: onboarding O1 EN subject lines, preheader, body, CTA

Subject lines (choose one at build):
- PRIMARY: You are in. Your first session starts now. (41 chars)
- ALT-1: Welcome to Maharat. Pick your field and begin. (46 chars)

Preheader: Every masterclass across every field is now open to you. Start with the one you
chose.

Body:
Hello,

You are now a Maharat subscriber. Every masterclass on the platform is yours, across all
seven fields and beyond.

Start where you left off. Pick the field that brought you here and open the first full
lesson. Music, cooking, acting, makeup, business, styling, marketing, and more are all
waiting.

One subscription, one summer, one real skill. This is the beginning.

CTA: Go to your masterclass

CTA landing: In-app or web class browse screen, or the field and chapter the subscriber
selected at gate entry (routed via the field_id from the lifecycle handoff payload). No
personal or sensitive data in the URL.

Notes: No price referenced. No plan length stated. This is a welcome, not a receipt.
Warm and empowering: "you are in," not "thank you for your purchase." The CTA routes to
the content, not back to a plans page. All instructor names omitted from this message;
the breadth-led subject lines and preheader carry the promise.

---

### ONBOARD-O2: First progress nudge (day 3 after subscription)

- id: ONBOARD-O2
- segment: new Summer of Skills subscribers, day 3 post-conversion
- trigger: day 3 after subscription_start
- timing: 3 days after subscription_start
- language: en
- fills: onboarding O2 EN subject lines, preheader, body, CTA

Subject lines (choose one at build):
- PRIMARY: Three days in. How is your skill coming along? (48 chars)
- ALT-1: Keep the momentum going. Your next lesson is ready. (51 chars)

Preheader: One short session a day builds more than you think. Open the next chapter now.

Body:
Hello,

Three days ago, you chose a field and started building a real skill. That is the hardest
step.

If you have already started a lesson, open the next chapter. If you have not yet begun,
today is a good day for it.

The summer is long enough to build something real. One lesson at a time.

CTA: Open your next lesson

CTA landing: The subscriber's in-progress class if a session event was recorded, otherwise
the class browse screen for their chosen field. No personal or sensitive data in the URL.
Field-personalized deep link if the platform supports it (field_id from the handoff payload).

Notes: No price. No plan reference. If first-session data is not available from the platform,
the copy reads naturally as an invitation to start. Empowering, not a nudge that implies the
subscriber wasted time. The body does not say "you have not started yet."

---

### ONBOARD-O3: Habit formation and breadth discovery (day 7 after subscription)

- id: ONBOARD-O3
- segment: new Summer of Skills subscribers, day 7 post-conversion
- trigger: day 7 after subscription_start
- timing: 7 days after subscription_start
- language: en
- fills: onboarding O3 EN subject lines, preheader, body, CTA

Subject lines (choose one at build):
- PRIMARY: One week. One skill taking shape. What is next? (47 chars)
- ALT-1: You have seven fields on one platform. Explore them. (51 chars)

Preheader: A short session every day is how a real skill gets built. Plus, there is more to
explore across every field on Maharat.

Body:
Hello,

One week in, and your skill is already taking shape.

A consistent, short session each day is how real progress gets made. You do not need long
blocks of time. The craft you are building responds to regular contact.

And when you are ready to look beyond your first field, the full roster is right here.
Seven fields, seven experts, every lesson unlocked. Music, cooking, acting, makeup,
business, styling, marketing, and more.

This summer, you have time. Use it.

CTA: Explore the full roster

CTA landing: Maharat class browse or Summer of Skills roster screen. No personal or
sensitive data in the URL.

Notes: No price. No plan reference. No accreditation. The "and more" breadth line
references unnamed additional fields; the four non-nameable instructors are never named.
All seven named fields are referenced as field labels only, not instructor names, so
confirm-at-gate discipline is not triggered in this breadth line. Warm and practical,
never deficit-framed.

---

## Section 2: Organic gap captions EN (acting post, interactive-poll story,
## free-chapter entry story)

These three captions fill the gaps identified in organic-package.md section 6 and the
open-item table in the AR copy status notes. The organic-package.md blocks ORG-S-05 and
ORG-S-18 (acting field, Kosai Khauli) and flags no dedicated AR poll or free-chapter story
variant exists. The EN captions here are authored to fill those slots on the EN side.

All three carry confirm-at-gate for Kosai Khauli's name. All cleared facts are
page-sourced from kosai-khauli/profile.md and strategy-artifact section 3.3. No chapter
names are used from Kosai Khauli's class (cleared in profile.md but not in scope for
caption copy per the organic brief). No invented facts.

---

### SOCIAL-S9: Acting field caption (Kosai Khauli, T2-ACT, ORG-S-05 and ORG-S-18)

- id: SOCIAL-S9
- segment: acting and performance interest, cold and warm audience
- format: IG feed (4:5) for ORG-S-05, IG Reels and TikTok (9:16) for ORG-S-18
- timing: ORG-S-05 proposed 2026-07-07, ORG-S-18 proposed 2026-08-14 (both ASSUMPTION)
- language: en
- fills: organic-package.md ORG-S-05 and ORG-S-18 EN caption slots, theme T2-ACT
- asset ref: ORG-S-05 uses C2/AB2 acting variant (per-field abstract card, acting icon);
  ORG-S-18 uses C6/AB8 multi-field breadth reel, cut C

Caption:
Acting is a craft. It can be taught.

Kosai Khauli, one of the biggest names in the Arab world, is teaching the fundamentals
of acting and expression on Maharat. The real work behind the performance, shared clearly,
step by step.

The first lesson is free.

CTA: Start the masterclass on Maharat. [Link in bio]

CTA landing: Kosai Khauli class page at maharat.com/en/class/acting/kosai-khauli-teaches-acting.
No personal or sensitive data in the URL.

Notes: "One of the biggest names in the Arab world" and "fundamentals of acting and
expression" are page-sourced and cleared per kosai-khauli/profile.md and strategy-artifact
section 3.3. Instructor name is confirm-at-gate. Rights-cleared photography is OPEN ITEM;
the abstract brand-constant creative (C2/AB2 acting variant) is the confirmed fallback.
The Reel version (ORG-S-18) uses the same caption; only the asset format differs. No
em dashes. One CTA.

---

### SOCIAL-S10: Interactive poll story caption (T7, ORG-S-02 and ORG-S-16)

- id: SOCIAL-S10
- segment: cold and warm audience, all interests, participatory
- format: IG Story and Snapchat Story (9:16) with interactive poll sticker
- timing: ORG-S-02 proposed 2026-07-01, ORG-S-16 proposed 2026-08-07 (both ASSUMPTION)
- language: en
- fills: organic-package.md ORG-S-02 and ORG-S-16 EN caption and on-screen text slots,
  theme T7
- asset ref: C7/AB7 (campaign identity thematic still, 9:16 Story format)

On-screen headline (displayed on the Story):
Which skill do you want to build this summer?

Poll options (sticker, no options baked into the art):
[Poll sticker placed by social team at publish. Options: Music, Cooking, Acting, Makeup,
Business, Styling, Marketing. The "and more" breadth is represented by the platform breadth
prompt in the follow-up story below.]

Caption (accompanying the Story post where visible, for accessibility and cross-platform use):
Which skill are you building this summer?

Pick your field. Maharat has a masterclass for each one, taught by an expert who set the
standard in it. And the first lesson in any of them is free.

[Poll: Music, Cooking, Acting, Makeup, Business, Styling, Marketing]

Follow-up story: the most-answered field gets a follow-up story spotlighting that
masterclass and its free first lesson. See note below.

CTA (on follow-up slide or swipe-up, where available): Start your free lesson on Maharat.
[Link sticker]

CTA landing: Summer of Skills landing page or Maharat homepage. No personal or sensitive
data in the URL.

Notes: No instructor is named in the poll story itself. The goal is signal and warm audience
data, not conversion at this step. No hard CTA on the poll slide; the CTA appears only on
the follow-up story. The poll options are text-only, applied as a sticker by the social team
at publish: nothing is baked into the art. Warm and participatory register. The follow-up
story after the poll closes should be produced by the social team using the nearest matching
SOCIAL-S caption for the winning field (e.g., SOCIAL-S3 for music, SOCIAL-S4 for cooking,
etc.). No em dashes. One CTA per slide.

---

### SOCIAL-S11: Free-chapter entry story sequence (T3, ORG-S-11)

- id: SOCIAL-S11
- segment: cold and warm audience, any field interest, low-friction try
- format: IG Story and Snapchat Story (9:16) multi-slide sequence, with link sticker
- timing: ORG-S-11 proposed 2026-07-21 (ASSUMPTION)
- language: en
- fills: organic-package.md ORG-S-11 EN caption and on-screen script slot, theme T3
- asset ref: C4/AB4 abstract free-entry path still, 9:16 Story crop with link sticker space

Slide 1 on-screen text (hook):
There is a field you have always wanted to go deeper in.

Caption supporting text:
One summer is long enough to make real progress, if you start.

Slide 2 on-screen text (tension and resolution):
You already know what you want to build. One free lesson from someone who set the
standard in your field is where to start.

Slide 3 on-screen text (CTA):
Pick a field. Start the free first lesson. No commitment needed.

CTA: Tap to start. [Link sticker]

Full caption for accessibility:
There is a field you have always wanted to go deeper in. This summer, the path is one free
lesson away.

Maharat has masterclasses across music, cooking, acting, makeup, business, styling,
marketing, and more. Every class starts with a free first lesson. No subscription needed
to begin.

Pick your field. Start today.

CTA: Start your free first lesson on Maharat. [Link sticker routes to Summer of Skills
landing page or the Maharat field-browse screen]

CTA landing: Summer of Skills landing page or Maharat homepage. No personal or sensitive
data in the URL.

Notes: No instructor is named in this story sequence. The goal is low-friction entry to a
free lesson. The "and more" breadth line appears in the caption; the four non-nameable
instructors are never named. Empowering throughout: the reader is not behind, they simply
have not found the right starting point. The link sticker routes to the signup gate or
class browse; the exact URL is confirmed at build once the gate platform is resolved.
No em dashes. One CTA per slide.

---

## Section 3: Gate consent copy EN (GATE-CONSENT-EMAIL-EN, GATE-CONSENT-WHATSAPP-EN)

These two consent lines fill the GATE-CONSENT-EN slot in conversion-package.md section 7.
They are authored per the direction in conversion-package.md sections 3.2 and 3.3 and
the compliance-verdict.md open items 2 and 5. Both must pass compliance-privacy-reviewer
and english-copy-qa before the gate deploys. The Saudi PDPL lawful basis and the live
Maharat privacy policy URL are OPEN ITEM; the consent lines carry a placeholder URL.

The consent line must be visible before the user submits. It must not be hidden behind a
scroll or a collapsed element. This is a hard requirement confirmed in the conversion-package
and the compliance verdict.

---

### GATE-CONSENT-EMAIL-EN: Email gate consent line

- id: GATE-CONSENT-EMAIL-EN
- placement: immediately below the email input field, above the submit button, in the
  GATE-CONSENT-EN slot (conversion-package.md section 7, COMP-GATE)
- language: en
- fills: GATE-CONSENT-EN slot, email gate variant
- routes to: compliance-privacy-reviewer (review before go-live), english-copy-qa

Consent line text:
By submitting, you agree to receive messages from Maharat about the platform and your
chosen field. Maharat is the data controller. You can unsubscribe at any time using the
link in any message. [Privacy Policy]

Notes on the line:
- "Maharat is the data controller": states the data controller explicitly per conversion-
  package.md section 3.2 direction (a).
- "receive messages from Maharat about the platform and your chosen field": states the
  purpose per direction (a).
- "[Privacy Policy]": this is a hyperlinked label. The href targets the live Maharat
  privacy policy URL (OPEN ITEM: confirm and insert the live URL at build; compliance-
  privacy-reviewer must confirm the live policy covers all required elements per
  compliance-verdict.md open item 9).
- "You can unsubscribe at any time using the link in any message": states the opt-out
  mechanism per direction (c) and conversion-package.md section 3.2 direction.
- The line must be visible before the user submits, not behind a scroll or collapse.
- Typography: body-sm (0.875 rem, 400, 1.6) per conversion-package.md section 7.
- No em dashes. No invented claim. No accreditation. No price.
- Saudi PDPL lawful basis to be confirmed by compliance-privacy-reviewer and Ahmed per
  compliance-verdict.md open item 7(a). The consent line wording may require adjustment
  once the lawful basis is confirmed; this is a design-ready draft, not final.

---

### GATE-CONSENT-WHATSAPP-EN: WhatsApp gate consent line

- id: GATE-CONSENT-WHATSAPP-EN
- placement: immediately below the phone number input field, above the submit button, in
  the GATE-CONSENT-EN slot, WhatsApp gate variant (conversion-package.md section 7,
  COMP-GATE, gate variant B)
- language: en
- fills: GATE-CONSENT-EN slot, WhatsApp gate variant
- routes to: compliance-privacy-reviewer (dedicated review before go-live), english-copy-qa

Consent line text:
By submitting, you agree to receive WhatsApp messages from Maharat about the platform and
your chosen field. Maharat is the data controller. To stop messages, reply "Stop" at any
time. [Privacy Policy]

Notes on the line:
- "receive WhatsApp messages from Maharat": explicitly references WhatsApp messaging per
  conversion-package.md section 3.3 direction (a) and compliance-verdict.md open item 2.
- "Maharat is the data controller": states the data controller explicitly.
- "about the platform and your chosen field": states the purpose.
- "To stop messages, reply 'Stop' at any time": states the stop mechanism explicitly per
  conversion-package.md section 3.3 direction (b). The word "Stop" may need to match the
  exact stop keyword the WhatsApp platform enforces; confirm with compliance-privacy-reviewer
  and the platform once the WhatsApp platform is named (compliance-verdict.md open item 8).
- "[Privacy Policy]": hyperlinked label. Same href note as the email consent line above.
- The consent line must be visible before the user submits, not behind a scroll or collapse.
- This consent must be separately logged with a timestamp and consent text version at
  submission, linked to the user's record in the lifecycle platform, per conversion-package.md
  section 3.3 direction (d). The logging mechanism design is OPEN ITEM (compliance-verdict.md
  open item 2); this copy is ready once that mechanism is designed and reviewed.
- Typography: body-sm (0.875 rem, 400, 1.6).
- No em dashes. No invented claim. No accreditation. No price.
- Saudi PDPL lawful basis to be confirmed per compliance-verdict.md open item 7(a).
- Meta WhatsApp Business Policy compliance requires a separate review of the consent logging
  mechanism before the WhatsApp gate goes live.

---

## Section 4: Press release EN (PR-RELEASE-EN)

- id: PR-RELEASE-EN
- produced_by: copywriter-en
- language: en
- fills: pr-package.md press release English variant slot, section 3
- routes to: english-copy-qa first, then brand-qa-reviewer; then compliance-privacy-reviewer
  for journalist data handling; then human gate for Ahmed's distribution approval
- status: draft. Not for distribution until all gates pass and Ahmed approves.

All instructor names in this press release are confirm-at-gate per pr-package.md open item 1
and strategy-artifact section 6. The catalog public-status column reads unconfirmed for all
seven. No name is used in distributed materials until each is individually cleared at the
human gate. The draft uses the names and flags each one with [confirm-at-gate].

Verify-before-public-use facts are excluded entirely: no Brands For Less, no garage detail,
no Omnicom, no Forbes, no Cannes, no 900-plus or 1000-plus figures.

Platform reach figures (200,000-plus social followers, 1.5 million-plus unique site visitors,
users in 100-plus countries) are sourced from the catalog (Entrepreneur, August 2025) and
marked [confirm-at-gate] below.

The quote placeholder follows the pr-package.md brief. The media contact line is a
placeholder. The co-founder names are flagged confirm-at-gate per pr-package.md open item 8.

---

FOR IMMEDIATE RELEASE

[DATELINE: City, Country, Date placeholder, to be confirmed by Ahmed before distribution]

Maharat Launches Summer of Skills with Seven Masterclasses from Regional Experts,
Free First Chapter on Every Class

Seven fields. Seven recognizable regional experts. One Arabic-first platform. The first
lesson in every masterclass is free.

CITY, DATE, 2026 -- Maharat, the Arabic-first self-development platform for the Arab
world, today launches Summer of Skills (صيف المهارات), a seasonal campaign inviting
Arabic-speaking learners across the GCC and the wider Arab world to build a real skill
this summer from a roster of seven live masterclasses. The fields span music, cooking,
acting, makeup, business, styling, and marketing. Every featured masterclass opens with a
free first chapter, giving any learner an immediate, no-commitment starting point in the
field they choose.

Maharat brings together seven recognized regional experts for Summer of Skills, each
teaching a structured masterclass in their discipline. The class roster includes:
[confirm-at-gate] Ragheb Alama, who brings 40 years in the music industry to a masterclass
on building a career in music, teaching for the first time in this format;
[confirm-at-gate] Salam Dakkak, named Best Female Chef in MENA and chef and owner of the
Michelin award winning restaurant Bait Maryam, teaching Levantine home cooking;
[confirm-at-gate] Kosai Khauli, one of the biggest names in the Arab world, teaching the
fundamentals of acting and expression;
[confirm-at-gate] Bassam Fattouh, a most sought-after regional makeup artist, teaching
makeup as a structured craft;
[confirm-at-gate] Toufic Kreidieh, who built a billion-dollar business from scratch,
teaching how to build and grow a business;
[confirm-at-gate] Cedric Haddad, a celebrity stylist trusted by the Arab world's biggest
stars, teaching personal styling;
and [confirm-at-gate] Elda Choucair, one of the Arab world's most respected marketing
leaders with decades of experience shaping iconic brands and industry-defining strategies,
teaching marketing. Each class begins with a free first chapter, and the full course is
accessible via a Maharat subscription at maharat.com.

[QUOTE: SPOKESPERSON NAME, approval required before distribution]

The Summer of Skills campaign runs across Maharat's owned channels, paid platforms, and
organic social, inviting both new and returning learners to choose a field and start
building a real skill this summer. The Arabic-first platform hosts masterclasses for
Arabic-speaking adults across the GCC and beyond, covering a breadth of fields from a
single subscription. Completion certificates are issued by Maharat on course completion.
Certificates are not accredited.

About Maharat

Maharat is an Arabic-first self-development platform for the Arab world. The platform
publishes masterclasses from regional experts and offers subscription plans for
Arabic-speaking learners across the GCC and the wider Arab world. Maharat was founded in
2023 [confirm-at-gate: by Arman Khederlarian and Bassem Jamaleddine] and has attracted
[confirm-at-gate] more than 200,000 social followers and more than 1.5 million unique site
visitors, with users in more than 100 countries. Maharat issues completion certificates.
Certificates are not accredited.

Media Contact:
[MEDIA CONTACT NAME]
[MEDIA CONTACT EMAIL]

Notes on this draft:
- No price stated anywhere. Brief marks price ASSUMPTION.
- No promotion, discount, or trial stated. Brief marks promotion ASSUMPTION. If Ahmed
  confirms a summer promotion before distribution, this draft must be updated and re-routed
  through english-copy-qa and brand-qa.
- No Skill Paths, roadmap, or unannounced plans referenced.
- No fundraising, investor, or bootstrapped reference. The catalog note "initially
  bootstrapped" is excluded per the guardrail against fundraising and unannounced plans
  in customer-facing output.
- All seven instructor names are confirm-at-gate. If any name is not cleared at distribution
  time, that name is removed and replaced with a field-only descriptor (for example,
  "a celebrity stylist trusted by the Arab world's biggest stars" for styling).
- The quote placeholder is not filled. An approved quote must replace the placeholder before
  distribution.
- The dateline and distribution date must be confirmed by Ahmed before any press release
  carries a date in distributed materials.
- The media contact line is a placeholder. The approved contact must be inserted before
  distribution.
- The co-founder names are flagged confirm-at-gate. If naming is not approved, the
  boilerplate reads "founded in 2023" without naming individuals.
- Platform reach figures are sourced from the catalog (Entrepreneur, August 2025) and
  marked confirm-at-gate. If figures have been updated since August 2025, confirm the
  current verified figures before distribution.
- No em dashes anywhere in this press release. Commas, colons, and periods used
  throughout.
- Western numerals only: 200,000-plus, 1.5 million-plus, 100-plus, 40 years, 7 fields,
  all Western numerals.
- No personal or sensitive data in any URL. The destination is maharat.com (clean domain
  only).

---

## Fills and routing

### Fills map (this file)

| id | channel or asset | headline or subject or title | CTA | copy slot filled |
|---|---|---|---|---|
| ONBOARD-O1 | Lifecycle email, onboarding | You are in. Your first session starts now. (primary subject) | Go to your masterclass | Onboarding O1 EN subject, preheader, body, CTA |
| ONBOARD-O2 | Lifecycle email, onboarding | Three days in. How is your skill coming along? (primary subject) | Open your next lesson | Onboarding O2 EN subject, preheader, body, CTA |
| ONBOARD-O3 | Lifecycle email, onboarding | One week. One skill taking shape. What is next? (primary subject) | Explore the full roster | Onboarding O3 EN subject, preheader, body, CTA |
| SOCIAL-S9 | Organic social (IG feed 4:5, IG Reels 9:16, TikTok 9:16) | Acting is a craft. It can be taught. (caption opener) | Start the masterclass on Maharat | Organic ORG-S-05 and ORG-S-18 EN caption slot, T2-ACT |
| SOCIAL-S10 | Organic social (IG Story 9:16, Snapchat Story 9:16) | Which skill do you want to build this summer? (on-screen headline) | Start your free lesson on Maharat | Organic ORG-S-02 and ORG-S-16 EN caption and on-screen text slot, T7 |
| SOCIAL-S11 | Organic social (IG Story 9:16, Snapchat Story 9:16) | There is a field you have always wanted to go deeper in. (Slide 1 on-screen) | Tap to start (link sticker) | Organic ORG-S-11 EN caption and on-screen script slot, T3 |
| GATE-CONSENT-EMAIL-EN | Landing page signup gate, email variant | By submitting, you agree to receive messages from Maharat... | (submit action) | GATE-CONSENT-EN slot, email variant, COMP-GATE section 7 |
| GATE-CONSENT-WHATSAPP-EN | Landing page signup gate, WhatsApp variant | By submitting, you agree to receive WhatsApp messages from Maharat... | (submit action) | GATE-CONSENT-EN slot, WhatsApp variant, COMP-GATE section 7 |
| PR-RELEASE-EN | PR stream, press release English variant | Maharat Launches Summer of Skills with Seven Masterclasses from Regional Experts, Free First Chapter on Every Class | (media contact line, no CTA) | pr-package.md press release EN variant slot |

### Routing

- ONBOARD-O1, O2, O3: route to english-copy-qa, then brand-qa-reviewer. Not executional
  until onboarding SOP and platform confirmed and Ahmed approves the sequence. Copy is
  complete; the lifecycle-package.md section 5 governs the flow design.
- SOCIAL-S9, SOCIAL-S10, SOCIAL-S11: route to english-copy-qa, then brand-qa-
  reviewer. These EN captions unblock the EN side of ORG-S-05, ORG-S-18, ORG-S-02,
  ORG-S-16, and ORG-S-11 in the organic-package.md calendar. The corresponding AR canonical
  acting variant, poll variant, and free-chapter story variant must also be produced by
  copywriter-ar and cleared through arabic-copy-qa and brand-qa before those posts are
  executional. SOCIAL-S9 also requires rights-cleared Kosai Khauli photography (OPEN
  ITEM) or confirmed abstract brand-constant creative fallback.
- GATE-CONSENT-EMAIL-EN, GATE-CONSENT-WHATSAPP-EN: route to english-copy-qa first, then
  compliance-privacy-reviewer (dedicated review before any live gate deployment), then
  brand-qa-reviewer last. The WhatsApp consent variant also requires the WhatsApp consent
  logging mechanism to be designed and reviewed separately (compliance-verdict.md open
  item 2) before the WhatsApp gate can go live.
- PR-RELEASE-EN: route to english-copy-qa first, then brand-qa-reviewer. Then to
  compliance-privacy-reviewer for journalist data handling clearance. Then to the human
  gate for Ahmed's distribution decision. Nothing distributes without Ahmed's explicit
  per-action approval. Embargo decision (open item in pr-package.md) must be confirmed
  before any date is shared with journalists.

Nothing in this file sends, publishes, distributes, or goes live. Every item stops at the
human gate for Ahmed's per-action, per-channel sign-off. Silence is not approval.
