"""Adversarial probe: can fabricated evidence get past validation in SEPIO form?

Issue #7439. Raised by @cmungall: the experimental SEPIO evidence model moves the
quoted text and its reference into a *nested* shape (``value`` on a DataItem, the
source one level down at ``reported_in.id``), and "the validator ran and said
nothing" is not the same as "the validator looked". A new structural path through
the anti-hallucination stack deserves to be attacked before it is trusted.

Every case below is a piece of evidence a curator (or a hallucinating agent) might
plausibly produce, expressed in SEPIO form, with a native-form control wherever the
comparison tells us whether a hole is SEPIO-specific or pre-existing. Each test
asserts on the layer that is *supposed* to catch it:

- schema validation      -- structural: is there a source at all?
- reference validation   -- semantic: does the quote actually appear in that source?
- the snippet audit      -- advisory: is anything going unchecked?

The tests deliberately assert on the *whole stack's* verdict, not one validator's,
because that is the property that matters: fabricated evidence must not survive
``just validate``.
"""

from __future__ import annotations

from pathlib import Path

import pytest
from linkml.validator import validate_file
from linkml_runtime.utils.schemaview import SchemaView

from dismech.reference_snippet_audit import audit_files

ROOT = Path(__file__).parent.parent
SCHEMA = ROOT / "src" / "dismech" / "schema" / "dismech.yaml"
CONFIG = ROOT / "conf" / "reference_validator_config.yaml"
CACHE = ROOT / "references_cache"

# Two real, cached references used as the raw material for the forgeries.
REAL_PMID = "PMID:9922375"
REAL_PMID_TITLE = "Structure and function of the CFTR chloride channel."
REAL_QUOTE = (
    "The CFTR is composed of five domains: two membrane-spanning domains (MSDs), "
    "two nucleotide-binding domains (NBDs), and a regulatory (R) domain."
)
OTHER_REAL_PMID = "PMID:23878362"

FABRICATED_QUOTE = (
    "CFTR dysfunction was shown to be reversed entirely by daily consumption "
    "of green cheese."
)


def _sepio_entry(item_body: str) -> str:
    """A minimal Disease carrying one SEPIO evidence item, indented into place."""
    return (
        "name: Adversarial fixture\n"
        "pathophysiology:\n"
        "- name: Mechanism Under Test\n"
        "  has_evidence_lines:\n"
        "  - evidence_type: HUMAN_CLINICAL\n"
        "    direction_of_evidence_provided: SUPPORT\n"
        "    has_evidence_items:\n" + item_body
    )


def _write(tmp_path: Path, content: str) -> Path:
    path = tmp_path / "case.yaml"
    path.write_text(content, encoding="utf-8")
    return path


@pytest.fixture(scope="module")
def schema():
    """The dismech schema, loaded once.

    Loaded through SchemaView so its relative `imports:` (e.g. the
    classifications/ modules) resolve against the schema file rather than the
    process working directory.
    """
    return SchemaView(str(SCHEMA)).schema


def _schema_validate(schema, path: Path) -> tuple[bool, str]:
    """Run LinkML schema validation. Returns ``(passed, joined messages)``."""
    report = validate_file(path, schema, "Disease")
    messages = "\n".join(str(r.message) for r in report.results)
    return not report.results, messages


def _audit(path: Path):
    return audit_files(
        [path], schema_path=SCHEMA, config_path=CONFIG, cache_dir=CACHE
    )


# --- The quote does not appear in the cited paper ----------------------------
#
# The core anti-hallucination guarantee. If this ever regresses in SEPIO form,
# the model is not safe to curate against, full stop.


def test_fabricated_quote_is_caught_in_sepio_form(tmp_path: Path) -> None:
    path = _write(
        tmp_path,
        _sepio_entry(
            "    - data_type: TEXT_SPAN\n"
            f"      value: {FABRICATED_QUOTE!r}\n"
            "      reported_in:\n"
            f"        id: {REAL_PMID}\n"
            f"        title: {REAL_PMID_TITLE!r}\n"
        ),
    )

    report = _audit(path)

    assert report.total == 1
    assert report.verified == 0
    assert len(report.mismatched) == 1
    assert "not found as substring" in report.mismatched[0].reason


def test_fabricated_quote_is_caught_in_native_form_too(tmp_path: Path) -> None:
    """Control: the SEPIO result above is not better or worse than the status quo."""
    path = _write(
        tmp_path,
        "name: Adversarial fixture\n"
        "pathophysiology:\n"
        "- name: Mechanism Under Test\n"
        "  evidence:\n"
        f"  - reference: {REAL_PMID}\n"
        "    supports: SUPPORT\n"
        f"    snippet: {FABRICATED_QUOTE!r}\n",
    )

    report = _audit(path)

    assert (report.total, report.verified) == (1, 0)
    assert len(report.mismatched) == 1


