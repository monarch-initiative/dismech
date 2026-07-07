# IEMbase 0281: PHYH-related Phytanoyl-CoA hydroxylase deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 281 |
| Nosology | 14.2.06.01 |
| Gene | PHYH |
| External IDs | OMIM:266500; ORPHA:773 |
| Generated mapping | MAPPED; `Adult_Refsum_Disease.yaml` |
| Candidate DisMech targets | `Adult_Refsum_Disease.yaml` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents classic Refsum disease / PHYH-related phytanoyl-CoA
hydroxylase deficiency. Inheritance is autosomal recessive and treatability is
marked yes, although the cached JSON has no specific treatment rows.

The characteristic biochemical pattern is increased serum phytanic acid, with
increased pristanic acid and increased serum and urinary pipecolic acid also
listed. Clinical rows include anosmia, ataxia, ichthyosis, sensory disturbance,
paresis, muscular atrophy, spinal muscular atrophy wording, neurocognitive and
behavioral issues, skeletal malformations, low-set ears, midface hypoplasia,
and hematuria.

## DisMech phenotype coverage

`Adult_Refsum_Disease.yaml` is the correct local target. The DisMech entry
models PHYH and PEX7-related disruption of peroxisomal phytanic acid
alpha-oxidation, elevated plasma and tissue phytanic acid, exogenous phytanic
acid retention, and the downstream neurologic, retinal, dermatologic, skeletal,
cardiac, and renal phenotype pattern.

Local phenotypes include sensorineural hearing impairment, anosmia, retinopathy,
visual impairment, ptosis, cataract, progressive visual loss, nystagmus,
nyctalopia, ichthyosis/dry skin, ataxia, hypotonia, cardiomyopathy,
arrhythmia/heart block, splenomegaly, pes cavus, hammertoe, respiratory
insufficiency, nail dysplasia, developmental regression, skeletal dysplasia,
skeletal muscle atrophy, hemiparesis, pyramidal signs, peripheral neuropathy,
severe intellectual disability, and renal insufficiency. Local treatment
coverage is stronger than IEMbase: phytanic-acid-restricted diet with fasting
avoidance, plus plasmapheresis or lipid apheresis for severe acute worsening.

## Concordance and completeness

Judgement: correct high-confidence mapping to `Adult_Refsum_Disease.yaml`.

IEMbase and DisMech agree on PHYH/classic Refsum identity, autosomal recessive
inheritance, phytanic acid accumulation, anosmia, ataxia, ichthyosis, sensory
and motor neurologic involvement, skeletal involvement, and renal signal.
DisMech is substantially richer for mechanism, ocular detail, cardiac
conduction/cardiomyopathy, treatment, and diagnostic interpretation.

IEMbase adds useful review prompts for pristanic acid, pipecolic acid, low-set
ears, midface hypoplasia, hematuria, and the spinal-muscular-atrophy wording.
Those should be checked against primary Refsum sources before any import,
especially because some may reflect broader peroxisomal or PEX7-associated
context rather than core PHYH adult Refsum disease.

## Curation actions

- Keep this record mapped to `Adult_Refsum_Disease.yaml`.
- Consider adding pristanic acid and pipecolic acid as secondary biochemical
  review prompts if supported in Refsum-specific sources.
- Review the IEMbase craniofacial, hematuria, and spinal muscular atrophy rows
  cautiously before importing them into the local entry.
