# IEMbase 0560: KCTD7-related CLN14 / EPM3

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 560 |
| Nosology | 20.4.12.01 |
| Gene | KCTD7 |
| External IDs | OMIM:611726; ORPHA:263516 |
| Generated mapping | UNMAPPED; best candidate `Progressive_Myoclonus_Epilepsy.yaml` |
| Candidate DisMech targets | `Progressive_Myoclonus_Epilepsy.yaml` and `Neuronal_Ceroid_Lipofuscinosis.yaml` as broad context only |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents KCTD7-related CLN14 disease, with alternate label
progressive myoclonic epilepsy type 3 and abbreviation CLN14 / EPM3. The
record is autosomal recessive, infantile form, of unknown treatability, and has
no treatment rows.

Clinical rows include ataxia, developmental regression, abnormal EEG,
electron-microscopy storage material, hypokinesia, microcephaly, myoclonic
epilepsy, neurodegenerative disease, myoclonic seizures, and abnormal, delayed,
or absent speech. Characteristic rows include cerebellar atrophy, cerebral
atrophy, epilepsy, language difficulties, movement disorder, muscular atrophy,
optic atrophy, spinal muscular atrophy, and vision loss or optic atrophy.

## DisMech phenotype coverage

`Progressive_Myoclonus_Epilepsy.yaml` covers the broad PME grouping and
mentions neuronal ceroid lipofuscinoses as one of the lysosomal storage
subgroups within PME. `Neuronal_Ceroid_Lipofuscinosis.yaml` covers the broad
NCL group and shared toxic endo-lysosomal storage, visual decline, seizures,
myoclonus, and motor/cognitive deterioration.

Neither local entry appears to model KCTD7, CLN14, or EPM3 specifically. The
generated PME candidate is therefore useful context but not an exact DisMech
target for this IEMbase record.

## Concordance and completeness

Judgement: broad partial context only; exact KCTD7/CLN14/EPM3 coverage remains
a local gap.

IEMbase overlaps with local PME and NCL group entries on myoclonic epilepsy,
neurodegeneration, seizures, ataxia, storage material, movement disorder,
visual/optic involvement, language difficulty, and cerebral/cerebellar
atrophy. The missing piece is a gene-specific KCTD7 CLN14 mechanism and
subtype entry.

IEMbase provides a compact curation seed for that gap, including infantile
onset, developmental regression, EEG abnormality, EM storage material,
hypokinesia, microcephaly, speech impairment, optic atrophy, and muscular or
spinal muscular atrophy.

## Curation actions

- Reject `Progressive_Myoclonus_Epilepsy.yaml` as an exact mapping; retain it
  only as grouping context.
- Create or prioritize a KCTD7-related CLN14 / EPM3 curation target under the
  NCL/PME neighborhood.
- Preserve IEMbase infantile-onset, regression, EEG, EM storage, optic, speech,
  and atrophy prompts for that future entry.
