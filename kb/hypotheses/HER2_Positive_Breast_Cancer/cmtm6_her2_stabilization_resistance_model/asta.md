---
provider: asta
model: Asta Scientific Corpus Retrieval
cached: false
start_time: '2026-05-26T23:19:03.773478'
end_time: '2026-05-26T23:19:07.703533'
duration_seconds: 3.93
template_file: templates/hypothesis_deep_research.md
template_variables:
  disease_name: HER2-Positive Breast Cancer
  category: ''
  hypothesis_group_id: cmtm6_her2_stabilization_resistance_model
  hypothesis_label: CMTM6 HER2 Stabilization Resistance Model
  hypothesis_status: EMERGING
  hypothesis_yaml: "hypothesis_group_id: cmtm6_her2_stabilization_resistance_model\n\
    hypothesis_label: CMTM6 HER2 Stabilization Resistance Model\nstatus: EMERGING\n\
    description: Trastuzumab resistance is sustained in part by post-translational\
    \ stabilization of the HER2\n  receptor protein at the cell surface. CMTM6 (CKLF-like\
    \ MARVEL transmembrane domain-containing 6) directly\n  interacts with HER2 and\
    \ inhibits HER2 ubiquitination, preserving the GRB2-adaptor output even under\n\
    \  trastuzumab pressure. Under the interactome- rebalancing framing, CMTM6 acts\
    \ as a separate post-translational\n  pivot point in parallel to GRB2 conformational\
    \ state, and degrading or inhibiting CMTM6 may resensitize\n  tumors to HER2-targeted\
    \ therapy. This hypothesis is independent of (and complementary to) GRB2-level\n\
    \  conformational control.\nevidence:\n- reference: PMID:36627608\n  supports:\
    \ SUPPORT\n  evidence_source: IN_VITRO\n  snippet: these findings highlight that\
    \ CMTM6 stabilizes HER2 protein, contributing to trastuzumab resistance\n    and\
    \ implicate CMTM6 as a potential prognostic marker and therapeutic target for\
    \ overcoming trastuzumab\n    resistance in HER2+ breast cancer\n  explanation:\
    \ Xu et al. directly establish CMTM6-mediated post-translational HER2 stabilization\
    \ as a\n    trastuzumab-resistance mechanism.\n- reference: PMID:36627608\n  supports:\
    \ SUPPORT\n  evidence_source: IN_VITRO\n  snippet: CMTM6 expression was upregulated\
    \ in trastuzumab-resistant HER2+ breast cancer cell\n  explanation: Co-localization,\
    \ co-immunoprecipitation, and ubiquitination data link CMTM6 expression\n    to\
    \ the trastuzumab-resistant state."
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    query_char_limit: 500
    paper_limit: 50
    snippet_limit: 20
    snippet_paper_limit: 50
    restrict_snippets_to_papers: false
    paper_fields: title,abstract,authors,year,url,venue,journal,tldr,publicationDate,citationCount,influentialCitationCount,externalIds
    publication_date_range: ''
    venues: ''
    inserted_before: ''
citation_count: 18
---

## Question

# Mechanistic Hypothesis Search

You are evaluating a specific disease mechanism hypothesis for the Disorder
Mechanisms Knowledge Base. This is not a general disease overview. Use the
hypothesis YAML below as the seed claim, then search for evidence that supports,
refutes, qualifies, or competes with this hypothesis.

## Target Disease
- **Disease Name:** HER2-Positive Breast Cancer
- **Category:**

## Target Hypothesis
- **Hypothesis ID:** cmtm6_her2_stabilization_resistance_model
- **Hypothesis Label:** CMTM6 HER2 Stabilization Resistance Model
- **Status in KB:** EMERGING

## Seed Hypothesis YAML

