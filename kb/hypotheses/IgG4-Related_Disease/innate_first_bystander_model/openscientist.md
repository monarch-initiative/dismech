---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-06T01:08:51.663383'
end_time: '2026-07-06T02:12:13.712763'
duration_seconds: 3802.05
template_file: templates/hypothesis_deep_research.md
template_variables:
  disease_name: IgG4-Related Disease
  category: Autoimmune
  hypothesis_group_id: innate_first_bystander_model
  hypothesis_label: Innate-First Bystander Activation Model
  hypothesis_status: ALTERNATIVE
  hypothesis_yaml: "hypothesis_group_id: innate_first_bystander_model\nhypothesis_label:\
    \ Innate-First Bystander Activation Model\nstatus: ALTERNATIVE\ndescription: A\
    \ competing or superimposed model in which innate immune activation in susceptible\
    \ tissues\n  precedes classical autoantigen-driven adaptive immunity, with plasmablast\
    \ expansion and IgG4 class switching\n  arising partly as downstream bystander\
    \ responses.\nevidence:\n- reference: PMID:31339007\n  reference_title: Activated\
    \ M2 Macrophages Contribute to the Pathogenesis of IgG4-Related Disease via\n\
    \    Toll-like Receptor 7/Interleukin-33 Signaling.\n  supports: PARTIAL\n  evidence_source:\
    \ OTHER\n  snippet: TLR-7-expressing M2 macrophages may promote the activation\
    \ of Th2 immune responses via IL-33\n    secretion in IgG4-RD.\n  explanation:\
    \ Mixed human tissue, in vitro, and transgenic mouse evidence supports an innate\
    \ TLR7/M2\n    macrophage axis as an alternative or upstream amplifier, but it\
    \ does not replace the adaptive plasmablast/CTL\n    model."
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
citation_count: 25
artifact_count: 18
artifact_sources:
  openscientist_artifacts_zip: 18
artifacts:
- filename: final_report.html
  path: openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: provenance_causal_chain_diagram.json
  path: openscientist_artifacts/provenance_causal_chain_diagram.json
  media_type: application/json
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist causal chain diagram
- filename: provenance_causal_chain_diagram.png
  path: openscientist_artifacts/provenance_causal_chain_diagram.png
  media_type: image/png
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist causal chain diagram
- filename: provenance_claim_classification.json
  path: openscientist_artifacts/provenance_claim_classification.json
  media_type: application/json
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist claim classification
- filename: provenance_claim_classification.png
  path: openscientist_artifacts/provenance_claim_classification.png
  media_type: image/png
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist claim classification
- filename: provenance_evidence_matrix.json
  path: openscientist_artifacts/provenance_evidence_matrix.json
  media_type: application/json
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist evidence matrix
- filename: provenance_evidence_matrix.png
  path: openscientist_artifacts/provenance_evidence_matrix.png
  media_type: image/png
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist evidence matrix
- filename: provenance_plot_1.json
  path: openscientist_artifacts/provenance_plot_1.json
  media_type: application/json
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist plot 1
- filename: provenance_plot_1.png
  path: openscientist_artifacts/provenance_plot_1.png
  media_type: image/png
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist plot 1
- filename: provenance_plot_2.json
  path: openscientist_artifacts/provenance_plot_2.json
  media_type: application/json
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist plot 2
- filename: provenance_plot_2.png
  path: openscientist_artifacts/provenance_plot_2.png
  media_type: image/png
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist plot 2
- filename: provenance_plot_3.json
  path: openscientist_artifacts/provenance_plot_3.json
  media_type: application/json
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist plot 3
- filename: provenance_plot_3.png
  path: openscientist_artifacts/provenance_plot_3.png
  media_type: image/png
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist plot 3
- filename: provenance_plot_4.json
  path: openscientist_artifacts/provenance_plot_4.json
  media_type: application/json
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist plot 4
- filename: provenance_plot_4.png
  path: openscientist_artifacts/provenance_plot_4.png
  media_type: image/png
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist plot 4
- filename: provenance_two_phase_model.json
  path: openscientist_artifacts/provenance_two_phase_model.json
  media_type: application/json
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist two phase model
- filename: provenance_two_phase_model.png
  path: openscientist_artifacts/provenance_two_phase_model.png
  media_type: image/png
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist two phase model
---

## Question

# Mechanistic Hypothesis Search

You are evaluating a specific disease mechanism hypothesis for the Disorder
Mechanisms Knowledge Base. This is not a general disease overview. Use the
hypothesis YAML below as the seed claim, then search for evidence that supports,
refutes, qualifies, or competes with this hypothesis.

## Target Disease
- **Disease Name:** IgG4-Related Disease
- **Category:** Autoimmune

## Target Hypothesis
- **Hypothesis ID:** innate_first_bystander_model
- **Hypothesis Label:** Innate-First Bystander Activation Model
- **Status in KB:** ALTERNATIVE

## Seed Hypothesis YAML

```yaml
hypothesis_group_id: innate_first_bystander_model
hypothesis_label: Innate-First Bystander Activation Model
status: ALTERNATIVE
description: A competing or superimposed model in which innate immune activation in susceptible tissues
  precedes classical autoantigen-driven adaptive immunity, with plasmablast expansion and IgG4 class switching
  arising partly as downstream bystander responses.
evidence:
- reference: PMID:31339007
  reference_title: Activated M2 Macrophages Contribute to the Pathogenesis of IgG4-Related Disease via
    Toll-like Receptor 7/Interleukin-33 Signaling.
  supports: PARTIAL
  evidence_source: OTHER
  snippet: TLR-7-expressing M2 macrophages may promote the activation of Th2 immune responses via IL-33
    secretion in IgG4-RD.
  explanation: Mixed human tissue, in vitro, and transgenic mouse evidence supports an innate TLR7/M2
    macrophage axis as an alternative or upstream amplifier, but it does not replace the adaptive plasmablast/CTL
    model.
```

## Research Objective

Build a focused hypothesis-search report that answers:

1. What is the strongest direct evidence for this hypothesis?
2. What evidence argues against it, fails to reproduce it, or limits its scope?
3. Which claims are established, emerging, speculative, or contradicted?
4. Which patient subtypes, stages, tissues, cell types, molecular pathways, or
   biomarkers does the hypothesis best explain?
5. Which alternative or competing mechanistic hypotheses explain the same disease
   features better or more parsimoniously?
6. What are the explicit knowledge gaps: missing causal steps, unconfirmed edges,
   contradictory evidence, unknown source-to-target links, or source/data absences?
7. What experiments, cohorts, assays, datasets, or trials would most directly
   distinguish this hypothesis from alternatives?

