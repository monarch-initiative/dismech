# Boomer batch: new and changed Mendelian inputs

The 2026-09-08 batch targets **1,534 saved inputs**: 1,357 `NOT_RUN` entries
from the Mendelian expansion and 177 `STALE_INPUT` entries changed by ICD
enrichment. The other 194 previously completed analyses are outside this run.

**All 1,534 attempts finished.** There were no worker errors or supervisor kills.

| Input cohort | Consistent | Retracted | Timed out | Total |
|---|---:|---:|---:|---:|
| New Mendelian inputs | 1,181 | 32 | 144 | 1,357 |
| Inputs changed by ICD enrichment | 0 | 0 | 177 | 177 |
| Total | 1,181 | 32 | 321 | 1,534 |

The completed searches cover **1,213 of the 1,357 new inputs (89.4%)**. All
177 changed subtype inputs exceeded the time budget, so their former completed
verdicts have been replaced by explicitly partial current results. Of the 321
timeouts, 320 returned a satisfiable candidate; the 156-hypothesis
`Autosomal_Recessive_Primary_Microcephaly` input returned none before timeout.

[retractions.tsv](retractions.tsv) lists the **33 rejected high-prior claims in
32 completed runs**, with labels. These are MONDO identity mappings to DOID (12),
ORDO (9), MESH (8), and ICD-11 Foundation (4). No ICD-10 mapping was rejected in
a completed run. This does not establish consistency for the timed-out inputs.

[attempts.tsv](attempts.tsv) records the latest attempt for each targeted entry.
Each disorder folder has a `solve.json` recording the input SHA-256, solver Git
commit, search configuration, status, runtime, and whether new solution files
were produced. `solution.yaml` and `solution.md` contain the current solver
output when available; the folder README states whether it is complete or partial.

## Search settings

Eight local worker processes each receive a **60-second search budget**, with
an additional supervisor deadline at 75 seconds for startup, rendering, or
an unresponsive search step. All workers use `PYTHONHASHSEED=0` and the same
clean Boomer checkout, identified by `boomer_commit` in `solve.json`.

This run used Boomer `16769dc84375af522357fc7b67077ee862bbc8e8`, Python 3.12.9,
NetworkX 3.6.1, Pydantic 2.13.4, and PyYAML 6.0.3. A detached clean checkout
was used because the working Boomer checkout contained unrelated local changes.

Each worker runs the **entire saved KB**. Partitioning is disabled by setting
its threshold to the input's hypothesis count; `max_pfacts_per_clique` is
`null`, so no hypotheses are dropped. The candidate-count cap is disabled and
the iteration cap is set to the maximum signed 64-bit integer. The time budget
is the practical stopping condition. This differs from the original 371-entry
run's clique-limited settings, so its results should not be pooled as if they
came from the same search protocol.

## Status meanings

| Status | Meaning |
|---|---|
| `ALL_MAPPINGS_CONSISTENT` | Search completed with a satisfiable assignment accepting all hypotheses whose prior is at least 0.5. |
| `RETRACTED` | Search completed and rejected one or more hypotheses whose prior is at least 0.5. This identifies competing assertions, not which source is wrong. |
| `TIMED_OUT` | Boomer returned before the supervisor deadline but reported that its search budget expired. Any assignment and posterior are provisional. |
| `TIMED_OUT_NO_RESULT` | The supervisor stopped the worker without receiving a serializable result. Any pre-existing solution files remain historical. |
| `NO_SATISFIABLE_SOLUTION` | Boomer returned no satisfiable assignment; no mapping verdict is asserted. |
| `ERROR` / `INPUT_CHANGED` | The attempt failed or the input changed during the attempt. No completed verdict is asserted. |

`n_retracted` is `NA` for incomplete attempts. `candidate_retractions` records
rejections in a returned provisional candidate separately. Both identity and
directional mapping hypotheses count; low-prior alternatives do not.

## Resume and reproduce

```bash
cd analyses
BOOMER_SRC=/path/to/clean/boomer-py/src just boomer-solve-pending 60 8
```

The runner requires a clean solver checkout so its Git commit identifies the
implementation used. It updates the main index and run ledger after each
completed attempt. Rerunning resumes `NOT_RUN` and `STALE_INPUT` entries;
it does not automatically retry timeouts or rerun completed analyses.

Input YAMLs are never regenerated. If an input changes while its worker runs,
the worker's output is not installed. If the index changes outside the runner,
the runner refuses to overwrite it. Failed workers do not overwrite previous
solution files. Output files are installed before the corresponding index
status is checkpointed.

Search timeouts depend on machine load. A fixed hash seed and rounded solver
floats limit incidental output differences, but a timed search is not guaranteed
to return byte-identical results. Runtime measurements in `solve.json` and the
ledger describe this run rather than a stable property of the input.

Final verification validated every returned solution against Boomer's model,
matched all attempt hashes and statuses, confirmed all 1,728 input YAMLs stayed
byte-identical, and confirmed the 776 files in the 194 previously completed
analysis folders stayed unchanged.
