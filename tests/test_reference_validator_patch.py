"""Tests for local linkml-reference-validator compatibility patches."""

import os
import subprocess
from pathlib import Path

from linkml_reference_validator.etl.extract.xml import XMLExtractor
from linkml_reference_validator.etl.reference_fetcher import ReferenceFetcher
from linkml_reference_validator.models import ReferenceValidationConfig


def test_pmid_network_methods_are_actually_wrapped():
    """The network-resilience patch must find something to wrap.

    ``apply_patch`` skips PMIDSource methods that no longer exist so an upstream
    rename cannot crash every consumer at import time (0.2.1 split
    ``_fetch_abstract`` into ``_fetch_pubmed_xml`` + ``_parse_abstract``, which
    did exactly that). The cost of that tolerance is that a rename could leave
    the retry logic silently attached to nothing, so assert the wrapping really
    happened -- via our own marker, not ``__wrapped__``, which ``functools.wraps``
    would also set if upstream started decorating these itself.
    """
    from linkml_reference_validator.etl.sources.pmid import PMIDSource

    import dismech.patch_reference_validator as patch

    present = [name for name in patch.PMID_NETWORK_METHODS if hasattr(PMIDSource, name)]
    unwrapped = [
        name
        for name in present
        if not getattr(getattr(PMIDSource, name), "_dismech_network_retry", False)
    ]
    assert not unwrapped, f"not wrapped by dismech: {unwrapped}"

    # Exactly one spelling of the PubMed fetch must be wrapped: none means the
    # retry logic is attached to nothing, both means the retries nest.
    fetch_wrapped = [
        name
        for name in patch.PMID_FETCH_ALTERNATIVES
        if getattr(getattr(PMIDSource, name, None), "_dismech_network_retry", False)
    ]
    assert len(fetch_wrapped) == 1, (
        f"expected exactly one of {patch.PMID_FETCH_ALTERNATIVES} to be wrapped, "
        f"got {fetch_wrapped}"
    )


def test_save_to_disk_patch_forwards_unknown_keyword_arguments():
    """The author-coercion wrapper must not pin upstream's signature.

    It originally declared ``(self, reference)``. linkml-reference-validator
    0.2.1 calls ``self._save_to_disk(content, private=...)`` from
    ``_save_by_access``, so every patched fetch of an **uncached** reference
    died with "unexpected keyword argument 'private'" -- meaning
    ``just validate-disorders`` on any entry citing something not already in
    references_cache/. Cached-only runs never touched the path, so it stayed
    invisible.

    Asserting on ``private`` specifically would just re-pin the signature one
    release later, so this checks the general property: arbitrary extra
    arguments reach the original.
    """
    from dismech.patch_reference_validator import _wrap_save_to_disk

    seen = {}

    class _Reference:
        def __init__(self):
            self.authors = ["Doe J"]

    def _original(self, reference, *args, **kwargs):
        seen["args"] = args
        seen["kwargs"] = kwargs

    # Wrap a stand-in original, so the assertion is about the wrapper's
    # forwarding rather than about whatever upstream's parameters happen to be
    # this release -- which is the whole point.
    _wrap_save_to_disk(_original)(None, _Reference(), True, private=True, future_arg="x")

    assert seen["args"] == (True,)
    assert seen["kwargs"] == {"private": True, "future_arg": "x"}


def test_save_to_disk_patch_survives_a_real_uncached_fetch(tmp_path, monkeypatch):
    """End-to-end guard for the same bug, against upstream's real call site.

    The forwarding test above uses a stand-in original, so it would still pass if
    upstream started calling ``_save_to_disk`` in some way the wrapper cannot
    accept at all. This drives the actual ``_save_by_access`` -> ``_save_to_disk``
    path with a stubbed network fetch, which is where ``private=`` is passed
    from, and is the exact shape of the crash.
    """
    from linkml_reference_validator.etl.reference_fetcher import ReferenceFetcher
    from linkml_reference_validator.models import ReferenceValidationConfig

    import dismech.patch_reference_validator  # noqa: F401  # side-effect: applies the patch

    fetcher = ReferenceFetcher(ReferenceValidationConfig(cache_dir=tmp_path))

    class _Content:
        reference_id = "PMID:14991055"
        title = "A real paper"
        journal = "Nat Genet"
        year = "2004"
        doi = None
        abstract = "Body text."
        full_text = None
        full_text_access_type = "open"

        def __init__(self):
            self.authors = ["Krakow D"]

        def __getattr__(self, _name):  # tolerate fields this stub omits
            return None

    monkeypatch.setattr(
        type(fetcher), "_materialize", lambda self, *a, **kw: _Content(), raising=False
    )
    fetcher._save_by_access(_Content())

    assert (tmp_path / "PMID_14991055.md").is_file()


