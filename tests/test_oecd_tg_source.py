"""Tests for the OECD Test Guideline structured-database source.

Unlike the other structured sources, this one needs no bulk download: the
paragraph index it renders is committed, so every test here runs offline and
none of them skip.

What these tests are protecting is one claim: **a sentence a curator reads in
the committed paragraph index can be quoted in a KB entry and will verify.**
That is the whole point of the source, and it breaks silently — a body that
reflows, re-wraps or re-encodes a paragraph still looks correct, and only a
reference-validation run over an entry that cites it would catch the drift.
``test_every_indexed_paragraph_is_quotable_from_the_body`` and
``test_every_extracted_quote_verifies_against_the_cache_body`` are that check.
"""

from __future__ import annotations

import json
from pathlib import Path

import pytest
import yaml

from dismech.reference_cache_frontmatter import check_cache_file
from dismech.structured_sources.oecd_tg import (
    PREFIX,
    OECDTestGuidelineSource,
    _normalize_identifier,
    _title_case_section,
)

REPO_ROOT = Path(__file__).parent.parent
OECD_DIR = REPO_ROOT / "data" / "oecd_tg"
MANIFEST = OECD_DIR / "MANIFEST.yaml"
INDEX = OECD_DIR / "tg442d-paragraphs.json"
METHODS = OECD_DIR / "tg442d-methods.json"
CACHE_FILE = REPO_ROOT / "references_cache" / "OECDTG_442D.md"


@pytest.fixture(scope="module")
def source() -> OECDTestGuidelineSource:
    OECDTestGuidelineSource.load_manifest(MANIFEST)
    src = OECDTestGuidelineSource(OECD_DIR)
    src.index()
    return src


@pytest.fixture(scope="module")
def body(source: OECDTestGuidelineSource) -> str:
    return source.serialize(f"{PREFIX}:442D").body


def test_the_identifier_comes_from_the_manifest(source: OECDTestGuidelineSource):
    """`OECD TG 442D` in the manifest becomes the CURIE `OECDTG:442D`."""
    assert list(source.identifiers()) == [f"{PREFIX}:442D"]


def test_every_indexed_paragraph_is_quotable_from_the_body(body: str):
    """The contract this source exists for.

    A curator reads a paragraph in the index and quotes a sentence of it. That
    quote is compared against this body as a substring, so the paragraph text
    has to survive rendering unchanged — not merely be present in some
    normalised form.
    """
    paragraphs = json.loads(INDEX.read_text(encoding="utf-8"))["paragraphs"]
    assert paragraphs, "the committed index is empty"
    missing = [p["citation_key"] for p in paragraphs if p["text"] not in body]
    assert not missing, f"paragraph text altered by rendering: {missing}"


def test_every_extracted_quote_verifies_against_the_cache_body(body: str):
    """The extracted facts become citable, which is the point of the exercise.

    Each quote in ``tg442d-methods.json`` is already checked against the index
    by ``just check-tg-extraction``. This checks the other half: that the same
    quote also verifies against the reference body a KB entry would cite, so a
    curator can move a fact out of the record and into an entry unchanged.
    """
    records = json.loads(METHODS.read_text(encoding="utf-8"))["methods"]
    failures: list[str] = []
    checked = 0
    for record in records:
        for field, value in (record.get("fields") or {}).items():
            if not isinstance(value, dict) or "quote" not in value:
                continue
            checked += 1
            if value["quote"] not in body:
                failures.append(f"{record['method']}/{field}")
    assert checked, "no quoted facts found to check"
    assert not failures, f"quotes that do not verify against the body: {failures}"


def test_the_body_states_its_own_scope_and_keeps_to_it(body: str):
    """The body promises not to carry PROCEDURE, so it must not carry it.

    The licence terms and the cell-line suppliers live in each appendix's
    PROCEDURE section, which the extraction deliberately excludes. A reader who
    trusts the scope note and finds procedural text anyway has been misled
    about what they are allowed to quote.

    Each string below is verbatim in the pinned PDF — the Promega licence in
    Appendix IA's PROCEDURE, the J-TEC tissue supplier in IC's, the JCRB
    deposit in ID's — so the absence being asserted is a real exclusion and
    not a string that happens to appear nowhere in the document.
    """
    assert "PROCEDURE and DATA AND REPORTING sections" in body
    for procedural in (
        "Promega limited use licence",
        "obtained from Japan Tissue Engineering",
        "the α-Sens® cell line from the JCRB Cell",
    ):
        assert procedural not in body, f"out-of-scope text in body: {procedural!r}"


