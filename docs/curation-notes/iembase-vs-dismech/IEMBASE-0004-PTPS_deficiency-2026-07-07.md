# IEMbase 0004: PTS-related 6-pyruvoyl-tetrahydropterin synthase deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 4 |
| Nosology | 21.1.04.01 |
| Gene | PTS |
| External IDs | OMIM:261640 |
| Generated mapping | MAPPED by `alias_exact:6 pyruvoyl tetrahydropterin synthase deficiency` |
| DisMech target | `kb/disorders/Tetrahydrobiopterin_Deficiency.yaml#PTPS Deficiency` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase lists low/normal birth weight, dystonia, limb hypertonia, axial
hypotonia, intellectual disability, eyelid ptosis, and swallowing difficulty as
characteristic. Additional features include choreoathetosis, cortical and
subcortical atrophy, drooling, abnormal EEG, hypopigmented hair, microcephaly,
pneumonia, psychomotor delay, eczematous rash, myoclonic and tonic-clonic
seizures, self-mutilation, sudden death, temperature instability, and tremor.

The biochemical pattern is specific: increased plasma phenylalanine, low CSF
5-HIAA and homovanillic acid, reduced PTPS activity in fibroblasts/RBCs,
positive BH4 loading test, low biopterin, high neopterin, and increased
prolactin.

Treatments include sapropterin/BH4, phenylalanine-reduced diet,
levodopa/carbidopa, 5-hydroxytryptophan, and folinic acid.

## DisMech phenotype coverage

DisMech maps this correctly to the PTPS subtype of `Tetrahydrobiopterin
Deficiency`. The umbrella captures hyperphenylalaninemia, developmental delay,
intellectual disability, generalized hypotonia, dystonia, parkinsonism,
oculogyric crisis, seizures, speech delay, gait ataxia, hyperprolactinemia,
urinary pterin profile, CSF neurotransmitter metabolites, and the expected
treatments.

## Concordance and completeness

Judgement: correct mapping with good umbrella-level concordance and partial
subtype-level completeness.

The main gap is subtype resolution. IEMbase distinguishes PTPS-specific
biopterin/neopterin directionality and enzyme testing, while DisMech currently
models these as broad urinary pterin and CSF neurotransmitter profile entries.
Several secondary clinical signs in IEMbase are also not explicit in DisMech:
ptosis, swallowing difficulty, choreoathetosis, brain atrophy, abnormal EEG,
hypopigmented hair, pneumonia, temperature instability, and sudden death.

## Curation actions

- Keep the mapping.
- Consider adding subtype-specific biochemical detail for PTPS activity, low
  biopterin, high neopterin, and BH4 loading response.
- Add secondary neurologic/imaging features only with independent phenotype
  evidence.
