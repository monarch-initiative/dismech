# Lysosomal acid lipase deficiency (OMIMPS:278000)

## Source entities and member coverage

Candidates below are grounded entries or subtypes whose MONDO term has an explicit
exact match to the numbered OMIM record. This is a mapping-based coverage audit,
not independent evidence of clinical equivalence. A family entry alone is not
counted as individual member coverage. Directional mappings in the selected records
are also shown with their predicates; these are not exact member coverage.

| OMIM member | Source label | MONDO exact matches | Before candidates | After candidates |
|---|---|---|---|---|
| OMIM:278000 | cholesteryl ester storage disease | MONDO:0019149 | Cholesteryl Ester Storage Disease (`kb/disorders/Cholesteryl_Ester_Storage_Disease.yaml`); Cholesteryl Ester Storage Disease — skos:exactMatch to MONDO:0019149 | Cholesteryl Ester Storage Disease (`kb/disorders/Cholesteryl_Ester_Storage_Disease.yaml`); Cholesteryl Ester Storage Disease — skos:exactMatch to MONDO:0019149 |
| OMIM:620151 | wolman disease | MONDO:0019148 | Wolman Disease (`kb/disorders/Wolman_Disease.yaml`) | Wolman Disease (`kb/disorders/Wolman_Disease.yaml`) |

## Joint solver comparison

| Snapshot | Curation commit | Hypotheses | Search status | Search confidence | Distinct satisfying assignments found | Enumeration | MAP certificate |
|---|---|---:|---|---:|---:|---|---|
| [before](before/solution.md) | `bef670f17076625c96e5e8955a0a83d2d5108257` | 5 | ALL_MAPPINGS_CONSISTENT | 0.9 | 32 | VERIFIED | [CERTIFIED](before/certificate.json) |
| [after](after/solution.md) | `790baff20fa863084cce942f1cc9f899b1936bdc` | 6 | ALL_MAPPINGS_CONSISTENT | 0.9 | 64 | VERIFIED | [CERTIFIED](after/certificate.json) |

Confidence compares the best two distinct complete assignments. It is not a
mapping marginal or proof of biological equivalence. Timeout values are provisional.
A separate MAP certificate proves the optimal all-true assignment and a distinct
runner-up when its sufficient conditions hold; it does not compute marginals or
whole-assignment posteriors. Both complete assignments are recorded in that file.

### Exhaustive enumeration (complete probabilities)

| Snapshot | Status | Distinct satisfying assignments | Confidence | Best whole-assignment posterior | Rejected mappings in optimal assignments |
|---|---|---:|---:|---:|---|
| [before](before/enumeration.json) | VERIFIED | 32 | 0.9 | 0.69447375 | None |
| [after](after/enumeration.json) | VERIFIED | 64 | 0.9 | 0.6597500625 | None |

The complete source assertions, aliases, logical edges and mapping provenance are in
[before/audit.json](before/audit.json) and [after/audit.json](after/audit.json).
Frozen selected curation fields, source blob hashes, source labels and hierarchy are in
[projection.json](projection.json). The parent directory documents assumptions and limitations.
