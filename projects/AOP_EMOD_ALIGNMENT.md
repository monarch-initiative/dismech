---
title: AOP EMOD Framework Alignment
status: IN_PROGRESS
description: >-
  Assess to what extent dismech's environmental-exposure and evidence model
  aligns with the Adverse Outcome Pathway framework & the expanded AOP Evidence Model (EMOD),
  with an eye towards identifying ways dismech might be expanded and enriched by incorporating AOPs,
  ways dismech might seed development of new AOPs, and ways that AOP EMOD might adopt evidence
  modeling approaches from dismech.
tags: [FRAMEWORK_ALIGNMENT, EVIDENCE, EXTERNAL_COLLABORATION, ENVIRONMENTAL_EXPOSURE, SCHEMA_EVOLUTION]
diseases:
  - Lead_Poisoning
modules:
  - cardiac_ion_channel_repolarization
  - cardiomyopathy_maladaptive_remodeling
  - glutamate_excitotoxicity
  - synaptic_vesicle_cycle
  - mitochondrial_dysfunction
  - excitatory_synapse_scaffold_disruption
  - drug_induced_liver_injury
  - drug_induced_nephrotoxicity
  - diabetic_vascular_complications
---

# AOP EMOD Framework Alignment

## Scope

This project started with issue [#8309](https://github.com/monarch-initiative/dismech/issues/8309), which
asked **to what extent** dismech's environmental-exposure and evidence modeling approaches align with the Adverse
Outcome Pathway (AOP) framework, including the AOP Evidence Model (EMOD) expansions. Iterative
refinement of the questions that need to be asked led to the content of this project document.
The project should be used to identify specific directions for dismech and AOP integration.

There are **two AOP reference categories** describing the AOP framework and the data classes on a conceptual level.

| Reference category | What it is | Status |
|---|---|---|
| **AOP-Wiki v2.8 data model** | The current structure. The AOP Developers' Handbook presents it conceptually to humans; the bulk XML serializes it. | Stable, citable |
| **AOP EMOD** | Computable expansion of v2.8, adding structure to fields that are currently free text. | Being adopted by the AOP community; details not OECD-endorsed and open to change |

`Lead_Poisoning` is the pilot comparator entry used to ground the comparison
against a real dismech pathograph.

## What this page is

It records an inventory of schema comparisons. It does **not** decide adoption. Whether dismech should
sanction AOP-Wiki as a structured reference source or represent canonical AOPs as
modules are separate calls belonging in their own issues.

**Stability is a property of individual constructs, not of either framework.** Both
models mix settled and experimental elements, so how firmly a claim can be stated
depends on which construct it describes — not on which side of the comparison it sits.

- **AOP side.** Settled: Key Event Components, deployed since AOP-Wiki Release 2.2,
  and the v2.8 serialization. Open: EMOD concepts are being adopted by the AOP
  community, but the details have not been endorsed by the OECD as the AOP standard
  and remain open to change.
- **dismech side.** Settled: `EvidenceItem` and `CausalEdge`, exercised across ~2000
  entries. Open: `biological_scale` is optional and barely populated, and OBI assay
  grounding is unvalidated.

## What is known about the AOP Schema

The record begins with each framework described on its own terms — what it defines,
and how firmly — before any construct is mapped from one to the other.

### The AOP-Wiki data model — v2.8 and EMOD properties

Normative reference: Villeneuve D, Meek B, Viviani B, Burgdorf T, LaLone C,
O'Brien J, et al. *AOP Developers' Handbook v2.8*. AOP-Wiki; 2026
([aopwiki.org/handbooks/6](https://aopwiki.org/handbooks/6)).

**What was inspected here is the serialization, not the Handbook prose** — the
official bulk XML export dated 2026-08-06 (holding 595 AOPs, 2361 KERs), processed in
@gingin77's [`aop_wiki_cli`](https://github.com/gingin77/aop_wiki_cli). The Handbook
outlines what AOP authors are instructed to do, whereas the XML shows which fields
exist and what they contain.

#### Backbone

`MIE → KE → KER → AO`, with `Prototypical Stressors` attached as a separate
annotation layer. AOPs are **stressor-agnostic by design**: the stressor→MIE link is
deliberately not part of an AOP. The reason is predictive toxicology — a mechanism
characterized once, in studies using prototypical stressors, can then be used to
screen thousands of chemicals against it.

An **Event** is the first-class object; MIE, KE, and AO are roles an Event plays
within a particular AOP. Events carry their own stable identifiers and exist
independently of any one AOP.

Re-using Events across AOPs is how AOP networks form. This is an explicit design
goal rather than an emergent property: an Event appearing in several AOPs is what
joins them into a network.

The backbone is neither strictly linear nor necessarily fully connected. Two Events
may sit in the same AOP without a KER pairing them, and a KER may itself record
feedforward or feedback loops — AOP 17 carries a neuroinflammation ⇄ cell-injury
loop.

#### Key Event Components

Key Event Components (KECs) were introduced in AOP-Wiki Release 2.2 to make Events
computable by binding them to OBO Foundry terms. Each KEC defines a discrete **action**,
**object**, and **process** term.

Action terms come from an AOP-Wiki controlled vocabulary based on the Phenotypes and
Traits Ontology (PATO). Object and process terms use selected bio-ontologies. Separate
controlled vocabularies define levels of biological organization (LoBO), sex, and life
stage; CL and UBERON give biological spatial context for Events; and NCBI Taxon labels
species applicability for Events, KERs, and AOPs.

EMOD adds **phenotype** as a fourth entity alongside action, object, and process. Its
Observation and Assay classes each define a biological object, process, and/or
phenotype, serving Events across all levels of biological organization from molecular to
population. The phenotype property does work the other three cannot: paired with
Experimental Effect it separates a chemical that induces an outcome from one that treats
it — the difference between an Observation mapping to a Seizure Event and one mapping to
a Decreased Seizure Event.

#### Maturity stages

AOPs can be classified in ways that reflect maturity of knowledge associated with a
pathway, how extensively they have been developed, and how much quantitative data is
available to support their use for predictive toxicology.

A 2014 paper on AOP development offers the following AOP classification options:

- **Putative AOP development** — "Assembly of a hypothesized set of KEs and KERs
  supported primarily through biological plausibility and/or statistical inference.
  Assembly of partial AOPs with incomplete linkage between the MIE and AO as a result
  of known gaps and uncertainties."
- **Qualitative formal AOP development** — KEs supported by descriptions of how they
  can be measured, and KERs supported by empirical evidence in addition to plausibility
  or statistical inference, "along with qualitative evaluation of the overall weight of
  evidence supporting the AOP." Formal in that the descriptions follow the
  internationally harmonized OECD guidance.
- **Quantitative AOP development** — KEs supported by descriptions of how they can be
  measured "and the accuracy and precision with which the measurements are made", with
  KERs supported by "quantitative understanding of what magnitude and/or duration of
  change in the upstream KE is needed to evoke some magnitude of change in the
  downstream KE."

The paper is explicit that "categorization in a particular phase is neither entirely
objective, nor absolute", and that all three stages have uses for regulatory decision
support. AOPs "can evolve over time toward greater predictive sophistication (or toward
obsolescence if rejected by subsequent evidence)".

A partial AOP whose Events are not all known is explicitly useful — for setting
priorities and identifying what to test next.

Source: Villeneuve DL, Crump D, Garcia-Reyero N, Hecker M, Hutchinson TH, LaLone CA,
Landesmann B, Lettieri T, Munn S, Nepelska M, Ottinger MA, Vergauwen L, Whelan M.
*Adverse outcome pathway (AOP) development I: strategies and principles.* Toxicol Sci
2014;142(2), Table 3. [PMID:25466378](https://pubmed.ncbi.nlm.nih.gov/25466378/).

### Evidence structure

#### Weight of Evidence

Evidence in v2.8 sits at two levels, and the split is easy to misread: the KER carries
prose, while the ordinal grade sits on the AOP.

**On the KER** — five free-text fields:

| Field | Holds |
|---|---|
| `<weight-of-evidence>` | prose |
| `<biological-plausibility>` | prose |
| `<empirical-support-linkage>` | prose |
| `<quantitative-understanding>` | prose, with `<description>` and `<response-response-relationship>` |
| `<uncertainties-or-inconsistencies>` | contradicting evidence, as a first-class field |

The KER also carries `evidence-collection-strategy`, `known-modulating-factors`,
`feedforward-feedback-loops`, `time-scale`, `references`, and taxonomic applicability.

**On the AOP** — the ordinal grades and the summaries:

| Field | Is |
|---|---|
| `<evidence>`, per relationship in the AOP's KER listing | the ordinal weight-of-evidence grade |
| `<quantitative-understanding-value>` | ordinal grade |
| `<key-event-essentiality-summary>` | essentiality — assessed at AOP level, not on the KER |
| `<weight-of-evidence-summary>` | AOP-level narrative |
| `<overall-assessment>` | the Bradford-Hill-style criteria prompt: dose-response concordance, temporal concordance, strength, consistency, specificity |

The grade vocabulary is **High / Moderate / Low / Not Specified**. Counted across the
2026-08-06 export (595 AOPs, 2361 KERs):

```
<evidence>                          High 2410 | Not Specified 1975 | Moderate 1120 | Low 239
<quantitative-understanding-value>  Not Specified 1896 | Moderate 525 | Low 448 | High 444
```

Not Specified is ~34% of weight-of-evidence grades and ~57% of quantitative-understanding
grades — a large share of the deployed corpus carries no grade at all.

**Grade coverage is not evidence strength, because the grade and the evidence behind it are
stored in different places.** The grade sits on the AOP's relationship listing; the
citations and the supporting prose sit on the KER. Nothing in the serialization couples
them, so a fully graded AOP can sit on top of relationships that document nothing. Whether
a grade carries weight has to be checked against that KER's `references`,
`<empirical-support-linkage>`, and `<biological-plausibility>` fields, one relationship at
a time.

This is an observation about the deployed data, not about what the Handbook asks of AOP
developers — the caveat above applies, and the Handbook's guidance on assigning the
weight-of-evidence grade has not been read here. Worth noting for anyone who does read it
that the Handbook's three-level `Low`/`Moderate`/`High` scale keyed to evidence
("biologically plausible, but has not been shown experimentally" through "considerable
supporting evidence") belongs to **KER Biological Domain of Applicability**, a different
construct, and should not be mistaken for the criteria behind the `<evidence>` grade
counted above.

Biological plausibility is a named field on the KER, kept separate from empirical
support, so the distinction between what is plausible and what is demonstrated is
carried on individual relationships as well as on the AOP as a whole.

#### EMOD evidence classes

EMOD adds structure to AOP-Wiki fields that are currently free text. Two of its classes
carry evidence, and they attach at different points in the backbone:

- **Evidence**, on the KER — evidence for causality between two Events.
- **Observation**, on the Event — a structured stressor/exposure to biological object or
  process record, with direction, aligned to a Key Event.

An Event may be supported by several Observations. At minimum an Observation names a stressor, a
biological entity that maps to the Event, and a direction of perturbation that aligns
with it. Additional biological context details like tissue, life stage and sex, are
important to include when using AOPs to support comparative analysis of NAMs and context-
of-use evaluation.

**Citation** is a third class, and it is what Observation and Evidence instances link
to. It carries the fields a journal or book citation needs, including URL links for
DOIs and PubMed IDs, and it replaces the free-text References fields on the AOP, KER,
and Event objects. Provenance becomes a link to a record rather than a string inside
one — in the deployed v2.8 corpus, KER evidence cites inline author-year references
that are not bound to any particular claim.

Source: Hench VK, Caufield JH, Moxon SAT, O'Brien JM, Edwards SW. *AOP-Wiki EMOD 3.0:
Data Model Expansions and Content Evaluation Framework for Using Agentic AI to Improve
Integration between AOPs and New Approach Methodologies (NAMs).* arXiv
[2605.21645](https://arxiv.org/abs/2605.21645), 2026. EMOD is modelled in LinkML at
[`EHS-Data-Standards/linkml-aop`](https://github.com/EHS-Data-Standards/linkml-aop),
under active development.

---

## Points of alignment and divergence

A construct or difference is listed here only if it informs an actionable direction
for integration between AOPs and dismech, or blocks one until resolved. Constructs
that merely resemble each other across the two models are left out.

### What enables integration now

| AOP / EMOD | dismech | What it enables |
|---|---|---|
| Assay / NAM | `ExperimentalModel`, `experimental_model_type`, `namo_type` | Both sides already speak NAM and bind NAMO CURIEs — the cheapest existing bridge |
| Citation | `EvidenceItem.reference` | Resolvable PMID/DOI on both sides, so evidence can move between them without re-keying. Modelled differently: EMOD normalizes — Citation is its own record that Observation and Evidence instances link to — while dismech bundles the reference, its quote, and its polarity into one `EvidenceItem` attached directly to the claim |
| KEC Object / Process | `cell_types`, `biological_processes`, `locations` | Shared GO/HP/CL/UBERON terms make Event-to-node matching computable rather than manual |
| KEC Action | `Descriptor.modifier` | Both PATO-derived; mappable term by term |
| Experiment Type | `EvidenceItem.evidence_source` | Mappable term by term, with one named gap: no clinical or epidemiological term on the AOP side |
| Evidence (attached to the KER) | `CausalEdge.evidence` | A validated verbatim quote supporting causality between two Events — the unit a KER with no weight-of-evidence assessment needs |
| Observation (attached to the Event) | `EnvironmentalMechanismTarget.evidence`, `ExperimentalReadout.evidence` | Grounds a stressor/exposure-to-mechanism record, with direction, in a quote validated against the cited source |
| Event reuse across AOPs; consensus Events | `kb/modules/` plus `Pathophysiology.conforms_to` | Both frameworks factor a recurring mechanism out of the entries sharing it. A module node is dismech's consensus Event, and `conforms_to` declares an entry's node "an organ-specific instance of" it — the relation needed when two AOP authors name one process differently. It is deliberately not inheritance: conforming entries duplicate the content, so this checks consistency and does not merge graphs |

The module layer is the part of dismech with no counterpart named elsewhere in this table,
and it is the closest dismech comes to the AOP's stressor-agnostic posture — a module
describes a conserved process rather than one disease. Where an AOP reuses one Event across
several pathways, dismech writes the process once in `kb/modules/` and has each entry
declare conformance to it.

### What blocks integration until resolved

| Divergence | Detail |
|---|---|
| No population level | AOP's levels of biological organization include Population; `BiologicalScaleEnum` has `MOLECULAR`, `CELLULAR`, `TISSUE`, `ORGANISM` and stops at the individual |
| No taxonomic applicability | AOPs qualify Events, KERs, and whole pathways by species; dismech records species only at model level, never on a mechanism |
| Toxicokinetics inside the causal chain | ADME sits outside an AOP by design — it determines dose at the MIE, and folding it in is what makes an AOP chemical-specific. dismech chains ADME steps and key events together with nothing marking which is which |
| Stressor-agnostic vs disease-anchored | An AOP deliberately excludes the stressor so one pathway serves many chemicals; a dismech graph is anchored to a single disease and pulls the exposure in as a node |

---

## What dismech could contribute to AOP EMOD

The reverse direction: dismech constructs that address a problem the AOP schema has
not yet solved. This is outbound — a contribution to another project, not a change to
dismech.

### Evidence bound to a validated quote

`EvidenceItem.snippet` requires every evidence item to carry a verbatim quote from the
cited source, machine-checked against the fetched text; a paraphrase fails validation.
The AOP schema binds citations to a KER or an Event, but nothing binds a specific
*claim* to specific *words* in the source.

This matters most where EMOD is explicitly headed. Structuring evidence for AI-readiness
raises the question of what stops a generated claim from drifting off its source, and a
required verbatim quote is a check that runs without a human reading the paper. dismech
has run on this constraint across ~2000 entries.

---

## The Lead_Poisoning use case

<!--
TODO: write this section. `Lead_Poisoning` is declared in the frontmatter and named in
Scope as the pilot comparator, but nothing in the body currently uses it.

Material is available in AOP_EMOD_ALIGNMENT/draft-sections-1-6.md, section 3, but two
things there need rework before reuse:
  - the "terminal mechanism node cannot sit in an AOP" claim is flagged SUSPECT — it
    rests on the false premise that a Key Event requires KERs on both sides;
  - the AOP 17 comparison predates the MIE and toxicokinetics reframing. Lead absorption
    and systemic distribution are ADME and sit outside an AOP; `Inhibition of
    delta-aminolevulinic acid dehydratase` is the MIE-shaped node.

The AOP side of the comparison is expected to come from the OpenScientist network work
rather than from a single published AOP, so AOP 17 may not remain the comparator.
-->

The AOP side draws on the eight AOPs that AOP-Wiki aggregates under lead as a prototypical
stressor ([stressor 59](https://aopwiki.org/stressors/59)): AOPs 12, 499, and 500
(neurodevelopmental) and 552, 555, 556, 558, and 560 (cardiac).

### Weight of evidence across the eight lead AOPs

They are a stark worked instance of the gap between grade coverage and evidence described
under Weight of Evidence above. All 40 relationship listings across them carry a grade and
none is Not Specified — by the corpus measure there, exemplary. But of their 36 unique
KERs, **20 carry no references, no empirical-support text and no biological-plausibility
text at all, and 18 of those 20 are graded High.** The empty ones are exactly the 20
cardiac KERs — every relationship in AOPs 552, 555, 556, 558 and 560 — while the 16
neurodevelopmental KERs in AOPs 12, 499 and 500 each carry roughly 1,500–10,600 characters
of references alongside empirical-support and plausibility narrative. The grades then run
*backwards* to that documentation: all three Low grades and seven of the nine Moderates sit
on the documented neuro relationships, while the undocumented cardiac ones are almost
uniformly High. The same inversion holds one level up — AOP 12 is the only OECD-endorsed
pathway of the eight, and the only one carrying Low grades.

### Do dismech modules already hold the consensus Events?

Asking whether Events chosen by different AOP authors denote one process is a question
dismech answers in `kb/modules/`, not with `mechanistic_hypotheses` — a module node is the
generic process and `conforms_to` declares an entry's node an organ-specific instance of
it. Testing that against the **21 unique Key Events** in the five cardiac lead AOPs, with
`cardiac_ion_channel_repolarization` and `cardiomyopathy_maladaptive_remodeling` as the
candidate modules:

| KE | Event | Module node | Fit |
|---|---|---|---|
| 698 | Altered, Action Potential | Altered Action Potential and Calcium Handling | yes |
| 1961 | Prolongation of Action Potential Duration | Altered Action Potential and Calcium Handling | yes — module names long QT physiology |
| 1962 | Prolongation of QT interval | Altered Action Potential and Calcium Handling | yes |
| 389 | Increased, Intracellular Calcium overload | Altered Action Potential and Calcium Handling | yes — `calcium ion transport` |
| 2289 | Hyperphosphorylation of RyR2 | Altered Action Potential and Calcium Handling | yes — module names SR calcium-release destabilization |
| 2283 | Increased early premature depolarizations | Arrhythmogenic Substrate and Triggered Activity | yes — module names EADs |
| 1963 | Torsades de Pointes | Ventricular Tachyarrhythmia | yes — module names torsade |
| 1106 | Occurrence, cardiac arrhythmia *(AO)* | Arrhythmogenic Substrate and Triggered Activity | yes |
| 2291 | Slowed Heart Rate | Sinoatrial Node Pacemaker Dysfunction | yes — module names sinus bradycardia and HCN4 |
| 2292 | Altered Cardiac Electrical Conduction | Sinoatrial Node Pacemaker Dysfunction | yes |
| 1321 | Increased, intracellular sodium | Altered Action Potential and Calcium Handling | partial — module names late sodium current, not Na⁺ accumulation |
| 2287 | Impaired Sodium-Calcium Exchange | Arrhythmogenic Substrate and Triggered Activity | partial — NCX appears only in the DAD description |
| 2281 | Increased uncoordinated cardiac contraction | Ventricular Tachyarrhythmia | partial |
| 1532 | Decrease, Cardiac contractility | Progressive Contractile Dysfunction | endpoint only — see below |
| 1535 | Heart failure *(AO)* | Structural Cardiac Impairment and Heart Failure | endpoint only — see below |
| 1529 | Blockade, L-Type Calcium Channels *(MIE)* | — | none |
| 593 | Inhibition, ERG voltage-gated potassium channel *(MIE)* | — | none |
| 1562 | Decreased Na/K ATPase activity *(MIE)* | — | none |
| 2288 | Phosphodiesterase inhibition *(MIE)* | — | none |
| 2290 | Inhibition of Funny current (If) *(MIE)* | — | none |
| 693 | Increased, cyclic adenosine monophosphate | — | none |

**Ten of 21 map cleanly and three partially, and the eight that do not fall into three
groups that each say something different.**

*All five MIEs are unmatched, and for one reason.* **The electrophysiology module starts
with a genetic cause, while an AOP starts with the damage itself — so a chemical that does
the same damage has nothing to attach to.** `cardiac_ion_channel_repolarization` begins at
`Cardiac Ion-Channel or Calcium-Handling Variant`, described as "a pathogenic germline
variant alters a cardiac ion channel". AOP 552 begins at `Blockade, L-Type Calcium Channels`
and stays silent on what did the blocking, which is what lets one pathway serve many
chemicals. A calcium channel that is not working produces the same altered action potential
whether a mutation broke it or lead is sitting in it, so everything downstream matches — but
lead cannot conform to a node that asserts the cause was a mutation. All five unmatched MIEs
are electrophysiologic, so all five fall in this module's territory.

The claim is specific to that module, **not** a property of the module layer, and not even
true of the other cardiac module here. `cardiomyopathy_maladaptive_remodeling` opens at
`Primary Cardiomyocyte Insult`, which is explicitly etiology-agnostic: a variant "in
inherited cardiomyopathies", but "in acquired and secondary cardiomyopathies … a hemodynamic
(pressure or volume overload), metabolic, toxic, or inflammatory stress". A chemical insult
is named in the node itself. Other modules open exactly where an AOP would —
`drug_induced_nephrotoxicity` at "Nephrotoxic Drug Exposure and Tubular Uptake",
`drug_induced_liver_injury` at "Reactive Drug Metabolite Formation",
`diabetic_vascular_complications` at "Chronic Hyperglycemia". dismech expresses chemical
entry points routinely; the module covering lead's cardiac electrophysiology was written for
inherited channelopathy and does not.

*The contractility arm reaches a matching endpoint by a different route.* KE1532 → KE1535
asserts calcium overload depresses contractility and produces heart failure directly.
`cardiomyopathy_maladaptive_remodeling` reaches the same outcome through neurohormonal
activation and ventricular remodeling, and `cardiac_ion_channel_repolarization` explicitly
scopes itself to "structurally normal hearts". So the endpoints align while the mechanism
between them does not — the AOPs compress a chain the module expands, or assert an acute
pump failure the module does not model.

*The cAMP/PDE arm is simply absent* from both modules.

#### The neurodevelopmental side scores worse, and for a different reason

Repeating the exercise on the **14 unique Key Events** in AOPs 12, 499, and 500, against
`glutamate_excitotoxicity`, `synaptic_vesicle_cycle`, `mitochondrial_dysfunction`, and
`excitatory_synapse_scaffold_disruption`:

| KE | Event | Module node | Fit |
|---|---|---|---|
| 1339 | Increase, intracellular calcium | Glutamate Receptor Overactivation and Calcium Overload | yes |
| 2151 | Disruption, neurotransmitter release | Neurotransmitter Release Failure and Synaptic Transmission Deficit | yes |
| 177 | Increase, Mitochondrial dysfunction | Mitochondrial Dysfunction and Oxidative Stress | yes |
| 1115 | Increase, Reactive oxygen species | Mitochondrial Dysfunction and Oxidative Stress | yes |
| 55 | Increase, Cell injury/death | Excitotoxic Neuronal Death | partial — module's death is excitotoxic specifically |
| 1262 | Apoptosis | Excitotoxic Neuronal Death | partial — same |
| 352 | N/A, Neurodegeneration *(AO)* | Excitotoxic Neuronal Death | partial — generic outcome against a specific one |
| 341 | Impairment, Learning and memory *(AO)* | Neurodevelopmental Phenotypic Output | partial — from `excitatory_synapse_scaffold_disruption` |
| 201 | Binding of antagonist, NMDA receptors *(MIE)* | — | none — sign-inverted, see below |
| 195 | Inhibition, NMDARs | — | none — sign-inverted |
| 52 | Decreased, Calcium influx | — | none — sign-inverted |
| 381 | Reduced levels of BDNF | — | none — no module covers BDNF |
| 188 | Neuroinflammation | — | none — appears only fused into organ-specific composite nodes |
| 2146 | Activation of MEK/ERK1/2 *(MIE)* | — | none — MAPK nodes exist but all are proliferation- or fibrosis-framed |

**Four of 14 clean and four partial** — worse than the cardiac side, despite these being the
well-documented AOPs. Documentation quality and module coverage turn out to be independent.

The reason is worth recording, because it is not the entry-point problem again. Three of the
six misses fail together because **dismech's only glutamate module is the mirror image of
lead's mechanism**. `glutamate_excitotoxicity` is built end to end on *over*activation —
"Excessive Glutamatergic Stimulation and Impaired Glutamate Clearance", "Glutamate
Receptor Overactivation and Calcium Overload" — while lead's neurodevelopmental MIE is NMDAR *antagonism*, giving decreased
calcium influx. The sign is inverted at every node, so KE52 cannot conform to a node whose
name asserts overload even though `modifier` could carry the direction.

This is the same directional split the OpenScientist report hit as its Finding 9 and
handled by keeping KE52 out of the merge. Finding it independently on the dismech side
establishes it as a real gap rather than an AOP-authoring artifact: the KB has no module for
developmental hypo-activation of glutamatergic signalling. Note the split runs *inside* the
neuro cluster — KE1339 (increase, from the MEK/ERK arm of AOPs 499 and 500) conforms cleanly
while KE52 (decrease, from AOP 12) cannot, so no single calcium node holds both.

The result cuts both ways. Two-thirds of the cardiac Events already have a home in modules
written for inherited arrhythmia and cardiomyopathy, with no lead in view — which is the
Event-reuse property that makes AOP networks work, arrived at independently. But
conformance is consistency-checking, not inheritance, so this yields a checkable claim that
two Events are instances of one process and **not** a merged network render. The graph half
of the question stays a query over the XML export.

*The rest is not yet written.* A consensus network from OpenScientist was the original plan
for the AOP side; whether it is still the right comparator is open, given the assessment
recorded in
[`AOP_EMOD_ALIGNMENT/assessments/`](AOP_EMOD_ALIGNMENT/assessments/openscientist-assessment-by-claude-code.yaml).

---

## Next Steps

The end goal this project leads to is **dismech-derived AOPs** — dismech pathographs as
source material for new AOPs, and dismech evidence as support for existing ones. Two
directions, in order of how close they are.

**Enriching existing AOPs** is the nearer one, and it needs no structural change on
either side. A dismech `EvidenceItem` carries a resolvable identifier plus a quote
validated against the source, which is close to what a KER with no weight-of-evidence
assessment needs — and Not Specified accounts for ~34% of weight-of-evidence grades and
~57% of quantitative-understanding grades in the deployed corpus.

**Seeding new AOPs** is the further one, and the divergences above are what stand in the
way: the toxicokinetic steps in a dismech chain have to be separated from the key
events, species applicability and a population level have no dismech counterpart, and a
disease-anchored graph has to be cut stressor-agnostic before it is an AOP.

<!--
## Not yet included

Drafted material held in
[`AOP_EMOD_ALIGNMENT/draft-sections-1-6.md`](AOP_EMOD_ALIGNMENT/draft-sections-1-6.md),
deliberately not on this page. Listed so the page's coverage is legible rather than
implied.

- **Enriching canonical evidence for existing AOPs.** The direction with the clearest
  target: Not Specified accounts for ~34% of weight-of-evidence grades and ~57% of
  quantitative-understanding grades, and a dismech `EvidenceItem` is close to what
  filling one needs.
- **Value-level mappings.** Term-by-term tables for the three enum pairs the comparison
  table calls mappable: LoBO to `BiologicalScaleEnum`, Experiment Type to
  `EvidenceSourceEnum`, and KEC Action to `ModifierEnum`.
- **Further EMOD classes.** Assay/NAM, Experiment Type, and Causal Agent, plus
  Biological Target Family, Harmonized Events and AOPs, Candidate Event Merger, and the
  Event Integration Score.
- **Further dismech contributions to EMOD.** `supports` polarity including `REFUTE`, the
  two evidence layers on a model link, `causal_link_type`, `hypothesis_groups`, and
  `HUMAN_CLINICAL` as an evidence source.
- **EMOD lineage and process detail.** Prototype history, the roll-up principle, the
  status of the Evidence class, and sources not yet read. Repo-side context rather than
  page content.

Two of the three directions named in this project's description — dismech enriched by
AOPs, and dismech seeding new AOPs — are represented here only as pointers.
-->
