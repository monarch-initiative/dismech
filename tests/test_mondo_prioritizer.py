from __future__ import annotations

import csv
import json
from copy import deepcopy
from pathlib import Path

import pytest
import yaml
from typer.testing import CliRunner

from dismech.compare.mondo_priority import app
from dismech.compare.mondo_priority import build_coverage_index
from dismech.compare.mondo_priority import load_candidates
from dismech.compare.mondo_priority import load_config
from dismech.compare.mondo_priority import score_candidates


def _write_yaml(path: Path, payload: dict) -> None:
    path.write_text(yaml.safe_dump(payload, sort_keys=False), encoding="utf-8")


def _write_candidate_tsv(path: Path, rows: list[dict[str, str]]) -> None:
    fieldnames = [
        "mondo_id",
        "label",
        "definition",
        "synonyms",
        "parents",
        "xrefs",
        "child_count",
        "clingen_definitive_count",
        "clingen_strong_count",
        "subset_match_count",
        "orphanet_match_count",
        "is_obsolete",
    ]
    with path.open("w", newline="", encoding="utf-8") as stream:
        writer = csv.DictWriter(stream, fieldnames=fieldnames, delimiter="\t")
        writer.writeheader()
        writer.writerows(rows)


def _write_json(path: Path, payload: list[dict[str, str]]) -> None:
    path.write_text(json.dumps(payload, indent=2), encoding="utf-8")


def _write_jsonl(path: Path, rows: list[dict[str, str]]) -> None:
    path.write_text(
        "\n".join(json.dumps(row, sort_keys=True) for row in rows) + "\n",
        encoding="utf-8",
    )


def _build_candidate_rows() -> list[dict[str, str]]:
    return [
        {
            "mondo_id": "MONDO:0002442",
            "label": "long QT syndrome",
            "definition": "Inherited repolarization disorder with ventricular arrhythmia risk.",
            "synonyms": "LQTS; long-qt syndrome",
            "parents": "cardiac channelopathy; arrhythmia syndrome",
            "xrefs": "OMIM:192500|Orphanet:101019",
            "child_count": "16",
            "clingen_definitive_count": "3",
            "clingen_strong_count": "0",
            "subset_match_count": "1",
            "orphanet_match_count": "1",
            "is_obsolete": "false",
        },
        {
            "mondo_id": "MONDO:0100316",
            "label": "long QT syndrome 1",
            "definition": "KCNQ1-related subtype of long QT syndrome.",
            "synonyms": "LQT1",
            "parents": "long QT syndrome",
            "xrefs": "OMIM:192500",
            "child_count": "0",
            "clingen_definitive_count": "1",
            "clingen_strong_count": "0",
            "subset_match_count": "1",
            "orphanet_match_count": "1",
            "is_obsolete": "false",
        },
        {
            "mondo_id": "MONDO:0011377",
            "label": "long QT syndrome 3",
            "definition": "SCN5A-related subtype of long QT syndrome.",
            "synonyms": "LQT3",
            "parents": "long QT syndrome",
            "xrefs": "OMIM:603830",
            "child_count": "0",
            "clingen_definitive_count": "1",
            "clingen_strong_count": "0",
            "subset_match_count": "1",
            "orphanet_match_count": "1",
            "is_obsolete": "false",
        },
        {
            "mondo_id": "MONDO:0010342",
            "label": "autism, susceptibility to, X-linked 3",
            "definition": "MECP2-linked susceptibility signal for autism spectrum presentations.",
            "synonyms": "AUTSX3",
            "parents": "neurodevelopmental disorder",
            "xrefs": "OMIM:300496",
            "child_count": "0",
            "clingen_definitive_count": "0",
            "clingen_strong_count": "0",
            "subset_match_count": "1",
            "orphanet_match_count": "0",
            "is_obsolete": "false",
        },
        {
            "mondo_id": "MONDO:0018997",
            "label": "Noonan syndrome",
            "definition": "RASopathy with congenital heart disease and characteristic facies.",
            "synonyms": "Noonan syndrome 1 spectrum",
            "parents": "RASopathy",
            "xrefs": "OMIM:163950|Orphanet:648",
            "child_count": "6",
            "clingen_definitive_count": "3",
            "clingen_strong_count": "1",
            "subset_match_count": "1",
            "orphanet_match_count": "1",
            "is_obsolete": "false",
        },
        {
            "mondo_id": "MONDO:0060577",
            "label": "neurodevelopmental disorder with microcephaly, ataxia, and seizures",
            "definition": "Rare syndromic neurodevelopmental disease defined by severe neurologic phenotype triad.",
            "synonyms": "microcephaly-ataxia-seizures syndrome",
            "parents": "neurodevelopmental disorder",
            "xrefs": "OMIM:620114",
            "child_count": "0",
            "clingen_definitive_count": "1",
            "clingen_strong_count": "0",
            "subset_match_count": "1",
            "orphanet_match_count": "0",
            "is_obsolete": "false",
        },
        {
            "mondo_id": "MONDO:0016343",
            "label": "obsolete unclassified cardiomyopathy",
            "definition": "Deprecated umbrella cardiomyopathy term retained for mapping history.",
            "synonyms": "",
            "parents": "deprecated cardiomyopathy",
            "xrefs": "",
            "child_count": "0",
            "clingen_definitive_count": "0",
            "clingen_strong_count": "0",
            "subset_match_count": "0",
            "orphanet_match_count": "0",
            "is_obsolete": "true",
        },
    ]


