"""What the quantitative medicine candidate filter must and must not count.

``model_qm_candidates`` reads fields dismech already records, so each step can
go wrong quietly: a mapping counted from the wrong prefix, a decision route
found through a biomarker that has no regulatory row, a model in ``models/``
missed because the record omits ``model_format``. Each test pins one of those.
"""

import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

import model_qm_candidates
from model_qm_candidates import assess, decision_targets, patient_mappings, read_order


def _model(**overrides) -> dict:
    model = {
        "name": "Urate model",
        "model_type": "KINETIC",
        "model_format": "SBML",
        "model_id": "BIOMD0000000001",
        "variables": [
            {
                "name": "Serum_Urate",
                "mappings_list": [
                    {"preferred_term": "Hyperuricemia", "term": {"id": "HP:0002149"}}
                ],
            }
        ],
        "modeled_mechanisms": [
            {
                "target": "Hyperuricemia",
                "relationship": "RECAPITULATES",
                "fidelity": "MODERATE",
            }
        ],
    }
    model.update(overrides)
    return model


ENTRY = {
    "name": "Gout",
    "biochemical": [
        {
            "name": "Serum urate",
            "readouts": [
                {
                    "target": "Hyperuricemia",
                    "regulatory_endpoint_refs": ["FDA_SE:row-1"],
                },
                {"target": "Tophus Formation"},
            ],
        }
    ],
    "treatments": [
        {
            "name": "Allopurinol",
            "target_mechanisms": [{"target": "Urate Overproduction"}],
        }
    ],
}


class TestSteps:
    def test_a_model_passing_every_step_is_a_candidate(self):
        row = assess(_model(), ENTRY, set())
        assert all(row["passed"].values())
        assert row["first_failed"] == ""

    def test_a_non_mechanistic_type_fails_step_one(self):
        row = assess(_model(model_type="MACHINE_LEARNING"), ENTRY, set())
        assert row["first_failed"] == "mechanistic"

    def test_a_model_in_models_dir_is_rerunnable_without_a_format(self):
        model = _model(model_format=None, model_id="urate_homeostasis")
        assert assess(model, ENTRY, {"urate_homeostasis"})["passed"]["rerunnable"]
        assert not assess(model, ENTRY, set())["passed"]["rerunnable"]

    def test_a_format_alone_is_not_rerunnable(self):
        model = _model(model_id=None, repository_url=None)
        assert not assess(model, ENTRY, set())["passed"]["rerunnable"]

    def test_only_loinc_and_hpo_mappings_count_as_patient_measurements(self):
        model = _model(
            variables=[
                {"name": "x", "mappings_list": [{"term": {"id": "CHEBI:17775"}}]},
                {"name": "y", "mappings_list": [{"term": {"id": "LOINC:3084-1"}}]},
            ]
        )
        assert patient_mappings(model) == ["LOINC:3084-1"]
        assert patient_mappings(_model(variables=[])) == []


class TestDecisionRoutes:
    def test_a_readout_without_a_regulatory_row_is_not_a_decision_route(self):
        routes = decision_targets(ENTRY)
        assert routes["Hyperuricemia"] == ["FDA surrogate endpoint"]
        assert "Tophus Formation" not in routes

    def test_a_treatment_target_is_a_decision_route(self):
        assert decision_targets(ENTRY)["Urate Overproduction"] == ["treatment target"]

    def test_a_model_linked_only_to_other_nodes_fails_step_four(self):
        model = _model(modeled_mechanisms=[{"target": "Tophus Formation"}])
        assert assess(model, ENTRY, set())["first_failed"] == "decision"


class TestReadOrder:
    def test_an_absent_fidelity_sorts_after_every_recorded_value(self):
        recorded = {"relationship": "", "fidelity": "LOW", "divergences": []}
        absent = {"relationship": "", "fidelity": "", "divergences": []}
        assert read_order(recorded) < read_order(absent)

    def test_an_invalidating_divergence_sorts_last(self):
        high = {
            "relationship": "RECAPITULATES",
            "fidelity": "HIGH",
            "divergences": [{"type": "PROXY_QUANTITY", "materiality": "INVALIDATING"}],
        }
        absent = {"relationship": "", "fidelity": "", "divergences": []}
        assert read_order(absent) < read_order(high)


class TestCollect:
    def test_the_funnel_counts_each_step_cumulatively(self, tmp_path):
        (tmp_path / "kb" / "disorders").mkdir(parents=True)
        entry = dict(
            ENTRY,
            computational_models=[
                _model(),
                _model(name="Classifier", model_type="MACHINE_LEARNING"),
                _model(name="Unmapped", variables=[]),
            ],
        )
        (tmp_path / "kb" / "disorders" / "Gout.yaml").write_text(yaml.safe_dump(entry))
        res = model_qm_candidates.collect(tmp_path, ["kb/disorders/*.yaml"])
        assert [s["kept"] for s in res["funnel"]] == [3, 2, 2, 1, 1]
        assert [m["name"] for m in res["candidates"]] == ["Urate model"]
        assert res["mapped_to_patient_measurements"] == 2
