# IEMbase 0339: GNE-related UDP-GlcNAc epimerase-kinase deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 339 |
| Nosology | 18.4.01.05 |
| Gene | GNE |
| External IDs | OMIM:600737; OMIM:605820; ORPHA:602 |
| Generated mapping | UNMAPPED; low-score candidate `Galactosemia.yaml` |
| Candidate DisMech targets | Reject `Galactosemia.yaml`; no GNE myopathy/CDG target |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents GNE-CDG, also labeled hereditary inclusion body myopathy 2
or distal myopathy with rimmed vacuoles. Characteristic rows include foot drop,
progressive muscular dystrophy, rimmed vacuoles on muscle histopathology,
muscle wasting, and respiratory dysfunction. Additional clinical rows include
cardiomyopathy, cholangiocarcinoma, and tubulofilaments on muscle
histopathology.

The biochemical rows include increased creatine kinase and serum
sialotransferrins. IEMbase records N-acetylmannosamine as a pharmacologic
treatment row with a phase 2/open-label evidence citation and an increased
Neu5Ac readout.

## DisMech phenotype coverage

The generated Galactosemia candidate is a lexical false positive around
"epimerase." DisMech Galactosemia models GALT, GALK1, and GALE defects in the
Leloir pathway, with galactose-restricted diet and galactose-1-phosphate or
galactitol biomarkers. It does not model GNE, sialic acid biosynthesis,
rimmed-vacuole distal myopathy, or N-acetylmannosamine therapy.

Other local myopathy files include rimmed-vacuole pathology in different
genetic contexts, but no GNE-specific target was found.

## Concordance and completeness

Judgement: true local disease gap; reject the Galactosemia candidate.

The IEMbase record points to GNE-related myopathy/sialic-acid biosynthesis
disease. Shared "epimerase" wording is not sufficient to map it to GALE or the
galactose metabolism umbrella.

## Curation actions

- Add a standalone GNE myopathy/GNE-CDG target before treating this record as
  mapped.
- Do not map to Galactosemia or unrelated rimmed-vacuole myopathy entries.
- Preserve distal weakness/foot drop, rimmed vacuoles, tubulofilaments,
  respiratory dysfunction, cardiomyopathy, cholangiocarcinoma, CK,
  sialotransferrins, and N-acetylmannosamine as future-curation prompts.
