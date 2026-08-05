---
reference_id: DOI:10.1038/s41467-023-41857-8
title: Multifaceted analysis of cross-tissue transcriptomes reveals phenotype–endotype associations in atopic dermatitis
authors:
- Aiko Sekita
- Hiroshi Kawasaki
- Ayano Fukushima-Nomura
- Kiyoshi Yashiro
- Keiji Tanese
- Susumu Toshima
- Koichi Ashizaki
- Tomohiro Miyai
- Junshi Yazaki
- Atsuo Kobayashi
- Shinichi Namba
- Tatsuhiko Naito
- Qingbo S. Wang
- Eiryo Kawakami
- Jun Seita
- Osamu Ohara
- Kazuhiro Sakurada
- Yukinori Okada
- Masayuki Amagai
- Haruhiko Koseki
journal: Nature Communications
year: '2023'
doi: 10.1038/s41467-023-41857-8
content_type: full_text_pdf
full_text_attempted: true
full_text_provider: openalex
full_text_url: "https://www.nature.com/articles/s41467-023-41857-8.pdf"
oa_status: gold
license: cc-by
local_pdf_path: files/DOI_10.1038_s41467-023-41857-8.pdf
---

# Multifaceted analysis of cross-tissue transcriptomes reveals phenotype–endotype associations in atopic dermatitis
**Authors:** Aiko Sekita, Hiroshi Kawasaki, Ayano Fukushima-Nomura, Kiyoshi Yashiro, Keiji Tanese, Susumu Toshima, Koichi Ashizaki, Tomohiro Miyai, Junshi Yazaki, Atsuo Kobayashi, Shinichi Namba, Tatsuhiko Naito, Qingbo S. Wang, Eiryo Kawakami, Jun Seita, Osamu Ohara, Kazuhiro Sakurada, Yukinori Okada, Masayuki Amagai, Haruhiko Koseki
**Journal:** Nature Communications (2023)
**DOI:** [10.1038/s41467-023-41857-8](https://doi.org/10.1038/s41467-023-41857-8)

## Content

Abstract
Atopic dermatitis (AD) is a skin disease that is heterogeneous both in terms of clinical manifestations and molecular profiles. It is increasingly recognized that AD is a systemic rather than a local disease and should be assessed in the context of whole-body pathophysiology. Here we show, via integrated RNA-sequencing of skin tissue and peripheral blood mononuclear cell (PBMC) samples along with clinical data from 115 AD patients and 14 matched healthy controls, that specific clinical presentations associate with matching differential molecular signatures. We establish a regression model based on transcriptome modules identified in weighted gene co-expression network analysis to extract molecular features associated with detailed clinical phenotypes of AD. The two main, qualitatively differential skin manifestations of AD, erythema and papulation are distinguished by differential immunological signatures. We further apply the regression model to a longitudinal dataset of 30 AD patients for personalized monitoring, highlighting patient heterogeneity in disease trajectories. The longitudinal features of blood tests and PBMC transcriptome modules identify three patient clusters which are aligned with clinical severity and reflect treatment history. Our approach thus serves as a framework for effective clinical investigation to gain a holistic view on the pathophysiology of complex human diseases.

Article https://doi.org/10.1038/s41467-023-41857-8
Multifaceted analysis of cross-tissue tran-
scriptomes reveals phenotype–endotype
associations in atopic dermatitis
Aiko Sekita 1,2, Hiroshi Kawasaki1,2, Ayano Fukushima-Nomura 2,
Kiyoshi Yashiro2, Keiji Tanese2, Susumu Toshima1,2,K o i c h iA s h i z a k i1,2,3,
Tomohiro Miyai 1,2,J u n s h iY a z a k i1,A t s u oK o b a y a s h i1, Shinichi Namba 4,5,
Tatsuhiko Naito 4,Q i n g b oS .W a n g1,4,5,E i r y oK a w a k a m i3,6,J u nS e i t a 1,3,
Osamu Ohara 7, Kazuhiro Sakurada3,8, Yukinori Okada 1,4,5 ,
Masayuki Amagai 1,2 &H a r u h i k oK o s e k i1,9
Atopic dermatitis (AD) is a skin disease that is heterogeneous both in terms of
clinical manifestations and molecular proﬁles. It is increasingly recognized
that AD is a systemic rather than a local disease and should be assessed in the
context of whole-body pathophysiolog y .H e r ew es h o w ,v i ai n t e g r a t e dR N A -
sequencing of skin tissue and peripheral blood mononuclear cell (PBMC)
samples along with clinical data from115 AD patients and 14 matched healthy
controls, that speciﬁc clinical presentations associate with matching differ-
ential molecular signatures. We establish a regression model based on tran-
scriptome modules identiﬁed in weighted gene co-expression network
analysis to extract molecular featuresassociated with detailed clinical phe-
notypes of AD. The two main, qualitatively differential skin manifestations of
AD, erythema and papulation are distinguished by differential immunological
signatures. We further apply the regression model to a longitudinal dataset of
30 AD patients for personalized monitoring, highlighting patient hetero-
geneity in disease trajectories. The longitudinal features of blood tests and
PBMC transcriptome modules identify three patient clusters which are aligned
with clinical severity and reﬂect treatment history. Our approach thus serves as
a framework for effective clinical investigation to gain a holistic view on the
pathophysiology of complex human diseases.
Atopic dermatitis (AD) is one of the most common chronic inﬂamma-
tory skin diseases worldwide and is characterized by a highly hetero-
geneous clinical phenotype
1,2. Causal factors, disease course and
underlying immunological pathwaysof AD vary greatly among patients,
making clinical management tremendously complicated3,4.I ns p i t eo f
growing therapeutic options with awave of development of novel tar-
geted drugs such as an anti-IL-4R α antibody5 and an anti-IL-31R α
antibody6, there is no consensus concerning therapeutic decisions for
individual patients7. In order to provide optimal treatment for each
patient with maximum cost-effectiveness, there is an urgent need to
characterize patients in terms of endotypes that are potentially linked
with disease course.
Although recent advances in biomedical technologies have
enabled us to acquire an enormous amount of patient omics data
including genome data, capturing fundamental endophenotypes of
individual patients is still challenging. In the past decades, multiple
Received: 14 September 2022
Accepted: 19 September 2023
Check for updates
A full list of af ﬁliations appears at the end of the paper. e-mail: yuki-okada@m.u-tokyo.ac.jp; amagai@keio.jp; haruhiko.koseki@riken.jp
Nature Communications|         (2023) 14:6133 1
1234567890():,;
1234567890():,;

attempts were made to uncover the biological features of skin tissues
or peripheral blood mononuclear cells (PBMC) from AD patients using
transcriptomic and proteomic approaches. Those studies have
revealed important roles of Th2 or Th17 pathways both in skin and in
PBMC along with altered skin barrier function in AD pathology
8– 10,a n d
some of them further demonstrated how these pathways can be tar-
geted by systemic treatment with immunosuppressants
11, anti-IL-4Rα
antibody12,13 and oral JAK inhibitors14. However, these observations in
either skin tissue or blood only focus on alterations in a speciﬁc part of
the body that could re ﬂect just one aspect of a highly complex
pathology. It is widely recognized that complex diseases should be
assessed in the context of whole-body level biology since organs are
communicating with each other
15– 17. Projects such as GTEx 18 and
Human Cell Atlas 19 can be utilized for per-tissue/cell type character-
ization of human biology, as well as characterization of inter-tissue
communications (“crosstalk”). Skin disorders including AD, which is
now recognized as a systemic disease 20,21, need special attention to
such crosstalk between the originally damaged organ and the circu-
latory system
22,23. The importance of considering cross-tissue interac-
tions in skin immunological regulation is also supported by the
evidence of concurrent biological alterations in both skin tissue and
blood after systemic treatment in AD
12,24,25 or in HIV infection, which
frequently causes cutaneous malignancies or inﬂammation26.
Other essential factors in AD pathology include the hetero-
geneous disease trajectories as characterized by repeated exacerba-
tion and remission, with different cycles by patients. Correspondingly,
most patients have their own medication history over time, based on
their incidence of exacerbations. Accounting for such heterogeneity in
disease trajectory has been extremely challenging in previous omics-
based studies of AD.
In this study, we carry out cross-sectional analysis and long-
itudinal analysis with observational datasets, aiming to capture biolo-
gical signatures in the context of clinical pro ﬁles in the Japanese AD
population. For the cross-sectional analysis, we analyze RNA-seq data
of both skin and PBMC from AD patients and healthy controls and link
them to clinical data. Via building regression models incorporating
both skin and PBMC transcriptome data that are preprocessed into
interpretable transcriptome modules, we establish factors that con-
tribute to clinical presentations across patients. For the longitudinal
analysis, we apply the transcriptome modules along with the regres-
sion models established in the analysis of cross-sectional dataset to a
time series dataset to monitor personalized disease courses and to
examine inter-patient heterogeneity in longitudinal features. These
multifaceted analyses of cross-tissue, cross-sectional and longitudinal
transcriptomes highlight the close association between phenotypes
and endotypes in AD. Our approach serves as a framework for effective
clinical investigation of heterogeneous and complex human diseases.
Results
Characterization of participants
A schematic presentation of the process of ﬁltering samples and
patients for each analysis was shown in Fig. S1. For cross-sectional
analysis, 188 AD patients and 45 healthy controls were extracted
from the overall sample collection according to the criteria de ﬁned
in the section Study design in “Methods”. RNA-seq data from samples
either with low read count (total read count <5 million) or with a
strong batch effect attributable to inadequate sample processing
were excluded. Consequently, 151 AD patients and 19 healthy con-
trols that met the criteria for RNA-seq data were extracted. Patients
were further ﬁltered by gene expression intensity of pilosebaceous
unit-related genes in skin samples (Fig. S2), resulting in 115 AD
patients and 14 healthy controls as eligible samples (one sample per
patient) for regression analysis using all of skin, PBMC and blood
tests (Fig. 1). Frequency distribution of the AD patients by disease
severity is shown in Fig. S3. All the samples (315 skin samples and 235
PBMC samples from both AD patients and healthy controls) that were
assured for RNA-seq data quality by itself were included for tran-
scriptome modules identi ﬁcation to increase power. Of these parti-
cipants, 27.1% (30 AD patients and 5 healthy controls) were female.
Sex (biological attribute) of the participants was determined based
on self-reporting. Their mean age was 41.3 years (AD: 40.5, healthy:
47.3, range, 21 – 70 years).
PBMC
(Once in a month for 1 year)
Clinical severity
Blood tests
Clinical severity
Systemic
treatmentClinical severity
Blood tests
EMR
++
+
HD
TR UP
LW
i) Cross-sectional analysis (n; AD = 115, healthy = 14)
Skin biopsy
a b
i) Detailed evaluation of eczema severity 
EASI partial score
ii) Longitudinal analysis (n; AD = 30)
PBMC sampling
Time
ii) Disease course and medication history
䞉䞉䞉䞉
Time
䞉Head/neck (HD)
䞉Trunk (TR)
䞉Upper limbs (UP)
䞉Lower limbs (LW)
Body region
䞉Lichenification
䞉Erythema
䞉Excoriation
䞉Induration/papulation
Skin manifestation
Fig. 1 | Summary of study design. a This study consists of two parts, i) a cross-
sectional part (n; Atopic dermatitis: AD = 115, healthy = 14) and ii) a longitudinal part
(n; AD = 30) to elucidate endotypes that are associated with phenotypes in AD.
b We focused of two classes of disease phenotypes highlighted by clinical data; i)
skin manifestation and ii) longitudinal disease course along with medication his-
tory, that were examined in association with endotypes in cross-sectional and
longitudinal analysis, respectively. EMR electronic medical records, EASI Eczema
Area and Severity Index.
Article https://doi.org/10.1038/s41467-023-41857-8
Nature Communications|         (2023) 14:6133 2

