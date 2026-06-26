# Brand QA Verdict: Bassam Fattouh Teaches Makeup, full-stack campaign

- campaign_id: 2026-06-bassam-fattouh-makeup
- gate: brand-qa-reviewer
- date: 2026-06-05
- verdict: PASS
- compliance-privacy-reviewer: verdict required in parallel. Both must pass for the asset
  package to advance. This verdict does not substitute for compliance-privacy-reviewer.
- prior gates confirmed:
  - arabic-copy-qa: pass (referenced in qa-copy-verdicts.md and lifecycle-package.md)
  - english-copy-qa: pass (copy-package.en.md self-check and lifecycle-package.md)
  - design-qa: pass (design-specs.md, Overall design QA verdict section)
- artifacts reviewed:
  copy-package.ar.md, copy-package.en.md, creative-package.md, design-specs.md,
  organic-package.md, content-package.md, pr-package.md, aso-package.md, seo-package.md,
  media-plan-package.md, paid-launch-package.md, conversion-package.md, lifecycle-package.md

---

## Check results

### 1. Voice: Thmanyah register, plain and confident, empowering, never deficit-framed

Result: PASS

Every customer-facing copy variant across all 14 artifacts leads with what the reader can
create, become, or do. No variant frames the reader as behind, lacking, or in need of
correction.

Selected spot checks:
- copy-package.ar.md AD-PRIMARY-A2: "المكياج مهارة تُتعلّم، لا موهبة تنتظرها." Capability
  frame, not correction. Pass.
- copy-package.en.md EN-EMAIL-E2 subject: "A look you create, not one you wait for."
  Empowering. Pass.
- conversion-package.md Section D body (AR): "شاهده، وقرر بعدها." Invitational, no pressure.
  Pass.
- organic-package.md community guidance 5.1: short, warm, confident, empowering, never stiff
  or corporate. Thmanyah benchmark named. Pass.

No deficit-framed copy found in any artifact.

### 2. Arabic-first

Result: PASS

All copy artifacts declare Arabic as primary. copy-package.ar.md is the primary copy
artifact; copy-package.en.md explicitly states it is not a translation but carries the same
voice. All channel assets carry ar and en slot pairs with ar as the default render. The
conversion-package.md page spec states default render is Arabic (RTL). The seo-package.md
states Arabic is primary throughout. The pr-package.md states Arabic is the primary press
release language.

### 3. No em dashes (U+2014 and U+2013)

Result: PASS

A full-corpus grep across all 14 artifacts found zero em dash characters (U+2014) and zero
en dash characters (U+2013) in any customer-facing copy, spec text, or internal document.
All separations use commas, colons, or periods as required.

### 4. No tatweel or kashida (U+0640)

Result: PASS

A full-corpus grep found zero U+0640 characters anywhere in the artifact set. The
prohibition is correctly stated in every Arabic-production spec and brief.

### 5. Western numerals only

Result: PASS

A full-corpus grep found zero Eastern Arabic-Indic numerals (U+0660 to U+0669) anywhere.
All numerals used in customer-facing copy are Western: "7" (price reference), "20" (chapter
count), "1" (free intro chapter). The design-specs.md global token table explicitly mandates
Western numerals only and marks Eastern Arabic numerals as prohibited. The paid-launch-
package.md pre-launch checklist confirms Western numerals in all in-platform copy.

### 6. RTL renders correctly

Result: PASS (at spec level; live render audit is an open item for conversion-engineer
before go-live, as correctly flagged in conversion-package.md section 2.4 and seo-package.md
Finding 3)

All design specs carry explicit RTL text-anchor assignments. Arabic overlay slots are right-
anchored; English overlay slots are left-anchored. No Arabic text is baked into any generated
image layer. copy-package.ar.md pre-handoff checklist confirms RTL-safe. design-specs.md
Check 1 (RTL correct) passes. The live render audit dependency on conversion-engineer is
correctly flagged as a pre-publish requirement, not a QA failure.

### 7. Visual constants: #141414, #1A1A1A, #009975

