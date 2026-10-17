---
provider: asta
model: Asta Scientific Corpus Retrieval
cached: false
start_time: '2026-10-15T02:49:28.509936'
end_time: '2026-10-15T02:49:31.778574'
duration_seconds: 3.27
template_file: templates/disease_pathophysiology_research_asta.md
template_sha: "f7329650955bb21ea272b1af717bf581fb46c355"
template_variables:
  disease_name: Familial Hypocalciuric Hypercalcemia 2
  mondo_id: MONDO:0007792
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
citation_count: 20
reference_validation:
  total_references: 36
  verified: 36
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 36
  on_topic: 20
  validator_version: 0.3.0
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

Pathophysiology and clinical mechanisms of Familial Hypocalciuric Hypercalcemia 2. Core disease mechanisms, molecular and cellular pathways, involved genes and proteins, relevant metabolites or drugs, affected cell types and anatomical structures, disease progression, major clinical phenotypes and complications, and treatment-relevant mechanism papers.

## Output

# Asta Literature Retrieval: Pathophysiology and clinical mechanisms of Familial Hypocalciuric Hypercalcemia 2. Core disease mechanisms, molecular...

This report is retrieval-only and is generated directly from Asta results.

- Papers retrieved: 20
- Snippets retrieved: 20

## Relevant Papers

### [1] Hypercalcemia. Pathophysiological aspects.
- Authors: I. Z̆ofková
- Year: 2016
- Venue: Physiological research
- URL: https://www.semanticscholar.org/paper/07e1255348bd1f4ff5acccd8fe008c6696a91ac6
- DOI: 10.33549/PHYSIOLRES.933059
- PMID: 26596315
- Citations: 29
- Summary: The metabolic pathways that contribute to maintain serum calcium concentration in narrow physiological range include the bone remodeling process, intestinal absorption and renal tubule resorption, which contribute to hyper- or hypocalcemia.
- Evidence snippets:
  - Snippet 1 (score: 0.627)
    > The metabolic pathways that contribute to maintain serum calcium concentration in narrow physiological range include the bone remodeling process, intestinal absorption and renal tubule resorption. Dysbalance in these regulations may lead to hyper- or hypocalcemia. Hypercalcemia is a potentionally life-threatening and relatively common clinical problem, which is mostly associated with hyperparathyroidism and/or malignant diseases (90 %). Scarce causes of hypercalcemia involve renal failure, kidney transplantation, endocrinopathies, granulomatous diseases, and the long-term treatment with some pharmaceuticals (vitamin D, retinoic acid, lithium). Genetic causes of hypercalcemia involve familial hypocalciuric hypercalcemia associated with an inactivation mutation in the calcium sensing receptor gene and/or a mutation in the CYP24A1 gene. Furthermore, hypercalcemia accompanying primary hyperparathyroidism, which develops as part of multiple endocrine neoplasia (MEN1 and MEN2), is also genetically determined. In this review mechanisms of hypercalcemia are discussed. The objective of this article is a review of hypercalcemia obtained from a Medline bibliographic search.

### [2] Applications of Metabolomics in Calcium Metabolism Disorders in Humans
- Authors: B. Podgórska, Marta Wielogórska-Partyka, J. Godzień, Julia Siemińska, M. Ciborowski et al.
- Year: 2022
- Venue: International Journal of Molecular Sciences
- URL: https://www.semanticscholar.org/paper/c9aadd33d0b446d2859296c5b9d0ee0e69c43d59
- DOI: 10.3390/ijms231810407
- PMID: 36142318
- PMCID: 9499180
- Citations: 13
- Summary: The present review highlights the potential of metabolomics in identifying the biomarkers of some of the most common endocrine disorders, such as primary hyperparathyroidism (PHPT), secondary hyper parathyroidisms (SHPT), calcium deficiency, osteoporosis and vitamin D supplementation.
- Evidence snippets:
  - Snippet 1 (score: 0.541)
    > It occurs either sporadically or as a familial, hereditary abnormality. The phenotypic diversity of PHPT clinical presentation may be due to the subclasses of parathyroid tumors with distinct molecular profiles [11]. Similarly to PHPT, familial hypocalciuric hypercalcemia (FHH) is a state that also leads to hypercalcemia and the elevation of PTH. Nevertheless, FHH is a rare inherited disorder with a mutation in the CaSRs. The opposite perturbation to hypercalcemia is hypocalcemia, which occurs in vitamin D deficiency and hypoparathyroidism due to irreversible parathyroidectomy, congenital disabilities or radiation damage [12,13].
    > Changes in calcium levels can induce a wide spectrum of symptoms, including skeletal anomalies, nephrolithiasis and muscle spasms [1]. This frequently affects patients' quality of life and despite the great pressure on the development of novel methods of diagnosis and treatment, medical approaches to calcium metabolism disorders often pose a significant diagnostic challenge [14]. Functional analyses have become increasingly popular. Among these, metabolomics is the comprehensive analysis of the entire metabolome. This discipline enables the high-throughput analysis of metabolites from cells, tissues, organs and biofluids using modern analytical chemistry techniques [15]. Metabolomics is an important 'omic' approach. Metabolites, i.e., small molecules, are markers of various biological processes [1]. The growing popularity of metabolomics and the metabolites' capacity to serve as sources of novel potential biomarkers used in screening diseases and efficient therapies are observed in various medical disciplines. The metabolome can be explored through either the untargeted analysis of a wide set of unknown metabolites or the targeted quantification of pre-defined known metabolites [16].
    > Metabolomics is still a relatively new field of science that links cellular phenotypes to their genotypes and delivers biochemical information associated with the regulation of specific gene transcripts [17]. Environmental factors may also induce metabolic changes.

