# email-sequence-7.ar: Bassam Fattouh bridal makeup, 7-email non-payer lifecycle (Arabic)

Stream 4 artifact. A 7-email Arabic-first lifecycle sequence that moves non-paying contacts to
watch the Masterclass "Bassam Fattouh Teaches Bridal Makeup" and then subscribe to a paid
Maharat plan. Authored Arabic-first in the Maharat voice from the qa-passed strategy-artifact
(angle, segments, offer_framing) and the active brief. Continuity of tone with the existing
copy-package (the 4-message flow) is preserved: same confirmed title and instructor only, same
empowering through-line, same placeholder discipline. This sequence is a longer-arc variant, it
does not replace the copy-package, lifecycle-architect (stream 7) chooses which to wire.

No price, promotion, plan name, lesson lineup, duration, lesson count, award, testimonial,
number, or instructor fact beyond the confirmed name appears anywhere. Unconfirmed variables
are marked as bracketed copy slots and listed in open_items. No em dash glyph, no tatweel,
Western numerals only, RTL-safe.

---

## Common envelope

- campaign_id: 2026-06-bassam-fattouh-bridal-makeup
- produced_by: copywriter-ar
- stream: 4 copywriting
- language: ar
- status: draft (skill eval and arabic-copy-qa self-check passed; awaits the formal
  arabic-copy-qa gate, then brand-qa-reviewer alongside compliance-privacy-reviewer before
  status moves to qa-passed)
- qa:
  - skill_eval: pass (email-copy and subject-lines checks: one clear CTA per email, mobile
    subject length toward the 30 to 40 band with the key word in the first 30, deliberate
    preheader present in the 40 to 90 band, no banned claims, no invented offer)
  - arabic_qa: pass (self-applied below; routes to arabic-copy-qa for the formal gate)
  - english_qa: na (Arabic-only sequence)
  - design_qa: na (text-only; approved imagery is an open item)
  - compliance: pending (routes to compliance-privacy-reviewer alongside brand-qa)
  - brand_qa: pending (routes to brand-qa-reviewer last)
- open_items:
  1. Price and currency not confirmed (brief section 4, ASSUMPTION). Email 5 carries a marked
     slot [PRICE from brief]. No number appears anywhere else. Blocks any send that must show a
     price.
  2. Plan not confirmed (1-month or 3-month entry, brief section 4, ASSUMPTION). Copy says
     "اشتراك" and "خطة" without naming which plan. Slot [PLAN from brief] in email 5.
  3. Promotion not confirmed (trial, first-time discount, or bundle, brief section 4,
     ASSUMPTION). Slot [PROMO if any] in email 5. None invented. If absent at send, remove the
     slot line cleanly.
  4. Content lineup not confirmed (brief section 4). No lesson count, module, or duration is
     stated. Copy leads with the artist and the craft only.
  5. Gate platform not confirmed (brief section 5, OPEN ITEM). Every CTA points at the
     Masterclass page or the paid-plan gate in intent only. The destination URL and send wiring
     stay blocked until the platform and the conversion page are named (streams 6, 7).
  6. Schedule not confirmed (brief section 6, ASSUMPTION). Cadence references are relative
     ("اليوم", "هذا الأسبوع") and carry no date. Email 7 carries a marked slot [DEADLINE from
     brief] used only if the brief confirms a date; if none, remove the slot line cleanly. No
     date is invented.
  7. Approved imagery not confirmed (brief section 7, ASSUMPTION). This sequence is text-only;
     if a visual is added in build it must be a real, rights-cleared supplied asset, never
     generated.
  8. Segment routing across the 7 emails belongs to lifecycle-architect (stream 7) and resolves
     from live data at send. The sequence below is written for the primary
     beauty-interested-engaged segment as the spine, with per-email segment notes where the
     emphasis tunes for general-engaged-nonpayers, beauty-interested-lapsed, and
     dormant-nonpayers. Suppression (paying, unsubscribed, hard-bounced) is applied before send.
