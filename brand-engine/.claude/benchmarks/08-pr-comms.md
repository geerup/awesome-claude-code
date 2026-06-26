# Benchmark: PR and communications

Internet benchmark for the Maharat Marketing Engine PR and communications stream. It pulls
authoritative real-world frameworks for press releases, media lists, pitching, announcement
planning, embargoes, and news hooks, compares them to what the engine already does, and
lands a prioritized set of recommendations. It is a benchmark only. It edits no skill file.

Scope of our stream: `skills/pr-comms/SKILL.md` (hub), the three sub-skills
`announcement-plan`, `press-release`, `media-list-outreach` with their templates,
`sops/pr-comms.md`, the `pr-package` block in `runtime/handoff-contract.md`, and the PR
guardrails in `CLAUDE.md`.

## Sources reviewed (web)

- Notified, 5 Press Release Best Practices for 2025: https://www.notified.com/blog/5-press-release-best-practices-for-2025-what-you-need-to-know
- eReleases, What to Include in a Press Release, Complete Guide 2025 to 2026: https://www.ereleases.com/what-include-in-press-release-complete-guide-2025-2026/
- Prowly, Press Release Format and Structure: https://prowly.com/magazine/press-release-format-guide/
- PR Newswire, How to Write an AP Style Press Release: https://www.prnewswire.com/resources/articles/ap-style-press-release/
- eReleases, AP Style for Press Releases, the Ultimate Guide: https://www.ereleases.com/press-release-sample/ap-style-for-press-releases-the-ultimate-guide/
- Prezly, How to Pitch Journalists in 2025: https://www.prezly.com/academy/how-to-pitch-to-journalists
- Prowly, How to Write a Media Pitch with real examples: https://prowly.com/magazine/media-pitch/
- Muck Rack, Pitching Best Practices (Cision State of the Media data): https://help.muckrack.com/en/articles/4743056-pitching-best-practices
- ACCESS Newswire, Embargoed Press Release best practices: https://www.accessnewswire.com/blog/press-releases-tips/embargoed-press-release
- pr.co, Best Practices for Embargoed Press Releases: https://pr.co/blog/best-practices-for-embargoed-press-releases
- Joni Sweet, 7 Embargo Rules from a Journalist: https://jonisweet.substack.com/p/how-to-use-embargoes-in-pr
- Everything PR, Digital PR That Works in 2025 (newsjacking, news hooks): https://everything-pr.com/digital-pr-that-works-cutting-through-the-noise-in-2025/
- Motive PR, How Newsjacking Can Transform Your Digital PR Strategy: https://www.motivepr.co.uk/blog/tips-for-effective-newsjacking-in-digital-pr

## Best-in-class elements

What reputable PR practice converges on, organized by the four areas requested.

### 1. Press release structure and templates

- Fixed element order, inverted pyramid: headline, optional subheadline, dateline, lead
  paragraph that answers the 5 Ws (who, what, when, where, why) in the first sentence or two,
  body in descending order of importance, supporting quote, boilerplate, media contact, then
  the end notation. Most newsworthy fact leads.
- Headline tested as a final product. Practitioners draft 5 to 10 variants and pick the
  clearest. Concise, informative, keyword-aware for search.
- Dateline carries two facts: place (city of origin) and the release date or timing status.
- Boilerplate, the "About" block, written in the third person, 100 words or fewer, with
  mission, founding date, main products or services, and notable recognition. Journalists lift
  it verbatim, so it must be self-contained and free of first-person language.
- Media contact block: named person, title, email, and phone. A real human, reachable.
- End notation: `###` centered on its own line after the boilerplate, the wire convention
  that signals the release is complete and nothing was cut in transmission. Some houses use
  `-30-`.
- Short paragraphs, two to four sentences, one idea each. AI-friendly and scannable
  formatting with subheads and bullets. Multimedia matters: releases with visuals get many
  times more views than text-only.
- Quotes add a human or strategic voice, attributed to a named, titled spokesperson, and are
  not used to carry hard facts that belong in the body.

### 2. Media list building and press pitch best practices

