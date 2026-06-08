---
provider: asta
model: Asta Scientific Corpus Retrieval
cached: false
start_time: '2026-05-26T23:06:32.077859'
end_time: '2026-05-26T23:06:35.565921'
duration_seconds: 3.49
template_file: templates/disease_pathophysiology_research_asta.md
template_variables:
  disease_name: COVID-19
  mondo_id: ''
  category: ''
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
citation_count: 20
---

## Question

Pathophysiology and clinical mechanisms of COVID-19. Core disease mechanisms, molecular and cellular pathways, involved genes and proteins, relevant metabolites or drugs, affected cell types and anatomical structures, disease progression, major clinical phenotypes and complications, and treatment-relevant mechanism papers.

## Output

# Asta Literature Retrieval: Pathophysiology and clinical mechanisms of COVID-19. Core disease mechanisms, molecular and cellular pathways, involv...

This report is retrieval-only and is generated directly from Asta results.

- Papers retrieved: 20
- Snippets retrieved: 20

## Relevant Papers

### [1] The COVID-19 puzzle: deciphering pathophysiology and phenotypes of a new disease entity
- Authors: M. Osuchowski, M. Winkler, T. Skirecki, S. Cajander, M. Shankar-Hari et al.
- Year: 2021
- Venue: The Lancet. Respiratory Medicine
- URL: https://www.semanticscholar.org/paper/4f3205544946f019893e40368b1369047effb80f
- DOI: 10.1016/S2213-2600(21)00218-6
- PMID: 33965003
- PMCID: 8102044
- Citations: 378
- Influential citations: 12
- Summary: Evidence for many distinctive mechanistic features indicates that COVID-19 constitutes a new disease entity, with emerging data suggesting involvement of an endotheliopathy-centred pathophysiology.
- Evidence snippets:
  - Snippet 1 (score: 0.740)
    > The zoonotic SARS-CoV-2 virus that causes COVID-19 continues to spread worldwide, with devastating consequences. While the medical community has gained insight into the epidemiology of COVID-19, important questions remain about the clinical complexities and underlying mechanisms of disease phenotypes. Severe COVID-19 most commonly involves respiratory manifestations, although other systems are also affected, and acute disease is often followed by protracted complications. Such complex manifestations suggest that SARS-CoV-2 dysregulates the host response, triggering wide-ranging immuno-inflammatory, thrombotic, and parenchymal derangements. We review the intricacies of COVID-19 pathophysiology, its various phenotypes, and the anti-SARS-CoV-2 host response at the humoral and cellular levels. Some similarities exist between COVID-19 and respiratory failure of other origins, but evidence for many distinctive mechanistic features indicates that COVID-19 constitutes a new disease entity, with emerging data suggesting involvement of an endotheliopathy-centred pathophysiology. Further research, combining basic and clinical studies, is needed to advance understanding of pathophysiological mechanisms and to characterise immuno-inflammatory derangements across the range of phenotypes to enable optimum care for patients with COVID-19.

### [2] Beyond dexamethasone, emerging immuno‐thrombotic therapies for COVID‐19
- Authors: M. Jensen, M. George, D. Gilroy, R. Sofat
- Year: 2020
- Venue: British Journal of Clinical Pharmacology
- URL: https://www.semanticscholar.org/paper/abe737ee4f8371568804e4bc37a89d81d53f50e9
- DOI: 10.1111/bcp.14540
- PMID: 32881064
- Citations: 7
- Summary: The pathophysiological mechanisms underpinning these cascades are reviewed with clinical correlates and the current therapeutic approaches being investigated to formulating rationale therapeutic approaches beyond the use of dexamethasone.
- Evidence snippets:
  - Snippet 1 (score: 0.618)
    > By reviewing what is known about the clinical and molecular pathophysiology of COVID-19 we have outlined a framework to understand existing therapeutic endeavours. Rational efforts to repurpose existing drugs can be understood in the context of the molecular pathways outlined-from upstream targets (entry via ACE2 or viral replication) to downstream targets (modulating the hyperinflammatory state and/or the coagulopathy). We therefore propose that 1 therapeutic approach could be viral clearance by either small molecular entities or preventative approaches when vaccines are available. However, advanced cases where immunological and thrombotic complications are present may require a combination approach, targeting both viral clearance and adjunctive treatment to address the key complications of serious infection (hyperinflammation and coagulopathy). The benefit of antivirals as adjunctive treatments in severe COVID-19 requires a better understanding of the degree to which viral persistence contributes to deterioration, requiring further studies exploring the relationship between viral RNA load kinetics and disease severity.
    > To move forward, it is essential to analyse the clinical phenotypes by collecting data on patient demographics, comorbidities, medication history, disease severity, and progression towards surrogate and clinical endpoints. We also require detailed laboratory data, including virology parameters (viral load, acute and convalescent serology) and inflammatory markers (including cytokine profiling), ideally with both real-time systemic and intrapulmonary monitoring. Genome-wide association studies, RNA and proteomic analyses will be crucial in evaluating the pathogenic mechanism behind intrinsic risk factors (for example sex and ethnicity), and approaches including Mendelian randomisation may steer towards causal pathways prioritising drugs for repurposing. Once the backlog of coronial autopsies is processed, research autopsies on COVID-19 positive patients must be prioritised.
    > The histology from postmortem studies, as well as the cytopathology from bronchoalveolar lavage, will be crucial in elucidating the mechanisms of mortality. Across all of these data domains, large cohorts will need to be analysed before conclusions can be drawn. To better understand the molecular pathways at play, efforts should also be made to elucidate the

