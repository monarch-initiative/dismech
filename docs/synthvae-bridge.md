# Pathograph → synthetic patients (the synthvae bridge)

This is the bridge between the dismech **pathograph** and the synthetic-patient
**VAE generator** ([justaddcoffee/synthetic_vae_generator](https://github.com/justaddcoffee/synthetic_vae_generator)),
which trains a conditional VAE on real phenopackets to learn HPO-symptom
co-occurrence and sample novel synthetic patients for benchmarking (e.g.
Exomiser reranking).

The two artifacts share a join key (**HP terms**) and a disease key (**MONDO**),
so a curated dismech disorder can be projected into the exact shape the VAE world
consumes — but grounded in curated biology rather than learned from sparse cases.

## Two pieces

1. **Extractor** — `src/dismech/export/synthvae_export.py`
   Projects every MONDO-anchored disorder to a per-disease *generative prior*:
   numeric phenotype probabilities plus the causal-branch each phenotype hangs
   off. Reuses the frequency parsing in `hpoa_export` (literal `12%` / `3/20`,
   an HP Frequency term, or the dismech `FrequencyEnum`) and maps HP Frequency
   bands to midpoint probabilities. The branch is the nearest upstream
   `pathophysiology` node in the disease's `pathographs/MONDO_*.json`.

   ```bash
   uv run python -m dismech.export.synthvae_export
   # -> output/synthvae/disease_priors.json   (1,426 diseases, ~15k phenotypes)
   ```

   Each record:
   ```json
   {
     "disease_id": "MONDO:0011581",
     "disease_name": "arrhythmogenic cardiomyopathy with wooly hair and keratoderma",
     "genes": [{"id": "hgnc:3052", "label": "DSP"}],
     "pathograph": "MONDO_0011581.json",
     "phenotypes": [
       {"hpo_id": "HP:0001644", "label": "Dilated cardiomyopathy",
        "probability": 0.9, "frequency_source": "band",
        "branch": "Contractile and Electrical Dysfunction"},
       ...
     ],
     "excluded": []
   }
   ```

2. **Sampler** — `scripts/synthvae_sampler.py`
   A white-box knowledge-based sampler that turns priors into phenopacket-v2-style
   synthetic patients. The counterpart to the learned VAE: it works for rare /
   cold-start diseases with no real cases, and can act as a structured prior or a
   plausibility baseline next to the VAE.

   ```bash
   uv run python scripts/synthvae_sampler.py --disease MONDO:0011581 -n 5 --mode branch
   # -> output/synthvae/synthetic_patients.jsonl
   ```

## Why the branch matters (curated co-occurrence)

`--mode marginal` draws each phenotype independently. `--mode branch` (default)
draws one shared `u ~ Uniform(0,1)` **per mechanistic branch**; a phenotype is
present iff `u < probability`. This **preserves every marginal exactly** while
inducing positive *within-branch* co-occurrence — exactly the structure the VAE
otherwise has to estimate from data. Measured on Carvajal (N=4000), for two
same-branch cardiac phenotypes each with P≈0.17:

| mode | P(VT) | P(SCD) | P(both) | independent expectation |
|------|-------|--------|---------|--------------------------|
| marginal | 0.170 | 0.172 | 0.035 | 0.029 |
| branch | 0.162 | 0.162 | **0.162** | 0.026 |

In branch mode the rarer cardiac signs (ventricular tachycardia, syncope, sudden
cardiac death) co-segregate when the cardiac branch is "severe", instead of
scattering independently — biologically faithful co-occurrence for free.

## Three ways the VAE project can use this

1. **Standalone sampler** for cold-start / rare diseases (no real cases to train on).
2. **Structured prior** to regularize the VAE where case data are sparse.
3. **Plausibility check**: score VAE output by pathograph-branch coherence
   (reusing the IDF/overlap machinery in `scripts/pathograph_overlap.py`).

Both outputs land under the gitignored `output/synthvae/`.
