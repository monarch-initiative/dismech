"""A `conforms_to` anchor that resolves says nothing about the node's content.

`groupings.module_node_names` checks the anchor points at a real module node,
and that is the whole of what is enforced today. CLAUDE.md states a stronger
contract -- "if a node declares conforms_to, it should include the expected
biological processes and causal edges from the module" -- which nothing checks,
so a node can claim an anchor it shares nothing with and pass every gate.

These tests pin the classification rather than any corpus number, because the
four classes have different causes and must not collapse into each other. In
particular `process_absent` must stay separate from `anchor_no_process`: the
first is a possible mismatch, the second is a module node with no GO term to
compare against, and merging them would report the latter as agreement.
"""

import subprocess
import sys
from pathlib import Path

# Inline the path rather than assigning ROOT first: ruff's E402 allows an
# import preceded by a `sys.path` preamble, but an intervening assignment
# breaks that allowance (#9964).
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from check_conformance_content import CLASSES, assess

ROOT = Path(__file__).parent.parent
SCRIPT = ROOT / "scripts" / "check_conformance_content.py"


def _module_node(processes=(), cell_types=(), edges=0):
    return {
        "processes": set(processes),
        "process_labels": [f"{t} label" for t in processes],
        "cell_types": set(cell_types),
        "edges": edges,
    }


def _node(name="N", processes=(), cell_types=(), downstream=0):
    out = {"name": name}
    if processes:
        out["biological_processes"] = [
            {"term": {"id": t, "label": "l"}} for t in processes
        ]
    if cell_types:
        out["cell_types"] = [{"term": {"id": t, "label": "l"}} for t in cell_types]
    if downstream:
        out["downstream"] = [{"target": f"T{i}"} for i in range(downstream)]
    return out


INDEX = {
    "m#Anchor": _module_node(processes=("GO:1",), cell_types=("CL:1",), edges=2),
    "m#Bare": _module_node(),
}


def _kinds(node, anchor="m#Anchor"):
    return {f.kind for f in assess("f.yaml", node, anchor, INDEX)}


def test_sharing_the_module_term_and_substituting_a_cell_type_is_clean():
    node = _node(processes=("GO:1",), cell_types=("CL:99",), downstream=1)
    assert _kinds(node) == set()


def test_a_node_sharing_no_process_term_is_reported():
    node = _node(processes=("GO:2",), cell_types=("CL:99",), downstream=1)
    assert _kinds(node) == {"process_absent"}


def test_a_module_node_with_no_go_term_is_its_own_class_not_agreement():
    """The distinction this check exists to keep: nothing to compare is not a match."""
    node = _node(processes=("GO:2",))
    assert _kinds(node, anchor="m#Bare") == {"anchor_no_process"}


def test_a_conformer_binding_no_cell_type_is_reported_even_when_the_process_matches():
    """Organ-specific cell-type substitution is the point of conformance."""
    node = _node(processes=("GO:1",), downstream=1)
    assert _kinds(node) == {"cell_type_absent"}


def test_a_conformer_with_no_downstream_edge_is_reported_separately():
    node = _node(processes=("GO:1",), cell_types=("CL:99",))
    assert _kinds(node) == {"edges_absent"}


def test_the_orthogonal_classes_can_co_occur_with_a_process_finding():
    node = _node(processes=("GO:2",))
    assert _kinds(node) == {"process_absent", "cell_type_absent", "edges_absent"}


def test_an_unresolvable_anchor_is_named_rather_than_scored_as_agreement():
    kinds = _kinds(_node(processes=("GO:1",)), anchor="m#Missing")
    assert kinds == {"unresolvable"}


def test_a_node_with_no_conforms_to_is_not_assessed():
    """iter_links only yields declared links, so a bare node contributes nothing."""
    from check_conformance_content import iter_links

    assert list(iter_links([])) == []


def test_every_class_name_is_covered_by_the_summary_constant():
    """CLASSES drives both --kind and the summary; a new class must be added there."""
    assert set(CLASSES) == {
        "process_absent",
        "anchor_no_process",
        "cell_type_absent",
        "edges_absent",
    }


def test_the_script_is_report_only_over_the_whole_kb():
    """Exit 0 with findings present: this is a worklist, not a gate (see the docstring)."""
    proc = subprocess.run(
        [
            sys.executable,
            str(SCRIPT),
            str(ROOT / "kb" / "disorders" / "MERRF_Syndrome.yaml"),
        ],
        capture_output=True,
        text=True,
        check=False,
    )
    assert proc.returncode == 0, proc.stderr
    assert "conformance link(s)" in proc.stdout


def test_strict_gates_when_asked():
    proc = subprocess.run(
        [
            sys.executable,
            str(SCRIPT),
            str(ROOT / "kb" / "disorders" / "MERRF_Syndrome.yaml"),
            "--strict",
            "--kind",
            "process_absent",
        ],
        capture_output=True,
        text=True,
        check=False,
    )
    assert proc.returncode == 1, proc.stdout
