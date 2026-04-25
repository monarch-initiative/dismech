---
provider: asta
model: Asta Scientific Corpus Retrieval
cached: false
start_time: '2026-04-24T18:21:27.179384'
end_time: '2026-04-24T18:21:31.516576'
duration_seconds: 4.34
template_file: templates/disease_pathophysiology_research_asta.md
template_variables:
  disease_name: UNC13A-Related Congenital NDD with Epilepsy
  mondo_id: ''
  category: Mendelian
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

Pathophysiology and clinical mechanisms of UNC13A-Related Congenital NDD with Epilepsy. Core disease mechanisms, molecular and cellular pathways, involved genes and proteins, relevant metabolites or drugs, affected cell types and anatomical structures, disease progression, major clinical phenotypes and complications, and treatment-relevant mechanism papers.

## Output

# Asta Literature Retrieval: Pathophysiology and clinical mechanisms of UNC13A-Related Congenital NDD with Epilepsy. Core disease mechanisms, mole...

This report is retrieval-only and is generated directly from Asta results.

- Papers retrieved: 17
- Snippets retrieved: 20

## Relevant Papers

### [1] Epilepsy phenotype and gene ontology analysis of the 129 genes in a large neurodevelopmental disorders cohort
- Authors: Y. Ko, S. Kim, Seungbo Lee, Jihoon G. Yoon, M. Kim et al.
- Year: 2023
- Venue: Frontiers in Neurology
- URL: https://www.semanticscholar.org/paper/f43c9f7586f4bca31dde58392f99660ca3ae2c97
- DOI: 10.3389/fneur.2023.1218706
- PMID: 37645600
- PMCID: 10461058
- Citations: 7
- Summary: Patients in the “epilepsy-genes” group started having seizures, often characterized by epilepsy syndrome, at a younger age and overall clinical features showed no significant differences between the two groups.
- Evidence snippets:
  - Snippet 1 (score: 0.646)
    > disorders that share neurodevelopmental processes. Further studies using advanced computational approaches, including integrative analysis of multiple biologic factors using omics data analysis, could shed light on the basic mechanisms underlying epilepsy and NDDs (28-30).
    > Our findings highlight overlapping neurologic features across different gene groups in an NDD cohort with epilepsy. We observed that various genes could be linked to different disease entities, including classic epilepsy syndromes, DEE, and neurodevelopmental disorders. These causative genes could be categorized based on their biological or molecular pathways, and the specific disease entity they are associated with. However, it is essential to note that patients carrying these genetic variants may exhibit heterogeneous and overlapping clinical courses in clinical practice. Considering the broad spectrum of phenotypes and genotypes in the NDD cohort, an exome-or genome-wide genetic approach would be preferable over a narrow-targeted approach based on phenotype except in cases with a highly suggestive etiology. The involvement of several causative genes involved in diverse molecular pathways and shared phenotypes demonstrated the complex and integrated mechanisms in the NDD cohort, which warrants further investigation.
  - Snippet 2 (score: 0.524)
    > Epilepsy genes showed compact and dense interactions with each other, whereas NDD genes showed a lack of interactions. The results are consistent with recent studies in which the molecular basis of epilepsy genes in NDD patients was analyzed (24). Various ion channel genes have been identified in earlyonset epilepsy patients in the early stages of clinical genetic studies (25). Initial studies on the genetic etiology of neurologic diseases often focused on early-onset epilepsy as it shows an apparent phenotype. Genes associated with sodium or potassium channels were documented first as they are often involved in very early-onset seizures. Studies eventually progressed to channelopathy research in the field of genetic epilepsy followed. As the NGS technique has become widely adopted, research on broad or non-specific NDDs has identified different causative genes, and follow-up reports of seizure phenotypes have been published. Our GO analysis was based on the accumulated evidence. Channelopathy, the main disease entity identified in the GO analysis of epilepsy genes, is characterized by alterations in neuronal excitability. NDD genes showed limited interactions with each other; thus, these genes may be involved in several pathomechanisms. However, recent studies suggested that the underlying biological mechanisms of epilepsy and NDDs include the complex interactions of various biological dimensions, including genes, epigenomes, cells, brain functions, and clinical manifestations (26,27). The findings of our study showing the similar clinical features of the two groups in our study supports the hypothesis that epilepsy and NDD are complex FIGURE Visualization of the gene ontology and pathway network of each gene group. Functionally grouped networks of epilepsy genes (A) and NDD genes (B) were derived from ClueGO enrichment analysis. Gene ontology terms and their associated genes share the same node color. The node size of each term corresponds to its enrichment significance. The lower the adjusted p-value of each term, the larger the node size. Edges are created based on the kappa score (≥ . ), which is calculated by taking into account the number of genes shared between two terms. Edge thickness is proportional to the kappa score.
    > disorders that share neurodevelopmental processes.

