# House voice - the locked editorial voice for all case copy

Greenlit by owner 2026-07-15. Every case study is written in this one voice.

## The voice: "Strategist Memo, with Operator restraint"

A hybrid of the two strongest voices from the voice swarm. Take the structural
moves of the strategist-memo voice and edit back in the operator's evidence-first
discipline.

### From the Memo voice - KEEP
- **Thesis-forward openers.** Each section opens with a one-line argument, then
  backs it. The problem section names the REAL problem beneath the obvious one
  (e.g. "Social's real problem was never the content. It was that nobody could
  prove it earned a thing.").
- **Load-bearing logic stated outright** ("Three calls built the function, and
  the first one made the other two provable.").
- **Honest ownership beat.** Claim the decisions, credit the team, in one line:
  "The team that grew around the function ran it; the calls were mine." This
  defuses the sole-credit flag before a skeptic can raise it. Use once per case,
  where it fits - never formulaic.
- Board-memo altitude: strong verbs, punchy rhythm, a little contrarian.

### From the Operator voice - EDIT BACK IN
- **Let the number stand.** Do NOT editorialize around it. Cut phrases like
  "reads as evidence and not a boast" or "not a boast" - state the figure and
  its source and stop. The receipt does the persuading.
- **Full citations, always.** Never compress "Salesforce, Vancouver Sprint 2024
  review" down to "tracked in Salesforce." Baseline + window + named source, in
  full, inline.
- Understatement over flourish. First person for ownership of the calls.

### Banned (from the Feature voice and generally)
- No third-person "written about him" framing. First person throughout.
- No color that isn't proof: cut lines like "an audience that smells marketing
  from a mile off" or "ran much of the world's cloud." Texture must be true and
  sourced, not decorative.

## The non-negotiables (unchanged across the build)
- No invention. Every fact traces to the case's named source on disk.
- Numbers ship as baseline + window + named source, inline.
- Hyphens only. NO em dashes or en dashes in authored copy.
- One honest caveat per case, kept. Never claim sole credit for team work.
- Do not touch design tokens, class names, chart/table markup, images, or the
  numbers themselves. Rewrite prose blocks in place only.

## Scope of a rewrite (what prose gets the treatment)
- The dek (header intro paragraph).
- Section 01 "The problem": the h2 and its paragraphs - thesis opener + stakes.
- Section 02 "The calls": the h2 and the decision sentences inside each existing
  .fork (rewrite the .d / rationale text as prose; KEEP the .fork / rejected /
  why HTML structure and every number).
- Section 03 "The run": the h2 and an optional one-line lede; keep the runlist,
  callouts, figures and their captions.
- Section 04: the caveat prose (keep it honest; keep any NEEDS_HUMAN chip).
- Never alter: strip-grid numbers, charts, tables, hbars, images, src, href,
  figcaptions' provenance, or the nav/footer.

## Case -> source map
- case-canonical-social.html    -> narrative/canonical-social.md
- case-ubuntu-summit.html       -> narrative/canonical-ubuntu-summit.md
- case-20-years.html            -> narrative/canonical-20-years.md
- case-data-ai.html             -> narrative/canonical-data-ai.md
- case-mindvalley-influencer.html -> narrative/mindvalley-influencer.md
- case-mindvalley-seo.html      -> narrative/mindvalley-seo.md
- case-cybersecurity.html       -> extracted/live-copy/portfolio-cybersecurity-awareness-month.md
  (lowest-authority live-site source; keep the existing honest downgrade in its
  caveat - do not inflate it to match the stronger cases)
