---
provider: asta
model: Asta Scientific Corpus Retrieval
cached: false
start_time: '2026-05-26T23:12:17.607956'
end_time: '2026-05-26T23:12:23.189814'
duration_seconds: 5.58
template_file: templates/hypothesis_deep_research.md
template_variables:
  disease_name: COVID-19
  category: ''
  hypothesis_group_id: nsp3_mac1_essentiality_model
  hypothesis_label: Nsp3 Mac1 Macrodomain Essentiality Model
  hypothesis_status: CANONICAL
  hypothesis_yaml: "hypothesis_group_id: nsp3_mac1_essentiality_model\nhypothesis_label:\
    \ Nsp3 Mac1 Macrodomain Essentiality Model\nstatus: CANONICAL\ndescription: The\
    \ SARS-CoV-2 Nsp3 macrodomain (Mac1) is a conserved coronavirus mono-ADP-ribosylhydrolase\n\
    \  that is essential for pathogenesis. By hydrolyzing PARP9/DTX3L-deposited mono-ADP-ribose\
    \ marks on host\n  proteins, Mac1 neutralizes the effector branch of the host\
    \ interferon antiviral program and is required\n  for productive replication in\
    \ vivo. This is the disease-level instantiation of the parp_parg_macrodomain_viral_evasion\n\
    \  module's canonical countermeasure hypothesis.\nevidence:\n- reference: PMID:33158944\n\
    \  supports: SUPPORT\n  evidence_source: MODEL_ORGANISM\n  snippet: Mac1 is essential\
    \ for pathogenesis in multiple animal models of CoV infection\n  explanation:\
    \ In vivo essentiality across multiple coronavirus models directly supports the\
    \ canonical\n    Mac1 essentiality hypothesis.\n- reference: PMID:34358560\n \
    \ supports: SUPPORT\n  evidence_source: IN_VITRO\n  snippet: the cellular function\
    \ of the SARS-CoV-2 Nsp3 macrodomain is to hydrolyze this end product of\n   \
    \ IFN signaling, rather than to suppress the IFN response itself\n  explanation:\
    \ Russo et al. position Mac1 at the effector end of the IFN antiviral cascade,\
    \ consistent\n    with the canonical countermeasure model."
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
citation_count: 17
---

## Question

# Mechanistic Hypothesis Search

You are evaluating a specific disease mechanism hypothesis for the Disorder
Mechanisms Knowledge Base. This is not a general disease overview. Use the
hypothesis YAML below as the seed claim, then search for evidence that supports,
refutes, qualifies, or competes with this hypothesis.

## Target Disease
- **Disease Name:** COVID-19
- **Category:**

## Target Hypothesis
- **Hypothesis ID:** nsp3_mac1_essentiality_model
- **Hypothesis Label:** Nsp3 Mac1 Macrodomain Essentiality Model
- **Status in KB:** CANONICAL

## Seed Hypothesis YAML

