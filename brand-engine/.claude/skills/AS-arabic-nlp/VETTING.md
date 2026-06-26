# Vetting: AS-arabic-nlp

Status: ADOPTED and live as of 2026-06-10, recorded as the Ahmed-gate adoption approval.
No em dashes, Western numerals.

## Pin

- Upstream: github.com/ArabAgentSkills/Skills, path `skills/arabic-nlp`.
- Commit: add86a278341568232c3fdac97caf01c0824dc5d.
- Fetched: 2026-06-10. Upstream repo license: MIT.
- This copy is reconciled, not byte-identical. The canonical bytes are at the pinned commit.
  Re-vet on any upstream bump (new SHA).

## Files reviewed at the pin

- `SKILL.md` (reconciled into `./SKILL.md`).
- `sources.yml` (transcribed into `./sources.yml`, Farasa removed).
- `vendors/{arabic-stopwords,camel-tools,farasa,pyarabic,qalsadi,tashaphyne}.md` (distilled
  into `./vendors.md`, Farasa removed).
- `references/integration-checklist.md` (copied into `./references/`).
- `evals/prompts.yml` (copied into `./evals/`, Farasa reference removed).
- `examples/source-backed-answer.md` (copied into `./examples/`).
- `scripts/list-vendors.mjs` (reviewed, then dropped, see Security review).

## Security review

- `scripts/list-vendors.mjs`: a read-only Node script. It reads one local JSON
  (`../../../data/processed/vendors.json`) and prints vendor rows to stdout. No network, no
  `child_process`, `exec`, `spawn`, or `eval`, no filesystem writes, no environment or secret
  access. Verdict: benign. It is also non-functional in the public export, because
  `data/processed/vendors.json` is not shipped publicly. Decision: dropped from this copy.
  Maharat does not execute third-party scripts, and the `SKILL.md` reads `sources.yml` directly.
- No other executable or network-calling code. The reference, vendor, and eval files are inert
  markdown and YAML.

## License findings (primary sources, confirmed)

The skill points at external libraries. Their licenses, not the skill's MIT, govern any use of
the libraries themselves.

- CAMeL Tools: MIT (NYU Abu Dhabi, 2018 to 2026). Confirmed at github.com/CAMeL-Lab/camel_tools,
  file LICENSE. Commercial-safe. The default for anything Maharat ships.
- PyArabic: GPL-3.0. Confirmed at github.com/linuxscout/pyarabic, file LICENSE. Copyleft.
- Tashaphyne, Qalsadi, Arabic Stopwords: same author family (linuxscout). Historically GPL.
  Treat as GPL until each LICENSE is confirmed individually.
- Farasa: research-only. The QCRI site states the FARASA package is made public for research
  purpose only, and non-research use requires contacting QCRI. Confirmed at farasa.qcri.org.
  Removed from this skill before adoption.

Implication: the skill defaults to CAMeL Tools, which is commercial-safe. The GPL family is
usable but copyleft, so prefer running it as a separate preprocessing process and get legal
sign-off before bundling or distributing. This is not legal advice. Legal confirms before
those libraries are used in production.

## Quality note

The upstream vendor files are templated from the payments atlas and carry sections that do not
apply to NLP libraries (Auth model, Webhooks, Refunds, Recurring and tokenization, Currencies),
with most fields marked "Unknown from public docs." They are leads, not authoritative facts.
The distilled `vendors.md` keeps only the useful, source-backed fields and adds the license
column.

## Reconciliation (diff vs upstream)

- Renamed to `AS-arabic-nlp` (provenance prefix).
- Added an Engine precedence section: `brand-voice.md` and the engine gates win, and the skill
  does not author or approve customer-facing copy.
- Added license-aware routing (CAMeL Tools default, GPL family flagged).
- Removed Farasa entirely (research-only, commercial restriction).
- Removed the instruction to run `scripts/list-vendors.mjs` and dropped the script.
- Confirmed no em dashes, no tatweel, Western numerals throughout.

## Adoption record

- Adopted 2026-06-10, recorded as the explicit Ahmed-gate approval, scope: keep the GPL family
  with the bundling flag.
- Promoted from `references/staged-skills/AS-arabic-nlp/` to `.claude/skills/AS-arabic-nlp/`.
- Branch merged to main.

## Open item (does not block the skill as guidance)

- Legal sign-off on the GPL-family licenses (PyArabic confirmed GPL-3.0, Tashaphyne and Qalsadi
  and arabic-stopwords to confirm individually) before those libraries are bundled or
  distributed in the product. Decide the integration pattern (separate-process preprocessing vs
  linked) at that time. Owner: legal.