For longitudinal analysis, time series dataset consisting of PBMC
transcriptome, laboratory blood tests and clinical severity score from
30 AD patients on monthly basis up to a year (total 360 time points)
were extracted, and after quality control, 280 data were considered as
eligible and used for longitudinal analysis. Of these AD patients, 7
patients (23.3%) were female, and 30 patients (100%) and 17 patients
(56.7%) overlapped with the cross-sectional population for PBMC only
and PBMC + skin analysis, respectively.
For meta-analysis of clinical severity scores, we used a total of
1424 data points obtained during the period of November 2016 to July
2021 from the 151 AD patients who were included in cross-sectional
and/or longitudinal analysis. The AD patients in this observational
study were basically under treatment with topical steroids and emol-
lients as directed by dermatologists, except for the 5 patients who
refrained from using topical steroids for some reason. Their history of
systemic treatment was categorized as follows: intermittent use of oral
steroids, intermittent use of immunosuppressant, antiallergic agents
with continuous use (a total of more than 120 days/year), antiallergic
agents with occasional use (a total of fewer than 120 days/year), and no
use of these agents. Drugs used for systemic treatment in the overall
AD population in this study are listed in the Table S2. Characteristic
information of the participants is summarized in Table S3.
Compositional analysis of clinical scores highlighted two dis-
tinct skin manifestations
The extent and severity of atopic dermatitis were measured using the
Eczema Area and Severity Index (EASI) 27. In this scoring system,
severity is determined by grading the key signs of eczema (i.e. ery-
thema, induration/papulation, excoriation, and licheni ﬁcation) over
the four anatomic divisions of the body (i.e. the head and neck, the
trunk, the upper extremities, and th e lower extremities) separately.
The average severity of each sign in each of the four body regions was
assigned a score of 0 – 3 (none, mild, moderate, and severe,
respectively).
To capture the relationship between individual components of
eczema severity, we performed multidimensional scaling (MDS) which
is a visual representation of distances between sets of objects
28 on the
collection of partial scores across patients (Fig.2a). Two major clusters
were found in the aspect of key signs of eczema (Fig. S4); one consisted
of erythema and licheniﬁcation and the other consisted of induration/
papulation and excoriation. This suggested that erythema and
induration/papulation constitute two distinct skin manifestations, apt
to be accompanied by licheniﬁcation and excoriation, respectively, as
signs of progression or chronicity. From a regional perspective, the
conﬁguration of the scores for the four body regions was all in the
same order in the MDS plot, i.e. from left to right are the lower
extremities, the upper extremities, the trunk to the head and neck,
leaving the head and neck distant from the other three regions. This
ﬁnding is consistent with the recent view that head and neck erythema
is a prominent form of AD
29,30.
Based on these ﬁndings, we de ﬁned two distinct phenotypes in
AD, an erythema form and a papulation form, using the summation of
either erythema or papulation scores in all the body regions except for
the head and neck, respectively. Meanwhile, we de ﬁned the general
severity of AD as the summation of all the scores, i.e. EASI (total) as is
conventionally used.
In order to pathologically characterize skin types of both ery-
thema and papulation in AD, we conducted immunohistochemistry
of lesional skin from the six erythema-skewed and the six
papulation-skewed patients (Figs. S5 – 7, Fig. 2b, c). Figure 2b, c
shows clinical and histological images of the representative
patients who have a score composition that is highly skewed to
either erythema or induration/papulation (partial score for the left
patient; erythema = 9.6, papulat ion = 4.8, the right patient; ery-
thema = 4.3, papulation = 8.6). Histological analysis revealed shared
and differential characteristics in the skin tissue between the ery-
thema- and papulation-skewed AD patients. In both skin samples,
intense in ﬁltration of immune cells including CD4
+ Tc e l l( F i g .2c),
macrophage (CD206 +), myeloid dendritic cell (CD11c +,D C - L A M P+)
and Langerhans cell (CD1a +), along with epidermal hyperplasia and
diminished epidermal barrier (as observed by ﬁlaggrin expression)
were commonly observed (Fig. S6). However, the patterns for
immune cell inﬁltration appeared to be different between erythema
and papulation; the skin sample from the erythema-skewed patient
were characterized by diffuse in ﬁltration of immune cells in dermis,
accompanied by epidermal lymphocytic in ﬁltration. On the other
hand, the skin sample from the papulation-skewed patient was
characterized by nodular in ﬁltration of immune cells in dermis
suggestive of geometrical heterogeneity over the lesion, as well as
prominent hyperkeratosis. Those observations were largely
reproduced in other ﬁve erythema-skewed patients and ﬁve
papulation-skewed patients, respectively (Fig. S5). Neutrophil
(myeloperoxidadse: MPO
+)i nﬁltration were substantially observed
in the skin sample from the erythema-skewed patients but not in the
skin sample from the papulation-skewed patients.
Transcriptional characteristics of skin tissue and PBMC typically
found in AD
To identify transcriptome signatures enriched in AD patients, we
ﬁrstly conducted differential gene expression analysis on RNA-seq
data of skin and PBMC specimens. Accordingly, 272 and 33 differ-
entially expressed genes for skin and PBMC, respectively, were
identiﬁed (|log2 fold change (log2FC)| ≧ 2 and false discovery rate
(FDR) < 0.01 for skin and |log2FC| ≧1 and FDR < 0.05 for PBMC,
Fig. 3a). Gene ontology (GO) terms enriched in skin of AD patients
included antimicrobial peptides, chemokine and interleukin signal-
ing genes and epidermal differentiation/keratinization, which is lar-
gely consistent with previous reports
10,31. GO terms enriched in PBMC
of AD patients included neutrophil degranulation and immune sys-
tem (Fig. 3b).
Inference in ligand-receptor coupling suggests augmented skin-
PBMC crosstalk in AD patients
The increased expression of inﬂammation-related genes in both skin
and PBMC suggested that inﬂammation induced in skin tissue in turn
triggered inﬂammatory responses in PBMC, or vice versa in some
cases, presumably through secretion of soluble factors that can act on
cells in the circulatory system
22. In order to illuminate such potential
crosstalk between skin tissue and PBMC, we integrated RNA-seq data
from both sources and quanti ﬁed ligand-receptor couplings that are
particularly engaged in inﬂammatory signaling
32.
We deﬁned active cytokine– receptor pairs as having concurrent
expression of a cytokine gene and its matching receptor gene at a
level of cytokine gene > 0.5 and receptor gene > 0 in value of variance
stabilizing transformation (vst) applied to the expression values that
were followed by normalization across the population. A total of 210
pairs of in ﬂammatory cytokine and receptor genes were assessed in
the skin and PBMC of each AD patient and healthy control. The active
cytokine– receptor pairs were enumerated according to classes
deﬁned by the combination of a sender organ that expressed a
cytokine gene and a receiver organ that expressed a receptor gene
(Fig. 4a; “Methods”). The total number of active cytokine – receptor
pairs was signiﬁcantly higher in AD patients than in healthy controls
(mean = 50.9 vs 29.6; p = 1.0E−3).
Among these, the number of connections from skin to skin and
the number of connections from skin to PBMC were signi ﬁcantly
increased in AD patients compared to healthy controls (mean = 24.6
vs 10.9 and 17.3 vs 10.6; p =8 . 3 E−5a n dp =2 . 8 E−3, respectively), while
the number of connections from PBMC to either of skin or PBMC was
not signiﬁcantly different between AD patients and healthy controls
Article https://doi.org/10.1038/s41467-023-41857-8
Nature Communications|         (2023) 14:6133 3

