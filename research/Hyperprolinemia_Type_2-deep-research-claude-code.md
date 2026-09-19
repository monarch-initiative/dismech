# Hyperprolinemia Type 2 (ALDH4A1, MONDO:0009401) — Claude Code literature sweep

**Date:** 2026-07-31
**Tool:** Claude Code (curation scanner, high_effort tier)
**Target entry:** `kb/disorders/Hyperprolinemia_Type_2.yaml`
**Context:** review follow-up on PR #7338 (issue #5558, IEMbase WP-003 row 1.7.06.01)

This artifact records a systematic literature sweep run *after* the initial
entry was drafted, in response to review finding #1 on PR #7338 ("no
deep-research artifact ships with this new entry, and findings 2–4 are all
things a literature sweep would have surfaced"). It documents what was
searched, what was found, and — importantly — which candidate papers were
inspected and deliberately **not** used.

## Method

PubMed E-utilities `esearch`, relevance-sorted, `retmax=40`, three
complementary queries chosen to catch gene-anchored, disease-name-anchored, and
enzyme-anchored literature respectively:

| Query | Hits | Retrieved |
|---|---|---|
| `ALDH4A1` | 89 | 40 |
| `hyperprolinemia type II` | 61 | 40 |
| `pyrroline-5-carboxylate dehydrogenase deficiency` | 30 | 30 |

Titles for every PMID appearing in the union that was **not** already cited by
the entry were retrieved via `esummary` and triaged. Every paper selected for
use was then fetched with `just fetch-reference` and each snippet verified as
an exact substring of the cached abstract via `just validate-references`.

## Baseline check

**GeneReviews: none exists.** Confirmed independently in the PR review — both
`hyperprolinemia[TI] AND GeneReviews[Book]` and
`(hyperprolinemia OR ALDH4A1 OR "pyrroline-5-carboxylate dehydrogenase") AND GeneReviews[Book]`
return zero results against a working control. No GeneReviews baseline
requirement applies to this entry.

**Orphanet:** `ORPHA:79101` cached via `just structured-rebuild-orphanet --id 79101`.
The record carries a definition and cross-references but **no HPO phenotype
table**, so it cannot supply frequency annotations for this disorder. Its
definition sentence is used as an evidence snippet for the
intellectual-deficit / developmental-delay phenotypes.

## Papers newly incorporated

### PMID:24173411 — van de Ven 2014, *J Inherit Metab Dis*
The largest HPII series in the literature: 4 metabolically confirmed patients
ascertained from 20,991 urinary organic acid profiles. Supplies four things the
entry lacked:

1. **Counter-evidence to the pyridoxine claim** — "The clinical course was
   non-progressive and independent from the B6 concentration and B6 therapy."
   Curated as `supports: REFUTE` on the treatment, against the single
   supporting case report. The treatment is now presented as genuinely
   conflicting rather than established.
2. **Intellectual disability** — 2 of 4 patients.
3. **Behavioral phenotype** — 4 of 4 with "significant behavioral problems,
   including anxiety and hallucinations."
4. **The mitochondrial arm** — 3 of 4 with biochemical markers of
   mitochondrial dysfunction, biopsy-confirmed in one.

### PMID:34302426 — Namavar 2021, *Am J Med Genet B*
PRISMA systematic review, 1753 studies screened, 35 included. Reports a common
psychiatric phenotype (developmental delay, intellectual disability, ASD,
psychosis spectrum) and — critically — **no biochemical–clinical phenotype
correlation**. Used both as phenotype support and as the reason the
neurodevelopmental pathophysiology node is marked `HYPOTHETICAL`.

**Scope caveat, applied throughout:** this review pools hyperprolinemia types I
and II. Every citation of it in the entry is therefore `supports: PARTIAL`, and
the HPII-specific anchors (PMID:24173411, ORPHA:79101, PMID:41602883) carry the
`SUPPORT` weight.

