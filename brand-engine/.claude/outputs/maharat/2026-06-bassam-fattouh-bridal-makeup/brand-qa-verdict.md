# brand-qa-verdict: Bassam Fattouh bridal makeup, non-payer lifecycle

v2 verdict: re-run on the updated v2 copy-package (preheaders added, subjects mobile-tuned,
frameworks applied per funnel stage, winback posture on M4 non-opener variant).

```
gate:     brand_qa
result:   pass
fix_list: []
```

---

## Common envelope

- campaign_id: 2026-06-bassam-fattouh-bridal-makeup
- produced_by: brand-qa-reviewer
- stream: cross-cutting brand gate (runs last on every customer-facing asset)
- asset_reviewed: outputs/2026-06-bassam-fattouh-bridal-makeup/copy-package.md (v2)
- status: verdict issued. This is not an approval to send. Only Ahmed at the human gate approves.
- qa:
  - brand_qa: pass (all 17 checks, v2 copy-package)

---

## Prior-gate validation

Required prior gates for a stream 4 Arabic copy package:

- skill_eval: pass. Stated in the copy-package v2 envelope. Email-copy and subject-line checks
  confirmed passed: one clear CTA per email, mobile subject length with key word front-loaded
  in the first 30 characters, deliberate preheader present, no banned claims, no invented offer.
- arabic_qa: pass. Self-applied by copywriter-ar and reported in the v2 envelope; routes
  formally to arabic-copy-qa as the required prior gate. Self-check result accepted per the
  task instruction stating arabic-copy-qa was self-applied and reported pass.
- english_qa: na. Arabic-only package. No English copy variants in scope.
- design_qa: na. No visual asset in this package.
- compliance: verdict on file. compliance-privacy-reviewer issued a pass (design-only,
  not-sendable) on 2026-06-02. That verdict listed blocking open item 2 as the copy-package
  compliance and brand_qa gates still pending. This brand-qa gate now resolves the brand_qa
  side. The compliance reviewer runs alongside this gate; both must pass to advance the asset.

Prior-gate state is valid. Brand QA proceeds.

---

## Check results (17 checks, all pass)

### 1. Voice: plain, confident, empowering, never deficit-framed

Result: PASS.

All 5 email variants, all 5 subject line sets, and all 5 preheaders reviewed.

- M1 opens with "إطلالة عروس تصنعينها بيديك", leading with what the reader can create.
- M2 leads with "تتعلمين من فنان مكياج رائد في المنطقة", framing access to expertise as
  a capability gain.
- M3 opens "افتحي الباب لمهارات لا تتوقف عند درس واحد", framing the subscription as an
  opening, not a remedy for a deficiency.
- M4-nonopener (PAS without shame, winback posture) uses "هذا طبيعي في زحمة الأيام" to
  normalize a missed email without blame or pressure. Problem is named as life being busy,
  never as a fault of the reader.
- M4-engaged closes with "ابني إطلالة تفخرين بها", empowering and forward-looking.

No message implies the reader is behind, lacking, failing, or needs fixing. Subject lines and
preheaders carry the same empowering posture throughout. No deficit framing found in any span.

### 2. Voice: Thmanyah tone (clear, modern, intelligent, never stiff)

Result: PASS.

Short active sentences and concrete nouns throughout all 5 variants, all subject sets, and all
preheaders. No academic, corporate, or hype register detected. The v2 preheaders read as one
clear, purposeful added promise per message, in the same register as the body, not as filler
or subject-line spillover.

### 3. Voice: Arabic-first

Result: PASS.

All customer-facing copy is Arabic. The only non-Arabic text in the package is the three
bracketed build-time placeholder tokens in M3 body:
  [PRICE / PLACEHOLDER from brief]
  [PLAN if named from brief]
  [PROMO if any from brief]

These are explicitly marked as tokens to be replaced from confirmed brief values before any
send. They are not shipped copy. No English prose appears in any customer-facing span.

