# IEMbase 0559: CTSF-related CLN13 / Kufs disease

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 559 |
| Nosology | 20.4.11.01 |
| Gene | CTSF |
| External IDs | OMIM:603539; ORPHA:352709 |
| Generated mapping | UNMAPPED; best candidate `Adult_Neuronal_Ceroid_Lipofuscinosis.yaml` |
| Candidate DisMech targets | `Adult_Neuronal_Ceroid_Lipofuscinosis.yaml` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents CTSF-related cathepsin F deficiency, with alternate labels
Kufs disease recessive type, neuronal ceroid lipofuscinosis 13, and CLN13. The
record is autosomal recessive, adult form, of unknown treatability, and has no
treatment rows.

Clinical rows include ataxia, dysarthria, electron-microscopy storage
material, movement disorder, muscular atrophy, seizures, tonic-clonic seizures,
and spinal muscular atrophy. Characteristic rows include behavioral disorder,
cerebellar atrophy, cerebral atrophy, cognitive decline, extrapyramidal
movement disorder, and neurodegenerative disease.

## DisMech phenotype coverage

`Adult_Neuronal_Ceroid_Lipofuscinosis.yaml` is the correct local target. The
entry explicitly models adult NCL / Kufs disease, including Type B Kufs disease
caused by recessive CTSF pathogenic variants, also designated CLN13. Its CTSF
branch models cathepsin F lysosomal protease dysfunction, lysosomal
proteolysis decrease, ceroid lipopigment storage, and progressive
neurodegeneration.

The local disease description covers adult-onset dementia with motor system
dysfunction, cerebellar ataxia or extrapyramidal signs, ultrastructural
storage inclusions, and supportive management.

## Concordance and completeness

Judgement: generated false negative; resolve to
`Adult_Neuronal_Ceroid_Lipofuscinosis.yaml#CTSF`.

IEMbase and DisMech agree on CTSF identity, recessive adult Kufs/CLN13 scope,
cathepsin F lysosomal protease dysfunction, storage material, cognitive
decline, ataxia or extrapyramidal movement disorder, cerebral/cerebellar
atrophy, and progressive neurodegeneration. DisMech is stronger for the
subtype framing and mechanism.

IEMbase adds useful review prompts for dysarthria, muscular atrophy, spinal
muscular atrophy, seizures, and tonic-clonic seizures. The seizure rows should
be source-checked because CTSF Type B Kufs disease is often framed locally as a
dementia/motor subtype without prominent myoclonic epilepsy.

## Curation actions

- Promote the IEMbase match to `Adult_Neuronal_Ceroid_Lipofuscinosis.yaml`,
  specifically the CTSF/CLN13 Type B Kufs branch.
- Add or verify CLN13 and "cathepsin F deficiency" aliases if not already
  surfaced.
- Review IEMbase seizure, dysarthria, muscular-atrophy, and spinal-muscular
  atrophy prompts before phenotype import.