(Fig. 4b). Stratiﬁed analysis on skin – PBMC interaction revealed pro-
gressive augmentation of the number of links in severe AD compared
to moderate and mild AD, suggesting that systemic in ﬂammation is
more evidently involved in severe AD, although there was no statis-
tical difference among three groups (Fig. S8). There were moderate
correlations between the total number of cytokine – receptor con-
nections and either EASI ( r = 0.32; p =2 . 5 E−4) or serum TARC
(r = 0.35; p = 6.6E−5, Fig. 4c).
The most frequently observed pairs in AD were CCL22-CCR4/and
CCL17-CCR4 in skin, while in healthy controls they were IL37 (skin) -
IL18R1/IL18RAP (PBMC) and IL34 (skin) - CSF1R (skin). The top two
frequently observed pairs involving PBMC in AD were CCL18 (skin) -
CCR8 (PBMC) and IL20 (skin) – IL20RB (PBMC) (Table S4). Cell types
responsible for expression of thes e cytokine/receptor genes were
estimated by referring to publicly available datasets that are suitable
for analyzing cell type expression
33,34. The most frequently appearing
cell types in AD were T cells and vascular endothelial cells (VEC) as
cytokine-expressing cells, and myeloid cells and T cells as receptor-
expressing cells, all of which were found in the skin. The most highly
involved cell type in PBMC was the monocyte, for both cytokine and
receptor expression (Table S5). Collectively, the indication of
enhanced ligand-receptor coupling involving both skin and the circu-
latory system in AD patients suggested the need for a system-level
investigation into AD pathology.
Identiﬁcation and characterization of transcriptional modules
associated with AD
To illuminate the heterogeneity in the biological signature across AD
patients, expression levels of not only DEGs between AD patients and
healthy controls but also the extended range of gene sets that have
potential association with AD pathology should be analyzed. Weighted
gene co-expression network analysis (WGCNA) is a powerful technique
to depict functional subsystems by highlighting biologically relevant
transcripts with reduced dimensionality across a population
35.W e
applied WGCNA to our entire expression dataset, including AD
patients and healthy controls for skin and PBMC, respectively to
identify AD-related transcriptional modules. This procedure identiﬁed
21 skin transcriptional modules (sModus) and 15 PBMC transcriptional
modules (pModus), each comprising 51 – 774 genes (mean; 258.7 for
skin, 191.8 for PBMC) that behave synchronously in a tissue, suggesting
their biological relevance to each other (Fig. 5a).
As expected, genes in each module exhibited substantial cell
type speciﬁcity in their expression as con ﬁrmed by referring to the
publicly available dataset of either single-cell RNA-seq (scRNA-seq)
(for skin) or sorted cell RNA-seq (for PBMC). Figures 5ba n dds h o w
the size of the ﬁrst principal component (PC1) value per cell type
obtained by applying principal component analysis (PCA) on gene
expression data of cell types for each gene module (i.e. matrix withm
columns of gene and n rows of cell types, where m is the number of
b
AD#1
(Erythema-
skewed) 
AD#2
(Papulation-
skewed) 
100 μm10 mm 100 μm
c
a
LW
LW
LW
LW
UP
UP
UP
UP
TR
TR
TR
HD
HD
Lichenification
Erythema
Excoriation
Induration/papulation
Skin manifestation
HD: head/neck
TR: trunk
UP: upper limbs
LW: lower limbs
Body region
MDS2
HD
MDS1
Fig. 2 | Compositional analysis of clinical scores highlighted two distinct skin
manifestations in AD. aSeparation pattern by multidimensional scaling (MDS)
on individual components of EASI across AD patients. Components that are
correlated with each other ( Pearson r > 0.40) were connected with gray lines.
Two major clusters were identi ﬁed in the aspect of key signs of eczema,
among which erythema and induration /papulation are two primary skin
manifestations that bear the distinction. Clinical pictures ( b) and immuno-
histochemistry of skin tissue for CD4 ( c, target protein was stained in red) in
two representative patients who have a score composition that are skewed to
either of erythema (upper) or induration/ papulation (lower). Upper: a 51-year-
old male patient who has erythema-skewed EASI composition (total = 19.6,
erythema = 5.2, papulation = 3.4). Lower: a 50-year-old male patient who has
papulation-skewed EASI composition (total = 21.0, erythema = 3.0, papulation
=8 . 4 ) .O n es l i d ep e rp a t i e n tw a ss t a i n e df o ro n em a r k e rp r o t e i ni nh i s t o l o g i c a l
analysis. Assays for other markers in the same patient samples are shown in
Supplementary Figs. 6 and 7.
Article https://doi.org/10.1038/s41467-023-41857-8
Nature Communications|         (2023) 14:6133 4

genes assigned to a given module). See Fig. S10 and Supplementary
note for further characterization of the gene modules. Relationships
among the top 30 genes of the ﬁrst principal component (PC1) from
each module were visualized on the basis of gene-gene networks
using thresholding of eigengene-based connectivity > 0.65 (Fig. 5c,
e). This analysis revealed several notable signaling compartments in
each tissue; compartments of acquired immune regulation (cytokine
signaling), innate immune regulation (interferon signaling) and
compartments of keratinization/formation of corni ﬁed envelope, in
skin tissue. Additionally, three modules were found to be repre-
senting skin appendages; sebaceous gland (sModu01, GO: fatty acid
metabolism) and sweat gland (sModu03 and sModu19, GO: ion
channel transport and developmental biology, respectively). The
intensity of these modules was not relevant to dermatitis, and was
strongly biased by sampling regions. Therefore, we considered these
two modules as noises, and excluded from the following analysis.
Another potential representation of skin appendage, although it is
not evident as much as above mentioned three modules, is a neu-
roreceptor signature by sModu02 which include KCNH4, CACNA1A
and ASIC2, genes coding ion channel subunits with suggested asso-
ciation with sensory neuron in human skin
36.
To obtain personalized pro ﬁles based on the transcriptional
modules, scores for each module and each patient were de ﬁned.
Since identiﬁed modules consist of co-expressing genes, expression
a
b
Skin PBMC
Antimicrobial peptides
Formation of the cornified envelope
Chemokine receptors bind chemokines
Keratinization
Toll-like Receptor Cascades
Collagen degradation
Toll Like Receptor 4 (TLR4) Cascade
Interferon alpha/beta signaling
Interleukin-10 signaling
Transcriptional Regulation by TP53
Interferon Signaling
Peptide ligand-binding receptors
Neutrophil degranulation
Innate Immune System
Cellular responses to external stimuli
Cellular responses to stress
Signaling by Interleukins
Interleukin-4 and Interleukin-13 signaling
Cytokine Signaling in Immune system
Immune System
AD enrichment score
AD enrichment score
0.0 0.2 0.4 0.6 0.8
BTC
RFX6
CDH12
IL36A
IL13
SOCS3
IFI27
CXCL10
log2(Fold Change)log2(Fold Change)
-log10(FDR)
-log10(FDR)
DUSP4
CCR10
SEMA3G
NOX3
EPGN
IL6
CCL17
CCL18
5
KCNJ3
MPO
FANK1
CSTG
CEACAM6
DEFA4
FOSB CXCL8
DUSP1
FOS
CEACAM8
SGCD
Neutrophil degranulation
Extracellular matrix organization
Cell Cycle, Mitotic
Innate Immune System
Cell Cycle
Immune System
0.0 0.2 0.4 0.6 0.8
Skin PBMC
SERPINB4
SPRR2ALCE3D
S100A9
LCE3E S100A7
S100A8
S100A7A
KRT6C
LCE3A
SPRR2B
SPRR1B
KRT16
C10orf99
SPRR1A
MMP12
NELL2
IL20
DEFB4A
MMP1
KLK6
LTF
Fig. 3 | General transcriptional characteristics of skin and PBMC in AD.
a Volcano plot with signiﬁcantly differentially expressed genes (|log2 fold change
(log2FC)|≧ 2 and false discovery rate (FDR) < 0.01 for skin and |log2FC|≧1a n d
FDR < 0.05 for PBMC) highlighted in red (up-regulated in AD) and blue (down-
regulated in AD) compared to healthy controls (n; AD = 115, healthy = 14).b Gene
ontology (GO) terms enriched in differentially expressed genes in AD (FDR < 0.1 and
Enrichment score > 0.5). Enrichment score was obtained based on the size of a given
gene set in GO terms (see“Methods”). Source data are provided as a Source Dataﬁle.
Article https://doi.org/10.1038/s41467-023-41857-8
Nature Communications|         (2023) 14:6133 5

patterns in each module became simple enough to be handled line-
arly, as veri ﬁed by substantially high value of explanatory capability
of PC1 (40 – 60%) when PCA was applied on gene expression data of
patients for each gene module. Therefore, we used the PC1 values
followed by standardization across patients as the index of intensity
of gene expression of transcriptome modules in each
patient (Fig. S9).
Regression analysis reveals differential patterns of modular
involvement in erythematous and papular skin manifestations
in AD
We next investigated how the AD phenotypes can be represented by
transcriptome modules from both skin and PBMC, as well as by
laboratory tests (Table S6) obtained at the same visits. Given the
relatively large number of variables to the sample size, we built
Fig. 4 | Inference in ligand-receptor coupling suggests augmented skin-PBMC
crosstalk in AD patients. aConnection map of cytokine– receptor coupling across
skin and PBMC in a representative healthy control (left) and AD patient (right).
Genes that code cytokines and receptors are aligned along the perimeter of the
circles. From the outer layer to the center is the tissue expressing the genes (either
skin or PBMC), inferred cell speciﬁcity, classiﬁcation of cytokine or receptor, and
the connections between cytokines and its matching receptors. The connections
were indicated in different colors according to the classiﬁcation of direction, i.e. in
which tissue the cytokines are produced and on which tissue they act. VEC: vascular
endothelia cell, vSMC: vascular smooth muscle cell.b Number of active connec-
tions between cytokines and receptors. Connections were enumerated according
to 4 classes deﬁned by a sender organ and a receiver organ. Boxplots show median
and ﬁrst and third quartiles, whiskers extending to the highest and lowest values no
further than 1.5*interquartile range. Brunner-Munzel rank test, two-sided,
**p < 0.01, NS: not signiﬁcant. c Pearson correlation between number of active
connections and clinical index, two-sided. N; Atopic dermatitis: AD = 115, healthy =
14 (biologically independent samples). Source data are provided as a Source
Data ﬁle.
Article https://doi.org/10.1038/s41467-023-41857-8
Nature Communications|         (2023) 14:6133 6

regression models using elastic net, an algorithm for regularized
regression and variable selection that is applicable to high dimensional
data with multicollinearity37.
To con ﬁrm that regularized regression is superior to linear
model in building regression models on our complex dataset con-
sisting of both skin and PBMC transcriptome, we compared the
performance of the linear model and elastic net (Fig. 6a). We found
that adj R
2 for the test dataset is higher in elastic net model compared
to linear model (adj R2 (training) = 0.65, R2 (test) = 0.02 for linear
model vs adj R2 (training) = 0.64, R2 (test) = 0.43 for elastic net model,
when all the variables are used), verifying the advantage of elastic net
in our data. Although addition of transcriptional modules did not
improve the overall model performance drastically, several gene
modules that were selected as the predictor variables for the AD
a
Skin PBMC
-4 40
Standardized
PC1 value
Cytokine 
signaling
Muscle 
contraction Extracellular
organization
Metabolism
Immune system
Interferon 
signaling
Homeostasis
Signaling by GPCR
Interferon 
signaling
Neutrophil 
degranulation
GPCR 
ligand 
binding
Cell cycle checkpoint
Lymphoid - non-
lymphoid 
interaction
Neutrophil degranulation/
Toll like receptor signaling
Signaling by BCR
FOXP3
CCR4
CCR8
FANK1
DUSP4
IL2RA
IL9R
IFI27
OASL
CXCR5
CD22
MS4A1
SPARC
ITGA2B
TREML1
CD163
KLRD1
CCL5
GZMB
TBX21
PF4
CENPF
MKI67
TOP2A
CDC20
E2F8
TLR4
TLR2
IL7R CCR2GRN
TYROBP
S100A9
FCN1
IL1RL1
CA1
PI16
CCR10
SEMA5A
FGF23
CXCL14
FGFBP2
KDM5D IGF1
IRF4
HSP90B1
GATA2HDC
CCR7
SIGLEC1
CD68
FCRL6
CXCL5
CXCL10
CD19
MX1
PPBP
DDX21
MSR1
CD163
STAB1
MMP2
FBN1
CLEC3B
PI16
COL4A1
KRT6A
S100A8
IL7R
CCL22
FOS
IL20
COL1A2
KRT10
DSC1
TNC
KRT14
DES
ATP5I
DCN
LOX
CCL19
ITGAX
MMP1
ELOVL3
GATA3
AWAT1
DCD
LYZ
AREG
NR4A3 IL2RA
e
c
Fatty acid 
metabolism
Mitotic 
cell cycleFormation of 
cornified 
envelope
FLG
LOR
IL37
KRT16 Cell cycle 
checkpoint
Keratinization
Keratinization
Ion 
channel 
transportSCGB2A2
Fig. 5 | Identiﬁcation and characterization of transcriptional modules from
skin/PBMC RNA-seq data. a Cluster dendrograms of transcripts produced by
implementation of WGCNA. Color indicates separation of transcriptional module.
Cell type expression and GO enrichment in skin tissue (b) and PBMC (d)a n a l y z e db y
referring public database. Visualization of gene-gene networks in PC1 top 30 genes
from each transcriptome module in skin (c) and PBMC (e). Genes that have
eigengene-based connectivity > 0.65 were connected with lines. sModu skin tran-
scriptome module, pModu PBMC transcriptome module, vSMC vascular smooth
muscle cell, IRS/seba inner root sheeth/sebaceous gland, VEC vascular
endothelia cell.
Article https://doi.org/10.1038/s41467-023-41857-8
Nature Communications|         (2023) 14:6133 7

