# Profiles: how the engine stays one machine for many brands

This engine is profile-parameterized. The **machine** (agents, runtime, skills, sops,
scripts, commands) is brand-agnostic and never changes. The **facts** a run reads come from
the active profile. Swap the profile, keep the machine.

## What a profile is

A profile is a bundle of facts the machine reads:
- a brand brief (who the brand is, audience, offers, goals)
- a brand voice (how it sounds and looks: tone, lexicon, visual constants)
- a brand-context (the shared foundation the 29 brand skills auto-read)
- a subjects registry (the marketable entities: you, your services, your venture, research targets)
- the work it has produced (briefs, outputs, references)

The active profile is named in `context/active-profile.md`. Its live files sit at the top of
`context/` (`01-brand-brief.md`, `brand-voice.md`) and in `context/profiles/<name>/`.

## The two profiles here

### `me` (active) — the personal brand and career engine
The reason this engine exists now. Bundle: `context/profiles/me/`. Built to produce
approval-ready personal-brand assets: career stories, Substack posts, a portfolio and
website, visuals, copy, and outreach. You are the sole human-approval gate.

### `maharat` (archived, read-only) — the original engine
The campaign-agnostic marketing engine this was adapted from, for Maharat (an Arabic-first
edtech platform). Preserved in full, nothing thrown out:
- `context/profiles/maharat/` — all Maharat context facts, the instructor registry, the
  email design system, mining plans, findings, the Skill Paths M14 subsystem, brand assets,
  the marketing-super-team reference, and a pristine copy of the original engine docs under
  `_engine-docs-original/`.
- `outputs/maharat/` — the real approval-ready campaign packages (420 files).
- `references/maharat/` — the research and readouts (352 files).
- `briefs/maharat/` — the original campaign briefs.

Treat `maharat/` as a worked reference and a library of patterns to borrow, not as the active
brand. Many of its assets (the email module system, the mining machinery, the QA evals, the
instructor pack anatomy) are directly reusable for `me`.