- Build the list by beat, not by outlet. Address the individual journalist who covers the
  subject, not a generic newsroom inbox. The list can include reporters, but also relevant
  newsletter writers, podcast hosts, and credible niche voices.
- Relevance is the deciding factor. Cision State of the Media (over 3,000 journalists) reports
  86 percent will instantly reject a pitch that does not match their beat, and roughly 79
  percent reject for irrelevance. A pitch that lands is short, beat-specific, evidence-rich,
  and asks for one thing.
- Personalize. Address by name, reference prior work or covered topics, and tie the story to
  what that reporter actually writes. No generic blast.
- Pitch structure: a personal hook, the core story, the proof, one clear call to action,
  ideally under 100 words, paragraphs of one or two sentences.
- Subject line is the first impression and the open or ignore decision. Treat it as load
  bearing.
- Cadence: a small number of polite, spaced follow-ups, not repeated identical sends.

### 3. PR announcement planning

- Plan the announcement around a genuine news hook: a real milestone, launch, data point, or
  tie to a cultural or national moment. The hook is the reason a journalist cares.
- Favor positive or neutral hooks (cultural milestones, achievements, contribution) over pure
  self-promotion. Support-over-sell builds trust and pickup.
- Offer a novel angle, data, or insight rather than echoing existing coverage.
- Consume the target media first. Understanding what those outlets actually cover tells you
  which hook will work.

### 4. Embargoes and news hooks

- An embargo gives trusted reporters early access so they can prepare a story to publish the
  moment the news goes public, in exchange for holding until a set time.
- Mark the embargo unmistakably: a clear line at the very top of the release with the exact
  date, time, and timezone the embargo lifts, repeated in the email subject, body, and any
  attachment.
- Embargo etiquette, the big one: get journalist agreement first. Ask if they want the
  embargoed news before sending the full story. Opt-in creates a written record. Marking
  "embargoed" without mutual agreement is what journalists resent, and an unagreed embargo is
  not binding.
- Keep embargo lists small and trusted, on the order of 5 to 10 reporters who cover the beat.
  Every extra recipient raises leak risk.
- Newsjacking, proactive (prepare for an anticipated moment) or reactive (respond fast to
  breaking news), can earn outsized coverage when the tie is genuine and timely, and backfires
  when forced or opportunistic.

## Our coverage

What the engine already does, with the file that does it.

- Full fixed structure is specified. `skills/pr-comms/press-release/SKILL.md` step 2 and
  `templates/press-release.md` define headline and dateline, lead paragraph, body, quote,
  boilerplate ("about Maharat"), and media contact. Order matches best practice.
- Inverted-pyramid intent is present: the lead is "the single sayable news, stated plainly"
  and the body runs each claim against a sayable source
  (`templates/press-release.md`, Lead and Body sections).
