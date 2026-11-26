# Anterior segment dysgenesis (OMIMPS:107250)

## Source entities and member coverage

Candidates below are grounded entries or subtypes whose MONDO term has an explicit
exact match to the numbered OMIM record. This is a mapping-based coverage audit,
not independent evidence of clinical equivalence. A family entry alone is not
counted as individual member coverage. Directional mappings in the selected records
are also shown with their predicates; these are not exact member coverage.

| OMIM member | Source label | MONDO exact matches | Before candidates | After candidates |
|---|---|---|---|---|
| OMIM:107250 | anterior segment dysgenesis 1 | MONDO:0007138 | No grounded candidate | No grounded candidate |
| OMIM:137600 | anterior segment dysgenesis 4 | MONDO:0007662 | No grounded candidate | No grounded candidate |
| OMIM:269400 | anterior segment dysgenesis 7 | MONDO:0010015 | No grounded candidate | No grounded candidate |
| OMIM:601631 | anterior segment dysgenesis 3 | MONDO:0024456 | No grounded candidate | No grounded candidate |
| OMIM:604229 | anterior segment dysgenesis 5 | MONDO:0011414 | No grounded candidate | No grounded candidate |
| OMIM:610256 | anterior segment dysgenesis 2 | MONDO:0012456 | Primary Aphakia (`kb/disorders/FOXE3_Anterior_Segment_Dysgenesis.yaml`) | Primary Aphakia (`kb/disorders/FOXE3_Anterior_Segment_Dysgenesis.yaml`) |
| OMIM:617315 | anterior segment dysgenesis 6 | MONDO:0015016 | No grounded candidate | No grounded candidate |
| OMIM:617319 | anterior segment dysgenesis 8 | MONDO:0015017 | No grounded candidate | No grounded candidate |

## Joint solver comparison

| Snapshot | Curation commit | Hypotheses | Search status | Search confidence | Distinct satisfying assignments found | Enumeration | MAP certificate |
|---|---|---:|---|---:|---:|---|---|
| [before](before/solution.md) | `4a5e3803772c52801fd00b4116e6e061e1ee7e56` | 7 | ALL_MAPPINGS_CONSISTENT | 0.9 | 96 | VERIFIED | [CERTIFIED](before/certificate.json) |
| [after](after/solution.md) | `4a5e3803772c52801fd00b4116e6e061e1ee7e56` | 6 | ALL_MAPPINGS_CONSISTENT | 0.9 | 64 | VERIFIED | [CERTIFIED](after/certificate.json) |

Confidence compares the best two distinct complete assignments. It is not a
mapping marginal or proof of biological equivalence. Timeout values are provisional.
A separate MAP certificate proves the optimal all-true assignment and a distinct
runner-up when its sufficient conditions hold; it does not compute marginals or
whole-assignment posteriors. Successful certificates record both assignments;
other statuses state which sufficient condition failed.

### Exhaustive enumeration (complete probabilities)

| Snapshot | Status | Distinct satisfying assignments | Confidence | Best whole-assignment posterior | Rejected mappings in optimal assignments |
|---|---|---:|---:|---:|---|
| [before](before/enumeration.json) | VERIFIED | 96 | 0.9 | 0.621753985602 | None |
| [after](after/enumeration.json) | VERIFIED | 64 | 0.9 | 0.625026375 | None |

The complete source assertions, aliases, logical edges and mapping provenance are in
[before/audit.json](before/audit.json) and [after/audit.json](after/audit.json).
Frozen selected curation fields, source blob hashes, source labels and hierarchy are in
[projection.json](projection.json). The parent directory documents assumptions and limitations.

## Controlled intervention and distinct alternatives

Curation is held fixed between these phases. See the [case interpretation](../README.md)
for the source correction, compiler change, or sensitivity experiment being tested.
A higher model score does not establish biological scope.


### before: best two distinct complete assignments

Whole-assignment posteriors: A = 0.621753985602; B = 0.069083776178.
Best-versus-next-best confidence: 0.9.
Only hypotheses with different truth values are shown; every other choice is identical.

| Hypothesis | Input prior | A | B | Mapping marginal |
|---|---:|---|---|---:|
| Primary Aphakia (dismech:FOXE3_Anterior_Segment_Dysgenesis#Primary Aphakia) ≡ congenital primary aphakia (MONDO:0012456) | 0.9 | accept | reject | 0.9 |

### after: best two distinct complete assignments

Whole-assignment posteriors: A = 0.625026375; B = 0.069447375.
Best-versus-next-best confidence: 0.9.
Only hypotheses with different truth values are shown; every other choice is identical.

| Hypothesis | Input prior | A | B | Mapping marginal |
|---|---:|---|---|---:|
| Primary Aphakia (dismech:FOXE3_Anterior_Segment_Dysgenesis#Primary Aphakia) ≡ congenital primary aphakia (MONDO:0012456) | 0.9 | accept | reject | 0.9 |
