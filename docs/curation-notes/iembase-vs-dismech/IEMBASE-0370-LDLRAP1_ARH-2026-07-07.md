# IEMbase 0370: LDLRAP1-related autosomal recessive hypercholesterolemia

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 370 |
| Nosology | 15.1.02.01 |
| Gene | LDLRAP1 |
| External IDs | OMIM:603813; OMIM:605747; ORPHA:391665 |
| Generated mapping | UNMAPPED; low candidate `Familial_Hypercholesterolemia.yaml` |
| Candidate DisMech targets | `Familial_Hypercholesterolemia.yaml#LDLRAP1-Related LDL Uptake Defect` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents autosomal recessive hypercholesterolemia caused by LDLRAP1,
also listed as ARH1. Inheritance is autosomal recessive.

Characteristic rows include arcus cornealis, xanthelasma, tendon xanthomas,
plasma LDL cholesterol, plasma HDL cholesterol, serum triglyceride, and plasma
Apo B. Clinical rows include carotid bruits, femoral bruits, and myocardial
ischemia. Treatment rows include ezetimibe, lomitapide, PCSK9 inhibitors, and
statins.

## DisMech phenotype coverage

The generated UNMAPPED status is a false negative. DisMech has a Familial
Hypercholesterolemia file that explicitly covers biallelic LDLRAP1 loss of
function as a recessive route into the LDL receptor pathway. The local mechanism
describes LDLRAP1 as the adaptor required for LDLR-LDL internalization through
clathrin-coated pits, with biallelic deficiency reducing hepatic LDL uptake and
converging on the same LDL-clearance defect as FH.

Local coverage is stronger for the receptor-internalization mechanism and FH
treatment framework. IEMbase is stronger for bruits and specific treatment rows
for this record.

## Concordance and completeness

Judgement: false negative; resolve to the local familial hypercholesterolemia
LDLRAP1/autosomal recessive hypercholesterolemia context.

The resources agree on LDLRAP1 identity, recessive inheritance, impaired LDL
clearance, elevated LDL cholesterol, tendon xanthomas, corneal arcus,
xanthelasma, and premature ischemic cardiovascular disease. IEMbase treatment
rows overlap with local LDL-lowering therapy, but lomitapide and PCSK9
inhibitors should be reviewed in the LDLRAP1-specific clinical context before
import.

## Curation actions

- Map this record to `Familial_Hypercholesterolemia.yaml`, specifically the
  LDLRAP1-related LDL uptake defect and autosomal recessive FH context.
- Consider future enrichment with carotid bruits, femoral bruits, Apo B, HDL
  cholesterol, LDL cholesterol, triglyceride rows, and LDLRAP1-specific
  treatment nuance.
- Preserve autosomal recessive inheritance and avoid merging this record into
  heterozygous LDLR/APOB/PCSK9 FH subtypes.
