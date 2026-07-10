---
reference_id: "DOI:10.1007/s00384-024-04776-8"
title: "Genomic mosaicism in colorectal cancer and polyposis syndromes: a systematic review and meta-analysis"
authors:
- Francisco Cezar Aquino de Moraes
- Nayara Rozalem Moretti
- Vitor Kendi Tsuchiya Sano
- Cristiane Wen Tsing Ngan
- Rommel Mario Rodríguez Burbano
journal: International Journal of Colorectal Disease
year: '2024'
doi: 10.1007/s00384-024-04776-8
content_type: full_text_pdf
full_text_attempted: true
full_text_provider: openalex
full_text_url: "https://link.springer.com/content/pdf/10.1007/s00384-024-04776-8.pdf"
oa_status: hybrid
license: cc-by
local_pdf_path: files/DOI_10.1007_s00384-024-04776-8.pdf
---

# Genomic mosaicism in colorectal cancer and polyposis syndromes: a systematic review and meta-analysis
**Authors:** Francisco Cezar Aquino de Moraes, Nayara Rozalem Moretti, Vitor Kendi Tsuchiya Sano, Cristiane Wen Tsing Ngan, Rommel Mario Rodríguez Burbano
**Journal:** International Journal of Colorectal Disease (2024)
**DOI:** [10.1007/s00384-024-04776-8](https://doi.org/10.1007/s00384-024-04776-8)

## Content

Abstract
Background
Colorectal cancer (CRC) and polypoid syndromes are significant public health concerns, with somatic mosaicism playing a crucial role in their genetic diversity. This study aimed to investigate the prevalence and impact of somatic mosaicism in these conditions.

Methods
A search was conducted using PubMed, Scopus, and Web of Sciences to identify studies evaluating mosaicism in patients with CRC or polyposis syndromes. Odds ratios (ORs) with 95% confidence intervals (CIs) were calculated to determine prevalence rates. Statistical analyses were performed using R software 4.3.

Results
A total of 27 studies, encompassing 2272 patients, were included in the analysis. Of these, 108 patients exhibited somatic mosaicism, resulting in an overall prevalence of 8.79% (95% CI 5.1 to 14.70%, I2 = 85; p < 0.01). Subgroup analyses revealed a significantly higher prevalence of mosaicism in patients with APC mutations (OR 13.43%, 95% CI 6.36 to 26.18%, I2 = 87; p < 0.01). Additionally, mosaicism in MLH1 and MSH2 genes was observed at rates of 2.75% (95% CI 1.20 to 6.18%) and 9.69% (95% CI 2.98 to 27.24%), respectively.

Conclusions
Our findings support the growing recognition of mosaicism as a critical factor in CRC susceptibility and underscore the importance of incorporating mosaicism screening into routine genetic testing for at-risk patients.

Vol.:(0123456789)
International Journal of Colorectal Disease (2024) 39:201 
https://doi.org/10.1007/s00384-024-04776-8
RESEARCH
Genomic mosaicism in colorectal cancer and polyposis syndromes: 
a systematic review and meta‑analysis
Francisco Cezar Aquino de Moraes1  · Nayara Rozalem Moretti2  · Vitor Kendi Tsuchiya Sano3  · 
Cristiane Wen Tsing Ngan4  · Rommel Mario Rodríguez Burbano5 
Accepted: 5 December 2024 / Published online: 15 December 2024 
© The Author(s) 2024
Abstract
Background Colorectal cancer (CRC) and polypoid syndromes are significant public health concerns, with somatic mosai-
cism playing a crucial role in their genetic diversity. This study aimed to investigate the prevalence and impact of somatic 
mosaicism in these conditions.
Methods A search was conducted using PubMed, Scopus, and Web of Sciences to identify studies evaluating mosaicism 
in patients with CRC or polyposis syndromes. Odds ratios (ORs) with 95% confidence intervals (CIs) were calculated to 
determine prevalence rates. Statistical analyses were performed using R software 4.3.
Results A total of 27 studies, encompassing 2272 patients, were included in the analysis. Of these, 108 patients exhibited 
somatic mosaicism, resulting in an overall prevalence of 8.79% (95% CI 5.1 to 14.70%, I 2 = 85; p < 0.01). Subgroup analy-
ses revealed a significantly higher prevalence of mosaicism in patients with APC mutations (OR 13.43%, 95% CI 6.36 to 
26.18%, I2 = 87; p < 0.01). Additionally, mosaicism in MLH1 and MSH2 genes was observed at rates of 2.75% (95% CI 1.20 
to 6.18%) and 9.69% (95% CI 2.98 to 27.24%), respectively.
Conclusions Our findings support the growing recognition of mosaicism as a critical factor in CRC susceptibility and under-
score the importance of incorporating mosaicism screening into routine genetic testing for at-risk patients.
Keywords Colorectal cancer · Mosaicism · Polypoid syndromes · APC mutation · MLH1 · MLH1 · MSH2
Introduction
Colorectal cancer (CRC) is a serious public health issue, 
with approximately 1.9 million new cases diagnosed annu-
ally [1–5]. Many patients are diagnosed at advanced stages, 
which limits treatment options and reduces survival rates 
[6]. Understanding genetic factors, such as somatic mosai-
cism, that influence the development of CRC is essential 
for improving early detection and personalizing treatments 
[7, 8]. Somatic mosaicism, which involves the presence of 
genetically distinct cells within the same individual, is a 
significant factor in the genetic diversity of diseases like 
CRC and polypoid syndromes [9 –11]. This mosaicism can 
arise both early in development and later in life, affecting 
the severity and progression of the disease in various ways 
[12, 13].
During embryogenesis, the timing of a mutation deter -
mines its distribution and impact on the organism [14– 16]. 
If a mutation occurs shortly after fertilization, during the 
first cell divisions, it may be incorporated into several germ 
layers of the embryo, such as the ectoderm, mesoderm, and 
endoderm [12, 17, 18]. This means that the mutation could 
be present in various tissues and organs, resulting in a more 
widespread phenotype, which could lead to the development 
of polyps in different regions of the colon and affect other 
 * Francisco Cezar Aquino de Moraes 
 francisco.cezar2205@gmail.com
1 Federal University of Pará, Belém, Pará 66073-005, Brazil
2 University of Western São Paulo, 
Presidente Prudente 19050-920, Brazil
3 Federal University of Acre, Rio Branco, Acre 69920-900, 
Brazil
4 University Anhembi Morumbi, 
Piracicaba, São Paulo 13425-380, Brazil
5 Ophir Loyola Hospital, Belém, Pará 66063-240, Brazil

 International Journal of Colorectal Disease (2024) 39:201
201 Page 2 of 14
organ systems, increasing the complexity and severity of the 
clinical condition [19, 20]. On the other hand, if the muta-
tion occurs at a later stage of embryogenesis, when the cells 
are more differentiated, its impact will be more localized 
[15, 21]. This could result in a more restricted manifestation 
of the disease, such as the formation of polyps in a single 
region of the colon [19]. This temporal differentiation is 
crucial for understanding the variations in the clinical pres-
entation of CRC and polypoid syndromes in patients with 
somatic mosaicism [10, 22].
Somatic mosaicism, characterized by the presence of 
genetically distinct cell populations within an individual, 
is increasingly recognized as a significant contributor to 
the genetic diversity observed in various diseases, includ-
ing CRC and polypoid syndromes [9 , 23–25]. In colorectal 
cancer, somatic mosaicism may manifest as early mutations 
that set the stage for the development of both benign and 
malignant lesions [26, 27]. For instance, mutations in genes 
such as APC, which play a critical role in the WNT signaling 
pathway, are often among the first events in the adenoma-
carcinoma sequence [28–30]. When these mutations occur in 
a mosaic pattern, different regions of the colon may harbor 
distinct genetic alterations, leading to varying degrees of 
polyp formation and cancer risk within the same individual 
[11, 31–33]. Polypoid syndromes, such as familial adenoma-
tous polyposis (FAP) and Lynch syndrome, may also exhibit 
mosaicism [10, 34]. In FAP, mosaicism in the APC gene 
can result in a milder phenotype, with fewer polyps and a 
later onset of cancer compared to individuals with germline 
mutations [35, 36]. This variation can complicate diagnosis 
and management, as standard screening protocols may not 
fully capture the extent of the disease in cases of mosaicism 
[12, 37].
Understanding the role of somatic mosaicism in CRC 
and polypoid syndromes is crucial for improving diagno-
sis and treatment. The presence of mosaicism can compli-
cate diagnosis and require more personalized strategies for 
clinical management. Therefore, this meta-analysis seeks to 
clarify the role of somatic mosaicism in CRC and polypoid 
syndromes, as well as to characterize the frequency of this 
condition in this patient group.
Methods
Protocol and registration
This systematic review and meta-analysis were conducted 
following Preferred Reporting Items for Systematic Reviews 
and Meta-Analysis (PRISMA) guidelines and the recom -
mendations from the Cochrane Collaboration, as detailed in 
Supplementary Material: Tables 1 and 2 [38]. The study was 
officially registered in the Prospective International Registry 
of Systematic Reviews (PROSPERO) under the identifier 
CRD2344534945 and is accessible at https:// www. crd. york. 
ac. uk/ as of 31 July 2024 [39].
Eligibility criteria
Studies that adhered to the following eligibility criteria were 
considered: (1) retrospective cohort studies, (2) case–control 
studies, (3) observational studies, (4) studies that provided data 
on patients who were officially diagnosed with colorectal can-
cer or polyposis syndromes, and (5) studies with patients who 
underwent testing for mosaicism. Articles that did not include 
confirmed diagnostic data for colorectal cancer or polyposis 
or lacked mosaicism testing were not considered. Moreover, 
studies with study designs such as case reports, reviews, opin-
ion pieces, technical reports, guidelines, animal studies, and 
in vitro experiments were also excluded. Only studies pub-
lished in English were considered, and the publication date 
was not restricted.
Search strategy
A systematic search of published studies was conducted on 
PubMed, Scopus, and Web of Science in August 2024. The 
search was further extended to include abstracts, articles, and 
scientific presentations. For each database, search strategies 
were meticulously adapted using both Medical Subject Head-
ings (MeSH) and input terms, following the specific syntax 
rules of each platform. Boolean operators (OR, AND) were 
employed to effectively combine search terms. To broaden 
our review’s scope, we also examined the references of the 
included articles and relevant systematic reviews. Concur -
rently, we ensured the currency of our research by setting up 
alerts in each database to notify us of newly published studies 
relevant to our search criteria. The detailed search strategies 
are provided in Supplementary Table 3.
The search strategy was executed collaboratively by 
two authors (N.R.M. and F.C.A.M.). To ensure compre -
hensive coverage, we assessed the included articles’ refer -
ences and abstracts and conducted systematic literature 
reviews. All studies screened through databases and refer -
ences were imported into the reference management soft-
ware (Rayyan version 1.1). Duplicates were removed using 
automatic screening (Zotero® version 6.0.37; Thomson 
Reuters, Philadelphia, PA, USA) and manual review. The 
titles and abstracts of the identified articles were indepen-
dently reviewed by the two authors, who also indepen-
dently extracted data according to predefined search criteria 
and quality assessment protocols. In cases of discrepancy 
between the reviewers, a third reviewer provided the final 
decision on study inclusion.

International Journal of Colorectal Disease (2024) 39:201 
 Page 3 of 14 201
Data extraction and risk of bias assessment
To compile the principal outcomes, two authors (N.R.M. and 
F.C.A.M.) independently extracted analyzed data from each 
included article. The variables collected encompassed the 
primary author and year of publication, the overall patient 
cohort size, the specific type of patients tested, the number of 
mosaic patients identified, the type of mosaicism detected, the 
methodologies employed for detection, and detailed patient 
phenotypes, including the number of individuals affected by 
each phenotype.
The Newcastle–Ottawa Scale (NOS) was used to assess the 
risk of bias and quality of the included studies. The scale eval-
uates studies across 7 to 8 domains depending on the study 
type, with each domain rated as “low risk,” “unclear risk,” or 
“high risk.” Studies were categorized based on total scores, 
with those scoring ≥ 7 considered high quality and those scor-
ing < 7 regarded as low quality. The NOS allocates points 
based on key criteria such as the selection of study cohorts, 
the comparability of groups concerning critical factors, and 
the assessment of outcomes, including follow-up duration and 
adequacy [40]. Two reviewers (N.M.R. and F.C.A.M.) con-
ducted evaluations independently, ensuring objectivity and 
reducing bias. Discrepancies between assessments and any 
conceptual, methodological, or statistical issues were resolved 
through consensus discussions involving the research team. 
Funnel plots were utilized to analyze the symmetry of all 
outcomes.
Endpoints and definitions
The primary outcomes of interest in this systematic review and 
meta-analysis were as follows: (1) determine the prevalence 
of mosaicism in patients diagnosed with colorectal cancer or 
polyposis syndromes; (2) identify the different types of mosai-
cism (APC, MLH1, and MSH2) present associate with the 
phenotype.
Statistical analysis
Baseline characteristics of the sample were analyzed to assess 
their potential impact on the outcomes. Prevalence rates were 
calculated, providing 95% confidence intervals (CIs) for each 
outcome. A fixed-effect model was applied for low heteroge-
neity outcomes (I2 < 25%) [41]. The DerSimonian and Laird 
random-effects model was employed for those with significant 
heterogeneity to account for variability across studies [42]. Het-
erogeneity and effect sizes were quantified using I2 and  Tau2 
statistics. All statistical analyses were conducted using R statis-
tical software, version 4.2.3 (R Foundation for Statistical Com-
puting). To ensure the robustness of the findings, sensitivity 
analyses were performed using leave-one-out and funnel plots.
Results
Study selection and baseline characteristics
Figure  1 illustrates the study selection process for the 
meta-analysis. Initially, 390 results were identified from 
three databases: PubMed (129 results), Scopus (152 
results), and Web of Science (109 results). After the ini-
tial screening, 162 duplicate studies were removed, leav -
ing 43 studies for full-text review. Of these, 16 studies 
were excluded for the following reasons: 4 due to insuf-
ficient data on specific mosaicism cases, 9 due to the 
absence of data on mosaicism detection, 2 because no 
mosaic variants were identified, and 2 for having the 
wrong study design. In total, 27 studies were included in 
the meta-analysis.
Characteristics of the included studies
A total of 27 studies were included, involving 2272 
patients, of which 108 had mosaicism. Fourteen studies 
found somatic APC, six MLH1, and four MSH2. The gen-
otyping method most used was next-generation sequencing 
(NGS). These characteristics are detailed in Table  1.
Fig. 1  Flowchart of studies included

 International Journal of Colorectal Disease (2024) 39:201
201 Page 4 of 14
Table 1  Characteristics of the included studies
Author, year Type of patients tested Mosaic 
patients
Patients tested Type of mosaicism Detection method Patient phenotypes (no. of patients 
affected)
Aretz, 2007 [43] Suspected or confirmed de novo 
APC mutation
8 75 Somatic APC PTT, DHPLC, SNaPshot AFAP (5),
FAP 100–200 (3)
Baert-Desurmont, 2018 [44] Patients with suspected hereditary 
colorectal cancer (CRC) and 
identified with class 4 or 5 genetic 
variants
2 323 Somatic APC Sanger, MLPA, NGS Adenomatous polyposis (1); Diffuse 
form (2)
3 Gene STK11 Independent Peutz–Jeghers patients 
(3)
Bossard, 2012 [45] Patients with metastatic colorectal 
adenocarcinoma (mCRC)
4 18 KRAS Gene PCR CRC (4)
Chan, 2006 [46] Early-onset or familial MSI CRCs 1 31 Gene MSH2 MSP, Clonal Bisulfite Sequencing, 
haplotype analysis, pyrosequenc-
ing
CRC < 50 (2)
EC < 50 (1)
Adenomas > 70 (1)
No phenotype (6)
Ciavarella, 2018 [47] Patients with unexplained colorectal 
adenomatous polyposis
4 8 Somatic APC Sanger, Dpcr, WES AFAP (2), FAP 100–200 (2)
Farrington, 1999 [48] Parents of de novo probands 2 5 Somatic APC Sanger, PCR cloning, single cell 
analysis
FAP (2)
Guillerm, 2020 [49] Patients with Lynch-like syndrome 
with mismatch repair gene muta-
tions (MMR)
1 15 Gene MSH2 NGS and Sanger CRC 
Hes, 2008 [50] APC mutation carriers 10 242 Somatic APC DGGE/PTT No polyps (1), AFAP(4), FAP (5)
Hitchins, 2011 [51] Patients with early-onset CRC and 
a LS-like phenotype with negative 
mismatch repair gene mutations 
(MMR)
1 122 Gene MLH1 qMSP, COBRA CRC < 50
Hitchins, 2023 [52] Patients with early-onset CRC and a 
LS-like phenotype with mismatch 
repair gene mutations (MMR)
4 281 Gene MLH1 Pyrosequencing, PCR and Clonal 
Bisulfite Sequencing
CRC 
Jansen, 2016 [53] Patients with unexplained adenoma-
tous polyposis or multiple primary 
colorectal carcinomas, who tested 
negative for germline APC and 
MUTYH mutations
9 18 Somatic APC NGS, Sanger AFAP (9)
Joo, 2023 [54] Patients with early-onset CRC and 
suspected MLH1 epimutation
3 97 Gene MLH1 ddPCR CRC (2); EOCRC—Early-Onset 
Colorectal Cancer (1)
Kanter-Smoler, 2008 [55] APC- and MUTYH-negative 
patients with de novo mutations
1 3 Somatic APC SSCP AFAP
Karstensen, 2024 [56] Patients with AFAP and negative for 
known pathogenic variants in com-
mon polyposis-associated genes
2 27 Somatic APC NGS AFAP (2)

International Journal of Colorectal Disease (2024) 39:201 
 Page 5 of 14 201
Table 1  (continued)
Author, year Type of patients tested Mosaic 
patients
Patients tested Type of mosaicism Detection method Patient phenotypes (no. of patients 
affected)
Kim, 2019 [57] Patients with clinically suspected 
familial adenomatous polyposis 
(FAP) who had no detectable path-
ogenic variants in known colonic 
polyposis-associated genes
7 28 Somatic APC NGS and MEMO-PCR FAP
Mongin, 2012 [58] De novo FAP patients without fam-
ily history
1 17 Somatic APC HRM, NGS, and Sanger FAP
Morak, 2008 [59] Patients with suspected HNPCC 
(hereditary nonpolyposis colorectal 
cancer) or Lynch syndrome, who 
had MSI-H tumors and loss of 
MLH1 protein expression, but 
tested negative for germline muta-
tions in MMR genes, with 12 of 
them showing aberrant MLH1 
promoter methylation
6 94 Gene MLH1 MSP, MS-MPLA, SNP typing, 
haplotype analysis
CRC (6)
Mur, 2014 [60] LS-suspected
families
6 22 Gene MSH2 MLPA, MS-MLPA CRC < 50 (7),
CRC52 (1),
DC52 (1)
Hg.ad28 (1)
Out, 2015 [61] Unexplained AFAP patients 4 173 Somatic APC HRM on leukocyte (171)
HRM on tumor DNA (2)
AFAP (4)
Pinto, 2018 [62] Mutation negative polyposis or CRC 
patients
4 38 Gene MLH1 MS-MLPA,
qMSP, ddPCR
CRC < 50 (4)
Rofes, 2021 [63] Patients with classic familial 
adenomatous polyposis (FAP) who 
had no causative germline vari-
ants identified in the APC and/or 
MUTYH genes
7 11 Somatic APC NGS and Sanger FAP (7)
Sourrouille, 2013 [64] Patients with microsatellite instabil-
ity (MSI) colorectal cancer, sus-
pected of having Lynch Syndrome, 
who tested negative for germline 
mutations and promoter methyla-
tion in MMR genes, specifically 
focusing on those with loss of 
MSH2 protein expression
1 18 Gene MSH2 Sanger, MLPA, HRM CRC 
Spier, 2016 (NGS) [65] Unexplained Types of mosai-
cism included variants detected 
in leukocytes FAP patients > 20 
synchronous adenomas > 40 non-
synchronous adenomas)
5 20 Somatic APC NGS on adenomas, Sanger and deep 
sequencing
AFAP (5)

 International Journal of Colorectal Disease (2024) 39:201
