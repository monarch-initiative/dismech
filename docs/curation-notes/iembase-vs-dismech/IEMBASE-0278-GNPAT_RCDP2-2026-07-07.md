# IEMbase 0278: GNPAT-related RCDP type 2

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 278 |
| Nosology | 14.5.03.02 |
| Gene | GNPAT |
| External IDs | OMIM:602744; ORPHA:309796 |
| Generated mapping | MAPPED to `Rhizomelic_Chondrodysplasia_Punctata_Plasmalogen_Synthesis_Defect.yaml#RCDP2` |
| Candidate DisMech targets | `Rhizomelic_Chondrodysplasia_Punctata_Plasmalogen_Synthesis_Defect.yaml#RCDP2` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents autosomal recessive GNPAT-related glycerone
3-phosphate acyltransferase deficiency, also called RCDP type 2. Prevalence is
listed as 1:100,000. Treatability is marked unknown and there are no treatment
rows in the cached JSON.

Characteristic clinical rows include cataract, cervical stenosis, coronal
clefts of thoracic and lumbar vertebral bodies, dysmorphic features,
epiphyseal dysplasia, joint contractures, metaphyseal dysplasia, skeletal
dysplasia, and disproportionate shortening of humeri and femora. Additional
rows include anteverted nares, high arched palate, broad nasal bridge,
dysplastic ears, epicanthal folds, micrognathia, epiphyseal calcific
stippling, growth retardation, congenital heart defects, sensorineural
deafness, epilepsy, ichthyosis, recurrent pneumonia/otitis, microcephaly,
severe intellectual deficiency, contractures, and spastic paresis.

The biochemical pattern is low RBC plasmalogens with normal VLCFA and bile-acid
intermediates. IEMbase also lists phytanic acid as normal to increased and
pristanic acid as low to normal.

## DisMech phenotype coverage

`Rhizomelic_Chondrodysplasia_Punctata_Plasmalogen_Synthesis_Defect.yaml#RCDP2`
is the correct local target. The local entry groups GNPAT, AGPS, and FAR1
single-enzyme plasmalogen-synthesis defects and explicitly distinguishes them
from PEX7/RCDP1. It covers GNPAT/DHAPAT deficiency, plasmalogen deficiency,
preserved phytanic-acid alpha-oxidation, skeletal dysplasia, cataract,
neurologic impairment, rhizomelia, chondrodysplasia punctata, coronal cleft
vertebrae, growth deficiency, intellectual disability, seizures, microcephaly,
spasticity, molecular testing, enzyme/complementation subtyping, supportive
care, and cataract extraction.

## Concordance and completeness

Judgement: correct subtype-level mapping with high concordance.

IEMbase and DisMech agree on GNPAT/RCDP2 identity, autosomal recessive
inheritance, decreased plasmalogens, normal VLCFA/bile-acid rows, cataract,
rhizomelic skeletal dysplasia, epiphyseal stippling/dysplasia, coronal clefts,
growth failure, intellectual disability, seizures, microcephaly, and spastic
motor involvement. DisMech is stronger for mechanism and for distinguishing
single-enzyme plasmalogen defects from PEX7 import defects.

IEMbase adds subtype-specific craniofacial, cervical stenosis, congenital
heart, recurrent infection, hearing, and ichthyosis prompts. The IEMbase
normal-to-increased phytanic acid row needs caution because the local
plasmalogen-synthesis entry treats preserved phytanic-acid alpha-oxidation as a
key discriminator from PEX7/RCDP1.

## Curation actions

- Keep the mapping to the local RCDP2 subtype.
- Use IEMbase's craniofacial, cervical-spine, infection, hearing, cardiac, and
  skin rows as enrichment prompts.
- Do not import phytanic-acid increase for RCDP2 without subtype-specific
  evidence review.