### [3] Prediction of severe adverse events, modes of action and drug treatments for COVID-19’s complications
- Authors: C. Astore, Hongyi Zhou, Joshy Jacob, J. Skolnick
- Year: 2021
- Venue: Scientific Reports
- URL: https://www.semanticscholar.org/paper/58831d6f4f1f144c67594e2455065f0f935183a4
- DOI: 10.1038/s41598-021-00368-6
- PMID: 34675303
- PMCID: 8531388
- Citations: 4
- Summary: A novel AI methodology MOATAI-VIR, which predicts disease-protein-pathway relationships and repurposed FDA-approved drugs to treat COVID-19’s clinical manifestations was developed, and 24/26 of the major clinical manifestations are successfully predicted.
- Evidence snippets:
  - Snippet 1 (score: 0.579)
    > Following SARS-CoV-2 infection, some COVID-19 patients experience severe host driven adverse events. To treat these complications, their underlying etiology and drug treatments must be identified. Thus, a novel AI methodology MOATAI-VIR, which predicts disease-protein-pathway relationships and repurposed FDA-approved drugs to treat COVID-19’s clinical manifestations was developed. SARS-CoV-2 interacting human proteins and GWAS identified respiratory failure genes provide the input from which the mode-of-action (MOA) proteins/pathways of the resulting disease comorbidities are predicted. These comorbidities are then mapped to their clinical manifestations. To assess each manifestation’s molecular basis, their prioritized shared proteins were subject to global pathway analysis. Next, the molecular features associated with hallmark COVID-19 phenotypes, e.g. unusual neurological symptoms, cytokine storms, and blood clots were explored. In practice, 24/26 of the major clinical manifestations are successfully predicted. Three major uncharacterized manifestation categories including neoplasms are also found. The prevalence of neoplasms suggests that SARS-CoV-2 might be an oncovirus due to shared molecular mechanisms between oncogenesis and viral replication. Then, repurposed FDA-approved drugs that might treat COVID-19’s clinical manifestations are predicted by virtual ligand screening of the most frequent comorbid protein targets. These drugs might help treat both COVID-19’s severe adverse events and lesser ones such as loss of taste/smell.

### [4] Immune and Metabolic Signatures of COVID-19 Revealed by Transcriptomics Data Reuse
- Authors: L. Gardinassi, C. O. Souza, Helioswilton Sales-Campos, S. Fonseca
- Year: 2020
- Venue: Frontiers in Immunology
- URL: https://www.semanticscholar.org/paper/88b6bf5f42d644dbb591a33e5733b65220ff4b88
- DOI: 10.3389/fimmu.2020.01636
- PMID: 32670298
- PMCID: 7332781
- Citations: 108
- Influential citations: 5
- Summary: Results indicate higher expression of genes related to oxidative phosphorylation both in peripheral mononuclear leukocytes and BALF, suggesting a critical role for mitochondrial activity during SARS-CoV-2 infection.
- Evidence snippets:
  - Snippet 1 (score: 0.565)
    > The current pandemic of coronavirus disease 19 (COVID-19) has affected millions of individuals and caused thousands of deaths worldwide. The pathophysiology of the disease is complex and mostly unknown. Therefore, identifying the molecular mechanisms that promote progression of the disease is critical to overcome this pandemic. To address such issues, recent studies have reported transcriptomic profiles of cells, tissues and fluids from COVID-19 patients that mainly demonstrated activation of humoral immunity, dysregulated type I and III interferon expression, intense innate immune responses and inflammatory signaling. Here, we provide novel perspectives on the pathophysiology of COVID-19 using robust functional approaches to analyze public transcriptome datasets. In addition, we compared the transcriptional signature of COVID-19 patients with individuals infected with SARS-CoV-1 and Influenza A (IAV) viruses. We identified a core transcriptional signature induced by the respiratory viruses in peripheral leukocytes, whereas the absence of significant type I interferon/antiviral responses characterized SARS-CoV-2 infection. We also identified the higher expression of genes involved in metabolic pathways including heme biosynthesis, oxidative phosphorylation and tryptophan metabolism. A BTM-driven meta-analysis of bronchoalveolar lavage fluid (BALF) from COVID-19 patients showed significant enrichment for neutrophils and chemokines, which were also significant in data from lung tissue of one deceased COVID-19 patient. Importantly, our results indicate higher expression of genes related to oxidative phosphorylation both in peripheral mononuclear leukocytes and BALF, suggesting a critical role for mitochondrial activity during SARS-CoV-2 infection. Collectively, these data point for immunopathological features and targets that can be therapeutically exploited to control COVID-19.

### [5] Severe Acute Respiratory Syndrome Coronavirus 2: From Gene Structure to Pathogenic Mechanisms and Potential Therapy
- Authors: Jun Wu, Xiaohui Yuan, Bing Wang, Rui Gu, Wei Li et al.
- Year: 2020
- Venue: Frontiers in Microbiology
- URL: https://www.semanticscholar.org/paper/699c43b38b76cbd7ff08dc13dd2d8ca2eb1577ee
- DOI: 10.3389/fmicb.2020.01576
- PMID: 32719672
- PMCID: 7347906
- Citations: 38
- Influential citations: 2
- Summary: The correlations among gene structure, protein function, and pathogenic mechanisms of SARS-CoV-2 are refined and potential therapeutic targets are discussed, aiming to accelerate the advanced design and development of vaccines and therapeutic drugs against COVID-19.
- Evidence snippets:
  - Snippet 1 (score: 0.554)
    > be developed to prevent and treat COVID-19 and reduce the serious impact on human beings. For this purpose, detailed information about the pathogenesis of COVID-19 at the cellular and molecular levels is urgently needed. In this review, we summarized the current understanding of gene structure, protein function and pathogenic mechanisms of SARS-CoV-2, Based on the above, we refined the correlations among gene structure, protein function, and pathogenic mechanisms of SARS-CoV-2. Importantly, we further discussed potential therapeutic targets, aiming to accelerate the advanced design and development of vaccines and therapeutic drugs against COVID-19.

