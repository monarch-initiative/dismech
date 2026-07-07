# IEMbase 0572: UCP2-related hyperinsulinism

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 572 |
| Nosology | 24.1.08.02 |
| Gene | UCP2 |
| External IDs | OMIM:601693; ORPHA:276556 |
| Generated mapping | UNMAPPED; best candidate `Pyruvate_Dehydrogenase_Deficiency.yaml` |
| Candidate DisMech targets | `Congenital_Isolated_Hyperinsulinism.yaml` as broad context only |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents UCP2-related uncoupling protein 2 deficiency, abbreviated
UCP2-HI. The record is autosomal dominant, idiopathic subtype, of unknown
treatability, and has no treatment rows.

Biochemical rows include decreased free fatty acids during hypoglycemia,
decreased ketones during hypoglycemia, low plasma glucose, and normal-to-high
insulin during hypoglycemia. Characteristic rows include hyperinsulinism and
hypoketotic hypoglycemia.

## DisMech phenotype coverage

`Congenital_Isolated_Hyperinsulinism.yaml` includes broad CHI mechanisms and an
evidence snippet naming UCP2 among known CHI genes, but it does not appear to
model a UCP2-HI subtype or UCP2-specific mitochondrial uncoupling/beta-cell
metabolic mechanism. The generated `Pyruvate_Dehydrogenase_Deficiency.yaml`
candidate is a false positive and does not match the UCP2-HI disease scope.

## Concordance and completeness

Judgement: broad CHI context only; exact UCP2-related hyperinsulinism coverage
remains a local gap.

IEMbase overlaps with the local CHI entry on hyperinsulinism, hypoketotic
hypoglycemia, low plasma glucose, suppressed free fatty acids, and suppressed
ketones. The gene-specific UCP2 mechanism and subtype are missing.

## Curation actions

- Reject `Pyruvate_Dehydrogenase_Deficiency.yaml` as an exact mapping.
- Add UCP2-HI to the congenital hyperinsulinism backlog.
- Preserve IEMbase free-fatty-acid, ketone, glucose, insulin, and UCP2-HI alias
  prompts for future source review.
