# copy-package: Bassam Fattouh bridal makeup, non-payer lifecycle (Arabic)

Stream 4 artifact. The Arabic email copy and subject lines for the 4-message non-payer
lifecycle flow, authored Arabic-first in the Maharat voice from the qa-passed
strategy-artifact (angle, segments, offer_framing) and the active brief. No price, promotion,
lesson lineup, duration, or instructor fact beyond the confirmed name appears anywhere.
Unconfirmed variables are marked as bracketed copy slots and listed in open_items. No em dash
glyph, no tatweel, Western numerals only, RTL-safe.

v2 update notes (changed from v1): (1) added a deliberate Arabic preheader / inbox-preview
line to every message, set on purpose as earned space in the 40 to 90 character band, true to
the body, not spilled body text; (2) rebuilt all subject options mobile-tuned toward the
30 to 40 character target band with the key word front-loaded inside the first 30; (3) applied
the now-optional copy frameworks per funnel stage (AIDA plus a 4 Us lead on the cold entry,
AIDA interest and desire plus 4 Us credible on the proof message, AIDA action plus a 4 Cs final
pass on the offer, PAS without shame on the non-opener nudge, a 4 Cs concise close on the
engaged final); (4) carried a winback-oriented note on the M4 non-opener variant for the
beauty-interested-lapsed and dormant-nonpayers segments, kept inside the existing branch rather
than adding a fifth message, to avoid bloat. Structure (4 messages plus the engaged versus
non-opener M4 branch) is unchanged. No new facts: same confirmed title and instructor only,
all price, plan, promotion, lineup variables stay marked placeholders.

---

## Common envelope

- campaign_id: 2026-06-bassam-fattouh-bridal-makeup
- produced_by: copywriter-ar
- stream: 4 copywriting
- status: draft (skill eval and arabic-copy-qa self-check passed; awaits brand-qa-reviewer and
  compliance-privacy-reviewer before status moves to qa-passed)
- qa:
  - skill_eval: pass (email-copy and subject-lines checks: one clear CTA per email, mobile
    subject length with the key word in the first 30 aimed at the 30 to 40 band, deliberate
    preheader present in the 40 to 90 band, frameworks applied as optional tools not imposed,
    no banned claims, no invented offer)
  - arabic_qa: pass (self-applied; routes to arabic-copy-qa for the formal gate)
  - english_qa: na (Arabic-only package; EN variants, if in scope, are authored by
    copywriter-en and merge at the same gate)
  - design_qa: na (no visual asset in this package; approved imagery is open item 7)
  - compliance: pending (routes to compliance-privacy-reviewer alongside brand-qa)
  - brand_qa: pending (routes to brand-qa-reviewer last)
- open_items:
  1. Price and currency not confirmed (brief section 4, ASSUMPTION). Message 3 carries a
     marked slot [PRICE / PLACEHOLDER from brief] and no number appears anywhere else. Blocks
     any send that must show a price.
  2. Plan not confirmed (1-month or 3-month entry, brief section 4). Copy says "اشتراك" and
     "خطة" without naming which plan. Slot [PLAN if named from brief] in message 3.
  3. Promotion not confirmed (trial, first-time discount, or bundle, brief section 4). Slot
     [PROMO if any from brief] in message 3. None invented. If absent at send, remove the slot
     line cleanly.
  4. Content lineup not confirmed (brief section 4). No lesson count, module, or duration is
     stated. Copy leads with the artist and the craft only.
  5. Gate platform not confirmed (brief section 5, OPEN ITEM). Every CTA points at the
     Masterclass page or the paid-plan gate in intent only. The destination URL and send
     wiring stay blocked until the platform and the conversion page are named (streams 6, 7).
  6. Schedule not confirmed (brief section 6). Cadence references in the flow ("اليوم",
     "هذا الأسبوع") are relative and carry no date. No start_date, end_date, or send_window
     is stated.
  7. Approved imagery not confirmed (brief section 7). This package is text-only; if a visual
     is added in build it must be a real, rights-cleared supplied asset, never generated.
  8. Engagement-branch routing (message 4) is written as two variants, non-opener and engaged.
     The trigger logic and the engagement window belong to lifecycle-architect (stream 7) and
     resolve from live data at send. The non-opener variant carries the winback posture for the
     beauty-interested-lapsed and dormant-nonpayers segments; segment routing within the branch
     is the lifecycle-architect's call from live data.
