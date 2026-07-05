from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).parent.parent
SCHEMA_PATH = ROOT_DIR / "src" / "dismech" / "schema" / "dismech.yaml"
OAK_CONFIG = ROOT_DIR / "conf" / "oak_config.yaml"


def test_lowercase_hgnc_curies_are_validated(tmp_path: Path) -> None:
    """Regression test for lowercase HGNC prefixes using the committed cache."""
    fixture = tmp_path / "hgnc_label_mismatch.yaml"
    fixture.write_text(
        "\n".join(
            [
                "name: HGNC label mismatch fixture",
                "pathophysiology:",
                "- name: Gene term",
                "  genes:",
                "  - preferred_term: COL10A1",
                "    term:",
                "      id: hgnc:2206",
                "      label: COL10A1",
            ]
        )
    )

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
            "--offline",
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
