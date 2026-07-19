# outputs/ (gated)

Nothing in this directory publishes, sends, submits, or spends without San's explicit yes. No auto-send path exists in this codebase; sending is a manual act by San, outside the system.

- `gated/` holds packs that passed machine evals and LLM QA review and now wait at the gate.
- Every file carries the gate header defined in `evals/llm-qa-rubric.md`.
- Approvals and rejections are logged in `log/decisions.md`.
