# Corrected probabilities for the completed Mendelian cohort

The September 11 refresh reran the **1,213 inputs that completed in the
[original batch](../pending/README.md)** using merged Boomer commit
`744038e30741009930f57919ca2f03c6473ed198` ([upstream PR](https://github.com/monarch-initiative/boomer-py/pull/39)).
It produced **1,176 consistent, 32 retracted, and 5 timed-out results**.
No chosen mapping assignments changed, including the provisional candidates
returned by the five timeouts. All 1,728 input YAMLs stayed byte-identical.

## Confidence and posterior results

All 1,213 previous confidence scores were 0.5. Among the **1,208 completed
refreshes**, corrected confidence is distributed as follows:

| Confidence | Inputs | Interpretation in this cohort |
|---:|---:|---|
| 0.50 | 32 | Retracted cases with equally probable best alternatives |
| 0.70 | 2 | Consistent cases with weaker grounding priors |
| 0.90 | 1,102 | Consistent cases |
| 0.95 | 72 | Consistent cases |

Confidence compares the best and next-best **distinct assignments**:
`P(best) / (P(best) + P(second))`. It is not the posterior probability of the
whole assignment, and neither quantity is a clinically calibrated probability.
Whole-assignment posteriors range from **0.551020 to 0.944982** for completed
consistent cases and **0.171681 to 0.391553** for retracted cases.

Concrete examples:

- **2-Methylbutyryl-CoA dehydrogenase deficiency:** confidence changes from
  0.5 to **0.9**, and whole-assignment posterior from 0.177293 to **0.652817**.
  Its chosen mappings are unchanged.
- **TTN-related myopathy, dominant-negative TTNsv:** confidence changes from
  0.5 to **0.7**. Its input gives the MONDO identity hypothesis a 0.7 prior;
  that hypothesis has corrected marginal posterior **0.678387**. The other
  0.7-confidence input is pentanucleotide-repeat familial adult myoclonus epilepsy.
- **ADan amyloidosis:** confidence remains **0.5**, while whole-assignment
  posterior rises from 0.095971 to **0.353377**. MONDO asserts identity with
  two ICD-11 Foundation concepts, *Familial dementia, Danish type*
  (`icd11f:2086401830`) and *ADan amyloidosis* (`icd11f:54507082`). Their
  competing identity hypotheses both have prior 0.95 and marginal posterior
  **0.487179**. The chosen assignment rejects the first and accepts the second;
  reversing that choice is equally probable. The solver has no preference
  between those alternatives under these inputs.

The same **33 high-prior mappings in 32 diseases** are retracted as before:
DOID 12, ORDO 9, MESH 8, and ICD-11 Foundation 4. Every rejected hypothesis has
marginal probability of being true **0.487179**. A retraction therefore identifies
a conflict requiring review; it does not establish that the selected source
mapping is wrong. No ICD-10 hypothesis was rejected in a completed result.

## Incomplete and unrefreshed results

Five previously consistent searches now reached the 60-second limit:

- Beta thalassemia
- Bloom syndrome
- Canavan disease
- Cerebrotendinous xanthomatosis
- Osteopetrosis

Their returned assignments match the baseline, but their probabilities and
consistency verdicts are provisional. They are excluded from the completed
confidence distribution above. Fixed time budgets are sensitive to runtime and
machine load; this comparison does not isolate the reason for those timeouts.

The **321 original timeout inputs and 194 older analyses** were not rerun.
Their folders remain unchanged. The combined index therefore now has 326
timeouts; older clique-limited results should not be pooled with these full
joint searches. The upstream fix corrects probability accounting but does not
eliminate repeated traversal work, so the timeout cohort still needs a separate
search pass.

## Artifacts and reproduction

- [baseline.json](baseline.json): previous metrics and chosen truth assignments,
  captured at the recorded dismech commit before the refresh.
- [manifest.json](manifest.json): solver commit, source-ledger hash, selected
  input hashes, timeout, and worker count.
- [attempts.tsv](attempts.tsv): every attempt and its completion status.
- [confidence.tsv](confidence.tsv): before/after comparison for each input;
  timeout rows are explicitly marked.
- [mapping-posteriors.tsv](mapping-posteriors.tsv): labeled hypotheses, priors,
  chosen truth values, and marginal probabilities of being true.
- [retractions.tsv](retractions.tsv): rejected high-prior mappings from completed searches.
- [summary.json](summary.json): distributions separated by completion status.

The run used Python 3.12.9, NetworkX 3.6.1, Pydantic 2.13.4, and PyYAML 6.0.3,
matching the original batch environment. Eight workers each received 60 seconds
plus a 15-second supervisor allowance, with `PYTHONHASHSEED=0`. Every search
used the whole input, no hypothesis-dropping clique limit, no candidate-count
cap, and the maximum signed 64-bit iteration limit. The merged fix deduplicates
complete satisfiable assignments for probability calculations; raw traversal
counts still govern search effort and candidate caps when enabled.

Use a clean checkout at the pinned solver commit:

```bash
cd analyses
BOOMER_SRC=/path/to/clean/boomer-py/src just boomer-refresh-completed
just boomer-confidence
```

The named run selects historical completed statuses from the original ledger,
checks input hashes, preserves that ledger, and checkpoints each attempt.
Repeating the command resumes interrupted work and skips installed results;
changing solver, cohort, or search settings requires a new run name.
See [solver setup](../../patches/README.md). Boomer remains an external analysis
checkout, with no dismech runtime dependency.

Verification checks every refreshed solution against Boomer's model, matches
ledger/index/metadata statuses and input hashes, confirms full-input settings,
and checks that all input files and all files outside this cohort are unchanged.
All 23 targeted analysis/regression tests passed. Repeating the named rerun
and regenerating the confidence reports changed no bytes.
