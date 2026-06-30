"""Tests for the deterministic phenopacket match-quality eval harness.

These run against a small hermetic temp KB (a couple of minimal disorder files)
rather than the full kb/disorders tree, so resolution stays fast and the
assertions do not drift as the real KB grows.
"""

from pathlib import Path

import pytest
import yaml

from phenoagent.eval import (
    aggregate_results,
    build_disease_index,
    evaluate_phenopacket,
    extract_ground_truth_disease,
    main,
    render_markdown,
    run_eval,
)
from phenoagent.matching import load_phenopacket

ROOT_DIR = Path(__file__).resolve().parents[2]
PHENOPACKET_DIR = ROOT_DIR / "tests" / "phenoagent" / "data" / "phenopackets"

GALACTOSEMIA_GT = PHENOPACKET_DIR / "Galactosemia_proband.gt.json"
FANCONI_GT = PHENOPACKET_DIR / "Fanconi_Anemia_proband.gt.json"
KB_MISS_GT = PHENOPACKET_DIR / "Stolerman_Syndrome_proband.gt.json"
NO_GT = PHENOPACKET_DIR / "PMID_35451551_proband.min.json"


def _phenotype(hp_id: str, label: str, frequency: str | None = None) -> dict:
    entry = {
        "name": label,
        "phenotype_term": {"preferred_term": label, "term": {"id": hp_id, "label": label}},
    }
    if frequency:
        entry["frequency"] = frequency
    return entry


@pytest.fixture(scope="module")
def kb_dir(tmp_path_factory) -> Path:
    """A minimal disorder directory with Galactosemia and Fanconi anemia."""
    kb = tmp_path_factory.mktemp("kb_disorders")
    (kb / "Galactosemia.yaml").write_text(
        yaml.safe_dump(
            {
                "name": "Galactosemia",
                "disease_term": {"term": {"id": "MONDO:0018116", "label": "galactosemia"}},
                "phenotypes": [
                    _phenotype("HP:0000518", "Cataract", "FREQUENT"),
                    _phenotype("HP:0002240", "Hepatomegaly", "FREQUENT"),
                    _phenotype("HP:0001508", "Failure to thrive", "FREQUENT"),
                    _phenotype("HP:0001249", "Intellectual disability", "OCCASIONAL"),
                ],
            }
        )
    )
    (kb / "Fanconi_Anemia.yaml").write_text(
        yaml.safe_dump(
            {
                "name": "Fanconi anemia",
                "disease_term": {"term": {"id": "MONDO:0019391", "label": "Fanconi anemia"}},
                "phenotypes": [
                    _phenotype("HP:0001873", "Thrombocytopenia", "VERY_FREQUENT"),
                    _phenotype("HP:0001903", "Anemia", "VERY_FREQUENT"),
                    _phenotype("HP:0004322", "Short stature", "FREQUENT"),
                    _phenotype("HP:0000957", "Cafe-au-lait spot", "FREQUENT"),
                    _phenotype("HP:0002119", "Ventriculomegaly", "OCCASIONAL"),
                ],
            }
        )
    )
    return kb


@pytest.fixture(scope="module")
def index(kb_dir):
    return build_disease_index(kb_dir=kb_dir)


# --- ground-truth extraction (no KB needed) ---------------------------------


def test_extract_ground_truth_from_interpretations():
    phenopacket = load_phenopacket(GALACTOSEMIA_GT)
    gt = extract_ground_truth_disease(phenopacket)
    assert gt == {"id": "MONDO:0018116", "label": "galactosemia"}


def test_extract_ground_truth_from_top_level_diseases():
    phenopacket = {
        "id": "x",
        "phenotypicFeatures": [],
        "diseases": [{"term": {"id": "MONDO:0019391", "label": "Fanconi anemia"}}],
    }
    assert extract_ground_truth_disease(phenopacket) == {
        "id": "MONDO:0019391",
        "label": "Fanconi anemia",
    }


def test_extract_ground_truth_absent_returns_none():
    phenopacket = load_phenopacket(NO_GT)
    assert extract_ground_truth_disease(phenopacket) is None


# --- disease index ----------------------------------------------------------


def test_disease_index_resolves_by_id_and_name(index):
    assert index.resolve("MONDO:0018116", None) == "Galactosemia"
    assert index.resolve("mondo:0018116", None) == "Galactosemia"  # case-insensitive
    assert index.resolve(None, "Fanconi anemia") == "Fanconi_Anemia"
    assert index.resolve("MONDO:9999999", "no such disease") is None


# --- per-packet evaluation --------------------------------------------------


