# Models

One folder per model, named by its `model_id`, which is also the `model_id` a
`computational_models` record in `kb/` uses to point at it. The files inside
carry fixed names, so nothing that consumes a model has to know its id twice.
`src/dismech/model_registry.py` is the only place that resolves these paths;
`tests/test_model_registry.py` keeps the tree in this shape.

| File | Meaning |
|---|---|
| `config.yaml` | dismech-perturb sidecar: the model is **runnable in-repo** (SBML through tellurium). `sbml_file` and `extension_file` resolve relative to the folder. |
| `model.xml` | the SBML the config points at |
| `model.ant` | its Antimony source, where the model was authored here (`model.xml` is the artifact that is loaded) |
| `extension.ant` | an Antimony extension co-simulated with the base model |
| `spec.yaml` | a **repository-authored** model with its own runner (a Boolean network, an agent-based model): the rule specification, with per-rule provenance into `kb/` |
| `run.py` | that model's runner; `--check` fails when `results.json` is stale, `--print` summarises |
| `results.json` | the runner's committed, deterministic output |

A folder holds exactly one of `config.yaml` or `spec.yaml`.

```bash
just gen-model-results            # run every config.yaml scenario -> exports/model_runs/ (needs tellurium)
just sedml-export                 # every config.yaml -> exports/sedml/<model_id>/
just check-authored-models        # every spec.yaml's run.py --check
uv run python models/<id>/run.py  # regenerate one authored model's results
```

The two kinds are deliberately different. A `config.yaml` model is a published
or curated SBML model plus a mapping of gene perturbations and scenarios onto
its parameters; its results are derived by a shared runner into
`exports/model_runs/` and the disorder page renders them. A `spec.yaml` model
is authored in this repository as an executable transcription of a curated
causal chain: every rule names the node or edge it encodes, nothing is fitted
to data, and its runner and results live beside the spec. See
`docs/explanation/computational-models.md`.
