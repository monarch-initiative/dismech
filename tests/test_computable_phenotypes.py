"""Computable phenotypes: HDR UK / PheKB sources, the HDR UK converter, the
CodeList schema slots, and the code-list checker.

Offline throughout: the HDR UK payloads and the PheKB page are fixtures under
``tests/data/``.
"""

from __future__ import annotations

import doctest
import json
from pathlib import Path

import pytest
import yaml
from linkml.validator import Validator
from linkml.validator.plugins import JsonschemaValidationPlugin
from typer.testing import CliRunner

from dismech import computable_phenotypes
from dismech.cli import app
from dismech.computable_phenotypes import (
    check_document,
    code_in_source,
    definition_from_hdruk,
)
from dismech.structured_sources import hdruk, phekb
from dismech.structured_sources.hdruk import entry_for, parse_record
from dismech.structured_sources.phekb import (
    PhenotypePage,
    is_journal_article,
    parse_page,
)

ROOT = Path(__file__).parent.parent
SCHEMA = ROOT / "src" / "dismech" / "schema" / "dismech.yaml"
DATA = Path(__file__).parent / "data"


@pytest.fixture(scope="module")
def ph304():
    detail = json.loads(
        (DATA / "hdruk" / "PH304.detail.json").read_text(encoding="utf-8")
    )
    codes = json.loads(
        (DATA / "hdruk" / "PH304.codes.json").read_text(encoding="utf-8")
    )
    return parse_record(detail, codes)


@pytest.fixture(scope="module")
def validator() -> Validator:
    return Validator(
        SCHEMA, validation_plugins=[JsonschemaValidationPlugin(closed=True)]
    )


def _errors(validator, disease):
    report = validator.validate(disease, target_class="Disease")
    return [str(r.message) for r in report.results if r.severity.name == "ERROR"]


@pytest.mark.parametrize("module", [hdruk, phekb, computable_phenotypes])
def test_module_doctests(module):
    # testpaths = ["tests"], so pytest never collects src/ doctests itself.
    result = doctest.testmod(module)
    assert result.attempted > 0
    assert result.failed == 0


# ----- HDR UK source -----


def test_hdruk_record_parses_codes_and_drops_personal_fields(ph304):
    assert ph304.phenotype_id == "PH304"
    assert ph304.version_id == 608
    assert ("MONDO:0011382", "sickle cell disease") in ph304.ontology
    icd10 = [c.curie for c in ph304.codes if c.prefix == "ICD10"]
    assert icd10 == ["ICD10:D57.0", "ICD10:D57.1", "ICD10:D57.2", "ICD10:D57.8"]
    body = entry_for(ph304).render()
    assert "ieuan" not in body  # the site username in `owner`


def test_hdruk_cache_body_rows_are_quotable(ph304):
    entry = entry_for(ph304)
    assert entry.filename() == "HDRUK_PH304.md"
    body = entry.body
    assert (
        "| ICD10:D57.0 | Sickle-cell anaemia with crisis | Sickle-cell anaemia - Secondary care - Diagnoses |"
        in body
    )
    assert "| Ontology | MONDO:0011382 sickle cell disease |" in body
    # Medcodes have no dismech code system: kept under the library's own name.
    assert "| 100001.0 (Med codes) |" in body


@pytest.mark.parametrize("bad", ["PH", "XY304", "HDRUK:304"])
def test_hdruk_rejects_non_phenotype_ids(bad):
    with pytest.raises(KeyError):
        hdruk.normalize_identifier(bad)


# ----- PheKB source -----


def test_phekb_page_parses_metadata_files_and_citation():
    page = parse_page((DATA / "phekb" / "615.html").read_text(encoding="utf-8"), "615")
    assert page.title == "Sickle Cell Disease"
    assert page.fields["Authors"] == "Michalik DE, Panepinto JA"
    assert page.fields["Owner Phenotyping Groups"] == "GPC; PCORI CDRN/PPRN"
    assert page.files[0][0] == "Computable Phenotype Description.pdf"
    assert page.pmids == ["27979750"]
    assert page.citation.startswith("Michalik DE, Panepinto JA.")


def test_phekb_body_lists_skipped_articles_without_transcribing_them():
    page = PhenotypePage(
        node_id="1",
        title="T",
        files=[("paper.pdf", "u"), ("algorithm.pdf", "v")],
        attachments={"algorithm.pdf": "282.5 Sickle cell trait"},
        skipped_articles=["paper.pdf"],
    )
    body = phekb.render_body(page)
    assert "- paper.pdf (journal article; cited by PMID, not transcribed)" in body
    assert "## Attachment: algorithm.pdf\n\n282.5 Sickle cell trait" in body
    assert "## Attachment: paper.pdf" not in body


