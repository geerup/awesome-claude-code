# Benchmark: strategy and planning

Internet benchmark for stream 2 (strategy and planning) of the Maharat Marketing Engine.
Compares our strategy SOP, skills, and templates against authoritative real-world frameworks
for audience segmentation, personas, positioning and value proposition, messaging angle,
go-to-market briefs, and success-metric selection. Written June 2026.

This doc is a benchmark only. It does not edit any skill, SOP, or template. Recommendations
are proposals for Ahmed to approve, consistent with the human-review gate.

Scope note: most public frameworks below are written for product and B2B sales motions. Our
engine is a campaign-level marketing engine for a consumer learning platform. We adopt the
reasoning, not the sales-org machinery (sales compensation, quotas, pipeline). Where a
framework element does not fit a campaign engine, that is called out, not imported wholesale.

---

## Sources reviewed (web)

- Strategyzer, The Value Proposition Canvas (customer jobs, pains, gains, and the value map
  of products and services, pain relievers, gain creators, plus the concept of fit):
  https://www.strategyzer.com/library/the-value-proposition-canvas
- Strategyzer, Value Proposition Design book summary:
  https://www.strategyzer.com/library/value-proposition-design-book-summary
- Amplitude, North Star Metric, how to find yours (a single metric that captures customer
  value, with leading-indicator input metrics, and the good-vs-bad criteria):
  https://amplitude.com/blog/product-north-star-metric
- Amplitude, About the North Star Framework:
  https://amplitude.com/books/north-star/about-north-star-framework
- April Dunford, An Introduction to Positioning, and the Lenny's Newsletter summary of her
  five positioning components and the positioning-is-not-messaging distinction:
  https://www.aprildunford.com/post/an-introduction-to-positioning
  https://www.lennysnewsletter.com/p/summary-april-dunford-on-product
- Gartner, Go-to-Market Strategy Framework (target market identification, demand generation,
  voice of the customer, and supporting components):
  https://www.gartner.com/en/sales/trends/go-to-market-strategy-framework
- Michael Brito, Audience Segmentation Strategy in 2025, and Klaviyo's B2C segmentation guide
  (the four segmentation types and the multi-layered demographic, behavioral, psychographic,
  and intent approach):
  https://www.britopian.com/research/audience-segmentation-strategy-in-2025/
  https://www.klaviyo.com/features/segmentation/strategy
- HubSpot Make My Persona and Miro proto-persona and buyer-persona templates (persona core
  elements, day-in-the-life, success drivers, objections, and the jobs-to-be-done job story):
  https://www.hubspot.com/make-my-persona
  https://miro.com/templates/proto-persona/

---

## Best-in-class elements

What the strongest public frameworks insist on for strategy and planning.

1. Segment on more than demographics. The 2025 consensus (Brito, Klaviyo) is a multi-layered
   cut: demographic plus behavioral plus psychographic plus real-time intent, where each
   layer corrects the others' blind spots. Behavioral and intent signals are treated as the
   sharpest predictors, not demographics alone.

2. Size and prioritize segments, do not just name them. Mature segmentation ranks segments by
   value and reachability so effort goes where it pays, and ties each segment to an
   activation path.

