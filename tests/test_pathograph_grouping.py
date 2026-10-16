"""The pathograph "Group by" control (#14539).

Grouping is done in the page script, ``templates/_pathograph_grouping.js``, on
a copy of the payload graph.py builds. These tests run that script under node
against small synthetic graphs, as the issue asks, rather than against live KB
entries whose node sets move with every curation PR. The Python side only adds
the keys the script groups on, and is tested directly.

The node tests are skipped when ``node`` is not installed; GitHub's Ubuntu
runners ship it.
"""

from __future__ import annotations

import json
import re
import shutil
import subprocess
from itertools import pairwise
from pathlib import Path

import pytest
import yaml

from dismech import render

REPO_ROOT = Path(__file__).resolve().parents[1]
JS_PATH = REPO_ROOT / "src" / "dismech" / "templates" / "_pathograph_grouping.js"
NODE = shutil.which("node")

needs_node = pytest.mark.skipif(NODE is None, reason="node is not installed")


def run_node(expression: str, payload: object) -> object:
    """Evaluate ``expression`` with the module bound to ``G`` and payload to ``input``."""
    program = (
        f"const G = require({json.dumps(str(JS_PATH))});\n"
        "const input = JSON.parse(require('fs').readFileSync(0, 'utf8'));\n"
        f"process.stdout.write(JSON.stringify(({expression})));\n"
    )
    proc = subprocess.run(
        [NODE, "-e", program],
        input=json.dumps(payload),
        capture_output=True,
        text=True,
        check=False,
        timeout=60,
    )
    assert proc.returncode == 0, proc.stderr
    return json.loads(proc.stdout)


def node(node_id: str, node_type: str = "pathophysiology", **extra) -> dict:
    return {
        "id": node_id,
        "node_type": node_type,
        "color": "#fff",
        "is_orphan": False,
        **extra,
    }


def edge(source: str, target: str, predicate: str = "causes", **extra) -> dict:
    return {
        "source": source,
        "target": target,
        "predicate": predicate,
        "is_orphan": False,
        **extra,
    }


def phenotype(node_id: str, system: str | None) -> dict:
    keys = {"phenotype_system": system} if system else {}
    return node(node_id, "phenotype", group_keys=keys)


def view(data: dict, mode: str, expanded: dict | None = None) -> dict:
    """Return the grouped view, reduced to plain ids for comparison."""
    return run_node(
        "(() => { const v = G.applyGrouping(input.data, input.mode, input.expanded);"
        " return {nodes: v.nodes.map(n => n.id).sort(),"
        " edges: v.edges.map(e => ({source: e.source, target: e.target, predicate: e.predicate,"
        " multiplicity: e.multiplicity || 1, hypothesis_groups: e.hypothesis_groups || []})),"
        " groups: v.groups.map(g => ({id: g.id, label: g.label, members: g.members.map(m => m.id),"
        " node_type: g.node_type, unexplained: g.unexplained, internal_edges: g.internal_edges})),"
        " skipped: v.skipped.map(g => g.id)}; })()",
        {"data": data, "mode": mode, "expanded": expanded or {}},
    )


def phenotype_fixture() -> dict:
    """Two mechanisms feeding five phenotypes in two systems, plus an orphan."""
    return {
        "nodes": [
            node("Mech A"),
            node("Mech B"),
            node("Mech C"),
            phenotype("Seizures", "Nervous System"),
            phenotype("Ataxia", "Nervous System"),
            phenotype("Hypotonia", "Nervous System"),
            phenotype("Cataract", "Eye"),
            phenotype("Unbound feature", None),
            node("phenotypes#Missing", "orphan", is_orphan=True),
            node("Drug", "treatment"),
        ],
        "edges": [
            edge("Mech A", "Mech B"),
            edge("Mech B", "Mech C"),
            edge("Mech B", "Seizures", hypothesis_groups=["h1"]),
            edge("Mech B", "Ataxia", hypothesis_groups=["h1"]),
            edge("Mech C", "Hypotonia"),
            edge("Mech C", "Cataract"),
            edge("Mech C", "Unbound feature"),
            edge("Mech C", "phenotypes#Missing", is_orphan=True),
            # Hypotonia is reached causally; this treats edge does not explain it
            # and is the only edge into Ataxia's sibling below.
            edge("Drug", "Ataxia", "treats"),
        ],
    }


@needs_node
def test_phenotypes_group_by_system_and_singletons_stay_put() -> None:
    v = view(phenotype_fixture(), "phenotype_system")
    assert [(g["label"], sorted(g["members"])) for g in v["groups"]] == [
        ("Nervous System phenotypes", ["Ataxia", "Hypotonia", "Seizures"])
    ]
    # A one-member system and a phenotype with no system are not grouped.
    assert "Cataract" in v["nodes"]
    assert "Unbound feature" in v["nodes"]


@needs_node
def test_orphan_targets_are_never_grouped() -> None:
    data = phenotype_fixture()
    # Even an orphan carrying a grouping key stays its own red node.
    data["nodes"][8]["group_keys"] = {"phenotype_system": "Nervous System"}
    v = view(data, "phenotype_system")
    assert "phenotypes#Missing" in v["nodes"]
    assert all("phenotypes#Missing" not in g["members"] for g in v["groups"])


