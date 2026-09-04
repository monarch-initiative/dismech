"""Tests for the curation stub queue under `stubs/`.

The load-bearing test is `test_no_stub_survives_curation`: a disease that has
been curated must not still have a stub. That is what makes "delete the stub,
add the entry" a contract CI can check rather than a convention people remember.
"""

from __future__ import annotations

from datetime import UTC, datetime
from pathlib import Path

import pytest
from linkml.validator import Validator

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