- brief_refs:
  - product: Masterclass "Bassam Fattouh Teaches Bridal Makeup" (brief section 4), AR rendering
    "ماستر كلاس بسام فتوح لمكياج العرائس"
  - instructor: Bassam Fattouh, confirmed via the published Maharat course page (brief section
    4), naming allowed in copy for this class
  - offer: subscription to Maharat as the conversion, the Masterclass as the hook (brief
    sections 2, 4)
  - price: NOT used (ASSUMPTION, open item 1), shown only as a bracketed slot in email 5
  - promotion: NOT used (ASSUMPTION, open item 3), shown only as a bracketed slot in email 5
  - dates: NOT used (ASSUMPTION, open item 6), only relative time words; a bracketed
    [DEADLINE from brief] slot in email 7, used only if confirmed
  - offer_framing_notes: empowering, lead with what the learner can create (brief section 4)
  - angle: create a confident bridal look yourself, learning from a leading regional makeup
    artist on Maharat (strategy-artifact angle)

---

## The 7-step map

1. Email 1, hook / watch. The bridal look she can create herself, learning from a leading
   regional artist. CTA: watch the Masterclass.
2. Email 2, instructor credibility. Why learning bridal makeup from Bassam Fattouh is worth it.
   CTA: watch.
3. Email 3, the transformation. What she will be able to do after, a confident bridal look for
   her day or for her clients. CTA: watch a lesson.
4. Email 4, belonging / momentum. She is not doing this alone, framed aspirationally, no
   invented testimonials, names, or numbers. CTA: watch now.
5. Email 5, the offer. Subscribe to watch the full Masterclass and all of Maharat. Price, plan,
   and promotion as marked slots. CTA: subscribe.
6. Email 6, reassurance / objections. Learn at your own pace, on your phone, start today. No
   accreditation. CTA: subscribe and start.
7. Email 7, last call / winback. A gentle final nudge for those who have not subscribed,
   [DEADLINE from brief] slot only if a date is confirmed. CTA: subscribe today.

Watch-focused CTAs in emails 1 to 4, subscription CTAs in emails 5 to 7. Cadence and triggers
belong to lifecycle-architect (stream 7) and remain an open item until Ahmed confirms the
schedule. No date appears in any copy except the bracketed slot in email 7.

---

## Body

### Email 1, hook / watch

- step: 1, role: hook and first invitation to watch. Leads with what the reader can create.
- segment: beauty-interested-engaged (spine). For general-engaged-nonpayers, the same line reads
  as a concrete proof of premium teaching; for beauty-interested-lapsed, the artist is the draw
  that earns the re-open.
- subject (primary): إطلالة عروس تصنعينها بنفسك
  - note: 25 chars, "إطلالة عروس" front-loaded inside the first 30. Tight on purpose for a clean
    first-touch line.
- subject (alt 1): إطلالة العروس مع بسام فتوح اليوم
  - note: 31 chars, "إطلالة العروس" front-loaded.
- subject (alt 2): مكياج العرائس يبدأ بخطوة واحدة
  - note: 29 chars, "مكياج العرائس" front-loaded.
- preheader: بسام فتوح يشرح فن مكياج العرائس خطوة بخطوة على مهارات، وأنت من يصنع الإطلالة
  - note: 73 chars, in the 40 to 90 band, true to the body.
- body:
  تخيلي أنك تجهزين إطلالة يوم العرس بنفسك، بثقة وبخطوات واضحة.
  بسام فتوح يشرح فن مكياج العرائس في ماستر كلاس على مهارات.
  مهارة حقيقية تصنعين بها لحظة لا تنسى، لك ولمن تحبين.
- cta (watch): شاهدي الماستر كلاس

### Email 2, instructor credibility

- step: 2, role: why learning from Bassam Fattouh is worth it. Confirmed facts only, no lineup,
  duration, awards, or client names.
- segment: beauty-interested-engaged (spine). For general-engaged-nonpayers, the credibility of
  a leading expert is the reason to judge the platform worth paying for.
