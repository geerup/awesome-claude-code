"""Eval cases for the claim checker: the approved v1 CV passes, each hard rule bites."""
import check_claims
import fact_bank
import pytest
from conftest import find_line


def statuses(report):
    return {r["line_id"]: r for r in report["lines"]}


def test_approved_v1_cv_passes_clean(draft):
    report = check_claims.check_draft(draft)
    assert report["draft_errors"] == []
    assert report["summary"] == {"pass": 15, "fail": 0, "needs_human": 0}


def test_fact_ids_are_unique_and_stable():
    facts, entries, _ = fact_bank.load()
    assert "CAN-pipeline-1c" in facts
    assert entries["MAH"]["title"] == "Senior Director, Marketing, Communications & Product"


def test_location_facts_are_unusable():
    facts, _, _ = fact_bank.load()
    assert not facts["ID-base"]["usable"]
    assert not facts["CAN-location-1"]["usable"]
    assert facts["CAN-location-2"]["usable"]


def mutate(draft, line_id, **changes):
    line = find_line(draft, line_id)
    line.update(changes)
    line.pop("variant_id", None)
    line["proposed"] = True
    return statuses(check_claims.check_draft(draft))[line_id]


@pytest.mark.parametrize("line_id,text,expect", [
    ("CAN-3", "Turned social into a pipeline channel: $6M+ enterprise pipeline influenced.",
     "number '6M' not in cited facts"),
    ("CAN-3", "Turned social into a channel; $5M+ enterprise pipeline generated.",
     "pipeline 'generated'"),
    ("CAN-3", "Turned social into a channel; $5M+ enterprise pipeline for sales.",
     "pipeline figure without 'influenced'"),
    ("CAN-1", "Led marketing communications — content and social.", "em dash"),
    ("CAN-1", "Led marketing communications – content and social.", "en dash"),
    ("CAN-1", "Led a team of 12 across content and social.", "headcount"),
    ("CAN-1", "Owned GTM for marketing communications and social media campaigns.",
     "did not own GTM"),
    ("MAH-1", "Built multi-agent content and campaign pipelines, live with 21 agents.",
     "NOT live"),
    ("MAH-2", "Orchestrated Arabic-first lifecycle marketing across the funnel.",
     "banned word 'orchestrated'"),
    ("MAH-2", "Delivered Arabic-first lifecycle marketing across the funnel.", "banned opener"),
    ("CAN-4", "Directed launches with Dell, Intel, NVIDIA, and Microsoft.",
     "entity 'Microsoft' not in cited facts"),
    ("CAN-1", "Led marketing communications from Tallinn for the company.", "location term"),
])
def test_hard_rules_fail(draft, line_id, text, expect):
    result = mutate(draft, line_id, text=text)
    assert result["status"] == "fail"
    assert any(expect in r for r in result["reasons"]), result["reasons"]


def test_unusable_fact_fails(draft):
    result = mutate(draft, "CAN-1", fact_ids=["CAN-scope_exact", "CAN-location-1"])
    assert any("not usable" in r for r in result["reasons"])


def test_cross_entry_attribution_fails(draft):
    # 3M grown 3x is Canonical only; citing it in the Maharat section fails.
    result = mutate(draft, "MAH-2", fact_ids=["MAH-marketing-1", "CAN-audience-1a"])
    assert any("belongs to CAN" in r for r in result["reasons"])


def test_headline_fact_inside_role_fails(draft):
    result = mutate(draft, "CAN-2", fact_ids=["CAN-audience-1a", "HL-career_combined_audience"])
    assert any("career combined" in r for r in result["reasons"])


def test_line_without_fact_ids_fails(draft):
    result = mutate(draft, "CAN-1", fact_ids=[])
    assert any("no fact_ids" in r for r in result["reasons"])


def test_proposed_wording_needs_human(draft):
    line = find_line(draft, "CAN-1")
    line["text"] = "Led marketing communications and social media campaigns."
    line["variant_id"] = None
    line["proposed"] = True
    assert statuses(check_claims.check_draft(draft))["CAN-1"]["status"] == "needs_human"


def test_variant_drift_needs_human(draft):
    find_line(draft, "CAN-1")["text"] = "Led marketing communications and social campaigns."
    assert statuses(check_claims.check_draft(draft))["CAN-1"]["status"] == "needs_human"


def test_no_variant_and_not_proposed_fails(draft):
    find_line(draft, "CAN-1")["variant_id"] = None
    assert statuses(check_claims.check_draft(draft))["CAN-1"]["status"] == "fail"


@pytest.mark.parametrize("field,value", [
    ("title", "Senior Director of Marketing and Communications"),
    ("dates", "2024 to Present"),
])
def test_role_heading_must_match_entries(draft, field, value):
    draft["sections"][2][field] = value
    report = check_claims.check_draft(draft)
    assert any(f"MAH {field}" in e for e in report["draft_errors"])


def test_market_name_rule(draft):
    draft["name"] = "Ahmed (San) El Sanhoury"
    assert check_claims.check_draft(draft)["draft_errors"]


def test_schema_violation_is_a_draft_error(draft):
    del draft["sections"][2]["lines"][0]["fact_ids"]
    assert check_claims.check_draft(draft)["draft_errors"]
