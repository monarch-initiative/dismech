# IEMbase 0311: CLN6-related lysosomal protein deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 311 |
| Nosology | 20.4.05.02 |
| Gene | CLN6 |
| External IDs | OMIM:601780; ORPHA:228340 |
| Generated mapping | UNMAPPED |
| Candidate DisMech targets | `Neuronal_Ceroid_Lipofuscinosis.yaml` as umbrella context only; `Adult_Neuronal_Ceroid_Lipofuscinosis.yaml` is not the correct phenotype scope |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents the CLN6 late-infantile lysosomal protein deficiency branch,
not the adult Kufs disease branch. Characteristic rows include cerebellar
atrophy, cerebral atrophy, movement disorder, muscular atrophy, optic atrophy,
pigmentary retinopathy, retinal dystrophy, seizures, myoclonic seizures,
abnormal or delayed speech, spinal muscular atrophy, and vision loss or optic
atrophy. Additional clinical rows include ataxia, cerebellar white matter
abnormalities, developmental regression, dystonia, abnormal EEG, abnormal ERG,
myoclonic epilepsy, myoclonus, neurodegenerative disease, tonic-clonic
seizures, abnormal somatosensory evoked potentials, spasticity, and abnormal
VEP.

No biochemical or treatment rows are present in the cached record.

## DisMech phenotype coverage

The current local KB has strong CLN6 coverage in
`Adult_Neuronal_Ceroid_Lipofuscinosis.yaml`, but that file models CLN6-related
Kufs/adult NCL, not CLN6 late-infantile disease. The broad
`Neuronal_Ceroid_Lipofuscinosis.yaml` file includes CLN6 in its genetic section
and covers shared NCL biology and phenotypes such as visual impairment, retinal
degeneration, cognitive impairment, seizures, developmental regression, motor
deterioration, myoclonus, and lysosomal storage.

There is no dedicated local NCL6/CLN6 late-infantile disease target.

## Concordance and completeness

Judgement: generated `UNMAPPED` status is appropriate for the late-infantile
CLN6 record. `Adult_Neuronal_Ceroid_Lipofuscinosis.yaml` should not be reused
for this IEMbase ID despite the shared CLN6 gene.

The broad NCL umbrella gives partial context for CLN6 as an NCL gene and for
the shared phenotype scaffold. It does not capture the late-infantile CLN6
entity, its age/scope distinction from adult Kufs disease, or the granular
IEMbase rows for optic atrophy, pigmentary retinopathy, speech abnormality,
MRI white-matter/cerebellar/cerebral atrophy, EEG/ERG/VEP/SSEP abnormalities,
dystonia, spasticity, and muscular atrophy.

## Curation actions

- Treat IEMbase 311 as a missing CLN6 late-infantile NCL target.
- Do not map this record to adult CLN6 Kufs disease.
- Consider a standalone NCL6/CLN6 late-infantile entry or subtype, keeping it
  distinct from `Adult_Neuronal_Ceroid_Lipofuscinosis.yaml`.
- Use the broad NCL umbrella only for temporary shared phenotype context.
