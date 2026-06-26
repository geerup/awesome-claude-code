# Email patterns: borrowed from MasterClass, adapted for Maharat (mined)

Source: [Newsletter Learnings](https://docs.google.com/document/d/1_XmS_NBqpfsP-QMztpMCkD-2vgtbj9MTRoFct4VSGos/edit)
(Dec 2023), the team's own study of MasterClass newsletters. Extracted 2026-06-04.
Borrow-before-inventing in action: these are proven structures; the engine renders
them English-first under the house rules. Drop-in for the real repo's email-copy skill.

Upgraded 2026-06-19 by a primary-source teardown of 39 live MasterClass sends
(`references/2026-06-masterclass-multiinstructor-teardown.md`). That teardown turns the thin
"Promotional" type below into a full, build-ready capability: the multi-instructor angle method
(`context/profiles/maharat/multi-instructor-angles.md`), the PROMOTION lifecycle pattern with an urgency ladder
(`skills/07-lifecycle-messaging/promo-sequence/`), and three build modules (LessonCardGrid,
IssueIndex, MemberWin in `context/profiles/maharat/email-design-system.md`). Use those for any multi-instructor or
catalog email; this file remains the quick map of the five types.

## The five email types and their structure

1. Class recall (re-engage around an existing class): dated visual featuring the
   instructor; instructor quote then CTA; class topics, each with its own CTA;
   instructor tips.
2. Class announcement: subject "Meet your new instructor"; open on a big statement
   with the instructor's picture, then CTA; short class brief; what you will learn.
3. Teaser: photos of current instructors then "guess who is next"; catalog-style big
   statements over class imagery, always with a CTA.
4. Pre-launch: RSVP mechanic with a hook (a chance to ask the instructor a question).
5. Promotional: urgency subject lines (ends today, ending soon, save up to X percent);
   occasion framing in the subject; the promotion bolded and unmissable; a short
   blurb; multiple classes each with a CTA; close on a CTA. This is the multi-instructor
   format: build the body as a themed digest (a hero umbrella outcome, a LessonCardGrid of
   instructor cards, an optional IssueIndex, a MemberWin) per
   `context/profiles/maharat/multi-instructor-angles.md`, and sequence it as the PROMOTION pattern
   (`skills/07-lifecycle-messaging/promo-sequence/`). One primary CTA, per-card links quiet
   secondaries.

## Single-instructor launch templates (verified structures from the 2026-06-19 corpus)

Three single-instructor shapes recur often enough to template. Each is an archetype in the
`/email-mockup` command (`commands/email-mockup.md`); the copy comes from the instructor pack and
`voice.md`, never invented.

1. Personal-voice launch (the strongest). The instructor speaks in first person: "Dear members,"
   a short, warm letter in their own voice about why they made the class and what the reader will
   gain, signed with the instructor's name and a one-line credential, one WATCH NOW CTA. Subjects
   like "My class on X is here." Module order: BodyCopy (the letter, multi-paragraph), BodyCopy
   (the signature line), the one CTA. Pairs directly with the instructor `voice.md`.
2. Meet-the-instructor announcement. An instructor quote as the preheader, a hero, a one-line
   benefit, then "Here is what you will learn to do" as a short ListBlock of outcomes, one CTA.
   Subject "Meet your new instructor: [Name]". Module order: BodyCopy (benefit), ListBlock (the
   outcomes), the one CTA.
3. Activation nudge. For an enrolled member who has not started: "Start your session with [Name]
   now", one CTA, no stacked pitch. This is an onboarding or activation touch (stream 7), not a
   launch.

## Subject-line patterns worth keeping
- Multi-instructor digest: "3 [ways or lessons] to [outcome]" (the number is the real card count).
- Launch: meet your new instructor.
- Post-launch personal-voice: "My class on X is here" (the instructor speaks, first person).
- Urgency: deadline first, saving second (the promo ladder: starts now, ends tomorrow, ends
  tonight, extended, last chance).
- Occasion: name the moment, attach the class (their examples span Valentine's, New Year,
  Black Friday, Cyber Monday, Thanksgiving, Giving Tuesday; Maharat's equivalents: Ramadan, Eid,
  back-to-school, National Day, a New Year reset).
- Gifting: "Give [the product], get [offer]" to existing members.

## Maharat adaptations (apply on every render)
- English-first MSA, Western numerals, no em dashes, empowering framing.
- Instructor claims pass the relevant pack's claims table (context/profiles/maharat/instructor-packs).
- One primary CTA per email in the non-payer flow (the SOP rule); the multi-CTA
  catalog pattern is for newsletter formats, not the conversion arc.
- Offers and percentages are brief inputs, never invented; "up to X percent" renders
  only from the active brief.
- The personal-voice subject pattern pairs naturally with instructor voice.md files.
