# IEMbase 0298: SMPD1-related Acid sphingomyelinase deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 298 |
| Nosology | 20.1.03.01 |
| Gene | SMPD1 |
| External IDs | OMIM:257200; OMIM:607616; ORPHA:77292 |
| Generated mapping | CANDIDATE; `Niemann-Pick_Disease_Type_A.yaml` |
| Candidate DisMech targets | `Niemann-Pick_Disease_Type_A.yaml`; `Niemann-Pick_Disease_Type_B.yaml` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents the acid sphingomyelinase deficiency spectrum and explicitly
names Niemann-Pick type A as severe and type B as milder. Inheritance is
autosomal recessive and treatability is unknown in the cached record.

The phenotype rows mix type A and type B features: cherry red spot, deafness,
foam cells, hepatosplenomegaly, hypoxia, liver cirrhosis, lymphadenopathy,
pancytopenia, pulmonary interstitial changes, thrombocytopenia, vision loss or
optic atrophy, developmental delay, failure to thrive, feeding difficulties,
hypotonia, jaundice, and seizures. Biochemical rows show increased serum
lysosphingomyelin and decreased sphingomyelinase activity, with the greatest
enzyme reduction in neonatal rows.

## DisMech phenotype coverage

The generated type A candidate is biologically valid but incomplete for the
IEMbase label. Local DisMech has separate entries for the main SMPD1 spectrum
ends: `Niemann-Pick_Disease_Type_A.yaml` and
`Niemann-Pick_Disease_Type_B.yaml`.

The type A file covers profound SMPD1/acid sphingomyelinase deficiency,
lysosomal sphingomyelin and secondary lipid accumulation, hepatosplenomegaly,
failure to thrive, neurodegeneration, hypotonia, developmental regression, and
cherry red spot. The type B file covers residual enzyme activity, visceral and
pulmonary sphingomyelin storage, hepatosplenomegaly, thrombocytopenia,
interstitial lung disease, atherogenic dyslipidemia, short stature, delayed
puberty, osteopenia, and olipudase alfa enzyme replacement.

## Concordance and completeness

Judgement: split the IEMbase spectrum record across local type A and type B
coverage; do not treat the generated type A candidate as complete.

IEMbase and DisMech agree on SMPD1 causality, recessive inheritance, acid
sphingomyelinase deficiency, lysosomal sphingomyelin storage, foam-cell
visceral disease, hepatosplenomegaly, thrombocytopenia/cytopenias, pulmonary
interstitial disease, neurologic severe-infantile disease, hypotonia,
developmental delay/regression, cherry red spot, and failure to thrive.

DisMech is more precise because it keeps type A and type B as distinct local
entities with different residual-enzyme, CNS, pulmonary, and treatment
implications. IEMbase adds useful spectrum-level prompts for deafness, hypoxia,
liver cirrhosis, lymphadenopathy, pancytopenia, vision loss/optic atrophy,
feeding difficulty, jaundice, lysosphingomyelin, and age-stratified enzyme
severity.

## Curation actions

- Resolve this record as spectrum-level coverage spanning
  `Niemann-Pick_Disease_Type_A.yaml` and `Niemann-Pick_Disease_Type_B.yaml`.
- Avoid importing type B pulmonary/visceral rows into the type A file without
  subtype context, and avoid importing severe neurologic type A rows into type B.
- Review lysosphingomyelin and the IEMbase type-specific clinical rows for
  possible addition to the appropriate local subtype files.
