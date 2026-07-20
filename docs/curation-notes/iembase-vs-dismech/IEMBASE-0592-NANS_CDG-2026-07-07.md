# IEMbase 0592: NANS-related N-acetylneuraminic acid synthase deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 592 |
| Nosology | 18.4.03.02 |
| Gene | NANS |
| External IDs | OMIM:610442; ORPHA:168454 |
| Generated mapping | UNMAPPED; best candidate `Spondyloepimetaphyseal_Dysplasia_Bieganski_Type.yaml` |
| Candidate DisMech targets | None exact |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents NANS-related N-acetylneuraminic acid synthase deficiency
(CDG), with alternate labels NANS-CDG and spondyloepimetaphyseal dysplasia,
Camera-Genevieve type. The record is autosomal recessive, classified under
disorders of multiple glycosylation pathways, has unknown treatability, and has
no treatment rows.

Biochemical rows include increased plasma and urinary N-acetyl-D-mannosamine.
Clinical rows include developmental delay, seizures, microcephaly, short
stature, facial dysmorphism, brachycephaly, broad nose, coarse face, flat ears,
full lips, prominent forehead, sunken nasal bridge, synophrys, premature carpal
ossification, small epiphyses, longitudinal metaphyseal striations, and skeletal
dysplasia.

## DisMech phenotype coverage

`Spondyloepimetaphyseal_Dysplasia_Bieganski_Type.yaml` is a false-positive
generated candidate. It models X-linked AIFM1-associated mitochondrial
spondyloepimetaphyseal dysplasia with neurodegeneration and hypomyelination.
It does not represent NANS, sialic-acid biosynthesis, N-acetylneuraminic acid
synthase deficiency, autosomal recessive inheritance, or N-acetyl-D-mannosamine
accumulation.

The local glycosylation entries provide broad CDG context, but no exact
NANS-CDG / Camera-Genevieve target was identified.

## Concordance and completeness

Judgement: true local gap; reject the Bieganski-type SEMD candidate.

The candidate shares skeletal-dysplasia language, but gene, inheritance,
pathway, biomarker, and disease identity diverge. IEMbase should be curated as a
NANS/sialic-acid biosynthesis CDG, not as AIFM1 mitochondrial skeletal-neurologic
disease.

## Curation actions

- Create or identify an exact NANS-CDG / Camera-Genevieve syndrome target
  before import.
- Reject `Spondyloepimetaphyseal_Dysplasia_Bieganski_Type.yaml` as an exact
  mapping.
- Preserve N-acetyl-D-mannosamine, skeletal maturation, metaphyseal/epiphyseal,
  facial, seizure, growth, and neurodevelopmental prompts.