### [3] Single-cell profiling resolves gain- and loss-of-function mechanisms in CASR to advance mechanism-aware variant classification
- Authors: S. Padigepati, David A. Stafford, Y. Kobayashi, Christopher A. Tan, Joseph Kim et al.
- Year: 2026
- Venue: bioRxiv
- URL: https://www.semanticscholar.org/paper/1727abf71331fa7eaa5589bca437e34a0ad86551
- DOI: 10.64898/2026.09.26.754690
- Summary: The effectiveness of using molecular mechanism annotations with scRNA-seq to train models that distinguish molecular mechanisms of pathogenicity in CASR has immediate relevance for clinical variant classification and establishes a foundation for mechanism-guided clinical management in disorders with mechanism-dependent interventions.
- Evidence snippets:
  - Snippet 1 (score: 0.528)
    > Here, we present a generalizable framework for predicting disease-specific mechanisms of pathogenicity in genes associated with multiple disorders. We combine single-cell RNA sequencing-based variant effect measurements with supervised machine learning, leveraging expert-curated sets of variants with known disease associations. We selected the calciumsensing receptor gene (CASR) as a model system because pathogenic variants in CASR are associated with two distinct clinical entities with opposing molecular etiologies: LOF variants cause familial hypocalciuric hypercalcemia type 1 (FHH1), 11 characterized by mild hypercalcemia with inappropriately low urinary calcium excretion, while GOF variants cause autosomal dominant hypocalcemia type 1 (ADH1), 12 marked by hypocalcemia with relative hypercalciuria. Using this system, we show that this integrated approach can not only identify pathogenic variants but also predict their specific disease mechanism, thereby enabling more precise clinical interpretation. This framework offers a path forward for resolving VUS in genes where multiple disease mechanisms complicate variant classification.

### [4] A novel missense variant of the calcium-sensing receptor gene associated with familial hypocalciuric hypercalcemia
- Authors: Martina Laganà, Anna Maria Grieco, V. Guarnieri, M. Castori, R. Pracella et al.
- Year: 2025
- Venue: JBMR Plus
- URL: https://www.semanticscholar.org/paper/f3943b05c56b95ee09ad7c017ba39ab6f10e2be1
- DOI: 10.1093/jbmrpl/ziaf137
- PMID: 40978122
- PMCID: 12445840
- Summary: The present case expands the mutational spectrum of CASR and reinforces the clinical utility of multidisciplinary assessment for adults presenting with unexplained hypercalcemia.
- Evidence snippets:
  - Snippet 1 (score: 0.517)
    > Familial hypocalciuric hypercalcemia (FHH) is an autosomal dominant inherited disorder caused by deleterious variants of three different genes. FHH type 1 (FHH1) is the most common genetic form and is associated with inactivating variants in the gene CA SR, which encodes for the calcium-sensing receptor (CaSR). CaSR is expressed on parathyroid cells, regulates calcium levels, and, consequently, PTH synthesis and release. 1 In a few cases, FHH derives from deleterious variants in the G-protein subunit α11 gene (GNA11), encoding the GNa-11 protein implicated in downstream CaSR signal transduction (FHH2), or in the adaptor-related protein complex 2 (AP2), sigma 1 subunit gene (AP2S1) that encodes the clathrin-associated AP2S1 protein involved in CaSR endocitosis (FHH3). 2 Loss-of-function (LoF) alterations in these genes increase the set-point for calcium sensing and consequently shift suppression of PTH secretion to a higher threshold of serum calcium concentration. Consequently, serum calcium exceeds the normal range, whereas serum PTH is inappropriately normal or mildly elevated, as the mechanism of negative feedback is compromised. Moreover, LoF variants lead to an increase in renal threshold for calcium tubular reabsorption, resulting in a lower renal calcium excretion than what is expected from the enhanced filtered load of calcium. 1,3,4 he differential diagnosis between FHH and other causes of hypercalcemia, mainly primary hyperparathyroidism (PHP), may be challenging, owing to variability in presentation and significant overlap, but it appears crucial for prognosis and correct treatment.
    > Familial hypocalciuric hypercalcemia remains largely underdiagnosed due to its frequently benign clinical course. Despite the rarity of the condition, clinicians should be advised to screen for FHH in patients with suggestive biochemical data (asymptomatic hypercalcemia and hypocalciuria) to prevent superf luous tests and unnecessary surgical treatment.

### [5] Case Reports of Patients Diagnosed with Familial Hypocalciuric Hypercalcemia, A Disorder That Should be Kept in Mind in Hypercalcemia Cases
- Authors: A. Buluş, Y. Yaşartekin, A. Ceylan
- Year: 2022
- Venue: Trends in Pediatrics
- URL: https://www.semanticscholar.org/paper/05149d137a5977f214eef939b4da643ece818f33
- DOI: 10.4274/tp.2022.83007
- Summary: A family diagnosed with FHH is presented, having heterozygous CaSR mutations in three generations, and failure to diagnose FHH may result in unwarranted treatment or surgery for a false diagnosis of primary hyperparathyroidism, given the significant overlap of biochemical features.
- Evidence snippets:
  - Snippet 1 (score: 0.515)
    > Y, Ceylan Case Reports of Patients Diagnosed with Familial Hypocalciuric Hypercalcemia, A Disorder that Should be Kept in Mind in Hypercalcemia Cases. Trends ABSTRACT Familial hypocalciuric hypercalcemia (FHH) causes hypercalcemia by three genetic mechanisms: Inactivating mutations in the calcium-sensing receptor ( CaSR ), G-protein subunit α11 or adapter-associated protein complex 2, sigma 1 subunit. In other cases, hypercalcemia causes significant morbidity and mortality, while FHH usually follows a benign course. Failure to diagnose FHH may result in unwarranted treatment or surgery for a false diagnosis of primary hyperparathyroidism, given the significant overlap of biochemical features. Patients carrying a heterozygous loss-of-function mutation in the CaSR gene are typically referred to as FHH-type 1 (FHH1). Although FHH1 causes lifelong hypercalcemia, it is usually benign and asymptomatic. FHH is the most common syndrome of CaSR gene mutation; it may sometimes be associated with a hypercalciuric tendency depending on the variant. Although hypercalcemia is a frequently encountered condition in our clinical practice, FHH is a clinic that we do not often think of. This paper presents a family diagnosed with FHH, having heterozygous CaSR mutations in three generations.

