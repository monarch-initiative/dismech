# IEMbase 0485: SLC37A4-related glucose-6-phosphate transporter deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 485 |
| Nosology | 3.4.04.01 |
| Gene | SLC37A4 |
| External IDs | OMIM:232220; ORPHA:79259 |
| Generated mapping | CANDIDATE; medium candidate `Glycogen_Storage_Disease_Type_I.yaml` |
| Candidate DisMech targets | `Glycogen_Storage_Disease_Type_I.yaml#GSD Ib (glucose-6-phosphate transporter deficiency)` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents autosomal recessive SLC37A4-related glucose-6-phosphate
transporter deficiency as GSD Ib / GSD I non-a. Treatments include fasting
avoidance, uncooked cornstarch, granulocyte colony-stimulating factor, liver
transplantation, empagliflozin, and hematopoietic stem cell transplant.
Biochemical rows overlap GSD Ia for glucose/lactate/lipid/urate/liver glycogen
abnormalities and add decreased neutrophil count plus increased plasma and
urine 1,5-anhydroglucitol-6-phosphate. Clinical rows include anemia, leukocyte
function impairment, recurrent infections, bleeding tendency, diarrhea, liver
adenoma/carcinoma, renal complications, osteopenia, pancreatitis, pulmonary
hypertension, short stature, tachypnea, delayed tooth eruption, and
taurodontism.

## DisMech phenotype coverage

`Glycogen_Storage_Disease_Type_I.yaml#GSD Ib (glucose-6-phosphate transporter
deficiency)` is the exact local target. The entry models SLC37A4/G6PT deficiency
as the GSD Ib subtype, the shared GSD I metabolic branch, and the GSD Ib-specific
neutropenia / neutrophil dysfunction branch with recurrent infections, oral
ulcers, mucosal lesions, and inflammatory bowel disease context. It includes
uncooked cornstarch, granulocyte colony-stimulating factor, empagliflozin for
GSD Ib neutropenia, liver transplantation, kidney transplantation, and other
metabolic complication treatments.

## Concordance and completeness

Judgement: accept generated candidate as correct subtype-level coverage.

The generated mapper treated this only as a medium disease-level candidate, but
the local GSD I file has an explicit GSD Ib subtype and SLC37A4 mechanisms. The
resources agree on the shared fasting hypoglycemia/metabolic GSD I phenotype,
the distinguishing neutropenia/neutrophil-dysfunction arm, infection risk,
cornstarch, G-CSF, empagliflozin, and liver-transplant context. IEMbase adds
important enrichment prompts, especially 1,5-anhydroglucitol-6-phosphate,
biotinidase, hematopoietic stem cell transplant, delayed tooth eruption,
taurodontism, and some renal/hepatic complication granularity.

## Curation actions

- Resolve this row to
  `Glycogen_Storage_Disease_Type_I.yaml#GSD Ib (glucose-6-phosphate transporter deficiency)`.
- Treat broad disease-level `Glycogen_Storage_Disease_Type_I.yaml` as acceptable
  only if the subtype anchor is preserved.
- Verify 1,5-anhydroglucitol-6-phosphate, hematopoietic stem cell transplant,
  biotinidase, delayed tooth eruption, and taurodontism before structural import.
