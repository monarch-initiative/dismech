# Models, fidelity, scale, and readouts

### Linking Models into the Pathograph (`modeled_mechanisms`)

All three model sections — `experimental_models:` (NAMs: organoids, organ-chips,
cell lines, iPSC-derived and primary cultures), `animal_models:`, and
`computational_models:` — reach the pathograph through the **same** link object,
`ModelMechanismLink`. A model that does not declare `modeled_mechanisms` is a
disconnected list entry: it renders, but no mechanism node knows about it.

**Which section does an animal model go in?** `animal_models:`. Whole-organism
animal models are never `experimental_models:` — that class is for non-animal
systems. Before `AnimalModel` had `modeled_mechanisms`, curators routed animal
models through `ExperimentalModel` with `experimental_model_type: OTHER` to reach
the pathograph; that workaround is no longer needed (#8199).

**The link records several things beyond the target:**

| Slot | What it says |
|---|---|
| `relationship` | what the model *does* to the node — `RECAPITULATES`, `PARTIALLY_RECAPITULATES`, `FAILS_TO_RECAPITULATE`, `PERTURBS`, `MEASURES`, `RESCUES` |
| `fidelity` | how faithfully it captures the human mechanism — `HIGH` / `MODERATE` / `LOW` / `UNKNOWN` |
| `limitations` | the specific translational caveat (species divergence, supraphysiological expression, missing compartments) |
| `model_scale` | the biological scale the model actually **observes** (`BiologicalScaleEnum`) |
| `readouts` | the **outcome measures** that ground the claim |

**`model_scale` is what the model observes, not what it is cited for.** A model
linked to a node is not necessarily operating at that node's scale: a Boolean
signalling network whose output node is named "bone erosion" still observes only
molecular or cellular state, and the tissue-level outcome is inferred. Record the
observed scale in `model_scale`, using the same `BiologicalScaleEnum` as
`Pathophysiology.biological_scale` so the two are directly comparable.

Do **not** record the comparison — derive it with `just model-scale-audit`. The
comparison is directional, and the directions are different claims:

| Relation | Meaning |
|---|---|
| model scale **below** target scale | **Upward extrapolation.** The model cannot observe the outcome it is cited for; the claim is inferential. Requires `limitations` (`check_upward_extrapolating_links_are_caveated`). |
| model scale **above** target scale | The model contains the target scale. Normally unremarkable — a whole animal can report a molecular readout. |
| equal | No scale gap. |

Both slots are optional, so a link with neither is `UNDETERMINED` rather than
defective — that is the state of most existing links. `model_scale` is
**orthogonal to `fidelity` and `relationship`**, not a restatement of them: a
molecular model linked to a molecular node reports no scale gap even when it is
a poor model for some unrelated reason. Read an aligned result as "no *scale*
gap", never as "good model".

Worked examples: the RA-FLS Boolean model (`CELLULAR`) linked to
`Synovial Hyperplasia` (`TISSUE`) is a 1-step upward extrapolation; the type 1
interferon Boolean model (`MOLECULAR`) linked to
`Enhanced Viral Replication and Tissue Pathology` (`TISSUE`) is a 2-step one.

**`divergences` types the caveat that `limitations` writes as prose.** `fidelity`
compresses every translational concern into one tier, so `LOW` never says *which*
problem it is, and a prose `limitations` string cannot answer "which models are limited
by calibration provenance rather than by species". Each entry in `divergences` names a
kind from `ModelDivergenceTypeEnum`, explains in the curator's own words why that kind of
gap applies **here**, and optionally records `materiality` — whether it bears on this
link's claim.

```yaml
  - target: Striatal Dopamine Deficiency
    relationship: PARTIALLY_RECAPITULATES
    fidelity: LOW
    model_scale: MOLECULAR
    divergences:
    - divergence_type: PROXY_QUANTITY
      materiality: INVALIDATING
      description: >-
        The model's quantity is transcriptional regulation of dopamine-synthesis
        genes. The node's quantity is dopamine concentration in the striatum.
    - divergence_type: BOUNDARY_OMISSION
      materiality: QUALIFYING
      description: >-
        Nigrostriatal terminal loss and the presynaptic deficit are not in the model.
```

Background reading: [`docs/explanation/model-credibility.md`](../../../../docs/explanation/model-credibility.md)
explains what a model-to-mechanism link does and does not claim, and how the design maps
onto the ten rules of credible practice in healthcare modeling (PMID:32993675) and the
ASME V&V 40 / FDA credibility frameworks. The taxonomy itself was fixed by reading all 50
computational-model `limitations` strings in the KB and clustering them — see
[`docs/superpowers/specs/2026-09-02-model-divergence-taxonomy.md`](../../../../docs/superpowers/specs/2026-09-02-model-divergence-taxonomy.md).
Rules for using it:

- **Multivalued on purpose.** A real caveat is usually several kinds at once; do not pick
  the single "best" one.
- **The type is never the argument.** `description` is required and must say *which*
  component is outside the boundary, *which* quantity stands in for *which*. A description
  that restates the enum value fails `check_model_divergences_are_typed_and_explained`.
- **`PROXY_QUANTITY` vs `BOUNDARY_OMISSION`** is the distinction to get right. In a
  boundary omission the thing is not in the model; in a proxy divergence it *is*, but as a
  stand-in of a different quantity. Both can occur at the same scale, so neither follows
  from `model_scale`.
- **`materiality` is per-divergence**, where `fidelity` is per-link. `IMMATERIAL` is worth
  recording — it stops a reader inferring that a known limitation of the model undermines
  *this* use of it.
- **A `SCALE_EXTRAPOLATION` divergence must agree with the scale slots**
  (`check_scale_extrapolation_divergence_agrees_with_scales`, and
  `just model-scale-audit --strict`).
- `divergences` and `limitations` coexist: the prose slot is the summary and holds the 831
  existing links' caveats. A typed divergence now satisfies the caveat requirement on a
  `FAILS_TO_RECAPITULATE` or upward-extrapolating link wherever `limitations` did.

Currently populated on computational models only. The taxonomy was chosen to extend to
NAM and animal models unchanged — `BOUNDARY_OMISSION`, `PROXY_QUANTITY`,
`CALIBRATION_PROVENANCE`, `POPULATION_MISMATCH` and `SPECIES_MISMATCH` all apply — and
extending it would likely add `SUPRAPHYSIOLOGICAL_EXPRESSION` and `INCOMPLETE_PHENOTYPE`,
both already evidenced in the animal set.

```yaml
animal_models:
- name: Canine degenerative myelopathy (SOD1 E40K homozygous dog)
  species: Dog
  genotype: SOD1 c.118G>A (p.E40K) homozygous
  publication: PMID:19188595
  modeled_mechanisms:
  - target: Motor Neuron Degeneration
    relationship: RECAPITULATES
    fidelity: MODERATE
    description: Naturally occurring, adult-onset SOD1-associated spinal cord degeneration.
    limitations: >-
      E40K is not among the SOD1 alleles that cause human ALS, and DM presents as
      an ascending spinal myelopathy rather than focal limb or bulbar onset.
    readouts:
    - name: Lateral white matter myelin and axon content
      target: Motor Neuron Degeneration     # required; must repeat the link's target
      direction: DECREASED
      interpretation: Structural correlate of the degeneration node in this model.
      evidence:
      - reference: PMID:19188595
        supports: SUPPORT
        evidence_source: MODEL_ORGANISM
        snippet: "exact quote from the abstract"
        explanation: Reports the histological measurement behind this readout.
    evidence:                                # separate claim — see below
    - reference: PMID:19188595
      supports: SUPPORT
      evidence_source: MODEL_ORGANISM
      snippet: "exact quote from the abstract"
      explanation: Supports treating this model as informative for the node.
```

**Two evidence layers, and they are different claims.** Evidence on the **link**
attests *"this model is informative for this node."* Evidence on each **readout**
attests *"this specific measurement was made, in this direction."* Do not collapse
them — a model can be well-established for a node while one of its readouts is a
single uncontrolled observation. Both are `recommended`, not required, so
incremental curation of an existing model entry is not blocked.

**Readouts live on the link, not on the model**, because one model typically
measures different things for different nodes (a liver-chip reports albumin for a
hepatocyte-death node and TMRM for a mitochondrial node). `readouts` reuses the
same `ExperimentalReadout` class as `Experiment.readouts`, so a *proposed*
experiment and a *realized* model are directly comparable — and a readout can be
grounded to an HP phenotype, a biomarker, a GO process, or an OBI assay.

- `direction` accepts the model values (`INCREASED`, `DECREASED`, `UNCHANGED`,
  `RESTORED`, `ABOLISHED`, `ALTERED`) as well as the older association-style
  `BiomarkerReadoutDirectionEnum` values. Prefer the model values for a
  measurement made in a model system. `UNCHANGED` is a real negative result —
  omit `direction` entirely when the measurement was simply not made.
- A readout's `target` is **required** and must repeat the link's `target`
  (`check_model_readout_targets_match_link` enforces this). The redundancy keeps
  a readout self-describing so it can be lifted out of its link. Note this is
  forward-looking: today only `biochemical.readouts` and
  `investigations.reports_on` are lifted into the graph and cx2, and
  `kgx_export.py` has no model handling at all — model-link readouts render in
  the HTML card but are not yet exported independently.
- **OBI assay grounding is under-supported today.** `OBI` is not in
  `conf/oak_config.yaml` and has no `cache/enums/` membership cache, so `assays:`
  terms cannot be validated the way HP/GO/CL terms are. Prefer
  `biological_processes` (GO) until that gap is closed.

**Negative results are first-class.** `FAILS_TO_RECAPITULATE` says a model does
*not* reproduce the human mechanism — the structural signal behind a
`HUMAN_MODEL_MISMATCH` discussion, which previously survived only as prose in
`description` or `notes`. Because it is a substantive negative claim, it requires
both `limitations` and `evidence`
(`check_failure_to_recapitulate_links_are_substantiated`).

**`name` on an animal model** is optional but recommended once the model carries
`modeled_mechanisms`: it is the stable pathograph label and in-page anchor. Absent
it, renderers fall back to `"<genotype> <species>"`, which is not stable across
edits and collides when one file carries two models of the same genotype.

**Worked exemplar:** `Amyotrophic_Lateral_Sclerosis` — the canine SOD1 E40K model
(`RECAPITULATES`, two histology readouts) and the equine motor neuron disease
model, which is `PARTIALLY_RECAPITULATES` against `Motor Neuron Degeneration`
(lower motor neurons only, so it misses the defining combined UMN/LMN degeneration)
while `RECAPITULATES` `Oxidative Stress`, with a `RESTORED` readout for the
vitamin-E rescue arm.
