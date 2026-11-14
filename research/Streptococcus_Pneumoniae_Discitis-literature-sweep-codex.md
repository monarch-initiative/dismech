# Streptococcus Pneumoniae Discitis literature sweep

- **Curator:** Codex
- **Date:** 2026-11-14
- **Disease:** streptococcus pneumoniae discitis
- **MONDO:** MONDO:8000003

## Scope and search

The stub was evaluated against the broader open `Infectious_Discitis` stub and
the existing `Staphylococcus_Discitis`, `Pneumococcal_Pneumonia`, and
`Pneumococcal_Meningitis` entries. The final curation treats MONDO:8000003 as a
rare organism/site leaf for invasive pneumococcal disease involving the
disc-endplate complex.

The local sweep used:

- `Streptococcus pneumoniae spondylodiscitis`
- `pneumococcal spondylodiscitis`
- `Streptococcus pneumoniae discitis`
- `spinal paraspinal pneumococcal infections`

## Mechanistic synthesis

The pneumococcal route is modeled as human upper-airway carriage followed by
invasive bloodstream spread and disseminated disc involvement by either direct
systemic bacteremia or extension through nearby abscesses. I did not copy the
S. aureus protein A / TNFR1 / RANKL osteoblast nodes from
`Staphylococcus_Discitis`, because the accessible pneumococcal discitis
literature supports the organism, bacteremic dissemination, local
spondylodiscitis, and epidural/paraspinal abscess manifestations but not an
equivalent pneumococcus-specific osteoblast signaling chain.

The core pneumococcal-specific review is PMID:24481748, which reports two
institutional cases plus 50 additional published spinal pneumococcal infection
cases. A 2024 open-access case report, PMID:38680822, was used for disseminated
penicillin-resistant pneumococcal disease with lumbar spondylodiscitis requiring
laminectomy/fenestration. Background reviews PMID:29599457 and PMID:21734248
support human upper-airway pneumococcal carriage and bloodstream invasion during
invasive pneumococcal disease.

## Open gaps

- No population incidence is recorded for pneumococcal discitis itself; the
  review supports only an ultra-rare cases-in-literature assertion.
- No molecular pneumococcus-specific vertebral osteomyelitis mechanism was
  curated because the discitis-specific literature is clinical.
- The broad `Infectious_Discitis` stub remains open as a future grouping parent
  for Staphylococcus, pneumococcal, Salmonella, E. coli, and fungal discitis
  leaves.

## Reference Validation

Checked with `linkml-reference-validator` 0.5.1.

| Outcome | Count |
| --- | --- |
| References checked | 4 |
| Resolved | 4 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 4 |
| On topic | 3 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 1 |
| Resolved | 1 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |

Every term resolved, and every label the report gave matched.
