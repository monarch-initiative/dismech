---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-11-09T00:26:54.692943'
end_time: '2026-11-09T00:40:10.179178'
duration_seconds: 795.49
template_file: templates/module_mechanism_research.md
template_variables:
  module_name: Chemical Respiratory Allergy Module
  module_slug: chemical_respiratory_allergy
  category: Module
  module_description: 'Conserved pathophysiology of chemical respiratory allergy (respiratory
    sensitization) induced by low molecular weight chemical sensitizers such as acid
    anhydrides (trimellitic anhydride, maleic anhydride), diisocyanates (TDI, MDI,
    HDI), reactive dyes, persulfate salts and chloramine-T, presenting clinically
    as occupational asthma and rhinitis. The chain runs: covalent haptenation of airway
    proteins by a reactive electrophile; airway epithelial danger signal release and
    barrier perturbation; dendritic cell activation and Th2-polarizing antigen presentation;
    hapten-specific Th2 effector and memory response; and airway hyperresponsiveness
    with variable airflow limitation. The module shares its covalent protein binding
    molecular initiating event with the skin sensitization AOP (AOP 40) and diverges
    downstream in the tissue compartment, the cytokine polarization and the effector
    outcome. Key conformance target is the dendritic cell activation node.'
  pathophysiology_summary: '- Covalent Protein Haptenation by Low Molecular Weight
    Sensitizer: a reactive electrophilic chemical binds nucleophilic residues on airway
    proteins, including secreted mucins and epithelial surface proteins, generating
    a hapten-protein adduct. Role trigger.

    - Airway Epithelial Danger Signal Release: haptenated epithelium releases IL-8,
    IL-6, IL-1beta and reactive oxygen species, loses MUC1 expression and shows junctional
    and apoptotic change. Role amplifier.

    - Dendritic Cell Activation and Th2-Polarizing Antigen Presentation: airway dendritic
    cells take up the hapten-protein adduct, mature, upregulate costimulatory molecules
    and present in a Th2-polarizing context; endothelial adhesion molecule expression
    recruits further cells. Role central_effector and key conformance target.

    - Hapten-Specific Th2 Effector and Memory Response: hapten-specific T cell expansion
    with IL-4, IL-5 and IL-13, eosinophil recruitment, and for high molecular weight
    and some low molecular weight sensitizers specific IgE. Role effector.

    - Airway Hyperresponsiveness and Variable Airflow Limitation: on re-exposure,
    bronchoconstriction, airway hyperresponsiveness and the clinical picture of occupational
    asthma. Role consequence.'
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
citation_count: 31
reference_validation:
  total_references: 31
  verified: 31
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 1
  quotes_valid: 1
  relevance_assessed: 31
  on_topic: 15
  validator_version: 0.5.1
term_validation:
  total_terms: 15
  verified: 15
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: chemical_respiratory_allergy-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: chemical_respiratory_allergy-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Mechanism Module Research Template

## Target Module
- **Module Name:** Chemical Respiratory Allergy Module
- **Module Slug:** chemical_respiratory_allergy
- **Category:** Module

## Current Module Description

Conserved pathophysiology of chemical respiratory allergy (respiratory sensitization) induced by low molecular weight chemical sensitizers such as acid anhydrides (trimellitic anhydride, maleic anhydride), diisocyanates (TDI, MDI, HDI), reactive dyes, persulfate salts and chloramine-T, presenting clinically as occupational asthma and rhinitis. The chain runs: covalent haptenation of airway proteins by a reactive electrophile; airway epithelial danger signal release and barrier perturbation; dendritic cell activation and Th2-polarizing antigen presentation; hapten-specific Th2 effector and memory response; and airway hyperresponsiveness with variable airflow limitation. The module shares its covalent protein binding molecular initiating event with the skin sensitization AOP (AOP 40) and diverges downstream in the tissue compartment, the cytokine polarization and the effector outcome. Key conformance target is the dendritic cell activation node.

## Current Provisional Nodes

- Covalent Protein Haptenation by Low Molecular Weight Sensitizer: a reactive electrophilic chemical binds nucleophilic residues on airway proteins, including secreted mucins and epithelial surface proteins, generating a hapten-protein adduct. Role trigger.
- Airway Epithelial Danger Signal Release: haptenated epithelium releases IL-8, IL-6, IL-1beta and reactive oxygen species, loses MUC1 expression and shows junctional and apoptotic change. Role amplifier.
- Dendritic Cell Activation and Th2-Polarizing Antigen Presentation: airway dendritic cells take up the hapten-protein adduct, mature, upregulate costimulatory molecules and present in a Th2-polarizing context; endothelial adhesion molecule expression recruits further cells. Role central_effector and key conformance target.
- Hapten-Specific Th2 Effector and Memory Response: hapten-specific T cell expansion with IL-4, IL-5 and IL-13, eosinophil recruitment, and for high molecular weight and some low molecular weight sensitizers specific IgE. Role effector.
- Airway Hyperresponsiveness and Variable Airflow Limitation: on re-exposure, bronchoconstriction, airway hyperresponsiveness and the clinical picture of occupational asthma. Role consequence.

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

# Chemical Respiratory Allergy Module — Mechanism Research Report

**Module slug:** `chemical_respiratory_allergy`
**Category:** Mechanism Module (reusable; multiple gene-axis disease entries conform to it)
**Date:** 2026-11-09
**Scope of investigation:** 5 iterations · 10 confirmed findings · 42 papers reviewed

---

## Summary

