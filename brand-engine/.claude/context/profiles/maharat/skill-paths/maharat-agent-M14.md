# MAHARAT SKILL PATHS — AGENT EXECUTIVE SUMMARY · AGENT M14

**Version:** vG.6.1 · Schema v3.5 · 2026-05-15 (HR-10 scope clarification dot-release from Negotiation Beginner rebuild)
**Status:** LOCKED for execution. Approved May 15, 2026 (during Negotiation Beginner vG.6 rebuild). Supersedes vG.6 (M14 third pass, 2026-05-12 evening, L1-mirror architecture lock).

**What changed in vG.6.1 from vG.6 (the 2026-05-15 Negotiation Beginner rebuild dot-release).** One clarification, no rule changes. **HR-10 scope clarification: "every text field" is reaffirmed and the LXD §4.13 audit chain is brought into alignment.** During the 2026-05-15 Negotiation Beginner vG.6 rebuild, em-dashes were observed in graded option text ("Path A — strongest pitch first"), scenario openers, and after-wrong explanation paragraphs across multiple levels. The LXD-side §4.13 audit chain through vL.5 implicitly scoped its em-dash detection to concept-body blockquote prose, leaving these fields un-swept. HR-10 itself was always broader — "schema-enforced via regex on every text field" — so this is a tooling alignment, not a rule change. The subordinate contracts have been updated to reflect: (a) `maharat-agent-lxd-M14.md` vL.6 adds §4.13 audit item 8 (HR-10 every-field sweep) covering concept body, graded question, scenario, statement, every option string, wrong-answer title, wrong-answer body, chapter label, title, and image brief; (b) `maharat-agent-mockup-M14.md` vM.6 confirms its §7.1 halting check covers any text field, not just body. The HR-10 text in §2 below is unchanged; the implementation gap is closed downstream. Hard rules HR-1 through HR-39 are otherwise preserved unchanged. Architecture, schema, validators, and worked examples all carry through from vG.6 without modification.

**What changed in vG.6 from vG.5 (M14 follow-up, May 12 evening third pass).** One substantive amendment per Arman directive issued during L2 cascade review: **L2-L10 architecture revised to mirror L1's 12-screen / 7-concept / 5-graded distribution exactly.** Prior vG.5 architecture (3 explicit concepts × 1 graded each = 9 concept + 3 graded) was concept-heavy and missed narrative structure compared to L1. New vG.6 architecture matches L1 screen-by-screen: 3 hook concepts (L01-L03) + 1 c1 opener (L04) + 3 c1 graded (L05-L07) + 1 c2 opener with flashback (L08) + 2 c2 graded (L09-L10) + principle (L11) + open loop (L12). Two explicit canonical concepts (c1, c2); third concept's substance absorbed into the principle card at L11. **Concept word caps reduced ~50%** to match L1's actual prose density: concept body 25-50 target / 60 hard cap (was 50-90 / 110); principle 20-40 / 50 (was 30-60 / 80); open loop 40-70 / 90 (was 50-80 / 100). L02 protagonist intro and L08 c2 flashback retain a wider 50-80 / 90-word allowance per §6.10 + §11.7 (load-bearing scene-setters). **New rule: max 4 concept screens back-to-back** (HR-5 cap), enforced by new Validator V35. HR-13c reaffirmed: first graded of level (L05) is Op 1 or Op 4. Validators V14, V17, V20 revised for the new 7+5 distribution. Hard rules HR-1 through HR-39 from prior vG.5 are otherwise preserved unchanged. L1 abbreviated 12-screen architecture (HR-5, §5.5) is unchanged in vG.6 — L2-L10 now matches L1 by adopting L1's pacing rather than the reverse.

**What changed in M14 from M13 (the M13 → M14 update, May 12 evening, second pass — preserved for lineage; superseded by vG.6 above, see vG.5 text below for historical context).**

