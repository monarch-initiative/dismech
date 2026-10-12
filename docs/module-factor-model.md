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

This is the **inference half** of the factor model: fixed, curated anchors. The
learned de-novo factors that explain the residual structure the anchors don't —
the candidate *new* modules — are built as a companion step; see
[Learned de-novo factors](#learned-de-novo-factors) below.

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

## Learned de-novo factors

`scripts/module_denovo_factors.py` is the unannotated-factor arm: it **learns**
additional latent factors for the phenotype co-occurrence the curated modules
don't capture, each a candidate for a mechanism module dismech has not yet
curated.

```bash
uv run python scripts/module_denovo_factors.py          # k=20 de-novo factors
# -> output/module_map/module_denovo_factors.{json,tsv}
```

It is a semi-supervised NMF (the f-scLVM / expiMap design): the disease ×
phenotype matrix is factored as `W @ H`, where H's first rows are the curated
module signatures **held fixed** and only the remaining *k* de-novo rows (plus all
of W) are learned. Holding the anchored rows fixed forces each de-novo factor to
explain only residual structure, so it is a new pattern by construction, not a
relabelling of a known module. Each factor is reported by its top phenotypes, the
diseases that load on it, and a **novelty** score (the fraction of its top
phenotypes not in any curated module) so a high-novelty factor stands out from one
that just re-expresses curated mechanisms.

One subtlety that is load-bearing: this model weights phenotype columns by an idf
over the **disease corpus**, not the module-only idf the anchored model uses — a
module-only idf would zero every uncurated phenotype and make discovering a new
cluster impossible.

On the current KB (2164 diseases × 4085 phenotypes, 105 fixed + 20 learned
factors) the top de-novo factors are clinically coherent clusters that are *not*
curated modules — genuine candidate modules:

- **androgen-biosynthesis / disorder of sex development** (novelty 1.0):
  cryptorchidism, ambiguous genitalia, micropenis, urogenital sinus anomaly —
  loaded by 5α-reductase-2 deficiency, 17β-HSD3 deficiency, FGFR1
  hypogonadotropic hypogonadism;
- **humoral immunodeficiency**: recurrent infections + low IgG/IgA — the
  agammaglobulinemias and CVID;
- **bone-marrow-failure / radial-ray**: absent thumb, pancytopenia, radial
  hypoplasia — Fanconi and inherited aplastic anemias;
- **alkaptonuria / ochronosis**: ochronosis, elevated urinary homogentisic acid,
  intervertebral disk calcification.

Same discipline as the candidate-conformance worklist: these are co-occurrence
clusters, not validated mechanisms — many will be organ-system or ascertainment
clusters rather than conserved mechanisms, and the matrix is pathograph-derived so
they inherit curation coverage and bias. A factor is a *lead* for a new module
that a curator reads (top phenotypes + loaded diseases) and adjudicates with the
`create-module` skill. *k* is chosen, not principled.

## Where this sits

Together with the module map and phenotype anchors this closes the loop the
digital-twin roadmap opened: curated module → CL/GO signature, module →
phenotype signature, disease ↔ module incidence, and now a continuous
disease × module loading that both validates the curation and extends it. The
loading vector is the interpretable, mechanism-grounded latent the VAE's opaque
`z` was missing — computed here by anchored inference rather than learned, with
the learned de-novo extension noted above.

Outputs land under the gitignored `output/module_map/`.
