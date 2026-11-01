"""Two disorder entries may share a ``disease_term`` only if both say how (#10113).

Design decisions §3a lets a promoted cancer stratum anchor to its parent's MONDO
term with ``skos:broadMatch`` recorded in ``mappings.mondo_mappings`` (SKOS
predicates read subject to object, so the narrower stratum records its broader
parent as ``broadMatch``). These tests pin the rule that states it: every entry
in a shared group records exactMatch or broadMatch for the term, and at most
one says exactMatch. A group with no exactMatch is legal, and a missing row
never counts as one. The legacy ``skos:narrowMatch`` spelling -- written under
an earlier, internally consistent but non-standard reading of the predicate --
is also accepted while that backlog migrates (dismech#10165, dismech#16243).
"""

import subprocess
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from check_shared_disease_terms import assess_all

ROOT = Path(__file__).parent.parent
SCRIPT = ROOT / "scripts" / "check_shared_disease_terms.py"
BASELINE = ROOT / "tests" / "shared_disease_term_baseline.txt"

CURIE = "MONDO:0005061"


def _entry(*predicates, curie=CURIE):
    doc = {"disease_term": {"term": {"id": curie, "label": "lung adenocarcinoma"}}}
    if predicates:
        doc["mappings"] = {
            "mondo_mappings": [
                {"term": {"id": curie}, "mapping_predicate": p} for p in predicates
            ]
        }
    return doc


def _kinds(docs):
    _, findings = assess_all(docs)
    return sorted((Path(f.path).stem, f.kind) for f in findings)


def test_unshared_term_needs_no_mapping():
    assert _kinds({"a.yaml": _entry()}) == []


def test_parent_exact_and_strata_broad_is_clean():
    """The canonical pattern: a stratum records its broader parent as broadMatch."""
    docs = {
        "parent.yaml": _entry("skos:exactMatch"),
        "s1.yaml": _entry("skos:broadMatch"),
        "s2.yaml": _entry("skos:broadMatch"),
    }
    assert _kinds(docs) == []


def test_all_broad_with_no_parent_entry_is_clean():
    """No parent entry yet (the lung adenocarcinoma strata): legal."""
    docs = {
        "s1.yaml": _entry("skos:broadMatch"),
        "s2.yaml": _entry("skos:broadMatch"),
    }
    assert _kinds(docs) == []


def test_parent_exact_and_strata_legacy_narrow_is_clean():
    """The legacy Cutaneous_Melanoma / BRAF_V600_Mutant_Melanoma spelling.

    ``skos:narrowMatch`` is still accepted on existing entries (dismech#10165,
    dismech#16243) even though new curation should write ``broadMatch``.
    """
    docs = {
        "parent.yaml": _entry("skos:exactMatch"),
        "s1.yaml": _entry("skos:narrowMatch"),
        "s2.yaml": _entry("skos:narrowMatch"),
    }
    assert _kinds(docs) == []


def test_all_legacy_narrow_with_no_parent_entry_is_clean():
    docs = {
        "s1.yaml": _entry("skos:narrowMatch"),
        "s2.yaml": _entry("skos:narrowMatch"),
    }
    assert _kinds(docs) == []


def test_bare_reuse_is_missing_and_never_an_implicit_exact_claim():
    """One stratum with no row must not keep the exact claim by default.

    Under "every entry but one records narrowMatch", the unmapped stratum would
    pass as the exact owner of the parent term. It must be reported instead.
    """
    docs = {"s1.yaml": _entry("skos:narrowMatch"), "s2.yaml": _entry()}
    assert _kinds(docs) == [("s2", "missing")]


def test_two_unmapped_entries_both_fail():
    assert _kinds({"a.yaml": _entry(), "b.yaml": _entry()}) == [
        ("a", "missing"),
        ("b", "missing"),
    ]


def test_two_exact_claims_are_both_reported():
    docs = {"a.yaml": _entry("skos:exactMatch"), "b.yaml": _entry("skos:exactMatch")}
    assert _kinds(docs) == [("a", "extra_exact"), ("b", "extra_exact")]


