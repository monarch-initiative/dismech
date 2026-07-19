# IEMbase 0468: UCP1-3-related uncoupling protein deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 468 |
| Nosology | 24.1.08.01 |
| Gene | UCP1; UCP2; UCP3 |
| External IDs | OMIM:601665; OMIM:607447 |
| Generated mapping | UNMAPPED; low candidate `Pyruvate_Dehydrogenase_Deficiency.yaml#E3-binding protein deficiency` |
| Candidate DisMech targets | No exact local target |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents UCP1-3-related uncoupling protein deficiency, abbreviated
UCPD. The source records autosomal recessive inheritance. The biochemical row is
increased plasma glucose, and characteristic clinical rows are type 2 diabetes
mellitus and susceptibility to obesity. There are no treatment rows.

## DisMech phenotype coverage

There is no exact local DisMech target for UCP1/UCP2/UCP3 uncoupling protein
deficiency. A local UCP2 mention occurs in congenital isolated hyperinsulinism
as one gene in a hyperinsulinism spectrum, which is not the same entity and has
opposite glucose physiology.

The generated `Pyruvate_Dehydrogenase_Deficiency.yaml` E3-binding protein
candidate is a false positive. Local PDH deficiency is a pyruvate
dehydrogenase-complex disorder with lactic acidosis and neurometabolic disease;
it does not model uncoupling-protein biology, obesity susceptibility, or type 2
diabetes risk.

## Concordance and completeness

Judgement: true local gap or scope-review item for UCP1-3 uncoupling-protein
deficiency; reject the PDH E3-binding protein candidate.

The IEMbase record looks more like a susceptibility/metabolic-risk phenotype
than the discrete Mendelian mitochondrial enzyme defects in nearby batches. If
DisMech curates it, the entry should make the disease/susceptibility boundary
explicit rather than mapping it to a mechanistically unrelated mitochondrial
energy-metabolism disorder.

## Curation actions

- Keep this record unmapped until an explicit UCP1/UCP2/UCP3 uncoupling-protein
  deficiency or susceptibility target exists.
- Do not map to `Pyruvate_Dehydrogenase_Deficiency.yaml`.
- Do not substitute UCP2 hyperinsulinism context for this hyperglycemia/obesity
  susceptibility record.
- If curated, include UCP1/UCP2/UCP3, source-stated autosomal recessive
  inheritance with verification, uncoupling-protein/mitochondrial energy
  expenditure biology, increased plasma glucose, type 2 diabetes mellitus, and
  obesity susceptibility.