### [2] Shared Disease Mechanisms in Neurodevelopmental Disorders: A Cellular and Molecular Biology Perspective
- Authors: Elizabeth A. Pattie, Philip H. Iffland
- Year: 2025
- Venue: Brain Sciences
- URL: https://www.semanticscholar.org/paper/865dae8982d06d64da4620ccd43bc895dda351f5
- DOI: 10.3390/brainsci16010054
- PMID: 41594775
- PMCID: 12839103
- Summary: Several genes—including CDKL5, TSC1/2, SCN1a, and TANC2—that have been associated with epilepsy, ASD, or other NDD phenotypes that play a critical role in regulating one or more stages of brain development or function but differ widely in their disease-causing mechanisms are described.
- Evidence snippets:
  - Snippet 1 (score: 0.555)
    > However, for genes that are critical for early stages of brain development, there tend to be higher rates of comorbidity. However, even in that context, some genes seem to impact separate downstream processes that serve as distinct etiologies for epilepsy and NDDs, as indicated by the genes where therapeutics improve one but not the other. Alternatively, there may be a causative relationship (e.g., cognitive impairments or developmental regression caused by neurotoxicity of seizure activity). However, many of the molecular and cellular mechanisms behind brain development, epilepsy, ASD, and NDDs still remain unclear. Indeed, there is still much that remains unknown about the molecular function of most of these genes and the sequence of events that connect molecular function to network function to disease phenotype. Further, things like gene dose sensitivity, genetic imprinting, variant-specific changes in protein product and domain functionality, and other factors that impact variable expressivity and penetrance make it challenging to interpret the relationship between gene function and phenotype. Many genes, especially ones that regulate broad cellular functions, such as proliferation, migration, and differentiation, are also likely to have syndromic presentations. Some of them are also linked to cancer development and progression, which further supports the importance of these genes in functional mechanisms of molecular and cellular biology. However, understanding these cellular mechanisms, especially when considering distinct functional outcomes across pathogenic variants, will be invaluable for identifying therapeutic targets and developing new treatment options.
    > There are several limitations that hinder the ability of investigators to clearly define disease mechanisms and implement novel therapies in NDDs. First, due to the rarity of some of these disorders, it is difficult to establish genotype-phenotype correlations, and the paucity of available samples makes it challenging to elucidate disease mechanism both within, and especially across, variants. Additionally, while the increased accessibility to whole genome sequencing has significantly expanded the number of identified pathogenic variants associated with NDDs, detection of somatic mosaic variants remains challenging in brain-specific disorders. GoF and LoF variants in the same genes can result in similar phenotypes, making understanding disease mechanisms even more challenging and can make large-scale clinical trials of novel therapies difficult.

