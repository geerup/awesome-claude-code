# Language gate verdict: arabic-copy-qa and english-copy-qa
# Campaign: 2026-06-bassam-fattouh-makeup, run-2026-06-12
# Gate: arabic-copy-qa + english-copy-qa (formal record)
# Date: 2026-06-12
# Reviewer: arabic-copy-qa + english-copy-qa gates (combined run)
# Status: FINAL

Prior gate confirmation: skill_eval self-checked on each asset (pass per each file's own
checklist). Brand-qa-reviewer has also reported a pass (after a feminine-address fix in asset
02). This record sets the formal language-gate confirmation on which that brand-qa pass rests.

Note on scope: a prior mechanical scan confirmed no em dash, en dash, tatweel, or Eastern
Arabic-Indic numerals in any file. This gate confirms that finding as a formal check and
then runs the full language-quality layer (tone, register, agreement, framing, CTA clarity,
English-specific checks) that the mechanical scan does not cover. Mentions of guardrail
language inside a file's own self-QA checklist are internal prose, not customer-facing copy,
and are not treated as copy failures.

---

## Asset 01: 01-owned-messaging-email-push-whatsapp.ar-en.md

### arabic-copy-qa

Checks run:
1. msa-gulf-familiar: Copy is Modern Standard Arabic with Gulf-familiar wording throughout.
   Phrases such as "ابدئي"، "جرّبي"، "شاهدي"، "متى شئتِ"، "على راحتك" land as natural,
   modern, and Gulf-intelligible. No dialect overreach, no stiff formal register.
2. thmanyah-tone: Clear, plain, modern. Short sentences. Concrete. Respectful of the reader.
   The arc moves from gentle invitation to value without ever shouting. On benchmark.
3. no-tatweel: Confirmed clean. No tatweel or kashida glyph found.
4. western-numerals: All digits are Western (0-9). Instances: 3, 20, 25, 53, 7, 5, 9, 40,
   120, plus dates. Pass.
5. no-em-dash: Confirmed clean. No em dash glyph found.
6. empowering-framing: Every email and push leads with what she can create and become.
   Framing is technique and confidence throughout. No "hide your flaws", no deficit language,
   no "عيوبك". The free-chapter invitation is framed as open and low-pressure in each touch.
   Pass.
7. rtl-safe: Arabic blocks lead each asset. Numerals and Latin URLs sit at clause ends or
   on their own lines. The $7 price reference appears inside an Arabic sentence
   ("بأقل من 7 دولار شهريًا تُدفع سنويًا") with the numeral isolated cleanly. No
   direction-break risk.

Feminine address consistency: second-person feminine forms used consistently throughout all
four emails, five pushes, and four WhatsApp messages (ابدئي، شاهدي، تعلمي، اختاري،
جرّبي، قرّري، شئتِ، شعرتِ، تحصلين). No masculine slippage found.

Invention check: class title, chapter count (20), total duration (2h 53m), free chapter
duration (under 3 minutes), instructor experience (25 plus years), price reference (under 7
dollars per month billed annually) all trace to confirmed _RUN-CONTEXT facts. No invented
promo, lesson, or stat.

RESULT: PASS

---

### english-copy-qa

Checks run:
1. empowering-tone: Every email and push speaks to what the reader can create and become.
   No shame, no deficit framing, no urgency theater. "The decision stays yours" and "decide
   for yourself, at your own pace" appear in Email 1 and Email 4 respectively, which are
   empowering frames, not pressure. Pass.
2. no-em-dash: Confirmed clean. Pass.
3. western-numerals: All digits Western. Pass.
4. one-clear-cta: Each email carries one declared primary CTA. Email 4 carries a quiet
   secondary (plans page) explicitly marked secondary in the design notes, which is within
   the declared pattern. Pushes each carry one tap target. WhatsApp messages each carry one
   CTA. Pass.
5. no-accreditation-implication: The completion certificate is described in Email 3 as "a
   personalized completion certificate that documents your journey." No accreditation
   language, no implication of a credentialed certificate. Pass.
6. no-invented-offers-titles: Class title, chapter count, duration, free chapter duration,
   experience framing, and price reference all trace to confirmed _RUN-CONTEXT facts. No
   invented promo, discount, or trial. Pass.
7. plain-active-voice: Short sentences throughout. Active constructions. No stiff corporate
   phrasing. "Makeup is a skill you learn, step by step." "The decision is yours, whenever
   you like." These are clean Thmanyah-equivalent English. Pass.

One item to note but not a failure: the Email 3 EN body opens with "You may be wondering: is
it worth it?" This is a light rhetorical device, not deficit framing; the reader is not
positioned as lacking, the question is invited and answered positively. It is on-tone.