201 Page 6 of 14
Table 1  (continued)
Author, year Type of patients tested Mosaic 
patients
Patients tested Type of mosaicism Detection method Patient phenotypes (no. of patients 
affected)
Spier, 2016 (WES) [66] Unexplained Types of mosaicism 
included variants detected in leu-
kocytes FAP patients > 40 non-
synchronous adenomas)
2 80 Somatic APC WES on leukocytes, Sanger and 
deep sequencing
FAP 100–500 (2)
Suter, 2004 [67] Mutation negative polyposis or CRC 
patients
2 44 Gene MLH1 COBRA CRC < 50 (2)
Takao, 2021 [68] Patients with unexplained colorectal 
adenomatous polyposis, negative 
for known germline mutations 
in 57 genes, including APC and 
MUTYH
6 46 Somatic APC High-coverage NGS FAP (6)
Ward, 2013 [69] CRC patiens suspected of having 
Lynch syndrome or displaying 
early-onset colorectal cancer, but 
without identified pathogenic ger-
mline mutations in the mismatch 
repair (MMR) genes,
2 416 Gene MLH1 qMSP, MS-HRM analysis, bisulfite 
sequencing, ddPCR
CRC (2)
 AFAP  attenuated familial adenomatous polyposis, COBRA  combined bisulfite restriction analysis,  CRC   colorectal cancer,  ddPCR  droplet digital PCR,  FAP  familial adenomatous polyposis,  
