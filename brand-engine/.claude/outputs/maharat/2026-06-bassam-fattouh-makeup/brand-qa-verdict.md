# Brand QA Verdict

- campaign_id: 2026-06-bassam-fattouh-makeup
- produced_by: brand-qa-reviewer
- verdict: FAIL
- brand_qa: fail
- review_date: 2026-06-05
- artifacts_reviewed:
  - 01-emails.ar-en.md
  - 02-social-posts.ar-en.md
  - 03-paid-ads.ar-en.md
  - 04-app-notifications.ar-en.md
  - 05-visual-briefs.md

---

## Prior gate confirmation

| Gate | Status |
|---|---|
| skill_eval | pass (confirmed by submitting agent) |
| arabic-copy-qa | pass (2 dialect fixes applied and confirmed) |
| english-copy-qa | pass |
| design-qa | pass (spec-level) |
| compliance-privacy-reviewer | pass (design-only, conditional, 7 open items surfaced for human gate) |

All prior gates confirmed. compliance-privacy-reviewer verdict is in flight and passes at the design level. Both gates are assessed together per runtime/verification.md.

---

## Check results

### 1. No em dashes

Scanned all 5 artifacts. No em dash or en dash glyph found.

Result: PASS.

---

### 2. No tatweel or kashida (U+0640)

Scanned all 5 artifacts. No tatweel or kashida found.

Result: PASS.

---

### 3. Western numerals only

Scanned all 5 artifacts. No Eastern Arabic-Indic digits (U+0660 to U+0669) found. All numerals present are Western (0-9).

Result: PASS.

---

### 4. Voice: plain, confident, empowering, never deficit-framed

The majority of the copy across all 5 artifacts is empowering and on tone. The following items were examined closely.

**FAIL: Hype-register subject line option in E4 (01-emails.ar-en.md)**

The E4 subject line set offers three options. One option is a hype phrase. Because subject line options are selectable choices, any option in the set must be clean.

Fix item 1 (see fix list below).

"لا نريدك أن تفوّت البداية" (E4 body AR) and "We do not want you to miss the start" (E4 body EN) are care-framing, not deficit-framing. They pass.

"مهارة المكياج تنتظرك، لا تؤجلها" and "خطوتك الأولى ما زالت بانتظارك" (E4 subject options AR), and "The makeup skill is waiting, do not put it off" and "Your first step is still here" (E4 subject options EN): these are urgency without hype and remain empowering. They pass.

"حين تتعلم من محترف، تختصر سنوات من التجربة" (Social Post 3 AR) and "When you learn from a professional, you skip years of trial and error" (EN): this frames the benefit of expert learning, not the reader's deficiency. It passes.

All push notification copy (P1 to P5) is empowering and on tone. PASS.
All paid ad copy (Concepts A to D) is empowering and on tone. PASS.

Result for this check overall: FAIL. One subject line option must be replaced (fix item 1 below).

---

### 5. Visual constants: #141414, #1A1A1A, emerald #009975; premium, uncluttered

05-visual-briefs.md explicitly calls all three color constants in every visual concept (V1 to V4) and in the binding rules at the top of the file. The direction "Premium, uncluttered, generous space, accent as a highlight not a flood" is present. No invented colors or off-brand palette instructions found.

The visual briefs are spec-level documents. No built assets are in scope for this review. The visual direction is brand-correct.

Result: PASS.

---

### 6. No Arabic text baked into generated images; overlays are build-time only

05-visual-briefs.md line 10: "No Arabic text baked into any generated image. All headlines are build-time overlay slots, added in Canva or Figma by the designer." This constraint is restated in 03-paid-ads.ar-en.md line 41.

Result: PASS.

---

### 7. No invented Skill Path titles or content lineup

No Skill Path title appears in any artifact. No lesson names, module names, lesson count, or duration are stated anywhere in customer-facing copy. All references to the content are generic ("مكتبة مهارات كاملة", "full Maharat library", "دروس وخبراء آخرين").

Result: PASS.

---

### 8. Instructor naming: confirmation basis

Bassam Fattouh is named in copy across all 5 artifacts. The brief (section 4) confirms the naming basis: "Publicly confirmed via the published Maharat course page (https://www.maharat.com/en/library/design-style/bassam-fattouh-teaches-makeup)." No other instructor is named. No generated likeness is used; the visual briefs require a real rights-cleared Maharat asset and explicitly prohibit generated likeness.

Result: PASS.

---

### 9. No accreditation implication

No accreditation claim, completion-certificate promotion, or implication that the Masterclass confers a recognized qualification appears in any artifact. 05-visual-briefs.md line 17 explicitly prohibits "accreditation marks or implied-accreditation visuals."

Result: PASS.

---

### 10. No fundraising, roadmap, or unannounced plans

No fundraising language, no roadmap, no launch date, no unannounced product found in any artifact.

Result: PASS.

---

### 11. Offer integrity: no price, no invented promotion, no invented plan specifics

No price or currency appears in customer-facing copy. All artifacts that reference plans do so generically ("اختر الخطة التي تناسبك", "Choose the plan that suits you") and note that the plan picker on the page carries confirmed numbers. No trial, discount, or promotion is invented. All open financial variables are explicitly surfaced as OPEN ITEM or ASSUMPTION in each artifact header, consistent with the brief.

Result: PASS.

---

### 12. No personal or sensitive data in URL parameters or tracking

This check is owned by compliance-privacy-reviewer, which has a passing verdict at the design level. For this gate's own scan: no URL with query parameters carrying personal data was found in any artifact. All CTA destinations reference the Masterclass page, signup gate, or app deep link, with explicit design constraints against personal data in URLs. The check is confirmed clean by this gate as well.

Result: PASS.

---

## Fix list

One item. Return to copywriter-ar and copywriter-en for the subject line replacement only.

---

### Fix item 1

- artifact: 01-emails.ar-en.md
- check: voice, no hype words (brand-voice.md: "Confident without shouting. No condescension, no over-explaining, no hype words.")
- offending span AR: "آخر فرصة لتبدأ مع بسام فتوح"
- offending span EN: "Last chance to start with Bassam Fattouh"
- location: E4 subject line options, first option in each language set
- required change: Replace both options with a subject line that carries last-call urgency in the empowering register already demonstrated by the other two options in the same set. The remaining two AR options ("مهارة المكياج تنتظرك، لا تؤجلها" and "خطوتك الأولى ما زالت بانتظارك") and the remaining two EN options ("The makeup skill is waiting, do not put it off" and "Your first step is still here") are already clean and acceptable. The replacement must match that register. Do not use "آخر فرصة", "last chance", or equivalent hype-urgency phrasing.

---

## Verdict summary

FAIL. One fix required before the package advances to the human gate.

The single failing item is confined to one subject line option (AR and EN pair) in E4 of 01-emails.ar-en.md. All other copy, visual direction, guardrails, mechanical rules, and offer claims across all 5 artifacts pass.

Once copywriter-ar and copywriter-en replace the flagged subject line option and resubmit 01-emails.ar-en.md to this gate, and this gate re-reviews and clears, the full package may advance to the human gate.

compliance-privacy-reviewer verdict: pass at design level (conditional, 7 open items for the human gate). That verdict stands independently and does not require regeneration.

Approval to advance past this gate is not approval to send or spend. The human gate and Ahmed's per-action sign-off are separate and required.
