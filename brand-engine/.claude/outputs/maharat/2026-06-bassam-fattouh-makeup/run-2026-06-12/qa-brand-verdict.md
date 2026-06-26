# Brand QA Verdict: Bassam Fattouh Teaches Makeup
## run-2026-06-12 | verdict date: 2026-06-12
## reviewer: brand-qa-reviewer | gate: final brand gate

Status of prior gates confirmed before this review:
- skill_eval: self-checked and passed by each producing agent (per file headers and self-QA checklists).
- arabic-copy-qa: files 01, 02, 03, 04 carry status "pending arabic-copy-qa" or note it must run. This gate has NOT been confirmed as passed before this brand review.
- english-copy-qa: same files carry status "pending english-copy-qa". NOT confirmed passed.
- compliance-privacy-reviewer: no verdict on record in this run folder at time of this review.

Procedural note: the prior-gate prerequisite (arabic-copy-qa and english-copy-qa passed, compliance-privacy-reviewer verdict in flight) is NOT confirmed for assets 01 through 04. This brand gate runs as instructed by the orchestrator, but the overall package cannot advance to the human gate until arabic-copy-qa, english-copy-qa, and compliance-privacy-reviewer verdicts are all confirmed. This note does not change the brand verdicts below; it is a routing flag for the orchestrator.

---

## ASSET 01: Owned Messaging (email, app push, WhatsApp)
### File: 01-owned-messaging-email-push-whatsapp.ar-en.md

**VERDICT: PASS**

Checks run:

Voice and tone:
- Plain, confident, empowering throughout. No deficit framing of the reader.
- Feminine address consistent: ابدئي، شاهدي، تعلمي، اختاري, and all verb conjugations use the feminine second person throughout every email and push.
- Thmanyah benchmark met: short sentences, concrete nouns, active voice.
- No urgency theater, no invented deadline.

Mechanical:
- No em dashes found anywhere in the file (commas, colons, and periods used throughout).
- No tatweel or kashida (U+0640) found.
- Western numerals only (3, 20, 25, 53, 7 and dates throughout). No Eastern Arabic-Indic digits.
- RTL-safe: Arabic copy leads each asset; numerals and Latin URLs placed at clause ends or on their own lines.

Guardrails:
- No invented Skill Path titles.
- Lesson themes referenced match the confirmed list exactly (Foundation 101, No-Makeup Makeup, Day to Night, Everyday Glam, Smokey Eyes, Color Glam, Graphic Metallic Look, A Career in Makeup, Final Touches, inclusive guidance). "A Career in Makeup" is correctly excluded from this file to avoid any career-promise reading.
- Bassam Fattouh named because published page confirms the association. Catalog confirmation flagged as the first blocking launch item (OPEN ITEM 1).
- No accreditation implied. Completion certificate described as "documenting the journey" only, matching the live-site framing.
- No career or professional outcome promised.
- No invented price, promo, trial, or discount. Public price reference used exactly: "بأقل من 7 دولار شهريًا تُدفع سنويًا" / "under $7 a month billed annually".
- No bridal positioning. Non-bridal class kept distinct.
- No client or brand-line names.
- No personal or sensitive data in any URL or link.
- WhatsApp: prior opt-in and pre-approved templates required, opt-out line on every message, consent and platform flagged as OPEN ITEMS.

Open items correctly flagged: all 5 open items from _RUN-CONTEXT are surfaced inline and not resolved by invention.

No findings. Asset passes all brand checks.

---

## ASSET 02: Organic Social
### File: 02-organic-social.ar-en.md

**VERDICT: FAIL**

3 failures found. Fix list below.

Checks run (all passing unless noted):

Voice and tone:
- Overall angle is empowering and correct: beauty as confidence, technique and confidence only, no career-outcome promise.
- "ليست مسألة إخفاء، بل إبراز" (ORG-04 slide 2): empowering reframe, not a violation. Pass.
- No deficit framing of the learner.

Mechanical:
- No em dashes. Pass.
- No tatweel. Pass.
- Western numerals only. Pass.

Guardrails: all pass (no invented lineup, no invented price, no accreditation, no bridal, no client names, no personal data in links, REAL ASSET REQUIRED correctly noted).

**FAILURE 1: feminine address violation, ORG-06 (X/Twitter)**

- Check: voice (feminine address, beauty and style campaign).
- Offending span: "يعلّمك المكياج خطوة بخطوة" (ORG-06 AR caption, line reading "أكثر من 25 سنة من الخبرة، وأحد أشهر خبراء التجميل في العالم العربي، يعلّمك المكياج خطوة بخطوة.").
- The pronoun "كَ" (the attached pronoun in "يعلّمك") is masculine or ungendered. The rule requires feminine address throughout for this beauty-and-style campaign.
- Required fix: replace "يعلّمك" with "يعلّمكِ" (feminine second person, kasra on the kaf). Full corrected line: "أكثر من 25 سنة من الخبرة، وأحد أشهر خبراء التجميل في العالم العربي، يعلّمكِ المكياج خطوة بخطوة."

