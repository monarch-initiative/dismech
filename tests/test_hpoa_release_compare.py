"""Tests for `scripts/hpoa_release_compare.py`.

These pin the two parsing paths that fail *silently* when they are wrong, which is
what makes them worth a test rather than a careful reading:

* `obo_is_a_target` — mondo.obo qualifies 45% of its `is_a:` lines with a
  `{source=...}` provenance block. Splitting on `!` alone leaves the braces attached,
  yielding a parent id that matches nothing, with no error: Fanconi anemia reported
  zero descendants. See dismech#11869.
* `read_hpoa` — a ragged row used to be padded into a dict missing its tail keys, so a
  malformed export read as a file full of empty values rather than as a malformed file.

The rest cover the subsumption classes and the disease-level join, using fixtures small
enough to check by eye.
"""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
_spec = importlib.util.spec_from_file_location(
    "hpoa_release_compare", ROOT / "scripts" / "hpoa_release_compare.py"
)
assert _spec and _spec.loader
hrc = importlib.util.module_from_spec(_spec)
sys.modules["hpoa_release_compare"] = hrc
_spec.loader.exec_module(hrc)


# --- obo_is_a_target -------------------------------------------------------------


@pytest.mark.parametrize(
    ("line", "expected"),
    [
        ("is_a: HP:0000118", "HP:0000118"),
        ("is_a: HP:0000118 ! Phenotypic abnormality", "HP:0000118"),
        # The case that cost the debugging time: a provenance block before the comment.
        (
            'is_a: MONDO:0019391 {source="OMIM:227650"} ! Fanconi anemia',
            "MONDO:0019391",
        ),
        (
            'is_a: MONDO:0019391 {source="DC-OMIM:227650", source="DOID:0111095"} ! x',
            "MONDO:0019391",
        ),
    ],
)
def test_obo_is_a_target_strips_comments_and_provenance(
    line: str, expected: str
) -> None:
    assert hrc.obo_is_a_target(line) == expected


def test_mondo_children_follows_a_provenance_qualified_edge(tmp_path: Path) -> None:
    """The regression proper: the subtree join is empty if the braces are not stripped."""
    obo = tmp_path / "mondo.obo"
    obo.write_text(
        "[Term]\n"
        "id: MONDO:0019391\n"
        "name: Fanconi anemia\n"
        "\n"
        "[Term]\n"
        "id: MONDO:0009215\n"
        "name: Fanconi anemia complementation group A\n"
        'is_a: MONDO:0019391 {source="OMIM:227650"} ! Fanconi anemia\n',
        encoding="utf-8",
    )
    children = hrc.load_mondo_children(obo)
    assert children["MONDO:0019391"] == {"MONDO:0009215"}
    assert hrc.descendants("MONDO:0019391", children, {}) == {"MONDO:0009215"}


def test_mondo_children_drops_an_obsolete_term(tmp_path: Path) -> None:
    """`is_a:` precedes `is_obsolete:`, so the filter has to run after the parse."""
    obo = tmp_path / "mondo.obo"
    obo.write_text(
        "[Term]\n"
        "id: MONDO:0000001\n"
        "\n"
        "[Term]\n"
        "id: MONDO:0000002\n"
        "is_a: MONDO:0000001 ! parent\n"
        "is_obsolete: true\n",
        encoding="utf-8",
    )
    assert hrc.load_mondo_children(obo)["MONDO:0000001"] == set()


# --- read_hpoa -------------------------------------------------------------------


def _write_hpoa(path: Path, body: str) -> Path:
    path.write_text(
        "#description: test\n#version: 2026-09-02\n"
        "database_id\tdisease_name\tqualifier\thpo_id\n" + body,
        encoding="utf-8",
    )
    return path


def test_read_hpoa_parses_comments_columns_and_rows(tmp_path: Path) -> None:
    path = _write_hpoa(tmp_path / "p.hpoa", "OMIM:1\tDisease\t\tHP:0000118\n")
    comments, columns, rows = hrc.read_hpoa(path)
    assert len(comments) == 2
    assert columns == ["database_id", "disease_name", "qualifier", "hpo_id"]
    assert rows == [
        {
            "database_id": "OMIM:1",
            "disease_name": "Disease",
            "qualifier": "",
            "hpo_id": "HP:0000118",
        }
    ]


