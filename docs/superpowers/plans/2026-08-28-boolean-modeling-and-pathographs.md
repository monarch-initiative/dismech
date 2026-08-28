# Boolean Modeling and dismech Pathographs (2026-08-28)

**Scope.** Three questions:

1. What is the state of the art in Boolean/logical modeling of disease, and what is the
   Disease Maps community actually doing with it?
2. Is Boolean modeling restricted to SIGNOR-style protein–protein / signaling models, or
   can it carry the broader, multi-scale node vocabulary dismech pathographs use?
3. Should Boolean models simply be another `model_type` under `computational_models`,
   alongside ABMs, ODEs and SBML — or do they need separate treatment?

Companion documents:
[`reports/computational-model-execution-landscape-2026-08-01.md`](../../reports/computational-model-execution-landscape-2026-08-01.md)
(the COMBINE/BioSimulators/CoLoMoTo survey this builds on),
[`explanation/computational-models.md`](../../explanation/computational-models.md)
(the in-repo `dismech-perturb` ODE runner), and
[`pathographs.md`](../../pathographs.md).

---

## 0. Answers up front

**On question 2 — no, Boolean modeling is not restricted to PPI/signaling networks.**
The formalism places no constraint on what a node denotes. Published disease Boolean
models routinely mix molecular species with cell populations, physiological states,
environmental exposures and clinical phenotypes in a single network. The canonical
MaBoSS prostate-cancer model has nine *input* nodes that are mostly not proteins at all
(Nutrients, Hypoxia, Acidosis, Carcinogen presence) and six *output* nodes that are
phenotypes rather than molecules (Proliferation, Apoptosis, Invasion, Migration,
Metastasis, DNA repair). Multiple-sclerosis multiscale networks carry immune cell
populations (Th17, Th1, CD8 subsets, memory B) as nodes, and connect them upward to
retinal damage and disability. That node vocabulary is close to a one-to-one match for
dismech's own — which is unsurprising, since both are abstractions of the same causal
biology.

So the node vocabulary is not the obstacle. **The obstacles are edge polarity and network
topology, and dismech currently has a problem with both** (§2).

**On question 3 — Boolean models are already a category, and that is the right answer for
half the problem, but it is the wrong frame for the other half.** There are two distinct
objects that both get called "Boolean modeling", and conflating them is the main design
risk here:

| | **Boolean model as an artifact** | **Boolean semantics as an interpretation of the pathograph** |
|---|---|---|
| What it is | A specific published or authored network with named nodes and update rules | A view over curated dismech content, mechanically derived |
| Where it belongs | `computational_models` entry, `model_type: BOOLEAN_NETWORK` — exactly like an ABM or ODE | An **exporter**, next to CX2 and KGX in `src/dismech/export/` |
| Analogue in repo | `models/urate_homeostasis.xml` + `.config.yaml` | `pathographs/MONDO_*.json`, `output/kgx/*.jsonl` |
| Curated by hand? | Yes — a curator cites or authors it | No — it is derived; curating it into YAML would be duplicating the pathograph |
| Status today | Enum value exists, one inert entry | Does not exist |

The user's instinct — "treat Boolean models separately, categorize them under
computational models the same way we treat ABMs, ODEs, SBML" — is correct for the left
column and **already implemented**: `ComputationalModelTypeEnum.BOOLEAN_NETWORK` has
existed all along. What is missing there is not a category but plumbing (§4).

The right column is the more interesting and more dismech-specific opportunity, and it is
explicitly *not* a `computational_models` entry. A compiled Boolean model of a pathograph
is a derived artifact of the same kind as the CX2 export. Putting it in the KB YAML would
mean hand-maintaining a second copy of the causal graph.

---

## 1. State of the art

### 1.1 The Disease Maps pipeline is the closest precedent

The Disease Maps community has a well-established route from a curated static map to an
executable model, and it is the single most relevant prior art for dismech:

