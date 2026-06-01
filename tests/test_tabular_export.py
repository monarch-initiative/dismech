"""Tests for generic tabular exporter."""

import csv
import tempfile
from pathlib import Path

import yaml

from dismech.export.tabular_export import TabularExporter


def _read_tsv(path: Path) -> list[dict[str, str]]:
    with open(path) as stream:
        return list(csv.DictReader(stream, delimiter="\t"))


def test_tabular_export_flattens_assertions_descriptors_and_evidence():
    with tempfile.TemporaryDirectory() as tmpdir:
        tmpdir_path = Path(tmpdir)
        kb_dir = tmpdir_path / "kb"
        kb_dir.mkdir()

        disorder = {
            "name": "Example Disorder",
            "category": "Genetic",
            "pathophysiology": [
                {
                    "name": "Inflammation",
                    "cell_types": [
                        {
                            "preferred_term": "microglial cell",
                            "term": {"id": "CL:0000129", "label": "microglial cell"},
                        }
                    ],
                    "evidence": [
                        {
                            "reference": "PMID:1",
                            "supports": "SUPPORT",
                            "evidence_source": "HUMAN_CLINICAL",
                            "snippet": "patho evidence",
                            "explanation": "patho explanation",
                        }
                    ],
                }
            ],
            "phenotypes": [
                {
                    "name": "Seizure",
                    "frequency": "FREQUENT",
                    "phenotype_term": {
                        "preferred_term": "Seizure",
                        "term": {"id": "HP:0001250", "label": "Seizure"},
                        "temporality": "RECURRENT",
                        "clinical_course": "PROGRESSIVE",
                        "severity": "SEVERE",
                        "onset": {"onset_category": "CHILDHOOD"},
                    },
                    "phenotype_contexts": [
                        {
                            "genetic_context": {
                                "gene": {
                                    "preferred_term": "SCN1A",
                                    "term": {"id": "hgnc:10585", "label": "SCN1A"},
                                }
                            },
                            "evidence": [
                                {
                                    "reference": "PMID:2",
                                    "supports": "SUPPORT",
                                    "snippet": "nested evidence",
                                }
                            ],
                        }
                    ],
                    "evidence": [
                        {
                            "reference": "PMID:3",
                            "supports": "SUPPORT",
                            "snippet": "phenotype evidence",
                        }
                    ],
                }
            ],
            "treatments": [
                {
                    "name": "Valproate",
                    "treatment_term": {
                        "preferred_term": "Pharmacotherapy",
                        "term": {"id": "NCIT:C15986", "label": "Pharmacotherapy"},
                        "qualifiers": [
                            {
                                "predicate": {
                                    "preferred_term": "therapeutic agent",
                                    "term": {"id": "NCIT:C2259", "label": "Therapeutic Agent"},
                                },
                                "value": {
                                    "preferred_term": "antibiotic",
                                    "term": {"id": "NCIT:C258", "label": "Antibiotic"},
                                },
                            }
                        ],
                    },
                }
            ],
        }

        yaml_path = kb_dir / "Example.yaml"
        with open(yaml_path, "w") as stream:
            yaml.safe_dump(disorder, stream, sort_keys=False)

        history_path = kb_dir / "Example.history.yaml"
        with open(history_path, "w") as stream:
            yaml.safe_dump({"name": "Historical Example", "phenotypes": []}, stream, sort_keys=False)

        exporter = TabularExporter()
        files = exporter.discover_disorder_files(kb_dir, include_history=False)
        assert files == [yaml_path]

        output_dir = tmpdir_path / "tabular"
        summary = exporter.export(files, output_dir=output_dir)

        assert summary.disorder_count == 1
        assert summary.assertion_count == 3
        assert summary.descriptor_count >= 4
        assert summary.evidence_count >= 3
        assert summary.postcomposition_count >= 1

        assertions = _read_tsv(output_dir / "assertions.tsv")
        assert {row["section"] for row in assertions} == {"pathophysiology", "phenotypes", "treatments"}

        descriptors = _read_tsv(output_dir / "descriptors.tsv")
        descriptor_paths = {row["path"] for row in descriptors}
        assert "phenotype_term" in descriptor_paths
        assert "treatment_term" in descriptor_paths
        assert "cell_types[0]" in descriptor_paths
        assert "phenotype_contexts[0].genetic_context.gene" in descriptor_paths

        treatment_term_row = next(row for row in descriptors if row["path"] == "treatment_term")
        assert treatment_term_row["section_name"] == "Valproate"
        assert treatment_term_row["section"] == "treatments"
        assert treatment_term_row["parent_path"] == "$"
        assert treatment_term_row["parent_name"] == "Valproate"
        assert treatment_term_row["qualifier_therapeutic_agent"] == "Antibiotic"
        assert treatment_term_row["qualifier_therapeutic_agent_ids"] == "NCIT:C258"
        assert treatment_term_row["qualifier_therapeutic_agent_predicate_ids"] == "NCIT:C2259"

        phenotype_term_row = next(row for row in descriptors if row["path"] == "phenotype_term")
        assert phenotype_term_row["postcomp_temporality"] == "RECURRENT"
        assert phenotype_term_row["postcomp_clinical_course"] == "PROGRESSIVE"
        assert phenotype_term_row["postcomp_severity"] == "SEVERE"
        assert phenotype_term_row["postcomp_onset"] == "CHILDHOOD"

        postcomposition = _read_tsv(output_dir / "descriptor_postcomposition.tsv")
        phenotype_postcomposition = {
            row["relation_type"]: row
            for row in postcomposition
            if row["descriptor_path"] == "phenotype_term"
        }
        assert phenotype_postcomposition["temporality"]["value_literal"] == "RECURRENT"
        assert phenotype_postcomposition["clinical_course"]["value_literal"] == "PROGRESSIVE"
        assert phenotype_postcomposition["severity"]["value_literal"] == "SEVERE"
        assert phenotype_postcomposition["onset"]["value_literal"] == "CHILDHOOD"

        qualifier_row = next(
            row
            for row in postcomposition
            if row["relation_type"] == "qualifier" and row["descriptor_path"] == "treatment_term"
        )
        assert qualifier_row["section_name"] == "Valproate"
        assert qualifier_row["predicate_term_id"] == "NCIT:C2259"
        assert qualifier_row["value_term_id"] == "NCIT:C258"

        evidence = _read_tsv(output_dir / "evidence.tsv")
        evidence_paths = {row["path"] for row in evidence}
        assert "evidence" in evidence_paths
        assert "phenotype_contexts[0].evidence" in evidence_paths

        assert (output_dir / "sections" / "phenotypes" / "assertions.tsv").exists()
        assert (output_dir / "sections" / "treatments" / "assertions.tsv").exists()
        assert (output_dir / "sections" / "treatments" / "descriptor_postcomposition.tsv").exists()