phenotypes provided insights into transcriptional regulation invol-
ving pathology.
We also built elastic net regression models to predict EASI (ery-
thema) and EASI (papulation) which made a major distinction in skin
manifestations as described above. The model performance (R
2)a n d
the set of signi ﬁcant features ( p < 0.05) in each model as well as its
biological characteristics are summarized in Table1.
Both in erythema and in papulation skin manifestation, a
decreased lymphocyte ratio in blood, an indication of increased pro-
portion of myeloid cells (a populational summation of monocytes and
neutrophils) and an increased eosinophil ratio in blood were found to
be associated with symptoms. Erythema was characterized by a bol-
stered signature of immediate early genes ( NR4A1, FOSL1, FOSB,
ATF3, NR4A2) and immune system (CD163, C1QB, C1QC, THY1, MS4A7)
that are inferentially expressed mainly in keratinocytes and myeloid
cells, respectively, in skin tissue, along with Treg speci ﬁcg e n e s
(CCR4, CNTNAP1, DUSP4, LMNA, PI16 ) in PBMC. In contrast, papula-
tion was characterized by decreased B cell signature ( FCRL1, MS4A1,
PAX5, CD22, LINC00926 ) and increased naive CD4 signature ( NELL2,
LRRN3, OBSCN, CCR7, GRASP1 ) in PBMC along with enhanced sig-
nature of interferon signaling ( MMP12, CCL18, IFI27, TYMP, COL6A6 )
and extracellular matrix ( PI15, GREM1, COL4A1, TNFAIP6, NNMT ),
suggestive of altered activity in VEC and ﬁbroblast in skin tissue. We
conﬁrmed by subanalysis that these results were not biased by the
potential in ﬂuence of the treatment difference among patients
(Table S7, Supplementary note). Dysregulated module networks
contributing to distinct phenotypes were predicted based on the
coefﬁcient of each variable (Fig. 6b). These results suggest that
pathologies underlying erythema and papulation are substantially
different on a molecular basis.
Personalized monitoring of trajectory of disease severity and
molecular signatures
One of the most essential features of AD is that patients follow a disease
course complicated by exacerbations and remissions throughout the
years, thereby patients take individual treatment steps based on their
b
EASI (total) EASI (erythema) EASI (papulation)
p01
s10
s14
ALT
Eosinophil
s08
s16s18
Total IgE
Eosinophil
p11
BUN
etycohpmyLetycohpmyL Lymphocyte
Eosinophil
Skin module PBMC module Blood test Negatively regulatedPositively regulated
a
Disease severity
(EASI)
Blood tests
ع+ 
Phenotype Basic information
+
Transcriptome
PBMC 14 modules
Skin 18 modulesHemogram (7)
Biochemistry (10)
Total IgE
Serum TARC
Age, age^2
Sex
ع+ 
ع+ 
ع++ +
ع+ 
Test R2
Elastic net
Train adj.R2
Linear model
(all variables)
0.41
0.29
0.20
0.43
0.56
0.48
0.42
0.65
Test R
2
0.28
0.28
0.13
0.02
Train adj.R
2
0.59
0.52
0.42
0.64
Fig. 6 | Regression analysis revealed differential patterns of modular involve-
ment in erythema and papulation skin manifestation in AD. a Regression
models for the prediction of clinical phenotypes. Adjustment was made forR2 in
training set with the number of prediction variables. b Predicted dysregulated
networks of blood tests and skin/PBMC transcriptome modules contributing to
distinct phenotypes. Node size and node frame color represent size and the sign of
coefﬁcients for each variable predicted by elastic net regression. sXX skin tran-
scriptome module XX, pXX PBMC transcriptome module XX, ALT alanine transa-
minase, BUN blood urea nitrogen.
Article https://doi.org/10.1038/s41467-023-41857-8
Nature Communications|         (2023) 14:6133 8

condition at a given time38,39. To provide an overview including symp-
tom changes and use of systemic treatment in individual patients, we
conducted monthly monitoring of PBMC transcriptomes, laboratory
tests and severity scores for 30 AD patients for up to a year. We lever-
aged transcriptomic modules generated in the cross-sectional patient
dataset and proﬁled the dynamics of transcriptomic features as well as
blood tests that were lastly analyzed in association with disease severity.
We ﬁrst tested the performance of elastic net regression model
trained with cross-sectional dataset when the model was applied to the
longitudinal dataset (Fig. 7a). Prediction performance for EASI (total)
was higher in a model using all of basic information (age, age^2, sex),
laboratory tests and PBMC transcriptome compared to a model using
only basic information and laboratory tests (R
2:0 . 1 5v s−0.24).
Taking a closer look at individual trajectories of disease course, we
found substantial variability in prediction accuracy among patients.
Personalized disease trajectories in two representative patients are
shown as examples in Fig. 7b. In the ﬁrst example, the prediction
seemed successful (Pearson r =0 . 8 1 ;p = 2.4E-3), accurately capturing
the diseaseﬂare (month 5). In contrast, prediction was unsuccessful in
the second example as evident by Pearson r = −0.44 (p =0 . 2 0 ) .T h e r e
was no signi ﬁcant difference in prediction accuracy of personalized
trajectories of disease severity among patients regarding treatment
classes (Fig. S11). We found that the time-course trajectory of the
weights of TARC which was selected as the top predictor varibale in the
elastic net model, strongly correlated with disease severity trajectory
(Pearsonr = 0.88;p =3 . 1 E−4) in theﬁrst example, but not in the second
example (Pearson r = −0.047; p = 0.91) (Fig. S12). These observations
suggest that the predominant features associated with disease course
vary by patients, which could limit the performance of linear models
assuming same feature weights across samples. Application of linear
mixed model (LMM) on each analyte in the time series data also
highlighted the varying random effects by patients (Fig. S13, Supple-
mentary note).
Close association between endotypic longitudinal features and
phenotypic longitudinal features
Given that another factor that accounts for the endotypes in individual
AD patients is longitudinal variability itself38, just as in other chronic
inﬂammatory diseases40, it is important to evaluate time series features
in clinical severity and transcriptome modules. Seven types of time
series features, i.e. mean, minimum, maximum, root mean square
(RMS), mean absolute change (MAC), approximate entropy, and
complexity-invariant distance (CID) were extracted from three cate-
gories of datasets, i.e. blood tests, PBMC transcriptome modules and
clinical severity (i.e. EASI) in individual patients at a monthly interval
over 1 year using the Python module Tsfresh
41 (Fig. 8a).
Hierarchical clustering of those 7 features of clinical severity in 30
AD patients showed two major clusters; one includes mean, maximum,
minimum and RMS, the other includes MAC, CID and approximate
entropy (Fig. S14). Therefore, we picked mean and MAC as repre-
sentative values in two clusters, respectively, for demonstration of
feature distribution among patients. Unsupervised k-means clustering
on 30 AD patients based on time series features of PBMC tran-
scriptome modules and blood tests, with number of clusters (= k)
determined using silhouette criterion, identiﬁed three patient clusters
(Fig. 8b). We applied PCA to this data of time series features to capture
the patient distribution in a reduced dimension with the underlying
structure that are differential across patients (Fig. 8c), and evaluated
the intensity of the top PC1/PC2 contributing factors (Fig.8d). Cluster 1
(n = 2) was characterized by stably high levels of pModu07 (GO: neu-
trophil degranulation/Toll-like receptor signal), pModu09 (GO: neu-
trophil degranulation/interleukin signaling) and neutrophil (complete
blood counts-derived ratio: CBC) and a stably low level of lymphocyte
(CBC), whereas Cluster 2 ( n = 7) showed volatile trajectories of all of
those terms throughout the observation period, as observed by high
values of MAC with a medium level of mean. An unstably high white
blood cell (WBC) count was also observed. Meanwhile, Cluster 3
(n = 21) was characterized by relatively low levels of all of those terms
except for lymphocyte (CBC), which was relatively high in this patient
cluster (Fig. 8d, Fig. S15).
Remarkably, those patient clusters were found to show clinical
phenotypes associated with endotypic longitudinal features. Cluster 1
showed severe and stable symptoms, Cluster 2 showed severe and
unstable symptoms, and Cluster 3 showed mild symptoms (Fig. 8e).
Additionally, this patient grouping was found to be closely linked with
prescription status of systemic treatment (Fig. 8f). Cluster 2, which
Table 1 | Prediction variables extracted in regression models
Objective variables R2 Predictors Coef ﬁcient P-value Tissue PC1 top 5 genes Cell type speci ﬁcity
EASI (total) Training 0.61 Test 0.43 Lymphocyte −0.40 8.80E −04 Blood – Lymphocyte
Total IgE 0.25 0.042 Blood – –
Eosinophil 0.21 0.043 Blood – Eosinophil
sModu10 0.27 0.081 Skin S100A8, S100A9, KRT6C, SERPINB4,
S100A7
Keratinocyte
EASI (erythema) Training 0.63 Test 0.51 sModu08 0.22 2.60E −03 Skin NR4A1, FOSL1, FOSB, ATF3, NR4A2 Keratinocyte
Lymphocyte −0.14 0.041 Skin – Lymphocyte
sModu18 0.13 0.076 Blood CD163, C1QB, C1QC, THY1, MS4A7 Myeloids
pModu11 0.13 0.077 Skin CCR4, CNTNAP1, DUSP4, LMNA, PI16 Treg
Eosinophil 0.11 0.099 Blood – Eosinophil
EASI (papulation) Training 0.54 Test 0.33 Lymphocyte −0.39 7.50E −04 Blood – Lymphocyte
pModu06 −0.27 0.0029 Blood FCRL1, MS4A1, PAX5, CD22, LINC00926 B cell
Eosinophil 0.22 0.0091 Blood – Eosinophil
pModu01 0.24 0.015 Blood NELL2, LRRN3, OBSCN, CCR7, GRASP1 Naive CD4
ALT 0.19 0.017 Blood – –
BUN −0.17 0.03 Blood – –
sModu14 0.24 0.031 Skin MMP12, CCL18, IFI27, TYMP, COL6A6 VEC
sModu16 0.18 0.073 Skin PI15, GREM1, COL4A1, TNFAIP6, NNMT Fibroblast
Elastic net regression was applied to data including basic information, blood test, skin transcriptome modules and PBMC transcriptome modules. Adjustment was made forR2 in training set with the
number of prediction variables.N = 129 (Atopic dermatitis: AD = 115, healthy = 14).
sModu skin transcriptome module,pModu PBMC transcriptome module,ALT alanine transaminase,BUN blood urea nitrogen, VEC vascular endothelial cells.
Article https://doi.org/10.1038/s41467-023-41857-8
Nature Communications|         (2023) 14:6133 9

