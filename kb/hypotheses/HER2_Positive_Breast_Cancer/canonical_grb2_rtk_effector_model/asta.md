---
provider: asta
model: Asta Scientific Corpus Retrieval
cached: false
start_time: '2026-05-26T23:12:22.164893'
end_time: '2026-05-26T23:12:26.883498'
duration_seconds: 4.72
template_file: templates/hypothesis_deep_research.md
template_variables:
  disease_name: HER2-Positive Breast Cancer
  category: ''
  hypothesis_group_id: canonical_grb2_rtk_effector_model
  hypothesis_label: Canonical HER2-GRB2 RTK Effector Model
  hypothesis_status: CANONICAL
  hypothesis_yaml: "hypothesis_group_id: canonical_grb2_rtk_effector_model\nhypothesis_label:\
    \ Canonical HER2-GRB2 RTK Effector Model\nstatus: CANONICAL\ndescription: Constitutively\
    \ activated HER2 receptors create phosphotyrosine docking sites that recruit\n\
    \  GRB2 adaptor complexes, coupling receptor activation to canonical RAS-MAPK\
    \ and PI3K-AKT proliferative\n  signaling. This is the textbook HER2+ breast cancer\
    \ signaling cascade and the explicit disease-level\n  instantiation of the rtk_grb2_signaling_adaptation\
    \ module's canonical effector hypothesis.\nevidence:\n- reference: PMID:28058850\n\
    \  supports: SUPPORT\n  evidence_source: OTHER\n  snippet: Signaling by FGFR4\
    \ and other fibroblast growth factor receptors involves tyrosine phosphorylation\n\
    \    of the receptor carboxyl terminus along with other substrates, such as FRS2,\
    \ recruitment of the GRB2\n    adaptor, and activation of the downstream RAS and\
    \ phosphoinositide 3-kinase pathways.\n  explanation: Review evidence supports\
    \ the canonical RTK-to-GRB2-to-RAS/PI3K architecture that HER2+\n    breast cancer\
    \ instantiates."
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
- **Hypothesis ID:** canonical_grb2_rtk_effector_model
- **Hypothesis Label:** Canonical HER2-GRB2 RTK Effector Model
- **Status in KB:** CANONICAL

## Seed Hypothesis YAML

