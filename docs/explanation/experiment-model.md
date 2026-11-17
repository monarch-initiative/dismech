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

Across `kb/` there are **3,191 proposed experiments in 1,186 files** (measured
2026-10-31; the corpus grew 34% in the two weeks this note was being written, so
treat any absolute count here as dated). Their slot fill rates:

| Slot | Fill |
|---|---|
| `experiment_id`, `name` | 100% |
| `description` | 99.8% |
| `experiment_design` | 36.4% (backfilled; see §9) |
| `would_support` | 27.3% |
| `decision_criterion` | 26.4% |
| `experiment_type` | 13.4% |
| `readouts` | 13.1% |
| `perturbations` | 5.0% |
| `model_systems` | 4.6% |
| `assays` | 0.5% |
| `executability` | 0% |

Two readings are possible. Either curators are not filling in slots they could
fill, or the slots do not fit what they are trying to say. The `experiment_type`
values settle it: of 428 populated values there are **384 distinct strings and
exactly one ontology CURIE** (`OBI:0003552`, in a single entry). Curators are
hand-rolling a taxonomy the schema declined to give them, and writing the rest
into `description` — the one slot that fits everything, at 99.8%.

The ratio is also getting *worse*, which is the strongest evidence that this is
a schema problem rather than a curation-effort problem: the free-text slot went
from 330 distinct strings in 368 values to 384 in 428, so almost every new
experiment that fills it invents a new string.

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

LinkML expresses this with `is_a` subclasses off the existing `Experiment`, which
is already the schema's commonest idiom (53 class-level `is_a` declarations, 29 of
them `Descriptor` subclasses).

**No `any_of` is needed on `Discussion.proposed_experiments`, and an earlier draft
of this note was wrong to propose one.** Tested against LinkML 1.10.0: a plain
`range: <Base>` on an `inlined_as_list` slot already accepts any subclass, and
already rejects an instance that mixes slots from two sibling subclasses. Adding
`any_of` over the same classes changes nothing — the two schemas produce
byte-identical validator behaviour on good data, bad data, and chimeric data. The
5 existing `any_of` uses in this schema are all *scalar* unions (`float|int|string`,
`FrequencyEnum|FrequencyQuantity`), and that is the only thing `any_of` should be
used for here; see the warning in the next section.

The one real cost of subclassing is the error message. A rejected instance reports
only `is not valid under any of the given schemas`, naming neither the family it
failed nor the offending slot. That is a genuine curator-usability regression, and
it is the main argument for pairing subclasses with an explicit `experiment_design`
discriminator rather than leaving the family implicit in which slots are present.

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
`Experiment.model_systems`.

**Do not fix this with `any_of`.** Widening the slot to
`any_of: [ExperimentalModel, AnimalModel, ComputationalModel]` was tried and
reverted; on LinkML 1.10.0 it does not work, in two different ways:

- Keeping `range: ExperimentalModel` alongside the `any_of` generates a broken
  union — two of the three branches collapse to `{"type": "string"}`, and the
  surviving `$ref` is **and**ed with the `anyOf`, so every already-valid
  `ExperimentalModel` in `kb/` starts failing with *"Additional properties are not
  allowed ('experimental_model_type', 'organism' were unexpected)"*.
- Switching to the scalar-union idiom (`range: Any` + `any_of`, as `percentage`
  uses) generates three correct `$ref` branches but is **worse**: JSON Schema
  ignores keywords sibling to `$ref`, so only `$ref: Any` applies — and `Any` is
  `additionalProperties: true`. The slot then accepts arbitrary garbage. A
  fixture carrying `totally_bogus_slot` validated clean.

