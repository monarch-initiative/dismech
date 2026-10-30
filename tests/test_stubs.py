"""Tests for the curation stub queue under `stubs/`.

The load-bearing test is `test_no_stub_survives_curation`: a disease that has
been curated must not still have a stub. That is what makes "delete the stub,
add the entry" a contract CI can check rather than a convention people remember.
"""

from __future__ import annotations

import json
from datetime import UTC, datetime
from pathlib import Path

import pytest
from linkml.validator import Validator
from linkml.validator.plugins import JsonschemaValidationPlugin

from dismech.stubs import (
    build_coverage_index,
    check_stubs,
    iter_stub_files,
    load_stubs,
    slugify_label,
    stub_filename,
)
from dismech.stubs.claims import (
    Claim,
    double_claims,
    index_claims,
    non_disease_claims,
    parse_claims,
    unkeyed_claims,
)
from dismech.stubs.seed import (
    Nomination,
    _dump,
    parse_rare_disease_identification,
    render_stub,
    yaml_scalar,
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
    # An explicit plugin is required: a plugin-less Validator returns an empty
    # report for any instance, making every assertion vacuous (dismech#8320).
    # `closed=True` is the `linkml-validate` CLI default, so pytest and CI
    # agree on unknown properties as well as on required ones.
    return Validator(
        str(STUB_SCHEMA_PATH),
        validation_plugins=[JsonschemaValidationPlugin(closed=True)],
    )


def test_stub_validator_fixture_is_not_inert(stub_validator):
    """Guard: the ``stub_validator`` fixture must actually validate.

    A plugin-less ``Validator`` short-circuits to an empty report, turning
    every stub conformance assertion into a no-op (dismech#8320).
    """
    report = stub_validator.validate(
        {"label": "no mondo_id"}, target_class="CurationStub"
    )
    errors = [r for r in report.results if r.severity.name == "ERROR"]

    assert errors, (
        "stub_validator produced no errors for a CurationStub missing its required "
        "`mondo_id` — it has no validation plugins and every test using it is vacuous"
    )


def test_stub_dir_exists():
    assert STUB_DIR.is_dir(), "stubs/ is the curation queue and must exist"


@pytest.mark.parametrize("path", STUB_FILES, ids=lambda p: p.name)
def test_stub_validates_against_schema(path, stub_validator):
    from dismech.yaml_io import safe_load

    data = safe_load(path.read_text(encoding="utf-8"))
    report = stub_validator.validate(data, target_class="CurationStub")
    messages = [r.message for r in report.results]
    assert not messages, f"{path.name}: {messages}"


def test_staleness_never_gates(issues):
    """A stale stub is drift, not a fault — it must not fail anyone's build.

    Stubs are informative, not curated content. If `already_curated` gated, an
    unrelated curation PR merging on `main` would turn every open stub PR red
    through no fault of its author, and curators would spend their time
    servicing a bookkeeping message. `dismech-stubs tidy` clears these instead.
    """
    for issue in issues:
        if issue.kind in {"already_curated", "obsolete_term"}:
            assert issue.severity == "advisory", (
                f"{issue.kind} must be advisory, not a gating error: {issue.format()}"
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


def test_obsolete_terms_are_reported_for_tidying(issues):
    """MONDO prefixes a retired concept's label. Reported, not gated."""
    for issue in issues:
        if issue.kind == "obsolete_term":
            assert issue.severity == "advisory"


# --- Obsolescence read from MONDO, not guessed from the label ----------------
#
# The label heuristic only fires when the nominating export captured the label
# after MONDO prefixed it with "obsolete", which is the unusual case — it
# matches none of the committed stubs while at least one names a term MONDO has
# ruled on (issue #10785). These cover the ontology-backed replacement: the
# SQLite reader against a fixture database, and the offline check that reads
# what the reader wrote into the stub.


def _fixture_mondo_db(tmp_path):
    """A semantic-SQL-shaped `statements` table holding four terms.

    A fixture rather than the live ontology: the real build is a ~1.2 GB
    download, and its contents move under us — `MONDO:0859244` is an obsoletion
    candidate in the pinned release and will be plainly obsolete in some later
    one, so a test asserting either against the real file has a scheduled
    failure in it.
    """
    import sqlite3

    path = tmp_path / "mondo.db"
    conn = sqlite3.connect(path)
    conn.execute(
        "create table statements "
        "(subject text, predicate text, object text, value text, datatype text)"
    )
    conn.executemany(
        "insert into statements (subject, predicate, object, value) values (?,?,?,?)",
        [
            (
                "obo:mondo.owl",
                "owl:versionIRI",
                "obo:mondo/releases/2026-05-05/mondo.owl",
                None,
            ),
            # Merged away, with a successor.
            ("MONDO:0000001", "owl:deprecated", None, "true"),
            ("MONDO:0000001", "IAO:0100001", "MONDO:0000002", None),
            # Retired with nothing to point at.
            ("MONDO:0000003", "owl:deprecated", None, "true"),
            # Decided but not yet done: still live, no deprecation flag.
            ("MONDO:0000004", "oio:inSubset", "obo:mondo#obsoletion_candidate", None),
            (
                "MONDO:0000004",
                "rdfs:comment",
                None,
                (
                    "This term is scheduled to be merged with MONDO:0000005 "
                    "other disease ... and replaced with MONDO:0000005"
                ),
            ),
            (
                "MONDO:0000004",
                "IAO:0000233",
                None,
                "https://github.com/monarch-initiative/mondo/issues/1",
            ),
            # Explicitly not retired. `owl:deprecated false` exists in the wild.
            ("MONDO:0000006", "owl:deprecated", None, "false"),
        ],
    )
    conn.commit()
    conn.close()
    return path


def test_obsolescence_is_read_from_the_ontology(tmp_path):
    from dismech.stubs.obsolescence import load_obsolescence

    index = load_obsolescence(_fixture_mondo_db(tmp_path))
    assert index is not None
    assert index.version == "2026-05-05"

    merged = index.get("MONDO:0000001")
    assert merged.obsolete and merged.replaced_by == "MONDO:0000002"
    assert "replaced by MONDO:0000002" in merged.describe()

    orphaned = index.get("MONDO:0000003")
    assert orphaned.obsolete and orphaned.replaced_by is None

    scheduled = index.get("MONDO:0000004")
    assert not scheduled.obsolete
    assert scheduled.obsoletion_candidate
    assert scheduled.proposed_replacement == "MONDO:0000005"
    assert "issues/1" in scheduled.obsoletion_note

    # A live term is absent from the mapping, not present and empty — including
    # one carrying an explicit `owl:deprecated false`.
    assert index.get("MONDO:0000006") is None
    assert index.get("MONDO:0000009") is None


def test_obsolescence_query_can_be_restricted_to_the_queue(tmp_path):
    """The census asks about the stub IDs, not all 30,000 MONDO terms."""
    from dismech.stubs.obsolescence import load_obsolescence

    db = _fixture_mondo_db(tmp_path)
    assert set(load_obsolescence(db, ["MONDO:0000003"]).terms) == {"MONDO:0000003"}
    assert load_obsolescence(db, []).terms == {}


def test_obsolescence_degrades_when_mondo_is_absent(tmp_path):
    """`check-stubs` must never require a 1.2 GB download to answer."""
    from dismech.stubs.obsolescence import load_obsolescence

    assert load_obsolescence(tmp_path / "no-such.db") is None


def test_replaced_term_is_repointed_rather_than_swept(tmp_path):
    """A merged term still names an uncurated disease — deleting loses the work.

    `tidy` keys on the finding kind, so the merge case has to be a kind of its
    own rather than a longer `obsolete_term` message, or the sweep would delete
    a stub whose only defect is that its identifier moved.
    """
    from dismech.stubs.cli import REPOINT_KINDS, STALE_KINDS

    (tmp_path / "Merged_Away.yaml").write_text(
        "mondo_id: MONDO:0000001\nlabel: merged away\n"
        "mondo_obsolete: true\nmondo_replaced_by: MONDO:0000002\n",
        encoding="utf-8",
    )
    (tmp_path / "Retired_Outright.yaml").write_text(
        "mondo_id: MONDO:0000003\nlabel: retired outright\nmondo_obsolete: true\n",
        encoding="utf-8",
    )

    found = {
        i.path.name: i for i in check_stubs(tmp_path) if i.kind != "already_curated"
    }
    assert found["Merged_Away.yaml"].kind == "obsolete_term_replaced"
    assert "MONDO:0000002" in found["Merged_Away.yaml"].message
    assert found["Merged_Away.yaml"].kind in REPOINT_KINDS
    assert found["Merged_Away.yaml"].kind not in STALE_KINDS
    assert found["Retired_Outright.yaml"].kind == "obsolete_term"
    assert found["Retired_Outright.yaml"].kind in STALE_KINDS
    for issue in found.values():
        assert issue.severity == "advisory", "staleness never gates"


def test_scheduled_obsoletion_is_reported_while_the_term_is_still_live(tmp_path):
    """The signal that actually catches things, months before deprecation does."""
    (tmp_path / "Phosphoribosylaminoimidazole_Carboxylase_Deficiency.yaml").write_text(
        "mondo_id: MONDO:0859244\n"
        "label: phosphoribosylaminoimidazole carboxylase deficiency\n"
        "mondo_obsoletion_candidate: >-\n"
        "  This term is scheduled to be merged with MONDO:0859003 PAICS deficiency\n",
        encoding="utf-8",
    )
    found = [i for i in check_stubs(tmp_path) if i.kind == "obsoletion_candidate"]
    assert len(found) == 1
    assert found[0].severity == "advisory"
    assert "MONDO:0859003" in found[0].message


def test_the_label_heuristic_survives_as_a_backstop(tmp_path):
    """A stub the enrichment pass has not reached still gets the old signal."""
    (tmp_path / "Obsolete_Thing.yaml").write_text(
        "mondo_id: MONDO:0000009\nlabel: obsolete thing\n", encoding="utf-8"
    )
    kinds = [
        i.kind for i in check_stubs(tmp_path) if i.path.name == "Obsolete_Thing.yaml"
    ]
    assert "obsolete_term" in kinds


def test_ontology_answer_wins_over_the_label(tmp_path):
    """A live term whose label happens to start with the word is not reported."""
    (tmp_path / "Obsolete_Sounding_Disease.yaml").write_text(
        "mondo_id: MONDO:0000009\nlabel: obsolete sounding disease\n"
        "mondo_obsoletion_candidate: scheduled for merge into MONDO:0000010\n",
        encoding="utf-8",
    )
    kinds = {i.kind for i in check_stubs(tmp_path)}
    assert "obsoletion_candidate" in kinds
    assert "obsolete_term" not in kinds, "the ontology already answered"


def test_term_iri_and_curie_forms_both_normalize():
    """`term_replaced_by` is a CURIE in some releases and a full IRI in others."""
    from dismech.stubs.obsolescence import normalize_term

    assert normalize_term("MONDO:0859003") == "MONDO:0859003"
    assert (
        normalize_term("http://purl.obolibrary.org/obo/MONDO_0859003")
        == "MONDO:0859003"
    )
    assert normalize_term(None) == ""

    # `mondo_replaced_by` is pattern-constrained in the schema, so a successor
    # outside MONDO is dropped here rather than written into a stub that then
    # fails `just validate-stubs`.
    for outside in ("DOID:1234", "http://example.org/whatever", "MONDO:12"):
        assert normalize_term(outside) == "", outside


def test_the_replacement_triple_beats_the_scheduled_merge_prose(tmp_path):
    """A scheduled term may carry `IAO:0100001`; the triple is authoritative.

    It is also the case that a term can carry several `rdfs:comment` rows, and
    keeping only one of them can drop the scheduled-obsoletion note entirely.
    """
    import sqlite3

    from dismech.stubs.obsolescence import load_obsolescence

    path = tmp_path / "mondo.db"
    conn = sqlite3.connect(path)
    conn.execute(
        "create table statements "
        "(subject text, predicate text, object text, value text, datatype text)"
    )
    conn.executemany(
        "insert into statements (subject, predicate, object, value) values (?,?,?,?)",
        [
            ("MONDO:0000004", "oio:inSubset", "obo:mondo#obsoletion_candidate", None),
            ("MONDO:0000004", "rdfs:comment", None, "An unrelated editor note."),
            (
                "MONDO:0000004",
                "rdfs:comment",
                None,
                "... and replaced with MONDO:0000009",
            ),
            ("MONDO:0000004", "IAO:0100001", "MONDO:0000005", None),
        ],
    )
    conn.commit()
    conn.close()

    scheduled = load_obsolescence(path).get("MONDO:0000004")
    assert scheduled.proposed_replacement == "MONDO:0000005", (
        "the IAO:0100001 triple should win over the prose"
    )
    # Both comments survive, so the scheduled-merge note is not lost to whichever
    # row the database happened to return last.
    assert "unrelated editor note" in scheduled.obsoletion_note
    assert "MONDO:0000009" in scheduled.obsoletion_note


def test_duplicate_detection_matches_synonyms_not_acronyms():
    """`Wilms tumor 1` must match a curated `Wilms' tumor`; `AIP` must not match."""
    from dismech.stubs.model import is_informative_label, normalize_label

    assert normalize_label("Wilms' tumor") == normalize_label("Wilms tumor")
    assert normalize_label("DeSanto-Shinawi") == normalize_label("Desanto shinawi")
    assert is_informative_label(normalize_label("Wilms tumor")) is True
    for acronym in ("AIP", "Bss", "CRD", "AMC"):
        assert is_informative_label(normalize_label(acronym)) is False


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

_NOW = datetime(2026, 8, 19, tzinfo=UTC)


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


# --- Emitter and loader error paths (PR #8993 review findings 1-4) ------------


@pytest.mark.parametrize(
    "value",
    [
        "a plain label",
        "multi\nline",  # a bare newline made the whole file unparseable
        "22",  # bare, this reads back as int
        "3.5",
        "yes",  # YAML 1.1 boolean
        "null",
        "2026-08-19",  # reads back as a date object
        "tab\there",
        "",
        " leading and trailing ",
        "#hash",
        "a: b",
        " leading space",  # resolves to a *different* string, not a non-string
        "trailing ",
        "a\x00b",  # PyYAML refuses a raw NUL even inside quotes
        "bel\x07",
        "esc\x1bx",
        "vt\x0bx",
        "del\x7fx",
        "nel\x85x",  # a line break PyYAML acts on, and not a control char
        ".inf",
        "NaN",
        "0x1f",
        "1_000",
        "~",
        "1:30",
        "a, b",
        '"quoted"',
        "back\\slash",
    ],
)
def test_emitted_scalars_round_trip_as_the_same_string(value):
    """The emitter's only real guarantee: what goes in comes back out."""
    import yaml

    loaded = yaml.safe_load(_dump({"mondo_id": "MONDO:0000001", "label": value}))
    assert loaded["label"] == value
    assert isinstance(loaded["label"], str)


def test_yaml_scalar_is_shared_with_the_enrichment_script():
    """One emitter, so a fix in it cannot leave a second copy behind."""
    assert yaml_scalar("multi\nline") == '"multi\\nline"'


def test_dump_never_emits_removed_claim_fields():
    """`claimed_by`/`issue` left the schema when claiming moved to GitHub."""
    emitted = _dump(
        {
            "mondo_id": "MONDO:0000001",
            "label": "test",
            "claimed_by": "someone",
            "issue": "42",
            "notes": "kept",
        }
    )
    assert "claimed_by" not in emitted
    assert "issue:" not in emitted
    assert "notes: kept" in emitted


def test_a_malformed_stub_is_reported_not_raised(tmp_path):
    """Anyone can add a stub by PR, so a broken one must not abort the check."""
    (tmp_path / "Good_Stub.yaml").write_text(
        "mondo_id: MONDO:0000001\nlabel: good stub\n", encoding="utf-8"
    )
    (tmp_path / "Broken.yaml").write_text(
        "mondo_id: MONDO:0000002\nlabel: [unclosed\n", encoding="utf-8"
    )
    found = check_stubs(tmp_path, coverage=build_coverage_index([]))
    kinds = {i.kind for i in found}
    assert "unparseable" in kinds
    unparseable = next(i for i in found if i.kind == "unparseable")
    assert unparseable.path.name == "Broken.yaml"
    # One line, so a report of many findings stays readable.
    assert "\n" not in unparseable.format()


def test_a_term_ref_without_a_label_still_validates(stub_validator):
    """A gene outside the HGNC term cache keeps its id rather than being dropped."""
    report = stub_validator.validate(
        {"mondo_id": "MONDO:0000001", "label": "t", "genes": [{"id": "hgnc:99999"}]},
        target_class="CurationStub",
    )
    assert not [r.message for r in report.results]


def test_tidy_survives_a_stub_that_is_stale_twice_over(tmp_path):
    """One stub can be both obsolete and already curated — deleting it twice crashed.

    MONDO retiring a term some time after somebody curated the disease under it
    is exactly what this queue expects to accumulate, and `tidy` is the only
    remedy for staleness, so a crash there left the queue with no sweep at all —
    after deleting an arbitrary prefix of the batch.
    """
    from typer.testing import CliRunner

    from dismech.stubs.cli import app

    stub = tmp_path / "Obsolete_Double_Stale.yaml"
    stub.write_text(
        "mondo_id: MONDO:0004979\nlabel: obsolete double stale\n", encoding="utf-8"
    )

    findings = check_stubs(tmp_path)
    kinds = [i.kind for i in findings if i.path == stub]
    assert "obsolete_term" in kinds and "already_curated" in kinds, (
        f"expected this stub to be stale twice over, got {kinds}"
    )

    result = CliRunner().invoke(app, ["tidy", "--stub-dir", str(tmp_path), "--apply"])
    assert result.exit_code == 0, result.output
    assert not stub.exists()
    assert "Deleted 1 stale stub" in result.output


@pytest.fixture
def next_cli(monkeypatch, coverage):
    """`dismech-stubs next` against the live KB, without re-indexing it per call.

    `next` reuses `check_stubs`, which builds the coverage index. The test
    session's persistent cache starts empty, so the first build there is cold
    (about half a minute on the current corpus). The module-scoped `coverage`
    fixture is the same index, so injecting it keeps the classification real
    and the test fast.
    """
    from typer.testing import CliRunner

    from dismech.stubs import cli

    monkeypatch.setattr(
        cli, "check_stubs", lambda stub_dir: check_stubs(stub_dir, coverage=coverage)
    )

    def invoke(*args):
        result = CliRunner().invoke(cli.app, ["next", *args])
        assert result.exit_code == 0, result.output
        return result.output

    return invoke


def test_next_leaves_out_a_stub_already_curated_as_a_subtype(tmp_path, next_cli):
    """A stub `tidy` would delete must not be offered for claiming (#9415, #11616).

    MONDO:0011346 is bound as a `has_subtypes[].subtype_term` in
    `Hereditary_Xanthinuria.yaml`, so `check` already calls the stub
    `already_curated`. `next` used to hand it out regardless.
    """
    (tmp_path / "Xanthinuria_Type_II.yaml").write_text(
        "mondo_id: MONDO:0011346\nlabel: xanthinuria type II\n", encoding="utf-8"
    )
    (tmp_path / "Uncurated_Disease.yaml").write_text(
        "mondo_id: MONDO:9999901\nlabel: uncurated test disease\n", encoding="utf-8"
    )

    default = next_cli("5", "--stub-dir", str(tmp_path))
    assert "MONDO:0011346" not in default
    assert "MONDO:9999901" in default

    included = next_cli("5", "--stub-dir", str(tmp_path), "--include-stale")
    assert "MONDO:0011346" in included
    assert "already_curated" in included


def test_next_keeps_and_annotates_a_possible_kb_duplicate(tmp_path, next_cli):
    """A name collision is a lump/split question, so the stub stays in the pool.

    It has to be visible in both output paths: `/claim-disease` reads `--json`,
    so a warning printed only in the text output would reach no agent.
    """
    import json

    (tmp_path / "Hereditary_Xanthinuria__MONDO_9999902.yaml").write_text(
        "mondo_id: MONDO:9999902\nlabel: Hereditary Xanthinuria\n", encoding="utf-8"
    )

    text = next_cli("5", "--stub-dir", str(tmp_path))
    assert "MONDO:9999902" in text
    assert "[advisory] possible_kb_duplicate" in text

    rows = json.loads(next_cli("5", "--stub-dir", str(tmp_path), "--json"))
    assert [row["mondo_id"] for row in rows] == ["MONDO:9999902"]
    kinds = [a["kind"] for a in rows[0]["advisories"]]
    assert kinds == ["possible_kb_duplicate"]
    assert "Hereditary_Xanthinuria.yaml" in rows[0]["advisories"][0]["message"]


def test_next_json_carries_the_enrichment_fields_when_present(tmp_path, next_cli):
    """`--json` must carry what the lump/split call turns on (#10180).

    The fields are emitted only when the stub has them. The enrichment omits an
    empty block rather than writing it empty, so absence means "MONDO records
    none", and a `null` would blur that.
    """
    import json

    (tmp_path / "Enriched_Test_Disease.yaml").write_text(
        "mondo_id: MONDO:9999903\n"
        "label: enriched test disease\n"
        "synonyms:\n- ETD\n"
        "mondo_parents:\n- id: MONDO:0002012\n  label: methylmalonic acidemia\n"
        "mondo_descendants:\n- id: MONDO:9999904\n  label: enriched test disease 1\n"
        "mondo_descendant_count: 1\n"
        "genes:\n- id: hgnc:7526\n  label: MMUT\n",
        encoding="utf-8",
    )
    (tmp_path / "Bare_Test_Disease.yaml").write_text(
        "mondo_id: MONDO:9999905\nlabel: bare test disease\n", encoding="utf-8"
    )

    rows = {
        row["mondo_id"]: row
        for row in json.loads(next_cli("5", "--stub-dir", str(tmp_path), "--json"))
    }
    enriched = rows["MONDO:9999903"]
    assert enriched["mondo_parents"] == [
        {"id": "MONDO:0002012", "label": "methylmalonic acidemia"}
    ]
    assert enriched["mondo_descendants"] == [
        {"id": "MONDO:9999904", "label": "enriched test disease 1"}
    ]
    assert enriched["mondo_descendant_count"] == 1
    assert enriched["genes"] == [{"id": "hgnc:7526", "label": "MMUT"}]
    assert enriched["synonyms"] == ["ETD"]

    bare = rows["MONDO:9999905"]
    from dismech.stubs.cli import ENRICHMENT_KEYS

    assert not set(ENRICHMENT_KEYS) & set(bare)
    # The base record is unchanged for both.
    for row in (enriched, bare):
        assert {"mondo_id", "label", "priority", "stub_path", "advisories"} <= set(row)

    text = next_cli("5", "--stub-dir", str(tmp_path))
    assert "enriched test disease  (MONDO descendants: 1)" in text
    assert "bare test disease\n" in text


def test_next_reports_a_missing_claims_file_without_a_traceback(tmp_path):
    """`--json` in the recipe's claims slot used to become a file path (#10180)."""
    from typer.testing import CliRunner

    from dismech.stubs.cli import app

    missing = tmp_path / "no_such_claims.json"
    for args in (
        ["next", "3", "--stub-dir", str(tmp_path), "--claims", str(missing)],
        ["claims", str(missing), "--stub-dir", str(tmp_path)],
    ):
        result = CliRunner().invoke(app, args)
        assert result.exit_code == 2, result.output
        assert not isinstance(result.exception, FileNotFoundError)
        assert "claims file not found" in result.output
        assert "just fetch-claims" in result.output


def _write_successor_fixture(stub_dir: Path) -> None:
    """Stubs for the CARASAL shape (#15853): one disease queued under two IDs.

    - `Merged_Test_Disease` was merged into MONDO:9999911, which has its own stub.
    - `Scheduled_Test_Disease` is scheduled to merge into MONDO:9999913, which
      also has its own stub; the successor comes from MONDO's note.
    - `Orphan_Merge_Test_Disease` was merged into a term nobody has stubbed.
    - `Retiring_Test_Disease` is scheduled with no replacement.
    """
    files = {
        "Merged_Test_Disease.yaml": (
            "mondo_id: MONDO:9999910\nlabel: merged test disease\n"
            "mondo_obsolete: true\nmondo_replaced_by: MONDO:9999911\n"
        ),
        "Successor_Test_Disease.yaml": (
            "mondo_id: MONDO:9999911\nlabel: successor test disease\n"
        ),
        "Scheduled_Test_Disease.yaml": (
            "mondo_id: MONDO:9999912\nlabel: scheduled test disease\n"
            "mondo_obsoletion_candidate: This term is scheduled to be merged with "
            "MONDO:9999913. This ID will therefore be obsoleted and replaced with "
            "MONDO:9999913 https://github.com/monarch-initiative/mondo/issues/1\n"
        ),
        "Scheduled_Successor_Test_Disease.yaml": (
            "mondo_id: MONDO:9999913\nlabel: scheduled successor test disease\n"
        ),
        "Orphan_Merge_Test_Disease.yaml": (
            "mondo_id: MONDO:9999914\nlabel: orphan merge test disease\n"
            "mondo_obsolete: true\nmondo_replaced_by: MONDO:9999915\n"
        ),
        "Retiring_Test_Disease.yaml": (
            "mondo_id: MONDO:9999916\nlabel: retiring test disease\n"
            "mondo_obsoletion_candidate: 'This term is scheduled for obsoletion. "
            "Term to consider: MONDO:9999911'\n"
        ),
    }
    for name, text in files.items():
        (stub_dir / name).write_text(text, encoding="utf-8")


def test_a_stub_whose_successor_is_already_stubbed_is_a_queue_duplicate(
    tmp_path, coverage
):
    """The CARASAL pair (#15853): repointing would only make a duplicate ID.

    Reported on the stub that is leaving, naming the successor, for a merge that
    has happened and for one MONDO has only scheduled. Never an error.
    """
    from dismech.stubs.cli import FOLD_KINDS, REPOINT_KINDS, STALE_KINDS

    _write_successor_fixture(tmp_path)
    findings = check_stubs(tmp_path, coverage=coverage)
    assert not [i for i in findings if i.severity == "error"], findings

    fold = {i.path.name: i for i in findings if i.kind == "successor_already_stubbed"}
    assert set(fold) == {"Merged_Test_Disease.yaml", "Scheduled_Test_Disease.yaml"}
    merged = fold["Merged_Test_Disease.yaml"]
    assert merged.successor == "MONDO:9999911"
    assert "Successor_Test_Disease.yaml" in merged.message
    assert "was merged into" in merged.message
    scheduled = fold["Scheduled_Test_Disease.yaml"]
    assert scheduled.successor == "MONDO:9999913"
    assert "is scheduled to merge into" in scheduled.message
    for issue in fold.values():
        assert issue.severity == "advisory"
        assert issue.kind in FOLD_KINDS
        assert issue.kind not in STALE_KINDS + REPOINT_KINDS

    # The repoint findings carry the successor too, where there is one. A "term
    # to consider" is not a successor.
    successors = {i.path.name: i.successor for i in findings if i.kind in REPOINT_KINDS}
    assert successors == {
        "Merged_Test_Disease.yaml": "MONDO:9999911",
        "Scheduled_Test_Disease.yaml": "MONDO:9999913",
        "Orphan_Merge_Test_Disease.yaml": "MONDO:9999915",
        "Retiring_Test_Disease.yaml": None,
    }


def test_next_names_the_successor_and_keeps_the_stub_in_the_pool(tmp_path, next_cli):
    """A stub leaving its MONDO ID is offered with the live ID beside it (#15853).

    Kept in the pool, because the disease is still uncurated, but a curator
    reading the row sees where the identifier is going before claiming it, in
    the text output and in `--json`, which is what `/claim-disease` reads.
    """
    import json

    _write_successor_fixture(tmp_path)

    text = next_cli("10", "--stub-dir", str(tmp_path))
    for mondo_id in ("MONDO:9999910", "MONDO:9999912", "MONDO:9999914"):
        assert f" {mondo_id}  " in text, f"{mondo_id} left the pool"
    assert "[advisory] obsolete_term_replaced -> MONDO:9999911:" in text
    assert "[advisory] obsoletion_candidate -> MONDO:9999913:" in text
    assert "[advisory] successor_already_stubbed -> MONDO:9999911:" in text
    assert "[advisory] obsolete_term_replaced -> MONDO:9999915:" in text
    assert "[advisory] obsoletion_candidate: MONDO:9999916" in text

    rows = {
        row["mondo_id"]: row
        for row in json.loads(next_cli("10", "--stub-dir", str(tmp_path), "--json"))
    }
    merged = {a["kind"]: a for a in rows["MONDO:9999910"]["advisories"]}
    assert merged["obsolete_term_replaced"]["successor"] == "MONDO:9999911"
    assert merged["successor_already_stubbed"]["successor"] == "MONDO:9999911"
    retiring = rows["MONDO:9999916"]["advisories"]
    assert [a["kind"] for a in retiring] == ["obsoletion_candidate"]
    assert "successor" not in retiring[0], "absent rather than null"
    assert rows["MONDO:9999911"]["advisories"] == []


def test_tidy_lists_a_successor_duplicate_without_deleting_it(tmp_path):
    from typer.testing import CliRunner

    from dismech.stubs.cli import app

    _write_successor_fixture(tmp_path)
    result = CliRunner().invoke(app, ["tidy", "--stub-dir", str(tmp_path), "--apply"])
    assert result.exit_code == 0, result.output
    assert "duplicates a stub for its MONDO successor (2)" in result.output
    # Listed once, under the remedy that applies: repointing would collide.
    assert "needs a repointed `mondo_id`, not deletion (2)" in result.output
    repoint_section = result.output.split("needs a repointed")[1]
    assert "Merged_Test_Disease.yaml" not in repoint_section
    assert "Orphan_Merge_Test_Disease.yaml" in repoint_section
    assert (tmp_path / "Merged_Test_Disease.yaml").exists()
    assert (tmp_path / "Scheduled_Test_Disease.yaml").exists()


# --- fetch-claims: GraphQL first, REST fallback, never an empty file (#15854) --

_REST_ROWS = [
    {
        "number": 15898,
        "title": "Curate CYP7B1-related disorder of oxysterol accumulation (MONDO:1060107)",
        "created_at": "2026-04-01T03:51:23Z",
        "html_url": "https://github.com/monarch-initiative/dismech/issues/15898",
        "assignees": ["caufieldjh"],
    },
]


def _fake_gh(graphql=None, rest=None):
    """A `subprocess.run` stand-in. Each route is (returncode, stdout, stderr)."""
    import subprocess

    calls = []

    def run(args, **kwargs):
        calls.append(args)
        route = graphql if args[1] == "issue" else rest
        assert route is not None, f"unexpected call: {args}"
        code, out, err = route
        return subprocess.CompletedProcess(args, code, out, err)

    run.calls = calls
    return run


_GRAPHQL_403 = (
    1,
    "",
    "non-200 OK status code: 403 Forbidden body: GraphQL is not available",
)
_REST_OK = (0, "\n".join(json.dumps(r) for r in _REST_ROWS) + "\n", "")


def test_fetch_claims_prefers_graphql_and_keeps_linked_pr_data():
    from dismech.stubs.fetch import fetch_claims

    rows = [dict(_GH_ROWS[0], closedByPullRequestsReferences=[])]
    run = _fake_gh(graphql=(0, json.dumps(rows), ""))
    result = fetch_claims(runner=run)
    assert result.route == "graphql" and result.linked_prs_available
    assert result.rows == rows
    assert len(run.calls) == 1


def test_fetch_claims_falls_back_to_rest_when_graphql_is_refused():
    """Claude Code cloud sessions: gh is present, GraphQL answers 403."""
    from dismech.stubs.fetch import fetch_claims

    run = _fake_gh(graphql=_GRAPHQL_403, rest=_REST_OK)
    result = fetch_claims(runner=run)
    assert result.route == "rest" and not result.linked_prs_available
    assert result.rows == _REST_ROWS
    assert "403" in result.notes[0]
    assert run.calls[1][:3] == ["gh", "api", "--paginate"]


def test_fetch_claims_uses_rest_when_graphql_hits_the_limit():
    """`gh issue list --limit N` truncates silently; REST paginates uncapped."""
    from dismech.stubs.fetch import CLAIM_FETCH_LIMIT, fetch_claims

    full = [{"number": i, "title": f"Curate x{i}"} for i in range(CLAIM_FETCH_LIMIT)]
    run = _fake_gh(graphql=(0, json.dumps(full), ""), rest=_REST_OK)
    result = fetch_claims(runner=run)
    assert result.route == "rest"
    assert "truncated" in result.notes[0]


def _invoke_fetch(tmp_path, monkeypatch, run):
    from typer.testing import CliRunner

    import dismech.stubs.fetch as fetch_mod
    from dismech.stubs.cli import app

    monkeypatch.setattr(fetch_mod.subprocess, "run", run)
    monkeypatch.setattr("dismech.stubs.cli.gh_available", lambda: True)
    out = tmp_path / "tmp" / "claims.json"
    return out, CliRunner().invoke(app, ["fetch-claims", "--out", str(out)])


def test_failed_fetch_exits_nonzero_and_leaves_the_file_alone(tmp_path, monkeypatch):
    run = _fake_gh(graphql=_GRAPHQL_403, rest=(1, "", "HTTP 502 Bad Gateway"))
    out, result = _invoke_fetch(tmp_path, monkeypatch, run)
    assert result.exit_code == 1, result.output
    assert not out.exists()
    assert "REST route also failed" in result.output

    # An earlier good file survives a later failed fetch.
    out.parent.mkdir(parents=True)
    out.write_text('[{"title": "Curate x (MONDO:0000001)"}]\n')
    before = out.read_text()
    out, result = _invoke_fetch(tmp_path, monkeypatch, run)
    assert result.exit_code == 1
    assert out.read_text() == before


def test_rest_output_that_is_not_json_is_a_failure(tmp_path, monkeypatch):
    run = _fake_gh(graphql=_GRAPHQL_403, rest=(0, "<html>proxy error</html>\n", ""))
    out, result = _invoke_fetch(tmp_path, monkeypatch, run)
    assert result.exit_code == 1
    assert not out.exists()


def test_successful_rest_fetch_writes_and_says_linked_prs_are_missing(
    tmp_path, monkeypatch
):
    run = _fake_gh(graphql=_GRAPHQL_403, rest=_REST_OK)
    out, result = _invoke_fetch(tmp_path, monkeypatch, run)
    assert result.exit_code == 0, result.output
    assert json.loads(out.read_text()) == _REST_ROWS
    assert "via the REST API" in result.output
    assert "over-report" in result.output
    assert not list(out.parent.glob(".claims.json.*"))  # no temp file left


def test_fetch_claims_without_gh_points_at_the_mcp_fallback(tmp_path, monkeypatch):
    from typer.testing import CliRunner

    from dismech.stubs.cli import app

    monkeypatch.setattr("dismech.stubs.cli.gh_available", lambda: False)
    out = tmp_path / "claims.json"
    result = CliRunner().invoke(app, ["fetch-claims", "--out", str(out)])
    assert result.exit_code == 127
    assert "claim-disease/SKILL.md" in result.output
    assert not out.exists()


def test_an_empty_claims_file_is_rejected_not_read_as_no_claims(tmp_path):
    """A zero-byte file is what a failed `gh ... > file` left (#15854, #11814)."""
    from typer.testing import CliRunner

    from dismech.stubs.cli import app

    empty = tmp_path / "claims.json"
    empty.write_text("")
    for args in (
        ["next", "3", "--stub-dir", str(tmp_path), "--claims", str(empty)],
        ["claims", str(empty), "--stub-dir", str(tmp_path)],
    ):
        result = CliRunner().invoke(app, args)
        assert result.exit_code == 2, result.output
        assert "claims file is empty" in result.output
        assert "just fetch-claims" in result.output


def test_rest_shaped_rows_parse():
    (claim,) = parse_claims(_REST_ROWS)
    assert claim.mondo_id == "MONDO:1060107"
    assert claim.url.endswith("/15898")
    assert claim.created_at == "2026-04-01T03:51:23Z"
    assert claim.assignees == ["caufieldjh"]
    assert claim.linked_pr_known is False
    assert claim.age_days(_NOW) is not None


def test_graphql_rows_know_their_linked_prs():
    (claim,) = parse_claims([dict(_GH_ROWS[0], closedByPullRequestsReferences=[])])
    assert claim.linked_pr_known is True and claim.has_linked_pr is False


def test_check_claims_warns_that_rest_stale_list_may_over_report(tmp_path):
    from typer.testing import CliRunner

    from dismech.stubs.cli import app

    path = tmp_path / "claims.json"
    old = {**_REST_ROWS[0], "created_at": "2020-01-01T00:00:00Z"}
    path.write_text(json.dumps([old]))
    result = CliRunner().invoke(app, ["claims", str(path), "--stub-dir", str(tmp_path)])
    assert result.exit_code == 0, result.output
    assert "stale" in result.output
    assert "linked-PR data is unavailable for 1" in result.output

    # With GraphQL-shaped data the note is absent.
    path.write_text(json.dumps([{**old, "closedByPullRequestsReferences": []}]))
    result = CliRunner().invoke(app, ["claims", str(path), "--stub-dir", str(tmp_path)])
    assert "stale" in result.output
    assert "linked-PR data is unavailable" not in result.output
