# IEMbase 0705: MT-ND1-related NADH dehydrogenase core subunit 1 deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 705 |
| Nosology | 6.1.18.01 |
| Nosology code | IEM0430 |
| Gene | MT-ND1 |
| External IDs | OMIM:252010; ORPHA:255210 |
| Generated mapping | UNMAPPED; weak generated candidate to `Pyruvate_Dehydrogenase_Deficiency.yaml` |
| Candidate DisMech targets | Broad complex I/Leigh context only; no exact MT-ND1 target |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents maternally inherited MT-ND1-related NADH dehydrogenase core
subunit 1 deficiency, within the mtDNA-encoded oxidative phosphorylation
protein group.

Biochemical rows show decreased fibroblast complex I activity and increased
plasma lactate across neonatal, infantile, childhood, adolescent, and adult
windows. Clinical rows include childhood-to-adult exercise intolerance and
adolescent/adult Leber hereditary optic neuropathy. Characteristic rows add
hypertrophic cardiomyopathy, dystonia, MELAS-like features, myopathy, and
spasticity.

## DisMech phenotype coverage

No exact MT-ND1 local target was identified.

`Leigh_Syndrome.yaml` has broad complex I disease context and states that mtDNA
MT-ND subunit variants can cause complex I-deficient Leigh-spectrum disease, but
the local entry does not model MT-ND1 specifically. `MELAS_Syndrome.yaml`
captures MT-ND5 and other mitochondrial-gene MELAS as a subtype, but it does
not provide MT-ND1-specific coverage. No exact LHON entry was identified.

The weak generated `Pyruvate_Dehydrogenase_Deficiency.yaml` candidate is a
pyruvate-metabolism neighbor, not an mtDNA complex I subunit disorder.

## Concordance and completeness

Judgement: true gene-specific local gap with broad mitochondrial syndrome
context only.

The local Leigh and MELAS entries are useful for syndrome-level interpretation,
but they are not complete disease-level coverage for MT-ND1 complex I
deficiency, LHON, cardiomyopathy, or the myopathy/spasticity package in this
IEMbase row.

## Curation actions

- Add a dedicated MT-ND1 complex I deficiency target if curated.
- Reject pyruvate dehydrogenase deficiency as exact coverage.
- Preserve decreased complex I activity, increased lactate, exercise
  intolerance, LHON, hypertrophic cardiomyopathy, dystonia, MELAS-like
  features, myopathy, and spasticity.
- Treat `Leigh_Syndrome.yaml` and `MELAS_Syndrome.yaml` as context, not exact
  MT-ND1 coverage.
