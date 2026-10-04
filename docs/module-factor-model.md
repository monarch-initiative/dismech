# Anchored module-factor model

The keystone the [mechanism-module map](module-map.md) and its phenotype anchors
were scaffolding for: a model that treats each curated mechanism module as a
**latent factor** over diseases and scores every disease's *soft loading* on
every module from the disease's own phenotype profile. It is the
mechanism-as-hidden-variable idea (the annotated-factor family —
f-scLVM / expiMap in single-cell genomics) applied to the pathograph, with the
curated module → phenotype signatures as the factor anchors.

```bash
uv run python scripts/module_factor_model.py
# -> output/module_map/module_factor_model.json  (summary)
#    output/module_map/module_factor_loadings.tsv
#    output/module_map/conformance_candidates.tsv
```

This is the **inference half** of the factor model: fixed, curated anchors now.
Learned de-novo factors for the residual structure the anchors don't explain
(the candidate *new* modules) are the next step and are deliberately not built
yet.

## What it computes

For each disease, an idf-weighted cosine between its phenotype vector (frequency
as the weight) and each module's phenotype signature (support-damped,
specificity-weighted — the same intuition as `scripts/pathograph_overlap.py`).
That score is the disease's continuous loading on the module — the soft,
graded version of the binary `conforms_to` edge.

Two outputs come from it, and both are careful about circularity.

### 1. Recovery of curated conformance (leave-one-out)

For each disease that declares `conforms_to` module *m*, how highly does *m* rank
among its module loadings? Scored **leave-one-out** — the module's signature is
recomputed with that disease's own phenotype contribution removed — so a
conformer cannot rank highly on a module just because it helped build that
module's signature.

On the current KB (105 modules with phenotype signatures, 521 conformers
scoreable):

| metric | model | random baseline |
|---|---|---|
| MRR | **0.75** | — |
| recall@1 | **0.64** | 0.010 |
| recall@3 | **0.83** | 0.029 |
| recall@5 | **0.91** | 0.048 |

The curated module is the single top-ranked factor ~64% of the time and in the
top five ~91% of the time — roughly 19× the random baseline. The soft loadings
track the curated mechanism graph, which is the evidence that the anchored factor
model is doing something real rather than fitting noise. (Figures move with the
KB; run it for current numbers.)

### 2. Candidate conformances (the actionable output)

A disease whose phenotype profile matches a module it does **not** declare is a
curation lead: *"this disease looks like it conforms to `<module>`, but the entry
doesn't say so."* A non-conformer never contributed to the module's signature, so
this half is not circular. It is the phenotype-signature complement to the
node-embedding `conforms_to_suggestions` idea.

The ranked head is a genuine mix of real leads and coincidental overlap, which is
exactly why it is a **worklist, not an autofill**:

- strong, obviously-correct leads — Membranous nephropathy and Minimal Change
  Disease → `nephrotic_podocyte_injury` (shared 5), mitochondrial Parkinson
  disease → `parkinsonism_dopaminergic_degeneration`, Anophthalmia-Microphthalmia
  → `ocular_morphogenesis_failure` (shared 9);
- coincidental phenotype overlap — Lyme disease → `gout_urate_crystal_inflammation`
  (shared 2), where a couple of shared arthritis phenotypes produce a high cosine
  with no mechanistic truth behind it.

So read the candidates by **score together with shared-phenotype count**, and
confirm each against the mechanism before adding a `conforms_to` edge — the same
"tooling proposes, curator adjudicates" discipline the rest of dismech uses. The
raw candidate set is large (tens of thousands with any nonzero overlap); the
useful worklist is the high-score, higher-shared tail of `conformance_candidates.tsv`.

## Where this sits

Together with the module map and phenotype anchors this closes the loop the
digital-twin roadmap opened: curated module → CL/GO signature, module →
phenotype signature, disease ↔ module incidence, and now a continuous
disease × module loading that both validates the curation and extends it. The
loading vector is the interpretable, mechanism-grounded latent the VAE's opaque
`z` was missing — computed here by anchored inference rather than learned, with
the learned de-novo extension noted above.

Outputs land under the gitignored `output/module_map/`.
