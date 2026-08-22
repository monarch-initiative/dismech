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

<!--
TODO: this section currently covers only the two EMOD evidence classes. The v2.8 data
model already carries a substantial evidence apparatus that belongs here too, including:

  - Weight of Evidence. Referenced once in the comparison table but never introduced.
    The KER carries free-text <weight-of-evidence>, <biological-plausibility>,
    <emperical-support-linkage> (note the schema's own typo), <quantitative-understanding>
    and <uncertainties-or-inconsistencies>; the ordinal grade sits separately on the AOP's
    relationship listing, as <evidence> and <quantitative-understanding-value>, with the
    vocabulary High / Moderate / Low / Not Specified. Counted across the 2026-08-06 export
    (595 AOPs, 2361 KERs), Not Specified is ~34% of weight-of-evidence grades and ~57% of
    quantitative-understanding grades.
  - Key event essentiality, assessed at AOP level as <key-event-essentiality-summary>,
    not on the KER.
  - <overall-assessment>, which carries the Bradford-Hill-style criteria prompt.
  - Citation practice in the deployed corpus: inline author-year references, with a
    separate <references> element, not identifiers bound to a specific claim.

Source material is in AOP_EMOD_ALIGNMENT/draft-sections-1-6.md, section 1.
-->

Biological plausibility is a named field on the KER, kept separate from empirical
support, so the distinction between what is plausible and what is demonstrated is
carried on individual relationships as well as on the AOP as a whole.

EMOD adds structure to AOP-Wiki fields that are currently free text. Two of its classes
carry evidence, and they attach at different points in the backbone:

- **Evidence**, on the KER — evidence for causality between two Events.
- **Observation**, on the Event — a structured stressor/exposure to biological object or
  process record, with direction, aligned to a Key Event.

An Event may have several Observations. At minimum an Observation names a stressor, a
biological entity that maps to the Event, and a direction of perturbation that aligns
with it.

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
| Citation | `EvidenceItem.reference` | Resolvable PMID/DOI on both sides, so evidence can move between them without re-keying |
| KEC Object / Process | `cell_types`, `biological_processes`, `locations` | Shared GO/HP/CL/UBERON terms make Event-to-node matching computable rather than manual |
| KEC Action | `Descriptor.modifier` | Both PATO-derived; mappable term by term |
| Experiment Type | `EvidenceItem.evidence_source` | Mappable term by term, with one named gap: no clinical or epidemiological term on the AOP side |
| Evidence (attached to the KER) | `CausalEdge.evidence` | A validated verbatim quote supporting causality between two Events — the unit a KER with no weight-of-evidence assessment needs |
| Observation (attached to the Event) | `EnvironmentalMechanismTarget.evidence`, `ExperimentalReadout.evidence` | Grounds a stressor/exposure-to-mechanism record, with direction, in a quote validated against the cited source |

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

*Not yet written.* The AOP side of this use case will draw on an AOP network with
consensus nodes, under development in OpenScientist.

