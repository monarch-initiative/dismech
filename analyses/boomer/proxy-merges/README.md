# MONDO annotation-aware proxy merges

The disorder generator now preserves MONDO xref qualifiers in a separate
`proxy-merges.json` report and uses them to permit specific same-vocabulary
proxy merges. Mapping hypotheses and their priors remain unchanged. The preferred
external ID is a representative, not a reason to assign it a larger probability.

For example, MONDO:0044720 explicitly marks both ORDO:139564 and ORDO:504476
as equivalent, and marks ORDO:504476 as preferred. We therefore permit that
particular pair to become equivalent through MONDO. Both mapping hypotheses
remain at 0.95. No unrelated ORDO pair receives an exception.

## Results

All 43 changed inputs were attempted with the merged unique-solutions solver.
The 22 previously completed results all completed again: **21 now accept all
high-prior mappings at confidence 0.9**, and **COL11A2 retains one retraction
at confidence 0.5**. Its permitted MeSH merge resolves one conflict; its
DOID:0080677/DOID:4258 pair lacks a preferred annotation and remains constrained.
All 21 previously timed-out inputs still time out; their probability estimates
remain provisional.

CANVAS and cblE both accept their two annotated external equivalents.
Each has 512 distinct consistent assignments, verified by independent exhaustive
enumeration. See the current top five complete assignments for
[CANVAS](alternatives/CANVAS-alternatives.md) and
[cblE](alternatives/Methylcobalamin_Deficiency_Type_cblE-alternatives.md).
The [historical 0.5 ties](../low-confidence/README.md) remain reproducible.

The initial 60-second, eight-worker batch finished 15 searches. Seven formerly
completed searches hit that short limit and were rerun with a 300-second limit
and two workers; all seven completed in 35–39 seconds each. Wall-clock times
are sensitive to concurrency. No hypotheses were pruned to obtain these results.

## Policy and compilation

For each MONDO subject with multiple equivalence hypotheses in one vocabulary:

1. Require a non-obsolete MONDO record and an explicit `MONDO:equivalentTo`
   source qualifier on every selected target. A bare xref is insufficient.
2. Require exactly one `MONDO:preferredExternal` among **all** of that record's
   equivalently mapped targets in the vocabulary, and require it in the input.
3. Permit pairs within that curated set to merge. Retain the other pairwise
   non-equivalence constraints in the vocabulary.

Missing annotations, absent or multiple preferred targets, and obsolete MONDO
records produce review decisions, with the original namespace constraints
retained. The report includes every candidate group, including legacy entries
outside the Mendelian migration scope. Permissions from separate MONDO records
are not transitively closed: permitting A/B and B/C does not permit A/C.

`MemberOfDisjointGroup` means non-equivalence here, not OWL class disjointness.
Unaffected vocabularies retain their original groups. An affected vocabulary is
compiled into two-member groups for the still-forbidden pairs. We use groups
because Boomer also consults them when inferring `ProperSubClassOf` from
`SubClassOf` plus non-equivalence; its current handling of
`NegatedFact(EquivalentTo(...))` does not provide that inference.

Both the main generator and ICD enrichment now translate ordinary external
hierarchy edges into `SubClassOf`. Namespace constraints separately impose
non-equivalence. Automatically making every source subclass edge strict would
otherwise prevent some permitted merges. Explicit `DisjointWith` assertions,
curated dismech strict subtype assertions, MONDO constraints, and probabilistic
directional mapping interpretations are preserved. The migration only converts
external strict edges in these generator-owned inputs; it is not a generic
relaxation tool for curator-authored Boomer KBs.

