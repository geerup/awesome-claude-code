# Maharat Skill Paths: Agent system (consolidated)

This folder is the consolidated home for the **Maharat Skill Paths** content-production agent
system: the contracts that govern how one Skill Paths learning **level** is designed, written,
illustrated, and reviewed before it reaches the CMS.

It is a **distinct system from the marketing engine** that lives in the rest of `.claude/`. The
marketing engine takes a campaign brief and produces approval-ready marketing. This system takes a
curriculum slot and produces an approval-ready learning level (Level JSON + validator output +
rationale + decision log + optional mockup). The two systems share a repo and a house style; they
do not share a roster. These files carry no agent frontmatter and are not loaded as marketing
subagents. They are contract documents, read by whoever (human or agent) is producing a level.

> If a Skill Paths request and a marketing-engine rule ever collide, treat them as separate
> stacks: marketing work follows `/.claude/CLAUDE.md`; level-production work follows
> `maharat-agent-M14.md` below.

---

## The four documents and their hierarchy

One canonical authority governs three subordinate role contracts. Every subordinate says, in its
own header: "When this document and M14 collide, M14 wins."

```
                 maharat-agent-M14.md   ......  CANONICAL AUTHORITY (vG.6.1 · Schema v3.5)
                 the level-production contract   HR-1 .. HR-39 · 22 validators · worked examples
                          |
        +-----------------+-----------------+
        |                 |                 |
  maharat-agent-     maharat-agent-    maharat-agent-
   lxd-M14.md        narrative-M14.md   mockup-M14.md
  "The Pedagogue"    "The Storyteller"  "The Visual Editor"
   vL.6              vN.5               vM.6
  LXD / Skill Path   Gamification +     Mockup Creation
   Developer          Narrative Architect Agent
        \                 |                 /
         \                |                /
          +---- shared/comparison-of-notes-protocol.md ----+
            the Section 9 review machinery all three share
```

| File | Role agent | Persona | Lane (gets loud about) |
|---|---|---|---|
| `maharat-agent-M14.md` | (canonical contract, not a persona) | The level-production authority. All hard rules HR-1 to HR-39, the 12-screen / 7-concept / 5-graded architecture, the schema, validators V14 to V35, and the full worked examples. | n/a |
| `maharat-agent-lxd-M14.md` | The Pedagogue | A 100-year educator with zero patience for "engagement theater." | Retrieval practice, cognitive-op progression, HR-13c first-slot difficulty, evidence-to-lineage tracing, math-check coherence, overstatement. |
| `maharat-agent-narrative-M14.md` | The Storyteller | A 100-year narrative craftsperson; the reader's experience is the whole point. | Flat protagonists, missed callbacks, broken cluster bookends, visual-identity drift, gamification cheapening, brand-voice drift, HR-19 named-character discipline. |
| `maharat-agent-mockup-M14.md` | The Visual Editor | A 100-year typographer; reveres white space, hierarchy is mercy. | Typographic violations, color-contrast collapse, whitespace starvation, frame inconsistency, RTL/Arabic rendering, lead-phrase tinting, split-card consistency. |

---

## Read order (for producing a level)

1. `maharat-agent-M14.md`, the contract. Sections 1 to 10 are binding; Section 11 is the worked
   example used as a pattern-match target when the rules leave room for interpretation.
2. The role contract for the stage you are in: `lxd` for design and lesson architecture,
   `narrative` for protagonist and cluster arc, `mockup` for the HTML preview render.
3. `shared/comparison-of-notes-protocol.md`: the loudness scale, tag set, and panel-review format
   used when the three role agents review a deliverable side by side.

The contract's own rule holds across all of them: **if a level being produced does not match
`maharat-agent-M14.md`, the level is wrong, regardless of how good it sounds.**

---

## The production pipeline (from M14 Section 1.3)

The Level JSON feeds a three-bot Slack pipeline into the CMS, with the first human review gate
after upload:

```
Path Skills Builder Bot  ->  Translation Bot  ->  CMS Upload Bot  ->  Strapi (first human gate)
   (produces Level JSON)     (adds Arabic)        (pushes EN + AR)      Lama = QA · Gaia = triage
```

People named across the contracts (for context when reading reviews and decision logs):

