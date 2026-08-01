"""Tests for the statistical phenotype-distribution schema and tooling.

Covers three things: that the schema and its worked examples stay valid, that
the lint catches the inconsistencies the schema itself cannot express, and that
the reference-cache export keeps the contract curator-quoted snippets depend on.
"""

from __future__ import annotations

import copy
from pathlib import Path

import pytest
from linkml_runtime.utils.schemaview import SchemaView

from dismech.phenotype_distribution import (
    Collection,
    cache_entry,
    discover_collections,
    lint_collections,
    load_collection,
    render_body,
    summary_row,
    write_cache_files,
)
from dismech.reference_cache_frontmatter import main as frontmatter_main

SCHEMA_PATH = Path("src/dismech/schema/phenotype_distribution.yaml")
EXAMPLES_DIR = Path("examples/phenotype_distributions")
KB_DIR = Path("kb/phenotype_distributions")

TARGET_CLASS = "PhenotypeDistributionCollection"


def _example_paths() -> list[Path]:
    return sorted(EXAMPLES_DIR.glob("*.yaml"))


def _all_paths() -> list[Path]:
    return sorted(EXAMPLES_DIR.glob("*.yaml")) + sorted(KB_DIR.glob("*.yaml"))


# ---------------------------------------------------------------------------
# Schema
# ---------------------------------------------------------------------------


def test_schema_loads_with_single_tree_root() -> None:
    sv = SchemaView(str(SCHEMA_PATH))
    roots = [name for name, cls in sv.all_classes().items() if cls.tree_root]
    assert roots == [TARGET_CLASS]


def test_evidence_direction_values_match_native_dismech_support_enum() -> None:
    """SEPIO direction must stay inter-convertible with native `supports`.

    The whole point of copying the vocabulary is that a native evidence item
    and a SEPIO evidence line say "SUPPORT" the same way; a drift here would
    silently break that.
    """
    sv = SchemaView(str(SCHEMA_PATH))
    native = SchemaView("src/dismech/schema/dismech.yaml")
    ours = set(sv.get_enum("EvidenceDirectionEnum").permissible_values)
    theirs = set(native.get_enum("EvidenceItemSupportEnum").permissible_values)
    assert ours == theirs


def test_frequency_class_values_match_native_frequency_enum() -> None:
    """Implied frequency bands must be the same bands dismech already uses."""
    sv = SchemaView(str(SCHEMA_PATH))
    native = SchemaView("src/dismech/schema/dismech.yaml")
    ours = sv.get_enum("FrequencyClassEnum").permissible_values
    theirs = native.get_enum("FrequencyEnum").permissible_values
    assert set(ours) == set(theirs)
    for name, pv in ours.items():
        assert pv.meaning == theirs[name].meaning


def test_model_layer_stays_at_the_common_denominator() -> None:
    """Model-family-specific structure belongs in `model_properties`.

    Latent phenotype model classes and their export shapes change fast. The
    escape hatch is what keeps a new one recordable without a schema change, so
    it must exist and the model class must carry it.
    """
    sv = SchemaView(str(SCHEMA_PATH))
    assert "ModelProperty" in sv.all_classes()
    model_slots = set(sv.class_slots("LatentPhenotypeModel"))
    assert "model_properties" in model_slots
    # Structure belonging to one family must not have become a first-class slot.
    family_specific = {
        "gating",
        "group_variable",
        "groups",
        "group_proportions",
        "background_only_proportion",
        "topic_blocks",
        "eta_scale",
    }
    assert not (model_slots & family_specific)


@pytest.mark.parametrize("path", _all_paths(), ids=lambda p: p.name)
def test_collections_validate_against_schema(path: Path) -> None:
    from linkml.validator import validate_file

    report = validate_file(str(path), str(SCHEMA_PATH), TARGET_CLASS)
    assert not report.results, [r.message for r in report.results]


# ---------------------------------------------------------------------------
# Lint
# ---------------------------------------------------------------------------


def test_examples_lint_clean() -> None:
    result = lint_collections(discover_collections(_all_paths()))
    assert result.errors == [], [i.format() for i in result.errors]
    assert result.warnings == [], [i.format() for i in result.warnings]
    assert result.n_records > 0