This follows MONDO's documented use of a preferred external term for a proxy
merge; the compilation into non-equivalence exceptions is our pipeline policy.
See the [MONDO merging guide](https://mondo.readthedocs.io/en/stable/editors-guide/merging-and-obsoleting/)
and [mapping annotation guide](https://mondo.readthedocs.io/en/stable/editors-guide/f-entities/).

## Source versions and artifacts

[mondo-mappings.json](mondo-mappings.json) is a deterministic extraction of
xref targets and qualifiers for the 3,030 MONDO subjects in saved mapping
hypotheses. It normalizes identifier prefixes such as `Orphanet` to `ORDO`,
while retaining original target spellings and qualifier values. The extractor
uses the OBO grammar through `fastobo`, rather than interpreting a bare xref as
an equivalence or parsing qualifiers with regular expressions.

The annotation source is
[mondo-edit.obo at f1526ee](https://github.com/monarch-initiative/mondo/blob/f1526eeae184f43741ca73ae0050d16f0061fd37/src/ontology/mondo-edit.obo).
Its exact download URL and SHA-256 are recorded in the catalog. This is an
**annotation-only refresh**: the saved graph still uses the earlier OAK
snapshots, including MONDO 2026-05-05. CANVAS's preferred annotation is absent
from that older MONDO graph. The migration neither imports new mappings from
the newer source nor refreshes old hierarchy or label snapshots. Each migrated
input has its own annotation report and hash; graph provenance is recorded
separately from annotation provenance.

- [decisions.tsv](decisions.tsv): 95 candidate groups, with scope and reasons.
  Of these, 46 groups in 43 Mendelian inputs qualify; 25 Mendelian groups need
  review. Another 13 qualifying and 11 review groups are in legacy entries.
- [updates.json](updates.json): original index values, input hashes, original
  solution hashes, confidence values, and chosen assignments for changed inputs.
- [baseline/](baseline/): exact original inputs for all 43 migrated entries;
  original CANVAS and cblE solutions also preserve the earlier tie investigation.
- [pending.tsv](pending.tsv): immutable cohort and current input hashes for the
  solver rerun. Its statuses describe the migration checkpoint, not current results.
- [rerun comparison](../runs/curated-proxy-merges/comparison.tsv): current outcomes
  against the baseline, incorporating the longer seven-case retry; timeout
  confidences are excluded from the comparison. `retry.tsv` records the short
  attempts selected for that follow-up.

Only 43 of the 1,728 saved input YAMLs changed. No full regeneration was needed;
all 43 retain identical `pfacts` and `labels`. Inputs without a permitted merge
retain their old bytes. A future full generation emits ordinary external
subclass edges for all entries; where the namespace group is unchanged, this
has the same subclass-plus-non-equivalence meaning as the old strict edge.

## Reproduce

From `analyses/`, with `BOOMER_SRC` pointing to a clean checkout of
`monarch-initiative/boomer-py` at `744038e30741009930f57919ca2f03c6473ed198`:

```bash
# Optional: re-extract the committed catalog from the pinned downloaded source.
just boomer-proxy-annotations /path/to/mondo-edit.obo \
  https://raw.githubusercontent.com/monarch-initiative/mondo/f1526eeae184f43741ca73ae0050d16f0061fd37/src/ontology/mondo-edit.obo

just boomer-proxy-migrate
just boomer-proxy-solve
just boomer-proxy-retry
just boomer-proxy-summary
uv run --with networkx python boomer/scripts/investigate_ties.py --current \
  --boomer-src "$BOOMER_SRC" --out boomer/proxy-merges/alternatives/experiments.json
just boomer-icd10-coverage
```

Migration preflights and validates all selected changes before writing, saves
baseline inputs, and marks old solutions stale. Repeating it verifies the
catalog and changed input hashes without rewriting results. A different catalog
or later input edit requires a new migration, not silently extending the old one.
The older ICD additive migration likewise rejects inputs changed since its own
manifest; its historical hashes must not be rewritten to hide this migration.

Full generation accepts `--mapping-annotations /path/to/catalog.json`; the
committed catalog is the default. New MONDO subjects absent from that catalog
get no inferred exception. Refresh the catalog explicitly when extending its
coverage. OAK remains the hierarchy and label source.

Tests cover OBO qualifiers, missing evidence, pair isolation, overlapping
permissions, explicit disjointness, preserved strictness, unchanged priors,
idempotence, migration scope, and preflight failure. Opt-in actual-solver tests
independently enumerate all assignments for both historical and current CANVAS,
including reversed hypothesis order:

```bash
PYTHONPATH=src BOOMER_SRC=/path/to/boomer-py/src uv run --with networkx --with fastobo pytest \
  tests/test_boomer_proxy_merges.py tests/test_boomer_unique_solutions.py
```
