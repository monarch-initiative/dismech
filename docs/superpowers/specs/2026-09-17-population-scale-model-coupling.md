# Population-Scale Model Coupling: what dismech would have to supply (2026-09-17)

**Purpose.** Answer two questions that came up from
[camdl](https://github.com/vsbuffalo/camdl), a compartmental infectious-disease
modelling DSL: does dismech capture infectious disease *models*, and if not, what
would it have to add for a within-host mechanism record and a between-host
transmission model to be coupled?

**Short answers.** No — `computational_models` is entirely within-host, and not one
infectious-disease entry carries a model at all. And the missing piece is not a
solver or a file format: it is a **mapping from a model's compartments to curated
disease states**, which is a small schema addition on top of machinery the KB
already has.

**Method.** Audit of `kb/` and `src/dismech/schema/dismech.yaml` at `3bfbcdb57`
(2026-09-16), plus a read of camdl's README for what a compartmental model actually
needs. Counts below are a snapshot; the KB grows.

---

## 1. What is captured today

**Infectious disease etiology is structured and well populated.** 133 of 2,965
disorder entries carry `infectious_agent:` (`dismech.yaml:4049`); 72 carry
`transmission:`; `hosts:` binds NCBITaxon with definitive/intermediate/reservoir
roles, and `agent_life_cycle:` / `vectors:` sit beside it. 29 modules are tagged
`INFECTIOUS_DISEASE`.

**Computational models exist but are all within-host.** 101 model instances across
48 files. `ComputationalModelTypeEnum` (`dismech.yaml:1945`) offers
GENOME_SCALE_METABOLIC, FLUX_BALANCE_ANALYSIS, KINETIC, AGENT_BASED,
BOOLEAN_NETWORK, PHYSIOLOGICAL, DIGITAL_TWIN, MACHINE_LEARNING,
PERTURBATION_PREDICTION, FOUNDATION_MODEL, STRUCTURAL_PREDICTION,
MOLECULAR_DOCKING. All 14 `AGENT_BASED` models are tissue-scale (PhysiCell tumour
microenvironment, mdx muscle regeneration). COVID-19's two models are SBML-qual
Boolean signalling maps.

**The intersection is empty.** No entry with `infectious_agent:` has a
`computational_models:` block.

**Population dynamics survives only as scalars and prose.**

| Slot | Shape | Use |
|---|---|---|
| `epidemiology:` → `EpidemiologyInfo` (`dismech.yaml:7018`) | name / description / `minimum_value` / `maximum_value` / `factors` / `unit` / evidence | 186 disorder entries; **6 reproduction-number records across 4 entries** — Measles R0 12–18, Cholera R0 1–20 and Rt 0.5–8, Hepatitis B R0 2–10 and Rt 0.3–1.2, Chickenpox R0 3–7 |
| `modeling_considerations:` | name / description / evidence | 3 entries (`Cholera`, `Long_COVID`, `Pontiac_Fever`) |

`Cholera.yaml`'s `modeling_considerations` is the tell: it is a cited wish-list for
a transmission model ("Environmental Dynamics", "Population Mobility"), and one of
its own references is PMID:30861666, *"Modeling cholera dynamics at multiple scales:
environmental evolution, between-host transmission, and within-host interaction."*
The coupled model is literally cited in the KB and nowhere represented.

## 2. What blocks hosting a transmission model

| | Status |
|---|---|
| `model_format` (`dismech.yaml:4762`) | **Not a blocker** — free text; `.camdl` or its JSON IR drops straight in, as `CellML`, `SBML-qual` and prose formats already do |
| `model_type` | No compartmental value. `AGENT_BASED` would be a lie for an ODE or Gillespie SEIR |
| `modeled_mechanisms` | Link targets resolve to pathograph nodes, which are within-host by construction. S/E/I/R compartments have no target |
| `BiologicalScaleEnum` (`dismech.yaml:2466`) | Stops at `ORGANISM` — `model_scale` cannot describe a population model |
| `EpidemiologyInfo` | Holds a min/max and free-text factors. No distribution, no denominator, no link to the mechanism that sets the value |

## 3. Coupling patterns, grounded in curated content

A nested (immuno-epidemiological) model is one where a within-host result supplies a
parameter or a structure to a between-host model. Five patterns, each with an entry
that already carries the within-host side.

**3.1 Compartment = curated disease state (structural).**
`Tuberculosis.yaml:89,103` carries exactly two `progression:` phases, `Latent` and
`Active` — the E and I compartments of every TB model written. The entry also holds
the initial condition (LTBI point prevalence 23.67%, ~1.7B people,
`Tuberculosis.yaml:65`). TB latency definitions are famously incommensurable between
models, so a shared anchor is the use case; what the anchor would buy is a
*mechanistic* definition of the state, and that part is not yet curated — the
`granuloma_formation` and `intracellular_pathogen_persistence` modules exist and are
the obvious conformance targets, but `Tuberculosis.yaml` declares no `conforms_to`
at all. Prerequisite, not a given.

**3.2 Rate parameter grounded in a mechanism (provenance).**
`Hepatitis_B.yaml:195` — perinatal infection carries up to 90% chronicity risk,
against roughly 5% in adults. In a compartmental model that is an age-stratified
branching probability into the carrier compartment. dismech supplies the mechanism
(neonatal immune tolerance) and the citation, so the age dependence is an evidenced
claim rather than a fitted nuisance parameter.

**3.3 Infectiousness as a within-host output (the canonical nested model).**
`Acquired_Immunodeficiency_Syndrome.yaml:796` curates HIV viral load as a biomarker
readout, and treatments reach mechanism nodes through `target_mechanisms`.
Transmission probability as a function of viral load, suppressed by ART, is
treatment-as-prevention. Malaria is the same shape with gametocyte density and
mosquito infectiousness.

**3.4 Observation model = case definition.**
camdl's fifth element is observations linking latent processes to measured data, and
reporting fraction is the classic identifiability wrecker when fitting to
surveillance. A surveillance time series counts whatever the case definition counts,
and 29 infectious entries already carry `definitions:` — 23 of them
`CASE_DEFINITION` (AIDS, Brucellosis, Campylobacteriosis, Acute Flaccid Myelitis),
11 `DIAGNOSTIC_CRITERIA` — beside LOINC-bound `biochemical:` reference ranges with
interpretation bands.

What is *not* there is the quantitative half. `validation_status` with a measured
PPV attaches to `PHENOTYPE_ALGORITHM` definitions, of which the KB has 20 and
**none on an infectious entry**. So the schema already supports anchoring a
reporting probability to a validated algorithm; no infectious entry exercises it.
That gap is small, self-contained, and independently useful — it is the cheapest
concrete follow-on this note identifies.

**3.5 Intervention arms.** 54 disorder entries carry `therapeutic_modality:
VACCINE`. Efficacy against infection, against onward transmission, and against
severe disease are three different parameters; `target_mechanisms` records which
node each acts on, which makes "leaky versus all-or-nothing" a mechanistic claim
instead of a modelling convention.

## 4. Cross-disease coupling — the class only a multi-disease KB serves

Patterns 3.1–3.5 could each be handled inside a single-disease modelling project.
These cannot: one disease's model changes another's, and the link lives in neither
model.

- **Measles immune amnesia.** `Measles.yaml:168` already carries `Immune amnesia` as
  a `downstream` edge off viral replication, with the VirScan repertoire-erasure
  evidence at `:248`. The coupled model is: measles SEIR output feeds a time-varying
  susceptibility multiplier into *every other* childhood-infection model. That is the
  all-cause-infectious-mortality result, and the link is a KB fact, not a model fact.
- **Antibiotic stewardship → C. difficile.**
  `Clostridioides_difficile_Infection.yaml:253` has `Loss of Colonization Resistance`
  as a causal target driven by antibiotic exposure (`gut_dysbiosis`). Antibiotic use
  is a *treatment* in every bacterial-infection model and a *susceptibility driver*
  in the CDI model: a stewardship intervention in model A changes the inflow to the
  susceptible compartment in model B.
- **Dengue ADE forces model topology, not just parameters.** `Dengue.yaml:403-405`
  explicitly records ADE as covered in deep-research artifacts but not yet a
  pathophysiology node. ADE is why a single-serotype SIR is wrong — serotype-stratified
  compartments with enhancement are required. A within-host immunology claim
  determining between-host model *structure* is the strongest argument for the
  mapping being semantic rather than numeric. Note the prerequisite: the ADE node is
  a curation increment that has to land first.
- **Infection → chronic sequelae.** `kb/comorbidities/` already holds
  `com_Influenza__Myocardial_Infarction`, `com_Influenza__Alzheimer_Disease`,
  `com_Respiratory_Syncytial_Virus_Infection__Heart_Failure`,
  `com_Rhinovirus_Infection__Asthma`. Transmission-model output (infections averted)
  feeding a chronic-disease incidence model is the vaccine cost-effectiveness
  argument that gets rebuilt ad hoc every time.
- **TB/HIV** — coinfection as a shared risk stratum across two coupled transmission
  models.

## 5. Proposal

Tiered, so the cheap part is not held hostage to the hard part.

**Tier 1 — one enum value.** Add `COMPARTMENTAL_TRANSMISSION` to
`ComputationalModelTypeEnum`, described to cover deterministic ODE, chain-binomial
and stochastic (Gillespie) compartmental transmission models. Agent-based
transmission models keep `AGENT_BASED`. With `model_format` already free text, this
alone lets the handful of diseases with real transmission-modelling literature
register a model with `repository_url`, `publication`, `findings` and `evidence`.
No new class, fully reversible.

**Tier 2 — the interface: `compartments:` on `ComputationalModel`.** A compartment
is not a mechanism the model recapitulates, so it does not belong in
`modeled_mechanisms`. Give it its own list, reusing the existing entity-reference
grammar so `check_entity_ref_foreign_keys` covers it for free:

```yaml
computational_models:
- name: Age-structured TB transmission model
  model_type: COMPARTMENTAL_TRANSMISSION
  model_format: camdl
  compartments:
  - name: L
    attaches_to: progression#Latent
    description: Infected, not infectious; reactivation hazard set by the granuloma state.
  - name: I
    attaches_to: progression#Active
```

That is the whole interface. Two models whose `L` both resolve to
`progression#Latent` are talking about the same state; two that do not, are not.

**Tier 3 — deferred, and not recommended yet.** A `POPULATION` value on
`BiologicalScaleEnum`, typed transmission parameters, and explicit cross-disease
coupling links. Each needs a decision that tier 2 does not.

### The scale question tier 3 has to answer first

`BiologicalScaleEnum` is shared between `Pathophysiology.biological_scale` and
`ModelMechanismLink.model_scale` on purpose: `just model-scale-audit` compares them,
reading *model scale below target* as upward extrapolation and *above* as
containment ("a whole animal can report a molecular readout").

Adding `POPULATION` breaks the containment reading. A SEIR model sitting "above" a
molecular node does not contain it in any useful sense — it cannot report that
readout at all. So `POPULATION` cannot simply be appended; it needs either a
separate model-scale enum (losing comparability, which was the point of sharing
one) or an explicit rule that the audit's directional reading applies only within an
organism. Tier 2 sidesteps this entirely by not routing compartments through
`modeled_mechanisms`.

## 6. What this does not claim

- **dismech does not become a modelling platform.** It records that a model exists,
  what its compartments mean, and what it predicts. Simulation, fitting and
  inference stay in camdl or wherever the model lives.
- **Nested models are frequently not identifiable** from surveillance data alone —
  coupling adds parameters faster than data constrains them. The value added here is
  provenance and shared semantics, not better fits. Nothing in this proposal should
  be read as encouragement to fit a coupled model because the KB made one
  expressible.
- **The addressable set is small.** Of 133 infectious entries, on the order of ten
  have transmission-modelling literature worth registering. This is a targeted
  addition, not a corpus-wide curation programme.
- **Scope is genuinely arguable.** A compartmental model is about a population;
  dismech's unit of content is a disorder's pathophysiology. Tier 1 and tier 2 are
  defensible as *registering and anchoring* models that explain a curated disease
  state. Anything beyond that is a scope decision for
  `docs/explanation/design-decisions.md`, not a schema decision.

## 7. Related

- [#4998](https://github.com/monarch-initiative/dismech/issues/4998) — structure
  infectious-agent etiology, split transmission versus life-cycle. Adjacent: it
  structures the *etiology*, this structures the *models*.
- [#7520](https://github.com/monarch-initiative/dismech/issues/7520) — render
  structured epidemiology on disorder pages. Any `EpidemiologyInfo` change should be
  coordinated with it. Note its out-of-scope list already names `transmission` (56
  files) and `modeling_considerations` (3) as slots the disorder template does not
  render: anything tier 1 or tier 2 adds will be invisible on the pages too until
  that rendering work happens.
- `docs/explanation/model-credibility.md` — what a model-to-mechanism link does and
  does not claim; the same discipline applies one scale up.
- `projects/PATHOPHYSIOLOGY_SCALE_FEASIBILITY.md` — the survey that fixed
  `BiologicalScaleEnum` at four values, and so the thing a `POPULATION` value has to
  argue against.
