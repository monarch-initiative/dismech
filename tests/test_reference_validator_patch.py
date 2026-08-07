"""Tests for local linkml-reference-validator compatibility patches."""

import os
import subprocess
from pathlib import Path

from linkml_reference_validator.etl.reference_fetcher import ReferenceFetcher
from linkml_reference_validator.models import ReferenceValidationConfig


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
            fetcher.get_cache_path(reference_id).name
            == "clinicaltrials_NCT06087757.md"
        ), reference_id


def test_bare_nct_patch_leaves_other_bare_identifiers_alone(tmp_path):
    """The bare-NCT rule must not capture unrelated prefixless identifiers."""
    import dismech.patch_reference_validator  # noqa: F401  # side-effect: applies the cache-path patch

    fetcher = ReferenceFetcher(ReferenceValidationConfig(cache_dir=tmp_path))

    for reference_id in ("NCTNOTANID", "12345678", "PMID:12345678"):
        assert "clinicaltrials_NCTNOTANID" not in fetcher.get_cache_path(
            reference_id
        ).name, reference_id


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