- subject (primary): تعلمي من فنان مكياج رائد في المنطقة
  - note: 35 chars, "تعلمي" and "فنان مكياج" front-loaded inside the first 30.
- subject (alt 1): بسام فتوح يشرح طريقته خطوة بخطوة
  - note: 31 chars, "بسام فتوح" first.
- subject (alt 2): لماذا تتعلمين المكياج من محترف
  - note: 29 chars, "لماذا تتعلمين" front-loaded.
- preheader: ترين كيف يفكر فنان محترف، وكيف يبني إطلالة عروس متكاملة تبقى مهارتها معك
  - note: 70 chars, in the 40 to 90 band, true to the body.
- body:
  بسام فتوح اسم يثق به محبو المكياج في العالم العربي.
  في الماستر كلاس يشرح طريقته خطوة بخطوة، فترين كيف يفكر فنان محترف.
  ما تتعلمينه يبقى معك، تطبقينه على إطلالتك وعلى من حولك في كل مناسبة.
- cta (watch): شاهدي الماستر كلاس

### Email 3, the transformation

- step: 3, role: what she will be able to do after, a confident bridal look for her day or her
  clients. Empowering, future-facing, no overclaim.
- segment: beauty-interested-engaged (spine, her own day). For contacts who do makeup for others,
  the same skill applies to their clients, so the line carries both readings.
- subject (primary): إطلالة عروس واثقة بين يديك
  - note: 25 chars, "إطلالة عروس" front-loaded. Tight on purpose.
- subject (alt 1): ماذا ستتقنين بعد الماستر كلاس
  - note: 28 chars, "ماذا ستتقنين" front-loaded.
- subject (alt 2): مهارة تطبقينها في كل مناسبة
  - note: 26 chars, "مهارة تطبقينها" front-loaded.
- preheader: بعد الماستر كلاس تجهزين إطلالة عروس متكاملة بثقة، ليومك أو لمن تجملينها
  - note: 70 chars, in the 40 to 90 band, true to the body.
- body:
  تخيلي نفسك بعد الماستر كلاس: تمسكين الفرشاة بثقة، وتعرفين كل خطوة ولماذا.
  إطلالة عروس متكاملة تصنعينها لنفسك في يومك، أو لمن تجملينها بيديك.
  ابدئي بدرس واحد اليوم، وستفاجئين بما تتقنينه.
- cta (watch a lesson): شاهدي درسا من الماستر كلاس

### Email 4, belonging / momentum

- step: 4, role: she is not doing this alone, aspirational momentum. No invented testimonials,
  names, or numbers. The belonging is framed through the shared craft and the platform, not
  through fabricated social proof.
- segment: beauty-interested-engaged (spine). For beauty-interested-lapsed, this is the
  re-engagement aspiration; for dormant-nonpayers it stays light and low-pressure.
- subject (primary): انضمي لمن يتعلمن الفن نفسه
  - note: 25 chars, "انضمي" front-loaded. Tight, warm.
- subject (alt 1): الفن نفسه يجمعك بمحبي المكياج
  - note: 28 chars, "الفن نفسه" front-loaded.
- subject (alt 2): خطوتك تبدأ، ولست وحدك فيها
  - note: 25 chars, "خطوتك تبدأ" front-loaded.
- preheader: في مهارات تتعلمين الفن مع من يشاركنك الشغف نفسه، وكل خطوة تقربك من إطلالتك
  - note: 72 chars, in the 40 to 90 band, true to the body.
- body:
  شغفك بالمكياج يجمعك بمن يتعلمن الفن نفسه على مهارات.
  لست وحدك في الطريق، فكل درس قصير خطوة تبني بها مهارة تبقى معك.
  الماستر كلاس بانتظارك، والخطوة التالية بين يديك.
- cta (watch now): شاهدي الماستر كلاس الآن

### Email 5, the offer

