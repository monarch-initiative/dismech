"""The upstream behaviours dismech's reference gate relies on.

These assertions used to live in ``tests/test_reference_validator_patch.py`` and
tested ``dismech.patch_reference_validator``, a 650-line runtime monkeypatch over
five private ``linkml-reference-validator`` methods. Every defect it worked
around is now fixed upstream, so the patch is gone (dismech#11849) and these
tests target the **behaviour** instead.

Keeping them matters. The patch was the only thing recording that dismech
depends on these; without it a future upstream regression would surface as a
curation mystery -- a body silently missing, a cached title truncated, a trial
re-fetched on every run -- rather than as a red test naming the upstream issue.

Each test names the upstream issue it pins:

============================================  =========================================
Behaviour                                     Upstream
============================================  =========================================
Article body kept when prose says "restricted" linkml/linkml-reference-validator#67
JATS tables extracted as quotable rows         linkml/linkml-reference-validator#68
Bare ``NCT…`` resolves to the cache it writes  linkml/linkml-reference-validator#69
Author containing a colon round-trips          linkml/linkml-reference-validator#70
``---`` inside a title does not truncate       linkml/linkml-reference-validator#71
Ligatures fold in ``normalize_text``           linkml/linkml-reference-validator#73
``split_supporting_text`` is public            linkml/linkml-reference-validator#74
============================================  =========================================

Network retry (linkml/linkml-reference-validator#66) is not covered here: it is a
transport behaviour with nothing deterministic to assert offline.
"""

from __future__ import annotations

import os
import re
import subprocess
from pathlib import Path

import pytest
from linkml_reference_validator.etl.extract.xml import XMLExtractor
from linkml_reference_validator.etl.reference_fetcher import (
    EXTRACTOR_CACHE_VERSION,
    ReferenceFetcher,
)
from linkml_reference_validator.matching import split_supporting_text
from linkml_reference_validator.models import ReferenceValidationConfig
from linkml_reference_validator.validation.supporting_text_validator import (
    SupportingTextValidator,
)


@pytest.fixture
def fetcher(tmp_path: Path) -> ReferenceFetcher:
    return ReferenceFetcher(ReferenceValidationConfig(cache_dir=tmp_path))


# --------------------------------------------------------------------------
# Full-text extraction (#67)
# --------------------------------------------------------------------------


def test_prose_use_of_restricted_does_not_hide_available_body():
    """The ordinary English word in article prose is not a restriction notice.

    PMC5593426 (PMID:28530713) says "IgM-restricted plasma cells" in its results
    and "Searches were restricted to the period from ..." in its methods. A
    whole-document word match discarded 88k characters of real article over
    those two sentences (dismech#10867).
    """
    body = (
        "<p>Mice lacking BACH2 have B cells that differentiate into "
        "IgM-restricted plasma cells.</p>"
        "<p>Searches were restricted to the period from 2007 to 2015.</p>"
        # Padded to article length on purpose: upstream only honours a stub
        # phrase below MAX_STUB_NOTICE_CHARS, so a toy fixture would be
        # discarded for its size rather than kept for its structure, and would
        # pin the wrong behaviour.
        + "<p>" + "Results paragraph. " * 200 + "</p>"
    )
    xml = f"<article><body><sec>{body}</sec></body></article>".encode()

    extracted = XMLExtractor().extract(xml)

    assert extracted is not None
    assert "IgM-restricted plasma cells" in extracted
    assert "Searches were restricted" in extracted


def test_jats_restricted_by_metadata_does_not_hide_available_body():
    """JATS ``restricted-by`` metadata is not evidence that the body is absent."""
    xml = b"""\
    <article>
      <processing-meta><restricted-by>pmc</restricted-by></processing-meta>
      <body><sec><p>Exact full-text evidence remains available.</p></sec></body>
    </article>
    """

    assert XMLExtractor().extract(xml) == "Exact full-text evidence remains available."