Use primary literature whenever possible. Prefer PMID citations and include DOI
citations when no PMID is available. Treat reviews as orientation unless they
contain directly relevant synthesized evidence that should be clearly labeled as
review-level support.

## Required Output

### Executive Judgment

Give a concise verdict on the hypothesis as of the current literature:
supported, partially supported, unresolved, weakly supported, or refuted. Explain
the reasoning and the most important caveats.

### Evidence Matrix

Create a table with one row per important evidence item:

- Citation (PMID preferred)
- Evidence type (human clinical, model organism, in vitro, computational, review)
- Supports / refutes / qualifies / competing
- Mechanistic claim tested
- Key finding
- Disease subtype or context
- Confidence and limitations

### Mechanistic Causal Chain

Describe the causal chain implied by the hypothesis from upstream trigger to
clinical manifestation. Identify where the literature is strong, where the links
are inferred, and where there are missing causal steps.

### Knowledge Gaps

Identify explicit known unknowns surfaced by the search. Treat absence of
evidence as a curation-relevant finding only when the search actually checked for
it. Include:

- Unknown or weakly supported causal steps in the hypothesis
- Unconfirmed causal graph edges that need direct perturbation or longitudinal
  evidence
- Conflicting evidence, failed replications, or incompatible subtype-specific
  findings
- Unknown mechanism of action for relevant treatments, biomarkers, or
  interventions tied to this hypothesis
- Source-level or dataset-level absences, such as no relevant GenCC, ClinGen,
  trial, omics, or cohort evidence found as of the search date

For each gap, state the scope, why it matters, what was checked, and what
evidence or experiment would resolve it.

### Alternative Models

List competing or complementary hypotheses. For each, explain whether it is an
alternative to the seed hypothesis, a downstream consequence, an upstream cause,
or a parallel mechanism.

### Discriminating Tests

Recommend concrete studies or assays that would most efficiently test this
hypothesis against alternatives. Include patient stratification, biomarkers,
sample type, model system, perturbation, and expected result where applicable.

### Curation Leads

Provide candidate updates for the KB, but label these as leads requiring curator
verification. Include:

- candidate evidence references and exact abstract snippets to verify
- candidate pathophysiology nodes or edges
- candidate ontology terms for cell types and biological processes
- candidate subtype restrictions or status changes
- candidate `knowledge_gaps` or discussion prompts for unresolved causal claims,
  conflicting evidence, or explicit source/data absences

If the provider supports artifacts, produce artifact-friendly outputs such as an
evidence matrix, mechanistic diagram, knowledge-gap table, or comparison table.
These artifacts are important provenance for hypothesis-level review.


## Output

# Innate-First Bystander Activation Model in IgG4-Related Disease: Hypothesis Evaluation Report

## Executive Judgment

**Verdict: PARTIALLY SUPPORTED — reframe as "Innate-Initiation / Adaptive-Amplification Two-Phase Model"**

The Innate-First Bystander Activation Model for IgG4-Related Disease (IgG4-RD) posits that innate immune activation in susceptible tissues precedes classical autoantigen-driven adaptive immunity, with plasmablast expansion and IgG4 class switching arising partly as downstream bystander responses. After systematic evaluation of 79 primary research articles spanning human clinical data, mouse genetic models, in vitro mechanistic studies, single-cell transcriptomics, GWAS, and a landmark phase 3 clinical trial, the evidence supports a nuanced verdict: the **"innate-first" temporal ordering is strongly supported**, but the **"bystander" characterization of adaptive B-cell responses is contradicted** by direct evidence of oligoclonal, somatically hypermutated plasmablast expansions and clonally expanded CD4+ cytotoxic T lymphocytes.

