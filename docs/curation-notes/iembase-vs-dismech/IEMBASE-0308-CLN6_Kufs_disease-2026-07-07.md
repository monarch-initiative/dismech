# IEMbase 0308: CLN6-related Kufs disease

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 308 |
| Nosology | 20.4.05.01 |
| Gene | CLN6 |
| External IDs | OMIM:204300; ORPHA:228340 |
| Generated mapping | MAPPED; `Adult_Neuronal_Ceroid_Lipofuscinosis.yaml` |
| Candidate DisMech targets | `Adult_Neuronal_Ceroid_Lipofuscinosis.yaml` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents CLN6-related Kufs disease as adult neuronal ceroid
lipofuscinosis with behavioral disorder, cerebral atrophy, cognitive
impairment, extrapyramidal movement disorder, movement disorder, myoclonic
epilepsy, and seizures. Additional clinical rows include ataxia, cerebellar
atrophy, abnormal EEG, electron-microscopy storage material, myoclonus,
neurodegenerative disease, tonic-clonic seizures, and spasticity.

No biochemical or treatment rows are present in the cached record.

## DisMech phenotype coverage

`Adult_Neuronal_Ceroid_Lipofuscinosis.yaml` is the correct local target. It
models Kufs disease as adult NCL with Type A and Type B clinical forms, and it
explicitly includes CLN6 as the main recessive Type A/Kufs-A gene. Mechanistic
coverage includes CLN6 EGRESS-complex lysosomal enzyme trafficking defect,
lipopigment accumulation, and progressive neurodegeneration.

Phenotype coverage includes dementia, myoclonus, seizure, cerebellar ataxia,
cerebral atrophy, and EEG photosensitivity. Biochemical/pathologic coverage
includes autofluorescent ceroid lipopigment storage, proteolysis-resistant
ceroid deposits, cathepsin F activity for the CTSF branch, and lysosomal enzyme
levels at the lysosome. Treatment coverage is supportive care and antiseizure
pharmacotherapy.

## Concordance and completeness

Judgement: correct file-level mapping to
`Adult_Neuronal_Ceroid_Lipofuscinosis.yaml`, with CLN6-specific coverage already
present locally.

Concordance is high for Kufs/adult NCL scope, CLN6 identity, adult progressive
myoclonus epilepsy, dementia/cognitive impairment, ataxia, seizures,
myoclonus, cerebral/cerebellar atrophy, EEG abnormality, storage material, and
supportive/antiseizure management. DisMech is richer for CLN6 trafficking
mechanism and adult NCL subtype structure.

IEMbase adds explicit extrapyramidal movement disorder, generalized movement
disorder, behavioral disorder, spasticity, and a generic neurodegenerative
disease row. These are compatible with the local description but not all are
modeled as discrete phenotypes.

## Curation actions

- Keep the generated adult NCL mapping.
- Consider adding a CLN6/Kufs-specific phenotype note for extrapyramidal signs
  and spasticity if source-backed.
- Keep CLN6 Kufs disease distinct from CLN6 late-infantile disease; they should
  not collapse to one phenotype record.
- Use the local adult NCL file, not the broad childhood NCL umbrella, as the
  canonical target for this IEMbase record.