@pytest.mark.parametrize(
    "predicate",
    ["skos:closeMatch", "skos:relatedMatch", "skos:narrowmatch", "narrowMatch", ""],
)
def test_other_predicates_and_misspellings_are_rejected(predicate):
    docs = {"a.yaml": _entry("skos:exactMatch"), "b.yaml": _entry(predicate)}
    assert _kinds(docs) == [("b", "bad_predicate")]


def test_wrong_case_gets_the_canonical_spelling_as_its_hint():
    docs = {"a.yaml": _entry("skos:exactMatch"), "b.yaml": _entry("skos:narrowmatch")}
    _, findings = assess_all(docs)
    assert "write skos:narrowMatch" in findings[0].detail


def test_conflicting_member_is_not_counted_as_an_exact_claimant():
    """Two rows for one CURIE with different predicates is ``conflicting``.

    Its exactMatch row is not counted toward ``extra_exact``, so ``a`` (the one
    valid exact claim) is clean and the group fails only on ``b``. That is
    enough: ``b`` must be repaired to one predicate either way, and if it keeps
    exactMatch the next run reports both as ``extra_exact``.
    """
    docs = {
        "a.yaml": _entry("skos:exactMatch"),
        "b.yaml": _entry("skos:narrowMatch", "skos:exactMatch"),
    }
    assert _kinds(docs) == [("b", "conflicting")]


def test_mapping_to_a_different_curie_does_not_count():
    other = _entry("skos:narrowMatch", curie="MONDO:0005233")
    other["disease_term"] = {"term": {"id": CURIE}}
    docs = {"a.yaml": _entry("skos:exactMatch"), "b.yaml": other}
    assert _kinds(docs) == [("b", "missing")]


def test_new_member_of_a_grandfathered_group_is_a_new_finding(monkeypatch, capsys):
    """Baseline rows are per member, so a grandfathered group admits no newcomer."""
    import check_shared_disease_terms as mod

    docs = {"kb/disorders/a.yaml": _entry(), "kb/disorders/b.yaml": _entry()}
    monkeypatch.setattr(mod, "load_disorders", lambda: docs)
    monkeypatch.setattr(
        mod,
        "load_baseline",
        lambda: {f"{CURIE}\tkb/disorders/a.yaml\tmissing"},
    )
    assert mod.main([]) == 1
    out = capsys.readouterr().out
    assert "missing: b" in out
    assert "missing: a" not in out


def test_fixed_baseline_row_is_reported_without_failing(monkeypatch, capsys):
    import check_shared_disease_terms as mod

    docs = {
        "kb/disorders/a.yaml": _entry("skos:exactMatch"),
        "kb/disorders/b.yaml": _entry("skos:narrowMatch"),
    }
    monkeypatch.setattr(mod, "load_disorders", lambda: docs)
    monkeypatch.setattr(
        mod, "load_baseline", lambda: {f"{CURIE}\tkb/disorders/b.yaml\tmissing"}
    )
    assert mod.main([]) == 0
    assert "no longer match" in capsys.readouterr().out


def test_baseline_rows_are_well_formed():
    rows = [
        line
        for line in BASELINE.read_text(encoding="utf-8").splitlines()
        if line.strip() and not line.startswith("#")
    ]
    assert rows == sorted(set(rows)), "baseline must be sorted and duplicate-free"
    for row in rows:
        curie, path, kind = row.split("\t")
        assert curie.startswith("MONDO:")
        assert path.startswith("kb/disorders/") and path.endswith(".yaml")
        assert kind in {"missing", "bad_predicate", "conflicting", "extra_exact"}


@pytest.mark.ci_step_twin("scripts/check_shared_disease_terms.py")
def test_committed_kb_has_no_new_shared_disease_terms():
    """The gate itself, over the real KB."""
    result = subprocess.run(
        [sys.executable, str(SCRIPT)],
        capture_output=True,
        text=True,
        cwd=ROOT,
        check=False,
    )
    assert result.returncode == 0, result.stdout + result.stderr
