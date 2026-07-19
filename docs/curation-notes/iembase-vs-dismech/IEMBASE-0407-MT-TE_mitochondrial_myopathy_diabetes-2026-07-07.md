# IEMbase 0407: MT-TE-related mitochondrial myopathy with diabetes mellitus

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 407 |
| Nosology | 6.2.23.01 |
| Gene | MT-TE |
| External IDs | OMIM:500002; ORPHA:2596 |
| Generated mapping | UNMAPPED; low candidate `Reversible_Infantile_Cytochrome_c_Oxidase_Deficiency.yaml` |
| Candidate DisMech targets | No exact local target |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents a mitochondrial MT-TE disorder linked to m.14709T>C, with
mitochondrial inheritance. The characteristic signal is adolescent/adult
hyperglycemia, insulin-dependent diabetes mellitus, and myopathy. Additional
adult clinical rows include ataxia, neurocognitive and behavioral issues, and
ophthalmoplegia. There are no treatment rows.

## DisMech phenotype coverage

There is no exact local DisMech target for MT-TE-related mitochondrial myopathy
with diabetes mellitus. The generated
`Reversible_Infantile_Cytochrome_c_Oxidase_Deficiency.yaml` candidate shares the
MT-TE gene, but it is a different MT-TE disease centered on homoplasmic
m.14674T>C/G, infantile reversible respiratory-chain or COX-deficient myopathy,
neonatal/infantile hypotonia, lactate elevation, macroglossia, liver
dysfunction, and spontaneous recovery.

Local generic diabetes entries are also not appropriate because the IEMbase
record is a maternally inherited mitochondrial diabetes-myopathy syndrome, not
common type 2 diabetes or pancreatic agenesis.

## Concordance and completeness

Judgement: true local gap; reject RIRCD as an exact mapping.

The shared MT-TE gene is not enough to merge these records. IEMbase 407 is
distinguished by m.14709T>C, adolescent/adult diabetes plus myopathy, and a
later-onset neurologic/ophthalmoplegic phenotype. Local RIRCD covers a different
variant, different age window, and different clinical trajectory.

## Curation actions

- Keep this record unmapped until an MT-TE m.14709T>C mitochondrial
  myopathy-with-diabetes target exists.
- Do not map to `Reversible_Infantile_Cytochrome_c_Oxidase_Deficiency.yaml`.
- If curated, include MT-TE/m.14709T>C, mitochondrial inheritance,
  insulin-dependent diabetes mellitus, hyperglycemia, myopathy, ataxia,
  neurocognitive issues, and ophthalmoplegia.
