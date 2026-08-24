---
reference_id: "STRCHIVE:CANVAS_RFC1"
title: "RFC1 — Cerebellar ataxia, neuropathy, and vestibular areflexia syndrome"
database: "STRchive"
content_type: "structured_record"
---

# STRCHIVE:CANVAS_RFC1  RFC1 — Cerebellar ataxia, neuropathy, and vestibular areflexia syndrome

**STRCHIVE:CANVAS_RFC1** — STRchive tandem-repeat disease locus `CANVAS_RFC1` (RFC1, Cerebellar ataxia, neuropathy, and vestibular areflexia syndrome).

## Locus

- STRchive ID: CANVAS_RFC1
- Gene: RFC1
- Gene strand: -
- Disease: Cerebellar ataxia, neuropathy, and vestibular areflexia syndrome
- Disease abbreviation: CANVAS
- Location type: Intronic
- Location in gene: Intron 2
- Inheritance: AR (Autosomal recessive)
- Mechanism: LoF

## Repeat

| Field | Value |
|---|---|
| Reference motif (reference orientation) | AAAAG |
| Pathogenic motif (reference orientation) | AAGGG, ACAGG, AGGGC, AAGGC, AGAGG |
| Pathogenic motif (gene orientation) | CCCTT, CCTGT, CCCTG, CCTTG, CCTCT |
| Benign motif (reference orientation) | AAAAG, AAAGG, AAGAG, AAAGGG |
| Motif length (bp) | 5 |
| Locus structure | (AAGGG)*(ACAGG)* |
| Reference copies | 11.8 |

## Repeat-count thresholds

Allele repeat counts (number of motif copies) by pathogenicity category. Bounds are inclusive as reported by STRchive; a blank bound is unbounded or not documented.

| Category | Min copies | Max copies |
|---|---|---|
| Benign | 0 | 11 |
| Intermediate | 11 | 200 |
| Pathogenic | 400 | 2750 |

## Genomic coordinates

| Build | Chrom | Start | Stop |
|---|---|---|---|
| hg38 | chr4 | 39348425 | 39348483 |
| hg19 | chr4 | 39350045 | 39350103 |
| T2T-chm13 | chr4 | 39318078 | 39318136 |

## Disease description

Sensory disturbances, imbalance, oscillopsia, chronic dry cough, dysarthria and dysphagia [@pmid:38876750]; Late-onset ataxia, sensory neuropathy, vestibular areflexia syndrome [@pmid:39349043].

## Mechanism

LoF; exact mechanism unknown [@pmid:38467784].

## Age of onset

Typical: 36-52; Range: 19-76 [@genereviews:NBK564656].

## Prevalence

- Details: Carrier frequency in European is 0.7-4% and in Chinese Han population is 2.24%; estimated prevalence of 1/20,000 to 1/625 [@genereviews:NBK564656]. Many cases are likely not diagnosed due to heterogeneous presentation [@pmid:39230846]. Observed in multiple ethnicities [@pmid:38876750]; patients diagnosed with European, Chinese Han, and Maori ancestry, as well as found in Japan, Canada, Brazil, the UK, Italy, Germany, and Australia [@genereviews:NBK564656].

## Details

Disease is caused by an insertion of a pathogenic motif, although motif presence is variable and can expand up to 200 repeats without apparently causing a phenotype [@genereviews:NBK564656]. Pathogenic expansions (ranging from 400-2750 pathogenic motifs) may be flanked by other motifs [@genereviews:NBK564656]. For example, (AAAGG)10-25(AAGGG)exp(AAAGG)4-6 [@pmid:32851396]. Motif heterogeneity is common in unaffected individuals [@genereviews:NBK564656], and motif associations are described by Delforge et al [@pmid:38627134]. The pathogenic size threshold appears to differ for the AAAGG motif: AAAGG expansions >= 600 repeats have been observed in CANVAS patients (vs 400 with established pathogenic motif AAGGG), while ~100-380 AAAGG repeats were found in unaffected controls [@pmid:37450567]. Length appears to impact age of onset and disease severity, with particular impact from the smaller allele [@doi:10.1136/jnnp-2024-ABN.259].

## Tags

- Locus tags: motif_affects_penetrance, length_affects_onset, length_affects_severity
- Disease tags: ataxia

## Cross-references

| Database | ID |
|---|---|
| MONDO | MONDO:0044720 |
| OMIM | OMIM:614575 |
| Orphanet | ORPHA:504476 |
| MedGen | 482853 |
| GARD | 17937 |
| MalaCards | CRB196 |
| GeneReviews | NBK564656 |
| gnomAD | RFC1 |
| STRipy | RFC1 |
| TR-Atlas | TR42349 |

## References

- genereviews:NBK564656
- pmid:38467784
- pmid:32851396
- pmid:38627134
- pmid:37450567
- doi:10.1136/jnnp-2024-ABN.259
- pmid:39230846
- pmid:38876750
- pmid:31230722
- pmid:39349043

## Source

STRchive (https://strchive.org), version **2.1.0** (snapshot 2026-07-23). A centralized catalog of tandem-repeat disease loci. Content is for research use and does not constitute medical guidance.

License: CC BY 4.0 (https://creativecommons.org/licenses/by/4.0/). This record is a reformatted and field-subset rendering of one locus from the STRchive `STRchive-loci.json` catalog; the source data are unmodified in substance.

[STRchive](https://strchive.org) · [source repository](https://github.com/hdashnow/STRchive)
