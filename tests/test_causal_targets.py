"""The pathograph's bare-name targets need their own guard.

`dismech.graph` builds edges by matching a `target` string verbatim against
another item's `name`. Nothing resolves it, so a broken target is silent in a
way a broken `attaches_to` is not: the entry passes LinkML validation, term
validation and snippet verification, and the page renders. The edge is still
appended, so the edge count never moves; the unresolved target lands in
`orphan_targets` and the renderer draws it as a phantom duplicate node, orphaning
the real node out of the graph. Issue #10112 found 175 such targets across 32
entries — written with the `<kind>#<name>` entity-reference grammar, which this
slot does not accept — including one entry left with 0 of 7 phenotypes connected.

These tests pin the classification, because the three classes have different
causes and must not collapse into each other.
"""

import subprocess
import sys
from pathlib import Path

# Inline the path rather than assigning ROOT first: ruff's E402 allows an
# import preceded by a `sys.path` preamble, but an intervening assignment
# breaks that allowance, and the two ruff versions this repo sees disagree
# about whether an E402 suppression is then required or itself unused (#9964).
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from check_causal_targets import BARE_TARGET_SLOTS, find_in

ROOT = Path(__file__).parent.parent
SCRIPT = ROOT / "scripts" / "check_causal_targets.py"


def _entry(**sections):
    return sections


def test_prefixed_target_that_would_resolve_is_a_hard_finding():
    """The #10112 defect: entity-ref grammar in a bare-name slot."""
    data = _entry(
        pathophysiology=[
            {"name": "Node A", "downstream": [{"target": "phenotypes#Bleeding"}]}
        ],
        phenotypes=[{"name": "Bleeding"}],
    )
    findings = find_in(data, "x.yaml")
    assert [(f.kind, f.target) for f in findings] == [
        ("prefixed", "phenotypes#Bleeding")
    ]


def test_bare_target_naming_a_real_node_is_clean():
    data = _entry(
        pathophysiology=[{"name": "Node A", "downstream": [{"target": "Bleeding"}]}],
        phenotypes=[{"name": "Bleeding"}],
    )
    assert find_in(data, "x.yaml") == []


def test_renamed_node_leaves_a_dangling_target():
    """The #9697 defect: a rename silently severs the graph."""
    data = _entry(
        pathophysiology=[{"name": "Node A", "downstream": [{"target": "Bleeding"}]}],
        phenotypes=[{"name": "Bleeding diathesis"}],
    )
    findings = find_in(data, "x.yaml")
    assert [(f.kind, f.target) for f in findings] == [("dangling", "Bleeding")]


def test_prefixed_target_that_would_not_resolve_is_dangling_not_prefixed():
    """A prefix is only 'mechanically fixable' if the bare form names something.

    `imaging_findings#...` in Charcot-Marie-Tooth_Disease_Type_4K points at a
    real curated item, but `imaging_findings` is not a graph node section, so
    stripping the prefix would convert a visible error into a silent one. It is
    a curator's call, so it is classified as dangling (and baselined) rather
    than reported as a mechanical fix.
    """
    data = _entry(
        pathophysiology=[
            {"name": "Node A", "downstream": [{"target": "imaging_findings#Lesion"}]}
        ],
    )
    findings = find_in(data, "x.yaml")
    assert [f.kind for f in findings] == ["dangling"]


def test_self_referential_target_is_its_own_class():
    """#9896 — reported, never gated; see the script docstring for why."""
    data = _entry(
        pathophysiology=[{"name": "Node A", "downstream": [{"target": "Node A"}]}]
    )
    assert [f.kind for f in find_in(data, "x.yaml")] == ["self"]


def test_experiment_readout_targets_are_not_checked_here():
    """`proposed_experiments` readouts/perturbations use the ref grammar legitimately.

    Including them would flag ~650 correct references; `check_entity_refs.py`
    owns that slot.
    """
    slots = {slot for _, slot in BARE_TARGET_SLOTS}
    assert "readouts" not in slots
    assert "perturbations" not in slots


def test_stale_baseline_rows_are_reported_without_failing(
    tmp_path, monkeypatch, capsys
):
    """A fixed target's row must not silently inflate the grandfathered count.

    The baseline's value is that its size measures remaining debt. A row left
    behind after its target was repaired makes the backlog look larger than it
    is, and before this nothing would ever have said so.
    """
    import check_causal_targets as mod

    committed = mod.BASELINE_PATH.read_text(encoding="utf-8")
    real = len(
        [
            line
            for line in committed.splitlines()
            if line.strip() and not line.startswith("#")
        ]
    )

    ghost = "kb/disorders/Nonexistent.yaml\tpathophysiology.downstream\tGhost\tTarget"
    padded = tmp_path / "baseline.txt"
    padded.write_text(committed + ghost + "\n")
    monkeypatch.setattr(mod, "BASELINE_PATH", padded)
    monkeypatch.setattr(sys, "argv", ["check_causal_targets.py"])

    exit_code = mod.main()
    out = capsys.readouterr().out

    assert exit_code == 0, (
        "a stale row is not a failure — the tree is better, not worse"
    )
    assert "1 baseline row(s) no longer match" in out
    assert "Ghost" in out
    # The reported count must exclude the stale row rather than inflate by it.
    assert f"({real} dangling target(s) grandfathered)" in out


def test_single_file_invocation_reports_no_stale_rows(tmp_path, monkeypatch, capsys):
    """Stale detection is only meaningful over the whole tree.

    `live` covers only the files scanned, so under explicit paths every baseline
    row outside that subset looks fixed. Before this was gated, a single-file run
    reported all 126 rows as stale and then printed "0 grandfathered" — reading
    as an empty backlog, which is the opposite of what the count is for.
    """
    import check_causal_targets as mod

    monkeypatch.setattr(
        sys, "argv", ["check_causal_targets.py", "kb/disorders/Asthma.yaml"]
    )
    exit_code = mod.main()
    out = capsys.readouterr().out

    assert exit_code == 0
    assert "no longer match" not in out, "per-file mode cannot judge staleness"
    real = len(
        [
            line
            for line in mod.BASELINE_PATH.read_text(encoding="utf-8").splitlines()
            if line.strip() and not line.startswith("#")
        ]
    )
    assert f"({real} dangling target(s) grandfathered)" in out


def test_committed_kb_has_no_new_broken_targets():
    """The gate itself, over the real KB."""
    result = subprocess.run(
        [sys.executable, str(SCRIPT)],
        capture_output=True,
        text=True,
        cwd=ROOT,
        check=False,
    )
    assert result.returncode == 0, result.stdout + result.stderr
