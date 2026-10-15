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
   `pathophysiology` node in the entry's pathograph, or `null` when no causal
   edge reaches the phenotype. The pathograph file is looked up in
   `pathographs/index.json` by the entry's `name`: when several entries share a
   MONDO id, `pathograph_export` writes `MONDO_<id>.json` for the first and
   `MONDO_<id>__<slug>.json` for the rest, so a lookup by MONDO id alone would
   hand one entry another's graph.

   Only `relationship_type: CAUSATIVE` genes from `genetic[]` are recorded, one
   per (gene, subtype), with the curated `case_fractions` share where present.
   About half the KB's `genetic[]` rows set no `relationship_type`, so an entry
   with no CAUSATIVE row falls back to its untyped rows, which keep
   `relationship_type: null`. Rows typed as modifier, susceptibility, risk
   factor, somatic driver and so on, and genes named on mechanism nodes, are
   never treated as diagnoses. Each phenotype and gene carries its curated `subtype`, if any.

   ```bash
   uv run python -m dismech.export.synthvae_export
   # -> output/synthvae/disease_priors.json   (3,396 diseases, ~44k phenotypes)
   ```

   Each record:
   ```json
   {
     "disease_id": "MONDO:0011581",
     "disease_name": "arrhythmogenic cardiomyopathy with wooly hair and keratoderma",
     "dismech_name": "Carvajal Syndrome",
     "subtypes": [],
     "genes": [{"id": "hgnc:3052", "label": "DSP", "relationship_type": null,
                "subtype": null, "case_fraction": null}],
     "pathograph": "MONDO_0011581.json",
     "phenotypes": [
       {"hpo_id": "HP:0001644", "label": "Dilated cardiomyopathy",
        "probability": 0.9, "frequency_source": "band",
        "branch": "Contractile and Electrical Dysfunction", "subtype": null},
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

   Each patient is first given one causal gene (weighted by `case_fractions`
   when every candidate gene has one, uniformly otherwise) and, for an entry
   with subtypes, one subtype: the gene's own subtype when it has one, otherwise
   a uniform draw, since dismech records no subtype frequencies. Phenotypes
   scoped to any other subtype are not drawn, so a patient never mixes the
   features of mutually exclusive subtypes. The gene is written as a single
   phenopacket v2 `GeneDescriptor` (`valueId: HGNC:<n>`, `symbol`) with
   `interpretationStatus: CAUSATIVE`; the subtype is recorded in
   `metaData.externalReferences`.

## Why the branch matters (curated co-occurrence)

`--mode marginal` draws each phenotype independently. `--mode branch` (default)
draws one shared `u ~ Uniform(0,1)` **per mechanistic branch**; a phenotype is
present iff `u < probability`. This preserves each phenotype's marginal while
inducing positive *within-branch* co-occurrence — exactly the structure the VAE
otherwise has to estimate from data. Two conditions apply:

* **Subtypes.** A subtype-scoped phenotype keeps its curated marginal *within*
  its subtype; across the whole cohort it is diluted by the share of patients
  drawn into other subtypes. Unscoped phenotypes are unaffected.
* **`--min-features`.** It defaults to 0. Any higher value redraws patients with
  too few features, which conditions every kept patient and pushes the marginals
  up, most for diseases whose phenotypes are all low-frequency (the rare and
  cold-start diseases this sampler is for). The sampler prints a note when it is
  set.

Measured on Carvajal (N=4000, no subtypes, `--min-features 0`), for two
same-branch cardiac phenotypes each with P≈0.17:

| mode | P(VT) | P(SCD) | P(both) | independent expectation |
|------|-------|--------|---------|--------------------------|
| marginal | 0.164 | 0.166 | 0.028 | 0.027 |
| branch | 0.163 | 0.163 | **0.163** | 0.027 |

In branch mode the rarer cardiac signs (ventricular tachycardia, syncope, sudden
cardiac death) co-segregate when the cardiac branch is "severe", instead of
scattering independently — biologically faithful co-occurrence for free.

## Three ways the VAE project can use this

1. **Standalone sampler** for cold-start / rare diseases (no real cases to train on).
2. **Structured prior** to regularize the VAE where case data are sparse.
3. **Plausibility check**: score VAE output by pathograph-branch coherence — see
   the QC layer below.

## QC layer (non-invasive plausibility check)

`scripts/synthvae_qc.py` implements Milestone 1 of
[synthetic_vae_generator#4](https://github.com/justaddcoffee/synthetic_vae_generator/issues/4):
score any phenopacket cohort (VAE output, the sampler above, or real
phenopacket-store cases) against the pathograph **without touching model
training**. It reports, per patient and per cohort:

* the matched disease entry (by MONDO id, else by causal gene). A MONDO id
  shared by several entries is resolved only through the pathograph file the
  patient names (as the sampler's output does) and is otherwise reported as
  `mondo_ambiguous` rather than guessed;
* each HPO term as **on-graph** (a causal edge in the pathograph reaches it, so
  a curated mechanism explains it), **listed, unconnected** (curated for the
  disease but no causal edge reaches it — about half the KB's phenotypes; see
  `just compliance-connectivity`), or **off-graph** (not curated for the
  disease at all — the plausibility red flag). `coverage` counts on-graph terms
  only; `listed_coverage` counts both of the first two;
* which mechanistic **branches** the on-graph terms activate.

```bash
uv run python scripts/synthvae_qc.py output/synthvae/synthetic_patients.jsonl
# -> output/synthvae/qc_report.json + a printed summary
```

This is *disease-mechanism* plausibility, complementary to HPO ontology logical
checks: ontology checks catch impossible term combinations; this catches
phenotype sets that don't hang together on the curated causal graph. Exact-term
matching today; HPO ancestor/descendant expansion (via OAK, as in
`scripts/pathograph_overlap.py`) is the natural refinement.

All outputs land under the gitignored `output/synthvae/`.
