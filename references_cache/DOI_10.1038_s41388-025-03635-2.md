---
reference_id: "DOI:10.1038/s41388-025-03635-2"
title: "Dissecting neuroblastoma heterogeneity through single-cell multi-omics: insights into development, immunity, and therapeutic resistance"
authors:
- Guo-qian He
- Si-jia He
- Xiao-yu Jing
- Yi-ling Dai
- Xia Guo
- Ju Gao
- Wei Zhang
journal: Oncogene
year: '2026'
doi: 10.1038/s41388-025-03635-2
content_type: full_text_pdf
full_text_attempted: true
full_text_provider: openalex
full_text_url: "https://www.nature.com/articles/s41388-025-03635-2.pdf"
oa_status: hybrid
license: cc-by-nc-nd
local_pdf_path: files/DOI_10.1038_s41388-025-03635-2.pdf
---

# Dissecting neuroblastoma heterogeneity through single-cell multi-omics: insights into development, immunity, and therapeutic resistance
**Authors:** Guo-qian He, Si-jia He, Xiao-yu Jing, Yi-ling Dai, Xia Guo, Ju Gao, Wei Zhang
**Journal:** Oncogene (2026)
**DOI:** [10.1038/s41388-025-03635-2](https://doi.org/10.1038/s41388-025-03635-2)

## Content

REVIEW ARTICLE OPEN
Dissecting neuroblastoma heterogeneity through single-cell
multi-omics: insights into development, immunity, and
therapeutic resistance
Guo-qian He 1,2, Si-jia He 1,2, Xiao-yu Jing 1,2, Yi-ling Dai 1,2, Xia Guo 1,3 ✉, Ju Gao 1,3 ✉ and Wei Zhang 4 ✉
© The Author(s) 2025
Neuroblastoma (NB), the most common extracranial solid tumor in children, is characterized by remarkable cellular heterogeneity
and clinical variability ranging from spontaneous regression to aggressive progression and relapse. Despite advances in multimodal
therapies, including surgery, chemotherapy, radiotherapy, differentiation therapy, and immunotherapy — treatment resistance
remains the principal barrier to improving survival in high-risk patients. Recent single-cell and spatial multi-omics studies have
revolutionized our understanding of NB by revealing its developmental origins, lineage hierarchy, and adaptive evolution under
therapeutic pressure. These technologies have delineated distinct cellular states along an adrenergic –mesenchymal continuum and
uncovered the dynamic interplay between tumor cells and their microenvironment. Genetic instability, epigenetic reprogramming,
and metabolic plasticity cooperate with immune and stromal remodeling to drive tumor persistence and relapse. At the molecular
level, mechanisms such as MYCN-driven chromatin remodeling, super-enhancer reorganization, bypass signaling activation,
quiescent persister programs, immune checkpoint engagement, and metabolic rewiring collectively enable therapeutic escape.
Importantly, these processes are reversible, highlighting tumor plasticity as both a hallmark and a potential vulnerability of NB.
Integrating single-cell transcriptomics, epigenomics, and spatial pro ﬁling provides an unprecedented framework to map resistance
evolution, identify lineage-speci ﬁc vulnerabilities, and guide rational combination strategies. Targeting epigenetic regulators,
metabolic checkpoints, and immune suppressive networks in a temporally coordinated manner holds promise for converting NB
from an adaptive to a controllable disease.
Oncogene (2026) 45:123–139; https://doi.org/10.1038/s41388-025-03635-2
INTRODUCTION
Neuroblastoma (NB) is one of the most prevalent pediatric solid
tumors, arising from neural crest –derived progenitors of the
sympathetic nervous system, most commonly in the adrenal
medulla, sympathetic chain, or abdominal regions [ 1, 2]. It
represents 8% –10% of all childhood cancers and occurs pre-
dominantly in children under ﬁve years of age, with earlier onset
generally predicting more favorable outcomes [ 3]. Clinically, NB is
characterized by striking heterogeneity, ranging from tumors with
spontaneous regression to highly aggressive and lethal forms. At
diagnosis, most high-risk cases already present metastatic spread
typically to bone marrow, bone, or lymph nodes [ 4, 5]. Despite
steady progress in multimodal therapy, including chemotherapy,
radiotherapy, surgical resection, autologous stem cell transplanta-
tion, and immunotherapy, long-term outcomes remain poor, with
ﬁve-year survival in high-risk NB lingering around 40% –50% [6–8].
Targeted therapy for NB is still limited. To date, most molecular
approaches have focused on ALK mutations, yet these alterations
are restricted to a minority of patients, underscoring the urgent
need to identify additional oncogenic drivers and actionable
therapeutic targets [9–12]. Immunotherapy has delivered the most
notable breakthrough to date, particularly with anti-GD2 mono-
clonal antibodies. The pivotal COG ANBL0032 trial demonstrated
that dinutuximab, combined with GM-CSF, IL-2, and retinoic acid
after autologous transplantation, signi ﬁcantly improved outcomes,
raising two-year event-free survival from 46% to 66% and overall
survival from 75% to 86% [ 13]. Subsequent long-term follow-up
and meta-analyses con ﬁrmed durable bene ﬁts, with 2 –5-year
survival rates increasing by approximately 10 –25 percentage
points, establishing anti-GD2 therapy as standard post-
consolidation treatment [ 14–16]. Yet, this progress has not
eliminated the grim prognosis of high-risk NB: more than half of
patients still relapse within ﬁve years, and recurrent tumors
frequently display heightened chemoresistance [ 7, 8]. Other
immunotherapeutic modalities, such as CAR T-cell therapy, remain
experimental, with limited ef ﬁcacy and signi ﬁ
cant toxicity [ 17–20].
These realities underscore that while NB therapy has advanced,
curative outcomes remain elusive.
A major impediment is the profound intratumoral heterogene-
ity of NB, which traditional bulk genomic or transcriptomicReceived: 24 June 2025 Revised: 1 November 2025 Accepted: 12 November 2025
Published online: 27 November 2025
1Department of Pediatrics, West China Second University Hospital, Sichuan University, Chengdu, Sichuan, China. 2Key Laboratory of Birth Defects and Related Diseases of Women
and Children (Sichuan University), Ministry of Education, Chengdu, Sichuan, China. 3NHC Key Laboratory of Chronobiology, Sichuan University, Chengdu, China. 4Department of
medical oncology, Sichuan Clinical Research Center for Cancer, Sichuan Cancer Hospital&Institute, Sichuan Cancer Center, School of Medicine, Uni versity of Electronic Science
and Technology of China, Chengdu, China. ✉email: guoxkl@163.com; gaoju651220@126.com; zhangwei850603@163.com
www.nature.com/oncOncogene
1234567890();,:

methods cannot capture [ 21–23]. Recent single-cell RNA sequen-
cing (scRNA-seq) studies have begun to resolve this complexity,
revealing diverse cellular lineages, functional plasticity, and
intricate interactions within the tumor microenvironment
[24, 25]. These insights have uncovered novel mechanisms of
tumorigenesis, therapeutic resistance, and relapses, while laying
the foundation for precision therapies tailored to tumor archi-
tecture at single-cell resolution.
In this review, we discuss recent progress in applying single-cell
technologies to NB, highlighting their potential to unravel tumor
heterogeneity and inform precision oncology.
COMPARISON OF EXISTING SINGLE-CELL TECHNOLOGIES FOR
CANCER RESEARCH
Single-cell technologies have emerged as a disruptive methodo-
logical innovation in cancer research. What was once narrowly
conﬁned to single-cell transcriptomics has now expanded into a
comprehensive framework of “broad-spectrum single-cell omics, ”
encompassing the transcriptome, epigenome, genome, proteome,
and even metabolome (Fig. 1). This multi-omics system provides a
technical foundation for systematically dissecting tumor initiation,
progression, microenvironmental remodeling, and therapeutic
responses at the single-cell level. By uncovering the profound
heterogeneity of tumor cell populations and their evolutionary
trajectories, it enables detailed mapping of tumor –immune
interactions and in-depth exploration of mechanisms such as
drug resistance and immune evasion. In doing so, single-cell omics
is driving a paradigm shift from population-level observation to
individual-level decoding, fundamentally reshaping our under-
standing of cancer biology.
Single-cell transcriptomic technologies: characterizing cell
states and reconstructing lineages
Among single-cell omics approaches, transcriptomic pro ﬁling is
the most mature and widely used, serving as a key entry point for
understanding cellular states and functions [ 26, 27]. Current
platforms include single-cell RNA sequencing (scRNA-seq), single-
nucleus RNA sequencing (snRNA-seq), and spatial transcriptomics
(scST), which provide complementary perspectives in terms of
cellular resolution, tissue adaptability, and spatial organization. As
mRNA expressions most directly re ﬂect cellular responses and
functional states, scRNA-seq has become the primary tool for
dissecting tumor heterogeneity, reconstructing developmental
trajectories, and pro ﬁling immune cell composition [ 28–30]. It has
been extensively applied across solid and hematological malig-
nancies, supported by a robust analytical toolkit, although it
remains constrained by reliance on high-quality tissue dissociation
and limits in sequencing depth and resolution [ 31, 32].
snRNA-seq offers an effective alternative for samples that are
difﬁcult to dissociate, structurally dense, or frozen [ 33]. By
capturing nuclear transcripts without enzymatic digestion, it
avoids stress-induced artifacts and enhances data stability
[26, 34], making it particularly valuable for tumors with complex
structures such as NB [ 35] and glioblastoma (GBM) [ 36].
Both scRNA-seq and snRNA-seq, however, lack spatial information.
scST overcomes this limitation by mapping gene expression to
tissue coordinates, integrating cell identity, functional state, and
structural context. This provides unprecedented insights into
tumor–immune architecture, cell –cell interactions and spatially
driven immunosuppressive niches (e.g., studies in medulloblastoma
[37]; glioma niche analyses [ 38]; immune macrophage subpopula-
tion spatial proﬁ
ling [39]). These technologies have already yielded
Transcriptomics
(scRNA-seq,snRNA-seq,scST)
sc/snRNA-Seq
scST
scDNA-seq
scATAC-seq scMS
Epigenomic
(SCATAC-seq)
Proteomics
Metabolomics
(scMS)
Genomics
(scDNA-seq)
Single cell
Multi-omics
IMC
CyTOF
CODEX/MACSima
CITE-seq
SCoPE-MS/SCoPE2;
nanoPOTS;plexDIA
Fig. 1 Overview of single-cell multi-omics technologies. Single-cell multi-omics has expanded beyond transcriptomics (scRNA-seq, snRNA-
seq, scST) to include epigenomics (scATAC-seq), genomics (scDNA-seq), proteomics (CyTOF , CITE-seq, SCoPE-MS, IMC, CODEX/MACSimA), and
metabolomics (scMS). This integrated framework enables comprehensive characterization of gene expression, chromatin accessibility,
genomic alterations, protein distribution, and metabolic dynamics at the single-cell level, thereby providing a powerful platform for dissecting
tumor heterogeneity, tumor –immune interactions, and therapeutic responses.
G.-q. He et al.
124
Oncogene (2026) 45:123 – 139

important discoveries. Okonechnikov et al. showed that large-scale
chromosomal aberrations frequently arise at early stages of
medulloblastoma, acting as initiating events of tumor evolution,
while single oncogenic alterations more often drive later progression
[40]. Van de Velde et al. identi ﬁed a pathogenic CD4 ⁺ T-cell subset
and ARG1⁺ myeloid cells as critical microenvironmental components
sustaining NB development [41].
Taken together, transcriptomic single-cell technologies provide
complementary advantages in resolution, tissue compatibility, and
spatial context. In NB and other complex tumors, they not only
reﬁne cellular lineage mapping and microenvironmental recon-
struction but also lay a foundation for integrative multi-omics
analyses.
Single-cell epigenomic technologies: chromatin accessibility
and fate determination
While transcriptomic pro ﬁling provides a precise snapshot of
cellular expression states, it does not fully capture the upstream
regulatory mechanisms that drive these changes, particularly the
early events underlying cell fate speci ﬁcation and state transitions
[42]. As a result, research has increasingly expanded toward the
epigenomic layer [ 43] and its derivative, single-nucleus ATAC
sequencing (snATACSingle-cell ATAC sequencing (scATAC-seq)-
seq) [ 44], have emerged as powerful tools to interrogate
chromatin accessibility, offering key insights into state reprogram-
ming and fate determination [ 45, 46].
scATAC-seq enables the detection of open chromatin regions, the
identiﬁcation of putative enhancers, promoters, and transcription
factor (TF) binding sites, and the inference of regulatory networks
and TF activity. It has been broadly applied across cancers to map
tumor epigenomes at single-cell resolution. For example, in clear cell
renal cell carcinoma (ccRCC), scATAC-seq revealed chromatin
remodeling features associated with aggressive phenotypes, pin-
pointing key regulatory elements and TF networks driving tumor
progression [ 47]. In triple-negative breast cancer, scATAC-seq
captured therapy-induced TF reprogramming patterns linked to
drug resistance [ 48]. Beyond tumor cells, scATAC-seq also offers
unique advantages in lineage tracing of immune populations. In
myeloid cells such as neutrophils, whose phenotypes are tightly
coupled with differentiation states, accessibility trajectories provide a
powerful framework to resolve developmental pathways and enable
ﬁne-grained subpopulation identiﬁcation and functional character-
ization [49, 50]. Importantly, integrative analysis of scATAC-seq with
scRNA-seq has become a central strategy, allowing prediction of TF
activity, reconstruction of regulatory networks, and multi-layered
dissection from chromatin accessibility to transcriptional output at
the single-cell level [51–53].
Similar to snRNA-seq, snATAC-seq is particularly suited for frozen
or dense tissues and is often combined with snRNA-seq. For
instance, as noted earlier, Konstantin Okonechnikov employed this
approach to distinguish chromosomal events during medulloblas-
toma initiation and progression [ 40]. In ccRCC, Wu and colleagues
used large-cohort snATAC-seq pro ﬁling to demonstrate that BAP1
mutations typically reduce global chromatin accessibility, whereas
PBRM1 mutations enhance chromatin openness, displaying a
mutually exclusive pattern that may represent distinct mechanisms
and transitional stages of disease development [54]. In glioblastoma
(GBM), Wang et al. integrated snATAC-seq with spatial transcrip-
tomics and uncovered higher chromatin accessibility and stronger
immune evasion signatures at the tumor margin, contrasted with
profound immunosuppression in the core [ 55]. They further
identiﬁed several region-speci ﬁc TFs, including RUNX, FOS, and
SPI1, as potential drivers of spatially de ﬁ
ned tumor programs.
Single-cell genomic technologies: genomic instability and
clonal evolution
Beyond chromatin-level alterations, the evolutionary origins of
tumor progression also involve genomic abnormalities such as
mutations and copy number variations (CNVs) [ 56, 57]. Single-cell
DNA sequencing (scDNA-seq) has therefore become a key
approach for delineating clonal evolutionary trajectories, genetic
heterogeneity, and chromosomal instability (CIN). For example,
Wang et al. analyzed hepatocellular carcinoma (HCC) samples with
scDNA-seq and demonstrated a two-phase model of CNV
accumulation characterized by “early catastrophic rearrangements
followed by late progressive evolution [ 58].” Progressive CNV
acquisition was strongly associated with recurrence risk, while
ploidy reconﬁguration events, such as whole-genome duplication,
indicated genetic continuity during clonal evolution and further
exacerbated tumor heterogeneity [ 59–61]. Similarly, Zhou et al.
developed Alleloscope, an algorithm that integrates scDNA-seq
and scATAC-seq data to resolve allele-speci ﬁc CNVs at single-cell
resolution. This method uncovered pervasive allelic imbalance and
copy-neutral loss of heterozygosity (LOH) within subclones and
enabled tracing of their coordinated changes with chromatin
accessibility [ 62].
It is noteworthy that although NB is characterized by marked
genomic instability, such as MYCN ampli ﬁcation, 1p/11q deletions,
and 17q gain [ 63, 64], applications of scDNA-seq in NB remain very
limited. On the one hand, most NB clinical specimens are obtained
from biopsies or frozen tissues, which often preclude the
extraction of high-quality DNA and hinder the technical feasibility
of scDNA-seq [ 65]. On the other hand, compared to adult cancers,
NB tends to harbor relatively simple clonal structures and lower
mutational burdens, reducing the immediate demand for high-
resolution clonal tracing tools [ 6, 66]. In addition, the availability of
extensive bulk WGS and WES datasets in NB provides a partial
substitute for single-cell analyses. Nevertheless, given the
presence of subclonal expansion, chromosomal aberrations
driving tumor progression, and relapse following immunotherapy,
future integration of scDNA-seq with transcriptomic and epige-
nomic modalities to reconstruct clonal evolution in NB remains
highly valuable and holds signi ﬁcant potential [ 67–69].
Single-cell proteomic technologies: functional phenotypes
and communication networks
Compared with transcriptomic and epigenomic approaches,
proteomics provides a direct readout of cellular functional states
and thus represents a critical dimension for understanding tumor
heterogeneity and signaling dynamics. Mass cytometry (CyTOF)
was among the ﬁrst technologies applied to single-cell protein
proﬁling and has been widely used to chart immune landscapes
across diverse cancers. For instance, Baughn et al. analyzed 34
protein markers in 49 multiple myeloma samples and delineated a
protein-level atlas of cellular heterogeneity, identifying subpopu-
lations associated with prognosis and therapeutic response [ 70]. In
HCC, Zhang and colleagues applied CyTOF to peripheral blood
immune cells and uncovered immune signatures relevant to
tumor detection [ 71]. Similarly, Garman et al. used CyTOF to
characterize tumor-in ﬁltrating immune cells in solid tumors,
highlighting its strength in identifying LAG-3 ⁺ T cells [ 72].
Moreover, the integration of CyTOF with conventional ﬂow
cytometry has been leveraged to build predictive scoring systems
for treatment response. In NB, although CyTOF studies remain
limited, exploratory work has demonstrated its potential. Nolo
et al. reported that P-selectin stimulation induces heterogeneous
activation of the PI3K/AKT and MAPK pathways across NB cell
lines, providing mechanistic support for P-selectin inhibition as a
therapeutic strategy [ 73]. Nonetheless, CyTOF is restricted by
antibody dependence, limited proteome coverage, and through-
put constraints, which hinder comprehensive proteomic pro
ﬁling
[74, 75].
Recent advances in single-cell proteomics have sought to
overcome these limitations by developing label-free mass
spectrometry platforms, joint transcriptome –protein assays
and spatially resolved imaging systems. In the label-free ﬁeld,
G.-q. He et al.
125
Oncogene (2026) 45:123 – 139

Single-Cell Proteomics by Mass Spectrometry (SCoPE-MS) and its
upgraded version SCoPE2 have achieved high-throughput quan-
tiﬁcation of single-cell proteomes with the aid of tandem mass tag
(TMT) labeling. Originally developed by Budnik et al. and validated
in human cancer cell lines such as U-937 and Jurkat, SCoPE-MS
demonstrated the ability to discriminate proteomic differences
among cell types and uncover functional heterogeneity during
differentiation [76]. Subsequent re ﬁnements by Slavov ’s group led
to SCoPE2, which markedly improved throughput, accuracy, and
automation, enabling quanti ﬁcation of >1000 proteins across
hundreds to thousands of single cells [ 77]. While the application of
SCoPE2 to primary tumor samples remains challenging, it has
already been successfully employed in models of immune cell
heterogeneity and differentiation. For example, in macrophage
differentiation models, the integration of SCoPE2 with scRNA-seq
uncovered transcription –protein decoupling patterns, underscor-
ing the importance of post-transcriptional regulation during
immune differentiation — an approach readily extendable to
tumor-associated macrophages (TAMs) [ 77]. However, Petelski
et al. also noted remaining technical limitations, including
relatively large sample processing volumes, multiple LC-MS/MS
runs, and ion co-isolation –induced quanti ﬁcation bias. Future
advances in microdroplet processing, barcoding strategies, and
parallel ion accumulation are expected to further improve
performance [ 78].
In this context, nanoPOTS (Nanodroplet Processing in One Pot
for Trace Samples) has emerged as a micro ﬂuidics-based platform
that reduces processing volumes below 200 nL, minimizing
sample loss and enhancing sensitivity for low-abundance proteins.
It has been successfully applied to HeLa cells and circulating
tumor cells (CTCs), and further re ﬁnements have increased
recovery and throughput, enabling quanti ﬁcation of >1500
proteins across different cell lines [ 79]. More recently, plexDIA,
which combines data-independent acquisition (DIA) with isotopic
labeling, allows parallelized sample analysis and signal sharing
across runs, thereby improving data completeness and through-
put. plexDIA can now quantify thousands of proteins in a single
run and has been applied to high-throughput analysis of human
single-cell samples [ 80]. Collectively, these advances provide
strong technological support for mapping proteomic heteroge-
neity in tumors.
In parallel, CITE-seq has emerged as a powerful alternative by
combining antibody-based protein detection with transcriptome
proﬁling, enabling cost-effective multimodal analyses. Unlike
conventional ﬂow cytometry, CITE-seq substantially expands the
number of detectable proteins (>100) while offering greater
quantitative accuracy and reproducibility [ 81, 82]. It has been
widely applied in cancer research to dissect immune hetero-
geneity, reconstruct TME, and predict therapeutic responses. For
example, Leader et al. used CITE-seq in non-small cell lung cancer
to delineate T-cell lineages and functional states and to associate
immune activation modules with tumor antigen load [ 83]. In NB,
CITE-seq applications remain scarce, but the technology holds
strong promise for identifying therapy-related immune subsets
and uncovering immune evasion mechanisms, especially when
integrated with TCR/BCR sequencing and spatial transcriptomics.
Another critical dimension is spatial proteomics, which comple-
ments CyTOF and CITE-seq by preserving spatial context of
protein expression within tissues. Imaging Mass Cytometry (IMC),
combining CyTOF with laser scanning microscopy, has been used
to build spatial immune atlases and prognostic models. For
example, Elaldi et al. pro ﬁled 35 immune-related markers in breast
cancer tissues, demonstrating spatial exclusion of immune cells by
tumor density [ 84]. Xiao et al. applied IMC to melanoma,
identifying spatial co-localization patterns among T cells, macro-
phages, and tumor cells, and linking distinct microenvironmental
architectures to clinical outcomes [ 85]. Similarly, CODEX (CO-
Detection by Indexing), a multiplexed antibody-based imaging
system, enables 50+ protein markers to be visualized in three
dimensions [ 86]. Goltsev et al. demonstrated the feasibility of
CODEX for high-dimensional proteomic imaging of spleen and
tumor tissues [ 87].
To date, applications of IMC and CODEX in NB remain scarce,
likely due to challenges in pediatric tumor tissue acquisition and
immature antibody validation frameworks. Nonetheless, given the
pronounced immune microenvironment heterogeneity and spa-
tial tissue organization of NB, integrating spatial proteomics
platforms into NB research could elucidate immune exclusion
zones, tumor –stroma interfaces, and spatial biomarkers of
therapeutic response, ultimately informing precision immunother-
apy strategies.
Single-cell metabolomic technologies: metabolic
reprogramming within the tumor ecosystem
Compared with transcriptomic, epigenomic, and proteomic
approaches, metabolomics provides the most direct snapshot of
biochemical activity, serving as a crucial window into tumor
metabolic reprogramming and microenvironmental adaptation.
However, the vast diversity of metabolites, their short half-lives,
and rapid ﬂuctuations in abundance pose major challenges for
generating high-quality data at single-cell resolution [ 88, 89]. In
recent years, mass spectrometry –based single-cell metabolomics
(scMS) has overcome many of these technical bottlenecks in
sensitivity and resolution, emerging as a powerful tool to dissect
metabolic heterogeneity. Typically employing high-resolution
platforms such as Orbitrap or TOF-MS combined with microsam-
pling, scMS enables both targeted and untargeted detection of
key pathways, at the single-cell or microscale tissue level [ 89]. This
approach has now been broadly applied to both solid and
hematological malignancies [ 90, 91].
Although large-scale applications of scMS in NB remain limited,
the known presence of MYCN-driven metabolic reprogramming
and divergent oxidative phosphorylation versus glycolytic states
among NB subpopulations suggests that coupling scMS with
spatial or proteomic modalities holds strong promise [ 92–94].
Such integrated approaches may uncover metabolic vulnerabil-
ities and guide the development of precision therapeutic
strategies for NB.
Single-cell decoding of neuroblastoma: from developmental
arrest to ADR/MES plasticity
To provide a more intuitive overv iew, the developmental origins
and state plasticity of NB can b e conceptualized as a continuum
from neural crest cell (NCC) arrest to dynamic transitions
between adrenergic (ADR) and mesenchymal (MES) phenotypes
(Fig. 2). This chapter highlights the lineage complexity and state
interconversion that underpin tumor heterogeneity, while
directly linking ADR/MES plasticity to therapy sensitivity and
resistance.
Developmental origins and trajectory heterogeneity in NB
Accumulating developmental evidence indicates that NB arises
from arrested differentiation of NCCs within the
sympatho–adrenal lineage [ 95, 96]. This framework accounts for
several biological features of NB, including phenotypic diversity,
mutational pro ﬁles, spontaneous regression, and sensitivity to
differentiation-inducing agents. NB was ﬁrst recognized as a
distinct tumor in the mid-19th century, and by 1910 was classi ﬁed
as neuronal in origin based on ﬁber-like structures resembling
sympathetic ganglion neurons [ 97]. Its capacity to differentiate
into mature neurons was noted early on, and the prevailing
consensus now holds that NB complexity re ﬂects the diverse and
dynamic trajectories of neural crest –derived lineages [ 6]. Jansky
et al. demonstrated that NB closely resembles developing NCC
progenitors, with clinical phenotypes mapping to distinct stages
of normal neural crest differentiation [ 98].
G.-q. He et al.
126
Oncogene (2026) 45:123 – 139

NCCs are proliferative, multipotent progenitors whose fates are
determined by both axial position and non –cell-autonomous cues
[99, 100]. For example, cranial NCCs generate bone and cartilage,
while sacral NCCs form enteric neurons. Cross-regional transplan-
tation experiments further show their plasticity: trunk NCCs
transplanted to the cranial region can produce bone/cartilage,
whereas cranial NCCs placed in the trunk region generate the full
sympatho–adrenal lineage, including sympathetic neurons, chro-
mafﬁn cells, Schwann cells, and melanocytes [ 96]. Thus, migratory
pathways and microenvironmental cues are tightly coupled to
lineage choice. Trunk-derived sympathoblasts possess dual
potential, giving rise to both neurons and mesenchymal-like cells.
A critical question therefore arises although sympathetic neurons
and chromaf ﬁn cells normally differentiate along mutually
exclusive lineages, this segregation may not hold in NB. Indeed,
NB cells can simultaneously exhibit sympathetic neuronal and
chromafﬁn/mesenchymal features, suggesting “rewiring” of their
developmental trajectories [ 101]. Two complementary explana-
tions have been proposed: (i) intrinsic dysregulation of develop-
mental programs that reactivates NCC multipotency and drives
aberrant (trans)differentiation; and (ii) extrinsic signals from the
tumor microenvironment, such as Schwann cell – or stroma-
derived cues, which promote fate switching linked to aggressive-
ness and therapy resistance [ 102]. Together, these mechanisms
TRUNK
Neurofilament protein
SOX10
PLP1
STMN2
ISL1
HAND2
TH
CHGA
PNMT
Early Late
Vimentin protein
ADRN CRC
gene loss
SE 
rerodeling
ADR MES
ResistanceSensitivity
Gene events: ARID1A-/-, PRRX1
NOTCH3 activation
PHOX2B
ASCL1
TH
DBH
NOTCH
VIM
FN1
PRRX1Mixed state
Fig. 2 Developmental origins and state plasticity of NB. NB arises from developmental arrest of NCCs within the sympatho –adrenal lineage,
leading to tumor cells trapped at intermediate differentiation states. NCC-derived progenitors such as sympathoblasts and Schwann cell
precursors (SCPs) exhibit dual potential, giving rise to adrenergic (ADR) and mesenchymal (MES) lineages. ADR cells express neuro ﬁlament
proteins and catecholamine biosynthesis markers (TH, CHGA, PNMT) and are associated with early developmental trajectories and
chemotherapy sensitivity. In contrast, MES cells express vimentin and stromal markers (SOX10, PLP1), correspond to late developmental states,
and confer therapy resistance. Single-cell multi-omic analyses have revealed that ADR and MES states are stabilized by distinct core regulatory
circuits (CRCs) and super-enhancers (SEs) yet remain interconvertible. Key genetic and epigenetic events, including ARID1A loss, PRRX1
upregulation, and NOTCH3 activation, promote ADR → MES transitions via enhancer remodeling, resulting in therapy-induced MES
enrichment. Conversely, a fraction of MES cells can revert to ADR upon microenvironmental changes, rebuilding tumor heterogeneity.
Transitional and hybrid states coexist within tumors, highlighting dynamic fate plasticity and the continuum from developmental arrest to
ADR/MES interconversion as determinants of NB progression, therapy sensitivity, and relapse.
G.-q. He et al.
127
Oncogene (2026) 45:123 – 139

underscore the pivotal role of the microenvironment in fate
plasticity within NB.
Single-cell studies have provided direct lineage evidence.
Schwann cell precursors (SCPs) have been identi ﬁed as the
predominant progenitors of both adrenal chromaf ﬁn cells and
sympathoblasts [98, 103–105], and also contribute to parasympa-
thetic ganglia formation [ 106]. NB tumor transcriptomes resemble
noradrenergic chromaf ﬁn cells, with malignant states typically
arrested at intermediate stages of sympatho –adrenal differentia-
tion [107]. Although both SCP-derived and NCC-derived pathways
exist, the resulting sympathoblast phenotypes are highly similar,
contributing to intertumoral complexity. NCC-derived cells traverse
multiple transcriptionally distinct states, progressing from undiffer-
entiated progenitors to fully differentiated, fate-committed cell
types [ 101, 104]. Projecting NB cells onto this continuum reveals
that the degree of progression from SCP to differentiated
noradrenergic cells strongly correlates with clinical outcome:
high-risk NB often retains immature sympathoblast features,
whereas low-risk NB is enriched for more differentiated states
[98, 107].
Further intratumoral evidence indicates that developmental
heterogeneity is recapitulated within tumors. Kameneva et al.
described a “fork-like” transitional state in which single cells co-
express key markers of both SCPs and chromaf ﬁn/sympathoblast
lineages [ 105]. Multi-omic single-cell pro ﬁling of human NB
samples further identi ﬁed aneuploid SCP-like subclones with
unique transcriptional signatures and clonal expansion, integrat-
ing precursor-like and transitional states into NB progression [ 108].
These ﬁndings align with large-scale genomic studies showing
parallel clonal evolution between primary and metastatic lesions,
with therapy-resistant clones driving relapse [ 68, 109, 110].
However, genomic data alone cannot resolve the phenotypes of
post-therapy persister cells. Integrated sc/snRNA-seq approaches
have begun to characterize their transcriptional states and roles in
clonal selection and relapse [ 67]. Collectively, these observations
highlight the temporal and spatial continuity between develop-
mental arrest, lineage plasticity, and tumor reconstruction,
reinforcing the tight coupling of NB clinical progression to its
developmental and lineage context, a theme further elaborated in
subsequent sections.
Tumor heterogeneity and cellular plasticity in NB
Building on its developmental origins, NB manifests at the tumor
level as heterogeneity and plasticity of differentiation outcomes.
Since the 1980s, when primary cultures and cell lines were ﬁrst
established, NB heterogeneity has been consistently observed.
Early in vitro studies broadly classi ﬁed tumor cells into neuron-like
(N-type) and substrate-adherent (S-type) categories [ 111–114].
N-type cells express neuro ﬁlament proteins and catecholamine
biosynthesis markers (e.g., TH, CHGA, PNMT) and exhibit neuronal
differentiation potential, whereas S-type cells are enriched for
vimentin and stromal markers (e.g., SOX10, PLP1), resembling non-
neuronal neural crest derivatives [
100, 115]. However, this binary
framework cannot explain three critical aspects: the long-term
coexistence and therapy-induced reshaping of subpopulations,
the reversible interconversion and existence of intermediate
states, and the regulatory drivers and causal mechanisms under-
lying these dynamics.
With the advent of single-cell transcriptomic, chromatin
accessibility, and epigenomic pro ﬁling, NB “types” are now better
deﬁned as plastic states maintained by core regulatory circuits
(CRCs) and super-enhancers (SEs) [ 116, 117]. Multi-omic integra-
tion has revealed two antagonistic but interconvertible networks:
ADR (also termed ADRN) and MES [ 101, 118]. Mirroring the early
N/S paradigm, ADR and MES states are also reversible: van
Groningen et al. demonstrated bidirectional spontaneous switch-
ing in cell lines [ 119], while Durbin et al. used longitudinal cultures
with sn/scRNA-seq to quantify transition rates, showing that ADR
→ MES transitions are generally faster than MES → ADR [ 101].
Clinical and in vivo data support functional associations: ADR
correlates with chemotherapy sensitivity, whereas MES is linked to
tolerance and resistance [ 116]. Under cytotoxic pressure, ADR cells
are preferentially eliminated, while low-proliferative/quiescent
MES cells are retained, leading to post-treatment MES enrichment
and phenotypic shift [ 120]. Upon drug withdrawal or microenvir-
onmental change, a fraction of MES cells can revert to ADR,
rebuilding heterogeneity and driving relapse [ 102, 118].
Mechanistically, ADR maintenance requires intact CRC/SE
architecture [ 117]. Its disruption increases the probability of MES
conversion, whereas stabilization or reinforcement of ADR-SE
peaks helps sustain the ADR state [ 101]. Two representative
studies provide causal nodes with sequencing evidence: van
Groningen et al. mapped the SE landscape of NB using H3K27ac
ChIP-seq with RNA-seq, showing that PRRX1 upregulation
reprograms enhancers and transcriptional pro ﬁles to drive ADR
→ MES, with MES preferentially enriched in post-treatment/
relapsed tumors [ 116]. Shi et al. reported that ARID1A (SWI/SNF)
loss promotes ADR → MES conversion and enhances platinum
resistance in ADR cells, supported by RNA-seq and multi-target
ChIP-seq evidence pointing to enhancer-mediated transcriptional
reprogramming [ 121]. Furthermore, van Groningen ’s group
proposed a NOTCH3 feed-forward module as a key switch for
CRC interconversion, where NOTCH3 activation triggers genome-
wide SE remodeling, downregulates ADR-CRC members, and
upregulates MES networks; inhibition of this axis partially blocks
the transition [ 119]. Notably, there is currently no single
transcription factor proven to induce stable MES → ADR
conversion, suggesting that reverse stabilization likely requires
multilayered regulation rather than a single TF.
Importantly, owing to the complexity of intrinsic genetic
regulation and extrinsic environmental cues, recent studies have
captured intermediate states, ADRN/MES subtypes, or novel
hybrid programs, linking them to NB plasticity. For instance,
Thirant et al. identi ﬁed a subset of adrenergic cells with
mesenchymal features using 10x scRNA-seq, validated in vitro
[122]. Chapple et al. applied an acNMF algorithm to scRNA-seq
maps, showing that
“weak mesenchymal-like ” programs fre-
quently coexist within ADR-dominant cells and can be induced
in vivo within 24 h of chemotherapy, indicating that therapy-
related hybrid populations constitute early escape mechanisms
[123]. Large-scale atlas efforts, such as the NBAtlas and integrative
spatial/multi-omic maps, have further con ﬁrmed co-expression
and neighborhood-speci ﬁc distribution of states in patient
samples, providing tissue-level evidence for hybrid subpopula-
tions [ 124].
In summary, single-cell omics have reframed NB from a binary
classiﬁcation into a developmental continuum of plastic states.
They enable dissection of ADR, MES, and transitional subpopula-
tions at single-cell resolution, anchoring them to CRC/SE
regulatory levers such as NOTCH3, PRRX1, and ARID1A. This shift
transforms our understanding from observing heterogeneity to
uncovering actionable mechanisms, offering conceptual footholds
for therapeutic intervention in clinical NB.
CELLULAR MECHANISMS OF NEUROBLASTOMA: FROM
GENETIC PREDISPOSITION TO THE METASTATIC
MICROENVIRONMENT
Developmental arrest and ADR/MES plasticity not only shape the
molecular and cellular landscape of NB but also provide a
conceptual framework for understanding its biological complexity.
However, how these molecular and developmental alterations
translate into the clinical heterogeneity and symptoms observed
in patients requires further elucidation at the level of cellular
regulatory mechanisms. Such insights are essential to clarify the core
dynamics of tumorigenesis and progression, while also identifying
G.-q. He et al.
128
Oncogene (2026) 45:123 – 139

potential entry points for targeted therapies, immunotherapies, and
interventions in TME. In this regard, single-cell omics technologies
have recently demonstrated unique advantages.
From the perspective of genetic predisposition, familial NB (FNB)
represents a rare subtype whose de ﬁning mechanisms have been
elucidated by single-cell studies. Using scRNA-seq, Zhang et al.
mapped the cellular atlas of FNB and revealed marked differences
from sporadic NB, FNB was characterized by a reduced proportion
of neuroendocrine cells and an increased proportion of immune
cells, with the identi ﬁcation of a cancer-associated ﬁbroblast (CAF)
subtype, Fib-4, with prognostic relevance [ 125]. In the context of
risk strati ﬁcation, Bedoya-Reina et al. employed snRNA-seq to
construct a reference atlas of postnatal human adrenal cells and
compared it to NB. Their analysis showed that low-risk NB
resembled sympathetic neurons and chromaf ﬁn cells, whereas
high-risk NB was enriched for TRKB ⁺ cholinergic progenitors. This
highlighted the link between aberrant developmental lineages and
NB risk and underscored the potential of single-cell omics for risk
prediction [ 126]. Mechanistically, George et al. summarized the
molecular hallmarks of high-risk NB, including MYCN ampli ﬁcation,
chromosomal instability, and activation of telomere maintenance
mechanisms, and proposed novel therapeutic strategies targeting
telomere biology [ 127]. Integrating these with single-cell multi-
omics approaches may provide a more re ﬁned understanding of
oncogenic drivers and actionable vulnerabilities. Moreover, Dong
et al. analyzed relapsed NB by scRNA-seq and demonstrated that
residual tumor cells acquire drug-resistant transcriptional states
that interact with an immunosuppressive microenvironment,
emphasizing the utility of single-cell pro ﬁling in capturing resistant
populations during tumor evolution [ 107].
Metastasis represents the ultimate stage of cancer evolution,
accounting for the majority of NB-related mortality and frequently
accompanied by treatment resistance. Importantly, the altered
bone marrow (BM) microenvironment in which disseminated NB
cells reside can reshape their transcriptional programs and
thereby promote resistance. Recent advances in scRNA-seq have
enabled high-resolution pro ﬁling of the NB BM niche, which is
particularly relevant given the strong predilection of NB for BM
metastasis. Mei et al. revealed enrichment of tumor-associated
neutrophils, macrophages, and exhausted T cells in metastatic BM,
alongside an increase in regulatory T cells and a decrease in B cells
and identi ﬁed malignant-cell markers associated with poor
prognosis [ 128]. Similarly, Fetahu et al. combined single-cell
transcriptomics with epigenomic pro ﬁling to uncover the central
role of monocytes in BM metastasis, highlighting their dual
functions in promoting in ﬂammation and mediating immunosup-
pression [129]. Complementarily, Kildisiute et al. [ 130] constructed
a large-scale single-cell atlas and demonstrated that noradrener-
gic tumor cells maintain a stable phenotype in BM metastases, yet
their interaction networks with immune cells undergo profound
rewiring, implicating the metastatic microenvironment as a critical
determinant of resistance and progression.
Collectively, these ﬁndings establish that NB metastasis is not
merely a passive process of cellular dissemination but is intimately
coupled with extensive remodeling of the immune microenviron-
ment, predominantly orchestrated by myeloid lineages. This
paradigm provides fresh perspectives on the molecular and
cellular dynamics underlying metastasis, reinforces the impor-
tance of dissecting the NB TME, and lays the conceptual
groundwork for developing therapies that target tumor to
microenvironment interactions.
THE TUMOR MICROENVIRONMENT OF NEUROBLASTOMA:
CELLULAR COMPOSITION AND FUNCTIONAL HETEROGENEITY
Single-cell atlas of the neuroblastoma microenvironment
Over the past decade, the rapid advancement of single-cell
technologies has profoundly enhanced our understanding of the
complex ecosystems of solid tumors. A series of landmark studies
have demonstrated that constructing high-resolution single-cell
atlases not only reveals intratumoral heterogeneity but also
elucidates the key mechanisms governing tumor evolution and
microenvironmental interactions. For instance, in glioblastoma,
Neftel et al. [ 131] proposed four dynamically interchangeable
cellular states, highlighting the coupling between tumor cell
plasticity and microenvironmental cues. In melanoma, Tirosh et al.
[132] delineated multidimensional interaction networks among
malignant, immune, and stromal cells, thereby uncovering the
ecological basis of immune evasion. In breast cancer, Azizi et al.
[133] and Wagner et al. [ 134] systematically mapped the
functional continuum of tumor-in ﬁltrating immune cells, linking
immune gradients to therapeutic responsiveness. In pancreatic
ductal adenocarcinoma, Elyada et al. [ 135] identi ﬁed distinct
subsets of CAFs with immunomodulatory functions, emphasizing
the central role of stromal cells in immune exclusion. Similarly, Ma
et al. [ 136] integrated single-cell transcriptomic data from
hepatocellular carcinoma to show that lineage diversity within
tumor cells drives microenvironmental remodeling and differential
responses to immunotherapy. Collectively, these studies have
deﬁned the current paradigm of single-cell atlas research in solid
tumors, from dissecting cellular composition and state plasticity to
stratifying immune and stromal function and linking atlas-derived
features to clinical outcomes and offering a multidimensional
framework for decoding tumor biology.
TME consists of both cellular and non-cellular components that
collectively orchestrate tumor initiation, progression, invasion,
metastasis, and therapeutic resistance [ 137–139]. Neuroblastoma
is composed of diverse cell types, including malignant neuro-
blasts, stromal cells, endothelial cells, CAFs, and various immune
cell populations residing within the tumor microenvironment
[112, 140]. The NBAtlas, which integrates single-cell transcriptomic
proﬁles from 61 patients across seven independent studies,
provides a uni ﬁed reference for de ﬁning the cellular composition
of NB. It highlights the extensive intratumoral heterogeneity and
immune complexity of the disease and establishes correlations
between transcriptional programs and clinical outcomes, serving
as an invaluable benchmark for annotating new single-cell
datasets [124]. Beyond compositional mapping, single-cell studies
targeting distinct biological contexts have expanded the func-
tional dimension of the NB atlas. Bedoya-Reina et al. [ 126]
compared single-nucleus transcriptomes of human postnatal
adrenal glands with NB samples, revealing that low-risk tumors
share transcriptional similarities with sympathetic neurons and
chromafﬁn cells, whereas high-risk tumors are enriched for TRKB ⁺
cholinergic progenitor-like populations, linking aberrant develop-
mental trajectories to clinical risk phenotypes. Moreover, in studies
focusing on the metastatic bone marrow niche, Mei et al. [ 128]
and Fetahu et al. [ 129] identi ﬁed a coordinated immunosuppres-
sive network involving tumor-associated neutrophils (TANs) and
the monocyte –macrophage axis as a key driver of NB metastasis.
Mei et al. showed that metastatic lesions are enriched in TANs and
monocyte–macrophage populations. TANs highly express CXCL8
and S100A8/A9, activating the CXCR2 –MAPK/NF-κB pathway to
induce immune exhaustion and upregulate ARG1 and PD-L1,
reinforcing suppression. Concurrently, monocyte –macrophage
cells secrete SPP1, MIF, and CCL2, which signal through
MIF–CD74/CD44 and SPP1 –ITGAV axes to promote M2 polariza-
tion, T-cell inhibition, and ECM remodeling, forming an immune-
excluded “myeloid barrier. ” Complementarily, Fetahu et al. identi-
ﬁed SPP1 ⁺ macrophages and CD163 ⁺/IL-10⁺ monocytes that drive
immune evasion and angiogenesis via TGF- β, VEGF, and IL-10
pathways, and regulate ECM organization through the
SPP1–ITGB1–STAT3 axis. Together, these ﬁndings position the
TAN–macrophage interaction network as a central mediator
linking immune suppression and stromal remodeling in
metastatic NB.
G.-q. He et al.
129
Oncogene (2026) 45:123 – 139

The immunosuppressive microenvironment promotes tumor
immune evasion
As illustrated in Fig. 3, recent studies based on NB patient samples
and murine models have progressively revealed the complex
immune architecture of the TME, emphasizing the remarkable
functional heterogeneity among immune cell populations [ 140]. In
addition to myeloid-derived suppressor cells (MDSCs), the NB TME
is enriched with multiple immunosuppressive components,
including TANs, regulatory T cells (Tregs), dysfunctional natural
killer (NK) cells, and TAMs [ 128, 140]. Among them, macrophages
display high plasticity and can dynamically switch between pro-
inﬂammatory M1 (CD68⁺, IL-1β⁺, TNF-α⁺) and anti-inﬂammatory M2
(CD163⁺, CD206 ⁺, IL-10 ⁺) phenotypes. While M1 macrophages
primarily mediate in ﬂammation and immune activation, M2
macrophages are involved in tissue remodeling and immunosup-
pression. Although high TAM in ﬁltration generally predicts poor
prognosis, certain pro-in ﬂammatory myeloid subsets have been
correlated with favorable outcomes, suggesting that macrophages
may exert context-dependent dual functions [ 141, 142].
Recent single-cell and multi-omics studies have further re ﬁned
this immunosuppressive landscape. Yu et al. [ 143], through
longitudinal single-cell multi-omics pro ﬁling of high-risk NB,
identiﬁed TAMs as the dominant immune population within the
TME. Their abundance markedly increased after therapy and
exhibited pronounced subtype heterogeneity, with subsets
enriched in immunosuppressive axes such as MIF –CD74/CD44/
Fig. 3 The immunosuppressive tumor microenvironment of neuroblastoma. Single-cell and spatial multi-omics analyses have revealed a
complex immunosuppressive network in the NB TME. Tumor-associated macrophages (TAMs) and neutrophils act as central mediators of
immune evasion and stromal remodeling. MIF ⁺ TAMs interact with tumor and stromal cells through MIF –CD74/CD44/CXCR4 signaling, while
SPP1⁺ TAMs promote angiogenesis and extracellular matrix (ECM) reorganization via SPP1 –ITGB1–STAT3 and VEGF pathways. Neutrophils
secrete CXCL8 and S100A8/A9, activating the CXCR2 –MAPK/NF-κB axis to induce immune exhaustion and PD-L1 upregulation. Cancer-
associated ﬁbroblasts (CAFs) further reinforce immune exclusion by releasing TGF- β, CXCL12, COL1A1, and FN1, forming a collagen-rich
physical barrier that limits effector T-cell in ﬁltration. Endothelial –immune crosstalk, exempli ﬁed by LGALS9 –HAVCR2 (TIM-3) interactions,
contributes to vascular immune suppression. In parallel, monocytes and MDSCs support macrophage recruitment and differentiation through
MIF–CD74/CD44 and SPP1 –ITGAV signaling. Collectively, these coordinated cellular and molecular interactions establish a highly suppressive
microenvironment that promotes immune escape, angiogenesis, and tumor progression in high-risk and relapsed NB.
G.-q. He et al.
130
Oncogene (2026) 45:123 – 139

CXCR4 and NECTIN2 –TIGIT. Wienke et al. [ 142] analyzed 24 NB
tumors (pre- and post-chemotherapy) using scRNA-seq and
revealed therapy-induced immune remodeling characterized by
the upregulation of suppressive pathways in both myeloid
and T-cell compartments. Giudice et al. [ 144], using a GPC2 CAR-
T therapy model, demonstrated that treatment-driven TME
reprogramming reshaped immune cell composition and effector
states, highlighting the plasticity of immunosuppressive circuits.
Strijker et al. [ 145] further showed that pharmacological inhibition
of M2-derived MIF enhanced CAR-T ef ﬁcacy, providing experi-
mental evidence for targeting TAM-associated druggable path-
ways. In spatial multi-omics analyses, Yu et al. [ 145] and Wienke
et al. [ 142] consistently reported upregulation of SPP1 ⁺ TAMs
and the MIF –CD74/CD44 axis in high-risk and relapsed NB,
which were closely associated with T-cell exhaustion phenotypes.
Spatial transcriptomics also revealed enriched LGALS9 –HAVCR2
(TIM-3) interactions between endothelial and NK/T cells
within immune-excluded regions, underscoring the importance
of vascular –immune crosstalk in maintaining suppression [ 146].
Additionally, Liu et al. [ 147] demonstrated in gastric cancer that
activation of the MIF –CD74 pathway drives macrophage repro-
gramming toward an immunosuppressive phenotype — a mechan-
ism also observed in NB TAMs — indicating a conserved axis across
solid tumors. Batchu et al. [ 148] con ﬁrmed this in a pan-cancer
integrated analysis, showing broad upregulation of MIF –CD74/
CD44 signaling associated with macrophage recruitment and
immune evasion, providing a comparative framework for NB
myeloid regulation.
Beyond the myeloid compartment, other immune cell types —
such as eosinophils, mast cells, and monocytes — can be recruited
to tumor sites through cytokines including IL-1, IFN- γ, and TNF- α,
thereby sustaining chronic in ﬂammation and facilitating metas-
tasis [ 149–151]. Meanwhile, a subset of cancer-associated
ﬁbroblasts (CAFs) within the NB microenvironment exhibits
immunosuppressive features [ 140]. Integrative single-cell and bulk
transcriptomic analyses [ 152] established a CAF-related prognostic
model, linking TGFB1 and CXCL12 secretion to distinct immune
inﬁltration patterns. Two CAF subtypes were de ﬁned: one
expressing TGF- β, CXCL12, COL1A1, and FN1, forming an
immune-excluded “collagen barrier,
” and another ACTA2 ⁺ myoﬁ-
broblastic subtype associated with ECM cross-linking and tissue
stiffening.
Single-cell and spatial studies in other solid tumors have also
revealed conserved mechanisms of CAF-mediated immune
exclusion. Elyada et al. [ 135] identi ﬁed MHC II ⁺ antigen-
presenting CAFs (apCAFs) in pancreatic ductal adenocarcinoma
that engage TAMs through TGF- β and CCL2 signaling feedback
loops. Peng et al. [ 153] found in colorectal cancer that
inﬂammatory CAFs (iCAFs) negatively correlate with NK and
monocyte in ﬁltration, suggesting cytokine-driven immune exclu-
sion zones. Zhang et al. [ 154] reported spatial co-localization of
FAP⁺ CAFs and SPP1 ⁺ macrophages, mediated by ECM-related
ligand–receptor networks that regulate immune tone. Jain et al.
[155] further con ﬁrmed, through single-cell and spatial transcrip-
tomics of glioblastoma, the presence of CAF-like ﬁbroblasts— an
unexpected ﬁnding in a neural malignancy traditionally consid-
ered ﬁbroblast-poor. These CAF-like cells localized near endothe-
lial and M2 macrophage clusters, jointly promoting local
immunosuppression and stromal stiffening.
MECHANISMS OF THERAPEUTIC RESISTANCE IN
NEUROBLASTOMA: CELLULAR LINEAGE EVOLUTION AND
ADAPTIVE PLASTICITY
Despite the substantial improvement in overall outcomes
achieved through multimodal therapies, therapeutic resistance
remains the major obstacle to long-term survival in patients with
high-risk and relapsed NB. Recent single-cell and spatial multi-
omics studies have delineated the dynamic trajectory of resistance
evolution. At diagnosis, NB tumors are predominantly composed
of highly proliferative ADR cells, with limited immune in ﬁltration.
Following induction chemotherapy, the cellular composition
undergoes profound remodeling, characterized by an increased
proportion of mesenchymal-like and persister-like tumor sub-
populations, accompanied by the gradual enrichment of myeloid
cells, particularly SPP1 ⁺ macrophages and neutrophils, within the
immune microenvironment. In relapse and metastatic stages,
tumor cells display markedly elevated heterogeneity and plasti-
city, coinciding with the expansion of tumor-associated neutro-
phils, immunosuppressive macrophages, and ﬁbroblasts in the
bone marrow niche, while effector T and NK cells are progressively
depleted [ 128, 129, 143]. This temporal shift in cellular composi-
tion, from a “tumor-dominant” to an “immunosuppressive and
stromal-reprogrammed” ecosystem, highlights the ecological
remodeling of NB under therapeutic pressure and provides a
spatiotemporal framework for understanding treatment failure
and relapse (as illustrated in Fig. 4).
Genetic and structural remodeling
Single-cell DNA and RNA sequencing have revealed marked
structural and clonal dynamics accompanying the development of
NB resistance. Avitabile et al. performed single-cell RNA analysis of
etoposide- and cisplatin-resistant NB cell lines and identi ﬁed
transcriptional clusters clearly segregated from parental cells,
enriched in pathways related to DNA repair, nucleosome
organization, and chromatin maintenance, suggesting that
genomic remodeling contributes to the establishment of drug
resistance [ 156]. Another integrative DNA/RNA sequencing study
of NB cell lines and patient samples demonstrated that hetero-
geneity in extrachromosomal DNA (ecDNA) copy number drives
MYCN expression variability and cell-state transitions, indicating
that ecDNA-mediated genomic plasticity underlies adaptive
phenotypic switching [ 157].
Epigenetic and Core Regulatory Circuit Remodeling
Epigenetic plasticity is one of the core mechanisms underlying the
formation and maintenance of drug resistance. Integrative analysis
shows that neuroblastoma undergoes extensive remodeling of
super-enhancers and CRCs during treatment, characterized by the
activation of stress-related transcriptional axes (PRRX1/NOTCH)
and the suppression of neural-lineage factors (ASCL1/PHOX2B)
[158, 159]. This state transition, formerly referred to as the
adrenergic–mesenchymal transition (AMT), actually lies within a
broader epigenetic continuum involving multiple reversible
developmental states. Pharmacological studies have shown that
targeting epigenetic regulators (such as BET, HDAC, or EP300) can
partially restore epigenetic balance, thereby reinducing the
sensitivity of resistant cells to therapy. Meanwhile, resistance
stratiﬁcation analysis has revealed a speci ﬁc pattern of rapid
attenuation in transcription factor regulatory activity (such as
BAZ1A, HCFC1, MAZ, and ZNF146), and their silencing signi ﬁcantly
inhibits the proliferation of NB cells in vitro, suggesting that this
pathway participates in the stabilization of epigenetic mainte-
nance and drug insensitivity [ 160]. At the single-cell level, the
imbalance of demethylation and chromatin assembly –related axes
accompanies the occurrence of AMT, further supporting the
critical role of the reversible “super-enhancer–CRC–cell fate ” loop
in drug resistance [ 156, 160].
Target loss and bypass activation
Integrated single-cell multi-omics analyses indicate that therapeu-
tic resistance in NB often arises from signal network rewiring
rather than the inactivation of a single pathway. Studies have
revealed that, under ALK inhibition or chemotherapy pressure, a
subset of NB cells can restore downstream cascades through
bypass receptor –ligand axes, thereby maintaining MAPK and
G.-q. He et al.
131
Oncogene (2026) 45:123 – 139

PI3K–AKT signaling and sustaining cell survival. A representative
example is that TAMs secrete HB-EGF, which in turn activates
ERBB4 signaling in tumor cells through paracrine interaction,
triggering ERK pathway activation and proliferation. Functional
validation demonstrated that both an HB-EGF neutralizing agent
(CRM197) and pan-ERBB inhibitors (e.g., afatinib) markedly
suppressed NB cell growth, indicating that the HB-EGF –ERBB4
axis acts as a key bypass route mobilized under therapeutic stress
[143].
In etoposide/cisplatin-resistant models, scRNA-seq pro ﬁling
further revealed that resistant clusters form transcriptionally
distinct subpopulations from their parental cells, with signi ﬁcant
enrichment of pathways related to DNA repair (such as the
BARD1/BRCA1/PARP1 axis) and drug target modi ﬁcation. These
alterations are accompanied by cell identity reprogramming and
concurrent signaling rewiring, supporting a model of plastic
resistance driven by functional redundancy [ 156].
In the context of ALK-targeted therapy, secondary ALK
mutations often coexist with downstream signal rerouting.
System-level genomic studies have revealed that ALK pathway
mutations not only confer inhibitor resistance but also expose
collateral vulnerabilities, providing rationale for multi-target
combination strategies or function-centric pathway blockade
approaches [ 161].
At the spatial level, integrated analyses combining imaging
mass cytometry (IMC) with single-cell and spatial transcriptomics
have shown that bypass activation frequently coincides with
stromal remodeling and immune exclusion. In NB bone marrow
metastatic niches, myeloid cells, particularly SPP1 ⁺ macrophages
and neutrophils — are enriched alongside upregulation of immu-
nosuppressive signaling axes and chromatin accessibility repro-
gramming, establishing a ligand-rich and receptor-rich
microenvironmental scaffold that facilitates bypass signaling [ 129].
Persister and memory-like cell programs
Drug resistance in NB is not merely the result of clonal selection
but also arises from a dynamic equilibrium of cell states. Single-cell
lineage tracing and RNA velocity analyses have shown that a
subset of cells can reduce RNA dynamics and transcriptional noise,
thereby entering a low-metabolic and low-proliferative persister
state [ 162]. Computational modeling and single-cell imaging
further suggest that, even after chemotherapy, gene expression
noise persists, which can drive the emergence of resistant
phenotypes within a clone without relying on rare gene
expression states. Among these, defective JNK signaling is closely
associated with persistence and regrowth, and JNK-de ﬁcient
subpopulations can be detected even in untreated cells, exhibit-
ing a form of “resistance memory ” [162]. Restoring JNK activity or
lowering the apoptotic threshold has been shown to signi ﬁcantly
increase drug sensitivity, offering a promising therapeutic
approach to eliminate latent residual cell populations.
Across resistant models and longitudinal clinical samples, a set
of recurrent “survival-type epigenetic programs ” has emerged,
characterized by decreased cell cycle scores, markedly reduced or
stagnant RNA velocity, and globally diminished chromatin
accessibility. A subset of surviving cells, after exposure to
Diagnosis
ADR PHOX2B
ASCL1
GATA3
MES
VIM
PRRX1
NFKBIA
RELB
Chemotherapy Remission Relapse
ADR
Genetic/Structural Drivers
Epigenetic & CRC
Remodeling
Target Loss & Bypass Activation
WGS/scDNA/scRNA
snATAC/snRNA
Multi-RNA  snATAC  IMC   CODEX
Persisters / Memory
Immune/Inflammatory
Vulnerability
Metabolic & RA Tolerance
JNK-KTR  sc/snRNA
scRNA  CITE  IMC   CODEX
scMS
MES
Persisters
Persisters
Persisters
MES
NOTCH3
HES1
MES
MES
ADR
ADR
ADR
1
2
3 4
5
6
Fig. 4 Cellular lineage evolution and multi-omic mechanisms of therapeutic resistance in neuroblastoma. Schematic representation of NB
cell-state transitions and resistance mechanisms under therapeutic pressure. During disease progression from diagnosis to relapse, ADR tumor
cells progressively convert to MES and persister-like states, accompanied by epigenetic reprogramming and ecological remodeling. Six major
resistance mechanisms are highlighted: (1) Genetic and structural drivers, MYCN ecDNA variation and clonal evolution; (2) Epigenetic and CRC
remodeling, super-enhancer (SE) reorganization and PRRX1/NOTCH activation with ASCL1/PHOX2B suppression; (3) Target loss and bypass
activation, receptor-ligand rewiring (e.g., HB-EGF –ERBB4) sustaining MAPK/PI3K signaling; (4) Persister and memory programs, low RNA
velocity and JNK-dependent transcriptional noise reduction; (5) Immune and in ﬂammatory vulnerability, TLR3-dsRNA activation, cGAS-STING
deﬁciency, and GD2 plasticity; and (6) Metabolic and retinoic acid tolerance, enhanced lipid metabolism, ROS buffering, and autocrine RA
synthesis. Together, these multi-layered processes drive adaptive resistance and therapeutic escape in NB.
G.-q. He et al.
132
Oncogene (2026) 45:123 – 139

chemotherapy, shows a pronounced decline in cell-cycle activity
and enters a state of slow proliferation or quiescence. RNA velocity
analyses reveal minimal transcriptional ﬂux and a lack of
directional transitions toward new cellular states [ 156]. Concur-
rently, multiple single-cell ATAC-seq, snATAC-seq, or joint multi-
omic studies have demonstrated that these residual or drug-
tolerant cells often exhibit a more closed chromatin landscape,
with fewer accessible regions and attenuated enhancer activity
[108, 129, 143]. Collectively, these ﬁndings indicate that NB
resistance involves not only transcriptional and metabolic
adaptation but also an epigenetically stabilized quiescent state,
representing a reversible yet resilient survival program that
bridges transient persistence and long-term resistance.
Immune and in ﬂammatory vulnerabilities
The TME plays a critical role in the development of therapeutic
resistance. Single-cell and spatial multi-omics studies have
revealed a deep coupling between in ﬂammatory and immune
signaling and the evolution of resistance. The epigenetic state
determines in ﬂammatory sensing, with ADR and MES lineages
exhibiting distinct capacities in innate immune pathways.
Speciﬁcally, most NB cells lack cGAS –STING–mediated DNA
sensing, whereas MES-state cells display a stronger TLR3-
dependent recognition of double-stranded RNA (dsRNA), accom-
panied by higher basal in ﬂammatory levels and a more active pro-
inﬂammatory transcriptomic pro ﬁle. Reprogramming ADR cells
into the MES state restores dsRNA responsiveness, induces
cytokine secretion, and enhances T cell –mediated cytotoxicity,
indicating an immune vulnerability window linked to lineage
plasticity [ 163].
In resistant lesions, immunosuppressive signaling axes are
frequently “switched on. ” Integrated single-cell transcriptomic
interaction analyses have identi ﬁed NECTIN2 –TIGIT as a key
immune checkpoint pathway in NB, and functional assays have
shown that combined blockade can partially reverse immune
escape and restore effector T cell activity. This ﬁnding is consistent
with the bone marrow metastatic niche, where SPP1 ⁺ macro-
phages and neutrophils are enriched, immunosuppressive signal-
ing is upregulated, and chromatin accessibility is reprogrammed,
together forming a microenvironmental foundation that facilitates
bypass activation and immune exclusion [ 142].
Moreover, the epigenetic plasticity of tumor-associated differ-
entiation antigens provides a manipulable opportunity for
combinatorial immunotherapy. Studies have demonstrated that
EZH2 inhibition can reprogram lineage states and upregulate GD2
expression, thereby restoring or enhancing anti-GD2 therapeutic
responses. This discovery links epigenetic modulators with
antibody-based therapy, offering a strategic anchor to counteract
AMT/MES-associated resistance [ 164].
Metabolic and retinoic acid tolerance
Metabolic adaptation represents a crucial layer in the develop-
ment of drug resistance in NB, particularly evident in MES and
persister-like subpopulations. These cells undergo extensive
metabolic rewiring, forming a state characterized by enhanced
oxidative phosphorylation (OXPHOS) and fatty acid oxidation
(FAO) dependence, increased antioxidant capacity, and activation
of endogenous all-trans retinoic acid (RA) synthesis, enabling long-
term survival under chemotherapeutic and oxidative stress.
Studies have shown that MYCN-ampli ﬁed NB cells exhibit
signiﬁcant metabolic reprogramming at the energetic level,
characterized by enhanced mitochondrial respiration, increased
dependence on FAO, and elevated glycolytic ﬂux. This type of
metabolic remodeling supports sustained energy production and
stress resistance, while simultaneously exposing new metabolic
vulnerabilities. For instance, the CPT1A-mediated FAO pathway
has been identi ﬁed as a potential therapeutic target [ 93, 165].
Moreover, the upregulation of lipid metabolism promotes
membrane biosynthesis, lipid signaling molecule generation,
and energy compensation, providing long-term metabolic support
for resistant cells.
In terms of oxidative stress defense, resistant NB cells often
display persistent activation of the glutathione (GSH) –Nrf2–HO-1
antioxidant axis. As a master regulator of oxidative stress, Nrf2
upregulates multiple antioxidant and detoxi ﬁcation-related genes,
thereby eliminating reactive oxygen species (ROS) and maintain-
ing intracellular redox homeostasis. This feature is recognized as a
hallmark of cell persistence and chemoresistance across multiple
cancer types [ 166].
More importantly, MES-type NB cells possess an intrinsic
ability to synthesize endogenous RA. Recent studies have shown
that this subpopulation forms an autocrine RA loop through
ALDH1A1/ALDH1A3-mediated retinal oxidation, leading to
pronounced differentiation resistance to exogenous RA
in vitro. Endogenous RA, in turn, maintains the MES transcrip-
tional state and promotes cell migration and survival, constitut-
ing a major mechanism of resistance to differentiation therapies
such as ATRA [ 167].
EMERGING BIOMARKERS AND THERAPEUTIC TARGETS
Identiﬁcation of emerging biomarkers driven by single-
cell omics
NB exhibits remarkable molecular and clinical heterogeneity,
which has long limited the ability of conventional bulk gene
expression analyses to precisely delineate its key drivers and
therapeutic response patterns [ 168]. In recent years, advances in
single-cell multi-omics integration — encompassing transcriptomic,
epigenomic, and proteomic data — have enabled researchers to
simultaneously dissect the dynamic states and molecular interac-
tions of tumor, immune, and stromal cells. This shift from
population-level to cell-speci ﬁc resolution has rede ﬁned biomar-
ker discovery, allowing reconstruction of NB ’s evolutionary
trajectory and treatment response at a molecular scale. Such an
approach not only reveals core regulatory nodes of tumor
initiation and progression but also provides a high-resolution
framework for risk strati ﬁcation and precision therapy.
Among these studies, several transcriptional regulators, includ-
ing STMN2, TUBA1A, PAGE5, and ETV1, have been identi ﬁed as key
drivers of NB tumorigenesis and intratumoral heterogeneity,
suggesting their potential as therapeutic targets. Moreover, ITGB1,
which is highly expressed in M2-like macrophages, has been
associated with favorable prognosis, underscoring its dual
potential as a diagnostic biomarker and immunotherapeutic
target [ 169].
Recent single-cell analyses have further illuminated critical
signaling pathways mediating immune evasion and therapeutic
resistance within the NB tumor microenvironment. The
NECTIN2–TIGIT axis has been recognized as a major immune
checkpoint pathway that promotes T cell exhaustion and
attenuates antitumor immunity [ 142]. In vivo experiments
demonstrated that co-targeting TIGIT and PD-L1 markedly
suppressed tumor growth and induced complete remission, even
in chemotherapy-resistant NB models, highlighting the transla-
tional potential of this pathway for immunotherapy.
At the molecular subtype level, pathway analysis has revealed
that speci ﬁc transcriptional signatures can delineate highly
aggressive NB subtypes associated with poor prognosis, provid-
ing new insights for precision-targeted interventions [ 170].
Notably, the PCLAF ⁺ neuroendocrine cell subpopulation has
been identi ﬁ
ed as a major driver of NB progression. Further
studies demonstrated that this subpopulation is highly suscep-
tible to cuproptosis, a newly characterized form of copper-
dependent cell death, suggesting a promising metabolic
vulnerability that may be exploited for therapeutic intervention
in refractory NB.
G.-q. He et al.
133
Oncogene (2026) 45:123 – 139

Computationally powered prognostic signature identi ﬁcation
With the rapid advancement of computational science and
artiﬁcial intelligence (AI), machine learning algorithms have
become widely applied across various aspects of cancer research,
including diagnosis, classi ﬁcation, prognosis prediction, and
treatment response assessment. In NB, this trend is particularly
pronounced. By integrating multi-omics datasets, such as bulk
RNA sequencing, methylome, proteome, radiomics, and histo-
pathology, researchers have developed accurate risk-strati ﬁcation
models that enable data-driven decision-making in clinical
diagnosis and outcome evaluation [ 171–174].
At the single-cell resolution, however, computational
approaches remain in a phase of rapid expansion, primarily
serving to elucidate therapy resistance mechanisms and identify
cell-speciﬁc biomarkers. For example, using the acNMF algorithm,
researchers constructed a predictive model of drug response and
discovered that adrenergic gene expression patterns were
conserved between clinical and preclinical NB models, while
drug-resistant mesenchymal transcriptional programs were largely
conﬁned to tumor-associated non-malignant cells [ 123]. In high-
risk NB, chemotherapy induced a “weak-mesenchymal” transcrip-
tional state within adrenergic cells, suggesting that treatment may
drive a reversible mesenchymal transition. This ﬁnding not only
clariﬁed the cellular origin of post-treatment relapse and
resistance but also revealed a potential intervention window to
reprogram reversible transcriptional states.
At the same time, traditional biomarker discovery methods are
often expensive and time-consuming, which limits their transla-
tional ef ﬁciency. Consequently, high-throughput computational
models have emerged as effective alternatives for identifying key
prognostic genes. By combining multi-omics integration with
machine learning, multiple molecular signatures with strong
translational potential have been developed in NB. For instance,
Li et al. [ 175] established a machine learning model based on
differential enhancer methylation, which accurately distinguished
INSS stage 4 from stage 4S NB and identi ﬁed methylation markers
with dual diagnostic and prognostic value. Xia et al. [ 176]
developed a four-gene prognostic model incorporating the
mRNA-based stemness index (mRNAsi), revealing a close coupling
between tumor stemness and immune in ﬁltration. Similarly,
Cheng et al. [ 177] integrated ferroptosis-related gene expression
and found that high levels of MYCN and RRM2 constituted a core
molecular basis of chemoresistance in NB. In addition, Wang et al.
[178] proposed a mitochondria-related gene (MRG) signature,
which outperformed the traditional MYCN-based classi ﬁcation in
risk prediction and identi ﬁed FEN1 as a crucial regulator linking
metabolic reprogramming and immune suppression in NB.
Furthermore, Cai et al. [ 179] integrated E2F family transcription
factor-related genes to construct a prognostic model capable of
stratifying distinct risk subtypes and pinpointing potential
druggable targets for individualized therapy. In a related
approach, Aierken et al. [ 180] developed an 11-gene neutrophil
extracellular trap (NETs)-related model, which maintained stable
performance across cohorts and revealed the association between
NETs signaling and immunosuppressive TME. Finally, Chen et al.
[181] proposed a T-cell exhaustion (TEX)-related risk signature,
accurately predicting both immunotherapy response and patient
prognosis.
Collectively, these computationally powered strategies have
accelerated the discovery of prognostic biomarkers and thera-
peutic targets in NB. By integrating high-dimensional omics data
with machine learning frameworks, researchers can now delineate
complex molecular networks, improve precision in risk prediction,
and identify actionable pathways —
offering new opportunities to
enhance the survival of high-risk and relapsed NB patients who
remain refractory to multimodal therapy.
CHALLENGES AND FUTURE PERSPECTIVES
Despite the remarkable progress achieved through single-cell
studies in NB, substantial technical and translational challenges
remain (Table 1). At the technical level, maintaining cell viability,
preventing sample contamination, and the high cost and long
turnaround time of single-cell sequencing continue to limit study
scale and reproducibility [ 182–187]. Moreover, intrinsic variability
in single-cell data — arising from differences in cell-cycle stage,
sequencing depth, and sample heterogeneity — complicates inter-
pretation and necessitates advanced algorithms and standardized
workﬂows to minimize bias [ 187]. The pronounced heterogeneity
of NB further increases analytical complexity, requiring simulta-
neous characterization of developmental hierarchies among
malignant lineages and dynamic interactions among immune,
stromal, and vascular components within TME
[6, 25, 102, 188, 189]. Achieving robust multidimensional data
integration from limited pediatric samples remains a major
bottleneck for clinical translation.
Future multi-omics research should prioritize cross-layer inte-
gration and dynamic tracing. Integrating single-cell transcrip-
tomics with epigenomics will help delineate regulatory networks
involving chromatin accessibility and epigenetic modi ﬁcations,
thereby revealing key transcriptional nodes driving tumor
evolution and therapeutic resistance. The inclusion of single-cell
proteomics and metabolomics will further bridge the gap
between gene expression and signaling execution, offering a
functional perspective on cellular states. In parallel, the conver-
gence of spatial transcriptomics and imaging mass cytometry
allows in-situ reconstruction of the cellular ecosystem of NB,
enabling real-time mapping of immune in ﬁltration, metastatic
Table 1. Overcoming Challenges and Shaping Future Directions in Neuroblastoma.
Research aspect Key challenges Potential solutions
Technical limitations Loss of cell viability, sample contamination,
and high sequencing cost
Optimize tissue handling and cell preservation techniques; employ
microdissection-based enrichment and low-input sequencing
strategies
Data reliability Insuf ﬁcient sequencing depth and high
intercellular variability
Increase sequencing depth; integrate temporal and spatial multi-
omics data to improve normalization and consistency
Tumor heterogeneity Complex microenvironmental and
intercellular diversity
Develop cross-layer multi-omics frameworks to capture
tumor–microenvironment interactions
Multi-omics integration Limited application beyond scRNA-seq Expand multi-omics coverage and develop hierarchical data
integration algorithms
Computational
resources
High computational demand and limited
scalability of algorithms
Incorporate AI/ML-assisted high-throughput computing platforms and
construct interpretable analytical frameworks
Translational validation Lack of robust clinical cohorts and
functional validation experiments
Establish longitudinal clinical cohorts integrating spatial omics and
experimental models for mechanistic validation
G.-q. He et al.
134
Oncogene (2026) 45:123 – 139

progression, and therapeutic response, thereby offering novel
avenues for precision intervention [ 29, 190–192]. However, multi-
omics approaches are not universally applicable. When research
goals focus on validating speci ﬁc pathways, conducting low-
throughput mechanistic studies, or achieving rapid clinical testing,
comprehensive multi-omics pro ﬁling may introduce unnecessary
noise, cost, and analytical burden. In such contexts, hypothesis-
driven targeted multi-omics or layered bulk –single-cell validation
strategies are more appropriate, balancing data dimensionality
with biological interpretability [ 193, 194]. Particularly in pediatric
NB, where tissue access and sample size are often constrained,
excessive sequencing depth should be avoided in favor of cell
enrichment, snRNA-seq, or organoid-based models to enhance
signal-to-noise ratio and representativeness [ 195, 196].
To overcome current analytical and technical limitations, the
integration of arti ﬁcial intelligence (AI) and machine learning (ML)
has emerged as a pivotal strategy. AI-driven frameworks enable
nonlinear feature extraction and multimodal pattern recognition,
substantially improving the identi ﬁcation of rare cell subsets and
transient phenotypic transitions [ 197, 198]. Through deep neural
networks (DNNs) and self-supervised learning paradigms, these
models can automatically uncover latent correlations across
transcriptomic, methylomic, and proteomic layers, reconstructing
lineage trajectories and disease evolution. Meanwhile, spatiotem-
poral AI models, such as graph neural networks (GNNs) and
multimodal Transformers, have shown promise in systematically
reconstructing tumor –immune–stromal interaction networks and
predicting key signaling pathways and actionable therapeutic
targets [ 199]. Furthermore, AI facilitates quality control, anomaly
detection, and visualization, correcting sequencing bias, mitigat-
ing batch effects, and enhancing denoising accuracy [ 200].
Collectively, these advances markedly improve the reproducibility
and standardization of single-cell analyses, establishing a scalable
computational foundation for NB multi-omics research.
Looking ahead, progress in NB research will depend on the
synergistic integration of bioinformatics, clinical oncology, and
basic science. From the bioinformatics perspective, developing
scalable algorithmic frameworks and open-access data-sharing
platforms will enable large-scale, multi-center integration of NB
datasets. Clinically, establishing single-cell-driven patient cohorts
will facilitate biomarker validation and personalized therapeutic
guidance. At the mechanistic level, exploring the dynamic
interplay among tumor, immune, and metabolic networks will
provide essential functional validation for multi-omics discoveries.
As deep learning and spatial multi-omics continue to converge,
NB research is poised to evolve from descriptive molecular
proﬁling toward predictive and mechanistic modeling, paving the
way for precision oncology and improved long-term survival in
high-risk patients.
CONCLUSION
Recent advances in single-cell technologies have fundamentally
reshaped our understanding of neuroblastoma by revealing its
remarkable cellular diversity and molecular complexity. Beyond
traditional bulk transcriptomic approaches, single-cell and spatial
multi-omics have enabled precise mapping of malignant, immune,
stromal, and endothelial cell populations, uncovering their lineage
relationships and functional plasticity during tumor initiation,
progression, and relapse. These insights have not only clari ﬁed the
developmental origins of neuroblastoma but also illuminated how
transcriptional reprogramming, metabolic adaptation, and
immune modulation collectively drive disease heterogeneity.
At the molecular level, integrative single-cell analyses have
identiﬁed multiple coexisting malignant programs, ranging from
proliferative, neuronal, and mesenchymal-like to stress-adaptive
and persister phenotypes, re ﬂecting the dynamic equilibrium of
tumor ecosystems under therapeutic pressure. Alterations in
chromatin accessibility, metabolic ﬂux, and inﬂammatory signaling
converge to promote cell survival, immune evasion, and
therapeutic resistance. These
ﬁndings highlight that treatment
failure in neuroblastoma arises not from a single resistant clone
but from a coordinated network of adaptive states across the
tumor microenvironment.
Looking forward, the continued integration of transcriptomic,
epigenomic, proteomic, and metabolomic data, combined with
artiﬁcial intelligence –driven modeling, will be essential to capture
the spatial and temporal evolution of neuroblastoma with greater
precision. Such approaches will accelerate the discovery of
predictive biomarkers, identify actionable therapeutic vulnerabil-
ities, and facilitate personalized treatment strategies. Ultimately,
the synergy between single-cell technologies, computational
biology, and translational validation is expected to transform
neuroblastoma management from static classi ﬁcation to dynamic,
precision-guided intervention.
REFERENCES
1. Maris JM, Matthay KK. Molecular biology of neuroblastoma. J Clin Oncol.
1999;17:2264.
2. Park JR, Eggert A, Caron H. Neuroblastoma: biology, prognosis, and treatment.
Hematol /Oncol Clin North Am. 2010;24:65 –86.
3. Evans AE, D ’angio GJ, Propert K, Anderson J, Hann HWL. Prognostic factors in
neuroblastoma. Cancer. 1987;59:1853 –9.
4. Shohet JM, Nuchtern JG, Foster JH. Treatment and prognosis of neuroblastoma.
UpToDate, Post, TW (Ed) Waltham, MA UpToDate 2022.
5. Kushner BH. Neuroblastoma: a disease requiring a multitude of imaging studies.
J Nucl Med. 2004;45:1172 –88.
6. Lundberg KI, Treis D, Johnsen JI. Neuroblastoma Heterogeneity, Plasticity, and
Emerging Therapies. Curr Oncol Rep. 2022;24:1053 –62.
7. Pinto NR, Applebaum MA, Volchenboum SL, Matthay KK, London WB, Ambros
PF, et al. Advances in risk classi ﬁcation and treatment strategies for neuro-
blastoma. J Clin Oncol. 2015;33:3008 –17.
8. Li R, Polishchuk A, DuBois S, Hawkins R, Lee SW, Bagatell R. et al. Patterns of
relapse in high-risk neuroblastoma patients treated with and without total body
irradiation. Int J Radiat Oncol Biol Phys. 2017;97:270 –7.
9. George RE, Sanda T, Hanna M, Fröhling S, Ii WL, Zhang J, et al. Activating
mutations in ALK provide a therapeutic target in neuroblastoma. Nature.
2008;455:975–8.
10. Bresler SC, Weiser DA, Huwe PJ, Park JH, Krytska K, Ryles H, et al. ALK mutations
confer differential oncogenic activation and sensitivity to ALK inhibition therapy
in neuroblastoma. Cancer cell. 2014;26:682 –94.
11. Trigg RM, Turner SD. ALK in neuroblastoma: biological and therapeutic impli-
cations. Cancers. 2018;10:113.
12. Schleiermacher G, Javanmardi N, Bernard V, Leroy Q, Cappo J, Rio Frio T, et al.
Emergence of new ALK mutations at relapse of neuroblastoma. J Clin Oncol.
2014;32:2727–34.
13. Ozkaynak MF, Gilman AL, London WB, Naranjo A, Diccianni MB, Tenney SC, et al.
A Comprehensive Safety Trial of Chimeric Antibody 14.18 With GM-CSF, IL-2,
and Isotretinoin in High-Risk Neuroblastoma Patients Following Myeloablative
Therapy: Children ’s Oncology Group Study ANBL0931. Front Immunol.
2018;9:1355.
14. Yu AL, Gilman AL, Ozkaynak MF, Naranjo A, Diccianni MB, Gan J, et al. Long-
Term Follow-up of a Phase III Study of ch14.18 (Dinutuximab) + Cytokine
Immunotherapy in Children with High-Risk Neuroblastoma: COG Study
ANBL0032. Clin Cancer Res. 2021;27:2179 –89.
15. Desai AV, Gilman AL, Ozkaynak MF, Naranjo A, London WB, Tenney SC, et al.
Outcomes Following GD2-Directed Postconsolidation Therapy for Neuro-
blastoma After Cessation of Random Assignment on ANBL0032: A Report From
the Children ’s Oncology Group. J Clin Oncol. 2022;40:4107 –18.
16. Tas ML, Dootjes LW, Fiocco M, de Krijger RR, Dierselhuis MP, van Eijkelenburg
NKA, et al. Anti-GD2 Based Immunotherapy Prevents Late Events in High-Risk
Neuroblastoma Patients over 18 Months at Diagnosis. Cancers (Basel)
2021;13:4941.
17. Richards RM, Sotillo E, Majzner RG. CAR T cell therapy for neuroblastoma. Front
Immunol. 2018;9:2380.
18. Moghimi B, Muthugounder S, Jambon S, Tibbetts R, Hung L, Bassiri H, et al.
Preclinical assessment of the ef ﬁcacy and speci ﬁcity of GD2-B7H3 SynNotch
CAR-T in metastatic neuroblastoma. Nat Commun. 2021;12:511.
19. Lutskovich D, Meleshko A & Katsin M. State of the art and perspectives of CAR-T
cell therapy for neuroblastoma. Cytotherapy 2024.
G.-q. He et al.
135
Oncogene (2026) 45:123 – 139

20. Sun M, Cao Y, Okada R, Reyes-González JM, Stack HG, Qin H, et al. Preclinical
optimization of a GPC2-targeting CAR T-cell therapy for neuroblastoma. J
Immuno Therapy of Cancer 2023;11:e005881.
21. Dexter DL, Leith JT. Tumor heterogeneity and drug resistance. J Clin Oncol.
1986;4:244–57.
22. Zhang A, Miao K, Sun H, Deng C-X. Tumor heterogeneity reshapes the tumor
microenvironment to in ﬂuence drug resistance. Int J Biol Sci. 2022;18:3019.
23. Dagogo-Jack I, Shaw AT. Tumour heterogeneity and resistance to cancer
therapies. Nat Rev Clin Oncol. 2018;15:81 –94.
24. Gomez RL, Ibragimova S, Ramachandran R, Philpott A, Ali FR. Tumoral hetero-
geneity in neuroblastoma. Biochimica et Biophysica Acta (BBA)-Rev Cancer.
2022;1877:188805.
25. Ngan ES-W. Heterogeneity of neuroblastoma. Oncoscience. 2015;2:837.
26. Lei Y, Tang R, Xu J, Wang W, Zhang B, Liu J, et al. Applications of single-cell
sequencing in cancer research: progress and perspectives. J Hematol Oncol.
2021;14:91.
27. Gulati GS, D ’Silva JP, Liu Y, Wang L, Newman AM. Pro ﬁling cell identity and
tissue architecture with single-cell and spatial transcriptomics. Nat Rev Mol Cell
Biol. 2025;26:11 –31.
28. Levitin HM, Yuan J, Sims PA. Single-Cell Transcriptomic Analysis of Tumor Het-
erogeneity. Trends Cancer. 2018;4:264 –8.
29. Zhang Y, Wang D, Peng M, Tang L, Ouyang J, Xiong F, et al. Single-cell RNA
sequencing in cancer research. J Exp Clin Cancer Res. 2021;40:81.
30. Wang W, Wang L, She J, Zhu J. Examining heterogeneity of stromal cells in
tumor microenvironment based on pan-cancer single-cell RNA sequencing data.
Cancer Biol Med. 2021;19:30 –42.
31. Denisenko E, Guo BB, Jones M, Hou R, de Kock L, Lassmann T, et al. Systematic
assessment of tissue dissociation and storage biases in single-cell and single-
nucleus RNA-seq work ﬂows. Genome Biol. 2020;21:130.
32. Tirosh I, Suva ML. Cancer cell states: Lessons from ten years of single-cell RNA-
sequencing of human tumors. Cancer Cell. 2024;42:1497 –506.
33. Guo Y, Wang W, Ye K, He L, Ge Q, Huang Y, et al. Single-Nucleus RNA-Seq: Open
the Era of Great Navigation for FFPE Tissue. Int J Mol Sci. 2023;24:13744.
34. Oh J-M, An M, Son D-S, Choi J, Cho YB, Yoo CE, et al. Comparison of cell type
distribution between single-cell and single-nucleus RNA sequencing: enrich-
ment of adherent cell types in single-nucleus RNA sequencing. Exp Mol Med.
2022;54:2128–34.
35. García-Vicente L, Martínez-Fernández M, Borja M, Tran V, Álvarez-Vázquez A,
Flores-Hernández R, et al. Single-nucleus RNA sequencing reveals a preclinical
model for the most common subtype of glioblastoma. Commun Biol.
2025;8:671.
36. Wang L, Jung J, Babikir H, Shamardani K, Jain S, Feng X, et al. A single-cell atlas
of glioblastoma evolution under therapy reveals cell-intrinsic and cell-extrinsic
therapeutic targets. Nat Cancer. 2022;3:1534 –52.
37. Chien F, Michaud ME, Bakhtiari M, Schroff C, Snuderl M, Velazquez Vega JE, et al.
Medulloblastoma Spatial Transcriptomics Reveals Tumor Microenvironment
Heterogeneity with High-Density Progenitor Cell Regions Correlating with High-
Risk Disease. bioRxiv 2024;28:2024.06.25.600684.
38. Ren Y, Huang Z, Zhou L, Xiao P, Song J, He P, et al. Spatial transcriptomics
reveals niche-speci ﬁc enrichment and vulnerabilities of radial glial stem-like
cells in malignant gliomas. Nat Commun. 2023;14:1028.
39. Oliveira, MFd, Romero JP, Chung M, Williams SR, Gottscho AD, et al. High-
deﬁnition spatial transcriptomic pro ﬁling of immune cell populations in color-
ectal cancer. Nat Genet. 2025;57:1512 –23.
40. Okonechnikov K, Joshi P, Körber V, Rademacher A, Bortolomeazzi M, Mallm JP,
et al. Oncogene aberrations drive medulloblastoma progression, not initiation.
Nature. 2025;642:1062 –72.
41. Van de Velde LA, Allen EK, Crawford JC, Wilson TL, Guy CS, Russier M, et al.
Neuroblastoma Formation Requires Unconventional CD4 T Cells and Arginase-1-
Dependent Myeloid Cells. Cancer Res. 2021;81:5047 –59.
42. Clark SJ, Lee HJ, Smallwood SA, Kelsey G, Reik W. Single-cell epigenomics:
powerful new methods for understanding gene regulation and cell identity.
Genome Biol. 2016;17:72.
43. Sinha S, Satpathy AT, Zhou W, Ji H, Stratton JA, Jaffer A, et al. Pro ﬁling Chro-
matin Accessibility at Single-cell Resolution. Genomics Proteom Bioinforma.
2021;19:172–90.
44. Ziffra RS, Kim CN, Ross JM, Wilfert A, Turner TN, Haeussler M, et al. Single-cell
epigenomics reveals mechanisms of human cortical development. Nature.
2021;598:205–13.
45. Feng D, Liang Z, Wang Y, Yao J, Yuan Z, Hu G, et al. Chromatin accessibility
illuminates single-cell regulatory dynamics of rice root tips. BMC Biol.
2022;20:274.
46. Xiang Y, Zhang S, Huang Y, Zheng Z, Sun J, Zhao Q, et al. Single-cell chromatin
accessibility pro ﬁling reveals regulatory mechanisms and evolution in pig
brains. BMC Biol. 2025;23:163.
47. Yu Z, Lv Y, Su C, Lu W, Zhang R, Li J, et al. Integrative Single-Cell Analysis Reveals
Transcriptional and Epigenetic Regulatory Features of Clear Cell Renal Cell
Carcinoma. Cancer Res. 2023;83:700 –19.
48. Fang K, Ohihoin AG, Liu T, Choppavarapu L, Nosirov B, Wang Q, et al. Integrated
single-cell analysis reveals distinct epigenetic-regulated cancer cell states and a
heterogeneity-guided core signature in tamoxifen-resistant breast cancer.
Genome Med. 2024;16:134.
49. Satpathy AT, Granja JM, Yost KE, Qi Y, Meschi F, McDermott GP, et al. Massively
parallel single-cell chromatin landscapes of human immune cell development
and intratumoral T cell exhaustion. Nat Biotechnol. 2019;37:925 –36.
50. Simon M, Stüve P, Schmidleithner L, Bittner S, Beumer N, Strieder N, et al.
Single-cell chromatin accessibility a nd transposable element landscapes
reveal shared features of tissue-residing immune cells. Immunity.
2024;57:1975 –93.e1910.
51. Cai S, Hu B, Wang X, Liu T, Lin Z, Tong X, et al. Integrative single-cell RNA-seq
and ATAC-seq analysis of myogenic differentiation in pig. BMC Biol. 2023;21:19.
52. Miyao T, Miyauchi M, Kelly ST, Terooatea TW, Ishikawa T, Oh E, et al. Integrative
analysis of scRNA-seq and scATAC-seq revealed transit-amplifying thymic epi-
thelial cells expressing autoimmune regulator. eLife. 2022;11:e73998.
53. Berest I, Tangherloni A. Integration of scATAC-Seq with scRNA-Seq Data.
Methods Mol Biol. 2023;2584:293 –310.
54. Wu Y, Terekhanova NV, Caravan W, Naser Al Deen N, Lal P, Chen S, et al. Epi-
genetic and transcriptomic characterization reveals progression markers and
essential pathways in clear cell renal cell carcinoma. Nat Commun.
2023;14:1681.
55. Wang X, Sun Q, Liu T, Lu H, Lin X, Wang W, et al. Single-cell multi-omics
sequencing uncovers region-speci ﬁc plasticity of glioblastoma for com-
plementary therapeutic targeting. Sci Adv. 2024;10:eadn4306.
56. Steele CD, Abbasi A, Islam SMA, Bowes AL, Khandekar A, Haase K, et al. Sig-
natures of copy number alterations in human cancer. Nature. 2022;606:984 –91.
57. Shlien A, Malkin D. Copy number variations and cancer. Genome Med.
2009;1:62.
58. Ma L, Wang L, Chang C-W, Heinrich S, Dominguez D, Forgues M, et al. Single-cell
atlas of tumor clonal evolution in liver cancer. bioRxiv 2020; 2020.2008.
2018.254748.
59. Ren Y, Huang S, Dai C, Xie D, Zheng L, Xie H, et al. Germline Predisposition and
Copy Number Alteration in Pre-stage Lung Adenocarcinomas Presenting as
Ground-Glass Nodules. Front Oncol. 2019;9:288.
60. Fu X, Lei H, Tao Y, Heselmeyer-Haddad K, Torres I, Dean M, et al. Joint Clustering
of Single-Cell Sequencing and Fluorescence In Situ Hybridization Data for
Reconstructing Clonal Heterogeneity in Cancers. J Comput Biol.
2021;28:1035–51.
61. Li B, Huang Z, Yu W, Liu S, Zhang J, Wang Q, et al. Molecular subtypes based on
CNVs related gene signatures identify candidate prognostic biomarkers in lung
adenocarcinoma. Neoplasia. 2021;23:704 –17.
62. Wu CY, Lau BT, Kim HS, Sathe A, Grimes SM, Ji HP, et al. Integrative single-cell
analysis of allele-speci ﬁc copy number alterations and chromatin accessibility in
cancer. Nat Biotechnol. 2021;39:1259 –69.
63. Mlakar V, Dupanloup I, Gonzales F, Papangelopoulou D, Ansari M. Gumy-Pause F
17q Gain in Neuroblastoma: A Review of Clinical and Biological Implications.
Cancers (Basel) 2024;16:338.
64. Attiyeh EF, London WB, Mossé YP, Wang Q, Winter C, Khazi D, et al. Chromo-
some 1p and 11q deletions and outcome in neuroblastoma. N Engl J Med.
2005;353:2243–53.
65. Zhou Y, Chen X, Chapman JS, Barrett MT. Single nucleus DNA sequencing of
ﬂow sorted archived frozen and formalin ﬁxed parafﬁn embedded solid tumors.
BMC Genomics. 2024;25:943.
66. Hwang WL, Wolfson RL, Niemierko A, Marcus KJ, DuBois SG, Haas-Kogan D.
Clinical Impact of Tumor Mutational Burden in Neuroblastoma. J Natl Cancer
Inst. 2019;111:695 –9.
67. Patel AG, Ashenberg O, Collins NB, Segerstolpe Å, Jiang S, Slyper M, et al. A
spatial cell atlas of neuroblastoma reveals developmental, epigenetic and spa-
tial axis of tumor heterogeneity. bioRxiv 2024;16:2024.01.07.574538.
68. Gundem G, Levine MF, Roberts SS, Cheung IY, Medina-Martínez JS, Feng Y, et al.
Clonal evolution during metastatic spread in high-risk neuroblastoma. Nat
Genet. 2023;55:1022 –33.
69. Brady SW, Liu Y, Ma X, Gout AM, Hagiwara K, Zhou X, et al. Pan-neuroblastoma
analysis reveals age- and signature-associated driver alterations. Nat Commun.
2020;11:5183.
70. Baughn LB, Jessen E, Sharma N, Tang H, Smadbeck JB, Long MD, et al. Mass
Cytometry reveals unique phenotypic patterns associated with subclonal
diversity and outcomes in multiple myeloma. Blood Cancer J. 2023;13:84.
71. Zhang Q, Ye M, Lin C, Hu M, Wang Y, Lou Y, et al. Mass cytometry-based
peripheral blood analysis as a novel tool for early detection of solid tumours: a
multicentre study. Gut. 2023;72:996 –1006.
G.-q. He et al.
136
Oncogene (2026) 45:123 – 139

72. Garman B, Jiang C, Daouti S, Kumar S, Mehta P, Jacques MK, et al. Compre-
hensive immunophenotyping of solid tumor-in ﬁltrating immune cells reveals
the expression characteristics of LAG-3 and its ligands. Front Immunol.
2023;14:2023.
73. Nolo R, Herbrich S, Rao A, Zweidler-McKay P, Kannan S, Gopalakrishnan V.
Targeting P-selectin blocks neuroblastoma growth. Oncotarget
2017;8:86657−70.
74. Fernández-Zapata C, Leman JKH, Priller J, Böttcher C. The use and limitations of
single-cell mass cytometry for studying human microglia function. Brain Pathol.
2020;30:1178–91.
75. Lee S, Vu HM, Lee JH, Lim H, Kim MS. Advances in Mass Spectrometry-Based
Single Cell Analysis. Biology (Basel) 2023;12:395.
76. Budnik B, Levy E, Harmange G, Slavov N. SCoPE-MS: mass spectrometry of single
mammalian cells quanti ﬁes proteome heterogeneity during cell differentiation.
Genome Biol. 2018;19:161.
77. Specht H, Emmott E, Petelski AA, Huffman RG, Perlman DH, Serra M, et al. Single-
cell proteomic and transcriptomic analysis of macrophage heterogeneity using
SCoPE2. Genome Biol. 2021;22:50.
78. Petelski AA, Emmott E, Leduc A, Huffman RG, Specht H, Perlman DH, et al.
Multiplexed single-cell proteomics using SCoPE2. Nat Protoc. 2021;16:5398 –425.
79. Zhu Y, Piehowski PD, Zhao R, Chen J, Shen Y, Moore RJ, et al. Nanodroplet
processing platform for deep and quantitative proteome pro ﬁling of 10-100
mammalian cells. Nat Commun. 2018;9:882.
80. Derks J, Leduc A, Wallmann G, Huffman RG, Willetts M, Khan S, et al. Increasing
the throughput of sensitive proteomics by plexDIA. Nat Biotechnol.
2023;41:50–59.
81. Stoeckius M, Hafemeister C, Stephenson W, Houck-Loomis B, Chattopadhyay PK,
Swerdlow H, et al. Simultaneous epitope and transcriptome measurement in
single cells. Nat Methods. 2017;14:865 –8.
82. Peterson VM, Zhang KX, Kumar N, Wong J, Li L, Wilson DC, et al. Multiplexed
quantiﬁcation of proteins and transcripts in single cells. Nat Biotechnol.
2017;35:936–9.
83. Leader AM, Grout JA, Maier BB, Nabet BY, Park MD, Tabachnikova A, et al. Single-
cell analysis of human non-small cell lung cancer lesions re ﬁnes tumor classi-
ﬁcation and patient strati ﬁcation. Cancer Cell. 2021;39:1594 –1609.e1512.
84. Elaldi R, Hemon P, Petti L, Cosson E, Desrues B, Sudaka A, et al. High Dimensional
Imaging Mass Cytometry Panel to Visualize the Tumor Immune Microenviron-
ment Contexture. Front Immunol. 2021;12:2021.
85. Xiao X, Guo Q, Cui C, Lin Y, Zhang L, Ding X, et al. Multiplexed imaging mass
cytometry reveals distinct tumor-immune microenvironments linked to immu-
notherapy responses in melanoma. Commun Med (Lond). 2022;2:131.
86. Kedei N, Pérez-Guijarro EE, Chen J-Q, Day C-P, Malik MQ, Goldstein DJ, et al.
CODEX high-multiplex imaging reveals distinct tumor microenvironment in
mouse melanoma models associated with response to immunotherapy. Cancer
Res. 2020;80:3863.
87. Goltsev Y, Samusik N, Kennedy-Darling J, Bhate S, Hale M, Vazquez G, et al. Deep
Proﬁling of Mouse Splenic Architecture with CODEX Multiplexed Imaging. Cell.
2018;174:968–81.e915.
88. Petrova B, Guler AT. Recent Developments in Single-Cell Metabolomics by Mass
Spectrometry─A Perspective. J Proteome Res. 2025;24:1493 –518.
89. Lanekoff I, Sharma VV, Marques C. Single-cell metabolomics: where are we and
where are we going?. Curr Opin Biotechnol. 2022;75:102693.
9 0 . W e iD ,X uM ,W a n gZ ,T o n gJ .T h eD e v e l o p m e n to fS i n g l e - C e l lM e t a b o l i s m
and Its Role in Studying Cancer Emergent Properties. Front Oncol.
2021;11:814085.
91. Zhang C, Le Dévédec SE, Ali A, Hankemeier T. Single-cell metabolomics by mass
spectrometry: ready for primetime?. Curr Opin Biotechnol. 2023;82:102963.
92. Oliynyk G, Ruiz-Pérez MV, Sainero-Alcolado L, Dzieran J, Zirath H, Gallart-Ayala H,
et al. MYCN-enhanced Oxidative and Glycolytic Metabolism Reveals Vulner-
abilities for Targeting Neuroblastoma. iScience. 2019;21:188 –204.
93. Bansal M, Gupta A, Ding HF. MYCN and Metabolic Reprogramming in Neuro-
blastoma. Cancers. 2022;14:4113.
94. Yoshida GJ. Beyond the Warburg Effect: N-Myc Contributes to Metabolic
Reprogramming in Cancer Cells. Front Oncol. 2020;10:791.
95. Jiang M, Stanke J, Lahti JM. The connections between neural crest development
and neuroblastoma. Curr Top Dev Biol. 2011;94:77 –127.
96. Tsubota S, Kadomatsu K. Origin and initiation mechanisms of neuroblastoma.
Cell Tissue Res. 2018;372:211 –21.
97. Wright JH. Neurocytoma or neuroblastoma, a kind of tumor not generally
recognized. J Exp Med. 1910;12:556 –61.
98. Jansky S, Sharma AK, Körber V, Quintero A, Toprak UH, Wecht EM, et al. Single-
cell transcriptomic analyses provide insights into the developmental origins of
neuroblastoma. Nat Genet. 2021;53:683 –93.
99. Johnsen JI, Dyberg C, Wickström M. Neuroblastoma-A Neural Crest Derived
Embryonal Malignancy. Front Mol Neurosci. 2019;12:9.
100. Zeineldin M, Patel AG, Dyer MA. Neuroblastoma: When differentiation goes
awry. Neuron. 2022;110:2916 –28.
101. Durbin AD, Versteeg R. Cell state plasticity in neuroblastoma. EJC Paediatr
Oncol. 2024;4:100184.
102. Ponzoni M, Bachetti T, Corrias MV, Brignole C, Pastorino F, Calarco E, et al.
Recent advances in the developmental origin of neuroblastoma: an overview. J
Exp Clin Cancer Res. 2022;41:92.
103. Furlan A, Dyachuk V, Kastriti ME, Calvo-Enrique L, Abdo H, Hadjab S, et al.
Multipotent peripheral glial cells generate neuroendocrine cells of the adrenal
medulla. Science 2017;357:eaal3753.
104. Hanemaaijer ES, Margaritis T, Sanders K, Bos FL, Candelli T, Al-Saati H, et al. Single-
cell atlas of developing murine adrenal gland reveals relation of Schwann cell
precursor signature to neuroblastoma phenotype. Proc Natl Acad Sci USA.
2021;118:e2022350118.
105. Kameneva P, Artemov AV, Kastriti ME, Faure L, Olsen TK, Otte J, et al. Single-cell
transcriptomics of human embryos identi ﬁes multiple sympathoblast lineages
with potential implications for neuroblastoma origin. Nat Genet.
2021;53:694–706.
106. Espinosa-Medina I, Outin E, Picard CA, Chettouh Z, Dymecki S, Consalez GG,
et al. Neurodevelopment. Parasympathetic ganglia derive from Schwann cell
precursors. Science. 2014;345:87 –90.
107. Dong R, Yang R, Zhan Y, Lai HD, Ye CJ, Yao XY, et al. Single-Cell Characterization
of Malignant Phenotypes and Developmental Trajectories of Adrenal Neuro-
blastoma. Cancer Cell. 2020;38:716 –33.e716.
108. Olsen TK, Otte J, Mei S, Embaie BT, Kameneva P, Cheng H, et al. Joint single-cell
genetic and transcriptomic analysis reveal pre-malignant SCP-like subclones in
human neuroblastoma. Mol Cancer. 2024;23:180.
109. Andersson N, Bakker B, Karlsson J, Valind A, Holmquist Mengelbier L, Spierings
DCJ, et al. Extensive Clonal Branching Shapes the Evolutionary History of High-
Risk Pediatric Cancers. Cancer Res. 2020;80:1512 –23.
110. Abbasi MR, Rifatbegovic F, Brunner C, Mann G, Ziegler A, Pötschger U, et al.
Impact of Disseminated Neuroblastoma Cells on the Identi ﬁcation of the
Relapse-Seeding Clone. Clin Cancer Res. 2017;23:4224 –32.
111. Sidell N, Altman A, Haussler MR, Seeger RC. Effects of retinoic acid (RA) on the
growth and phenotypic expression of several human neuroblastoma cell lines.
Exp Cell Res. 1983;148:21 –30.
112. Boeva V, Louis-Brennetot C, Peltier A, Durand S, Pierre-Eugène C, Raynal V, et al.
Heterogeneity of neuroblastoma cell identity de ﬁned by transcriptional circui-
tries. Nat Genet. 2017;49:1408 –13.
113. Ciccarone V, Spengler BA, Meyers MB, Biedler JL, Ross RA. Phenotypic diversi-
ﬁcation in human neuroblastoma cells: expression of distinct neural crest
lineages. Cancer Res. 1989;49:219 –25.
114. Rettig WJ, Spengler BA, Chesa PG, Old LJ, Biedler JL. Coordinate changes in
neuronal phenotype and surface antigen expression in human neuroblastoma
cell variants. Cancer Res. 1987;47:1383 –9.
115. Acosta S, Lavarino C, Paris R, Garcia I, de Torres C, Rodríguez E, et al. Compre-
hensive characterization of neuroblastoma cell line subtypes reveals bilineage
potential similar to neural crest stem cells. BMC Developmental Biol. 2009;9:12.
116. van Groningen T, Koster J, Valentijn LJ, Zwijnenburg DA, Akogul N, Hasselt NE,
et al. Neuroblastoma is composed of two super-enhancer-associated differ-
entiation states. Nat Genet. 2017;49:1261 –6.
117. Gomez RL, Woods LM, Ramachandran R, Abou Tayoun AN, Philpott A, Ali FR.
Super-enhancer associated core regulatory circuits mediate susceptibility to
retinoic acid in neuroblastoma cells. Front Cell Dev Biol. 2022;10:943924.
118. Sengupta S, Das S, Crespo AC, Cornel AM, Patel AG, Mahadevan NR, et al.
Mesenchymal and adrenergic cell lineage states in neuroblastoma possess
distinct immunogenic phenotypes. Nat Cancer. 2022;3:1228 –46.
119. van Groningen T, Akogul N, Westerhout EM, Chan A, Hasselt NE, Zwijnenburg
DA, et al. A NOTCH feed-forward loop drives reprogramming from adrenergic to
mesenchymal state in neuroblastoma. Nat Commun. 2019;10:1530.
120. Xu M, Hong JJ, Zhang X, Sun M, Liu X, Kang J. Targeting SWI/SNF ATPases
reduces neuroblastoma cell plasticity. EMBO J. 2024;43:4522 –4541.
121. Shi H, Tao T, Abraham BJ, Durbin AD, Zimmerman MW, Kadoch C, et al. ARID1A
loss in neuroblastoma promotes the adrenergic-to-mesenchymal transition by
regulating enhancer-mediated gene expression. Sci Adv. 2020;6:eaaz3440.
122. Thirant C, Peltier A, Durand S, Kramdi A, Louis-Brennetot C, Pierre-Eugène C,
et al. Reversible transitions between noradrenergic and mesenchymal tumor
identities de ﬁne cell plasticity in neuroblastoma. Nat Commun. 2023;14:2575.
123. Chapple RH, Liu X, Natarajan S, Alexander MIM, Kim Y, Patel AG, et al. An
integrated single-cell RNA-seq map of human neuroblastoma tumors and pre-
clinical models uncovers divergent mesenchymal-like gene expression pro-
grams. Genome Biol. 2024;25:161.
124. Bonine N, Zanzani V, Van Hemelryk A, Vanneste B, Zwicker C, Thoné T, et al.
NBAtlas: A harmonized single-cell transcriptomic reference atlas of human
neuroblastoma tumors. Cell Rep. 2024;43:114804.
G.-q. He et al.
137
Oncogene (2026) 45:123 – 139

125. Zhang Y, Ma Y, Liu Q, Du Y, Peng L, Zhou J, et al. Single-cell transcriptome
sequencing reveals tumor heterogeneity in family neuroblastoma. Front
Immunol. 2023;14:1197773.
126. Bedoya-Reina OC, Li W, Arceo M, Plescher M, Bullova P, Pui H, et al. Single-nuclei
transcriptomes from human adrenal gland reveal distinct cellular identities of
low and high-risk neuroblastoma tumors. Nat Commun. 2021;12:5309.
127. George SL, Parmar V, Lorenzi F, Marshall LV, Jamin Y, Poon E, et al. Novel
therapeutic strategies targeting telomere maintenance mechanisms in high-risk
neuroblastoma. J Exp Clin Cancer Res. 2020;39:78.
128. Mei S, Alchahin AM, Embaie BT, Gavriliuc IM, Verhoeven BM, Zhao T, et al.
Single-cell analyses of metastatic bone marrow in human neuroblastoma
reveals microenvironmental remodeling and metastatic signature. JCI Insight
2024;9:e173337.
129. Fetahu IS, Esser-Skala W, Dnyansagar R, Sindelar S, Rifatbegovic F, Bileck A, et al.
Single-cell transcriptomics and epigenomics unravel the role of monocytes in
neuroblastoma bone marrow metastasis. Nat Commun. 2023;14:3620.
130. Kildisiute G, Kholosy WM, Young MD, Roberts K, Elmentaite R, van Hooff SR, et al.
Tumor to normal single-cell mRNA comparisons reveal a pan-neuroblastoma
cancer cell. Sci Adv. 2021;7:eabd3311.
131. Neftel C, Laffy J, Filbin MG, Hara T, Shore ME, Rahme GJ, et al. An Integrative
Model of Cellular States, Plasticity, and Genetics for Glioblastoma. Cell.
2019;178:835–49.e821.
132. Tirosh I, Izar B, Prakadan SM, Wadsworth MH 2nd, Treacy D, Trombetta JJ, et al.
Dissecting the multicellular ecosystem of metastatic melanoma by single-cell
RNA-seq. Science. 2016;352:189 –96.
133. Azizi E, Carr AJ, Plitas G, Cornish AE, Konopacki C, Prabhakaran S, et al. Single-
Cell Map of Diverse Immune Phenotypes in the Breast Tumor Microenviron-
ment. Cell. 2018;174:1293 –1308.e1236.
134. Wagner J, Rapsomaniki MA, Chevrier S, Anzeneder T, Langwieder C, Dykgers A,
et al. A Single-Cell Atlas of the Tumor and Immune Ecosystem of Human Breast
Cancer. Cell. 2019;177:1330 –45.e1318.
135. Elyada E, Bolisetty M, Laise P, Flynn WF, Courtois ET, Burkhart RA, et al. Cross-Species
Single-Cell Analysis of Pancreatic Ductal Adenocarcinoma Reveals Antigen-
Presenting Cancer-Associated Fibroblasts. Cancer Discov. 2019;9:1102–23.
136. Ma L, Wang L, Khatib SA, Chang CW, Heinrich S, Dominguez DA, et al. Single-cell
atlas of tumor cell evolution in response to therapy in hepatocellular carcinoma
and intrahepatic cholangiocarcinoma. J Hepatol. 2021;75:1397 –408.
137. Peng C, Xu Y, Wu J, Wu D, Zhou L, Xia X. TME-Related Biomimetic Strategies
Against Cancer. Int J Nanomed. 2024;19:109 –35.
138. Chen D, Zhang X, Li Z, Zhu B. Metabolic regulatory crosstalk between tumor
microenvironment and tumor-associated macrophages. Theranostics. 2021;11:
1016–30.
139. Tiwari A, Trivedi R, Lin SY. Tumor microenvironment: barrier or opportunity
towards effective cancer therapy. J Biomed Sci. 2022;29:83.
140. Costa A, Thirant C, Kramdi A, Pierre-Eugène C, Louis-Brennetot C, Blanchard O,
et al. Single-cell transcriptomics reveals shared immunosuppressive landscapes
of mouse and human neuroblastoma. J Immunother Cancer. 2022;10:e004807.
141. Murray PJ. Macrophage Polarization. Annu Rev Physiol. 2017;79:541 –66.
142. Wienke J, Visser LL, Kholosy WM, Keller KM, Barisa M, Poon E, et al. Integrative
analysis of neuroblastoma by single-cell RNA sequencing identi ﬁes the NECTIN2-
TIGIT axis as a target for immunotherapy. Cancer Cell. 2024;42:283 –300.e288.
143. Yu W, Biyik-Sit R, Uzun Y, Chen CH, Thadi A, Sussman JH, et al. Longitudinal
single-cell multiomic atlas of high-risk neuroblastoma reveals chemotherapy-
induced tumor microenvironment rewiring. Nat Genet. 2025;57:1142 –54.
144. Giudice AM, Roth SL, Matlaga S, Cresswell-Clay E, Mishra P, Schürch PM, et al.
Reprogramming the neuroblastoma tumor immune microenvironment to
enhance GPC2 CAR T cells. Mol Ther. 2025;33:4552 –69.
145. Strijker JGM, Pascual-Pasto G, Grothusen GP, Kalmeijer YJ, Kalaitsidou E, Zhao C,
et al. Blocking MIF secretion enhances CAR T-cell ef ﬁcacy against neuro-
blastoma. Eur J Cancer. 2025;218:115263.
146. Verhoeven BM, Mei S, Olsen TK, Gustafsson K, Valind A, Lindström A, et al. The
immune cell atlas of human neuroblastoma. Cell Rep Med. 2022;3:100657.
147. Liu W, Wang C, Liang L, Zhang C, Li Y, Xiao J, et al. Single-cell RNA sequencing
analysis revealed the immunosuppressive remodeling of tumor-associated macro-
phages mediated by the MIF-CD74 axis in gastric cancer. Sci Rep. 2025;15:26883.
148. Batchu S, Hanafy KA, Redjal N, Godil SS, Thomas AJ. Single-cell analysis reveals
diversity of tumor-associated macrophages and their interactions with T lym-
phocytes in glioblastoma. Sci Rep. 2023;13:20874.
149. Ghaffari S, Rezaei N. Eosinophils in the tumor microenvironment: implications
for cancer immunotherapy. J Transl Med. 2023;21:551.
150. Ligan C, Ma XH, Zhao SL, Zhao W. The regulatory role and mechanism of mast
cells in tumor microenvironment. Am J Cancer Res. 2024;14:1 –15.
151. Zhao H, Wu L, Yan G, Chen Y, Zhou M, Wu Y, et al. In ﬂammation and tumor
progression: signaling pathways and targeted intervention. Signal Transduct
Target Ther. 2021;6:263.
152. Cao Z, Wang Q, Han Y, Lin J, Wu Q, Xu C, et al. Integrated single-cell and bulk
RNA sequencing analysis establishes a cancer associated ﬁ
broblast-related
signature for predicting prognosis and therapeutic responses in neuroblastoma.
Discov Oncol. 2025;16:1235.
153. Peng Z, Ye M, Ding H, Feng Z, Hu K. Spatial transcriptomics atlas reveals the
crosstalk between cancer-associated ﬁbroblasts and tumor microenvironment
components in colorectal cancer. J Transl Med. 2022;20:302.
154. Qi J, Sun H, Zhang Y, Wang Z, Xun Z, Li Z, et al. Single-cell and spatial analysis
reveal interaction of FAP(+) ﬁbroblasts and SPP1(+) macrophages in colorectal
cancer. Nat Commun. 2022;13:1742.
155. Jain S, Rick JW, Joshi RS, Beniwal A, Spatz J, Gill S, et al. Single-cell RNA
sequencing and spatial transcriptomics reveal cancer-associated ﬁbroblasts in
glioblastoma with protumoral effects. J Clin Invest. 2023;133:e147087.
156. Avitabile M, Bon ﬁglio F, Aievola V, Cantalupo S, Maiorino T, Lasorsa VA, et al.
Single-cell transcriptomics of neuroblastoma identi ﬁes chemoresistance-
associated genes and pathways. Comput Struct Biotechnol J. 2022;20:4437 –45.
157. Stöber MC, Chamorro González R, Brückner L, Conrad T, Wittstruck N, Szy-
mansky A, et al. Intercellular extrachromosomal DNA copy-number hetero-
geneity drives neuroblastoma cell state diversity. Cell Rep. 2024;43:114711.
158. Singh S, Fang J, Jin H, Van De Velde L-A, Cortes A, Chen J, et al. RBM39 degrader
invigorates innate immunity to eradicate neuroblastoma despite cancer cell
plasticity. Nat Commun. 2025;16:8287.
159. Wang L, Tan TK, Kim H, Kappei D, Tan SH, Look AT, et al. ASCL1 characterizes
adrenergic neuroblastoma via its pioneer function and cooperation with core
regulatory circuit factors. Cell Rep. 2023;42:113541.
160. Milazzo G, Perini G, Giorgi FM. Single-Cell Sequencing Identi ﬁes Master Regulators
Affected by Panobinostat in Neuroblastoma Cells. Genes (Basel) 2022;13:2240.
161. Berlak M, Tucker E, Dorel M, Winkler A, McGearey A, Rodriguez-Fos E, et al.
Mutations in ALK signaling pathways conferring resistance to ALK inhibitor
treatment lead to collateral vulnerabilities in neuroblastoma cells. Mol Cancer.
2022;21:126.
162. Hastings JF, Latham SL, Kamili A, Wheatley MS, Han JZR, Wong-Erasmus M, et al.
Memory of stochastic single-cell apoptotic signaling promotes chemoresistance
in neuroblastoma. Sci Adv. 2023;9:eabp8314.
163. Wolpaw AJ, Grossmann LD, Dessau JL, Dong MM, Aaron BJ, Brafford PA, et al.
Epigenetic state determines in ﬂammatory sensing in neuroblastoma. Proc Natl
Acad Sci USA. 2022;119:e2102358119.
164. Mabe NW, Huang M, Dalton GN, Alexe G, Schaefer DA, Geraghty AC, et al.
Transition to a mesenchymal state in neuroblastoma confers resistance to anti-
GD2 antibody via reduced expression of ST8SIA1. Nat Cancer. 2022;3:976 –93.
165. Agostini M, Melino G, Habeb B, Calandria JM, Bazan NG. Targeting lipid meta-
bolism in cancer: neuroblastoma. Cancer Metastasis Rev. 2022;41:255 –60.
166. Zhou X, Wang X, Li N, Guo Y, Yang X, Lei Y. Therapy resistance in neuroblastoma:
Mechanisms and reversal strategies. Front Pharm. 2023;14:1114295.
167. van Groningen T, Niklasson CU, Chan A, Akogul N, Westerhout EM, von et al. An
immature subset of neuroblastoma cells synthesizes retinoic acid and depends
on this metabolite. bioRxiv 2021; 2021.2005. 2018.444639.
168. Embaie BT, Sarkar H, Alchahin AM, Otte J, Olsen TK, Tümmler C, et al. Com-
parative Single-Cell Transcriptomics of Human Neuroblastoma and Preclinical
Models Reveals Conservation of an Adrenergic Cell State. Cancer Res.
2025;85:1015–34.
169. Liu Q, Wang Z, Jiang Y, Shao F, Ma Y, Zhu M, et al. Single-cell landscape analysis
reveals distinct regression trajectories and novel prognostic biomarkers in pri-
mary neuroblastoma. Genes Dis. 2022;9:1624 –38.
170. Sun L, Shao W, Lin Z, Lin J, Zhao F, Yu J. Single-cell RNA sequencing explored
potential therapeutic targets by revealing the tumor microenvironment of
neuroblastoma and its expression in cell death. Discov Oncol. 2024;15:409.
171. Jahangiri L. Predicting Neuroblastoma Patient Risk Groups, Outcomes, and
Treatment Response Using Machine Learning Methods: A Review. Med Sci.
(Basel) 2024;12:5.
172. Segura MF, Soriano A, Roma J, Piskareva O, Jiménez C, Boloix A, et al. Metho-
dological advances in the discovery of novel neuroblastoma therapeutics.
Expert Opin Drug Discov. 2022;17:167 –79.
173. Liu G, Poon M, Zapala MA, Temple WC, Vo KT, Matthay KK, et al. Incorporating
Radiomics into Machine Learning Models to Predict Outcomes of Neuro-
blastoma. J Digit Imaging. 2022;35:605 –12.
174. Tranchevent LC, Azuaje F, Rajapakse JC. A deep neural network approach to
predicting clinical outcomes of neuroblastoma patients. BMC Med Genomics.
2019;12:178.
175. Li S, Mi T, Jin L, Liu Y, Zhang Z, Wang J, et al. Integrative analysis with machine
learning identi ﬁes diagnostic and prognostic signatures in neuroblastoma
based on differentially DNA methylated enhancers between INSS stage 4 and 4S
neuroblastoma. J Cancer Res Clin Oncol. 2024;150:148.
176. Xia Y, Wang C, Li X, Gao M, Hogg HDJ, Tunthanathip T, et al. Development and
validation of a novel stemness-related prognostic model for neuroblastoma
G.-q. He et al.
138
Oncogene (2026) 45:123 – 139

using integrated machine learning and bioinformatics analyses. Transl Pediatr.
2024;13:91–109.
177. Cheng J, Dong X, Yang Y, Qin X, Zhou X, Zhang D. Synergistic machine learning
models utilizing ferroptosis-related genes for improved neuroblastoma out-
come prediction. Transl Pediatr. 2024;13:2164 –82.
178. Wang C, Tan J, Jin Y, Li Z, Yang J, Jia Y, et al. A mitochondria-related genes
associated neuroblastoma signature - based on bulk and single-cell tran-
scriptome sequencing data analysis, and experimental validation. Front Immu-
nol. 2024;15:1415736.
179. Cai D, Xu H, He S, Xu D, Li L. Precision prognostication in neuroblastomas via
clinically validated E2F activity signatures. Front Immunol. 2025;16:1612667.
180. Aierken Y, Tan K, Liu T, Lv Z. Prognosis and immune in ﬁltration prediction in
neuroblastoma based on neutrophil extracellular traps-related gene signature.
Sci Rep. 2025;15:5343.
181. Chen J, Zhai X, Kuang H, Zhang A. Prediction of neuroblastoma prognosis with a
novel T-cell exhaustion-related gene signature. Sci Rep. 2025;15:17885.
182. Ren X, Kang B, Zhang Z. Understanding tumor ecosystems by single-cell
sequencing: promises and limitations. Genome Biol. 2018;19:211.
183. Kharchenko PV. The triumphs and limitations of computational methods for
scRNA-seq. Nat Methods. 2021;18:723 –32.
184. Gawad C, Koh W, Quake SR. Single-cell genome sequencing: current state of the
science. Nat Rev Genet. 2016;17:175 –88.
185. Papalexi E, Satija R. Single-cell RNA sequencing to explore immune cell het-
erogeneity. Nat Rev Immunol. 2018;18:35 –45.
186. Lähnemann D, Köster J, Szczurek E, McCarthy DJ, Hicks SC, Robinson MD, et al.
Eleven grand challenges in single-cell data science. Genome Biol. 2020;21:31.
187. Stegle O, Teichmann SA, Marioni JC. Computational and analytical challenges in
single-cell transcriptomics. Nat Rev Genet. 2015;16:133 –45.
188. Schwab M, Westermann F, Hero B, Berthold F. Neuroblastoma: biology and
molecular and chromosomal pathology. Lancet Oncol. 2003;4:472 –80.
189. Brodeur GM, Nakagawara A. Molecular basis of clinical heterogeneity in neu-
roblastoma. Am J Pediatr Hematol Oncol. 1992;14:111 –6.
190. Baslan T, Hicks J. Unravelling biology and shifting paradigms in cancer with
single-cell sequencing. Nat Rev Cancer. 2017;17:557 –69.
191. Lim B, Lin Y, Navin N. Advancing Cancer Research and Medicine with Single-Cell
Genomics. Cancer Cell. 2020;37:456 –70.
192. Gohil SH, Iorgulescu JB, Braun DA, Keskin DB, Livak KJ. Applying high-
dimensional single-cell technologies to the analysis of cancer immunotherapy.
Nat Rev Clin Oncol. 2021;18:244 –56.
193. Le J, Dian Y, Zhao D, Guo Z, Luo Z, Chen X, et al. Single-cell multi-omics in cancer
immunotherapy: from tumor heterogeneity to personalized precision treatment.
Mol Cancer. 2025;24:221.
194. Dong M, Wang L, Hu N, Rao Y, Wang Z, Zhang Y. Integration of multi-omics
approaches in exploring intra-tumoral heterogeneity. Cancer Cell Int.
2025;25:317.
195. Lampis S, Galardi A, Di Paolo V, Di Giannatale A. Organoids as a new approach
for improving pediatric cancer research. Front Oncol. 2024;14:1414311.
196. Xiao Y, Li Y, Jing X, Weng L, Liu X, Liu Q, et al. Organoid models in oncology:
advancing precision cancer therapy and vaccine development. Cancer Biology
&. Medicine. 2025;22:903 –27.
197. Athaya T, Ripan RC, Li X, Hu H. Multimodal deep learning approaches for single-
cell multi-omics data integration. Brief Bioinform. 2023;24:bbad313.
198. Zhang J, Che Y, Liu R, Wang Z, Liu W. Deep learning-driven multi-omics analysis:
enhancing cancer diagnostics and therapeutics. Brief Bioinform 2025;26:bbaf440.
199. Waqas A, Tripathi A, Ramachandran RP, Stewart PA, Rasool G. Multimodal data
integration for oncology in the era of deep neural networks: a review. Front Artif
Intell. 2024;7:1408843.
200. Hu H, Quon G. scPair: Boosting single cell multimodal analysis by leveraging
implicit feature selection and single cell atlases. Nat Commun. 2024;15:9932.
AUTHOR CONTRIBUTIONS
GQH conceived of the presented idea and manuscript preparation. SJH, XYJ and YLD
conducted the primary review of the literature and gave intellectual input. XG, JG and WZ
conceived and organized the manuscript. All authors reviewed the results, provided
critical feedback and comments, and approved the ﬁnal version of the manuscript.
FUNDING
This study was funded by Chengdu Municipal Science Bureau Key Research and
Development Support Program Project (NO.2024-YF05-00034-SN) and Clinical
Research Special Funding of Wu Jieping Medical Foundation (25H1008) to GQH.
COMPETING INTERESTS
The authors declare no competing interests.
ADDITIONAL INFORMATION
Correspondence and requests for materials should be addressed to Xia Guo, Ju Gao
or Wei Zhang.
Reprints and permission information is available at http://www.nature.com/
reprints
Publisher’s note Springer Nature remains neutral with regard to jurisdictional claims
in published maps and institutional af ﬁliations.
Open Access This article is licensed under a Creative Commons
Attribution-NonCommercial-NoDerivatives 4.0 International License,
which permits any non-commercial use, sharing, distribution and reproduction in any
medium or format, as long as you give appropriate credit to the original author(s) and
the source, provide a link to the Creative Commons licence, and indicate if you modiﬁed
the licensed material. You do not have permission under this licence to share adapted
material derived from this article or parts of it. The images or other third party material in
this article are included in the article ’s Creative Commons licence, unless indicated
otherwise in a credit line to the material. If material is not included in the article ’s
Creative Commons licence and your intended use is not permitted by statutory
regulation or exceeds the permitted use, you will need to obtain permission directly
from the copyright holder. To view a copy of this licence, visit http://
creativecommons.org/licenses/by-nc-nd/4.0/.
© The Author(s) 2025
G.-q. He et al.
139
Oncogene (2026) 45:123 – 139