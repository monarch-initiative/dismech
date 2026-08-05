# IEMbase 0647: FKRP-related muscular dystrophy-dystroglycanopathy type C

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 647 |
| Nosology | 18.2.09.04 |
| Gene | FKRP |
| External IDs | OMIM:606596; ORPHA:34515 |
| Generated mapping | UNMAPPED; weak candidate `Dystroglycanopathy.yaml` |
| Candidate DisMech targets | `Dystroglycanopathy.yaml`; `Autosomal_Recessive_Limb-Girdle_Muscular_Dystrophy.yaml#LGMDR9` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents this row as FKRP-CDG type C, the limb-girdle muscular
dystrophy end of the FKRP dystroglycanopathy spectrum.

Biochemical rows include markedly increased plasma creatine kinase and normal
serum sialotransferrins. Clinical rows include obligate limb-girdle muscular
dystrophy, calf muscle hypertrophy becoming more prominent in adolescence and
adulthood, optional cardiomyopathy, optional myoglobinuria, optional
respiratory failure after infancy, optional tongue hypertrophy after infancy,
and optional spinal abnormalities.

## DisMech phenotype coverage

`Dystroglycanopathy.yaml` includes FKRP (`MDDG5`) and type C
dystroglycanopathy, with elevated CK, muscular dystrophy, proximal weakness,
cardiac/respiratory complications in the spectrum, and FKRP-specific treatment
context.

`Autosomal_Recessive_Limb-Girdle_Muscular_Dystrophy.yaml` also has a specific
`LGMDR9` subtype for FKRP-related dystroglycanopathy / LGMD2I. That entry
captures biallelic FKRP variants, limb-girdle muscle weakness, elevated CK,
cardiomyopathy, respiratory insufficiency, and calf hypertrophy. It does not
clearly preserve myoglobinuria or tongue hypertrophy.

## Concordance and completeness

Judgement: covered locally, despite generated `UNMAPPED` status.

This is the strongest local match in the batch: the disease is represented by
both the dystroglycanopathy spectrum entry and an FKRP-specific recessive LGMD
subtype. Remaining incompleteness is phenotype granularity rather than a missing
anchor.

## Curation actions

- Treat as covered by `Dystroglycanopathy.yaml` and
  `Autosomal_Recessive_Limb-Girdle_Muscular_Dystrophy.yaml#LGMDR9`.
- Consider updating the mapping rules to recognize the FKRP/LGMD2I target.
- Preserve CK, normal sialotransferrins, limb-girdle weakness, calf hypertrophy,
  cardiomyopathy, respiratory failure, spinal abnormalities, myoglobinuria, and
  tongue hypertrophy prompts.