- brief_refs:
  - product: Masterclass "Bassam Fattouh Teaches Bridal Makeup" (brief section 4), AR rendering
    "ماستر كلاس بسام فتوح لمكياج العرائس"
  - instructor: Bassam Fattouh, confirmed via the published Maharat course page (brief section
    4), naming allowed in copy for this class
  - offer: subscription to Maharat as the conversion, Masterclass as the hook (brief section 2, 4)
  - price: NOT used (ASSUMPTION, open item 1), shown only as a bracketed slot
  - promotion: NOT used (ASSUMPTION, open item 3), shown only as a bracketed slot
  - dates: NOT used (ASSUMPTION, open item 6), only relative time words
  - offer_framing_notes: empowering, lead with what the learner can create (brief section 4)
  - angle: create a confident bridal look yourself, learning from a leading regional makeup
    artist on Maharat (strategy-artifact angle)

---

## Body

### variants[]

```
id:        email-nonpayer-m1-entry
segment:   beauty-interested-engaged
language:  ar
framework: AIDA, opened with a 4 Us useful and ultra-specific lead line
headline:  إطلالة عروس تصنعينها بيديك
body:      تخيلي أنك تجهزين إطلالة يوم العرس بنفسك، بثقة وبخطوات واضحة.
           بسام فتوح يشرح فن مكياج العرائس في ماستر كلاس على مهارات.
           الفكرة بسيطة: مهارة حقيقية تصنعين بها لحظة لا تنسى، لك ولمن تحبين.
cta:       شاهدي الماستر كلاس
preheader: بسام فتوح يشرح فن مكياج العرائس خطوة بخطوة على مهارات، وأنت من يصنع الإطلالة
subject_ref: subj-nonpayer-m1
fills:     none (text-only; if a visual is added in build it overlays a real supplied asset)
```

```
id:        email-nonpayer-m2-proof
segment:   beauty-interested-engaged
language:  ar
framework: AIDA interest and desire, 4 Us unique and credible on the proof line
headline:  تتعلمين من فنان مكياج رائد في المنطقة
body:      بسام فتوح اسم يثق به محبو المكياج في العالم العربي، والآن يشرح طريقته خطوة بخطوة.
           في الماستر كلاس ترين كيف يفكر فنان محترف، وكيف تبنين إطلالة عروس متكاملة.
           ما تتعلمينه يبقى معك، تطبقينه على إطلالتك وعلى من حولك في كل مناسبة.
cta:       تعرفي على الماستر كلاس
preheader: ترين كيف يفكر فنان محترف، وكيف يبني إطلالة عروس متكاملة تبقى مهارتها معك
subject_ref: subj-nonpayer-m2
fills:     none
```

```
id:        email-nonpayer-m3-offer
segment:   beauty-interested-engaged, general-engaged-nonpayers
language:  ar
framework: AIDA action, 4 Cs final pass for a clear single offer line
headline:  افتحي الباب لمهارات لا تتوقف عند درس واحد
body:      الماستر كلاس بداية. الاشتراك في مهارات يفتح لك تعلما متواصلا من خبراء المنطقة، في مكان واحد.
           اختاري خطتك وابدئي اليوم: [PRICE / PLACEHOLDER from brief] [PLAN if named from brief].
           [PROMO if any from brief]
cta:       اشتركي وابدئي التعلم
preheader: خطة واحدة تفتح لك تعلما متواصلا من خبراء المنطقة، والماستر كلاس بدايتك
subject_ref: subj-nonpayer-m3
fills:     none
```

