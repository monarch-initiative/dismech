---
provider: cyberian-codex
model: codex-local-synthesis
cached: true
start_time: "2026-04-14T08:20:00Z"
end_time: "2026-04-14T08:20:00Z"
duration_seconds: 0.0
template_file: codex_supplement_local
template_variables:
  disease_name: Bilateral Striopallidodentate Calcinosis
  category: Mendelian
citation_count: 13
source_providers:
- pubmed-manual
---

## Question

Codex secondary synthesis for disorder curation.

## Curation Summary

- Disease anchor: `MONDO:0008947` (`bilateral striopallidodentate calcinosis`), with exact MONDO synonyms including `PFBC`, `Primary Familial Brain Calcification`, and narrow synonym `Fahr disease`.
- Curation strategy: keep one disease/root page and document heterogeneity inside it. Do not split into multiple premature gene pages.
- YAML evidence policy: only PMID-backed abstract quotes that can survive `validate-references`.

## Disease Framing

- BSPDC/PFBC is the same broad disease spectrum for this curation purpose.
- The 2025 Brain review (`PMID:40344186`) states: `To date, seven genes have been linked to PFBC`.
- Recent literature supports two high-level subtype buckets for the parent page:
  - Autosomal dominant PFBC: `SLC20A2`, `XPR1`, `PDGFRB`, `PDGFB`
  - Autosomal recessive PFBC: `MYORG`, `JAM2`, `NAA60`
- I did not promote older, less stable candidate-gene mentions into the YAML unless I had direct and current PMID-backed support consistent with the current core-gene set.

## Mechanistic Synthesis

- Shared mechanism 1: phosphate transport dysregulation.
  - `SLC20A2` is the major dominant phosphate-import gene (`PMID:32506582`).
  - `XPR1` adds the complementary phosphate-export defect (`PMID:25938945`).
  - `NAA60` converges on the same axis by lowering cell-surface `SLC20A2` and extracellular phosphate uptake (`PMID:38480682`).
- Shared mechanism 2: neurovascular-unit dysfunction.
  - `PDGFB` / `PDGFRB` connect PFBC to endothelial-pericyte biology and blood-brain barrier maintenance (`PMID:23913003`, `PMID:23255827`).
  - `JAM2` makes the neurovascular-unit hypothesis explicit through impaired cell-cell adhesion (`PMID:31851307`).
  - `MYORG` is likely in the same broader pathway family, but the most validator-safe abstract wording is still more cautious (`PMID:30656188`).
- Emerging mechanistic theme not over-modeled in YAML:
  - `PMID:40344186` links `NAA60` and `SLC20A2` to Golgi integrity and highlights Golgi fragmentation as an emerging PFBC topic.

## Phenotype Synthesis

- Core parent-page phenotypes best supported by abstract-level quotes:
  - intracranial calcification / bilateral basal ganglia and extra-basal calcification
  - parkinsonism
  - cognitive impairment
  - psychosis / psychiatric presentation
- Heterogeneity point worth preserving:
  - recessive disease is generally more severe and can include seizures and heavier cortical involvement (`PMID:31851307`).
- I avoided overcommitting to additional phenotypes unless I had a clean HPO mapping plus an exact abstract sentence.

## Treatment Synthesis

- Current clinically supported treatment remains symptomatic rather than disease-modifying.
  - `PMID:39036637` supports dopaminergic replacement therapy for PFBC-associated parkinsonism.
- The strongest emerging precision-treatment paper is subtype-specific and preclinical.
  - `PMID:39121859` shows ASO-mediated splice correction as a potential therapy for `SLC20A2` haploinsufficiency.
- I kept treatment modeling conservative:
  - one symptomatic pharmacotherapy entry
  - one experimental ASO entry

## YAML Decisions

- Included:
  - one spectrum/root disorder page
  - two inheritance-level subtypes
  - seven causative genes with direct support
  - two shared mechanism nodes
  - four core phenotypes plus one recessive-severity phenotype
  - one symptomatic and one experimental treatment
- Deliberately not included:
  - separate gene-specific disorder pages
  - secondary/idiopathic basal ganglia calcification syndromes outside MONDO:0008947
  - weaker or unstable gene claims not anchored by current direct PMID evidence

## PMID Set Used For YAML

- PMID:23122487
- PMID:23255827
- PMID:23913003
- PMID:25938945
- PMID:29955172
- PMID:30656188
- PMID:31851307
- PMID:32506582
- PMID:38480682
- PMID:39036637
- PMID:39121859
- PMID:40344186

