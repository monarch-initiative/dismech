---
name: model-curation
description: >-
  Curate or review animal, experimental, and computational model records in
  dismech, including modeled_mechanisms, fidelity, divergences, biological scale,
  readouts, and failed recapitulation. Use for model-to-human relevance and
  model-system phenotype evidence. Not for executing a model or assessing an
  external provider's computational research run.
---

# Curate Models and Their Mechanism Links

Dismech records what a model establishes about a disease mechanism, including
partial or failed recapitulation. A model's existence is not proof of fidelity.

Read [mechanism links](references/mechanism-links.md) before adding or reviewing
`modeled_mechanisms`. It owns the schema patterns and worked examples for:

- `animal_models` for whole organisms; `experimental_models` for non-animal
  systems such as cells, organoids, and organ chips; `computational_models` for
  computational representations;
- the link's `relationship`, `fidelity`, `limitations`, and `divergences`;
- `model_scale` as the scale actually observed, versus the target node's scale;
- link evidence versus evidence for each measured `readout`;
- negative results and `FAILS_TO_RECAPITULATE`.

Use `dismech-references` to distinguish human, animal, in-vitro, and computational
evidence. Use `pathograph` for the target mechanism and entity-reference grammar,
and `dismech-terms` for bindings. Read [model credibility](../../../docs/explanation/model-credibility.md)
for the interpretation of model-to-mechanism claims.

## Questions to settle for each link

1. What does the model actually perturb, measure, rescue, or reproduce?
2. What is the evidence for that relationship to this target, independently of
   evidence that the model exists?
3. What quantity and biological scale were observed? An inferred tissue outcome
   from molecular state is upward extrapolation, even if the output variable
   has the tissue outcome's name.
4. Which boundaries, proxies, calibration sources, populations, or species
   differences qualify or invalidate this particular claim?
5. Which readouts were measured, with what direction and evidence? An unchanged
   measurement is a result; an unmeasured quantity has no direction to record.

Record a `HUMAN_MODEL_MISMATCH` discussion when evidence exists in a model but
its fidelity to the human mechanism is the open question. Use `KNOWLEDGE_GAP`
for absent evidence. Do not silently promote a model result into a human phenotype.

For MorPhiC-derived records, also read
[cellular phenotypes](references/cellular-phenotypes.md). Verify that the
perturbation and system are disease-relevant before adding the phenotype or dataset.

Run normal schema, term, and evidence validation, graph-reference checks when
targets change, and `just model-scale-audit --strict` when assessing scale links.
Respect the evidence and limitation requirements on failed recapitulation and
upward extrapolation described in the detailed guide.

Assessment of a provider's actual data access, execution artifacts, replay, or
cross-provider agreement belongs to `review-hypothesis-exploration` instead.
