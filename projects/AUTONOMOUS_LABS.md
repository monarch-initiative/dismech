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
