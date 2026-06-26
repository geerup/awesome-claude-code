# Benchmark: measurement, reporting, and QA

How the engine's measurement (stream 8), reporting and learning (stream 9), and the QA and
governance gates (arabic-copy-qa, english-copy-qa, design-qa, compliance-privacy-check,
build-vs-buy-eval, verification) compare to real-world best practice. The aim is to find gaps
worth closing and to name where ours is deliberately stronger, measured only against the
engine's own principles. No skill file was edited to produce this. This is a reference doc.

## Sources reviewed (web)

Reviewed June 2026. Used for the cross-checks below.

KPI selection, dashboards, and performance report structure
- HubSpot, KPI dashboards in marketing: https://blog.hubspot.com/marketing/kpi-dashboard
- Sona, Marketing KPI report template, a complete guide: https://www.sona.com/blog/marketing-kpi-report-template-a-complete-guide-to-effective-reporting
- Whatagraph, KPI dashboard examples and how to build one: https://whatagraph.com/blog/articles/marketing-kpi-dashboard
- Qlik, KPI examples and templates: https://www.qlik.com/us/kpi/kpi-examples

Vanity vs actionable metrics, North Star
- Amplitude, what makes a good vs bad North Star metric: https://amplitude.com/blog/good-bad-north-star-metric
- Userpilot, vanity metrics definition and examples: https://userpilot.com/blog/vanity-metrics/
- Mind the Product, measuring the right North Star metric: https://www.mindtheproduct.com/measuring-the-right-north-star-metric/

A/B test and experiment design (hypothesis, one variable, sample size, stop rule)
- Statsig, experiment design best practices: https://www.statsig.com/perspectives/ab-testing-design-best-practices
- NN/g, A/B testing 101: https://www.nngroup.com/articles/ab-testing/
- Evan Miller, how not to run an A/B test (fixed sample, no peeking): https://www.evanmiller.org/how-not-to-run-an-ab-test.html
- Optimizely, sample size calculations for experiments: https://www.optimizely.com/insights/blog/sample-size-calculations-for-experiments/

Campaign post-mortem, retrospective, learnings log
- Pedowitz Group, what a campaign post-mortem should include: https://www.pedowitzgroup.com/what-should-be-included-in-a-campaign-post-mortem-analysis
- TeamRetro, marketing campaign retrospective: https://www.teamretro.com/retro-template/marketing-campaign-retrospective/
- Assemble, campaign post-mortem template that improves ROI: https://www.onassemble.com/blog/campaign-post-mortem-template-that-actually-improves-roi

Content and brand QA checklists
- Filestage, content quality assurance process and QA checklists: https://filestage.io/blog/content-quality-assurance/
- Siteimprove, how to build a content quality assurance framework: https://www.siteimprove.com/blog/content-quality-assurance-framework/
- Search Engine Land, QA workflow for AI-generated content: https://searchengineland.com/guide/qa-workflow-for-ai-generate-content

Vendor and build-vs-buy evaluation scorecards
- G2, software vendor evaluation criteria and process: https://track.g2.com/resources/software-vendor-evaluation
- Software Advice, the ultimate software vendor evaluation guide: https://www.softwareadvice.com/resources/software-evaluation/

Data privacy compliance (GDPR and Saudi PDPL)
- CookieYes, Saudi PDPL overview: https://www.cookieyes.com/blog/saudi-arabia-personal-data-protection-law/
- Enzuzo, Saudi PDPL overview and compliance requirements: https://www.enzuzo.com/blog/saudi-arabia-personal-data-protection-law-pdpl
- PwC Middle East, KSA data protection law: https://www.pwc.com/m1/en/services/consulting/technology/cyber-security/navigating-data-privacy-regulations/ksa-data-protection-law.html

## Best-in-class elements

What the strongest sources converge on, by area.

Measurement and KPI selection
- One primary metric per effort. The North Star idea: pick the single metric that best
  captures customer value, make every team able to see how they move it. Avoid building a
  scorecard around 20-plus numbers; 5 to 10 KPIs keeps focus and speeds decisions.
- Separate metrics from KPIs. Page views and impressions are metrics; only those tied to a
  business objective (CAC, conversion, retention) are KPIs. A vanity metric grows and feels
  good but does not change a decision.
- Actionable test: "we changed X and metric Y moved." If you cannot link an action to the
  number, it is not actionable.

A/B test and experiment design
- One hypothesis, one variable. A test that changes two things teaches nothing about either.
- Hypothesis written from real data, in a structured one-line form (population, change,
  expected effect, reason). PICOT-style framing reduces ambiguity.