def test_tabular_export_flattens_treatment_dietary_modifications():
    with tempfile.TemporaryDirectory() as tmpdir:
        tmpdir_path = Path(tmpdir)
        kb_dir = tmpdir_path / "kb"
        kb_dir.mkdir()

        disorder = {
            "name": "Example Dietary Disorder",
            "category": "Genetic",
            "treatments": [
                {
                    "name": "Gluten-free diet",
                    "treatment_term": {
                        "preferred_term": "dietary intervention",
                        "term": {"id": "MAXO:0000088", "label": "dietary intervention"},
                        "dietary_modifications": [
                            {
                                "action": "AVOID",
                                "food": {
                                    "preferred_term": "wheat food product",
                                    "term": {
                                        "id": "FOODON:00001141",
                                        "label": "wheat food product",
                                    },
                                },
                            },
                            {
                                "action": "AVOID",
                                "food": {
                                    "preferred_term": "barley",
                                    "term": {
                                        "id": "FOODON:00003108",
                                        "label": "barley seed (raw)",
                                    },
                                },
                            },
                        ],
                    },
                }
            ],
        }

        yaml_path = kb_dir / "ExampleDiet.yaml"
        with open(yaml_path, "w") as stream:
            yaml.safe_dump(disorder, stream, sort_keys=False)

        exporter = TabularExporter()
        output_dir = tmpdir_path / "tabular"
        exporter.export([yaml_path], output_dir=output_dir)

        descriptors = _read_tsv(output_dir / "descriptors.tsv")
        treatment_term_row = next(row for row in descriptors if row["path"] == "treatment_term")
        assert treatment_term_row["postcomp_dietary_modification"] == (
            "AVOID wheat food product; AVOID barley seed (raw)"
        )
        assert treatment_term_row["postcomp_dietary_modification_ids"] == (
            "FOODON:00001141; FOODON:00003108"
        )
        assert treatment_term_row["postcomp_dietary_modification_actions"] == "AVOID"

        postcomposition = _read_tsv(output_dir / "descriptor_postcomposition.tsv")
        dietary_rows = [
            row
            for row in postcomposition
            if row["relation_type"] == "dietary_modification" and row["descriptor_path"] == "treatment_term"
        ]
        assert len(dietary_rows) == 2
        assert dietary_rows[0]["predicate_preferred_term"] == "AVOID"
        assert dietary_rows[0]["value_term_id"] == "FOODON:00001141"
