# The Experiment Model

*Status: design proposal, not yet a schema change. Tracked in
[§12 Gaps](design-decisions.md#12-gaps).*

`Experiment` is the class dismech uses to say *what would settle an open question*.
It is reached from `Discussion.proposed_experiments` and is deliberately
status-neutral: the schema's own comment says the object may "later be reused to
represent experiments that have been carried out."

This note argues that the class is under-specified in a way the data can
demonstrate, proposes splitting it by **design family**, and sets out how far
dismech should — and should not — go toward emitting protocols an automation core
or cloud lab could run. It is the data-model counterpart to the strategy in
[`projects/AUTONOMOUS_LABS.md`](../../projects/AUTONOMOUS_LABS.md), which names
the execution standards and the Ewing sarcoma demonstrator but specifies no schema.

## 1. The evidence that the flat class is failing

Across `kb/` there are **2,378 proposed experiments in 800 files**. Their slot
fill rates:

| Slot | Fill |
|---|---|
| `experiment_id`, `name` | 100% |
| `description` | 99.7% |
| `decision_criterion` | 30.5% |
| `would_support` | 15.6% |
| `experiment_type` | 15.5% |
| `readouts` | 12.2% |
| `supporting_outcome` | 9.5% |
| `controls` | 6.4% |
| `model_systems` | 5.7% |
| `perturbations` | 5.0% |
| `evidence` | 2.3% |
| `assays` | 0.5% |

Two readings are possible. Either curators are not filling in slots they could
fill, or the slots do not fit what they are trying to say. The `experiment_type`
values settle it: of 368 populated values there are **330 distinct strings and
exactly one ontology CURIE** (`OBI:0003552`, in a single entry). Curators are
hand-rolling a taxonomy the schema declined to give them, and writing the rest
into `description` — the one slot that fits everything, at 99.7%.

Note that `experiment_type` is documented as "prefer OBI terms when available."
That instruction is currently unfollowable: OBI is absent from
`conf/oak_config.yaml` and has no `cache/enums/` membership cache, so an OBI
binding cannot be validated the way HP/GO/CL bindings are. The same gap is
already recorded for `assays:` in CLAUDE.md. Any OBI-based plan has to close that
first.

## 2. Why the split is by design family

The four design families curators actually propose need near-disjoint slots:

| Family | Discriminating slots |
|---|---|
| Perturbation screen | compound/genetic library, model panel, readout assay, hit-calling threshold, counter-screen |
| Human observational | cohort size, inclusion/exclusion, exposure and outcome definitions, confounders, follow-up duration |
| Interventional trial | arms, randomization, blinding, primary endpoint, powering |
| In-silico | base model, parameter sweep, training/held-out data, validation metric |

A cohort study has no library and no plate; a screen has no confounders and no
follow-up duration. Flattening them into one class means every experiment carries
mostly-empty slots and every curator falls back to prose — which is what the table
in §1 shows happening.

LinkML expresses this with an abstract base plus `is_a` subclasses, surfaced as an
`any_of` on `Discussion.proposed_experiments`. Both idioms are already in use here
(53 `is_a` declarations, 5 `any_of`), so this is not a new pattern for the schema.

The shared base keeps what is genuinely type-agnostic — `experiment_id`, `name`,
`description`, `would_support` / `would_refute`, `supporting_outcome` /
`refuting_outcome`, `decision_criterion`, `evidence`, `notes`. These mean the same
thing for an organoid screen and a registry study, which is precisely the test for
whether a slot belongs on the base.

### An unrelated bug the split should fix at the same time

`Experiment.model_systems` has range `ExperimentalModel` — a class explicitly
scoped to non-animal New Approach Methodologies, whose `ExperimentalModelTypeEnum`
is `ORGANOID / ORGAN_ON_CHIP / CELL_LINE / IPSC_DERIVED_MODEL /
PRIMARY_CELL_CULTURE / CO_CULTURE / OTHER`. It cannot hold an `AnimalModel` or a
`ComputationalModel`, though both classes exist and both carry `modeled_mechanisms`.

So `OTHER` has become a dumping ground. Of the 135 `model_systems` on proposed
experiments, 38 are `OTHER`, and they are not one kind of thing:

```
OTHER | In-silico human ventricular action-potential model     <- computational
OTHER | Gyrencephalic ferret cortex                            <- animal
OTHER | Inducible SMN degradation SMA mouse model              <- animal
OTHER | Multi-region postmortem human MDD brain cohort         <- human cohort
```

`ExperimentalModel`'s own comment forbids exactly this ("Do not route an animal
model here via `experimental_model_type: OTHER`") — but for a *proposed* experiment
there is no alternative route. The fix that closed this for realized models
(#8199, giving `AnimalModel` its own `modeled_mechanisms`) was never applied to
`Experiment.model_systems`. Widening it to `any_of: [ExperimentalModel,
AnimalModel, ComputationalModel]` is worth doing independently of everything else
in this note.

This also answers "are some proposed experiments computational?" — yes, but only
about 3–5 of 2,378 unambiguously so, and they have nowhere to go. A keyword sweep
returns 7 candidates, of which several are false positives (in
`Primary_Ciliary_Dyskinesia_30`, "docking-complex" is the ciliary outer-dynein-arm
docking complex, not molecular docking). The genuine ones include CFD nasal
dosimetry in `Formaldehyde_Poisoning`, computational variant-effect predictors in
`SCN8A-Related_Developmental_and_Epileptic_Encephalopathy`, and
computationally-prioritised exosome cargo in `Keratoconus`.

## 3. Layers, not just types

The subclass split is necessary but not sufficient. The more consequential
boundary is between two layers that a single class would silently merge:

**Layer 1 — the scientific claim.** What question is open, what result would
settle it, and what that result licenses about a named pathograph edge. This is
disease-specific, curator-authored, and type-agnostic.

**Layer 2 — the executable protocol.** Reagents, catalog numbers, concentrations,
plate maps, incubation times, instrument calls. This is *not disease knowledge*.
It is protocol engineering, with its own lifecycle: versioned, parameterized, and
reused across many diseases.

Layer 2 does not belong in `kb/disorders/*.yaml`. A curator writing EWS-FLI1
chromatin biology is not going to specify well volumes, and if they did, the same
screening protocol would be duplicated into every disease entry that screens a
compound library — the same duplication argument that keeps mechanism modules
separate from the disorders that conform to them.

Dismech should hold layer 1 in full, and hold a **typed handle** to layer 2.

## 4. The executability ladder

Before any protocol binding exists, the schema should be able to say honestly how
far a proposal has been specified. A small closed enum on the base class:

| Value | Meaning |
|---|---|
| `CONCEPTUAL` | A design sketch in prose. The result would be interpretable, but the experiment is not specified enough to hand to anyone. |
| `SPECIFIED` | Model system, perturbation, readout and comparator are named as structured objects. A domain expert could write the protocol. |
| `PARAMETERIZED` | Bound to a named external protocol, with dismech supplying the scientific parameters. |
| `EXECUTABLE` | The bound protocol is machine-runnable and its parameters are complete. |

Today **all 2,378 would be `CONCEPTUAL`**, and stating that plainly is the point.
The ladder is worth adding on its own merit even if no protocol is ever bound: it
converts "we have 2,378 proposed experiments" — which invites the reading that
they are ready to run — into a defensible claim.

## 5. Protocol binding

The handle to layer 2, on the base class:

```yaml
executability: PARAMETERIZED
protocol_binding:
  protocol: labop:ht-faire-384/v2.1   # or a protocols.io DOI, or repo + tag
  protocol_format: LABOP              # LABOP | AUTOPROTOCOL | PROTOCOLS_IO | OTHER
  parameters:                          # dismech supplies SCIENTIFIC parameters only
    cell_panel: [A673, SK-N-MC]
    sentinel_loci: GGAA microsatellite enhancers
    perturbation: ETV6 degrader
```

`protocol_reference` already exists as a free string ("PMID, DOI, protocols.io
DOI, URL, or other stable identifier"). `protocol_binding` is the structured
successor for the executable case; the free-text slot stays for citing a methods
paper.

**The honest assessment of the cloud-lab distance.** The gap between what dismech
holds and what Emerald or Strateos accepts is not a schema gap. The Ewing
demonstrator — the richest proposed experiment in the KB — currently says:

> "Screen annotated epigenetic compounds, targeted degraders, kinase/chemical-probe
> libraries, and EWS-FLI1 or ETV6 perturbation controls"

An Autoprotocol run needs specific catalog numbers, concentrations, plate layouts,
timings and instrument models. No set of LinkML slots closes that distance from
the curation side, and a schema-wide push on execution detail would produce 2,378
empty slots — the failure mode `experiment_type` is already demonstrating.

## 6. What dismech actually owns

The strategically important claim in this note: **the protocol is not the valuable
part.** Protocols are increasingly commodity, and an LLM with instrument
documentation can draft one.

What dismech holds and a cloud lab cannot generate is the **pre-registered decision
rule bound to a named causal edge** — `decision_criterion` plus `would_support` /
`would_refute` pointing at specific `pathophysiology#` nodes. That is what turns a
returned plate reading into a pathograph update rather than a number.

`would_support` / `would_refute` are already hardened: #9224 restricted them to
entity references with no baseline, and 562 of 564 resolve as live in-page links.
`decision_criterion` is not: it is a free-text string, populated on 30.5% of
experiments. **That asymmetry is backwards**, and closing it is worth more than any
reagent slot. A structured `DecisionRule` — a readout reference, a comparator, a
threshold, and what the outcome licenses — is the actual pre-registration.

## 7. The missing return path

`Experiment` is documented as reusable for experiments already carried out, but
there is no `result` slot, and `EvidenceItem` (`reference`, `reference_title`,
`supports`, `directness`, `evidence_source`, `snippet`, `explanation`, `images`)
carries no pointer back to the experiment that produced it. Step 5 of the
AUTONOMOUS_LABS loop — "results return as evidence" — is unmodeled.

This collides with an exploration already on the books. §12 of the design register
carries **Experiment-grounded evidence**: an optional
`experiment{design, system, perturbation, readout, result, inference}` block on
`EvidenceItem` plus an `inference.role` enum, worked on the FH PCSK9 sub-graph
(see [The Evidence Model](evidence-model.md)).

That proposal and this one are **the same object viewed from opposite ends** — one
prospective, one retrospective. `experiment.design` and this note's design families
are the same enum; `experiment.readout` and `Experiment.readouts` are the same
class. Designing them separately would produce two incompatible vocabularies for
one concept, which is the shape of the `PARTIAL` / `directness` conflation that
#7439 had to unpick. **They should be one design.**

## 8. Staged proposal

| Stage | Work | Value absent any automation |
|---|---|---|
| 1 | Subclass by design family; add `executability`; widen `model_systems` to `any_of: [ExperimentalModel, AnimalModel, ComputationalModel]` | High. Makes 2,378 experiments classifiable and stops the `OTHER` leak. The 330 free-text strings cluster into ~8 families and can be backfilled semi-mechanically. |
| 2 | Structure `decision_criterion` as a `DecisionRule`, unified with the §12 experiment-grounded evidence design; add the return path from `EvidenceItem` | High. This is the pre-registration and the round-trip — the part that is dismech's own. |
| 3 | `protocol_binding` + `protocol_format`, applied to the Ewing demonstrator only | Low breadth, high signal. One worked exemplar, not a KB-wide push. |

Stages 1 and 2 pay for themselves whether or not a robot ever runs anything.
Stage 3 should stay a single exemplar until someone has actual automation-core
access.

## 9. Explicitly rejected

- **Subclassing by every parameter.** A class per assay type would multiply
  indefinitely and re-create the 330-string problem in class names.
- **Reagent-level detail in `kb/`.** See §3. It is not disease knowledge, it
  duplicates across entries, and curators will not author it.
- **Binding `experiment_type` to OBI as a first step.** Blocked on OBI adapter and
  enum-cache support (§1). The closed design-family enum does not depend on it and
  can land first; an OBI `Descriptor` remains available for finer detail later.
- **A `COMPUTATIONAL` value added to `ExperimentalModelTypeEnum`.** That enum types
  non-animal *wet-lab* NAMs. `ComputationalModel` already exists as its own class
  with `model_type`, `model_format` and `model_software`; the fix is to let
  `model_systems` reference it, not to grow a parallel vocabulary.

## Sources

- Slot fill rates and `OTHER`-bucket contents: computed over `kb/**/*.yaml`,
  2026-09-02.
- Strategy, execution standards (LabOP, Autoprotocol, SiLA 2), and the Ewing
  demonstrator: [`projects/AUTONOMOUS_LABS.md`](../../projects/AUTONOMOUS_LABS.md).
- Ewing curation target: `kb/disorders/Ewing_Sarcoma.yaml`,
  `gap_ewing_chromatin_reversal_screen`.
- Retrospective counterpart: [The Evidence Model](evidence-model.md) and
  [FH worked example](../reports/fh-experiment-grounded-evidence-2026-07-30.md).
