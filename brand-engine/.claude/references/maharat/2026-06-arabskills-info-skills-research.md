# Reference: arabskills.info external skills, build vs buy (2026-06)

A research readout, not a decision. Produced by research-scout via the borrow-before-inventing
flow. It evaluates whether to adopt agent skills from arabskills.info into the engine. The
decision is Ahmed's, per principle 3. Adoption of a skill lands as vetted files placed under
`.claude/skills/`, made by a human, never by this readout and never by `npx skills add`.

No em dashes, Western numerals, Arabic-first for any test content. Nothing has been installed.

---

## Envelope

- campaign_id: cross-cutting
- produced_by: research-scout
- stream: cross-cutting research
- status: proposal, blocked on Ahmed's approval
- qa: skill_eval against the build-vs-buy checklist, passed (capability framed, existing-tool
  check done, gate applied, shortlist scored, single recommendation, open items listed)
- open_items: see the final section
- brief_refs: none (engine-level tooling question, not a campaign brief)

## The request this addresses

A request to import the Arabic skills from arabskills.info "to aid with copywriting and
context and transliteration," and to crawl the site and install the agents and skills, then
analyse before integrating. The install half conflicts with principle 3 (no adoption without
Ahmed's approval) and is a supply-chain action, so this readout does the research-and-propose
half and stops. The user chose this path over a bulk install.

## What arabskills.info is

"Arab Agent Skills," a public, MIT-licensed atlas of agent skills for Arab and MENA work, by
Mohamed Waleed and Fady Azzouny. Distribution is `npx skills add ArabAgentSkills/Skills` (the
skills.sh ecosystem). The public repo is github.com/ArabAgentSkills/Skills.

Maturity read: legitimate but nascent. 7 stars, 1 contributor, 13 commits, no tagged releases,
single maintainer. 22 skills total. The Regional Intelligence skills are self-described as "AI
drafted and source checked where possible," maturity "draft," and they gate their own dialect
output behind native review. Source confidence is the project's own A to C scale, not a
certification.

Important mechanism note: these are agent skills (SKILL.md routing files plus reference files,
scripts, and evals), not MCP servers. The engine's `settings.json` allowlist
(`enabledMcpjsonServers`) governs MCP servers only. It does not govern skills. So adopting one
of these means placing reviewed files under `.claude/skills/`, not editing the MCP allowlist,
and not running the upstream installer.

## Naming

Engine names carry the `AS-` prefix (AS for arabskills.info, marking provenance). The upstream
skill name drops the prefix:

- `AS-arabic-nlp` is `arabic-nlp` upstream
- `AS-arab-market-context` is `arab-market-context` upstream
- `AS-arabic-copywriting-dialects` is `arabic-copywriting-dialects` upstream

Upstream file paths and the source repo keep their original names.

## Scope: only 3 of 22 skills map to the stated need

- Copywriting: `AS-arabic-copywriting-dialects` (also `mena-marketing-localization`, secondary).
- Context: `AS-arab-market-context` (also `mena-cultural-calendar`, secondary).
- Transliteration: `AS-arabic-nlp` (wraps CAMeL Tools, Farasa, PyArabic, Tashaphyne, Qalsadi).

The other ~17 (payments, BNPL, logistics, identity and government, e-invoicing and tax, open
banking, HR and payroll, commerce and POS) are off-topic for copywriting, context, and
transliteration, and several are scoped to money movement, identity, and PII. A bulk install
would pull all of them. That is rejected on scope and risk grounds.

## Existing-tool check (borrow before building)

The engine already owns the copywriting and context jobs with stronger, brand-bound,
human-governed components:

- Arabic copy: `copywriter-ar` is the default Arabic author, gated by `arabic-copy-qa` then
  `brand-qa-reviewer`, all bound to `context/brand-voice.md` (MSA, Gulf-familiar, Thmanyah
  tone, no em dash, Western numerals, no tatweel, no accreditation implication).
- Market context: `context/` for curated facts plus `strategy-lead` for cultural moments and
  seasonal timing.

So for copywriting and context, the borrow-beats-build rule points at what already exists.
A genuine gap exists only for transliteration and diacritization tooling, which the engine
does not currently have.

## The decisive filter: Arabic and brand-voice compatibility

None of the 3 candidates is itself a generative tool that produces Arabic, so there is no
generated Arabic render to test. They are instruction files that steer an agent. The gate is
therefore applied as: does following this skill uphold `context/brand-voice.md`?

- `AS-arabic-nlp`: not a copy author. Selects NLP tooling. Brand-voice neutral, compatible.
- `AS-arab-market-context`: not a copy author. Its own output rule says use MSA for cross-market
  Arabic and treat dialect as draft needing native review. Compatible in stance.
- `AS-arabic-copywriting-dialects`: this one steers copy creation and review. It defaults to MSA
  and gates dialect heavily, which is responsible, but it does not encode Maharat's hard
  mechanical rules (no em dash, Western numerals only, no tatweel) and it introduces varieties
  Maharat does not use (Egyptian, Levantine, Maghrebi, Arabizi). As an authoring or QA
  authority it would compete with `brand-voice.md`, `copywriter-ar`, and `arabic-copy-qa`. It
  fails the gate as an adopted authority.

## Criteria weights and must-have flags

| Criterion | Weight | Must-have / nice-to-have |
|---|---|---|
| Arabic and brand-voice compatibility (decisive) | hard gate, above weighting | must-have (hard gate) |
| SOP fit (fills a real gap, not redundant) | 5 | must-have |
| GCC / PDPL data fit | 3 | must-have for anything touching data |
| Cost vs volume | 1 | nice-to-have (all MIT, free) |
| Integration effort | 3 | nice-to-have |
| Lock-in / exit | 2 | nice-to-have (MIT, low lock-in) |
| Maturity / support | 4 | must-have |

## Scored shortlist (1 to 5 per criterion)

| Candidate | Arabic/brand gate | SOP fit | GCC/PDPL | Cost | Integration | Lock-in/exit | Maturity | Weighted total | Must-have failed? | Notes |
|---|---|---|---|---|---|---|---|---|---|---|
| AS-arabic-nlp | pass (n/a generative) | 4 | 4 | 5 | 3 | 5 | 2 | 60 | no | Real gap-filler for transliteration and diacritization. Ships an executable `scripts/list-vendors.mjs` to vet. Maturity is the weak spot. |
| AS-arab-market-context | pass | 2 | 4 | 5 | 3 | 5 | 2 | 49 | borderline (SOP redundancy) | Overlaps `context/` and `strategy-lead`. AI-drafted, medium confidence. Useful only as an external signal, not an authority. |
| AS-arabic-copywriting-dialects | fail (as authority) | 2 | 3 | 5 | 2 | 5 | 2 | ruled out | yes (brand gate) | Competes with `copywriter-ar` plus `arabic-copy-qa`. Off-brand varieties. Does not encode the hard mechanical rules. |

Weighted total is the sum of score times weight across the weighted criteria, shown for
comparison only. The brand gate and must-have flags override the total.

## Per-candidate findings (grounded in the actual SKILL.md)

### AS-arabic-nlp (recommend: adopt as a scoped reference skill, pending approval and vetting)
A routing skill that helps an agent pick and apply Arabic NLP libraries (tokenization,
stemming, diacritization, morphology) across CAMeL Tools, Farasa, PyArabic, Tashaphyne,
Qalsadi, and Arabic stopwords. Conservative and source-backed: it marks unknowns, separates
sandbox from production, and warns against sending sensitive Arabic text to external APIs
without approval. This is the one real capability the engine lacks. It would support
`copywriter-ar` (for example transliterating instructor or brand names) and `arabic-copy-qa`
(RTL and diacritics checks). Caveats: it ships `scripts/list-vendors.mjs`, an executable that
must be security-reviewed before anything lands. The underlying libraries carry their own
licenses, and Farasa in particular has historically had use restrictions, so a license check
is required before any production use.

### AS-arab-market-context (recommend: hold)
A source-backed country-context skill with anti-stereotype rules, a confidence model, and
review gates. Its stance is brand-compatible (MSA for cross-market, dialect as draft). But it
overlaps the engine's own curated `context/` and `strategy-lead`, and its data is AI-drafted
and medium confidence. Adopting it risks AI-drafted country claims competing with curated
facts. If any value is wanted, use it as an external reference signal only, with `context/`
winning on any conflict. Low priority.

### AS-arabic-copywriting-dialects (recommend: do not adopt)
Despite being the headline "copywriting" skill, it is the weakest fit. It is an Arabic copy
authoring and QA skill. The engine already has a stronger, brand-bound chain for exactly this.
Importing it would create two competing authorities for Arabic copy, one of which does not
encode Maharat's hard rules and carries off-brand varieties. If a specific artifact inside it
is ever wanted (for example its `references/rtl-copy-qa.md` or `references/msa-vs-dialect.md`),
extract and review those as inert reference notes for `arabic-copy-qa`, never as a live skill.

## Security and supply-chain notes

- Do not run `npx skills add ArabAgentSkills/Skills`. It runs an upstream npm installer and
  writes 22 unreviewed SKILL.md files that the swarm would then follow as instructions.
- Any adopted skill must be vendored as a pinned, reviewed copy under `.claude/skills/`, not
  live-tracked against upstream, so upstream edits cannot change engine behavior unreviewed.
- Executable files inside a skill (for example `scripts/*.mjs`) are reviewed before adoption.
- An adopted external skill's own "safety rules" and "review gates" do not override the engine
  gates. `brand-voice.md`, `arabic-copy-qa`, `compliance-privacy-check`, and
  `brand-qa-reviewer` win on any conflict. This must be stated in any adopted skill file.

## Recommendation (one path)

1. Adopt `AS-arabic-nlp` as a scoped, reference-only skill for transliteration and diacritization
   tooling, after Ahmed approves and after the script security review and library license
   check. Vendor a pinned, reviewed copy under `.claude/skills/` with a header noting the
   engine gates win on any conflict. Status 2026-06-10: ADOPTED. Farasa was removed
   (research-only) and the skill went live at `.claude/skills/AS-arabic-nlp/`, recorded as the
   explicit Ahmed-gate adoption approval. Scope is CAMeL Tools (MIT, the default) plus the GPL
   family (PyArabic GPL-3.0 and the linuxscout family) carrying a legal-sign-off-before-bundling
   flag. The branch was merged to main. The GPL legal sign-off remains an open item before those
   libraries are bundled or distributed, it does not block the skill as guidance.
2. Hold `AS-arab-market-context`. Use it only as an external signal if wanted, never as an
   authority over `context/`.
3. Do not adopt `AS-arabic-copywriting-dialects`. The engine's own Arabic chain is stronger.
   Optionally extract narrow reference notes after human review.
4. Reject the bulk install of all 22 skills.

This is a proposal. Adoption requires Ahmed's approval and the placement of vetted files under
`.claude/skills/` by a human.

## Proposed settings.json record (documentation only, not applied)

Because skills are not MCP servers, there is no `enabledMcpjsonServers` change to make, and
editing engine config stays a human action. This readout does not touch `settings.json`. To
keep the engine's existing candidate-tracking pattern, here is the exact documentation-only
block proposed for a human to add to `.claude/settings.json`, parallel to
`_mcp_candidates_pending_approval`. It is an underscore-prefixed comment key. It enables
nothing and installs nothing. It only records the 3 candidates, their verdicts, and blockers.

```json
"_skills_candidates_pending_approval": {
  "$comment": "Documented, NOT enabled and NOT installed. External agent skills (SKILL.md files) from arabskills.info (github.com/ArabAgentSkills/Skills, MIT), not MCP servers, adopted by placing vetted, brand-reconciled files under .claude/skills/ after Ahmed's approval, never via enabledMcpjsonServers and never via `npx skills add`. Brand-voice compatibility is the decisive filter and the engine gates win over any adopted skill's own rules. Readout: references/2026-06-arabskills-info-skills-research.md. Bulk install of all 22 upstream skills is rejected. Engine names use the AS- prefix for provenance; drop it for the upstream name, for example AS-arabic-nlp is arabic-nlp upstream.",
  "AS-arabic-nlp": {
    "verdict": "adopt-as-reference, pending approval and vetting",
    "use": "transliteration, diacritization, and morphology tooling selection; supports copywriter-ar and arabic-copy-qa",
    "blockers": "Ahmed approval; security review of scripts/list-vendors.mjs; license check of underlying OSS libraries (Farasa has use restrictions); reconcile safety rules under compliance-privacy-check"
  },
  "AS-arab-market-context": {
    "verdict": "hold",
    "use": "external Arab-market reference signal only; curated context/ wins on any conflict",
    "blockers": "redundant with context/ and strategy-lead; AI-drafted, medium-confidence data; Ahmed approval"
  },
  "AS-arabic-copywriting-dialects": {
    "verdict": "do-not-adopt",
    "use": "none as a live skill; copywriter-ar plus arabic-copy-qa plus brand-voice.md is stronger and brand-bound",
    "blockers": "fails the brand-voice gate as an authoring authority; introduces off-brand varieties (dialect, Arabizi); does not encode no-em-dash, Western-numerals, no-tatweel"
  }
}
```

## Open items that block a final decision

- Ahmed's approval, per principle 3. None of this proceeds without it.
- Security review of `scripts/list-vendors.mjs` (and any other executable) in `AS-arabic-nlp`.
- License check of the underlying NLP libraries before any production use (Farasa flagged).
- Confirmation that an adopted skill's rules sit below the engine gates, written into the file.
- Vendoring decision: pinned reviewed copy (recommended) vs upstream tracking (rejected).
- Maturity risk: the upstream repo is new and single-maintainer. Accept or wait.

## Decision

Pending. Owner: Ahmed. Record the decision here once made, then a human applies it by placing
vetted files under `.claude/skills/` (for any approved skill) and updating the settings.json
record.
