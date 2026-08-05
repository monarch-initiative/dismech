# IEMbase 0706: MT-ND2-related NADH dehydrogenase core subunit 2 deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 706 |
| Nosology | 6.1.19.01 |
| Nosology code | IEM0431 |
| Gene | MT-ND2 |
| External IDs | OMIM:252010; ORPHA:255210 |
| Generated mapping | UNMAPPED; weak generated candidate to `Pyruvate_Dehydrogenase_Deficiency.yaml` |
| Candidate DisMech targets | Broad complex I/Leigh context only; no exact MT-ND2 target |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents maternally inherited MT-ND2-related NADH dehydrogenase core
subunit 2 deficiency.

Biochemical rows show decreased fibroblast complex I activity and increased
plasma lactate across all age windows, plus low-to-normal plasma glucose in
neonatal and infantile windows. Clinical rows include exercise intolerance from
infancy through adulthood and adolescent/adult Leber hereditary optic
neuropathy. Characteristic rows add neonatal-to-childhood Leigh syndrome and
ragged red fibers across all age windows.

## DisMech phenotype coverage

No exact MT-ND2 local target was identified.

`Leigh_Syndrome.yaml` covers the broad syndrome-level relationship between
complex I dysfunction and Leigh-spectrum disease. It does not model MT-ND2,
ragged red fibers, or the LHON/exercise-intolerance presentation as a
gene-specific disease. No exact LHON target was identified.

The weak generated `Pyruvate_Dehydrogenase_Deficiency.yaml` candidate is not an
mtDNA complex I subunit disease and should not be treated as coverage.

## Concordance and completeness

Judgement: true local gap with broad Leigh overlap only.

The IEMbase signal is a combined complex I deficiency, LHON, Leigh, and
mitochondrial myopathy/ragged-red-fiber phenotype. That phenotype package is
not represented by a local MT-ND2 target.

## Curation actions

- Add a dedicated MT-ND2 complex I deficiency target if curated.
- Reject pyruvate dehydrogenase deficiency as exact coverage.
- Preserve decreased complex I activity, increased lactate, low-to-normal
  neonatal/infantile glucose, exercise intolerance, LHON, Leigh syndrome, and
  ragged red fibers.
