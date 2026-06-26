# 03-workflow-map: the 9 streams along one funnel

A campaign decomposes into 9 streams that hand off along one funnel. This is the conceptual
map. The runnable ownership table is `runtime/stream-ownership.md`. The artifacts that cross
each boundary are in `runtime/handoff-contract.md`.

## The 9 streams

1. Brief intake
2. Strategy and planning
3. Creative production
4. Copywriting
5. Build and launch
6. Conversion path
7. Lifecycle messaging
8. Monitoring and optimization
9. Reporting and learning

## Funnel logic

Acquisition (paid ads or organic social) sends traffic to the signup gate (email or
WhatsApp), which is the entry to lifecycle messaging. Owned-audience work (for example the
non-payer email flow) starts at stream 7, not at acquisition. Reporting feeds the next
campaign's strategy.

## Entry points and acquisition channels

- Entry A, paid acquisition: the full pipeline, streams 1 to 9, paid path through stream 5.
  performance-marketer plans the media, paid-build-engineer stages it.
- Entry B, owned audience: starts at stream 7. No paid build. Strategy and copy still run.
  The non-payer email flow is this entry point and the likely first build.
- Entry C, organic acquisition: organic-social distributes across the social following.

Five acquisition channels feed the same conversion path and lifecycle, each with a dedicated
owner agent, skill group, and SOP: paid performance (performance-marketer), SEO
(seo-specialist), blog and content (content-marketer), app and ASO (aso-specialist), and PR
and communications (pr-comms). They reuse streams 2, 3, 4, 8, and 9, and all stop at the
human gate. See `runtime/stream-ownership.md` for the full channel map.

## What each stream owes

Each stream has an SOP with: trigger, inputs, steps, output, quality bar, example output,
review owner. Long-form SOP files now exist in `sops/` for all 9 streams, plus one for each of
the 5 acquisition channels. Every stream is also covered by its skill package with the same
QA evals.

## SOP coverage status

- Long-form SOPs exist for all 9 streams: `sops/01-brief-intake.md` through
  `sops/09-reporting-learning.md`.
- Plus one SOP per acquisition channel: `sops/aso.md`, `sops/content-marketing.md`,
  `sops/paid-performance.md`, `sops/pr-comms.md`, `sops/seo.md`.
- Every stream is also covered by its skill package in `skills/` with the same QA evals.

For the per-stream owner, skills, and QA gate, read `runtime/stream-ownership.md`.
