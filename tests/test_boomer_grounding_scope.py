"""An explicit scope qualifier must govern the primary grounding hypothesis."""

import importlib.util
import json
from pathlib import Path

import pytest

SCRIPT = (
    Path(__file__).resolve().parents[1] / "analyses/boomer/scripts/omimps_pilots.py"
)
spec = importlib.util.spec_from_file_location("scope_pilot", SCRIPT)
pilot = importlib.util.module_from_spec(spec)
spec.loader.exec_module(pilot)


@pytest.mark.parametrize(
    "predicate,kind,reverse",
    [
        ("skos:broadMatch", "SubClassOf", False),
        ("skos:narrowMatch", "SubClassOf", True),
        ("skos:relatedMatch", None, False),
        ("skos:closeMatch", None, False),
    ],
)
def test_primary_grounding_honors_its_explicit_predicate(predicate, kind, reverse):
    data = json.loads((pilot.OUT / "bbs/projection.json").read_text())
    record = data["snapshots"]["after"]["records"][data["root"]]["data"]
    term = pilot.term_id(record["disease_term"])
    record["mappings"]["mondo_mappings"] = [
        {"term": {"id": term}, "mapping_predicate": predicate}
    ]
    kb, audit = pilot.compile_snapshot(data, "after")
    subject = "dismech:Bardet-Biedl_Syndrome"
    direct = [
        p["fact"]
        for p in kb["pfacts"]
        if {p["fact"].get("sub"), p["fact"].get("equivalent", p["fact"].get("sup"))}
        == {subject, term}
    ]
    if kind:
        assert direct == [
            {
                "fact_type": kind,
                "sub": term if reverse else subject,
                "sup": subject if reverse else term,
            }
        ]
    else:
        assert direct == []
    assert any(
        a["subject"] == subject and a["target"] == term and a["predicate"] == predicate
        for a in audit["mapping_assertions"]
    )


def test_conflicting_primary_qualifiers_are_not_silently_chosen():
    data = json.loads((pilot.OUT / "bbs/projection.json").read_text())
    record = data["snapshots"]["after"]["records"][data["root"]]["data"]
    term = pilot.term_id(record["disease_term"])
    record["mappings"]["mondo_mappings"] = [
        {"term": {"id": term}, "mapping_predicate": p}
        for p in ("skos:exactMatch", "skos:broadMatch")
    ]
    with pytest.raises(ValueError, match="Conflicting grounding predicates"):
        pilot.compile_snapshot(data, "after")


@pytest.mark.parametrize("conflict", [False, True])
def test_subtype_qualifier_follows_curated_in_alias(conflict):
    data = json.loads((pilot.OUT / "pnh/projection.json").read_text())
    records = data["snapshots"]["after"]["records"]
    subtype = records[data["root"]]["data"]["has_subtypes"][1]
    term = pilot.term_id(subtype["subtype_term"])
    subtype["mappings"] = {
        "mondo_mappings": [
            {"term": {"id": term}, "mapping_predicate": "skos:broadMatch"}
        ]
    }
    child = "Paroxysmal_Nocturnal_Hemoglobinuria_2"
    if conflict:
        records[f"kb/disorders/{child}.yaml"]["data"]["mappings"] = {
            "mondo_mappings": [
                {"term": {"id": term}, "mapping_predicate": "skos:exactMatch"}
            ]
        }
        with pytest.raises(ValueError, match="Conflicting alias grounding predicates"):
            pilot.compile_snapshot(data, "after")
    else:
        kb, audit = pilot.compile_snapshot(data, "after")
        subject = "dismech:" + child
        assert {"fact_type": "SubClassOf", "sub": subject, "sup": term} in [
            p["fact"] for p in kb["pfacts"]
        ]
        assert not any(
            p["fact"].get("sub") == subject and p["fact"].get("equivalent") == term
            for p in kb["pfacts"]
        )
        assert (
            audit["aliases"][
                "dismech:Paroxysmal_Nocturnal_Hemoglobinuria#PIGT-associated PNH2"
            ]
            == subject
        )
