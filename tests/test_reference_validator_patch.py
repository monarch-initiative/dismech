"""Tests for local linkml-reference-validator compatibility patches."""

import os
import subprocess
from pathlib import Path

from linkml_reference_validator.etl.reference_fetcher import ReferenceFetcher
from linkml_reference_validator.models import ReferenceValidationConfig


def test_clinicaltrials_cache_path_uses_repo_lowercase_naming(tmp_path):
    import dismech.patch_reference_validator  # noqa: F401

    fetcher = ReferenceFetcher(ReferenceValidationConfig(cache_dir=tmp_path))

    cache_path = fetcher.get_cache_path("CLINICALTRIALS:NCT00004645")

    assert cache_path.name == "clinicaltrials_NCT00004645.md"


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
