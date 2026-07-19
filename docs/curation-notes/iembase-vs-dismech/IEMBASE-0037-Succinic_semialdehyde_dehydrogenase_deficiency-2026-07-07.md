# IEMbase 0037: ALDH5A1-related succinic semialdehyde dehydrogenase deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 37 |
| Nosology | 23.2.06.01 |
| Gene | ALDH5A1 |
| External IDs | OMIM:271980; OMIM:610045 |
| Generated mapping | MAPPED by `identifier:OMIM:271980` |
| Candidate DisMech targets | `Succinic_Semialdehyde_Dehydrogenase_Deficiency.yaml` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents SSADH deficiency as an ALDH5A1-related GABA degradation
disorder. Its main biochemical marker is increased urinary 4-hydroxybutyric
acid.

The characteristic phenotype set includes ataxia, abnormal EEG, generalized EEG
slowing, hypotonia, language difficulties, psychomotor delay, seizures, and
spike-wave discharges. Additional features include anxiety, attention disorder,
aggressive behavior, feeding difficulties, hyperactivity, sleep disturbance,
oculomotor dyspraxia, strabismus, decreased tendon reflexes, cerebral and
cerebellar atrophy, globus pallidus T2 hyperintensity, brainstem T2 signal,
dentate nucleus T2 signal, and subcortical white-matter T2 signal. IEMbase
lists vigabatrin as a pharmacologic treatment.

## DisMech phenotype coverage

The generated mapping to
`Succinic_Semialdehyde_Dehydrogenase_Deficiency.yaml` is correct. DisMech covers
the ALDH5A1 enzymatic block, GABA catabolic process, succinic semialdehyde to
succinate block, GABA and 4-hydroxybutyrate/GHB accumulation, 4,5-DHHA, redox
and mitochondrial stress, intellectual disability, ataxia, hypotonia, global
developmental delay, atypical behavior, bilateral tonic-clonic seizures,
myoclonic seizures, status epilepticus, SUDEP, expressive language delay, sleep
disturbance, autism, dystonia, chorea, exertional dyskinesia, anxiety,
obsessive-compulsive traits, ADHD-like attention problems, aggression, basal
ganglia/globus-pallidus T2 hyperintensity, urinary organic acid/GHB testing,
ALDH5A1 molecular testing, and brain MRI.

DisMech also adds important treatment nuance: vigabatrin is discussed as
inconsistent and potentially manifestation-exacerbating because it can further
increase GABA, and tiagabine is similarly cautioned against. DisMech lists
symptom-directed anticonvulsant therapy and neuropsychiatric supportive care
rather than treating vigabatrin as an uncomplicated therapy.

## Concordance and completeness

Judgement: correct mapping and high concordance. DisMech is richer
mechanistically and more cautious therapeutically; IEMbase is richer for
granular EEG and MRI subfeatures.

IEMbase adds explicit generalized slowing and spike-wave EEG labels, cerebellar
atrophy, cerebral atrophy, brainstem T2 signal, dentate nucleus T2 signal,
subcortical white-matter T2 signal, oculomotor dyspraxia, strabismus, decreased
tendon reflexes, feeding difficulties, and hyperactivity. DisMech adds broader
metabolomics, oxidative stress, movement-disorder detail, SUDEP, autism,
OCD-like traits, and explicit treatment cautions.

## Curation actions

- Keep the generated mapping.
- Consider adding selected IEMbase MRI/EEG refinements, especially generalized
  slowing, spike-wave discharges, brainstem and dentate T2 signal, and cerebral
  or cerebellar atrophy.
- Do not import IEMbase's vigabatrin treatment row without preserving the
  existing DisMech caution that vigabatrin may worsen manifestations.
