"""Tests for the gene-activity-grounding ratchet (scripts/check_gene_activity_grounding.py)."""

from __future__ import annotations

import importlib.util
import sys
from collections import Counter
from pathlib import Path

import pytest

ROOT = Path(__file__).parent.parent
SCRIPT_PATH = ROOT / "scripts" / "check_gene_activity_grounding.py"
SPEC = importlib.util.spec_from_file_location(
    "check_gene_activity_grounding", SCRIPT_PATH
)
assert SPEC and SPEC.loader
check = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = check
SPEC.loader.exec_module(check)


@pytest.mark.ci_step_twin("scripts/check_gene_activity_grounding.py")
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


def test_ref_mode_honors_only_lines_the_branch_adds(monkeypatch):
    """In ref mode only the committed lines a branch *adds or raises* count.

    A genuinely MF-less node a PR adds (absent from the base branch) is
    grandfathered by a committed-baseline line even under ``--against-ref`` --
    what dismech#12669 needed and what the gate's docstring already promised.
    But a stale-high line identical on both sides, for a gene since grounded on
    the base branch, must NOT be honored: otherwise a later PR could strip that
    molecular function with CI still green. ``committed_head - committed_ref``
    keeps only the added/raised lines; ``from_ref | exemptions`` is per-key max.
    """
    monkeypatch.setattr(
        check,
        "baseline_from_ref",
        lambda ref, root=check.ROOT: Counter(
            {"kb/disorders/OnMain.yaml\tFOO": 2}  # live base-branch finding
        ),
    )
    # HEAD's committed file: a new exemption, a raised count, and a stale line.
    monkeypatch.setattr(
        check,
        "load_baseline",
        lambda path=check.BASELINE_PATH: Counter(
            {
                "kb/disorders/New.yaml\tBAR": 1,  # added by this branch
                "kb/disorders/Raised.yaml\tBAZ": 2,  # raised 1 -> 2 by this branch
                "kb/disorders/Fixed.yaml\tOLD": 1,  # stale: identical at the ref
            }
        ),
    )
    # The ref's committed file: the raised line at its lower count, plus the
    # stale line unchanged. New.yaml is absent (this branch introduced it).
    monkeypatch.setattr(
        check,
        "baseline_at_ref",
        lambda ref, root=check.ROOT: Counter(
            {
                "kb/disorders/Raised.yaml\tBAZ": 1,
                "kb/disorders/Fixed.yaml\tOLD": 1,
            }
        ),
    )
    merged = check.resolve_baseline("origin/main")
    assert merged == Counter(
        {
            "kb/disorders/OnMain.yaml\tFOO": 2,  # from the base branch findings
            "kb/disorders/New.yaml\tBAR": 1,  # added exemption, honored
            "kb/disorders/Raised.yaml\tBAZ": 2,  # raised line honored at its full count
        }
    )
    # The reviewer's case: the stale line (identical at ref and HEAD, absent
    # from from_ref) grandfathers nothing, so stripping that gene's MF regresses.
    assert check.new_findings([("kb/disorders/Fixed.yaml", "OLD")], merged) == [
        ("kb/disorders/Fixed.yaml", "OLD")
    ]
    # The added exemption passes; a second, un-exempted occurrence still fails.
    assert check.new_findings(
        [("kb/disorders/New.yaml", "BAR"), ("kb/disorders/New.yaml", "BAR")], merged
    ) == [("kb/disorders/New.yaml", "BAR")]


def test_ref_mode_falls_back_to_committed_when_ref_unreadable(monkeypatch):
    """An unreadable ref still falls back to the committed baseline alone."""
    monkeypatch.setattr(check, "baseline_from_ref", lambda ref, root=check.ROOT: None)
    sentinel = Counter({"kb/disorders/X.yaml\tACP2": 1})
    monkeypatch.setattr(check, "load_baseline", lambda path=check.BASELINE_PATH: sentinel)
    assert check.resolve_baseline("origin/does-not-exist") == sentinel


def test_baseline_at_ref_returns_empty_when_blob_unreadable(monkeypatch):
    """A ref with no baseline blob yields an empty Counter, not an error."""

    class _Proc:
        returncode = 128
        stdout = b""

    monkeypatch.setattr(check.subprocess, "run", lambda *a, **k: _Proc())
    assert check.baseline_at_ref("origin/nonexistent") == Counter()


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
