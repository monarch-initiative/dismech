"""MONDO annotations permit specific proxy pairs without weakening other constraints."""

from copy import deepcopy
import csv
import importlib
from itertools import product
import json
import os
from pathlib import Path
import sys

import pytest
import yaml

SCRIPTS = Path(__file__).resolve().parents[1] / "analyses/boomer/scripts"
sys.path.insert(0, str(SCRIPTS))
from apply_proxy_merges import migrate  # noqa: E402
from build_analyses import INDEX_FIELDNAMES  # noqa: E402
from enrich_icd10_inputs import tsv  # noqa: E402
from proxy_merges import ProxyPolicy, extract  # noqa: E402


def policy():
    return ProxyPolicy(
        {
            "source_url": "https://example.org/pinned.obo",
            "source_sha256": "test",
            "terms": {
                "MONDO:1": {
                    "mappings": {
                        target: {
                            "qualifiers": {
                                "source": ["MONDO:equivalentTo"]
                                + (
                                    ["MONDO:preferredExternal"]
                                    if target == "ORDO:2"
                                    else []
                                )
                            }
                        }
                        for target in ("ORDO:1", "ORDO:2")
                    }
                },
            },
        }
    )


def input_kb():
    return {
        "name": "Example",
        "facts": [
            {"fact_type": "MemberOfDisjointGroup", "group": "ORDO", "sub": f"ORDO:{i}"}
            for i in (1, 2, 3)
        ]
        + [
            {"fact_type": "ProperSubClassOf", "sub": "ORDO:1", "sup": "ORDO:2"},
            {"fact_type": "ProperSubClassOf", "sub": "ORDO:2", "sup": "ORDO:3"},
            {
                "fact_type": "ProperSubClassOf",
                "sub": "dismech:child",
                "sup": "dismech:parent",
            },
            {
                "fact_type": "ProperSubClassOf",
                "sub": "MONDO:child",
                "sup": "MONDO:parent",
            },
        ],
        "pfacts": [
            {
                "fact": {
                    "fact_type": "EquivalentTo",
                    "sub": "MONDO:1",
                    "equivalent": f"ORDO:{i}",
                },
                "prob": 0.95,
            }
            for i in (1, 2)
        ],
        "labels": {"ORDO:1": "Existing label"},
    }


def test_extract_preserves_qualifiers_and_normalizes_targets(tmp_path):
    path = tmp_path / "mondo.obo"
    path.write_text("""format-version: 1.2

[Term]
id: MONDO:1
xref: Orphanet:1 {source="DOID:1", source="MONDO:equivalentTo", source="OMIM:1"}
xref: Orphanet:2 {source="MONDO:equivalentTo", source="MONDO:preferredExternal"}
xref: Orphanet:3

[Term]
id: MONDO:2
is_obsolete: true
""")
    catalog = extract(
        path, {"MONDO:1", "MONDO:2", "MONDO:3"}, "https://example.org/pinned.obo"
    )
    mapping = catalog["terms"]["MONDO:1"]["mappings"]["ORDO:1"]
    assert mapping["raw_targets"] == ["Orphanet:1"]
    assert mapping["qualifiers"]["source"] == ["DOID:1", "MONDO:equivalentTo", "OMIM:1"]
    assert catalog["terms"]["MONDO:2"]["obsolete"]
    assert catalog["missing_terms"] == ["MONDO:3"]
    p = ProxyPolicy(catalog)
    assert p.decisions(input_kb())[0]["decision"] == "PERMIT_PROXY_MERGE"
    kb = input_kb()
    kb["pfacts"][1]["fact"]["equivalent"] = "ORDO:3"
    assert p.decisions(kb)[0]["decision"] == "REVIEW_UNCONFIRMED_MAPPING"


