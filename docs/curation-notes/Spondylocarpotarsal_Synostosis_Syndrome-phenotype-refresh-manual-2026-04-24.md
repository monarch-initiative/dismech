---
provider: manual_pubmed_review
model: n/a
cached: false
start_time: '2026-04-19T07:05:00Z'
end_time: '2026-04-19T07:27:31Z'
duration_seconds: 1351.0
citation_count: 8
notes: >
  Focused phenotype curation review for issue #1527. The goal was to tighten the
  SCTSS phenotype section to abstract-supported, HPO-grounded manifestations only,
  adding clinically important missing findings and softening unsupported strength
  claims.
---

## Question

What phenotype manifestations of spondylocarpotarsal synostosis syndrome are directly
supported by PubMed abstracts and should be represented in the phenotype section of
`kb/disorders/Spondylocarpotarsal_Synostosis_Syndrome.yaml`?

## Output

# SCTSS phenotype curation summary

## Core axial and appendicular skeletal findings retained

- Disproportionate short stature
- Vertebral fusion
- Block vertebrae
- Carpal synostosis / coalition
- Tarsal synostosis / coalition
- Scoliosis
- Lordosis / hyperlordosis

## Clinically important additional phenotypes supported by abstracts

- Short neck
- Delayed ossification of carpal bones
- Hearing impairment
- Joint stiffness / joint limitation
- Clinodactyly
- Pes planus
- Enamel hypoplasia
- Cleft palate
- Round face

## Claims intentionally softened or avoided

- Frequency qualifiers were omitted because the available abstracts mostly support
  disease-phenotype association rather than whole-disease frequency bands.
- Onset qualifiers were omitted because age-of-onset detail was generally in full text
  rather than the abstract.
- Sensorineural hearing loss was broadened to hearing impairment because the abstract
  literature supports conductive, mixed, and sensorineural forms across different
  reports.
- Short trunk, clubfoot, pectus carinatum, winged scapula, rib anomalies, coxa valga,
  gait difficulty, and ophthalmologic compromise were reviewed but not promoted into the
  final phenotype list because they were either difficult to ground cleanly to HPO with
  the available abstract evidence or appeared too family-specific for the narrow
  phenotype refresh requested here.

## References

- PMID:10766994
- PMID:17635842
- PMID:18257094
- PMID:18470895
- PMID:28145000
- PMID:29566257
- PMID:37781000
- PMID:39086440