### [6] Classification of the present pharmaceutical agents based on the possible effective mechanism on the COVID-19 infection
- Authors: Maryam Amini Pouya, Seyyedeh Maryam Afshani, A. Maghsoudi, S. Hassani, K. Mirnia
- Year: 2020
- Venue: DARU Journal of Pharmaceutical Sciences
- URL: https://www.semanticscholar.org/paper/ecb046c2539c2490d1b1b37d7f936fe278b2e6f1
- DOI: 10.1007/s40199-020-00359-4
- PMID: 32734518
- PMCID: 7391927
- Citations: 13
- Influential citations: 2
- Summary: The present review has aimed to gather and categorize all implemented drugs based on the susceptible virulence mechanisms, and the pathophysiological events in the host cells, discussing and suggesting treatments.
- Evidence snippets:
  - Snippet 1 (score: 0.553)
    > There are several types of research on the COVID-19 disease which have been conducting. It seems that prevailing over the pandemic would be achieved only by mastering over the virus pathophysiology. We tried to categorize the massive amount of available information for useful interpretation. We searched databases with different keywords and search strategies that focus on virulence and pathophysiology of COVID-19. The present review has aimed to gather and categorize all implemented drugs based on the susceptible virulence mechanisms, and the pathophysiological events in the host cells, discussing and suggesting treatments. As a result, the COVID-19 lifecycle were categorized as following steps: “Host Cell Attachment” which is mainly conducted with ACE2 receptors and TMPRSS2 from the host cell and Spike (S) protein, “Endocytosis Pathway” which is performed mainly by clathrin-mediated endocytosis, and “Viral Replication” which contains translation and replication of RNA viral genome. The virus pathogenicity is continued by “Inflammatory Reactions” which mainly caused moderate to severe COVID-19 disease. Besides, the possible effective therapeutics’ mechanism and the pharmaceutical agents that had at least one experience as a preclinical or clinical study on COVID-19 were clearly defined. The treatment protocol would be occasional based on the stage of the infection and the patient situation. The cocktail of medicines, which could affect almost all mentioned stages of COVID-19 disease, might be vital for patients with severe phenomena. The classification of the possible mechanism of medicines based on COVID-19 pathogenicity The classification of the possible mechanism of medicines based on COVID-19 pathogenicity

### [7] Multi-omics approach to COVID-19: a domain-based literature review
- Authors: C. Montaldo, F. Messina, I. Abbate, M. Antonioli, V. Bordoni et al.
- Year: 2021
- Venue: Journal of Translational Medicine
- URL: https://www.semanticscholar.org/paper/0c7804617654881ff5b118da3e412f1a4b3339c4
- DOI: 10.1186/s12967-021-03168-8
- PMID: 34876157
- PMCID: 8649311
- Citations: 17
- Influential citations: 1
- Summary: The analysis revealed that dysregulated pathways of innate immune responses can affect COVID-19 progression and outcomes, and multi-omics approach may help to further investigate unknown aspects of the disease.
- Evidence snippets:
  - Snippet 1 (score: 0.551)
    > Omics data, driven by rapid advances in laboratory techniques, have been generated very quickly during the COVID-19 pandemic. Our aim is to use omics data to highlight the involvement of specific pathways, as well as that of cell types and organs, in the pathophysiology of COVID-19, and to highlight their links with clinical phenotypes of SARS-CoV-2 infection. The analysis was based on the domain model, where for domain it is intended a conceptual repository, useful to summarize multiple biological pathways involved at different levels. The relevant domains considered in the analysis were: virus, pathways and phenotypes. An interdisciplinary expert working group was defined for each domain, to carry out an independent literature scoping review. The analysis revealed that dysregulated pathways of innate immune responses, (i.e., complement activation, inflammatory responses, neutrophil activation and degranulation, platelet degranulation) can affect COVID-19 progression and outcomes. These results are consistent with several clinical studies. Multi-omics approach may help to further investigate unknown aspects of the disease. However, the disease mechanisms are too complex to be explained by a single molecular signature and it is necessary to consider an integrated approach to identify hallmarks of severity.

### [8] Cutaneous Manifestations in Patients With COVID-19: Clinical Characteristics and Possible Pathophysiologic Mechanisms
- Authors: F. González, C. Correa, E. Contreras, R. Agudo, Severo
- Year: 2020
- Venue: Actas Dermo-Sifiliograficas
- URL: https://www.semanticscholar.org/paper/979d18b1f483a260b011a536cc10bb7dfae9629f
- DOI: 10.1016/j.adengl.2021.01.024
- PMID: 34012165
- PMCID: 7843072
- Citations: 30
- Influential citations: 1
- Summary: Graphical Abstract
- Evidence snippets:
  - Snippet 1 (score: 0.544)
    > The COVID-19 pandemic has created enormous challenges for health care professionals, including the need to keep abreast with the vast spectrum of clinical manifestations associated with this disease. COVID-19 is a multisystemic disease that affects multiple organs, including the skin. The occurrence of cutaneous manifestations, however, represents an advantage, as their recognition can lead to early suspicion of disease in some cases and provide clues about individual immune responses or complications in others.
    > Based on the pathophysiological mechanisms hypothesized, we propose classifying the various cutaneous manifestations of COVID-19 into 2 groups: 1) manifestations primarily linked to a direct cytopathogenic effect on cells such as keratinocytes, which are involved in many known viral infections (morbilliform or urticarial rashes, reactions similar to drug eruptions, varicella-like lesions) and 2) manifestations linked to an uncontrolled release of cytokines due to alterations in specific white blood cells, such as T cells and macrophages. This second group could be divided into a further 2 groups: 1) manifestations characterized by features similar to those seen in macrophage activation syndrome (acral ischemia, gangrene, retiform purple, livedo racemosa) and associated with poor outcomes in terms of morbidity and mortality and 2) cutaneous manifestations with a mild, self-limiting disease course, observed in young patients and linked to the activation of an early type I IFN response (chilblain-like lesions) (Fig. 7). This hypothesis is one of the first in the literature to provide a possible explanation of the pathophysiological mechanisms underlying the main cutaneous manifestations of COVID-19; it also provides a means of classifying these manifestations and establishing their possible prognostic value.
    > We believe that it is paramount for physicians, nurses, respiratory therapists, health care professionals still in training, and even members of the general population to be aware of the relationship between SARS-CoV-2 infection and the skin and its various manifestations. Heightened awareness will promote an active search for manifestations and a detailed study of cases, adding to the scientific knowledge and our understanding of the pathophysiology of COVID-

