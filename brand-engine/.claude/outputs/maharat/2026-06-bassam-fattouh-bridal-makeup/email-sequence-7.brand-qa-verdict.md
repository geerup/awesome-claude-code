# qa-verdict: brand-qa-reviewer

- gate: brand_qa
- campaign_id: 2026-06-bassam-fattouh-bridal-makeup
- asset: email-sequence-7.md (7-email bilingual non-payer lifecycle, AR and EN)
- reviewer: brand-qa-reviewer
- date: 2026-06-03
- run: resubmission (prior verdict: fail, 2 items)
- result: pass

---

## Prior gate confirmation

- skill_eval: pass (confirmed per asset status block)
- arabic_qa: pass (confirmed per asset status block)
- english_qa: pass (confirmed per asset status block)
- compliance-privacy-reviewer: verdict in flight alongside this gate per verification.md; both must pass to advance

Prior gate requirements satisfied. This gate runs.

---

## Prior failure resolution

### Fix item 1 (resolved)

Prior failure: Email 4, Arabic body, "كثيرات" asserted an unconfirmed community size.
Submitted change: replaced with "بمن".
Current asset line: "شغفك بالمكياج يجمعك بمن يتعلمن الفن نفسه على مهارات."
Verdict: the quantity word is gone. The line uses a neutral relative clause with no size claim. Fixed and confirmed.

### Fix item 2 (resolved)

Prior failure: Email 7, English subject alt 1, "Still thinking? We kept your spot." implied an invented reservation.
Submitted change: replaced with "Still thinking? Start whenever you like."
Current asset line: "Still thinking? Start whenever you like."
Verdict: no reservation, no scarcity, no capacity claim. Low-pressure re-engagement only. Fixed and confirmed.

---

## Full re-check across all 7 emails, both languages

### 1. Voice: plain, confident, empowering, never deficit-framed

All 7 emails in both languages checked.

- Email 1 AR/EN: imagination prompt, outcome-led. No deficit framing. Pass.
- Email 2 AR/EN: credibility frame, active constructions. No shame or gap language. Pass.
- Email 3 AR/EN: transformation framing, encouraging. No deficit framing. Pass.
- Email 4 AR/EN: belonging frame. EN "You are not figuring it out alone" and AR "لست وحدك في الطريق" are empowering, not deficit-framed. No quantity invented. Pass.
- Email 5 AR/EN: offer presentation, factual and action-focused. Pass.
- Email 6 AR/EN: barrier-removing reassurance. "No long blocks of time needed. No previous experience required." removes barriers without implying the reader is deficient. Pass.
- Email 7 AR/EN: gentle winback. "Maybe the timing was not right. That is completely fine." Low-pressure, no shame. Pass.

Result: pass

### 2. Mechanical: no [em dash], no tatweel/kashida, Western numerals only, RTL-safe

- [Em dash] glyph: not found in any subject, preheader, body, CTA, or note across all 7 emails in both languages. Pass.
- Tatweel/kashida (U+0640): not found anywhere in the Arabic copy. Pass.
- Eastern Arabic-Indic numerals (U+0660 to U+0669): not found. All numerals throughout the asset are Western (0 to 9). Pass.
- RTL: Arabic copy is standard right-to-left script. No mixed-direction anomalies detected. Pass.

Result: pass

### 3. Guardrails: no invented Skill Path titles or content lineup, instructor confirmed, no accreditation, no fundraising or roadmap

- Skill Path titles: none appear. "الماستر كلاس" / "Masterclass" is the confirmed product entity from the brief. No invented Path names. Pass.
- Content lineup: no lesson count, module name, or duration stated anywhere. Copy leads with artist and craft only, consistent with the open-items block in the asset. Pass.
- Instructor naming: Bassam Fattouh. Confirmed via published Maharat course page per brief. Naming is permitted. Pass.
- Accreditation: no "certificate", "accredited", "certified", "شهادة معتمدة", or equivalent language found anywhere in the customer-facing copy. Pass.
- Fundraising, roadmap, unannounced plans: none. Pass.
- Invented quantity: "كثيرات" removed (fix item 1). Email 4 Arabic body now uses "بمن يتعلمن", neutral, no size claim. Email 4 English uses "others" and "people who share your passion", no figure. Pass.

Result: pass

### 4. Offer integrity: price, plan, promotion, deadline remain bracketed; no invented reservation or scarcity; CTA mapping watch 1-4, subscribe 5-7

Bracketed slots:
- Price: "[PRICE from brief]" appears in Email 5 AR and EN only. No price figure appears elsewhere. Pass.
- Plan: "[PLAN from brief]" in Email 5 AR and EN only. Pass.
- Promotion: "[PROMO if any]" in Email 5 AR and EN only. None invented. Pass.
- Deadline: "[DEADLINE from brief]" in Email 7 AR and EN body only. No date invented. Pass.

Invented reservation or scarcity:
- Email 7 EN subject alt 1 now reads "Still thinking? Start whenever you like." No reservation, no capacity constraint, no scarcity claim (fix item 2 confirmed resolved).
- Email 7 EN preheader "The Masterclass and all of Maharat are still here, one step away." is a factual availability statement, not a reservation claim. Pass.
- Email 7 AR subjects: "إطلالتك ما زالت بانتظارك", "فرصتك لتبدئي ما زالت قائمة", "خطوة أخيرة نحو إطلالتك". Warm re-engagement, no invented scarcity. Pass.

CTA mapping:
- Email 1: "Watch the Masterclass" / "شاهدي الماستر كلاس". Watch-focused. Pass.
- Email 2: "Watch the Masterclass" / "شاهدي الماستر كلاس". Watch-focused. Pass.
- Email 3: "Watch a Lesson" / "شاهدي درسا من الماستر كلاس". Watch-focused. Pass.
- Email 4: "Watch Now" / "شاهدي الماستر كلاس الآن". Watch-focused. Pass.
- Email 5: "Subscribe Now" / "اشتركي الآن". Subscription-focused. Pass.
- Email 6: "Subscribe and Start Today" / "اشتركي وابدئي اليوم". Subscription-focused. Pass.
- Email 7: "Subscribe Today" / "اشتركي اليوم". Subscription-focused. Pass.

Result: pass

### 5. Visual constants

Text-only copy asset. No visual embedded. Visual constants (#141414, #1A1A1A, emerald #009975) apply at build time and are not checked against a copy file. Pass.

---

## Verdict summary

result: pass

fix_list: []

Both prior failures are resolved. No new failures detected. All checks pass across all 7 emails in both languages.

This gate passes. The asset advances to its next stage subject to compliance-privacy-reviewer also passing. Both gates must pass to advance per verification.md.

Approval to advance past QA is not approval to send. The human gate is separate and has not been reached. Nothing publishes, sends, or spends without explicit sign-off from Ahmed.