### [3] Recent advances in epilepsy genomics and genetic testing
- Authors: M. Hebbar, H. Mefford
- Year: 2020
- Venue: F1000Research
- URL: https://www.semanticscholar.org/paper/fed719aa3e9431d33ff157c61af9c0ef59c15333
- DOI: 10.12688/f1000research.21366.1
- PMID: 32201576
- PMCID: 7076331
- Citations: 75
- Influential citations: 4
- Summary: This review discusses the major advances in epilepsy genomics that have surfaced in recent years and aims to build a better understanding of pathogenesis and genetic testing options in DEE.
- Evidence snippets:
  - Snippet 1 (score: 0.533)
    > Several novel genes and disorders associated with DEE have been identified in the last few years [16][17][18] (Table 1). Many of the genes causing epilepsy encode components of neuronal ion channels leading to neuronal hyperexcitability or depletion of inhibitory mechanisms 19,20 . However, recently, several new genes coding for proteins other than ion channels have been identified, such as chromatin remodelers, intracellular signaling molecules, metabolic enzymes, transcription factors, and mitochondrial complex genes 5,21,22 . The search term "epilepsy" OR "seizure" OR "epileptic syndrome" OR "epileptic encephalopathy" from 2016 to 2019 led to 66 entries in Online Mendelian Inheritance in Man. Although comprehensive discussion of all the discoveries is beyond the scope of this review, selected major advances are highlighted below.
    > ES trios have revealed the influence of de novo mutations as a genetic cause of severe epilepsies (Table 1). A recent study compared de novo variants identified in individuals with variable NDDs with and without epilepsy 23 . In the subset of 1,942 subjects with NDDs with epilepsy, 33 genes were observed to have significant excess of de novo variants, three of which had limited or no previous evidence of disease association: CACNA1E, SNAP25, and GABRB2. Nine de novo missense and two truncating variants in CACNA1E variants were identified in this cohort 23 . In a subsequent study, de novo variants in CACNA1E were identified in 30 individuals with DEE 16 . Detailed phenotyping revealed refractory infantile-onset seizures, severe hypotonia, and profound developmental delay, often with congenital contractures, hyperkinetic movement disorders, macrocephaly, and early death 16 . Functional analysis revealed consistent gain-of-function effects in R-type calcium channels. Some patients were seizure free on treatment with the anti-epileptic drug topiramate, which blocks R-type calcium channels. The condition is now catalogued as early infantile epileptic encephalopathy type 69 (#MIM 618285).

### [4] Cytogenomic epileptology
- Authors: I. Iourov, A. P. Gerasimov, M. Zelenova, N. Ivanova, O. S. Kurinnaia et al.
- Year: 2023
- Venue: Molecular Cytogenetics
- URL: https://www.semanticscholar.org/paper/ab5b2a77cbe744a9032f5e99810539a65107f9d5
- DOI: 10.1186/s13039-022-00634-w
- PMID: 36600272
- PMCID: 9814426
- Citations: 4
- Summary: Epileptic-associated cytogenomic variations require more profound research; ontological analyses of epilepsy genes affected by chromosomal rearrangements and/or CNVs with unraveling pathways implicating epilepsy-associated genes are beneficial for epileptology; and molecular neurocytogenetic analysis of postoperative samples are warranted in patients suffering from epileptic disorders.
- Evidence snippets:
  - Snippet 1 (score: 0.507)
    > However, molecular definition of loci and intracellular pathways affected by chromosomal aberrations remain usually elusive in the epileptic context. It is reasonable to suggest that genomic complexity of chromosomal rearrangements, which encompass from tens to hundreds of genes, hinders the possibility of uncovering molecular and cellular pathways to epilepsy in each affected individual. Since this sophistication leads to difficulties in developing the treatment of epilepsy, clinical interest is limited in cases of epileptic chromosomal abnormalities. Consequently, a large number of patients with chromosomal disorders and epilepsy cannot get appropriate care and treatment. To solve the problem, specific interpretational/bioinformatic methods are required for unraveling molecular mechanisms of epilepsy in chromosomal disorders.
    > Chromosomal imbalances affecting brain functioning are common and are able to involve random genomic loci of any size or even entire chromosomes (e.g. aneuploidy or gains/losses of whole chromosomes in cellular nuclei) [10,14]. Accordingly, to describe molecular mechanisms for specific epileptic condition in an affected individual, localization and ontologies of epilepsy-associated genes as well as candidate processes for epileptiform activity are to be known.
    > Somatic mosaicism is another source for alterations to functioning of the central nervous system. Molecular genetic analyses have repeatedly demonstrated that tissue-specific (brain-specific) mosaicism for causative mutations is detectable in individuals with neurodevelopmental diseases including a wide spectrum of epileptic disorders [15][16][17][18]. Generally, epilepsy is associated with the presence of cellular population affected by a mutation (gene mutation) and cellular population with the same mutation in the affected brain. More precisely, abnormal cells are more likely to be concentrated in epilepsyassociated brain lesions [19,20].

### [5] Delineation of functionally essential protein regions for 242 neurodevelopmental genes
- Authors: S. Iqbal, Tobias Brünger, Eduardo Pérez-Palma, Marie Macnee, A. Brunklaus et al.
- Year: 2022
- Venue: Brain
- URL: https://www.semanticscholar.org/paper/b226a7a3472a3026d9af453561a45563d322bf8c
- DOI: 10.1093/brain/awac381
- PMID: 36256779
- PMCID: 9924913
- Citations: 9
- Summary: A novel consensus approach that overlays evolutionary, and population based genomic scores to identify 3D essential sites (Essential3D) on protein structures is developed and demonstrated that the consensus annotation of Essential3D sites improves prioritization of disease mutations over single annotations.
- Evidence snippets:
  - Snippet 1 (score: 0.506)
    > Neurodevelopmental disorders (NDDs) are a group of congenital or early-onset conditions that affect about 2-5% of children worldwide. 1,2 DDs are characterized by neurocognitive deficits with symptoms ranging from mild impairments, allowing those affected to live reasonably everyday lives, to severe disorders that require lifelong care. 3,4 iverse factors such as gestational infection and maternal alcohol consumption contribute to NDDs. 5,6 However, inherited genetic variants that disrupt genes, encoding instructions for neuronal development and functioning, are major contributors to individual risk for NDDs and can, in fact, be causal for the disorder. 3,7 A few hundreds of such genes have been reported, [7][8][9][10][11][12][13] but most of them have only recently been identified. This novelty opens an avenue to extend the frontier of knowledge about these NDD-associated genes and their disease mechanisms; for example, identifying regions in the corresponding human proteins that are conserved for their molecular functions and should be constraint against deleterious mutations.
    > Previous studies have estimated that around 42-48% of patients with a severe developmental disorder carry a pathogenic de novo mutation in a protein-coding gene, with missense de novo mutations (i.e. a single nucleotide change leading to a single amino acid substitution) being more common compared to protein-truncating de novo mutations (PTVs; nonsense, frameshift and essential splice site variants 13 ). In contrast to PTVs, interpretation of missense variants is challenging due to their variegated functional outcomes depending on the amino acid substituted and the protein domain affected. Missense variants in the same NDD-associated gene can possess a range of pathogenicity, 3 causing mild-to-severe phenotypes and often leading to multiple clinically distinct disorders due to differences in the protein's altered molecular function. For example, different pathogenic SCN1A variants can lead to Dravet syndrome, a severe epilepsy syndrome, or generalized epilepsy with febrile seizures plus (GEFS+), a milder epilepsy manifestation. 14,15

### [6] Precision Therapeutics in Lennox–Gastaut Syndrome: Targeting Molecular Pathophysiology in a Developmental and Epileptic Encephalopathy
- Authors: Debopam Samanta
- Year: 2025
- Venue: Children
- URL: https://www.semanticscholar.org/paper/455479c1bfbea7b90b73c109228f67c813d13888
- DOI: 10.3390/children12040481
- PMID: 40310132
- PMCID: 12025602
- Citations: 19
- Influential citations: 1
- Summary: A narrative review explores precision therapeutic strategies for LGS based on molecular pathophysiology, including channelopathies, receptor and ligand dysfunction, receptor and ligand dysfunction, cell signaling abnormalities, cell signaling abnormalities, synaptopathies, and the repurposing of existing medications with mechanism-specific effects.
- Evidence snippets:
  - Snippet 1 (score: 0.505)
    > A key advantage of disease-modifying therapies is their potential to target pathogenic mechanisms early in the disease course, potentially preventing the progression of some infantile epileptic encephalopathies to LGS.
    > This narrative review explores precision therapeutic strategies based on specific monogenic causes and disease mechanisms relevant to LGS. A comprehensive literature search (PubMed, MEDLINE, ClinicalTrials.gov, conference abstracts from the American Academy of Neurology and American Epilepsy Society, and gray literature) was conducted through 19 February 2025 to identify established ASMs, repurposed and novel drugs, as well as various gene therapy approaches with potential relevance to LGS. Given that over 900 monogenic causes of DEEs have been identified-implicating diverse cellular components such as ion channels, receptors, synaptic proteins, signaling pathways, metabolic processes, and epigenetic regulators-this review discusses current and emerging precision therapeutics based on shared molecular mechanisms and the pathophysiology of select genes associated with LGS [17] (Table 1).
  - Snippet 2 (score: 0.487)
    > Lennox–Gastaut syndrome (LGS) is a severe childhood-onset developmental and epileptic encephalopathy characterized by multiple drug-resistant seizure types, cognitive impairment, and distinctive electroencephalographic patterns. Current treatments primarily focus on symptom management through antiseizure medications (ASMs), dietary therapy, epilepsy surgery, and neuromodulation, but often fail to address the underlying pathophysiology or improve cognitive outcomes. As genetic causes are identified in 30–40% of LGS cases, precision therapeutics targeting specific molecular mechanisms are emerging as promising disease-modifying approaches. This narrative review explores precision therapeutic strategies for LGS based on molecular pathophysiology, including channelopathies (SCN2A, SCN8A, KCNQ2, KCNA2, KCNT1, CACNA1A), receptor and ligand dysfunction (GABA/glutamate systems), cell signaling abnormalities (mTOR pathway), synaptopathies (STXBP1, IQSEC2, DNM1), epigenetic dysregulation (CHD2), and CDKL5 deficiency disorder. Treatment modalities discussed include traditional ASMs, dietary therapy, targeted pharmacotherapy, antisense oligonucleotides, gene therapy, and the repurposing of existing medications with mechanism-specific effects. Early intervention with precision therapeutics may not only improve seizure control but could also potentially prevent progression to LGS in susceptible populations. Future directions include developing computable phenotypes for accurate diagnosis, refining molecular subgrouping, enhancing drug development, advancing gene-based therapies, personalizing neuromodulation, implementing adaptive clinical trial designs, and ensuring equitable access to precision therapeutic approaches. While significant challenges remain, integrating biological insights with innovative clinical strategies offers new hope for transforming LGS treatment from symptomatic management to targeted disease modification.

### [7] Exploring the Landscape of Pre- and Post-Synaptic Pediatric Disorders with Epilepsy: A Narrative Review on Molecular Mechanisms Involved
- Authors: Giovanna Scorrano, Ludovica Di Francesco, Armando Di Ludovico, Francesco Chiarelli, S. Matricardi
- Year: 2024
- Venue: International Journal of Molecular Sciences
- URL: https://www.semanticscholar.org/paper/d194d701009fe8f817e4719aa1fcea9d399e1829
- DOI: 10.3390/ijms252211982
- PMID: 39596051
- PMCID: 11593774
- Citations: 6
- Summary: A narrative review of emerged molecular mechanisms related to NDDs and epilepsy due to defects in pre- and post-synaptic transmission focused on the most recently discovered SNAREopathies and AMPA-related synaptopathies.
- Evidence snippets:
  - Snippet 1 (score: 0.505)
    > Neurodevelopmental disorders (NDDs) are a group of conditions affecting brain development, with variable degrees of severity and heterogeneous clinical features. They include intellectual disability (ID), autism spectrum disorder (ASD), attention-deficit/hyperactivity disorder (ADHD), often coexisting with epilepsy, extra-neurological comorbidities, and multisystemic involvement. In recent years, next-generation sequencing (NGS) technologies allowed the identification of several gene pathogenic variants etiologically related to these disorders in a large cohort of affected children. These genes encode proteins involved in synaptic homeostasis, such as SNARE proteins, implicated in calcium-triggered pre-synaptic release of neurotransmitters, or channel subunit proteins, such as post-synaptic ionotropic glutamate receptors involved in the brain’s fast excitatory neurotransmission. In this narrative review, we dissected emerged molecular mechanisms related to NDDs and epilepsy due to defects in pre- and post-synaptic transmission. We focused on the most recently discovered SNAREopathies and AMPA-related synaptopathies.
  - Snippet 2 (score: 0.490)
    > The association between synaptic dysfunction and epilepsy underscores the importance of understanding the molecular underpinnings of these disorders. Many NDDs with epileptic manifestations involve variants in genes that regulate the formation, maintenance, and plasticity of synapses. proteins such as STXBP1 and TBC1D24 are essential for proper synaptic vesicle dynamics, and their disruption can lead to abnormal neurotransmitter release and epileptic seizures. Likewise, postsynaptic proteins like PSD-95, Shank, and Neuroligins, which play pivotal roles in organizing the postsynaptic density and ensuring effective receptor signaling, are frequently implicated in NDDs associated with seizures.
    > A prompt and accurate diagnosis of these conditions is crucial for optimizing patient care and improving patients' and their families' quality of life. Genetic testing should be routinely performed in all patients displaying NDDs associated with epilepsy or extraneurological comorbidities, as identifying the underlying genetic cause can guide personalized treatment strategies. This is particularly important given that many synaptic disorders can present with developmental and epileptic encephalopathy, where early intervention can modify the clinical trajectory and improve outcomes.
    > Concurrently, functional animal model studies and clinical trials on patients with synaptopathies and associated epilepsy should be carried out to enhance our understanding of the pathogenesis of these disorders. By deepening our knowledge of the molecular mechanisms involved in pre-and post-synaptic transmission, we can develop targeted therapies to restore synaptic function and potentially modify the natural history of these complex conditions.
    > Further understanding of the specific pathways affected in presynaptic versus postsynaptic synaptopathies will be crucial in developing more precise and effective treatments.
    > As for many other monogenic diseases with epilepsy, the variability in phenotypic expression could arise from several factors, including the possibility that a single variant may lead to multiple phenotypes, reflecting these genes' broad roles in neural development, synaptic function, and brain connectivity. In other cases, different variants within the same gene may result in distinct phenotypes.

### [8] Editorial: In vitro and in vivo models for neurodevelopmental disorders
- Authors: Angelica D’Amore, Maria Marchese, Wardiya Afshar-Saber, M. Hameed
- Year: 2023
- Venue: Frontiers in Neuroscience
- URL: https://www.semanticscholar.org/paper/363a97d218672cdde3cc7a46abc26b7506313422
- DOI: 10.3389/fnins.2023.1239577
- PMID: 37502680
- PMCID: 10368529
- Citations: 3
- Summary: In vitro and in vivo models for neurodevelopmental disorders and how these models change over time are studied are studied.
- Evidence snippets:
  - Snippet 1 (score: 0.504)
    > In vitro and in vivo models for neurodevelopmental disorders Neurodevelopmental disorders (NDDs) are a group of disorders affecting brain development and function. Each disorder within this heterogenous group (i.e., intellectual disability/ID, autism spectrum disorder/ASD, attention-deficit/hyperactivity disorder etc.) has distinct clinical characteristics and phenotypical variability. While each disorder is indeed defined by a set of symptoms, individual symptoms are not necessarily restricted to one disorder. Comorbidity of two or more NDDs is frequently observed: for instance, a combination of ID, ASD, and epilepsy is commonly reported in patients (Parenti et al., 2020). Many NDDs have strong genetic bases and several hundred genes have been implicated in such NDDs either through genetic association studies, rare mutations, copy number variation etc. However, there is a significant proportion of NDDs with an unknown genetic cause (i.e., idiopathic) and, in those instances, the diagnosis is based only on interviews and medical examination. To date, several pathways have been associated with NDDs (mTOR, WNT, pathways associated with chromatin remodeling and synaptic function etc.) and understanding the molecular mechanism behind NDDs has the potential to define druggable targets, making in-vitro and in-vivo disease models fundamental tools for advancing the field (Thapar et al., 2017;Cardoso et al., 2019;Bozzi and Fagiolini, 2020;Nussinov et al., 2023).
    > In the last decades, the scientific community has been focusing on investigating the cellular and molecular mechanisms behind NDDs, trying to develop effective tools, using both in-vitro and in-vivo models. These complex disorders can be modeled using either animal models, such as rodents and zebrafish, or cellular models like iPSCs, enabling behavioral and functional analyses in the presence of disease-causing mutations.

### [9] Further delineation of EBF3-related syndromic neurodevelopmental disorder in twelve Chinese patients
- Authors: Jitao Zhu, Wenhui Li, Sha Yu, Wei Lu, Qiong Xu et al.
- Year: 2023
- Venue: Frontiers in Pediatrics
- URL: https://www.semanticscholar.org/paper/a102a60d4a7104dbfc9de63bba735fb74a2594bd
- DOI: 10.3389/fped.2023.1091532
- PMID: 36937983
- PMCID: 10020332
- Citations: 4
- Summary: This study further expanded the gene mutation spectrum of EBF3-related NDD by identifying five missense variants (four novel variants and one known variant) and seven copy number variations (CNVs) of E BF3 gene using next-generation sequencing.
- Evidence snippets:
  - Snippet 1 (score: 0.497)
    > Neurodevelopmental disorders (NDDs) account for a significant proportion of congenital disorders, which impose an enormous financial burden on families and society. Researches have suggested that hundreds of genes are involved in the pathogenesis of NDDs, but the underlying mechanisms remain unclear (1). Affected individuals present with various neurological symptoms, including developmental delay (DD), intellectual disability (ID), autism spectrum disorder (ASD), epilepsy and other minor symptoms such as decreased pain sensitivity or hyperactivity (2,3). In addition, patients may also present with phenotypes in other systems, such as congenital heart defects, skeletal or muscular abnormalities, metabolic disorders, gastrointestinal problems, distinctive facial features or strabismus, etc. Despite the high heterogeneity of pathogenic genes and the diverse clinical features of NDDs, advances in next-generation sequencing technology have facilitated the diagnosis of such diseases (4,5).
    > EBF3 is one of the causative genes that lead to syndromic NDDs. The earliest reports of EBF3-related NDD dated back to 2017, in which a total of 21 cases were summarized and analyzed (6)(7)(8). In their description, multiple systems were involved, including central nervous system (CNS), genitourinary system, skeletal system, etc. Major phenotypes included DD/ID, ataxia, hypotonia, structural CNS malformations, genitourinary abnormalities, subtle facial features, and strabismus. Other less common phenotypes included dysarthria, constipation, decreased pain sensitivity during development, and behavioral deficits such as attention deficit and ASD or ASD-like symptoms. Since then, more than 30 additional cases of EBF3-related NDDs have been reported (9)(10)(11)(12)(13)(14)(15)(16). A recent meta-analysis integrated previously published 42 cases with detailed patient information and their 41 new cases, and quantified the risk and severity of patient phenotypes based on these 83 patients (17).

### [10] Novel Compound Heterozygous Mutation in TRAPPC9 Gene: The Relevance of Whole Genome Sequencing
- Authors: M. I. Álvarez-Mora, J. Corominas, C. Gilissen, Aurora Sánchez, I. Madrigal et al.
- Year: 2021
- Venue: Genes
- URL: https://www.semanticscholar.org/paper/3e788272810efce3dc4aa96d2c9de7e1549554dc
- DOI: 10.3390/genes12040557
- PMID: 33921338
- PMCID: 8068822
- Citations: 18
- Influential citations: 1
- Summary: A case report of two siblings affected with severe ID and other comorbidities, who embarked on a genetic testing odyssey until diagnosis was reached by using whole genome sequencing (WGS), demonstrating the clinical utility of WGS in patients who remain undiagnosed after whole exome sequencing.
- Evidence snippets:
  - Snippet 1 (score: 0.482)
    > Neurodevelopmental psychiatric disorders, including autism spectrum disorder (ASD), intellectual disability (ID), epilepsy, and schizophrenia (SZ), are a group of heterogeneous disorders associated mainly with the disruption of the tightly coordinated events that lead to brain development [1]. This process results from highly complex and coordinated activity involving genetic and environmental processes. This group of disorders constitutes a serious health problem in our society, accounting as a group for one of the top 30 leading contributors to overall disease burden, as measured by global disability adjusted life years [2].
    > Neurodevelopmental disorders (NDDs) are associated with a sex bias, with a male:female ratio of 2:1 existing among individuals with ID and a 4:1 ratio for individuals with ASD [3]. NDDs are clinically heterogeneous, with overlapping symptoms, and frequently co-occur, suggesting a common genetic etiology; this explains the high degree of comorbidity among them [4]. Much like their phenotypes, the genetic etiology underlying NDDs is highly heterogeneous, with varying degrees of genetic overlap and penetrance, or expressivity, across phenotypes. Many studies have suggested shared molecular pathways for ID and other NDDs. This has been inspired by the high comorbidity that is commonly observed between ID and other cognitive impairments such as ASD and epilepsy [5]. Insights from "The Psychiatric Cell Map Initiative" have evidenced three main molecular pathways involved in these disorders: protein synthesis, transcriptional or epigenetic regulation and synaptic signaling [6,7].
    > Advances in high-throughput technologies and their implementation worldwide have had a considerable impact on elucidating the molecular causes underlying NDDs, especially for ID and ASD [5]. The introduction of whole exome sequencing (WES) into medical practice has transformed the diagnosis and management of patients with genetic disease. Nevertheless, etiology remains elusive in close to 50% of NDD cases, even in those families with multiple affected individuals, strongly hinting at a genetic cause.

### [11] Brain Organoids as Model Systems for Genetic Neurodevelopmental Disorders
- Authors: Simona Baldassari, I. Musante, M. Iacomino, F. Zara, V. Salpietro et al.
- Year: 2020
- Venue: Frontiers in Cell and Developmental Biology
- URL: https://www.semanticscholar.org/paper/20966871cdee3a028915b5ea9acb02db54fbfd5e
- DOI: 10.3389/fcell.2020.590119
- PMID: 33154971
- PMCID: 7586734
- Citations: 44
- Influential citations: 1
- Summary: Emerging methodological approaches in the field of brain organoid technologies and their application to dissect disease mechanisms underlying an array of pediatric brain developmental disorders, with a particular focus on autism spectrum disorders (ASDs) and epileptic encephalopathies are summarized.
- Evidence snippets:
  - Snippet 1 (score: 0.477)
    > Neurodevelopmental disorders (NDDs) encompass a range of frequently co-existing conditions that include intellectual disability (ID), developmental delay (DD), and autism spectrum disorders (ASDs) (Heyne et al., 2018;Salpietro et al., 2019). ASDs represent a complex set of behaviorally defined phenotypes, characterized by impairments in social interaction, communication and restricted or stereotyped behaviors (Chen et al., 2018). Epilepsy and NDDs frequently occur together, and when refractory seizures are accompanied by cognitive slowing or regression, patients are considered to have an epileptic encephalopathy (EE) (Scheffer et al., 2017). Both ID and ASDs are clinically and etiologically heterogeneous and a unifying pathophysiology has not yet been identified for either the disorder as a whole or its core behavioral components (Myers et al., 2020). Family and twin studies suggest high (0.65-0.91) heritability (Chen et al., 2018) and genetic dissection of the complex molecular architecture of ID/ASD is revealing contributions from both coding and non-coding DNA changes (Williams et al., 2019). Chromosomal microarray and next-generation sequencing (NGS) led over the last decade to the identification of a number of de novo and inherited variants implicated in the molecular etiology of ID/ASD variably associated with epilepsy (Wang et al., 2019). Deleterious variants in the same genes are often implicated in multiple NDDs characterized by autistic features and other comorbidities such ID, seizures or developmental epileptic encephalopathies, and neuropsychiatric conditions including schizophrenia and attention-deficit/hyperactivity disorder (O'Donovan and Owen, 2016). Defining the full spectrum of defective molecular pathways will help diagnose, monitor and accelerate treatment development in genetic NDDs (Lombardi et al., 2015). Currently, susceptibility and major mendelian alleles identified in NDDs explain only a small percentage of risk, and most of the work is still ahead to uncover the complex genetics of these disorders.

### [12] De novo MAP2K4 variants cause a novel neurodevelopmental syndrome with impaired JNK signaling in iPSC-derived neurons
- Authors: T. Nomakuchi, Alyssa L. Rippert, Sabrina A. Santos De León, Elizabeth M. Gonzalez, Dong Li et al.
- Year: 2025
- Venue: medRxiv
- URL: https://www.semanticscholar.org/paper/ed0a58bdca948781182e57e534bb5b46729f11ae
- DOI: 10.64898/2025.12.23.25342932
- PMID: 41480045
- PMCID: 12755259
- Summary: These findings establish MAP2K4 as a Mendelian neurodevelopmental disorder gene and identify impaired JNK signaling as the underlying mechanism and expands the spectrum of JNK-pathway disorders and underscores the critical role of JNK signaling in human brain development.
- Evidence snippets:
  - Snippet 1 (score: 0.476)
    > Here, we report a novel syndromic NDD caused by de novo MAP2K4 variants. The clinical features in our cohort included ID in the majority of living probands (7/8), structural brain anomalies on MRI in a subset, and epilepsy in half. Congenital malformations were frequent, particularly musculoskeletal (scoliosis, hip dysplasia, camptodactyly, vertebral anomalies) and genitourinary anomalies (ectopic kidney, megacystis, pyelectasis, hypospadias). Cardiac anomalies were less common and included ventricular septal defect and patent ductus arteriosus. Prenatal complications such as polyhydramnios, oligohydramnios and fetal growth restriction were observed in most pregnancies, and perinatal stroke occurred in two probands. Dysmorphic features were variable and nonspecific but often included downslanting palpebral fissures, long philtrum, and coarse facies. Our functional data confirms the reduction of JNK activation in cell lines with MAP2K4 haploinsufficiency, and abnormal neuronal differentiation.
    > In addition to highlighting MAP2K4 as a novel Mendelian neurodevelopmental disorder gene, our findings expand the spectrum of neurodevelopmental disorders linked to the JNK pathway. Mendelian NDD syndromes due to genes linked with the JNK pathway include MAP4K4, MAPK8IP3, TAOK1 and TAOK2-related NDD 13,16,27 . These syndromes share NDD phenotype as their core feature, with or without additional findings including structural brain anomalies and epilepsy. Because they have only recently been described, the full spectrum and defining characteristics of their NDD phenotypes, as well as their underlying mechanisms including the role of the JNK pathway, remain to be determined. MAP4K4, for instance, can regulate JAK-STAT, Notch, NF-8kB and MAPK/ERK pathways 16,17 .

### [13] Hypotonia and intellectual disability without dysmorphic features in a patient with PIGN-related disease
- Authors: I. Thiffault, Britton D. Zuccarelli, Holly I. Welsh, Xuan Yuan, E. Farrow et al.
- Year: 2017
- Venue: BMC Medical Genetics
- URL: https://www.semanticscholar.org/paper/2c58a10c237b0c776ed965ca40648661b6140268
- DOI: 10.1186/s12881-017-0481-9
- PMID: 29096607
- PMCID: 5668960
- Citations: 18
- Summary: This patient has no significant dysmorphic features or multiple congenital anomalies, which is consistent with recent reports linking non-truncating variants with a milder phenotype, highlighting the importance of functional studies in interpreting sequence variants.
- Evidence snippets:
  - Snippet 1 (score: 0.469)
    > was first reported to have a disease association in May of 2014, is represented on only 2 of 47 Epilepsy panels and 2 of 24 Autism/Intellectual disability panels listed in NextGxDx. The comparison of such gene lists is difficult for clinicians and the curation is onerous for the clinical laboratory to manage. Clinical WES/WGS removes the guesswork related to gene inclusion, since all genes relevant to the patient's phenotype are queried in the analysis process. In the current case, by using WES in a young child with hypotonia, seizures, a diagnosis of PIGN-related disease was made.
    > The clinical severity of the cases reported to date seems to correlate with the predicted functional severity of the pathogenic variants seen in PIGN. The male we described here further supports the genotype-phenotype assertions. He has marked phenotypic overlap with the previously reported cases. More recently, Fryns syndrome can be caused by recessive mutations in PIGN, providing further evidence for genetic heterogeneity [16,17]. The patient we report and two recent published reports [13,15] suggest that major congenital anomalies are not a core feature of PIGN-related disorders and are associated only in the presence of two truncating variants. Evaluation for pathogenic variants in genes involved the GPI-anchor synthesis pathway, causing PIG-associated epilepsy/multiple congenital anomalies-hypotonia-seizures syndrome, should be considered in patients of all ethnicities with epilepsy, with or without additional features. The increasing number of phenotypes associated with pathogenic variants (coding and non-coding) in the GPI pathway suggests that expansion of genotype-phenotype correlations related to GPI pathophysiology still requires further investigations.

### [14] Pathogenic variants associated with speech/cognitive delay and seizures affect genes with expression biases in excitatory neurons and microglia in developing human cortex
- Authors: Jeffrey B. Russ, Alexa C. Stone, Kayli Maney, Lauren C. Morris, Caroline F. Wright et al.
- Year: 2024
- Venue: bioRxiv
- URL: https://www.semanticscholar.org/paper/b4665a0858d9bf4f226a4fb6bb85703b872ae27c
- DOI: 10.1101/2024.07.01.601597
- PMID: 39005386
- PMCID: 11245013
- Summary: By combining extensive phenotype datasets from subjects with neurodevelopmental disorders with massive human cortical snRNAseq datasets across developmental stages, cell-specific expression biases for genes in which pathogenic variants are associated with speech/cognitive delay and seizures are identified.
- Evidence snippets:
  - Snippet 1 (score: 0.466)
    > Neurodevelopmental disorders (NDDs) broadly encompass both macroanatomic congenital brain malformations, as well as microcircuit and molecular disorders of development, such as autism spectrum disorder, epilepsy, and developmental delay.Although any individual disorder may be somewhat rare, their cumulative prevalence is high and often results in significant, chronic disability for many pediatric patients.
    > 2][13] In fact, high rates of neurodevelopmental comorbidities have made it challenging to pinpoint the distinct genetic and cellular pathophysiology of individual neurodevelopmental symptoms and untangle them from the comorbid pathophysiology of co-existing neurodevelopmental condtions. 145][16][17][18][19] Large, national studies, such as the Deciphering Developmental Disorders (DDD) study, have begun depositing highly detailed, standardized phenotypic information into accessible databases and linking them with genome-wide data and specific genetic diagnoses. 16,20Despite an enhanced understanding of genotype-phenotype relationships for many genetic forms of NDDs, our understanding of the nuanced cortical pathophysiology that likely mediates the symptoms of these conditions remains sparse.Novel strategies are required to begin untangling the interplay between pathogenic genetic variants, their effect on highly specific cortical cell types, and the subsequent cell-specific dysfunction that underlies NDDs.
    > 2][23][24] Through this work, a hierarchy of distinct cortical cell types defined by their transcriptomic signatures has emerged, allowing us to probe the expression levels of tens of thousands of genes in individual cells from human postmortem cortex at increasing scale. 25,26Previous studies have used this information to evaluate the convergence of autism-associated genes 22,24,27 or congenital hydrocephalusrelated genes 28 in human cortical transcriptomic data.However, these studies evaluate only a single neurodevelopmental phenotype, include fewer than two hundred disease-related genes, and map them within transcriptomic datasets of fewer than 20,000 cells.