def test_real_quote_attributed_to_the_wrong_paper_is_caught(tmp_path: Path) -> None:
    """A genuine quote, but cited to a different (real, cached) paper."""
    path = _write(
        tmp_path,
        _sepio_entry(
            "    - data_type: TEXT_SPAN\n"
            f"      value: {REAL_QUOTE!r}\n"
            "      reported_in:\n"
            f"        id: {OTHER_REAL_PMID}\n"
        ),
    )

    report = _audit(path)

    assert (report.total, report.verified) == (1, 0)
    assert len(report.mismatched) == 1


def test_genuine_evidence_still_verifies(schema, tmp_path: Path) -> None:
    """Negative control for the negative controls: honest evidence must pass."""
    path = _write(
        tmp_path,
        _sepio_entry(
            "    - data_type: TEXT_SPAN\n"
            f"      value: {REAL_QUOTE!r}\n"
            "      reported_in:\n"
            f"        id: {REAL_PMID}\n"
        ),
    )

    passed, output = _schema_validate(schema, path)
    assert passed, output

    report = _audit(path)
    assert (report.total, report.verified) == (1, 1)
    assert report.mismatched == []


# --- Evidence with no source at all ------------------------------------------
#
# The hole the probe actually found. The reference validator only checks excerpts
# that HAVE a reference, so an optional source means a fabricated quote attributed
# to nothing is both schema-valid and reference-valid: it passes by not being
# looked at. Closed by making `reported_in` (and `Document.id`) required, which is
# a deliberate tightening of upstream SEPIO.


def test_evidence_item_without_a_source_fails_schema_validation(
    schema, tmp_path: Path
) -> None:
    path = _write(
        tmp_path,
        _sepio_entry(
            "    - data_type: TEXT_SPAN\n"
            f"      value: {FABRICATED_QUOTE!r}\n"
        ),
    )

    passed, output = _schema_validate(schema, path)

    assert not passed, "an evidence item with no source must not validate"
    assert "reported_in" in output


def test_source_document_without_an_identifier_fails_schema_validation(
    schema, tmp_path: Path
) -> None:
    """The nastier variant: a source that LOOKS cited but carries no identifier.

    Native form cannot express this -- `reference:` is a CURIE string or absent --
    so it is a shape the nested model introduces, and the one most likely to fool a
    human reviewer skimming a diff.
    """
    path = _write(
        tmp_path,
        _sepio_entry(
            "    - data_type: TEXT_SPAN\n"
            f"      value: {FABRICATED_QUOTE!r}\n"
            "      reported_in:\n"
            "        document_type: PRIMARY_LITERATURE\n"
            "        title: A definitive study of the thing I am claiming.\n"
        ),
    )

    passed, output = _schema_validate(schema, path)

    assert not passed, "a source document with no identifier must not validate"
    assert "id" in output


def test_audit_reports_an_unsourced_excerpt_rather_than_counting_nothing(
    tmp_path: Path,
) -> None:
    """Belt and braces behind the schema fix, and it covers native form too.

    Before this, a file whose only evidence was an unsourced quote audited as
    ``0 (no reference/snippet pairs in input)`` -- which reads as "nothing to
    check" when it means "an unverifiable claim is present". That reassuring zero
    is precisely the failure mode #7252 exists to prevent.
    """
    path = _write(
        tmp_path,
        "name: Adversarial fixture\n"
        "pathophysiology:\n"
        "- name: Mechanism Under Test\n"
        "  evidence:\n"
        "  - supports: SUPPORT\n"
        f"    snippet: {FABRICATED_QUOTE!r}\n",
    )

    report = _audit(path)

    assert report.total == 1
    assert report.verified == 0
    assert report.unsourced == 1
    assert "no reference" in report.mismatched[0].reason
    assert "no reference to check against" in report.summary_line()
    # The old behaviour, stated so a regression is unmistakable.
    assert "no reference/snippet pairs in input" not in report.summary_line()


# --- Known residual gap, asserted so it cannot regress unnoticed -------------


def test_skipped_prefix_reference_is_visibly_unverified_not_silently_passed(
    tmp_path: Path,
) -> None:
    """A quote cited to a prefix in `skip_prefixes` is never substring-checked.

    This is a PRE-EXISTING property of the reference-validator config (DOI, MONDO
    and the dataset accessions are all skipped), inherited by the SEPIO form
    rather than introduced by it -- so it is out of scope to fix here. What this
    test pins down is that the audit still *counts* the pair and reports it as
    unverified, so the gap is visible in the summary line instead of looking like
    a clean run. See the pilot doc's "Residual gaps" section.
    """
    path = _write(
        tmp_path,
        _sepio_entry(
            "    - data_type: TEXT_SPAN\n"
            f"      value: {FABRICATED_QUOTE!r}\n"
            "      reported_in:\n"
            "        id: DOI:10.1000/completely.made.up\n"
        ),
    )

    report = _audit(path)

    assert report.total == 1
    assert report.verified == 0
    assert report.skipped_prefix == 1
    assert "skipped by prefix" in report.summary_line()
