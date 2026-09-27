# Boomer probability correction: use the merged upstream fix

[PR #39](https://github.com/monarch-initiative/boomer-py/pull/39) is merged.
Use a clean Boomer checkout at **`744038e30741009930f57919ca2f03c6473ed198`**
for the corrected dismech rerun. The checked-in
[`unique-solutions.patch`](unique-solutions.patch) is the historical prototype;
**do not apply it to the merged version**.

The original solver counted multiple search paths to the same complete
assignment when calculating confidence and posteriors. The upstream fix keys
solutions by `(hypothesis index, truth value)`, preserving independent input
priors and genuine ties between distinct solutions. It separates raw traversal
statistics and effort caps from the unique assignments used for scoring.

This differs from the local prototype: the prototype deduplicated before the
candidate cap. The merged fix preserves the raw-node cap. Our full-KB batch
runs disable that cap, so this distinction does not change their configuration.

## Use the merged solver

From the repository root, for a fresh checkout:

```bash
git clone https://github.com/monarch-initiative/boomer-py .cache/boomer-merged
git -C .cache/boomer-merged checkout --detach 744038e30741009930f57919ca2f03c6473ed198
BOOMER_SRC="$PWD/.cache/boomer-merged/src" uv run pytest tests/test_boomer_unique_solutions.py -q
BOOMER_SRC="$PWD/.cache/boomer-merged/src" just --justfile analyses/justfile boomer-refresh-completed
just --justfile analyses/justfile boomer-confidence
```

Boomer remains an analysis-only dependency loaded through `--boomer-src`;
there is no Boomer dependency in dismech's `pyproject.toml`. Each attempt records
its solver revision. The named rerun manifest also pins the input hashes,
source ledger hash, worker count, and timeout. Rerunning resumes missing
checkpoints; a changed configuration requires a new run name.

## Validation and results

The opt-in tests in
[`test_boomer_unique_solutions.py`](../../../tests/test_boomer_unique_solutions.py)
compare three real KBs against exhaustive Boolean enumeration, including every
marginal posterior and reversed hypothesis order. They also verify the raw
candidate cap and retention of separate priors for the same logical fact.
They skip when `BOOMER_SRC` is absent.

| Input | Confidence before | After | Whole-solution posterior before | After |
|---|---:|---:|---:|---:|
| 2-Methylbutyryl-CoA Dehydrogenase Deficiency | 0.5 | 0.9 | 0.177293 | 0.652817 |
| ADan amyloidosis | 0.5 | 0.5 | 0.095971 | 0.353377 |

The ADan tie is retained: the best assignments accept different ICD-11
identity mappings. The [completed-cohort rerun](../runs/unique-solutions-completed/README.md)
contains the larger before/after comparison.

Saved aggregate probabilities cannot be corrected without rerunning: the
solution files do not retain every candidate assignment, and different
assignments occur with different multiplicities. Neither the merged fix nor
the prototype prevents repeated work during traversal. Timed-out searches
remain provisional, even with corrected aggregation.