Result: PASS

design-specs.md global token table specifies all three constants on every spec. The emerald
#009975 is used as an accent highlight only: accent bars, CTA chip fills, transition marks.
It does not flood any frame. design-specs.md Check 4 (visual constants applied) passes. The
creative-package.md concept framing note explicitly specifies all three constants on every
element. The conversion-package.md page spec section 2.2 applies all three constants. No
asset uses #009975 as a background or dominant color.

### 8. Premium and uncluttered

Result: PASS

design-specs.md Check 5 (premium and uncluttered) passes, with specific reasoning per spec:
DS1 (single focal point, generous field), DS2 (single brushstroke, clean dark field), DS3
(generous card padding, even breathing room), DS4 (deliberate segment structure), DS5 (slim
banner, minimal). All layouts specify generous safe areas and breathing room. No busy graphic
elements in any concept.

### 9. No Arabic text baked into generated image layers

Result: PASS

design-specs.md Check 6 (no Arabic text baked into any generated image) passes. All
generated prompts P2 through P6 specify text-free output. All copy is overlay, applied at
build time from QA-passed copywriter-ar and copywriter-en output. creative-package.md
explicitly states all image prompts output text-free. organic-package.md repurposing notes
confirm "No Arabic text baked into video."

### 10. No invented Skill Path titles or content lineup

Result: PASS

All lesson titles cited across every artifact trace to the confirmed 20-chapter lineup from
the live class page (instructor profile.md, cleared). No Skill Path title appears in any
customer-facing copy. The one Skill Path reference in the organic-package.md community
guidance ("Questions about upcoming classes, other instructors, or the product roadmap.
Reply: Stay tuned for more and nothing else. No roadmap, no unannounced plans.") is a
prohibition instruction, not a claim. All lesson names used in copy-package.ar.md,
copy-package.en.md, creative-package.md, design-specs.md, pr-package.md, aso-package.md,
seo-package.md, content-package.md, and conversion-package.md are confirmed from the cleared
profile.

### 11. Instructor named only on the cleared basis

Result: PASS

Bassam Fattouh (بسام فتوح) is named throughout. Public naming is cleared per
profile.md: live Maharat course page confirmed HTTP 200 on 2026-06-05, Ahmed sign-off on
file 2026-06-05. No awards, career figures, or credentials beyond "leading regional makeup
artist" (cleared as "leading regional makeup artist, teaches makeup on Maharat" per
profile.md confirmed public facts) are attributed to him in any customer-facing copy.
The creative-package.md C4 segment 2 authority card explicitly instructs: "Use only facts
marked cleared in the instructor profile. Do not invent an award, a figure, or an
accreditation." design-specs.md OI-5 repeats this constraint and the slot is labeled
accordingly.

### 12. No accreditation implication

Result: PASS

Zero accreditation claims found in any customer-facing copy across all 14 artifacts. Every
artifact with Arabic copy, English copy, SEO schema direction, or ASO description explicitly
prohibits accreditation language. The seo-package.md schema spec instructs that
educationalCredentialAwarded, if included, must read exactly "شهادة إتمام" and never
"accredited" or "certified by." The conversion-package.md Section G footer spec states
"No accreditation marks, no certification endorsement logos." The aso-package.md review
response policy states the completion certificate response must not imply external
accreditation.

### 13. No fundraising, roadmap, or unannounced plans

Result: PASS

Zero fundraising references, zero roadmap references, zero unannounced plan references found
in any customer-facing copy across all 14 artifacts. The pr-package.md guardrail check
explicitly verifies this and passes. All artifacts that discuss future decisions (platform
confirmation, asset confirmation, promotion confirmation) correctly mark those as open items
for Ahmed, not claims in copy.

### 14. Offer integrity: price, promotion, and claims trace to the brief

Result: PASS

