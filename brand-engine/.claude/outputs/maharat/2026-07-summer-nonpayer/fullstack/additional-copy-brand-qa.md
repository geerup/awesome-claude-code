# Brand QA verdict: additional copy package (AR and EN)
# Four deferred deliverables: onboarding, organic gap captions, gate-consent, press release

## Envelope

- verdict_by: brand-qa-reviewer
- campaign_id: 2026-07-summer-nonpayer
- assets_reviewed:
  - outputs/2026-07-summer-nonpayer/fullstack/additional-copy.ar.md
  - outputs/2026-07-summer-nonpayer/fullstack/additional-copy.en.md
- review_date: 2026-06-12
- re_verification_date: 2026-06-12
- grounding_refs: CLAUDE.md; context/brand-voice.md;
  outputs/2026-07-summer-nonpayer/fullstack/strategy-artifact.md;
  skills/brand-voice-qa/SKILL.md; runtime/verification.md

## Prior gate state, confirmed before review

- skill_eval: self-run pass recorded on both files. Accepted for this gate.
- arabic_qa: self-run pass recorded on additional-copy.ar.md (2026-06-12, pre-gate).
  Accepted for this gate. Routes to arabic-copy-qa as gate of record after brand-qa.
- english_qa: pass (re-run post brand-qa fix, 2026-06-12). Fix applied: SOCIAL-S11
  Slide 2 on-screen text rewritten from deficit-framed to capability-led per brand-qa
  fix list. Organic gap caption ids reconciled to AR canonical: SOCIAL-S-ACT to
  SOCIAL-S9, SOCIAL-S-POLL to SOCIAL-S10, SOCIAL-S-FREE to SOCIAL-S11. Accepted for
  this gate.
- compliance-privacy-reviewer: verdict in flight. Required alongside this gate for
  gate-consent copy (GATE-CONSENT-EMAIL-AR, GATE-CONSENT-WHATSAPP-AR,
  GATE-CONSENT-EMAIL-EN, GATE-CONSENT-WHATSAPP-EN) and for press release distribution
  handling. Both this gate and compliance-privacy-reviewer must pass for those assets
  to advance. This gate does not own compliance-privacy checks.

---

## Checks run

The following checks were run against every section of both files:

1. Voice: plain, confident, empowering, never deficit-framed. Thmanyah tone. Arabic-first.
2. Mechanical: no em dash (U+2014), no tatweel or kashida (U+0640), Western numerals
   only (U+0030 to U+0039), RTL-safe construction.
3. Visual constants: not applicable (copy-only assets, no visual surfaces in scope).
4. Guardrails: no invented Skill Path titles or content lineup, no unconfirmed instructor
   names asserted (all seven flagged confirm-at-gate), no accreditation implication, no
   fundraising or roadmap or unannounced plans.
5. Offer integrity: no price, no promotion, no plan length anywhere. No invented claim.
   All instructor credentials are cleared, page-sourced lines only.
6. Excluded facts confirmed absent: Toufic Kreidieh's Brands For Less name and garage
   detail, Elda Choucair's Omnicom, Forbes, Cannes, and the 900-plus and 1000-plus
   figures. Absent from both files.
7. Non-nameable instructors (Rahma Riad, Sami Al Jaber, Mona Ataya, Mo Islam): not
   named anywhere in either file. Confirmed.
8. Press release specifics: quote confirmed as a clear placeholder, all names are
   flagged confirm-at-gate inline, media contacts are placeholders, boilerplate uses
   only public press facts, no funding or bootstrapped reference in any body paragraph.

---

## Section verdicts

### 1. Onboarding (ONBOARD-O1, O2, O3): AR

```
skill        brand-qa-reviewer
target       additional-copy.ar.md, section 1: ONBOARD-O1, ONBOARD-O2, ONBOARD-O3
result       pass
```

All checks pass. Empowering throughout: O1 leads with "you are in" and open access,
O2 is skills-momentum framing with no "you have not started" construction, O3 frames
habit and breadth without re-selling. No price, promo, or plan length. No instructor
names in the onboarding bodies (breadth by field only, no confirm-at-gate dependency).
No em dash, no tatweel, no Eastern numerals. Certificate not referenced in onboarding,
so no accreditation risk. No guardrail breach.

---

### 1. Onboarding (ONBOARD-O1, O2, O3): EN

```
skill        brand-qa-reviewer
target       additional-copy.en.md, section 1: ONBOARD-O1, ONBOARD-O2, ONBOARD-O3
result       pass
```

All checks pass. O1 "you are in" welcome, empowering register, no receipt framing.
O2 "That is the hardest step" acknowledges the subscriber's first action positively,
not their inaction. "If you have not yet begun, today is a good day for it" is
empowering, not shaming. O3 "Seven fields, seven experts, every lesson unlocked" uses
"experts" as a generic count descriptor with no instructor names, so confirm-at-gate
discipline is not triggered. No em dash. No price, promo, plan length, accreditation.

---