**FAILURE 2: feminine address violation, ORG-08 (YouTube Shorts)**

- Check: voice (feminine address).
- Offending span: "بسام فتّوح يعلّمك خطوات السموكي والألوان في صفه، خطوة بخطوة." (ORG-08 AR caption).
- Same violation: "يعلّمك" uses the masculine/ungendered attached pronoun.
- Required fix: replace "يعلّمك" with "يعلّمكِ". Full corrected line: "بسام فتّوح يعلّمكِ خطوات السموكي والألوان في صفه، خطوة بخطوة."

**FAILURE 3: feminine address inconsistency, ORG-10 (Instagram Reels)**

- Check: voice (feminine address consistency within the same sentence).
- Offending span: "في صفه، يعلّمك بسام فتّوح كيف تختارين وتطبّقين الأساس المناسب لبشرتك، مع إرشادات للبشرة الناضجة وللمحجبات." (ORG-10 AR caption).
- The verb "يعلّمك" uses the masculine/ungendered pronoun, while "تختارين" and "تطبّقين" immediately after it are correctly feminine. The sentence is internally inconsistent and the opening verb violates the feminine-address rule.
- Required fix: replace "يعلّمك" with "يعلّمكِ". Full corrected line: "في صفه، يعلّمكِ بسام فتّوح كيف تختارين وتطبّقين الأساس المناسب لبشرتك، مع إرشادات للبشرة الناضجة وللمحجبات."

Routing: return to copywriter-ar with these 3 targeted fixes. All other organic social copy passes. Resubmit this asset after correction.

---

## ASSET 03: Paid Advertising
### File: 03-paid-advertising.ar-en.md

**VERDICT: PASS**

Checks run:

Voice and tone:
- SET B option 1: "وصلتِ إلى سقف الدروس المجانية؟ / Hit the ceiling of free tutorials?" Assessed in context. This is a self-selecting hook for the advancing-enthusiasts segment (segment 2), which is defined as learners who have already been consuming free tutorials and want the next level. The feminine address is correct (وصلتِ). This framing names a situation the reader recognizes in herself; it is not a deficit-framing of her person or natural appearance. Pass.
- SET F option 1 (TikTok, AR): "وقفي تخمنين خطوات مكياجك. / Stop guessing your makeup steps." Reviewed carefully. "وقفي تخمنين" is a direct-response hook at TikTok-native register, and it is immediately followed by an empowering path (Bassam Fattouh walks through every step). The subject is technique steps, not the reader's appearance or worth. It does not frame the reader as deficient as a person. This falls within the permitted range for the TikTok tone register (native, lighter, per the asset's stated format guidance). Pass on balance.
- All remaining sets: empowering framing throughout. Feminine address used consistently (وصلتِ، تعلّميها، ارفعي، اشتركي, etc.).

Mechanical:
- No em dashes. Pass.
- No tatweel. Pass.
- Western numerals only (20, 25, 53, 7, percentages, dates). Pass.
- No Eastern Arabic-Indic digits. Pass.

Guardrails:
- No invented Skill Path titles. Pass.
- All lesson themes from the confirmed list only (no-makeup-makeup, smokey eyes, color glam, graphic metallic, foundation, day to night, final touches, inclusive guidance). Pass.
- "A Career in Makeup" not used as a promise or a standalone claim anywhere in the ad copy. Pass.
- Bassam Fattouh named, catalog confirmation flagged as OPEN ITEM 1. Pass.
- No accreditation claim anywhere. Pass.
- No invented price, promo, trial, or discount. Public price reference used exactly. Pass.
- No bridal positioning. Bridal queries explicitly excluded as negatives in the keyword strategy. Pass.
- No client or brand-line names. Pass.
- No personal or sensitive data in any URL or audience definition. Lookalike and retargeting audiences flagged as gated. Pass.
- Budget by percentage only, currency unconfirmed and not invented. Pass.
- Generated visuals text-free, no Bassam likeness, OPEN ITEM 6 correctly surfaced. Pass.

No failures. Asset passes all brand checks.

---

## ASSET 04: Blog and Content
### File: 04-blog-content.ar-en.md

**VERDICT: PASS**

Checks run:

Voice and tone (flagship article AR):
- "تعزيز ما لديك بلمسة خفيفة، لا اخفاء اي شيء": this is the article's thesis. "لا اخفاء اي شيء" means "hide nothing" and is empowering, not deficit-framed. It is the exact mirror of the brand-voice rule (skin at its best, enhance not correct). Pass.
- "الجمال في المكياج بدون مكياج هو معرفة متى يكفي ما فعلت": empowering, confident, correct.
- No deficit framing of the reader, no correction language, no mention of flaws.
- Brief D note "never 'hide flaws' or 'عيوبك'" is documentation within the brief, not a violation in customer-facing copy. Pass.

Voice and tone (flagship article EN):
- "enhance what you have, hide nothing": empowering. Pass.
- "This quiet first step is what separates a heavy finish from a look that breathes": a comparative about technique quality, not a critique of the reader. Pass.
- No deficit framing. Pass.

