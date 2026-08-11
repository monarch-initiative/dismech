# IEMbase 0507: APOE-related dysbetalipoproteinemia

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 507 |
| Nosology | 15.3.13.01 |
| Gene | APOE |
| External IDs | OMIM:617347; ORPHA:412 |
| Generated mapping | UNMAPPED; no candidate |
| Candidate DisMech targets | Partial context in `Hyperlipidemia.yaml` and `Sea-Blue_Histiocyte_Syndrome.yaml` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents autosomal recessive APOE-related apolipoprotein E deficiency
as dysbetalipoproteinemia / hyperlipoproteinemia type 3. Treatment rows include
atorvastatin, bezafibrate, ciprofibrate, ezetimibe, fenofibrate, gemfibrozil,
lipid-lowering diet, nicotinic acid, rosuvastatin, and simvastatin.
Biochemical rows include adult markedly increased serum cholesterol,
normal-to-low HDL cholesterol, positive broad beta lipoprotein electrophoresis,
and increased serum triglyceride. Clinical rows include palmar xanthomas,
tuberoeruptive xanthomas, carotid bruits, femoral bruits, intermittent
claudication, myocardial ischemia, and sea-blue histiocytes.

## DisMech phenotype coverage

No exact local target was found. `Hyperlipidemia.yaml` provides partial context:
it models broad dyslipidemia, apoB-containing lipoprotein/remnant biology,
atherogenic vascular consequences, statins, fibrates, ezetimibe, lifestyle
management, and an APOE genetic note that APOE e2 can cause type III
hyperlipoproteinemia. However, the entry does not define a dysbetalipoproteinemia
or hyperlipoproteinemia type III subtype and does not model broad beta
electrophoresis, palmar/tuberoeruptive xanthomas, or APOE deficiency as an exact
Mendelian/oligogenic disease entity.

`Sea-Blue_Histiocyte_Syndrome.yaml` also provides partial context because it
models APOE-associated primary sea-blue histiocytosis and hypertriglyceridemia,
but that entry is about lipid-laden marrow histiocytes and primary sea-blue
histiocyte syndrome rather than familial dysbetalipoproteinemia.

## Concordance and completeness

Judgement: partial local context only; exact APOE dysbetalipoproteinemia local
gap.

The current KB can explain several downstream lipid and vascular consequences,
but it lacks the disease identity that IEMbase is asking for: APOE-related
dysbetalipoproteinemia / type III hyperlipoproteinemia with remnant
lipoprotein accumulation and broad beta electrophoresis. The sea-blue
histiocyte signal should be handled carefully because it can be a feature or
related morphology, but the existing APOE sea-blue histiocytosis entry is not
the same disease.

## Curation actions

- Do not map this record as fully covered by `Hyperlipidemia.yaml` or
  `Sea-Blue_Histiocyte_Syndrome.yaml`.
- Track APOE-related dysbetalipoproteinemia / hyperlipoproteinemia type III as
  an exact local gap or as a potential new subtype under the hyperlipidemia
  entry after scope review.
- Preserve IEMbase prompts for broad beta electrophoresis, palmar and
  tuberoeruptive xanthomas, intermittent claudication, bruits, myocardial
  ischemia, sea-blue histiocytes, and the listed lipid-lowering therapies.
