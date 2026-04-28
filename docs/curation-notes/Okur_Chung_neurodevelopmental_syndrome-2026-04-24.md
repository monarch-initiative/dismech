# Okur-Chung Neurodevelopmental Syndrome Curation Notes

Date: 2026-04-09

## Disease Anchoring

- Primary disease term used in the YAML entry: `MONDO:0014893` `Okur-Chung neurodevelopmental syndrome`
- Cross-references found locally in repo source tables:
  - `OMIM:617062`
  - `Orphanet:689422`
- Naming decision:
  - Entry title kept as `Okur-Chung Neurodevelopmental Syndrome`
  - Synonyms include `OCNDS`, `Okur-Chung syndrome`, and `CSNK2A1-related neurodevelopmental disorder`

## Curation Decisions

- Existing repo triage rows classify the gene-disease mechanism as gain of function, but the primary literature is more mixed.
- The YAML therefore treats OCNDS as a `CSNK2A1`-driven disorder with mechanistic heterogeneity:
  - reduced kinase activity for many missense variants
  - altered substrate specificity for at least some recurrent missense variants
  - probable haploinsufficiency for at least some null variants
- This avoids overcommitting to a single gain-of-function model not supported across the disease spectrum.

## Core Evidence Used

- `PMID:27048600`
  - Original disease-defining report
  - Established de novo `CSNK2A1` variants and core features
- `PMID:29383814`
  - 11-individual clinical study
  - Supports hypotonia, swallowing difficulty, and congenital heart defects
- `PMID:29240241`
  - 8 additional cases
  - Supports high prevalence of neurodevelopmental delay and multisystem involvement
- `PMID:33944995`
  - Functional variant study
  - Supports reduced CK2alpha kinase activity and abnormal localization
- `PMID:35517865`
  - Mechanistic study of recurrent `K198R`
  - Supports altered substrate specificity rather than complete loss of function
- `PMID:39367055`
  - Knock-in mouse model
  - Supports altered phosphoregulation, impaired synaptic maturation, and reduced hippocampal plasticity
- `PMID:39497417`
  - Recent phenotype expansion
  - Supports microcephaly as common but under-recognized
- `PMID:40677894`
  - Natural-history cohort
  - Supports conserved core phenotype, universal speech/language delay, and higher symptom burden in loop-region variants
- `PMID:38444259`
  - Familial null-variant report
  - Supports haploinsufficiency as a potential mechanism and milder null-variant phenotypes
- `PMID:37491870`
  - Familial transmission report
  - Supports autosomal dominant inherited OCNDS in addition to de novo disease
- `PMID:39070093`
  - Patient-organization roadmap
  - Used only for rarity framing and the statement that there are no approved disease-modifying treatments

## Sections Intentionally Omitted

- `treatments`
  - Omitted because current literature supports symptom management but not a validated disease-specific or disease-modifying intervention
- `biomarkers`
  - Omitted because mutation location is still presented as a potential or exploratory stratifier rather than a clinically established biomarker
- `progression`
  - Omitted because the available literature is stronger on core phenotype prevalence than on reproducible phase-based natural history staging

## Validation Targets

- Schema validation for the new YAML
- Reference validation against fetched PubMed cache
- Term validation for HPO, GO, CL, UBERON, HGNC, MONDO
