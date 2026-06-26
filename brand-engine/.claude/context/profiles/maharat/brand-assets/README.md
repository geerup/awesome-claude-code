# Maharat brand assets (official kit)

Provided by the team (2026-06-08). The canonical logos and brand fonts.

## Fonts (the real brand type)

- Latin: Acumin Pro (`fonts/acumin-pro/`).
- Arabic display: Lyon Arabic Display (`fonts/lyon-arabic-display/`, includes web woff/woff2 + css).
- Arabic alternate: 29LT Azer (`fonts/29lt-azer/`).

Email loads these via Ortto's hosted font CSS, exactly as the live Maharat sends do:
- `https://accounts-api-us.ortto.app/-/settings/custom-fonts.css?family=Acumin+Pro&k=bWFoYXJhdA`
- `https://accounts-api-us.ortto.app/-/settings/custom-fonts.css?family=Lyon+Arabic+Display&k=bWFoYXJhdA`

Stacks: AR `'Lyon Arabic Display','Tahoma',Arial,sans-serif`; EN `'Acumin Pro',Arial,Helvetica,sans-serif`.

Open governance item (Ahmed's call): the font binaries under `fonts/` are committed here, but the
engine's standing rule keeps licensed font binaries out of git (the `.claude/assets/fonts/` build
cache is gitignored for exactly this reason) because email loads the type from the Ortto-hosted CSS
above, never from the repo. Lyon Arabic Display in particular ships under a Commercial Type license
that restricts redistribution. So these binaries are unused at render time and carry a licensing
question. The de-dup left them in place rather than delete licensed assets unilaterally: whether to
remove them from git, keeping only the hosted CSS and these notes, is a rights decision for Ahmed.

Canonical type: the official kit and the live emails use Acumin Pro (EN) and Lyon Arabic Display
(AR), with 29LT Azer as the AR alternate. An earlier `email-design-system.html` had floated
Fraunces, Plus Jakarta, and IBM Plex Sans Arabic as a proposed rebrand; that file was retired in the
email de-dup and no rebrand is confirmed, so templates follow this official kit. The visual standard
is `context/email-design-system.md`.

## Logos (`logo/`)

- `maharat-white.*` for dark backgrounds (#141414), the email default.
- `maharat-black.*` for light backgrounds.
- `maharat-fullcolor.*` full color. SVG (vector master) and PNG provided.

For email, the logo needs a hosted URL; the live sends use
`m.autopilotapp.com/maharat/logo/l_80b9b5a2-...png`. These files are the masters for design and for
hosting a clean white logo if needed.
