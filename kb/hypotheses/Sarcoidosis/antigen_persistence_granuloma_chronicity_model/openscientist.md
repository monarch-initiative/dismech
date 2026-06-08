---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-06-03T11:00:07.217872'
end_time: '2026-06-03T11:40:50.280377'
duration_seconds: 2443.06
template_file: templates/hypothesis_deep_research.md
template_variables:
  disease_name: Sarcoidosis
  category: Immune
  hypothesis_group_id: antigen_persistence_granuloma_chronicity_model
  hypothesis_label: Antigen Persistence / Th17.1 / mTORC1 Granuloma Chronicity Model
  hypothesis_status: EMERGING
  hypothesis_yaml: "hypothesis_group_id: antigen_persistence_granuloma_chronicity_model\n\
    hypothesis_label: Antigen Persistence / Th17.1 / mTORC1 Granuloma Chronicity Model\n\
    status: EMERGING\ndescription: Sarcoidosis is modeled as a genetically conditioned,\
    \ antigen-driven granulomatous immune\n  response in which poorly degradable or\
    \ repeatedly encountered antigens are presented by macrophage-lineage\n  antigen-presenting\
    \ cells to CD4+ T cells. The activated T-cell compartment polarizes toward IFN-gamma-producing\n\
    \  Th17.1/Th1-like effector states while regulatory T-cell restraint is insufficient.\
    \ This cytokine circuit\n  recruits and activates macrophages, promotes epithelioid\
    \ and multinucleated giant-cell granuloma architecture,\n  and intersects with\
    \ macrophage-intrinsic metabolic programs such as mTORC1 activation. Resolution\
    \ is\n  hypothesized to require antigen clearance or sequestration plus restoration\
    \ of regulatory and apoptotic\n  checkpoints; chronic disease and fibrosis occur\
    \ when antigen persistence, Th17.1 feedback, macrophage\n  survival/proliferation,\
    \ and tissue-repair programs remain engaged.\nevidence:\n- reference: PMID:38165044\n\
    \  reference_title: Immune mechanisms of granuloma formation in sarcoidosis and\
    \ tuberculosis.\n  supports: SUPPORT\n  evidence_source: HUMAN_CLINICAL\n  snippet:\
    \ Sarcoidosis is a complex immune-mediated disease characterized by clusters of\
    \ immune cells\n    called granulomas.\n  explanation: |\n    Recent mechanistic\
    \ review used as the seed reference for the hypothesis-search deep-research run\
    \ and for the antigen/T-cell/macrophage granuloma-chronicity framing.\n- reference:\
    \ PMID:31273209\n  reference_title: Sarcoidosis.\n  supports: SUPPORT\n  evidence_source:\
    \ HUMAN_CLINICAL\n  snippet: The disease develops in genetically predisposed individuals\
    \ with exposure to an as-yet unknown\n    antigen.\n  explanation: |\n    Nature\
    \ Reviews Disease Primers review supports the central upstream premise of this\
    \ hypothesis: genetically predisposed patients encounter an unknown antigenic\
    \ trigger."
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
citation_count: 44
---

## Question

# Mechanistic Hypothesis Search

You are evaluating a specific disease mechanism hypothesis for the Disorder
Mechanisms Knowledge Base. This is not a general disease overview. Use the
hypothesis YAML below as the seed claim, then search for evidence that supports,
refutes, qualifies, or competes with this hypothesis.

## Target Disease
- **Disease Name:** Sarcoidosis
- **Category:** Immune

## Target Hypothesis
- **Hypothesis ID:** antigen_persistence_granuloma_chronicity_model
- **Hypothesis Label:** Antigen Persistence / Th17.1 / mTORC1 Granuloma Chronicity Model
- **Status in KB:** EMERGING

## Seed Hypothesis YAML

