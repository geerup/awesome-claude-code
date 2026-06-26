---
name: 04-copywriting
description: Hub for stream 4 copywriting. Use when a brief or strategy-artifact needs customer-facing words written, triggers on "write the copy," "draft the ad," "email copy," "subject lines," "headline." Routes to ad-copy, email-copy, and subject-lines, and assembles the copy-package that streams 5, 6, and 7 consume.
---

# 04 Copywriting (stream 4 hub)

The entry point for all customer-facing words. Owned by `copywriter-ar`, reasoning mode,
English-first in the active brand voice. This hub does not write copy itself. It reads the inputs,
routes to the right sub-skill, and assembles the `copy-package` defined in
`runtime/handoff-contract.md`.

## Purpose

Turn a strategy-artifact (segment, angle, offer framing) into approval-ready copy variants,
subject lines, and a clear map of which asset-brief slots each variant fills. One machine,
any campaign. Targets, offers, and prices are read from the brief, never invented.

## When to use

- A campaign needs ad copy, email body copy, or email subject lines.
- A `creative-package` arrived with empty copy-overlay slots to fill.
- The orchestrator dispatches stream 4 (per `runtime/stream-ownership.md`).

Route by asset:
- Paid or social ad text, headline plus body plus one CTA per variant per segment: `ad-copy`.
- Lifecycle or campaign email body copy, one clear CTA: `email-copy`.
- Email subject lines, several options with one primary flagged: `subject-lines`.

## Inputs

- The `strategy-artifact`: segments, angle, offer_framing.
- The active `briefs/` file: offer, price, and promotion only when the asset shows them.
- `context/brand-voice.md`: the voice and the hard mechanical rules.
- The `creative-package` asset_briefs, when copy overlays creative (the slots to fill).

If a needed variable is absent from both brief and context, stop and ask. Do not fill the
gap with an invented value.

## Steps

1. Validate the incoming envelope: right campaign_id, status at least qa-passed, required
   strategy fields present, open_items read. If incomplete, return it, do not start.
2. List the assets to produce per segment, and which asset_brief slots they fill.
3. Route each asset to its sub-skill and draft English-first, one clear CTA per asset.
4. Assemble the `copy-package` body: variants[], subject_lines[], fills.
5. Run the gate stack in order: skill eval, then `arabic-copy-qa` (all Arabic copy), then
   `brand-qa-reviewer`. A fail is a hard stop that returns to the author with exact fixes.
6. On pass, set status to qa-passed and hand the copy-package downstream.

## Output: the copy-package

The body shape, exactly as `runtime/handoff-contract.md` defines it:

```
variants[]        each: id, segment, headline, body, one CTA, language (ar | en)
subject_lines[]   for email assets, with the chosen primary flagged
fills             which asset_brief copy slots each variant fills
```

Wrapped in the common envelope (campaign_id, produced_by, stream, status, qa, open_items,
brief_refs). See `templates/` in each sub-skill for the per-asset shape.

## How it connects

- Consumes: `strategy-artifact` (stream 2), `creative-package` asset_briefs (stream 3).
- Produces: `copy-package` (stream 4 -> 5, 6, 7).
- Gate before advance: skill eval + `arabic-copy-qa` + `brand-qa-reviewer`, in that order,
  per `runtime/verification.md`. Only qa-passed copy crosses the boundary.
