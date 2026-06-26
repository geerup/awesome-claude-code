# Brand QA verdict: the Maharat instructor email set

Gate: brand-qa-reviewer (criteria: `agents/brand-qa-reviewer.md` + `skills/brand-voice-qa`,
anchored on `context/brand-voice.md` and `.claude/CLAUDE.md`).
Scope: the rendered email set, 134 emails. The 9 seven-step instructor builds (E1 to E7, AR and
EN, 14 each = 126) plus the Bassam Fattouh 4-email non-payer build (8). Verify only, nothing
edited as a result of this gate (the one agent-flagged item was reviewed and cleared, see below).
Date: 2026-06-18. Status: INTERNAL DRAFT, nothing sends.

Review method, per the run instruction: the shared template once, then the per-instructor
specifics (names, claims discipline, header, the 3 card picks), then the cross-cutting guardrails.

---

## VERDICT (headline)

PASS on every brand check EXCEPT one standing BLOCK, recorded below. The block is not a copy or
design defect, it is a roster-permission gate: the emails name instructors whose public status is
`unconfirmed`. Send is blocked until Ahmed confirms the roster's public status.

- Quality-to-advance: the copy and visuals meet the brand bar (see the pass list).
- Send-permission: BLOCKED by the unconfirmed public status of every named instructor.

---

## The one BLOCK (record, do not resolve)

Instructor naming guardrail vs catalog status.

- `context/brand-voice.md` and `.claude/CLAUDE.md`: "Do not name instructors publicly without
  confirmation."
- `context/instructors/_CATALOG.md`: every one of the 11 rows carries Public status `unconfirmed`.
  The catalog rule is explicit: "public status changes ONLY on explicit team confirmation; launch
  evidence records what this run found (it informs the human review, it does not flip the status)."
- The email set names instructors in customer-facing copy: each build names its own instructor,
  and every build's "our other classes" grid names three more. The distinct set of named
  instructors across all 10 builds is 8 people: Bassam Fattouh, Cedric Haddad, Elda Choucair,
  Kosai Khauli, Ragheb Alama, Rahma Riad, Salam Dakkak, Toufic Kredieh (Kreidieh). Each maps to an
  `unconfirmed` row in `_CATALOG.md` (the bridal build maps to the same `bassam-fattouh` row;
  rahma-riad is additionally `mined-thin`, class existence itself unconfirmed).

BLOCK: the emails name instructors whose public status is `unconfirmed`. Several rows carry strong
launch evidence (Elda strongest, internal launch plan executed Feb 2026; Ragheb, Salam, Kosai,
Bassam, Toufic, Cedric strong), but evidence does not flip the status. Send is blocked until Ahmed
confirms the roster's public status. This is the same standing status as the existing Bassam build.
Routing: stop and ask Ahmed, the human gate (decision 1). The gate does not approve around it.

---

## What PASSES (recorded exactly)

### A. Voice and tone (empowering, Thmanyah, Arabic-first): PASS, all 134

Copy is consistently empowering, never deficit-framed, and Arabic-first with Gulf-familiar MSA in
the Thmanyah register. The frame is what the reader can become ("خطوة بخطوة", "تطبخ بثقة",
"40 years of experience, in your hands"), never what they lack. No hype, no condescension, no
academic or corporate stiffness. The English follows the same plain, confident, empowering spirit.
No deficit-framed line ("you are behind", "stop wasting", "fix yourself") appears in any subject,
preheader, headline, body, list item, or CTA across the set.

### B. Visual constants (#141414 / #1A1A1A / #009975 only, no gold, no #1c1c1c): PASS, all 134

Swept every rendered file for the forbidden colors: zero hits for the pending gold `#C4963C` and
zero for the panel `#1c1c1c`. The only colors present are the brand set and the documented renderer
neutrals: `#141414` (paper), `#1A1A1A` (panel), `#009975` (emerald accent, one per email), plus the
hairline `#262626` and the grayscale ink/body/mute (`#FFFFFF`, `#E6E6E6`, `#9A9A9A`, `#8a8a8a`,
`#6F6F6F`). Premium and uncluttered, one emerald accent per email. The CTA is the near-black
`#141414` label on emerald `#009975` (about 5:1, clears WCAG AA), never white on emerald.

### C. Mechanical hard rules: PASS, all 134

No em dashes, no en dashes, no tatweel (U+0640), Western numerals only (no Eastern Arabic-Indic
U+0660 to U+0669) anywhere in the set. Enforced by the same code-point sweep the renderer and
`scripts/house_style_sweep.py` run; clean on every email plus every spec and index. RTL renders
correctly (`dir="rtl"` for AR, `dir="ltr"` for EN).

### D. No invented Skill Path titles or lesson lineup: PASS