- Sample size fixed in advance from the baseline rate and the minimum detectable effect.
- Stop rule set before launch. The single biggest error is peeking and stopping when one
  arm pulls ahead; fixed-horizon tests require waiting out the planned sample or duration.
  Run at least one full week, ideally two, to capture weekly cycles. Bayesian or
  always-valid sequential methods are the only valid way to stop early, and only if chosen
  up front.

Performance report structure
- A clear narrative top to bottom: reporting period, objective, KPI scorecard (actual vs
  target), channel or funnel breakdown, insights, data sources. Headline result first.
- Monthly cadence for the report, weekly check-ins at the campaign level for live paid.

Campaign post-mortem and learnings
- Objectives and hypotheses, final results vs targets, funnel diagnostics, creative and offer
  analysis, channel and spend, tracking and attribution integrity, root-cause analysis.
- The two non-negotiables: trackable action items, each with an owner and a due date.
- Close the loop: a retrospective only pays off if its lessons feed the next initiative.

Content and brand QA
- A repeatable, documented checklist beats informal review: accuracy, clarity, brand voice
  and tone, compliance and legal, links and functionality, metadata.
- For AI-generated content, add explicit checks: factual accuracy, source verification,
  hallucination, brand voice, funnel fit, compliance risk, channel requirements, named owner.
- Both tooling and human review; QA is a gate, not a suggestion.

Vendor and build-vs-buy evaluation
- A weighted scorecard against criteria tied to strategic goals: cost, quality, delivery,
  service, compliance, technical capability, lock-in and exit, cultural fit.
- Separate must-have from nice-to-have (MoSCoW) so a deal-breaker is not offset by extras.
- A cross-functional review team to reduce single-reviewer bias.

Data privacy (GDPR and Saudi PDPL)
- PDPL is GDPR-inspired. For direct marketing: explicit opt-in consent before any promotional
  message; sensitive data must not be used for marketing.
- Data minimization: collect only what the primary purpose needs.
- Cross-border transfer and data residency: do not move KSA personal data outside the Kingdom
  without the prescribed safeguards.
- A published privacy policy disclosing what is collected, why, and with whom it is shared;
  accuracy, security, and data-subject rights. Enforcement in KSA is now active, not
  theoretical (SDAIA decisions in 2025 and 2026).

## Our coverage

Where the engine already meets the best-in-class elements, with the files that carry them.

Measurement and KPI selection
- One primary metric, fixed up front, is the spine of stream 8. Every read measures against
  the strategy-artifact success_metric and "never a metric invented after the fact." See
  `skills/08-monitoring-optimization/SKILL.md` and
  `skills/08-monitoring-optimization/performance-readout/SKILL.md`.
- Vanity metrics are named and excluded explicitly (impressions, raw reach, follower count)
  in `performance-readout/SKILL.md`, `performance-readout/templates/performance-readout.md`,
  the warehouse-query skill and spec, and across stream 9.
- "Every claim carries its evidence (number, source, window)" is enforced in the readout
  template's what_works and what_does_not_work blocks.

A/B test and experiment design
- One variable only, hold everything else constant: `ab-test-plan/SKILL.md` step 1 and the
  template's variable_under_test section.
- Hypothesis in the exact best-practice one-line form, tied to the success_metric:
  "Changing X to Y will move [success_metric] because [reason]." See `ab-test-plan/SKILL.md`
  step 2 and `ab-test-plan/templates/ab-test-plan.md`.
- Stop rule mandatory and set before the test runs, with a decision threshold and "no moving
  the goalposts after the fact." See `ab-test-plan/SKILL.md` step 5 and the template stop-rule
  block. This matches the Evan Miller and NN/g no-peeking discipline.

Performance report and reporting cadence
- Report structure maps to the narrative best practice: success_metric restated, results vs
  target with gap stated plainly, what_worked with evidence, what_to_change, open items. See
  `campaign-report/templates/campaign-report.md` and the report-artifact body in
  `runtime/handoff-contract.md`.
- Headline result stated plainly, miss or beat, no softening: campaign-report template.

Campaign post-mortem and learnings
- The close-out report covers results vs target, what worked with evidence, and concrete
  changes for the next brief: `skills/09-reporting-learning/campaign-report/SKILL.md`.
- The learnings loop is a real, durable, append-only log keyed by campaign_id, feeding the
  next campaign's strategy-lead via the report-artifact. See
  `skills/09-reporting-learning/learnings-log/SKILL.md` and
  `learnings-log/templates/learnings-log.md`. This is the "close the loop" element, built in.
- Observations without a metric are quarantined as not-yet-banked, not promoted to learnings.

Content and brand QA
- A binary, documented, repeatable gate stack, run in order, that returns structured fix
  lists rather than vibes: `runtime/verification.md`.