@pytest.mark.parametrize(
    "first_page,expected",
    [
        ("Arthritis Care & Research Vol. 69 DOI 10.1002/acr.22989", True),
        ("doi: https://doi.org/10.1016/j.acap.2016.12.005", True),
        ("Table 1. Summary of Computable Phenotype 282.41", False),
    ],
)
def test_journal_article_detection(first_page, expected):
    assert is_journal_article(first_page) is expected


# ----- converter -----


def test_definition_from_hdruk_validates_against_the_schema(ph304, validator):
    definition = definition_from_hdruk(ph304)
    assert definition["source_reference"] == "HDRUK:PH304"
    items = definition["criteria_sets"][0]["inclusion_criteria"]
    systems = [item["code_lists"][0]["code_system"] for item in items]
    assert systems == ["READ2", "ICD10"]  # medcodes dropped
    assert "Med codes (13 codes)" in definition["notes"]
    assert definition["evidence"][0]["snippet"].startswith("At the specified date")
    disease = {"name": "Sickle Cell Disease", "definitions": [definition]}
    assert _errors(validator, disease) == []


def test_converted_codes_are_found_in_their_own_cache_record(ph304, tmp_path):
    entry = entry_for(ph304)
    (tmp_path / entry.filename()).write_text(entry.render(), encoding="utf-8")
    doc = {"definitions": [definition_from_hdruk(ph304)]}
    assert check_document(doc, Path("x.yaml"), tmp_path, tmp_path) == []


# ----- schema -----


def test_counts_intervals_and_set_logic_validate(validator):
    disease = {
        "name": "Test",
        "definitions": [
            {
                "name": "CP",
                "definition_type": "PHENOTYPE_ALGORITHM",
                "source_reference": "PHEKB:615",
                "criteria_set_logic": "ALL_OF",
                "criteria_sets": [
                    {
                        "name": "Visits",
                        "inclusion_criteria": [
                            {
                                "preferred_term": "Outpatient visits",
                                "minimum_occurrences": 2,
                                "minimum_interval_days": 30,
                            }
                        ],
                    }
                ],
            }
        ],
    }
    assert _errors(validator, disease) == []


@pytest.mark.parametrize(
    "patch",
    [
        {"criteria_set_logic": "SOME_OF"},
        {
            "criteria_sets": [
                {
                    "name": "s",
                    "inclusion_criteria": [
                        {"preferred_term": "x", "minimum_occurrences": 0}
                    ],
                }
            ]
        },
        {
            "criteria_sets": [
                {
                    "name": "s",
                    "inclusion_criteria": [
                        {
                            "preferred_term": "x",
                            "code_lists": [{"code_system": "MEDCODE", "codes": []}],
                        }
                    ],
                }
            ]
        },
    ],
)
def test_invalid_cp_values_are_rejected(validator, patch):
    definition = {"name": "CP", "definition_type": "PHENOTYPE_ALGORITHM", **patch}
    assert _errors(validator, {"name": "Test", "definitions": [definition]})


# ----- checker -----


def _doc(codes, system="ICD10", reference=None):
    code_list = {"code_system": system, "codes": codes}
    if reference:
        code_list["source_reference"] = reference
    return {
        "definitions": [
            {"criteria_sets": [{"inclusion_criteria": [{"code_lists": [code_list]}]}]}
        ]
    }


def _write_cache(tmp_path, reference, body):
    (tmp_path / (reference.replace(":", "_") + ".md")).write_text(
        f'---\nreference_id: "{reference}"\n---\n\n{body}', encoding="utf-8"
    )


@pytest.mark.parametrize(
    "codes,system,problem",
    [
        ([{"id": "ICD10CM:D57.0", "label": "x"}], "ICD10", "prefix does not match"),
        ([{"id": "SNOMEDCT:12ab", "label": "x"}], "SNOMEDCT", "not a well-formed"),
        ([{"id": "ICD9CM:28X4", "label": "x"}], "ICD9CM", "not a well-formed"),
    ],
)
def test_checker_flags_malformed_codes(codes, system, problem, tmp_path):
    findings = check_document(_doc(codes, system), Path("x.yaml"), tmp_path, tmp_path)
    assert [problem in f.problem for f in findings] == [True]


def test_checker_flags_a_label_tidied_away_from_the_source(tmp_path):
    _write_cache(
        tmp_path, "HDRUK:PH1", "| ICD10:D57.0 | Sickle-cell anaemia with crisis | c |\n"
    )
    good = _doc(
        [{"id": "ICD10:D57.0", "label": "Sickle-cell anaemia with crisis"}],
        reference="HDRUK:PH1",
    )
    bad = _doc(
        [{"id": "ICD10:D57.0", "label": "Sickle cell anemia with crisis"}],
        reference="HDRUK:PH1",
    )
    assert check_document(good, Path("x.yaml"), tmp_path, tmp_path) == []
    findings = check_document(bad, Path("x.yaml"), tmp_path, tmp_path)
    assert len(findings) == 1 and "not found in HDRUK:PH1" in findings[0].problem


