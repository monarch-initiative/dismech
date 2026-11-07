# Citations for Research Query

**Query:** # Mechanism Module Research Template

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

**Provider:** openscientist
**Generated:** 2026-11-07T16:59:57.184638

1. PMID:40972999
2. PMID:26551712
3. PMID:42844347
4. PMID:20133743
5. PMID:25909755
6. PMID:37155889
7. PMID:29658272
8. PMID:26677805
9. PMID:22965115
10. PMID:31383749
11. PMID:22014577
12. PMID:22014567
13. PMID:25564569
14. PMID:31898230
15. PMID:40815486
16. PMID:34158350
17. PMID:39172027
18. PMID:39936983
19. PMID:20122946
20. PMID:17081101
21. PMID:17785452
22. PMID:24366543
23. PMID:18757741
24. PMID:34600335
25. PMID:14517554
26. PMID:20404090
27. PMID:27100828
28. PMID:20215646
29. PMID:40919319
30. PMID:19665035
31. PMID:26058897
32. PMID:23434765
33. PMID:29807365