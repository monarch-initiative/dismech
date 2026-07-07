# IEMbase 0479: SLC5A2-related sodium-glucose cotransporter 2 deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 479 |
| Nosology | 3.6.08.01 |
| Gene | SLC5A2 |
| External IDs | OMIM:233100; ORPHA:69076 |
| Generated mapping | UNMAPPED; best candidate `Glycogen_Storage_Disease_Type_I.yaml` |
| Candidate DisMech targets | `Familial_Renal_Glucosuria.yaml`; rejected lexical candidate `Glycogen_Storage_Disease_Type_I.yaml` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents SLC5A2-related sodium-glucose cotransporter 2 deficiency as
familial renal glucosuria type 1 / SGLT2 deficiency. It lists autosomal
recessive inheritance. The biochemical rows are focused and renal: urinary
glucose is increased across ages, plasma glucose is normal, and urinary amino
acids are normal to increased. No clinical or treatment rows are recorded.

## DisMech phenotype coverage

`Familial_Renal_Glucosuria.yaml` is the exact local target, even though the
generated mapper missed it. The local entry models familial renal glucosuria as
persistent isolated glucosuria without hyperglycemia and without generalized
Fanconi-type proximal tubulopathy, with a specific `SLC5A2-Related` subtype. It
captures SLC5A2/SGLT2 loss of function, reduced proximal tubular glucose
reabsorption, normal blood glucose with glucosuria, and occasional volume
depletion / renin-angiotensin-aldosterone activation in high-glucosuria cases.

## Concordance and completeness

Judgement: false negative generated mapping; resolve to
`Familial_Renal_Glucosuria.yaml#SLC5A2-Related`.

The GSD I candidate is a lexical/metabolic false positive. GSD I and GSD Ib have
fasting hypoglycemia, liver/kidney glycogen-storage disease, and broad secondary
metabolic derangements, while SLC5A2 familial renal glucosuria is an isolated
renal glucose-reabsorption defect with normal plasma glucose. The main
discordance is inheritance: IEMbase simplifies this row as autosomal recessive,
whereas the local entry records semidominant/codominant inheritance with
incomplete penetrance for SLC5A2-related disease.

## Curation actions

- Treat this as covered by `Familial_Renal_Glucosuria.yaml#SLC5A2-Related`.
- Reject `Glycogen_Storage_Disease_Type_I.yaml` as an exact mapping.
- Preserve the inheritance discrepancy as a review flag rather than overwriting
  the local semidominant/incomplete-penetrance model.
