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
                        "preferred_term": "pharmacotherapy",
                        "term": {"id": "MAXO:0000058", "label": "pharmacotherapy"},
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

        postcomposition = _read_tsv(output_dir / "descriptor_postcomposition.tsv")
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