3. Personas carry decision-useful fields, not biography. The strong templates (HubSpot, Miro)
   converge on a tight set: an archetype, a day-in-the-life, goals and success drivers, top
   objections, and real verbatim quotes. The job story ("when I..., I want to..., so that
   I...") forces a need, not a label.

4. Positioning precedes messaging, and has explicit inputs. Dunford's five components are:
   competitive alternatives (what the customer would do otherwise), unique attributes, the
   value those attributes enable, the target customer who cares most about that value, and
   the market category that frames it. Positioning is the input set; messaging is written
   from it, never before it.

5. Value is mapped to a real customer profile. The Value Proposition Canvas demands fit: every
   pain reliever and gain creator must trace to a stated customer pain or gain. A claimed
   benefit with no matching customer job is flagged as a miss.

6. One single-minded proposition per campaign. The advertising-brief tradition and Dunford
   both push to a single load-bearing idea. Decide the one thing; everything else supports it.

7. A go-to-market brief is structured and complete. Gartner's components: target market
   identification, first touchpoint and demand generation, voice of the customer, plus the
   commercial model. The discipline is completeness: the brief states market, offer,
   audience, channel, and how customer feedback re-enters the plan.

8. Pick one north-star metric, defined by clear criteria. Amplitude: the north star is a
   single metric that captures the value customers actually get, is a leading (not lagging)
   indicator, is measurable, and sits above a small set of input metrics that teams can move.
   A good metric reflects customer value and predicts revenue; a bad one is a vanity count or
   a pure lagging financial number nobody can act on.

---

## Our coverage

Where our engine already does these things, with file citations.

- Multi-axis segmentation. `skills/02-strategy-planning/audience-segmentation/SKILL.md` names
  engagement state, prior interest, and recency of last open as axes, which is behavioral and
  intent layering, not demographics alone. `templates/segmentation-plan.md` section 1 forces
  the author to state the axes and why each matters.
- Each segment is named, defined, and justified. The `segments[]` shape in the hub
  (`skills/02-strategy-planning/SKILL.md`) and in `runtime/handoff-contract.md` requires name,
  size, definition, and why. The "why" field carries the activation rationale.
- Sizing discipline. `audience-segmentation/SKILL.md` and `segmentation-plan.md` sections 3
  and 4 require every size to trace to data, or be marked an estimate, or be flagged as
  resolved from live data at send time. This is the prioritization-by-data instinct, enforced
  as a hard rule against invented numbers.
- A single core angle. `offer-and-angle/SKILL.md` and `templates/angle-and-offer-framing.md`
  section 1 require one core_message, a rationale, and a single through_line, with optional
  per-segment tuning that must not break the one idea. This is the single-minded proposition.
- Offer framing tied to value, not price. `angle-and-offer-framing.md` section 2 frames the
  hook, the value, and the path to a first action, and shows price only if the brief supplies
  it. The empowering check in section 3 ties the angle to what the reader can build.
- A channel plan and one success metric. The hub assembles channel_plan and success_metric
  into the strategy-artifact (`SKILL.md` steps 4 and 5, `sops/02-strategy-planning.md` steps 1
  and 5). The metric is read from the brief, carried forward unchanged, and is the only thing
  streams 8 and 9 measure against.
- A complete, validated handoff. `runtime/handoff-contract.md` defines the strategy-artifact
  body (segments, angle, offer_framing, channel_plan, success_metric) inside a common envelope
  with status, qa, open_items, and brief_refs, and a downstream validation rule. This is a
  go-to-market brief with a completeness gate built in.

---

## Gaps and missing elements (prioritized)

### High

- No explicit pains-and-gains or jobs-to-be-done step. We jump from segment definition to
  angle without a structured customer-profile pass. The Value Proposition Canvas and the JTBD
  job story would force each angle to trace to a stated customer pain or gain for that
  segment, which is the discipline that keeps an angle from being a clever line with no need
  behind it. Today the link from segment "why" to angle "rationale" is implicit.
- No competitive-alternative field in the angle. Dunford's first positioning input is what the
  customer would otherwise do (a competitor, a free workaround, or nothing). Our offer framing
  states the hook and value but never the alternative it beats. For a learning platform the
  honest alternative is often free content on social or doing nothing, and naming it sharpens
  the angle. Missing today.
- Success-metric quality criteria are asserted but not tested. Our rule is strong on
  provenance (carry the brief's number unchanged, no vanity metrics) but has no checklist for
  whether the chosen metric is a good one: leading vs lagging, captures customer value,
  movable via inputs. If a brief names a weak metric, the engine carries it faithfully but
  does not flag it. Amplitude's good-vs-bad test would catch that.

### Medium

- No input-metric layer under the north star. Amplitude pairs one north-star metric with a
  small set of leading input metrics that teams can actually move. Our success_metric is a
  single number with no stated leading indicators, so stream 8 has nothing intermediate to
  steer by before the lagging result lands.
- No lightweight persona artifact. Segments carry name, definition, and why, but not the
  decision-useful persona fields (day-in-the-life, top objections, a real or representative
  quote, success drivers). Copywriters in stream 4 inherit a segment, not a person to write
  to. A proto-persona block per segment would close this without heavy research.
- Market category and frame are unstated. Dunford's market-category component (how the buyer
  files what you are) is absent. For a campaign engine this is lower stakes, but the angle
  sometimes implies a category (a class, a path, a habit) without making it a deliberate
  choice.

### Low

- No explicit fit check between offer and customer profile. The Value Proposition Canvas asks
  whether each gain creator and pain reliever maps to a real customer gain or pain. We have an
  empowering check but not a fit check. Low because the angle through-line partly covers it.
- Voice-of-the-customer loop is implicit. Gartner makes customer feedback re-entry a named
  component. Our engine handles this across streams via the report-artifact feeding the next
  campaign's strategy-lead (`runtime/handoff-contract.md`), so it exists at the engine level,
  just not inside stream 2.

---

## Where ours is stronger

These are deliberate strengths of our engine, not gaps in the public frameworks.

- No invented segment sizes. Public segmentation guides freely model and estimate segment
  sizes. Our `audience-segmentation/SKILL.md` and `segmentation-plan.md` forbid an invented
  size outright: every figure traces to data, is marked an estimate, or is flagged as resolved
  from live data at send time. This is stricter and safer than the benchmark norm, and it
  prevents a plausible-looking number from becoming a planning fact.
- Success-metric discipline. Most frameworks let teams add metrics and revisit them often
  (Amplitude even celebrates changing the north star repeatedly). Our SOP sets one metric from
  the brief, carries it forward unchanged, bars vanity metrics, and makes it the single thing
  streams 8 and 9 measure against (`sops/02-strategy-planning.md` step 1, hub step 5). That
  single-source discipline is a genuine strength for honest reporting.
- English-first, Gulf and Saudi focus. The public templates are English-default and culture-
  neutral. Our engine bakes Modern Standard Arabic with Gulf-familiar wording, the Thmanyah
  tone, no tatweel, Western numerals, and empowering (never deficit-framed) framing into the
  strategy layer itself, so the angle is built right for the market from the first artifact.
- The handoff envelope. No public strategy framework ships a structured handoff contract with
  status, qa, open_items, brief_refs, and a downstream validation rule
  (`runtime/handoff-contract.md`). Our strategy-artifact cannot cross a boundary below
  qa-passed and cannot hide an unresolved assumption. That makes strategy auditable and
  composable in a way a canvas or a slide does not.
- Stop-and-ask over invent. Every public framework assumes the strategist fills gaps with best
  judgment. Our constitution turns a missing variable into a hard stop. For a campaign-agnostic
  engine handling real spend and sends, that is the correct and stronger default.

---

## Recommendations

Specific, prioritized, tied to the sources. All are proposals for Ahmed, not changes made here.
None require importing the sales-org machinery the public GTM frameworks carry.

### High priority

1. Add a pains-and-gains step before the angle, tied to each segment. In
   `offer-and-angle/SKILL.md` add a step, and in `angle-and-offer-framing.md` a short section,
   that lists the top customer pains and desired gains per segment and requires the angle's
   rationale to relieve a named pain or create a named gain. Source: Strategyzer Value
   Proposition Canvas and the JTBD job story. This makes the implicit segment-to-angle link
   explicit and testable, and it is the single highest-leverage gap.

2. Add a competitive-alternative field to the offer framing. In `angle-and-offer-framing.md`
   section 2, add `alternative:` (what the reader does instead: free content, another app, or
   nothing) and require the positioning to beat it. Source: April Dunford, positioning
   component one. Low cost, sharpens every angle.

3. Add a success-metric quality check to the SOP. In `sops/02-strategy-planning.md` step 1 and
   the hub quality bar, add a brief test: is the metric a leading indicator, does it capture
   customer value, is it movable. Keep the provenance rule (carry the brief's number unchanged)
   but if the metric fails the test, raise it to Ahmed as an open item rather than carrying a
   weak metric silently. Source: Amplitude good-vs-bad north star criteria.

### Medium priority

4. Introduce a leading input-metric layer under success_metric. Extend the strategy-artifact
   in `runtime/handoff-contract.md` and the hub output so success_metric can carry a small set
   of leading input metrics stream 8 can steer by before the lagging result lands. Source:
   Amplitude North Star Framework (metric plus inputs). Coordinate with streams 8 and 9 since
   it touches the contract.

5. Add a proto-persona block per segment. In `segmentation-plan.md` section 2, add optional
   fields per segment: a day-in-the-life line, top one or two objections, and a representative
   quote, drawn only from data or context, never invented, and flagged when illustrative.
   Source: HubSpot and Miro persona and proto-persona templates. This gives stream 4
   copywriters a person to write to without heavy new research.

6. Name the market category or frame in the angle. In `angle-and-offer-framing.md` section 1,
   add an optional `category_frame:` line stating how the reader should file the offer (a
   class, a path, a daily habit). Source: April Dunford, market category. Keep it optional
   given the campaign-level scope.

### Low priority

7. Add an offer-to-profile fit check. In `angle-and-offer-framing.md` section 3, extend the
   empowering check with a one-line fit check: every value claim maps to a stated segment pain
   or gain. Source: Strategyzer fit concept. Pairs naturally with recommendation 1.

8. Make the voice-of-the-customer loop visible in stream 2. Add a one-line note in
   `02-strategy-planning/SKILL.md` inputs that the prior campaign's report-artifact learnings,
   where one exists, are read before segmenting. Source: Gartner voice-of-the-customer
   component. The mechanism already exists at the engine level; this just surfaces it in the
   strategy step.
