"""Tests for HPOA-extended exporter."""
from pathlib import Path

import pytest
import yaml

from dismech.export.hpoa_export import (
    FREQUENCY_TO_HP,
    export,
    hpoa_rows_for_disorder,
    parse_frequency,
    slugify,
)


def _write(path: Path, payload: dict) -> Path:
    path.write_text(yaml.safe_dump(payload, sort_keys=False))
    return path


def test_slugify():
    assert slugify("22q11.2_Deletion_Syndrome") == "22q11-2-deletion-syndrome"
    assert slugify("Carpal Tunnel Syndrome") == "carpal-tunnel-syndrome"
    assert slugify("") == "unnamed"
    assert slugify("--leading---and---trailing--") == "leading-and-trailing"


def test_parse_frequency_percent_range():
    assert parse_frequency({"description": "occurs in 50-60% of patients"}) == "50-60%"


def test_parse_frequency_single_percent():
    assert (
        parse_frequency({"description": "Cardiac defects occur in 75% of patients"})
        == "75%"
    )


def test_parse_frequency_approximate():
    assert (
        parse_frequency({"description": "symptomatic in about 10% of reported patients"})
        == "10%"
    )


def test_parse_frequency_ratio():
    assert parse_frequency({"description": "observed in 12/45 patients"}) == "12/45"


def test_parse_frequency_falls_back_to_enum():
    assert parse_frequency({"description": "no number here", "frequency": "FREQUENT"}) == "HP:0040282"
    assert parse_frequency({"frequency": "VERY_RARE"}) == "HP:0040284"


def test_parse_frequency_returns_none_when_missing():
    assert parse_frequency({"description": "no number"}) is None
    assert parse_frequency({}) is None


def test_model_organism_evidence_dropped(tmp_path):
    yaml_path = _write(
        tmp_path / "Test_Disorder.yaml",
        {
            "name": "Test",
            "disease_term": {"term": {"id": "MONDO:0000001", "label": "test"}},
            "creation_date": "2026-01-01T00:00:00Z",
            "phenotypes": [
                {
                    "name": "Phen A",
                    "frequency": "FREQUENT",
                    "phenotype_term": {"term": {"id": "HP:0000001", "label": "A"}},
                    "evidence": [
                        {"reference": "PMID:1", "evidence_source": "HUMAN_CLINICAL", "supports": "SUPPORT"},
                        {"reference": "PMID:2", "evidence_source": "MODEL_ORGANISM", "supports": "SUPPORT"},
                    ],
                },
            ],
        },
    )
    hpoa, _ = hpoa_rows_for_disorder(yaml_path)
    refs = [r["reference"] for r in hpoa]
    assert "PMID:1" in refs
    assert "PMID:2" not in refs


def test_phenotype_without_human_evidence_still_emits_iea_row(tmp_path):
    """A phenotype with only model-organism evidence still emits one IEA row anchored on the disease."""
    yaml_path = _write(
        tmp_path / "X.yaml",
        {
            "disease_term": {"term": {"id": "MONDO:0000001", "label": "x"}},
            "creation_date": "2026-01-01T00:00:00Z",
            "phenotypes": [
                {
                    "name": "A",
                    "frequency": "OCCASIONAL",
                    "phenotype_term": {"term": {"id": "HP:0000001", "label": "A"}},
                    "evidence": [
                        {"reference": "PMID:99", "evidence_source": "MODEL_ORGANISM"},
                    ],
                },
            ],
        },
    )
    hpoa, _ = hpoa_rows_for_disorder(yaml_path)
    assert len(hpoa) == 1
    assert hpoa[0]["reference"] == "MONDO:0000001"
    assert hpoa[0]["evidence"] == "IEA"


def test_in_vitro_evidence_kept_as_pcs(tmp_path):
    yaml_path = _write(
        tmp_path / "X.yaml",
        {
            "disease_term": {"term": {"id": "MONDO:0000001", "label": "x"}},
            "creation_date": "2026-01-01T00:00:00Z",
            "phenotypes": [
                {
                    "name": "A",
                    "phenotype_term": {"term": {"id": "HP:0000001", "label": "A"}},
                    "evidence": [
                        {"reference": "PMID:5", "evidence_source": "IN_VITRO"},
                    ],
                },
            ],
        },
    )
    hpoa, _ = hpoa_rows_for_disorder(yaml_path)
    assert hpoa[0]["evidence"] == "PCS"