- Arabic copy QA: MSA with Gulf-familiar wording, Thmanyah tone, no tatweel, Western numerals,
  no em dash, empowering framing, RTL-safe. `skills/arabic-copy-qa/SKILL.md` and its fix-list.
- English copy QA: empowering tone, no em dash, Western numerals, one clear CTA, no
  accreditation implication, no invented offers or titles, plain active voice.
  `skills/english-copy-qa/SKILL.md` and its fix-list.
- Design QA: RTL, brand visual constants, rendered Western numerals, no Arabic baked into
  generated images, safe areas, premium and uncluttered, with a human design check retained.
  `skills/design-qa/SKILL.md` and its fix-list.
- AI-specific QA the sources call for (no invented facts, source-checked references) is
  covered by no-invented-offers-titles in english-copy-qa and the guardrails in CLAUDE.md.

Vendor and build-vs-buy
- A weighted scorecard with fixed criteria: Arabic capability (decisive), SOP fit, GCC and
  PDPL data fit, cost vs volume, integration effort, lock-in and exit, maturity and support.
  See `skills/build-vs-buy-eval/SKILL.md` and `templates/build-vs-buy-scorecard.md`.
- Borrow before building (the existing-tool check) and a single clear recommendation with
  blocking open items. Propose, never adopt: adoption is a human settings.json change.

Data privacy (GDPR and PDPL)
- Consent and opt-in, suppression, no PII in URLs or tracking, data-flows disclosed, and the
  Saudi PDPL and data-residency open item surfaced for the human gate. See
  `skills/compliance-privacy-check/SKILL.md` checks 1 to 5 and the fix-list template.
- PDPL data residency is treated as a standing open item that is flagged, never silently
  assumed resolved (pdpl-residency-surfaced). Tool adoption is never done by the gate.

## Gaps and missing elements

Prioritized. Each is a real best-practice element that our files underspecify or omit. None
require editing a skill now; they are candidates for a future skill revision.

Priority 1, sample-size and significance method in the A/B plan
- Best practice fixes sample size in advance from the baseline rate and the minimum
  detectable effect, and names the inference method (fixed-horizon with a significance
  threshold, or a sequential or Bayesian method chosen up front). Our `ab-test-plan` template
  asks for a stop condition (sample size or duration) and a decision threshold, but does not
  ask the author to derive the sample size from a baseline and an MDE, nor to state the
  significance level or the method. Risk: a "sample size" that is a guess, and an underpowered
  test that reads as inconclusive. Sources: Optimizely, Evan Miller, NN/g, Statsig.

Priority 2, action items with named owners and due dates in the report
- Every post-mortem source names trackable action items, each with an owner and a due date,
  as the non-negotiable output. Our `campaign-report` what_to_change captures the change and
  the why, but not an owner or a due date, and the next-brief routing is implicit. Adding an
  owner and a target date per change would close the accountability loop the sources demand.
  Sources: Pedowitz, Assemble, TeamRetro.

Priority 3, funnel and segment diagnostics in the readout and report
- Best-in-class post-mortems include funnel diagnostics (reach to engagement to conversion to
  revenue) and a segment or channel breakdown, not only the single headline metric. Our
  readout and report center the one success_metric (correct and deliberate) but do not ask for
  a funnel-stage or per-segment cut even though the strategy-artifact carries segments. A
  supporting-cut section, still anchored to the success_metric, would aid root-cause without
  reintroducing vanity metrics. Sources: Pedowitz, Whatagraph, Sona.

Priority 4, weighting and must-have gating in the scorecard
- Vendor-scorecard best practice assigns a weight per criterion and separates must-have from
  nice-to-have so a deal-breaker is not averaged away. Our `build-vs-buy-scorecard` scores 1
  to 5 per criterion and treats Arabic capability as a hard gate (good), but the other
  criteria are unweighted and there is no must-have versus nice-to-have split. Adding weights
  and a must-have column would make the recommendation more defensible. Sources: G2, Software
  Advice (MoSCoW, weighted matrix).

Priority 5, explicit PDPL and GDPR data-subject and retention checks
- The compliance gate covers consent, suppression, PII-in-URLs, data-flow disclosure, and
  residency surfacing. It does not explicitly check for data minimization (collect only what
  the purpose needs), a retention or deletion stance, or data-subject-rights handling
  (access, deletion), all of which PDPL and GDPR require. These could be added as checks or at
  least as surfaced open items. Sources: CookieYes, Enzuzo, PwC.

Priority 6, reporting cadence is implicit
- Sources recommend a monthly report with weekly campaign-level check-ins. Our stream 8 and 9
  trigger on events (a live window, a campaign close) rather than a stated cadence. This is a
  reasonable design for an agentic engine, but naming a default cadence in the SOP would help
  the human gate know when to expect a readout. Sources: Sona, HubSpot. Low priority.

