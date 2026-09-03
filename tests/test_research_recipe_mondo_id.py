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

import contextlib
import io
import re
import sys
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).parent.parent
KB = ROOT / "kb" / "disorders"
RECIPES = ("research-disorder", "research-datasets", "research-disorder-cyberian-codex")


def _recipe_body(text: str, recipe: str) -> str:
    lines = text.split("\n")
    start = next(
        i for i, ln in enumerate(lines) if re.match(rf"^{re.escape(recipe)}(?=[ :]).*:$", ln)
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
    # Tolerate quoting style and trailing whitespace: a single-quoted or
    # line-continued form would reintroduce the bug and pass a literal match.
    empty_var = re.compile(
        r"""--var\s+['\"]?mondo_id=['\"]?\s*\\?\s*$""", re.MULTILINE
    )
    offenders = [r for r in RECIPES if empty_var.search(_recipe_body(text, r))]
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


def _shipped_extraction_code() -> str:
    """Pull the extraction one-liner out of `project.justfile` verbatim.

    Reading it rather than restating it is the point: a hardcoded copy tests
    the copy. An earlier version of this file did exactly that, so the corpus
    test below was verifying a transcription while claiming to verify the
    shipped code.
    """
    bodies = {r: _recipe_body(_justfile(), r) for r in RECIPES}
    codes = set()
    for recipe, body in bodies.items():
        m = re.search(r'mondo_id=\$\(uv run python -c "(.+?)" "\$yaml_file"', body)
        assert m, f"could not find the extraction one-liner in {recipe}"
        codes.add(m.group(1))
    assert len(codes) == 1, (
        f"the three recipes no longer share one extraction: {codes}"
    )
    return codes.pop()


def _extract(path: Path, code: str) -> str:
    """Run the shipped extraction, in-process, against one file.

    In-process rather than by subprocess so the whole-corpus test stays fast;
    the code string is still the one read out of the justfile.
    """
    buf = io.StringIO()
    argv = sys.argv
    try:
        sys.argv = ["-c", str(path)]
        with contextlib.redirect_stdout(buf):
            exec(compile(code, "<justfile one-liner>", "exec"), {"__name__": "__main__"})
    finally:
        sys.argv = argv
    return buf.getvalue().strip()


@pytest.mark.kb_data
def test_extraction_matches_the_parsed_disease_term_for_every_entry():
    """Exactness, across the whole corpus rather than a sample.

    Marked `kb_data`: this parses all 2,535 KB files twice - once here for the
    expected value and once inside the shipped one-liner, which opens the path
    itself - which is squarely the "whole-KB sweep, slow and CPU-bound" the
    marker exists for. It runs parallel under `just test-kb` and in the nightly
    sweep. The fast lane keeps the string assertions and the named-entry tests
    below, which cover the same guarantees for the entries these docstrings are
    actually about, in about two seconds.

    The `-A3` window was verified on four hand-picked entries and passed; all
    four happened to have no `description:` in the block, which is the only
    failure mode the change had. Sampling was the wrong check.
    """
    code = _shipped_extraction_code()
    mismatches = []
    for path in sorted(KB.glob("*.yaml")):
        try:
            data = yaml.safe_load(path.read_text()) or {}
        except yaml.YAMLError:
            continue
        term = (data.get("disease_term") or {}).get("term") or {}
        raw = (term.get("id") or "").strip() if isinstance(term, dict) else ""
        # The recipes deliberately withhold a non-MONDO id and the ontology
        # root, so the expected value is the guarded form, not the raw binding.
        expected = raw if raw.startswith("MONDO:") and raw != "MONDO:0000001" else ""
        actual = _extract(path, code)
        if actual != expected:
            mismatches.append((path.name, actual, expected))
    assert not mismatches, (
        f"mondo_id extraction disagrees with the parsed disease_term.term.id "
        f"for {len(mismatches)} entries: {mismatches[:5]}"
    )


def test_named_entries_extract_correctly():
    """The edge cases these docstrings are actually about, in the fast lane.

    The whole-corpus sweep is marked `kb_data` because it parses every KB file
    twice. These five entries are the ones that have actually broken, so they
    stay in the fast lane where a code PR pays for them:

    * `Dorsalgia` binds MONDO:0000001, the root of MONDO, labelled "disease".
      Sending it would tell a provider the disease's identifier is the root of
      the ontology -- a wrong identity rather than a missing one, which is
      worse in exactly the code path this plumbing exists to make trustworthy.
    * `Acute_Post-Surgical_Pain` and `CKD-Mineral_Bone_Disorder` have unbound
      `disease_term`s; a line window read past the block and returned a
      commented-out term and a `skos:closeMatch` cross-reference respectively.
    * `Marfan_Syndrome` and `Noonan_Syndrome` carry a `description:` inside the
      block, which `grep -A3` could not see past.
    """
    code = _shipped_extraction_code()
    expected = {
        "Dorsalgia": "",
        "Acute_Post-Surgical_Pain": "",
        "CKD-Mineral_Bone_Disorder": "",
        "Marfan_Syndrome": "MONDO:0007947",
        "Noonan_Syndrome": "MONDO:0018997",
    }
    wrong = {}
    for name, want in expected.items():
        path = KB / f"{name}.yaml"
        if not path.exists():
            continue
        got = _extract(path, code)
        if got != want:
            wrong[name] = f"got {got!r}, want {want!r}"
    assert not wrong, f"extraction is wrong for known edge cases: {wrong}"
