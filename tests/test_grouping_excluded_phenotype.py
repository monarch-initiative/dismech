"""An excluded phenotype must not satisfy a HAS_PHENOTYPE criterion.

A curated entry can record a phenotype in order to say it is *absent*:
``frequency: EXCLUDED`` on the phenotype record, or ``modifier: ABSENT`` on its
descriptor. ``extract_disease_facts`` used to fold both into the presence facts,
so a grouping criterion naming that term was satisfied by the very record that
denied it. ``Mucopolysaccharidosis type X`` is the live case: it records
``Dysostosis multiplex`` (HP:0000943) as EXCLUDED, and the Mucopolysaccharidoses
grouping's criterion names that term.
"""

from __future__ import annotations

import pytest

from dismech import groupings as G


def _entry(**phenotype_extra) -> dict:
    return {
        "name": "Test Disease",
        "phenotypes": [
            {
                "name": "Dysostosis multiplex",
                "phenotype_term": {
                    "preferred_term": "Dysostosis multiplex",
                    "term": {"id": "HP:0000943", "label": "Dysostosis multiplex"},
                    **phenotype_extra.pop("descriptor", {}),
                },
                **phenotype_extra,
            }
        ],
    }


def _leaf() -> dict:
    return {
        "criterion_predicate": "HAS_PHENOTYPE",
        "description": "Dysostosis multiplex.",
        "phenotype_term": {"term": {"id": "HP:0000943"}},
    }


@pytest.fixture(autouse=True)
def exact_matching():
    """Closure is irrelevant here; evaluate on exact ids to stay offline."""
    G.term_closure.cache_clear()
    G.set_closure_enabled(False)
    yield
    G.term_closure.cache_clear()
    G.set_closure_enabled(True)


def test_present_phenotype_is_a_fact():
    facts = G.extract_disease_facts("Test Disease", _entry(frequency="FREQUENT"))
    assert facts.phenotype_freq == {"HP:0000943": "FREQUENT"}
    assert G._eval_leaf(_leaf(), facts) is G.Satisfaction.SATISFIED


def test_excluded_frequency_is_not_a_presence_fact():
    facts = G.extract_disease_facts("Test Disease", _entry(frequency="EXCLUDED"))
    assert "HP:0000943" not in facts.phenotype_freq
    assert G._eval_leaf(_leaf(), facts) is G.Satisfaction.NOT_SATISFIED


def test_absent_modifier_is_not_a_presence_fact():
    facts = G.extract_disease_facts(
        "Test Disease", _entry(descriptor={"modifier": "ABSENT"})
    )
    assert "HP:0000943" not in facts.phenotype_freq
    assert G._eval_leaf(_leaf(), facts) is G.Satisfaction.NOT_SATISFIED


def test_exclusion_does_not_erase_a_separate_presence_record():
    """An entry may exclude a term in one subtype and assert it in another."""
    data = _entry(frequency="EXCLUDED")
    data["phenotypes"].append(
        {
            "name": "Dysostosis multiplex (other subtype)",
            "frequency": "OCCASIONAL",
            "phenotype_term": {"term": {"id": "HP:0000943"}},
        }
    )
    facts = G.extract_disease_facts("Test Disease", data)
    assert facts.phenotype_freq == {"HP:0000943": "OCCASIONAL"}