### [9] COVID-19 - toward a comprehensive understanding of the disease.
- Authors: M. Kowalik, P. Trzonkowski, Magdalena Łasińska-Kowara, A. Mital, T. Smiatacz et al.
- Year: 2020
- Venue: Cardiology journal
- URL: https://www.semanticscholar.org/paper/46589b7e2e7c45eca789a793a3aee9a6e51fc61c
- DOI: 10.5603/CJ.a2020.0065
- PMID: 32378729
- Citations: 63
- Influential citations: 5
- Summary: The current state of knowledge on COVID-19 is presented: beginning from the virus, its transmission, and mechanisms of entry into the human body, through the pathological effects on the cellular level, up to immunological reaction, systemic and organ presentation.
- Evidence snippets:
  - Snippet 1 (score: 0.520)
    > The coronavirus disease 2019 (COVID- 19) is caused by the severe acute respiratory syndrome coronavirus-2 (SARS-CoV-2) and has rapidly spread around the globe, emerging as a significant threat worldwide [1].Although evidence on the pathophysiology of COVID-19 is rapidly growing, underlying pathological mechanisms which cause some patients to get seriously sick while others experience mild symptoms, remains hitherto unexplained.Understanding the underlying pathological mechanisms of the clinical features of the disease will increase the efficacy of management strategies and subsequently prevent many fatal outcomes.
    > Herein provided, is a comprehensive view of different pathological aspects of COVID-19, potentially influencing the vulnerable development of the disease.

### [10] Deciphering SARS CoV-2-associated pathways from RNA sequencing data of COVID-19-infected A549 cells and potential therapeutics using in silico methods
- Authors: Peter Natesan Pushparaj, L. Damiati, Iuliana Denetiu, S. Bakhashab, M. Asif et al.
- Year: 2022
- Venue: Medicine
- URL: https://www.semanticscholar.org/paper/faa795a709980949db77ad58656543501119b246
- DOI: 10.1097/MD.0000000000029554
- PMID: 36107502
- PMCID: 9439635
- Citations: 2
- Summary: COVID-19 infection activated key infectious disease-specific immune-related signaling pathways such as influenza A, viral protein interaction with cytokine and cytokine receptors, measles, Epstein-Barr virus infection, and IL-17 signaling pathway.
- Evidence snippets:
  - Snippet 1 (score: 0.520)
    > COVID-19 is highly infectious and pathogenic compared to other viral infections, and the exact mortality rate has yet to be determined because the pandemic is not yet under control in several countries. [9,12] Therefore, deciphering the underlying pathologic mechanisms is central to identifying and developing COVID-19specific drugs to effectively treat and prevent person-to-person transmission, COVID-19 complications, and reduce mortality. COVID-19 is usually characterized by cough, breathing problems, high body temperature, diarrhea, and abdominal discomfort, and in severe cases, it causes atypical pneumonia, SARS, stroke, thrombosis, multiple organ failure, and in some cases, death. [3] It was found that approximately 80% of COVID-19 cases had mild or asymptomatic symptoms, with the elderly and those with other comorbid conditions more likely to develop severe symptoms and succumb to the disease. [4,9] Distinguishing COVID-19 from other influenza viruses, SARS, and MERS coronaviruses is essential in the clinical setting to develop effective or efficient treatment strategies for patients. [39] Noninfectious diseases such as idiopathic interstitial pneumonia, cryptogenic organizing pneumonia, dermatomyositis, and vasculitis also need to be differentially diagnosed from COVID-19 [7,9,39] The COVID -19 infection of A549 cells activated upstream genes, such as STAT2, IRF9, IFNB1, IL1B, and IRF3. Biological processes such as the type I interferon signaling pathway, defense response to viruses, negative regulation of viral genome replication, and interferon-gamma-mediated signaling pathways were differentially regulated. Molecular functions such as chemokine activity, CXCR chemokine receptor binding, 2ʹ-5ʹ-oligoadenylate synthetase activity, double-stranded RNA binding, and protein ADP-ribosylase activity were enriched in the COVIDinfected cells. Cytokines are hormones of the immune system that are important for innate and adaptive host responses, cell growth and differentiation, repair and development, cellular homeostasis, and cell death. [35,40,41] Cytok

