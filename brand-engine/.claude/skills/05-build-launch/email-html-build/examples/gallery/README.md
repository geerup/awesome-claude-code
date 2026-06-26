# Example: email template gallery

A worked output of `/email-template-gallery mock` (see `commands/email-template-gallery.md`). One
mockup per buildable archetype, rendered from a single `spec.json` into one combined preview,
`index.html`:

- `g1-digest` (AR and EN): the multi-instructor "3 ways to X" digest (IssueIndex, LessonCardGrid, MemberWin).
- `g2-promo` (EN): one email of the occasion or sale ladder, the lineup as cards.
- `g3-voice` (EN): the instructor's first-person personal-voice launch.
- `g4-meet` (EN): the "Meet your new instructor" announcement plus "what you will learn".
- `g5-gift` (EN): give-a-membership, aimed at existing members.
- `g6-class` (EN): the single-instructor 7-step style, with the "other classes" ClassCardGrid.

This is a MOCKUP gallery. All copy is placeholder and labeled MOCK; "Instructor One" through "Six"
are NOT real catalog entries; no real offer, discount, or date appears. The contest archetype is
intentionally absent (compliance-gated). For a real send, every slot is QA-passed copy, every named
instructor is catalog-status-confirmed, every credential is page-cleared, placeholder portraits are
replaced with rights-cleared text-free portraits staged to the Ortto CDN, and the build passes the
full gate stack and the human gate. Nothing here sends.

Regenerate: `python3 .claude/scripts/email_render.py .claude/skills/05-build-launch/email-html-build/examples/gallery/spec.json`.
Open `index.html` to see all templates side by side.
