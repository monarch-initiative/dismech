"""`just validate-pre-edit` must not block an edit on an ontology outage (#12634).

The pre-edit hook blocks a disorder edit whenever `validate-pre-edit` exits
non-zero. Term validation looks uncached CURIEs up over the network, so an OLS
timeout used to block a schema-valid, correct edit, and agents learned to write
the file from a shell command instead, which skips the hook altogether.

These tests run the real recipe from the real justfile, with a fake ``uv`` on
PATH standing in for every validator, and the real term-validator wrapper in
between. The recipe runs in a scratch working directory so the JSON Schema cache
it writes (``tmp/linkml-validate``) never lands in the checkout.
"""

from __future__ import annotations

import os
import shutil
import stat
import subprocess
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
WRAPPER = ROOT / "scripts" / "run_term_validator.sh"

pytestmark = pytest.mark.skipif(shutil.which("just") is None, reason="needs `just`")

OUTAGE = (
    "\n🌐 Unable to validate at this time: ontology service unavailable.\n"
    "   could not reach ontology service to resolve HP:0000001 (ReadTimeout)"
)


def _fake_uv(tmp_path: Path, *, schema_rc: int, term_output: str, term_rc: int) -> Path:
    """A ``uv`` shim that answers for the three commands the recipe runs."""
    bin_dir = tmp_path / "bin"
    bin_dir.mkdir()
    (tmp_path / "term_output.txt").write_text(term_output)
    shim = bin_dir / "uv"
    shim.write_text(
        "#!/usr/bin/env bash\n"
        'case "$2" in\n'
        "  gen-json-schema) echo '{}' ;;\n"
        f"  linkml-validate) exit {schema_rc} ;;\n"
        f'  linkml-term-validator) cat "{tmp_path / "term_output.txt"}"; exit {term_rc} ;;\n'
        '  *) echo "unexpected uv call: $*" >&2; exit 99 ;;\n'
        "esac\n"
    )
    shim.chmod(shim.stat().st_mode | stat.S_IXUSR)
    return bin_dir


def _run_recipe(
    tmp_path: Path, *, schema_rc: int = 0, term_output: str, term_rc: int
) -> subprocess.CompletedProcess[str]:
    bin_dir = _fake_uv(
        tmp_path, schema_rc=schema_rc, term_output=term_output, term_rc=term_rc
    )
    work = tmp_path / "work"
    work.mkdir()
    # Environment rather than flags, so the recipe's own nested `just` call
    # (`_linkml-validate-config`) resolves the same justfile and directory.
    env = dict(
        os.environ,
        PATH=f"{bin_dir}:{os.environ['PATH']}",
        JUST_JUSTFILE=str(ROOT / "justfile"),
        JUST_WORKING_DIRECTORY=str(work),
    )
    return subprocess.run(
        [
            "just",
            "--set",
            "term_validator",
            str(WRAPPER),
            "--set",
            "ref_validator",
            "true",
            "validate-pre-edit",
            "Some_Disease.yaml",
        ],
        capture_output=True,
        text=True,
        env=env,
        check=False,
    )


def test_ontology_outage_warns_and_lets_the_edit_through(tmp_path: Path) -> None:
    result = _run_recipe(tmp_path, term_output=OUTAGE, term_rc=2)
    output = result.stdout + result.stderr
    assert result.returncode == 0, output
    assert "TERMS NOT CHECKED" in result.stderr
    assert "Pre-edit validation passed" in result.stdout


def test_a_real_term_error_still_blocks(tmp_path: Path) -> None:
    result = _run_recipe(
        tmp_path,
        term_output="❌ ERROR: Label mismatch for 'HP:0000001'",
        term_rc=1,
    )
    assert result.returncode != 0
    assert "TERMS NOT CHECKED" not in result.stderr
    assert "Pre-edit validation passed" not in result.stdout


def test_a_schema_error_still_blocks_even_during_an_outage(tmp_path: Path) -> None:
    result = _run_recipe(tmp_path, schema_rc=1, term_output=OUTAGE, term_rc=2)
    assert result.returncode != 0
    assert "Pre-edit validation passed" not in result.stdout


def test_a_clean_run_passes_without_the_outage_warning(tmp_path: Path) -> None:
    result = _run_recipe(tmp_path, term_output="✅ Validation passed", term_rc=0)
    assert result.returncode == 0, result.stdout + result.stderr
    assert "TERMS NOT CHECKED" not in result.stderr
