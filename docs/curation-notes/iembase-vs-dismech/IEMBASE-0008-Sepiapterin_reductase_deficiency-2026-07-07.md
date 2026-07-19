# IEMbase 0008: SPR-related sepiapterin reductase deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 8 |
| Nosology | 21.1.08.01 |
| Gene | SPR |
| External IDs | OMIM:182125 |
| Generated mapping | AMBIGUOUS by `alias_exact:sepiapterin reductase deficiency` |
| Candidate DisMech targets | `Disorder_of_Catecholamine_Synthesis.yaml#Sepiapterin reductase deficiency`; `Tetrahydrobiopterin_Deficiency.yaml#SPR Deficiency` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

Characteristic clinical features are cerebral palsy-like presentation, diurnal
fluctuation, hypokinesia, and psychomotor delay. Additional features include
axial hypotonia, psychotic behavior, dysarthria, abnormal eye movements,
gastrointestinal dysmotility, language difficulty, muscle weakness, oculogyric
crisis, parkinsonism, increased tendon reflexes, and tremor.

The biochemical pattern is monoamine/BH4-related but differs from the
hyperphenylalaninemic BH4 disorders: phenylalanine is listed, CSF 5-HIAA and HVA
are low, phenylalanine loading is relevant, pterins include biopterin, BH2,
neopterin, and sepiapterin, and prolactin is increased.

Treatments are levodopa/carbidopa, 5-hydroxytryptophan, and folinic acid.

## DisMech phenotype coverage

Both local targets are meaningful. `Tetrahydrobiopterin Deficiency` has an `SPR
Deficiency` subtype and explicitly notes that hyperphenylalaninemia is typically
absent because peripheral BH4 regeneration can preserve phenylalanine handling.
It also covers dystonia, parkinsonism, oculogyric crisis, seizures,
hyperprolactinemia, pterin profiles, CSF neurotransmitter metabolites, and the
major treatments.

`Disorder of Catecholamine Synthesis` has a sepiapterin reductase deficiency
subtype and more directly captures the monoamine/catecholamine synthesis
context, including movement disorder, developmental delay, hypotonia,
oculogyric crisis, parkinsonism, dystonia, autonomic dysfunction, low HVA, low
5-HIAA, and carbidopa-levodopa therapy.

## Concordance and completeness

Judgement: ambiguous mapping is biologically understandable rather than a simple
error. For IEMbase crosswalk purposes, one canonical target should be selected
to avoid double counting.

The strongest canonical target depends on the crosswalk policy. If classification
follows the BH4 pathway, use `Tetrahydrobiopterin_Deficiency#SPR Deficiency`. If
phenotype/mechanism follows monoamine deficiency, use
`Disorder_of_Catecholamine_Synthesis#Sepiapterin reductase deficiency`.

DisMech is missing several IEMbase-specific clinical details: cerebral
palsy-like presentation, psychotic behavior, dysarthria, GI dysmotility,
language difficulty, muscle weakness, increased tendon reflexes, tremor, and
sepiapterin-specific pterin findings.

## Curation actions

- Decide the canonical crosswalk target for SPR deficiency and record the other
  as secondary context.
- Consider explicit sepiapterin/pterin biochemical markers and diurnal
  fluctuation as subtype-level data.
- Review whether cerebral palsy-like presentation should be represented as a
  historical/misdiagnosis note rather than a core phenotype.