That second failure is the dangerous one, and it is the same shape as the
`qualifiers` blind spot (#10197): validation appears to pass because it has
silently stopped happening. `range: Any` + `any_of` is safe for the scalar unions
it is used for today and must not be extended to inlined object ranges.

**The fix is the three-way split the KB already uses.** `Disease` separates
`experimental_models:` / `animal_models:` / `computational_models:`, and the
latter two slots already exist with exactly the right ranges and
`inlined_as_list: true`. Adding them to the `Experiment` class reuses those slots
verbatim, needs no union, validates properly in both directions, and gives
curators the same three section names at both levels.

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
| `PARAMETERIZED` | Bound to a named external protocol, with dismech supplying the scientific parameters. In practice the signal for this rung is an `executable_protocols` entry (§5). |
| `EXECUTABLE` | The bound protocol is machine-runnable and its parameters are complete. |

Today **all 2,378 would be `CONCEPTUAL`**, and stating that plainly is the point.
The ladder is worth adding on its own merit even if no protocol is ever bound: it
converts "we have 2,378 proposed experiments" — which invites the reading that
they are ready to run — into a defensible claim.

## 5. Protocol binding — largely built upstream already

**This section originally proposed a `protocol_binding` slot. While this note was
being written, `Experiment.executable_protocols` landed on `main`, and it covers
most of what that proposal was for.** The proposal is superseded rather than
pending, and what remains open is narrower than it was.

The shipped `ExecutableProtocol` class records "a concrete, orderable protocol at
a named provider that would execute some or all of a proposed experiment": a
required `name` as the provider publishes it, plus `provider`, `venue_type`,
`protocol_id`, `protocol_url`, `inputs_required`, `retrieved_date`, and
`measures` — the pathograph nodes it would return a measurement on. Currently
used in one entry (`Prolidase_Deficiency`).

It is a better fit for this note's argument than the `protocol_binding` sketch
was, in three ways worth recording:

- **It is explicitly a feasibility note, not a plan.** Its own comment says
  recording a protocol "does not propose, authorise, fund, or commit to running
  anything, and it is not evidence about the disease". That is the layer-1 /
  layer-2 boundary from §3, enforced in the class's documentation.
- **`measures` points into the pathograph**, so a recorded service is tied to the
  node whose gap it would close — the same discipline `would_support` applies to
  the decision rule, and more than the opaque parameter map in the old sketch.
- **It deliberately carries no price, turnaround, or throughput**, on the grounds
  that those "go out of date without any signal that they have, and reproducing a
  vendor's price list is not this knowledge base's job". `test_executable_protocol_schema.py`
  gates both that exclusion and the rule that a catalogue identifier is never
  recorded without `retrieved_date`.

Two things the old sketch had that the shipped class does not, and only one of
them is a real gap:

- **A machine-readable protocol *format*** (`LABOP` / `AUTOPROTOCOL` /
  `PROTOCOLS_IO`). A `protocol_url` at a provider is orderable by a human; it is
  not a document an automation core can execute. This is the remaining gap, and
  it is only worth closing if someone actually has automation access — see §9 on
  how thin the executable slice turns out to be.
- **A parameter map** for the scientific parameters dismech supplies.
  `inputs_required` already covers the useful half of this, and a free-form map
  would have been the weakest part of the sketch. Not a gap.

`protocol_reference` remains the right slot for citing a *methods paper*; the two
are properly distinguished in the shipped slot's own description.

**The honest assessment of the cloud-lab distance is unchanged.** The gap between
what dismech holds and what Emerald or Strateos accepts is not a schema gap. The
Ewing demonstrator — still the richest proposed experiment in the KB — says:

> "Screen annotated epigenetic compounds, targeted degraders, kinase/chemical-probe
> libraries, and EWS-FLI1 or ETV6 perturbation controls"

An Autoprotocol run needs specific catalog numbers, concentrations, plate layouts,
timings and instrument models. No set of LinkML slots closes that distance from
the curation side, and a schema-wide push on execution detail would produce
thousands of empty slots — the failure mode `experiment_type` is already
demonstrating.

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
| 1a | **ENACTED.** `ExperimentDesignEnum` (8 values) + `ExperimentExecutabilityEnum` (4) as optional `experiment_design` / `executability` slots on `Experiment`; `animal_models` and `computational_models` added to the `Experiment` class | High. Makes 2,378 experiments classifiable and closes the `OTHER` leak. The 330 free-text strings cluster into the 8 families and can be backfilled semi-mechanically. |
| 1b | **ENACTED for the backfill (§9).** 1,165 of 3,200 experiments classified, 2,035 worklisted. The model-system migration is **not** done: only 17 of 59 are migrations, each needs an `organism`→`species` transformation, and 21 are human cohorts with no home in the schema at all | High. The enum went from available to the third-best-filled slot on `Experiment`. |
| 1c | Per-family detail blocks (`screen_details`, `cohort_details`, …), either as `is_a` subclasses or as the discriminator-plus-detail-block idiom `therapeutic_modality` / `aso_details` already uses. **1b has now sized these:** targeted perturbation (668) and human observational (320) are where the weight is, and the latter needs a study-population slot to absorb the 21 homeless cohorts | Medium-high. 1b showed which families carry weight, and that one of them is leaking into `model_systems: OTHER`. |
| 2 | Structure `decision_criterion` as a `DecisionRule`, unified with the §12 experiment-grounded evidence design; add the return path from `EvidenceItem` | High. This is the pre-registration and the round-trip — the part that is dismech's own. |
| 3 | **Largely superseded** by `Experiment.executable_protocols`, which landed upstream (§5). What remains is a machine-readable `protocol_format`, worth doing only with real automation access | Low breadth. One worked exemplar at most, not a KB-wide push. |

Stages 1 and 2 pay for themselves whether or not a robot ever runs anything.
Stage 3 should stay a single exemplar until someone has actual automation-core
access.

**Why 1a landed the discriminator rather than the subclasses the staging table
originally called for.** Both are wanted, but the enum is the part that can be
populated on every experiment today, and it is what makes the backfill in 1b
possible at all: a subclass cannot be chosen for an instance until the
family-specific slots exist to justify the choice, so subclassing first would have
produced four empty classes and no classified experiments. The enum also supplies
the diagnosable error that bare subclassing lacks (see §2), and it is gated for
free — `check_enum_values.py` is an ungated, whole-KB CI step, so a bad
`experiment_design` fails on any PR, including a `kb/`-only one.

## 9. What the backfill actually achieved (stage 1b)

`scripts/backfill_experiment_design.py` assigned **1,165 of 3,200 experiments
(36.4%)**, across 729 files, in a diff that is 1,165 insertions and zero
deletions. That single slot is now better filled than `decision_criterion`
(26.4%) and nearly three times better filled than the `experiment_type` it
supersedes (13.4%).

| Family | n |
|---|---|
| TARGETED_PERTURBATION | 668 |
| HUMAN_OBSERVATIONAL | 320 |
| DESCRIPTIVE_PROFILING | 113 |
| INTERVENTIONAL_TRIAL | 61 |
| PERTURBATION_SCREEN | 2 |
| IN_SILICO | 1 |

The remaining 2,035 are in
`docs/reports/data/experiment-design-backfill-worklist-2026-11-06.tsv` with the
reason each was skipped. They are deliberately left absent: 1,892 raise no
unambiguous anchor at all, 109 use a perturbation word only for a comparator,
and 34 raise anchors from two families, where `MIXED` is a curator's judgement
that a script cannot make. This follows `scripts/migrate_supports_enum.py`,
which refused on the same grounds to guess a `directness` nobody had assessed.

**Precision was measured, not assumed.** Two blind stratified samples were read
by hand against the enum definitions: 80% on the first rules, 94% after scoping
matches to the experiment's *method statement*, and the two residual failures in
that sample are exactly what the screen-name and human-study-unit guards in the
script now catch. A later review found one systematic error outside the sample:
`hypomorphic` alone often describes the patients' own alleles in a
genotype-stratified human study, which engineers nothing. It now counts as a
targeted-perturbation anchor only when the same method statement names an
engineered system (a mouse, zebrafish, model, knock-in or conditional allele),
which moved 11 experiments from `TARGETED_PERTURBATION` to the worklist. It is not 100%, so the annotation is advisory and the diff is
meant to be read.

**The distribution is itself a finding.** `PERTURBATION_SCREEN` matches twice in
3,191 experiments. The flagship cloud-lab demonstrator in
`projects/AUTONOMOUS_LABS.md` is a high-throughput chromatin screen, and the
automation standards that project names — LabOP, Autoprotocol, SiLA — are built
for exactly that shape of experiment. But the KB's proposed experiments are
overwhelmingly *targeted* perturbations and *human* studies, neither of which a
cloud lab can run. This does not sink the project; it does mean the executable
slice is far thinner than the headline count of 3,191 proposals suggests, and
stage 3 should be sized against the screens, not the corpus.

### The model-system migration is curation, not migration

Of the 59 model systems still carrying `OTHER` or no type
(`docs/reports/data/experiment-model-systems-worklist-2026-11-06.tsv`):

| Classification | n | Disposition |
|---|---|---|
| Human cohort | 21 | **No schema home** — see below |
| Animal model | 15 | Move to `animal_models` |
| NAM missing its type | 10 | Stays; needs a real `experimental_model_type` |
| Unclear | 11 | Curator judgement |
| Computational | 2 | Move to `computational_models` |

So only 17 are migrations, and they are **not moves**: `ExperimentalModel`
carries `organism`, `AnimalModel` carries `species` plus `genotype`, so each one
is a data transformation. Several name no species at all ("Gyrencephalic
mammalian model", "Genotype-specific arrhythmogenic cardiomyopathy models"), and
scripting a `species` value for those would fabricate one. They are left as
curator work with the worklist committed, rather than mechanically mis-tagged —
the failure CLAUDE.md records for the nutritional-support treatment backfill.

**The 21 human cohorts are the real finding, and they change stage 1c.** A
patient cohort is not a model system under any of the three classes, because it
is not a model of anything — it is the study population. The three-way split
inherited from the disease level (`experimental_models` / `animal_models` /
`computational_models`) has no fourth branch for human subjects, and curators
with nowhere else to put a cohort put it in `model_systems: OTHER`. That is an
argument for the `HUMAN_OBSERVATIONAL` detail block in stage 1c carrying the
study population as a first-class slot — and, incidentally, the single largest
use of the `OTHER` bucket this note set out to close.

### What the migration pass closed, and why the animal rows stayed put

Of the 59 rows, 11 are now closed: both computational systems moved to
`computational_models` (the CiPA in-silico arm in `Long_QT_Syndrome` and the
temperature-dependent CaV1.2 model in `Timothy_Syndrome`, both typed `KINETIC`),
and nine of the ten NAMs got a real `experimental_model_type`.

A twelfth is decided but not yet applied. One of the eleven "unclear" rows is
not unclear at all — `Hepatocellular_Carcinoma`'s HepG2 row is a cell line, and
it reads as ambiguous only because its description is about *labelling* the line
correctly (hepatoblastoma-derived, not HCC-derived) rather than about what kind
of system it is. That entry carries seven pre-existing reference-validation
failures unrelated to this axis — two cached references with no content, a paper
title used as an evidence snippet, and three JAMA snippets that concatenate the
structured-abstract section label onto the first sentence, so `ImportanceThe
burden of liver cancer varies worldwide.` does not match a cache that has the
label on its own line. Touching the file for a one-word enum value would pull
all seven into the changed-path validator, so the row waits for the change that
fixes them.

**The fifteen animal rows were not moved, and the reason is stronger than the
missing species.** Measured against the two classes rather than assumed: five of
the fifteen carry an NCBITaxon-bound `organism`, which `AnimalModel.species` — a
plain string — would turn back into free text; three of those five also carry
`tissue_term` or `cell_types`, for which `AnimalModel` has no slot at all. The
remaining ten record no organism whatsoever, and four of those name no species
anywhere in the record ("Gyrencephalic mammalian model", "CML patient-derived
xenograft (PDX)", "Rat and mouse embryonic neocortex", "Rodent or porcine VML
injury model").

So the migration is lossy exactly where the record is best annotated and
under-determined exactly where it is worst. There is no subset of the fifteen
where it is clean, which is the signal that the target class is wrong rather
than that the rows are sloppy.

**The cause is the same inheritance that produced the human-cohort problem.**
`Experiment`'s model sections were given the disease level's three-way split,
and the two levels ask different questions. At disease level an `AnimalModel`
record describes an animal *line* — genotype, background, alleles — and that is
what its slots are for. At experiment level what needs describing is a
*preparation*: a ferret cortex, the brain and microglia of an `Atp7b` R778L
mouse, rat and mouse embryonic neocortex under in-utero electroporation. A
preparation is scoped to a tissue and a cell type, which is what
`ExperimentalModel` expresses and `AnimalModel` does not. Adding an in-vivo
value to `ExperimentalModelTypeEnum` is not the fix either: that class defines
itself as non-animal, so the value would contradict its own scope statement.
Together with the 21 human cohorts, **36 of the 59 rows have no good home** — a
considerably stronger argument for the stage-1c detail blocks than the cohorts
alone.

Two smaller findings from the same pass. The worklist itself misfiled one row:
"SMA mouse model with locked miR-128-3p inhibitor" is classified as a NAM
needing a type, but its description is a severe SMA mouse (`Smn1-/-`; `Smn2`
transgene), so it belongs with the animal rows and keeps `OTHER` for the reason
above. And `ExperimentalModelTypeEnum` has no value for an engineered 3D tissue:
`MRPL44_Deficiency`'s maturation-promoted engineered heart tissue exists
precisely to escape the immaturity of monolayer iPSC cardiomyocytes, yet the
only true value available is `IPSC_DERIVED_MODEL`, the same one its monolayer
siblings carry. The distinction survives in the name and description rather than
in the enum, which is the ontology-binding compromise CLAUDE.md already
sanctions for `preferred_term`, applied to a closed vocabulary instead.

### The DESCRIPTIVE_PROFILING / HUMAN_OBSERVATIONAL tie-break

Both values fit a study that measures human material without perturbing it, and
the backfill left the overlap unresolved. The discriminator is the **unit of
analysis**, now recorded in both enum descriptions:

- `HUMAN_OBSERVATIONAL` when the inference is about the *people* — penetrance,
  prevalence, natural history, genotype-phenotype correlation, case-control
  association. The participants are the study population.
- `DESCRIPTIVE_PROFILING` when the inference is about the *specimens* — a
  single-cell atlas, a spatial map, postmortem characterization. The
  participants are where the tissue came from.

Two things follow that are easy to miss. `DESCRIPTIVE_PROFILING` is not a
human-material value at all: profiling an animal or an in-vitro system without
perturbing it belongs there too, so the two values only compete over
human-specimen profiling and not over the whole non-perturbational space. And
the word in the title decides nothing — "Longitudinal profiling of
presymptomatic HMOX1-null siblings" follows people and is
`HUMAN_OBSERVATIONAL`, while "Adequately powered brain EWAS with cell-type
deconvolution" characterizes a methylome and is `DESCRIPTIVE_PROFILING`.

**The rule codifies existing practice rather than reclassifying it.** Read
against the 453 records already carrying one of the two values, it moves
exactly one. That is the outcome a tie-break should have: it makes the next
assignment deterministic without churning the corpus. The one move,
`exp_imcd_pretreatment_endotype_stratified_trial`, was not a profiling-versus-cohort
confusion at all — the proposal randomizes patients to an endotype-matched agent
after the profiling step, so it is an `INTERVENTIONAL_TRIAL` whose stratification
arm had been read as the design.

A related false positive is worth stating, because it is the shape a stricter
rule would get wrong. Four other `HUMAN_OBSERVATIONAL` records mention
randomization in order to *rule it out*, and the clearest says why: a registry
rather than a trial "because withholding chelation from a severely poisoned
child is not randomisable". The other three likewise call a randomized
comparison not feasible or not realistic at their disease's rarity. All four
are correctly non-interventional, and all four mention the word because the
author anticipated the question. What makes a record `INTERVENTIONAL_TRIAL` is
the investigator allocating the intervention, not the word appearing.

### Two values had no uses, and one of them has a visible population

`METHOD_DEVELOPMENT` and `MIXED` were unused across every assignment the
backfill made, which is what a conservative matcher does to the values that
need judgement: both require reading an experiment's purpose rather than its
nouns. Each now has a first use, and they came from opposite directions.

`exp_acy1_hearing_replication` is the straightforward `MIXED` case. Its name
gives two arms equal billing — "Independent human hearing cohort replication
and orthogonal model validation" — and the point of the word *orthogonal* is
that neither arm alone settles the question, which is precisely the condition
the value documents.

`METHOD_DEVELOPMENT` is the more interesting one, because what identifies it is
not in the experiment at all. `exp_stxbp1_mouse_human_trajectory_comparison`
runs two perturbation arms (an `Stxbp1+/-` mouse series and patient iPSC
neurons against an isogenic-corrected control), so every anchor in its own text
points at `TARGETED_PERTURBATION`. But it sits under a `HUMAN_MODEL_MISMATCH`
discussion, its stated aim is to "quantify where the mouse under-represents
human severity", and its decision criterion is whether the mouse is a faithful
model. The object under test is the model system, which is what
`METHOD_DEVELOPMENT` means. The perturbations are how the comparison is made,
not what it is about.

**That generalizes into a prior, and it must not be applied as a rule.** 918
proposed experiments across the KB sit under `HUMAN_MODEL_MISMATCH`
discussions — the second-largest discussion kind after `KNOWLEDGE_GAP` — and
they are where `METHOD_DEVELOPMENT`'s real population lives. But a gap of that
kind asks whether a model reflects human biology, and an experiment proposed to
close it can legitimately be model validation (`METHOD_DEVELOPMENT`), a human
study supplying the comparator (`HUMAN_OBSERVATIONAL`), or a perturbation in a
better model (`TARGETED_PERTURBATION`). Reassigning them from the parent
discussion's `kind` would repeat the backfill's error at four times the scale.
The usable finding is narrower and sharper: the parent discussion's `kind` is a
signal the backfill never read, and it is the one place to look for the value
that currently has a population of one.

## 10. Explicitly rejected

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

- Slot fill rates, design distribution and `OTHER`-bucket contents: computed
  over `kb/**/*.yaml`, 2026-10-31. The corpus is growing fast (2,378 experiments
  on 2026-09-02, 3,191 on 2026-10-31), so recompute rather than quoting these.
- Backfill tooling and worklists: `scripts/backfill_experiment_design.py`,
  `docs/reports/data/experiment-design-backfill-worklist-2026-11-06.tsv`,
  `docs/reports/data/experiment-model-systems-worklist-2026-11-06.tsv`.
- Strategy, execution standards (LabOP, Autoprotocol, SiLA 2), and the Ewing
  demonstrator: [`projects/AUTONOMOUS_LABS.md`](../../projects/AUTONOMOUS_LABS.md).
- Ewing curation target: `kb/disorders/Ewing_Sarcoma.yaml`,
  `gap_ewing_chromatin_reversal_screen`.
- Retrospective counterpart: [The Evidence Model](evidence-model.md) and
  [FH worked example](../reports/fh-experiment-grounded-evidence-2026-07-30.md).
