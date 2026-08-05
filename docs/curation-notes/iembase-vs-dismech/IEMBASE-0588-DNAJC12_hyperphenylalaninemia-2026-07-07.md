# IEMbase 0588: DNAJC12-related hyperphenylalaninemia

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 588 |
| Nosology | 23.1.08.02 |
| Gene | DNAJC12 |
| External IDs | OMIM:606060 |
| Generated mapping | UNMAPPED |
| Candidate DisMech targets | `Disorder_of_Catecholamine_Synthesis.yaml#DNAJC12-related monoamine synthesis disorder` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents DNAJC12-related hyperphenylalaninemia. The record is
autosomal recessive, classified under monoamine neurotransmission, has unknown
treatability, and lists 5-hydroxytryptophan, BH4, and L-dopa plus carbidopa.

Biochemical rows include increased plasma phenylalanine, decreased CSF 5-HIAA,
decreased CSF HVA, normal-to-increased CSF biopterin, normal DBS and urinary
biopterin, and normal CSF, DBS, and urinary neopterin. Clinical rows include
autism and dystonia.

## DisMech phenotype coverage

`Disorder_of_Catecholamine_Synthesis.yaml` contains the correct local target as
the DNAJC12-related monoamine synthesis disorder subtype. It models DNAJC12
pathogenic variants, monoamine-synthesis co-chaperone dysfunction,
hyperphenylalaninemia, combined monoamine deficiency, infantile dystonia,
developmental delay, cognitive deficits, and young-onset parkinsonism.

`Phenylketonuria.yaml` and `Tetrahydrobiopterin_Deficiency.yaml` are useful
context for hyperphenylalaninemia and monoamine metabolism, but the exact local
coverage is the DNAJC12 subtype in the catecholamine-synthesis umbrella.

## Concordance and completeness

Judgement: generated false negative; resolve to
`Disorder_of_Catecholamine_Synthesis.yaml#DNAJC12-related monoamine synthesis disorder`.

IEMbase and DisMech agree on DNAJC12, autosomal recessive disease,
hyperphenylalaninemia, monoamine-synthesis dysfunction, and dystonia. IEMbase
adds a useful diagnostic pattern: low CSF HVA/5-HIAA with normal or only
variably increased pterin markers, plus treatment prompts for BH4,
5-hydroxytryptophan, and L-dopa/carbidopa. IEMbase also adds autism as a
clinical review prompt.

## Curation actions

- Promote this record to
  `Disorder_of_Catecholamine_Synthesis.yaml#DNAJC12-related monoamine synthesis disorder`.
- Preserve the low CSF HVA/5-HIAA, pterin-normality, treatment, autism, and
  dystonia prompts for source-level review.
- Do not map this record to PAH-related PKU or primary BH4 enzyme deficiency
  as the exact disease target.
