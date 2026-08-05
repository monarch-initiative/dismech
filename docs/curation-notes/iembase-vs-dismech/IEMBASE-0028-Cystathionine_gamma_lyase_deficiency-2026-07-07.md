# IEMbase 0028: CTH-related cystathionine gamma-lyase deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 28 |
| Nosology | 1.5.07.01 |
| Gene | CTH |
| External IDs | OMIM:219500 |
| Generated mapping | UNMAPPED; best fuzzy candidate `Homocystinuria.yaml` |
| Candidate DisMech targets | none currently valid |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents cystathionine gamma-lyase deficiency/cystathioninuria as a
biochemical condition with no clinical significance. The only characteristic
clinical row is `No clinical significance` across all age bands.

The biochemical signal is high plasma cystathionine, very high plasma/urinary
cystathionine, low methionine-to-cystathionine ratio, normal cysteine, and
normal-to-mildly high total homocysteine. No treatments are listed and
treatability is unknown.

## DisMech phenotype coverage

There is no current DisMech entry for CTH deficiency or cystathioninuria. The
best fuzzy candidate, `Homocystinuria.yaml`, should be rejected. CBS-deficient
homocystinuria has low cystathionine, marked hyperhomocystinemia, elevated or
variable methionine, and a severe ocular/skeletal/vascular phenotype. CTH
deficiency has the opposite cystathionine signal and is represented by IEMbase
as clinically insignificant.

## Concordance and completeness

Judgement: generated status is correctly unmapped. The fuzzy homocystinuria
candidate is mechanistically misleading despite pathway proximity.

There is no local DisMech coverage to compare for phenotype completeness. If a
future entry is created, it should be framed as a mostly biochemical
cystathioninuria record unless stronger clinical evidence is added.

## Curation actions

- Do not map this record to `Homocystinuria.yaml`.
- If curated, preserve the low-clinical-significance judgement and avoid
  importing CBS-deficiency complications.
- The key differentiator is high cystathionine in CTH deficiency versus low
  cystathionine in CBS deficiency.
