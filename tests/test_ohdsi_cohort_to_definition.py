"""Tests for scripts/ohdsi_cohort_to_definition.py.

Covers the local file-parse mapping and the WebAPI live-fetch normalization
(the WebAPI envelope carries ``expression`` as a JSON-encoded string, which must
be normalized to a dict before the shared parser runs). The fetch is exercised
with a stubbed HTTP layer so the test needs no network.
"""

from __future__ import annotations

import json
import types

import httpx

from scripts.ohdsi_cohort_to_definition import (
    build_definition,
    fetch_cohort_from_webapi,
)


def _args(**overrides):
    base = {"name": None, "description": None, "scope": None}
    base.update(overrides)
    return types.SimpleNamespace(**base)


def _sample_expression():
    return {
        "ConceptSets": [
            {
                "id": 0,
                "name": "Asthma",
                "expression": {"items": [{"c": 1}, {"c": 2}, {"c": 3}]},
            }
        ],
        "InclusionRules": [{"name": "Age >= 18"}],
    }


def test_build_definition_from_file_shape():
    data = {
        "name": "Type 2 diabetes mellitus",
        "description": "Cohort of T2DM patients.",
        "expression": _sample_expression(),
    }

    definition = build_definition(data, _args())

    assert definition["name"] == "Type 2 diabetes mellitus"
    assert definition["definition_type"] == "PHENOTYPE_ALGORITHM"
    assert definition["scope"] == "OMOP CDM (OHDSI)"

    primary = definition["criteria_sets"][0]
    assert primary["name"] == "Primary criteria"
    assert primary["inclusion_criteria"][0] == {
        "preferred_term": "Concept set: Asthma",
        "description": "3 concept(s)",
    }
    assert any(cs["name"] == "Age >= 18" for cs in definition["criteria_sets"])


def test_fetch_cohort_from_webapi_normalizes_string_expression(monkeypatch):
    envelope = {
        "id": 7,
        "name": "Asthma cohort",
        "description": "desc",
        # WebAPI returns the cohort expression as a JSON-encoded *string*.
        "expression": json.dumps(_sample_expression()),
    }

    class _FakeResponse:
        def raise_for_status(self):
            return None

        def json(self):
            return envelope

    class _FakeClient:
        def __init__(self, *args, **kwargs):
            pass

        def __enter__(self):
            return self

        def __exit__(self, *args):
            return False

        def get(self, url, headers=None):
            assert url == "https://example.org/WebAPI/cohortdefinition/7"
            return _FakeResponse()

    monkeypatch.setattr(httpx, "Client", _FakeClient)

    data = fetch_cohort_from_webapi("https://example.org/WebAPI/", 7)

    # The string expression must be parsed into a dict for the shared parser.
    assert isinstance(data["expression"], dict)

    definition = build_definition(data, _args())
    assert definition["name"] == "Asthma cohort"
    assert (
        definition["criteria_sets"][0]["inclusion_criteria"][0]["description"]
        == "3 concept(s)"
    )
