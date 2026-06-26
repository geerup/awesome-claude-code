---
name: ab-test-plan
description: Sub-skill of stream 8. Use to design a single-variable A/B test with a clear hypothesis and a stop rule before running it. Triggers on "plan an A/B test," "should we test this," "test the subject line," "test the angle," "set up an experiment." Reasoning only. Tests exactly one variable, ties the hypothesis to the strategy-artifact success_metric, defines a stop rule up front, and stays a proposal: the test only runs once it clears the human gate, and the skill never launches or spends on its own.
---

# A/B Test Plan (stream 8 sub-skill)

Designs a test worth running. Owned by `analytics-reporter`, reasoning mode. One variable,
one hypothesis, one stop rule. A test that changes two things at once teaches nothing, so it
is not allowed here.

## Purpose

Produce a clean test plan: the single variable under test, the hypothesis tied to the
success_metric, the two variants, how traffic splits, what is measured, and the stop rule
that ends the test. The plan is a proposal for the human gate, not a launched test.

## When to use

- A performance-readout surfaced a question worth answering with a controlled test.
- Someone wants to test a subject line, an angle, a creative, a CTA, or a send time.
- Before any test runs, to make sure it is single-variable and has a stop rule.

## Inputs

- The `strategy-artifact`: success_metric (what the test moves), segments, angle.
- The `performance-readout` (if one exists): the finding that motivates the test.
- The active `briefs/` file: any constraint on audience, window, or spend.

If the success_metric is absent, stop and ask. Do not invent the metric the test is judged on.

## Steps

1. Name the one variable under test. If a second variable would change too, narrow the test
   until only one moves. Hold everything else constant.
2. Write the hypothesis: "Changing X to Y will move [success_metric] because [reason]." Tie
   it to the success_metric, not a vanity metric.
3. Define variants: control (A) and one variant (B), differing only in the one variable.
4. Define the split, the audience, and the measurement window.
5. Derive the sample size before launch. State the baseline rate (current value of the
   success_metric), the minimum detectable effect (the smallest change worth detecting), and
   the per-arm sample size that follows from them. Name the method and the significance level:
   either a fixed-horizon test with its significance level (for example 95 percent), or a named
   sequential or Bayesian method. Choose the method and stop rule BEFORE launch, never after.
   No peeking, no stopping early unless the chosen method is sequential or Bayesian.
6. Write the stop rule up front: the sample size or duration that ends the test, and the
   decision threshold on the success_metric. No moving the goalposts after the fact.
7. Mark the plan a human-gate proposal. The test runs only on approval; the skill does not
   launch or spend.
8. Run the skill eval for structure and completeness.

## Output

Use `templates/ab-test-plan.md`. The shape:
- variable_under_test (exactly one),
- hypothesis (tied to the success_metric),
- variants A and B,
- split, audience, window,
- sample_size_and_method (baseline rate, minimum detectable effect, derived per-arm sample
  size, significance level or named sequential or Bayesian method, chosen before launch),
- stop_rule (sample or duration plus the decision threshold),
- human-gate note.

Internal artifact. It does not cross a boundary on its own and it does not launch a test.

## Hard rules

- One variable only. Tie the hypothesis to the success_metric the strategy set, never a
  metric invented after the fact, never a vanity metric.
- Sample size is derived, not guessed: baseline rate plus minimum detectable effect give the
  per-arm sample size. The method and significance level (or named sequential or Bayesian
  method) are chosen before launch. No peeking, no early stop unless the chosen method allows it.
- A stop rule is mandatory and is set before the test runs.
- Propose, do not act. The test launches only through the human gate, per `CLAUDE.md`.
- No em dashes, no tatweel, Western numerals only.
