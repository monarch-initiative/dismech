"""`just fetch-reference` must regenerate structured-source records, not hand them to LRV.

AGENTS.md tells every agent to regenerate any ``references_cache/`` file with
``just fetch-reference <ID>``. For a ``CGGV:`` (or ``ORPHA:``, ``CGDS:``,
``ICEES:``, ``NCIT:``) id that used to fall through to
``linkml-reference-validator cache reference``, which has no source for those
prefixes and fails with "No source found" (dismech#13575). The recipe routes
them to the structured-source rebuild instead; this pins that routing.
"""

from __future__ import annotations

import re
import subprocess
import textwrap
from pathlib import Path

import pytest

JUSTFILE = Path(__file__).resolve().parents[1] / "project.justfile"


def _fetch_reference_recipe() -> str:
    text = JUSTFILE.read_text(encoding="utf-8")
    match = re.search(
        r"^fetch-reference \+identifiers:\n(.*?)(?=^\S)", text, re.DOTALL | re.MULTILINE
    )
    assert match, "fetch-reference recipe not found in project.justfile"
    return match.group(1)


@pytest.mark.parametrize(
    ("prefix", "source"),
    [
        ("CGGV", "clingen"),
        ("CGDS", "clingen-dosage"),
        ("ORPHA", "orphanet"),
        ("ICEES", "icees"),
        ("NCIT", "ncit"),
    ],
)
def test_fetch_reference_routes_structured_prefix_to_its_rebuild(
    prefix: str, source: str
):
    recipe = _fetch_reference_recipe()
    # A `case` arm naming the prefix...
    arm = re.search(
        rf"^\s*{prefix}:\*[^)]*\)\n(.*?)^\s*;;", recipe, re.DOTALL | re.MULTILINE
    )
    assert arm, f"no case arm for {prefix}:* in fetch-reference"
    # ...whose body rebuilds through the structured-source CLI for that source.
    assert f"structured_sources.cli rebuild {source} --id" in arm.group(1)


def test_fetch_reference_has_no_lowercase_structured_arms():
    """The serializers accept `CGGV:`/`ORPHA:`/... (and `Orphanet:`), never
    lowercase prefixes, so a lowercase arm can only route an id into a
    KeyError (review on #13766)."""
    recipe = _fetch_reference_recipe()
    arms = re.findall(r"^\s*([A-Za-z_|:*]+)\)\n", recipe, re.MULTILINE)
    lowercase = [
        a
        for a in arms
        for pat in a.split("|")
        if pat.split(":")[0] in {"cggv", "cgds", "orpha", "icees", "ncit"}
    ]
    assert not lowercase, lowercase


def test_ncit_arm_checks_for_the_local_build_before_rebuilding():
    """`rebuild ncit` opens `sqlite:obo:ncit`, and OAK downloads that build when
    it is absent (CLAUDE.md, oak_db). fetch-reference must ask first."""
    recipe = _fetch_reference_recipe()
    arm = re.search(
        r"^\s*NCIT:\*[^)]*\)\n(.*?)^\s*;;", recipe, re.DOTALL | re.MULTILINE
    )
    assert arm, "no NCIT arm"
    assert "local_build_present" in arm.group(1)


def test_orphanet_arm_refreshes_when_any_product_is_missing():
    """Every ORPHA record merges five products, and the source refuses a partial
    set (#13941). The arm must check all five, the same five the loader needs,
    and tolerate a drifted-pin refresh failure, which still downloads them."""
    from dismech.structured_sources.orphanet import _PRODUCT_FILES

    recipe = _fetch_reference_recipe()
    arm = re.search(
        r"^\s*ORPHA:\*[^)]*\)\n(.*?)^\s*;;", recipe, re.DOTALL | re.MULTILINE
    )
    assert arm, "no ORPHA arm"
    body = arm.group(1)
    listed = re.search(r"for orpha_file in ([^;]+);", body)
    assert listed, "ORPHA arm does not loop over the product files"
    assert tuple(listed.group(1).split()) == _PRODUCT_FILES
    assert "structured_sources.cli refresh orphanet || true" in body
    assert body.index("refresh orphanet") < body.index("rebuild orphanet")


def _run_recipe(tmp_path: Path, *args: str):
    """Run the recipe body with `{{identifiers}}` substituted the way `just`
    does (space-joined, unquoted) against a stub validator that records its
    argv, so nothing is fetched."""
    body = textwrap.dedent(_fetch_reference_recipe())
    script = tmp_path / "recipe.sh"
    script.write_text(body.replace("{{identifiers}}", " ".join(args)))
    stub = tmp_path / "scripts" / "run_reference_validator.sh"
    stub.parent.mkdir()
    stub.write_text('#!/usr/bin/env bash\necho "LRV: $*"\n')
    stub.chmod(0o755)
    return subprocess.run(
        ["bash", str(script)], check=False, cwd=tmp_path, capture_output=True, text=True
    )


def test_force_flag_reaches_the_validator_not_the_identifier_loop(tmp_path):
    """`just fetch-reference PMID:X --force` used to treat `--force` as a second
    reference id and fail with "Missing argument 'REFERENCE_ID'" (#13185)."""
    result = _run_recipe(tmp_path, "PMID:26094573", "--force")
    assert result.returncode == 0, result.stderr
    assert "LRV: cache reference --force PMID:26094573" in result.stdout
    assert "Fetching reference: --force" not in result.stdout


def test_plain_fetch_passes_no_flags(tmp_path):
    result = _run_recipe(tmp_path, "PMID:1", "DOI:10.1/x")
    assert result.returncode == 0, result.stderr
    assert "LRV: cache reference PMID:1" in result.stdout
    assert "LRV: cache reference DOI:10.1/x" in result.stdout


def test_flags_without_an_identifier_fail(tmp_path):
    result = _run_recipe(tmp_path, "--force")
    assert result.returncode != 0
    assert "LRV:" not in result.stdout
