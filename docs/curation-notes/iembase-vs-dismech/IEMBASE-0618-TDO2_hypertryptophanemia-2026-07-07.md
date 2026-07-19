# IEMbase 0618: TDO2-related hypertryptophanemia

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 618 |
| Nosology | 1.8.03.01 |
| Gene | TDO2 |
| External IDs | OMIM:600627; ORPHA:2224 |
| Generated mapping | UNMAPPED |
| Candidate DisMech targets | None exact; `Alkaptonuria.yaml` is a pathway-neighbor false candidate |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents TDO2-related hypertryptophanemia / tryptophan
2,3-dioxygenase deficiency as an autosomal recessive disorder with unknown
treatability and no treatment rows.

The cached record is biochemical-only: increased tryptophan in dried blood
spots during the neonatal/infancy period, increased plasma tryptophan from
infancy through adulthood, and increased serum serotonin from infancy through
adolescence. No clinical or characteristic symptom rows are present.

## DisMech phenotype coverage

No exact TDO2 target was identified locally. `Alkaptonuria.yaml` is a false
candidate driven by aromatic-amino-acid metabolism neighborhood only; HGD
homogentisate metabolism is not TDO2 tryptophan catabolism.

## Concordance and completeness

Judgement: true local gap, with scope review needed.

Because IEMbase supplies only biochemical rows and no clinical manifestations,
curation should first decide whether this qualifies as a DisMech disease entry
or should be tracked as a biochemical trait / low-priority metabolic finding.

## Curation actions

- Do not map to `Alkaptonuria.yaml`.
- Source-review TDO2 hypertryptophanemia disease scope before creating a local
  disease entry.
- Preserve tryptophan and serotonin biomarker prompts if the entity is curated.
