# Brand-Voice QA Verdict

## Envelope

```
skill        brand-voice-qa
gate         brand_voice
target       brand-voice-hero.ar.md (HERO-* set) + copy-package.ar.md (AR funnel copy)
campaign_id  2026-07-summer-nonpayer
reviewed_by  brand-voice-reviewer
date         2026-06-12
result       pass
re_verified  2026-06-12 (second pass, both prior blocking fixes confirmed resolved, no regression)
```

All eight checks ran against both files in this re-verification pass. Both prior blocking fixes
are confirmed resolved. The two new ad units (AD-STYLING-1, AD-MARKETING-1) are on-voice and use
only cleared facts. No regression found. The copy advances to brand-qa-reviewer.

---

## Fix 1: voice-alignment (HERO-MANIFESTO deficit frame)

Prior failing span: "لديك الساعات، ولديك الفضول، وينقصك فقط أن تبدأ"

Current HERO-MANIFESTO: "هذا الصيف وقتك. لديك الساعات، ولديك الفضول، والقرار قرارك أن تبدأ."

Confirmed resolved. "ينقصك" is removed. The replacement "والقرار قرارك أن تبدأ" leads with
what the reader already holds and frames starting as the reader's own choice. The empowering
posture carries through the whole manifesto: every line builds on what the reader has, can
choose, and will become. No deficit word or frame anywhere in the HERO set.

---

## Fix 2: instructor-framing (ك suffix in ad headlines and display-title list)

Prior failing span: five headlines in copy-package.ar.md using "يعلّمك / تعلّمك".

Current state, all five original headlines confirmed corrected:
- AD-MUSIC-1: "راغب علامة يعلّم الموسيقى" (masculine يعلّم, no ك)
- AD-COOK-1: "سلام دقاق تعلّم الطبخ الشامي" (feminine تعلّم, no ك)
- AD-MAKEUP-1: "بسام فتوح يعلّم المكياج" (masculine يعلّم, no ك)
- AD-BUSINESS-1: "توفيق كريديه يعلّم بناء الأعمال" (masculine يعلّم, no ك)
- AD-ACTING-1: "قصي خولي يعلّم التمثيل" (masculine يعلّم, no ك)

Two new units, verified on the same pattern:
- AD-STYLING-1: "سيدريك حداد يعلّم التنسيق" (Cedric is male, يعلّم correct, no ك)
- AD-MARKETING-1: "إلدا شقير تعلّم التسويق" (Elda is female, تعلّم correct, no ك)

Display-title list in open_items confirmed: all seven titles use the correct gender-agreed verb
form with no ك suffix. The body copy within each ad uses reader-addressed forms (يشاركك,
تأخذك, يأخذك), which is separate from the fixed title pattern and is not a failure.

Confirmed resolved across all occurrences.

---

## New unit voice check: AD-STYLING-1 (Cedric) and AD-MARKETING-1 (Elda)

AD-STYLING-1: empowering throughout ("اكتشفي أسلوبك الخاص", "أناقة تصنعينها بثقة"), framing
styling as confidence and self-expression, not correction. Authority anchored to the cleared,
page-sourced fact (celebrity stylist trusted by the Arab world's biggest stars). Feminine address
correct for the styling category. No private clients, no Brands For Less, no invented fact.

AD-MARKETING-1: empowering and outcome-led ("تسويقاً يصنع الفرق"). Authority anchored to
cleared, page-sourced facts only ("من أبرز قادة التسويق في العالم العربي، بخبرة عقود في
صناعة علامات تجارية أيقونية"). Omnicom, Forbes, Cannes, the 900-plus and 1000-plus figures,
and all other verify-before-use facts are excluded. Masculine/plural address correct for the
marketing category (not beauty or styling). Both new units are on-voice.

---

## All eight checks, final status

1. voice-alignment: pass. No deficit frame anywhere in either file. HERO-MANIFESTO rewrite is
   on-voice. All funnel copy leads with what the reader can build and become. Thmanyah tone
   holds: modern, confident, not stiff, not hype.
2. positioning-and-mission: pass. All four core anchors present and correctly used
   ("تعلّم من نخبة العرب", "منبر للعرب، من قبل العرب", "تثقيف وترفيه وإلهام العالم العربي",
   "التعلّم يجب أن يكون ملهمًا لا مرهقًا"). No contradiction.
3. lexicon: pass. Brand signature vocabulary throughout. "من يصنعون المعيار" extends the
   lexicon consistently. Loanwords ("لوك") used only where the manual confirms on-brand.
   No hype without grounding, no deficit or correction vocabulary.
4. instructor-framing: pass. All seven headlines use the correct "[الاسم] يعلّم/تعلّم [الموضوع]"
   pattern, verb agrees with instructor gender. No ك suffix in any title. Authority anchored
   to a concrete, cleared, page-sourced proof in every case. No private clients named. No
   accreditation implied. Verify-before-use facts excluded.
5. product-framing: pass. No invented Skill Path titles, no invented class titles or lesson
   counts, no price in any body, no accreditation implied. "مهارة حقيقية" framed as skill and
   confidence, never as a credential. Taxonomy (صفوف, اشتراك) used correctly.
6. address-and-register: pass. Feminine singular for beauty and styling (AD-MAKEUP-1,
   AD-STYLING-1, SOCIAL-S5, SOCIAL-S6). Masculine singular or inclusive plural everywhere else
   including AD-MARKETING-1. Person and number consistent within each asset, no mid-asset switch.
7. guardrails: pass. No accreditation implied. No roadmap, fundraising, or unannounced plan. All
   featured classes are confirmed, published masterclasses. The four non-nameable instructors
   never appear by name. All verify-before-use facts (Brands For Less, Omnicom, Forbes, Cannes,
   garage detail, 900-plus and 1000-plus figures) correctly excluded.
8. result-is-binary: pass. Every check passes. Copy advances.

---

## Regression scan

Deficit framing: no regression. No "ينقصك", no "متأخر", no correction framing anywhere in
either file. The retargeting recall ("بدأت ولم تكمل؟") and last-call lines ("لا نريدك أن
تفوّت صيفك", "لا تدع صيفك يمضي") are invitations, not deficit frames, and were passed in the
prior verdict. No change to their status.

Gendered address: no regression. Beauty and styling assets hold feminine consistently.
All other assets hold masculine or plural. No mid-asset switch found in any unit.

---

## Routing

Pass. The copy advances to brand-qa-reviewer. No fix list.

Prior verdict (fail, 2026-06-12): two blocking items, voice-alignment and instructor-framing.
This re-verification (pass, 2026-06-12): both resolved, no regression, new units on-voice.
