---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-06-04T08:10:13.105148'
end_time: '2026-06-04T08:55:22.739355'
duration_seconds: 2709.63
template_file: templates/hypothesis_deep_research.md
template_variables:
  disease_name: IgG4-Related Disease
  category: Autoimmune
  hypothesis_group_id: plasmablast_autoantigen_fibrosis_driver_model
  hypothesis_label: Plasmablast-Autoantigen Fibrosis Driver Model
  hypothesis_status: CANONICAL
  hypothesis_yaml: "hypothesis_group_id: plasmablast_autoantigen_fibrosis_driver_model\n\
    hypothesis_label: Plasmablast-Autoantigen Fibrosis Driver Model\nstatus: CANONICAL\n\
    description: A still-incomplete adaptive immune model in which unresolved autoantigen\
    \ or innate triggers\n  expand B-cell/plasmablast and T-cell axes; Tfh cells promote\
    \ IgG4 class switching, plasmablasts mark\n  and sustain the B-lineage response,\
    \ and CD4-positive cytotoxic T cells provide fibrogenic cytokines\n  that drive\
    \ storiform fibrosis and organ injury."
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
citation_count: 33
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
- **Hypothesis ID:** plasmablast_autoantigen_fibrosis_driver_model
- **Hypothesis Label:** Plasmablast-Autoantigen Fibrosis Driver Model
- **Status in KB:** CANONICAL

## Seed Hypothesis YAML

