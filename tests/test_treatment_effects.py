"""Negative treatment effects: graph, export, and the check (#10151, #10048)."""

from __future__ import annotations

import json
from pathlib import Path

import pytest
from linkml_runtime.utils.schemaview import SchemaView

from dismech.export.cx2_export import EDGE_STYLE_BY_PREDICATE, disorder_to_cx2
from dismech.graph import (
    ENVIRONMENTAL_PREDICATES,
    MODEL_RELATIONSHIP_PREDICATES,
    NEGATIVE_TREATMENT_EFFECT_PREDICATES,
    build_causal_graph,
    generate_mermaid,
    graph_to_json,
    treatment_edge_predicate,
)
from dismech.node_role_audit import _link_index
from dismech.qc_plugins import CAUSAL_PREDICATES, GENE_WIRING_PREDICATES
from scripts import check_treatment_effects as check

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = {"reference": "PMID:1", "supports": "SUPPORT", "snippet": "It did not help."}


def _link(effect=None, target="Cartilage Loss", **extra):
    link = {"target": target, **extra}
    if effect:
        link["treatment_effect"] = effect
    return link


def _entry(*links, target_phenotypes=None):
    treatment = {"name": "Drug", "target_mechanisms": list(links)}
    if target_phenotypes:
        treatment["target_phenotypes"] = target_phenotypes
    return {
        "name": "Disease",
        "pathophysiology": [{"name": "Cartilage Loss"}],
        "phenotypes": [
            {
                "name": "Seizure",
                "phenotype_term": {
                    "preferred_term": "Seizure",
                    "term": {"id": "HP:0001250", "label": "Seizure"},
                },
            }
        ],
        "treatments": [treatment],
    }


def _edges(entry):
    return {
        (e.target, e.predicate)
        for e in build_causal_graph(entry).edges
        if e.source == "Drug"
    }


def test_every_effect_has_a_decided_predicate():
    values = (
        SchemaView(str(ROOT / "src/dismech/schema/dismech.yaml"))
        .get_enum("TreatmentEffectEnum")
        .permissible_values
    )
    assert {v: treatment_edge_predicate(v) for v in values} == {
        "INHIBITS": "targets",
        "ACTIVATES": "targets",
        "MODULATES": "targets",
        "BYPASSES": "targets",
        "RESTORES": "targets",
        "NO_EFFECT": "no_effect_on",
        "EXACERBATES": "worsens",
    }
    assert treatment_edge_predicate(None) == "targets"


def test_negative_predicates_collide_with_nothing():
    negative = set(NEGATIVE_TREATMENT_EFFECT_PREDICATES.values())
    taken = (
        CAUSAL_PREDICATES
        | GENE_WIRING_PREDICATES
        | ENVIRONMENTAL_PREDICATES
        | set(MODEL_RELATIONSHIP_PREDICATES.values())
    )
    assert not negative & taken


@pytest.mark.parametrize(
    ("effect", "predicate"), [("NO_EFFECT", "no_effect_on"), ("EXACERBATES", "worsens")]
)
def test_negative_effect_reaches_every_surface(effect, predicate):
    entry = _entry(_link(effect, description="Did not help.", evidence=[EVIDENCE]))
    graph = build_causal_graph(entry)
    assert _edges(entry) == {("Cartilage Loss", predicate)}

    payload = json.loads(graph_to_json(graph, entry))
    (edge,) = [e for e in payload["edges"] if e["source"] == "Drug"]
    assert edge["predicate"] == predicate
    assert edge["description"] == "Did not help."

    assert f"-.->|{predicate.replace('_', ' ')}|" in generate_mermaid(graph)


def test_cx2_keeps_the_evidence_on_a_negative_edge():
    """The exporter keys edge detail on the predicate, so the two must agree."""
    entry = _entry(_link("NO_EFFECT", description="Did not help.", evidence=[EVIDENCE]))
    document = disorder_to_cx2(entry)
    edges = next(a["edges"] for a in document if "edges" in a)
    (edge,) = [e["v"] for e in edges if e["v"]["predicate"] == "no_effect_on"]
    assert edge["description"] == "Did not help."
    assert "PMID:1" in edge["Evidence"]
    assert edge["treatment_effect"] == "NO_EFFECT"
    assert edge["target_arrow_shape"] == "tee"


@pytest.mark.parametrize("template", ["disorder.html.j2", "module.html.j2"])
def test_page_styles_match_cx2(template):
    text = (ROOT / "src/dismech/templates" / template).read_text()
    for predicate in NEGATIVE_TREATMENT_EFFECT_PREDICATES.values():
        color = EDGE_STYLE_BY_PREDICATE[predicate].color
        (line,) = [x for x in text.splitlines() if x.strip().startswith(f"{predicate}:")]
        assert color in line
        marker = line.split('marker: "')[1].split('"')[0]
        assert f'.attr("id", "{marker}")' in text