### PMID:21168532 — He & DiMario 2011, *Mitochondrion*
Not flagged in the PR review; surfaced by the `ALDH4A1` and enzyme-anchored
queries. A Drosophila P5CDh-null model ("establishing a fly model for human
type II hyperprolinemia") showing doubled proline **together with swollen
mitochondria** and larval/pupal lethality. This is independent, cross-species
corroboration of the mitochondrial arm from a completely different system,
which is what justifies modeling that arm at all rather than treating the
human n=4 finding as noise. Tagged `MODEL_ORGANISM`. The authors' own
"first correlation between the loss of P5CDh and morphological defects in
mitochondria" framing is quoted to keep the node `PROVISIONAL`.

### PMID:41602883 — AlQurashi 2025, *Front Pediatr*
Also not flagged in the review; the most recent HPII case report. A
consanguineous Saudi child presenting with global developmental delay and
clinically diagnosed ASD, with a homozygous ALDH4A1 variant. Supplies the only
HPII-specific primary citation for developmental delay (previously resting on
the Orphanet definition alone).

**Caveat recorded in the entry:** the variant is of **uncertain significance**,
not an established pathogenic allele. The ASD phenotype is therefore curated as
two `PARTIAL` items with no frequency band, and the developmental-delay note
states the VUS status explicitly.

## Candidates inspected and NOT used

Recording these so a future curator does not re-triage them:

| PMID | Title | Why not used |
|---|---|---|
| 37141741 | PYCR2 deficiency causes hereditary spastic paraplegia | Different gene/disease (PYCR2, not ALDH4A1). Relevant to the deferred PYCR1/PYCR2 scoping question on #5558, not to this entry. |
| 23462603 | PRODH mutations in Korean neonates with type I hyperprolinemia | HPI, not HPII. |
| 24842239 | Long-term neuropsychiatric follow-up in hyperprolinemia type I | HPI, not HPII. Belongs to the future HPI entry. |
| 21643764 | Behavioral and neurochemical effects of proline | Proline-loading pharmacology, not HPII disease biology. |
| 28712849 | Structure, function, mechanism of proline utilization A (PutA) | Bacterial enzymology; entry already cites the human structural paper (PMID:22516612). |
| 18806117 | Inborn errors of proline metabolism | Review; adds no claim not already primary-sourced. |
| 26693506 | SAXS fingerprints of aldehyde dehydrogenase oligomers | Biophysics of the ALDH family generally, not disease-relevant. |
| 18062169 / 36980111 / 30930802 | Vitamin B6-related / B6-dependent epilepsies | Cover the *primary* B6-dependent epilepsies (ALDH7A1, PNPO). HPII causes a **secondary** B6 deficiency by a different route; citing these would blur a distinction the entry deliberately makes. |
| 25391710 | Schizophrenia/first-episode psychosis in children | General psychiatry; hyperprolinemia not the subject. |
| 9590014 | [Hyperprolinemia type II] | Japanese-language 1998 review; superseded by PMID:24931297, already cited. |

## Named Entity Confusion (NEC) preflight

Re-verified for this sweep, since "hyperprolinemia type II" is a numbered-series
label of exactly the kind flagged in `research/nec_risk_disease_classes.md`:

```
uv run runoak -i sqlite:obo:mondo info MONDO:0009401 -O obo
  relationship: RO:0004003 HGNC:406 ! ALDH4A1
  xref: OMIM:239510
  xref: Orphanet:79101
```

Gene, OMIM, and ORPHA all match WP-003 row 1.7.06.01. Every paper incorporated
above was checked to be about ALDH4A1/HPII specifically, with the HPI-pooling
caveat on PMID:34302426 handled by downgrading it to `PARTIAL`. **PASS.**

## Residual gaps after this sweep

Both are tracked as `KNOWLEDGE_GAP` discussions in the entry rather than left
implicit:

- `gap_hpii_plp_seizure_causality` — the PLP-depletion-causes-seizures model is
  now a matter of **conflicting** evidence, not absent evidence: one case
  reports B6-responsive seizures, the only cohort reports a course independent
  of B6 therapy. No controlled trial exists and none is likely at this
  prevalence.
- `gap_hpii_penetrance_and_phenotype` — no biochemical–clinical correlation has
  been demonstrated, so neither penetrance nor severity is predicted by proline
  level, and the modifiers remain unidentified.

A third gap is noted here but not curated as a discussion because it is a
literature-coverage limitation rather than a mechanistic one: **every clinical
statement about HPII rests on a total of roughly a dozen patients worldwide.**
No frequency bands are curated anywhere in the entry for this reason.
