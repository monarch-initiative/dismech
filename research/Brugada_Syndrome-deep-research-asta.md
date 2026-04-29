---
provider: asta
model: Asta Scientific Corpus Retrieval
cached: false
start_time: '2026-04-14T00:42:54.741272'
end_time: '2026-04-14T00:42:58.164436'
duration_seconds: 3.42
template_file: templates/disease_pathophysiology_research_asta.md
template_variables:
  disease_name: Brugada syndrome
  mondo_id: ''
  category: Genetic
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

Pathophysiology and clinical mechanisms of Brugada syndrome. Core disease mechanisms, molecular and cellular pathways, involved genes and proteins, relevant metabolites or drugs, affected cell types and anatomical structures, disease progression, major clinical phenotypes and complications, and treatment-relevant mechanism papers.

## Output

# Asta Literature Retrieval: Pathophysiology and clinical mechanisms of Brugada syndrome. Core disease mechanisms, molecular and cellular pathways...

This report is retrieval-only and is generated directly from Asta results.

- Papers retrieved: 20
- Snippets retrieved: 20

## Relevant Papers

### [1] Single Cell Transcriptomics Trajectory and Molecular Convergence of Clinically Relevant Mutations in Brugada Syndrome.
- Authors: Richa Tambi, Reem Abdel Hameid, Asma R. Bankapur, Nasna Nassir, G. Begum et al.
- Year: 2021
- Venue: American journal of physiology. Heart and circulatory physiology
- URL: https://www.semanticscholar.org/paper/4458fe1e74cb382da1dc5c596ed05dee7dbae385
- DOI: 10.1152/ajpheart.00061.2021
- PMID: 33797273
- Citations: 6
- Summary: It is suggested that genomic and proteomic hotspots in BrS converge into ion transport pathway and cardiomyocyte as a major BrS associated cell type that provides insight into the complex genetic etiology of BrS.
- Evidence snippets:
  - Snippet 1 (score: 0.487)
    > Brugada syndrome (BrS) is a rare, inherited arrhythmia with high risk of sudden cardiac death. To evaluate the molecular convergence of clinically relevant mutations and to identify developmental cardiac cell types that are associated with BrS etiology, we collected 733 mutations represented by 16 sodium, calcium, potassium channels, regulatory and structural genes related to BrS. Among the clinically relevant mutations, 266 are unique singletons and 88 mutations are recurrent. We observed an over representation of clinically relevant mutations (~80%) in SCN5A gene, and also identified several candidate genes, including GPD1L, TRPM4 and SCN10A. Furthermore, protein domain enrichment analysis revealed that a large proportion of the mutations impacted ion-transport domains in multiple genes, including SCN5A, TRPM4 and SCN10A. A comparative protein domain analysis of SCN5A further established a significant (p=0.04) enrichment of clinically relevant mutations within ion-transport domain, including a significant (p=0.02) mutation hotspot within 1321-1380 residue. The enrichment of clinically relevant mutations within SCN5A ion transport domain is stronger (p=0.00003) among early onset of BrS. Our spatiotemporal cellular heart developmental (prenatal to adult) trajectory analysis applying single cell transcriptome identified the most frequently BrS mutated genes (SCN5A and GPD1L) are significantly upregulated in the prenatal cardiomyocytes. A more restrictive cellular expression trajectory is prominent in the adult heart ventricular cardiomyocytes compared to prenatal. Our study suggests that genomic and proteomic hotspots in BrS converge into ion transport pathway and cardiomyocyte as a major BrS associated cell type that provides insight into the complex genetic etiology of BrS.

### [2] Sodium channel current loss of function in induced pluripotent stem cell-derived cardiomyocytes from a Brugada syndrome patient
- Authors: E. Selga, F. Sendfeld, R. Martínez-Moreno, Claire N. Medine, O. Tura-Ceide et al.
- Year: 2018
- Venue: Journal of Molecular and Cellular Cardiology
- URL: https://www.semanticscholar.org/paper/58904fb4a8370cf03af046e5fa2828965e5dbf62
- DOI: 10.1016/j.yjmcc.2017.10.002
- PMID: 29024690
- PMCID: 5807028
- Citations: 52
- Influential citations: 4
- Summary: Cardiomyocytes derived from iPS cells from a Brugada syndrome patient with a mutation in SCN5A recapitulate the loss of function of sodium channel current associated with this syndrome; including pro-arrhythmic changes in channel function not detected using conventional heterologous expression systems.
- Evidence snippets:
  - Snippet 1 (score: 0.463)
    > Brugada syndrome is an autosomal dominant hereditary condition that is responsible for 20% of sudden cardiac deaths of patients with structurally normal hearts [1]. It is characterized by an abnormal electrocardiogram with ST-segment elevation in the right precordial leads V 1 to V 3 and right bundle-branch block frequently leading to ventricular fibrillation [2]. Patients often present symptoms of ventricular tachycardia, bradycardia, and atrial ventricular node conduction disorder, and more males than females are diagnosed with Brugada syndrome. To date, the implantation of a cardioverter defibrillator is the only proven effective treatment of the disease [3,4]. Whilst Brugada syndrome has been associated with mutations in 23 genes [5], the majority of these disease-related mutations have been found in SCN5A [6]. This gene encodes the alpha-subunit of the cardiac sodium channel (Na v 1.5) which is responsible for the sodium inward current (I Na ). Heterologous expression of recombinant Na v 1.5 channels in conventional cellular systems has provided invaluable insight into the molecular and electrophysiological basis of Brugada syndrome. Still, the main limitation of this approach is that the cells typically used (i.e., HEK293 cells, Xenopus oocytes) deviate considerably from human cardiomyocytes in many relevant aspects. These cells do not reflect the modulatory effects of accessory channel subunits or the influence of potential compensatory pathways, both of which could take place in native cardiomyocytes. Thus, studies of mutant channels using such expression systems might be missing important characteristics of native cardiomyocytes relevant to pathophysiology.
    > The differentiation of induced pluripotent stem (iPS) cells from patients with cardiac diseases into cardiomyocytes (iPS-CM) provides a cell model highly homologous to native human cardiomyocytes. The use of these surrogate cells allows investigators to study mutant ion channels in their native patient-specific cell environment. This includes all their regulatory proteins, and importantly, a physiologically controlled level of protein expression. To date, several cardiac channelopathies including long QT syndrome

