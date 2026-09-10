# Count solutions once when calculating Boomer probabilities

The September 8 batch imported Boomer from a local clean Git checkout at
`16769dc84375af522357fc7b67077ee862bbc8e8`. Boomer is not installed by
dismech's `pyproject.toml`; `--boomer-src` selects its source directory.

At that revision, `search()` can return multiple terminal nodes with the same
complete assignment of hypothesis indices to truth values. `solve()` counts
each node separately when ranking candidates and normalizing probabilities.
Upstream `tests/test_search.py::test_asserted_multi_labeled_edges` explicitly
notes the identical-world behavior in a TODO, and some existing test expectations
include its effect. The documented model defines a solution by its assignment,
not the path taken to reach it.

## Local correction

[`unique-solutions.patch`](unique-solutions.patch) adds a set of complete
satisfiable assignments in `solve()`, keyed by `(hypothesis index, truth value)`.
An assignment is accepted once, before the candidate cap is checked and before
confidence or posteriors are calculated. Distinct assignments with equal priors
remain separate. Separate hypothesis indices with different priors also remain
separate and continue to contribute to the joint probability.

The patch does not change search traversal, reasoning, input facts, or priors.
Unsatisfiable branches remain available for the existing pruning statistics.
Those coverage statistics remain estimates; this does not repair overlapping
implicit counts or turn a timeout into a completed search. Deduplicating while
aggregating does not prevent the search from spending time on repeated paths.

This is a local mitigation, not an upstream release. The patch targets the exact
revision above; do not apply it blindly to another revision. An upstream change
should also update the existing tests that currently expect repeated-world
counts and probabilities.

## Reproduce the corrected checkout

From the dismech repository root, using a fresh destination:

```bash
git clone https://github.com/monarch-initiative/boomer-py .cache/boomer-unique-solutions
git -C .cache/boomer-unique-solutions checkout -b dismech-unique-solutions 16769dc84375af522357fc7b67077ee862bbc8e8
git -C .cache/boomer-unique-solutions apply --check --unidiff-zero "$PWD/analyses/boomer/patches/unique-solutions.patch"
git -C .cache/boomer-unique-solutions apply --unidiff-zero "$PWD/analyses/boomer/patches/unique-solutions.patch"
BOOMER_SRC="$PWD/.cache/boomer-unique-solutions/src" PYTHONHASHSEED=0 \
  uv run pytest tests/test_boomer_unique_solutions.py -q
git -C .cache/boomer-unique-solutions add src/boomer/search.py
git -C .cache/boomer-unique-solutions commit -m "Deduplicate complete assignments before scoring solutions"
```

The local commit makes the patched checkout clean and gives it a distinct
revision that the batch runner can record. The patch has zero context lines,
so `git apply` requires `--unidiff-zero`. It is stored here instead of changing
the user's working Boomer checkout or introducing an implicit runtime patch.

To inspect a corrected solve without replacing saved results:

```bash
BOOMER_SRC="$PWD/.cache/boomer-unique-solutions/src" \
  just --justfile analyses/justfile boomer-solve 2-Methylbutyryl-CoA_Dehydrogenase_Deficiency
```

This prints a new solve to stdout. The CLI's default search limits still apply;
the regression tests below disable partitioning and count caps for their small
inputs. `boomer-solve-pending` only processes `NOT_RUN` and `STALE_INPUT` rows,
so merely changing `BOOMER_SRC` does not refresh already completed results.

## Verification

[`test_boomer_unique_solutions.py`](../../../tests/test_boomer_unique_solutions.py)
contains seven opt-in tests. They fail against the original solver and pass
against the patched solver (the original was checked with stop-on-first-failure).
Without `BOOMER_SRC`, they skip rather than adding a runtime dependency.

For two real saved inputs, the tests enumerate every Boolean assignment once,
check consistency with Boomer's reasoner, and independently calculate the joint
weights, confidence, whole-solution posterior, and every marginal posterior.
They repeat with reversed hypothesis order. This verifies aggregation against
exhaustive enumeration under the existing reasoner's semantics; it is not an
independent validation of that reasoner or the ontology assertions.

| Input | Returned satisfiable nodes before | Distinct solutions | Confidence before | Confidence after | Whole-solution posterior before | After |
|---|---:|---:|---:|---:|---:|---:|
| 2-Methylbutyryl-CoA Dehydrogenase Deficiency | 288 | 128 | 0.5 | 0.9 | 0.177293 | 0.652817 |
| ADan amyloidosis | 432 | 192 | 0.5 | 0.5 | 0.095971 | 0.353377 |

The ADan tie is retained: the top assignments accept different ICD-11 identity
mappings. The other tests verify that duplicate paths do not consume the
candidate cap, equal-weight distinct assignments survive, and two priors for
the same logical fact both contribute to its probability.

No saved inputs or solution files were changed by this correction. Existing
`solution.yaml` files retain only the selected assignment and aggregate scores,
not the full candidate population, so their probabilities cannot be repaired
by a simple post-processing pass. Rerunning the saved KBs is required. Different
assignments occur with different multiplicities, so dividing all scores by four
would not correct them.