HRM  high-resolution melting,  MSP  methylation-specific PCR,  NR  not related,  MS-MLPA  methylation-specific multiplex ligation-dependent amplification MS-MLPA,  MLPA  multiplex 
ligation-dependent amplification,  NGS  next-generation sequencing technology,  PCR  polymerase chain reaction,  qPCR  quantitative real-time PCR,  qMSP  quantitative methylation-specific 
PCR,  MEMO-PCR  mutant enrichment with 3′-modified oligonucleotides PCR,  MS-HRM  methylation-sensitive high-resolution melting,  SSCP  single-strand conformation polymorphism,  
WES  whole exome sequencing

International Journal of Colorectal Disease (2024) 39:201 
 Page 7 of 14 201
General analysis
Prevalence of overall mosaicism
The estimated prevalence of overall mosaicism was deter -
mined from 26 studies involving a total of 2,272 patients 
and 108 events. The prevalence was calculated as an odds 
ratio (OR) of 8.79% (95% CI 5.1 to 14.70%, Fig.  2A). Sig-
nificant heterogeneity (I 2 = 85; p < 0.01) was observed, 
which is expected due to the inclusion of observational 
studies.
APC mutation
The prevalence of APC mutations in patients with gastric 
cancer or polyposis syndromes was assessed in 15 studies 
encompassing 1076 patients. Seventy APC mutations were 
identified, resulting in an estimated OR of 13.43% (95% CI 
Fig. 2  Prevalence. A Overall mosaicism. B APC mutation

 International Journal of Colorectal Disease (2024) 39:201
201 Page 8 of 14
6.36 to 26.18%, Fig. 2B). The heterogeneity for APC muta-
tions was also significant (I2 = 87; p < 0.01).
MLH1 and MSH2 mosaicism
The prevalence of MLH1 mosaicism was analyzed in 7 stud-
ies involving 1092 patients. Twenty-two cases of MLH1 
mosaicism were identified, leading to an estimated preva-
lence of 2.75% (95% CI 1.20 to 6.18%, Fig. 3A). The hetero-
geneity for MLH1 mosaicism was 71% (p < 0.01).
For MSH2 mosaicism, three studies with 86 patients 
identified 9 cases. The estimated prevalence of MSH2 mosa-
icism was 9.69% (95% CI 2.98 to 27.24%, Fig.  3B), with a 
heterogeneity of 58% (p < 0.01).
Sensitivity analysis and quality assessment
A leave-one-out sensitivity analysis was conducted to assess 
the impact of individual studies on the prevalence estimates 
of overall mosaicism, APC mutation, MLH1, and MSH2 
mosaicism. A significant reduction in heterogeneity (I 2 
decreased from 58 to 0%) was observed for the prevalence of 
MSH2 mosaicism when the Mur 2014 study was excluded. 
However, omitting individual studies in the other sensi-
tivity analyses did not result in substantial changes to the 
heterogeneity values. The funnel plot of overall prevalence 
mosaicism in Fig. 4 exhibited an asymmetrical distribution, 
suggesting a potential risk of publication bias. This is 
expected given the nature of the analysis, which involved 
single-arm observational studies with varying levels of vari-
ance. For quality assessment we used the Newcastle–Ottawa 
Scale for observational studies sixteen studies were consid-
ered high quality and eleven studies as low quality (Fig. 5).
Discussion
This meta-analysis aimed to explore the prevalence and 
clinical significance of mosaicism in patients with CRC and 
polyposis syndromes. We identified 27 studies that met our 
inclusion criteria, with data sourced from major databases, 
including PubMed, Scopus, and Web of Science. Our sys-
tematic review focused on specific genes linked to mosai-
cism, including APC, MLH1, and MSH2. The findings dem-
onstrate a clear association between mosaicism and these 
gene mutations, highlighting the importance of mosaicism 
in CRC pathogenesis and polyposis. The estimated overall 
prevalence of mosaicism was 8.79%, but this rate varied sig-
nificantly depending on the gene involved.
Our analysis of APC mutations showed a prevalence of 
13.43%, reinforcing the critical role this gene plays in FAP 
and attenuated familial adenomatous polyposis (AFAP). The 
high heterogeneity observed in the studies, with an I 2 value 
of 87%, reflects the complexity of APC mosaicism, which 
Fig. 3  Prevalence. A MLH1. B MSH2

