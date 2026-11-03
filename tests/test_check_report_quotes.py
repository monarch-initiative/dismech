"""Quote extraction and the comparison form, which decide whether a quote is real.

`just check-report-quotes` reads a provider report and asks, per quote, whether
that text appears in the abstract the report attributes it to. Both halves of
that are text handling: pulling the quote out of Markdown with the PMID that
follows it, and folding both sides so that typographic differences do not read as
a fabricated quote. Neither touches the network, so both are testable here; the
fetch is not.
"""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

import check_report_quotes as checker

REPORT = """\
Some prose introducing a finding.

> "Loss of glucocorticoid receptor function produced a sustained elevation of
> cortisol in adult animals."

[PMID:22641177](https://pubmed.ncbi.nlm.nih.gov/22641177/)

Another paragraph.

> *"A second claim, bolded the way one provider emits them."*

Source: [PMID:30820902](https://pubmed.ncbi.nlm.nih.gov/30820902/)

> "A third claim with nothing cited anywhere near it."

And then only prose, for several hundred characters, so that no PMID falls
within reach of the quote above.
"""


def test_a_quote_is_paired_with_the_pmid_that_follows_it() -> None:
    found = checker.pairs(REPORT)

    assert [pmid for _, pmid in found] == ["22641177", "30820902", None]


def test_a_quote_wrapped_across_block_quote_lines_is_rejoined() -> None:
    """Each continuation line carries its own "> ". Left in, every multi-line
    quote would fail to match its source and read as a fabrication."""
    quote = checker.pairs(REPORT)[0][0]

    assert ">" not in quote
    assert "function produced a sustained elevation of cortisol" in quote


def test_a_quote_with_no_citation_keeps_a_null_pmid() -> None:
    """It becomes NO_PMID, which is one of the two verdicts `--strict` fails on."""
    assert checker.pairs(REPORT)[-1][1] is None


def test_the_comparison_form_folds_what_a_provider_substitutes() -> None:
    """Curly quotes, en dashes and case are typography, not evidence of a paraphrase."""
    report_side = checker.normalise("“T-cell receptor” signalling — reduced")
    source_side = checker.normalise("T-cell receptor signalling - reduced")

    assert report_side == source_side


def test_the_comparison_form_still_separates_different_claims() -> None:
    assert checker.normalise("cortisol rose") != checker.normalise("cortisol fell")


def test_only_an_unattributable_quote_is_a_strict_failure() -> None:
    """NOT_IN_ABSTRACT is not a failure: a report may quote a full text this
    script cannot read. A missing or unresolvable PMID is never legitimate."""
    assert checker.FAILING == ("NO_PMID", "PMID_UNRESOLVED")
    assert "NOT_IN_ABSTRACT" not in checker.FAILING
