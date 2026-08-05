# IEMbase 0488: GBE1-related glycogen branching enzyme deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 488 |
| Nosology | 3.4.07.01 |
| Gene | GBE1 |
| External IDs | OMIM:232500; ORPHA:308621 |
| Generated mapping | MAPPED; HIGH; `Glycogen_Storage_Disease_Type_IV.yaml` |
| Candidate DisMech targets | `Glycogen_Storage_Disease_Type_IV.yaml` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents autosomal recessive GBE1-related glycogen branching enzyme
deficiency as glycogen storage disease type IV / Andersen disease / adult
polyglucosan body disease. Treatments are liver transplantation and a
low-carbohydrate, protein-enriched diet. Biochemical rows include increased
ASAT/ALAT, decreased branching enzyme in fibroblasts, liver, muscle, red blood
cells, and white blood cells, prolonged prothrombin time, increased hepatic
glycogen, increased bilirubin, and decreased coagulation factors. Clinical rows
include adult polyglucosan body disease, arthrogryposis multiplex,
cardiomyopathy, failure to thrive, fasting intolerance, axial hypotonia, muscle
weakness, and muscular atrophy.

## DisMech phenotype coverage

`Glycogen_Storage_Disease_Type_IV.yaml` is the correct local target. The entry
models autosomal recessive GBE1 deficiency, impaired glycogen branching,
poorly branched glycogen / polyglucosan accumulation, hepatic, cardiac,
neuromuscular, congenital, childhood, and adult polyglucosan body disease
subtypes, failure to thrive, hypotonia, cardiomyopathy, muscle weakness,
skeletal muscle atrophy, prolonged prothrombin time, glycogen branching enzyme
activity testing, polyglucosan storage, liver transplantation, and symptomatic
management.

## Concordance and completeness

Judgement: correct generated mapping with high concordance.

IEMbase and DisMech agree on the GBE1/GSD IV identity, recessive inheritance,
branching enzyme deficiency, polyglucosan storage, multisystem hepatic,
cardiac, neuromuscular, and adult APBD spectrum, and liver transplantation for
progressive hepatic disease. IEMbase adds more explicit compartmental prompts
for branching enzyme testing in fibroblast, liver, muscle, RBC, and WBC, and it
lists bilirubin, coagulation-factor decrease, fasting intolerance, and
protein-enriched low-carbohydrate dietary management as import prompts.

## Curation actions

- Treat this as covered by `Glycogen_Storage_Disease_Type_IV.yaml`.
- If importing IEMbase prompts, verify compartment-specific branching enzyme
  testing, bilirubin, coagulation-factor reduction, fasting intolerance, and
  dietary wording.
- Review the IEMbase ORPHA:308621 versus local Orphanet ORPHA:367 identifier
  difference before using Orphanet-derived evidence.