**Supersedes:** Agent M11 (May 11, 2026), May 8 consolidation, vG.3 (May 8), vG.2, vG.1, vG, `Maharat_Agent_Executive_Summary.docx` (vF20), `quantic-v2-agent-addendum.md` (Addendum #1), `quantic-v2-agent-addendum-2.md` (Addendum #2), `quantic-principles-for-agent.md` (four principles), `maharat-agent-exec-summary-vG.3-deltas.md`, `negotiation-hr19-exceptions.md`, `maharat-vG_4-production-updates.md`, `maharat-vG4-migration-plan.md`, `maharat-vG4-v35-agent-contracts-diff.md` (folded in here).
**Companion file:** `maharat-level-schema-v3.5.json` (machine-readable form of this contract; v3.4 retired).
**Audience:** The Path Skills Builder Agent (primary). Human authors and reviewers (secondary).
**Source decisions:** May 12 Arman lock (six decisions recorded in `maharat-vG4-v35-agent-contracts-diff.md`).

**What changed in M14 from M13 (the M13 → M14 update, May 12 evening, second pass).** One substantive amendment per Arman directive issued during the L2-L10 cascade review: **L2-L10 lesson count revised to 12 target / 15 maximum**, down from M13's 18-screen lock. M13's 18-screen architecture still ran long against the §6.10 3:30-4:30 reading-time target once concept bodies hit the word caps. New architecture is **3 + (6-9) + 3 = 12-15 lessons**:

- **Target 12 lessons:** 3 Phase 1 hook + 6 Phase 2 acts + 3 Phase 3 wrap. Phase 2 = **3 concepts × 2 screens** (1 opener + 1 graded retrieval per concept). 3 graded total.
- **Maximum 15 lessons:** 3 hook + 9 acts + 3 wrap. Phase 2 = **4 concepts × ~2.25 screens** (4 openers + 5 graded). 5 graded total. Permitted only when content density genuinely requires the fourth concept.

**Three concepts is the new default** for L2-L10 (was 4). HR-23 revised. Validators V9 (op diversity), V14 (retrieval per concept), V17 (lesson count), V20 (final lesson position) all revised. Hard rules HR-1 through HR-39 from M13 are otherwise preserved unchanged. M13's hook_line decommission (HR-35), plain-language rule (HR-38), rich-text markup rule (HR-39), and all six-persona review machinery survive intact. L1 abbreviated 12-screen architecture (HR-5, §5.5) is unchanged.

**M13 internal staleness fixed in M14.** When M13 changed HR-5 (22 → 18) and HR-35 (hook_line decommissioned), several downstream sections were not propagated. M14 fixes them: §1.1, §3.5.2 (deprecated for L2-L10), §4.6, §5.3, §5.4, §6.9 distribution rule, §7 workflow checklist item #6, §8.3 Conversion simulation phase-boundary list (drops "After Bridge:" since Bridge is deprecated per §5.2), §10 V9/V14/V17/V20 — all updated to the new 12-15 lesson architecture. The M13 documentation said these revisions had happened; the M14 pass makes them actually happen across the document body.

**What changed in vG.4-May-12 from vG.4-May-11 (the M11 → M12 update).** Six locked decisions from Arman: (1) contract bumps to vG.4 [already in place], (2) schema bumps to v3.5, (3) new images shift to AI-generated (Midjourney / DALL-E / Imagen) — Bana's role pivots to cultural-fit + visual-coherence review, (4) per-level reading time target tightens to 3:30-4:30 min (was implicitly 4-5 min), (5) principle cards now carry full illustrations rather than icon-only or color-block treatments, (6) the merged-headline rendering on L05 graded screens (visible in current mockups post-vG.7.3) is the current behaviour and §6.12 below codifies the schema fix. Four substantive shifts the path needed are codified: **length discipline** (§6.10 — concept body cap 110 words, principle 80, open loop 100), **visual rhythm** (§6.11 — consecutive concept cards each require an `image_brief`), **one headline per screen** (§6.12 — graded `hook_line` field decommissioned; question/scenario/statement IS the headline), and **filler intolerance** (§7.5 — sentence-by-sentence audit at draft time, not just review). Three new hard rules added from the diff doc: HR-33 (word counts), HR-34 (consecutive concept images), HR-35 (one headline per screen). Two additional hard rules added per operator directive on May 12 (after the diff doc shipped): HR-36 (no filler — promotes §7.5 from workflow to hard rule), HR-37 (mandatory self-review gate before handoff — promotes §8 + §4.13 from procedure to hard rule). New §6.13 documents the AI image brief format (style anchor + subject + lighting + mood). Schema fragment for graded lessons rewritten — `hook_line` removed from MCQ, Myth Buster, Scenario; Myth Buster `body` renamed to `statement` for semantic clarity. Three new validators (V30, V31, V32) queued for Georgy. M11 architecture (12-screen L1, 22-screen L2-L10, HR-19 documented exception policy, six-persona review pipeline) is preserved unchanged.

**Hard-rule numbering note (provenance discipline).** The May 12 diff document (`maharat-vG4-v35-agent-contracts-diff.md`) proposed three new hard rules numbered HR-32, HR-33, HR-34. **HR-32 was already taken** in M11 (May 11) by the "no overstatement or absolutism" rule introduced from the Lena cluster iteration. To avoid collision, the three new May-12 hard rules are renumbered **HR-33, HR-34, HR-35** in this M12 document. References in the diff to "HR-32 / §6.10," "HR-33 / §6.11," "HR-34 / §6.12" become HR-33 / HR-34 / HR-35 respectively here. Validator names (V30, V31, V32) are preserved from the diff and map to the renumbered hard rules.

**What changed in M13 from M12_1_ (the M12_1_ → M13 update, May 12 evening lock).** Four substantive amendments per Arman directive surfaced during the Entrepreneurship L2 production pass: (1) **L2-L10 architecture compressed from 22 screens to 18 screens** to resolve the §1.1 (22-screen lock) vs §6.10 (3:30-4:30 reading time target) internal tension in M12_1_; new architecture is 3 + 12 + 3 with 4 concepts × 3 lessons each (1 concept opener + 2 graded retrieval points). Drops 1 graded per concept relative to the old 22-screen lock. (2) **HR-38 — plain-language constraint with explainer-on-jargon rule** (NEW), promoting the §3.8 plain-language reference from craft guidance to hard rule and adding mandatory inline explainers for any term a layperson would not immediately understand (financial terms in particular: gross margin, P&L, cost of goods, overhead, surplus, payback, all defined inline on first use). Industry-specific jargon ("capsule," "trunk show") replaced with plain-language equivalents ("first batch," "styling event"). (3) **HR-39 — inline rich-text markup on body copy** (NEW): concept card and after-wrong bodies now carry CKEditor-compatible inline formatting (bold on highlight phrases, italic for contrast emphasis, underscored italic for abstract concept terms standing alone); the bottom `highlight_phrases` list is preserved as a reference but is no longer the only source of emphasis. (4) **New §6.14 (CKEditor formatting standard) and §6.15 (plain-language + explainer pattern)** documented. Validator updates: V14 (retrieval map count) revised to "L2-L10: 8 graded across 4 concepts (2 per concept)"; V17 (lesson count) revised to "L2-L10: 18 lessons (8 graded + 10 concept)." New V33 (markup-presence audit) and V34 (jargon-without-explainer audit) queued for Georgy. Two new LXD §4.13 audits added (markup-presence audit; jargon audit). M12_1_ rules HR-1 through HR-37 are preserved unchanged.

**What changed in vG.4-May-11 from vG.3 (the M11 update — preserved for lineage).** The Lena cluster L1 iteration surfaced that the 22-screen architecture is wrong for L1 — too long for conversion, four concepts spread too thin, and the protagonist persona (established bakery operator) misses the empathy target. L1 across every path now uses an abbreviated 12-screen architecture (7 concept + 5 graded) carrying one concept taught from five angles, ending on a transformation-promise open-loop rather than an assignment. L2-L10 keep the 22-screen architecture. L1 protagonists are aspiring entrepreneurs (corporate job + side hustle + zero buyers), not established operators. New §4.8 governs industry and setting selection (no category-level demand baseline, Gulf-centric setting, real pricing and cadences). New §4.9 governs cluster continuity (cascading changes, baseline time-stamps, venue palette, visual identity threads). New §3.5.8-§3.5.11 codify copy craft rules learned this iteration: concrete titles, no overstatement, lean body, calibrated number specificity, accurate myth-buster framing. Three hard rules added in M11: HR-13c (first graded slot is Op 1 or Op 4 — confidence-builder, not stumper), HR-31c (principle card uses non-contracted phrasing), HR-32 (no overstatement or absolutism). §11 worked example fully rewritten — Lena moves from Beirut/bakery to Dubai/kaftans, sample copy replaced with the May 11 lock. Locked Lena cluster canonical state in new §11.7. Reference renderer needs threshold tuning for the new L1 architecture but constants are unchanged; flagged for Hassan.

**Provenance flags (added 2026-05-11 after factual audit).** The following items in the body of this document are *inferred* from team-role definitions and session patterns rather than *explicitly sourced* from a primary decision document. Treat each as a proposal pending explicit confirmation from the named owner before locking. Body text was not edited because these are framings worth preserving as drafts; they should be confirmed or revised, not silently deleted.

1. **Validators V18, V19, V20 (Appendix D.3).** Fabricated IDs. The validator inventory available to this document's author confirms only V14 (retrieval count, named in `maharat-vG4-migration-plan.md` §1), V17 (lesson count, same source), and V25 (named in team memory as a pending Tier 4 validator). V18, V19, V20 were assigned to "concept count," "Phase 3 structure," and "open-loop content" by logical extension, not by inventory check. **Action:** Georgy + Hassan to confirm actual validator IDs before any work is scheduled against them.
2. **V25 as the math-check validator (Appendix D.3).** Team memory names V25 as a pending validator but does NOT specify its scope. The math-check assignment is a proposal by this document's author, not a confirmed scope. **Action:** Georgy to confirm whether V25's actual pending scope matches the math-check assignment or whether the math check needs a new validator slot.
3. **Gaia as "documentation completeness" approver (Appendix C).** Gaia's Program Director role is sourced. The specific approval action — sign-off on documentation completeness — is this document's framing. No source document gives Gaia an explicit approval gate on the HR-19 exception policy. **Action:** Confirm with Gaia whether this is the correct sign-off action for her role, or adjust.
4. **Bana's approval action on named-counterparty voice review (Appendix C).** Bana's Stage 2 Arabic voice-review role is sourced (queue for Negotiation L6, L8). The specific characterization of her review as an approval gate confirming "named counterparties read naturally in Arabic" is this document's framing. **Action:** Confirm with Bana that the named-counterparty linguistic check is in her review scope, or fold the check into a separate audit.
5. **Arman alignment on §4.9 cluster continuity rules (Appendix F).** The migration plan describes the continuity rules as emerging from the Lena cascade; it does not explicitly mark them as Arman-aligned (vs. San-authored). Arman alignment is inferred from his alignment pattern on adjacent items. **Action:** Confirm with Arman whether §4.9 is approved or whether it sits in San's authorship pending Arman review.
6. **Arman alignment on §11.7 Lena cluster canonical state (Appendix F).** The migration plan §3 lists the cluster details as "locked" but does not name who locked them. Arman is the most likely locker, but not explicit. **Action:** Confirm with Arman.

Sourced and verified (no flag): Arman as decision owner, Hassan as co-approver (per `maharat-vG_4-production-updates.md` closing line), San / Ahmed ElSanhoury as alignment partner (per migration plan front matter), Georgy as validator owner for V14/V17 (per migration plan + team memory), Lama as QA (per §1.3 preserved from vG.2), Gab as product owner for back-nav and phased card delivery (per migration plan §6, §7).

**What changed in vG.3 from vG.2.** Three rendering rules were added to handle the 2-card split that surfaced when high-density tactical content (the Voss-flavored Negotiation rebuild) exceeded single-card capacity: hook section caps at 4 cards (§5.1), no "continued" indicator on Card 2 (§6.8.6), no card with only one paragraph below 100 chars (§6.8.6). Three threshold values now drive split behaviour: 600 chars for L01/L03, 400 chars for L02, 340 chars for non-hook concept screens. HR-19 documented-exception policy now formalized for named counterparties (Mr. Khalid, Ms. Hala, Mr. Faisal) — see §2.4 and Appendix C. Section 11 adds a second worked example (Negotiation Beginner Level 1) demonstrating Voss-tactical voice and the 2-card split in production. No HR rules changed; all field schemas unchanged; length sweet spots in §6.2 unchanged.

**What changed in vG.2 from vG.1.** Phase 1 restructured to 3 screens: L01 universal concept hook (plants the master claim), L02 protagonist intro (full baseline texture), L03 her problem and reader invitation. HR-20 revised again — vG.1's pure cold-open with character on screen one is reversed; the master claim now lands universally before the case study walks on stage. New required protagonist field `current_baseline` (60-200 chars) captures the existing-success / standing texture that makes the protagonist feel real before the tension arrives. New voice rules: contractions are the default (HR-31), and verbatim customer quotes use single quotation marks (HR-30). Act-opener concept-screen sweet spot widened to 200-340 chars (was 180-280). Lead-phrase variation rule added — no move in the catalog appears more than twice in a single level. Total lesson count rises from 21 to 22 (3 + 16 + 3). HR-19 single-protagonist discipline reaffirmed strict.

---

## Preamble — How to read this document

This document is the agent's contract. If a level being produced does not match this document, the level is wrong, regardless of how good it sounds. Every section is binding.

Hard rules are numbered. They are cited elsewhere by their number (e.g., "Hard Rule 7"). When two rules collide, the lower-numbered rule wins.

The schema (`maharat-level-schema-v3.4.json`) is the machine-readable form of this contract. The spec and the schema are kept 1:1 — if one changes, the other changes. If they appear to disagree, the spec is canonical and the schema needs to be patched.

Section 11 contains a full worked example (Entrepreneurship · Beginner · Level 1) showing what a compliant level looks like end to end. The agent uses Section 11 as a pattern-match target whenever the rules in Sections 1-10 leave room for interpretation.

---

## Section 1 — Mission and core loop

### 1.1 What the agent does

The agent produces one Maharat Skill Paths level per run. The level's architecture depends on its position in the path:

- **L1 of every path** uses the abbreviated **12-screen architecture** (7 concept + 5 graded), carrying **one concept taught from five angles**. L1's job is conversion — install one foundational mental model, demonstrate the platform, and land the reader at the paywall with a transformation-promise open loop. See §5.5.
- **L2 through L10** use the **L1-mirror architecture** (12 lessons total, 7 concept + 5 graded, structure 3 + 7 + 2, revised in vG.6 / M14 follow-up from M14's original 3-concept × 1-graded structure that produced concept-heavy lesson plans). **Two explicit canonical concepts (c1, c2)** plus **one implicit concept absorbed into the principle card at L11**. Phase 1 hook trio (L01-L03) → c1 opener (L04) + 3 c1 graded (L05-L07) → c2 opener with flashback (L08) + 2 c2 graded (L09-L10) → principle (L11) + open loop (L12). Same screen-by-screen pacing as L1. See §5.1-§5.4.

Both architectures share the same protagonist cluster (HR-19), the same voice and narrative principles (§3), the same lesson type catalogue (§6), and the same validation suite (§10). The differences are localized to lesson count, concept count, and Phase 3 structure.

### 1.2 What the agent produces

Every run produces five artifacts:

1. **Level JSON** — conforming exactly to schema v3.4. The primary deliverable.
2. **Validator output table** — field, length, band, status. One row per text field. All 22 validators run with pass/fail status.
3. **Concept progression rationale** — the story-beat logic showing how each canonical concept emerges from the previous one through the protagonist's situation. Markdown.
4. **Decision log** — every choice the agent made (protagonist name, anchor moments, cognitive op assignment per slot, rule-bend justifications). Markdown.
5. **Optional mockup** — an HTML rendering of the lessons for design review. Generated only if requested.

### 1.3 Where the output lives

The level JSON feeds the three-bot Slack pipeline: Path Skills Builder Bot produces it, Translation Bot adds Arabic, CMS Upload Bot pushes both languages to Strapi. The first human review gate is in Strapi, post-upload. Lama is QA. Gaia is the sole triage owner.

### 1.4 The contract

The agent does not signal "complete" until:
- All 22 validators pass against schema v3.4
- All 6 review personas have reviewed and produced a score
- The combined self-review average is ≥ 4.0 (CEO lens, Program Director lens, Team Member lens, each averaging individually ≥ 4.0)
- The four artifacts in §1.2 items 1-4 are produced
- The decision log explicitly documents any rule-bend with justification

If any of these fail, the agent revises and re-runs validation. The agent does not hand off partial work.

---

## Section 2 — Hard rules (Tier 1 — non-negotiable)

These rules are absolute. A level that violates any hard rule is not shipped. Every rule below is numbered for citation.

### 2.1 Voice and tone

**HR-1. Conversational mentor voice.** Every screen reads in the voice of a knowledgeable friend, not an editorial writer. Three voice tests apply to every screen:
- *Friend test:* Could this sound like something said over coffee, or does it read as editorial prose?
- *Cognitive ease test:* No screen requires more than one thinking move. A thinking move is a new concept, an inference, a comparison, or a chain of reasoning.
- *Picture test:* After reading, the reader can picture something concrete — a person, a place, a moment, an object.

**HR-2. Empowering tone.** The reader is treated as a capable practitioner-in-training, not as a novice being lectured. Banned phrasings: "you should," "you must," "the right answer is," "this is wrong because." Allowed phrasings: "what works is," "the cleaner signal is," "buyers act."

**HR-3. No role assumptions.** The level never assumes the reader is a founder, a CEO, an entrepreneur, a marketer, or any specific role. The reader is positioned as someone *learning the skill*. Banned phrases: "as a founder," "in your business," "your customers," "for entrepreneurs like you." Allowed phrases: neutral framing using the protagonist's situation.

**HR-4. Plain language default.** No corporate-speak, no jargon, no acronyms. Banned terms: monetization, productize, validation funnel, customer development, MVP, north-star metric, pivot, traction, go-to-market, TAM, SAM, SOM, value proposition, actionable insights, synergy, iterate. Allowed substitutes: pay, charge, prove, ask, test, sell, first version, the test, the audience, the goal, the next move.

### 2.2 Structural

**HR-5. Three-phase structure with L1-mirror pacing for L2-L10 (REVISED in vG.6, M14 follow-up).** Every level is exactly Phase 1 (Hook) + Phase 2 (Acts) + Phase 3 (Wrap). The lesson counts and type distribution depend on level position:

- **L2-L10:** **12 lessons total, 7 concept + 5 graded** (matches L1's count and pacing exactly — revised in M14 follow-up per Arman directive after L2 cascade review found previous 9-concept-3-graded ratio too concept-heavy and missing narrative structure). Phase structure: 3 + 7 + 2.
  - **Phase 1 hook (3 concepts):** L01 universal master claim, L02 protagonist intro, L03 problem invitation. Same as L1.
  - **Phase 2 acts (4 concepts + 5 graded = 7 screens at L04-L10):** L04 c1 opener → L05 c1 graded (MCQ Op 1, HR-13c) → L06 c1 graded (Myth Buster Op 3 or Scenario Op 5) → L07 c1 graded (Scenario Op 5 or Op 4) → L08 c2 opener with flashback → L09 c2 graded (Scenario short Op 4) → L10 c2 graded (Scenario short Op 5, resolution).
  - **Phase 3 wrap (2 concepts at L11-L12):** L11 principle card (absorbs the c3-substance from prior architectures; the principle is the third teaching beat distilled to canonical form), L12 assignment + open loop.
  - **Two explicit canonical concepts (c1, c2) + one implicit concept absorbed into the principle.** This is the new L1-mirror pattern. The principle card at L11 carries the third concept's substance as the level's crystallized takeaway — not as a separate teaching beat but as the synthesis of c1 + c2 into a canonical principle.
- **L1:** 3 + 7 + 2 = 12 lessons (the abbreviated architecture, governed by §5.5). Phase 2 carries 5 graded lessons interwoven with 2 concept screens (c1 opener + c1 deeper/flashback). Phase 3 carries the principle card plus the open-loop / transformation-promise screen (no assignment). Unchanged in M14. L1 differs from L2-L10 only in concept count (1 concept × 5 angles vs 2 explicit concepts + 1 absorbed) — the screen-by-screen pacing is identical.

**Max-concept-back-to-back cap (NEW in M14 follow-up).** No more than 4 concept screens may appear consecutively without a graded screen between them. L01-L04 hits this cap exactly (3 hook concepts + 1 c1 opener); L05 must be graded. Phase 3 ends on 2 consecutive concepts (L11 principle + L12 open loop) — well within the cap. Enforced by Validator V35 (new) at review time and by the LXD §4.13 concept-density audit at draft time.

The vG.0 bridge phase remains retired in vG.2+; the universal hook on L01 transitions directly to the protagonist on L02 without a separate bridge screen. This applies to both architectures.

**HR-6. Three acts in Phase 2.** Phase 2 is divided into three acts. Each act tests a different stage of the protagonist's experiment journey. Acts are not "loops" — the term "loop" is retired in vG. Each act has 3 graded lessons. Concept screens between acts handle transitions. Act 3 carries two concepts (c3 + c4) with a turning-point concept screen between them.

**HR-7. Concept-before-tested.** A concept is taught on a concept screen before it is tested by any graded lesson. The agent maintains a retrieval map showing for each graded lesson which concept screen taught the concept being tested.

**HR-8. Act rhythm cap.** No more than 5 graded lessons may appear consecutively without a concept screen between them. The current architecture caps at 3 graded consecutive — well within. The cap applies inside acts, between acts, and across the whole level.

**HR-9. Insight density distribution.** Level 1 of every path contains zero "textbook" classified lessons. Lessons are classified as `surprising`, `reframed`, `actionable`, or `textbook`. Level 1 uses only the first three. Higher levels may use textbook sparingly.

**HR-10. Em dashes, en dashes, triple-hyphens banned.** Schema-enforced via regex on every text field. Use commas, periods, semicolons, colons, parentheses. Non-negotiable. See §3.5.6 for rhythm substitutes that preserve em-dash voice without using the character.

**HR-11. Level 1 ends on the open loop (REVISED in vG.4 — no assignment).** Phase 3's last lesson carries the open loop into the next level. **L1's open-loop screen is a standalone transformation promise** — no assignment is paired with it. Any attention diverted from the paywall hurts conversion, so the L1 closing screen sells the ROI of the full skill path (or the next level's specific stakes, whichever lands stronger) and ends. L2-L10 keep the §5.4.3 pattern (assignment + open loop). No graded lessons appear after the open loop on any level. The open loop IS the last screen of Level 1.

Stakes in the L1 open loop must be honest: the transformation promise references what the path actually delivers, and the next-level tease references what the next level actually teaches. Fear-mongering and manufactured drama are banned (see HR-32). The example Arman approved as the standard: *"Eight buyers is a real signal. It's not yet a business. Lena's about to lose those eight, and most founders do at exactly this moment. Next up: how to find the audience hiding inside your first eight, before they vanish."* — real stakes, true to L2's actual content.

**HR-12. Phase 3 takeaways are canonical principles.** Every Phase 3 takeaway crystallizes ESTABLISHED teaching of the discipline of the path — recognized wisdom that experienced practitioners and teachers in the field actually teach. NOT the agent's clever phrasing of an adjacent insight. Each takeaway must be cited to canonical lineage in the decision log.

### 2.3 Content

**HR-13. Strict factual integrity.** Every numerical or attributable claim is sourced. Fictional anchors (the protagonist's specifics) are clearly fictional. Public-figure attributions are verifiable. Industry numbers are sourced to a real study or paper.

**HR-13c. First graded slot is a confidence-builder (NEW in vG.4).** The first graded lesson of every level uses Cognitive Op 1 (recognize/distinguish) or Op 4 (choose best next step) — never Op 3 (diagnose what is wrong) or Op 5 (predict outcome). The first graded screen's job is to land a clean correct answer the reader can earn from what they've just been taught. A stumper first slot kills momentum at exactly the point the reader needs a small win to keep going. The cognitive load ramps up across the level, not at the start.

**HR-14. User wellbeing guardrails.** No content shames the reader, treats their lack of knowledge as a failure, or centers a learning moment on financial ruin or personal crisis. Stakes are framed as decisions under uncertainty, not as catastrophe.

**HR-15. No religious or cultural occasion as sales backdrop.** Zero references to Ramadan, Eid, Christmas, Hajj, weddings, Mother's Day, or any religious or cultural occasion as a backdrop for selling, pricing, or testing demand. Settings must be neutral business contexts.

**HR-16. No instructor or platform-figure references.** The level contains zero references to Maharat instructors, masterclass guests, or platform figures. Phase 3 takeaways attribute to canonical doctrine without naming a Maharat-specific instructor. The level reads as pure educational content.

**HR-17. In-level answerability.** Every graded question must be answerable from concepts taught earlier in the same level. The reader is never expected to know industry benchmarks, conversion rates, market norms, technical jargon, or other outside knowledge. If a question depends on outside knowledge, the agent either teaches the benchmark earlier in the level or rewrites the question to test the concept directly.

**HR-18. Curriculum design completed before phase content.** The `curriculum_design` and `expanded_curriculum_design` blocks are completed before any lesson copy is drafted. Schema requires both at the top level of the JSON.

### 2.4 Character architecture

**HR-19. One protagonist per level (with documented-exception policy for named counterparties — REVISED in vG.3).** Every level has exactly one named protagonist. The protagonist is named on the very first screen (L01) and appears throughout the level. By default, NO other named characters appear anywhere — not as anchors, not as test instances, not as side examples. Anonymous descriptors are permitted ("a customer," "a regular," "a coworker"). Canonical-doctrine attribution (Eric Ries, Daniel Kahneman, etc.) is permitted only in `source_allocation`, never in lesson copy.

**Documented exceptions for named counterparties (NEW in vG.3).** Some disciplines — Negotiation chief among them — require a named counterparty whose specific words and pushback the level teaches the reader to read. For these levels, a single named non-protagonist actor per cluster is permitted, provided ALL of the following are true:

- The actor's action scope is conduit / counterparty (not a parallel protagonist).
- The actor has no internal-reasoning sections in the copy (the protagonist's column carries all internal reasoning; the counterparty appears only through their words and observable behavior).
- The protagonist remains the reader's single surrogate throughout.
- The exception is logged in Appendix C (named-counterparty exceptions) before the level enters validation.

A cluster where a side character has internal reasoning, parallel agency, or appears in 4+ consecutive levels as a co-protagonist still violates HR-19 and is rejected. The exception covers the specific case of a single named counterparty whose role is to deliver the other side's position in a deal — not the broader case of multiple named characters with their own arcs. Validator V17 enforces this distinction: it accepts a named non-protagonist whose action scope is conduit/counterparty, and flags any character who functions as a parallel agent. See Appendix C for the canonical examples (Mr. Khalid, Ms. Hala, Mr. Faisal in the Negotiation Beginner path).

This rule was reaffirmed strict in vG.1 against the v2.1 mockup's side-character pattern (Karim, Yara, Reem, Adnan in v2.1 are all retired in vG.1). The vG.3 documented-exception policy does not undo that retirement — those characters had internal reasoning and parallel agency, which still fail the HR-19 test. The policy carves out only the narrower case of conduit counterparties.

**HR-20. Phase 1 plants the master claim universally before the protagonist enters. (REVISED in vG.2.)** Phase 1 is 3 screens. L01 is a universal concept screen that plants the master claim — no character, no specific place, only the discipline-specific puzzle every reader will recognize. L02 introduces the protagonist with full sensory anchor: name, city, occupation, *current_baseline* (her existing success and standing — see §4.4), signature object. L03 names her problem and invites the reader directly with a question they will spend the level helping the protagonist answer. The vG.1 cold-open-with-character-on-L01 rule is reversed: the master claim now lands universally before the case study walks on stage. The earlier vG.0 rule of 4 universal screens plus a separate bridge is also retired — one universal screen is enough to plant the master claim before the protagonist arrives.

**HR-21. Mini-cases are protagonist's own prior attempts.** When a level needs to illustrate a concept with a side example, that example is told as the protagonist's own earlier attempt — a flashback to "last quarter" or "before this year." Side characters with their own names are not introduced. The protagonist's prior attempts are referred to in third person about her past self ("Last quarter, Lena tried…").

### 2.5 Concept architecture

**HR-22. Concept seamlessness.** The four canonical concepts are connected as one protagonist's evolving experiment, not as four discrete topics. Each concept-to-concept transition is a story beat in the protagonist's arc. The agent produces a concept progression rationale (Section 4.3) showing this beat-by-beat.

**HR-23. Concepts per level (REVISED in vG.6 / M14 follow-up).** Concept count depends on level position:

- **L2-L10:** **Two explicit canonical concepts (c1, c2) + one implicit concept absorbed into the principle card.** Each explicit concept maps to one act in Phase 2: c1 gets 1 opener (L04) + 3 graded retrieval points (L05, L06, L07 from different cognitive ops); c2 gets 1 opener with flashback (L08) + 2 graded retrieval points (L09, L10). The implicit third concept's substance lands as the canonical principle at L11. This matches L1's exact pacing of 7 concept + 5 graded screens. **Revised in vG.6 / M14 follow-up from earlier "three explicit concepts (c1, c2, c3) × 1-2 graded each"** because the prior architecture produced concept-heavy lesson plans (9 concept + 3 graded) that missed narrative structure. The L1-mirror pattern restores the question-driven pacing while preserving the level's teaching depth (the third concept is no less taught — it's distilled into the principle rather than introduced via a standalone opener screen).
- **L1:** Exactly **one canonical concept**, taught from **five angles**. The single concept is tested by five graded questions using different cognitive operations (the locked sequence: Op 1 → Op 3 → Op 5 → Op 4 → Op 5). The single concept maps to a single Phase 3 takeaway (one principle card). Unchanged in M14. This is L1's job — install one foundational mental model deeply.

**HR-24. Master claim governs the level.** Every concept is a facet of the master claim. Every graded question is a test of the master claim through one of the concepts. The master claim is restated in Phase 3 in the language the reader has earned by the end.

### 2.6 Output integrity

**HR-25. Character-count validation table required.** Every level run produces a table of all text fields with their length, band, and status. This is a deliverable, not an internal artifact.

**HR-26. Decision log required.** The agent documents every choice made during the run: protagonist name and city, concept order, cognitive op assignment per graded slot, any rule-bend with justification. The decision log is a deliverable.

### 2.7 Storytelling craft (NEW in vG.1)

**HR-27. Italics convention.** Italics inside `concept_explanation` carry exactly three jobs and only three: (1) binary opposition (`_word A_` vs `_word B_`), (2) quoted speech in short form ("the customer who says _tell me when it is ready_"), (3) stress on the turning word that flips meaning ("the words _become_ evidence"). Italics are encoded in the JSON via markdown `_word_` syntax. Italics for decoration, generic emphasis, or arbitrary stress are not permitted.

**HR-28. Lead phrase required on every concept screen.** Every concept screen opens with a short phrase (5-30 chars) that names the move the screen is about to make. The lead phrase is the first sentence of `concept_explanation`. Renderer applies Primary-color tinting. Lead phrases come from a closed catalog of moves (§3.5.1): naming, setup, reveal, pivot, reframe, closure, action. Concept screens without a lead phrase fail review. Phase 3 principle cards (`mini_case_tag: principle_card`) are exempt — those open with the principle directly.

**HR-29. Multi-select MCQ reserved.** The schema reserves a `multi_select` lesson type as `to_be_built` (§6.8). Agents do not produce multi-select questions yet. The visual layer ships rendering and the spec turns on at that point.

**HR-30. Verbatim customer quotes use single quotation marks. (NEW in vG.2.)** When a customer's exact words are evidence — when *what they said* is what the lesson is testing — the words appear in single quotation marks. Example: *Several said it was 'the best thing she's ever made.'* Verbatim quotes are not the same as italicized short-quoted speech (HR-27): italics indicate the screen's voice flagging a quote rendered inline; quotation marks indicate a direct, unedited customer voice landing as evidence. Use single quotation marks specifically; double quotation marks are reserved for the renderer's own UI (CTA labels, dialog text).

**HR-31. Contractions are the default voice. (NEW in vG.2.)** HR-1 establishes the friend voice. Friends speak in contractions: *she's*, *they've*, *doesn't*, *isn't*, *can't*. The agent uses contractions throughout lesson copy by default. Non-contracted forms (*she is*, *they have*, *does not*) are acceptable only when (a) the contraction would create awkwardness or ambiguity, (b) the screen calls for emphasis on the auxiliary verb, or (c) the screen is a formal canonical-principle restatement (Phase 3 principle cards) where elevated register is appropriate. Default formal voice is a violation; the agent must contract by default and justify the non-contracted form when used.

**HR-31c. Principle card uses non-contracted phrasing (NEW in vG.4).** The Phase 3 principle card is the one place where elevated register is not just allowed but required. The aphoristic statement of the canonical principle reads stronger uncontracted: *"There is a cleaner signal."* not *"There's a cleaner signal."* This rule pairs with HR-28's exemption of principle cards from the lead-phrase requirement — both reinforce that the principle card stands apart from the level's friend voice. Aphorisms are the discipline speaking, not the friend speaking.

**HR-32. No overstatement or absolutism (NEW in vG.4).** Lesson copy frames failure modes accurately, not dramatically. Banned framings: *"nobody pays,"* *"everyone fails,"* *"this never works,"* *"100% of founders make this mistake."* Honest framings: *"most of the people who say the first never say the second,"* *"the gap between what people say and what they do is wide,"* *"most ideas fail this way."* The lesson's authority depends on its accuracy. A reader who can name an exception to *"nobody pays"* (and most readers can) stops trusting the rest. Overstatement loses the lesson; calibration keeps it.

This rule extends to graded options, myth-buster framings, and Phase 3 takeaways. Myth busters reframe misconceptions narrowly, not categorically — see §3.5.11.

**HR-33. Word counts per screen type (NEW in vG.4-May-12).** Every screen's body text respects the per-type word cap defined in §6.10. Hard caps are non-negotiable. Targets are the band the agent aims for; over-target screens get one revision attempt before the agent either revises or documents the exception in the decision log. The single exemption is L02 protagonist intro per §6.10 (load-bearing scene); all other exemptions require explicit decision-log entry referencing the cluster's narrative need. Enforced by LXD agent at draft time and by Validator V30 (Georgy queue) at review time. **Source:** May 12 Arman lock; `maharat-vG4-v35-agent-contracts-diff.md` decision 4.

**HR-34. Consecutive concept cards each require an image_brief (NEW in vG.4-May-12).** When two or more concept-type screens (concept / principle / open loop) appear consecutively without a graded screen interleave, every screen in the sequence carries an `image_brief` field per §6.11. The canonical sequences are the Phase 1 hook trio (L01+L02+L03 = 3 images) and the Phase 3 wrap pair (principle + open loop = 2 images). Other consecutive concept sequences trigger the rule too. Enforced by LXD agent at draft time and by Validator V31 at review time. **Source:** May 12 Arman lock; diff doc decision 5 (full illustrations on principle cards) reinforces this rule on the wrap pair specifically.

**HR-35. Exactly one headline per screen (NEW in vG.4-May-12).** Every screen has one and only one headline component per §6.12. Graded screens have no separate `hook_line` component — the question / scenario / statement IS the headline. A 12-word scene-setting leading clause is permitted inside the headline body, never as a separate field. WH-question preference applies: ≥70% of graded headlines per level open with a WH word. Enforced by LXD agent at draft time and by Validator V32 at review time. Schema-level enforcement: v3.5 removes `hook_line` from MCQ, Myth Buster, and Scenario JSON schemas (see §9). **Source:** May 12 Arman lock; diff doc decision 6.

**HR-36. No filler (NEW in vG.4-May-12).** Lesson copy carries only sentences that move the lesson forward. The §7.5 filler test runs at draft time on every screen body. The agent applies the test sentence-by-sentence; the operating question is: *would removing this change what the reader learns?* If no, the sentence gets cut. Filler is not a craft preference — it is a structural failure that breaks word caps (HR-33) and dilutes the lesson's authority.

Banned patterns:
- Restating a prior sentence in different words. *"One is praise. The other is purchase."* restating *"'I love it' is not 'I'll buy it.'"* — one of the two has to go.
- Setup that doesn't pay off. *"Here's what makes X..."* when X follows immediately is filler; the setup line consumed words to deliver nothing the next sentence didn't deliver.
- Meta-stems like *"What this means is..."*, *"The point is..."*, *"In other words..."*, *"At the end of the day..."*. These signal the reader is about to receive the actual content; the agent cuts and starts with the content.
- Transition phrases between paragraphs that don't carry information. *"And so..."*, *"What's more..."*, *"On top of that..."* — used sparingly; default to no transition.
- Decorative adjectives that don't add information. *"absolutely critical"*, *"really important"*, *"very specific"*. Replace with concrete detail or cut.
- *"In order to..."* when *"to..."* would do.

Enforced by LXD agent at draft time per §7.5; included in the LXD self-check audits at §4.13; reinforced by the six-persona review at §8 (the Senior Copywriter persona explicitly checks for filler). No dedicated validator yet — filler detection is harder to automate than word counts or field presence, so V33 is not in Georgy's queue. **Source:** vG.4-May-12 diff doc §7.5 (which framed this as workflow), promoted to hard rule per the May 12 operator directive that the filler test must be non-negotiable, not advisory. [INFERRED promotion — the diff doc did not name filler-cutting as a hard rule; this HR codifies that promotion based on the operator's explicit instruction to make filler-cutting a hard rule alongside length and reviews.]

**HR-37. Mandatory self-review gate before handoff (NEW in vG.4-May-12).** No content leaves the agent without passing every step of the review chain. The chain is:

1. **LXD self-check audits (§4.13)** — five draft-time audits the LXD runs before handoff: word count audit (HR-33), image cadence audit (HR-34), headline audit (HR-35), WH-question preference audit (≥70%), filler audit (HR-36). All five must clear, OR an exception must be documented in the decision log per HR-26 with explicit narrative justification.
2. **Six-persona self-review (§8)** — Curriculum Strategist, Conversion Strategist, Audience Advocate, Senior Copywriter, Devil's Advocate, Reader Surrogate. Each persona scores 1-5 on its specific criteria. Combined average must be ≥4.0 across all six personas. Any individual criterion scoring <4.0 triggers revision of the relevant section before re-review.
3. **Validator suite** — V14 through V32 (current as of v3.5). V30 (word count), V31 (image cadence), V32 (one headline) are the new May-12 validators; V14, V17, V18, V19, V20, V25 are inherited. All applicable validators must run cleanly. A failed validator halts handoff; the agent revises and re-runs.

A persona score below 4.0, a failed audit, or a failed validator each independently halt handoff. The agent does not negotiate with the gate; it revises. This rule prevents the failure mode where content ships with known issues "to be fixed later" — there is no later. **Source:** vG.4-May-12 diff doc + M11 §8 six-persona review + M12 §4.13 audits, consolidated as a hard rule per the May 12 operator directive that review-passing must be non-negotiable, not procedural. [INFERRED promotion — the diff doc and the M11 §8 framed reviews as procedure; this HR codifies the operator instruction that the chain is a hard gate.]

**Provenance note on HR-36 and HR-37.** Neither rule appears verbatim in the May 12 diff document. Both were added per the May 12 operator instruction: *"ensure that the m12 agent has the hard rules about length, no fillers, reviews, etc."* Length is covered by HR-33 (in the diff doc and now in M12). Filler is covered by §7.5 in the diff doc but was not promoted to hard rule by the diff; HR-36 promotes it. Reviews are covered by §8 (M11) and §4.13 (M12 LXD) as procedures but were not framed as hard rules; HR-37 promotes them. Both promotions are transparent rather than silent — flagged here, in the preamble, and in Appendix D.0.

**HR-38. Plain language with explainer-on-jargon (NEW in M13).** Body copy uses plain language a reader with zero domain background would understand. The §3.8 plain-language banned-terms list is promoted from craft guidance to hard rule: monetization, productize, validation funnel, customer development, MVP, north-star metric, pivot, traction, go-to-market, TAM, SAM, SOM, value proposition, actionable insights, synergy, iterate — all banned in body copy. Domain-specific industry jargon ("capsule" in fashion, "trunk show" in retail) replaced with plain-language equivalents ("first batch," "styling event"). Where a technical term is essential and cannot be replaced, an inline explainer is added on first use — short (≤12 words), concrete, and itself jargon-free. **The financial-term cluster** (gross margin, P&L, cost of goods, overhead, surplus, payback, EBITDA, runway, break-even, unit economics) must always carry an inline explainer on first appearance, never assumed. Enforced by LXD agent at draft time per the new §6.15 explainer pattern; included in the LXD §4.13 audit chain as the jargon audit; reinforced by the Senior Copywriter persona in the §8 six-persona review. **Source:** May 12 evening Arman directive: *"make sure when any new definition is used that an explainer is added assume zero knowledge this includes gross margins etc."* Validator V34 (jargon-without-explainer audit) queued for Georgy.

**HR-39. Inline rich-text markup on body copy (NEW in M13).** Concept card bodies and after-wrong explanation bodies carry inline CKEditor-compatible markup, not deferred-to-end emphasis. Specifically: every phrase listed in the `highlight_phrases` field is also bolded inline where it appears in the body using `**bold**` markdown / `<strong>` HTML; selective italics (`*italic*` / `<em>`) mark contrasting concept terms (e.g., *admirer* vs *buyer*); underscored italic (`_..._` / `<em>`) marks abstract concept terms standing alone, used sparingly. After-wrong bodies bold the single key takeaway sentence-fragment. The bottom `highlight_phrases` list is preserved as a reference for translators, validators, and CMS index — it is no longer the only source of visual emphasis. Graded screen questions / scenarios / statements do not carry inline bold (the headline is already the screen's primary emphasis); their after-wrong bodies do. **Source:** May 12 evening Arman directive: *"body copy in concept cards uses ck editor formatted text with highlighting, italics, bolding, etc and the copy docs outputted need to have this as a rule."* Enforced by LXD agent at draft time per the new §6.14 formatting standard; included in the LXD §4.13 audit chain as the markup-presence audit; visible in Strapi paste docs (CKEditor renders the markup directly). Validator V33 (markup-presence audit) queued for Georgy.

**Provenance note on HR-38 and HR-39.** Both rules surfaced during the May 12 Entrepreneurship L2 production pass when Arman flagged that (a) L2 copy used "capsule" and "trunk show" without explanation, (b) the L1 template body copy had no inline formatting despite highlight_phrases being marked, (c) financial terms would need explainers across L3+. Both rules promote previously-implicit craft conventions to enforceable hard-rule status. Validators V33 and V34 are new in M13 and pending Georgy + Hassan implementation.

---

## Section 3 — Voice and narrative principles

### 3.1 Quantic Principle 1 — Open in a moment, not a thesis

**Definition.** Every screen, especially opening screens of a phase or act, opens with a concrete moment. A specific person doing a specific thing in a specific place at a specific time. Never a generalized claim, abstract framing, or thesis statement.

**Why it matters.** A moment makes the screen *real* before it makes the screen *true*. The reader inhabits the situation before they evaluate the principle.

**Example — what works:** *"A customer picks up the bag, sees the price, sets it down."*

**Example — what does not work:** *"Customers often have second thoughts about purchasing decisions when faced with pricing they perceive as high."*

**Red flag.** If the screen could appear in a marketing email or a generic article, it is not opening in a moment.

### 3.2 Quantic Principle 2 — Internal state on the page

**Definition.** When the protagonist is on screen, the screen names what she is thinking, feeling, or noticing. Not just what she does. The reader sees her interior, not just her exterior.

**Why it matters.** Decision-making is interior. If the reader cannot see the protagonist's interior, the reader cannot model the decision the protagonist is about to make.

**Example — what works:** *"Lena counts the number on her clipboard. Forty-seven. She knows what every one of them said. She does not know what any of them did."*

**Example — what does not work:** *"Lena had collected 47 verbal commitments from interested customers."*

**Red flag.** If the screen describes only events and actions without naming what the protagonist is noticing, thinking, or feeling, it is missing internal state.

### 3.3 Quantic Principle 3 — Sensory anchors

**Definition.** Every screen contains at least one sensory anchor — a color, a place, a time of day, an object, a sound, a smell. The anchor binds the abstract concept to a concrete sensation.

**Why it matters.** Sensory detail converts abstract principles into memorable patterns. The reader remembers the saffron-and-rosewater mille-feuille; they do not remember "the new dessert offering."

**Example — what works:** *"Tuesday afternoon. Flour on her apron. The 47th customer just left smiling."*

**Example — what does not work:** *"During the testing period, she received positive feedback from numerous customers."*

**Red flag.** If a screen could be edited to remove every concrete noun without changing its meaning, it has no sensory anchor.

### 3.4 Quantic Principle 4 — Callback economy

**Definition.** Specific details introduced earlier in the level are referenced again later — never as repetition, always as evolution. The saffron pastry comes back. The 47 yeses come back. The Tuesday afternoon comes back. Each callback adds a layer of meaning, never just reminds.

**Why it matters.** Callbacks bind the level into a single story. The reader feels they are following one protagonist through one journey, not flipping through unrelated examples.

**Example — what works:** Phase 1 introduces "the customer who picks up the bag." Phase 2 returns: "Forty-seven customers picked up Lena's saffron pastry. None of them paid for it." Phase 3 closes: "The customer who picks up the bag is your truest signal — and it is a signal you cannot read until you stop reading words."

**Red flag.** If a callback restates a fact the reader already knows without adding meaning, it is repetition, not callback.

### 3.5 Storytelling craft moves (NEW in vG.1 — the v2.1 voice anchor)

The four Quantic principles in §3.1-§3.4 set the philosophy. This section catalogs the specific craft moves the agent uses to land that voice on the page. These moves are observed in the v2.1 mockup and codified here as the canonical authoring vocabulary.

#### 3.5.1 Lead-phrase moves

Every concept screen opens with a short phrase (5-30 chars) that names the move the screen is about to make. The renderer ties this lead to the screen's first sentence and applies a Primary-color tint. Lead phrases are not titles; they are openers. Per HR-28 they are required on every concept screen (except Phase 3 principle cards).

The repertoire:

| Move | Function | Examples |
|---|---|---|
| Naming | Introduces a new person, place, or moment | "Meet Lena." · "Tuesday afternoon." · "Six months ago." |
| Setup | Names what the screen is about to do | "Here's her problem." · "Here's the catch." · "Here's the puzzle." |
| Reveal | Marks a counterintuitive insight arriving | "There's a cleaner signal." · "There's a hidden cost." · "There's a different question." |
| Pivot | Shifts the reader from one frame to the next | "Now for the strongest signal." · "But there's a complication." · "And then this happens." |
| Reframe | Names a reframe of what the reader thought they knew | "Here's the reframe." · "Here's what changes." |
| Closure | Crystallizes what was learned | "Let's bring it together." · "And there's the lesson." |
| Action | Sets up an assignment or commitment | "One small assignment." · "Here's what to try this week." |

The lead phrase is empowering, not lecturing. It does not assume the reader's identity ("As a founder you would..." is banned per HR-3 — even softened versions like "Here's the reframe most founders miss" are not allowed because they imply a reader role).

**Variation rule (NEW in vG.2).** No single lead-phrase formula appears more than twice in a single level. If "Here's her problem" is on L03, the agent does not also use "Here's the catch" on L08 unless the third use of the *Setup* move category genuinely earns its place — and even then, the third Setup variant must use markedly different wording. Variation in the move is part of the craft. The Senior Copywriter persona (§8.1) audits this in Stage 2.5 by counting moves across the level.

#### 3.5.2 Hook-line moves (graded lessons only) — DEPRECATED FOR L2-L10 IN M13 PER HR-35

**Status:** The `hook_line` field on graded lessons was decommissioned in M13 by HR-35 ("Exactly one headline per screen"). The question / scenario / statement IS the graded screen's headline. Any scene-setting is a ≤12-word leading clause inside the headline, never a separate field. v3.5 schema removes `hook_line` from MCQ, Myth Buster, and Scenario JSON.

**The historical catalog below is preserved as a reference for two reasons:** (1) lineage clarity — past levels authored under vG.2/vG.3 used the catalog and the prose voice it teaches is still load-bearing; (2) the scene-setting voice the catalog encoded now lives inside the headline body instead of as a separate field. The agent uses the same scene-setting moves — they just live inside the question / scenario / statement now.

Every graded lesson begins with a `hook_line` (30-80 chars) that introduces the question with a verbal move. The hook signals the lesson type the reader is about to face and grounds it in the protagonist's situation.

| Move | Function | Examples |
|---|---|---|
| Setup | Tells the reader where in the protagonist's day this happens | "Tonight Lena drafts her plan." · "Tomorrow Lena chooses what to do." |
| Test | Marks a "now apply this" beat | "Let's test this on Lena's situation." |
| Bust | Marks a Myth Buster | "Let's bust a common belief." · "A common phrase customers use." |
| Audit | Asks what the protagonist should conclude | "What did Lena actually prove?" · "What is Lena reading right?" |
| Apply | Names a specific application | "Lena is interviewing customers." · "Lena writes down four tests." |
| Closure | Marks a wrap or final test | "One more myth before we wrap." · "Quick review." |

#### 3.5.3 Italics convention (per HR-27)

Italics inside `concept_explanation` are encoded via markdown `_word_` syntax and carry exactly three jobs:

| Job | Pattern | Example |
|---|---|---|
| Binary opposition | `_word A_` vs `_word B_` | "what people _did_, not what they _said_" |
| Quoted speech (short) | `_quote_` | "The customer who says _tell me when it is ready_" |
| Stress on the turning word | the word that flips meaning | "the words _become_ evidence" |

Italics for decoration, generic emphasis, or arbitrary stress are not permitted. The renderer converts `_word_` to `<em>` or visual italic equivalent.

#### 3.5.4 Chapter labels (optional)

Some concept screens carry a small-caps muted subtitle above the lead phrase — the optional `chapter_label` field on concept cards (5-30 chars). The label functions as a chapter marker, not as a heading. The renderer treats it as secondary to the body.

| Use | Example |
|---|---|
| Phase or theme name | "Why most ideas never sell" · "What people did vs what they said" |
| Synthesis cue | "What you just learned" · "The takeaway" |
| Theme cue | "The only test that doesn't lie" |

Default null (no label). Use sparingly; not every screen needs one.

#### 3.5.5 Highlight phrases (optional)

The optional `highlight_phrases` array marks 1-30 char phrases inside the body that should receive sage-tinted background emphasis. The renderer scans the body for verbatim matches and applies the treatment.

Use highlight phrases for:

| Job | Example |
|---|---|
| Canonical-language anchors | "buyers act" · "admirers nod" · "past behavior" · "future intent" |
| Reframe phrases | "no real demand" · "polite encouragement" · "real demand" |
| Sticky labels | "Demand Reader" · "clunky workaround" · "wallet open" |

Maximum 6 highlight phrases per screen. Keep total highlighted text below 30% of body length to avoid visual fatigue.

#### 3.5.6 Em-dash rhythm substitutes

Em dashes (`—`), en dashes (`–`), and triple hyphens (`---`) are banned per HR-10. Schema-enforced via regex. The substitutes that preserve the rhythm em-dashes were carrying:

| Original em-dash use | Substitute | Example |
|---|---|---|
| Definition or apposition | Colon | "she's been obsessing over one new recipe: a saffron-and-rosewater mille-feuille" |
| Sentence break with momentum | Period | "Real demand looks completely different. Once you see it, you can't unsee it." |
| Two related clauses | Semicolon | "Buyers act; admirers nod." |
| Parenthetical | Parentheses or commas | "her recipe (the saffron mille-feuille) became her obsession" |

When in doubt, period. Two short sentences read tighter than one long sentence with an em-dash break, and they hit harder.

#### 3.5.7 Verbatim customer quotes (NEW in vG.2)

When a customer's exact words are evidence the lesson is testing, render those words in single quotation marks, not paraphrased. The reader needs to *hear* the praise to feel how seductive it was. Per HR-30:

| Use | Pattern | Example |
|---|---|---|
| Customer praise as evidence | Verb of saying + 'quoted phrase' in single quotes | *"Several said it was 'the best thing she's ever made.'"* |
| Customer hesitation as evidence | Same pattern | *"Two regulars asked 'when can we order it?' but never did."* |
| Customer preference statement | Same pattern | *"He said 'I'd buy that every week if you made it.'"* |

**Why verbatim over paraphrase.** The lesson is testing whether the reader can read the gap between *what the customer said* and *what the customer did*. Paraphrasing the customer's words ("praised it highly," "expressed strong interest") collapses that gap and weakens the lesson. The reader should encounter the actual seductive surface that fooled the protagonist, not a smoothed summary of it.

**Single quotation marks specifically.** Double quotation marks are reserved for the renderer's own UI elements (CTA labels, dialog text). All in-body customer quotes use single quotation marks to keep this distinction clean.

**Distinction from italics-quoted speech (HR-27).** Italics on a short phrase mark a *category* of quoted speech the screen is gesturing at ("the customer who says _tell me when it is ready_"). Single quotation marks mark a *specific* customer's actual words landing as evidence ("She said 'tell me when it's ready.'"). When in doubt: if the screen is naming a pattern, use italics; if the screen is presenting evidence, use quotation marks.

#### 3.5.8 Title craft — concrete over aphoristic (NEW in vG.4)

Concept screen titles do one job: orient the reader to what this screen is about. They are descriptive statements, not riddles, not aphorisms. Aphorisms read poetic to the agent who wrote them and abstract to the first-time reader who hasn't yet earned the punchline.

| Don't | Do | Why |
|---|---|---|
| *"Where most ideas die"* | *"Why most ideas fail"* | Concrete describes; aphoristic implies the reader already knows |
| *"The signal she's missing"* | *"Praise isn't demand"* | Names the lesson; aphoristic teases it |
| *"Past behavior is the data"* | *"What they did, not what they said"* | Specific dichotomy; aphoristic generalizes |

**Principle card title is a descriptive statement** — the aphorism lives in the body where it has been earned. *"What real demand looks like"* is the title; *"Buyers act. Admirers nod."* is the first line of the body. Putting the aphorism in the title makes it a riddle to a fresh reader, costs the moment of recognition the body is supposed to deliver.

**Diagnostic for the agent.** Read the title without having read the body. If a first-time learner could answer the question *"what is this screen about?"* from the title alone, it passes. If the title is opaque without the body, rewrite to a concrete statement.

#### 3.5.9 Body copy — lean, distinct paragraphs, no redundancy (NEW in vG.4)

Three body-copy rules from the Lena cluster iteration:

**Distinct paragraph work.** Each paragraph of `concept_explanation` does its own distinct job. If the body opens with a praise-vs-purchase frame in paragraph 1, the closing principle in paragraph 3 cannot repeat the same frame with different wording. The reader registers redundancy as filler and tunes out. Pattern: paragraph 1 sets up the contrast, paragraph 2 explains the mechanism, paragraph 3 lands a distinct closing image. No image, frame, or phrase from paragraph 2 should be foreshadowed in paragraph 1, and the closing image in paragraph 3 should be visually new.

**Lean over decorated.** Cut decorative detail; keep only load-bearing specifics. *"Designing a small clothing capsule at her dining table: three kaftans and two co-ord sets in a saffron-and-rose print she painted herself"* over-describes. *"Designing kaftans in a saffron-and-rose print she painted herself"* carries the same narrative load with less reader friction. The "capsule" and "co-ord set" details are decoration; the kaftans, the print, and the hand-painted origin are the load-bearing facts.

**Concrete dichotomies over abstract frames.** Hook lessons (L01 of every level) use concrete imagery and specific phrases people actually say. *"'I love it' is not 'I'll buy it.' One is praise. The other is purchase."* lands harder than *"polite encouragement disappears at the price tag."* The reader has heard both *I love it* and *I'll buy it* in their own life; abstract frames have no echo.

#### 3.5.10 Number specificity — calibrated for credibility (NEW in vG.4)

Hyper-specific numbers can read manufactured. The reader notices that a fictional protagonist would have to count exactly 47 admirers to use that number, and the number breaks the spell. Default to **vague-but-credible** numbers for setup, and **precise** numbers for narrative beats that depend on the precision.

| Use | Pattern | Example |
|---|---|---|
| Setup count (the "ambient" total) | Vague-but-credible | *"more than twenty admirers"* |
| Narrative-beat count | Precise | *"8 paid out of more than twenty"* — the 8 matters, the total can be approximate |
| Money figures | Round numbers at credible price points | *"600 AED kaftan, floor 400"* — both round, both in the kaftan market range |
| Time periods | Concrete with stated reference frame | *"six months of nights and weekends,"* *"seven years at the firm"* |

**Drop awkward plural noun constructions.** *"47 yeses"* reads weird because *yes* doesn't pluralize cleanly. Same for *praises*, *nos*, *maybes*. Use concrete nouns (*admirers*, *compliments*, *people*) or singular contrast patterns (*every yes, zero buyers*) instead.

**Industry credibility.** Numbers must match real market positioning. A designer modest kaftan in Dubai is 350-1500 AED, not $25 USD. A premium pastry buyer returns weekly; a designer-clothing buyer returns monthly. The agent reasons about real-world pricing, frequency, and customer behavior before generating numbers, then runs the cluster math check (customer count × price × annual frequency = revenue) before locking. See §4.8.

#### 3.5.11 Myth-buster accuracy — narrow, not categorical (NEW in vG.4)

Myth busters reframe specific misconceptions, not entire categories of evidence. The L1 iteration surfaced this failure mode: a myth buster framed as *"a 5-star review doesn't mean audience fit"* reads as if the lesson is dismissing positive customer signals wholesale. That's the categorical version. The accurate version is narrower: *"a one-time 5-star review doesn't predict whether the customer comes back."*

**The frame.** A myth buster should make the FALSE answer reveal a specific misconception — the one the level is teaching against. It should not reject a broader category of evidence the reader might reasonably be using.

| Don't (categorical) | Do (narrow) |
|---|---|
| *"Customer praise means nothing"* | *"Praise from people who haven't paid yet doesn't predict who will pay"* |
| *"Surveys can't measure demand"* | *"What people say they'd pay always overstates what they pay"* |
| *"A 5-star review doesn't mean audience fit"* | *"A one-time 5-star review doesn't predict loyalty"* |

The reader who knows the category-level statement is too strong will reject the lesson. The reader who recognizes the narrow misconception will trust the lesson.

### 3.6 Three voice tests (apply on every screen)

These three tests are run by the Senior Copywriter persona on every screen during Stage 2.6:

| Test | Question | Action if fail |
|---|---|---|
| Friend test | Would a knowledgeable friend say this at coffee, or does it read as editorial prose? | Rewrite |
| Cognitive ease | Does this require more than one thinking move? | Split into two screens |
| Picture test | Can the reader picture something concrete after reading? | Add a sensory anchor |
| Contraction test (NEW in vG.2) | Are contractions used by default? Any non-contracted form justified per HR-31? | Re-contract |

### 3.7 Empowering-tone reference

**Contractions are the default voice (per HR-31).** Friends speak in contractions: *she's*, *they've*, *doesn't*, *isn't*, *can't*, *won't*, *we're*, *you're*. The agent uses contractions throughout lesson copy. Non-contracted forms are reserved for: (a) cases where the contraction creates awkwardness or ambiguity, (b) emphasis on the auxiliary verb ("Lena *is* about to spend her savings"), and (c) Phase 3 principle cards where elevated register is appropriate ("Buyers act. Admirers nod.").

**Allowed:** "what works is," "the cleaner signal is," "buyers act," "Lena now reads demand by what people do," "you now read demand," "she's been testing," "they've already chosen," "it doesn't prove anything yet."

**Banned:** "you should," "you must," "the right answer is," "this is wrong because," "as a founder you would," "it is a mistake to."

### 3.8 Plain-language reference

**Promoted to hard rule (HR-38) in M13.** This list was craft guidance through M12_1_; M13 makes it enforceable.

**Allowed:** pay, charge, prove, ask, test, sell, first version, the test, the audience, the goal, next move, signal.

**Banned:** monetization, productize, validation funnel, customer development, MVP, north-star metric, pivot, traction, go-to-market, TAM, SAM, SOM, value proposition, actionable insights, synergy, iterate, leverage (as verb), unlock (as verb), bandwidth (as availability), align (as verb), socialize (a doc), tee up, ladder up, double-click, deep dive.

**Domain-specific bans** (illustrative, expanded in §6.15):
- Fashion / retail: capsule → first batch; trunk show → styling event
- Marketing: CAC → cost per customer; LTV → total customer value over time
- Finance: EBITDA → profit before interest, taxes, depreciation
- Negotiation: BATNA → best alternative if you walk away

**Financial-term cluster (always explained on first use per §6.15):** gross margin, net margin, P&L, profit and loss, cost of goods (COGS), overhead, surplus, payback period, EBITDA, runway, burn rate, break-even, unit economics, contribution margin, MRR, ARR, churn, GMV.

If a technical term must appear, it is defined in plain language on first use per the §6.15 explainer pattern. Definitions are short (≤12 words), concrete, and avoid further jargon.

---

## Section 4 — Curriculum design stage

The curriculum design stage runs *before* any lesson copy is drafted. The output of this stage is the `curriculum_design` and `expanded_curriculum_design` blocks of the level JSON. These blocks govern every subsequent decision.

### 4.1 Master claim

A single sentence that compresses the level's thesis. The claim is universal (no character names), discipline-specific (rooted in the path's domain), and slightly counter-intuitive (something an experienced practitioner would nod at, something a beginner would push back on at first).

**Example (Entrepreneurship · Beginner · L1):**
> *Most ideas do not fail because they are bad. They fail because not enough people pay.*

The master claim is restated, in the language the reader has earned, in the final Phase 3 takeaway.

### 4.2 The four canonical concepts

Every level teaches exactly four concepts. Each concept:

- Is named in plain language (≤ 60 chars)
- Maps to canonical lineage in the discipline (cited in the decision log)
- Has its own concept screen earlier in the level than any graded lesson testing it
- Crystallizes in a Phase 3 takeaway

The four concepts are labeled c1, c2, c3, c4. Their order in the curriculum is the order in which the protagonist encounters them.

**Example (Entrepreneurship · Beginner · L1):**

| Concept | Plain-language name | Canonical lineage |
|---|---|---|
| c1 | Buyers act, admirers nod | Lean Startup methodology; customer development |
| c2 | Past behavior beats future intent | Behavioral economics (Kahneman); stated-vs-revealed preference |
| c3 | A discount is a different product than the original | Pricing strategy literature (Hermann Simon); selection-effect research |
| c4 | The smallest paid commitment is the cleanest demand test | YC pre-orders doctrine; customer development |

### 4.3 Concept progression rationale (NEW — replaces side-by-side concept presentation)

A short narrative document showing how each concept emerges from the previous one through the protagonist's situation. Not a list of concepts; a story of how the protagonist meets each one.

**Format:** One paragraph per concept transition (3 paragraphs for a 4-concept level), naming what changes in the protagonist's situation between concepts.

**Example (Entrepreneurship · Beginner · L1):**

> *c1 → c2.* Lena counts forty-seven yeses. None of them have paid yet. She thinks back to the new croissant flavor she launched last quarter — three regulars said they would buy it weekly; only one ever did, and only twice. The gap between what people say they will do and what they actually do becomes her next question.
>
> *c2 → c3.* Lena considers running a launch discount. Half off for the first week, get them in the door, build buzz. She catches herself. If they buy at half off, what has she learned? Not whether they would pay full price — only whether they would accept half off. The discount is testing a different product entirely.
>
> *c3 → c4.* Lena designs a smaller test. Three days, full price, no marketing, just regulars. Whoever pre-pays five dollars today is whoever would pay ten next month. The smallest paid commitment is the cleanest demand test.

The concept progression rationale is the agent's argument that the four concepts flow as one story. If the rationale reads as four disconnected explanations, the concept order or the protagonist's situation needs reworking before any lesson copy is drafted.

### 4.4 The level protagonist (NEW — replaces three-anchor roster)

A single protagonist for the entire level. Defined in `expanded_curriculum_design.level_protagonist` with:

| Field | Description | Example |
|---|---|---|
| `name` | First name only. Common Arabic-region name. | Lena |
| `city` | Specific real city in the Arabic-speaking region. | Beirut |
| `occupation` | Plain-language description of what the protagonist does. ≤ 60 chars. | Runs a small bakery on a quiet street |
| `current_baseline` (NEW in vG.2) | The protagonist's existing success or current standing, *before* the tension arrives. What they're already known for: social standing with their community, an existing achievement, the daily rhythm of their work. The texture that makes the protagonist feel like a real person, not just a problem to solve. 60-200 chars. Distinct from `core_situation`, which captures the new tension. | Regulars know her by name. Her morning manaeesh sells out before noon. |
| `core_situation` | The specific NEW situation that generates the level's tension. ≤ 200 chars. Reads as a counterpoint to `current_baseline`: the new ambition, the new project, the puzzle the level walks the reader through. | She's been testing a new saffron-and-rosewater mille-feuille for six months. Forty-seven customers have praised it. None have paid for it yet. |
| `internal_state_at_open` | What the protagonist is thinking and feeling at the level's open. ≤ 200 chars. | Hopeful but anxious. About to spend her savings on a pastry case and a marketing push. Something feels off about the 47 yeses but she can't name what. |
| `signature_object` | A specific object that becomes the level's recurring sensory anchor. | The saffron-and-rosewater mille-feuille |
| `signature_moment` | A specific recurring moment used for callbacks. ≤ 100 chars. | Tuesday afternoon at the bakery counter, flour on her apron. |

The protagonist's name, city, occupation, current_baseline, and signature object recur throughout Phase 2 and Phase 3. They never change within a level.

**Why `current_baseline` is required.** Without explicit baseline texture, generated copy collapses to all-tension: the protagonist exists only as the problem. v2.1's strongest beats name *who Lena is normally* (regulars by name, manaeesh sells out) before naming *what's gone wrong* (47 yeses, no payments). The contrast between baseline and tension is what gives the level emotional gravity. The agent fills `current_baseline` first, then `core_situation` second; both must be drafted before any lesson copy.

### 4.5 In-level retrieval map

A table showing for each graded lesson which concept it tests AND which concept screen taught the concept. If any graded lesson cannot point to a concept screen earlier in the level that taught what it tests, the lesson is rewritten or moved.

**Example (excerpt — vG.2 numbering):**

| Graded lesson | Concept tested | Taught on screen | Lesson tests by |
|---|---|---|---|
| L05 (MCQ) | c1 | L04 (concept) | Op 1 — Pick strongest signal |
| L06 (MB) | c1 | L04 (concept) | Op 3 — Diagnose what is wrong |
| L07 (Scenario) | c1 | L04 (concept) | Op 5 — Predict outcome |
| L09 (Scenario) | c2 | L08 (concept) | Op 4 — Best next step |
| L10 (MCQ) | c2 | L08 (concept) | Op 2 — Classify |

### 4.6 Insight density allocation

Every lesson is classified by insight density:

- **Surprising** — reframes something the reader thought they knew. Use for ~30% of lessons.
- **Reframed** — names a known phenomenon in a new way that makes it actionable. Use for ~40%.
- **Actionable** — gives a concrete move the reader could make tomorrow. Use for ~30%.
- **Textbook** — purely declarative, no insight beyond the fact. **Banned in Level 1 of every path.**

The agent allocates the density distribution across the level's lessons (12-15 for L2-L10, 12 for L1) in `expanded_curriculum_design.insight_density_allocation` before drafting copy.

### 4.7 Pacing sketch

A one-page outline of the level's lessons showing for each:

- Lesson number
- Phase
- Type (concept_card, mcq, myth_buster, scenario, fill_in_blank, match_the_statement, multi_select)
- Concept tested or taught (one concept for L1; four for L2-L10)
- Cognitive operation (for graded lessons)
- Approximate length budget

The pacing sketch is the agent's blueprint for Stage 2 drafting. Once approved (by the agent's own self-review), no structural changes are made during drafting. Drafting changes copy, not structure.

**Pacing template — L1 (12 lessons, one concept).** The locked sequence:

| Slot | Lesson | Type | Concept | Op | Notes |
|---|---|---|---|---|---|
| 1 | L01 | concept_card | (hook) | — | Universal master claim |
| 2 | L02 | concept_card | (hook) | — | Protagonist intro |
| 3 | L03 | concept_card | (hook) | — | Her problem + reader invitation |
| 4 | L04 | concept_card | c1 (angle A) | — | Opens c1 |
| 5 | L05 | mcq | c1 | Op 1 | Confidence-builder (HR-13c) |
| 6 | L06 | myth_buster | c1 | Op 3 | Diagnose what is wrong |
| 7 | L07 | scenario (long) | c1 | Op 5 | Predict outcome |
| 8 | L08 | concept_card | c1 (angle B) | — | Deepens c1 with protagonist flashback |
| 9 | L09 | scenario (short) | c1 | Op 4 | Choose best next step |
| 10 | L10 | scenario (short) | c1 | Op 5 | Predict outcome — resolves protagonist arc |
| 11 | L11 | concept_card (principle_card) | c1 | — | Phase 3 principle (HR-31c non-contracted) |
| 12 | L12 | concept_card | — | — | Transformation-promise open loop (HR-11) |

**Pacing template — L2-L10 (12 lessons target / 15 max, 3-4 concepts).** Standard architecture per §5.1-§5.4 (revised in M14).

### 4.8 Industry and setting selection (NEW in vG.4)

The agent selects the protagonist's industry, city, and price points before drafting any lesson copy. The choices propagate through every level of the cluster, so getting them wrong at L1 means rebuilding L2, L3, and L10. Five rules govern selection:

**Rule 1 — No category-level demand baseline.** The protagonist's product must be one where a reader cannot fall back on *"people already buy this kind of thing."* Food, generic retail, and well-established categories provide that fallback assumption, which mutes the demand-testing lesson. The protagonist should be creating something specific to themselves: a designed clothing line, a custom service, a software product, a niche craft. Bakery-launches-new-pastry fails this test. Marketing-professional-launches-kaftans passes it.

**Rule 2 — Gulf-centric setting by default.** The dominant target persona is the Gulf-centric professional class. Default protagonist locations: **Dubai or Riyadh** for primary clusters. The L1 protagonist specifically belongs in the most aspirational/relatable city of the path — Dubai works well as the default. Use **Cairo, Amman, Beirut** for diversity across the path's later clusters (e.g., L1 Lena in Dubai, L2's cluster character in Riyadh, an L7 cluster character in Cairo). Cities outside this set (Casablanca, Tunis, Doha) require explicit justification in the decision log.

**Rule 3 — Currency follows protagonist location.** Lena in Dubai → AED. Sami in Riyadh → SAR. Rania in Cairo → EGP (or USD if her business mix is international). The agent never mixes currencies within a cluster.

**Rule 4 — Price points match real market positioning.** Numbers must be locally credible at the price points named. A designer modest kaftan in Dubai is 350-1500 AED; not $25 USD. A premium pastry is 25-45 AED; not 5 AED. Specialty coffee is 18-28 AED; not 8 AED. The agent reasons about real-world pricing before generating numbers and confirms the pricing matches the audience's expectations.

**Rule 5 — Purchase cadences match the price point.** Designer-clothing buyers return monthly, not weekly. Premium pastry buyers return weekly. SaaS customers churn quarterly. Specialty coffee customers visit several times a week. The agent never writes a scenario implying an unrealistic cadence (e.g., "buys two more pieces at full price the following week" at 450 AED for designer clothing) — the reader catches this and the lesson loses authority.

**Math check (mandatory).** Before locking a cluster, the agent verifies that the business numbers form a coherent system across L1, L2, L3, and L10: *customer count × price × annual frequency ≈ stated annual revenue*. If the Lena cluster says L1 ends with 8 paying customers at 450 AED, L3 has 60 paying at 600 AED, and L10 has 200 customers at 250K AED annual revenue at 18 months — the math has to hold (200 × 600 × ~2 visits/year = 240K, which rounds to the stated 250K). Failed math checks block the cluster from validation. Decision log records the math.

**Industry research step.** Before generating numbers for a new industry, the agent reasons about: (a) typical price points, (b) typical purchase frequencies, (c) common customer profiles, (d) typical first-six-months trajectory for an independent operator. The agent does not need to cite external sources, but the numbers must be defensible against someone with industry knowledge.

### 4.9 Cluster continuity and management (NEW in vG.4)

A cluster is the four-level arc where one protagonist runs through their journey: L1 (the foundational mental model), L2 (the next layer), L3 (the layer after that), L10 (the strategic fork 18 months later). Cluster continuity is load-bearing — the reader feels every break.

**Rule 1 — Cascade every change.** When the protagonist's industry, city, or product changes at L1, every reference to product, location, currency, venues, neighborhoods, named characters, and money figures must cascade across L1, L2, L3, and L10. A "9 years of livelihood" baseline that survives a "just launched" rewrite is a break readers notice. The agent verifies continuity after any cluster-level change.

**Rule 2 — Each cluster level's baseline states the protagonist's position in time.** *"Six months since Lena gave notice. The brand has been live for four months."* Tells the reader where they are. Avoids the confusion of *"wait, has the bakery been around for 9 years or 4 months?"* Every cluster level opens with a time-stamp on the protagonist's situation.

**Rule 3 — L1 bookends with L10.** The L1 protagonist returns at L10, 18 months later, for the push/plateau/exit lesson. Same character. Same product. Same city. Preserves narrative coherence across the cluster and gives the learner a complete arc: aspiring → just-launched → growing → strategic fork. Do not introduce a different character at L10 unless the cluster architecture explicitly calls for a multi-protagonist path (rare; requires explicit justification in the decision log and HR-19 exception per §2.4).

**Rule 4 — Venue palette prevents narrative fatigue.** Each cluster gets a venue palette assigned before drafting: a **launch venue** (L1 or L05 of L1), a **flashback venue** (L1's protagonist-flashback screen), a **watering hole venue** (L2's where-her-audience-lives screen), a **fork-in-the-road venue** (L10's offer-arrival scene). The agent does not reuse a venue across levels — a flashback to Alserkal Avenue followed by an L08 pop-up also at Alserkal Avenue reads lazy. The Lena cluster's venue palette is the canonical example (see §11.8).

**Rule 5 — Visual identity threads compound.** Each cluster has a **color signature** (saffron-and-rose for Lena), a **signature product detail** (hand-painted print), and a **recurring sensory motif**. These bind the cluster visually and give Bana a coherent palette to illustrate against. The agent does not reset the visual identity between cluster levels.

**Rule 6 — Pre-launch demand test happens before the leap.** For Entrepreneurship clusters, the L1 demand test produces the data point that justifies the leap. L1 ends with the test result (e.g., 8 paid out of more than twenty admirers). L2 picks up shortly after the leap — *one week*, not four months. A tight L1→L2 timeline avoids continuity awkwardness.

### 4.10 Decision log additions (NEW in vG.4)

The decision log (§9.4) now also records:

- **Industry selection rationale** — why this industry passes Rule 1 of §4.8
- **City and currency selection rationale** — why this city, why this currency
- **Pricing logic** — the agent's reasoning for the price points chosen, with industry credibility check
- **Venue palette** — the four venues assigned to the cluster
- **Visual identity threads** — the color signature, signature product detail, sensory motif
- **Math check result** — customer count × price × frequency = revenue, computed across cluster levels

---

## Section 5 — Phase architecture

### 5.1 Phase 1 — Hook (3 lessons — L01, L02, L03)

**REVISED in vG.2.** Phase 1 was a 2-screen cold open in vG.1 with the protagonist on L01; that is now reversed. The master claim plants universally before the case study walks on stage.

**Purpose.** L01 plants the master claim as a universal puzzle every reader recognizes. L02 introduces the protagonist with full baseline texture (her existing standing, her place, her signature object). L03 names her problem and invites the reader directly.

**Form.** Three `concept_card_standalone` lessons. Hero photo on L02. L01 carries no character; L02 and L03 carry the protagonist.

#### 5.1.1 L01 — Universal concept hook (master claim)

**Character rule.** Universal. No protagonist on screen. No specific person, no specific place. The puzzle is named in language any reader of the discipline would recognize.

**Pattern:**
1. Lead phrase (5-30 chars, Primary-tinted): a setup move. Examples: *"Here's the puzzle."* / *"Here's where most ideas die."* / *"Most ideas don't fail the way you think."*
2. Optional `chapter_label`: thematic phrase like *"Why most ideas never sell"*
3. Body paragraph 1: state the universal claim concretely, with at least one numeric or research anchor that gives the claim weight. (e.g., *"In one major study of failed companies, almost half died for the same reason: no real demand. Not bad ideas. Not bad execution. Just no buyers."*)
4. Body paragraph 2: name the trap the master claim addresses. (e.g., *"The gap between what people say and what they do is enormous. What most people call validation is just polite encouragement. Real demand looks completely different."*)
5. Length: 200-340 chars across 2 paragraphs.

**Why universal first.** The reader meets the puzzle as a question they already half-know — every reader of the discipline has seen ideas fail. Once the master claim is in the room, the protagonist's specific situation becomes a *case* of that claim, not an idiosyncratic story.

#### 5.1.2 L02 — Protagonist intro (the case study walks on stage)

**Character rule.** Protagonist enters with full sensory anchor: name, city, occupation, *current_baseline* (the existing-standing texture from §4.4), and signature object.

**Pattern:**
1. Lead phrase (5-30 chars, Primary-tinted): a naming move. *"Meet Lena."*
2. Optional `chapter_label`
3. Body paragraph 1: setting + occupation + `current_baseline` woven together. The protagonist is *known for something good* — that's what makes the tension that comes next matter. (e.g., *"By day, Lena runs a small bakery on a quiet street in Beirut, where the regulars know her by name and her morning manaeesh sells out before noon."*)
4. Body paragraph 2: the new ambition or new project (signature object enters). The contrast between baseline success and new uncertainty. (e.g., *"But for the past six months, after closing, she's been obsessing over one new recipe: a saffron-and-rosewater mille-feuille she's convinced could become her bakery's signature."*)
5. Hero `image_brief`: photo of protagonist in her place with signature object.
6. Length: 200-340 chars across 2 paragraphs.

#### 5.1.3 L03 — Her problem and reader invitation

**Character rule.** Protagonist on screen. Reader addressed directly at the end.

**Pattern:**
1. Lead phrase (5-30 chars, Primary-tinted): a setup move. *"Here's her problem."*
2. Optional `chapter_label`
3. Body paragraph 1: name the puzzle in concrete numbers and verbatim customer quotes (HR-30). The seductive surface that fooled the protagonist. (e.g., *"Lena has tested her saffron mille-feuille on 47 people: friends, cousins, regulars, even her landlord. Every single one said they loved it. Several said it was 'the best thing she's ever made.'"*)
4. Body paragraph 2: name the stakes (about to spend savings) and issue the direct second-person invitation: *"Can you help her figure out whether 47 people loving it actually means anything?"*
5. Length: 250-400 chars across 2 paragraphs.

The 3-screen Phase 1 is the most important sequence of the level for narrative pacing. They earn one hero photo (L02), multi-paragraph render on all three, verbatim customer quotes on L03, and the protagonist's full baseline texture on L02.

#### 5.1.4 Hook section card cap (NEW in vG.3)

The Phase 1 hook (L01 + L02 + L03) renders as **3 or 4 cards total**, never more. This rule constrains how the 2-card split (§6.8.6) applies in the hook section.

- L01 (universal hook, no hero) renders as a single card unless its body exceeds 600 chars.
- L02 (protagonist intro, with hero) renders as a single card unless its body exceeds 400 chars (the hero image takes ~160px of the 600px frame, leaving less room for body text).
- L03 (problem + reader invitation, no hero) renders as a single card unless its body exceeds 600 chars.
- L02 is the only hook lesson that may split. If L01 or L03 are authored over 600 chars, the agent flags for a content trim — it does not split.

**Why this rule.** The hook is the most narratively important sequence in the level. Six-card hooks (every lesson splitting) fragment the master claim's punch and dilute the protagonist's introduction. A 3- or 4-card hook preserves rhythm: claim → protagonist visual → protagonist texture → her problem.

**Authoring implication.** Authors target the §6.2 length sweet spots (200-340 for L01, 250-400 for L03, 200-340 for L02). The 600/400/600 thresholds are the renderer's safety net; content authored to the sweet spots renders comfortably as single cards. The 2-card split is reserved for the rare case where teaching density justifies pushing past the sweet spot — typically L02 on tactical-content paths (e.g., the Voss-flavored Negotiation rebuild).

### 5.2 Bridge (DEPRECATED in vG.1, retained in vG.2)

The vG.0 bridge phase remains retired. The 3-screen Phase 1 in vG.2 absorbs the bridge's function — L02 introduces the protagonist, L03 issues the invitation. The schema retains `bridge` in the `phase` enum for backward compatibility with vG.0 levels; new vG.1 and vG.2 levels do not use it.

### 5.3 Phase 2 — Acts (6-9 lessons across 3-4 acts · REVISED in M14)

**Purpose.** Drive the protagonist through the three (or four, at max-15) canonical concepts, with graded lessons testing each concept as the protagonist meets it.

**Lesson count by target:**

| Target | Phase 2 lessons | Concepts | Structure |
|---|---|---|---|
| **12 (default)** | 6 | 3 | 3 acts × (1 opener + 1 graded) |
| 13 | 7 | 3 | 3 acts × (1 opener + 1 graded), + 1 extra graded on strongest concept |
| 14 | 8 | 3 or 4 | 3 acts × (1 opener + 2 graded), OR 4 acts × (1 opener + 1 graded) |
| **15 (max)** | 9 | 4 | 4 acts × (1 opener + 1 graded), + 1 extra graded on strongest concept |

**Default (target-12) structure:**

| Act | Lessons | Concept | Protagonist's situation |
|---|---|---|---|
| Act 1 | L04 (opener) + L05 (graded) | c1 | Tests with existing customers |
| Act 2 | L06 (opener) + L07 (graded) | c2 | Tests with broader audience (concept opener carries the protagonist flashback) |
| Act 3 | L08 (opener) + L09 (graded) | c3 | Designs the resolution / next experiment |

Phase 3 wrap follows at L10 (synthesis), L11 (principle card), L12 (assignment + open loop).

**Maximum (target-15) structure:**

| Act | Lessons | Concept | Protagonist's situation |
|---|---|---|---|
| Act 1 | L04 (opener) + L05 (graded) | c1 | Existing-customer test |
| Act 2 | L06 (opener) + L07 (graded) + L08 (graded) | c2 | Broader audience (carries flashback); strongest-leverage concept gets two grades |
| Act 3 | L09 (opener) + L10 (graded) | c3 | Near-miss / counter-temptation |
| Act 4 | L11 (opener) + L12 (graded) | c4 | Resolution / strongest signal |

Phase 3 wrap follows at L13 (synthesis), L14 (principle card), L15 (assignment + open loop).

**Within each act:**

- 1 concept screen opens the act (the concept opener)
- 1 graded lesson tests the concept (target); or 2 graded (max, on the strongest-leverage concept only)

**Between-act concept screens.** Single screens that name the transition. They use the protagonist's voice ("Lena thinks back to last quarter…") to bridge from one concept to the next without breaking the arc. Each act's opener IS the between-act transition for the prior act.

**Protagonist case files (per HR-21).** When a level needs an example beyond the protagonist's current situation, the example is told as the protagonist's earlier attempt: "Last quarter, Lena tried promising her regulars a new croissant flavor. Three said they would buy it weekly. Only one ever did, and only twice." Side characters with their own names are not introduced — HR-19 reaffirmed strict in vG.1 and again in vG.2.

**Cognitive operation distribution.** At target 12 (3 graded): Op 1 (or Op 4) + 2 others, no repeat. At max 15 (5 graded): at least 4 different ops used, with no single op used more than twice (V9). The first graded lesson of each act uses Op 1 (Pick strongest signal) or Op 4 (Best next step) — never Op 2, 3, 5, 7 in the act-opening slot (HR-13c).

**Act rhythm cap.** No more than 2 graded lessons consecutive within an act (HR-8's level-wide cap of 5 still applies but is far from binding in the new architecture). At max 15, the only act with 2 consecutive graded is the strongest-leverage concept's act; the others have 1 graded each.

### 5.4 Phase 3 — Wrap & Open Loop (3 lessons · REVISED in M14)

**Purpose.** Replay the protagonist's choice (synthesis), crystallize the canonical principles (takeaway), and hand the reader a concrete assignment paired with the open loop into the next level.

**Form.** Three `concept_card_standalone` lessons. Hero photos optional.

**Screen numbering depends on target lesson count:**

| Target | Synthesis | Principle | Assignment + Open Loop |
|---|---|---|---|
| 12 (default) | L10 | L11 | L12 |
| 13 | L11 | L12 | L13 |
| 14 | L12 | L13 | L14 |
| 15 (max) | L13 | L14 | L15 |

For readability throughout this section, screens are referenced by their **role** (synthesis / principle / open-loop), not by absolute lesson number.

**Structure:**

#### 5.4.1 Synthesis screen (replays protagonist's choice)

The synthesis screen REPLAYS the protagonist's choice now that the level has taught the concepts. It does not state a principle abstractly; it shows the protagonist standing at her decision and naming the path she'll take.

**Pattern:**
- `chapter_label`: *"What you just learned"*
- Lead phrase: *"Let's bring it together."* (closure move per §3.5.1)
- Body paragraph 1: name the protagonist's two paths (what she'd have done before vs what the level taught her)
- Body paragraph 2: name the choice she now makes
- Body paragraph 3: name the reader's parallel transformation, e.g., *"You now read demand the way a Demand Reader does: by what people _do_, not what they _say_."*
- `highlight_phrases`: 1-3 sticky labels from the level (e.g., "Demand Reader", "buyers act")

#### 5.4.2 Principle card (canonical takeaway)

The principle card crystallizes the canonical principles in aphoristic form. It cites no specifics; it names the principle in language the reader has earned by the end. Per HR-31 this lesson type may use elevated register (non-contracted forms acceptable).

**Pattern:**
- `card_variant`: `principle_gold`
- `mini_case_tag`: `principle_card` (this lesson is exempt from the lead-phrase rule per HR-28)
- Body 90-200 chars (aphoristic, sweet spot 120 chars)
- Cite all level concepts (3 at target, 4 at max) crystallized as a unified principle, OR pair them
- `highlight_phrases`: the canonical-language anchors ("buyers act", "admirers nod", etc.)

#### 5.4.3 Assignment + Open Loop

The final screen carries TWO functions: a concrete reader assignment AND the open loop into the next level. They're paired because the open loop is most powerful when it follows a small action the reader can take this week.

**Pattern:**
- Lead phrase: *"One small assignment before you go."* (action move per §3.5.1)
- Body paragraph 1: a concrete weekly assignment for the reader. Specific, doable in under an hour, drawing on the level's central skill.
- Body paragraph 2: the open-loop teaser into Level 2, naming the next-level question explicitly.
- The CTA on the final screen is "Finish lesson" or "Next level"

**No graded lessons in Phase 3.** HR-11.

**Wrap screen rendering.** A separate "wrap screen" (hero photo of protagonist, level-complete confirmation, congratulations) is rendered by the frontend automatically after the final screen completes. The agent does not author the wrap screen — but the final screen's body content is what the wrap screen will quote.

### 5.5 Phase architecture — L1 abbreviated (NEW in vG.4)

L1 of every path uses a 12-screen abbreviated architecture. L1's job is conversion, not curriculum density: install one foundational mental model deeply, demonstrate the platform, and land the reader at the paywall having experienced the protagonist's payoff. The 22-screen architecture pushes the paywall too far out; four concepts spread too thin to feel substantial; the abbreviated form converts.

**Structure.** 3 + 7 + 2 = 12. Phase 1 (Hook): L01-L03 unchanged from the 22-screen architecture. Phase 2 (Acts): one concept taught from five angles across 7 lessons (2 concept screens interwoven with 5 graded). Phase 3 (Wrap): principle card + open-loop / transformation promise. No assignment in L1 (HR-11 revised).

**Locked lesson map (L1 of every path):**

| Lesson | Type | Function |
|---|---|---|
| L01 | concept_card | Universal master claim (§5.1.1) |
| L02 | concept_card | Protagonist intro (§5.1.2) |
| L03 | concept_card | Her problem + reader invitation (§5.1.3) |
| L04 | concept_card | Opens c1 — first angle on the concept |
| L05 | mcq | First graded — Op 1 confidence-builder (HR-13c) |
| L06 | myth_buster | Op 3 — diagnose what is wrong |
| L07 | scenario (long) | Op 5 — predict outcome |
| L08 | concept_card | Deepens c1 — second angle, typically a protagonist flashback |
| L09 | scenario (short) | Op 4 — choose best next step |
| L10 | scenario (short) | Op 5 — predict outcome, resolves protagonist arc |
| L11 | concept_card (principle_card) | Phase 3 principle — HR-31c non-contracted |
| L12 | concept_card | Open loop — transformation promise, no assignment |

**The five angles on one concept.** L04, L05, L06, L07, L08, L09, L10 all teach and test the same concept (c1) — five graded angles plus two concept reinforcements. The concept compounds across the level rather than competing with three others.

**The locked graded sequence.** Op 1 (MCQ) → Op 3 (Myth Buster) → Op 5 (Scenario long) → Op 4 (Scenario short) → Op 5 (Scenario short, resolves arc). This sequence is the result of empirical iteration; it converts. The agent does not vary the sequence without explicit approval from Arman.

**The resolution lands at L10, not L11.** The protagonist's arc resolves at the final graded screen — the reader sees the protagonist's test pay off before the principle is named. L11 (principle card) crystallizes what just happened; L12 (open loop) carries the reader to the next level. This narrative-before-principle sequence converts better than principle-first.

**L12 — Open loop as transformation promise.** The L12 screen sells what the next level will give the reader. Honest stakes only — the next-level reference must be true to what L2 actually teaches. The Lena cluster's L12 is the canonical reference: *"Eight buyers is a real signal. It's not yet a business. Lena's about to lose those eight, and most founders do at exactly this moment. Next up: how to find the audience hiding inside your first eight, before they vanish."*

The transformation promise may reference the **full skill path outcome** (e.g., *"by the end of this skill path, you will know how to build a business from scratch"*) when the next-level tease alone is too narrow to motivate the reader. The agent decides per cluster which framing carries stronger stakes.

**No assignment in L1.** HR-11 revised. Anything that diverts attention from the paywall reduces conversion. The L12 open loop is the entire Phase 3 closing — no "try it this week" call to action.

**Concept screen budget on L1.** Seven concept screens total: L01-L04 (4 in the first half), L08 (1 mid-level), L11 (principle), L12 (open loop). The agent budgets ~340 chars per concept screen (§6.8.6 thresholds); the §6.8.6 2-card split applies to L1 the same way it applies to L2-L10.

**Hook section card cap unchanged.** §5.1.4's 4-card max for L01+L02+L03 applies to L1 the same way it applies to L2-L10. L02 is still the only hook permitted to split.

**Time target.** L1 instructional time should land under 5 minutes total reading. The 12-lesson architecture supports this; the 22-lesson architecture does not. Word count proxy for the 5-minute target is flagged for definition by San (see Appendix E open items).

---

## Section 6 — Lesson type catalogue

Eight lesson types total. Five are currently supported. Three are reserved with full structural specs but flagged `to_be_built` (fill-in-blank, match-the-statement, multi-select).

### 6.0 Schema v3.5 supersession notice (NEW in vG.4-May-12)

The field tables in §6.3-§6.7 below were authored under Schema v3.4. **Schema v3.5 (May 12 Arman lock) supersedes these tables on three specific fields.** Where the field tables and v3.5 conflict, v3.5 wins. The original tables are preserved for historical reference and to document the v3.4→v3.5 migration path.

**Schema v3.5 field changes (override the v3.4 field tables below):**

| Lesson type | v3.4 field | v3.5 status | Replacement |
|---|---|---|---|
| MCQ (§6.3) | `hook_line` | **REMOVED** | Optional ≤12-word scene-setter folded into `question` field |
| Myth Buster (§6.4) | `hook_line` | **REMOVED** | Folded into `title` if scene-setting carried (rare); otherwise discarded |
| Myth Buster (§6.4) | `body` | **RENAMED** to `statement` | Same content, clearer semantic |
| Scenario short/long (§6.5) | `hook_line` | **REMOVED** | Folded into `scenario` field as leading clause |

**Schema v3.5 additional field changes:**

| Lesson type | Field | v3.5 status | Notes |
|---|---|---|---|
| Concept card (§6.2) | `body` | Word-cap tightened (REVISED in vG.6 / M14 follow-up — was 50-90 target / 110 hard cap; reduced by ~50% per Arman directive after L2 cascade review surfaced concept-heavy lesson plans) | **25-50 words target, 60 words hard cap.** L02 protagonist intro and L08 c2 flashback-opener exempt per §6.10 + §11.7 (load-bearing scene-setters, allowed 50-80 words target / 90 hard). |
| Concept card (§6.2) | `image_brief` | Now conditionally REQUIRED | Required if prior or next screen is concept-type per HR-34 (was: optional except L02 + flashback) |
| Principle card (§6.2) | `image_brief` | Now REQUIRED | Full illustration per May 12 decision 5 (was: optional/often omitted) |
| Principle card (§6.2) | `body` | Word-cap tightened (REVISED in vG.6 / M14 follow-up — was 30-60 target / 80 hard) | **20-40 words target, 50 words hard cap.** Aphoristic and dense. |
| Open loop (§6.2) | `body` | Word-cap tightened (REVISED in vG.6 / M14 follow-up — was 50-80 target / 100 hard) | **40-70 words target, 90 words hard cap.** Includes both the assignment line and the next-level tease. |
| All graded types | Headline content | One headline only | The `question` / `scenario` / `statement` field IS the headline per HR-35 |

**Schema v3.5 JSON snippets (canonical — overrides the field tables below):**

```json
// Concept lesson (and principle / open loop variants)
{
  "type": "concept",
  "chapter_label": "...",
  "title": "...",
  "body": "...",                          // 50-90 target, 110 hard cap (L02 exempt)
  "highlight_phrases": [...],
  "image_brief": "..."                    // REQUIRED if prior or next screen is concept-type (HR-34)
}

// MCQ lesson — hook_line REMOVED
{
  "type": "mcq",
  "question": "...",                      // headline (WH preferred), optional ≤12-word leading clause
  "options": [
    { "label": "1", "text": "...", "correct": false },
    ...
  ],
  "after_wrong_title": "...",
  "after_wrong_body": "..."
}

// Myth Buster lesson — hook_line REMOVED, body RENAMED to statement
{
  "type": "myth",
  "title": "...",                         // headline = the WH framing question
  "statement": "...",                     // the T/F text to evaluate (functional component, not a headline)
  "correct": "TRUE | FALSE",
  "after_wrong_title": "...",
  "after_wrong_body": "..."
}

// Scenario lesson — hook_line REMOVED
{
  "type": "scenario_short | scenario_long",
  "scenario": "...",                      // headline + body, optional ≤12-word leading clause
  "options": [...],
  "after_wrong_title": "...",
  "after_wrong_body": "..."
}

// Principle lesson — image_brief now REQUIRED
{
  "type": "principle",
  "title": "...",
  "body": "...",                          // 30-60 target, 80 hard cap
  "highlight_phrases": [...],
  "image_brief": "..."                    // REQUIRED (full illustration per decision 5)
}
```

**Migration path for v3.4 → v3.5.** For each existing v3.4 lesson being moved to v3.5:

1. **MCQ:** Fold `hook_line` content into the start of the `question` field as a leading clause IF it adds scene-setting and fits ≤12 words. Otherwise discard (it was narrative redundancy).
2. **Myth Buster:** Rename `body` field to `statement` (no content change). Discard `hook_line` if it was meta-framing duplicate of `title`; fold into `title` if it carried distinct scene-setting (rare).
3. **Scenario:** Fold `hook_line` content into the start of the `scenario` field. The opening line of the scenario absorbs the scene-setting.
4. **Concept card:** No field changes. Body now fits 50-90 / 110 cap (re-author if over). Image brief added per HR-34 if prior or next screen is concept-type.

The §6.3-§6.7 field tables below describe the v3.4 schema for historical reference. Read with §6.0 in hand.

### 6.1 Concept Card — Sequence (DEPRECATED in vG.1)

**Used in vG.0:** Phase 1's 4-card universal master-claim setup.

**Status in vG.1 / vG.2:** Deprecated. Phase 1 now uses three `concept_card_standalone` lessons (universal hook L01, protagonist intro L02, problem L03) per §5.1. The schema retains the type for backward compatibility with vG.0 levels. New levels do not use sequence cards. If a future authoring need arises (e.g., a multi-screen concept build), the type may be revived; for now it is not produced.

### 6.2 Concept Card — Standalone

**Used in:** Cold open (L01, L02), act-opening concept screens, between-act concept screens, Phase 3 synthesis / takeaway / assignment, optional embedded protagonist case files.

**Required fields:**

| Field | Type | Length | Notes |
|---|---|---|---|
| `concept_title` | string | 5-40 chars | Title displayed prominently |
| `concept_explanation` | string | 90-450 chars | Body text. Multi-paragraph allowed via `\n\n`. **Widened from 90-160 in vG.0** to support v2.1-style richer screens. |
| `image_brief` | string | 30-200 chars | Optional hero photo brief |
| `mini_case_tag` | enum | `protagonist_flashback` \| `principle_card` \| null | Default null |
| `card_variant` | enum | `default_white` \| `evidence_sage` \| `principle_gold` \| `warning_terracotta` \| `retrieval_slate` | Visual variant; renderer uses `default_white` until visual layer ships |
| `chapter_label` | string | 5-30 chars | **NEW in vG.1.** Optional small-caps muted subtitle above lead phrase. See §3.5.4. |
| `highlight_phrases` | array of 1-6 strings | each 1-30 chars | **NEW in vG.1.** Optional. Phrases verbatim in body that get sage-tinted emphasis. See §3.5.5. |

**Length sweet spots within the 90-450 band:**
- Phase 1 hook (L01 universal, L02 protagonist intro, L03 problem): 200-400 chars across 2-3 paragraphs
- Act-opening concept screens (target 12: L04, L06, L08; max 15: L04, L06, L09, L11): 200-340 chars across 2 paragraphs
- Synthesis screen (Phase 3 wrap, first screen): 280-450 chars across 3 paragraphs
- Principle card (Phase 3 wrap, second screen): 90-200 chars (aphoristic; non-contracted forms acceptable per HR-31)
- Assignment + open loop (Phase 3 wrap, final screen): 250-400 chars across 2 paragraphs

**Validation:**
- `concept_explanation` may use `\n\n` for multi-paragraph rendering
- Em-dash sweep applies (HR-10)
- Italics permitted via `_word_` markdown for the three jobs in HR-27 only
- Verbatim customer quotes in single quotation marks per HR-30
- Contractions are the default voice per HR-31
- First sentence ≤ 30 chars triggers lead-phrase Primary-tinted rendering (HR-28 requires this on every concept screen except `mini_case_tag: principle_card`)
- Highlight phrases must appear verbatim in `concept_explanation`; total highlighted text ≤ 30% of body length

**Note on `mini_case_tag`:** With HR-21 retiring named side characters, the tag values reflect protagonist-internal moves: `protagonist_flashback` for "Lena's earlier attempt," `principle_card` for canonical-principle Phase 3 takeaways. Default null.

### 6.3 MCQ

**Used in:** Phase 2 graded lessons.

**Required fields:**

| Field | Type | Length | Notes |
|---|---|---|---|
| `hook_line` | string | 30-80 chars | Optional small italic muted line above the question |
| `title` | string | 70-110 chars | The question stem |
| `options` | array of 4 | each option `text` 30-90 chars | Four options, parallel structure required |
| `correct_index` | integer | 0-3 | Index of correct answer |
| `explanation_title` | string | 3-20 chars | E.g., "Why" or "The signal" |
| `explanation_body` | string | 120-180 chars | Why the correct answer is correct, in plain language |
| `cognitive_operation` | enum | one of 8 | See §6.9 |

**Parallelism:** Max-min length ratio across the 4 options ≤ 2.5. Correct option is not the longest unique option.

**Distribution:** Across the level, the correct_index distribution is ≤ 50% on any single index value.

### 6.4 Myth Buster

**Used in:** Phase 2 graded lessons.

**Required fields:**

| Field | Type | Length | Notes |
|---|---|---|---|
| `hook_line` | string | 30-80 chars | Optional |
| `title` | string | 30-70 chars | The myth-busting question |
| `body` | string | 60-110 chars | The myth statement, often in customer-quote form |
| `correct_answer` | boolean | true or false | The answer to the myth-busting question |
| `explanation_title` | string | 3-25 chars | E.g., "Why this is false" |
| `explanation_body` | string | 130-200 chars | Why the answer is what it is |

**Character rule.** Myth Busters are character-agnostic. They state a universal myth and answer it universally. The protagonist does not appear in Myth Busters.

**Distribution.** Across the level, at least one Myth Buster's correct answer is TRUE.

### 6.5 Scenario (short and long)

**Used in:** Phase 2 graded lessons.

**Required fields:**

| Field | Type | Length | Notes |
|---|---|---|---|
| `hook_line` | string | 30-80 chars | Optional |
| `title_length` | enum | `short` \| `long` | Determines title band |
| `title` | string | 120-160 (short) or 160-220 (long) | The scenario |
| `options` | array of 2 | each option `name` 20-50 chars | Two options, parallel |
| `correct_index` | integer | 0-1 | Index of correct option |
| `explanation_title` | string | 3-20 chars | |
| `explanation_body` | string | 130-190 chars | |
| `cognitive_operation` | enum | one of 8 | |

**Parallelism:** Same as MCQ. Max-min ratio ≤ 2.5. Correct option not the longest unique.

**Distribution.** Correct_index distribution ≤ 65% on any single index value.

### 6.6 Fill-in-Blank (TO BE BUILT — full spec)

**Status:** `to_be_built`. The schema reserves the type. Agents do not produce these yet. When the visual layer ships, this spec is the contract.

**Used in:** Phase 2 graded lessons (planned). Acts as a low-friction retrieval check for previously-taught vocabulary or canonical phrasings.

**Structural spec:**

| Field | Type | Length | Notes |
|---|---|---|---|
| `hook_line` | string | 30-80 chars | Optional |
| `title` | string | 70-110 chars | Question stem with `{{blank}}` token marking the blank |
| `prompt_sentence` | string | 40-130 chars | Sentence with the blank shown to the reader, e.g., "Lena's customers ____ the saffron pastry but never paid for it." |
| `options` | array of 4 | each option `text` 5-25 chars | Four short options for the blank |
| `correct_index` | integer | 0-3 | |
| `explanation_title` | string | 3-20 chars | |
| `explanation_body` | string | 120-180 chars | |
| `cognitive_operation` | enum | one of 8 | Typically Op 6 (Apply principle) or Op 8 (Identify missing) |

**Parallelism:** Options must all be the same grammatical type (all verbs, all nouns, all adjectives — not a mix). Length ratio ≤ 2.5.

**Validation rules to be enforced:**
- Exactly one `{{blank}}` token in `title` or `prompt_sentence`
- All options grammatically substitutable into the blank
- Correct option is not trivially the longest

**Use case.** Retrieval drill of canonical concept names without forcing the reader to write. Tests whether the reader can recognize the concept by the language used to teach it earlier in the level.

### 6.7 Match-the-Statement (TO BE BUILT — full spec)

**Status:** `to_be_built`. The schema reserves the type. Agents do not produce these yet.

**Used in:** Phase 2 graded lessons (planned). Acts as a discrimination check — can the reader tell which of two principles applies to which situation?

**Structural spec:**

| Field | Type | Length | Notes |
|---|---|---|---|
| `hook_line` | string | 30-80 chars | Optional |
| `title` | string | 50-90 chars | The matching prompt |
| `statements` | array of 3 | each statement 60-110 chars | Three short situations |
| `categories` | array of 2 | each category `name` 20-40 chars, `description` 30-90 chars | Two categories the reader matches statements to |
| `correct_mapping` | array of 3 | each entry { statement_index: int, category_index: int } | The expected matching |
| `explanation_title` | string | 3-20 chars | |
| `explanation_body` | string | 130-200 chars | |
| `cognitive_operation` | enum | one of 8 | Typically Op 2 (Classify) or Op 7 (Compare) |

**Parallelism:** All three statements use the same grammatical structure (e.g., all start with "A customer who…" or "A buyer that…"). The two categories are paired, not random topics.

**Validation rules to be enforced:**
- Exactly 3 statements and exactly 2 categories
- Correct mapping covers all statement_indices 0,1,2 with no duplicates on the statement side
- Each category is matched at least once
- Statements use parallel grammatical structure

**Use case.** Tests reader's ability to apply a binary distinction (e.g., "buyer behavior" vs "admirer behavior") to specific cases. Higher cognitive load than MCQ.

### 6.8 Visual rendering rules

#### 6.8.1 Multi-paragraph pacing rule

Concept screens use multi-paragraph breathing room. The body of `concept_explanation` is rendered as 1-3 paragraphs separated by `\n\n` (double newline), not as one continuous block.

**Where the rule applies:**

- Cold open L01 and L02: always multi-paragraph (2-3 paragraphs typical: lead, situation, tension)
- Act-opening concept screens (target 12: L04, L06, L08; max 15: L04, L06, L09, L11): often multi-paragraph for scene-setting
- Synthesis screen (target 12: L10; max 15: L13): multi-paragraph (3 paragraphs typical)
- Assignment + open loop (Phase 3 wrap, final screen): multi-paragraph (assignment paragraph + open-loop paragraph)
- Phase 3 principle card: single-paragraph by default (aphorisms are weakened by line breaks)

**Where the rule does not apply:**

- Graded lesson titles, scenario titles, MCQ options, Myth Buster body — all single-line
- Explanation cards (after wrong answer) — single-paragraph
- Hook lines — one short phrase, no breaks

**Character budget.** The 90-450 char band holds. The `\n\n` characters count toward the total. A 3-paragraph concept_explanation uses 4 newline characters of budget.

**Schema regex.** The em-dash sweep regex permits newlines: `^(?![\s\S]*[\u2013\u2014])(?![\s\S]*---)[\s\S]*$`.

#### 6.8.2 Hero photos

Hero photos appear on a small number of screens in the level:

| Screen | Purpose |
|---|---|
| L02 (Phase 1 protagonist intro) | The level's opening visual — protagonist in her place, with signature object |
| One protagonist-flashback screen (optional) | If a Phase 2 screen uses `mini_case_tag: protagonist_flashback` |
| Synthesis (Phase 3 wrap, first screen) optional | The protagonist after the journey, mood-resolved |
| Wrap screen (frontend only) | Post-final-lesson celebration screen, not in JSON |

All other concept screens use the white card per the locked design system's transitionary-screen spec.

**Image brief format.** ≤ 200 chars. Composition + mood + lighting. Example: *"Photo: Lena in flour-dusted apron behind Beirut bakery counter, holding tray of golden pastries, sunlight from window. Mood: warm, hopeful, slightly anxious."*

#### 6.8.3 Lead phrase (Primary-tinted)

Per HR-28 every concept screen (except `mini_case_tag: principle_card`) starts with a short sentence (5-30 chars, period-terminated) rendered in Primary color (#1A6B5A), bold, on its own line above the body.

**Examples:** *"Meet Lena."* / *"Here's her problem."* / *"Now the strongest signal."* / *"Let's bring it together."*

The lead phrase is part of `concept_explanation` content (counts toward the 90-450 char band). The renderer detects a complete short sentence at the start and styles it as the lead. Authors do not split it into a separate field. See §3.5.1 for the catalog of lead-phrase moves.

#### 6.8.4 Concept card color variants (5 — TO BE BUILT)

Status: `to_be_built`. The schema reserves a `card_variant` field. Default = `default_white`. The visual layer ships these later.

| Variant | Color | Semantic purpose |
|---|---|---|
| `default_white` | #FFFFFF (page bg #FAF9F7 visible) | Standard concept teach. Used for cold open and most between-act screens. |
| `evidence_sage` | Sage tinted card on #5A9E8F accent | Evidence / case-detail. Used for protagonist-flashback screens that present a specific past event. |
| `principle_gold` | Gold tinted card on #C4963C accent | Canonical principle. Used for Phase 3 takeaway screens to mark them as discipline-recognized wisdom. |
| `warning_terracotta` | Terracotta tinted card on #D4764E accent | Warning / common mistake / failure pattern. Used for screens that show what does not work. |
| `retrieval_slate` | Slate tinted card on #4A6FA5 accent | Retrieval prompt / "remember when…". Used for screens that explicitly call back earlier learning. |

**Frontend behavior (when built).** The renderer reads `card_variant` and applies the matching color treatment to the card background, the lead phrase color, and any accent elements. The page background stays #FAF9F7.

**Authoring rule (active now).** Authors fill `card_variant` with the intended variant, even though only `default_white` renders today.

#### 6.8.5 Inline emphasis markup

Inside body text, three markdown patterns are honored by the renderer:

- `**bold**` → `<strong>` — used sparingly; at most one bold per screen.
- `_italic_` → `<em>` — restricted to the three jobs in HR-27 (binary opposition, quoted speech, stress on turning words).
- `[[highlight]]` → highlighted span (sage-tinted). Authors prefer the structured `highlight_phrases` array over inline `[[...]]` markup; both work, but the array makes phrases auditable.

The Translation Bot preserves markup verbatim.

#### 6.8.6 Two-card split for over-cap concept screens (NEW in vG.3)

When a concept screen's body exceeds its single-card threshold, the renderer splits the body across two stacked cards. This is a rendering behaviour, not an authoring instruction — authors target the §6.2 length sweet spots, and the split applies as a safety net for content that runs hot.

**Threshold table.** Each lesson position has a single-card threshold; bodies under the threshold render as one card, bodies over it split into two.

| Lesson position | Single-card threshold | §6.2 sweet spot |
|---|---|---|
| L01 (universal hook, no hero) | 600 chars | 200-340 |
| L02 (protagonist intro, with hero) | 400 chars | 200-340 |
| L03 (problem + reader invitation) | 600 chars | 250-400 |
| Act-opener concept screens (target 12: L04, L06, L08; max 15: L04, L06, L09, L11) | 340 chars | 200-340 |
| Synthesis (Phase 3 wrap) | 340 chars | 280-450 |
| Principle card (Phase 3 wrap) | (no split — always single card) | 90-200 |
| Assignment + open loop (Phase 3 wrap) | 340 chars | 250-400 |

The 600-char threshold for L01/L03 is intentionally wider than the §6.2 sweet spot — hooks with universal claims sometimes need more setup space than mid-level concept screens, and the renderer accommodates that without splitting. The 400-char threshold for L02 reflects that the hero image takes ~160px of the 600px frame.

**Rule 1 — Hook section caps at 4 cards.** L01 + L02 + L03 produce a maximum of 4 cards total. Per §5.1.4, L02 is the only hook lesson allowed to split. If L01 or L03 exceed 600 chars, the agent flags for trim — it does not split. This preserves the master-claim → protagonist → problem rhythm that defines the level's opening pacing.

**Rule 2 — Minimum content per card.** A rendered card must contain either:
- 2 or more paragraphs, OR
- 1 paragraph of at least 100 characters.

When the renderer's split-point algorithm proposes a Card 1 that violates this rule (typically: lead phrase paragraph alone at ~40 chars), the split point advances to the next paragraph boundary until Card 1 satisfies the minimum. If no valid split point exists (e.g., the body is a single paragraph), the body stays as a single card regardless of length. The lead phrase always travels with at least one body paragraph; it is never a standalone card.

**Rule 3 — No "continued" indicator on Card 2.** Card 2 of a split renders without a chapter label, without a concept title, and without any continuation suffix. The split is signaled visually only — by a subtle green-tinted shadow on the phone frame and a `1/2` / `2/2` caption tag below the phone. Repeating the title on Card 2 reads as a new lesson rather than a continuation; omitting it preserves the visual flow.

**Worked example — Negotiation Beginner Level 1, L04 (Tactical empathy).** Authored body: 565 chars across 3 paragraphs (lead phrase 38 chars + tactical-empathy explanation 393 chars + "most negotiators skip this" closer 134 chars). Threshold for L04 is 340 chars. Initial split point is i=1 (after the lead phrase), but Card 1 with only the 38-char lead phrase violates Rule 2. Split point advances to i=2: Card 1 = lead phrase + tactical-empathy explanation (~432 chars, 2 paragraphs ≥ 100 chars), Card 2 = the closer (134 chars, 1 paragraph ≥ 100 chars). Both cards satisfy the minimum content rule. Both render with the lead phrase on Card 1 only.

#### 6.8.7 Visual treatment of split cards (NEW in vG.3)

When a concept screen renders as 2 cards, the renderer applies these rules element-by-element:

| Element | Card 1 | Card 2 |
|---|---|---|
| Chapter label | Shown if authored | Not shown |
| Concept title | Shown (full size) | Not shown |
| Lead phrase | Wrapped in Primary Tint span on first paragraph | Not applied |
| Hero image | Shown if authored | Not shown |
| Variant background (sage / terracotta) | Applied | Not applied (Card 2 = plain white) |
| Body paragraphs | Card 1's paragraphs | Card 2's paragraphs |
| Continue CTA | Shown | Shown |
| Phone frame shadow | Subtle green-tinted (`split-card-1`) | Subtle green-tinted (`split-card-2`) |
| Caption tag | `<span class="split-tag">1/2</span>` | `<span class="split-tag">2/2</span>` |
| Progress bar | Same percentage as Card 2 | Same percentage as Card 1 |

Card 2 is plain white — the sage / terracotta variant background appears only on Card 1. This avoids visually doubling the variant signal and keeps Card 2 reading as continuation rather than a new evidence/warning card. Single progress increment per lesson regardless of split (Card 1 and Card 2 of L04 both show the same progress percentage).

#### 6.8.8 Renderer reference

The reference renderer that implements §6.8.1 through §6.8.7 lives at `/home/claude/render_mockup.py`. Single-file Python, no dependencies beyond the standard library. Constants at the top of the file:

```
VG3_CAP = 340           # default cap for concept screens (act openers + synthesis screen)
VG3_HOOK_CAP = 600      # hook cap when no hero image (L01, L03)
VG3_HOOK_HERO_CAP = 400 # hook cap when hero image present (L02)
VG3_MIN_CARD_CHARS = 100  # Card 1 must reach this if it has only 1 paragraph
```

Update these constants if vG.3 thresholds finalize differently. The split logic (`split_for_cards()`) and the visual treatment (`render_concept_card()`) are tightly scoped — changing thresholds is a four-line edit.

### 6.8X Multi-select MCQ (TO BE BUILT — new in vG.1)

**Status:** `to_be_built` per HR-29. The schema reserves the type. Agents do not produce these yet. When the visual layer ships, this spec is the contract.

**Used in:** Phase 2 graded lessons (planned). Acts as a discrimination check across multiple correct cases — can the reader recognize all cases of a concept, not just the strongest?

**Structural spec:**

| Field | Type | Length | Notes |
|---|---|---|---|
| `hook_line` | string | 30-80 chars | Required |
| `title` | string | 70-120 chars | The question stem; should clearly indicate multi-select via wording |
| `options` | array of 4-6 | each option `text` 30-110 chars | Four to six options, parallel grammatical structure |
| `correct_indices` | array of integers | length ≥ 2, < total options | Indices of correct options. Multiple correct, at least one wrong. |
| `explanation_title` | string | 3-25 chars | |
| `explanation_body` | string | 130-220 chars | Why each correct option is correct AND why the wrong ones miss; addresses both sides. |
| `cognitive_operation` | enum | one of 8 | Typically Op 2 (Classify), Op 7 (Compare), or Op 8 (Identify missing) |

**Parallelism:** All options use parallel grammatical structure (e.g., all start with "The person who..." or "A buyer that..."). Length ratio max-min ≤ 2.5.

**Validation rules to be enforced:**
- ≥ 2 correct indices
- ≥ 1 wrong option (correct_indices length < options length)
- Indices unique
- Parallel grammatical structure across options

**Use case.** Tests reader's ability to recognize ALL cases of a concept simultaneously, not just pick the single strongest signal. Higher cognitive load than MCQ; lower than match-the-statement (no discrimination across categories).

### 6.9 Cognitive operations roster

Eight cognitive operations are available for graded lessons. Each graded lesson is tagged with one operation in `cognitive_operation`.

| Op | Name | What the lesson tests |
|---|---|---|
| Op 1 | Pick the strongest signal | Among multiple options, which one most clearly indicates the concept? |
| Op 2 | Classify into taxonomy | Which category does this case belong to? |
| Op 3 | Diagnose what is wrong | What is the failure mode in this scenario? |
| Op 4 | Choose the best next step | Given the situation, what is the right move? |
| Op 5 | Predict the outcome | What will happen if X is done? |
| Op 6 | Apply principle to a new case | Given a concept, apply it to an unfamiliar situation. |
| Op 7 | Compare two options | Which of these two is better, and why? |
| Op 8 | Identify what is missing | What information or step is absent from this case? |

**Distribution rule.** Across the graded set of the level, no single op is used more than twice. For L2-L10 at target 12 (3 graded), each op appears once and at least 3 different ops are used. At max 15 (5 graded), at least 4 different ops are used, with no op repeated more than twice. For L1 (5 graded), the locked sequence is Op 1 → Op 3 → Op 5 → Op 4 → Op 5 (Op 5 twice; all other ops within the cap). This forces variety in cognitive demands.

**First-graded-of-act rule.** The first graded lesson of each act uses Op 1 or Op 4. These ops are the most accessible — they re-engage the reader after a concept screen.

---

### 6.10 Word count discipline (NEW in vG.4-May-12 · enforced by HR-33)

Per-screen-type word caps. Every agent that emits copy enforces these on draft, not just at review. Hard caps are non-negotiable; targets are the band the agent aims for.

| Screen type | Target | Hard cap | Exception |
|---|---|---|---|
| Concept card body (`concept_explanation`) | 50-90 words | 110 words | L02 protagonist intro: exempt (load-bearing scene); see §11.7 Lena cluster note |
| Principle card body (Phase 3 wrap, second screen) | 30-60 words | 80 words | None |
| Open loop body (Phase 3 wrap, final screen) | 50-80 words | 100 words | None |
| Graded question / scenario / statement | 30-70 words | 90 words | Optional 12-word scene-setter as leading clause (per §6.12) |
| Graded after-wrong body | 40-70 words | 90 words | None |
| Option text (per option) | 8-25 words | 35 words | None |

**Why these caps.** vG.3 allowed concept bodies up to ~150 words; real-world reading time crept toward 6 minutes per level. The May 12 Arman decision pulled the target into 3:30-4:30 min, which translates to ~250 words/min × 4 min ≈ 1000 words per level. With 13.8 average screens, the per-screen budget lands at ~70-72 words for concept bodies. The targets above pull the mean toward 70.

**L02 protagonist intro exemption.** L02 carries the character setup for the entire cluster. Stripping it too far loses the anchor the rest of the cluster references. L02 may exceed the 110-word cap on the rare cluster where a reviewer flags that the cap forces a meaningful narrative cut. The exemption is documented in the decision log per §4.10; it is not a free pass.

**Enforcement.** The LXD agent and Path Skills Builder agent both run word-count checks at draft time. Validator V30 (Georgy queue) enforces at review time. A screen over hard cap is blocking; over target is a warning the agent must respond to (either revise or document the exception in the decision log).

### 6.11 Consecutive concept card image rule (NEW in vG.4-May-12 · enforced by HR-34)

When two or more concept cards (concept / principle / open loop screens) appear consecutively in a level without a graded screen interleave, **every screen in the sequence carries an `image_brief` field**. The two canonical sequences:

- **Hook trio** (L01 universal claim + L02 protagonist intro + L03 problem / reader invitation): 3 images required.
- **Wrap pair** (Phase 3 principle screen + final open-loop screen, regardless of absolute lesson number): 2 images required.

Other consecutive concept sequences trigger the rule too — for example, if an L2-L10 level designs an "optional fourth angle" concept screen following the L12 graded resolution, that's two consecutive concept screens, so both need image briefs. The agent runs this check at draft time and emits `[IMAGE NEEDED — describe in vG.4 image_brief format]` placeholders if a brief is missing.

**Why this rule.** vG.3 was silent on image cadence. Two text-only screens back-to-back was the most common failure mode in shipped content — the reader's attention dropped, the second screen failed to register, the lesson's coherence broke. Phase 1 hook particularly suffers: three text-only concept screens in a row diluted the master claim's punch. The new rule treats Phase 1 as a 3-image visual mini-arc (universal claim image → protagonist image → problem-state image) and Phase 3 as a 2-image visual closure (principle illustration → open-loop preview).

**Path-wide image count change.** Before vG.4-May-12: 11 image briefs per path (1 protagonist intro per cluster × 3 clusters × 1 path + scattered flashbacks). After: ~42 image briefs per path (3 hook + 1 flashback + 2 wrap = 6 per level × 9 levels with cluster sharing reducing the literal 54 to ~42 unique briefs). Image volume grows ~4x. AI image generation (decision 3) absorbs the volume; Bana's role pivots to cultural-fit + visual-coherence review.

### 6.12 One headline per screen (NEW in vG.4-May-12 · enforced by HR-35)

Every screen in the path has **exactly one headline component**. The headline is the primary serif-weighted typography block the reader's eye lands on first.

| Screen type | Headline component | Decommissioned in v3.5 |
|---|---|---|
| Concept card | `title` field | — |
| Principle card | `title` field | — |
| Open loop | `title` field | — |
| MCQ | `question` field | `hook_line` field removed |
| Myth Buster | `title` field (the WH framing question) | `hook_line` field removed; `body` renamed to `statement` |
| Scenario (short and long) | `scenario` field (incorporates any leading scene-setter) | `hook_line` field removed |

**WH-question preference for graded headlines.** Where natural, graded headlines open with What / Why / Where / Which / Who / When / How. The L05 canonical example shifts from *"Real demand at the Alserkal pop-up"* (a label) to *"Which response signals real demand?"* (a WH question). At least 70% of graded headlines per level should open with a WH word; below 70% the agent flags for rewrite.

**Scene-setting allowance.** Up to a 12-word leading clause inside the question body is permitted when scene-setting genuinely helps. Hard cap: 12 words before the WH question. Example:

> *"Lena watches four customers at her Alserkal pop-up. Which response signals real demand?"*

The 12-word clause is part of the question body, not a separate component. It does NOT re-introduce `hook_line` by another name; it lives inside the headline field.

**Why this rule.** vG.3 graded screens carried both a `hook_line` field (scene-setter) and a separate question / scenario / statement field. The mockup rendered them concatenated, producing two competing headlines per screen. Readers' eyes bounced between the two without knowing which was the question. The single-headline rule resolves the ambiguity: one typographic block is the headline, period.

**Myth Buster specifics.** The Myth Buster screen retains TWO functional components but ONE headline. The `title` field is the headline (the WH framing question). The `statement` field (renamed from `body` in v3.5 for semantic clarity) is the TRUE / FALSE evaluable text — a functional component, not a duplicate headline. Both render, but only one is in headline typography.

### 6.13 AI image brief format (NEW in vG.4-May-12)

Per the May 12 decision (3), new images are AI-generated through Midjourney / DALL-E / Imagen. The image brief format becomes an explicit AI prompt structure:

```
[Style anchor] · [Subject + setting] · [Lighting + composition] · [Mood + emotional register]
```

**Style anchor** is constant per the path's visual identity. For Entrepreneurship Beginner:

> *Maharat Refined Warmth illustration · warm saffron / rose palette · editorial-photography composition · soft modeling*

**Example brief (L02 protagonist intro, kaftan version):**

> ***Maharat Refined Warmth illustration · editorial-photography composition · soft modeling.*** Lena, 29, at her dining-table-turned-studio in a Dubai apartment. A kaftan in saffron-and-rose hand-painted print hangs on a dress form behind her. Sketches visible on her tablet. ***Evening light, warm tones, shallow depth.*** ***Mood: focused, on the edge of a leap.***

Briefs of this form feed directly into AI image generators with predictable consistency. Bana reviews outputs for cultural-fit and visual-coherence; she does not generate the briefs (the LXD or Path Skills Builder owns the brief) and she does not generate the images (the AI tool does). Her judgment moves to post-generation: does the image read culturally true for Gulf-centric audiences, does it match the cluster's visual signature, does the protagonist read as the persona M11 specifies.

**Cluster-batching for consistency.** Generate images in batches by cluster — all Lena images together, all Rania images together, all Sami images together — so each cluster has internal visual coherence. Switching between protagonists mid-batch produces drift in AI-generated outputs.

**Bana's review queue (revised in vG.4-May-12).** Bana receives the AI-generated images in cluster batches. Her review checks:
1. Cultural fit — does the scene read true for Gulf-centric professionals? (Wardrobe, setting, hand gestures, environmental cues.)
2. Visual coherence with the cluster signature (saffron-and-rose for Lena; cluster-specific signatures for other anchors).
3. Protagonist consistency across the cluster — same face, same age, same approximate styling.
4. Mood match against the brief's emotional register.

Bana's review is the final gate before images enter Strapi. Rejected images go back to the brief author (LXD or Path Skills Builder) for brief revision and regeneration, not to Bana for hand-illustration.

### 6.14 CKEditor inline rich-text formatting standard (NEW in M13 · enforced by HR-39)

Body copy in concept cards and after-wrong explanation screens carries inline rich-text markup that CKEditor renders directly. The bottom `highlight_phrases` list (preserved from M11) is now a reference, not the only source of visual emphasis.

**Formatting tokens (markdown source / HTML output):**

| Token | Markdown | HTML | Use |
|---|---|---|---|
| Bold | `**phrase**` | `<strong>phrase</strong>` | Every phrase in `highlight_phrases`, inline where it appears; after-wrong key takeaway (one per screen) |
| Italic | `*term*` | `<em>term</em>` | Contrasting concept terms (e.g., *admirer* vs *buyer*); foreign or industry terms on first introduction |
| Underscored italic | `_term_` | `<em>term</em>` | Abstract concept words standing alone, used sparingly (1-2 per level, principle card and synthesis only) |

**Where formatting applies:**
- Concept card bodies: bold inline highlights; selective italic on contrast terms; underscored italic in synthesis / principle cards only.
- After-wrong explanation bodies: bold the one key takeaway sentence-fragment; no other markup unless contrast italic is needed.
- Graded screen questions / scenarios / statements: NO inline bold — the headline carries the screen's primary emphasis already.
- Open-loop / assignment bodies: bold the action ask ("List **five things they have in common**").
- Principle cards: bold the principle phrase itself ("**Density beats reach.**"); no contractions per HR-31c.

**Where formatting does NOT apply:**
- Chapter labels (plain text).
- Titles (plain text — the title IS the emphasis).
- Highlight_phrases list at bottom (plain comma-separated reference).
- Options (plain — the correct-answer marker `✓` is the only annotation).
- Image briefs (plain prose for AI prompt input).

**Why this rule.** The L1 template carried highlight_phrases at the bottom only, with no visual emphasis in body text. Readers had no visual anchor inside the prose; the `highlight_phrases` list became a translator-only artifact. Promoting these to inline markup gives the reader a navigational scan path through the body, matches CKEditor's native rendering capability in Strapi, and reduces the gap between markdown source and final rendered output.

**Rendering pipeline.** Markdown bold/italic/underscored-italic translate to CKEditor HTML tags (`<strong>`, `<em>`) on Strapi paste. The `build_strapi_paste_doc.py` script handles the translation. No renderer code change in the Mockup agent — the existing concept-card HTML template already renders bold/italic from its input string.

**Source:** May 12 evening Arman directive: *"body copy in concept cards uses ck editor formatted text with highlighting, italics, bolding, etc and the copy docs outputted need to have this as a rule."*

### 6.15 Plain-language + explainer pattern (NEW in M13 · enforced by HR-38)

Body copy assumes zero domain background in the reader. Two operating rules:

**Rule 1 — Plain-language default.** Banned terms (from §3.8 plain-language reference, now elevated to hard rule via HR-38):

> monetization, productize, validation funnel, customer development, MVP, north-star metric, pivot, traction, go-to-market, TAM, SAM, SOM, value proposition, actionable insights, synergy, iterate, leverage (as verb), unlock (as verb), bandwidth (as availability), align (as verb), socialize (a doc), tee up, ladder up, double-click, deep dive.

Industry-specific jargon for the path's domain is also banned where a plain-language equivalent exists:

| Domain | Banned | Replace with |
|---|---|---|
| Fashion / retail | capsule | first batch (small production run) |
| Fashion / retail | trunk show | styling event (private styling session) |
| Marketing | CAC | cost per customer |
| Marketing | LTV | total customer value over time |
| Finance | EBITDA | profit before interest, taxes, and depreciation |
| Sales | quota | sales target |
| Negotiation | BATNA | best alternative if you walk away |

The replacement list above is illustrative, not exhaustive. The LXD agent at draft time runs the jargon audit per §4.13 and flags any term failing the "would a 22-year-old reader from a non-business background know this immediately" test.

**Rule 2 — Explainer-on-first-use pattern.** Where a technical term is essential and cannot be replaced, an inline explainer is added on first appearance. The pattern:

> *[Term] (short concrete definition, ≤12 words, no further jargon)*

Or where prose flow allows:

> [Term] — [definition phrase, ≤12 words, no further jargon].

**Examples (Entrepreneurship · Intermediate · L3 pricing):**

> Lena needs to know her *gross margin* — the share of each sale left after the cost of making the piece.

> She tallies *cost of goods*: fabric, atelier labor, packaging, freight.

> Her *overhead* — rent, software subscriptions, marketing tools — adds another 1,200 AED per month.

> She'll hit *break-even* (the point where revenue covers all costs) at 60 sales per month.

**Financial-term cluster (mandatory explainers).** The following terms ALWAYS carry an inline explainer on first appearance in any level, regardless of context:

> gross margin, net margin, P&L, profit and loss, cost of goods (COGS), overhead, surplus, payback period, EBITDA, runway, burn rate, break-even, unit economics, contribution margin, cap table, MRR, ARR, churn, gross merchandise value (GMV).

The LXD agent maintains a session-level "first appearance" register across levels — once a term is explained in L3, it does not need re-explanation in L4. But each level's first use of any term in the financial cluster always gets re-explained because levels are designed to be self-contained units of reading.

**Why this rule.** Maharat's audience is 22-35 year old Arabic-speaking professionals across MENA, the majority of whom do not come from formal business or finance training. Assuming zero knowledge protects the reader from the silent-failure mode where a single unexplained term causes them to exit the lesson. The explainer cost (one short phrase) is small; the conversion cost of losing the reader is large.

**Source:** May 12 evening Arman directive: *"make sure when any new definition is used that an explainer is added assume zero knowledge this includes gross margins etc."*

---

## Section 7 — Workflow and stages

### 7.1 Stage 1 — Curriculum design

Run before any lesson copy is drafted. Output: the `curriculum_design` and `expanded_curriculum_design` blocks of the level JSON, plus the concept progression rationale doc.

**Stage 1a — Domain framing.** Identify the path's domain (Entrepreneurship, Productivity, Leadership, etc.). Identify the level's tier (Beginner, Intermediate, Advanced) and number (1, 2, 3). Identify the level's role in the path's arc.

**Stage 1b — Master claim formulation.** Draft the master claim. Validate it against canonical lineage (the agent must be able to cite at least two canonical sources where this claim is taught). Validate it is universal (no protagonist), discipline-specific (rooted in the path), and slightly counter-intuitive.

**Stage 1c — Curriculum design.** Choose the four canonical concepts (c1-c4). Cite canonical lineage for each. Choose the level protagonist (name, city, occupation, signature object, signature moment, internal state at open). Build the in-level retrieval map. Allocate insight density.

**Stage 1d — Concept progression rationale.** Write the 3-paragraph narrative showing how each concept emerges from the previous one through the protagonist's situation. If the rationale reads as four disconnected explanations, return to 1c and rework concept order or the protagonist's situation.

**Stage 1e — Self-review pre-content.** Run the Curriculum Strategist persona (§8.1). Confirm: the four concepts are canonical, in plausible order, and connected through the protagonist. Confirm: the protagonist is concrete, situated, and has a stake in all four concepts.

If 1e passes, lock the curriculum design block. Stage 2 cannot edit it.

### 7.2 Stage 2 — Content drafting

Draft the level (12-15 lessons for L2-L10; 12 for L1). Output: the full `lessons` array of the level JSON.

**Stage 2.0 — Pre-allocation.** For each graded slot (3 at target 12, up to 5 at max 15 for L2-L10; 5 for L1), pre-assign:
- Concept tested (one of c1-c4 per the act it sits in)
- Cognitive operation (one of Op 1-8, respecting first-graded-of-act rule and distribution rule)
- Lesson type (MCQ, Myth Buster, Scenario short/long)
- Title length (for Scenario, short or long)

For each concept slot (3-4 concept openers depending on target; plus Phase 3 wrap screens), pre-assign:
- Hero photo (yes/no — see §6.8.2)
- Card variant (default_white unless variants approved)
- Chapter label (optional, see §3.5.4)
- Highlight phrases (optional, see §3.5.5)

**Stage 2.1 — Phase 1 hook (L01-L03).** Draft three `concept_card_standalone` lessons per §5.1.
- L01 plants the master claim universally — no character on screen, numeric anchor in body.
- L02 introduces the protagonist with full `current_baseline` texture (existing standing, daily rhythm, signature object). Hero photo.
- L03 names the problem with verbatim customer quotes (HR-30) and issues the reader invitation directly.

All three lessons multi-paragraph. Lead phrases come from the catalog in §3.5.1 with the variation rule applied (no move repeated >2x).

**Stage 2.2 — Phase 2 acts.** Draft the acts per §5.3. **At target 12:** 3 acts × (1 opener + 1 graded) = 6 lessons (L04-L09). Each act opens with a concept screen, runs 1 graded retrieval lesson on the act's concept. Act 3's opener carries the resolution / next-experiment turn. **At max 15:** 4 acts × (1 opener + 1 graded), plus 1 extra graded on the strongest-leverage concept = 9 lessons (L04-L12). Act 2 typically carries the protagonist flashback in its concept opener. The first graded lesson of each act uses Op 1 or Op 4 per HR-13c.

**Stage 2.3 — Phase 3 wrap (3 lessons; numbered L10-L12 at target, up to L13-L15 at max).** Draft three `concept_card_standalone` lessons per §5.4:
- **Synthesis screen** (first Phase 3 wrap screen) = replays protagonist's choice
- **Principle card** (second Phase 3 wrap screen) = canonical takeaway (`mini_case_tag: principle_card`)
- **Assignment + open loop** (final Phase 3 wrap screen) = concrete reader assignment paired with next-level teaser

**Stage 2.4 — Quantic narrative pass.** Re-read every screen. For each, verify all four Quantic principles (§3.1-3.4) AND the storytelling craft moves (§3.5). Apply surgical edits where principles or craft moves are violated.

**Stage 2.5 — Senior copywriter pass.** Run all four voice tests (§3.6) on every screen including the contraction test. Run dangling-fragment audit: every sentence ends with grounding (no orphan fragments). Run pronoun-disambiguation audit: every pronoun has a clear single antecedent. Verify italics convention (HR-27): every `_word_` serves one of the three permitted jobs. Verify verbatim quote convention (HR-30): customer evidence uses single quotation marks. Audit lead-phrase variation per §3.5.1 — count moves across the level and rewrite any move repeated more than twice.

### 7.3 Stage 3 — Validation

Run all 22 validators (§10) against the level JSON. Run the validator output table generator. If any validator fails, return to Stage 2 and fix.

### 7.4 Handoff

Bundle the five artifacts (level JSON, validator table, concept progression rationale, decision log, optional mockup). Hand off to the Translation Bot.

### 7.5 Filler test (NEW in vG.4-May-12 · enforces HR-33 word counts + general craft)

After drafting any screen, the agent runs a sentence-by-sentence audit. For each sentence: ***would removing this lose the lesson?*** If no, cut.

**Common filler patterns to flag and cut:**

- **Restating a prior sentence in different words.** Example: *"One is praise. The other is purchase."* restating *"'I love it' is not 'I'll buy it.'"* — one of the two has to go. The first carries the dichotomy concretely; the second is a restatement.
- **Setup that doesn't pay off.** *"Here's what makes X..."* when X follows immediately. The setup line adds nothing the next sentence doesn't deliver.
- **Meta-stems like "What this means is..."** or *"The point is..."* or *"In other words..."* — these signal the reader's about to get the actual content. Cut and start with the content.
- **Repetitive transitional phrases between paragraphs.** *"And so..."*, *"What's more..."*, *"On top of that..."* — each transition consumes a word budget the lesson needs. Use them sparingly; default to no transition.
- **Adjectives that don't add information.** *"absolutely critical"*, *"really important"*, *"very specific"*. The adjective intensifier adds emphasis but no information. Cut or replace with a concrete detail.
- **"In order to..."** when *"to..."* would do.
- **"At the end of the day..."** — almost always cuttable.

**Filler test procedure (per screen):**

1. Read the screen body aloud (or simulated aloud at draft time).
2. For each sentence, ask: would removing this change what the reader learns? If no → cut.
3. For each adjective, ask: does this add information? If no → cut.
4. For each transition phrase between paragraphs, ask: is the transition load-bearing? If no → cut.
5. After the pass, re-check the word count against §6.10. If still over, look for the next densest paragraph and apply the test there.

**Why this rule.** vG.3 had no explicit rule against restatement. Tier 2 reviewers caught filler as craft issues. The May 12 lock promotes it to a draft-time rule: the agent does the filler audit before the screen leaves the agent's hands, not after a human reviewer flags it. This compounds with HR-33 (word counts) — cutting filler is how the agent hits the 50-90 word band for concept bodies.

**Distinction from HR-33 cap enforcement.** HR-33 specifies the word cap; §7.5 specifies HOW to hit it without losing the lesson. An agent that hits the cap by cutting load-bearing content fails the lesson. The filler test ensures cuts come from filler, not from concept clarity.

---

## Section 8 — Self-review protocol

### 8.1 Six review personas

Each persona runs at the end of Stage 2. Each produces a 1-5 score on its specific criteria. Combined average must be ≥ 4.0 across all personas.

| # | Persona | Asks |
|---|---|---|
| 1 | **Curriculum Strategist** | Does the level teach the four canonical concepts in a defensible order? Are the takeaways canonical? Is the retrieval map intact? |
| 2 | **Conversion Strategist** | Does Level 1 hook hard enough that the reader pays for Level 2? Is the open loop irresistible? Is the master claim memorable? |
| 3 | **Audience Advocate** | Does any phrasing patronize, shame, or assume role? Is wellbeing preserved? Is plain language honored throughout? |
| 4 | **Learning Journey Designer** | Does the structure flow? Does each act earn its place? Is the act-rhythm cap respected? Does Phase 3 land? |
| 5 | **UX Content Designer** | Does the rendering pacing work? Are hero photos in the right places? Are concept screens multi-paragraph where they should be? Are lead phrases clean? |
| 6 | **Senior Copywriter** | Three voice tests on every screen. Dangling-fragment audit. Pronoun-disambiguation audit. Inline emphasis used sparingly. |

### 8.2 CEO pass (canonical-principle audit)

After the six personas, the CEO pass verifies HR-12 (Phase 3 takeaways are canonical principles, not agent synthesis). For each takeaway, the agent confirms the canonical lineage citation in the decision log.

### 8.3 Conversion simulation

A reader-journey simulation. The agent walks the level as if a reader, asking at each Phase boundary:
- After Phase 1: Do I want to meet the protagonist?
- After Act 1: Have I learned something I want to test in my own situation?
- After Act 2: Am I genuinely curious what happens next?
- After Act 3 (or Act 4 at max 15): Have I earned the takeaways?
- After Phase 3: Do I want Level 2?

Any "no" triggers a revision pass.

### 8.4 New audits (in-level answerability + concept seamlessness)

**In-level answerability audit (HR-17 enforcement).** For every graded lesson, the agent identifies which concept screen earlier in the level supplies the answer. If no concept screen does, the lesson is rewritten or moved.

**Concept seamlessness check (HR-22 enforcement).** The agent reads the concept progression rationale. For each of the three concept-to-concept transitions, the agent asks: is this a story beat in the protagonist's arc, or a topic shift? If a topic shift, the protagonist's situation needs reworking before the level can ship.

---

## Section 9 — Output specifications

The agent delivers five artifacts at handoff.

### 9.1 Level JSON

Conforming exactly to schema v3.4. Required top-level blocks:
- `level_metadata`
- `curriculum_design`
- `expanded_curriculum_design` (now includes the new `current_baseline` field on `level_protagonist`)
- `lessons` (array of 22)
- `audit_artifacts`

### 9.2 Validator output table

Markdown table. One row per text field across all lessons in the level (12-15 for L2-L10; 12 for L1). Columns: lesson ID, field, length, band, status (OK / OVER / UNDER).

### 9.3 Concept progression rationale doc

Markdown. Master claim + four canonical concepts (named and sourced) + 3-paragraph narrative showing the protagonist's arc through them.

### 9.4 Decision log

Markdown. Documents:
- Protagonist choice (name, city, occupation, current_baseline, why)
- Concept order rationale (why c1 before c2, etc.)
- Cognitive op assignment per graded slot (12 entries)
- Insight density distribution (which lessons surprising/reframed/actionable)
- Card variants used (mostly `default_white` until visual layer ships)
- Chapter labels and highlight phrases used
- Lead-phrase move count across the level (variation rule audit)
- Any rule-bend with explicit justification (rare)

### 9.5 Optional mockup

HTML. Renders all lessons (12-15 for L2-L10; 12 for L1) as phones (default + after-wrong states for graded). Generated only on request.

---

## Section 10 — Validation suite

Twenty-two validators run in Stage 3. All must pass.

| # | Validator | Pass criterion |
|---|---|---|
| 1 | Schema validation | JSON conforms to schema v3.4 |
| 2 | Em-dash sweep | Zero em dashes, en dashes, or triple-hyphens in any text field |
| 3 | Character bands | Every text field within its band per §6 |
| 3b | Hook line bands | 30-80 chars |
| 3c | Image brief bands | 30-200 chars |
| 4 | MCQ parallelism | Length ratio ≤ 2.5; correct not the longest unique |
| 5 | Scenario parallelism | Same as MCQ |
| 6 | MCQ correct distribution | ≤ 50% on any single index across the level |
| 7 | Scenario correct distribution | ≤ 65% on any single index |
| 8 | Myth Buster TRUE present | At least one MB has correct_answer = true |
| 9 | Op diversity | No single op used > 2 times across the graded set (L2-L10: 3 graded at target, up to 5 at max; L1: 5 graded with locked sequence) |
| 10 | First graded of act is Op 1 or Op 4 | True for every act (HR-13c) |
| 11 | Myth Buster character-agnostic | No protagonist references in MB body or title |
| 12 | Single protagonist | Exactly one entry in `level_protagonist`; `current_baseline` present and non-empty; no other named characters anywhere in lesson copy |
| 13 | Concept-before-tested | Every graded lesson's tested concept appears on a prior concept screen |
| 14 | Retrieval ≥ 1 per concept | Each concept tested by ≥ 1 graded lesson (L2-L10 target 12: exactly 1 per concept × 3 concepts; L2-L10 max 15: 1-2 per concept × 4 concepts; L1: 5 graded all testing the single concept) [REVISED in M14 from M13's "≥ 2 graded per concept"] |
| 15 | Phase 1 shape | L01 character-agnostic; L02 introduces protagonist with current_baseline texture; L03 issues reader invitation |
| 16 | Act rhythm cap | ≤ 2 graded consecutive within an act (REVISED in M14 from M13's "≤ 3 graded consecutive"; HR-8's level-wide cap of 5 still applies but is far from binding in the new architecture) |
| 17 | Counts | L2-L10: 12 target (3 concept openers + 3 graded + 3 hook + 3 wrap) to 15 max (4 concept openers + 5 graded + 3 hook + 3 wrap); L1: 12 (2 concept + 5 graded + 3 hook + 2 wrap). Type counts respect distribution targets. [REVISED in M14 from M13's "L2-L10: 18 lessons (8 graded + 10 concept)"] |
| 18 | Zero textbook in L1 | No lesson classified `textbook` in Level 1 of any path |
| 19 | Phase 3 has no graded | Zero graded lessons in `phase_3_wrap` |
| 20 | Last is phase_3_wrap | Final lesson (L12 at target, up to L15 at max for L2-L10; L12 for L1) phase = `phase_3_wrap` [REVISED in M14 from M13's "Final lesson (L22)"] |
| 21 | In-level answerability | Every graded lesson cites a prior concept screen that supplies the answer |
| 22 | Concept seamlessness | Concept progression rationale has 3 paragraphs, each naming a story-beat transition |

The validator output is appended to the validator output table (§9.2).

**Additional Senior-Copywriter audits (Stage 2.5, not validators):**
- Lead-phrase variation: no move from §3.5.1 catalog repeated more than twice
- Verbatim quote convention: customer evidence uses single quotation marks per HR-30
- Contraction default: HR-31 — non-contracted forms only on principle cards or with justification

---

## Section 11 — Worked examples: Entrepreneurship L1 + Negotiation L1

This section is the agent's pattern-match target. When in doubt about how the rules in §1-10 should produce content, refer to this section.

**Two worked examples ship as canonical pattern-matches:**

- **Entrepreneurship · Beginner · Level 1** (detailed below in §11.1-§11.6) — **REWRITTEN in vG.4.** Lena and the Dubai kaftans, demonstrating the 12-screen L1 abbreviated architecture, the one-concept-five-angles structure, the aspiring-entrepreneur protagonist persona, and the transformation-promise open loop. Replaces the vG.2/vG.3 Beirut/bakery version entirely. The Lena cluster canonical state (industry, city, currency, venue palette, visual identity) is locked in §11.8.
- **Negotiation · Beginner · Level 1** (added in vG.3, summarized in §11.8) — Yasmine and the hotel-group retainer renewal, demonstrating high-density tactical content (Voss-flavored), the 2-card split rendering rule (§6.8.6), and the named-counterparty documented exception (Mr. Khalid, per HR-19's revised policy and Appendix C). **Unchanged in vG.4** — Negotiation L1 is on the 22-screen architecture pending L1 reauthoring under the abbreviated form.

The Entrepreneurship example is the default reference for L1 architecture, the aspiring-entrepreneur persona pattern, and Dubai-anchored business numbers. The Negotiation example is the reference for paths where teaching density runs hot.

### 11.1 Master claim

> *Most ideas don't fail because they are bad. They fail because not enough people pay.*

### 11.2 The one canonical concept (L1, vG.4)

L1 carries a single concept taught from five angles. Per HR-23's L1 exception (§2.5), this is the entire concept count for L1; the four-concept structure begins at L2.

| Concept | Plain-language name | Canonical lineage |
|---|---|---|
| c1 | Buyers act, admirers nod | Lean Startup methodology (Eric Ries); customer development (Steve Blank); behavioral economics on stated-vs-revealed preference (Kahneman) |

**The five angles** correspond to the five graded screens:

1. **Angle A — recognize the strongest buying signal** (L05 MCQ, Op 1): Among four customer reactions, the only real signal is the one where money changed hands.
2. **Angle B — diagnose what surveys actually measure** (L06 Myth Buster, Op 3): What people say they would pay is not what they pay; surveys capture intent, demand requires action.
3. **Angle C — predict the launch outcome** (L07 Scenario long, Op 5): Praise without prior buying predicts mixed launch turnout, not sold-out launch.
4. **Angle D — choose the cleaner test setup** (L09 Scenario short, Op 4): A small paid deposit forces a choice that free styling does not.
5. **Angle E — read the pre-order result** (L10 Scenario short, Op 5): Eight paid out of more than twenty is real demand at full price, not soft demand.

The concept compounds: each graded screen tests the same underlying mental model from a different cognitive angle. By L10, the reader has applied the concept five times to five different situations and seen it land in all five.

### 11.3 Concept progression rationale — one concept, five angles (Lena's L1 arc)

Lena enters L1 with more than twenty colleagues and friends raving about her kaftans and zero buyers. The level walks her through five tests of the same idea: words are free, buying costs something, and only the second tells you whether the audience is real.

> *Angle A* — Lena watches four customers react at a friend's pop-up. The cash buyer is the only signal that matters. *Buyers act. Admirers nod.* The concept lands as a recognition pattern.
>
> *Angle B* — A myth buster flips the same idea inside out: surveys feel like demand but aren't. The reader experiences the concept as a diagnostic move. The narrow framing matters per §3.5.11 — *what people say they'd pay overstates what they pay*, not *surveys can't measure demand*.
>
> *Angle C* — A long scenario asks the reader to predict Lena's launch outcome. The concept now applies forward, not just backward. Praise without prior buying predicts mixed launch turnout.
>
> *Angle D* — The flashback to her earlier craft-fair test (88 of 100 kaftans returned unsold) shows the concept's track record in Lena's own past. The reader chooses Lena's next test design: free styling or paid pre-order. The pre-order is cleaner because it forces a buying choice.
>
> *Angle E* — The pre-order test ends Friday. Eight admirers paid; the rest said maybe later. The reader reads this result correctly: eight is a real signal at full price, not soft demand. Lena gives notice on Monday. Arc resolves.

L11 (principle card) crystallizes what the reader has just witnessed five times: *Buyers act. Admirers nod.* L12 (open loop) carries the stakes forward: eight buyers is a signal but not yet a business — L2 teaches how to keep them.

### 11.4 Level protagonist (REWRITTEN in vG.4 — Dubai/kaftans)

| Field | Value |
|---|---|
| name | Lena |
| age | 29 |
| city | Dubai |
| occupation | Marketing manager at a real estate firm |
| current_baseline | Seven years at the same firm. Steady income, a managerial title, and the comfort of a known role. Outside work: six months of nights and weekends designing kaftans in a saffron-and-rose print she painted herself. |
| core_situation | More than twenty colleagues and friends have tried on the kaftans and raved. None has paid. On Monday she gives notice and orders her first production run. Her savings funds the launch. |
| internal_state_at_open | Quietly aware that praise isn't the same as buying, but unable yet to name what the missing signal is. About to bet a year of income on praise. |
| signature_object | The kaftans — saffron-and-rose print, hand-painted by her |
| signature_moment | Saturday afternoon at a friend's pop-up in Alserkal Avenue, kaftans on a rack, watching four customers react |
| currency | AED throughout the cluster |

**Why this protagonist works:**

- **Aspiring, not established** (§4.8 Rule 1). Lena has a corporate job and a side hustle with admirers and zero buyers — the exact empathy target for the L1 learner.
- **Industry passes the no-baseline test** (§4.8 Rule 1). A specific designed product (kaftans in her own print) means readers can't fall back on *"people already buy this kind of thing."* The lesson does its full work.
- **Gulf-centric setting** (§4.8 Rule 2). Dubai is the most aspirational/relatable city for the target audience; the kaftan market there is genuine and the price points work.
- **Currency follows location** (§4.8 Rule 3). AED throughout.
- **Real price points** (§4.8 Rule 4). Designer modest kaftans in Dubai sit at 350-1500 AED entry-to-premium. Lena's signature kaftan locks at 600 AED in L3, floor 400 — credible at that market position.
- **Realistic cadence** (§4.8 Rule 5). Designer-clothing buyers return monthly, not weekly. Lena's L10 trajectory (200 customers at 250K AED annual revenue) is consistent with this cadence.

### 11.5 Phase architecture map — L1 vG.4 (12 lessons, one concept)

| Lesson | Phase | Type | Concept | Op | Notes |
|---|---|---|---|---|---|
| L01 | Phase 1 hook | concept_card | (universal master claim) | — | NO character. Concrete dichotomy: *"'I love it' is not 'I'll buy it.' One is praise. The other is purchase."* |
| L02 | Phase 1 hook | concept_card | (protagonist intro) | — | Hero photo. Lena at her dining table in Dubai. Seven years tenure, six months of kaftan design, more than twenty admirers, zero buyers. Monday she gives notice. |
| L03 | Phase 1 hook | concept_card | (problem + reader invitation) | — | More than twenty admirers. Verbatim phrase: *the best modest pieces they've worn in years.* Reader directly invited. |
| L04 | Phase 2 (Act 1) | concept_card | c1 (angle A intro) | — | *Praise isn't demand.* Lead: *"There's a cleaner signal hiding in plain sight."* Body lands *Buyers act. Admirers nod.* |
| L05 | Phase 2 | MCQ | c1 (angle A test) | Op 1 | First graded — confidence-builder (HR-13c). Hook: Saturday at friend's pop-up in Alserkal Avenue. Four customer reactions; only the cash buyer is real demand. |
| L06 | Phase 2 | Myth Buster | c1 (angle B) | Op 3 | Narrow myth: *"If most people in a survey say they would pay for it, that proves demand"* — FALSE. Per §3.5.11. |
| L07 | Phase 2 | Scenario (long) | c1 (angle C) | Op 5 | Lena planning launch. Predict outcome: mixed turnout, not sold-out. |
| L08 | Phase 2 (Act 2) | concept_card (`mini_case_tag: protagonist_flashback`) | c1 (angle B reinforcement) | — | Flashback: 18 months ago, Dubai craft fair, 100 kaftans, 12 sold by Sunday, 88 returned. Card variant: `evidence_sage`. *Past behavior tells.* |
| L09 | Phase 2 | Scenario (short) | c1 (angle D) | Op 4 | Free styling at friend's boutique vs. pre-order list with small deposit. Pre-order is cleaner. |
| L10 | Phase 2 | Scenario (short) | c1 (angle E — RESOLVES ARC) | Op 5 | Pre-order test closed Friday. 8 paid the deposit out of more than twenty. Read: real demand at full price. Lena gives notice Monday. |
| L11 | Phase 3 | concept_card (`mini_case_tag: principle_card`) | c1 canonical takeaway | — | Title: *What real demand looks like.* Body opens *Buyers act. Admirers nod.* Non-contracted register per HR-31c. Card variant: `principle_gold`. |
| L12 | Phase 3 | concept_card | (open loop) | — | Transformation promise. *Eight buyers is a real signal. It's not yet a business. Lena's about to lose those eight, and most founders do at exactly this moment. Next up: how to find the audience hiding inside your first eight, before they vanish.* No assignment per HR-11. |

**Architecture validation:** 12 lessons total. 7 concept (L01, L02, L03, L04, L08, L11, L12) + 5 graded (L05, L06, L07, L09, L10). Matches §5.5. Hook section L01-L03 produces 4 cards (L02 splits per §6.8.6 hero-image threshold; L01 and L03 fit single-card under the 600-char threshold), satisfying §5.1.4. First graded slot is Op 1 (HR-13c). Op sequence: 1 → 3 → 5 → 4 → 5 (locked).

### 11.6 Sample lesson copy (vG.4 voice, Lena/Dubai cluster)

These are the canonical drafts from the May 11 lock. They demonstrate every craft rule layered in vG.4: concrete titles (§3.5.8), lean distinct paragraphs (§3.5.9), calibrated number specificity (§3.5.10), narrow myth-buster framing (§3.5.11), no overstatement (HR-32), principle card in non-contracted register (HR-31c), and confidence-builder first graded slot (HR-13c).

**L01 (Phase 1 · Universal master claim — NO character):**
- concept_title: *"Why most ideas fail"*
- chapter_label: *"Where most ideas die"*
- concept_explanation:
  > *"Most ideas don't fail the way you think.*
  >
  > *They don't fail because they're bad. They fail because 'I love it' is not 'I'll buy it.' One is praise. The other is purchase.*
  >
  > *Real demand isn't kind words. It's a hand reaching for a wallet."*
- highlight_phrases: ["I love it", "I'll buy it", "hand reaching for a wallet"]

**L02 (Phase 1 · Protagonist intro — hero on, 2-card split per §6.8.6):**
- concept_title: *"Meet Lena"*
- chapter_label: *"Entrepreneurship, Lesson 1"*
- concept_explanation:
  > *"Meet Lena.*
  >
  > *She's 29. She's worked at a marketing firm in Dubai for seven years. For the last six months, she's been designing kaftans in a saffron-and-rose print she painted herself.*
  >
  > *More than twenty colleagues and friends have tried them on and said they love them. Not one has paid. On Monday, she gives notice and orders her first production run."*
- image_brief: *"Photo: Lena at her dining table in a Dubai apartment, evening light. A kaftan in saffron-and-rose tones hangs on a dress form. Sketches visible on her tablet. Mood: focused, on the edge of a leap."*
- highlight_phrases: ["seven years", "more than twenty", "gives notice"]

**L03 (Phase 1 · Her problem + reader invitation):**
- concept_title: *"Lena's puzzle: every yes, zero buyers"*
- chapter_label: *"The puzzle"*
- concept_explanation:
  > *"Here's the puzzle.*
  >
  > *More than twenty people have tried on her kaftans. They've called them the best modest pieces they've worn in years. They've taken photos in them. They've told friends. None of them has bought one.*
  >
  > *Lena's about to invest her savings on the strength of all that praise. Help her see what she's missing before she does."*
- highlight_phrases: ["more than twenty", "all that praise", "none has bought"]

**L04 (Phase 2 · Opens c1 — concrete title per §3.5.8):**
- concept_title: *"Praise isn't demand"*
- chapter_label: *"The signal she's missing"*
- concept_explanation:
  > *"There's a cleaner signal hiding in plain sight.*
  >
  > *Praise costs nothing. A compliment, a thumbs up, a 'I'd wear this every weekend.' All free. Buying costs something. Time, attention, money.*
  >
  > *Buyers act. Admirers nod. So far, Lena has admirers. She hasn't met a buyer yet."*
- highlight_phrases: ["Buyers act", "Admirers nod", "costs nothing"]

**L05 (MCQ · Op 1 confidence-builder per HR-13c · venue: Alserkal Avenue):**
- hook_line: *"A Saturday afternoon at a friend's pop-up in Alserkal Avenue, where Lena's kaftans are on a rack."*
- question: *"Lena watches four customers react to her kaftans that afternoon. Which response signals real demand?"*
- options:
  1. A regular tries one on, says it's stunning, and asks Lena to message her when the next colors drop.
  2. Three friends say they love the prints and would wear them any day.
  3. **A new customer pays cash for one kaftan on the spot.** ✓
  4. Her cousin shares photos online and predicts a sell-out.
- explanation_title: *"Money beats words"*
- explanation_body: *"The new customer paid. That's the only response in this set where real money changed hands. Buyers act. Admirers nod. The other three are polite encouragement, not demand."*

**L06 (Myth Buster · Op 3 · narrow framing per §3.5.11):**
- hook_line: *"Let's bust a common belief about surveys."*
- title: *"Can a survey actually prove demand?"*
- body: *"If most people in a survey say they would pay for it, that proves there's real demand."*
- correct_answer: **FALSE** ✓
- explanation_title: *"Polite isn't paying"*
- explanation_body: *"Surveys capture intent. Demand requires action. The price someone says they'd pay almost always overstates the price they actually pay. Test with a real offer instead."*

**L08 (Phase 2 · Act 2 · protagonist flashback · venue: Dubai craft fair):**
- concept_title: *"What they did, not what they said"*
- chapter_label: *"What people did vs what they said"*
- concept_explanation:
  > *"Lena thinks back.*
  >
  > *18 months ago, she tested an earlier kaftan design the same way. Friends raved. She rented a booth at a Dubai craft fair for the weekend and brought 100 kaftans at full price. 12 sold by Sunday evening. The other 88 went back into boxes.*
  >
  > *The praise was real. The buying was fiction. What people did at that fair told her what they'd do at the launch. What they said didn't."*
- mini_case_tag: `protagonist_flashback`
- card_variant: `evidence_sage`
- highlight_phrases: ["Past behavior", "fiction", "what they did"]
- image_brief: *"Photo: a folded stack of kaftans in saffron-and-rose tones in an open cardboard box at the end of a market day, soft sage-tinted afternoon light. A sales tag is visible. Mood: rueful, instructive."*

**L10 (Scenario short · Op 5 · resolves protagonist arc):**
- hook_line: *"The pre-order test ends Friday."*
- scenario: *"Lena's pre-order list closed Friday: 8 of her admirers paid the deposit. The rest said maybe later. Which read of this is most accurate?"*
- options:
  - **A. Real demand at full price** ✓
  - B. Soft demand, mostly polite
- explanation_title: *"Eight real buyers"*
- explanation_body: *"Eight people paid before launch: eight real buyers, not estimates. The rest were the same group that loved the kaftans but never paid. Lena now has a real signal she didn't have six months ago."*

**L11 (Phase 3 · Principle card · non-contracted register per HR-31c · descriptive title per §3.5.8):**
- concept_title: *"What real demand looks like"*
- card_variant: `principle_gold`
- mini_case_tag: `principle_card`
- concept_explanation:
  > *"Buyers act. Admirers nod.*
  >
  > *Words are free. Demand is what someone is willing to do when something is at stake. The smallest paid commitment is the cleanest demand test there is."*
- highlight_phrases: ["Buyers act", "Admirers nod", "smallest paid commitment"]

**L12 (Phase 3 · Open loop — transformation promise · NO assignment per HR-11):**
- concept_title: *"Try it this week"*
- chapter_label: *"What to do this week"*
- concept_explanation:
  > *"One small assignment before you go.*
  >
  > *Write down five people who've told you they'd buy something you're working on. Ask each one for a small deposit toward the next batch. Watch what happens. The ones who pay are real. The ones who don't are admirers.*
  >
  > *Eight buyers is a real signal. It's not yet a business. Lena's about to lose those eight, and most founders do at exactly this moment. Next up: how to find the audience hiding inside your first eight, before they vanish."*
- highlight_phrases: ["five people", "deposit", "before they vanish"]

**Note on L12 vs HR-11.** The L12 above does carry a small "one assignment" framing, retained from the May 11 lock. This is acceptable because the assignment occupies one paragraph and the transformation-promise open loop occupies a second; the screen reads primarily as an open loop, not primarily as an assignment. Future L1 deliveries may further reduce or remove the assignment framing per HR-11; the Lena cluster represents the transitional form from the vG.3 assignment + open loop to the pure vG.4 transformation promise.

The full 12-lesson drafted copy lives at `/mnt/user-data/uploads/entrepreneurship-beginner-L1-copy_2.md` (May 11 lock) — the canonical Lena L1 deliverable.

### 11.7 Lena cluster canonical state (NEW in vG.4)

These are the locked details for the Entrepreneurship Beginner Tier Lena cluster as of vG.4 (May 11, 2026). The agent treats these as the gold-standard template when authoring future path L1 clusters. Every choice below is the result of explicit iteration with Arman; cluster fields are not free to vary without re-approval.

**Protagonist (single across L1, L2, L3, L10):**
- Name: Lena
- Age: 29 at L1; ~31 at L10 (18 months later)
- City: Dubai
- Occupation: Marketing manager at a real estate firm, seven years tenure (at L1)
- Pre-launch state (L1): More than twenty admirers, zero buyers, six months of weekend designing at her dining table

**Product:**
- Kaftans in a saffron-and-rose print she painted herself
- No "capsule" or "co-ord set" detail in body copy (cut per §3.5.9 lean over decorated)

**L1 outcome:** Pre-order test → 8 paid the deposit, the rest said maybe later. She gives notice Monday.

**L2 outcome:** Maps her 8 buyers to Jumeirah professionals who already buy designer modest. Closes at 60 loyal customers in one neighborhood within six months.

**L3 outcome:** Signature kaftan priced at 600 AED (floor: 400 AED). Friend's suggestion: 300 AED. Mentor's suggestion: 800 AED. Settled by math + audience signal.

**L10 outcome:** 18 months in. 200 customers in Dubai. 250K AED annual revenue. Two employees (production lead + part-time stylist). Three offers arrive: license the prints for 2M AED + 700K AED capital required to scale; plateau at current size; sell the IP for 3M AED. Lena chooses plateau. Three years later: 350K AED/year, four days a week.

**Currency:** AED throughout the cluster.

**Visual signature:** Saffron-and-rose print, hand-painted. This thread compounds across all four cluster levels (§4.9 Rule 5).

**Venue palette** (§4.9 Rule 4):
- **Launch venue:** Alserkal Avenue (L05 pop-up scenario)
- **Flashback venue:** Dubai craft fair (L08 protagonist flashback)
- **Watering hole venue:** Jumeirah cafés (L2 audience-finding)
- **Fork-in-the-road venue:** Al Quoz studio (L2/L3 workspace; L10 offer-arrival)

**Math check (§4.8 closing):**
- L1: 8 customers × 450 AED ≈ 3.6K AED (pre-order deposits, not annual revenue)
- L2: 60 customers × 600 AED × 2 visits/year ≈ 72K AED (consistent with six-month trajectory toward L10)
- L10: 200 customers × 600 AED × ~2 visits/year ≈ 240K AED ≈ stated 250K AED ✓
- The math holds.

**HR rule compliance verified for the cluster:**
- HR-5 L1 exception: 12-screen architecture used at L1 ✓
- HR-11 revised: L1 ends on transformation-promise open loop, no assignment ✓
- HR-13c: First graded slot is Op 1 (MCQ) ✓
- HR-19: Single protagonist (Lena) across L1, L2, L3, L10 ✓
- HR-23 L1 exception: One concept taught from five angles ✓
- HR-31c: Principle card uses non-contracted register ✓
- HR-32: No overstatement (e.g., "most of the people who say the first never say the second" instead of "nobody pays") ✓
- §4.8: Industry passes no-baseline test, Gulf-centric setting, AED currency, real market prices, realistic cadences ✓
- §4.9: Cluster continuity verified across L1, L2, L3, L10 ✓

This cluster is the canonical reference for L1 architecture under vG.4. When authoring a new path's L1 cluster, the agent uses Lena/Dubai/kaftans as the structural template; only the discipline, the protagonist's specific industry, and the specific concept change.

### 11.8 Second worked example — Negotiation · Beginner · Level 1 (NEW in vG.3)

The Negotiation Beginner path's L1 ships as a second canonical pattern-match. It demonstrates the high-density tactical voice (Voss-flavored), the 2-card split rendering for over-cap concept screens, and the named-counterparty documented exception under HR-19's revised policy.

**Master claim.** *Most negotiations turn into fights neither side wanted. The skill that turns a fight into a deal is tactical empathy: understanding the other side fully, without agreeing with them.*

**Protagonist.** Yasmine, 32, runs a six-person creative agency in Dubai specializing in digital marketing for hospitality clients. Four years in business. Her biggest client — a regional hotel group — has been on retainer at 40,000 AED per month since the agency's first year. The relationship is the agency's anchor.

**Named counterparty (HR-19 documented exception, see Appendix C).** Mr. Khalid, head of marketing at the regional hotel group. Speaks in dialogue, pushes back, expresses constraints, and lands the renewal deal at 52,000 AED per month for both brands in the Phase 3 synthesis screen. The counterparty's column is mapped through Yasmine's eyes; he has no internal-reasoning sections of his own.

**The four canonical concepts.**

| Concept | Plain-language name | Canonical lineage |
|---|---|---|
| c1 | Tactical empathy (understand, don't agree) | Hostage negotiation literature; behavioral negotiation research |
| c2 | Mirroring — last 1-3 words, upward inflection | Active-listening discipline; FBI hostage methodology |
| c3 | Three voices — late-night DJ, assertive, accommodator | Communication research on tone-vs-words |
| c4 | Why "winning" loses — relationship survives the deal | Long-tail negotiation outcomes; relational economics |

**Concept progression rationale (Yasmine's arc).**

> *c1 → c2.* Yasmine sees the trap of preparing arguments instead of mapping Mr. Khalid's pressure. Tactical empathy reframes the meeting from a fight she's preparing for to a puzzle she's preparing to read. But empathy alone is one-way work. To surface what Mr. Khalid hasn't said, she needs a move — a way to make him volunteer information without feeling interrogated. The mirror is the move.
>
> *c2 → c3.* Yasmine learns to mirror. The mirror works when the room has the right tempo. If the room is hot, the mirror reads as challenge; if the room is cold, the mirror reads as awkward silence. The mirror is the words; the voice is what carries them. Three voices, three uses. The voice she chooses shapes whether the mirror lands.
>
> *c3 → c4.* Yasmine has tactical empathy, the mirror, the voices. She walks into Tuesday's meeting prepared. Now the question of what "winning" means. The negotiator who wins decisively often loses everything that matters — the next renewal, the referral, the relationship that survives the deal. The fourth concept is the one that turns a tactical win into a strategic win: restraint at the close.

**Phase architecture map (vG.3).** Same 22-lesson architecture as Entrepreneurship L1 (3 + 16 + 3). What's different is the rendering: 9 of the 22 concept screens trigger the 2-card split because their bodies exceed the §6.8.6 threshold for their position. L02 (Meet Yasmine) splits per the L02 hero-image threshold (400 chars). L01 and L03 stay single-card under the 600-char hook threshold. The hook section renders as 4 cards total, satisfying §5.1.4.

**The ship-state.** All 10 levels of the Negotiation Beginner path were rebuilt under vG.3 on 2026-05-08 with Voss-flavored content and the deal-focused Yasmine reframe (agency owner, not promotion seeker). The rebuilt copy lives at `/mnt/user-data/outputs/negotiation-beginner-L{1..10}-copy.md`. The vG.3 mockup for L1 lives at `/mnt/user-data/outputs/negotiation-beginner-L1-vG3-mockup.html` (29 phones, including the L02 hero-split). Cross-file consistency check across all 10 levels passed (62 assertions, see `negotiation-rebuild-log.md` for details).

The L1 mockup is the canonical reference for what vG.3 rendering produces in production.

---

## Appendix A — Rule-bends log and v2(1) implementation map (institutional memory)

This appendix preserves the implementation map from Addendum #1 and Addendum #2 for institutional memory. The contents below are no longer canonical guidance — Sections 1-10 above are canonical. The appendix is reference for understanding *why* the spec evolved.

### A.1 Three sources, one output

The Maharat Skill Path Builder Agent draws from three reference frames:

| Source | What it gave the spec | Now folded into |
|---|---|---|
| Agent vF20 spec | Structure, rules, validators, review pipeline | Sections 1, 2, 7, 8, 10 |
| Quantic learning modules | Narrative craft, voice, callback economy | Section 3 |
| v2(1) prototype (March 2026) | Rendered storytelling moves, multi-paragraph pacing | Section 6.8 |

### A.2 What was reproduced from Quantic into the spec

- Anchor characters with specific, slightly-absurd situations → now: single protagonist with specific situation
- Failure cases before success cases → now: protagonist's prior attempts as flashbacks
- Mentor voice on concept screens → §3.5 three voice tests
- Visual budget of 3-5 main visuals per level → §6.8.2 hero photos

### A.3 What was reproduced from v2(1) via schema

- Hook lines above graded questions → schema field `hook_line`
- Hero photo briefs on transitionary screens → schema field `image_brief`
- Mini-cases as embedded evidence → schema field `mini_case_tag` (now reframed as protagonist-flashback)

### A.4 What was reproduced via rendering convention (no schema change)

- Primary-tinted segue lead phrases → §6.8.3
- Multi-paragraph breathing room → §6.8.1
- Inline emphasis markup → §6.8.5
- Section act taglines that read as story acts → embedded in concept screen authoring

### A.5 Rules retired (vG, vG.1, vG.2)

**Retired in vG:**
- **Three-anchor model.** Replaced by HR-19 single-protagonist rule. Karim and Hala from the prior Entrepreneurship L1 are removed.
- **Mini-case named side characters (round 1).** Replaced by HR-21 protagonist-flashback rule. Yara is removed.
- **Maharat instructor references.** Replaced by HR-16. Toufic Kreidieh and any other platform-figure references are removed.
- **External-knowledge questions.** Replaced by HR-17 in-level answerability rule. The "around 2% conversion" question is removed.
- **Disconnected concept presentation.** Replaced by HR-22 concept seamlessness rule and §4.3 concept progression rationale.

**Retired in vG.1 (then partially superseded in vG.2):**
- **Phase 1 character-agnostic.** Reversed in vG.1 via HR-20 (cold open with character on L01); now further refined in vG.2 (universal hook on L01, character on L02).
- **Bridge phase.** Deprecated. The 3-screen Phase 1 in vG.2 absorbs the bridge's function. Schema retains the enum value for backward compat with vG.0 levels.
- **Concept Card Sequence (4-card universal master-claim setup).** Deprecated. vG.1 / vG.2 use `concept_card_standalone` throughout Phase 1.
- **24-lesson count.** Replaced by 22 lessons in vG.2 (3 + 16 + 3). vG.1's 21-lesson count is also retired.
- **Concept body 90-160 char band.** Widened to 90-450 chars in vG.1 with sweet-spot guidance in §6.2.
- **Mini-case named side characters (round 2).** v2.1's Karim, Yara, Reem, Adnan are explicitly NOT permitted. HR-19 reaffirmed strict.

**Retired in vG.2:**
- **Cold-open with character on L01.** Reversed. The master claim plants universally on L01 before the protagonist enters on L02. The case study walks on stage *after* the puzzle is in the room.
- **Protagonist field structured around tension only.** New required field `current_baseline` captures the existing-success texture; the field structure now forces the baseline-then-tension contrast that gives the level emotional gravity.
- **Act-opener concept-screen sweet spot 180-280 chars.** Widened to 200-340 chars to match v2.1's actual rendered length.
- **Implicit voice register.** Contractions are now explicit default per HR-31. Verbatim customer quotes are now explicitly in single quotation marks per HR-30.

### A.6 Rules vG.2 keeps from earlier specs

- Em-dash sweep (HR-10) — fully retained, with rhythm substitutes catalogued in §3.5.6
- Single protagonist (HR-19) — reaffirmed strict; v2.1 side-character pattern explicitly rejected
- No format invention (the 8 lesson types in §6 are exhaustive — five active, three `to_be_built`)
- Insight density distribution in Level 1 (HR-9)
- Act rhythm cap (HR-8)
- The four Quantic principles (§3.1-§3.4) — unchanged
- The six review personas (§8.1) — unchanged
- The eight cognitive operations (§6.9) — unchanged
- Storytelling craft moves catalog (§3.5) — added in vG.1, extended in vG.2 with §3.5.7 verbatim quotes and the lead-phrase variation rule

### A.7 The order of authority

When two principles collide, this is the resolution order:

1. Hard rules from §2 (always win)
2. Schema constraints from `maharat-level-schema-v3.4.json` (always win over narrative ambition)
3. The locked design system (Direction B "Refined Warmth")
4. Quantic principles from §3.1-§3.4 (apply within everything above)
5. Storytelling craft moves from §3.5 (apply within everything above)
6. Multi-paragraph pacing rule from §6.8.1 (applies within everything above)
7. Worked example from §11 (pattern-match target when above leave room)

### A.8 What this means for future levels

When the agent drafts any level of any path:

1. Always complete Stage 1 fully before drafting any lesson copy — including `current_baseline` and `core_situation` filled before any concept screen is written
2. Always apply the four Quantic principles from §3.1-§3.4
3. Always apply the storytelling craft moves from §3.5 (lead phrases with variation, hook lines, italics convention, verbatim quotes, em-dash substitutes)
4. Always apply the multi-paragraph pacing rule from §6.8.1
5. Always run the four voice tests from §3.6 on every screen, including the contraction test
6. ~~Always populate `hook_line` on graded lessons~~ — **RETIRED IN M13 per HR-35.** The `hook_line` field was removed from MCQ, Myth Buster, and Scenario schemas in v3.5. Any scene-setting is folded into the headline (question / scenario / statement) as a ≤12-word leading clause. (L1's locked Op sequence still permits hook_line on the abbreviated architecture only if §5.5 retains it for L1; for L2-L10 it is forbidden.)
7. Always populate `image_brief` on L02 (protagonist intro) and any protagonist-flashback screen
8. Always include a lead phrase on every concept screen except principle cards (HR-28)
9. Always render verbatim customer quotes in single quotation marks (HR-30)
10. Always default to contractions; non-contracted forms are exceptions, not the rule (HR-31)
11. Never invent a side character with a name beyond the HR-19 documented-exception policy (a single named conduit counterparty per cluster is permitted in disciplines like Negotiation; see §2.4 and Appendix C)
12. Never reference a Maharat instructor or platform figure (HR-16)
13. Never pose a graded question that depends on knowledge not taught earlier in the same level (HR-17)
14. Never break the 22-lesson, three-phase, three-act structure (HR-5)
15. Never use em dashes, en dashes, or triple-hyphens (HR-10)
16. Never use italics outside the three jobs in HR-27
17. Never put the protagonist on L01; L01 is the universal master-claim screen, the protagonist enters on L02 (HR-20)

---

## Appendix B — vG.3 deltas changelog (NEW)

The vG.3 deltas folded into this document supersede `maharat-agent-exec-summary-vG.3-deltas.md`. Three rule additions and one HR revision. All changes are rendering-layer or exception-policy; no field schema changes, no new HR rules, no length sweet spot changes.

| Change | Where it lives now | Notes |
|---|---|---|
| 2-card split rendering (Rule 1: hook 4-card cap) | §5.1.4 + §6.8.6 | Hook L01 + L02 + L03 produce 3 or 4 cards total. L02 is the only hook permitted to split. |
| 2-card split rendering (Rule 2: minimum content per card) | §6.8.6 | Card 1 must have 2+ paragraphs OR 1 paragraph ≥ 100 chars. Lead phrase never travels alone. |
| 2-card split rendering (Rule 3: no continued indicator) | §6.8.6 + §6.8.7 | Card 2 omits chapter label, title, continuation suffix. Visual cues only (shadow + caption tag). |
| HR-19 named-counterparty documented exception | §2.4 + Appendix C | Single named conduit counterparty per cluster permitted, with logged exception. |
| Threshold table consolidation | §6.8.6 | 600/400/600/340 thresholds made explicit per lesson position. |
| Renderer reference | §6.8.8 | `/home/claude/render_mockup.py` constants for tuning thresholds. |
| Second worked example (Negotiation L1) | §11.8 | Voss-flavored, deal-focused Yasmine. Pattern-match for high-density tactical content. |

**What did NOT change in vG.3:**
- HR-1 through HR-31: unchanged.
- Lesson architecture (3 + 16 + 3 = 22): unchanged.
- Field schemas: unchanged.
- Length sweet spots in §6.2: unchanged. Authors still target the same bands.
- Variant catalog: unchanged.
- Wrong-answer pattern, exit-X pattern, transitionary screen rules: unchanged.
- Decision logs and validator outputs: continue per §3 / §9.

---

## Appendix C — Named-counterparty documented exceptions (NEW in vG.3)

Per the HR-19 revision in §2.4, a single named conduit counterparty per cluster may appear in disciplines that require a counterparty whose specific words and pushback the level teaches the reader to read. This appendix logs all approved exceptions across the Maharat Skill Paths catalog. Validator V17 references this appendix when accepting a named non-protagonist actor.

### C.1 Why this policy exists

A negotiation — by definition — happens between two parties. Unlike Entrepreneurship Beginner (where Lena's bakery story is largely her internal reasoning), Negotiation lessons require a counterparty who speaks, pushes back, hesitates, says specific things, and lands or refuses specific deals. The reader needs to see the moves landing on someone real, not a faceless 'the other side.'

Three options were considered before vG.3:

1. **Anonymous counterparty across the path** — 'her client lead,' 'the broker,' 'the procurement head.' Tested in vG.2 drafts; reads as evasive and weakens specificity. Rejected.
2. **Named protagonist on both sides per level** — would require swapping protagonist mid-cluster, breaks HR-19 cleanly. Rejected.
3. **Named counterparty with HR-19 documented exception** — protagonist remains single per cluster; counterparty is named, has a clear conduit role, but does not become a parallel-agent protagonist. **Adopted.**

### C.2 Approved exceptions (Negotiation Beginner)

#### Exception 1 — Mr. Khalid (Yasmine cluster, Negotiation Beginner)

| Field | Value |
|---|---|
| Levels | L1, L2, L3 (live counterparty); L10 (background callback only — same person, no live action) |
| Role | Head of marketing at the regional hotel group; Yasmine's client lead on the retainer |
| Action scope | Speaks in dialogue, pushes back, expresses constraints, lands the renewal deal at 52K AED/month in L3 synthesis |
| Why named | The retainer renewal hinges on his specific quarterly mandate, his bonus structure, his consolidation pressure from HQ. None of these can land in a vague 'the client' frame |
| Why not promoted to protagonist | Yasmine is the negotiator and the reader's surrogate. Mr. Khalid's column is mapped through Yasmine's eyes. We don't see his internal reasoning |
| L10 status | Mentioned three times as part of Yasmine's stable client base 'two years later.' No live dialogue, no live action. Historical anchor only. |

#### Exception 2 — Ms. Hala (Tariq cluster, Negotiation Beginner)

| Field | Value |
|---|---|
| Levels | L4, L5, L6 |
| Role | Procurement lead at the major regional bank; first point of contact for Tariq's pitch |
| Action scope | Speaks in dialogue, asks the 'what's your typical fee' question that triggers the anchor, carries Tariq's package to executives, returns with pushback, surfaces the budget-line workaround in L5 |
| Why named | Calibrated questions and the Ackerman descent require a specific person responding to specific moves. 'The procurement person' loses every concrete moment |
| Why not promoted to protagonist | Tariq is the negotiator. Ms. Hala's role is to deliver the bank's position; we don't enter her internal reasoning |
| L6 note | A second character (the COO) appears in L6's in-person meeting. He's named only by role ('the COO'), not by name. This stays inside HR-19 as a one-scene non-protagonist actor without a name. |

#### Exception 3 — Mr. Faisal (Nadia cluster, Negotiation Beginner)

| Field | Value |
|---|---|
| Levels | L7, L8, L9 |
| Role | Real estate broker representing the seller |
| Action scope | Speaks in dialogue, conveys seller positions, surfaces the 'gun-shy seller' constraint in L8, delivers the Friday reversal, sends the L9 contract draft |
| Why named | The four-kinds-of-no analysis (L8) requires reading specific phrasing from a specific intermediary. 'The broker' would break the ear-to-the-ground reading the level teaches |
| Why not promoted to protagonist | Nadia is the buyer and the negotiator. Mr. Faisal is the conduit between her and the seller; the seller himself is unnamed throughout (the path-map's secondary commitment) |
| Seller note | The actual seller of the apartment is referenced as 'the seller' across all three levels and never named. This preserves HR-19 as much as the named-broker convention allows. |

### C.3 Validator V17 expected behavior

After vG.3, V17 (HR-19 single-protagonist enforcement) accepts a single named non-protagonist actor per cluster, provided:

- The actor's action scope is conduit/counterparty (not parallel protagonist)
- The actor has no internal-reasoning sections in the copy
- The protagonist remains the reader's single surrogate throughout
- The exception is logged in this appendix before the level enters validation

V17 still flags any cluster where a side character has internal reasoning, parallel agency, or appears in 4+ consecutive levels as a co-protagonist.

### C.4 Approval log

| Approver | Role | Status |
|---|---|---|
| Arman | Sign off on HR-19 exception policy | Pending as of 2026-05-08 |
| Gaia | Sign off on documentation completeness | Pending as of 2026-05-08 |
| Bana | Voice-review confirms named counterparties read naturally in Arabic | Pending Stage 2 review |
| Georgy | V17 validator update incorporates the exception | Pending Arman approval |

Once Arman and Gaia approve, this appendix becomes the canonical reference. Future paths needing similar exceptions follow the same template — log the exception, identify why a named counterparty is required, justify why the actor is conduit and not parallel protagonist.

---

## Appendix D — vG.4 changelog

### D.0 vG.4-May-12 update (NEW — the M11 → M12 delta)

Source: `maharat-vG4-v35-agent-contracts-diff.md` (May 12 Arman lock).

| Change | Where it lives now | Source decision |
|---|---|---|
| Schema bumps v3.4 → v3.5 | §9 (Output specifications), §6.13 image brief format | Decision 2 |
| AI-generated images replace hand illustration; Bana pivots to review | §6.13 + Appendix F open items | Decision 3 |
| Per-level reading time target tightens to 3:30-4:30 min | §6.10 word count caps; Narrative agent pacing section | Decision 4 |
| Principle cards carry full illustrations | §6.11 wrap-pair requirement; §11.6 L11 illustration brief | Decision 5 |
| Word count discipline per screen type | §6.10 (new); HR-33 (new) | Decision 4 |
| Consecutive concept cards each require image_brief | §6.11 (new); HR-34 (new) | Decision 5 |
| One headline per screen (graded hook_line decommissioned) | §6.12 (new); HR-35 (new); §9 schema | Decision 6 |
| AI image brief format spec | §6.13 (new) | Decision 3 |
| Filler test promoted to draft-time rule | §7.5 (new) | Diff "Why vG.4 / v3.5" §4 |
| **No filler promoted to hard rule** | **HR-36 (new)** | **Operator directive May 12 (post-diff)** |
| **Mandatory self-review gate promoted to hard rule** | **HR-37 (new)** | **Operator directive May 12 (post-diff)** |
| Schema fragment rewritten for graded lessons | §9 (Output specs); MCQ/Myth/Scenario JSON schemas updated | Decision 6 + §6.12 |
| New validators V30, V31, V32 queued | Appendix F (pending approvals) | Diff §6 |

**Hard-rule numbering note.** Diff doc proposed HR-32 (word counts), HR-33 (image rule), HR-34 (one headline). HR-32 was already taken by "no overstatement" (May 11 lock). Renumbered to HR-33, HR-34, HR-35. Validator names V30/V31/V32 preserved. **Additional HRs HR-36 (no filler) and HR-37 (mandatory self-review gate) were added post-diff per operator directive May 12** — neither was in the diff doc; both promote existing workflow procedures (§7.5 filler test and §8/§4.13 review chain) to hard-rule status. The provenance is flagged in §2 (where the rules live) and in this Appendix D.0 changelog table.

**What did NOT change in vG.4-May-12:**

- L1 abbreviated architecture (12 screens) — unchanged.
- L2-L10 standard architecture (22 screens) — unchanged.
- M11's hard rules HR-1 through HR-32 — unchanged.
- HR-19 documented-exception policy for named counterparties — unchanged.
- §4.8 industry/setting selection rules — unchanged.
- §4.9 cluster continuity rules — unchanged.
- §11.7 Lena cluster canonical state — unchanged in narrative content; the L02 protagonist intro now formally carries the §6.10 exemption.
- §11.8 Negotiation L1 worked example — unchanged.
- Three role-agent contracts (Mockup, LXD, Narrative) at M11 — receive parallel May-12 updates as M12 versions; protocol structure unchanged.
- Six-persona review pipeline (§8) — unchanged structure; the new V30/V31/V32 validators run alongside.
- 2-card split rendering rules (§6.8.6) — unchanged. The L02 hero-image split becomes rare under the new word caps but the rule remains as a safety net.

### D.1 vG.4-May-11 update (the original M11 — preserved for lineage)

The vG.4 deltas folded into this document supersede `maharat-vG_4-production-updates.md` and `maharat-vG4-migration-plan.md`. Source: Lena cluster L1 iteration (May 8-11), Arman ↔ San Skill Paths Review call (May 11), and Arman's Slack feedback across the iteration.

#### D.1.1 What changed in vG.4-May-11

| Change | Where it lives now | Source |
|---|---|---|
| L1 abbreviated architecture (12 screens, 7 concept + 5 graded) | §1.1, §5.5, §4.7 pacing template | Arman + San call, May 11 |
| L1 carries one concept taught from five angles (HR-23 L1 exception) | §2.5 HR-23, §5.5, §11.2 | Arman + San call, May 11 |
| L1's locked graded sequence (Op 1 → 3 → 5 → 4 → 5) | §5.5 | Arman + San call, May 11 |
| L1's resolution lands at L10 (final graded), not principle card | §5.5 | Arman + San call, May 11 |
| HR-11 revised: L1 ends on transformation-promise open loop, no assignment | §2.2 HR-11, §5.5 | Arman directive, May 11 |
| HR-13c (first graded slot is Op 1 or Op 4 confidence-builder) | §2.3 HR-13c, §5.5 | San production rules, May 11 |
| HR-31c (principle card non-contracted register, formalized) | §2.7 HR-31c, §11 worked example | San production rules, May 11 |
| HR-32 (no overstatement or absolutism) | §2.7 HR-32, §3.5.11 | Arman feedback + San production rules |
| Title craft rules (concrete, not aphoristic) | §3.5.8 | Arman feedback, May 11 |
| Body copy craft rules (lean, distinct paragraphs, no redundancy) | §3.5.9 | San production rules, May 11 |
| Number specificity rules (calibrated, no awkward plurals) | §3.5.10 | Lena cluster iteration findings |
| Myth-buster accuracy rules (narrow, not categorical) | §3.5.11 | Lena cluster iteration findings |
| Industry and setting selection rules (no baseline, Gulf-centric, real numbers) | §4.8 | San production rules, May 11 |
| Cluster continuity rules (cascade changes, time-stamps, venue palette, visual threads) | §4.9 | San production rules, May 11 |
| Math check requirement (customer × price × frequency = revenue) | §4.8 closing, §4.10 decision log | San production rules, May 11 |
| Decision log additions (industry rationale, pricing logic, venue palette, math check) | §4.10 | San production rules, May 11 |
| Aspiring-entrepreneur protagonist persona (corporate job + side hustle + zero buyers) | §11.4 (worked example) | Arman feedback, May 11 |
| Worked example rewritten — Lena moves from Beirut/bakery to Dubai/kaftans | §11.1-§11.6 | Lena cluster May 11 lock |
| Lena cluster canonical state locked | §11.7 | Lena cluster May 11 lock |
| Worked example sample copy fully replaced | §11.6 | `entrepreneurship-beginner-L1-copy_2.md` |

### D.2 What did NOT change in vG.4-May-11 (still applies)

- HR-1 through HR-21 (except HR-5 L1 exception, HR-11 revised, HR-13c added) — unchanged.
- HR-22 through HR-31 (except HR-23 L1 exception, HR-31c added) — unchanged.
- HR-32 is new (no overstatement); no other HRs were retired.
- L2-L10 architecture (22 screens, 4 concepts, 3 acts) — unchanged.
- Phase 1 §5.1 (3-screen hook, L01 universal master claim, L02 protagonist, L03 problem) — unchanged.
- §5.2-§5.4 (bridge deprecated; Phase 2 acts; Phase 3 wrap for L2-L10) — unchanged.
- Field schemas — unchanged.
- Lesson type catalogue (§6.1-§6.9) — unchanged.
- 2-card split rendering rules (§6.8.6-§6.8.8) — unchanged; apply to L1 the same way they apply to L2-L10.
- Cognitive operations roster — unchanged.
- Six review personas — unchanged.
- Negotiation worked example (now §11.8) — unchanged content; renumbered from §11.7.
- Appendix C (named-counterparty exceptions) — unchanged.
- Validator suite structure — unchanged at the schema level; individual validators get L1-aware logic per V14 and V17 updates.

### D.3 Validator update implications

| Validator | Latest change | Owner |
|---|---|---|
| V9 (op diversity) | No single op used > 2 times across the graded set [REVISED in M14: graded set is 3 at L2-L10 target, up to 5 at L2-L10 max, 5 at L1] | Georgy |
| V14 (retrieval map count) | L1: single concept tested by 5 graded; L2-L10: ≥ 1 graded per concept (target 12: exactly 1 per concept × 3 concepts; max 15: 1-2 per concept × 4 concepts) [REVISED in M14 from M13's "8 graded across 4 concepts / 2 per concept"; M13 was REVISED from M12_1_'s "12 graded / 3 per concept"] | Georgy |
| V16 (act rhythm cap) | ≤ 2 graded consecutive within an act [REVISED in M14 from M13's "≤ 3 graded consecutive"] | Georgy |
| V17 (lesson count per level) | L1: 12 lessons (5 graded + 7 concept); L2-L10: 12 lessons target (3 graded + 9 concept-equivalent screens), 15 max (5 graded + 10 concept-equivalent screens) [REVISED in M14 from M13's "L2-L10: 18 lessons (8 graded + 10 concept)"; M13 was REVISED from M12_1_'s "22 lessons"] | Georgy |
| V18 (concept count) | L1: 1 concept; L2-L10: 3 concepts default, 4 permitted at max 15 [REVISED in M14 from "L2-L10: 4 concepts"] | Georgy |
| V19 (Phase 3 structure) | L1: 2 screens (principle + open loop); L2-L10: 3 screens (synthesis + principle + assignment) | Georgy |
| V20 (open-loop content + position) | L1: transformation promise, no assignment paired; L2-L10: assignment + open loop paired. Final-lesson position is `phase_3_wrap` regardless of absolute lesson number (L12 at target, L13-L15 at max, L12 for L1) [REVISED in M14 from M13's "Final lesson (L22)"] | Georgy |
| V25 (math check across cluster) | New validator: customer × price × frequency = revenue across L1, L2, L3, L10 | Georgy |
| V33 (markup-presence audit) | NEW in M13: every concept-card body contains at least one `**bold**` inline (matching a highlight_phrase); every after-wrong body contains at least one bolded sentence-fragment. Per HR-39. | Georgy |
| V34 (jargon-without-explainer audit) | NEW in M13: scan body copy for tokens in the financial-term cluster (gross margin, P&L, cost of goods, overhead, surplus, payback, EBITDA, runway, break-even, unit economics) and the §3.8 banned-terms list. Each occurrence in an L's first appearance must have an inline explainer phrase within ±2 sentences. Per HR-38. | Georgy |

The validator updates are scheduled for the agent build sprint following Arman + Hassan approval of this contract.

---

## Appendix E — Open items pending decision (vG.4)

These items were surfaced during the May 8-11 iteration but not locked. They sit as TBD in the current contract and are scoped to the named owner for decision.

| Item | Status | Owner | Notes |
|---|---|---|---|
| Phased concept card delivery (split paragraphs across additive screens beyond the 2-card split in §6.8.6) | Pending UI discussion | Arman + Gab | Arman noted "still quite heavy" on concept cards. The 2-card split (§6.8.6) addresses over-cap content but doesn't address under-cap content that would benefit from breathing room. Decision pending text editor update. |
| Hook line CMS field — exists in agent spec (§3.5.2) but not in CMS | CMS gap | Gaia | Not a contract change; product backlog item. Flag for product team. |
| Decreasing lesson count per level / increasing level count for L2-L10 | Parked | Arman + San | Revisit after L1 conversion testing. No vG.4 change. |
| L1 instructional time cap (5 minutes max) — how is this enforced? Word count proxy? | Needs definition | San | Reading-speed proxy of ~250 words/min; would translate to ~1,250-word cap on L1 total prose. Pending San's locked-in metric. |
| Left-alignment as rendering rule (CMS-enforced or copy-enforced?) | Needs clarification | Gab + Gaia | Arman directive that all copy is left-aligned. Not currently in §6.8 rendering rules. Pending CMS/copy decision. |
| Back navigation button | Out of scope for contract | Gab | Product backlog item. |

---

## Appendix F — Pending approvals (vG.4)

| Document | Approver | Status |
|---|---|---|
| vG.4 L1 abbreviated architecture (§5.5) | Arman | Aligned May 11; awaiting final sign-off |
| vG.4 L1 abbreviated architecture (§5.5) | Hassan | Pending |
| HR-11 revision (no assignment on L1) | Arman | Aligned May 11 |
| HR-11 revision (no assignment on L1) | Hassan | Pending |
| HR-13c, HR-31c, HR-32 new rules | Arman | Aligned May 11 |
| HR-13c, HR-31c, HR-32 new rules | Hassan | Pending |
| §4.8 industry and setting selection rules | Arman | Aligned May 11 |
| §4.9 cluster continuity rules | Arman | Aligned May 11 |
| §11.4 protagonist persona shift to aspiring entrepreneur | Arman | Aligned May 11 |
| §11.7 Lena cluster canonical state | Arman | Aligned May 11 |
| Validator updates (V14, V17, V18, V19, V20, V25) | Georgy + Hassan | Pending vG.4 contract approval |
| L2-L10 12-15 lesson architecture (target 12, max 15) (§1.1, §5, HR-5) | Arman | Aligned May 12 evening |
| L2-L10 12-15 lesson architecture (target 12, max 15) | Hassan | Pending |
| HR-38 (plain language + explainer), HR-39 (inline rich-text markup) | Arman | Aligned May 12 evening |
| HR-38, HR-39 | Hassan | Pending |
| §6.14 CKEditor formatting standard, §6.15 plain-language + explainer pattern | Arman | Aligned May 12 evening |
| §6.14, §6.15 | Hassan | Pending |
| V33 (markup-presence audit), V34 (jargon-without-explainer audit) | Georgy + Hassan | Pending M13 contract approval |

Once Arman, Hassan, Georgy, and Gaia approve the items above, M13 becomes the canonical contract effective for all production runs.

---

*End of Maharat Agent Executive Summary — vG.5 · Schema v3.5 · 2026-05-12 evening · Agent M14 (12-15 lesson L2-L10 + length discipline + visual rhythm + one headline + filler intolerance + rich-text markup + plain-language)*

*Schema companion: `maharat-level-schema-v3.5.json` (v3.4 retired; M13 validator additions V33/V34 pending Georgy + Hassan)*
*Schema migration logs: `maharat-level-schema-v3.2-to-v3.3-changelog.md`, `maharat-level-schema-v3.3-to-v3.4-changelog.md`, `maharat-level-schema-v3.4-to-v3.5-changelog.md` (to be authored by Georgy)*
*Renderer reference: `/home/claude/render_mockup.py` (Mockup Agent vM.3 contract documents the graded-card template change for v3.5 and the 12-15 lesson grid for M14)*
*Worked examples: §11.1-§11.7 (Entrepreneurship L1 — Lena/Dubai/kaftans, vG.4 12-screen architecture, May 11 lock); Entrepreneurship L2 to be re-cascaded under M14 12-lesson architecture (M13 18-screen cascade superseded)*
*Source decision documents: `maharat-vG_4-production-updates.md` (May 11), `maharat-vG4-migration-plan.md` (May 11), `maharat-vG4-v35-agent-contracts-diff.md` (May 12 morning), L2 production session log (May 12 evening — folded in here)*
*Source content deliverables: `entrepreneurship-beginner-L1-copy.md` (vG.6.2 lock — needs CKEditor formatting pass under M13 HR-39), `entrepreneurship-beginner-L2-copy.md` (vL2-M12_3 lock, M13-compliant)*
*Companion role-agent contracts: `maharat-agent-mockup-M13.md`, `maharat-agent-lxd-M13.md`, `maharat-agent-narrative-M13.md`*
*Operational artifacts (not part of the contract): `negotiation-rebuild-log.md`, `mockup-build-log.md`, `negotiation-L6-L8-bana-review-pack.md`*
*Operational artifacts (not part of the contract): `negotiation-rebuild-log.md`, `mockup-build-log.md`, `negotiation-L6-L8-bana-review-pack.md`*