### 4. Mechanical: no em dash glyph

Result: PASS.

No em dash glyph [em dash] (U+2014) is present in any customer-facing span, subject line,
preheader, or internal copy field. Grep-confirmed zero matches across the entire file.
Separators used throughout are commas, colons, and periods only.

### 5. Mechanical: no tatweel or kashida

Result: PASS.

No tatweel or kashida (U+0640) character is present anywhere in the Arabic copy, subject
lines, or preheaders. Grep-confirmed zero matches across the entire file.

### 6. Mechanical: Western numerals only

Result: PASS.

No Eastern Arabic numerals (Arabic-Indic, U+0660 to U+0669) are present anywhere in the
file. Grep-confirmed zero matches. The only digits present are Western (0 to 9), appearing
solely in internal metadata fields (hex color references, character-count annotations, section
numbering), none of which are customer-facing copy.

### 7. Mechanical: RTL renders correctly

Result: PASS.

Arabic is the primary direction throughout all 5 variants, all subject lines, and all
preheaders. The three bracketed placeholder tokens in M3 body are Latin-script build-time
substitution markers that are replaced before the message renders to any reader. No
mixed-direction constructs are present that would break RTL rendering.

### 8. Mechanical (v2): deliberate preheaders in the 40 to 90 character band

Result: PASS.

All 5 preheaders reviewed. Each is a purpose-written line that adds a distinct, honest promise
that is true to its email body. None is an accidental spill of body text. All 5 lines are pure
Arabic, RTL-safe, and fall within the 40 to 90 character band:

- M1: "بسام فتوح يشرح فن مكياج العرائس خطوة بخطوة على مهارات، وأنت من يصنع الإطلالة"
- M2: "ترين كيف يفكر فنان محترف، وكيف يبني إطلالة عروس متكاملة تبقى مهارتها معك"
- M3: "خطة واحدة تفتح لك تعلما متواصلا من خبراء المنطقة، والماستر كلاس بدايتك"
- M4-nonopener: "ماستر كلاس بسام فتوح لمكياج العرائس ما زال متاحا وقت ما تجهزين، بلا ضغط"
- M4-engaged: "اشتراك واحد يمنحك الماستر كلاس وتعلما متواصلا، وخطوتك الأخيرة تبدأ اليوم"

All 5 preheaders read as intentional added value, not filler. No defects.

### 9. Mechanical (v2): mobile subject line length and key-word front-loading

Result: PASS.

All 5 primary subject lines reviewed against the 30 to 40 character target band with the key
word inside the first 30 characters:

- M1 primary "إطلالة عروس تصنعينها بنفسك مع بسام فتوح": 38 characters, "إطلالة عروس"
  front-loaded in the first 30. In band.
- M2 primary "تعلمي إطلالة العروس من فنان مكياج رائد": 37 characters, "تعلمي" and
  "إطلالة العروس" front-loaded in the first 30. In band.
- M3 primary "ابدئي اشتراكك وتعلمي بلا توقف على مهارات": 38 characters, "ابدئي اشتراكك"
  front-loaded in the first 30. In band.
- M4-nonopener primary "ما زالت إطلالة العروس بانتظارك": 29 characters, deliberate soft
  winback line held just under the band on purpose, as noted in the envelope. Key word
  "ما زالت إطلالة العروس" inside the first 30. Intentional noted exception.
- M4-engaged primary "آخر دعوة لتبدئي رحلتك مع مهارات": 30 characters, at the band floor,
  "آخر دعوة" front-loaded. In band.

Alternatives span the band with one tight line each for test purposes, as stated in the
envelope. No defects.

### 10. Guardrail: no invented Skill Path titles or content lineup

Result: PASS.