```yaml
hypothesis_group_id: plasmablast_autoantigen_fibrosis_driver_model
hypothesis_label: Plasmablast-Autoantigen Fibrosis Driver Model
status: CANONICAL
description: A still-incomplete adaptive immune model in which unresolved autoantigen or innate triggers
  expand B-cell/plasmablast and T-cell axes; Tfh cells promote IgG4 class switching, plasmablasts mark
  and sustain the B-lineage response, and CD4-positive cytotoxic T cells provide fibrogenic cytokines
  that drive storiform fibrosis and organ injury.
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

# Hypothesis Evaluation Report: Plasmablast-Autoantigen Fibrosis Driver Model in IgG4-Related Disease

## Executive Judgment

**Verdict: PARTIALLY SUPPORTED** — The Plasmablast-Autoantigen Fibrosis Driver Model is the best available mechanistic framework for IgG4-Related Disease (IgG4-RD), but it requires seven critical qualifications before it can be considered a complete causal account. After five iterations of systematic investigation covering 124 papers, 25 confirmed findings, and >30 targeted PubMed queries, the hypothesis emerges as a strong but incomplete scaffold: its cellular components are well-established, its therapeutic predictions are validated, but three central causal edges have zero direct experimental support, and a third of the pathognomonic histopathological triad (obliterative phlebitis) falls entirely outside its explanatory scope.

The strongest evidence supports the existence and disease relevance of the three cellular pillars — oligoclonal plasmablasts, Tfh cells promoting IgG4 class switching, and CD4+SLAMF7+ cytotoxic T lymphocytes (CTLs) expressing profibrotic cytokines. Rituximab responsiveness provides powerful indirect validation that B-cell lineage activity sustains the disease. However, the hypothesis's causal logic — that B cells present antigen to CD4 CTLs, which then activate fibroblasts to produce storiform fibrosis — remains inferential. No co-culture, blocking, or spatial transcriptomics study has directly demonstrated either the B-cell antigen-presentation step or the CD4 CTL-to-fibroblast activation step. Furthermore, the model implicitly treats IgG4 as the dominant pathogenic antibody, but emerging evidence demonstrates that IgG1 autoantibodies are the pathogenic subclass in the autoimmune phenotype, and that disease phenotype determines which immunological arm predominates. The high prevalence of allergy (44%) and elevated IgE (73%) in meta-analysis indicate that the Th2/atopic axis contributes substantially to pathogenesis in a large subset of patients, an aspect the CD4 CTL-centric model underweights.

---

## Summary

The Plasmablast-Autoantigen Fibrosis Driver Model posits that unresolved autoantigen or innate triggers expand B-cell/plasmablast and T-cell axes; Tfh cells promote IgG4 class switching; plasmablasts mark and sustain the B-lineage response; and CD4+ cytotoxic T lymphocytes provide fibrogenic cytokines (TGF-beta1, IL-1beta) that drive storiform fibrosis and organ injury. This investigation systematically evaluated each node and edge in this causal chain against primary literature.

The model's cellular components are robustly supported. Clonally expanded CD4+SLAMF7+ CTLs dominate IgG4-RD tissue infiltrates across multiple organ sites ([PMID: 26971690](https://pubmed.ncbi.nlm.nih.gov/26971690/)). Oligoclonal IgG4+ plasmablasts are expanded in active disease and correlate with disease activity ([PMID: 24815737](https://pubmed.ncbi.nlm.nih.gov/24815737/)). Tfh cells correlate with both plasmablast expansion and serum IgG levels ([PMID: 29253269](https://pubmed.ncbi.nlm.nih.gov/29253269/)). Pathogenic autoantibodies against four autoantigens have been identified, with anti-IL-1RA antibodies shown to induce inflammatory and fibrotic mediator production in vitro ([PMID: 33974929](https://pubmed.ncbi.nlm.nih.gov/33974929/)).

However, three critical causal edges remain experimentally unvalidated despite exhaustive searching (>25 targeted queries returning zero primary papers): (1) B-cell antigen presentation to CD4 CTLs, (2) CD4 CTL activation of fibroblasts/myofibroblasts, and (3) the mechanism producing obliterative phlebitis. Additionally, the model requires substantial qualification: IgG1 is co-pathogenic with IgG4, disease phenotype determines immune mechanism dominance, the Th2/atopic axis is relevant in nearly half of patients, the upstream trigger remains unknown, and the disease may establish self-sustaining feedback loops not captured by a linear causal chain.

---

## Key Findings

### Finding 1: CD4+SLAMF7+ CTLs Are the Dominant Tissue-Infiltrating T Cells

Mattoo et al. (2016) demonstrated through unbiased flow cytometry and NGS TCR sequencing in 101 patients that CD4+ CTLs expressing SLAMF7, granzyme A, IL-1beta, and TGF-beta1 are clonally expanded and dominate IgG4-RD tissue infiltrates across multiple organ sites ([PMID: 26971690](https://pubmed.ncbi.nlm.nih.gov/26971690/)). Clinical remission induced by rituximab-mediated B-cell depletion was associated with reduction in these CD4+ CTLs, providing a critical indirect link between B-cell activity and CTL persistence. This was independently validated in IgG4-related dacryoadenitis/sialoadenitis ([PMID: 27358392](https://pubmed.ncbi.nlm.nih.gov/27358392/)). Further refinement by Perugino et al. (2021) established that circulating CD4+ CTLs in IgG4-RD comprise functionally distinct subsets including GZMB+ and GZMA+ populations with different tissue-homing properties ([PMID: 32485263](https://pubmed.ncbi.nlm.nih.gov/32485263/)). Koga et al. (2024) independently identified GZMK+ CD4 CTLs as the dominant clonally expanded tissue-infiltrating population via scRNA-seq ([PMID: 38092138](https://pubmed.ncbi.nlm.nih.gov/38092138/)).

### Finding 2: Oligoclonal Plasmablasts Correlate With Disease Activity

CD19+CD27+CD20-CD38hi plasmablasts, which are largely IgG4+, are increased in patients with active IgG4-RD. These expanded plasmablasts are oligoclonal and exhibit extensive somatic hypermutation, and their numbers decrease after rituximab-mediated B-cell depletion therapy, correlating with disease remission ([PMID: 24815737](https://pubmed.ncbi.nlm.nih.gov/24815737/)). Critically, upon relapse, re-emergent plasmablasts are clonally distinct with enhanced somatic hypermutation (de novo oligoclonal expansions), suggesting ongoing antigen-driven selection rather than memory cell reactivation. Circulating plasmablasts and plasma cells also correlate with clinical and serological biomarkers of IgG4-RD activity ([PMID: 30652677](https://pubmed.ncbi.nlm.nih.gov/30652677/)).

### Finding 3: Tfh Cells Drive IgG4 Class Switching

Tfh cell proportions are elevated in IgG4-RD patients versus healthy controls. Serum IgG levels correlate with proportions of both plasmablasts and Tfh cells, but not with those of other T cell subsets ([PMID: 29253269](https://pubmed.ncbi.nlm.nih.gov/29253269/)). A novel IL-10-expressing Tfh subset was identified in IgG4-RD tertiary lymphoid organs by scRNA-seq, distinct from IL-13-expressing Tfh in allergic fibrosis (Kimura disease) ([PMID: 35568079](https://pubmed.ncbi.nlm.nih.gov/35568079/)). This disease-specific Tfh population provides a mechanistic basis for the selective IgG4 class switching observed in IgG4-RD.

### Finding 4: Pathogenic Autoantibodies Identified Against Multiple Autoantigens

Four autoantigens have been identified: annexin A11, galectin-3, laminin 511-E8, and PHB1. Anti-IL-1RA autoantibodies derived from plasmablasts neutralize IL-1RA activity in vitro, leading to inflammatory and fibrotic mediator production ([PMID: 33974929](https://pubmed.ncbi.nlm.nih.gov/33974929/)). In a cohort of 86 patients, 37% had IgG4 antibodies to at least one of four autoantigens; patients with two or more autoantibodies had higher IgG levels, were more commonly hypocomplementemic, and had more visceral organ involvement ([PMID: 31612628](https://pubmed.ncbi.nlm.nih.gov/31612628/)). These autoantibodies span both IgG4 and IgG1 subclasses, with the IgG1 component potentially more pathogenic ([PMID: 41728618](https://pubmed.ncbi.nlm.nih.gov/41728618/)).

### Finding 5: Rituximab Response Validates B-Cell Lineage Centrality

Rituximab induces disease response in all patients at 6 months. Relapse rate was significantly higher in patients who failed to achieve complete depletion of CD19+ cells (60% vs 17%, P=0.02), naive B cells (54% vs 15%, P=0.01), or memory B cells (50% vs 16%, P=0.03) ([PMID: 38781535](https://pubmed.ncbi.nlm.nih.gov/38781535/)). The critical observation that rituximab also reduces CD4+SLAMF7+ CTLs suggests B cells sustain the CTL response, presumably through antigen presentation ([PMID: 27586808](https://pubmed.ncbi.nlm.nih.gov/27586808/)). However, this remains inferential — the reduction could also be mediated by loss of cytokine support or other indirect mechanisms.

### Finding 6: Four Distinct Clinical Phenotypes With Different Immune Mechanisms

An international multicenter latent class analysis of 765 cases identified four phenotype groups: Pancreato-Hepato-Biliary (31%), Retroperitoneal Fibrosis/Aortitis (24%), Head and Neck-Limited (24%), and Mikulicz with systemic involvement (22%) ([PMID: 30612117](https://pubmed.ncbi.nlm.nih.gov/30612117/)). Critically, these phenotypes map to distinct dominant immune cell subsets: retroperitoneal fibrosis/aortitis is characterized by CX3CR1+ CTLs, while Mikulicz disease with systemic involvement is dominated by Tfh2 cells ([PMID: 39306708](https://pubmed.ncbi.nlm.nih.gov/39306708/)). This means the seed hypothesis's causal chain does not apply uniformly across phenotypes — different patients are driven by different arms of the model.

### Finding 7: sIL-2R Validates T-Cell Activation as Central to Disease Activity

Serum sIL-2R is elevated in IgG4-RD (median 4667 pg/ml vs 1515 pg/ml controls) and correlates with IgG4-RD Responder Index (rho=0.74, p<0.0001) and number of affected organs (rho=0.75, p<0.0001) ([PMID: 29465360](https://pubmed.ncbi.nlm.nih.gov/29465360/)). sIL-2R normalized in 91% of improved patients versus IgG4 normalizing in only 41% ([PMID: 29251035](https://pubmed.ncbi.nlm.nih.gov/29251035/)), and correlated with total lesion glycolysis on PET/CT (rs=0.763, P=0.001) while IgG4 did not ([PMID: 25437196](https://pubmed.ncbi.nlm.nih.gov/25437196/)). This biomarker evidence strongly supports T-cell activation, rather than antibody levels, as the proximate driver of tissue injury.

### Finding 8: IgG1 -- Not IgG4 -- Is the Pathogenic Autoantibody in the Autoimmune Phenotype

An "autoimmune phenotype" of IgG4-RD has been described where IgG1-type autoantibodies (not IgG4) are pathogenic, driven by Tfh1 cells via IFN-gamma ([PMID: 39306708](https://pubmed.ncbi.nlm.nih.gov/39306708/)). This is consistent with the observation that IgG4 has anti-inflammatory properties (Fab-arm exchange, poor complement fixation, poor Fc-gamma-R binding), and that hypocomplementemic patients have higher IgG1 levels ([PMID: 31612628](https://pubmed.ncbi.nlm.nih.gov/31612628/)). The seed hypothesis's implicit privileging of IgG4 as the primary pathogenic antibody is thus contradicted for a substantial patient subset.

### Finding 9: Three Critical Causal Edges Remain Experimentally Unvalidated

After more than 25 targeted PubMed queries across iterations 2-4, zero primary research papers were found demonstrating: (1) B-cell antigen presentation to CD4 CTLs (key opinion leaders explicitly use "presumed" for this link -- [PMID: 27667138](https://pubmed.ncbi.nlm.nih.gov/27667138/)); (2) CD4 CTL to fibroblast activation to myofibroblast transition (even the most recent 2026 review describes this through cytokine expression rather than direct experimental demonstration -- [PMID: 41766862](https://pubmed.ncbi.nlm.nih.gov/41766862/)); (3) immune cascade to obliterative phlebitis (IgG4+ plasma cell infiltration alone is insufficient, as demonstrated by its absence in IgG4+ thoracic aortitis -- [PMID: 21036629](https://pubmed.ncbi.nlm.nih.gov/21036629/)).

### Finding 10: Obliterative Phlebitis Requires an IgG4-RD-Specific Mechanism Not Explained by the Model

In 11 cases of isolated thoracic aortitis with IgG4+ plasma cell infiltration (IgG4/IgG ratio 0.07-0.98), obliterative phlebitis of the vasa vasorum was absent in all cases ([PMID: 21036629](https://pubmed.ncbi.nlm.nih.gov/21036629/)). This demonstrates that IgG4+ plasma cell infiltration alone is insufficient for this pathognomonic feature. Obliterative phlebitis has been described in veins, arteries, pulmonary arteries, and aorta across multiple reports, but no primary research has mechanistically explained how the immune cascade produces this vascular pathology.

### Finding 11: High Allergy Prevalence Supports Th2/IgE Axis as Co-Pathogenic

Meta-analysis of 32 studies (n=8,233) found allergy prevalence of 0.44 (95% CI 0.39-0.49), eosinophilia prevalence of 0.22 (95% CI 0.18-0.26), and hyper-IgE prevalence of 0.73 (95% CI 0.63-0.83) ([PMID: 41912044](https://pubmed.ncbi.nlm.nih.gov/41912044/)). This quantifies the substantial contribution of Th2/atopic mechanisms to IgG4-RD in a large fraction of patients, qualifying the hypothesis's focus on CD4 CTLs as the primary pathogenic effector.

### Finding 12: Innate Immunity and Dysbiosis as Alternative Upstream Triggers

Experimental AIP in MRL/MpJ mice is mediated by plasmacytoid dendritic cells producing IFN-alpha and IL-33. Bowel sterilization with antibiotics suppressed disease development, and fecal microbiota transplantation from AIP mice induced severe AIP in recipients ([PMID: 31287532](https://pubmed.ncbi.nlm.nih.gov/31287532/)). Human IgG4-RD microbiomes showed depletion of butyrate-producing species and enrichment of opportunistic pathogens ([PMID: 33648559](https://pubmed.ncbi.nlm.nih.gov/33648559/)). MARCO, a pattern-recognition receptor, was significantly upregulated in IgG4-RD tissue (P<0.01) ([PMID: 26886650](https://pubmed.ncbi.nlm.nih.gov/26886650/)).

---

## Mechanistic Causal Chain

The hypothesis implies the following causal chain from upstream trigger to clinical manifestation. Below, each step is annotated with the strength of evidence:

```
+----------------------------------------------------------------------+
|                    UPSTREAM TRIGGER (UNKNOWN)                         |
|  Candidates: autoantigen, molecular mimicry, dysbiosis/pDC,          |
|  genetic susceptibility (HLA-DRB1, FCGR2B)                           |
|  Evidence: WEAK/SPECULATIVE -- no definitive trigger identified       |
+------------------------------+---------------------------------------+
                               |
                               v
