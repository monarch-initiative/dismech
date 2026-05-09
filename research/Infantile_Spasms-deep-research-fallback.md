# Infantile Spasms Deep Research Fallback

## Provider attempts

- `timeout 75s just research-disorder falcon Infantile_Spasms`
  - Result: timed out with `Recipe research-disorder was terminated by signal 15`.
- `timeout 75s just research-disorder openai Infantile_Spasms`
  - Result: timed out with `Recipe research-disorder was terminated by signal 15`.

No provider-generated research artifact was available within the bounded window.

## Evidence-backed curation scope

The entry was curated from deterministic generated caches and primary/secondary biomedical sources:

- Orphadata structured records:
  - `ORPHA:697160` Infantile epileptic spasms syndrome, including inheritance, genes, phenotypes, and cross-references.
  - `ORPHA:3451` West syndrome legacy exact mapping to `MONDO:0018097`.
- PubMed caches:
  - `PMID:35503712` ILAE classification and definition of epilepsy syndromes with onset in neonates and infants.
  - `PMID:39029407` Danish national IESS epidemiology and outcome cohort.
  - `PMID:27838190` ICISS randomized trial of hormonal therapy with or without vigabatrin.
  - `PMID:16239177` UKISS randomized trial follow-up comparing hormone treatment and vigabatrin.
  - `PMID:31903560` prednisolone/prednisone versus ACTH RCT meta-analysis.
  - `PMID:35765990` network meta-analysis of first-line IESS treatments.
  - `PMID:22364326` vigabatrin monotherapy review, including mechanism and TSC-specific first-line use.
  - `PMID:37736852` current treatment-modality review and West syndrome triad wording.
- ClinicalTrials.gov caches:
  - `clinicaltrials:NCT04302116` vigabatrin plus high-dose prednisolone versus vigabatrin alone.
  - `clinicaltrials:NCT04289467` fenfluramine for refractory infantile spasms.

## Modeling notes

- ORPHA:697160 lists the generic HPO root `HP:0000707` Abnormality of the nervous system. It is intentionally documented in YAML notes rather than modeled as a phenotype because the entry includes more specific neurologic findings.
- Treatment modeling emphasizes first-line hormonal therapy, vigabatrin, and combination therapy because these have cached RCT/meta-analysis support.
- Refractory fenfluramine is represented as an active Phase II clinical trial rather than a standard treatment.
