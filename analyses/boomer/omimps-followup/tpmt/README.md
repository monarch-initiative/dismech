# Thiopurines, poor metabolism of (OMIMPS:610460)

## Source entities and member coverage

Candidates below are grounded entries or subtypes whose MONDO term has an explicit
exact match to the numbered OMIM record. This is a mapping-based coverage audit,
not independent evidence of clinical equivalence. A family entry alone is not
counted as individual member coverage. Directional mappings in the selected records
are also shown with their predicates; these are not exact member coverage.

| OMIM member | Source label | MONDO exact matches | Before candidates | After candidates |
|---|---|---|---|---|
| OMIM:610460 | thiopurines, poor metabolism of, 1 | MONDO:0012503 | Thiopurine S-methyltransferase Deficiency (`kb/disorders/Thiopurine_S-methyltransferase_Deficiency.yaml`); Thiopurine S-methyltransferase Deficiency — skos:exactMatch to MONDO:0012503 | Thiopurine S-methyltransferase Deficiency (`kb/disorders/Thiopurine_S-methyltransferase_Deficiency.yaml`); Thiopurine S-methyltransferase Deficiency — skos:exactMatch to MONDO:0012503 |
| OMIM:616903 | thiopurines, poor metabolism of, 2 | MONDO:0014826 | No grounded candidate | No grounded candidate |

## Joint solver comparison

| Snapshot | Curation commit | Hypotheses | Search status | Search confidence | Distinct satisfying assignments found | Enumeration | MAP certificate |
|---|---|---:|---|---:|---:|---|---|
| [before](before/solution.md) | `4154918d9967242bca0c68972680e9d7e90ee605` | 6 | RETRACTED | 0.5 | 39 | VERIFIED | [ALL_TRUE_INCONSISTENT](before/certificate.json) |
| [after](after/solution.md) | `4154918d9967242bca0c68972680e9d7e90ee605` | 6 | ALL_MAPPINGS_CONSISTENT | 0.9 | 39 | VERIFIED | [CERTIFIED](after/certificate.json) |

Confidence compares the best two distinct complete assignments. It is not a
mapping marginal or proof of biological equivalence. Timeout values are provisional.
A separate MAP certificate proves the optimal all-true assignment and a distinct
runner-up when its sufficient conditions hold; it does not compute marginals or
whole-assignment posteriors. Successful certificates record both assignments;
other statuses state which sufficient condition failed.

### Exhaustive enumeration (complete probabilities)

| Snapshot | Status | Distinct satisfying assignments | Confidence | Best whole-assignment posterior | Rejected mappings in optimal assignments |
|---|---|---:|---:|---:|---|
| [before](before/enumeration.json) | VERIFIED | 39 | 0.5 | 0.393593384589 | [[2], [3]] |
| [after](after/enumeration.json) | VERIFIED | 39 | 0.9 | 0.765492645618 | None |

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
| MONDO:0012503 | thiopurine S-methyltransferase deficiency | MONDO:0000210, MONDO:0019052 |
| DOID:0061004 | poor metabolism of thiopurines 1 | DOID:0080172 |
| DOID:0080172 | poor metabolism of thiopurines | DOID:0050737, DOID:655 |

### before: best two distinct complete assignments

Whole-assignment posteriors: A = 0.393593384589; B = 0.393593384589.
Best-versus-next-best confidence: 0.5.
Only hypotheses with different truth values are shown; every other choice is identical.

| Hypothesis | Input prior | A | B | Mapping marginal |
|---|---:|---|---|---:|
| thiopurine S-methyltransferase deficiency (MONDO:0012503) ≡ poor metabolism of thiopurines 1 (DOID:0061004) | 0.95 | reject | accept | 0.487179487179 |
| thiopurine S-methyltransferase deficiency (MONDO:0012503) ≡ poor metabolism of thiopurines (DOID:0080172) | 0.95 | accept | reject | 0.487179487179 |

### after: best two distinct complete assignments

Whole-assignment posteriors: A = 0.765492645618; B = 0.085054738402.
Best-versus-next-best confidence: 0.9.
Only hypotheses with different truth values are shown; every other choice is identical.

| Hypothesis | Input prior | A | B | Mapping marginal |
|---|---:|---|---|---:|
| Thiopurine S-methyltransferase Deficiency (dismech:Thiopurine_S-methyltransferase_Deficiency) ≡ thiopurine S-methyltransferase deficiency (MONDO:0012503) | 0.9 | accept | reject | 0.89530029185 |
