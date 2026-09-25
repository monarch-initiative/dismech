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
import re
import shutil
import stat
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
WRAPPER = ROOT / "scripts" / "run_term_validator.sh"
CLASSIFIER = ROOT / "scripts" / "classify_offline_term_results.py"

pytestmark = pytest.mark.skipif(shutil.which("just") is None, reason="needs `just`")

OUTAGE = (
    "\n🌐 Unable to validate at this time: ontology service unavailable.\n"
    "   could not reach ontology service to resolve HP:0000001 (ReadTimeout)"
)


# Real linkml-term-validator 0.4.5 `--offline` output, trimmed to the result
# blocks: one uncached CURIE, reported both ways it can be.
OFFLINE_UNCACHED = """
❌ Validation failed with 2 issue(s):

  ❌ ERROR: Cannot validate 'HP:9999998' against dynamic enum 'PhenotypeTerm' offline: enum closure not materialized in cache (materialize it online first with --saturate-enum-caches or --cache-strategy greedy, then re-run offline)
      path: phenotypes[1].phenotype_term.term
      slot: term
      field: id
      validation: offline (enum cache not materialized)
  ❌ ERROR: Term 'HP:9999998' not found in offline cache
      path: phenotypes[1].phenotype_term.term
      slot: term
      field: id
      prefix: HP (offline: cache-only)
"""

# A wrong label on a cached CURIE: a real error the offline run can see.
OFFLINE_CACHED_LABEL_MISMATCH = """
❌ Validation failed with 1 issue(s):

  ⚠️  WARN: Label mismatch for 'HP:0030828': expected 'Wheezing', got 'Wheezingz'
      path: phenotypes[0].phenotype_term.term
      slot: term
      label_field: label
      curie: HP:0030828
"""


def _fake_uv(
    tmp_path: Path,
    *,
    schema_rc: int,
    term_output: str,
    term_rc: int,
    offline_output: str,
    offline_rc: int,
) -> Path:
    """A ``uv`` shim that answers for the commands the recipe runs.

    Term validation answers with ``term_output`` online and ``offline_output``
    when ``--offline`` is passed. ``uv run python`` runs the real interpreter,
    so the recipe's classifier script is exercised for real.
    """
    bin_dir = tmp_path / "bin"
    bin_dir.mkdir()
    (tmp_path / "term_output.txt").write_text(term_output)
    (tmp_path / "offline_output.txt").write_text(offline_output)
    shim = bin_dir / "uv"
    shim.write_text(
        "#!/usr/bin/env bash\n"
        'case "$2" in\n'
        "  gen-json-schema) echo '{}' ;;\n"
        f"  linkml-validate) exit {schema_rc} ;;\n"
        "  linkml-term-validator)\n"
        '    if [[ " $* " == *" --offline "* ]]; then\n'
        f'      cat "{tmp_path / "offline_output.txt"}"; exit {offline_rc}\n'
        "    fi\n"
        f'    cat "{tmp_path / "term_output.txt"}"; exit {term_rc} ;;\n'
        f'  python) shift 2; exec "{sys.executable}" "$@" ;;\n'
        '  *) echo "unexpected uv call: $*" >&2; exit 99 ;;\n'
        "esac\n"
    )
    shim.chmod(shim.stat().st_mode | stat.S_IXUSR)
    return bin_dir


def _run_recipe(
    tmp_path: Path,
    *,
    schema_rc: int = 0,
    term_output: str,
    term_rc: int,
    offline_output: str = "✅ Validation passed",
    offline_rc: int = 0,
) -> subprocess.CompletedProcess[str]:
    bin_dir = _fake_uv(
        tmp_path,
        schema_rc=schema_rc,
        term_output=term_output,
        term_rc=term_rc,
        offline_output=offline_output,
        offline_rc=offline_rc,
    )
    work = tmp_path / "work"
    work.mkdir()
    # The classifier is called by a path relative to the checkout.
    (work / "scripts").mkdir()
    (work / "scripts" / CLASSIFIER.name).symlink_to(CLASSIFIER)
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


def test_outage_rechecks_cached_terms_and_lists_the_rest(tmp_path: Path) -> None:
    """Terms the cache cannot answer for are named, not silently skipped (#12658)."""
    result = _run_recipe(
        tmp_path,
        term_output=OUTAGE,
        term_rc=2,
        offline_output=OFFLINE_UNCACHED,
        offline_rc=1,
    )
    assert result.returncode == 0, result.stdout + result.stderr
    assert "TERMS NOT CHECKED" in result.stderr
    assert (
        "not checked: HP:9999998 at phenotypes[1].phenotype_term.term" in result.stderr
    )
    assert "Pre-edit validation passed" in result.stdout


def test_outage_still_blocks_a_wrong_label_on_a_cached_term(tmp_path: Path) -> None:
    """The case #12658 was filed for: an outage used to let this through."""
    result = _run_recipe(
        tmp_path,
        term_output=OUTAGE,
        term_rc=2,
        offline_output=OFFLINE_CACHED_LABEL_MISMATCH + OFFLINE_UNCACHED,
        offline_rc=1,
    )
    assert result.returncode != 0
    assert "Label mismatch for 'HP:0030828'" in result.stderr
    assert "Pre-edit validation passed" not in result.stdout


def test_unreadable_offline_output_falls_back_to_the_warning(tmp_path: Path) -> None:
    """A classifier that cannot parse the recheck must not start blocking edits."""
    result = _run_recipe(
        tmp_path,
        term_output=OUTAGE,
        term_rc=2,
        offline_output="Traceback (most recent call last):\n  boom",
        offline_rc=1,
    )
    assert result.returncode == 0, result.stdout + result.stderr
    assert "not checked: all terms" in result.stderr


def test_recipe_and_wrapper_agree_on_the_outage_exit_code() -> None:
    """The wrapper's constant and the recipe's literal must stay in step."""
    wrapper = WRAPPER.read_text()
    match = re.search(r"^EXIT_SERVICE_UNAVAILABLE=(\d+)$", wrapper, re.MULTILINE)
    assert match, "wrapper no longer defines EXIT_SERVICE_UNAVAILABLE"
    recipe = subprocess.run(
        ["just", "--justfile", str(ROOT / "justfile"), "--show", "validate-pre-edit"],
        capture_output=True,
        text=True,
        check=True,
    ).stdout
    assert f'"$term_rc" -eq {match.group(1)} ]' in recipe