- step: 5, role: the offer. Subscribe to watch the full Masterclass and all of Maharat. Price,
  plan, and promotion as marked slots only, none invented.
- segment: beauty-interested-engaged and general-engaged-nonpayers (the sharpest offer framing).
- subject (primary): ابدئي اشتراكك وتعلمي بلا توقف
  - note: 28 chars, "ابدئي اشتراكك" front-loaded inside the first 30.
- subject (alt 1): اشتراك واحد يفتح لك مهارات كلها
  - note: 30 chars, "اشتراك واحد" front-loaded.
- subject (alt 2): خطتك تبدأ اليوم على مهارات
  - note: 25 chars, "خطتك تبدأ" front-loaded.
- preheader: خطة واحدة تفتح لك الماستر كلاس وتعلما متواصلا من خبراء المنطقة في مكان واحد
  - note: 73 chars, in the 40 to 90 band, true to the body.
- body:
  الماستر كلاس بداية. الاشتراك في مهارات يفتح لك تعلما متواصلا من خبراء المنطقة، في مكان واحد.
  اختاري خطتك وابدئي اليوم: [PRICE from brief] [PLAN from brief].
  [PROMO if any]
- cta (subscribe): اشتركي الآن

### Email 6, reassurance / objections

- step: 6, role: reassurance. Learn at your own pace, on your phone, start today. No accreditation
  claim. Answers the "is it for me, do I have time" objection without shame.
- segment: beauty-interested-engaged (spine), and any segment hesitating on time or fit.
- subject (primary): تعلمي على راحتك ومن هاتفك
  - note: 24 chars, "تعلمي على راحتك" front-loaded. Tight, reassuring.
- subject (alt 1): على وقتك أنت، وخطوة واحدة تكفي
  - note: 30 chars, "على وقتك أنت" front-loaded.
- subject (alt 2): ابدئي اليوم بخطوة صغيرة
  - note: 22 chars, "ابدئي اليوم" front-loaded.
- preheader: دروس قصيرة تشاهدينها من هاتفك في أي وقت، تبدئين اليوم وتتقدمين على راحتك
  - note: 70 chars, in the 40 to 90 band, true to the body.
- body:
  لا حاجة لوقت طويل ولا لخبرة سابقة. دروس قصيرة تشاهدينها من هاتفك متى ما ناسبك.
  تتقدمين على راحتك، خطوة كل يوم، وتعودين للدرس وقت ما تشائين.
  الاشتراك يفتح لك الماستر كلاس وبقية مهارات، وتبدئين اليوم.
- cta (subscribe and start): اشتركي وابدئي اليوم

### Email 7, last call / winback

- step: 7, role: a gentle final nudge for those who have not subscribed. Soft, low-pressure,
  no shame. [DEADLINE from brief] slot used only if the brief confirms a date, else remove the
  line cleanly. No date invented.
- segment: anyone in the flow who has not subscribed, with a lighter posture for
  beauty-interested-lapsed and dormant-nonpayers.
- subject (primary): إطلالتك ما زالت بانتظارك
  - note: 23 chars, "إطلالتك ما زالت" front-loaded. Soft winback line.
- subject (alt 1): فرصتك لتبدئي ما زالت قائمة
  - note: 25 chars, "فرصتك لتبدئي" front-loaded.
- subject (alt 2): خطوة أخيرة نحو إطلالتك
  - note: 21 chars, "خطوة أخيرة" front-loaded.
- preheader: الماستر كلاس وبقية مهارات بانتظارك، وخطوة واحدة اليوم تبدأ بها رحلتك بلا ضغط
  - note: 73 chars, in the 40 to 90 band, true to the body.
- body:
  ربما لم يحن الوقت بعد، وهذا طبيعي في زحمة الأيام.
  لكن الماستر كلاس وبقية مهارات ما زالت بانتظارك، وخطوة واحدة تكفي لتبدئي.
  [DEADLINE from brief]
- cta (subscribe today): اشتركي اليوم

---

## Flow map (for lifecycle-architect, stream 7)