@pytest.mark.parametrize(
    "change,expected",
    [
        ("missing", "REVIEW_UNCONFIRMED_MAPPING"),
        ("obsolete", "REVIEW_OBSOLETE_MONDO"),
        ("unconfirmed", "REVIEW_UNCONFIRMED_MAPPING"),
        ("no_preference", "REVIEW_PREFERENCE_COUNT"),
        ("two_preferences", "REVIEW_PREFERENCE_COUNT"),
        ("absent_preferred", "REVIEW_PREFERRED_TARGET_ABSENT"),
    ],
)
def test_incomplete_evidence_keeps_namespace_constraints(change, expected):
    p, kb = policy(), input_kb()
    term = p.catalog["terms"]["MONDO:1"]
    mappings = term["mappings"]
    if change == "missing":
        p.catalog["terms"] = {}
    elif change == "obsolete":
        term["obsolete"] = True
    elif change == "unconfirmed":
        mappings["ORDO:1"]["qualifiers"]["source"] = []
    elif change == "no_preference":
        mappings["ORDO:2"]["qualifiers"]["source"] = ["MONDO:equivalentTo"]
    elif change == "two_preferences":
        mappings["ORDO:1"]["qualifiers"]["source"].append("MONDO:preferredExternal")
    else:
        mappings["ORDO:3"] = deepcopy(mappings["ORDO:2"])
        mappings["ORDO:2"]["qualifiers"]["source"] = ["MONDO:equivalentTo"]
    before = deepcopy(kb)
    assert p.apply(kb)[0]["decision"] == expected
    assert [
        f for f in kb["facts"] if f["fact_type"] == "MemberOfDisjointGroup"
    ] == before["facts"][:3]
    assert kb["pfacts"] == before["pfacts"]


def test_priors_labels_explicit_axioms_and_idempotence():
    p, kb = policy(), input_kb()
    explicit = {"fact_type": "DisjointWith", "sub": "ORDO:1", "sibling": "ORDO:2"}
    kb["facts"].append(explicit)
    before = deepcopy(kb)
    p.apply(kb)
    assert kb["pfacts"] == before["pfacts"]
    assert kb["labels"] == before["labels"]
    assert explicit in kb["facts"]
    assert kb["facts"][:4] == [
        {**f, "fact_type": "SubClassOf"} if f["sub"].startswith("ORDO:") else f
        for f in before["facts"][3:7]
    ]
    once = deepcopy(kb)
    p.apply(kb)
    assert kb == once


@pytest.fixture
def engine(monkeypatch):
    source = os.environ.get("BOOMER_SRC")
    if not source:
        pytest.skip("Set BOOMER_SRC for actual reasoner checks")
    monkeypatch.syspath_prepend(str(Path(source).resolve()))
    model = importlib.import_module("boomer.model")
    search = importlib.import_module("boomer.search")
    return model, search.get_reasoner(model.SearchConfig().reasoner_class)


def test_proxy_pair_can_merge_but_third_target_stays_distinct(engine):
    model, reasoner = engine
    kb = input_kb()
    assert not reasoner.reason(
        model.KB.model_validate(kb), [(0, True), (1, True)]
    ).satisfiable
    policy().apply(kb)
    merged = model.KB.model_validate(kb)
    assert reasoner.reason(merged, [(0, True), (1, True)]).satisfiable
    for entity in ("ORDO:1", "ORDO:2"):
        conflict = merged.model_copy(deep=True)
        conflict.facts.append(model.EquivalentTo(sub=entity, equivalent="ORDO:3"))
        assert not reasoner.reason(conflict, [(0, True), (1, True)]).satisfiable
    # Retained non-equivalence must still entail strictness for directional hypotheses.
    merged.pfacts.append(
        model.PFact(fact=model.ProperSubClassOf(sub="ORDO:2", sup="ORDO:3"), prob=0.8)
    )
    assert not reasoner.reason(merged, [(0, True), (1, True), (2, False)]).satisfiable
    merged.facts.append(model.DisjointWith(sub="ORDO:1", sibling="ORDO:2"))
    assert not reasoner.reason(merged, [(0, True), (1, True)]).satisfiable


