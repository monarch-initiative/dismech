---
reference_id: url:https://zenodo.org/records/23035979/files/1-s2.0-S0161813X26000355-main.pdf
extractor_version: 1
title: "https://zenodo.org/records/23035979/files/1-s2.0-S0161813X26000355-main.pdf"
content_type: full_text_pdf
full_text_url: "https://zenodo.org/records/23035979/files/1-s2.0-S0161813X26000355-main.pdf"
---

# https://zenodo.org/records/23035979/files/1-s2.0-S0161813X26000355-main.pdf

## Content

The zebrafish visual and acoustic motor response (VAMR) assay has the
potential to add value to the developmental neurotoxicity in Vitro battery
(DNT IVB)
Julia Spath
a , 1
, Jana Raab
a , 1
, Jana Schor
c , d
, Stefan Scholz
a
, Sebastian Gutsfeld
a , *
,
Tamara Tal
a , b , **
a
Ecotoxicology Department, Chemicals in the Environment Research Section, Helmholtz Centre for Environmental Research – UFZ, Leipzig, Germany
b
Medical Faculty, University Leipzig, Leipzig, Germany
c
Computational Biology Department, Helmholtz Centre for Enviromental Research - UFZ, Leipzig, Germany
d
Faculty of Mathematics and Computer Science, University of Leipzig, Leipzig, Germany
ARTICLE INFO
Keywords:
DNT
Zebrafish
Automated behavior testing
New Approach Methods
NAMs
DNT IVB
ABSTRACT
Less than 150 chemicals have been evaluated for their potential to cause developmental neurotoxicity (DNT)
using OECD rodent-based test guidelines. The DNT in vitro battery (DNT IVB), comprised of 17 human or rodent
cell-based assays, is a proposed alternative. Recent work identified three false negative compounds that are
developmentally neurotoxic in rodent or human studies but negative in the DNT IVB (5,5-diphenylhydantoin,
maneb, nicotine). We hypothesized that multi-behavioral phenotyping in early-life stage zebrafish can com -
plement the DNT IVB. Zebrafish embryos or larvae were acutely (40 min) or developmentally (1 – 5 days post-
fertilization) exposed to 12 DNT positive chemicals 5,5-diphenylhydantoin, BDE-99, chlorpyrifos, haloperidol,
hexachlorophene, ketamine hydrochloride, maneb, nicotine, PFOA, tebuconazole, trichlorfon, or triethlytin
bromide or to 0.4% DMSO. Behavior was evaluated using the Visual and Acoustic Motor Response (VAMR) assay,
comprised of 26 behavioral endpoints including visual and acoustic startle responses, non-associative habituation
learning, and memory retention. Five proposed DNT negative compounds were also evaluated under both
exposure paradigms. To fit concentration response data, generalized additive and linear mixed effects modeling
strategies were combined with Fr ´echet distance calculations. Hit calls were identified such that inclusion of the
zebrafish VAMR assay within the DNT IVB would potentially increase battery sensitivity without compromising
battery specificity. Hits in the VAMR assay were typically detected at 1 – 4 orders of magnitude lower concen -
trations relative to the DNT IVB. Taken together, the zebrafish behavior-based VAMR assay can add value to the
DNT IVB by increasing test battery sensitivity and enhancing potency detection.
1. Introduction
The developing nervous system is particularly sensitive to chemical
exposure ( Bennett et al., 2016 ) and can result in Developmental
Neurotoxicity (DNT) or any harmful neurodevelopmental effect caused
by chemical exposure in utero or during early life stages ( Grandjean and
Landrigan, 2014 ). Disruption of neurodevelopment can have severe
consequences, leading to impaired cognitive function and learning
abilities ( Tooley et al., 2021 ) or other neurobehavioral deficits such as
attention deficit hyperactivity disorder ( Dalsager et al., 2019 ) or Autism
Spectrum Disorder ( Lyall et al., 2017; Pistollato et al., 2020 ). Despite
this understanding, fewer than 150 unique chemicals ( Feshuk et al.,
2023 ), out of an estimated number of 350,000 chemicals registered for
production and use ( Wang et al., 2020 ), have been assessed for their
potential to cause DNT using Organization for Economic Cooperation
and Development (OECD) DNT test guidelines ( Crofton and Mundy,
2021; Makris et al., 2009 ) housed in the US EPA ToxRef database
( Feshuk et al., 2023 ). This gap in testing exists because OECD DNT test
* Corresponding author.
** Corresponding author at: Ecotoxicology Department, Chemicals in the Environment Research Section, Helmholtz Centre for Environmental Research – UFZ,
Leipzig, Germany.
E-mail addresses: sebastian.gutsfeld@ufz.de (S. Gutsfeld), tamara.tal@ufz.de (T. Tal).
1
Equal contribution
Contents lists available at ScienceDirect
Neurotoxicology
journal homepag e: www.else vier.com/loc ate/neuro
https://doi.org/10.1016/j.neuro.2026.103414
Received 23 December 2025; Received in revised form 27 February 2026; Accepted 28 February 2026
Neurotoxicology 114 (2026) 103414
Available online 2 March 2026
0161-813X/© 2026 The Author(s). Published by Elsevier B.V. This is an open access article under the CC BY license ( http://creativecommons.org/licenses/by/4.0/ ).

guidelines are performed in the offspring of pregnant rodents ( Makris
et al., 2009; OECD, 2007, 2025; Sachana et al., 2019 ), resulting in ex -
periments that are time-, and resource-intensive and present with ethical
concerns ( Bal-Price, 2018a; Crofton, 2010 ). This underscores the need
for New Approach Methods (NAM) ( Bal-Price, 2018 ; Crofton, 2010 )
performed in cellular or alternative test systems ( Tal et al., 2024 ).
A promising alternative to rodent-based DNT studies is the DNT in
vitro battery (DNT IVB), comprised of 17 cell-based New Approach
Methods (NAMs) that cover key neurodevelopmental processes such as
proliferation of neural progenitor cells, migration of neural crest cells,
radial glia cells, neurons, and oligodendrocytes, differentiation of neural
progenitor cells into neurons and oligodendrocytes, neurite outgrowth
of peripheral and central neurons, and non-specific cytotoxicity ( Blum
et al., 2023; Carstens et al., 2022; Masjosthusmann et al., 2020 ). While
the DNT IVB provides important endpoints for the evaluation of devel -
opmental neurotoxicity, it is currently unable to capture complex
cellular endpoints related to myelination, blood-brain barrier develop -
ment and function, and neuroinflammation, or functional indicators of
control-like neurodevelopment that are measured in the rodent test
guidelines, including motor activity, motor and sensory function,
learning, and memory ( Bal-Price, 2018a; Blum et al., 2023; Fritsche
et al., 2015; Juberg et al., 2023; Masjosthusmann et al., 2020; OECD,
2007 ). In addition, in vitro assays can fail to detect the neurotoxicity of
compounds that require biotransformation to exert DNT effects ( Juberg
et al., 2023 ).
We hypothesized that zebrafish behavior-based testing can fill un -
certainties in the DNT IVB while simultaneously adhering to the 3R
principle to reduce, refine, or replace the use of animal testing in
chemical safety assessment ( Pallocca, 2022 ). Zebrafish up to five days
post-fertilization (dpf), according to EU legislation, represent an un -
protected life stage. The model can therefore serve as a functional
( L ´egar ´e et al., 2025 ), 3R-compliant alternative to rodent DNT studies
( Cassar et al., 2020 ), with relevance to humans ( Tal et al., 2020 ). Ad -
vantages of using early life stage zebrafish for DNT testing are plentiful
( Tanguay, 2025 ) and include a high degree of genetic homology to
humans where approximately 82% of genes associated with diseases are
related to at least one zebrafish orthologue ( Howe et al., 2013 ). Zebra -
fish also rapidly develop external to the mother such that offspring can
be easily used in medium-to-high-throughput chemical screens. This
includes automated behavior testing where responses to visual and
acoustic stimuli can provide a functional readout of neurodevelopment
( Herold et al., 2025; Leuthold et al., 2025; McAtee and Abdelmoneim,
2024 ). This is possible due to a wide range of stereotyped behaviors
present in early-life stage zebrafish such as contractions, visual motor
responses, visual and acoustic startle responses, non-associative habit -
uation learning, and memory retention ( Bruni et al., 2016; Leuthold
et al., 2025 ). Inclusion of zebrafish behavior-based testing can poten -
tially complement the DNT IVB due to their intact blood-brain barrier,
myelinated axons, presence of functional neurotransmitter systems such
as γ -Aminobutyric acid (GABA), glutamate, serotonin, dopamine,
noradrenaline, and acetylcholine dependent signaling ( Horzmann and
Freeman, 2016; Panula et al., 2010 ), and the ability to test for altered
behavior, including learning and memory effects ( Tal et al., 2024 ), all in
a metabolically competent test system ( Juberg et al., 2023 ).
The Visual and Acoustic Motor Response (VAMR) NAM contains 26
endpoints that have the collective potential to capture chemical-
dependent effects on visual and acoustic startle responses, visual
motor responses, seizure-like activity and effects on non-associative
habituation learning, and memory retention ( Herold et al., 2025; Leut -
hold et al., 2025 ). Here, we hypothesized that the VAMR NAM can
improve the detection of reference chemicals that cause DNT in rodent
guideline studies but were missed by cellular assays in the test battery
(‘false negatives ’ ). We also hypothesized that, because behavior is such a
sensitive readout of potential DNT effects, when comparing ‘true posi -
tive ’ compounds, potency values would be lower in the zebrafish-based
VAMR NAM relative to the DNT IVB. This study demonstrates that the
VAMR NAM can detect ‘false negative ’ compounds missed by the DNT
IVB and, for ‘true positive ’ chemicals, enhances potency detection.
Evaluation of ‘predicted negative ’ chemicals for DNT ( Blum et al., 2023;
Carstens et al., 2022; Martin et al., 2022 ), additionally identified both
assay-specific negatives and false negatives in the VAMR assay. Taken
together, the VAMR NAM can potentially add value to the DNT IVB and,
more broadly, this work demonstrates that multi-behavioral phenotyp -
ing in early life-stage zebrafish yields rapid, useful information on the
ability of chemicals to disrupt nervous system development and
function.
2. Material and methods
2.1. Zebrafish husbandry
All procedures involving the care and handling of zebrafish ( Danio
rerio ) were conducted in compliance with established guidelines and
regulations. Approval was granted by the local government authority
(Landesdirektion Sachsen, Gesch ¨aftszeichen 24 – 5131/252/7) ensuring
adherence to ethical and legal standards. The zebrafish strain used was
the in-house ‘UFZ-OBI/WIK ’ strain. Zebrafish were housed in 27 L glass
tanks with approximately five fish per L, pH levels were maintained
between 7 and 8, water hardness between 4 and 16
◦
dH, nitrate below
50 mg/L, nitrite below 0.05 mg/L, ammonia below 0.35 mg/L, and
oxygen saturation between 87% and 91%, and fish were kept under a
14:10 light cycle at 28
◦
C. The recirculating aquaculture system
exchanged water at a rate of approximately 5x/hour/tank with a 10%
exchange from system to fresh water/day. Water is filtered and UV-
sterilized before circling back into the tanks. Dry food (Sparos) and
shell-free artemia (Sanders) were each provided once daily during the
week and artemia was additionally provided once daily on Saturday and
Sunday.
2.2. Chemical selection and preparation
This study assessed 12 chemicals predicted to be developmental
neurotoxicants ( Aschner, 2016 ; Mundy and Crofton, 2024 ). Based on
subsets of the DNT IVB (EU assays depicted in ( Blum et al., 2023 ); US
EPA assays reflected in ( Carstens et al., 2022 )), this included nine
compounds that were selective for DNT endpoints (relative to
non-specific cytotoxicity) in the DNT IVB, classified as ‘true positive ’
(TP) compounds and included 2,2 ′ ,4,4 ′ ,5-pentabromdiphenylether
(BDE-99), chlorpyrifos, haloperidol, hexachlorophene, ketamine hy -
drochloride, perfluorooctanoic acid (PFOA), tebuconazole, trichlorfon,
and triethyltin bromide. AC50 values from the US EPA DNT IVB for
BDE-99 and PFOA were not reported in the published manuscript
( Carstens et al., 2022 ) but were identified in the US EPA CompTox
database (v4.3; https://comptox.epa.gov/dashboard/ ; accessed
December 2025). It is important to note that isomers of ketamine hy -
drochloride were tested in different subsets of the DNT IVB. Ketamine
hydrochloride was tested here and in the European DNT IVB assays
( Blum et al., 2023 ) while L-ketamine hydrochloride was tested in the
EPA DNT IVB assays ( Carstens et al., 2022 ). Three chemicals classified as
‘false negative ’ (FN) in the DNT IVB, meaning they were associated with
human DNT or were DNT positive in rodent guideline studies ( Aschner,
2016 ; Mundy and Crofton, 2024 ) but negative in the DNT IVB ( Blum
et al., 2023; Carstens et al., 2022 ) were also evaluated. These included 5,
5-diphenylhydantoin (DPH), maneb, and nicotine. Four additional
chemicals, classified as “ favorable ” DNT negative reference chemicals
(D-mannitol, ibuprofen, saccharin, and sodium benzoate) and one that
was not (acetaminophen), were also evaluated ( Martin et al., 2022 ;
Mundy and Crofton, 2024 ). Chemical Abstracts Service Registry
(CASRN) number, SMILES identifiers, and supplier for each chemical are
listed in Table S1 . For exposure, 20 mM stocks were prepared by dis -
solving solid chemicals in anhydrous dimethyl sulfoxide (DMSO). For
hexachlorophene, 1 mM stocks were prepared. Chemical stocks were
J. Spath et al.                                                                                                                                                                                                                                    Neurotoxicology 114 (2026) 103414
2

aliquoted and stored at -80
◦
C. Each aliquot was discarded after a single
use.
2.3. Zebrafish handling
Embryos were collected between 2 and 3.5 h post fertilization (hpf)
using a dissection microscope (Olympus SZx7-ILLT). Selection was
based on defined criteria, including symmetrical cell division and a well-
defined blastocoel ( Kimmel et al., 1995 ). To decrease the microbial load,
embryos were bleached for 5 min using a 0.05% NaOCl solution and
then washed in 10% Hanks' Balanced Salt Solution (HBSS). Approxi -
mately 50 zebrafish embryos were placed in glass crystallization dishes
with 50 ml of 10% HBSS and stored on a 14:10 h light:dark cycle at 28
◦
C.
2.4. Acute exposure
At 4 dpf, zebrafish were transferred to 96-square well polystyrene
plates (Uniplate ® , Whatman microplate devices), with one larva per
well containing 400 μ L of 10% HBSS. Zebrafish selection was based on
the presence of normal developmental landmarks including the presence
of a swim bladder. Microsealers (Biorad) and parafilm were used to
prevent evaporation. Plates were stored in a 14:10 h light:dark cycle at
28
◦
C. At 5 dpf, plates were kept in the dark until exposure to the test
compounds. Based on previous work, an initial concentration of 80 µ M
was selected ( Gaballah et al., 2020; Herold et al., 2025; Leuthold et al.,
2025 ). Chemicals were serially diluted with DMSO using quarter log
spacing to obtain six concentrations (4.4 – 80 µ M) of each test substance.
If compound exposure was lethal in more than 50% of the tested con -
centration, the first no effect concentration was selected for subsequent
experiments. Compounds to which this applied were nicotine (highest
concentration tested = 25.1 µ M), hexachlorophene (0.6 µ M), maneb
(4.4 µ M), and triethyltin bromide (4.4 µ M). Curve fitting requires
identification of no effect levels. To obtain no effect levels for potent
compounds, including chlorpyrifos, haloperidol, hexachlorophene,
tebuconazole, trichlorfon, and triethyltin bromide, testing occurred at
additional concentrations, starting with one overlapping concentration
to the previous experiment and serially diluted with DMSO to generate
six concentrations with log spacing. For nicotine, a volatile compound, a
different strategy was applied to prevent contamination of control
larvae. Larvae in columns 1 – 4 were exposed to one of six concentrations
(quarter-log spacing, 1.4 – 25.1 µ M), followed by four columns with no
larvae and four columns containing the vehicle control such that, in the
data analysis, each concentration had a concentration-specific vehicle
control group. For each experiment, three plates were evaluated
collectively containing 36 zebrafish per exposure group and 72 control
larvae. For all exposure scenarios, a final vehicle concentration of 0.4%
was used, which does not alter behavior in the testing phase of the
behavior assay ( Herold et al., 2025 ). Exposure was conducted under
light conditions, then plates were placed in the light in an incubator set
to 28
◦
C for 40 min, then transferred to the behavior apparatus for
testing.
2.5. Developmental exposure
Embryo collection, selection, and preparation were performed on
day 0 as described above. At 1 dpf, embryos were transferred to a 96-
square well polystyrene plate (Uniplate ® , Whatman microplate de -
vices), with one embryo per well containing 400 μ L of 10% HBSS. Em -
bryo selection was based on the presence of normal developmental
landmarks then chemical exposures commenced. Selection of the initial
test concentration was based on preliminary qualitative range finding
assessments where the highest test concentration for the behavioral
assessment was set between the lowest effect and no effect concentra -
tions, based on morphological assessments (i.e., absence of malforma -
tions and presence of an inflated swim bladder). Compounds were
serially diluted with DMSO using semi log spacing to obtain nine
concentrations of each test substance. For each experiment, four plates
were evaluated collectively containing 32 zebrafish per exposure group
and 96 control larvae. For all exposure scenarios, a final vehicle con -
centration of 0.4% was used, which does not alter behavior in the testing
phase of the behavior assay ( Fig. S1 ). Microsealers (Biorad) and parafilm
were used to prevent evaporation and plates were stored in a 14:10 h
light:dark cycle at 28
◦
C until behavior assessment on 5 dpf. At 5 dpf,
plates were kept in the dark until 40 min before behavior testing.
2.6. Automated behavior testing and processing of behavior data
Based on previous work ( Herold et al., 2025; Leuthold et al., 2025 ),
the Visual and Acoustic Motor Response (VAMR) assay was used. The
assay consists of 26 sequential behavior endpoints following the appli -
cation of visual (dark (0 lux) or light (13.5 klux)) stimuli or acoustic (low
(65 dB) or high volume (75 dB), measured with the app “ Schallmes -
sung/Sound Meter ” , V 1.4.3 and an android device microphone) stimuli
with a frequency of 300 Hz. Each stimulus triggered a range of quanti -
fiable behavioral responses (pixel changes per second). The assay had
duration of 1 h 17 min and was performed at a constant temperature of
28
◦
C. Briefly, following a 1 min light period (13.5 klux), a dark period
ensued comprised of the Visual Startle Response Baseline (VSRB) (i.e.,
activity during 1 s directly after the light change) and a subsequent
20 min baseline period, divided into four endpoints (BSL1 – 4). Next, 13.5
klux light was applied for 10 min, comprised of a 1 s visual startle
response (VSR1) endpoint and 9 min 59 s Visual Motor Response
(VMR1) endpoint. The rest of the assay was performed under dark
conditions (0 lux). This began with the VSR2 endpoint which captured a
1 s startle response, followed by a 4 min 59 s period (VMR2) and an
additional 15 min period, comprised of three 5 min periods
(VMR3-VMR5). Next, an acoustic startle response (ASR1) endpoint,
consisting of the mean motor activity across five low-intensity acoustic
stimuli (65 dB) interspaced by 1 min interstimulus intervals (ISIs) that
were summed to generate the ISI1 endpoint. This was followed by the
ASR2 endpoint, comprised of the mean motor activity across five
high-intensity acoustic stimuli (75 dB) interspaced by one-minute ISIs
(summed to form ISI2). This was followed by Acoustic Startle Habitua -
tion (ASH) training comprised of five habituation bouts, each consisting
of 30 1 s high-intensity acoustic stimuli interspersed by 1 s ISIs. The
ASH1 endpoint reflects the cumulative motor activity during the final
ten stimuli which comprise bout 1, relative to the summed activity
during the initial and final ten stimuli, again within bout 1 ( Herold et al.,
2025; Leuthold et al., 2025; Lloyd et al., 2014 ). Potentiation of habit -
uation (ASH1/5) was determined by calculating the ratio of motor ac -
tivity in the final habituation bout (ASH5) to the sum of activities in both
the initial (ASH1) and final bout (ASH5). The cumulative value of the
five habituation bouts comprised the ASHsum endpoint. The habituation
period was followed by a 3 min rest period. Then, five high-intensity
acoustic stimuli (1 s, 1 min ISI) were averaged (ASR3) and scaled to
the average responses from ASR2 and ASR3 endpoints as a reflection of
memory retention (ASR2/3) post-habituation training. Summed motor
activity during Inter-Endpoint Intervals (IEI1 – 3) and Inter-Bout In -
tervals (IBI) was also determined ( Table S2 ). Each experiment contained
3 – 6 plates of zebrafish, depending on whether additional concentrations
were tested to identify no effect concentrations for behavior modeling.
Each experiment was assessed on the same behavior apparatus (Zebra -
box, Viewpoint). Multiple instruments were used. Video tracking was
conducted at 25 frames per second using ZebraLab software (ViewPoint)
in quantization mode.
2.7. Behavior analysis
All behavior plates exposed to the same chemical and tested on the
same day were treated as a single experimental unit. Within each unit,
all individuals assigned to a given exposure concentration (including
DMSO control larvae) were pooled across plates. For some test
J. Spath et al.                                                                                                                                                                                                                                    Neurotoxicology 114 (2026) 103414
3

chemicals, in order to reach no effect concentrations, multiple experi -
mental units were required to evaluate extended concentration ranges
that could not be covered within a single run. In such cases, the statis -
tical models described in Sections 2.7.1 and 2.7.2 were fitted separately
for each experimental unit (i.e., two experimental units yielded two
independent models). Consequently, all reported p-values represent
comparisons between each concentration and its corresponding control
within the same experimental unit. When concentration ranges over -
lapped across units, the data were retained as separate sets and dis -
played in distinct line and rain boxplots. In addition, because nicotine
was volatile, only one concentration was tested per plate in a experi -
mental unit. Therefore, line and boxplots contain concentration specific
vehicle control data.
2.7.1. Analysis of timeseries endpoints (BSL1-4, VMR1-5)
Analysis procedures for timeseries endpoints have been previously
described in detail ( Gutsfeld et al., 2024 ) and are briefly explained here.
The analysis pipeline used for these endpoints is available as a
user-friendly set of R-written functions (version 0.1; Zenodo, ( Gutsfeld,
2024 )). For all timeseries endpoints, pixels changed per individual larva
was summed in 1-min intervals. For assay phases BSL1 – 4 and VMR2 – 5
(each 5-min long), five 1-min movement sums were calculated per in -
dividual larva. For VMR1 (10-min long) ten 1-min movement sums were
calculated per individual larva. For all values from BSL1 – 4 and VMR1 – 5,
a model of pixels changed was fit using a beta distribution. The upper
limit for normalization was defined as 1.001 times the largest pixel
change by any individual larva within each experiment. Movement sum
data were fitted using generalized additive mixed-effects models
(GAMMs) from the mgcv package (v1.9 – 3) in R ( Wood, 2017 ). Temporal
nonlinearity was captured using smoothing splines, while concentration
and phase were incorporated as categorical predictors, including their
second-order interactions. Individual variability due to repeated mea -
surements was modeled as random effects. Model adequacy was evalu -
ated through visual inspection of the estimated smooth functions and
corresponding residual diagnostics ( Fig. S2 ). Estimated marginal means
(EMMs) were derived as post hoc comparisons between exposure and
control groups using the emmeans package (v1.11.1) ( Lenth and Pias -
kowksi, 2025 ), with Dunnett adjustments applied to control for multiple
testing.
2.7.2. Analysis of single-value endpoints (VSRB, VSR1-2, ASR1-3, ASR2/
3, ISI1-3, IEI1-3, ASH1, ASH1/5, IBI, ASHsum)
All single value endpoints were modeled using individual gaussian
linear models. For each endpoint in each experiment, the processed
response per animal was modeled using exposure concentration as a
categorical variable. EMMs were calculated as post hoc tests of the fitted
model and obtained p-values for exposure versus control group com -
parisons were Dunnett-adjusted to account for multiple comparisons
using the r package emmeans ( Lenth and Piaskowksi, 2025 ).
2.8. Curve fitting
The tcplfit2 package (v0.1.8) ( Sheffield et al., 2022 ) was used to
derive toxicologically relevant metrics, including point of departure
estimates (ACC), half-maximal effect concentrations (AC50), and
Benchmark Concentrations (BMC) from the behavioral endpoints
described above. To obtain hit calls, assay-specific cutoff values were
defined, as explained below. An endpoint was classified as a hit, if the hit
call was ≥ 0.9. Hit calls were included in downstream analyses only for
curve fits with less than two flags. BMC values were derived by using the
tcplfit2 default calculation of 1.39 * one standard deviation of the
baseline response ( Sheffield et al., 2022 ). Calculated values for VAM -
R_acute and VAMR_dev are shown in Table S3 and Table S4 .
2.8.1. Curve fitting of timeseries endpoints (BSL1-4, VMR1-5)
For time-series endpoints, GAMM model predictions (excluding
random effects) were used to derive input metrics for tcplfit2. The
dissimilarity between predicted mean fits of control (0.4% DMSO) and
exposure groups was quantified using Fr ´echet distance calculations
implemented in the R package longitudinalData (v2.4.7) ( Genolini,
2009 ). This procedure produced one distance metric for each con -
trol – concentration comparison, which was then supplied to tcplfit2. To
determine the activity cutoff, Fr ´echet distances were calculated between
the predicted model fit for each individual control larva and the
population-level control fit. The mean of these distances was used as the
cutoff value. For compounds tested across multiple experimental units,
cutoff distributions were first generated within each unit, then pooled
and the mean of the pooled values was used as the shared cutoff.
2.8.2. Curve fitting of single value endpoints (VSRB-VSR2, ASR1-3, ASR2/
3, ISI1-3, IEI1-3, ASH1, ASH1/5, IBI, ASHsum)
For single-value endpoints, the absolute coefficient estimates from
the linear models described in Section 2.7.2 were used as input for
tcplfit2. These coefficients represent the absolute deviation of the mean
response at each concentration from the corresponding baseline mean.
The activity cutoff was defined as the mean absolute deviation of the
baseline values, and the standard deviation used for BMC estimation was
defined as the baseline standard deviation.
2.9. Baseline toxicity prediction
The baseline toxicity represents the predicted hydrophobicity-driven
non-specific toxicity concentration (LC
50
) based on a linear regression
model ( Klüver et al., 2019 ). For zebrafish embryos, the LC
50
was pre -
dicted from the D
lip/w
, the ionization-corrected liposome water partition
coefficient using the following equation:
log LC
50 zebrafish embryo
( mM ) = � 0 . 99 ∗ D
lip / w
+ 2 . 22
The D
lip/w
was used as a proxy for partition between biological
membranes and water and is composed of the K
lip/w
for neutral and
multiple charged species. The K
lip/w
can be measured or predicted from
the octanol-water partition coefficient ( K
ow
). In the present study K
lip/w
was obtained via prediction from experimental Abraham parameters
( Ulrich et al., 2024 ). When these were not available, a regression
equation was used to estimate the log K
lip/w
from the K
ow
.
Log
K lip
w
( neutral ) = 1 . 01 × log K ow + 0 . 12
Octanol-water partition constants ( K
ow
) were retrieved from exper -
imental data in the CompTox database ( Williams et al., 2017 ) ( https
://comptox.epa.gov/dashboard/ ). If experimental data was not avail -
able, the mean K
ow
was determined from the predicted values using
KOWWIN v1.67 and ACD/Labs Consensus data obtained from CompTox
database. To obtain the D
lip/w
the sum of the fractions of the K
lip/w
of
neutral and ionized species at pH 7.4 were calculated using pKa values
with the Henderson-Hasselbalch equation. The log K
lip/w
of ionized
species was considered as one log unit below the log K
lip/w
of the neutral
species.
D
lip / w
( pH 7 . 4 ) =
∑
n
i = 1
f
i
∗ k
lip / w
( i )
2.10. Data availability
All underlying data are available via DOI: 10.5281/zen -
odo.17937513 (will be made public upon manuscript acceptance).
J. Spath et al.                                                                                                                                                                                                                                    Neurotoxicology 114 (2026) 103414
4

Fig. 1. Experimental design. (A) Compounds tested in the VAMR NAM. ‘False negative ’ compounds, denoted in green, were associated with DNT in human studies
and/or positive for DNT in rodent studies but negative in the DNT IVB. ‘True positive ’ compounds, denoted in blue, were associated with human DNT and/or positive
in rodent DNT studies and positive in the DNT-IVB. ‘Predicted negative ’ compounds, shown in pink, include chemicals that are predicted to be negative for DNT
based on available in vitro and in vivo DNT data. (B) Acute VAMR assay. Embryos were collected at 0 dpf, added to 96 well plates at 4 dpf, and exposed to test
chemicals at 5 dpf. 40 min later, the VAMR behavior test was performed. (C) Developmental VAMR assay. Embryos were collected at 0 dpf, added to 96-well plates at
1 dpf, and exposed to test chemicals at 1 dpf. At 5 dpf, the VAMR behavior test was performed. VAMR NAM data for larvae (D) acutely (n = 1790) or (E) devel -
opmentally (n = 1573) exposed to 0.4% DMSO. Motor activity (y-axis) across 26 behavioral endpoints (x-axis). The initial visual startle response (VSRB) represents
the movement in the 1 s period following a light-to-dark transition. Activity during the 20 min dark period (BSL1 – 4). A visual startle response (VSR1) was caused by a
dark-to-light transition. The light period (13.5 klux) reduced motor activity. A visual startle response (VSR2) was triggered by a light-to-dark transition. After an
initial increase in motor activity, swimming behavior decreases back to baseline activity in a 20 min dark period (VMR2 – 5). A series of five low-intensity acoustic
stimuli (1 s) provoked acoustic startle responses (ASR1). A series of high-intensity acoustic stimuli (interstimulus interval (ISI) = 1 s) caused a decrement in the
startle response, indicative of habituation. ASHsum represents the aggregate sum of the five habituation bouts. ASH, acoustic startle habituation; ASR, acoustic startle
response; BSL, baseline motor activity; dpf, day post fertilization; IBI, inter-bout interval; IEI, inter-endpoint interval; ISI, inter-stimulus interval; NAM, New
Approach Method; VMR, visual motor response; VSR, visual startle response; VSRB, visual startle response baseline.
J. Spath et al.                                                                                                                                                                                                                                    Neurotoxicology 114 (2026) 103414
5

Fig. 2. Acute or developmental exposure to chlorpyrifos altered neurobehavior in zebrafish. Motor activity (pixels/s) (y-axis) over time (x-axis) is depicted for
zebrafish larvae (A) acutely or (B) developmentally exposed to 4.4 μ M or 5.3 μ M chlorpyrifos (blue), respectively (n = 27 – 36), as compared to the 0.4% DMSO (grey;
n = 72 – 95). Boxplots depict behavioral responses following (C-F) acute exposure to 0.00004 – 80 µ M chlorpyrifos or (G-J) developmental exposure to 0.0017 – 16.7 µ M
chlorpyrifos. For acute data, to reach no effect concentrations, two concentration ranges were screened and are reflected side-by-side with experiment-specific control
data (grey). Numbers below the boxplots represent adjusted p-values (grey: p ≥ 0.05; black: p < 0.05) and horizontal dotted lines show the median motor activity in
the control group. ASH, acoustic startle habituation; ASR, acoustic startle response; BSL, baseline motor activity; IBI, inter-bout interval; IEI, inter-endpoints interval;
ISI, inter-stimulus interval; NAM, New Approach Method; VMR, visual motor response; VSR, visual startle response; VSRB, visual startle response base -
line. n = 16 – 95.
J. Spath et al.                                                                                                                                                                                                                                    Neurotoxicology 114 (2026) 103414
6

3. Results
3.1. Selection of test chemicals for evaluation in the zebrafish Visual and
Acoustic Motor Response (VAMR) assay
Twelve compounds were selected for testing with mammalian or
human evidence for DNT ( Table S1 ) ( Aschner, 2016 ; Mundy and Crof -
ton, 2024 ). Of these, nine were positive in the DNT IVB and considered
here as ‘true positives’ ( Fig. 1 A, Table S1 ). The remaining three chem -
icals were associated with DNT in human or rodent DNT test guideline
studies but negative in the DNT IVB and therefore defined here as ‘false
negatives’ ( Fig. 1 A, Table S1 ). In addition, five predicted negative
chemicals were selected ( Fig. 1 A, Table S1 ) ( Blum et al., 2023; Carstens
et al., 2022; Martin et al., 2022 ; Mundy and Crofton, 2024 ). To test the
hypothesis that a functional, behavior-based assay can increase the
sensitivity and potency detection of the DNT IVB, true positive, false
negative, and predicted negative compounds were evaluated in the 26
endpoint Visual and Acoustic Motor Response (VAMR) NAM ( Herold
et al., 2025; Leuthold et al., 2025 ) using acute ( Fig. 1 B) and develop -
mental ( Fig. 1 C) exposure regimes. For acute exposures, 5 dpf zebrafish
were exposed to test compounds 40 min before behavior testing
( Fig. 1 B). In contrast, for developmental exposures, zebrafish were
exposed from 1 to 5 dpf, followed by behavior testing on day 5 ( Fig. 1 C).
The behavior test was identical for acute ( Fig. 1 D) and developmental
( Fig. 1 E) exposure regimes.
3.2. Acute or developmental exposure to chlorpyrifos altered behavior
with opposite directionality
The 17 chemical test set was evaluated using acute (acute VAMR
assay) and developmental (developmental VAMR assay) exposure de -
signs. Acute exposure to 0.00004–80 µM chlorpyrifos was characterized
by increased locomotor activity in normally quiescent periods (VMR1,
ISI1–3, IEI1–3, IBI) ( Fig. 2 A, C-E, Fig. S3 ) and increased activity during
some dark periods ( Fig. S3 ). In contrast, developmental exposure to
0.0017–16.7 µM chlorpyrifos resulted in reductions in motor activity
across most endpoints ( Fig. 2 B, G-J, Fig. S4 ) although no effect was
observed in the light period (VMR1). Line- and boxplots for all test
chemicals are included in the data supplement ( Fig. S3-S4 ).
3.3. Acute or developmental exposure to chlorpyrifos caused
concentration dependent behavior effects
To enable comparisons between DNT IVB and VAMR assay data,
novel curve fitting methods were applied (see Section 2.7 ). Curve fits for
the same endpoints shown in Fig. 2 are depicted for zebrafish acutely
( Fig. 3 A-D) or developmentally ( Fig. 3 E-H) exposed to chlorpyrifos.
Acute exposure resulted in AC50 values ranging from 2.46 to 9.01 µM.
For the same endpoints in the developmental exposure assay, lower
AC50 values, ranging from 0.08 to 0.17 µM were estimated. Curve fits
with estimated concentration response metrics for all test chemicals are
included in the supplement ( Fig. S5-S6 ).
3.4. Integration of acute and developmental activity patterns and DNT hit
call concordance
The VAMR assay contains behavior data on 26 endpoints. To visu -
alize chemical- and exposure period-dependent activity patterns, log10-
AC50 values ( Tables S3-S4 ) were used ( Fig. 4 ). Grey squares indicate
negative endpoints while red and blue shading represents hit calls
following acute or developmental exposure, respectively. Hit calls were
included for curve fits with less than two flags, which is a more stringent
cutoff than previous work ( Carstens et al., 2022; Martin et al., 2024 )
while also minimizing the identification of false positive chemicals. The
nine true positive DNT reference chemicals (represented by shades of
blue) were detected as hits in the acute and developmental VAMR
assays, whereas the three false negative chemicals (represented in
shades of green) were only hits in the acute VAMR assay (5,5-diphe -
nylhydantoin, maneb, and nicotine) ( Fig. 4 A, Fig. S7 ). Among the five
predicted negative reference chemicals, ibuprofen was the only chemi -
cal that altered behavior ( Fig. 4 A, Fig. S7-S9 ). The remaining predicted
negative chemicals (sodium benzoate, D-mannitol, acetaminophen, and
saccharin) were classified as negatives ( Fig. 4 A, Fig. S8 ). In 19 instances,
when chemicals were positive for the same endpoint in acute and
developmental exposure assays, depicted by yellow squares, the un -
derlying color represents the exposure regime that produced the most
sensitive behavior effect ( Fig. 4 A). For 18/19 instances, enhanced po -
tency was detected following developmental exposure, relative to the
acute exposure regime. This result is further illustrated when comparing
the most sensitive endpoint (MSE) for each chemical that was positive in
both assays. MSEs derived following developmental exposure were
typically greater than one order of magnitude lower than those identi -
fied in the acute VAMR assay ( Fig. 4 B).
3.5. The VAMR assay can add value to the DNT IVB
To evaluate the potential added value of the VAMR assay to the DNT
IVB, log10-AC50 MSEs obtained in the acute or developmental VAMR
assays were compared to log10-AC50 MSE values derived from the DNT
IVB ( Blum et al., 2023; Carstens et al., 2022 ) ( Fig. 5 A). As a predictive
measure of non-specific toxicity effects in zebrafish larvae, zebrafish
baseline toxicity values predicted to cause cell membrane disruption
were also included ( Klüver et al., 2019 ). For all compounds, measured
behavior effects occurred at concentrations that were orders of magni -
tude lower than the predicted baseline value. For three false negative
chemicals in the DNT IVB (nicotine, 5,5-diphenylhydantoin, maneb)
( Fig. 1 A), effects were only identified in the acute VAMR assay. Keta -
mine hydrochloride was tested here and in the European DNT IVB assays
( Blum et al., 2023 ) while L-ketamine hydrochloride was tested in the US
EPA DNT IVB assays ( Carstens et al., 2022 ). For these isomers, more
sensitive effects were determined in MEA assay endpoints, relative to the
measured behavior effects in the VAMR assay. For the eight other true
positive chemicals (BDE-99, chlorpyrifos, haloperidol, hexachloro -
phene, PFOA, tebuconazole, trichlorfon, triethyltin bromide), testing in
the VAMR NAM following developmental exposure resulted in 1–4 or -
ders of magnitude reduced log10-AC50 values as compared to acute
VAMR or DNT IVB assay data ( Fig. 5 A,B). When comparing MSE
log10-AC50 values across assays, this observation was significant
( Fig. 5 C). In contrast, there was no significant difference in potency
values between MSE values derived from the DNT IVB and the acute
VAMR assay ( Fig. 5 C). Finally, looking at overall hit concordance, seven
out of nine true positive chemicals were positive in the DNT IVB and
both acute and developmental VAMR assays. An additional three false
negatives in the DNT IVB were only positive following acute exposure in
the VAMR NAM ( Fig. 5 D).
4. Discussion
ECHA has recently stated that the development of NAMs for neuro -
toxicity testing is a key regulatory challenge ( European Chemicals
Agency, 2025 ). While the DNT IVB represents a promising alternative,
its use in a regulatory context is still pending, in part due to a series of
potential uncertainties associated with the test battery ( OECD, 2023 ).
One issue relates to a lack of biological coverage for key neuro -
developmental processes including myelination, blood-brain barrier
maturation, neuroinflammation, and neurotransmitter-based processes
( Bal-Price, 2018 ; OECD, 2023 ). In addition, cell-based strategies are
unable to account for potential chemical effects on complex behaviors
such as learning and memory, limiting comparability to OECD DNT
rodent-based test guidelines ( Bal-Price, 2018 ; Fritsche et al., 2015 ;
Masjosthusmann et al., 2020 ; OECD, 2008 ). The VAMR assay used in the
current study expands the widely used zebrafish photomotor response
J. Spath et al.                                                                                                                                                                                                                                    Neurotoxicology 114 (2026) 103414
7

Fig. 3. Estimated hit calls following acute or developmental exposure to chlorpyrifos. Curve fits for (A-D) acute and (E-H) developmental data depicted in Fig. 2
using the US EPA tcplfit2 pipeline ( Sheffield et al., 2022 ). The winning model is depicted in red. The blue line represents the AC50 value and the dashed line depicts
the point of departure. Hit calls, are defined as positive when the value is > 0.9. AC50, ACC estimates, and flags are also listed. ASR, acoustic startle response; BSL,
baseline motor activity; exp, exponential model; gls, gain loss model; IEI, inter-endpoints interval; pow, power model; VMR, visual motor response. n = 16 – 144.
J. Spath et al.                                                                                                                                                                                                                                    Neurotoxicology 114 (2026) 103414
8

assay (i.e., light-dark-transition assay) to additionally capture startle
responses, seizure-like behavior, learning, and memory-related end -
points ( Herold et al., 2025; Leuthold et al., 2025 ). To demonstrate its
potential added value to the DNT IVB, multiple strategies were
employed. The first approach aimed to determine whether the VAMR
assay enhanced battery sensitivity by assessing the neuroactive potential
of three ‘false negative ’ compounds in the DNT IVB. The second
approach compared potency estimates for nine ‘true positive ’ DNT
compounds to ask whether the VAMR assay increased potency detection.
In addition, five ‘predicted negatives ’ were evaluated to determine how
assay inclusion might affect battery selectivity.
4.1. Enhanced phenotypic coverage
The VAMR assay expands on the classical photomotor response assay
( Geier et al., 2018; Gutsfeld et al., 2024; Hagstrom et al., 2019; Irons
et al., 2010; Jarema et al., 2022a; Owen et al., 2025 ) to add acoustic
stimuli and endpoints that cover visual and acoustic startle responses,
Fig. 4. Patterns of general DNT-relevant activity using log10-AC50 metric ( μ M). (A) Non-hierarchical clustering of compound-specific profiles across the 26
endpoints is shown for all study chemicals including nine true positives (blue), three false negatives (green), and five predicted negatives (pink). Heatmap colors
represent log10-AC50 values following acute (red) or developmental (blue) exposure. Yellow squares indicate that a particular endpoint was a hit under both
exposure regimes. In those cases, the underlying red or blue shading was determined by the most sensitive assay. (B) Log10-AC50 values for the MSE following acute
or developmental exposure in the VAMR assay. ASH, acoustic startle habituation; ASR, acoustic startle response; BSL, baseline motor activity; dpf, day post
fertilization; IBI, inter-bout interval; IEI, inter-endpoints interval; ISI, inter-stimulus interval; MSE, most sensitive endpoint; VMR, visual motor response; VSR, visual
startle response; VSRB, visual startle response baseline.
J. Spath et al.                                                                                                                                                                                                                                    Neurotoxicology 114 (2026) 103414
9

habituation learning, potentiation of habituation, memory retention,
and activity measurements during typically quiescent periods ( Herold
et al., 2025; Leuthold et al., 2025 ). The extended phenotypic battery can
yield diverse and unique behavior profiles that are potentially related to
complex learning-related endpoints included in OECD guideline studies.
Altered habituation ( Rankin et al., 2009 ) is linked to N-methyl- -
D-aspartate receptor (NMDAR) antagonism in rhesus monkeys ( Paule
et al., 2011 ), rodents ( Lambot et al., 2016 ), and zebrafish ( Best et al.,
2008; Roberts et al., 2011, 2016; Zoodsma et al., 2020 ). As predicted,
acute exposure to ketamine hydrochloride, a prototypical NMDAR
antagonist ( Anis et al., 1983 ), blocked habituation learning, although
the effect was not observed following developmental exposure. Acute
exposure to trichlorfon also impaired habituation learning at the highest
test concentration and, following developmental exposure, inappro -
priate acceleration of habituation potentiation. This compound has not
been previously evaluated in rodent test guidelines but has been linked
to enhanced blood-brain barrier permeability in a catfish model
( Baldissera et al., 2019 ) and reduced cerebellar and cortical brain
weights in prenatally exposed guinea pigs ( Hjelde et al., 1998 ). Exposure
to nicotine, a nicotinic acetylcholine receptor (nAChR) agonist, also
impaired habituation learning in the acute, but not developmental,
VAMR assay. Interestingly, nicotine exposure has been previously re -
ported to enhance learning in adult animals ( Olausson et al., 2003;
Schildein et al., 2002 ), including zebrafish ( Eddins et al., 2009; Levin
et al., 2006 ). In contrast to ketamine hydrochloride, trichlorfon, and
nicotine, acute and developmental exposure to the pesticide tebucona -
zole inappropriately accelerated habituation learning, replicating pre -
vious work ( Rowson et al., 2025 ), although is not clear if these data
represent habituation learning according to previously defined criteria
( Rankin et al., 2009 ). Acute, but not developmental, exposure to maneb
also accelerated habituation learning although there were insufficient
no effect concentrations to fit this endpoint. This aligns with previous
work in adult rats showing that maneb exposure altered learning
( Chernoff et al., 1979; Sobotka et al., 1972 ). Finally, developmental
Fig. 5. The VAMR NAM increased assay sensitivity and potency detection relative to the DNT IVB. (A) Most sensitive (MSE) log10-AC50 values for the DNT
IVB and the acute and developmental VAMR assays. (B) Chemical-specific potency differences across the three assays. (C) Log10-AC50 MSE values for each assay.
Significance was determined using a Kruskal-Wallis test. (D) Hit concordance between the DNT IVB, acute VAMR assay, and developmental VAMR assay. DNT IVB
data are represented by yellow squares. Zebrafish data are depicted by red circles for the acute VAMR assay and blue diamonds for the developmental VAMR assay.
Zebrafish baseline toxicity predictions are represented by grey triangles.
J. Spath et al.                                                                                                                                                                                                                                    Neurotoxicology 114 (2026) 103414
10

exposure to haloperidol inappropriately accelerated habituation
learning. In addition to habituation learning, the VAMR assay contains a
second learning-related readout termed potentiation of habituation,
defined as a response decrement that becomes more rapid or pro -
nounced after multiple stimulus bouts ( Rankin et al., 2009 ). Acute
exposure to haloperidol or 5,5-diphenylhydantoin inappropriately
accelerated habituation potentiation, in line with previous work
showing reduced learning-related effects in rodents and humans
( Mccartney et al., 1999; Rosengarten and Quartermain, 2002; Scolnik,
1994; Weisenburger et al., 1990 ). Collectively, the higher phenotypic
coverage inherent in the VAMR NAM captures chemical effects on
complex behaviors, including learning-related behaviors with potential
relevance to higher order taxa, including humans.
4.2. Exposure window alters VAMR assay activity patterns
We previously showed that the VAMR NAM can identify novel
neuroactive chemicals following a short, 40 min exposure ( Herold et al.,
2025; Leuthold et al., 2025 ). To better understand whether acute effects
reflect a DNT-relevant endpoint, this study compared acute and devel -
opmental exposure regimes. Seven out of 12 DNT-positive reference
chemicals and four out of five predicted negatives were correctly clas -
sified in both the acute and developmental VAMR assays. This results in
a 65% hit call concordance when comparing the acute and develop -
mental VAMR assays. This is in line with network formation assay data
where 70.3% concordance between selective effects following acute
(60-min exposure) or developmental (0 – 12 days in vitro ) exposure was
observed for a 243 chemical test set ( Martin et al., 2024 ). Interestingly,
among the seven reference chemicals positive in acute and develop -
mental VAMR assays, five elicited a wider range of endpoint-specific hit
calls following acute exposure, relative to developmental exposure. In
contrast, exposure to trichlorfon resulted in more endpoint-specific hit
calls following the developmental exposure regime while the same
number of endpoint-specific hit calls were observed following acute and
developmental exposure to PFOA. Taken together, this supports the
concept that short-term, receptor-mediated neuroactivity effects are
reflected by a high degree of phenotypic diversity using
multi-behavioral testing ( Herold et al., 2025; Kokel and Peterson, 2011;
Leuthold et al., 2025 ).
From a directionality perspective, acute and developmental exposure
to four positive reference chemicals (haloperidol, tebuconazole, trie -
thyltin bromide, and trichlorfon) provoked behavior effects in the same
endpoints with the same directionality. In the case of locomotion-related
endpoints captured in the classic light-dark transition test, this was
consistent with previously published work ( F ´elix et al., 2017; Irons et al.,
2013; Rowson et al., 2025 ). Behavior effects provoked by chlorpyrifos
exposure was observed under both exposure paradigms but with oppo -
site directionality. Acute exposure was characterized by assay-wide
hyperactivity and developmental exposure resulted in widespread
hypoactivity. This confirms earlier work showing hyperactivity and
hypoactivity effects following acute or developmental exposure,
respectively, again in the light-dark transition test ( Jarema et al., 2015;
Jarema et al., 2022a, b ; Kienle et al., 2009 ; Rowson et al., 2025 ). In the
current study, 5,5-diphenylhydantoin was only active under acute
exposure conditions. Developmental exposure to this compound was
previously reported to alter behavior in zebrafish larvae ( Rowson et al.,
2025 ). In comparison to the single exposure at 1 dpf used here, this study
used a semi-static developmental exposure design characterized by two
exposures (0 and 3 dpf), followed by a 24 hr depuration before behavior
testing ( Jarema et al., 2022 ; Rowson et al., 2025 ). This may have
counteracted potential issues related to compound stability or meta -
bolism. Similar to 5,5-diphenylhydantoin, nicotine was also only active
following acute exposure. For this compound, discordant acute and
developmental behavior effects also likely stemmed from a lack of
compound stability ( Angevine et al., 2023 ). However, in this case, a
second, semi-static exposure did not result in appreciable behavior
effects ( Jarema et al., 2022 ; Petzold et al., 2009 ). Maneb was also only
active under the acute exposure condition. This is in line with previous
work showing that semi-static developmental exposure to maneb did not
provoke behavior effects ( Jarema et al., 2022 ). Similar to nicotine and 5,
5-diphenylhydantoin, this result may again be related to physicochem -
ical parameters ( Kubens et al., 2024 ) as this chemical required heat and
UV light to solubilize in DMSO, potentially affecting compound stability.
Finally, while ketamine hydrochloride was only a hit in the acute VAMR
assay, the highest concentration tested in the developmental VAMR
assay was significant relative to the control. This is consistent with
previous work showing alteration of swimming behavior in 5 dpf larvae
following acute, but not semi-static developmental, exposure to keta -
mine ( Tombari et al., 2023 ). Overall, and in line with previous work
( Von Wyl et al., 2023 ), for the 12 DNT reference chemicals evaluated
here, conservation of directionality was heterogenous across exposure
regimes.
4.3. Novel approach to derive potency estimates from zebrafish behavior-
based data
A critical requirement for increasing the relevance of zebrafish
behavioral data in risk assessment, and for enabling comparisons with
other experimental platforms such as the DNT IVB, is the ability to apply
concentration-response modeling to derive toxicologically meaningful
potency metrics. First, zebrafish behavioral time-series data needs to be
reduced to two-dimensions (i.e., response and concentration) ( Rowson
et al., 2025 ), in line with the EFSA recommendation to use benchmark
concentration (BMC) modeling ( EFSA Scientific Committee et al., 2022 ).
Several dimensionality reduction strategies have been proposed, specific
to light – dark transition assays, and incorporate assumptions about ste -
reotypical zebrafish swimming behavior ( Rowson et al., 2025; Thomas
et al., 2019 ). While these approaches produce biologically meaningful
results, they are coupled to specific behavior assay designs and corre -
sponding stereotypic movement patterns. In contrast, alternative
methods based on metrics such as area under the curve and movement
similarity indices avoid behavioral assumptions ( Hsieh et al., 2019 ).
These approaches generally do not include formal statistical compari -
sons between treatment and control groups. Here, we used an integra -
tive framework that combines statistical hypothesis testing and
dimensionality reduction within a single modeling approach, indepen -
dent of assay-specific behavioral assumptions. We previously reported
that generalized additive mixed-effects models (GAMMs) can capture
complex behavioral dynamics ( Gutsfeld et al., 2024; Owen et al., 2025 ).
Here, we demonstrated the flexibility of this approach by applying it to
the phenotypically complex VAMR assay. We further calculated Fr ´echet
distances between fitted model curves to derive direction-independent
inputs for concentration-response modeling. Using these distances as
the input for the established tcplfit2 pipeline ( Sheffield et al., 2022 )
aligned our approach with existing zebrafish modeling efforts ( Rowson
et al., 2025 ). However, to minimize 'false positives', we applied a more
stringent continuous hit-call threshold ( ≥ 0.9 vs > 0.8). Differences in
concentration – response outcomes are often driven less by modeling
strategy than by assay design, particularly vehicle control variability
and inter-experimental variability of responses ( Carstens et al., 2025 ). In
this study, we addressed these challenges by explicitly accounting for
control variability at the experimental-unit level. As a result, robust
concentration – response relationships were obtained across all 26
behavioral endpoints. This enabled the generation of comprehensive
behavioral profiles for each chemical, previously identified as a need in
zebrafish-based neurotoxicity screening ( Thomas et al., 2019 ). To our
knowledge, this study presents the first unified approach for time-series
zebrafish behavioral data that simultaneously supports statistical
inference and concentration-response modeling and yields concentra -
tion response metrics that are comparable to recent DNT IVB assess -
ments ( Carstens et al., 2025 ).
J. Spath et al.                                                                                                                                                                                                                                    Neurotoxicology 114 (2026) 103414
11

4.4. Assay potency values were lower in the developmental VAMR assay
Although the acute VAMR assay resulted in more diverse behavior
profiles, for the seven chemicals that were active following acute and
developmental exposure, all yielded potency values that were typically
1–3 orders of magnitude lower following developmental exposure. This
is in line with previous work using a network formation assay where,
among selective, concordant hits in both acute (60-min exposure) and
developmental (0–12 days in vitro) exposure modes, the majority of
median potency values were lower following developmental exposure
( Martin et al., 2024 ). Overall, enhanced potency detection has the po -
tential to align more closely with real-world human exposure levels,
lower testing costs, and ultimately, produce more protective estimated
effect concentrations.
4.5. The VAMR assay enhances sensitivity and potency detection of the
DNT IVB
The acute VAMR assay correctly classified 11 out of 12 predicted
positives, including three false negative chemicals missed by the cell-
based DNT IVB, and all predicted negative (5/5) compounds. For
these widely studied reference compounds, these data support the
concept that the addition of the acute VAMR assay to the DNT IVB may
have the potential to increase battery sensitivity without compromising
battery specificity. However, because these results were derived
following an acute, 40 min exposure, and likely reflect short-term, re -
ceptor-mediated effects ( Kokel and Peterson, 2011; Leuthold et al.,
2025; Owen et al., 2025 ), it is not clear whether behavior effects are
predictive of later developmental neurotoxicity outcomes. To evaluate
this, the same chemicals were assessed following a single developmental
exposure (1–5 dpf). As discussed previously, in the developmental
VAMR assay, the three false negative chemicals in the DNT IVB were also
negative. These discordant data may be related to unfavorable physi -
cochemical properties ( Angevine et al., 2023; Kubens et al., 2024 )
highlighting that the physicochemical applicability domains of the acute
and developmental VAMR assays likely vary. Future work should eval -
uate a wider chemical space to define the physicochemical applicability
domain ( Blum et al., 2025 ) of the acute and developmental VAMR as -
says. While the developmental VAMR assay failed to capture the three
false negative chemicals in the DNT IVB, for positive chemicals, effects
were identified at 1–4 orders of magnitude lower concentrations, rela -
tive to the DNT IVB. Enhanced potency detection is advantageous
because it will result in more protective estimated effect concentrations.
Regarding assay specificity, among the five predicted negative chem -
icals ( Martin et al., 2022 ) that were negative in the acute VAMR assay,
only developmental exposure to ibuprofen caused
concentration-dependent behavior effects. While this is in line with
previous work ( Islam et al., 2023 ), because there is a lack of in vivo test
guideline data for the predictive negatives, the ability to formally
evaluate assay specificity is limited ( Carstens et al., 2022, 2025; Martin
et al., 2024 ). Collectively, these findings demonstrate that acute and
developmental exposure paradigms are complementary in capturing a
broader spectrum of neurodevelopmental disruptions. To reduce
experimental load while retaining sensitivity to both transient and
persistent effects, future studies may benefit from implementing a
hybrid exposure design, such as a 24 h exposure, to simultaneously
capture developmental neurotoxicity outcomes and shorter-term neu -
roactivity disruptions during key windows of neurodevelopment ( EFSA
et al., 2024 ).
4.6. Remaining uncertainties for inclusion of the VAMR assay in the DNT
IVB
The DNT IVB contains uncertainties related to the lack of metabolic
activity and a potential failure to capture key neurodevelopmental mode
(s) of action ( OECD, 2023 ). A key consideration is the applicability
domain, or the ability of the battery to detect potential perturbations of
diverse neurodevelopmental pathways while enabling testing of com -
pounds with a wide range of physicochemical properties (OECD, GD 34).
As an alternative animal model, early life stage zebrafish contain a vast
array of potential cell, organ, and functional targets, by which DNT
chemicals can potentially disrupt neurodevelopment ( Tal et al., 2020 ).
This includes key modes of action that cellular assays are predicted to
miss such as thyroid hormone disruption and chemical effects on com -
plex neurodevelopmental behaviors such as learning and memory, all of
which are detectable in early life stage zebrafish ( Fagundes et al., 2024;
Herold et al., 2025; Leuthold et al., 2025; Van Dingenen et al., 2024 ).
While zebrafish contain a liver and gut microbiome, there are likely
toxicokinetic differences between zebrafish and humans that influence
chemical adsorption, distribution, metabolism, and elimination. Inter -
estingly, it was recently shown that zebrafish and human models form
the same toxic metabolite following exposure to acetaminophen and
that zebrafish are able to process testosterone similarly to humans, via
CYP3A4/5-like and UDP-glucuronosyltransferase-dependent meta -
bolism ( Chng et al., 2012 ). While zebrafish have been shown to contain a
complete range of cytochrome P450 genes ( Goldstone et al., 2010 ), they
do have differences in liver and hepatocyte structure ( Goessling and
Sadler, 2015 ). A more systematic assessment is needed on a wider
chemical space to understand to which extent species-specific metabolic
changes may compromise the ability of alternative models to predict
chemical effects. Finally, while the potential addition of zebrafish
behavior-based data to the DNT IVB might cover existing uncertainties
related to metabolic function and the mechanistic applicability domain,
there is still an absence of a strategy to combine and interpret data from
battery NAMs and a lack of determination of a minimum assay set
necessary to adequately predict DNT ( OECD, 2023 ).
Any discussion concerning added value will invariably hinge on the
definition of what constitutes a positive response. Recent DNT IVB pa -
pers have included battery metrics considering selective and non-
selective hits ( Blum et al., 2023; Carstens et al., 2022 ). While cell
death can be a DNT-relevant key event within an adverse outcome
pathway (AOP) ( Society of Advencement of AOPs, 2025 ), if this occurs
in the absence of preceding DNT process-based key events, it is likely not
indicative of a chemical that is specific for DNT. For subsets of the DNT
IVB, inclusion of cell death in hit calls resulted in 93% sensitivity (69%
specificity) ( Carstens et al., 2022 ) or 86% sensitivity (94% specificity)
( Blum et al., 2023 ). However, if only chemicals that are selective for
assay endpoints are included, sensitivity values decreased (68–74%)
and, at the same time, more stringent hit calls considerably benefited
calculated battery specificity values (92–100%) ( Blum et al., 2023;
Carstens et al., 2022 ). Assay performance metrics are also dependent on
criteria used for hit inclusion. For US EPA ToxCast analyses, concen -
tration response curves are required to exhibit two or fewer flags ( Paul
Friedman et al., 2020 ), and similar thresholds have been applied in EPA
DNT IVB studies, where criteria of less than three flags ( Carstens et al.,
2022; Martin et al., 2024 ) have been used. For tcpl v3.0 and later,
preliminary evaluations suggest that exclusion of curves with less than
four flags may be appropriate to filter out low-confidence curves
( Feshuk et al., 2023 ). Here, we applied a more conservative cutoff of
with less than two flags to maximize specificity. However, applying less
stringent criteria (e.g., fewer than four flags) would increase sensitivity
while compromising specificity. To ultimately use a NAM-based strategy
to predict DNT, assay or battery specificity should be prioritized. This
supports the use of selectivity filtering, which is implemented for some
of the DNT IVB assays ( Hoelting et al., 2016; Nyffeler, 2017 ). This is
particularly relevant for the comparison of DNT IVB and zebrafish
behavior-based data. Selectivity is inherent in zebrafish behavior data
because non-specific malformations confound behavior assessments and
malformed animals or those without a swim bladder are therefore
removed from downstream analyses ( Herold et al., 2025; Irons et al.,
2013; Jarema et al., 2015, 2022a,b; Leuthold et al., 2025 ; Owen et al.,
2025, 2025 ; Rericha et al., 2021 ).
J. Spath et al.                                                                                                                                                                                                                                    Neurotoxicology 114 (2026) 103414
12

5. Summary
In this study, we asked whether a next-generation visual and acoustic
motor response zebrafish assay can detect DNT effects in compounds
that were missed by in vitro DNT IVB assays. Three false negative
chemicals in the DNT IVB were correctly classified as hits in the VAMR
assay, but only following acute exposure. While inclusion of the VAMR
assay may have the potential to add value to the DNT IVB, more work is
needed to understand the relevance of acute neuroactivity effects in the
context of DNT potential. Relative to the DNT IVB, the VAMR assay
detected hits at lower potency values but this benefit was tempered by a
higher likelihood of misclassifying compounds under developmental
exposure conditions. Future work should optimize the exposure window
to potentially examine shorter developmental exposures to determine
whether assay sensitivity can be enhanced. The data generated here
covered a relatively small chemical set. Future work under the European
Partnership for Assessment of Risks from Chemicals will examine an 88-
chemical test set, with matching DNT IVB data ( Tal et al., 2024 ). This is
necessary to more conclusively understand whether the VAMR NAM
adds value to the DNT IVB.
Author agreement
All authors have seen and approved the final version of the manu -
script being submitted. They warrant that the article is the authors'
original work, hasn't received prior publication and isn't under consid -
eration for publication elsewhere. All authors have read the manuscript,
agree to its submission, and accept responsibility for manuscript
contents.
CRediT authorship contribution statement
Tamara Tal: Writing – review & editing, Writing – original draft,
Supervision, Project administration, Funding acquisition, Conceptuali -
zation. Stefan Scholz: Writing – review & editing, Data curation.
Sebastian Gutsfeld: Writing – review & editing, Writing – original
draft, Supervision, Project administration, Methodology, Funding
acquisition, Conceptualization. Jana Raab: Writing – review & editing,
Visualization, Validation, Methodology, Investigation, Formal analysis,
Data curation. Jana Schor: Writing – review & editing, Methodology.
Julia Spath: Writing – review & editing, Writing – original draft,
Visualization, Validation, Methodology, Investigation, Formal analysis,
Data curation.
Funding
This work was funded by a W2 Helmholtz Association Grant to T. Tal
and a Transfun grant, funded by the UFZ Technology Transfer Office, to
S. Gutsfeld and T. Tal. This work was carried out in the framework of the
European Partnership for the Assessment of Risks from Chemicals
(PARC) and has received funding from the European Union ’ s Horizon
Europe research and innovation programme under Grant Agreement No
101057014. We gratefully acknowledge access to the platform CITEPro
(Chemicals in the Environment Profiler) funded by the Helmholtz
Association.
Declaration of generative AI and AI-assisted technologies in the
manuscript preparation process
During the preparation of this work, claude.ai (Sonnet 4.5)/PyCharm
AI assistant was used for debugging and refinement of code developed
by JR and JS. Refined code was deeply reviewed. The authors take full
responsibility for the content of the published code and article.
Declaration of Competing Interest
The authors declare the following financial interests/personal re -
lationships which may be considered as potential competing interests:
This work was funded by a W2 Helmholtz Association Grant to T. Tal
and a Transfun grant, funded by the UFZ Technology Transfer Office, to
S. Gutsfeld and T. Tal. This work was carried out in the framework of the
European Partnership for the Assessment of Risks from Chemicals
(PARC) and has received funding from the European Union ’ s Horizon
Europe research and innovation programme under Grant Agreement No
101057014. We gratefully acknowledge access to the platform CITEPro
(Chemicals in the Environment Profiler) funded by the Helmholtz As -
sociation. There are no conflicts of interest to disclose.
Acknowledgments
We thank Nicole Schweiger and Tim Jonat for UFZ fish husbandry.
We acknowledge Nadia Herold for training Julia Spath to perform
zebrafish-based experiments. Fig. 1 was partially created using
BioRender.
Appendix A. Supporting information
Supplementary data associated with this article can be found in the
online version at doi:10.1016/j.neuro.2026.103414 .
Data availability
All underlying data are available via DOI: 10.5281/zen -
odo.17937513 (will be made public upon manuscript acceptance).
References
Angevine, D.J., Camacho, K.J., Zhang, X., Rzayev, J., Benedict, J.B., 2023. Enhancing the
Stability of Nicotine via Crystallization Using Enantiopure Tartaric Acid Salt
Formers. ACS Omega 8 (17), 15535 – 15542. https://doi.org/10.1021/
acsomega.3c00849 .
Anis, N.A., Berry, S.C., Burton, N.R., Lodge, D., 1983. The dissociative anaesthetics,
ketamine and phencyclidine, selectively reduce excitation of central mammalian
neurones by N-methyl-aspartate. Br. J. Pharmacol. 79 (2), 565 – 575. https://doi.org/
10.1111/j.1476-5381.1983.tb11031.x .
Aschner, M., 2016. Reference compounds for alternative test methods to indicate
developmental neurotoxicity (DNT) potential of chemicals: Example lists and criteria
for their selection and use. ALTEX. https://doi.org/10.14573/altex.1604201 .
Baldissera, M.D., Souza, C.F., Descovi, S.N., Zanella, R., Prestes, O.D., Da Silva, A.S.,
Baldisserotto, B., 2019. Organophosphate pesticide trichlorfon induced neurotoxic
effects in freshwater silver catfish Rhamdia quelen via disruption of blood-brain
barrier: Implications on oxidative status, cell viability and brain neurotransmitters.
Comparative Biochemistry Physiology Part C Toxicology & Pharmacology 218,
8 – 13. https://doi.org/10.1016/j.cbpc.2018.12.006 .
Bal-Price, A., 2018a. Recommendation on test readiness criteria for new approach
methods in toxicology: Exemplified for developmental neurotoxicity. ALTEX
306 – 352. https://doi.org/10.14573/altex.1712081 .
Bennett, D., Bellinger, D.C., Birnbaum, L.S., DABT, A.T.S., Bradman, A., Chen, A., Cory-
Slechta, D.A., Engel, S.M., Fallin, M.D., Halladay, A., Hauser, R., Hertz-Picciotto, I.,
Kwiatkowski, C.F., Lanphear, B.P., Marquez, E., Marty, M., McPartland, J.,
Newschaffer, C.J., National Medical Association, 2016. Project TENDR: targeting
environmental neuro-developmental risks The TENDR consensus statement. Environ.
Health Perspect. 124 (7). https://doi.org/10.1289/EHP358 .
Best, J.D., Berghmans, S., Hunt, J.J.F.G., Clarke, S.C., Fleming, A., Goldsmith, P.,
Roach, A.G., 2008a. Non-Associative learning in Larval Zebrafish. Article 5.
Neuropsychopharmacology 33 (5). https://doi.org/10.1038/sj.npp.1301489 .
Blum, J., Bartmann, K., De Paula Souza, J., Fritsche, E., 2025. Developmental
neurotoxicity as a case example for a six-step framework for the sustainable
regulatory implementation of NAMs. Curr. Opin. Toxicol. 42, 100528. https://doi.
org/10.1016/j.cotox.2025.100528 .
Blum, J., Masjosthusmann, S., Bartmann, K., Bendt, F., Dolde, X., D ¨onmez, A., F ¨orster, N.,
Holzer, A.-K., Hübenthal, U., Ke ß el, H.E., Kilic, S., Klose, J., Pahl, M., Stürzl, L.-C.,
Mangas, I., Terron, A., Crofton, K.M., Scholze, M., Mosig, A., Fritsche, E., 2023.
Establishment of a human cell-based in vitro battery to assess developmental
neurotoxicity hazard of chemicals. Chemosphere 311, 137035. https://doi.org/
10.1016/j.chemosphere.2022.137035 .
Bruni, G., Rennekamp, A.J., Velenich, A., McCarroll, M., Gendelev, L., Fertsch, E.,
Taylor, J., Lakhani, P., Lensen, D., Evron, T., Lorello, P.J., Huang, X.-P.,
Kolczewski, S., Carey, G., Caldarone, B.J., Prinssen, E., Roth, B.L., Keiser, M.J.,
Peterson, R.T., Kokel, D., 2016. Zebrafish behavioral profiling identifies multitarget
J. Spath et al.                                                                                                                                                                                                                                    Neurotoxicology 114 (2026) 103414
13

antipsychotic-like compounds. Nat. Chem. Biol. 12 (7), 559 – 566. https://doi.org/
10.1038/nchembio.2097 .
Carstens, K.E., Carpenter, A.F., Martin, M.M., Harrill, J.A., Shafer, T.J., Paul
Friedman, K., 2022. Integrating Data From In Vitro New Approach Methodologies for
Developmental Neurotoxicity. Article 1. Toxicol. Sci. 187 (1). https://doi.org/
10.1093/toxsci/kfac018 .
Carstens, K.E., D ¨onmez, A., Hsieh, J.-H., Bartmann, K., Friedman, K.P., Koch, K.,
Scholze, M., Fritsche, E., 2025. A comparative study of biostatistical pipelines for
benchmark concentration modeling of in vitro screening assays. Comput. Toxicol.
34, 100360. https://doi.org/10.1016/j.comtox.2025.100360 .
Cassar, S., Adatto, I., Freeman, J.L., Gamse, J.T., Iturria, I., Lawrence, C., Muriana, A.,
Peterson, R.T., Van Cruchten, S., Zon, L.I., 2020. Use of Zebrafish in Drug Discovery
Toxicology. Chem. Res. Toxicol. 33 (1), 95 – 118. https://doi.org/10.1021/acs.
chemrestox.9b00335 .
Chernoff, N., Kavlock, R.J., Rogers, E.H., Carver, B.D., Murray, S., 1979. Perinatal
toxicity of maneb, ethylene thiourea, and ethylenebisisothiocyanate sulfide in
rodents. J. Toxicol. Environ. Health 5 (5), 821 – 834. https://doi.org/10.1080/
15287397909529792 .
Chng, H.T., Ho, H.K., Yap, C.W., Lam, S.H., Chan, E.C.Y., 2012. An Investigation of the
Bioactivation Potential and Metabolism Profile of Zebrafish versus Human. SLAS
Discov. 17 (7), 974 – 986. https://doi.org/10.1177/1087057112447305 .
Crofton, K., 2010. Developmental neurotoxicity testing: Recommendations for
developing alternative methods for the screening and prioritization of chemicals.
ALTEX 9 – 15. https://doi.org/10.14573/altex.2011.1.009 .
Crofton, K.M., Mundy, W.R., 2021. External Scientific Report on the Interpretation of
Data from the Developmental Neurotoxicity In Vitro Testing Assays for Use in
Integrated Approaches for Testing and Assessment. EFSA Support. Publ. 18 (10).
https://doi.org/10.2903/sp.efsa.2021.EN-6924 .
Crofton, K.M., Paparella, M., Price, A., Mangas, I., Martino, L., Terron, A., Hern ´andez-
Jerez, A., EFSA (European Food Safety Authority), 2024. A developmental
neurotoxicity adverse outcome pathway (DNT-AOP) with voltage gate sodium
channel (VGSC) inhibition as a molecular initiating event (MiE). EFSA J 22 (8).
https://doi.org/10.2903/j.efsa.2024.8954 .
Dalsager, L., Fage-Larsen, B., Bilenberg, N., Jensen, T.K., Nielsen, F., Kyhl, H.B.,
Grandjean, P., Andersen, H.R., 2019. Maternal urinary concentrations of pyrethroid
and chlorpyrifos metabolites and attention deficit hyperactivity disorder (ADHD)
symptoms in 2-4-year-old children from the Odense Child Cohort. Environ. Res. 176,
108533. https://doi.org/10.1016/j.envres.2019.108533 .
Eddins, D., Petro, A., Williams, P., Cerutti, D.T., Levin, E.D., 2009. Nicotine effects on
learning in zebrafish: The role of dopaminergic systems. Psychopharmacology 202
(1 – 3), 103 – 109. https://doi.org/10.1007/s00213-008-1287-4 .
EFSA Scientific Committee, More, S.J., Bampidis, V., Benford, D., Bragard, C.,
Halldorsson, T.I., Hern ´andez-Jerez, A.F., Bennekou, S.H., Koutsoumanis, K.,
Lambr ´e, C., Machera, K., Mennes, W., Mullins, E., Nielsen, S.S., Schrenk, D.,
Turck, D., Younes, M., Aerts, M., Edler, L., Schlatter, J., 2022. Guidance on the use of
the benchmark dose approach in risk assessment. EFSA J 20 (10). https://doi.org/
10.2903/j.efsa.2022.7584 .
European Chemicals Agency, 2025. Key areas of regulatory challenge. Publications
Office https://data.europa.eu/doi/10.2823/8572710 .
Fagundes, T., Pannetier, P., G ¨olz, L., Behnstedt, L., Morthorst, J., Vergauwen, L.,
Knapen, D., Holbech, H., Braunbeck, T., Baumann, L., 2024. The generation gap in
endocrine disruption: Can the integrated fish endocrine disruptor test (iFEDT) bridge
the gap by assessing intergenerational effects of thyroid hormone system disruption?
Aquatic Toxicology (Amsterdam Netherlands) 272, 106969. https://doi.org/
10.1016/j.aquatox.2024.106969 .
F ´elix, L.M., Antunes, L.M., Coimbra, A.M., Valentim, A.M., 2017. Behavioral alterations
of zebrafish larvae after early embryonic exposure to ketamine. Article 4.
Psychopharmacology 234 (4). https://doi.org/10.1007/s00213-016-4491-7 .
Feshuk, M., Kolaczkowski, L., Watford, S., Paul Friedman, K., 2023. ToxRefDB v2.1:
Update to curated in vivo study data in the Toxicity Reference Database. Front.
Toxicol. 5, 1260305. https://doi.org/10.3389/ftox.2023.1260305 .
Fritsche, E., Alm, H., Baumann, J., Geerts, L., Håkansson, H., Masjosthusmann, S.,
Witters, H., 2015. Literature review on in vitro and alternative Developmental
Neurotoxicity (DNT) testing methods. EFSA Support. Publ. 12 (4). https://doi.org/
10.2903/sp.efsa.2015.EN-778 .
Gaballah, S., Swank, A., Sobus, J.R., Howey, X.M., Schmid, J., Catron, T., McCord, J.,
Hines, E., Strynar, M., Tal, T., 2020. Evaluation of Developmental Toxicity,
Developmental Neurotoxicity, and Tissue Dose in Zebrafish Exposed to GenX and
Other PFAS. Environ. Health Perspect. 128 (4), 047005. https://doi.org/10.1289/
EHP5843 .
Geier, M.C., James Minick, D., Truong, L., Tilton, S., Pande, P., Anderson, K.A.,
Teeguardan, J., Tanguay, R.L., 2018. Systematic developmental neurotoxicity
assessment of a representative PAH Superfund mixture using zebrafish. Toxicol.
Appl. Pharmacol. 354, 115 – 125. https://doi.org/10.1016/j.taap.2018.03.029 .
Genolini, C., 2009. Longitud. Longitud. Data (S. 2. 4. 7) [Dataset]. https://doi.org/
10.32614/CRAN.package.longitudinalData .
Goessling, W., Sadler, K.C., 2015. Zebrafish: An Important Tool for Liver Disease
Research. Gastroenterology 149 (6), 1361 – 1377. https://doi.org/10.1053/j.
gastro.2015.08.034 .
Goldstone, J.V., McArthur, A.G., Kubota, A., Zanette, J., Parente, T., J ¨onsson, M.E.,
Nelson, D.R., Stegeman, J.J., 2010. Identification and developmental expression of
the full complement of Cytochrome P450 genes in Zebrafish. BMC Genom. 11 (1),
643. https://doi.org/10.1186/1471-2164-11-643 .
Grandjean, P., Landrigan, P.J., 2014. Neurobehavioural effects of developmental
toxicity. Lancet Neurol. 13 (3), 330 – 338. https://doi.org/10.1016/S1474-4422(13)
70278-3 .
Gutsfeld, S. (2024). Analysis of Zebrafish Swimming Behavior Data using Mixed Effects
Modelling: Used in: Investigation of peroxisome proliferator-activated receptor
genes as requirements for visual startle response hyperactivity in larval zebrafish
exposed to structurally similar Per- and Polyfluoroalkyl Substances (PFAS) (Version
v0.1) [Software]. Zenodo. https://doi.org/10.5281/ZENODO.11396730.
Gutsfeld, S., Wehmas, L., Omoyeni, I., Schweiger, N., Leuthold, D., Michaelis, P.,
Howey, X.M., Gaballah, S., Herold, N., Vogs, C., Wood, C., Bertotto, L., Wu, G.-M.,
Klüver, N., Busch, W., Scholz, S., Schor, J., Tal, T., 2024. Investigation of Peroxisome
Proliferator-Activated Receptor Genes as Requirements for Visual Startle Response
Hyperactivity in Larval Zebrafish Exposed to Structurally Similar Per- and
Polyfluoroalkyl Substances (PFAS). Article 7. Environ. Health Perspect. 132 (7).
https://doi.org/10.1289/EHP13667 .
Hagstrom, D., Truong, L., Zhang, S., Tanguay, R., Collins, E.-M.S., 2019. Comparative
analysis of zebrafish and planarian model systems for developmental neurotoxicity
screens using an 87-compound library. Article 1. Toxicol. Sci. 167 (1). https://doi.
org/10.1093/toxsci/kfy180 .
Herold, N.K., Gutsfeld, S., Leuthold, D., Wray, C., Spath, J., Tal, T., 2025. Multi-
behavioral fingerprints can identify potential modes of action for neuroactive
environmental chemicals. NeuroToxicology 108, 377 – 399. https://doi.org/
10.1016/j.neuro.2025.05.001 .
Hjelde, T., Mehl, A., Schanke, T.M., Fonnumb, F., 1998. Teratogenic effects of trichlorfon
(Metrifonate) on the guinea-pig brain. Determination of the effective dose and the
sensitive period. Neurochem. Int. 32 (5 – 6), 469 – 477. https://doi.org/10.1016/
S0197-0186(97)00125-3 .
Hoelting, L., Klima, S., Karreman, C., Grinberg, M., Meisig, J., Henry, M., Rotshteyn, T.,
Rahnenführer, J., Blüthgen, N., Sachinidis, A., Waldmann, T., Leist, M., 2016. Stem
Cell-Derived Immature Human Dorsal Root Ganglia Neurons to Identify Peripheral
Neurotoxicants. Stem Cells Transl. Med. 5 (4), 476 – 487. https://doi.org/10.5966/
sctm.2015-0108 .
Horzmann, K.A., Freeman, J.L., 2016. Zebrafish Get Connected: Investigating
Neurotransmission Targets and Alterations in Chemical Toxicity. Toxics 4 (3), 19.
https://doi.org/10.3390/toxics4030019 .
Howe, K., Clark, M.D., Torroja, C.F., Torrance, J., Berthelot, C., Muffato, M., Collins, J.E.,
Humphray, S., McLaren, K., Matthews, L., McLaren, S., Sealy, I., Caccamo, M.,
Churcher, C., Scott, C., Barrett, J.C., Koch, R., Rauch, G.-J., White, S., Stemple, D.L.,
2013. The zebrafish reference genome sequence and its relationship to the human
genome. Nature 496 (7446), 498 – 503. https://doi.org/10.1038/nature12111 .
Hsieh, J.-H., Ryan, K., Sedykh, A., Lin, J.-A., Shapiro, A.J., Parham, F., Behl, M., 2019.
Application of Benchmark Concentration (BMC) Analysis on Zebrafish Data: A New
Perspective for Quantifying Toxicity in Alternative Animal Models. Toxicol. Sci. 167
(1), 92 – 104. https://doi.org/10.1093/toxsci/kfy258 .
Irons, T.D., Kelly, P.E., Hunter, D.L., Macphail, R.C., Padilla, S., 2013. Acute
administration of dopaminergic drugs has differential effects on locomotion in larval
zebrafish. Article 4. Pharmacol. Biochem. Behav. 103 (4). https://doi.org/10.1016/j.
pbb.2012.12.010 .
Irons, T.D., MacPhail, R.C., Hunter, D.L., Padilla, S., 2010. Acute neuroactive drug
exposures alter locomotor activity in larval zebrafish. Neurotoxicology Teratol. 32
(1), 84 – 90. https://doi.org/10.1016/j.ntt.2009.04.066 .
Islam, M.A., Lopes, I., Domingues, I., Silva, D.C.V.R., Blasco, J., Pereira, J.L., Araújo, C.V.
M., 2023. Behavioural, developmental and biochemical effects in zebrafish caused
by ibuprofen, irgarol and terbuthylazine. Chemosphere 344, 140373. https://doi.
org/10.1016/j.chemosphere.2023.140373 .
Jarema, K.A., Hunter, D.L., Hill, B.N., Olin, J.K., Britton, K.N., Waalkes, M.R., Padilla, S.,
2022a. Developmental Neurotoxicity and Behavioral Screening in Larval Zebrafish
with a Comparison to Other Published Results. Article 5. Toxics 10 (5). https://doi.
org/10.3390/toxics10050256 .
Jarema, K.A., Hunter, D.L., Hill, B.N., Olin, J.K., Britton, K.N., Waalkes, M.R., Padilla, S.,
2022b. Developmental Neurotoxicity and Behavioral Screening in Larval Zebrafish
with a Comparison to Other Published Results. Toxics 10 (5), 256. https://doi.org/
10.3390/toxics10050256 .
Jarema, K.A., Hunter, D.L., Shaffer, R.M., Behl, M., Padilla, S., 2015. Acute and
developmental behavioral effects of flame retardants and related chemicals in
zebrafish. Neurotoxicology Teratol. 52, 194 – 209. https://doi.org/10.1016/j.
ntt.2015.08.010 .
Juberg, D.R., Fox, D.A., Forcelli, P.A., Kacew, S., Lipscomb, J.C., Saghir, S.A., Sherwin, C.
M., Koenig, C.M., Hays, S.M., Kirman, C.R., 2023. A perspective on In vitro
developmental neurotoxicity test assay results: An expert panel review. Regul.
Toxicol. Pharmacol. 143, 105444. https://doi.org/10.1016/j.yrtph.2023.105444 .
Kienle, C., K ¨ohler, H.-R., Gerhardt, A., 2009. Behavioural and developmental toxicity of
chlorpyrifos and nickel chloride to zebrafish (Danio rerio) embryos and larvae.
Ecotoxicol. Environ. Saf. 72 (6), 1740 – 1747. https://doi.org/10.1016/j.
ecoenv.2009.04.014 .
Kimmel, C.B., Ballard, W.W., Kimmel, S.R., Ullmann, B., Schilling, T.F., 1995. Stages of
embryonic development of the zebrafish. Dev. Dyn. 203 (3). https://doi.org/
10.1002/aja.1002030302 . Article 3.
Klüver, N., Bittermann, K., Escher, B.I., 2019. QSAR for baseline toxicity and
classification of specific modes of action of ionizable organic chemicals in the
zebrafish embryo toxicity test. Aquat. Toxicol. 207, 110 – 119. https://doi.org/
10.1016/j.aquatox.2018.12.003 .
Kokel, D., Peterson, R.T., 2011. Using the zebrafish photomotor response for
psychotropic drug screening. Methods Cell Biol. 105, 517 – 524. https://doi.org/
10.1016/B978-0-12-381320-6.00022-9 .
Kubens, L., Weishaupt, A.-K., Michaelis, V., Rohn, I., Mohr, F., Bornhorst, J., 2024.
Exposure to the environmentally relevant fungicide Maneb: Studying toxicity in the
soil nematode Caenorhabditis elegans. Environ. Int. 183, 108372. https://doi.org/
10.1016/j.envint.2023.108372 .
J. Spath et al.                                                                                                                                                                                                                                    Neurotoxicology 114 (2026) 103414
14

Lambot, L., Chaves Rodriguez, E., Houtteman, D., Li, Y., Schiffmann, S.N., Gall, D., De
Kerchove d ’ Exaerde, A., 2016. Striatopallidal Neuron NMDA Receptors Control
Synaptic Connectivity, Locomotor, and Goal-Directed Behaviors. J. Neurosci. 36
(18), 4976 – 4992. https://doi.org/10.1523/JNEUROSCI.2717-15.2016 .
L ´egar ´e, A., Lemieux, M., Boily, V., Poulin, S., L ´egar ´e, A., Desrosiers, P., De Koninck, P.,
2025. Structural and genetic determinants of zebrafish functional brain networks.
Sci. Adv. 11 (28), eadv7576. https://doi.org/10.1126/sciadv.adv7576 .
Lenth, R., & Piaskowksi, J. (2025). emmeans: Estimated Marginal Means, aka Least-
Squares Means (Version R package version 2.0.0) [Dataset]. 〈 https://rvlenth.github.
io/emmeans/ 〉 .
Leuthold, D., Herold, N.K., Nerlich, J., Bartmann, K., Scharkin, I., Hallermann, S.J.,
Schweiger, N., Fritsche, E., Tal, T., 2025. Multi-behavioral phenotyping in early-life-
stage zebrafish for identifying disruptors of non-associative learning. Environ.
Health Perspect., EHP16568 https://doi.org/10.1289/EHP16568 .
Levin, E.D., Limpuangthip, J., Rachakonda, T., Peterson, M., 2006. Timing of nicotine
effects on learning in zebrafish. Psychopharmacology 184 (3 – 4), 547 – 552. https://
doi.org/10.1007/s00213-005-0162-9 .
Lloyd, D.R., Medina, D.J., Hawk, L.W., Fosco, W.D., Richards, J.B., 2014. Habituation of
reinforcer effectiveness. Front. Integr. Neurosci. 7. https://doi.org/10.3389/
fnint.2013.00107 .
Lyall, K., Croen, Lisa A., Sj ¨odin, A., Yoshida, C.K., Zerbo, O., Kharrazi, M., Windham, G.
C., 2017. Polychlorinated Biphenyl and Organochlorine Pesticide Concentrations in
Maternal Mid-Pregnancy Serum Samples: Association with Autism Spectrum
Disorder and Intellectual Disability. Environ. Health Perspect. 125 (3), 474 – 480.
https://doi.org/10.1289/EHP277 .
Makris, S.L., Raffaele, K., Allen, S., Bowers, W.J., Hass, U., Alleva, E., Calamandrei, G.,
Sheets, L., Amcoff, P., Delrue, N., Crofton, K.M., 2009. A Retrospective Performance
Assessment of the Developmental Neurotoxicity Study in Support of OECD Test
Guideline 426. Environ. Health Perspect. 117 (1), 17 – 25. https://doi.org/10.1289/
ehp.11447 .
Martin, M.M., Baker, N.C., Boyes, W.K., Carstens, K.E., Culbreth, M.E., Gilbert, M.E.,
Harrill, J.A., Nyffeler, J., Padilla, S., Friedman, K.P., Shafer, T.J., 2022. An expert-
driven literature review of “ negative ” chemicals for developmental neurotoxicity
(DNT) in vitro assay evaluation. Neurotoxicology Teratol. 93, 107117. https://doi.
org/10.1016/j.ntt.2022.107117 .
Martin, M.M., Carpenter, A.F., Shafer, T.J., Paul Friedman, K., Carstens, K.E., 2024.
Chemical effects on neural network activity: Comparison of acute versus network
formation exposure in microelectrode array assays. Toxicology 505, 153842.
https://doi.org/10.1016/j.tox.2024.153842 .
Masjosthusmann, S., Blum, J., Bartmann, K., Dolde, X., Holzer, A., Stürzl, L., Ke ß el, E.H.,
F ¨orster, N., D ¨onmez, A., Klose, J., Pahl, M., Waldmann, T., Bendt, F., Kisitu, J.,
Suciu, I., Hübenthal, U., Mosig, A., Leist, M., Fritsche, E., 2020. Establishment of an a
priori protocol for the implementation and interpretation of an in-vitro testing
battery for the assessment of developmental neurotoxicity. EFSA Support. Publ. 17
(10). https://doi.org/10.2903/sp.efsa.2020.EN-1938 .
McAtee, D., Abdelmoneim, A., 2024. A zebrafish-based acoustic motor response (AMR)
assay to evaluate chemical-induced developmental neurotoxicity. NeuroToxicology
103, 60 – 70. https://doi.org/10.1016/j.neuro.2024.06.003 .
Mccartney, M.A., Scinto, P.L., Wang, S.-S., Altan, S., 1999. Developmental Effects of
Phenytoin May Differ Depending on Sex of Offspring. Neurotoxicology Teratol. 21
(2), 119 – 128. https://doi.org/10.1016/S0892-0362(98)00047-6 .
Mundy, W.R., Crofton, K.M., 2024a. Recommended DNT Reference Chemical Test Set For
In Vitro Assay Development*. EFSA Support. Publ. 21 (12). https://doi.org/
10.2903/sp.efsa.2024.EN-9175 .
Nyffeler, J., 2017. Design of a high-throughput human neural crest cell migration assay
to indicate potential developmental toxicants. ALTEX 75 – 94. https://doi.org/
10.14573/altex.1605031 .
OECD, 2007. Test No. 426: Developmental Neurotoxicity Study. OECD. https://doi.org/
10.1787/9789264067394-en .
OECD, 2008. Test No. 407: Repeated Dose 28-day Oral Toxicity Study in Rodents. OECD.
https://doi.org/10.1787/9789264070684-en .
OECD, 2023a. Initial recommendations on evaluation of data from the developmental
neurotoxicity (DNT) in-vitro testing battery (No. 13). Ser. Test. Assess. 377 (13). Article
13. 〈 https://www.oecd.org/env/ehs/testing/developmental-neurotoxicity.htm 〉 .
OECD, 2025. Test No. 443: Extended One-Generation Reproductive Toxicity Study.
OECD Publishing. https://doi.org/10.1787/9789264185371-en .
Olausson, P., Jentsch, J.D., Taylor, J.R., 2003. Repeated Nicotine Exposure Enhances
Reward-Related Learning in the Rat. Neuropsychopharmacology 28 (7), 1264 – 1271.
https://doi.org/10.1038/sj.npp.1300173 .
Owen, R., De Macedo, G., Nerlich, J., Scharkin, I., Bartmann, K., D ¨obler, J.,
Engelmann, B., Rolle-Kampczyk, U.E., Leuthold, D., Gutsfeld, S., Schweiger, N.,
Tal, T., 2025. Perfluorooctanesulfonic acid (PFOS) antagonizes gamma-
aminobutyric acid (GABA) receptors in larval zebrafish and mammalian models.
Toxicol. Sci. 207 (2), 449 – 466. https://doi.org/10.1093/toxsci/kfaf101 .
Pallocca, G., 2022. Next-generation risk assessment of chemicals – Rolling out a human-
centric testing strategy to drive 3R implementation: The RISK-HUNT3R project
perspective. ALTEX. https://doi.org/10.14573/altex.2204051 .
Panula, P., Chen, Y.-C., Priyadarshini, M., Kudo, H., Semenova, S., Sundvik, M.,
Sallinen, V., 2010. The comparative neuroanatomy and neurochemistry of zebrafish
CNS systems of relevance to human neuropsychiatric diseases. Neurobiol. Dis. 40
(1), 46 – 57. https://doi.org/10.1016/j.nbd.2010.05.010 .
Paul Friedman, K., Gagne, M., Loo, L.-H., Karamertzanis, P., Netzeva, T., Sobanski, T.,
Franzosa, J.A., Richard, A.M., Lougee, R.R., Gissi, A., Lee, J.-Y.J., Angrish, M.,
Dorne, J.L., Foster, S., Raffaele, K., Bahadori, T., Gwinn, M.R., Lambert, J.,
Whelan, M., Thomas, R.S., 2020. Utility of In Vitro Bioactivity as a Lower Bound
Estimate of In Vivo Adverse Effect Levels and in Risk-Based Prioritization. Toxicol.
Sci. 173 (1), 202 – 225. https://doi.org/10.1093/toxsci/kfz201 .
Paule, M.G., Li, M., Allen, R.R., Liu, F., Zou, X., Hotchkiss, C., Hanig, J.P., Patterson, T.A.,
Slikker, W., Wang, C., 2011. Ketamine anesthesia during the first week of life can
cause long-lasting cognitive deficits in rhesus monkeys. Neurotoxicology Teratol. 33
(2), 220 – 230. https://doi.org/10.1016/j.ntt.2011.01.001 .
Petzold, A.M., Balciunas, D., Sivasubbu, S., Clark, K.J., Bedell, V.M., Westcot, S.E.,
Myers, S.R., Moulder, G.L., Thomas, M.J., Ekker, S.C., 2009. Nicotine response
genetics in the zebrafish. Proc. Natl. Acad. Sci. 106 (44), 18662 – 18667. https://doi.
org/10.1073/pnas.0908247106 .
Pistollato, F., de Gyves, E.M., Carpi, D., Bopp, S.K., Nunes, C., Worth, A., Bal-Price, A.,
2020. Assessment of developmental neurotoxicity induced by chemical mixtures
using an adverse outcome pathway concept. Environmental Health A Global Access
Science Source 19 (1), 23. https://doi.org/10.1186/s12940-020-00578-x .
Rankin, C.H., Abrams, T., Barry, R.J., Bhatnagar, S., Clayton, D.F., Colombo, J.,
Coppola, G., Geyer, M.A., Glanzman, D.L., Marsland, S., McSweeney, F.K., Wilson, D.
A., Wu, C.-F., Thompson, R.F., 2009. Habituation revisited: An updated and revised
description of the behavioral characteristics of habituation. Neurobiol. Learn. Mem.
92 (2), 135 – 138. https://doi.org/10.1016/j.nlm.2008.09.012 .
Rericha, Y., Cao, D., Truong, L., Simonich, M., Field, J.A., Tanguay, R.L., 2021. Behavior
Effects of Structurally Diverse Per- and Polyfluoroalkyl Substances in Zebrafish.
Chem. Res. Toxicol. 34 (6), 1409 – 1416. https://doi.org/10.1021/acs.
chemrestox.1c00101 .
Roberts, A.C., Pearce, K.C., Choe, R.C., Alzagatiti, J.B., Yeung, A.K., Bill, B.R.,
Glanzman, D.L., 2016. Long-term habituation of the C-start escape response in
zebrafish larvae. Neurobiol. Learn. Mem. 134, 360 – 368. https://doi.org/10.1016/j.
nlm.2016.08.014 .
Roberts, A.C., Reichl, J., Song, M.Y., Dearinger, A.D., Moridzadeh, N., Lu, E.D.,
Pearce, K., Esdin, J., Glanzman, D.L., 2011. Habituation of the C-Start Response in
Larval Zebrafish Exhibits Several Distinct Phases and Sensitivity to NMDA Receptor
Blockade. PLoS ONE 6 (12), e29132. https://doi.org/10.1371/journal.
pone.0029132 .
Rosengarten, H., Quartermain, D., 2002. Effect of prenatal administration of haloperidol,
risperidone, quetiapine and olanzapine on spatial learning and retention in adult
rats. Pharmacol. Biochem. Behav. 72 (3), 575 – 579. https://doi.org/10.1016/S0091-
3057(02)00727-X .
Rowson, Z., Setzer, R.W., Padilla, S., Paul Friedman, K., Carstens, K.E., 2025. A data
analysis approach for locomotor behavioral responses in developmentally exposed
zebrafish. NAM J. 1, 100033. https://doi.org/10.1016/j.namjnl.2025.100033 .
Sachana, M., Bal-Price, A., Crofton, K.M., Bennekou, S.H., Shafer, T.J., Behl, M.,
Terron, A., 2019. International Regulatory and Scientific Effort for Improved
Developmental Neurotoxicity Testing. Toxicol. Sci. 167 (1), 45 – 57. https://doi.org/
10.1093/toxsci/kfy211 .
Schildein, S., Huston, J.P., Schwarting, R.K.W., 2002. Open Field Habituation Learning Is
Improved by Nicotine and Attenuated by Mecamylamine Administered Posttrial into
the Nucleus Accumbens. Neurobiol. Learn. Mem. 77 (3), 277 – 290. https://doi.org/
10.1006/nlme.2001.4017 .
Scolnik, D., 1994. Neurodevelopment of children exposed in utero to phenytoin and
carbamazepine monotherapy. JAMA J. Am. Med. Assoc. 271 (10), 767. https://doi.
org/10.1001/jama.1994.03510340057034 .
Sheffield, T., Brown, J., Davidson, S., Friedman, K.P., Judson, R., 2022. tcplfit2: An R-
language general purpose concentration – response modeling package. Bioinformatics
38 (4), 1157 – 1158. https://doi.org/10.1093/bioinformatics/btab779 .
Sobotka, T.J., Brodie, R.E., Cook, M.P., 1972. Behavioral and neuroendocrine effects in
rats of postnatal exposure to low dietary levels of maneb. Article 2. Dev. Psychobiol.
5 (2). https://doi.org/10.1002/dev.420050207 .
Society of Advencement of AOPs. (2025). AOP-Wiki . aopwiki.org.
Tal, T., Myhre, O., Fritsche, E., Rüegg, J., Craenen, K., Aiello-Holden, K., Agrillo, C.,
Babin, P.J., Escher, B.I., Dirven, H., Hellsten, K., Dolva, K., Hessel, E.,
Heusinkveld, H.J., Hadzhiev, Y., Hurem, S., Jagiello, K., Judzinska, B., Klüver, N.,
Bartmann, K., 2024a. New approach methods to assess developmental and adult
neurotoxicity for regulatory use: A PARC work package 5 project. Front. Toxicol. 6,
1359507. https://doi.org/10.3389/ftox.2024.1359507 .
Tal, T., Yaghoobi, B., Lein, P.J., 2020a. Translational toxicology in zebrafish, 23 – 24 Curr.
Opin. Toxicol. 56 – 66. https://doi.org/10.1016/j.cotox.2020.05.004 .
Tanguay, R.L., 2025. ToxPoint: The indispensable role of zebrafish as a new approach
methodology (NAM) in toxicology. Toxicol. Sci. 208 (1), 40 – 41. https://doi.org/
10.1093/toxsci/kfaf121 .
Thomas, D.G., Shankaran, H., Truong, L., Tanguay, R.L., Waters, K.M., 2019. Time-
dependent behavioral data from zebrafish reveals novel signatures of chemical
toxicity using point of departure analysis. Comput. Toxicol. 9, 50 – 60. https://doi.
org/10.1016/j.comtox.2018.11.001 .
Tombari, R.J., Mundy, P.C., Morales, K.M., Dunlap, L.E., Olson, D.E., Lein, P.J., 2023.
Developmental Neurotoxicity Screen of Psychedelics and Other Drugs of Abuse in
Larval Zebrafish ( Danio rerio . ACS Chem. Neurosci. 14 (5), 875 – 884. https://doi.
org/10.1021/acschemneuro.2c00642 .
Tooley, U.A., Bassett, D.S., Mackey, A.P., 2021. Environmental influences on the pace of
brain development. Nat. Rev. Neurosci. 22 (6), 372 – 384. https://doi.org/10.1038/
s41583-021-00457-5 .
Ulrich, N., Endo, S., Brown, T.N., Watanabe, N., Bronner, G., Abraham, M.H., Goss, K.-U.,
2024. UFZ-LSER database v 3.2.1 [Internet], Leipzig, Germany, Helmholtz Centre for
Environmental Research-UFZ. 2017 [accessed on 9 December 2024]. Available from
http://www.ufz.de/lserd .
Van Dingenen, I., Andersen, E., Volz, S., Christiansen, M., Nov ´ak, J., Haigis, A.-C.,
Stacy, E., Blackwell, B.R., Villeneuve, D.L., Vergauwen, L., Hilscherov ´a, K.,
Holbech, H., Knapen, D., 2024. The thyroid hormone system disrupting potential of
J. Spath et al.                                                                                                                                                                                                                                    Neurotoxicology 114 (2026) 103414
15

resorcinol in fish. Ecotoxicol. Environ. Saf. 284, 116995. https://doi.org/10.1016/j.
ecoenv.2024.116995 .
Von Wyl, M., K ¨onemann, S., Vom Berg, C., 2023. Different developmental insecticide
exposure windows trigger distinct locomotor phenotypes in the early life stages of
zebrafish. Chemosphere 317, 137874. https://doi.org/10.1016/j.
chemosphere.2023.137874 .
Wang, Z., Walker, G.W., Muir, D.C.G., Nagatani-Yoshida, K., 2020. Toward a global
understanding of chemical pollution: a first comprehensive analysis of national and
regional chemical inventories. Enviromental Sci. Technol. 54, 2575 – 2584 .
Weisenburger, W.P., Minck, D.R., Acuff, K.D., Vorhees, C.V., 1990. Dose-response effects
of prenatal phenytoin exposure in rats: effects on early locomotion, maze learning,
and memory as a function of phenytoin-induced circling behavior. Neurotoxicology
Teratol. 12 (2), 145 – 152. https://doi.org/10.1016/0892-0362(90)90127-x .
Williams, A.J., Grulke, C.M., Edwards, J., McEachran, A.D., Mansouri, K., Baker, N.C.,
Patlewicz, G., Shah, I., Wambaugh, J.F., Judson, R.S., Richard, A.M., 2017. The
CompTox Chemistry Dashboard: a community data resource for environmental
chemistry. J. Cheminform 9, 61 .
Wood, S.N., 2017. Generalized Additive Models: An Introduction with R (2. Aufl.).
Chapman and Hall/CRC. https://doi.org/10.1201/9781315370279 .
Zoodsma, J.D., Chan, K., Bhandiwad, A.A., Golann, D.R., Liu, G., Syed, S.A., Napoli, A.J.,
Burgess, H.A., Sirotkin, H.I., Wollmuth, L.P., 2020. A Model to Study NMDA
Receptors in Early Nervous System Development. J. Neurosci. 40 (18), 3631 – 3645.
https://doi.org/10.1523/JNEUROSCI.3025-19.2020 .
Glossary
Acoustic Startle Response (ASR): A specific type of startle reflex triggered by sudden sound
stimuli, used to assess auditory function and neurotoxicity in zebrafish and other
model organisms.
Active concentration at the cutoff (ACC): Point of departure estimates.
Acute Exposure: A short-term exposure to a substance, often used in toxicology to assess
immediate or rapid effects on biological systems, in contrast to chronic exposure,
which involves long-term or repeated exposure.
Basal Motor Activity/Baseline activity: The level of motor activity in an organism under
normal, non-stimulated conditions. Used as a control to compare with stimulated or
chemically altered motor responses.
Benchmark Concentration (BMC): Activity concentration observed at the benchmark
response level.
Concentration-Response: A two-dimensional metric (concentration and response) to derive
toxicological relevant potency metrics.
Developmental Exposure: Exposure to a substance that last at least 24 h.
Developmental Neurotoxicity (DNT): Toxic effects on the developing nervous system, typi -
cally assessed through changes in motor activity, sensory function, learning, memory,
and brain histopathology, often leading to long-term or permanent neurobehavioral
deficits.
Developmental Neurotoxicity in vitro Test Battery (DNT IVB): A test battery comprised of 17
in vitro assays covering a multitude of key neurodevelopmental processes.
Endpoints: Measurable outcomes used in toxicological studies to evaluate biological or
behavioral responses, such as startle responses, habituation, motor activity, and
memory retention.
Gamma-aminobutyric acid (GABA) Receptor: Receptors that respond to the inhibitory
neurotransmitter GABA, critical for regulating neuronal excitability and preventing
overstimulation, playing roles in sedation, anxiety regulation, and seizure prevention.
Generalized Additive Mixed-Effects models (GAMMs): Statistical tool that combines Gener -
alized Additive Models with Linear Mixed-Effects Models to analyze complex data.
Habituation: A type of non-associative learning where an organism gradually reduces its
response to a repeated, non-threatening stimulus. In toxicology, habituation is often
used to assess learning and memory.
Half-maximal effect concentrations (AC50): Active concentration at 50% of the maximal
predicted change in response (top) value
Interstimulus Interval (ISI): The period of time between consecutive stimuli in an experi -
ment. This is used to assess how quickly and consistently an organism responds to
repeated stimuli.
Memory Retention: The ability of an organism to recall or retain learned responses over
time, evaluated by testing the persistence of learned behavior after a delay.
Mode of Action (MoA): The specific biochemical interaction through which a chemical
substance produces its effect on a living organism. In toxicology, identifying a
chemical ’ s MoA helps determine its potential hazards.
MSE: Most Sensitive Endpoint in DNT IVB or VAMR assays.
Motor Activity: A measure of movement (depicted as pixel changes per second).
New Approach Method (NAM): A method in toxicity testing which is 3R-compliant (replace,
reduce, refine).
Nicotinic Acetylcholine Receptor (nAChR): Ligand-gated ion channels that respond to the
neurotransmitter acetylcholine and nicotine.
N-Methyl-D-aspartic acid (NMDA) Receptor: A receptor subtype of glutamate involved in
synaptic plasticity, memory, and learning. Overactivation of NMDA receptors can lead
to excitotoxicity, which is implicated in various neurodegenerative diseases.
OECD Test Guidelines (TG): A set of internationally recognized protocols for conducting
toxicological tests, including those that assess developmental neurotoxicity (e.g.,
OECD TG 426). These guidelines are used to ensure consistency and reliability in
regulatory testing.
Potentiation of Habituation: The increase in habituation with repeated stimulus exposure. In
toxicological assays, it is used to assess the learning capabilities of organisms, with
impaired potentiation suggesting learning deficits.
Visual and Acoustic Motor Response (VAMR): An automated behavior assay in zebrafish
larvae designed to assess motor responses to visual (light) and acoustic (sound)
stimuli, providing endpoints related to neurodevelopment and neurotoxicity.
J. Spath et al.                                                                                                                                                                                                                                    Neurotoxicology 114 (2026) 103414
16