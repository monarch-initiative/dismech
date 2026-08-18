# Mechanism-module map

dismech curates a large cross-disease mechanism layer — ~90+ mechanism modules
(`kb/modules/`) linked to disorders by hundreds of `conforms_to` edges spanning
a large fraction of the KB — but until now it was only ever used as a per-file
consistency check, never assembled into anything queryable. `module_map` builds
that assembled view. (Exact counts grow with the KB; the tool prints current
totals — run it rather than trusting a number here.)

```bash
uv run python -m dismech.export.module_map
# -> output/module_map/module_map.json
#    output/module_map/module_signatures.tsv
#    output/module_map/disease_module_incidence.tsv
```

## What it produces

1. **module → mechanism signature** — the CL / GO / UBERON / gene terms each
   module emits across its pathophysiology nodes. **Modules encode mechanism
   (cell types + biological processes), not phenotypes** — so most modules have
   no intrinsic HP term, by design. The HP phenotype anchors come from the
   *conforming diseases'* nodes, not the module itself.
2. **disease ↔ module incidence** — which disorders conform to which modules, at
   which node, each edge resolved against the module's real node names (MONDO id
   carried through for joins).
3. **an audit** — unused modules, modules with no intrinsic HP term, unresolved
   `conforms_to` targets, the diseases conforming to the most modules (rich
   multimorbidity exemplars, e.g. Hepatocellular Carcinoma), the most-reused
   modules (e.g. `epilepsy_excitation_inhibition_imbalance`,
   `lysosomal_substrate_accumulation`, `fibrotic_response`), and terms shared
   across modules.

## Why this is the anchor scaffold for the module-factor model

The longer-term goal is a model where the **mechanism module is a hidden
variable**: a patient = a mixture of module activations, anchored to these
curated modules (see `docs/digital-twin-roadmap.md` when it lands). This map is
the supervised scaffold that model needs — the module → CL/GO signatures are the
factor anchors, and the disease → module incidence is the observed loading
matrix.

**One deliberate non-step:** module → *phenotype* anchors are **not** built here
by naive aggregation. A disease that conforms to several modules must have its
phenotypes attributed by causal branch (which phenotypes are downstream of the
conforming node), not blanket-assigned to every module it touches — doing
otherwise would reintroduce exactly the mechanism-conflation the module
factorization exists to avoid. That attribution is a downstream construction over
the pathograph and is intentionally left to the next step.

Outputs land under the gitignored `output/module_map/`.
