"""A pathophysiology node may conform to more than one module node (dismech#13923).

``conforms_to`` accepts a single string or a list of strings. These tests pin
the three places that has to hold: the schema accepts both spellings, the
reader normalises both, and the KB foreign-key check resolves every list item.
"""

from __future__ import annotations

import pytest
from linkml.validator import Validator
from linkml.validator.plugins import JsonschemaValidationPlugin

from dismech.conformance import iter_conforms_to, module_stem, normalize_conforms_to
from tests.test_data import (
    SCHEMA_PATH,
    _iter_conforms_to,
    check_conforms_to_module_node_references,
)

MTORC1 = "mtorc1_hyperactivation#Constitutive mTORC1 Hyperactivation"
NUTRIENT = "deregulated_nutrient_sensing#mTORC1 Hyperactivation"


@pytest.mark.parametrize(
    ("value", "expected"),
    [
        (None, []),
        ("", []),
        ("  ", []),
        (MTORC1, [MTORC1]),
        (f"  {MTORC1} ", [MTORC1]),
        ([MTORC1, NUTRIENT], [MTORC1, NUTRIENT]),
        ([MTORC1, "", None, 3, NUTRIENT], [MTORC1, NUTRIENT]),
        ([MTORC1, MTORC1], [MTORC1, MTORC1]),  # duplicates are the KB check's job
        ({"not": "a ref"}, []),
    ],
)
def test_normalize_conforms_to(value, expected):
    assert normalize_conforms_to(value) == expected


def test_iter_conforms_to_reads_a_node():
    assert iter_conforms_to({"name": "x", "conforms_to": [MTORC1, NUTRIENT]}) == [
        MTORC1,
        NUTRIENT,
    ]
    assert iter_conforms_to({"name": "x"}) == []
    assert iter_conforms_to("not a node") == []


def test_module_stem():
    assert module_stem(MTORC1) == "mtorc1_hyperactivation"
    assert module_stem("fibrotic_response") == "fibrotic_response"


@pytest.fixture(scope="module")
def validator():
    return Validator(
        SCHEMA_PATH,
        validation_plugins=[JsonschemaValidationPlugin(closed=True)],
    )


def _disease(conforms_to):
    return {
        "name": "Synthetic",
        "pathophysiology": [{"name": "Node", "conforms_to": conforms_to}],
    }


@pytest.mark.parametrize("conforms_to", [MTORC1, [MTORC1], [MTORC1, NUTRIENT]])
def test_schema_accepts_scalar_and_list(validator, conforms_to):
    """Both spellings validate, so the ~3,500 scalar lines never need migrating."""
    report = validator.validate(_disease(conforms_to), target_class="Disease")
    assert not [r.message for r in report.results if "conforms_to" in r.message]


@pytest.mark.parametrize("conforms_to", [3, [MTORC1, 3], {"target": MTORC1}])
def test_schema_rejects_non_string_references(validator, conforms_to):
    report = validator.validate(_disease(conforms_to), target_class="Disease")
    assert [r for r in report.results if "conforms_to" in r.message]


def test_every_list_item_is_yielded_with_its_own_path():
    pairs = list(_iter_conforms_to(_disease([MTORC1, NUTRIENT])))
    assert pairs == [
        ("pathophysiology[0].conforms_to[0]", MTORC1),
        ("pathophysiology[0].conforms_to[1]", NUTRIENT),
    ]
    assert list(_iter_conforms_to(_disease(MTORC1))) == [
        ("pathophysiology[0].conforms_to", MTORC1)
    ]


def test_foreign_key_check_resolves_every_list_item():
    check_conforms_to_module_node_references("Synthetic.yaml", _disease([MTORC1, NUTRIENT]))
    with pytest.raises(AssertionError, match=r"conforms_to\[1\].*no_such_module"):
        check_conforms_to_module_node_references(
            "Synthetic.yaml", _disease([MTORC1, "no_such_module#Anything"])
        )


def test_foreign_key_check_rejects_a_reference_listed_twice():
    with pytest.raises(AssertionError, match="listed twice on the same node"):
        check_conforms_to_module_node_references(
            "Synthetic.yaml", _disease([MTORC1, MTORC1])
        )


def test_the_same_reference_on_two_nodes_is_not_a_duplicate():
    data = {
        "name": "Synthetic",
        "pathophysiology": [
            {"name": "A", "conforms_to": MTORC1},
            {"name": "B", "conforms_to": [MTORC1]},
        ],
    }
    check_conforms_to_module_node_references("Synthetic.yaml", data)


# Consumers. Each of these used to read `conforms_to` as a string, so a list
# was skipped or, in the KGX exporter, stringified into one bogus reference.


def test_maximal_kgx_export_emits_one_edge_per_reference():
    from dismech.export.maximal_kgx_export import GraphAccumulator, process_entry
    from dismech.export.sepio_export import pathophysiology_node_id

    acc = GraphAccumulator()
    process_entry(acc, "Synthetic", _disease([MTORC1, NUTRIENT]), "disorder")
    node_id = pathophysiology_node_id("Synthetic", "Node")
    objects = {o for s, p, o in acc.edges if s == node_id and p == "dismech:conforms_to"}
    assert objects == {
        pathophysiology_node_id("mtorc1_hyperactivation", "Constitutive mTORC1 Hyperactivation"),
        pathophysiology_node_id("deregulated_nutrient_sensing", "mTORC1 Hyperactivation"),
    }


def test_grouping_facts_collect_every_module():
    from dismech.groupings import extract_disease_facts

    facts = extract_disease_facts("Synthetic", _disease([MTORC1, NUTRIENT]))
    assert facts.module_stems == {"mtorc1_hyperactivation", "deregulated_nutrient_sensing"}
    assert len(facts.module_refs) == 2


def test_module_map_walk_yields_every_reference():
    from dismech.export.module_map import _iter_conforms

    assert list(_iter_conforms(_disease([MTORC1, NUTRIENT]))) == [
        (MTORC1, "Node"),
        (NUTRIENT, "Node"),
    ]


def test_list_paths_index_the_raw_list():
    data = _disease([MTORC1, 3, NUTRIENT])
    assert list(_iter_conforms_to(data))[-1] == (
        "pathophysiology[0].conforms_to[2]",
        NUTRIENT,
    )


def test_embedding_label_ignores_reference_order():
    from dismech.node_embeddings.cli import _label
    from dismech.node_embeddings.nodes import PathoNode

    a = PathoNode("D", "x", (MTORC1, NUTRIENT), ())
    b = PathoNode("D", "x", (NUTRIENT, MTORC1), ())
    assert _label(a) == _label(b)