### 2. Organic gap captions (SOCIAL-S9, SOCIAL-S10, SOCIAL-S11): AR

```
skill        brand-qa-reviewer
target       additional-copy.ar.md, section 2: SOCIAL-S9, SOCIAL-S10, SOCIAL-S11
result       pass
```

All checks pass.

S9 (acting, Kosai Khauli): cleared, page-sourced credentials only, "confirm-at-gate"
discipline held, instructor line uses the correct pattern ("يعلّم التمثيل"). No chapter
count or lesson title. Empowering, field-led framing.

S10 (poll): participation framing, no instructor named, fields only, soft CTA as
required for the T7 brief. No deficit framing. Four non-nameables absent.

S11 (free-chapter story): "لا حاجة لخبرة سابقة، ولا للبحث في مصادر متفرقة" echoes
the confirmed live-site accessibility line ("ليس هناك أي خبرة سابقة مطلوبة") framing.
This is an access-barrier removal ("you do not need X"), not a personal deficit frame
("you lack X"). Consistent with brand-voice.md empowering/deficit worked examples and
the live corpus. Pass.

No em dash, no tatweel, no Eastern numerals across all 3 captions.

---

### 2. Organic gap captions (SOCIAL-S9, SOCIAL-S10, SOCIAL-S11): EN

```
skill        brand-qa-reviewer
target       additional-copy.en.md, section 2: SOCIAL-S9, SOCIAL-S10, SOCIAL-S11
result       pass
```

Re-verification run 2026-06-12. Prior verdict failed 1 item (SOCIAL-S-FREE Slide 2,
deficit framing). Fix confirmed applied. Id reconciliation confirmed.

Fix verification:
- Prior failing span "The problem is never motivation. It is not knowing where to begin."
  is absent from the file. Confirmed by full read of SOCIAL-S11.
- Replacement Slide 2 on-screen text: "You already know what you want to build. One
  free lesson from someone who set the standard in your field is where to start."
  Capability-led. No problem or deficit attribution. Speaks to what the reader can do.
  Consistent with the fix direction and with brand-voice.md worked examples. Pass.

Id reconciliation confirmed:
- SOCIAL-S9 (acting): present, id correct, fills map updated. Matches AR canonical.
- SOCIAL-S10 (poll): present, id correct, fills map updated. Matches AR canonical.
- SOCIAL-S11 (free-chapter): present, id correct, fills map updated. Matches AR
  canonical. Envelope QA note records the reconciliation explicitly.

Regression scan, Section 2 EN:
- SOCIAL-S9: "Acting is a craft. It can be taught." and "The real work behind the
  performance, shared clearly, step by step." Capability-led throughout. No deficit.
- SOCIAL-S10: "Which skill do you want to build this summer?" and "Maharat has a
  masterclass for each one, taught by an expert who set the standard in it."
  Participatory and empowering. No deficit.
- SOCIAL-S11 Slide 1: "There is a field you have always wanted to go deeper in."
  Aspiration framing. No deficit.
- SOCIAL-S11 full caption: "This summer, the path is one free lesson away."
  Empowering. No deficit.
- No em dashes in any of the 3 captions. No Eastern numerals. No invented credentials.
  No accreditation. No guardrail breach.

No regression found.

---

### 3. Gate-consent copy (GATE-CONSENT-EMAIL-AR, GATE-CONSENT-WHATSAPP-AR): AR

```
skill        brand-qa-reviewer
target       additional-copy.ar.md, section 3: GATE-CONSENT-EMAIL-AR,
             GATE-CONSENT-WHATSAPP-AR
result       pass (brand checks only; compliance-privacy-reviewer verdict required
             separately before live gate use)
```

Brand checks pass. Plain, non-promotional, one action per line. No price, no promo,
no accreditation, no fundraising, no Skill Paths. No em dash, no tatweel, no Eastern
numerals. Consent copy is honest and concise in the required Thmanyah register: plain
information, not a sales surface. Both policy links are placeholders, correctly marked.

Note: Compliance-privacy-reviewer owns the privacy, consent disclosure completeness,
PDPL lawful basis, and data-handling checks on these lines. This gate does not and
cannot pass those assets for live gate use on its own. Both gates must pass.

---

### 3. Gate-consent copy (GATE-CONSENT-EMAIL-EN, GATE-CONSENT-WHATSAPP-EN): EN

```
skill        brand-qa-reviewer
target       additional-copy.en.md, section 3: GATE-CONSENT-EMAIL-EN,
             GATE-CONSENT-WHATSAPP-EN
result       pass (brand checks only; compliance-privacy-reviewer verdict required
             separately before live gate use)
```

Brand checks pass. Plain, one action per line, no price, no promo, no accreditation,
no fundraising. No em dashes. "Maharat is the data controller" and the opt-out lines
are plain, direct, and non-promotional. Policy link placeholder correctly marked.

Same note as AR: compliance-privacy-reviewer must also pass these before any live use.

---

