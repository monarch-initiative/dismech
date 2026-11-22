# Maple syrup urine disease (OMIMPS:248600)

## Source entities and member coverage

Candidates below are grounded entries or subtypes whose MONDO term has an explicit
exact match to the numbered OMIM record. This is a mapping-based coverage audit,
not independent evidence of clinical equivalence. A family entry alone is not
counted as individual member coverage. Directional mappings in the selected records
are also shown with their predicates; these are not exact member coverage.

| OMIM member | Source label | MONDO exact matches | Before candidates | After candidates |
|---|---|---|---|---|
| OMIM:246900 | dihydrolipoamide dehydrogenase deficiency | MONDO:0009529 | E3 deficiency (`kb/disorders/Pyruvate_Dehydrogenase_Deficiency.yaml`) | E3 deficiency (`kb/disorders/Pyruvate_Dehydrogenase_Deficiency.yaml`) |
| OMIM:248600 | maple syrup urine disease, type 1a | MONDO:0023691 | Type IA (`kb/disorders/Maple_Syrup_Urine_Disease.yaml`) | Type IA (`kb/disorders/Maple_Syrup_Urine_Disease.yaml`) |
| OMIM:615135 | maple syrup urine disease, mild variant | MONDO:0014057 | No grounded candidate | PPM1K-Related Mild Variant (`kb/disorders/Maple_Syrup_Urine_Disease.yaml`) |
| OMIM:620698 | maple syrup urine disease, type 1b | MONDO:0023692 | Type IB (`kb/disorders/Maple_Syrup_Urine_Disease.yaml`) | Type IB (`kb/disorders/Maple_Syrup_Urine_Disease.yaml`) |
| OMIM:620699 | maple syrup urine disease, type 2 | MONDO:0023693 | Type II (`kb/disorders/Maple_Syrup_Urine_Disease.yaml`) | Type II (`kb/disorders/Maple_Syrup_Urine_Disease.yaml`) |

## Joint solver comparison

| Snapshot | Curation commit | Hypotheses | Search status | Search confidence | Distinct satisfying assignments found | Enumeration | MAP certificate |
|---|---|---:|---|---:|---:|---|---|
| [before](before/solution.md) | `bef670f17076625c96e5e8955a0a83d2d5108257` | 8 | ALL_MAPPINGS_CONSISTENT | 0.9 | 256 | VERIFIED | [CERTIFIED](before/certificate.json) |
| [after](after/solution.md) | `12e38bd36f3eae59d4a7c42ab640ee1e9b81d5b5` | 10 | TIMED_OUT | 0.9 | 1024 | EXHAUSTIVELY_ENUMERATED | [CERTIFIED](after/certificate.json) |

Confidence compares the best two distinct complete assignments. It is not a
mapping marginal or proof of biological equivalence. Timeout values are provisional.
A separate MAP certificate proves the optimal all-true assignment and a distinct
runner-up when its sufficient conditions hold; it does not compute marginals or
whole-assignment posteriors. Both complete assignments are recorded in that file.

### Exhaustive enumeration (complete probabilities)

| Snapshot | Status | Distinct satisfying assignments | Confidence | Best whole-assignment posterior | Rejected mappings in optimal assignments |
|---|---|---:|---:|---:|---|
| [before](before/enumeration.json) | VERIFIED | 256 | 0.9 | 0.534397550625 | None |
| [after](after/enumeration.json) | EXHAUSTIVELY_ENUMERATED | 1024 | 0.9 | 0.456909905784 | None |

The complete source assertions, aliases, logical edges and mapping provenance are in
[before/audit.json](before/audit.json) and [after/audit.json](after/audit.json).
Frozen selected curation fields, source blob hashes, source labels and hierarchy are in
[projection.json](projection.json). The parent directory documents assumptions and limitations.