def _build_kb_dir(tmp_path: Path) -> Path:
    kb_dir = tmp_path / "kb"
    kb_dir.mkdir()
    _write_yaml(
        kb_dir / "Noonan_Syndrome.yaml",
        {
            "name": "Noonan Syndrome",
            "disease_term": {
                "term": {"id": "MONDO:0018997", "label": "Noonan syndrome"}
            },
        },
    )
    return kb_dir


def test_scoring_assigns_expected_specificity_buckets_and_actions(
    tmp_path: Path,
) -> None:
    kb_dir = _build_kb_dir(tmp_path)
    candidate_path = tmp_path / "candidates.tsv"
    _write_candidate_tsv(candidate_path, _build_candidate_rows())

    config = load_config()
    coverage = build_coverage_index(kb_dir)
    results = score_candidates(load_candidates(candidate_path), coverage, config)
    by_label = {row.label: row for row in results}

    assert (
        by_label["long QT syndrome"].recommended_action == "CURATE_ROOT_WITH_SUBTYPES"
    )
    assert by_label["long QT syndrome"].specificity_bucket == "broad_parent"

    assert by_label["long QT syndrome 1"].recommended_action == "LUMP_INTO_PARENT"
    assert by_label["long QT syndrome 1"].specificity_bucket == "subtype_series"

    assert (
        by_label["autism, susceptibility to, X-linked 3"].recommended_action
        == "DROP_GROUPING_TERM"
    )
    assert (
        by_label["autism, susceptibility to, X-linked 3"].specificity_bucket
        == "grouping_term"
    )

    assert by_label["Noonan syndrome"].recommended_action == "ALREADY_CURATED"
    assert by_label["Noonan syndrome"].curated_match == "Noonan_Syndrome.yaml"

    assert (
        by_label[
            "neurodevelopmental disorder with microcephaly, ataxia, and seizures"
        ].recommended_action
        == "REVIEW_AGAINST_PARENT"
    )

    assert by_label["long QT syndrome"].score > by_label["long QT syndrome 1"].score
    assert (
        by_label["long QT syndrome 1"].score
        > by_label["autism, susceptibility to, X-linked 3"].score
    )
    assert by_label["obsolete unclassified cardiomyopathy"].score < 0