### [3] Sudden cardiac death and inherited channelopathy: the basic electrophysiology of the myocyte and myocardium in ion channel disease
- Authors: C. A. Martin, Gareth D. K. Matthews, C. Huang
- Year: 2012
- Venue: Heart
- URL: https://www.semanticscholar.org/paper/29976470123eed75b8f529e1e4485294a96481a9
- DOI: 10.1136/heartjnl-2011-300953
- PMID: 22422742
- PMCID: 3308472
- Citations: 73
- Influential citations: 5
- Summary: Basic research using molecular techniques, as well as animal models, has proved extremely useful in improving knowledge of inherited arrhythmogenic syndromes and provides novel markers for risk assessment and a basis for new strategies of treatment.
- Evidence snippets:
  - Snippet 1 (score: 0.460)
    > Ion channels are pore-forming proteins that provide pathways for the controlled trans-membrane movement of ions. This is critical for a range of physiological processes including action potential (AP) generation and propagation, resulting in the release of intracellular Ca 2+ stores triggering mechanical activity. Abnormalities in cardiac ion channel function or in their associated regulatory proteins may lead to arrhythmias and sudden cardiac death (SCD). SCD poses a major medical challenge and significant public health burden, accounting for over 300 000 deaths per year in the USA, 1 and up to 70 000 deaths per year in the UK, 2 with survival rates of only 2%. In the majority of cases, the arrhythmias are a manifestation of underlying ischaemic heart disease; however, autopsy fails to reveal a cause in up to 40% of SCD patients. 3 Despite the high prevalence and large impact on society of cardiac arrhythmias, our understanding of the cellular and molecular mechanisms governing the initiation, maintenance and propagation of arrhythmias remains limited. Consequently, current risk stratification of patients and families with these conditions is inadequate and the mainstay of treatment is often restricted to implantable cardioverter defibrillator implantation. Although new techniques are being developed to investigate the mechanisms that predispose to SCD, invasive studies in humans are limited. Therefore, basic research using molecular techniques as well as animal models is essential in improving our understanding of the mechanisms of arrhythmogenesis at the cellular level. This review forms the third paper in a series of inherited channelopathy reviews published in this journal, with the earlier papers discussing the impact of pathophysiology 4 and the role of the Sudden Adult Death Syndrome clinic 5a in the management of ion channel disease. The current review will focus on the role of basic science in investigating primary electrical diseases of the heart as a paradigm for cardiac arrhythmias, concentrating on Brugada syndrome (BrS), long QT syndrome (LQTS) and catecholaminergic polymorphic ventricular tachycardia (CPVT).

### [4] Electrophysiological Mechanisms of Brugada Syndrome: Insights from Pre-clinical and Clinical Studies
- Authors: G. Tse, Tong Liu, K. H. C. Li, V. Laxton, Y. W. Chan et al.
- Year: 2016
- Venue: Frontiers in Physiology
- URL: https://www.semanticscholar.org/paper/8d4acfb8df7ee01acd6c2d82a8f73ab8ee2a55f9
- DOI: 10.3389/fphys.2016.00467
- PMID: 27803673
- PMCID: 5067537
- Citations: 54
- Influential citations: 3
- Summary: Evidence from computational modeling, pre-clinical, and clinical studies illustrates that molecular abnormalities found in BrS lead to alterations in excitation wavelength (λ), which ultimately elevates arrhythmic risk.
- Evidence snippets:
  - Snippet 1 (score: 0.457)
    > Brugada syndrome (BrS), is a primary electrical disorder predisposing affected individuals to sudden cardiac death via the development of ventricular tachycardia and fibrillation (VT/VF). Originally, BrS was linked to mutations in the SCN5A, which encodes for the cardiac Na+ channel. To date, variants in 19 genes have been implicated in this condition, with 11, 5, 3, and 1 genes affecting the Na+, K+, Ca2+, and funny currents, respectively. Diagnosis of BrS is based on ECG criteria of coved- or saddle-shaped ST segment elevation and/or T-wave inversion with or without drug challenge. Three hypotheses based on abnormal depolarization, abnormal repolarization, and current-load-mismatch have been put forward to explain the electrophysiological mechanisms responsible for BrS. Evidence from computational modeling, pre-clinical, and clinical studies illustrates that molecular abnormalities found in BrS lead to alterations in excitation wavelength (λ), which ultimately elevates arrhythmic risk. A major challenge for clinicians in managing this condition is the difficulty in predicting the subset of patients who will suffer from life-threatening VT/VF. Several repolarization risk markers have been used thus far, but these neglect the contributions of conduction abnormalities in the form of slowing and dispersion. Indices incorporating both repolarization and conduction and based on the concept of λ have recently been proposed. These may have better predictive values than the existing markers.