### [11] Landscape of Molecular Crosstalk Perturbation between Lung Cancer and COVID-19
- Authors: Aditi Kuchi, Jiande Wu, J. Fuloria, C. Hicks
- Year: 2022
- Venue: International Journal of Environmental Research and Public Health
- URL: https://www.semanticscholar.org/paper/9094685853a78a21c392c5aed65c33e8896a6671
- DOI: 10.3390/ijerph19063454
- PMID: 35329141
- PMCID: 8953719
- Citations: 5
- Summary: A signature of genes associated with both diseases and signatures of genes uniquely associated with each disease are revealed, confirming crosstalk in molecular perturbation between COVID-19 and lung cancer.
- Evidence snippets:
  - Snippet 1 (score: 0.518)
    > Some of the major challenges in clinical management of COVID-19 include extrapulmonary manifestations of the disease and its effects on multiple organs, including the lungs [40][41][42]. Extrapulmonary manifestations include thrombotic complications, myocardial dysfunction and arrhythmia, acute coronary disease syndromes, acute kidney injury, gastrointestinal symptoms, hepatocellular injury, hyperglycemia and ketosis, neurologic illnesses, ocular symptoms and dermatologic complications [40][41][42][43]. Although we did not investigate the association of the discovered genes with extrapulmonary manifestations in COVID-19, the discovery of genes with multiple overlapping functions involved in many biological processes suggests that some of the identified genes and gene regulatory networks may be involved in extrapulmonary activities. Moreover, the lung as an organ is likely to function in unison with other organs. Under such conditions, the effects of COVID-19 on the lungs have potential to trigger a cascade of events likely to affect other organs and lead to extrapulmonary manifestations. Indeed, lungs as organs contain many cells that can play many different roles. Although we did not examine individual lung cells, previous studies have shown that transcription profiling could reveal novel mechanisms of SARS-CoV-2 infection in human lung cells [44,45].
    > Another finding of significance in this investigation was the discovery of gene regulatory networks and signaling pathways associated with both diseases. This suggests that the host-pathogen interactions linking the two diseases are complex. The novel as-pect and clinical significance of this finding is that it could increase our understanding of host-pathogen interactions, a critical step in vaccine and drug development [46]. For example, the discovery of the coronavirus pathogenesis signaling pathway in this study has the promise to increase our understanding of the pathogenesis of COVID-19 and the molecular mechanisms driving the disease. Although signatures of genes associated with COVID-19 have been reported [17,21], molecular crosstalk perturbation between COVID-19 and lung cancer has not been reported.

### [12] COVID-19: Current understanding of its Pathophysiology, Clinical presentation and Treatment
- Authors: A. Parasher
- Year: 2020
- Venue: Postgraduate Medical Journal
- URL: https://www.semanticscholar.org/paper/93f5e6826aef71d8b0000b561e699024f3e67e1d
- DOI: 10.1136/postgradmedj-2020-138577
- PMID: 32978337
- PMCID: 10017004
- Citations: 621
- Influential citations: 31
- Summary: An update on the pathophysiology, clinical presentation and the most recent management strategies for COVID-19 has been described, with pharmaceutical corporations having started human trials in many countries.
- Evidence snippets:
  - Snippet 1 (score: 0.515)
    > Although much has been discovered regarding the transmission and presentation, less is known about the pathophysiology of COVID-19. An overview of the disease pathophysiology has been shown in figure 2. 6 22 23

### [13] Integrated Transcriptomic Analysis Reveals Reciprocal Interactions between SARS-CoV-2 Infection and Multi-Organ Dysfunction, Especially the Correlation of Renal Failure and COVID-19
- Authors: Pai Li, Meng Liu, W. He
- Year: 2024
- Venue: Life
- URL: https://www.semanticscholar.org/paper/eec0afd79dfca7dd7d09deb6ef8a607160a9b493
- DOI: 10.3390/life14080960
- PMID: 39202702
- PMCID: 11355357
- Citations: 3
- Summary: An integrated transcriptomic analysis to investigate the effects of SARS-CoV-2 on various organs, with a particular focus on the relationship between renal failure and COVID-19 revealed that COVID-19 patients with renal failure exhibited lower metabolic activity in lung epithelial and B cells, with reduced ligand–receptor interactions, suggesting a compromised immune response.
- Evidence snippets:
  - Snippet 1 (score: 0.514)
    > Transcriptional dysregulation always leads to various pathological phenotypes. Herein, we used DisGeNET to predict the potential associations between hub genes and other complications. Interestingly, apart from respiratory defects, we observed a consistent enrichment of brain cancers related diseases such as glioblastoma and ganglioglioma across these organs (Table S4). Clinical studies have reported that 80% of COVID-19 hospitalized patients had neurological symptoms and predominant manifestations including acute encephalopathy, coma, and stroke. It is demonstrated that SARS-CoV-2 could potentially damage the brain in multiple ways. The virus is capable of attacking specific brain cells, reducing the blood supply to brain tissue, and inducing the production of immune molecules that damage brain cells [60]. However, further studies should be performed to investigate the consequences of COVID-related brain damage. Furthermore, diseases related to the digestive system have also been documented in these organs, such as esophagus diseases, hyperinsulinism, and neoplasms of the stomach and colon. It is reported that more than half of COVID-19 patients are at a higher risk of developing hyperglycemia, and approximately 33% of patients developed diabetic ketoacidosis [61,62]. However, there is limited study on the impact of COVID-19 on the other digestive organs. Prolonged clinical observation is crucial in refining medical strategies, enhancing patient care, and ultimately mitigating the impact of the pandemic.
    > Currently, effective drug treatment for COVID-19 treatment is still limited. Clinical trials have indicated that remdesivir is effective in reducing the recovery time and mitigating respiratory tract infection for hospitalized COVID-19 adults. The mechanism of remdesivir is suppressing the viral RNA-dependent RNA polymerase (RdRp) [63]. Herein, we predicted potential drugs based on the hub genes from different datasets (Table S5). Mechanistically, these drugs can either attenuate inflammation or impede viral entry, representing strategic approaches in new drug design.