No lesson count, module name, duration, or lesson sequence appears in any variant, subject
line, or preheader. The only content referenced is the real Masterclass title "Bassam Fattouh
Teaches Bridal Makeup" and its Arabic rendering "ماستر كلاس بسام فتوح لمكياج العرائس", which
matches the brief (section 4) exactly. The phrase "درس واحد" in the M3 headline and one
subject alternative is a rhetorical framing device ("skills that do not stop at one lesson"),
not an invented lesson count or lineup claim. No Skill Path title is named or implied. No
invented content specifics.

### 11. Guardrail: instructor name confirmed

Result: PASS.

Bassam Fattouh is named only in copy for this class. His naming is explicitly permitted by the
brief (section 4): confirmed via the published Maharat course page. No other instructor is
named or implied anywhere in the package.

### 12. Guardrail: no accreditation implication

Result: PASS.

No variant, subject line, or preheader contains any certificate, accreditation, recognized
qualification, or equivalent phrase implying external recognition. Copy refers to the
Masterclass as a class and to gaining a usable skill, not to earning a credential.

### 13. Guardrail: no fundraising, roadmap, or unannounced plans

Result: PASS.

No fundraising language, no roadmap disclosure, and no mention of unannounced features or
plans appears anywhere in the package.

### 14. Offer integrity: price

Result: PASS.

Price appears only as the marked placeholder "[PRICE / PLACEHOLDER from brief]" in M3 body.
No number is invented or assumed. Traces correctly to brief section 4 (ASSUMPTION, open item
1 in the copy-package envelope). The slot is to be filled from confirmed brief values before
any send.

### 15. Offer integrity: promotion

Result: PASS.

Promotion appears only as the marked placeholder "[PROMO if any from brief]" in M3 body, with
the explicit note that if absent at send the slot line is removed cleanly. No promotion is
invented. Traces correctly to brief section 4 (ASSUMPTION, open item 3 in the copy-package
envelope).

### 16. Offer integrity: plan

Result: PASS.

No plan name (1-month, 3-month, or otherwise) is named in any customer-facing span. Present
only as the marked placeholder "[PLAN if named from brief]" in M3 body. Traces correctly to
brief section 4 (ASSUMPTION, open item 2 in the copy-package envelope). No plan name invented.

### 17. Offer integrity: all other claims

Result: PASS.

All other claims are traceable to confirmed sources:

- The Masterclass is on Maharat: confirmed, brief section 4 and the published course page.
- Bassam Fattouh is the instructor: confirmed, brief section 4 and the published course page.
- The subscription provides access to continuous learning from regional experts ("تعلما
  متواصلا من خبراء المنطقة"): the platform offer described in context/brand-voice.md
  (Masterclasses: premium video from regional experts) and the brief. No number of experts,
  no expert names beyond Bassam Fattouh for this class, and no specific lineup is named.
  Claim is accurate and not overstated.

No claim in the package is untraced to the brief or confirmed context.

---

## compliance-privacy-reviewer

The compliance-privacy-reviewer verdict is on file (dated 2026-06-02, pass, design-only,
not-sendable). That verdict listed as blocking open item 2 that the copy-package compliance
and brand_qa gates were still pending. This brand-qa gate now resolves the brand_qa side of
that open item. The compliance side of the copy-package gate is owned by
compliance-privacy-reviewer and is separate from this gate.

This gate does not own privacy and consent checks. Both this gate and the
compliance-privacy-reviewer must return pass for the asset to advance to its next stage per
runtime/verification.md.

---

## Verdict

```
gate:     brand_qa
result:   pass
fix_list: []
```

No failures. No fix list. All 17 brand and guardrail checks pass against the v2 copy-package.

The copy-package may advance to its next stage once the compliance-privacy-reviewer also
confirms its pass on the copy-package itself. The compliance verdict on file covers the
lifecycle-package as design-only, not-sendable; the compliance reviewer should note the
copy-package as a remaining item on its side.

Advancing past QA is not approval to send. The human gate (Ahmed) is separate and must give
explicit per-send approval before anything goes out. All 8 open items in the copy-package
envelope remain open and must be resolved at the human gate before any send proceeds.
