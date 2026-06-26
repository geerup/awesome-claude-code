---
name: AS-arabic-nlp
description: Reference skill for selecting and applying Arabic NLP tooling (transliteration, diacritization, tokenization, stemming, morphology) across CAMeL Tools, PyArabic, Tashaphyne, Qalsadi, and Arabic stopwords. Reference only, it does not author customer-facing Arabic copy.
---

# AS-arabic-nlp (reference only)

## Status and provenance

- ADOPTED and live. Approved 2026-06-10, recorded as the Ahmed-gate adoption approval. Lives
  under `.claude/skills/AS-arabic-nlp/`.
- Source: arabskills.info, github.com/ArabAgentSkills/Skills, upstream skill `arabic-nlp`,
  pinned at commit add86a278341568232c3fdac97caf01c0824dc5d (fetched 2026-06-10). Upstream
  repo license is MIT.
- Security, license, and reconciliation record: see `VETTING.md` in this folder. Farasa was
  removed before adoption (research-only).

## Engine precedence (non-negotiable)

- This skill is subordinate to the engine. `context/brand-voice.md`, `arabic-copy-qa`,
  `compliance-privacy-check`, and `brand-qa-reviewer` win over anything written here.
- It does not write or approve customer-facing Arabic copy. `copywriter-ar` owns Arabic
  authoring. Any transliteration or text this skill helps produce still passes `arabic-copy-qa`
  and `brand-qa-reviewer`.
- Western numerals only (0 to 9). No tatweel or kashida. No em dashes. RTL-safe.

## When to use

- Choosing or applying an Arabic NLP library for transliteration, diacritization,
  tokenization, stemming, or morphological analysis, in support of `copywriter-ar` or
  `arabic-copy-qa`. For example, transliterating a name into Arabic, or checking diacritics on
  a rendered line.

## When not to use

- To author or sign off customer-facing copy. That is `copywriter-ar` plus the gates.
- To make accuracy or benchmark claims without a source.
- To send personal or sensitive Arabic text to a third-party API. Local libraries by default.
  Any hosted API (for example a hosted NLP service) is a gated, compliance-reviewed action and
  never receives customer PII.

## License-aware routing (Maharat, commercial use)

- Default to CAMeL Tools for anything Maharat ships. It is MIT licensed (NYU Abu Dhabi), so it
  is commercial-safe.
- PyArabic, Tashaphyne, Qalsadi, and Arabic stopwords are GPL-family (PyArabic confirmed
  GPL-3.0). Usable, but copyleft. Before bundling or distributing, get legal sign-off, and
  prefer running them as a separate preprocessing process rather than linking them into shipped
  product code.
- Farasa is intentionally excluded. It is research-only (QCRI permits research use only,
  non-research use requires a QCRI license), so it is not part of this skill. Do not add it
  back without a QCRI license and legal sign-off.

## Vendor registry (this skill's scope)

arabic-stopwords, camel-tools, pyarabic, qalsadi, tashaphyne. Facts live in `vendors.md` and
`sources.yml`. Treat the upstream vendor notes as leads, not ground truth: they are thin and
templated from an unrelated atlas. Confirm against each official source before implementing.

## Default workflow

1. Read `sources.yml` for the vendors and their source confidence. Do not run any script. The
   upstream `scripts/` helper is removed on purpose, read the files directly.
2. Identify the task (transliteration, diacritization, tokenization, stemming, morphology) and
   the constraints (local vs hosted, data sensitivity, license).
3. Apply the license-aware routing above. Default to CAMeL Tools.
4. For implementation or review work, read `references/integration-checklist.md`.
5. Answer with source-backed facts, explicit unknowns (`Unknown from public docs` or `Needs
   vendor access`), and validation steps. Name the files you read.

## Safety

- Local libraries by default. No customer PII to external APIs. Any hosted call is gated and
  compliance-reviewed.
- Separate sandbox and production. Check license and data handling before any production use.
- Benchmark on the target dialect and domain. Document tokenizer and stemmer limitations.

## Done criteria

- The files read are named.
- The recommendation is license-aware and source-backed.
- Unknowns are labeled, not guessed.
- Engine gates and brand-voice precedence are respected.