```yaml
hypothesis_group_id: canonical_grb2_rtk_effector_model
hypothesis_label: Canonical HER2-GRB2 RTK Effector Model
status: CANONICAL
description: Constitutively activated HER2 receptors create phosphotyrosine docking sites that recruit
  GRB2 adaptor complexes, coupling receptor activation to canonical RAS-MAPK and PI3K-AKT proliferative
  signaling. This is the textbook HER2+ breast cancer signaling cascade and the explicit disease-level
  instantiation of the rtk_grb2_signaling_adaptation module's canonical effector hypothesis.
evidence:
- reference: PMID:28058850
  supports: SUPPORT
  evidence_source: OTHER
  snippet: Signaling by FGFR4 and other fibroblast growth factor receptors involves tyrosine phosphorylation
    of the receptor carboxyl terminus along with other substrates, such as FRS2, recruitment of the GRB2
    adaptor, and activation of the downstream RAS and phosphoinositide 3-kinase pathways.
  explanation: Review evidence supports the canonical RTK-to-GRB2-to-RAS/PI3K architecture that HER2+
    breast cancer instantiates.
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
  - Snippet 1 (score: 0.577)
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
  - Snippet 2 (score: 0.518)
    > Although ACE-inhibitors have proved beneficial for hypertension in many study populations, there remains the question of whether they are the optimal treatment in some distinct target population, such as African or Caribbean populations. In this case, it is necessary to determine the status of the following general mechanistic claim: the relevant hypertensive mechanisms in the study populations are sufficiently similar to the mechanisms in African or Caribbean populations. This general mechanistic claim can be evaluated by evaluating a more specific mechanism hypothesis, namely that African and Caribbean populations have a lower renin state. As we shall see in Chap. 6, there is some good mechanistic evidence in favour of this specific mechanism hypothesis, and this undermines the general mechanistic claim. This is why, instead, calcium channel blockers are the recommended antihypertensive treatment in African and Caribbean populations (Clarke et al. 2014).
    > There are two main ways to identify a specific mechanism hypothesis. First, a specific mechanism hypothesis may be proposed on the basis of published studies from the clinical study literature. If a clinical study establishes a correlation between a putative cause and effect, and the suggestion is that this correlation is causal, then the authors of such a study usually identify at least one possible mechanism hypothesis of the following form: It is plausible that mechanism with features F links the putative cause and effect in the study population. The study may also point out possible masking mechanisms (Illari 2011). Given this, the discussion section of a published paper that reports the results of a clinical study is a good place to look in order to locate a specific mechanism hypothesis.
  - Snippet 3 (score: 0.512)
    > The overall approach to gathering evidence of mechanisms of action. Each proposed mechanism of action, or partial description of proposed mechanism of action, is a specific mechanism hypothesis. But note that a specific mechanism hypothesis need not be a complete description of a mechanism.
    > Example: Specific mechanism hypotheses for determining efficacy.
    > Aspirin prevents heart disease via cyclooxygenase (COX) inhibition, and the mechanisms that underlie this prevention are established. However, aspirin also seems to reduce the incidence of some cancers. Here, the mechanisms are much less well understood. As Chan et al. (2011) write: "the mechanism of aspirin's antineoplastic effect is less clear, with substantial evidence supporting both COX-dependent and COX-independent mechanisms. Moreover, data supporting the importance of COX-dependent mechanisms are not entirely consistent concerning the relative importance of the COX-1 and COX-2 isoforms in carcinogenesis". In this quotation, the general mechanistic claim is that aspirin exhibits an antineoplastic effect. There are also a couple of more specific mechanism hypotheses, for example, that this antineoplastic effect is mediated by COX-dependent mechanisms. Evidence relating to these more specific mechanism hypotheses provides a way to determine the status of the general mechanistic claim.
    > External validity. In order to evaluate the general mechanistic claim that there is a mechanism in the target population sufficiently similar to the mechanism responsible for the correlation observed in the study population, specific mechanism hypotheses need to pertain to the mechanism of action. It is important to consider the possibility that the mechanism in the target population may contain further component mechanisms that counteract the mechanism of action in the study population and affect the extent of the correlation between the putative cause and effect. So one needs to ask, are there any masking mechanisms in the target population?
    > Example: Specific mechanism hypotheses for determining external validity.
    > According to NICE guidelines, treatment for hypertension should differ depending on ethnicity (NICE 2011). Although ACE-inhibitors have proved beneficial for hypertension in many study populations, there remains the question of whether they are the optimal treatment in some distinct target population, such as African or Caribbean populations.

### [2] The Rise of Hypothesis-Driven Artificial Intelligence in Oncology
- Authors: Zilin Xianyu, Cristina Correia, C. Ung, Shizhen Zhu, D. Billadeau et al.
- Year: 2024
- Venue: Cancers
- URL: https://www.semanticscholar.org/paper/f05721d59597ea5471ac85617fda99b4e73fb936
- DOI: 10.3390/cancers16040822
- PMID: 38398213
- PMCID: 10886811
- Citations: 17
- Summary: Hobbit-driven AI holds great promise in the discovery of new mechanistic and functional insights that explain the complexity of cancer etiology and potentially chart a new roadmap to improve treatment regimens for individual patients.
- Evidence snippets:
  - Snippet 1 (score: 0.526)
    > Despite their wide area of application in cancer research, hypothesis-driven AI tools show several areas for improvement. While some models such as OncoNPC have shown efficacy, there is a need to generalize these models across different patient populations and cancer types. However, since these models were developed based on disease-specific domain knowledge, this might inadvertently limit their utility in other disease contexts. Utilizing domain knowledge agnostic to a specific disease type while retaining the flexibility to adapt to a specific biological context can enhance the generalizability of a hypothesis-driven AI tool to broader disease types. Moreover, as the structure and dimensionality of data become more complex by including distinct biological layers such as genetics and environmental, researchers face greater challenges in formulating hypotheses that can effectively manage different levels of data attributes, and this demands further abstract reasoning from researchers. Additionally, the selection of which knowledge domain to integrate into algorithmic design remains subjective and varies among researchers.
    > Figure 4 summarizes the new ingredients needed for designing hypothesis-driven AI algorithms and illustrates how these can be utilized to unearth hidden gems embedded within the data to help better inform clinical decisions. Below we provide some open questions and food for thought that we think could inspire the development of hypothesisdriven AI in the near future.

### [3] Identification of Biomarkers for Breast Cancer Using Databases
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
  - Snippet 1 (score: 0.526)
    > GEO dataset is used to identify biomarkers in specific drugs-resistance breast cancer. One of these is Lapatinib, a dual tyrosine kinase inhibitor that interferes with epidermal growth factor receptor and HER2/neu pathways by treating HER2-positive breast cancer. A study presented a novel strategy for researching the mechanism of laptinib-resistance breast cancers. 31 The oncogenic isoform of HER2, HER2∆16, is expressed with HER2 in nearly 50% of HER2 positive breast tumors, and HER2∆16 drives metastasis and resistance to drugs including tamoxifen and trastuzumab. 32 ][35][36] GEO database contributed to development of technologies and provided information on specific disease characteristics. The aim is enhancing, indexing, linking, searching and displaying capacity in order to permit more data mining. 37 The search engine enlarges the data and it can lead to understanding of unidentified relationships between variety of data types, facilitating novel hypothesis generation, or assisting in the analysis of available information.

### [4] Cross-Resistance Among Sequential Cancer Therapeutics: An Emerging Issue
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
  - Snippet 1 (score: 0.517)
    > The loss of target on HER2-targeted therapy is a widely recognized issue that has been discussed above for both BC (36)(37)(38)(39)(40)(41)(42)(43)(44)(45)(46)(47) and GC (60)(61)(62). Provided that the knowledge of the underlying mechanisms is of paramount relevance, this evidence offers the opportunity to reconsider the strategies behind the design of RCTs. Indeed, many of these studies investigate the efficacy of new therapeutic approaches in metastatic/recurring patients stratified based on the molecular features of primary tumors. Interpreting the results generated from these trials could lead to sub-optimal clinical decision-making.
    > An emblematic example of this is the failure of the randomized phase II study WJOG7112G (T-ACT). The aim of the study was to explore the efficacy of paclitaxel with or without trastuzumab in 99 patients with HER2+ advanced GC who had disease progression after first-line chemotherapy with trastuzumab. Median PFS and OS were not significantly different between the two groups. In this case, loss of HER2 has been reported as a possible explanation for failure. Indeed, when HER2 status was re-evaluated in tumor biopsy specimens from 16 patients following disease progression, HER2 loss was observed in 11 patients (69%) (161).
    > In the specific case of HER2-targeted therapy, re-evaluating the HER2 status at the time of disease progression would be required (43). Supporting this, an ongoing phase II, open-label, single arm trial aimed at evaluating the efficacy and safety of T-Dxd in Western GC patients progressed with a trastuzumabcontaining regimen (DESTINY-Gastric02, NCT04014075) required patients to be re-tested for HER2 positivity before being treated with T-Dxd.
    > The Darwinian selection hypothesis assumes that cancer therapy selects pre-existing mutant cells that overtake the bulk cell population. However, this is a simplified mechanism that does not account for therapy resistance alone. In a more complicated scenario, genetic alterations and changes in the gene expression state often emerge under the selective pressure exerted

### [5] A diseasome cluster-based drug repurposing of soluble guanylate cyclase activators from smooth muscle relaxation to direct neuroprotection
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
  - Snippet 1 (score: 0.507)
    > Drug discovery and development follows a relatively uniform path from mechanistic hypothesis, preclinical disease models to clinical validation. However, in recent years, a string of major drug developments have failed due to lack of efficacy. 1 One reason for this appears to reside in our current definitions of 'disease', i.e., mostly organ-based or by an apparent phenotype or symptom and not by an underlying mechanisms. However, without a validated pathomechanism no mechanism-based drugs can be developed and, therefore, rather surrogate parameters or risk factors are treated instead. Finding a rational approach towards mechanism-based disease definitions may therefore have a tremendous impact on drug discovery and medicine in general.
    > Using a data-driven approach, disease-disease networks (diseosome) have been constructed in which diseases are linked based on common molecular or regulatory mechanisms, 2 such as shared genetic associations, 2 protein interactions 3,4 or gene-disease interactions. 5 These diseasomes exhibit local clusters of diseases whose molecular relationships are well understood, but also unexpected clusters of surprisingly heterogeneous diseases. 3 Such clustering of disease phenotypes is likely due to underlying hidden common pathomechanisms. Importantly, these common mechanism clusters may provide previously unrecognized molecular definitions of these phenotypes and at the same time targets for mechanism-based drug discovery and repurposing.
    > Here we test the clinical validity of this approach by focusing on one cluster of highly prevalent combinations of vascular, neurological and metabolic disease phenotypes with high unmet medical need. Genetic evidence points to cGMP signaling as being part of its underlying pathomechanism. 5,6 We then inquire in a non-hypothesis-based manner using disease-disease networks based on common genetic origins, common protein interactions between disease genes, shared disease symptoms and disease co-morbidity for possible drug repurposing of cGMP modulators within this cluster.

### [6] SKiM-GPT: combining biomedical literature-based discovery with large language model hypothesis evaluation
- Authors: Jack Freeman, R. Millikin, Leo Xu, Ishaan Sharma, Bethany Moore et al.
- Year: 2025
- Venue: BMC Bioinformatics
- URL: https://www.semanticscholar.org/paper/ce7a6900a181708dba6ed2bf612d06b0be1d20b1
- DOI: 10.1186/s12859-025-06350-7
- PMID: 41408154
- PMCID: 12829140
- Summary: SKiM-GPT is introduced, a retrieval-augmented generation (RAG) system that combines SKiM’s co-occurrence search and retrieval with frontier LLMs to evaluate user- defined hypotheses, and achieves strong ordinal agreement with four expert biologists, demonstrating its ability to replicate expert judgment.
- Evidence snippets:
  - Snippet 1 (score: 0.506)
    > B Positive hypothesis condition. Without any provided abstracts ("No text"), when asked whether each drug "improves breast-cancer patient outcomes, " SKiM-GPT assigns positive scores (median = + 2), indicating that parametric (trained) memory is biased towards positive scores in these cases as expected ("parametric-knowledge leakage"). C Neutral hypothesis condition. Feeding synthetic abstracts that state no relationship exists between the drug and breast cancer patient outcomes increases scores for neutral hypotheses (median = + 2) for all drugs, indicating the model grounds its judgment in the supplied context rather than internal bias. D Negative hypothesis condition. Providing synthetic abstracts that refute drug efficacy results in increased scores for negative hypotheses (median = + 2). Together, panels B-D indicate that SKiM-GPT's scores mirror the sentiment of the abstracts rather than the LLM's training data SKiM-GPT correctly classified 19 of them, confirming 16 true drug-gene treatment links (positive scores) and correctly discarding three false positives (zero or negative scores). In the one case where SKiM-GPT was unable to correctly classify, the gene name SLN returned no relevant abstracts, as the abbreviation SLN can also stand for "sentinel lymph node" which is often a term associated with cancers.
    > Table 2. Assessment of SKiM-GPT's ability to remove false-positive hits in an LBD search. "Breast Cancer" was used as the A-term, a list of human genes as B-terms, and FDA-approved drugs as C-terms. The hypothesis "{C-term} treats {A-term} through its effect on {B-term}" was used to evaluate the top 20 hits ranked by p-value. For each SKiM A-B-C hit (column 1), SKiM-GPT scores the provided hypothesis from −2 (strongly refutes) to + 2 (strongly supports) after relevance filtering (column 2). Scores were classified as a true-positives (TP) or true-negatives (TN) based on current clinical or mechanistic evidence (column 3). The comments (column 4) contain context-specific notes written by human judges.

### [7] Shared genetics between breast cancer and predisposing diseases identifies novel breast cancer treatment candidates
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
  - Snippet 1 (score: 0.500)
    > Health conditions including high cholesterol and type 2 diabetes incur increased risk for breast cancer. Previous genetics research has supported a biological explanation: these diseases, which we will refer to as predisposing diseases, share genetic variation with breast cancer. Building on this, we hypothesize that finding the shared genetics between breast cancer and its predisposing diseases can help us discover new drugs for breast cancer. Specifically, we hypothesize that drugs approved for a predisposing disease and targeting its shared biology with breast cancer can treat the latter disease (Fig. 1A).
    > To test this hypothesis, we first search the scientific literature (epidemiological and statistical genetic studies) for diseases with genetic variation known to predispose Fig. 1 Outline of the approach. A. Tested hypothesis that a drug treating a health condition known to increase the risk for breast cancer and targets the shared biology of both conditions may also treat breast cancer. B-E. Proposed workflow to identify the most likely shared genes between breast cancer and a predisposing disease and connect them to drugs approved for the predisposing disease individuals to breast cancer. We find six such diseases [30][31][32][33][34] (Table 1).
    > Next, we aim to identify the shared genetics between each pair of breast cancer and a predisposing disease and connect them to drugs approved for the predisposing disease. We first use publicly available GWAS summary statistics data (Table 1) and a local genetic correlation analysis, to find the shared genetics (Fig. 1B-D). Then, for each predisposing disease, we use a network biology method to link the shared genes to canonical pathways, and similarly for all drugs treating the predisposing disease, we link their targets to the pathways (Fig. 1E). By finding drugs that target shared pathways, we both prioritize candidate drugs for repurposing for breast cancer and provide biological insights that support their effect in disease treatment.
    > Finally, we evaluate our list of candidate drugs. To do so, we compile a list of 583 drugs either in clinical trials (N = 451) or approved (N = 132) for breast cancer and test for enrichment within our candidate drugs.

### [8] Discovery and analysis of consistent active sub-networks in cancers
- Authors: R. Gaire, Lorey K. Smith, P. Humbert, James Bailey, Peter James Stuckey et al.
- Year: 2013
- Venue: BMC Bioinformatics
- URL: https://www.semanticscholar.org/paper/1ba07521863c145402c23fba5ba4c92e5905e58b
- DOI: 10.1186/1471-2105-14-S2-S7
- PMID: 23368093
- PMCID: 3549822
- Citations: 15
- Summary: Comparison of the basal subtype of breast cancer and the mesenchymal subtype of glioblastoma ASNs shows that an ASN in the vicinity of IL 6 is conserved across the two subtypes, suggesting that subtypes of different cancers can show molecular similarities indicating that the therapeutic approaches in different types of cancers may be shared.
- Evidence snippets:
  - Snippet 1 (score: 0.496)
    > The full genome sequencing of cancer cases demonstrates how remarkably heterogeneous cancer cases are [1]. This heterogeneity is consistent with the hypothesis that most mutations are innocent bystander consequences of the failure of cancer cells' intrinsic mechanism to repair and guard the integrity of the genome [2]. However, the observed heterogeneity of the cancer mutations combined with the knowledge of multiple lesions that all could lead to the same phenotypic consequence [3], leads to a new emerging hypothesis. According to this competing hypothesis, intrinsic subtype specific cancer causing mutations are rare, but their biological output is common [4].
    > The recognition that cancer stem cells within a tumour mass uniquely carry the potential for overt malignancy [5,6] and the discovery that these cells can be transformed into and change forms between epithelial or mesenchymal cells, a phenomena known as epithelial-mesenchymal transformation (EMT) [7], has increased our insight into the link between EMT and fatal cancer phenotypes, such as metastasis and resistance to treatments. In addition, the discovery of intrinsic subtypes of breast cancer that express unique groups of genes [8] has advanced its prognosis. Some intrinsic subtypes of breast cancer are associated with elevated susceptibility to specific drugs, such as Herceptin (for amplified HER2 cases) and Tamoxifen (for ER+ cases), while other subtypes, such as the mesenchymal basal/triple negative cases remain without a matching therapeutic strategy. Being able to compare subtypes of different cancers may help identify genes causing the specific subtypes of cancers, leading to identify better therapeutic targets. More importantly, this could provide a scientific basis to sharing therapeutic strategies in subtypes of different cancers.
    > The task of interpreting gene expression profiles in a disease is not only to differentiate the non-random changes from the random and irrelevant changes, but also to identify the disease causing changes, their downstream effects and the cellular responses related to the disease. If such a procedure worked, one would expect to see the intrinsic signature of luminal breast cancer subtype emerging as downstream to gene ER. Furthermore, one could identify driver mutations of the mesenchymal/ basal subtype for which therapeutic strategies

### [9] The next-generation Open Targets Platform: reimagined, redesigned, rebuilt
- Authors: D. Ochoa, Andrew Hercules, M. Carmona, D. Suveges, Jarrod Baker et al.
- Year: 2022
- Venue: Nucleic Acids Research
- URL: https://www.semanticscholar.org/paper/1eb72ef89e6b7722e114e195f68cd45c86e6f344
- DOI: 10.1093/nar/gkac1046
- PMID: 36399499
- PMCID: 9825572
- Citations: 321
- Influential citations: 29
- Summary: The Open Targets Platform has reimagined, redesigned, and rebuilt in order to streamline data integration and harmonisation, expand the ways in which users can explore the data, and improve the user experience.
- Evidence snippets:
  - Snippet 1 (score: 0.493)
    > The Open Targets consortium brings together expertise and capabilities from academic and pharmaceutical industry partners with the vision to systematically identify targets that will ultimately lead to more effective and safer drugs for disease treatment. To facilitate therapeutic hypothesis building, the consortium experimentally generates novel evidence and contextualises it with available knowledge in the public domain. In this task, genetics provides an unprecedented source of causal evidence, to the extent that two-D1354 Nucleic Acids Research, 2023, Vol. 51, Database issue thirds of the drugs approved in 2021 were directly or indirectly supported by genetic evidence (1)(2)(3).
    > The Open Targets Platform (https://platform. opentargets.org/) provides an open source informatic solution for the identification and prioritisation of targets using publicly available data (4). The Platform provides the necessary knowledgebase to characterise targets, diseases and drugs in the context of drug discovery, as well as the relationships between the entities, with particular focus on target-disease associations (Figure 1). Powered with an in-house target identification scoring framework, evidence is aggregated across sources to provide ranked lists of gene-disease associations. To maintain up-todate-evidence, ensure regular updates from external data sources and integrate user feedback and new features, the Platform is released five times a year.
    > Within the last 2 years, the Platform has been widely used by the community as a source of truth in various contexts, including; supporting Crohn's disease associations or approved kinase inhibitors, as a prioritisation tool in the search for drug repurposing opportunities, or more generally as a data source to build corporate knowledge graphs to assist drug development (5)(6)(7). Moreover, our open-source code has been re-used by the NIH National Cancer Institute Childhood Cancer Data Initiative to develop and launch a customised Molecular Targets Platform that integrates patient-specific data, aiming to facilitate therapeutic hypotheses building and target discovery in paediatric cancer (https://moleculartargets.ccdi.cancer.gov/). This is just the first example of the many potential applications of the Platform open-source code to create separate instances in order to integrate experimental or pre-publication results.

### [10] Pharmacokinetic and exposure–response analysis of pertuzumab in patients with HER2-positive metastatic gastric or gastroesophageal junction cancer
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
  - Snippet 1 (score: 0.493)
    > Tumor burden was ruled out as a potential mechanism in previously published popPK analyses [14]. Shed HER2 ECD was investigated within the JACOB study, as it was a significant covariate for the clearance of trastuzumab or ado-trastuzumab emtansine in MBC, although in these studies, the magnitude of impact was relatively small and not of clinical relevance [22,23]. In the JACOB study, baseline shed HER2 ECD levels were comparable to levels seen previously in breast cancer patients [F. Hoffmann-La Roche Ltd. Data on file] and there was no apparent relationship between baseline shed HER2 ECD and steady-state pertuzumab C min .
    > One promising non-target hypothesis is potential gastric protein leakage or protein-losing enteropathy (PLE) in patients with AGC. There is no direct clinical evidence for a relationship between PLE and the PK of mAbs; however, it is conceivable that PLE could be a driving factor in faster mAb clearance, given that GC is one of the disease states associated with PLE [24] and patients with PLE often develop hypoalbuminemia [25], which is known to be negatively correlated with mAb clearance [9,14,21,23]. Yang et al. [26] showed a decrease in murine IgG1 mAb area under the curve for 0-14 days from 1368 ± 255 to 594 ± 224 μg/mL/day in a murine model of colitis and PLE, providing preclinical support of this potential hypothesis.
    > Further studies are needed to identify first-line treatment options to improve patient outcomes in HER2-positive AGC and to better identify patients who might benefit from dual anti-HER2 targeted regimens [11]. Using methods beyond the current process for identifying HER2-positive AGC may compensate for the intratumoral heterogeneity observed in GC, which may have negatively impacted responses to targeted therapies in this and other trials [27,28].

### [11] PIK3CAH1047R and Her2 initiated mammary tumors escape PI3K dependency by compensatory activation of MEK-ERK signaling
- Authors: Hailing Cheng, Pixu Liu, Carolynn E. Ohlson, Erbo Xu, Lynn K Symonds et al.
- Year: 2015
- Venue: Oncogene
- URL: https://www.semanticscholar.org/paper/fa9ef1dd841484add71630de5ac5f5647503006f
- DOI: 10.1038/onc.2015.377
- PMID: 26640141
- PMCID: 4896860
- Citations: 39
- Influential citations: 1
- Summary: PIK3CA-specific inhibition as a monotherapy followed by combination therapy targeting MAPK and HER2 in a timely manner may be an effective treatment approach against HER2-positive cancers with coexisting PIK3 CA-activating mutations.
- Evidence snippets:
  - Snippet 1 (score: 0.492)
    > ER2 is a receptor tyrosine kinase (RTK) that enhances the PI3K/AKT signaling pathway and the MAPK signaling pathway mainly through HER2/HER3 hetero-dimerization, 2 or activation of the MAPK signaling pathway preferentially through HER2 homodimerization. 18 Recent comprehensive genomic characterization revealed that up to 40% of HER2-positive breast cancers carry mutations in PIK3CA, 19 and that this circumstance correlates with lymph node metastases and poor patient outcome. [20][21][22] Such findings suggested that PIK3CA mutations may represent an important determinant of resistance to anti-HER2 therapies, thereby justifying further investigation of PI3K as a therapeutic target in HER2-positive breast cancer.
    > Recent studies have shown that PI3K/AKT inhibition induces the expression and phosphorylation of multiple RTKs, including HER3, and this may attenuate their antitumor effects. 23,24 Although these studies elegantly delineated the oncogenic rewiring of signaling pathways in cancer cell models as a result of targeted inhibition of PI3K/AKT signaling, direct in vivo evidence that supports this notion is still lacking. Thus, an appropriate animal model that recapitulates genetic and molecular aspects of human cancers is needed to test this hypothesis in a physiological context.
    > Clinical trials testing PI3K inhibitors alone or in combination with HER2-directed therapies are ongoing (clinicaltrials.gov). Hence, knowledge gained from understanding the impact of PI3K activation on HER2-positive breast cancer can be used to optimize HER2-targeted cancer therapies, leading to rational design of effective treatment strategies for this subtype of breast cancer also harboring oncogenic PIK3CA mutations. We generated a compound mouse model of mammary tumors in which an oncogenic mutation of human PIK3CA, H1047R, is expressed in a doxycycline-inducible manner while the activated Her2/Neu is constitutively expressed. Using this model, we investigated the impact of PI3K activation on tumor initiation and maintenance of HER2-positive breast cancer.

### [12] Immune cell profiles of metastatic HER2-positive breast cancer patients according to the sites of metastasis
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
  - Snippet 1 (score: 0.490)
    > Since immunology has a central role in HER2-positive breast cancer and targeted treatment acts through immunemediated mechanisms [5], we speculate that the presence of liver metastases would accordingly be associated with adverse prognosis and specific tumour immune profiles of the primary tumour.
    > In the current study, we tested this hypothesis by evaluating the prognosis and tumour immune cell profiles of 54 patients with metastatic HER2-positive breast cancer treated with trastuzumab containing regimens.

### [13] Large molecular systems landscape uncovers T cell trapping in human skin cancer
- Authors: Reyk Hillert, Anne Gieseler, Andreas Krusche, D. Humme, H.-J. Röwert-Huber et al.
- Year: 2016
- Venue: Scientific Reports
- URL: https://www.semanticscholar.org/paper/33de2062cfd1ed11b827368d31223ecb21fac495
- DOI: 10.1038/srep19012
- PMID: 26757895
- PMCID: 4725819
- Citations: 12
- Summary: Applying imaging cycler microscopy to analyse the immune contexture in a human skin cancer led to discovery of a mechanism of T cell trapping in the epidermis, which involves SPIKE, a network of suprabasal keratinocyte projections piercing and interconnecting CD8 T cells.
- Evidence snippets:
  - Snippet 1 (score: 0.490)
    > As shown before, inhibition of the lead proteins, e.g. in tumour cells results in disassembly of the corresponding protein clusters and loss of function 25 . Similar principles were demonstrated for amyothrophic lateral sclerosis (ALS) where CD16 (Fcgamma RIII) on human peripheral lymphocytes was identified as lead drug target 38 This protein was then confirmed as potential ALS drug target in a FcgammaRIII KO mouse model 28 and recently in a clinical phase II trial showing well tolerated downregulation of CD16 in ALS patients 29 with a halt of disease progression in 27% of the patients 30 . This empirical verification supports the toponome hypothesis that lead proteins controlling in vivo protein network topology and (dys)function can be predictive drug targets in chronic diseases and that the combinatorial geometry of protein networks at the target sites of the disease, as shown in present study, can provide important functional information on disease mechanisms.
    > ICM-based target identification and decoding of disease mechanisms in situ may thus complement current strategies for discovery of checkpoint controls as therapeutic target for reconstitution or enhancement of T cell activity against cancer 2,6,7,15,39-43 . The T cell trapping machinery may be a disease-specific robustness node for MF that ensures cancer progression by massively blocking cytotoxic T cells. As such it may be a target for therapeutic interventions that restore efficient anti-tumour immune responses.

### [14] Ranking of cell clusters in a single-cell RNA-sequencing analysis framework using prior knowledge
- Authors: A. Oulas, Kyriaki Savva, Nestoras Karathanasis, George M. Spyrou
- Year: 2023
- Venue: PLOS Computational Biology
- URL: https://www.semanticscholar.org/paper/efaf940a9b0405a5405ebf033673f32b3a1268df
- DOI: 10.1371/journal.pcbi.1011550
- PMID: 38635836
- PMCID: 11060557
- Citations: 1
- Summary: This work presents a novel methodology that exploits prior knowledge for a disease in combination with expert-user information to accentuate cell types from a scRNA-seq analysis that are most closely related to the molecular mechanism of a disease of interest.
- Evidence snippets:
  - Snippet 1 (score: 0.489)
    > The basic analysis flow of our methodology (see Figure 1 -Step 1) begins by performing scRNA-Seq analysis using SEURAT (ver. 4.3.0) (7) The checklist is comprised of pathways and drugs, as well as drug MOAs (optional), associated with the disease. 2) Hypothesis-driven mode: where the user can provide specific keywords/terms associated with the hypothesis under investigation (i.e., to check for signs of inflammation in the different cell types, the user may provide targeted terms associated with inflammation, e.g., Cytokines). For the hypothesis-driven approach, the new keyword terms that are defined are used to perform de-novo querying across the different supported databases (see below). The search extracts the relevant database entries (if any) associated with the keywords. As it may be difficult for the user to provide specific drug names as keywords for this approach, our methodology supports the input of drug MOAs, which can be supplied instead. Our method then proceeds to search and extract the relevant drugs associated with these MOAs using information from the Drug Repurposing Hub Database (https://clue.io/repurposing). The Drug repurposing hub is a curated and annotated collection of FDA-approved drugs, clinical trial drugs, and pre-clinical tool compounds ( 9). This information is made available for our methodology as a text file.
    > The order of the prior knowledge information is important for downstream analytics.
    > For the Discovery mode approach the order is defined by an enrichment score provided by MalaCards. For the Hypothesis-driven approach the user has to define the order of the keywords with most relevant/important keywords provided first.

### [15] Identification of disease mechanisms and novel disease genes using clinical concept embeddings learned from massive amounts of biomedical data
- Authors: A. Bugrim
- Year: 2023
- Venue: bioRxiv
- URL: https://www.semanticscholar.org/paper/ee810c8e4db715b5333cf89bf7034bfcaf424245
- DOI: 10.1101/2023.04.27.538319
- Citations: 2
- Summary: Combination of disease embeddings learned from massive amounts of biomedical records with curated data on gene-disease associations can reliably reveal groups of functionally related diseases and their molecular mechanisms and predict novel gene-Disease association co-embeddings.
- Evidence snippets:
  - Snippet 1 (score: 0.488)
    > This implies the existence of an unidentified physiological or molecular link. One hypothesis that can be put forward is that high level of activity of genes involved in vascular remodeling (such as matrix metalloproteinases MMP9, MMP2) makes a person predisposed to both: developing aortic aneurisms and suffering more severe consequences as a result of pulmonary embolism. While the role of these proteins in aortic aneurisms is well documented (41,42), the evidence has also emerged that inhibition of MMP9 in laboratory animals helps to alleviate effects of pulmonary embolism (43)(44)(45)(46) providing some support for this hypothesis. Another group of diseases (cluster "B" on Fig. 4) is a set of heart conditions. Some of these, such as heart failure and cardiac arrest are downstream effects of PE and are immediate causes of mortality in PE patients. It is interesting to note that while these conditions are aligned to PE in the embedding space, overall, there is not much similarity between diseases in cluster "B" and those in cluster "C". This may reflect the fact that in general, heart conditions are attributed to many different causes, while at the same time thrombi formation leads to many problems with PE and subsequent heart failure being only one of its consequences. This can be contrasted with the observation that myocardial infarction and acute coronary syndrome, rather than being grouped with other heart conditions, form a small tightly connected cluster with coronary thrombosis (cluster "E"). This shows that clinical connection of these heart conditions to coronary thrombosis is very strong and specific.
    > Above we demonstrate that close alignment of diseases in the embedding space can result from common or related molecular or physiological mechanisms. This property of disease embeddings can be leveraged for generating hypothesis about novel molecular mechanisms of pathological conditions and for suggesting potential drug targets for their treatment. It also helps to uncover unexpected mechanistic similarities between seemingly unrelated pathologies and to guide drug repositioning based on such connections. These goals are achieved by combining disease embedding with gene-disease association data.

### [16] RareAgent: Self-Evolving Reasoning for Drug Repurposing in Rare Diseases
- Authors: Lang Qin, Z. Gan, Xu Cao, Pengcheng Jiang, Yankai Jiang et al.
- Year: 2025
- Venue: ArXiv
- URL: https://www.semanticscholar.org/paper/ad0dc7cd9de3e46fb22cc025706d54dfe58331a0
- DOI: 10.48550/arXiv.2510.05764
- Summary: RareAgent is presented, a self-evolving multi-agent system that reframes this task from passive pattern recognition to active evidence-seeking reasoning, and improves the indication AUPRC by 18.1% over reasoning baselines and provides a transparent reasoning chain consistent with clinical evidence.
- Evidence snippets:
  - Snippet 1 (score: 0.487)
    > RareAgent operationalizes the scientific discovery process using a team of four AI agents with specialized roles, who collaborate on a shared whiteboard by constructing T-EGraph.
    > • Principal Investigator (PI): The strategic orchestrator. The PI does not directly manipulate evidence but sets research goals, evaluates the state of the T-EGraph, identifies knowledge gaps, issues directives to other agents, and is responsible for self-evolutionary learning loops.
    > • Explorer: The hypothesis generator. The Explorer initiates the investigation by querying the external KG using GNN to propose an initial set of plausible drug-disease hypotheses.
    > • Proponent: The constructive advocate. The Proponent's goal is to build a coherent, mechanistic case for a given hypothesis. It searches for and adds supporting evidence to the T-EGraph, aiming to form complete causal chains (e.g., Drug → Target → Pathway → Phenotype).
    > • Skeptic: The adversarial challenger. The Skeptic's role is to challenge the current hypothesis by finding counter-evidence, identifying risks, and exposing logical fallacies. It adds refuting evidence, such as off-target effects or safety concerns, to the T-EGraph.
    > The overall workflow proceeds in three phases: (1) Hypothesis Generation, where the Explorer seeds the investigation;
    > (2) Iterative Refinement, an autonomous adversarial debate where the Proponent and Skeptic build upon the T-EGraph under the PI's guidance; and (3) Self-Evolution, where the PI analyzes completed investigations to refine agent policies and distill reusable knowledge. All four agents are realized as LLM modules with role-specific policies, and the backbone is swappable and orthogonal to our contributions.

### [17] Integrative Systems Biology Resources and Approaches in Disease Analytics
- Authors: Marco Fernandes, H. Husi
- Year: 2019
- Venue: Systems Biology
- URL: https://www.semanticscholar.org/paper/b6360f094840c900e0116b69fe90daebe3161325
- DOI: 10.5772/INTECHOPEN.84834
- Citations: 1
- Summary: Several database resources, standalone and web-based tools applied in disease analytics workflows based in data-driven integration of outputs of multi-omic detection platforms are described.
- Evidence snippets:
  - Snippet 1 (score: 0.486)
    > Over the last decade the emergence of high-throughput screening platforms and the increase in availability of large-scale-omics data, as well as clinical data from electronic health records comprising phenotypic, therapeutic and environmental factors information opened the possibility to mechanistically understand diseases and diseases stages at the molecular level. Thereby, a great number of wealth data in many kidney and cardiovascular conditions was generated, however these findings were neither translated nor reached the clinical setting and are still enclosed in peer-reviewed literature and across general scope expression profiling databases. Simultaneously it has become apparent that the existing systems to integrate and correlate this data are either inadequate or non-existent. Due to the multi-factorial molecular phenotype of disease, it is evident that development of novel therapeutic and disease detection approaches should be based upon the study of the entire "System" simultaneously. Figure 1 gives a general overview in the fundamental difference between conventional and systems approaches, whereby in the context of conventional approaches a hypothesis is put forward that is assumed to be of importance in the disease or biological condition. This hypothesis is then tested and either validated or refuted based on the outcome of this hypothesis-driven methodology. Yet, it is obvious that it is easy to investigate any hypothesis and then choose the one that appears most correct, in the real world constraints such as time and financial resources do not allow for such an approach, and hypotheses are usually generated on a best-guess basis which can lead to a substantial amount of bias, resulting in skewed or partial insights and can often be misleading. In order to avoid such scenarios, research driven by the data itself rather than a hypothesis has been proposed a long time ago, but could not be properly implemented due to the lack of unbiased large-scale data or the ability to integrate disparate data in the first place. Additionally, a successful systems approach requires underlying prior knowledge, such as physicochemical parameters in how molecules interact with each other, what reactions they are involved in and other unconnected information. This knowledge has only slowly been accumulated through conventional research and has only over the last 10-15 years been available to such an extent where a systems approach became feasible. Data-driven systems biology-based diagnostic and prognostic models consisting of relevant panels of molecules-key branches of the cellular network, appear to more

### [18] DeepEvidence: Empowering Biomedical Discovery with Deep Knowledge Graph Research
- Authors: Zifeng Wang, Zheng Chen, Ziwei Yang, Xuan Wang, Qiao Jin et al.
- Year: 2025
- Venue: ArXiv
- URL: https://www.semanticscholar.org/paper/f06a59cb27b36766098ecb235c9ada048e145ed0
- DOI: 10.48550/arXiv.2601.11560
- Citations: 2
- Summary: DeepEvidence is introduced, an AI-agent framework designed to perform Deep Research across various heterogeneous biomedical KGs, and demonstrates substantial gains in systematic exploration and evidence synthesis.
- Evidence snippets:
  - Snippet 1 (score: 0.486)
    > Edges represent a controlled set of mechanistic membership association and evidence level relations, and every node and relation is grounded with explicit provenance from primary literature or curated knowledge graphs. Rather than encoding context as free text, the agent attaches short factual observations to entities, capturing experimental setting methodology and quantitative or mechanistic outcomes. During reasoning, the agent queries the existing graph before adding new content, merges near duplicates, updates observations instead of creating redundant nodes, and records conflicting findings with separate evidence links. We add the prompt in Supplementary Note A.4 to the agent's system prompt as additional guidance. This tight coupling between the agent and the evidence graph enables iterative hypothesis refinement, evidence aggregation, and transparent traceability, ensuring that conclusions are derived from an explicit, structured, and auditable body of biomedical evidence.
    > To facilitate cross-knowledge-base research and entity bridging, we implemented unified modality-wise search tools that aggregate information from multiple authoritative sources through a single interface. For instance, the unified gene search tool queries BioThings (MyGene.info), KEGG, and Open Targets simultaneously, returning consolidated results with cross-database identifiers. Similar unified tools exist for diseases, drugs, compounds, targets, pathways, and variants. Beyond entity lookup, we integrated relation-based search capabilities via the PubTator3 API, enabling agents to discover entities linked through specific semantic relationships such as TREAT, CAUSE, INTERACT, INHIBIT, and ASSOCIATE. This allows agents to traverse from diseases to candidate drugs, from genes to associated phenotypes, or from chemicals to their biological targets, supporting the depth-first reasoning patterns essential for mechanistic hypothesis generation. Together, these unified search and relation tools provide the knowledge infrastructure that enables research agents to bridge heterogeneous knowledge graphs and synthesize evidence across multiple biomedical domains.

## Notes

- This provider combines `search_papers_by_relevance` with `snippet_search`.
- No synthesis or second-stage model call is performed.
