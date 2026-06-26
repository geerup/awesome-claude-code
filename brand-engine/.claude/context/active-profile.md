# Active profile

active: me

The engine runs one profile at a time. The active profile names which fact bundle the
machine loads as its source of truth. Facts for the active profile live in the top-level
`context/` files (`01-brand-brief.md`, `brand-voice.md`) and in `context/profiles/<active>/`.
Variables still come from the active `briefs/` file, never invented.

Profiles available:
- `me` (active): the personal brand and career engine. See `context/profiles/me/`.
- `maharat` (archived, read-only): the original Maharat marketing engine this was adapted
  from. Preserved in full under `context/profiles/maharat/`. Do not treat as the active
  brand; it is a worked reference. See `context/profiles/_README.md`.

To switch profiles: change the `active:` line above, point `context/brand-voice.md` and
`context/01-brand-brief.md` at that profile's bundle, and set `.agents/brand-context.md`
to that profile's brand-context. The machine (agents, runtime, skills, sops, scripts) does
not change between profiles.
