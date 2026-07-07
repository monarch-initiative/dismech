# IEMbase 0115: ALAD-related delta-aminolevulinate dehydratase deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 115 |
| Nosology | 17.1.03.01 |
| Gene | ALAD |
| External IDs | OMIM:125270; ORPHA:100924 |
| Generated mapping | MAPPED, high confidence |
| Candidate DisMech targets | `Porphyria_due_to_ALA_Dehydratase_Deficiency.yaml`; secondary umbrella subtype in `Inherited_Porphyria.yaml#Porphyria due to ALA Dehydratase Deficiency` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents this as ALAD-related delta-aminolevulinate dehydratase
deficiency, with alternate labels Doss porphyria, porphobilinogen synthase
deficiency, and ALAD. Treatability is marked yes.

The characteristic biochemical rows are markedly decreased red-blood-cell
delta-ALA dehydratase, increased urinary delta-ALA, and increased urinary
coproporphyrin III. Clinical rows include coma, constipation, hyperesthesia,
hypertension, motor neuropathy, nausea, renal failure, tachycardia, and
vomiting. Treatments listed are heme arginate infusion and hydroxyurea.

## DisMech phenotype coverage

`Porphyria_due_to_ALA_Dehydratase_Deficiency.yaml` is the correct canonical
target. It models biallelic ALAD pathogenic variants, reduced porphobilinogen
synthase activity, markedly reduced erythrocyte ALAD activity, upstream ALA
accumulation, urinary coproporphyrins, acute neurovisceral attacks, and the key
diagnostic distinction from AIP: little or no PBG overproduction.

The local treatment section directly covers hemin/heme arginate, glucose or
carbohydrate loading, the uncertain status of givosiran in ADP, and
hydroxyurea as an experimental erythroid-directed option.

## Concordance and completeness

Judgement: correct standalone mapping with high biochemical concordance.

The overlap is strong for ALAD enzyme deficiency, urinary ALA, coproporphyrin
abnormality, acute neurovisceral symptoms, and heme arginate. DisMech is richer
for mechanism and for distinguishing inherited ADP from AIP and acquired ALAD
inhibition. IEMbase adds a few clinical rows that could be surfaced more
explicitly in the standalone entry, especially hyperesthesia, hypertension,
tachycardia, renal failure, and coma.

## Curation actions

- Keep `Porphyria_due_to_ALA_Dehydratase_Deficiency.yaml` as the canonical
  target.
- Keep the inherited porphyria umbrella subtype as secondary classification
  context.
- Review IEMbase's autonomic, renal, and severe encephalopathic rows for future
  ADP phenotype expansion.
