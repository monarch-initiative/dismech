---
provider: asta
model: Asta Scientific Corpus Retrieval
cached: false
start_time: '2026-11-26T19:09:32.829890'
end_time: '2026-11-26T19:09:37.025298'
duration_seconds: 4.2
template_file: templates/disease_pathophysiology_research_asta.md
template_sha: "f7329650955bb21ea272b1af717bf581fb46c355"
template_variables:
  disease_name: D-Lactate Dehydrogenase Deficiency
  mondo_id: MONDO:0009505
  category: Mendelian
  causal_genes: LDHD
  omim_id: OMIM:245450
  synonyms: D-lactic aciduria with susceptibility to gout
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
citation_count: 19
reference_validation:
  total_references: 37
  verified: 35
  not_found: 2
  unverifiable: 0
  confabulation_rate: 0.054
  relevance_assessed: 35
  on_topic: 9
  unresolved_references:
  - PMID:36430419
  - DOI:10.1007/s00018-025-05652-6
  needs_review: true
  validator_version: 0.8.0
term_validation:
  total_terms: 0
  verified: 0
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

Pathophysiology and clinical mechanisms of D-Lactate Dehydrogenase Deficiency. Core disease mechanisms, molecular and cellular pathways, involved genes and proteins, relevant metabolites or drugs, affected cell types and anatomical structures, disease progression, major clinical phenotypes and complications, and treatment-relevant mechanism papers.

## Output

# Asta Literature Retrieval: Pathophysiology and clinical mechanisms of D-Lactate Dehydrogenase Deficiency. Core disease mechanisms, molecular and...

This report is retrieval-only and is generated directly from Asta results.

- Papers retrieved: 19
- Snippets retrieved: 19

## Relevant Papers

### [1] PROCEEDINGS OF THE XIX CONGRESS OF THE ITALIAN SOCIETY OF MYOLOGY
- Authors: June, C. Minetti, A. Berardinelli, A. Aliverti, A. Ambrosini
- Year: 2019
- Venue: Acta Myologica
- URL: https://www.semanticscholar.org/paper/ef33e60e12f45e3b53f7dca4296ed13355e3b67b
- PMID: 31309183
- PMCID: 6598409
- Citations: 1
- Influential citations: 1
- Summary: European muscle MRI study in Limb Girdle Muscular Dystrophy Type 2A, a progressive myopathy caused by deficiency of calpain 3, a calcium-dependent cysteine protease of skeletal muscle, and it represents the most frequent type of LGMD worldwide.
- Evidence snippets:
  - Snippet 1 (score: 0.456)
    > ated, genomes, nuclear and mitochondrial DNAs. The genetic and biochemical intricacy of mitochondrial bioenergetics explains the extreme heterogeneity of mitochondrial disorders, a group of highly invalidating human conditions, for which no effective treatment is nowadays available. In addition to bioenergetic failure, other mechanisms are probably predominant in the pathogenesis of specific syndromes, such as alterations of cellular redox status, the production of reactive oxygen species, compromised Ca 2+ homeostasis, mitochondrial protein and organelle quality control, and mitochondrial pathways of apoptosis. By investigating selected families and patients, we have identified several new disease genes, each responsible of distinct defects of the respiratory chain, mtDNA metabolism, or both, associated with paediatric or adultonset clinical presentations. Recently published and still unpublished findings will be presented and discussed. Structural analysis and the creation of ad hoc recombinant lines in yeast, flies, and mice have allowed us to dissect out the molecular consequences of the ablation or defects of some of these proteins, and their physical status in normal and disease conditions. These models have also been exploited to implement experimental therapeutic strategies, based on gene and cell replacement, or pharmacological control of mitochondrial biogenesis. Background. Limb Girdle Muscular Dystrophy type 2A (LGMD2A) is a progressive myopathy caused by deficiency of calpain 3, a calcium-dependent cysteine protease of skeletal muscle, and it represents the most frequent type of LGMD worldwide. In the last few years, muscle magnetic resonance imaging (MRI) has been proposed as a tool for identifying patterns of muscular involvement in genetically disorders, and as a biomarker of disease progression in muscle diseases.

### [2] Rare biochemical & genetic conditions: clues for broader mechanistic insights
- Authors: A. Mentis, M. Dalamaga
- Year: 2025
- Venue: Cellular and Molecular Life Sciences: CMLS
- URL: https://www.semanticscholar.org/paper/7093ca07773a0427930c301ef5c28ce909e4abf9
- DOI: 10.1007/s00018-025-05652-6
- PMID: 40210765
- PMCID: 11985829
- Citations: 1
- Summary: Evidence is synthesized demonstrating how valuable knowledge of biochemical pathways related to rare disorders can be for biomedicine, which highlights the continued value of biochemical pathways and studies in understanding human pathophysiology and drug discovery even in the genomics era.
- Evidence snippets:
  - Snippet 1 (score: 0.453)
    > The discussion above highlights the importance of rare but distinct features (phenotypes, syndromes, or molecular responses) to human pathophysiology. However, distinct diseases like cancer and inborn errors of metabolism can share common and/or overlapping molecular pathways. For example, the rare biochemical disorder D-2-hydroxyglutaric aciduria type 2, which is caused by germline mutations in the isocitrate dehydrogenase 2 (IDH2) gene and which causes progressive brain damage, is treated with enasidenib, a drug that has been approved to treat a blood cancer, namely acute myeloid leukemia caused by somatic mutations in the IDH2 gene [28,29], Similarly, lonafarnib, a farnesyltransferase inhibitor with antineoplastic properties, also reduces Parkinson-related tau pathology through a lysosomeactivating mechanism involving the Rhes protein [30]. These approaches show how drugs can be repurposed based on shared mechanisms between apparently different disorders.
    > Additionally, biochemical substances previously considered byproducts of cellular metabolism, such as urea and lactate, have recently attracted considerable attention due to their mechanistic value. First, urea, a byproduct of nitrogen metabolism, has been reported as a cancer biomarker by increasing pyrimidine-to-purine conversion. The latter increases the number of DNA and RNA transversion mutations and, as such, increases the rates of hydrophobic tumor neoantigens responsive to immunotherapy [31]. Even if the precise impact of several variants remains unclear, enzymes that are part of the urea cycle (e.g., ornithine transcarbamylase) appear to provide metabolic clues about cancer survival and development, an area of potential future research interest [32,33]. Likewise, phenylalanine substitutions at the codon reassignment level enhance the repertoire of cell surface antigens under conditions of tryptophan depletion [34]. Third, lactate has recently been shown to be involved in DNA repair (namely, homologous recombination-mediated pathways) through lactylation of the Nijmegen breakage syndrome 1 (NBS1) protein.

