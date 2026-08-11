# IEMbase 0506: USF1-related familial combined hyperlipidemia

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 506 |
| Nosology | 15.3.20.01 |
| Gene | USF1 |
| External IDs | OMIM:144250; OMIM:602491 |
| Generated mapping | MAPPED; HIGH; `Hyperlipidemia.yaml#Familial Combined Hyperlipidemia` |
| Candidate DisMech targets | `Hyperlipidemia.yaml#Familial Combined Hyperlipidemia` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents USF1-related familial combined hyperlipidemia, also named
hyperlipoproteinemia type 2B / FCHL / HLP type 2, as a complex-trait lipid
disorder with unknown inheritance in the local JSON. No treatments are listed.
Biochemical rows include decreased HDL cholesterol, increased LDL cholesterol,
increased serum triglyceride, and increased plasma Apo B. Clinical rows include
arcus cornealis, xanthelasma, carotid bruits, femoral bruits, and adult
myocardial ischemia.

## DisMech phenotype coverage

`Hyperlipidemia.yaml#Familial Combined Hyperlipidemia` is the correct local
target. The local hyperlipidemia entry has a Familial Combined Hyperlipidemia
subtype characterized by elevated total cholesterol, LDL cholesterol, and/or
triglycerides with variable expression among affected family members. The file
also models shared dyslipidemia mechanisms including hepatic apoB-containing
lipoprotein clearance, VLDL overproduction, impaired LPL/ApoC-III regulation,
atherogenic lipoprotein infiltration of arterial intima, foam-cell formation,
fibrous plaque formation, coronary artery disease, and lipid-lowering
treatments.

## Concordance and completeness

Judgement: correct generated mapping with moderate-to-high phenotype
concordance.

IEMbase and DisMech agree on the FCHL identity and on the mixed LDL/TG/HDL
dyslipidemia phenotype with atherosclerotic/coronary consequences. IEMbase adds
more specific prompts for USF1, Apo B elevation, xanthelasma, arcus cornealis,
carotid and femoral bruits, and myocardial ischemia timing. The current
DisMech entry does not visibly model USF1 as a gene-level susceptibility locus,
so the subtype coverage is clinically correct but incomplete at the gene-specific
IEMbase level.

## Curation actions

- Keep the mapping to `Hyperlipidemia.yaml#Familial Combined Hyperlipidemia`.
- Consider adding USF1 as a susceptibility/modifier gene only with verified
  evidence, because the DisMech target is a broad complex-trait hyperlipidemia
  entry.
- Consider future enrichment for Apo B elevation, arcus cornealis, xanthelasma,
  and peripheral bruit prompts if they fit the entry's intended scope.