Mechanical:
- No em dashes. Pass.
- No tatweel. Pass.
- Western numerals only (25, $7, 2:47, dates). Pass.

Guardrails:
- No invented Skill Path titles. Pass.
- Lesson themes used match the confirmed list. The "color glam / graphic metallic" article is correctly held back as OPEN ITEM 2. Pass.
- No search volume numbers invented. Method-derived clusters noted as estimates, not claimed volumes. Pass.
- Bassam Fattouh named, catalog confirmation flagged as OPEN ITEM 3. Pass.
- No accreditation implied. Pass.
- No career or professional outcome promised. Pass.
- Public price reference only, no invented promo. Pass.
- No bridal positioning. Pass.
- No client or brand-line names. Pass.
- No personal or sensitive data in any URL. Pass.
- CTA structure correct: primary "watch free first chapter", secondary "see the plans". No invented conversion mechanic. Pass.

No failures. Asset passes all brand checks.

---

## ASSET 05: Visual Prompt Library
### File: 05-visual-prompts.md

**VERDICT: PASS**

Checks run:

Visual constants:
- Every prompt specifies #141414 as the background ground. Pass.
- Every prompt specifies #1A1A1A as the card surface or secondary surface plane. Pass.
- Every prompt specifies #009975 as the emerald accent, consistently as a single-element accent (one ferrule, one pod, one swatch, one pan among twelve). The accent is never specified as a flood fill or a dominant color. Pass.

Text-free generation:
- Every prompt contains the negative instruction "no text, no letters, no Arabic script, no Latin text, no numerals, no watermark, no logo" in its negative prompt block. Pass.
- The hard rule at the file header is explicit and repeated. Pass.
- All overlay slots are empty and directed to copywriter-ar or copywriter-en to fill at build. Pass.

No generated Bassam likeness:
- The hard rule is stated at the top of the file ("HARD RULE: NO GENERATED LIKENESS OF BASSAM FATTOUH") and enforced in every prompt subject description. No prompt calls for any instructor face, portrait, silhouette, or likeness.
- Instructor-likeness slots are bridged with still-life and technique-hands subject matter (rights-question sidestepped correctly).
- OPEN ITEM 1 (rights-cleared real assets) flagged as blocking. Pass.

Safe overlay areas:
- Every prompt specifies aspect ratio, pixel dimensions, and copy-overlay safe areas (upper zone, lower CTA strip, lateral margins). Pass.

Premium and uncluttered:
- Every prompt specifies generous negative space, a maximum of four objects in any still-life, directional controlled lighting, and near-black dominant ground. Pass.
- Motion prompts specify slow, deliberate pacing with a single visual beat. Pass.

Guardrails:
- No invented lesson lineup, no price, no promo anywhere in this file. Pass.
- Rendering flagged as a gated action pending tool approval. Pass.

No failures. Asset passes all brand checks.

---

## OVERALL VERDICT

| Asset | File | Brand QA result |
|---|---|---|
| 01 Owned messaging (email, push, WhatsApp) | 01-owned-messaging-email-push-whatsapp.ar-en.md | PASS |
| 02 Organic social | 02-organic-social.ar-en.md | FAIL (3 items) |
| 03 Paid advertising | 03-paid-advertising.ar-en.md | PASS |
| 04 Blog and content | 04-blog-content.ar-en.md | PASS |
| 05 Visual prompt library | 05-visual-prompts.md | PASS |

**Overall brand QA: FAIL.**

One asset (02-organic-social.ar-en.md) fails on 3 instances of masculine/ungendered pronoun used in customer-facing Arabic copy for a feminine-address campaign. These are targeted, character-level fixes (3 instances of "يعلّمك" to "يعلّمكِ" in ORG-06, ORG-08, and ORG-10). All other copy in file 02 passes.

**Routing instruction:** Return 02-organic-social.ar-en.md to copywriter-ar with the 3 fix items above. All other 4 assets are brand-cleared and may hold pending resolution of the routing flags below. Once the corrected file 02 is resubmitted and passes this gate, the package may advance, subject to the gate-stack conditions below.

---

## Gate-stack routing flags (for the orchestrator)

The package may NOT advance to the human gate until ALL of the following are confirmed:

1. arabic-copy-qa: a passed verdict must be on record for assets 01, 02 (corrected), 03, and 04. Not confirmed at time of this review.
2. english-copy-qa: a passed verdict must be on record for the same assets. Not confirmed.
3. compliance-privacy-reviewer: a verdict must be in flight or passed. Not confirmed.
4. Brand QA on the corrected 02-organic-social.ar-en.md: must resubmit to this gate after the 3-item fix.

These are routing conditions, not additional brand failures. The 4 brand-passing assets are ready for their prior gate confirmations to be recorded.

---

produced_by: brand-qa-reviewer
run_id: run-2026-06-12
campaign_id: 2026-06-bassam-fattouh-makeup
verdict_date: 2026-06-12
status: fail (one asset). Package does not advance until file 02 is corrected, resubmitted, and prior gate verdicts are confirmed.