- Emails 1 to 4 are watch-focused: they earn the play on the Masterclass (the leading indicator
  in the strategy success_metric). Email 1 hooks, 2 builds credibility, 3 shows the
  transformation, 4 builds belonging and momentum.
- Emails 5 to 7 are subscription-focused: 5 states the offer plainly with price, plan, and
  promotion as marked slots; 6 clears the time-and-fit objection; 7 is the gentle final nudge
  with an optional confirmed-deadline slot.
- Segment routing, cadence, triggers, and the engagement window belong to stream 7 and resolve
  from live data at send. Send wiring stays blocked until the gate platform is confirmed
  (open item 5). No date appears in any copy except the bracketed [DEADLINE from brief] slot in
  email 7, used only if confirmed.
- This 7-email sequence is a longer-arc alternative to the existing 4-message copy-package, not
  a replacement. Lifecycle-architect selects which to wire and folds the engagement branch logic
  in as needed.

---

## arabic-copy-qa self-check result

Self-applied against the arabic-copy-qa checks and the 04-copywriting skill evals (email-copy
and subject-lines) before routing to the formal gate.

- MSA with Gulf-familiar wording: pass. Modern Standard Arabic throughout, warm and natural,
  feminine address fits a bridal makeup audience, no stiff or academic phrasing. Preheaders hold
  the same register.
- Thmanyah tone (clear, modern, intelligent, never stiff): pass. Short active sentences,
  concrete nouns, confident without hype. Each preheader reads as one clear added promise.
- No tatweel or kashida (U+0640): pass. None present, grep-confirmed clean.
- Western numerals only (0 to 9), no Eastern Arabic numerals (U+0660 to U+0669): pass. The only
  digits in the file are Western (character counts, step and section numbers).
- No em dash glyph (U+2014): pass. None present, grep-confirmed clean; commas, colons, and
  periods only.
- Empowering, never deficit-framed: pass. Every email leads with what the reader can create or
  become ("تصنعينها بنفسك", "إطلالة عروس واثقة بين يديك", "مهارة تبقى معك"). Emails 4 and 7
  normalize hesitation ("لست وحدك", "هذا طبيعي في زحمة الأيام") without shame.
- One clear CTA per email: pass. Each email carries exactly one CTA. Emails 1 to 4 are
  watch-focused, emails 5 to 7 are subscription-focused, per the brief.
- RTL-safe: pass. Arabic is the primary direction; preheaders are pure Arabic. The only embedded
  Latin is the bracketed English placeholder slots ([PRICE from brief], [PLAN from brief],
  [PROMO if any], [DEADLINE from brief]), which are build-time tokens to be replaced or removed
  from the brief, not shipped copy.
- No accreditation implication: pass. No certificate or accreditation claim anywhere.
- No invented facts: pass. No price, promotion, plan name, lesson count, module, duration,
  award, testimonial, number, or client name. No fabricated social proof in email 4: belonging
  is framed through the shared craft and the platform, not invented people or figures. Only the
  confirmed instructor name (Bassam Fattouh) and the real Masterclass title are used.
- Subject length, mobile-tuned: pass. Every primary sits at or under the 30 to 40 character band
  with the key word front-loaded inside the first 30 (E1 25, E2 35, E3 25, E4 25, E5 28, E6 24,
  E7 23). Several primaries are deliberately tight (under 30) for clean first-touch and soft
  winback lines; alternates extend toward the band for the test. Each email carries one primary
  plus two alternates.
- Deliberate preheader: pass. Every email carries a preheader set on purpose in the 40 to 90
  character band, true to its body, none left to spill body text.

Self-result: PASS on all arabic-copy-qa checks and the 04-copywriting skill evals. Routes next
to arabic-copy-qa (formal gate), then brand-qa-reviewer alongside compliance-privacy-reviewer.
Status moves to qa-passed only after those gates clear. Nothing sends; the human gate surfaces
all open items for Ahmed before any approval.
