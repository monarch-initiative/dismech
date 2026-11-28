# Basal cell nevus syndrome (OMIMPS:109400)

## Source entities and member coverage

Candidates below are grounded entries or subtypes whose MONDO term has an explicit
exact match to the numbered OMIM record. This is a mapping-based coverage audit,
not independent evidence of clinical equivalence. A family entry alone is not
counted as individual member coverage. Directional mappings in the selected records
are also shown with their predicates; these are not exact member coverage.

| OMIM member | Source label | MONDO exact matches | Before candidates | After candidates |
|---|---|---|---|---|
| OMIM:109400 | basal cell nevus syndrome 1 | MONDO:0958174 | PTCH1-related nevoid basal cell carcinoma syndrome (`kb/disorders/PTCH1-related_Nevoid_Basal_Cell_Carcinoma_Syndrome.yaml`) | PTCH1-related nevoid basal cell carcinoma syndrome (`kb/disorders/PTCH1-related_Nevoid_Basal_Cell_Carcinoma_Syndrome.yaml`) |
| OMIM:620343 | basal cell nevus syndrome 2 | MONDO:0958189 | SUFU-related nevoid basal cell carcinoma syndrome (`kb/disorders/SUFU-related_Nevoid_Basal_Cell_Carcinoma_Syndrome.yaml`) | SUFU-related nevoid basal cell carcinoma syndrome (`kb/disorders/SUFU-related_Nevoid_Basal_Cell_Carcinoma_Syndrome.yaml`) |

## Joint solver comparison

| Snapshot | Curation commit | Hypotheses | Search status | Search confidence | Distinct satisfying assignments found | Enumeration | MAP certificate |
|---|---|---:|---|---:|---:|---|---|
| [before](before/solution.md) | `0f93e8333acae054726a37ad8a0d65dbf3b0c5b7` | 6 | RETRACTED | 0.5 | 30 | VERIFIED | [ALL_TRUE_INCONSISTENT](before/certificate.json) |
| [after](after/solution.md) | `0f93e8333acae054726a37ad8a0d65dbf3b0c5b7` | 6 | ALL_MAPPINGS_CONSISTENT | 0.95 | 40 | VERIFIED | [ALL_TRUE_SATISFIABLE_SECOND_NOT_CERTIFIED](after/certificate.json) |

Confidence compares the best two distinct complete assignments. It is not a
mapping marginal or proof of biological equivalence. Timeout values are provisional.
A separate MAP certificate proves the optimal all-true assignment and a distinct
runner-up when its sufficient conditions hold; it does not compute marginals or
whole-assignment posteriors. Successful certificates record both assignments;
other statuses state which sufficient condition failed.

### Exhaustive enumeration (complete probabilities)

| Snapshot | Status | Distinct satisfying assignments | Confidence | Best whole-assignment posterior | Rejected mappings in optimal assignments |
|---|---|---:|---:|---:|---|
| [before](before/enumeration.json) | VERIFIED | 30 | 0.5 | 0.456082452579 | [[2], [3]] |
| [after](after/enumeration.json) | VERIFIED | 40 | 0.95 | 0.844892743403 | None |

The complete source assertions, aliases, logical edges and mapping provenance are in
[before/audit.json](before/audit.json) and [after/audit.json](after/audit.json).
Frozen selected curation fields, source blob hashes, source labels and hierarchy are in
[projection.json](projection.json). The parent directory documents assumptions and limitations.

## Controlled intervention and distinct alternatives

Curation is held fixed between these phases. See the [case interpretation](../README.md)
for the source correction, compiler change, or sensitivity experiment being tested.
A higher model score does not establish biological scope.

| Source entity | Canonical label | Relevant source parents |
|---|---|---|
| MONDO:0007187 | nevoid basal cell carcinoma syndrome | MONDO:0000426, MONDO:0015356, MONDO:0019755, MONDO:0021147, MONDO:0042983 |
| MONDO:0958174 | basal cell nevus syndrome 1 | MONDO:0007187 |
| DOID:2512 | nevoid basal cell carcinoma syndrome | DOID:225 |
| DOID:0070365 | nevoid basal cell carcinoma syndrome 1 | DOID:0050736, DOID:2512 |

### before: best two distinct complete assignments

Whole-assignment posteriors: A = 0.456082452579; B = 0.456082452579.
Best-versus-next-best confidence: 0.5.
Only hypotheses with different truth values are shown; every other choice is identical.

| Hypothesis | Input prior | A | B | Mapping marginal |
|---|---:|---|---|---:|
| nevoid basal cell carcinoma syndrome (MONDO:0007187) ≡ nevoid basal cell carcinoma syndrome 1 (DOID:0070365) | 0.95 | reject | accept | 0.487179487179 |
| nevoid basal cell carcinoma syndrome (MONDO:0007187) ≡ nevoid basal cell carcinoma syndrome (DOID:2512) | 0.95 | accept | reject | 0.487179487179 |

### after: best two distinct complete assignments

Whole-assignment posteriors: A = 0.844892743403; B = 0.044468039126.
Best-versus-next-best confidence: 0.95.
Only hypotheses with different truth values are shown; every other choice is identical.

| Hypothesis | Input prior | A | B | Mapping marginal |
|---|---:|---|---|---:|
| nevoid basal cell carcinoma syndrome (MONDO:0007187) ≡ nevoid basal cell carcinoma syndrome (DOID:2512) | 0.95 | accept | reject | 0.95 |
