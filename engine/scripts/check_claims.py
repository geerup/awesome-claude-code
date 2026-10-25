#!/usr/bin/env python3
"""Deterministic claim checker for writer drafts (outputs/**/draft.json).

Runs before anything renders. The validate_draft hook calls it on every write, and
R01's machine pass runs it from the CLI. Code decides what code can decide; the LLM
entailment pass (R01 judgment) runs after it and only on lines that pass here.

Per line:
  fail         blocks the write: unknown or unusable fact, number or entity absent
               from the cited facts, hard-rule breach (rules/hard.json), cross-entry
               attribution, missing variant and not marked proposed.
  needs_human  goes to San at the gate: proposed wording, or text that drifts from
               its approved variant. Excluded from render until approved.
  pass         every check held.

Usage: python3 engine/scripts/check_claims.py <draft.json> [--write]
  --write  also write factcheck.json next to the draft.
Exit 0 = no fail lines, 1 = fail lines or draft errors, 2 = usage.
"""
import hashlib
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import fact_bank  # noqa: E402

ENGINE = fact_bank.ENGINE
HARD = json.loads((ENGINE / "rules" / "hard.json").read_text())
BRAND = json.loads((ENGINE / "data" / "brand.json").read_text())
VARIANTS = ENGINE / "data" / "variants.jsonl"
SCHEMAS = ENGINE / "schemas"

BANNED_WORDS = [w.lower() for w in BRAND["banned"]["words"]]
NOT_X_BUT_Y = re.compile(r"\bnot\s+(a\s+|an\s+|the\s+)?\w+([ ,]+\w+){0,3},?\s+but\s+", re.I)
# A figure that measures pipeline itself: "$5M+ enterprise pipeline", "lifted pipeline 50%".
PIPELINE_FIGURE = re.compile(
    r"\$[\d.,]+[KMB]?\+?\s+(\w+\s+){0,2}pipeline|pipeline\s+(\w+\s+){0,3}(by\s+)?\d[\d.]*%",
    re.I)
HEADCOUNT = [re.compile(p, re.I) for p in HARD["headcount_patterns"]]
LOCATION = re.compile(r"\b(" + "|".join(HARD["location_terms"]) + r")\b")
SECTION_RULES = {
    k: ([re.compile(p, re.I) for p in v["forbidden_patterns"]], v["reason"])
    for k, v in HARD["section_rules"].items()
}
# A new segment starts at line start or after these marks; its first word is
# capitalised by grammar, not because it names something.
SEGMENT_START = re.compile(r"(^|[.:;·(]\s+|\(|\s-\s)$")
ALLOWED_ENTITIES = set(HARD["entity_allowlist"])
ROLE_KINDS = {"role"}
HEADLINE_FORBIDDEN_KINDS = {"role", "earlier"}


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode()).hexdigest()


def load_variants() -> dict[str, dict]:
    if not VARIANTS.exists():
        return {}
    out = {}
    for raw in VARIANTS.read_text().splitlines():
        if raw.strip():
            v = json.loads(raw)
            out[v["variant_id"]] = v
    return out


def schema_errors(obj, schema_name: str) -> list[str]:
    try:
        import jsonschema
    except ImportError:
        return ["jsonschema is not installed (pip install jsonschema); failing closed"]
    schema = json.loads((SCHEMAS / schema_name).read_text())
    validator = jsonschema.Draft7Validator(schema)
    return [f"schema: {'/'.join(map(str, e.path)) or '<root>'}: {e.message}"
            for e in validator.iter_errors(obj)]


def line_entities(text: str) -> list[str]:
    found = []
    for m in fact_bank.ENTITY_TOKEN.finditer(text):
        if SEGMENT_START.search(text[: m.start()]):
            continue
        found.append(m.group(0))
    return found


def check_text(text: str, cited: list[dict], section: dict) -> list[str]:
    """Hard-rule and grounding checks shared by draft lines and new variants."""
    reasons = []
    low = text.lower()
    for ch, name in HARD["forbidden_characters"].items():
        if ch in text:
            reasons.append(f"{name} in text; use a hyphen or restructure")
    for w in BANNED_WORDS:
        if re.search(rf"\b{re.escape(w)}\b", low):
            reasons.append(f"banned word '{w}' (brand.json)")
    if re.match(r"^\s*(" + "|".join(HARD["banned_openers"]) + r")\b", low):
        reasons.append("banned opener (Boosted/Achieved/Delivered)")
    if NOT_X_BUT_Y.search(text):
        reasons.append("'not X but Y' construction")
    for adj in HARD["pipeline"]["banned_adjacent"]:
        if re.search(rf"pipeline\s+{adj}|{adj}\s+pipeline", low):
            reasons.append(f"pipeline '{adj}': pipeline is always 'influenced'")
    for sentence in re.split(r"(?<=[.;])\s+", text):
        if PIPELINE_FIGURE.search(sentence) and "influenced" not in sentence.lower():
            reasons.append("pipeline figure without 'influenced'")
    for pat in HEADCOUNT:
        if pat.search(text):
            reasons.append(f"headcount language ('{pat.search(text).group(0)}'): stays out")
    if LOCATION.search(text):
        reasons.append("location term: standing rule omits location from outbound materials")

    entry_id = section.get("entry_id")
    if entry_id in SECTION_RULES:
        patterns, why = SECTION_RULES[entry_id]
        for pat in patterns:
            if pat.search(text):
                reasons.append(f"'{pat.search(text).group(0)}' in {entry_id} section: {why}")

    if not cited:
        return reasons
    cited_numbers = {n for f in cited for n in f["numbers"]}
    for tok in fact_bank.numbers_in(text):
        if tok not in cited_numbers:
            reasons.append(f"number '{tok}' not in cited facts")
    cited_text = " ".join(f["claim"] for f in cited)
    for ent in line_entities(text):
        if ent not in ALLOWED_ENTITIES and ent not in cited_text:
            reasons.append(f"entity '{ent}' not in cited facts")
    return reasons