International Journal of Colorectal Disease (2024) 39:201 
 Page 9 of 14 201
likely arises from its diverse clinical presentations and the 
range of detection methods used across studies. APC mosai-
cism is increasingly recognized as a cause of de novo FAP 
and AFAP, where patients may present with fewer adenomas 
or a later onset of symptoms [10, 70]. This highlights the 
need for improved detection techniques to accurately diag-
nose mosaicism in clinical practice [11, 71, 72].
MLH1 mosaicism, with an estimated prevalence of 
2.75%, was less common but still significant. This mutation 
is associated with Lynch syndrome, a hereditary condition 
that increases the risk of CRC and other cancers [73– 75]. 
Despite its lower prevalence compared to APC mutations, 
MLH1 mosaicism plays a crucial role in CRC susceptibility 
[76, 77]. The studies included in this meta-analysis showed 
moderate heterogeneity (I2 = 71%), suggesting variability in 
the methods used to detect mosaic MLH1 mutations. This 
highlights the need for more standardized protocols in future 
research to accurately assess the prevalence and clinical 
implications of MLH1 mosaicism [78].
The prevalence of MSH2 mosaicism, reported at 9.69%, 
was based on three studies involving 86 patients. Although 
the sample size was smaller, the heterogeneity was rela-
tively low (I2 = 58%), indicating a more consistent detection 
method across these studies. MSH2 mosaicism, like MLH1, 
is associated with Lynch syndrome and poses a significant 
risk for CRC development [73, 79–81]. Given the increasing 
recognition of mosaic mutations in Lynch syndrome genes, 
it is essential to incorporate mosaicism screening into the 
standard genetic testing for patients with suspected Lynch 
syndrome, particularly when no germline mutations are 
identified [75, 82].
The overall prevalence of mosaicism in our analysis, 
8.79%, may be an underestimate due to the limitations in 
detection methods, particularly in older studies that relied on 
less sensitive techniques. Newer methods, such as NGS and 
droplet digital PCR, have shown greater sensitivity in detect-
ing low-level mosaicism, but their use is not yet widespread 
in routine diagnostics [83, 84]. This variability in detection 
technologies likely contributed to the significant heterogene-
ity observed across studies. Future research should prioritize 
the development and implementation of more sensitive and 
standardized methods for detecting mosaicism to provide 
more accurate prevalence estimates.
One of the major challenges in studying mosaicism is 
the wide range of clinical presentations, particularly for 
genes like APC, where mosaic mutations can result in either 
severe FAP or milder AFAP phenotypes [85]. This clinical 
variability complicates the diagnosis and management of 
mosaicism, as traditional genetic screening methods may 
not capture low-level mosaic mutations present in a small 
proportion of cells [86, 87]. Our findings emphasize the need 
for clinicians to consider mosaicism in patients with atypical 
or milder presentations of polyposis syndromes, even when 
family history is absent.
The prior study by Jansen and Goel [ 10], a systematic 
review on mosaicism in colorectal cancer and polyposis 
syndromes, identified that genomic mosaicism may play 
an important role in contributing to the predisposition for 
Fig. 4  Funnel plot of overall mosaicism

 International Journal of Colorectal Disease (2024) 39:201
