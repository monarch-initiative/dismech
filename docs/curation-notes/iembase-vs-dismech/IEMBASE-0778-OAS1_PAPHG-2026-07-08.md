# IEMbase 0778: OAS1-related 2-prime,5-prime-oligoadenylate synthetase 1 deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 778 |
| Nosology | 16.3.1.01 |
| Nosology code | IEM0035 |
| Gene | OAS1 |
| External IDs | OMIM:222100 |
| Generated mapping | UNMAPPED; weak candidate `Holocarboxylase_Synthetase_Deficiency.yaml` |
| Candidate DisMech targets | None accepted; broad phenotype overlap only with hereditary PAP entries |
| Review date | 2026-07-08 |

## IEMbase phenotype signal

IEMbase labels this autosomal dominant record as OAS1-related
2-prime,5-prime-oligoadenylate synthetase 1 deficiency, with alternate name
infantile-onset pulmonary alveolar proteinosis with hypogammaglobulinemia
(PAPHG). The source signal combines pulmonary alveolar proteinosis, recurrent
respiratory infections, respiratory failure, increased susceptibility to viral
infection, failure to thrive, splenomegaly, early death, small non-foamy
alveolar macrophages on bronchoalveolar lavage, low IgG/immunoglobulins, and a
low leukocyte laboratory row. The source clinical table labels a leukocytosis
row, which conflicts with the low leukocyte laboratory direction and should be
reviewed.

## DisMech phenotype coverage

No local DisMech disease represents OAS1/PAPHG. The generated candidate,
`Holocarboxylase_Synthetase_Deficiency.yaml`, is a different HLCS
biotin-dependent multiple carboxylase deficiency and should be rejected despite
weak lexical similarity.

`Hereditary_Pulmonary_Alveolar_Proteinosis.yaml` overlaps phenotypically for
pulmonary alveolar proteinosis, failure to thrive, respiratory failure, and
infection risk, but it is explicitly a CSF2RA/CSF2RB GM-CSF receptor disorder
with autosomal recessive inheritance and foamy macrophage/surfactant-clearance
biology. It does not cover OAS1, autosomal dominant inheritance,
hypogammaglobulinemia, viral susceptibility, leukopenia, or the small
non-foamy macrophage signal.

## Concordance and completeness

Judgement: true local gap; reject the holocarboxylase candidate and do not
collapse into hereditary PAP.

The pulmonary phenotype overlap is not sufficient for disease coverage because
the gene, inheritance, immune phenotype, and macrophage biology differ. This is
best treated as a missing OAS1/PAPHG entity, with hereditary PAP as a future
differential/neighbor rather than a mapping target.

## Curation actions

- Treat IEMbase 0778 as an unmapped OAS1/PAPHG gap.
- Reject `Holocarboxylase_Synthetase_Deficiency.yaml` as a false candidate.
- Do not use `Hereditary_Pulmonary_Alveolar_Proteinosis.yaml` as exact coverage;
  retain it only as broad pulmonary phenotype context.
- If curated later, preserve hypogammaglobulinemia, viral susceptibility,
  leukocyte-count ambiguity, small non-foamy alveolar macrophages, respiratory
  failure, splenomegaly, and early death.
