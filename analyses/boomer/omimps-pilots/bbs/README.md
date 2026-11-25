# Bardet-Biedl syndrome (OMIMPS:209900)

## Source entities and member coverage

Candidates below are grounded entries or subtypes whose MONDO term has an explicit
exact match to the numbered OMIM record. This is a mapping-based coverage audit,
not independent evidence of clinical equivalence. A family entry alone is not
counted as individual member coverage. Directional mappings in the selected records
are also shown with their predicates; these are not exact member coverage.

| OMIM member | Source label | MONDO exact matches | Before candidates | After candidates |
|---|---|---|---|---|
| OMIM:209900 | bardet-biedl syndrome 1 | MONDO:0008854 | No grounded candidate | No grounded candidate |
| OMIM:600151 | bardet-biedl syndrome 3 | MONDO:0010832 | No grounded candidate | No grounded candidate |
| OMIM:605231 | bardet-biedl syndrome 6 | MONDO:0011523 | No grounded candidate | No grounded candidate |
| OMIM:615981 | bardet-biedl syndrome 2 | MONDO:0014432 | No grounded candidate | No grounded candidate |
| OMIM:615982 | bardet-biedl syndrome 4 | MONDO:0014433 | No grounded candidate | No grounded candidate |
| OMIM:615983 | bardet-biedl syndrome 5 | MONDO:0014434 | BBS5 — skos:narrowMatch to MONDO:0014434 | BBS5 — skos:narrowMatch to MONDO:0014434 |
| OMIM:615984 | bardet-biedl syndrome 7 | MONDO:0014435 | BBS7 — skos:narrowMatch to MONDO:0014435 | BBS7 — skos:narrowMatch to MONDO:0014435 |
| OMIM:615985 | bardet-biedl syndrome 8 | MONDO:0014436 | No grounded candidate | No grounded candidate |
| OMIM:615986 | bardet-biedl syndrome 9 | MONDO:0014437 | No grounded candidate | No grounded candidate |
| OMIM:615987 | bardet-biedl syndrome 10 | MONDO:0014438 | BBS10 — skos:narrowMatch to MONDO:0014438 | BBS10 — skos:narrowMatch to MONDO:0014438 |
| OMIM:615988 | bardet-biedl syndrome 11 | MONDO:0014439 | No grounded candidate | No grounded candidate |
| OMIM:615989 | bardet-biedl syndrome 12 | MONDO:0014440 | BBS12 — skos:narrowMatch to MONDO:0014440 | BBS12 — skos:narrowMatch to MONDO:0014440 |
| OMIM:615990 | bardet-biedl syndrome 13 | MONDO:0014441 | No grounded candidate | No grounded candidate |
| OMIM:615991 | bardet-biedl syndrome 14 | MONDO:0014442 | No grounded candidate | No grounded candidate |
| OMIM:615992 | bardet-biedl syndrome 15 | MONDO:0014443 | No grounded candidate | No grounded candidate |
| OMIM:615993 | bardet-biedl syndrome 16 | MONDO:0014444 | No grounded candidate | No grounded candidate |
| OMIM:615994 | bardet-biedl syndrome 17 | MONDO:0014445 | No grounded candidate | No grounded candidate |
| OMIM:615995 | bardet-biedl syndrome 18 | MONDO:0014446 | No grounded candidate | No grounded candidate |
| OMIM:615996 | bardet-biedl syndrome 19 | MONDO:0014447 | No grounded candidate | No grounded candidate |
| OMIM:617119 | bardet-biedl syndrome 22 | MONDO:0014926 | No grounded candidate | No grounded candidate |
| OMIM:617406 | bardet-biedl syndrome 21 | MONDO:0044308 | No grounded candidate | No grounded candidate |
| OMIM:619471 | bardet-biedl syndrome 20 | MONDO:0023670 | No grounded candidate | No grounded candidate |

## Joint solver comparison

| Snapshot | Curation commit | Hypotheses | Search status | Search confidence | Distinct satisfying assignments found | Enumeration | MAP certificate |
|---|---|---:|---|---:|---:|---|---|
| [before](before/solution.md) | `a7a4dda562c1fb88c74441601cfe02e2b3f24823` | 14 | TIMED_OUT | 0.9 | 807 | EXHAUSTIVELY_ENUMERATED | [CERTIFIED](before/certificate.json) |
| [after](after/solution.md) | `70f732e3bfe6f7ab306c3a2e19f013a4999b1b08` | 15 | TIMED_OUT | 0.9 | 279 | EXHAUSTIVELY_ENUMERATED | [CERTIFIED](after/certificate.json) |

Confidence compares the best two distinct complete assignments. It is not a
mapping marginal or proof of biological equivalence. Timeout values are provisional.
A separate MAP certificate proves the optimal all-true assignment and a distinct
runner-up when its sufficient conditions hold; it does not compute marginals or
whole-assignment posteriors. Both complete assignments are recorded in that file.

### Exhaustive enumeration (complete probabilities)

| Snapshot | Status | Distinct satisfying assignments | Confidence | Best whole-assignment posterior | Rejected mappings in optimal assignments |
|---|---|---:|---:|---:|---|
| [before](before/enumeration.json) | EXHAUSTIVELY_ENUMERATED | 5184 | 0.9 | 0.44741599759 | None |
| [after](after/enumeration.json) | EXHAUSTIVELY_ENUMERATED | 6480 | 0.9 | 0.515675095796 | None |

The complete source assertions, aliases, logical edges and mapping provenance are in
[before/audit.json](before/audit.json) and [after/audit.json](after/audit.json).
Frozen selected curation fields, source blob hashes, source labels and hierarchy are in
[projection.json](projection.json). The parent directory documents assumptions and limitations.
