# IEMbase 0152: UMPS-related hereditary orotic aciduria

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 152 |
| Nosology | 16.1.03.01 |
| Gene | UMPS |
| External IDs | OMIM:258900; ORPHA:30 |
| Generated mapping | MAPPED to `Hereditary_Orotic_Aciduria.yaml` |
| Candidate DisMech targets | `Hereditary_Orotic_Aciduria.yaml` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents this as UMPS-related uridine monophosphate synthase
deficiency, with alternate labels hereditary orotic aciduria and orotate
phosphoribosyltransferase deficiency. Treatability is marked yes.

The biochemical rows include decreased red-cell UMPS/OPRT activity, increased
plasma orotic acid, markedly increased urinary orotic acid, and reticulocyte
abnormality. Clinical rows include megaloblastic anemia, hypochromia,
anisocytosis, poikilocytosis, developmental delay, failure to thrive, diarrhea,
T-cell immunodeficiency, recurrent infections, hematuria, and urolithiasis.

## DisMech phenotype coverage

`Hereditary_Orotic_Aciduria.yaml` is the correct target. It models biallelic
UMPS loss of function, deficient orotate phosphoribosyltransferase and/or
OMP decarboxylase activity, impaired de novo UMP synthesis, massive urinary
orotic acid overexcretion, megaloblastic anemia, global developmental delay,
failure to thrive, T-cell immunodeficiency, recurrent respiratory infections,
orotic acid crystalluria, and uridine triacetate therapy.

## Concordance and completeness

Judgement: correct mapping with high concordance.

The IEMbase and DisMech profiles agree on UMPS, orotic acid accumulation,
megaloblastic anemia, developmental delay, failure to thrive, T-cell
immunodeficiency, recurrent infection, and treatment by uridine replacement.
IEMbase adds plasma orotic acid and selected hematologic smear terms, plus
hematuria/urolithiasis wording that could be reviewed against the local
crystalluria-focused renal phenotype.

## Curation actions

- Keep the mapping to `Hereditary_Orotic_Aciduria.yaml`.
- Consider future biomarker refinement for plasma orotic acid and explicit
  red-cell UMPS/OPRT activity.
- Review whether IEMbase hematuria/urolithiasis should be represented locally
  as downstream consequences of orotic acid crystalluria or left as unconfirmed
  IEMbase-only clinical rows.