```
id:        email-nonpayer-m4-nonopener
segment:   beauty-interested-lapsed, dormant-nonpayers
language:  ar
framework: PAS without shame (problem named as life getting busy, never as a fault), winback posture
headline:  ما زالت الإطلالة بانتظارك
body:      ربما فاتك ذكرنا الأول، وهذا طبيعي في زحمة الأيام.
           ماستر كلاس بسام فتوح لمكياج العرائس ما زال هنا، ومتاح وقت ما تجهزين.
           خطوة واحدة تكفي لتبدئي.
cta:       شاهدي الماستر كلاس
preheader: ماستر كلاس بسام فتوح لمكياج العرائس ما زال متاحا وقت ما تجهزين، بلا ضغط
subject_ref: subj-nonpayer-m4-nonopener
fills:     none
winback_note: for beauty-interested-lapsed and dormant-nonpayers this is the re-engagement
           touch. It leads with the draw of the class and the artist to earn the re-open
           before any offer, and keeps a light, low-pressure posture so a dormant contact is
           not pushed further away. No price, no promotion, one soft CTA only.
```

```
id:        email-nonpayer-m4-engaged
segment:   beauty-interested-engaged, general-engaged-nonpayers
language:  ar
framework: AIDA action close, 4 Cs final pass, compelling and concise
headline:  هذه آخر دعوة لتبدئي رحلتك
body:      تابعت معنا حتى الآن، وهذه خطوتك الأخيرة لتحولي الاهتمام إلى مهارة.
           اشتراك واحد يمنحك الماستر كلاس وتعلما متواصلا من خبراء المنطقة.
           ابدئي اليوم وابني إطلالة تفخرين بها.
cta:       اشتركي الآن
preheader: اشتراك واحد يمنحك الماستر كلاس وتعلما متواصلا، وخطوتك الأخيرة تبدأ اليوم
subject_ref: subj-nonpayer-m4-engaged
fills:     none
```

### subject_lines[]

Each set carries a deliberate preheader (the same line set on the paired variant above, in the
40 to 90 character band) and a mobile-length note. Subjects are front-loaded so the key word
lands inside the first 30 characters, with each line aimed at the 30 to 40 character target,
because most opens are on mobile where the inbox shows about 33 to 35 characters. Where an
angle reads strongest as a tight line under 30, the primary stays short on purpose and the note
records the choice; the alternatives stretch into the band for the test.

```
id:        subj-nonpayer-m1
email_ref: email-nonpayer-m1-entry
preheader: بسام فتوح يشرح فن مكياج العرائس خطوة بخطوة على مهارات، وأنت من يصنع الإطلالة
options:
  - text: إطلالة عروس تصنعينها بنفسك مع بسام فتوح    language: ar   primary: true    note: 38 chars, "إطلالة عروس" front-loaded in the first 30
  - text: مكياج العرائس مع بسام فتوح على مهارات       language: ar   primary: false   note: 35 chars, "مكياج العرائس" front-loaded
  - text: فن إطلالة العرس بين يديك                    language: ar   primary: false   note: 23 chars, "فن إطلالة" front-loaded (tight alternative)
primary:   إطلالة عروس تصنعينها بنفسك مع بسام فتوح
mobile_note: primary 38 characters, in the 30 to 40 band, key word "إطلالة عروس" inside the first 30, front-loaded.
```