def test_evaluate_scored_packet_resolves_and_scores(index, kb_dir):
    result = evaluate_phenopacket(GALACTOSEMIA_GT, kb_dir=kb_dir, disease_index=index)
    assert result.status == "SCORED"
    assert result.ground_truth_id == "MONDO:0018116"
    assert result.resolved_slug == "Galactosemia"

    metrics = result.metrics
    # Cataract, Hepatomegaly, Failure to thrive, Intellectual disability are exact;
    # Seizure has no model match; excluded "Abnormality of the liver" is a parent of
    # Hepatomegaly, so it registers as a related (broader) match, not unmatched.
    assert metrics["case_exact"] == 4
    assert metrics["case_unmatched"] == 1  # Seizure
    assert metrics["case_related"] >= 1  # the excluded liver parent term
    assert metrics["exact_recall"] == pytest.approx(4 / 6, abs=1e-3)
    assert metrics["related_recall"] >= metrics["exact_recall"]
    assert metrics["model_coverage"] == pytest.approx(1.0)


def test_evaluate_kb_miss_when_disease_absent(index, kb_dir):
    result = evaluate_phenopacket(KB_MISS_GT, kb_dir=kb_dir, disease_index=index)
    assert result.status == "KB_MISS"
    assert result.ground_truth_id == "MONDO:0032739"
    assert result.resolved_slug is None
    assert result.metrics == {}


def test_evaluate_no_ground_truth(index, kb_dir):
    result = evaluate_phenopacket(NO_GT, kb_dir=kb_dir, disease_index=index)
    assert result.status == "NO_GROUND_TRUTH"
    assert result.resolved_slug is None


def test_evaluate_fallback_resolution_without_index(kb_dir):
    """Without an index, resolution falls back to resolve_disease_reference."""
    result = evaluate_phenopacket(GALACTOSEMIA_GT, kb_dir=kb_dir)
    assert result.status == "SCORED"
    assert result.resolved_slug == "Galactosemia"


def test_pr_is_diagnosis_is_degenerate_zero_on_deterministic_run(index, kb_dir):
    """Documents why the harness scores on a surrogate, not pr_is_diagnosis."""
    result = evaluate_phenopacket(FANCONI_GT, kb_dir=kb_dir, disease_index=index)
    assert result.status == "SCORED"
    # Ventriculomegaly is a model-only row -> NO_EXPLANATION (0.0) -> product is 0.0.
    assert result.metrics["pr_is_diagnosis"] == 0.0
    assert result.metrics["model_only"] >= 1


# --- aggregation / reporting ------------------------------------------------


def test_run_eval_directory_aggregates_all_statuses(index, kb_dir):
    report = run_eval([PHENOPACKET_DIR], kb_dir=kb_dir, disease_index=index)
    summary = report["summary"]
    assert summary["n_scored"] == 2  # Galactosemia + Fanconi
    assert summary["n_kb_miss"] == 1  # Stolerman
    assert summary["n_no_ground_truth"] >= 1  # the .min.json fixtures
    assert 0.0 <= summary["kb_coverage_rate"] <= 1.0
    assert any("MONDO:0032739" in d for d in summary["kb_miss_diseases"])


def test_aggregate_means_only_over_scored(index, kb_dir):
    results = [
        evaluate_phenopacket(GALACTOSEMIA_GT, kb_dir=kb_dir, disease_index=index),
        evaluate_phenopacket(FANCONI_GT, kb_dir=kb_dir, disease_index=index),
        evaluate_phenopacket(KB_MISS_GT, kb_dir=kb_dir, disease_index=index),
        evaluate_phenopacket(NO_GT, kb_dir=kb_dir, disease_index=index),
    ]
    summary = aggregate_results(results)
    assert summary["n_scored"] == 2
    assert summary["n_kb_miss"] == 1
    assert summary["n_no_ground_truth"] == 1
    assert "mean_exact_recall" in summary
    assert 0.0 <= summary["mean_exact_recall"] <= 1.0


def test_render_markdown_contains_coverage_and_caveat(index, kb_dir):
    report = run_eval([GALACTOSEMIA_GT, KB_MISS_GT], kb_dir=kb_dir, disease_index=index)
    markdown = render_markdown(report)
    assert "Phenopacket Match-Quality Eval" in markdown
    assert "pr_is_diagnosis" in markdown  # the caveat is surfaced
    assert "KB coverage rate" in markdown


def test_main_writes_json_and_markdown(tmp_path, capsys, kb_dir):
    json_out = tmp_path / "report.json"
    md_out = tmp_path / "report.md"
    exit_code = main(
        [
            str(GALACTOSEMIA_GT),
            str(KB_MISS_GT),
            "--kb-dir",
            str(kb_dir),
            "--json",
            str(json_out),
            "--markdown",
            str(md_out),
        ]
    )
    assert exit_code == 0
    assert json_out.exists()
    assert md_out.exists()
    captured = capsys.readouterr()
    assert "Phenopacket Match-Quality Eval" in captured.out
