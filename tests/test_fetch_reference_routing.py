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
