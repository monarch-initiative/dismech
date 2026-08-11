# IEMbase 0369: PCSK9-related proprotein convertase superactivity

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 369 |
| Nosology | 15.1.05.01 |
| Gene | PCSK9 |
| External IDs | OMIM:603776; OMIM:607786; ORPHA:391665 |
| Generated mapping | UNMAPPED; low candidate `Familial_Hypercholesterolemia.yaml` |
| Candidate DisMech targets | `Familial_Hypercholesterolemia.yaml#PCSK9 Gain-of-Function` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents autosomal dominant hypercholesterolemia type 3 caused by
PCSK9 gain-of-function, also listed as HCHOLA3. Inheritance is autosomal
dominant.

Characteristic rows include arcus cornealis, xanthelasma, tendon xanthomas,
plasma LDL cholesterol, plasma HDL cholesterol, serum triglyceride, and plasma
Apo B. Additional clinical rows include carotid bruits, femoral bruits, and
myocardial ischemia. The cached IEMbase record has no treatment rows.

## DisMech phenotype coverage

The generated UNMAPPED status is a false negative. DisMech has a Familial
Hypercholesterolemia file that explicitly models PCSK9 gain-of-function as a
dominant FH mechanism. Local content describes excess PCSK9 accelerating LDL
receptor degradation after endocytosis, reducing LDL receptor recycling,
impairing hepatic LDL clearance, and producing elevated LDL-C, tendon xanthomas,
and premature atherosclerotic cardiovascular disease.

Local coverage is stronger for the PCSK9 to LDLR degradation mechanism and
LDL-lowering treatment context. IEMbase is stronger for bruits and
specimen-specific lipoprotein rows.

## Concordance and completeness

Judgement: false negative; resolve to the local familial hypercholesterolemia
PCSK9 gain-of-function context.

The resources agree on PCSK9 identity, autosomal dominant inheritance,
hypercholesterolemia type 3, elevated LDL cholesterol, xanthomas, corneal arcus,
xanthelasma, and ischemic atherosclerotic complications. The missing treatment
signal in IEMbase should not be interpreted as absence of disease-directed
therapy because the local FH entry has strong LDL-lowering management coverage.

## Curation actions

- Map this record to `Familial_Hypercholesterolemia.yaml`, specifically the
  PCSK9 gain-of-function and PCSK9-mediated LDLR degradation context.
- Consider future enrichment with carotid bruits, femoral bruits, Apo B, HDL
  cholesterol, LDL cholesterol, and triglyceride rows after source verification.
- Do not import the lack of IEMbase treatments as negative evidence; local FH
  treatment coverage remains relevant.
