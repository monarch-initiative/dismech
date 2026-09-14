---
reference_id: "STRCHIVE:DM2_CNBP"
title: "CNBP — Myotonic Dystrophy Type 2"
database: "STRchive"
content_type: "structured_record"
---

# STRCHIVE:DM2_CNBP  CNBP — Myotonic Dystrophy Type 2

**STRCHIVE:DM2_CNBP** — STRchive tandem-repeat disease locus `DM2_CNBP` (CNBP, Myotonic Dystrophy Type 2).

## Locus

- STRchive ID: DM2_CNBP
- Gene: CNBP
- Gene strand: -
- Disease: Myotonic Dystrophy Type 2
- Disease abbreviation: DM2
- Location type: Intronic
- Location in gene: Intron 1
- Inheritance: AD (Autosomal dominant)
- Mechanism: GoF

## Repeat

| Field | Value |
|---|---|
| Reference motif (reference orientation) | CAGG |
| Pathogenic motif (reference orientation) | CAGG |
| Pathogenic motif (gene orientation) | CCTG |
| Motif length (bp) | 4 |
| Locus structure | (CAGG)*(CAGA)*(CA)* |
| Reference copies | 20.8 |

## Repeat-count thresholds

Allele repeat counts (number of motif copies) by pathogenicity category. Bounds are inclusive as reported by STRchive; a blank bound is unbounded or not documented.

| Category | Min copies | Max copies |
|---|---|---|
| Benign | 11 | 26 |
| Intermediate | 27 | 74 |
| Pathogenic | 75 | 11000 |

## Genomic coordinates

| Build | Chrom | Start | Stop |
|---|---|---|---|
| hg38 | chr3 | 129172577 | 129172659 |
| hg19 | chr3 | 128891420 | 128891502 |
| T2T-chm13 | chr3 | 131917483 | 131917557 |

## Disease description

Myotonic dystrophy type 2 (MD2), also known as proximal myotonic myopathy, is a very rare genetic multi-system disorder of late childhood or adult-onset characterized by mild myotonia, muscle weakness, and rarely cardiac conduction disorders [@mondo:0011266].

## Mechanism

Aberrant splicing, RAN translation [@pmid:22140091; @pmid:38467784].

## Age of onset

Typical: 28-56 [@pmid:29086017]; Range: 0-73 [@pmid:31159885].

## Prevalence

- Prevalence: 2.29/100000
- Details: 2.29/100,000 [@pmid:35483324]; population specific prevalence [@genereviews:NBK1466]. Most cases have European ancestry, but disease has been reported worldwide [@genereviews:NBK1466].

## Details

Detailed overview of disease locus through 2024 by Rimoldi et al [@pmid:39643839]. ≤30 uninterrupted CCTG repeats or 11-26 CCTG repeats with GCTC/TCTG interruptions are considered benign; 27-29 repeats with interruptions have currently unknown significance, ~30-~54 repeats are considered premutations, ~55-74 repeats are premutations with possible reduced penetrance, and >74 repeat alleles are considered pathogenic [@genereviews:NBK1466]. Penetrance is age-dependent and approaches 100%. Locus structure is (TG)n(TCTG)n(CCTG)n. CCTG expansion causes DM2 but the other repeat units are also variable. Interruptions include GCTG/TCTG/GGCT [@pmid:35245110]. The effect of the (TCTG)n repeat remains to be determined, but it is potentially common in the repeat structure of this locus [@pmid:39703464].

## Tags

- Locus tags: somatic_instability, motif_affects_instability
- Disease tags: myotonic_dystrophy

## Cross-references

| Database | ID |
|---|---|
| MONDO | MONDO:0011266 |
| OMIM | OMIM:602668 |
| Orphanet | ORPHA:606 |
| MedGen | 419137 |
| GARD | 9728 |
| MalaCards | MYT020 |
| GeneReviews | NBK1466 |
| gnomAD | CNBP |
| STRipy | CNBP |
| TR-Atlas | TR35563 |
| TR-Atlas | TR35564 |
| TR-Atlas | TR35565 |

## References

- pmid:29086017
- pmid:31159885
- pmid:22140091
- pmid:38467784
- pmid:39643839
- genereviews:NBK1466
- pmid:35245110
- pmid:35483324
- pmid:11486088
- mondo:0011266

## Source

STRchive (https://strchive.org), version **2.1.0** (snapshot 2026-07-23). A centralized catalog of tandem-repeat disease loci. Content is for research use and does not constitute medical guidance.

License: CC BY 4.0 (https://creativecommons.org/licenses/by/4.0/). This record is a reformatted and field-subset rendering of one locus from the STRchive `STRchive-loci.json` catalog; the source data are unmodified in substance.

[STRchive](https://strchive.org) · [source repository](https://github.com/hdashnow/STRchive)