### [3] Altered Redox Homeostasis in Branched-Chain Amino Acid Disorders, Organic Acidurias, and Homocystinuria
- Authors: E. Richard, L. Gallego-Villar, A. Rivera-Barahona, A. Oyarzábal, B. Pérez et al.
- Year: 2018
- Venue: Oxidative Medicine and Cellular Longevity
- URL: https://www.semanticscholar.org/paper/a02a988d26ef8a032bade854c27c8c28792a6dfa
- DOI: 10.1155/2018/1246069
- PMID: 29743968
- PMCID: 5884027
- Citations: 37
- Influential citations: 2
- Summary: The published data on mitochondrial dysfunction, oxidative stress, and impaired redox signaling in branched-chain amino acid disorders, other organic acidurias, and homocystinuria are described, along with recent studies exploring the efficiency of antioxidants and mitochondria-targeted therapies as therapeutic compounds in these diseases.
- Evidence snippets:
  - Snippet 1 (score: 0.448)
    > Dehydrogenase. MSUD (MIM #248600), caused by the deficiency of branched-chain α-ketoacid dehydrogenase complex (BCKDHc) activity, is characterized by elevated levels of BCAAs and their corresponding α-keto-acids (BCKAs) in body fluids and tissues, resulting in complex neurological phenotypes [37]. As the important gatekeeping enzyme that it is, BCKDHc is regulated by reversible phosphorylation catalyzed by a specific BCKD kinase (BCKDK) that inhibits BCKDHc function, halting the catabolic pathway of BCAAs [41], and a dephosphorylation catalyzed by the mitochondrial protein phosphatase PP2Cm (encoded by the PPM1K gene) that stimulates BCKDHc activity [42]. Optimal BCKDHc activity necessary to maintain BCAA homeostasis is achieved by the coordinated response of BCKDK and PP2Cm activities. Blockage or unrestrained BCAA metabolism through BCKDHc leads to a dysmetabolism of BCAAs resulting in MSUD or BCKDK deficiency (MIM #614923) (Figure 1), two different clinical conditions with a hallmark of neurological perturbation.
    > MSUD results from mutations in the genes E1α-BCKDHA (MIM #608348), E1β-BCKDHB (MIM #24861), and E2-DBT (MIM #248610) [37]. The disease affects 1 : 185,000 newborns worldwide and is manifested by diverse clinical phenotypes, ranging from the most severe form-seen in 70% of patients with MSUD and associated with a profound neurological impact and high mortality if not treated early-to mild forms that present during early development. The mechanisms underlying brain injury are not completely understood. Different studies have been carried out using chemical induction of the disease by BCAAs or BCKAs in cultured cells [43,44] and animal models [45][46][47][48].

### [4] Diagnosis and Clinical Management of Long-chain Fatty-acid Oxidation Disorders: A Review.
- Authors: Joshua Baker, B. Burton
- Year: 2021
- Venue: TouchREVIEWS in endocrinology
- URL: https://www.semanticscholar.org/paper/952c303d9b7cbf2095eb0d1ae7c7b3ab0d92c08d
- DOI: 10.17925/ee.2021.17.2.108
- PMID: 35118456
- Citations: 19
- Summary: This article reviews the major LC-FAODs and their clinical presentation and indicates that triheptanoin approval has improved the outcome for affected individuals.
- Evidence snippets:
  - Snippet 1 (score: 0.439)
    > Very long-chain acyl-CoA dehydrogenase (VLCAD) is the most common LC-FAOD. It is due to biallelic variants in ACADVL, which encodes an enzyme involved in the metabolism of acylcarnitines with 14-20 carbons. 1 Severely affected patients present in the neonatal period with the typical hypoketotic hypoglycaemia, hypotonia, myopathy, hepatic dysfunction, cardiomyopathy and cardiac arrythmias.
    > In the long-term, patients typically experience recurrent rhabdomyolysis and may exhibit cardiac disease progression with significant stress. With the expansion of newborn screening, many more individuals with a milder phenotype are being identified, with symptoms of skeletal myopathy and rhabdomyolysis not presenting until adolescence or adulthood; some may remain asymptomatic for life. 11 This milder form has now become the most commonly diagnosed phenotype. 11 ng-chain 3-hydroxyacyl-CoA dehydrogenase deficiency/trifunctional protein deficiency
    > Long-chain 3-hydroxyacyl-CoA dehydrogenase (LCHAD) and trifunctional protein (TFP) are two disorders that are clinically indistinguishable.
    > Molecularly, they can be differentiated through the evaluation of HADHA and HADHB. 1 Most affected patients present in infancy or early childhood with hypoglycaemia, hepatic dysfunction, cardiomyopathy and sudden death. LCHAD may also present with maternal HELLP (haemolysis, elevated liver enzymes, and a low platelet count) syndrome or acute fatty liver of pregnancy when the foetus is affected. Long-term sequelae include myopathy, recurrent rhabdomyolysis and exercise intolerance.
    > Unique phenotypic features of LCHAD/TFP include peripheral neuropathy and retinopathy. 12 Concern has also been raised for the increased comorbidities of intellectual disability and autism spectrum disorders in LCHAD. 13 Further research on the underlying mechanism is still required.

### [5] Changes in Serum Proteomic Profiles at Different Stages of Pregnancy Toxemia in Goats
- Authors: M. Uzti̇mür, C. N. Ünal, G. Akpinar
- Year: 2025
- Venue: Journal of Veterinary Internal Medicine
- URL: https://www.semanticscholar.org/paper/4b9c488b5dbd65d7b26fd2ad9aed70e8c4b59942
- DOI: 10.1111/jvim.70139
- PMID: 40492724
- PMCID: 12150350
- Citations: 2
- Summary: Understanding the serum proteome profiles of goats with pregnancy toxemia might help identify the proteomes and pathways responsible for the development of this disease and improve diagnosis and treatment.
- Evidence snippets:
  - Snippet 1 (score: 0.434)
    > The pathophysiology and progression of this disease are not fully understood.
    > Traditional biomedical research has focused on the analysis of single genes, proteins, metabolites, or metabolic pathways in diseases. This molecular reductionist approach is based on the assumption that identifying genetic variations and molecular components will lead to new treatments for diseases [13][14][15][16]. However, many diseases are complex and multifactorial, and in order to determine the phenotype of such diseases, it is necessary to understand the changes that occur in more than one gene, pathway, protein, or metabolite at the cellular, tissue, and organismal levels [17][18][19]. Therefore, in recent years, proteomics, as one field of multi-omics technologies, has helped in evaluating the complex pathogenetic mechanisms of different diseases from a broad perspective and has made substantial contributions [20,21]. In veterinary medicine, proteomic analysis of metabolic diseases such as ketosis [16], hypocalcemia [22], and fatty liver [23] in dairy cows has contributed valuable insights for the definition of new pathophysiological pathways and new diagnosis and treatment protocols for these diseases. The proteomic approach can contribute importantly to a broad and detailed understanding of the changes that occur at the organismal level associated with the increase in BHBA concentration in goats with pregnancy toxemia. Our aim was to evaluate the serum protein profiles of goats with SPT or CPT using proteomic techniques to determine the proteomic profiles of these animals and to identify the relevant pathophysiological mechanisms.

### [6] Exploring the contribution of mitochondrial dynamics to multiple acyl-CoA dehydrogenase deficiency-related phenotype
- Authors: S. Brandão, R. Ferreira, H. Rocha
- Year: 2019
- Venue: Archives of Physiology and Biochemistry
- URL: https://www.semanticscholar.org/paper/3fa2c0768599e679dca543d47a13fa756385ed12
- DOI: 10.1080/13813455.2019.1628065
- PMID: 31215835
- Citations: 6
- Summary: The role of mitochondria on the regulation of cell homeostasis through the production of ROS, mitophagy, apoptosis, and mitochondrial biogenesis is overviewed and multiple acyl-CoA dehydrogenase deficiency (MADD) is considered an interesting model to better understand this interplay.
- Evidence snippets:
  - Snippet 1 (score: 0.424)
    > Mitochondrial fatty acid b-oxidation disorders (FAOD) are a group of inherited metabolic disorders, affecting mitochondrial enzymes involved in the b-oxidation of fatty acids (Kompare andRizzo 2008, Sahai andMarsden 2009). These disorders are usually transmitted in an autosomal recessive pattern being individually rare, but together they represent a large and important group of inherited metabolic disorders (Sahai and Marsden 2009). The main affected organs include heart, liver and skeletal muscles (Kompare and Rizzo 2008). The mortality and morbidity rates associated with these conditions can be prevented, or at least decreased, if disorders are early recognized and treated (Sahai and Marsden 2009). Indeed, fatty acid oxidation disorders can lead to serious health problems and even to death if not treated or when the diagnosis is done too late. The advantages of an early intervention make this group of disorders main targets of newborn screening (NBS) programs worldwide (Sahai and Marsden 2009, Lindner et al. 2010, Rocha et al. 2014.
    > Among FAOD, multiple acyl-CoA dehydrogenase deficiency (MADD) is one of the screened disorders that present heterogeneous clinical phenotypes Goodman 1985, 2001), being recognized three clinical forms. Two severe neonatal-onset forms: with (type I) and without (type II) congenital abnormalities. The late-onset form (type III) is associated to milder phenotypes (Vockley and Whiteman 2002). In most FAOD, including MADD, the association between the phenotype and the genotype is not straightforward (Gregersen et al. 2001, Kompare and Rizzo 2008, Olsen et al. 2013. The observed clinical spectrum in MADD patients suggests that other specific molecular and cellular mechanisms may have a key role in MADD pathogenesis, in addition to mutations in the genes associated to this disease (Olsen et al. 2003, Gr€ unert 2014. These findings make MADD an interesting model to better understand the molecular mechanisms underlying the pathophysiology associated with MADD and other FAOD.
    > Herein, we overview FAO metabolism, its regulation and contextualize MADD, the chosen model to study mitochondrial dynamics disturbances in FAO. We also critically analyze the potential contribution of the molecular pathways

### [7] CHDH, a key mitochondrial enzyme, plays a diagnostic role in metabolic disorders diseases and tumor progression
- Authors: Yi-Fei Li, Xinzhuang Shen, Xiao-Wen Yang, F. Lian, Yanping Li et al.
- Year: 2023
- Venue: Frontiers in Genetics
- URL: https://www.semanticscholar.org/paper/4b93413fe5b96b65544a52be91f0df3ba2d2f3dd
- DOI: 10.3389/fgene.2023.1240650
- PMID: 37600654
- PMCID: 10433736
- Citations: 16
- Summary: The work evaluates the feasibility of CHDH as a molecular marker relevant to the diagnosis of some metabolic disorders diseases and tumors, which may provide new targets for the treatment of related diseases and tumor prognosis.
- Evidence snippets:
  - Snippet 1 (score: 0.424)
    > Human choline dehydrogenase (CHDH) is a transmembrane protein located in mitochondria. CHDH has been shown to be one of the important catalytic enzymes that catalyze the oxidation of choline to betaine and is involved in mitochondrial autophagy after mitochondrial damage. In recent years, an increasing number of studies have focused on CHDH and found a close association with the pathogenesis of various diseases, including tumor prognosis. Here we summarized the genomic localization, protein structure and basic functions of CHDH and discuss the progress of CHDH research in metabolic disorders and other diseases. Moreover, we described the regulatory role of CHDH on the progression of different types of malignant tumors. In addition, major pathogenic mechanisms of CHDH in multiple diseases may be associated with single nucleotide polymorphism (SNP). We look forward to providing new strategies and basis for clinical diagnosis and prognosis prediction of diseases by diagnosing SNP loci of CHDH genes. Our work evaluates the feasibility of CHDH as a molecular marker relevant to the diagnosis of some metabolic disorders diseases and tumors, which may provide new targets for the treatment of related diseases and tumors.

### [8] Mitochondrial Fatty Acid β-Oxidation Disorders: From Disease to Lipidomic Studies—A Critical Review
- Authors: I. Guerra, H. Ferreira, T. Melo, H. Rocha, S. Moreira et al.
- Year: 2022
- Venue: International Journal of Molecular Sciences
- URL: https://www.semanticscholar.org/paper/c48a05883ea26a50bd6ddfed9c444fb0b191f0b3
- DOI: 10.3390/ijms232213933
- PMID: 36430419
- PMCID: 9696092
- Citations: 93
- Influential citations: 4
- Summary: The need of mass-spectrometry-based lipidomic studies to understand (epi)lipidome remodelling in FAODs is highlighted, thus allowing to elucidate the pathophysiology and the identification of possible biomarkers for disease prognosis and an evaluation of therapeutic efficacy.
- Evidence snippets:
  - Snippet 1 (score: 0.419)
    > Mitochondrial fatty acid (FA) β-oxidation is a complex pathway which occurs in mitochondria to produce energy from lipids. The deficiency in specific transport proteins of FA or enzymes involved in FA β-oxidation is responsible for FA β-oxidation disorders (FAODs) [1]. More than 15 distinct disorders have been described, and the most prevalent FAODs are the medium-chain acyl-CoA dehydrogenase deficiency (MCADD), the longchain hydroxy acyl-CoA dehydrogenase deficiency (LCHADD), and the very long chain acyl-CoA dehydrogenase deficiency (VLCADD) [2]. The clinical severity and age of onset are highly variable [1]. There is some overlap in the clinical phenotypes of diverse FAODs, such as acute hypoketotic hypoglycaemia and encephalopathy episodes. Although cardiac arrhythmias can occur in both MCADD and long-chain FAODs, cardiomyopathy and myopathy occur only in the latter [3]. Clinical phenotypes, with potential life-threatening manifestations, are the consequence of energy deficiencies and toxic effects of FA and acylcarnitine (CAR) accumulation [4,5]. To manage these diseases, patients need to follow a life-long avoidance of long fasting, a normal/low-fat diet, and carbohydrate and carnitine supplementation [1]. Both the disturbance of FAO and diet modifications can cause changes in the lipidome in FAOD patients. These can have a role in disease pathophysiology, determining clinical manifestations and prognosis.
    > Lipids have multiple functions in cells/biofluids, namely as an energy source, or as a major components of cell membranes and signalling molecules. Disturbances in the lipid profile have been associated with the pathophysiology of several diseases [6][7][8][9][10]. In FAODs, changes in lipids, namely in free and esterified FAs of plasma, dried blood spots (DBSs), and tissues have been reported.

### [9] On the Molecular Basis of D-Bifunctional Protein Deficiency Type III
- Authors: Maija L. Mehtälä, M. Lensink, Laura P. Pietikäinen, J. Hiltunen, T. Glumoff
- Year: 2013
- Venue: PLoS ONE
- URL: https://www.semanticscholar.org/paper/fe3866ff6131921a474ef83d32b5931299cb3f46
- DOI: 10.1371/journal.pone.0053688
- PMID: 23308274
- PMCID: 3538638
- Citations: 12
- Influential citations: 1
- Summary: Despite variations not affecting the catalytic residues, enzyme kinetic performance of the recombinant protein variants were compromised to a varying extent and this can be judged as the direct molecular cause for D-BP deficiency.
- Evidence snippets:
  - Snippet 1 (score: 0.419)
    > D-BP deficiency results, via an unknown mechanism, in usually severe clinical abnormalities such as delayed psychomotor development, neonatal hypotonia and seizures, visual and hearing impairment, as well as craniofacial dysmorphic features [8]. Patients diagnosed with D-BP deficiency can be grouped into three groups: deficiency in both the hydratase and the dehydrogenase units (type I), the loss of activity of the hydratase unit of MFE-2 affecting the second reaction of b-oxidation (type II), or the loss of activity of the dehydrogenase unit of MFE-2 affecting the third reaction of b-oxidation (type III). The symptoms are the same regardless of the type of deficiency [9]. The clinical manifestations of D-BP deficient patients are similar to those of patients affected by a peroxisome biogenesis disorder collectively called the Zellweger spectrum disorders. Diagnosis of the deficiency is complemented by measurements of the levels of indicative fatty acids in plasma, fatty acids and enzyme activities in patient's cells, usually skin fibroblasts, and mutation analysis. Analyses have revealed both missense and nonsense mutations with varying effects on the protein structure and residual activity of either or both enzymatic domains of MFE-2 [10].
    > We have previously studied a cohort of 110 D-BP deficiency patients with clinical and biochemical data available [9]. Several of these patients presented milder symptoms and extended life span. In silico protein structural studies indicated a correlation between the severity of the disease and the degree of disturbance to the protein structure. In this paper we report further structurefunction studies with the aim to understand the molecular basis and the mechanisms leading to D-BP deficiency. Based on our previous studies all functional domains of human MFE-2 can be expressed and purified as stand-alone proteins that fold into their native conformations as fully active dimers [5][6][7]. When dimerization occurs the contacts in full-length MFE-2 are mainly between enzyme units of different monomers rather than within a monomer [7]. In this study we only focused on the variations located in the dehydrogenase domain to study the activity-stability relationship in vitro and in silico.

### [10] Baseline urinary metabolites predict albuminuria response to spironolactone in type 2 diabetes.
- Authors: S. Mulder, P. Perco, C. Oxlund, Uzma F Mehdi, T. Hankemeier et al.
- Year: 2020
- Venue: Translational research : the journal of laboratory and clinical medicine
- URL: https://www.semanticscholar.org/paper/e5f7ffaa67fba1fe09d82c2d3787ad398d175bb6
- DOI: 10.1016/j.trsl.2020.04.010
- PMID: 32438071
- Citations: 10
- Summary: The data suggest that urinary metabolites may be used as a tool to tailor optimal therapy and move in the direction of personalized medicine.
- Evidence snippets:
  - Snippet 1 (score: 0.418)
    > In-silico modeling of spironolactone mechanism of action and DKD pathophysiology. Network-based molecular models reflecting spironolactone mechanism of action as well as DKD pathophysiology were generated following previously described and successfully applied computational workflows. 8,9 n brief, molecular features associated with spironolactone were consolidated from 3 data sources, namely scientific literature, DrugBank, and a transcriptomics data set from DrugMatrix. Molecular features were defined as genes, transcripts, or proteins. Scientific articles annotated with spironolactone as major MeSH term were retrieved and genes were extracted using NCBI's gene2pubmed file. This set of genes was complemented by drug targets listed in DrugBank for spironolactone. 10 We further extracted transcripts being differentially expressed between spironolactone-treated and untreated kidney samples of animal models as stored in DrugMatrix. 11 The unique set of spironolactone associated molecular features was mapped onto a hybrid interaction network including protein-protein interaction data from IntAct, BioGrid, and Reactome together with computationally inferred relations. 12 Interactions between members of the spironolactone feature set were extracted and the MCODE algorithm was used to identify clusters of highly interconnected proteins. 13  previously published DKD molecular model was used which was constructed following the same logic using data from scientific literature as well as from Omics datasets in the context of DKD. 7 Proteomics data of the published CKD273 proteomics classifier were used in order to identify DKD processes linked with DKD progression by mapping the set of proteins in the CKD273 classifier onto the DKD molecular network thus defining progression-associated process units. 14 twork interference analysis and identification of candidate metabolites. Network alignment method was used to identify DKD molecular processes linked to DKD prognosis affected by spironolactone treatment on the molecular level. Metabolites linked to proteins in affected DKD molecular processes were identified via enzyme-metabolite associations as stored in the Human Metabolome Database and forwarded to measurements in clinical samples. 15

### [11] L- and D-Lactate: unveiling their hidden functions in disease and health
- Authors: Jianting Li, Peng Ma, Zhi-Zhen Liu, Jun Xie
- Year: 2025
- Venue: Cell Communication and Signaling : CCS
- URL: https://www.semanticscholar.org/paper/a5def141b1007c2e10028c176a467777b54a79da
- DOI: 10.1186/s12964-025-02132-z
- PMID: 40075490
- PMCID: 11905701
- Citations: 77
- Influential citations: 4
- Summary: This review synthesizes the current understanding of L- and D-lactate, offering insights into their potential as targets for therapeutic innovation and assess the therapeutic prospects of targeting lactate metabolism, highlighting emerging strategies for intervention in clinical settings.
- Evidence snippets:
  - Snippet 1 (score: 0.416)
    > In tumors, L-lactate activates endothelial cells and induces angiogenesis through HIF-dependent and HIF-independent pathways, which rely on MCT1-mediated lactate import and prolyl hydroxylate (PHD) inhibition [143,144]. Recently, a distinct HIF-independent mechanism in which accumulated lactate during hypoxia binds to NDRG3, preventing its degradation and further promoting angiogenesis, was identified [145]. Together, these findings underscore the potential of L-lactate as a therapeutic target in cardiovascular and developmental disorders. D-lactate, produced by gut bacteria, has been implicated in cardiovascular disease, as its translocation into systemic circulation may impact cardiovascular health, suggesting that gut barrier-targeted therapies may prevent cardiovascular events [146]. Elevated D-lactate levels aid in the diagnosis of acute appendicitis, with the potential to differentiate types of appendicitis in pediatric patients [147]. In cystic fibrosis, D-lactate is correlated with clinical severity and pancreatic insufficiency, as measured by the Shwachman-Kulczycki score [148]. Elevated D-lactate levels have also been observed in type 1 and type 2 diabetes, where gut dysbiosis and increased, intestinal permeability may contribute to systemic D-lactate elevation [149][150][151]. This correlation with diabetic complications, possibly through elevated methylglyoxal levels, suggests that D-lactate could serve as a diagnostic marker; however, further studies are needed to clarify its role in various conditions. Summary, it is worth noting that the regulation of diseases by L-and D-lactate exists within a complex network of interplay and mutual influence in diseases (Fig. 4). The impact of L-and D-lactate on inflammation could serve as a driving factor for the tumorigenesis. In addition, inflammation driven by L-and D-lactate, often linked to infectious diseases. Within this intricate network, L-and D-lactate emerges as a critical regulator, influencing intracellular signaling, gene expression, intercellular communication, and immune responses, thereby shaping disease progression.

### [12] Lactate and gastric cancer immunotherapy from regulatory mechanisms to therapeutic strategies: a critical review
- Authors: Yuan-Zhu Hao, Ya-Nan Zhang, Yu Zhang, Duo Yang, Dan Ren et al.
- Year: 2025
- Venue: European Journal of Medical Research
- URL: https://www.semanticscholar.org/paper/65ed5d34047e9c8a4e6679b2d3dee2ec69063852
- DOI: 10.1186/s40001-025-03383-9
- PMID: 41239494
- PMCID: 12619365
- Citations: 8
- Influential citations: 1
- Summary: This review elucidates the dual roles and clinical value of lactate in gastric cancer as both an energy substrate and a signalling molecule within the tumour microenvironment and positions lactylation as a critical metabolic–epigenetic bridge.
- Evidence snippets:
  - Snippet 1 (score: 0.415)
    > Functionally, D-lactylation is an important negative immune regulatory mechanism. K310 and other sites of p65, a key subunit of NF-κB, can be modified by D-lactylation, and its transcriptional activity can be inhibited, thus driving macrophages to polarise toward an anti-inflammatory M2 phenotype and establishing a negative feedback loop of "inflammation-lactylation-inhibition-inflammation" [86].
    > In tumour biology, this mechanism plays a pivotal role. D-lactylation enhances the immunosuppressive function of TAMs by modifying histones (such as H3K18la) or signalling proteins [87,88]. Moreover, chemoresistance can be induced by upregulating genes such as the glutamate-cysteine ligase catalytic (GCLC) subunit in colorectal cancer stem cells [89]. Clinically, activation of this pathway is associated with the severity of inflammatory diseases and the prognosis of patients with tumours [86], providing a new strategy for targeting the metabolicimmune crosstalk.
    > As a pivotal molecule in tumour metabolism, lactate plays a crucial role in the formation of the TME, interplay between metabolic and immune networks, and the precise regulation of lactylation modifications, gradually transitioning from fundamental mechanisms to clinical advancement. Studies have demonstrated significant breakthroughs in cancer treatment through regulatory strategies targeting lactate metabolic reprogramming in the TME. By employing specific interventions such as lactate dehydrogenase inhibitors and monocarboxylate transporter blockers, in conjunction with ICIs or chemotherapeutic agents, these strategies can synergistically reverse the immunosuppressive TME and enhance drug sensitivity [90,91]. The underlying mechanisms encompass the modulation of the HIF-1α/PD-L1 signalling axis [92][93][94], the remodelling of T-cell metabolic adaptability, and the activation of immunogenic cell death pathways [95][96][97].

### [13] Integrative analysis of mitochondrial and immune pathways in diabetic kidney disease: identification of AASS and CASP3 as key predictors and therapeutic targets
- Authors: Xin-Xin Yu, Yong-Zheng Hu, Wei Jiang
- Year: 2025
- Venue: Renal Failure
- URL: https://www.semanticscholar.org/paper/5a75314ef028d8821f1a85197d939c2935ca5fef
- DOI: 10.1080/0886022X.2025.2465811
- PMID: 39988817
- PMCID: 11852243
- Citations: 7
- Summary: These findings establish AASS and CASP3 as dual biomarkers and therapeutic targets, bridging mitochondrial-immune crosstalk to DKD pathogenesis and providing actionable insights for targeting kidney damage in diabetes.
- Evidence snippets:
  - Snippet 1 (score: 0.415)
    > DKD is a major debilitating complication of diabetes that often progresses to end-stage renal disease (ESRD) if untreated or poorly managed. DKD is characterized by a complex interplay of molecular and genetic alterations, including inflammation, oxidative stress, mitochondrial dysfunction, and apoptosis. These interwoven mechanisms contribute to the deterioration of kidney function and are critical for understanding the pathophysiology of the disease. Despite significant advances in our knowledge, the precise molecular pathways driving DKD remain incompletely understood, underscoring the need for continued research to identify novel biomarkers and therapeutic targets that can halt or even reverse disease progression.
    > In this study, we employed a multifaceted approach to elucidate the underlying genetic and molecular mechanisms of DKD. Through the analysis of publicly available datasets from the GEO, we identified a set of significant DEGs in DKD samples. Using WGCNA, we identified gene modules that were strongly associated with DKD traits, which provided a deeper understanding of the molecular networks underlying the disease. The functional enrichment analysis of these DEGs highlighted immune response pathways and mitochondria-related genes, suggesting that mitochondrial dysfunction is a key driver of DKD progression. Immune cell infiltration analysis revealed distinct immune signatures in DKD patients compared with healthy controls, reinforcing the concept that immune dysregulation plays a significant role in the pathogenesis of DKD. Furthermore, machine learning algorithms were employed to predict key regulatory genes, increasing our ability to identify potential biomarkers and therapeutic targets. These findings were validated in animal models, in which increased levels of ROS and altered gene expression of candidate genes were observed. Our study integrates advanced bioinformatics tools, machine learning techniques, and experimental validation to provide a comprehensive molecular landscape of DKD, identifying critical genes and pathways that could inform future therapeutic strategies. The identification of key genes such as AASS and CASP3, their functional implications, and their potential as therapeutic targets provides valuable insights into the pathogenesis of DKD.
    > The CASP3 gene encodes a cysteine-aspartic acid protease that plays a crucial role in the execution of apoptosis [20].

### [14] Metabolic reprogramming rewires aberrant immune responses to drive endothelial dysfunction in Kawasaki disease: a narrative review
- Authors: Zi-Xuan Zhao, Shu-Hui Wang, Xuan Li, Li-Yan Zhu, Hai-Tao Lv et al.
- Year: 2026
- Venue: Translational Pediatrics
- URL: https://www.semanticscholar.org/paper/f1557c6cd0fef8e4359dafb386e3fdef4f5e3056
- DOI: 10.21037/tp-2026-0494
- PMID: 42724070
- PMCID: 13559126
- Summary: An integrated overview of metabolic alterations in KD pathogenesis is provided, focusing on clinical observations, mechanistic insights, and experimental evidence, which highlights metabolic reprogramming as a key interface linking immune dysregulation, endothelial injury, and vascular complications in KD.
- Evidence snippets:
  - Snippet 1 (score: 0.415)
    > Future studies should prioritize elucidating the molecular mechanisms underlying kynurenine pathway dysregulation, validating clinically relevant metabolic biomarkers and therapeutic targets, and integrating multiomics approaches with longitudinal clinical trials to enable patient stratification and the development of precision, Future studies from multiple centers integrating metabolomics with single-cell transcriptomics, spatial omics, proteomics, and functional metabolic analyses might comprehensively define cell-type-specific metabolic programs in immune cells, endothelial cells, and vascular smooth muscle cells during KD progression. Particular attention should be directed toward elucidating how metabolic reprogramming regulates immune cell fate decisions, inflammatory signaling pathways, and endothelial integrity. Importantly, distinguishing protective metabolic adaptations from pathogenic metabolic alterations will be essential for identifying key metabolites and pathways that either drive or restrain disease progression in KD. Furthermore, mechanistic investigations are needed to determine how specific metabolites function as signaling regulators or as donor molecules for protein posttranslational modifications involved in immune responses and vascular injury. Such studies may help uncover novel mechanisms or biomarkers for disease diagnosis, risk stratification, and therapeutic monitoring in KD. In addition, further metabolic research of KD patient samples from different centers, together with validation of the related mechanisms using KD mouse models, will facilitate the identification of metabolic signatures associated with disease severity, treatment response, and long-term cardiovascular outcomes. Targeting dysregulated metabolites or metabolic pathways may offer a promising approach for preventing coronary artery complications and improving the long-term cardiovascular prognosis of patients with KD. distributed in accordance with the Creative Commons Attribution-NonCommercial-NoDerivs 4.0 International License (CC BY-NC-ND 4.0), which permits the noncommercial replication and distribution of the article with the strict proviso that no changes or edits are made and the original work is properly cited (including links to both the formal publication through the relevant DOI and the license). See: https://creativecommons.org/licenses/by-nc-nd/4.0/.

### [15] Therapies for Mitochondrial Disease: Past, Present, and Future
- Authors: M. Ball, N. V. Van Bergen, A. Compton, D. Thorburn, Shamima Abd Rahman et al.
- Year: 2025
- Venue: Journal of Inherited Metabolic Disease
- URL: https://www.semanticscholar.org/paper/196ee50a950f29bc4134cfb8fe6bdfa9a3a1468b
- DOI: 10.1002/jimd.70065
- PMID: 40714961
- PMCID: 12301291
- Citations: 19
- Influential citations: 1
- Summary: The latest developments in the pursuit to identify effective treatments for mitochondrial disease are examined and the barriers impeding their success in translation to clinical practice are discussed.
- Evidence snippets:
  - Snippet 1 (score: 0.414)
    > Mitochondrial disease is a diverse group of clinically and genetically complex disorders caused by pathogenic variants in nuclear or mitochondrial DNA‐encoded genes that disrupt mitochondrial energy production or other important mitochondrial pathways. Mitochondrial disease can present with a wide spectrum of clinical features and can often be difficult to recognize. These conditions can be devastating; however, for the majority, there is no targeted treatment. In the last 60 years, mitochondrial medicine has experienced significant evolution, moving from the pre‐molecular era to the Age of Genomics in which considerable gene discovery and advancement in our understanding of the pathophysiology of mitochondrial disease have been made. In the last decade, in response to the urgent need for effective treatments, a wide range of emerging therapies have been developed, driven by innovative approaches addressing both the genetic and cellular mechanisms underpinning the diseases. Emerging therapies include dietary intervention, small molecule therapies aimed to restore mitochondrial function, stem cell or liver transplantation, and gene or RNA‐based therapies. However, despite these advances, translation to clinical practice is complicated by the sheer genetic and clinical complexity of mitochondrial disease, difficulty in efficient and precise delivery of therapies to affected tissues, rarity of individual genetic conditions, lack of reliable biomarkers and clinically relevant outcome measures, and the dearth of natural history data. This review examines the latest developments in the pursuit to identify effective treatments for mitochondrial disease and discusses the barriers impeding their success in translation to clinical practice. While treatment for mitochondrial disease may be on the horizon, many challenges must be addressed before it can become a reality.

### [16] Mitochondrial Dysfunction in Diabetes: Shedding Light on a Widespread Oversight
- Authors: F. Iheagwam, A. J. Joseph, E. D. Adedoyin, Olawumi Toyin Iheagwam, S. A. Ejoh
- Year: 2025
- Venue: Pathophysiology
- URL: https://www.semanticscholar.org/paper/dbf8042761c1a5fc50f8cd894cc498505abac7cb
- DOI: 10.3390/pathophysiology32010009
- PMID: 39982365
- PMCID: 12077258
- Citations: 48
- Influential citations: 1
- Summary: This review aims to elucidate the complex link between mitochondrial dysfunction and diabetes, covering the spectrum of diabetes types, the role of mitochondria in insulin resistance, highlighting pathophysiological mechanisms, mitochondrial DNA damage, and altered mitochondrial biogenesis and dynamics.
- Evidence snippets:
  - Snippet 1 (score: 0.413)
    > The landscape of DM research is continuously evolving, with emerging technologies and approaches offering new insights into the pathophysiology of the disease and potential therapeutic targets. Advancements in omics technologies, encompassing genomes, transcriptomics, proteomics, and metabolomics, have transformed the molecular mechanisms underlying DM [134]. High-throughput sequencing techniques enable comprehensive analysis of genetic variants, gene expression profiles, protein abundance, and metabolite levels associated with DM and its complications [135]. Single-cell omics approaches provide unprecedented resolution and granularity, allowing researchers to dissect cellular heterogeneity and identify novel cell types, subpopulations, and signalling pathways involved in DM pathogenesis. Integrating multi-omics data sets offers a systems-level perspective of DM, unravelling complex networks of molecular interactions and regulatory circuits underlying disease progression [136].
    > In addition to omics technologies, advances in imaging modalities, such as MRI, PET, and optical imaging, enable non-invasive visualisation and quantification of metabolic, functional, and structural changes. Molecular imaging probes targeting specific biomarkers and metabolic pathways provide valuable insights into disease mechanisms and treatment responses in preclinical and clinical settings [85]. Despite significant progress in DM research, numerous unanswered questions and knowledge gaps persist, hindering the ability to develop effective prevention and treatment strategies. Key areas requiring further investigation include the role of epigenetics, environmental factors, and the microbiome in DM susceptibility and progression. Moreover, the interaction between environmental cues and genetic predisposition remains incompletely understood, highlighting the need for comprehensive multi-omics studies and large-scale epidemiological analyses to identify gene-environment interactions and modifiable risk factors for DM [137]. Furthermore, the heterogeneity of DM phenotypes and clinical outcomes poses a challenge for personalised medicine approaches, necessitating robust biomarkers and predictive models to stratify patients based on disease subtypes, prognosis, and treatment response [138].

### [17] The ties that bind: functional clusters in limb-girdle muscular dystrophy
- Authors: E. Barton, Christina A. Pacak, Whitney L. Stoppel, Peter B. Kang
- Year: 2020
- Venue: Skeletal Muscle
- URL: https://www.semanticscholar.org/paper/3493c658bb8716d789a05ddf292162832e064e47
- DOI: 10.1186/s13395-020-00240-7
- PMID: 32727611
- PMCID: 7389686
- Citations: 25
- Summary: A deeper understanding of these disease pathways could yield a new generation of precision therapies that would each be expected to treat a broader range of LGMD patients than a single subtype, thus expanding the scope of the molecular medicines that may be developed for this complex array of muscular dystrophies.
- Evidence snippets:
  - Snippet 1 (score: 0.411)
    > Pyridine nucleotide-disulfide reductase [55] Many of the protein functions listed require further confirmation or are disputed these methodologies. Those patients with moderate disease phenotypes regardless of the underlying causative gene mutation would likely fall into a category where there may be interest in testing a pharmacological treatment (that could be halted) but reduced interest in a more permanent experimental strategy. For all of the above-mentioned reasons, the identification of unifying therapeutic targets applicable to multiple subtypes of
    > LGMDs is highly desirable.
    > To identify such targets, we should first consider the question: What binds all of these LGMDs together? The two core phenotypic features are progressive proximal muscle weakness, along with characteristic signs of muscle fiber destruction on biopsy, referred to as "dystrophic" features. Nuances in clinical presentation have helped to distinguish some of the LGMDs, such as the frequent occurrence of difficulty walking on tiptoes in LGMD R2 (LGMD2B), caused by dysferlin deficiency. However, heterogeneity associated with variable ages of onset and ranges of severity makes it generally difficult to distinguish and diagnose LGMD subtypes based on clinical presentation alone. A change in perspective is in order to aid in understanding disease pathways responsible for clinical features even when the genetic mutation is unknown. Further, given the large number of genespecific LGMD subtypes, it could very well be that several major disease mechanisms may be shared across the family of diseases. Yet despite careful studies that have collectively determined the cellular localization of most proteins associated with LGMD (Fig. 1), there is limited knowledge of potentially unifying molecular disease mechanisms. We assert that the identification of functional clusters of these proteins, grouped by such common mechanisms, will streamline our understanding of the disease processes and identify therapeutic targets relevant to individuals in multiple disease subgroups, including individuals whose pathogenic mutations have not been found. By extension, this approach may serve as a tool to not only find common mechanisms, but may also help to distinguish LGMD subtypes that do not share similar functional patterns, and afford further refinement of potential treatments.

### [18] Wasting Mechanisms in Muscular Dystrophy
- Authors: Jonghyun Shin, Marjan M. Tajrishi, Y. Ogura, A. Kumar
- Year: 2013
- Venue: The international journal of biochemistry & cell biology
- URL: https://www.semanticscholar.org/paper/a4de726eec1b28151758e90b3b2bcc6ab5a101ca
- DOI: 10.1016/j.biocel.2013.05.001
- PMID: 23669245
- PMCID: 3759654
- Citations: 146
- Influential citations: 5
- Summary: Major cellular and molecular mechanisms leading to muscle wasting in muscular dystrophy are reviewed and it is suggested that aberrant activation of several signaling pathways aggravate pathological cascades in dystrophic muscle.
- Evidence snippets:
  - Snippet 1 (score: 0.410)
    > Muscular dystrophy is a group of more than 30 different clinical genetic disorders that are characterized by progressive skeletal muscle wasting and degeneration. Primary deficiency of specific extracellular matrix, sarcoplasmic, cytoskeletal, or nuclear membrane protein results in several secondary changes such as sarcolemmal instability, calcium influx, fiber necrosis, oxidative stress, inflammatory response, breakdown of extracellular matrix, and eventually fibrosis which leads to loss of ambulance and cardiac and respiratory failure. A number of molecular processes have now been identified which hasten disease progression in human patients and animal models of muscular dystrophy. Accumulating evidence further suggests that aberrant activation of several signaling pathways aggravate pathological cascades in dystrophic muscle. Although replacement of defective gene with wild-type is paramount to cure, management of secondary pathological changes has enormous potential to improving the quality of life and extending lifespan of muscular dystrophy patients. In this article, we have reviewed major cellular and molecular mechanisms leading to muscle wasting in muscular dystrophy.

### [19] New therapeutic targets in rare genetic skeletal diseases
- Authors: M. D. Briggs, P. A. Bell, M. Wright, K. A. Pirog
- Year: 2015
- Venue: Expert Opinion on Orphan Drugs
- URL: https://www.semanticscholar.org/paper/1363107f71ae6d2d60abca471cddf3da5d13644b
- DOI: 10.1517/21678707.2015.1083853
- PMID: 26635999
- PMCID: 4643203
- Citations: 40
- Influential citations: 1
- Summary: An overview of disease mechanisms that are shared amongst groups of different GSDs and potential therapeutic approaches that are under investigation are described to generate critical mass for the identification and validation of novel therapeutic targets and biomarkers.
- Evidence snippets:
  - Snippet 1 (score: 0.409)
    > However, emerging knowledge suggests that the primary genetic defect may be less important than the cells' response to the expression of the mutant gene product [107]. Moreover, the largely overlooked response of a cell (i.e. chondrocyte) to the abnormal extracellular environment is also important for disease progression as illustrated by several GSDs discussed in this review.
    > It is important that 'omics'-based approaches and technologies are systematically applied to the study of rare GSDs so that definitive reference profiles and disease signatures are generated for each phenotype. These can then be used in a Systems Biology approach to identify both common and dissimilar pathological signatures and disease mechanisms. This approach is entirely dependent upon relevant in vitro and in vivo models (and also novel 'disease-mechanism phenocopies' [107]) for testing new diagnostic and prognostic tools and for determining the molecular mechanisms that underpin the pathophysiology so that effective therapeutic treatments can be developed and validated. This approach will eventually lead to personalized treatments and care strategies centred on shared disease mechanisms with the use of relevant biomarkers to monitor the efficacy of treatment and disease progression.
    > It is vital that all relevant stakeholders are involved from the outset in defining the appropriate outcomes of any potential therapeutic regime. The perceptions of a successful therapy can differ widely between the clinical academic community and the relevant patient-support groups and it is vital that there is engagement on all these issues.
    > In summary, the identification of causative genes and mutations for GSDs over the last 20 years, coupled with the generation and in-depth analysis of a plethora of relevant cell and mouse models, has derived new knowledge on disease mechanisms and suggested potential therapeutic targets. The fast-evolving hypothesis that clinically disparate diseases can share common disease mechanisms is a powerful concept that will generate critical mass for the identification and validation of novel therapeutic targets and biomarkers.

## Notes

- This provider combines `search_papers_by_relevance` with `snippet_search`.
- No synthesis or second-stage model call is performed.

## Reference Validation

Checked with `linkml-reference-validator` 0.8.0.

| Outcome | Count |
| --- | --- |
| References checked | 37 |
| Resolved | 35 |
| Unresolved (possible confabulation) | 2 |
| Unverifiable | 0 |
| References weighed for topical relevance | 35 |
| On topic | 9 |
| Off topic | 0 |

### Unresolved references

These identifiers did not resolve to a record and may be fabricated. A lookup that failed for transport reasons is indistinguishable from one that failed because the record does not exist, so spot-check before acting on them:

- `PMID:36430419` (1 mention) - Identifier did not resolve to a record
- `DOI:10.1007/s00018-025-05652-6` (1 mention) - Identifier did not resolve to a record

## Term Validation

No ontology term identifiers were found in this report.