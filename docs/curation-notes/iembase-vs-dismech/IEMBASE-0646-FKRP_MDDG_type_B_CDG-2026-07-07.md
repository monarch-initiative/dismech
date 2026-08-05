# IEMbase 0646: FKRP-related muscular dystrophy-dystroglycanopathy type B

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 646 |
| Nosology | 18.2.09.03 |
| Gene | FKRP |
| External IDs | OMIM:606612; ORPHA:34515 |
| Generated mapping | UNMAPPED; weak candidate `Dystroglycanopathy.yaml` |
| Candidate DisMech targets | `Dystroglycanopathy.yaml` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents FKRP-CDG type B as autosomal recessive congenital muscular
dystrophy-dystroglycanopathy with or without intellectual disability.

Biochemical rows include markedly increased plasma creatine kinase and normal
serum sialotransferrins across ages. Clinical rows include muscular dystrophy
and hypotonia as characteristic features, with optional cerebellar
abnormalities, cerebellar white-matter MRI abnormalities, feeding difficulties,
intellectual disability, microcephaly, nodular heterotopia, pachygyria, and
spinal abnormalities.

## DisMech phenotype coverage

`Dystroglycanopathy.yaml` includes the FKRP gene subtype and the type B severity
subtype. It covers the shared matriglycan defect, muscular dystrophy, elevated
CK, hypotonia, variable intellectual disability, and the principle that
structural brain abnormalities may occur in type B but are less severe than in
type A.

The local entry does not spell out the FKRP type B phenotype bundle: nodular
heterotopia, cerebellar white-matter abnormalities, feeding difficulties,
microcephaly, and spinal abnormalities are not captured as FKRP B5-specific
phenotype prompts.

## Concordance and completeness

Judgement: broad local coverage with row-level incompleteness.

DisMech covers FKRP and type B dystroglycanopathy, so this is not a true
absence of local coverage. The missing piece is an exact FKRP type B /
congenital-with-or-without-ID subtype that preserves the milder brain and
feeding/spinal phenotype spectrum.

## Curation actions

- Map broadly to `Dystroglycanopathy.yaml`.
- Consider adding FKRP type B / MDDG B5 detail under the FKRP subtype if exact
  IEMbase row coverage is prioritized.
- Preserve CK, normal sialotransferrins, hypotonia, muscular dystrophy,
  variable ID, cerebellar/white-matter, nodular heterotopia, pachygyria,
  feeding, microcephaly, and spinal prompts.
