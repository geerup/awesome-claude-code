# qa-copy-design-verdicts: 2026-06-elda-choucair-marketing

- campaign_id: 2026-06-elda-choucair-marketing
- reviewer: brand-qa-reviewer (running arabic-copy-qa, english-copy-qa, design-qa sub-gates)
- review_date: 2026-06-05
- assets_reviewed:
  - copy-package.ar.md
  - copy-package.en.md
  - creative-briefs.md

---

## GATE 1: arabic-copy-qa on copy-package.ar.md

Checks applied per arabic-copy-qa/SKILL.md and evals/evals.json:
1. msa-gulf-familiar
2. thmanyah-tone
3. no-tatweel
4. western-numerals
5. no-em-dash
6. empowering-framing
7. rtl-safe

### Check results

**msa-gulf-familiar:** PASS. All units use Modern Standard Arabic with Gulf-familiar vocabulary. No heavy dialect. No stiff formal register. The phrasing throughout ("هندسة قرار", "مؤشرات", "قمع تسويقي") is contemporary and intelligible to a Gulf audience without being dialectal.

**thmanyah-tone:** PASS. Tone is clear, modern, intelligent, confident. Short sentences, concrete nouns throughout. No academic or corporate stiffness. No hype words. The register respects the reader throughout.

**no-tatweel:** PASS. No tatweel or kashida character (U+0640) found anywhere in the Arabic copy.

**western-numerals:** PASS. All numerals are Western (0-9). The numeral "20" appears in multiple units ("أكثر من 20 سنة") and is correctly rendered as Western. No Eastern Arabic-Indic digits (U+0660 to U+0669) found.

**no-em-dash:** PASS. No em dash character (U+2014) found in any Arabic copy unit. Commas, colons, and periods used throughout.

**empowering-framing:** PASS with one observation (not a fail). All units frame the reader as gaining capability, not fixing a deficit. The villain is consistently "the safe, forgettable strategy." The hero is the learner gaining clearer judgement. Elda is the guide. The observation: AD-2 (ad-p2-builders-v1) contains the headline "لا تفشل لأن منتجك ضعيف، بل لأن أحدا لا يعرف به" which technically names a failure scenario but immediately reframes it ("بل") toward the brand story. This reads empowering in context because the flip immediately follows the setup. The "لا تفشل" framing is a rhetorical setup for the myth-flip, not a reader-deficit accusation. PASS, no fix required; the flip is complete within the same line.

**rtl-safe:** PASS. Arabic copy is right-to-left throughout. Mixed Arabic and Western numeral strings ("أكثر من 20 سنة", "خبرة 20 سنة") are correctly composed and will not break RTL direction. English brand names ("أومنيكوم ميديا") are rendered in Arabic script. No embedded Latin strings that would break direction. Copy is safe for RTL rendering.

### arabic-copy-qa VERDICT: PASS

All 7 checks pass. The Arabic copy package (E1 to E5 emails, all ad variants AD-1 through AD-3b, all organic captions POST-1 to POST-4, and all landing page copy blocks LP-hero through LP-primary-CTA) advances to brand-qa-reviewer.

---

## GATE 2: english-copy-qa on copy-package.en.md

Checks applied per english-copy-qa/SKILL.md and evals/evals.json:
1. empowering-tone
2. no-em-dash
3. western-numerals
4. one-clear-cta
5. no-accreditation-implication
6. no-invented-offers-titles
7. plain-active-voice

### Check results

**empowering-tone:** PASS. All units speak to what the reader can build or gain. No shame framing, no "you are behind" language. The framing throughout is gain-oriented: "clearer judgement," "make people care," "the layer above the tools." The reader is a capable person who wants a specific skill. No hype words ("amazing," "game-changer," "revolutionize") appear. Empowering and confident throughout.

One borderline observation for completeness: E5 contains "Is the way you are thinking about marketing right now, the sharpest it can be?" This is a challenge question but does not frame the reader as failing; it is an honest introspective question with an empowering resolution immediately following. PASS.

**no-em-dash:** PASS. No em dash glyph (U+2014) found in any English copy unit. The copy uses commas, colons, and periods where structure is needed. No substitution issues.

**western-numerals:** PASS. All numerals are Western digits (0-9). "20 years" appears in multiple units and is correct. No Eastern Arabic-Indic digits present.