### [14] Pathophysiology of acute respiratory syndrome coronavirus 2 infection: a systematic literature review to inform EULAR points to consider
- Authors: A. Najm, A. Alunno, X. Mariette, B. Terrier, G. de Marco et al.
- Year: 2021
- Venue: RMD Open
- URL: https://www.semanticscholar.org/paper/717fa55739f281a20c8b9e0181868819d9a628c1
- DOI: 10.1136/rmdopen-2020-001549
- PMID: 33574116
- PMCID: 7880117
- Citations: 16
- Summary: SARS-CoV-2 infection affects both humoral and cellular immunity depending on both disease severity and individual parameters, which informed the EULAR ‘points to consider’ on COVID-19 pathophysiology and immunomodulatory therapies.
- Evidence snippets:
  - Snippet 1 (score: 0.514)
    > Background The SARS-CoV-2 pandemic is a global health problem. Beside the specific pathogenic effect of SARS-CoV-2, incompletely understood deleterious and aberrant host immune responses play critical roles in severe disease. Our objective was to summarise the available information on the pathophysiology of COVID-19. Methods Two reviewers independently identified eligible studies according to the following PICO framework: P (population): patients with SARS-CoV-2 infection; I (intervention): any intervention/no intervention; C (comparator): any comparator; O (outcome) any clinical or serological outcome including but not limited to immune cell phenotype and function and serum cytokine concentration. Results Of the 55 496 records yielded, 84 articles were eligible for inclusion according to question-specific research criteria. Proinflammatory cytokine expression, including interleukin-6 (IL-6), was increased, especially in severe COVID-19, although not as high as other states with severe systemic inflammation. The myeloid and lymphoid compartments were differentially affected by SARS-CoV-2 infection depending on disease phenotype. Failure to maintain high interferon (IFN) levels was characteristic of severe forms of COVID-19 and could be related to loss-of-function mutations in the IFN pathway and/or the presence of anti-IFN antibodies. Antibody response to SARS-CoV-2 infection showed a high variability across individuals and disease spectrum. Multiparametric algorithms showed variable diagnostic performances in predicting survival, hospitalisation, disease progression or severity, and mortality. Conclusions SARS-CoV-2 infection affects both humoral and cellular immunity depending on both disease severity and individual parameters. This systematic literature review informed the EULAR ‘points to consider’ on COVID-19 pathophysiology and immunomodulatory therapies.

### [15] Integrated transcriptomic analysis of COVID-19 stages and recovery: insights into key gene signatures, immune features, and diagnostic biomarkers through machine learning
- Authors: Zhiyuan Gong, He An
- Year: 2025
- Venue: Frontiers in Genetics
- URL: https://www.semanticscholar.org/paper/e48c08f9746d91f904034aeb536df2cdcd3a9009
- DOI: 10.3389/fgene.2025.1599867
- PMID: 40444276
- PMCID: 12119500
- Citations: 2
- Summary: This study identified CCR5, CYSLTR1, and KLRG1 as efficient diagnostic biomarkers for severe COVID-19 using machine learning and revealed immune regulatory features across COVID-19 progression and recovery.
- Evidence snippets:
  - Snippet 1 (score: 0.509)
    > The global COVID-19 pandemic, caused by the SARS-CoV-2 virus, has led to significant morbidity and mortality worldwide. Despite extensive research, the mechanisms underlying disease progression and recovery remain incompletely understood. Clinical manifestations of COVID-19 vary widely, ranging from asymptomatic cases to severe pneumonia, acute respiratory distress syndrome (ARDS), and death. Severe cases are often associated with dysregulated immune responses, including hyperinflammation and impaired adaptive immunity, which are particularly pronounced in patients requiring intensive care unit (ICU) admission (Chen et al., 2020;Wang et al., 2022;Blanco-Melo et al., 2020). While clinical scores such as the Sequential Organ Failure Assessment (SOFA) and biomarkers like C-reactive protein (CRP) are routinely used, their diagnostic efficacy in distinguishing severe cases remains limited (Herold et al., 2020;Zhou et al., 2020). There is an urgent need for precise molecular markers to improve patient stratification and inform treatment strategies.
    > Transcriptomic analysis offers a powerful approach to investigate the dynamic gene expression changes associated with disease progression and recovery. Previous studies have demonstrated that transcriptomic signatures can provide insights into the immune landscape, highlighting shifts in immune cell populations and identifying pathways involved in disease pathogenesis (Ou et al., 2024;Cappelletti et al., 2023). Immune profiling, particularly through the analysis of immune cell infiltration, can further delineate the roles of adaptive and innate immune responses in COVID-19. However, few studies have comprehensively examined the gene expression and immune regulation across the full spectrum of COVID-19 stages, from mild cases to ICU admission and through the recovery phase.
    > Recent advancements in machine learning techniques, such as LASSO regression and random forest algorithms, have enabled the identification of robust diagnostic and prognostic biomarkers from complex transcriptomic datasets (Chen and Ishwaran, 2012;Wang et al., 2024;Fan et al., 2022;Xie et al., 2024). These approaches are particularly effective in handling high-dimensional data, allowing for the identification of key genes associated with severe disease.

