"""Tests for ``scripts/check_gene_validity.py`` (#10179).

``Genetic.validity`` holds a ClinGen-ladder tier. When the entry cites a ClinGen
``CGGV:`` assertion, the tier is already written down in the cached assertion,
so the audit can compare the two without judgement. These tests pin the rules
that keep that comparison honest: a tier belongs to a gene-disease *pair*, so an
assertion for another disease must never fill or contradict the slot.
"""

import sys
from pathlib import Path

import pytest

# Inline the path rather than assigning ROOT first, for ruff's E402 allowance
# (same preamble as tests/test_causal_targets.py, #9964).
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

import check_gene_validity as mod
from check_gene_validity import assess, parse_assertion

ROOT = Path(__file__).resolve().parents[1]

ALS22 = "CGGV:assertion_aaaa-2025-03-27T160000.000Z"
MACRO = "CGGV:assertion_bbbb-2023-11-06T170000.000Z"
ALS22_AR = "CGGV:assertion_cccc-2024-01-01T000000.000Z"


def _cache_file(gene, hgnc, disease, mondo, moi, classification):
    return (
        "---\n"
        'database: "ClinGen"\n'
        "---\n\n"
        "## Evidence summary\n\n"
        "Narrative | with | pipes that must not parse as a row.\n\n"
        "## Gene-disease validity\n\n"
        "| Gene | HGNC | Disease | MONDO | MOI | Classification | SOP | GCEP "
        "| Classification date |\n"
        "|---|---|---|---|---|---|---|---|---|\n"
        f"| {gene} | {hgnc} | {disease} | {mondo} | {moi} | {classification} "
        "| SOP10 | Some GCEP | 2025-03-27T16:00:00.000Z |\n\n"
        "## Online report\n\n- Curation ID: CCID:000001\n"
    )


@pytest.fixture
def cache(tmp_path):
    rows = {
        ALS22: (
            "TUBA4A",
            "HGNC:12407",
            "ALS type 22",
            "MONDO:0014531",
            "AD",
            "Moderate",
        ),
        MACRO: (
            "TUBA4A",
            "HGNC:12407",
            "macrothrombocytopenia",
            "MONDO:0000001",
            "AD",
            "Limited",
        ),
        ALS22_AR: (
            "TUBA4A",
            "HGNC:12407",
            "ALS type 22",
            "MONDO:0014531",
            "AR",
            "Definitive",
        ),
    }
    for curie, row in rows.items():
        mod.cache_path(curie, tmp_path).write_text(_cache_file(*row), encoding="utf-8")
    return tmp_path


def _entry(
    *cited, validity=None, relationship="CAUSATIVE", mondo="MONDO:0014531", **extra
):
    record = {
        "name": "TUBA4A",
        "relationship_type": relationship,
        "gene_term": {"term": {"id": "hgnc:12407", "label": "TUBA4A"}},
        "evidence": [{"reference": c} for c in cited],
    }
    if validity:
        record["validity"] = validity
    data = {
        "name": "Probe",
        "disease_term": {"term": {"id": mondo}},
        "genetic": [record],
    }
    data.update(extra)
    return data


def _kinds(findings):
    return sorted((f.kind, f.clingen) for f in findings)


def test_parses_the_validity_row_and_ignores_narrative_pipes():
    text = _cache_file(
        "SOX10", "HGNC:11190", "WS4C", "MONDO:0013202", "AD", "Definitive"
    )
    a = parse_assertion("CGGV:x", text)
    assert (a.gene, a.hgnc, a.mondo, a.moi, a.classification) == (
        "SOX10",
        "hgnc:11190",
        "MONDO:0013202",
        "AD",
        "DEFINITIVE",
    )


def test_every_committed_cggv_cache_file_parses():
    """The parser must read the real cache, not only the fixture's shape."""
    files = sorted((ROOT / "references_cache").glob("CGGV_*.md"))
    assert files, "expected committed CGGV cache files"
    unparsed = [
        f.name
        for f in files
        if parse_assertion(f.stem.replace("_", ":", 1), f.read_text(encoding="utf-8"))
        is None
    ]
    assert unparsed == []


def test_same_disease_assertion_is_a_backfill_candidate(cache):
    findings = assess(_entry(ALS22), "x.yaml", cache)
    assert ("backfill", "MODERATE") in _kinds(findings)


def test_matching_validity_is_clean(cache):
    findings = assess(
        _entry(ALS22, validity="MODERATE", relationship="RISK_FACTOR"), "x.yaml", cache
    )
    assert findings == []


