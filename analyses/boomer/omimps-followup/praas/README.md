# Proteosome-associated autoinflammatory syndrome (OMIMPS:256040)

## Source entities and member coverage

Candidates below are grounded entries or subtypes whose MONDO term has an explicit
exact match to the numbered OMIM record. This is a mapping-based coverage audit,
not independent evidence of clinical equivalence. A family entry alone is not
counted as individual member coverage. Directional mappings in the selected records
are also shown with their predicates; these are not exact member coverage.

| OMIM member | Source label | MONDO exact matches | Before candidates | After candidates |
|---|---|---|---|---|
| OMIM:256040 | proteasome-associated autoinflammatory syndrome 1 | MONDO:0054698 | PRAAS1 (`kb/disorders/Proteasome_Associated_Autoinflammatory_Syndrome.yaml`) | PRAAS1 (`kb/disorders/Proteasome_Associated_Autoinflammatory_Syndrome.yaml`) |
| OMIM:617591 | proteasome-associated autoinflammatory syndrome 3 | MONDO:0054699 | PRAAS3 (`kb/disorders/Proteasome_Associated_Autoinflammatory_Syndrome.yaml`) | PRAAS3 (`kb/disorders/Proteasome_Associated_Autoinflammatory_Syndrome.yaml`) |
| OMIM:618048 | proteasome-associated autoinflammatory syndrome 2 | MONDO:0054700 | PRAAS2 (`kb/disorders/Proteasome_Associated_Autoinflammatory_Syndrome.yaml`) | PRAAS2 (`kb/disorders/Proteasome_Associated_Autoinflammatory_Syndrome.yaml`) |
| OMIM:619175 | proteasome-associated autoinflammatory syndrome 5 | MONDO:0030924 | PRAAS5 (`kb/disorders/Proteasome_Associated_Autoinflammatory_Syndrome.yaml`) | PRAAS5 (`kb/disorders/Proteasome_Associated_Autoinflammatory_Syndrome.yaml`) |
| OMIM:619183 | proteasome-associated autoinflammatory syndrome 4 | MONDO:0030931 | PRAAS4 (`kb/disorders/Proteasome_Associated_Autoinflammatory_Syndrome.yaml`) | PRAAS4 (`kb/disorders/Proteasome_Associated_Autoinflammatory_Syndrome.yaml`) |
| OMIM:620796 | proteasome-associated autoinflammatory syndrome 6 | MONDO:0968983 | PRAAS6 (`kb/disorders/Proteasome_Associated_Autoinflammatory_Syndrome.yaml`) | PRAAS6 (`kb/disorders/Proteasome_Associated_Autoinflammatory_Syndrome.yaml`) |

## Joint solver comparison

| Snapshot | Curation commit | Hypotheses | Search status | Search confidence | Distinct satisfying assignments found | Enumeration | MAP certificate |
|---|---|---:|---|---:|---:|---|---|
| [before](before/solution.md) | `f923d7630deda4d7a0ef50e02f3b41568564e6a8` | 17 | TIMED_OUT | 0.5 | 1202 | EXHAUSTIVELY_ENUMERATED | [ALL_TRUE_INCONSISTENT](before/certificate.json) |
| [after](after/solution.md) | `f923d7630deda4d7a0ef50e02f3b41568564e6a8` | 17 | TIMED_OUT | 0.9 | 1267 | EXHAUSTIVELY_ENUMERATED | [CERTIFIED](after/certificate.json) |

Confidence compares the best two distinct complete assignments. It is not a
mapping marginal or proof of biological equivalence. Timeout values are provisional.
A separate MAP certificate proves the optimal all-true assignment and a distinct
runner-up when its sufficient conditions hold; it does not compute marginals or
whole-assignment posteriors. Successful certificates record both assignments;
other statuses state which sufficient condition failed.

### Exhaustive enumeration (complete probabilities)

| Snapshot | Status | Distinct satisfying assignments | Confidence | Best whole-assignment posterior | Rejected mappings in optimal assignments |
|---|---|---:|---:|---:|---|
| [before](before/enumeration.json) | EXHAUSTIVELY_ENUMERATED | 61440 | 0.5 | 0.187549731394 | [[9], [8]] |
| [after](after/enumeration.json) | EXHAUSTIVELY_ENUMERATED | 81920 | 0.9 | 0.347435877408 | None |

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
| MONDO:0009726 | proteosome-associated autoinflammatory syndrome | MONDO:0005046, MONDO:0006025, MONDO:0019751, MONDO:0957408 |
| MONDO:0054698 | proteasome-associated autoinflammatory syndrome 1 | MONDO:0009726 |
| DOID:0060913 | proteasome-associated autoinflammatory syndrome | DOID:0051000 |
| DOID:0050553 | proteasome-associated autoinflammatory syndrome 1 | DOID:0050737, DOID:0060913, DOID:0080578 |

### before: best two distinct complete assignments

Whole-assignment posteriors: A = 0.187549731394; B = 0.187549731394.
Best-versus-next-best confidence: 0.5.
Only hypotheses with different truth values are shown; every other choice is identical.

| Hypothesis | Input prior | A | B | Mapping marginal |
|---|---:|---|---|---:|
| proteosome-associated autoinflammatory syndrome (MONDO:0009726) ≡ proteasome-associated autoinflammatory syndrome 1 (DOID:0050553) | 0.95 | accept | reject | 0.487179487179 |
| proteosome-associated autoinflammatory syndrome (MONDO:0009726) ≡ proteasome-associated autoinflammatory syndrome (DOID:0060913) | 0.95 | reject | accept | 0.487179487179 |

### after: best two distinct complete assignments

Whole-assignment posteriors: A = 0.347435877408; B = 0.038603986379.
Best-versus-next-best confidence: 0.9.
Only hypotheses with different truth values are shown; every other choice is identical.

| Hypothesis | Input prior | A | B | Mapping marginal |
|---|---:|---|---|---:|
| PRAAS6 (dismech:Proteasome_Associated_Autoinflammatory_Syndrome#PRAAS6) ≡ proteasome-associated autoinflammatory syndrome 6 (MONDO:0968983) | 0.9 | accept | reject | 0.9 |
