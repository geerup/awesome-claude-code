# Instructor mining plan: one product pack per instructor

> SUPERSEDED for execution by context/mining-plan-v2.md (regenerated from pilot A
> learnings, 2026-06-04). This file remains as design history; the destination
> mappings here still apply where v2 references them.

Phase 1 of the Drive mining (instructors first, the 00- Maharat folder comes after).
Each instructor is a product: a masterclass (or more), with its own assets, product
specifics, claims, websites, and content. This plan turns each into a self-contained,
reusable pack the engine loads whenever a campaign features that instructor.

Grounded in an actual crawl: the folder roster, Mona Ataya's ONE-LINERS and playlist
questions, Ragheb Alama's product cheatsheets, and the per-instructor Organic and
Research-and-Strategy subfolders.

House rules on everything extracted: no em dashes, no tatweel, Western numerals,
empowering framing, never imply accreditation. The raw Drive content violates several
of these (the sampled docs contain em dashes, Eastern Arabic numerals, and
Levantine colloquial), so extraction always rewrites, never copies through.

---

## 1. The roster (from the Drive)

01 Ragheb Alama, 02 Salam Dakkak, 03 Kosai Khauli, 04 Bassam Fattouh, 05 Rahma Riad,
06 Toufic Kredieh, 07 Sami Al Jaber, 08 Cedric Haddad, 09 Mona Ataya, 10 Elda Choucair,
plus Mo Islam (unnumbered, newer, possibly in production).

Observed variance: newer folders (09, 10, Mo Islam) are rich (one-liners, playlist
questions, organic, research and strategy). Older folders (01 to 06, created Dec 2024)
may be thinner or differently structured (Ragheb Alama carries bilingual product
cheatsheets like Maqamat Made Simple). The pipeline below tolerates this variance:
every pack has the same shape, with gaps marked rather than invented.

## 2. What a per-instructor pack looks like

Two homes, clean separation: facts live in context (single source of truth), generation
aids live in the skill pack.

```
context/instructors/
  _CATALOG.md                     The registry: one row per instructor
  mona-ataya.md                   The fact file (see anatomy below)
  ragheb-alama.md
  ...

skills/instructor-marketing/      Hub skill, mirrors the stream-hub pattern
  SKILL.md                        Routes by instructor + the rules common to all
  mona-ataya/                     One sub-pack per instructor
    SKILL.md                      How to market THIS product
    voice.md                      Register, signature phrases, hook patterns
    templates/                    Distilled one-liner library, organic examples
    evals/evals.json              Pack-specific acceptance checks
  ragheb-alama/
  ...
```

### 2.1 context/instructors/_CATALOG.md (the registry)

One table, one row per instructor:
- slug, name AR, name EN
- domain (entrepreneurship, music, makeup artistry, football, ...)
- products: masterclass title(s) and any playlists or cheatsheet assets
- public status: launched | in production | unconfirmed  <- requires team confirmation,
  folder existence proves production, not permission to market
- pack status: mined | partial | todo
- Drive folder link

This catalog is the executable form of the guardrail "never name instructors publicly
without confirmation": copywriter-ar and creative-director check status here before any
public-facing use. It becomes reads_first for both agents.

### 2.2 context/instructors/<slug>.md (the fact file)

Sections, every fact with a source link and extraction date:
- Bio in two lines (who they are, why they have authority)
- The product: class themes and promises (from playlist questions), structure if known
- Verified claims vs unverified claims. The one-liners embed strong marketing claims
  (raised 60 million dollars while raising 3 kids, founded Mumzworld when regional
  internet penetration was 2 percent, 90 percent of startups fail in year one). These
  are powerful and dangerous: each goes in a claims table with status
  verified (source) | unverified (do not use publicly until confirmed). Copy may only
  use verified rows.
- Assets and surfaces: landing page URL, social handles, video assets, PDF cheatsheets,
  anything a campaign can point at or reuse. The websites the user mentioned live here.
- Audience notes from Research and Strategy (who this product is for, positioning)

### 2.3 skills/instructor-marketing/<slug>/voice.md

Distilled from the one-liners and organic content:
- Register observed in source (the sampled one-liners are Levantine colloquial: بدكم،
  هالإشي، رح علمكن) vs the brand rule (Gulf-familiar MSA). The pack records both and
  defers to the register policy decision (open question 1 below). Until decided, packs
  extract hook patterns, not dialect.
