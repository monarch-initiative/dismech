# PTEN Hamartoma Tumor Syndrome Deep Research Fallback

## Provider Attempts

- `timeout 120s just research-disorder falcon PTEN_Hamartoma_Tumor_Syndrome`
  - Result: timed out with exit code 124 after starting
    `research/PTEN_Hamartoma_Tumor_Syndrome-deep-research-falcon.md`.
- `timeout 120s just research-disorder openai PTEN_Hamartoma_Tumor_Syndrome`
  - Result: timed out with exit code 124 after starting
    `research/PTEN_Hamartoma_Tumor_Syndrome-deep-research-openai.md`.

## Evidence Scope Used

The curation used direct structured Orphanet evidence and cached PubMed /
ClinicalTrials evidence rather than waiting further on provider output:

- ORPHA:306498 for disease definition, inheritance, prevalence, subtypes, and
  non-malignant manifestations.
- PMID:18781191 for the core PTEN loss -> PI3K/AKT/mTOR activation mechanism.
- PMID:20301661 for GeneReviews clinical characteristics, molecular diagnosis,
  inheritance, surveillance, genetic counseling, and subtype descriptions.
- PMID:33140411 for age-, sex-, and cancer-type-specific PHTS malignancy risks
  and surveillance support.
- PMID:31609537 for childhood PHTS, overgrowth, intellectual disability,
  macrocephaly-autism/developmental delay, and tumor-predisposition spectrum.
- PMID:26564076 for the broad neurodevelopmental spectrum including autism.
- PMID:35594551 and clinicaltrials:NCT02991807 for the phase II everolimus
  randomized trial.

## Scope Confirmation

The YAML intentionally centers on the syndrome-group PHTS entry rather than the
already-curated Cowden syndrome file. It includes PTEN as the defining causative
gene, the major Orphanet/GeneReviews subtype spectrum, core mechanism nodes,
representative non-malignant manifestations, major cancer-risk phenotypes,
diagnostic PTEN testing, surveillance, genetic counseling, and the completed
everolimus trial.
