from __future__ import annotations

import csv
from pathlib import Path

import yaml
from typer.testing import CliRunner

from dismech.compare.g2p import build_release_row_table
from dismech.compare.g2p import app as g2p_compare_app
from dismech.compare.g2p import compare_gene, run_comparison, survey_genes
from dismech.compare.g2p import compute_release_overview
from dismech.compare.g2p_audit import compare_gene as compat_compare_gene


def _write_g2p_csv(path: Path, rows: list[dict[str, str]]) -> None:
    fieldnames = [
        "g2p id",
        "gene symbol",
        "gene mim",
        "hgnc id",
        "previous gene symbols",
        "disease name",
        "disease mim",
        "disease MONDO",
        "allelic requirement",
        "cross cutting modifier",
        "confidence",
        "variant consequence",
        "variant types",
        "molecular mechanism",
        "molecular mechanism support",
        "molecular mechanism categorisation",
        "molecular mechanism evidence",
        "phenotypes",
        "publications",
        "additional mined publications",
        "panel",
        "comments",
        "date of last review",
        "review",
    ]
    with path.open("w", newline="", encoding="utf-8") as stream:
        writer = csv.DictWriter(stream, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def _write_yaml(path: Path, payload: dict) -> None:
    path.write_text(yaml.safe_dump(payload, sort_keys=False), encoding="utf-8")


def _build_single_gene_fixture(tmp_path: Path) -> tuple[Path, Path]:
    kb_dir = tmp_path / "kb"
    kb_dir.mkdir()

    _write_yaml(
        kb_dir / "Cowden_Syndrome.yaml",
        {
            "name": "Cowden Syndrome",
            "disease_term": {
                "term": {"id": "MONDO:0016063", "label": "Cowden disease"}
            },
            "genetic": [
                {
                    "name": "PTEN",
                    "association": "Causative",
                    "gene_term": {
                        "preferred_term": "PTEN",
                        "term": {"id": "hgnc:9588", "label": "PTEN"},
                    },
                    "evidence": [{"reference": "PMID:111"}],
                }
            ],
            "phenotypes": [
                {
                    "name": "Lhermitte-Duclos Disease",
                    "phenotype_term": {
                        "term": {
                            "id": "HP:0500009",
                            "label": "Dysplastic gangliocytoma of the cerebellum",
                        }
                    },
                    "evidence": [{"reference": "PMID:222"}],
                }
            ],
        },
    )

    g2p_path = tmp_path / "pten.csv"
    _write_g2p_csv(
        g2p_path,
        [
            {
                "g2p id": "G2P00413",
                "gene symbol": "PTEN",
                "gene mim": "601728",
                "hgnc id": "9588",
                "previous gene symbols": "",
                "disease name": "PTEN-related hamartoma tumour syndrome (Cowden syndrome)",
                "disease mim": "158350",
                "disease MONDO": "MONDO:0008021",
                "allelic requirement": "monoallelic_autosomal",
                "cross cutting modifier": "",
                "confidence": "definitive",
                "variant consequence": "absent gene product",
                "variant types": "frameshift_variant",
                "molecular mechanism": "loss of function",
                "molecular mechanism support": "evidence",
                "molecular mechanism categorisation": "destabilising LOF:evidence",
                "molecular mechanism evidence": "111 -> biochemical",
                "phenotypes": "HP:0000256; HP:0500009",
                "publications": "111;555",
                "additional mined publications": "",
                "panel": "DD; Cancer",
                "comments": "",
                "date of last review": "2025-05-08 12:16:01+00:00",
                "review": "",
            }
        ],
    )
    return kb_dir, g2p_path


def test_compare_gene_reports_direct_and_secondary_matches(tmp_path: Path) -> None:
    kb_dir = tmp_path / "kb"
    kb_dir.mkdir()

    _write_yaml(
        kb_dir / "Cowden_Syndrome.yaml",
        {
            "name": "Cowden Syndrome",
            "disease_term": {
                "term": {"id": "MONDO:0016063", "label": "Cowden disease"}
            },
            "genetic": [
                {
                    "name": "PTEN",
                    "association": "Causative",
                    "gene_term": {
                        "preferred_term": "PTEN",
                        "term": {"id": "hgnc:9588", "label": "PTEN"},
                    },
                    "evidence": [{"reference": "PMID:111"}],
                }
            ],
            "phenotypes": [
                {
                    "name": "Lhermitte-Duclos Disease",
                    "phenotype_term": {
                        "term": {
                            "id": "HP:0500009",
                            "label": "Dysplastic gangliocytoma of the cerebellum",
                        }
                    },
                    "evidence": [{"reference": "PMID:222"}],
                }
            ],
        },
    )
    _write_yaml(
        kb_dir / "Juvenile_Polyposis_Syndrome.yaml",
        {
            "name": "Juvenile Polyposis Syndrome",
            "disease_term": {
                "term": {"id": "MONDO:0017380", "label": "juvenile polyposis syndrome"}
            },
            "genetic": [
                {
                    "name": "PTEN",
                    "association": "Subtype-specific contiguous deletion partner",
                    "gene_term": {
                        "preferred_term": "PTEN",
                        "term": {"id": "hgnc:9588", "label": "PTEN"},
                    },
                    "evidence": [{"reference": "PMID:333"}],
                }
            ],
        },
    )
    _write_yaml(
        kb_dir / "Metastatic_Melanoma.yaml",
        {
            "name": "Metastatic Melanoma",
            "disease_term": {
                "term": {"id": "MONDO:0005105", "label": "metastatic melanoma"}
            },
            "genetic": [
                {
                    "name": "PTEN",
                    "association": "Somatic loss of function",
                    "gene_term": {
                        "preferred_term": "PTEN",
                        "term": {"id": "hgnc:9588", "label": "PTEN"},
                    },
                    "evidence": [{"reference": "PMID:444"}],
                }
            ],
        },
    )

    g2p_path = tmp_path / "pten.csv"
    _write_g2p_csv(
        g2p_path,
        [
            {
                "g2p id": "G2P00413",
                "gene symbol": "PTEN",
                "gene mim": "601728",
                "hgnc id": "9588",
                "previous gene symbols": "",
                "disease name": "PTEN-related hamartoma tumour syndrome (Cowden syndrome)",
                "disease mim": "158350",
                "disease MONDO": "MONDO:0008021",
                "allelic requirement": "monoallelic_autosomal",
                "cross cutting modifier": "",
                "confidence": "definitive",
                "variant consequence": "absent gene product",
                "variant types": "frameshift_variant",
                "molecular mechanism": "loss of function",
                "molecular mechanism support": "evidence",
                "molecular mechanism categorisation": "destabilising LOF:evidence",
                "molecular mechanism evidence": "111 -> biochemical",
                "phenotypes": "HP:0000256; HP:0500009",
                "publications": "111;555",
                "additional mined publications": "",
                "panel": "DD; Cancer",
                "comments": "",
                "date of last review": "2025-05-08 12:16:01+00:00",
                "review": "",
            },
            {
                "g2p id": "G2P02322",
                "gene symbol": "PTEN",
                "gene mim": "601728",
                "hgnc id": "9588",
                "previous gene symbols": "",
                "disease name": "PTEN-related Lhermitte-Duclos disease",
                "disease mim": "",
                "disease MONDO": "MONDO:0008021",
                "allelic requirement": "monoallelic_autosomal",
                "cross cutting modifier": "",
                "confidence": "definitive",
                "variant consequence": "absent gene product",
                "variant types": "",
                "molecular mechanism": "loss of function",
                "molecular mechanism support": "inferred",
                "molecular mechanism categorisation": "",
                "molecular mechanism evidence": "",
                "phenotypes": "HP:0500009",
                "publications": "222",
                "additional mined publications": "",
                "panel": "Eye; Skin",
                "comments": "",
                "date of last review": "2017-09-24 22:47:04+00:00",
                "review": "",
            },
        ],
    )

    report = compare_gene("PTEN", kb_dir=kb_dir, g2p_source=str(g2p_path))

    assert report["g2p_row_count"] == 2
    assert report["dismech_match_count"] == 3
    assert [match["match_strength"] for match in report["dismech_matches"]] == [
        "causative",
        "subtype_specific",
        "secondary_genetic",
    ]
    assert report["summary"]["row_status_counts"] == {
        "EMBEDDED_NOT_ROOTED": 1,
        "ROOT_MATCH": 1,
    }
    assert report["g2p_mondo_collisions"] == [
        {
            "disease_mondo": "MONDO:0008021",
            "disease_names": [
                "PTEN-related Lhermitte-Duclos disease",
                "PTEN-related hamartoma tumour syndrome (Cowden syndrome)",
            ],
        }
    ]

    first_row = report["g2p_rows"][0]
    assert first_row["row_status"] == "ROOT_MATCH"
    assert first_row["curation_priority"] == "LOW"
    assert first_row["curation_action"] == "KEEP_EXISTING_ROOT"
    assert first_row["dismech_candidates"] == [
        {
            "disorder_name": "Cowden Syndrome",
            "disease_mondo": "MONDO:0016063",
            "file": "Cowden_Syndrome.yaml",
            "match_reasons": ["name_or_parenthetical_alias"],
            "match_strength": "causative",
            "shared_phenotype_count": 1,
            "shared_phenotype_ids": ["HP:0500009"],
            "shared_reviewed_pmids_with_sections": ["111"],
            "shared_reviewed_pmids_with_disease": ["111"],
        }
    ]
    second_row = report["g2p_rows"][1]
    assert second_row["row_status"] == "EMBEDDED_NOT_ROOTED"
    assert second_row["curation_priority"] == "MEDIUM"
    assert second_row["curation_action"] == "DECIDE_IF_EMBEDDED_CONCEPT_NEEDS_ROOT"
    assert second_row["related_direct_matches"] == [
        {
            "disorder_name": "Cowden Syndrome",
            "file": "Cowden_Syndrome.yaml",
            "match_strength": "causative",
            "shared_phenotype_count": 1,
            "shared_phenotype_ids": ["HP:0500009"],
            "shared_reviewed_pmids_with_sections": [],
            "shared_reviewed_pmids_with_disease": ["222"],
        }
    ]

    direct_coverage = report["publication_coverage"]["direct_dismech_matched_sections"]
    assert direct_coverage["overlap_pmids"] == ["111"]
    assert direct_coverage["missing_from_dismech_pmids"] == ["222", "555"]
    assert direct_coverage["extra_in_dismech_pmids"] == ["333"]

    table, summary, gene_symbol = run_comparison(
        "PTEN", kb_dir=kb_dir, g2p_source=str(g2p_path)
    )
    assert gene_symbol == "PTEN"
    assert [row["row_status"] for row in table] == [
        "EMBEDDED_NOT_ROOTED",
        "ROOT_MATCH",
    ]
    assert [row["curation_priority"] for row in table] == ["MEDIUM", "LOW"]
    assert summary["mapped_row_count"] == 1
    assert summary["highest_curation_priority"] == "MEDIUM"
    assert summary["primary_curation_action"] == "DECIDE_IF_EMBEDDED_CONCEPT_NEEDS_ROOT"
    assert compat_compare_gene is compare_gene


def test_compare_gene_reports_pathophysiology_only_matches(tmp_path: Path) -> None:
    kb_dir = tmp_path / "kb"
    kb_dir.mkdir()

    _write_yaml(
        kb_dir / "Mechanism_Only.yaml",
        {
            "name": "Mechanism Only Disorder",
            "disease_term": {
                "term": {"id": "MONDO:9999999", "label": "mechanism only disorder"}
            },
            "pathophysiology": [
                {
                    "name": "PTEN Signaling Defect",
                    "gene": {
                        "preferred_term": "PTEN",
                        "term": {"id": "hgnc:9588", "label": "PTEN"},
                    },
                    "evidence": [{"reference": "PMID:666"}],
                }
            ],
        },
    )

    g2p_path = tmp_path / "pten.csv"
    _write_g2p_csv(
        g2p_path,
        [
            {
                "g2p id": "G2P1",
                "gene symbol": "PTEN",
                "gene mim": "",
                "hgnc id": "9588",
                "previous gene symbols": "",
                "disease name": "Unmatched PTEN disease",
                "disease mim": "",
                "disease MONDO": "",
                "allelic requirement": "",
                "cross cutting modifier": "",
                "confidence": "limited",
                "variant consequence": "",
                "variant types": "",
                "molecular mechanism": "",
                "molecular mechanism support": "",
                "molecular mechanism categorisation": "",
                "molecular mechanism evidence": "",
                "phenotypes": "",
                "publications": "777",
                "additional mined publications": "",
                "panel": "",
                "comments": "",
                "date of last review": "",
                "review": "",
            }
        ],
    )

    report = compare_gene("PTEN", kb_dir=kb_dir, g2p_source=str(g2p_path))

    assert report["dismech_matches"][0]["match_strength"] == "pathophysiology_only"
    assert report["g2p_rows"][0]["row_status"] == "EMBEDDED_NOT_ROOTED"
    all_sections = report["publication_coverage"]["all_dismech_matched_sections"]
    assert all_sections["extra_in_dismech_pmids"] == ["666"]


def test_survey_genes_uses_one_g2p_source_for_multiple_reports(tmp_path: Path) -> None:
    kb_dir = tmp_path / "kb"
    kb_dir.mkdir()

    _write_yaml(
        kb_dir / "Alexander_Disease.yaml",
        {
            "name": "Alexander Disease",
            "disease_term": {
                "term": {"id": "MONDO:0008752", "label": "Alexander disease"}
            },
            "genetic": [
                {
                    "name": "GFAP",
                    "association": "Causative",
                    "gene_term": {
                        "preferred_term": "GFAP",
                        "term": {"id": "hgnc:4235", "label": "GFAP"},
                    },
                    "evidence": [{"reference": "PMID:10"}],
                }
            ],
        },
    )
    _write_yaml(
        kb_dir / "Atelosteogenesis_Type_I.yaml",
        {
            "name": "Atelosteogenesis Type I",
            "disease_term": {
                "term": {"id": "MONDO:0007167", "label": "atelosteogenesis type I"}
            },
            "genetic": [
                {
                    "name": "FLNB",
                    "association": "Causative",
                    "gene_term": {
                        "preferred_term": "FLNB",
                        "term": {"id": "hgnc:3775", "label": "FLNB"},
                    },
                    "evidence": [{"reference": "PMID:20"}],
                }
            ],
        },
    )

    g2p_path = tmp_path / "genes.csv"
    _write_g2p_csv(
        g2p_path,
        [
            {
                "g2p id": "GFAP1",
                "gene symbol": "GFAP",
                "gene mim": "",
                "hgnc id": "4235",
                "previous gene symbols": "",
                "disease name": "GFAP-related Alexander disease",
                "disease mim": "",
                "disease MONDO": "MONDO:0008752",
                "allelic requirement": "",
                "cross cutting modifier": "",
                "confidence": "definitive",
                "variant consequence": "",
                "variant types": "",
                "molecular mechanism": "",
                "molecular mechanism support": "",
                "molecular mechanism categorisation": "",
                "molecular mechanism evidence": "",
                "phenotypes": "",
                "publications": "10",
                "additional mined publications": "",
                "panel": "",
                "comments": "",
                "date of last review": "",
                "review": "",
            },
            {
                "g2p id": "FLNB1",
                "gene symbol": "FLNB",
                "gene mim": "",
                "hgnc id": "3775",
                "previous gene symbols": "",
                "disease name": "FLNB-related atelosteogenesis, type 1",
                "disease mim": "",
                "disease MONDO": "MONDO:0007167",
                "allelic requirement": "",
                "cross cutting modifier": "",
                "confidence": "definitive",
                "variant consequence": "",
                "variant types": "",
                "molecular mechanism": "",
                "molecular mechanism support": "",
                "molecular mechanism categorisation": "",
                "molecular mechanism evidence": "",
                "phenotypes": "",
                "publications": "20",
                "additional mined publications": "",
                "panel": "",
                "comments": "",
                "date of last review": "",
                "review": "",
            },
        ],
    )

    summaries = survey_genes(["GFAP", "FLNB"], kb_dir=kb_dir, g2p_source=str(g2p_path))

    assert [summary["gene_symbol"] for summary in summaries] == ["FLNB", "GFAP"]
    assert summaries[0]["direct_section_pmid_overlap_count"] == 1
    assert summaries[1]["direct_section_pmid_overlap_count"] == 1
    assert summaries[0]["highest_curation_priority"] == "LOW"
    assert summaries[1]["highest_curation_priority"] == "LOW"


def test_compare_tsv_output_does_not_leak_summary_to_stdout(tmp_path: Path) -> None:
    kb_dir, g2p_path = _build_single_gene_fixture(tmp_path)
    output_path = tmp_path / "report.tsv"

    runner = CliRunner(mix_stderr=False)
    result = runner.invoke(
        g2p_compare_app,
        [
            "compare",
            "PTEN",
            "--kb-dir",
            str(kb_dir),
            "--g2p-source",
            str(g2p_path),
            "--format",
            "tsv",
            "--output",
            str(output_path),
        ],
    )

    assert result.exit_code == 0
    assert result.stdout == ""
    assert "Gene: PTEN" in result.stderr
    output_text = output_path.read_text(encoding="utf-8")
    assert output_text.startswith("gene_symbol\tg2p_id\tg2p_disease_name")
    assert "Gene: PTEN" not in output_text


def test_release_overview_counts_priorities_and_actions(tmp_path: Path) -> None:
    kb_dir = tmp_path / "kb"
    kb_dir.mkdir()

    _write_yaml(
        kb_dir / "Alpha.yaml",
        {
            "name": "Alpha Disorder",
            "disease_term": {"term": {"id": "MONDO:1", "label": "alpha disorder"}},
            "genetic": [
                {
                    "name": "GENE1",
                    "association": "Causative",
                    "gene_term": {
                        "preferred_term": "GENE1",
                        "term": {"id": "hgnc:1", "label": "GENE1"},
                    },
                    "evidence": [{"reference": "PMID:10"}],
                }
            ],
        },
    )

    g2p_path = tmp_path / "genes.csv"
    _write_g2p_csv(
        g2p_path,
        [
            {
                "g2p id": "GENE1_ROW",
                "gene symbol": "GENE1",
                "gene mim": "",
                "hgnc id": "1",
                "previous gene symbols": "",
                "disease name": "GENE1-related alpha disorder",
                "disease mim": "",
                "disease MONDO": "MONDO:1",
                "allelic requirement": "",
                "cross cutting modifier": "",
                "confidence": "definitive",
                "variant consequence": "",
                "variant types": "",
                "molecular mechanism": "",
                "molecular mechanism support": "",
                "molecular mechanism categorisation": "",
                "molecular mechanism evidence": "",
                "phenotypes": "",
                "publications": "10",
                "additional mined publications": "",
                "panel": "",
                "comments": "",
                "date of last review": "",
                "review": "",
            },
            {
                "g2p id": "GENE2_ROW",
                "gene symbol": "GENE2",
                "gene mim": "",
                "hgnc id": "2",
                "previous gene symbols": "",
                "disease name": "GENE2-related missing disorder",
                "disease mim": "",
                "disease MONDO": "MONDO:2",
                "allelic requirement": "",
                "cross cutting modifier": "",
                "confidence": "definitive",
                "variant consequence": "",
                "variant types": "",
                "molecular mechanism": "",
                "molecular mechanism support": "",
                "molecular mechanism categorisation": "",
                "molecular mechanism evidence": "",
                "phenotypes": "",
                "publications": "20",
                "additional mined publications": "",
                "panel": "",
                "comments": "",
                "date of last review": "",
                "review": "",
            },
        ],
    )

    report_gene1 = compare_gene("GENE1", kb_dir=kb_dir, g2p_source=str(g2p_path))
    report_gene2 = compare_gene("GENE2", kb_dir=kb_dir, g2p_source=str(g2p_path))
    summaries = [report_gene1["summary"], report_gene2["summary"]]
    rows = build_release_row_table([report_gene1, report_gene2])
    overview = compute_release_overview([report_gene1, report_gene2], summaries)

    assert [row["gene_symbol"] for row in rows] == ["GENE2", "GENE1"]
    assert overview["total_genes"] == 2
    assert overview["total_rows"] == 2
    assert overview["total_actionable_rows"] == 1
    assert overview["row_status_counts"] == {
        "NO_DISMECH_MATCH": 1,
        "ROOT_MATCH": 1,
    }
    assert overview["genes_by_highest_priority"] == {"CRITICAL": 1, "LOW": 1}