### [16] Neurotropism as a Mechanism of the Damaging Action of Coronavirus
- Authors: O. Gomazkov
- Year: 2022
- Venue: Biology Bulletin Reviews
- URL: https://www.semanticscholar.org/paper/4dd95df7a188cd57ea35404e71d1a90c9a813219
- DOI: 10.1134/S2079086422060044
- PMCID: 9749633
- Citations: 2
- Summary: New aspects of pathogenesis that consider the principle of neurotropism as the leading cause of SARS-CoV-2 infection and central nervous system dysfunction are outlined and additional mechanisms for coronavirus transfection are demonstrated.
- Evidence snippets:
  - Snippet 1 (score: 0.509)
    > The outbreak of the COVID-19 pandemic led to large-scale studies of the pathogenesis of this disease, which is a tricky complex of concomitant negative processes and consequences. An analysis of the clinical experience shows that pathogenesis of the respiratory distress syndrome caused by the SARS-CoV-2 virus exhibits a huge range of manifestations. These include clinical disorders of whole systems, individual organs, tissues, and biochemical reactions. COVID-19 represents a disturbance of cellular and molecular processes that gives reasons to identify pathogenic links. Diffuse alveolar lung injury with pronounced microangiopathy in the form of bilateral pneumonia is a typical clinical manifestation of COVID-19. Systemic infection is accompanied by a rapid increase in circulating chemokines and interleukins in the blood, which cross the blood-brain barrier (BBB) to enter the brain. Clinical materials indicate a variety of symptoms related to immediate or long-term neurodegenerative and mental disorders.
    > Data on the neuroinvasive potential of SARS-CoV-2 confirm damage to the structures of the brain and peripheral nervous system. A detailed understanding of the pathogenesis, and identification of cellular and biochemical targets of SARS-CoV-2 are important in order to elaborate a therapeutic anti-COVID strategy. This paper takes into account aspects of  pathogenesis that allow us to analyze the cellular and biochemical mechanisms of viral invasion leading to various forms of neurodegenerative and mental complications.
    > Neurotropism is considered a leading mechanism involved in the neurodestructive effect of SARS-CoV-2. Experimental data are a basis for interpretation of the mechanisms associated with cellular tropism of coronaviruses. In addition to the traditional consideration of ACE2 (angiotensin-converting enzyme 2) as the main transporter in coronavirus entry, we assess the involvement of other molecules (neuropilins and other proteins), which facilitate transfection and contribute to SARS-CoV-2 neurotropism. The virus entry into the brain tissue is associated with a processes wherein disturbance of the immune defense plays a leading role. Neuroinflammation with an altered phenotype of microglial cells and astrocytes results in damage to brain systems.

