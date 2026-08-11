---
reference_id: DOI:10.1038/s42003-023-04790-6
title: Identifying dysregulated immune cell subsets following volumetric muscle loss with pseudo-time trajectories
authors:
- Lauren A. Hymel
- Shannon E. Anderson
- Thomas C. Turner
- William Y. York
- Hongmanlin Zhang
- Adrian R. Liversage
- Hong Seo Lim
- Peng Qiu
- Luke J. Mortensen
- Young C. Jang
- Nick J. Willett
- Edward A. Botchwey
journal: Communications Biology
year: '2023'
doi: 10.1038/s42003-023-04790-6
content_type: full_text_pdf
full_text_attempted: true
full_text_provider: openalex
full_text_url: "https://www.nature.com/articles/s42003-023-04790-6.pdf"
oa_status: gold
license: cc-by
local_pdf_path: files/DOI_10.1038_s42003-023-04790-6.pdf
---

# Identifying dysregulated immune cell subsets following volumetric muscle loss with pseudo-time trajectories
**Authors:** Lauren A. Hymel, Shannon E. Anderson, Thomas C. Turner, William Y. York, Hongmanlin Zhang, Adrian R. Liversage, Hong Seo Lim, Peng Qiu, Luke J. Mortensen, Young C. Jang, Nick J. Willett, Edward A. Botchwey
**Journal:** Communications Biology (2023)
**DOI:** [10.1038/s42003-023-04790-6](https://doi.org/10.1038/s42003-023-04790-6)

## Content

Abstract

                    Volumetric muscle loss (VML) results in permanent functional deficits and remains a substantial regenerative medicine challenge. A coordinated immune response is crucial for timely myofiber regeneration, however the immune response following VML has yet to be fully characterized. Here, we leveraged dimensionality reduction and pseudo-time analysis techniques to elucidate the cellular players underlying a functional or pathological outcome as a result of subcritical injury or critical VML in the murine quadriceps, respectively. We found that critical VML resulted in a sustained presence of M2-like and CD206
                    hi
                    Ly6C
                    hi
                    ‘hybrid’ macrophages whereas subcritical defects resolved these populations. Notably, the retained M2-like macrophages from critical VML injuries presented with aberrant cytokine production which may contribute to fibrogenesis, as indicated by their co-localization with fibroadipogenic progenitors (FAPs) in areas of collagen deposition within the defect. Furthermore, several T cell subpopulations were significantly elevated in critical VML compared to subcritical injuries. These results demonstrate a dysregulated immune response in critical VML that is unable to fully resolve the chronic inflammatory state and transition to a pro-regenerative microenvironment within the first week after injury. These data provide important insights into potential therapeutic strategies which could reduce the immune cell burden and pro-fibrotic signaling characteristic of VML.

ARTICLE
Identifying dysregulated immune cell subsets
following volumetric muscle loss with pseudo-time
trajectories
Lauren A. Hymel 1,2,10, Shannon E. Anderson 1,2,10, Thomas C. Turner 1,2, William Y. York 1,
Hongmanlin Zhang 2,3, Adrian R. Liversage 4,5, Hong Seo Lim 1,2, Peng Qiu 1,2, Luke J. Mortensen 4,5,
Young C. Jang 1,6 ✉, Nick J. Willett 2,6,7,8,9 ✉ & Edward A. Botchwey 1,2 ✉
Volumetric muscle loss (VML) results in permanent functional de ﬁcits and remains a sub-
stantial regenerative medicine challenge. A coordinated immune response is crucial for timely
myoﬁber regeneration, however the immune response following VML has yet to be fully
characterized. Here, we leveraged dimensionality reduction and pseudo-time analysis tech-
niques to elucidate the cellular players underlying a functional or pathological outcome as a
result of subcritical injury or critical VML in the murine quadriceps, respectively. We found
that critical VML resulted in a sustained presence of M2-like and CD206
hiLy6Chi ‘hybrid’
macrophages whereas subcritical defects resolved these populations. Notably, the retained
M2-like macrophages from critical VML injuries presented with aberrant cytokine production
which may contribute to ﬁbrogenesis, as indicated by their co-localization with ﬁbroadipo-
genic progenitors (FAPs) in areas of collagen deposition within the defect. Furthermore,
several T cell subpopulations were signi ﬁcantly elevated in critical VML compared to sub-
critical injuries. These results demonstrate a dysregulated immune response in critical VML
that is unable to fully resolve the chronic in ﬂammatory state and transition to a pro-
regenerative microenvironment within the ﬁrst week after injury. These data provide
important insights into potential therapeutic strategies which could reduce the immune cell
burden and pro- ﬁbrotic signaling characteristic of VML.
https://doi.org/10.1038/s42003-023-04790-6 OPEN
1 Department of Biomedical Engineering, Georgia Institute of Technology, Atlanta, GA, USA.2 Petit Institute for Bioengineering and Bioscience, Georgia Institute of
Technology, Atlanta, GA, USA.3 School of Materials Science and Engineering, Georgia Institute of Technology, Atlanta, GA, USA.4 School of Chemical, Materials,
and Biomedical Engineering, University of Georgia, Athens, GA, USA.5 Regenerative Bioscience Center, Rhodes Center for ADS, University of Georgia, Athens, GA,
USA. 6 Department of Orthopaedics, Emory University, Atlanta, GA, USA.7 Atlanta Veterans Affairs Medical Center, Decatur, GA, USA. 8 Phil and Penny Knight
Campus for Accelerating Scientiﬁc Impact, University of Oregon, Eugene, OR, USA.9 The Veterans Affairs Portland Health Care System, Portland, OR, USA.10These
authors contributed equally: Lauren A. Hymel, Shannon E. Anderson. ✉email: young.jang@emory.edu; nwillett@uoregon.edu; edward.botchwey@bme.gatech.edu
COMMUNICATIONS BIOLOGY |           (2023) 6:749 | https://doi.org/10.1038/s42003-023-04790-6 | www.nature.com/commsbio 1
1234567890():,;

F
ollowing acute muscle injury, skeletal muscle ’s robust
regenerative response relies on the prompt and proper
coordination of immune cells. The cellular dynamics of
myeloid and lymphoid cell traf ﬁcking into and out of the muscle
coincide with each stage of the muscle regenerative process 1.
Following muscle injury, there is degeneration and necrosis of
damaged myo ﬁbers2, triggering the invasion of neutrophils that
peak within hours following injury and drop off after 24 h 3.A s
neutrophils secrete tumor necrosis factor (TNF) and interferon- γ
(IFN-γ), monocyte derived pro-in ﬂammatory phagocytic (M1)
macrophages in ﬁltrate the muscle to aid in the removal of tissue
debris and propagate pro-in ﬂammatory signals by secretion of
cytokines1. Both TNF- α and IFN- γ play a role in macrophage
induction and skeletal muscle regeneration by silencing Pax7 and
preventing the expression of MyoD to maintain a required pool of
skeletal muscle stem/satellite cells (MuSCs), in an activated,
proliferative state1,4. M1 macrophage secretion of TNF- α is also a
mechanism to induce ﬁbroadipogenic progenitor cell (FAP)
clearance by apoptosis 5. FAPs are muscle- resident mesenchymal
stromal cells, and their regulated apoptosis induced by TNF- α is a
key signaling event for healthy extracellular matrix (ECM)
secretion6.
Once in tissue, classical Ly6C hi monocytes can convert into
non-classical Ly6C lo monocytes which are biased progenitors
of pro-regenerative (M2) macrophages, as we have shown
previously7. The transition to an anti-in ﬂammatory, interleukin
(IL)-10 and transforming growth factor (TGF)- β rich environ-
ment corresponds with both a transition to M2 macrophages
around 4 –7 days post injury 8,9 as well as the differentiation and
growth stages of myogenesis 10. As the skeletal muscle regenerates,
myeloid cells traf ﬁc out of the tissue by 2 weeks post-injury 11.
This coordinated response of myeloid cells is crucial for the
proper regeneration of skeletal muscle, as the depletion or altered
polarization of macrophages has been shown to increase adipose
and ﬁbrotic tissue deposition while reducing regenerated myo ﬁ-
ber cross-sectional area 12,13.
In addition to myeloid derived cells, lymphoid-derived T-cells
also respond to muscle injury. Peak in ﬁltration of CD4 + helper
and CD8 + cytotoxic T cells occurs at 3 days post-injury, return-
ing to baseline levels gradually by day 14 14. Regulatory T cells
(Treg cells) in ﬁltrate the muscle after acute injury with similar
kinetics to that of M2 macrophages — peaking at day 4 post-
injury15. The T cell response has been implicated in the main-
tenance of myeloid cell in ﬁltration. The depletion of CD8 + T cells
have been shown to reduce skeletal muscle regeneration through
a reduction in the recruitment of pro-in ﬂammatory M1
macrophages14. Similarly, depletion of T reg cells impairs muscle
repair and prolongs in ﬂammation15, which could be attributed to
the need of T reg cells for the transition from M1 to M2 macro-
phage phenotype, the ability of T reg cells to limit IFN- γ and
macrophage accrual, or the need for T reg derived IL-10 15–17. The
regulation of myeloid and lymphoid immune cell in ﬁltration and
clearance works in concert with the stages of myogenesis for
prompt muscle regeneration after acute injury.
By contrast, following large volume skeletal muscle loss that
exceeds the regenerative threshold (volumetric muscle loss,
VML), chronic in ﬂammation produces an inhospitable micro-
environment that does not allow for muscle regeneration. Instead,
healthy muscle ﬁbers are replaced by non-contractile ﬁbrotic
tissue resulting in chronic loss of function and permanent
disability18–20. This in ﬂammatory microenvironment after VML
has been previously characterized as having an enduring presence
of CD4 + and CD8 + T cells, as well as improper macrophage
polarization6,11,15,21,22. Moreover, a muscle environment that is
rich with both pro- and anti- in ﬂammatory factors (i.e. TNF- α
and TGF- β) can cause sustained presence of M2 macrophages
that shift from ‘pro-reparative’to ‘pro-ﬁbrotic’and drive FAPs to
a pathological state rather than a regenerative one 23. However,
the initial immune cell response following a critical muscle defect
that often leads to chronic in ﬂammation and ﬁbrotic outcomes
has not been elucidated. Previously, we characterized multiple
full-thickness biopsy punch injuries in the quadriceps muscles as
a VML model in C57BL/6 mice. We found that a 2 mm diameter
biopsy punch injury caused damage to the tissue, but the muscle
was able to regenerate without signi ﬁcant ﬁbrotic scarring
(denoted as subcritical injury). However, a 3 mm injury caused
persistent ﬁbrotic scarring and in ﬂammation through 4 weeks
following injury (denoted as critical VML injury) 24.
A population of cells captured at the same time via high-
dimensional immune cell pro ﬁling includes many distinct inter-
mediate differentiation states of cells; however, classical analytical
techniques only evaluate their average properties and thus mask
trends occurring across individual cells and subpopulations 25–27.
In this study, we approached this challenge by employing a
unique dimensionality reduction and clustering analytical strat-
egy that combines both uniform manifold approximation and
projection (UMAP) and spanning-tree progression analysis of
density-normalized events (SPADE); this analytical approach
captures the functional heterogeneity of the early immune cell
response and dynamics after an injury event and was applied to
the scenario of critical VML injury (Fig. 1). UMAP was utilized
for graphing single cells isolated from multiparameter ﬂow
Fig. 1 Graphical work ﬂow of multiparameter pseudo-time analysis applied to single cell ﬂow cytometry data. Animals received either a full-thickness,
unilateral subcritical injury (2 mm diameter biopsy) or critical VML injury (3 mm diameter biopsy) to the left quadriceps. Uninjured left quadriceps muscle
(indicated as day 0 in timeline) from naïve mice was used as a control. At 1, 3, or 7 days post injury, tissue was excised, digested, and single cells were
isolated and stained for ﬂow cytometric analysis. Dimensionality reduction and pseudo-time clustering algorithms, namely UMAP and SPADE, were
employed to characterize the temporal immune response of myeloid and lymphoid cells following VML. Created with BioRender.com.
ARTICLE COMMUNICATIONS BIOLOGY | https://doi.org/10.1038/s42003-023-04790-6
2 COMMUNICATIONS BIOLOGY |           (2023) 6:749 | https://doi.org/10.1038/s42003-023-04790-6 | www.nature.com/commsbio

cytometric analysis into a lower dimensional representation 28.
Furthermore, we leveraged SPADE clustering to reconstruct cel-
lular hierarchies and transitional states that can be inferred
through time — a concept known as ‘pseudo-time’25,29. By gen-
erating SPADE dendrograms with pooled sample data across
timepoints, single cells were clustered into distinct nodes and
then ordered along a trajectory to temporally track cellular
lineages and progressions. These dimensionality reduction and
clustering tools provide greater insights into the underlying het-
erogeneous cell populations contributing to the early immune
response after VML injury.
Previous studies have comprehensively reconstructed the
temporal response of cell populations following more established,
acute models of muscle injury 30,31. The objective of this study was
to characterize the immune cell dynamics that in ﬂuence the
pathological phenotype of a traumatic VML injury that cannot
endogenously regenerate versus a full-thickness injury still cap-
able of regeneration (2 mm subcritical injury) using our quad-
riceps VML model in C57BL/6 mice. We hypothesized that
critical VML would lead to persistent elevation of key immune
cell subpopulations, particularly those which are associated with
promoting ﬁbrosis.
Results
UMAP visualization of immune cell recruitment to critical
VML injury reveals persistent myeloid cell response . The ﬂow
panel designed for myeloid cell characterization contained anti-
bodies for CD11b, CD64, and MerTK for identifying all myeloid
cells, including parent monocyte and macrophage populations.
CD11b, a cell surface leukocyte integrin expressed on myeloid-
lineage cells, served as our canonical myeloid cell marker
32.
CD64, a high-afﬁnity Fc receptor, and MerTK, a receptor tyrosine
kinase and mediator of phagocytosis, are commonly used to
delineate tissue monocytes (CD11b +CD64+MerTK-SSClo) from
macrophages (CD11b +CD64+MerTK+)33. Ly6C antigen further
differentiates between classical Ly6C hi and non-classical Ly6C lo
murine monocytes 7,32, and together with mannose receptor
CD206, can be used to classify pro- in ﬂammatory M1-like mac-
rophages (Ly6C hiCD206lo) from alternatively activated M2-like
macrophages (Ly6C loCD206hi)34.
Following subcritical injury (2 mm) or critical (3 mm) VML
injury, immune cells were isolated from injured quadriceps
muscles and analyzed at 1, 3, and 7 days post injury via biplot
gating and multi-dimensional immunophenotyping analysis of
ﬂow cytometry data (Fig. 1, bi-plot gating in Supplementary
Fig. 1). Quadriceps explanted from naïve (uninjured) mice were
used as a control. All CD11b + myeloid cells from uninjured and
injured animals at all timepoints (days 1, 3, and 7) were used to
construct a UMAP plot that graphs single cells by their surface
marker pro ﬁles, where further distances between cells indicates
dissimilar cellular phenotypes (Fig. 2). Surface marker expression
values are represented on the UMAP, ranging from dark blue
(low expression) to yellow (high expression) (Fig. 2a). Each
CD11b+ cellular event is represented as a dot on the UMAP, with
those coming from uninjured quadriceps overlaid in green and
those from subcritical injury or critical VML injured quadriceps
overlaid in blue and red, respectively (Fig. 2b).
At day 1, myeloid cells from injured quadriceps qualitatively
localized near the bottom left of the UMAP plot, indicating that
day 1 myeloid cells have low expression of CD206, MerTK, and
CXCR4, chemokine receptor for stromal cell- derived factor 1
(SDF-1), but highly express Ly6C (Fig. 2a, b). In contrast, the
upper right portion of the UMAP is enriched for day 3 and day 7
cells, representing a phenotypic switch to increased CD206,
CD64, MerTK, stem cell antigen-1 (Sca-1), CD29 (integrin β1),
and CXCR4 expression and a lower expression of Ly6C by day 7.
While the overlay of CD11b + events is located similarly in
UMAP space between subcritical injury and critical VML, the
number of events is remarkably different. At days 3 and 7, critical
VML injuries presented with a higher number of myeloid cells
within the UMAP compared to subcritical injuries, suggesting
that in ﬂammation was not completely resolved by day 7.
The increased expression of CD64 and MerTK in the upper
right portion of the UMAP suggests that mononuclear phagocyte
populations are present at days 3 and 7 post injury. Thus, a
UMAP plot comprised of all CD11b
+CD64+MerTK-SSClo
monocytes and CD11b +CD64+MerTK+ macrophages pooled
from all samples across all three timepoints was constructed
(Fig. 3). Expression levels of surface markers characterizing
monocyte and macrophage subsets were overlaid onto UMAP
plots to illustrate the expression pro ﬁle of unique mononuclear
phagocyte subpopulations (Fig. 3a). While the location of overlaid
monocytes and macrophages appear similar between subcritical
injury and critical VML at days 1 and 3, the top middle and far
right sections of the UMAP largely contain day 7 cells from
critical VML (Fig. 3b). Notably, these day 7 critical VML
mononuclear phagocytes are positioned in UMAP space based on
their low expression of Ly6C and high expression of CD206
(Fig. 3a, b). This retention of mononuclear phagocytes may be
explained by the increased secretions of pro-in ﬂammatory
cytokines within the injury niche as indicated by an upwards
trend in TNF- α expressing neutrophils at day 7 in critical VML
(Supplementary Fig. 2).
Monocyte subpopulations facilitate the chronic in ﬂammation
characteristic of critical VML . To overcome the intrinsic chal-
lenge of subjective cell subset identi ﬁcation presented by tradi-
tional methods for analyzing multiparameter single-cell data,
unsupervised SPADE clustering analysis was applied to our ﬂow
cytometry data. SPADE groups the cells into distinct clusters, or
nodes, by similar marker expression and then arranges these
nodes into branching trajectories that infer cellular transitions
through time 35. We constructed a SPADE dendrogram with
CD11b+CD64+MerTK-SSClo monocytes from all samples and all
timepoints (days 1, 3, and 7) after injury, including uninjured
controls. The SPADE dendrogram is color annotated into three
monocyte subpopulations identi ﬁed by the median Ly6C
expression of each node (Supplementary Fig. 3a). A corre-
sponding SPADE node heatmap, where each column correlates to
one SPADE node and rows correlate to surface marker expres-
sion, indicates the distinction of these three unique monocyte
subsets based on Ly6C expression (Fig. 4a, b). From left to right,
the phenotype of the monocyte SPADE nodes transition from
Ly6Chi to Ly6C lo, illustrating the dynamic biological progression
of monocytes after VML.
The concentration of cells within each of the three SPADE-
identiﬁed monocyte subpopulations was quanti ﬁed for all time-
points (Fig. 4c). For all subsets, there was a signi ﬁcant increase in
the number of monocytes present in critical VML at day 3 post
injury. Ly6C int monocytes— which would typically be left out
of traditional gating strategies between the ‘high’ and ‘low’
expressing gates — and Ly6C lo monocytes both reached peak
concentrations at day 3 with Ly6C lo monocytes reaching the
highest concentration of all the subpopulations at any timepoint.
To evaluate the cytokine expression pro ﬁle of these monocyte
subsets, we again performed ﬂow cytometry analysis from
explanted quadriceps at days 3 and 7 after subcritical injury or
critical VML. There were no differences found in the concentra-
tion of TNF- α+ or SDF-1 + monocyte subsets in ﬁltrating
subcritical injury and critical VML at day 3 (Supplementary
COMMUNICATIONS BIOLOGY | https://doi.org/10.1038/s42003-023-04790-6 ARTICLE
COMMUNICATIONS BIOLOGY |           (2023) 6:749 | https://doi.org/10.1038/s42003-023-04790-6 | www.nature.com/commsbio 3

Fig. 2 Persistent myeloid cell response in critical VML injury as visualized by UMAP analysis. UMAP representation comprised of single cell ﬂow
cytometry data from explanted quadriceps muscle at days 1, 3, and 7 post injury in addition to uninjured quadriceps. a UMAP projection overlaid with
marker expression values of each targeted surface protein. Marker expression levels range from dark blue to yellow, representing low to high express ion,
respectively. b CD11b+ cells from uninjured quadriceps overlaid onto UMAP (green). CD11b + cells from quadriceps that received a subcritical injury (blue,
top) and those from quadriceps that received a critically sized VML injury (red, bottom) overlaid onto the UMAP at days 1, 3, and 7 post injury (left to
right). UMAP constructed from n = 4 biologically independent animals per experimental group.
ARTICLE COMMUNICATIONS BIOLOGY | https://doi.org/10.1038/s42003-023-04790-6
4 COMMUNICATIONS BIOLOGY |           (2023) 6:749 | https://doi.org/10.1038/s42003-023-04790-6 | www.nature.com/commsbio

Fig. 3 UMAP analysis reveals accumulation of mononuclear phagocytes in critically sized VML injuries. UMAP generated from ﬂow cytometry gated
CD11b+CD64+MerTK+ macrophages and CD11b+CD64+MerTK-SSClo monocytes extracted from quadriceps tissue (uninjured and at days 1, 3, and 7 post
injury). a UMAP projection overlaid with surface maker expression values. Marker expression levels range from dark blue to yellow, representing low to
high expression, respectively. b Visualization of mononuclear phagocyte in ﬁltration in quadriceps that received no injury (uninjured), subcritical injury
(blue, top) or critically sized injury (red, bottom) at each timepoint post injury (days 1, 3, and 7). UMAP constructed from n = 4 biologically independent
animals per experimental group.
Fig. 4 Unbiased SPADE clustering identi ﬁes distinct monocyte subpopulations that are signi ﬁcantly increased in critically sized injuries 3 days post
VML. SPADE dendrogram generated from all CD11b +CD64+MerTK-SSClo monocytes isolated from quadriceps muscle of mice which were uninjured or
those which received a subcritical injury or critical VML injury (at days 1, 3, and 7 post injury). a Monocyte SPADE dendrogram annotated by nodes
containing monocytes with low (Ly6C lo), intermediate (Ly6Cint), or high (Ly6C hi) expression of Ly6C. b Protein signature of each SPADE node represented
as a heatmap. SPADE nodes classi ﬁed according to their expression of Ly6C. Color annotation of SPADE nodes on the dendrogram align with those on the
heatmap. c Quantiﬁcation of monocyte subsets (per mg of tissue) within quadriceps muscle at each timepoint post injury. Data presented as mean ± S.E.M.
Statistical analyses performed include two-way ANOVA with Sidak multiple comparisons between injury sizes at each timepoint. * p < 0.05, ** p < 0.01.
n = 4 biologically independent animals per experimental group. D1: day 1, D3: day 3, D7: day 7.
COMMUNICATIONS BIOLOGY | https://doi.org/10.1038/s42003-023-04790-6 ARTICLE
COMMUNICATIONS BIOLOGY |           (2023) 6:749 | https://doi.org/10.1038/s42003-023-04790-6 | www.nature.com/commsbio 5

Fig. 3b –d). However, at day 7, the number of Ly6C int monocytes
expressing TNF- α and Ly6C hi monocytes expressing SDF-1 were
signiﬁcantly elevated in critical VML. Almost no monocytes,
regardless of subset classi ﬁcation, expressed TNF- α or SDF-1 in
subcritical injuries at day 7 (Supplementary Fig. 3c, d).
Aberrant macrophage subsets dysregulated following critical
VML injury may contribute to ﬁbrotic VML pathology . All
CD11b+CD64+MerTK+ macrophages, from uninjured and
injured quadriceps (at days 1, 3, and 7 post injury) were used to
generate a SPADE dendrogram (Fig. 5a). SPADE clustered the
macrophages into nodes ordered along 4 marked trajectories,
each color-coded, characterized by the surface marker expression
of each node (Supplementary Fig. 4a, b). Most macrophages
present within the injured muscle at day 1 are clustered within
nodes of the initial M1-like trajectory, characterized by its
Ly6ChiCD206lo expression pro ﬁle. Moving down the dendro-
gram, as indicated by dotted gray arrows, the ordered nodes split
into 3 separate branches: an unpolarized (Ly6C loCD206lo) tra-
jectory, an M2-like (Ly6C loCD206hi) trajectory, and a ‘hybrid’
(Ly6ChiCD206hi) macrophage trajectory (Fig. 5a, Supplementary
Fig. 4a, b). Quantifying the number of macrophages within each
annotated SPADE trajectory, it was found that there were no
changes in the concentrations of M1-like or unpolarized macro-
phages between injury sizes at any timepoint. By contrast, both
M2-like macrophages and hybrid macrophages were signi ﬁcantly
elevated at 7 days post injury (Fig. 5b). Our data shows that
CXCR4 expression elevates concurrently with CD206 for both
M2-like and hybrid macrophage subtypes (Supplementary
Fig. 4a). Thus, the dual expression of CD206 and CXCR4 may
deﬁne speci ﬁc macrophage subsets with a sustained and dysre-
gulated response following critical VML.
While most studies have characterized the role of M2-like
macrophages in establishing an anti-in ﬂammatory microenviron-
ment and promotion of tissue regeneration, in the presence of
chronic in ﬂammatory stimuli, M2-like macrophages are known
to secrete large amounts of pro- ﬁbrotic cytokines and promote
tissue and organ ﬁbrosis36. To examine the intracellular cytokine
proﬁle of the signi ﬁcantly elevated M2-like macrophages in
critical VML, ﬂow cytometry analysis was performed at days 3
and 7 post subcritical injury and critical VML. A SPADE
dendrogram was constructed of all CD11b +CD64+MerTK+
macrophage events from both timepoints and injury sizes, and
nodes were grouped into the same four phenotype subtypes (M1-
like, M2-like, unpolarized, and hybrid) based on expression of
Ly6C and CD206 (Fig. 6a, Supplementary Fig. 4c).
Within the M2-like macrophage subset, nodes were subse-
quently annotated based on expression of intracellular TNF- α and
TGF-β. The M2-like macrophage trajectory segregated based on
the expression pro ﬁles of these particular cytokines, indicating a
divergence in M2-like macrophage phenotype progression as a
function of injury severity. M2-like macrophage SPADE nodes
that expressed both TNF- α and TGF- β were annotated as solid
green whereas nodes that did not express either cytokine were
annotated with only a green outline (Fig. 6b, Supplementary
Fig. 4c). All nodes either expressed both or neither of the two
cytokines, as there were no TNF- α
+TGF-β- or TNF- α-TGF-β+
expressing M2-like nodes. At day 3 post injury, there were no
differences in the concentrations of TNF- α+TGF-β+ or TNF- α-
TGF-β- M2-like macrophages between injury sizes. At day 7, very
few M2-like macrophages remain in subcritical defects, but there
is a clear retention of M2-like macrophages in critical VML
injured quadriceps- the majority of them expressing both TNF- α
and TGF- β (represented as green segment of stacked bar graph)
Fig. 5 SPADE identi ﬁcation of macrophage subsets uncovers two unique populations expressing CD206 which are signi ﬁcantly increased in critical
VML injuries at day 7. SPADE dendrogram generated from all CD11b +CD64+MerTK+ macrophages isolated from quadriceps muscle of mice which were
uninjured or those which received a subcritical injury or critically sized VML injury (at days 1, 3, and 7 post injury). a Macrophage SPADE dendrogram
annotated based on CD206 and Ly6C expression to designate nodes to a M1-like, M2-like, unpolarized, or hybrid macrophage phenotype. Gray arrow
indicates general movement over time following injury. b Quantiﬁcation of macrophage subsets (per mg of tissue) within quadriceps muscle at each
timepoint post injury. Dashed gray line represents average value for uninjured controls. Data presented as mean ± S.E.M. Statistical analyses perfo rmed
include two-way ANOVA with Sidak test for multiple comparisons between injury sizes at each timepoint. ** p < 0.01. n = 4 biologically independent
animals per experimental group. D1: day 1, D3: day 3, D7: day 7, M φ: macrophage.
ARTICLE COMMUNICATIONS BIOLOGY | https://doi.org/10.1038/s42003-023-04790-6
6 COMMUNICATIONS BIOLOGY |           (2023) 6:749 | https://doi.org/10.1038/s42003-023-04790-6 | www.nature.com/commsbio

(Fig. 6c). To further probe this unique secretome, we harnessed
multiplexed cytokine analysis to resolve functional heterogene-
ities of M2-like macrophages as a response to subcritical injury or
critical VML. Sorted M2-like macrophages from critical VML had
over a two-fold elevation in total cytokine production compared
to subcritical injury. Interestingly, regulatory cytokines (IL4,
IL10) speci ﬁcally were signi ﬁcantly increased in critical VML, as
they were undetected in subcritical injuries at the day 7 timepoint
(Fig. 6d).
Uninjured, subcritical injury, and critical VML quadriceps
cross-sections were used for immunohistochemical (IHC)
analysis at 7 days post injury (Fig. 7) to visually assess the
sustained presence of M2-like macrophages within the defect.
Cross-sections were stained with dystrophin (white), DAPI
(blue), CD68 (red) and CD206 (green), and M2-like macrophages
were identiﬁed as CD68
+CD206+DAPI+ (merged to yellow) cells
within the muscle tissue. Uninjured control quadriceps showed
healthy skeletal muscle morphology with DAPI + myonuclei
located at the periphery and little to no M2-like macrophages
(Fig. 7a, d, g). Quadriceps that received subcritical injuries
presented with visible DAPI + cellular in ﬁltration at day 7, some
of which were identi ﬁed as M2-like macrophages (Fig. 7b, e, pink
arrows). The morphology of myo ﬁbers adjacent to the defect
space appear largely unaffected. (Fig. 7b). In contrast, there was a
Fig. 6 M2-like macrophages from critical VML defects have aberrant cytokine production pro ﬁle that may contribute to pathological ﬁbrosis. a– c Flow
cytometry was performed on single cells isolated from quadriceps of mice that received a subcritical injury or critical VML injury at days 3 and 7 post i njury.
CD11b+CD64+MerTK+ macrophages pooled from all samples from both injury sizes and both timepoints were used to construct a SPADE dendrogram.
a Macrophage SPADE dendrogram annotated based on CD206 and Ly6C expression to designate nodes to a M1-like, M2-like, unpolarized, or hybrid
macrophage phenotype. b M2-like macrophages (green annotation) distinguished by their intracellular expression of TNF- α and TGF-β (TNF-α+ TGF-β+
nodes: solid green; TNF- α- TGF-β- nodes: green outline). c Number of TNF- α+ TGF-β+ and TNF- α- TGF-β- M2-like macrophages per mg of tissue
represented as a stacked bar graph at day 3 and day 7 post subcritical injury or critical VML. d Concentration of cytokines (categorized into 5 classes) from
lysate of FACS sorted M2-like macrophages at day 7 post subcritical injury and critical VML as measured by Isoplexis. Data presented as mean ± S.E.M.
Statistical analysis included repeated measures two-way ANOVA with Sidak test between injury sizes per cytokine class. * p < 0.05 for regulatory cytokines
between injury size. n = 3– 4( a– c)o r4 d biologically independent animals per experimental group. M φ: macrophage.
COMMUNICATIONS BIOLOGY | https://doi.org/10.1038/s42003-023-04790-6 ARTICLE
COMMUNICATIONS BIOLOGY |           (2023) 6:749 | https://doi.org/10.1038/s42003-023-04790-6 | www.nature.com/commsbio 7

signiﬁcant increase in the in ﬁltration and persistence of M2-like
macrophages within the defect area of critically injured quad-
riceps (Fig. 7c, f, g, pink arrows) compared to both subcritical
injury and uninjured tissue. There is an obvious ablation of tissue
structure with necrotic myo ﬁbers spaced apart, distorted in their
morphology, and with clusters of mononuclear cells surrounding
them (Fig. 7c, f).
To explore whether retained M2-like macrophages with
divergent cytokine pro ﬁles from critical VML are taking part in
ﬁbrotic signaling with FAPs, we performed second harmonic
generation imaging on quadriceps sections stained for M2-like
macrophages (CD206, red) and FAPs (PDGFRα, red) with collagen
deposition illustrated in blue (Fig. 7h–j). Uninjured tissue
presented with very little M2-like macrophages or FAPs localized
near collagen (Fig. 7h). Critical VML resulted in signi ﬁcantly
increased numbers of M2-like macrophages and FAPs per collagen
within the injury site compared to uninjured tissue, whereas no
differences were observed between uninjured and subcritical injury
(Fig. 7k). Importantly, M2-like macrophages and FAPs co-localize
in regions of collagen deposition in critical VML, but this was not
often observed in subcritical defects (Fig. 7i, j).
Chronic in ﬂammatory stimuli from critical VML propagates
unchecked T cell activation and recruitment to injury milieu .
All CD3
+ T cells from all animals and at all timepoints (days 1, 3,
and 7; bi-plot gating strategy of T cells in Supplementary Fig. 5)
were used to construct a UMAP plot to visualize T cell in ﬁltration
and phenotype transitions in a lower dimensional space (Fig. 8).
Relative expression levels of each measured T cell surface marker
were overlaid onto the UMAP to illustrate the locations of
Fig. 7 Retained M2-like macrophages in critical VML co-localize with FAPs in defect areas of marked collagen deposition. a – f Representative IHC
images of quadriceps cross-sections from uninjured ( a, d), subcritical injury ( b, e), and critical VML ( c, f) at 7 days post injury. Cross-sections stained for
dystrophin (white), CD68 (red), CD206 (green), and DAPI (blue). Dotted pink boxes in a– c represent ROI regions presented in d– f where pink arrows
indicate CD68+CD206+DAPI+ M2-like macrophages (yellow). g Quantiﬁed number of M2-like macrophages from each injury group at day 7 timepoint.
h– j SHG imaging of representative day 7 cross-sections from uninjured ( h), subcritical injury ( i), and critical VML ( j) quadriceps. Cross-sections stained for
CD206 (red; M2-like macrophages) and PDGFR α (green; FAPs) with detected SHG signal (blue; collagen). k Number of M2-like macrophages (light gray)
and FAPs (dark gray) per detected collagen signal within defect area imaged. Scale bars represent 100 µm( a– c), 50 µm( d– f), and 10 µm( h– j). Data
presented as mean ± S.E.M. Statistical analyses performed include one-way ANOVA and repeated measures two-way ANOVA with Holm-Sidak test or
Fisher’s LSD test, respectively. * p < 0.05 for number of M2-like macrophages per collagen, # p < 0.05 for number of FAPs per collagen. n = 3 biologically
independent animals per group. IHC: immunohistochemistry; SHG: second harmonic generation; PDGFR α: platelet derived growth factor receptor alpha;
FAPs: ﬁbroadipogenic progenitors.
ARTICLE COMMUNICATIONS BIOLOGY | https://doi.org/10.1038/s42003-023-04790-6
8 COMMUNICATIONS BIOLOGY |           (2023) 6:749 | https://doi.org/10.1038/s42003-023-04790-6 | www.nature.com/commsbio

heterogeneous T cell subpopulations within the UMAP space
(Fig. 8a). The few T cells present in uninjured quadriceps were
overlaid in green on the UMAP while T cells from subcritical
injured quadriceps are overlaid in blue, and T cells from critical
VML quadriceps are overlaid in red, by timepoint (Fig. 8b). The
location of overlaid T cells from different biological samples
provides a visual representation of T cell subtype dynamics fol-
lowing subcritical injury and critical VML.
Temporal dynamics of T cells were observed through the
UMAP, as the left and right side of the UMAP projection is
enriched for day 1 or day 7 T cells, respectively (Fig. 8b). T cells
from subcritical injury and critical VML share similar surface
marker dynamics, indicated by their similar location within the
UMAP at each timepoint. At day 1, it appears that T cells have a
low expression of CD4, expressed by helper T cells, and IL-7
receptor, CD127. Yet by day 3, there is a clear shift in phenotype
as T cells localize in areas of high CD4 and CD127 expression,
with T reg marker CD25 and cytotoxic T cell marker CD8
remaining relatively constant with time (Fig. 8a, b). Importantly,
increased T cell numbers from critical VML at days 3 and 7 post
injury can be qualitatively observed in the UMAPs relative to
subcritical injury (Fig. 8b) which may indicate hyperactivation of
the adaptive immune response.
To characterize and quantify unique subsets of T cells within
subcritical injury and critical VML, all CD3 + T cells from all
animals and timepoints were used to generate a SPADE
dendrogram (Fig. 9a). SPADE clustering of T cell events by their
surface marker expression pro ﬁle (Fig. 9b) also revealed a clear
localization of T cells by timepoint indicating the phenotypic
transition that occurs within the ﬁrst week following injury. The
nodes were grouped into 3 time-associated clusters: the initial T cell
response (annotated light gray), transition T cells (annotated dark
gray), and ﬁnal T cell fates (annotated black) (Fig. 9a) as indicated
by relative cell frequencies overlaid onto each SPADE node by
timepoint (Supplementary Fig. 6a). The percentage of total T cells
within each of these time-associated clusters was quanti ﬁed
(Supplementary Fig. 6b –d). The percentage of total T cells from
day 1 samples in the initial T cell response population was
signiﬁcantly higher than the percentage of T cells from 3 and 7 days
post injury, and the percentage of day 7 T cells is signiﬁcantly lower
than those at day 3 (Supplementary Fig. 6b). This result veriﬁes that
the left side of the SPADE dendrogram (light gray annotation) is
comprised predominately of day 1 T cells. Within the transitional T
cell population, representing a group of T cells that are not yet in
their ‘ﬁnal’phenotype state, the percentage of T cells from days 3
and 7 were signi ﬁcantly higher than those from day 1
(Supplementary Fig. 6c). In ﬁnal T cell fate nodes (far right of
dendrogram), the percentage of T cells at day 7 were signi ﬁcantly
elevated compared to the percentage at days 1 and 3 (Supplemen-
tary Fig. 6d). These ﬁndings conﬁrm that the clustering of T cells
via surface marker expression coincides with the progression of
time (Fig. 9a, indicated with dashed black arrow). No differences
were observed in the percentage of T cells between subcritical
injury and critical VML at any time point within these time-
associated node clusters.
Within each of the three time-associated node clusters, speciﬁcT
cell subtypes of interest were identi ﬁed by their unique marker
expression proﬁle as shown at each SPADE node in the form of a
heatmap (Fig. 9b) or overlaid onto each node in the dendrogram
(Supplementary Fig. 7). The SPADE nodes of the heatmap are
organized from left to right in the same progression as the
dendrogram. Within the greater ‘initial T cell response ’grouping,
inactivated T cells were characterized by their low expression of all
measured markers in addition to low forward scatter area (FSC)
and side scatter area (SSC), which indicate small relative cell size
and low intracellular granularity, respectively. The cells present in
these nodes were quanti ﬁed and it was found that there were
signiﬁcantly more inactivated T cells in critical VML at 3 days post
injury compared to subcritical injuries (Fig. 9c). Nodes containing
CD8+ cytotoxic T cells were identi ﬁed by their high expression of
CD8 but low expression of all other surface markers, FSC, and SSC
(Fig. 9b). CD8+ cytotoxic T cells were signiﬁcantly elevated at day 3
following critical VML injury (Fig. 9c).
As the dendrogram progresses into transition and ﬁnal T cell
fate stages, it is observed that cell size and intracellular granularity
is increased as measured by FSC and SSC (Fig. 9b). A
subpopulation of transitional T cells positive for all measured
surface markers was identi ﬁed. These ‘all-positive T cells ’ were
Fig. 8 Critical VML injury presents with increased T cell recruitment 3 days post injury as visualized by UMAP. CD3+ T cells pooled from all quadricep
samples (uninjured, subcritical injury, and critical VML) and all timepoints (days 1, 3, and 7) were used to generate a UMAP projection. a Expression levels
of T cell surface markers overlaid onto UMAP. Marker expression levels range from dark blue to yellow, representing low to high expression, respectiv ely.
b CD3+ T cells isolated from uninjured quadriceps (green), subcritical injuries (blue, top), and critically sized injuries (red, bottom) at each timepoin t.
UMAP constructed from n = 4 biologically independent animals per experimental group.
COMMUNICATIONS BIOLOGY | https://doi.org/10.1038/s42003-023-04790-6 ARTICLE
COMMUNICATIONS BIOLOGY |           (2023) 6:749 | https://doi.org/10.1038/s42003-023-04790-6 | www.nature.com/commsbio 9

present within critically injured muscle at signi ﬁcantly higher
concentrations at days 3 and 7 (Fig. 9b, c). Two subsets of interest
were identi ﬁed within the ﬁnal fate T cells comprised chie ﬂyo f
T cells from day 7. One of these subsets highly expressed both
CD4 and CD127 (Fig. 9b, dark blue annotation). These
CD127 + helper T cells were signi ﬁcantly increased at days 3
and 7 after critical VML (Fig. 9c). Finally, a group of nodes
containing CD127 + Treg cells (CD4 +CD25+) were identi ﬁed
within the greater ﬁnal fates T cells clustering. This T reg subset
presented with low expression of CD8 and was also signi ﬁcantly
elevated at days 3 and 7 post injury in critical VML (Fig. 9b, c).
Taken together, SPADE analysis was able to reconstruct the
phenotypic transitions of T cell populations occurring through
time and facilitated robust characterization and quanti ﬁcation of
speciﬁc T cell subsets to reveal a dysregulated T cell response
occurring at day 3 and 7 in critical VML.
Discussion
The proper coordination of immune cells is crucial for prompt and
proper regeneration and repair of damaged muscle following minor
muscle injuries. Although skeletal muscle possesses remarkable
regenerative capabilities, the traumatic loss of muscle characteristic
of VML ablates the extracellular matrix and MuSC niche necessary
for the initiation of myogenesis; thus, muscle ’s innate capacity for
regeneration becomes inadequate to functionally recover muscle37.
In this series of studies, our data reveals key differences in the
concentrations and temporal dynamics of identi ﬁed immune cell
subsets present within injured muscle following subcritical injury
and critical VML. Subcritical injuries elicited an immune response
similar to what is expected from an acute muscle injury, as most of
the inﬂammation had been resolved by day 7. In contrast, critical
VML presented with a sustained elevation of several unique mye-
loid and lymphoid cell subsets as characterized by UMAP and
SPADE pseudo-time analysis. These results were summarized in
Supplementary Fig. 8, where the average concentration data for
each subtype and injury size were plotted to demonstrate the
altered immune response to critical VML.
While single cell resolution by ﬂow cytometry analysis provides
a powerful tool for temporal evaluation of the immune response,
increased dimensionality obscures the underlying heterogeneity
of the data and increases the likelihood of introducing user bias
when identifying cell populations
38. Further, bi-plots only display
Fig. 9 Pseudotime analysis reveals a dysregulated T cell response to critical VML injury. a Pre-gated CD3 + T cells from all samples (uninjured,
subcritical injury, and critical VML) and all timepoints (days 1, 3, and 7) were used to construct a SPADE dendrogram. SPADE nodes annotated by relativ e
percentage of T cells present from each timepoint. Gray arrow indicates time response of T cells with day 1 T-cells primarily occupying left side of
dendrogram (light gray) and day 7 T cells primarily occupying nodes on right side of dendrogram (black). b Protein signature of each SPADE node
represented as a heatmap. SPADE nodes grouped by temporal in ﬁltration kinetics (initial T cells, transition T cells, or ﬁnal T cell fates) and further
annotated by FSC, SSC, and surface marker expression pro ﬁles. c T cell subtype cell counts quanti ﬁed as cell concentration (cells/mg tissue). Quanti ﬁed
subtypes identiﬁed and annotated in b. Data presented as mean ± S.E.M. Statistical analyses performed on log transformed data with two-way ANOVA and
Sidak multiple comparisons to determine differences between injury sizes. * p < 0.05, **p < 0.01, ****p < 0.0001, n = 4 biologically independent animals per
experimental group. D1: day 1, D3: day 3, D7: day 7.
ARTICLE COMMUNICATIONS BIOLOGY | https://doi.org/10.1038/s42003-023-04790-6
10 COMMUNICATIONS BIOLOGY |           (2023) 6:749 | https://doi.org/10.1038/s42003-023-04790-6 | www.nature.com/commsbio

correlations between two markers at a time, and it is dif ﬁcult to
fully characterize high-dimensional data with a series of two-
dimensional visualizations. We harnessed the unbiased dimen-
sionality reduction methods, UMAP and SPADE, to overcome
these limitations and analyze the temporal progression of
immune cells present in injured muscle dependent on injury size.
We observed that critical VML injury showed increased CD11b
+
cell retention in injured muscle at day 7 and a transient increase
in MerTK, CXCR4 and CD206 expression. We found that in
particular, mononuclear phagocytes elicited a prolonged immune
response in critical VML, including a speci ﬁc CD206
hiLy6Clo
subset that was not present in subcritical injuries by day 7, a
ﬁnding that would not be easily discovered without imple-
mentation of advanced, dimensionality reduction visualization
techniques.
We hypothesized that the sustained presence of mononuclear
phagocytes within critical VML injuries may lead to the persis-
tence of pro-in ﬂammatory cytokines such as TNF- α and SDF-1.
There was a signi ﬁcant increase in all identi ﬁed monocyte subsets
at day 3 post injury, suggesting an increased extravasation of
monocytes from circulation to larger injuries. We found that at
day 7 post injury, the concentrations of TNF- α+ neutrophils in
addition to TNF- α+ and SDF-1 + monocytes were signi ﬁcantly
elevated in critical VML but little to none were present in sub-
critical injuries. These results may indicate that early accumula-
tion of pro-in ﬂammatory myeloid cells in critical VML
propagates the secretions of potent leukocyte chemo-attractants
such as TNF- α and SDF-1, leading to immune cell retention at
day 7 onwards. In an environment rich in cytokines such as TNF-
α and IFN- γ, it is likely that MuSCs may ef ﬁciently activate and
proliferate but fail to differentiate into myotubes as a result of a
failed in ﬂammatory-to-regenerative transition; 1,4 thus, myogen-
esis is impaired and ﬁbrotic and fatty in ﬁltration ﬁll the defect
rather than functional muscle.
In minor injuries, elevation of M2-like macrophages and their
progenitors, non-classical Ly6Clo monocytes, has been linked with
improved muscle healing 10,39. However, our results indicate an
abnormal persistence of M2-like macrophages in critical VML at
day 7. Taking advantage of the unique capability of SPADE to
preserve rare cell types often masked in bulk cellular analysis, we
discovered a population of hybrid CD206 and Ly6C co-expressing
macrophages which were also signi ﬁcantly increased in critical
VML. We found that both of these CD206 hi macrophage subsets
have concurrent elevations in CXCR4 expression which has been
reported to be linked to ﬁbrosis, in part through their expression
and secretion of tissue inhibitor of metalloprotease 1 (TIMP1)40.I t
is notable that CXCR4 is elevated in M2s, as they are known to
secrete pro-ﬁbrotic cytokines such as TGF- β. It is also of interest
that CXCR4 is highly expressed in hybrid macrophages, suggesting
a potential role for CD206 hiLy6Chi macrophages in ﬁbrosis.
Previous studies have shown that macrophages simultaneously
expressing pro- and anti-in ﬂammatory cytokines may result from
impaired M1-to-M2 phenotypic transitions and contribute to
chronic in ﬂammation and subsequent tissue ﬁbrosis6,41,42.W e
sought to further characterize the cytokine pro ﬁle of the M2-like
macrophages persisting in critical VML and found that the
majority of M2-like macrophages present at day 7 co-expressed
TNF-α and TGF-β, as identi ﬁed via SPADE clustering analysis. It
has been shown that when macrophages co-express these cyto-
kines, TGF- β dominates the response and leads to unregulated
ECM deposition by FAPs to facilitate tissue ﬁbrosis6. The
hypothesis that aberrant M2-like macrophages induced by VML
propagate pro- ﬁbrotic signaling with FAPs is further evidenced
by their increased co-localization with collagen in the injury
milieu as captured by SHG imaging. Multiplexed cytokine ana-
lysis from sorted M2-like macrophages revealed signi ﬁcantly
increased concentrations of IL-10 and IL-4 in critical VML
relative to subcritical injury. While IL-10 is often considered a
canonical anti-in ﬂammatory cytokine, it has been found that
over-exposure to IL-10 induced ﬁbrocyte recruitment and exa-
cerbated lung ﬁbrosis;43 thus, its excess production in VML may
exacerbate dysregulated ECM deposition. In our murine model,
critical VML injured quadriceps resulted in increased vascular
volume compared to uninjured tissue 24, and M2-like macro-
phages have known roles for promoting angiogenesis in patho-
logical conditions 44. It is an interesting hypothesis that M2-like
macrophages may be driving both the increased ﬁbrotic and
angiogenic response in VML, as ﬁbroplasia and angiogenesis are
known to be co-dependent processes in injury repair 45. Future
studies are necessary to elucidate the mechanisms by which M2-
like macrophages regulate pro- ﬁbrotic and pro-angiogenic
responses within the injury milieu of VML.
T cells are known to play important roles in aiding macrophage
trafﬁcking and polarization during muscle healing 14,17. Further,
as phagocytic macrophages populate the injury, they present
antigens on their cell surface and secrete cytokines responsible for
activating T cells and the adaptive immune response 46. We found
that overall T cell numbers peaked around day 3 post injury, as
would be expected 14. Despite seemingly appropriate dynamics,
we found that there were several subsets of T cells that presented
with an altered response to critical VML at days 3 and 7 com-
pared to subcritical injuries.
We qualitatively observed an increase in T cell size over time,
represented by FSC, which indicates antigenic stimulation and T
cell activation 47. CD8 + cytotoxic T cells were increased at day 3
and a population of T cells highly expressing all measured mar-
kers was signi ﬁcantly elevated in critical VML at days 3 and 7,
indicating increased T cell activation induced by larger injury
size. CD4 +CD8+ T cells have been shown to be highly cytotoxic
which may lead to intensi ﬁed tissue damage 48, but further
investigation is necessary to determine if these double-positive
T cells are detrimental to muscle regeneration. Lastly, we iden-
tiﬁed two T cell populations expressing IL-7 receptor, CD127:
CD127+CD4+ helper T cells and CD127 +CD4+CD25+ Treg cells.
As CD127 has been reported to be expressed on activated T reg
cells in the presence of IL-7 49, our results may be indicative of
elevated IL-7 in our critical VML model. IL-7 has been found to
reduce myoblast differentiation and fusion 50, so future studies
measuring whether increased IL-7 induced by critical VML
upregulates CD127 + T cells and impedes myogenesis is of
interest. While signi ﬁcant increases in T reg cells after critical VML
was not expected, it is possible that despite a local enrichment of
Treg cells, their immunosuppressive function is reduced in
the presence of chronic in ﬂammatory stimuli51. T cell exhaustion,
a state of T cell dysregulation due to chronic antigen
presentation52, could be impairing the role of T reg cells to mediate
myoblast differentiation during muscle regeneration. Often stu-
died in the context of cancer and long-term infections, future
studies evaluating the extent of T cell exhaustion occurring in
severe trauma injuries such as VML would be greatly bene ﬁcial.
We have previously reported that 3 mm full thickness defects
in the murine quadriceps VML model results in ﬁbrosis, fatty
inﬁltration, and lack of myo ﬁber regeneration within the injury
site- similar to the clinical scenario 24. Here, we elucidate key
immune cellular players that underlie this pathophysiology.
Leveraging dimensionality reduction and clustering techniques to
visualize the correlation of multiple measured markers across cell
types was crucial to identifying altered cellular transitions at early
timepoints after VML. However, these ﬁndings do not preclude
that these SPADE-identi ﬁed subsets could not be identi ﬁed using
more conventional strategies. One limitation to this series of
studies is only assessing immune cell in ﬁltration kinetics during
COMMUNICATIONS BIOLOGY | https://doi.org/10.1038/s42003-023-04790-6 ARTICLE
COMMUNICATIONS BIOLOGY |           (2023) 6:749 | https://doi.org/10.1038/s42003-023-04790-6 | www.nature.com/commsbio 11

the ﬁrst week after injury. Uncovering cellular progressions
thereafter and determining whether VML injured muscle reaches
a veriﬁable state of resolution at a later timepoint will be a subject
of future work. Revealing speci ﬁc immune cell subtypes dysre-
gulated in critical VML, particularly those with heterogeneous
and progressive phenotypes, is an important approach to exam-
ining failed endogenous repair mechanisms at the cellular and
molecular level. These studies may provide the necessary foun-
dation for the development of targeted regenerative immu-
notherapies to improve clinical outcomes following VML.
Methods
Animals. C57BL/6 J mice were purchased from Jackson Laboratory and main-
tained as a breeding colony. All animals used in the study were male, 6.1 ± 0.5
(mean ± standard deviation) months in age at the time of euthanasia. A total of 60
mice were utilized for the presented series of studies.
Quadriceps volumetric muscle loss injury . Surgical procedure performed as
previously reported
24. Brieﬂy, the left hindlimb was prepped and sterilized. A single
incision was made above the quadriceps and a 2 mm or 3 mm biopsy punch (VWR,
21909-132, -136) was used to make a full-thickness muscle defect. Skin was closed
with wound clips and muscle was left to recover without intervention for 1, 3, or
7 days before euthanasia by CO
2 inhalation. Naïve mice were utilized for uninjured
control quadriceps. For all animals (injured mice or uninjured naïve mice), the left
quadriceps muscle was dissected and analyzed.
Tissue harvest and ﬂow cytometry . Quadriceps were prepared for ﬂow cyto-
metry analysis on a FACS AriaIII ﬂow cytometer (BD Biosciences) as previously
reported34. Brie ﬂy, entire injured (or uninjured for controls), left quadriceps were
harvested and digested with 5,500U/ml collagenase II and 2.5U/ml Dispase II for
1.5 h in a shaking 37 °C water bath. The digested muscles were ﬁltered through a
cell strainer to obtain a single cell suspension. Single-cell suspensions were stained
for live cells using Zombie NIR (BioLegend, 1:100 dilution) dyes in cell-culture
grade PBS per manufacturer instructions. Cells were then ﬁxed in 4% PFA for
10 min at 4 °C. Cells were stained with cell phenotyping antibodies in a 1:1 volume
ratio of 3% FBS and Brilliant Stain Buffer (BD Biosciences) according to standard
procedures. The following antibodies were used in the T cell phenotyping panel:
BV605-conjugated anti-CD4 (BioLegend), BV785-conjugated anti-CD8 (BioLe-
gend), BV421-conjugated anti-CD3 ε (BioLegend), PerCP-Cy5.5-conjugated anti-
CD25 (BioLegend), and APC-conjugated anti-CD127 (BioLegend). The following
antibodies were used for myeloid cell phenotyping: BV421 or PE-Cy5-conjugated
anti-CD11b (BioLegend), APC-Cy7-conjugated anti-Ly6G, BV510 or PerCP-
Cy5.5-conjugated anti-Ly6C (BioLegend), BV711 or FITC-conjugated anti-CD64
(BioLegend), PE or APC-conjugated anti-MerTK (BioLegend), PE-Cy7 conjugated
anti-CD206 (BioLegend), FITC-conjugated anti-Ly6A/E (BioLegend), APC-
conjugated Lineage antibody cocktail (BD Pharmigen), APC-conjugated anti-CD31
(BioLegend), PE-Cy5 conjugated anti-CD29 (BioLegend), and PerCP-Cy5.5-con-
jugated anti-CXCR4 (BioLegend). The following intracellular antibodies were used
in ﬂow cytometry experiments when indicated: BV510-conjugated anti-TNF- α
(BioLegend), BV421-conjugated anti-TGF- β (BioLegend), and PE-conjugated anti-
SDF-1 (R&D Systems). 30 μL of CountBright Absolute Counting Beads (C36950,
Invitrogen) were added per sample for absolute quanti ﬁcation of cell populations.
All ﬂow cytometry antibodies were used at a concentration of 0.25 or 0.5 µg per
100uL staining volume, in accordance with manufacturer recommendation.
Immunophenotyping of myeloid and lymphoid cell subsets . Single, live cells
were selected in FlowJo software for subsequent immunophenotyping analysis.
Myeloid cells were identi ﬁed as CD11b
+ cells while T cell populations were
identiﬁed as CD3 +. Neutrophils were selected as CD11b +Ly6G+ cells. Monocytes
were gated as CD11b +CD64+MerTK-SSClo cells and macrophages as
CD11b+CD64+MerTK+ cells. Subsets of monocytes, macrophages, and T cells
were further analyzed using SPADE analysis, as described. Conventional bi-plot
gating strategies provided for all myeloid and lymphoid cell types and sub-
populations (Supplementary Figs. 1 –3, 5). A total of 28 quadriceps were used for
myeloid and lymphoid immunophenotyping of uninjured and injured quadriceps
at days 1, 3, and 7 post injury ( n = 4 per experimental group). A total of 15
quadriceps were used for intracellular ﬂow cytometry experiments performed at
days 3 and 7 post injury ( n = 3, 4 per experimental group).
Uniform Manifold Approximation and Projection (UMAP) . UMAPs generated
as previously reported
27,34,53. Brieﬂy, UMAP was used to embed high-dimensional
ﬂow cytometry data into a space of two dimensions, cells are visualized in a scatter
plot where similarity is demonstrated via proximity to other points. Prior to UMAP
dimensional reduction, each ﬂow cytometry sample ( n = 4 per experimental group)
was pre-gated to select cellular subsets of interest (i.e. CD11b
+ myeloid cells and
CD3+ T cells) and then imported into Python 3.7 using fcsparser ( https://github.
com/eyurtsev/fcsparser) and Pandas 2.5. Each channel except for FSC and SSC was
normalized by applying arcsinh/150. UMAP parameters of n_neighbors = 15 and
min_dist = 0.1 were applied for compliance with UMAP assumptions. A composite
UMAP projection that utilized data points from all desired samples was generated
using Matplotlib. Cells from speci ﬁc biological samples or timepoints were visua-
lized by overlaying onto the generated UMAP projection which combined all
samples and timepoints ( https://github.com/lmcinnes/umap).
Spanning-tree Progression Analysis of Density-normalized Events (SPADE) .
SPADE trees generated as previously reported 27,34,53. Brie ﬂy, SPADE was per-
formed through MATLAB and the source code is available at http://pengqiu.
gatech.edu/software/SPADE/. MATLAB-based SPADE automatically generates the
tree by performing density-dependent down-sampling, agglomerative clustering,
linking clusters with a minimum spanning-tree algorithm and up-sampling based
on user input. The SPADE tree was generated by exporting uncompensated pre-
gated live, single cells or select pre-gated cellular subsets (i.e. CD3
+ T cells). The
following SPADE parameters were used: Apply compensation matrix in FCS
header, Arcsinh transformation with cofactor 150, neighborhood size 5, local
density approximation factor 1.5, max allowable cells in pooled downsampled data
50000, target density 20000 cells remaining, and number of desired clusters 50-100,
depending on cell population size.
SPADE node heatmap . SPADE dendrogram heatmaps were constructed with
calculated z-scores of ﬂuorescence intensities for each measured surface marker
across all nodes of a SPADE dendrogram. Each row of the heatmap corresponds to
a surface marker and each column represents a single SPADE node. Marker
expression levels range from dark blue to dark red, indicating low to high
expression, respectively.
Isoplexis cytokine secretome analysis . Quadriceps tissue from subcritical injury
and critical VML injury were explanted at day 7 timepoint. Single cells were isolated
and prepared for ﬂow cytometry analysis as reported in “Tissue harvest and ﬂow
cytometry.” Single-cell suspensions were stained with the following antibodies:
Zombie Red (1:100 dilution), APC-Cy7 conjugated anti-CD11b, FITC conjugated
anti-CD64, APC conjugated anti- MerTK, PE-Cy7 conjugated anti-CD206, and
PerCP-Cy5.5 conjugated anti-Ly6C. Single, live, CD11b
+CD64+MerTK+
CD206hiLy6Clo M2-like macrophages were sorted on a FACS Aria IIIu ﬂow cyt-
ometer (BD Biosciences). Sorted cells were prepared for multiplexed Isoplexis ana-
lysis as previously reported
54. Brieﬂy, 10,000 sorted M2-like macrophages from each
animal (n = 4 per experimental group; 8 quadriceps total) were lysed using non-
denaturing lysis buffer and centrifuged at 14,000xg for 10 min. Supernatant was
collected and loaded into CodePlex chip according to manufacturer instructions.
Lysis buffer was used for background measurements. Codeplex chips were inserted
into IsoLight instrument to measure cytokine pro ﬁle of each sample for all targeted
cytokines (Isoplexis, CodePlex Mouse Adaptive Immune Panel). IsoSpeak software
was used for automated quantitative measurements. Cytokines grouped by classes:
Regulatory (IL-10, IL-4), Effector (IFN- γ, MIP-1a, TNF- α), Chemoattractive (IP-10,
KC, RANTES), Stimulatory (GM-CSF, IL-12, IL-2, IL-5), Inﬂammatory (IL-17A, IL-
1b, IL-6, MCP-1).
Quadriceps tissue histology and immunostaining . Tissue processing and his-
tology done as previously reported
24. Brie ﬂy, muscle was dissected, weighed, and
snap frozen in liquid nitrogen cooled isopentane. 10 µm cryosections (CryoStar
NX70 Cryostat) were taken throughout the defect region. Samples were blocked
and permeabilized before staining with anti-dystrophin (Abcam, ab15277, 1:200)
and anti-CD68 (Abcam, ab53444, 1:150), diluted in blocking buffer, for 1-h
incubation at room temperature. Secondary antibodies conjugated to Alexa Fluor
647 (Invitrogen, A21245, 1:250), Alexa Fluor 555 (Abcam, ab150158, 1:250), and
Alexa Fluor 488- conjugated CD206 (BioLegend, 141710, 1:150) were incubated for
30 min at room temperature. Slides were mounted with Fluoroshield Mounting
Medium with DAPI (Abcam, ab104139) and stored at 4 °C. Primary antibody anti-
PDGFRα (Cell Signaling Technology, 3174, 1:200) was used for immunostaining
samples prior to SHG imaging followed by staining with secondary antibody
conjugated to Alexa Fluor 421 (Abcam, ab175652, 1:250) and Alexa Fluor 488-
conjugated CD206 (BioLegend, 141710, 1:150). Slides prepared for SHG were
mounted with PerMount Mounting Medium (VWR, 100496) and stored at 4 °C.
Confocal imaging and quanti ﬁcation of M2-like macrophages in quadriceps
cross-sections. Immuno ﬂuorescence images were taken on Nikon W1 Spinning
Disk Confocal microscope at 20x and stitched together with Nikon NIS-Elements
imaging software. The number of M2-like macrophages were quanti ﬁed by taking
ﬁve representative regions of each section for three replicate sections per animal
(n = 3 animals per experimental group; 9 quadriceps total). The three sections per
animal selected for analysis came from different locations within the defect: one
from the proximal end of the defect, one in the center of the defect, and one taken
at the distal end of the injury. CD68
+CD206+DAPI+ M2-like macrophages were
counted using the ImageJ multipoint tool and summed for all ﬁve representative
regions per section. Total M2-like macrophage numbers from each of the three
selected sections were averaged and normalized to total region of interest area.
ARTICLE COMMUNICATIONS BIOLOGY | https://doi.org/10.1038/s42003-023-04790-6
12 COMMUNICATIONS BIOLOGY |           (2023) 6:749 | https://doi.org/10.1038/s42003-023-04790-6 | www.nature.com/commsbio

Second harmonic generation (SHG) imaging of quadriceps cross-sections and
quantiﬁcation of M2-like macrophages and FAPs per collagen . Quadriceps
cryosections of 10 µm thickness were prepared and immunostained as described
above. Multispectral imaging of the slide mounted quadricep muscles was performed
using a custom multiphoton microscope, similar to the previously reported
setup
55–57. In short, the excitation source is a Ti:Sapphire femtosecond pulsed laser
(Chameleon Ultra II, Coherent), set to output a wavelength of 775 nm, the power of
which is adjusted by a half-waveplate and polarizing beam splitter, and is rapidly
modulated by a Pockels cell. A combination resonant scanner and galvo scanner
enables fast scanning of the excitation beam across the sample. Light emitted from the
sample is collected by photon multiplier tubes, allowing for the capture of three
spectral channels. Bandpass ﬁlters at 542 (targeting M2-like macrophages), 457
(targeting FAPs) and 390 (targeting collagen using SHG) provide the requisite spe-
ciﬁcity for single cell analysis. For each injury condition, ~15 images within a region
of 80μmx8 0 μm of each of three samples were collected. Individual M2-like mac-
rophages and FAPs were counted, while a measurement of collagen was performed by
thresholding the SHG images using the default Otsu method in ImageJ. M2-like
macrophages and FAP counts were divided by the mean value of the thresholded
images (range 0-255) to provide a metric for cell count relative to collagen.
Statistics and reproducibility . All statistical analyses were done in GraphPad
Prism 8. Data displayed with outlined bars representing the mean, error bars are ±
Standard Error of the Mean (S.E.M.). For multiple comparisons, one-way or two-
way ANOVA, as appropriate, with Sidak test unless otherwise indicated ,p < 0.05
considered signiﬁcant. Statistical analyses utilized individual animals as biologically
independent replicates. Flow cytometry gating, analysis, and histological quanti ﬁ-
cations were performed in a blinded manner.
Study approval . All animal studies were approved by the Georgia Institute of
Technology Institutional Animal Care and Use Committee.
Reporting summary . Further information on research design is available in the Nature
Portfolio Reporting Summary linked to this article.
Data availability
The authors declare that all relevant data supporting the ﬁndings of this study are
available within the paper and its supplementary ﬁles. All source data for main ﬁgures is
provided in Supplementary Data 1. All other data will be available from corresponding
authors upon reasonable request.
Code availability
The analysis software used in this article is open source. The MATLAB source code for
SPADE is available at http://pengqiu.gatech.edu/software/SPADE/. UMAP source code
used in these studies are available through GitHub ( https://github.com/lmcinnes/umap).
Received: 16 December 2021; Accepted: 31 March 2023;
References
1. Tidball, J. G. Regulation of muscle growth and regeneration by the immune
system. Nat. Rev. Immunol. 17, 165 –178 (2017).
2. Matsuda, R., Nishikawa, A. & Tanaka, H. Visualization of dystrophic muscle
staining with evans blue: evidence muscle 1 ﬁbers in Mdx mouse of apoptosis
in by vital. J. Biochem. 118, 959 –964 (1995).
3. Fielding, R. A. et al. Acute phase response in exercise III Neutrophil and IL-
1p accumu lation in skeletal muscle. Am. J. Physiol. 265, R166 –R172
(1993).
4. Wosczyna, M. N. & Rando, T. A. A muscle stem cell support group: coordinated
cellular responses in muscle regeneration. Dev. Cell 46,1 3 5–143 (2018).
5. Joe, A. W. et al. Muscle injury activates resident ﬁbro/adipogenic progenitors
that facilitate myogenesis. Nat. Cell Biol. 12, 153 –163 (2010).
6. Lemos, D. R. et al. Nilotinib reduces muscle ﬁbrosis in chronic muscle injury
by promoting TNF-mediated apoptosis of ﬁbro/adipogenic progenitors. Nat.
Med 21, 786 –794 (2015).
7. Olingy, C. E. et al. Non-classical monocytes are biased progenitors of wound
healing macrophages during soft tissue injury. Sci. Rep. https://doi.org/10.
1038/s41598-017-00477-1 (2017).
8. Arnold, L. et al. In ﬂammatory monocytes recruited after skeletal muscle injury
switch into antiin ﬂammatory macrophages to support myogenesis. J. Exp.
Med. 204, 1057 –1069 (2007).
9. St Pierre, B. A. & Tidball, J. G. Differential response of macrophage
subpopulations to soleus muscle reloading after rat hindlimb suspension. J.
Appl Physiol. (1985) 77, 290 –297 (1994).
10. Deng, B., Wehling-Henricks, M., Villalta, S. A., Wang, Y. & Tidball, J. G. IL-10
triggers changes in macrophage phenotype that promote muscle growth and
regeneration. J. Immunol. 189, 3669 –3680 (2012).
11. Chazaud, B. In ﬂammation and skeletal muscle regeneration: leave it to the
macrophages! Trends Immunol. 41, 481 –492 (2020).
12. Wang, H. et al. Altered macrophage phenotype transition impairs skeletal
muscle regeneration. Am. J. Pathol. 184, 1167 –1184 (2014).
13. Summan, M. et al. Macrophages and skeletal muscle regeneration: a
clodronate-containing liposome depletion study. Am. J. Physiol. Regul. Integr.
Comp. Physiol. 290, R1488 –R1495 (2006).
14. Zhang, J. et al. CD8 T cells are involved in skeletal muscle regeneration
through facilitating MCP-1 secretion and Gr1(high) macrophage in ﬁltration.
J. Immunol. 193, 5149 –5160 (2014).
15. Burzyn, D. et al. A special population of regulatory T cells potentiates muscle
repair. Cell 155, 1282 –1295 (2013).
16. Villalta, S. A. et al. Regulatory T cells suppress muscle in ﬂammation and
injury in muscular dystrophy. Sci. Transl. Med 6, 258ra142 (2014).
17. Panduro, M., Benoist, C. & Mathis, D. Treg cells limit IFN-gamma production
to control macrophage accrual and phenotype during skeletal muscle
regeneration. Proc. Natl Acad. Sci. USA 115, E2585 –E2593 (2018).
18. Grogan, B. F. & Hsu, J. R., Skeletal Trauma Research, C. Volumetric muscle
loss. J. Am. Acad. Orthop. Surg. 19,S 3 5–S37 (2011).
19. Corona, B. T., Rivera, J. C., Owens, J. G., Wenke, J. C. & Rathbone, C. R.
Volumetric muscle loss leads to permanent disability following extremity
trauma. J. Rehabil. Res Dev. 52, 785 –792 (2015).
20. Pollot, B. E. C., B.T. in Skeletal Muscle Regeneration in the Mouse Methods and
Protocols Methods in Molecular Biology (ed. M. Kyba) Ch. 7 (Springer, 2017).
21. Novak, M. L., Weinheimer-Haus, E. M. & Koh, T. J. Macrophage activation
and skeletal muscle healing following traumatic injury. J. Pathol. 232, 344–355
(2014).
22. Kuswanto, W. et al. Poor repair of skeletal muscle in aging mice re ﬂects a
defect in local, Interleukin-33-dependent accumulation of regulatory T cells.
Immunity 44, 355 –367 (2016).
23. Contreras, O. et al. Cross-talk between TGF-beta and PDGFRalpha signaling
pathways regulates the fate of stromal ﬁbro-adipogenic progenitors. J. Cell. Sci.
https://doi.org/10.1242/jcs.232157 (2019).
24. Anderson, S. E. et al. Determination of a critical size threshold for volumetric
muscle loss in the mouse quadriceps. Tissue Eng. Part C. Methods 25,5 9 –70
(2019).
25. Trapnell, C. et al. The dynamics and regulators of cell fate decisions are
revealed by pseudotemporal ordering of single cells. Nat. Biotechnol. 32,
381–386 (2014).
26. Ramskold, D. et al. Author Correction: Full-length mRNA-Seq from single-
cell levels of RNA and individual circulating tumor cells. Nat. Biotechnol. 38,
374 (2020).
27. Turner, T. C. et al. Harnessing lipid signaling pathways to target specialized
pro-angiogenic neutrophil subsets for regenerative immunotherapy. Sci. Adv .
https://doi.org/10.1126/sciadv.aba7702 (2020).
28. Becht, E. et al. Dimensionality reduction for visualizing single-cell data using
UMAP. Nat. Biotechnol. https://doi.org/10.1038/nbt.4314 (2018).
29. Anchang, B. et al. Visualization and cellular hierarchy inference of single-cell
data using SPADE. Nat. Protoc. 11, 1264 –1279 (2016).
30. Oprescu, S. N., Yue, F., Qiu, J. M., Brito, L. F. & Kuang, S. Temporal dynamics
and heterogeneity of cell populations during skeletal muscle regeneration.
iScience. https://doi.org/10.1016/j.isci.2020.100993 (2020).
31. De Micheli, A. J. et al. Single-cell analysis of the muscle stem cell hierarchy
identiﬁes heterotypic communication signals involved in skeletal muscle
regeneration. Cell Rep . https://doi.org/10.1016/j.celrep.2020.02.067 (2020).
32. Cossarizza, A. et al. Guidelines for the use of ﬂow cytometry and cell sorting in
immunological studies (third edition). Eur. J. Immunol. 51, 2708–3145 (2021).
33. Gautier, E. L. et al. Gene-expression pro ﬁles and transcriptional regulatory
pathways that underlie the identity and diversity of mouse tissue
macrophages. Nat. Immunol. 13, 1118 –1128 (2012).
34. Hymel, L. A. et al. Modulating local S1P receptor signaling as a regenerative
immunotherapy after volumetric muscle loss injury. J. Biomed. Mater. Res. A
109, 695 –712 (2021).
35. Qiu, P. et al. Extracting a cellular hierarchy from high-dimensional cytometry
data with SPADE. Nat. Biotechnol. 29, 886 –891 (2011).
36. Braga, T. T., Agudelo, J. S. & Camara, N. O. Macrophages during the ﬁbrotic
Process: M2 as Friend and Foe. Front. Immunol. 6, 602 (2015).
37. Aguilar, C. A. et al. Correction: Multiscale analysis of a regenerative therapy
for treatment of volumetric muscle loss injury. Cell Death Disco. 4, 16 (2018).
38. Palit, S., Heuser, C., de Almeida, G. P., Theis, F. J. & Zielinski, C. E. Meeting
the challenges of high-dimensional single-cell data analysis in immunology.
Front. Immunol. 10, 1515 (2019).
COMMUNICATIONS BIOLOGY | https://doi.org/10.1038/s42003-023-04790-6 ARTICLE
COMMUNICATIONS BIOLOGY |           (2023) 6:749 | https://doi.org/10.1038/s42003-023-04790-6 | www.nature.com/commsbio 13

39. San Emeterio, C. L., Olingy, C. E., Chu, Y. & Botchwey, E. A. Selective
recruitment of non-classical monocytes promotes skeletal muscle repair.
Biomaterials 117,3 2 –43 (2017).
40. Chen, Y. et al. Aging reprograms the hematopoietic-vascular niche to impede
regeneration and promote ﬁbrosis. Cell Metab. 33, 395 –410.e394 (2021).
41. Borthwick, L. A., Wynn, T. A. & Fisher, A. J. Cytokine mediated tissue ﬁbrosis.
Biochim. Biophys. Acta 1832, 1049 –1060 (2013).
42. Villalta, S. A., Nguyen, H. X., Deng, B., Gotoh, T. & Tidball, J. G. Shifts in
macrophage phenotypes and macrophage competition for arginine
metabolism affect the severity of muscle pathology in muscular dystrophy.
Hum. Mol. Genet . 18, 482 –496 (2009).
43. Sun, L. et al. New concepts of IL-10-induced lung ﬁbrosis: ﬁbrocyte
recruitment and M2 activation in a CCL2/CCR2 axis. Am. J. Physiol. Lung Cell
Mol. Physiol. 300, L341 –L353 (2011).
44. Jetten, N. et al. Anti-in ﬂammatory M2, but not pro-in ﬂammatory M1
macrophages promote angiogenesis in vivo. Angiogenesis 17, 109–118 (2014).
45. Greaves, N. S., Ashcroft, K. J., Baguneid, M. & Bayat, A. Current understanding
of molecular and cellular mechanisms in ﬁbroplasia and angiogenesis during
acute wound healing. J. Dermatol. Sci. 72,2 0 6–217 (2013).
46. Guerriero, J. L. Macrophages: Their untold story in T cell activation and
function. Int Rev. Cell Mol. Biol. 342,7 3 –93 (2019).
47. Bohmer, R. M., Bandala-Sanchez, E. & Harrison, L. C. Forward light scatter is
a simple measure of T-cell activation and proliferation but is not universally
suited for doublet discrimination. Cytom. A 79, 646 –652 (2011).
48. Overgaard, N. H., Jung, J. W., Steptoe, R. J. & Wells, J. W. CD4 +/CD8+
double-positive T cells: more than just a developmental stage? J. Leukoc. Biol.
97,3 1 –38 (2015).
49. Simonetta, F. et al. Increased CD127 expression on activated FOXP3 +CD4+
regulatory T cells. Eur. J. Immunol. 40, 2528 –2538 (2010).
50. Haugen, F. et al. IL-7 is expressed and secreted by human skeletal muscle cells.
Am. J. Physiol. Cell Physiol. 298, C807 –C816 (2010).
51. Dejaco, C., Duftner, C., Grubeck-Loebenstein, B. & Schirmer, M. Imbalance of
regulatory T cells in human autoimmune diseases. Immunology 117, 289–300
(2006).
52. Wherry, E. J. T cell exhaustion. Nat. Immunol. 12, 492 –499 (2011).
53. San Emeterio, C. L. et al. Nano ﬁber-based delivery of bioactive lipids promotes
pro-regenerative in ﬂammation and enhances muscle ﬁber growth after
volumetric muscle loss. Front Bioeng. Biotechnol. 9, 650289 (2021).
54. Fernandez-Yague, M. A. et al. Analyzing immune response to engineered
hydrogels by hierarchical clustering of in ﬂammatory cell subsets. Sci. Adv. 8,
eabd8056 (2022).
55. Forouhesh Tehrani, K., Pendleton, E. G., Southern, W. M., Call, J. A. &
Mortensen, L. J. Spatial frequency metrics for analysis of microscopic images
of musculoskeletal tissues. Connect Tissue Res. 62,4 –14 (2021).
56. Pendleton, E. G., Tehrani, K. F., Barrow, R. P. & Mortensen, L. J. Second
harmonic generation characterization of collagen in whole bone. Biomed. Opt.
Express 11, 4379 –4396 (2020).
57. Tehrani, K. F. et al. Five-dimensional two-photon volumetric microscopy of
in-vivo dynamic activities using liquid lens remote focusing. Biomed. Opt.
Express 10, 3591 –3604 (2019).
Acknowledgements
We thank the core facilities at the Parker H. Petit Institute of Bioengineering and
Bioscience at Georgia Institute of Technology and the Atlanta Veterans Affairs Medical
Center for the use of shared equipment, services, and expertize. This research was
supported by funding from the Department of Defense (Award No. W81XWH-20-1-
0336), the NIH (Grant No. R01AR078375, R01AR062368, and R56DE029703), the U.S.
Department of Veterans Affairs (Grant No. 5 I01 RX001985) and the NSF Engineering
Research Center for Cell Manufacturing Technologies. L.A.H. was supported by the NSF
Graduate Research Fellowship (Grant No. DGE-1650044) and Predoctoral NRSA F31
Fellowship (AWD-003391). S.E.A. and T.C.T. were trainees on the NIH/NIGMS-spon-
sored Cell and Tissue Engineering (CTEng) Biotechnology Training Program
(T32GM008433) while this work was conducted.
Author contributions
L.A.H., S.E.A., Y.C.J., N.J.W., and E.A.B. designed the research studies, analyzed the data,
wrote the manuscript, and reviewed the manuscript. L.A.H., S.E.A., T.C.T., H.Z., and
A.R.L. performed the experiments, analyzed the data, and reviewed the manuscript.
W.Y.Y., H.S.L., P.Q., and L.J.M. contributed to methodology and reviewed the
manuscript.
Competing interests
The authors declare no competing interests.
Additional information
Supplementary information The online version contains supplementary material
available at https://doi.org/10.1038/s42003-023-04790-6.
Correspondence and requests for materials should be addressed to Young C. Jang,
Nick J. Willett or Edward A. Botchwey.
Peer review information Communications Biology thanks Koyal Garg, Sarah Greising
and the other, anonymous, reviewer(s) for their contribution to the peer review of this
work. Primary Handling Editors: Liming Sun and Zhijuan Qiu.
Reprints and permission information is available at http://www.nature.com/reprints
Publisher’s note Springer Nature remains neutral with regard to jurisdictional claims in
published maps and institutional af ﬁliations.
Open Access This article is licensed under a Creative Commons
Attribution 4.0 International License, which permits use, sharing,
adaptation, distribution and reproduction in any medium or format, as long as you give
appropriate credit to the original author(s) and the source, provide a link to the Creative
Commons license, and indicate if changes were made. The images or other third party
material in this article are included in the article ’s Creative Commons license, unless
indicated otherwise in a credit line to the material. If material is not included in the
article’s Creative Commons license and your intended use is not permitted by statutory
regulation or exceeds the permitted use, you will need to obtain permission directly from
the copyright holder. To view a copy of this license, visit http://creativecommons.org/
licenses/by/4.0/.
© The Author(s) 2023
ARTICLE COMMUNICATIONS BIOLOGY | https://doi.org/10.1038/s42003-023-04790-6
14 COMMUNICATIONS BIOLOGY |           (2023) 6:749 | https://doi.org/10.1038/s42003-023-04790-6 | www.nature.com/commsbio