- **Arman**: decision owner; the locks (vG.6, M14, HR additions) trace to his directives.
- **Hassan**: co-approver; validator implementation.
- **San / Ahmed ElSanhoury**: alignment partner on architecture and continuity rules.
- **Georgy**: validator owner (V14, V17, and the V30+ queue).
- **Lama**: QA.
- **Gab**: product owner (back-navigation, phased card delivery).
- **Gaia**: Program Director; the operator who reconciles panel reviews and the sole triage owner.
- **Bana**: Arabic voice review and AI-image cultural-fit / visual-coherence review.
- **Makhoul + Shifaa**: React Native frontend; production-render parity (the authoritative render,
  as opposed to the non-authoritative HTML mockup).

---

## Version lineage (current locked state)

| Document | Current version | Schema | Last lock |
|---|---|---|---|
| `maharat-agent-M14.md` | vG.6.1 | v3.5 | 2026-05-15 (HR-10 scope clarification dot-release) |
| `maharat-agent-lxd-M14.md` | vL.6 | v3.5 | 2026-05-15 (Section 4.13 audit chain to 9 audits) |
| `maharat-agent-narrative-M14.md` | vN.5 | v3.5 | 2026-05-12 (L1-mirror lock) |
| `maharat-agent-mockup-M14.md` | vM.6 | v3.5 | 2026-05-15 (multi-paragraph parser mandate) |

The headline architecture as of this lock: every level is **12 lessons, 7 concept + 5 graded**,
phase structure **3 + 7 + 2**. L1 carries one concept from five angles; L2 to L10 carry two
explicit canonical concepts plus a third absorbed into the L11 principle card. Hard rules run
**HR-1 to HR-39**. Em dashes, en dashes, and triple-hyphens are banned on every text field (HR-10).

---

## Companion artifacts referenced but not yet in this repo

The contracts cite several files that are not part of this upload. They are listed here so the gap
is explicit, not silent. None should be invented; each needs to be supplied by its owner.

| Referenced file | What it is | Owner |
|---|---|---|
| `maharat-level-schema-v3.5.json` | The machine-readable form of the M14 contract. Kept 1:1 with the spec. | Georgy / Hassan |
| `render_mockup.py` (cited as `/home/claude/render_mockup.py`) | The Mockup agent's reference renderer (vM.6 multi-paragraph body parser). | Renderer maintainer |
| `maharat-level-schema-*-changelog.md` (v3.2 to v3.5) | Schema delta changelogs cited in the lineage. | Georgy |

---

## Notes on faithful preservation

These four contracts are **locked documents** and are reproduced here byte-faithful to their
uploaded originals. Two consequences worth flagging:

1. **Em dashes appear inside the four contract files.** The marketing engine's house style bans
   them, and the M14 contract itself bans them on level text fields (HR-10). But the contracts'
   own prose narration contains em dashes. They were left untouched to preserve the locked text.
   The files I authored for this consolidation (this README and `shared/comparison-of-notes-protocol.md`)
   follow house style: no em dashes, no en dashes, Western numerals only.
2. **Minor internal staleness exists in the locked sources** (for example, the Mockup contract's
   closing footer still reads "vM.2 · Contract vG.4" while its header is vM.6). These are the
   source documents' own provenance artifacts and were not corrected here, consistent with the
   contracts' culture of flagging rather than silently editing. Correcting them is an owner
   decision (Arman / Georgy), not a consolidation decision.

---

## What this consolidation did

- Brought the four scattered uploads into one self-contained subsystem at `.claude/skill-paths/`.
- Renamed each to the canonical filename its siblings already cross-reference
  (`maharat-agent-M14.md`, `maharat-agent-lxd-M14.md`, `maharat-agent-narrative-M14.md`,
  `maharat-agent-mockup-M14.md`), so every internal `maharat-agent-*.md` reference now resolves
  to a real neighbor file.
- Extracted the triplicated Section 9 review core (loudness scale, tag set, panel-review format)
  into one source of truth at `shared/comparison-of-notes-protocol.md`, leaving each agent's
  role-specific 9.4 to 9.6 in its own contract.
- Added this README as the index: hierarchy, read order, pipeline, lineage, missing companions,
  and preservation notes.

Kept deliberately out of scope (owner decisions, not consolidation decisions): editing any locked
rule text, resolving the schema and renderer companion files, and reconciling the source
documents' internal version-footer staleness.
