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
| `run.js` | optional browser port of `run.py`, inlined into the model's page so a reader can run it there. It must reproduce `results.json` exactly; a per-model parity test holds it to that (`tests/test_neuronal_migration_abm_js.py` for the agent-based model) |

A folder holds exactly one of `config.yaml` or `spec.yaml`.

```bash
just gen-model-results            # run every config.yaml scenario -> exports/model_runs/ (needs tellurium)
just sedml-export                 # every config.yaml -> exports/sedml/<model_id>/
just check-authored-models        # every spec.yaml's run.py --check
uv run python models/<id>/run.py  # regenerate one authored model's results
just gen-model-pages              # pages/models/<id>.html for every folder (also part of gen-pages)
```

Every folder gets a generated page at `pages/models/<model_id>.html`
(`src/dismech/model_pages.py`): the entries that curate it, its rules with their
provenance, the committed scenarios and sweeps or `exports/model_runs/` run, and
how to run it. The card on the disorder or module page links to it. Like every
page under `pages/`, it is derived and never committed from a hand-authored PR.

**A `run.js` port is a second implementation, so change `run.py` first.** The
port makes the same random draws as CPython (MT19937 seeded from the run name
through SHA-512, as `random.Random(str)` does) and rounds as `round()` does, which
is what lets the page say that a committed scenario replayed in the browser *is*
the committed run. Edit a rule in `run.py`, regenerate `results.json`, then make
the same edit in `run.js`; the parity test fails until the two agree.

The two kinds are deliberately different. A `config.yaml` model is a published
or curated SBML model plus a mapping of gene perturbations and scenarios onto
its parameters; its results are derived by a shared runner into
`exports/model_runs/` and the disorder page renders them. A `spec.yaml` model
is authored in this repository as an executable transcription of a curated
causal chain: every rule names the node or edge it encodes, nothing is fitted
to data, and its runner and results live beside the spec. See
`docs/explanation/computational-models.md`.
