# IEMbase 0600: PGM1-related phosphoglucomutase 1 deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 600 |
| Nosology | 18.4.05.03 |
| Gene | PGM1 |
| External IDs | OMIM:614921; ORPHA:319646 |
| Generated mapping | CANDIDATE; `Glycogen_Storage_Disease_Type_I.yaml` |
| Candidate DisMech targets | None exact |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents PGM1-related phosphoglucomutase 1 deficiency, labelled
PGM1-CDG and glycogen storage disease type XIV. The record is autosomal
recessive, classified under disorders of multiple glycosylation pathways, and
lists D-galactose as a pharmacological treatment.

Biochemical rows include increased creatine kinase, increased transaminases,
increased ammonia, decreased glucose, increased insulin during hypoglycemia,
very decreased free fatty acids and ketones during hypoglycemia, decreased
antithrombin III, increased asialo-, mono-, di-, and trisialotransferrin, and
decreased tetrasialotransferrin. Clinical rows include hepatopathy, episodic
hypoglycemia, hyperinsulinism, dilated cardiomyopathy, muscle weakness,
rhabdomyolysis, hypogonadotropic hypogonadism, short stature, growth-hormone
deficiency, bifid uvula, cleft palate, first arch syndrome, thrombosis, and
malignant-hyperthermia susceptibility.

## DisMech phenotype coverage

`Glycogen_Storage_Disease_Type_I.yaml` is a false-positive generated candidate.
It models GSD I from G6PC1 or SLC37A4 defects in glucose-6-phosphate hydrolysis
or transport. It has overlapping fasting hypoglycemia and hepatomegaly language,
but it does not represent PGM1, phosphoglucomutase 1 deficiency, mixed
glycogenosis-CDG biology, transferrin glycosylation abnormalities, D-galactose
treatment, antithrombin deficiency, or the endocrine/myopathic phenotype.

`PGM2L1_Deficiency.yaml` is a paralog/pathway neighbor only. No exact PGM1-CDG /
GSD XIV target was identified locally.

## Concordance and completeness

Judgement: true local gap; reject GSD I as exact coverage.

The generated candidate is explainable by the glycogen-storage synonym and
hypoglycemia/hepatopathy overlap, but gene, enzymatic step, biomarker profile,
treatment, and phenotype breadth diverge. IEMbase 0600 should remain a separate
PGM1-CDG / GSD XIV work item.

## Curation actions

- Create or identify an exact PGM1-CDG / glycogen storage disease type XIV target
  before import.
- Reject `Glycogen_Storage_Disease_Type_I.yaml` as an exact mapping.
- Preserve D-galactose treatment, transferrin isoform pattern, antithrombin III,
  nonketotic hypoglycemia, hyperinsulinism, cardiomyopathy, rhabdomyolysis,
  hepatopathy, endocrine, clefting/first-arch, thrombosis, and
  malignant-hyperthermia-susceptibility prompts.
