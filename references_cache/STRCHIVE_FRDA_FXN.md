---
reference_id: "STRCHIVE:FRDA_FXN"
title: "FXN — Friedreich ataxia"
database: "STRchive"
content_type: "structured_record"
---

# STRCHIVE:FRDA_FXN  FXN — Friedreich ataxia

**STRCHIVE:FRDA_FXN** — STRchive tandem-repeat disease locus `FRDA_FXN` (FXN, Friedreich ataxia).

## Locus

- STRchive ID: FRDA_FXN
- Gene: FXN
- Gene strand: +
- Disease: Friedreich ataxia
- Disease abbreviation: FRDA
- Location type: Intronic
- Location in gene: Intron 1
- Inheritance: AR (Autosomal recessive)
- Mechanism: LoF

## Repeat

| Field | Value |
|---|---|
| Reference motif (reference orientation) | GAA |
| Pathogenic motif (reference orientation) | GAA |
| Pathogenic motif (gene orientation) | AAG |
| Motif length (bp) | 3 |
| Locus structure | (A)*(GAA)* |
| Reference copies | 6 |

## Repeat-count thresholds

Allele repeat counts (number of motif copies) by pathogenicity category. Bounds are inclusive as reported by STRchive; a blank bound is unbounded or not documented.

| Category | Min copies | Max copies |
|---|---|---|
| Benign | 5 | 33 |
| Intermediate | 34 | 55 |
| Pathogenic | 56 | 1700 |

## Genomic coordinates

| Build | Chrom | Start | Stop |
|---|---|---|---|
| hg38 | chr9 | 69037286 | 69037304 |
| hg19 | chr9 | 71652202 | 71652220 |
| T2T-chm13 | chr9 | 81210843 | 81210861 |

## Disease description

Any Friedreich ataxia in which the cause of the disease is a mutation in the FXN gene [@mondo:0100340].

## Mechanism

Loss of function via transcriptional silencing [@pmid:16205714; @pmid:36169768].

## Age of onset

Typical: 10-15; Range: 2-80 [@genereviews:NBK1281].

## Prevalence

- Prevalence: 1/50000
- Details: 1/50,000 [@omim:229300; @pmid:29100084]: Known carrier frequency 1000/100,000; observed 421/100,000. Most common inherited ataxia in Europe, the Middle East, India, and North Africa; not documented in Southeast Asia, in sub-Saharan Africa, or among Native Americans [@genereviews:NBK1281].

## Details

96% of FA patients have biallelic GAA expansions in intron 1 (compared to compound heterozygous with another mutation type), in which the reference allele is conventionally 5-33 repeats [@genereviews:NBK1281]. Intermediate alleles (34-55) are associated with premutations, but may lead to disease as exact pathogenicity/penetrance thresholds have not been demarcated [@genereviews:NBK1281]. The expanded repeats can interrupted either with GAAGAG, GAAGGA, or GAAGAAAA sequences, leading to differential phenotypes [@pmid:11748752]. Allele size is correlated with disease severity and inversely correlated to age of onset, and expansions can reach 1700 repeats [@pmid:8815938].

## Tags

- Locus tags: somatic_instability, maternal_expansion, length_affects_onset, length_affects_phenotype, motif_affects_instability, motif_affects_onset, motif_affects_penetrance
- Disease tags: ataxia

## Cross-references

| Database | ID |
|---|---|
| MONDO | MONDO:0100340 |
| OMIM | OMIM:229300 |
| Orphanet | ORPHA:95 |
| MedGen | 383962 |
| GARD | 6468 |
| MalaCards | FRD001 |
| GeneReviews | NBK1281 |
| gnomAD | FXN |
| STRipy | FXN |
| TR-Atlas | TR93516 |

## References

- genereviews:NBK1281
- pmid:16205714
- pmid:36169768
- pmid:11748752
- pmid:8815938
- omim:229300
- pmid:29100084
- pmid:8596916
- mondo:0100340

## Source

STRchive (https://strchive.org), version **2.1.0** (snapshot 2026-07-23). A centralized catalog of tandem-repeat disease loci. Content is for research use and does not constitute medical guidance.

License: CC BY 4.0 (https://creativecommons.org/licenses/by/4.0/). This record is a reformatted and field-subset rendering of one locus from the STRchive `STRchive-loci.json` catalog; the source data are unmodified in substance.

[STRchive](https://strchive.org) · [source repository](https://github.com/hdashnow/STRchive)