### [5] Towards Mutation-Specific Precision Medicine in Atypical Clinical Phenotypes of Inherited Arrhythmia Syndromes
- Authors: T. Nakajima, S. Tamura, M. Kurabayashi, Y. Kaneko
- Year: 2021
- Venue: International Journal of Molecular Sciences
- URL: https://www.semanticscholar.org/paper/3d299f57f344d42eff9d3565d1581dae7fb87a54
- DOI: 10.3390/ijms22083930
- PMID: 33920294
- PMCID: 8069124
- Citations: 6
- Influential citations: 1
- Summary: Since the epileptic phenotype appears to manifest prior to cardiac events in this mutation carrier, identifying KCND3 mutations in patients with epilepsy and providing optimal therapy will help prevent sudden unexpected death in epilepsy.
- Evidence snippets:
  - Snippet 1 (score: 0.457)
    > Recent advances in molecular genetics have identified many causal genes for inherited arrhythmia syndromes (IASs) such as long QT syndrome (LQTS) [1], short QT syndrome (SQTS) [2], Brugada syndrome (BrS) [3,4] and early repolarization (ER) syndrome (ERS) [3,5]. Most causal genes for IASs encode cardiac ion channels or their related proteins. Genotype-phenotype studies and functional analyses of mutant genes, using heterologous expression systems and experimental animal models, have revealed the pathophysiology of IASs and enabled the establishment of causal gene-specific precision medicine [6][7][8]. Furthermore, analyses of patient-specific and/or genome-edited induced pluripotent stem cell-derived cardiomyocytes (iPSC-CMs) have provided further insights into the pathophysiology of IASs and novel promising therapeutic strategies for IASs, although there are still some limitations of using iPSC-CMs, such as immature structure and function and mixed population of atrial, ventricular, and nodal cells, as a standard technology [9].
    > The altered function of causal genes that encode cardiac ion channels is caused by multiple mechanisms, including trafficking defects, producing non-functional channels, altered channel gating properties, and a combination thereof. These altered functions of mutant channels underly the clinical phenotypes of IASs [10][11][12]. Particularly, unique electrophysiological properties of mutant channels have been shown to be associated with the atypical clinical phenotypes of IASs [10,13]. Furthermore, the elucidation of the mechanisms underlying the atypical clinical phenotypes of IASs has raised the possibility of mutation-specific precision medicine.
    > We herein review the current knowledge of genotype-phenotype relationships, underlying molecular and cellular mechanisms, and established pharmacological therapies of IASs, including LQTS, SQTS, and J wave syndrome (BrS and ERS).

### [6] J wave syndrome: Benign or malignant?
- Authors: Alborz Sherafati, M. Eslami, Reza Mollazadeh
- Year: 2021
- Venue: ARYA Atherosclerosis
- URL: https://www.semanticscholar.org/paper/c6ffd16e004d12c90e5acac0f7df05d8cb202b71
- DOI: 10.22122/arya.v17i0.2259
- PMID: 35685231
- PMCID: 9137236
- Citations: 1
- Summary: This paper describes 2 patients with early repolarization and Brugada syndrome, and discusses their definition, epidemiology, genetics, cellular mechanism, diagnosis, risk stratification, and finally, therapeutic challenges and options one by one in detail.
- Evidence snippets:
  - Snippet 1 (score: 0.453)
    > J wave syndrome is an electrical disease of the heart due to pathologic early repolarization. It encompasses a clinical spectrum from aborted sudden cardiac death due to ventricular arrhythmia (VA) usually in young affected patients to self-terminating ventricular ectopies, and finally, asymptomatic relatives of probands detected during electrocardiography acquisition (early repolarization pattern). This syndrome consists of 2 phenotypes, early repolarization and Brugada syndrome. Herein, we first describe 2 patients with early repolarization and Brugada syndrome, then, discuss their definition, epidemiology, genetics, cellular mechanism, diagnosis, risk stratification, and finally, therapeutic challenges and options one by one in detail.

### [7] The Mechanism of Ajmaline and Thus Brugada Syndrome: Not Only the Sodium Channel!
- Authors: M. Monasky, E. Micaglio, S. D’Imperio, C. Pappone
- Year: 2021
- Venue: Frontiers in Cardiovascular Medicine
- URL: https://www.semanticscholar.org/paper/17af37987335d9ae6f2219b4e0a922fa6f82428c
- DOI: 10.3389/fcvm.2021.782596
- PMID: 35004896
- PMCID: 8733296
- Citations: 13
- Summary: Clinical studies have implicated several candidate genes in BrS, encoding not only for sodium, potassium, and calcium channel proteins, but also for signaling- related, scaffolding-related, sarcomeric, and mitochondrial proteins, which could prove absolutely relevant in the mechanism of BrS.
- Evidence snippets:
  - Snippet 1 (score: 0.452)
    > Ajmaline is an anti-arrhythmic drug that is used to unmask the type-1 Brugada syndrome (BrS) electrocardiogram pattern to diagnose the syndrome. Thus, the disease is defined at its core as a particular response to this or other drugs. Ajmaline is usually described as a sodium-channel blocker, and most research into the mechanism of BrS has centered around this idea that the sodium channel is somehow impaired in BrS, and thus the genetics research has placed much emphasis on sodium channel gene mutations, especially the gene SCN5A, to the point that it has even been suggested that only the SCN5A gene should be screened in BrS patients. However, pathogenic rare variants in SCN5A are identified in only 20–30% of cases, and recent data indicates that SCN5A variants are actually, in many cases, prognostic rather than diagnostic, resulting in a more severe phenotype. Furthermore, the misconception by some that ajmaline only influences the sodium current is flawed, in that ajmaline actually acts additionally on potassium and calcium currents, as well as mitochondria and metabolic pathways. Clinical studies have implicated several candidate genes in BrS, encoding not only for sodium, potassium, and calcium channel proteins, but also for signaling-related, scaffolding-related, sarcomeric, and mitochondrial proteins. Thus, these proteins, as well as any proteins that act upon them, could prove absolutely relevant in the mechanism of BrS.