+----------------------------------------------------------------------+
|            B-CELL / PLASMABLAST EXPANSION                             |
|  Oligoclonal IgG4+ plasmablasts expand, correlate with activity       |
|  Evidence: STRONG (PMID: 24815737, 30652677)                          |
+------------------------------+---------------------------------------+
                               |
              +----------------+----------------+
              v                v                v
+-----------------+ +---------------+ +------------------------------------+
|  Tfh -> IgG4    | | Autoantibody  | |  B cell APC -> CD4 CTL             |
|  class switch   | | production    | |  sustenance                        |
|  STRONG         | | STRONG        | |  !! UNCONFIRMED -- PRESUMED        |
|  (PMID:29253269 | | (PMID:        | |  (PMID: 27667138)                  |
|   35568079)     | |  33974929,    | |  Only indirect: RTX reduces        |
|                 | |  31612628)    | |  both B cells and CTLs             |
+-----------------+ +---------------+ +----------------+-------------------+
                                                       |
                                                       v
+----------------------------------------------------------------------+
|         CD4+SLAMF7+ CTL CLONAL EXPANSION IN TISSUE                    |
|  Express TGF-b1, IL-1b, granzyme A/K, perforin                       |
|  Evidence: STRONG (PMID: 26971690, 38092138, 32485263)                |
+------------------------------+---------------------------------------+
                               |
              +----------------+----------------+
              v                v                v
