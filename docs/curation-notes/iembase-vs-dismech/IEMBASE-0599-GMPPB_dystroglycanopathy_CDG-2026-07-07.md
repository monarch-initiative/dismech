# IEMbase 0599: GMPPB-related muscular dystrophy-dystroglycanopathy

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 599 |
| Nosology | 18.4.02.01 |
| Gene | GMPPB |
| External IDs | OMIM:615350; OMIM:615351; OMIM:615352; ORPHA:588 |
| Generated mapping | CANDIDATE; `Dystroglycanopathy.yaml` |
| Candidate DisMech targets | `Dystroglycanopathy.yaml#MDDG14 (GMPPB)`; `Congenital_Myasthenic_Syndrome.yaml#GMPPB` (secondary context) |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents GMPPB-related muscular dystrophy-dystroglycanopathy, also
labelled GMPPB-CDG and MDDGA. The record is autosomal recessive, classified
under multiple glycosylation pathways, has unknown treatability, and has no
treatment rows.

Biochemical rows include increased plasma creatine kinase and muscle
hypoglycosylation of alpha-dystroglycan. Clinical rows include hypotonia, muscle
weakness, limb-girdle muscular dystrophy, congenital myasthenic syndrome,
cataract, epilepsy, cerebellar hypoplasia, microcephaly, intellectual
disability, and myoglobinuria.

## DisMech phenotype coverage

`Dystroglycanopathy.yaml` is a valid local target at subtype level. It models the
muscular dystrophy-dystroglycanopathy spectrum caused by defective
O-mannosylation of alpha-dystroglycan, and explicitly includes `MDDG14 (GMPPB)`,
where GMPPB supplies GDP-mannose for the dystroglycan glycosylation pathway. It
also includes reduced alpha-dystroglycan glycosylation and broad brain, eye,
muscle, seizure, and CK coverage.

`Congenital_Myasthenic_Syndrome.yaml` provides secondary context because it
includes GMPPB among glycosylation-related CMS genes and describes the
myasthenic-myopathic limb-girdle presentation. That entry is not the primary
disease target for IEMbase 0599, but it is relevant for the congenital
myasthenic-syndrome phenotype row.

## Concordance and completeness

Judgement: accept the generated candidate as subtype-level local coverage, with
secondary CMS context.

The IEMbase record and DisMech agree on gene, recessive inheritance,
alpha-dystroglycan hypoglycosylation, muscular dystrophy, and the
myasthenic-myopathic overlap. IEMbase adds a concise checklist of GMPPB-specific
review prompts that are not all explicit in the local subtype block.

## Curation actions

- Map to `Dystroglycanopathy.yaml#MDDG14 (GMPPB)` for disease-level import.
- Use `Congenital_Myasthenic_Syndrome.yaml#GMPPB` only as secondary phenotype
  context for the CMS overlap.
- Preserve creatine kinase, alpha-dystroglycan hypoglycosylation, cataract,
  cerebellar hypoplasia, microcephaly, epilepsy, intellectual disability,
  myoglobinuria, limb-girdle weakness, and CMS rows as source-review prompts.
