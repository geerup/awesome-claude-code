# Example: multi-instructor digest mockup

A worked output of `/email-mockup multi-instructor-digest mock` (see
`commands/email-mockup.md`). It demonstrates the "3 ways to [outcome]" multi-instructor digest:
the IssueIndex block, a 3-card LessonCardGrid (each card an outcome headline, a "with [Name],
[credential]" line, and a quiet secondary link), and the MemberWin block, with one primary emerald
CTA. Rendered AR and EN from `spec.json` by `scripts/email_render.py`, house-style clean.

This is a MOCKUP. The copy is placeholder and labeled MOCK; "Instructor One, Two, Three" are NOT
real catalog entries; there is no real offer. For a real send, every copy slot is a QA-passed
variant, every named instructor is catalog-status-confirmed in
`context/profiles/maharat/instructors/_EMAIL-IMAGE-MANIFEST.md` plus `_CATALOG.md`, every credential is page-cleared,
the placeholder portrait is replaced with a rights-cleared, text-free portrait staged to the Ortto
CDN, and the build passes the full gate stack and the human gate. Nothing here sends.

Files: `spec.json` (the recipe), `e1.ar.html` and `e1.en.html` (the rendered mockup), `index.html`
(a side-by-side preview sheet). Regenerate with
`python3 .claude/scripts/email_render.py .claude/skills/05-build-launch/email-html-build/examples/multi-instructor-digest/spec.json`.
