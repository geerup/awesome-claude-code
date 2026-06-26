# Source-Backed Answer Example

Request: Compare two vendors for a specific workflow.

Use this structure:

## Files read

- `sources.yml`
- `vendors.md`
- `references/integration-checklist.md` when implementation or launch readiness is requested

## Recommendation

Give the safest source-backed option for the requested workflow. If the evidence is weak, say
that a vendor-access step is required before implementation.

## Source-backed comparison

Compare only facts present in the vendor files and source URLs. Mention docs access, docs
confidence, source quality, license, and fit.

## Unknowns

List every missing endpoint shape, auth detail, SDK claim, compliance claim, pricing claim, or
production behavior as `Unknown from public docs` or `Needs vendor access`.

## Validation steps

Include sandbox or test-account checks, retry and idempotency checks, logging and privacy
checks, a license check, and a production approval gate.

Avoid:

- Inventing endpoint paths.
- Claiming support for flows not in the source-backed notes.
- Treating a blog or directory as ground truth.
- Giving live-action instructions for high-risk flows without explicit approval.

Category: arabic-nlp
