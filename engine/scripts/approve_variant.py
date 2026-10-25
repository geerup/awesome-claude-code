#!/usr/bin/env python3
"""The only write path into data/variants.jsonl (the guard hook denies every other).

A variant is an approved phrasing of one or more atomic facts. Writers assemble
lines from approved variants; anything new is marked proposed and goes to San.
This script records San's approval, it never grants it: every variant must name
the log/decisions.md entry where San said yes, and must pass the same hard-rule
and grounding checks a draft line does.

Usage:
  python3 engine/scripts/approve_variant.py --variant-id V-CAN-pipeline-1 \
      --fact-ids CAN-pipeline-1a,CAN-pipeline-1c --angle commercial-impact \
      --text "..." --decision-ref "<exact '## ' heading in log/decisions.md>" \
      --approved-on 2026-10-25
  python3 engine/scripts/approve_variant.py --batch variants.pending.jsonl
Exit 0 = all appended, 1 = nothing appended (any failure rejects the whole batch).
"""
import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import check_claims  # noqa: E402
import fact_bank  # noqa: E402

DECISIONS = fact_bank.ENGINE / "log" / "decisions.md"


def decision_headings() -> set[str]:
    return {line[3:].strip() for line in DECISIONS.read_text().splitlines()
            if line.startswith("## ")}


def validate(variant: dict, facts: dict, existing: dict, headings: set[str]) -> list[str]:
    errors = check_claims.schema_errors(variant, "variant.schema.json")
    if errors:
        return errors
    if variant["variant_id"] in existing:
        errors.append(f"{variant['variant_id']} already exists; variants are append-only")
    if variant["decision_ref"] not in headings:
        errors.append(f"decision_ref not found as a heading in log/decisions.md: "
                      f"'{variant['decision_ref']}'")
    cited = []
    for fid in variant["fact_ids"]:
        fact = facts.get(fid)
        if fact is None:
            errors.append(f"unknown fact_id '{fid}'")
        elif not fact["usable"]:
            errors.append(f"fact '{fid}' is not usable")
        else:
            cited.append(fact)
    entry_ids = {f["entry_id"] for f in cited}
    section = {"kind": "role", "entry_id": entry_ids.pop()} if len(entry_ids) == 1 \
        else {"kind": "other"}
    errors += check_claims.check_text(variant["text"], cited, section)
    return [f"{variant['variant_id']}: {e}" for e in errors]


def main(argv) -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--batch", type=Path)
    ap.add_argument("--variant-id")
    ap.add_argument("--fact-ids")
    ap.add_argument("--angle")
    ap.add_argument("--text")
    ap.add_argument("--decision-ref")
    ap.add_argument("--approved-on")
    args = ap.parse_args(argv[1:])

    if args.batch:
        pending = [json.loads(x) for x in args.batch.read_text().splitlines() if x.strip()]
    else:
        pending = [{
            "variant_id": args.variant_id,
            "fact_ids": (args.fact_ids or "").split(",") if args.fact_ids else [],
            "angle": args.angle, "text": args.text, "status": "approved",
            "approved_by": "San", "decision_ref": args.decision_ref,
            "approved_on": args.approved_on,
        }]

    facts, _, _ = fact_bank.load()
    existing = check_claims.load_variants()
    headings = decision_headings()
    errors = []
    for v in pending:
        errors += validate(v, facts, existing, headings)
        existing[v.get("variant_id")] = v
    if errors:
        print("REJECTED, nothing appended:")
        for e in errors:
            print("  " + e)
        return 1
    with check_claims.VARIANTS.open("a") as fh:
        for v in pending:
            fh.write(json.dumps(v, ensure_ascii=False) + "\n")
    print(f"appended {len(pending)} approved variant(s) to data/variants.jsonl")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