def test_untyped_phenotype_emits_dismech_curie(tmp_path):
    yaml_path = _write(
        tmp_path / "ATTR_Amyloidosis.yaml",
        {
            "disease_term": {"term": {"id": "MONDO:0007100", "label": "ATTR amyloidosis"}},
            "creation_date": "2026-01-01T00:00:00Z",
            "phenotypes": [
                {
                    "name": "Carpal Tunnel Syndrome",
                    "frequency": "OCCASIONAL",
                    "phenotype_term": {"preferred_term": "Carpal Tunnel Syndrome"},
                    "evidence": [{"reference": "PMID:30404120", "evidence_source": "HUMAN_CLINICAL"}],
                },
            ],
        },
    )
    hpoa, _ = hpoa_rows_for_disorder(yaml_path)
    assert len(hpoa) == 1
    assert hpoa[0]["hpo_id"] == "DISMECH:attr-amyloidosis#carpal-tunnel-syndrome"
    assert hpoa[0]["dismech_name"] == "Carpal Tunnel Syndrome"
    assert hpoa[0]["evidence"] == "PCS"


def test_mondo_typed_routes_to_comorbidity(tmp_path):
    yaml_path = _write(
        tmp_path / "Campylobacteriosis.yaml",
        {
            "disease_term": {"term": {"id": "MONDO:0005688", "label": "campylobacteriosis"}},
            "creation_date": "2026-01-01T00:00:00Z",
            "phenotypes": [
                {
                    "name": "Guillain-Barre syndrome",
                    "phenotype_term": {"term": {"id": "MONDO:0016218", "label": "Guillain-Barre syndrome"}},
                    "evidence": [{"reference": "PMID:1", "evidence_source": "HUMAN_CLINICAL"}],
                },
            ],
        },
    )
    hpoa, comorb = hpoa_rows_for_disorder(yaml_path)
    assert hpoa == []
    assert len(comorb) == 1
    assert comorb[0]["comorbid_id"] == "MONDO:0016218"
    assert comorb[0]["predicate"] == "biolink:associated_with"
    assert comorb[0]["evidence"] == "PCS"


def test_refute_emits_NOT_qualifier(tmp_path):
    yaml_path = _write(
        tmp_path / "X.yaml",
        {
            "disease_term": {"term": {"id": "MONDO:0000001", "label": "x"}},
            "creation_date": "2026-01-01T00:00:00Z",
            "phenotypes": [
                {
                    "name": "A",
                    "phenotype_term": {"term": {"id": "HP:0000001", "label": "A"}},
                    "evidence": [
                        {"reference": "PMID:1", "evidence_source": "HUMAN_CLINICAL", "supports": "REFUTE"},
                    ],
                },
            ],
        },
    )
    rows, _ = hpoa_rows_for_disorder(yaml_path)
    assert rows[0]["qualifier"] == "NOT"


def test_non_mondo_disease_skipped(tmp_path):
    yaml_path = _write(
        tmp_path / "X.yaml",
        {
            "disease_term": {"term": {"id": "OMIM:12345"}},
            "phenotypes": [{"name": "A", "phenotype_term": {"term": {"id": "HP:0000001"}}}],
        },
    )
    hpoa, comorb = hpoa_rows_for_disorder(yaml_path)
    assert hpoa == []
    assert comorb == []


def test_one_row_per_evidence_item(tmp_path):
    yaml_path = _write(
        tmp_path / "X.yaml",
        {
            "disease_term": {"term": {"id": "MONDO:0000001", "label": "x"}},
            "creation_date": "2026-01-01T00:00:00Z",
            "phenotypes": [
                {
                    "name": "A",
                    "phenotype_term": {"term": {"id": "HP:0000001", "label": "A"}},
                    "evidence": [
                        {"reference": "PMID:1", "evidence_source": "HUMAN_CLINICAL"},
                        {"reference": "PMID:2", "evidence_source": "HUMAN_CLINICAL"},
                    ],
                },
            ],
        },
    )
    rows, _ = hpoa_rows_for_disorder(yaml_path)
    assert [r["reference"] for r in rows] == ["PMID:1", "PMID:2"]


def test_export_writes_files(tmp_path):
    kb = tmp_path / "kb"
    kb.mkdir()
    _write(
        kb / "Test.yaml",
        {
            "disease_term": {"term": {"id": "MONDO:0000001", "label": "test"}},
            "creation_date": "2026-01-01T00:00:00Z",
            "phenotypes": [
                {
                    "name": "A",
                    "phenotype_term": {"term": {"id": "HP:0000001", "label": "A"}},
                    "evidence": [{"reference": "PMID:1", "evidence_source": "HUMAN_CLINICAL"}],
                },
            ],
        },
    )
    out = tmp_path / "out"
    n_hpoa, n_comorb = export(kb, out)
    assert n_hpoa == 1
    assert n_comorb == 0
    content = (out / "phenotype.dismech.hpoa").read_text()
    assert content.startswith("#description:")
    assert "MONDO:0000001\ttest\t" in content