### [8] Novel SCN5A Variant Shows Multiple Phenotypic Expression in the Same Family
- Authors: C. Balla, D. Mele, F. Vitali, C. Andreoli, E. Tonet et al.
- Year: 2021
- Venue: Circulation. Genomic and Precision Medicine
- URL: https://www.semanticscholar.org/paper/4fe4800a3f77d817cbd57f6152fab6fba5688f8f
- DOI: 10.1161/CIRCGEN.121.003481
- PMID: 34749512
- PMCID: 8694256
- Citations: 7
- Summary: This is an open access article under the terms of the Creative Commons Attribution Non-Commercial-NoDerivs License, which permits use, distribution, and reproduction in any medium, provided that the original work is properly cited, the use is noncommercial, and no modifications or adaptations are made.
- Evidence snippets:
  - Snippet 1 (score: 0.438)
    > To our knowledge, the present case is the first description of an SCN5A variant showing multiple phenotypic expression ranging from Brugada syndrome to ACM in the same family.
    > Brugada syndrome is an inherited channelopathy first described as a pure electrical disorder predisposing to the risk of sudden cardiac death. Subsequence evidence have shown subtle RV structural abnormalities and RV outflow tract changes leading to different hypothesis on the pathophysiology of the syndrome. 2,3 CM is a genetic heart muscle disorder characterized by fibro-fatty replacement that predispose to ventricular arrhythmias leading to cardiac arrest in young people.
    > The hypothesis of the close connection between Brugada syndrome and ACM has been supported by the results of Te Riele et al, 4 which show that rare variants in SCN5A are present in ≈2% of patients affected by ACM. Functional analysis of one of the SCN5A mutation showed not only reduced INa amplitude but also a structural deficit in the organization of cell adhesion, supporting the hypothesis that voltage-gated sodium 1.5 may channel have different mechanisms causing cardiomyopathy. 4 ultiple mutation-positive family members harboring the same variant show different phenotypes. Factors, such as age, comorbidities, and environmental factors, may modify the effects of the primary genetic defect. Interindividual variability in disease expression may also be due to the inheritance of genetic modifiers that have a role to determine the age of onset, its rate of progression, and incidence of major cardiac events or to protect from the development of the disease. 5 e current family adds further evidence about the pleiotropic nature of SCN5A showing how a single SCN5A variant may have different clinical expression in the same family.

### [9] Sudden death of a patient with epilepsy: When Brugada syndrome mimicry can be fatal
- Authors: Gabriele Negro, G. Ciconte, V. Borrelli, R. Rondine, V. Maiolo et al.
- Year: 2021
- Venue: HeartRhythm Case Reports
- URL: https://www.semanticscholar.org/paper/8a91c724330c3814a3156e52911a60db4a637556
- DOI: 10.1016/j.hrcr.2021.12.008
- PMID: 35492846
- PMCID: 9039568
- Citations: 3
- Influential citations: 1
- Summary: are useful in controlling malignant neurologic manifestations, and their adjunctive use in refractory epilepsy reduces mortality 7-fold, and a community-based study found an increased risk of SCD in patients with epilepsy treated with AEDs.
- Evidence snippets:
  - Snippet 1 (score: 0.432)
    > Brugada syndrome (BrS) is an inherited disorder characterized by coved-type ST-segment elevation in the right precordial leads and increased risk of sudden cardiac death (SCD) in ostensibly normal heart. 1 The electrocardiogram (ECG) manifestations may occur spontaneously or after the exposure to sodium channel blocking agents. 2 The main clinical manifestations (syncope and SCD) are caused by malignant ventricular tachycardia / ventricular fibrillation, which are related to an arrhythmogenic epicardial substrate located in the anterior aspect of the right ventricular outflow tract. 3,4 Idiopathic epilepsy and BrS share the pathophysiology of altered transmembrane ion current caused by mutations of ion channel subunit genes. Sodium channel dysfunction represents a common pathogenetic pathway for these 2 clinical entities that may be involved as a mechanism of sudden death. In addition, mutations of ion channel or arrhythmiarelated genes are the most common defects found in patients experiencing sudden death in epilepsy. 5 Coexistence of epilepsy and BrS in a family with SCN5A mutation has been reported, suggesting that sodium channel mutation may be responsible for cardiac and cerebral manifestations, probably at different ages in the same individual and/or in the same family. 6 The latter underlines the importance of careful assessment of symptoms, detailed family history, and a thorough ECG analysis when evaluating patients with seizure-like symptoms.
    > Antiepileptic drugs (AEDs) are useful in controlling malignant neurologic manifestations, and their adjunctive use in refractory epilepsy reduces mortality 7-fold. 7 On the other hand, a community-based study found an increased risk of SCD in patients with epilepsy treated with AEDs, and this risk was specifically associated with the use of sodium channel blockers. 8 Among sodium channel blockers used as AEDs, phenytoin (which belongs to the IB class of antiarrhythmic drugs) has been described to induce a type 1 ECG Brugada pattern at supratherapeutic doses. 9 However, its direct role as a trigger of a fatal ventricular arrhythmia in a patient with BrS has never

### [10] Brugada Syndrome: Oligogenic or Mendelian Disease?
- Authors: M. Monasky, E. Micaglio, G. Ciconte, C. Pappone
- Year: 2020
- Venue: International Journal of Molecular Sciences
- URL: https://www.semanticscholar.org/paper/79897e2657e5991ed3c7fa322cd57acd0033a832
- DOI: 10.3390/ijms21051687
- PMID: 32121523
- PMCID: 7084676
- Citations: 50
- Influential citations: 3
- Summary: This work has suggested that the best model for studying Brugada syndrome is the human patient population, because there is no mutated gene that connects all, or even a majority, of BrS cases, and it is currently impossible to create animal and cell line genetic models that represent all BrS Cases.
- Evidence snippets:
  - Snippet 1 (score: 0.429)
    > Brugada syndrome (BrS) is diagnosed by a coved-type ST-segment elevation in the right precordial leads on the electrocardiogram (ECG), and it is associated with an increased risk of sudden cardiac death (SCD) compared to the general population. Although BrS is considered a genetic disease, its molecular mechanism remains elusive in about 70–85% of clinically-confirmed cases. Variants occurring in at least 26 different genes have been previously considered causative, although the causative effect of all but the SCN5A gene has been recently challenged, due to the lack of systematic, evidence-based evaluations, such as a variant’s frequency among the general population, family segregation analyses, and functional studies. Also, variants within a particular gene can be associated with an array of different phenotypes, even within the same family, preventing a clear genotype–phenotype correlation. Moreover, an emerging concept is that a single mutation may not be enough to cause the BrS phenotype, due to the increasing number of common variants now thought to be clinically relevant. Thus, not only the complete list of genes causative of the BrS phenotype remains to be determined, but also the interplay between rare and common multiple variants. This is particularly true for some common polymorphisms whose roles have been recently re-evaluated by outstanding works, including considering for the first time ever a polygenic risk score derived from the heterozygous state for both common and rare variants. The more common a certain variant is, the less impact this variant might have on heart function. We are aware that further studies are warranted to validate a polygenic risk score, because there is no mutated gene that connects all, or even a majority, of BrS cases. For the same reason, it is currently impossible to create animal and cell line genetic models that represent all BrS cases, which would enable the expansion of studies of this syndrome. Thus, the best model at this point is the human patient population. Further studies should first aim to uncover genetic variants within individuals, as well as to collect family segregation data to identify potential genetic causes of BrS.