### [17] Prognostic Value of Serum MICA Levels as a Marker of Severity in COVID-19 Patients
- Authors: Faramarz Farzad, N. Yaghoubi, F. Azad, M. Mahmoudi, M. Mohammadi
- Year: 2021
- Venue: Immunological Investigations
- URL: https://www.semanticscholar.org/paper/3baeda34001b82bacbb92ac36e7b06320e9e32d7
- DOI: 10.1080/08820139.2022.2069035
- PMID: 35481955
- Citations: 5
- Summary: Higher serum MICA levels may be associated with respiratory failure in COVID-19 and may serve as a marker of clinical severity in patients infected with SARS-CoV-2, particularly when clinical manifestations are insufficient to make a confident prediction.
- Evidence snippets:
  - Snippet 1 (score: 0.506)
    > Severe acute respiratory syndrome coronavirus 2 (SARS-CoV-2), the causative pathogen of COVID-19 disease, continues to spread and imposes significant burdens on the public health system (Baud et al. 2020). To date, numerous studies have been conducted to incorporate novel COVID-19 biomarker testing into clinical practices to aid the global fight against COVID-19 infection's life-threatening complications (Aceti et al. 2020;Ren et al. 2020;Shen et al. 2020). A vast majority of investigations into prognostic markers for COVID-19 progression have focussed on the pathogenesis of SARS-CoV-2 infection. However, many aspects of viral pathogenicity remain unknown (Zheng et al. 2021). In general, the molecular mechanisms of COVID-19 disease include suppressed antiviral immune responses, oxidative stress, and inflammatory processes caused by excessive cytokine secretion, leading to acute lung disease, tissue fibrosis, coagulopathy, and pneumonia (Mrityunjaya et al. 2020). Given the nature of the aforementioned pathologic events, immune dysregulation may play a significant role in the progression of COVID-19 and subsequent poor disease outcomes (Fathi et al. 2020). The close connection between the immune system and the various clinical manifestations of COVID-19 also demonstrates that COVID-19 may be an immunerelated disease with viral origin and pathogenicity (Paces et al. 2020).
    > Under normal conditions, innate immune cells are the first defenders against the virus-infected cells. Indeed, early intervention of natural immunity by type I interferon (IFN-1) and natural killer (NK) cells ensures a rapid but nonspecific response to cytopathic viruses (Maggi et al. 2020). In response to tissue damage and pathogen invasion, the innate immune cells produce several pro-inflammatory cytokines, including IL-1, IL-6, TNF-α, IL-2, GM-CSF, and IFN-γ (Hosseini et al. 2020). These cytokines can promote the migration of the immune cells from the blood circulation to the infected tissues, where they trigger damage and cellular death (

### [18] Clinical-Pathological Correlation of the Pathophysiology and Mechanism of Action of COVID-19 — a Primer for Clinicians
- Authors: J. Chee, W. Loh, Zheng Liu, J. Mullol, D. Wang
- Year: 2021
- Venue: Current Allergy and Asthma Reports
- URL: https://www.semanticscholar.org/paper/8ca542721b218e91f22708c6d3d9fef5fb7bfc8e
- DOI: 10.1007/s11882-021-01015-w
- PMID: 34259961
- PMCID: 8277568
- Citations: 9
- Influential citations: 1
- Summary: This review presents a comprehensive summary of the pathophysiology of COVID-19, the mechanisms of action of the SARS-CoV-2 virus, and the correlation with the clinical and biochemical characteristics of the disease.
- Evidence snippets:
  - Snippet 1 (score: 0.505)
    > Clinical-Pathological Correlation of the Pathophysiology and Mechanism of Action of COVID-19 — a Primer for Clinicians

### [19] Decoding the interplay between COVID-19 and diabetic nephropathy through bioinformatics and systems biology techniques
- Authors: Xianxiang Chen, Qingle Zeng, M. Xia, Yufen J. Chen
- Year: 2025
- Venue: Biochemistry and Biophysics Reports
- URL: https://www.semanticscholar.org/paper/7a3c484b8ab8bcd1157016380199c507ff06fb38
- DOI: 10.1016/j.bbrep.2025.102366
- PMID: 41332907
- PMCID: 12666057
- Citations: 1
- Summary: Shared molecular pathways and hub genes between COVID-19 and DN are revealed, providing insights into immune dysregulation and tissue injury mechanisms and underscore the value of integrative bioinformatics in guiding precision medicine approaches for complex disease interactions.
- Evidence snippets:
  - Snippet 1 (score: 0.503)
    > Aims Individuals with diabetic nephropathy (DN), a major diabetic complication, have been disproportionately affected by the coronavirus disease 2019 (COVID-19) pandemic. This study aimed to investigate the molecular interplay between COVID-19 and DN using bioinformatics and systems biology approaches to identify shared mechanisms and therapeutic targets for their improved synergistic clinical management. Methods Transcriptomic datasets (COVID-19, GSE171110; DN, GSE30528) were analyzed to identify differentially expressed genes (DEGs). Additionally, functional enrichment, protein-protein interaction (PPI) networks, transcription factor (TF)–microRNA (miRNA) regulatory networks, and drug-gene associations were explored. The diagnostic potential of hub genes was validated using receiver operating characteristic curves. Results In total, 3975 DEGs (2796 upregulated; 1179 downregulated) were identified in patients with COVID-19 versus controls, and 348 DEGs (93 upregulated; 255 downregulated) were found in patients with DN. Among them, 83 DEGs overlapped, presenting shared molecular pathways, including hematopoietic cell lineage, focal adhesion, and complement/coagulation cascades. PPI analysis revealed five major hub genes (IL7R, CD2, GZMA, CD3D, and FCER1A) associated with immune regulation and tissue injury, and regulatory network analysis identified 46 TFs and 88 miRNAs interacting with them. Based on transcriptomic signatures, drug repurposing candidates, such as alpha-d-mannose, aspirin, and methotrexate, were identified. Additionally, hub genes showed a high diagnostic potential (area under the curve >0.80 for COVID-19 and DN). Finally, we use external datasets to validate hub genes. Conclusions The findings of this study reveal shared molecular pathways and hub genes between COVID-19 and DN, providing insights into immune dysregulation and tissue injury mechanisms. Strategies associated with identified biomarkers and therapeutic candidates, including interleukin-7 receptor-targeting strategies, offer the potential for improving clinical

### [20] Bioinformatics and system biology approaches to identify pathophysiological impact of COVID-19 to the progression and severity of neurological diseases
- Authors: Md. Habibur Rahman, Humayan Kabir Rana, Silong Peng, Md Golam Kibria, Md Zahidul Islam et al.
- Year: 2021
- Venue: Computers in Biology and Medicine
- URL: https://www.semanticscholar.org/paper/77e343dc18ecfebde09640a81b5c56b22557bbf2
- DOI: 10.1016/j.compbiomed.2021.104859
- PMID: 34601390
- PMCID: 8483812
- Citations: 31
- Summary: This research investigated how COVID-19 and ND interact and the impact of CO VID-19 on the severity of NDs by performing transcriptomic analyses of COVID and NDs samples by developing the pipeline of bioinformatics and network-based approaches.
- Evidence snippets:
  - Snippet 1 (score: 0.502)
    > The Coronavirus Disease 2019 (COVID-19) still tends to propagate and increase the occurrence of COVID-19 across the globe. The clinical and epidemiological analyses indicate the link between COVID-19 and Neurological Diseases (NDs) that drive the progression and severity of NDs. Elucidating why some patients with COVID-19 influence the progression of NDs and patients with NDs who are diagnosed with COVID-19 are becoming increasingly sick, although others are not is unclear. In this research, we investigated how COVID-19 and ND interact and the impact of COVID-19 on the severity of NDs by performing transcriptomic analyses of COVID-19 and NDs samples by developing the pipeline of bioinformatics and network-based approaches. The transcriptomic study identified the contributing genes which are then filtered with cell signaling pathway, gene ontology, protein-protein interactions, transcription factor, and microRNA analysis. Identifying hub-proteins using protein-protein interactions leads to the identification of a therapeutic strategy. Additionally, the incorporation of comorbidity interactions score enhances the identification beyond simply detecting novel biological mechanisms involved in the pathophysiology of COVID-19 and its NDs comorbidities. By computing the semantic similarity between COVID-19 and each of the ND, we have found gene-based maximum semantic score between COVID-19 and Parkinson's disease, the minimum semantic score between COVID-19 and Multiple sclerosis. Similarly, we have found gene ontology-based maximum semantic score between COVID-19 and Huntington disease, minimum semantic score between COVID-19 and Epilepsy disease. Finally, we validated our findings using gold-standard databases and literature searches to determine which genes and pathways had previously been associated with COVID-19 and NDs.

## Notes

- This provider combines `search_papers_by_relevance` with `snippet_search`.
- No synthesis or second-stage model call is performed.
