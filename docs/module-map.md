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
factorization exists to avoid. That attribution is done separately, over the
pathograph, by `dismech.export.module_phenotype_anchors` (below).

## Module → phenotype anchors (branch attribution)

`module_phenotype_anchors` completes the anchor matrix by walking **downstream**
from each conforming pathophysiology node, through the disease's own pathograph
(`pathographs/MONDO_*.json`), to the phenotype nodes that branch actually
reaches — and crediting those HPO phenotypes to the module. Aggregated across
every conformer, the result is the module's *clinical* signature.

```bash
uv run python -m dismech.export.module_phenotype_anchors
# -> output/module_map/module_phenotype_anchors.json + .tsv
```

The signatures come out biologically sensible with no per-disease research —
`lysosomal_substrate_accumulation` → Seizures / Coarse facial features /
Hepatosplenomegaly; `cardiac_ion_channel_repolarization` → Syncope / Sudden
cardiac death / Ventricular fibrillation; `mps_gag_storage` → Dysostosis
multiplex / Short stature / Coarse facies — because the attribution is by causal
branch, not by disease. Coverage is reported honestly: only about half of
conforming branches reach a phenotype node, matching the KB-wide causal-inlink
figure (a branch that stops at the pathophysiology layer contributes no anchor).

This is the module → phenotype half of the factor-model anchor matrix; the
module → CL/GO signature and disease ↔ module incidence above are the other half.

Outputs land under the gitignored `output/module_map/`.
