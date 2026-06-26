# The email pipeline, end to end

How a Maharat campaign becomes a gated, staged, ready-to-send email: the streams, the owning agent
for each, the skills (SOPs) they run, the files that govern them, and where the output lands. This is
a map, not a new rule. The rules live in
[`CLAUDE.md`](https://github.com/hostmaster-maharat/claude/blob/main/.claude/CLAUDE.md) and the anchor
docs it points to.

Every step is a relay: one owning agent, one skill, one named package, handed off through the envelope
in [`runtime/handoff-contract.md`](https://github.com/hostmaster-maharat/claude/blob/main/.claude/runtime/handoff-contract.md).
Reasoning agents design and write; nothing sends until the human gate. The whole run is composed by the
[orchestrator](https://github.com/hostmaster-maharat/claude/blob/main/.claude/agents/orchestrator.md)
out of the four shapes in
[`runtime/SWARM.md`](https://github.com/hostmaster-maharat/claude/blob/main/.claude/runtime/SWARM.md),
with ownership fixed in
[`runtime/stream-ownership.md`](https://github.com/hostmaster-maharat/claude/blob/main/.claude/runtime/stream-ownership.md).

## The straight line

| # | Stream | Owner agent | Skill (SOP) | Emits |
|---|---|---|---|---|
| 1 | Brief intake | [strategy-lead](https://github.com/hostmaster-maharat/claude/blob/main/.claude/agents/strategy-lead.md) | [01-brief-intake](https://github.com/hostmaster-maharat/claude/tree/main/.claude/skills/01-brief-intake) | validated brief |
| 2 | Strategy | [strategy-lead](https://github.com/hostmaster-maharat/claude/blob/main/.claude/agents/strategy-lead.md) | [02-strategy-planning](https://github.com/hostmaster-maharat/claude/tree/main/.claude/skills/02-strategy-planning) | `strategy-artifact` (segments, angle, offer, success metric) |
| 7 | **Lifecycle design** | [lifecycle-architect](https://github.com/hostmaster-maharat/claude/blob/main/.claude/agents/lifecycle-architect.md) | [07-lifecycle-messaging](https://github.com/hostmaster-maharat/claude/blob/main/.claude/skills/07-lifecycle-messaging/SKILL.md) | `lifecycle-package` (the flow: which email sits where, cadence, branches) |
| 4 | **Copywriting** | [copywriter-ar](https://github.com/hostmaster-maharat/claude/blob/main/.claude/agents/copywriter-ar.md) (default) + [copywriter-en](https://github.com/hostmaster-maharat/claude/blob/main/.claude/agents/copywriter-en.md) | [04-copywriting](https://github.com/hostmaster-maharat/claude/blob/main/.claude/skills/04-copywriting/SKILL.md) | `copy-package` (every variant keyed by `data-copy-id`) |
| 3 | Creative + header | [creative-director](https://github.com/hostmaster-maharat/claude/blob/main/.claude/agents/creative-director.md) + [designer](https://github.com/hostmaster-maharat/claude/blob/main/.claude/agents/designer.md) | [03-creative-production](https://github.com/hostmaster-maharat/claude/tree/main/.claude/skills/03-creative-production) | text-free assets; the header is gate-zero |
| 5 | **Email HTML build** | [paid-build-engineer](https://github.com/hostmaster-maharat/claude/blob/main/.claude/agents/paid-build-engineer.md) + [designer](https://github.com/hostmaster-maharat/claude/blob/main/.claude/agents/designer.md) | [05-build-launch / email-html-build](https://github.com/hostmaster-maharat/claude/blob/main/.claude/skills/05-build-launch/email-html-build/SKILL.md) | the slotted HTML, one file per email per language |
| gate | Human gate | [human-gate](https://github.com/hostmaster-maharat/claude/blob/main/.claude/agents/human-gate.md) | (none) | the approval-ready package (waits for Ahmed) |
| 8 to 9 | Monitor, report | [analytics-reporter](https://github.com/hostmaster-maharat/claude/blob/main/.claude/agents/analytics-reporter.md) | [08-monitoring](https://github.com/hostmaster-maharat/claude/tree/main/.claude/skills/08-monitoring-optimization), [09-reporting](https://github.com/hostmaster-maharat/claude/tree/main/.claude/skills/09-reporting-learning) | the report that feeds the next brief |

The three bold streams are the email-creation core: **lifecycle decides the sequence, copy writes the
words, build assembles words plus images into HTML.** Lifecycle never writes copy; build never invents
copy. Every word is a live HTML slot bound by `data-copy-id` to a QA-passed copy variant.

## How the HTML actually gets made (stream 5)

Two anchor docs govern every build:

- [`context/profiles/maharat/email-design-system.md`](https://github.com/hostmaster-maharat/claude/blob/main/.claude/context/profiles/maharat/email-design-system.md):
  the visual standard, the 12+1 component library (LogoBar, Hero, SectionHeading, BodyCopy, Button,
  ListBlock, ClassCardGrid, Footer, and the rest), the tokens, the dark and light themes.
- [`runtime/email-module-map.md`](https://github.com/hostmaster-maharat/claude/blob/main/.claude/runtime/email-module-map.md):
  the slot contract (`data-ortto-module`, `data-slot`, `data-role`, `data-lang`, `data-copy-id`,
  `data-link-slot`) and which gate each slot routes to.

The concrete pipeline in this repo is spec-driven:

> [`spec.json`](https://github.com/hostmaster-maharat/claude/blob/main/.claude/outputs/2026-06-bassam-fattouh-makeup/email-7step/bassam-fattouh/spec.json) (copy per slot)
> to [`scripts/email_render.py`](https://github.com/hostmaster-maharat/claude/blob/main/.claude/scripts/email_render.py) (the stdlib renderer)
> to `e1.ar.html` ... `e7.en.html` (slotted, RTL-correct, self-contained)
> to [`scripts/house_style_sweep.py`](https://github.com/hostmaster-maharat/claude/blob/main/.claude/scripts/house_style_sweep.py) (no em dash, no tatweel, Western numerals only)

`email_render.py` reads the campaign `spec.json` into the slot contract and writes one self-contained
HTML per email per language. An MJML authoring path lives under
[`skills/05-build-launch/email-html-build/mjml/`](https://github.com/hostmaster-maharat/claude/tree/main/.claude/skills/05-build-launch/email-html-build/mjml)
and compiles to the same slotted output; the committed HTML is the source of truth either way. The
header image is a precondition (gate-zero): no build starts without a verified header for the
instructor in
[`context/profiles/maharat/instructors/_EMAIL-IMAGE-MANIFEST.md`](https://github.com/hostmaster-maharat/claude/blob/main/.claude/context/profiles/maharat/instructors/_EMAIL-IMAGE-MANIFEST.md).

## The gate stack on a built email

Per [`runtime/verification.md`](https://github.com/hostmaster-maharat/claude/blob/main/.claude/runtime/verification.md),
in order, stopping at the first failure:

1. **Skill eval**: [`email-html-build/evals/evals.json`](https://github.com/hostmaster-maharat/claude/blob/main/.claude/skills/05-build-launch/email-html-build/evals/evals.json),
   run by [`scripts/eval_runner.py`](https://github.com/hostmaster-maharat/claude/blob/main/.claude/scripts/eval_runner.py) (structure, every copy slot bound, one primary CTA, brand fonts via Ortto CSS, brand constants only, house-style clean).
2. **Language copy QA**, per slot by `data-lang`: [`arabic-copy-qa`](https://github.com/hostmaster-maharat/claude/blob/main/.claude/skills/arabic-copy-qa/SKILL.md) or [`english-copy-qa`](https://github.com/hostmaster-maharat/claude/blob/main/.claude/skills/english-copy-qa/SKILL.md).
3. **Asset QA**: [`email-asset-qa`](https://github.com/hostmaster-maharat/claude/blob/main/.claude/skills/email-asset-qa/SKILL.md) on every `data-slot="element"` image (agent [email-asset-reviewer](https://github.com/hostmaster-maharat/claude/blob/main/.claude/agents/email-asset-reviewer.md)).
4. **Accessibility QA**: [`accessibility-qa`](https://github.com/hostmaster-maharat/claude/blob/main/.claude/skills/accessibility-qa/SKILL.md) on the render (agent [accessibility-reviewer](https://github.com/hostmaster-maharat/claude/blob/main/.claude/agents/accessibility-reviewer.md)).
5. **Compliance and privacy**: [`compliance-privacy-check`](https://github.com/hostmaster-maharat/claude/blob/main/.claude/skills/compliance-privacy-check/SKILL.md) on the send, suppression, links, unsubscribe (agent [compliance-privacy-reviewer](https://github.com/hostmaster-maharat/claude/blob/main/.claude/agents/compliance-privacy-reviewer.md)).
6. **Brand QA**, last, on the whole email: agent [brand-qa-reviewer](https://github.com/hostmaster-maharat/claude/blob/main/.claude/agents/brand-qa-reviewer.md).
7. **Human gate**: nothing sends without Ahmed, an attributable commit or recorded sign-off, never inferred. See [human-gate](https://github.com/hostmaster-maharat/claude/blob/main/.claude/agents/human-gate.md).

## Staging and send (Ortto, after the gates)

The gate-passed HTML is pushed to Ortto as drafts via the Ortto MCP (`create_asset`): it reads and
drafts only, no send, no delete, no image upload. Targeting is an Ortto audience; the 7-step becomes an
Ortto journey with a language split on `str::language`, suppression, and exit on `paying`. The send
itself is a human action in Ortto. A send-capable integration stays disabled until
[`runtime/send-safeguards.md`](https://github.com/hostmaster-maharat/claude/blob/main/.claude/runtime/send-safeguards.md)
is in force. The full build-and-stage runbook is
[`context/profiles/maharat/email-creation-cheatsheet.md`](https://github.com/hostmaster-maharat/claude/blob/main/.claude/context/profiles/maharat/email-creation-cheatsheet.md).

## Where everything lives

**Constitution and inputs**
- [`CLAUDE.md`](https://github.com/hostmaster-maharat/claude/blob/main/.claude/CLAUDE.md): the four principles, the two gates, the brand rules.
- [`briefs/`](https://github.com/hostmaster-maharat/claude/tree/main/.claude/briefs): per-campaign inputs, e.g. [`2026-06-nonpayer-email.md`](https://github.com/hostmaster-maharat/claude/blob/main/.claude/briefs/2026-06-nonpayer-email.md), [`2026-06-bassam-fattouh-makeup.md`](https://github.com/hostmaster-maharat/claude/blob/main/.claude/briefs/2026-06-bassam-fattouh-makeup.md).

**Durable facts ([`context/`](https://github.com/hostmaster-maharat/claude/tree/main/.claude/context))**
- [`brand-voice.md`](https://github.com/hostmaster-maharat/claude/blob/main/.claude/context/brand-voice.md): voice manual and worked examples.
- [`email-design-system.md`](https://github.com/hostmaster-maharat/claude/blob/main/.claude/context/profiles/maharat/email-design-system.md): the visual standard and component library.
- [`email-creation-cheatsheet.md`](https://github.com/hostmaster-maharat/claude/blob/main/.claude/context/profiles/maharat/email-creation-cheatsheet.md): the practical build and Ortto runbook.
- [`instructors/_CATALOG.md`](https://github.com/hostmaster-maharat/claude/blob/main/.claude/context/profiles/maharat/instructors/_CATALOG.md): public-status gate (confirmed vs unconfirmed).
- [`instructors/_EMAIL-IMAGE-MANIFEST.md`](https://github.com/hostmaster-maharat/claude/blob/main/.claude/context/profiles/maharat/instructors/_EMAIL-IMAGE-MANIFEST.md): the verified header per instructor (gate-zero).

**Run mechanics ([`runtime/`](https://github.com/hostmaster-maharat/claude/tree/main/.claude/runtime))**
- [`SWARM.md`](https://github.com/hostmaster-maharat/claude/blob/main/.claude/runtime/SWARM.md): the four shapes and the orchestrator loop.
- [`stream-ownership.md`](https://github.com/hostmaster-maharat/claude/blob/main/.claude/runtime/stream-ownership.md): who owns each stream.
- [`email-module-map.md`](https://github.com/hostmaster-maharat/claude/blob/main/.claude/runtime/email-module-map.md): the slot contract (anchor).
- [`verification.md`](https://github.com/hostmaster-maharat/claude/blob/main/.claude/runtime/verification.md): the gate order.
- [`send-safeguards.md`](https://github.com/hostmaster-maharat/claude/blob/main/.claude/runtime/send-safeguards.md): the standing safeguards before any send.
- [`handoff-contract.md`](https://github.com/hostmaster-maharat/claude/blob/main/.claude/runtime/handoff-contract.md): the package envelopes.

**Agents** ([the roster: `agents/_AGENTS-INDEX.md`](https://github.com/hostmaster-maharat/claude/blob/main/.claude/agents/_AGENTS-INDEX.md), 28 specialists). The email path uses
[lifecycle-architect](https://github.com/hostmaster-maharat/claude/blob/main/.claude/agents/lifecycle-architect.md),
[copywriter-ar](https://github.com/hostmaster-maharat/claude/blob/main/.claude/agents/copywriter-ar.md),
[copywriter-en](https://github.com/hostmaster-maharat/claude/blob/main/.claude/agents/copywriter-en.md),
[designer](https://github.com/hostmaster-maharat/claude/blob/main/.claude/agents/designer.md),
[paid-build-engineer](https://github.com/hostmaster-maharat/claude/blob/main/.claude/agents/paid-build-engineer.md),
the verifier agents ([email-asset-reviewer](https://github.com/hostmaster-maharat/claude/blob/main/.claude/agents/email-asset-reviewer.md),
[accessibility-reviewer](https://github.com/hostmaster-maharat/claude/blob/main/.claude/agents/accessibility-reviewer.md),
[compliance-privacy-reviewer](https://github.com/hostmaster-maharat/claude/blob/main/.claude/agents/compliance-privacy-reviewer.md),
[brand-qa-reviewer](https://github.com/hostmaster-maharat/claude/blob/main/.claude/agents/brand-qa-reviewer.md)),
and [human-gate](https://github.com/hostmaster-maharat/claude/blob/main/.claude/agents/human-gate.md).

**Skills ([`skills/`](https://github.com/hostmaster-maharat/claude/tree/main/.claude/skills), the SOPs)**
- [`04-copywriting`](https://github.com/hostmaster-maharat/claude/tree/main/.claude/skills/04-copywriting): email-copy, subject-lines, ad-copy.
- [`05-build-launch/email-html-build`](https://github.com/hostmaster-maharat/claude/tree/main/.claude/skills/05-build-launch/email-html-build): the HTML build SOP (plus `mjml/` and `evals/`).
- [`07-lifecycle-messaging`](https://github.com/hostmaster-maharat/claude/tree/main/.claude/skills/07-lifecycle-messaging): segmentation-logic, nonpayer-email-flow, onboarding-sequence, event-sequence, winback-flow, and `templates/sequence-standards.md`.
- QA gates: [arabic-copy-qa](https://github.com/hostmaster-maharat/claude/blob/main/.claude/skills/arabic-copy-qa/SKILL.md), [english-copy-qa](https://github.com/hostmaster-maharat/claude/blob/main/.claude/skills/english-copy-qa/SKILL.md), [email-asset-qa](https://github.com/hostmaster-maharat/claude/blob/main/.claude/skills/email-asset-qa/SKILL.md), [accessibility-qa](https://github.com/hostmaster-maharat/claude/blob/main/.claude/skills/accessibility-qa/SKILL.md), [compliance-privacy-check](https://github.com/hostmaster-maharat/claude/blob/main/.claude/skills/compliance-privacy-check/SKILL.md).

**Scripts ([`scripts/`](https://github.com/hostmaster-maharat/claude/tree/main/.claude/scripts))**
- [`email_render.py`](https://github.com/hostmaster-maharat/claude/blob/main/.claude/scripts/email_render.py): spec.json to slotted HTML (the renderer).
- [`house_style_sweep.py`](https://github.com/hostmaster-maharat/claude/blob/main/.claude/scripts/house_style_sweep.py): the no-em-dash, Western-numeral sweep.
- [`eval_runner.py`](https://github.com/hostmaster-maharat/claude/blob/main/.claude/scripts/eval_runner.py): runs the skill evals.
- [`drive_image_sync.py`](https://github.com/hostmaster-maharat/claude/blob/main/.claude/scripts/drive_image_sync.py) + [`image_catalog_check.py`](https://github.com/hostmaster-maharat/claude/blob/main/.claude/scripts/image_catalog_check.py): the image catalog and Drive pull.

**Outputs ([`outputs/<campaign>/`](https://github.com/hostmaster-maharat/claude/tree/main/.claude/outputs))**: the produced work.

## The Bassam run mapped onto the line (worked example)

- Brief: [`briefs/2026-06-bassam-fattouh-makeup.md`](https://github.com/hostmaster-maharat/claude/blob/main/.claude/briefs/2026-06-bassam-fattouh-makeup.md)
- Spec and HTML: [`email-7step/bassam-fattouh/`](https://github.com/hostmaster-maharat/claude/tree/main/.claude/outputs/2026-06-bassam-fattouh-makeup/email-7step/bassam-fattouh) ([`spec.json`](https://github.com/hostmaster-maharat/claude/blob/main/.claude/outputs/2026-06-bassam-fattouh-makeup/email-7step/bassam-fattouh/spec.json) plus `e1.ar.html` ... `e7.en.html`, 14 files)
- Enrichment and gate results: [`_REVIEW-AND-ENRICHMENT.md`](https://github.com/hostmaster-maharat/claude/blob/main/.claude/outputs/2026-06-bassam-fattouh-makeup/email-7step/_REVIEW-AND-ENRICHMENT.md)
- Targeting: [`_TARGETING-watched-first-chapter.md`](https://github.com/hostmaster-maharat/claude/blob/main/.claude/outputs/2026-06-bassam-fattouh-makeup/_TARGETING-watched-first-chapter.md)
- Send wiring: [`_SEND-SETUP-bassam.md`](https://github.com/hostmaster-maharat/claude/blob/main/.claude/outputs/2026-06-bassam-fattouh-makeup/_SEND-SETUP-bassam.md)
- Ortto staging status, the 14 asset ids: [`_ORTTO-STAGING-STATUS.md`](https://github.com/hostmaster-maharat/claude/blob/main/.claude/outputs/2026-06-bassam-fattouh-makeup/_ORTTO-STAGING-STATUS.md)