### [11] Mechanisms of Arrhythmias in the Brugada Syndrome
- Authors: M. Blok, B. Boukens
- Year: 2020
- Venue: International Journal of Molecular Sciences
- URL: https://www.semanticscholar.org/paper/cb44ffeb4b14245da88023a83a796a25982dd88a
- DOI: 10.3390/ijms21197051
- PMID: 32992720
- PMCID: 7582368
- Citations: 34
- Influential citations: 2
- Summary: Identifying the site of origin and mechanism of Brugada syndrome would greatly benefit the development of mechanism-driven treatment strategies.
- Evidence snippets:
  - Snippet 1 (score: 0.426)
    > The human iPSC technology has consistently been employed over the years to allow investigation of the molecular and cellular mechanism of Brugada syndrome in the setting of the native patient-specific cell environment. Despite this major advantage, human iPSC-derived cardiomyocyte models fail to capture the complex changes in tissue architecture that occur in Brugada syndrome. Nevertheless, human iPSC-derived cardiomyocytes are a useful tool to study the functional predisposition to Brugada syndrome. Collectively, these studies led to profound divergent results which could be explained by the variety of genetic mutations studied. In part, the effect of mutations may vary, even if affecting the same gene [144,145]. Furthermore, protocols for human iPSC-derived cardiomyocyte differentiation do not yield a pure cell population of a single type, but rather a variety of cardiomyocytes with divergent phenotypes. In addition, human iPSC-derived cardiomyocytes are characterized by their immature, fetal-like phenotype which, compared to adult cardiomyocytes, consists of different structural and functional properties [146].
    > While some studies reported no clear electrophysiological abnormalities in Brugada syndrome patient-derived iPSC-derived cardiomyocyte lines compared to controls [147,148], other reports contrarily showed evidence of significant alterations in action potential duration [65,144], decreased I Na density [65,144,145,[149][150][151], decreased action potential upstroke velocity [65,144,145,150,151], or irregular calcium handling [65,145]. Ma and colleagues found that pacing at a frequency of 0.1 Hz led to a small subgroup (25%) of Brugada syndrome patient-derived iPSC-derived cardiomyocytes presenting with action potentials which were by the authors claimed to resemble the loss of action potential dome configuration as postulated by the repolarization hypothesis, albeit the pacing frequency exceeding human physiological range [71,144]. Only a few studies focus on the potential presence of morphological changes, which were observed by Belbachir and colleagues in the form of cytoskeletal defects [65].

### [12] Investigation of a Large Kindred Reveals Cardiac Calsequestrin (CASQ2) as a Cause of Brugada Syndrome
- Authors: M. d'Apolito, Francesco Santoro, A. Ranaldi, I. Ragnatela, A. Colia et al.
- Year: 2024
- Venue: Genes
- URL: https://www.semanticscholar.org/paper/7c80f9ec717d86903e5d13270507333e20a7c078
- DOI: 10.3390/genes15070822
- PMID: 39062601
- PMCID: 11275647
- Citations: 1
- Summary: The data suggest that the p.Tyr178His substitution is associated with BrS in the family investigated, affecting the stability of the protein, disrupting filamentation at the interdimer interface, and affecting the subsequent formation of tetramers and polymers that contain calcium-binding sites.
- Evidence snippets:
  - Snippet 1 (score: 0.421)
    > Brugada syndrome (BrS) is one of the main hereditary channelopathies characterized by risk of ventricular fibrillation (VF) and sudden cardiac death in an anatomically healthy heart. BrS was first described by Pedro and Josep Brugada in 1992 as a hereditary arrhythmogenic disorder characterized by clinical-electrocardiographic arrhythmia, with a low prevalence globally (0.5 per 1000 or 5 to 20 per 10,000 individuals) [1][2][3]. BrS is found predominantly in men aged between 30 and 40, with a male/female ratio of 9:1 in Southeast Asia and 3:1 among Caucasians [4].
    > BrS is characterized by the presence of ST segment elevation in the right precordial leads (V1 to V3), referred to as electrocardiogram (ECG) type I. The diagnosis is established on the existence of spontaneous or drug-induced ST segment elevation characterized by ≥2 mm elevation of the J-point and ST segment, either superiorly convex "arched" (BrS type II) or descending linear (BrS type III).
    > The ST elevation is followed by a symmetrical negative T wave in ≥1 right and/or high right precordial leads [5,6].
    > In spite of the most recent models on further inheritance pathways, BrS is still considered to be an autosomal dominant Mendelian disorder inherited with incomplete penetrance. Genetic mutations have been identified in 11-28% of patients with BrS, with a major percentage affecting the SCN5A (sodium voltage-gated channel alpha subunit 5) gene [7]. Actually, SCN5A is considered the only clinically relevant gene evaluated, even if it is mutated in only about 20% of patients with BrS [7,8]. Pathogenic variations in the SCN5A gene, which encodes the α subunit of the voltage-gated cardiac Na+ channel protein (Nav1.5), were detected in patients with BrS, impairing the proper function of the channel. Genetic variants in over 27 other genes have also been associated with the pathophysiology of BrS.

### [13] Molecular Mechanisms of Inherited Arrhythmias
- Authors: C. Wolf, C. Berul
- Year: 2008
- Venue: Current Genomics
- URL: https://www.semanticscholar.org/paper/8dc574fc997d6e863ac851b4a75d122de6d9aa61
- DOI: 10.2174/138920208784340768
- PMID: 19440513
- PMCID: 2679644
- Citations: 26
- Influential citations: 3
- Summary: The molecular basis of inherited arrhythmias in structurally normal and altered hearts is summarized, which helps explain the molecular and functional mechanisms of long QT syndrome, Brugada syndrome, catecholaminergic polymorphic ventricular tachycardia, and other electrical myopathies.
- Evidence snippets:
  - Snippet 1 (score: 0.420)
    > Inherited arrhythmias can be life threatening, and are major cause of mortality and morbidity in developed nations. Identification of molecular pathways that increase susceptibility to arrhythmia is necessary to prevent disease occurrence, to improve current therapies and to target new drug development. In recent years, the discovery of pathogenic mutations in inherited arrhythmia syndromes has provided novel insights for the understanding and treatment of diseases predisposing to sudden cardiac death. In patients with the long QT syndromes (LQTS), genotype-phenotype relation studies [1] and genetic testing have influenced patient risk stratification [2] and refined treatment strategies [3].
    > Arrhythmia mechanisms include abnormal automaticity, triggered activity, and re-entrant excitation. Each of these mechanisms can occur in any type of myocardial disease or in inherited cardiac arrhythmias. The current article focuses on molecular mechanisms of arrhythmias in the structurally abnormal and normal heart. Hypertrophic and dilated cardiomyopathies, as well as arrhythmogenic right ventricular dysplasia/cardiomyopathy are common substrates of inherited arrhythmias in the structurally abnormal heart. Genetic diseases causing arrhythmias in the structural normal heart, also called electrical myopathies, include the long QT syndromes, Brugada syndrome, catecholaminergic polymorphic ventricular tachycardia (CPVT), and non-defined familiar idiopathic ventricular fibrillation. Most, but not all of these disorders are caused by mutations in genes encoding cardiac ion-channel proteins. Among family members carrying an identical mutation in a single gene, remarkable phenotypic variability and expressivity may be observed, suggesting both environmental [4] and genetic modifiers [5].

### [14] Natural History of Arrhythmogenic Cardiomyopathy
- Authors: G. Mattesi, A. Zorzi, D. Corrado, A. Cipriani
- Year: 2020
- Venue: Journal of Clinical Medicine
- URL: https://www.semanticscholar.org/paper/9d38bdd10019689e9b2ebc49e792f40200041d31
- DOI: 10.3390/jcm9030878
- PMID: 32210158
- PMCID: 7141540
- Citations: 38
- Influential citations: 2
- Summary: The genetic basis, the clinical course and the phenotypic variants of AC are addressed, including non-desmosomal and nongenetic variants reported in patients with AC, some of which showing overlapping phenotypes with other non-ischemic diseases.
- Evidence snippets:
  - Snippet 1 (score: 0.418)
    > Relationship between arrhythmogenic right ventricular cardiomyopathy (ARVC) and Brugada Syndrome. Mutant desmosomal proteins may induce potentially lethal ventricular arrhythmias by causing gap-junction remodeling and modifying the amplitude and kinetics of the sodium current, as a consequence of the cross-talk between these molecules at the intercalated discs. According to this view, Brugada syndrome and ARVC may share clinical features and arrhythmic mechanisms because of their common origin from the connexome, a coordinated network of proteins involving desmosomes, sodium channels, and gap-junction, aimed to control synergistically adhesion, excitability, and coupling of myocardial cells [18][19][20]. ECG = electrocardiogram; VT = ventricular tachycardia. Modified from Ref [20] with permission of the publisher.
    > Genes encoding non-desmosomal proteins like ion channels and cytoskeletal components have been also associated with phenotypes within the spectrum of AC, and this may confirm the "final common pathway" hypothesis, by which inherited cardiac diseases with similar phenotype and genetic heterogeneity are due to variants in genes encoding proteins of similar function or involved in a common pathway. According to this view, AC should be considered a disease not only of desmosomes, but of the intercalated disc as a whole [1]. In fact, mutations in transforming grow factor-3 (TFGB3) and in transmembrane protein 43 (TMEM43), which disrupt the desmosomal function, have been detected in patients with classical ARVC [21][22][23], as well as variants in αT-catenin Syndrome. Mutant desmosomal proteins may induce potentially lethal ventricular arrhythmias by causing gap-junction remodeling and modifying the amplitude and kinetics of the sodium current, as a consequence of the cross-talk between these molecules at the intercalated discs. According to this view, Brugada syndrome and ARVC may share clinical features and arrhythmic mechanisms because of their common origin from the connexome, a coordinated network

### [15] Genetics of Atrial Fibrillation and Possible Implications for Ischemic Stroke
- Authors: R. Lemmens, S. Hermans, D. Nuyens, V. Thijs
- Year: 2011
- Venue: Stroke Research and Treatment
- URL: https://www.semanticscholar.org/paper/0345b2f055b006c87f2022cd3480ec4305266284
- DOI: 10.4061/2011/208694
- PMID: 21822468
- PMCID: 3148589
- Citations: 10
- Summary: The current knowledge on the genetic background of atrial fibrillation and the consequences for cerebrovascular disease is reviewed.
- Evidence snippets:
  - Snippet 1 (score: 0.413)
    > The human cardiac sodium channel (SCN5A) is responsible for fast depolarization of cardiomyocytes and has been a therapeutic target for antiarrhythmic drugs. Initially mutations in SCN5A were identified in families with long QT syndrome [8]. Over the years, more than 200 mutations have been reported in SCN5A which are associated with variable cardiac diseases like Brugada syndrome, progressive conduction defect, sick sinus node syndrome, dilated cardiomyopathy and AF [9]. Genotype-phenotype correlations revealed that most mutations are linked to specific clinical spectrums, but that clinical overlaps exist for the same genetic defects [10]. Both Brugada syndrome and long QT syndrome can be complicated with supraventricular arrhythmias which often include AF [11]. More evidence for the role of mutations in SCN5A in the pathophysiology of AF was provided by the identification of a family with a dilated cardiomyopathy and AF carrying a mutation in SCN5A [12]. Additionally, novel mutations in the same gene were reported in familial forms of AF with and without structural cardiac disease [13][14][15][16]. It was determined that rare variants in SCN5A are present in nearly 6% of AF probands [14]. In two studies, functional analysis of the mutation showed a depolarizing shift in steady-state inactivation resulting in cellular hyperexcitability (gain of function) [15,16]. A loss of function was suggested by the study of another variant which revealed a hyperpolarizing shift in steady-state inactivation resulting in prolongation of the atrial action potential duration [13]. This delayed atrial repolarization could induce atrial torsades resulting in AF. Different mechanisms, both loss of function as well as gain of function, have been suggested in various syndromes. Furthermore, there is a wide spectrum of mutations which are associated with overlapping syndromes, suggesting environmental or other genetic factors to be of importance in determining the phenotype.

### [16] NaV1.5 autoantibodies in Brugada syndrome: pathogenetic implications
- Authors: A. Tarantino, G. Ciconte, D. Melgari, Anthony Frosio, A. Ghiroldi et al.
- Year: 2024
- Venue: European Heart Journal
- URL: https://www.semanticscholar.org/paper/48d95bef9ba5c15b6785ffc2a838788ed411a23e
- DOI: 10.1093/eurheartj/ehae480
- PMID: 39078224
- PMCID: 11491155
- Citations: 16
- Summary: The presence of anti-NaV1.5 autoantibodies in the majority of BrS patients is demonstrated, suggesting an immunopathogenic component of the syndrome beyond genetic predispositions and prompt reconsideration of the underlying mechanisms of BrS.
- Evidence snippets:
  - Snippet 1 (score: 0.411)
    > In a significant shift from the translational perspective to Brugada syndrome (BrS), this study highlights the role of autoimmunity by identifying anti-NaV1.5 autoantibodies in affected patients, including those without SCN5A mutations. This discovery is set to complement previous diagnostics based on electrocardiographic manifestations and drug testing and provides a reliable, non-invasive biomarker but also calls for a reevaluation of the pathophysiology of BrS involving immune-mediated mechanisms. The potential of immunomodulatory therapies, especially for genetically elusive cases, may introduce a new era of personalized treatment strategies.
    > blockers (SCBs), 5 this approach has significant limitations. 6 The pro-arrhythmic potential of such drugs, which are often not available in various countries, and the need for special cardiac monitoring for their administration limit their widespread use. 7 These compounding challenges are ongoing concerns regarding the true specificity and sensitivity of these drug tests. 6 Therefore, the difficulties in consistently detecting the diagnostic ECG pattern associated with the genetic inheritance of BrS 2,8,9 point to an inadequate estimate of the true prevalence of the disease. 0][11][12][13] About 20%-25% of BrS diagnoses are associated with variants in this gene, but the genetic basis for the remaining majority, almost 70%-75%, remains unknown. 14,15 In addition to SCN5A, other genes, including those related to sodium channel β-subunits and potassium and calcium channel genes, have also been investigated for their possible involvement, suggesting a broad and complex genetic basis for the syndrome. 14,15 Nevertheless, the clinical relevance of variations in these additional genes is frequently debated, highlighting the challenges that genetic testing faces in definitively diagnosing a significant proportion of BrS cases. 15,16 To address the complexities associated with genotype-phenotype correlation in BrS, a comprehensive scoring system was developed to aid clinicians identify BrS patients. 2,17 evertheless, the integration of ECG recordings, genetic information, clinical characteristics, and family history into the diagnostic process for BrS is intricate.

