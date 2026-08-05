# IEMbase 0767: HPGD-related 15-hydroxy-prostaglandin dehydrogenase deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 767 |
| Nosology | 14.3.02.01 |
| Nosology code | IEM0685 |
| Gene | HPGD |
| External IDs | OMIM:259100; OMIM:119900; ORPHA:217059 |
| Generated mapping | CANDIDATE; `Primary_Hypertrophic_Osteoarthropathy.yaml` |
| Candidate DisMech targets | `Primary_Hypertrophic_Osteoarthropathy.yaml` subtype PHOAR1 |
| Review date | 2026-07-08 |

## IEMbase phenotype signal

IEMbase labels this autosomal recessive record as HPGD-related
15-hydroxy-prostaglandin dehydrogenase deficiency, with alternate name primary
hypertrophic osteoarthropathy type 1 and abbreviation PHOAR1. The source signal
includes high urinary prostaglandin E2 across all age bands, normal urinary
prostaglandin M, digital clubbing, pachydermia, periostitis, arthralgia,
arthritis, swollen joints, thickened skin, hand/foot enlargement, coarse facial
features, cranial suture defects, hyperhidrosis, and patent ductus arteriosus.

## DisMech phenotype coverage

`Primary_Hypertrophic_Osteoarthropathy.yaml` is the correct local target. It
models PHO as an HPGD/SLCO2A1 prostaglandin E2 metabolism disorder and includes
a PHOAR1 subtype for biallelic HPGD loss-of-function. The local pathophysiology
captures defective PGE2 degradation, elevated PGE2, periosteal new bone
formation, connective tissue proliferation, and phenotypes including digital
clubbing, periostosis, pachydermia, cutis verticis gyrata, arthralgia,
hyperhidrosis, joint swelling, delayed cranial suture closure, anemia, peptic
ulcer, and patent ductus arteriosus.

## Concordance and completeness

Judgement: exact subtype coverage; generated candidate should be accepted.

The disease identity, gene, inheritance, PGE2 mechanism, and clinical triad are
strongly concordant. The main discrepancy is biochemical: IEMbase records
urinary prostaglandin M as normal for HPGD/PHOAR1, while the local PHO entry
models decreased urinary PGE-M in PHOAR1 and elevated PGE-M in PHOAR2. That
difference should be reviewed before converting IEMbase's PGE-M row into a
curated biochemical assertion.

## Curation actions

- Treat `Primary_Hypertrophic_Osteoarthropathy.yaml` subtype PHOAR1 as exact
  local coverage.
- Review the IEMbase normal urinary prostaglandin M row against local decreased
  PHOAR1 PGE-M evidence before making any KB change.
- Preserve hand/foot enlargement, coarse facial features, arthritis, and
  cranial suture defects as phenotype-completeness prompts.