- Dateline carries place and date, with an example (`templates/press-release.md`, "Riyadh,
  2026-06-03").
- Boilerplate is sourced from stable company facts only and bounded against roadmap,
  fundraising, and accreditation (`press-release/SKILL.md` step 5,
  `templates/press-release.md` Boilerplate section).
- Media contact is a named role with a clean channel, with an explicit no-personal-data rule
  (`templates/press-release.md`, Media contact section).
- English-first with an English version that follows the same facts and boundary, not a loose
  translation (`press-release/SKILL.md` step 2).
- Quote discipline is strong: attributed only to an approved spokesperson, and quote approval
  is a tracked open item until confirmed (all three sub-skills plus both templates).
- Media list is built by relevance and mapped to markets and angle, with a per-outlet angle, a
  contact role, a contact channel, and a "source confirmed?" flag
  (`media-list-outreach/SKILL.md` step 2, `templates/media-list-and-outreach.md`).
- Outreach sequence is planned: order, angle per outlet, timing or embargo, follow-up cadence,
  and a pitch copy variant reference (`templates/media-list-and-outreach.md`, Outreach plan).
- Embargo is referenced as a timing field and an open item ("embargo not confirmed")
  (`media-list-outreach/SKILL.md` step 4 and template).
- Announcement planning is a dedicated first gate. `announcement-plan/SKILL.md` fixes the
  sayable set and the hold-out set and produces the `guardrail_check` that everything else
  waits on.
- Data handling for journalist contacts is explicit and tied to compliance: need-to-know,
  never echoed into tracking or a public thread, with the Saudi PDPL and data-residency open
  item surfaced (`media-list-outreach/SKILL.md` step 3, template Data handling section).
- The gate stack and human gate are wired end to end: skill eval, then `arabic-copy-qa` or
  `english-copy-qa`, then `compliance-privacy-check`, then `brand-qa-reviewer`, then the human
  gate for any distribution (`pr-comms/SKILL.md`, `sops/pr-comms.md`,
  `runtime/handoff-contract.md` pr-package block).

## Gaps and missing elements (prioritized)

1. Embargo agreement is not modeled as opt-in. Our skills treat the embargo as a timing field
   and a "not confirmed" open item, but the single most emphasized rule in the sources is that
   an embargo is only valid once the journalist has agreed to it in advance. There is no
   step that requires asking the reporter first and recording the opt-in before the full
   release is shared. This is both a best-practice gap and a quiet leak-risk gap. (Sources:
   Joni Sweet, pr.co, ACCESS Newswire.)
2. No news-hook field in the announcement plan. The plan rules on what is sayable but never
   asks the prior question reporters care about most: why is this news, and what is the hook.
   A sayable-but-unnewsworthy announcement clears our gate yet would be ignored by the media.
   (Sources: Everything PR, Motive PR, Muck Rack.)
3. Pitch length, relevance, and "ask for one thing" are not specified. The media-list skill
   plans the sequence and references pitch copy by id, but gives the copywriters no shape for
   the pitch itself: under ~100 words, beat-specific, one clear ask, personalized to prior
   work. Given that 86 percent of journalists reject off-beat pitches, this shape is the
   difference between pickup and silence. (Sources: Muck Rack/Cision, Prezly, Prowly.)
4. Beat-level targeting is implicit, not required. The media list captures "relevance to the
   angle" and "contact role" but does not require mapping to a named reporter's beat or
   referencing their prior coverage. Outlet-level relevance is weaker than beat-level
   relevance. (Sources: Prezly, Muck Rack.)
5. No `###` or end-notation convention and no subheadline slot. The release template omits the
   wire end notation that signals completeness and the optional subheadline that best practice
   uses to extend the headline. Minor but standard. (Sources: eReleases AP Style, PR Newswire.)
6. Headline variant testing is not prompted. Best practice drafts several headlines and picks
   the clearest. The template asks for one line. A "draft N, pick one" note would lift quality.
   (Source: Notified.)
7. Multimedia is absent from the release shape. Releases with visuals get materially more
   views, yet the template has no slot to reference an approved, design-QA-passed visual.
   Worth noting that any such visual must clear `design-qa` and carry no baked-in Arabic text.
   (Source: Notified.)
8. Boilerplate word ceiling and third-person rule are not stated. We bound the boilerplate by
   content (stable facts, no roadmap) but not by form (100 words or fewer, third person). Both
   are easy, high-signal additions. (Sources: eReleases AP Style, PR Newswire.)

## Where ours is stronger

The engine is materially stronger than generic PR guidance on governance, and these are
deliberate, load-bearing differences, not gaps to close.

- Sayable-set discipline. Every claim in the release must trace to a fact that is already
  public or confirmed in the brief. A claim with no sayable source is dropped, not softened
  (`press-release/SKILL.md` step 3). Generic guidance assumes the facts are free to use; we do
  not.
- A hard guardrail that sits above the whole stream: never name an unannounced plan, a
  roadmap, fundraising, or an unconfirmed instructor, and never imply a certificate is
  accredited. Only public or brief-confirmed facts appear, and in doubt it stays out and
  becomes an open item (`CLAUDE.md` guardrails, all three sub-skills, `sops/pr-comms.md`).
  Most public PR advice has no equivalent stop.
- A dedicated announcement-plan gate that fixes the boundary before any release or pitch is
  written, with a `guardrail_check` where a single hold-out leak is a hard fail that returns
  the offending span (`announcement-plan/SKILL.md` step 5). Real-world practice rarely formalizes
  a go or no-go boundary at all.
- Distribution is gated, never automatic. Nothing sends or publishes without explicit
  human sign-off, per action and per campaign, and silence is never approval
  (`pr-comms/SKILL.md` hard rules, `sops/pr-comms.md` review owner). Mainstream PR workflows
  push to send.
- Compliance and brand gates are mandatory and ordered. Copy QA, then
  `compliance-privacy-check`, then `brand-qa-reviewer`, before anything is package-ready
  (`runtime/verification.md` path reflected across the stream).
- Journalist data handling is treated as a privacy obligation, need-to-know, never in a
  tracking parameter or public thread, with PDPL and data-residency surfaced
  (`media-list-outreach/SKILL.md` step 3). Generic media-list advice is silent on data
  protection.
- Quote approval as a standing open item until confirmed, with attribution only to an approved
  spokesperson. Stricter than the typical "add a quote" instruction.
- Separation of authorship. The hub plans and routes and never writes final copy. Copy is
  authored by `copywriter-ar` and the English copywriter and referenced by QA-passed variant
  id. This keeps the brand-voice and English-first gates in force on every public line.

## Recommendations (specific edits, prioritized, tied to sources)

These are proposals for a later editing pass. This benchmark changes no skill file.

1. Add an embargo opt-in step to `media-list-outreach`. In `SKILL.md` step 4 and the template
   Outreach plan, require that any embargo be agreed by the journalist in advance: send a
   short interest note, record the opt-in, and only then share the full release. Mark the
   embargo line (date, time, timezone) at the top of the release and repeat it in the pitch
   subject and body. Keep embargo lists small, 5 to 10 trusted beat reporters. Add "embargo
   not yet agreed by recipient" as a distinct open item, separate from "embargo not confirmed."
   This is the highest-value gap and a leak-risk reduction. (Joni Sweet, pr.co, ACCESS
   Newswire.)
2. Add a news-hook field to `announcement-plan`. In `SKILL.md` and
   `templates/announcement-plan.md`, after the objective and angle, require a one-line "news
   hook": why this is news now, drawn only from the sayable set. A sayable announcement with no
   hook should be flagged as weak, not just passed. Keep the hook honest and inside the
   boundary, no forced newsjacking. (Everything PR, Motive PR, Muck Rack.)
3. Specify the pitch shape for the copywriters. In `media-list-outreach/SKILL.md` step 4, brief
   the pitch as: under roughly 100 words, beat-specific, personalized to the reporter's prior
   coverage, a single clear ask, with a tested subject line. State that off-beat or generic
   pitches are rejected at high rates so relevance is non-negotiable. The pitch still runs the
   copy QA, compliance, and brand gates. (Muck Rack/Cision, Prezly, Prowly.)
4. Strengthen the media list to beat level. In `templates/media-list-and-outreach.md`, add a
   column or note for the named reporter's beat and a reference to their prior relevant
   coverage, so "relevance to the angle" is grounded in what the person actually writes, not
   just the outlet. Keep the "source confirmed?" flag and the no-invented-contact rule.
   (Prezly, Muck Rack.)
5. Complete the release template's standard form. In `templates/press-release.md`, add an
   optional subheadline slot under the headline, a `###` end notation line after the
   boilerplate, a boilerplate note "100 words or fewer, third person," and a "draft 5 to 10
   headline variants, keep the clearest" prompt. All stay English-first and inside the no
   em dash, no tatweel, Western numerals rules. (eReleases AP Style, PR Newswire, Notified.)
6. Add an optional multimedia reference to the release. In `templates/press-release.md`, allow
   a reference to one approved visual by id, with the explicit condition that it has cleared
   `design-qa` and carries no baked-in Arabic text. Keep it optional so a text-only release
   still passes. (Notified.)

## Brand-rule self-check

This document was checked against the engine brand rules. No em dash glyph is present (a grep
for the em dash character returns nothing). No tatweel or kashida is used. All numerals are
Western (0 to 9). Percentages and counts in the sources are written with Western numerals and
the word "percent."