```
id:        subj-nonpayer-m2
email_ref: email-nonpayer-m2-proof
preheader: ترين كيف يفكر فنان محترف، وكيف يبني إطلالة عروس متكاملة تبقى مهارتها معك
options:
  - text: تعلمي إطلالة العروس من فنان مكياج رائد      language: ar   primary: true    note: 37 chars, "تعلمي" + "إطلالة العروس" front-loaded in the first 30
  - text: بسام فتوح يشرح إطلالة العروس خطوة بخطوة     language: ar   primary: false   note: 38 chars, "بسام فتوح" first
  - text: كيف يبني المحترف إطلالة عروس                language: ar   primary: false   note: 27 chars, "كيف يبني المحترف" first (tight alternative)
primary:   تعلمي إطلالة العروس من فنان مكياج رائد
mobile_note: primary 37 characters, in the 30 to 40 band, key words "تعلمي" and "إطلالة العروس" inside the first 30.
```

```
id:        subj-nonpayer-m3
email_ref: email-nonpayer-m3-offer
preheader: خطة واحدة تفتح لك تعلما متواصلا من خبراء المنطقة، والماستر كلاس بدايتك
options:
  - text: ابدئي اشتراكك وتعلمي بلا توقف على مهارات    language: ar   primary: true    note: 38 chars, "ابدئي اشتراكك" front-loaded in the first 30
  - text: مهارة جديدة تبدأ بخطوة واحدة اليوم          language: ar   primary: false   note: 33 chars, "مهارة جديدة" first
  - text: تعلم لا يتوقف عند درس واحد                  language: ar   primary: false   note: 25 chars, "تعلم لا يتوقف" first (tight alternative)
primary:   ابدئي اشتراكك وتعلمي بلا توقف على مهارات
mobile_note: primary 38 characters, in the 30 to 40 band, key word "ابدئي اشتراكك" inside the first 30, front-loaded.
```

```
id:        subj-nonpayer-m4-nonopener
email_ref: email-nonpayer-m4-nonopener
preheader: ماستر كلاس بسام فتوح لمكياج العرائس ما زال متاحا وقت ما تجهزين، بلا ضغط
options:
  - text: ما زالت إطلالة العروس بانتظارك              language: ar   primary: true    note: 29 chars, "ما زالت إطلالة العروس" front-loaded
  - text: إطلالتك ما زالت بانتظارك مع بسام فتوح       language: ar   primary: false   note: 36 chars, "إطلالتك" first
  - text: خطوة واحدة تكفي لتبدئي اليوم                language: ar   primary: false   note: 27 chars, "خطوة واحدة" first (tight alternative)
primary:   ما زالت إطلالة العروس بانتظارك
mobile_note: primary 29 characters, just under the band on purpose for a soft winback line, key word "ما زالت إطلالة العروس" inside the first 30.
```

```
id:        subj-nonpayer-m4-engaged
email_ref: email-nonpayer-m4-engaged
preheader: اشتراك واحد يمنحك الماستر كلاس وتعلما متواصلا، وخطوتك الأخيرة تبدأ اليوم
options:
  - text: آخر دعوة لتبدئي رحلتك مع مهارات             language: ar   primary: true    note: 30 chars, "آخر دعوة" front-loaded in the first 30
  - text: حولي اهتمامك إلى مهارة تبقى معك             language: ar   primary: false   note: 31 chars, "حولي اهتمامك" first
  - text: خطوتك الأخيرة تبدأ اليوم                    language: ar   primary: false   note: 23 chars, "خطوتك الأخيرة" first (tight alternative)
primary:   آخر دعوة لتبدئي رحلتك مع مهارات
mobile_note: primary 30 characters, at the band floor, key word "آخر دعوة" front-loaded inside the first 30.
```

### fills