### [15] 2022 Overview of Metabolic Epilepsies
- Authors: Birutė Tumienė, C. Ferreira, C. V. van Karnebeek
- Year: 2022
- Venue: Genes
- URL: https://www.semanticscholar.org/paper/f6b7bbb183ecd8eed45d800b1043667770a2d126
- DOI: 10.3390/genes13030508
- PMID: 35328062
- PMCID: 8952328
- Citations: 18
- Influential citations: 1
- Summary: The main goals of this study were to identify the scope of metabolic epilepsies and to investigate their clinical presentation, diagnostic approaches and treatments, which may significantly change health outcomes if diagnosed in time.
- Evidence snippets:
  - Snippet 1 (score: 0.465)
    > Understanding the genetic architecture of metabolic epilepsies is of paramount importance, both to current clinical practice and for the identification of further research directions. Metabolic epilepsy, defined as epilepsy that results directly from an inherited metabolic disorder (IMD) in which seizures are a core symptom of the disorder [1], are at the intersection of the disciplines of biochemical and molecular genetics and epileptology. In the last decade, high-throughput gene-sequencing studies have yielded an abundance of discoveries that change the paradigms in both epilepsy genetics [2] and IMDs [3]. The International Classification of Inherited Metabolic Disorders (ICIMD), which was recently adopted and endorsed by the international metabolic community, expands the definition of IMDs according to the current understanding of molecular and cell biology and encompasses more than 1500 IMDs. This classification includes all conditions where the impairment of biochemical pathways is intrinsic to the disorder's pathomechanism, while the presence of a diagnostic metabolic biomarker is no longer a prerequisite [4]. In this ever-growing classification, vastly expanded conventional IMD categories such as congenital disorders of glycosylation can be found, as well as recently defined IMD groups such as congenital disorders of autophagy [5], disorders of metabolite repair/proofreading [6], and disorders of the synaptic vesicle cycle [7]. Metabolic epilepsies belong to various IMD groups [8,9]. A significant number of these diseases have specific treatments that may significantly change health outcomes if diagnosed in time. This treatment not only replaces or complements conventional treatment with antiseizure drugs (ASD), but also targets the pathophysiology of the disorder and other systemic symptoms besides seizures. In recent years, the number of treatable metabolic epilepsies has increased significantly due to major breakthroughs in treatment strategies, elucidation and targeting of diseases' molecular mechanisms and the application of new methodologies for clinical trials in small populations, which are applicable to rare diseases [8,10].

