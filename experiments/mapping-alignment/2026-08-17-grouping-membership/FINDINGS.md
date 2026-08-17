# dismech grouping membership vs MONDO hierarchy

**Run date:** 2026-08-17
**KB state:** `d1f1d3c78e` (main, after #8671)
**MONDO:** local semantic-sql build, `~/.data/oaklib/mondo.db`, retrieved 2026-08-11
**Tooling:** [`grouping_audit.py`](../scripts/grouping_audit.py)

## Question

A `kb/groupings/` entry is a curated **union**: it lists the member diseases that
belong together, and points *down* at them rather than being inferred from them.
When the grouping itself carries a `skos:exactMatch` MONDO mapping and its members
carry `disease_term`s, the union becomes checkable — if the grouping *is* that
MONDO class, every member's term should be a descendant of it.

This is a second, independent structure to test the same underlying question as
the [subtype-hierarchy run](../2026-08-17-subtype-hierarchy/FINDINGS.md): does
dismech's curated structure agree with MONDO's?

Note the existing `just check-groupings` evaluates members against
`membership_criteria` — a different question. It does not compare member
`disease_term`s against the grouping's own MONDO mapping.

## Scope

65 groupings, 398 members. Only the **13 groupings whose MONDO mapping is
`skos:exactMatch`** are checked, giving 104 member checks.

The other 52 groupings are skipped deliberately, not for lack of data. A
`broadMatch` grouping is explicitly *narrower* than its MONDO term and a
`narrowMatch` one explicitly *wider*, so neither licenses the descendant
expectation; `closeMatch` and `relatedMatch` are too weak to test against. Reading
those as identity claims is exactly the error that inflated the first pass of this
experiment.

## Results

| Verdict | n |
|---|---|
| `AGREES` | 93 |
| `SILENT` | 8 |
| `SAME_TERM` | 2 |
| member has no MONDO `disease_term` | 1 |

**89.4% agreement** (93/104), and — notably — **zero `REVERSED` cases**. No
grouping produces a logical contradiction.

## The 8 violations are MONDO gaps again

| Grouping | Member | Member term |
|---|---|---|
| Ciliopathies | Nephronophthisis | `MONDO:0019005` nephronophthisis |
| Ciliopathies | Short-Rib Polydactyly Syndrome | `MONDO:0015461` |
| Ciliopathies | Cranioectodermal Dysplasia | `MONDO:0009032` |
| Ciliopathies | EYS-Related Retinitis Pigmentosa | `MONDO:0011272` retinitis pigmentosa 25 |
| Disorders of GPI Anchor Biosynthesis | Multiple Congenital Anomalies-Hypotonia-Seizures Syndrome | `MONDO:0100247` |
| Mitochondrial Complex IV Deficiency | SCO2-Related Fatal Infantile Cardioencephalomyopathy | `MONDO:0011451` |
| Mitochondrial Complex IV Deficiency | COX15-Related COX Deficiency | `MONDO:0014051` |
| Tubulinopathies | TUBA1A-related Tubulinopathy | `MONDO:0012703` lissencephaly due to TUBA1A mutation |

Several are textbook members of their grouping. Nephronophthisis is a canonical
ciliopathy; `lissencephaly due to TUBA1A mutation` is a canonical tubulinopathy.
That MONDO does not place them under `MONDO:0005308 ciliopathy` and
`MONDO:0100153 tubulinopathy` respectively reads as missing `is_a` edges rather
than as dismech mis-grouping them.

## What this adds to the experiment

Two structurally independent checks now agree closely:

| Check | Pairs | Agreement | Contradictions |
|---|---|---|---|
| subtype hierarchy | 1,148 | 88.7% | 1 |
| grouping membership | 104 | 89.4% | 0 |

Same rate, same failure mode, one contradiction between them. That consistency is
itself the finding: dismech's curated structure agrees with MONDO wherever MONDO
has an opinion, and where it disagrees the gap is almost always on MONDO's side.

Combined, the two runs yield **126 candidate MONDO enrichment proposals** (118 +
8) derived from independent curation.

This run needed **no solver** — with zero `REVERSED` cases there is nothing
jointly unsatisfiable to resolve. Recorded as such rather than run through boomer
for appearances.

## Limits of this measurement

- **13 of 65 groupings tested.** The `exactMatch` restriction is deliberate and
  correct, but it means this measures a minority of the grouping corpus, and the
  agreement rate should not be read as covering all groupings.
- **`SILENT` is not proof of a MONDO gap.** It is the absence of an asserted path.
  Some members may be legitimately outside the MONDO class even though dismech
  groups them — a grouping's `grouping_basis` can be `SHARED_MECHANISM` or
  `CLINICAL_CONVENTION`, which need not track MONDO's classification axis. Each
  needs a human before it goes upstream.
- **Members are matched by `Disease.name`**, which is what `members[].member`
  references. A rename would silently drop a member from this audit;
  `tests/test_data.py` enforces the foreign key, so that is caught elsewhere.
- **Same fixed MONDO snapshot** as the other runs; re-run before filing anything.

## Reproducing

```bash
uv run python experiments/mapping-alignment/scripts/grouping_audit.py \
    --out experiments/mapping-alignment/2026-08-17-grouping-membership/violations.tsv
```

No solver required.