def test_treats_edge_is_not_drawn_where_the_entry_denies_it():
    phenotypes = [
        {
            "preferred_term": "Seizure",
            "term": {"id": "HP:0001250", "label": "Seizure"},
        }
    ]
    denied = _entry(_link("NO_EFFECT", "Seizure"), target_phenotypes=phenotypes)
    assert _edges(denied) == {("Seizure", "no_effect_on")}

    elsewhere = _entry(_link("NO_EFFECT"), target_phenotypes=phenotypes)
    assert ("Seizure", "treats") in _edges(elsewhere)

    mixed = _entry(
        _link("NO_EFFECT", "Seizure"),
        _link("INHIBITS", "Seizure"),
        target_phenotypes=phenotypes,
    )
    assert ("Seizure", "treats") in _edges(mixed)


def test_a_failed_treatment_is_not_an_intervention_point():
    assert _link_index(_entry(_link("NO_EFFECT")))["targeted"] == set()
    assert _link_index(_entry(_link("INHIBITS")))["targeted"] == {"Cartilage Loss"}


def _kinds(entry):
    names = {n["name"] for n in entry["pathophysiology"]}
    return [
        f.kind
        for t in entry["treatments"]
        for f in check.check_treatment(Path("x.yaml"), t, names)
    ]


@pytest.mark.parametrize("effect", sorted(check.NEGATIVE_EFFECTS))
def test_negative_effect_requires_link_evidence(effect):
    assert _kinds(_entry(_link(effect))) == ["NEGATIVE_WITHOUT_EVIDENCE"]
    assert _kinds(_entry(_link(effect, evidence=[EVIDENCE]))) == []
    refute = [{**EVIDENCE, "supports": "REFUTE"}]
    assert _kinds(_entry(_link(effect, evidence=refute))) == ["NEGATIVE_ALL_REFUTE"]


def test_all_refute_evidence_under_a_therapeutic_effect_is_reported():
    refute = {**EVIDENCE, "supports": "REFUTE"}
    assert _kinds(_entry(_link("INHIBITS", evidence=[refute]))) == ["REFUTED_EFFECT"]
    assert _kinds(_entry(_link("INHIBITS", evidence=[refute, EVIDENCE]))) == []


@pytest.mark.parametrize(
    ("effect", "target", "text", "found"),
    [
        ("MODULATES", "Cartilage Loss", "Does not modify the underlying loss.", True),
        (None, "Cartilage Loss", "Counselling; it doesn't alter cartilage.", True),
        ("RESTORES", "Cartilage Loss", "Does not restore the matrix.", True),
        ("INHIBITS", "Cartilage Loss", "Slows loss; does not restore matrix.", False),
        ("BYPASSES", "Cartilage Loss", "Does not act on the lesion.", False),
        ("NO_EFFECT", "Cartilage Loss", "It was ineffective.", False),
        ("INHIBITS", "Seizure", "Does not act on the migration defect.", False),
        ("INHIBITS", "Seizure", "It was ineffective.", True),
        ("INHIBITS", "Cartilage Loss", "For refractory disease.", False),
    ],
)
def test_denied_effect(effect, target, text, found):
    link = _link(effect, target, description=text, evidence=[EVIDENCE])
    assert ("DENIED_EFFECT" in _kinds(_entry(link))) is found


def test_untyped_genetic_counseling_with_targets_is_reported():
    entry = _entry(_link())
    entry["treatments"][0]["treatment_term"] = {
        "preferred_term": "genetic counseling",
        "term": {"id": "NCIT:C15240", "label": "Genetic Counseling"},
    }
    assert "NON_THERAPEUTIC_TARGET" in _kinds(entry)
    entry["treatments"][0].pop("target_mechanisms")
    assert _kinds(entry) == []


def test_main_gates_on_a_planted_negative_link(tmp_path, capsys):
    path = tmp_path / "Planted.yaml"
    path.write_text(
        "name: X\npathophysiology:\n- name: N\ntreatments:\n- name: T\n"
        "  target_mechanisms:\n  - target: N\n    treatment_effect: NO_EFFECT\n"
    )
    assert check.main([str(path)]) == 1
    assert "NEGATIVE_WITHOUT_EVIDENCE" in capsys.readouterr().out
    assert check.main([str(tmp_path / "missing.yaml")]) == 2


@pytest.mark.kb_data
def test_kb_is_clean():
    findings, effects = check.scan([])
    assert not [f for f in findings if f.kind in check.GATING]
    assert effects["NO_EFFECT"] and effects["EXACERBATES"]
