---
analysis_contract: required
---

# Hypothesis Test by Simulation of a Published Model

You are testing a mechanistic hypothesis for the Disorder Mechanisms Knowledge
Base by running a published computational model. This is not a literature-review
task. The run succeeds only if you install the model's simulator, execute
simulations, classify their outcomes, and save enough artifacts for an
independent replay of the classification.

## Target

- Disease: {disease_name}
- Hypothesis ID: {hypothesis_group_id}
- Hypothesis label: {hypothesis_label}

The hypothesis as curated:

```yaml
{hypothesis_yaml}
```

## Model

- Model inputs:

{dataset_inputs}

- Settings to perturb:

{target_variables}

## Analysis objective

{analysis_objective}

## Runtime contract

Use the code execution facility immediately. You may install the simulator the
model requires (for example with `pip` or `conda`/`micromamba`) and any
standard scientific Python package. Record every install command and the exact
resolved versions. Do not reimplement, approximate, or simplify the model: run
the deposited model files. If the simulator cannot be installed or the control
simulation does not run, write `MANIFEST.yaml` with `status: FAILED`, the failed
step and the error, then stop. Do not answer from memory, switch to literature
synthesis, invent results, or present proposed code as executed.

Budget. Single simulations are long. Run replicates in parallel across all
available cores, and shorten nothing that changes the model's dynamics. Run the
control condition first. Choose the number of replicates per condition from the
measured wall-clock time of the first control run so that every condition gets
the same number of replicates and the whole job finishes inside the time
available. State the replicate count and why in `methods.md`. Fewer replicates
than the original publication is acceptable and must be reported as a
limitation; unequal replicate counts between conditions are not acceptable.

Write every generated file beneath this exact directory:

`{artifact_dir}`

Raw simulation output goes in `{artifact_dir}/raw/`. It is recoverable by
re-running and will not be committed.

If the run succeeds, the artifact directory must contain:

- `MANIFEST.yaml`: `schema_version: '1.0'`, `provider: openscientist`,
  `status: SUCCEEDED`, `fallback_used: false`,
  `direct_analysis_completed: true`, UTC start/end times, every input
  (model archive, analysis scripts) with its canonical URL, retrieval time,
  byte count and SHA-256, all output paths with role, byte count and SHA-256,
  the exact comparison, and limitations. Store each `sha256` as exactly 64
  lowercase hexadecimal characters. The outputs must include distinct `CODE`,
  `ENVIRONMENT` and `TABULAR_RESULT` roles; other useful roles are `METHODS`,
  `SUMMARY`, `FIGURE`.
- `simulate.py`: the driver that sets each condition's parameters on the
  deposited model and launches its replicates, writing to `raw/`.
- `analysis.py`: standalone deterministic classification and aggregation over
  the saved simulation output, accepting `--output-dir` and `--cache-dir`
  (the `raw/` directory). It must regenerate every tabular result without an
  LLM and without re-running simulations.
- `environment.txt`: OS, Python version, simulator version and exact versions
  of every third-party package.
- `methods.md`: conditions and their exact parameter values, replicate count
  and its justification, random seeds if the simulator exposes them, simulation
  length, the outcome classification rule, and statistical tests.
- `runs.csv`: one row per simulation with condition, replicate, seed, runtime,
  and classified outcome.
- `condition_results.csv`: one row per condition with replicate count, count
  and proportion of each outcome class, the proportion of any defect, and the
  test against control (two-sided Fisher exact test) with its p-value.
- `comparison.md`: the computed results, clearly separating what the
  simulations show from biological inference about the disease.
- At least one figure: a final-state frame for one control run and one run of
  each perturbed condition.

Classify outcomes with the model authors' own scheme and, where they provide
it, their own analysis code. Validate your classifier on the control condition
before applying it: report how many control runs it calls normal.

Before declaring success, execute `analysis.py` once more into a clean `replay/`
subdirectory with `--cache-dir {artifact_dir}/raw`. Verify the replayed
`runs.csv` and `condition_results.csv` are byte-identical to the primary
outputs. Under `replay` in the manifest, record the exact nonempty `command`,
`verified: true`, a `byte_identity` mapping naming every `TABULAR_RESULT`
primary path with value `true`, and an `assets` list giving each replay file's
path beneath `replay/`, role, positive `byte_count` and lowercase SHA-256.

## Final response contract

Finish and close `MANIFEST.yaml` before emitting a success marker. Do not add
an `artifact_manifest_sha256` field yourself; the runner adds it.

The first line must be exactly one of:

`ANALYSIS_STATUS: SUCCEEDED`

`ANALYSIS_STATUS: FAILED`

Use `SUCCEEDED` only after all required artifacts exist and the clean replay
matches. Then summarize the results per condition and point to the artifacts.
On failure, name the failed step and error only; do not provide a fallback
scientific verdict.
