---
reference_id: "STRCHIVE:CJD_PRNP"
title: "PRNP — Creutzfeldt-Jakob disease"
database: "STRchive"
content_type: "structured_record"
---

# STRCHIVE:CJD_PRNP  PRNP — Creutzfeldt-Jakob disease

**STRCHIVE:CJD_PRNP** — STRchive tandem-repeat disease locus `CJD_PRNP` (PRNP, Creutzfeldt-Jakob disease).

## Locus

- STRchive ID: CJD_PRNP
- Gene: PRNP
- Gene strand: +
- Disease: Creutzfeldt-Jakob disease
- Disease abbreviation: CJD
- Location type: Coding
- Location in gene: Exon 2
- Inheritance: AD (Autosomal dominant)
- Mechanism: LoF?

## Repeat

| Field | Value |
|---|---|
| Reference motif (reference orientation) | GGTGGTGGCTGGGGGCAGCCTCAT |
| Pathogenic motif (reference orientation) | CCTCATGGTGGTGGCTGGGGGCAG |
| Pathogenic motif (gene orientation) | AGCCTCATGGTGGTGGCTGGGGGC |
| Motif length (bp) | 24 |
| Locus structure | (CCTCAGGGCGGTGGTGGCTGGGGGCAG)*(CCTCATGGTGGTGGCTGGGGGCAG)* |

## Repeat-count thresholds

Allele repeat counts (number of motif copies) by pathogenicity category. Bounds are inclusive as reported by STRchive; a blank bound is unbounded or not documented.

| Category | Min copies | Max copies |
|---|---|---|
| Benign | 4 | 4 |
| Intermediate | - | - |
| Pathogenic | 5 | 16 |

## Genomic coordinates

| Build | Chrom | Start | Stop |
|---|---|---|---|
| hg38 | chr20 | 4699397 | 4699493 |
| hg19 | chr20 | 4680043 | 4680139 |
| T2T-chm13 | chr20 | 4738633 | 4738705 |

## Disease description

Inherited or familial Creutzfeldt-Jakob disease (fCJD) is a very rare form of genetic prion disease characterized by typical CJD features (rapidly progressive dementia, personality/behavioral changes, psychiatric disorders, myoclonus, and ataxia) with a genetic cause and sometimes a family history of dementia [@mondo:0007403].

## Mechanism

Loss of function hypothesized [@pmid:38467784]

## Age of onset

Typical: 50-60 [@genereviews:NBK1229]; Range: 31-63 [@pmid:37379724].

## Prevalence

- Details: <0.0225/1,000,000: <15% of CJ variants are repeat expansions [@genereviews:NBK535148]. 15% newly diagnosed prion disease cases are genetic [@genereviews:NBK1229], 1 individual per million per year worldwide (350 cases annually in US) [@pmid:29939637]. Found worldwide [@genereviews:NBK1229].

## Details

Normal PRNP alleles have one nonapeptide followed by four octapeptide tandem repeat sequences, each of which comprises the  amino acids: Pro-(His/Gln)-Gly-Gly-Gly-(-/Trp)-Gly-Gln; any additional repeat leads to pathogenicity, with the largest repeat observed 16 motifs [@genereviews:NBK1229]. Insertion length may correspond to phenotype, such as CJD versus frontotemporal dementia [@pmid:36977684].

## Tags

- Locus tags: length_affects_phenotype

## Cross-references

| Database | ID |
|---|---|
| MONDO | MONDO:0007403 |
| OMIM | OMIM:123400 |
| Orphanet | ORPHA:282166 |
| MedGen | 155837 |
| GARD | 17307 |
| MalaCards | CRT072 |
| GeneReviews | NBK1229 |
| gnomAD | PRNP |
| TR-Atlas | TR157963 |
| TR-Atlas | TR157964 |

## References

- genereviews:NBK1229
- pmid:37379724
- pmid:38467784
- pmid:36977684
- genereviews:NBK535148
- pmid:29939637
- pmid:1683708
- mondo:0007403

## Source

STRchive (https://strchive.org), version **2.1.0** (snapshot 2026-07-23). A centralized catalog of tandem-repeat disease loci. Content is for research use and does not constitute medical guidance.

License: CC BY 4.0 (https://creativecommons.org/licenses/by/4.0/). This record is a reformatted and field-subset rendering of one locus from the STRchive `STRchive-loci.json` catalog; the source data are unmodified in substance.

[STRchive](https://strchive.org) · [source repository](https://github.com/hdashnow/STRchive)