```yaml
hypothesis_group_id: antigen_persistence_granuloma_chronicity_model
hypothesis_label: Antigen Persistence / Th17.1 / mTORC1 Granuloma Chronicity Model
status: EMERGING
description: Sarcoidosis is modeled as a genetically conditioned, antigen-driven granulomatous immune
  response in which poorly degradable or repeatedly encountered antigens are presented by macrophage-lineage
  antigen-presenting cells to CD4+ T cells. The activated T-cell compartment polarizes toward IFN-gamma-producing
  Th17.1/Th1-like effector states while regulatory T-cell restraint is insufficient. This cytokine circuit
  recruits and activates macrophages, promotes epithelioid and multinucleated giant-cell granuloma architecture,
  and intersects with macrophage-intrinsic metabolic programs such as mTORC1 activation. Resolution is
  hypothesized to require antigen clearance or sequestration plus restoration of regulatory and apoptotic
  checkpoints; chronic disease and fibrosis occur when antigen persistence, Th17.1 feedback, macrophage
  survival/proliferation, and tissue-repair programs remain engaged.
evidence:
- reference: PMID:38165044
  reference_title: Immune mechanisms of granuloma formation in sarcoidosis and tuberculosis.
  supports: SUPPORT
  evidence_source: HUMAN_CLINICAL
  snippet: Sarcoidosis is a complex immune-mediated disease characterized by clusters of immune cells
    called granulomas.
  explanation: |
    Recent mechanistic review used as the seed reference for the hypothesis-search deep-research run and for the antigen/T-cell/macrophage granuloma-chronicity framing.
- reference: PMID:31273209
  reference_title: Sarcoidosis.
  supports: SUPPORT
  evidence_source: HUMAN_CLINICAL
  snippet: The disease develops in genetically predisposed individuals with exposure to an as-yet unknown
    antigen.
  explanation: |
    Nature Reviews Disease Primers review supports the central upstream premise of this hypothesis: genetically predisposed patients encounter an unknown antigenic trigger.
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

# Hypothesis Evaluation Report: Antigen Persistence / Th17.1 / mTORC1 Granuloma Chronicity Model in Sarcoidosis

**Hypothesis ID:** `antigen_persistence_granuloma_chronicity_model`  
**Status in KB:** EMERGING  
**Evaluation Date:** 2026-06-03  
**Papers Reviewed:** 101  
**Findings Confirmed:** 12  

---

## Executive Judgment

**Verdict: PARTIALLY SUPPORTED — Retain EMERGING status**

The Antigen Persistence / Th17.1 / mTORC1 Granuloma Chronicity Model proposes that sarcoidosis arises from a genetically conditioned, antigen-driven granulomatous immune response in which poorly degradable antigens are presented to CD4+ T cells, polarizing toward Th17.1/Th1-like effector states with insufficient regulatory T-cell restraint, intersecting with mTORC1-driven macrophage metabolic programs. Resolution requires antigen clearance and restoration of regulatory checkpoints; chronicity and fibrosis result when these fail. After systematic evaluation against 101 primary publications, genome-wide association studies, clinical trials, single-cell transcriptomic data, and proteomic profiling, this report concludes that the hypothesis is **partially supported** with important qualifications.

The three mechanistic pillars of the hypothesis each have strong, independent evidentiary support: (1) GWAS meta-analyses identify IL23R as the largest-effect non-HLA risk locus, directly validating the Th17 axis; (2) Th17.1 cells are confirmed as the predominant IFN-γ source in sarcoidosis lungs with impaired Treg function at disease sites; (3) mTORC1 activation in macrophages is causally sufficient for granuloma formation in mouse models, with clinical sirolimus efficacy in cutaneous sarcoidosis. However, the **integrated causal chain** connecting these pillars remains unproven. The critical Th17.1→mTORC1 link is speculative and these may represent parallel converging pathways rather than a sequential cascade. The Phase II CLEAR antimycobacterial trial failed definitively in pulmonary sarcoidosis (p=0.64), weakening the specific mycobacterial antigen persistence claim. Fibrosis involves distinct EMT pathways rather than simple inflammatory persistence. Anti-TNF drugs paradoxically induce sarcoidosis, complicating the cytokine circuit model. No single pathway-targeted therapy is dramatically effective (meta-analysis I²=76.3%), suggesting disease heterogeneity that exceeds the model's scope. The hypothesis should retain EMERGING status with subtype restriction to non-Löfgren's progressive pulmonary sarcoidosis and refinement to accommodate non-viable antigen remnants, self-antigens, and semi-independent T cell and macrophage arms.

---

## Summary

Sarcoidosis is a systemic granulomatous disease whose etiology has remained unresolved despite decades of investigation. The Antigen Persistence / Th17.1 / mTORC1 Granuloma Chronicity Model represents an integrative attempt to unify three major research streams — antigen-driven T cell activation, Th17.1/Th1 immune polarization with regulatory failure, and macrophage-intrinsic metabolic reprogramming — into a coherent mechanistic narrative. This report evaluates each component against the current literature, identifies knowledge gaps, and assesses competing hypotheses.

The strongest evidence supports the individual pillars: genetic architecture studies involving over 9,700 cases validate IL23R/Th17 and HLA class II pathways as core disease determinants; functional studies demonstrate Th17.1 cells as the dominant IFN-γ producers in the sarcoid lung; and mouse genetic models prove mTORC1 activation is sufficient for granuloma formation with translational validation through sirolimus clinical trials. However, the connections between these pillars — particularly whether Th17.1-derived cytokines directly activate macrophage mTORC1, and whether a specific persistent antigen drives the entire cascade — remain inferential rather than experimentally demonstrated.

Critical challenges to the model include: the failure of antimycobacterial therapy in the definitive Phase II pulmonary trial despite cutaneous sarcoidosis responding; the paradoxical induction of sarcoidosis by anti-TNF agents that should suppress granuloma formation according to the model; proteomic evidence that fibrosis and active granulomatous inflammation operate through distinct molecular programs (EMT vs. mTORC1/MYC); and single-cell transcriptomic data revealing macrophage heterogeneity (five distinct subpopulations) not captured by the original hypothesis. These findings collectively argue for a more nuanced, subtype-aware model with semi-independent converging pathways rather than a single linear cascade.

---

## Key Findings

### Finding 1: mTORC1 Activation Drives Macrophage Granuloma Formation — Established

The mTORC1 pathway represents the most causally validated component of the hypothesis. Linke et al. (2017) demonstrated that mTORC1 activation via Tsc2 deletion in macrophages is sufficient to induce granuloma formation in vivo, establishing a direct causal link ([PMID: 28092373](https://pubmed.ncbi.nlm.nih.gov/28092373/)). This study showed that mTORC1 promotes metabolic reprogramming toward glycolysis via CDK4, inhibits NF-κB signaling and apoptosis, and that in human sarcoidosis patients, mTORC1 activation, macrophage proliferation, and glycolysis correlated with clinical disease progression. Hiranuma et al. (2024) extended this by showing aberrant monocytopoiesis driven by mTORC1 gives rise to granulomas in sarcoidosis model mice, with immature monocytes maturing into granuloma macrophages ([PMID: 38147536](https://pubmed.ncbi.nlm.nih.gov/38147536/)). The translational bridge was established by Redl et al. (2024), who conducted a clinical trial of sirolimus (mTORC1 inhibitor) in cutaneous sarcoidosis showing that systemic treatment resulted in clinical and histological improvement in 70% of participants (median CSAMI change -7.0, p=0.018) with long-lasting effects beyond one year after treatment cessation ([PMID: 38267106](https://pubmed.ncbi.nlm.nih.gov/38267106/)). A recent review confirmed mTORC1 as a druggable therapeutic target, noting that sirolimus restores autophagy and macrophage function ([PMID: 40996589](https://pubmed.ncbi.nlm.nih.gov/40996589/)).

**Evidence strength:** Strong (causal mouse model + human correlation + clinical intervention). This is the most mechanistically validated node in the hypothesis.

### Finding 2: Th17.1 Cells Are the Predominant IFN-γ Source and Associate with Disease Progression — Established

A paradigm shift from classical Th1 to Th17.1 cells as the key effector population in sarcoidosis is now well-supported. Broos et al. (2016) demonstrated that Th17.1 cells, rather than classical Th1 cells, are responsible for the exaggerated IFN-γ production in pulmonary sarcoidosis ([PMID: 27379969](https://pubmed.ncbi.nlm.nih.gov/27379969/)). Miedema et al. (2018) showed that IFN-γ-producing Th17.1 cells appear more pathogenic in non-Löfgren's sarcoidosis and are possibly linked to disease progression, while Löfgren's syndrome shows a broader cytokine profile ([PMID: 29310925](https://pubmed.ncbi.nlm.nih.gov/29310925/)). Sakthivel et al. (2017) found Th17.1 cells recognizing the auto-antigen vimentin on HLA-DR3 accumulate in granulomas in acute sarcoidosis ([PMID: 27755127](https://pubmed.ncbi.nlm.nih.gov/27755127/)). Misra & Agarwal (2022) confirmed that Th17.1 lymphocytes are concentrated in mediastinal lymph nodes and alveolar lining and are the predominant source of IFN-γ in the sarcoid lung ([PMID: 35546376](https://pubmed.ncbi.nlm.nih.gov/35546376/)).

**Evidence strength:** Strong for the Th17.1 identity of effector T cells; moderate for the causal link to disease progression (associative, not interventional). Subtype specificity: strongest in non-Löfgren's disease.

### Finding 3: Impaired Treg Function and Survival Contributes to Unchecked Inflammation — Established

The regulatory failure arm of the hypothesis is supported by multiple independent lines of evidence. Broos et al. (2015) showed that Tregs in sarcoidosis have impaired survival and enhanced apoptotic susceptibility via CD95L, with enhanced CD95 expression specifically on activated Tregs but not Th cells ([PMID: 26376720](https://pubmed.ncbi.nlm.nih.gov/26376720/)). Kumari et al. (2021) found Treg cells functionally defective at the pathological site in pulmonary sarcoidosis, with the OX40 pathway implicated; critically, inhibiting OX40 restored Treg function, suggesting a tractable therapeutic intervention ([PMID: 33901497](https://pubmed.ncbi.nlm.nih.gov/33901497/)). Frye et al. (2020) reported altered Treg functions with reduced CTLA-4 expression and prolonged inflammation, motivating the ABASARC abatacept trial ([PMID: 32551397](https://pubmed.ncbi.nlm.nih.gov/32551397/)). Vagts et al. (2025) integrated recent transcriptomic data confirming that deficient regulatory pathways fail to counterbalance T cell activation, creating a perpetuating inflammatory loop underlying disease persistence and fibrotic progression ([PMID: 41197661](https://pubmed.ncbi.nlm.nih.gov/41197661/)).

**Evidence strength:** Strong for Treg dysfunction; moderate for its causal role in chronicity (no longitudinal perturbation data in humans yet).

### Finding 4: Antigen-Driven CD4+ T Cell Oligoclonal Expansion Supports Antigen Persistence — Emerging

The antigen-driven nature of the T cell response is supported by TCR repertoire studies. Forman et al. (1994) demonstrated selective activation and accumulation of oligoclonal Vβ-specific T cells in active pulmonary sarcoidosis, with biased expression of multiple Vβ families and sequence analysis showing clonal expansion with similar V(D)J junctional region motifs ([PMID: 7929830](https://pubmed.ncbi.nlm.nih.gov/7929830/)). Silver et al. (1996) showed clonality of 11–46% in lung Vβ8+ T cells with common VDJ junctional amino acid residues consistent with antigen-specific response ([PMID: 8881751](https://pubmed.ncbi.nlm.nih.gov/8881751/)). Oswald-Richter et al. (2012) found CD4+ T cell immune responses to mycobacterial ESAT-6 in 17/27 sarcoidosis subjects vs. 2/14 PPD-negative controls (p=0.008), with MALDI-IMS localizing ESAT-6-consistent signals within granulomatous inflammation ([PMID: 22552860](https://pubmed.ncbi.nlm.nih.gov/22552860/)). However, the identity of the driving antigen(s) remains uncertain, and the CLEAR trial failure challenges the viable mycobacterial infection hypothesis.

**Evidence strength:** Strong for antigen-driven T cell expansion; weak for specific antigen identity.

### Finding 5: GWAS Confirms IL23R/Th17 and HLA Class II Pathways as Core Genetic Architecture — Established

Genome-wide association studies provide the strongest population-level validation of the hypothesis. Yuan et al. (2025) identified 28 genomic loci associated with sarcoidosis in a GWAS of 9,755 cases, with the C1orf141-IL23R locus showing the largest effect size, and enrichment analysis establishing key roles for T cell activation, leukocyte adhesion, and cytokine production ([PMID: 40075078](https://pubmed.ncbi.nlm.nih.gov/40075078/)). Fischer et al. (2015) identified IL12B, NFKB1, SH2B3, HLA-B, HLA-DPB1, BTNL2, and IL23R as risk loci with genome-wide significance in an Immunochip study of >19,000 individuals, with protein network analyses suggesting a prominent role of the drug-targetable IL23/Th17 signaling pathway ([PMID: 26051272](https://pubmed.ncbi.nlm.nih.gov/26051272/)). Ricci et al. (2025) conducted a multi-ancestry meta-analysis (9,659 cases) identifying 19 European and 2 African risk loci with heritability of 0.25 (European) and 0.19 (African) ([PMID: 41466414](https://pubmed.ncbi.nlm.nih.gov/41466414/)). Liao et al. (2023) confirmed multiple independent HLA association signals including HLA-DRA, DRB1*0101, and DQA1*0101 ([PMID: 37399103](https://pubmed.ncbi.nlm.nih.gov/37399103/)).

**Evidence strength:** Very strong. GWAS independently validates the Th17/IL-23 and antigen-presentation (HLA class II) axes of the hypothesis at the population genetic level.

### Finding 6: Proteomic Evidence Distinguishes mTORC1-Driven Inflammation from EMT-Driven Fibrosis — Qualifies

Shastry et al. (2025) performed SomaScan 11K plasma proteomics on CT-defined sarcoidosis phenotypes, finding that progressive fibrosis was associated with epithelial-mesenchymal transition pathways, while progressive nodular disease was linked to mTORC1 and MYC signaling and metabolic activation ([PMID: 40667074](https://pubmed.ncbi.nlm.nih.gov/40667074/)). This demonstrates that fibrosis and active granulomatous inflammation have distinct molecular signatures, qualifying the hypothesis's assumption that fibrosis is simply a downstream consequence of persistent inflammation.

### Finding 7: Phase II CLEAR Antimycobacterial Trial Failed in Pulmonary Sarcoidosis — Weakens Specific Mycobacterial Claim

Drake et al. (2021) conducted the definitive double-blind, placebo-controlled, multicenter Phase II trial of antimycobacterial therapy (CLEAR regimen: levofloxacin, ethambutol, azithromycin, rifabutin) for 16 weeks in pulmonary sarcoidosis. The ITT analysis revealed no significant difference in FVC (CLEAR -1.1% vs. placebo +0.02%, p=0.64), no benefit in 6MWD (p=0.91), and quality of life actually favored placebo (p=0.028) ([PMID: 33387486](https://pubmed.ncbi.nlm.nih.gov/33387486/)). This contrasts with the earlier open-label Phase I study showing FVC improvement of 0.42L at 8 weeks (p=0.016) ([PMID: 24284293](https://pubmed.ncbi.nlm.nih.gov/24284293/)) and a randomized trial showing benefit in cutaneous sarcoidosis (lesion diameter reduction, p=0.05; granuloma burden reduction, p=0.02) ([PMID: 23863960](https://pubmed.ncbi.nlm.nih.gov/23863960/)).

**Interpretation:** The trial failure does not rule out antigen persistence in general but significantly weakens the specific claim that viable mycobacterial infection drives chronic pulmonary sarcoidosis. The cutaneous response suggests organ-specific differences. The antigen persistence model may need refinement toward non-viable antigen remnants (e.g., serum amyloid A aggregates, mycobacterial catalase-peroxidase fragments) or self-antigens (e.g., vimentin).

### Finding 8: Anti-TNF Drugs Paradoxically Induce Sarcoidosis — Complicates Cytokine Circuit Model

Bez et al. (2026) reported 26 cases of anti-TNF drug-induced sarcoidosis reaction in IBD patients (infliximab 57.7%, adalimumab 42.3%), with median onset 21 months and extrathoracic involvement more prevalent than conventional sarcoidosis (76.7%) ([PMID: 42170754](https://pubmed.ncbi.nlm.nih.gov/42170754/)). Wendling & Prati (2014) proposed the mechanism involves an imbalance of cytokines toward interferons, chemokines, and probably IL-17 when TNF is blocked ([PMID: 24325385](https://pubmed.ncbi.nlm.nih.gov/24325385/)).

**Interpretation:** This paradox is partially reconcilable with the hypothesis: TNF blockade may shift the cytokine balance toward IFN-γ and IL-17, effectively amplifying the Th17.1 arm. However, it demonstrates that the cytokine network is more complex than a simple linear cascade and that TNF plays a dual role — both promoting and restraining granulomatous inflammation.

### Finding 9: Checkpoint Inhibitor-Induced Sarcoidosis Supports Immune Dysregulation Model

Multiple case reports/series document that PD-1/PD-L1/CTLA-4 immune checkpoint inhibitors trigger sarcoid-like granulomatous reactions ([PMID: 40103819](https://pubmed.ncbi.nlm.nih.gov/40103819/); [PMID: 30326785](https://pubmed.ncbi.nlm.nih.gov/30326785/); [PMID: 31279873](https://pubmed.ncbi.nlm.nih.gov/31279873/); [PMID: 30220489](https://pubmed.ncbi.nlm.nih.gov/30220489/)). Kubo et al. (2021) demonstrated strong PD-L1 expression in epithelioid granulomatous lesions, suggesting PD-L1 plays a homeostatic role restraining granulomatous inflammation ([PMID: 33570446](https://pubmed.ncbi.nlm.nih.gov/33570446/)). This provides a human "experiment of nature" confirming that immune checkpoint disruption — the pharmacological equivalent of Treg/regulatory failure — can trigger granuloma formation, strongly supporting the regulatory failure component of the hypothesis.

### Finding 10: scRNA-seq Reveals Macrophage Heterogeneity Beyond the Hypothesis

Moore et al. (2025) performed scRNA-seq on BAL from 16 sarcoidosis patients and 14 controls, identifying five macrophage populations: resident, high metallothionein resident, recruited, profibrotic recruited, and proliferating macrophages ([PMID: 39896662](https://pubmed.ncbi.nlm.nih.gov/39896662/)). Each subpopulation had unique gene expression profiles with differential expression linked to sarcoidosis. Changes in gene expression associated with disease progression were observed in resident and recruited macrophages. This heterogeneity is not captured by the original hypothesis, which treats macrophages as a monolithic population.

### Finding 11: Therapeutic Landscape Shows Modest, Heterogeneous Responses

Bechman et al. (2025) conducted a meta-analysis of 16 studies (8 RCTs) of biologic and targeted synthetic therapies, finding a mean FVC change of 4.79% (95% CI 1.22–8.35) driven by anti-TNF trials (5.70%, 95% CI 1.61–9.78), with substantial heterogeneity (I²=76.3%) ([PMID: 40393718](https://pubmed.ncbi.nlm.nih.gov/40393718/)). Efzofitimod, a novel neuropilin-2 targeting immunomodulator, showed dose-dependent steroid-sparing and quality-of-life improvements in Phase II ([PMID: 36356657](https://pubmed.ncbi.nlm.nih.gov/36356657/)). This neuropilin-2 target is not captured by the hypothesis, highlighting additional mechanisms. No single pathway-targeted therapy is dramatically effective, consistent with a complex multi-pathway disease rather than a single linear cascade.

### Finding 12: Serum Biomarkers Confirm Ongoing T Cell and Macrophage Activation

sIL-2R and neopterin are significantly elevated in chronic sarcoidosis vs. controls, with the panel of YKL-40, sIL-2R, ACE, and hs-CRP best discriminating active from inactive disease ([PMID: 30154391](https://pubmed.ncbi.nlm.nih.gov/30154391/)). Prasse et al. (2008) found sIL-2R and neopterin particularly increased in patients requiring long-term treatment ([PMID: 17975200](https://pubmed.ncbi.nlm.nih.gov/17975200/)). Combined serological markers had 80% sensitivity and 100% specificity for PET-positive inflammatory activity ([PMID: 21899998](https://pubmed.ncbi.nlm.nih.gov/21899998/)). These biomarkers confirm persistent immune activation consistent with the hypothesis but are not specific to its proposed mechanism.

---

## Mechanistic Causal Chain

The hypothesis implies a sequential causal chain from upstream trigger to clinical manifestation. Below, each node is assessed for evidence strength:

{{figure:mechanistic_diagram.png|caption=Mechanistic causal chain diagram with evidence strength assessment for each node, from upstream genetic susceptibility through antigen encounter, T cell activation, macrophage metabolic reprogramming, and granuloma formation to clinical outcomes}}

### Causal Chain Nodes (Upstream → Downstream)

| Step | Mechanistic Node | Evidence Strength | Key Evidence |
|------|-----------------|-------------------|--------------|
| 1 | HLA class II / IL23R genetic susceptibility | **STRONG** | GWAS: 28 loci, IL23R largest effect; heritability 0.25 (EUR) |
| 2 | Antigen encounter (microbial/environmental/self) | **MODERATE** | Oligoclonal TCR expansion; ESAT-6 responses (p=0.008) |
| 3 | Antigen persistence / poor degradation | **WEAK** | CLEAR trial FAILED (p=0.64); cutaneous responded; viable infection unproven |
| 4 | Macrophage antigen presentation to CD4+ T cells | **STRONG** | HLA-DRB1 associations; beryllium disease analogy |
| 5 | Th17.1/Th1 polarization | **STRONG** | Th17.1 = predominant IFN-γ source in BAL |
| 6 | Treg impairment / checkpoint failure | **STRONG** | CD95-mediated Treg apoptosis; OX40 pathway; checkpoint inhibitor induction |
| 7 | Th17.1 → macrophage mTORC1 activation | **SPECULATIVE** | No direct experimental evidence for this specific link |
| 8 | mTORC1-driven macrophage proliferation & metabolic shift | **STRONG** | Tsc2 KO mice → granulomas; aberrant monocytopoiesis |
| 9 | Granuloma formation & maintenance | **STRONG** | Histological hallmark; multiple models |
| 10 | Resolution vs. chronicity | **MODERATE** | Biomarker correlation; subtype associations |
| 11 | Fibrosis | **WEAK (as linear extension)** | EMT pathways distinct from mTORC1; separate molecular program |

**Critical missing link:** Step 7 — the hypothesized Th17.1→mTORC1 connection — has no direct experimental evidence. IFN-γ can activate mTOR signaling in macrophages, but whether Th17.1-derived IFN-γ specifically drives the mTORC1 program in sarcoidosis granuloma macrophages has not been demonstrated. These may be semi-independent converging pathways, each individually contributing to granuloma formation rather than operating as a sequential cascade.

---

## Evidence Matrix

{{figure:claim_status_table.png|caption=Claim-by-claim status assessment of the hypothesis components: established (green), emerging (yellow), speculative (orange), weakened (red), and contradicted claims with supporting evidence and confidence levels}}

| Citation | Evidence Type | Direction | Mechanistic Claim | Key Finding | Context | Confidence |
|----------|--------------|-----------|-------------------|-------------|---------|------------|
| [PMID: 28092373](https://pubmed.ncbi.nlm.nih.gov/28092373/) | Mouse model + human | SUPPORTS | mTORC1 → granuloma | Tsc2 deletion sufficient for granulomas | Pulmonary/systemic | High |
| [PMID: 38147536](https://pubmed.ncbi.nlm.nih.gov/38147536/) | Mouse model | SUPPORTS | mTORC1 → monocytopoiesis | Aberrant mTORC1-driven monocytopoiesis | Model mice | High |
| [PMID: 38267106](https://pubmed.ncbi.nlm.nih.gov/38267106/) | RCT | SUPPORTS | mTORC1 inhibition therapeutic | Sirolimus: 70% response, p=0.018 | Cutaneous sarcoidosis | High |
| [PMID: 27379969](https://pubmed.ncbi.nlm.nih.gov/27379969/) | Human clinical | SUPPORTS | Th17.1 = IFN-γ source | Th17.1 not Th1 produce IFN-γ | Pulmonary | High |
| [PMID: 29310925](https://pubmed.ncbi.nlm.nih.gov/29310925/) | Human clinical | SUPPORTS | Th17.1 → progression | Th17.1 pathogenic in non-LS | Non-Löfgren's | Moderate |
| [PMID: 26376720](https://pubmed.ncbi.nlm.nih.gov/26376720/) | Human clinical | SUPPORTS | Treg impairment | Enhanced CD95, impaired Treg survival | Systemic | High |
| [PMID: 33901497](https://pubmed.ncbi.nlm.nih.gov/33901497/) | Human clinical | SUPPORTS | Treg functional defect | OX40-mediated Treg suppression | Pulmonary sites | High |
| [PMID: 40075078](https://pubmed.ncbi.nlm.nih.gov/40075078/) | GWAS (9,755 cases) | SUPPORTS | IL23R/Th17 genetic basis | IL23R largest effect; 28 loci | Population-level | Very high |
| [PMID: 26051272](https://pubmed.ncbi.nlm.nih.gov/26051272/) | GWAS (>19,000) | SUPPORTS | IL23/Th17 pathway | Drug-targetable IL23/Th17 pathway | Population-level | Very high |
| [PMID: 41466414](https://pubmed.ncbi.nlm.nih.gov/41466414/) | Meta-GWAS (9,659) | SUPPORTS | Genetic architecture | h²=0.25 (EUR), 0.19 (AFR); IFN-γ enriched | Multi-ancestry | Very high |
| [PMID: 7929830](https://pubmed.ncbi.nlm.nih.gov/7929830/) | Human clinical | SUPPORTS | Antigen-driven TCR | Oligoclonal Vβ expansion with shared motifs | Active pulmonary | Moderate |
| [PMID: 22552860](https://pubmed.ncbi.nlm.nih.gov/22552860/) | Human clinical | SUPPORTS | Mycobacterial antigen | ESAT-6 responses: 17/27 vs 2/14 (p=0.008) | Pulmonary | Moderate |
| [PMID: 33387486](https://pubmed.ncbi.nlm.nih.gov/33387486/) | Phase II RCT | WEAKENS | Mycobacterial infection → disease | CLEAR: FVC p=0.64, no benefit | Chronic pulmonary | High |
| [PMID: 23863960](https://pubmed.ncbi.nlm.nih.gov/23863960/) | RCT | QUALIFIES | Antimycobacterial efficacy | Cutaneous response (p=0.05) but not pulmonary | Cutaneous | Moderate |
| [PMID: 42170754](https://pubmed.ncbi.nlm.nih.gov/42170754/) | Case series (26) | COMPLICATES | TNF in granuloma circuit | Anti-TNF induces sarcoidosis; 21mo onset | IBD patients | Moderate |
| [PMID: 24325385](https://pubmed.ncbi.nlm.nih.gov/24325385/) | Review | QUALIFIES | Cytokine rebalancing | TNF blockade → IFN/IL-17 shift | Multiple diseases | Low-moderate |
| [PMID: 40667074](https://pubmed.ncbi.nlm.nih.gov/40667074/) | Proteomics | QUALIFIES | Fibrosis as linear extension | EMT (fibrosis) vs mTORC1/MYC (nodular) | CT phenotypes | Moderate |
| [PMID: 39896662](https://pubmed.ncbi.nlm.nih.gov/39896662/) | scRNA-seq | QUALIFIES | Macrophage monolithic model | 5 distinct macrophage subpopulations | BAL | High |
| [PMID: 33570446](https://pubmed.ncbi.nlm.nih.gov/33570446/) | Human pathology | SUPPORTS | PD-L1/regulatory role | PD-L1 on granulomas = homeostatic restraint | Multiple granulomatous | Moderate |
| [PMID: 40393718](https://pubmed.ncbi.nlm.nih.gov/40393718/) | Meta-analysis (16 studies) | QUALIFIES | Single-pathway targeting | FVC 4.79%, I²=76.3%; heterogeneous | Multiple therapies | High |
| [PMID: 41197661](https://pubmed.ncbi.nlm.nih.gov/41197661/) | Integrative review | SUPPORTS | Regulatory failure loop | Deficient regulatory pathways → perpetuating loop | Comprehensive | Moderate |
| [PMID: 36356657](https://pubmed.ncbi.nlm.nih.gov/36356657/) | Phase II trial | COMPETING | Neuropilin-2 mechanism | Efzofitimod steroid-sparing via NRP2 | Pulmonary | Moderate |

---

## Knowledge Gaps

{{figure:knowledge_gaps_table.png|caption=Priority assessment of knowledge gaps in the hypothesis, ranked by impact and tractability, from the Th17.1→mTORC1 causal link to organ-specific antigen identity}}

### Gap 1: Th17.1 → mTORC1 Causal Link (HIGH PRIORITY)

**Scope:** The hypothesis places Th17.1-derived IFN-γ upstream of macrophage mTORC1 activation, but no study has directly tested whether Th17.1 cell products activate mTORC1 in sarcoidosis macrophages.

**Why it matters:** This is the central integrative claim of the hypothesis. If the T cell and macrophage arms operate independently, the model needs fundamental revision from a linear cascade to a convergent network.

**What was checked:** Literature search for "Th17.1 mTORC1 sarcoidosis," "IFN-gamma mTOR macrophage granuloma." While IFN-γ can activate mTOR signaling in TB macrophages ([PMID: 25194337](https://pubmed.ncbi.nlm.nih.gov/25194337/)), this has not been demonstrated specifically for Th17.1-derived IFN-γ in the sarcoidosis context.

**Resolution:** Co-culture experiments with sarcoidosis BAL Th17.1 cells and autologous macrophages, measuring mTORC1 phosphorylation (p-S6K, p-4E-BP1) with and without IFN-γ neutralization.

### Gap 2: Identity of the Persistent Antigen (HIGH PRIORITY)

**Scope:** Despite extensive investigation, the specific antigen(s) driving chronic sarcoidosis remain unidentified. Mycobacterial antigens (ESAT-6, KatG) are the strongest candidates but the CLEAR trial failure challenges the viable infection model.

**Why it matters:** The entire upstream arm of the hypothesis depends on antigen persistence. Without identifying the antigen, the model cannot be fully validated or used for therapeutic targeting.

**What was checked:** ESAT-6 immunoreactivity (positive in 63% of cases, [PMID: 22552860](https://pubmed.ncbi.nlm.nih.gov/22552860/)); Propionibacterium acnes studies; vimentin auto-antigen; serum amyloid A aggregates. No single antigen accounts for all cases.

**Resolution:** Unbiased antigen discovery using TCR-peptide-MHC deconvolution from sarcoidosis BAL T cells; antigen arrays across disease subtypes; longitudinal antigen-specific T cell tracking.

### Gap 3: Organ-Specific Pathway Differences (MODERATE PRIORITY)

**Scope:** Antimycobacterial therapy succeeded in cutaneous but failed in pulmonary sarcoidosis. Proteomic phenotyping shows distinct pathways for fibrotic vs. nodular disease. The hypothesis does not account for organ-specific mechanisms.

**Why it matters:** A single-mechanism model cannot guide organ-specific treatment decisions.

**What was checked:** CLEAR trial pulmonary vs. cutaneous results; CT phenotype proteomics; cardiac sarcoidosis mTORC1 model.

**Resolution:** Multi-organ tissue sampling (BAL, skin biopsy, lymph node) with matched single-cell transcriptomics and spatial proteomics in the same patients.

### Gap 4: Fibrosis Mechanism Disconnect (MODERATE PRIORITY)

**Scope:** The hypothesis assumes fibrosis results from persistent inflammation, but proteomic data show fibrosis involves distinct EMT pathways rather than mTORC1/MYC signaling ([PMID: 40667074](https://pubmed.ncbi.nlm.nih.gov/40667074/)).

**Why it matters:** If fibrosis is a parallel or divergent process, anti-inflammatory approaches alone may not prevent fibrotic progression.

**What was checked:** Proteomic phenotyping; IPF literature; sarcoidosis fibrosis reviews.

**Resolution:** Longitudinal cohort with serial imaging, proteomics, and BAL sampling to determine whether fibrosis develops from persistent inflammation or through independent pathways.

### Gap 5: No GenCC/ClinGen or Large-Scale Multi-Omic Integration

**Scope:** No GenCC or ClinGen entries exist for sarcoidosis gene-disease relationships. Large-scale multi-omic (genomics + transcriptomics + proteomics + metabolomics) integration studies are absent.

**What was checked:** GenCC database, ClinGen, GWASCatalog integration studies.

**Resolution:** Systematic multi-omic cohort with matched genomics, single-cell RNA-seq, proteomics, and metabolomics in phenotyped patients.

### Gap 6: Löfgren's vs. Non-Löfgren's Mechanistic Divergence

**Scope:** The hypothesis appears most applicable to non-Löfgren's progressive disease. Löfgren's syndrome has distinct genetic associations (HLA-DRB1*0301), broader cytokine profiles, higher ICOS+ Tregs, and generally resolves spontaneously. Whether the hypothesis applies at all to Löfgren's is unclear.

**What was checked:** Miedema et al. (2018) showing Th17.1 specificity for non-LS; ICOS expression studies; genetic architecture differences.

**Resolution:** Parallel characterization of Th17.1 frequency, mTORC1 activation, Treg function, and TCR repertoire in Löfgren's vs. non-Löfgren's patients at matched timepoints.

---

## Alternative Models

### 1. Serum Amyloid A (SAA) Aggregate Model
**Relationship to seed hypothesis:** Complementary/alternative upstream trigger

Chen & Moller (2015) proposed that sarcoidosis is triggered by a hyperimmune Th1 response to pathogenic microbial and tissue antigens associated with aberrant aggregation of serum amyloid A within granulomas, which promotes progressive chronic granulomatous inflammation in the absence of ongoing infection ([PMID: 25771769](https://pubmed.ncbi.nlm.nih.gov/25771769/)). This model addresses the CLEAR trial failure by providing a mechanism for persistent granulomatous inflammation without viable organisms — SAA aggregates serve as the persistent "antigen" rather than live microbes.

### 2. Endogenous Hypersensitivity / Latent Microbial Reactivation Model
**Relationship:** Alternative upstream mechanism

Recent work proposes sarcoidosis as an "endogenous hypersensitivity infection" where latent microbial antigens (P. acnes, mycobacteria) are reactivated under specific conditions ([PMID: 41597666](https://pubmed.ncbi.nlm.nih.gov/41597666/); [PMID: 40837573](https://pubmed.ncbi.nlm.nih.gov/40837573/)). This differs from the seed hypothesis in emphasizing reactivation dynamics rather than continuous antigen persistence.

### 3. Macrophage-Autonomous Metabolic Model
**Relationship:** Parallel mechanism (independent of T cell arm)

The mTORC1 mouse model ([PMID: 28092373](https://pubmed.ncbi.nlm.nih.gov/28092373/)) demonstrates granuloma formation from macrophage-intrinsic metabolic reprogramming without requiring T cell input. This suggests that the macrophage arm may be partially autonomous — metabolic checkpoint activation in macrophages could drive granuloma formation independently of the Th17.1 circuit, especially in some disease subtypes.

### 4. Immune Checkpoint / PD-L1 Homeostasis Model
**Relationship:** Complementary regulatory mechanism

Checkpoint inhibitor-induced sarcoidosis demonstrates that disruption of PD-1/PD-L1 signaling alone can trigger granuloma formation ([PMID: 33570446](https://pubmed.ncbi.nlm.nih.gov/33570446/)). This places the regulatory checkpoint failure upstream of granuloma formation and suggests that PD-L1 on granuloma cells serves a homeostatic restraining function. This model complements the Treg failure arm of the hypothesis but suggests additional regulatory axes beyond CTLA-4 and FoxP3+ Tregs.

### 5. Multi-Antigen / Multi-Pathway Convergence Model
**Relationship:** Refinement of seed hypothesis

Given the evidence that (a) different antigens may drive disease in different populations (mycobacteria in US/Europe, P. acnes in Japan), (b) the T cell and macrophage arms may be semi-independent, and (c) fibrosis operates through distinct EMT pathways, the most parsimonious model may be a convergence framework where multiple upstream triggers and parallel effector pathways converge on granuloma formation. This preserves the core insights of the seed hypothesis while accommodating the observed heterogeneity.

### 6. DAMPs / Heat Shock Protein Model
**Relationship:** Alternative upstream trigger

Dubaniewicz (2013) proposed that human and microbial heat shock proteins (HSPs) as damage-associated molecular patterns (DAMPs) or pathogen-associated molecular patterns (PAMPs) may induce sarcoid granuloma through both infectious and non-infectious factors ([PMID: 23993988](https://pubmed.ncbi.nlm.nih.gov/23993988/)). This model broadens the antigen concept beyond specific microbial peptides to include endogenous danger signals.

---

## Discriminating Tests

### Test 1: Th17.1→mTORC1 Causal Link
- **Design:** Ex vivo co-culture of paired BAL Th17.1 cells and alveolar macrophages from sarcoidosis patients
- **Perturbation:** Anti-IFN-γ, anti-IL-17, IL-23R blockade
- **Readout:** Macrophage phospho-S6K, phospho-4E-BP1, glycolytic flux (Seahorse assay)
- **Expected if hypothesis correct:** IFN-γ neutralization abolishes mTORC1 activation in macrophages
- **Expected if parallel pathways:** mTORC1 activation persists despite Th17.1 cytokine blockade

### Test 2: Antigen Identity via Unbiased TCR Deconvolution
- **Design:** Single-cell TCR-seq from BAL + matched peptide-MHC tetramer screening
- **Stratification:** Löfgren's vs. non-Löfgren's, progressive vs. resolving
- **Sample:** 50+ patients across phenotypes
- **Expected:** Convergent antigen specificity in non-Löfgren's; divergent in Löfgren's

### Test 3: mTORC1 Inhibitor vs. Anti-IL-23 Head-to-Head
- **Design:** Randomized, multi-center trial comparing sirolimus vs. anti-IL-23 (e.g., guselkumab) vs. combination in chronic pulmonary sarcoidosis
- **Biomarkers:** sIL-2R, neopterin, BAL cell counts, Th17.1 frequency, macrophage p-S6K
- **Expected if sequential cascade:** Combination superior; anti-IL-23 reduces both T cell and macrophage arms
- **Expected if parallel pathways:** Each drug helps different biomarkers; combination only additive

### Test 4: Longitudinal Multi-Omic Phenotyping
- **Design:** Prospective cohort (n≥200) with serial sampling at diagnosis, 6mo, 12mo, 24mo
- **Omics:** Whole-genome sequencing, scRNA-seq (BAL + blood), plasma proteomics (SomaScan), metabolomics
- **Stratification:** By IL23R genotype, HLA-DRB1 status, clinical trajectory
- **Goal:** Determine whether genetic risk maps to specific pathway activation patterns and which patients follow the Th17.1→mTORC1 cascade vs. alternative trajectories

### Test 5: Organ-Specific Antigen Challenge
- **Design:** Compare antigen-specific T cell responses across organ compartments (BAL, skin biopsy, aqueous humor) in patients with multi-organ sarcoidosis
- **Antigens:** ESAT-6, KatG, vimentin, P. acnes lysate, SAA peptides
- **Goal:** Determine whether the same antigen drives disease in different organs or organ-specific antigens exist

---

## Curation Leads (Requiring Curator Verification)

### Candidate Evidence References

1. **[PMID: 42143504](https://pubmed.ncbi.nlm.nih.gov/42143504/)** — CXCR6 targeting suppresses granuloma formation through inhibiting Th17 responses. Abstract mentions CXCR6 on CD4+ T cells in sarcoidosis lungs. *Curator action:* Verify abstract snippet; if confirmed, add as SUPPORT for Th17 effector axis.

2. **[PMID: 37750561](https://pubmed.ncbi.nlm.nih.gov/37750561/)** — mTORC1-dependent mouse model for cardiac sarcoidosis. Extends the Linke et al. pulmonary model to cardiac involvement. *Curator action:* Verify cardiac phenotype details; if confirmed, add as SUPPORT for mTORC1 sufficiency across organs.

3. **[PMID: 41597666](https://pubmed.ncbi.nlm.nih.gov/41597666/)** — "Endogenous hypersensitivity infection" model. May provide refined antigen persistence framing. *Curator action:* Full text review needed to assess whether this is a competing or complementary model.

4. **[PMID: 40086403](https://pubmed.ncbi.nlm.nih.gov/40086403/)** — Comparative review of HP and sarcoidosis immunology highlighting PD-1, TIGIT, and m6A/m5C modifications. *Curator action:* Evaluate whether epigenetic regulators should be added as a knowledge gap for the hypothesis.

### Candidate Pathophysiology Edges

| Source Node | Target Node | Edge Type | Status | Evidence |
|------------|-------------|-----------|--------|----------|
| IL23R genetic risk | Th17.1 polarization | Causal (genetic) | **ESTABLISHED** | GWAS: largest non-HLA effect |
| HLA-DRB1 | Antigen presentation to CD4+ | Causal (genetic) | **ESTABLISHED** | GWAS + functional studies |
| Th17.1 IFN-γ | Macrophage mTORC1 activation | Causal (hypothesized) | **SPECULATIVE** | No direct evidence |
| mTORC1 activation | Macrophage proliferation | Causal | **ESTABLISHED** | Tsc2 KO mice |
| mTORC1 activation | Glycolytic metabolic shift | Causal | **ESTABLISHED** | Linke et al. CDK4 pathway |
| Treg CD95 apoptosis | Unchecked Th17.1 expansion | Causal (hypothesized) | **EMERGING** | Broos et al. + correlative |
| OX40 overexpression | Treg functional defect | Causal | **EMERGING** | Kumari et al. restoration |
| TNF blockade | IFN-γ/IL-17 shift | Causal (paradoxical) | **EMERGING** | Anti-TNF DISR cases |
| Persistent inflammation | Fibrosis | Sequential | **WEAKENED** | EMT vs. mTORC1 distinct programs |

### Candidate Ontology Terms

- **Cell types:** Th17.1 cell (CCR6+CXCR3+CD4+ T cell; no specific CL term exists); proliferating alveolar macrophage; profibrotic recruited macrophage; high-metallothionein resident macrophage
- **Biological processes:** GO:0032729 (positive regulation of IFN-γ production); GO:0031929 (TOR signaling); GO:0002467 (germinal center formation — approximate for granuloma)
- **Disease subtypes:** Löfgren's syndrome; non-Löfgren's chronic pulmonary sarcoidosis; cutaneous sarcoidosis; cardiac sarcoidosis; drug-induced sarcoidosis reaction (DISR)

### Candidate Status Changes

- **Hypothesis status:** Retain **EMERGING** — strong pillars but unproven integrated chain
- **Subtype restriction:** Add qualifier: "Best supported for non-Löfgren's progressive pulmonary sarcoidosis"
- **Antigen persistence claim:** Downgrade from implied "viable infection" to "non-viable antigen remnants or self-antigens"
- **Fibrosis as extension:** Flag as **WEAKENED** — fibrosis likely involves parallel EMT pathways

### Candidate Knowledge Gap Entries for KB

1. **Th17.1→mTORC1 link unconfirmed** — No direct perturbation evidence; critical for hypothesis integrity
2. **Antigen identity unknown** — Multiple candidates, none definitive across subtypes
3. **Organ-specific mechanisms undefined** — Cutaneous vs. pulmonary divergence in antimycobacterial response
4. **No large-scale multi-omic integration** — scRNA-seq and proteomics exist separately, not integrated
5. **Fibrosis mechanism independent** — EMT program distinct from inflammatory persistence
6. **No GenCC/ClinGen entries** — Sarcoidosis gene-disease relationships not curated in these databases

---

## Limitations of This Report

1. **Search scope:** Literature search was conducted via PubMed with specific query terms. Important findings in non-English literature, preprints, or databases not indexed in PubMed may have been missed.

2. **Publication bias:** Positive findings (e.g., Th17.1 in BAL) are more likely to be published than negative results. The true rate of null findings for specific pathway components may be underestimated.

3. **Subtype heterogeneity:** Sarcoidosis is increasingly recognized as a syndrome rather than a single disease. Findings from one subtype (e.g., Löfgren's) may not apply to others (e.g., chronic fibrotic).

4. **Animal model limitations:** The mTORC1 mouse model (Tsc2 KO) is highly artificial — constitutive genetic activation of mTORC1 does not recapitulate the upstream events of human sarcoidosis. The model proves sufficiency, not necessity.

5. **Trial evidence gap:** The only definitive RCT testing a specific mechanistic prediction (CLEAR antimycobacterial) was negative. Sirolimus and anti-IL-23 trials are small or still in progress.

6. **Temporal limitation:** This analysis reflects literature available through early June 2026. Several ongoing trials (abatacept/ABASARC, larger sirolimus studies) may substantially update the evidence base.

---

## Proposed Follow-Up Experiments and Actions

### Immediate (6–12 months)
- Conduct Th17.1/macrophage co-culture experiments to test the Th17.1→mTORC1 link
- Analyze existing scRNA-seq datasets for mTORC1 pathway activation signatures in macrophage subpopulations
- Perform TCR-seq on paired BAL samples from resolving vs. chronic patients

### Medium-term (1–3 years)
- Launch multi-center, randomized trial of sirolimus vs. anti-IL-23 in chronic pulmonary sarcoidosis
- Establish prospective multi-omic cohort with longitudinal sampling
- Develop organ-on-chip models for sarcoidosis with Th17.1 + macrophage compartments

### Long-term (3–5 years)
- Integrate genomic, transcriptomic, proteomic, and metabolomic data for patient subtyping
- Develop predictive biomarker panels for treatment selection based on pathway activation
- Test combination therapies targeting both T cell (anti-IL-23) and macrophage (sirolimus) arms

---

*Report generated from systematic evaluation of 101 publications across 5 investigation iterations. All PMIDs verified against PubMed. Citation snippets extracted from verified abstracts.*
