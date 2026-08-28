"""Deep-research reports are term-validated wherever they are generated.

Reports suggest ontology terms because the templates ask them to, and until
`deep-research-client` 0.2.11 nothing checked those suggestions — citation
validation does not reach them (dismech#9729: a report with 26/26 verified
citations offered MONDO:0010674, Hunter syndrome, as the Charcot-Marie-Tooth
X-linked term). These tests keep the flags wired to every path that writes a
report, so a recipe added later does not silently skip the check.
"""

from __future__ import annotations

import importlib.util
import re
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent

# Loaded the way tests/test_hypothesis_deep_research.py loads it: the script is
# run directly rather than installed, so it is imported from its path rather
# than through sys.path, which keeps every import at the top of this file.
SCRIPT_PATH = ROOT / "scripts" / "hypothesis_deep_research.py"
SPEC = importlib.util.spec_from_file_location("hypothesis_deep_research", SCRIPT_PATH)
assert SPEC and SPEC.loader
hypothesis_deep_research = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = hypothesis_deep_research
SPEC.loader.exec_module(hypothesis_deep_research)

JUSTFILE = (ROOT / "project.justfile").read_text()


def test_every_research_recipe_validates_terms_and_references() -> None:
    """No recipe checks a report's citations while skipping its ontology terms."""
    reference_lines = JUSTFILE.count("{{dr_validation}}")
    term_lines = JUSTFILE.count("{{dr_term_validation}}")

    assert reference_lines >= 6, "expected the research recipes to validate references"
    assert term_lines == reference_lines, (
        "every recipe carrying {{dr_validation}} must also carry "
        "{{dr_term_validation}}; a research recipe is validating citations "
        "but not ontology terms"
    )


def test_term_validation_defaults_skip_hgnc() -> None:
    """Gene CURIEs are reported as unverifiable rather than as confabulations.

    `sqlite:obo:hgnc` holds gene terms under the lowercase `hgnc:` this repo
    uses, so the uppercase `HGNC:4283` a report writes resolves to nothing and
    is reported as invented; through the `ols:` adapter the same CURIE comes
    back as "mitochondrial chromosome". Both are false alarms on a real gene.
    """
    match = re.search(r'(?m)^dr_term_validation := "(.*)"$', JUSTFILE)
    assert match is not None, "dr_term_validation variable not found"
    flags = match.group(1)

    assert "--validate-terms" in flags
    assert "--term-skip-prefix HGNC" in flags
    assert "--term-cache-dir terms_cache" in flags
    assert "--term-oak-config" not in flags, (
        "conf/oak_config.yaml routes HGNC/GENO/ECTO to sqlite:obo:, which makes "
        "a research run download hundreds of MB mid-validation"
    )


def test_retrofit_recipe_matches_the_generation_time_defaults() -> None:
    """A report checked after the fact is checked the same way as a fresh one."""
    match = re.search(
        r"(?m)^validate-research-terms \+args:\n((?:    .*\n)+)", JUSTFILE
    )
    assert match is not None, "validate-research-terms recipe not found"
    body = match.group(1)

    assert "validate-terms" in body
    assert "--cache-dir terms_cache" in body
    assert "--skip-prefix HGNC" in body
    assert "--in-place" in body
    assert "{{dr_client}}" in body, (
        "go through the wrapper, as every other deep-research-client call does"
    )


def test_hypothesis_research_validates_terms_by_default() -> None:
    """The hypothesis path builds its own command and needs the flags too."""
    assert hypothesis_deep_research.term_validation_args([]) == [
        "--validate-terms",
        "--term-cache-dir",
        "terms_cache",
        "--term-skip-prefix",
        "HGNC",
    ]


def test_caller_supplied_term_flags_win() -> None:
    """A curator steering term validation does not get the defaults as well."""
    assert hypothesis_deep_research.term_validation_args(["--term-offline"]) == []
    assert hypothesis_deep_research.term_validation_args(["--validate-terms"]) == []
    assert hypothesis_deep_research.term_validation_args(["--param", "x=1"]) != []