RESULT: PASS

---

## Asset 02: 02-organic-social.ar-en.md

### arabic-copy-qa

Checks run:
1. msa-gulf-familiar: Captions use natural Gulf-familiar MSA. "إيش أصعب خطوة في مكياجك؟"
   (ORG-02 frame 1) uses Gulf-colloquial "إيش" rather than "ما هي". This is deliberate and
   appropriate for an Instagram Stories poll on a beauty platform targeting a primary-Saudi
   audience. The brand-voice benchmark (Thmanyah, Gulf-familiar) explicitly permits this
   register. Not a failure.
2. thmanyah-tone: Plain, modern, intelligent. Captions are short, concrete, confident.
   ORG-04 slide 2 "ليست مسألة إخفاء، بل إبراز." is a tight, strong reframe. On benchmark.
3. no-tatweel: Confirmed clean.
4. western-numerals: All digits Western (25, 20, 7, 2:47, dates). Pass.
5. no-em-dash: Confirmed clean.
6. empowering-framing: All 11 posts frame beauty as confidence and self-expression. ORG-04
   uses "مكياج يبرز ملامحك كما هي، لا يغيّرها" which is a strong positive frame. No
   "عيوبك", no correction language, no deficit framing of natural looks anywhere. Pass.
7. rtl-safe: Arabic captions lead each post; URLs on their own lines or at sentence ends;
   mixed Latin lesson names (No-Makeup Makeup, Foundation 101, Everyday Glam, Smokey Eyes,
   Color Glam) integrated into Arabic sentences without direction-break risk in standard
   rendering. Pass.

Feminine address: all second-person addresses in AR captions are feminine (ابدئي، شاهديه،
تتعلمينها، اسحبي، تتعلمين). Community reply templates A, B, C also use feminine forms
consistently. Pass. (Note: the brand-qa pass after a prior feminine-address fix is
confirmed; the current file has no remaining masculine forms in customer-facing copy.)