def _mutate(path: Path, mutator) -> Collection:
    coll = load_collection(path)
    coll = Collection(path=coll.path, data=copy.deepcopy(coll.data))
    mutator(coll.data)
    return coll


@pytest.fixture()
def cf_collection_path() -> Path:
    return EXAMPLES_DIR / "cystic_fibrosis_illustrative.yaml"


def _error_messages(coll: Collection) -> str:
    return " ".join(i.message for i in lint_collections([coll]).errors)


def test_lint_flags_duplicate_record_ids(cf_collection_path: Path) -> None:
    def mutate(data):
        data["distributions"][1]["record_id"] = data["distributions"][0]["record_id"]

    assert "duplicate record_id" in _error_messages(_mutate(cf_collection_path, mutate))


def test_lint_flags_mismatched_evidence_reference(cf_collection_path: Path) -> None:
    def mutate(data):
        data["distributions"][0]["dismech_bindings"][0]["evidence_reference"] = (
            "PHENODIST:something-else"
        )

    assert "does not match this record" in _error_messages(
        _mutate(cf_collection_path, mutate)
    )


def test_lint_flags_unresolvable_target_entry(cf_collection_path: Path) -> None:
    def mutate(data):
        data["distributions"][0]["dismech_bindings"][0]["target_entry"] = "No_Such_Disease"

    assert "does not" in _error_messages(_mutate(cf_collection_path, mutate))


def test_lint_flags_interval_not_bracketing_point_estimate(
    cf_collection_path: Path,
) -> None:
    def mutate(data):
        data["distributions"][0]["distribution"]["summary"]["point_estimate"] = 0.99

    assert "above the interval upper bound" in _error_messages(
        _mutate(cf_collection_path, mutate)
    )


def test_lint_flags_frequency_band_contradicting_point_estimate(
    cf_collection_path: Path,
) -> None:
    def mutate(data):
        data["distributions"][0]["implied_frequency_class"] = "OCCASIONAL"

    assert "falls in the VERY_FREQUENT band" in _error_messages(
        _mutate(cf_collection_path, mutate)
    )


def test_lint_flags_self_contradictory_identity_attestation(
    cf_collection_path: Path,
) -> None:
    def mutate(data):
        att = data["distributions"][0]["cohort"]["identity_attestation"]
        att["unique_person_count"] = 900

    assert "one row per person" in _error_messages(_mutate(cf_collection_path, mutate))


def test_lint_flags_matrix_dimension_mismatch() -> None:
    path = EXAMPLES_DIR / "charmpheno_population_eds.yaml"

    def mutate(data):
        for record in data["distributions"]:
            for param in record["distribution"].get("parameters") or []:
                if param.get("matrix_value"):
                    param["matrix_value"]["values"].pop()
                    return

    assert "entries but lists" in _error_messages(_mutate(path, mutate))


def test_lint_flags_latent_mixture_without_a_model() -> None:
    path = EXAMPLES_DIR / "charmpheno_population_eds.yaml"

    def mutate(data):
        del data["model"]

    assert "declares no `model`" in _error_messages(_mutate(path, mutate))


# ---------------------------------------------------------------------------
# Reference-cache export
# ---------------------------------------------------------------------------


def test_summary_row_column_contract(cf_collection_path: Path) -> None:
    """The quotable summary row's column order is part of the cache contract.

    Curators quote this row as an evidence snippet, so reordering or dropping a
    column silently invalidates every snippet already quoted from it.
    """
    coll = load_collection(cf_collection_path)
    record = coll.records[0]
    row = summary_row(record)
    cells = [c.strip() for c in row.strip().strip("|").split("|")]
    assert cells == [
        "CF-PI-PROPORTION-001",
        "PHENOTYPE_PROPORTION",
        "BETA",
        "0.862",
        "95% CREDIBLE_EQUAL_TAILED 0.842-0.881",
        "n=1240",
        "whole cohort",
    ]


