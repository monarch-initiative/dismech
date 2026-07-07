# IEMbase 0676: FDPS-related farnesylpyrophosphate synthetase deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 676 |
| Nosology | 14.7.05.01 |
| Nosology code | IEM0744 |
| Gene | FDPS |
| External IDs | OMIM:616631; ORPHA:79152 |
| Generated mapping | UNMAPPED; best candidate `Carbamoyl_Phosphate_Synthetase_I_Deficiency.yaml` |
| Candidate DisMech targets | Broad sterol/isoprenoid-pathway context only; no exact FDPS/POROK9 target |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents autosomal dominant FDPS-related farnesylpyrophosphate
synthetase deficiency, labeled porokeratosis type 9.

The cached phenotype signal includes characteristic actinic porokeratosis and
keratotic skin lesions in adolescence and adulthood. No biochemical rows are
present in the cached disease record.

## DisMech phenotype coverage

No exact FDPS, farnesylpyrophosphate synthetase deficiency, or porokeratosis type
9 local target was identified.

`Carbamoyl_Phosphate_Synthetase_I_Deficiency.yaml` is a lexical false positive
and should not be used. It is a urea-cycle disorder and does not share the
dominant mevalonate/isoprenoid dermatologic phenotype. `Mevalonate_Kinase_Deficiency.yaml`
is only broad pathway context and represents a different recessive systemic
autoinflammatory disease.

## Concordance and completeness

Judgement: true local gap.

The row is best interpreted as a dominant porokeratosis/keratinization disorder
from a downstream mevalonate-pathway gene, not as urea-cycle disease and not as
classic MVK-related mevalonate kinase deficiency.

## Curation actions

- Add a dedicated FDPS/POROK9 target if this disease is curated.
- Reject CPS1 deficiency as exact coverage.
- Preserve actinic porokeratosis and keratotic skin lesions as the phenotype
  signal.
- Keep this grouped with the PMVK and MVD porokeratosis records if a sterol-pathway
  porokeratosis curation sweep is planned.
