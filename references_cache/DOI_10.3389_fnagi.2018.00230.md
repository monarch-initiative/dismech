---
reference_id: DOI:10.3389/fnagi.2018.00230
title: Clustering Analysis of FDG-PET Imaging in Primary Progressive Aphasia
authors:
- Jordi A. Matias-Guiu
- Josefa Díaz-Álvarez
- José Luis Ayala
- José Luis Risco-Martín
- Teresa Moreno-Ramos
- Vanesa Pytel
- Jorge Matias-Guiu
- José Luis Carreras
- María Nieves Cabrera-Martín
journal: Frontiers in Aging Neuroscience
year: '2018'
doi: 10.3389/fnagi.2018.00230
content_type: full_text_pdf
full_text_attempted: true
full_text_provider: openalex
full_text_url: "https://www.frontiersin.org/articles/10.3389/fnagi.2018.00230/pdf"
oa_status: gold
license: cc-by
local_pdf_path: files/DOI_10.3389_fnagi.2018.00230.pdf
---

# Clustering Analysis of FDG-PET Imaging in Primary Progressive Aphasia
**Authors:** Jordi A. Matias-Guiu, Josefa Díaz-Álvarez, José Luis Ayala, José Luis Risco-Martín, Teresa Moreno-Ramos, Vanesa Pytel, Jorge Matias-Guiu, José Luis Carreras, María Nieves Cabrera-Martín
**Journal:** Frontiers in Aging Neuroscience (2018)
**DOI:** [10.3389/fnagi.2018.00230](https://doi.org/10.3389/fnagi.2018.00230)

## Content

ORIGINAL RESEARCH
published: 31 July 2018
doi: 10.3389/fnagi.2018.00230
Frontiers in Aging Neuroscience | www.frontiersin.org 1 July 2018 | Volume 10 | Article 230
Edited by:
Changiz Geula,
Northwestern University, United States
Reviewed by:
David Bergeron,
Université de Montréal, Canada
Daniel Llano,
University of Illinois at
Urbana-Champaign, United States
Hidenao Fukuyama,
Kyoto University, Japan
*Correspondence:
Jordi A. Matias-Guiu
jordimatiasguiu@hotmail.com
Received: 10 April 2018
Accepted: 11 July 2018
Published: 31 July 2018
Citation:
Matias-Guiu JA, Díaz-Álvarez J,
Ayala JL, Risco-Martín JL,
Moreno-Ramos T , Pytel V ,
Matias-Guiu J, Carreras JL and
Cabrera-Martín MN (2018) Clustering
Analysis of FDG-PET Imaging in
Primary Progressive Aphasia.
Front. Aging Neurosci. 10:230.
doi: 10.3389/fnagi.2018.00230
Clustering Analysis of FDG-PET
Imaging in Primary Progressive
Aphasia
Jordi A. Matias-Guiu 1*, Josefa Díaz-Álvarez 2, José Luis Ayala 3, José Luis Risco-Martín 3,
Teresa Moreno-Ramos 1, Vanesa Pytel 1, Jorge Matias-Guiu 1, José Luis Carreras 4 and
María Nieves Cabrera-Martín 4
1 Department of Neurology, Hospital Clinico San Carlos, San C arlos Research Health Institute (IdISSC), Universidad
Complutense, Madrid, Spain, 2 Department of Computer Architecture and Communications, C entro Universitario de Mérida,
Universidad de Extremadura, Mérida, Spain, 3 Department of Computer Architecture and Automation, Unive rsidad
Complutense, Madrid, Spain, 4 Department of Nuclear Medicine, Hospital Clinico San Carlo s, San Carlos Research Health
Institute (IdISSC), Universidad Complutense, Madrid, Spain
Background: Primary progressive aphasia (PPA) is a clinical syndrome ch aracterized by
the neurodegeneration of language brain systems. Three mai n clinical forms (non-ﬂuent,
semantic, and logopenic PPA) have been recognized, but applicability of the classiﬁcation
and the capacity to predict the underlying pathology is cont roversial. We aimed to study
FDG-PET imaging data in a large consecutive case series of pa tients with PPA to cluster
them into different subtypes according to regional brain me tabolism.
Methods: 122 FDG-PET imaging studies belonging to 91 PPA patients and 28 healthy
controls were included. We developed a hierarchical agglom erative cluster analysis
with Ward’ s linkage method, an unsupervised clustering alg orithm. We conducted
voxel-based brain mapping analysis to evaluate the pattern s of hypometabolism of each
identiﬁed cluster.
Results: Cluster analysis conﬁrmed the three current PPA variants, b ut the optimal
number of clusters according to Davies-Bouldin index was 6 s ubtypes of PPA. This
classiﬁcation resulted from splitting non-ﬂuent variant into three subtypes, while logopenic
PPA was split into two subtypes. Voxel-brain mapping analys is displayed different
patterns of hypometabolism for each PPA group. New subtypes also showed a different
clinical course and were predictive of amyloid imaging resu lts.
Conclusion: Our study found that there are more than the three already rec ognized
subtypes of PPA. These new subtypes were more predictive of c linical course and
showed different neuroimaging patterns. Our results suppo rt the usefulness of FDG-PET
in evaluating PPA, and the applicability of computational m ethods in the analysis of brain
metabolism for improving the classiﬁcation of neurodegene rative disorders.
Keywords: primary progressive aphasia, positron emission to mography, ﬂuorodeoxyglucose, brain metabolism,
clustering analysis, frontotemporal dementia, Alzheimer’s disease, unsupervised machine learning

Matias-Guiu et al. Clustering Analysis of PPA
1. INTRODUCTION
Primary progressive aphasia (PPA) is a clinical syndrome
characterized by neurodegeneration of language brain syst ems
(
Mesulam et al., 2014 ). It may be the onset of several
neurodegenerative disorders, including tauopathies, TDP- 43
proteinopathies, and Alzheimer’s disease (AD). Clinically,
current classiﬁcation distinguishes three main variants: non-
ﬂuent or agrammatic, semantic, and logopenic. Non-ﬂuent PPA
is associated with tauopathies, such as progressive supranucl ear
palsy, but also TDP-43 proteinopathies. The semantic variant
is closely associated with TDP-43 type C pathology, and the
logopenic variant may be the onset of AD in approximately 80–
90 % of cases (
Marshall et al., 2018 ). This current classiﬁcation
into three clinical variants has been a milestone in PPA rese arch,
because it has improved the clinical-pathological correlati on
(Matias-Guiu and Garcia-Ramos, 2013 ). However, prediction
of the underlying pathology using clinical features is still
incomplete, and even the usefulness of the current classiﬁca tion
is a matter of debate.
In this regard, some studies have found a large percentage of
patients not fulﬁlling the diagnostic criteria for a speciﬁc subtype,
especially the logopenic variant (
Sajjadi et al., 2012; Mesulam
and Weintraub, 2014; Wicklund et al., 2014 ). Furthermore,
other studies have suggested that apraxia of speech should be
separated from agrammatic/non-ﬂuent aphasia (
Josephs et al.,
2012) and have proposed alternative ways to categorize subtypes
of PPA (Botha et al., 2015 ). Because several pathological entities
have been associated with PPA (diﬀerent tauopathies, AD, and
three subtypes of TDP-43 proteinopathies) (
Harris et al., 2013 ),
clinical diagnosis should advance in order to improve the
prediction of the underlying pathology in each individual patient.
In addition, PPA patients may develop a second syndrome during
the clinical course, such as atypical parkinsonian syndromes ,
behavioral symptoms like in behavioral variant frontotempor al
dementia, dementia of Alzheimer’s type, etc. (
Rogalski and
Mesulam, 2009; Matias-Guiu et al., 2015a ). However, despite the
eﬀorts to improve cognitive and linguistic assessment of patie nts
and their classiﬁcation, the diagnosis of PPA is still chall enging,
and the existence of two, three or more clinical variants is
controversial (
V andenberghe, 2016).
Neurodegenerative diseases are determined by a relatively
speciﬁc predilection of each disease for certain brain region s
and networks ( Cummings, 2003; Leyton et al., 2016 ). 18F-
Fluorodeoxyglucose positron emission tomography (FDG-PET)
is considered a useful tool in the evaluation of patients with
neurodegenerative disorders and, speciﬁcally, in PPA (
Matias-
Guiu et al., 2015b, 2017a ). In fact, FDG-PET shows synaptic
dysfunction and neurodegeneration and, hence, is a reliabl e
biomarker, since it depicts speciﬁc brain regions impaired in each
patient.
We hypothesized that performing clustering analyses of
regional brain metabolism could allow an improvement in the
classiﬁcation of PPA patients. Thus, we aimed to study FDG-
PET imaging data of a large consecutive case series of patient s
with PPA using unsupervised clustering algorithms in order t o
ﬁnd out the optimal classiﬁcation groups. We aimed to verify th e
standard three-groups classiﬁcation of PPA types and, then, t o
discover subtype representations of the disease that could deri ve
into diﬀerent clinical course.
2. METHODS
2.1. Participants
This study involved 150 FDG-PET imaging studies belonging
to 91 patients with PPA (31 of them were scanned a second
time during the follow-up, making a total of 122 scans) and 28
healthy controls (all of whom were scanned once). Participan ts
were recruited consecutively in our center between Novembe r
2011 and May 2017, and they were followed-up until March
2018. Three cases with crossed aphasia (i.e., those patients w ith
predominant right-hemisphere hypometabolism) were excluded.
All patients met the current consensus criteria for PPA (
Gorno-
Tempini et al., 2011 ) and they were classiﬁed into the three
clinical variants according to the diagnostic criteria (cli nical and
neuroimaging supported) and follow-up. Thus, clinical diagnosis
of PPA variant was based on more than the initial assessment t o
avoid the existence of undetermined cases or the overdiagno sis
of certain variants according to the current consensus crite ria
(Sajjadi et al., 2012; Matias-Guiu et al., 2014 )
All participants underwent a detailed neurological and
neuropsychological assessment, together with FDG-PET.
Language assessment was performed following current
recommendations for PPA (
Gorno-Tempini et al., 2011 ),
and has been described elsewhere ( Matias-Guiu et al., 2015a;
Matías-Guiu et al., 2017b ). Amyloid imaging was available
in 43 patients. PPA patients were followed every 6 months
approximately, with a mean time of follow-up of 29.9 ± 17.3
months from FDG-PET imaging until the end of the follow-up or
the end of the study. During follow-up, progressive supranucle ar
palsy, corticobasal syndrome, and amyotrophic lateral sclerosi s
were deﬁned according to the diagnostic criteria for “probabl e”;
behavioral syndrome was deﬁned as the development of
symptoms suggestive of the behavioral variant of frontotempo ral
dementia, such as disinhibition, dietary changes, empathy l oss,
etc. impacting in daily living with or without dementia; and
dementia was deﬁned as the impairment in daily-living activit ies
due to other deﬁcits beyond language and with no signs or
symptoms suggestive of another alternative disorder (
Hauw
et al., 1994; Brooks et al., 2000; Armstrong et al., 2013 ). Healthy
controls were recruited from the Department of Neurology
among patients’ spouses or healthy volunteers. Healthy contr ols
were matched to the PPA group by age and gender, underwent
a comprehensive neuropsychological examination to exclude
cognitive deﬁcits, and neurological diseases and suggestiv e
symptoms were conﬁdently ruled out. The Institutional Research
Ethics Committee from our center approved the research
protocol.
2.2. FDG-PET Images Acquisition and
Preprocessing
PET images were acquired following European
guidelines (
V arrone et al., 2009 ). Images were obtained in a
Siemens Biograph True Point PET-CT scanner that integrates
Frontiers in Aging Neuroscience | www.frontiersin.org 2 July 2018 | Volume 10 | Article 230

Matias-Guiu et al. Clustering Analysis of PPA
FIGURE 1 | Distribution of patients within each cluster. X-axis repre sents the number of clusters, while in the Y -axis we show the n umber of patients assigned to each
cluster. The different colors of the bars indicate the clini cal PPA diagnosis for each patient within the cluster (1 non- ﬂuent/agrammatic, 2 semantic, 3 logopenic) and
healthy controls.
TABLE 1 | Distribution of patients per cluster and clinical PPA diagn osis for Linkage.
4 Clusters
PPA K0 K1 K2 K3
1 46 0 0 0
2 15 0 0 0
3 2 37 22 0
HC 2 0 0 26
5 Clusters
PPA K0 K1 K2 K3 K4
1 22 0 24 0 0
2 13 0 0 0 0
3 2 37 0 22 0
HC 0 0 2 0 26
6 Clusters
PPA K0 K1 K2 K3 K4 K5
1 22 0 24 0 0 0
2 0 0 0 15 0 0
3 2 37 0 0 22 0
HC 0 0 2 0 0 26
7 Clusters
PPA K0 K1 K2 K3 K4 K5 K6
1 22 0 24 0 0 0 0
2 0 0 0 15 0 0 0
3 2 37 0 0 22 0 0
HC 0 0 2 0 0 14 12
8 Clusters
PPA K0 K1 K2 K3 K4 K5 K6 K7
1 16 0 24 0 0 6 0 0
2 0 0 0 15 0 0 0 0
3 1 37 0 0 22 1 0 0
HC 0 0 2 0 0 14 12 0
The number of patients assigned to each cluster are shown, and their pre vious clinical PPA diagnosis is represented by the column labeled PPA. V alues 1, 2, and 3 in the ﬁrst column
correspond to non-ﬂuent/agrammatic, semantic and logopenic PPA, respectively, whereas HC represents healthy controls. Kn speciﬁes the number of clusters, where n = 0,1, .., N and
N is a value between 4 and 8.
Frontiers in Aging Neuroscience | www.frontiersin.org 3 July 2018 | Volume 10 | Article 230

Matias-Guiu et al. Clustering Analysis of PPA
a 6-detector CT with a late-generation PET using lutetium
oxyorthosilicate crystals. Patients fasted for at least 6 h before
the scan. 18F-FDG (185 MBq) was administered intravenously
30 min before acquisition of images. During this period of
time, patients remained at sensory rest. CT scan parameters
were: kVp/eﬀective mAs/rotation: 130/40/1; slice thickness : 3
mm; reconstruction interval: 1.5 mm; and pitch: 0.75. For PET
acquisition, one bed position was obtained, and the acquisit ion
time was 10 min.
Images were preprocessed using Statistical Parametric
Mapping 8 software (https://www.ﬁl.ion.ucl.ac.uk/spm/). They
were realigned, and normalized to the Montreal Neurological
Institute standard space using a speciﬁc FDG-PET template
for cognitive disorders (
Della Rosa et al., 2014 ). Global
mean normalization was performed individually. Marsbar
software was used to perform a region of interest analysis
of 116 brain areas of the Automatic Anatomical Labeling
atlas belonging to the whole brain. Thus, mean uptake
values were obtained for each participant in 116 regions of
interest.
2.3. Data Analysis
Clustering analysis (
Hennig et al., 2015 ) is one of the most
frequent algorithms for processing data. It is based on the
idea of distance and similarity among the attributes of the
samples. Recently, several types of clustering algorithms have
FIGURE 2 | Dendrogram from the classiﬁcation with Linkage and the criterion function Davies-Bouldin. 4 clusters.
FIGURE 3 | Dendrogram from the classiﬁcation with Linkage and the criterion function Davies-Bouldin. 8 clusters.
Frontiers in Aging Neuroscience | www.frontiersin.org 4 July 2018 | Volume 10 | Article 230

Matias-Guiu et al. Clustering Analysis of PPA
been developed: hierarchical clustering, partitional clust ering,
model-based clustering, grid-based clustering and densit y-
base clustering. Each one applies diﬀerent optimization
methods. In this study, we applied Agglomerative Hierarchica l
Clustering (HCA) as unsupervised learning algorithm (
Everitt
et al., 2011 ), particularly the Ward Linkage (Ward, 1963 )
algorithm.
HCA belongs to the special case of overlapping clustering
algorithms. These iterative bottom-up classiﬁcation meth ods
create a sequence of partitions, which satisfy that C = ⋃ n
i=1 Ci,
where Ci with i = 1, 2, ..n are diﬀerent partitions. The lowest level
partitions are included into the highest level partitions.
The process starts clustering two closer observations and
a new cluster is merged in every step. The process builds
a tree structure known as dendrogram, and continues until
all observations are clustered. The root class contains all the
observations. There are several aggregation methods and, i n this
work, we have selected the Ward’s Linkage method.
This algorithm does not guarantee ﬁnding the optimal
solution, but it has demonstrated to provide a good behavior.
Moreover, although the computational cost associated with
Hierarchical Clustering is higher than partitional Clusteri ng, the
dendrogram obtained allows us to explore diﬀerent partitions,
simply by changing the cut-oﬀ level as shown in the dendrogram
representation. In this way, the problem of not knowing
the k value in advance, like for instance in the k-means
algorithm (
Mathworks, 2008 ), is solved. As a result, this
clustering technique produces good clustering solutions (Jain and
Dubes, 1988).
Ward’s method works in terms of dissimilarities and it is based
on the minimum variance method and the Error Sum of Squares
(SSE). Ward’s method estimates the proximity between cluster s
through their centroids. It measures the proximity between t wo
clusters according to the increase of the SSE. Ward’s methodtries
to minimize the sum of the squared distances for each point into
the cluster, with respect to each cluster’s centroid.
Dissimilarities between a cluster with i and j as components,
and the rest of the objects, are computed following
the Lance-Willians dissimilarity formula , as shown in
Equation (1).
d(i
⋃
j, k) = α id(i, k) + α jd(j, k) + β d(j, k) + γ |d(i, k) − d(j, k)|
(1)
where i corresponds to the components in the cluster i, α i, α j,
β , and γ are the agglomerative criterion. For the Ward’s method
α i = |i|+|k|
|i|+|j|+|k| , β = |k|
|i|+|j|+|k| and γ = 0. The coordinates of the
cluster center, comprising i and j, are computed as g = |i|gi+|j|gj
|i|+|j| ,
which represent a vector in the space of the set of attributes.
|i||j|
|i|+|j| ||gi − gj||2 computes the dissimilarity between cluster with
centers gi and gj.
The following analysis was carried out using both Matlab
and Weka software. Initially, we evaluated the possibility of
ﬁnding 4, 5, 6, 7, and 8 clusters in the acquired data.
This process was performed in Matlab with the evalclusters
function and the mentioned unsupervised learning algorithm,
using the Davies-Bouldin criterion (
Davies and Bouldin, 1979 ).
Evalclusters function returned 8 as the optimal number of
FIGURE 4 | Davies Bouldin values for the number of cluster explored (4, 5, 6, 7, and 8). Lower values of this metric mean a better ﬁtting of the sample data to the
number of clusters.
Frontiers in Aging Neuroscience | www.frontiersin.org 5 July 2018 | Volume 10 | Article 230

Matias-Guiu et al. Clustering Analysis of PPA
clusters. However, we decided to launch tests with clusters
from 4 to 8, in order to analyze how patients were split into
subgroups.
Davies-Bouldin (DB) index measures the similarity of clusters,
and how compact a cluster is. DB depends both on the
data and the algorithm. A minimum value represents a more
compact cluster and therefore the clustering performed has
higher homogeneity. DB is computed as R = 1
n
∑ n
i=1 Ri, where
Ri is the maximum value for Rij = si+sj
dij
with i ̸=j and dij is the
distance between the centers of clusters i, j.
After this set of experiments, the next task was to apply the
Ward Linkage method according to the number of potential
clusters to explore, and in order to obtain a classiﬁcation of
patients for this number of clusters. This process was carried out
using the Weka software. As a result, patients were assigned to
diﬀerent clusters in accordance with the classiﬁcation meth od
and the data similarity.
2.4. Brain Metabolism Analysis of Clusters
FDG-PET images of each obtained cluster were compared to an
additional control group of 32 healthy subjects. Prior to statistical
analysis, images had been spatially normalized and smoothed
at 12 mm full-width at half maximum. Statistical Parametric
Mapping version 8 was used for preprocessing and analysis. A
two-sample T test was conducted to compare between groups,
using age and gender as covariates. Statistical signiﬁcance was set
at p < 0.05 using family-wise error correction at cluster level. Al l
voxel-based mapping analyses and statistics are shown in Table
S1 (Supplementary Material).
3. RESUL TS
3.1. Description of the Sample
The sample included 122 FDG-PET imaging studies from 91
patients with PPA: 46 with the non-ﬂuent, 15 with semantic,
and 61 with logopenic variants. The mean age of the PPA
group was 73.48 ± 7.79, and 63 (51.6%) were women. Mean
age of onset of symptoms was 70.65 ± 10.67 years. In the
PPA group, at the moment of FDG-PET imaging, Mini-
Mental State Examination score was 23 [interquartile range
14–27] and Addenbrooke’s Cognitive Examination was 51.22
± 23.4. Mean Functional Activities Questionnaire score was
4 [0–12].
FIGURE 5 | Clustering in four groups. Voxel-based brain mapping analy sis showing regions with lower metabolism in the group k1 (lo gopenic PPA subtype 1, in red)
and the group k2 (logopenic PPA subtype 2, in green) in compar ison to healthy controls.
Frontiers in Aging Neuroscience | www.frontiersin.org 6 July 2018 | Volume 10 | Article 230

Matias-Guiu et al. Clustering Analysis of PPA
3.2. Cluster Analysis General Results
Clustering results are represented in Figure 1, where a graph
for each number of clusters is drawn. For a better explanation
of the results, Table 1 details the distribution of patients per
cluster.
Figure 2 shows the dendrogram from the 4-cluster scenario,
while Figure 3 shows the dendrogram for the corresponding
8-cluster scenario.
The application of the Davies-Bouldin criterion function
returned 8 as the optimal number of clusters, with an index val ue
of 2.079, as shown in Figure 4. The ﬁgure also shows how 4
clusters could be the second best option, while 5, 6, and 7 clus ters
were not selected by this quality metric.
3.3. Clinical and Neuroimaging
Characteristics for 4 Clusters
The following groups were found when classifying for 4
clusters. The ﬁrst group k0 included 65 patients, and mainly
comprised patients with non-ﬂuent and semantic PPA. The
second (k1, n = 37) and third groups (k2, n = 22) were mostly
patients with logopenic PPA, while k3 ( n = 26) were healthy
controls.
In comparison to healthy controls, k0 showed lower
metabolism mainly in the left frontal lobe and the anterior
temporal lobe. k1 showed hypometabolism in two main clusters:
the ﬁrst one involving the left supramarginal, superior, midd le
and inferior temporal gyri and the inferior parietal lobule; a nd
the second one including left middle and inferior frontal gyri and
precentral gyrus. k2 showed lower metabolism in a main cluster
in the left hemisphere involving the middle, superior, and inferior
temporal gyri, as well as fusiform, angular, and parahippocampal
gyri. There was an additional cluster in the right temporal lob e
and the right angular gyrus ( Figure 5).
When available, amyloid biomarkers were positive in all cases
classiﬁed into k1 and k2 clusters (18/18 and 15/15, respectiv ely)
and negative in 90% of cases classiﬁed into the k0 cluster (1/10
positive).
During follow-up, k0 evolved mainly to progressive
supranuclear palsy ( n = 18, 27.7 %) and behavioral symptoms
(n = 13, 20 %). Patients within the k1 group evolved to global
dementia in 26 (70.3 %). In k2, 15 (68.2 %) progressed also to
dementia.
3.4. Clinical and Neuroimaging
Characteristics for 5 and 6 Clusters
In this analysis, groups mainly involving logopenic PPA and
healthy controls remained unchanged. Conversely, the grou p
including non-ﬂuent and semantic variants was divided in tw o
(in the case of 5 clusters classiﬁcation) and three (in 6 clust ers)
groups: k0 ( n = 24), k2 ( n = 26), and k3 ( n = 15). k0 and k2
were patients with non-ﬂuent PPA, while k3 were all patients with
semantic PPA.
FIGURE 6 | Clustering in six groups. Voxel-based brain mapping analys is showing regions with lower metabolism in the group k0 (non -ﬂuent PPA subtype 1, in blue)
and the group k2 (non-ﬂuent PPA subtype 2, in yellow) in compar ison to healthy controls.
Frontiers in Aging Neuroscience | www.frontiersin.org 7 July 2018 | Volume 10 | Article 230

Matias-Guiu et al. Clustering Analysis of PPA
In comparison to healthy controls, k0 showed lower
metabolism in the left frontal lobe (superior, middle, media l and
inferior frontal gyru, cingulate), insula, caudate and ext ended
also to left inferior parietal lobule and middle temporal gyru s.
k2 showed lower metabolism in left frontal lobe (precentral,
cingulate, middle, medial, and inferior frontal gyri) and a lso in
the right frontal lobe (medial, middle and superior frontal, and
cingulate gyri) ( Figure 6). In turn, k3 showed lower metabolism
in two main clusters in bilateral anterior temporal lobe (especially
in the left side), and extended to some regions of the frontal lobe
(Figure 7).
Amyloid imaging was negative in all cases in k0 ( n = 3) and
k3 (n = 6), and positive in one case in k2.
During follow-up, patients in the k0 group developed
symptoms of progressive supranuclear palsy ( n = 6, 25.0 %),
global dementia ( n = 6, 25 %), and behavioral syndrome ( n = 4,
16.7 %). In k2, most patients evolved to progressive supranuclea r
palsy ( n = 12, 46.2 %). In k3, 9 cases (60 %) developed a
behavioral syndrome.
3.5. Clinical and Neuroimaging
Characteristics for 7 and 8 Clusters
When 7-8 clusters were considered, the former k0 group in
6 clusters was further subdivided into two subgroups (k0, n
= 17; and k5, n = 7). Besides, healthy controls were also
subdivided in two subgroups (k6, n = 14; and k7, n = 12). The
subdivision of healthy controls in two groups probably reﬂect s
gender diﬀerences in regional brain metabolism, because 100% of
cases in k6 and k7 were women and men, respectively(
Hu et al.,
2013).
In comparison to the healthy control group, k0 showed lower
metabolism in the left frontal lobe (superior, middle and inf erior
frontal gyri, cingulate, insula), inferior and temporal gyr i, left
caudate, left inferior parietal lobule, and left rectal gyru s.
Furthermore, k5 showed lower metabolism in a large cluster
involving inferior, middle and superior frontal gyri, anter ior
cingulate, insula and orbital gyri in the left hemisphere. k5
also showed additional regions of hypometabolism including le ft
inferior parietal lobule and angular gyri, left inferior and middle
FIGURE 7 | Clustering in six or eight groups. Voxel-based brain mappin g analysis showing regions with lower metabolism in the grou p k3 (semantic PPA, in green) in
comparison to healthy controls.
Frontiers in Aging Neuroscience | www.frontiersin.org 8 July 2018 | Volume 10 | Article 230

Matias-Guiu et al. Clustering Analysis of PPA
temporal gyri, and some small clusters in right middle fronta l
gyrus, left thalamus, and left medial frontal gyrus ( Figure 8).
During follow-up, k5 evolved to dementia with ( n = 4,
57.1 %) or without ( n = 2, 28.6 %) prominent behavioral
symptoms. k0 showed a more heterogeneous clinical course: 6
(35.3 %) developed progressive supranuclear palsy) and 4 (23.5
%) dementia with no other signs. The diﬀerent clinical courses of
each cluster are summarized in Figure 9.
4. DISCUSSION
Our study addresses an open issue in the ﬁeld of PPA
regarding how patients with PPA should be classiﬁed into
diﬀerent subtypes. This is a very relevant question because
current classiﬁcation into three clinical variants aims to predict
underlying pathology. Classiﬁcation of PPA patients should
be useful for outcome prediction, and it may be crucial in
the near future when disease-modifying therapies are availa ble.
Our results conﬁrm the current classiﬁcation in non-ﬂuent,
semantic, and logopenic variants, but also suggest that curre nt
categorization may be improved.
The analysis of the distribution of patients among 4 clusters
indicates that the HCA method Linkage distinguishes between
patients associated with frontotemporal lobar degeneration
(group k0), AD (groups k1 and k2) and healthy controls.
This suggests, on the one hand, the capacity of FDG-PET
to discriminate between frontotemporal degeneration and AD ;
and, on the other hand, to distinguish between PPA and
healthy controls. Interestingly, patients who clinically be long
to the logopenic variant were divided in two groups. Both
groups showed left parieto-temporal hypometabolism. However,
the ﬁrst one associated left frontal hypometabolism, while the
second one involved left posterior cingulate and right parieto -
temporal hypometabolism. Some previous studies have suggested
the existence of some subtypes within the logopenic variant,
which might explain the clinical heterogeneity of this varian t
(
Machulda et al., 2013; Leyton et al., 2015 ). In our series,
the percentage of progression to dementia was similar in both
groups.
FIGURE 8 | Clustering in eight groups. Voxel-based brain mapping anal ysis showing regions with lower metabolism in the group k0 (n on-ﬂuent PPA subtype 1A, in
violet) and k5 (non-ﬂuent PPA subtype 1B, in green) in compari son to healthy controls.
Frontiers in Aging Neuroscience | www.frontiersin.org 9 July 2018 | Volume 10 | Article 230

Matias-Guiu et al. Clustering Analysis of PPA
FIGURE 9 | Flowchart of patient distribution within clusters, taking into account predominant clinical variants according to co nsensus classiﬁcation and second clinical
syndromes. Non-ﬂuent PPA is shown in blue, semantic PPA in gre en, logopenic PPA in yellow, and healthy controls in orange. ALS, amyotrophic lateral sclerosis;
bvFTD, behavioral variant frontotemporal dementia; CBS, c orticobasal syndrome; PPA, primary progressive aphasia; P SP , progressive supranuclear palsy.
Classiﬁcation in 6 clusters divided the former group
including several variants of PPA associated with frontotemporal
degeneration in three subgroups: k0 (which could be called no n-
ﬂuent subtype 1), k2 (non-ﬂuent subtype 2), and k3 (which
corresponds to the semantic variant). The second syndrome
during the follow-up in k2 was more frequently progressive
supranuclear palsy, which has been considered very speciﬁc
for tauopathies 4R (
Josephs et al., 2006 ). In contrast, non-
ﬂuent subtype 1 showed more heterogeneous progression.
However, when classifying in 8 clusters (6 subtypes of PPA),
k0 is subdivided in k0 (which could be named as non-
ﬂuent subtype 1A) and k5 (which could be called non-ﬂuent
subtype 1B). k5 evolved mainly to dementia with or without
prominent behavioral symptoms but without parkinsonism or
motor neuron disease, which might be suggestive of TDP-43 type
A proteinopathy. Patterns of hypometabolism diﬀered between
groups. In the non-ﬂuent subtype 1, hypometabolism was mainly
restricted to the left hemisphere, involving left frontal lo be and
also the temporal and parietal lobes. This is a neuroimaging
pattern previously associated with TDP-43 proteinopathies type
A (
Rohrer et al., 2010; Harper et al., 2017 ). Conversely, non-
ﬂuent subtype 2 showed a more medial and bilateral impairment
of the frontal lobe, which has been previously associated wit h
evolution to progressive supranuclear palsy ( Josephs et al.,
2012; Matias-Guiu et al., 2015a ). These results agree with
previous studies with pathological conﬁrmation, which have
described some neuroimaging patterns more suggestive of
tau than TDP-43 proteinopathies in non-ﬂuent PPA, such
as the more medial frontal and subcortical impairment, or
the greater involvement of white matter than gray matter in
MRI (
Caso et al., 2014; Xia et al., 2017; Santos-Santos et al.,
2018).
Our study suggests that FDG-PET may classify patients
with PPA and, in turn, it could enable the prediction of the
clinical course and possible underlying neuropathology. This is
especially relevant considering some diﬃculties, limitati ons, and
reduced availability of other PET tracers for amyloid and ta u.
In this regard, amyloid imaging may not be speciﬁc for AD,
especially with aging, or it may be indicative of mixed patholo gy
in cases associated with frontotemporal degeneration (
Santos-
Santos et al., 2018 ). In turn, tau tracers such as 18F-A V1451
showed also milder uptake in tauopathies not associated with AD
or even TDP-43 proteinopathies, as has been recently outlined
(
Makaretz et al., 2017; Josephs et al., 2018 ).
Frontiers in Aging Neuroscience | www.frontiersin.org 10 July 2018 | Volume 10 | Article 230

Matias-Guiu et al. Clustering Analysis of PPA
According to Davies-Bouldin index, 6 subtypes of PPA (8
clusters) seem to be the a more optimized classiﬁcation. We
included a group of 31 patients with a second FDG-PET study
during the follow-up and, in all cases, both studies were cla ssiﬁed
in the same cluster. Thus, none cluster seems to be a later
stage of a previous one, and this supports the idea that each
cluster represents a speciﬁc subtype of PPA. To our knowledge,
this is the ﬁrst study using computational analysis performed
on the FDG-PET attributes in PPA, which may improve the
classiﬁcation of patients. Some previous studies have used da ta
mining techniques applied to neuropsychological and language
performance (
Knibb et al., 2006; Wicklund et al., 2014; Maruta
et al., 2015; Hoﬀman et al., 2017 ), generally conﬁrming the
non-ﬂuent and semantic variants, but questioning the logope nic
subtype. For instance, Hoﬀman et al. found three main clusters ,
the ﬁrst one including the semantic variant, the second one
patients with non-ﬂuent and logopenic variants, and the third
cluster with patients in more advanced stages of disease (
Hoﬀman
et al., 2017). Analysis of the topography of brain metabolism may
represent a better source for computational algorithms, beca use
it is less inﬂuenced by several factors such as culture, educ ational
level, etc., which impact on language and cognitive assessme nts.
Our study has some limitations. First, although clusters ar e
clearly deﬁned, HCA methods, particularly Linkage, present
as weakness that every cluster is compared only with the
closest cluster. In addition, cluster analysis was based on brain
metabolism in several regions of interest based on AAL atlas .
Second, amyloid biomarkers were not performed in all patients ,
and tau imaging was not available. Further research is neces sary
to validate our ﬁndings in independent cohorts of patients,
especially with longitudinal neuroimaging and pathological
conﬁrmation.
In conclusion, we found that unsupervised clustering analysi s
of FDG-PET data favored, based on the Davies-Bouldin index,
the classiﬁcation of PPA into six variants rather than three
subtypes as currently recommended in consensus PPA criteria .
These subtypes try to go beyond the current categorization in
three variants, probably improving the prediction of clinical
outcome. In this regard, we have identiﬁed three subtypes wit hin
non-ﬂuent variant, two subtypes within logopenic PPA, and
conﬁrmed the semantic variant. These results also support the
usefulness of FDG-PET in evaluating PPA and the possibility
to improve the classiﬁcation of patients with PPA using FDG-
PET imaging exclusively. Furthermore, our study suggests
the applicability of computational methods for clustering in
the analysis of brain metabolism, which could provide new
insights in neurodegenerative disorders. Future studies sh ould
evaluate clinical and language features, and longitudinal follow-
up characteristics of each new subtype.
ETHICS STATEMENT
All procedures performed in studies involving human
participants were in accordance with the ethical standards
of the institutional research committee of the Hospital Clin ico
San Carlos and with the 1964 Helsinki declaration and its later
amendments. Informed consent was obtained from all individual
participants included in the study or their caregivers.
AUTHOR CONTRIBUTIONS
JAM-G and JA study concept and design. JM-G and JC study
supervision. TM-R and VP literature search. JAM-G, MC-M,
TM-R, and VP acquisition of data. JAM-G, JD-Á, JA, and JR
interpretation of data. JD-Á, JA, and JR statistical analysis ofdata.
JAM-G, JD-Á, and JA writing the manuscript. MC-M, JM-G, and
JC critical revision of the manuscript for important intellec tual
content.
ACKNOWLEDGMENTS
We acknowledge support from Spanish Ministry of Economy
and Competitiveness and European Regional Development
Fund (FEDER) under project TIN2017-85727-C4-4-P and
projects IB16035, of the Regional Government of Extremadura,
Department of Commerce and Economy, conceded by the
European Regional Development Fund, A way to build
Europe.
SUPPLEMENTARY MATERIAL
The Supplementary Material for this article can be found
online at: https://www.frontiersin.org/articles/10.338 9/fnagi.
2018.00230/full#supplementary-material
REFERENCES
Armstrong, M. J., Litvan, I., Lang, A. E., Bak, T. H., Bhatia, K. P. ,
Borroni, B., et al. (2013). Criteria for the diagnosis of corticoba sal
degeneration. Neurology 80, 496–503. doi: 10.1212/WNL.0b013e3182
7f0fd1
Botha, H., Duﬀy, J. R., Whitwell, J. L., Strand, E. A., Machulda, M. M.,
Schwarz, C. G., et al. (2015). Classiﬁcation and clinicoradiologi c features of
primary progressive aphasia (PPA) and apraxia of speech. Cortex 69, 220–236.
doi: 10.1016/j.cortex.2015.05.013
Brooks, B. R., Miller, R. G., Swash, M., and Munsat, T. L. (2000). El
Escorial revisited: revised criteria for the diagnosis of amyotroph ic lateral
sclerosis. Amyotroph. Lateral Scler. Other Motor Neuron Disord. 1, 293–299.
doi: 10.1080/146608200300079536
Caso, F., Mandelli, M. L., Henry, M., Gesierich, B., Bettcher, B. M ., Ogar,
J., et al. (2014). In vivo signatures of nonﬂuent/agrammatic primary
progressive aphasia caused by FTLD pathology. Neurology 82, 239–247.
doi: 10.1212/WNL.0000000000000031
Cummings, J. L. (2003). Toward a molecular neuropsychiatry of
neurodegenerative diseases. Ann. Neurol. 54, 147–154. doi: 10.1002/ana.10616
Davies, D. L., and Bouldin, D. W. (1979). A cluster separation measure. IEEE Trans.
Pattern Anal. Mach. Intell. 1, 224–227. doi: 10.1109/TPAMI.1979.4766909
Della Rosa, P. A., Cerami, C., Gallivanone, F., Prestia, A., Caroli, A. , Castiglioni, I.,
et al. (2014). A standardized [18F]-FDG-PET template for spatial normalization
in statistical parametric mapping of dementia. Neuroinformatics 12, 575–593.
doi: 10.1007/s12021-014-9235-4
Everitt, B. S., Landau, S., Leese, M., and Stahl, D. (2011). Hierarchical Clustering, in
Cluster Analysis, 5th Edn. Chichester: John Wiley & Sons, Ltd.
Frontiers in Aging Neuroscience | www.frontiersin.org 11 July 2018 | Volume 10 | Article 230

Matias-Guiu et al. Clustering Analysis of PPA
Gorno-Tempini, M., Hillis, A., Weintraub, S., Kertesz, A., Mendez, M ., Cappa,
S., et al. (2011). Classiﬁcation of primary progressive aphasia and its variants.
Neurology 76, 1006–1014. doi: 10.1212/WNL.0b013e31821103e6
Harper, L., Bouwman, F., Burton, E. J., Barkhof, F., Scheltens, P., O’Brien,
J. T., et al. (2017). Patterns of atrophy in pathologically conﬁrmed
dementias: a voxelwise analysis. J. Neurol. Neurosurg. Psychiatry 88, 908–916.
doi: 10.1136/jnnp-2016-314978
Harris, J. M., Gall, C., Thompson, J. C., Richardson, A. M., Neary, D., du Plessis,
D., et al. (2013). Classiﬁcation and pathology of primary progressive aph asia.
Neurology 81, 1832–1839. doi: 10.1212/01.wnl.0000436070.28137.7b
Hauw, J. J., Daniel, S. E., Dickson, D., Horoupian, D. S., Jellinger , K., Lantos,
P. L., et al. (1994). Preliminary NINDS neuropathologic criteria for St eele-
Richardson-Olszewski syndrome (progressive supranuclear palsy). Neurology
44, 2015–2019. doi: 10.1212/WNL.44.11.2015
Hennig, C., Meila, M., Murtagh, F., and Rocci, R. (2015). Handbook of Cluster
Analysis. London: Routledge.
Hoﬀman, P., Sajjadi, S. A., Patterson, K., and Nestor, P. J. (20 17). Data-driven
classiﬁcation of patients with primary progressive aphasia. Brain Lang. 174,
86–93. doi: 10.1016/j.bandl.2017.08.001
Hu, Y., Xu, Q., Li, K., Zhu, H., Qi, R., Zhang, Z., et al. (2013). Gen der
diﬀerences of brain glucose metabolic networks revealed by FDG-PET:
evidence from a large cohort of 400 young adults. PLoS ONE 8:e83821.
doi: 10.1371/journal.pone.0083821
Jain, A. K., and Dubes, R. C. (1988). Algorithms for Clustering Data . Upper Saddle
River, NJ: Prentice-Hall, Inc.
Josephs, K. A., Duﬀy, J. R., Strand, E. A., Machulda, M. M., Senje m,
M. L., Master, A. V., et al. (2012). Characterizing a neurodegene rative
syndrome: primary progressive apraxia of speech. Brain 135(Pt 5), 1522–1536.
doi: 10.1093/brain/aws032
Josephs, K. A., Martin, P. R., Botha, H., Schwarz, C. G., Duﬀy, J. R ., Clark, H. M.,
et al. (2018). [18F]AV-1451 tau-PET and primary progressive aphasia. Ann.
Neurol. 83, 599–611. doi: 10.1002/ana.25183
Josephs, K. A., Petersen, R. C., Knopman, D. S., Boeve, B. F., Whi twell, J. L.,
Duﬀy, J. R., et al. (2006). Clinicopathologic analysis of frontote mporal
and corticobasal degenerations and PSP. Neurology 66, 41–48.
doi: 10.1212/01.wnl.0000191307.69661.c3
Knibb, J. A., Xuereb, J. H., Patterson, K., and Hodges, J. R. (2006 ). Clinical and
pathological characterization of progressive aphasia. Ann. Neurol. 59, 156–165.
doi: 10.1002/ana.20700
Leyton, C. E., Britton, A. K., Hodges, J. R., Halliday, G. M., and K ril, J. J.
(2016). Distinctive pathological mechanisms involved in primary progre ssive
aphasias. Neurobiol. Aging 38, 82–92. doi: 10.1016/j.neurobiolaging.2015.
10.017
Leyton, C. E., Hodges, J. R., McLean, C. A., Kril, J. J., Piguet, O ., and
Ballard, K. J. (2015). Is the logopenic-variant of primary progressive
aphasia a unitary disorder? Cortex 67, 122–133. doi: 10.1016/j.cortex.2015.
03.011
Machulda, M. M., Whitwell, J. L., Duﬀy, J. R., Strand, E. A., Dean, P. M.,
Senjem, M. L., et al. (2013). Identiﬁcation of an atypical varian t of logopenic
progressive aphasia. Brain Lang. 127, 139–144. doi: 10.1016/j.bandl.2013.
02.007
Makaretz, S. J., Quimby, M., Collins, J., Makris, N., McGinnis, S. , Schultz, A., et al.
(2017). Flortaucipir tau PET imaging in semantic variant primary progress ive
aphasia. J. Neurol. Neurosurg. Psychiatry . doi: 10.1136/jnnp-2017-316409.
[Epub ahead of print].
Marshall, C. R., Hardy, C. J. D., Volkmer, A., Russell, L. L., Bond, R. L., Fletcher,
P. D., et al. (2018). Primary progressive aphasia: a clinical approach. J. Neurol.
265, 1474-1490. doi: 10.1007/s00415-018-8762-6
Maruta, C., Pereira, T., Madeira, S. C., De Mendonca, A., and Guerreiro, M. (2015).
Classiﬁcation of primary progressive aphasia: Do unsupervised data min ing
methods support a logopenic variant? Amyotroph Lateral Scler. Frontotemporal
Degener. 16, 147–159. doi: 10.3109/21678421.2015.1026266
Mathworks (2008). K-means Clustering. Available online at: https://es.mathworks.
com/help/stats/kmeans.html?requestedDomain=true (Accessed April 1, 2018).
Matias-Guiu, J. A., Cabrera-Martin, M. N., Garcia-Ramos, R., Mo reno-Ramos,
T., V alles-Salgado, M., Carreras, J. L., et al. (2014). Evaluation of the new
consensus criteria for the diagnosis of primary progressive aphasia us ing
ﬂuorodeoxyglucose positron emission tomography. Dement. Geriatr. Cogn.
Disord. 38, 147–152. doi: 10.1159/000358233
Matias-Guiu, J. A., Cabrera-Martin, M. N., Matias-Guiu, J., an d Carreras, J. L.
(2017a). FDG-PET/CT or MRI for the Diagnosis of Primary Progressi ve
Aphasia? Am. J. Neuroradiol. 38:E63. doi: 10.3174/ajnr.A5255
Matias-Guiu, J. A., Cabrera-Martin, M. N., Moreno-Ramos, T., Gar cia-Ramos,
R., Porta-Etessam, J., Carreras, J. L., et al. (2015a). Clinical cou rse of primary
progressive aphasia: clinical and FDG-PET patterns. J. Neurol. 262, 570–577.
doi: 10.1007/s00415-014-7608-0
Matias-Guiu, J. A., Cabrera-Martin, M. N., Perez-Castejon, M. J ., Moreno-Ramos,
T., Rodriguez-Rey, C., Garcia-Ramos, R., et al. (2015b). Visua l and statistical
analysis of 18F-FDG-PET in primary progressive aphasia. Eur. J. Nucl. Med.
Mol. Imaging 42, 916–927. doi: 10.1007/s00259-015-2994-9
Matías-Guiu, J. A., Cuetos, F., Cabrera-Martin, M. N., V alles-Sa lgado, M.,
Moreno-Ramos, T., Carreras, J. L., et al. (2017b). Reading diﬃculti es in
primary progressive aphasia in a regular language-speaking cohort of patie nts.
Neuropsychologia 101, 132–140. doi: 10.1016/j.neuropsychologia.2017.05.018
Matias-Guiu, J. A., and Garcia-Ramos, R. (2013). Primary progressi ve
aphasia: from syndrome to disease. Neurologia 28, 366–374.
doi: 10.1016/j.nrleng.2012.04.018
Mesulam, M. M., Rogalski, E. J., Wieneke, C., Hurley, R. S., Geula, C. ,
Bigio, E. H., et al. (2014). Primary progressive aphasia and the evolvin g
neurology of the language network. Nat. Rev. Neurol. 10, 554–569.
doi: 10.1038/nrneurol.2014.159
Mesulam, M. M., and Weintraub, S. (2014). Is it time to revisit the c lassiﬁcation
guidelines for primary progressive aphasia? Neurology 82, 1108–1109.
doi: 10.1212/WNL.0000000000000272
Rogalski, E. J., and Mesulam, M. M. (2009). Clinical trajectories a nd biological
features of primary progressive aphasia (PPA). Curr. Alzheimer Res. 6, 331–336.
doi: 10.2174/156720509788929264
Rohrer, J. D., Geser, F., Zhou, J., Gennatas, E. D., Sidhu, M., Trojanowski,
J. Q., et al. (2010). TDP-43 subtypes are associated with distin ct
atrophy patterns in frontotemporal dementia. Neurology 75, 2204–2211.
doi: 10.1212/WNL.0b013e318202038c
Sajjadi, S. A., Patterson, K., Arnold, R. J., Watson, P. C., and Nestor, P. J. (2012).
Primary progressive aphasia: a tale of two syndromes and the rest. Neurology
78, 1670–1677. doi: 10.1212/WNL.0b013e3182574f79
Santos-Santos, M. A., Rabinovici, G. D., Iaccarino, L., Ayak ta, N., Tammewar,
G., Lobach, I., et al. (2018). Rates of amyloid imaging positivity in
patients with primary progressive aphasia. JAMA Neurol. 75, 342–352.
doi: 10.1001/jamaneurol.2017.4309
V andenberghe, R. (2016). Classiﬁcation of the primary progressive a phasias:
principles and review of progress since 2011. Alzheimers Res. Ther 8:16.
doi: 10.1186/s13195-016-0185-y
V arrone, A., Asenbaum, S., V ander Borght, T., Booij, J., Nobili, F., Nagren,
K., et al. (2009). EANM procedure guidelines for PET brain imaging us ing
[18F]FDG, version 2. Eur. J. Nucl. Med. Mol. Imaging 36, 2103–2110.
doi: 10.1007/s00259-009-1264-0
Ward, J. H. Jr. (1963). Hierarchical grouping to optimize an objective function. J.
Am. Stat. Assoc. 58, 236–244. doi: 10.1080/01621459.1963.10500845
Wicklund, M. R., Duﬀy, J. R., Strand, E. A., Machulda, M. M., Whit well,
J. L., and Josephs, K. A. (2014). Quantitative application of the
primary progressive aphasia consensus criteria Neurology 82, 1119–1126.
doi: 10.1212/WNL.0000000000000261
Xia, C., Makaretz, S. J., Caso, C., McGinnis, S., Gomperts, S. N., S epulcre, J., et al.
(2017). Association of in vivo [18F]AV-1451 Tau PET imaging results with
cortical atrophy and symptoms in typical and atypical Alzheimer disease. JAMA
Neurol 74, 427–436. doi: 10.1001/jamaneurol.2016.5755
Conﬂict of Interest Statement: The authors declare that the research was
conducted in the absence of any commercial or ﬁnancial relations hips that could
be construed as a potential conﬂict of interest.
Copyright © 2018 Matias-Guiu, Díaz-Álvarez, Ayala, Risco-Martín, Moreno-
Ramos, Pytel, Matias-Guiu, Carreras and Cabrera-Martín. Th is is an open-access
article distributed under the terms of the Creative Commons Attribution License (CC
BY). The use, distribution or reproduction in other forums is permitted, provided
the original author(s) and the copyright owner(s) are credit ed and that the original
publication in this journal is cited, in accordance with acc epted academic practice.
No use, distribution or reproduction is permitted which doe s not comply with these
terms.
Frontiers in Aging Neuroscience | www.frontiersin.org 12 July 2018 | Volume 10 | Article 230