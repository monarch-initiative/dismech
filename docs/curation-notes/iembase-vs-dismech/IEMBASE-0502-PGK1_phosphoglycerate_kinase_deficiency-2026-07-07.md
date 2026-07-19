# IEMbase 0502: PGK1-related phosphoglycerate kinase deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 502 |
| Nosology | 3.3.1.01 |
| Gene | PGK1 |
| External IDs | OMIM:300653; ORPHA:713 |
| Generated mapping | UNMAPPED; best scored candidate `Glycogen_Storage_Disease_Type_VII.yaml` (0.742) |
| Candidate DisMech targets | `Glycogen_Storage_Disease_Type_VII.yaml` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents X-linked PGK1-related phosphoglycerate kinase deficiency as
muscle phosphoglycerate kinase deficiency. No treatments are listed.
Biochemical rows include normal-to-increased plasma creatine kinase, decreased
overall and muscle phosphoglycerate kinase activity, normal-to-increased plasma
bilirubin, normal-to-increased blood reticulocytes, and normal-to-increased
urine myoglobin. Clinical rows include optional hemolytic anemia, decreased RBC
life span, exercise intolerance, muscle cramps, muscle pain, muscle weakness,
psychomotor retardation, retinal dystrophy, and seizures.

## DisMech phenotype coverage

`Glycogen_Storage_Disease_Type_VII.yaml` is not the correct target. The local
GSD VII file models autosomal recessive PFKM/Tarui disease with reduced
phosphofructokinase activity, exercise intolerance, hemolytic anemia, and
myoglobinuria. Those overlapping glycolysis and hemolysis signals make it a
useful neighbor, but it does not model PGK1, phosphoglycerate kinase deficiency,
X-linked inheritance, retinal dystrophy, seizures, or the PGK enzyme assay.

## Concordance and completeness

Judgement: unmapped true gap; reject the GSD VII neighbor as exact coverage.

IEMbase's source disease is a multisystem X-linked glycolytic enzyme disorder
with myopathic, hematologic, neurologic, and retinal features. The best-scored
DisMech candidate covers a different glycolytic step and a different Mendelian
entity. Shared hemolysis and exercise-intolerance vocabulary is insufficient for
mapping.

## Curation actions

- Keep this record unmapped until a PGK1 phosphoglycerate kinase deficiency
  entry is created.
- Do not substitute `Glycogen_Storage_Disease_Type_VII.yaml` as exact coverage.
- Preserve IEMbase prompts for X-linked inheritance, PGK activity, shortened RBC
  life span, hemolysis, myoglobinuria, retinal dystrophy, seizures, and
  psychomotor delay for a future exact entry.
