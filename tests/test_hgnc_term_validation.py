from __future__ import annotations

import subprocess
import sys
from pathlib import Path

import pytest

ROOT_DIR = Path(__file__).parent.parent
SCHEMA_PATH = ROOT_DIR / "src" / "dismech" / "schema" / "dismech.yaml"
OAK_CONFIG = ROOT_DIR / "conf" / "oak_config.yaml"
DISORDER_FILE = (
    ROOT_DIR / "kb" / "disorders" / "Metaphyseal_Chondrodysplasia_Schmid_Type.yaml"
)


@pytest.mark.skipif(not DISORDER_FILE.exists(), reason="MCDS fixture is missing")
def test_lowercase_hgnc_curies_are_validated(tmp_path: Path) -> None:
    """Regression test for lowercase HGNC prefixes in disorder files."""
    original = DISORDER_FILE.read_text()
    needle = "id: hgnc:2185\n      label: COL10A1"
    replacement = "id: hgnc:2206\n      label: COL10A1"

    assert needle in original, "Expected the canonical COL10A1 HGNC mapping in fixture"

    mutated = original.replace(needle, replacement, 1)
    fixture = tmp_path / DISORDER_FILE.name
    fixture.write_text(mutated)

    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "linkml_term_validator.cli",
            "validate-data",
            str(fixture),
            "-s",
            str(SCHEMA_PATH),
            "-t",
            "Disease",
            "--labels",
            "--no-dynamic-enums",
            "--no-cache",
            "-c",
            str(OAK_CONFIG),
        ],
        cwd=ROOT_DIR,
        capture_output=True,
        text=True,
        check=False,
    )

    output = f"{result.stdout}\n{result.stderr}"
    assert result.returncode != 0, output
    assert "hgnc:2206" in output, output
    assert "COL4A4" in output, output
