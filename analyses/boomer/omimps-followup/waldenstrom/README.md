# Macroglobulinemia, Waldenstrom (OMIMPS:153600)

## Source entities and member coverage

Candidates below are grounded entries or subtypes whose MONDO term has an explicit
exact match to the numbered OMIM record. This is a mapping-based coverage audit,
not independent evidence of clinical equivalence. A family entry alone is not
counted as individual member coverage. Directional mappings in the selected records
are also shown with their predicates; these are not exact member coverage.

| OMIM member | Source label | MONDO exact matches | Before candidates | After candidates |
|---|---|---|---|---|
| OMIM:153600 | macroglobulinemia, waldenstrom, susceptibility to, 1 | MONDO:0100281 | No grounded candidate | No grounded candidate |
| OMIM:610430 | macroglobulinemia, waldenstrom, susceptibility to, 2 | MONDO:0012491 | No grounded candidate | No grounded candidate |

## Joint solver comparison

| Snapshot | Curation commit | Hypotheses | Search status | Search confidence | Distinct satisfying assignments found | Enumeration | MAP certificate |
|---|---|---:|---|---:|---:|---|---|
| [before](before/solution.md) | `2d9b2e5c35c3471a85b2690a8dff3e72573785d1` | 2 | ALL_MAPPINGS_CONSISTENT | 0.9 | 4 | VERIFIED | [CERTIFIED](before/certificate.json) |
| [after](after/solution.md) | `2d9b2e5c35c3471a85b2690a8dff3e72573785d1` | 1 | ALL_MAPPINGS_CONSISTENT | 0.9 | 2 | VERIFIED | [CERTIFIED](after/certificate.json) |

Confidence compares the best two distinct complete assignments. It is not a
mapping marginal or proof of biological equivalence. Timeout values are provisional.
A separate MAP certificate proves the optimal all-true assignment and a distinct
runner-up when its sufficient conditions hold; it does not compute marginals or
whole-assignment posteriors. Successful certificates record both assignments;
other statuses state which sufficient condition failed.

### Exhaustive enumeration (complete probabilities)

| Snapshot | Status | Distinct satisfying assignments | Confidence | Best whole-assignment posterior | Rejected mappings in optimal assignments |
|---|---|---:|---:|---:|---|
| [before](before/enumeration.json) | VERIFIED | 4 | 0.9 | 0.855 | None |
| [after](after/enumeration.json) | VERIFIED | 2 | 0.9 | 0.9 | None |

The complete source assertions, aliases, logical edges and mapping provenance are in
[before/audit.json](before/audit.json) and [after/audit.json](after/audit.json).
Frozen selected curation fields, source blob hashes, source labels and hierarchy are in
[projection.json](projection.json). The parent directory documents assumptions and limitations.

## Controlled intervention and distinct alternatives

Curation is held fixed between these phases. See the [case interpretation](../README.md)
for the source correction, compiler change, or sensitivity experiment being tested.
A higher model score does not establish biological scope.


### before: best two distinct complete assignments

Whole-assignment posteriors: A = 0.855; B = 0.095.
Best-versus-next-best confidence: 0.9.
Only hypotheses with different truth values are shown; every other choice is identical.

| Hypothesis | Input prior | A | B | Mapping marginal |
|---|---:|---|---|---:|
| Waldenstrom Macroglobulinemia (dismech:Waldenstrom_Macroglobulinemia) ≡ Waldenstrom macroglobulinemia (MONDO:0100280) | 0.9 | accept | reject | 0.9 |

### after: best two distinct complete assignments

Whole-assignment posteriors: A = 0.9; B = 0.1.
Best-versus-next-best confidence: 0.9.
Only hypotheses with different truth values are shown; every other choice is identical.

| Hypothesis | Input prior | A | B | Mapping marginal |
|---|---:|---|---|---:|
| Waldenstrom Macroglobulinemia (dismech:Waldenstrom_Macroglobulinemia) ≡ Waldenstrom macroglobulinemia (MONDO:0100280) | 0.9 | accept | reject | 0.9 |