def test_permissions_are_not_transitively_closed(engine):
    model, reasoner = engine
    p, kb = policy(), input_kb()
    kb["facts"] = kb["facts"][:3]
    p.catalog["terms"]["MONDO:2"] = {
        "mappings": {
            target: {
                "qualifiers": {
                    "source": ["MONDO:equivalentTo"]
                    + (["MONDO:preferredExternal"] if target == "ORDO:2" else [])
                }
            }
            for target in ("ORDO:2", "ORDO:3")
        }
    }
    kb["pfacts"].extend(
        {
            "fact": {
                "fact_type": "EquivalentTo",
                "sub": "MONDO:2",
                "equivalent": target,
            },
            "prob": 0.95,
        }
        for target in ("ORDO:2", "ORDO:3")
    )
    p.apply(kb)
    kb = model.KB.model_validate(kb)
    for values in product((False, True), repeat=4):
        # All four identities would transitively merge the unpermitted 1/3 pair.
        assert reasoner.reason(kb, list(enumerate(values))).satisfiable == (
            not all(values)
        )


def test_migration_preflight_preservation_scope_and_resume(tmp_path):
    base, diseases = tmp_path / "boomer", tmp_path / "diseases"
    diseases.mkdir()
    rows = []
    for slug, category in (("Example", "Mendelian"), ("Legacy", "Cancer")):
        folder = base / "disorders" / slug
        folder.mkdir(parents=True)
        (folder / "kb.yaml").write_text(yaml.safe_dump(input_kb(), sort_keys=False))
        (folder / "README.md").write_text(
            "# Example\n\n## What boomer did\n\nHistorical\n"
        )
        (folder / "solution.yaml").write_text("confidence: 0.5\nsolved_pfacts: []\n")
        (folder / "solution.md").write_text("Historical\n")
        (diseases / f"{slug}.yaml").write_text(f"category: {category}\n")
        row = dict.fromkeys(INDEX_FIELDNAMES, "0")
        row.update(slug=slug, status="RETRACTED", n_pfacts="2")
        rows.append(row)
    (base / "index.tsv").write_bytes(tsv(rows, INDEX_FIELDNAMES, "\r\n"))
    before = {p: p.read_bytes() for p in tmp_path.rglob("*") if p.is_file()}

    def invalid(_):
        raise ValueError("Invalid model")

    with pytest.raises(ValueError, match="Invalid model"):
        migrate(base, diseases, policy(), invalid)
    assert before == {p: p.read_bytes() for p in tmp_path.rglob("*") if p.is_file()}
    migrate(base, diseases, policy(), lambda _: None)
    with (base / "index.tsv").open() as stream:
        index = list(csv.DictReader(stream, delimiter="\t"))
    assert index[0]["status"] == "STALE_INPUT"
    assert index[1] == rows[1]
    for name in ("solution.yaml", "solution.md"):
        path = base / "disorders/Example" / name
        assert path.read_bytes() == before[path]
    assert (base / "proxy-merges/baseline/Example/kb.yaml").read_bytes() == before[
        base / "disorders/Example/kb.yaml"
    ]
    first = {p: p.read_bytes() for p in tmp_path.rglob("*") if p.is_file()}
    migrate(base, diseases, policy(), lambda _: None)
    assert first == {p: p.read_bytes() for p in tmp_path.rglob("*") if p.is_file()}
    p = policy()
    p.catalog["source_sha256"] = "changed"
    with pytest.raises(ValueError, match="catalog changed"):
        migrate(base, diseases, p, lambda _: None)
    path = base / "disorders/Example/kb.yaml"
    path.write_text(path.read_text() + "\n")
    with pytest.raises(ValueError, match="input changed"):
        migrate(base, diseases, policy(), lambda _: None)
    assert json.loads((base / "disorders/Example/proxy-merges.json").read_text())[
        "annotations"
    ]["MONDO:1"]
