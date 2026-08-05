# IEMbase 0644: FKTN-related muscular dystrophy-dystroglycanopathy type C

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 644 |
| Nosology | 18.2.08.03 |
| Gene | FKTN |
| External IDs | OMIM:611588; ORPHA:272 |
| Generated mapping | UNMAPPED; weak candidate `Dystroglycanopathy.yaml` |
| Candidate DisMech targets | `Dystroglycanopathy.yaml`; possible future LGMD subtype context |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents this as autosomal recessive FKTN-CDG type C, the limb-girdle
muscular dystrophy end of the FKTN dystroglycanopathy spectrum.

Biochemical rows include markedly increased plasma creatine kinase across ages
and normal serum sialotransferrins. Clinical rows emphasize limb-girdle
muscular dystrophy, optional hypotonia, optional cardiomyopathy, and optional
rigid spine from childhood onward.

## DisMech phenotype coverage

`Dystroglycanopathy.yaml` captures the FKTN gene subtype (`MDDG4`) and the type
C severity subtype. It represents defective alpha-dystroglycan glycosylation,
elevated CK, muscular dystrophy, proximal weakness, and the continuous severity
gradient from severe congenital disease to limb-girdle disease.

`Autosomal_Recessive_Limb-Girdle_Muscular_Dystrophy.yaml` has a specific FKRP
LGMDR9 subtype but does not appear to include an FKTN limb-girdle subtype.
Therefore, the best current local target remains `Dystroglycanopathy.yaml`
rather than the AR LGMD file.

## Concordance and completeness

Judgement: broad local coverage; missing exact FKTN limb-girdle row.

DisMech covers the mechanism and the type C category, but the exact FKTN type C
/ limb-girdle entity is not rooted as its own local subtype. IEMbase-specific
prompts that would improve future curation include rigid spine and explicit
cardiomyopathy in the FKTN limb-girdle context.

## Curation actions

- Map broadly to `Dystroglycanopathy.yaml`.
- Do not map to AR LGMD unless an FKTN-specific recessive LGMD subtype is added
  there.
- Preserve CK, normal sialotransferrins, limb-girdle muscular dystrophy,
  hypotonia, cardiomyopathy, and rigid-spine prompts.
