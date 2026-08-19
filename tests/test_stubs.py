"""Tests for the curation stub queue under `stubs/`.

The load-bearing test is `test_no_stub_survives_curation`: a disease that has
been curated must not still have a stub. That is what makes "delete the stub,
add the entry" a contract CI can check rather than a convention people remember.
"""

from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path

import pytest
from linkml.validator import Validator

from dismech.stubs.claims import (
    Claim,
    double_claims,
    index_claims,
    non_disease_claims,
    parse_claims,
    unkeyed_claims,
)
from dismech.stubs import (
    build_coverage_index,
    check_stubs,
    iter_stub_files,
    load_stubs,
    slugify_label,
    stub_filename,
)
from dismech.stubs.seed import (
    Nomination,
    parse_rare_disease_identification,
    render_stub,
)

ROOT_DIR = Path(__file__).parent.parent
STUB_DIR = ROOT_DIR / "stubs"
STUB_SCHEMA_PATH = ROOT_DIR / "src" / "dismech" / "schema" / "curation_stub.yaml"

STUB_FILES = iter_stub_files(STUB_DIR)


@pytest.fixture(scope="module")
def coverage():
    return build_coverage_index()


@pytest.fixture(scope="module")
def issues():
    return check_stubs(STUB_DIR)


@pytest.fixture(scope="module")
def stub_validator():
    return Validator(str(STUB_SCHEMA_PATH))


def test_stub_dir_exists():
    assert STUB_DIR.is_dir(), "stubs/ is the curation queue and must exist"


@pytest.mark.parametrize("path", STUB_FILES, ids=lambda p: p.name)
def test_stub_validates_against_schema(path, stub_validator):
    from dismech.yaml_io import safe_load

    data = safe_load(path.read_text(encoding="utf-8"))
    report = stub_validator.validate(data, target_class="CurationStub")
    messages = [r.message for r in report.results]
    assert not messages, f"{path.name}: {messages}"


def test_no_stub_survives_curation(issues):
    """A curated disease must not still have a stub file."""
    stale = [i for i in issues if i.kind == "already_curated"]
    assert not stale, (
        "These stubs name a MONDO ID the KB already covers. A curation PR must "
        "delete the stub it curates:\n" + "\n".join(i.format() for i in stale)
    )


def test_stub_mondo_ids_are_unique(issues):
    dupes = [i for i in issues if i.kind == "duplicate_mondo_id"]
    assert not dupes, "\n".join(i.format() for i in dupes)


def test_stub_filenames_match_labels(issues):
    mismatched = [i for i in issues if i.kind == "filename_mismatch"]
    assert not mismatched, "\n".join(i.format() for i in mismatched)


def test_stub_enum_values_are_valid(issues):
    bad = [
        i for i in issues if i.kind.startswith("bad_") or i.kind.startswith("missing_")
    ]
    assert not bad, "\n".join(i.format() for i in bad)


def test_check_reports_no_errors(issues):
    """`just check-stubs` gates on errors only; advisories are informational."""
    errors = [i for i in issues if i.severity == "error"]
    assert not errors, "\n".join(i.format() for i in errors)


@pytest.mark.parametrize(
    ("label", "expected"),
    [
        ("alcohol sensitivity, acute", "Alcohol_Sensitivity_Acute"),
        ("22q11.2 deletion syndrome", "22q11.2_Deletion_Syndrome"),
        ("Behçet disease", "Behcet_Disease"),
        ("IgG4-related disease", "IgG4-related_Disease"),
    ],
)
def test_slugify_label(label, expected):
    assert slugify_label(label) == expected


def test_stub_filename_falls_back_to_mondo_id():
    assert stub_filename("!!!", "MONDO:0000001") == "MONDO_0000001.yaml"


def test_rdi_parser_normalizes_an_entry():
    payload = {
        "diseases": [
            {
                "mondo_id": "MONDO:0012454",
                "mondo_label": "alcohol sensitivity, acute",
                "mondo_synonyms": ["alcohol intolerance"],
                "justification_summary": ["Diagnostic delay impact"],
                "prioritization_category": "initial",
                "prevalence_category": "H",
            }
        ]
    }
    (nomination,) = parse_rare_disease_identification(payload)
    assert nomination.mondo_id == "MONDO:0012454"
    assert nomination.rationale == "Diagnostic delay impact"
    assert "prioritization_category=initial" in nomination.tags


def test_seeded_stubs_do_not_prejudge_entry_type():
    """A seeder cannot decide Disease vs Grouping; that is a curator's call."""
    payload = render_stub(
        Nomination(mondo_id="MONDO:0000001", label="test disease"),
        source_name="test",
        source_url=None,
        added="2026-01-01",
    )
    assert payload["entry_type"] == "UNDECIDED"
    assert payload["priority"] == "NORMAL"
    assert payload["status"] == "OPEN"


