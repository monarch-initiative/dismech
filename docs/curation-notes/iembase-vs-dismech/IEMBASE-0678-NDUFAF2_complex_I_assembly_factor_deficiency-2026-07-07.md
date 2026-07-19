# IEMbase 0678: NDUFAF2-related complex I assembly factor 2 deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 678 |
| Nosology | 7.1.02.01 |
| Nosology code | IEM0438 |
| Gene | NDUFAF2 |
| External IDs | OMIM:618233; ORPHA:255241 |
| Generated mapping | CANDIDATE to `COX14-Related_COX_Deficiency.yaml` |
| Candidate DisMech targets | Broad complex I/Leigh context only; no exact NDUFAF2 target |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents autosomal recessive NDUFAF2-related complex I assembly factor
2 deficiency, also labeled mitochondrial complex I deficiency, nuclear type 10.

Biochemical rows show decreased fibroblast complex I activity and increased
plasma lactate from neonatal through adolescent ages. Clinical rows include
hypotonia, renal tubular acidosis, possible respiratory insufficiency from
muscle weakness or diaphragm paralysis, and characteristic ataxia, basal
ganglia MRI abnormalities, encephalopathy, nystagmus, and optic atrophy.

## DisMech phenotype coverage

No exact NDUFAF2 or MC1DN10 target was identified.

`Leigh_Syndrome.yaml` covers broad complex I-linked Leigh biology and several
overlapping neurologic features, including basal-ganglia involvement, hypotonia,
movement disorder, ataxia, lactic acidosis, and seizures. That is syndrome
context, not a gene-specific NDUFAF2 disease model.

The generated `COX14-Related_COX_Deficiency.yaml` candidate is a wrong-complex
match. COX14 is a complex IV assembly factor and does not cover NDUFAF2-related
complex I assembly failure.

## Concordance and completeness

Judgement: true local gap.

The strongest preservation points are the complex I enzyme readout and the
NDUFAF2-specific phenotype prompts that are not guaranteed by generic Leigh
coverage: renal tubular acidosis, respiratory insufficiency/diaphragm weakness,
nystagmus, and optic atrophy.

## Curation actions

- Add a dedicated NDUFAF2/MC1DN10 target if curated.
- Reject COX14-related complex IV deficiency as exact coverage.
- Preserve decreased fibroblast complex I activity, lactate, renal tubular
  acidosis, respiratory insufficiency, basal-ganglia lesions, nystagmus, optic
  atrophy, ataxia, and encephalopathy.
- Use broad Leigh context only for shared mitochondrial neurologic features.
