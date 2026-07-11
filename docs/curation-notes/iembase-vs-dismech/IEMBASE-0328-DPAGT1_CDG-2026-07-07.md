# IEMbase 0328: DPAGT1-related UDP-GlcNAc:Dol-P-GlcNac-P transferase deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 328 |
| Nosology | 18.1.03.01 |
| Gene | DPAGT1 |
| External IDs | OMIM:608093; ORPHA:86309 |
| Generated mapping | UNMAPPED |
| Candidate DisMech targets | No valid local DPAGT1-CDG target; `Congenital_Myasthenic_Syndrome.yaml` is partial secondary context |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents DPAGT1-CDG/CDG-Ij. Characteristic rows include high-arched
palate, cataract, contractures, psychomotor retardation, and strabismus.
Additional clinical rows include congenital myasthenic syndrome, dysmorphism,
type 2 fiber tubular aggregates on muscle EM, epilepsy, exotropia, fatal
outcome, feeding difficulties, fetal hypokinesia phenotype, hypertonia,
hypotonia, intellectual disability, microcephaly, micrognathia, and nystagmus.

The biochemical rows include normal-to-increased creatine kinase and
transaminase, normal-to-increased asialotransferrin and disialotransferrin,
low-to-normal fibroblast lipid-linked Man9GlcNAc2, possible type 1
sialotransferrin pattern, low-to-normal tetrasialotransferrin, and decreased
antithrombin III. No treatment rows are present.

## DisMech phenotype coverage

DisMech has meaningful but incomplete context in `Congenital_Myasthenic_Syndrome.yaml`.
That entry includes DPAGT1 as a causal glycosylation-related CMS gene and
describes the N-linked glycosylation branch with tubular aggregates, elevated
CK, limb-girdle CMS, and neuromuscular-junction glycoprotein glycosylation
defects.

That coverage is not equivalent to a DPAGT1-CDG disease entry. IEMbase frames
DPAGT1 as a CDG-Ij disorder with systemic CDG features, fetal hypokinesia,
microcephaly, cataract/strabismus, abnormal transferrin, lipid-linked
Man9GlcNAc2, and antithrombin III abnormalities. The local CMS file captures
the neuromuscular branch but not the multisystem CDG biochemical entity.

## Concordance and completeness

Judgement: partial local neuromuscular context, but canonical DPAGT1-CDG remains
a local disease gap.

The generated UNMAPPED status is understandable because there is no dedicated
DPAGT1-CDG file. Manual curation should avoid collapsing DPAGT1-CDG into the
CMS umbrella: the IEMbase record combines CMS with broader congenital
glycosylation disease.

## Curation actions

- Add a standalone DPAGT1-CDG target before treating this record as fully
  mapped.
- Preserve `Congenital_Myasthenic_Syndrome.yaml` as secondary context for the
  CMS/tubular-aggregate/CK branch.
- Carry forward fetal hypokinesia, cataract/strabismus, microcephaly,
  Man9GlcNAc2, type I transferrin, and antithrombin III rows for future
  DPAGT1-CDG curation.
