# Homocystinuria-megaloblastic anemia (OMIMPS:236270)

## Source entities and member coverage

Candidates below are grounded entries or subtypes whose MONDO term has an explicit
exact match to the numbered OMIM record. This is a mapping-based coverage audit,
not independent evidence of clinical equivalence. A family entry alone is not
counted as individual member coverage. Directional mappings in the selected records
are also shown with their predicates; these are not exact member coverage.

| OMIM member | Source label | MONDO exact matches | Before candidates | After candidates |
|---|---|---|---|---|
| OMIM:236270 | homocystinuria-megaloblastic anemia, cble type | MONDO:0009354 | cblE (`kb/disorders/Inborn_Disorder_of_Cobalamin_Metabolism_and_Transport.yaml`); Methylcobalamin Deficiency Type cblE (`kb/disorders/Methylcobalamin_Deficiency_Type_cblE.yaml`) | cblE (`kb/disorders/Inborn_Disorder_of_Cobalamin_Metabolism_and_Transport.yaml`); Methylcobalamin Deficiency Type cblE (`kb/disorders/Methylcobalamin_Deficiency_Type_cblE.yaml`) |
| OMIM:250940 | homocystinuria-megaloblastic anemia, cblg type | MONDO:0009609 | cblG (`kb/disorders/Inborn_Disorder_of_Cobalamin_Metabolism_and_Transport.yaml`); Methylcobalamin Deficiency Type cblG (`kb/disorders/Methylcobalamin_Deficiency_Type_cblG.yaml`) | cblG (`kb/disorders/Inborn_Disorder_of_Cobalamin_Metabolism_and_Transport.yaml`); Methylcobalamin Deficiency Type cblG (`kb/disorders/Methylcobalamin_Deficiency_Type_cblG.yaml`) |
| OMIM:620952 | homocystinuria-megaloblastic anemia, cbld type | MONDO:0700297 | cblD-HC (`kb/disorders/MMADHC-related_Disorder_of_Cobalamin_Metabolism_cblD_Type.yaml`) | cblD-HC (`kb/disorders/MMADHC-related_Disorder_of_Cobalamin_Metabolism_cblD_Type.yaml`) |

## Joint solver comparison

| Snapshot | Curation commit | Hypotheses | Search status | Search confidence | Distinct satisfying assignments found | Enumeration | MAP certificate |
|---|---|---:|---|---:|---:|---|---|
| [before](before/solution.md) | `bef670f17076625c96e5e8955a0a83d2d5108257` | 14 | TIMED_OUT | 0.9 | 1763 | EXHAUSTIVELY_ENUMERATED | [CERTIFIED](before/certificate.json) |
| [after](after/solution.md) | `bf2c4a6a5efdb3a4eff0e377186fdcab53ba2c2a` | 15 | TIMED_OUT | 0.9 | 2012 | EXHAUSTIVELY_ENUMERATED | [CERTIFIED](after/certificate.json) |

Confidence compares the best two distinct complete assignments. It is not a
mapping marginal or proof of biological equivalence. Timeout values are provisional.
A separate MAP certificate proves the optimal all-true assignment and a distinct
runner-up when its sufficient conditions hold; it does not compute marginals or
whole-assignment posteriors. Both complete assignments are recorded in that file.

### Exhaustive enumeration (complete probabilities)

| Snapshot | Status | Distinct satisfying assignments | Confidence | Best whole-assignment posterior | Rejected mappings in optimal assignments |
|---|---|---:|---:|---:|---|
| [before](before/enumeration.json) | EXHAUSTIVELY_ENUMERATED | 10240 | 0.9 | 0.386482671882 | None |
| [after](after/enumeration.json) | EXHAUSTIVELY_ENUMERATED | 20480 | 0.9 | 0.367158538288 | None |

The complete source assertions, aliases, logical edges and mapping provenance are in
[before/audit.json](before/audit.json) and [after/audit.json](after/audit.json).
Frozen selected curation fields, source blob hashes, source labels and hierarchy are in
[projection.json](projection.json). The parent directory documents assumptions and limitations.
