---
reference_id: DOI:10.3389/fneur.2022.910054
title: The Role of Graph Theory in Evaluating Brain Network Alterations in Frontotemporal Dementia
authors:
- Salvatore Nigro
- Marco Filardi
- Benedetta Tafuri
- Roberto De Blasi
- Alessia Cedola
- Giuseppe Gigli
- Giancarlo Logroscino
journal: Frontiers in Neurology
year: '2022'
doi: 10.3389/fneur.2022.910054
content_type: full_text_pdf
full_text_attempted: true
full_text_provider: openalex
full_text_url: "https://www.frontiersin.org/articles/10.3389/fneur.2022.910054/pdf"
oa_status: gold
license: cc-by
local_pdf_path: files/DOI_10.3389_fneur.2022.910054.pdf
---

# The Role of Graph Theory in Evaluating Brain Network Alterations in Frontotemporal Dementia
**Authors:** Salvatore Nigro, Marco Filardi, Benedetta Tafuri, Roberto De Blasi, Alessia Cedola, Giuseppe Gigli, Giancarlo Logroscino
**Journal:** Frontiers in Neurology (2022)
**DOI:** [10.3389/fneur.2022.910054](https://doi.org/10.3389/fneur.2022.910054)

## Content

Frontotemporal dementia (FTD) is a spectrum of clinical syndromes that affects personality, behavior, language, and cognition. The current diagnostic criteria recognize three main clinical subtypes: the behavioral variant of FTD (bvFTD), the semantic variant of primary progressive aphasia (svPPA), and the non-fluent/agrammatic variant of PPA (nfvPPA). Patients with FTD display heterogeneous clinical and neuropsychological features that highly overlap with those presented by psychiatric syndromes and other types of dementia. Moreover, up to now there are no reliable disease biomarkers, which makes the diagnosis of FTD particularly challenging. To overcome this issue, different studies have adopted metrics derived from magnetic resonance imaging (MRI) to characterize structural and functional brain abnormalities. Within this field, a growing body of scientific literature has shown that graph theory analysis applied to MRI data displays unique potentialities in unveiling brain network abnormalities of FTD subtypes. Here, we provide a critical overview of studies that adopted graph theory to examine the topological changes of large-scale brain networks in FTD. Moreover, we also discuss the possible role of information arising from brain network organization in the diagnostic algorithm of FTD-spectrum disorders and in investigating the neural correlates of clinical symptoms and cognitive deficits experienced by patients.

MINI REVIEW
published: 28 June 2022
doi: 10.3389/fneur.2022.910054
Frontiers in Neurology | www.frontiersin.org 1 June 2022 | Volume 13 | Article 910054
Edited by:
Liyong Wu,
Capital Medical University, China
Reviewed by:
Peter S. Pressman,
University of Colorado Denver,
United States
*Correspondence:
Giancarlo Logroscino
giancarlo.logroscino@uniba.it
Salvatore Nigro
salvatoreangelo.nigro@gmail.com
†These authors have contributed
equally to this work and share ﬁrst
authorship
Specialty section:
This article was submitted to
Dementia and Neurodegenerative
Diseases,
a section of the journal
Frontiers in Neurology
Received: 31 March 2022
Accepted: 02 June 2022
Published: 28 June 2022
Citation:
Nigro S, Filardi M, Tafuri B, De Blasi R,
Cedola A, Gigli G and Logroscino G
(2022) The Role of Graph Theory in
Evaluating Brain Network Alterations in
Frontotemporal Dementia.
Front. Neurol. 13:910054.
doi: 10.3389/fneur.2022.910054
The Role of Graph Theory in
Evaluating Brain Network Alterations
in Frontotemporal Dementia
Salvatore Nigro 1,2*†, Marco Filardi 2,3†, Benedetta Tafuri 2,3, Roberto De Blasi 4,
Alessia Cedola 1, Giuseppe Gigli 1,5 and Giancarlo Logroscino 2,3*
1 Institute of Nanotechnology (NANOTEC), National Research C ouncil, Lecce, Italy, 2 Center for Neurodegenerative Diseases
and the Aging Brain, Department of Clinical Research in Neur ology, University of Bari Aldo Moro, “Pia Fondazione Cardin ale
G. Panico”, Tricase, Italy, 3 Department of Basic Medicine, Neuroscience, and Sense Orga ns, University of Bari Aldo Moro,
Bari, Italy, 4 Department of Radiology, “Pia Fondazione Cardinale G. Pani co”, Tricase, Lecce, Italy, 5 Department of
Mathematics and Physics “Ennio De Giorgi”, University of Sa lento, Lecce, Italy
Frontotemporal dementia (FTD) is a spectrum of clinical syn dromes that affects
personality, behavior, language, and cognition. The curre nt diagnostic criteria recognize
three main clinical subtypes: the behavioral variant of FTD (bvFTD), the semantic variant
of primary progressive aphasia (svPPA), and the non-ﬂuent/ agrammatic variant of PPA
(nfvPPA). Patients with FTD display heterogeneous clinica l and neuropsychological
features that highly overlap with those presented by psychi atric syndromes and other
types of dementia. Moreover, up to now there are no reliable d isease biomarkers,
which makes the diagnosis of FTD particularly challenging. T o overcome this issue,
different studies have adopted metrics derived from magnet ic resonance imaging (MRI)
to characterize structural and functional brain abnormali ties. Within this ﬁeld, a growing
body of scientiﬁc literature has shown that graph theory ana lysis applied to MRI data
displays unique potentialities in unveiling brain network abnormalities of FTD subtypes.
Here, we provide a critical overview of studies that adopted graph theory to examine
the topological changes of large-scale brain networks in FT D. Moreover, we also discuss
the possible role of information arising from brain network organization in the diagnostic
algorithm of FTD-spectrum disorders and in investigating t he neural correlates of clinical
symptoms and cognitive deﬁcits experienced by patients.
Keywords: frontotemporal dementia, primary progressive aphas ia, graph analysis, connectome analysis, small-
world, brain networks, magnetic resonance imaging, diffusion tensor imaging
INTRODUCTION
Frontotemporal dementia (FTD) is a neurodegenerative disord er characterized by executive,
behavioral, and/or language deﬁcits (
1, 2). The current diagnostic criteria recognize three main FTD
subtypes according to clinical presentation: the behavioral variant of FTD (bvFTD), the semantic
variant of a primary progressive aphasia (svPPA), and the non-ﬂ uent/agrammatic variant of PPA
(nfvPPA) ( 3, 4). bvFTD is the most common subtype characterized by prominent changes in
behavior and personality, as well as deﬁcits in executive fun ctions and social cognition ( 3, 5). On
the other hand, loss of semantic knowledge, agrammatism, and ﬂuency deﬁcits are the core features
of svPPA and nfvPPA (4).

Nigro et al. Graph Theory in FTD
The highly heterogeneous clinical and neuropsychological
phenotype presented by patients with FTD makes the diagnosis
of frontotemporal dementia per se and FTD subtypes particularly
challenging, especially in the early disease stages when the
symptoms are more nuanced (
1). To overcome this issue several
studies have used magnetic resonance imaging (MRI) to identif y
potential disease biomarkers and help clinicians in establi shing a
correct and timely diagnosis ( 6–8). Neuroimaging studies have
consistently documented patterns of bilateral fronto-tempo ral
gray matter alterations in patients with bvFTD ( 9–11). Atrophy
in temporal brain regions has been associated with language
impairments in patients with svPPA (
7, 12), while a higher
involvement of frontal regions (i.e., inferior frontal gyr us and
insula) is typically observed in patients with nfvPPA ( 13).
More recently, several studies have applied advanced MRI
acquisitions and analyses to obtain an in-depth characteriz ation
of brain alterations with respect to the simple gray matter
atrophy. Particularly, an increasing number of studies have
assessed brain connectivity through graph-theoretical met hods,
highlighting that this approach shows unique potentialities i n
FTD (
14–29).
Graph theory is an analytical framework that allows describing
the brain as a complex network identifying topological properties
that reﬂects global and local information communication ( 30–
33). Global and local graph properties allowed to identify
speciﬁc patterns of functional and structural alteration in
several neuropsychiatric and neurodegenerative disorders ,
including FTD subtypes (
34–38). Moreover, several studies have
demonstrated associations between cognitive impairments a nd
network properties, making graph theory a suitable approach to
investigate the neural correlates of cognitive performance (
34).
Nonetheless, graph theory results are often diﬃcult to inter pret
due to the diﬀerent metrics and levels (i.e., global and local ) at
which the analysis can be performed.
Here, we provided a step-by-step guide to interpret graph
theory outcomes in FTD. Firstly, we introduced the key
concepts underlying brain network construction and describ ed
the graph-based properties most frequently used to characteri ze
topological network organization. Second, we provided a crit ical
overview of studies that applied graph analysis in FTD by
discussing functional and structural network properties and their
association with clinical/neuropsychological variables. Finally,
we discussed the pros and cons of graph theory approaches in
FTD and points out a future research agenda.
GRAPH THEORY: KEY CONCEPTS AND
NETWORK CONSTRUCTION
Network Construction
Graph theory allows modeling a network as a set of discrete
elements (nodes) and their mutual relationships (edges)
(
30, 32, 39). Nodes usually represent predeﬁned brain regions,
and edges represent functional or structural connections between
regions ( 30, 31). Two brain regions are considered functionally
connected if they display coherent or synchronized neural
activity (
30, 40). Functionally connectivity is typically estimated
using functional MRI (fMRI) ( 41), but more recent studies
have shown that also single-photon emission computerized
tomography (SPECT) and F-ﬂuorodeoxyglucose positron
emission tomography (FDG-PET) are reliable techniques to
assess functional connections (
42–44). Structural connectivity is
typically estimated by the reconstruction of white matter ari sing
from diﬀusion tensor imaging (DTI) ( 45, 46). White matter
streamlines can be estimated using deterministic or probabil istic
tractography, and several measures of connectivity strengt h (e.g.,
number of streamlines, fractional anisotropy, mean diﬀusivi ty)
can be computed between pairs of brain regions ( 46, 47).
The structural connectivity between brain regions can also b e
indirectly estimated in terms of covariation of their gray m atter
morphological properties (volumes, cortical thickness, surf ace
area, and gyriﬁcation) or similarity among their gray-leve l
intensity ( 48–50) based on the assumption that morphological
features would covary due to shared axonal connectivity and /or
genetic factors ( 48). For detailed information on the pros, cons,
and most appropriate use of each MRI technique, we refer the
readers to the study by Islam et al. (
51). The deﬁned network
is represented through a connection matrix, which is typicall y
ﬁltered by applying thresholding and binarization approaches
(
52, 53). Diﬀerent approaches could be used to reduce the
inﬂuence of spurious connections on network topology, from
the simplest application of an absolute or proportional threshol d
to more recent approaches such as minimum spanning tree
(MST) (
54). A graphical representation of the framework for
the construction of a structural and functional brain netwo rk is
presented in Figure 1.
Segregation and Integration Properties
Diﬀerent global and local graph metrics are used to assess features
of brain network organization. Overall, they can be grouped i nto
information processing integration and segregation metric s (
30,
55, 56). Concerning brain network integration, the characterist ic
path length ( Lp) and global eﬃciency (global_E) are the most
frequently used metrics ( 55–57). Lp is deﬁned as the average
shortest path length between all pairs of nodes in the network (56)
and global_E is deﬁned as the average inverse shortest path length
(57). Brain networks with short Lp and/or high global_E are
thought to transfer information across regions more eﬃcien tly
(52, 56).
The modularity ( M) and average clustering coeﬃcient
(average_Clust_C) are the two widely used metrics of brain
network segregation that allow to assess information proces sing
within specialized brain subsystems (
55, 56). M is calculated by
partitioning the network into subgroups of nodes maximizing
intraconnections and minimizing interconnections (
58). The
average_Clust_C coeﬃcient is deﬁned as the average fractio n
in which pairs of neighboring nodes are also neighbors of
each other (
56). A high value of modularity and/or clustering
coeﬃcient mirror a higher propensity of the brain to execute
specialized processes within interconnected brain regions (
53,
56, 59). A small-world (SW) topology is characterized by high
clustering and short path length, which allows to support both
segregated/specialized and distributed/integrated inform ation
processing (
39, 55, 57).
Frontiers in Neurology | www.frontiersin.org 2 June 2022 | Volume 13 | Article 910054

Nigro et al. Graph Theory in FTD
FIGURE 1 | Schematic representation of brain network construction. (A) Diffusion tensor imaging; (B) resting-state fMRI; (C) gray matter structural covariance.
The above-described global metrics can also be deﬁned at a
local level to characterize integration (local path-length : local_Lp
and local eﬃciency: local_E) and segregation (local cluste ring
coeﬃcient: local_Clust_C) properties for each brain region ( 56).
Within-module degree and participation coeﬃcient can also be
computed for each node to characterize its connectivity with in
and across modules (
58).
Centrality Measures and Hubs Deﬁnition
Centrality measures allow to identify nodes with a high inﬂu ence
on the network function (
56). Nodal degree (deg) is a measure
of centrality deﬁned as the number or the sum of connectivity
weights of the edges incident to a node (
53, 56, 59). Between
centrality (BC) measures the fraction of shortest paths between all
node pairs in the network that pass through a given index node
(
56, 59). Closeness centrality ( CC) measures the mean distance
between a given node and the rest of the network ( 30, 56, 59).
Centrality measures allow the identiﬁcation of network hub s,
which represent topologically central regions that play a cruc ial
role in inter-network communication ( 33). A brain region is
usually deﬁned as a hub when its nodal metrics are at least one
standard deviation greater than the average of the correspon ding
measure over the entire network (
21, 60). Hub regions tend to
be densely interconnected and form a rich-club structure in the
brain organization where the hubs are more connected among
themselves than to nodes with lower centrality (
33).
Regarding networks deﬁned using the MST approach,
alternative metrics are used to characterize centrality (m aximum
degree, maximum betweenness), distance (diameter), and
topological aspects (degree divergence, leaf fraction) (
54).
NETWORKS AL TERATIONS IN PATIENTS
WITH FTD
Sixteen studies applied graph analysis to assess structural an d
functional brain network alteration in patients with FTD. El even
studies (68.7%) compared bvFTD patients with healthy controls ,
one study compared svPPA patients with healthy controls,
one study compared nfvPPA with healthy controls and three
studies compared FTD subtypes among themselves and with
healthy controls. The study from Sedeno et al. reported on a
pooled sample of patients with PPA, which did not allow us to
discern disease-speciﬁc information, therefore, we decide d not
to consider these results when discussing network alterati ons of
PPA patients. Collectively, these studies analyzed 472 bvFTD, 70
svPPA, 94 nfvPPA, and 15 logopenic-variant primary progressive
aphasia (lvPPA) patients. Detailed information for each stud y is
reported in Table 1.
Global and Local Networks Alterations in
BvFTD
Behavioral variant of FTD is by far the most extensively stud ied
FTD dementia in terms of brain network alterations. Overall,
the brain networks of patients with bvFTD showed preserved
small-worldness organization, but signiﬁcant alterations in global
properties of the functional network have been consistently
observed across studies (
14, 17, 18, 23). Studies that applied
Frontiers in Neurology | www.frontiersin.org 3 June 2022 | Volume 13 | Article 910054

Nigro et al. Graph Theory in FTD
TABLE 1 | Summary of studies that used graph analysis in patients with FTD.
Reference Sample Mean Age MMSE Modality Network size Connecti vity
measures
Binary(B)/
weighted
(W)
Global
properties
Local
properties
Hub (H)/
modularity
(M)
Agosta et al.
(
14)
50 controls 18 bvFTD 61 ± 9
61 ± 8
29 ± 1
21 ± 7
rs-fMRI 90 ROIs grouped
into 8 macro-areas
Pearson’ s
correlation
B Clust_C, Lp
global_E, Ass
mean deg
deg Bc H
Agosta et al.
(
15)
50 controls 13 svPPA 61.0 ± 9.0
59.4 ± 9.6
22.2 ± 7.2
29.0 ± 1.0
rs-fMRI 90 ROIs Pearson’ s
correlation
B Clust_C, Lp
global_E, Ass
mean deg, SW
deg Bc H
Daianu et al.
(
16)
37 controls 20 bvFTD
23 EOAD
59.4 ± 9.6
60.7 ± 10.7
59.6 ± 8.8
29.1 ± 0.9
24.1 ± 4.7
23.4 ± 4.2
DTI 68 ROIs Fiber density FA
MD
W Rich club
organization
deg –
Sedeno et al.
(
17)
12 controls 14 bvFTD
10 stroke
62.58 ± 6.30
66.42 ± 6.83
54.50 ± 9.80
29.08 ± 1.44
25.50 ± 3.87
28.80 ± 1.09
rs-fMRI 116 ROIs grouped
into 7 networks
Wavelet
analysis
B Average Bc – –
Sedeno et al.
(
18)
Site 1: 16 controls 16
bvFTD 13 FIS; Site 2:
29 controls 17 bvFTD 8
PPA; Site 3: 15
Controls 14 bvFTD
15 AD
63.50 ± 7.22
69.37 ± 7.29
62.77 ± 10.4
61.30 ± 7.16
65.23 ± 8.29
60.12 ± 5.81
69.13 ± 6.59
65.33 ± 9.12
64.07 ± 7.34
– rs-fMRI 90 ROIs Pearson’ s
correlation
B/W Lp
Clust_C
deg Bc CC –
Filippi et al.
(
19)
32 controls 38 bvFTD
37 EOAD
62.3 ± 2.6
63.8 ± 7.3
62.1 ± 3.9
29.3 ± 0.8
22.7 ± 5.8
19.3 ± 4.9
rs-fMRI 220 ROIs grouped
into 6 macro-areas
Pearson’ s
correlation
W Clust_C, Lp
local_E
mean strength
Clust_C, Lp
mean
strength
local_E
-
Vijverberg
et al. (
20)
59 bvFTD 90 AD 74
SCD
62.1 ± 6.0
63.1 ± 6.1
61.3 ± 6.6
24.6 ± 3.5
21.1 ± 5.0
28.3 ± 1.9
T1 weighted 90 ROIs Intra-cortical
similarity
B deg, Lp
Clust_C, Bc
SW
deg, Lp
Clust_C Bc
-
Mandelli et al.
(
21)
20 controls 20 nfvPPA 68.6 ± 6.0
68.8 ± 7.3
29.1 ± 1.5
26.2 ± 3.7
rs-fMRI 110 regions
belonging to the
speech production
network
Pearson’ s
correlation
– global_E
Lp
Ass
deg Bc H
M
Reyes et al.
(
22)
32 controls 50 bvFTD
14 svPPA 22 nfvPPA
61.25 ± 7.28
65.85 ± 8.1
60.3 ± 7.65
63.63 ± 6.87
28.86 ± 1.27
22.47 ± 6.5
16.67 ± 7.66
16.9 ± 6.92
rs-fMRI 90 ROIs Pearson’ s
correlation
W global_E
Lp, deg,
Clust_C, Bc
– –
(Continued)
Frontiers in Neurology | www.frontiersin.org 4 June 2022 | Volume 13 | Article 910054

Nigro et al. Graph Theory in FTD
TABLE 1 | Continued
Reference Sample Mean Age MMSE Modality Network size Connecti vity
measures
Binary(B)/
weighted
(W)
Global
properties
Local
properties
Hub (H)/
modularity
(M)
Saba et al.
(
23)
39 controls 41 bvFTD 61.7 ± 6.5
65.6 ± 7.01
– rs-fMRI 116 ROIs Wavelet correlation B (MST) Maximum deg,
maximum Bc,
diameter, Ecc,
Ass, deg
leaf fraction
– –
Malpetti et al.
(
24)
82 controls 82 bvFTD 67.93 ± 6.95
69.37 ± 7.73
68.7 ± 1.5
71.4 ± 2.2
FDG-PET 121 ROIs Metabolic
connectivity
– – – H
M
T ao et al. (25) 17 controls 18 nfvPPA
15 lvPPA 9 svPPA
65 ± 8.18
69 ± 5.37
64 ± 8.12
69 ± 5.25
- rs-fMRI 76 ROIs Pearson’ s
correlation
B global_E, Lp
Ass, Clust_C
SW
Lp Clust_C H
Zhou et al.
(
26)
20 controls 64 bvFTD 68.7 ± 1.5
71.8 ± 1.7
29.50 ± 0.1
20.08 ± 4.35
SPECT 90 ROIs Pearson’ s
correlation
B global_E
SW
local_E Bc
deg
H
Nigro et al.
(
27)
20 controls 25 bvFTD 63.60 ± 5.90
66.92 ± 7.69
27.90 ± 1.68
20.80 ± 5.57
T1 82 ROIs Joint variation W SW local_E
Clust_C
deg
-
Ng et al. (
29) 47 controls 14 bvFTD
50 AD
63.20 ± 5.00
62.05 ± 5.47
65.45 ± 5.87
29.02 ± 1.15
20.82 ± 5.66
21.21 ± 6.72
rs-fMRI 141 ROIs Pearson’ s
correlation
W - deg, local_E
within-
module deg
partic_c
M
Nigro et al.
(
28)
110 controls 34 svPPA
34 nfvPPA
63.12 ± 7.49
62.91 ± 6.29
68.32 ± 7.27
29.35 ± 0.77
24.97 ± 5.10
25.54 ± 4.04
T1 82 ROIs Joint variation W SW local_E
Clust_C
deg
H
bvFTD, behavioral variant of frontotemporal dementia; svPPA, sema ntic variant of primary progressive aphasia; nfvPPA, non-ﬂuent/agram matic variant of primary progressive aphasia; lvPPA, logopenic variant of primary progressive
aphasia; PPA, primary progressive aphasia; EOAD, early-onset Alz heimer’s disease; FIS, fronto-insular stroke; AD, Alzheimer’s disease; SCD, subjective cognitive decline; MMSE, Mini-Mental State Examination ; rs-fMRI, resting state
functional magnetic resonance imaging; DTI, diffusion tensor ima ging; FDG-PET , F-ﬂuorodeoxyglucose positron emission tomography; SPECT , single-photon emission computed tomography; ROI, region of interest; Clust_C, clusterin g
coefﬁcient; Lp, path length; E, efﬁciency; Ass, assortativity; deg, degree ; SW, small-worldness index; Bc, betweenness centrality; Ecc, eccen tricity.
Frontiers in Neurology | www.frontiersin.org 5 June 2022 | Volume 13 | Article 910054

Nigro et al. Graph Theory in FTD
graph analysis to resting state-fMRI documented alterations
of both integration and segregation of information processi ng
as reﬂected by lower average clustering coeﬃcient, global
eﬃciency, and higher characteristic path length (
14, 18). A
recent study that adopted MST-based analysis provided further
information documenting a higher diameter and eccentricit y
(
23), which indicates a loss of eﬃciency in exchange informatio n
capacity. Similar results arise from studies that applied graph
theory to structural MRI (
20, 27), which showed a reduced
global eﬃciency and clustering coeﬃcient, suggesting an ov erall
reduced ability in information transfer. On the other hand,
evidence is less conclusive for studies that assessed alter ations
at the local level. The majority of studies found a reduction of
nodal degree, particularly evident over frontal regions (na mely,
orbitofrontal gyrus, anterior cingulate cortex, superior t emporal
pole, insula, superior and middle frontal gyri) (
14, 16, 17,
19, 26), but alterations have been also observed over the left
caudate nucleus, superior parietal and occipital lobes ( 14). A
decreased integration and interconnection in temporal and
frontal brain regions were also conﬁrmed by a multicenter
study investigating functional brain network organizatio n (
18).
Moreover, patients with bvFTD showed an extensive reallocation
of nodes across modules, most notably in the fronto-parietal ,
limbic-basal ganglia, and cingulum-temporal modules ( 24).
Studies on structural MRI corroborated these ﬁndings by
documenting lower local eﬃciency in the cortical thickness of
caudal and rostral middle frontal gyrus, rostral anterior cingulate,
and transverse temporal gyrus (
27).
Finally, a loss of hubs over diﬀerent brain regions, namely
frontal gyrus (right superior frontal, inferior orbitofron tal gyri,
left anterior cingulate cortex, and cuneus), basal ganglia , limbic
system, cerebellum, and temporo-occipital cortex has also be en
reported. By contrast, new hubs appeared in the orbitofrontal and
parietotemporal brain regions (14, 24).
Global and Local Networks Alterations in
svPPA
The global brain network organization of patients with svPPA
was characterized by a decreased global eﬃciency and cluste ring
coeﬃcient, and a higher characteristic path length (
15, 22),
which could reﬂect lower segregation and integration in the
overall network organization. This ﬁnding was also conﬁrme d
by a recent study showing a reduced small-worldness index in
the structural brain network of patients (
28). At a local level,
a reduced nodal eﬃciency, degree, and clustering coeﬃcient
have been observed in several brain regions, including the l eft
middle and superior temporal gyri, entorhinal cortex, amygda la,
fusiform, hippocampus, and insula (
15, 28). Moreover, a loss of
hubs was observed in left-hemisphere regions ( 15).
Global and Local Networks Alterations in
nfvPPA
In patients with nfvPPA, a lower global eﬃciency was observed
over the whole-brain network and in the speech production
network (SPN) (
21, 22). Increased path length, clustering
coeﬃcient, and modularity were also observed in the SPN ( 21).
While the increased path length suggested a reduction in the
information integration, the higher clustering coeﬃcient a nd
modularity may indicate a tendency of the network to segregat e
into smaller communities (
21). At a local level, lower clustering
coeﬃcient, degree, and local eﬃciency were observed in seve ral
frontal regions including the left caudal and middle fronta l
gyrus, superior frontal gyrus, and left pars opercularis ( 27).
Moreover, a loss of hubs in the left fronto-parietal-temporal
area of the SPN, typically aﬀected by the disease, was also
documented while additional hubs were being recruited more
anteriorly within the left frontal regions and in the right
hemisphere (
21).
Global and Local Networks Alterations
Between FTD Subtypes
When FTD subtypes were directly compared, a lower global
eﬃciency was observed in patients with nfvPPA relative to
bvFTD but not to svPPA (
22). Moreover, patients with nfvPPA
presented a less small-worldness index than patients with
svPPA (
28). At local level, signiﬁcant diﬀerences were observed
only between PPA subtypes. In particular, decreased clusterin g
coeﬃcient, degree, and local eﬃciency in the temporal pole
were observed in patients with svPPA relative to nfvPPA.
By contrast, patients with svPPA display higher values of
these local metrics in the left caudal frontal gyrus and left
pars opercularis than nfvPPA (
28). A diﬀerent conﬁguration
of hubs was also found among PPA variants ( 25). More
in detail, both lvPPA and svPPA showed a lateralized hub
distribution (right brain hemisphere) while patients with nfvP PA
were characterized by a bilateral distribution across both
hemispheres (
25).
Association of Brain Network T opology
With Clinical/Neuropsychological
A very limited number of studies have correlated graph analys is
metrics with clinical/neuropsychological impairments in FTD ,
with all studies speciﬁcally focused on patients with bvFTD.
A lower clustering coeﬃcient in the right hippocampus has
been associated with impairment in cognition and executive
functioning, while a lower degree in the superior occipital
gyrus has been associated with attentional impairments (
20).
Apathy and inhibition (measured through the frontal system
behavior scale) showed a negative association with path leng th
and a positive association with global eﬃciency, degree, and
clustering (
22). Increased nodal centrality in the left insular and
right frontal hubs resulted associated with the degree of so cial
cognition impairments. More recently, the severity of behavi oral
alterations (assessed through the neuropsychiatric invent ory)
was associated with lower modularity in the salience/ventr al
attention network and higher modularity within the module
degree in the left cingulate cortex of the control network (
29).
Finally, higher overall cognitive functioning (assessed t hrough
the MMSE) resulted associated with higher eﬃciency of caudal
anterior cingulate thickness (
27).
Frontiers in Neurology | www.frontiersin.org 6 June 2022 | Volume 13 | Article 910054

Nigro et al. Graph Theory in FTD
LIMITATIONS AND FUTURE DIRECTIONS
The diagnosis of FTD-spectrum dementia is established based
on clinical presentation, yet at the same time it is becoming
increasingly reliant on neuroimaging. Indeed, the current
diagnostic criteria (
3, 4) require the documentation of frontal
and/or anterior temporal atrophy for establishing the diagno sis
of “probable” bvFTD. With the advent of new and more
sophisticated analytical techniques, such as graph theory an alysis
and the study of connectome, neuroimaging data are likely to
gain a key role in the diagnosis of dementia, including FTD
subtypes. However, up to now, graph theory has been extensivel y
applied to document altered brain connectivity in Alzheimer’ s
disease (
36, 61–63), while studies in FTD are rare and markedly
skewed in favor of bvFTD, with only two studies speciﬁcally
focused on svPPA and nfvPPA.
In bvFTD, graph analysis revealed a loss of eﬃciency in the
information processing across brain regions reﬂected by red uced
clustering coeﬃcient and increased path length.
The pattern of neuroanatomical involvement highlighted by
graph analysis overlapped with that observed in previous studie s
that analyzed “classic” quantitative neuroimaging metric s (i.e.,
gray-matter atrophy) in documenting alterations over frontal and
temporal regions, further conﬁrming their crucial role in bv FTD
pathogenesis (
10, 11, 64). Local network alterations showed loss
of central nodes in the frontotemporal cortex and limbic syst em
and a reorganization of network hubs, which could either mir ror
a compensatory process or be related to disease progression.
Moreover, global and local metrics were associated with the
severity of behavioral symptoms, overall cognitive functio ning,
and impairment in speciﬁc cognitive domains, suggesting that
the alterations of information processing may exert a signiﬁ cant
eﬀect on the cognitive and behavioral symptoms experienced
by patients.
Concerning svPPA, the few available studies documented
reduced nodal eﬃciency, degree and clustering, and loss of h ubs
over several temporal and limbic regions, which indicates a
reduced centrality of these regions in the information tran sfer.
On the other hand, alterations over frontal brain regions
such as the caudal middle and superior frontal gyrus were
associated with nfvPPA. Moreover, patients with nfvPPA showed
a reorganization of hub distribution in the speech production
network and loss of hubs in the fronto–parietal–temporal area s.
When network alterations are compared between FTD
subtypes, nfvPPA presented a higher impairment of global
metrics compared to both bvFTD and svPPA. Moreover, svPPA
and nfvPPA showed diﬀerences in local metrics: patients
with nfvPPA display local abnormalities in brain regions
crucial for language production (left caudal frontal gyrus a nd
pars opercularis), while patients with svPPA showed greater
impairment in areas associated with language comprehension
such as the temporal pole.
Taken together, these results indicate that graph theory is
capable of detecting speciﬁc brain network alterations in pati ents
with FTD that could potentially serve as a disease biomarker.
However, there is a series of methodological issues that limi ts its
broader applicability.
First, there is a lack of standardized protocols for performin g
graph analysis, resulting in a wide variability of metrics and
approaches across studies. Particularly the choice of thresholding,
which is often arbitrary, signiﬁcantly aﬀects graph metric
quantiﬁcation and therefore limits the reproducibility of re sults.
More recent techniques, such as MST , have the potential to
overcome this issue but to date have been applied only in one
study in the ﬁeld of FTD.
Second, graph metrics are inﬂuenced by the parcellation
scheme used to deﬁne network nodes, yet no consensus
exists regarding which brain parcellation could be considered
optimal to capture functional activity or anatomical intersu bject
variability. Third, all studies reviewed that analyzed fMRI focused
on static functional connectivity, assuming temporal stabi lity
over scanning time. However, recent studies have reported
that connectivity shows time-dependent ﬂuctuations on the
scale of seconds to minutes (
65). Noteworthy, these time-
dependent changes per se have provided novel insights into
brain organization and should be considered in future studie s
on patients with FTD ( 66). Fourth, new reliable and practical
frameworks need to be proposed to deﬁne graph metrics using
the integration of diﬀerent brain imaging modalities. Final ly,
all studies applied a “transversal” research design, with diﬀe rent
graph metrics being assessed during a singular MRI session,
while longitudinal studies are completely lacking, precludin g the
possibility to quantify the predictive value of these metrics on
disease progression.
CONCLUSIONS
Graph analysis is proven to be able to detect speciﬁc global and
local brain network alterations in patients with bvFTD, while
the number of studies is too limited to draw any deﬁnitive
conclusions on svPPA and nfvPPA. The assessment of network
alterations in FTD spectrum may have important clinical
implications both in the diagnostic process, as a potential disea se
biomarker, and in the follow-up as an approach potentially able
to track disease course.
AUTHOR CONTRIBUTIONS
Conceptualization: SN and GL. Data curation: BT , RDB, and
AC. Investigation: SN, MF , and BT. Methodology: SN, MF , BT ,
RDB, and AC. Supervision: GL and GG. Writing—review and
editing for important intellectual content: SN, MF , BT , AC, GG ,
and GL. Writing—original manuscript: SN and MF. All authors
contributed to the article and approved the submitted version .
FUNDING
This work has been supported with the founding of Regione
Puglia and CNR for Tecnopolo per la Medicina di Precisione.
D.G.R. n. 2117 of 21.11.2018 (B84I18000540002).
Frontiers in Neurology | www.frontiersin.org 7 June 2022 | Volume 13 | Article 910054

Nigro et al. Graph Theory in FTD
REFERENCES
1. Bang J, Spina S, Miller BL. Frontotemporal dementia. Lancet. (2015)
386:1672–82. doi: 10.1016/S0140-6736(15)00461-4
2. Snowden JS, Thompson JC, Stopford CL, Richardson AMT , Gerhard A,
Neary D, et al. The clinical diagnosis of early-onset dementias: di agnostic
accuracy and clinicopathological relationships. Brain. (2011) 134:2478–
92. doi: 10.1093/brain/awr189
3. Rascovsky K, Hodges JR, Knopman D, Mendez MF , Kramer JH,
Neuhaus J, et al. Sensitivity of revised diagnostic criteria for the
behavioural variant of frontotemporal dementia. Brain. (2011) 134:2456–77.
doi: 10.1093/brain/awr179
4. Gorno-Tempini ML, Hillis AE, Weintraub S, Kertesz A, Mendez M,
Cappa SF , et al. Classiﬁcation of primary progressive aphasia and its
variants. Neurology. (2011) 76:1006–14. doi: 10.1212/WNL.0b013e31821
103e6
5. Johnson JK, Diehl J, Mendez MF , Neuhaus J, Shapira JS, Forman M,
et al. Frontotemporal lobar degeneration: demographic characteristics of 353
patients. Arch Neurol. (2005) 62:925–30. doi: 10.1001/archneur.62.6.925
6. McCarthy J, Collins DL, Ducharme S. Morphometric MRI as a
diagnostic biomarker of frontotemporal dementia: a systematic
review to determine clinical applicability. Neuroimage Clin. (2018)
20:685–96. doi: 10.1016/j.nicl.2018.08.028
7. Collins JA, Montal V , Hochberg D, Quimby M, Mandelli ML, Makris
N, et al. Focal temporal pole atrophy and network degeneration in
semantic variant primary progressive aphasia. Brain. (2017) 140:457–
71. doi: 10.1093/brain/aww313
8. Tee BL, Gorno-Tempini ML. Primary progressive aphasia: a
model for neurodegenerative disease. Curr Opin Neurol. (2019)
32:255–65. doi: 10.1097/WCO.0000000000000673
9. Rosen HJ, Gorno-Tempini ML, Goldman WP , Perry RJ, Schuﬀ N, Weiner
M, et al. Patterns of brain atrophy in frontotemporal dementia and semant ic
dementia. Neurology. (2002) 58:198–208. doi: 10.1212/WNL.58.2.198
10. Boccardi M, Sabattoli F , Laakso MP , Testa C, Rossi R, Beltramello A, et al.
Frontotemporal dementia as a neural system disease. Neurobiol Aging. (2005)
26:37–44. doi: 10.1016/j.neurobiolaging.2004.02.019
11. Whitwell JL, Przybelski SA, Weigand SD, Ivnik RJ, Vemuri P , Gun ter
JL, et al. Distinct anatomical subtypes of the behavioural varian t of
frontotemporal dementia: a cluster analysis study. Brain. (2009) 132:2932–
46. doi: 10.1093/brain/awp232
12. Brambati SM, Rankin KP , Narvid J, Seeley WW, Dean D, Rosen HJ,
et al. Atrophy progression in semantic dementia with asymmetric temporal
involvement: a tensor-based morphometry study. Neurobiol Aging. (2009)
30:103–11. doi: 10.1016/j.neurobiolaging.2007.05.014
13. Mandelli ML, Vitali P , Santos M, Henry M, Gola K, Rosenberg L,
et al. Two insular regions are diﬀerentially involved in behavioral va riant
FTD and nonﬂuent/agrammatic variant PPA. Cortex. (2016) 74:149–
57. doi: 10.1016/j.cortex.2015.10.012
14. Agosta F , Sala S, V alsasina P , Meani A, Canu E, Magnani G, et a l.
Brain network connectivity assessed using graph theory in frontot emporal
dementia. Neurology. (2013) 81:134–43. doi: 10.1212/WNL.0b013e31829a33f8
15. Agosta F , Galantucci S, V alsasina P , Canu E, Meani A, Marcon e
A, et al. Disrupted brain connectome in semantic variant of
primary progressive aphasia. Neurobiol Aging. (2014) 35:2646–
55. doi: 10.1016/j.neurobiolaging.2014.05.017
16. Daianu M, Mezher A, Mendez MF , Jahanshad N, Jimenez EE, Tho mpson
PM. Disrupted rich club network in behavioral variant frontotemporal
dementia and early-onset Alzheimer’s disease. Hum Brain Mapp. (2016)
37:868–83. doi: 10.1002/hbm.23069
17. Sedeño L, Couto B, García-Cordero I, Melloni M, Baez S, Morales S epúlveda
JP , et al. Brain network organization and social executive perfo rmance
in frontotemporal dementia. J Int Neuropsychol Soc. (2016) 22:250–
62. doi: 10.1017/S1355617715000703
18. Sedeño L, Piguet O, Abrevaya S, Desmaras H, García-Cordero I, Ba ez S,
et al. Tackling variability: a multicenter study to provide a gold-sta ndard
network approach for frontotemporal dementia . Hum Brain Mapp. (2017)
38:3804–22. doi: 10.1002/hbm.23627
19. Filippi M, Basaia S, Canu E, Imperiale F , Meani A, Caso F , et al. Brain network
connectivity diﬀers in early-onset neurodegenerative dementia . Neurology.
(2017) 89:1764–72. doi: 10.1212/WNL.0000000000004577
20. Vijverberg EGB, Tijms BM, Dopp J, Hong YJ, Teunissen CE, Barkh of
F , et al. Gray matter network diﬀerences between behavioral variant
frontotemporal dementia and Alzheimer’s disease . Neurobiol Aging. (2017)
50:77–86. doi: 10.1016/j.neurobiolaging.2016.11.005
21. Mandelli ML, Welch AE, Vilaplana E, Watson C, Battistella G, Brown
JA, et al. Altered topology of the functional speech production
network in non-ﬂuent/agrammatic variant of PPA. Cortex. (2018)
108:252–64. doi: 10.1016/j.cortex.2018.08.002
22. Reyes P , Ortega-Merchan MP , Rueda A, Uriza F , Santamaria-García H, Rojas-
Serrano N, et al. Functional connectivity changes in behavioral, semantic,
and nonﬂuent variants of frontotemporal dementia. Behav Neurol. (2018)
2018:9684129. doi: 10.1155/2018/9684129
23. Saba V , Premi E, Cristillo V , Gazzina S, Palluzzi F , Zanetti O, et a l.
Brain connectivity and information-ﬂow breakdown revealed by a min imum
spanning tree-based analysis of MRI data in behavioral variant frontotemporal
dementia. Front Neurosci. (2019) 13:211. doi: 10.3389/fnins.2019.00211
24. Malpetti M, Carli G, Sala A, Cerami C, Marcone A, Iannaccone S, et a l.
V ariant-speciﬁc vulnerability in metabolic connectivity and resti ng-state
networks in behavioural variant of frontotemporal dementia. Cortex. (2019)
120:483–97. doi: 10.1016/j.cortex.2019.07.018
25. Tao Y , Ficek B, Rapp B, Tsapkini K. Diﬀerent patterns of functio nal
network reorganization across the variants of primary progressive
aphasia: a graph-theoretic analysis. Neurobiol Aging. (2020)
96:184–96. doi: 10.1016/j.neurobiolaging.2020.09.007
26. Zhou J, Greicius MD, Gennatas ED, Growdon ME, Jang JY , Rabin ovici
GD, et al. Divergent network connectivity changes in behaviou ral variant
frontotemporal dementia and Alzheimer’s disease.Brain. (2010) 133:1352–67.
doi: 10.1093/brain/awq075
27. Nigro S, Tafuri B, Urso D, De Blasi R, Frisullo ME, Barulli MR, et al.
Brain structural covariance networks in behavioral variant of front otemporal
dementia. Brain Sci. (2021) 11:192. doi: 10.3390/brainsci11020192
28. Nigro S, Tafuri B, Urso D, De Blasi R, Cedola A, Gigli G, et al. Altered
structural brain networks in linguistic variants of frontotemporal de mentia.
Brain Imaging Behav. (2021) 16:1113–22.
29. Ng ASL, Wang J, Ng KK, Chong JSX, Qian X, Lim JKW, et al.
Distinct network topology in Alzheimer’s disease and behavioral
variant frontotemporal dementia. Alzheimers Res Ther. (2021)
13:13. doi: 10.1186/s13195-020-00752-w
30. Bullmore E, Sporns O. Complex brain networks: graph theoretical analysis
of structural and functional systems. Nat Rev Neurosci. (2009) 10:186–
98. doi: 10.1038/nrn2575
31. He Y , Evans A. Graph theoretical modeling of brain connectivity. Curr Opin
Neurol. (2010) 23:341–50. doi: 10.1097/WCO.0b013e32833aa567
32. Stam CJ, Reijneveld JC. Graph theoretical analysis of complex net works in the
brain. Nonlinear Biomed Phys. (2007) 1:3. doi: 10.1186/1753-4631-1-3
33. van den Heuvel MP , Sporns O. Network hubs in the human brain. Trends
Cogn Sci. (2013) 17:683–96. doi: 10.1016/j.tics.2013.09.012
34. Griﬀa A, Baumann PS, Thiran J-P , Hagmann P. Structural
connectomics in brain diseases. Neuroimage. (2013) 80:515–
26. doi: 10.1016/j.neuroimage.2013.04.056
35. Yun J-Y , Boedhoe PSW, Vriend C, Jahanshad N, Abe Y , Ameis SH, e t al.
Brain structural covariance networks in obsessive-compulsive diso rder: a
graph analysis from the ENIGMA Consortium. Brain. (2020) 143:684–700.
doi: 10.1093/brain/awaa001
36. Brier MR, Thomas JB, Fagan AM, Hassenstab J, Holtzman
DM, Benzinger TL, et al. Functional connectivity and graph
theory in preclinical Alzheimer’s disease. Neurobiol Aging. (2014)
35:757–68. doi: 10.1016/j.neurobiolaging.2013.10.081
37. Nigro S, Riccelli R, Passamonti L, Arabia G, Morelli M, Nisticò R, e t al.
Characterizing structural neural networks in de novo Parkinson disease
patients using diﬀusion tensor imaging. Hum Brain Mapp. (2016) 37:4500–
10. doi: 10.1002/hbm.23324
38. Nigro S, Passamonti L, Riccelli R, Toschi N, Rocca F , V alentino P , et al.
Structural “connectomic” alterations in the limbic system of multiple
Frontiers in Neurology | www.frontiersin.org 8 June 2022 | Volume 13 | Article 910054

Nigro et al. Graph Theory in FTD
sclerosis patients with major depression. Mult Scler. (2015) 21:1003–
12. doi: 10.1177/1352458514558474
39. Sporns O, Zwi JD. The small world of the cerebral cortex. Neuroinform. (2004)
2:145–62. doi: 10.1385/NI:2:2:145
40. Lang EW, Tomé AM, Keck IR, Górriz-Sáez JM, Puntonet CG. Brain
connectivity analysis: a short survey. Comput Intell Neurosci. (2012)
2012:412512. doi: 10.1155/2012/412512
41. Pievani M, Filippini N, van den Heuvel MP , Cappa SF , Frisoni
GB. Brain connectivity in neurodegenerative diseases–from
phenotype to proteinopathy. Nat Rev Neurol. (2014) 10:620–
33. doi: 10.1038/nrneurol.2014.178
42. Malpetti M, Ballarini T , Presotto L, Garibotto V , Tettamanti M, Pe rani D,
et al. Gender diﬀerences in healthy aging and Alzheimer’s dementia : a 18
F-FDG-PET study of brain and cognitive reserve . Hum Brain Mapp. (2017)
38:4212–27. doi: 10.1002/hbm.23659
43. Ballarini T , Iaccarino L, Magnani G, Ayakta N, Miller BL, Jagust WJ, et al.
Neuropsychiatric subsyndromes and brain metabolic network dysfunct ions
in early onset Alzheimer’s disease. Hum Brain Mapp. (2016) 37:4234–
47. doi: 10.1002/hbm.23305
44. Sala A, Caminiti SP , Presotto L, Premi E, Pilotto A, Turrone R, et al. Altered
brain metabolic connectivity at multiscale level in early Parkinson’s disease.
Sci Rep. (2017) 7:4256. doi: 10.1038/s41598-017-04102-z
45. Petersen MV , Lund TE, Sunde N, Frandsen J, Rosendal F , Juul N,
et al. Probabilistic versus deterministic tractography for delineat ion of
the cortico-subthalamic hyperdirect pathway in patients with Parkin son
disease selected for deep brain stimulation. J Neurosurg. (2017) 126:1657–
68. doi: 10.3171/2016.4.JNS1624
46. Mori S, van Zijl PCM. Fiber tracking: principles and strategies - a technical
review. NMR Biomed. (2002) 15:468–80. doi: 10.1002/nbm.781
47. Grier MD, Zimmermann J, Heilbronner SR. Estimating brain
connectivity with diﬀusion-weighted magnetic resonance imag ing:
promise and peril. Biol Psychiatry Cogn Neurosci Neuroimaging. (2020)
5:846–54. doi: 10.1016/j.bpsc.2020.04.009
48. Alexander-Bloch A, Giedd JN, Bullmore E. Imaging structural co-
variance between human brain regions. Nat Rev Neurosci. (2013) 14:322–
36. doi: 10.1038/nrn3465
49. Spreng RN, Turner GR. Structural covariance of the default
network in healthy and pathological aging. J Neurosci. (2013)
33:15226–34. doi: 10.1523/JNEUROSCI.2261-13.2013
50. DuPre E, Spreng RN. Structural covariance networks across the
life span, from 6 to 94 years of age. Netw Neurosci. (2017)
1:302–23. doi: 10.1162/NETN_a_00016
51. Islam MR, Yin X, Ulhaq A, Zhang Y , Wang H, Anjum N, et al. Survey of g raph
based complex brain network analysis using functional and diﬀusio nal MRI.
Am J Appl Sci. (2017) 14:1186–208. doi: 10.3844/ajassp.2017.1186.1208
52. Fornito A, Zalesky A, Bullmore E. Fundamentals of Brain Network Analysis .
Cambridge, MA: Academic Press. (2016), p. 496.
53. Fornito A, Bullmore ET. Connectomics: a new paradigm for
understanding brain disease. Eur Neuropsychopharmacol. (2015)
25:733–48. doi: 10.1016/j.euroneuro.2014.02.011
54. Tewarie P , van Dellen E, Hillebrand A, Stam CJ. The minimum spanning
tree: an unbiased method for brain network analysis. Neuroimage. (2015)
104:177–88. doi: 10.1016/j.neuroimage.2014.10.015
55. Watts DJ, Strogatz SH. Collective dynamics of ‘small-world’ networks. Nature.
(1998) 393:440–2. doi: 10.1038/30918
56. Rubinov M, Sporns O. Complex network measures of brain
connectivity: uses and interpretations. Neuroimage. (2010)
52:1059–69. doi: 10.1016/j.neuroimage.2009.10.003
57. Latora V , Marchiori M. Eﬃcient behavior of small-world networks. Phys Rev
Lett. (2001) 87:198701. doi: 10.1103/PhysRevLett.87.198701
58. Newman MEJ. Modularity and community structure in networks. Proc Natl
Acad Sci USA. (2006) 103:8577–82. doi: 10.1073/pnas.0601602103
59. Boccaletti S, Latora V , Moreno Y , Chavez M, Hwang D-U.
Complex networks: structure and dynamics. Phys Rep. (2006)
424:175–308. doi: 10.1016/j.physrep.2005.10.009
60. Oldham S, Fornito A. The development of brain network hubs. Dev Cogn
Neurosci. (2019) 36:100607. doi: 10.1016/j.dcn.2018.12.005
61. Afshari S, Jalili M. Directed Functional networks in Alzheimer’ s disease:
disruption of global and local connectivity measures. IEEE J Biomed Health
Inform. (2017) 21:949–55. doi: 10.1109/JBHI.2016.2578954
62. John M, Ikuta T , Ferbinteanu J. Graph analysis of structural bra in networks in
Alzheimer’s disease: beyond small world properties.Brain Struct Funct. (2017)
222:923–42. doi: 10.1007/s00429-016-1255-4
63. Mears D, Pollard HB. Network science and the human brain: using gra ph
theory to understand the brain and one of its hubs, the amygdala, i n health
and disease. J Neurosci Res. (2016) 94:590–605. doi: 10.1002/jnr.23705
64. Meeter LH, Kaat LD, Rohrer JD, van Swieten JC. Imaging and ﬂui d
biomarkers in frontotemporal dementia. Nat Rev Neurol. (2017) 13:406–
19. doi: 10.1038/nrneurol.2017.75
65. Hutchison RM, Womelsdorf T , Allen EA, Bandettini PA,
Calhoun VD, Corbetta M, et al. Dynamic functional connectivity :
promise, issues, and interpretations. Neuroimage. (2013) 80:360–
78. doi: 10.1016/j.neuroimage.2013.05.079
66. Preti MG, Bolton TA, V an De Ville D. The dynamic
functional connectome: State-of-the-art and perspectives.
Neuroimage. (2017) 160:41–54. doi: 10.1016/j.neuroimage.20
16.12.061
Conﬂict of Interest: The authors declare that the research was conducted in the
absence of any commercial or ﬁnancial relationships that could be c onstrued as a
potential conﬂict of interest.
Publisher’s Note:All claims expressed in this article are solely those of the authors
and do not necessarily represent those of their aﬃliated organizat ions, or those of
the publisher, the editors and the reviewers. Any product that may b e evaluated in
this article, or claim that may be made by its manufacturer, is not gua ranteed or
endorsed by the publisher.
Copyright © 2022 Nigro, Filardi, T afuri, De Blasi, Cedola, Gigli a nd Logroscino.
This is an open-access article distributed under the terms o f the Creative Commons
Attribution License (CC BY). The use, distribution or repro duction in other forums
is permitted, provided the original author(s) and the copyri ght owner(s) are credited
and that the original publication in this journal is cited, in accordance with accepted
academic practice. No use, distribution or reproduction is permitted which does not
comply with these terms.
Frontiers in Neurology | www.frontiersin.org 9 June 2022 | Volume 13 | Article 910054