201 Page 10 of 14
colorectal cancer development and in the phenotypic vari-
ability observed in hereditary polyposis syndromes. Our 
analysis expands upon these findings by incorporating addi-
tional studies and conducting a meta-analysis, a quantitative 
assessment of mosaicism frequency and its clinical charac-
teristics within these populations. The statistical analysis in 
our study not only serves to quantify the frequency of these 
mutations but is also particularly important for the diagnos-
tic and prognostic implications, which are addressed here 
for the first time.
The clinical implications of mosaicism extend beyond 
diagnosis to genetic counseling and patient management. 
Patients with mosaic variants may have a lower risk of 
transmitting the mutation to offspring, depending on the 
timing and extent of the mosaic mutation during embry -
onic development [11]. However, the potential for germline 
transmission remains a concern, particularly for early-onset 
CRC cases [88]. As such, genetic counseling for patients 
with mosaicism should be approached with caution, and 
testing of family members may be warranted, especially 
Fig. 5  Newcastle–Ottawa scale

International Journal of Colorectal Disease (2024) 39:201 
 Page 11 of 14 201
in cases of APC mosaicism where the risk of transmission 
is higher.
Conclusion
In conclusion, this meta-analysis provides important 
insights into the prevalence and clinical impact of mosai-
cism in CRC and polyposis syndromes. The significant 
heterogeneity observed in the studies highlights the need 
for more standardized detection methods and larger, more 
comprehensive studies. Despite these limitations, our find-
ings support the growing recognition of mosaicism as a 
critical factor in CRC susceptibility and underscore the 
importance of incorporating mosaicism screening into rou-
tine genetic testing for at-risk patients. Future research 
should focus on refining detection techniques and explor -
ing the full clinical spectrum of mosaicism to improve 
patient care and outcomes.
Supplementary Information The online version contains supplemen-
tary material available at https:// doi. org/ 10. 1007/ s00384- 024- 04776-8.
Acknowledgements We thank the Federal University of Pará (UFPA); 
the Center for Research Oncology (NPO/UFPA), and thanks to the Pró-
Reitoria de Pesquisa e Pós-Graduação da UFPA (PROPESP) for pay -
ing for the article’s publication fee. This support had no role in study 
design, data collection and analysis, decision to publish, or preparation 
of the manuscript.
Author contribution All authors contributed to the study conception 
and design. [F.C.A.M] conceived the project, material preparation, data 
collection and analysis were performed by [F.C.A.M., and N.R.M.]. 
The figures and tables were created by [F.C.A.M., V.K.T.S., C.W.T. 
N., and R.M.R.B.]. The first draft of the manuscript was written by 
[F.C.A.M., N.R.M., V.K.T.S., C.W.T. N., and R.M.R.B.] and all authors 
commented on previous versions of the manuscript. All authors read 
and approved the final manuscript.
Data availability Availability of data and materials: Data is provided 
within the manuscript or supplementary information files.
Declarations 
Ethical approval Not applicable.
Consent for publication  Not applicable.
Conflict of interest The authors declare no competing interests.
Open Access This article is licensed under a Creative Commons Attri-
bution 4.0 International License, which permits use, sharing, adapta-
tion, distribution and reproduction in any medium or format, as long 
as you give appropriate credit to the original author(s) and the source, 
provide a link to the Creative Commons licence, and indicate if changes 
were made. The images or other third party material in this article are 
included in the article’s Creative Commons licence, unless indicated 
otherwise in a credit line to the material. If material is not included in 
the article’s Creative Commons licence and your intended use is not 
permitted by statutory regulation or exceeds the permitted use, you will 
need to obtain permission directly from the copyright holder. To view a 
copy of this licence, visit http://creativecommons.org/licenses/by/4.0/.
References
 1. Rawla P, Sunkara T, Barsouk A (2019) Epidemiology of colo -
rectal cancer: incidence, mortality, survival, and risk factors. Prz 
Gastroenterol 14:89–103. https:// doi. org/ 10. 5114/ pg. 2018. 81072
 2. Marcellinaro R, Spoletini D, Grieco M et al (2023) Colorectal 
cancer: current updates and future perspectives. J Clin Med 13:40. 
https:// doi. org/ 10. 3390/ jcm13 010040
 3. Roshandel G, Ghasemi-Kebria F, Malekzadeh R (2024) Colorec-
tal cancer: epidemiology, risk factors, and prevention. Cancers 
16:1530. https:// doi. org/ 10. 3390/ cance rs160 81530
 4. Aquino de Moraes FC, Dantas Leite Pessôa FD, de Castro D, 
Ribeiro CH et  al (2024) Trifluridine-tipiracil plus bevaci -
zumab versus trifluridine-tipiracil monotherapy for chemore-
fractory metastatic colorectal cancer: a systematic review and 
meta-analysis. BMC Cancer 24:674. https:// doi. org/ 10. 1186/  
s12885- 024- 12447-8
 5. de Moraes FCA, Kelly FA, Souza MEC, Burbano RMR (2024) 
Impact of adjuvant chemotherapy on survival after pathological 
complete response in rectal cancer: a meta-analysis of 31,558 
patients. Int J Colorectal Dis 39:96. https:// doi. org/ 10. 1007/ 
s00384- 024- 04668-x
 6. Hernandez Dominguez O, Yilmaz S, Steele SR (2023) Stage IV 
colorectal cancer management and treatment. J Clin Med 12:2072. 
https:// doi. org/ 10. 3390/ jcm12 052072
 7. Valle L (2014) Genetic predisposition to colorectal cancer: where 
we stand and future perspectives. World J Gastroenterol 20:9828–
9849. https:// doi. org/ 10. 3748/ wjg. v20. i29. 9828
 8. PDQ Cancer Genetics Editorial Board (2002) Genetics of Colo-
rectal Cancer (PDQ®): Health Professional Version. In: PDQ 
Cancer Information Summaries. National Cancer Institute (US), 
Bethesda (MD)
 9. Freed D, Stevens EL, Pevsner J (2014) Somatic mosaicism in 
the human genome. Genes 5:1064–1094. https:// doi. org/ 10. 3390/ 
genes 50410 64
 10. Lucia Jansen AM, Goel A (2020) Mosaicism in patients with colo-
rectal cancer or polyposis syndromes: a systematic review. Clin 
Gastroenterol Hepatol 18:1949–1960. https:// doi. org/ 10. 1016/j. 
cgh. 2020. 02. 049
 11. Campbell IM, Shaw CA, Stankiewicz P, Lupski JR (2015) Somatic 
mosaicism: implications for disease and transmission genetics. 
Trends Genet 31:382–392. https:// doi. org/ 10. 1016/j. tig. 2015. 03. 
013
 12. Thorpe J, Osei-Owusu IA, Avigdor BE et al (2020) Mosaicism in 
human health and disease. Annu Rev Genet 54:487–510. https://  
doi. org/ 10. 1146/ annur ev- genet- 041720- 093403
 13. Mohiuddin M, Kooy RF, Pearson CE (2022) De novo mutations, 