def test_checker_flags_an_uncached_source(tmp_path):
    findings = check_document(
        _doc([{"id": "ICD10:D57.0", "label": "x"}], reference="HDRUK:PH9"),
        Path("x.yaml"),
        tmp_path,
        tmp_path,
    )
    assert findings[0].problem.startswith("source_reference is not cached")


def test_code_in_source_requires_a_whole_code():
    body = "282.61 HbSS disease without crisis"
    assert not code_in_source("ICD9CM:82.61", "HbSS disease without crisis", body)


# ----- CLI -----


def test_cli_hdruk_definition_offline_writes_fragment_and_cache(tmp_path, monkeypatch):
    monkeypatch.setenv("DISMECH_ROOT", str(tmp_path))
    (tmp_path / "justfile").write_text("", encoding="utf-8")
    (tmp_path / "kb").mkdir()
    result = CliRunner().invoke(
        app,
        [
            "hdruk-definition",
            "PH304",
            "--detail-json",
            str(DATA / "hdruk" / "PH304.detail.json"),
            "--codes-json",
            str(DATA / "hdruk" / "PH304.codes.json"),
        ],
    )
    assert result.exit_code == 0, result.output
    fragment = yaml.safe_load(result.stdout)
    assert fragment["definitions"][0]["source_reference"] == "HDRUK:PH304"
    assert (tmp_path / "references_cache" / "HDRUK_PH304.md").exists()


def test_cli_check_codelists_exit_codes(tmp_path, monkeypatch):
    monkeypatch.setenv("DISMECH_ROOT", str(tmp_path))
    good = tmp_path / "good.yaml"
    bad = tmp_path / "bad.yaml"
    good.write_text(
        yaml.safe_dump(_doc([{"id": "ICD10:D57.0", "label": "x"}])), encoding="utf-8"
    )
    bad.write_text(
        yaml.safe_dump(_doc([{"id": "SNOMED:1", "label": "x"}], "SNOMEDCT")),
        encoding="utf-8",
    )
    runner = CliRunner()
    assert runner.invoke(app, ["check-codelists", str(good)]).exit_code == 0
    result = runner.invoke(app, ["check-codelists", str(bad)])
    assert result.exit_code == 1
    assert "prefix does not match code_system SNOMEDCT" in result.stdout


# ----- bulk import support -----


def test_omitted_code_systems_are_left_out_and_recorded(ph304, tmp_path):
    record = hdruk.omit_code_systems(ph304, {"READ2"})
    assert record.omitted == {"Read codes v2": 13}
    assert not any(c.prefix == "READ2" for c in record.codes)
    body = entry_for(record).body
    assert "READ2:" not in body
    assert "Not cached: 13 Read codes v2." in body
    definition = definition_from_hdruk(record)
    systems = [
        item["code_lists"][0]["code_system"]
        for item in definition["criteria_sets"][0]["inclusion_criteria"]
    ]
    assert systems == ["ICD10"]
    assert "Codes omitted from this transcription" in definition["notes"]
    assert "13 Read codes v2" in definition["notes"]
    (tmp_path / entry_for(record).filename()).write_text(
        entry_for(record).render(), encoding="utf-8"
    )
    doc = {"definitions": [definition]}
    assert check_document(doc, Path("x.yaml"), tmp_path, tmp_path) == []


def test_a_record_with_only_omitted_codes_has_nothing_to_transcribe(ph304):
    record = hdruk.omit_code_systems(ph304, {"READ2", "ICD10"})
    assert computable_phenotypes.transcribable_codes(record) == 0


ENTRY = """\
name: Test Disease
disease_term:
  term:
    id: MONDO:0011382
    label: sickle cell disease
{block}notes: kept   # a comment the loader never sees
"""

EXISTING = """\
definitions:
- name: Older definition
  definition_type: OTHER
"""


@pytest.mark.parametrize("block", ["", EXISTING])
def test_append_definitions_adds_once_and_leaves_the_rest_alone(ph304, tmp_path, block):
    path = tmp_path / "Test_Disease.yaml"
    path.write_text(ENTRY.format(block=block), encoding="utf-8")
    definition = definition_from_hdruk(ph304)
    added = computable_phenotypes.append_definitions(path, [definition])
    assert added == [definition["name"]]
    text = path.read_text(encoding="utf-8")
    assert "notes: kept   # a comment the loader never sees" in text
    doc = yaml.safe_load(text)
    assert doc["definitions"][-1]["source_reference"] == "HDRUK:PH304"
    assert len(doc["definitions"]) == (2 if block else 1)
    assert computable_phenotypes.append_definitions(path, [definition]) == []
    assert path.read_text(encoding="utf-8") == text