def test_each_paragraph_is_keyed_by_division(body: str):
    """Numbering restarts per appendix, so the division is part of the key."""
    for key in ("### 442D/GI/1", "### 442D/IA/8", "### 442D/IB/8", "### 442D/ID/8"):
        assert key in body, f"missing paragraph heading {key}"
    # IA/8 and IB/8 are different paragraphs; the body must hold both.
    assert "the human AKR1C2 gene" in body
    assert "the rat NQO1 gene" in body


def test_rendering_is_deterministic(source: OECDTestGuidelineSource):
    """Two renders of one index give the same bytes, so a rebuild is a no-op."""
    first = source.serialize(f"{PREFIX}:442D").render()
    second = source.serialize(f"{PREFIX}:442D").render()
    assert first == second


def test_committed_cache_file_matches_a_fresh_render(
    source: OECDTestGuidelineSource,
):
    """The committed cache file is what the current code produces.

    Without this, an edit to the renderer or a re-extraction of the index
    leaves the committed file stale, and a snippet that verifies locally fails
    for whoever rebuilds — the drift the hierarchy-cache check exists for.
    Remedy: `just oecd-tg-rebuild`.
    """
    assert CACHE_FILE.exists(), f"{CACHE_FILE} missing — run `just oecd-tg-rebuild`"
    expected = source.serialize(f"{PREFIX}:442D").render()
    assert CACHE_FILE.read_text(encoding="utf-8") == expected, (
        "references_cache/OECDTG_442D.md is stale; run `just oecd-tg-rebuild`"
    )


def test_cache_entry_matches_the_frontmatter_contract(
    source: OECDTestGuidelineSource, tmp_path: Path
):
    path = source.write_cache_file(f"{PREFIX}:442D", tmp_path)
    assert not check_cache_file(path)


def test_frontmatter_pins_the_pdf_the_text_came_from(
    source: OECDTestGuidelineSource,
):
    """The DOI resolves to the current edition, so the sha256 is the real pin."""
    entry = source.serialize(f"{PREFIX}:442D")
    manifest = yaml.safe_load(MANIFEST.read_text(encoding="utf-8"))
    pinned = manifest["guidelines"][0]["sha256"]
    assert entry.extra_frontmatter["source_sha256"] == pinned
    index_sha = json.loads(INDEX.read_text(encoding="utf-8"))["source"]["sha256"]
    assert index_sha == pinned, (
        "the manifest pin and the index's own recorded sha256 disagree, so the "
        "committed text may not be from the pinned PDF"
    )


@pytest.mark.parametrize(
    "spelling", ["OECDTG:442D", "oecdtg:442d", "442D", "442d", " OECDTG:442D "]
)
def test_identifier_spellings_normalize_to_one_record(spelling: str):
    assert _normalize_identifier(spelling) == f"{PREFIX}:442D"


def test_a_different_prefix_is_refused():
    with pytest.raises(ValueError, match="not an OECDTG: identifier"):
        _normalize_identifier("ORPHA:558")


def test_an_unknown_guideline_raises_and_names_what_is_known(
    source: OECDTestGuidelineSource,
):
    with pytest.raises(KeyError, match="OECDTG:442D"):
        source.serialize("OECDTG:999Z")


def test_a_manifest_id_that_is_not_a_tg_number_is_refused(tmp_path: Path):
    """The CURIE is derived from the manifest id, so the id has to parse."""
    manifest = tmp_path / "MANIFEST.yaml"
    manifest.write_text(
        'guidelines:\n- id: "Some Other Document"\n  index: x.json\n',
        encoding="utf-8",
    )
    OECDTestGuidelineSource.load_manifest(manifest)
    try:
        src = OECDTestGuidelineSource(tmp_path)
        with pytest.raises(ValueError, match="not of the form"):
            src.index()
    finally:
        OECDTestGuidelineSource.load_manifest(MANIFEST)


def test_a_missing_index_names_the_rebuild_command(tmp_path: Path):
    manifest = tmp_path / "MANIFEST.yaml"
    manifest.write_text(
        'guidelines:\n- id: "OECD TG 442D"\n  index: absent-paragraphs.json\n',
        encoding="utf-8",
    )
    OECDTestGuidelineSource.load_manifest(manifest)
    try:
        src = OECDTestGuidelineSource(tmp_path)
        with pytest.raises(FileNotFoundError, match="just extract-oecd-tg"):
            src.index()
    finally:
        OECDTestGuidelineSource.load_manifest(MANIFEST)


def test_all_caps_section_headings_become_running_text():
    assert (
        _title_case_section("INITIAL CONSIDERATIONS, APPLICABILITY AND LIMITATIONS")
        == "Initial Considerations, Applicability and Limitations"
    )
    assert _title_case_section("PRINCIPLE OF THE TEST") == "Principle of the Test"
    # A heading that is already mixed case is left exactly as the guideline set it.
    assert _title_case_section("Principle of the Test") == "Principle of the Test"
    assert _title_case_section("") == ""