def test_clinicaltrials_cache_path_uses_repo_lowercase_naming(tmp_path):
    import dismech.patch_reference_validator  # noqa: F401  # side-effect: applies the cache-path patch

    fetcher = ReferenceFetcher(ReferenceValidationConfig(cache_dir=tmp_path))

    cache_path = fetcher.get_cache_path("CLINICALTRIALS:NCT00004645")

    assert cache_path.name == "clinicaltrials_NCT00004645.md"


def test_bare_nct_reference_resolves_to_clinicaltrials_cache_path(tmp_path):
    """A prefixless ``NCT…`` id must read from the file the fetch writes.

    Upstream ``_parse_reference_id`` has no bare-NCT rule, so the lookup derived
    ``NCT….md`` while the fetched record was saved as ``clinicaltrials_NCT….md``
    -- a permanent cache miss that re-fetched from ClinicalTrials.gov on every
    validation run (dismech#7288).
    """
    import dismech.patch_reference_validator  # noqa: F401  # side-effect: applies the cache-path patch

    fetcher = ReferenceFetcher(ReferenceValidationConfig(cache_dir=tmp_path))

    for reference_id in ("NCT06087757", "nct06087757"):
        assert (
            fetcher.get_cache_path(reference_id).name == "clinicaltrials_NCT06087757.md"
        ), reference_id


def test_bare_nct_patch_leaves_other_bare_identifiers_alone(tmp_path):
    """The bare-NCT rule must not capture unrelated prefixless identifiers."""
    import dismech.patch_reference_validator  # noqa: F401  # side-effect: applies the cache-path patch

    fetcher = ReferenceFetcher(ReferenceValidationConfig(cache_dir=tmp_path))

    for reference_id in ("NCTNOTANID", "12345678", "PMID:12345678"):
        assert (
            "clinicaltrials_NCTNOTANID" not in fetcher.get_cache_path(reference_id).name
        ), reference_id


def test_pmc_restricted_by_metadata_does_not_hide_available_body():
    """JATS ``restricted-by`` metadata is not evidence that the body is absent."""
    import dismech.patch_reference_validator  # noqa: F401  # applies XML patch

    xml = b"""\
    <article>
      <processing-meta><restricted-by>pmc</restricted-by></processing-meta>
      <body><sec><p>Exact full-text evidence remains available.</p></sec></body>
    </article>
    """

    assert XMLExtractor().extract(xml) == "Exact full-text evidence remains available."


def test_pmc_restricted_record_without_body_remains_unavailable():
    """The compatibility patch must not manufacture text for an absent body."""
    import dismech.patch_reference_validator  # noqa: F401  # applies XML patch

    xml = b"<article><restricted-by>pmc</restricted-by></article>"

    assert XMLExtractor().extract(xml) is None


def test_prose_use_of_restricted_does_not_hide_available_body():
    """The ordinary English word in article prose is not a restriction notice.

    PMC5593426 (PMID:28530713) carries no ``restricted-by`` metadata at all -- it
    says "IgM-restricted plasma cells" in the results and "Searches were
    restricted to the period from ..." in the methods. Upstream's whole-document
    word match discarded the entire body over those two sentences (issue #10867).
    """
    import dismech.patch_reference_validator  # noqa: F401  # applies XML patch

    xml = b"""\
    <article>
      <body><sec>
        <p>Mice lacking BACH2 have B cells that differentiate into IgM-restricted plasma cells.</p>
        <p>Searches were restricted to the period from 2007 to 2015.</p>
      </sec></body>
    </article>
    """

    extracted = XMLExtractor().extract(xml)

    assert extracted is not None
    assert "IgM-restricted plasma cells" in extracted
    assert "Searches were restricted" in extracted


def test_pmc_unavailable_record_shape_remains_unavailable():
    """A genuinely unavailable PMC record is front matter with no ``<body>``.

    This is the shape ``efetch`` actually returns when PMC will not serve the
    full text: the trigger phrase sits in the front matter and there is no body
    element. Dropping the word match must not turn one of these into full text.
    """
    import dismech.patch_reference_validator  # noqa: F401  # applies XML patch

    xml = b"""\
    <article>
      <front><article-meta>
        <permissions><license><license-p>The full text cannot be obtained from PMC.</license-p></license></permissions>
      </article-meta></front>
    </article>
    """

    assert XMLExtractor().extract(xml) is None