def check_line(line: dict, section: dict, facts: dict, variants: dict) -> dict:
    reasons, soft = [], []
    ids = line.get("fact_ids") or []
    if not ids:
        reasons.append("no fact_ids: every line cites the bank")
    cited = []
    for fid in ids:
        fact = facts.get(fid)
        if fact is None:
            reasons.append(f"unknown fact_id '{fid}'")
            continue
        if not fact["usable"]:
            reasons.append(f"fact '{fid}' is not usable ({'; '.join(fact['constraints'])})")
        if section["kind"] in ROLE_KINDS and fact["entry_id"] != section.get("entry_id"):
            reasons.append(f"fact '{fid}' belongs to {fact['entry_id']}, cited in "
                           f"{section.get('entry_id')} section")
        if section["kind"] in HEADLINE_FORBIDDEN_KINDS and fact["entry_id"] == "headline":
            reasons.append(f"headline fact '{fid}' is career combined; never inside a role")
        cited.append(fact)

    reasons += check_text(line["text"], cited, section)

    vid = line.get("variant_id")
    if vid:
        variant = variants.get(vid)
        if variant is None:
            reasons.append(f"unknown variant_id '{vid}'")
        else:
            if sorted(variant["fact_ids"]) != sorted(ids):
                reasons.append(f"fact_ids differ from variant {vid}: {variant['fact_ids']}")
            if variant["text"] != line["text"]:
                soft.append(f"text drifts from approved variant {vid}; San approves the new"
                            " wording via approve_variant.py")
    elif line.get("proposed"):
        soft.append("proposed wording: excluded from render until San approves it")
    else:
        reasons.append("no approved variant_id and not marked proposed")

    status = "fail" if reasons else ("needs_human" if soft else "pass")
    return {"line_id": line["line_id"], "status": status, "reasons": reasons + soft}


def check_draft(draft: dict) -> dict:
    facts, entries, master_digest = fact_bank.load()
    variants = load_variants()
    errors = schema_errors(draft, "draft.schema.json")
    lines_out = []
    if not errors:
        ident = {"MENA": "ID-name_mena", "western_global": "ID-name_western_global"}
        expected_name = facts[ident[draft["market"]]]["claim"]
        if draft["name"] != expected_name:
            errors.append(f"name '{draft['name']}' must be '{expected_name}' for "
                          f"{draft['market']} materials")
        seen_ids = set()
        for section in draft["sections"]:
            if section["kind"] == "role":
                entry = entries.get(section["entry_id"])
                if entry is None:
                    errors.append(f"unknown entry_id '{section['entry_id']}'")
                else:
                    for field in ("title", "org", "dates"):
                        if section[field] != entry[field]:
                            errors.append(f"{section['entry_id']} {field} '{section[field]}' "
                                          f"must be exactly '{entry[field]}'")
            lines = list(section["lines"])
            if section.get("subtitle"):
                lines.insert(0, section["subtitle"])
            for line in lines:
                if line["line_id"] in seen_ids:
                    errors.append(f"duplicate line_id '{line['line_id']}'")
                seen_ids.add(line["line_id"])
                lines_out.append(check_line(line, section, facts, variants))
    summary = {s: sum(1 for r in lines_out if r["status"] == s)
               for s in ("pass", "fail", "needs_human")}
    return {"master_sha256": master_digest, "summary": summary, "draft_errors": errors,
            "lines": lines_out}


def report_for(path: Path, text: str) -> dict:
    try:
        draft = json.loads(text)
    except json.JSONDecodeError as exc:
        report = {"master_sha256": fact_bank.master_sha256(),
                  "summary": {"pass": 0, "fail": 0, "needs_human": 0},
                  "draft_errors": [f"invalid JSON: {exc}"], "lines": []}
    else:
        report = check_draft(draft)
    return {"draft": str(path.name), "draft_sha256": sha256_text(text), **report}


def blocking(report: dict) -> list[str]:
    out = [f"draft: {e}" for e in report["draft_errors"]]
    for r in report["lines"]:
        if r["status"] == "fail":
            out.append(f"{r['line_id']}: " + "; ".join(r["reasons"]))
    return out


def main(argv) -> int:
    args = [a for a in argv[1:] if not a.startswith("--")]
    if len(args) != 1:
        print(__doc__)
        return 2
    path = Path(args[0])
    report = report_for(path, path.read_text())
    if "--write" in argv:
        (path.parent / "factcheck.json").write_text(json.dumps(report, indent=2) + "\n")
    s = report["summary"]
    print(f"{path}: {s['pass']} pass, {s['fail']} fail, {s['needs_human']} needs_human, "
          f"{len(report['draft_errors'])} draft errors")
    for r in report["lines"]:
        if r["status"] != "pass":
            print(f"  [{r['status']}] {r['line_id']}: " + "; ".join(r["reasons"]))
    for e in report["draft_errors"]:
        print(f"  [draft] {e}")
    return 1 if blocking(report) else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
