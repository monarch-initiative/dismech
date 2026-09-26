"""Tests for the inverted (ancestor-walk) grouping MONDO consistency check.

The check exists because the descendant direction is the expensive one and is
unavailable through the configured ``ols:mondo`` adapter. These tests pin the
*verdict logic* — which predicates assert subsumption, and what counts as a
contradiction — and stub the ancestor lookup so nothing here touches the
network.
"""

from pathlib import Path

import yaml

from scripts import grouping_mondo_consistency as gmc


def _write_yaml(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(yaml.safe_dump(data, sort_keys=False))


def _grouping(name: str, mondo: str, predicate: str, members: list[str]) -> dict:
    return {
        "name": name,
        "mappings": {
            "mondo_mappings": [
                {"term": {"id": mondo, "label": "mapped class"},
                 "mapping_predicate": predicate}
            ]
        },
        "members": [{"member": m, "member_type": "DISEASE"} for m in members],
    }


def _setup(tmp_path, monkeypatch, groupings: list[dict], diseases: dict[str, str],
           ancestry: dict[str, list[str]]):
    gdir = tmp_path / "groupings"
    ddir = tmp_path / "disorders"
    for g in groupings:
        _write_yaml(gdir / f"{g['name'].replace(' ', '_')}.yaml", g)
    for dname, mondo in diseases.items():
        _write_yaml(
            ddir / f"{dname.replace(' ', '_')}.yaml",
            {"name": dname, "disease_term": {"term": {"id": mondo, "label": dname}}},
        )
    monkeypatch.setattr(gmc, "GROUPINGS_DIR", str(gdir))
    monkeypatch.setattr(gmc, "DISORDERS_DIR", str(ddir))
    monkeypatch.setattr(
        gmc, "ancestors", lambda curie, cache, *, pause=0: ancestry.get(curie)
    )


def test_member_inside_the_mapped_class_is_a_descendant(tmp_path, monkeypatch):
    _setup(
        tmp_path, monkeypatch,
        [_grouping("Inside", "MONDO:0000100", "skos:exactMatch", ["Alpha"])],
        {"Alpha": "MONDO:0000111"},
        {"MONDO:0000111": ["MONDO:0000100", "MONDO:0000001"]},
    )
    (v,) = gmc.build_verdicts()
    assert [m.verdict for m in v.members] == ["descendant"]
    assert not v.contradicted


def test_exact_match_holding_an_outside_member_is_contradicted(tmp_path, monkeypatch):
    """The umbrella case: exactMatch claims coextension the members deny."""
    _setup(
        tmp_path, monkeypatch,
        [_grouping("Umbrella", "MONDO:0000100", "skos:exactMatch", ["Alpha", "Beta"])],
        {"Alpha": "MONDO:0000111", "Beta": "MONDO:0000222"},
        {
            "MONDO:0000111": ["MONDO:0000100"],
            "MONDO:0000222": ["MONDO:0000999"],  # a sibling branch
        },
    )
    (v,) = gmc.build_verdicts()
    assert v.contradicted
    assert [m.disease for m in v.outside] == ["Beta"]
    assert len(v.descendants) == 1


def test_narrow_match_also_asserts_subsumption(tmp_path, monkeypatch):
    """narrowMatch says the dismech concept sits INSIDE the class, so an
    outside member contradicts it exactly as an exactMatch does."""
    _setup(
        tmp_path, monkeypatch,
        [_grouping("Narrow", "MONDO:0000100", "skos:narrowMatch", ["Beta"])],
        {"Beta": "MONDO:0000222"},
        {"MONDO:0000222": ["MONDO:0000999"]},
    )
    (v,) = gmc.build_verdicts()
    assert v.asserts_subsumption
    assert v.contradicted


def test_broad_match_asserts_nothing_so_an_outside_member_is_not_a_finding(
    tmp_path, monkeypatch
):
    """broadMatch says the dismech concept CONTAINS the class. Members outside
    it are expected, not defects — this is the predicate the umbrella would
    move to, and it must not then report its own members as findings."""
    _setup(
        tmp_path, monkeypatch,
        [_grouping("Broad", "MONDO:0000100", "skos:broadMatch", ["Beta"])],
        {"Beta": "MONDO:0000222"},
        {"MONDO:0000222": ["MONDO:0000999"]},
    )
    (v,) = gmc.build_verdicts()
    assert not v.asserts_subsumption
    assert v.outside and not v.contradicted


def test_failed_lookup_is_not_reported_as_outside(tmp_path, monkeypatch):
    """A network failure must never masquerade as evidence that a member sits
    outside the class — that would turn an outage into a curation finding."""
    _setup(
        tmp_path, monkeypatch,
        [_grouping("Flaky", "MONDO:0000100", "skos:exactMatch", ["Alpha"])],
        {"Alpha": "MONDO:0000111"},
        {},  # lookup returns None
    )
    (v,) = gmc.build_verdicts()
    assert [m.verdict for m in v.members] == ["lookup_failed"]
    assert not v.outside
    assert not v.contradicted


def test_member_without_a_mondo_term_is_unresolved_not_outside(tmp_path, monkeypatch):
    _setup(
        tmp_path, monkeypatch,
        [_grouping("Unbound", "MONDO:0000100", "skos:exactMatch", ["Gamma"])],
        {},  # Gamma has no disorder file, so no disease_term
        {},
    )
    (v,) = gmc.build_verdicts()
    assert [m.verdict for m in v.members] == ["no_mondo_term"]
    assert not v.contradicted


def test_nested_grouping_members_are_expanded_and_attributed(tmp_path, monkeypatch):
    """A disease held through a nested grouping is a member of the parent, and
    the report says which child it came through."""
    parent = {
        "name": "Parent",
        "mappings": {"mondo_mappings": [
            {"term": {"id": "MONDO:0000100", "label": "mapped"},
             "mapping_predicate": "skos:exactMatch"}
        ]},
        "members": [{"member": "Child", "member_type": "GROUPING"}],
    }
    child = _grouping("Child", "MONDO:0000100", "skos:narrowMatch", ["Alpha"])
    _setup(
        tmp_path, monkeypatch, [parent, child],
        {"Alpha": "MONDO:0000111"},
        {"MONDO:0000111": ["MONDO:0000100"]},
    )
    verdicts = {v.grouping: v for v in gmc.build_verdicts()}
    pv = verdicts["Parent"]
    assert [(m.disease, m.via) for m in pv.members] == [("Alpha", "Child")]
    assert not pv.contradicted


def test_strict_exits_nonzero_only_on_a_contradicted_predicate(tmp_path, monkeypatch):
    _setup(
        tmp_path, monkeypatch,
        [_grouping("Umbrella", "MONDO:0000100", "skos:exactMatch", ["Beta"])],
        {"Beta": "MONDO:0000222"},
        {"MONDO:0000222": ["MONDO:0000999"]},
    )
    assert gmc.main([]) == 0
    assert gmc.main(["--strict"]) == 1