```yaml
hypothesis_group_id: cmtm6_her2_stabilization_resistance_model
hypothesis_label: CMTM6 HER2 Stabilization Resistance Model
status: EMERGING
description: Trastuzumab resistance is sustained in part by post-translational stabilization of the HER2
  receptor protein at the cell surface. CMTM6 (CKLF-like MARVEL transmembrane domain-containing 6) directly
  interacts with HER2 and inhibits HER2 ubiquitination, preserving the GRB2-adaptor output even under
  trastuzumab pressure. Under the interactome- rebalancing framing, CMTM6 acts as a separate post-translational
  pivot point in parallel to GRB2 conformational state, and degrading or inhibiting CMTM6 may resensitize
  tumors to HER2-targeted therapy. This hypothesis is independent of (and complementary to) GRB2-level
  conformational control.
evidence:
- reference: PMID:36627608
  supports: SUPPORT
  evidence_source: IN_VITRO
  snippet: these findings highlight that CMTM6 stabilizes HER2 protein, contributing to trastuzumab resistance
    and implicate CMTM6 as a potential prognostic marker and therapeutic target for overcoming trastuzumab
    resistance in HER2+ breast cancer
  explanation: Xu et al. directly establish CMTM6-mediated post-translational HER2 stabilization as a
    trastuzumab-resistance mechanism.
- reference: PMID:36627608
  supports: SUPPORT
  evidence_source: IN_VITRO
  snippet: CMTM6 expression was upregulated in trastuzumab-resistant HER2+ breast cancer cell
  explanation: Co-localization, co-immunoprecipitation, and ubiquitination data link CMTM6 expression
    to the trastuzumab-resistant state.
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

# Asta Literature Retrieval: Mechanistic Hypothesis Search You are evaluating a specific disease mechanism hypothesis for the Disorder Mechanisms...

This report is retrieval-only and is generated directly from Asta results.

- Papers retrieved: 18
- Snippets retrieved: 20

## Relevant Papers

### [1] Gathering Evidence of Mechanisms
- Authors: Veli-Pekka Parkkinen, Christian Wallmann, Michael Wilde, B. Clarke, P. Illari et al.
- Year: 2018
- Venue: Unknown venue
- URL: https://www.semanticscholar.org/paper/06480fd932fc88915a4efb4c894a5ae4ed98452d
- DOI: 10.1007/978-3-319-94610-8_5
- Citations: 1
- Summary: Key issues include increased precision concerning the nature of the hypothesis being examined, attention to differences between the study population and the target population of the evidence assessors, and being alert for masking mechanisms, which are other mechanisms which may mask the action of the mechanism being assessed.
- Evidence snippets:
  - Snippet 1 (score: 0.609)
    > General mechanistic claim for efficacy. In formulating the general mechanistic claim for efficacy, the following questions should be addressed:
    > • What is the relevant population?
    > • What is the intervention or exposure level?
    > • What is the outcome and how is it measured? General mechanistic claim for external validity. In determining the general mechanistic claim concerning external validity, the following questions should be addressed:
    > • What is the target population? What is the study population?
    > • What is the intervention or exposure level in the target?
    > • What is the outcome and how is it measured in the target?
    > • What is the intervention or exposure level in the study?
    > • What is the outcome and how is it measured in the study?
    > It may be that existing evidence from clinical studies together with already wellestablished mechanisms is enough to establish the general mechanistic claim. In other cases, the existing evidence fails to establish causality, and it is necessary to identify and evaluate mechanistic studies. To this end, this chapter presents the following five-step strategy for gathering evidence of mechanisms:
    > 1. Identify: Identify a number of specific mechanism hypotheses. 2. Formulate: For each specific mechanism hypothesis, formulate a number of review questions. 3. Search: Use these review questions to search the literature. 4. Refine: Identify the evidence most relevant to the mechanism hypothesis by refining the results of this search. 5. Present. Present the evidence relevant to the mechanism hypothesis. This strategy is intended to help overcome some of the practical difficulties with identifying evidence of mechanisms-difficulties which may prevent appraisers from considering all the relevant evidence. Once this evidence of mechanisms has been identified, it can then be evaluated alongside the existing evidence of correlation from clinical studies, as explained in Chaps. 6 and 7.
    > The overall approach of this chapter is illustrated in Fig. 5.1. The five steps outlined above are explained in detail in the following sections.
  - Snippet 2 (score: 0.553)
    > The overall approach to gathering evidence of mechanisms of action. Each proposed mechanism of action, or partial description of proposed mechanism of action, is a specific mechanism hypothesis. But note that a specific mechanism hypothesis need not be a complete description of a mechanism.
    > Example: Specific mechanism hypotheses for determining efficacy.
    > Aspirin prevents heart disease via cyclooxygenase (COX) inhibition, and the mechanisms that underlie this prevention are established. However, aspirin also seems to reduce the incidence of some cancers. Here, the mechanisms are much less well understood. As Chan et al. (2011) write: "the mechanism of aspirin's antineoplastic effect is less clear, with substantial evidence supporting both COX-dependent and COX-independent mechanisms. Moreover, data supporting the importance of COX-dependent mechanisms are not entirely consistent concerning the relative importance of the COX-1 and COX-2 isoforms in carcinogenesis". In this quotation, the general mechanistic claim is that aspirin exhibits an antineoplastic effect. There are also a couple of more specific mechanism hypotheses, for example, that this antineoplastic effect is mediated by COX-dependent mechanisms. Evidence relating to these more specific mechanism hypotheses provides a way to determine the status of the general mechanistic claim.
    > External validity. In order to evaluate the general mechanistic claim that there is a mechanism in the target population sufficiently similar to the mechanism responsible for the correlation observed in the study population, specific mechanism hypotheses need to pertain to the mechanism of action. It is important to consider the possibility that the mechanism in the target population may contain further component mechanisms that counteract the mechanism of action in the study population and affect the extent of the correlation between the putative cause and effect. So one needs to ask, are there any masking mechanisms in the target population?
    > Example: Specific mechanism hypotheses for determining external validity.
    > According to NICE guidelines, treatment for hypertension should differ depending on ethnicity (NICE 2011). Although ACE-inhibitors have proved beneficial for hypertension in many study populations, there remains the question of whether they are the optimal treatment in some distinct target population, such as African or Caribbean populations.
  - Snippet 3 (score: 0.547)
    > Although ACE-inhibitors have proved beneficial for hypertension in many study populations, there remains the question of whether they are the optimal treatment in some distinct target population, such as African or Caribbean populations. In this case, it is necessary to determine the status of the following general mechanistic claim: the relevant hypertensive mechanisms in the study populations are sufficiently similar to the mechanisms in African or Caribbean populations. This general mechanistic claim can be evaluated by evaluating a more specific mechanism hypothesis, namely that African and Caribbean populations have a lower renin state. As we shall see in Chap. 6, there is some good mechanistic evidence in favour of this specific mechanism hypothesis, and this undermines the general mechanistic claim. This is why, instead, calcium channel blockers are the recommended antihypertensive treatment in African and Caribbean populations (Clarke et al. 2014).
    > There are two main ways to identify a specific mechanism hypothesis. First, a specific mechanism hypothesis may be proposed on the basis of published studies from the clinical study literature. If a clinical study establishes a correlation between a putative cause and effect, and the suggestion is that this correlation is causal, then the authors of such a study usually identify at least one possible mechanism hypothesis of the following form: It is plausible that mechanism with features F links the putative cause and effect in the study population. The study may also point out possible masking mechanisms (Illari 2011). Given this, the discussion section of a published paper that reports the results of a clinical study is a good place to look in order to locate a specific mechanism hypothesis.

### [2] Identification of Biomarkers for Breast Cancer Using Databases
- Authors: Eunhye Lee, A. Moon
- Year: 2016
- Venue: Journal of Cancer Prevention
- URL: https://www.semanticscholar.org/paper/9b33e30afc69380f4e374d30f12b9da9fc4ec013
- DOI: 10.15430/JCP.2016.21.4.235
- PMID: 28053957
- PMCID: 5207607
- Citations: 24
- Summary: This review summarizes the current databases which have been utilized for identification of biomarkers for breast cancer and would be beneficial to seeking appropriate strategies for diagnosis and treatment of breast cancer.
- Evidence snippets:
  - Snippet 1 (score: 0.602)
    > GEO dataset is used to identify biomarkers in specific drugs-resistance breast cancer. One of these is Lapatinib, a dual tyrosine kinase inhibitor that interferes with epidermal growth factor receptor and HER2/neu pathways by treating HER2-positive breast cancer. A study presented a novel strategy for researching the mechanism of laptinib-resistance breast cancers. 31 The oncogenic isoform of HER2, HER2∆16, is expressed with HER2 in nearly 50% of HER2 positive breast tumors, and HER2∆16 drives metastasis and resistance to drugs including tamoxifen and trastuzumab. 32 ][35][36] GEO database contributed to development of technologies and provided information on specific disease characteristics. The aim is enhancing, indexing, linking, searching and displaying capacity in order to permit more data mining. 37 The search engine enlarges the data and it can lead to understanding of unidentified relationships between variety of data types, facilitating novel hypothesis generation, or assisting in the analysis of available information.

### [3] Cross-Resistance Among Sequential Cancer Therapeutics: An Emerging Issue
- Authors: Rossella Loria, P. Vici, F. S. Di Lisa, S. Soddu, M. Maugeri-Saccà et al.
- Year: 2022
- Venue: Frontiers in Oncology
- URL: https://www.semanticscholar.org/paper/cb43697914b25bbaa34869cbe04ffec4defb8ced
- DOI: 10.3389/fonc.2022.877380
- PMID: 35814399
- PMCID: 9259985
- Citations: 29
- Influential citations: 1
- Summary: The main cross-resistance events described in the diverse tumor types are summarized and insight into the molecular mechanisms involved in this process are provided to discuss the current challenges and provide perspectives for the research and development of strategies to overcome cross-Resistance.
- Evidence snippets:
  - Snippet 1 (score: 0.582)
    > The loss of target on HER2-targeted therapy is a widely recognized issue that has been discussed above for both BC (36)(37)(38)(39)(40)(41)(42)(43)(44)(45)(46)(47) and GC (60)(61)(62). Provided that the knowledge of the underlying mechanisms is of paramount relevance, this evidence offers the opportunity to reconsider the strategies behind the design of RCTs. Indeed, many of these studies investigate the efficacy of new therapeutic approaches in metastatic/recurring patients stratified based on the molecular features of primary tumors. Interpreting the results generated from these trials could lead to sub-optimal clinical decision-making.
    > An emblematic example of this is the failure of the randomized phase II study WJOG7112G (T-ACT). The aim of the study was to explore the efficacy of paclitaxel with or without trastuzumab in 99 patients with HER2+ advanced GC who had disease progression after first-line chemotherapy with trastuzumab. Median PFS and OS were not significantly different between the two groups. In this case, loss of HER2 has been reported as a possible explanation for failure. Indeed, when HER2 status was re-evaluated in tumor biopsy specimens from 16 patients following disease progression, HER2 loss was observed in 11 patients (69%) (161).
    > In the specific case of HER2-targeted therapy, re-evaluating the HER2 status at the time of disease progression would be required (43). Supporting this, an ongoing phase II, open-label, single arm trial aimed at evaluating the efficacy and safety of T-Dxd in Western GC patients progressed with a trastuzumabcontaining regimen (DESTINY-Gastric02, NCT04014075) required patients to be re-tested for HER2 positivity before being treated with T-Dxd.
    > The Darwinian selection hypothesis assumes that cancer therapy selects pre-existing mutant cells that overtake the bulk cell population. However, this is a simplified mechanism that does not account for therapy resistance alone. In a more complicated scenario, genetic alterations and changes in the gene expression state often emerge under the selective pressure exerted

### [4] Pharmacokinetic and exposure–response analysis of pertuzumab in patients with HER2-positive metastatic gastric or gastroesophageal junction cancer
- Authors: Whitney P. Kirschbrown, Bei Wang, Ihsan Nijem, A. Ohtsu, P. Hoff et al.
- Year: 2019
- Venue: Cancer Chemotherapy and Pharmacology
- URL: https://www.semanticscholar.org/paper/a492f9caf28f09d00f0c32bddf510e6551559553
- DOI: 10.1007/s00280-019-03871-w
- PMID: 31183514
- PMCID: 6682857
- Citations: 10
- Summary: Pertuzumab exposure in JACOB was consistent with prior studies in advanced gastric cancer and breast cancer and appears to be an appropriate dose selection.
- Evidence snippets:
  - Snippet 1 (score: 0.547)
    > Tumor burden was ruled out as a potential mechanism in previously published popPK analyses [14]. Shed HER2 ECD was investigated within the JACOB study, as it was a significant covariate for the clearance of trastuzumab or ado-trastuzumab emtansine in MBC, although in these studies, the magnitude of impact was relatively small and not of clinical relevance [22,23]. In the JACOB study, baseline shed HER2 ECD levels were comparable to levels seen previously in breast cancer patients [F. Hoffmann-La Roche Ltd. Data on file] and there was no apparent relationship between baseline shed HER2 ECD and steady-state pertuzumab C min .
    > One promising non-target hypothesis is potential gastric protein leakage or protein-losing enteropathy (PLE) in patients with AGC. There is no direct clinical evidence for a relationship between PLE and the PK of mAbs; however, it is conceivable that PLE could be a driving factor in faster mAb clearance, given that GC is one of the disease states associated with PLE [24] and patients with PLE often develop hypoalbuminemia [25], which is known to be negatively correlated with mAb clearance [9,14,21,23]. Yang et al. [26] showed a decrease in murine IgG1 mAb area under the curve for 0-14 days from 1368 ± 255 to 594 ± 224 μg/mL/day in a murine model of colitis and PLE, providing preclinical support of this potential hypothesis.
    > Further studies are needed to identify first-line treatment options to improve patient outcomes in HER2-positive AGC and to better identify patients who might benefit from dual anti-HER2 targeted regimens [11]. Using methods beyond the current process for identifying HER2-positive AGC may compensate for the intratumoral heterogeneity observed in GC, which may have negatively impacted responses to targeted therapies in this and other trials [27,28].

### [5] SKiM-GPT: combining biomedical literature-based discovery with large language model hypothesis evaluation
- Authors: Jack Freeman, R. Millikin, Leo Xu, Ishaan Sharma, Bethany Moore et al.
- Year: 2025
- Venue: BMC Bioinformatics
- URL: https://www.semanticscholar.org/paper/ce7a6900a181708dba6ed2bf612d06b0be1d20b1
- DOI: 10.1186/s12859-025-06350-7
- PMID: 41408154
- PMCID: 12829140
- Summary: SKiM-GPT is introduced, a retrieval-augmented generation (RAG) system that combines SKiM’s co-occurrence search and retrieval with frontier LLMs to evaluate user- defined hypotheses, and achieves strong ordinal agreement with four expert biologists, demonstrating its ability to replicate expert judgment.
- Evidence snippets:
  - Snippet 1 (score: 0.542)
    > B Positive hypothesis condition. Without any provided abstracts ("No text"), when asked whether each drug "improves breast-cancer patient outcomes, " SKiM-GPT assigns positive scores (median = + 2), indicating that parametric (trained) memory is biased towards positive scores in these cases as expected ("parametric-knowledge leakage"). C Neutral hypothesis condition. Feeding synthetic abstracts that state no relationship exists between the drug and breast cancer patient outcomes increases scores for neutral hypotheses (median = + 2) for all drugs, indicating the model grounds its judgment in the supplied context rather than internal bias. D Negative hypothesis condition. Providing synthetic abstracts that refute drug efficacy results in increased scores for negative hypotheses (median = + 2). Together, panels B-D indicate that SKiM-GPT's scores mirror the sentiment of the abstracts rather than the LLM's training data SKiM-GPT correctly classified 19 of them, confirming 16 true drug-gene treatment links (positive scores) and correctly discarding three false positives (zero or negative scores). In the one case where SKiM-GPT was unable to correctly classify, the gene name SLN returned no relevant abstracts, as the abbreviation SLN can also stand for "sentinel lymph node" which is often a term associated with cancers.
    > Table 2. Assessment of SKiM-GPT's ability to remove false-positive hits in an LBD search. "Breast Cancer" was used as the A-term, a list of human genes as B-terms, and FDA-approved drugs as C-terms. The hypothesis "{C-term} treats {A-term} through its effect on {B-term}" was used to evaluate the top 20 hits ranked by p-value. For each SKiM A-B-C hit (column 1), SKiM-GPT scores the provided hypothesis from −2 (strongly refutes) to + 2 (strongly supports) after relevance filtering (column 2). Scores were classified as a true-positives (TP) or true-negatives (TN) based on current clinical or mechanistic evidence (column 3). The comments (column 4) contain context-specific notes written by human judges.

### [6] Immune cell profiles of metastatic HER2-positive breast cancer patients according to the sites of metastasis
- Authors: T. Honkanen, Milla E. K. Luukkainen, Antti Tikkanen, P. Karihtala, Markus J. Mäkinen et al.
- Year: 2021
- Venue: Breast Cancer Research and Treatment
- URL: https://www.semanticscholar.org/paper/f95f5f3008b0b18de39a4025a3d293e414e13fdc
- DOI: 10.1007/s10549-021-06447-6
- PMID: 34817749
- PMCID: 8763933
- Citations: 8
- Summary: The results suggest that the site of metastasis is associated with prognosis in HER2-positive breast cancer, highlighted by the poor prognosis of liver metastases.
- Evidence snippets:
  - Snippet 1 (score: 0.535)
    > Since immunology has a central role in HER2-positive breast cancer and targeted treatment acts through immunemediated mechanisms [5], we speculate that the presence of liver metastases would accordingly be associated with adverse prognosis and specific tumour immune profiles of the primary tumour.
    > In the current study, we tested this hypothesis by evaluating the prognosis and tumour immune cell profiles of 54 patients with metastatic HER2-positive breast cancer treated with trastuzumab containing regimens.

### [7] Nomogram to predict pathologic complete response in HER2-positive breast cancer treated with neoadjuvant systemic therapy
- Authors: T. Fujii, T. Kogawa, Jimin Wu, A. Sahin, Dian Liu et al.
- Year: 2017
- Venue: British Journal of Cancer
- URL: https://www.semanticscholar.org/paper/5dd1997db04466e24a85b0ce97b07fdd746e4ffa
- DOI: 10.1038/bjc.2016.444
- PMID: 28081544
- PMCID: 5318977
- Citations: 24
- Influential citations: 3
- Summary: A nomogram was built to predict the pCR rate after NST among patients with HER2-positive primary breast cancer using clinicopathologic factors and showed good agreement.
- Evidence snippets:
  - Snippet 1 (score: 0.534)
    > et al, 2013). Currently, we recommend the anti-HER2 doublet therapy of TmAb and pertuzumab as a treatment in neoadjuvant setting in HER2 þ breast cancer.
    > Sensitivity to systemic therapy is known to vary depending on hormone receptor (HR) status among patients with HER2-positive breast cancer. Previous studies reported that HR-positive tumours were less sensitive to combination systemic therapies. The pCR rate in patients with HR-positive and HER2-positive disease was 20%, compared with 36% in those with HR-negative disease (Gianni et al, 2012). Another study showed that HR-negative status significantly increased the duration of event-free survival in patients with HER2-positive disease (hazard ratio 0.46, 95% confidence interval (CI) 0.27-0.80), but HR-positive status did not affect event-free survival (hazard ratio 0.87, 95% CI 0.43-1.74) (Gianni et al, 2010). pCR rates after NST with regimens that include TmAb tend to be high in patients with HR-negative and HER2-positive breast cancer. However, the optimal way of predicting which patients in this group are most likely to achieve pCR after NST with regimens that include anti-HER2-targeted therapies is still unknown. In addition, oestrogen receptor (ER) expression is currently considered as a categorical variable in clinical settings; it is unclear whether ER expression level as a continuous variable is associated with pCR.
    > Recently, our group showed that a high HER2/CEP17 ratio is a predictor of high pCR rates among patients with HER2-positive locally advanced breast cancer who received NST that included TmAb (Kogawa et al, 2016). Given that HR status tends to predict pCR rates, considering ER expression (as a continuous variable) together with HER2/CEP17 ratio may provide a better prediction of pCR rates than either variable alone. We hypothesised that high HER2/CEP17 ratios and low ER expression levels are associated with high pCR rates in patients with HER2-positive breast cancer treated with NST. We constructed a nomogram to predict pCR rates in patients with primary

### [8] HER2 and ESR1 mRNA expression levels and response to neoadjuvant trastuzumab plus chemotherapy in patients with primary breast cancer
- Authors: C. Denkert, J. Huober, S. Loibl, J. Prinzler, R. Kronenwett et al.
- Year: 2013
- Venue: Breast Cancer Research : BCR
- URL: https://www.semanticscholar.org/paper/bbb3e4e5254ae4f1d7d01e34ceaa3294c787b51e
- DOI: 10.1186/bcr3384
- PMID: 23391338
- PMCID: 3672694
- Citations: 73
- Influential citations: 4
- Summary: This study investigated HER2 and ESR1 mRNA levels in core biopsies of HER2-positive breast carcinomas from patients treated within the neoadjuvant GeparQuattro trial and concluded only patients with cHER2- positive tumors - irrespective of the method used - have an increased pCR rate with trastuzumab plus chemotherapy.
- Evidence snippets:
  - Snippet 1 (score: 0.530)
    > HER2 mRNA levels were only significant in the group of ESR1positive tumors, similar to the subpopulation treatment effect pattern plot (STEPP) analysis. In contrast to the mRNA analysis, HER2 SISH ratio and copy number were not significant in centrally evaluated HER2-positive cases. ns, not signficant.
    > -negative tumors [40]. In our study 11 cases were negative for HER2 mRNA despite positivity by SISH, and those cases had a low pCR rate of only 27%. Furthermore seven tumors were mRNA-positive but SISHnegative with a pCR rate of 43%. Therefore, in our small cohort there is no evidence that patients with central IHC-positive results but negative HER2 mRNA have relevant benefit from trastuzumab with regard to pCR, which raises the hypothesis that HER2 mRNA might be more suitable for response prediction than SISH. We would like to emphasize that the low number of cases makes it impossible to fully evaluate this hypothesis in the context of our study, and that currently all indications for HER2-targeted therapies should be based on the established Food and Drug Administration (FDA) criteria.
    > The differences between HER2 mRNA and the classical methods of IHC and SISH might explain the finding that a different magnitude of benefit according to ER status has not been seen for trastuzumab in any of the adjuvant trastuzumab trials.
    > There are several limitations of our study; it was retrospective, the analysis could only be performed in a subpopulation, and we used only one pCR definition without separating the group of residual ductal carcinoma in-situ (DCIS). This separation was not possible in our cohort due to the smaller sample size. It should also be noted that some studies suggest that pCR might not be a reliable surrogate for long-term disease outcome in ER+/HER2+ disease [44]. The advantages of the study are that we used a population from a prospective clinical trial with a standardized assay system, as well as a predefined hypothesis and analysis plan.

### [9] Molecular imaging predicts lack of T-DM1 response in advanced HER2-positive breast cancer (final results of ZEPHIR trial)
- Authors: Magdalena Mileva, E. de Vries, T. Guiot, Z. Wimana, Anne-Leen Deleu et al.
- Year: 2024
- Venue: NPJ Breast Cancer
- URL: https://www.semanticscholar.org/paper/0ff3a54a786d12f7955bb2b72f2d31f507472ecf
- DOI: 10.1038/s41523-023-00610-6
- PMID: 38184611
- PMCID: 10771456
- Citations: 32
- Summary: Heterogeneity in HER2 expression generates interest in “whole-body” assessment of HER2 status using molecular imaging and HER2 PET/CT can successfully identify BC lesions and patients with a low probability of clinical benefit from T-DM1.
- Evidence snippets:
  - Snippet 1 (score: 0.527)
    > Our study prospectively evaluated PET imaging as a powerful tool for better treatment individualization and early prediction of T-DM1 response in patients with advanced HER2-positive breast cancer.Up to now, not a single predictive biomarker of T-DM1 efficacy in HER2-positive breast cancer has been identified: HER2 mRNA expression and mutations of the PiK 3 CA gene (encoding the p110α catalytic subunit of the phosphatidylinositol 3-kinase), for example, turned out to be "prognostic" but not "predictive" biomarkers in the advanced disease trials 16 .This is a limitation in the era of personalized oncology and also given the relatively high cost of the drug.
    > Being the first prospective and comprehensive imaging study in advanced HER2-positive breast cancer, we could not formulate a patient-oriented statistical hypothesis, which is why the primary endpoint of our study was a lesion-based analysis.In the complete patient cohort, a considerable number of lesions (39%) did not show sufficient target expression on HER2 PET/CT.Moreover, these lesions were less likely to respond anatomically after three cycles of T-DM1 than lesions showing high 89 Zr-trastuzumab uptake on PET imaging.Further investigation is required to understand why in 18 out of 93 HER2-negative lesions on HER2 PET/CT, an objective anatomic response was still observed after three cycles of T-DM1.Our study could not distinguish between a real lack of receptor overexpression, receptor masking 17,18 , or induced response in low HER2 availability due to a high potency of DM1 in the absence of intracellular resistance mechanisms.In "HER2-low" tumors (defined as an ICH score of 1+ or 2+ and negative results on FISH), a new generation of ADC, trastuzumab deruxtecan, prolongs progression-free survival and overall survival compared to the physician's choice of chemotherapy 19 .

### [10] Determination of HER2 status using both serum HER2 levels and circulating tumor cells in patients with recurrent breast cancer whose primary tumor was HER2 negative or of unknown HER2 status
- Authors: T. Fehm, S. Becker, S. Duerr-Stoerzer, K. Sotlar, V. Mueller et al.
- Year: 2007
- Venue: Breast cancer research : BCR
- URL: https://www.semanticscholar.org/paper/d978813f071eae7f40906131650b58285b8073bc
- DOI: 10.1186/bcr1783
- PMID: 17963511
- PMCID: 2242672
- Citations: 192
- Influential citations: 7
- Summary: A subgroup of patients with initially negative or unknown HER2 status can have elevated serum HER2 levels and/or HER2-positive CTCs at the time of development of metastatic disease.
- Evidence snippets:
  - Snippet 1 (score: 0.523)
    > the time of metastatic disease were observed by Anderson and coworkers (34%) [34] and Fehm and colleagues (34%) [35] using the serum test. Currently, such patients are not considered eligible for HER2-targeted therapy, but based on recent studies it is high likely that such individuals would respond to Herceptin [29].
    > The clinical significance of HER2 positive circulating tumor cells Tumors, including metastatic lesions, shed large numbers of tumor cells into the blood circulation [36], and the presence of CTCs is of biologic relevance in the metastatic setting. Based on the hypothesis that the phenotype of CTCs may reflect the phenotype of metastatic disease, characterization of CTCs may be useful for reassessment of HER2 status and additional therapeutic markers [20]. However, this option is limited to those patients with detectable CTCs. Reported positivity rates for CTCs in metastatic breast cancer patients range from 20% to 60% [37,38].
    > In our prospective study, in which 67 patients could be included, 21 patients had detectable CTCs (31%). HER2 was over-expressed in eight of these 21 patients (38%). Meng and coworkers [20] reassessed the HER2 status in 31 metastatic patients with CTCs. Nine out of 24 patients with initially HER2negative tumors had HER2-positive cells; this rate (38%) is lower than our observed positivity rate. Four of these nine patients were treated with a Herceptin-containing chemotherapy regimen. Two of these patients exhibited partial or complete remission [20].
    > Hayes and colleagues [39] evaluated the number of HER2positive CTCs during the course of treatment by flow cytometry in 19 metastatic breast cancer patients. During disease progression, the HER2 status of CTCs changed from negative to positive in all cases (n = 3). In contrast, patients responding to trastuzumab treatment lost their HER2-positive cell fraction. Meng and coworkers [40] analyzed the urokinase-type plasminogen activator receptor and HER2 gene status in individual breast cancer cells from metastatic breast cancer patients. Five out of 52 formerly HER2-

### [11] Shared genetics between breast cancer and predisposing diseases identifies novel breast cancer treatment candidates
- Authors: P. N. Lalagkas, R. Melamed
- Year: 2024
- Venue: Human Genomics
- URL: https://www.semanticscholar.org/paper/5ed48d880dca9568260615e67fcb2cbd68c1bb3a
- DOI: 10.1186/s40246-024-00688-4
- PMID: 39538313
- PMCID: 11562851
- Citations: 1
- Summary: This work exploits the genetics of breast cancer and linked predisposing diseases to propose novel drug repurposing opportunities and develops a method to not only prioritize drugs for repurposing, but also to highlight shared etiology explaining repurposing.
- Evidence snippets:
  - Snippet 1 (score: 0.520)
    > Health conditions including high cholesterol and type 2 diabetes incur increased risk for breast cancer. Previous genetics research has supported a biological explanation: these diseases, which we will refer to as predisposing diseases, share genetic variation with breast cancer. Building on this, we hypothesize that finding the shared genetics between breast cancer and its predisposing diseases can help us discover new drugs for breast cancer. Specifically, we hypothesize that drugs approved for a predisposing disease and targeting its shared biology with breast cancer can treat the latter disease (Fig. 1A).
    > To test this hypothesis, we first search the scientific literature (epidemiological and statistical genetic studies) for diseases with genetic variation known to predispose Fig. 1 Outline of the approach. A. Tested hypothesis that a drug treating a health condition known to increase the risk for breast cancer and targets the shared biology of both conditions may also treat breast cancer. B-E. Proposed workflow to identify the most likely shared genes between breast cancer and a predisposing disease and connect them to drugs approved for the predisposing disease individuals to breast cancer. We find six such diseases [30][31][32][33][34] (Table 1).
    > Next, we aim to identify the shared genetics between each pair of breast cancer and a predisposing disease and connect them to drugs approved for the predisposing disease. We first use publicly available GWAS summary statistics data (Table 1) and a local genetic correlation analysis, to find the shared genetics (Fig. 1B-D). Then, for each predisposing disease, we use a network biology method to link the shared genes to canonical pathways, and similarly for all drugs treating the predisposing disease, we link their targets to the pathways (Fig. 1E). By finding drugs that target shared pathways, we both prioritize candidate drugs for repurposing for breast cancer and provide biological insights that support their effect in disease treatment.
    > Finally, we evaluate our list of candidate drugs. To do so, we compile a list of 583 drugs either in clinical trials (N = 451) or approved (N = 132) for breast cancer and test for enrichment within our candidate drugs.

### [12] A diseasome cluster-based drug repurposing of soluble guanylate cyclase activators from smooth muscle relaxation to direct neuroprotection
- Authors: F. Langhauser, A. I. Casas, V. Dao, E. Guney, Jörg Menche et al.
- Year: 2018
- Venue: NPJ Systems Biology and Applications
- URL: https://www.semanticscholar.org/paper/44d6cd1d0dd2993b9a9f6b17e3f9705fb04892b8
- DOI: 10.1038/s41540-017-0039-7
- PMID: 29423274
- PMCID: 5799370
- Citations: 61
- Influential citations: 2
- Summary: It is shown that, based on this principle, a cardio-pulmonary drug can be surprisingly repurposed for a previously not recognised application as a direct neuroprotectant, and it is found that the cyclic GMP forming soluble guanylate cyclase becomes dysfunctional upon stroke but regains catalytic activity in the presence of specific activator compounds.
- Evidence snippets:
  - Snippet 1 (score: 0.519)
    > Drug discovery and development follows a relatively uniform path from mechanistic hypothesis, preclinical disease models to clinical validation. However, in recent years, a string of major drug developments have failed due to lack of efficacy. 1 One reason for this appears to reside in our current definitions of 'disease', i.e., mostly organ-based or by an apparent phenotype or symptom and not by an underlying mechanisms. However, without a validated pathomechanism no mechanism-based drugs can be developed and, therefore, rather surrogate parameters or risk factors are treated instead. Finding a rational approach towards mechanism-based disease definitions may therefore have a tremendous impact on drug discovery and medicine in general.
    > Using a data-driven approach, disease-disease networks (diseosome) have been constructed in which diseases are linked based on common molecular or regulatory mechanisms, 2 such as shared genetic associations, 2 protein interactions 3,4 or gene-disease interactions. 5 These diseasomes exhibit local clusters of diseases whose molecular relationships are well understood, but also unexpected clusters of surprisingly heterogeneous diseases. 3 Such clustering of disease phenotypes is likely due to underlying hidden common pathomechanisms. Importantly, these common mechanism clusters may provide previously unrecognized molecular definitions of these phenotypes and at the same time targets for mechanism-based drug discovery and repurposing.
    > Here we test the clinical validity of this approach by focusing on one cluster of highly prevalent combinations of vascular, neurological and metabolic disease phenotypes with high unmet medical need. Genetic evidence points to cGMP signaling as being part of its underlying pathomechanism. 5,6 We then inquire in a non-hypothesis-based manner using disease-disease networks based on common genetic origins, common protein interactions between disease genes, shared disease symptoms and disease co-morbidity for possible drug repurposing of cGMP modulators within this cluster.

### [13] Detection and HER2 Expression of Circulating Tumor Cells: Prospective Monitoring in Breast Cancer Patients Treated in the Neoadjuvant GeparQuattro Trial
- Authors: S. Riethdorf, V. Müller, Liling Zhang, T. Rau, S. Loibl et al.
- Year: 2010
- Venue: Clinical Cancer Research
- URL: https://www.semanticscholar.org/paper/e3e313d07b1e35bbcc2e79faa787d099a75d3ff3
- DOI: 10.1158/1078-0432.CCR-09-2042
- PMID: 20406831
- Citations: 488
- Influential citations: 20
- Summary: CTC number was low in patients with primary breast cancer and the decrease in CTC incidence during treatment was not correlated with standard clinical characteristics and primary tumor response, and there was no association between tumor response to NT and CTC detection.
- Evidence snippets:
  - Snippet 1 (score: 0.517)
    > hm et al. (54) on CTC at the time of metastatic disease in 21 patients with initially HER2-negative breast cancer that indicated HER2 overexpression in 8 of these cases (38.1%). These data support the conclusion that measurement of HER2 expression of CTC from patients with metastatic breast cancer will also help identify patients who might benefit from trastuzumab treatment.
    > One of our goals for future research will be to understand the biology of cells surviving trastuzumab treatment that are probably responsible for metastatic spread. Based on these results, it will be of great interest to design clinical trials to correlate clinical responses to HER2-targeted therapy based on HER2-positive CTC in adjuvant and metastatic breast cancer. Determining the HER2 expression of CTC will also be of relevance for study designs including new therapeutic approaches targeting HER2. The ongoing study GeparQuinto randomizes patients between trastuzumab and lapatinib, also targeting HER2, and additionally, epidermal growth factor receptor as NT; we are currently examining HER2 expression on CTC in these patients (http://www.germanbreastgroup.de/geparquinto). In the context of this trial, it should be possible to examine if trastuzumab and lapatinib treatment affect the kinetics and HER2 expression on CTC.
    > In summary, our findings support the hypothesis that detection and characterization of CTC could help to better understand the effect of NT on disseminating tumor cells, which may eventually lead to an improvement of current treatment strategies.

### [14] AK4 Promotes the Progression of HER2-Positive Breast Cancer by Facilitating Cell Proliferation and Invasion
- Authors: Jie Zhang, Yan-Tao Yin, Chi Wu, Ronglin Qiu, Wenli Jiang et al.
- Year: 2019
- Venue: Disease Markers
- URL: https://www.semanticscholar.org/paper/c51af8ad2760e81edb65d5bd78c40938244e28d1
- DOI: 10.1155/2019/8186091
- PMID: 31827645
- PMCID: 6886328
- Citations: 19
- Influential citations: 1
- Summary: It is mechanically confirmed that AK4 depletion showed the obvious impairment of cell proliferation and invasion in MCF7 and MDA-MB-231 cells and is a novel therapeutic target of HER2-positive breast cancer.
- Evidence snippets:
  - Snippet 1 (score: 0.516)
    > Through immunohistochemistry (IHC) assays, we found that AK4 was highly expressed in human HER2-positive breast cancer tissues and investigated the link between the expression levels of AK4 and clinical features of patients who underwent HER2-positive breast cancer. AK4 depletion also blocked the cell proliferation and invasion of HER2positive breast cancer both in vitro and in vivo. We therefore believe that AK4 could serve as a novel therapeutic target for the treatment of HER2-positive breast cancer.
    > HER2 is an important prognostic factor for breast cancer [22]. The development and metastasis of HER2-positive (overexpressed or amplified) breast cancer is different from other subtypes of breast cancer and is treated differently [23]. Recently, targeted therapy had good effects on this cancer [24,25]. Some targeted drugs, such as Herceptin and Lapatinib, specifically target the HER2 gene and have shown efficacy in early and late (metastatic) HER2-positive breast cancer [26,27]. Although HER2 is the driving gene of breast cancer, several genes are still involved in the progression of HER2-positive breast cancer. As potential therapeutic targets, it is necessary to develop relevant targeted drugs and participate in combined therapy to improve the prognosis of patients with HER2-positive breast cancer [28]. Interestingly, we found that AK4, as a member of the adenylate kinase family, was involved in the progression of HER2positive breast cancer. AK4 was highly expressed in tumor tissues. Additionally, it was correlated with the clinical features of patients. Therefore, AK4 could serve as a novel therapeutic target for the treatment of HER2-positive breast cancer.
    > From the analysis of 82 human HER2-positive breast cancer samples and the adjacent tissue samples through IHC assays, we found that AK4 was highly expressed in  Disease Markers tumor tissues. Additionally, AK4 expression was significantly correlated with clinical characteristics including pTNM stage and lymph node metastasis. These clinical analyses confirmed the potential effects of AK4 in the progression of HER2-positive breast cancer. Further investigations proved our hypothesis that AK4 could serve as a trigger of cancer progression through the regulation of cancer cell proliferation and invasion.

### [15] Dual- versus single-agent HER2 inhibition and incidence of intracranial metastatic disease: a systematic review and meta-analysis
- Authors: A. Erickson, S. Habbous, Christianne Hoey, K. Jerzak, Sunit Das
- Year: 2021
- Venue: NPJ Breast Cancer
- URL: https://www.semanticscholar.org/paper/6781ca0c03e097d469bae59ccc225f2a5e25ed6f
- DOI: 10.1038/s41523-021-00220-0
- PMID: 33602948
- PMCID: 7892568
- Citations: 3
- Summary: The hypothesis that prolonged survival afforded by improved extracranial disease control is associated with increased IMD incidence is challenged, and dual HER2-targeted therapy was associated with improved overall survival and progression-free survival.
- Evidence snippets:
  - Snippet 1 (score: 0.515)
    > Observational studies have suggested that HER2 inhibition with trastuzumab may be associated with an increased incidence of intracranial metastatic disease (IMD) due to its ability to prolong survival. We hypothesized that prolonged survival associated with dual-agent HER2 inhibition may be associated with an even higher incidence of IMD. This study pooled estimates of IMD incidence and survival among patients with HER2-positive breast cancer receiving dual- versus single-agent HER2 targeted therapy, as well as trastuzumab versus chemotherapy, observation, or another HER2-targeted agent. We searched PubMed, EMBASE, and CENTRAL from inception to 25 March 2020. We included randomized controlled trials that reported IMD incidence for patients with HER2-positive breast cancer receiving trastuzumab as the experimental or control arm irrespective of disease stage. Among 465 records identified, 19 randomized controlled trials (32,572 patients) were included. Meta-analysis of four studies showed that dual HER2-targeted therapy was associated with improved overall survival (HR 0.76; 95% CI, 0.66–0.87) and progression-free survival (HR 0.77; 95% CI, 0.68–0.87) compared to single HER2-targeted therapy, but the risk of IMD was similar (RR 1.03; 95% CI, 0.83–1.27). Our study challenges the hypothesis that prolonged survival afforded by improved extracranial disease control is associated with increased IMD incidence.

### [16] Dual- versus single-agent HER2 inhibition and incidence of intracranial metastatic disease: a systematic review and meta-analysis
- Authors: A. Erickson, S. Habbous, Christianne Hoey, K. Jerzak, Sunit Das
- Year: 2021
- Venue: npj Breast Cancer
- URL: https://www.semanticscholar.org/paper/bb2940449df9cf69f1f5aab07fd1e518029d8a8d
- DOI: 10.1038/s41523-021-00220-0
- Summary: The hypothesis that prolonged survival afforded by improved extracranial disease control is associated with increased IMD incidence is challenged, and dual HER2-targeted therapy was associated with improved overall survival and progression-free survival.
- Evidence snippets:
  - Snippet 1 (score: 0.515)
    > Observational studies have suggested that HER2 inhibition with trastuzumab may be associated with an increased incidence of intracranial metastatic disease (IMD) due to its ability to prolong survival. We hypothesized that prolonged survival associated with dual-agent HER2 inhibition may be associated with an even higher incidence of IMD. This study pooled estimates of IMD incidence and survival among patients with HER2-positive breast cancer receiving dual- versus single-agent HER2 targeted therapy, as well as trastuzumab versus chemotherapy, observation, or another HER2-targeted agent. We searched PubMed, EMBASE, and CENTRAL from inception to 25 March 2020. We included randomized controlled trials that reported IMD incidence for patients with HER2-positive breast cancer receiving trastuzumab as the experimental or control arm irrespective of disease stage. Among 465 records identified, 19 randomized controlled trials (32,572 patients) were included. Meta-analysis of four studies showed that dual HER2-targeted therapy was associated with improved overall survival (HR 0.76; 95% CI, 0.66–0.87) and progression-free survival (HR 0.77; 95% CI, 0.68–0.87) compared to single HER2-targeted therapy, but the risk of IMD was similar (RR 1.03; 95% CI, 0.83–1.27). Our study challenges the hypothesis that prolonged survival afforded by improved extracranial disease control is associated with increased IMD incidence.

### [17] DiseaseConnect: a comprehensive web server for mechanism-based disease–disease connections
- Authors: Chun-Chi Liu, Y. Tseng, Wenyuan Li, Chia-Yu Wu, I. Mayzus et al.
- Year: 2014
- Venue: Nucleic Acids Research
- URL: https://www.semanticscholar.org/paper/164eec8e3e9af7dd3b1182e46be7577b90d44e1b
- DOI: 10.1093/nar/gku412
- PMID: 24895436
- PMCID: 4086092
- Citations: 100
- Influential citations: 6
- Summary: The DiseaseConnect is a web server for analysis and visualization of a comprehensive knowledge on mechanism-based disease connectivity that integrates comprehensive omics and literature data, including a large amount of gene expression data, Genome-Wide Association Studies catalog, and text-mined knowledge, to discover disease–disease connectivity via common molecular mechanisms.
- Evidence snippets:
  - Snippet 1 (score: 0.513)
    > After viewing all diseases and molecules related to a query disease, users can further explore the shared molecular mechanism(s) between two specific diseases by clicking an edge in the disease network. For example, when a user queries MM, the web server generates a disease-disease network. The user can then click the connection between MM and hemorrhagic disorders (HD) to view a network of shared genes and drugs between HD and MM. Figure 6A shows a small part of this network with the shared gene PSMB5 and the drug bortezomib. PSMB5 is a DEG for both HD and MM, and also has a GeneRIF association with MM. Bortezomib is a therapeutic proteasome inhibitor for treating MM, and targets PSMB5 (39). Interestingly, bortezomib can also treat HD (40), suggesting that shared disease genes can serve as good targets for drug repositioning strategies. Figure 6B shows another example network for the queried disease pair 'arthritis' and 'Crohn disease', both involve the tumor necrosis factor (TNF), based on the data sources GWAS and GeneRIF. Thalidomide is an immunomodulatory drug that targets TNF. Interestingly, thalidomide can treat both arthritis and Crohn diseases (41), supporting our hypothesis that diseases with a shared molecular mechanism are likely to be treated by the same drug. Another drug shown in Figure 6B, 'adalimumab', is known to target TNF and can treat arthritis, suggesting that it may also be effective for Crohn disease. In fact, this inference is confirmed independently by a recent report of Peters et al. (42). Also, several clinical trials about Adalimumab and Crohn disease (e.g. ClinicalTrials.gov ID: NCT01556672 and NCT01958827) are currently ongoing.

### [18] Trastuzumab and first-line taxane chemotherapy in metastatic breast cancer patients with a HER2-negative tumor and HER2-positive circulating tumor cells: a phase II trial
- Authors: Noortje Verschoor, M. Bos, I. D. de Kruijff, M. Van, J. Kraan et al.
- Year: 2024
- Venue: Breast Cancer Research and Treatment
- URL: https://www.semanticscholar.org/paper/27666f62e949ba4071df10978655085b62820f45
- DOI: 10.1007/s10549-023-07231-4
- PMID: 38291268
- PMCID: 11062986
- Citations: 4
- Summary: It is argued that randomized studies investigating agents that are proven to be solely effective in the HER2-positive patient group in patients with HER2-positive CTCs and HER2-negative tissue are currently infeasible.
- Evidence snippets:
  - Snippet 1 (score: 0.511)
    > With the introduction of anti-HER2 targeted therapy, the clinical outcome of patients with HER2-positive breast cancer has greatly improved. HER2-positive disease is defined by receptor overexpression, caused by amplification of the ERBB2 gene. According to current guidelines, HER2-status is determined by semi-quantitative determination of overexpression by immunohistochemistry, complemented by in situ hybridization if necessary [1]. HER2-positivity is an inherently aggressive trait and is present in 10-15% of all primary invasive breast cancers. Heterogeneity between lesions has been described when the disease advances to the metastatic state, with conversion from HER2-negative to HER2-positive state in up to 10% [2][3][4]. Retrospective research suggests that patients with discordant HER2receptor status between the primary and metastatic lesion derive benefit from HER2-targeting treatment, although this has to be confirmed in larger series [5]. The current guidelines for metastatic breast cancer recommend tissue re-evaluation prior to initiating a new line of systemic treatment if possible, and to treat patients with targeted therapy if HER2-is positive in at least one biopsy [6]. It is however not always feasible to biopsy metastatic lesions to re-evaluate HER2-status. Non-invasive evaluation of the HER2-status on circulating tumor cells (CTCs) is proposed as a possible solution. The general hypothesis is that CTCs detach from all tumor lesions and therefore provide a better reflection of receptor status of all metastatic lesions [7]. However, CTCs are rare events, which are detected against a vast background of lymphocytes, which complicates evaluation of genomic markers at a single cell level. Riethdorf et al. therefore proposed an immunostaining method to evaluate HER2-expression on CTCs, that can be combined with the FDA-approved CellSearch method, the current gold standard to retrieve CTCs, due to its proven clinical validity [8,9].

## Notes

- This provider combines `search_papers_by_relevance` with `snippet_search`.
- No synthesis or second-stage model call is performed.