- Signature phrases and beliefs worth quoting (with the claims-table caveat)
- Hook patterns found in this instructor's copy, classified: pain-question opener,
  myth-flip, credential drop, empathy opener, stat shock, direct promise
- What this instructor would never say (tone boundaries)

### 2.4 skills/instructor-marketing/<slug>/SKILL.md

The judgment layer: how to market this product. Target segments and the angle per
segment, which hooks work for which audience, what the class actually delivers (so copy
never overpromises), how this product pairs with others (Skill Paths cross-sell), and
the routing into streams 3, 4, 7 (creative briefs, copy, lifecycle).

### 2.5 templates/ and evals/

- templates/: the one-liner library for this instructor (rewritten to house style,
  classified by hook pattern, source-linked), plus any reusable organic formats and
  product assets (the Maqamat cheatsheet pattern is itself a lead-magnet template).
- evals/evals.json, pack-specific checks:
  1. instructor status in _CATALOG is launched (hard fail otherwise for public assets)
  2. every factual claim matches a verified row in the fact file
  3. themes mentioned exist in the product section (no invented class content)
  4. register matches the decided policy
  5. the standard Arabic checks (Western numerals, no tatweel, no em dashes)
  These run inside the usual gate stack, before arabic-copy-qa and brand-qa.

### 2.6 The hub: skills/instructor-marketing/SKILL.md

Routes a request naming an instructor to the right sub-pack, holds the rules common to
all packs (the claims discipline, the status check, the register policy), and defines
what happens when a campaign features an instructor with no pack yet: stop and flag,
do not improvise from general knowledge.

## 3. The mining pipeline, per instructor

Same five steps as the master plan, specialized:

1. Inventory the folder: list every doc and subfolder into
   references/drive-extraction-log.md. Note: subfolders did not always enumerate via
   the search API in sampling (Research and Strategy returned empty). Where that
   happens, open the folder in the Drive UI or fetch docs by direct link, and record
   what could not be read so gaps are explicit.
2. Extract: read playlist questions (themes), one-liners (hooks + claims), organic
   (formats), research and strategy (positioning), product docs (assets).
3. Distill into the pack: fact file first (claims table separated into verified vs
   unverified), then voice.md, then SKILL.md, then templates, then evals. Fix house
   style on the way in.
4. Wire: add the row to _CATALOG.md, link the pack from the hub SKILL.md, and confirm
   copywriter-ar and creative-director list the catalog in reads_first.
5. Verify (human, two checks): Ahmed or the team confirms public status, and someone
   owns claim verification (open question 2). No pack is marked mined until both clear.

## 4. Order of execution

Pilot on two, then batch:
- Pilot A: Mona Ataya (09). Richest sampled folder, exercises every pack section
  including the claims table.
- Pilot B: Ragheb Alama (01). Oldest-style folder plus product cheatsheets, exercises
  the thin-folder path and the asset-template path.

Run both pilots end to end, adjust the pack anatomy from what they teach, then batch
the remaining nine in folder order, newest first (10, Mo Islam, 08, 07, ...), since
newer folders are richer and likelier to feature in upcoming campaigns.

After the pilots, before the batch: 30-minute review with the team on the three open
questions below.

## 5. Open questions (decide after the pilots, before the batch)

1. Register policy: the one-liners are deliberately colloquial Levantine while the
   brand rule is Gulf-familiar MSA. Is instructor-voice colloquial a sanctioned
   exception (the instructor's natural voice), or does everything re-render to brand
   register? Owner: Arman (brand) with Ahmed. The packs are built to support either.
2. Claims verification owner: who confirms biographical and statistical claims before
   they are marked verified? This is a one-time pass per instructor with high reuse value.
3. Folder access: confirm whether the un-enumerable subfolders are a permissions scope
   issue for the connector or genuinely empty, so the extraction log is accurate.

## 6. Deliverables checklist for phase 1

- [ ] context/instructors/_CATALOG.md with all 11 rows (status column pending team)
- [ ] 2 pilot packs complete (Mona Ataya, Ragheb Alama): fact file, voice, SKILL,
      templates, evals
- [ ] skills/instructor-marketing/SKILL.md hub with routing and common rules
- [ ] references/drive-extraction-log.md: instructor section, one table per folder
- [ ] reads_first updates for copywriter-ar and creative-director
- [ ] The three open questions answered and recorded in the catalog header
- [ ] Remaining 9 packs batched after the pilot review

Phase 2 (the 00- Maharat folder) starts after the pilot review, per the master mining
plan (drive-content-mining-plan.md), beginning with 07 Email and WhatsApp Marketing.