def test_read_hpoa_rejects_a_ragged_row(tmp_path: Path) -> None:
    path = _write_hpoa(tmp_path / "p.hpoa", "OMIM:1\tDisease\n")
    with pytest.raises(ValueError, match="expected 4 fields, found 2"):
        hrc.read_hpoa(path)


# --- subsumption scoring ---------------------------------------------------------


def test_score_join_classifies_exact_specific_general_and_novel() -> None:
    # HP:0000002 is-a HP:0000001; HP:0000003 and HP:0000009 are unrelated leaves.
    parents = {"HP:0000002": {"HP:0000001"}}
    dis = {"MONDO:1": {"HP:0000001", "HP:0000002", "HP:0000009", "HP:0000003"}}
    release = {"OMIM:1": {"HP:0000001", "HP:0000003"}}
    # dismech vs release: 0000001 and 0000003 are EXACT; 0000002 is a child of an
    # annotated term (MORE_SPECIFIC); 0000009 is novel.
    totals, rows = score_for(dis, release, parents)
    assert totals["exact"] == 2
    assert totals["more_specific"] == 1
    assert totals["novel"] == 1
    assert rows[0]["novel_terms"] == "HP:0000009"


def test_score_join_counts_a_parent_of_an_annotated_term_as_more_general() -> None:
    parents = {"HP:0000002": {"HP:0000001"}}
    totals, _ = score_for(
        {"MONDO:1": {"HP:0000001"}}, {"OMIM:1": {"HP:0000002"}}, parents
    )
    assert totals["more_general"] == 1
    assert totals["novel"] == 0


def score_for(dis, release, parents):
    return hrc.score_join(
        dis,
        release,
        {m: {"OMIM:1"} for m in dis},
        parents,
        {},
        {m: "Test disease" for m in dis},
    )


# --- the worklist covers non-joining diseases ------------------------------------


def test_merge_join_rows_emits_non_joining_diseases_with_a_status() -> None:
    direct = [
        {
            "mondo_id": "MONDO:1",
            "disease_name": "Joined",
            "hpoa_ids": "OMIM:1",
            "n_dismech": 3,
            "n_hpoa": 2,
            "n_exact": 2,
            "n_more_specific": 0,
            "n_more_general": 0,
            "n_novel": 1,
            "n_hpoa_only": 0,
            "novel_terms": "HP:0000009",
        }
    ]
    rows = hrc.merge_join_rows(
        direct,
        [],
        {"MONDO:1": "Joined", "MONDO:2": "Unmapped", "MONDO:3": "No annotations"},
        {"MONDO:2": "unmapped", "MONDO:3": "mapped_but_unannotated"},
        {"MONDO:1": 3, "MONDO:2": 7, "MONDO:3": 4},
    )
    by_id = {r["mondo_id"]: r for r in rows}
    assert set(by_id) == {"MONDO:1", "MONDO:2", "MONDO:3"}
    assert by_id["MONDO:1"]["join_status"] == "direct"
    assert by_id["MONDO:2"]["join_status"] == "unmapped"
    assert by_id["MONDO:3"]["join_status"] == "mapped_but_unannotated"
    # A non-joining disease keeps its phenotype count and carries empty score columns.
    assert by_id["MONDO:2"]["n_dismech"] == 7
    assert by_id["MONDO:2"]["direct_n_exact"] == ""


# --- value-space reporting -------------------------------------------------------


def test_union_value_table_only_claims_release_only_when_it_is_true() -> None:
    d_rows = [{"aspect": "P"} for _ in range(3)]
    h_rows = [{"aspect": a} for a in ("P", "C", "I", "M")]
    out = hrc.union_value_table(d_rows, h_rows, "aspect", limit=2)
    assert "further values used only by the release." in out

    # If the export populates a value that falls into the hidden tail, drop the claim.
    d_rows = [{"aspect": a} for a in ("P", "P", "C", "I", "M")]
    out = hrc.union_value_table(d_rows, h_rows, "aspect", limit=2)
    assert "further values." in out
    assert "used only by the release" not in out


def test_classify_frequency_matches_the_three_permitted_forms() -> None:
    assert hrc.classify_frequency("HP:0040282") == "HP frequency term"
    assert hrc.classify_frequency("12%") == "percentage"
    assert hrc.classify_frequency("3/7") == "n/m ratio"
    assert hrc.classify_frequency("") == "(empty)"
    # The range forms the export emits, which HPOA does not allow.
    assert hrc.classify_frequency("30-79%") == "other"
    assert hrc.classify_frequency("99-80%") == "other"