genetic mosaicism and human disease. Front Genet 13:983668. 
https:// doi. org/ 10. 3389/ fgene. 2022. 983668
 14. Acuna-Hidalgo R, Veltman JA, Hoischen A (2016) New insights 
into the generation and role of de novo mutations in health 
and disease. Genome Biol 17:241. https:// doi. org/ 10. 1186/ 
s13059- 016- 1110-1
 15. Uchimura A, Matsumoto H, Satoh Y et al (2022) Early embry -
onic mutations reveal dynamics of somatic and germ cell line-
ages in mice. Genome Res 32:945–955. https:// doi. org/ 10. 1101/ 
gr. 276363. 121

 International Journal of Colorectal Disease (2024) 39:201
201 Page 12 of 14
 16. Muyas F, Zapata L, Guigó R, Ossowski S (2020) The rate and 
spectrum of mosaic mutations during embryogenesis revealed by 
RNA sequencing of 49 tissues. Genome Med 12:49. https:// doi.  
org/ 10. 1186/ s13073- 020- 00746-1
 17. Ansari A, Pillarisetty LS (2024) Embryology, ectoderm. In: Stat-
Pearls. StatPearls Publishing, Treasure Island (FL)
 18. Thowfeequ S, Srinivas S (2022) Embryonic and extraembry -
onic tissues during mammalian development: shifting bound -
aries in time and space. Philos Trans R Soc Lond B Biol Sci 
377:20210255. https:// doi. org/ 10. 1098/ rstb. 2021. 0255
 19. Shussman N, Wexner SD (2014) Colorectal polyps and polyposis 
syndromes. Gastroenterol Rep 2:1–15. https:// doi. org/ 10. 1093/ 
gastro/ got041
 20. Talseth-Palmer BA (2017) The genetic basis of colonic adenoma-
tous polyposis syndromes. Hered Cancer Clin Pract 15:5. https:// 
doi. org/ 10. 1186/ s13053- 017- 0065-x
 21. Ju YS, Martincorena I, Gerstung M et al (2017) Somatic mutations 
reveal asymmetric cellular dynamics in the early human embryo. 
Nature 543:714–718. https:// doi. org/ 10. 1038/ natur e21703
 22. Yen T, Stanich PP, Axell L, Patel SG (1993) APC-associated poly-
posis conditions. In: Adam MP, Feldman J, Mirzaa GM, et al (eds) 
GeneReviews®. University of Washington, Seattle, Seattle (WA)
 23. Lee M, Lui ACY, Chan JCK et al (2023) Revealing parental 
mosaicism: the hidden answer to the recurrence of apparent de 
novo variants. Hum Genomics 17:91. https:// doi. org/ 10. 1186/  
s40246- 023- 00535-y
 24. de Moraes FCA, de Oliveira Rodrigues ALS, Priantti JN et al 
(2024) Efficacy and safety of anti-EGFR therapy rechallenge 
in metastatic colorectal cancer: a systematic review and meta-
analysis. J Gastrointest Canc 56:9. https:// doi. org/ 10. 1007/  
s12029- 024- 01128-1
 25. de Moraes FCA, Pasqualotto E, Chavez MP et al (2024) Effi-
cacy and safety of Zolbetuximab plus chemotherapy for advanced 
CLDN18.2-positive gastric or gastro-oesophageal adenocarci-
noma: a meta-analysis of randomized clinical trials. BMC Cancer 
24:240. https:// doi. org/ 10. 1186/ s12885- 024- 11980-w
 26. Vijg J (2014) Somatic mutations, genome mosaicism, cancer 
and aging. Curr Opin Genet Dev 26:141–149. https:// doi. org/ 10. 
1016/j. gde. 2014. 04. 002
 27. dos Santos W, dos Reis MB, Porto J et  al (2022) Somatic 
targeted mutation profiling of colorectal cancer precursor 
lesions. BMC Med Genomics 15:143. https:// doi. org/ 10. 1186/  
s12920- 022- 01294-w
 28. Groenewald W, Lund AH, Gay DM (2023) The role of WNT 
pathway mutations in cancer development and an overview of 
therapeutic options. Cells 12:990. https:// doi. org/ 10. 3390/ cells 
12070 990
 29. Hankey W, Frankel WL, Groden J (2018) Functions of the 
APC tumor suppressor protein dependent and independent of 
canonical WNT signaling: Implications for therapeutic target-
ing. Cancer Metastasis Rev 37:159–172. https:// doi. org/ 10. 1007/ 
s10555- 017- 9725-6
 30. Bienz M, Clevers H (2000) Linking colorectal cancer to Wnt sign-
aling. Cell 103:311–320. https:// doi. org/ 10. 1016/ S0092- 8674(00) 
00122-7
 31. Testa U, Pelosi E, Castelli G (2018) Colorectal cancer: genetic 
abnormalities, tumor progression, tumor heterogeneity, clonal 
evolution and tumor-initiating cells. Med Sci 6:31. https:// doi.  
org/ 10. 3390/ medsc i6020 031
 32. Lindor NM, McMaster ML, Lindor CJ, Greene MH (2008) Con-
cise handbook of familial cancer susceptibility syndromes. J Natl 
Cancer Inst Monogr 2008(38):3–93. https:// doi. org/ 10. 1093/ jncim 
onogr aphs/ lgn001
 33. Moraes FCA de, Rodrigues Sobreira LE, Cavalcanti Souza ME, 
Burbano RMR The role of CLDN18.2 in gastric cancer prognosis: 
a systematic review and meta-analysis. Biomarkers 1–14. https:// 
doi. org/ 10. 1080/ 13547 50X. 2024. 24229 65
 34. Haimov D, Lieberman S, Castellvi-Bel S et al (2022) Nonma-
lignant features associated with inherited colorectal cancer syn-
dromes-clues for diagnosis. Cancers 14:628. https:// doi. org/ 10. 
3390/ cance rs140 30628
 35. Yamaguchi K, Komura M, Yamaguchi R et al (2015) Detection of 
APC mosaicism by next-generation sequencing in an FAP patient. 
J Hum Genet 60:227–231. https:// doi. org/ 10. 1038/ jhg. 2015. 14
 36. Leoz ML, Carballal S, Moreira L et al (2015) The genetic basis of 
familial adenomatous polyposis and its implications for clinical 
practice and risk management. Appl Clin Genet 8:95–107. https:// 
doi. org/ 10. 2147/ TACG. S51484
 37. Cook CB, Armstrong L, Boerkoel CF et al (2021) Somatic mosai-
cism detected by genome-wide sequencing in 500 parent–child 
trios with suspected genetic disease: clinical and genetic coun-
seling implications. Cold Spring Harb Mol Case Stud 7:a006125. 
https:// doi. org/ 10. 1101/ mcs. a0061 25
 38. Page MJ, McKenzie JE, Bossuyt PM et al (2021) The PRISMA 
2020 statement: an updated guideline for reporting systematic 
reviews. BMJ 372:n71. https:// doi. org/ 10. 1136/ bmj. n71
 39. Schiavo JH (2019) PROSPERO: an international register of sys-
tematic review Protocols. Med Ref Serv Q 38:171–180. https://  
doi. org/ 10. 1080/ 02763 869. 2019. 15880 72
 40. Lo CK-L, Mertz D, Loeb M (2014) Newcastle-Ottawa Scale: 
