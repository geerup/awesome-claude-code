#!/usr/bin/env python3
"""Atomic evidence bank, derived deterministically from data/master.json.

master.json stays the single source of truth (M00 section 1). This script splits
every claim into atomic facts with stable ids, carries status and constraints,
and writes two derived files that writers and checkers cite:

  data/facts.jsonl    one atomic fact per line (schemas/fact.schema.json)
  data/entries.json   roles with exact titles, dates, org (schemas/entries.schema.json)

Both are generated, gitignored, and never hand-edited (the guard hook denies it).
Every record carries master_sha256 so a stale bank is detectable.

Usage: python3 engine/scripts/fact_bank.py [--check]
  --check  exit 1 if the files on disk are missing or stale, write nothing.
"""
import hashlib
import json
import re
import sys
from pathlib import Path

ENGINE = Path(__file__).resolve().parent.parent
MASTER = ENGINE / "data" / "master.json"
FACTS_OUT = ENGINE / "data" / "facts.jsonl"
ENTRIES_OUT = ENGINE / "data" / "entries.json"

ORG_PREFIX = {
    "Maharat": "MAH",
    "Canonical (Ubuntu)": "CAN",
    "Mindvalley": "MVL",
    "Goodwall": "GDW",
    "Payd": "PAY",
    "Agiliux": "AGI",
}
AGENCY_PREFIX = "AGY"

# Sources that are exported platform or company data. Anything else (CV, M00,
# peer recommendation) is attested by San and flagged for interview prep.
DOCUMENTARY_SOURCES = re.compile(
    r"Sprout|Salesforce|GA4|Meltwater|YouTube|LinkedIn export|LinkedIn competitor|Gartner"
    r"|analytics|platform data|company data|PAYD data|Agiliux data|agency reports"
    r"|event data|email platform|campaign docs|PR tracking|outreach data|influencer sheet",
    re.I,
)

# Standing rule (master.json meta.standing_rules): location stays out of outbound materials.
LOCATION_TERMS = re.compile(r"\b(Tallinn|Estonia)\b")

# Same token grammar as evals/machine_check.py: identifiers (R01, B2B) are not metrics.
NUM_TOKEN = re.compile(r"(?<![\w.-])\d[\d,.]*[KMB+x%]*")
# Capitalised words and acronyms; checkers compare line entities against these.
ENTITY_TOKEN = re.compile(r"\b[A-Z][\w'&.]*[\w&]|\b[A-Z]\b")


def master_sha256() -> str:
    return hashlib.sha256(MASTER.read_bytes()).hexdigest()


def normalize_number(token: str) -> str:
    return token.rstrip(".,+").lstrip("~")


def numbers_in(text: str) -> list[str]:
    seen = []
    for tok in NUM_TOKEN.findall(text):
        n = normalize_number(tok)
        if n and n not in seen:
            seen.append(n)
    return seen


def entities_in(text: str) -> list[str]:
    seen = []
    for tok in ENTITY_TOKEN.findall(text):
        if tok not in seen:
            seen.append(tok)
    return seen


def split_atoms(claim: str) -> list[str]:
    """Split a semicolon-joined claim into atoms; never split inside parentheses."""
    atoms, depth, buf = [], 0, []
    for ch in claim:
        depth += ch == "("
        depth -= ch == ")"
        if ch == ";" and depth == 0:
            atoms.append("".join(buf).strip())
            buf = []
        else:
            buf.append(ch)
    atoms.append("".join(buf).strip())
    return [a for a in atoms if a]


def status_for(source: str) -> str:
    return "Folder" if DOCUMENTARY_SOURCES.search(source or "") else "San only"


def make_fact(fact_id, entry_id, claim, source, themes, constraints=(), usable=True):
    return {
        "fact_id": fact_id,
        "entry_id": entry_id,
        "claim": claim,
        "numbers": numbers_in(claim),
        "entities": entities_in(claim),
        "themes": list(themes),
        "source": source,
        "status": status_for(source),
        "usable": usable,
        "constraints": list(constraints),
    }


def claim_constraints(win: dict) -> list[str]:
    out = []
    for key in ("hard_rule", "language_rule", "framing_rule", "scope_note", "status"):
        if win.get(key):
            out.append(f"{key}: {win[key]}")
    return out