### [16] The function of Mef2c toward the development of excitatory and inhibitory cortical neurons
- Authors: Claire Ward, Lucas Sjulson, R. Batista-Brito
- Year: 2024
- Venue: Frontiers in Cellular Neuroscience
- URL: https://www.semanticscholar.org/paper/d05b2343a54f1801b46e0cc7c84c17d15fc3e1ff
- DOI: 10.3389/fncel.2024.1465821
- PMID: 39376213
- PMCID: 11456456
- Citations: 3
- Summary: How the transcription factor MEF2C, a risk factor for various NDDs, impacts cortical development is reviewed, using MEF2C loss-of-function as a study case to illustrate how brain dysfunction and altered behavior may derive from the dysfunction of specific cortical circuits at specific developmental times.
- Evidence snippets:
  - Snippet 1 (score: 0.463)
    > Brain development is a pivotal and meticulously orchestrated process, governed by numerous neurobiological pathways that lay the foundation for essential brain functions. It is likely that various NDDs share pathways and circuits that become altered during prenatal or early postnatal stages. A main challenge in NDD treatment is the fact that diagnosis often occurs after the most effective time for treatment. Early identification of biomarkers for NDDs is critical given its potential for early intervention. Another big challenge is that despite significant advancements in understanding the pathophysiology of NDDs, targeted and effective treatments are still rare. Identification of common NDD molecular pathways and circuit dysfunction could potentially serve as an early prognostic indicator for NDDs and allow for targeted therapies.
    > The convergence of genetic factors and the existence of critical periods of vulnerability for NDDs underscores the potential for drugs to target fundamental networks as soon as possible in order to prevent or mitigate clinical manifestations of NDDs. However, more work needs to be done to establish a causal link between molecular and circuit abnormalities, disease pathology, and abnormal behavior. Animal models offer the opportunity to comprehensively unravel the molecular, circuit, and temporal intricacies of NDDs, pinpointing potential therapeutic targets, and ultimately informing us about new treatment modalities. In particular, the mouse as a disease model can provide valuable tools in deciphering the intricate genetic landscape of NDDs as well as elucidating the molecular, cellular, and circuit impacts of diverse mutations toward brain development and disease physiology. Interestingly, pharmacological and gene therapy approaches have both been applied in Mef2c +/− models, rescuing both cellular and behavioral phenotypes (Tu et al., 2017;Li et al., 2023). Nonetheless, for animal models to be useful it is important to consider the fundamental differences between animal models and humans, especially during development.
    > Single-cell omics techniques, alongside non-invasive brain activity measures like EEGs, computational models, and bioinformatics network analysis, offer a pathway to delineate parallels between animal models and humans.

