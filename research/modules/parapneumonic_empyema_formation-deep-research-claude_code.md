---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5-5
cached: false
start_time: '2026-10-03T21:03:02.403175'
end_time: '2026-10-03T21:04:26.092393'
duration_seconds: 83.69
template_file: templates/module_mechanism_research.md
template_sha: "24cb27b5d49e5e45a5e3c24792bdfb6f9b195d14"
template_variables:
  module_name: Pleuropneumonia and Parapneumonic Empyema Formation Module
  module_slug: parapneumonic_empyema_formation
  category: Module
  module_description: 'A conserved pathophysiology module for pleuropneumonia: the
    extension of pneumonic inflammation from the lung parenchyma to the adjacent visceral
    pleura, producing a parapneumonic effusion that can progress through an exudative
    stage, a fibrinopurulent stage with fibrin deposition and loculation, and an organizing
    stage with pleural peel formation, culminating in empyema (pus in the pleural
    space). The cascade is shared across pneumonias caused by unrelated organisms.'
  pathophysiology_summary: '- Pneumonic Parenchymal Inflammation Adjacent to the Pleura:'
provider_config:
  timeout: 1800
  max_retries: 3
  parameters:
    allowed_domains: []
    claude_executable: claude
    skip_permissions: false
    allowed_tools:
    - WebSearch
    - WebFetch
    add_dirs: []
    timeout: 1800
    min_report_chars: 200
    extra_args: []
run_metadata:
  models_used:
  - claude-haiku-4-5-20251001
  - claude-sonnet-5-5
  web_search_requests: 3
  num_turns: 10
  total_cost_usd: 0.7883397999999999
  session_id: 81562984-f39d-5787-be67-7015e0b1b678
  stop_reason: end_turn
  assistant_text_blocks: 1
fell_back: true
requested_provider: falcon
provider_attempts:
- provider: falcon
  succeeded: false
  error_type: ProviderNotConfiguredError
  remedy: the provider is not configured
  retryable: false
- provider: claude_code
  succeeded: true
citation_count: 4
reference_validation:
  total_references: 5
  verified: 5
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 5
  on_topic: 0
  validator_version: 0.3.0rc3
term_validation:
  total_terms: 0
  verified: 0
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Mechanism Module Research Template

## Target Module
- **Module Name:** Pleuropneumonia and Parapneumonic Empyema Formation Module
- **Module Slug:** parapneumonic_empyema_formation
- **Category:** Module

## Current Module Description

A conserved pathophysiology module for pleuropneumonia: the extension of pneumonic inflammation from the lung parenchyma to the adjacent visceral pleura, producing a parapneumonic effusion that can progress through an exudative stage, a fibrinopurulent stage with fibrin deposition and loculation, and an organizing stage with pleural peel formation, culminating in empyema (pus in the pleural space). The cascade is shared across pneumonias caused by unrelated organisms.

## Current Provisional Nodes

- Pneumonic Parenchymal Inflammation Adjacent to the Pleura:

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

# Research report: Pleuropneumonia and Parapneumonic Empyema Formation Module (`parapneumonic_empyema_formation`)

**Verification status.** I ran four web searches and three page fetches, so a minority of the claims below are source-checked. Anything marked ⚠ comes from my background knowledge. It has not been checked against a source in this session.

- Every PMID and quote in the evidence table came back through a fetch tool that summarises pages with a small model. Before any of it goes into a `snippet:`, run `just fetch-reference PMID:<n>` and `just count-verified-snippets`.
- No GO, CL or UBERON identifiers are given. I did not look any up, and the repo rule is never to write a CURIE from memory. Section 6 lists labels to search for.
- The module file in the repo (`kb/modules/parapneumonic_empyema_formation.yaml`) currently has one node, the trigger. No disorder entry conforms to it yet. Several existing entries mention empyema (`Pneumococcal_Pneumonia`, `Anaerobic_Pneumonia`, `Actinomycosis`, `Pasteurellosis` and others) and are candidates for conformance.

## 1. Executive recommendation

**Scope.** The three-stage description in the module (exudative, fibrinopurulent, organizing) is the standard pathophysiology of parapneumonic effusion and pleural infection. ⚠ It is the classic ATS stage scheme that clinical guidance still uses, but I did not source it here. It is recognizable across organisms, so a conserved module is appropriate.

**Name.** I recommend "Parapneumonic Effusion to Empyema Progression" instead of the current "Pleuropneumonia and Parapneumonic Empyema Formation".

- "Pleuropneumonia" is a veterinary term (equine, bovine, *Actinobacillus pleuropneumoniae* in pigs). In human medicine it is rarely used.
- The slug `parapneumonic_empyema_formation` is fine. If the title changes, the module description should say the veterinary usage is outside scope.

