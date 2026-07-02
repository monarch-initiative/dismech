"""Tests for the NEC-risk disease-class audit (``scripts/nec_risk_audit.py``).

Named Entity Confusion (NEC) is the deep-research failure mode tracked in
issue #3889. This suite exercises the *risk-class flagger* that scans
``kb/disorders`` for the four structural NEC-risk patterns named in the issue
(numbered series, eponym collision, synonym aliasing, acronym ambiguity).

It is the complement of any future test of the per-report gene-identity
cross-check (``src/dismech/preflight_dr.py``, #3902): this file pins the
*detection logic that already lives on ``main``* — the pure ``eponyms_in`` and
``audit`` helpers — so refactors of the audit cannot silently regress the
four NEC-risk categories.

Test cases mirror real documented NEC incidents from #3889:
  * eponym collision  — the Walker-Warburg / Temtamy surname-sharing pattern;
  * synonym aliasing  — the Lichtenstein-Knorr case (a synonym pointing at a
    different eponymous entity);
  * acronym ambiguity — ``MWS`` (Marden-Walker / Mowat-Wilson / Muckle-Wells).
"""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path


ROOT = Path(__file__).parent.parent
SCRIPT_PATH = ROOT / "scripts" / "nec_risk_audit.py"
SPEC = importlib.util.spec_from_file_location("nec_risk_audit", SCRIPT_PATH)
assert SPEC and SPEC.loader
nec_risk_audit = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = nec_risk_audit
SPEC.loader.exec_module(nec_risk_audit)


def _row(name, *, file="X.yaml", label=None, mondo="MONDO:0000001", synonyms=None):
    """Build a row in the shape ``load_entries`` produces."""
    return {
        "file": file,
        "name": name,
        "mondo": mondo,
        "label": name if label is None else label,
        "synonyms": list(synonyms or []),
    }


# --------------------------------------------------------------------------- #
# eponyms_in
# --------------------------------------------------------------------------- #


def test_eponyms_in_hyphenated_pair():
    # Both surnames of a hyphenated eponym are extracted.
    assert nec_risk_audit.eponyms_in("Walker-Warburg syndrome") == {"Walker", "Warburg"}


def test_eponyms_in_single_surname_before_head_noun():
    # A lone capitalized surname directly before a disease head-noun is caught.
    assert nec_risk_audit.eponyms_in("Marfan syndrome") == {"Marfan"}
    assert "Temtamy" in nec_risk_audit.eponyms_in("Temtamy syndrome")


def test_eponyms_in_suppresses_common_descriptors():
    # Capitalized common nouns/descriptors must not be mistaken for surnames.
    assert nec_risk_audit.eponyms_in("Familial Hypercholesterolemia") == set()
    assert nec_risk_audit.eponyms_in("Congenital Muscular Dystrophy") == set()
    # Charcot is deliberately suppressed (recurs as a plain descriptor).
    assert "Charcot" not in nec_risk_audit.eponyms_in("Charcot-Marie-Tooth disease")


def test_eponyms_in_no_eponym_returns_empty():
    assert nec_risk_audit.eponyms_in("Asthma") == set()


# --------------------------------------------------------------------------- #
# audit — NUMBERED_SERIES
# --------------------------------------------------------------------------- #


def test_audit_flags_numbered_series_type_and_prefix():
    rows = [_row("Spinocerebellar ataxia type 3", synonyms=["SCA3"])]
    findings = nec_risk_audit.audit(rows)
    series = findings.get("NUMBERED_SERIES", [])
    assert len(series) == 1
    hits = set(series[0]["hits"])
    assert "type 3" in hits
    assert "SCA3" in hits


def test_audit_numbered_series_matches_roman_numerals():
    rows = [_row("Mucopolysaccharidosis type II")]
    findings = nec_risk_audit.audit(rows)
    assert findings.get("NUMBERED_SERIES")
    assert "type II" in set(findings["NUMBERED_SERIES"][0]["hits"])


# --------------------------------------------------------------------------- #
# audit — EPONYM_COLLISION
# --------------------------------------------------------------------------- #


