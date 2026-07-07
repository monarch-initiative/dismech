# IEMbase 0598: GMPPA-related GDP-mannose pyrophosphorylase B deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 598 |
| Nosology | 18.4.01.03 |
| Gene | GMPPA |
| External IDs | OMIM:615510; ORPHA:869 |
| Generated mapping | UNMAPPED; best candidate `CHIME_syndrome.yaml` |
| Candidate DisMech targets | None exact |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents GMPPA-related GDP-mannose pyrophosphorylase B deficiency
(CDG), with alternate labels GMPPA-CDG, alacrima-achalasia-mental retardation
syndrome, and AAMR. The record is autosomal recessive, classified under
disorders of multiple glycosylation pathways, has unknown treatability, and has
no treatment rows.

The biochemical row reports normal serum sialotransferrins. Clinical rows
include facial dysmorphism, growth retardation, impaired hearing, postural
hypotension, hypotonia, prominent forehead, protruding chin, short philtrum,
thin lips with downturned mouth corners, triangular/asymmetric facies,
achalasia, alacrima, developmental delay, dysphagia, gait disturbance,
intellectual disability, ocular abnormalities, and regurgitation.

## DisMech phenotype coverage

`CHIME_syndrome.yaml` is a false-positive generated candidate. CHIME models
PIGL-related GPI-anchor biosynthesis disease with coloboma, congenital heart
defects, ichthyosiform dermatosis, intellectual disability, ear anomalies, and
seizures. It does not represent GMPPA, GDP-mannose pyrophosphorylase biology,
AAMR, achalasia, alacrima, postural hypotension, or normal transferrin
glycosylation.

The local knowledge base has broader glycosylation and alacrima context in
other entries, but no exact GMPPA/AAMR target was identified.

## Concordance and completeness

Judgement: true local gap; reject CHIME syndrome as exact coverage.

The generated candidate shares neurodevelopmental, hearing, and facial
phenotype language, but gene, pathway, cardinal clinical triad, and biochemical
pattern differ. IEMbase should be curated as GMPPA/AAMR rather than a GPI-anchor
or CHIME-spectrum disorder.

## Curation actions

- Create or identify an exact GMPPA-CDG / AAMR target before import.
- Reject `CHIME_syndrome.yaml` as an exact mapping.
- Preserve normal sialotransferrins, achalasia, alacrima, dysphagia,
  regurgitation, postural hypotension, hearing impairment, gait disturbance,
  facial dysmorphism, growth retardation, hypotonia, and intellectual-disability
  prompts.
