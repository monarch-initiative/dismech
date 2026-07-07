# IEMbase 0527: LDLR-related homozygous familial hypercholesterolemia

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 527 |
| Nosology | 15.1.01.02 |
| Gene | LDLR |
| External IDs | OMIM:143890; OMIM:606945; ORPHA:391665 |
| Generated mapping | UNMAPPED; best candidate `Familial_Hypercholesterolemia.yaml` |
| Candidate DisMech targets | `Familial_Hypercholesterolemia.yaml#Homozygous Familial Hypercholesterolemia` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents LDLR-related homozygous familial hypercholesterolemia, with
hyperlipoproteinemia type 2A and HoFH as alternate labels. The record is marked
autosomal recessive and treatable.

The biochemical signal is very high LDL cholesterol and Apo B with normal HDL
cholesterol and triglycerides. Clinical rows include coronary atherosclerosis,
myocardial ischemia, carotid stenosis, carotid and femoral bruits, aortic valve
disease, calcified aortic valve, arcus cornealis, xanthelasma, and tendon
xanthomas. Treatment rows include statins, ezetimibe, PCSK9 inhibitors,
inclisiran, evinacumab, lomitapide, bile acid sequestrants, and low-fat diet.

## DisMech phenotype coverage

The generated UNMAPPED status is a false negative. `Familial_Hypercholesterolemia.yaml`
contains a homozygous FH subtype and LDLR mechanism coverage. The local file
models reduced hepatic LDL receptor function, lifelong LDL cholesterol excess,
childhood-to-adolescent severe atherosclerotic disease in HoFH, aortic valve
disease, tendon and skin cholesterol deposition, and intensive LDL-lowering
therapy.

Local coverage is also strong for HoFH-specific therapy, including evinacumab,
lomitapide, PCSK9-directed therapies where residual LDLR function exists, LDL
apheresis, statins, ezetimibe, diet, and last-resort liver transplantation
context.

## Concordance and completeness

Judgement: false negative; resolve to the local familial hypercholesterolemia
file, specifically its homozygous FH / LDLR context.

IEMbase and DisMech agree on LDLR identity, severe LDL-C and Apo B elevation,
cholesterol-deposition phenotypes, premature cardiovascular disease, aortic
valve involvement, and combination LDL-lowering treatment. IEMbase adds compact
bruit and specimen-level lipoprotein prompts.

## Curation actions

- Map this record to `Familial_Hypercholesterolemia.yaml#Homozygous Familial Hypercholesterolemia`.
- Consider adding HoFH, hyperlipoproteinemia type 2A, and the IEMbase treatment
  list to alias/management checks if missing from future mapping data.
- Preserve carotid/femoral bruits, Apo B, HDL, triglyceride, aortic-valve, and
  xanthoma rows as enrichment prompts.