def test_render_is_deterministic(cf_collection_path: Path) -> None:
    coll = load_collection(cf_collection_path)
    record = coll.records[0]
    assert render_body(coll, record) == render_body(coll, record)


def test_cache_entry_identifier_and_filename(cf_collection_path: Path) -> None:
    coll = load_collection(cf_collection_path)
    entry = cache_entry(coll, coll.records[0])
    assert entry.reference_id == "PHENODIST:CF-PI-PROPORTION-001"
    assert entry.filename() == "PHENODIST_CF-PI-PROPORTION-001.md"
    assert entry.title.endswith("in Cystic Fibrosis")


def test_rendered_body_contains_the_quotable_summary_row(
    cf_collection_path: Path,
) -> None:
    coll = load_collection(cf_collection_path)
    record = coll.records[0]
    assert summary_row(record) in render_body(coll, record)


def test_table_cells_never_contain_unescaped_pipes(cf_collection_path: Path) -> None:
    """A stray pipe in free text must not break a quotable row."""
    coll = load_collection(cf_collection_path)
    coll = Collection(path=coll.path, data=copy.deepcopy(coll.data))
    coll.data["distributions"][0]["measure_description"] = "a | b | c"
    body = render_body(coll, coll.records[0])
    line = next(ln for ln in body.splitlines() if ln.startswith("| Measure description"))
    assert line.count("|") - line.count(r"\|") == 3  # two delimiters + separator


def test_suppressed_bins_render_distinguishably_from_zero() -> None:
    """A withheld bin and a reported zero must not look the same in the cache."""
    path = EXAMPLES_DIR / "charmpheno_population_eds.yaml"
    coll = load_collection(path)
    record = next(
        r for r in coll.records if r["record_id"] == "CHARMPHENO-EDS-T96-THETA-001"
    )
    body = render_body(coll, record)
    bin_rows = [ln for ln in body.splitlines() if ln.startswith("| [0.")]
    suppressed = [ln for ln in bin_rows if ln.rstrip().endswith("true |")]
    reported_zero = [ln for ln in bin_rows if "| 0 |" in ln]
    assert suppressed, bin_rows
    assert reported_zero, bin_rows
    assert not set(suppressed) & set(reported_zero)


def test_written_cache_files_satisfy_the_frontmatter_contract(
    tmp_path: Path,
) -> None:
    collections = discover_collections(_all_paths())
    written = write_cache_files(collections, tmp_path)
    assert written
    assert frontmatter_main([str(tmp_path)]) == 0


def test_write_cache_files_is_idempotent(tmp_path: Path) -> None:
    collections = discover_collections(_all_paths())
    write_cache_files(collections, tmp_path)
    first = {p.name: p.read_bytes() for p in tmp_path.glob("*.md")}
    write_cache_files(collections, tmp_path)
    second = {p.name: p.read_bytes() for p in tmp_path.glob("*.md")}
    assert first == second


def test_no_temporary_files_left_behind(tmp_path: Path) -> None:
    write_cache_files(discover_collections(_all_paths()), tmp_path)
    assert not list(tmp_path.glob("*.tmp"))


# ---------------------------------------------------------------------------
# Repository hygiene
# ---------------------------------------------------------------------------


def test_example_collections_are_not_citable_from_kb_entries() -> None:
    """Illustrative records carry synthetic numbers and must stay uncited.

    They are still linted and rendered so the tooling is exercised, but nothing
    under kb/ may cite one, and no cache file for one may be committed.
    """
    example_ids = {
        record["record_id"]
        for coll in discover_collections(_example_paths())
        for record in coll.records
    }
    assert example_ids

    cited = set()
    for path in Path("kb").rglob("*.yaml"):
        text = path.read_text(encoding="utf-8")
        if "PHENODIST:" not in text:
            continue
        for rid in example_ids:
            if f"PHENODIST:{rid}" in text:
                cited.add((path.name, rid))
    assert not cited, f"kb entries cite illustrative records: {sorted(cited)}"

    committed = [
        p.name
        for rid in example_ids
        if (p := Path("references_cache") / f"PHENODIST_{rid}.md").exists()
    ]
    assert not committed, f"illustrative cache files are committed: {sorted(committed)}"
