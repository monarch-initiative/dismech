# IEMbase 0648: VPS33A-related mucopolysaccharidosis-plus syndrome

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 648 |
| Nosology | 19.4.12.02 |
| Gene | VPS33A |
| External IDs | OMIM:617303; ORPHA:505248 |
| Generated mapping | UNMAPPED; weak candidate `Hurler_syndrome.yaml` |
| Candidate DisMech targets | False exact candidate; possible MPS grouping context |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents VPS33A-related mucopolysaccharidosis-plus syndrome as an
autosomal recessive complex-molecule degradation disorder.

Biochemical rows show markedly increased heparan sulfate in plasma and urine,
increased total urinary GAGs, increased urinary dermatan sulfate, and increased
urinary oligosaccharides including N-acetylneuraminic acid. Clinical rows
combine an MPS-like storage phenotype with severe extra features: coarse facial
features, hepatosplenomegaly, dysostosis multiplex, macroglossia, hirsutism,
short stature, joint contractures, anemia, thrombocytopenia, bone marrow
hypoplasia, foam cells, lymphocyte granulation, proteinuria, hypertrophic
cardiomyopathy, congenital heart defects, heart failure, recurrent respiratory
infections, respiratory dysfunction, developmental delay, pyramidal signs, and
optic atrophy.

## DisMech phenotype coverage

`Hurler_syndrome.yaml` is not an exact target. It correctly overlaps on MPS-like
features such as heparan/dermatan sulfate storage, coarse facies, dysostosis
multiplex, hepatosplenomegaly, cardiac disease, respiratory disease, and
neurodevelopmental involvement. However, Hurler syndrome is IDUA deficiency
within MPS I, whereas the IEMbase row is VPS33A-related MPS-plus syndrome.

The `Mucopolysaccharidoses` grouping currently defines membership around
deficiency of a GAG-degrading lysosomal enzyme and lists classic enzyme MPS
members. VPS33A MPS-plus is not represented there and may not fit that
membership definition cleanly because its primary gene is a vesicle-trafficking
/ lysosomal pathway component rather than a canonical GAG-degrading enzyme.

## Concordance and completeness

Judgement: true local VPS33A MPS-plus gap; reject Hurler as exact.

The weak Hurler candidate is useful as phenotype context but would conflate the
gene, enzyme defect, and mechanism. The IEMbase phenotype signal also includes
hematologic/bone-marrow, renal proteinuria, severe infection/respiratory, and
cardiac-plus features that are central to MPS-plus and not well modeled by a
classic MPS I entry.

## Curation actions

- Do not map to `Hurler_syndrome.yaml` as exact coverage.
- Curate VPS33A-related mucopolysaccharidosis-plus syndrome separately if
  selected.
- Revisit whether the MPS grouping should include or explicitly exclude
  MPS-plus disorders under a separate rationale.
- Preserve heparan/dermatan/total GAG, oligosaccharide, coarse facies,
  hepatosplenomegaly, dysostosis, hematologic, proteinuria, cardiac,
  respiratory/infection, developmental, pyramidal, and optic-atrophy prompts.
