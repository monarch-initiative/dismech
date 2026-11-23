---
title: MMRRC Mouse Models
status: IN_PROGRESS
tags: [MODELS, ANIMAL_MODELS, MOUSE, MMRRC, MGI]
description: Make dismech's mouse models identifiable as MMRRC lines (MGI allele + repository stock), and use the join to prioritise mouse-model curation for the MMRRC-Monarch event at UNC on 2026-12-10.
diseases:
  - Wilsons_Disease
  - Gorlin_Syndrome
---

# MMRRC Mouse Models

## Goal

The MMRRC wants a report, for any mouse line it holds, on how well that line
models disease mechanisms: to help decide whether to keep a line, and to ship
with the mouse when it is requested.

dismech already records *what* mice model. Of 2,588 mouse `animal_models`
records, 2,250 link to pathograph nodes through `modeled_mechanisms`. It does
not record *which* mouse: about 2% carry any MGI identifier and none names a
repository stock. This project closes that gap and uses the MMRRC catalogue to
decide what to curate first.

## The join

`just mmrrc-fetch` downloads MMRRC's holdings from IMSR (findmice.org) and MGI's
mouse-to-HGNC report into `data/mmrrc/` (gitignored, ~0.5 GB).
`just mmrrc-join` sorts every MMRRC mouse line into a bucket:

| Bucket | Meaning | Work |
|---|---|---|
| `BIND` | A dismech entry whose causal gene is this line's ortholog already has a mouse record naming the gene | Read both. If it is the same allele, add the MGI allele and stock; if not, add the line as a new record |
| `ADD` | The ortholog is a causal gene of a dismech entry, but no mouse record there names it | Add an `animal_models` record with `modeled_mechanisms` |
| `CURATE` | The ortholog is not a causal gene of any entry | The disease goes to the stub queue first |
| `MULTI_GENE` | More than five genes: mostly Beutler-lab ENU pedigrees (`Mtgx…Btlr`), plus deletions and consomics | Not gene models; out of scope for now |
| `NO_ORTHOLOG` | No gene with an HGNC ortholog after excluding tool alleles | Out of scope |

"Causal gene" means a `genetic[]` row typed `CAUSATIVE`, `SOMATIC_DRIVER` or
untyped, or a `has_subtypes[].genes` binding. The join excludes alleles that do
not model their host gene: construct knock-ins at docking loci (`Hprt1`,
`Col1a1`, `H11`, `Tigre`), reporter and Cre transgenes such as GENSAT's
`Tg(Ptch1-EGFP)EZ56Gsat`, and the `A<tm1Brd>` coat-colour marker in KOMP lines.

**A row is a lead, never a binding.** A `BIND` row says the gene matches. In a
spot check of six, some were plausibly the same model (`Kcnj10<tm1Lst>` for the
EAST syndrome knockout) and others were a different allele of the same gene
(`Irak4<m1Btlr>`, an ENU allele, against an `Irak4`-null record). Every MGI and
MMRRC identifier written into the KB is read from MGI or MMRRC in the same step.

## Census (IMSR fetched 2026-11-23)

IMSR lists 69,785 MMRRC holdings; 23,373 are mouse lines (live or cryopreserved)
and the rest exist only as ES cells.

| Bucket | Lines | Human genes |
|---|---:|---:|
| `BIND` | 1,500 | 852 |
| `ADD` | 2,512 | 1,603 |
| `CURATE` | 8,790 | 6,669 |
| `MULTI_GENE` | 7,740 | — |
| `NO_ORTHOLOG` | 2,831 | — |

About 4,000 lines (`BIND` + `ADD`) touch a disease dismech already curates.
Several large entries with many MMRRC lines have **no mouse records at all**,
among them Dilated_Cardiomyopathy, Congenital_Heart_Disease,
Genetic_Developmental_and_Epileptic_Encephalopathy and
Charcot-Marie-Tooth_Disease_Type_2.

**Flagship check.** MMRRC holds no orderable *Atp7b* line (ES cells only), so
Wilson disease's classic mouse models are held elsewhere. Gorlin syndrome's
MMRRC lines are *Sufu* and *Ptch2* KOMP/EUCOMM alleles; no *Ptch1* mutant line.
The CZI flagship list and the MMRRC-first queue therefore only partly overlap,
and the flagships need non-MMRRC mice (JAX, published lines) as well.

## Plan to 2026-12-10

- [x] Join MMRRC holdings to dismech (`scripts/mmrrc_fetch.py`, `scripts/mmrrc_join.py`)
- [ ] Schema: MGI allele IDs, repository stock IDs and background strain on `AnimalModel` (`extend-schema`)
- [ ] `/claim-mouse-model` skill: claim issues titled by MGI allele ID
- [ ] Work `BIND` rows, then `ADD` rows, ordered by knowledge-gap relevance and uniqueness
- [ ] Flagship worked examples: Wilson, Gorlin
- [ ] Per-mouse report prototype for the event

Background and prioritisation rationale: the "Mice in the Pathograph" explainer
shared with the MMRRC-Monarch group.
