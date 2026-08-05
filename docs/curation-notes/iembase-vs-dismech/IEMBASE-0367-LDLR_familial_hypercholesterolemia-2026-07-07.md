# IEMbase 0367: LDLR-related heterozygous familial hypercholesterolemia

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 367 |
| Nosology | 15.1.01.01 |
| Gene | LDLR |
| External IDs | OMIM:143890; OMIM:606945; ORPHA:391665 |
| Generated mapping | UNMAPPED; low candidate `Familial_Hypercholesterolemia.yaml` |
| Candidate DisMech targets | `Familial_Hypercholesterolemia.yaml#Heterozygous FH/LDLR` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents LDLR-related heterozygous familial hypercholesterolemia, also
listed as hyperlipoproteinemia type 2A. The record is autosomal dominant and
reports prevalence text of approximately 1:500 heterozygotes and 1:1,000,000
homozygotes.

Characteristic rows include plasma Apo B, arcus cornealis, plasma LDL
cholesterol, xanthelasma, and tendon xanthomas. Additional clinical rows include
carotid bruits, femoral bruits, and myocardial ischemia. Biochemical rows
include plasma Apo B, plasma HDL cholesterol, plasma LDL cholesterol, and serum
triglyceride. Treatment rows include colesevelam, ezetimibe, low-fat diet, PCSK9
inhibitors, and statins.

## DisMech phenotype coverage

The generated UNMAPPED status is a false negative. DisMech has a Familial
Hypercholesterolemia file that explicitly covers heterozygous FH caused by one
pathogenic allele in LDLR, APOB, or PCSK9. The local LDLR mechanism describes
reduced hepatic LDL receptor function, impaired receptor-mediated LDL
clearance, elevated LDL-C from birth, tendon xanthomas, premature ASCVD, and
lifelong LDL-lowering therapy.

Local coverage is stronger for the hepatocyte LDL-clearance mechanism and the
broader FH management model. IEMbase is stronger for bruits and specimen-level
lipoprotein rows.

## Concordance and completeness

Judgement: false negative; resolve to the local familial hypercholesterolemia
LDLR/heterozygous FH context.

The resources agree on LDLR identity, autosomal dominant inheritance,
heterozygous FH, elevated LDL cholesterol, tendon xanthomas, corneal arcus,
premature atherosclerotic ischemic disease, statins, ezetimibe, PCSK9
inhibitors, and diet/lifestyle treatment context.

## Curation actions

- Map this record to `Familial_Hypercholesterolemia.yaml`, specifically the
  heterozygous FH and LDLR functional-defect context.
- Consider future enrichment with carotid bruits, femoral bruits, Apo B, HDL
  cholesterol, triglyceride rows, colesevelam, and the IEMbase prevalence
  wording after source verification.
- Keep homozygous prevalence wording distinct from the heterozygous disease
  scope when importing any prevalence information.
