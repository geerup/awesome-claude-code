# AS-arabic-nlp (ADOPTED, live)

This skill is live under `.claude/skills/AS-arabic-nlp/`. It was staged, vetted, and adopted on
2026-06-10, recorded as the Ahmed-gate adoption approval. Farasa was removed before adoption
because it is research-only.

- What it is: a reference skill for selecting and applying Arabic NLP tooling (transliteration,
  diacritization, tokenization, stemming, morphology). Source: arabskills.info, upstream skill
  `arabic-nlp`, pinned at commit add86a2.
- Scope: CAMeL Tools (MIT, the default) plus the GPL-family libraries (PyArabic, Tashaphyne,
  Qalsadi, arabic-stopwords), which carry a legal-sign-off-before-bundling flag. See `VETTING.md`.
- It is reference only. It does not author customer-facing Arabic copy (`copywriter-ar` owns
  that), and anything it helps produce still passes `arabic-copy-qa` and `brand-qa-reviewer`.

Open follow-up, which does not block the skill as guidance: legal sign-off on the GPL-family
licenses before those libraries are bundled or distributed in the product. Tracked in
`../../references/REVIEW-QUEUE.md`. Full build-vs-buy readout:
`../../references/2026-06-arabskills-info-skills-research.md`.
