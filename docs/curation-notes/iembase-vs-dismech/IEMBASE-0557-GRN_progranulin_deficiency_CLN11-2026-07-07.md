# IEMbase 0557: GRN-related progranulin deficiency / CLN11

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 557 |
| Nosology | 20.4.09.01 |
| Gene | GRN |
| External IDs | OMIM:614706; ORPHA:100070 |
| Generated mapping | UNMAPPED |
| Candidate DisMech targets | `Neuronal_Ceroid_Lipofuscinosis.yaml` for the recessive NCL aspect; frontotemporal dementia entries as separate context |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents GRN-related progranulin deficiency under the neuronal ceroid
lipofuscinosis subgroup. Alternate labels distinguish dominant frontotemporal
lobar degeneration with TDP-43 inclusions from recessive CLN11 disease. The
record lists both autosomal dominant and autosomal recessive inheritance, an
adult form subtype, unknown treatability, and no treatment rows.

The clinical signal includes adult ataxia, abnormal EEG, electron-microscopy
storage material, abnormal ERG, movement disorder, and seizures. Characteristic
rows include cerebellar atrophy on MRI, language difficulties, muscular
atrophy, retinal dystrophy, spinal muscular atrophy, and vision loss or optic
atrophy.

## DisMech phenotype coverage

`Neuronal_Ceroid_Lipofuscinosis.yaml` is the best existing local target for the
recessive CLN11/NCL aspect. The entry models NCL as a heterogeneous lysosomal
neurodegenerative disease group with toxic endo-lysosomal storage,
autofluorescent lipopigment accumulation, progressive visual and cognitive
decline, seizures, myoclonus, and worsening motor dysfunction. Its genetic
section includes GRN as a definitive autosomal recessive NCL gene relationship.

DisMech also has frontotemporal dementia context mentioning GRN, but that is a
separate dominant GRN-FTLD/TDP-43 disease axis rather than the recessive CLN11
storage disease represented by the NCL entry.

## Concordance and completeness

Judgement: generated false negative for the recessive CLN11/NCL aspect; resolve
that portion to `Neuronal_Ceroid_Lipofuscinosis.yaml#GRN`, while preserving the
dominant GRN-FTLD label as separate or only partially covered context.

IEMbase and DisMech agree at the broad NCL level on GRN, recessive NCL
classification, storage material, neurodegeneration, seizures, movement
disorder, visual involvement, and cerebral/cerebellar degeneration. DisMech is
stronger for shared NCL lysosomal-storage mechanisms, while IEMbase is more
explicit about adult CLN11 presentation and the dual dominant versus recessive
GRN nosology.

IEMbase adds useful prompts for language difficulty, retinal dystrophy,
abnormal ERG, optic atrophy or vision loss, spinal muscular atrophy, and
distinguishing dominant GRN-FTLD from recessive CLN11.

## Curation actions

- Treat the recessive CLN11/NCL portion as covered by
  `Neuronal_Ceroid_Lipofuscinosis.yaml`, not as a complete absence of local
  coverage.
- Do not collapse dominant GRN-FTLD/TDP-43 disease into the NCL entry without a
  deliberate spectrum or subtype decision.
- Consider adding a GRN/CLN11 subtype note under the NCL entry, including
  adult-onset retinal, language, cerebellar, EEG, and EM storage prompts.
