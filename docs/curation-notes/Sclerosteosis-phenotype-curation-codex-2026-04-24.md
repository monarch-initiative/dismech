---
curator: codex
date: '2026-04-19'
issue: 1528
scope: phenotype section only
disease_file: kb/disorders/Sclerosteosis.yaml
---

# Sclerosteosis phenotype curation notes

## Core phenotype sources used

- PMID:12694228, "The natural history of sclerosteosis."
  - Strongest cohort source for phenotype frequency and course.
  - Usable abstract statements:
    - "Facial palsy and deafness, as a result of cranial nerve entrapment, developed in childhood in 52 (82%) affected persons."
    - "Mandibular overgrowth was present in 46 (73%) adults and syndactyly in 48 (76%)."
    - "Twenty-four from complications related to elevation of intracranial pressure as a result of calvarial overgrowth."
- PMID:11181578, "Increased bone density in sclerosteosis is due to the deficiency of a novel secreted protein (SOST)."
  - Best concise abstract for generalized skeletal sclerosis plus cranial nerve complications.
  - Usable abstract statements:
    - "Radiologically, it is characterized by a generalized hyperostosis and sclerosis leading to a markedly thickened and sclerotic skull"
    - "with mandible, ribs, clavicles and all long bones also being affected"
    - "Due to narrowing of the foramina of the cranial nerves, facial nerve palsy, hearing loss and atrophy of the optic nerves can occur."
    - "mainly differentiated by hand malformations and a large stature in sclerosteosis patients."
- PMID:223247, "Sclerosteosis in South Africa."
  - Useful for early clinical presentation.
  - Usable abstract statement:
    - "Early presenting features are syndactyly and facial palsy"
- PMID:11385236, "Syndactyly/brachyphalangy and nail dysplasias as marker lesions for sclerosteosis."
  - Best abstract for the morphology of the hand malformation.
  - Usable abstract statements:
    - "the presence of asymmetric cutaneous syndactyly of the index and middle fingers is characteristic."
    - "In many cases this syndactyly is associated with nail dysplasia"
- PMID:11570544, "Dental and oral manifestations of sclerosteosis."
  - Best abstract for mandibular enlargement.
  - Usable abstract statement:
    - "Gross asymmetrical hypertrophy of the mandible was present in all eight patients"
- PMID:7891385, "Sclerosteosis in a Spanish male: first report in a person of Mediterranean origin."
  - Useful corroboration for generalized bone sclerosis and tubular bone cortical widening.
  - Usable abstract statement:
    - "the typical radiological features, including generalised bone sclerosis and cortical widening of the tubular bones"
- PMID:8433139, "Sclerosteosis: neurosurgical experience with 14 cases."
  - Best abstract-level support for raised intracranial pressure as a presenting neurosurgical complication.
  - Usable abstract statement:
    - "presents with cranial nerve palsies and raised intracranial pressure"

## Curation decisions

- Kept phenotype additions restricted to claims explicitly supported in cached abstracts.
- Softened unsupported specificity:
  - `Sensorineural hearing impairment` -> `Hearing impairment`
  - `Facial nerve compression` -> `Facial palsy secondary to cranial hyperostosis`
- Added frequency only where a cohort abstract gave direct counts:
  - syndactyly
  - mandibular overgrowth / prognathia
- Added onset only where the abstract directly stated childhood development:
  - facial palsy
  - hearing impairment

## Findings not promoted to disease-level phenotype claims

- Drooling, mastication difficulty, partial anodontia, delayed eruption, and tori are evidence-backed in PMID:11570544 but come from a small eight-adult oral series; they were left out to keep the phenotype section centered on consistently replicated, clinically important manifestations.
- Headache, blurred vision, proptosis, and chin protrusion were seen in newer single-case reports, but the older cohort and mechanism papers already supported the broader disease-level manifestations more cleanly.