### [17] Pathogenesis of Brugada Syndrome: -Review from Our Study-
- Authors: I. Watanabe
- Year: 2018
- Venue: Journal of Nihon University Medical Association
- URL: https://www.semanticscholar.org/paper/6290fe46092f7b72090ffc16c56cf8de2af4f69b
- DOI: 10.4264/NUMA.77.2_77
- Summary: This work presents a meta-modelling study of saddleback function and its applications in cardiology and women’s health using a 3D model.
- Evidence snippets:
  - Snippet 1 (score: 0.410)
    > Pathogenesis of Brugada Syndrome: -Review from Our Study-

### [18] Brugada syndrome: current concepts and genetic background
- Authors: A. Pérez-Riera, J. Mendes, F. D. Silva, F. Yanowitz, L. D. Abreu et al.
- Year: 2021
- Venue: Journal of Human Growth and Development
- URL: https://www.semanticscholar.org/paper/9703afec4b429fa5ae6a08c66a4249bbc9337705
- DOI: 10.36311/JHGD.V31.11074
- Citations: 4
- Summary: This in depth analytical study of the countless mutations attributed to Brugada syndrome may constitute a real cornerstone that will help to better understand this intriguing syndrome.
- Evidence snippets:
  - Snippet 1 (score: 0.409)
    > which suggests that parasympathetic tone is a determining factor in arrhythmogenesis: higher level of vagal tone and higher levels of Ito (cardiac transient outward potassium current) is evident during slower heart rates. Although BrS is considered a genetic disease, its mechanism remains unknown in ≈70-75% of cases and no single mutation is sufficient to cause the BrS phenotype. Although ≈20% of patients with BrS carry mutations in SCN5A, which encodes for the pore-forming α subunit of the cardiac sodium channels, the molecular mechanisms underlying this condition are still largely unknown. SCN5A, that was identified as the first BrS-associated gene in 1998, has emerged as the most common gene associated with the syndrome. The SCN5A gene is considered as the only gene definitely associated with BrS. Currently, the oligogenic disease model is the accepted model 1 . More than 400 mutations in the SCN5A gene have been associated with SB. In an evidence-based review of genes reported to cause BS, which are in clinical use, 20 of the 21 genes did not have enough genetic evidence to support their causality for BS. Type 2 Brugada ECG (Electrocardiographic/ Electrocardiogram) pattern has also been associated with mutations in SCN5A (glycerol-3-phosphate dehydrogenase 1-like (GPD1L) protein), which is the domain responsible for a site homologous to SCN5A, and CACNA1C, the gene responsible for the α-subunit of cardiac L-type calcium channels.
    > To date, mutations of more than 20 genes, other than SCN5A, have been implicated in the pathogenesis of BrS. Multiple pathogenic variants of genes have been shown to alter the normal function of sodium ↓Loss-Of-Function (↓LOF), potassium Gain-Of-Function (↑GOF), and mutations in genes encoding for potassium channels have also been implicated.
    > Genes influencing I to , include KCNE3, KCND3 and SEMA3A (semaphoring, an endogenous potassium channel inhibitor) while KCNJ8, HCN4, KCN5 and ABCC9 (encoding for SUR2A

### [19] Inherited Cardiac Arrhythmia Syndromes: Focus on Molecular Mechanisms Underlying TRPM4 Channelopathies
- Authors: M. Amarouch, Jaouad El Hilaly
- Year: 2020
- Venue: Cardiovascular Therapeutics
- URL: https://www.semanticscholar.org/paper/b0b9f5789588a6f6e45f67fe8035b96fef10d183
- DOI: 10.1155/2020/6615038
- PMID: 33381229
- PMCID: 7759408
- Citations: 27
- Summary: The main objective of this article is to review the major cardiac TRPM4 channelopathies and recent advances regarding their genetic background and the underlying molecular mechanisms.
- Evidence snippets:
  - Snippet 1 (score: 0.407)
    > The Transient Receptor Potential Melastatin 4 (TRPM4) is a transmembrane N-glycosylated ion channel that belongs to the large family of TRP proteins. It has an equal permeability to Na+ and K+ and is activated via an increase of the intracellular calcium concentration and membrane depolarization. Due to its wide distribution, TRPM4 dysfunction has been linked with several pathophysiological processes, including inherited cardiac arrhythmias. Many pathogenic variants of the TRPM4 gene have been identified in patients with different forms of cardiac disorders such as conduction defects, Brugada syndrome, and congenital long QT syndrome. At the cellular level, these variants induce either gain- or loss-of-function of TRPM4 channels for similar clinical phenotypes. However, the molecular mechanisms associating these functional alterations to the clinical phenotypes remain poorly understood. The main objective of this article is to review the major cardiac TRPM4 channelopathies and recent advances regarding their genetic background and the underlying molecular mechanisms.

### [20] Comparative Analysis of Genetic Variations in the Nav1.5 Sodium Channel Subunits that Underlie Brugada Syndrome Using Patient-Specific iPSC-CMs
- Authors: Yue Zhu, Linlin Wang, C. Cui, Shaojie Chen, Hongwu Chen et al.
- Year: 2020
- Venue: Unknown venue
- URL: https://www.semanticscholar.org/paper/2728fb811958a39c5487464bc2e9bf7ab604dea9
- DOI: 10.21203/rs.3.rs-70177/v1
- Summary: Comparison of structural and electrophysiological characteristics of sodium channel subunits with different genetic variations and the safety of quinidine for use with BrS patient-specific iPSC-derived cardiomyocytes provides an advantageous platform for exploring disease mechanisms and evaluating drug safety in vitro.
- Evidence snippets:
  - Snippet 1 (score: 0.400)
    > Background: Brugada syndrome (BrS) is an autosomal dominant disorder that causes a high predisposition to sudden cardiac death. Several genes have been reported to be associated with BrS. Considering that the heterogeneity in clinical manifestations may result from genetic variations, the application of patient-specific induced pluripotent stem (iPS) cell-derived cardiomyocytes (CMs) may help to reveal cell phenotype characteristics resulting from different genetic backgrounds. The present study was to compare the structural and electrophysiological characteristics of sodium channel subunits with different genetic variations and evaluate the safety of quinidine for use with BrS patient-specific iPSC-derived cardiomyocytes.Methods: Two BrS patient-specific iPS cell lines were constructed that carried missense mutations in SCN5A and SCN1B. One iPS cell line from a healthy volunteer was used as a control. The differentiated cardiomyocytes from the three groups were evaluated by flow cytometry, immunofluorescence staining, electron microscopy, as well as calcium transient and patch clamp analyses to assess different pathological phenotypes. Finally, we evaluated the drug responses to varying concentrations of quinidine by measuring the action potential.Results: Compared to the control group, BrS-CMs showed a significant reduction in sodium current, prolonged action potential duration and varying degrees of decreased Vmax, but no structural difference was observed. After applying different concentrations of quinidine, the disease-specific groups and the control group had a downward trend in maximal upstroke velocity, resting membrane potential and action potential amplitude, and exhibited prolonged action potential duration without increasing incidence of arrhythmic events.Conclusion: Both patient-specific iPSC-CMs recapitulated the BrS phenotype at the cellular level. Although the SCN5A variation led to a markedly lower sodium current than what was observed with the SCN1B variation, their responses to quinidine were quite similar. The present study provides an advantageous platform for exploring disease mechanisms and evaluating drug safety in vitro.

## Notes

- This provider combines `search_papers_by_relevance` with `snippet_search`.
- No synthesis or second-stage model call is performed.
