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
    the retry logic silently attached to nothing, so assert at least one of the
    known names was really wrapped -- and that the wrapped one is a name this
    version of the validator has.
    """
    import dismech.patch_reference_validator as patch  # noqa: F401  # side-effect: applies the patch
    from linkml_reference_validator.etl.sources.pmid import PMIDSource

    present = [
        name for name in patch.PMID_NETWORK_METHODS if hasattr(PMIDSource, name)
    ]
    assert present, (
        "linkml-reference-validator exposes none of "
        f"{patch.PMID_NETWORK_METHODS}; update PMID_NETWORK_METHODS"
    )
    wrapped = [
        name for name in present if hasattr(getattr(PMIDSource, name), "__wrapped__")
    ]
    assert wrapped == present, f"not wrapped: {sorted(set(present) - set(wrapped))}"


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


def test_fetch_reference_recipe_uses_patched_validator_wrapper():
    """Cache generation must apply the same compatibility patches as validation."""
    recipe = Path("project.justfile").read_text(encoding="utf-8")

    assert 'scripts/run_reference_validator.sh cache reference "$identifier"' in recipe


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
