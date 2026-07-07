# IEMbase 0100: DDC-related aromatic L-amino acid decarboxylase deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 100 |
| Nosology | 23.1.02.01 |
| Gene | DDC |
| External IDs | OMIM:608643 |
| Generated mapping | AMBIGUOUS |
| Candidate DisMech targets | `Aromatic_L_Amino_Acid_Decarboxylase_Deficiency.yaml`; `Disorder_of_Catecholamine_Synthesis.yaml#Aromatic L-amino acid decarboxylase deficiency` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents this as autosomal recessive DDC/AADC deficiency in the
monoamine neurotransmission group. Treatability is marked yes.

The characteristic biochemical rows are decreased CSF MHPG, decreased CSF
5-HIAA, increased CSF 5-hydroxytryptophan, decreased CSF homovanillic acid, and
increased CSF L-dopa. The clinical rows are developmental delay, dysarthria,
dystonia, hyperkinesia, and insomnia.

Treatments are monoamine oxidase inhibitors, folinic acid, gene therapy,
L-dopa plus carbidopa depending on mutation, and pyridoxine.

## DisMech phenotype coverage

The generated AMBIGUOUS status is caused by two legitimate local matches. The
canonical target should be the standalone
`Aromatic_L_Amino_Acid_Decarboxylase_Deficiency.yaml` entry, with
`Disorder_of_Catecholamine_Synthesis.yaml#Aromatic L-amino acid decarboxylase
deficiency` retained as umbrella context.

The standalone entry covers biallelic DDC variants, AADC enzymatic deficiency,
combined serotonin/dopamine/norepinephrine/epinephrine synthesis failure,
decreased CSF HVA, decreased CSF 5-HIAA, increased 3-O-methyldopa, motor circuit
dysfunction, dysautonomia, and neurodevelopmental impairment. It includes
dysarthria, dystonia, oculogyric crisis, hypotonia, hypokinesia, ptosis,
developmental delay, autonomic features, and disease-directed eladocagene
exuparvovec gene therapy plus pyridoxine, dopamine agonist, and MAO-inhibitor
pharmacotherapy.

## Concordance and completeness

Judgement: ambiguous generated mapping, but high concordance after selecting the
standalone AADC deficiency entry.

IEMbase is more explicit about the CSF compartment for MHPG, 5-HIAA,
5-hydroxytryptophan, HVA, and L-dopa, and includes folinic acid and the
mutation-dependent L-dopa/carbidopa row. DisMech is substantially richer for
mechanism, autonomic and ocular-motor features, broader phenotype evidence, and
approved gene therapy.

## Curation actions

- Resolve to `Aromatic_L_Amino_Acid_Decarboxylase_Deficiency.yaml` as the
  canonical disease target.
- Keep `Disorder_of_Catecholamine_Synthesis.yaml#Aromatic L-amino acid
  decarboxylase deficiency` as secondary umbrella context.
- Consider adding IEMbase-specific CSF MHPG, 5-hydroxytryptophan, and L-dopa
  biomarker rows if the standalone entry is further normalized.