## Where ours is stronger

Measured only against the engine's own success criteria, not against vanity benchmarks.

- Measure against the strategy success_metric, never invented after the fact. The North Star
  literature recommends one primary metric; our engine goes further and makes it a hard stop.
  If the strategy-artifact has no success_metric, every stream 8 and 9 skill must stop and
  ask rather than choose a metric. Most templates assume the analyst will pick KPIs at report
  time, which is exactly the after-the-fact selection that invites cherry-picking.
- No vanity metrics, enforced by name. The sources warn against vanity metrics; we name them
  (impressions, raw reach, follower count) and bar them from standing in for the success_metric
  in five separate files. The discipline is written into the templates, not left to judgment.
- Propose, never act. Every optimization move, test, and tool decision is a human-gate
  proposal. No skill pauses, shifts budget, sends, or adopts a tool on its own. Public
  best-practice frameworks rarely build this separation in; here it is a constitutional rule.
- A binary gate stack with structured fix lists. The QA literature recommends a checklist;
  ours is a hard stop in a fixed order (skill eval, language QA, design QA, compliance, brand
  QA) that returns a machine-readable fix list, one item per failure with the offending span
  quoted, and re-runs the same gate. No soft warnings pass through. That is stricter than the
  pass-with-comments review most sources describe.
- Arabic-specific QA. No generic content-QA framework checks tatweel, Eastern numerals,
  RTL-safety, dialect drift, or a Thmanyah tone benchmark. Our `arabic-copy-qa` does, and the
  build-vs-buy scorecard makes Arabic capability the decisive, disqualifying filter for any
  generative tool. This is a genuine capability the off-the-shelf checklists do not have.
- PDPL surfacing as a first-class behavior. Rather than treating residency as a one-time legal
  sign-off, the compliance gate surfaces the Saudi PDPL and data-residency open item every
  time Saudi user data, a send, or storage is in scope, and it never assumes the item is
  resolved. Surfacing-not-resolving is the right posture for an engine that cannot itself give
  legal sign-off.
- The learnings loop into the next campaign. The retrospective sources end at "feed the next
  initiative" as advice. Our engine implements it: an append-only learnings log keyed by
  campaign_id, referenced from the report-artifact (learnings_log_ref), consumed by the next
  campaign's strategy-lead. Observations without a metric are explicitly held back from being
  banked. The loop is a built mechanism, not a recommendation.

## Recommendations

Specific, prioritized edits for a future skill revision, each tied to a source. None applied
here; this doc only proposes.

1. Add a sample-size and method block to the A/B test plan (Priority 1). In
   `ab-test-plan/templates/ab-test-plan.md` and step 5 of the skill, require: baseline rate,
   minimum detectable effect, derived sample size per arm, significance level (or the named
   sequential or Bayesian method), and a note that the method is chosen before launch.
   Sources: Optimizely sample-size guide, Evan Miller, NN/g.

2. Add owner and due date to each what_to_change item in the campaign report (Priority 2). In
   `campaign-report/templates/campaign-report.md`, extend each change to carry an owner and a
   target date or target brief, so the action is trackable, matching the post-mortem
   non-negotiable. Sources: Pedowitz, Assemble.

3. Add an optional supporting-cuts section to the readout and report (Priority 3), anchored to
   the success_metric: a funnel-stage view and a per-segment cut drawn from the
   strategy-artifact segments, with a one-line rule that these support the success_metric and
   never replace it or reintroduce vanity metrics. Sources: Pedowitz, Whatagraph, Sona.

4. Add weights and a must-have column to the build-vs-buy scorecard (Priority 4). In
   `build-vs-buy-scorecard.md`, allow a weight per criterion and a must-have versus nice-to-have
   flag, keeping Arabic capability as the existing hard gate. Sources: G2, Software Advice
   (weighted matrix, MoSCoW).

5. Extend the compliance gate with data-minimization, retention, and data-subject-rights
   checks (Priority 5). Add to `compliance-privacy-check/SKILL.md` either as checks or as
   surfaced open items: collect only what the purpose needs, a stated retention or deletion
   stance, and access and deletion request handling, all required by PDPL and GDPR. Sources:
   CookieYes, Enzuzo, PwC.

6. State a default reporting cadence in the SOPs (Priority 6, low). Note in
   `sops/08-monitoring-optimization.md` and `sops/09-reporting-learning.md` a default of a
   monthly report with weekly campaign-level check-ins for live paid, while keeping the
   event-driven triggers. Sources: Sona, HubSpot.

Top 3 to act on first: recommendations 1, 2, and 5. They close the clearest gaps against the
strongest sources (test rigor, accountability, and legal completeness) and each is a contained
edit to one skill or template.
