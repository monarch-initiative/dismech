"""The research recipes must hand the provider the entry's own MONDO ID.

`just research-disorder` dispatches a deep-research run from a disorder YAML.
For a long time it passed ``--var "mondo_id="`` — hardcoded empty — so every
run went out with a disease *name* and no identifier.

That is not cosmetic. An openscientist run for "Cardiomyopathy Dilated 2H"
came back naming RPL3L as the causal gene, which is cardiomyopathy dilated
2*D*: a different disease, one letter away in the name and better documented.
With no identifier there was nothing to disambiguate on. Re-running the same
provider with ``mondo_id=MONDO:0859358`` produced a correct GET3/ASNA1 report
(issue #10495, PR #10696).

Nothing downstream catches this. The report's own reference validation
returned 19/19 resolved and 0 off topic, because relevance is scored against
the report's *own* vocabulary — a report built around the wrong disease scores
its wrong-disease citations as on topic.

Two ways of extracting the ID were tried and both were wrong in the same way:
a line window (``grep -A3``/``-A8``) has no idea where the ``disease_term``
block ends, so it silently missed 20 entries whose block carries a
``description:``, and on two others it reached *past* the block and returned a
MONDO the entry itself rejects — into a "do not use this term" comment in
``Acute_Post-Surgical_Pain``, and into a ``skos:closeMatch`` cross-reference in
``CKD-Mineral_Bone_Disorder``. Parsing the YAML is exact by construction; these
tests pin that and forbid a regression to a line window.
"""

import re
import subprocess
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).parent.parent
KB = ROOT / "kb" / "disorders"
RECIPES = ("research-disorder", "research-datasets", "research-disorder-cyberian-codex")


def _recipe_body(text: str, recipe: str) -> str:
    lines = text.split("\n")
    start = next(
        i for i, ln in enumerate(lines) if re.match(rf"^{re.escape(recipe)}\b.*:$", ln)
    )
    body = []
    for ln in lines[start + 1 :]:
        if ln and not ln[0].isspace():
            break
        body.append(ln)
    return "\n".join(body)


def _justfile() -> str:
    return (ROOT / "project.justfile").read_text()


def test_no_recipe_hardcodes_an_empty_mondo_id():
    """The regression that caused the wrong-disease report."""
    text = _justfile()
    offenders = [r for r in RECIPES if '--var "mondo_id=" ' in _recipe_body(text, r)]
    assert not offenders, (
        f"These recipes hardcode an empty mondo_id: {offenders}. A deep-research run "
        "dispatched with a disease name and no identifier can resolve to a "
        "similarly-named disease -- see issue #10495."
    )


def test_every_research_recipe_passes_the_extracted_mondo_id():
    text = _justfile()
    for recipe in RECIPES:
        body = _recipe_body(text, recipe)
        assert '--var "mondo_id=$mondo_id"' in body, (
            f"{recipe} does not forward the extracted mondo_id to the provider."
        )
        assert "mondo_id=$(" in body, f"{recipe} does not extract a mondo_id at all."


def test_mondo_extraction_does_not_use_a_line_window():
    """A `grep -A<n>` window cannot know where the disease_term block ends."""
    text = _justfile()
    for recipe in RECIPES:
        body = _recipe_body(text, recipe)
        window = re.search(r"mondo_id=\$\(grep -A\d+", body)
        assert window is None, (
            f"{recipe} extracts mondo_id with a fixed line window. That silently "
            "misses entries whose disease_term block carries a description:, and on "
            "entries with an unbound disease_term it reads past the block into "
            "comments or mappings and returns a MONDO the entry rejects. Parse the "
            "YAML instead."
        )


def _extract(path: Path) -> str:
    """Run the same extraction the recipes use."""
    code = (
        "import sys,yaml;d=yaml.safe_load(open(sys.argv[1])) or {};"
        "t=(d.get('disease_term') or {}).get('term') or {};"
        "print(t.get('id') or '' if isinstance(t,dict) else '')"
    )
    out = subprocess.run(
        [sys.executable, "-c", code, str(path)],
        capture_output=True,
        text=True,
        check=False,
    )
    return out.stdout.strip()


def test_extraction_matches_the_parsed_disease_term_for_every_entry():
    """Exactness, across the whole corpus rather than a sample.

    The `-A3` window was verified on four hand-picked entries and passed; all
    four happened to have no `description:` in the block, which is the only
    failure mode the change had. Sampling was the wrong check.
    """
    mismatches = []
    for path in sorted(KB.glob("*.yaml")):
        try:
            data = yaml.safe_load(path.read_text()) or {}
        except yaml.YAMLError:
            continue
        term = (data.get("disease_term") or {}).get("term") or {}
        expected = (term.get("id") or "") if isinstance(term, dict) else ""
        actual = _extract(path)
        if actual != expected:
            mismatches.append((path.name, actual, expected))
    assert not mismatches, (
        f"mondo_id extraction disagrees with the parsed disease_term.term.id "
        f"for {len(mismatches)} entries: {mismatches[:5]}"
    )


def test_unbound_disease_term_yields_no_mondo_id():
    """An entry that deliberately declines to bind a term must send nothing.

    Both of these have an unbound top-level `disease_term`. A line window
    returned a MONDO for each anyway -- from a "do not use this term" comment
    and from a `skos:closeMatch` cross-reference respectively, neither of which
    is disease identity.
    """
    for name in ("Acute_Post-Surgical_Pain", "CKD-Mineral_Bone_Disorder"):
        path = KB / f"{name}.yaml"
        if not path.exists():
            continue
        assert _extract(path) == "", (
            f"{name} has an unbound disease_term but extraction returned an ID. "
            "A cross-reference or a commented-out term is not disease identity."
        )
