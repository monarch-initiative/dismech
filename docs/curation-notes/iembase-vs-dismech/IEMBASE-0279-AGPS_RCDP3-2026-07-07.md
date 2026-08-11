# IEMbase 0279: AGPS-related RCDP type 3

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 279 |
| Nosology | 14.5.03.03 |
| Gene | AGPS |
| External IDs | OMIM:600121; ORPHA:309803 |
| Generated mapping | MAPPED to `Rhizomelic_Chondrodysplasia_Punctata_Plasmalogen_Synthesis_Defect.yaml#RCDP3` |
| Candidate DisMech targets | `Rhizomelic_Chondrodysplasia_Punctata_Plasmalogen_Synthesis_Defect.yaml#RCDP3` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents autosomal recessive AGPS-related alkylglycerone
3-phosphate synthase deficiency, also called RCDP type 3. Prevalence is listed
as 1:100,000. Treatability is marked unknown and there are no treatment rows in
the cached JSON.

Characteristic clinical rows include cataract, cervical stenosis, contractures,
joint contractures, coronal clefts of thoracic and lumbar vertebral bodies,
dysmorphic features, epiphyseal dysplasia, growth retardation, metaphyseal
dysplasia, skeletal dysplasia, and disproportionate shortening of the humeri
and femora. Additional rows include epiphyseal calcific stippling, congenital
heart defects, sensorineural deafness, epilepsy, ichthyosis, recurrent
pneumonia/otitis, microcephaly, severe intellectual deficiency, spastic paresis,
full cheeks, hypertelorism, midface hypoplasia, and small nose with upturned
nostrils.

The biochemical pattern is low RBC plasmalogens with normal VLCFA and bile-acid
intermediates. IEMbase also lists phytanic acid as normal to increased and
pristanic acid as low to normal.

## DisMech phenotype coverage

`Rhizomelic_Chondrodysplasia_Punctata_Plasmalogen_Synthesis_Defect.yaml#RCDP3`
is the correct local target. The local entry explicitly includes AGPS/RCDP3,
describes the alkyl-DHAP synthase block in the plasmalogen-synthesis pathway,
and covers decreased plasmalogens, preserved phytanic-acid alpha-oxidation,
skeletal dysplasia, cataract, neurologic impairment, rhizomelia,
chondrodysplasia punctata, coronal cleft vertebrae, growth deficiency,
intellectual disability, seizures, microcephaly, spasticity, molecular testing,
enzyme/complementation subtyping, supportive care, and cataract extraction.

## Concordance and completeness

Judgement: correct subtype-level mapping with high concordance.

IEMbase and DisMech agree on AGPS/RCDP3 identity, autosomal recessive
inheritance, decreased plasmalogens, normal VLCFA/bile-acid rows, cataract,
rhizomelic skeletal dysplasia, epiphyseal dysplasia/stippling, coronal clefts,
growth failure, intellectual disability, seizures, microcephaly, and spastic
motor involvement. DisMech is richer for pathway-level mechanism and subtyping.

IEMbase adds AGPS-specific facial detail, cervical stenosis, congenital heart
defect, recurrent infection, sensorineural deafness, and ichthyosis prompts.
As for RCDP2, the normal-to-increased phytanic acid row should be reviewed
before import because preserved phytanic-acid alpha-oxidation is a key local
distinction from PEX7/RCDP1.

## Curation actions

- Keep the mapping to the local RCDP3 subtype.
- Use IEMbase's craniofacial, cervical-spine, infection, hearing, cardiac, and
  skin rows as enrichment prompts.
- Do not import phytanic-acid increase for RCDP3 without subtype-specific
  evidence review.
