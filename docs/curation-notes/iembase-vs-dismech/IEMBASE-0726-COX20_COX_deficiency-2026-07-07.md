# IEMbase 0726: COX20-related cytochrome c oxidase assembly factor 20 deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 726 |
| Nosology | 7.4.04.01 |
| Nosology code | IEM0472 |
| Gene | COX20 |
| External IDs | OMIM:220110; ORPHA:254905 |
| Generated mapping | UNMAPPED; weak candidate `COX20-Related_COX_Deficiency.yaml` |
| Candidate DisMech targets | `COX20-Related_COX_Deficiency.yaml` is exact local coverage |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents autosomal recessive COX20-related cytochrome c oxidase
assembly factor 20 deficiency. The cached phenotype rows show normal-to-high
plasma lactate from infancy through adulthood, cerebellar ataxia that becomes
strongest in adolescence and adulthood, possible dystonia from childhood onward,
and possible infantile or childhood hypotonia.

## DisMech phenotype coverage

DisMech has exact local coverage in `COX20-Related_COX_Deficiency.yaml`. The
entry resolves to mitochondrial complex IV deficiency nuclear type 11
(MONDO:0033645) and describes biallelic COX20/FAM36A loss as defective COX2
maturation: COX20 normally stabilizes newly synthesized COX2 and presents it to
the SCO1/SCO2 copper-metallochaperone module.

Local phenotype coverage is strong for hypotonia, progressive cerebellar
ataxia, dystonia, dysarthria, areflexia, and sensory axonal neuropathy.

## Concordance and completeness

Judgement: false negative from the generated mapper. The correct target is
`COX20-Related_COX_Deficiency.yaml`.

The IEMbase record and local file align on COX20, autosomal recessive complex IV
assembly disease, and the ataxia/hypotonia/dystonia phenotype. IEMbase adds
age-banded lactate detail, while DisMech is richer for COX2 maturation,
dysarthria, areflexia, and sensory axonal neuropathy.

## Curation actions

- Resolve IEMbase 726 to `COX20-Related_COX_Deficiency.yaml`.
- Treat the generated UNMAPPED status as stale or overly strict.
- Preserve normal-to-high lactate, progressive cerebellar ataxia, dystonia, and
  hypotonia.
- Keep local mechanistic detail on COX2 maturation and SCO1/SCO2 handoff.
