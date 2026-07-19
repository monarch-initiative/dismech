from __future__ import annotations

import sys
from pathlib import Path


sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

import fetch_iembase_diseases as fib  # noqa: E402


def test_extract_disease_index_records_flattens_browse_context() -> None:
    browse_tree = [
        {
            "collection_code": "A",
            "name": "Intermediary Metabolism",
            "disorders_groups": [
                {
                    "name": "Disorders of amino acid metabolism",
                    "icimd_nosology_group_code": 1,
                    "subgroups": [
                        {
                            "name": "Urea cycle disorders",
                            "icimd_nosology_subgroup_code": 1.0,
                            "disorders": [
                                {
                                    "id": 13,
                                    "name": "OTC-related Ornithine transcarbamylase deficiency",
                                    "name_alt1": "Ornithine carbamoyltransferase deficiency",
                                    "name_alt2": None,
                                    "gene_sym": "OTC",
                                    "inheritance": "X-linked",
                                    "icimd_nosology_disorder_num": "1.1.03.01",
                                }
                            ],
                        }
                    ],
                }
            ],
        }
    ]

    rows = fib.extract_disease_index_records(browse_tree)

    assert rows == [
        {
            "id": 13,
            "name": "OTC-related Ornithine transcarbamylase deficiency",
            "name_alt1": "Ornithine carbamoyltransferase deficiency",
            "name_alt2": None,
            "gene_sym": "OTC",
            "inheritance": "X-linked",
            "icimd_nosology_disorder_num": "1.1.03.01",
            "collection_code": "A",
            "collection_name": "Intermediary Metabolism",
            "icimd_nosology_group_code": 1,
            "group_name": "Disorders of amino acid metabolism",
            "icimd_nosology_subgroup_code": 1.0,
            "subgroup_name": "Urea cycle disorders",
            "detail_json": "diseases/13.json",
        }
    ]


def test_extract_disease_index_records_rejects_duplicate_ids() -> None:
    browse_tree = [
        {
            "collection_code": "A",
            "name": "Collection",
            "disorders_groups": [
                {
                    "name": "Group",
                    "subgroups": [
                        {
                            "name": "Subgroup",
                            "disorders": [
                                {"id": 1, "name": "One"},
                                {"id": 1, "name": "One again"},
                            ],
                        }
                    ],
                }
            ],
        }
    ]

    try:
        fib.extract_disease_index_records(browse_tree)
    except ValueError as exc:
        assert "duplicate IEMbase disease ids" in str(exc)
    else:
        raise AssertionError("expected duplicate disease ids to raise ValueError")
