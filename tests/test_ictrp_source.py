"""Tests for the WHO ICTRP structured-database source.

All tests run offline against saved ``Trial2.aspx`` fixtures. The contact
values in the fixture are placeholders, not the real investigator details on
the live record — the source drops those fields, so the fixture only needs the
surrounding markup for the drop to be exercised.
"""

from __future__ import annotations

from pathlib import Path

import pytest

from dismech import ictrp_audit
from dismech.structured_sources.ictrp import (
    ICTRPSource,
    TrialNotFound,
    normalize_identifier,
    parse_trial_page,
)

DATA_DIR = Path(__file__).parent / "data" / "ictrp"
CHICTR_PAGE = (DATA_DIR / "chictr2100045397.html").read_text(encoding="utf-8")
NOT_FOUND_PAGE = (DATA_DIR / "not_found.html").read_text(encoding="utf-8")


@pytest.fixture
def record():
    return parse_trial_page(CHICTR_PAGE)


def test_parses_main_identifier_and_register(record):
    assert record.trial_id == "ChiCTR2100045397"
    assert record.register == "ChiCTR"
    assert record.registration_year == "2021"


def test_parses_registration_fields(record):
    assert record.fields["Date of registration"] == "2021-04-14"
    assert record.fields["Primary sponsor"] == (
        "The First Affiliated Hospital of Zhengzhou University"
    )
    assert record.fields["Countries of recruitment"] == "China"


def test_parses_free_text_sections(record):
    assert record.sections["Health condition(s) or problem(s) studied"] == [
        "Movement disorders"
    ]
    criteria = "\n".join(record.sections["Key inclusion & exclusion criteria"])
    assert "Inclusion criteria:" in criteria
    assert "Exclusion criteria:" in criteria
    # A bare "Age minimum:" label line is rejoined with its value.
    assert "Age minimum: 18" in criteria


def test_investigator_contact_data_is_dropped(record):
    """Personal data in the source record must not reach the cache file."""
    body = "\n".join(ICTRPSource(Path("data/ictrp"))._render_body(record))
    for personal in (
        "Contact Name One",
        "contact-one@example.org",
        "+00 0000000001",
        "1 Example Road",
    ):
        assert personal in CHICTR_PAGE, "fixture should contain the contact markup"
        assert personal not in body

    for label in ("Telephone", "Email", "Affiliation", "Contact type"):
        assert f"| {label} |" not in body


def test_absent_record_raises_trial_not_found():
    """The portal serves its 'not found' shell with HTTP 200, so parse detects it."""
    with pytest.raises(TrialNotFound):
        parse_trial_page(NOT_FOUND_PAGE)


def test_serialize_builds_cache_entry(record, monkeypatch):
    source = ICTRPSource(Path("data/ictrp"))
    monkeypatch.setattr(source, "fetch_page", lambda trial_id: CHICTR_PAGE)
    entry = source.serialize("ICTRP:ChiCTR2100045397")

    assert entry.reference_id == "ICTRP:ChiCTR2100045397"
    assert entry.filename() == "ICTRP_ChiCTR2100045397.md"
    assert entry.content_type == "structured_record"
    assert entry.extra_frontmatter["database"] == "WHO ICTRP"

    rendered = entry.render()
    assert rendered.startswith("---\n")
    # Table rows are the quotable unit, so they must survive verbatim.
    assert "| Register | ChiCTR |" in rendered
    assert "| Main ID | ChiCTR2100045397 |" in rendered
    assert (
        "| Primary sponsor | The First Affiliated Hospital of Zhengzhou University |"
        in rendered
    )


def test_serialize_is_deterministic(record, monkeypatch):
    """Two renders of one record are byte-identical (no fetch timestamps)."""
    source = ICTRPSource(Path("data/ictrp"))
    monkeypatch.setattr(source, "fetch_page", lambda trial_id: CHICTR_PAGE)
    assert source.serialize("ChiCTR2100045397").render() == (
        source.serialize("ChiCTR2100045397").render()
    )