### 4. Press release (PR-RELEASE-AR): AR

```
skill        brand-qa-reviewer
target       additional-copy.ar.md, section 4: PR-RELEASE-AR
result       pass
```

All checks pass.

Voice: press register, not hype, empowering and capability-led throughout. "بنى عملاً
بمليارات الدولارات من الصفر" and "أربعون عاماً في عالم الموسيقى" are concrete
credential anchors, not vague claims.

Mechanical: no em dash, no tatweel, no Eastern numerals. The figures 2023, 200000,
1.5, 100 are all Western. Confirmed by Grep.

Guardrails:
- No bootstrapped or funding reference in any body paragraph. Confirmed.
- No Skill Paths, roadmap, or unannounced plans. Confirmed.
- Certificate: "شهادة إتمام مخصصة باسم المتعلم ... غير معتمدة" in the boilerplate.
  Non-accreditation stated explicitly. Pass.
- All 7 names carry [confirm-at-gate] inline. Non-nameables absent. Verified.
- Verify-before-use facts (Brands For Less, garage detail, Omnicom, Forbes, Cannes,
  figures) absent from all body paragraphs. Confirmed.

Press release specifics:
- Quote is a clear placeholder: "[QUOTE: SPOKESPERSON NAME, approval required before
  distribution]". Pass.
- Dateline is a placeholder: "[المدينة]، [التاريخ]:". Pass.
- Media contact line is a placeholder: "[MEDIA CONTACT NAME], [MEDIA CONTACT EMAIL]".
  Pass.
- Boilerplate uses only public press facts (platform launch year, social followers,
  unique visitors, country count), all sourced from the catalog (Entrepreneur, Aug 2025)
  and marked confirm-at-gate. No invented or unverified fact asserted.

---

### 4. Press release (PR-RELEASE-EN): EN

```
skill        brand-qa-reviewer
target       additional-copy.en.md, section 4: PR-RELEASE-EN
result       pass
```

All checks pass.

Voice: press register, concise, empowering, no hype. Credential anchors are
concrete and page-sourced.

Mechanical: no em dash. "CITY, DATE, 2026 --" uses a double-hyphen press wire
dateline convention, not the banned U+2014 em dash character. Western numerals
throughout (200,000-plus, 1.5 million-plus, 100-plus, 40 years). Confirmed by Grep.

Guardrails:
- No bootstrapped, funding, or investor reference in any body paragraph. The exclusion
  note appears only in the internal metadata; the body is clean. Confirmed.
- No Skill Paths, roadmap, or unannounced plans. Confirmed.
- Certificates: "Certificates are not accredited." stated twice, once in the body and
  once in the boilerplate. Non-accreditation explicit. Pass.
- All 7 names carry [confirm-at-gate] inline. Non-nameables absent. Verified.
- Verify-before-use facts absent from all body paragraphs. Confirmed.

Press release specifics:
- Quote is a clear placeholder: "[QUOTE: SPOKESPERSON NAME, approval required before
  distribution]". Pass.
- Dateline is a placeholder: "[DATELINE: City, Country, Date placeholder, to be
  confirmed by Ahmed before distribution]". Pass.
- Media contact lines are placeholders: "[MEDIA CONTACT NAME]" and
  "[MEDIA CONTACT EMAIL]". Pass.
- Co-founder names are flagged confirm-at-gate: "2023 [confirm-at-gate: by Arman
  Khederlarian and Bassem Jamaleddine]". Pass.
- Boilerplate platform figures are flagged confirm-at-gate. No invented or unverified
  figures asserted. Pass.

---

## Overall verdict

```
skill        brand-qa-reviewer
campaign     2026-07-summer-nonpayer
assets       additional-copy.ar.md (all 4 sections)
             additional-copy.en.md (all 4 sections)
overall      PASS
```

Re-verification 2026-06-12. The 1 prior failing item (SOCIAL-S11 Slide 2 deficit
framing) is resolved. Id reconciliation (SOCIAL-S9, S10, S11) confirmed against AR
canonical. Full regression scan of Section 2 EN finds no new failures. All sections
in both languages pass. No open brand-qa items.

## Routing

- additional-copy.ar.md: all 4 sections pass brand-qa. The file advances per routing
  note in the asset. Gate-consent AR sections additionally require compliance-privacy-
  reviewer pass before live gate use (handled separately, not by this gate).

- additional-copy.en.md: all 4 sections pass brand-qa. The file advances per routing
  note in the asset. Gate-consent EN sections additionally require compliance-privacy-
  reviewer pass before live gate use (handled separately, not by this gate).

- Gate-consent (both AR and EN): compliance-privacy-reviewer verdict is required
  alongside this gate. Both gates must pass before any live gate deployment.

- Press releases (AR and EN): human gate required before any distribution. No quote,
  dateline, or media contact is in place; none of these assets distribute until Ahmed's
  per-action approval per the human gate.

Nothing in either file sends, publishes, distributes, or goes live. The human gate
is separate and is required before any action.