def build(master: dict) -> tuple[list[dict], dict]:
    facts: list[dict] = []
    entries: dict = {}

    ident = master["identity"]
    for key in ("name_western_global", "name_mena", "email", "website", "linkedin_slug",
                "education"):
        facts.append(make_fact(f"ID-{key}", "identity", ident[key], "CV", ["identity"]))
    facts.append(make_fact("ID-languages", "identity", ", ".join(ident["languages"]), "CV",
                           ["identity", "languages"]))
    facts.append(make_fact("ID-certifications", "identity", ", ".join(ident["certifications"]),
                           "CV", ["identity", "certifications"]))
    facts.append(make_fact("ID-base", "identity", ident["base"], "CV", ["identity"],
                           ["standing rule: location omitted from outbound materials"],
                           usable=False))

    pos = master["positioning"]
    for key in ("sentence", "cv_descriptor", "agentic_register"):
        facts.append(make_fact(f"POS-{key}", "positioning", pos[key], "M00; CV", ["positioning"]))

    for key, stat in master["headline_stats"].items():
        text = stat["value"]
        if stat.get("context"):
            text = f"{text}. {stat['context']}"
        constraints = ["career combined headline; never inside a single role section"]
        if key == "canonical_organic_community":
            constraints = ["Canonical only"]
        facts.append(make_fact(f"HL-{key}", "headline", text, stat.get("source", ""),
                               ["headline"], constraints))
        if stat.get("precise"):
            facts.append(make_fact(f"HL-{key}-precise", "headline", stat["precise"],
                                   stat.get("source", ""), ["headline"], constraints))

    for exp in master["experience"]:
        prefix = ORG_PREFIX.get(exp["org"], AGENCY_PREFIX)
        entries[prefix] = {
            "entry_id": prefix,
            "org": exp["org"],
            "title": exp["title"],
            "dates": exp["dates"],
            "rules": [r for r in (exp.get("title_rule"), exp.get("scope_rule")) if r],
        }
        for field in ("org", "title", "dates", "budget", "reporting", "sector", "scope_exact",
                      "significance"):
            if exp.get(field):
                facts.append(make_fact(f"{prefix}-{field}", prefix, exp[field], "CV", [field]))
        if exp.get("location"):
            for i, atom in enumerate(re.split(r"(?<=\.)\s+", exp["location"]), 1):
                atom = atom.rstrip(".")
                hidden = bool(LOCATION_TERMS.search(atom))
                facts.append(make_fact(
                    f"{prefix}-location-{i}", prefix, atom, "CV", ["location"],
                    ["standing rule: location omitted from outbound materials"] if hidden else [],
                    usable=not hidden))
        for category, wins in exp.get("wins_by_category", {}).items():
            for n, win in enumerate(wins, 1):
                atoms = split_atoms(win["claim"])
                for k, atom in enumerate(atoms):
                    suffix = chr(ord("a") + k) if len(atoms) > 1 else ""
                    facts.append(make_fact(f"{prefix}-{category}-{n}{suffix}", prefix, atom,
                                           win.get("source", ""), [category],
                                           claim_constraints(win)))

    for i, t in enumerate(master["testimonials"], 1):
        facts.append(make_fact(f"TST-{i}", "testimonials",
                               f"{t['name']}, {t['role']}: \"{t['quote']}\"", t["source"],
                               ["testimonial"]))
    for i, s in enumerate(master["speaking_and_publications"], 1):
        facts.append(make_fact(f"SPK-{i}", "speaking", s, "CV", ["speaking"]))
    for key, s in master["skills"].items():
        facts.append(make_fact(f"SK-{key}", "skills", s, "CV", ["skills"]))

    ids = [f["fact_id"] for f in facts]
    dupes = {i for i in ids if ids.count(i) > 1}
    if dupes:
        raise ValueError(f"duplicate fact ids: {sorted(dupes)}")
    return facts, entries


def load() -> tuple[dict[str, dict], dict, str]:
    """In-memory bank for checkers: always current with master.json, no file needed."""
    digest = master_sha256()
    facts, entries = build(json.loads(MASTER.read_text()))
    return {f["fact_id"]: f for f in facts}, entries, digest


def render() -> tuple[str, str]:
    facts, entries, digest = load()
    facts_text = "".join(
        json.dumps({**f, "master_sha256": digest}, ensure_ascii=False) + "\n"
        for f in facts.values())
    entries_text = json.dumps({"master_sha256": digest, "entries": entries}, indent=2,
                              ensure_ascii=False) + "\n"
    return facts_text, entries_text


def main(argv) -> int:
    facts_text, entries_text = render()
    if "--check" in argv:
        current = (FACTS_OUT.exists() and FACTS_OUT.read_text() == facts_text
                   and ENTRIES_OUT.exists() and ENTRIES_OUT.read_text() == entries_text)
        print("bank current" if current else "bank missing or stale: run fact_bank.py")
        return 0 if current else 1
    FACTS_OUT.write_text(facts_text)
    ENTRIES_OUT.write_text(entries_text)
    print(f"wrote {facts_text.count(chr(10))} facts and {len(json.loads(entries_text)['entries'])}"
          f" entries from master.json {json.loads(entries_text)['master_sha256'][:12]}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
