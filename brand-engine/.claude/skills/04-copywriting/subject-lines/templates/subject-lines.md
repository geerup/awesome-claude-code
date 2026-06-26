# Subject lines template

One set per email. Several options, exactly one flagged primary. English-first. Hold the
length and clarity bar. All example copy is illustrative only. Replace it. Do not invent
offers, prices, Skill Path titles, or instructor names.

## Subject set block

```
id:        subj-<segment>            # e.g. subj-nonpayer
email_ref: <email variant id these subjects pair with>   # e.g. email-nonpayer-v1
options:
  - text: <subject option 1>    language: ar | en    primary: true
  - text: <subject option 2>    language: ar | en    primary: false
  - text: <subject option 3>    language: ar | en    primary: false
primary:   <the text of the one option flagged primary>
preheader: <inbox-preview line, set on purpose, true to the body>   # roughly 40 to 90 characters
```

The `preheader` is a deliberate deliverable, the inbox-preview text that shows after the
subject. Set it on purpose as earned extra space, do not let body text spill into it. Keep it
true to the body, roughly 40 to 90 characters, same language as the primary subject.

## Illustrative example (Arabic, replace before use)

```
id:        subj-example
email_ref: email-example-v1
options:
  - text: مهارة جديدة تبدأ بخطوة    language: ar    primary: true
  - text: 10 دقائق تكفي للبداية      language: ar    primary: false
  - text: رحلتك تنتظرك                language: ar    primary: false
primary:   مهارة جديدة تبدأ بخطوة
preheader: ابدأ بدرس واحد قصير اليوم وكمل على راحتك
```

## Subject patterns by archetype (from the reference corpus)

Reach for the pattern that fits the email, never force one. Full method in
`context/profiles/maharat/multi-instructor-angles.md` and `skills/04-copywriting/email-copy/templates/newsletter-patterns.md`.

- Multi-instructor digest: "3 [ways or lessons] to [outcome]" (the number is the real card count,
  Western numerals, and it is the umbrella outcome itself).
- Single-instructor launch: "NEW: [outcome]" or the instructor's first-person "My class on X is
  here".
- Announcement: "Meet your new instructor: [Name]".
- Promo ladder: deadline first, saving second ("ends tonight", "ends tomorrow", "last chance",
  "extended"), only with a real deadline from the brief.
- Occasion: name the real moment and attach the class (Ramadan, Eid, National Day, back-to-school).
- Gifting: "Give [the product], get [offer]" to existing members.

## Checklist before handoff

- Several options, three to five, each a real alternative.
- Exactly one option flagged primary true.
- Mobile length: aim for roughly 30 to 40 characters, key word inside the first 30.
- Front-loaded: the angle lands in the first few words, before truncation.
- A deliberate preheader is set, roughly 40 to 90 characters, true to the body, not spilled body text.
- Each subject true to the paired email body. No clickbait, no shame.
- No em dash, no tatweel, Western numerals only.
- Empowering, never deficit-framed. No accreditation implication.
- Every offer or price traces to the brief. Nothing invented.