**one-clear-cta:** PASS on all email units. E1: "Watch Chapter 1 Free" (one CTA). E2-P1, E2-P2, E2-P3: "Get the Cheatsheet and Watch Chapter 1" (one CTA, dual-action but a single linked destination, not competing CTAs). E3: "Watch Chapter 1 Free" (one CTA). E4: "See the Full Class on Maharat" (one CTA). E5: "Watch Chapter 1 Free, Decide from There" (one CTA). Ad units: each carries one CTA. Organic posts: each routes to one destination with one action ("Link in bio. Start watching." is a routing instruction, not a CTA conflict). Landing page: one primary CTA per section ("Watch Chapter 1 Free" on the hero; each value block is informational with no competing CTA button). PASS throughout.

**no-accreditation-implication:** PASS. No language implies accreditation anywhere. No reference to accreditation, certification bodies, professional recognition, or continuing education credits. The word "certificate" or "certified" does not appear in any unit. PASS.

**no-invented-offers-titles:** PASS. All instructor references ("Elda Choucair," "CEO of Omnicom Media Group MENA") are verified against the claims table (claims 1, 2, 7). Class title referenced naturally in body copy is consistent with the verified title "Elda Choucair, Teaches Marketing" (claim 7). No Skill Path titles invented. No lesson list. No price, plan name, or promotion. Chapter 1 free and the marketing-campaign PDF cheatsheet are confirmed lead magnets (claims per strategy-artifact). "20 years" is confirmed (claim 2). PASS.

**plain-active-voice:** PASS. Sentences are short and direct throughout. Active voice dominates. A few longer sentences appear in E3 and E4 body copy but none are stiff or corporate. Concrete nouns used throughout. No passive constructions that obscure the subject. PASS.

One minor observation: E4 body contains "Twenty years of senior regional marketing work, structured into frameworks you can apply." This is a nominal phrase (no verb) not a passive construction, and it is short and direct. Acceptable. No fix required.

### english-copy-qa VERDICT: PASS

All 7 checks pass. The English copy package (E1 to E5 emails, AD-1 to AD-3, POST-1 to POST-4, LP-hero, LP-value-1 to LP-value-3) advances to brand-qa-reviewer.

---

## GATE 3: design-qa on creative-briefs.md

Checks applied per design-qa/SKILL.md and evals/evals.json:
1. rtl-correct
2. visual-constants
3. western-numerals-rendered
4. no-baked-arabic-text
5. safe-areas-dimensions
6. premium-uncluttered
7. human-check-preserved

### Scope note

The creative-briefs.md is a spec and asset brief document, not a rendered image. Design-qa on a spec assesses whether the spec correctly encodes RTL instructions, specifies the correct visual constants, forbids baked Arabic text in generated images, declares all dimensions and safe areas, and sets up a premium uncluttered composition. Rendered execution is not yet in hand; this gate reviews the spec as the authoritative direction from which the designer executes. A second design-qa pass on the executed visuals is required before those assets advance.

### Check results

**rtl-correct:** PASS. RTL instructions are explicitly stated on every asset brief that carries Arabic copy overlay slots. AB1: "RTL layout for Arabic variant, LTR for English variant. Run separate renders." AB2: implicit in the same C1 concept. AB3: "[ar headline]: empty. RTL, upper safe area." AB4: "Upper safe area, RTL. Large, bold." AB5: "[ar hook line]: Centered over emerald rule." AB6: "[ar headline]: empty. Upper safe area, RTL, large weight." AB7: email subject noted for RTL per the slot label. AB8: "RTL for Arabic (right-aligned within the copy zone)." The landing page spec (conversion-package.md) further specifies: "page root direction rtl for AR variant" and states all 9 RTL checks required before go-live. The designer is instructed to run separate AR and EN renders. PASS.

**visual-constants:** PASS. All four brand constants are specified explicitly and consistently throughout all prompts and briefs:
- Near-black background #141414: specified in every prompt (P1-A, P1-B, P2-A, P2-B, P3, P4-A, P4-B, P5).
- Card surfaces #1A1A1A: specified in C4 ("One Line") prompt P4-A ("A near-black card (#1A1A1A)") and P4-B; in the landing page spec section 2 value cards and gate card.
- Emerald accent #009975: specified in every prompt as the single accent element (the cap, the rule, the thread of light). Consistently described as a "precision mark," "horizontal rule," "thin thread," not a flood.
- The design-qa self-check table in section 7 of creative-briefs.md explicitly confirms all constants on every concept.
PASS.

