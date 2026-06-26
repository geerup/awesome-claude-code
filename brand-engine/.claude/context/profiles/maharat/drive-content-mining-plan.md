# Drive content mining plan: from the Maharat Drive into the engine

> SUPERSEDED for execution by context/mining-plan-v2.md (regenerated from pilot A
> learnings, 2026-06-04). This file remains as design history; the destination
> mappings here still apply where v2 references them.

Source: the shared Drive folder (https://drive.google.com/drive/folders/191DbJxsBrG8Ey29ID8jvO7FYacfmQp_P).
Goal: divide its content into the four asset types the engine runs on: skills, templates,
evals, and context. The Drive stays the source of record; the `.claude/` tree gets
distilled derivatives, never raw dumps.

House rules apply to everything extracted: no em dashes, no tatweel, Western numerals,
empowering framing, Arabic-first, never imply accreditation.

---

## 1. What is in the Drive (inventory from sampling)

Three content families, each feeding the engine differently:

A. Instructor folders (01 Ragheb Alama, 02 Salam Dakkak, 03 Kosai Khauli, 04 Bassam
   Fattouh, 05 Rahma Riad, 06 Toufic Kredieh, 07 Sami Al Jaber, 08 Cedric Haddad,
   09 Mona Ataya, 10 Elda Choucair, plus Mo Islam). Sampled contents per instructor:
   - Playlist questions, bilingual EN + AR (the masterclass themes: confidence, time
     management, scaling, funding, and so on)
   - ONE-LINERS docs: polished Arabic marketing one-liners per class, written in the
     instructor's voice. These are ad-copy and email-copy gold.
   - Organic/ subfolder (organic social content)
   - Research and Strategy/ subfolder (per-instructor positioning work)

B. 00- Maharat: the marketing department archive. Subfolders sampled: 00 Guidelines,
   01 Research, 01 Campaigns, 07 Email/WhatsApp Marketing, 10 PR/Affiliate,
   11 Sponsorships, 12 Lead Gen, 12 Reporting, 13 App and Notifications, 14 Social
   Media, 15 CRM, 16 Paid, 17 Playlists, Growth Hacking, Data, $100M Money Models,
   Canva Migration, Team, Third Party/Agencies, Process/Project Management.

C. Cheat Sheets (Website, Maharat Guides) and Maharat x Read The Room (partnership).

## 2. The sorting rule: which asset type each thing becomes

One question decides where a piece of content goes:

- Is it a stable fact about Maharat, its catalog, or its people? -> context/
- Is it a reusable output format or a worked example to imitate? -> templates/ (inside the owning skill)
- Is it process knowledge, a playbook, or a judgment pattern? -> a skill (SKILL.md)
- Is it an example of known-good (or known-bad) output that defines the quality bar? -> evals/

The same Drive doc can feed more than one. A past campaign email feeds a template (its
structure), an eval (its approved final copy as a golden example), and context (the
offer and result facts it records).

## 3. The mapping, by Drive area

### 3.1 Instructor folders -> the biggest single win

New context file: `context/instructor-catalog.md`
- One entry per instructor: name (AR + EN), domain, masterclass themes (from playlist
  questions), confirmed public status. This directly serves the guardrail "do not name
  instructors publicly without confirmation": the catalog records which instructors are
  launched and publicly marketable vs in production. Verification of each status with
  the team is a step in this plan, not assumed from folder existence.
- Voice notes per instructor distilled from the one-liners: how this person sounds in
  Arabic copy.

New cross-cutting skill: `skills/instructor-voice/`
- SKILL.md: how to write marketing copy in a given instructor's register, grounded in
  the catalog and their one-liners. Used by copywriter-ar and creative-director whenever
  a campaign features an instructor.
- templates/: the ONE-LINERS docs distilled into a one-liner pattern library (hook
  shapes: pain-question, myth-flip, promise, empathy-opener), with 2 to 3 real examples
  each, attributed to their Drive source by link.
- evals/evals.json: checks that instructor copy (a) matches a confirmed-public
  instructor, (b) uses only themes in the catalog, (c) passes the usual Arabic rules.

Feeds existing skills:
- `04-copywriting/ad-copy` and `email-copy` templates/ gain the one-liner pattern library.
- `02-strategy-planning/offer-and-angle` gains the per-instructor Research and Strategy
  positioning as worked examples.

### 3.2 00- Maharat / 00 Guidelines -> context and eval criteria

- Distill into `context/brand-voice.md` (enrich, do not replace): any tone, formatting,
  or visual rules in the official guidelines that the current file lacks. Where the
  Drive guidelines conflict with the current brand rules, flag for Ahmed/Arman rather
  than silently overwriting (Arman owns brand decisions).
- The same rules become assertions in `arabic-copy-qa/evals` and
  `brand-qa-reviewer` checks, so the official guideline is executable, not just readable.

### 3.3 00- Maharat / 01 Campaigns + 01 Research -> skills and learnings

- Past campaign docs -> `skills/09-reporting-learning/learnings-log/templates/`: each
  past campaign distilled to a one-page precedent (objective, audience, offer, channel,
  what happened, what to reuse). These seed the learnings log the engine was going to
  build from zero.
- Research docs -> `context/market-research-digest.md`: stable findings about the
  audience and market worth keeping (only conclusions that are still current; date-stamp
  everything extracted).

### 3.4 00- Maharat / 07 Email + WhatsApp Marketing -> the first build's fuel

Highest priority area, it feeds the candidate first build (non-payer email flow):
- Real past emails -> `04-copywriting/email-copy/templates/` (structure) and
  `evals/` golden examples (approved final copy = the quality bar made concrete).
- Any segmentation or flow logic docs -> `07-lifecycle-messaging/segmentation-logic`
  and `nonpayer-email-flow` templates.
- Any platform usage notes may NAME THE INCUMBENT email/WhatsApp platform, the open
  item blocking the platform decision. Extracting that name is a deliverable of this
  plan, not a side effect.

### 3.5 00- Maharat / 16 Paid, 12 Lead Gen, 14 Social, 13 App and Notifications

- Paid -> `05-build-launch/paid-campaign-build/templates/`: past ad structures, naming
  conventions, audience setups as worked examples.
- Lead Gen -> `06-conversion-path/landing-page` and `02-strategy-planning` templates:
  past lead magnets (the PDF guides) and gate setups.
- Social -> `03-creative-production` templates: organic formats that worked.
- App and Notifications -> a future `07-lifecycle-messaging/push-notifications` sub-skill
  (todo, only if push becomes a campaign channel).

### 3.6 00- Maharat / 12 Reporting + Data -> reporting skill

- Past reports -> `09-reporting-learning/campaign-report/templates/`: the report format
  the team already reads, so the engine's reports look familiar.
- Metric definitions in Data -> `context/metrics-glossary.md`: what the team means by
  each KPI, so analytics-reporter uses house definitions.

### 3.7 $100M Money Models + Growth Hacking -> offer and experiment skills

- Offer frameworks -> `02-strategy-planning/offer-and-angle/templates/`: distilled
  framework summaries (own words, no reproduced book content), as thinking aids.
- Growth experiments -> `08-monitoring-optimization/ab-test-plan/templates/`: past
  experiment formats and any results worth keeping as precedents.

### 3.8 Cheat Sheets (Website, Maharat Guides) -> context

- Website cheat sheet -> `context/website-map.md`: pages, URLs, gate locations. The
  conversion-engineer needs this to wire paths without guessing.
- Maharat Guides -> `context/lead-magnet-catalog.md`: the PDF guides that exist, for
  lead-gen campaigns to reference real assets instead of inventing them.

### 3.9 Out of scope for now

- Sponsorships, PR/Affiliate, Team, Third Party/Agencies, Process/PM, Canva Migration:
  not part of the 9 campaign streams (and B2B/enterprise is parked per the board).
  Inventory them in the extraction log but extract nothing yet.
- Maharat x Read The Room: partnership content, same treatment.

## 4. How the extraction runs (the pipeline)

Run per Drive area, in priority order: 3.4 email (first build fuel), 3.1 instructors,
3.2 guidelines, 3.3 campaigns and research, then the rest.

1. Inventory. List the area's files with links into `references/drive-extraction-log.md`
   (one table per area: file, type, destination, status). This log is the bridge between
   Drive and the scaffold and prevents double-extraction.
2. Extract. Read the docs (google_drive_fetch). Pull facts, patterns, examples.
3. Distill. Rewrite into the destination format. Rules:
   - Context files state facts with a source link and an extraction date.
   - Templates carry structure plus 2 to 3 real examples, each linked to its source doc.
   - Evals encode the quality bar as concrete checks, with golden examples copied in.
   - Skills describe the judgment pattern, citing the precedent docs.
   - Everything passes the house style on the way in (the Drive content itself may
     contain em dashes or Eastern numerals; fix on extraction, never propagate).
4. Wire. Add the new files to the owning skill or context, update `_AGENTS-INDEX.md`
   reads_first where a new context file becomes mandatory reading (the instructor
   catalog becomes reads_first for copywriter-ar and creative-director).
5. Verify. Two human checks at the gate:
   - Ahmed/team confirm the instructor-catalog public statuses (guardrail).
   - Arman confirms any brand-guideline deltas before brand-voice.md changes.

## 5. Sensitivities and guardrails for this extraction

- Instructor names: extraction puts them in internal context only. Public use still
  requires the confirmed-status flag in the catalog. The folders prove production, not
  permission to market.
- Dialect note: the sampled one-liners and playlist questions lean Levantine colloquial
  (بدكم، هالإشي، عم), while the brand rule is MSA with Gulf-familiar wording. Do not
  treat the one-liners as voice-canon. Extract their hook patterns and energy, flag the
  register mismatch in the instructor-voice skill, and let copywriter-ar re-render in
  brand register. This mismatch is itself a finding to confirm with the team: is
  instructor-voice colloquial a deliberate exception to MSA?
- No accreditation claims, no roadmap or unannounced content: if a Drive doc references
  unlaunched plans, it stays out of context files.
- Third-party frameworks ($100M Money Models): distill ideas in our own words, link, do
  not reproduce the source material.
- Personal data: if any doc in CRM or Data contains contact-level data, never copy it
  into the scaffold; reference the system that holds it.

## 6. Deliverables checklist

Context (new or enriched):
- [ ] context/instructor-catalog.md (with confirmed-status column, pending team check)
- [ ] context/market-research-digest.md
- [ ] context/metrics-glossary.md
- [ ] context/website-map.md
- [ ] context/lead-magnet-catalog.md
- [ ] context/brand-voice.md enrichment (pending Arman on deltas)

Skills (new):
- [ ] skills/instructor-voice/ (SKILL.md + templates + evals)

Templates (into existing skills):
- [ ] 04-copywriting: one-liner pattern library, real email examples
- [ ] 02-strategy-planning: instructor positioning examples, offer frameworks
- [ ] 05-build-launch: past paid structures
- [ ] 06-conversion-path: lead magnet and gate examples
- [ ] 07-lifecycle-messaging: past flow logic
- [ ] 09-reporting-learning: campaign precedents, report format

Evals (enriched):
- [ ] arabic-copy-qa: guideline rules as assertions
- [ ] 04-copywriting evals: golden examples from approved past emails
- [ ] instructor-voice evals: catalog-bound checks

Open items this extraction may close:
- [ ] The incumbent email/WhatsApp platform name (look in 07 Email/WhatsApp Marketing)
- [ ] The full marketing brand kit beyond the three visual constants (look in 00 Guidelines)

Log:
- [ ] references/drive-extraction-log.md (running, one table per area)