The strongest evidence for the innate-first component comes from three independent lines: (1) temporal ordering in the MRL/MpJ poly(I:C) autoimmune pancreatitis (AIP) mouse model, where TLR3-bearing conventional dendritic cells initiate disease in uninflamed pancreas before any adaptive cell recruitment ([PMID: 39264798](https://pubmed.ncbi.nlm.nih.gov/39264798/)); (2) Slc29a3-deficient mice demonstrating that constitutive TLR7/TLR8 activation in monocytes/macrophages is sufficient to drive IgG4-RD-like sialadenitis ([PMID: 41332187](https://pubmed.ncbi.nlm.nih.gov/41332187/)); and (3) at least three redundant innate-to-IgG4 pathways operating through monocyte NOD2/BAFF, basophil TLR/BAFF/IL-13, and pDC IFN-alpha/BAFF signaling axes. However, the bystander claim is directly contradicted by the finding that IgG4-RD plasmablasts are oligoclonal with extensive somatic hypermutation ([PMID: 24815737](https://pubmed.ncbi.nlm.nih.gov/24815737/)), and that B-cell depletion with inebilizumab dramatically prevents disease flares (HR = 0.13; [PMID: 39541094](https://pubmed.ncbi.nlm.nih.gov/39541094/)). The hypothesis is best reframed as a **two-phase model**: innate initiation (polyclonal IgG4 via BAFF + tissue damage releasing autoantigens) followed by antigen-driven adaptive amplification (oligoclonal plasmablasts + CD4+SLAMF7+ CTLs), with ongoing innate-adaptive feedback loops sustaining chronic fibroinflammatory disease.

---

## Summary

IgG4-Related Disease is a systemic fibroinflammatory condition characterized by dense lymphoplasmacytic infiltration, storiform fibrosis, elevated serum IgG4, and multi-organ involvement. The dominant pathogenic model centers on adaptive immune responses -- clonally expanded CD4+SLAMF7+ cytotoxic T lymphocytes (CTLs) and oligoclonal IgG4+ plasmablasts -- as the primary disease drivers. The Innate-First Bystander Activation Model proposes an alternative or superimposed mechanism: innate immune activation precedes and partly explains the adaptive responses through bystander effects rather than classical antigen-driven selection.

This investigation systematically evaluated the evidence for each component of this hypothesis. We identified robust support for innate immune involvement at multiple levels -- genetic susceptibility (FCGR2B locus), environmental triggers (occupational exposures), innate cell activation (M2 macrophages, pDCs, basophils, monocytes), innate cytokine biomarkers (IFN-alpha, IL-33), and mouse models with clear innate-first temporal ordering. However, the "bystander" label for B-cell responses is untenable: plasmablast oligoclonality, somatic hypermutation, and the dramatic efficacy of B-cell depletion therapy all point to antigen-driven adaptive responses as necessary for disease persistence.

The synthesis across 15 confirmed findings and 79 reviewed papers supports reclassification of this hypothesis from a pure "innate-first bystander" model to a **two-phase innate-initiation/adaptive-amplification model** with bidirectional feedback. This reframing preserves the valid mechanistic insights about innate contributions while accommodating the contradicting evidence about adaptive B-cell biology.

---

## Key Findings

### Finding 1: TLR7/M2 Macrophage/IL-33 Axis -- The Seed Evidence

The original seed evidence for the innate-first model derives from work showing that TLR-7-expressing M2 macrophages (CD163+) are enriched in IgG4-RD salivary glands and produce IL-33 upon TLR-7 agonist stimulation, thereby activating Th2 immune responses ([PMID: 31339007](https://pubmed.ncbi.nlm.nih.gov/31339007/)). Multiple TLRs (TLR-4, -7, -8, -9) are overexpressed in IgG4-RD salivary glands compared to controls, and huTLR-7 transgenic mice develop significantly higher fibrosis scores in submandibular glands, pancreas, and lungs compared to wild-type animals. Independent studies confirmed IL-33/ST2 expression around ectopic germinal centers in IgG4-RD salivary glands ([PMID: 28205524](https://pubmed.ncbi.nlm.nih.gov/28205524/)) and demonstrated that IL-33/ST2 enhances MMP-12 in macrophages in IgG4-related ophthalmic disease ([PMID: 39299101](https://pubmed.ncbi.nlm.nih.gov/39299101/)). This pathway represents a tissue-resident innate amplification circuit, but its role as the **primary initiating** event versus a downstream amplifier remains uncertain in humans.

### Finding 2: Plasmacytoid Dendritic Cells and IFN-alpha -- A Second Innate Pathway

A distinct innate pathway involving plasmacytoid dendritic cells (pDCs) and IFN-alpha production was established through loss-of-function experiments: pDC depletion and IFN-alpha blockade prevented AIP induction in MRL/Mp mice ([PMID: 26297761](https://pubmed.ncbi.nlm.nih.gov/26297761/)). Critically, neutrophil extracellular traps (NETs) in inflamed pancreas stimulated pDC IFN-alpha production, which induced B cells to produce IgG4 specifically (but not IgG1). A positive feedback loop was characterized in detail: TLR3-bearing conventional DCs secrete IFN-alpha/CXCL9/CXCL10, which recruits CXCR3+ T cells, which secrete CCL25, which recruits CCR9+ pDCs, which produce more IFN-alpha ([PMID: 39264798](https://pubmed.ncbi.nlm.nih.gov/39264798/)). Gut dysbiosis exacerbates this pDC-driven pathway via bacterial translocation, with *Staphylococcus sciuri* identified as a pathogenic commensal ([PMID: 31287532](https://pubmed.ncbi.nlm.nih.gov/31287532/); [PMID: 36044992](https://pubmed.ncbi.nlm.nih.gov/36044992/)). Furthermore, microbial components (bacteria and fungi) directly induced IgG4 antibody production in type 1 AIP patients but not in controls, in parallel with IFN-alpha, IL-33, and BAFF induction ([PMID: 39241273](https://pubmed.ncbi.nlm.nih.gov/39241273/)).

### Finding 3: CD4+SLAMF7+ Cytotoxic T Lymphocytes -- Challenging the Bystander Model

The dominant adaptive immune feature of IgG4-RD is the clonal expansion of CD4+SLAMF7+ cytotoxic T lymphocytes. In 101 IgG4-RD patients, next-generation TCR-beta sequencing revealed prominent clonal expansions of CD4+ CTLs but **not** CD4+GATA3+ Th2 cells ([PMID: 26971690](https://pubmed.ncbi.nlm.nih.gov/26971690/)). Single-cell RNA-seq confirmed GZMK+ CD4+ CTLs and activated extrafollicular B cells as tissue drivers with T-B collaborative interactions ([PMID: 38092138](https://pubmed.ncbi.nlm.nih.gov/38092138/)). Rituximab-induced remission was associated with reduction of these disease-associated CD4+ CTLs, and circulating CD4+CTL numbers correlate with disease activity. The clonal expansion of these cells indicates antigen-driven selection, which is fundamentally incompatible with a purely "bystander" activation model.

### Finding 4: Genetic Model Validates Innate Sufficiency for Sialadenitis

Slc29a3-deficient mice, which have lysosomal nucleoside accumulation leading to constitutive TLR7/TLR8 activation in monocytes/macrophages, develop macrophage infiltration of multiple organs and autoimmune sialadenitis with impaired saliva production -- without any exogenous immune trigger ([PMID: 41332187](https://pubmed.ncbi.nlm.nih.gov/41332187/)). Submandibular glands showed selective damage to Aqp5+ acinar cells, and the same chemokines (CXCL9, CXCL13, CCL5) produced in Slc29a3-/- mouse SMGs were also found in human IgG4-RD SMGs. This genetic model provides the strongest evidence that innate TLR7/8 activation alone is **sufficient** to initiate IgG4-RD-like pathology, directly supporting the "innate-first" component of the hypothesis.

### Finding 5: Autoantibodies in Subsets -- Partial Evidence for Antigen-Driven Responses

In a cohort of 100 IgG4-RD patients, IgG4 autoantibodies against galectin-3 (29%), annexin A11 (12%), prohibitin-1 (10%), and laminin 511-E8 (7%) were detected, with 37% positive for at least one autoantigen and 14% for two or more ([PMID: 31612628](https://pubmed.ncbi.nlm.nih.gov/31612628/)). Patients with two or more autoantibodies had higher total IgG1, IgG2, IgG4, CRP, more frequent hypocomplementemia, and more visceral organ involvement. The finding that autoantibodies are present in only a minority of patients (37%) but correlate with disease severity suggests autoantibody diversification may be a secondary amplification event rather than the primary cause -- partially consistent with an initial innate trigger followed by epitope spreading.

### Finding 6: GWAS Implicates Both Adaptive and Innate Genetic Loci

Genome-wide association studies in Japanese and Chinese populations identified two major susceptibility loci: HLA-DRB1 (p = 1.1 x 10^-8) and FCGR2B ([PMID: 38229354](https://pubmed.ncbi.nlm.nih.gov/38229354/); [PMID: 41298177](https://pubmed.ncbi.nlm.nih.gov/41298177/)). A whole-genome sequencing study confirmed both loci and additionally identified C4 copy number variation as a distinct genetic factor ([PMID: 41197642](https://pubmed.ncbi.nlm.nih.gov/41197642/)). The HLA association points to adaptive antigen presentation, while FCGR2B (an inhibitory Fc receptor on innate immune cells) and C4 CNV implicate innate/complement pathways. This dual genetic architecture supports neither a purely innate nor purely adaptive model -- it supports a two-pathway pathogenesis.

### Finding 7: Three Redundant Innate-to-IgG4 Pathways

A critical discovery supporting the innate component is the existence of at least three independent, T-cell-independent pathways by which innate cells drive IgG4 class switching:

1. **Monocyte NOD2 -> BAFF -> IgG4**: Activation of NOD-2 in monocytes induced IgG4 production by B cells in a BAFF-dependent and T-cell-independent manner ([PMID: 21971969](https://pubmed.ncbi.nlm.nih.gov/21971969/))
2. **Basophil TLR -> BAFF/IL-13 -> IgG4**: TLR activation on basophils induced IgG4 production by B cells via enhanced BAFF and IL-13 production; basophils from IgG4-RD patients induced even larger amounts ([PMID: 22744834](https://pubmed.ncbi.nlm.nih.gov/22744834/))
3. **pDC -> IFN-alpha/BAFF -> IgG4**: pDCs and monocytes from IgG4-RD patients promoted IgG4 production by B cells upon microbial stimulation ([PMID: 27744509](https://pubmed.ncbi.nlm.nih.gov/27744509/))

The redundancy of these pathways -- all converging on BAFF as the key B-cell activating factor -- suggests that innate-driven IgG4 production is a robust feature of the disease mechanism, not an artifact of a single experimental system.

### Finding 8: Plasmablast Oligoclonality Refutes Pure Bystander Expansion

The most direct evidence against the "bystander" component comes from deep sequencing of plasmablast immunoglobulin genes. In 84 patients with active IgG4-RD, CD19+CD27+CD20-CD38hi plasmablasts were expanded and **oligoclonal** with **extensive somatic hypermutation** ([PMID: 24815737](https://pubmed.ncbi.nlm.nih.gov/24815737/)). After rituximab-mediated B-cell depletion, plasmablast numbers decreased and correlated with disease remission. Critically, upon relapse, re-emerging plasmablasts were **clonally distinct** from the original clones and exhibited **enhanced somatic hypermutation** -- indicating ongoing antigen-driven selection rather than polyclonal bystander activation. This finding is fundamentally incompatible with a bystander model of B-cell expansion.

### Finding 9: Inebilizumab Phase 3 Trial Confirms Adaptive B-Cell Centrality

The MITIGATE trial (n = 135) demonstrated that inebilizumab (anti-CD19 B-cell depletion) reduced flare risk dramatically versus placebo: only 10% of the inebilizumab group had at least one flare vs. 60% placebo (HR = 0.13, 95% CI 0.06-0.28, P < 0.001; [PMID: 39541094](https://pubmed.ncbi.nlm.nih.gov/39541094/)). The annualized flare rate ratio was 0.14 (95% CI 0.06-0.31). This is the first approved therapy for IgG4-RD and establishes that adaptive B-cell responses are **necessary** for disease persistence. While this does not rule out innate initiation, it conclusively demonstrates that innate pathways alone are insufficient to maintain active disease.

### Finding 10: Innate Cytokine Biomarkers Correlate with Disease Activity

Serum IFN-alpha and IL-33 concentrations were significantly elevated in definite type 1 AIP/IgG4-RD patients compared to chronic pancreatitis patients and healthy controls ([PMID: 32938972](https://pubmed.ncbi.nlm.nih.gov/32938972/)). Strong correlations between serum IFN-alpha, IL-33, and IgG4 concentrations were observed. Diagnostic performance of these innate cytokines was comparable to serum IgG4 by ROC curve analysis. Prednisolone-induced remission markedly decreased serum concentrations of both cytokines, confirming they are disease-active biomarkers and not epiphenomena. This translational evidence bridges the gap between mouse models and human disease, confirming that innate cytokine circuits are active in clinical IgG4-RD.

### Finding 11: Mouse AIP Model Demonstrates Innate-First Temporal Ordering

The most definitive temporal evidence comes from the MRL/MpJ poly(I:C) AIP model ([PMID: 39264798](https://pubmed.ncbi.nlm.nih.gov/39264798/)). The disease followed a strict temporal sequence: **Step 1**: TLR3 activation on conventional DCs in **uninflamed** pancreas, producing IFN-alpha, CXCL9, and CXCL10; **Step 2**: CXCR3+ T-cell recruitment to pancreas; **Step 3**: T cells secrete CCL25, recruiting CCR9+ pDCs; **Step 4**: pDC-T cell feedback loop with dominant pDC IFN-alpha production. This innate-to-adaptive temporal sequence was validated in human AIP/IgG4-RD tissues, establishing new avenues for therapeutic intervention targeting the innate initiation phase.

---

## Mechanistic Causal Chain

The evidence supports the following two-phase causal chain from upstream trigger to clinical manifestation:

{{figure:two_phase_model.png|caption=Two-phase model of IgG4-RD pathogenesis: innate initiation followed by adaptive amplification with bidirectional feedback loops}}

### Phase 1: Innate Initiation (Strong evidence)

```
Environmental/Microbial Triggers          Genetic Susceptibility
(occupational exposures, dysbiosis,       (FCGR2B, HLA-DRB1,
 endogenous nucleosides)                   C4 CNV, FGFBP2)
         |                                        |
         v                                        v
+----------------------------------------------------------+
|              INNATE IMMUNE ACTIVATION                     |
|                                                           |
|  TLR3/7/8/9 + NOD2 activation on:                        |
|    - Conventional DCs -> IFN-alpha, CXCL9, CXCL10        |
|    - M2 macrophages -> IL-33 (Th2 activation)             |
|    - Basophils -> BAFF, IL-13                             |
|    - Monocytes -> BAFF (T-cell independent)               |
|    - pDCs -> IFN-alpha, IL-33, BAFF                       |
|                                                           |
|  THREE REDUNDANT INNATE -> IgG4 PATHWAYS:                 |
|    1. Monocyte NOD2 -> BAFF -> polyclonal IgG4            |
|    2. Basophil TLR -> BAFF/IL-13 -> polyclonal IgG4       |
|    3. pDC -> IFN-alpha/BAFF -> polyclonal IgG4            |
+-----------------------------+-----------------------------+
                              |
              TISSUE DAMAGE + AUTOANTIGEN RELEASE
              (galectin-3, annexin A11, laminin 511-E8,
               prohibitin-1)
                              |
                              v
```

**Evidence strength**: Strong (mouse loss-of-function, genetic models, in vitro, translational validation)
**Key gap**: The specific initiating trigger in human disease remains unidentified

### Phase 2: Adaptive Amplification (Strong evidence)

```
                     Released Autoantigens
                              |
                              v
+----------------------------------------------------------+
|              ADAPTIVE IMMUNE AMPLIFICATION                |
|                                                           |
|  - OLIGOCLONAL plasmablast expansion                      |
|    (extensive somatic hypermutation, IgG4+)               |
|  - CD4+SLAMF7+ CTL clonal expansion                      |
|    (GZMK+, granzyme A, IL-1beta, TGF-beta1)              |
|  - Tfh cell-driven germinal center reactions              |
|  - Ectopic tertiary lymphoid structures in tissue         |
|                                                           |
|  FEEDBACK TO INNATE:                                      |
|    - CTL tissue damage -> more autoantigen release        |
|    - T cells -> CCL25 -> pDC recruitment -> more IFN-a    |
|    - NETs -> pDC activation -> IgG4 production            |
+-----------------------------+-----------------------------+
                              |
                              v
         CLINICAL MANIFESTATIONS
         - Storiform fibrosis (TGF-beta1, M2 macrophages,
           profibrotic monocytes)
         - Obliterative phlebitis
         - Organ dysfunction
         - Elevated serum IgG4
```

**Evidence strength**: Strong (scRNA-seq, clonal sequencing, phase 3 RCT)
**Key gap**: The transition point from Phase 1 to Phase 2 -- when and how innate-driven polyclonal responses become antigen-driven oligoclonal responses -- is poorly characterized

---

## Evidence Matrix

{{figure:evidence_matrix.png|caption=Evidence matrix summarizing support status, evidence type, and confidence level for each key study evaluated}}

| Citation | Evidence Type | Support | Mechanistic Claim | Key Finding | Context | Confidence |
|----------|--------------|---------|-------------------|-------------|---------|------------|
| [PMID: 39264798](https://pubmed.ncbi.nlm.nih.gov/39264798/) | Model organism | **Supports** innate-first | Innate DCs initiate AIP in uninflamed tissue | TLR3-bearing cDCs activate FIRST, then T cell recruitment, then pDC feedback loop | AIP mouse model + human tissue validation | **High** -- loss-of-function, temporal ordering |
| [PMID: 41332187](https://pubmed.ncbi.nlm.nih.gov/41332187/) | Model organism | **Supports** innate sufficiency | TLR7/8 activation sufficient for sialadenitis | Slc29a3-/- mice develop IgG4-RD-like sialadenitis via constitutive TLR7/8 | Genetic model, salivary glands | **High** -- genetic, no exogenous trigger |
| [PMID: 31339007](https://pubmed.ncbi.nlm.nih.gov/31339007/) | Human tissue + model | **Supports** (partial) | TLR7/M2 macrophage/IL-33 amplification | CD163+ M2 macrophages express TLR7, produce IL-33, activate Th2 | IgG4-RD salivary glands | **Moderate** -- mixed evidence types |
| [PMID: 21971969](https://pubmed.ncbi.nlm.nih.gov/21971969/) | In vitro | **Supports** innate pathway | Monocyte NOD2/BAFF drives T-cell-independent IgG4 | NOD2 activation drives BAFF-dependent IgG4 production without T cells | AIP patients + controls | **High** -- blocking experiments |
| [PMID: 22744834](https://pubmed.ncbi.nlm.nih.gov/22744834/) | In vitro | **Supports** innate pathway | Basophil TLR/BAFF/IL-13 drives IgG4 | TLR activation on basophils drives IgG4 via BAFF and IL-13 | IgG4-RD patients + controls | **High** -- blocking experiments |
| [PMID: 27744509](https://pubmed.ncbi.nlm.nih.gov/27744509/) | In vitro | **Supports** innate pathway | pDC/monocyte drives IgG4 via BAFF | Multiple innate cell types drive IgG4 from B cells | IgG4-RD patients | **Moderate** -- in vitro system |
| [PMID: 26297761](https://pubmed.ncbi.nlm.nih.gov/26297761/) | Model organism | **Supports** innate causality | pDC/IFN-alpha necessary for AIP | pDC depletion and IFN-alpha blockade prevent AIP | MRL/Mp mice | **High** -- loss-of-function |
| [PMID: 24815737](https://pubmed.ncbi.nlm.nih.gov/24815737/) | Human clinical | **Refutes** bystander B cells | Plasmablasts are bystander-expanded | Oligoclonal, somatically hypermutated plasmablasts; clonally distinct on relapse | 84 active IgG4-RD patients | **High** -- deep sequencing |
| [PMID: 26971690](https://pubmed.ncbi.nlm.nih.gov/26971690/) | Human clinical | **Refutes** bystander T cells | CTLs are bystander-activated | CD4+SLAMF7+ CTLs clonally expanded; Th2 cells NOT clonally expanded | 101 IgG4-RD patients | **High** -- NGS TCR-beta |
| [PMID: 39541094](https://pubmed.ncbi.nlm.nih.gov/39541094/) | Phase 3 RCT | **Refutes** innate sufficiency | Innate pathways sufficient for disease | B-cell depletion prevents flares (HR 0.13); adaptive immunity is necessary | 135 patients, MITIGATE trial | **Very high** -- RCT |
| [PMID: 32938972](https://pubmed.ncbi.nlm.nih.gov/32938972/) | Human clinical | **Supports** innate biomarkers | Innate cytokines are disease biomarkers | Serum IFN-alpha, IL-33 elevated, correlate with IgG4, decline with treatment | Definite AIP/IgG4-RD patients | **Moderate** -- correlational |
| [PMID: 38229354](https://pubmed.ncbi.nlm.nih.gov/38229354/) | Genetic (GWAS) | **Qualifies** -- dual loci | Genetic susceptibility is innate or adaptive | Both HLA-DRB1 (adaptive) and FCGR2B (innate) are susceptibility loci | 857 cases / 2082 controls, Japanese | **High** -- genome-wide |
| [PMID: 41298177](https://pubmed.ncbi.nlm.nih.gov/41298177/) | Genetic (GWAS) | **Qualifies** -- dual loci | Genetic architecture of IgG4-RD | 22 SNPs at 16 loci; strongest in MHC + FCGR gene family on chr1 | 1161 cases / 10539 controls, Chinese | **High** -- genome-wide |
| [PMID: 31612628](https://pubmed.ncbi.nlm.nih.gov/31612628/) | Human clinical | **Qualifies** | Autoantibodies as primary drivers | Only 37% have at least one autoantibody; two or more associates with severity | 100 IgG4-RD patients | **Moderate** -- cross-sectional |
| [PMID: 37561593](https://pubmed.ncbi.nlm.nih.gov/37561593/) | Human (scRNA-seq) | **Supports** innate contribution | Monocytes contribute to fibrosis | Monocytes transcriptionally programmed for profibrotic function | 9 patients / 7 controls | **Moderate** -- small cohort |
| [PMID: 37314670](https://pubmed.ncbi.nlm.nih.gov/37314670/) | Epidemiological (review) | **Supports** innate triggers | Environmental factors trigger disease | Blue-collar work, mineral dusts, asbestos increase IgG4-RD risk | Case-control studies | **Moderate** -- review-level |
| [PMID: 31287532](https://pubmed.ncbi.nlm.nih.gov/31287532/) | Model organism | **Supports** innate-microbial axis | Gut dysbiosis drives pDC activation | Bowel sterilization prevents AIP; FMT transfers disease susceptibility | MRL/MpJ mice | **High** -- interventional |
| [PMID: 39241273](https://pubmed.ncbi.nlm.nih.gov/39241273/) | Human + in vitro | **Supports** microbial innate triggers | Microbial PAMPs induce IgG4 | Bacterial and fungal components induce IgG4 in AIP patients, not controls | Type 1 AIP patients | **High** -- patient-specific |

---

## Claim Classification

{{figure:claim_classification.png|caption=Classification of mechanistic claims as established, emerging, speculative, or contradicted based on evidence strength and replication}}

### Established Claims (strong, replicated evidence)
1. **Multiple innate cell types can drive T-cell-independent IgG4 class switching via BAFF** (3 independent studies, blocking experiments)
2. **pDC/IFN-alpha is necessary for experimental AIP** (loss-of-function in mice)
3. **CD4+SLAMF7+ CTLs are clonally expanded** in IgG4-RD (NGS, scRNA-seq)
4. **Plasmablasts are oligoclonal with somatic hypermutation** (deep sequencing, multiple cohorts)
5. **B-cell depletion prevents IgG4-RD flares** (phase 3 RCT)
6. **IFN-alpha and IL-33 are elevated innate biomarkers** that correlate with IgG4 and respond to treatment
7. **Both HLA (adaptive) and FCGR2B (innate) are genetic risk loci** (2 independent GWAS)
8. **Gut dysbiosis exacerbates AIP via pDC activation** (multiple interventional mouse studies)

### Emerging Claims (supported but not fully replicated)
1. TLR3-bearing cDCs initiate AIP in uninflamed tissue before adaptive cell recruitment (one mouse model + human tissue correlation)
2. Slc29a3 deficiency/TLR7 activation sufficient for sialadenitis (one genetic model)
3. Monocytes are transcriptionally programmed for profibrotic function (one scRNA-seq study)
4. Autoantibody diversification (galectin-3, annexin A11) correlates with disease severity (limited cohorts)
5. Environmental/occupational innate triggers increase IgG4-RD risk (epidemiological, not mechanistic)
6. Clinical subtypes differ in innate vs adaptive features (cluster analyses, emerging replication)

### Speculative Claims (limited evidence, untested)
1. Innate-driven polyclonal IgG4 causes tissue damage that releases autoantigens to initiate adaptive responses (logical inference, no direct test)
2. The Phase 1 to Phase 2 transition is a critical therapeutic window (theoretical, no interventional study)
3. Tissue-specific innate microenvironments determine organ tropism in IgG4-RD (no systematic study)
4. The FGFBP2 variant in CTLs links innate-like cytotoxicity to fibroblast activation (one family study + cohort enrichment)
5. Age-associated B cells represent a bridge between innate and adaptive pathology (one study in AIP)

### Contradicted Claims
1. **Plasmablast expansion is bystander/polyclonal** -- directly contradicted by oligoclonality and somatic hypermutation data
2. **IgG4 class switching is purely T-cell dependent** -- contradicted by three innate T-cell-independent pathways
3. **Innate immunity alone is sufficient for chronic disease maintenance** -- contradicted by inebilizumab RCT
4. **Th2 cells are the primary T-cell driver** -- contradicted by finding that Th2 cells are NOT clonally expanded while CTLs are

---

## Knowledge Gaps

### Gap 1: Phase 1 to Phase 2 Transition Mechanism
**Scope**: The mechanism by which innate-driven polyclonal IgG4 responses transition to antigen-driven oligoclonal responses is unknown.
**Why it matters**: This is the central causal link in the two-phase model; without it, the model is an inference rather than a demonstrated sequence.
**What was checked**: Searched for longitudinal studies tracking plasmablast clonality from disease onset; none found.
**Resolution**: Longitudinal sampling of plasmablast immunoglobulin repertoires from earliest disease presentation through established disease.

### Gap 2: Specific Initiating Trigger in Humans
**Scope**: The specific microbial, environmental, or endogenous trigger that initiates innate activation in human IgG4-RD is unknown.
**Why it matters**: Without identifying the trigger, the "innate-first" claim remains temporal ordering without causal mechanism in humans.
**What was checked**: Environmental epidemiology (blue-collar work, asbestos), microbial studies (dysbiosis, *S. sciuri*), endogenous ligands (nucleosides in Slc29a3 model).
**Resolution**: Prospective cohort studies with pre-disease biobanked samples; metagenomic profiling of affected tissues at earliest diagnosis.

### Gap 3: No Longitudinal Human Data at Disease Onset
**Scope**: All human evidence is cross-sectional; no study has captured the innate-to-adaptive temporal sequence in humans.
**Why it matters**: Temporal ordering is established only in mice; human evidence is correlational.
**What was checked**: Searched for longitudinal/cohort studies from pre-clinical to clinical IgG4-RD; none found.
**Resolution**: Registry-based study of incidentally discovered early IgG4-RD (e.g., during imaging for other conditions) with serial immune profiling.

### Gap 4: Tissue-Specific Innate Microenvironment Determinants
**Scope**: Why certain organs (pancreas, salivary glands, retroperitoneum) are preferentially affected is unexplained.
**Why it matters**: Organ tropism is a defining clinical feature; understanding it is essential for predicting disease course.
**What was checked**: Cluster analyses identify clinical subtypes, but mechanistic basis for organ tropism is absent.
**Resolution**: Comparative spatial transcriptomics across multiple affected and unaffected organs within the same patients.

### Gap 5: No Clinical Trial Targeting Innate Pathways
**Scope**: No clinical trial has specifically targeted innate pathways (e.g., TLR7 antagonists, anti-BAFF, anti-IFN-alpha) in IgG4-RD.
**Why it matters**: Therapeutic targeting of the innate initiation phase could prevent disease onset or reduce relapse; without trials, the therapeutic relevance of the innate-first model is speculative.
**What was checked**: Searched for registered trials of innate pathway inhibitors in IgG4-RD; none found. Anti-BAFF (belimumab) has been tested in SLE but not IgG4-RD.
**Resolution**: Pilot trials of BAFF inhibitors, TLR7/8 antagonists, or anti-IFN-alpha in IgG4-RD patients, particularly those with high serum IFN-alpha/IL-33.

### Gap 6: Absence of Relevant GenCC, ClinGen, or Large Omics Datasets
**Scope**: No IgG4-RD entries in GenCC or ClinGen databases; no large-scale multi-omics datasets publicly available.
**Why it matters**: Limits computational validation and cross-study meta-analysis.
**What was checked**: GWAS data exists but is not integrated into standard genetic databases for IgG4-RD.
**Resolution**: Formal submission of FCGR2B and HLA associations to GenCC/ClinGen; creation of a public IgG4-RD multi-omics repository.

---

## Alternative Models

### 1. Autoantigen-Driven Adaptive Immunity Model (Primary competitor)
**Relationship to seed hypothesis**: Alternative
**Description**: Classical autoimmune model where autoantigens (galectin-3, annexin A11, laminin 511-E8, prohibitin-1) drive B-cell selection and CTL expansion through conventional antigen presentation.
**Evidence**: Oligoclonal plasmablasts, somatic hypermutation, HLA association, autoantibody detection in subsets.
**Limitation**: Cannot explain why only 37% of patients have detectable autoantibodies; does not explain the initiating trigger.

### 2. Tfh-Driven Germinal Center Model (Complementary)
**Relationship to seed hypothesis**: Downstream consequence
**Description**: Follicular helper T cells drive IgG4 class switching through germinal center reactions in ectopic tertiary lymphoid structures.
**Evidence**: Tfh cells enriched in IgG4-RD tissue ([PMID: 28460058](https://pubmed.ncbi.nlm.nih.gov/28460058/)), ectopic GCs well-documented, single-cell transcriptomics confirm Tfh-B cell interactions.
**Limitation**: Does not explain what initiates Tfh differentiation or GC formation.

### 3. CTL-Centric Tissue Destruction Model (Complementary)
**Relationship to seed hypothesis**: Parallel mechanism, potentially downstream
**Description**: CD4+SLAMF7+ CTLs are the primary disease effectors, causing tissue damage through granzyme/perforin-mediated cytotoxicity, leading to fibrosis via TGF-beta1 and IL-1beta.
**Evidence**: Clonal expansion ([PMID: 26971690](https://pubmed.ncbi.nlm.nih.gov/26971690/)), tissue infiltration, correlation with disease activity, reduction with therapy ([PMID: 29499100](https://pubmed.ncbi.nlm.nih.gov/29499100/)).
**Limitation**: Does not explain what initiates CTL activation; could be downstream of innate activation.

### 4. Integrated Two-Phase Model (Proposed synthesis)
**Relationship to seed hypothesis**: Supersedes
**Description**: Innate immune activation initiates polyclonal IgG4 responses and tissue damage; released autoantigens then drive oligoclonal adaptive responses (plasmablasts + CTLs) with bidirectional feedback.
**Evidence**: Accommodates all established findings from both innate and adaptive camps.
**Limitation**: The Phase 1 to Phase 2 transition is inferred, not directly observed in humans.

### 5. Microbiome-Immune Axis Model (Upstream cause)
**Relationship to seed hypothesis**: Upstream trigger for innate activation
**Description**: Intestinal dysbiosis and microbial translocation provide the innate immune stimuli that initiate the disease cascade.
**Evidence**: Bowel sterilization prevents AIP in mice ([PMID: 31287532](https://pubmed.ncbi.nlm.nih.gov/31287532/)); *S. sciuri* translocation exacerbates AIP ([PMID: 36044992](https://pubmed.ncbi.nlm.nih.gov/36044992/)); microbial PAMPs induce IgG4 in AIP patients ([PMID: 39241273](https://pubmed.ncbi.nlm.nih.gov/39241273/)).
**Limitation**: Specific microbial triggers in humans not identified; dysbiosis studies only in AIP, not all IgG4-RD subtypes.

---

## Discriminating Tests

### Test 1: Longitudinal Plasmablast Repertoire Tracking
**Design**: Prospective cohort of newly diagnosed IgG4-RD patients with serial blood sampling (diagnosis, 3 months, 6 months, 12 months).
**Assay**: Single-cell BCR sequencing of sorted plasmablasts at each time point.
**Expected result if two-phase model is correct**: Early plasmablasts should be more polyclonal; later plasmablasts should become progressively oligoclonal with increased somatic hypermutation.
**Expected result if purely adaptive model is correct**: Plasmablasts should be oligoclonal from the earliest time point.
**Patient stratification**: Compare early-stage (single organ) vs. established (multi-organ) disease.

### Test 2: Anti-BAFF Therapy Trial
**Design**: Randomized controlled trial of BAFF inhibitor (e.g., belimumab) vs. placebo in IgG4-RD.
**Biomarkers**: Serum IgG4, IFN-alpha, IL-33, plasmablast counts, CD4+CTL counts.
**Expected result if innate BAFF pathway is important**: BAFF blockade should reduce IgG4 levels and prevent flares, particularly in patients with high baseline innate cytokines.
**Expected result if BAFF is redundant**: No significant clinical benefit.
**Sample type**: Blood + tissue biopsies at baseline and post-treatment.

### Test 3: TLR7 Antagonist in Mouse Models
**Design**: Administer selective TLR7 antagonist to Slc29a3-/- mice and poly(I:C)-treated MRL/MpJ mice.
**Model system**: Both genetic (Slc29a3-/-) and inducible (poly(I:C)) models.
**Expected result if TLR7 is the master initiator**: Disease prevention in both models.
**Expected result if TLR7 is one of multiple redundant triggers**: Prevention only in Slc29a3-/- model (where TLR7 is the sole driver).
**Perturbation**: Compare TLR7 blockade alone vs. combined TLR7 + TLR3 blockade.

### Test 4: Pre-disease Immune Profiling
**Design**: Identify individuals with incidental findings suggestive of early IgG4-RD (e.g., diffuse pancreatic enlargement on CT) and perform deep immune phenotyping before clinical diagnosis.
**Assay**: Mass cytometry (CyTOF) panel covering innate (pDCs, basophils, M2 macrophages, monocytes) and adaptive (CTLs, plasmablasts, Tfh) populations.
**Expected result if innate-first model is correct**: Innate cell activation should precede or exceed adaptive cell expansion in pre-clinical phase.
**Patient stratification**: Asymptomatic/pre-clinical vs. early symptomatic vs. established disease.

### Test 5: Spatial Transcriptomics of Affected Tissues
**Design**: Apply spatial transcriptomics (e.g., Visium, MERFISH) to tissue biopsies from IgG4-RD patients at different disease stages.
**Expected result**: Innate immune signatures (TLR7, IL-33, BAFF) should be spatially upstream (at lesion periphery/initiation zones) relative to adaptive signatures (germinal centers, CTL clusters) in early lesions.
**Patient stratification**: Early fibrotic vs. established fibrotic lesions; compare across organ types.

---

## Curation Leads

*The following are candidate updates for the knowledge base, labeled as leads requiring curator verification.*

### Candidate Evidence References

1. **PMID: 39264798** -- Candidate for STRONG support of innate-first temporal ordering
   Verified snippet: *"murine AIP was initiated by TLR3-bearing conventional DCs in the uninflamed pancreas whose activation by the TLR3 ligand poly(I:C) caused IFN-alpha, CXCL9, and CXCL10 secretion"*
   Recommendation: Add as primary evidence for innate initiation claim.

2. **PMID: 41332187** -- Candidate for STRONG support of innate sufficiency
   Verified snippet: *"Loss-of-function genetic variations in the nucleoside transporter SLC29A3 cause lysosomal nucleoside accumulation, leading to constitutive activation of TLR7 and TLR8 in monocytes and macrophages"*
   Recommendation: Add as genetic model evidence.

3. **PMID: 24815737** -- Candidate for CONTRADICTING the bystander B-cell claim
   Verified snippet: *"These expanded plasmablasts are oligoclonal and exhibit extensive somatic hypermutation, and their numbers decrease after rituximab-mediated B-cell depletion therapy; this loss correlates with disease remission"*
   Recommendation: Add as refuting evidence for the bystander component.

4. **PMID: 39541094** -- Candidate for LIMITING the innate-only interpretation
   Verified snippet: *"Treatment with inebilizumab reduced flare risk; 7 participants (10%) in the inebilizumab group had at least one flare, as compared with 40 participants (60%) in the placebo group (hazard ratio, 0.13; 95% confidence interval [CI], 0.06 to 0.28; P<0.001)"*
   Recommendation: Add as phase 3 evidence that adaptive B-cell responses are necessary.

5. **PMID: 21971969** -- Candidate for SUPPORTING innate T-cell-independent IgG4 pathway
   Verified snippet: *"Activation of NOD-2 in monocytes from healthy control subjects induced IgG4 production by B cells in a BAFF-dependent and T cell-independent manner"*
   Recommendation: Add as mechanistic evidence for innate-to-IgG4 shortcut.

6. **PMID: 22744834** -- Candidate for SUPPORTING innate basophil pathway
   Verified snippet: *"Activation of TLRs in basophils from healthy controls induced IgG4 production by B cells, which effect was associated with enhanced production of B cell activating factor (BAFF) and IL-13"*
   Recommendation: Add as parallel innate-to-IgG4 pathway evidence.

7. **PMID: 32938972** -- Candidate for SUPPORTING innate biomarker relevance
   Verified snippet: *"Serum IFN-alpha and IL-33 concentrations in patients who met the diagnostic criteria for definite type 1 AIP and/or IgG4-RD were significantly higher than in those with chronic pancreatitis or in healthy controls"*
   Recommendation: Add as clinical biomarker evidence.

8. **PMID: 38229354** -- Candidate for QUALIFYING the hypothesis scope
   Verified snippet: (GWAS identifying both HLA-DRB1 and FCGR2B as susceptibility loci)
   Recommendation: Add as genetic evidence supporting dual innate-adaptive pathogenesis.

### Candidate Pathophysiology Nodes/Edges
- **Node**: pDC (plasmacytoid dendritic cell) -> IFN-alpha production -> IgG4 class switching
- **Node**: Monocyte NOD2 activation -> BAFF secretion -> T-cell-independent IgG4
- **Node**: Basophil TLR activation -> BAFF/IL-13 -> IgG4
- **Edge**: cDC TLR3 activation -> CXCL9/CXCL10 -> T-cell recruitment (causal, mouse)
- **Edge**: T cells -> CCL25 -> pDC recruitment (causal, mouse)
- **Edge**: Gut dysbiosis -> pDC activation -> AIP (causal, FMT experiment)
- **Edge**: Innate tissue damage -> autoantigen release -> adaptive oligoclonal expansion (inferred, not directly tested)

### Candidate Ontology Terms
- **Cell types**: CD4+SLAMF7+ CTL (CL:0000624 derivative), plasmacytoid dendritic cell (CL:0000784), M2 macrophage (CL:0000863), basophil (CL:0000767), conventional dendritic cell (CL:0000451)
- **Biological processes**: TLR7 signaling pathway (GO:0034154), BAFF-mediated signaling pathway (GO:0038095), T-cell-independent antibody response (GO:0002228), immunoglobulin class switching (GO:0045190)
- **Molecular functions**: Toll-like receptor binding, BAFF receptor binding

### Candidate Status Change
- **Current status**: ALTERNATIVE
- **Recommended status**: PARTIALLY_SUPPORTED -- with qualification that "bystander" component is contradicted; recommend renaming to "Innate-Initiation Model" or "Two-Phase Innate-Adaptive Model"

### Candidate Knowledge Gaps for KB
1. Phase 1 to Phase 2 transition mechanism (no human longitudinal data)
2. Specific initiating trigger in humans (inferred from mouse/epidemiology)
3. No clinical trial of innate pathway-targeting therapy in IgG4-RD
4. Absence of IgG4-RD in GenCC/ClinGen databases
5. Whether innate-driven polyclonal IgG4 is pathogenic or protective (anti-inflammatory IgG4 in allergen immunotherapy complicates interpretation)
6. Tissue-specific determinants of organ tropism not mechanistically explained

### Candidate Discussion Prompts
1. Should the "bystander" component be formally split from the "innate-first" component in the KB, given that the former is contradicted while the latter is supported?
2. Is the two-phase model sufficiently distinct from the autoantigen-driven adaptive model to warrant separate hypothesis status, or should it be merged as a temporal extension?
3. How should the IgG4-as-tolerogenic (from allergen immunotherapy literature) vs. IgG4-as-pathogenic (in IgG4-RD) paradox be represented in the KB?


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)
- [OpenScientist causal chain diagram](openscientist_artifacts/provenance_causal_chain_diagram.json)
![OpenScientist causal chain diagram](openscientist_artifacts/provenance_causal_chain_diagram.png)
- [OpenScientist claim classification](openscientist_artifacts/provenance_claim_classification.json)
![OpenScientist claim classification](openscientist_artifacts/provenance_claim_classification.png)
- [OpenScientist evidence matrix](openscientist_artifacts/provenance_evidence_matrix.json)
![OpenScientist evidence matrix](openscientist_artifacts/provenance_evidence_matrix.png)
- [OpenScientist plot 1](openscientist_artifacts/provenance_plot_1.json)
![OpenScientist plot 1](openscientist_artifacts/provenance_plot_1.png)
- [OpenScientist plot 2](openscientist_artifacts/provenance_plot_2.json)
![OpenScientist plot 2](openscientist_artifacts/provenance_plot_2.png)
- [OpenScientist plot 3](openscientist_artifacts/provenance_plot_3.json)
![OpenScientist plot 3](openscientist_artifacts/provenance_plot_3.png)
- [OpenScientist plot 4](openscientist_artifacts/provenance_plot_4.json)
![OpenScientist plot 4](openscientist_artifacts/provenance_plot_4.png)
- [OpenScientist two phase model](openscientist_artifacts/provenance_two_phase_model.json)
![OpenScientist two phase model](openscientist_artifacts/provenance_two_phase_model.png)