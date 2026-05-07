# Fontaine Progeroid Syndrome fallback research

## Scope

This fallback artifact supports the initial direct-Orpha curation of
Fontaine_Progeroid_Syndrome while provider-based deep research is attempted
with bounded timeouts. The entry focuses on the MONDO:0012853 / SLC25A24
Fontaine progeroid syndrome root and its Orphanet historical subtype records:
ORPHA:697101, ORPHA:2963, and ORPHA:2095.

## Structured sources

- ORPHA:697101: disease-level Fontaine progeroid syndrome record with exact
  OMIM:612289 mapping.
- ORPHA:2963: Progeroid syndrome, Petty type; includes exact MONDO:0012853,
  autosomal dominant inheritance, SLC25A24 gene association, epidemiology, and
  HPO phenotype-frequency rows.
- ORPHA:2095: Gorlin-Chaudhry-Moss syndrome; includes historical GCM synonyms,
  SLC25A24 gene association, epidemiology, and HPO phenotype-frequency rows.

## Primary literature used

- PMID:35679445 GeneReviews, "SLC25A24 Fontaine Progeroid Syndrome." Used for
  the current clinical definition, molecular diagnosis, autosomal dominant
  usually de novo inheritance, management, surveillance, and recurrence-risk
  counseling.
- PMID:29100093 Ehmke et al. 2017, AJHG. Used for recurrent de novo SLC25A24
  variants, mitochondrial inner membrane ATP-Mg/Pi carrier function,
  patient-fibroblast mitochondrial swelling, low matrix ATP, oxidative-stress
  sensitivity, gain-of-pathological-function interpretation, and linkage to
  skeletal/connective-tissue development.
- PMID:29100094 Writzl et al. 2017, AJHG. Used for the Fontaine syndrome name,
  recurrent codon 217 SLC25A24 variants, ATP-Mg/phosphate exchange, substrate
  cavity and transporter-dynamics modeling, altered mitochondrial morphology,
  decreased proliferation, increased membrane potential, decreased ATP-linked
  oxygen consumption, and impaired mitochondrial ATP synthesis.
- PMID:31775791 Ryu et al. 2019. Used for integration of GCMS and
  Fontaine-Farriaux syndrome under Fontaine progeroid syndrome and long-term
  clinical follow-up.
- PMID:38980211 Pannier et al. 2024. Used for prenatal diagnosis, fetal
  phenotype extension, exome/genome diagnostic utility, and paternal SLC25A24
  mosaicism.
- PMID:36093452 Lally et al. 2022. Used for early-lethality summary.
- PMID:41271664 Riko et al. 2025. Used for neonatal mitochondrial disease and
  decreased mitochondrial respiratory chain enzyme activity.
- PMID:23686885 Rosti et al. 2013. Background historical GCM phenotype review;
  not required for the primary mechanism graph because Orphanet and SLC25A24
  molecular evidence cover the structured claims.

## Literature-scope notes

PubMed searches were run for "Fontaine progeroid syndrome",
"Gorlin-Chaudhry-Moss syndrome", "Petty Laxova Wiedemann syndrome", and
"SLC25A24 progeroid". The priority curation evidence was selected from
GeneReviews, the two 2017 AJHG molecular discovery papers, Orphanet structured
records, and later case reports that add prenatal, long-term follow-up,
lethality, mosaicism, or mitochondrial-disease information.

## Provider attempts

- 2026-05-07: `timeout 75s just research-disorder falcon
  Fontaine_Progeroid_Syndrome` timed out with signal 15 before producing an
  artifact.
- 2026-05-07: `timeout 75s just research-disorder openai
  Fontaine_Progeroid_Syndrome` timed out with signal 15 before producing an
  artifact.

Because both bounded provider attempts failed to return promptly, this curation
proceeds from the PubMed, GeneReviews, and Orphanet evidence above.
