# IEMbase 0728: SCO2-related myopia 6

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 728 |
| Nosology | 7.4.06.01 |
| Nosology code | IEM0474 |
| Gene | SCO2 |
| External IDs | OMIM:604377; OMIM:608908; ORPHA:98619 |
| Generated mapping | MAPPED to `SCO2-Related_Fatal_Infantile_Cardioencephalomyopathy.yaml` |
| Candidate DisMech targets | `SCO2-Related_Fatal_Infantile_Cardioencephalomyopathy.yaml` is exact for the fatal COX-deficiency phenotype |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

The IEMbase primary name is SCO2-related myopia 6, but the alternate-name field
and phenotype rows strongly point to fatal infantile cardioencephalomyopathy due
to cytochrome c oxidase deficiency 1. The cached rows include increased CSF and
plasma lactate, hypertrophic cardiomyopathy, dystonia, epilepsy, hypotonia,
Leigh syndrome, distal muscular atrophy, peripheral neuropathy, nystagmus,
perinatal death, ptosis, respiratory failure, psychomotor retardation, and
muscle weakness.

## DisMech phenotype coverage

DisMech has exact coverage for the fatal infantile COX-deficiency phenotype in
`SCO2-Related_Fatal_Infantile_Cardioencephalomyopathy.yaml`. The entry resolves
to MONDO:0011451 and describes biallelic SCO2 variants as a copper-delivery
defect affecting the CuA center of COX2, with fatal infantile hypertrophic
cardiomyopathy, encephalopathy, hypotonia, and lactic acidosis.

## Concordance and completeness

Judgement: correct mapping for the fatal infantile cardioencephalomyopathy
entity, with a source-label caveat.

The local target is appropriate for the phenotype and alternate name in the
IEMbase record. The "myopia 6" primary label should not override the clear
fatal COX-deficiency phenotype signal. IEMbase is more granular for neurologic,
neuromuscular, respiratory, ocular-motor, and age-banded lactate features, while
DisMech is stronger for SCO2 copper-delivery mechanism and disease identity.

## Curation actions

- Keep `SCO2-Related_Fatal_Infantile_Cardioencephalomyopathy.yaml` as the
  canonical target for the fatal infantile COX-deficiency content.
- Preserve the IEMbase primary-name anomaly as a source-label caveat.
- Consider reviewing local SCO2 phenotypes for dystonia, epilepsy, Leigh
  syndrome, distal muscular atrophy, peripheral neuropathy, nystagmus, ptosis,
  respiratory failure, psychomotor retardation, and muscle weakness.
- Avoid treating myopia 6 as the operative disease identity for this IEMbase row
  unless future source review splits the record.