def test_a_short_body_using_a_stub_phrase_is_still_discarded():
    """Known, deliberate residual: upstream trades this for safety on stubs.

    The fix is a *length-gated* phrase match, not the structural "has a body"
    test dismech's patch used. Below ``MAX_STUB_NOTICE_CHARS`` a document saying
    "restricted" is still treated as a placeholder, so a genuinely short article
    -- an erratum, a letter -- using that word is discarded. Upstream names this
    case in its own comment and accepts it, because lowering the bound would
    start admitting real stubs.

    Pinned so it reads as a known limit rather than a fresh surprise; if
    upstream ever narrows it, this test is where that shows up.
    """
    xml = (
        b"<article><body><sec><p>Erratum: analysis was restricted to "
        b"imputed variants.</p></sec></body></article>"
    )

    assert XMLExtractor().extract(xml) is None


def test_unavailable_record_shape_remains_unavailable():
    """A genuinely unavailable PMC record is front matter with no ``<body>``.

    This is the shape ``efetch`` returns when PMC will not serve the full text.
    Relaxing the word match must not turn one of these into full text -- that
    direction is the dangerous one, because a curator would be quoting a licence
    notice.
    """
    xml = b"""\
    <article>
      <front><article-meta>
        <permissions><license><license-p>The full text cannot be obtained from PMC.</license-p></license></permissions>
      </article-meta></front>
    </article>
    """

    assert XMLExtractor().extract(xml) is None


# --------------------------------------------------------------------------
# JATS tables (#68)
# --------------------------------------------------------------------------


def test_jats_tables_are_extracted_as_quotable_rows():
    """A clinical Table 1 is often the only place a per-patient finding appears.

    Rows are emitted pipe-delimited so a curator can quote one the same way they
    quote an ORPHA or ICEES row (dismech#10876).
    """
    xml = b"""\
    <article><body>
      <p>Prose paragraph.</p>
      <table-wrap>
        <label>Table 1</label><caption><p>Clinical features</p></caption>
        <table>
          <tr><th>Patient</th><th>1</th><th>2</th></tr>
          <tr><td>Splenomegaly</td><td>Yes</td><td>No</td></tr>
        </table>
      </table-wrap>
    </body></article>
    """

    extracted = XMLExtractor().extract(xml)

    assert extracted is not None
    assert "Prose paragraph." in extracted
    assert "| Splenomegaly | Yes | No |" in extracted


def test_jats_table_is_extracted_exactly_once():
    """Regression: the table must not be appended twice.

    dismech's retired patch called upstream and *then* appended tables itself.
    Once upstream did the same, every re-fetched XML cache got each table
    duplicated -- observed in ``references_cache/PMID_42181267.md`` during the
    upgrade trial, with both of its table headings written twice. This test is
    the tripwire for anyone reintroducing a local table appender.
    """
    xml = b"""\
    <article><body>
      <table-wrap><label>Table 1</label>
        <table><tr><td>Splenomegaly</td><td>Yes</td></tr></table>
      </table-wrap>
    </body></article>
    """

    extracted = XMLExtractor().extract(xml) or ""

    assert extracted.count("Splenomegaly") == 1


# --------------------------------------------------------------------------
# Cache path and frontmatter round-trip (#69, #70, #71)
# --------------------------------------------------------------------------


@pytest.mark.parametrize(
    "reference_id",
    ["NCT12345678", "clinicaltrials:NCT12345678", "CLINICALTRIALS:NCT12345678"],
)
def test_nct_spellings_share_one_cache_path(fetcher, reference_id):
    """Read and write must agree, or the trial is re-fetched on every run.

    A bare ``NCT…`` used to derive ``NCT12345678.md`` on read while the
    ClinicalTrials source wrote ``clinicaltrials_NCT12345678.md`` (dismech#7288).
    """
    assert Path(fetcher.get_cache_path(reference_id)).name == (
        "clinicaltrials_NCT12345678.md"
    )


