"""Tests for `dismech.model_links`, the single walk over every ModelMechanismLink.

A `ModelMechanismLink` reaches the pathograph from four places: the three
top-level model sections, and the `model_systems` of a proposed experiment. The
fourth was skipped by both `tests/test_data.py` and
`scripts/model_scale_audit.py`, each of which walked only the top-level
sections, so the divergence, scale, readout-target and caveat gates had no
opinion on a link inside a `KNOWLEDGE_GAP` proposal — 27 such links across three
entries were already in `kb/` and unchecked (dismech#13375).

These tests pin the coverage rather than the counts: the point is that each of
the four homes is reached and that a proposed link is distinguishable from a
curated one, not how many happen to exist today.
"""

from pathlib import Path

import pytest
import yaml

from dismech.model_links import MODEL_SECTIONS, iter_model_links

ROOT_DIR = Path(__file__).parent.parent


def _entry(**sections):
    base = {"name": "Test Disease", "pathophysiology": [{"name": "Node A"}]}
    base.update(sections)
    return base


def _model(target="Node A", **link):
    return {"name": "M", "modeled_mechanisms": [{"target": target, **link}]}


@pytest.mark.parametrize("section", MODEL_SECTIONS)
def test_each_top_level_model_section_is_walked(section):
    sites = list(iter_model_links(_entry(**{section: [_model()]})))
    assert [s.path_prefix for s in sites] == [section]
    assert sites[0].proposed is False


def test_proposed_experiment_model_systems_are_walked():
    """The home that every gate used to skip."""
    data = _entry(
        discussions=[
            {
                "discussion_id": "g",
                "proposed_experiments": [
                    {"experiment_id": "e", "model_systems": [_model()]}
                ],
            }
        ]
    )
    sites = list(iter_model_links(data))
    assert len(sites) == 1
    assert sites[0].path_prefix == (
        "discussions[0].proposed_experiments[0].model_systems"
    )
    assert sites[0].proposed is True


def test_experiment_control_model_systems_are_walked():
    """A control carries model systems with the same shape as its experiment."""
    data = _entry(
        discussions=[
            {
                "discussion_id": "g",
                "proposed_experiments": [
                    {
                        "experiment_id": "e",
                        "controls": [{"name": "c", "model_systems": [_model()]}],
                    }
                ],
            }
        ]
    )
    sites = list(iter_model_links(data))
    assert len(sites) == 1
    assert sites[0].path_prefix == (
        "discussions[0].proposed_experiments[0].controls[0].model_systems"
    )
    assert sites[0].proposed is True


def test_path_prefix_composes_into_the_location_callers_format():
    """Callers build `f"{path_prefix}[{i}].modeled_mechanisms[{j}]"`.

    That formatting predates this module and must keep yielding a location that
    actually points at the link, now that the prefix can be a deep path.
    """
    data = _entry(
        discussions=[
            {
                "discussion_id": "g",
                "proposed_experiments": [
                    {"experiment_id": "x"},
                    {"experiment_id": "e", "model_systems": [{}, _model()]},
                ],
            }
        ]
    )
    site = next(s for s in iter_model_links(data) if s.proposed)
    location = (
        f"{site.path_prefix}[{site.model_index}].modeled_mechanisms[{site.link_index}]"
    )
    assert location == (
        "discussions[0].proposed_experiments[1].model_systems[1].modeled_mechanisms[0]"
    )


def test_include_proposed_false_restricts_to_curated_models():
    """A report about models that exist should be able to exclude proposals."""
    data = _entry(
        animal_models=[_model()],
        discussions=[
            {
                "discussion_id": "g",
                "proposed_experiments": [
                    {"experiment_id": "e", "model_systems": [_model()]}
                ],
            }
        ],
    )
    assert len(list(iter_model_links(data))) == 2
    curated = list(iter_model_links(data, include_proposed=False))
    assert [s.path_prefix for s in curated] == ["animal_models"]


@pytest.mark.parametrize(
    "data",
    [
        None,
        [],
        "string",
        {},
        {"animal_models": "not a list"},
        {"animal_models": ["not a dict"]},
        {"animal_models": [{"modeled_mechanisms": "not a list"}]},
        {"animal_models": [{"modeled_mechanisms": ["not a dict"]}]},
        {"discussions": "not a list"},
        {"discussions": [{"proposed_experiments": "not a list"}]},
        {"discussions": [{"proposed_experiments": [{"controls": "not a list"}]}]},
    ],
)
def test_malformed_input_yields_nothing_rather_than_raising(data):
    """Shape errors are another check's job; this walk must not crash on them."""
    assert list(iter_model_links(data)) == []


@pytest.mark.kb_data
def test_the_committed_proposed_links_are_reached():
    """Regression: the entry whose link exposed the gap is now walked.

    `model_scale_audit` reported `model->mechanism links: 0` for this file while
    it carried one, which is what made a vacuous "the link is ALIGNED" claim
    possible in the first place.
    """
    path = ROOT_DIR / "kb" / "disorders" / "Prolidase_Deficiency.yaml"
    with path.open(encoding="utf-8") as handle:
        data = yaml.safe_load(handle)
    proposed = [s for s in iter_model_links(data) if s.proposed]
    assert proposed, "the proposed-experiment model link is not being walked"
    assert all(s.link.get("target") for s in proposed)