def test_contradicting_validity_is_a_conflict(cache):
    findings = assess(_entry(ALS22, validity="DEFINITIVE"), "x.yaml", cache)
    assert ("conflict", "MODERATE") in _kinds(findings)


def test_assertion_for_another_disease_never_fills_or_contradicts(cache):
    """The gene's second disease is not this entry's tier."""
    findings = assess(_entry(MACRO, validity="DEFINITIVE"), "x.yaml", cache)
    assert findings == [], "a recorded value must not conflict with another disease"

    findings = assess(_entry(MACRO), "x.yaml", cache)
    assert _kinds(findings) == [("other_disease", "LIMITED")]


def test_exact_match_mapping_counts_as_the_entry_disease(cache):
    mappings = {
        "mondo_mappings": [
            {"term": {"id": "MONDO:0000001"}, "mapping_predicate": "skos:exactMatch"}
        ]
    }
    findings = assess(
        _entry(MACRO, mondo="MONDO:9999999", mappings=mappings), "x.yaml", cache
    )
    assert ("backfill", "LIMITED") in _kinds(findings)


def test_broad_match_mapping_does_not(cache):
    mappings = {
        "mondo_mappings": [
            {"term": {"id": "MONDO:0000001"}, "mapping_predicate": "skos:broadMatch"}
        ]
    }
    findings = assess(
        _entry(MACRO, mondo="MONDO:9999999", mappings=mappings), "x.yaml", cache
    )
    assert _kinds(findings) == [("other_disease", "LIMITED")]


def test_subtype_term_counts_as_the_entry_disease(cache):
    subtypes = [{"name": "Macro", "subtype_term": {"term": {"id": "MONDO:0000001"}}}]
    findings = assess(
        _entry(MACRO, mondo="MONDO:9999999", has_subtypes=subtypes), "x.yaml", cache
    )
    assert ("backfill", "LIMITED") in _kinds(findings)


def test_two_tiers_for_the_same_disease_are_ambiguous(cache):
    """Typically two modes of inheritance classified separately."""
    findings = assess(
        _entry(ALS22, ALS22_AR, relationship="RISK_FACTOR"), "x.yaml", cache
    )
    assert _kinds(findings) == [("ambiguous", "DEFINITIVE,MODERATE")]
    assert " AD (" in findings[0].detail and " AR (" in findings[0].detail


def test_either_same_disease_tier_satisfies_a_recorded_value(cache):
    findings = assess(_entry(ALS22, ALS22_AR, validity="DEFINITIVE"), "x.yaml", cache)
    assert findings == []


def test_causative_below_strong_is_overstated(cache):
    findings = assess(_entry(ALS22), "x.yaml", cache)
    assert ("overstated", "MODERATE") in _kinds(findings)


def test_causative_is_not_overstated_by_another_disease(cache):
    findings = assess(_entry(MACRO), "x.yaml", cache)
    assert "overstated" not in {f.kind for f in findings}


def test_uncached_citation_is_reported(cache):
    findings = assess(_entry("CGGV:assertion_zzzz-2020"), "x.yaml", cache)
    assert _kinds(findings) == [("uncached", "")]


def test_gene_match_prefers_hgnc_over_symbol(cache):
    """A record bound to another HGNC id must not match on a shared name."""
    data = _entry(ALS22)
    data["genetic"][0]["gene_term"]["term"] = {"id": "hgnc:1", "label": "TUBA4A"}
    assert assess(data, "x.yaml", cache) == []


def test_symbol_match_when_no_hgnc_is_bound(cache):
    data = _entry(ALS22)
    del data["genetic"][0]["gene_term"]
    assert ("backfill", "MODERATE") in _kinds(assess(data, "x.yaml", cache))


# --- CLI ---------------------------------------------------------------------


def _write_entry(tmp_path, data):
    import yaml

    path = tmp_path / "Probe.yaml"
    path.write_text(yaml.safe_dump(data), encoding="utf-8")
    return path


def test_conflict_fails_the_run_and_report_mode_does_not(
    cache, tmp_path, monkeypatch, capsys
):
    monkeypatch.setattr(mod, "CACHE_DIR", cache)
    path = _write_entry(tmp_path, _entry(ALS22, validity="DEFINITIVE"))

    assert mod.main([str(path)]) == 1
    assert "contradict" in capsys.readouterr().err
    assert mod.main([str(path), "--report"]) == 0


def test_missing_path_is_a_usage_error(tmp_path, capsys):
    assert mod.main([str(tmp_path / "Nope.yaml")]) == 2
    assert "Nope.yaml" in capsys.readouterr().err


def test_committed_kb_has_no_conflicts():
    """The gate itself, over the real KB."""
    assert mod.main(["--kind", "conflict"]) == 0
