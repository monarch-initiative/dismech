# IEMbase 0760: PLA2G6-related phospholipase A2 group 6 deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 760 |
| Nosology | 14.5.01.12 |
| Nosology code | IEM0669 |
| Gene | PLA2G6 |
| External IDs | OMIM:256600; ORPHA:35069 |
| Generated mapping | MAPPED; `Neurodegeneration_With_Brain_Iron_Accumulation.yaml` |
| Candidate DisMech targets | `Neurodegeneration_With_Brain_Iron_Accumulation.yaml`; related context in `Adult_Onset_Dystonia_Parkinsonism.yaml` |
| Review date | 2026-07-08 |

## IEMbase phenotype signal

IEMbase labels this autosomal recessive record as PLA2G6-related phospholipase
A2 group 6 deficiency, with alternate names neurodegeneration with brain iron
accumulation, atypical neuroaxonal dystrophy, and NBIA2A. The source signal
includes brain iron, neurodegeneration with brain iron accumulation, neuroaxonal
dystrophy, basal ganglia MRI abnormalities, cerebellar atrophy, dystonia,
adult parkinsonism or hypokinetic parkinsonism, ataxia, extrapyramidal movement
disorder, spasticity, tetraparesis, truncal hypotonia, psychomotor regression,
epilepsy, abnormal EEG and EMG, slow nerve conduction velocity, interictal
nystagmus, strabismus, optic atrophy, and possible autism.

## DisMech phenotype coverage

`Neurodegeneration_With_Brain_Iron_Accumulation.yaml` is a correct local target.
It includes a PLAN / PLA2G6-associated neurodegeneration subtype, the causal
PLA2G6 gene, lipid-metabolism pathway context, basal-ganglia iron accumulation,
oxidative neuronal injury, progressive motor and cognitive decline, dystonia,
parkinsonism, spasticity, developmental regression, ataxia, cerebellar atrophy,
and diagnostic brain MRI for iron deposition.

`Adult_Onset_Dystonia_Parkinsonism.yaml` is relevant subtype-context for the
adult PLA2G6/PARK14 parkinsonism end of the spectrum, but it is narrower than
the IEMbase NBIA2A / atypical neuroaxonal dystrophy record.

## Concordance and completeness

Judgement: correct mapping to the broad NBIA/PLAN target, with useful related
context in the separate PLA2G6 dystonia-parkinsonism entry.

DisMech covers the major disease identity, gene, NBIA mechanism, iron-imaging
signature, movement disorder, regression, ataxia, and cerebellar atrophy
signals. IEMbase adds a more detailed clinical checklist for PLA2G6 disease,
especially neuroaxonal dystrophy wording, optic atrophy, strabismus,
nystagmus, abnormal EEG/EMG, epilepsy, slow nerve conduction velocity,
tetraparesis, truncal hypotonia, and autism.

## Curation actions

- Keep `Neurodegeneration_With_Brain_Iron_Accumulation.yaml` as the primary
  mapping for this IEMbase record.
- Use `Adult_Onset_Dystonia_Parkinsonism.yaml` only as adult PLA2G6-spectrum
  context, not as the sole mapping.
- Consider the IEMbase ocular, electrophysiology, seizure, and peripheral nerve
  rows when refining PLAN/NBIA phenotype completeness.
