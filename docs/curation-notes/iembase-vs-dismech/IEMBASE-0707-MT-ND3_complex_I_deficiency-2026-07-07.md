# IEMbase 0707: MT-ND3-related NADH dehydrogenase core subunit 3 deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 707 |
| Nosology | 6.1.2.01 |
| Nosology code | IEM0432 |
| Gene | MT-ND3 |
| External IDs | OMIM:252010; ORPHA:99718 |
| Generated mapping | UNMAPPED; weak generated candidate to `Pyruvate_Dehydrogenase_Deficiency.yaml` |
| Candidate DisMech targets | Broad complex I/Leigh context only; no exact MT-ND3 target |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents maternally inherited MT-ND3-related NADH dehydrogenase core
subunit 3 deficiency.

Biochemical rows show decreased fibroblast complex I activity and increased
plasma lactate across all age windows. Clinical rows include dystonia, epilepsy,
abnormal eye movements, Leber hereditary optic neuropathy, and neuropathy.
Characteristic rows include encephalopathy, Leigh syndrome, myopathy, and optic
atrophy.

## DisMech phenotype coverage

No exact MT-ND3 local target was identified.

`Leigh_Syndrome.yaml` covers complex I-related Leigh-spectrum neurologic
disease, including lactate elevation, dystonia/movement disorder, neuropathy,
seizures, and ophthalmologic involvement as broad features. It does not model
MT-ND3 specifically. No exact local LHON target was identified.

The weak generated `Pyruvate_Dehydrogenase_Deficiency.yaml` candidate is a
metabolic-neighbor false positive rather than mtDNA complex I disease.

## Concordance and completeness

Judgement: true gene-specific local gap with broad Leigh overlap only.

The IEMbase row is a complex I core-subunit disease spanning Leigh,
encephalopathy, epilepsy, dystonia, optic involvement, and neuropathy. The
local Leigh entry can support syndrome context but is not complete MT-ND3
coverage.

## Curation actions

- Add a dedicated MT-ND3 complex I deficiency target if curated.
- Reject pyruvate dehydrogenase deficiency as exact coverage.
- Preserve decreased complex I activity, increased lactate, dystonia, epilepsy,
  abnormal eye movements, LHON, neuropathy, encephalopathy, Leigh syndrome,
  myopathy, and optic atrophy.
