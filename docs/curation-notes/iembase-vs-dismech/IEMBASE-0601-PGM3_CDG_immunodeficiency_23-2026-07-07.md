# IEMbase 0601: PGM3-related phosphoglucomutase 3 deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 601 |
| Nosology | 18.4.06.01 |
| Gene | PGM3 |
| External IDs | OMIM:615816; OMIM:172100; ORPHA:443811 |
| Generated mapping | CANDIDATE; `IKBKG_Ectodermal_Dysplasia_with_Immunodeficiency.yaml#IMD33` |
| Candidate DisMech targets | None exact |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents PGM3-related phosphoglucomutase 3 deficiency, labelled
PGM3-CDG and immunodeficiency-23. The record is autosomal recessive, classified
under disorders of multiple glycosylation pathways, has unknown treatability,
and has no treatment rows.

Biochemical rows include increased serum N-glycans and O-glycans, normal serum
sialotransferrins, normal-to-increased IgE, and decreased CD19-positive B-cell
counts. Clinical rows include T-cell immunodeficiency, recurrent infections,
neutropenia, atopy, intellectual disability, short stature, skeletal dysplasia,
brachydactyly, facial dysmorphism, midface hypoplasia, micrognathia, downturned
mouth corners, and short neck.

## DisMech phenotype coverage

`IKBKG_Ectodermal_Dysplasia_with_Immunodeficiency.yaml#IMD33` is a
false-positive generated candidate. It models X-linked IKBKG/NEMO-related
mycobacterial susceptibility and NF-kB signaling impairment, not PGM3,
hexosamine/N-glycosylation biology, autosomal recessive inheritance, or the
PGM3-CDG skeletal-dysmorphic immune phenotype.

`Autosomal_Dominant_Hyper-IgE_Syndrome.yaml` mentions PGM3 only as a gene-panel
differential for STAT3-HIES. That is useful diagnostic context but not disease
coverage. No exact PGM3-CDG / immunodeficiency-23 target was identified.

## Concordance and completeness

Judgement: true local gap; reject IMD33 as exact coverage.

The generated candidate shares immunodeficiency wording, but the causal gene,
inheritance, pathway, immune phenotype, and syndromic features are different.
IEMbase 0601 should not be collapsed into IKBKG/NEMO deficiency or STAT3-HIES
context.

## Curation actions

- Create or identify an exact PGM3-CDG / immunodeficiency-23 target before
  import.
- Reject `IKBKG_Ectodermal_Dysplasia_with_Immunodeficiency.yaml#IMD33` as an
  exact mapping.
- Preserve N- and O-glycan abnormalities with normal sialotransferrins, CD19
  B-cell decrease, IgE range, T-cell immunodeficiency, neutropenia, infection,
  atopy, skeletal dysplasia, brachydactyly, facial, growth, and
  neurodevelopmental prompts.
