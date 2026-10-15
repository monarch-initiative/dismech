---
title: Autonomous Labs Project
status: IN_PROGRESS
description: 'DisMech plus OpenScientist can become an auditable experiment-suggestion layer for disease biology: DisMech stores a computable pathograph, OpenScientist searches and ranks mechanistic gaps, and a protocol layer turns selected gaps into standardized experiments that can be reviewed by humans and...'
diseases:
- Ewing_Sarcoma
- Prolidase_Deficiency
---

# Autonomous Labs Project

## Working Thesis

DisMech plus OpenScientist can become an auditable experiment-suggestion layer
for disease biology: DisMech stores a computable pathograph, OpenScientist
searches and ranks mechanistic gaps, and a protocol layer turns selected gaps
into standardized experiments that can be reviewed by humans and executed by
university automation cores or cloud labs.

This is not a claim that AI should autonomously invent therapies. The useful
near-term claim is narrower: AI can maintain a disease-mechanism graph, identify
weak causal edges, propose bounded experiments, and package those experiments
into reproducible, machine-readable protocols.

## UNC Lineberger Anchor

The UNC Lineberger "Priming the pump for new cancer treatments" story is a good
case study because the named investigators cover the whole loop:

| Researcher | DisMech/OpenScientist role | Automation relevance |
| --- | --- | --- |
| Ian Davis | Disease-mechanism graph for Ewing sarcoma, especially EWS-FLI1 chromatin rewiring | Defines causal nodes, models, and chromatin readouts |
| Samantha Pattenden | Chromatin assay development and screening | HT-FAIRE converts chromatin accessibility into an automated plate assay |
| David Drewry | Chemical probe and medicinal chemistry infrastructure | Supplies annotated compound libraries and probe optimization logic |
| Pengda Liu | Protein-modification and targeted-degradation biology | Provides degrader-style perturbations such as TF-PROTAC concepts |
| Lindsey James | Chemical biology of chromatin regulators and degraders | Shows how degrader discovery can be tied to selectivity and phenotype assays |

## Ewing Sarcoma Demonstrator

The strongest disease-specific demonstration is an Ewing chromatin-accessibility
loop:

1. DisMech encodes the Ewing pathograph: EWS-FLI1 fusion, GGAA enhancer
   reprogramming, ETV6 counter-regulation, NuRD/CHD4 repression, core regulatory
   circuitry, replication stress, and STAG2 modifiers.
2. OpenScientist identifies a concrete gap: which EWS-FLI1-dependent chromatin
   states are causal dependencies rather than passenger accessibility changes?
3. The platform proposes a standardized experiment: automated HT-FAIRE,
   ATAC-qPCR, or low-input ATAC-seq across Ewing models, perturbing epigenetic
   compounds, degraders, EWS-FLI1 controls, and ETV6 controls.
4. A protocol compiler emits a reviewed protocol compatible with laboratory
   automation standards or a university cloud-lab/core facility.
5. Results return as evidence: hit compounds, chromatin-state changes,
   transcriptional rescue, toxicity separation, and updated pathograph edges.

The corresponding curation target in `kb/disorders/Ewing_Sarcoma.yaml` is
`gap_ewing_chromatin_reversal_screen`.

## Protocol And Execution Layer

Candidate execution standards and systems:

- LabOP: protocol representation intended to exchange experimental protocols
  and translate them into lab-specific instructions.
- Autoprotocol / cloud-lab APIs: practical execution targets for liquid handling,
  plate-based assays, sequencing preparation, and compound screens.
- SiLA 2: open lab-automation interoperability standard for instruments and
  services.
- Academic cloud labs: CMU/Emerald Cloud Lab is the clean public precedent for a
  remote-controlled academic lab substrate.
- Coscientist: a proof of principle that LLM agents can use documentation,
  APIs, liquid handlers, and cloud-lab interfaces to plan and execute chemistry
  workflows under constrained conditions.

## Commercial Cloud-Lab Catalogues: What Is Actually Orderable

The execution layer above lists candidate standards. This section records what a
specific commercial catalogue turned out to contain, because the answer changed
which demonstrator is reachable.

Ginkgo Cloud Lab (`https://cloud.ginkgo.bio/protocols`, read 2026-10-01)
publishes 18 protocols. They are almost entirely **protein biochemistry**:
cell-free expression validation and optimisation, HiBiT and A280
quantification, Strep-tag and His-tag purification, LabChip purity, a SYPRO
Orange thermal shift assay, Echo-MS detection of an enzymatic reaction,
minibinder expression with SPR target onboarding, IVT mRNA/circRNA synthesis,
E. coli and Pichia expression, and assay-onboarding services. Input is
typically DNA sequences submitted as a CSV.