def test_stubs_are_not_all_claimed():
    """Sanity check that the queue still has work in it."""
    stubs = load_stubs(STUB_DIR)
    if not stubs:
        pytest.skip("stub queue is empty")
    assert any(s.status == "OPEN" for s in stubs)


# --- Claims: GitHub is the live lock -----------------------------------------

_GH_ROWS = [
    {
        "number": 8955,
        "title": "Curate rickets (MONDO:0005520)",
        "assignees": [{"login": "sierra-moxon"}],
        "createdAt": "2026-08-19T15:49:27Z",
    },
    {
        # Long-open, no PR — the stale case.
        "number": 1675,
        "title": "Curate autosomal dominant cerebellar ataxia type I (MONDO:0019792)",
        "assignees": [{"login": "dragon-ai-agent"}],
        "createdAt": "2026-04-24T21:26:21Z",
    },
    {
        # Real issue #2029: no MONDO ID in the title, so it locks nothing.
        "number": 2029,
        "title": "curate peripartum cardiomyopathy",
        "assignees": [],
        "createdAt": "2026-05-04T17:44:35Z",
    },
]

_NOW = datetime(2026, 8, 19, tzinfo=timezone.utc)


def test_parse_claims_keys_on_the_mondo_id_in_the_title():
    claims = parse_claims(_GH_ROWS)
    assert [c.mondo_id for c in claims] == [
        "MONDO:0005520",
        "MONDO:0019792",
        None,
    ]
    assert claims[0].assignees == ["sierra-moxon"]


def test_parse_claims_accepts_both_assignee_shapes():
    (plain,) = parse_claims(
        [{"number": 1, "title": "Curate x (MONDO:0000001)", "assignees": ["bob"]}]
    )
    assert plain.assignees == ["bob"]


def test_unkeyed_claims_are_reported_not_silently_dropped():
    """An issue with no MONDO ID locks nothing; it must surface for retitling."""
    (unkeyed,) = unkeyed_claims(parse_claims(_GH_ROWS))
    assert unkeyed.number == 2029


def test_module_claims_are_not_nagged_for_a_missing_mondo_id():
    """The label covers "a disease (or other entry)"; modules have no MONDO ID."""
    rows = _GH_ROWS + [
        {
            "number": 9100,
            "title": "Claim: refresh the fibrotic_response module",
            "assignees": [],
        }
    ]
    claims = parse_claims(rows)
    assert [c.number for c in unkeyed_claims(claims)] == [2029]
    assert [c.number for c in non_disease_claims(claims)] == [9100]


def test_index_claims_maps_mondo_id_to_claim():
    index = index_claims(parse_claims(_GH_ROWS))
    assert index["MONDO:0005520"].number == 8955
    assert None not in index


def test_double_claims_detects_two_issues_on_one_disease():
    rows = _GH_ROWS + [
        {"number": 9001, "title": "Curate rickets (MONDO:0005520)", "assignees": []}
    ]
    doubles = double_claims(parse_claims(rows))
    assert set(doubles) == {"MONDO:0005520"}
    assert [c.number for c in doubles["MONDO:0005520"]] == [8955, 9001]


def test_a_claim_with_an_open_pr_is_never_stale():
    """Curation PRs sit in review for weeks; the lock must outlast them."""
    old_with_pr = Claim(
        number=1,
        title="Curate x (MONDO:0000001)",
        mondo_id="MONDO:0000001",
        created_at="2026-01-01T00:00:00Z",
        has_linked_pr=True,
    )
    assert old_with_pr.age_days(_NOW) > 200
    assert old_with_pr.is_stale(30, _NOW) is False


def test_an_old_claim_with_no_pr_is_stale():
    old, fresh = parse_claims(_GH_ROWS)[1], parse_claims(_GH_ROWS)[0]
    assert old.is_stale(30, _NOW) is True
    assert fresh.is_stale(30, _NOW) is False


def test_claims_with_no_created_at_are_not_guessed_stale():
    claim = Claim(number=1, title="t", mondo_id="MONDO:0000001")
    assert claim.age_days(_NOW) is None
    assert claim.is_stale(30, _NOW) is False


def test_stub_schema_has_no_claim_fields():
    """One fact, one source of truth: claiming lives on GitHub, not in YAML."""
    from dismech.stubs.model import STATUSES

    assert "CLAIMED" not in STATUSES
    schema = (STUB_SCHEMA_PATH).read_text(encoding="utf-8")
    assert "claimed_by" not in schema
