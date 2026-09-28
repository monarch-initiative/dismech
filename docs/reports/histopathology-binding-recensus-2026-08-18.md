# Histopathology `finding_term` binding: re-census (2026-08-18)

Re-measurement of the ontology-binding gap that motivated the open design
discussion [#5140](https://github.com/monarch-initiative/dismech/issues/5140)
("the boundary between phenotypes (HP) and histopathology (NCIT)"), tracked in
[`design-decisions.md`](../explanation/design-decisions.md) §12.

The original triage
([`histopathology_ncit_triage-2026-07-02.md`](histopathology_ncit_triage-2026-07-02.md))
reported **123 unbound findings across 76 files**. That snapshot is six weeks
old and predates §9 (`ImagingFinding`) and §10 (electrophysiology), both of
which changed how the project reasons about finding-vs-phenotype boundaries.
This report re-derives the numbers and — more usefully — characterises *what
kind of thing* the unbound tail actually is, because the answer bears directly
on which of the issue's options A–D can work.

Regenerate every figure below with:

```bash
uv run python scripts/histopathology_binding_census.py
uv run python scripts/histopathology_binding_census.py --list-unbound   # per-finding detail
```

## Census

```
histopathology findings: 707 across 387 KB files
  ontology-bound finding_term: 382 (54%)
  unbound: 325 (46%) across 188 files
    no finding_term block at all: 293
    finding_term with preferred_term only: 32

bound-term vocabulary: NCIT 368, HP 14
```

Two things to note before reading further.

- **The gap grew, and grew faster than coverage.** 325 unbound against the
  triage's 123, across 188 files against 76. This is not regression — curation
  volume grew too — but binding is not keeping pace with new histopathology
  curation, so the decision in #5140 is not getting cheaper to defer.
- **The `HP:0025461` carve-out is nearly unused.** 14 of 382 bound findings use
  it, against 368 NCIT. The narrow HP accommodation already in
  `HistopathologyFindingTerm` is carrying almost no load.

## The finding that reframes the options

The issue frames the gap as a *vocabulary coverage* problem: NCIT is sparse for
organ-specific microscopic findings, HP has the terms but is fenced off at
`HP:0025461`, so option B (broaden the HP root) is the coverage win. The data do
not support that framing for most of the tail.

```
distinct unbound labels: 324 for 325 unbound findings
post-composed labels: 190 of 325 unbound (58%) vs 77 of 382 bound (20%)
findings using an inherited post-composition slot
  (located_in, modifier, laterality, spatial_extent, severity): 0 of 707
```

**There is essentially no recurring vocabulary in the unbound tail** — 324
distinct strings for 325 findings. A missing-terms problem produces repeats
(the same "foot process effacement" showing up in a dozen renal entries);
this does not. Spot-reading the tail shows why: the labels are rich
post-compositions, not single concepts —

- `Interface injury with vacuolar change and necrotic keratinocytes`
- `Intratubular 2,8-DHA crystals with chronic tubulointerstitial injury`
- `Neocortical GABAergic Interneuron Depletion and Mislocalization`
- `Atypical CD8-positive lymphomatoid infiltrate with lymphomatoid vasculitis (FUMHD)`

— each bundling an entity, a quality, often a cell type, a site, and a severity
or distribution modifier into one string. The unbound half is measurably
different in kind from the bound half: **58% of unbound labels are compound
against 20% of bound ones** (median 5 words vs 3). Curators bind when the
observation *is* one concept and fall back to prose when it is several. That is
the correct instinct, and it is not a vocabulary gap.

The corollary is the actionable part: **broadening the vocabulary addresses at
most the ~135 single-concept unbound findings, not the ~190 post-composed
ones.** Even a perfect merged HP+NCIT morphology vocabulary would leave the
majority of the tail unbindable, because no ontology pre-composes
"2,8-DHA crystals *with* chronic tubulointerstitial injury".

## The unused machinery

`HistopathologyFindingDescriptor` `is_a: Descriptor`, so it already inherits
`located_in` (UBERON), `modifier`, `laterality`, `spatial_extent`, and
`severity` — exactly the axes those compound labels are informally encoding in
prose. **Not one of the 707 findings uses any of them.** Every `finding_term` in
the KB is a bare `{preferred_term, term?}` pair.

This looks like a documentation gap rather than a modeling one. Compare the two
sibling classes in `src/dismech/schema/dismech.yaml`:

- `ImagingFindingDescriptor` — its description explicitly says *"Inherits
  located_in (UBERON body site), laterality, spatial_extent, and modifier from
  Descriptor for post-composition"*, and its comments tell curators where body
  site and distribution go.
- `HistopathologyFindingDescriptor` — says only which branches `term` may bind
  to. Post-composition is never mentioned, in the class, in `CLAUDE.md`, or in
  any worked example.

So curators had no signal that the compound case had a structured home, and
prose was the only available answer.

## What this suggests for #5140's options

Offered as input to the maintainer decision, not as a decision:

- **Option B (broaden the HP root) is worth doing but is not the coverage win
  it looks like** — it is scoped to roughly the 135 single-concept findings.
  Whatever root is chosen, the "NCIT vs HP" selection rule the issue asks for in
  question 1 still has to be written, because the two vocabularies do overlap in
  that single-concept space.
- **A fifth option belongs on the table: head term + post-composition.** Bind
  the head concept (which NCIT usually *does* have — infiltrate, crystal
  deposition, demyelination, keratinocyte necrosis) and carry site, cell type,
  distribution, and severity in the inherited `Descriptor` slots, instead of
  hunting for a pre-composed code that does not exist. This needs no schema
  change — only a documented convention, a worked example, and the
  `ImagingFindingDescriptor`-style note on the class. It is also the option most
  consistent with §10's stated test, which turns on whether a *term* exists, not
  on whether a *sentence* does.
- **Question 4 (entity-level "findings" → `disease_term`/subtype) remains
  independent** of the vocabulary question and can be settled separately, as the
  earlier triage comment noted.

## Caveats

- "Compound" is a syntactic heuristic (clause joiners, commas, slashes, or more
  than four words), not a semantic judgement; it is stated in
  `scripts/histopathology_binding_census.py` and can be tuned there. It will
  misfile a genuinely single-concept term with a long name, and will miss a
  two-concept label written tersely. The 58%-vs-20% *contrast* between the
  unbound and bound halves is the robust signal, not the exact percentage.
- The census counts binding, not binding *quality*. A finding bound to an
  over-broad NCIT term counts as bound here. Assessing whether the 382 bound
  terms are specific enough is separate work.
- No claim is made that any specific unbound finding *has* an available HP or
  NCIT term — testing that requires per-term ontology lookup and was out of
  scope for an offline census.