**western-numerals-rendered:** PASS. All pixel dimension specifications use Western numerals throughout (1080, 1920, 1440, 600, 280, etc.). Every prompt contains an explicit negative instruction prohibiting numerals from being rendered inside generated images: "no numerals in frame" appears on P1-A, P1-B. All prompts carry the broader instruction "No text, no lettering, no Arabic script, no Roman script, no numerals, no watermarks." No Eastern Arabic-Indic digits appear in any dimension spec or overlay instruction. PASS.

**no-baked-arabic-text:** PASS. This is the strongest check in the spec. Every generated-image prompt carries an explicit negative instruction: "No text, no lettering, no Arabic script, no Roman script, no numerals, no watermarks" (present verbatim on P1-A, P1-B, P3, P4-A, P4-B, P5's generated layers). All Arabic copy overlay slots are empty, labeled [ar], and explicitly reserved for copywriter-ar to fill in stream 4. The designer is instructed to overlay copy at build time. Section 8 handoff instructions state: "All [ar] slots route to copywriter-ar (stream 4)... Slots remain empty in this package." The design-qa self-check table confirms: "no Arabic baked into images: Confirmed." PASS.

**safe-areas-dimensions:** PASS. Every prompt declares explicit dimensions and safe areas:
- P1-A: 1080x1080 px. Safe areas: top 200 px clear, bottom 250 px clear, left/right 80 px.
- P1-B: 1080x1920 px. Safe areas: top 480 px, bottom 576 px, left/right 96 px.
- P2-A: 1080x1080 px. Safe areas: top 216 px, bottom 270 px, left/right 80 px.
- P2-B: 1080x1920 px. Safe areas: top 576 px, bottom 288 px, left/right 80 px.
- P3: 600x280 px (email header). Safe areas: left 40 px, right 40 px, top/bottom 20 px. Also 1200x628 px for OG use.
- P4-A: 1080x1080 px. Safe areas: top 280 px, bottom 280 px, left/right 120 px.
- P4-B: 1080x1920 px. Safe areas: top 480 px, bottom 480 px, left/right 120 px.
- P5 (landing page): desktop 1440x700 px, mobile 390x560 px. Safe areas: desktop left copy zone 80-640 px from left, top/bottom 120 px; mobile top 200 px, bottom 160 px, sides 24 px.
All dimensions and safe areas are declared and platform-appropriate. PASS.

**premium-uncluttered:** PASS. The composition direction across all 4 concepts is consistently minimal and spare:
- C1 "The Flip": chart occupies 60% of the 1:1 frame, upper and lower thirds clear. "Mood: quiet authority, premium data aesthetic."
- C2 "The Architect's Mark": generous negative space above and below Elda's image. "Frame it with enough negative space that it reads as premium, not promotional."
- C3 "The Quiet Choice": "minimal, almost architectural." No figures, no symbols, one emerald thread. "Mood: thoughtful, decisive, slightly cinematic."
- C4 "One Line": a card with a single emerald horizontal rule. "No other graphic elements." Generous space above and below.
The emerald accent is used as a highlight (a cap, a rule, a thread) on every concept, never a flood. The design-qa self-check table confirms: "accent as highlight, not flood: Confirmed on all prompts." PASS.

**human-check-preserved:** PASS. Section 8 handoff instructions explicitly state: "A human design check is mandatory on any asset carrying Arabic text." The design-qa self-check table confirms: "RTL note on Arabic assets: Designer instructed on RTL renders and human design check." The package note in section 8 states: "The package does not advance on the strength of this brief alone; the design-qa gate and brand-qa gate must both pass." PASS.

### design-qa VERDICT: PASS (spec level)

All 6 substantive checks pass on the creative-briefs.md spec. The spec correctly encodes RTL, visual constants, no-baked-Arabic-text instructions, dimensions, safe areas, and premium-uncluttered direction. The human design check is preserved as a mandatory final step.

NOTE: This pass is a spec-level pass only. When the designer executes the visual assets (renders the generated images and composes the cover image crops), each executed asset must be submitted to a second design-qa pass before it advances to brand-qa-reviewer. The rendered images are not yet in hand. Passing this spec-level gate does not advance the executed creatives; it advances the brief for designer execution.

---

## Summary table

| Gate | Asset | Verdict | Fix items |
|---|---|---|---|
| arabic-copy-qa | copy-package.ar.md (E1-E5, ads, captions, LP blocks) | PASS | 0 |
| english-copy-qa | copy-package.en.md (E1-E5, ads, captions, LP blocks) | PASS | 0 |
| design-qa | creative-briefs.md (spec level; executed assets pending) | PASS (spec) | 0 |