No creative-package arrived for this campaign (stream 3 is conditional on open item 7,
approved imagery). All five email variants are text-only and fill no asset_brief copy-overlay
slot. If a real, rights-cleared supplied asset is later approved and an email needs a visual,
the copy in each variant overlays it in build, never baked into a generated image, RTL-safe,
with the brand visual constants (#141414, #1A1A1A, emerald #009975) applied at build.

---

## Flow map (for lifecycle-architect, stream 7)

- Message 1, entry/value: email-nonpayer-m1-entry. Leads with what the reader can create.
- Message 2, proof/credibility: email-nonpayer-m2-proof. The artist and the craft, confirmed
  facts only, no lineup, duration, awards, or client names.
- Message 3, offer: email-nonpayer-m3-offer. Subscription stated plainly with the price,
  plan, and promotion left as marked slots from the brief.
- Message 4, engagement branch: email-nonpayer-m4-nonopener (lighter nudge for non-openers,
  and the winback touch for the lapsed and dormant segments) and email-nonpayer-m4-engaged
  (stronger close for engaged readers). Branch trigger, segment routing, and engagement window
  belong to stream 7, resolved from live data at send.

Cadence and triggers are proposed in the strategy-artifact (about 2 weeks, 4 messages) and
remain an open item until Ahmed confirms the schedule. No date appears in any copy.

---

## arabic-copy-qa self-check result (v2)

Self-applied against the arabic-copy-qa checks before routing to the formal gate. Re-run on the
v2 additions (preheaders set into the 40 to 90 band, subjects tuned toward the 30 to 40 band,
frameworks per stage, winback note).

- MSA with Gulf-familiar wording: pass. Modern Standard Arabic throughout, warm and natural,
  feminine address fits a bridal makeup audience, no stiff or academic phrasing. New and
  lengthened preheaders hold the same register.
- Thmanyah tone (clear, modern, intelligent, never stiff): pass. Short active sentences,
  concrete nouns, confident without hype. Preheaders read as one clear added promise, not filler.
- No tatweel or kashida (U+0640): pass. None present, grep-confirmed clean.
- Western numerals only (0 to 9), no Eastern Arabic numerals (U+0660 to U+0669): pass. The only
  digits in the file are Western (hex color codes, character counts, section numbers).
- No em dash glyph (U+2014): pass. None present, grep-confirmed clean; commas, colons, and
  periods only.
- Empowering, never deficit-framed: pass. Every message leads with what the reader can create
  or become ("تصنعينها بيديك", "مهارة تبقى معك", "حولي اهتمامك إلى مهارة"). The non-opener and
  winback line normalizes a missed email ("هذا طبيعي في زحمة الأيام") without shame, holding the
  PAS structure to the empowering rule.
- RTL-safe: pass. Arabic is the primary direction; preheaders are pure Arabic. The only embedded
  Latin is the bracketed English placeholder slots in message 3, which are build-time tokens to
  be replaced from the brief, not shipped copy.
- No accreditation implication: pass. No certificate or accreditation claim anywhere.
- No invented facts: pass. No price, promotion, plan name, lesson count, module, duration,
  award, or client name. Only the confirmed instructor name (Bassam Fattouh) and the real
  Masterclass title are used. The winback note adds posture guidance only, no new facts.
- Mobile subject length (v2 check): pass. Every primary is in or at the 30 to 40 band (M1 38,
  M2 37, M3 38, M4-engaged 30) with one deliberate soft exception (M4-nonopener 29, a softer
  winback line held just under the band on purpose), and every primary keeps its key word
  inside the first 30 characters, front-loaded. Alternatives span the band and one tight line
  each for the test.
- Deliberate preheader (v2 check): pass. Every message and subject set carries a preheader set
  on purpose in the 40 to 90 character band, true to its body, none left to spill body text.
- Frameworks optional (v2 check): pass. AIDA, the 4 Us, PAS, and the 4 Cs are applied per funnel
  stage as tools to sharpen each line, not imposed as a rigid template, and the Arabic-first
  Thmanyah voice stays primary throughout.

Self-result: PASS on all arabic-copy-qa checks, including the v2 mobile-length, preheader, and
framework checks. Routes next to arabic-copy-qa (formal gate), then brand-qa-reviewer alongside
compliance-privacy-reviewer. Status moves to qa-passed only after those gates clear.
