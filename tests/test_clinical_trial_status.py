"""Tests for the ClinicalTrials.gov status audit (offline: no network)."""

from pathlib import Path

from dismech.clinical_trial_status import (
    CuratedTrial,
    PHASE_MAP,
    STATUS_MAP,
    audit_trials,
    fetch_live_studies,
    iter_curated_trials,
    render_markdown,
    render_text,
    AuditReport,
    _resolve_nct_id,
)


def _trial(**kwargs):
    base = dict(
        path="kb/disorders/Example.yaml",
        index=0,
        nct_id="NCT00000001",
        name="NCT00000001",
        status="RECRUITING",
        phase="PHASE_II",
    )
    base.update(kwargs)
    return CuratedTrial(**base)


def _live(status="RECRUITING", phases=("PHASE2",), last_update="2026-01-01"):
    return {"NCT00000001": {"status": status, "phases": list(phases), "last_update": last_update}}


# --------------------------------------------------------------------------
# id resolution
# --------------------------------------------------------------------------


def test_resolve_nct_id_prefers_name():
    assert _resolve_nct_id({"name": "NCT06087757"}) == "NCT06087757"


def test_resolve_nct_id_falls_back_to_evidence_reference():
    """8 KB trials are named by acronym/EudraCT but may still cite an NCT record."""
    trial = {
        "name": "EMERALD",
        "evidence": [{"reference": "clinicaltrials:NCT03778931"}],
    }
    assert _resolve_nct_id(trial) == "NCT03778931"


def test_resolve_nct_id_returns_none_when_unresolvable():
    assert _resolve_nct_id({"name": "ML-DS 2006 (EudraCT 2007-006219-2)"}) is None


def test_resolve_nct_id_is_case_insensitive_and_normalizes():
    assert _resolve_nct_id({"name": "nct06087757"}) == "NCT06087757"


# --------------------------------------------------------------------------
# drift detection
# --------------------------------------------------------------------------


def test_no_findings_when_curated_matches_registry():
    assert audit_trials([_trial()], _live()) == []


def test_status_drift_is_reported():
    findings = audit_trials([_trial(status="RECRUITING")], _live(status="COMPLETED"))

    assert [f.kind for f in findings] == ["status_drift"]
    assert findings[0].curated == "RECRUITING"
    assert findings[0].live == "COMPLETED"
    assert findings[0].last_update == "2026-01-01"


def test_terminated_status_is_flagged_as_a_curation_signal():
    """TERMINATED is rarely a one-field edit -- it should stand out in the report."""
    findings = audit_trials([_trial(status="COMPLETED")], _live(status="TERMINATED"))

    assert findings[0].curation_signal is True


def test_completed_status_is_not_a_curation_signal():
    findings = audit_trials([_trial(status="RECRUITING")], _live(status="COMPLETED"))

    assert findings[0].curation_signal is False


def test_not_yet_recruiting_maps_to_dismech_not_recruiting():
    assert audit_trials([_trial(status="NOT_RECRUITING")], _live(status="NOT_YET_RECRUITING")) == []


def test_multi_phase_registry_record_matches_any_of_its_phases():
    """A PHASE1|PHASE2 registry record must not drift against curated PHASE_I."""
    assert audit_trials([_trial(phase="PHASE_I")], _live(phases=("PHASE1", "PHASE2"))) == []
    assert audit_trials([_trial(phase="PHASE_II")], _live(phases=("PHASE1", "PHASE2"))) == []


def test_phase_drift_is_reported():
    findings = audit_trials([_trial(phase="PHASE_III")], _live(phases=("PHASE1",)))

    assert [f.kind for f in findings] == ["phase_drift"]
    assert findings[0].live == "PHASE_I"


def test_missing_curated_status_is_reported_separately_from_drift():
    findings = audit_trials([_trial(status=None)], _live())

    assert [f.kind for f in findings] == ["missing_status"]
    assert findings[0].live == "RECRUITING"


def test_missing_curated_phase_is_reported():
    findings = audit_trials([_trial(phase=None)], _live())

    assert [f.kind for f in findings] == ["missing_phase"]


def test_missing_phase_not_reported_when_registry_has_none():
    assert audit_trials([_trial(phase=None)], _live(phases=())) == []


def test_id_absent_from_registry_is_reported_as_not_found():
    findings = audit_trials([_trial()], {})

    assert [f.kind for f in findings] == ["not_found"]


def test_unresolvable_id_is_reported_and_not_queried():
    findings = audit_trials([_trial(nct_id=None, name="BESTCILIA")], {})

    assert [f.kind for f in findings] == ["unresolvable_id"]