### [6] Successful prednisolone or calcimimetic treatment of acquired hypocalciuric hypercalcemia caused by biased allosteric CaSR autoantibodies
- Authors: N. Makita, Junichiro Sato, Katsunori Manaka, Kimiko Akahane, Takahiro Ito et al.
- Year: 2022
- Venue: JCI Insight
- URL: https://www.semanticscholar.org/paper/394952935bd7c3b71b69dda4b7a8db2dc9a6c102
- DOI: 10.1172/jci.insight.156742
- PMID: 36099030
- PMCID: 9714797
- Citations: 5
- Summary: 3 patients with symptomatic AHH who shared characteristics with the 2 cases previously reported are described, and their observations may provide new insights into the phenotype and characteristics of AHH and the mechanisms by which the biased agonism of GPCRs operate.
- Evidence snippets:
  - Snippet 1 (score: 0.498)
    > In the kidney, CaSR signaling activation in cells of the thick ascending loop of Henle results in hypercalciuria (23). Loss-of-function mutations of CaSR at 1 or both alleles inhibit CaSR signaling and cause increased PTH secretion, referred to as familial hypocalciuric hypercalcemia 1 (FHH1) and neonatal severe hyperparathyroidism (NSHPT), respectively (26,27). Also in the kidney, a CaSR signaling block in cells of the thick ascending loop of Henle causes hypocalciuria.
    > As an acquired disease analogous to ADH1, acquired hypoparathyroidism, including immune-checkpoint inhibitor-related hypoparathyroidism, has been reported to be caused by activating autoantibodies against CaSR (29)(30)(31)(32)(33)(34). Acquired hypocalciuric hypercalcemia (AHH), which is analogous to FHH1 or NSHPT, has been reported to be also caused by autoantibodies against CaSR (14,15,(35)(36)(37)(38). Depending on the reported AHH cases, autoantibodies work either as pure blocking entities (35) or in a biased manner (14,15). By investigating their mode of action, both the pathophysiological mechanisms underlying this heterologous disease from the perspective of the epitopes detected and possible effective treatments and the physiological mechanisms by which PTH secretion is regulated in the human body have been further elucidated (15).
    > In our present study, we report on 3 additional patients with AHH who were elderly men with no evidence of any other autoimmune disorders such as chronic thyroiditis, thus, differing from most autoimmune cases. This was also the case for the 2 patients with AHH we had previously described. These 3 individuals displayed symptomatic PTH-dependent hypercalcemia with hypocalciuria and were, thus, clinically suspected of having AHH. This diagnosis was subsequently confirmed using in vitro analysis. Their Ca levels spontaneously fluctuated from approximately normal to subfatally high ranges.

### [7] A novel CaSR mutation presenting as a severe case of neonatal familial hypocalciuric hypercalcemia
- Authors: Ksenia N. Tonyushkina, S. O'Connor, N. Dunbar
- Year: 2012
- Venue: International Journal of Pediatric Endocrinology
- URL: https://www.semanticscholar.org/paper/da3271fb1d616d9c9f5ef0a89d45faecc566225d
- DOI: 10.1186/1687-9856-2012-13
- PMID: 22620673
- PMCID: 3465174
- Citations: 16
- Influential citations: 1
- Summary: This neonate with intrauterine fractures and demineralization, moderate hypercalcemia and hyperparathyroidism was found to have a novel inactivating missense mutation of the CaSR not detected in her mother.
- Evidence snippets:
  - Snippet 1 (score: 0.485)
    > Familial hypocalciuric hypercalcemia (FHH) is an autosomal dominant disorder characterized by modestly elevated serum calcium (Ca), inappropriately high parathyroid hormone (PTH) levels and low urinary Ca excretion [1]. FHH is caused by inactivating mutations of the gene encoding the Calcium-Sensing Receptor (CaSR), a seven transmembrane G-protein-coupled receptor. The CaSR is expressed primarily in parathyroid chief cells and renal tubular cells and activates an intracellular signaling cascade to maintain serum calcium levels within a narrow range. The gene for the CaSR is located on chromosome 3q13.3-21 and encodes for a 1078 amino acid sequence. Normally, elevated levels of serum calcium activate the CaSR which then inhibits both the secretion of PTH in the parathyroid glands and the reabsorption of Ca 2+ and Mg 2+ in the renal tubules. Therefore an inactivating mutation of the CaSR leads to an elevated set point for serum Ca with the consequence of having both inappropriate secretion of PTH and renal reabsorption of Ca 2+ [2].
    > The clinical impact of these mutations, at least 250 of which have been reported, is highly variable and ranges from totally asymptomatic to fatal. In the neonatal period, homozygous inactivating mutations result in neonatal severe hyperparathyroidism (NSHPT) with severe symptomatic hypercalcemia, undermineralized bones, rib cage deformity, and long-bone and rib fractures [3]. This condition requires aggressive medical management often including emergent parathyroidectomy and can be fatal. Neonatal heterozygous inactivating mutations are usually associated with modest hypercalcemia and hyperparathyroidism with mild or absent bone disease which gradually evolves to a more benign FHH phenotype [4][5][6][7]. Lastly, heterozygous FHH can go wholly unrecognized for years until elevated serum calcium is noted [8].

### [8] Clinical, Biochemical, and Genetic Profile of an Indian Kindred with Type 1 Familial Hypocalciuric Hypercalcemia
- Authors: S. Alam, Alpesh Goyal, N. Tandon
- Year: 2021
- Venue: Indian Journal of Endocrinology and Metabolism
- URL: https://www.semanticscholar.org/paper/ae6b8b00d7320660b7761d97cefa0976e59938de
- DOI: 10.4103/ijem.ijem_349_21
- PMID: 35300448
- PMCID: 8923312
- Citations: 2
- Summary: An Indian kindred with genetically confirmed type 1 FHH where the presentation in the index case was delayed till the age of 48 years, and confounded by secondary hyperparathyroidism related to vitamin D deficiency is described.
- Evidence snippets:
  - Snippet 1 (score: 0.475)
    > Sir, Familial hypocalciuric hypercalcemia (FHH) is a rare genetic disorder with autosomal dominant inheritance and high penetrance that manifests with mild parathyroid hormone (PTH)-dependent hypercalcemia and hypocalciuria. [1,2] he disorder results from an inherited defect in calcium sensing mechanism at the level of parathyroid gland and the thick ascending limb of loop of Henle of kidney. [3] FHH is genetically heterogenous and three subtypes have been described, namely, FHH1, FHH2, and FHH3, related to inactivating mutations in the genes encoding calcium sensing receptor (CaSR), G-protein subunit alpha-11 (GNA11), and adaptor-related protein complex 2 sigma 1 subunit (AP2S1) proteins, respectively. [3] Most patients with FHH are asymptomatic. [4] The disorder runs a benign course in most patients; parathyroidectomy is neither required, nor it is curative. [5] Symptoms of neonatal hypocalcemia have been described in unaffected children of women affected with this rare disorder. [6] Here, we describe an Indian kindred with genetically confirmed type 1 FHH where the presentation in the index case was delayed till the age of 48 years, and confounded by secondary hyperparathyroidism related to vitamin D deficiency.
    > A 48-year-old female initially presented to an orthopedic specialist with complaints of generalized body ache for the past 2 years. Her initial work-up including complete blood count, liver and kidney function tests was unremarkable. She had mild hypercalcemia (serum calcium: 10.8 mg/ dL, N: 8.5-10.5 mg/dL), mild hypophosphatemia (serum phosphate: 2.4 mg/dL, N: 2.5-4.5 mg/dL), raised serum PTH (164.7 pg/mL, N: 15-65 pg/mL), and low serum 25-hydroxyvitamin D levels (6.8 ng/mL, N: 20-50 ng/ mL) [Table 1].

### [9] Familial Syndromes of Primary Hyperparathyroidism
- Authors: W. Simonds
- Year: 2020
- Venue: Calcium Disorders, Hypercalcemia and Hypocalcemia - Recent Advances, New Perspectives and Treatments [Working Title]
- URL: https://www.semanticscholar.org/paper/b6e10049c4507f0eb117c3721ebc63ed57bf4d79
- DOI: 10.5772/intechopen.93036
- Citations: 2
- Summary: Future approaches for the discovery of novel genes pertinent to parathyroid tumor development are the analysis of acquired genetic alterations in DNA isolated from parathyoid tumors and the investigation of familial HPT in kindreds lacking germline mutation in the known genes predisposing to HPT.
- Evidence snippets:
  - Snippet 1 (score: 0.468)
    > PTH secretion from cells of the parathyroid glands is finely regulated in response to changes in the ambient ionized calcium level in order to maintain the circulating calcium concentration within a defined physiologic range. The G protein-coupled CASR is a critical regulator of PTH secretion and is located on the plasma membrane of chief cells in the parathyroid glands [10,11]. In a classic endocrine negative feedback loop, the active form of cholecalciferol, 1,25-dihydroxyvitamin D, whose synthesis is stimulated by PTH acting on proximal renal tubular cells, inhibits PTH biosynthesis and release from parathyroid cells [12][13][14][15]. The simultaneous demonstration of elevated serum calcium with an inappropriately normal or elevated PTH is a typical clinical definition of HPT [16]. The vast majority of parathyroid tumors are adenomas (i.e. benign tumors), with parathyroid cancer accounting for less than 1% of HPT in most series.
    > Most cases of HPT are sporadic with inherited forms of HPT representing only 2-5% of cases. As illustrated in Table 1, research into the molecular pathophysiology of this small subcategory of cases has notwithstanding yielded important understanding with respect to the genes and pathways that promote parathyroid tumorigenesis. Multiple endocrine neoplasia type 1 (MEN1), multiple endocrine neoplasia type 2A (MEN2A), the hyperparathyroidism-jaw tumor syndrome (HPT-JT), and familial isolated hyperparathyroidism (FIHP) are the most common inherited disorders associated with . Familial hypocalciuric hypercalcemia (FHH) is a related and largely benign autosomal dominant condition characterized by lifelong asymptomatic hypercalcemia. Often mis-diagnosed as HPT, in FHH the PTH-dependent hypercalcemia does not correct with partial or even subtotal parathyroidectomy [22]. The relevance of these inherited disorders to the underlying molecular pathogenetic alterations in parathyroid tumorigenesis will be discussed in more detail below.

### [10] Exploring global calcimimetics research trends: a systematic and thematic review of Web of Science and Scopus databases from 1997 to 2024
- Authors: R. Abdelrahman, T. Musa, C. L. Mgbechidinma, E. O. Ahmed
- Year: 2025
- Venue: Frontiers in Nephrology
- URL: https://www.semanticscholar.org/paper/8d22281d01f2b59e9c3d14da3c191d404588a7d5
- DOI: 10.3389/fneph.2025.1617466
- PMID: 40881674
- PMCID: 12380556
- Citations: 1
- Summary: While the thematic map highlighted robust research on the pathophysiology of CKD-MBD, critical clinical outcomes remain underexplored and future trials should highlight these gaps, particularly in high-risk subgroups such as diabetic patients with CKD.
- Evidence snippets:
  - Snippet 1 (score: 0.467)
    > The thematic map of the authors' keywords revealed four distinct clusters of research themes related to calcium metabolism and kidney disease, indicating interdisciplinary connections. The key observations reported cluster "chronic kidney disease (CKD) & mineral disorders" in basic and motor themes, followed by "calcium homeostasis & genetic disorders" in niche themes, which included highlights of the genetic and molecular mechanisms of calcium regulation [familial hypocalciuric hypercalcemia (FHH) as a niche area]. The "hypercalcemia" cluster linked hypercalcemic states to bone pathologies, located in the emerging and basic themes. "Chronic kidney disease" was the most dominant research, and "vascular calcification" was a critical sub-theme (Figure 7A).
    > The thematic KeyWords Plus analysis in Figure 7B identified three key domains, including pharmacological targets (CaSR and cinacalcet) reported in niche themes and central CKD-MBD pathway (HD, vascular calcification, and vitamin D) cases as reported in emerging/declining themes. The small association between "diabetes" and "mineral metabolism" (despite shared CKD complications) suggests a critical research gap.
    > Figure 7C illustrates a thematic clustering process that used abstract words, likely from a biomedical or pharmacological study, focusing on keywords related to calcium sensing and receptor modulation. The structure suggests an emerging thematic analysis, where the dominant topics were grouped hierarchically or by relevance. These findings suggest that "calcium-sensing receptors" and "effects calcimimetic" are major research subjects.

### [11] Familial hypocalciuric hypercalcemia and primary hyperparathyroidism: a case report of an unusual association and literature review
- Authors: Emre Inan, Ezgi Ulaş, Hatice Özışık, Gokcen Ünal Kocabaş, Mehmet Yiğit et al.
- Year: 2025
- Venue: The Egyptian Journal of Internal Medicine
- URL: https://www.semanticscholar.org/paper/e048f73bdcb9b11550ae539361d65c59f968f0db
- DOI: 10.1186/s43162-025-00564-0
- Summary: Patients may still exhibit mild to moderate hypercalcemia following surgery, thus more invasive procedures should be avoided; failure of parathyroid exploration should not be assumed.
- Evidence snippets:
  - Snippet 1 (score: 0.466)
    > Familial Hypocalciuric Hypercalcemia (FHH) represents a group of rare genetic diseases caused by inactivating mutation in the calcium-sensing receptor (CaSR) gene or its associated proteins. It is marked by persistent hypercalcemia, typically asymptomatic, improperly diminished urine calcium excretion, and resistance Familial hypocalciuric hypercalcemia and primary hyperparathyroidism: a case report of an unusual association and literature review Emre İnan 1* , Ezgi Ulaş 1 , Hatice Özışık 1 , Gökçen Ünal Kocabaş 1 , Mehmet Yiğit 1 , Ayça Aykut 1 , Asude Durmaz 1 , Yeşim Ertan 1 , Murat Özdemir 1 , Mehmet Erdoğan 1 and Banu Pınar Şarer Yürekli 1 genotype-phenotype relationships. To date, over 200 CASR mutations have been identified [3]. Mutations affecting the chromosome region 19p13.3 are categorized as FHH2 when caused by loss of function mutations in the GNA11 gene, which encodes the G-protein subunit α11 [4]. Similarly, they are classified as FHH3 when resulting from loss of function mutations in the AP2S1 gene, responsible for encoding the sigma 1 subunit of the adaptor-related protein complex 2 (AP2σ) [5].
    > Primary hyperparathyroidism (PHPT) frequently leads to hypercalcemia in adults, often requiring surgical intervention, particularly when end-organ damage is present or when the patient is young. The risks of prolonged monitoring are considered too uncertain to avoid definitive treatment [6]. Most patients with PHPT are diagnosed not due to symptoms indicative of PHPT but rather through routine clinical practice, as serum calcium is commonly included in standard basic metabolic panel assessments [3]. In 80-90% of cases, PHPT is attributed to the presence of a solitary parathyroid adenoma. About 10-15% of cases are due to four-gland hyperplasia, 5% are due to multiple adenomas, and less than 1% are caused by parathyroid malignancies [7].

### [12] Biased antibodies and beyond: a new era in the diagnosis of PTH-dependent hypercalcemia
- Authors: Noriko Makita, Katsunori Manaka, Maho Taguchi, Hirofumi Horikoshi, Junichiro Sato et al.
- Year: 2025
- Venue: Endocrine Journal
- URL: https://www.semanticscholar.org/paper/558d736d9ff595c82490d7b7bf187064e007b01b
- DOI: 10.1507/endocrj.EJ25-0051
- PMID: 40335290
- PMCID: 12436076
- Citations: 1
- Summary: A novel diagnostic guide for PTH-dependent hypercalcemia is proposed, anticipating that this guide will help identify previously undiagnosed AHH cases in routine practice, enabling timely and effective management of this rare condition.
- Evidence snippets:
  - Snippet 1 (score: 0.465)
    > Hypercalcemia, a common electrolyte imbalance, requires accurate differential diagnosis to guide appropriate management. PTH-dependent hypercalcemia, predominantly caused by primary hyperparathyroidism (PHPT) and rarely by familial hypocalciuric hypercalcemia (FHH)—mainly due to heterozygous loss-of-function mutations in the CASR gene encoding the calcium-sensing receptor (CaSR)—now includes acquired hypocalciuric hypercalcemia (AHH) as an emerging disease entity. Initially identified as analogous to FHH, AHH was characterized by blocking antibodies targeting the CaSR. However, our research has identified unique autoantibodies, termed biased antibodies, that paradoxically regulate signaling by enhancing Gq activity while suppressing Gi activity. Investigating their mechanisms has not only provided insights into specific treatments for AHH but also suggested novel activation mechanisms and binding sites of the CaSR, offering a fresh perspective on the regulation of PTH secretion. In clinical practice, recognizing AHH is crucial. A key diagnostic feature is fluctuating serum calcium levels, making a wait-and-see approach viable for mild hypercalcemia. Conversely, hypercalcemic crises necessitate immediate diagnostic and therapeutic interventions. The most important diagnostic clue to differentiate AHH from PHPT is hypermagnesemia. Additionally, AHH is less likely to involve AVP resistance (i.e., nephrogenic diabetes insipidus) and acute kidney injury (AKI), owing to preserved medullary hyperosmolarity and minimal interference with AVP signaling. Finally, a relatively low PTH level serves as another distinguishing feature. Based on these observations, we propose a novel diagnostic guide for PTH-dependent hypercalcemia. We anticipate that this guide will help identify previously undiagnosed AHH cases in routine practice, enabling timely and effective management of this rare condition.

### [13] Case Report: Severe Neonatal Course in Paternally Derived Familial Hypocalciuric Hypercalcemia
- Authors: Jakob Höppner, Sabrina Lais, C. Roll, A. Wegener-Panzer, D. Wieczorek et al.
- Year: 2021
- Venue: Frontiers in Endocrinology
- URL: https://www.semanticscholar.org/paper/84b1859574413f8e62244408e65f6b7b256f9523
- DOI: 10.3389/fendo.2021.700612
- PMID: 34659108
- PMCID: 8518617
- Citations: 5
- Summary: Familial hypocalciuric hypercalcemia is a mostly benign condition, but transient neonatal hyperparathyroidism may occur in affected neonates if the mutation is paternally inherited, and the condition can be treated successfully with cinacalcet.
- Evidence snippets:
  - Snippet 1 (score: 0.458)
    > Loss-of-function mutations in the calcium-sensing and signaling pathway cause a spectrum of calcium-hyposensitivity-disorders with elevated PTH secretion (1). The resulting disorders can be summarized by inappropriately high PTH concentration despite elevated serum calcium levels.
    > Familial hypocalciuric hypercalcemia (FHH) comprises a genetically heterogenic group (2): FHH1 [OMIM #145980] is caused by heterozygous inactivating mutations in the calciumsensing receptor (CaSR) gene (3). FHH2 and 3 are caused by mutations in genes encoding for proteins involved in calcium signal transduction (4)(5)(6). The CaSR is a member of the subfamily of G protein-coupled transmembrane receptors and is expressed in parathyroid chief cells and the renal tubulus (7). FHH typically presents with the biochemical triad: life-long, non-symptomatic, non-progressive hypercalcemia, normal or slightly elevated serum PTH levels and hypocalciuria (8). Thus, FHH is thought to be a mostly benign condition, with no definite association to adverse outcomes (8). Accordingly, the vast majority of patients with FHH do not require medical or surgical treatment (2,9) and counseling of affected individuals aims to avoid future misdiagnosis and unnecessary parathyroidectomies (9,10).
    > In contrast to the clinically benign course of FHH1, neonatal severe primary hyperparathyroidism (NSHPT) [OMIM #239200] is a severe rare disease associated with a high mortality and is usually caused by homozygous inactivating mutations in the CaSR gene (8,11). Infants with NSHPT develop severe and symptomatic hypercalcemia with muscular hypotonia, respiratory distress, fractures, intestinal dysmotility, and failure to thrive in the early days of life (12)(13)(14).

### [14] Integrated Whole-Exome and Transcriptome Sequencing of Sporadic Parathyroid Adenoma
- Authors: Ya Hu, Xiang Zhang, O. Wang, M. Cui, Xiaobin Li et al.
- Year: 2021
- Venue: Frontiers in Endocrinology
- URL: https://www.semanticscholar.org/paper/9df21dbc09335b81fbc6861045797d78ba81bf29
- DOI: 10.3389/fendo.2021.631680
- PMID: 34054720
- PMCID: 8163014
- Citations: 16
- Summary: According to the RNA-seq data clustering analysis, cyclin D1, β-catenin, VDR, CASR and GCM2 may be important factors contributing to the PA gene expression profile.
- Evidence snippets:
  - Snippet 1 (score: 0.450)
    > Primary hyperparathyroidism (pHPT) is a common endocrine disorder with an incidence of approximately 66 and 25 per 100000 person-years among women and men, respectively (1). It was reported that the prevalence of pHPT was as high as 2.1% in postmenopausal women (2). The parathyroid tumor tissue secretes excessive parathyroid hormone, which results in hypercalcemia and related complications, such as osteoporosis, bone fracture, urolithiasis and renal failure. Parathyroid adenoma (PA) accounts for approximately 85% of pHPT. The genetic mechanisms of PA are not fully known, even though tremendous efforts have been made in previous studies. In PA with a hereditary background, the most wellknown driver gene of PA was multiple endocrine neoplasia type 1 (MEN1). Other possible driver genes for hereditary pHPT include RET in MEN-2, CDKN1B in MEN-4, CDC73 in hyperparathyroidism-jaw tumor syndrome, GCM2 in familial isolated pHPT, CASR in familial hypocalciuric hypercalcemia type 1, GNA11 in familial hypocalciuric hypercalcemia type 2, and AP2S1 in familial hypocalciuric hypercalcemia type 3. For sporadic PA, somatic mutation of MEN1 was identified in approximately 35% of cases (3). Mutation of CCND1 or overexpression of cyclin D1 was found in 30% of sporadic PA cases. Other genes, such as CASR, EZH2, CDKI, and CTNNB1, may also contribute to the tumorigenesis of PA. However, the driver genes could still not be identified in a substantial proportion of sporadic PA.
    > Several studies have explored the molecular mechanism of PA with next-generation sequencing (NGS) technologies, such as whole-exome sequencing (WES) or transcriptome sequencing (RNA-seq). In 2018, Wei et al. (4) used WES to explore genetic abnormalities in 20 specimens of PAs.

### [15] Genetics of Hyperparathyroidism Including Parathyroid Cancer
- Authors: W. Simonds
- Year: 2017
- Venue: Endocrinology and metabolism clinics of North America
- URL: https://www.semanticscholar.org/paper/8d3c8f863c00b638106b63e7a446fb3a39c7e346
- DOI: 10.1016/j.ecl.2017.01.006
- PMID: 28476229
- PMCID: 5424626
- Citations: 26
- Influential citations: 5
- Summary: Primary hyperparathyroidism is a metabolic disease caused by the excessive secretion of parathyroid hormone from one or more neoplastic parathyroid glands that can be associated with a familial syndrome.
- Evidence snippets:
  - Snippet 1 (score: 0.450)
    > Maintenance of the serum calcium concentration within a relatively narrow physiologic range is achieved by regulation of parathyroid hormone (PTH) secretion from parathyroid cells in response to changes in the circulating ionized calcium level. The G protein-coupled CaSR located on the surface membrane of the parathyroid chief cells negatively regulates the secretion of PTH. 2,3 In clinical medicine, HPT is typically defined by the conjunction of elevated serum ionized calcium with inappropriately elevated PTH. 1 Most parathyroid tumors are benign adenomas. Parathyroid carcinoma is a rare cause of HPT seen in less than 1% of cases.
    > Approximately 2 to 5 % of cases of HPT are associated with familial disease. Study of this small subset has nevertheless provided great insight into the genetic changes and molecular pathways that promote parathyroid neoplasia ( Table 1). The most common genetic disorders associated with HPT are MEN1, multiple endocrine neoplasia type 2A (MEN2A), HPT-JT, and familial isolated hyperparathyroidism (FIHP). [4][5][6][7] Familial hypocalciuric hypercalcemia (FHH) is a related, genetically heterogeneous, largely benign condition of PTH-dependent hypercalcemia often mimicking HPT that does not correct with partial or subtotal parathyroidectomy (PTX). 8 These genetic disorders and their relation to the underlying molecular and genetic alterations relevant to parathyroid neoplasia will be discussed in detail below.

### [16] Disorders of the Calcium Sensing Signaling Pathway: From Familial Hypocalciuric Hypercalcemia (FHH) to Life Threatening Conditions in Infancy
- Authors: Jakob Höppner, Kathrin Sinningen, A. Raimann, B. Obermayer-Pietsch, C. Grasemann
- Year: 2022
- Venue: Journal of Clinical Medicine
- URL: https://www.semanticscholar.org/paper/12f8f3ef678598e485ff1062c8faa0877eacb3ee
- DOI: 10.3390/jcm11092595
- PMID: 35566721
- PMCID: 9100033
- Citations: 18
- Influential citations: 1
- Summary: This review focuses on the genetic and pathophysiological framework that leads to the severe neonatal form of familial hypocalciuric hypercalcemia, gives recommendations for counselling and summarizes treatment options.
- Evidence snippets:
  - Snippet 1 (score: 0.449)
    > Loss-of-function (LOF) mutations in the calcium-sensing pathway may cause various calcium-hyposensitivity-diseases which are characterized by elevated serum calcium levels. Pathophysiologically, this is based on a shift of the 'set point' of the calcium concentration at which PTH secretion is half-maximal [1]. The resulting disorders share a constellation of inappropriately high PTH concentrations despite elevated serum calcium levels and are categorized into three groups based on genetic origin, time of onset and severity of clinical symptoms, namely familial hypocalciuric hypercalcemia (FHH), neonatal severe primary hyperparathyroidism (NSHPT), and neonatal hyperparathyroidism (NHPT) [2][3][4].
    > FHH comprises a genetically heterogeneous group [5]: FHH1 [OMIM #145980] is usually caused by heterozygous inactivating mutations in the calcium sensing receptor gene (CaSR) and accounts for about 65% of all FHH cases [3]. Mutations in other genes encoding for proteins with a role in calcium signaling (GNA11 and AP2S1) cause FHH2 and 3 [6][7][8].
    > The aims of this review are to present the pathophysiology of calcium-sensing receptor signaling disorders with a focus on intra-uterine calcium homeostasis and the differing clinical outcomes in neonates.

### [17] New therapeutic targets in rare genetic skeletal diseases
- Authors: M. Briggs, P. A. Bell, M. Wright, K. A. Pirog
- Year: 2015
- Venue: Expert Opinion on Orphan Drugs
- URL: https://www.semanticscholar.org/paper/1363107f71ae6d2d60abca471cddf3da5d13644b
- DOI: 10.1517/21678707.2015.1083853
- PMID: 26635999
- PMCID: 4643203
- Citations: 39
- Influential citations: 1
- Summary: An overview of disease mechanisms that are shared amongst groups of different GSDs and potential therapeutic approaches that are under investigation are described to generate critical mass for the identification and validation of novel therapeutic targets and biomarkers.
- Evidence snippets:
  - Snippet 1 (score: 0.446)
    > However, emerging knowledge suggests that the primary genetic defect may be less important than the cells' response to the expression of the mutant gene product [107]. Moreover, the largely overlooked response of a cell (i.e. chondrocyte) to the abnormal extracellular environment is also important for disease progression as illustrated by several GSDs discussed in this review.
    > It is important that 'omics'-based approaches and technologies are systematically applied to the study of rare GSDs so that definitive reference profiles and disease signatures are generated for each phenotype. These can then be used in a Systems Biology approach to identify both common and dissimilar pathological signatures and disease mechanisms. This approach is entirely dependent upon relevant in vitro and in vivo models (and also novel 'disease-mechanism phenocopies' [107]) for testing new diagnostic and prognostic tools and for determining the molecular mechanisms that underpin the pathophysiology so that effective therapeutic treatments can be developed and validated. This approach will eventually lead to personalized treatments and care strategies centred on shared disease mechanisms with the use of relevant biomarkers to monitor the efficacy of treatment and disease progression.
    > It is vital that all relevant stakeholders are involved from the outset in defining the appropriate outcomes of any potential therapeutic regime. The perceptions of a successful therapy can differ widely between the clinical academic community and the relevant patient-support groups and it is vital that there is engagement on all these issues.
    > In summary, the identification of causative genes and mutations for GSDs over the last 20 years, coupled with the generation and in-depth analysis of a plethora of relevant cell and mouse models, has derived new knowledge on disease mechanisms and suggested potential therapeutic targets. The fast-evolving hypothesis that clinically disparate diseases can share common disease mechanisms is a powerful concept that will generate critical mass for the identification and validation of novel therapeutic targets and biomarkers.

### [18] Research progress on pathogenic genes of dilated cardiomyopathy
- Authors: Xiao Zhang, Xin-Yue Zhang, Yun-Ru Chen, Na Huan, Chenglong Wang et al.
- Year: 2026
- Venue: iScience
- URL: https://www.semanticscholar.org/paper/44e063ee7afd11e0d1d30ad4fe9080e16b2c1bf4
- DOI: 10.1016/j.isci.2026.115511
- PMID: 42058912
- PMCID: 13122708
- Citations: 1
- Summary: Summary Dilated cardiomyopathy (DCM) is a primary myocardial disorder characterized by progressive ventricular dilatation and impaired myocardial systolic contractility, and it represents the most common form of cardiomyopathy globally. DCM drives a substantial worldwide disease burden, thus presenting a formidable and persistent challenge to global public health systems. The pathogenesis of DCM is marked by extreme etiological heterogeneity: 30%–50% of cases have a familial origin, with gene...
- Evidence snippets:
  - Snippet 1 (score: 0.446)
    > This paper focuses on exploring the mechanisms of familial hereditary DCM. In addition to familial hereditary DCM, acquired DCM also exists in clinical practice. This type of DCM is primarily caused by environmental factors acting on a potential genetic predisposition, such as infectious DCM, which accounts for approximately 95% of acquired DCM cases. 204 It is important to emphasize that acquired DCM differs significantly from familial hereditary DCM. This section will exclusively address familial hereditary DCM. DCM disease-causing genes exhibit high heterogeneity, with significant variations in the proportion of patients affected by different genes. This results in ''single-gene mutation-targeted drugs'' covering only a very small fraction of patients. Even for TTN, the most prevalent gene, such drugs cover only 25% of end-stage/familial DCM patients. The proportion of patients affected by other genes is even lower, meaning ''single-gene drugs'' inherently face the problem of a ''narrow target population'' from the outset. This strict ''gene-mechanism-drug'' correspondence limits each drug class to serving only a tiny patient subgroup, making large-scale clinical application difficult. Furthermore, merely improving downstream symptoms cannot halt the core pathological processes driving disease progression. Therefore, we can shift our research focus upstream to explore the common pathological environment that leads to mutations in relevant disease-causing genes, the likelihood of staged gene mutations, or improve the internal environment to activate the body's gene repair mechanisms for treating DCM. Therefore, future therapies should not only target single-gene treatments but also explore how to improve the shared pathological environment. By reversing the ''soil'' in which gene mutations take effect, we can achieve broad-spectrum intervention for polygenic DCM.

### [19] Control of PTH secretion by the TRPC1 ion channel
- Authors: Marta Onopiuk, B. Eby, V. Nesin, Peter Ngo, M. Lerner et al.
- Year: 2020
- Venue: JCI Insight
- URL: https://www.semanticscholar.org/paper/8b25128bce63ef887aa258a7432dedb4bed01e37
- DOI: 10.1172/jci.insight.132496
- PMID: 32213715
- PMCID: 7205425
- Citations: 11
- Summary: Mice lacking the transient receptor potential canonical channel 1 (TRPC1) develop chronic hypercalcemia, hypocalciuria, and elevated PTH levels, mimicking human FHH, and TRPC1-mediated Ca2+ signaling is identified as an essential component of the cellular apparatus controlling PTH secretion in the PTG downstream of CaSR.
- Evidence snippets:
  - Snippet 1 (score: 0.442)
    > Familial hypocalciuric hypercalcemia (FHH) is a genetic condition associated with hypocalciuria, hypercalcemia, and, in some cases, inappropriately high levels of circulating parathyroid hormone (PTH). FHH is associated with inactivating mutations in the gene encoding the Ca2+-sensing receptor (CaSR), a GPCR, and GNA11 encoding G protein subunit α 11 (Gα11), implicating defective GPCR signaling as the root pathophysiology for FHH. However, the downstream mechanism by which CaSR activation inhibits PTH production/secretion is incompletely understood. Here, we show that mice lacking the transient receptor potential canonical channel 1 (TRPC1) develop chronic hypercalcemia, hypocalciuria, and elevated PTH levels, mimicking human FHH. Ex vivo and in vitro studies revealed that TRPC1 serves a necessary and sufficient mediator to suppress PTH secretion from parathyroid glands (PTGs) downstream of CaSR in response to high extracellular Ca2+ concentration. Gα11 physically interacted with both the N- and C-termini of TRPC1 and enhanced CaSR-induced TRPC1 activity in transfected cells. These data identify TRPC1-mediated Ca2+ signaling as an essential component of the cellular apparatus controlling PTH secretion in the PTG downstream of CaSR.

### [20] Cinacalcet reverses short QT interval in Familial Hypocalciuric Hypercalcemia type 1
- Authors: T. Cuny, P. Romanet, M. Goldsworthy, Carole Guerin, Marie Wilkin et al.
- Year: 2023
- Venue: The Journal of clinical endocrinology and metabolism
- URL: https://www.semanticscholar.org/paper/e3e574e1855420fdea1c760d2bc6d1a8c5063d69
- DOI: 10.1210/clinem/dgad494
- PMID: 37602721
- PMCID: 7615553
- Citations: 3
- Summary: The results indicate that FHH-1 patients should be assessed for a short QT interval, and a cinacalcet test used to select patients who are likely to benefit from this treatment.
- Evidence snippets:
  - Snippet 1 (score: 0.441)
    > Familial hypocalciuric hypercalcemia (FHH) is an autosomal dominant genetic disease mainly caused by germline calcium-sensing receptor (CASR) inactivating mutations (also called FHH-1)(1). More rarely FHH can be related to AP2S1 or GNA11 inactivating mutation, both genes encoding for proteins involved downstream of CASR activation (2,3).
    > FHH is usually characterized by mild elevation of calcemia with inappropriate or normal plasma parathyroid hormone (PTH) and, eventually, very low 24-hour urinary calcium excretion, best expressed by a urine calcium-to-creatinine clearance ratio (CCCR) <0.01 (3). Parathyroid thyroid imaging, if done, can be negative, a finding that together with hypocalciuria should raise the suspicion of FHH and argued against parathyroidectomy (4).
    > Hypercalcemia can be complicated by cardiac arrhythmias, as a consequence of a short QT interval (5). To date there is no data reporting the occurrence of possible cardiac arrhythmias in FHH-1 patients, possibly linked to the mild biochemical phenotype usually observed in this context.
    > Cinacalcet, a positive allosteric modulator of CaSR, can decrease PTH secretion (6) and was successfully used for FHH with a more severe hypercalcemia (7,8), however its benefits in mild presentation of FHH is counterbalanced by possible side effects (hypocalcemia, nausea, vomiting) and cost burden (9,10). In certain circumstances, the use of cinacalcet can be discussed on an individual basis at a multidisciplinary team meeting to ensure proper indication and follow-up. This can be the case in patients with short QT interval, a finding that could predispose to sudden cardiac death (11). Here, we present three family members with FHH-1 and a severe short QT interval who were potential candidates for cinacalcet therapy after demonstrating their sensitivity to the compound via a cinacalcet test.

## Notes

- This provider combines `search_papers_by_relevance` with `snippet_search`.
- No synthesis or second-stage model call is performed.

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 36 |
| Resolved | 36 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 36 |
| On topic | 20 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

No ontology term identifiers were found in this report.