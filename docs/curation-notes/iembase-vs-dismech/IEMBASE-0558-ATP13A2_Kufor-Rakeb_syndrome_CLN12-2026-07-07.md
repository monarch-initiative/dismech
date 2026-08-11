# IEMbase 0558: ATP13A2-related Kufor-Rakeb syndrome / CLN12

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 558 |
| Nosology | 20.4.1.01 |
| Gene | ATP13A2 |
| External IDs | OMIM:606693; ORPHA:306674 |
| Generated mapping | UNMAPPED; best candidate `Kufor-Rakeb_syndrome.yaml` |
| Candidate DisMech targets | `Kufor-Rakeb_syndrome.yaml` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents ATP13A2-related lysosomal type 5 P-type ATPase deficiency,
with alternate labels Kufor-Rakeb syndrome, Parkinson disease 9, and neuronal
ceroid lipofuscinosis 12 / CLN12. The record is autosomal recessive, juvenile
form, of unknown treatability, and has no treatment rows.

Clinical rows include cognitive dysfunction, dysarthria, electron-microscopy
storage material, extrapyramidal movement disorder, gait disturbance, and
neurodegenerative disease. Characteristic rows include akinesia, behavioral
disorder, movement disorder, myoclonus, and rigidity.

## DisMech phenotype coverage

`Kufor-Rakeb_syndrome.yaml` is the correct local target. It models autosomal
recessive ATP13A2-related juvenile parkinsonism with spastic paraparesis,
supranuclear eye movement abnormalities, progressive cognitive decline, and
possible psychosis. The mechanism chain covers ATP13A2 loss, impaired
lysosomal polyamine transport, lysosomal polyamine storage, secondary
lysosomal hydrolase dysfunction, glucosylsphingosine accumulation, impaired
mitochondrial quality control, and progressive neurodegeneration.

Local phenotypes include bradykinesia, rigidity, dystonia, spastic
paraparesis, abnormal eye movement, facial myokymia, cognitive impairment, and
psychiatric symptoms.

## Concordance and completeness

Judgement: generated false negative; resolve to `Kufor-Rakeb_syndrome.yaml`.

IEMbase and DisMech agree on ATP13A2 identity, recessive inheritance, juvenile
neurodegeneration, parkinsonian/extrapyramidal motor disease, rigidity,
akinesia or bradykinesia, cognitive involvement, behavioral or psychiatric
features, and lysosomal storage biology. DisMech is stronger for the
polyamine-transport and lysosome-mitochondria mechanism.

IEMbase adds CLN12 and neuronal ceroid lipofuscinosis aliases, EM storage
material, dysarthria, gait disturbance, and myoclonus prompts that are useful
for aliasing and phenotype review.

## Curation actions

- Promote the IEMbase match to `Kufor-Rakeb_syndrome.yaml`.
- Add or verify aliases for CLN12, neuronal ceroid lipofuscinosis 12, and
  ATP13A2-related lysosomal type 5 P-type ATPase deficiency.
- Consider reviewing IEMbase-specific EM storage material, myoclonus,
  dysarthria, and gait-disturbance rows for possible phenotype additions.
