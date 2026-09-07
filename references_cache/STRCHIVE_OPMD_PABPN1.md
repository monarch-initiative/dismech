---
reference_id: "STRCHIVE:OPMD_PABPN1"
title: "PABPN1 — Oculopharyngeal muscular dystrophy"
database: "STRchive"
content_type: "structured_record"
---

# STRCHIVE:OPMD_PABPN1  PABPN1 — Oculopharyngeal muscular dystrophy

**STRCHIVE:OPMD_PABPN1** — STRchive tandem-repeat disease locus `OPMD_PABPN1` (PABPN1, Oculopharyngeal muscular dystrophy).

## Locus

- STRchive ID: OPMD_PABPN1
- Gene: PABPN1
- Gene strand: +
- Disease: Oculopharyngeal muscular dystrophy
- Disease abbreviation: OPMD
- Location type: Coding
- Location in gene: Exon 1
- Inheritance: AD (Autosomal dominant), AR (Autosomal recessive)
- Mechanism: GoF/LoF

## Repeat

| Field | Value |
|---|---|
| Reference motif (reference orientation) | GCN |
| Pathogenic motif (reference orientation) | GCN |
| Pathogenic motif (gene orientation) | CNG |
| Motif length (bp) | 3 |
| Locus structure | (GCN)* |
| Reference copies | 7 |

## Repeat-count thresholds

Allele repeat counts (number of motif copies) by pathogenicity category. Bounds are inclusive as reported by STRchive; a blank bound is unbounded or not documented.

| Category | Min copies | Max copies |
|---|---|---|
| Benign | 10 | 10 |
| Intermediate | 11 | 11 |
| Pathogenic | 12 | 18 |

## Genomic coordinates

| Build | Chrom | Start | Stop |
|---|---|---|---|
| hg38 | chr14 | 23321472 | 23321502 |
| hg19 | chr14 | 23790681 | 23790711 |
| T2T-chm13 | chr14 | 17522488 | 17522518 |

## Disease description

Ptosis and dysphagia [@pmid:39349043]; facial weakness, ptosis [@pmid:38876750].

## Mechanism

Polyalanine expansions leading to cellular toxicity (loss of function) as well as abnormal aggregation and inefficient protein degradation, which may impact mRNA processing [@genereviews:NBK1126].

## Age of onset

Typical: 40-59 [@pmid:37519616]; Range: 20-79 [@pmid:35112761].

## Prevalence

- Prevalence: 1/100000
- Details: 1/100,000 (population specific) [@pmid:29100084]. Frequency of (GCN)11 alleles is 1-2% of North America/Europe/Japan [@genereviews:NBK1126]. Disease is found worldwide, in more than 30 countries [@genereviews:NBK1126].

## Details

Disease is caused by a GCN polyalanine expansion in the first exon of PABPN1. Most known patients have (GCG)+, but GCN (any polyalanine) may be pathogenic [@genereviews:NBK1126]. This locus acts in a dominant manner for allele sizes ≥ 12 GCN motifs (90% of cases) and in a recessive manner for 11 GCN motifs, i.e. the genotype (GCN)11(GCN)11 (10% of cases). Additionally, disease is known to be more severe in cases of two expanded alleles. Age of onset is inverse to allele size, while penetrance and severity increase with allele size [@genereviews:NBK1126]. Mild, late-onset disease can occur in individuals with a (GCN)10(GCN)11 genotype, suggesting variable penetrance [@pmid:28011929]. The definition of this locus differs in the literature with prior work counting exact GCG motifs for a benign size of (GCG)6 [@pmid:9462747], while later resources count GCNs (any alanine codon), widening the region by 4 motifs to a benign size of (GCN)10 [@genereviews:NBK1126; @pmid:39349043]. STRchive is using the GCN definition.

## Tags

- Locus tags: length_affects_onset, length_affects_severity

## Cross-references

| Database | ID |
|---|---|
| MONDO | MONDO:0958176 |
| OMIM | OMIM:164300 |
| Orphanet | ORPHA:270 |
| MedGen | 1054618 |
| GARD | 7245 |
| MalaCards | OCL088 |
| GeneReviews | NBK1126 |
| gnomAD | PABPN1 |
| STRipy | PABPN1 |
| TR-Atlas | TR128439 |

## References

- pmid:37519616
- pmid:35112761
- genereviews:NBK1126
- pmid:28011929
- pmid:9462747
- pmid:39349043
- pmid:29100084
- pmid:38876750

## Source

STRchive (https://strchive.org), version **2.1.0** (snapshot 2026-07-23). A centralized catalog of tandem-repeat disease loci. Content is for research use and does not constitute medical guidance.

License: CC BY 4.0 (https://creativecommons.org/licenses/by/4.0/). This record is a reformatted and field-subset rendering of one locus from the STRchive `STRchive-loci.json` catalog; the source data are unmodified in substance.

[STRchive](https://strchive.org) · [source repository](https://github.com/hdashnow/STRchive)