def test_author_containing_a_colon_round_trips_as_a_string(fetcher):
    """A corporate author with a contact address must not reparse as a mapping.

    Unquoted, ``Consortium. Electronic address: x@y`` loads back as a dict, and
    serialization then raises on it -- including when trying to regenerate the
    damaged record, which re-loads it first.
    """
    document = (
        "---\n"
        "reference_id: PMID:1\n"
        "title: T\n"
        "authors:\n"
        '- "X Consortium. Electronic address: a@b.org"\n'
        "content_type: abstract_only\n"
        "---\n\n## Content\n\nBody.\n"
    )

    reference = fetcher._load_markdown_format(document, "PMID:1")

    assert reference.authors == ["X Consortium. Electronic address: a@b.org"]
    assert all(isinstance(author, str) for author in reference.authors)


@pytest.mark.parametrize(
    "title",
    [
        "Disease---Location, Year",  # MMWR house style
        "A----G(8344) transition",  # pre-1996 NLM ASCII arrow
    ],
)
def test_triple_hyphen_in_a_title_does_not_truncate_the_record(fetcher, title):
    """Frontmatter ends at the ``---`` *line*, not the first ``---`` substring.

    Splitting on the substring loses the title and every field after it, which
    reads as an ordinary incomplete record rather than a parse failure
    (dismech#7697).
    """
    document = (
        "---\n"
        "reference_id: PMID:2\n"
        f'title: "{title}"\n'
        "journal: MMWR\n"
        "year: '1999'\n"
        "content_type: abstract_only\n"
        "---\n\n## Content\n\nBody text.\n"
    )

    reference = fetcher._load_markdown_format(document, "PMID:2")

    assert reference.title == title
    assert reference.journal == "MMWR"
    assert reference.content_type == "abstract_only"


# --------------------------------------------------------------------------
# Snippet matching (#73, #74)
# --------------------------------------------------------------------------


@pytest.mark.parametrize(
    ("ligature", "expansion"),
    [
        ("amyloid ﬁbrils", "amyloid fibrils"),
        ("eﬀect", "effect"),
        ("inﬂammation", "inflammation"),
        ("ﬃnity", "ffinity"),
    ],
)
def test_pdf_ligatures_fold_in_normalize_text(ligature, expansion):
    """PDF extraction emits ``ﬁ`` as one codepoint, so a faithful quote must match.

    ``\\w`` treats U+FB01 as a single word character, so without folding a
    correct transcription can never match its own cached source.
    """
    normalize = SupportingTextValidator.normalize_text

    assert normalize(ligature) == normalize(expansion)


def test_distinct_letters_are_not_folded_to_ascii_digraphs():
    """``Æ``/``Œ`` are letters, not typography, and upstream preserves them.

    dismech's retired local table folded these to ``AE``/``OE``. Upstream
    declines to, because equating them changes scientific terms. No snippet in
    ``kb/`` contains one, so aligning with upstream costs nothing -- this test
    pins the choice so the divergence is not quietly reintroduced.
    """
    normalize = SupportingTextValidator.normalize_text

    assert normalize("Æ") != normalize("AE")
    assert normalize("œ") != normalize("oe")


def test_split_supporting_text_is_importable_and_splits_on_ellipsis():
    """dismech's snippet audit calls this instead of copying the private version.

    The audit reports on what the gate enforces, so the two must never disagree
    about where a ``...`` breaks a quote.
    """
    assert split_supporting_text("protein functions ... in cells") == [
        "protein functions",
        "in cells",
    ]


def test_split_supporting_text_keeps_configured_literal_brackets():
    """Editorial brackets are stripped; configured scientific notation is kept."""
    assert split_supporting_text("protein [important] functions") == [
        "protein functions"
    ]
    assert split_supporting_text("binds [2Fe-2S] cluster", [r"^\d"]) == [
        "binds [2Fe-2S] cluster"
    ]


# --------------------------------------------------------------------------
# Wrapper policy that is dismech's own, not upstream's
# --------------------------------------------------------------------------


