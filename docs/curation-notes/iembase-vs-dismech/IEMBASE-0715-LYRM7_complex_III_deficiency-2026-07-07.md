# IEMbase 0715: LYRM7-related mitochondrial complex III deficiency, nuclear type 8

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 715 |
| Nosology | 7.3.04.01 |
| Nosology code | IEM0461 |
| Gene | LYRM7 |
| External IDs | OMIM:615838; ORPHA:1460 |
| Generated mapping | CANDIDATE to `TACO1-Related_COX_Deficiency.yaml` |
| Candidate DisMech targets | No exact LYRM7/MC3DN8 target identified |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents autosomal recessive LYRM7-related mitochondrial complex III
deficiency, nuclear type 8. MONDO resolves this disease to the LYRM7-specific
complex III deficiency nuclear type 8 term with OMIM:615838.

The cached rows emphasize increased plasma lactate in infancy and childhood,
cavitating leukodystrophy on MRI, developmental delay, episodic encephalopathy,
and hypotonia. A possible perinatal-death row is also present in the source
phenotype table.

## DisMech phenotype coverage

No exact LYRM7 or MC3DN8 local target was identified.

The generated `TACO1-Related_COX_Deficiency.yaml` candidate is a complex IV
COX I translation disorder, not a complex III LYRM7 disorder. The high fuzzy
score appears to be driven by the shared "nuclear type 8" phrasing across
different respiratory-chain complexes.

## Concordance and completeness

Judgement: true local complex III gap. The TACO1 candidate should be rejected.

The IEMbase record is specific for LYRM7/MC3DN8 and carries a neurologic,
leukodystrophy, lactate, and hypotonia phenotype signal. A complex IV TACO1
entry is not acceptable exact coverage despite the broad mitochondrial
respiratory-chain overlap.

## Curation actions

- Add a dedicated LYRM7/MC3DN8 target if curated.
- Reject `TACO1-Related_COX_Deficiency.yaml` as exact coverage.
- Preserve lactate elevation, cavitating leukodystrophy, developmental delay,
  episodic encephalopathy, hypotonia, and possible perinatal death.
- Keep complex III nuclear type 8 distinct from TACO1 complex IV nuclear type 8.