The Chemical Respiratory Allergy module describes a **well-conserved, literature-supported causal mechanism** that is, in effect, identical to the formally published **Adverse Outcome Pathway (AOP) for respiratory sensitization**. The AOP structures the process as four key events — KE1: binding of the respiratory sensitizer to a protein; KE2: activation of lung epithelial cells; KE3: activation of dendritic cells; KE4: T-cell response — which map one-to-one onto the module's provisional nodes, with a fifth node (airway hyperresponsiveness/variable airflow limitation) added as the adverse clinical outcome ([PMID: 40189662](https://pubmed.ncbi.nlm.nih.gov/40189662/)). This gives the module a strong external scaffold: the proposed DAG is not speculative but reflects an established regulatory toxicology framework. The dendritic cell activation node (KE3) is correctly chosen as the conformance target, because it is the mechanistic hinge between innate danger signaling and adaptive Th2 polarization.

The best-supported shared mechanism runs: a **low-molecular-weight (LMW) electrophilic sensitizer** (diisocyanates, acid anhydrides, reactive dyes, persulfate salts, chloramine-T) covalently haptenates — or, for some agents, oxidatively modifies — nucleophilic residues on airway and self proteins, generating neoantigens ([PMID: 26853746](https://pubmed.ncbi.nlm.nih.gov/26853746/), [PMID: 15778257](https://pubmed.ncbi.nlm.nih.gov/15778257/)). The haptenated epithelium releases danger signals (IL-8, IL-6, IL-1β, ROS) and stress proteins ([PMID: 29717106](https://pubmed.ncbi.nlm.nih.gov/29717106/)). Airway dendritic cells mature via an oxidative-stress/ERK pathway, upregulating maturation (CD83) and Th2-polarizing (OX40L) markers ([PMID: 24742817](https://pubmed.ncbi.nlm.nih.gov/24742817/)). The result is a hapten-specific **Th2** effector and memory response (IL-4/IL-5/IL-13, eosinophilia), which on re-exposure produces airway hyperresponsiveness and variable airflow limitation — the clinical picture of occupational asthma and rhinitis ([PMID: 31071364](https://pubmed.ncbi.nlm.nih.gov/31071364/), [PMID: 33474863](https://pubmed.ncbi.nlm.nih.gov/33474863/)).

Two scope refinements are recommended. First, the name is better framed around **"respiratory sensitization"** than "allergy," and the module should remain **restricted to LMW chemical sensitizers**, explicitly excluding high-molecular-weight (protein) allergens and irritant/non-immunologic ("RADS") occupational asthma. Second, **specific IgE should be an optional, sensitizer-dependent branch, not a core requirement**, because it is reliably induced by acid anhydrides (e.g., trimellitic anhydride) but is absent in roughly three-quarters of diisocyanate asthmatics ([PMID: 20545707](https://pubmed.ncbi.nlm.nih.gov/20545707/)). Genetic factors (HLA class II, GST isoforms, CTNNA3) and molecular markers (SOD1, HMOX1, CD83, OX40L) are **susceptibility modifiers that map onto existing core nodes** rather than defining new ones ([PMID: 36276967](https://pubmed.ncbi.nlm.nih.gov/36276967/)).

---

## Key Findings

### Finding 1 — The molecular initiating event is covalent haptenation (and oxidative modification) of airway/self proteins by LMW electrophiles

The module's trigger node is strongly supported. Diisocyanates (TDI, HDI, MDI) react covalently with human serum albumin (HSA) and hemoglobin to form haptenated neoantigens. The chemistry is bivalent and cross-linking: MDI binds 5–6 mol per mol of HSA within the first minute of reaction and produces both inter- and intramolecular cross-linking visible on SDS-PAGE ([PMID: 2979744](https://pubmed.ncbi.nlm.nih.gov/2979744/), [PMID: 26853746](https://pubmed.ncbi.nlm.nih.gov/26853746/), [PMID: 23743149](https://pubmed.ncbi.nlm.nih.gov/23743149/)). As the primary source states, *"Diisocyanates (dNCOs) are low molecular weight chemical sensitizers that react with autologous proteins to produce neoantigens"* ([PMID: 26853746](https://pubmed.ncbi.nlm.nih.gov/26853746/)).

Structure–activity relationship (SAR) analyses generalize this across sensitizer classes. In a comparison of 78 LMW asthmagens versus 301 controls, *"nitrogen or oxygen containing functional groups such as isocyanate, amine, acid anhydride, and carbonyl were associated with an occupational asthma hazard, particularly when the functional group was present twice or more in the same molecule"* — the model correctly classified 90% of compounds, with external validation sensitivity 86% and specificity 99% ([PMID: 15778257](https://pubmed.ncbi.nlm.nih.gov/15778257/)). Mechanistic SAR profilers confirm the basis is *"electrophilic reaction chemistry and protein cross-linking potential"* ([PMID: 28177949](https://pubmed.ncbi.nlm.nih.gov/28177949/)). The requirement for ≥2 electrophilic groups per molecule aligns with the cross-linking chemistry observed for diisocyanates and underpins the "reactive electrophile" wording in the node.

**Curation note:** the MIE wording should admit **oxidative protein modification** alongside covalent adduction, because persulfate salts act substantially through oxidative chemistry rather than classical nucleophilic adduction (see Findings 6 and 9). This shared MIE is also the point of overlap with the skin sensitization AOP (AOP 40), from which this module diverges downstream.

### Finding 2 — The full causal chain to Th2 and airway hyperresponsiveness is demonstrated in diisocyanate mouse models

The causal edges from sensitization through Th2 effector response to the airway hyperresponsiveness (AHR) consequence are experimentally demonstrated. In BALB/c mice, dermal sensitization with 0.5% TDI followed by repeated airway (intranasal/oropharyngeal) TDI challenge produces a pronounced Th2 cytokine response (IL-4/IL-5/IL-13), eosinophilic airway inflammation, and AHR to methacholine. Critically, repeated airway TDI exposure **without** prior dermal sensitization yields only a mixed Th1/Th2 response and **no AHR** — establishing that prior sensitization is causally required for the Th2/AHR outcome: *"when mice are first dermally sensitized with TDI, followed by repeated intranasal TDI challenges, this results in a pronounced Th2 response and AHR. Dermal exposure to TDI determines airway hyperreactivity after repeated airway exposure to TDI"* ([PMID: 31071364](https://pubmed.ncbi.nlm.nih.gov/31071364/)).

A companion study confirms the effector and consequence nodes and documents the cellular players: *"prior dermal sensitization with TDI alone results in AHR and predominant eosinophilic airway inflammation, accompanied by a typical type 2 helper T (Th2) cytokine profile,"* with recruitment of dendritic cells and ILC2 to the lung ([PMID: 33474863](https://pubmed.ncbi.nlm.nih.gov/33474863/)). This is the strongest in vivo causal evidence tying the upstream nodes to the clinical consequence, and it also demonstrates that **route of sensitization (dermal)** can drive respiratory outcome — biologically important for a module that shares its MIE with skin sensitization.

### Finding 3 — Th2 cytokine polarization is the defining divergence from contact (Th1) sensitizers

The module's central claim — that chemical respiratory sensitizers present antigen in a **Th2-polarizing** context — is supported by cross-species cytokine fingerprinting. The reference respiratory allergen trimellitic anhydride (TMA) elicits high Th2-type IL-10 and IL-13 (and IL-4) with low Th1 IL-12/IFN-γ, whereas the reference contact allergen DNCB elicits the converse Th1 phenotype (all cytokines differed P<0.01 in BALB/c mice): *"TMA-activated LNC isolated from BALB/c mice or BN rats elaborated high levels of the Th2-type cytokines interleukin (IL)-10 and IL-13, but relatively little of the Th1-type cytokines IL-12 or interferon gamma"* ([PMID: 12419703](https://pubmed.ncbi.nlm.nih.gov/12419703/)).

Flow cytometry corroborates Th2/IgE skewing specific to the respiratory sensitizer: *"An increased proportion of IgE+ cells correlated to total serum IgE level and an enhancement of MHC II molecule expression were observed in the lymph node B lymphocytes from TMA-treated mice. The percentage of IL-4-producing CD4+ lymphocytes and the IL-4 receptor expression were clearly higher following TMA exposure"* ([PMID: 15922011](https://pubmed.ncbi.nlm.nih.gov/15922011/)). This Th1-vs-Th2 contrast is the mechanistic justification for keeping chemical respiratory and chemical contact sensitization as distinct modules sharing only the MIE.

### Finding 4 — The airway epithelial danger-signal (amplifier) node is supported by human airway epithelial data

The epithelial danger-signal node (KE2) is supported in human airway epithelial cells (HAECs). Stimulation with a TDI–HSA conjugate induces dose-dependent release of the stress proteins clusterin and progranulin that positively correlates with IL-8, accompanied by intracellular ROS production: *"TDI-human serum albumin stimulation induced significant CLU/PGRN release from HAECs in a dose-dependent manner, which positively correlated with IL-8 and folliculin levels"* ([PMID: 29717106](https://pubmed.ncbi.nlm.nih.gov/29717106/)). The same work links epithelial oxidative stress causally to disease: *"Toluene diisocyanate (TDI) exposure induces oxidative stress and epithelial cell-derived inflammation, which affect the pathogenesis of TDI-induced occupational asthma."* In TDI-occupational-asthma patients, serum clusterin/progranulin are significantly reduced versus exposed and healthy controls (P<0.05), providing a human clinical correlate. Reviews reinforce the epithelium as the orchestrating hub: *"Airway epithelial cells are the first to encounter diisocyanates and orchestrate various responses, such as cytokine release, oxidative stress generation, and autoantibody formation"* ([PMID: 23324746](https://pubmed.ncbi.nlm.nih.gov/23324746/)).

### Finding 5 — The dendritic cell activation node (KE3, conformance target) is molecularly supported via oxidative-stress/ERK signaling

The conformance-target node is supported at the molecular level. In human DC-like THP-1 cells, the respiratory sensitizer HDI inhibits cytoplasmic superoxide dismutase 1 (SOD1, P<0.05), raising superoxide (O2⁻, P<0.001), which drives ERK phosphorylation (~6-fold, P<0.001) and transcriptional upregulation of detoxification/protection genes and the DC maturation marker CD83: *"Increased O2(-) levels promote ERK phosphorylation (approx sixfold compared to control; P < 0.001) and downstream transcriptional increase of several genes: HMOX1 (P < 0.05)... MDR1 (P < 0.01)... and CD83 (P < 0.05), a DC maturation marker"* ([PMID: 24742817](https://pubmed.ncbi.nlm.nih.gov/24742817/)). This links the haptenation/oxidative-stress events directly to DC maturation.

The **Th2-polarizing** quality of antigen presentation is additionally discriminated in vitro by OX40L: a 3D dendritic cell coculture system distinguishes chemical respiratory from contact sensitizers by OX40L expression in DCs ([PMID: 28824649](https://pubmed.ncbi.nlm.nih.gov/28824649/)). Because OX40L is an established Th2-polarizing costimulatory ligand, its selective induction by respiratory sensitizers provides a molecular basis for the "Th2-polarizing antigen presentation" element of the node — and makes OX40L a candidate conformance biomarker for KE3. Costimulatory molecules CD80/CD86 and MHC II are the classical maturation outputs also required for sensitization ([PMID: 18313130](https://pubmed.ncbi.nlm.nih.gov/18313130/)).

### Finding 6 — Specific IgE is a variable/optional branch, not a core requirement

The evidence sharply distinguishes two sensitizer subgroups. For **diisocyanates**, allergen-specific IgE is *"reportedly absent in a large portion of affected individuals"* — detectable in only ~25% of diisocyanate asthmatics ([PMID: 20545707](https://pubmed.ncbi.nlm.nih.gov/20545707/)). By contrast, **acid anhydrides (TMA)** reliably induce specific and total serum IgE in both mice and Brown Norway rats ([PMID: 15922011](https://pubmed.ncbi.nlm.nih.gov/15922011/), [PMID: 11893415](https://pubmed.ncbi.nlm.nih.gov/11893415/), [PMID: 11807923](https://pubmed.ncbi.nlm.nih.gov/11807923/)). Reviews describe diisocyanate-OA as a complex interaction of innate and adaptive immune responses in which airway epithelial cells orchestrate cytokine release, oxidative stress and autoantibody formation ([PMID: 23324746](https://pubmed.ncbi.nlm.nih.gov/23324746/)). The practical consequence for the module is clear: **IgE cannot be a required conformance node**; it should be modeled as an optional sensitizer-dependent branch off the Th2 effector node.

### Finding 7 — The published respiratory-sensitization AOP validates the module DAG

The module's architecture matches a formally published AOP: *"The adverse outcome pathway for respiratory sensitization consists of key event (KE) 1: binding of the respiratory sensitizer to a protein, KE2: activation of lung epithelial cells, KE3: activation of dendritic cells, and KE4: T-cell response"* ([PMID: 40189662](https://pubmed.ncbi.nlm.nih.gov/40189662/)). This framework was applied experimentally to accepted respiratory sensitizers (piperazine, chloramine-T, TDI) in a human bronchial (Calu-3) air–liquid interface model. Complementary work shows MDI reprograms human alveolar macrophages/epithelium, enhancing IL-1α/IL-1β and chemokines: *"chemokine production (CCL2, CCL5, CXCL8) was enhanced, suggesting macrophage-mediated modulation of epithelial responses and immune cell recruitment potential"* ([PMID: 42203024](https://pubmed.ncbi.nlm.nih.gov/42203024/)) — supporting the KE2 danger-signal/recruitment element and implicating macrophages as a supporting (non-core) innate cell type.

### Finding 8 — Genetic susceptibility maps onto antigen-processing, detoxification, and oxidative-stress nodes

Only a subset of exposed workers develops disease, and genetics determine susceptibility rather than the mechanism itself. A systematic review with meta-analysis (22 studies, 943 comparisons, 82 genes/serotypes) found diisocyanate-asthma-associated genes cluster in *"antigen processing, lymphocyte activation, cytokine production regulation, and response to oxidative stress"*; meta-analyzed markers included CTNNA3, GSTM1/GSTP1 and HLA class II serotypes ([PMID: 36276967](https://pubmed.ncbi.nlm.nih.gov/36276967/)). These functional categories map directly onto existing core nodes (DC antigen presentation, Th2 effector, epithelial oxidative danger signal), confirming that susceptibility genes are **modifiers of**, not **additions to**, the conserved chain.

### Finding 9 — Human evidence: a single LMW sensitizer causes multi-organ allergic disease through a shared T-cell mechanism

Direct human evidence links one causal agent to multiple clinical manifestations through a common adaptive mechanism. In a hairdresser who developed contact dermatitis, rhinoconjunctivitis, and delayed-onset bronchial asthma after persulfate exposure, patch testing gave a delayed cutaneous reaction, nasal challenge reduced airflow at 24 h, and *"a significant proliferation of T cells to bleaching powder was reproducibly found by a lymphocyte proliferation analysis"* ([PMID: 10227340](https://pubmed.ncbi.nlm.nih.gov/10227340/)). This supports the module's premise that a shared T-cell-mediated mechanism underlies skin and respiratory manifestations of the same sensitizer — the conceptual link to AOP 40. A similar multi-manifestation picture (asthma, rhinitis, urticaria, positive skin prick tests) is reported for the novel LMW sensitizer BCMBA ([PMID: 29175989](https://pubmed.ncbi.nlm.nih.gov/29175989/)).

### Finding 10 — OX40L on dendritic cells discriminates chemical respiratory sensitizers in vitro

A 3D dendritic cell coculture system distinguishes chemical respiratory and contact sensitizers by OX40L expression in dendritic cells ([PMID: 28824649](https://pubmed.ncbi.nlm.nih.gov/28824649/)). OX40L (TNFSF4) is an established Th2-polarizing costimulatory ligand, so its selective induction by respiratory sensitizers provides a molecular readout for the "Th2-polarizing antigen presentation" element of the DC conformance node and a candidate discriminating biomarker between the respiratory (Th2) and contact (Th1) branches. *(Abstract truncated in retrieval — flagged for full-text verification of effect sizes.)*

---

## Mechanistic Model / Interpretation

The module is best represented as a linear DAG mirroring the published respiratory-sensitization AOP, with two optional branches hanging off the effector node and susceptibility modifiers annotated at the relevant nodes.

```
  [N1] Covalent/oxidative protein haptenation         (TRIGGER / KE1)
       by LMW electrophilic sensitizer
       — isocyanate, acid anhydride, reactive dye,
         persulfate (oxidative), chloramine-T
                     |
                     v
  [N2] Airway epithelial danger-signal release         (AMPLIFIER / KE2)
       IL-8, IL-6, IL-1β, ROS; stress proteins
       (clusterin, progranulin); barrier/MUC1 change
                     |
                     v
  [N3] Dendritic cell activation + Th2-polarizing       (CENTRAL EFFECTOR / KE3)
       antigen presentation                              ***CONFORMANCE TARGET***
       SOD1↓ → O2⁻↑ → ERK-P → CD83↑; OX40L↑;
       costimulation (CD80/CD86), MHC II
                     |
                     v
  [N4] Hapten-specific Th2 effector + memory            (EFFECTOR / KE4)
       IL-4, IL-5, IL-13; eosinophil recruitment
          |                         |
          | (optional, sensitizer- | (optional)
          |  dependent)            |
          v                         v
   [B1] Specific IgE           [B2] ILC2 amplification
   (acid anhydrides: yes;      of type-2 inflammation
    diisocyanates: ~25%)
                     |
                     v
  [N5] Airway hyperresponsiveness +                     (CONSEQUENCE)
       variable airflow limitation
       → occupational asthma / rhinitis
```

### Node roles and conformance recommendation

| Node | Role | Core / Optional | AOP mapping | Conformance evidence |
|------|------|-----------------|-------------|----------------------|
| N1 Haptenation (covalent **or** oxidative) | trigger | **Core/required** | KE1 | SAR + protein-adduct chemistry ([PMID: 15778257](https://pubmed.ncbi.nlm.nih.gov/15778257/), [PMID: 26853746](https://pubmed.ncbi.nlm.nih.gov/26853746/)) |
| N2 Epithelial danger signal | amplifier | **Core/required** | KE2 | HAEC IL-8/ROS/stress proteins ([PMID: 29717106](https://pubmed.ncbi.nlm.nih.gov/29717106/)) |
| N3 DC activation + Th2 presentation | central_effector | **Core/required (conformance target)** | KE3 | CD83/OX40L induction ([PMID: 24742817](https://pubmed.ncbi.nlm.nih.gov/24742817/), [PMID: 28824649](https://pubmed.ncbi.nlm.nih.gov/28824649/)) |
| N4 Hapten-specific Th2 effector/memory | effector | **Core/required** | KE4 | Th2 cytokine fingerprint, mouse AHR ([PMID: 12419703](https://pubmed.ncbi.nlm.nih.gov/12419703/), [PMID: 31071364](https://pubmed.ncbi.nlm.nih.gov/31071364/)) |
| B1 Specific IgE | effector branch | **Optional / sensitizer-dependent** | — | Absent in ~75% of dNCO asthma ([PMID: 20545707](https://pubmed.ncbi.nlm.nih.gov/20545707/)) |
| B2 ILC2 type-2 amplification | effector branch | **Optional** | — | ILC2 recruitment in TDI model ([PMID: 33474863](https://pubmed.ncbi.nlm.nih.gov/33474863/)) |
| N5 AHR / variable airflow limitation | consequence | **Core/required** | adverse outcome | Methacholine AHR in sensitized mice ([PMID: 31071364](https://pubmed.ncbi.nlm.nih.gov/31071364/)) |

### Key causal edges and their evidence

- **N1 → N2:** TDI–HSA adduct drives epithelial IL-8/ROS/stress-protein release ([PMID: 29717106](https://pubmed.ncbi.nlm.nih.gov/29717106/)).
- **N2 → N3:** Oxidative stress (SOD1 inhibition → superoxide → ERK) drives DC maturation marker CD83 ([PMID: 24742817](https://pubmed.ncbi.nlm.nih.gov/24742817/)); epithelial/macrophage chemokines recruit immune cells ([PMID: 42203024](https://pubmed.ncbi.nlm.nih.gov/42203024/)).
- **N3 → N4:** Th2-polarizing DC phenotype (OX40L) precedes Th2 cytokine effector response ([PMID: 28824649](https://pubmed.ncbi.nlm.nih.gov/28824649/), [PMID: 12419703](https://pubmed.ncbi.nlm.nih.gov/12419703/)).
- **N4 → N5:** Prior sensitization is causally required for AHR; unsensitized airway exposure gives no AHR ([PMID: 31071364](https://pubmed.ncbi.nlm.nih.gov/31071364/), [PMID: 33474863](https://pubmed.ncbi.nlm.nih.gov/33474863/)).

### Module name and scope recommendation

The current name is acceptable, but the literature better supports **"Chemical (Low-Molecular-Weight) Respiratory Sensitization"** over "allergy," because (a) "sensitization" is the regulatory/AOP term, and (b) "allergy" implies IgE mediation that is frequently absent for diisocyanates. The scope should remain **restricted to LMW chemical sensitizers**. Classification reviews are explicit that chemical respiratory allergy must be separated from protein (HMW) allergy and from non-immunologic irritant-induced asthma: chemical respiratory allergy resulting in occupational asthma must be identified "accurately" and distinguished "from chemicals that cause occupational asthma through non-immunological mechanisms" ([PMID: 33831493](https://pubmed.ncbi.nlm.nih.gov/33831493/)).

### Relationship to the skin sensitization AOP (AOP 40)

The module **shares its MIE** (N1 / covalent protein binding) with skin sensitization but **diverges at N2–N4**: a different tissue compartment (airway vs skin), **Th2** vs **Th1** cytokine polarization, and asthma/rhinitis vs contact dermatitis outcome ([PMID: 12419703](https://pubmed.ncbi.nlm.nih.gov/12419703/), [PMID: 15922011](https://pubmed.ncbi.nlm.nih.gov/15922011/)). The persulfate case demonstrates that a single agent can traverse both pathways via a shared T-cell mechanism ([PMID: 10227340](https://pubmed.ncbi.nlm.nih.gov/10227340/)).

### Gene-to-node mapping

| Gene / marker | Node | Functional role | Source |
|---------------|------|-----------------|--------|
| HLA class II serotypes (DQ/DR) | N3 DC antigen presentation | Antigen presentation / susceptibility | [PMID: 36276967](https://pubmed.ncbi.nlm.nih.gov/36276967/) |
| GSTM1, GSTP1 | N1/N2 detox + danger | Glutathione detoxification of electrophiles | [PMID: 36276967](https://pubmed.ncbi.nlm.nih.gov/36276967/) |
| CTNNA3 (α-T-catenin) | N2 (barrier/adhesion) | Epithelial junction / susceptibility | [PMID: 36276967](https://pubmed.ncbi.nlm.nih.gov/36276967/) |
| SOD1 | N3 DC activation | Superoxide dismutase; its inhibition drives ERK/CD83 | [PMID: 24742817](https://pubmed.ncbi.nlm.nih.gov/24742817/) |
| HMOX1, MDR1 (ABCB1) | N2/N3 | Oxidative-stress/xenobiotic detox response | [PMID: 24742817](https://pubmed.ncbi.nlm.nih.gov/24742817/) |
| CD83 | N3 DC activation | DC maturation marker (conformance biomarker) | [PMID: 24742817](https://pubmed.ncbi.nlm.nih.gov/24742817/) |
| TNFSF4 (OX40L) | N3 DC Th2 polarization | Th2-polarizing costimulatory ligand (conformance biomarker) | [PMID: 28824649](https://pubmed.ncbi.nlm.nih.gov/28824649/) |
| CD80 / CD86 | N3 DC activation | Costimulation required for sensitization | [PMID: 18313130](https://pubmed.ncbi.nlm.nih.gov/18313130/) |
| IL4, IL5, IL13, IL10 | N4 Th2 effector | Type-2 cytokines | [PMID: 12419703](https://pubmed.ncbi.nlm.nih.gov/12419703/), [PMID: 33474863](https://pubmed.ncbi.nlm.nih.gov/33474863/) |
| SMAD3 (TGF-β signaling) | N4 (regulatory) | Regulates specific-antibody/cytokine response to TMA | [PMID: 19752570](https://pubmed.ncbi.nlm.nih.gov/19752570/) |
| CLU (clusterin), GRN (progranulin) | N2 | Oxidative-stress-linked epithelial mediators; candidate biomarkers | [PMID: 29717106](https://pubmed.ncbi.nlm.nih.gov/29717106/) |

*Note: all genes listed are **susceptibility modifiers or node biomarkers**, not independent required nodes. HLA, GST, and CTNNA3 are population-level risk factors; SOD1/HMOX1/CD83/OX40L are mechanistic markers of KE2–KE3.*

---

## Evidence Base

The table below stratifies the key literature by evidence type and records the exact supporting quote.

| PMID | Evidence type | Exact quote | Supported claim |
|------|---------------|-------------|-----------------|
| [26853746](https://pubmed.ncbi.nlm.nih.gov/26853746/) | In vitro (chemistry) | "Diisocyanates (dNCOs) are low molecular weight chemical sensitizers that react with autologous proteins to produce neoantigens." | N1 covalent haptenation MIE |
| [15778257](https://pubmed.ncbi.nlm.nih.gov/15778257/) | SAR / computational | "Nitrogen or oxygen containing functional groups such as isocyanate, amine, acid anhydride, and carbonyl were associated with an occupational asthma hazard, particularly when the functional group was present twice or more in the same molecule." | N1 electrophilic/cross-linking chemistry across sensitizers |
| [28177949](https://pubmed.ncbi.nlm.nih.gov/28177949/) | Review / SAR | "mechanistic alerts usually based on electrophilic reaction chemistry and protein cross-linking potential." | N1 mechanistic basis |
| [31071364](https://pubmed.ncbi.nlm.nih.gov/31071364/) | Model organism (mouse) | "when mice are first dermally sensitized with TDI, followed by repeated intranasal TDI challenges, this results in a pronounced Th2 response and AHR." | N4→N5 causal requirement of sensitization |
| [33474863](https://pubmed.ncbi.nlm.nih.gov/33474863/) | Model organism (mouse) | "prior dermal sensitization with TDI alone results in AHR and predominant eosinophilic airway inflammation, accompanied by a typical type 2 helper T (Th2) cytokine profile" | N4/N5 + DC/ILC2 recruitment |
| [12419703](https://pubmed.ncbi.nlm.nih.gov/12419703/) | Model organism (mouse/rat) | "TMA-activated LNC isolated from BALB/c mice or BN rats elaborated high levels of the Th2-type cytokines interleukin (IL)-10 and IL-13, but relatively little of the Th1-type cytokines IL-12 or interferon gamma." | Th2 vs Th1 divergence (respiratory vs contact) |
| [15922011](https://pubmed.ncbi.nlm.nih.gov/15922011/) | Model organism (flow cytometry) | "The percentage of IL-4-producing CD4+ lymphocytes and the IL-4 receptor expression were clearly higher following TMA exposure." | N3/N4 Th2/IgE skewing |
| [29717106](https://pubmed.ncbi.nlm.nih.gov/29717106/) | In vitro + human | "TDI-human serum albumin stimulation induced significant CLU/PGRN release from HAECs in a dose-dependent manner, which positively correlated with IL-8 and folliculin levels." | N2 epithelial danger signal |
| [23324746](https://pubmed.ncbi.nlm.nih.gov/23324746/) | Review | "Airway epithelial cells are the first to encounter diisocyanates and orchestrate various responses, such as cytokine release, oxidative stress generation, and autoantibody formation." | N2 epithelial orchestration; heterogeneous mechanism |
| [20545707](https://pubmed.ncbi.nlm.nih.gov/20545707/) | Review (Pro/Con) | "one important characteristic of hypersensitivity ('allergen'-specific IgE) is reportedly absent in a large portion of affected individuals" | IgE is optional, not core |
| [40189662](https://pubmed.ncbi.nlm.nih.gov/40189662/) | In vitro / AOP framework | "The adverse outcome pathway for respiratory sensitization consists of key event (KE) 1: binding of the respiratory sensitizer to a protein, KE2: activation of lung epithelial cells, KE3: activation of dendritic cells, and KE4: T-cell response." | Validates full DAG + DC conformance target |
| [42203024](https://pubmed.ncbi.nlm.nih.gov/42203024/) | In vitro (human) | "chemokine production (CCL2, CCL5, CXCL8) was enhanced, suggesting macrophage-mediated modulation of epithelial responses and immune cell recruitment potential" | N2 recruitment element (MDI) |
| [24742817](https://pubmed.ncbi.nlm.nih.gov/24742817/) | In vitro (human DC-like) | "Increased O2(-) levels promote ERK phosphorylation... and downstream transcriptional increase of several genes: HMOX1... MDR1... and CD83..., a DC maturation marker." | N3 DC activation via oxidative/ERK |
| [36276967](https://pubmed.ncbi.nlm.nih.gov/36276967/) | Human genetics (meta-analysis) | "Protein network functions for the DA-associated genes from this review include: antigen processing, lymphocyte activation, cytokine production regulation, and response to oxidative stress." | Susceptibility genes map to core nodes |
| [10227340](https://pubmed.ncbi.nlm.nih.gov/10227340/) | Human (case/mechanistic) | "a significant proliferation of T cells to bleaching powder was reproducibly found by a lymphocyte proliferation analysis" | Shared T-cell mechanism across skin + respiratory |
| [28824649](https://pubmed.ncbi.nlm.nih.gov/28824649/) | In vitro (3D DC coculture) | *(title)* "Prediction of Chemical Respiratory and Contact Sensitizers by OX40L Expression in Dendritic Cells Using a Novel 3D Coculture System" — abstract truncated, FLAG full-text | N3 Th2-polarizing DC marker |

**Evidence stratification by type.** *Human clinical / genetic:* PMIDs 10227340, 29175989, 36276967, 32561498, 33831493. *Human in vitro (cells):* 29717106, 24742817, 40189662, 42203024, 28824649. *Model organism (mouse/rat):* 31071364, 33474863, 12419703, 15922011, 11893415, 11807923, 19752570, 19589094, 33618472. *Chemistry / SAR / in silico:* 26853746, 23743149, 2979744, 15778257, 28177949, 27100370, 30090324. *Reviews / AOP methodology:* 23324746, 20545707, 18603401, 28507730, 26500288, 26583909, 39785825, 39450940.

---

## Ontology Suggestions

*Suggested by label; curators must confirm exact IDs — do not import the provisional IDs below without verification.*

**Gene Ontology — biological process (GO BP):**
- *response to xenobiotic stimulus* / *protein modification process* (haptenation) → N1
- *response to oxidative stress* (candidate GO:0006979) → N1/N2
- *inflammatory response*; *interleukin-8 production* → N2
- *dendritic cell differentiation* (candidate GO:0097028); *antigen processing and presentation of peptide antigen via MHC class II*; *positive regulation of T cell activation* → N3
- *T-helper 2 cell differentiation* (candidate GO:0045064); *interleukin-4/5/13 production*; *eosinophil chemotaxis* (candidate GO:0048245); *immunoglobulin production* → N4 (IgE optional)
- *positive regulation of ERK1 and ERK2 cascade* → N3 mechanistic edge
- *bronchoconstriction / regulation of smooth muscle contraction* → N5

**Cell Ontology (CL):**
- *bronchial epithelial cell* (candidate CL:0002328); *goblet cell*; *club cell* → N2
- *dendritic cell* (candidate CL:0000451); *myeloid dendritic cell* (candidate CL:0000782) → N3
- *T-helper 2 cell* (candidate CL:0000546); *CD4-positive, alpha-beta T cell* → N4
- *eosinophil* (candidate CL:0000771); *mast cell*; *B cell / IgE-secreting plasma cell* → N4/B1
- *group 2 innate lymphoid cell / ILC2* (candidate CL:0001069) → B2 optional branch
- *alveolar macrophage* (candidate CL:0000583) → N2 supporting cell
- *airway smooth muscle cell* → N5

**Anatomy (UBERON):**
- *bronchus* (candidate UBERON:0002185); *bronchial epithelium* → N2/N5
- *lung* (candidate UBERON:0002048); *respiratory airway*; *trachea* → N3/N4/N5
- *nasal cavity* (candidate UBERON:0001707) → rhinitis manifestation
- *bronchus-associated / mediastinal (bronchial) lymph node* → N3 priming site
- *skin* (candidate UBERON:0002097) → cross-reference to shared MIE / dermal sensitization route

---

## Out-of-Scope / Boundary Notes

1. **High-molecular-weight (protein) allergens are excluded.** The module is specifically about LMW chemical sensitizers acting via haptenation; protein allergens are reliably IgE-mediated and follow a related but distinct AOP ([PMID: 33831493](https://pubmed.ncbi.nlm.nih.gov/33831493/), [PMID: 28507730](https://pubmed.ncbi.nlm.nih.gov/28507730/)).
2. **Irritant-induced / non-immunologic occupational asthma (RADS) is excluded** — no sensitization, no hapten-specific T cells ([PMID: 32561498](https://pubmed.ncbi.nlm.nih.gov/32561498/), [PMID: 17064651](https://pubmed.ncbi.nlm.nih.gov/17064651/)).
3. **Specific IgE as a required mechanism is out of scope** for the core module; it is a sensitizer-dependent optional branch ([PMID: 20545707](https://pubmed.ncbi.nlm.nih.gov/20545707/)).
4. **ILC2 / innate-only amplification** is supportive but optional; adaptive Th2 priming remains core ([PMID: 33474863](https://pubmed.ncbi.nlm.nih.gov/33474863/)).
5. **microRNA regulation** of diisocyanate-OA is an emerging, mechanistically unsettled layer; keep as modifier, not a node ([PMID: 39450940](https://pubmed.ncbi.nlm.nih.gov/39450940/)).
6. **MUC1 loss and specific junctional/apoptotic detail in N2** are plausible but not corroborated in the retrieved abstracts — **flag for full-text verification** before curating as node detail.
7. **Acute high-dose chemical injury** (e.g., Bhopal methyl isocyanate, [PMID: 19819837](https://pubmed.ncbi.nlm.nih.gov/19819837/)) is distinct from sensitization and excluded.
8. **Inorganic sensitizers (e.g., platinum salts, [PMID: 32153767](https://pubmed.ncbi.nlm.nih.gov/32153767/))** likely act through related reactivity but were not core to this module's chemistry; treat as a separate candidate branch pending curation.

---

## Limitations and Knowledge Gaps

- **No validated predictive assay** exists for chemical respiratory sensitizers; identification relies heavily on human clinical data, so several causal edges rest on animal models and in vitro systems rather than controlled human mechanistic studies ([PMID: 33831493](https://pubmed.ncbi.nlm.nih.gov/33831493/), [PMID: 39785825](https://pubmed.ncbi.nlm.nih.gov/39785825/)).
- **IgE-independent Th2 polarization** for diisocyanates is mechanistically incompletely resolved: how DCs drive a Th2/eosinophilic phenotype without robust IgE is not fully explained; autoantibody and oxidative-stress mechanisms are invoked but not definitively causal ([PMID: 23324746](https://pubmed.ncbi.nlm.nih.gov/23324746/)).
- **Dermal-to-respiratory route** evidence comes largely from mouse models; the degree to which human respiratory sensitization requires or is modified by dermal exposure is uncertain ([PMID: 31071364](https://pubmed.ncbi.nlm.nih.gov/31071364/)).
- **DC conformance marker specificity:** OX40L and CD83 are promising but derive from THP-1 / 3D coculture surrogate systems; primary airway-DC confirmation is a gap ([PMID: 24742817](https://pubmed.ncbi.nlm.nih.gov/24742817/), [PMID: 28824649](https://pubmed.ncbi.nlm.nih.gov/28824649/)).
- **Genetics are associative, not causal:** HLA/GST/CTNNA3 associations come from meta-analysis of heterogeneous studies; effect sizes and replication vary ([PMID: 36276967](https://pubmed.ncbi.nlm.nih.gov/36276967/)).
- **Depth is uneven across sensitizer classes:** mechanistic detail is richest for diisocyanates and TMA; reactive dyes and chloramine-T are supported mainly by inclusion in AOP/air–liquid-interface test frameworks rather than deep mechanism.
- **Abstract-level evidence:** several candidate snippets (MUC1 loss, OX40L effect sizes, AOP air–liquid-interface detail in PMIDs 28824649, 40189662, 42203024) require full-text verification before final curation.

---

## Proposed Follow-up Experiments / Actions (for curators)

1. **Rename** the module to "Chemical (Low-Molecular-Weight) Respiratory Sensitization" (retain "allergy" as a synonym) and codify the LMW-only boundary in the description.
2. **Adopt the KE1–KE4 + outcome DAG** explicitly, cross-linking to the respiratory-sensitization AOP (AOP-Wiki) and noting the shared-MIE relationship to skin-sensitization AOP 40.
3. **Mark N1–N5 as core/required**, and add B1 (specific IgE) and B2 (ILC2) as optional sensitizer-dependent branches with annotated examples (acid anhydrides → IgE positive; diisocyanates → frequently IgE negative).
4. **Expand the MIE node wording** to "covalent haptenation **or** oxidative modification of airway/self proteins" to accommodate persulfate salts.
5. **Designate DC conformance biomarkers** (CD83, OX40L, CD80/CD86, MHC II upregulation in a Th2-polarizing context) for the KE3 conformance target, flagging the need for primary airway-DC validation.
6. **Create a susceptibility-modifier annotation layer** (HLA class II, GSTM1/GSTP1, CTNNA3, SOD1/HMOX1) attached to nodes rather than as independent nodes.
7. **Verify flagged full texts** (PMIDs 28824649, 40189662, 42203024; MUC1-loss claim) before locking evidence snippets.
8. **Confirm ontology IDs** for all GO/CL/UBERON terms above with a curator; do not import provisional IDs without checking.
9. **Curate allele-level detail** (HLA class II alleles, CTNNA3 variants) from the meta-analysis source ([PMID: 36276967](https://pubmed.ncbi.nlm.nih.gov/36276967/)) for the gene-axis disease entries that will conform to this module.

---

*Report compiled from 10 confirmed findings across 5 investigation iterations, grounded in 42 reviewed papers. All causal claims are attributed to the specific PMIDs whose abstracts/snippets support them. This is a literature-synthesis curation report; no primary datasets were provided.*


## Artifacts

- [OpenScientist final report](chemical_respiratory_allergy-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](chemical_respiratory_allergy-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.5.1.

| Outcome | Count |
| --- | --- |
| References checked | 31 |
| Resolved | 31 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 1 |
| Quoted claims found in source | 1 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 31 |
| On topic | 15 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 15 |
| Resolved | 15 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |

Every term resolved, and every label the report gave matched.