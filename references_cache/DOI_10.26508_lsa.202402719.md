---
reference_id: DOI:10.26508/lsa.202402719
title: PRDM16 determines specification of ventricular cardiomyocytes by suppressing alternative cell fates
authors:
- Jore Van Wauwe
- Alexia Mahy
- Sander Craps
- Samaneh Ekhteraei-Tousi
- Pieter Vrancaert
- Hannelore Kemps
- Wouter Dheedene
- Rosa Doñate Puertas
- Sander Trenson
- H. Llewelyn Roderick
- Manu Beerens
- Aernout Luttun
journal: Life Science Alliance
year: '2024'
doi: 10.26508/lsa.202402719
content_type: full_text_pdf
is_preprint: false
full_text_attempted: true
full_text_provider: openalex
full_text_url: "https://www.life-science-alliance.org/content/lsa/7/12/e202402719.full.pdf"
oa_status: gold
license: cc-by
local_pdf_path: files/DOI_10.26508_lsa.202402719.pdf
---

# PRDM16 determines specification of ventricular cardiomyocytes by suppressing alternative cell fates
**Authors:** Jore Van Wauwe, Alexia Mahy, Sander Craps, Samaneh Ekhteraei-Tousi, Pieter Vrancaert, Hannelore Kemps, Wouter Dheedene, Rosa Doñate Puertas, Sander Trenson, H. Llewelyn Roderick, Manu Beerens, Aernout Luttun
**Journal:** Life Science Alliance (2024)
**DOI:** [10.26508/lsa.202402719](https://doi.org/10.26508/lsa.202402719)

## Content

PRDM16 is a transcription factor with histone methyltransferase activity expressed at the earliest stages of cardiac development. Pathogenic mutations in humans lead to cardiomyopathy, conduction abnormalities, and heart failure. PRDM16 is specifically expressed in ventricular but not atrial cardiomyocytes, and its expression declines postnatally. Because in other tissues PRDM16 is best known for its role in binary cell fate decisions, we hypothesized a similar decision-making function in cardiomyocytes. Here, we demonstrated that cardiomyocyte-specific deletion of
                    Prdm16
                    during cardiac development results in contractile dysfunction and abnormal electrophysiology of the postnatal heart, resulting in premature death. By combined RNA+ATAC single-cell sequencing, we found that PRDM16 favors ventricular working cardiomyocyte identity, by opposing the activity of master regulators of ventricular conduction and atrial fate. Myocardial loss of PRDM16 during development resulted in hyperplasia of the (distal) ventricular conduction system. Hence, PRDM16 plays an indispensable role during cardiac development by driving ventricular working cardiomyocyte identity.

Research Article
PRDM16 determines speci ﬁcation of ventricular
cardiomyocytes by suppressing alternative cell fates
Jore Van Wauwe 1 , Alexia Mahy 1 , Sander Craps 1 , Samaneh Ekhteraei-Tousi 2 , Pieter Vrancaert 1,
Hannelore Kemps 1 , Wouter Dheedene 1 , Rosa Doñate Puertas 2 , Sander Trenson 3 , H. Llewelyn Roderick 2 ,
Manu Beerens 4,5 , Aernout Luttun 1
PRDM16 is a transcription factor with histone methyltransferase
activity expressed at the earliest stages of cardiac development.
Pathogenic mutations in humans lead to cardiomyopathy, con-
duction abnormalities, and heart failure. PRDM16 is speciﬁ cally
expressed in ventricular but not atrial cardiomyocytes, and its
expression declines postnatally. Because in other tissues PRDM16
is best known for its role in binary cell fate decisions, we hy-
pothesized a similar decision-making function in cardiomyocytes.
Here, we demonstrated that cardiomyocyte-speci ﬁc deletion of
Prdm16 during cardiac development results in contractile dys-
function and abnormal electrophysiology of the postnatal heart,
resulting in premature death. By combined RNA+ATAC single-cell
sequencing, we found that PRDM16 favors ventricular working
cardiomyocyte identity, by opposing the activity of master reg-
ulators of ventricular conduction and atrial fate. Myocardial loss
of PRDM16 during development resulted in hyperplasia of the
(distal) ventricular conduction system. Hence, PRDM16 plays an
indispensable role during cardiac development by driving ven-
tricular working cardiomyocyte identity.
DOI 10.26508/lsa.202402719 | Received 14 March 2024 | Revised 6 September
2024 | Accepted 9 September 2024 | Published online 20 September 2024
Introduction
The mammalian heart is a complex organ, composed of four
morphologically, molecularly, and functionally diverse chambers.
Atria and ventricles each host cardiomyocytes (CMs) with distinct
expression pro ﬁles and different electrophysiological properties
(Cao et al, 2023 ; Kane & Terracciano, 2017 ; Ng et al, 2010 ). The atria
eject blood into the ventricles, while the latter pump the blood
through our lungs and body. This pumping activity is ensured by
ventricular working CMs, which continuously contract in sequence
from the cardiac apex to its base upon electrical stimulation. This
pattern is coordinated by cells from the cardiac conduction system,
which display different features than the contractile working CMs
(Munshi, 2012 ). The ventricular conduction system (VCS) is re-
sponsible for the rapid propagation of the electrical signal through
the ventricles. The proximal VCS encompasses the bundle of His
located in the septum, which splits at the base of the heart in the
left and right bundle branches. These bundle branches each ramify
in a complex network of subendocardial Purkinje ﬁbers (PFs),
known as the distal VCS (Choquet et al, 2021 ). Although differen-
tiation of the proximal VCS is complete at ventricular septation, the
formation of the distal Purkinje system occurs in two phases
whereby an initial scaffold is formed early on, followed by a phase
of recruitment of additional PFs by continuous differentiation from
trabecular precursors, a process that persists until birth (Fig S1A ; all
supplemental online items are designated “S”)( Mikawa et al, 2003 ;
Choquet et al, 2021 ). The trabecular protrusions gradually disap-
pear, whereas the fast proliferating compact myocardial layer
expands and both the ventricular wall and VCS mature (MacGrogan
et al, 2018 ; Lupu et al, 2020 ). Defects in the speci ﬁcation and
morphogenesis of the VCS cause life-threatening syndromes, in-
cluding Brugada and long-QT syndromes, both characterized by
lethal cardiac arrhythmias (Haissaguerre et al, 2016; Choquet et al,
2021). Hence, it is important to understand the cellular and mo-
lecular mechanisms that underlie the speci ﬁcation and formation
of cardiac wall development.
This heterogeneity among CMs is largely established by cell fate
decisions governed and monitored by transcription factor (TF)
networks that tightly orchestrate spatial and temporal regulation of
gene expression, through either DNA interactions or chromatin
remodeling ( Christoffels & Moorman, 2009 ; Shekhar et al, 2018 ;
Pawlak et al, 2019). Over the last decades, many TFs involved in such
decisions in CMs have been identi ﬁed, including TBX5, a master
regulator of atrial and conduction cell fates (Pawlak et al, 2019 ;
Choquet et al, 2021 ; Cao et al, 2023 ). Positive regulatory domain –
containing protein (PRDM)16, a member of the PRDM family of TFs
1Center for Molecular and Vascular Biology, Department of Cardiovascular Sciences, KU Leuven, Leuven, Belgium 2Laboratory of Experimental Cardiology, Department of
Cardiovascular Sciences, KU Leuven, Leuven, Belgium 3Cardiology Lab, Department of Cardiovascular Sciences, KU Leuven, Leuven, Belgium 4Institute for Clinical
Chemistry and Laboratory Medicine, Medizinische Klinik und Poliklinik Universit ¨atsklinikum Hamburg-Eppendorf, Hamburg, Germany 5German Centre of Cardiovascular
Research (DZHK), Partner Site Hamburg, Luebeck, Kiel, Hamburg, Germany
Correspondence: aernout.luttun@kuleuven.be
©2 0 2 4Van Wauwe et al. https://doi.org/10.26508/lsa.202402719 vol 7 | no 12 | e202402719 1o f2 5
on 31 August, 2026life-science-alliance.org Downloaded from 
http://doi.org/10.26508/lsa.202402719Published Online: 20 September, 2024 | Supp Info: 

with methyltransferase activity, is a TF speci ﬁcally expressed in
ventricular CMs while absent in atria (Bjork et al, 2010 ; Arndt et al,
2013; Wu et al, 2022 ). Its asymmetric expression pattern in the heart
suggests a cell fate decision-making role. Indeed, PRDM16 was
recently put forward as a positive regulator of ventricular compact
CM fate, highlighting for the ﬁrst time the contribution of PRDM16 to
the speci ﬁcation and heterogeneity among CMs ( Wu et al, 2022 ).
Accordingly, pathogenic mutations lead to left ventricular non-
compaction cardiomyopathy (LVNC), dilated cardiomyopathy, and
ventricular conduction abnormalities in patients (Arndt et al, 2013 ;
Harms et al, 2014; Long et al, 2017; van Waning et al, 2018; Mazzarotto
et al, 2021 ; Wu et al, 2022 ; Kramer et al, 2023 ). Loss-of-function
studies in mice resulted in LVNC, ventricular conduction defects,
and hypertrophic cardiomyopathy ( Cibi et al, 2020 ; Nam et al, 2020 ;
Kang et al, 2022 ; Wu et al, 2022 ; Kramer et al, 2023 ; Sun et al, 2023 ;
Kuhnisch et al, 2024 ). However, as a result of using different Cre
driver strains to induce PRDM16 loss, the phenotypic outcome of
these animal studies was highly heterogeneous ranging from
early postnatal lethality to cardiac dysfunction only acquired in
adulthood or after an additional challenge ( Cibi et al, 2020 ; Nam
et al, 2020 ; Wu et al, 2022; Kramer et al, 2023 ). In these studies,
expression pro ﬁling has been performed either before birth or
during the adult stage. Therefore, the transcriptional changes
governed by PRDM16 during early postnatal cardiac development,
when myocardium is still maturing and cell fate decisions need to
be maintained, remain poorly characterized ( Li et al, 2022 ; Sweat
et al, 2023 ).
We and others have previously shown the asymmetric expres-
sion pattern of PRDM16 in endothelial cells (ECs) and adipocytes,
which coincides with its role in cell fate decision-making. PRDM16
favors an arterial EC and brown adipocyte cell fate over venous ECs
and white adipocytes, respectively (Seale et al, 2007 ; Aranguren
et al, 2013 ; Craps et al, 2021 ; Thompson et al, 2023 ; Van Wauwe et al,
2024 Preprint). Mechanistic studies further revealed that PRDM16
not only exerts its effects on gene expression, and hence cell fate
decisions, via direct binding to th e promoter regions of its target
genes, but primarily indirectly v ia interaction with other DNA
binding TFs and by altering the accessibility of chromatin
through its methylating activity or recruitment of chromatin-
modifying enzymes ( Kajimura et al, 2008 ; Harms et al, 2014; Li
et al, 2015 ; Cibi et al, 2020 ; Jiang et al, 2022 ; Wu et al, 2022 ).
 It,
however, remains unknown whether and how PRDM16 orches-
trates cardiac development and function through modi ﬁcation
of chromatin accessibility, rather than transcriptional activity, at
deﬁned loci.
Here, we applied a combined RNA and Assay for Transposase-
Accessible Chromatin (ATAC) sequencing approach at single-cell
resolution to resolve cellular and molecular mechanisms governed
by PRDM16 in heart development at 7 d after birth. We found that in
accordance with its asymmetric myocardial expression pattern,
PRDM16 is involved in a decision process whereby it favors ven-
tricular contractile CM cell fates through opposing the activity of
master regulators of atrial and conduction cell fates. Myocardial
deletion of Prdm16 during development resulted in hyperplasia of
the (distal) VCS, providing a potential explanation for the sudden
death of PRDM16-de ﬁcient mice we observed between 1 and 3 wk
after birth.
Results
PRDM16 loss in CMs during development causes early-onset
cardiomyopathy
PRDM16 expression in the developing mouse heart was evident
in the compact and trabecular ventricular myocardium from
embryonic day (E)10.5 onward, but was notably absent from the
atria, as previously reported ( Fig S1A –D)( Bjork et al, 2010 ; Arndt
et al, 2013 ; Litvinukova et al, 2020 ; Wu et al, 2022 ). At E14.5 and
E17.5, PRDM16 expression became more restricted to CMs of the
compact myocardium ( Fig S1E and F). Immunostaining at
postnatal day (P)7 revealed that PRDM16 expression in the
ventricles was present in CMs and in coronary arterial ECs and
smooth muscle cells (SMCs) ( Fig S1G and H ). Notably, the ex-
pression of PRDM16 in the heart signi ﬁcantly declined after
birth, as shown by Wu et al (2022) . To study the role of PRDM16
during cardiac development, we generated mice with
cardiomyocyte-speci ﬁc Prdm16 deletion from early cardiac
development onward, by inter-crossing an Sm22 α-Cre driver
line with mice harboring two ﬂoxed Prdm16 exon 9 alleles ( Fig
S2A), resulting in Prdm16
lox/lox ;Sm22 α-Cre Tg/+ or Prdm16 lox/lox ;
Sm22 α-Cre +/+ offspring (referred to as Prdm16 cKO mice and
Prdm16 WT littermate controls, respectively). Sm22 α is transiently
expressed in the mouse (pre)myocardium between E8.0 and
E12.5 ( Fig S1A )( Li et al, 1996 ). Sm22 α-Cre driver activity faithfully
reported the endogenous Sm22 α expression pattern in eGFP
reporter mice, as evident from eG FP expression throughout the
myocardium ( Fig S2B and C). At P7, immunohistochemistry,
RT– qPCR, and immunoblotting demonstrated that our strategy
successfully eliminated PRDM16 expression in CMs (with an
efﬁciency at P7 of 93% ± 1%, n =4 ; Fig S1I, K –M). PRDM16 loss was
also evident in coronary artery SMCs and arterial SMCs in P7
brains and lungs, but not in arterial ECs, bronchiolar epithelial
cells, and various cells in the choroid plexus known to express
PRDM16 ( Figs S1J and S2D–F)( Shimada et al, 2017 ; Strassman
et al, 2017 ; Fei et al, 2019 ; Craps et al, 2021 ).
In contrast to the 100% mortality by P7 previously reported for
Prdm16 deletion in CMs from E7.5 onward by cTnT-Cre and Xmlc2-
Cre (Wu et al, 2022), we did not observe notable losses of Prdm16
cKO
pups at that time, as shown by a nearly Mendelian distribution
(Table 1). However, Prdm16
cKO mice had lower body weights (Table
S1), a signi ﬁcantly reduced ejection fraction (EF), and CM hyper-
trophy compared with their Prdm16WT littermates (Fig 1A and B and
Table S1). Prdm16cKO LVs featured signiﬁcant up-regulation of stress
and hypertrophy-related marker genes, that is, Nppa and Nppb,
encoding the atrial and brain natriuretic peptide, respectively (Fig
1C). Unlike their Prdm16
WT littermates, Prdm16cKO offspring had
clear signs of perivascular and interstitial ﬁbrosis ( Fig 1D). Like in
humans and zebra ﬁsh ( Arndt et al, 2013 ; Hong et al, 2014 ; van
Waning et al, 2018 ; Kramer et al, 2023 ), Prdm16cKO pups showed
signiﬁcant signs of a reduced compact LV, together with excessive
trabeculation (Figs 1E and S3). Moreover, already at P7, Prdm16cKO
pups showed an aberrant electrocardiogram (ECG), that is, a pro-
longed QRS duration ( Fig 1F), as previously described at later time
points in mice and humans (Hong et al, 2014; Nam et al, 2020), and a
PRDM16 determines cardiomyocyte fate Van Wauwe et al. https://doi.org/10.26508/lsa.202402719 vol 7 | no 12 | e202402719 2o f2 5

signiﬁcantly increased QRS amplitude that accords with LV hy-
pertrophy. Although our Sm22α -Cre driver also eliminated PRDM16
expression in SMCs (Fig S1H versus Fig S1J), SMC coverage was not
affected in Prdm16cKO hearts ( Fig S1N ), suggesting that the earlier
PRDM16 loss in CMs ( Fig S1A ) was the primary culprit for the ob-
served phenotypic aberrations. Thus, de ﬁciency of PRDM16 in CMs
caused severe signs of cardiomyopathy early on.
Prdm16 deletion in CMs during development leads to premature
death or progressive cardiomyopathy
Although nearly all Prdm16 cKO mice were alive at P7, 60% of both
male and female Prdm16 cKO mice died by weaning age (3 wk),
after which no further losses were observed ( Table 1 ). We then
monitored the cardiac phenotype of the surviving adult mice,
which revealed progressive signs of heart failure to a similar
extent in both male and female mice ( Fig S4 and Table S1). Both
at 8 and at 16 wk of age, Prdm16
cKO mice showed signiﬁ cant
diastolic and systolic dysfunctio n, as evidenced by an increased
E/e9 ratio and a lowered EF, respectively (Fig S4A and E and Table
S1). Prdm16 cKO hearts had dilated LVs, as evidenced from sig-
niﬁcantly increased LV internal diameter and decreased pos-
terior wall thickness obtained at end-systole (LVIDs and LVPWs,
respectively; Table S1), which was more pronounced at 16 wk of
age. Nppa and Nppb expression was signi ﬁcantly up-regulated in
the LVs of adult Prdm16
cKO mice ( Fig S4B and F ). Furthermore,
Prdm16 cKO mice also featured signi ﬁcant perivascular ﬁbrosis at
8 and 16 wk, where the latter time point also featured signi ﬁcant
interstitial ﬁbrosis ( Fig S4C and G ). Like P7 pups, surviving adult
Prdm16 cKO mice showed a signi ﬁcantly prolonged QRS duration
and an increased QRS amplitude, while maintaining a normal
heart rate ( Fig S4D and H and Table S1).
PRDM16 loss in CMs during development perturbs the cardiac
cellular landscape
Because Prdm16
cKO mice started to die beyond P7 and this time
point has recently been proposed to represent a transition state
that is essential for CM subtype speci ﬁcation and subsequent
maturation (Li et al, 2022), we chose this transition state to look into
the effect of PRDM16 on the cellular composition of the heart by
single-nucleus (sn)RNA/ATACseq (Fig 2A ). We chose to focus our
analysis on the LV only given the restricted expression of PRDM16 in
the ventricles (our study and those by others [Bjork et al, 2010; Arndt
et al, 2013; Wu et al, 2022]) and because of the predominant effect of
pathogenic PRDM16 mutations leading to LVNC in patients (Arndt
et al, 2013; Delplancq et al, 2020; Mazzarotto et al, 2021). After pooling
four samples per condition and stringent quality control (Table S2),
5,468 nuclei remained. Unsuperv ised low-resolution clustering
and dimensionality reduction on the integrated Prdm16
cKO and
Prdm16WT RNA/ATACseq datasets resolved the major cell types of
the LV, that is, 2 clusters of CMs including Myh6+ mature (m)CMs and
Top2a+ proliferating (p)CMs, and additional non-CM cell types in-
cluding Dcn+ ﬁbroblasts (FBs), Cdh5+ ECs, Pdgfrb+ mural cells (MCs),
and Csf1r+ immune cells (ICs; Fig 2A and B )( Wei et al, 2011; Hu et al,
2018; Asp et al, 2019 ; Cui et al, 2020 ; Muhl et al, 2020 ; Tucker et al,
2020). Although the proportions of these fractions closely re ﬂected
the expected size at this postnatal stage in Prdm16WT hearts ( Hu
et al, 2018 ; Cui et al, 2020 ), the relative contributions of these
populations shifted in Prdm16cKO hearts ( Fig 2C ). Indeed, in ac-
cordance with the observed ﬁbrosis, the proportion of FBs in-
creased signiﬁcantly and their expression proﬁle changed toward a
myoﬁbroblast-like signature (Table S3), whereas mCM nuclei were
signiﬁcantly reduced in numbers, as con ﬁrmed by in situ assess-
ment by immunostaining on an independent set of mice ( Fig 2D ).
Smaller shifts were seen in the vascular cellular landscape, with a
slight increase in the EC compartment and a decrease in the MC
compartment (Fig 2C ).
To gain a greater insight into the cellular landscape shifts, in-
cluding the identi ﬁcation of different CM subpopulations featuring
unique marker genes, we re-clustered the total CM nucleus pop-
ulation ( Fig S5A and Table S3). We now found 3 CM subclusters, of
which the largest subcluster (0) expressed several markers of
mature ventricular CMs (including Ryr2; Fig S5A and Table S3)
(Pallante et al, 2010 ; Goodyer et al, 2019 ; Cao et al, 2023 ). Inter-
estingly, 90.3% of Prdm16
WT nuclei were represented in this larger
mature CM subcluster. CM subcluster (1) represented a “mixed”
nature as it was marked not only by genes known to be typical for
the VCS (e.g., Slc6a6, Cacna2d2,a n d Ryr3; Table S3) but also by
genes known as atrial CM genes (e.g., Myl4 and EphA4; Table S3)
(Goodyer et al, 2019 ; Cao et al, 2023 ). Prdm16WT nuclei only rep-
resented 1.2% of this atrial/VCS cluster. Finally, the smallest CM
subcluster (2) exhibited a very clear “proliferation ” gene signature,
including Top2a. We also re-clustered the other main cell types
(Fig S5A and Table S3) and examined the expression of Prdm16
within each subcluster. This analysis detected the presence of
Prdm16 in Prdm16
WT nuclei in all CM subclusters, as well as in the
SMCs and in arterial ECs, in accordance with the expression
pattern we documented by IF staining above ( Figs S1G and H , S2D-
F,a n d S5B).
Table 1. Genotype distribution.
Genotype Prdm16WT Prdm16cKO
Seven days of age (P7)
Expected ratio (%) 50 50
Observed ratio (%) 52 48
Observed absolute n = 42 n = 39
Post-weaning (all)
Expected ratio (%) 50 50
Observed ratio (%) 71 29
Observed absolute n = 622 n = 253
Post-weaning (male)
Expected ratio (%) 50 50
Observed ratio (%) 71 29
Observed absolute n = 334 n = 135
Post-weaning (female)
Expected ratio (%) 50 50
Observed ratio (%) 71 29
Observed absolute n = 288 n = 118
PRDM16 determines cardiomyocyte fate Van Wauwe et al. https://doi.org/10.26508/lsa.202402719 vol 7 | no 12 | e202402719 3o f2 5

Figure 1. PRDM16 loss during cardiac development causes early-onset cardiomyopathy.
(A) Ejection fraction (EF) of 7-d-old (P7) mouse pups expressed in % ( n = 12/12). WT, wild-type; cKO, Prdm16 conditional knockout. (B) Representative pictures of cross-
sections stained with LAMININ (red) and TO-PRO-3 (blue) and quantitative analysis of the cardiomyocyte size of P7 hearts expressed in μm2 (n = 7/6). (C) mRNA levels of
cardiac stress markers Nppa (n = 8/11) and Nppb (n = 7/12), measured in P7 heart apex. (D) Representative images of Sirius Red– stained cross-sections revealing ﬁbrosis in
PRDM16 determines cardiomyocyte fate Van Wauwe et al. https://doi.org/10.26508/lsa.202402719 vol 7 | no 12 | e202402719 4o f2 5

Interestingly, the overall loss of CMs in Prdm16cKO mice could
mainly be attributed to a remarkable 2.7-fold reduction of the
mature CM Prdm16cKO cluster, whereas the subcluster with a mixed
atrial/VCS signature was strikingly overrepresented in Prdm16cKO
hearts (i.e., ~30-fold increase; Fig S5A). The latter may partly account
for the aberrant ECG of Prdm16cKO mice (Fig 1F). Altogether, deletion
of Prdm16 during ventricular wall development altered the cellular
landscape of the heart aligning with the aberrant cardiac
phenotype.
PRDM16 loss in CMs triggers changes in gene expression and
chromatin accessibility related to hypertrophy, metabolism,
conduction, and TGFβ signaling
We next performed a differential analysis of RNA expression and
chromatin accessibility between Prdm16
cKO and Prdm16WT CMs to
better understand the molecular mechanisms driving the observed
cardiac phenotypes. It was remarkable that ~79% of the mature CM
cluster 0 represented Prdm16
WT nuclei, whereas ~97% of nuclei from
the “mixed” cluster originated from Prdm16cKO hearts (Fig 3A and B).
In contrast, Prdm16cKO did not affect the size of the cluster rep-
resenting proliferating CMs ( Fig 3B ). Because the main CM sub-
clusters were almost exclusively related to one of the genotypes
(and hence the contamination of cells from the other genotype
would have a limited impact on differential gene expression), we
decided to look at differentially expressed genes (DEGs) and dif-
ferentially accessible regions (DARs) of the CM cluster in total, that
is, by comparing Prdm16
cKO versus Prdm16WT CMs ( Fig 3B ). This
revealed 1,665 DEGs (1,137 and 528, higher or lower expressed in
Prdm16
cKO mice, respectively; Fig 3C and Table S4). Upon screening
of the DEG lists, a number of clear traits caused by PRDM16 de ﬁ-
ciency were manifest. First, in accordance with the observed CM size
increase ( Fig 1B ), higher expressed DEGs were associated with
cardiac hypertrophy (e.g., Nppa, Gpx3, Sparc; Fig 3C and Table S4)
(Farrell et al, 2018 ; Cibi et al, 2020 ; Vigil-Garcia et al, 2021 ). Second,
lower expressed genes were related to fatty acid (FA) metabolism
(e.g., Lpl, Ppara, Cpt1a; Fig 3C and Table S4), re ﬂecting an energy
source switch in these cells of the failing heart away from FA. Third,
the top higher (i.e., Fgf12, encoding a non-canonical FGF that does
not bind FGF receptors but associates with sodium channels) and
lower expressed (i.e., Kcnd2, encoding the potassium channel
subunit K
v4.2) genes are both related to ion channels, potentially
involved in the aberrant cardiac conduction (Table S4). Finally, in
line with previous ﬁndings (Arndt et al, 2013 ; Kodo et al, 2016; Nam
et al, 2020 ; Sun et al, 2023 ), we also observed higher expression in
(target) genes from the increased TGF β signaling pathway (e.g.,
Spred1, Smad2, Tgfb2; Fig 3C and Table S4); however, a similar
proportion of (target) genes was lower expressed (e.g., Ltbp1, Itgb6,
Tgfbr3; Fig 3C and Table S4).
Likewise, we identiﬁed 718 DARs, of which 501 and 217 were more
and less accessible in Prdm16
cKO mice, respectively (Fig 3D and
Table S5). Annotation of altered chromatin regions revealed that
this occurred mostly at intronic and intergenic, but also at promoter
locations (Fig 3D ). As more DEGs were higher expressed and more
DARs displayed an open chromatin structure in the absence of
PRDM16, our results suggest that PRDM16 mainly acts as a tran-
scriptional repressor in CMs. Gene ontology (GO) analysis on the
more highly expressed DEGs and on the open DARs revealed en-
richment for GO terms related to “heart growth ” and “(dilated)
cardiomyopathy,” and interestingly also identiﬁed terms associated
with “chamber type, ”“ conduction system, ” and “arrhythmias,” the
last two compatible with the aberrant ECG (Fig 3E and Table S6). On
the contrary, many GO terms related to fat(ty acid) metabolism/
oxidation were identi ﬁed among the down-regulated DEGs and
genes associated with more closed DARs (Table S6). Additional
annotation analysis using ToppGene con ﬁrmed these ﬁndings in-
cluding the appearance of “cardiac conduction system devel-
opment ” and “bundle of His to Purkinje myocyte signaling ”
among the functional terms associated with higher expressed
DEGs, and the extraction of “fatty acid oxidation ” and “heart
development ” and “regulation of cardiac muscle contraction ” as
functional terms related to the lower expressed genes (Table S6).
Altogether, PRDM16 loss caused expression/chromatin accessi-
bility changes in CMs in line with our observed cardiac phenotype
and previous studies.
PRDM16 loss in CMs causes a shift toward atrial and conduction
cell fates
A deeper analysis of the DEGs unveiled that many of the up-
regulated DEGs encoded known atrial markers (e.g., Fgf12, Myl4;
Fig 4A and Table S4) or (ventricular) conduction markers (i.e., Ryr3,
Cacna2d2; Fig 4B and Table S4) (Hartung et al, 1997; Koibuchi & Chin,
2007; Ng et al, 2010; Wiencierz et al, 2015; DeLaughter et al, 2016; Kane
& Terracciano, 2017 ; Litvinukova et al, 2020 ; Nam et al, 2020 ; Tucker
et al, 2020 ; Wu
et al, 2022 ). In support of this fate switch, we
compared our DEGs with published gene expression signatures of
CMs from atria (Cao et al, 2023 ) or the conduction system (Shekhar
et al, 2018). We found that 312 and 287 out of 1,665 DEGs were part of
the published atrial or conduction system signatures, of which the
majority (273 or 87.5% and 246 or 85.7%, respectively) were higher
expressed after Prdm16 deletion ( Fig 4C and D and Tables S4 and
S7). Because the published atrial and conduction signatures
showed some overlap, we ﬁltered out these common genes after
which 216 and 191 unique atrial and unique conduction DEGs
remained. Again, most of the unique marker genes (i.e., 84.7% of
atrial and 81.7% of conduction DEGs) were signi ﬁcantly higher
expressed in Prdm16
cKO CMs, demonstrating that there was a
P7 mouse hearts, insets showing perivascular (PV; bright ﬁeld, top) and interstitial (IS; bright ﬁeld, bottom left ; polarized light, bottom right ) ﬁbrosis, and bar graphs
showing the quantitative analysis of PV and IS ﬁbrosis. PV ﬁbrotic area was corrected for the smooth muscle cell area of the vessel and expressed in arbitrary units (AU; n =
11/7). (E) Representative images of Natriuretic Peptide Receptor 3 –stained transversal sections marking the endocardial lining and quantitative analysis of the compact
myocardial wall thickness expressed in μm( right); level 1 represents the base, and level 2 represents the apex of the left ventricle (LV;n = 3/4). The yellow line delineates
the trabecular (T)/compact (C) border. RV: right ventricle. (F) Average surface electrocardiogram measured in P7 mice in rest expressed in mV over time (in msec). Bar
graphs show quantitative analysis of QRS duration ( n = 12/7) and amplitude ( n = 9/6). Quantitative data are expressed as the mean ± SEM; * P <0 . 0 5b yat test. Scale bars:
20 μm (B), 500 μm (D, E).
PRDM16 determines cardiomyocyte fate Van Wauwe et al. https://doi.org/10.26508/lsa.202402719 vol 7 | no 12 | e202402719 5o f2 5

Figure 2. PRDM16 loss in CMs during development perturbs the cardiac cellular landscape.
(A) Experimental setup of droplet-based single-nucleus multiome RNA and ATACsequencing (10x Genomics) experiment on pooled left ventricles (LVs) of 7-d-old (P7)WT (n =4 )
or Prdm16 conditional knockout (cKO; n = 4) mouse hearts. Nuclei were isolated and subjected to combined single-nucleus RNA and ATAC sequencing (left). Uniform Manifold
Approximation and Projection dimensional reduction panels are shown for each separate modality (middle), as well as after integration (top right) and splitting per genotype
(bottom right). (B) Dot plot representing major cellpopulations (clusters) identiﬁed in the heart on the x-axis with their marker genes represented on the y-axis. Color code of
different clusters matches that of the integrated Uniform Manifold Approximation and Projection in (A). The size of the dots represents the percentage of cells expressing the
marker gene; the dot color indicates average expression levels expressed in log(fold change). The number of nuclei per cluster is indicated below theplot.(C) Bar graph representing
the cellular proportions for each cluster inWT versuscKO samples. mCM, mature cardiomyocyte; pCM, proliferating cardiomyocyte; FB,ﬁbroblast; EC, endothelial cell; MC, mural
cell; IC, immune cell. To calculate marker genes, a Wilcoxon test was used with log(fold change) threshold = 0,Padjusted< 0.05; to calculate cell proportion differences, Fisher’se x a c t
test was used with FDR < 0.05.(D) Representative images of PCM1-stained cross-sections ofWT and cKO P7 hearts (left) and corresponding quantiﬁcation of cell proportion expressed
as % ( right; n = 3/4). Quantitative data are expressed as the mean ± SEM; * P <0 . 0 5b ya t test. Scale bars: 20 μm( D ) .
PRDM16 determines cardiomyocyte fate Van Wauwe et al. https://doi.org/10.26508/lsa.202402719 vol 7 | no 12 | e202402719 6o f2 5

Figure 3. PRDM16 loss in CMs triggers changes in gene expression and chromatin accessibility related to hypertrophy, metabolism, conduction, and TG Fβ signaling.
(A, B) Uniform Manifold Approximation and Projection (UMAP) representing re-clustered cardiomyocyte (CM) cellular landscape identifying three major cell clusters (A)
and the same UMAP split by genotype ((B), left;r e d :WT CMs; blue: Prdm16-deﬁcient CMs [cKO]). (A, B) Bar graph ((B), right) shows proportions of WT (red) and cKO (blue)
CMs represented in subclusters 0, 1, and 2 from panel (A). (C) Bar graph showing the numbers of differentially expressed genes (DEGs) identi ﬁed in CMs. Green and purple
bars represent the number of higher and lower expressed genes, respectively. Volcano plots show higher expressed (green) or lower expressed (purple) DEGs in CMs,
PRDM16 determines cardiomyocyte fate Van Wauwe et al. https://doi.org/10.26508/lsa.202402719 vol 7 | no 12 | e202402719 7o f2 5

double fate shift upon Prdm16 deletion (Fig S6A and B and Tables S4
and S7). Vice versa, CMs from Prdm16cKO hearts displayed signi ﬁ-
cantly reduced expression levels of genes characteristic of ven-
tricular ( Cao et al, 2023 ) or working CMs ( Shekhar et al, 2018 )( Fig
4A–D and Tables S4 and S7), suggesting loss of PRDM16 triggers a
shift away from ventricular working CM fate. Also at the chromatin
level, and in line with the transcriptomic remodeling, most genes
related to more open DARs were part of the atrial or conduction
signature, whereas most genes related to closed DARs were part of
the ventricular working CM gene signature (Fig S6C and D and
Tables S5 and S8). The expression pattern of several atrial, ven-
tricular, working, or conduction genes was validated by RT –qPCR or
at the protein level by immunostaining or immunoblotting (Fig
S7A–D).
The remarkable shift toward a VCS signature was in part due to
an increase in the proportion of PFs. Indeed, when increasing the
resolution of CM clustering, we identiﬁed a small CM subpopulation
(cluster 7) with a signi ﬁcantly higher expression of PF genes (e.g.,
Cntn2, Cpne5), which are also signi ﬁcantly increased in Prdm16
cKO
CMs compared with Prdm16WT cells (Figs 4E and S8A and Table S3).
The proportion of this PF cluster increased ~5-fold from 0.5% in
Prdm16WT CMs to 2.3% in PRDM16-de ﬁcient CMs ( Fig S8A and B and
Table S3). The increase in PFs was con ﬁrmed at the protein level by
the signi ﬁcantly (~5.4-fold) increased staining for the speci ﬁc
mature PF marker CONTACTIN-2 ( Fig 4F)( Pallante et al, 2010) and by
the apparent increase in the RNA expression of additional PF
markers ( Fig S8C ). Altogether, PRDM16 loss during development
caused expression changes in CMs re ﬂecting alterations related to
a shift toward both atrial and conduction cell fates, the latter
resulting in a hyperplastic (distal) VCS.
PRDM16 suppresses the activity of master regulators of atrial and
conduction fates
To better understand how PRDM16 regulates gene expression in
CMs, we performed TF motif enrichment analysis, focusing on open
DARs in Prdm16
cKO CMs. Using both chromVAR and HOMER, we
revealed 309 and 59 signi ﬁcantly enriched motifs, respectively, of
which 31 overlapped. Some of these motifs are known to be as-
sociated with PRDM16, including TGIF1/2, TEAD1-4, and MEF2C (Fig
S9A). Furthermore, several other motifs represent members of the
GATA and TBX families, known to be involved in CM cell fate
decision-making (Fig S9A ). When performing the same motif
analysis on the subset of open atrial or conduction DARs (Table S8),
the combined chromVAR and HOMER analysis revealed similar
motifs as described above (Fig 5A and B). Remarkably, for both atrial
and conduction genes, TBX5 motifs were present in about 50% of
the DARs, in line with its known role as a master regulator of atrial
and conduction fates ( Fig 5A and B )( Pawlak et al, 2019 ; Choquet
et al, 2021 ; Cao et al, 2023 ; Sweat et al, 2023 ). Another commonly
present pathway known to be suppressed by PRDM16 was the TGF β
pathway, with TGIF motifs in 50% of DARs associated with atrial
genes and SMAD2-3 motifs in 7% of DARs associated with con-
duction genes (Fig 5A and B ). Furthermore, PRDM16 loss also sig-
niﬁcantly increased the expression of some of these TFs (i.e., Tbx5,
Mef2c, Smad2, Pbx3), suggesting that PRDM16 puts a double brake
on their activity by (1) blocking the accessibility of DNA binding sites
of these TFs and (2) by regulating the expression of these TFs (Fig
5C).
Knowing that certain master regulators were differentially
expressed after PRDM16 loss, and after identifying DEGs of atrial
and VCS cell fates, we calculated TF –gene associations and con-
structed gene regulatory networks (GRNs) for both atrial and
conduction cell fates. Within each fate-speciﬁc GRN, we then looked
at how PRDM16 could regulate such a network. To construct these
GRNs, we used the R package Functional Inference of Gene Reg-
ulation (FigR), which uses our RNA count data and paired ATAC peak
counts. FigR ﬁrst identi ﬁes signi ﬁcant peak –gene associations,
linking cis-regulatory elements to target genes, and de ﬁnes these
as domains of regulatory chromatin (DORCs). We identi ﬁed 8,221
DORCs and ﬁltered the associated genes based on our previously
identiﬁed atrial and conduction DEGs (to construct an atrial- and
conduction-speciﬁc network; Table S7), retaining the DORCs of 165
atrial and 162 conduction coding genes, respectively. FigR then
identiﬁes TF modulators associated with these domains to con-
struct a GRN. A regulation score is calculated for each TF-DORC
association. Averaging these regulation scores for each TF identiﬁes
them as activators (positive mean regulation score) or repressors
(negative mean regulation score) (Fig 5D and E and Table S9). Some
of the top ﬁve activating TFs for atrial and conduction genes that
emerged from our FigR analysis were common with those extracted
from the motif analysis, that is, MEF2C and TBX5 (Fig 5D and E and
Table S9). Plotting a heatmap based on the regulation score of the
top ﬁve activator TFs and associated DORCs of the genes of our
atrial and conduction GRNs alo ngside PRDM16 clearly revealed
that PRDM16 was opposing the activity of these master activators
(Fig
5D and E ). Our GRN analysis showed that only a minority of the
atrial and conduction DEGs were uniquely regulated by PRDM16 (Fig
S9B and C ). Together, this indicates that PRDM16 represses atrial
and conduction cell fates in the heart primarily by con ﬁning the
activity of master regulator TFs.
PRDM16 orchestrates CM fate decision by acting on promoters
and distant enhancers
We then focused on these peak –gene associations to study more
precisely how PRDM16 regulates genes related to atrial and con-
duction fates. We combined the 165 atrial and 162 conduction DEGs
from our GRNs, and focused on those genes with signi ﬁcant DARs.
This resulted in a compiled list of 120 signi ﬁcant DARs associated
representative for hypertrophy ( left), fatty acid (FA) metabolism ( middle), or TGF β signaling ( right). The absolute number and proportions of DEGs for each term are
indicated. (D) Bar graph showing the numbers of differentially accessible regions (DARs) identi ﬁed in CMs. Green and purple bars represent the number of more and less
accessible regions, respectively. Pie charts represent the annotation (expressed in %) of more open ( top) or more closed (bottom) DARs in CMs. UTR, untranslated region;
TTS, transcription termination site. (E) Functional annotation on DEGs higher expressed in cKO CMs showing the top 25 cardiac-related terms. Terms related to chamber
type, conduction, and growth are highlighted in red.
PRDM16 determines cardiomyocyte fate Van Wauwe et al. https://doi.org/10.26508/lsa.202402719 vol 7 | no 12 | e202402719 8o f2 5

Figure 4. PRDM16 loss in CMs causes a shift toward atrial and conduction fates.
(A) Integrated Uniform Manifold Approximation and Projections (UMAPs) showing the enriched expression of ventricular genes ( Kcne1, Myh7b; left)i n WT
cardiomyocytes (CMs) and the enriched expression of atrial genes ( Fgf12, Myl4; right)i n Prdm16-deﬁcient (cKO) CMs. The color scale represents log(fold change) from low
(white) to high (purple). (B) Integrated UMAPs showing the enriched expression of ventricular working CM genes (Kcnd2, Pde3a; left)i n WT CMs and the enriched expression
PRDM16 determines cardiomyocyte fate Van Wauwe et al. https://doi.org/10.26508/lsa.202402719 vol 7 | no 12 | e202402719 9o f2 5

with 67 coding DEGs. First, we looked at whether PRDM16 DNA
binding motifs, as identiﬁed in the CIS-BP database ( Weirauch et al,
2014), were present in these DARs. We found such motif(s) in DARs
associated with 23 out of 67 DEGs (Fig 6A ). We then identi ﬁed
PRDM16 binding motifs present in the promoter region (+/ − 2k bo f
the transcriptional start site [TSS]) and cross-checked these regions
with a previously published PRDM16 ChIPseq dataset (Wu et al,
2022) generated on CMs from E13.5 hearts. This revealed that
binding to the same promoter region was conﬁrmed for 5 DEGs (e.g.,
Ryr3, Lrp8; Fig 6A , green box ; Fig 6B ), suggesting that PRDM16 can
directly bind to the promoter of these genes. On the contrary, the
PRDM16 ChIPseq dataset also revealed potential binding to the
promoter region of 5 DEGs (e.g., Nppa, Gpx3) in the absence of a
PRDM16 binding motif, suggesting indirect binding of PRDM16 (Fig
6A, gray box ; Fig 6C ). For the regions outside the promoters, we
cross-checked with the ENCODE database on P0 hearts to identify
which of these corresponded to enhancer regions (Fig 6A , pink
boxes). This revealed 20 DEGs with enhancers, the majority of which
were marked with the active enhancer mark H3K27Ac (e.g., Sparc,
Camk1d; Fig 6A , pink boxes). In four cases (e.g., Slc6a6, Tbx5), the
enhancer regions were marked with the mark H3K4me3 (Fig 6A, pink
boxes). Remarkably, ChIPseq-validated TBX5 binding sites ( Steimle
JD et al, 2018 ; Akerberg et al, 2019 ) lay in close vicinity for 4 out of 5
genes that harbored a conﬁrmed direct binding site for PRDM16 and
for all ﬁve genes with suggested indirect PRDM16 binding in their
promoter region (Fig 6A , gray and green boxes; Fig 6B and C ). This
suggests both TFs may co-occupy regulatory regions of the same
genes. Finally, to link distal cis-regulatory elements to the TSS of
target genes, we performed a peak-to-gene analysis. For seven
atrial or conduction markers (including Tbx5 and Slc6a6), we
identiﬁed such distant enhancers, some of which harbored a
PRDM16 binding motif and/or a ChIPseq-validated TBX5 binding site
(Fig
6D). Thus, PRDM16 favors the ventricular CM cell fate by
modulating atrial and conduction gene expression, which involves
both direct and indirect binding to target regions (both promoter
and distant enhancer regions). Moreover, a number of these target
regions are also recognized by TF TBX5, which is known to favor
these alternative cell fates.
Discussion
Cardiac cells are a heterogeneous mixture of subtypes each re-
sponsible for different functions to ensure continuous cardiac
contraction. To establish these different cellular subtypes,
appropriate lineage decisions must be taken and maintained. TFs
play an orchestrating role in the decision-making process from
early on during cardiac development. Here, we revealed that
PRDM16 is one of these key TFs that co-regulates the proper
speciﬁcation of ventricular working CMs mainly by suppression of
genes typical for atrial and conduction fates, by opposing the
activity of master regulators. PRDM16 loss in CMs during devel-
opment resulted in their differentiation toward more atrial- and
conduction-like cells, thereby causing (distal) VCS hyperplasia (as
graphically summarized in the graphical abstract). The latter is
likely co-responsible for the premature death of a large proportion
of PRDM16-de ﬁcient pups.
Arndt et al (2013) showed that PRDM16 mutations in humans and
prdm16 knockdown in zebra ﬁsh are associated with cardiomyop-
athy potentially because of cell-autonomous changes in CMs.
Prompted by these observations, studies in mice were performed to
investigate the CM-speciﬁc role of PRDM16 using the Cre-lox system
(Arndt et al, 2013 ; Cibi et al, 2020 ; Nam et al, 2020 ; Wu et al, 2022 ;
Kramer et al, 2023). In these studies, different Cre drivers were used
and the phenotypic consequences of Cre-driven Prdm16 deletion
were remarkably diverse, because of the distinct cell populations
being targeted and the speci ﬁc developmental time frames during
which Cre recombinase was active. For our studies, we used the
Sm22α-Cre line, which is active in the developing heart, and
faithfully deleted Prdm16 between E8.5 and E12, a crucial time
window during cardiac development. Recently, sexual dimorphism
in cardiomyopathy patients because of PRDM16 mutations has
been reported, with females having a higher chance of developing
cardiomyopathy (Kramer et al, 2023 ). In mice, this sexual dimor-
phism was also seen in models that did report a mild phenoty-
pe— that is, without lethality — after Prdm16 deletion ( Nam et al,
2020; Kramer et al, 2023; Kuhnisch et al, 2024). Here, we did observe a
more dramatic phenotype (including early mortality) but found no
sex differences. This may be related to the fact that the severe
phenotype may overrule the sex effect of PRDM16 loss in CMs.
One of the main phenotypic traits already present at P7 and
persisting until adulthood in Prdm16
cKO mice was a prolonged QRS
complex, which indicates a delayed action potential. At least three
observations from our study may be responsible for the abnormal
ECG. First, we noted the signi ﬁcantly reduced expression of ion
channel genes implicated in cardiac electrophysiology, including
Kcnd2 and Fgf12. Mutations in Kcnd2 have been associated with
long-QT syndrome (Berger et al, 2010 ; Marks, 2013 ; Haissaguerre
et al, 2016) and/or sudden cardiac death (Toib et al, 2017 ; Farrell
et al, 2018 ). Moreover, mice carrying a gain-of-function missense
mutation in FGF12 were recently shown to suffer from bradycardia
of ventricular conduction genes (Cacna2d2, Ryr3; right)i n cKO CMs. The color scale represents log(fold change) from low (white) to high (purple). (C) Bar graphs show the
expression of atrial ( top) or ventricular ( bottom) markers ( Cao et al, 2023 ) overlapping with the differentially expressed gene lists and their average Log 2FC, revealing the
higher expression (green; average Log 2FC > 0) of 87.5% of the atrial genes and the lower expression (purple; average Log 2FC < 0) of 66.0% of the ventricular genes. The full
marker lists are shown in Table S7. (D) Bar graphs show the expression of ventricular conduction ( top) or working ( bottom) markers ( Shekhar et al, 2018 ) overlapping
with the differentially expressed gene lists and their average Log 2FC, revealing the higher expression (green; average Log 2FC > 0) of 85.3% of the ventricular conduction
genes and the lower expression (purple; average Log 2FC < 0) of 61.5% of the ventricular working genes. The full marker lists are shown in Table S7. (E) Integrated UMAP of
re-clustered CMs subclustered at high resolution highlighting the PF cluster in pink (left). The complete subcluster analysis is shown in Fig S8. The middle top panel (WT)
and top right panel (cKO) show the expression of the PF marker CONTACTIN-2 (Cntn2) in CMs. The middle lower panel (WT) and lower right panel (cKO) show the expression
of the PF marker Copine5 (Cpne5) in CMs. Insets focus on the Purkinje cluster. The color scale represents log(fold change) from low (white) to high (purple).
(F) Representative images of CONTACTIN-2 protein staining identifying the PFs in WT versus cKO P7 mouse hearts. The bar graph shows quantitative analysis of relative
CONTACTIN-2 area as a % of the whole ventricles ( n = 7/6). Quantitative data are expressed as the mean ± SEM; * P <0 . 0 5b ya t test. Scale bars: 500 μm( F ) .
PRDM16 determines cardiomyocyte fate Van Wauwe et al. https://doi.org/10.26508/lsa.202402719 vol 7 | no 12 | e202402719 10 of 25

Figure 5. PRDM16 suppresses the activity of master regulators of atrial and conduction fates.
(A) Scheme showing 100 atrial-speci ﬁc more open (logFC > 0) differentially accessible regions (DARs) in Prdm16-deﬁcient (cKO) versus WT cardiomyocytes (CMs) that
were scanned for transcription factor (TF) motifs revealing 130 and 39 motifs, using chromVAR and HOMER, respectively, of which 13 overlapped. Overl apping TF motifs are
listed on the right along with the percentage of DARs containing the motif sequence. (B) Scheme showing 69 ventricular conduction-speciﬁc more open (logFC > 0) DARs in
PRDM16 determines cardiomyocyte fate Van Wauwe et al. https://doi.org/10.26508/lsa.202402719 vol 7 | no 12 | e202402719 11 of 25

and sudden cardiac death (Veliskova et al, 2021 ). Second, the in-
creased ﬁbrosis seen in PRDM16-de ﬁcient myocardium may cause
the formation of heterotypic junctions between myoﬁbroblasts and
CMs resulting in lower electrical conductivity ( Rubart et al, 2018 ).
Finally, structural abnormalities in the VCS are invariably associ-
ated with arrhythmias (Choquet et al, 2021 ). In the majority of re-
ported cases (e.g., de ﬁciency of ETV1, NKX2.5, NCAM-1), the
abnormalities represent VCS hypoplasia, but few cases of hyper-
plasia have been reported to date (Shekhar et al, 2018 ; Choquet
et al, 2021 ). Only recently, a Hand1 mutant lacking an LV-speci ﬁc
enhancer was reported to cause VCS hyperplasia with reduced
conduction velocity (Vincentz et al, 2019 ). Similarly, we found
(distal) VCS hyperplasia in Prdm16
cKO hearts. Wu et al showed that
during early development, PRDM16 cooperates with HAND1 re-
garding LV speciﬁcation (Wu et al, 2022). However, Hand1 expression
was not changed in our setting because of the different time points
in cardiac development in both studies. The hyperplasia of the VCS
in our PRDM16-de ﬁcient mouse model was manifest at the histo-
logical level by an increase in the distal region consisting of PFs. The
observed prolonged QRS is indeed compatible with defects in the
distal VCS ( Christoffels & Moorman, 2009 ; Choquet et al, 2020 ). By
subclustering, we were also able to resolve a cell population
compatible with the PF gene signature. The transcriptional changes
we observed revealed an increase in several PF markers including
Cntn2 and Ryr3. PFs have speci ﬁc electrophysiological properties
and particular Ca
2+ dynamics with RYR3 being expressed about 100-
fold higher in PFs versus working myocardium and being more
sensitive to Ca
2+ than RYR2 to stabilize the electric function of PFs
(Pallante et al, 2010 ; Haissaguerre et al, 2016; Daniels et al, 2017 ). At
the same time, the high sensitivity to Ca 2+ makes PFs more
arrhythmogenic, which may result in sudden cardiac death because
of ventricular ﬁbrillation (Haissaguerre et al, 2016). As no less than
60% of the Prdm16
cKO pups died before weaning age, it is tempting
to speculate that the aberrant VCS in these mice contributes to
arrhythmias that could lead to premature death. Although this
pattern is consistent with such a cause of death, further analysis is
required to con ﬁrm this.
It has been shown that the VCS in part differentiates from tra-
becular progenitor CMs because of a slower proliferation rate
(Choquet et al, 2021 ). Interestingly, during embryonic development
these trabeculae disappear because of an even faster proliferating
compact myocardium, whereas the VCS continues to recruit cells
and continues to mature postnatally ( Choquet et al, 2020 ). Wu et al
documented a role of PRDM16 in determining the compact ven-
tricular CM fate at the expense of trabecular gene expression at
E13.5, a time point in line with the disappearance of the trabeculae
(Fig S1A )( Wu et al, 2022 ). We found that taking a transcriptomic
snapshot of cardiac Prdm16 deletion at P7 (also falling within the
temporal window of VCS development; Fig S1A)r eﬂected the role of
PRDM16 in the decision to become part of the ventricular working
myocardium, which requires the suppression of conduction marker
genes. Hence, our study complements the ﬁndings of Wu et al (2022)
on the detrimental role of PRDM16 operating as an important
regulator of compact versus trabecular and working versus con-
duction CMs. When using a previously published reference sig-
nature for trabecular CMs (Li et al, 2016), we noticed only a partial
and rather mild transcriptomic shift toward a trabecular fate upon
PRDM16 loss when comparing to Wu et al (2022) , likely because of
the later time point in our study ( Fig S10 and Table S4). However, we
did see clear anatomic signs of hypertrabeculation, in accordance
with previous reports demonstrating hypertrabeculation may
persist until adulthood, whereas related expression changes in CMs
subside by P3 (Luxan et al, 2013). Vice versa, besides the focus by Wu
et al on trabeculation, they also described up-regulation of a
neuron-like transcriptomic signature upon PRDM16 loss in E13.5
embryos but less dramatic compared with our data because of the
earlier transcriptomic snapshot in their study (Wu et al, 2022 ). This
again supports the differentiation shift during the embryonic de-
velopment of CM progenitors toward a conduction identity upon
PRDM16 loss. In addition, Nam et al (2020) showed that the tran-
scriptome of 1-mo-old PRDM16-de ﬁcient hearts with prolonged
QRS also displayed the increased expression of conduction marker
genes in CMs, including Cntn2, Ryr3, and Cacna2d2. Hence, PRDM16
still determines the cardiomyocyte cell fate postnatally, during the
late phase of VCS development (Nam et al, 2020 ).
Similar to other studies ( Cibi et al, 2020), our multiomics analysis
revealed that the primary function of PRDM16 is to suppress al-
ternative cell fates. We therefore pinpointed our mechanistic
studies toward how it elicited this effect by primarily focusing on
up-regulated genes after PRDM16 loss. Nevertheless, there was also
a signi ﬁcant set of genes that was down-regulated upon PRDM16
loss, including many genes typical for ventricular working CMs. This
dual activity of PRDM16 has been reported in other cell types,
including ECs, SMCs, neurons, and adipocytes (Kajimura et al, 2008 ;
Aranguren et al, 2013 ; Baizabal et al, 2018 ; Wang et al, 2023 ). Our TF
motif and GRN analyses commonly revealed that PRDM16 most
likely mediates its repressive effects on atrial and conduction
marker genes through opposition of master regulator TFs, most
notably TBX5. Not only was TBX5 up-regulated, but we also noticed
increased enrichment for TBX5 binding motifs in peaks associated
with up-regulated genes. Intriguingly, a similar motif analysis by Wu
et al showed increased enrichment for TBX5 binding motifs at
PRDM16 peaks of down-regulated genes after ChIPseq of Prdm16
cKO
versus Prdm16WT embryonic LVs. This suggested a positive
cKO versus WT CMs that were scanned for TF motifs revealing 94 and 27 motifs, using chromVAR and HOMER, respectively, of which seven overlapped. Overlapping TF
motifs are listed on the right along with the percentage of DARs containing the motif sequence. (C) Violin plots of enriched TFs differentially expressed in cKO versus WT
CMs. Gene regulatory network (GRN) analysis using FigR identifying domains of regulatory chromatin (DORCs) and associated genes. (D, E) To obtain atrial-speciﬁc (D) or
conduction-speciﬁc (E) GRNs, genes were ﬁltered using established atrial ( Cao et al, 2023 ) or conduction ( Shekhar et al, 2018 ) gene signatures and for being
differentially expressed. Bar graphs represent the mean regulation score (y-axis, log 10-transformed per TF across all DORCs). The upper section of the bar graphs zooms in
on the top 10 “master activator” TFs (positive mean regulation score) of the GRN. Heatmaps represent TF-DORC associations colored according to their regulation score
(blue = negative or repressor; red = positive or activator), with DORCs representing the associated atrial or conduction differentially expressed genes (y-axis). TFs (x-axis)
represent the top ﬁve master activators alongside PRDM16. The purple line indicates the repressing regulation by PRDM16 compared with the other TFs. The raw data for
motif and heatmap analysis are included in Table S9. The color scale represents the regulation score per TF-DORC association.
PRDM16 determines cardiomyocyte fate Van Wauwe et al. https://doi.org/10.26508/lsa.202402719 vol 7 | no 12 | e202402719 12 of 25

Figure 6. PRDM16 orchestrates CM fate decision by acting on promoters and distant enhancers.
(A) Decision tree identifying PRDM16 targets in differentially accessible regions associated with 67 atrial- and/or conduction-speci ﬁc coding differentially expressed
genes (DEGs) and located inside or outside the promoter region. A combination of HOMER-PRDM16 binding motif analysis, publicly available PRDM16 ChI Pseq (E13.5
cardiomyocytes), and ENCODE datasets (P0 hearts) was applied to determine whether PRDM16 directly or indirectly binds their promoter (green and gray boxes,
PRDM16 determines cardiomyocyte fate Van Wauwe et al. https://doi.org/10.26508/lsa.202402719 vol 7 | no 12 | e202402719 13 of 25

cooperation between PRDM16 and TBX5 in the decision between
compact versus trabecular CMs rather than an opposition as we
propose here in conduction versus working CMs (Wu et al, 2022 ).
Interestingly, a recent study put forward TBX5 as a master regulator
of the atrial fate that was also important for maintaining this fate
later in life ( Sweat et al, 2023 ). Whether PRDM16 also maintains
ventricular (working) CM fate by cooperation with positive
regulators/facilitators of this fate, for example, ERR α/γ or HEY2,
remains to be determined ( Koibuchi & Chin, 2007 ; Sweat et al,
2023).
Although previous studies suggested that PRDM16 mainly acts
through indirect association with DNA (Baizabal et al, 2018 ; Wu et al,
2022), our analysis revealed a multitude of PRDM16 binding sites in
the promoter region of atrial and conduction genes, a fraction of
which was validated by crossover with the ChIPseq dataset of Wu
et al (2022). At the same time, overlapping the atrial and conduction
DEG lists with the same ChIPseq dataset also revealed PRDM16
binding in their promoters in the absence of the binding motif,
corroborating that PRDM16 may also associate with DNA as part of a
transcriptional complex, in line with previous studies. A noteworthy
limitation to this crossover analysis is the already abovementioned
temporal mismatch between the study of Wu et al (2022) and our
study (Fig S1A). Unlike previous studies, our analysis also included
an evaluation of the effects of PRDM16 de ﬁciency on chromatin
accessibility, inspired by previous observations that describe
epigenetic actions by PRDM16 either through association with
histone-modifying enzymes or by its own methylation activities
(Pinheiro et al, 2012 ; Di Zazzo et al, 2013 ; Harms et al, 2014 ; Li et al,
2015; Baizabal et al, 2018 ; Cibi et al, 2020 ; Jiang et al, 2022 ). ATACseq
revealed that deletion of Prdm16 in CMs resulted in a signi ﬁcant
number of DARs, the majority of which were associated with in-
creased accessibility, further supporting the major repressive effect
of PRDM16. Integration of RNAseq and ATACseq enabled us not only
to perform TF motif and GRN analyses, but also to address the
question whether PRDM16 acts on distant cis-regulatory elements,
a mechanism that has been detected earlier during PRDM16-
mediated neuronal differentiation (Baizabal et al, 2018 ). The in-
volvement of distant enhancers was indeed shown for a subset of
genes, including Tbx5. Altogether, the involvement of epigenetic
activity governed by PRDM16 adds another layer of complexity to its
mode of action in CMs.
In this study, we showed that PRDM16 orchestrates the decision
for a CM (progenitor) to differentiate toward a mature ventricular
CM. Therefore, it will be very appealing to test whether the over-
expression of PRDM16 is suf ﬁcient to induce such a fate in induced
pluripotency stem cell –derived CMs ( Kodo et al, 2016; Funakoshi
et al, 2021). If successful, this may represent an inexhaustible source
of mature ventricular CMs to be used for regenerative therapies in
post-infarct
patients for seeding regenerative patches of myo-
cardium, which in their current status lack proper mature ven-
tricular physiology.
Materials and Methods
Animal strains and husbandry
Animal experiments were approved by the KU Leuven Animal Ethics
Committee and performed under the Committee ’s guidelines.
Animals were housed under speci ﬁc pathogen-free conditions and
kept in a 12/12-h light/dark cycle and allowed access to standard
rodent chow and water ad libitum. Sex was not determined for pups
found dead in their cage. Three genetically modi ﬁed mouse strains
were used ( Fig S2A ): (1) ubiquitous constitutive Prdm16 knockout
mice ( Prdm16 Gt(OST67423)Lex ; referred to as “Prdm16-LacZ”)
purchased from the Mutant Mouse Resource & Research Center
(MMRRC) and backcrossed for nine generations on a C57BL/6
background ( Kajimura et al, 2008 ); (2) conditional Prdm16 knock-
out mice generated by inter-crossing homozygous Prdm16
lox/lox
mice (available through B. Spiegelman, Boston, USA; on a C57BL/6
background [ Cohen et al, 2014 ]) with LoxP sites ﬂanking exon 9 of
the Prdm16 gene and Sm22 α-Cre driver mice (available through
J. Herz, Texas, USA; on a mixed CD1/C57BL/6 background [ Holtwick
et al, 2002 ]), which we refer to as “Prdm16cKO” (and their corre-
sponding Cre-negative littermates “Prdm16WT”); (3) a Cre activity
reporter strain generated by inter-crossing Sm22 α-Cre driver mice
with mice harboring a R26R CAG-boosted eGFP (RCE) cassette with a
ﬂoxed STOP codon before the GFP-encoding gene under the CAG
promoter in the Rosa26 locus ( Sousa et al, 2009 ). For genotyping,
genomic DNA was extracted using tissue from mouse ears and put
overnight in lysis buffer. Isopropanol-based isolation of the DNA
was performed, and alleles of interest were genotyped using
Thermo Fisher Scienti ﬁc PuReTaq PCR beads. Primers are listed in
Table 2 .
Tissue/embryo harvesting
When euthanized for tissue collection, adult animals were injected
with Dolethal (66.7 μg/g), whereas 7-d-old pups were decapitated.
The chest was cut open, and organs were dissected out and snap-
respectively) or potentially interacts with their enhancer regions (pink boxes; genes in bold-face font are those associated with distant enhancers). ChIP, chromatin
immunoprecipitation. The color code of enhancer regions corresponds to the one used by ENCODE: H3K27Ac: histone-3-lysine-27 acetylated (yellow), H3K4me3: histone-3-
lysine-4 trimethylated (red), and CTCF-bound: CCCTC-binding factor (blue). ATAC peaks of the promoter region of WT (red) and Prdm16-deﬁcient ( cKO,b l u e )
cardiomyocytes for genes from the green box in (A), representing cases of ChIPseq-validated direct PRDM16 binding to the promoter region. ATAC peaks of the promoter
region of WT (red) and cKO (blue) cardiomyocytes for genes from the gray box in (A), representing cases of ChIPseq-validated indirect PRDM16 binding to the promoter
region. (D) Peak-to-gene link plots identifying distant enhancer regions in WT (red) versus cKO (blue) cardiomyocytes in Slc6a6 and Tbx5. Purple strings indicate the peak-
to-gene link; the color scale represents correlation signiﬁcance (from 0 to 1). Arrowheads represent enhancers identiﬁed by the ENCODE database. Transcriptional start
site is marked in (B, C, D) by fuchsia arrow and white line +/ − 2-kb region indicated by fuchsia line. Differentially accessible regions are highlighted in (B, C, D) by light-
orange shades. Brown lines ( top) in (B, C, D) represent ChIPseq-validated (in E9.5 or E12.5 cardiomyocytes) (Steimle et al, 2018 ; Akerberg et al, 2019 ) TBX5 binding site
regions. Green lines (bottom) in (B, C) represent PRDM16 target peaks validated by ChIPseq in E13.5 CMs ( Wu et al, 2022). Dark-orange lines (top) in (B) represent HOMER-
predicted PRDM16 binding sites. The differential expression of the genes is shown as violin plots. expr, expression; chr, chromosome; pks, peaks.
PRDM16 determines cardiomyocyte fate Van Wauwe et al. https://doi.org/10.26508/lsa.202402719 vol 7 | no 12 | e202402719 14 of 25

Table 2. Detailed resources table.
Antibody Source Identi ﬁer
Anti-PRDM16 antibody (sheep) R&D Systems Cat#AF6295 ( Bauters et al, 2017)
Anti-GFP antibody (chicken) Abcam Cat#ab13970
Anti-LAMININ antibody (rabbit) Sigma-Aldrich Cat#L9393
Anti-ENDOMUCIN antibody (goat) R&D Systems Cat#AF4666
Anti-DESMIN antibody (goat) R&D Systems Cat#AF3844
Anti-PCM1 antibody (rabbit) Sigma-Aldrich Cat#HPA023370
Anti-CONTACTIN-2 antibody (goat) R&D Systems Cat#4439
Anti-SMA-CY3 antibody (mouse) Sigma-Aldrich Cat#F3777
Anti-MYL4 antibody (rabbit) Thermo Fisher Scientiﬁ c Cat#PA5-119955
Anti-FGF12 antibody (rabbit) Abcam Cat#ab231956 ( Tian et al, 2024)
Anti-CACNA2D2 antibody (rabbit) Novus Biologicals Cat#NBP1-81501 ( Zhang et al, 2017)
Anti-NPR3 antibody (mouse) Santa Cruz Cat#sc-515449
Anti-FHL2 antibody (rabbit) Thermo Fisher Scientiﬁ c Cat#21619-1-AP
Anti-CD31 antibody (rabbit) Abcam Cat#Ab28364
Primer Sequence Source
Mouse Gapdh forward 5 9-ccgcatcttcttgtgcagt-39 Integrated DNA Technologies (IDT)
Mouse Gapdh reverse 5 9-gaatttgccgtgagtggagt-39 IDT
Mouse Prdm16 forward 5 9-cagcacggtgaagccattc-39 IDT
Mouse Prdm16 reverse 5 9-gcgtgcatccgcttgtg-39 IDT
Mouse Nppa forward 5 9-gcttcgggggtaggattgac-39 IDT
Mouse Nppa reverse 5 9-gaggcaagaccccactagac-39 IDT
Mouse Nppb forward 5 9-tgggctgtaacgcactgaag-39 IDT
Mouse Nppb reverse 5 9-acttcaaaggtggtcccaga-39 IDT
Mouse Ryr3 forward 5 9-gacaggacc
 aggaacggaag-39 IDT
Mouse Ryr3 reverse 59-gctccaccgtcttttctgga-39 IDT
Mouse Tuba1b forward 59-ccagatgccaagtgacaaga-39 IDT
Mouse Tuba1b reverse 59-gatctccttgccaatggtgt-39 IDT
Mouse Kcne1 forward 59-cagcagagcctcgaccattt-39 IDT
Mouse Kcne1 reverse 59-ctgaagctctccaggacacg-39 IDT
Mouse Fgf12 forward 59-ctacaccctcttcaatctaattcc-39 IDT
Mouse Fgf12 reverse 59-ttccccttcatgatttgacc-39 IDT
Mouse Myl4 forward 59-ccaatggctgcatcaactatgaa-39 IDT
Mouse Myl4 reverse 59-ccatgtgagtccaatactccgtaa-39 IDT
Mouse Kcnd2 forward 59-ctgctcacggagacacaaaa-39 IDT
Mouse Kcnd2 reverse 59-cggctgttggatagtggagt-39 IDT
Mouse Pde3a forward
59-agaatccatgccaccgatgt-39 IDT
Mouse Pde3a reverse 59-cccatgtgtccgtgtgtaaa-39 IDT
Mouse Cacna2d2 forward 59-aattggtggagaaagtggca-39 IDT
Mouse Cacna2d2 reverse 59-ggctttctggaaattctctgc-39 IDT
Mouse Thbs4 forward 59-cagacagagatggcattggagac-39 IDT
Mouse Thbs4 reverse 59-ggttactgacatcaggacagctg-39 IDT
Mouse Hey2 forward 59-gagaagactagtgccaacagc-39 IDT
Mouse Hey2 reverse 59-gcatgggcatcaaagtagcct-39 IDT
(Continued on following page)
PRDM16 determines cardiomyocyte fate Van Wauwe et al. https://doi.org/10.26508/lsa.202402719 vol 7 | no 12 | e202402719 15 of 25

frozen (for cryosectioning, RNA or protein isolation) or post- ﬁxed
overnight in 4% PFA for further histological processing. Timed
matings were set up for embryo collection at E9.5, E10.5 E11.5, E14.5,
and E17.5. Pregnant dams were killed by cervical dislocation, fol-
lowed by dissection of the uterus that was put in ice-cold PBS. Then,
embryos were dissected out one by one in ice-cold PBS, followed by
overnight ﬁxation in PFA at 4°C for further histological processing,
or embedded in Tissue-Tek and snap-frozen for cryosectioning.
Echocardiography
Echocardiography was performed on both pups and adult animals
using a Vevo2100 or Vevo3100 system (FUJIFILM VisualSonics). Pups
were subjected to echocardiography at P7. Pups were anesthetized
brieﬂy by 1.5 –2% iso ﬂurane in 2.5% O
2, and immediately ﬁxed on
their back on a preheated heating pad. ECG gel was used to make
the connection between the paws and the ECG pads. Preheated
echo gel was applied prior to obtain a short-axis view (SAX) image.
Pups were put back with the mother immediately after recording.
Adult animals were put in an anesthetic induction chamber, and
anesthesia was induced with 5% iso ﬂurane in 2.5% O
2. Once asleep,
isoﬂurane levels were reduced to 1.5–2% and the animal was placed
on its back on a heating plate containing ECG pads. After applying
ECG gel on both fore and hind paws, they wereﬁxed on the ECG pads
to monitor ECG, respiratory rate, and heart rate of the mice during
the procedure. A rectal probe was used to monitor body temper-
ature, and an extra heating lamp was used to keep body tem-
perature stable at 37°C. Once body temperature, heart rate, and
breathing were stable (i.e., 37°C, ±500 beats per minute, and ±100
respiratory rate, respectively), echo recording was performed. The
following images of the heart were captured: SAX, M-mode through
SAX, long-axis view (LAX), and apical four-chamber view. Flow rate
Table 2. Continued
Antibody Source Identi ﬁer
Mouse Ank2 forward 5 9-tggaaggagcacaagagtcgt-39 IDT
Mouse Ank2 reverse 5 9-cagagccagcttcactttcttg-39 IDT
Genotyping: Cre allele forward 5 9-gaccggtaatgcaggcaa-39 IDT
Genotyping: Cre allele reverse 5 9-tccaaagcatgcagagaatgt-39 IDT
Genotyping: ﬂoxed Prdm16 allele forward 5 9-gagctaggcagggacactgct-39 IDT
Genotyping: ﬂoxed Prdm16 allele reverse 5 9-ccagtatcagagaggcaagaa-39 IDT
Genotyping: Prdm16GT(OST67423)LEX 1 59-acaggcgaggaactgtatgaaagg-39 IDT
Genotyping: Prdm16GT(OST67423)LEX 2 59-ccatctgaggtcgtctgaaactgg-39 IDT
Genotyping: Prdm16GT(OST67423)LEX 3 59-aaatggcgttacttaagctagcttgc-39 IDT
Software Source Identi ﬁer
Cell Ranger Arc v1.0.1 10X Genomics https://support.10xgenomics.com/single-cell-multiome-
atac-gex/software/overview/welcome
CellBender v0.1.0 Fleming et al (2023) https://github.com/broadinstitute/CellBender
scDblFinder v1.10.0 Germain et al (2021) https://github.com/plger/scDblFinder
clusterProﬁler v4.4.4 Yu et al (2012) https://bioconductor.org/packages/release/bioc/html/
clusterProﬁler.html
rGREAT
v4.0.4 Gu and Hubschmann (2023) http://great.stanford.edu
Seurat v4.3.0 Satija Lab https://satijalab.org/seurat/
Signac v1.10.0 Stuart Lab https://stuartlab.org/signac/
HOMER v4.11 Heinz et al (2010) http://homer.ucsd.edu/homer/
chromVAR v1.18 Schep et al (2017) https://greenleaﬂab.github.io/chromVAR/articles/
Introduction.html
FigR v0.1.0 Kartha et al (2022) https://buenrostrolab.github.io/FigR/
Fiji v2.14.0 Schindelin et al (2012) https://imagej.net/software/ﬁji/#publication
NIH ImageJ v1.53 https://imagej.net/nih-image/
GraphPad Prism v9.4.1 GraphPad Software https://www.graphpad.com/features
Vevo LAB v5.5.1 FUJIFILM VisualSonics, Inc. https://www.visualsonics.com/product/software/vevo-lab
QuPath v0.4.0 Bankhead et al (2017) https://qupath.github.io/
ZEN Microscopy Software ZEISS Group https://www.zeiss.com/microscopy/en/products/
software/zeiss-zen.html
ToppGene Chen et al (2009) https://toppgene.cchmc.org/
PRDM16 determines cardiomyocyte fate Van Wauwe et al. https://doi.org/10.26508/lsa.202402719 vol 7 | no 12 | e202402719 16 of 25

through the pulmonary artery (via SAX view) and mitral valve (via
apical four-chamber view) was measured using pulsed-wave
Doppler where the degree of the Doppler angle was kept equal
for each animal. Mitral valve movement was assessed via tissue
Doppler at the septal base of the mitral valve visualized on the
apical four-chamber view. ECG data were retrieved from the surface
ECG of the Vevo2100 and Vevo3100 imaging system. ECG of 25
cardiac cycles was averaged. QRS was determined manually, where
Q was the minimum voltage before the R-peak, R was the maximum
voltage, and S was the minimum voltage immediately after the
R-peak. The time between Q and S was de ﬁned as QRS duration.
Maximum amplitude was the maximum voltage of the R-peak.
Histology and morphometry
PRDM16 expression
To study the expression pattern of PRDM16, two different tech-
niques were used. The ﬁrst method took advantage of the presence
of a gene trap cassette in the Prdm16 locus encoding β-galacto-
sidase in Prdm16-LacZ mice ( Fig S2A ). After dissection, embryos
were submerged in ﬁxation solution (PBS containing 0.2% glutar-
aldehyde and 2 mmol/liter MgCl
2) for 20 min at 4°C before starting
the X-gal staining protocol. Brieﬂ y, embryos (E9.5 and E10.5) were
washed three times with PBS for 10 min and incubated overnight at
30°C with staining solution (PBS containing 1 mg/ml X-gal (Life
Technologies), 5 mmol/liter K
3Fe(CN)6, 5 mmol/liter K4Fe(CN)6, and 2
mmol/liter MgCl2). The next day, embryos were washed three times
with PBS for 10 min and ﬁxed with 4% PFA for 2 h at room tem-
perature (RT). Before processing for parafﬁn embedding, a ﬁnal PBS
washing step was performed. Samples were sectioned, and cross-
sections were counterstained with nuclear fast red dye. PRDM16 WT
littermates served as negative controls. For the second method, a
staining protocol was optimized for immuno ﬂuorescence analysis.
Brieﬂy, tissues were dissected out, snap-frozen in liquid N
2, and
stored at −80°C until cryosectioning. Samples were mounted with
Tissue-Tek, and 7- μm sections were made using a Leica 3050S
cryostat. Sections were air-dried and ﬁxed with 4% PFA for 10 min.
Next, sections were washed with Milli-Q water, washed three times
with TNT (TNB + 0.05% Tween-20), and subsequently permeabilized
with PBS containing 0.1% Triton for 30 min. Non-speci ﬁc protein
interactions were prevented by incubating slides with blocking
buffer (TNB containing 10% donkey serum) for 1 h. Slides were co-
incubated overnight at 4°C with sheep anti-PRDM16 antibody and
anti-PCM1 antibody (to measure recombination ef ﬁciency in P7
hearts) or anti-ENDOMUCIN antibody (to delineate trabeculae in
E14.5 embryos; all primary antibodies are listed in Table 2). The next
day, slides were washed three times with TNT and incubated with
donkey anti-sheep IgG Alexa 488 antibody and donkey anti-rabbit
IgG Alexa 568 antibody or donkey anti-goat IgG Alexa 488 for 2 h at
RT. Nuclear staining was obtained by incubating slides with TO-
PRO-3 iodide or Hoechst for 15 min. Finally, slides were mounted
with ProLong Gold Antifade. Antibodies used for immunostaining
were validated during optimization of the staining procedure
during which a negative control condition was included (i.e., an
identical staining procedure with exclusion of the primary anti-
body). In case of staining for PRDM16, the antibody was validated by
loss of staining upon Prdm16 knockout.
SM22α-Cre activity
SM22α-Cre-RCEembryos (collected at E11.5) and P7 mouse hearts were
ﬁxed overnight in 4% PFA, dehydrated in a series of ethanol and xylene,
and parafﬁn-embedded for sectioning. Parafﬁn sections were stained
with an anti-GFP antibody, combined with a second primary antibody
labeling–speciﬁc cardiac cell–type markers (i.e., anti-DESMIN for CMs;
Table 2). Brieﬂy, parafﬁn sections were deparaf ﬁnized and antigens
were exposed by boiling in citrate buffer or DAKO buffer depending on
the primary antibody. Next, endogenous peroxidases were inactivated
using methanol containing 0.3% H
2O2 for 20 min. Cell membranes were
subsequently lysed using 0.1% Triton X-100 in PBS, and non-speci ﬁc
antibody binding was blocked using 2% BSA in TBS for 1 h, followed by
incubation with primary antibodies in TNB overnight. The next day,
primary antibodies were washed off and slides were incubated with
matching Alexa-conjugated secondary antibodies for 2 h in TNB. Where
necessary, ampliﬁcation was performed using Cy3 or ﬂuorescein tyr-
amide (FT) kits (PerkinElmer, NEL744001KT and NEL741001KT). Brieﬂy,
slides were incubated with horseradish peroxidase –conjugated
streptavidin (1:100) dissolved in TNB for 30 min, washed three times
with TNT, and incubated for 8 min withA-diluent containing FT (1:50) or
cyanine (Cy)3-tyramide (1:50). Slides were washed and mounted with
ProLong Gold Antifade mounting media.
SMC coating
To measure vascular SMC area of the coronary arteries, paraf ﬁn
cross-sections of P7 hearts were co-stained for CD31 and αSMA.
After deparaf ﬁnization and dehydration, sections were boiled in
Tris–EDTA–antigen retrieval for 20 min followed by a 20-min slow
cool-down. Next, endogenous peroxidases were inactivated using
methanol containing 0.3% H
2O2 for 20 min. Slides were washed with
TBS and blocked for 1 h with TNB, followed by overnight primary
antibody incubation (targeting CD31 and αSMA-Cy3; Table 2 ). The
next day, slides were washed and incubated with secondary an-
tibody goat anti-rabbit biotin for 45 min. A TSA biotin detection kit
(NEL741001KT; PerkinElmer) was used to amplify the ﬂuorescent
signal as described above. Images were taken on a ZEISS upright
microscope and saved as a ZVI ﬁle, to open in Fiji. The EC layer area
was measured based on the FT signal, and the SMC layer was
measured based on the Cy3 signal. Both channels were opened
separately in Fiji, converted to RGB, and made binary to measure
the area via the wand-tracing tool. Analyses were performed by an
investigator unaware of the mouse genotype. All analyses per-
formed on images were done in Fiji, unless mentioned otherwise.
CM hypertrophy
To measure CM size, transversal cardiac parafﬁn sections were
stained for LAMININ. Brieﬂ y, after deparaf ﬁnization, citrate (pH 6)-
based antigen retrieval, and blocking, tissue slides were embedded
overnight with primary anti-LAMININ antibody (Table 2 ). The next
day, slides were incubated with secondary Alexa 568 antibody for 2
h, followed by TO-PRO-3 for 15 min before mounting with ProLong
Gold Antifade.
Fibrosis
Cardiac cross-sections were stained with Sirius Red to assess ﬁ-
brosis. Brieﬂy, parafﬁn sections were deparaf ﬁnized and incubated
for 90 min in freshly prepared Sirius Red (picric acid) solution
PRDM16 determines cardiomyocyte fate Van Wauwe et al. https://doi.org/10.26508/lsa.202402719 vol 7 | no 12 | e202402719 17 of 25

followed by differentiation in HCl for 2 min. Sections were dehy-
drated and mounted with DPX. Brightﬁeld images were recorded on
a ZEISS upright microscope, and ﬁbrosis was detected and cate-
gorized into perivascular ﬁbrosis and interstitial ﬁbrosis. The
presence of interstitial ﬁbrosis in P7 hearts was con ﬁrmed by
analyzing the sections under polarized light. Analysis was per-
formed by an investigator unaware of the mouse genotype. Rep-
resentative images for each group represent the group average.
Compact layer expansion
P7 hearts were sectioned sagittally, and endocardium was identi-
ﬁed via Natriuretic Peptide Receptor 3 (NPR3) or ENDOMUCIN
staining to distinguish compact from non-compact myocardium.
Brieﬂy, after deparaf ﬁnization, DAKO –antigen retrieval, and
blocking, tissue slides were embedded overnight with primary anti-
ENDOMUCIN antibody (Table 2). The next day, slides were incubated
with secondary Alexa 488 antibody for 2 h, followed by TO-PRO-3 for
15 min before mounting with ProLong Gold Antifade. For NPR3, after
deparafﬁnization and citrate (pH 6) –antigen retrieval, endogenous
peroxidases were inactivated using methanol containing 0.3% H
2O2
for 20 min. Slides were washed with TBS, incubated in 0.1% Triton for
30 min, and blocked for 1 h with TNB supplemented with 10% goat
serum, followed by overnight primary antibody incubation targeting
NPR3 ( Table 2 ). The next day, slides were washed and incubated
with secondary antibody goat anti-mouse biotin for 45 min. A TSA
biotin detection kit (NEL741001KT; PerkinElmer) was used to amplify
the ﬂuorescent signal. The width of the compact myocardium
(spanning from the outer epicardium to the border of the non-
compact myocardium, the latter determined based on the NPR3- or
ENDOMUCIN-lined trabecular invaginations) was measured at two
locations in the LV from the base to the apex. Both at the base and
at the apex level, the shortest distance from the endocardium to
the epicardium was used for measurement.
VCS
To identify the (distal) VCS, frozen P7 hearts were sectioned sag-
ittally and stained for CONTACTIN-2, a PF marker (Pallante et al,
2010). Brieﬂy, cryosections were ﬁxed with 4% PFA for at least 10 min.
Slides were incubated with 0.1% Triton X-100 for 30 min followed by
a blocking step (10% PIG in TNB, for 1 h) before overnight incubation
with primary antibody against CONTACTIN-2 (Table 2 ). The next day,
slides were incubated with secondary Alexa 488 antibody for 2 h,
before mounting with ProLong Gold Antifade. Whole sections were
imaged using mosaic scanning on a ZEISS upright wide ﬁeld mi-
croscope. The total CONTACTIN-2 area of both ventricles was
measured and normalized to the total ventricular tissue area using
QuPath ( https://qupath.github.io/).
Cardiac MYL4 or FHL2 expression
P7 hearts were sectioned sagittally (MYL4) or transversely (FHL2),
and atrial marker MYOSIN LIGHT CHAIN-4 (MYL4) and ventricular
marker Four And A Half LIM Domains 2 (FHL2) were used to show the
ventricular-to-atrial identity shift in ventricular CMs at the protein
level. Brie ﬂy, after deparaf ﬁnization, Tris –EDTA–antigen retrieval,
and blocking (including elimination of endogenous peroxidase
activity using H
2O2 in methanol), tissue slides were embedded
overnight with primary anti-MYL4 antibody or anti-FHL2 antibody
(Table 2 ). The next day, for MYL4 detection, slides were incubated
with secondary horseradish peroxidase (HRP) –labeled antibody
for 45 min, followed by DAB/H 2O2 developing solution. After
termination of DAB/H 2O2-HRP reaction, the tissue was counter-
stained with hematoxylin. To detect FHL2, slides were incubated
with secondary Alexa 568 antibody for 2 h, followed by Hoechst
staining for 15 min before mounting with ProLong Gold Antifade.
MYL4 expression was quanti ﬁed by measuring brown-colored
area over the total myocardial area using QuPath ( https://
qupath.github.io/ ), and FHL2 expression was determined by
measuring the mean ﬂuorescence intensity signal in the heart
using Fiji.
Reverse transcription –quantitative PCR (RT– qPCR)
For RNA extraction, the tissue was snap-frozen in MP Lysing
Matrix Tubes (containing beads for homogenization) and upon
isolation supplemented with TRI zol and mechanically dissoci-
ated using a Ribolyser FastPrep- 24 homogenizer (MP-Bio). RNA
was isolated based on chloroform extraction. Isolated RNA was
reverse-transcribed using Superscript III Reverse Transcriptase
( P r o m e g a )t oo b t a i nc D N Af o rR T–qPCR. A QuantStudio 3 system
(Applied Biosystems) was used for RT –qPCR with ﬂuorescent
SYBR Green detection. Thermocycling conditions used for RT –
qPCR were as follows: hold (50°C, 2 min); hold (95°C, 10 min); 40
cycles of ampli ﬁcation (95°C, 0:15 min/X°C based on primer,
1m i n ) ;a n dﬁnal melting curve analysis: 95°C, 0:15 min; X°C based
on primer, 95°C (dissociation), 0:15 min with a temperature in-
crement of 0.1°C per second. Gene expression values were
normalized to housekeeping genes Gapdh or alpha-tubulin
(Tuba1b ). Data were calculated as 2
(−ΔΔCT) , using universal mouse
cDNA as a reference sample. Primers and primer sequences are
listed in Table 2 .
Immunoblotting
For protein extraction, the tissue was snap-frozen in MP Lysing
Matrix Tubes (containing beads for homogenization) and upon
isolation supplemented with RIPA lysis buffer and mechanically
dissociated using a Ribolyser FastPrep-24 homogenizer (MP-Bio).
The protein concentration was measured using the bicinchoninic
acid protein assay kit (#23225; Thermo Fisher Scienti ﬁc), 40 μgo f
protein was mixed with reducing agent (NP009; Life Technologies)
and lithium dodecyl sulfate sample buffer (NP007; Life Technolo-
gies), boiled, and loaded on gel to separate proteins. Proteins were
subsequently transferred to a nitrocellulose membrane that was
blocked with 5% BSA or 5% milk for 1 h before incubation with
primary antibody (against PRDM16, FGF12, CACNA2D2, or β-TUBULIN;
Table 2) overnight. The next day, the blot was washed and incubated
with HRP-conjugated secondary antibody for 1 h at RT. Bound
antibodies were detected using Pierce ECL Western Blotting Sub-
strate or SuperSignal West Femto Maximum Sensitivity Substrate
(Thermo Fisher Scienti ﬁc) on a Bio-Rad ChemiDoc XRS+ molecular
imager equipped with Image Lab software (Bio-Rad Laboratories).
Bands were quanti ﬁed using NIH ImageJ software, with β-TUBULIN
staining as a loading control.
PRDM16 determines cardiomyocyte fate Van Wauwe et al. https://doi.org/10.26508/lsa.202402719 vol 7 | no 12 | e202402719 18 of 25

Single-nucleus multiomics
Both the isolation protocol of the single nuclei and the bio-
informatics analysis of the data were based on Amoni et al (2023) ,
with minor modi ﬁcations related to our study.
Isolation of nuclei
Seven-day-old pups were decapitated, and hearts were immedi-
ately removed and placed in PBS, all done on ice. The atria, part of
the base, and the entire right ventricle were removed, and the
remaining LV was cut into small pieces and snap-frozen in liquid N
2.
Four samples per genotype were pooled to obtain ~80 mg of heart
tissue per sample into gentleMACS M Tubes containing lysis buffer
(5 mM CaCl
2, 3 mM MgAc, 2 mM EDTA, 0.5 mM EGTA, and 10 mM
Tris–HCl, pH 8, in H 2O, supplemented before use with 1 mM DTT,
1 μg/ml actinomycin D, 0.05% Protease Inhibitor Cocktail, and 0.04
U/μl RNA inhibitors — RNase OUT). The ﬁrst step of the isolation
protocol was a mechanical dissociation using the gentleMACS
dissociator. After mechanical dissociation, the tissue was exposed
to lysis buffer supplemented with NP-40 (0.1%) and digitonin
(0.01%) for lysis of the cell membrane. After a 15-min incubation on
ice, the homogenate was passed through a 30- μm ﬁlter and spun
down. The pellet was dissolved in sucrose buffer (1 M sucrose, 3 mM
MgAc, and 10 mM Tris –HCl, pH 8, in H
2O, supplemented with 1 mM
DTT, 1 µg/ml actinomycin D, 0.05% Protease Inhibitor Cocktail, and
0.04 U/μl RNA inhibitors— RNase OUT). To isolate the nuclei from the
cell debris, the nucleus-containing sucrose solution was pipetted
gently on top of fresh sucrose buffer. After centrifugation, nuclei
were pelleted followed by multiple rounds of resuspension in
washing buffer (750 μg/ml UltraPure BSA and 0.04 U/ μl RNA
inhibitors— RNase OUT in PBS) before sorting. Nuclei were sorted on
an ARIA3 FACS sorter based on 7-AAD staining. Sorted nuclei were
counted on a LUNA cell counter, spun down, and resuspended in
washing buffer to the desired concentration according to the 10X
Genomics recommendations.
Multiomics library preparation
After FACS, samples were submitted to the KU Leuven Genomics
Core and processed using the 10X Genomics Next GEM Single Cell
Multiome Assay for Transposase-Accessible Chromatin (ATAC) +
Gene Expression Reagents kit to generate the gel beads-in-
emulsion (GEMs) containing single nuclei. Next, joint single-
nucleus RNA and single-nucleus ATAC libraries were generated
according to the 10X Genomics protocol. Finally, libraries were
sequenced at a depth of 30 K on Illumina NovaSeq 6000 by the KU
Leuven Genomics Core.
Multiomics data analysis
Raw data were processed by 10X Cell Ranger ARC to demultiplex raw
base call (BCL) ﬁles generated by Illumina sequencer into FASTQ
ﬁles. The FASTQ ﬁles were subsequently aligned to the mouse
reference genome mm10, and count matrices were generated for
both RNA and ATAC molecules. These un ﬁltered count matrices
were ﬁrst processed by CellBender to remove ambient RNA and
scDblFinder to remove doublets (Table S2). These ﬁltered matrices
were ﬁnally further processed by R packages Seurat v4.0 and Signac
v1.10. Per sample (Prdm16
WT and Prdm16cKO), a SeuratObject was
generated that included an RNA data slot for gene expression and
an ATAC data slot for chromatin fragments. Each SeuratObject was
quality-checked based on the number of unique molecular iden-
tiﬁers per cell, number of genes detected per cell, genes per unique
molecular identi ﬁer, mitochondrial RNA, nucleosome signal, and
TSS enrichment score. The exact thresholds used for both RNA data
and ATAC data slots on both samples are summarized in Table S2.
RNA data were processed, and normalization was performed fol-
lowed by principal component (PC) analysis, neighbor identiﬁcation
(k = 20), and Uniform Manifold Approximation and Projection
(UMAP). The number of PCs used for UMAP embeddings was cal-
culated as the last PC where the difference between two subse-
quent PCs was less than 0.1% in variation, being 11 PCs for Prdm16
WT
and 15 PCs for Prdm16cKO. After UMAP, clustering was performed
using the smart local moving algorithm (Waltman & van Eck, 2013)a t
a low resolution of each sample to identify the main cell pop-
ulations. These clusters were used to recall the peaks per sample
using MACS2 based on a combined set of peaks. After recalling the
peaks, ATAC data were normalized using the term frequency –
inverse document frequency (TF-IDF) followed by top feature se-
lection and singular value decomposition on the TD-IDF matrix. This
dimension reduction of ATAC data is known as late semantic
indexing. Late semantic indexing components were used for graph-
based clustering of the ATAC data as described for the RNA data.
Multiomics data integration
Datasets were merged and integrated for RNA and ATAC assays
based on anchor integration for each assay, separately. The batch
effect of the RNA datasets was corrected by reciprocal PC analysis
(RPCA). Finally, RNAseq and ATACseq data were integrated using
weighted nearest neighbor (WNN) analysis following the recom-
mended Seurat vignette for 10X Multiome datasets. Dimensional
reduction was performed on the integrated SeuratObject, now
containing both RNA and ATAC assays, using the FindMultiMo-
dalNeighbors function of Seurat. PCs used to ﬁnd neighbors and for
UMAP afterward were again calculated as described above. Clus-
tering was performed using the smart local moving algorithm,
initially at low resolution (0.09) to identify the main cell clusters,
then at high resolution (0.5 for MCs, 0.4 for ECs and CMs, and 0.1 for
FBs and ICs) to identify subclusters. Cluster marker genes were
identiﬁed using FindAllMarkers of the Seurat package. Thresholds
were set at Log
2FC > 0.25, min.diff.pct > 0.1, only.pos = TRUE, and
Pval_adj > 0.05. Cluster identities were annotated manually based
on literature (references included in the main text). For EC and MC
clusters, populations of 77 and 26 cells, respectively, were identi ﬁed
as contaminated (because of the mixed expression of marker genes
of different populations) and were therefore removed from these
clusters. Populations were compared using Fisher ’s exact test with
an FDR < 0.05 as a threshold for signi ﬁcance.
Downstream analysis on CMs
DEG and DAR analyses were performed using the FindMarkers
function on either the RNA or ATAC data slot, respectively. DEG
analysis was performed using the Wilcoxon test with thresholds
Pval_adj < 0.05. DAR analysis was performed using logistic re-
gression with the total number of ATAC fragments as a latent
variable, with thresholds Pval_adj < 0.05 and min.pct = 0.05. The R
PRDM16 determines cardiomyocyte fate Van Wauwe et al. https://doi.org/10.26508/lsa.202402719 vol 7 | no 12 | e202402719 19 of 25

package clusterProﬁler was used for GO and on the DEG lists, using
all genes detected as a list of background genes. Additional GO
analysis was done in ToppGene using the default settings. Analysis
for GO was performed with the Benjamini –Hochberg Pval_adj
method, p_val < 0.01, and q_val < 0.05. GO and functional anno-
tations of DARs were performed using rGREAT with default pa-
rameters, ﬁltered for p_val < 0.05. Annotation of the DARs was
performed using HOMER. Finally, peak-to-gene linkage analysis was
calculated for all associated peaks and genes using the built-in
function of Signac with default parameters.
Motif enrichment analysis
DARs were scanned for enriched motifs using the built-in function
of Signac (chromVAR) and using HOMER. PRDM16 binding motif was
constructed based on the CIS-BP database ( Weirauch et al, 2014 ),
and manually added to the HOMER library. Next, DARs were
scanned by HOMER to identify potential PRDM16 DNA binding
places.
GRN analysis
FigR was used to build GRNs based on the multiome input data.
From the complete merged cardiomyocyte Seurat_object, FigR ﬁrst
determines peak–gene associations based on our paired single-cell
accessibility (ATAC) and RNA count data. Per gene, signi ﬁcant
peak–gene associations are identi ﬁed as DORCs. Next, genes with
associated regulatory regions were ﬁltered for being differentially
expressed and for being known as either atrial-speci ﬁco r
conduction-speciﬁc, using previously established gene signatures
for each (Table S7) (Shekhar et al, 2018 ; Cao et al, 2023 ). FigR then
identiﬁes TF modulators linked to these regulatory regions and
genes to construct a GRN displaying TF –gene relationships. Default
parameters were used, with a transcription regulatory mean score
of 0.5. Heatmaps and networks were constructed following the FigR
manual.
Code
Non-custom analysis software was created to perform the analysis.
Images were analyzed using Fiji and QuPath built-in tools. Multiome
sequencing data were analyzed using standard R packages (R
v4.2.3), referred to throughout the article and in Table 2 .
Microscopy and imaging analysis
Fluorescence images of Fig 1 (Cy3, Alexa 568, TO-PRO-3) were taken
using a ZEISS LSM 700 laser scanning confocal microscope and a
Plan-Apochromat 63x/1.40 Oil DIC M27 objective ( Fig 1B) or a ZEISS
microscope equipped with an AxioCam 506 mono camera and EC
Plan-Neoﬂuar 10x/0.30 M27 objective to make mosaics and re-
construct full sagittal heart sections (Fig 1E ). Bright ﬁeld/polarized
light images of Sirius Red –stained sections in Fig 1D were taken
using a ZEISS microscope equipped with an AxioCam HRc camera
and an EC Plan-Neo ﬂuar 10x/0.30 M27 objective for mosaic images
to construct full heart sections and an EC Plan-Neo ﬂuar 20x/0.40
M27 objective for representative insets. Fluorescence images of Fig
2 (Alexa 568; Hoechst) were taken using a ZEISS microscope
equipped with an AxioCam 506 mono camera and an EC Plan-
Apochromat 20x/0.8 M27 objective ( Fig 2D). Fluorescence images of
Fig 4F (Alexa 488) were taken with a ZEISS microscope using an
AxioCam MRc5 camera and EC Plan-Neoﬂ uar 2.5x/0.075 M27 ob-
jective, or EC Plan-Neo ﬂuar 5x/0.15 M27 objective for insets. Fluo-
rescence images of Fig S1 (Alexa
 488, Alexa 568, TO-PRO-3; Hoechst)
were taken using a ZEISS LSM 700 laser scanning confocal micro-
scope using a Plan-Apochromat 20x/0.8 M27 objective (Fig S1G and
I) or a Plan-Apochromat 63x/1.40 Oil DIC M27 objective (Fig S1H and
J), or a ZEISS microscope equipped with an AxioCam 506 mono
camera with Plan-Apochromat 40x/0.95 Korr M27 objective to make
mosaics and reconstruct a full sagittal heart section (inset rep-
resents 1 tile of the mosaic; Fig S1E and F ). Brightﬁeld images of Fig
S1 were taken using a ZEISS Axio Observer microscope equipped
with an AxioCam MRc5 camera and EC Plan-Neoﬂ uar 20x/0.50 M27
objective ( Fig S1B and C ) or an EC Plan-Neo ﬂuar 40x/0.75 M27
objective (Fig S1D). Fluorescence images of Fig S2 (Alexa 488, Alexa
568; Hoechst) were taken using a ZEISS LSM 700 laser scanning
confocal microscope with an EC Plan-Neo ﬂuar 10x/0.30 M27 ob-
jective ( Fig S2B ) or a Plan-Apochromat 63x/1.40 Oil DIC M27 ob-
jective ( Fig S2C and E ), or a ZEISS microscope equipped with an
AxioCam 506 mono camera and an EC Plan-Neo ﬂuar 10x/0.30 M27
objective to make mosaics and reconstruct the full brain section
(Fig S2D) or an EC Plan-Apochromat 20x/0.8 M27 objective ( Fig S2D,
insets) to make mosaics of the area of interest or a ZEISS mi-
croscope with an AxioCam 506 mono camera and an EC Plan-
Apochromat 40x/0.95 Korr M27 objective ( Fig S2F ). Fluorescence
images of Fig S3 (Alexa 488) were taken using a ZEISS Axio Ob-
server microscope equipped with an AxioCam MRc5 camera and
EC Plan-Neo ﬂuar 2.5x/0.075 M27 objective to make mosaics and
reconstruct the full heart section. Bright ﬁeld images of Sirius
Red–stained sections in Fig S4C and G were taken using a ZEISS
microscope with AxioCam HRc camera and an EC Plan-Neo ﬂuar
10x/0.30 M27 objective for mosaic images to construct full heart
s e c t i o n sa n da nE CP l a n - N e oﬂuar 20x/0.40 M27 objective for
representative insets. Bright ﬁeld images of Fig S7C were taken
using a ZEISS microscope equipped with an AxioCam 506 color
camera and an EC Plan-Neo ﬂuar 10x/0.30 M27 objective to make
mosaics and reconstruct full sagittal heart section. Fluorescence
images of Fig S7D (Alexa 568; Hoechst) were taken using a ZEISS
microscope with an AxioCam 506 color camera and EC Plan-
Apochromat 20x/0.4 M27 objective to make mosaics and recon-
struct full sagittal heart section. Imaging software connected to
the microscope and camera was AxioVision or ZEN Blue. All images
were analyzed using Fiji or QuPath as indicated throughout the
article.
Statistics
Continuous data were presented as the mean ± SEM. Continuous
datasets were analyzed using GraphPad Prism v9.4.1. When both
groups were normally distributed (Shapiro –Wilk test), a parametric
two-sided unpaired t test was used. Where not all groups in an
experiment were normally distributed or when normality could not
be estimated by the Shapiro –Wilk test, a non-parametric Mann–
Whitney test was used. In case of comparing multiple groups for
echocardiography parameters, a two-way ANOVA with a Bonferroni
post hoc test was performed. The numbers of mice used for each
PRDM16 determines cardiomyocyte fate Van Wauwe et al. https://doi.org/10.26508/lsa.202402719 vol 7 | no 12 | e202402719 20 of 25

group were indicated in the (supplementary) ﬁgure legends and
supplementary tables. Data were considered signi ﬁcant when P <
0.05 (in case of multiple comparison, i.e., when analyzing the se-
quencing data, corrected by the Benjamini –Hochberg procedure;
referred to as Padjusted or FDR). Statistical analysis of the single-cell
multiome data was done in R (v4.2.3) using the aforementioned
packages Seurat, Signac, clusterProﬁler, and FigR. Populations were
compared using Fisher ’s exact test with an FDR < 0.05 as threshold
for signi ﬁcance.
Online supplemental materials
Table S1 summarizes echocardiography parameters of P7, 8- and 16-
wk-old mice, including statistics and sample sizes. Table S2 shows
the number of nuclei per condition after different quality control
steps. Table S3 lists marker genes for the cellular landscape of P7
hearts and the DEGs of Prdm16
cKO versus Prdm16WT FBs. Table S4
represents DEGs of Prdm16cKO versus Prdm16WT CMs. Table S5 rep-
resents DARs ofPrdm16cKO versus Prdm16WT CMs. Table S6 represents
GO terms related to both DEGs and DARs. Table S7 represents full
lists of DEGs overlapping with atrial, ventricular, conduction, or
working CMs, as well as lists of unique DEGs for atrial or conduction
CMs. Table S8 represents full lists of DARs overlapping with atrial,
ventricular, conduction, or working CMs. Table S9 represents a full
list of TF–gene regulation as shown on bar graphs and heatmaps of
Fig 5D and E. Fig S1 shows PRDM16 expression in the developing and
early postnatal heart, and ef ﬁciency and speci ﬁcity of Prdm16
deletion in the heart at P7 and SMC coverage of coronary arteries at
P7. Fig S2 shows mouse models used in this study, the activity
pattern of the SM22α -Cre reporter, and the speci ﬁcity of Prdm16
deletion in brains and lungs at P7. Fig S3 shows the analysis of the
compact layer thickness based on ENDOMUCIN staining. Fig S4
shows the cardiac phenotype of Prdm16
cKO mice and their WT
littermates at 8 and 16 wks of age. Fig S5 shows UMAPs, marker
genes, and cell proportions of re-clustered main cell populations
of the heart; and Prdm16 expression in the different subclusters.
Fig S6 shows the ventricular-to-atrial and working-to-conduction
s h i f t sb a s e do nD E G sa n dD A R s .Fig S7 shows the validation of the
expression of some DEGs by RT –qPCR or at the protein level (by
immunohistochemistry or immunoblotting). Fig S8 highlights the
PF cluster including the expression of known PF markers. Fig S9
shows TF motif analysis on all up-regulated DARs and highlights
overlapping 31 motifs between chromVAR and HOMER. In addition,
network analysis of TF –gene regulation using FigR is visualized,
highlighting the genes uniquely regulated by PRDM16. Fig S10
shows the expression of markers typical for trabecular or com-
pact CMs.
Data Availability
Sequencing reads and single-nucleus expression matrices have
b e e nd e p o s i t e di nN C B I’s Gene Expression Omnibus ( http://
www.ncbi.nlm.nih.gov/geo/). The accession number for the
snRNAseq and snATACseq data reported in this study is
GSE255382 . Any additional information required to reanalyze the
data reported in this study is available upon request from the lead
contact. All data were analyzed with standard programs and
packages as indicated in Table 2 . Non-custom analysis software
was created to perform the analysis. Further information on
and requests for resources and reagents should be directed
to and will be ful ﬁlled by the lead contact, Aernout Luttun
(aernout.luttun@kuleuven.be).
Supplementary Information
Supplementary Information is available at https://doi.org/10.26508/lsa.
202402719.
Acknowledgements
We thank P Vandervoort, E Caluw ´e, and M Lox (Center for Molecular and
Vascular Biology, KU Leuven, Leuven, Belgium) for technical assistance,
and K Sipido, R Vennekens, E Jones, and A Zwijsen for insightful discus-
sions. We acknowledge the KU Leuven Genomics Core for RNA and ATAC
sequencing. This work was supported by internal KU Leuven funding (C14/
19/095 to A Luttun, a Program Financing grant PF/10/014 to A Luttun, and
C14/21/093 to HL Roderick); a European Research Council Grant (FP7-StG-
IMAGINED203291) to A Luttun; three Fonds voor Wetenschappelijk
Onderzoek (FWO) grants (G099521N, G060923N, and WOG001420N to A
Luttun); three predoctoral FWO fellowships (1157318N to W Dheedene,
1S25817N to J Van Wauwe, and 11P9W24N to P Vrancaert); and one post-
doctoral FWO fellowship (1271824N to H Kemps). The multiomics studies
were funded by the support of the Belgian Heart Fund, in collaboration
with the Belgian Society for Cardiology, and managed by the King Baudouin
Foundation (2022-J1190990-225777).
Author Contributions
J Van Wauwe: conceptualization, data curation, formal analysis,
validation, investigation, visualization, methodology, and wri-
ting— original draft, review, and editing.
A Mahy: formal analysis, investigation, methodology, and wri-
ting— review and editing.
S Craps: formal analysis, investigation, methodology, and wri-
ting— review and editing.
S Ekhteraei-Tousi: data curation, investigation, methodology, and
writing— review and editing.
P Vrancaert: formal analysis, investigation, methodology, and wri-
ting— review and editing.
H Kemps: formal analysis, investigation, methodology, and wri-
ting— review and editing.
W Dheedene: formal analysis, investigation, methodology, and
writing— review and editing.
R Doñate Puertas: data curation, investigation, methodology, and
writing— review and editing.
S Trenson: investigation, methodology, and writing — review and
editing.
HL Roderick: resources, investigation, methodology, and wri-
ting— review and editing.
M Beerens: conceptualization, formal analysis, supervision, inves-
tigation, methodology, and writing — review and editing.
PRDM16 determines cardiomyocyte fate Van Wauwe et al. https://doi.org/10.26508/lsa.202402719 vol 7 | no 12 | e202402719 21 of 25

A Luttun: conceptualization, resources, data curation, formal
analysis, supervision, funding acquisition, and writing — original
draft, review, and editing.
Conﬂict of Interest Statement
The authors declare that they have no con ﬂict of interest.
References
A k e r b e r gB N ,G uF ,V a n D u s e nN J ,Z h a n gX ,D o n gR ,L iK ,Z h a n gB ,Z h o uB ,
Sethi I, Ma Q, et al (2019) A reference map of murine cardiac
transcription factor chromatin occupancy identiﬁ es dynamic and
conserved enhancers. Nat Commun 10: 4907. doi: 10.1038/s41467-
019-12812-3
Amoni M, Vermoortele D, Ekhteraei-Tousi S, Donate Puertas R, Gilbert G,
Youness M, Thienpont B, Willems R, Roderick HL, Claus P, et al (2023)
Heterogeneity of repolarization and cell-cell variability of
cardiomyocyte remodeling within the myocardial infarction border
zone contribute to arrhythmia susceptibility. Circ Arrhythm
Electrophysiol 16: e011677. doi: 10.1161/CIRCEP.122.011677
Aranguren XL, Agirre X, Beerens M, Coppiello G, Uriz M, Vandersmissen I,
Benkheil M, Panadero J, Aguado N, Pascual-Montano A, et al (2013)
Unraveling a novel transcription factor code determining the human
arterial-speciﬁc endothelial cell signature. Blood 122: 3982– 3992.
doi:10.1182/blood-2013-02-483255
Arndt AK, Schafer S, Drenckhahn JD, Sabeh MK, Plovie ER, Caliebe A, Klopocki
E, Musso G, Werdich AA, Kalwa H, et al (2013) Fine mapping of the 1p36
deletion syndrome identi ﬁes mutation of prdm16 as a cause of
cardiomyopathy. Am J Hum Genet 93: 67 –77. doi: 10.1016/
j.ajhg.2013.05.015
Asp M, Giacomello S, Larsson L, Wu C, Furth D, Qian X, Wardell E, Custodio J,
Reimegard J, Salmen F, et al (2019) A spatiotemporal organ-wide gene
expression and cell atlas of the developing human heart. Cell 179:
1647–1660.e19. doi: 10.1016/j.cell.2019.11.025
Baizabal JM, Mistry M, Garcia MT, Gomez N, Olukoya O, Tran D, Johnson MB,
Walsh CA, Harwell CC (2018) The epigenetic state of prdm16-regulated
enhancers in radial glia controls cortical neuron position. Neuron 98:
945–962.e8. doi: 10.1016/j.neuron.2018.04.033
Bankhead P, Loughrey MB, Fernandez JA, Dombrowski Y, McArt DG, Dunne PD,
McQuaid S, Gray RT, Murray LJ, Coleman HG, et al (2017) Qupath: Open
source software for digital pathology image analysis. Sci Rep 7: 16878.
doi:10.1038/s41598-017-17204-5
Bauters D, Cobbaut M, Geys L, Van Lint J, Hemmeryckx B, Lijnen HR (2017) Loss
of adamts5 enhances brown adipose tissue mass and promotes
browning of white adipose tissue via creb signaling. Mol Metab 6:
715–724. doi: 10.1016/j.molmet.2017.05.004
Berger SI, Ma’ayan A, Iyengar R (2010) Systems pharmacology of arrhythmias.
Sci Signal 3: ra30. doi: 10.1126/scisignal.2000723
Bjork BC, Turbe-Doan A, Prysak M, Herron BJ, Beier DR (2010) Prdm16 is
required for normal palatogenesis in mice. Hum Mol Genet 19:
774–789. doi: 10.1093/hmg/ddp543
Cao Y, Zhang X, Akerberg BN, Yuan H, Sakamoto T, Xiao F, VanDusen NJ, Zhou P,
Sweat ME, Wang Y, et al (2023) In vivo dissection of chamber-selective
enhancers reveals estrogen-related receptor as a regulator of
ventricular cardiomyocyte identity. Circulation 147: 881 –896.
doi:10.1161/CIRCULATIONAHA.122.061955
Chen J, Bardes EE, Aronow BJ, Jegga AG (2009) Toppgene suite for gene list
enrichment analysis and candidate gene prioritization. Nucleic Acids
Res 37: W305 –W311. doi: 10.1093/nar/gkp427
Choquet C, Kelly RG, Miquerol L (2020) Nkx2-5 de ﬁnes distinct scaffold and
recruitment phases during formation of the murine cardiac
purk
inje ﬁber network. Nat Commun 11: 5300. doi: 10.1038/s41467-
020-19150-9
Choquet C, Boulgakoff L, Kelly RG, Miquerol L (2021) New insights into the
development and morphogenesis of the cardiac purkinje ﬁber
network: Linking architecture and function. J Cardiovasc Dev Dis 8: 95.
doi:10.3390/jcdd8080095
Christoffels VM, Moorman AF (2009) Development of the cardiac conduction
system: Why are some regions of the heart more arrhythmogenic than
others? Circ Arrhythm Electrophysiol 2: 195 –207. doi: 10.1161/
CIRCEP.108.829341
Cibi DM, Bi-Lin KW, Shekeran SG, Sandireddy R, Tee N, Singh A, Wu Y,
Srinivasan DK, Kovalik JP, Ghosh S, et al (2020) Prdm16 deﬁciency leads
to age-dependent cardiac hypertrophy, adverse remodeling,
mitochondrial dysfunction, and heart failure. Cell Rep 33: 108288.
doi:10.1016/j.celrep.2020.108288
Cohen P, Levy JD, Zhang Y, Frontini A, Kolodin DP, Svensson KJ, Lo JC, Zeng X, Ye
L, Khandekar MJ, et al (2014) Ablation of prdm16 and beige adipose
causes metabolic dysfunction and a subcutaneous to visceral fat
switch. Cell 156: 304 –316. doi: 10.1016/j.cell.2013.12.021
Craps S, Van Wauwe J, De Moudt S, De Munck D, Leloup AJA, Boeckx B, Vervliet
T, Dheedene W, Criem N, Geeroms C, et al (2021) Prdm16 supports
arterial ﬂow recovery by maintaining endothelial function. Circ Res
129: 63 –77. doi: 10.1161/CIRCRESAHA.120.318501
Cui M, Wang Z, Chen K, Shah AM, Tan W, Duan L, Sanchez-Ortiz E, Li H, Xu L, Liu
N, et al (2020) Dynamic transcriptional responses to injury of
regenerative and non-regenerative cardiomyocytes revealed by
single-nucleus rna sequencing. Dev Cell 53: 102 –116.e8. doi: 10.1016/
j.devcel.2020.02.019
Daniels RE, Haq KT, Miller LS, Chia EW, Miura M, Sorrentino V, McGuire JJ,
Stuyvers BD (2017) Cardiac expression of ryanodine receptor subtype
3; a strategic component in the intracellular ca(2+) release system of
purkinje ﬁbers in large mammalian heart. J Mol Cell Cardiol 104: 31–42.
doi:10.1016/j.yjmcc.2017.01.011
DeLaughter DM, Bick AG, Wakimoto H, McKean D, Gorham JM, Kathiriya IS,
Hinson JT, Homsy J, Gray J, Pu W, et al (2016) Single-cell resolution of
temporal gene expression during heart development. Dev Cell 39:
480–490. doi: 10.1016/j.devcel.2016.10.001
Delplancq G, Tarris G, Vitobello A, Nambot S, Sorlin A, Philippe C, Carmignac V,
Duffourd Y, Denis C, Eicher JC, et al (2020) Cardiomyopathy due to
prdm16 mutation: First description of a fetal presentation, with
possible modi ﬁer genes. Am J Med Genet C Semin Med Genet 184:
129–135. doi: 10.1002/ajmg.c.31766
D iZ a z z oE ,D eR o s aC ,A b b o n d a n z aC ,M o n c h a r m o n tB( 2 0 1 3 )P r d m
proteins: Molecular mechanisms in signal transduction and
transcriptional regulation. Biology 2: 107 –141. doi: 10.3390/
biology2010107
Farrell E, Armstrong AE, Grimes AC, Naya FJ, de Lange WJ, Ralphe JC (2018)
Transcriptome analysis of cardiac hypertrophic growth in mybpc3-
null mice suggests early responders in hypertrophic remodeling.
Front
Physiol 9: 1442. doi: 10.3389/fphys.2018.01442
Fei LR, Huang WJ, Wang Y, Lei L, Li ZH, Zheng YW, Wang Z, Yang MQ, Liu CC, Xu
HT (2019) Prdm16 functions as a suppressor of lung
adenocarcinoma metastasis. J Exp Clin Cancer Res 38: 35.
doi:10.1186/s13046-019-1042-1
Fleming SJ, Chaf ﬁnM D ,A r d u i n iA ,A k k a dA D ,B a n k sE ,M a r i o n iJ C ,P h i l i p p a k i s
AA, Ellinor PT, Babadi M (2023) Unsupervised removal of systematic
background noise from droplet-based single-cell experiments
using cellbender. Nat Methods 20: 1323 –1335. doi: 10.1038/s41592-
023-01943-7
Funakoshi S, Fernandes I, Mastikhina O, Wilkinson D, Tran T, Dhahri W, Mazine
A, Yang D, Burnett B, Lee J, et al (2021) Generation of mature compact
PRDM16 determines cardiomyocyte fate Van Wauwe et al. https://doi.org/10.26508/lsa.202402719 vol 7 | no 12 | e202402719 22 of 25

ventricular cardiomyocytes from human pluripotent stem cells. Nat
Commun 12: 3155. doi: 10.1038/s41467-021-23329-z
Germain PL, Lun A, Garcia Meixide C, Macnair W, Robinson MD (2021) Doublet
identiﬁcation in single-cell sequencing data using scdbl ﬁnder.
F1000Res 10: 979. doi: 10.12688/f1000research.73600.2
Goodyer WR, Beyersdorf BM, Paik DT, Tian L, Li G, Buikema JW, Chirikian O,
Choi S, Venkatraman S, Adams EL, et al (2019) Transcriptomic
proﬁling of the developing cardiac conduction system at single-
cell resolution. Circ Res 125: 379 –397. doi: 10.1161/
CIRCRESAHA.118.314578
Gu Z, Hubschmann D (2023) Rgreat: An r/bioconductor package for functional
enrichment on genomic regions. Bioinformatics 39: btac745.
doi:10.1093/bioinformatics/btac745
Haissaguerre M, Vigmond E, Stuyvers B, Hocini M, Bernus O (2016) Ventricular
arrhythmias and the his-purkinje system. Nat Rev Cardiol 13: 155–166.
doi:10.1038/nrcardio.2015.193
Harms MJ, Ishibashi J, Wang W, Lim HW, Goyama S, Sato T, Kurokawa M, Won KJ,
Seale P (2014) Prdm16 is required for the maintenance of brown
adipocyte identity and function in adult mice. Cell Metab 19: 593–604.
doi:10.1016/j.cmet.2014.03.007
Hartung H, Feldman B, Lovec H, Coulier F, Birnbaum D, Goldfarb M (1997)
Murine fgf-12 and fgf-13: Expression in embryonic nervous system,
connective tissue and heart. Mech Dev 64: 31 –39. doi: 10.1016/s0925-
4773(97)00042-7
Heinz S, Benner C, Spann N, Bertolino E, Lin YC, Laslo P, Cheng JX, Murre C,
Singh H, Glass CK (2010) Simple combinations of lineage-determining
transcription factors prime cis-regulatory elements required for
macrophage and b cell identities. Mol Cell 38: 576 –589. doi: 10.1016/
j.molcel.2010.05.004
Holtwick R, Gotthardt M, Skryabin B, Steinmetz M, Potthast R, Zetsche B,
Hammer RE, Herz J, Kuhn M (2002) Smooth muscle-selective deletion
of guanylyl cyclase-a prevents the acute but not chronic effects of
anp on blood pressure. Proc Natl Acad Sci U S A 99: 7142 –7147.
doi:10.1073/pnas.102650499
H o n gK W ,L i mJ E ,K i mJ W ,T a b a r aY ,U e s h i m aH ,M i k iT ,M a t s u d aF ,C h oY S ,K i m
Y, Oh B (2014) Identi ﬁcation of three novel genetic variations
associated with electrocardiographic traits (qrs duration and pr
interval) in east asians. Hum Mol Genet 23: 6659 –6667. doi: 10.1093/
hmg/ddu374
Hu P, Liu J, Zhao J, Wilkins BJ, Lupino K, Wu H, Pei L (2018) Single-nucleus
transcriptomic survey of cell diversity and functional maturation in
postnatal mammalian hearts. Genes Dev 32: 1344 –1357. doi: 10.1101/
gad.316802.118
Jiang N, Yang M, Han Y, Zhao H, Sun L (2022) Prdm16 regulating adipocyte
transformation and thermogenesis: A promising therapeutic target
for obesity and diabetes. Front Pharmacol 13: 870250. doi: 10.3389/
fphar.2022.870250
Kajimura S, Seale P, Tomaru T, Erdjument-Bromage H, Cooper MP, Ruas JL,
Chin S, Tempst P, Lazar MA, Spiegelman BM (2008) Regulation of the
brown and white fat gene programs through a prdm16/ctbp
transcriptional complex. Genes Dev 22: 1397 –1409.
doi: 10.1101/
gad.1666108
Kane C, Terracciano CMN (2017) Concise review: Criteria for chamber-speci ﬁc
categorization of human cardiac myocytes derived from pluripotent
stem cells. Stem Cells 35: 1881– 1897. doi: 10.1002/stem.2649
Kang JO, Ha TW, Jung HU, Lim JE, Oh B (2022) A cardiac-null mutation of
prdm16 causes hypotension in mice with cardiac hypertrophy via
increased nitric oxide synthase 1. PLoS One 17: e0267938. doi: 10.1371/
journal.pone.0267938
Kartha VK, Duarte FM, Hu Y, Ma S, Chew JG, Lareau CA, Earl A, Burkett ZD,
Kohlway AS, Lebofsky R, et al (2022) Functional inference of gene
regulation using single-cell multi-omics. Cell Genom 2: 100166.
doi:10.1016/j.xgen.2022.100166
Kodo K, Ong SG, Jahanbani F, Termglinchan V, Hirono K, InanlooRahatloo K,
Ebert AD, Shukla P, Abilez OJ, Churko JM, et al (2016) iPSC-derived
cardiomyocytes reveal abnormal TGF- β signalling in left ventricular
non-compaction cardiomyopathy. Nat Cell Biol 18: 1031 –1042.
doi:10.1038/ncb3411
Koibuchi N, Chin MT (2007) Chf1/hey2 plays a pivotal role in left ventricular
maturation through suppression of ectopic atrial gene expression.
Circ Res 100: 850 –855. doi: 10.1161/01.RES.0000261693.13269.bf
Kramer RJ, Fatahian AN, Chan A, Mortenson J, Osher J, Sun B, Parker LE,
Rosamilia MB, Potter KB, Moore K, et al (2023) Prdm16 deletion is
associated with sex-dependent cardiomyopathy and cardiac
mortality: A translational, multi-institutional cohort study. Circ Genom
Precis Med 16: 390 –400. doi: 10.1161/CIRCGEN.122.003912
Kuhnisch J, Theisen S, Dartsch J, Fritsche-Guenther R, Kirchner M, Obermayer
B, Bauer A, Kahlert AK, Rothe M, Beule D, et al (2024) Prdm16 mutation
determines sex-speciﬁc cardiac metabolism and identi ﬁes two novel
cardiac metabolic regulators. Cardiovasc Res 119: 2902 –2916.
doi:10.1093/cvr/cvad154
Li L, Miano JM, Cserjesi P, Olson EN (1996) Sm22 alpha, a marker of adult
smooth muscle, is expressed in multiple myogenic lineages during
embryogenesis. Circ Res 78: 188 –195. doi: 10.1161/01.res.78.2.188
Li X, Wang J, Jiang Z, Guo F, Soloway PD, Zhao R (2015) Role of prdm16 and its pr
domain in the epigenetic regulation of myogenic and adipogenic
genes during transdifferentiation of c2c12 cells. Gene 570: 191 –198.
doi:10.1016/j.gene.2015.06.017
Li G, Xu A, Sim S, Priest JR, Tian X, Khan T, Quertermous T, Zhou B, Tsao PS,
Quake SR, et al (2016) Transcriptomic pro ﬁling maps anatomically
patterned subpopulations among single embryonic cardiac cells. Dev
Cell 39: 491 –507. doi: 10.1016/j.devcel.2016.10.014
L iZ ,Y a oF ,Y uP ,L iD ,Z h a n gM ,M a oL ,S h e nX ,R e nZ ,W a n gL ,Z h o uB( 2 0 2 2 )
Postnatal state transition of cardiomyocyte as a primary step in
heart maturation. Protein Cell 13: 842 –862. doi: 10.1007/s13238-022-
00908-4
Litvinukova M, Talavera-Lopez C, Maatz H, Reichart D, Worth CL, Lindberg EL,
Kanda M, Polanski K, Heinig M, Lee M, et al (2020) Cells of the adult
human heart. Nature 588:
 466–472. doi: 10.1038/s41586-020-2797-4
Long PA, Evans JM, Olson TM (2017) Diagnostic yield of whole exome
sequencing in pediatric dilated cardiomyopathy. J Cardiovasc Dev Dis
4: 11. doi: 10.3390/jcdd4030011
Lupu IE, De Val S, Smart N (2020) Coronary vessel formation in development
and disease: Mechanisms and insights for therapy. Nat Rev Cardiol 17:
790–806. doi: 10.1038/s41569-020-0400-1
Luxan G, Casanova JC, Martinez-Poveda B, Prados B, D’Amato G, MacGrogan D,
Gonzalez-Rajal A, Dobarro D, Torroja C, Martinez F, et al (2013)
Mutations in the notch pathway regulator mib1 cause left ventricular
noncompaction cardiomyopathy. Nat Med 19: 193 –201. doi: 10.1038/
nm.3046
MacGrogan D, Munch J, de la Pompa JL (2018) Notch and interacting signalling
pathways in cardiac development, disease, and regeneration. Nat Rev
Cardiol 15: 685 –704. doi: 10.1038/s41569-018-0100-2
Marks AR (2013) Calcium cycling proteins and heart failure: Mechanisms and
therapeutics. J Clin Invest 123: 46 –52. doi: 10.1172/JCI62834
Mazzarotto F, Hawley MH, Beltrami M, Beekman L, de Marvao A, McGurk KA,
Statton B, Boschi B, Girolami F, Roberts AM, et al (2021) Systematic
large-scale assessment of the genetic architecture of left ventricular
noncompaction reveals diverse etiologies. Genet Med 23: 856 –864.
doi:10.1038/s41436-020-01049-x
Mikawa T, Gourdie RG, Takebayashi-Suzuki K, Kanzawa N, Hyer J, Pennisi DJ,
Poma CP, Shulimovich M, Diaz KG, Layliev J, et al (2003) Induction and
patterning of the purkinje ﬁbre network. Novartis Found Symp 250:
142–153. doi: 10.1002/0470868066.ch9
Muhl L, Genove G, Leptidis S, Liu J, He L, Mocci G, Sun Y, Gustafsson S,
Buyandelger B, Chivukula IV, et al (2020) Single-cell analysis uncovers
PRDM16 determines cardiomyocyte fate Van Wauwe et al. https://doi.org/10.26508/lsa.202402719 vol 7 | no 12 | e202402719 23 of 25

ﬁbroblast heterogeneity and criteria for ﬁbroblast and mural cell
identiﬁcation and discrimination. Nat Commun 11: 3953. doi: 10.1038/
s41467-020-17740-1
Munshi NV (2012) Gene regulatory networks in cardiac conduction system
development. Circ Res 110: 1525 –1537. doi: 10.1161/
CIRCRESAHA.111.260026
Nam JM, Lim JE, Ha TW, Oh B, Kang JO (2020) Cardiac-speci ﬁc inactivation of
prdm16 effects cardiac conduction abnormalities and
cardiomyopathy-associated phenotypes. Am J Physiol Heart Circ
Physiol 318: H764 –H777. doi: 10.1152/ajpheart.00647.2019
Ng SY, Wong CK, Tsang SY (2010) Differential gene expressions in atrial and
ventricular myocytes: Insights into the road of applying embryonic
stem cell-derived cardiomyocytes for future therapies. Am J Physiol
Cell Physiol 299: C1234 –C1249. doi: 10.1152/ajpcell.00402.2009
Pallante BA, Giovannone S, Fang-Yu L, Zhang J, Liu N, Kang G, Dun W, Boyden
PA, Fishman GI (2010) Contactin-2 expression in the cardiac purkinje
ﬁber network. Circ Arrhythm Electrophysiol 3: 186– 194. doi: 10.1161/
CIRCEP.109.928820
Pawlak M, Kedzierska KZ, Migdal M, Karim AN, Ramilowski JA, Bugajski L,
Hashimoto K, Marconi A, Piwocka K, Carninci P, et al (2019) Dynamics of
cardiomyocyte transcriptome and chromatin landscape demarcates
key events of heart development. Genome Res 29: 506– 519.
doi:10.1101/gr.244491.118
Pinheiro I, Margueron R, Shukeir N, Eisold M, Fritzsch C, Richter FM, Mittler G,
Genoud C, Goyama S, Kurokawa M, et al (2012) Prdm3 and prdm16 are
h3k9me1 methyltransferases required for mammalian
heterochromatin integrity. Cell 150: 948 –960. doi: 10.1016/
j.cell.2012.06.048
Rubart M, Tao W, Lu XL, Conway SJ, Reuter SP, Lin SF, Soonpaa MH (2018)
Electrical coupling between ventricular myocytes and myo ﬁbroblasts
in the infarcted mouse heart. Cardiovasc Res 114: 389 –400.
doi:10.1093/cvr/cvx163
Schep AN, Wu B, Buenrostro JD, Greenleaf WJ (2017) Chromvar: Inferring
transcription-factor-associated accessibility from single-cell
epigenomic data. Nat Methods 14: 975 –978. doi: 10.1038/nmeth.4401
Schindelin J, Arganda-Carreras I, Frise E, Kaynig V, Longair M, Pietzsch T,
Preibisch S, Rueden C, Saalfeld S, Schmid B, et al (2012) Fiji: An open-
source platform for biological-image analysis. Nat Methods 9:
676–682. doi: 10.1038/nmeth.2019
Seale P, Kajimura S, Yang W, Chin S, Rohas LM, Uldry M, Tavernier G, Langin D,
Spiegelman BM (2007) Transcriptional control of brown fat
determination by prdm16. Cell Metab 6: 38 –54. doi: 10.1016/
j.cmet.2007.06.001
Shekhar A, Lin X, Lin B, Liu FY, Zhang J, Khodadadi-Jamayran A, Tsirigos A, Bu L,
Fishman GI, Park DS (2018) Etv1 activates a rapid conduction
transcriptional program in rodent and human cardiomyocytes. Sci
Rep 8:
9944. doi: 10.1038/s41598-018-28239-7
Shimada IS, Acar M, Burgess RJ, Zhao Z, Morrison SJ (2017) Prdm16 is required
for the maintenance of neural stem cells in the postnatal forebrain
and their differentiation into ependymal cells. Genes Dev 31:
1134–1146. doi: 10.1101/gad.291773.116
Sousa VH, Miyoshi G, Hjerling-Lef ﬂer J, Karayannis T, Fishell G (2009)
Characterization of nkx6-2-derived neocortical interneuron lineages.
Cereb Cortex 19: i1 –i10. doi: 10.1093/cercor/bhp038
Steimle JD, Rankin SA, Slagle CE, Bekeny J, Rydeen AB, Chan SS, Kweon J,
Yang XH, Ikegami K, Nadadur RD, et al (2018) Evolutionarily
conserved tbx5-wnt2/2b pathway orchestrates cardiopulmonary
development. Proc Natl Acad Sci U S A 115: E10615 –E10624.
doi:10.1073/pnas.1811624115
Strassman A, Schnutgen F, Dai Q, Jones JC, Gomez AC, Pitstick L, Holton NE,
Moskal R, Leslie ER, von Melchner H, et al (2017) Generation of a
multipurpose prdm16 mouse allele by targeted gene trapping. Dis
Model Mech 10: 909 –922. doi: 10.1242/dmm.029561
Sun B, Rouzbehani OMT, Kramer RJ, Ghosh R, Perelli RM, Atkins S, Fatahian
AN, Davis K, Szulik MW, Goodman MA, et al (2023) Nonsense
variant PRDM16-Q187X causes impaired myocardial development
and TGF- β signaling resulting in noncompaction cardiomyopathy
in humans and mice. Circ Heart Fail 16: e010351. doi: 10.1161/
CIRCHEARTFAILURE.122.010351
Sweat ME, Cao Y, Zhang X, Burnicka-Turek O, Perez-Cervantes C, Arulsamy K,
Lu F, Keating EM, Akerberg BN, Ma Q, et al (2023) Tbx5 maintains atrial
identity in post-natal cardiomyocytes by regulating an atrial-speci ﬁc
enhancer network. Nat Cardiovasc Res 2: 881–898. doi:10.1038/s44161-
023-00334-7
Thompson M, Sakabe M, Verba M, Hao J, Meadows SM, Lu QR, Xin M (2023)
Prdm16 regulates arterial development and vascular integrity. Front
Physiol 14: 1165379. doi: 10.3389/fphys.2023.1165379
Tian G, Li J, Wang W, Zhou L (2024) Fgf12 restrains mitochondria-dependent
ferroptosis in doxorubicin-induced cardiomyocytes through the
activation of fgfr1/ampk/nrf2 signaling. Drug Dev Res 85: e22149.
doi:10.1002/ddr.22149
Toib A, Zhang C, Borghetti G, Zhang X, Wallner M, Yang Y, Troupes CD, Kubo H,
Sharp TE, Feldsott E, et al (2017) Remodeling of repolarization and
arrhythmia susceptibility in a myosin-binding protein c knockout
mouse model. Am J Physiol Heart Circ Physiol 313: H620 –H630.
doi:10.1152/ajpheart.00167.2017
Tucker NR, Chaf ﬁn M, Fleming SJ, Hall AW, Parsons VA, Bedi KC Jr., Akkad AD,
Herndon CN, Arduini A, Papangeli I, et al (2020) Transcriptional and
cellular diversity of the human heart. Circulation 142: 466 –482.
doi:10.1161/CIRCULATIONAHA.119.045401
van Waning JI, Caliskan K, Hoedemaekers YM, van Spaendonck-Zwarts KY,
Baas AF, Boekholdt SM, van Melle JP, Teske AJ, Asselbergs FW, Backx A,
et al (2018) Genetics, clinical features, and long-term outcome of
noncompaction cardiomyopathy. J Am Coll Cardiol 71: 711 –722.
doi:10.1016/j.jacc.2017.12.019
Van Wauwe J, Craps S, KC A, Asuncion L, Vrancaert P, Daems D, Finck C,
W r i g h tS ,A l a w iM ,M ü l l e rC ,e ta l( 2 0 2 4 )P r d m 1 6a m p l iﬁes notch
signaling and suppresses venous lineage speci ﬁcation to prevent
arteriovenous malformations during vascular development.
BioRxiv .d
o i : 10.1101/2021.12.05.471275 (Preprint posted June 5,
2024).
Veliskova J, Marra C, Liu Y, Shekhar A, Park DS, Iatckova V, Xie Y, Fishman GI,
Velisek L, Goldfarb M (2021) Early onset epilepsy and sudden
unexpected death in epilepsy with cardiac arrhythmia in mice
carrying the early infantile epileptic encephalopathy 47 gain-of-
function fhf1(fgf12) missense mutation. Epilepsia 62: 1546 –1558.
doi:10.1111/epi.16916
Vigil-Garcia M, Demkes CJ, Eding JEC, Versteeg D, de Ruiter H, Perini I,
Kooijman L, Gladka MM, Asselbergs FW, Vink A, et al (2021) Gene
expression pro ﬁling of hypertrophic cardiomyocytes identi ﬁes new
players in pathological remodelling. Cardiovasc Res 117: 1532 –1545.
doi:10.1093/cvr/cvaa233
Vincentz JW, Firulli BA, Toolan KP, Arking DE, Sotoodehnia N, Wan J, Chen PS,
de Gier-de Vries C, Christoffels VM, Rubart-von der Lohe M, et al (2019)
Variation in a left ventricle-speci ﬁc hand1 enhancer impairs gata
transcription factor binding and disrupts conduction system
development and function. Circ Res 125: 575 –589. doi: 10.1161/
CIRCRESAHA.119.315313
Waltman L, van Eck NJ (2013) A smart local moving algorithm for large-scale
modularity-based community detection. Eur Phys J B 86: 471.
doi:10.1140/epjb/e2013-40829-0
Wang Z, Zhao X, Zhao G, Guo Y, Lu H, Mu W, Zhong J, Garcia-Barrio M, Zhang J,
Chen YE, et al (2023) Prdm16 de ﬁciency in vascular smooth muscle
cells aggravates abdominal aortic aneurysm. JCI Insight 8: e167041.
doi:10.1172/jci.insight.167041
Wei EQ, Barnett AS, Pitt GS, Hennessey JA (2011) Fibroblast growth factor
homologous factors in the heart: A potential locus for cardiac
PRDM16 determines cardiomyocyte fate Van Wauwe et al. https://doi.org/10.26508/lsa.202402719 vol 7 | no 12 | e202402719 24 of 25

arrhythmias. Trends Cardiovasc Med 21: 199 –203. doi: 10.1016/
j.tcm.2012.05.010
Weirauch MT, Yang A, Albu M, Cote AG, Montenegro-Montero A, Drewe P,
Najafabadi HS, Lambert SA, Mann I, Cook K, et al (2014) Determination
and inference of eukaryotic transcription factor sequence speci ﬁcity.
Cell 158: 1431 –1443. doi: 10.1016/j.cell.2014.08.009
Wiencierz AM, Kernbach M, Ecklebe J, Monnerat G, Tomiuk S, Raulf A, Christalla
P, Malan D, Hesse M, Bosio A, et al (2015) Differential expression levels
of integrin α6 enable the selective identiﬁcation and isolation of atrial
and ventricular cardiomyocytes. PLoS One 10: e0143538. doi: 10.1371/
journal.pone.0143538
Wu T, Liang Z, Zhang Z, Liu C, Zhang L, Gu Y, Peterson KL, Evans SM, Fu XD, Chen
J (2022) Prdm16 is a compact myocardium-enriched transcription
factor required to maintain compact myocardial cardiomyocyte
identity in left ventricle. Circulation 145: 586 –602. doi: 10.1161/
CIRCULATIONAHA.121.056666
Yu G, Wang LG, Han Y, He QY (2012) Clusterpro ﬁler: An r package for
comparing biological themes among gene clusters. OMICS 16: 284–287.
doi:10.1089/omi.2011.0118
Zhang J, Wu L, Li Z, Fu G (2017) Mir-1231 exacerbates arrhythmia by targeting
calciumchannel gene cacna2d2 in myocardial infarction. Am J Transl
Res 9: 1822 –1833. doi: 10.1093/europace/eux230
License: This article is available under a Creative
Commons License (Attribution 4.0 International, as
described at https://creativecommons.org/
licenses/by/4.0/).
PRDM16 determines cardiomyocyte fate Van Wauwe et al. https://doi.org/10.26508/lsa.202402719 vol 7 | no 12 | e202402719 25 of 25

Advertisement 
BeerensAernout Luttun
Kemps, Wouter Dheedene, Rosa Doñate Puertas, Sander Trenson, H. Llewelyn Roderick, Manu 
Jore Van Wauwe, Alexia Mahy, Sander Craps, Samaneh Ekhteraei-Tousi, Pieter Vrancaert, Hannelore
  
suppressing alternative cell fates
PRDM16 determines specification of ventricular cardiomyocytes by
http://doi.org/10.26508/lsa.202402719
Vol 7 | No 12 | e202402719