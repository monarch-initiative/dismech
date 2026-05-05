---
provider: codex_manual_pubmed_review
model: gpt-5
cached: false
start_time: '2026-04-19T01:45:00Z'
end_time: '2026-04-19T02:21:10Z'
duration_seconds: 2170.0
citation_count: 5
notes: >
  Phenotype-focused curation research for issue #1484. Primary aim was to expand
  the phenotype section with only exact PMID-backed manifestations and to avoid
  generalizing niche overlap findings beyond what the literature directly
  supports.
---

## Question

What phenotype manifestations of metatropic dysplasia are directly supported by
primary PMID-backed evidence and precise HPO mappings?

## Key sources reviewed

- PMID:20425821, Camacho et al. 2010. Core clinical and radiographic phenotype
  plus additional manifestations from the cached full text.
- PMID:21658220, Andreucci et al. 2011. Spectrum cohort including 15 metatropic
  dysplasia patients; useful for shared short stature/platyspondyly/progressive
  scoliosis language.
- PMID:19232556, Krakow et al. 2009. Nonlethal metatropic dysplasia within the
  TRPV4 spectrum; useful for progressive scoliosis, metaphyseal involvement, and
  carpal ossification delay.
- PMID:28321993, Theroux et al. 2017. Largest metatropic dysplasia anesthetic
  cohort; useful for spinal canal narrowing/stenosis and airway-related
  complications.
- PMID:21964829, Unger et al. 2011. Severe overlap phenotype with fetal akinesia
  and congenital contractures.

## Phenotypes selected for YAML curation

- Disproportionate short-limb short stature
  Evidence basis: PMID:20425821 plus PMID:21658220.
- Kyphoscoliosis
  Evidence basis: PMID:20425821.
- Platyspondyly
  Evidence basis: PMID:21658220.
- Joint contractures
  Evidence basis: PMID:20425821 full text.
- Hypoplasia of the odontoid process
  Evidence basis: PMID:20425821 full text.
- Spinal canal stenosis
  Evidence basis: PMID:28321993.
- Thoracic hypoplasia and neonatal respiratory distress
  Evidence basis: PMID:20425821 full text.
- Metaphyseal widening
  Evidence basis: PMID:20425821.
- Dumbbell-shaped long bones
  Evidence basis: PMID:20425821.
- Halberd-shaped pelvis
  Evidence basis: PMID:20425821.
- Brachydactyly
  Evidence basis: PMID:20425821.
- Delayed ossification of carpal bones
  Evidence basis: PMID:20425821 and PMID:19232556.
- Frontal bossing and midface retrusion
  Evidence basis: PMID:20425821.
- Sensorineural hearing impairment
  Evidence basis: PMID:20425821 full text.

## Manifestations reviewed but not generalized into the main phenotype list

- Fetal akinesia
  PMID:21964829 supports this in severe overlap cases caused by certain TRPV4
  variants, but the paper explicitly frames it as unusual and mutation-specific,
  so it was not generalized as a core phenotype of metatropic dysplasia.
- Difficult airway
  PMID:28321993 supports this as a peri-anesthetic management problem, but it is
  more a procedural consequence of the skeletal phenotype than a clean disease
  phenotype term for the YAML phenotype section.
- Squared-off jaw
  PMID:20425821 clearly mentions it, but I did not add it because the
  corresponding HPO grounding was less straightforward than the other
  craniofacial findings and the current issue prioritized well-grounded ontology
  specificity.
