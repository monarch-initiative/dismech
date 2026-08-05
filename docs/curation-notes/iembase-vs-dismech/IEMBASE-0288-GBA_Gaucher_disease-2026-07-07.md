# IEMbase 0288: GBA-related Glucocerebrosidase deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 288 |
| Nosology | 20.1.01.01 |
| Gene | GBA |
| External IDs | OMIM:230800; ORPHA:355 |
| Generated mapping | MAPPED; `Gaucher_Disease.yaml` |
| Candidate DisMech targets | `Gaucher_Disease.yaml` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents Gaucher disease / acid beta-glucosidase deficiency. The gene
field uses `GBA`, while local DisMech generally uses `GBA1`. Inheritance is
autosomal recessive, treatability is marked yes, and prevalence is listed as
1:75,000 overall and 1:850 in Ashkenazi Jewish populations.

Clinical rows include delayed tooth eruption, developmental delay, early death,
hemophagocytosis, kyphosis, liver cirrhosis, malignancy, osteoporosis,
pancytopenia, pathological fractures, pulmonary hypertension, and restrictive
lung disease. Biochemical rows include increased chitotriosidase, decreased
beta-D-glucosidase activity, and increased serum glucosylsphingosine. Treatment
rows list eliglustat, imiglucerase, taliglucerase, velaglucerase, and
miglustat, with effects on blood, digestive, musculoskeletal, growth, and
biomarker phenotypes.

## DisMech phenotype coverage

`Gaucher_Disease.yaml` is the correct local target. It models GBA1
glucocerebrosidase deficiency, glucocerebroside and glucosylsphingosine
accumulation, Gaucher macrophage activation, inflammatory mediators including
chitotriosidase, neuronopathic branches, bone disease, hematologic and visceral
disease, and type 1, type 2, and type 3 subtypes.

Local phenotypes include hepatomegaly, splenomegaly, thrombocytopenia, anemia,
fatigue, bone pain, osteopenia, pathologic fractures, Erlenmeyer flask
deformity, oculomotor apraxia, supranuclear gaze palsy, seizures, myoclonus,
dysphagia, spasticity, global developmental delay, strabismus, failure to
thrive, and parkinsonism. Local biochemical entries include beta
glucocerebrosidase activity, chitotriosidase, and glucosylsphingosine
(Lyso-Gb1). Local treatment coverage includes enzyme replacement therapy,
substrate reduction therapy, supportive care, genetic counseling, and
investigational lentiviral gene therapy; the ERT and SRT entries name the same
general modalities as IEMbase, including imiglucerase, velaglucerase alfa,
taliglucerase alfa, miglustat, and eliglustat.

## Concordance and completeness

Judgement: correct high-concordance mapping to `Gaucher_Disease.yaml`.

IEMbase and DisMech agree on Gaucher identity, recessive GBA/GBA1 disease,
beta-glucosidase deficiency, chitotriosidase, glucosylsphingosine, cytopenias,
skeletal disease, developmental and early-lethal neuronopathic disease, and the
main ERT/SRT treatment landscape. DisMech is richer for subtypes, mechanism,
bone pain and radiographic bone phenotypes, neuro-ophthalmic disease, and
treatment caveats.

IEMbase adds review prompts for hemophagocytosis, delayed tooth eruption, liver
cirrhosis, malignancy, pulmonary hypertension, and restrictive lung disease. It
also gives agent-level treatment rows that could motivate adding explicit
therapeutic agents to the local generic ERT/SRT records if desired.

## Curation actions

- Keep this record mapped to `Gaucher_Disease.yaml`.
- Use the IEMbase treatment list as a prompt to consider explicit therapeutic
  agents on local ERT/SRT records.
- Review hemophagocytosis, pulmonary hypertension, restrictive lung disease,
  liver cirrhosis, malignancy, and delayed tooth eruption before importing.
