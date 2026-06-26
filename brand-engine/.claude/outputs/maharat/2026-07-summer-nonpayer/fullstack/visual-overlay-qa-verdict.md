# Visual Overlay QA Verdict: Summer of Skills, full-stack non-payer campaign

## Envelope

- campaign_id: 2026-07-summer-nonpayer
- gate: brand-qa-reviewer
- files_reviewed:
  - outputs/2026-07-summer-nonpayer/fullstack/visual-overlay-copy.ar.md
  - outputs/2026-07-summer-nonpayer/fullstack/visual-overlay-copy.en.md
- references_checked:
  - CLAUDE.md
  - context/brand-voice.md
  - outputs/2026-07-summer-nonpayer/fullstack/creative-package.md (AB1 to AB9, DS1 to DS8)
  - outputs/2026-07-summer-nonpayer/fullstack/copy-package.ar.md (all variant IDs cited as AR sources)
  - outputs/2026-07-summer-nonpayer/fullstack/brand-voice-hero.ar.md (HERO-SIGNATURE, HERO-HEADLINE, HERO-POSITIONING, HERO-CTA)
  - outputs/2026-07-summer-nonpayer/fullstack/copy-package.en.md (all variant IDs cited as EN sources)
- compliance-privacy-reviewer: verdict not yet confirmed in this run. Both gates must pass to advance. This verdict is recorded; the asset does not advance until compliance-privacy-reviewer also returns a pass.
- date: 2026-06-16

---

## Prior-gate status

### AR file
- skill_eval: the AR overlay file carries no new authorship (binding only); the source copy-package.ar.md carries skill-eval status. Accepted as in-scope.
- arabic_qa: the AR overlay file records a self-run pass and states it routes to arabic-copy-qa as the gate of record. A self-run is not a gate-of-record pass. The gate-of-record arabic-copy-qa verdict for the length-adapted lockups in this file is not yet confirmed.

Action: the AR file must pass arabic-copy-qa (gate of record) before it advances to build. This brand-qa verdict runs now on the substance and records the prior-gate gap. If arabic-copy-qa returns a fail, the AR file returns to copywriter-ar before advancing regardless of this verdict.

### EN file
- skill_eval: the EN overlay file records a self-run pass. Not a gate-of-record pass.
- english_qa: the EN overlay file records a self-check pass and states it routes to english-copy-qa for independent verification. A self-check is not a gate-of-record pass. The gate-of-record english-copy-qa verdict for this file is not yet confirmed.

Action: the EN file must pass english-copy-qa (gate of record) before it advances to build. This brand-qa verdict runs now on the substance and records the prior-gate gap.

---

## Verdict

- visual-overlay-copy.ar.md: PASS
- visual-overlay-copy.en.md: FAIL

---

## AR file: full check record

### Check 1: Binding integrity

Every source variant ID cited in the AR overlay file was verified against copy-package.ar.md and brand-voice-hero.ar.md. All IDs exist in those QA-passed sources.

Slots and their source traces:

- AB1 [ar headline] cites AD-BREADTH-1 headline (ar): verified. Bound text "صيف المهارات، اختر مجالك" matches the source verbatim.
- AB1 [ar subline] cites AD-BREADTH-1 primary text line 2 (ar): verified. Bound text matches the source field-list line verbatim.
- AB1 [ar cta chip] cites AD-BREADTH-1 cta (ar): verified. "ابدأ مجاناً" matches verbatim.
- AB2 DS2-music field headline cites AD-MUSIC-1 headline (ar): verified. "راغب علامة يعلّم الموسيقى" matches verbatim.
- AB2 DS2-music credential cites AD-MUSIC-1 primary text (ar): the bound text "راغب علامة، 40 عاماً في عالم الموسيقى" is a faithful length-adapted condensation of the AD-MUSIC-1 primary text line (40 years in the music industry). No new claim. Digit 40 is Western. Accepted.
- AB2 DS2-cook field headline cites AD-COOK-1 headline (ar): "سلام دقاق تعلّم الطبخ الشامي" matches verbatim.
- AB2 DS2-cook credential cites AD-COOK-1 primary text (ar): bound text is a faithful condensation of the cleared Best Female Chef in MENA and Michelin award winning Bait Maryam credential. No new claim. Accepted.
- AB2 DS2-acting field headline cites AD-ACTING-1 headline (ar): "قصي خولي يعلّم التمثيل" matches verbatim.
- AB2 DS2-acting credential cites AD-ACTING-1 primary text (ar): bound text "قصي خولي، أحد أبرز الأسماء في العالم العربي" is a faithful condensation. No new claim.
- AB2 DS2-makeup field headline cites AD-MAKEUP-1 headline (ar): "بسام فتوح يعلّم المكياج" matches verbatim.
- AB2 DS2-makeup credential cites AD-MAKEUP-1 primary text (ar): bound text is a faithful condensation. No new claim. Feminine address held correctly per source.
- AB2 DS2-business field headline cites AD-BUSINESS-1 headline (ar): "توفيق كريديه يعلّم بناء الأعمال" matches verbatim.
- AB2 DS2-business credential cites AD-BUSINESS-1 primary text (ar): bound text "توفيق كريديه، بنى عملاً بمليارات الدولارات من الصفر" uses only the cleared credential. Brands For Less and the garage detail are excluded. No new claim.
- AB2 DS2-styling field headline cites AD-STYLING-1 headline (ar): "سيدريك حداد يعلّم التنسيق" matches verbatim.
- AB2 DS2-styling credential cites AD-STYLING-1 primary text (ar): bound text is a faithful condensation of the cleared celebrity stylist credential. No new claim. Feminine address held correctly.
- AB2 DS2-marketing field headline cites AD-MARKETING-1 headline (ar): "إلدا شقير تعلّم التسويق" matches verbatim.
- AB2 DS2-marketing credential cites AD-MARKETING-1 primary text (ar): bound text "إلدا شقير، من أبرز قادة التسويق في العالم العربي بخبرة عقود في صناعة علامات تجارية أيقونية" uses only the cleared credential. Omnicom, Forbes, Cannes, and figures excluded. No new claim.
- AB2 DS2-breadth slot cites AD-BREADTH-1 (ar): verified. No instructor name in this slot.
- AB4 DS4-A still [ar headline] cites EMAIL-SUBJECT-E1 primary (ar): "صيف المهارات يبدأ بخطوة واحدة" matches the source verbatim.
- AB4 DS4-A still [ar subline] cites EMAIL-PREHEADER-E1 (ar): "نخبة من يصنعون المعيار في مجالات عديدة، والدرس الأول مجاني في المجال الذي تختاره." matches the source verbatim.
- AB4 DS4-A still [ar cta chip] cites EMAIL-CTA-E1 (ar): "ابدأ الدرس المجاني" matches verbatim.
- AB4 email header E1 to E5 [ar email header line] slots cite EMAIL-SUBJECT-E1 to E5 primary (ar): all five verified against copy-package.ar.md. All match verbatim.
- AB5 push P1 to P5 [ar push line] slots cite PUSH-BODY-P1 to P5 (ar): all five verified. All match verbatim.
- AB6 DS5 [ar headline] cites AD-RETARGET-1 headline (ar): "أكمل ما بدأته هذا الصيف" matches verbatim.
- AB6 DS5 [ar cta chip] cites AD-RETARGET-1 cta (ar): "أكمل الآن" matches verbatim.
- AB6 DS5 field labels 1 to 7 cite AD-BREADTH-1 field list (ar): the seven field names (الموسيقى، الطبخ، التمثيل، المكياج، الأعمال، التنسيق، التسويق) are drawn directly from the AD-BREADTH-1 field-list line. Verified.
- AB7 DS6 [ar campaign theme label] cites HERO-SIGNATURE theme word (ar) and EMAIL-SUBJECT-E1 and SOCIAL-S1: "صيف المهارات" is the campaign theme carried from the brief and used verbatim across all QA-passed sources. Not an invented product or class title. Accepted.
- AB7 DS6 [ar supporting line] cites HERO-SIGNATURE primary (ar) tail and SOCIAL-S1 line 1: bound text "اختر مجالك، وابنِ مهارة حقيقية مع نخبة من يصنعون المعيار." is the SOCIAL-S1 line 1 with the opening "هذا الصيف،" dropped. Every word in the bound text is present verbatim in SOCIAL-S1 line 1. Faithful length-adapted lockup. No new claim.
- AB7 DS6 [ar cta chip] cites SOCIAL-CTA-S1 (ar): "ابدأ مجاناً" matches verbatim.
- AB9 DS8 [ar landing hero headline] cites LP-HEADLINE-1 (ar): "هذا الصيف، اختر مجالك وابنِ مهارة حقيقية" matches the source verbatim.
- AB9 DS8 [ar landing hero subline] cites LP-SUBHEAD-1 (ar): "تعلّم من نخبة من يصنعون المعيار في مجالهم، عبر مجالات عديدة على منصة واحدة. ابدأ بالدرس الأول مجاناً." matches verbatim.
- AB9 DS8 [ar cta button label] cites LP-CTA-1 (ar): "ابدأ الدرس المجاني" matches verbatim.