@needs_node
def test_merged_edges_keep_their_style_and_count_members() -> None:
    v = view(phenotype_fixture(), "phenotype_system")
    group_id = v["groups"][0]["id"]
    into_group = [e for e in v["edges"] if e["target"] == group_id]
    # Mech B's two hypothesis edges merge into one; Mech C's plain causal edge
    # does not merge with them, and the treats edge keeps its own predicate.
    assert sorted(
        (e["source"], e["predicate"], e["multiplicity"], e["hypothesis_groups"])
        for e in into_group
    ) == [
        ("Drug", "treats", 1, []),
        ("Mech B", "causes", 2, ["h1"]),
        ("Mech C", "causes", 1, []),
    ]


@needs_node
def test_group_reports_phenotypes_without_a_causal_inlink() -> None:
    data = phenotype_fixture()
    # Drop the causal edge into Ataxia: only the treats edge is left.
    data["edges"] = [
        e
        for e in data["edges"]
        if not (e["target"] == "Ataxia" and e["predicate"] == "causes")
    ]
    v = view(data, "phenotype_system")
    assert v["groups"][0]["unexplained"] == ["Ataxia"]


@needs_node
def test_expanded_group_is_drawn_as_its_members() -> None:
    data = phenotype_fixture()
    group_id = view(data, "phenotype_system")["groups"][0]["id"]
    v = view(data, "phenotype_system", {group_id: True})
    assert v["groups"] == []
    assert {"Seizures", "Ataxia", "Hypotonia"} <= set(v["nodes"])


@needs_node
def test_treatments_group_by_shared_target_set() -> None:
    data = {
        "nodes": [
            node("Mech"),
            phenotype("Pain", None),
            phenotype("Fever", None),
            node("Ibuprofen", "treatment"),
            node("Naproxen", "treatment"),
            node("Paracetamol", "treatment"),
        ],
        "edges": [
            edge("Mech", "Pain"),
            edge("Mech", "Fever"),
            edge("Ibuprofen", "Pain", "treats"),
            edge("Naproxen", "Pain", "treats"),
            edge("Paracetamol", "Pain", "treats"),
            edge("Paracetamol", "Fever", "treats"),
        ],
    }
    v = view(data, "treatment_target")
    assert [(g["label"], g["members"]) for g in v["groups"]] == [
        ("Treatments → Pain", ["Ibuprofen", "Naproxen"])
    ]
    assert "Paracetamol" in v["nodes"]


@needs_node
def test_mechanisms_group_by_conformed_module() -> None:
    data = {
        "nodes": [
            node("Trigger"),
            node("Stellate activation", group_keys={"modules": ["fibrotic_response"]}),
            node("Matrix deposition", group_keys={"modules": ["fibrotic_response"]}),
            node("Scarring"),
            node("Portal hypertension"),
            phenotype("Ascites", None),
        ],
        "edges": [
            edge("Trigger", "Stellate activation"),
            edge("Stellate activation", "Matrix deposition"),
            edge("Matrix deposition", "Scarring"),
            edge("Scarring", "Portal hypertension"),
            edge("Portal hypertension", "Ascites"),
        ],
    }
    v = view(data, "module")
    assert [(g["label"], g["members"]) for g in v["groups"]] == [
        ("Fibrotic response module", ["Stellate activation", "Matrix deposition"])
    ]
    assert v["groups"][0]["internal_edges"] == 1


@needs_node
def test_linear_runs_collapse_but_branch_points_and_ends_stay() -> None:
    chain = [
        "Variant",
        "Loss of protein",
        "Pathway down",
        "Cell death",
        "Atrophy",
        "Weakness",
    ]
    data = {
        "nodes": [node(n) for n in chain] + [node("Side branch")],
        "edges": [edge(a, b) for a, b in pairwise(chain)]
        + [edge("Atrophy", "Side branch")],
    }
    v = view(data, "chain")
    assert [(g["label"], g["members"]) for g in v["groups"]] == [
        (
            "Loss of protein → … → Cell death (3 steps)",
            ["Loss of protein", "Pathway down", "Cell death"],
        )
    ]
    # Atrophy branches, so it stays; so do both ends of the run.
    assert {"Variant", "Atrophy", "Weakness", "Side branch"} <= set(v["nodes"])


@needs_node
def test_a_bare_chain_keeps_both_ends_and_one_box() -> None:
    chain = ["A", "B", "C", "D"]
    data = {
        "nodes": [node(n) for n in chain],
        "edges": [edge(a, b) for a, b in pairwise(chain)],
    }
    assert view(data, "chain")["nodes"] == sorted(["A", "D", "__group__:chain:B"])


@needs_node
def test_grouping_never_leaves_fewer_than_the_floor() -> None:
    # Folding B, C and D into one module box would leave two nodes on screen.
    data = {
        "nodes": [node("A")]
        + [node(n, group_keys={"modules": ["m"]}) for n in ("B", "C", "D")],
        "edges": [edge("A", "B"), edge("B", "C"), edge("C", "D")],
    }
    v = view(data, "module")
    assert not v["groups"]
    assert v["skipped"] == ["__group__:module:m"]
    assert len(v["nodes"]) == 4