manifested severe and unstable symptoms, highly overlapped with the
patients who were under systemic therapy with an oral immunosup-
pressant (5/7 patient overlap), while Cluster 1 and Cluster 3 were
mostly managing the disease either with antihistamines only or with-
out systemic treatment.
The dynamics of EASI (total), top PC1/PC2 contributing factors, as
well as the treatment periods in representative patients are shown in
Fig. 8g. One possible logic for the observation of patient overlap
between disease severity/stabilityand systemic treatment is that only
severe patients are supposed to be candidates for systemic immuno-
suppressant therapy that leads to rapid symptom mitigation and glo-
bal transcriptome alterations
13, but could cause a ﬂare at the time of
drug cessation. Patients treated with immunosuppressants in this
study were all administered with the drug intermittently as instructed
by their dermatologists, considering their symptom improvement or
the risk of side effects. Accordingly, some patients experienced disease
ﬂare during washout periods. We thus note that systemic immuno-
suppressant therapy could partially contribute to instability of disease
severity trajectory as well as other personal time series features.
Discussion
With an increase of therapeutic options expected in the coming years,
(1) understanding heterogeneity in disease phenotypes and endotypes
and (2) patient stratiﬁcation into subgroups based on phenotypes or
endotypes, are the two urgent tasks for the development of persona-
lized medicine in AD. Phenotypic heterogeneity among AD patients,
which has been empirically recognized though not yet clearly deﬁned,
includes variability in skin manifestation and longitudinal disease
course. In this study, we sought to elucidate endotypic heterogeneity
in association with these two aspects of phenotype, aiming at pro-
viding clinically signiﬁcant and applicable insights in dermatology.
We pro ﬁled patients with transcriptome analysis on skin and
blood biospecimens, each re ﬂecting different aspects of disease
state; skin for primary pathology at the site of ongoing or probable
inﬂammation
10, and blood, a relatively homogeneous compartment,
for systemic regulation of inﬂammation42. Although previous studies
have reported patient stratiﬁcation in AD based on single tissue data
such as serum cytokine pro ﬁles43, whole blood transcriptomes 44,o r
skin barrier pro ﬁles of comorbidity-strati ﬁed patient groups (with/
without food allergy)45, there are few reports on clinically signi ﬁcant
endotypes regarding both skin and the circulatory system so far. He
et al. demonstrated that patient groups de ﬁned on the basis of dis-
ease severity have differential molecular proﬁles in both non-lesional
skin and serum 46. Indeed, clinical manifestations in AD should be
evaluated beyond the criterion of simple severity, given that several
speciﬁc detailed signs of eczema have long been recognized in AD
27
including erythema and papulation, two distinct skin manifestations
highlighted in our cross-sectional analysis. Exploring molecular
involvement in such speci ﬁc phenotypes using both skin and PBMC
data should provide deeper insights into the unique characteristics
of individual patients than in the case where the focus is on con-
ventional general severity or just the presence of disease (AD versus
healthy controls).
Our combinatorial approach of WGCNA and elastic net regres-
sion enabled us to ef ﬁciently and jointly analyze high dimensional
datasets of skin and PBMC transcriptomes. Our ﬁnding on skin
manifestation-dependent molecular proﬁles suggests that endotypes
in AD (i.e. biological subtypes that were de ﬁned based on tissue
Fig. 7 | Prediction performance of regression models on longitudinal dataset.
a Performance of elastic net regression models to predict general disease severity
(log2(EASI.total+1)). Models were trained with cross-sectional patient dataset and
tested on longitudinal dataset. Adjustment was made forR2 in training set with the
number of prediction variables.b Trajectories of observed and predicted disease
severity (log2(EASI.total+1)) in two representative patients both with successful
prediction outcome (left,r =0 . 8 1 ,p =2 . 4 E−3) and with unsuccessful prediction
outcome (right, r = −0.44, p = 0.20) assessed by two-sided Pearson correlation.
Source data are provided as a Source Data ﬁle.
Article https://doi.org/10.1038/s41467-023-41857-8
Nature Communications|         (2023) 14:6133 10

Fig. 8 | Time series features of disease severity, clinical lab and PBMC tran-
scriptome in each patient in association with history of systemic therapy.
a Schematic of extraction of time series features in 30 AD patients. b Silhouette
width plot for identifying the optimal number of patient clusters based on time
series features.c–f PCA on 30 AD patients using time series features of blood tests
and PBMC transcriptome modules. Color indicates patient clusters deﬁned by
k-means (c), the intensity of time series feature (upper; mean, lower; MAC) of 5
variables normalized among patients (d), time series features of clinical severity (e),
and history of internal medication (f). g Dynamics of EASI (total), pModu07,
pModu09, lymphocyte, neutrophil and WBC as well as period of internal medica-
tion in representative patients. MAC mean absolute change, pModu PBMC tran-
scriptome module, WBC white blood cell. Source data are provided as a Source
Data ﬁle.
Article https://doi.org/10.1038/s41467-023-41857-8
Nature Communications|         (2023) 14:6133 11

transcriptome analysis in our study) are closely associated with the
phenotypes of AD that were de ﬁned by visual evaluation of the skin.
More fundamentally, this observation supports the assumption that
the AD population comprises a variety of pathophysiological sub-
types. Our report demonstrates association between endotypes and
phenotypes with granularity beyond general clinical severity in AD.
Furthermore, we assessed heterogeneity in personal long-
itudinal features in PBMC transcriptome modules and blood tests in
association with clinical severity. We identiﬁed three patient clusters
based on longitudinal blood-derived signatures that were found to
be closely linked with disease course and medication history. Our
demonstration is the ﬁrst step of patient strati ﬁcation in the view of
longitudinal features in AD, serving as a signiﬁcant movement toward
the grand challenge of personalized medicine.
There were also biological ﬁndings in the longitudinal analysis.
Three top contributing factors for patient clustering was pModu07,
pModu09, and neutrophil count, all of which was signatures
reﬂecting innate immunity activity. This suggested that the
dynamics of innate immunity may be the major force for instability
in longitudinal disease course. As to the factors correlated with
disease severity in individual patients, in addition to serum TARC,
LDH and eosinophil counts, all of which are well-recognized bio-
markers in AD
47,n e w l yd e ﬁned PBMC transcriptome modules
including pModu01 (inferred cell speci ﬁcity: naive CD4, PC1 top
genes: NELL2, LRRN3, OBSCN, CCR7 and GRASP1) and pModu04
(inferred cell speci ﬁcity: Treg, PC1 top genes: MKI67, RRM2, TOP2A,
ASPM and MYBL2)w e r ei d e n t iﬁed as contributing factors in a per-
sonal disease course.
Although our study demonstrated integrative analysis of
transcriptome data both from primarily diseased tissue and from
circulatory system is advantageous for understanding patient
endotypes, such assessment could not be applied in routine clinical
examination especially in the longitudinal contexts, since acquiring
biospecimen other than blood requires invasive sampling. Our next
task is therefore, to identify representative biomarkers that can
predict system-level pathology in individual patients only by rou-
tine clinical examination.
There are some limitations in this study. First, the clinical
deﬁnition of skin phenotype manifestations is not totally objec-
tive. Scoring for severity of eczema was based on visual evaluation,
which is strongly dependent on the expertise and experience of
the dermatologists. The fact that most AD patients manifested
multiple signs of eczema including erythema and papules simul-
taneously, with blurred boundaries, makes this issue even more of
a problem. In the future, skin manifestations should be computa-
tionally and quantitatively evaluated, for example, through the
abundance of hemoglobin or pigmentation in the skin, as has been
investigated in some other skin disorders
48,49.S e c o n d ,o u rt r a n -
scriptome data is from bulk RNA-seq which yields mixed sig-
natures of different cell types in the tissue. Although we could
infer cell type speci ﬁcity for each molecular signature by decon-
volution taking advantage of external scRNA-seq data, the reso-
lution and accuracy is limited compared to the original scRNA-seq
data
50– 52. Other limitations in our study includes limited sample
size and population diversity, as is always the challenge in studies
on complex human diseases. Above all, the AD patients in our
cohort were enrolled in the single university hospital and can be
potentially characterized by speci ﬁc spectrum in disease severity.
Studies with extended sample size and diversity may illuminate
more profound heterogeneity in AD. Including non-lesional skin in
the analysis would also serve this purpose since non-lesional skin
could be a representation for con genital epidermal barrier func-
tion or immune regulation in pre-disease states. On the whole, our
study highlighted inter- and intra- patient heterogeneity in AD, and
demonstrated the promises of personalized AD treatment.
Methods
Study design
This study was approved by the Keio University School of Medicine
Ethics Committee (Approval Number 20150325, 20160225, 20160131
and 20160377) and the RIKEN Eth ics Committee (Approval Number
H28-24) and conducted according to all relevant requirements from
the Declaration of Helsinki. Written informed consent on sample col-
lection, data acquisition and usage, and publication was obtained from
all the participants. Participants received 5000 yen at one sampling of
biospecimen for compensation for discomfort or inconvenience.
Diagnosis of AD was made according to diagnostic criteria of Haniﬁn
and Rajka
53.
We enrolled 196 Japanese AD patients who visited Keio Uni-
versity hospital and 46 healthy controls for skin and blood sampling
study between December 2016 and February 2020 via information
posters and documents. Pregnant or breast-feeding women, patients
with episodes of lidocaine allergy, prilocaine allergy, or complica-
tions of bleeding disorders were excluded from recruitment. For
cross-sectional analysis, we extracted eligible sample population
based on the following criteria:(1) 20 years of age or older, (2) not
being under systemic therapy with anti-IL-4R α mAb nor JAK inhibi-
tors, (3) having undergone biopsy from the back for skin samples.
Accordingly, 188 AD patients and 45 healthy controls were extracted,
and after data quality control as described in RNA-seq and data
processing section as well as ﬁltering with missing values in blood
tests, 121 AD patients and 19 healthy controls were considered to be
eligible for regression analysis on PBMC and blood tests, and 115 AD
patients were considered to be eligible for regression analysis on all
of skin, PBMC and blood tests.
For longitudinal analysis, samples from 30 AD patients who were
enrolled in prospective observational study between December 2016
and September 2018 were analyzed. Time series dataset consisting of
PBMC transcriptome, laboratory blood tests and clinical severity score
from 30 AD patients on monthly basis up to a year (total 360 time
points), were extracted. After data quality control, 280 data were
considered to be eligible and used for analysis.
All the patients included in two analyses were treated according to
the Japanese guideline for atopic dermatitis
54, such as emollients,
topical corticosteroids and/or tacrolimus, oral antihistamines and
immunosuppressants
29. Note that the use of antihistamines was
recommended as an adjuvant therapy to anti-in ﬂammatory topical
therapy to reduce itchiness in the treatment policy proposed by the
Japanese guideline at the moment (i.e. 2016– 2020)
54.T h i sp o l i c yw a s
later modiﬁed to lower the grading of recommendation for the use of
antihistamines in the revised guideline in 2021 in response to the
increased recognition of uncertainty of its ef ﬁcacy on relief of
itchiness
55,56.
The Eczema Area and Severity Index (EASI) 27, assessed by two
board-certiﬁed dermatologist, was used for analysis as disease sever-
ity. Patient information including disease history, medication history
(within 4 weeks for the cross-sectional dataset and 13 months for the
longitudinal dataset), laboratory blood test data, and EASI were
extracted andﬁled from electronic medical records along with patient
questionnaires.
Sample collection
For skin RNA-seq, lesional skin biopsy samples (1 mm punch) were
obtained from the backs of the participants using Biopsy Punch (Kai
Medical) under local anesthesia with Emla creem (lidocaine 2.5% and
prilocaine 2.5%, Sato Pharmaceutical) which was administered 1 h
before the performance of biopsy. Samples were placed in RNAlater
(Life Technologies) overnight at 4 °C and stored at−80 °C until further
processing. For immunohistochemistry, skin biopsy samples (1 mm
punch) were taken from sites exhibiting similar skin conditions in close
proximity (within 5 mm region) to the skin samples for RNA-seq,
Article https://doi.org/10.1038/s41467-023-41857-8
Nature Communications|         (2023) 14:6133 12