comparing reviewers’ to authors’ assessments. BMC Med Res 
Methodol 14:45. https:// doi. org/ 10. 1186/ 1471- 2288- 14- 45
 41. Higgins JPT, Thompson SG, Deeks JJ, Altman DG (2003) Meas-
uring inconsistency in meta-analyses. BMJ 327:557–560. https:// 
doi. org/ 10. 1136/ bmj. 327. 7414. 557
 42. IntHout J, Ioannidis JPA, Borm GF (2014) The Hartung-Knapp-
Sidik-Jonkman method for random effects meta-analysis is 
straightforward and considerably outperforms the standard Der -
Simonian-Laird method. BMC Med Res Methodol 14:25. https:// 
doi. org/ 10. 1186/ 1471- 2288- 14- 25
 43. Aretz S, Stienen D, Friedrichs N et al (2007) Somatic APC mosai-
cism: a frequent cause of familial adenomatous polyposis (FAP). 
Hum Mutat 28:985–992. https:// doi. org/ 10. 1002/ humu. 20549
 44. Baert-Desurmont S, Coutant S, Charbonnier F et al (2018) Opti-
mization of the diagnosis of inherited colorectal cancer using 
NGS and capture of exonic and intronic sequences of panel 
genes. Eur J Hum Genet 26:1597–1602. https:// doi. org/ 10. 1038/ 
s41431- 018- 0207-2
 45. Bossard C, Küry S, Jamet P et al (2012) Delineation of the infre-
quent mosaicism of KRAS mutational status in metastatic colo-
rectal adenocarcinomas. J Clin Pathol 65:466–469. https:// doi. org/ 
10. 1136/ jclin path- 2011- 200608
 46. Chan TL, Yuen ST, Kong CK et al (2006) Heritable germline epimu-
tation of MSH2 in a family with hereditary nonpolyposis colorectal 
cancer. Nat Genet 38:1178–1183. https:// doi. org/ 10. 1038/ ng1866
 47. Ciavarella M, Miccoli S, Prossomariti A et al (2018) Somatic APC 
mosaicism and oligogenic inheritance in genetically unsolved 
colorectal adenomatous polyposis patients. Eur J Hum Genet 
26:387–395. https:// doi. org/ 10. 1038/ s41431- 017- 0086-y
 48. Farrington SM, Dunlop MG (1999) Mosaicism and sporadic 
familial adenomatous polyposis. Am J Hum Genet 64:653–658. 
https:// doi. org/ 10. 1086/ 302236
 49. Guillerm E, Svrcek M, Bardier-Dupas A et al (2020) Molecular 
tumor testing in patients with Lynch-like syndrome reveals a de 
novo mosaic variant of a mismatch repair gene transmitted to off-
spring. Eur J Hum Genet 28:1624–1628. https:// doi. org/ 10. 1038/ 
s41431- 020- 0689-6
 50. Hes FJ, Nielsen M, Bik EC et al (2008) Somatic APC mosaicism: 
an underestimated cause of polyposis coli. Gut 57:71–76. https:// 
doi. org/ 10. 1136/ gut. 2006. 117796

International Journal of Colorectal Disease (2024) 39:201 
 Page 13 of 14 201
 51. Hitchins MP, Owens SE, Kwok C-T et al (2011) Identification of 
new cases of early-onset colorectal cancer with an MLH1 epimu-
tation in an ethnically diverse South African cohort. Clin Genet 
80:428–434. https:// doi. org/ 10. 1111/j. 1399- 0004. 2011. 01660.x
 52. Hitchins MP, Dámaso E, Alvarez R et al (2023) Constitutional 
MLH1 methylation is a major contributor to mismatch repair-
deficient, MLH1-methylated colorectal cancer in patients aged 
55 years and younger. J Natl Compr Canc Netw 21:743-752.e11. 
https:// doi. org/ 10. 6004/ jnccn. 2023. 7020
 53. Jansen AML, Geilenkirchen MA, van Wezel T et al (2016) 
Whole gene capture analysis of 15 CRC susceptibility genes in 
suspected Lynch syndrome Patients. PLoS ONE 11:e0157381. 
https:// doi. org/ 10. 1371/ journ al. pone. 01573 81
 54. Joo JE, Mahmood K, Walker R et al (2023) Identifying primary 
and secondary MLH1 epimutation carriers displaying low-level 
constitutional MLH1 methylation using droplet digital PCR and 
genome-wide DNA methylation profiling of colorectal cancers. Clin 
Epigenetics 15:95. https:// doi. org/ 10. 1186/ s13148- 023- 01511-y
 55. Kanter-Smoler G, Fritzell K, Rohlin A et al (2008) Clinical 
characterization and the mutation spectrum in Swedish adeno-
matous polyposis families. BMC Med 6:10. https:// doi. org/ 10. 
1186/ 1741- 7015-6- 10
 56. Karstensen JG, Hansen TVO, Burisch J et al (2024) Re-eval-
uating the genotypes of patients with adenomatous polyposis 
of unknown etiology: a nationwide study. Eur J Hum Genet 
32:588–592. https:// doi. org/ 10. 1038/ s41431- 024- 01585-z
 57. Kim B, Won D, Jang M et al (2019) Next-generation sequencing 
with comprehensive bioinformatics analysis facilitates somatic 
mosaic APC gene mutation detection in patients with familial 
adenomatous polyposis. BMC Med Genomics 12:103. https://  
doi. org/ 10. 1186/ s12920- 019- 0553-0
 58. Mongin C, Coulet F, Lefevre JH et al (2012) Unexplained poly -
posis: a challenge for geneticists, pathologists and gastroenter -
ologists. Clin Genet 81:38–46. https:// doi. org/ 10. 1111/j. 1399- 
0004. 2011. 01676.x
 59. Morak M, Schackert HK, Rahner N et al (2008) Further evi-
dence for heritability of an epimutation in one of 12 cases with 
MLH1 promoter methylation in blood cells clinically displaying 
HNPCC. Eur J Hum Genet 16:804–811. https:// doi. org/ 10. 1038/ 
ejhg. 2008. 25
 60. Mur P, De Voer RM, Olivera-Salguero R et al (2018) Germline 
mutations in the spindle assembly checkpoint genes BUB1 and 
BUB3 are infrequent in familial colorectal cancer and polyposis. 
Mol Cancer 17:23. https:// doi. org/ 10. 1186/ s12943- 018- 0762-8
 61. Out AA, van Minderhout IJHM, van der Stoep N et al (2015) 
High-resolution melting (HRM) re-analysis of a polyposis 
patients cohort reveals previously undetected heterozygous and 
mosaic APC gene mutations. Fam Cancer 14:247–257. https://  
doi. org/ 10. 1007/ s10689- 015- 9780-5
 62. Pinto D, Pinto C, Guerra J et al (2018) Contribution of MLH1 
constitutional methylation for Lynch syndrome diagnosis in 
patients with tumor MLH1 downregulation. Cancer Med 7:433–
444. https:// doi. org/ 10. 1002/ cam4. 1285
 63. Rofes P, González S, Navarro M et al (2021) Paired somatic-ger-
mline testing of 15 polyposis and colorectal cancer-predisposing 
genes highlights the role of APC mosaicism in de novo familial 
adenomatous polyposis. J Mol Diagn 23:1452–1459. https:// doi. 
org/ 10. 1016/j. jmoldx. 2021. 07. 024
 64. Sourrouille I, Coulet F, Lefevre JH et  al (2013) Somatic 
