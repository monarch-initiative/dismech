"""Tests for the gene-activity-grounding ratchet (scripts/check_gene_activity_grounding.py)."""

from __future__ import annotations

import importlib.util
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).parent.parent
SCRIPT_PATH = ROOT / "scripts" / "check_gene_activity_grounding.py"
SPEC = importlib.util.spec_from_file_location(
    "check_gene_activity_grounding", SCRIPT_PATH
)
assert SPEC and SPEC.loader
check = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = check
SPEC.loader.exec_module(check)


def test_no_newly_ungrounded_genes():
    # resolve_baseline() grandfathers against origin/main when CI sets
    # GENE_ACTIVITY_BASELINE_REF (so the base branch is green by construction
    # and parallel merges cannot clobber the grandfather set), and falls back
    # to the committed baseline for local runs / shallow checkouts.
    baseline = check.resolve_baseline()
    new = [
        f"{rel}: {name}"
        for rel, name in check.new_findings(check.scan_repo(), baseline)
    ]
    assert not new, (
        "Gene(s) wired into the pathograph whose landing node names no "
        "molecular function. GO puts a molecular function between a gene and a "
        "biological process; without it the graph says what the cell can no "
        "longer do but not what the protein can no longer do. Bind "
        "`molecular_functions:` on the node the gene reaches:\n  " + "\n  ".join(new)
    )


def _entry(with_mf: bool) -> dict:
    node = {
        "name": "ACP2 Deficiency",
        "gene": {"term": {"id": "hgnc:123", "label": "ACP2"}},
        "biological_processes": [
            {"term": {"id": "GO:0016311", "label": "dephosphorylation"}}
        ],
    }
    if with_mf:
        node["molecular_functions"] = [
            {"term": {"id": "GO:0003993", "label": "acid phosphatase activity"}}
        ]
    return {
        "name": "Test Disorder",
        "genetic": [
            {
                "name": "ACP2",
                "gene_term": {"term": {"id": "hgnc:123", "label": "ACP2"}},
                "relationship_type": "CAUSAL",
            }
        ],
        "pathophysiology": [node],
    }


def _write(tmp_path: Path, name: str, entry: dict) -> Path:
    import yaml

    kb = tmp_path / "kb" / "disorders"
    kb.mkdir(parents=True, exist_ok=True)
    (kb / f"{name}.yaml").write_text(yaml.safe_dump(entry), encoding="utf-8")
    return tmp_path


def test_scan_flags_a_process_only_landing(tmp_path):
    root = _write(tmp_path, "Test_Disorder", _entry(with_mf=False))
    assert check.scan_repo(scan_dir=root / "kb", rel_to=root) == [
        ("kb/disorders/Test_Disorder.yaml", "ACP2")
    ]


def test_scan_accepts_a_landing_node_with_a_molecular_function(tmp_path):
    root = _write(tmp_path, "Test_Disorder", _entry(with_mf=True))
    assert check.scan_repo(scan_dir=root / "kb", rel_to=root) == []


def test_scan_covers_kb_beyond_disorders(tmp_path):
    """kb/modules and kb/comorbidities validate against the same Disease class."""
    entry = _entry(with_mf=False)
    modules = tmp_path / "kb" / "modules"
    modules.mkdir(parents=True)
    import yaml

    (modules / "some_module.yaml").write_text(yaml.safe_dump(entry), encoding="utf-8")
    assert check.scan_repo(scan_dir=tmp_path / "kb", rel_to=tmp_path) == [
        ("kb/modules/some_module.yaml", "ACP2")
    ]


def test_unparseable_yaml_is_skipped_with_a_warning(tmp_path, capsys):
    kb = tmp_path / "kb" / "disorders"
    kb.mkdir(parents=True)
    (kb / "Broken.yaml").write_text("name: [unclosed\n", encoding="utf-8")
    assert check.scan_repo(scan_dir=tmp_path / "kb", rel_to=tmp_path) == []
    assert "skipping unparseable" in capsys.readouterr().err


def test_baseline_grandfathers_a_known_finding():
    findings = [("kb/disorders/X.yaml", "ACP2")]
    baseline = Counter({"kb/disorders/X.yaml\tACP2": 1})
    assert check.new_findings(findings, baseline) == []


def test_a_second_occurrence_beyond_the_baselined_count_is_new():
    """One grandfathered entry must not admit a second of the same name."""
    findings = [("kb/disorders/X.yaml", "ACP2"), ("kb/disorders/X.yaml", "ACP2")]
    baseline = Counter({"kb/disorders/X.yaml\tACP2": 1})
    assert check.new_findings(findings, baseline) == [("kb/disorders/X.yaml", "ACP2")]


def test_baseline_roundtrips(tmp_path):
    findings = [("kb/disorders/X.yaml", "ACP2"), ("kb/disorders/X.yaml", "ACP2")]
    path = tmp_path / "baseline.txt"
    check.write_baseline(findings, path)
    assert check.load_baseline(path) == Counter({"kb/disorders/X.yaml\tACP2": 2})


def test_committed_baseline_is_wellformed():
    """Parses, is non-empty, and every path it names still exists.

    Deliberately not asserting the baseline *equals* the current findings. It is
    allowed to drift stale-high as curation binds terms: a line for a gene that
    is now grounded grandfathers nothing, and requiring every fix to regenerate
    the file would make parallel curation PRs race to update it -- the churn the
    ref-based grandfathering exists to avoid.
    """
    baseline = check.load_baseline()
    assert baseline, "the committed fallback baseline should not be empty"
    missing = [
        key.split("\t")[0]
        for key in baseline
        if not (ROOT / key.split("\t")[0]).exists()
    ]
    assert not missing, (
        f"baseline names files that no longer exist: {sorted(set(missing))}"
    )