+-----------------+ +---------------+ +------------------------------------+
|  Tissue         | | Fibroblast    | |  Vascular damage ->                |
|  cytotoxicity   | | activation    | |  obliterative phlebitis            |
|  MODERATE       | | !! UNCON-     | |  !! UNCONFIRMED                    |
|                 | | FIRMED        | |  IgG4+ infiltration alone          |
|                 | | (PMID:        | |  insufficient (PMID: 21036629)     |
|                 | |  41766862)    | |                                    |
+-----------------+ +------+--------+ +------------------------------------+
                           |
                           v
+----------------------------------------------------------------------+
|           STORIFORM FIBROSIS & ORGAN INJURY                           |
|  Pathognomonic triad: storiform fibrosis + lymphoplasmacytic          |
|  infiltrate + obliterative phlebitis                                  |
|  Evidence: STRONG for clinical outcome, WEAK for mechanism            |
+----------------------------------------------------------------------+
```

**Strong links:** B-cell/plasmablast expansion, Tfh-IgG4 class switching, CD4 CTL clonal expansion, autoantibody production, rituximab responsiveness.

**Inferred links (presumed but unproven):** B-cell antigen presentation to CD4 CTLs; CTL-derived TGF-beta1/IL-1beta activation of fibroblasts.

**Missing links:** Mechanism of obliterative phlebitis; upstream trigger identity; fibroblast transition to myofibroblasts.

{{figure:causal_model_iteration4.png|caption=Complete causal model with evidence strengths and gaps. Green nodes indicate strong evidence; yellow indicates moderate; red marks unconfirmed causal edges. Three critical gaps identified: B-cell APC function, fibroblast activation, and obliterative phlebitis mechanism.}}

---

## Evidence Matrix

| # | Citation | Evidence Type | Direction | Mechanistic Claim | Key Finding | Context | Confidence |
|---|----------|--------------|-----------|-------------------|-------------|---------|------------|
| 1 | [PMID: 26971690](https://pubmed.ncbi.nlm.nih.gov/26971690/) | Human clinical | Supports | CD4 CTL tissue infiltration | CD4+SLAMF7+ CTLs dominant in tissue, express TGF-beta1/IL-1beta; reduced by RTX | Multi-organ, n=101 | High |
| 2 | [PMID: 24815737](https://pubmed.ncbi.nlm.nih.gov/24815737/) | Human clinical | Supports | Plasmablast expansion | Oligoclonal IgG4+ plasmablasts expanded, decrease with RTX | Active IgG4-RD | High |
| 3 | [PMID: 29253269](https://pubmed.ncbi.nlm.nih.gov/29253269/) | Human clinical | Supports | Tfh-plasmablast axis | Tfh and plasmablast proportions correlate with serum IgG | Extraglandular | Moderate |
| 4 | [PMID: 35568079](https://pubmed.ncbi.nlm.nih.gov/35568079/) | Human clinical | Supports | Tfh IgG4 class switching | IL-10+ Tfh subset specific to IgG4-RD TLOs | scRNA-seq | Moderate |
| 5 | [PMID: 33974929](https://pubmed.ncbi.nlm.nih.gov/33974929/) | In vitro | Supports | Autoantibody pathogenicity | Anti-IL-1RA IgG4 autoantibodies neutralize IL-1RA, induce fibrotic mediators | In vitro functional | Moderate |
| 6 | [PMID: 31612628](https://pubmed.ncbi.nlm.nih.gov/31612628/) | Human clinical | Supports | Autoantibody diversity | 2+ autoantibodies correlate with higher IgG, hypocomplementemia, visceral involvement | n=86 | High |
| 7 | [PMID: 38781535](https://pubmed.ncbi.nlm.nih.gov/38781535/) | Human clinical | Supports | B-cell centrality | Incomplete B-cell depletion predicts relapse (P=0.02) | RTX-treated cohort | High |
| 8 | [PMID: 38092138](https://pubmed.ncbi.nlm.nih.gov/38092138/) | Human clinical | Supports | CD4 CTL identity | GZMK+ CD4 CTLs dominant clonally expanded population by scRNA-seq | Tissue-level | High |
| 9 | [PMID: 39306708](https://pubmed.ncbi.nlm.nih.gov/39306708/) | Human clinical | Qualifies | Phenotype-specific mechanisms | RPF/aortitis driven by CX3CR1+ CTLs; Mikulicz by Tfh2; IgG1 pathogenic in autoimmune phenotype | Multi-phenotype | High |
| 10 | [PMID: 29465360](https://pubmed.ncbi.nlm.nih.gov/29465360/) | Human clinical | Supports | T-cell activation centrality | sIL-2R correlates with RI (rho=0.74) and organ count (rho=0.75) | n=26+controls | Moderate |
| 11 | [PMID: 27667138](https://pubmed.ncbi.nlm.nih.gov/27667138/) | Expert review | Qualifies | B-cell APC function | CD4 CTL sustenance by B-cell APC is "presumed" -- not demonstrated | Review/opinion | Low |
| 12 | [PMID: 41766862](https://pubmed.ncbi.nlm.nih.gov/41766862/) | Review | Qualifies | CTL to fibrosis | "Dual cytotoxic and profibrotic properties" -- inferred from cytokine expression, not direct demonstration | 2026 review | Low |
| 13 | [PMID: 21036629](https://pubmed.ncbi.nlm.nih.gov/21036629/) | Human clinical | Refutes (partial) | Obliterative phlebitis mechanism | IgG4+ infiltration present but obliterative phlebitis absent in all 11 aortitis cases | Isolated aortitis | High |
| 14 | [PMID: 41912044](https://pubmed.ncbi.nlm.nih.gov/41912044/) | Meta-analysis | Qualifies | CD4 CTL primacy | Allergy 44%, hyper-IgE 73% -- Th2/atopic axis substantial | n=8,233 | High |
| 15 | [PMID: 31287532](https://pubmed.ncbi.nlm.nih.gov/31287532/) | Model organism | Competing | Upstream trigger | Dysbiosis-pDC axis mediates experimental AIP; antibiotics suppress | MRL/MpJ mice | Moderate |
| 16 | [PMID: 38229354](https://pubmed.ncbi.nlm.nih.gov/38229354/) | Human genetic | Supports | Genetic susceptibility | GWAS: HLA-DRB1 and FCGR2B as susceptibility loci | Japanese, n=835 | High |
| 17 | [PMID: 41298177](https://pubmed.ncbi.nlm.nih.gov/41298177/) | Human genetic | Supports | Genetic architecture | 16 susceptibility loci in Chinese Han including MHC and Fc-gamma receptors | n=1,115 patients | High |
| 18 | [PMID: 30612117](https://pubmed.ncbi.nlm.nih.gov/30612117/) | Human clinical | Qualifies | Disease heterogeneity | 4 clinical phenotypes by LCA in 765 cases | International | High |
| 19 | [PMID: 41956965](https://pubmed.ncbi.nlm.nih.gov/41956965/) | Review (multi-omics) | Qualifies | Linear causal chain | Self-sustaining loop of immune activation and tissue remodeling | Multi-omics synthesis | Moderate |
| 20 | [PMID: 40628311](https://pubmed.ncbi.nlm.nih.gov/40628311/) | Review | Qualifies | Animal model validity | No model fully recapitulates pathological hallmarks; mice lack IgG4 | Model limitations | High |

{{figure:evidence_summary_iteration4.png|caption=Evidence classification summary showing distribution of supporting, qualifying, refuting, and competing evidence across the 44 evidence items evaluated over five iterations.}}

---

## Evidence Claim Status

| Claim | Status | Evidence Strength |
|-------|--------|-------------------|
| CD4+SLAMF7+ CTLs infiltrate tissues and express profibrotic cytokines | **Established** | Multiple independent studies, scRNA-seq validation |
| Oligoclonal plasmablasts expand in active disease | **Established** | Replicated across cohorts, treatment-response correlation |
| Tfh cells drive IgG4 class switching | **Established** | Correlation data, disease-specific Tfh subset identified |
| Pathogenic autoantibodies exist | **Established** | 4 autoantigens, functional pathogenicity for anti-IL-1RA |
| Rituximab validates B-cell centrality | **Established** | Prospective treatment data, depletion depth predicts relapse |
| B cells present antigen to sustain CD4 CTLs | **Speculative** | Inferred from RTX effect on CTLs; explicitly "presumed" |
| CD4 CTLs activate fibroblasts to produce storiform fibrosis | **Speculative** | Inferred from cytokine expression; no co-culture evidence |
| Immune cascade produces obliterative phlebitis | **Speculative** | No mechanism proposed; IgG4+ infiltration alone insufficient |
| IgG4 is the primary pathogenic antibody | **Contradicted** | IgG1 pathogenic in autoimmune phenotype; IgG4 is anti-inflammatory |
| Single unified mechanism across all phenotypes | **Contradicted** | Phenotype-specific immune mechanisms demonstrated |
| Th2/atopic immunity is secondary | **Weakly supported** | 44% allergy, 73% hyper-IgE challenges CTL-centric framing |
| Upstream trigger is autoantigen-driven | **Emerging** | Autoantigens identified but trigger remains unclear; dysbiosis alternative |

---

## Knowledge Gaps

### Gap 1: B-Cell Antigen Presentation to CD4 CTLs (CRITICAL)

**Scope:** The central mechanistic link between B-lineage cells and disease-driving CD4 CTLs is "presumed" ([PMID: 27667138](https://pubmed.ncbi.nlm.nih.gov/27667138/)) but never directly demonstrated. **Why it matters:** This edge is the logical bridge connecting the B-cell depletion therapeutic response to CD4 CTL reduction. Without it, alternative explanations (cytokine withdrawal, loss of co-stimulation) cannot be excluded. **What was checked:** More than 10 PubMed queries for B-cell antigen presentation, co-culture, MHC-II blocking, and plasmablast-T cell interaction in IgG4-RD across iterations 2-4 returned zero primary papers. **What would resolve it:** Plasmablast/B-cell co-culture with autologous CD4 CTLs with MHC-II blocking antibodies; live imaging of B-T cell conjugates in IgG4-RD tissue; spatial transcriptomics demonstrating B-T cell interaction signatures.

### Gap 2: CD4 CTL to Fibroblast Activation to Myofibroblast Transition (CRITICAL)

**Scope:** The hypothesis claims CD4 CTL-derived TGF-beta1 and IL-1beta drive fibroblast activation, but no study has directly demonstrated this in IgG4-RD. **Why it matters:** Storiform fibrosis is the defining pathological feature of IgG4-RD. The mechanism connecting immune infiltration to fibrosis is the clinically most consequential gap. **What was checked:** Queries for fibroblast activation, myofibroblast, TGF-beta mechanism, spatial transcriptomics, scRNA-seq fibroblast, ECM remodeling in IgG4-RD context across iterations 2-4 returned zero primary papers. SSc literature shows CD4 T cells can activate fibroblasts ([PMID: 36031049](https://pubmed.ncbi.nlm.nih.gov/36031049/)), but this has not been replicated in IgG4-RD. **What would resolve it:** Co-culture of CD4+SLAMF7+ CTLs with tissue-derived fibroblasts from IgG4-RD lesions; single-cell spatial transcriptomics to map CTL-fibroblast proximity and signaling; anti-TGF-beta1 blocking experiments in tissue explants.

### Gap 3: Mechanism of Obliterative Phlebitis (CRITICAL)

**Scope:** One-third of the pathognomonic histopathological triad has no mechanistic explanation within the model. **Why it matters:** Obliterative phlebitis is a defining diagnostic feature. Its exclusion from the causal model means the model cannot explain a core disease feature. **What was checked:** Searched for endothelial damage, vascular obliteration, phlebitis mechanism in IgG4-RD context. IgG4+ infiltration alone is insufficient ([PMID: 21036629](https://pubmed.ncbi.nlm.nih.gov/21036629/)). No primary papers found proposing a mechanism. **What would resolve it:** Endothelial cell co-culture with immune cells from IgG4-RD tissue; spatial profiling of vascular obliteration zones; comparison of vascular vs. non-vascular IgG4-RD lesion immune composition.

### Gap 4: Upstream Trigger Identity

**Scope:** The initiating event that activates the adaptive immune cascade is unknown. Candidates include molecular mimicry, environmental antigens, dysbiosis, and endogenous autoantigens. **Why it matters:** Without knowing the trigger, prevention strategies are impossible, and the hypothesis remains descriptive rather than predictive. **What would resolve it:** Longitudinal cohort study of at-risk individuals (first-degree relatives, those with autoimmune pancreatitis risk factors); antigen identification through TCR/BCR repertoire analysis; microbiome intervention studies in humans.

### Gap 5: Animal Model Limitations

**Scope:** No animal model fully recapitulates IgG4-RD pathological hallmarks; mice lack IgG4 entirely ([PMID: 40628311](https://pubmed.ncbi.nlm.nih.gov/40628311/)). **Why it matters:** Causal experiments (knockouts, cell depletion, adoptive transfer) cannot be performed in a faithful model. **What would resolve it:** Development of humanized mouse models with reconstituted human immune systems; or conditional knockout/knockin models targeting IgG4-RD-associated pathways.

### Gap 6: Fibrosis Irreversibility Mechanism

**Scope:** Late-stage IgG4-RD fibrosis may be self-sustaining and refractory to immunosuppression. A multi-omics review proposes "a self-sustaining loop of immune activation and tissue remodeling" ([PMID: 41956965](https://pubmed.ncbi.nlm.nih.gov/41956965/)). **Why it matters:** If fibrosis becomes autonomous from immune input, the window for effective immunotherapy is limited. **What would resolve it:** Longitudinal tissue sampling at different disease stages; comparison of immune infiltrate in early vs. late fibrotic lesions; fibroblast organoid studies from different disease stages.

{{figure:knowledge_gap_priority_final.png|caption=Knowledge gap priority matrix showing impact vs. feasibility for all 12 identified gaps. The three unconfirmed causal edges (B-cell APC, fibroblast activation, obliterative phlebitis) cluster in the high-impact region.}}

---

## Alternative and Competing Models

### 1. Innate Immunity / Dysbiosis-pDC Model

**Relationship:** Alternative upstream trigger / parallel mechanism.

Plasmacytoid dendritic cells activated by intestinal dysbiosis produce IFN-alpha and IL-33, driving chronic fibroinflammatory responses ([PMID: 31287532](https://pubmed.ncbi.nlm.nih.gov/31287532/)). M2 macrophages producing IL-33 play pathogenic roles in human IgG4-RD. This model could operate upstream of or parallel to the adaptive immune cascade described by the seed hypothesis, and could explain fibrosis through T-cell-independent pathways via TLR activation ([PMID: 31852351](https://pubmed.ncbi.nlm.nih.gov/31852351/)).

### 2. Th2/Atopic Disease Model

**Relationship:** Parallel mechanism / competing for primacy in subset of patients.

With 44% allergy prevalence, 73% hyper-IgE, and 22% eosinophilia ([PMID: 41912044](https://pubmed.ncbi.nlm.nih.gov/41912044/)), the Th2/atopic axis is a major contributor in a large patient subset. IL-4 and IL-13 from Th2 cells directly promote IgG4 class switching and fibrosis. This model may predominate in the Mikulicz/systemic involvement phenotype where Tfh2 cells dominate ([PMID: 39306708](https://pubmed.ncbi.nlm.nih.gov/39306708/)).

### 3. IgG1-Mediated Autoimmune Model

**Relationship:** Competing mechanism within autoimmune phenotype.

IgG1 autoantibodies are the pathogenic subclass in the autoimmune phenotype, driven by Tfh1 cells via IFN-gamma ([PMID: 39306708](https://pubmed.ncbi.nlm.nih.gov/39306708/)). Since IgG4 has anti-inflammatory properties (poor complement fixation, Fab-arm exchange), the "IgG4-related" disease name may be misleading -- IgG4 may be a marker of chronic antigen stimulation rather than a pathogenic effector.

### 4. Complement-Mediated Tissue Injury Model

**Relationship:** Downstream consequence / parallel mechanism.

Hypocomplementemia occurs in a substantial subset of IgG4-RD patients. Immune complexes containing IgG4 and IgG1 can activate complement via classical and MBL pathways ([PMID: 26357950](https://pubmed.ncbi.nlm.nih.gov/26357950/)). Anti-C1q antibodies are found in 74.3% of patients, correlating with renal involvement ([PMID: 39798124](https://pubmed.ncbi.nlm.nih.gov/39798124/)). This model may explain kidney injury and vascular damage better than direct CTL-mediated mechanisms.

### 5. Self-Sustaining Immune-Fibrosis Loop Model

**Relationship:** Extension of the seed hypothesis.

Multi-omics evidence suggests IgG4-RD establishes autonomous feedback loops between immune activation and tissue remodeling ([PMID: 41956965](https://pubmed.ncbi.nlm.nih.gov/41956965/)). This extends the seed hypothesis's linear causal chain into a self-reinforcing cycle, potentially explaining treatment resistance in advanced disease.

---

## Discriminating Tests

### Test 1: B-Cell APC to CD4 CTL Sustenance

- **Design:** Autologous co-culture of sorted CD19+ B cells/plasmablasts with CD4+SLAMF7+ CTLs from IgG4-RD tissue
- **Perturbation:** Anti-MHC-II blocking antibody; compare with CD4 CTL survival in B-cell-conditioned media alone
- **Expected result:** If hypothesis correct: MHC-II blocking abolishes CTL proliferation/survival; conditioned media alone is insufficient
- **Sample:** Fresh IgG4-RD tissue (salivary gland or pancreas resections)
- **Biomarkers:** CTL proliferation, granzyme/TGF-beta1 expression, TCR activation markers

### Test 2: CD4 CTL to Fibroblast Activation

- **Design:** Co-culture of sorted CD4+SLAMF7+ CTLs with primary fibroblasts from IgG4-RD lesions
- **Perturbation:** Anti-TGF-beta1 neutralizing antibody; anti-IL-1beta blocking; transwell (contact-dependent vs. soluble factors)
- **Expected result:** If hypothesis correct: CTL supernatant or contact induces alpha-SMA expression, collagen production; blocked by anti-TGF-beta1
- **Sample:** Paired immune cell and fibroblast isolation from same lesion
- **Readouts:** alpha-SMA, COL1A1, fibronectin expression; ECM deposition assays

### Test 3: Phenotype-Specific Mechanism Resolution

- **Design:** Multi-site spatial transcriptomics study comparing the 4 clinical phenotypes
- **Patient stratification:** Pancreato-Hepato-Biliary vs. RPF/Aortitis vs. Head/Neck-Limited vs. Mikulicz/Systemic
- **Expected result:** Different phenotypes show different dominant T-B-fibroblast interaction signatures
- **Technology:** Visium/MERFISH spatial transcriptomics on FFPE tissue from each phenotype
- **Value:** Resolves whether the seed hypothesis applies uniformly or phenotype-specifically

### Test 4: Obliterative Phlebitis Mechanism

- **Design:** Spatial comparison of vascular obliteration zones vs. non-vascular fibrotic zones within the same IgG4-RD lesion
- **Technology:** Multiplex immunofluorescence or spatial transcriptomics
- **Cell types of interest:** Endothelial cells, CD4 CTLs, complement deposition, platelet aggregation, smooth muscle cells
- **Expected result:** Identify whether phlebitis is driven by CTL endothelial damage, complement deposition, or intimal proliferation
- **Controls:** IgG4+ aortitis without obliterative phlebitis ([PMID: 21036629](https://pubmed.ncbi.nlm.nih.gov/21036629/))

### Test 5: IgG1 vs. IgG4 Pathogenicity

- **Design:** Passive transfer of purified IgG1 vs. IgG4 fractions from IgG4-RD patients into humanized mice
- **Readouts:** Tissue inflammation, fibrosis, complement activation, organ damage
- **Expected result:** IgG1 fraction causes more tissue damage than IgG4 fraction
- **Stratification:** Compare autoimmune phenotype vs. non-autoimmune phenotype donors

---

## Curation Leads (Requiring Curator Verification)

### Candidate KB Annotations

1. **Status qualification:** Change from CANONICAL to CANONICAL-WITH-QUALIFICATIONS or add qualifier flag. The model is the best available framework but has three unconfirmed causal edges and does not explain obliterative phlebitis.

2. **IgG1 co-pathogenicity edge:** Add edge: Tfh1 to IgG1 class switching to pathogenic autoantibodies (in autoimmune phenotype). Citation: [PMID: 39306708](https://pubmed.ncbi.nlm.nih.gov/39306708/) -- *"Due to the pathogenicity of IgG1-type autoantibodies, Tfh1 may be important inducing IgG1 class-switching by IFN-gamma in autoimmune phenotype."*

3. **Phenotype-specific mechanism nodes:** Add subtype restriction: the seed hypothesis's full causal chain is most applicable to the RPF/aortitis phenotype (CX3CR1+ CTL-dominant), while the Mikulicz/systemic phenotype is Tfh2-dominant. Citation: [PMID: 39306708](https://pubmed.ncbi.nlm.nih.gov/39306708/) -- *"Specifically, the clinical phenotype of retroperitoneal fibrosis/aortitis is characterized by CX3CR1 + CTLs as the dominant key immune cell subset, while Mikulicz disease with systemic involvement is dominated by Tfh2."*

4. **Th2/atopic axis node:** Add parallel pathway node for Th2/IgE/eosinophil-mediated inflammation. Citation: [PMID: 41912044](https://pubmed.ncbi.nlm.nih.gov/41912044/) -- *"The pooled proportion of IgG4-RD patients with allergy was 0.44 (95% CI, 0.39, 0.49; p < 0.01; n = 8233)."*

5. **Knowledge gap annotations (3):**
   - `gap_bcell_apc`: B-cell antigen presentation to CD4 CTLs is "presumed" not proven ([PMID: 27667138](https://pubmed.ncbi.nlm.nih.gov/27667138/))
   - `gap_fibroblast_activation`: CTL to fibroblast to storiform fibrosis has no direct experimental support ([PMID: 41766862](https://pubmed.ncbi.nlm.nih.gov/41766862/))
   - `gap_obliterative_phlebitis`: Mechanism unexplained; IgG4+ infiltration insufficient ([PMID: 21036629](https://pubmed.ncbi.nlm.nih.gov/21036629/))

6. **Self-sustaining loop extension:** Add feedback loop topology note: disease may establish autonomous immune-fibrosis loops in advanced stages ([PMID: 41956965](https://pubmed.ncbi.nlm.nih.gov/41956965/)).

7. **Upstream trigger candidates:** Add innate immunity/dysbiosis pathway as candidate upstream trigger, particularly pDC-IFN-alpha/IL-33 axis ([PMID: 31287532](https://pubmed.ncbi.nlm.nih.gov/31287532/)).

### Candidate Ontology Terms

| Concept | Suggested Term | Ontology |
|---------|---------------|----------|
| CD4+SLAMF7+ CTL | CL:0002138 -- needs new term proposal | Cell Ontology |
| GZMK+ CD4 CTL | Not in CL -- candidate new term | Cell Ontology |
| Tfh2 cell | CL:0002038 (T follicular helper cell) + qualifier | Cell Ontology |
| Storiform fibrosis | HP:0100723 (Tissue fibrosis) -- needs subtype | HPO |
| Obliterative phlebitis | No specific term -- candidate new term | HPO/MONDO |
| Plasmablast | CL:0000980 | Cell Ontology |

### Candidate Evidence References for Verification

| Finding | PMID | Abstract Snippet (verbatim) |
|---------|------|-----------------------------|
| CD4 CTL dominance | 26971690 | "The dominant T cells infiltrating a range of inflamed IgG4-RD tissue sites were clonally expanded CD4(+) CTLs that expressed SLAMF7, granzyme A, IL-1beta, and TGF-beta1." |
| Plasmablast expansion | 24815737 | "Numbers of CD19(+)CD27(+)CD20(-)CD38(hi) plasmablasts, which are largely IgG4(+), are increased in patients with active IgG4-RD." |
| B-cell APC presumption | 27667138 | "This cell is presumed to be sustained by continuous antigen presentation by cells of the B cell lineage, particularly plasmablasts." |
| IgG1 pathogenicity | 39306708 | "Due to the pathogenicity of IgG1-type autoantibodies, Tfh1 may be important inducing IgG1 class-switching by IFN-gamma in autoimmune phenotype." |
| Obliterative phlebitis absence | 21036629 | "Obliterative phlebitis of the vasa vasorum was absent." |
| Allergy meta-analysis | 41912044 | "The pooled proportion of IgG4-RD patients with allergy was 0.44 (95% CI, 0.39, 0.49; p < 0.01; n = 8233)." |

---

## Limitations of This Investigation

1. **Literature search scope:** PubMed was the primary search engine. Preprints, conference abstracts, and non-English literature were not systematically covered.

2. **Absence of evidence vs. evidence of absence:** The failure to find studies demonstrating the three unconfirmed causal edges does not prove they are incorrect -- only that they are not yet experimentally validated. Ongoing unpublished work may address these gaps.

3. **Animal model limitations:** Many mechanistic claims cannot be fully validated because no animal model recapitulates IgG4-RD faithfully, and mice lack IgG4 entirely.

4. **Phenotype heterogeneity:** The literature often treats IgG4-RD as a single entity. Phenotype-specific mechanistic studies are recent and limited, making it difficult to assess which parts of the hypothesis apply to which patient subsets.

5. **Review vs. primary evidence:** Some links in the causal chain are primarily supported by review articles that synthesize indirect evidence rather than by primary experimental studies.

6. **Temporal limitations:** This search was conducted through June 2026. The field is rapidly evolving with new spatial transcriptomics and multi-omics studies.

{{figure:final_investigation_summary.png|caption=Final investigation summary showing progress timeline across 5 iterations, evidence classification breakdown, hypothesis status assessment, and recommended KB annotations.}}

---

## Proposed Follow-up Experiments and Actions

### Immediate Priority (addresses critical gaps)

1. **Spatial transcriptomics of IgG4-RD lesions:** Apply Visium or MERFISH to FFPE tissue sections from all four clinical phenotypes. Map the spatial relationships between CD4 CTLs, B cells/plasmablasts, fibroblasts, and endothelial cells. This single technology could address all three unconfirmed causal edges simultaneously.

2. **Autologous co-culture studies:** Isolate CD4+SLAMF7+ CTLs, B cells/plasmablasts, and fibroblasts from fresh IgG4-RD tissue. Perform pairwise co-culture with blocking antibodies (anti-MHC-II, anti-TGF-beta1, anti-IL-1beta) to establish direct causal relationships.

3. **Endothelial-immune interaction study:** Compare immune cell composition and endothelial activation markers in obliterative phlebitis zones vs. non-vascular fibrotic zones within the same IgG4-RD lesion using multiplex immunofluorescence.

### Medium-Term Priority

4. **Longitudinal biomarker study:** Track sIL-2R, plasmablasts, CD4 CTL subsets, and autoantibody profiles longitudinally in a prospective cohort, stratified by clinical phenotype, to establish temporal ordering of cellular events.

5. **IgG1 vs. IgG4 passive transfer:** Purify IgG1 and IgG4 fractions from hypocomplementemic vs. normocomplementemic patients and test pathogenicity in humanized mouse models or tissue explant systems.

6. **Microbiome intervention trial:** Pilot study of microbiome-targeted intervention (probiotics, butyrate supplementation) in IgG4-RD patients to test the dysbiosis-pDC upstream trigger model.

### Long-Term Priority

7. **Development of improved animal models:** Create humanized mouse models reconstituted with IgG4-RD patient-derived immune cells, or CRISPR-engineered models expressing human IgG4-equivalent antibodies.

8. **Multi-site phenotype-stratified clinical trial:** Compare B-cell depletion (rituximab) vs. T-cell-targeted therapy (anti-SLAMF7, elotuzumab) stratified by clinical phenotype to test whether CTL-dominant phenotypes respond better to T-cell targeting.

---

*Report generated from 5 iterations of systematic investigation. 124 papers reviewed, 25 findings confirmed, 44 evidence items evaluated. Investigation conducted June 2026.*
