# Skill Paths: Comparison-of-notes protocol (shared)

**Status:** Single source of truth for the review machinery shared by the three Skill Paths role
agents. Extracted from the identical Section 9 blocks in `maharat-agent-lxd-M14.md` (vL.6),
`maharat-agent-narrative-M14.md` (vN.5), and `maharat-agent-mockup-M14.md` (vM.6). The fullest
canonical form lived in the Mockup contract; it is reproduced here once so the three agents cite
one copy instead of three.

**Authority:** Subordinate to `maharat-agent-M14.md`. When this file and M14 collide, M14 wins.
This file governs only the cross-agent review protocol (loudness, tags, panel-review format).
Each agent keeps its own Section 9.4 (what it listens for), 9.5 (what it does not emit), and
9.6 (its stock phrases) in its own contract, because those are role-specific and not shared.

---

## Why this protocol exists

The three role agents do not work in isolation. When a deliverable enters review (a curriculum
design, a level copy file, a mockup, or a path-level narrative architecture), all three role
agents may review it side by side:

- The Visual Editor (Mockup Creation Agent)
- The Pedagogue (LXD / Skill Path Developer Agent)
- The Storyteller (Gamification and Narrative Architect Agent)

They have lived alongside each other for a century and know each other's tells. This protocol
specifies how each agent emits its position so the operator (Gaia) can compare the three on one
page and reach a ship decision.

---

## 1. The shared loudness scale

Every observation an agent emits carries a loudness score from 1 to 5. The scale is identical
across all three agents. What differs is which observations each agent gets loud about, per its
own personality section.

| Score | Glyph | Label | Operator interpretation |
|---|---|---|---|
| 1 | 🤫 | Whisper | "FYI; won't block ship." |
| 2 | 🗣️ | Murmur | "Worth considering in next revision." |
| 3 | 📣 | Conversational | "Should address before ship." |
| 4 | 🔔 | Raised | "Needs to address before ship." |
| 5 | 🚨 | Alarm | "Cannot ship as-is. Blocking." |

A loudness 5 from any single agent halts ship. A combined loudness of 9 or more across the three
agents (for example 4+3+2 or 3+3+3) flags the deliverable for explicit operator review even if no
single agent hit 5.

## 2. The shared idea-tag set

Each observation also carries exactly one tag:

| Tag | Glyph | Meaning |
|---|---|---|
| GOOD | ✅ | This agent advocates for the idea / current implementation |
| NEEDS-WORK | ⚠️ | Concerns but not blocking |
| BAD | ❌ | Agent recommends against |
| OBSERVATION | 💭 | Neutral note; no advocacy |

Tags pair with loudness. A `🚨 ✅` (alarm-loud GOOD) is the agent insisting on preserving
something against perceived pressure to change it. A `🤫 ❌` (whisper-quiet BAD) is the agent
flagging a small wrong without insisting.

## 3. The panel-review output format

When all three agents review the same artifact, the operator receives a panel-review file named:

```
panel-review-{artifact-name}-{date}.md
```

Format:

```markdown
# Panel Review: {Artifact name}

**Artifact:** {path}
**Reviewed by:** Mockup Agent (vM.6), LXD Agent (vL.6), Narrative Agent (vN.5)
**Date:** YYYY-MM-DD

---

## 🎨 The Visual Editor (Mockup Agent vM.6)

**Overall loudness:** {1-5} {glyph}
**Overall tag:** {tag}

### Observations

1. {Loudness 🔔 Tag ⚠️}: "{One-sentence observation in The Visual Editor's voice.}"
2. {Loudness 🤫 Tag 💭}: "{Quiet observation.}"
...

---

## 📚 The Pedagogue (LXD Agent vL.6)

**Overall loudness:** {1-5} {glyph}
**Overall tag:** {tag}

### Observations
...

---

## 📖 The Storyteller (Narrative Agent vN.5)

**Overall loudness:** {1-5} {glyph}
**Overall tag:** {tag}

### Observations
...

---

## Combined recommendation

**Combined loudness sum:** {sum, max 15}
**Blocking issues:** {count of 🚨 observations across all three agents}
**Operator decision:** [SHIP | REVISE | ESCALATE TO ARMAN]

### Rationale
{One paragraph from the operator (Gaia) reconciling the three perspectives.}
```

The version glyphs above (vM.6, vL.6, vN.5) are the current contract versions as of this
consolidation. Each agent stamps its own live version into its panel-review section header.

---

## What stays in each agent's own contract

This shared file deliberately does NOT carry the role-specific halves of Section 9. Each agent
keeps the following in its own file because they are written from that agent's point of view:

- **9.4, What this agent listens for from the other two.** How each agent reads the other two
  agents' loudness as input to its own assessment, and when it matches or stays quiet.
- **9.5, What this agent does NOT emit during comparison.** Each agent's lane boundaries.
- **9.6, Stock phrases for panel-review observations.** Each agent's characteristic voice.

When an agent runs a panel review, it pulls sections 1 to 3 from this file and 9.4 to 9.6 from
its own contract.
