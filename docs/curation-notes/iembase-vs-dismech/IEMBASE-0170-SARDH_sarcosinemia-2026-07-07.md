# IEMbase 0170: SARDH-related sarcosinemia

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 170 |
| Nosology | 2.3.02.01 |
| Gene | SARDH |
| External IDs | OMIM:268900; ORPHA:3129 |
| Generated mapping | UNMAPPED; best candidate `Isovaleric_Acidemia.yaml` |
| Candidate DisMech targets | None valid |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents this as SARDH-related sarcosine dehydrogenase deficiency,
with alternate labels sarcosinemia and SDD. Treatability is marked unknown.
The extracted local JSON is very sparse: sarcosine is increased in plasma and
urine across age bands, and there are no clinical or treatment rows in the
record.

## DisMech phenotype coverage

No valid local DisMech target was found. The generated best candidate,
`Isovaleric_Acidemia.yaml`, is a false positive. It models IVD-related leucine
catabolism with isovaleric acid, isovalerylcarnitine, isovalerylglycine,
hyperammonemic organic-acidemia crises, and leucine-directed management. That
mechanism and biomarker profile are distinct from SARDH-related sarcosine
accumulation.

Local search found sarcosine only as pathway context inside
`Dimethylglycine_Dehydrogenase_Deficiency.yaml`, not as a SARDH disease entry.

## Concordance and completeness

Judgement: true local gap.

IEMbase provides a biochemical-only SARDH/sarcosinemia record. DisMech does
not currently have a standalone SARDH-related sarcosinemia target, and the
isovaleric acidemia candidate should not be used as a pathway-neighbor
substitute.

## Curation actions

- Do not map this record to `Isovaleric_Acidemia.yaml`.
- Add a future standalone SARDH/sarcosinemia entry only if project scope keeps
  this sparse biochemical disorder.
- Expected minimum future coverage: SARDH, sarcosine dehydrogenase deficiency,
  increased plasma sarcosine, increased urinary sarcosine, and an explicit note
  on limited or absent clinical phenotype if supported by sources.
