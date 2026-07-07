# IEMbase 0478: LAMP2-related lysosome-associated membrane protein 2 deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 478 |
| Nosology | 20.6.16.01 |
| Gene | LAMP2 |
| External IDs | OMIM:300257; ORPHA:34587 |
| Generated mapping | MAPPED; high candidate `Danon_disease.yaml` |
| Candidate DisMech targets | `Danon_disease.yaml` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents X-linked LAMP2 lysosome-associated membrane protein 2
deficiency as Danon disease / glycogen storage disease type IIb. The biochemical
signal is dominated by increased plasma ASAT/ALAT, increased plasma creatine
kinase, increased hepatic and muscle glycogen, and vacuolated myocytes. IEMbase
also records normal alpha-1,4-glucosidase activity in dried blood spot,
fibroblast, and muscle assays, which helps separate Danon disease from Pompe
disease despite shared glycogen-storage vocabulary. Clinical rows include
abnormal EEG, central vision loss, myopia, and vacuolated lymphocytes. No
treatment row is recorded.

## DisMech phenotype coverage

`Danon_disease.yaml` is the correct local target. The entry models LAMP2/LAMP-2B
deficiency, impaired autophagosome-lysosome fusion, autophagic vacuole
accumulation, glycogen-containing vacuoles in cardiac and skeletal muscle,
hypertrophic and dilated cardiomyopathy, skeletal myopathy, intellectual
disability, Wolff-Parkinson-White syndrome, retinal dystrophy / visual
impairment, elevated creatine kinase, and elevated hepatic transaminases.

## Concordance and completeness

Judgement: correct Danon disease mapping with high concordance.

The resources agree on disease identity, LAMP2 causation, X-linked inheritance,
autophagic/vacuolar muscle pathology, glycogen accumulation, cardiac and
skeletal-muscle involvement, and transaminase/CK abnormalities. IEMbase adds
several useful differential and enrichment prompts: normal alpha-1,4-glucosidase
assays as an explicit Pompe-differentiating row, abnormal EEG, myopia, central
vision loss, and vacuolated lymphocytes. DisMech is stronger on the causal
pathograph and cardiac electrophysiology/remodeling details.

## Curation actions

- Keep the mapping to `Danon_disease.yaml`.
- If importing IEMbase-derived prompts, verify normal alpha-1,4-glucosidase
  activity, abnormal EEG, central vision loss, myopia, and vacuolated
  lymphocytes against source evidence before adding them structurally.