```yaml
hypothesis_group_id: nsp3_mac1_essentiality_model
hypothesis_label: Nsp3 Mac1 Macrodomain Essentiality Model
status: CANONICAL
description: The SARS-CoV-2 Nsp3 macrodomain (Mac1) is a conserved coronavirus mono-ADP-ribosylhydrolase
  that is essential for pathogenesis. By hydrolyzing PARP9/DTX3L-deposited mono-ADP-ribose marks on host
  proteins, Mac1 neutralizes the effector branch of the host interferon antiviral program and is required
  for productive replication in vivo. This is the disease-level instantiation of the parp_parg_macrodomain_viral_evasion
  module's canonical countermeasure hypothesis.
evidence:
- reference: PMID:33158944
  supports: SUPPORT
  evidence_source: MODEL_ORGANISM
  snippet: Mac1 is essential for pathogenesis in multiple animal models of CoV infection
  explanation: In vivo essentiality across multiple coronavirus models directly supports the canonical
    Mac1 essentiality hypothesis.
- reference: PMID:34358560
  supports: SUPPORT
  evidence_source: IN_VITRO
  snippet: the cellular function of the SARS-CoV-2 Nsp3 macrodomain is to hydrolyze this end product of
    IFN signaling, rather than to suppress the IFN response itself
  explanation: Russo et al. position Mac1 at the effector end of the IFN antiviral cascade, consistent
    with the canonical countermeasure model.
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

- Papers retrieved: 17
- Snippets retrieved: 20

## Relevant Papers

### [1] Whole patient knowledge modeling of COVID-19 symptomatology reveals common molecular mechanisms
- Authors: S. Brock, David B Jackson, Theodoros G. Soldatos, K. Hornischer, Anne Schäfer et al.
- Year: 2023
- Venue: Frontiers in Molecular Medicine
- URL: https://www.semanticscholar.org/paper/c4cb8ce50e078b71d83a74b18eef01fac0748cbe
- DOI: 10.3389/fmmed.2022.1035290
- PMID: 39086962
- PMCID: 11285600
- Citations: 3
- Summary: This work followed an iterative, expert-driven process to compile data published prior to and during the early stages of the pandemic into a comprehensive COVID-19 knowledge model, suggesting the importance of whole patient knowledge frameworks in hypothesis generation and testing.
- Evidence snippets:
  - Snippet 1 (score: 0.634)
    > Infection with SARS-CoV-2 coronavirus causes systemic, multi-faceted COVID-19 disease. However, knowledge connecting its intricate clinical manifestations with molecular mechanisms remains fragmented. Deciphering the molecular basis of COVID-19 at the whole-patient level is paramount to the development of effective therapeutic approaches. With this goal in mind, we followed an iterative, expert-driven process to compile data published prior to and during the early stages of the pandemic into a comprehensive COVID-19 knowledge model. Recent updates to this model have also validated multiple earlier predictions, suggesting the importance of such knowledge frameworks in hypothesis generation and testing. Overall, our findings suggest that SARS-CoV-2 perturbs several specific mechanisms, unleashing a pathogenesis spectrum, ranging from "a perfect storm" triggered by acute hyper-inflammation, to accelerated aging in protracted "long COVID-19" syndromes. In this work, we shortly report on these findings that we share with the community via 1) a synopsis of key evidence associating COVID-19 symptoms and plausible mechanisms, with details presented within 2) the accompanying "COVID-19 Explorer" webserver, developed specifically for this purpose (found at https://covid19. molecularhealth.com). We anticipate that our model will continue to facilitate clinico-molecular insights across organ systems together with hypothesis generation for the testing of potential repurposing drug candidates, new pharmacological targets and clinically relevant biomarkers. Our work suggests that whole patient knowledge models of human disease can potentially expedite the development of new therapeutic strategies and support evidence-driven clinical hypothesis generation and decision making.
  - Snippet 2 (score: 0.588)
    > computer-augmented modeling approach, guided by disease modeling experts that allowed us to build a comprehensive digital model during the early phases of the pandemic (Brock et al., 2022).
    > In this work, we explore the utility and importance of the holistic patient-level knowledge model within the COVID-19 Explorer resource and examine its key features, particularly surrounding the molecular underpinnings of COVID-19 symptomatology. Characteristically, the model suggests that the multitude and complexity of observed, and seemingly disparate COVID-19 clinical phenotypes may be linked to the pleiotropic activity of eight core molecular mechanisms involved in the host response. Moreover, the model revealed functionally connected mechanisms across multiple organ systems and identified novel hypotheses for both viral dependent and independent disease mechanisms. Here, we discuss these molecular perspectives in detail, including the content of the causative pathogenic mechanisms underlying COVID-19 phenotypes, real world confirmatory observations, and examples that demonstrate some of the key analytical utilities (e.g., risk factors). Finally, we focus on the detection of potentially new (or unobvious) clinico-molecular insights across organsystems and on the identification of potential pharmacologic targets against COVID-19 (Brock et al., 2022).
    > Our results show that structuring emergent molecular knowledge via a pan-symptomatic disease format, helped develop a comprehensive whole patient COVID-19 knowledge model that could expedite evidence-driven hypothesis generation and the discovery of novel clinico-molecular insights. Inspired by the effectiveness of this strategy, we propose that whole-patient knowledge modeling of systemic symptomatology for any disease, as opposed to traditional pathway-specific modeling, may provide important advantages in tackling current unmet medical needs and future health emergencies. Importantly, the whole-patient knowledge model is provided to the community in the form of both an open-source web-sever (found at https://covid19. molecularhealth.com), and a tabular COVID-19 "Cockpit" (Brock et al., 2022). Together they are aimed at enabling a variety of use-case scenarios useful to support translational and clinical researchers in hypothesis generation and the development of

### [2] The peripheral and core regions of virus-host network of COVID-19
- Authors: Bingbo Wang, Xianan Dong, Jie Hu, Xiujuan Ma, Chao Han et al.
- Year: 2021
- Venue: Briefings in Bioinformatics
- URL: https://www.semanticscholar.org/paper/eab5ec5446a62abe1461e15c8ae2e15e7a267c8c
- DOI: 10.1093/bib/bbab169
- PMID: 33956950
- PMCID: 8136014
- Citations: 7
- Summary: It is found that the virus-host proteins (VHPs) form a significantly connected VHN, among which highly perturbed proteins aggregate into an observable core region and the periphery-core pattern can offer insights into interconnectivity of SARS-CoV-2 VHPs but also facilitate the research on therapeutic drugs.
- Evidence snippets:
  - Snippet 1 (score: 0.564)
    > In this study, we draw upon the latest advances in COVID-19 virus-host research and network medicine methods to identify the VHN and core region of COVID-19, and we find that both VHN and core regions are internally tightly connected topologies in the human interactome. Then, we combine the C3 disease modules of 70 diseases and the core regions of SARS and H1N1 to analyze the disease similarity. We compute their network distance with the VHN or core region of COVID-19 based on their location in human interactome and find several high similarity diseases including immune and neurological diseases and cancers. We identified drug targets based on network proximity and predicted drug outcomes as high as 0.77, suggesting that COVID-19's peripheral and core regions also provide an opportunity for drug repurposing. This result can provide new insights into understanding the disease mechanisms of COVID-19 and guide us in the prevention and treatment of COVID-19.
    > Core region typically consists of genes specific for the underlying disease. Based on the hypothesis that the similar molecular mechanism of diseases lies in their overlapped peripheries, we identify the molecular mechanism of disease causation, new comorbidity and aid rational drug target for COVID-19. In particular, we construct the flower model for COVID-19, SARS and H1N1 and show the details of their overlapped peripheral proteins. Enrichment analysis further proved that overlapped peripheries consistently enrich in Parkinson Disease, Huntington Disease, Alzheimer Disease and Non-Alcoholic Fatty Liver Disease pathways; provide 16 proteins targeted by 9 existing drugs currently undergoing clinical trials and drugs predicted by periphery have a certain effectiveness in the treatment of COVID-19. The periphery and core structure of COVID-19 provides new insights for the analysis of disease relationship and drug prediction.
    > Although Ratnakumar et al. [21] proposed instructive methods for identifying disease core genes, there are variety of definitions including highest differential expression level, strongest effect mutations or interpretable mechanistic links to disease.

### [3] Gathering Evidence of Mechanisms
- Authors: Veli-Pekka Parkkinen, Christian Wallmann, Michael Wilde, B. Clarke, P. Illari et al.
- Year: 2018
- Venue: Unknown venue
- URL: https://www.semanticscholar.org/paper/06480fd932fc88915a4efb4c894a5ae4ed98452d
- DOI: 10.1007/978-3-319-94610-8_5
- Citations: 1
- Summary: Key issues include increased precision concerning the nature of the hypothesis being examined, attention to differences between the study population and the target population of the evidence assessors, and being alert for masking mechanisms, which are other mechanisms which may mask the action of the mechanism being assessed.
- Evidence snippets:
  - Snippet 1 (score: 0.558)
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
  - Snippet 2 (score: 0.532)
    > Although ACE-inhibitors have proved beneficial for hypertension in many study populations, there remains the question of whether they are the optimal treatment in some distinct target population, such as African or Caribbean populations. In this case, it is necessary to determine the status of the following general mechanistic claim: the relevant hypertensive mechanisms in the study populations are sufficiently similar to the mechanisms in African or Caribbean populations. This general mechanistic claim can be evaluated by evaluating a more specific mechanism hypothesis, namely that African and Caribbean populations have a lower renin state. As we shall see in Chap. 6, there is some good mechanistic evidence in favour of this specific mechanism hypothesis, and this undermines the general mechanistic claim. This is why, instead, calcium channel blockers are the recommended antihypertensive treatment in African and Caribbean populations (Clarke et al. 2014).
    > There are two main ways to identify a specific mechanism hypothesis. First, a specific mechanism hypothesis may be proposed on the basis of published studies from the clinical study literature. If a clinical study establishes a correlation between a putative cause and effect, and the suggestion is that this correlation is causal, then the authors of such a study usually identify at least one possible mechanism hypothesis of the following form: It is plausible that mechanism with features F links the putative cause and effect in the study population. The study may also point out possible masking mechanisms (Illari 2011). Given this, the discussion section of a published paper that reports the results of a clinical study is a good place to look in order to locate a specific mechanism hypothesis.
  - Snippet 3 (score: 0.490)
    > The overall approach to gathering evidence of mechanisms of action. Each proposed mechanism of action, or partial description of proposed mechanism of action, is a specific mechanism hypothesis. But note that a specific mechanism hypothesis need not be a complete description of a mechanism.
    > Example: Specific mechanism hypotheses for determining efficacy.
    > Aspirin prevents heart disease via cyclooxygenase (COX) inhibition, and the mechanisms that underlie this prevention are established. However, aspirin also seems to reduce the incidence of some cancers. Here, the mechanisms are much less well understood. As Chan et al. (2011) write: "the mechanism of aspirin's antineoplastic effect is less clear, with substantial evidence supporting both COX-dependent and COX-independent mechanisms. Moreover, data supporting the importance of COX-dependent mechanisms are not entirely consistent concerning the relative importance of the COX-1 and COX-2 isoforms in carcinogenesis". In this quotation, the general mechanistic claim is that aspirin exhibits an antineoplastic effect. There are also a couple of more specific mechanism hypotheses, for example, that this antineoplastic effect is mediated by COX-dependent mechanisms. Evidence relating to these more specific mechanism hypotheses provides a way to determine the status of the general mechanistic claim.
    > External validity. In order to evaluate the general mechanistic claim that there is a mechanism in the target population sufficiently similar to the mechanism responsible for the correlation observed in the study population, specific mechanism hypotheses need to pertain to the mechanism of action. It is important to consider the possibility that the mechanism in the target population may contain further component mechanisms that counteract the mechanism of action in the study population and affect the extent of the correlation between the putative cause and effect. So one needs to ask, are there any masking mechanisms in the target population?
    > Example: Specific mechanism hypotheses for determining external validity.
    > According to NICE guidelines, treatment for hypertension should differ depending on ethnicity (NICE 2011). Although ACE-inhibitors have proved beneficial for hypertension in many study populations, there remains the question of whether they are the optimal treatment in some distinct target population, such as African or Caribbean populations.

### [4] A diseasome cluster-based drug repurposing of soluble guanylate cyclase activators from smooth muscle relaxation to direct neuroprotection
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
  - Snippet 1 (score: 0.547)
    > Drug discovery and development follows a relatively uniform path from mechanistic hypothesis, preclinical disease models to clinical validation. However, in recent years, a string of major drug developments have failed due to lack of efficacy. 1 One reason for this appears to reside in our current definitions of 'disease', i.e., mostly organ-based or by an apparent phenotype or symptom and not by an underlying mechanisms. However, without a validated pathomechanism no mechanism-based drugs can be developed and, therefore, rather surrogate parameters or risk factors are treated instead. Finding a rational approach towards mechanism-based disease definitions may therefore have a tremendous impact on drug discovery and medicine in general.
    > Using a data-driven approach, disease-disease networks (diseosome) have been constructed in which diseases are linked based on common molecular or regulatory mechanisms, 2 such as shared genetic associations, 2 protein interactions 3,4 or gene-disease interactions. 5 These diseasomes exhibit local clusters of diseases whose molecular relationships are well understood, but also unexpected clusters of surprisingly heterogeneous diseases. 3 Such clustering of disease phenotypes is likely due to underlying hidden common pathomechanisms. Importantly, these common mechanism clusters may provide previously unrecognized molecular definitions of these phenotypes and at the same time targets for mechanism-based drug discovery and repurposing.
    > Here we test the clinical validity of this approach by focusing on one cluster of highly prevalent combinations of vascular, neurological and metabolic disease phenotypes with high unmet medical need. Genetic evidence points to cGMP signaling as being part of its underlying pathomechanism. 5,6 We then inquire in a non-hypothesis-based manner using disease-disease networks based on common genetic origins, common protein interactions between disease genes, shared disease symptoms and disease co-morbidity for possible drug repurposing of cGMP modulators within this cluster.

### [5] Mechanistic Research for the Student or Educator (Part I of II)
- Authors: R. Leak, James B. Schreiber
- Year: 2020
- Venue: Frontiers in Pharmacology
- URL: https://www.semanticscholar.org/paper/310d1cb284042ff6ce384dcc47b7f50a124237e7
- DOI: 10.3389/fphar.2022.775632
- PMID: 35847028
- PMCID: 9283720
- Summary: In this two-part series, the caveats and strengths of mechanistic preclinical research are briefly described, using the intuitive example of pharmaceutical drug testing in experimental models of human diseases to help the new student appreciate the strengths and limitations of scientific research.
- Evidence snippets:
  - Snippet 1 (score: 0.534)
    > STEM educators are responsible for training students in the rigorous conduct and evaluation of mechanistic research. However, the PubMed search terms "(education) AND (mechanistic) AND (hypothesis)" or the alternate search terms "(teaching) AND (mechanistic) AND (hypothesis)" do not capture publications focused on teaching students how to identify mechanisms of drug action or the associated caveats. To fill this gap, we will discuss problems related to testing two commonly-encountered hypotheses, using preclinical drug testing as a teaching tool: Hypothesis 1. The pharmaceutical drug candidate (or any kind of intervention) reduces the toxic effects of preclinical disease by upregulating the function of a protein Hypothesis 2. The pharmaceutical drug candidate (or any kind of intervention) reduces the toxic effects of preclinical disease by downregulating the function of a protein
    > To test these hypotheses, it is necessary to determine if the therapeutic effects of the drug can be abolished (or at least attenuated) when the proposed mechanism of action has been interfered with. This is discussed in detail in Part II of this twopart series. In our examples, the null hypotheses state that the drug continues to mitigate the toxic effects of preclinical disease, even when the function of the protein is experimentally manipulated. However, rejection or retention of the null hypothesis will not be argued further in this series (Greenland, 2019). Rather, the focus is on the test hypothesis-as in a modern grant proposal.
    > The reader may wonder if the researcher really needs a mechanistic hypothesis to commence their laboratory work. The short answer is, "Of course not." The beginner does not even need a non-mechanistic hypothesis-they can perform a study to simply observe and describe a biological phenomenon. Unlike mechanistic work, descriptive and observational studies are not dependent upon crafting any a priori hypothesis. Although this type of descriptive research may be viewed less favorably by reviewers of papers and grant applications, it can be less biased than hypothetico-deductive research, by virtue of its exploratory and open-ended nature (Marincola, 2007;Casadevall and Fang, 2008). The beginner may find that descriptive research is essential in the

### [6] Structure-based discovery of inhibitors of Mac1 domain of nonstructural protein-3 of SARS-CoV-2 by machine learning-augmented screening of chemical space
- Authors: Fuqiang Ban, Rahul Ravichandran, G. Correy, Oleksandra Herasymenko, Madhushika Silva et al.
- Year: 2025
- Venue: bioRxiv
- URL: https://www.semanticscholar.org/paper/5cb90b48c50644b10a7e31328ed3e4647f47a71c
- DOI: 10.1101/2025.09.05.674529
- PMID: 40964377
- PMCID: 12440007
- Summary: The results illustrate the effectiveness of ML-accelerated docking to rapidly identify novel chemical series and provide a strong foundation for the development of SARS-CoV-2 NSP3 Mac1 inhibitors.
- Evidence snippets:
  - Snippet 1 (score: 0.516)
    > ADP-ribosylation is a NAD+-dependent modification of proteins or nucleic acids, broadly categorized as Mono(ADP-ribosyl)ation (MARylation) or poly(ADP-ribosyl)ation (PARylation). The process of MARylation plays a complex role in antiviral response through modifying host and viral proteins. To counteract antiviral ADP-ribosylation by host Poly(ADP-ribose) polymerases (PARPs), SARS-CoV-2 and other coronaviruses encode a conserved macrodomain within the nonstructural protein 3 (NSP3) that hydrolyzes ADPribose modifications, thereby reversing the effect of ADP ribosylation 1 , which enhances interferon signalling 2 . In SARS-CoV-2, the Macrodomain 1 (Mac1) of NSP3 plays a key role in the immune evasion capabilities responsible for the coronavirus disease 2019 (COVID-19) pandemic 3 . In particular, Mac1 displays mono(ADP-ribosyl) hydrolase activity to block interferon response and acts against the host defense mechanism, which is essential and critical for coronavirus pathogenesis and lethality 1,4 .
    > An active site mutation inactivating Mac1 has been shown to render SARS-CoV-1 and SARS-CoV-2 nonlethal in a lethal mouse model of viral infection, and virus bearing the mutation do not replicate as efficiently in interferon-stimulated cells as wild type virus. 5 erefore, Mac1 has emerged as a potential antiviral drug target with promising therapeutic value.
    > Following the onset of COVID-19, many inhibitors of Mac1 have been reported. 6 In particular, Gahbauer et al. identified 160 Mac1 ligands representing 119 different scaffolds and determined 152 complex crystal structures through iterations of fragment screening, structure-based design, protein crystallography, and binding evaluation, identifying several molecules with low-to sub-micromolar potencies. 7 o other approaches of fragment-linking 8 and virtual screening of ultra-large chemical libraries 9 were also employed for the discovery and optimization of potent Mac1 ligands.

### [7] Network-based integrative multi-omics approach reveals biosignatures specific to COVID-19 disease phases
- Authors: Francis E. Agamah, Thomas H. A. Ederveen, Michelle Skelton, Darren P. Martin, Emile R. Chimusa et al.
- Year: 2023
- Venue: Frontiers in Molecular Biosciences
- URL: https://www.semanticscholar.org/paper/17f9e0e3ecb026cc63a5d13c4917c27ea0253318
- DOI: 10.3389/fmolb.2024.1393240
- PMID: 39040605
- PMCID: 11260748
- Citations: 4
- Summary: This study identified both biosignatures of different omics types enriched in disease-related pathways and their associated interactions that are either common between or unique to mild, moderate, and severe COVID-19 disease phases.
- Evidence snippets:
  - Snippet 1 (score: 0.515)
    > Having demonstrated that cross-layer interactions could be a distinctive feature, if not a hallmark, of severe COVID-19, it warrants deeper investigation into the potential causal relationships that these cross-layer interactions, have with disease progression: relationships that might illuminate ways to prevent and/or reverse this progression.
    > IL6 is a vital innate immune cytokine in protection against other viral infections such as influenza A virus, which can cause pneumonia (Guirao et al., 2020). An increase in IL6 levels has previously been observed in patients with respiratory dysfunction, implying a possible mechanism of cytokine-mediated lung damage caused by COVID-19 infection (Gou et al., 2020;Guirao et al., 2020). Our hypothesis-driven approach revealed that higher COVID-19 disease severity was associated with an increased number of interactions between IL6 and other multi-omics layers, therefore suggesting that our approach may discriminate between COVID-19 and other respiratory disorders. However, to confirm we will need future studies on the evaluation of network-based multi-omics approaches for COVID-19 compared to other infectious diseases, including those of viral and bacterial nature.
    > Our study suggests a deeper understanding of the underlying biological interactions in different phases of COVID-19 disease. The results (Figures 4,5,along with Table 5; Supplementary Table S3 and Supplementary Material S2) present an extensive analysis of multilayered graphs generated by complementary approaches including data-driven and hypothesis-driven seeds, and shed light on the complex interactions underlying different phases of COVID-19. These findings suggest a nuanced understanding of how various molecular features interact and influence disease severity. However, heterogeneity, different sample sizes, and sensitivity of types of samples used for sequencing across studies might be a potential source of bias. The hypothesis-driven approach offers a reductionist strategy for experimental proof whereas the data-driven approach offers a holistic strategy and hypothesis generation. We recommend considering both data-and hypothesis-driven approaches in studies utilizing multiple source omics datasets. Also, the complexity of disease severity harmonization, identifier mapping, and feature selection might be potential sources of bias in our studies.

### [8] Use of renin–angiotensin–aldosterone system inhibitors and risk of COVID-19 requiring admission to hospital: a case-population study
- Authors: F. D. de Abajo, S. Rodríguez‐Martín, V. Lerma, G. Mejía-Abril, M. Aguilar et al.
- Year: 2020
- Venue: Lancet (London, England)
- URL: https://www.semanticscholar.org/paper/5ea714f2f9622f9030f104a7eb50b0b79b2f106b
- DOI: 10.1016/S0140-6736(20)31030-8
- PMID: 32416785
- PMCID: 7255214
- Citations: 377
- Influential citations: 16
- Summary: RAAS inhibitors do not increase the risk of COVID-19 requiring admission to hospital, including fatal cases and those admitted to intensive care units, and should not be discontinued to prevent a severe case of COVID-19.
- Evidence snippets:
  - Snippet 1 (score: 0.507)
    > Evidence before this study Inhibitors of the renin-angiotensin-aldosterone system (RAAS) have been hypothesised to predispose patients to more severe COVID-19. This hypothesis is based on two facts: these drugs have been reported to upregulate the expression of angiotensinconverting enzyme (ACE) 2, the gateway used by severe acute respiratory syndrome coronavirus 2 to enter cells, and patients with severe COVID-19 have a high prevalence of cardiovascular diseases. Many scientific societies adopted the position of not recommending the discontinuation of treatment. Yet, epidemiological evidence is lacking and the hypothesis has not been confirmed or refuted. We searched PubMed on April 15, 2020, for publications in English since Jan 1, 2020, using the search terms "COVID-19" and "ACE inhibitors OR angiotensin-converting enzyme inhibitors OR angiotensin receptor blockers OR RAAS inhibitors OR RAS inhibitors OR RAAS blockers OR RAS blockers", filtering by "human" and "observational study", and no result was returned.

### [9] Cascading from SARS-CoV-2 to Parkinson’s Disease through Protein-Protein Interactions
- Authors: Ernesto Estrada
- Year: 2021
- Venue: Viruses
- URL: https://www.semanticscholar.org/paper/b012d46aba9b8899e9981dbebae70fc4c846474a
- DOI: 10.3390/v13050897
- PMID: 34066091
- PMCID: 8150712
- Citations: 17
- Influential citations: 1
- Summary: A molecular-level mechanistic hypothesis is presented that provides several routes for the cascading of effects from the lungs of COVID-19 patients to PD, and the disruption of autophagy/ubiquitination processes appears as an important mechanism that triggers the generation of large amounts of exosomes containing perturbators in their cargo, which would insult several PD-vulnerable proteins, potentially triggering Parkinsonism in COIDs patients.
- Evidence snippets:
  - Snippet 1 (score: 0.504)
    > Extensive extrapulmonary damages in a dozen of organs/systems, including the central nervous system (CNS), are reported in patients of the coronavirus disease 2019 (COVID-19). Three cases of Parkinson’s disease (PD) have been reported as a direct consequence of COVID-19. In spite of the scarce data for establishing a definitive link between COVID-19 and PD, some hypotheses have been proposed to explain the cases reported. They, however, do not fit well with the clinical findings reported for COVID-19 patients, in general, and for the PD cases reported, in particular. Given the importance of this potential connection, we present here a molecular-level mechanistic hypothesis that explains well these findings and will serve to explore the potential CNS damage in COVID-19 patients. The model explaining the cascade effects from COVID-19 to CNS is developed by using bioinformatic tools. It includes the post-translational modification of host proteins in the lungs by viral proteins, the transport of modified host proteins via exosomes out the lungs, and the disruption of protein-protein interaction in the CNS by these modified host proteins. Our hypothesis is supported by finding 44 proteins significantly expressed in the CNS which are associated with PD and whose interactions can be perturbed by 24 host proteins significantly expressed in the lungs. These 24 perturbators are found to interact with viral proteins and to form part of the cargoes of exosomes in human tissues. The joint set of perturbators and PD-vulnerable proteins form a tightly connected network with significantly more connections than expected by selecting a random cluster of proteins of similar size from the human proteome. The molecular-level mechanistic hypothesis presented here provides several routes for the cascading of effects from the lungs of COVID-19 patients to PD. In particular, the disruption of autophagy/ubiquitination processes appears as an important mechanism that triggers the generation of large amounts of exosomes containing perturbators in their cargo, which would insult several PD-vulnerable proteins, potentially triggering Parkinsonism in COVID-19 patients.

### [10] The cognitive science of COVID-19: Acceptance, denial, and belief change
- Authors: P. Thagard
- Year: 2021
- Venue: Methods (San Diego, Calif.)
- URL: https://www.semanticscholar.org/paper/76beb1dd87692e36d49120c0e07dfe80b6f8b8d9
- DOI: 10.1016/j.ymeth.2021.03.009
- PMID: 33744395
- PMCID: 8545909
- Citations: 18
- Influential citations: 1
- Summary: Because the spread of pandemics depends heavily on human choices and behaviors, dealing with COVID-19 requires insights from cognitive science which integrates psychology, neuroscience, computer modeling, philosophy, anthropology, and linguistics.
- Evidence snippets:
  - Snippet 1 (score: 0.502)
    > The alternative account of inference to causal hypotheses is the theory of explanatory coherence that has been applied to many cases of medical and scientific reasoning such as the claim that the Zika virus causes birth defects [9][10][11][12][13][14]. This theory is based on the philosophical idea that causal reasoning is inference to the best explanation of the available evidence, but fleshes it out into a computational model using neural networks that do not require probabilities. Instead, causal reasoning is understood as a process of simultaneously satisfying multiple constraints.
    > The main positive constraints for explanatory coherence are that causal hypotheses explain the evidence for them and that these hypotheses can in turn be explained by deeper hypotheses concerning the relevant mechanisms. For example, the hypothesis that wearing masks prevents disease explains various pieces of evidence such as that there is less spread of disease in mask-wearing countries such as China. Moreover, scientists can explain the effectiveness of wearing masks by identifying the underlying mechanism: the virus spreads on droplets through the air and masks block the droplets. Hence the claim that wearing masks prevents disease spread gets coherence both from what it explains and from what explains it.
    > The main negative constraints operating in explanatory coherence concern the alternative causal hypotheses that compete with each other. For example, the hypothesis that wearing masks prevents disease has to compete with the hypothesis that masks do not prevent disease which purports to explain other pieces of evidence such as that medical personnel get sick despite wearing masks. A hypothesis is accepted or rejected based on its overall coherence with all of the evidence and all other hypothesis, where coherence is a matter of satisfying as many constraints as possible. Fig. 1 shows the structure of the explanatory coherence assessment of the mask hypothesis. The hypothesis that wearing masks causes a reduction of spread of COVID-19 gets its explanatory coherence from 4 directions: what it explains, what explains it, analogy with SARS and other infectious diseases, and competition with the claim that masks do not prevent COVID-19 [15][16][17][18][19][20][21][22][23][24][25]

### [11] Malaria, COVID-19 and angiotensin-converting enzyme 2: what does the available population data say?
- Authors: A. De, M. Dash, A. Tiwari, A. Sinha
- Year: 2021
- Venue: Open Biology
- URL: https://www.semanticscholar.org/paper/5f3bcc1a04189b2360efd02fd025fed381d55eb9
- DOI: 10.1098/rsob.210213
- PMID: 34637655
- PMCID: 8510699
- Citations: 2
- Summary: Based on the existing global and Indian data on malaria, COVID-19 and the suggested ACE2 mutation, the association could not be examined robustly, neither accepting nor refuting the suggested hypothesis.
- Evidence snippets:
  - Snippet 1 (score: 0.499)
    > The etiopathogenesis of COVID-19 and its differential geographic spread suggest some populations are apparently ‘less affected’ through many host-related factors that involve angiotensin-converting enzyme 2 (ACE2) protein, which is also the entry receptor for SARS-CoV-2. The role of ACE2 has been well studied in COVID-19 but not in the context of malaria and COVID-19. We have previously suggested how malaria might intersect with COVID-19 through ACE2 mutation and here we evaluate the currently available data that could provide a link between the two diseases. Based on the existing global and Indian data on malaria, COVID-19 and the suggested ACE2 mutation, the association could not be examined robustly, neither accepting nor refuting the suggested hypothesis. We strongly recommend targeted evaluation of this hypothesis through carefully designed robust molecular epidemiological studies.

### [12] DiseaseConnect: a comprehensive web server for mechanism-based disease–disease connections
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
  - Snippet 1 (score: 0.499)
    > After viewing all diseases and molecules related to a query disease, users can further explore the shared molecular mechanism(s) between two specific diseases by clicking an edge in the disease network. For example, when a user queries MM, the web server generates a disease-disease network. The user can then click the connection between MM and hemorrhagic disorders (HD) to view a network of shared genes and drugs between HD and MM. Figure 6A shows a small part of this network with the shared gene PSMB5 and the drug bortezomib. PSMB5 is a DEG for both HD and MM, and also has a GeneRIF association with MM. Bortezomib is a therapeutic proteasome inhibitor for treating MM, and targets PSMB5 (39). Interestingly, bortezomib can also treat HD (40), suggesting that shared disease genes can serve as good targets for drug repositioning strategies. Figure 6B shows another example network for the queried disease pair 'arthritis' and 'Crohn disease', both involve the tumor necrosis factor (TNF), based on the data sources GWAS and GeneRIF. Thalidomide is an immunomodulatory drug that targets TNF. Interestingly, thalidomide can treat both arthritis and Crohn diseases (41), supporting our hypothesis that diseases with a shared molecular mechanism are likely to be treated by the same drug. Another drug shown in Figure 6B, 'adalimumab', is known to target TNF and can treat arthritis, suggesting that it may also be effective for Crohn disease. In fact, this inference is confirmed independently by a recent report of Peters et al. (42). Also, several clinical trials about Adalimumab and Crohn disease (e.g. ClinicalTrials.gov ID: NCT01556672 and NCT01958827) are currently ongoing.

### [13] Systems Bioinformatics Reveals Possible Relationship between COVID-19 and the Development of Neurological Diseases and Neuropsychiatric Disorders
- Authors: Anna Onisiforou, G. Spyrou
- Year: 2022
- Venue: Viruses
- URL: https://www.semanticscholar.org/paper/6db0f7d994622b5e960d5b8ae7cb402b584d9816
- DOI: 10.3390/v14102270
- PMID: 36298824
- PMCID: 9611753
- Citations: 17
- Summary: The results suggest that there might be an increased risk for the development of NDs after COVID-19 both via autoreactivity and virus–host PPIs.
- Evidence snippets:
  - Snippet 1 (score: 0.497)
    > Moreover, in this study we choose to focus on a specific list of 10 neurological diseases and 3 neuropsychiatric disorders. The diseases/disorders examined in this study were selected based on the hypothesis that diseases/disorders whose development and/or progression has been associated with viral infections have a higher probability to be triggered by a new emerging virus, in this case SARS-CoV-2, than other diseases, as viruses share several common pathogenic mechanisms. However, our selection list is not exhaustive as other neurological diseases or even other types of diseases, particularly autoimmune diseases, which have a strong association with viral infections can also potentially be triggered by COVID-19. Nonetheless, these diseases are beyond the scope of this paper and may be addressed in future works using the presented computational methodology.

### [14] Utility of compartmental models to test the competing hypotheses of pathogen evolution and human intervention
- Authors: Barsha Saha, Majid Bani-Yaghoub, C. Podder
- Year: 2026
- Venue: Frontiers in Public Health
- URL: https://www.semanticscholar.org/paper/749f3bc337708c7462f520ae5f06ceb914a49149
- DOI: 10.3389/fpubh.2025.1702428
- PMID: 41626397
- PMCID: 12853639
- Citations: 1
- Summary: A new model-based hypothesis testing (MBHT) approach, which uses compartmental models to evaluate the hypotheses in epidemiology and reveals that model-based hypothesis testing offers a powerful yet underutilized approach to uncovering drivers of viral mutation and gaining deeper insights into pathogen evolution during outbreaks.
- Evidence snippets:
  - Snippet 1 (score: 0.493)
    > Model-Based Hypothesis Testing (MBHT) is a framework that enables researchers to evaluate competing mechanistic hypotheses by integrating compartmental models with relevant data. In many settings, there is insufficient direct evidence to distinguish among hypotheses at the level of individual parameters or mechanisms. Unlike traditional hypothesis testing, which typically relies on a test statistic derived from observed data, MBHT leverages the output of a validated dynamical model that captures the underlying ecological, evolutionary, or epidemiological processes (37,38). For example, even when direct measurements of disease transmission rates or virulence are unavailable, their distributions can be inferred by fitting a compartmental model to morbidity and mortality data. These inferred parameter distributions can then be used to quantify the relative support for alternative hypotheses. In this way, MBHT enhances the specificity and interpretability of inference by comparing hypotheses through model-based simulations rather than relying solely on empirical contrasts.
    > The MBHT approach differs fundamentally from classical hypothesis testing by offering a mechanistic, model-driven framework tailored to nonlinear, time-dependent systems. Conventional statistical methods typically compare outcomes between control and treatment groups, assuming that the relevant mechanisms can be probed directly from data. In contrast, MBHT relies on model analysis and simulation to identify the best-supported hypothesis, especially when key mechanisms are only indirectly observed (39). Algorithms such as Approximate Bayesian Computation, Markov Chain Monte Carlo, and machinelearning-based emulators can be used to align model output with observed data and to assess the robustness of conclusions. This makes MBHT particularly well suited for dynamic systems such as pathogen evolution, where feedbacks between transmission, immunity, and intervention strategies create complex adaptive and co-evolutionary dynamics that may not be adequately captured by standard statistical tests. Figure 1 summarizes the typical workflow for applying MBHT to ecological and evolutionary systems or other complex dynamical settings. First, competing hypotheses are formulated on the basis of a comprehensive literature review and supplemented with data from relevant repositories. To test these hypotheses, a compartmental disease model is constructed, analyzed using standard mathematical tools, and simulated by sampling parameter values from specified prior ranges.

### [15] SARS-CoV-2 Mac1 is required for IFN antagonism and efficient virus replication in cell culture and in mice
- Authors: Yousef M. O. Alhammad, Srivatsan Parthasarathy, Roshan Ghimire, Catherine M. Kerr, J. O'Connor et al.
- Year: 2023
- Venue: Proceedings of the National Academy of Sciences of the United States of America
- URL: https://www.semanticscholar.org/paper/4b95ed83758a296de204a9e74691af9fcbc4b92c
- DOI: 10.1073/pnas.2302083120
- PMID: 37607224
- PMCID: 10468617
- Citations: 43
- Influential citations: 2
- Summary: It is found that SARS-CoV-2 containing a complete Mac1 deletion replicates normally in cell culture but induces an elevated IFN response, has reduced viral loads in vivo, and does not cause significant disease in mice.
- Evidence snippets:
  - Snippet 1 (score: 0.490)
    > In the cases of E protein and nsp15, the viruses that replicate normally in the absence of these proteins have additional accessory proteins that have overlapping or redundant functions. For instance, the 4a and 4b MERS-CoV proteins were found to have redundant functions with nsp15 in blocking the innate immune response to infection (57). We hypothesize that the Sarbecoviruses may have evolved unique accessory proteins or other domains in the nonstructural proteins that have redundant functions with Mac1 in promoting viral replication. One intriguing hypothesis is that one or both of the additional macrodomains in Sarbecoviruses (Mac2/Mac3) may functionally compensate for the loss of Mac1, even though they do not share the same biochemical functions. Efforts to identify proteins that can functionally compensate for Mac1 are ongoing. Regardless, we and others have found that Mac1 is critical for CoVs to replicate efficiently and cause disease in all animal models of infection that have been tested (Fig. 5) (18,26,31).
    > Mac1 is only a small domain within nsp3, but there is the potential for a complete deletion to impact other domains within nsp3, including PLpro. Previously, it was shown in MHV that PLP2 can interact with Mac1, and mutations in Mac1 outside of the ADP-ribose binding pocket were found to have a temperaturedependent phenotype (58). However, PLpro is essential for polyprotein processing and virus replication, but here, we found that there was no defect in nsp3 staining or in the replication of ΔMac1 in Vero E6 and A549 cells, and only a modest defect in Calu-3 cells. In addition, the phenotypes we observed, including increased IFN production, have previously been observed following Mac1 point mutant virus infection with SARS-CoV and MHV (18,32). We have also demonstrated that these phenotypes in MHV can be reversed with PARP inhibitors or siRNAs (32).

### [16] Strategies to identify candidate repurposable drugs: COVID-19 treatment as a case example
- Authors: A. Imami, Robert E. Mccullumsmith, S. O’Donovan
- Year: 2021
- Venue: Translational Psychiatry
- URL: https://www.semanticscholar.org/paper/b4ae909dde0722a51145d2f7ff696e60cc99b17d
- DOI: 10.1038/s41398-021-01724-w
- PMID: 34785660
- PMCID: 8594646
- Citations: 9
- Summary: This work discusses examples of machine-learning and signature-based approaches that have been adapted to rapidly identify candidate drugs in the development and use of bioinformatic tools to identify candidate repurposable drugs for CNS disorders.
- Evidence snippets:
  - Snippet 1 (score: 0.483)
    > Even in the case of COVID-19, where we have knowledge of the causative pathogen and sufficient understanding of the molecular mechanisms of infection to identify the viral proteins that can be targeted to inhibit viral replication, development of approved treatments is a challenge. For CNS diseases, a major stumbling block to the identification of effective therapies remains our limited understanding of the etiology of these disorders. The heterogeneity and complexity of CNS disorders undoubtedly contributes to the very low rates of clinical approval of new drugs, which often fail in clinical trials due to a lack of efficacy [77]. For drugs that attempt to treat the causes of neurodegenerative diseases like Alzheimer's disease and Parkinson's disease, the clinical failure rate has been high [78]. The shortcomings of animal models [79] and difficulties in designing drugs that have the physiochemical properties to be successfully delivered across the blood brain barrier are other limiting factors [80]. The challenges to successful drug discovery and drug repurposing in the CNS have been reviewed in detail elsewhere [78, [81][82][83][84].
    > A standard approach to discover new drugs, high-throughput screening to identify compounds that show activity against a single target or pathway, has resulted in diminishing success over the years [85], and has been particularly limited for brain-related disorders. For example, for Alzheimer's disease the "amyloid hypothesis" led to the identification of a target pathological pathway and a search for drugs that can inhibit beta-amyloid aggregation. This has not resulted in successful disease-modifying treatment [86]. Drug repositioning using signature-based and machine-learning approaches offers an alternative strategy for drug identification for brain-related disorders, which to date has primarily relied on serendipitous findings [87] and incremental improvements of existing drugs for treatment [78].
    > Signature-based strategies are already identifying promising drug leads for different brain disorders.

### [17] Extracting a Knowledge Base of Mechanisms from COVID-19 Papers
- Authors: Aida Amini, Tom Hope, David Wadden, Madeleine van Zuylen, E. Horvitz et al.
- Year: 2020
- Venue: ArXiv
- URL: https://www.semanticscholar.org/paper/c4ce6aca9aed41d57d588674484932e0c2cd3547
- DOI: 10.18653/V1/2021.NAACL-MAIN.355
- Citations: 31
- Influential citations: 2
- Summary: This work pursues the construction of a knowledge base of mechanisms—a fundamental concept across the sciences, which encompasses activities, functions and causal relations, ranging from cellular processes to economic impacts, by developing a broad, unified schema.
- Evidence snippets:
  - Snippet 1 (score: 0.480)
    > We show how our system can be used to search for mechanism relations across a KB of 2M functional relations, and evaluate its utility in two search applications: Studying the viral mechanisms of SARS-CoV-2, and discovering medical applications of AI in the literature. Targeted biomedical search. This task involves searching for SARS-CoV-2 mechanism relations focused on a specific well-known statement or question regarding the virus (e.g., SARS-CoV-2 binds ACE2 receptor to gain entry into cells). Table 4: Human evaluation stats for our predictions vs. baseline SRL. We note that human evaluation scores are considerably higher than captured by our automated metrics wrt ground truth annotations, yet still correlated with them -indicating their usefulness in this challenging setting.
    > In this scenario, we issue queries which specify both the subject and the object of a mechanism relation (e.g., for a given relation (s 1 = SARS-CoV-2, s 2 = binds ACE2 receptor), retrieve relations where s * 1 is relevant/similar to "SARS-CoV-2" and s * 2 relevant to "binds ACE2 receptor"). This task is designed to test our framework's ability to support researchers looking to quickly generate a list of relations pertaining to a specific hypothesis. Open-ended cross-domain search. This task is focused on discovering diverse ways in which AI research areas or methods are applied in the CORD-19 corpus. Unlike the previous scenario, here evaluators are given queries where only the subject of the relation is specified, s 1 -with queries consisting of popular, leading subfields and methods within AI (e.g., deep reinforcement learning or text analysis). The aim of this task is to evaluate whether we can support exploratory search over relations, potentially surfacing inspirations for new applications of AI against COVID-19, or helping biomedical researchers and practitioners discover where AI methods are being used. Task Setup and Evaluation In both tasks, our goal is to see if we can retrieve relevant relations that expert annotators consider useful and correct. To evaluate these tasks, we re-   Table 5 shows examples from the two tasks.

## Notes

- This provider combines `search_papers_by_relevance` with `snippet_search`.
- No synthesis or second-stage model call is performed.
