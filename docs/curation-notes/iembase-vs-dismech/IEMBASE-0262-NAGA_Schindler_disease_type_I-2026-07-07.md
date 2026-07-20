# IEMbase 0262: Alpha-N-acetylgalactosaminidase deficiency, Schindler disease type I

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 262 |
| Nosology | 20.3.05.01 |
| Gene | NAGA |
| External IDs | OMIM:609241; ORPHA:79281 |
| Generated mapping | MAPPED; `NAGA_Deficiency_Type_3.yaml` |
| Candidate DisMech targets | `Schindler_Disease.yaml`; `NAGA_Deficiency_Type_3.yaml` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents this as alpha-N-acetylgalactosaminidase deficiency with
alternate labels Schindler disease type I and NAGA. The record is autosomal
recessive and treatability is marked unknown, with no treatment rows in the
cached JSON.

Biochemical rows include decreased alpha-N-acetylgalactosaminidase activity in
fibroblasts and white blood cells, plus increased urinary
N-acetylgalactosaminyl-oligosaccharides. Clinical rows include ataxia,
neuroaxonal dystrophy, and exaggerated startle response.

## DisMech phenotype coverage

`Schindler_Disease.yaml` is the correct local target. The local entry defines
Schindler disease as alpha-N-acetylgalactosaminidase deficiency type 1, the
severe infantile neuroaxonal-dystrophy form of NAGA deficiency. It covers
biallelic NAGA variants, loss of lysosomal alpha-N-acetylgalactosaminidase,
glycopeptide/glycoconjugate accumulation, urinary glycopeptide excretion,
developmental regression, hypotonia, spasticity, areflexia, blindness, hearing
impairment, CNS axonal spheroids, and supportive care.

`NAGA_Deficiency_Type_3.yaml` is not the right canonical target for this
IEMbase record because it represents Schindler disease type III, the
intermediate phenotype.

## Concordance and completeness

Judgement: generated mapping is a false positive to type 3; resolve to
`Schindler_Disease.yaml`.

IEMbase and the local Schindler disease entry agree on NAGA/type I identity,
alpha-N-acetylgalactosaminidase deficiency, urinary oligosaccharide or
glycopeptide storage signal, autosomal recessive inheritance, and neuroaxonal
dystrophy. IEMbase adds ataxia and exaggerated startle response as compact
phenotype prompts. The generated type 3 target shares the enzyme defect but is
the wrong severity/type entity.

## Curation actions

- Remap this record to `Schindler_Disease.yaml`.
- Do not use `NAGA_Deficiency_Type_3.yaml` as the canonical target for Schindler
  disease type I.
- Use IEMbase's ataxia and exaggerated-startle rows as phenotype review prompts
  for the Schindler type I entry.
