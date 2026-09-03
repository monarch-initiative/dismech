# Model Credibility: what a model can and cannot support

A dismech entry may cite a model — a computational model, a non-animal method (NAM), an
animal model — and link it to a specific pathophysiology node with `modeled_mechanisms`.
That link is an assertion, and this page is about what the assertion means, how much of it
is checkable, and how the schema records the parts that are not.

The short version: **a model-to-mechanism link is a narrow claim about a specific use, not
a verdict on the model.** dismech records four separable things about it —
*what the model does* (`relationship`), *how faithfully* (`fidelity`), *at what scale it
observes* (`model_scale`), and *in what specific respects it falls short*
(`divergences`) — and derives what it can rather than asking a curator to assert it.

Related pages: [computational models](computational-models.md) for the `dismech-perturb`
runner, [design decisions 3b and 3c](design-decisions.md) for the records of the two
choices described here, and the
[model-divergence taxonomy survey](../superpowers/specs/2026-09-02-model-divergence-taxonomy.md)
for the evidence behind the value set.

---

## 1. The problem

Nearly every curated model link carries a caveat. Across `kb/disorders/` and
`kb/modules/`, **831 of 1,131 model→mechanism links (73%) have a `limitations` string.**
Curators reliably notice and write down what is wrong with a model. What was missing was
any structure over it.

Two consequences followed:

**`fidelity` was overloaded.** `HIGH`/`MODERATE`/`LOW`/`UNKNOWN` absorbs species
divergence, missing compartments, calibration provenance, absent dynamics and scale
extrapolation into a single tier. `LOW` tells a reader that something is wrong, never
*which* thing. And the profile differs sharply by modality — the animal set is dominated
by species divergence and allele mismatch, the computational set by calibration
provenance, absent dynamics and proxy quantities — so the same tier means very different
things in the two cases.

**Prose is not queryable.** "Which of our models are limited by calibration provenance
rather than by species?" is a reasonable question to ask of a knowledge base and was
unanswerable against a free-text field.

## 2. What a link claims

`ModelMechanismLink` asserts: *this model is informative for this mechanism node.*

It deliberately does **not** assert that the model is good, validated, or preferred. That
narrowing is the whole point — it makes the claim checkable. A model can be excellent for
one node in an entry and misleading for another, which is also why `readouts` live on the
link rather than on the model.

This is the same move the model-credibility literature makes with **context of use**: you
do not assess a model, you assess a model *for a stated use*. ASME V&V 40 and the FDA
credibility guidance both anchor every credibility activity in a stated question of
interest, context of use, and quantity of interest, and both require an **applicability
analysis** — an argument that the available validation evidence is relevant to *that*
context. A dismech link is a context-of-use statement; `divergences` is its applicability
analysis.

### 2.1 On borrowing from a medical-device framework

ASME V&V 40 and the FDA guidance were written for regulatory submissions of physics-based
device models. dismech is not a device submission and nothing here is a regulatory claim.
Two things make the borrowing sound anyway, and it is worth being explicit about which:

**What transfers.** The *structural* ideas are not device-specific. "Assess a model for a
stated use rather than in the abstract", "argue applicability separately from validity",
and "grade how much evidence you need by how much the answer matters" are claims about
the logic of model-based inference. They hold for a Boolean network of interferon
signalling exactly as they hold for a finite-element model of a pedicle screw.

**What does not.** The *procedural* apparatus does not transfer and is not imitated here:
no verification-and-validation plan, no uncertainty quantification, no sensitivity
hierarchy, no numeric credibility goals, no submission. dismech is annotating *published
models it did not build*, usually from the paper alone. It cannot assess numerical
accuracy and does not try to.