@pytest.mark.parametrize(
    "raw,expected",
    [
        ("ICTRP:ChiCTR2100045397", "ChiCTR2100045397"),
        ("ictrp:ISRCTN67795930", "ISRCTN67795930"),
        ("  CTRI/2021/05/033585  ", "CTRI/2021/05/033585"),
        ("JPRN-UMIN000008696", "JPRN-UMIN000008696"),
    ],
)
def test_normalize_identifier(raw, expected):
    assert normalize_identifier(raw) == expected


def test_identifiers_reports_cached_trials(tmp_path):
    """With no bulk file, the cache directory is the source's index."""
    (tmp_path / "ICTRP_ChiCTR2100045397.md").write_text(
        '---\nreference_id: "ICTRP:ChiCTR2100045397"\ncontent_type: "structured_record"\n---\n',
        encoding="utf-8",
    )
    (tmp_path / "PMID_1.md").write_text(
        '---\nreference_id: "PMID:1"\ncontent_type: "abstract_only"\n---\n',
        encoding="utf-8",
    )
    source = ICTRPSource(tmp_path / "data", cache_dir=tmp_path)
    assert list(source.identifiers()) == ["ChiCTR2100045397"]


def test_identifiers_empty_without_cache_dir(tmp_path):
    assert list(ICTRPSource(tmp_path, cache_dir=None).identifiers()) == []


# ----- audit -----


def _write(path: Path, text: str) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    return path


def test_audit_classifies_trial_name_and_stranded(tmp_path):
    kb = tmp_path / "kb"
    _write(
        kb / "disorders" / "Example.yaml",
        "clinical_trials:\n"
        "- name: ChiCTR2100045397\n"
        "  description: >-\n"
        "    A trial.\n"
        "treatments:\n"
        "- name: Something\n"
        "  notes: Registered as ISRCTN67795930, not on ClinicalTrials.gov.\n",
    )
    hits = ictrp_audit.scan(kb, tmp_path / "references_cache")
    placements = {hit.identifier: hit.placement for hit in hits}
    assert placements["ChiCTR2100045397"] == "TRIAL_NAME"
    assert placements["ISRCTN67795930"] == "STRANDED"


def test_audit_marks_cited_when_backed_by_cache(tmp_path):
    kb = tmp_path / "kb"
    cache = tmp_path / "references_cache"
    _write(cache / "ICTRP_ChiCTR2100045397.md", "---\n---\n")
    _write(
        kb / "disorders" / "Example.yaml",
        "clinical_trials:\n"
        "- name: ChiCTR2100045397\n"
        "  evidence:\n"
        "  - reference: ICTRP:ChiCTR2100045397\n",
    )
    hits = ictrp_audit.scan(kb, cache)
    assert {hit.placement for hit in hits} == {"CITED"}


def test_audit_finds_bare_eudract_number_once(tmp_path):
    """A prefixed match must not also be reported by the bare-number pattern."""
    kb = tmp_path / "kb"
    _write(
        kb / "disorders" / "Example.yaml",
        "treatments:\n"
        "- name: A\n"
        "  description: Registered on EudraCT as 2018-004611-50.\n"
        "- name: B\n"
        "  description: See EUCTR2015-005805-35 for details.\n",
    )
    hits = ictrp_audit.scan(kb, tmp_path / "references_cache")
    identifiers = sorted(hit.identifier for hit in hits)
    assert identifiers == ["2018-004611-50", "EUCTR2015-005805-35"]


def test_audit_strict_exit_code(tmp_path, capsys):
    kb = tmp_path / "kb"
    _write(kb / "disorders" / "Example.yaml", "notes: ISRCTN67795930\n")
    code = ictrp_audit.main(
        [
            "--kb-dir",
            str(kb),
            "--cache-dir",
            str(tmp_path / "references_cache"),
            "--strict",
        ]
    )
    assert code == 1
    assert "ISRCTN67795930" in capsys.readouterr().out
