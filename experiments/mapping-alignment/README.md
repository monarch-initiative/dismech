# mapping-alignment

**Question:** dismech, MONDO, and the external vocabularies each make assertions
about the same diseases. Where those assertions are checked against each other
rather than in isolation, do they agree — and where they conflict, can a
probabilistic reasoner say which one to give up?

Nothing in the validation stack asks this. `just validate-terms` confirms a term
*exists* and that its label matches; `linkml-reference-validator` checks quoted
evidence. Neither checks whether dismech's own structure is consistent with the
structure of the ontology it is grounded in.

## Why a solver, and where it earns its place

The prompt for these runs was whether
[`boomer-py`](https://github.com/monarch-initiative/boomer-py) — a Python
reimplementation of BOOMER, which resolves competing ontology mappings by finding
the most probable globally consistent assignment — is useful against dismech.

The answer so far is **yes, but narrowly**, and the reason is a semantic one worth
stating up front.

dismech's `disease_term` is a **grounding**, not an identity claim: the schema
defines it as "The MONDO disease term for this disease", and `subtype_term` as
"The ontology term grounding this subtype… Prefer MONDO when available". Only
`mappings[].mapping_predicate` asserts a `skos:` relationship. Treating a shared
`disease_term` as a shared `skos:exactMatch` manufactures conflicts that are not
there — 136 MONDO terms are grounded by more than one entry, but that is
expected when MONDO has no more specific term (five NSCLC molecular-subtype
entries all ground to `MONDO:0005061` *lung adenocarcinoma*, correctly). Under
the correct reading only **1** term in the KB has two entries claiming
`exactMatch` to it.

So the KB contains few jointly-unsatisfiable constraint sets, and a solver is not
the right tool for most mapping QC here. Where it *is* the right tool is the case
no single-source check can reach: an inconsistency that only exists when
dismech's hierarchy, the mappings, and MONDO's hierarchy are evaluated together.
The `Adult_Refsum_Disease` case in the subtype-hierarchy run is exactly that, and
a groupby cannot find it.

## Runs

| Run | Question | Headline |
|---|---|---|
| [`2026-08-17-subtype-hierarchy/`](2026-08-17-subtype-hierarchy/) | Does MONDO agree with the subsumptions dismech asserts via `has_subtypes`? | 88.7% agreement (1,018/1,148). 1 genuine contradiction; 118 apparent MONDO gaps, all consistent to add. |
| [`2026-08-17-grouping-membership/`](2026-08-17-grouping-membership/) | Does MONDO agree that the members of an `exactMatch`-mapped grouping fall under its term? | 89.4% agreement (93/104). 0 contradictions; 8 more apparent MONDO gaps. |
| [`2026-08-17-cross-source/`](2026-08-17-cross-source/) | Do dismech's direct ICD/NCIT mappings agree with MONDO's own xrefs? | 7 disagreements, 6 of them granularity. Negative result for the solver. |

Two structurally independent checks of the same underlying question agree
closely — 88.7% and 89.4%, same failure mode, one contradiction between them.
That consistency is itself a result: dismech's curated structure agrees with
MONDO wherever MONDO has an opinion, and where it disagrees the gap is almost
always on MONDO's side. Between them the two runs yield **126 candidate MONDO
enrichment proposals** derived from independent curation.

## Tooling

| Script | Needs boomer | Purpose |
|---|---|---|
| [`scripts/hierarchy_audit.py`](scripts/hierarchy_audit.py) | no | Classify every grounded parent/subtype pair against MONDO's closure. |
| [`scripts/solve_conflicts.py`](scripts/solve_conflicts.py) | yes | Hand each non-agreeing pair to boomer with the dismech, MONDO, and mapping constraints that bear on it. |
| [`scripts/grouping_audit.py`](scripts/grouping_audit.py) | no | Check members of `exactMatch`-mapped groupings against the grouping's MONDO term. |
| [`scripts/crosssource_audit.py`](scripts/crosssource_audit.py) | no | Compare direct external mappings against MONDO's xrefs for the same vocabulary. |

Three of the four need no solver at all. `solve_conflicts.py` takes
`--boomer-src` pointing at a `boomer-py` checkout; **nothing in the repo depends
on boomer**, and no dependency was added. That is deliberate — boomer-py is an
early-stage project (~25 commits at time of writing) and this experiment does not
justify taking it on as a dependency.

All four read a local semantic-sql MONDO build at `~/.data/oaklib/mondo.db`. It
is a fixed snapshot, so re-run before acting on any finding.

## Methodological notes carried forward

Two mistakes made and corrected while building this, recorded so they are not
repeated:

- **Circular lexical evidence.** An earlier version of the specificity audit that
  produced #8671 used `disease_term.preferred_term` as a lexical synonym when
  matching entries against MONDO labels. That string is derived from the mapping
  under test, so it corroborated the mapping with itself. Excluding it dropped
  the raw match count 6,091 → 4,299 and removed several spurious hits. Only
  curator-authored, mapping-independent labels are safe as evidence.
- **Bare-acronym lexical matches.** 789 of 2,958 subtype names are acronym-like.
  Matching on the bare acronym produces confident nonsense — `TBS` matched
  Townes-Brocks syndrome for a Temple-Baraitser subtype, `AD` matched Alzheimer
  disease for anauxetic dysplasia. Of 512 acronym subtypes that matched
  something, only 10 disagreed with the curated term, and 6 of those 10 were
  wrong. Never propose a retarget from a synonym-only match on a bare acronym
  without a second signal.
