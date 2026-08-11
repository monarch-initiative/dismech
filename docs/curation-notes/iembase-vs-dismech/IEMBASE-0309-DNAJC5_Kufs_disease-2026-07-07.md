# IEMbase 0309: DNAJC5-related Kufs disease

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 309 |
| Nosology | 20.4.03.01 |
| Gene | DNAJC5 |
| External IDs | OMIM:162350; ORPHA:228343 |
| Generated mapping | MAPPED; `Adult_Neuronal_Ceroid_Lipofuscinosis.yaml` |
| Candidate DisMech targets | `Adult_Neuronal_Ceroid_Lipofuscinosis.yaml` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents DNAJC5-related Kufs disease, also known as CLN4B/Parry-type
NCL, with behavioral disorder, cognitive decline, movement disorder, seizures,
and tonic-clonic seizures. Additional clinical rows include ataxia, cerebellar
atrophy, cerebral atrophy, abnormal EEG, electron-microscopy storage material,
extrapyramidal movement disorder, myoclonus, neurodegenerative disease,
psychiatric disturbances, and spasticity.

No biochemical or treatment rows are present in the cached record.

## DisMech phenotype coverage

`Adult_Neuronal_Ceroid_Lipofuscinosis.yaml` is the correct local target. It
models DNAJC5 as the autosomal dominant CLN4/adult NCL gene and includes a
DNAJC5/CSPalpha misfolding and synaptic dysfunction mechanism. The file covers
the broader adult NCL/Kufs phenotype with dementia, myoclonus, seizure,
cerebellar ataxia, cerebral atrophy, EEG photosensitivity, ceroid lipopigment
storage, and supportive plus antiseizure management.

The local subtype structure is clinical Type A/Type B rather than gene-specific
CLN4 versus CLN6 versus CTSF subtypes, so DNAJC5 is captured in `genetic` and
pathophysiology rather than as a separate subtype target.

## Concordance and completeness

Judgement: correct file-level mapping to
`Adult_Neuronal_Ceroid_Lipofuscinosis.yaml`; a future DNAJC5/CLN4 subtype could
make this mapping more precise.

Concordance is high for adult NCL/Kufs scope, DNAJC5 identity, autosomal
dominant adult NCL mechanism, cognitive decline/dementia, seizures, myoclonus,
ataxia, cerebral/cerebellar atrophy, EEG abnormality, and storage material.
DisMech is richer for molecular mechanism and pathologic readouts.

IEMbase adds explicit behavioral disorder, psychiatric disturbances,
extrapyramidal movement disorder, spasticity, and movement disorder rows. These
are consistent with adult NCL but are not all discrete local phenotype entries.

## Curation actions

- Keep the generated adult NCL mapping for DNAJC5-related Kufs disease.
- Consider a future gene-specific CLN4/DNAJC5 subtype or differentiating
  mechanism if mapping infrastructure supports it.
- Review psychiatric, extrapyramidal, and spasticity rows before phenotype
  expansion.
- Keep this record separate from CLN6-related Kufs disease even though both map
  to the same adult NCL file today.
