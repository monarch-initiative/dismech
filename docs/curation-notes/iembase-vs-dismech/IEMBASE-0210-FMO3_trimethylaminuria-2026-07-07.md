# IEMbase 0210: FMO3-related primary trimethylaminuria

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 210 |
| Nosology | 2.3.03.01 |
| Gene | FMO3 |
| External IDs | OMIM:602079; ORPHA:468726 |
| Generated mapping | UNMAPPED |
| Candidate DisMech targets | `erythromelalgia.yaml` is a false-positive lexical candidate; `Dimethylglycine_Dehydrogenase_Deficiency.yaml` is only a fish-odor differential |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents this as FMO3-related flavin-containing monooxygenase 3
deficiency, with alternate labels primary trimethylaminuria, fish odor
syndrome, and TMA. Treatability is marked unknown.

The biochemical rows include increased urinary trimethylamine and decreased
urinary TMAO/TMA ratio. The characteristic clinical row is fish odor in urine.
The additional clinical row states no clinical significance. No treatment rows
are listed.

## DisMech phenotype coverage

No local DisMech entry covers primary FMO3-related trimethylaminuria. The
generated best candidate, `erythromelalgia.yaml`, is a false-positive match to
the word "primary" and has no mechanistic or phenotypic relationship.
`Dimethylglycine_Dehydrogenase_Deficiency.yaml` is also not a target: it
includes fish odor as a differential clue but is a DMGDH/dimethylglycine
metabolism disorder, not FMO3-dependent trimethylamine oxidation deficiency.

## Concordance and completeness

Judgement: true local disease gap.

IEMbase gives a narrow but specific trimethylaminuria profile: FMO3, increased
urinary trimethylamine, decreased TMAO/TMA ratio, fish odor, and minimal direct
clinical morbidity. DisMech currently lacks the FMO3 entity and should not
reuse either erythromelalgia or DMGDH deficiency as a substitute.

## Curation actions

- Do not map this record to `erythromelalgia.yaml`.
- Keep `Dimethylglycine_Dehydrogenase_Deficiency.yaml` only as a fish-odor
  differential, not as a trimethylaminuria target.
- Consider a future FMO3/primary trimethylaminuria entry with urinary
  trimethylamine increase, low TMAO/TMA ratio, fish odor, and low systemic
  clinical burden.
