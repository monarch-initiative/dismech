# IEMbase 0544: MCEE-related methylmalonic aciduria 3

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 544 |
| Nosology | 1.2.2.01 |
| Gene | MCEE |
| External IDs | OMIM:251120; ORPHA:308425 |
| Generated mapping | CANDIDATE; `Methylmalonic_Acidemia.yaml` |
| Candidate DisMech targets | Broad `Methylmalonic_Acidemia.yaml` context only |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents MCEE-related methylmalonic aciduria due to
methylmalonyl-CoA epimerase deficiency, with alternate labels methylmalonic
aciduria 3 and MMAE. The record is autosomal recessive, marked as a benign
form, and treatability is unknown. The treatment row lists protein restriction
during stress.

The phenotype signal is deliberately sparse: increased urinary methylmalonic
acid is the characteristic biochemical row, and the only clinical row states no
clinical significance across age periods.

## DisMech phenotype coverage

`Methylmalonic_Acidemia.yaml` provides useful broad context for methylmalonic
acid accumulation and propionate-pathway disease, but it does not currently
model MCEE, methylmalonyl-CoA epimerase deficiency, or the benign MMAE subtype.
The local entry focuses on MMUT and adenosylcobalamin-handling defects such as
MMAA and MMAB, with recurrent metabolic decompensation, kidney disease,
neurologic injury, cardiomyopathy, C3 propionylcarnitine, methylcitric acid,
and crisis-management logic.

That coverage is much more severe and mechanistically different from the
IEMbase MCEE record.

## Concordance and completeness

Judgement: partial broad context only; do not treat the generated candidate as
an exact MCEE mapping.

IEMbase and DisMech overlap on methylmalonic acid elevation, but IEMbase is a
gene-specific, benign epimerase-deficiency record. The current local MMA entry
does not include the MCEE mechanism or the low-clinical-significance scope.

## Curation actions

- Do not collapse this record into the existing MMA entry as an exact match.
- If MCEE is in scope, add a methylmalonic aciduria 3 / MMAE subtype or a small
  standalone MCEE target under methylmalonic acidemia context.
- Preserve urinary methylmalonic acid, benign/no-clinical-significance wording,
  autosomal recessive inheritance, and stress protein-restriction as prompts.