def test_fetch_reference_recipe_uses_patched_validator_wrapper():
    """Cache generation must apply the same compatibility patches as validation."""
    recipe = Path("project.justfile").read_text(encoding="utf-8")

    assert 'scripts/run_reference_validator.sh cache reference "$identifier"' in recipe


def test_deep_research_recipes_use_the_patched_client_wrapper():
    """deep-research-client validates references, so it needs the patches too.

    Since 0.2.9 it calls linkml-reference-validator in-process, which makes every
    research recipe a path that reads and writes references_cache/. Calling
    `uv run deep-research-client` directly would skip the #7697 delimiter-aware
    frontmatter read, and a truncated read surfaces as a false "unresolved
    reference" -- which curators are told to act on by dropping the claim.

    Every invocation goes through the wrapper, with no exemption for the
    subcommands that happen not to validate today (`providers`,
    `edison-trajectory`): "which subcommands touch the cache" is a fact about
    upstream that changed once already, in 0.2.9, and a rule with no exceptions
    is the one that survives the next change.
    """
    recipe = Path("project.justfile").read_text(encoding="utf-8")

    unwrapped = [
        line.strip()
        for line in recipe.splitlines()
        if "uv run deep-research-client" in line and not line.lstrip().startswith("#")
    ]
    assert not unwrapped, (
        "these call deep-research-client without dismech's validator patches; "
        f"route them through {{{{dr_client}}}}: {unwrapped}"
    )
    assert 'dr_client := "scripts/run_deep_research_client.sh"' in recipe


def test_reference_validator_wrapper_treats_warning_only_exit_as_advisory(
    tmp_path: Path,
) -> None:
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
        [
            "bash",
            "scripts/run_reference_validator.sh",
            "validate",
            "data",
            "dummy.yaml",
        ],
        capture_output=True,
        check=False,
        env=env,
        text=True,
    )

    assert result.returncode == 0
    assert "[WARNING] transient reference fetch failed" in result.stdout


def test_jats_tables_are_appended_as_quotable_rows():
    """A clinical report's Table 1 must reach the cache, not just its paragraphs.

    Upstream keeps ``<body>`` paragraphs only. In PMID:28530713 that dropped the
    one place the founding report records immunoglobulin replacement and the
    per-subject isotype pattern (issue #10867). NIHMS-converted JATS puts tables
    in a trailing ``<floats-group>``, outside ``<body>``, so they are located
    across the whole document.
    """
    import dismech.patch_reference_validator  # noqa: F401  # applies XML patch

    xml = b"""\
    <article>
      <body><sec><p>Affected subjects had lymphocyte-maturation defects.</p></sec></body>
      <floats-group>
        <table-wrap>
          <label>Table 1</label><caption><p>Summary clinical characteristics.</p></caption>
          <table>
            <tr><th>Patients</th><th>A.II.1</th><th>B.III.2</th></tr>
            <tr><td>IgA</td><td>Low</td><td>Low</td></tr>
            <tr><td></td><td></td><td></td></tr>
            <tr><td>On IvIg treatment</td><td>Yes</td><td>No</td></tr>
          </table>
        </table-wrap>
      </floats-group>
    </article>
    """

    extracted = XMLExtractor().extract(xml)

    assert "Affected subjects had lymphocyte-maturation defects." in extracted
    assert "## Table 1 Summary clinical characteristics." in extracted
    assert "| On IvIg treatment | Yes | No |" in extracted
    # An all-empty row carries nothing quotable and is dropped.
    assert "|  |  |  |" not in extracted


def test_oversized_jats_table_is_not_appended():
    """A data dump is not a quotable clinical table and must not bloat the cache."""
    import dismech.patch_reference_validator  # noqa: F401  # applies XML patch

    rows = "".join(f"<tr><td>probe{n}</td><td>{n}</td></tr>" for n in range(500))
    xml = (
        "<article><body><sec><p>Body paragraph.</p></sec></body>"
        f"<floats-group><table-wrap><label>Table S1</label><table>{rows}</table>"
        "</table-wrap></floats-group></article>"
    ).encode("utf-8")

    extracted = XMLExtractor().extract(xml)

    assert extracted == "Body paragraph."


def test_article_without_tables_is_unchanged():
    """The table pass must be a no-op for an article that carries none."""
    import dismech.patch_reference_validator  # noqa: F401  # applies XML patch

    xml = b"<article><body><sec><p>Body paragraph.</p></sec></body></article>"

    assert XMLExtractor().extract(xml) == "Body paragraph."