The one price used is "under 7 dollars per month billed annually" / "أقل من 7 دولارات
شهرياً عند الاشتراك السنوي" (public reference only). It appears only in ad concept C
(AD-PRIMARY-A3, EN-AD-C), the landing page plans section, and the conversion-package.md
subscription section, each carrying a note confirming the public reference basis. No
promotional offer, discount, trial, or bundle is stated or implied in any artifact. Every
artifact carrying the price marks it as the public reference only and flags that any campaign-
specific promotion requires Ahmed's confirmation before any copy is updated.

### 15. No personal or sensitive data in URL parameters

Result: PASS (ownership note: this is a compliance-privacy-reviewer check, carried here for
confirmation only)

All CTAs and landing destinations across copy-package.ar.md, copy-package.en.md,
conversion-package.md, paid-launch-package.md, and organic-package.md explicitly state "No
personal or sensitive data in any URL." UTM parameters carry only campaign, source, medium,
and content identifiers. No user identifier, email, phone, or personal attribute appears in
any UTM field specification.

---

## Noted items (not failures, surfaced for the human gate)

The following items are open workflow or procedural matters correctly flagged within the
artifacts. They are not brand-qa failures. Each is carried to the human gate.

1. lifecycle-package.md open_item 2 and message table still describe E4 as "BLOCKED pending
   brand-qa E4 subject line fix." This references the previous brand-qa-verdict cycle. The
   current copy-package.ar.md EMAIL-E4 and copy-package.en.md EN-EMAIL-E4 carry the fixed
   subject lines. The lifecycle-package.md internal notation is stale and should be updated
   by lifecycle-architect to reflect that the fix is now in place. This is a housekeeping
   item, not a customer-facing failure.

2. Bassam Fattouh rights-cleared photography, class stills, and footage remain OPEN ITEMs
   across creative-package.md, design-specs.md, organic-package.md, aso-package.md, and
   conversion-package.md. AB1 (hero portrait) and AB4 (class trailer) are correctly build-
   blocked. No generated likeness is permitted and none is specified. This gate is correctly
   applied; the human gate must resolve it before those assets go live.

3. ORG-11 (quote inspiration carousel) in organic-package.md is correctly blocked pending
   confirmed verbatim Bassam Fattouh quotes. The open items table specifies the fallback.
   No invented quote is present.

4. Posts 9 to 13 in organic-package.md are new caption requests, not yet produced. They are
   correctly flagged as requiring arabic-copy-qa, english-copy-qa, and brand-qa before the
   calendar advances. Brand-qa has not reviewed those captions; they do not exist yet and
   will route through this gate when produced.

5. The gate platform (email or WhatsApp) is OPEN ITEM across multiple artifacts. All gate-
   landing CTAs are correctly flagged as blocked until the platform is confirmed. This is
   a human-gate decision.

6. compliance-privacy-reviewer runs alongside this gate and owns privacy and tracking-consent
   checks. Both gates must pass for the package to advance. This brand-qa verdict does not
   substitute for that gate.

---

## Verdict

qa.brand_qa: PASS

All brand and guardrail checks pass. The 14 artifacts reviewed carry:
- Consistent Thmanyah voice, empowering throughout, never deficit-framed.
- Zero em dashes, zero tatweel, zero Eastern Arabic numerals.
- Visual constants (#141414, #1A1A1A, #009975) applied correctly and consistently.
- No generated likeness, no Arabic text baked into image layers.
- No invented lesson titles, no Skill Path titles, no unconfirmed instructor claims.
- No accreditation implication anywhere.
- No fundraising, roadmap, or unannounced plans.
- Price stated only as the confirmed public reference, only where the asset calls for it.
- No invented promotion, discount, or trial.
- No personal or sensitive data in any URL parameter specification.

The noted items above are procedural open items correctly managed within the artifacts. None
constitutes a brand failure. They travel to the human gate.

This verdict is valid for the artifacts as reviewed on 2026-06-05. Any subsequent revision to
any customer-facing asset requires brand-qa re-review of the revised artifact before it
advances.

Approval to advance past this QA gate is not approval to send, publish, or spend. The human
gate is separate. Nothing activates without Ahmed's explicit per-action sign-off.