def test_audit_flags_eponym_collision_across_entries():
    # Two distinct entries sharing the surname "Walker" -> collision on Walker.
    rows = [
        _row("Walker-Warburg syndrome", file="A.yaml"),
        _row("Walker-Smith syndrome", file="B.yaml"),
    ]
    findings = nec_risk_audit.audit(rows)
    collisions = {f["eponym"]: f["files"] for f in findings.get("EPONYM_COLLISION", [])}
    assert "Walker" in collisions
    assert collisions["Walker"] == ["A.yaml", "B.yaml"]


def test_audit_no_collision_for_unique_eponym():
    rows = [
        _row("Marfan syndrome", file="A.yaml"),
        _row("Walker-Warburg syndrome", file="B.yaml"),
    ]
    findings = nec_risk_audit.audit(rows)
    # No surname is shared across the two entries.
    assert findings.get("EPONYM_COLLISION", []) == []


# --------------------------------------------------------------------------- #
# audit — SYNONYM_ALIASING
# --------------------------------------------------------------------------- #


def test_audit_flags_synonym_aliasing():
    # The Lichtenstein-Knorr pattern: a synonym carries a *different* eponym
    # than the primary name -> historical-synonym-maps-elsewhere risk.
    rows = [
        _row(
            "Lichtenstein-Knorr syndrome",
            synonyms=["Boucher-Neuhauser syndrome"],
        )
    ]
    findings = nec_risk_audit.audit(rows)
    aliasing = findings.get("SYNONYM_ALIASING", [])
    assert len(aliasing) == 1
    extra = set(aliasing[0]["alias_eponyms"])
    assert {"Boucher", "Neuhauser"} <= extra
    # The primary-name eponyms must NOT appear as alias eponyms.
    assert "Lichtenstein" not in extra
    assert "Knorr" not in extra


def test_audit_no_aliasing_when_synonym_shares_name_eponym():
    rows = [_row("Marfan syndrome", synonyms=["Marfan disease"])]
    findings = nec_risk_audit.audit(rows)
    assert findings.get("SYNONYM_ALIASING", []) == []


# --------------------------------------------------------------------------- #
# audit — ACRONYM_AMBIGUITY
# --------------------------------------------------------------------------- #


def test_audit_flags_short_acronym_synonym():
    # "MWS" resolves to Marden-Walker / Mowat-Wilson / Muckle-Wells.
    rows = [_row("Mowat-Wilson syndrome", synonyms=["MWS"])]
    findings = nec_risk_audit.audit(rows)
    acr = findings.get("ACRONYM_AMBIGUITY", [])
    assert len(acr) == 1
    assert "MWS" in acr[0]["acronyms"]


def test_audit_ignores_long_lowercase_synonyms_as_acronyms():
    rows = [_row("Mowat-Wilson syndrome", synonyms=["Hirschsprung-associated"])]
    findings = nec_risk_audit.audit(rows)
    assert findings.get("ACRONYM_AMBIGUITY", []) == []


# --------------------------------------------------------------------------- #
# audit — benign entry produces no findings
# --------------------------------------------------------------------------- #


def test_audit_benign_entry_has_no_findings():
    rows = [_row("Asthma", mondo="MONDO:0004979", synonyms=[])]
    findings = nec_risk_audit.audit(rows)
    for cat in (
        "NUMBERED_SERIES",
        "EPONYM_COLLISION",
        "SYNONYM_ALIASING",
        "ACRONYM_AMBIGUITY",
    ):
        assert findings.get(cat, []) == []


# --------------------------------------------------------------------------- #
# integration — runs over the real knowledge base
# --------------------------------------------------------------------------- #


def test_load_entries_returns_well_formed_rows():
    rows = nec_risk_audit.load_entries()
    assert rows, "expected at least one disorder entry"
    expected_keys = {"file", "name", "mondo", "label", "synonyms"}
    for r in rows[:5]:
        assert expected_keys <= set(r)
        assert isinstance(r["synonyms"], list)


def test_audit_over_real_kb_runs_and_returns_known_categories():
    rows = nec_risk_audit.load_entries()
    findings = nec_risk_audit.audit(rows)
    # The audit must always return only the four documented risk classes.
    assert set(findings).issubset(
        {"NUMBERED_SERIES", "EPONYM_COLLISION", "SYNONYM_ALIASING", "ACRONYM_AMBIGUITY"}
    )
    # Every collision finding references more than one distinct file.
    for f in findings.get("EPONYM_COLLISION", []):
        assert len(f["files"]) > 1
