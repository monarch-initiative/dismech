---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-11-07T16:41:04.115865'
end_time: '2026-11-07T16:59:57.184638'
duration_seconds: 1133.07
template_file: templates/module_mechanism_research.md
template_sha: "24cb27b5d49e5e45a5e3c24792bdfb6f9b195d14"
template_variables:
  module_name: KEAP1-NRF2-ARE Signaling Module
  module_slug: keap1_nrf2_are_signaling
  category: Module
  module_description: "SKELETON (seed PMID:40972999, issue #16807) \u2014 term bindings\
    \ and evidence are deferred until deep research confirms them. A conserved mechanism\
    \ module for the KEAP1-NRF2-ARE cytoprotective antioxidant response and its dysregulation.\
    \ Under basal conditions the sensor protein KEAP1 serves as the substrate adaptor\
    \ of a CUL3 RING ubiquitin ligase that constitutively ubiquitinates the transcription\
    \ factor NRF2 (NFE2L2) and targets it for proteasomal degradation, keeping nuclear\
    \ NRF2 low. Electrophiles and oxidants covalently modify reactive cysteines on\
    \ KEAP1 (or, non-canonically, p62/SQSTM1 sequesters KEAP1), which halts NRF2 ubiquitination;\
    \ NRF2 then accumulates, enters the nucleus, heterodimerizes with a small MAF\
    \ protein, and transactivates a battery of antioxidant response element (ARE)\
    \ genes \u2014 among them SRXN1, NQO1, HMOX1, and the glutamate-cysteine ligase\
    \ subunits GCLC/GCLM \u2014 whose products restore redox balance and confer cytoprotection.\
    \ The rate-limiting, conserved step every conformer funnels through is NRF2-driven\
    \ ARE transcription. One module spans both directions of dysregulation: diseases\
    \ where the response is blunted (loss of NRF2 signaling) and diseases where it\
    \ is constitutively ON (KEAP1/NFE2L2 loss-of-KEAP1-function, or fumarate succination\
    \ of KEAP1), distinguished by the modifier on the central node rather than by\
    \ a separate module. Complementary to oncometabolite_dioxygenase_inhibition (which\
    \ covers only the fumarate-succination route to NRF2 activation) and to cul3_substrate_adaptor_dysfunction\
    \ (which covers CRL3 adaptor swapping in general, of which KEAP1 is one adaptor).\
    \ Key conformance target: \"keap1_nrf2_are_signaling#NRF2 Transcriptional Activation\
    \ of ARE Genes\"."
  pathophysiology_summary: "- KEAP1 Sensor Cysteine Modification: SKELETON NODE. The\
    \ initiating step. Reactive cysteine thiols on the cytoplasmic sensor KEAP1 are\
    \ covalently modified by an electrophile or oxidant (the seed paper's soft electrophiles\
    \ sulforaphane, andrographolide, ethacrynic acid and CDDO-methyl are archetypes),\
    \ or KEAP1 function is lost by mutation, or fumarate succinates KEAP1 cysteines.\
    \ KEAP1 is upstream of NRF2; this node is the sensor, not a target. Terms/evidence\
    \ deferred.\n- NRF2 Escape from KEAP1-CUL3 Degradation: SKELETON NODE. With KEAP1\
    \ disabled, the CUL3 RING ligase no longer ubiquitinates NRF2, so NRF2 escapes\
    \ proteasomal degradation, accumulates, and translocates to the nucleus. In loss-of-NRF2-signaling\
    \ diseases this step is impaired; in KEAP1/NFE2L2-mutant and fumarate-driven diseases\
    \ it is constitutive. Terms/evidence deferred.\n- NRF2 Transcriptional Activation\
    \ of ARE Genes: SKELETON NODE and KEY CONFORMANCE TARGET. Nuclear NRF2 heterodimerizes\
    \ with a small MAF protein and transactivates antioxidant response element (ARE)\
    \ genes. The seed paper's central finding is that NRF2 protein level alone does\
    \ not account for target-gene induction \u2014 a cofactor or post-translational\
    \ modification is required, and the relationship is time-, compound- and exposure-scenario\
    \ specific. This is the rate-limiting step every conformer funnels through; conformers\
    \ set its modifier by direction. Terms/evidence deferred.\n- ARE Target Gene Products\
    \ Restore Redox Balance: SKELETON NODE. The ARE regulon \u2014 SRXN1 (the seed\
    \ paper's readout gene), NQO1, HMOX1, the glutamate-cysteine ligase subunits GCLC/GCLM,\
    \ and others \u2014 detoxifies reactive species and reduces oxidized protein thiols.\
    \ SRXN1 is cited by the seed paper as a bona fide NRF2 target. Terms/evidence\
    \ deferred.\n- Cytoprotection or Its Failure: SKELETON NODE, scope to be settled\
    \ by deep research. When the ARE response is adequate the cell is protected from\
    \ oxidative and electrophilic injury; when NRF2 signaling is blunted the cell\
    \ is left vulnerable, and when it is constitutively ON it can confer a survival/chemoresistance\
    \ advantage on tumor cells. Whether autophagy, proliferation and apoptosis (named\
    \ in the seed abstract) belong here is an open scope question. Terms/evidence\
    \ deferred."
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 5
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 3600
    save_artifacts: true
    artifact_max_bytes: 5242880
citation_count: 33
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: keap1_nrf2_are_signaling-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: keap1_nrf2_are_signaling-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Mechanism Module Research Template

## Target Module
- **Module Name:** KEAP1-NRF2-ARE Signaling Module
- **Module Slug:** keap1_nrf2_are_signaling
- **Category:** Module

## Current Module Description