def test_expanded_access_status_is_unmappable_not_silently_coerced():
    """AVAILABLE has no ClinicalTrialStatusEnum equivalent; do not coerce to UNKNOWN."""
    findings = audit_trials([_trial()], _live(status="AVAILABLE"))

    kinds = [f.kind for f in findings]
    assert "unmappable_status" in kinds
    assert "status_drift" not in kinds


# --------------------------------------------------------------------------
# enum mappings stay aligned with the schema
# --------------------------------------------------------------------------


def test_status_map_targets_are_all_real_schema_enum_values():
    import yaml

    schema = yaml.safe_load(
        (Path(__file__).parent.parent / "src/dismech/schema/dismech.yaml").read_text()
    )
    allowed = set(schema["enums"]["ClinicalTrialStatusEnum"]["permissible_values"])

    assert set(STATUS_MAP.values()) <= allowed


def test_phase_map_targets_are_all_real_schema_enum_values():
    import yaml

    schema = yaml.safe_load(
        (Path(__file__).parent.parent / "src/dismech/schema/dismech.yaml").read_text()
    )
    allowed = set(schema["enums"]["ClinicalTrialPhaseEnum"]["permissible_values"])

    assert set(PHASE_MAP.values()) <= allowed


# --------------------------------------------------------------------------
# KB traversal and fetch batching
# --------------------------------------------------------------------------


def test_iter_curated_trials_reads_status_and_phase(tmp_path):
    path = tmp_path / "Example.yaml"
    path.write_text(
        "name: Example\n"
        "clinical_trials:\n"
        "- name: NCT00000001\n"
        "  phase: PHASE_II\n"
        "  status: RECRUITING\n"
        "- name: NCT00000002\n",
        encoding="utf-8",
    )

    trials = list(iter_curated_trials([path]))

    assert [t.nct_id for t in trials] == ["NCT00000001", "NCT00000002"]
    assert trials[0].status == "RECRUITING"
    assert trials[1].status is None
    assert trials[0].location == "Example.yaml:clinical_trials[0]"


def test_iter_curated_trials_skips_unparseable_file(tmp_path):
    bad = tmp_path / "Bad.yaml"
    bad.write_text("name: [unclosed\n", encoding="utf-8")

    assert list(iter_curated_trials([bad])) == []


def test_fetch_live_studies_batches_requests():
    """~800 ids must not become ~800 requests."""
    calls = []

    class FakeResponse:
        def raise_for_status(self):
            pass

        def json(self):
            return {"studies": []}

    class FakeSession:
        def get(self, url, params=None, timeout=None):
            calls.append(params["filter.ids"].split(","))
            return FakeResponse()

    ids = [f"NCT{i:08d}" for i in range(250)]
    fetch_live_studies(ids, batch_size=100, rate_limit_delay=0, session=FakeSession())

    assert [len(c) for c in calls] == [100, 100, 50]


def test_fetch_live_studies_parses_registry_payload():
    class FakeResponse:
        def raise_for_status(self):
            pass

        def json(self):
            return {
                "studies": [
                    {
                        "protocolSection": {
                            "identificationModule": {"nctId": "NCT00000001"},
                            "statusModule": {
                                "overallStatus": "COMPLETED",
                                "lastUpdateSubmitDate": "2025-12-10",
                            },
                            "designModule": {"phases": ["PHASE3"]},
                        }
                    }
                ]
            }

    class FakeSession:
        def get(self, url, params=None, timeout=None):
            return FakeResponse()

    live = fetch_live_studies(["NCT00000001"], rate_limit_delay=0, session=FakeSession())

    assert live == {
        "NCT00000001": {
            "status": "COMPLETED",
            "phases": ["PHASE3"],
            "last_update": "2025-12-10",
        }
    }


# --------------------------------------------------------------------------
# rendering
# --------------------------------------------------------------------------


def test_render_text_states_that_nothing_was_modified():
    report = AuditReport(trials_seen=1, ids_resolved=1, ids_queried=1, ids_returned=1)
    report.findings = audit_trials([_trial()], _live(status="COMPLETED"))

    text = render_text(report)

    assert "Status drift" in text
    assert "no KB files were modified" in text


def test_render_markdown_emits_a_table_row_per_finding():
    report = AuditReport(trials_seen=1, ids_resolved=1, ids_queried=1, ids_returned=1)
    report.findings = audit_trials([_trial()], _live(status="COMPLETED"))

    markdown = render_markdown(report)

    assert markdown.startswith("# ClinicalTrials.gov status audit")
    assert "status_drift" in markdown
