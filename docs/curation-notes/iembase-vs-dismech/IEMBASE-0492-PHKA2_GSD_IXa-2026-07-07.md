# IEMbase 0492: PHKA2-related hepatic phosphorylase kinase alpha-2 subunit deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 492 |
| Nosology | 3.4.1.01 |
| Gene | PHKA2 |
| External IDs | OMIM:306000; ORPHA:264580 |
| Generated mapping | CANDIDATE; MEDIUM; `Glycogen_Storage_Disease_Type_I.yaml` |
| Candidate DisMech targets | `Glycogen_Storage_Disease_Type_I.yaml` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents X-linked PHKA2-related hepatic phosphorylase kinase alpha-2
subunit deficiency as glycogen storage disease type IXa. No treatments are
listed. Biochemical rows include normal-to-increased ASAT/ALAT and biotinidase,
decreased-to-normal phosphorylase kinase overall, decreased liver phosphorylase
kinase, increased fasted plasma and urine ketones, normal-to-markedly
increased liver glycogen, normal-to-increased cholesterol, low-to-normal
fasting glucose, normal fasting plasma and urine lactate, normal-to-increased
triglycerides, and normal plasma and urine uric acid. Clinical rows include
doll-like adiposity, hypoglycemia, and short stature.

## DisMech phenotype coverage

`Glycogen_Storage_Disease_Type_I.yaml` is not the correct target. It covers GSD
I due to G6PC1/SLC37A4 defects and autosomal recessive GSD Ia/Ib subtypes. It
does not model PHKA2, X-linked phosphorylase kinase deficiency, GSD IXa, or the
phosphorylase-kinase/liver-glycogen profile represented by IEMbase.

## Concordance and completeness

Judgement: false-positive candidate; true PHKA2/GSD IXa local gap.

The candidate file is a carbohydrate-storage neighbor, but it is a different
glycogenosis. IEMbase's disease is an X-linked hepatic phosphorylase kinase
defect with relatively preserved lactate and uric acid, ketotic fasting
hypoglycemia, liver glycogen storage, and short stature. The GSD I file's
glucose-6-phosphatase mechanism and subtype structure do not provide exact
coverage.

## Curation actions

- Do not map this record to `Glycogen_Storage_Disease_Type_I.yaml`.
- Track PHKA2-related GSD IXa as a local curation gap.
- Preserve IEMbase prompts for X-linked inheritance, liver phosphorylase kinase
  activity, normal lactate/uric acid, ketones, short stature, doll-like
  adiposity, and biotinidase for a future exact entry.