def test_mondo_id_match_falls_back_to_file_when_label_differs(tmp_path: Path) -> None:
    kb_dir = tmp_path / "kb"
    kb_dir.mkdir()
    _write_yaml(
        kb_dir / "Long_QT_Syndrome.yaml",
        {
            "name": "LQT Syndrome",
            "disease_term": {
                "term": {"id": "MONDO:0002442", "label": "long QT syndrome"}
            },
        },
    )
    candidate_path = tmp_path / "candidates.tsv"
    _write_candidate_tsv(
        candidate_path,
        [row for row in _build_candidate_rows() if row["mondo_id"] == "MONDO:0002442"],
    )

    results = score_candidates(
        load_candidates(candidate_path),
        coverage=build_coverage_index(kb_dir),
        config=load_config(),
    )

    assert len(results) == 1
    assert results[0].recommended_action == "ALREADY_CURATED"
    assert results[0].curated_match == "Long_QT_Syndrome.yaml"
    assert results[0].score < 0


def test_config_override_changes_weighted_score(tmp_path: Path) -> None:
    kb_dir = _build_kb_dir(tmp_path)
    candidate_path = tmp_path / "candidates.tsv"
    _write_candidate_tsv(candidate_path, _build_candidate_rows())
    candidates = load_candidates(candidate_path)
    coverage = build_coverage_index(kb_dir)

    baseline_config = load_config()
    baseline = {
        row.label: row
        for row in score_candidates(
            candidates, coverage=coverage, config=baseline_config
        )
    }

    custom_config = deepcopy(baseline_config)
    custom_config["weights"]["subset_match_count"] = 25
    rescored = {
        row.label: row
        for row in score_candidates(candidates, coverage=coverage, config=custom_config)
    }

    assert (
        rescored["long QT syndrome"].score - baseline["long QT syndrome"].score
    ) == 20
    assert (
        rescored["long QT syndrome 1"].score - baseline["long QT syndrome 1"].score
    ) == 20


def test_load_candidates_accepts_json_and_jsonl(tmp_path: Path) -> None:
    rows = _build_candidate_rows()[:2]
    json_path = tmp_path / "candidates.json"
    jsonl_path = tmp_path / "candidates.jsonl"
    _write_json(json_path, rows)
    _write_jsonl(jsonl_path, rows)

    json_candidates = load_candidates(json_path)
    jsonl_candidates = load_candidates(jsonl_path)

    assert [candidate.mondo_id for candidate in json_candidates] == [
        "MONDO:0002442",
        "MONDO:0100316",
    ]
    assert [candidate.mondo_id for candidate in jsonl_candidates] == [
        "MONDO:0002442",
        "MONDO:0100316",
    ]


def test_load_candidates_rejects_rows_missing_required_fields(tmp_path: Path) -> None:
    bad_path = tmp_path / "bad.json"
    _write_json(
        bad_path,
        [
            {
                "label": "missing mondo id",
                "definition": "invalid candidate row",
            }
        ],
    )

    with pytest.raises(ValueError, match="MONDO id and label"):
        load_candidates(bad_path)


def test_cli_scores_candidates_end_to_end(tmp_path: Path) -> None:
    kb_dir = _build_kb_dir(tmp_path)
    candidate_path = tmp_path / "candidates.tsv"
    _write_candidate_tsv(candidate_path, _build_candidate_rows())

    runner = CliRunner()
    result = runner.invoke(
        app,
        [
            str(candidate_path),
            "--kb-dir",
            str(kb_dir),
            "--format",
            "table",
            "--top",
            "3",
        ],
    )

    assert result.exit_code == 0
    lines = [line for line in result.stdout.strip().splitlines() if line]
    assert lines[0].startswith("score\tmondo_id\tlabel")
    assert "long QT syndrome" in lines[1]
    assert "CURATE_ROOT_WITH_SUBTYPES" in lines[1]
