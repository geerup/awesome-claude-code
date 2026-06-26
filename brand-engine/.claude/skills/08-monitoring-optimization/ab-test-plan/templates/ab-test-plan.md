# A/B Test Plan

Internal artifact. Owned by analytics-reporter. One variable, one hypothesis, one stop rule.
A proposal for the human gate, not a launched test. The skill never launches or spends on its own.

## Envelope

- campaign_id:
- produced_by: analytics-reporter
- stream: 8 monitoring and optimization
- status: draft | qa-passed
- motivated by: (the performance-readout finding, if any)

## Variable under test (exactly one)

Name the single variable that changes between A and B. If a second variable would also move,
narrow the test until only one moves. Everything else is held constant.

- variable_under_test:

## Hypothesis (tied to the success_metric)

Write it in one line: "Changing X to Y will move [success_metric] because [reason]."
Tie it to the success_metric the strategy-artifact set, never a vanity metric.
If the strategy-artifact has no success_metric, stop and ask. Do not invent one.

- success_metric (restated from the strategy-artifact):
- hypothesis:

## Variants

| Variant | Description | The one thing that differs |
|---|---|---|
| A (control) |  |  |
| B |  |  |

## Split, audience, window

- split: (e.g. 50/50)
- audience: (segment from the strategy-artifact)
- window: (start date to end date, Western numerals)

## Sample size and method (derived before the test runs)

Derive the sample size from the baseline rate and the minimum detectable effect. Do not guess
a sample size. Name the inference method and the significance level, or the named sequential or
Bayesian method. The method and the stop rule are chosen BEFORE launch, never after, so there
is no peeking and no early stop unless the chosen method is sequential or Bayesian.

- baseline rate (current value of the success_metric):
- minimum detectable effect (smallest change worth detecting, absolute or relative):
- derived per-arm sample size (from baseline and MDE):
- significance level or method: (e.g. fixed-horizon at 95 percent, or a named sequential or Bayesian method)
- chosen before launch: yes (method and stop rule fixed up front, no peeking)

## Stop rule (set before the test runs)

The sample size or duration that ends the test, and the decision threshold on the
success_metric. No moving the goalposts after the fact.

- stop condition (sample size or duration):
- decision threshold (on the success_metric):
- what happens at the threshold: (declare B the winner, keep A, or inconclusive)

## Human-gate proposal

This plan is a proposal. The test runs only after the human gate approves it. The skill does
not launch the test, change a live campaign, or spend.

- spend_on_approval (if any, with currency and window):
- flips_live: one plain sentence of what approving this test does

## Open items

- Anything unresolved (instrumentation gap, tool not yet approved, audience not yet sized).