mosaicism and double somatic hits can lead to MSI colorec-
tal tumors. Fam Cancer 12:27–33. https:// doi. org/ 10. 1007/ 
s10689- 012- 9568-9
 65. Spier I, Drichel D, Kerick M et al (2016) Low-level APC muta-
tional mosaicism is the underlying cause in a substantial frac-
tion of unexplained colorectal adenomatous polyposis cases. 
J Med Genet 53:172–179. https:// doi. org/ 10. 1136/ jmedg  
enet- 2015- 103468
 66. Spier I, Kerick M, Drichel D et al (2016) Exome sequencing iden-
tifies potential novel candidate genes in patients with unexplained 
colorectal adenomatous polyposis. Fam Cancer 15:281–288. 
https:// doi. org/ 10. 1007/ s10689- 016- 9870-z
 67. Suter CM, Martin DIK, Ward RL (2004) Germline epimutation of 
MLH1 in individuals with multiple cancers. Nat Genet 36:497–
501. https:// doi. org/ 10. 1038/ ng1342
 68. Takao M, Yamaguchi T, Eguchi H et al (2021) APC germline vari-
ant analysis in the adenomatous polyposis phenotype in Japanese 
patients. Int J Clin Oncol 26:1661–1670. https:// doi. org/ 10. 1007/ 
s10147- 021- 01946-4
 69. Ward RL, Dobbins T, Lindor NM et al (2013) Identification of 
constitutional MLH1 epimutations and promoter variants in colo-
rectal cancer patients from the Colon Cancer Family Registry. 
Genet Med 15:25–35. https:// doi. org/ 10. 1038/ gim. 2012. 91
 70. Half E, Bercovich D, Rozen P (2009) Familial adenomatous 
polyposis. Orphanet J Rare Dis 4:22. https:// doi. org/ 10. 1186/  
1750- 1172-4- 22
 71. Vado Y, Manero-Azua A, Pereda A, Perez de Nanclares G (2024) 
Choosing the Best Tissue and Technique to Detect Mosaicism 
in Fibrous Dysplasia/McCune–Albright Syndrome (FD/MAS). 
Genes 15:120. https:// doi. org/ 10. 3390/ genes 15010 120
 72. Lagarde A, Mougel G, Coppin L et al (2022) Systematic detec -
tion of mosaicism by using digital NGS reveals three new MEN1 
mosaicisms. Endocr Connect 11:e220093. https:// doi. org/ 10. 1530/ 
EC- 22- 0093
 73. Ramsoekh D, Wagner A, van Leerdam ME et al (2009) Cancer 
risk in MLH1, MSH2 and MSH6 mutation carriers; different risk 
profiles may influence clinical management. Hered Cancer Clin 
Pract 7:17. https:// doi. org/ 10. 1186/ 1897- 4287-7- 17
 74. Idos G, Valle L (1993) Lynch Syndrome. In: Adam MP, Feldman 
J, Mirzaa GM, et al (eds) GeneReviews®. University of Washing-
ton, Seattle, Seattle (WA)
 75. Bhattacharya P, Leslie SW, McHugh TW (2024) Lynch syndrome 
(hereditary nonpolyposis colorectal cancer). In: StatPearls. Stat-
Pearls Publishing, Treasure Island (FL)
 76. Castillejo A, Hernández-Illán E, Rodriguez-Soler M et al (2015) 
Prevalence of MLH1 constitutional epimutations as a cause of 
Lynch syndrome in unselected versus selected consecutive series 
of patients with colorectal cancer. J Med Genet 52:498–502. 
https:// doi. org/ 10. 1136/ jmedg enet- 2015- 103076
 77. Boland PM, Yurgelun MB, Boland CR (2018) Recent progress in 
Lynch syndrome and other familial colorectal cancer syndromes. 
CA Cancer J Clin 68:217–231. https:// doi. org/ 10. 3322/ caac. 21448
 78. Yurgelun MB, Hampel H (2018) Recent advances in Lynch syn-
drome: diagnosis, treatment, and cancer prevention. Am Soc 
Clin Oncol Educ Book 101–109. https:// doi. org/ 10. 1200/ EDBK_ 
208341
 79. Win AK, Dowty JG, Reece JC et al (2021) Variation in the risk of 
colorectal cancer in families with Lynch syndrome: a retrospec-
tive cohort study. Lancet Oncol 22:1014–1022. https:// doi. org/ 10. 
1016/ S1470- 2045(21) 00189-3
 80. Plaschke J, Engel C, Krüger S et al (2004) Lower incidence of 
colorectal cancer and later age of disease onset in 27 families with 
pathogenic MSH6 germline mutations compared with families 
with MLH1 or MSH2 mutations: the German Hereditary Non-
polyposis Colorectal Cancer Consortium. J Clin Oncol 22:4486–
4494. https:// doi. org/ 10. 1200/ JCO. 2004. 02. 033
 81. Dal Buono A, Puccini A, Franchellucci G et al (2024) Lynch syn-
drome: from multidisciplinary management to precision preven-
tion. Cancers 16:849. https:// doi. org/ 10. 3390/ cance rs160 50849
 82. Gallon R, Gawthorpe P, Phelps RL et al (2021) How should we 
test for Lynch syndrome? A review of current guidelines and 

 International Journal of Colorectal Disease (2024) 39:201
201 Page 14 of 14
future strategies. Cancers 13:406. https:// doi. org/ 10. 3390/ cance 
rs130 30406
 83. Lee WS, Lockhart PJ (2023) Utility of droplet digital polymerase 
chain reaction for studying somatic mosaicism: brain malforma-
tions and beyond. Neural Regen Res 18:2389–2390. https:// doi.  
org/ 10. 4103/ 1673- 5374. 371356
 84. Salk JJ, Schmitt MW, Loeb LA (2018) Enhancing the accuracy 
of next-generation sequencing for detecting rare and subclonal 
mutations. Nat Rev Genet 19:269–285. https:// doi. org/ 10. 1038/ 
nrg. 2017. 117
 85. Truty R, Rojahn S, Ouyang K et al (2023) Patterns of mosai-
cism for sequence and copy-number variants discovered through 
clinical deep sequencing of disease-related genes in one million 
individuals. Am J Hum Genet 110:551–564. https:// doi. org/ 10. 
1016/j. ajhg. 2023. 02. 013
 86. Campbell IM, Yuan B, Robberecht C et al (2014) Parental somatic 
mosaicism is underrecognized and influences recurrence risk of 
genomic disorders. Am J Hum Genet 95:173–182. https:// doi. org/ 
10. 1016/j. ajhg. 2014. 07. 003
 87. Rohlin A, Wernersson J, Engwall Y et al (2009) Parallel sequenc-
ing used in detection of mosaic mutations: comparison with four 
diagnostic DNA screening techniques. Hum Mutat 30:1012–1020. 
https:// doi. org/ 10. 1002/ humu. 20980
 88. Stoffel EM, Murphy CC (2020) Epidemiology and mechanisms 
of the increasing incidence of colon and rectal cancers in young 
adults. Gastroenterology 158:341–353. https:// doi. org/ 10. 1053/j. 
gastro. 2019. 07. 055
Publisher's Note Springer Nature remains neutral with regard to 
jurisdictional claims in published maps and institutional affiliations.