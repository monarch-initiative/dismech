---
provider: manual_pubmed_review
model: n/a
cached: false
start_time: '2026-04-14T07:43:00Z'
end_time: '2026-04-14T07:58:00Z'
duration_seconds: 900.0
citation_count: 7
notes: >
  Automated provider run via `just research-disorder openai
  Blepharophimosis_Ptosis_and_Epicanthus_Inversus_Syndrome` was attempted first
  but stalled in this environment and did not produce an output file. Manual
  deep research was then completed from PubMed-backed cached references prior to
  curation.
---

## Question

Provide a concise but mechanistic review of blepharophimosis, ptosis, and
epicanthus inversus syndrome (BPES) as a disease-root entry with subtype
structure, causal gene, inheritance, core pathophysiology, hallmark phenotypes,
and management-relevant treatments.

## Output

# Blepharophimosis, Ptosis, and Epicanthus Inversus Syndrome: Mechanistic Summary

## Disease-root framing

BPES is best curated as a **disease root with subtype structure**, not as a flat
eyelid phenotype bucket. Recent clinical review data explicitly separate **BPES-I**
from **BPES-II** by the presence or absence of **primary ovarian insufficiency**
(PMID:41555764). Review literature also emphasizes that both subtypes share the
same congenital eyelid complex and that genotype alone does not fully determine
subtype assignment (PMID:33806295).

## Genetics and inheritance

BPES is a predominantly **autosomal dominant** disorder caused by heterozygous
pathogenic variants in **FOXL2** (PMID:33806295; PMID:20301614). FOXL2 is the
single causal anchor for the classic root disease and should be modeled as the
causative gene in the disorder entry.

## Core pathophysiology

Two mechanistic axes repeatedly emerge from the literature:

1. **Eyelid developmental dysregulation**
   FOXL2 variants impair transcriptional control of eyelid-development targets.
   Functional data show failure of mutant FOXL2 proteins to transactivate
   **OSR2**, which is consistent with the eyelid malformation phenotype
   (PMID:33796131).

2. **Ovarian reserve maintenance failure in Type I**
   FOXL2 dysfunction also affects ovarian biology. Functional assays show loss of
   FOXL2 repression on **CYP19A1** and **CCND2** promoters (PMID:31823134), and
   clinical cohorts demonstrate diminished ovarian reserve with adverse assisted
   reproductive technology outcomes in FOXL2-mutant BPES women (PMID:35574016).

Variant class influences severity but does not create a deterministic rule.
Truncating FOXL2 variants are enriched in BPES-I, whereas polyalanine-region
changes are more often associated with BPES-II (PMID:41555764; PMID:33806295).

## Hallmark phenotypes

The four cardinal BPES features present at birth are:

- Blepharophimosis
- Ptosis
- Epicanthus inversus
- Telecanthus

These are explicitly defined in GeneReviews (PMID:20301614). Associated ocular
features include **strabismus**, **refractive errors**, and **amblyopia**
(PMID:20301614). Type I additionally carries **primary ovarian insufficiency**
and **female infertility** risk (PMID:20301614; PMID:31823134).

## Treatment-relevant findings

Management is multidisciplinary and naturally separates into ocular and
reproductive domains:

- **Staged eyelid surgery**: medial canthoplasty for blepharophimosis,
  epicanthus inversus, and telecanthus, followed later by ptosis correction
  (PMID:20301614).
- **Frontalis suspension / canthoplasty approaches**: clinical series support
  staged canthoplasty plus frontalis suspension for correction of epicanthus,
  telecanthus, and coexisting blepharoptosis (PMID:35590300).
- **Hormone replacement therapy** for BPES-I-associated ovarian insufficiency
  (PMID:20301614).
- **Assisted reproductive technology** and fertility planning for affected women
  with FOXL2 mutations, though outcomes are heterogeneous (PMID:35574016;
  PMID:20301614).

## References

- PMID:20301614
- PMID:31823134
- PMID:33796131
- PMID:33806295
- PMID:35574016
- PMID:35590300
- PMID:41555764
