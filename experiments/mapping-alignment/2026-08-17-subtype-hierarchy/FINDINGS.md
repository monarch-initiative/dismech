# dismech subtype hierarchy vs MONDO hierarchy

**Run date:** 2026-08-17
**KB state:** `d1f1d3c78e` (main, after #8671)
**MONDO:** local semantic-sql build, `~/.data/oaklib/mondo.db`, retrieved 2026-08-11
**Tooling:** [`hierarchy_audit.py`](../scripts/hierarchy_audit.py),
[`solve_conflicts.py`](../scripts/solve_conflicts.py); solver `pyboomer`
([monarch-initiative/boomer-py](https://github.com/monarch-initiative/boomer-py) @ `2bb826c`)

## Question

A dismech entry that declares `has_subtypes` is asserting a real subsumption: the
subtype is a kind of the parent entry. When the parent carries a `disease_term`
and the subtype carries a `subtype_term`, both grounded in MONDO, that assertion
becomes checkable against MONDO's own hierarchy.

Nothing in the current validation stack checks it. `just validate-terms` confirms
each term *exists*; no check confirms the two terms stand in the relationship
dismech's structure implies.

## Method

1. Collect every (parent entry, subtype) pair where both sides carry a MONDO term.
2. Classify against MONDO's entailed `rdfs:subClassOf` closure.
3. Hand every non-agreeing pair to boomer together with the constraints that bear
   on it: dismech's `subtype < parent` (hard), MONDO's subsumption and
   `owl:disjointWith` axioms relating the two terms (hard), and the two identity
   mappings as probabilistic facts with competing subsumption readings.

## Results

1,148 parent/subtype pairs are grounded on both sides.

| Verdict | n | Meaning |
|---|---|---|
| `AGREES` | 1,018 | MONDO has the subtype's term as a descendant of the parent's. |
| `SILENT` | 118 | MONDO relates the two terms in neither direction. |
| `SAME_TERM` | 11 | Subtype and parent grounded to the same term. |
| `REVERSED` | 1 | MONDO says the parent's term is a *descendant* of the subtype's. |

**88.7% agreement.** Where dismech curators asserted a subtype relation and both
sides are grounded, MONDO independently corroborates it nearly nine times in ten.
That is the headline number, and it is a positive result about the KB.

Boomer disposed of all 119 non-agreeing pairs with **zero timeouts** (largest KB:
7 pfacts):

| Outcome | n |
|---|---|
| `PROPOSED_EDGE_CONSISTENT` | 118 |
| `RETRACTED_SUBTYPE_MAPPING` | 1 |

### The one genuine contradiction

`Adult_Refsum_Disease#Type 1` is the only `REVERSED` case, and it is genuinely
unsatisfiable rather than merely unsupported:

- dismech asserts `Adult_Refsum_Disease#Type 1 < Adult_Refsum_Disease`
- the mappings assert `#Type 1 ≡ MONDO:0100258` (phytanoyl-CoA hydroxylase
  deficiency) and `Adult_Refsum_Disease ≡ MONDO:0009958` (adult Refsum disease)
- MONDO asserts `MONDO:0009958 is_a MONDO:0100258`

Chaining those gives `#Type 1 < #Type 1`, and `ProperSubClassOf` is irreflexive.
One of the two identity claims has to go; boomer retracts the subtype's.

This is the case that justifies a solver. It is invisible to every single-source
check — the terms exist, the labels match, each mapping is individually plausible.
It only appears when dismech's hierarchy, the mappings, and MONDO's hierarchy are
evaluated together.

**Not yet fixed in the KB.** Which assertion is wrong is a curation judgement:
MONDO treats adult Refsum disease as a *kind of* PHYH deficiency, dismech treats
PHYH deficiency as the *Type 1 subtype of* adult Refsum disease. Resolving it
means deciding whose nosology dismech follows, not editing a label.

### The 118 silent cases are MONDO gaps, not dismech errors

Spot-checking the `SILENT` rows, they overwhelmingly look like missing `is_a`
edges in MONDO rather than curation mistakes:

- `MONDO:0021081` *anti-NMDA receptor encephalitis* is `is_a MONDO:0019956`
  *encephalitis* only — it does not sit under `MONDO:0020640` *autoimmune
  encephalitis*, though it is the paradigmatic member of that class.
- `MONDO:0035940` *B-lymphoblastic leukemia/lymphoma with t(9;22)* sits under
  `MONDO:0035605` *…with recurrent genetic abnormality*, a branch that does not
  reach `MONDO:0004967` *acute lymphoblastic leukemia*.

For each, boomer confirmed that adding the edge dismech's hierarchy implies is
**consistent with everything MONDO already asserts** — no cycle, no violated
disjointness. All 118 came back `PROPOSED_EDGE_CONSISTENT`.

That makes this list a candidate set of MONDO enrichment proposals derived from
independent curation, which is a more interesting artifact than a dismech defect
list would have been.

## Limits of this measurement

- **`PROPOSED_EDGE_CONSISTENT` is a consistency result, not a correctness
  result.** It says adding the edge breaks nothing MONDO asserts. It does not say
  the edge is biologically right. MONDO has only 533 `owl:disjointWith` axioms, so
  the constraint doing the work is weak, and a proposal can be consistent and
  still wrong. Every one needs a human before it goes to MONDO.
- **Priors are uniform and uncalibrated** (0.90 for each identity mapping). With
  one contradiction in the corpus, nothing here tests whether the priors
  discriminate; the `REVERSED` verdict rests on unsatisfiability, not on the
  posterior ranking.
- **Grounded pairs only.** 1,148 of 2,958 subtypes carry a `subtype_term`; the
  rest are unchecked, and the agreement rate says nothing about them.
- **MONDO is a fixed snapshot.** Some `SILENT` gaps may already be closed
  upstream; re-run before filing anything.
- **The `AGREES` count is not independent corroboration in every case.** Where a
  curator picked the terms *by* navigating MONDO's hierarchy, agreement is partly
  circular. There is no way to separate those from the file alone.

## Reproducing

```bash
uv run python experiments/mapping-alignment/scripts/hierarchy_audit.py \
    --out experiments/mapping-alignment/2026-08-17-subtype-hierarchy/conflicts.tsv

uv run --with networkx python experiments/mapping-alignment/scripts/solve_conflicts.py \
    --conflicts experiments/mapping-alignment/2026-08-17-subtype-hierarchy/conflicts.tsv \
    --out experiments/mapping-alignment/2026-08-17-subtype-hierarchy/verdicts.tsv
```

`solve_conflicts.py` needs a `boomer-py` checkout; point `--boomer-src` at its
`src/`. Nothing in the repo depends on it — the audit script alone reproduces the
classification table without boomer.