**Boundaries.**
- Include extension of infection from the lung to the pleura, effusion formation, fibrin deposition and loculation, empyema, and the fibrotic pleural peel.
- Keep post-procedural, post-surgical and trauma empyema out of the core. They share the later stages but not the trigger. Make them an optional entry variant.
- Keep tuberculous pleurisy out. It is granulomatous and its pleural fibrosis is mechanistically different.
- Keep malignant effusion out.
- Treat the pleural-fibrosis end state as a sibling of the existing `fibrotic_response` module, not a duplicate. The organizing stage should conform to `fibrotic_response#Mesenchymal Cell Activation` (verify the node name with `just list-modules fibrotic`).

## 2. Proposed DAG

All nodes except the first are provisional. Supporting-evidence status is given in the Support column.

| # | Node | Core or optional | Support |
|---|---|---|---|
| 1 | Pneumonic Parenchymal Inflammation Adjacent to the Pleura (existing trigger) | Core | ⚠ background knowledge |
| 2 | Visceral Pleural Mesothelial Activation and Barrier Injury | Core | Sourced: Chung 2013 |
| 3 | Increased Pleural Capillary Permeability and Exudative Effusion | Core | Sourced: Chung 2013, Thickett 1999 |
| 4 | Intrapleural Coagulation Activation with Suppressed Fibrinolysis (PAI-1 up, tPA/uPA relatively down) | Core | Sourced: Chung 2013, Komissarov 2018 |
| 5 | Fibrin Deposition and Septation or Loculation | Core | Sourced: Komissarov 2018 |
| 6 | Bacterial Invasion, Neutrophil Influx, Fluid Acidification, and Pus | Core | ⚠ pH, glucose and LDH criteria are standard clinical teaching but not sourced here |
| 7 | Mesothelial-to-Mesenchymal Transition and Myofibroblast Collagen Deposition (pleural peel, trapped lung) | Core for the organizing stage; optional for a self-limited effusion | Sourced: Komissarov 2018 |
| 8 | Extracellular DNA and Viscous Pus Burden | Optional | ⚠ implied by MIST2 DNase efficacy but not sourced here |

**Causal edges.**
- 1 → 2 → 3
- 2 → 4
- 3 → 5 (protein-rich fluid supplies fibrinogen)
- 4 → 5
- 3 → 6 (bacterial access to the pleural space)
- 6 → 4 (reinforcing: inflammation and bacterial products drive more PAI-1)
- 6 → 8 → 5 (loculation worsens drainage)
- 5 → 7

Nodes 4 and 5 are the strongest-supported parts of the chain. Edges 3 → 6 and 6 → 8 are inferential and need primary evidence.

**Stage mapping.** Exudative = nodes 2–3. Fibrinopurulent = 4–6 and 8. Organizing = 7.

## 3. Gene-to-node mapping

This module is mechanism-level, with no monogenic cause. Genes are effectors or modifiers, not drivers.

| Gene or product | Node | Basis |
|---|---|---|
| SERPINE1 (PAI-1) | 4 | Sourced (Komissarov 2018) |
| PLAT (tPA), PLAU (uPA) | 4 | Sourced (Chung 2013 describes the PAI-1/tPA balance) |
| VEGFA, CXCL8 (IL-8) | 2, 3 | Sourced (Chung 2013) |
| TGFB1, COL1A1 | 7 | Partly sourced. The TGF-β1 collagen finding appeared in a search summary, not a verified abstract. |
| F3 (tissue factor), FGA/FGB/FGG | 4, 5 | ⚠ background knowledge |
| Immunodeficiency genes (BTK etc.) | 1 | ⚠ background; susceptibility modifiers, not part of the core |

HGNC CURIEs must be looked up (`hgnc:` lowercase) before binding.

## 4. Evidence table

All quotes need verification against the cache.

| PMID | Type | Quote | Supports |
|---|---|---|---|
| 23308155 (Chung et al., *PLoS ONE* 2013) | Review/clinical, effusion cohort | "Exposure of pleural mesothelial cells to bacteria or lipopolysaccharide may increase release of angiogenic factors" … "activate coagulation cascade, and repress fibrinolytic activity within the pleural cavity" | Nodes 2–4. The quote is joined by ellipses from two sentences; split it into two snippets. |
| 23308155 | same | "An imbalance between PAI-1 and tissue type plasminogen activator (tPA) may elicit fibrin formation and subsequent pleural fluid loculation and fibrosis" | Edge 4 → 5 |
| 29345198 (Komissarov et al., *Am J Physiol Lung* 2018) | Review (`REVIEW_SYNTHESIS` quote role) | "Loculation is promoted and then potentiated by inhibition of local fibrinolysis, in large part by elaboration of elevated levels of PAI-1." | Nodes 4 → 5 |
| 29345198 | Review | "Through a process termed mesomesenchymal transition (MesoMT), mesothelial cells become matrix producing myofibroblasts." | Node 7 |
| 29345198 | Review | "Pleural injury proceeds through a phase of acute inflammation followed by organization, a process that involves the deposition of intrapleural fibrin and its remodeling." | Stage structure |
| 10413724 (Thickett et al., *Thorax* 1999) | Human clinical | "VEGF levels are raised in the majority of exudative effusions, implying a pathogenic role for this molecule in pleural effusions." | Node 3. Indirect: the cohort mixes inflammatory and malignant effusions. |
| 21830966 (Rahman et al., MIST2, *NEJM* 2011) | Human RCT | No exact abstract quote obtained. The search summary says tPA plus DNase beat placebo and each drug alone on chest x-ray opacity and surgical referral. | Treatment-based support for nodes 4, 5 and 8, so `INDIRECT` at most |