Binding integrity: PASS. All source IDs real, all bound strings traceable to QA-passed sources, all length adaptations are faithful subsets with no new words, claims, names, figures, or titles.

### Check 2: Visual-brief fit

- All AR slots are labeled [ar ...], RTL, right-anchored per the design-spec placement notes.
- Slot purposes match the asset brief slot map in creative-package.md: headlines are in upper safe areas, credentials and callouts are in card lower zones, CTAs are in the CTA zone with emerald fill noted, field labels are tile-level, campaign theme label is inside the #1A1A1A card upper zone.
- No slot crosses into a purpose it was not assigned in the asset brief.
- The DS2-breadth [ar instructor name and credential] slot correctly carries the unnamed breadth phrase rather than an instructor name, per the asset brief's note that this slot carries no instructor name.
- AB9 slots are passed to web-design-director as directed by the creative-package handoff.

Visual-brief fit: PASS.

### Check 3: Instructor-naming discipline

- Seven nameable instructors: Ragheb Alama, Salam Dakkak, Kosai Khauli, Bassam Fattouh, Toufic Kreidieh, Cedric Haddad, Elda Choucair. All seven are marked confirm-at-gate in every slot that carries a name. Every credential is drawn from cleared, page-sourced facts only.
- Four non-nameable instructors (Rahma Riad, Sami Al Jaber, Mona Ataya, Mo Islam): not named in any slot. The unnamed breadth phrase "والمزيد عبر مجالات عديدة" is the only form that covers them. Verified across all slots.
- Toufic Kreidieh verify-before-public-use: Brands For Less and the garage detail do not appear in any slot. The DS2-business credential slot carries only "بنى عملاً بمليارات الدولارات من الصفر". Confirmed.
- Elda Choucair verify-before-public-use: Omnicom, Forbes, Cannes, and the figures do not appear in any slot. The DS2-marketing credential slot carries only the cleared descriptor. Confirmed.

Instructor-naming discipline: PASS.

### Check 4: Mechanical

- Em dash (U+2014): searched. No match found in any slot or note.
- Tatweel or kashida (U+0640): searched. No match found anywhere in the file.
- Eastern Arabic-Indic digits (U+0660 to U+0669): searched. No match found. The sole digit used is 40 (DS2-music credential), which is Western.
- Accreditation implication: "مهارة حقيقية" is used throughout. This means real, usable skill and is not an accreditation claim. No certificate-as-accredited language appears in any slot.

Mechanical: PASS.

### Check 5: AR/EN alignment (AR side)

AR covers: AB1, AB2 (8 variants: 7 per-field plus breadth), AB4 (still + email header E1 to E5), AB5 (push P1 to P5), AB6, AB7, AB9.

Slot count per asset:
- AB1: 3 AR slots.
- AB2 per variant: 4 AR slots x 8 variants = 32 slots.
- AB4 still: 3 AR slots.
- AB4 email header: 5 AR slots (one per E1 to E5).
- AB5 push: 5 AR slots (one per P1 to P5).
- AB6: 9 AR slots (1 headline + 7 field labels + 1 CTA).
- AB7: 3 AR slots.
- AB9: 3 AR slots.

The AR slot structure matches the EN slot structure on all assets. No asset brief is covered in AR but not EN, or vice versa. Slot labels are parallel and correctly language-marked ([ar ...] in the AR file, [en ...] in the EN file).

AR/EN alignment (AR side): PASS.

---

## AR file verdict: PASS

