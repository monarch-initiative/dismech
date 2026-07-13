# IEMbase 0712: TTC19-related mitochondrial complex III deficiency, nuclear type 2

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 712 |
| Nosology | 7.3.02.02 |
| Nosology code | IEM0459 |
| Gene | TTC19 |
| External IDs | OMIM:615157; ORPHA:1460 |
| Generated mapping | CANDIDATE to `COX11-Related_COX_Deficiency.yaml` |
| Candidate DisMech targets | No exact TTC19/MC3DN2 target identified |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents autosomal recessive TTC19-related mitochondrial complex III
deficiency, nuclear type 2. MONDO resolves this disease to the TTC19-specific
term mitochondrial complex III deficiency nuclear type 2 with OMIM:615157.

The cached phenotype rows show neonatal low-to-normal plasma glucose, increased
plasma lactate from neonatal through childhood windows, possible basal ganglia
MRI abnormalities and developmental delay from infancy onward, gait ataxia from
infancy through adulthood, possible neonatal hypoglycemia, and neonatal
metabolic acidosis.

## DisMech phenotype coverage

No exact TTC19 or MC3DN2 local target was identified.

The generated `COX11-Related_COX_Deficiency.yaml` candidate is a complex IV
copper-delivery disorder, not complex III TTC19 disease. Local CoQ10 and
ETFDH/MADD entries mention electron transfer into or through complex III, and
`HIDEA_Syndrome.yaml` includes unrelated complex III activity findings, but
none of these are exact TTC19 complex III deficiency coverage.

## Concordance and completeness

Judgement: true local complex III gap. The COX11 candidate should be rejected.

The IEMbase row points to a TTC19-specific complex III disorder with lactate,
basal ganglia/developmental findings, ataxia, hypoglycemia, and metabolic
acidosis. A complex IV COX entry is not an acceptable mapping despite
respiratory-chain overlap.

## Curation actions

- Add a dedicated TTC19/MC3DN2 target if curated.
- Reject `COX11-Related_COX_Deficiency.yaml` as exact coverage.
- Preserve lactate, low-to-normal glucose, hypoglycemia, metabolic acidosis,
  basal ganglia MRI abnormalities, developmental delay, and gait ataxia.
- Keep complex III deficiency distinct from complex IV COX deficiency.
