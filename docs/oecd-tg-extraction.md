# Extracting test-method details from OECD Test Guidelines

An OECD Test Guideline is the authoritative statement of what a validated test method
measures. It is also unstructured prose, which means a claim sourced from it cannot be
checked without re-reading the PDF.

## Why the method name is not enough: IL-8 in TG 442D and TG 442E

Two guidelines in this series address different key events of the skin sensitisation
AOP, and **IL-8 appears in both, meaning something different each time.**

- **TG 442D — Key Event 2, keratinocyte activation.** IL-8 is one of four marker genes
  (with ATF3, GCLM and DNAJB4) quantified by RT-qPCR in the EpiSensA and Epi2SensA test
  methods, in reconstructed human epidermis.
- **TG 442E — Key Event 3, dendritic cell activation.** TG 442E covers the **IL-8 Luc
  assay**, a luciferase reporter method. TG 442D points at it in its own paragraph 5:
  "the OECD TG 442E addresses the activation of dendritic cells, the third key event of
  the skin sensitisation AOP".

Both usages are correct and they are not interchangeable. The string `IL-8` does not
distinguish a marker gene at one key event from a reporter assay at another; only the
guideline, the method and the paragraph do. Both are already curated here as separate
models (see
[#15944](https://github.com/monarch-initiative/dismech/issues/15944)), so the
distinction is one this repository already depends on.

It is an easy distinction to lose. While
[#16338](https://github.com/monarch-initiative/dismech/issues/16338) was being written,
the proposal itself claimed that a published figure had misplaced IL-8 at Key Event 3 —
reasoning from TG 442D alone, where IL-8 is a Key Event 2 marker gene, without checking
TG 442E, which covers the reporter assay and makes Key Event 3 correct. There was no
error in the paper. The mistake was in the proposal, which is the sharpest argument for
recording which guideline, which method, which key event, and which paragraph each fact
came from: that record settles the question in one lookup.

Two features of the guidelines make the distinction easy to lose, and both are things an
extraction can preserve:

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
just check-tg-extraction --records data/oecd_tg/tg442d-methods.json
```

A record is one per **test method**, not one per guideline — TG 442D yields five —
with the source guideline as a property of the record. The judgement itself is
guided by the `extract-tg-method` skill, which carries the field vocabulary and the
four ways a verbatim quote can still be cited for a claim it does not make.

`data/oecd_tg/tg442d-methods.json` holds the result: KeratinoSens™, LuSens, EpiSensA,
Epi2SensA and α-Sens®, plus `CITED_COMPARATOR` stubs for the five animal methods TG 442D
names but does not describe (GPMT and the Buehler Test under TG 406, the LLNA under
TG 429, and its modifications under TG 442A and TG 442B). Seventy-four quoted facts,
each verified against the index.

Two things that extraction settled, both of which a method name alone would have lost:

- **The three luciferase methods differ in their response element.** KeratinoSens™ uses
  the ARE of the human *AKR1C2* gene, LuSens the ARE of the **rat** *NQO1* gene, and
  α-Sens® a quadruplicated ARE whose sequence the guideline states is identical to the
  KeratinoSens™ VRM.
- **Performance figures are mostly agreement with a mouse assay.** All five methods
  report accuracy against the LLNA; only EpiSensA and α-Sens® also report it against
  human data, and the two diverge — EpiSensA is 67.6% specific against the LLNA and
  52.9% against human results. The comparator is therefore part of the field name
  (`performance_vs_llna`, `performance_vs_human`), not a neighbouring field that can be
  dropped while the number survives.

## Citing a guideline from a KB entry

Not yet possible with a verified snippet. `just fetch-reference
DOI:10.1787/9789264229822-en` resolves and titles correctly — "Test No. 442D: In Vitro
Skin Sensitisation" — but caches with `content_type: unavailable`, because the OECD
iLibrary landing page carries no abstract. There is no body for
`linkml-reference-validator` to match a quote against, so an entry can name the
guideline but cannot quote it.

The paragraph index is the missing body, and the repository already has the pattern for
this: a structured-database source (`src/dismech/structured_sources/`) that writes a
line-oriented `references_cache/` file whose rows are stable quotable substrings, as
`ORPHA:`, `CGGV:`, `ICEES:` and `NCIT:` do. Until that exists, a method carried into a
disease entry cites the literature for its evidence and names the guideline and
paragraph in prose.

## What the checker does and does not establish

It checks that each recorded quote is a real substring of the paragraph it cites. That
catches a fabricated quote, a quote attributed to the wrong appendix (it says where the
sentence actually is), and a citation to an out-of-scope paragraph.

It also rejects three shapes that would otherwise pass as citations without being any:
a bare value with no quote at all (`"key_event": 2`), a quote that normalises to nothing
(`"(TM)"`, whitespace — the empty string is a substring of every paragraph), and a quote
below a five-word floor. The floor is `MIN_QUOTE_WORDS`, the same as the repository's
`MIN_SNIPPET_WORDS` for evidence snippets and for the same reason: a three-word fragment
matches in many paragraphs, so neither the match nor the "appears in &lt;other
paragraph&gt;" diagnosis means anything.

**It cannot tell whether a quoted sentence supports the value attached to it.** A quote
can be verbatim, correctly located, and cited for a claim it does not make — a TG 442D
marker-gene sentence recorded against Key Event 3, say. That needs a reader, and
`test_the_checker_cannot_tell_whether_a_quote_supports_its_value` pins the limitation so
nobody mistakes a green run for a correct extraction.

## Four things that will bite

**Use pypdf's `layout` extraction mode, not the default.** On this document the default
`plain` mode inserts spaces inside words — `asses sing`, `Ker atinoSens`, `de pendent`.
Whitespace normalisation collapses runs of spaces but does not close a gap inside a
word, so every quote taken from `plain` output is unusable as a verbatim quote. The
extractor pins this, and
`test_a_mid_word_gap_still_fails` keeps the checker from papering over it.

**A hyphenated word breaks across a line, and the join splits it.** `layout` mode has
its own version of the same defect, and it is harder to see because the gap lands on a
hyphen where it reads as punctuation. "non-sensitisers" printed across a line break
arrived as `non- sensitisers`, and `Reverse Transcription-quantitative PCR` as
`Transcription- quantitative` from justified spacing inside a single line. Seventeen
such spots were committed in the first index, including `IL- 8` in the EpiSensA
marker-gene list, which made that list unquotable. `join_lines` and
`close_hyphen_gaps` close both causes, keeping the hyphen and dropping only the space;
a suspended hyphen (`5- and 10-fold`) is exempted by the same `COORD_RE` guard
`scripts/check_folded_hyphens.py` uses, so the two detectors agree by construction.
`test_committed_index_has_no_word_split_at_a_hyphen` keeps the committed index clean.

**The guideline writes the same method name several ways.** Body text has
`KeratinoSens™`; title blocks have `KeratinoSensTM` — and appendices IB and ID use the
title-block spelling in running prose. The checker drops the trademark marker on both
sides, so a quote typed `KeratinoSens`, `KeratinoSens(TM)` or `KeratinoSens™` all
verify.

**One α is not the other.** Paragraph ID/3 writes the α-Sens® name once with U+237A,
the APL functional symbol, where every other mention uses U+03B1. Both fold to `alpha`,
so a quote copied from either sentence verifies — but a tool comparing the raw strings
would see two different method names.

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