All five checks pass. The AR file advances to arabic-copy-qa (gate of record for the length-adapted lockups) and, on that pass, to build. It does not advance to build until arabic-copy-qa (gate of record) confirms. Nothing sends, publishes, or spends.

---

## EN file: full check record

### Check 1: Binding integrity

Source IDs verified against copy-package.en.md. Most slots bind cleanly. One binding integrity failure is identified and recorded below.

Clean bindings:
- AB1 and AB2 per-variant and AB4 Groups A, B, C and AB5 and AB6 and AB9 slots: all source IDs exist, all bound text matches sources verbatim or within faithful length adaptation. Verified.
- AB7 [en campaign theme label] cites SOCIAL-S1 caption opener (en) and LP-HEADLINE-1 (en): "Summer of Skills." matches both sources verbatim. Accepted.
- AB7 [en cta chip] email-channel variant "Explore the roster and start free" cites EMAIL-E1 CTA (en): matches verbatim. Social-channel variant "[Link in bio / Swipe up]" is noted as a social convention slot. Accepted.

Binding integrity failure:

AB7 [en supporting line], condensed overlay form. The file provides two versions of this slot. The full-source version ("Choose any field. Learn from the person who set the standard in it. Build a real skill before summer ends.") is drawn verbatim from SOCIAL-S1 and is acceptable. The condensed overlay version presented as preferred is:

"Choose your field. Build a real skill this summer."

The file claims: "No content is invented: the condensed form uses only words present in the source." This claim is incorrect.

- SOCIAL-S1 says "Choose any field." The condensed form changes "any" to "your", producing "Choose your field." The word "your" in the pairing "your field" does not appear in SOCIAL-S1 in this construction. SOCIAL-S1's only instance of "your" before "field" does not exist; the phrase "Your first lesson" appears separately. "Choose your field" is not a verbatim subset of SOCIAL-S1.
- SOCIAL-S1 says "Build a real skill before summer ends." The condensed form uses "this summer" instead. "This summer" does not appear in SOCIAL-S1.
- The condensed form is not a verbatim subset of LP-HEADLINE-1 or LP-HEADLINE-2 either. LP-HEADLINE-2 carries "Build a real skill this summer." but does not carry "Choose your field."

The condensed overlay form "Choose your field. Build a real skill this summer." is a new construction that introduces phrasing not present verbatim in the single cited QA-passed source (SOCIAL-S1). It is not a length-adapted lockup of that source; it is new copy.

fix_list:
- {
    check: "binding-integrity",
    span: "Choose your field. Build a real skill this summer.",
    fix: "Replace with a verbatim subset of SOCIAL-S1 that fits the slot. The acceptable condensed form using only SOCIAL-S1 words is: 'Choose any field. Build a real skill before summer ends.' If a shorter form is needed, use: 'Choose any field. Build a real skill.' Both phrases are verbatim subsets of SOCIAL-S1. Do not change 'any' to 'your' and do not introduce 'this summer' from a source not cited in this slot. If the intent is to source from LP-HEADLINE-2 ('Build a real skill this summer.'), add LP-HEADLINE-2 as a co-source and adjust the headline accordingly; this requires arabic-copy-qa or english-copy-qa confirmation on the combination."
  }

### Check 2: Visual-brief fit

- All EN slots are labeled [en ...], LTR, left-anchored per the placement notes.
- Slot purposes match the asset brief slot map in creative-package.md. No slot crosses into a purpose not assigned to it.
- The DS2-breadth [en instructor name and credential] slot correctly carries "And more across many fields." rather than an instructor name.
- AB9 slots are passed to web-design-director as directed.

Note: the EN envelope states "ar_canonical: visual-overlay-copy.ar.md does not yet exist as of 2026-06-16." The AR file does now exist (also dated 2026-06-16). This stale note is an internal housekeeping item, not a brand failure. The slot structures are confirmed parallel. No fix required for this note.

Visual-brief fit: PASS (subject to the binding fix above, which affects only the AB7 supporting line slot).

### Check 3: Instructor-naming discipline