def test_reference_validator_wrapper_treats_warning_only_exit_as_advisory(
    tmp_path: Path,
) -> None:
    """Warning-only results stay advisory. This is dismech policy, not a patch.

    It is the one thing ``scripts/run_reference_validator.sh`` still exists to
    do, now that the compatibility patches are gone.
    """
    fake_uv = tmp_path / "uv"
    fake_uv.write_text(
        "#!/usr/bin/env bash\n"
        "printf '%s\\n' '    [WARNING] transient reference fetch failed'\n"
        "exit 1\n",
        encoding="utf-8",
    )
    fake_uv.chmod(0o755)

    env = {**os.environ, "PATH": f"{tmp_path}{os.pathsep}{os.environ['PATH']}"}
    result = subprocess.run(
        ["bash", "scripts/run_reference_validator.sh", "validate", "data", "dummy.yaml"],
        capture_output=True,
        check=False,
        env=env,
        text=True,
    )

    assert result.returncode == 0
    assert "[WARNING] transient reference fetch failed" in result.stdout


def test_every_surviving_monkeypatch_cites_an_upstream_issue():
    """Ten of the twelve patches are retired; each survivor must justify itself.

    The rule (dismech#11849, and the ``dismech-references`` skill) is that a
    patch over the validator's internals is temporary and tracked upstream.
    This is the mechanical half: every class attribute the module replaces must
    be one of the known survivors, and each must name the upstream issue that
    deletes it.

    The budget is not a style preference. Two of the twelve arrived in curation
    PRs while this branch was in review -- one of them fetching full text from
    non-open-access articles by retrying past a browser check -- and neither was
    noticed until a rebase. A thirteenth fails here rather than in a rebase six
    weeks later.

    Survivors, both gaps upstream has not closed:

    * ``_wrap_url_fetch`` -- ``URLSource`` caches the response body verbatim,
      and this repository commits its cache to a public git repository
      (linkml/linkml-reference-validator#92).
    * ``_wrap_jstage_pdf_title`` -- a PDF URL is cached with the URL as its
      title, which is either a blocked title check or a URL copied into the KB
      as the paper's name (linkml/linkml-reference-validator#93).
    """
    module = Path("src/dismech/patch_reference_validator.py")
    source = module.read_text(encoding="utf-8")

    patched = sorted(
        set(re.findall(r"^\s+([A-Z]\w+)\.(\w+) = ", source, re.MULTILINE))
        - {(cls, attr) for cls, attr in re.findall(r"^\s+([A-Z]\w+)\.(\w+) = ", source, re.MULTILINE)
           if attr.endswith("_applied")}
    )
    assert patched == [("URLSource", "fetch")], (
        "retire a patch, or file an upstream issue and add it here. "
        f"Currently patching: {patched}"
    )

    for issue in ("linkml/linkml-reference-validator#92",
                  "linkml/linkml-reference-validator#93"):
        assert issue in source, f"a surviving patch must name {issue}"

    wrappers = set(re.findall(r"^def (_wrap_\w+)\(", source, re.MULTILINE))
    assert wrappers == {"_wrap_url_fetch", "_wrap_jstage_pdf_title"}, (
        f"unexpected patch wrappers, each needs an upstream issue: {sorted(wrappers)}"
    )


def test_retired_patches_are_not_reimported():
    """Nothing may import the retired helpers, which no longer exist."""
    gone = ("dismech.doi_cache_case", "dismech.patch_reference_validator._wrap_")

    def offends(path: Path) -> bool:
        return any(
            any(g in line for g in gone) and not line.lstrip().startswith("#")
            for line in path.read_text(encoding="utf-8").splitlines()
        )

    offenders = [
        path
        for path in (*Path("scripts").rglob("*.py"), *Path("src").rglob("*.py"))
        if path.name != "patch_reference_validator.py" and offends(path)
    ]
    assert not offenders, f"importing retired helpers: {offenders}"