Commercial terms — price, turnaround, throughput — are deliberately recorded
nowhere in this repository. They change with no signal that they have, and
this project is not a reseller's catalogue; a curator settles them with the
provider when something is actually ordered.

**The Ewing chromatin demonstrator above is not executable on this catalogue.**
Nothing in it does chromatin accessibility, cell-line culture, or a
sequencing readout, so HT-FAIRE, ATAC-qPCR and low-input ATAC-seq are all out
of scope; that loop needs the UNC automation core it was designed around. This
is not a defect in the demonstrator — it is a statement about which rung of the
execution layer each catalogue serves. A commercial cloud lab of this shape
reaches **protein-level** mechanism questions: variant functional impact,
expression, folding, binding, and enzyme turnover.

So the first entry curated against this catalogue is a protein-biochemistry
gap rather than the Ewing one:
`Prolidase_Deficiency` → `pd_allele_panel_abundance_stability_catalysis`
(see `Experiment.executable_protocols`, and the CLAUDE.md section of the same
name). Clinical practice reports one "residual prolidase activity" figure per
patient, measured in erythrocyte or fibroblast lysate, and the entry's open gap
records that severity is uncoupled from it. Three catalogue protocols decompose
that figure into abundance (HiBiT), folding (thermal shift) and catalysis
(Echo-MS on an imidodipeptide substrate), which is a decomposition the clinical
assay cannot make. That amount-versus-activity distinction is the axis deferred
in design decisions §12, which names the residual-activity genotype-severity
question among its motivating cases.

Open questions before this is a closed loop:

- **There is no public submission API.** The catalogue is served as a storefront;
  ordering appears to be a commercial transaction, not an API call. Any claim
  that a plan can be "submitted programmatically" is unverified, and the final
  hop is currently a human.
- **Scoping a panel needs a conversation, not the catalogue.** The published
  prices do not state what they are charged per, and several protocols give no
  maximum panel size, so the cost and scheduling of a real submission cannot be
  read off the listing at all. This is part of why the schema does not try to
  carry them.
- **Method validation is per-substrate.** Echo-MS is open-access in principle, but
  whether a given substrate/product pair is validated is a separate question, and
  the provider sells method onboarding as its own line item.

## Pre-Execution Verification

`ExecutableProtocol` records that a run is *possible*. It deliberately says
nothing about whether a particular run should proceed, which is the gate the
section below is about. The candidate mechanism for that gate is
[`clauz3`](https://github.com/normalform-ai/clauz3) with its
[autolabs domain library](https://github.com/normalform-ai/clauz3-tools-autolabs):
an agent-authored plan calls trusted side-effecting functions, carries
`@clauz3.guarantee(...)` decorators, and `clauz3 prove` discharges those
guarantees with Z3 *before* anything executes. Its existing `lims` domain
already carries the contract shapes this project needs — instrument
allowlists, cumulative budget bounds, and a `no_hazard_sequence` biosecurity
contract on the oligo-ordering flow, which is exactly the step a variant-panel
experiment reaches when its DNA templates are ordered.

That work is not in this repository and is not a dependency of the schema
block: a cloud-lab contract domain would be a change to
`clauz3-tools-autolabs`, scoped there and provable against mock effects with
no provider access at all. Recorded here so the division is explicit —
dismech states what a gap would take; the verifier decides whether a plan
honouring that is allowed to run; neither is the human review this project
requires before either.

## Safety And Governance

The platform should keep human review as a hard gate before execution. Required
checks include PI approval, institutional biosafety review where relevant,
model-system and reagent provenance, protocol versioning, dose/exposure bounds,
biosecurity screening, data-management plans, and curator review before any new
result updates the knowledge base.

## Near-Term KB Ideas

- Add disease-level knowledge gaps that include proposed experiments, modeled
  after the Parkinson disease isogenic hPSC example.
- Prefer experiments that map directly to pathograph edges and have clear
  decision criteria.
- For Ewing sarcoma, prioritize high-throughput chromatin assays because they
  connect a canonical mechanism, an existing Davis/Pattenden automated assay,
  and a cloud-lab-compatible perturbation format.
- Treat OpenScientist reports as provenance for hypothesis generation, but cite
  primary papers in disease YAML evidence whenever possible.

## Sources

- UNC Lineberger: https://unclineberger.org/news/priming-the-pump-for-new-cancer-treatments/
- Pattenden et al. HT-FAIRE Ewing screen: PMID:26929321
- Patel et al. Davis lab EWS-FLI chromatin retargeting: PMID:22086061
- CMU academic cloud lab: https://www.cmu.edu/news/stories/archives/2021/august/first-academic-cloud-lab.html
- Coscientist: https://www.nature.com/articles/s41586-023-06792-0
- LabOP: https://github.com/Bioprotocols/labop
- SiLA: https://sila-standard.com/standards/