- Seven nameable instructors: all seven carry confirm-at-gate in every slot that includes a name, with explicit fallback text (unnamed credential descriptor) if name is not cleared.
- Four non-nameable instructors (Rahma Riad, Sami Al Jaber, Mona Ataya, Mo Islam): not named in any slot anywhere in the EN file. Only "And more across many fields." covers them. Confirmed.
- Toufic Kreidieh verify-before-public-use: Brands For Less and garage detail do not appear in any slot. DS2-business carries only "Built a billion-dollar business from scratch." Confirmed.
- Elda Choucair verify-before-public-use: Omnicom, Forbes, Cannes, and figures do not appear in any slot. DS2-marketing carries only "One of the Arab world's most respected marketing leaders." Confirmed.

Instructor-naming discipline: PASS.

### Check 4: Mechanical

- Em dash (U+2014): searched. No match found in any slot or note.
- Eastern Arabic-Indic digits (U+0660 to U+0669): searched. No match found. The sole digit is 40 (music field slots, AD-MUSIC-1), Western.
- Tatweel (U+0640): no Arabic strings present in the EN file; not applicable.
- Accreditation implication: no certificate-as-accredited language appears in any slot. "A real skill" and "a skill that stays with you" are empowering outcome framings, not accreditation claims.

Mechanical: PASS.

### Check 5: AR/EN alignment (EN side)

EN covers: AB1, AB2 (8 variants: 7 per-field plus breadth), AB4/AB5 (combined section with Groups A, B, C covering still, email header, and push), AB6, AB7, AB9.

Slot count per asset matches the AR file on all assets:
- AB1: 3 EN slots, parallel to 3 AR slots.
- AB2 per variant: 4 EN slots x 8 variants = 32, parallel to AR.
- AB4 still (Group A): 3 EN slots, parallel to 3 AR slots.
- AB4 email header (Group B): 5 EN slots (E1 to E5), parallel to 5 AR slots.
- AB5 push (Group C): 5 EN slots (P1 to P5), parallel to 5 AR slots.
- AB6: 9 EN slots (1 headline + 7 field labels + 1 CTA), parallel to 9 AR slots.
- AB7: 3 EN slots, parallel to 3 AR slots.
- AB9: 3 EN slots, parallel to 3 AR slots.

No asset brief covered in one language and absent from the other. Slot labels parallel and correctly language-marked.

AR/EN alignment (EN side): PASS.

---

## EN file verdict: FAIL

One binding integrity failure: the condensed overlay form for [en supporting line] in AB7 introduces copy not present verbatim in the cited QA-passed source. The exact fix is specified above.

The EN file returns to copywriter-en with the fix list. On resubmission, copywriter-en corrects the AB7 [en supporting line] condensed overlay form, records the corrected source, and resubmits to english-copy-qa (gate of record) and then back to this gate. No other item in the EN file fails.

---

## Fix list (EN file only)

1. {
     check: "binding-integrity",
     asset: "AB7 / DS6 [en supporting line] condensed overlay form",
     span: "Choose your field. Build a real skill this summer.",
     fix: "Replace with a verbatim subset of SOCIAL-S1. Acceptable condensed forms are: 'Choose any field. Build a real skill before summer ends.' or the further shortened 'Choose any field. Build a real skill.' Do not use 'your field' (SOCIAL-S1 uses 'any field') and do not use 'this summer' (SOCIAL-S1 uses 'before summer ends'). If a different source such as LP-HEADLINE-2 is intended, cite it explicitly alongside SOCIAL-S1 and confirm the combination does not introduce a new message."
   }

---

## Gate routing

- AR file (visual-overlay-copy.ar.md): brand-qa PASS. Still requires arabic-copy-qa gate-of-record pass for the length-adapted lockups before advancing to build. On arabic-copy-qa pass, the AR file advances to the designer for build, pending compliance-privacy-reviewer pass.
- EN file (visual-overlay-copy.en.md): brand-qa FAIL. Returns to copywriter-en with the fix list above. Copywriter-en corrects the AB7 [en supporting line] condensed form, resubmits to english-copy-qa (gate of record), and then back to brand-qa-reviewer. No other slot is affected.
- Both files: compliance-privacy-reviewer must also pass before any asset advances. That gate runs alongside this one and is not yet confirmed.
- Human gate: nothing publishes, sends, or spends until Ahmed approves. All open items from creative-package.md (OI-1 through OI-9) surface at the human gate per instructor and per item.

Status: verdict filed 2026-06-16. Not approved to advance. Nothing builds, publishes, or spends.