### [17] The genetic cause of neurodevelopmental disorders in 30 consanguineous families
- Authors: S. A. Paracha, Shoaib Nawaz, Muhammad Tahir Sarwar, Asma Shaheen, Gohar Zaman et al.
- Year: 2024
- Venue: Frontiers in Medicine
- URL: https://www.semanticscholar.org/paper/eb738ac139535c28d3420c60c67245e6a6e02853
- DOI: 10.3389/fmed.2024.1424753
- PMID: 39281811
- PMCID: 11392838
- Citations: 7
- Summary: A high frequency of ASPM variants in the genetic analysis of 30 consanguineous families exhibiting features of NDDs, particularly those associated with autosomal recessive primary microcephaly, contributes to studies on genotype–phenotype correlation, genetic counseling for families, and a deeper understanding of human brain function and development.
- Evidence snippets:
  - Snippet 1 (score: 0.451)
    > NDDs are a heterogeneous group of disorders associated with intellectual disability (ID), global developmental delay (GDD), epilepsy, mild-to-severe microcephaly, autism spectrum disorders (ASD), attention-deficit/hyperactivity disorders (ADHD), and learning disorders. These disorders lack precise boundaries in their clinical definitions, epidemiology, genetics, and other associated phenotypes, which can result in significant limitations in intellectual functioning and adaptive behavior (8). Additional features such as hearing impairment, speech and language disorders, ID, epilepsy, and learning disorders are commonly observed in NDD patients (4).
    > Approximately 40% of NDD ID conditions remain molecularly undiagnosed, and approximately 50% have an environmental etiology (36) Environmental factors include improper care during pregnancies, 3D protein modeling for the variant identified in five proteins, including ABAT, BCKDK, DDHD2, ERCC2, and SLC12A6. Protein modeling revealed that the identified variants in these proteins resulted in substantial changes in the secondary structures that might lead to improper folding, structure, and function, causing severe NDDs in the affected individuals of the families.
    > In the past few years, genetic, psychological, neuroanatomical, and molecular analyses of NDDs have led to the discovery of novel genes and the identification of associated pathways. These advances across all disciplines have brought us to a new scientific frontier that integrates molecular genetics with developmental cognitive neuroscience. Identifying variants in a population and discovering novel associated genes will enhance our current understanding of developmental brain disorders (37,38). Furthermore, prenatal genetic screening is crucial to prevent the proliferation of severe NDDs and protect future generations (39-43). Preventing rare genetic disorders such as NDDs before they become common is imperative..

## Notes

- This provider combines `search_papers_by_relevance` with `snippet_search`.
- No synthesis or second-stage model call is performed.