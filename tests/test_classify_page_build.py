"""Tests for the full-vs-incremental page-build classifier (issue #5507)."""

import importlib.util
import sys
from pathlib import Path

_SPEC = importlib.util.spec_from_file_location(
    "classify_page_build",
    Path(__file__).resolve().parents[1] / "scripts" / "classify_page_build.py",
)
classify_page_build = importlib.util.module_from_spec(_SPEC)
# Register before exec so the module's @dataclass can resolve its own module.
sys.modules[_SPEC.name] = classify_page_build
_SPEC.loader.exec_module(classify_page_build)
classify = classify_page_build.classify


def test_single_disorder_is_incremental():
    d = classify([("M", "kb/disorders/Asthma.yaml")])
    assert d.mode == "incremental"
    assert d.disorder_files == ["kb/disorders/Asthma.yaml"]


def test_curation_pr_with_reference_cache_and_history_is_incremental():
    # The common curation PR shape: a disorder edit plus its cached references
    # and a history record. Neutral companions must NOT force a full rebuild.
    d = classify(
        [
            ("M", "kb/disorders/Marfan_Syndrome.yaml"),
            ("A", "references_cache/PMID_12345678.md"),
            ("A", "history/disorders/Marfan_Syndrome/2026-07-06T00Z-claude-code-a1.yaml"),
            ("M", "cache/hp/terms.csv"),
        ]
    )
    assert d.mode == "incremental"
    assert d.disorder_files == ["kb/disorders/Marfan_Syndrome.yaml"]


def test_template_change_forces_full():
    d = classify([("M", "src/dismech/templates/disorder.html.j2")])
    assert d.mode == "full"


def test_render_py_change_forces_full():
    d = classify([("M", "src/dismech/render.py")])
    assert d.mode == "full"


def test_graph_and_export_changes_force_full():
    assert classify([("M", "src/dismech/graph.py")]).mode == "full"
    assert classify([("M", "src/dismech/export/browser_export.py")]).mode == "full"


def test_schema_change_forces_full():
    d = classify([("M", "src/dismech/schema/dismech.yaml")])
    assert d.mode == "full"


def test_justfile_and_conf_force_full():
    assert classify([("M", "project.justfile")]).mode == "full"
    assert classify([("M", "conf/qc_config.yaml")]).mode == "full"


def test_disorder_deletion_forces_full():
    d = classify([("D", "kb/disorders/Old_Disease.yaml")])
    assert d.mode == "full"


def test_disorder_rename_forces_full():
    d = classify([("R100", "kb/disorders/New_Name.yaml")])
    assert d.mode == "full"


def test_comorbidity_only_is_incremental_with_no_disorder_files():
    # A changed comorbidity is re-rendered by the always-run aggregate pass, so
    # no individual disorder page needs rendering.
    d = classify([("M", "kb/comorbidities/com_A__B.yaml")])
    assert d.mode == "incremental"
    assert d.disorder_files == []


def test_module_change_is_incremental():
    d = classify([("M", "kb/modules/fibrotic_response.yaml")])
    assert d.mode == "incremental"
    assert d.disorder_files == []


def test_research_report_is_incremental():
    d = classify([("A", "research/Foo-deep-research-falcon.md")])
    assert d.mode == "incremental"
    assert d.disorder_files == []


def test_history_yaml_is_neutral():
    d = classify([("A", "kb/disorders/Asthma.history.yaml")])
    assert d.mode == "incremental"
    assert d.disorder_files == []


def test_grouping_change_is_neutral_for_this_workflow():
    # Grouping pages are handled by a separate workflow.
    d = classify([("M", "kb/groupings/Mucopolysaccharidoses.yaml")])
    assert d.mode == "incremental"
    assert d.disorder_files == []


def test_docs_only_is_incremental():
    d = classify([("M", "docs/history.md")])
    assert d.mode == "incremental"
    assert d.disorder_files == []


def test_unknown_path_fails_safe_to_full():
    d = classify([("A", "some/unexpected/module.py")])
    assert d.mode == "full"


def test_mixed_local_and_global_is_full():
    d = classify(
        [
            ("M", "kb/disorders/Asthma.yaml"),
            ("M", "src/dismech/templates/disorder.html.j2"),
        ]
    )
    assert d.mode == "full"


def test_multiple_disorders_sorted_and_deduped():
    d = classify(
        [
            ("M", "kb/disorders/Zed.yaml"),
            ("M", "kb/disorders/Asthma.yaml"),
            ("M", "kb/disorders/Asthma.yaml"),
        ]
    )
    assert d.mode == "incremental"
    assert d.disorder_files == ["kb/disorders/Asthma.yaml", "kb/disorders/Zed.yaml"]
