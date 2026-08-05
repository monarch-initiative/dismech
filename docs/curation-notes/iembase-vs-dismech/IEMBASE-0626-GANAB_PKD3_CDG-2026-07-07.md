# IEMbase 0626: GANAB-related alpha glucosidase II deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 626 |
| Nosology | 18.1.21.01 |
| Gene | GANAB |
| External IDs | OMIM:600666; ORPHA:730 |
| Generated mapping | AMBIGUOUS; identifier match to local ADPKD / PKD entities |
| Candidate DisMech targets | `Autosomal_Dominant_Polycystic_Kidney_Disease.yaml`; `Polycystic_Kidney_Disease.yaml#Autosomal Dominant PKD (ADPKD)` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents GANAB-related alpha glucosidase II deficiency / GANAB-CDG /
polycystic kidney disease 3 as an autosomal dominant disorder with unknown
treatability and no treatment rows.

The cached phenotype signal is adult cystic-organ disease: normal adult serum
sialotransferrins, optional adult polycystic liver disease, and adult
polycystic kidney disease.

## DisMech phenotype coverage

The generated ambiguity is an identifier-placement issue rather than a false
candidate. ORPHA:730 maps to autosomal dominant polycystic kidney disease, and
local coverage exists in both `Autosomal_Dominant_Polycystic_Kidney_Disease.yaml`
and `Polycystic_Kidney_Disease.yaml#Autosomal Dominant PKD (ADPKD)`.

The standalone ADPKD file explicitly includes "GANAB pathogenic variants" as
causative and describes GANAB as an ADPKD-spectrum gene involved in glycoprotein
processing and polycystin maturation. The broader PKD file also lists "GANAB
Mutations" as a causative ADPKD gene with a milder phenotype.

## Concordance and completeness

Judgement: covered at the ADPKD disease-family level, with subtype-specific
curation caveats.

DisMech already has an appropriate ADPKD target and GANAB gene support. The
remaining gap is the IEMbase-specific "GANAB-CDG / alpha glucosidase II
deficiency" framing and the normal sialotransferrin readout, not the disease
placement itself.

## Curation actions

- Prefer `Autosomal_Dominant_Polycystic_Kidney_Disease.yaml` as the canonical
  local mapping.
- Do not create a duplicate GANAB-CDG disease outside the ADPKD spectrum unless
  source review supports distinct disease scope.
- Consider adding GANAB/PKD3 subtype notes and preserving adult kidney cyst,
  liver cyst, and normal sialotransferrin prompts.