@needs_node
def test_default_mode_is_off_for_small_graphs_and_the_biggest_win_otherwise() -> None:
    data = phenotype_fixture()
    chosen = run_node(
        "[G.chooseDefaultMode(input, input.edges.length), G.chooseDefaultMode(input, 2), G.chooseDefaultMode(input, null)]",
        data,
    )
    # At or below the mean: off. Above it: the only mode with a group here.
    # With no mean known (an empty corpus): off.
    assert chosen == ["none", "phenotype_system", "none"]


@needs_node
def test_default_mode_picks_the_mode_drawing_fewest_edges() -> None:
    data = phenotype_fixture()
    # Add four treatments sharing one target: grouping them saves three edges,
    # while the phenotype grouping saves one (two hypothesis edges merge).
    for name in ("T1", "T2", "T3", "T4"):
        data["nodes"].append(node(name, "treatment"))
        data["edges"].append(edge(name, "Cataract", "treats"))
    edges = run_node(
        "Object.fromEntries(G.MODES.map(m => [m.key, G.applyGrouping(input, m.key, {}).edges.length]))",
        data,
    )
    expected = min((k for k in edges if k != "none"), key=lambda k: edges[k])
    assert run_node("G.chooseDefaultMode(input, 1)", data) == expected
    assert expected == "treatment_target"


def test_grouping_script_has_no_jinja_syntax() -> None:
    # The page inlines this file with a Jinja include, so these sequences
    # would be parsed as template syntax rather than shipped as JavaScript.
    text = JS_PATH.read_text()
    for token in ("{{", "{%", "{#"):
        assert token not in text, token


def test_grouping_context_adds_keys_without_changing_the_graph(monkeypatch) -> None:
    monkeypatch.setattr(
        render,
        "_load_hpo_category_cache",
        lambda: {"HP:0001250": ["Nervous System", "Growth"]},
    )
    payload = json.dumps(
        {
            "nodes": [
                {
                    "id": "Seizures",
                    "node_type": "phenotype",
                    "meta": {"term_id": "HP:0001250"},
                },
                {
                    "id": "Odd feature",
                    "node_type": "phenotype",
                    "meta": {"term_id": "HP:9999999"},
                },
                {"id": "Activation", "node_type": "pathophysiology"},
            ],
            "edges": [
                {"source": "Activation", "target": "Seizures", "predicate": "causes"}
            ],
            "orphan_targets": [],
        }
    )
    disorder = {
        "pathophysiology": [
            {
                "name": "Activation",
                "conforms_to": "fibrotic_response#Mesenchymal Cell Activation",
            }
        ]
    }
    data = json.loads(render._add_pathograph_grouping_context(payload, disorder, 22))
    keys = {n["id"]: n.get("group_keys") for n in data["nodes"]}
    # The first listed category is the one the phenotype cards file under.
    assert keys == {
        "Seizures": {"phenotype_system": "Nervous System"},
        "Odd feature": None,
        "Activation": {"modules": ["fibrotic_response"]},
    }
    assert data["grouping"] == {"mean_edge_count": 22}
    assert data["edges"] == json.loads(payload)["edges"]
    assert render._add_pathograph_grouping_context("", disorder, 22) == ""


def _write_disorder(path: Path, name: str, chain_length: int) -> None:
    names = [f"{name} step {i}" for i in range(chain_length)]
    path.write_text(
        yaml.safe_dump(
            {
                "name": name,
                "pathophysiology": [
                    {"name": a, "downstream": [{"target": b}]}
                    for a, b in pairwise(names)
                ]
                + [{"name": names[-1]}],
            }
        )
    )


def test_mean_edge_count_covers_only_entries_with_a_pathograph(tmp_path: Path) -> None:
    _write_disorder(tmp_path / "One.yaml", "One", 3)  # 2 edges
    _write_disorder(tmp_path / "Two.yaml", "Two", 6)  # 5 edges
    (tmp_path / "Empty.yaml").write_text(yaml.safe_dump({"name": "Empty"}))
    render._pathograph_mean_edge_count.cache_clear()
    assert render._pathograph_mean_edge_count(tmp_path) == round(3.5)


def test_rendered_page_carries_the_group_by_control(tmp_path: Path) -> None:
    _write_disorder(tmp_path / "Small.yaml", "Small", 3)
    _write_disorder(tmp_path / "Large.yaml", "Large", 9)
    render._pathograph_mean_edge_count.cache_clear()
    out = tmp_path / "Large.html"
    render.render_disorder(tmp_path / "Large.yaml", out)
    page = out.read_text()
    assert 'id="pathograph-groupbar"' in page
    assert "var PathographGrouping" in page
    match = re.search(r"var graphData = JSON\.parse\((\".*?\")\);\n", page)
    assert match
    data = json.loads(json.loads(match.group(1)))
    assert data["grouping"] == {"mean_edge_count": round((2 + 8) / 2)}