No Skill Path title is named and no lesson, chapter, or module lineup is invented. The builds speak
in the cleared product taxonomy (the masterclass / the class, "the first lesson free", "subscribe
to unlock the full class") without inventing a curriculum.

### E. No accreditation implication: PASS, all 134

Zero hits for accredited / certified / certification (EN) and معتمد / اعتماد (AR) in any
customer-facing copy. No certificate claim of any kind appears in these nurture emails. (The word
"accreditation" appears only inside the specs' `held_back_claims` documentation, never in copy.)

### F. No fundraising, roadmap, or unannounced plans: PASS

No fundraising talk, no roadmap, no launch-date or unannounced-plan language. The Skill Paths
product (built, not yet launched) is not announced. Co-founder names, funding, and internal launch
plans (which exist in `_CATALOG.md`) stay out of the copy.

### G. Offer integrity and claims discipline (claims trace to the pack/page): PASS

No invented price, plan tier, monthly figure, subscription date, or duration in any build. Step 7
(subscribe) points to the cleared class page, not an invented plan-picker. The only numeric claims
in the entire set are two, both traceable:
- Ragheb "40 years of experience" / "أكثر من 40 سنة": verbatim from his cleared masterclass page
  tagline (`skills/instructor-marketing/ragheb-alama/masterclass-pages.md`).
- Salam "over 20 recipes" / "أكثر من 20 وصفة": pack-supported (see the reviewed item below).
Each build also carries an explicit `held_back_claims` list in its spec (6 to 10 items) documenting
the specifics deliberately withheld (exact dish lists, precise counts, award bodies, Michelin star,
income or career-outcome promises, testimonials, ratings, student counts). Spot checks confirm the
copy does not contain the withheld specifics. Elda's withheld credentials (CEO Omnicom, Forbes,
Cannes, 100 plus brands) correctly do not appear, replaced by the generic "one of the Arab world's
most respected marketing leaders".

---

## Reviewed and cleared (one agent-flagged item, not a defect)

A sub-reviewer flagged Salam's "over 20 recipes / أكثر من 20 وصفة" (E3 list and preheader, AR and
EN) as a possibly invented count. Reviewed against the full Salam pack, which is the cleared source
(the spec's `generated_from` names SKILL.md, voice.md, masterclass-pages.md):

- `skills/instructor-marketing/salam-dakkak/voice.md` line 11 lists the direct promise verbatim:
  "أكثر من 20 وصفة، خطوة بخطوة، من مطبخ سلام دكاك إلى مطبخك."
- `skills/instructor-marketing/salam-dakkak/SKILL.md` states the differentiator is "20 plus
  concrete recipes" and the home-cooks angle is "20 plus recipes".
- The spec's own `held_back_claims` keeps the framing loose ("the page-supported 20 plus recipes")
  and explicitly excludes any precise count beyond that.

Conclusion: "over 20" is the cleared, deliberately loose pack framing, not an invented precise
count. It traces to the pack. No concrete defect, so no copy was rewritten (per the run rule, copy
is rewritten only on a concrete defect). Recorded here for the audit trail.

---

## Per-build summary

| Build | Instructor (named) | A voice | B/C visual+mech | D paths | E accred | F leaks | G claims |
|---|---|---|---|---|---|---|---|
| bassam-fattouh (7-step) | Bassam Fattouh | pass | pass | pass | pass | pass | pass |
| bassam-fattouh-bridal (7-step) | Bassam Fattouh | pass | pass | pass | pass | pass | pass |
| cedric-haddad (7-step) | Cedric Haddad | pass | pass | pass | pass | pass | pass |
| elda-choucair (7-step) | Elda Choucair | pass | pass | pass | pass | pass | pass |
| kosai-khauli (7-step) | Kosai Khauli | pass | pass | pass | pass | pass | pass |
| ragheb-alama (7-step) | Ragheb Alama | pass | pass | pass | pass | pass | pass |
| rahma-riad (7-step) | Rahma Riad | pass | pass | pass | pass | pass | pass |
| salam-dakkak (7-step) | Salam Dakkak | pass | pass | pass | pass | pass | pass |
| toufic-kredieh (7-step) | Toufic Kreidieh | pass | pass | pass | pass | pass | pass |
| bassam-fattouh (4-email) | Bassam Fattouh | pass | pass | pass | pass | pass | pass |

Every build passes A through G on the merits. All 10 are send-blocked by the one standing block:
the named instructors are `unconfirmed` in `_CATALOG.md`.

---

## Disposition

`qa.brand_qa: pass-with-block`. The asset meets the brand bar and may advance to the human gate as
an approval-ready package, but it carries an unresolved send-blocking item (the unconfirmed roster
public status) that the human gate must see and that only Ahmed can clear. Brand-qa does not flip
an instructor's public status, it only flags it. Nothing sends.