def test_a_refresh_may_not_replace_cached_full_text_with_an_abstract(tmp_path):
    """Upstream #85: a refresh may improve an entry, never demote one.

    Full-text retrieval fails transiently and silently -- a rate-limited PMC
    request answers with a reCAPTCHA interstitial on an HTTP 200 -- so a record
    that really has full text can come back abstract-only. Before #85 that was
    written straight over the cache, destroying what the entry held. dismech
    relies on this: 4,571 of its cache entries are ``full_text_pdf`` alone.

    The refresh is simulated rather than fetched, so this pins
    ``_preserve_cached_full_text`` specifically. Letting the fetch simply fail
    would exercise ``_stale_fallback`` instead -- a different guarantee that
    holds even without #85.
    """
    from linkml_reference_validator.models import ReferenceContent

    cache = tmp_path / "cache"
    cache.mkdir()
    entry = cache / "PMID_15034580.md"
    entry.write_text(
        "---\n"
        "reference_id: PMID:15034580\n"
        f"extractor_version: {EXTRACTOR_CACHE_VERSION}\n"
        "content_type: full_text_pdf\n"
        "---\n\n# T\n\n## Content\n\nFULL TEXT BODY THAT MUST SURVIVE.\n",
        encoding="utf-8",
    )
    fetcher = ReferenceFetcher(
        ReferenceValidationConfig(cache_dir=cache, email="test@example.org")
    )

    abstract_only = ReferenceContent(
        reference_id="PMID:15034580",
        title="A record whose full text did not come back",
        content="Only the abstract this time.",
        content_type="abstract_only",
    )
    preserved = fetcher._preserve_cached_full_text(
        "PMID:15034580", abstract_only, force_refresh=False
    )

    assert preserved is not None, "a refresh losing full text must be refused"
    kept = entry.read_text(encoding="utf-8")
    assert "FULL TEXT BODY THAT MUST SURVIVE." in kept
    assert "content_type: full_text_pdf" in kept
    assert "Only the abstract this time." not in kept


def test_a_lowercased_doi_reuses_its_mixed_case_cache_file(tmp_path):
    """Upstream #87, for dismech#9112 and #11204.

    ``canonical_ref`` lowercases DOIs; the cache lookup must not, or a DOI
    fetched in two capitalizations writes two files. On a case-insensitive
    filesystem those collide and git reports one as permanently modified, which
    is what #11204 was. This used to be ``src/dismech/doi_cache_case.py``.
    """
    cache = tmp_path / "cache"
    cache.mkdir()
    mixed = cache / "DOI_10.1016_S0002-9440(10)63332-9.md"
    mixed.write_text(
        "---\nreference_id: DOI:10.1016/S0002-9440(10)63332-9\n"
        "content_type: abstract_only\n---\n\n## Content\n\nBody.\n",
        encoding="utf-8",
    )
    fetcher = ReferenceFetcher(
        ReferenceValidationConfig(cache_dir=cache, email="test@example.org")
    )
    fetcher.forget_cache_listing()

    resolved = fetcher.get_cache_path("doi:10.1016/s0002-9440(10)63332-9")
    assert resolved == mixed, f"lowercased DOI resolved to {resolved}, not {mixed}"


def test_an_abstract_stored_in_other_abstract_is_read(tmp_path):
    """Upstream #88: PubMed keeps some abstracts outside ``<Abstract>``.

    PIP/KIE/NASA/AIDS abstracts, mostly on pre-1990 records, live in
    ``OtherAbstract``. Reading only ``Abstract`` reported no content for them,
    and a refresh then deleted the abstract the cache already held -- 967 and
    1175 characters lost from two references cited in ``kb/``.
    """
    from bs4 import BeautifulSoup
    from linkml_reference_validator.etl.sources.pmid import PMIDSource

    soup = BeautifulSoup(
        '<OtherAbstract Type="PIP" Language="eng">'
        "<AbstractText>Glucose absorption raises sodium uptake.</AbstractText>"
        "</OtherAbstract>",
        "xml",
    )
    assert (
        PMIDSource()._parse_abstract(soup) == "Glucose absorption raises sodium uptake."
    )
