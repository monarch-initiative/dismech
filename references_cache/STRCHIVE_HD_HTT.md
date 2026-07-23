---
reference_id: "STRCHIVE:HD_HTT"
title: "HTT — Huntington disease"
database: "STRchive"
content_type: "structured_record"
---

# STRCHIVE:HD_HTT  HTT — Huntington disease

**STRCHIVE:HD_HTT** — STRchive tandem-repeat disease locus `HD_HTT` (HTT, Huntington disease).

## Locus

- STRchive ID: HD_HTT
- Gene: HTT
- Gene strand: +
- Disease: Huntington disease
- Disease abbreviation: HD
- Location type: Coding
- Location in gene: Exon 1
- Inheritance: AD (Autosomal dominant)
- Mechanism: GoF/LoF

## Repeat

| Field | Value |
|---|---|
| Reference motif (reference orientation) | CAG |
| Pathogenic motif (reference orientation) | CAG |
| Pathogenic motif (gene orientation) | AGC |
| Motif length (bp) | 3 |
| Locus structure | (CAG)*CAACAG(CCG)* |
| Reference copies | 21.3 |

## Repeat-count thresholds

Allele repeat counts (number of motif copies) by pathogenicity category. Bounds are inclusive as reported by STRchive; a blank bound is unbounded or not documented.

| Category | Min copies | Max copies |
|---|---|---|
| Benign | 6 | 26 |
| Intermediate | 27 | 39 |
| Pathogenic | 40 | 250 |

## Genomic coordinates

| Build | Chrom | Start | Stop |
|---|---|---|---|
| hg38 | chr4 | 3074877 | 3074940 |
| hg19 | chr4 | 3076604 | 3076667 |
| T2T-chm13 | chr4 | 3073604 | 3073694 |

## Disease description

Huntington disease (HD) is a rare neurodegenerative disorder of the central nervous system characterized by unwanted choreatic movements, behavioral and psychiatric disturbances and dementia [@mondo:0007739].

## Mechanism

While the primary pathogenic mechanism is gain of function of the protein product, pathogenesis is complex and multifactorial [@pmid:27940602].

## Age of onset

Typical: 35-44 [@genereviews:NBK1305]; Range: 1-85 [@pmid:39441074; @pmid:21171977].

## Prevalence

- Prevalence: 1/10000
- Details: 6.5-15/100,000 [@pmid:29100084]. 9.71-17:100,000 (European) vs. 0.1-2/100,000 (African), as many as 1 in 400 have reduced penetrance (0.2-2% for 36-38 CAG) HTT alleles [@genereviews:NBK1305]. Found across ethnicities/ancestries, with population-dependent prevalence [@genereviews:NBK1305].

## Details

27-35 motifs are unstable/premutations, while 36-39 motifs are associated with reduced penetrance and mild phenotypes [@pmid:39572770]. >60 motifs assocated with onset age <20 years [@genereviews:NBK1305]. Only CAG expansions are considered pathogenic, but interruptions impact pathogenicity (e.g. CAA) [@pmid:35245110]. Only fathers with premutations are considered at risk of transmitting pathogenic alleles [@pmid:19507258]. CAG repeats in the non-HD range (>= 21 repeats) may modulate psychiatric disease risk in an age-dependent manner [@pmid:39572770]

## Tags

- Locus tags: somatic_instability, anticipation, paternal_expansion, length_affects_onset, length_affects_penetrance, length_affects_phenotype, length_affects_severity, motif_affects_instability, motif_affects_onset, motif_affects_penetrance, proposed_modifier

## Cross-references

| Database | ID |
|---|---|
| MONDO | MONDO:0007739 |
| OMIM | OMIM:143100 |
| Orphanet | ORPHA:399 |
| MedGen | 5654 |
| GARD | 6677 |
| MalaCards | HNT016 |
| GeneReviews | NBK1305 |
| gnomAD | HTT |
| STRipy | HTT |
| TR-Atlas | TR40017 |
| TR-Atlas | TR40018 |

## References

- genereviews:NBK1305
- pmid:39441074
- pmid:21171977
- pmid:27940602
- pmid:39572770
- pmid:35245110
- pmid:19507258
- pmid:29100084
- pmid:8458085
- mondo:0007739

## Source

STRchive (https://strchive.org), version **2.1.0** (snapshot 2026-07-23). A centralized catalog of tandem-repeat disease loci. Content is for research use and does not constitute medical guidance.

License: CC BY 4.0 (https://creativecommons.org/licenses/by/4.0/). This record is a reformatted and field-subset rendering of one locus from the STRchive `STRchive-loci.json` catalog; the source data are unmodified in substance.

[STRchive](https://strchive.org) · [source repository](https://github.com/hdashnow/STRchive)