**The domain-general check.** The healthcare-wide
[ten rules of credible practice](https://pmc.ncbi.nlm.nih.gov/articles/PMC7526418/)
(Erdemir et al., *J Transl Med* 2020, PMID:32993675) reach the same conclusions without
any device framing. That paper explicitly covers "research, diagnosis, risk assessment,
prevention, therapy, rehabilitation, surgery, intervention design, and regulation", and
converged on rules "useful across a broad swath of model types". Three of its ten rules
are what this page describes:

| Rule | dismech implementation |
|---|---|
| 1. Define context clearly | `ModelMechanismLink` — a model is linked to a *specific* mechanism node, never to the entry at large |
| 3. Evaluate within context | `materiality` — does *this* divergence bear on *this* claim |
| 4. List limitations explicitly | `divergences` — typed and individually explained, not a prose blob |
| 10. Conform to standards | the SBML-qual / COMBINE alignment described in [computational models](computational-models.md) |

So the design is anchored in a healthcare-wide statement of credible practice, with the
device standards contributing vocabulary — *context of use*, *applicability*,
*risk-informed grading* — that the ten rules leave less formalised.

## 3. What the schema records

### 3.1 `model_scale` — the derivable part

`ModelMechanismLink.model_scale` records the biological scale the model **observes**,
using the same `BiologicalScaleEnum` as `Pathophysiology.biological_scale`. The gap
between the two is then **derived, never stored** (`just model-scale-audit`).

A model linked to a node is not necessarily operating at that node's scale. A Boolean
signalling network whose output node is named "bone erosion" observes cellular state and
*infers* the tissue outcome. Recording both scales makes that inference visible.

The comparison is **directional**, and the directions are different claims:

| Relation | Meaning |
|---|---|
| model **below** target | Upward extrapolation. The model cannot observe the outcome it is cited for. The reviewable case; requires `limitations` or a typed divergence. |
| model **above** target | The model contains the target scale. Unremarkable — a whole animal can report a molecular readout. |
| equal | No scale gap. |

Collapsing those into one "mismatch" flag would lose exactly the distinction that makes
the comparison worth computing.

### 3.2 `divergences` — the part that must be curated

Everything else needs a person. `ModelMechanismLink.divergences` is multivalued; each
`ModelDivergence` carries:

- **`divergence_type`** (required) — a value from `ModelDivergenceTypeEnum`
- **`description`** (required) — why that kind of gap applies *here*, in specific terms
- **`materiality`** (optional) — whether it bears on this link's claim
- **`evidence`** (optional) — for a divergence that is itself a published finding

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
        These are different measurements separated by transcription, translation,
        synthesis, transport and terminal survival.
    - divergence_type: BOUNDARY_OMISSION
      materiality: QUALIFYING
      description: >-
        Nigrostriatal terminal loss and the presynaptic deficit that clinically
        defines this node are not in the model.
```

The taxonomy was **derived from the KB, not invented**: all 50 computational-model
`limitations` strings were read and clustered, with the animal and NAM sets probed to
establish which kinds are shared. Every value has quoted evidence in the
[survey](../superpowers/specs/2026-09-02-model-divergence-taxonomy.md).

### 3.3 The distinction that matters most

**`PROXY_QUANTITY` vs `BOUNDARY_OMISSION`.** In a boundary omission the thing is not in
the model. In a proxy divergence it *is* — but as a stand-in of a different quantity.

Both can occur at the *same* biological scale, which is why neither follows from
`model_scale` and why the derivable part could never have been the whole answer. In V&V 40
vocabulary this is a *quantity of interest* mismatch, and it is the single most common
reason a dismech link is `PARTIALLY_RECAPITULATES`.

The Fanconi anemia FA/BRCA link is the worked case: model and target are both `MOLECULAR`,
so the scale comparison reports no gap, yet the link is `PARTIALLY_RECAPITULATES` because
homologous recombination appears as network components inside a crosslink-repair model —
what is reported is their activation state, where the node describes recombination
fidelity.

### 3.4 `materiality` and why it is per-divergence

`fidelity` grades a link; `materiality` grades one divergence *of* that link. A link can
carry several divergences of different weight, and the interesting value is `IMMATERIAL` —
a real limitation of the model that does not bear on this particular use of it. Recording
it stops a reader inferring that a known weakness undermines a claim it has no purchase on.

This mirrors the risk-informed grading in V&V 40 and the FDA guidance, where the
credibility evidence a model needs is set by its influence on the decision and the
consequence of the decision being wrong, rather than by one global quality score. Recording
materiality per divergence is also what could eventually let `fidelity` be *derived* rather
than authored — not proposed here, but the reason the slot is shaped this way.

## 4. What none of this claims

- **Not a quality score.** An `ALIGNED` scale comparison means "no *scale* gap", never
  "good model". A link with no divergences recorded may simply be uncurated.
- **Not verification.** dismech annotates published models from their papers. Nothing
  here speaks to numerical accuracy, solver convergence, or code correctness — the
  *verification* half of V&V is entirely out of scope.
- **Not exhaustive.** `OTHER` exists, and a divergence not in the taxonomy is a signal the
  taxonomy needs a value, not that the model is fine.
- **Not a regulatory assessment.** Borrowed vocabulary is not a borrowed warrant.

## 5. Current scope

`divergences` is populated on computational models only (10 links, 26 divergences). The
taxonomy was chosen to extend to NAM and animal models unchanged —
`BOUNDARY_OMISSION`, `PROXY_QUANTITY`, `CALIBRATION_PROVENANCE`, `POPULATION_MISMATCH` and
`SPECIES_MISMATCH` all apply as written. Extending would likely add
`SUPRAPHYSIOLOGICAL_EXPRESSION` and `INCOMPLETE_PHENOTYPE`, each already visible in the
animal set at 20–53 keyword hits and so evidenceable the same way the first eleven were.

Roughly 780 animal and NAM links carry prose `limitations` ready to be structured.

## 6. Tooling

```bash
just model-scale-audit                                    # census + cross-checks
just model-scale-audit --format list --verdict MODEL_BELOW_TARGET
just model-scale-audit --strict                           # gate
```

`--strict` fails on an upward-extrapolating link carrying neither `limitations` nor a
typed divergence, and on a `SCALE_EXTRAPOLATION` divergence contradicted by the scale
slots. The same two rules are enforced as tests
(`test_upward_extrapolating_links_are_caveated`,
`test_scale_extrapolation_divergence_agrees_with_scales`), alongside
`test_model_divergences_are_typed_and_explained`, which rejects a `description` that
merely restates its enum value.

## References

**Credible practice, domain-general**

- Erdemir A, Mulugeta L, Ku JP, et al. [Credible practice of modeling and simulation in healthcare: ten rules from a multidisciplinary perspective](https://pmc.ncbi.nlm.nih.gov/articles/PMC7526418/). *J Transl Med* 2020; PMID:32993675. Committee on Credible Practice of Modeling & Simulation in Healthcare (IMAG/MSM).

**Credibility frameworks, medical-device origin**

- ASME V&V 40-2018, [Assessing Credibility of Computational Modeling through Verification and Validation: Application to Medical Devices](https://www.asme.org/codes-standards/find-codes-standards/assessing-credibility-of-computational-modeling-through-verification-and-validation-application-to-medical-devices). FDA-recognized consensus standard; source of *context of use*, *applicability analysis*, and model risk as influence × consequence.
- FDA, [Assessing the Credibility of Computational Modeling and Simulation in Medical Device Submissions](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/assessing-credibility-computational-modeling-and-simulation-medical-device-submissions). Final guidance, CDRH, 16 November 2023; docket FDA-2021-D-0980.

**Model annotation and exchange**

- Le Novère N, et al. Minimum information requested in the annotation of biochemical models (MIRIAM). *Nat Biotechnol* 2005; PMID:16333295. The systems-biology-native convention for model provenance annotation, and the reason dismech records `model_format`, `repository_url` and `publication` rather than inventing its own.
- [COMBINE standards](https://co.mbine.org/) — SBML, SBML-qual, SED-ML, KiSAO, OMEX. See [computational models](computational-models.md).
