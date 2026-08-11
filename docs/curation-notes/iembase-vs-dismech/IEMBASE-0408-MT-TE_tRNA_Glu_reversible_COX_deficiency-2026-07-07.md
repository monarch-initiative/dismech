# IEMbase 0408: MT-TE-related mitochondrial tRNA(Glu) deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 408 |
| Nosology | 6.2.06.01 |
| Gene | MT-TE |
| External IDs | OMIM:500009; ORPHA:254864 |
| Generated mapping | UNMAPPED; low candidate `Reversible_Infantile_Cytochrome_c_Oxidase_Deficiency.yaml` |
| Candidate DisMech targets | `Reversible_Infantile_Cytochrome_c_Oxidase_Deficiency.yaml` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents MT-TE-related mitochondrial tRNA(Glu) deficiency, also listed
as mitochondrial myopathy with reversible cytochrome c oxidase deficiency. The
source variant is m.14674T>C and inheritance is mitochondrial. Biochemical rows
include increased plasma creatine kinase and lactate in neonatal/infantile
stages with normalization later. Clinical rows include hypotonia and decreased
tendon reflexes, while characteristic rows include liver dysfunction,
macroglossia, and myopathy. There are no treatment rows.

## DisMech phenotype coverage

The generated unmapped status is a false negative. Local
`Reversible_Infantile_Cytochrome_c_Oxidase_Deficiency.yaml` directly models
reversible infantile cytochrome c oxidase deficiency as an MT-TE/mt-tRNA(Glu)
disease, most commonly due to homoplasmic m.14674T>C and less often
m.14674T>G. It covers mitochondrial inheritance, reduced mt-tRNA(Glu), impaired
mitochondrial translation and respiratory-chain function, COX-deficient
mitochondrial myopathy, ragged-red and COX-negative fibers, infantile hypotonia,
lactate, macroglossia, liver involvement, and spontaneous clinical/biochemical
recovery.

Local DisMech is stronger for the molecular mechanism and recovery model.
IEMbase adds a compact age-banded presentation for CK, lactate, hypotonia,
reflexes, liver dysfunction, macroglossia, and myopathy.

## Concordance and completeness

Judgement: false negative; resolve to
`Reversible_Infantile_Cytochrome_c_Oxidase_Deficiency.yaml`.

The resources agree on disease identity, MT-TE/mt-tRNA(Glu), m.14674T>C,
mitochondrial inheritance, infantile COX-deficient myopathy, lactate/CK
abnormalities, and reversible age course.

## Curation actions

- Map this record to `Reversible_Infantile_Cytochrome_c_Oxidase_Deficiency.yaml`.
- Consider adding IEMbase's explicit decreased tendon reflexes and CK/lactate
  age-banding after source verification.
- Preserve the distinction from MT-TE m.14709T>C mitochondrial myopathy with
  diabetes mellitus.