immediately snap-frozen and stored at−80 °C until further processing.
For PBMC RNA-seq, PBMC were isolated from venous peripheral blood
by density gradient puri ﬁcation using Vacutainer CPT tubes (Becton
Dickinson) following the manufacturer ’s instructions, suspended in
RNAlater and stored at −80 °C until further processing.
Immunohistochemistry
We deﬁned the degree of erythema-skewness as erythema/(erythema +
papulation) using the EASI partial points, and randomly picked six
patients who have erythema-skewness ≧0.6 as erythema-skewed
patients and six patients who have erythema-skewness ≦0.4 as
papulation-skewed patients for histopathological analysis. Frozen skin
samples from the selected AD patients were thawed and immediately
embedded in O.C.T. compound (Sakura Finetech), snap-frozen and
stored at −80 °C until cryosectioning. Immunostaining was performed
using the streptavidin-biotin complex/alkaline phosphatase method as
previously described
57 with few modi ﬁcations. Brie ﬂy, 10- μm-thick
cryostat-cut tissue sections wereﬁxed for 5 min in ice-cold acetone and
rehydrated in phosphate-buffered saline with 0.1% Triton-X followed
by incubation with normal goat serum for 1 h. The sections were
incubated with the primary antibodies (Table S8) diluted in blocking
solution overnight at 4 °C, followed by a biotinylated secondary anti-
body (either anti-mouse or anti-rabbit according to the primary anti-
bodies, dilution: 1/200) and therea fter with a streptavidin-biotin
complex/alkaline phosphatase (Vectastain ABC-AP; Vector). Finally,
the sections were developed with alkaline phosphatase substrate
(ImmPACT Vector Red; Vector) and counterstained with hematoxylin.
The images were captured using a digital image acquisition and ana-
lysis system (BX43 microscope, DP27 digital camera, cellSens v3.3
Software; Olympus).
RNA-seq and data processing
For skin tissue RNA-seq, skin specimens were homogenized with
BioMasher (Nippi) in TRIzol Reagent (Thermo), and RNA was isolated
with Direct-Zol RNA Kit (ZYMO RESERCH). Library preparation was
carried out using NEBNext Ultra RNA Library Prep Kit (New England
Biolabs) following the manufacturer ’s instructions. For PBMC RNA-
seq, RNA was isolated using Maxwell 16 LEV simplyRNA Blood Kit and
Maxwell 16 Instrument (Promega) and library preparation were car-
ried out with SureSelect Strand-Speci ﬁc RNA Library Prep Kit (Agi-
lent). The libraries were pooled for skin tissue RNA-seq and PBMC
RNA-seq, respectively, and sequenced on HiSeq1500 or HiSeq2500
with bcl2fastq (Illumina) to obtain 15 – 20 million reads using the 50-
bp single-end read conﬁguration. Reads were aligned to the Ensembl
GRCh38 human genome assembly using STAR (2.5.2)
58 and feature
counts were performed with the R package Rsubread 59. R version
3.6.2 was used for all the following analysis in R language unless
speciﬁed otherwise. Genes were ﬁltered by both of the following
conditions: (1) expressed in more than 5% of the sample population,
(2) maximum reads across the population >8. Samples were ﬁltered
with the criteria of total read count > 5 million. Genes coding
hemoglobin proteins ( “HBA2”, “HBB”, “HBA1”) and ribosomal pro-
teins were removed. The batch effects from each dataset attributable
to difference in experimental periods or locations for sequencing
were adjusted by ComBat-seq
60 with R package sva. Differential gene
expression analysis and vst normalization were conducted using the
R package DESeq2
61. Since there is a chance where skin samples are
occupied by considerable volume ratio of pilosebaceous unit in 1 mm
punch biopsy, only biased by sampling regions, skin samples were
also ﬁltered by gene expression intensity of pilosebaceous unit-
related gene set. A cluster that showed extremely strong signature of
pilosebaceous unit-related genes in Uniform Manifold Approxima-
tion and Projection (UMAP)
62 as analyzed with R package umap, were
excluded. GO analysis and GSEA were performed with the R package
clusterProﬁler
63 and ReactomePA64.
Inference in ligand–receptor coupling
Since our datasets consist of bulk-derived samples, which represent
mixed signatures of any cell type present in the tissue, we evaluated
the degree of ligand – receptor coupling with a binary scoring
approach
32 and thereafter cell type speci ﬁcity for individual active
cytokines and receptors were inferred by using publicly available
datasets of cell type-speciﬁce x p r e s s i o n .
Ligand– receptor pairs that are classi ﬁed into in ﬂammatory
response were extracted from the list of cytokine – receptor interac-
tions in the KEGG pathway database (https://www.genome.jp/kegg/)
65.
Possible active cytokine– receptor pairs were de ﬁned as concurrent
presence of pairs of possible active cytokines and possible active
receptors. Considering the biological context for the differential reg-
ulation of cytokines and receptors
66 along with previously reported
approaches33, we used the different conditions for the de ﬁnitions of
possible active cytokines and possible active receptors. Possible active
cytokines were deﬁned by their expression > 0.5 in the value of vst
normalization which accounts for the top 14.2% of the overall popu-
lation, while possible active receptors were deﬁned by their expression
>0 in the value of vst normalization which accounts for the top 48.6%
of the overall population.
A total of 210 pairs of in ﬂammatory cytokine and receptor genes
were assessed in the skin and PBMC of each of AD patient and healthy
control. The active cytokine – receptor pairs were enumerated
according to classes deﬁned by the combination of a sender organ that
expressed a cytokine gene and a receiver organ that expressed a
cognate receptor. Comparison of the number of active connections
between cytokines and receptors between AD patients and healthy
controls were carried out by a non-parametric Brunner-Munzel rank
test
67 with R package lawstat68, taking into account the nature of the
data that showed non-normal and heteroscedastic distribution in two
patient groups. P values less than 0.05 were considered signiﬁcant.
For each of the cytokine and receptor genes, cell types respon-
sible for the cytokine/receptor gene expression were estimated by
referring to publicly available datasets (GSE147424; scRNA-seq of skin
tissue from AD patients and healthy controls
33,H u m a nP r o t e i nA t l a s
blood cell gene data; RNA-seq of 18 cell types sorted from human
peripheral blood34, for skin and PBMC RNA-seq data, respectively). R
package Seurat69 with R version 4.0.2 was used for scRNA-seq re-ana-
lysis. Reference datasets were standardized among cell types and
genes that were expressed at a level of z-score >2 were deemed as cell
type-speciﬁc genes. Note that expression of cytokine/receptor genes
were widely shared across multiple cell types in PBMC. Since con-
tribution of granulocytes may be negligible because of their small
fraction in PBMC compared to other cell types, we excluded neu-
trophil, eosinophil and basophil from the cell type annotation in this
analysis. Ligand – receptor connection were visualized using the R
package circlize
70.
Module detection and validation
Gene co-expression networks of skin and PBMC transcriptomes were
constructed from the vst normalized matrix of variance top 10,000
genes in respective datasets using the R package WGCNA
71.M o d u l e s
were generated following the procedures recommended by the pub-
lication author, including determination of the algorithm ’sh y p e r -
parameters. Soft-thresholding power ( β) was chosen as the lowest
power for which the scale-free topologyﬁt index reached 0.80 with the
minimum threshold of 6. As each module is composed of genes highly
correlated with each other, the intensity of overall expression of a
g i v e nm o d u l ei nap a t i e n tw a sr e p r e s e n t e da st h eﬁrst principal com-
ponent of expression of all the genes in the module. Hub genes were
deﬁned using the signed KME function and transcriptome networks
were visualized using the R package igraph
72. Module characterization
was performed based on both cell type speci ﬁcity and GO. Cell type
speciﬁcity in its expression was determined by referring to the same
Article https://doi.org/10.1038/s41467-023-41857-8
Nature Communications|         (2023) 14:6133 13

external dataset used in the previous section, i.e. either scRNA-seq
(skin) or sorted cell RNA-seq (PBMC). Because number of genes in the
PBMC modules was speciﬁcally expressed by granulocytes, we inclu-
ded neutrophil, eosinophil, and basophil for the cell type annotation in
this analysis. Note that the cell type frequency was not taken into
account for the size of the contribution to expression of each gene. GO
analysis were performed with the R package clusterProﬁler.
Regression analysis
Elastic net, a regularization and variable selection method that combines
the L1 and L2 penalties of the lasso and ridge methods37,w a sa p p l i e do n
cross-sectional datasets consisting of both skin and PBMC RNA-seq data
along with blood tests (AD patients:n = 115, healthy controls:n =1 4 ) t o
determine the strength of the relationship between disease phenotypes
and omics features using the R package glmnet
73. For each phenotype
deﬁned with clinical scores, samples were labeled with the degree of
speciﬁc skin conditions in continuou s values, and were split into a
training set (70%) and a testing set (30%). Models were built on the
training set with optimization of the regularization parameterλ which
determines how much shrinkage is used to train the model, through ten-
fold cross validation. Another hyperparameter ofα which determines
the ratio of L1 penalty to the combination of L1 and L2 penalties was set
to 0.5, intending to exploit both the sparse representation effect in the
lasso and the grouping effect in the ridge. Then the model with the
optimal parameters was applied to the test set to get the R
2 value to
evaluate how well the modelﬁtt ot h eo b s e r v e dd a t a .
For longitudinal data analysis, the model was trained on a total
cross-sectional dataset excluding 30 AD patients who are enrolled in
the longitudinal cohort, and tested on the longitudinal dataset from 30
AD patients. Prediction performance on the test set was evaluated with
R
2.C l o s e n e s so fﬁt in personalized trajectory was evaluated with the
Pearson correlation coefﬁcient.
Longitudinal data analysis
Time series data from blood tests, PBMC transcriptome modules and
clinical severity were proﬁled by patients in date order. By using the
Python (version 3.7.4) module Tsfresh 41, seven types of time series
features, i.e., mean, minimum, maximum, root mean square (RMS),
mean absolute change (MAC), approximate entropy, and complexity-
invariant distance (CID) were extracted in individual patients. The
values of time series features were standardized among patients. PCA
followed by unsupervised k-means clustering was conducted on
longitudinal features of PBMC transcriptome modules and blood tests
to identify patient clusters based on longitudinal endotypes.
Reporting summary
Further information on research design is available in the Nature
Portfolio Reporting Summary linked to this article.
Data availability
RNA-seq data generated in this study have been deposited in the
National Bioscience Database Center (NBDC) Human Database. Raw
data are available at the Japanese Genotype-phenotype Archive (JGA)
with accession codes JGAS000628 under controlled access for issue
on privacy in informed consent by participants which can be accessed
through application for hum0413 at the NBDC. The reference data
used in this study are available in the Gene Expression Omnibus
database under accession code GSE147424 and Human Protein Atlas
database with the title of “RNA HPA immune cell gene data ”.S o u r c e
data are provided with this paper.
Code availability
The source code to reproduce the presented results are available at the
online code repository ( https://github.com/aico007/AD_
heterogeneity_analysis).
References
1. Weidinger, S. & Novak, N. Atopic dermatitis. Lancet 387,
1109– 1122 (2016).
2. Yew, Y. W., Thyssen, J. P. & Silverberg, J. I. A systematic review and
meta-analysis of the regional and age-related differences in atopic
dermatitis clinical characteristics.J. Am. Acad. Dermatol. 80,
390– 401 (2019).
3. Czarnowicki, T., He, H., Krueger, J. G. & Guttman-Yassky, E. Atopic
dermatitis endotypes and implications for targeted therapeutics.J.
Allergy Clin. Immunol.143,1 – 11 (2019).
4. Bieber, T. Atopic dermatitis: an expanding therapeutic pipeline for a
complex disease.Nat. Rev. Drug Discov. 21,2 1– 40 (2022).
5. Simpson, E. L. et al. Two phase 3 trials of dupilumab versus placebo
in atopic dermatitis.N. Engl. J. Med 375, 2335– 2348 (2016).
6. Ruzicka, T. et al. Anti-interleuki n-31 receptor A antibody for atopic
dermatitis.N. Engl. J. Med. 376,8 2 6– 835 (2017).
7. Chun, P. I. F. & Lehman, H. Current and future monoclonal anti-
bodies in the treatment of atopic dermatitis.C l i n .R e v .A l l e r g y
Immunol. 59,2 0 8– 219 (2020).
8. Gittler, J. K. et al. Progressive activation of T(H)2/T(H)22 cytokines
and selective epidermal proteins characterizes acute and
chronic atopic dermatitis. J. Allergy Clin. Immunol. 130,
1344– 1354 (2012).
9. Suarez-Farinas, M. et al. Intrinsic atopic dermatitis shows similar
T(H)2 and higher T(H)17 immune activation compared with extrinsic
atopic dermatitis.J. Allergy Clin. Immun. 132,3 6 1– 370 (2013).
10. Tsoi, L. C. et al. Atopic dermatitis Is an IL-13-dominant disease with
greater molecular heterogeneity compared to psoriasis.J. Investig.
Dermatol. 139,1 4 8 0– 1489 (2019).
11. Khattri, S. et al. Ef ﬁcacy and safety of ustekinumab treatment in
adults with moderate-to-severe atopic dermatitis.Exp. Dermatol.
26,2 8– 35 (2017).
12. Guttman-Yassky, E. et al. Dupilumab progressively improves sys-
temic and cutaneous abnormalities in patients with atopic derma-
titis. J. Allergy Clin. Immunol. 143,1 5 5– 172 (2019).
13. Mobus, L. et al. Atopic dermatitis displays stable and dynamic skin
transcriptome signatures.J. Allergy Clin. Immunol. 147,2 1 3
– 223
(2021).
14. Pavel, A. B. et al. Oral Janus kinase/SYK inhibition (ASN002) sup-
presses inﬂammation and improves epidermal barrier markers in
patients with atopic dermatitis.J. Allergy Clin. Immunol. 144,
1011– 1024 (2019).
15. Kozawa, S. et al. The body-wide transcriptome landscape of disease
models. iScience 2,2 3 8– 268 (2018).
16. Priest, C. & Tontonoz, P. Inter-organ cross-talk in metabolic syn-
drome. Nat. Metab. 1, 1177– 1188 (2019).
17. Picollet-D ’hahan, N., Zuchowska, A., Lemeunier, I. & Le Gac, S.
Multiorgan-on-a-chip: a systemic approach to model and decipher
inter-organ communication.Trends Biotechnol.39,7 8 8– 810 (2021).
18. GTEx Consortium et al. Genetic effects on gene expression across
human tissues. Nature 550,2 0 4– 213 (2017).
19. Regev, A. et al. The human cell atlas. Elife 6,e 2 7 0 4 1( 2 0 1 7 ) .
20. Brunner, P. M. et al. Increasing c omorbidities suggest that atopic
dermatitis is a systemic disorder.J. Investig. Dermatol.137,
18– 25 (2017).
21. Oliveira, C. & Torres, T. More than skin deep: the systemic nature of
atopic dermatitis.Eur. J. Dermatol 29,2 5 0– 258 (2019).
22. Hu, Y. et al. Metabolic syndrome and skin diseases. Front. Endo-
crinol. 10,7 8 8( 2 0 1 9 ) .
23. Glickman, J. W. et al. Cross-sectional study of blood biomarkers of
patients with moderate to severe alopecia areata reveals systemic
immune and cardiovascular biomarker dysregulation.J. Am. Acad.
Dermatol. 84,3 7 0– 380 (2021).
24. Imai, Y., Kusakabe, M., Nagai, M., Yasuda, K. & Yamanishi, K.
Dupilumab effects on innate lymphoid cell and helper T Cell
Article https://doi.org/10.1038/s41467-023-41857-8
Nature Communications|         (2023) 14:6133 14

populations in patients with atopic dermatitis. JID Innov. 1,
100003 (2021).
25. Mack, M. R. et al. Blood natural killer cell deﬁciency reveals an
immunotherapy strategy for atopic dermatitis.Sci. Transl. Med. 12
eaay1005 (2020).
26. Saluzzo, S. et al. Delayed antir etroviral therapy in HIV-infected
individuals leads to irreversible depletion of skin- and mucosa-
resident memory T cells. Immunity 54, 2842– 2858 e2845 (2021).
27. Hani ﬁn, J. M. et al. The eczema area and severity index (EASI):
assessment of reliability in atopic dermatitis. EASI Evaluator Group.
Exp. Dermatol. 10,1 1– 18 (2001).
28. Mead, A. Review of the develop ment of multidimensional scaling
methods. J. R. Stat. Soc. Ser. D. (Statistician) 41,2 7– 39 (1992).
29. Yasuda-Sekiguchi, F. et al. Single nucleotide variations in genes
associated with innate immunity are enriched in Japanese adult
cases of face and neck type atopic dermatitis.J. Dermatol. Sci.101,
93– 100 (2021).
30. de Wijs, L. E. M. et al. Clinical and histopathological characterization
of paradoxical head and neck erythema in patients with atopic
dermatitis treated with dupilumab: a case series.Br. J. Dermatol.
183,7 4 5– 749 (2020).
31. Suarez-Farinas et al. RNA sequencing atopic dermatitis tran-
scriptome proﬁling provides insights into novel disease mechan-
isms with potential therapeutic implications.J. Allergy Clin. Immun.
135,1 2 1 8– 1227 (2015).
32. Armingol, E., Of ﬁc e r ,A . ,H a r i s m e n d y ,O .&L e w i s ,N .E .D e c i p h e r i n g
cell-cell interactions and communication from gene expression.
Nat. Rev. Genet. 22,7 1– 88 (2021).
33. He, H. L. et al. Single-cell transcriptome analysis of human skin
identiﬁes novel ﬁbroblast subpopulation and enrichment of
immune subsets in atopic dermatitis.J. Allergy Clin. Immun. 145,
1615– 1628 (2020).
34. Uhlen, M. et al. A genome-wide transcriptomic analysis of protein-
coding genes in human blood cells. Science 366,1 4 7 1( 2 0 1 9 ) .
35. Stuart, J. M., Segal, E., Koller, D. & Kim, S. K. A gene-coexpression
network for global discovery of conserved genetic modules.Sci-
ence 302,2 4 9– 255 (2003).
36. Geffeney, S. L. & Goodman, M. B. How we feel: ion channel part-
nerships that detect mechanical inputs and give rise to touch and
pain perception.Neuron 74,6 0 9– 619 (2012).
37. Zou, H. & Hastie, T. Regularization and variable selection via the
elastic net (vol B 67, pg 301, 2005). J .R .S t a t .S o c .B67,
768– 768 (2005).
38. Chovatiya, R. et al. Clinical phenotyping of atopic dermatitis
using combined itch and lesional severity: A prospective obser-
vational study. Ann. Allergy Asthma Immunol. 127,8 3– 90
e82 (2021).
39. Boguniewicz, M. et al. Expert perspectives on management of
moderate-to-severe atopic dermatitis: a multidisciplinary con-
sensus addressing currenta n de m e r g i n gt h e r a p i e s .J. Allergy Clin.
Immunol. Pract. 5,1 5 1 9– 1531 (2017).
4 0 . N i m ,H .T .e ta l .N o v e lm e t h o d so fincorporating time in longitudinal
multivariate analysis reveals hidden associations with disease
activity in systemic lupus erythematosus.Front. Immunol. 10,
1649 (2019).
4 1 . C h r i s t ,M . ,B r a u n ,N . ,N e u f f e r ,J .&K e m p a - L i e h r ,A .W .T i m es e r i e s
FeatuRe extraction on basis of scalable hypothesis tests (tsfresh - A
Python package).Neurocomputing307,7 2– 77 (2018).
42. Mohr, S. & Liew, C. C. The peripheral-blood transcriptome: new
insights into disease and risk assessment.Trends Mol. Med. 13,
422– 432 (2007).
43. Bakker, D. S. et al. Con ﬁrmation of multiple endotypes in atopic
dermatitis based on serum biomarkers.J. Allergy Clin. Immun.147,
189– 198 (2021).
44. Mobus, L. et al. Blood transcriptome pro ﬁling identiﬁes two candi-
date endotypes of atopic dermatitis.J. Allergy Clin. Immunol. 150,
385– 395 (2022).
4 5 . L e u n g ,D .Y .M .e ta l .T h en o n l e s i o n a ls k i ns u r f a c ed i s t i n g u i s h e s
atopic dermatitis with food allergy as a unique endotype.Sci.
Transl. Med. 11, eaav2685 (2019).
46. He, H. et al. Mild atopic dermatitis lacks systemic inﬂammation and
shows reduced nonlesional skin abnormalities.J. Allergy Clin.
Immun. 147,1 3 6 9– 1380 (2021).
47. Thijs, J. et al. Biomarkers for atopic dermatitis: a systematic review
and meta-analysis.Curr. Opin. Allergy Clin. Immunol.15,
453–
460 (2015).
48. Abdlaty, R. et al. Hyperspectral imaging and classi ﬁcation for
grading skin erythema.Front. Phys. 6,1 – 10 (2018).
49. Romano, R. A., Rosa, R. G. T., Salvio, A. G., Jo, J. A. & Kurachi,
C. Multispectral auto ﬂuorescence dermoscope for skin lesion
assessment. Photodiagnosis Photodyn Ther. 30,1 0 1 7 0 4
(2020).
50. Alkon, N. et al. Single-cell analysis reveals innate lymphoid cell
lineage inﬁdelity in atopic dermatitis.J. Allergy Clin. Immun. 149,
624– 639 (2022).
51. Reynolds, G. et al. Developmental cell programs are co-opted in
inﬂammatory skin disease.Science 371, 364 (2021).
52. Nakamizo, S. et al. Single-cell analysis of human skin identi ﬁes
CD14(+) type 3 dendritic cells co-producing IL1B and IL23A in
psoriasis.J. Exp. Med. 218, e20202345 (2021).
53. Hani ﬁn, J. M. & Rajka, G. Diagnostic features of atopic-dermatitis.
Acta Derm. Venereol. 60,4 4– 47 (1980).
54. Katoh, N. et al. Japanese guidelines for atopic dermatitis 2020.
Allergol. Int. 69,3 5 6– 369 (2020).
55. Saeki, H. et al. English version of clinical practice guidelines for the
management of atopic dermatitis 2021.J. Dermatol. 49,
e315– e375 (2022).
56. Matterne, U. et al. Oral H1 antihistamines as ‘add-on’ therapy to
topical treatment for eczema.Cochrane Database Syst. Rev.1,
CD012167 (2019).
5 7 . S c h l a p b a c h ,C . ,H a n n i ,T . ,Y a w a l k a r ,N .&H u n g e r ,R .E .E x p r e s s i o no f
the IL-23/Th17 pathway in lesions of hidradenitis suppurativa.J. Am.
Acad. Dermatol. 65,7 9 0– 798 (2011).
58. Dobin, A. et al. STAR: ultrafast universal RNA-seq aligner. Bioinfor-
matics 29,1 5– 21 (2013).
59. Liao, Y., Smyth, G. K. & Shi, W. The R package Rsubread is easier,
faster, cheaper and better for alignment and quantiﬁcation of RNA
sequencing reads.Nucleic Acids Res. 47, e47 (2019).
60. Zhang, Y., Parmigiani, G. & Johnson, W. E. ComBat-seq: batch effect
adjustment for RNA-seq count data.NAR Genom. Bioinform.2,
lqaa078 (2020).
61. Love, M. I., Huber, W. & Anders, S. Moderated estimation of fold
change and dispersion for RNA-seq data with DESeq2.Genome Biol.
15,5 5 0( 2 0 1 4 ) .
62. Yang, Y. et al. Dimensionality reduction by UMAP reinforces sample
heterogeneity analysis in bulk transcriptomic data.Cell Rep. 36,
109442 (2021).
6 3 . Y u ,G . ,W a n g ,L .G . ,H a n ,Y .&H e ,Q .Y .c l u s t e r P r oﬁler: an R package
for comparing biological themes among gene clusters. OMICS 16,
284– 287 (2012).
64. Yu, G. & He, Q. Y. ReactomePA: an R/Bioconductor package for
reactome pathway analysis and visualization.Mol. Biosyst. 12,
477– 479 (2016).
65. Ogata, H. et al. KEGG: kyoto encyclopedia of genes and genomes.
Nucleic Acids Res. 27,2 9– 34 (1999).
66. Cendrowski, J., Maminska, A. & Miaczynska, M. Endocytic regulation
of cytokine receptor signaling.Cytokine Growth Factor Rev.32,
63– 73 (2016).
Article https://doi.org/10.1038/s41467-023-41857-8
Nature Communications|         (2023) 14:6133 15

67. Brunner, E. & Munzel, U. The nonparametric Behrens-Fisher pro-
blem: Asymptotic theory and a small-sample approximation.Biom.
J. 42,1 7– 25 (2000).
6 8 . H u i ,W . ,G e l ,Y .R .&G a s t w i r t h ,J .L .l a w s t a t :A nRp a c k a g ef o rl a w ,
public policy and biostatistics.J. Stat. Softw. 28,1 – 26 (2008).
69. Hao, Y. et al. Integrated analysis of multimodal single-cell data.Cell
184,3 5 7 3– 3587 e3529 (2021).
7 0 . G u ,Z . ,G u ,L . ,E i l s ,R . ,S c h l e s n e r ,M .&B r o r s ,B .c i r c l i z eI m p l e m e n t s
and enhances circular visualization in R.Bioinformatics30,
2811– 2812 (2014).
71. Langfelder, P. & Horvath, S. WGCNA: an R package for weighted
correlation network analysis.BMC Bioinformatics9 (2008).
72. Csárdi, G. & Nepusz, T. The igraph software package for complex
network research.Complex Syst. 1695,1 – 9( 2 0 0 6 ) .
73. Friedman, J., Hastie, T. & Tibshirani, R. Regularization paths for
generalized linear models via coordinate descent.J. Stat. Softw.33,
1– 22 (2010).
Acknowledgements
We would like to sincerely thank all the participants involved in this
study. We thank H. Maeo, S. Shibata, R. Sato, M. Tanaka and E. Numazaki
for supporting biospecimen sampling. We thank R. Ohashi, A. Hananoe,
M. Otsuka, E. Okutsu, Y. Koseki, A. Sugimoto and T. Takemori for sup-
porting maintenance of the storage of human samples and data. We
t h a n kR .E d a h i r o ,Y .T o m o f u j i ,S .K o y a s u ,K .Y a m a m o t o ,K .F u j i o ,T .E n d o
and T. Ishikawa for helpful advice on analysis. This study was supported
by AMED (22ek0410079 and JP19ek0410046, awarded to H. Koseki;
JP21ek0410058 and JP18ek0410028, awarded to M.A.), JST
(JPMJIH1504, awarded to K.S. and H. Koseki) and Japan Society for the
Promotion of Science (JSPS) KAKENHI (18K16072 and 20K17333, awar-
d e dt oA . S . ) .T h ei m a g ei nF i g .1 is from TogoTV (© 2016 DBCLS TogoTV,
CC-BY-4.0 https://creativecommons.org/licenses/by/4.0/deed.en).
Author contributions
Study concept and design: H. Koseki, M.A., H. Kawasaki, K.S.; Acquisition
of clinical samples: H. Kawasaki, A.F.N., K.Y., K.T., S.T., M.A.; Data col-
lection: K.A., T.M., J.Y., A.K., O.O., H. Kawasaki, A.F.N., A.S.; Analysis and
interpretation of data: A.S., Y.O., E.K. J.S., S.N., T.N., Q.W.; Drafting of the
paper: A.S., Y.O., H. Koseki. All authors reviewed and approved theﬁnal
draft of the paper.
Competing interests
H. Koseki has received research funds (grants paid to his institution) from
Maruho and Kao. M.A. has received research support and funds (grants
paid to his institution) from Maruho, Ono, Torii, Sato and Taiho. H.
Kawasaki has received research funds (grants paid to his institution) from
Torii. The rest of the authors declare no competing interests.
Additional information
Supplementary informationThe online version contains
supplementary material available at
https://doi.org/10.1038/s41467-023-41857-8.
Correspondenceand requests for materials should be addressed to
Yukinori Okada, Masayuki Amagai or Haruhiko Koseki.
Peer review informationNature Communicationsthanks Thomas Bieber
and the other, anonymous, reviewer(s)for their contribution to the peer
review of this work. A peer review ﬁle is available.
Reprints and permissions informationis available at
http://www.nature.com/reprints
Publisher’s note Springer Nature remains neutral with regard to jur-
isdictional claims in published maps and institutional afﬁliations.
Open Access This article is licensed under a Creative Commons
Attribution 4.0 International License, which permits use, sharing,
adaptation, distribution and reproduction in any medium or format, as
long as you give appropriate credit to the original author(s) and the
source, provide a link to the Creative Commons license, and indicate if
changes were made. The images or other third party material in this
article are included in the article’s Creative Commons license, unless
indicated otherwise in a credit line to the material. If material is not
included in the article’s Creative Commons license and your intended
use is not permitted by statutory regulation or exceeds the permitted
use, you will need to obtain permission directly from the copyright
holder. To view a copy of this license, visithttp://creativecommons.org/
licenses/by/4.0/.
© The Author(s) 2023
1RIKEN Center for Integrative Medical Sciences, Yokohama, Japan.2Department of Dermatology, Keio University School of Medicine, Tokyo, Japan.3Advanced
Data Science Project, RIKEN Information R&D and Strategy Headquarters, Tokyo, Japan.4Department of Statistical Genetics, Osaka University Graduate
School of Medicine, Osaka, Japan. 5Department of Genome Informatics, Graduate School of Medicine, The University of Tokyo, Tokyo, Japan.6Artiﬁcial
Intelligence Medicine, Graduate School of Medicine, Chiba University, Chiba, Japan.7Kazusa DNA Research Institute, Chiba, Japan.8Department of Extended
Intelligence for Medicine, Keio University School of Medicine, Tokyo, Japan.9Cellular and Molecular Medicine, Advanced Research Departments, Graduate
School of Medicine, Chiba University, Chiba, Japan. e-mail: yuki-okada@m.u-tokyo.ac.jp; amagai@keio.jp; haruhiko.koseki@riken.jp
Article https://doi.org/10.1038/s41467-023-41857-8
Nature Communications|         (2023) 14:6133 16