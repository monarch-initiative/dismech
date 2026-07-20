# IEMbase 0368: APOB-related familial defective apolipoprotein B

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 368 |
| Nosology | 15.1.03.01 |
| Gene | APOB |
| External IDs | OMIM:144010; ORPHA:391665 |
| Generated mapping | UNMAPPED; low candidate `Familial_Hypercholesterolemia.yaml` |
| Candidate DisMech targets | `Familial_Hypercholesterolemia.yaml#APOB-LDLR Binding Defect` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents APOB-related familial defective apolipoprotein B, with
alternate names autosomal dominant hypercholesterolemia type 2
(binding-defective apo B) and autosomal dominant hypercholesterolemia type B.
It is listed as an autosomal dominant disorder.

Characteristic rows include plasma Apo B, arcus cornealis, plasma LDL
cholesterol, serum triglyceride, xanthelasma, and tendon xanthomas. Additional
clinical rows include carotid bruits, femoral bruits, and myocardial ischemia.
Biochemical rows include plasma Apo B, plasma HDL cholesterol, plasma LDL
cholesterol, and serum triglyceride. Treatment rows include fibrates, low-fat
diet, and statins.

## DisMech phenotype coverage

The generated UNMAPPED status is a false negative. DisMech has a Familial
Hypercholesterolemia file that explicitly covers APOB as an FH gene and includes
an APOB-LDLR binding-defect mechanism. Local mechanism describes defective LDL
particle binding to the LDL receptor, impaired receptor-mediated LDL clearance,
elevated LDL-C, xanthomas, and premature ASCVD risk.

Local coverage is stronger for the APOB-LDLR binding mechanism and broader FH
management context. IEMbase is stronger for specimen-specific Apo B, HDL, LDL,
and triglyceride rows.

## Concordance and completeness

Judgement: false negative; resolve to the local familial hypercholesterolemia
APOB binding-defect context.

The resources agree on APOB identity, autosomal dominant inheritance, familial
defective apolipoprotein B/autosomal dominant hypercholesterolemia type 2,
elevated LDL cholesterol, tendon xanthomas, corneal arcus, xanthelasma, and
ischemic atherosclerotic complications.

## Curation actions

- Map this record to `Familial_Hypercholesterolemia.yaml`, specifically the
  APOB-LDLR binding-defect context.
- Consider future enrichment with carotid bruits, femoral bruits, Apo B, HDL
  cholesterol, and triglyceride rows after source verification.
- Review the IEMbase fibrate treatment row carefully before import, because the
  core APOB/FH management target is LDL lowering and fibrates may reflect
  mixed-lipid context rather than the primary disease mechanism.