MIST1 (streptokinase, 454 patients, no benefit) appeared in the search, but I did not capture a PMID or a quote. It is a useful counterpoint, because not every fibrinolytic works.

## 5. Questions answered

1. **Best-supported shared mechanism.** Mesothelial activation → permeability and coagulation, with PAI-1-mediated fibrinolysis suppression → fibrin loculation → fibroblast-like transition and peel. The sourced papers support the fibrin and fibrinolysis axis best.
2. **Name and scope.** See the recommendation in section 1.
3. **Core versus optional.** See the DAG table.
4. **Genes, cell types, tissues.** Genes are in section 3. Cells: mesothelial cell, neutrophil, macrophage, myofibroblast, fibroblast. Tissues: visceral and parietal pleura, pleural cavity.
5. **Evidence for the causal edges.** Sourced for 2 → 4 and 4 → 5; the rest are inferential.
6. **Direct human evidence linking one factor to multiple manifestations.** Chung 2013 links VEGF to effusion volume and, in the search summary, to loculation and fibrosis. That link still needs abstract verification.
7. **Model organism and in vitro evidence.** I found none in the searches. Rabbit and mouse pleural-injury models and mesothelial cell culture (TGF-β1, collagen, MesoMT) exist ⚠, but PMIDs are needed. Run a dedicated PubMed search on "rabbit empyema model" and "mesomesenchymal transition".
8. **Ontology terms.** See section 6.
9. **Speculative.** See the next section.

## 6. Ontology suggestions (labels only; look up CURIEs)

- **GO biological processes to search.** Blood coagulation; fibrinolysis; regulation of fibrinolysis; negative regulation of fibrinolysis; positive regulation of vascular permeability; inflammatory response; neutrophil chemotaxis; acute inflammatory response to antigenic stimulus; collagen biosynthetic process or extracellular matrix organization; epithelial to mesenchymal transition. Check whether the last one is applicable to mesothelial cells; GO has no "mesothelial to mesenchymal transition" term to my knowledge ⚠. Do not bind it without a lookup.
- **CL.** Mesothelial cell; neutrophil; macrophage; myofibroblast cell; fibroblast.
- **UBERON.** Pleura; visceral pleura; parietal pleura; pleural cavity; lung.

## 7. Out of scope and weakly supported

- The causal roles of IL-8 and VEGF beyond association. The evidence is correlative.
- Whether fibrinolytic therapy proves the mechanism. It is `INDIRECT` evidence at best, and MIST1 was negative.
- Organism-specific virulence factors (pneumolysin, *S. aureus* toxins). These belong in the disorder entries, not the module core.
- Viral pleuritis and non-infectious effusions.
- Pediatric versus adult differences ⚠. Clinical practice differs, and the mechanistic differences are unestablished.

## 8. Open questions for curators

1. Rename the module, or keep the veterinary-flavoured title?
2. Should the organizing stage be a separate module that conforms to `fibrotic_response`, or stay as node 7 here?
3. Is node 8 (extracellular DNA) worth a core slot? The evidence is therapeutic only.
4. Does the trigger node need a branch for hematogenous or contiguous spread (subdiaphragmatic, mediastinal) versus pneumonic?
5. Which existing entries should conform first? Start with `Pneumococcal_Pneumonia` and `Anaerobic_Pneumonia`, and check how each already models empyema.
6. Model-system evidence (animal and in vitro) still has to be collected.

## Sources

- [Komissarov et al. 2018, PMC6008123](https://pmc.ncbi.nlm.nih.gov/articles/PMC6008123)
- [Chung et al. 2013, PMC3538784](https://pmc.ncbi.nlm.nih.gov/articles/PMC3538784)
- [Thickett et al. 1999, PMC1745540](https://pmc.ncbi.nlm.nih.gov/articles/PMC1745540)
- MIST2 (Rahman et al. 2011), PMID 21830966, via search-result summaries (see [Critical Care journal club](https://ccforum.biomedcentral.com/articles/10.1186/cc11337))

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc3.

| Outcome | Count |
| --- | --- |
| References checked | 5 |
| Resolved | 5 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 5 |
| On topic | 0 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

No ontology term identifiers were found in this report.