**CellDesigner map → [CaSQ](https://academic.oup.com/bioinformatics/article/36/16/4473/5836892)
→ SBML-qual → GINsim / Cell Collective / MaBoSS.**

CaSQ ("CellDesigner as SBML-qual") infers *parameter-free* preliminary Boolean rules from
network topology plus semantic annotations, with no hand-written update functions, and
**retains the source map's references, annotations and layout** in the generated model.
That last property is what makes the output reviewable rather than a black box, and it is
the property dismech would most want to replicate.

Three flagship applications:

- **COVID-19 Disease Map.** Mechanistic C19DMap diagrams were translated wholesale by CaSQ
  into executable Boolean networks and
  [deposited as SBML-qual](https://fairdomhub.org/models/714), then used for
  [drug-target identification](https://www.frontiersin.org/journals/immunology/articles/10.3389/fimmu.2023.1282859/full).
- **Rheumatoid arthritis.** The RA-map (>1000 biomolecules) became one of the largest
  executable Boolean models in biology; the fibroblast-like-synoviocyte model
  [predicts drug synergies in the arthritic joint](https://www.nature.com/articles/s41540-023-00294-5).
- **Parkinson's disease.** The PD-map drives
  [cohort-specific probabilistic Boolean models](https://www.cell.com/iscience/fulltext/S2589-0042(24)02181-3)
  (*iScience* 2024), integrating patient cohort data to distinguish subtype-specific
  pathway deregulation (dopamine transcription, PI3K/AKT, FOXO3, mTOR-MAPK, PRKN mitophagy).

This is mainstream in that community, not a niche. At **DMCM 2025** the programme includes
Adrien Rougny on *"A query-driven framework for constructing Boolean networks from disease
maps: application to Parkinson's disease"*, Philippe Castera on *"Boolean modeling of
immune responses to vaccines"*, Othmane Hayoun-Mya on drug synergies through multiscale
modeling, and a Joaquín Dopazo keynote on causal modeling of disease maps for target
discovery. The query-driven framing in Rougny's talk is notable: it treats Boolean-network
construction as *a query over a map* rather than a one-shot conversion — which is closer
to what a dismech exporter would be than CaSQ's batch translation is.

### 1.2 Tooling is consolidated and cheap to adopt

The [CoLoMoTo consortium](https://pmc.ncbi.nlm.nih.gov/articles/PMC6018415/) ships ~20
tools (GINsim, bioLQM, MaBoSS, Pint, Cell Collective, pyBoolNet, mpbn) in one Docker image
with a Jupyter interface and a Python API per tool; the
[2025 Interface Focus tutorial](https://royalsocietypublishing.org/rsfs/article/15/3/20250002/235797/Reproducible-Boolean-model-analyses-and)
is the current reference. `bioLQM` converts SBML-qual to every other tool's native format.
Our own execution-landscape report already classed this as **Tier 1 — laptop, seconds**:
attractor computation on FA/BRCA-scale networks is trivial. There is no HPC story to worry
about at dismech's network sizes.

**SBML-qual** is the interchange standard
([L3 package spec](https://sbml.org/specifications/sbml-level-3/version-1/qual/sbml-qual-version-1-release-1.pdf),
[paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC3892043/)): `QualitativeSpecies` with
`initialLevel`/`maxLevel`, and `Transition` elements carrying function terms. Critically it
is **multi-valued, not merely Boolean** — a species may have `maxLevel > 1`, with
successor states differing by at most 1 per step. That matters for dismech because
`ModifierEnum` already distinguishes graded states (`INCREASED`/`DECREASED`) from
qualitative ones (`GAIN_OF_FUNCTION`/`LOSS_OF_FUNCTION`), and a three-level species
(0 = absent, 1 = normal, 2 = elevated) expresses that far more naturally than a Boolean.

### 1.3 Semantics: most-permissive is the right fit for dismech's abstraction level

This is the most technically important point in the survey.

Classical Boolean semantics (synchronous, asynchronous) are known to **miss behaviors**
that a quantitative system compatible with the same logic would show.
[Most Permissive Boolean Networks](https://www.nature.com/articles/s41467-020-18112-5)
(Paulevé et al., *Nat Commun* 2020) fix this: MPBN carries a formal guarantee not to miss
any trajectory achievable by *any* quantitative refinement of the network, specifically
including transitions arising from heterogeneous time scales and concentration scales.
Reachability is also dramatically cheaper to decide than in the classical modes.

Why this matters here: **4,695 dismech backbone edges are explicitly typed
`INDIRECT_UNKNOWN_INTERMEDIATES`** and another 3,994 `INDIRECT_KNOWN_INTERMEDIATES`. A
dismech causal edge is, by construction, a *coarse abstraction over omitted intermediates
with unknown kinetics*. That is precisely the class of object MPBN was designed to
over-approximate soundly. Under asynchronous semantics, a compiled dismech model would be
making timing claims the curation does not support; under most-permissive semantics it
makes only the claims the curation does support. **Any pathograph-compilation work should
target MPBN (`mpbn`/`bioLQM`) as its default semantics, and should say so explicitly.**

### 1.4 Multiscale coupling is a solved-enough problem

[PhysiBoSS 2.0](https://www.nature.com/articles/s41540-023-00314-4) embeds MaBoSS Boolean
networks as the intracellular layer inside PhysiCell agent-based simulations — Boolean
node states drive agent phenotype decisions, and the microenvironment feeds back into
Boolean input nodes. This is directly relevant because dismech already catalogues nine
`AGENT_BASED` PhysiCell models, and because it demonstrates the composition pattern our
own landscape report identified as the endpoint: "a molecular ODE node feeding a cellular
Boolean node feeding a tissue-scale ABM". It also validates the taxonomy question — the
field does treat Boolean as a peer modality to ABM and ODE, and composes them.

---

## 2. What dismech has today (measured 2026-08-28)

Whole-KB scan of `kb/disorders/` + `kb/modules/`:

| Quantity | Value |
|---|---:|
| Files with a `pathophysiology` block | 2,516 |
| Pathophysiology nodes | 15,288 |
| `downstream` (`CausalEdge`) edges | 27,525 |
| **Median pathograph size** | **5 nodes, 5 edges** |
| Largest pathograph | 116 edges (`Fanconi_Anemia`) |
| Targets with exactly one incoming edge | 22,578 / 24,653 (**91.6%**) |
| Targets needing an AND/OR decision (>1 in-edge) | 2,075 (8.4%) |
| **Pathographs containing any feedback loop** | **39 / 2,351 (1.7%)** |
| Nodes with a sign-bearing descriptor `modifier` | 7,041 (46.1%) |
| Nodes with only sign-neutral modifiers (`ABNORMAL`/`DYSREGULATED`) | 2,118 (13.9%) |
| Nodes with no `modifier` at all | 6,129 (40.1%) |
| Nodes whose *name* matches a directional lexicon | 6,377 (41.7%) |
| Nodes tagged `biological_scale` | 6,720 (44.0%) |
| Edges carrying `hypothesis_groups` | 1,715 (6.2%) |
| `computational_models` objects across the KB | 67 in 26 entries (71 in 28 after the stage-3 curation below) |
| …of which `model_type: BOOLEAN_NETWORK` | **1** at survey time (Fanconi anemia, FA/BRCA, PMID:22267503); **5** after stage 3 |

### 2.1 The two structural findings that shape everything else

**Finding 1 — `CausalEdge` has no sign.** The backbone edge class carries `target`,
`description`, `evidence`, `hypothesis_groups`, `causal_link_type` and
`intermediate_mechanisms`. `causal_link_type` encodes *directness*
(`DIRECT` / `INDIRECT_KNOWN_INTERMEDIATES` / …), **not polarity**. Meanwhile the
*peripheral* link classes already have exactly the vocabulary a logical model needs:
`TreatmentMechanismTarget.treatment_effect` (`INHIBITS`/`ACTIVATES`/…) and
`EnvironmentalMechanismTarget.environmental_effect`
(`TRIGGERS`/`EXACERBATES`/`PROTECTS_AGAINST`/…). The causal spine is the one unsigned
layer in the graph. That asymmetry is the central schema fact.

Sign is not absent from the KB — it is encoded in *node names and node descriptor
modifiers* ("Calcitriol Deficiency", "Decreased BMD", `modifier: INCREASED`) rather than
on edges. That convention works for human readers and for narrative rendering. It does not
survive mechanical compilation, and it is silently fragile: a "Decreased X" node feeding a
"Reduced Y" node is a double negative that no validator currently checks.

**Finding 2 — pathographs are trees, not networks.** 91.6% of targets have in-degree 1 and
only 1.7% of pathographs contain any feedback loop at all. This is the finding that should
temper expectations most, and it needs stating plainly:

> **A Boolean model compiled from a typical dismech pathograph today would be dynamically
> trivial.** A DAG has exactly one fixed point per input configuration. No multistability,
> no oscillation, no interesting attractor landscape, no drug-synergy prediction. Every
> headline result the field gets from Boolean models — the RA drug synergies, the PD
> subtype separation, the MaBoSS phenotype probabilities — comes from *feedback loops and
> combinatorial logic*, and dismech has almost none of either.

This is not a reason to abandon the idea. It is a reason to be precise about what the
near-term payoff actually is (§5), and to recognise that the causal-spine curation style —
short linear chains from etiology to phenotype — is a deliberate and reasonable modeling
choice that happens to be orthogonal to what makes Boolean dynamics informative.

### 2.2 What is already in place and reusable

- **`ComputationalModelTypeEnum.BOOLEAN_NETWORK` exists.** No new enum needed.
- **`ModelMechanismLink`** is shared across `experimental_models`, `animal_models` and
  `computational_models`, and already links a model to a pathophysiology node with
  `relationship` / `fidelity` / `limitations` / `readouts`. A Boolean model needs nothing
  new here.
- **`perturbations` is typed `GeneDescriptor`** — which is a *better* fit for Boolean
  models (node knock-out / knock-in are the native Boolean perturbation) than it is for
  the ODE models it was written for.
- **`hypothesis_groups` on `CausalEdge`** is a ready-made selector for compiling
  *alternative* logical models from one pathograph, at zero schema cost (§5.3).
- **`biological_scale`** (44% tagged, `MOLECULAR`/`CELLULAR`/`TISSUE`/`ORGANISM`) is the
  natural axis for deciding which layer of a composed model a node belongs to.
- **The `models/<model_id>.{xml,ant,config.yaml}` convention** plus
  `perturb/__main__.py:_find_model_config` gives a working pattern for attaching an
  executable artifact to a `computational_models` entry via `model_id`.

### 2.3 What is missing

1. `model_format` is a **free-text string**, 34/67 unset, with 22 distinct prose values in
   use. Any design that keys off `model_format: SBML-qual` needs the range tightened first.
2. **No slot for an in-repo model artifact path** — the ODE path gets away with a
   filename convention off `model_id`.
3. **`ModelVariableDescriptor.threshold` is float-valued** and `extract_model_variables`
   hard-requires `threshold` + `threshold_direction` + an `HP:` term. For a Boolean model
   the node *is* the phenotype; `threshold: 0.5, threshold_direction: above` is a
   semantic hack that should not be enshrined.
4. **The one existing `BOOLEAN_NETWORK` entry is inert** — no `model_format`, no
   `model_id`, no `repository_url`, no `modeled_mechanisms`. It is a bare literature
   citation, and is exactly the "disconnected list entry" failure mode CLAUDE.md warns
   about. *(Resolved 2026-08-28: it now carries two `modeled_mechanisms` links — see
   the stage-3 note below.)*

---

## 3. Design position

**Boolean modeling enters dismech along two independent tracks that share almost no
machinery. Do not merge them.**

- **Track A — Boolean models as catalogued and executable artifacts.** Low risk, follows
  the ODE precedent exactly, unblocks curation immediately. This is the "same as ABM/ODE/
  SBML" framing, and it is right.
- **Track B — pathograph → logical-model export.** Higher value, higher risk, requires one
  schema change, and its near-term payoff is *validation and reachability queries*, not
  simulation.

Track A should not wait for Track B, and Track B's schema change is worth making on its
own merits regardless of whether any Boolean model is ever compiled (§5.1).

---

## 4. Track A — Boolean models as `computational_models` entries

The goal is that a curator can cite the RA-FLS model or the FA/BRCA model, and that where
an SBML-qual file exists we can actually run it and map attractors onto HP phenotypes,
using the same `ModelVariable` machinery the ODE path uses.

**A1. Tighten `model_format` to an enum.** Introduce `ModelFormatEnum` with at least
`SBML`, `SBML_QUAL`, `SBML_FBC`, `CELLML`, `ANTIMONY`, `BNET`, `GINML`, `MABOSS_BND_CFG`,
`PHYSICELL_XML`, `ONNX`, `MATLAB`, `OTHER`. Migrate the 33 populated free-text values;
this is the mechanical backfill item 1 of the execution-landscape report already asked for.
Without this, "is this model runnable and by what engine" stays unanswerable.

**A2. Adopt the artifact convention for Boolean models.** `models/<model_id>.sbmlqual.xml`
as the canonical stored form (bioLQM converts to everything else), with `.bnet` permitted
as the human-editable source in the way `.ant` is for ODE models. No new slot needed —
reuse `model_id`.

**A3. Relax `extract_model_variables` for discrete models.** Allow a `ModelVariable` whose
`dataset_identifier` names a Boolean node to map to an HP term **with no threshold**, and
add `threshold_kind: DISCRETE_STATE` (or equivalent) so the intent is explicit rather than
encoded as `0.5 / above`. Note `threshold_kind` already exists as a *derived* field in
`perturb/results_export.py` but not in the schema — promoting it is a small, well-motivated
change.

**A4. Add a CoLoMoTo execution path to `dismech.perturb`.** Mirror the structure of the
proposed COBRApy path (item 3 of the landscape report, which established the precedent that
a new execution class needs *no new schema*): load SBML-qual via `bioLQM`/`mpbn`, apply
`perturbations` as node fixings, compute attractors under most-permissive semantics, read
the output-node states, and emit the same `exports/model_runs/<model_id>.json` shape the
ODE path emits. Scenarios come from `models/<model_id>.config.yaml` as today, with
`gene_effects` mapping a gene to a node fixing (`LoF → 0`, `GoF → 1`) instead of to a
parameter multiplier — a natural fit for the existing `GeneEffect` dataclass.

**A5. Repair and extend the FA/BRCA entry as the pilot.** It is already curated, the
network is small, and the paper is a CoLoMoTo-era Boolean model. Add `model_format`,
`repository_url`, `modeled_mechanisms` linking to the Fanconi anemia pathograph's DNA-repair
nodes, and — if the published network can be obtained or reconstructed — a
`models/` artifact. Then add 3–5 more from the Disease Maps corpus (RA-FLS, a COVID-19
C19DMap submodel, the PD-map cohort models), which are all deposited and citable.

None of A1–A5 requires a change to `Disease`, `Pathophysiology` or `CausalEdge`.

---

## 5. Track B — pathograph → logical model

### 5.1 The one schema change: sign on `CausalEdge`

Add a polarity slot to `CausalEdge`, mirroring the existing and well-established
`treatment_effect` / `environmental_effect` precedent:

```yaml
  causal_effect:
    description: >-
      Whether the source mechanism promotes or suppresses the target mechanism's state.
      Note that dismech node names frequently already encode a direction ("Decreased Bone
      Mineral Density"); this slot describes the influence of source on target as named,
      so an edge onto a negatively-named node is normally PROMOTES.
    range: CausalEffectEnum
```

```yaml
  CausalEffectEnum:
    permissible_values:
      PROMOTES:     # source state increases the likelihood/degree of the target state
      SUPPRESSES:   # source state decreases it
      REQUIRED_FOR: # target cannot occur without source (necessity, not just promotion)
      UNKNOWN:
```

**Why this is cheap.** Because dismech encodes sign in node names, the overwhelming
majority of backbone edges are `PROMOTES` — the edge "PTH Excess → Decreased BMD" is a
*promoting* edge onto a negatively-named state. So the backfill is mostly a default, and
genuine curation effort falls only on the minority of genuinely suppressive edges
(compensatory mechanisms, negative feedback, protective responses). That is a much smaller
ask than "sign 27,525 edges".

**Why it is worth doing anyway, independent of Boolean modeling.** An unsigned causal edge
is lossy for the KGX/BioLink export too — BioLink distinguishes
`causes` from predicates carrying directionality, and the environmental exporter already
special-cases `PROTECTS_AGAINST` to reach
`biolink:associated_with_decreased_likelihood_of`. The backbone cannot currently express
the same thing. Sign also enables a **double-negation lint**: flag a `PROMOTES` edge whose
source and target descriptor `modifier`s are both `DECREASED`, which today is an
undetectable curation error.

`REQUIRED_FOR` is included deliberately: it is the distinction that lets a compiler emit
`AND` rather than `OR` at the 8.4% of targets with multiple in-edges, and it corresponds to
the necessary/sufficient logic-type distinction that the causal-logic-inference literature
uses to reduce manual Boolean-model construction effort.

Per the process in [`explanation/design-decisions.md`](../../explanation/design-decisions.md),
this needs an issue, maintainer sign-off, and a design-decision entry in the same PR as the
schema change.

### 5.2 The exporter

`src/dismech/export/logical_export.py`, sitting alongside `cx2_export.py` and
`kgx_export.py`, reusing `graph.build_causal_graph` so it inherits every edge kind for free
(treatment `targets`, environmental `triggers`, biochemical `readout`, genetic
`contributes_to`) rather than reading YAML afresh.

Compilation rules, in brief:

- Each graph node → one `QualitativeSpecies`. Default Boolean; allow `maxLevel: 2` where a
  node carries graded `INCREASED`/`DECREASED` modifiers.
- Node role from in/out degree: zero in-degree → **input** node (etiology, exposure,
  genotype); `phenotype`-typed nodes → **output**/read-out nodes, directly mirroring the
  MaBoSS input/output convention (§1.1). This is where the answer to question 2 becomes
  concrete: dismech's node typing already *is* the input/phenotype-output structure that
  published Boolean disease models hand-build.
- Edge → term in the target's transition function, sign from `causal_effect`.
- Multiple in-edges → `OR` by default; `AND` over the `REQUIRED_FOR` subset.
- `treatment_effect: INHIBITS` → a suppressing input node, giving *in-silico treatment
  perturbation for free* on any pathograph with curated `target_mechanisms`.
- Emit **SBML-qual**, so the entire CoLoMoTo stack applies with no bespoke tooling.
- Carry evidence: like CaSQ, retain PMIDs and node/edge provenance as SBML annotations so
  the generated model is reviewable against the curation it came from.
- **Declare most-permissive semantics** (§1.3) in the export and in any analysis.

### 5.3 What this buys us in the near term — and what it does not

Given §2.1 Finding 2, be honest about the payoff ordering:

1. **Consistency checking (real, immediate).** Compiling to a logical model turns curation
   defects into type errors: double negations, edges whose sign contradicts the target's
   modifier, phenotype nodes unreachable from any etiologic input, nodes that no input can
   ever activate. This is analogous in spirit to `check-entity-refs` and would catch a
   class of error nothing currently detects.
2. **Reachability and perturbation queries (real, immediate).** "If treatment T inhibits
   node X, which phenotype nodes become unreachable?" is answerable on a DAG, is cheap
   under MPBN, and is exactly the question the curated `treatment.target_mechanisms` edges
   were built to support. This works *without* feedback loops.
3. **Competing-hypothesis comparison (real, and distinctively dismech).** `hypothesis_groups`
   lets us compile one logical model per `MechanisticHypothesis` from the *same* pathograph
   and ask which hypothesis's model reaches the observed phenotype set. No other disease-map
   resource has hypothesis-tagged edges to do this with. Only 6.2% of edges are tagged
   today, so this starts as a pilot on the entries that are.
4. **Attractor landscapes, multistability, drug synergy (not yet).** These need feedback
   loops. 1.7% of pathographs have any. Claiming these as near-term deliverables would be
   overselling.

A useful side effect: running the exporter across the KB produces a *ranked list of
pathographs that would benefit from feedback curation* — the entries where the literature
plainly describes a vicious cycle that the current linear chain does not capture. That is a
concrete curation-quality signal derived from the modeling work, even before the modeling
work pays off.

---

## 6. Staged plan

| Stage | Work | Depends on | Payoff |
|---|---|---|---|
| **0** | Open the design-decision issue for `CausalEdge.causal_effect`; tag `@cmungall` | — | Unblocks Track B |
| **1** | A1 `ModelFormatEnum` + backfill; A5 repair the FA/BRCA entry | — | Fixes the known `model_format` mess; the one Boolean entry stops being inert |
| **2** | A2 artifact convention, A3 discrete thresholds, A4 CoLoMoTo runner | 1 | Boolean models become *runnable in-repo*, joining the four ODE models |
| **3** ✅ | Curate 3–5 Disease Maps Boolean models (RA-FLS, C19DMap submodel, PD-map) with `modeled_mechanisms` | — | Real content; validates the pipeline against externally published models |
| **4** | Schema: `causal_effect` + `CausalEffectEnum`; double-negation lint; default backfill | 0 | Signed causal spine — valuable for KGX/BioLink independently |
| **5** | `logical_export.py` → SBML-qual, MPBN semantics; consistency + reachability checks over the KB | 4 | Curation-defect detection; treatment-perturbation queries |
| **6** | Hypothesis-group model comparison pilot on the 6.2% tagged edges | 5 | The distinctive research contribution |
| **7** | *(exploratory)* feedback-loop curation worklist; PhysiBoSS-style composition using `biological_scale` | 5 | Where genuine Boolean dynamics would start to pay off |

### Stage 3 status — done (2026-08-28)

Five `BOOLEAN_NETWORK` models are now curated and pathograph-linked, ahead of stages 1–2
(the curation does not depend on the `ModelFormatEnum` or the runner):

| Entry | Model | PMID | Links |
|---|---|---|---:|
| `Rheumatoid_Arthritis` | RA-FLS large-scale Boolean model | 37454172 | 3 |
| `Parkinsons_Disease` | PD map cohort-specific probabilistic Boolean models | 39429779 | 2 |
| `COVID-19` | C19DMap SBML-qual model collection (FAIRDOMHub 714) | 34664389 | 1 |
| `COVID-19` | Type 1 interferon signalling Boolean model | 38414974 | 2 |
| `Fanconi_Anemia` | FA/BRCA pathway Boolean model *(A5 repair)* | 22267503 | 2 |

All five record `model_format: SBML-qual` except the 2012 FA/BRCA model, where the format
and repository are left unset with the reason recorded in `notes` rather than guessed.
Four of the five carry a `repository_url`. Ten `modeled_mechanisms` links were added in
total, four of them `PARTIALLY_RECAPITULATES` with `LOW`/`MODERATE` fidelity where the
Boolean model addresses a molecular pathway rather than the tissue- or organism-scale node
it is linked to — the honest grading matters more here than link count.

This also produced the first worked instances of the §5.2 claim that dismech node typing
already matches the input/output structure of published Boolean disease models: the type 1
IFN model's four output nodes (viral replication, antiviral response, inflammation, IFNA1
secretion) and the RA-FLS model's five phenotype submodels are curated as `readouts` on the
links, grounding phenotype-level Boolean outputs against dismech pathophysiology nodes.

Stages 1–3 are Track A and can proceed immediately and independently. Stage 4 is worth
doing on its own merits. Stages 5–7 are where the research value is, and are gated on 4.

---

## 7. Risks and open questions

- **The trivial-dynamics risk (§2.1) is the main one.** Mitigation: frame Track B's stage-5
  deliverable as validation and reachability, not simulation, and let the feedback-curation
  worklist (stage 7) be the path to dynamics rather than assuming it.
- **Sign-in-node-name vs sign-on-edge is a genuine modeling ambiguity.** The proposed
  `causal_effect` semantics ("influence of source on target *as named*") must be stated
  unambiguously in the slot description and in CLAUDE.md, or curators will split evenly on
  how to sign an edge into a "Decreased X" node. The double-negation lint is the safety net.
- **Do we ever want multi-valued rather than Boolean?** SBML-qual supports it and
  `ModifierEnum`'s graded/qualitative split maps onto it well. Recommendation: emit Boolean
  first, keep `maxLevel` in the exporter's design so the door stays open.
- **Should modules carry logical models?** `kb/modules/` is where reusable mechanism
  structure lives and is the most plausible home for curated feedback loops (a fibrotic
  response *is* a vicious cycle). A module-level logical model that conforming disorders
  inherit is attractive — but note the modules design is explicitly **not DRY**, so this
  would need care to avoid contradicting the conformance model.
- **Naming.** "Boolean" vs "logical" vs "qualitative": the field uses *logical model* as
  the superset (Boolean + multi-valued). Prefer `logical_export.py` and "logical model" in
  prose, reserving `BOOLEAN_NETWORK` for the existing enum value.

---

## Sources

**Reviews and methodology**

- [Boolean modelling as a logic-based dynamic approach in systems medicine](https://www.sciencedirect.com/science/article/pii/S2001037022002495), *CSBJ* 2022
- [Applications of Boolean modeling to study the dynamics of a complex disease and therapeutics responses](https://pmc.ncbi.nlm.nih.gov/articles/PMC10267406/)
- [Concepts in Boolean network modeling: What do they all mean?](https://www.sciencedirect.com/science/article/pii/S200103701930460X)
- [The status of causality in biological databases: data resources and data retrieval possibilities to support logical modeling](https://academic.oup.com/bib/article/22/4/bbaa390/6055722), *Brief Bioinform* 2021 (SIGNOR and peers)
- [Inference of a Boolean Network From Causal Logic Implications](https://pmc.ncbi.nlm.nih.gov/articles/PMC9246059/) (necessary/sufficient logic types)

**Semantics**

- [Reconciling qualitative, abstract, and scalable modeling of biological networks](https://www.nature.com/articles/s41467-020-18112-5), *Nat Commun* 2020 (most-permissive)
- [Most Permissive Semantics of Boolean Networks](https://arxiv.org/pdf/1808.10240)

**Standards and tooling**

- [SBML Level 3 Package: Qualitative Models](https://sbml.org/specifications/sbml-level-3/version-1/qual/sbml-qual-version-1-release-1.pdf); [SBML qualitative models paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC3892043/)
- [The CoLoMoTo Interactive Notebook](https://pmc.ncbi.nlm.nih.gov/articles/PMC6018415/), *Front Physiol* 2018
- [Reproducible Boolean model analyses and simulations with the CoLoMoTo software suite](https://royalsocietypublishing.org/rsfs/article/15/3/20250002/235797/Reproducible-Boolean-model-analyses-and), *Interface Focus* 2025
- [Automated inference of Boolean models from molecular interaction maps using CaSQ](https://academic.oup.com/bioinformatics/article/36/16/4473/5836892), *Bioinformatics* 2020; [docs](https://soliman.gitlabpages.inria.fr/casq/)
- [bioLQM: a java library for the manipulation and conversion of logical qualitative models](https://www.biorxiv.org/content/10.1101/287011v1.full.pdf)

**Disease Maps applications**

- [Systems medicine disease maps: community-driven comprehensive representation of disease mechanisms](https://www.nature.com/articles/s41540-018-0059-y), *npj Syst Biol Appl* 2018
- [COVID-19 Disease Map](https://fairdomhub.org/models/714) (SBML-qual deposits); [drug-target identification using the map](https://www.frontiersin.org/journals/immunology/articles/10.3389/fimmu.2023.1282859/full)
- [A large-scale Boolean model of the rheumatoid arthritis fibroblast-like synoviocytes predicts drug synergies](https://www.nature.com/articles/s41540-023-00294-5), *npj Syst Biol Appl* 2023
- [Cohort-specific Boolean models highlight different regulatory modules during Parkinson's disease progression](https://www.cell.com/iscience/fulltext/S2589-0042(24)02181-3), *iScience* 2024
- [DMCM 2025 programme](https://disease-maps.io/DMCM2025/) (Rougny, Castera, Hayoun-Mya, Dopazo)

**Non-molecular nodes and multiscale composition**

- [Modeling signaling pathways in biology with MaBoSS](https://pmc.ncbi.nlm.nih.gov/articles/PMC9582792/), *CSBJ* 2022 (prostate model input/output phenotype nodes)
- [Patient-specific Boolean models of signalling networks guide personalised treatments](https://elifesciences.org/articles/72626), *eLife* 2022
- [Multiscale networks in multiple sclerosis](https://pmc.ncbi.nlm.nih.gov/articles/PMC10852301/) (cell-population and disability-level nodes)
- [PhysiBoSS 2.0: a sustainable integration of stochastic Boolean and agent-based modelling frameworks](https://www.nature.com/articles/s41540-023-00314-4), *npj Syst Biol Appl* 2023
