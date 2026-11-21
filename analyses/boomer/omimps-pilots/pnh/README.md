# Paroxysmal nocturnal hemoglobinuria (OMIMPS:300818)

## Source entities and member coverage

Candidates below are grounded entries or subtypes whose MONDO term has an explicit
exact match to the numbered OMIM record. This is a mapping-based coverage audit,
not independent evidence of clinical equivalence. A family entry alone is not
counted as individual member coverage. Directional mappings in the selected records
are also shown with their predicates; these are not exact member coverage.

| OMIM member | Source label | MONDO exact matches | Before candidates | After candidates |
|---|---|---|---|---|
| OMIM:300818 | paroxysmal nocturnal hemoglobinuria 1 | MONDO:0010438 | Paroxysmal Nocturnal Hemoglobinuria — skos:narrowMatch to MONDO:0010438 | PIGA-associated PNH1 (`kb/disorders/Paroxysmal_Nocturnal_Hemoglobinuria.yaml`); Paroxysmal Nocturnal Hemoglobinuria — skos:narrowMatch to MONDO:0010438 |
| OMIM:615399 | paroxysmal nocturnal hemoglobinuria 2 | MONDO:0014166 | Paroxysmal Nocturnal Hemoglobinuria — skos:narrowMatch to MONDO:0014166 | PIGT-associated PNH2 (`kb/disorders/Paroxysmal_Nocturnal_Hemoglobinuria.yaml`); Paroxysmal Nocturnal Hemoglobinuria 2 (`kb/disorders/Paroxysmal_Nocturnal_Hemoglobinuria_2.yaml`); Paroxysmal Nocturnal Hemoglobinuria — skos:narrowMatch to MONDO:0014166 |

## Joint solver comparison

| Snapshot | Curation commit | Hypotheses | Search status | Search confidence | Distinct satisfying assignments found | Enumeration | MAP certificate |
|---|---|---:|---|---:|---:|---|---|
| [before](before/solution.md) | `bef670f17076625c96e5e8955a0a83d2d5108257` | 6 | ALL_MAPPINGS_CONSISTENT | 0.9 | 40 | VERIFIED | [CERTIFIED](before/certificate.json) |
| [after](after/solution.md) | `e98ca0e393a21f8d9c6228da25edc73a5bfdd197` | 9 | ALL_MAPPINGS_CONSISTENT | 0.9 | 129 | VERIFIED | [CERTIFIED](after/certificate.json) |

Confidence compares the best two distinct complete assignments. It is not a
mapping marginal or proof of biological equivalence. Timeout values are provisional.
A separate MAP certificate proves the optimal all-true assignment and a distinct
runner-up when its sufficient conditions hold; it does not compute marginals or
whole-assignment posteriors. Both complete assignments are recorded in that file.

### Exhaustive enumeration (complete probabilities)

| Snapshot | Status | Distinct satisfying assignments | Confidence | Best whole-assignment posterior | Rejected mappings in optimal assignments |
|---|---|---:|---:|---:|---|
| [before](before/enumeration.json) | VERIFIED | 40 | 0.9 | 0.76339034667 | None |
| [after](after/enumeration.json) | VERIFIED | 129 | 0.9 | 0.72033393157 | None |

The complete source assertions, aliases, logical edges and mapping provenance are in
[before/audit.json](before/audit.json) and [after/audit.json](after/audit.json).
Frozen selected curation fields, source blob hashes, source labels and hierarchy are in
[projection.json](projection.json). The parent directory documents assumptions and limitations.