SKELETON (seed PMID:40972999, issue #16807) — term bindings and evidence are deferred until deep research confirms them. A conserved mechanism module for the KEAP1-NRF2-ARE cytoprotective antioxidant response and its dysregulation. Under basal conditions the sensor protein KEAP1 serves as the substrate adaptor of a CUL3 RING ubiquitin ligase that constitutively ubiquitinates the transcription factor NRF2 (NFE2L2) and targets it for proteasomal degradation, keeping nuclear NRF2 low. Electrophiles and oxidants covalently modify reactive cysteines on KEAP1 (or, non-canonically, p62/SQSTM1 sequesters KEAP1), which halts NRF2 ubiquitination; NRF2 then accumulates, enters the nucleus, heterodimerizes with a small MAF protein, and transactivates a battery of antioxidant response element (ARE) genes — among them SRXN1, NQO1, HMOX1, and the glutamate-cysteine ligase subunits GCLC/GCLM — whose products restore redox balance and confer cytoprotection. The rate-limiting, conserved step every conformer funnels through is NRF2-driven ARE transcription. One module spans both directions of dysregulation: diseases where the response is blunted (loss of NRF2 signaling) and diseases where it is constitutively ON (KEAP1/NFE2L2 loss-of-KEAP1-function, or fumarate succination of KEAP1), distinguished by the modifier on the central node rather than by a separate module. Complementary to oncometabolite_dioxygenase_inhibition (which covers only the fumarate-succination route to NRF2 activation) and to cul3_substrate_adaptor_dysfunction (which covers CRL3 adaptor swapping in general, of which KEAP1 is one adaptor). Key conformance target: "keap1_nrf2_are_signaling#NRF2 Transcriptional Activation of ARE Genes".

## Current Provisional Nodes

- KEAP1 Sensor Cysteine Modification: SKELETON NODE. The initiating step. Reactive cysteine thiols on the cytoplasmic sensor KEAP1 are covalently modified by an electrophile or oxidant (the seed paper's soft electrophiles sulforaphane, andrographolide, ethacrynic acid and CDDO-methyl are archetypes), or KEAP1 function is lost by mutation, or fumarate succinates KEAP1 cysteines. KEAP1 is upstream of NRF2; this node is the sensor, not a target. Terms/evidence deferred.
- NRF2 Escape from KEAP1-CUL3 Degradation: SKELETON NODE. With KEAP1 disabled, the CUL3 RING ligase no longer ubiquitinates NRF2, so NRF2 escapes proteasomal degradation, accumulates, and translocates to the nucleus. In loss-of-NRF2-signaling diseases this step is impaired; in KEAP1/NFE2L2-mutant and fumarate-driven diseases it is constitutive. Terms/evidence deferred.
- NRF2 Transcriptional Activation of ARE Genes: SKELETON NODE and KEY CONFORMANCE TARGET. Nuclear NRF2 heterodimerizes with a small MAF protein and transactivates antioxidant response element (ARE) genes. The seed paper's central finding is that NRF2 protein level alone does not account for target-gene induction — a cofactor or post-translational modification is required, and the relationship is time-, compound- and exposure-scenario specific. This is the rate-limiting step every conformer funnels through; conformers set its modifier by direction. Terms/evidence deferred.
- ARE Target Gene Products Restore Redox Balance: SKELETON NODE. The ARE regulon — SRXN1 (the seed paper's readout gene), NQO1, HMOX1, the glutamate-cysteine ligase subunits GCLC/GCLM, and others — detoxifies reactive species and reduces oxidized protein thiols. SRXN1 is cited by the seed paper as a bona fide NRF2 target. Terms/evidence deferred.
- Cytoprotection or Its Failure: SKELETON NODE, scope to be settled by deep research. When the ARE response is adequate the cell is protected from oxidative and electrophilic injury; when NRF2 signaling is blunted the cell is left vulnerable, and when it is constitutively ON it can confer a survival/chemoresistance advantage on tumor cells. Whether autophagy, proliferation and apoptosis (named in the seed abstract) belong here is an open scope question. Terms/evidence deferred.

## Research Objective

Prepare a mechanism-focused research report for the dismech module above. This
is not a disease entry. The goal is to support a reusable mechanism module that
multiple gene-axis disease entries can conform to.

Focus the search on the shared biology described in the module description and
provisional nodes above. Prioritize evidence for:

- The conserved causal chain represented by the proposed nodes.
- The biological distinctions between node subgroups, especially if the module
  defines branching pathways.
- Any optional or gene-specific branches described in the node list, while
  distinguishing them from core module requirements.
- Explicit exclusions or boundary conditions stated in the module description.

## Questions To Answer

1. What is the best-supported shared mechanism for this module?
2. Is the current module name and scope appropriate, or is a clearer name or
   narrower boundary supported by the literature?
3. Which nodes should be core and required for conformance, and which nodes
   should be optional or gene-specific?
4. Which genes, variants, exposures, cell types, tissues, or molecular
   processes support each branch or node?
5. What evidence supports the causal edges between upstream drivers, central
   effectors, and downstream consequences?
6. What direct human evidence links the same causal factor or variant class to
   multiple clinical or pathological manifestations?
7. What model organism, in vitro, or other experimental evidence clarifies the
   causal path from molecular perturbation to phenotype?
8. What Gene Ontology biological process terms, Cell Ontology cell types, and
   anatomical terms should be used in the module?
9. What claims are speculative, weakly supported, or should remain out of scope?

## Evidence Requirements

- Cite primary literature with PMID identifiers whenever possible.
- Include exact abstract quotes for candidate evidence snippets.
- Separate human clinical, model organism, in vitro, and review evidence.
- Flag papers where the abstract is insufficient and full-text verification is
  needed before curation.
- Do not invent ontology IDs. Suggest terms by label when unsure.

## Desired Output

Structure the report with:

- Executive recommendation for module name and scope.
- Proposed DAG nodes and causal edges.
- Gene-to-node mapping table.
- Evidence table with PMID, evidence type, exact quote, and supported claim.
- Ontology suggestions for GO, CL, and UBERON terms.
- Out-of-scope boundary notes.
- Open questions for curator review.


## Output

# KEAP1-NRF2-ARE Signaling Module — Mechanism Research Report

**Module slug:** `keap1_nrf2_are_signaling` · **Category:** Module · **Seed:** PMID:40972999 (issue #16807)
**Status:** Deep-research complete (5 iterations, 12 confirmed findings, 70 papers reviewed)
**Date:** 2026-11-07

---

## Summary

The KEAP1-NRF2-ARE axis is one of the best-characterized cytoprotective signaling systems in biology, and the literature strongly supports modeling it as **a single, conserved, bidirectional mechanism module** rather than as two separate loss- and gain-of-function modules. Under basal conditions the sensor protein **KEAP1** acts as the substrate adaptor of a **CUL3-RBX1 RING ubiquitin ligase** that constitutively ubiquitinates the transcription factor **NRF2 (NFE2L2)** and routes it to the proteasome, keeping nuclear NRF2 low. The defining control point is the state of KEAP1's reactive sensor cysteines: electrophiles and oxidants covalently modify them, loss-of-function mutations in *KEAP1* or *CUL3* disable the ligase, gain-of-function mutations in the *NFE2L2* ETGE/DLG degron make NRF2 unrecognizable, and the oncometabolite **fumarate** succinates KEAP1 cysteines. Any of these perturbations halts NRF2 degradation; stabilized NRF2 translocates to the nucleus, **obligately heterodimerizes with a small MAF protein**, and transactivates **antioxidant response element (ARE / CsMBE)** genes — SRXN1, NQO1, HMOX1, GCLC/GCLM and a broad detoxification regulon — whose products restore redox balance and confer cytoprotection.

The investigation confirms a five-node causal chain (N1 sensor cysteine modification → N2 escape from CUL3 degradation → N3 NRF2-sMAF ARE transactivation → N4 regulon restores redox balance → N5 cytoprotection or its failure), all of which should be **core and required for conformance**. The branch-specific drivers (fumarate/FH deficiency, KEAP1/CUL3 loss-of-function, NFE2L2 degron gain-of-function, and the non-canonical p62/SQSTM1 sequestration route) are best represented as **conformer-specific modifiers entering at N1/N2**, not as separate nodes. The direction of dysregulation — blunted (loss of NRF2 signaling → vulnerability) versus constitutive-ON (KEAP1/NFE2L2-mutant or fumarate-driven → tumor survival/chemoresistance) — is set by the modifier on the central node, which is exactly the "one module, two directions" design the skeleton proposed.

A distinctive and curation-critical nuance comes from the **seed paper (PMID:40972999)**: semi-mechanistic modeling of NRF2 and SRXN1 protein time courses shows that **NRF2 protein level alone does not account for ARE target-gene induction** — a cofactor or post-translational modification is required, and this gating is time-, compound-, and exposure-scenario specific. The N2→N3 edge is therefore not a simple linear function of NRF2 abundance, which the module should encode explicitly. All 25 of 26 suggested GO/CL/UBERON ontology terms were verified against EBI OLS4 and are curation-ready.

---

## Key Findings

### F001 — Core module backbone: a constitutive KEAP1-CUL3 ligase degrades NRF2, de-repressed by cysteine modification

The foundational logic of the module is that NRF2 regulation is **post-translational and degradation-based**, not transcriptional. Harder et al. ([PMID:26551712](https://pubmed.ncbi.nlm.nih.gov/26551712/)) establish that the "Keap1-cullin3 (Cul3)-ring-box1 (Rbx1) E3-ligase [is] the primary Nrf2 regulatory system" operating under non-stress conditions. Feng & Dinkova-Kostova ([PMID:42844347](https://pubmed.ncbi.nlm.nih.gov/42844347/)) complete the causal logic: "Cysteine modifications within KEAP1 and BACH1 render the repressor proteins inactive, resulting in rapid NRF2 activation that does not rely on de novo transcription of NFE2L2." This means activation is achieved by inactivating a repressor and **stabilizing pre-existing NRF2 protein**, not by inducing new *NFE2L2* mRNA — the defining mechanistic signature of the module. This finding anchors the basal state (N1 → N2) and justifies treating KEAP1 cysteine status as the master switch.

### F002 — Node 1: KEAP1 is a promiscuous reactive-cysteine sensor integrating diverse electrophilic and oxidative inputs

KEAP1 functions as a single sensor node that integrates chemically heterogeneous signals. Ogura et al. ([PMID:20133743](https://pubmed.ncbi.nlm.nih.gov/20133743/)) show that "upon exposure to oxidative and electrophilic stress, reactive cysteine residues in intervening region (IVR) and Broad complex, Tramtrack, and Bric-à-Brac domains of Keap1 are modified by electrophiles. This modification prevents Nrf2 from rapid degradation and induces Nrf2 activity by repression of Keap1." The T-REX targeted-delivery platform of Lin et al. ([PMID:25909755](https://pubmed.ncbi.nlm.nih.gov/25909755/)) demonstrates that "Keap1 [is] a promiscuous electrophile-responsive sensor able to respond with similar efficiencies to discrete electrophilic signals." Feng & Dinkova-Kostova add that KEAP1's highly reactive cysteines are modified by ROS, RNS and electrophilic species of both endogenous and exogenous origin. Because many distinct chemical inputs converge on the same cysteine-modification event, N1 is correctly modeled as **one promiscuous sensor node** rather than a family of input-specific nodes. (Expanded repertoire examples in the literature include S-lactoylation by a reactive glycolytic metabolite, [PMID:37155889](https://pubmed.ncbi.nlm.nih.gov/37155889/), and arsenite acting on the RBX1 RING finger, [PMID:29658272](https://pubmed.ncbi.nlm.nih.gov/29658272/) — a reminder that the ligase complex, not only KEAP1, can be targeted.)

### F003 — Node 3 (KEY CONFORMANCE TARGET): the NRF2-small MAF heterodimer on ARE/CsMBE is strictly required for cytoprotective gene induction

The central, rate-limiting node is the formation of the NRF2-sMAF heterodimer on ARE (CsMBE) sequences. Otsuki et al. ([PMID:26677805](https://pubmed.ncbi.nlm.nih.gov/26677805/)) show that "Nrf2-small Maf (sMaf) heterodimer is essential for the inducible expression of cytoprotective genes upon exposure to oxidative and xenobiotic stresses," and that the CsMBE cistrome is strictly required for this function. Genome-wide, Hirotsu et al. ([PMID:22965115](https://pubmed.ncbi.nlm.nih.gov/22965115/)) find that "the majority of the Nrf2-regulated cytoprotective genes were found in the vicinity of Nrf2-MafG-binding sites." The tethered-dimer experiments of Katsuoka et al. ([PMID:31383749](https://pubmed.ncbi.nlm.nih.gov/31383749/)) provide direct functional proof that the Nrf2-MafG heterodimer acts as the transcriptional activator of NRF2-dependent genes. This makes the **obligate sMAF partnership** a hard requirement for conformance: NRF2 stabilization without sMAF partnering does not produce the regulon. N3 is the step every conformer — loss-direction or gain-direction — must funnel through.

### F004 — Seed-paper finding: NRF2 protein level alone does not account for ARE target induction; a cofactor/PTM gates the N2→N3 edge

The seed paper, Sharma et al. ([PMID:40972999](https://pubmed.ncbi.nlm.nih.gov/40972999/)), built a semi-mechanistic nonlinear mixed-effects (NLME) model of NRF2 and SRXN1 protein time courses in HepG2 cells exposed to the soft electrophiles sulforaphane, andrographolide, ethacrynic acid and CDDO-methyl, across single and repeated exposures and a wide concentration range. Their central conclusion: "NRF2 requires a cofactor or post-translational modification to regulate its activity as a transcription factor. Moreover, this modulation of the transcription factor activity of NRF2 is time-, compound- and exposure scenario specific." For the module, this is the key subtlety at the **N2→N3 edge**: target-gene output cannot be modeled as a monotonic function of NRF2 abundance. The curated module should encode N3 as a **cofactor/PTM-gated** step whose modifier is context-dependent — consistent with the skeleton's note that N3 "requires a cofactor or post-translational modification."

### F005 — Constitutive-ON branch: fumarate succination of KEAP1 activates NRF2 in FH-deficient cancer (HLRCC / type 2 papillary RCC)

The fumarate conformer enters at the sensor node through covalent cysteine modification by an endogenous oncometabolite. Adam et al. ([PMID:22014577](https://pubmed.ncbi.nlm.nih.gov/22014577/)) show in Fh1-deficient mice that "fumarate modifies cysteine residues within the Kelch-like ECH-associated protein 1 (KEAP1), abrogating its ability to repress the Nuclear factor (erythroid-derived 2)-like 2 (Nrf2)-mediated antioxidant response pathway," and that this antioxidant activation is HIF-independent. Kinch et al. ([PMID:22014567](https://pubmed.ncbi.nlm.nih.gov/22014567/)) tie the full chain together: "FH deficiency leads to succination of Keap1, stabilization of Nrf2, and induction of stress-response genes including HMOX1, which is important for the survival of FH-deficient cells." Srinivasan et al. ([PMID:25564569](https://pubmed.ncbi.nlm.nih.gov/25564569/)) confirm that FH-deficient RCC shows fumarate-induced succination of KEAP1 activating Nrf2, and that CUL3 and NRF2 mutations/activation phenotypes also appear in sporadic type 2 papillary RCC. This branch is explicitly complementary to the `oncometabolite_dioxygenase_inhibition` module but enters this module at N1 as a modifier.

### F006 — Constitutive-ON branch: somatic KEAP1/NFE2L2/CUL3 mutations drive NRF2 addiction and chemoresistance

Across human cancers, the three genes of the module are mutated in a **mutually exclusive** pattern — strong genetic evidence that they operate in one convergent pathway. Wang et al. ([PMID:31898230](https://pubmed.ncbi.nlm.nih.gov/31898230/)) note "the mutual exclusivity of somatic mutations in KEAP1, NRF2, and CUL3 in human lung cancer." Ngo et al. ([PMID:40815486](https://pubmed.ncbi.nlm.nih.gov/40815486/)) summarize the downstream phenotype: "aberrant NRF2 activation occurs in cancer due to mutations in the KEAP1/NRF2 pathway, and it contributes to the generation of a tumor microenvironment that favors the proliferation, survival, and chemoresistance of cancer cells." Zhang et al. ([PMID:34158350](https://pubmed.ncbi.nlm.nih.gov/34158350/)) show that pharmacological NRF2-pathway inhibition re-sensitizes KEAP1-mutant lung cancer cells to chemotherapy, closing the causal loop from genetic driver to therapeutically relevant phenotype. This branch populates the constitutive-ON pole of N5.

### F007 — Optional non-canonical branch: p62/SQSTM1 sequesters KEAP1 to activate NRF2 independent of cysteine modification

A mechanistically distinct, **optional** route activates NRF2 without direct cysteine chemistry. Yang et al. ([PMID:39172027](https://pubmed.ncbi.nlm.nih.gov/39172027/)) describe how phosphorylated, aggregated SQSTM1/p62 "sequesters KEAP1 and activates the non-canonical SQSTM1-KEAP1-NFE2L2 antioxidant pathway." Dahl-Wilkie et al. ([PMID:39936983](https://pubmed.ncbi.nlm.nih.gov/39936983/)) show chronic IL-1-exposed LNCaP prostate cancer cells accumulate a basal p62-KEAP1 complex, with p62 sequestering KEAP1 to the autophagosome for degradation — but, notably, **only a subset of NRF2 target genes was induced**, echoing the seed paper's cofactor-gating point (F004). This branch connects the module to autophagy biology and should be flagged as an optional, conformer-specific entry at N1/N2 rather than a core requirement.

### F008 — Downstream nodes 4–5: the ARE regulon restores redox balance; NRF2-null confers vulnerability, activation is protective (bidirectional)

The downstream arm is directly supported by mouse genetics. Klaassen & Reisman ([PMID:20122946](https://pubmed.ncbi.nlm.nih.gov/20122946/)) report that NRF2 positively regulates a large battery of cytoprotective genes (NQO1, GSTs, UGTs, MRP efflux transporters) and that "livers of Nrf2-null mice are more susceptible to various oxidative/electrophilic stress-induced pathologies than wild-type mice. In contrast, both pharmacological and genetic models of hepatic Nrf2 activation are protective against oxidative/electrophilic stress." This is the empirical basis for the **bidirectional N5 node**: loss = vulnerability, activation = protection. Hirotsu et al. ([PMID:22965115](https://pubmed.ncbi.nlm.nih.gov/22965115/)) further show the Nrf2-MafG regulon extends into glucose and amino-acid metabolism, so N4 ("regulon restores redox balance") should be framed to allow metabolic outputs alongside classic antioxidant/detoxification genes.

### F009 — Node 2 mechanism: the ETGE/DLG "hinge-and-latch" degron, and human cancer degron mutations that cause constitutive activation

The molecular basis of N2 is a two-site recognition code. Tong et al. ([PMID:17081101](https://pubmed.ncbi.nlm.nih.gov/17081101/), [PMID:17785452](https://pubmed.ncbi.nlm.nih.gov/17785452/)) establish that KEAP1 recognizes NRF2 through the high-affinity **ETGE** (hinge) and low-affinity **DLG** (latch) motifs in the Neh2 domain, where "the DLG motif works to correctly position the lysines within the Nrf2 Neh2 domain for efficient ubiquitination." Fukutomi et al. ([PMID:24366543](https://pubmed.ncbi.nlm.nih.gov/24366543/)) solved the Keap1-DLGex complex at 1.6 Å and showed it "interprets well the human-cancer-derived loss-of-function mutations in DLGex." Critically, Shibata et al. ([PMID:18757741](https://pubmed.ncbi.nlm.nih.gov/18757741/)) provide direct human-tumor evidence: cancer mutations "specifically alter amino acids in the DLG or ETGE motifs, resulting in aberrant cellular accumulation of Nrf2. Mutant Nrf2 cells display constitutive induction of cytoprotective enzymes and drug efflux pumps, which are insensitive to Keap1-mediated regulation" — and siRNA knockdown re-sensitizes cells to oxidative stress and chemotherapy. This defines the **NFE2L2 gain-of-function conformer at N2**. Liu et al. ([PMID:34600335](https://pubmed.ncbi.nlm.nih.gov/34600335/)) add quantitative modeling of the ETGE/DLG open/closed states and NRF2 ultrasensitivity.

### F010 — Ontology IDs verified against EBI OLS4 (curation-ready)

A programmatic lookup against EBI OLS4 (2026-11-07) confirmed exact label↔ID matches for 25 of 26 candidate terms (see Ontology Suggestions section). The one candidate that did not resolve — "negative regulation of oxidative stress-induced cell death" — was dropped. This makes the module's ontology annotation layer immediately usable by curators without manual re-verification.

### F011 — Genetic epistasis proves KEAP1 is upstream of NRF2 (N1 → N2), and constitutive activation is hormetic

Wakabayashi et al. ([PMID:14517554](https://pubmed.ncbi.nlm.nih.gov/14517554/)) provide the definitive directionality proof: Keap1-deficient mice "died postnatally, probably from malnutrition resulting from hyperkeratosis in the esophagus and forestomach... Breeding to Nrf2-deficient mice reversed the phenotypic Keap1 deficiencies. These experiments show that Keap1 acts upstream of Nrf2." Because removing NRF2 completely rescues the Keap1-null lethal phenotype, the entire pathology is NRF2-dependent — the module's core causal arrow N1 → N2 is genetically secured. Taguchi et al. ([PMID:20404090](https://pubmed.ncbi.nlm.nih.gov/20404090/)) show the response is **hormetic**: graded Keap1 reduction protects against acetaminophen toxicity, but "constitutive Nrf2 activation beyond a certain threshold is rather disadvantageous to long-term survival." This supports modeling N5 as bidirectional with an optimum, not a monotonic "more NRF2 is better" relationship.

### F012 — Evolutionary conservation, human blunted-direction evidence, and the sole clinical NRF2 therapy

The axis is deeply conserved. Loboda et al. ([PMID:27100828](https://pubmed.ncbi.nlm.nih.gov/27100828/)) note "the vertebrate Nrf2 belongs to Cap 'n' Collar (Cnc) bZIP family of transcription factors and shares a high homology with SKN-1 from Caenorhabditis elegans or CncC found in Drosophila melanogaster," justifying the "conserved mechanism module" designation. Sykiotis & Bohmann ([PMID:20215646](https://pubmed.ncbi.nlm.nih.gov/20215646/)) supply the human loss-direction evidence: "In humans, polymorphisms that decrease Nrf2 abundance have been associated with various pathologies of the skin, respiratory system, and digestive tract" — one variant class linked to multiple organ manifestations, exactly the cross-manifestation evidence the research brief requested. On the translational side, Sezgin Bayindir et al. ([PMID:40919319](https://pubmed.ncbi.nlm.nih.gov/40919319/)) note that "dimethyl fumarate remains the sole NRF2-targeting therapy in clinical practice, used for multiple sclerosis," anchoring the activation direction in approved human therapy.

---

## Mechanistic Model / Interpretation

### Executive recommendation on name and scope

**Keep the module name `keap1_nrf2_are_signaling`.** The literature uses "KEAP1-NRF2" and "KEAP1-NRF2-ARE" as the standard designations, the three core genes are genetically mutually exclusive in cancer (one pathway, F006), and the axis is evolutionarily conserved (F012). **Keep the single bidirectional scope.** The same central node (NRF2-sMAF ARE transactivation) is the rate-limiting step for both the blunted and constitutive-ON directions; the direction is set by the modifier on KEAP1/NRF2, not by separate biology. Splitting into two modules would duplicate N1–N5 and sever the shared conformance target.

### Proposed DAG — five core nodes

```
          ┌─ electrophile/oxidant cysteine modification  ┐
          ├─ fumarate succination (FH-deficient)         │ (conformer-specific
  DRIVERS ┼─ KEAP1 / CUL3 loss-of-function mutation       ├  modifiers; enter at
          ├─ NFE2L2 ETGE/DLG degron gain-of-function      │  N1 or N2)
          └─ p62/SQSTM1 sequestration (non-canonical)    ┘
                         │
                         ▼
   [N1] KEAP1 Sensor Cysteine Modification / loss of KEAP1 repression
                         │  (basal: KEAP1-CUL3-RBX1 constitutively ubiquitinates NRF2)
                         ▼
   [N2] NRF2 Escape from KEAP1-CUL3 Degradation
                         │  (ETGE/DLG hinge-and-latch; stabilized NRF2 → nucleus)
                         │  ◄── cofactor/PTM gate (seed paper): output ≠ f(NRF2 level)
                         ▼
   [N3] NRF2–small MAF Transcriptional Activation of ARE/CsMBE Genes   ★ KEY CONFORMANCE TARGET
                         │
                         ▼
   [N4] ARE Target Gene Products Restore Redox Balance
        (SRXN1, NQO1, HMOX1, GCLC/GCLM, GSTs, UGTs, MRP efflux; + metabolic genes)
                         │
                         ▼
   [N5] Cytoprotection  ◄──────► Its Failure   (BIDIRECTIONAL, hormetic optimum)
        activation = protection / tumor survival & chemoresistance
        loss       = vulnerability to oxidative & electrophilic injury
```

### Core vs. optional nodes

| Node | Label | Core? | Notes |
|------|-------|-------|-------|
| N1 | KEAP1 Sensor Cysteine Modification / loss of repression | **Core** | Single promiscuous sensor; accepts all driver modifiers (F002) |
| N2 | NRF2 Escape from KEAP1-CUL3 Degradation | **Core** | ETGE/DLG degron; upstream directionality genetically proven (F009, F011) |
| N3 | NRF2-sMAF ARE/CsMBE Transactivation | **Core — key conformance target** | Obligate sMAF partner; cofactor/PTM-gated edge (F003, F004) |
| N4 | ARE Regulon Restores Redox Balance | **Core** | Regulon spans antioxidant + metabolic genes (F008) |
| N5 | Cytoprotection or Its Failure | **Core, bidirectional** | Hormetic; set by modifier direction (F008, F011) |

**Conformer-specific modifiers (not separate nodes):** fumarate/FH (F005), KEAP1/CUL3 LoF (F006), NFE2L2 degron GoF (F009), p62/SQSTM1 non-canonical sequestration (F007). The p62 route is the most clearly *optional* branch and should be labeled as such.

### Gene-to-node mapping

| Gene | Role | Node(s) | Direction | Evidence |
|------|------|---------|-----------|----------|
| KEAP1 | Sensor / CUL3 substrate adaptor | N1, N2 | LoF → ON | F001, F002, F006, F011 |
| CUL3 | RING ligase scaffold | N2 | LoF → ON | F001, F006 |
| RBX1 | RING-box component | N2 | (arsenite target) | F001; [PMID:29658272] |
| NFE2L2 (NRF2) | Central transcription factor | N2, N3 | degron GoF → ON; low-abundance variants → blunted | F003, F004, F009, F012 |
| MAFF/MAFG/MAFK | Obligate heterodimer partner | N3 | required | F003 |
| FH | TCA enzyme; loss → fumarate | N1 (succination) | LoF → ON | F005 |
| SQSTM1 (p62) | Non-canonical KEAP1 sequestration | N1/N2 | optional → ON | F007 |
| SRXN1, NQO1, HMOX1, GCLC, GCLM, GSTs, UGTs | ARE regulon effectors | N4 | output | F004, F005, F008 |

---

## Evidence Base

| PMID | Evidence type | Exact quote | Supported claim |
|------|---------------|-------------|-----------------|
| [26551712](https://pubmed.ncbi.nlm.nih.gov/26551712/) | Review | "the Kelch-like ECH-associated protein 1 (Keap1)-cullin3 (Cul3)-ring-box1 (Rbx1) E3-ligase to be the primary Nrf2 regulatory system." | Basal degradation machinery (N1/N2) |
| [42844347](https://pubmed.ncbi.nlm.nih.gov/42844347/) | Review | "Cysteine modifications within KEAP1 and BACH1 render the repressor proteins inactive, resulting in rapid NRF2 activation that does not rely on de novo transcription of NFE2L2" | Module logic: stabilization, not transcription |
| [20133743](https://pubmed.ncbi.nlm.nih.gov/20133743/) | In vitro / structural | "reactive cysteine residues in [IVR] and [BTB] domains of Keap1 are modified by electrophiles. This modification prevents Nrf2 from rapid degradation" | N1 sensor cysteine modification |
| [25909755](https://pubmed.ncbi.nlm.nih.gov/25909755/) | In vitro | "Keap1 [is] a promiscuous electrophile-responsive sensor able to respond with similar efficiencies to discrete electrophilic signals" | N1 as single promiscuous sensor |
| [26677805](https://pubmed.ncbi.nlm.nih.gov/26677805/) | Model organism / genomic | "Nrf2-small Maf (sMaf) heterodimer is essential for the inducible expression of cytoprotective genes" | N3 obligate sMAF requirement |
| [22965115](https://pubmed.ncbi.nlm.nih.gov/22965115/) | Genomic (ChIP-seq) | "The majority of the Nrf2-regulated cytoprotective genes were found in the vicinity of Nrf2-MafG-binding sites." | N3→N4 genome-wide |
| [31383749](https://pubmed.ncbi.nlm.nih.gov/31383749/) | In vitro (tethered dimer) | Nrf2-MafG heterodimer "acts as a transcriptional activator of Nrf2-dependent genes" | N3 direct functional proof |
| [40972999](https://pubmed.ncbi.nlm.nih.gov/40972999/) | In vitro + modeling (SEED) | "NRF2 requires a cofactor or post-translational modification to regulate its activity as a transcription factor... time-, compound- and exposure scenario specific." | N2→N3 cofactor/PTM gate |
| [22014577](https://pubmed.ncbi.nlm.nih.gov/22014577/) | Model organism | "fumarate modifies cysteine residues within [KEAP1], abrogating its ability to repress the... Nrf2-mediated antioxidant response pathway" | Fumarate conformer at N1 |
| [22014567](https://pubmed.ncbi.nlm.nih.gov/22014567/) | Review/commentary | "FH deficiency leads to succination of Keap1, stabilization of Nrf2, and induction of stress-response genes including HMOX1" | Full fumarate chain N1→N4→N5 |
| [25564569](https://pubmed.ncbi.nlm.nih.gov/25564569/) | Review (human cancer) | "In fumarate hydratase-deficient RCC, fumarate-induced succination of KEAP1 activates Nrf2" | HLRCC / type 2 papillary RCC |
| [40815486](https://pubmed.ncbi.nlm.nih.gov/40815486/) | Review | "aberrant NRF2 activation occurs in cancer due to mutations in the KEAP1/NRF2 pathway... proliferation, survival, and chemoresistance" | Constitutive-ON phenotype (N5) |
| [31898230](https://pubmed.ncbi.nlm.nih.gov/31898230/) | Review (human cancer) | "the mutual exclusivity of somatic mutations in KEAP1, NRF2, and CUL3 in human lung cancer" | One convergent module |
| [34158350](https://pubmed.ncbi.nlm.nih.gov/34158350/) | In vitro | NRF2-pathway inhibitor "Sensitizes Keap1-Mutant Lung Cancer Cells to Chemotherapy" | Causal driver→chemoresistance |
| [39172027](https://pubmed.ncbi.nlm.nih.gov/39172027/) | In vitro | "sequesters KEAP1 and activates the non-canonical SQSTM1-KEAP1-NFE2L2 antioxidant pathway" | Optional p62 branch |
| [39936983](https://pubmed.ncbi.nlm.nih.gov/39936983/) | In vitro | p62 "promotes non-canonical NRF2... by binding and sequestering KEAP1" (only a subset of targets induced) | Optional p62 branch; partial regulon |
| [20122946](https://pubmed.ncbi.nlm.nih.gov/20122946/) | Model organism | "livers of Nrf2-null mice are more susceptible... Nrf2 activation [is] protective against oxidative/electrophilic stress" | Bidirectional N5 |
| [18757741](https://pubmed.ncbi.nlm.nih.gov/18757741/) | Human tumor | mutations "alter amino acids in the DLG or ETGE motifs, resulting in aberrant cellular accumulation of Nrf2... insensitive to Keap1-mediated regulation" | NFE2L2 GoF conformer at N2 |
| [17785452](https://pubmed.ncbi.nlm.nih.gov/17785452/) | Review/structural | "The DLG motif works to correctly position the lysines within the Nrf2 Neh2 domain for efficient ubiquitination." | Hinge-and-latch mechanism (N2) |
| [24366543](https://pubmed.ncbi.nlm.nih.gov/24366543/) | Structural (1.6 Å) | DLGex structure "interprets well the human-cancer-derived loss-of-function mutations" | Degron structural basis |
| [17081101](https://pubmed.ncbi.nlm.nih.gov/17081101/) | Review | ETGE/DLG "function as a hinge and latch attenuating Keap1 activity in different redox states" | Two-site recognition model |
| [34600335](https://pubmed.ncbi.nlm.nih.gov/34600335/) | Modeling | Modeling of "ETGE and DLG motifs, NRF2 production, KEAP1-dependent and independent NRF2 degradation" and ultrasensitivity | Quantitative N2 behavior |
| [14517554](https://pubmed.ncbi.nlm.nih.gov/14517554/) | Model organism (epistasis) | "Breeding to Nrf2-deficient mice reversed the phenotypic Keap1 deficiencies... Keap1 acts upstream of Nrf2" | N1→N2 directionality |
| [20404090](https://pubmed.ncbi.nlm.nih.gov/20404090/) | Model organism | "constitutive Nrf2 activation beyond a certain threshold is rather disadvantageous to long-term survival" | Hormetic N5 |
| [27100828](https://pubmed.ncbi.nlm.nih.gov/27100828/) | Review | "vertebrate Nrf2 belongs to Cap 'n' Collar (Cnc) bZIP family... high homology with SKN-1... or CncC" | Evolutionary conservation |
| [20215646](https://pubmed.ncbi.nlm.nih.gov/20215646/) | Review (human) | "polymorphisms that decrease Nrf2 abundance have been associated with various pathologies of the skin, respiratory system, and digestive tract" | Blunted-direction human evidence |
| [40919319](https://pubmed.ncbi.nlm.nih.gov/40919319/) | Review (clinical) | "dimethyl fumarate remains the sole NRF2-targeting therapy in clinical practice, used for multiple sclerosis" | Human therapeutic anchor |

**Evidence-type separation.** Human clinical/tumor evidence: PMID 18757741, 31898230, 25564569, 20215646, 40919319. Model organism: PMID 22014577, 20122946, 14517554, 20404090. In vitro: PMID 20133743, 25909755, 31383749, 40972999, 34158350, 39172027, 39936983. Structural/modeling: PMID 24366543, 17785452, 17081101, 34600335. Review/synthesis: PMID 26551712, 42844347, 27100828, 40815486, 22014567.

**Full-text verification flags:** The seed paper (PMID:40972999) abstract names the cofactor/PTM gate but does not identify the molecular cofactor — full text should be checked before binding a specific PTM term. PMID:14517554 was recorded with a snippet "mismatch" flag during curation (quote paraphrased from abstract) and should be re-verified verbatim. PMID:39936983's claim that only a subset of NRF2 targets is induced warrants full-text confirmation of which genes.

---

## Ontology Suggestions (verified against EBI OLS4, 2026-11-07)

**GO biological process / function (for nodes):**

| GO ID | Label | Node |
|-------|-------|------|
| GO:0006979 | response to oxidative stress | N1/N5 |
| GO:0034599 | cellular response to oxidative stress | N1/N5 |
| GO:0098869 | cellular oxidant detoxification | N4 |
| GO:0045454 | cell redox homeostasis | N4 |
| GO:0016567 | protein ubiquitination | N2 |
| GO:0043161 | proteasome-mediated ubiquitin-dependent protein catabolic process | N2 |
| GO:0031463 | Cul3-RING ubiquitin ligase complex | N2 (component) |
| GO:0045944 | positive regulation of transcription by RNA polymerase II | N3 |
| GO:0006355 | regulation of DNA-templated transcription | N3 |
| GO:0000981 | DNA-binding transcription factor activity, RNA polymerase II-specific | N3 |
| GO:0006750 | glutathione biosynthetic process | N4 (GCLC/GCLM) |
| GO:0006749 | glutathione metabolic process | N4 |
| GO:0006805 | xenobiotic metabolic process | N4 |
| GO:0009410 | response to xenobiotic stimulus | N1/N4 |

**CL cell types:** CL:0000182 hepatocyte; CL:0000066 epithelial cell; CL:0000082 epithelial cell of lung; CL:0002328 bronchial epithelial cell; CL:0002518 kidney epithelial cell; CL:0002306 epithelial cell of proximal tubule.

**UBERON anatomy:** UBERON:0002107 liver; UBERON:0002048 lung; UBERON:0002113 kidney; UBERON:0000995 uterus; UBERON:0002097 skin of body.

*Dropped:* "negative regulation of oxidative stress-induced cell death" did not resolve to a stable ID in OLS4 and should be suggested by label only, if at all.

---

## Out-of-Scope Boundary Notes

- **Fumarate succination** enters this module at N1 as a modifier but its upstream metabolic biology (FH loss → dioxygenase inhibition) belongs to the complementary `oncometabolite_dioxygenase_inhibition` module; cross-reference rather than duplicate.
- **General CRL3 adaptor swapping** is covered by `cul3_substrate_adaptor_dysfunction`; this module covers only KEAP1 as one specific CUL3 adaptor.
- **BACH1** is a parallel ARE repressor (PMID:42844347) and NRF1/NFE2L1 is a related CNC factor (PMID:19665035); both are adjacent biology and should stay out of the core node set unless a curator decides to add them.
- **Autophagy, proliferation, and apoptosis** named in the seed abstract are candidate N5 outputs but their scope is unresolved (see Limitations); do not bind them as core without curator decision.
- **TrxR1 (PMID:26058897), GSK3β/Fyn phosphorylation (PMID:23434765), and PML-body nuclear degradation (PMID:29807365)** are parallel/auxiliary NRF2 regulators beyond the canonical KEAP1-CUL3 axis; treat as out-of-scope auxiliary mechanisms pending full-text review.

---

## Limitations and Knowledge Gaps

1. **The cofactor/PTM gate (N2→N3) is molecularly unidentified.** The seed paper (PMID:40972999) is clear that NRF2 protein level does not predict target induction, but the responsible cofactor or post-translational modification is not named. Candidate mechanisms in the broader literature (GSK3β/Fyn cascades, PMID:23434765; TrxR1, PMID:26058897; nuclear PML-body degradation, PMID:29807365) remain unbound to this module and need full-text validation before curation.
2. **Scope of N5 is partly open.** Whether autophagy, proliferation and apoptosis belong inside N5 or in adjacent modules is unresolved. The p62/SQSTM1 branch in particular blurs the boundary with autophagy.
3. **Partial regulon activation.** Both the seed paper and the p62 study (PMID:39936983) observe that only subsets of ARE genes respond under certain conditions, implying promoter-specific or gene-specific thresholds that a single N3→N4 edge cannot fully capture.
4. **One snippet flagged as a mismatch** (PMID:14517554) and several key abstracts are review-level; primary-literature verification is advised for the epistasis and FH-succination quotes before they are used as curation evidence.
5. **Module boundaries with neighbors** were asserted from the description, not independently re-derived; a curator should confirm the fumarate and CUL3-adaptor overlaps are handled by cross-references rather than duplicated nodes.

---

## Proposed Follow-up Actions

1. **Bind the N3 modifier explicitly.** Encode N3 as a cofactor/PTM-gated step and add a curator note citing PMID:40972999; obtain the seed paper full text to attempt identification of the cofactor/PTM so a specific term can be bound.
2. **Finalize the five core nodes** (N1–N5) as required for conformance, with N3 as the key conformance target, and register the four driver sets (fumarate/FH, KEAP1/CUL3 LoF, NFE2L2 GoF, p62/SQSTM1) as conformer-specific modifiers — the p62 route labeled optional/non-canonical.
3. **Attach the gene-to-node table** (KEAP1, CUL3, RBX1, NFE2L2, MAFF/G/K, FH, SQSTM1, and the SRXN1/NQO1/HMOX1/GCLC/GCLM regulon) as the module's conformance scaffold.
4. **Apply the verified ontology set** (F010) directly; suggest the one dropped term by label only.
5. **Verify the two flagged snippets** (PMID:14517554 epistasis quote; PMID:39936983 subset-induction claim) against full text before finalizing evidence bindings.
6. **Model N5 as hormetic/bidirectional** (PMID:20404090) rather than monotonic, and have a curator settle the autophagy/apoptosis/proliferation scope question.
7. **Cross-reference, do not duplicate,** the fumarate succination entry with `oncometabolite_dioxygenase_inhibition` and the CUL3 adaptor biology with `cul3_substrate_adaptor_dysfunction`.

---

## Open Questions for Curator Review

1. Should the **molecular identity** of the N2→N3 cofactor/PTM gate be left as an abstract modifier, or should a provisional candidate (e.g., a specific phosphorylation site) be proposed?
2. Do **autophagy, proliferation, and apoptosis** belong inside N5, or should they be separate downstream modules?
3. Should the **p62/SQSTM1 non-canonical branch** be a formally recognized optional conformer, given it induces only a partial regulon?
4. Should **BACH1** (parallel ARE repressor) and **NRF1/NFE2L1** be acknowledged as adjacent nodes or kept strictly out of scope?
5. Is the **hormetic/bidirectional** framing of N5 (optimum, not monotonic) acceptable for the module schema?

---

*Report generated from 12 confirmed findings across 5 research iterations; 70 papers reviewed. All quoted snippets are drawn from the cited abstracts as recorded in the knowledge state.*


## Artifacts

- [OpenScientist final report](keap1_nrf2_are_signaling-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](keap1_nrf2_are_signaling-deep-research-openscientist_artifacts/final_report.pdf)