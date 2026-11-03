# Extracting test-method details from OECD Test Guidelines

An OECD Test Guideline is the authoritative statement of what a validated test method
measures. It is also unstructured prose, which means a claim sourced from it cannot be
checked without re-reading the PDF — and claims sourced from it do go wrong.

The motivating case is IL-8. TG 442D names IL-8 as one of four marker genes quantified
by RT-qPCR in the EpiSensA and Epi2SensA test methods, which address **Key Event 2** of
the skin sensitisation AOP, keratinocyte activation. The **IL-8 Luc assay** is a
different thing: a dendritic-cell activation method, **Key Event 3**, covered by TG
442E. TG 442D says as much in its own paragraph 5. A published figure placed IL-8 under
Key Event 3, and both halves of the conflation are already curated in this repository
(see [#15944](https://github.com/monarch-initiative/dismech/issues/15944)).

Two features of the guideline make that mistake easy, and both are things an extraction
can preserve:

- **A gene symbol carries no key event on its own.** `IL-8` means one thing in a list of
  reconstructed-human-epidermis marker genes and another in the name of a reporter
  assay. What disambiguates them is the sentence and the paragraph they sit in.
- **Adjacent paragraphs make different kinds of claim.** TG 442D's paragraph 2 states
  scope — which key event the guideline addresses. Paragraph 3 states validation status
  — "These test methods have all been considered scientifically valid", then separates
  the validated reference methods from the Performance-Standards-based ones, naming a
  different peer-review body for each. A fact lifted from paragraph 3 without its
  paragraph loses the difference between *what a method measures* and *how it was
  validated*.

## The contract

**Every extracted fact carries three things: the value, the guideline's own sentence,
and the paragraph number.**

A field holding `"key_event": 2` is a paraphrase. It may well be right, and nothing can
check it. The same field carrying the sentence it came from and `442D/IA/1` can be
checked by a script and by any reader with the PDF.

**Paragraph numbering restarts in every division**, so a bare paragraph number is
ambiguous across the five methods TG 442D describes. A citation key names both:
`442D/IA/3` is paragraph 3 of Appendix IA, not paragraph 3 of the guideline. The
General Introduction is `GI`.

## Scope

In scope:

- the General Introduction
- within each appendix, `Initial Considerations` and `Principle of the Test`

Out of scope: `PROCEDURE`, `DATA AND REPORTING`, the interpretation of results and
prediction model sections, and the preparation details for biological elements and test
chemicals.

Note this is narrower than the whole document but wider than the introduction alone.
Each method's biology — cell line, reporter construct, tissue model, marker genes — is
described in its appendix, so extracting only the General Introduction would drop
exactly what the extraction is for.

## The two layers, and why they are separate

**Layer 1 is deterministic.** `scripts/extract_oecd_tg.py` turns the PDF into a
paragraph index: every in-scope numbered paragraph, with its division, section,
subheading and page. It extracts text and nothing else.

```bash
just extract-oecd-tg path/to/TG_442D.pdf
just check-tg-extraction                       # reports on the index alone
```

**Layer 2 is a judgement.** Which paragraph supports which fact about which method is
not something a script can decide, and the extraction's whole purpose is to get that
right. It is made against the index rather than against the PDF, so the result is
checkable.

```bash
just check-tg-extraction --records path/to/records.json
```

A record is one per **test method**, not one per guideline — TG 442D yields five —
with the source guideline as a property of the record.

## What the checker does and does not establish

It checks that each recorded quote is a real substring of the paragraph it cites. That
catches a fabricated quote, a quote attributed to the wrong appendix (it says where the
sentence actually is), a value with no quote, and a citation to an out-of-scope
paragraph.

**It cannot tell whether a quoted sentence supports the value attached to it.** A quote
can be verbatim, correctly located, and cited for a claim it does not make — which is
the IL-8 error itself. That needs a reader, and
`test_the_checker_cannot_tell_whether_a_quote_supports_its_value` pins the limitation so
nobody mistakes a green run for a correct extraction.

## Two things that will bite

**Use pypdf's `layout` extraction mode, not the default.** On this document the default
`plain` mode inserts spaces inside words — `asses sing`, `Ker atinoSens`, `de pendent`.
Whitespace normalisation collapses runs of spaces but does not close a gap inside a
word, so every quote taken from `plain` output is unusable as a verbatim quote. The
extractor pins this, and
`test_a_mid_word_gap_still_fails` keeps the checker from papering over it.

**The guideline writes the same method name several ways.** Body text has
`KeratinoSens™`; title blocks have `KeratinoSensTM`. The checker drops the trademark
marker on both sides, so a quote typed `KeratinoSens`, `KeratinoSens(TM)` or
`KeratinoSens™` all verify. Prefer quoting body text.

## Source pinning

`data/oecd_tg/MANIFEST.yaml` pins each guideline's sha256, DOI, adoption date and page
count. The PDFs are not committed; the index is, so it is reviewable and the extraction
is auditable without the 3 MB binary.

A guideline is revised under the same number, and its iLibrary DOI resolves to the
current edition rather than the pinned one. A checksum mismatch therefore usually means
a new adoption, not a corrupt download. Record the new checksum and adoption date and
re-extract — do not edit the checksum to make an old index validate.

OECD Guidelines for the Testing of Chemicals are published under
[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/); quoted guideline text is
attributed to the OECD.

## Scale

TG 442D first, deliberately. The skin-sensitisation cluster (442C, 442E, 497, and the
animal guidelines 406, 429, 442A, 442B) and OECD Section 4 more broadly are follow-ups,
and whether this approach generalises is something the first guideline should answer
rather than something to assume.

Tracked in [#16338](https://github.com/monarch-initiative/dismech/issues/16338).
