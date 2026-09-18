"""Tests for the computational-models browser data exporter."""

from pathlib import Path

from dismech.export.models_export import (
    ModelsExporter,
    humanize_enum,
    make_anchor_id,
    repository_host,
)
from dismech.render import _make_anchor_id

REPO_ROOT = Path(__file__).resolve().parents[1]


def test_anchor_id_matches_renderer():
    """The browser deep-link must land on the anchor the renderer emits."""
    for name in (
        "Minimal Urate Homeostasis Model",
        "Topp Beta-Cell Mass / Insulin / Glucose Model",
        "PDAC CAF-Mediated Invasion PhysiCell Model",
    ):
        assert make_anchor_id(name) == _make_anchor_id("computational-model", name)


def test_humanize_enum():
    assert humanize_enum("GENOME_SCALE_METABOLIC") == "Genome Scale Metabolic"
    assert humanize_enum("BOOLEAN_NETWORK") == "Boolean Network"
    assert humanize_enum(None) == ""


def test_repository_host_classification():
    assert repository_host("https://www.ebi.ac.uk/biomodels/BIOMD0000000341") == "BioModels"
    assert repository_host("https://www.vmh.life/") == "Virtual Metabolic Human"
    assert repository_host("https://github.com/jtmff/torord") == "GitHub"
    assert repository_host("https://example.org/model") == "Other"
    assert repository_host(None) == "No repository link"


def _entry():
    return {
        "name": "Test Disorder",
        "category": "Metabolic",
        "parents": ["Inborn Error of Metabolism"],
        "creation_date": "2025-01-01T00:00:00Z",
        "disease_term": {"term": {"id": "MONDO:0000001"}},
        "computational_models": [
            {
                "name": "Minimal Urate Homeostasis Model",
                "description": "A single-compartment ODE model.",
                "model_type": "KINETIC",
                "model_id": "urate_homeostasis",
                "model_format": "SBML",
                "model_software": "Antimony/tellurium",
                "publication": "PMID:29904633",
                "perturbations": [
                    {"preferred_term": "ABCG2", "term": {"id": "hgnc:74", "label": "ABCG2"}},
                ],
                "variables": [
                    {
                        "name": "Serum urate",
                        "dataset_identifier": "U",
                        "unit": "mg/dL",
                        "mappings_list": [
                            {"preferred_term": "Hyperuricemia", "term": {"id": "HP:0002149"}}
                        ],
                    }
                ],
                "modeled_mechanisms": [{"target": "Hyperuricemia"}],
                "findings": [
                    {
                        "statement": "The solubility limit sets the threshold.",
                        "evidence": [{"reference": "PMID:29904633"}],
                    }
                ],
                "evidence": [{"reference": "PMID:29904633"}],
            },
            {
                "name": "Recon3D with PAH knockout",
                "model_type": "GENOME_SCALE_METABOLIC",
                "model_id": "Recon3D",
                "repository_url": "https://github.com/VirtualMetabolicHuman/Recon",
            },
            # Nameless models cannot be anchored or linked, so they are skipped.
            {"model_type": "KINETIC"},
        ],
    }


def _records(runnable=("urate_homeostasis",)):
    exporter = ModelsExporter(models_dir=Path("does-not-exist"))
    exporter.runnable_model_ids = set(runnable)
    return exporter.extract_models(
        _entry(),
        source_type="Disorder",
        source_file="kb/disorders/Test.yaml",
        page_url="../../pages/disorders/Test_Disorder.html",
    )


def test_extract_models_flattens_and_skips_nameless():
    records = _records()
    assert [r["name"] for r in records] == [
        "Minimal Urate Homeostasis Model",
        "Recon3D with PAH knockout",
    ]

    urate = records[0]
    assert urate["model_type"] == "Kinetic"
    assert urate["model_type_raw"] == "KINETIC"
    assert urate["source_name"] == "Test Disorder"
    assert urate["disease_id"] == "MONDO:0000001"
    assert urate["parents"] == ["Inborn Error of Metabolism"]
    assert urate["perturbations"] == ["ABCG2"]
    assert urate["perturbation_ids"] == ["hgnc:74"]
    assert urate["variables"] == ["Serum urate"]
    assert urate["variable_ids"] == ["U"]
    assert urate["variable_terms"] == ["Hyperuricemia"]
    assert urate["modeled_mechanisms"] == ["Hyperuricemia"]
    assert urate["num_findings"] == 1
    # Model-level and finding-level evidence are pooled and de-duplicated.
    assert urate["evidence_refs"] == ["PMID:29904633"]
    assert urate["num_evidence"] == 1
    assert urate["page_url"].endswith("#computational-model-minimal-urate-homeostasis-model")


def test_runnable_flag_tracks_local_perturb_config():
    urate, recon = _records()
    assert urate["runnable"] == "Runnable in-repo"
    assert recon["runnable"] == "Reference only"

    urate_only_ref, _ = _records(runnable=())
    assert urate_only_ref["runnable"] == "Reference only"


def test_missing_format_and_software_get_facetable_placeholders():
    _, recon = _records()
    assert recon["model_format"] == "Format not recorded"
    assert recon["model_software"] == "Software not recorded"
    assert recon["repository_host"] == "GitHub"


def test_model_keys_are_unique_across_the_knowledge_base():
    """Model names repeat across disorders (AGORA2, MICOM), so keys must not."""
    records = ModelsExporter().collect_records(
        REPO_ROOT / "kb" / "disorders", REPO_ROOT / "kb" / "modules"
    )
    assert records, "expected at least one curated computational model"
    keys = [r["model_key"] for r in records]
    assert len(keys) == len(set(keys))


def test_runnable_models_resolve_to_committed_perturb_configs():
    """Every model flagged runnable must have its config checked into models/."""
    exporter = ModelsExporter(models_dir=REPO_ROOT / "models")
    records = exporter.collect_records(
        REPO_ROOT / "kb" / "disorders", REPO_ROOT / "kb" / "modules"
    )
    runnable = [r for r in records if r["runnable"] == "Runnable in-repo"]
    assert runnable, "expected the dismech-perturb models to be flagged runnable"
    for record in runnable:
        config = REPO_ROOT / "models" / f"{record['model_id']}.config.yaml"
        assert config.exists(), f"{record['name']} claims runnable without {config}"


# Deliberately NOT tested here: the committed app/models/data.js against the
# committed KB. This file is rebuilt from every computational_models block in
# kb/, so requiring repo state to match forced each model-curation PR to commit
# a regenerated 2,800-line artifact — which made any two concurrent model PRs
# conflict on it and nothing else. Nine approved PRs deadlocked that way
# (#9104, #9119, #9122, #9140, #9142, #9145, #9263, #9324, #9325).
#
# It is the same invariant, and the same resolution, as the sibling app/data.js
# index: see the note in tests/test_check_browser_data_links.py. The invariant
# belongs to the generate-pages run, which regenerates and commits the file
# after rendering and gates on its links, not to repo state between builds.