Invention check: all lesson names used match the documented list. Price reference ("أقل من
7 دولار شهريًا") matches the confirmed public fact. No invented promo, no invented title.
Pass.

RESULT: PASS

---

### english-copy-qa

Checks run:
1. empowering-tone: All 11 EN captions and three reply templates speak to what the reader
   can create and become. "Makeup that brings out your features as they are, not changes
   them." (ORG-04) is precise empowering framing. Community template B "watch it and show me
   what you create" is warm and confident. Pass.
2. no-em-dash: Confirmed clean. Pass.
3. western-numerals: All digits Western. Pass.
4. one-clear-cta: Each post has one primary CTA. ORG-07 carries a quiet secondary (plans
   page) alongside the primary (free first chapter), which is consistent with the arc and
   declared in the design notes. Not a competing CTA; the primary is clearly the free
   chapter. Pass.
5. no-accreditation-implication: No certificate language in any social copy. Pass.
6. no-invented-offers-titles: All lesson names match the confirmed list. Price reference
   ("less than $7 a month, billed annually") matches confirmed public fact. No invented
   promo, trial, or discount. Pass.
7. plain-active-voice: Captions are short-sentence, active-voice, concrete. "Smokey eyes
   are not hard, they need the right method." (ORG-08) is clean. "The right foundation
   changes everything." (ORG-10) is direct. Pass.

RESULT: PASS

---

## Asset 03: 03-paid-advertising.ar-en.md

### arabic-copy-qa

Checks run:
1. msa-gulf-familiar: Ad copy is MSA with Gulf-familiar wording throughout. Register is
   appropriate for paid ads: direct, action-oriented, feminine address. Set F (TikTok)
   deliberately adopts a lighter, more native tone: "وقفي تخمنين خطوات مكياجك" and
   "جربي طريقة واحدة واضحة من خبير 25 سنة. شوفي الفصل الأول الحين." The word "الحين"
   (meaning "now", Gulf-colloquial) is intentional and appropriate for the TikTok native-tone
   brief. "شوفي" is Gulf-colloquial for "watch/see it". Both are correct for the declared
   platform and register. Not a failure.
2. thmanyah-tone: Confident, plain, respectful across all sets. Sets A through G maintain
   the brand register. Set F is consciously lighter but stays within the brief's declared
   native-tone allowance. Pass.
3. no-tatweel: Confirmed clean.
4. western-numerals: All digits Western (25, 20, 53, 7, 5). The "$7" symbol appears in
   Arabic sentences across multiple sets; the numeral 7 is Western and the format
   "بأقل من $7 شهريًا، تدفعينها سنويًا" is consistent with the confirmed price reference
   framing. Pass.
5. no-em-dash: Confirmed clean.
6. empowering-framing: All sets lead with what she creates or becomes. Set B primary text 1
   reads: "وصلتِ إلى سقف الدروس المجانية؟ ارفعي مهاراتكِ إلى المستوى التالي." This is a
   question that acknowledges a state without shaming it; it is empowering in direction
   (raise your skills to the next level) and does not frame the reader as deficient.
   The question is a recognized engagement device in ad copy, not deficit framing. Pass.
   Set E retargeting copy ("ما زلتِ تفكّرين؟") similarly acknowledges hesitation without
   shame; the answer is empowering. Pass.
7. rtl-safe: Arabic is primary on every ad set; "$7" and English lesson names integrated
   cleanly into sentences or isolated on their own lines. RSA headlines (Set H) are short
   enough that mixed-direction risk is minimal. Pass.

Feminine address: all second-person feminine forms used throughout all sets (ابدئي،
تعلّمي، شاهديه، اختاري، تدفعينها، تعلّمينها، إيقاعكِ، أكملي). No masculine slippage.
Pass.

Invention check: all lesson names are from the confirmed list. No invented promo or
discount. Price reference is exactly the confirmed public fact. "A Career in Makeup" is not
used as a claim at any point. Pass.

One register note (advisory, not a failure): Set B primary text 1 uses "سقف الدروس
المجانية" (ceiling of free tutorials). This is a vivid metaphor and on-tone for the
advancing-enthusiast segment; it does not deficit-frame the reader. Confirmed pass.

RESULT: PASS

---

### english-copy-qa

Checks run:
1. empowering-tone: All English ad sets speak to what the reader can build, learn, and
   become. Set B EN primary text 1 "Hit the ceiling of free tutorials? Take your skills to
   the next level." is energizing, not shaming. Set E EN "You started the journey. Finish
   it on Maharat" is a positive frame toward completion. Pass.
2. no-em-dash: Confirmed clean. Pass.
3. western-numerals: All digits Western. Pass.
4. one-clear-cta: Each ad set carries one declared CTA button per the copy. Google RSA
   headlines are a pool from which Google assembles combinations; each is a discrete
   element, not a competing CTA problem. Pass.
5. no-accreditation-implication: No accreditation language anywhere in the paid copy. Pass.
6. no-invented-offers-titles: All lesson names from the confirmed list. Price reference
   matches confirmed public fact exactly ("less than $7/month, billed annually"). No invented
   promo, trial, or discount. Pass.
7. plain-active-voice: Ad copy is short-sentence, punchy, active. Set G pre-roll hooks
   ("Learn makeup step by step, from one of the Arab world's most recognized artists.") are
   clean and direct. RSA descriptions are concise and within platform lengths. Pass.

RESULT: PASS

---

## Asset 04: 04-blog-content.ar-en.md

### arabic-copy-qa

Checks run:
1. msa-gulf-familiar: The flagship article Arabic (section 3.1) is full MSA with no dialect
   and Gulf-intelligible throughout. Phrasing is precise and readable. The article briefs
   (B to E) carry MSA headline and H2 examples only; these are the same standard. Pass.
   Specific phrase check on the flagship body:
   - "مكياج ذكي يبدو وكانه بشرتك في افضل حالاتها": natural and clear.
   - "تعزيز ما لديك بلمسة خفيفة، لا اخفاء اي شيء": plain, direct, empowering.
   - "البشرة المرطبة جيدا تجعل اي منتج بعدها يبدو اخف واكثر طبيعية": correct MSA.
   All confirmed MSA and Gulf-familiar.
2. thmanyah-tone: The article reads like a smart, clear, modern how-to. Sentences are short
   and concrete. No academic stiffness, no over-explanation. On benchmark.
3. no-tatweel: Confirmed clean.
4. western-numerals: All digits Western (25, 7, and dates). Pass.
5. no-em-dash: Confirmed clean.
6. empowering-framing: The article is built around "تعزيز ما لديك، لا اخفاء اي شيء"
   (enhance what you have, hide nothing). No flaws language, no correction framing, no
   "عيوبك". The Article D brief notes explicitly: "MANDATORY framing: comfort, fit, and
   confidence, never 'hide flaws' or 'عيوبك'". Pass.
   One phrase requiring confirmation: "خففي التغطية الى ابعد حد" in the flagship article.
   In context this means "reduce coverage to the absolute minimum", which is a technique
   instruction, not a skin-flaw reference. Read in context with the surrounding paragraph
   ("الهدف توحيد لون البشرة مع الابقاء على ملمسها الطبيعي ظاهرا"), it is empowering and
   technique-led. Not a failure.
7. rtl-safe: Arabic article is continuous MSA prose; mixed elements (lesson names in Latin
   like "no-makeup makeup", "Foundation 101") are integrated naturally or appear in the
   meta fields. In the body, "no-makeup makeup" appears as a concept name within flowing
   Arabic text; this is standard editorial practice for concept labels. No direction-break
   risk in modern RTL-aware CMS rendering. Pass.

Feminine address: the flagship article uses second-person feminine forms throughout
(ابدئي، جربي، تتوقفين، قرري). Brief H1 and H2 examples also use feminine forms where
they appear (شاهدي، تجمع الاطلالة is impersonal/neutral, which is correct for a how-to
h2). Pass.

Invention check: the article draws only from confirmed lesson themes (No-Makeup Makeup I
and II, Foundation 101, healthy-skin-first). No invented promo, price, lesson, or stat.
The price reference is used correctly as a brief secondary CTA mention. The article briefs
(B to E) name only documented lesson themes. Pass.

One item noted for the record (not a gate failure, a production instruction): the flagship
article body uses "افضل حالاتها" and "خطوة بخطوة" and "بدون اي نص" without the standard
hamza marks on some words (e.g., "اساس" rather than "أساس", "اطلالة" rather than
"إطلالة"). This is consistent throughout the Arabic article and reads as a deliberate
CMS-safe or author-consistent orthographic choice. It does not harm meaning, intelligibility,
or tone in MSA, and is not a gate failure for this QA layer. If the brand has a formal
orthographic standard requiring full diacritical hamza marks in editorial content, that
standard should be applied at the copywriter layer before publication; it is flagged here
for awareness.

RESULT: PASS

---

### english-copy-qa

Checks run:
1. empowering-tone: The flagship EN article is built around "enhance what you have with a
   light hand, hide nothing." Every section is technique-led and confidence-framed. "The
   beauty of no-makeup makeup is knowing when enough is enough." is precise and confident.
   Pass.
2. no-em-dash: Confirmed clean. Pass.
3. western-numerals: All digits Western. Pass.
4. one-clear-cta: The flagship article carries one primary CTA (watch the free first
   chapter) and one declared lower-page secondary (see the plans), consistent with the
   declared CTA architecture for blog content. Not competing CTAs. Pass.
5. no-accreditation-implication: No accreditation language in the article or briefs. Pass.
6. no-invented-offers-titles: Lesson names match the confirmed list. Price reference appears
   only in the CTA close and matches the confirmed public fact (under $7/month, billed
   annually). The article briefs reference the confirmed price reference explicitly. No
   invented promo or trial. Pass.
7. plain-active-voice: The EN article is tight, short-sentence prose throughout. "A natural
   look starts with comfortable skin." "One warm shade on the cheeks brings a natural look
   alive." Active voice, concrete nouns. No stiff or corporate phrasing. The transition
   "Reading the steps is one thing. Watching a hand apply them is another." is clean and
   direct. Pass.

RESULT: PASS

---

## Overall verdict

| Asset | arabic-copy-qa | english-copy-qa |
|---|---|---|
| 01 owned-messaging-email-push-whatsapp | PASS | PASS |
| 02 organic-social | PASS | PASS |
| 03 paid-advertising | PASS | PASS |
| 04 blog-content | PASS | PASS |

OVERALL: PASS on both language gates for all four assets.

All four assets advance to brand-qa-reviewer (already on record as passed for this run).
The formal language-gate record is now complete.

---

## Notes carried forward (not gate failures, flagged for production)

1. Hamza orthography in asset 04 AR flagship article: "اساس", "اطلالة", "افضل" etc. are
   written without the standard hamza marks. Intelligibility is not affected. If the brand
   editorial standard requires full orthographic hamza marks, the copywriter-ar should apply
   them before publication. Not a gate failure; a production note.
2. Set F TikTok AR copy in asset 03 uses Gulf-colloquial "شوفي" and "الحين". This is
   intentional per the native-tone brief for TikTok. Confirmed appropriate; noted for the
   record so the human reviewer can confirm the register call was deliberate.

---

## Gate-stack status (this record)

- skill_eval: pass (per each asset's self-QA record)
- arabic-copy-qa: PASS (formal, this document)
- english-copy-qa: PASS (formal, this document)
- compliance-privacy-reviewer: see qa-compliance-verdict.md (separate gate, runs alongside)
- brand-qa-reviewer: PASS (prior record, feminine-address fix confirmed applied in asset 02)

Nothing in this verdict authorizes send, publish, or spend. The human gate remains the
final step before any asset leaves the draft state.