def test_cli_hdruk_definition_appends_to_a_disorder(tmp_path, monkeypatch):
    monkeypatch.setenv("DISMECH_ROOT", str(tmp_path))
    (tmp_path / "justfile").write_text("", encoding="utf-8")
    (tmp_path / "kb").mkdir()
    entry = tmp_path / "Test_Disease.yaml"
    entry.write_text(ENTRY.format(block=""), encoding="utf-8")
    args = [
        "hdruk-definition",
        "PH304",
        "--detail-json",
        str(DATA / "hdruk" / "PH304.detail.json"),
        "--codes-json",
        str(DATA / "hdruk" / "PH304.codes.json"),
        "--exclude-code-system",
        "READ2",
        "--disorder",
        str(entry),
    ]
    result = CliRunner().invoke(app, args)
    assert result.exit_code == 0, result.output
    doc = yaml.safe_load(entry.read_text(encoding="utf-8"))
    assert "13 Read codes v2" in doc["definitions"][0]["notes"]
    cache = (tmp_path / "references_cache" / "HDRUK_PH304.md").read_text(
        encoding="utf-8"
    )
    assert "READ2:" not in cache


def test_cli_hdruk_definition_skips_a_record_tagged_for_another_disease(
    tmp_path, monkeypatch
):
    monkeypatch.setenv("DISMECH_ROOT", str(tmp_path))
    (tmp_path / "justfile").write_text("", encoding="utf-8")
    (tmp_path / "kb").mkdir()
    entry = tmp_path / "Other.yaml"
    entry.write_text(
        ENTRY.format(block="").replace("MONDO:0011382", "MONDO:0007915"),
        encoding="utf-8",
    )
    before = entry.read_text(encoding="utf-8")
    result = CliRunner().invoke(
        app,
        [
            "hdruk-definition",
            "PH304",
            "--detail-json",
            str(DATA / "hdruk" / "PH304.detail.json"),
            "--codes-json",
            str(DATA / "hdruk" / "PH304.codes.json"),
            "--disorder",
            str(entry),
        ],
    )
    assert result.exit_code == 0, result.output
    assert "SKIP PH304: HDR UK tags PH304 MONDO:0011382" in result.output
    assert entry.read_text(encoding="utf-8") == before
    assert not (tmp_path / "references_cache" / "HDRUK_PH304.md").exists()


def test_a_label_containing_a_pipe_matches_its_escaped_cache_row():
    body = "| READ2:E1100 | single manic episode-unspecif\\| single manic episode, unspecified | c |"
    label = "single manic episode-unspecif| single manic episode, unspecified"
    assert code_in_source("READ2:E1100", label, body)


def test_malformed_source_codes_are_left_out_and_counted():
    record = hdruk.PhenotypeRecord(
        "PH9",
        1,
        "x",
        codes=[
            hdruk.Code("ICD10 codes", "A15-A19", "Tuberculosis", "c"),
            hdruk.Code("ICD10 codes", "A15.0", "Tuberculosis of lung", "c"),
            hdruk.Code("Read codes v2", "4109NC", "CORONARY INFARCTION", "c"),
        ],
    )
    assert computable_phenotypes.transcribable_codes(record) == 1
    definition = definition_from_hdruk(record)
    lists = [
        item["code_lists"][0]
        for item in definition["criteria_sets"][0]["inclusion_criteria"]
    ]
    assert [c["id"] for cl in lists for c in cl["codes"]] == ["ICD10:A15.0"]
    assert "1 ICD10 codes entries" in definition["notes"]
    assert "(e.g. A15-A19)" in definition["notes"]
    assert "(e.g. 4109NC)" in definition["notes"]


def test_an_all_numeric_read_concept_is_cached_but_not_transcribed():
    record = hdruk.PhenotypeRecord(
        "PH9",
        1,
        "x",
        codes=hdruk.relabel_numeric_read_codes(
            [
                hdruk.Code(
                    "Read codes v2", "11536", "Methylphenidate 20mg", "ADHD prod"
                ),
                hdruk.Code(
                    "Read codes v2", "13212", "Methylphenidate 10mg", "ADHD prod"
                ),
                hdruk.Code("ICD10 codes", "F90.0", "Disturbance of activity", "ADHD"),
            ]
        ),
    )
    assert computable_phenotypes.transcribable_codes(record) == 1
    definition = definition_from_hdruk(record)
    assert "all numeric: CPRD medcodes or product codes" in definition["notes"]
    body = entry_for(record).body
    assert "READ2:11536" not in body
    assert "11536 (Read codes v2 (all numeric" in body
