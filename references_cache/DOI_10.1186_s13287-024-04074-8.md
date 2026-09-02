---
reference_id: DOI:10.1186/s13287-024-04074-8
title: An hiPSC-CM approach for electrophysiological phenotyping of a patient-specific case of short-coupled TdP
authors:
- Willem B. van Ham
- Esmeralda E. M. Meijboom
- Merel L. Ligtermoet
- Jantine Monshouwer-Kloots
- Anneline S. J. M. te Riele
- Folkert W. Asselbergs
- Eva van Rooij
- Mimount Bourfiss
- Toon A. B. van Veen
journal: "Stem Cell Research &amp; Therapy"
year: '2024'
doi: 10.1186/s13287-024-04074-8
content_type: full_text_pdf
full_text_attempted: true
full_text_provider: openalex
full_text_url: "https://stemcellres.biomedcentral.com/counter/pdf/10.1186/s13287-024-04074-8"
oa_status: gold
license: cc-by-nc-nd
local_pdf_path: files/DOI_10.1186_s13287-024-04074-8.pdf
---

# An hiPSC-CM approach for electrophysiological phenotyping of a patient-specific case of short-coupled TdP
**Authors:** Willem B. van Ham, Esmeralda E. M. Meijboom, Merel L. Ligtermoet, Jantine Monshouwer-Kloots, Anneline S. J. M. te Riele, Folkert W. Asselbergs, Eva van Rooij, Mimount Bourfiss, Toon A. B. van Veen
**Journal:** Stem Cell Research &amp; Therapy (2024)
**DOI:** [10.1186/s13287-024-04074-8](https://doi.org/10.1186/s13287-024-04074-8)

## Content

van Ham et al. Stem Cell Research & Therapy          (2024) 15:470  
https://doi.org/10.1186/s13287-024-04074-8
RESEARCH Open Access
© The Author(s) 2024. Open Access  This article is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 
International License, which permits any non-commercial use, sharing, distribution and reproduction in any medium or format, as long 
as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if 
you modified the licensed material. You do not have permission under this licence to share adapted material derived from this article or 
parts of it. The images or other third party material in this article are included in the article’s Creative Commons licence, unless indicated 
otherwise in a credit line to the material. If material is not included in the article’s Creative Commons licence and your intended use is not 
permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To 
view a copy of this licence, visit http:// creat iveco mmons. org/ licen ses/ by- nc- nd/4. 0/.
Stem Cell Research & Therapy
An hiPSC-CM approach 
for electrophysiological phenotyping 
of a patient-specific case of short-coupled TdP
Willem B. van Ham1*  , Esmeralda E. M. Meijboom1  , Merel L. Ligtermoet1, Jantine Monshouwer-Kloots2, 
Anneline S. J. M. te Riele3  , Folkert W. Asselbergs3,4  , Eva van Rooij2,3  , Mimount Bourfiss3†   and 
Toon A. B. van Veen1†   
Abstract 
Introduction A healthy young woman, age 26 without prior cardiac complications, experienced an out-of-hospital 
cardiac arrest caused by ventricular fibrillation (VF), which coincided with a fever. Comprehensive diagnostics includ-
ing echo, CMR, exercise testing, and genetic sequencing, did not identify any potential cause. This led to the diagnosis 
of idiopathic VF and installment of an implantable cardioverter defibrillator, which six months later appropriately inter-
vened another VF episode under conditions comparable to the first event. A second diagnostic opinion concluded 
short-coupled Torsade de Pointes (scTdP), and the patient was started on a verapamil treatment.
Methods From this patient, human induced pluripotent stem cell cardiomyocyte (hiPSC-CM) lines were generated 
to study cellular electrophysiology. Without a known genetic pathogenic variation, no isogenic control line could 
be produced, therefore a healthy age- and sex-matched control hiPSC-CM line was used. Cellular electrophysiology 
was studied in these cardiomyocytes using calcium- and voltage sensitive fluorescent dyes and measurements were 
carried out at 37 °C and 39 °C, to mimic the condition of hyperthermia in the patient. mRNA expression of electro-
physiologically relevant genes were analyzed to identify a potential underlying mechanism.
Results Calcium transients measured in patient lines at a physiological temperature indicated the occurrence 
of early after transients (EATs). Strikingly, at 39 °C the incidence of EATs further increased. Membrane potential data 
from the patient also revealed shorter action potentials that, combined with the EATs, indicate the premature release 
of calcium during diastole, which could be responsible for the extrasystoles in the patient. Gene expression profiles 
were mainly downregulated in the patient but could not clearly aid in unraveling a mechanism behind the occur-
rence of EATs. Pharmacological screening was performed to evaluate the treatment regimen and to determine 
a mechanism of action of the EATs. While verapamil, dantrolene, and flecainide did not decrease the incidence of EATs, 
calcium handling parameters were affected indicating functionality of the drugs.
†Mimount Bourfiss and Toon A. B. van Veen are shared senior authors.
Anneline S. J. M. te Riele: Member of the European Reference Network for rare, 
low prevalence and complex diseases of the heart: ERN GUARD-Heart (ERN 
GUARD HEART; http://guardheart.ern-net.eu).
*Correspondence:
Willem B. van Ham
W.B.vanHam-6@umcutrecht.nl
Full list of author information is available at the end of the article

Page 2 of 13van Ham et al. Stem Cell Research & Therapy          (2024) 15:470 
Conclusion This patient-specific case of electrophysiological phenotyping resulted in a hypothesis of the possible 
mechanism behind the scTdP arrhythmias, but also accentuates the applicability of patient-specific hiPSC-CM disease 
modeling and phenotyping.
Keywords Short-coupled Torsade de Pointes, hiPSC-CM, Patient-specific, Phenotyping, Calcium handling dysfunction
Introduction
Inherited and acquired cardiomyopathies and cardiac 
channelopathies include a considerable number of car -
diac diseases with various genetic predisposition, disease 
progression, and clinical presentation [1–4]. Unfortu -
nately, the most common and often first symptom in 
arrhythmogenic forms of cardiomyopathy is sudden car -
diac death (SCD), caused by severe cardiac arrhythmias. 
These diseases are often introduced due to genetic vari -
ations, including complex variations like compound and 
digenetic heterozygosity [5]. However, a primary clinical 
phenotype can also be present in patients without (or 
unknown) genetic predisposition [6, 7]. The unlimited 
use of human induced pluripotent stem cell derived car -
diomyocytes (hiPSC-CMs) has facilitated numerous pos -
sibilities for physiological studies, disease modeling and 
phenotyping, and pharmacological safety screenings. 
Studying patient-specific hiPSC-CM models can aid in 
understanding not only the mechanism underlying a dis -
ease phenotype, but it also provides a method to predict 
potential clinical presentations based on experimental 
phenotypes. Additionally, it might help to identify rela -
tives at risk [8].
At the basis of cardiac arrhythmias stands the dysreg -
ulation of the cardiac action potential (AP) and calcium 
handling within the cardiomyocytes [9]. Conduction 
of the AP across the myocardium activates the cardio -
myocytes in a synchronized manner, followed by the 
calcium release from the sarco-endoplasmic reticulum 
(SR) within the individual cells, which then results in the 
contraction of the myocardial tissue [10]. Any of these 
processes can be disrupted by decreased or increased 
function of the proteins involved. Pharmacological inter -
ventions can be applied to modulate the effects of dis -
turbed ion transport, by blocking, altering kinetics, or 
activating different ion channels and transporters.
In this study we included a 26-year-old female patient 
without prior cardiac (or related) family history, who suf-
fered from an out of hospital sudden cardiac arrest due 
to ventricular fibrillation (VF) while she was having a 
fever. Extensive clinical diagnostics, including cardiac 
echo and cardiac magnetic resonance imaging (CMR), 
genetic sequencing, and exercise testing, did not iden -
tify a cause for the VF. The ectopy originated from the 
lower left septal segment and was therefore suggested to 
be Purkinje fiber related. Given the fact that no extensive 
electrophysiological testing has been performed this 
could however not be confirmed. The patient was diag -
nosed with short-coupled Torsade de Pointes (scTdP). 
An implantable cardioverter defibrillator (ICD) was 
implanted, which several months later had to intervene 
another VF during a second period of hyperthermia. 
The ICD interrogation of the minute prior to the inter -
ventional shock included a VF episode befitting to the 
scTdP diagnosis (Fig.  1). Both a self-terminating VF and 
the intervened VF episode were initiated by short cou -
pled ectopic activity. Additionally, several extrasystoles 
preceded the arrhythmias in this brief timespan. The 
patient was instrumented on verapamil. Blood was taken 
from the patient and hiPSC-CMs were produced. In the 
absence of an identified genetic variation, a healthy age- 
and sex-matched donor was used a control.
We investigated the experimental electrophysiological 
phenotype of the hiPSC-CMs of the patient and a healthy 
individual, in an attempt to discover a potential mecha -
nism for the VF occurrence in the patient. We were able 
to identify a calcium handling disturbance, which was 
even worsened by a hyperthermic condition, while phar -
macological interventions did not alleviate the calcium 
handling disruptions. The ensemble of electrophysiologi -
cal effects resulted in a hypothesis of the possible mecha -
nism behind the scTdP arrhythmias, but also accentuates 
the applicability of patient-specific hiPSC-CM disease 
modeling and phenotyping.
Methods
Drugs
Dantrolene (Sigma-Aldrich, D9175) and flecainide 
(Sigma-Aldrich F6777) were dissolved in DMSO to 
10 mM, filtered, and stored at – 20 °C. Verapamil (Cen -
trafarm) was diluted at 2.5  mg/mL HCl and stored at 
room temperature. Drugs were added to the culture 
medium for 24 h prior to experiments, DMSO was used 
for vehicle measurements.
Generation of human iPSC clones
iPSC lines were commercially generated through episo -
mal reprogramming of isolated peripheral blood mono -
nuclear cells derived from the patient and a healthy 
age- and sex-matched control at the Leiden University 
Medical Center hiPSC core facility. Episomal repro -
gramming was performed as described previously [11]. 

Page 3 of 13
van Ham et al. Stem Cell Research & Therapy          (2024) 15:470 
 
Pluripotency vectors included NANOG, SSEA4, and 
OCT3/4, and FACS characteristics are also shown in Fig-
ure S1. Three independent clones were produced for the 
patient and one clone for the healthy individual. Clones 
were obtained frozen in liquid nitrogen.
Bulk karyo‑sequencing
 ± 1000 hiPSCs were collected as pellet to which 5  µl of 
2  µg Proteinase K (NEB) in 1 × CutSmart Buffer (NEB) 
was added for 2 h at 55 °C followed by 10 min at 80 °C. 
DNA was digested using 10 µl of 10 U NLAIII (NEB) in 
1 × CutSmart Buffer for 2 h at 37 °C followed by 20 min at 
80 °C. DNA fragments were ligated to adapters by adding 
20 µl of 800 U T4 DNA ligase (NEB), 1 mM ATP (Ther -
moFisher) and 50 nM adapter in 1 × T4 DNA ligase buffer 
(NEB) and incubating at 16  °C overnight. The library 
preparation, sequencing and analysis was performed as 
described previously [12].
Cell culture
hiPSCs were cultured on Geltrex-coated wells (Gibco, 
A1413302). Cells were refreshed daily with Essen -
tial 8 Medium (Gibco, A1517001), and passaged once 
they reached 80–100% confluency. Briefly, medium 
was aspirated, and TrypLE Express Enzyme (Gibco, 
12605010) was added for 5  min at 37  °C. After incuba -
tion, 4  mL of Essential 8 Medium, supplemented with 
1 µM thiazovivin (Sigma-Aldrich, 420220), was added to 
the dissociated cells and the cell suspension was trans -
ferred to a 15 mL Falcon tube. Cells were centrifuged at 
300 RCF for 3 min. Subsequently, cells were seeded at a 
density of 15.000  cells/cm2 in Essential 8 Medium, sup -
plemented with 1 µM thiazovivin. Medium was refreshed 
the next day with plain Essential 8.
Cardiomyocyte differentiation
hiPSCs were grown until 80–90% confluency and washed 
once with dPBS (Gibco, 14190094). Cells were then 
cultured with RMPI +  + (bare RPMI-1640-Medium-
GlutaMAXSupplement-HEPES (Gibco, 72400-021) sup -
plemented with 0.5 mg/mL human recombinant albumin 
(Sigma-Aldrich, A9731) and 0.2  mg/mL L-Ascorbic 
Acid 2-Phosphate (Sigma, A8960)), added with 4  µM 
CHIR99021 (Sigma, 361559). After 48  h, medium was 
replaced with RMPI +  + added with 5 µM IWP2 (Sigma, 
681671), following a single rinse with bare RMPI-
1640. Cells were then refreshed every other day with 
RMPI +  + , for four days. From there, cells were cultured 
every three to four days with complete RMPI medium 
(bare RMPI-1640, supplemented with B-27 Supplement 
(Gibco, 17504001)). Then, to increase cardiomyocyte 
purity, complete RMPI medium was replaced with selec -
tion medium (RPMI 1640 without glucose and without 
HEPES (Biological Industries, 01-101-1A), added with 
Fig. 1 Intervention of ventricular fibrillation as seen on the ICD interrogation of the patient. Electrical signal as detected by the implantable 
cardioverter defibrillator (ICD) of the patient, consisting of a regular rhythm, independent extrasystoles, a self-terminating ventricular fibrillation 
(VF), and the intervened VF. 5 subsequent squares represent a timespan of 1 s. The lighting symbol represents the moment of the ICD shock. Letters 
underneath the interrogation represent sensing (S), tachycardia (T), capacitor charging/charged (C), post-shock pacing (P), unclassified event (•), 
noise (N)

Page 4 of 13van Ham et al. Stem Cell Research & Therapy          (2024) 15:470 
4 mM lactate (Chemcruz SC-301818A), 3.5 mM HEPES 
(Sigma H0887), and B-27 supplement) [13]. After four 
days of selection, historically reaching a purity of 90–95%, 
cells were placed in complete RMPI medium, supple -
mented with 1% penicillin–streptomycin (Thermo Fisher 
Scientific 15140122). Prior to optical experiments, the 
hiPSC-CMs were dissociated with TrypLE Select Enzyme 
without phenol red (Gibco, A1217703) and seeded on 
Geltrex-coated coverslips. Three to four independent dif -
ferentiations were produced of each hiPSC line.
Optical electrophysiology
hiPSC-CMs were seeded at a density of 150.000 cells 
per Geltrex-coated coverslip to allow formation of mon -
olayered clusters. Coverslips were incubated with either 
Powerload and FluoVolt (ThermoFisher, F10488, 1:1000) 
or Fluo-4-AM (ThermoFisher, F14201, 1:1000) in com -
plete RMPI medium for 20  min at 37  °C. Clusters were 
recorded at 37  °C and 39  °C (the latter to mimic fever) 
during which the coverslips were placed in a bath solu -
tion containing (mM): NaCl (130), KCl (4), CaCl2 (1.8), 
MgCl2 (1.2), NaHCO3 (18), HEPES (10), Glucose (10), 
with pH 7.4. Fluorescent signals were recorded using a 
custom-built microscope (Cairn Research, UK) using a 
10 × objective. Blue light was filtered using an excitation 
filter (482/35 nm) and projected on the objective with a 
dichroic mirror (515 nm). Fluorescent signals were cap -
tured, via a long-pass emission filter (514 nm), by a high-
speed camera (Andor Zula 5.5.CL3). Analysis of the data 
was performed using Fiji and Peaks, a custom-written 
Matlab script (https:// doi. org/ 10. 17605/ OSF. IO/ 86UFE). 
Analyzed signals of the spontaneously beating hiPSC-
CMs were then adjusted for beating rate using a modi -
fied Fredericia’s correction: APDcorrected = APD/(∛(60/
BPM).
Quantitative PCR
Total RNA was isolated from hiPSC-derived cardiomyo -
cytes using the RNeasy Mini Kit (Qiagen, 74104) follow -
ing the protocol supplied by the manufacturer. Total RNA 
was reverse transcribed using the iScript cDNA Synthesis 
Kit (Bio Rad, 1708891). Quantitative PCR (qPCR) reac -
tions were performed on a Bio Rad CFX96 Real-Time 
PCR Detection System using the iQ SYBR Green Super -
mix kit (Bio Rad, 170-8885). Primers used for amplifica -
tion can be found in Table S1. The  2(−ΔΔCT) method was 
used to analyze the data.
Statistical analysis
All statistical analysis was executed using Graph -
Pad Prism v.9 software. Comparisons were analyzed 
using a Student’s T-test (action potential data), One-
Way ANOVA, with Tukey’s post-hoc test to correct for 
multiple comparisons (mRNA expression data) or Two-
Way ANOVA, with Tukey’s post-hoc test to correct for 
multiple comparisons (calcium handling data). Data is 
shown as individual datapoints.
Results
Electrophysiological disturbances
In order to uncover a potential cause for the ventricular 
arrhythmias experienced by the patient (Fig.  1), hiPSCs 
were generated from the patient and an age- and sex-
matched healthy control. hiPSC characterization and 
karyotyping data are shown in Figure S1. Optical screen -
ing of calcium transients (CaTs) was performed using a 
fluorescent calcium sensitive dye, which resides in the 
cytosol. Release of SR calcium via the ryanodine recep -
tor (RyR2) and removal via mainly the sarco-endoplasmic 
reticulum calcium ATPase (SERCA2A) and the sodium-
calcium exchanger (NCX1) are represented in recordings 
as peak up- and downstrokes, respectively. In the hiPSC-
CMs monolayered clusters of the patient, initial calcium 
releases were followed by additional releases, which were 
defined as early after transients (EATs) (Fig.  2A). Under 
normothermic conditions, these EATs were observed in 
8.14% of the measurements in the patient, compared to 
0% in the healthy control cells (Fig.  2B). The occurrence 
of these EATs was even further increased during hyper -
thermia, resulting in 17.99% EATs in the measurements 
in the patient, compared to 2.94% in the healthy con -
trol. Interestingly, the single EAT in the control line that 
was observed in only one CaT during the recording and 
displayed an amplitude that was smaller than the initial 
calcium release. However, the recorded EATs originat -
ing from the patient lines mainly occurred in every CaT 
of those recordings, while also having amplitudes that 
matched the original released ones (Figure S2).
Morphology of CaTs were analyzed to quantify release 
and removal times of cytosolic calcium in these meas -
urements (Fig.  3A). An increased number of calcium 
releases, as well as increased amplitudes were detected 
in the patient, without displaying a prolonged release 
time (Fig.  3B–D). Both cytosolic calcium removal and 
total CaT duration were lengthened in cells from the 
patient, which was seen at a regular temperature and 
during hyperthermia (Fig.  3E, F). This was mainly 
driven by extreme CaT durations corresponding to EAT 
measurements.
In the control and patient lines, action potential dura -
tion (APD) was also measured using a voltage-sensitive 
dye, at both normo- and hyperthermia (Figure S3). Anal -
ysis of the AP fluorescence signal was performed, with 
the depolarization and repolarization as peak up- and 
downstrokes, respectively (Fig.  4A). In the cells from the 
patient, spontaneous beating rates (Fig.  4B) were similar 

Page 5 of 13
van Ham et al. Stem Cell Research & Therapy          (2024) 15:470 
 
when compared to those recorded during CaT measure -
ments (Fig.  3B). The beating rate of healthy and patient 
hiPSC-CMs in the APD measurements was similar 
(Fig.  4B). Interestingly, action potential repolarization 
was shorter in the patient (Fig.  4C, D). Together, these 
data suggest electrophysiological disturbances that could 
underly the clinical phenotype of the patient, strength -
ened by an aggravation of the disturbed calcium handling 
by a hyperthermic condition.
Gene expression profile
While no pathogenic genetic variations were identi -
fied in the patient, studying gene expression could aid 
in identifying a cause for the occurrence of the EATs. 
Therefore, mRNA expression of electrophysiologically 
relevant genes was quantified in multiple clones and dif -
ferentiations of the two individuals (Figure S4). mRNA 
expression of many important calcium handling pro -
teins was significantly decreased, including RyR2, SER -
CA2a, phospholamban (PLN), L-type calcium channel 
 (CaV1.2), NCX1, and the calcium/calmodulin dependent 
kinase (CAMK2), or showed a trend towards downregu -
lation, such as calsequestrin (CSQ2). mRNA expression 
of proteins involved in the formation of the AP were also 
decreased, including the rapid component of the potas -
sium repolarization current  (KV11.1) and the depolar -
izing sodium current  (NaV1.5). mRNA expression of the 
potassium current mainly responsible for the stabiliza -
tion of the resting membrane potential  (KIR2.1) was also 
seemingly lower in the patient, but is known to be close 
to absent as generally reported in all hiPSC-CMs [14]. 
Overall, the majority of important genes involved in cel -
lular electrophysiology and calcium handling was signifi -
cantly downregulated in the patient.
Hampered pharmacological screening
To investigate the effects of several drugs on the mech -
anisms behind the observed and aberrant EATs, cells 
from the two individuals were incubated with 5.5  µM 
verapamil (a  CaV1.2 blocker), 10 µM dantrolene (a RyR2 
blocker), or 10 µM flecainide (a  NaV1.5 blocker) for 24 h. 
CaTs were measured under hyperthermic conditions, and 
the occurrence of EATs was quantified. While only 1 EAT 
was observed in each of the four conditions using con -
trol cells (4–6.25%), the number of EATs in the patient 
at hyperthermia with vehicle administration (15.52%, 
Fig.  5) was comparable compared to the previous base -
line experiments (17.99%, Fig.  2). Verapamil (20.75%), 
Fig. 2 Occurrence of early after transients in patient hiPSC-CMs. Calcium transient measurements were performed in hiPSC-CMs from the patient 
and a healthy control during normo- and hyperthermia. A During measurements of hiPSC-CMs of the patient extra calcium releases, termed 
early after transients (EATs), were observed during normo- and hyperthermia. B Quantification of the EATs highlighted the increased occurrence 
in the patient, especially after hyperthermia. N = number of measured cell clusters, originating from one clone (healthy) and 3 clones (patient) each 
with 3–4 hiPSC-CM differentiations

Page 6 of 13van Ham et al. Stem Cell Research & Therapy          (2024) 15:470 
dantrolene (24.49%), and flecainide (17.50%) even further 
increased the incidence of EATs (Fig.  5), which indicates 
a more profound disruption of the calcium kinetics in the 
hiPSC-CMs of specifically the patient.
Quantification of the CaTs partly supported the effects 
of verapamil and dantrolene. Although the number of 
calcium signals per minute (SPM) and amplitude did 
not differ between healthy and patient cells, the number 
of SPM seemed to be lower for the patient (Fig.  6A, B) 
when compared to the initial set of calcium experiments 
(Fig.  3B). However, release time was increased after 
verapamil administration in the patient, but otherwise 
similar or even shortened compared to previous meas -
urements (Fig.  6C). The CaT length was only influenced 
by dantrolene, which resulted mainly from those meas -
urements that displayed extreme EATs (Fig.  6D, E). 
Additionally, while no drug was able to decrease the 
occurrence of EATs, amplitude of EATs seemed to be 
diminished in a majority of the measurements (Figure 
S5). All combined, the applied pharmacological screen -
ing did not result in improved calcium regulation, but 
in contrast even worsened the situation of disturbed cal -
cium handling.
Discussion
In this study, we generated hiPSC-CMs from a patient 
who was successfully resuscitated from an out of hospi -
tal sudden cardiac arrest due to ventricular arrhythmias 
Fig. 3 Calcium transient parameters indicating disturbed calcium handling. Calcium transient measurements were performed in hiPSC-CMs 
from the patient (red) and a healthy control (black) during normo- and hyperthermia. A Definitions of parameters based on the amplitude, and 10% 
and 90% of the up- and downstroke of the fluorescence intensity. B Number of signals per minute (SPM). C Amplitude of the initial calcium signal, 
representing the amount of calcium in the initial release. D Rise time of the calcium signal, representing the release time of calcium into the cytosol. 
E Decay time of the calcium signal, representing the removal time of calcium from the cytosol. F 90% of the calcium transient duration (CTD), 
representing the duration of the entire calcium transient. N = 34–221 measured cell clusters, originating from one clone (healthy) and 3 clones 
(patient) each with 3–4 hiPSC-CM differentiations

Page 7 of 13
van Ham et al. Stem Cell Research & Therapy          (2024) 15:470 
 
without a known cause. The cardiac arrest occurred 
under conditions of fever. In the absence of a known 
genetic variation in the patient, hiPSC-CMs were pro -
duced from a healthy age- and sex-matched control. 
Upon evaluating calcium handling in all hiPSC-CM 
lines, we found a striking occurrence of premature cal -
cium releases (EATs) in the patient under normothermic 
conditions, which robustly increased under hyperther -
mic conditions. Further analysis of action potentials in 
the patient indicated a shortened APD, again both in 
normo- and hyperthermia. In general, mRNA expression 
of electrophysiologically crucial genes was also dimin -
ished in the patient, which cannot convincingly uncover 
a mechanism behind the EAT occurrence. We then per -
formed a pharmacological screening to further study the 
proarrhythmic mechanism initiating the EATs, as well 
as to evaluate the effect of the current clinical treatment 
in the patient. Drug regimen was focused on controlling 
extracellular calcium load via  CaV1.2 (by application of 
verapamil) and SR-calcium release (by application of dan-
trolene and flecainide). In contrast to what was expected, 
neither verapamil, dantrolene, nor flecainide ameliorated 
Fig. 4 Shortened action potentials in patient hiPSC-CMs. Action potential measurements were performed in hiPSC-CMs from the patient 
(red) and a healthy control (black) during normo- and hyperthermia. A Definitions of parameters based on 50% and 90% of the downstroke 
of the fluorescence intensity. B Number of signals per minute (SPM). C 50% of the action potential duration (APD), representing early repolarization. 
D 90% of the APD, representing total repolarization. N = 47–135 measured cell clusters, originating from one clone (control) and 3 clones (patient) 
each with 3–4 hiPSC-CM differentiations

Page 8 of 13van Ham et al. Stem Cell Research & Therapy          (2024) 15:470 
the incidence of EATs and even further perturbed the dis-
turbed calcium handling, although it did seem to affect 
the calcium handling in terms of decreased amplitude 
and slowed CaT duration. In contrast, treatment of the 
healthy cells with those drugs did not worsen outcome. 
This study highlights the potential of patient-specific 
application and disease phenotyping using hiPSC-CMs.
Short‑coupled torsade de pointes
As extra calcium is being released from the SR (EATs) 
without being triggered by a new AP , which can occur 
when the cardiac membrane potential is either still depo-
larized or completely repolarized, it can cause early or 
delayed after depolarizations (EADs and DADs), respec -
tively [15]. These EADs and DADs are prematurely trig -
gered action potentials, and in case that SR-calcium 
release is involved, are caused by increasing inward 
sodium current via the NCX1 in return for an outward 
calcium flux [16, 17]. In the experimental data from our 
patient, both APD shortening and EATs are observed, 
creating the ideal circumstance for DAD formation, 
which could result in triggered activity in the form of 
premature ventricular complexes (PVCs) and VF [18, 
19]. However, it is important to note that the electro -
physiological immaturity of hiPSC-CMs is mainly notice-
able in the shorter AP , which could mean that the EATs 
observed in our study, might result in either EADs or 
DADs. Within our AP measurements we did not observe 
any DAD-like peaks; however, within spontaneously 
active hiPSC-CMs it is difficult to determine which sig -
nals are DAD-triggered action potentials.
Both EADs and DADs have been hypothesized as cause 
for the development of scTdP , although EADs are thought 
to be more likely since patients often have normal QT 
intervals. As PVCs prior to the TdP are short coupled, it 
would require an early triggered AP [20–22]. The PVCs 
present prior to scTdP in patients often originate from 
the Purkinje fiber network, which are especially likely to 
result in VF [21, 23]. As this seems to be the case in our 
patient, the experienced VF episodes developed are with 
a high degree of plausibility caused by early membrane 
depolarizations due to triggered extra calcium release 
from the SR. The use of verapamil has been shown to be 
effective in decreasing TdP occurrence, while not reduc -
ing the risk of SCD, leaving ICD implantation as advisa -
ble treatment [20, 22, 24, 25]. Whether the hyperthermia 
in the patient has acted as a secondary trigger remains 
unresolved.
Pharmacological screening in diseased hiPSC‑CMs
The pharmacological intervention, using verapamil, dant-
rolene, and flecainide, did not decrease the occurrence of 
EATs in the patient lines. While to a certain extend these 
drugs did show to be effective, all have limitations in 
term of preventing EATs. Verapamil is a  CaV1.2 blocker 
that can inhibit or delay calcium-induced calcium release 
Fig. 5 Occurrence of early after transients after pharmacological intervention. Calcium transient measurements were performed in hiPSC-CMs 
from the patient and a healthy control during hyperthermia after 24 h incubation with either verapamil (5.5 µM), dantrolene (10 µM), flecainide 
(10 µM), or a vehicle (DMSO). Compared to the prior experiment, the occurrence of early after transients (EATs) after drug administration did 
not alter in the vehicle group, while the patient had a similar or increased percentage of EATs. N = number of measured cell clusters, originating 
from one clone (control) and 3 clones (patient) each with 3–4 hiPSC-CM differentiations

Page 9 of 13
van Ham et al. Stem Cell Research & Therapy          (2024) 15:470 
 
(CICR), by lowering the calcium availability in the dyad 
between T-tubules and the SR. Blocking this channel 
would then prevent extra CICR-triggered releases in 
mature cardiomyocytes. However, hiPSC-CMs remain 
rather immature and are lacking the formation of 
T-tubules [26, 27]. This could potentially imply that the 
role of dyad calcium is dominated by general cytosolic 
calcium, obstructing the prevention of EATs by vera -
pamil in hiPSC-CMS. The use of flecainide was applied 
in our experiments with a similar reasoning of indirectly 
limiting CICR. Flecainide is a  NaV1.5 blocker, which 
would lower the cytosolic sodium concentration, reduc -
ing the influx of calcium via NCX1, eventually reducing 
the reactivation of RyR2. Interestingly, while the affin -
ity of flecainide is much higher for Nav1.5 and several 
potassium channels [28], a direct blockade of RyR2 has 
also been proposed [29, 30]. Again, no decrease in EAT 
prevalence was observed after flecainide treatment in the 
patient cells, which implies improbability of the contro -
versial RyR2 blockade. However, flecainide analogs spe -
cifically targeting only  NaV1.5 have severely decreased 
effects on RyR2-induced calcium release, highlighting the 
efficacy of direct RyR2 binding by flecainide [31]. Dant -
rolene is originally a RyR1 (present in skeletal muscle) 
blocker, used for treating muscular spasticity and malig -
nant hyperthermia [32]. However, it has been shown that 
Fig. 6 Calcium transient parameters after drug administration. Calcium transient measurements were performed in hiPSC-CMs from the patient 
(red) and a healthy control (black) during hyperthermia after 24 h incubation with either verapamil (5.5 µM), dantrolene (10 µM), flecainide 
(10 µM), or a vehicle (DMSO). A Number of signals per minute (SPM). B Amplitude of the initial calcium signal, representing the amount of calcium 
in the initial release. C Rise time of the calcium signal, representing the release time of calcium into the cytosol. D Decay time of the calcium signal, 
representing the removal time of calcium from the cytosol. E 90% of the calcium transient duration (CTD), representing the duration of the entire 
calcium transient. N = 15–58 measured cell clusters, originating from one clone (control) and 3 clones (patient) each with 3–4 hiPSC-CM 
differentiations

Page 10 of 13van Ham et al. Stem Cell Research & Therapy          (2024) 15:470 
dantrolene can also block RyR2 (the isoform primarily 
present in the heart) [33], and has proven to be effec -
tive in hiPSC-CM models of RyR2 muations [34, 35]. The 
binding of dantrolene to RyR2 is rather specific, where it 
is proposed to bind only the unzipped state of the protein 
in which the channel has an increased open probability, 
often caused by pathogenic genetic variations [36]. This 
would suggest that if dantrolene was effective in com -
pletely blocking the EATs, there would be a mechanistic 
link with RyR2 such as a pathogenic genetic variation 
or chemical interaction. We observed only a decrease 
in EAT amplitude and not their occurrence. Moreo -
ver, within the clinically analyzed gene panel for inher -
ited arrhythmias (Table  S2), we carefully checked the 
sequence of the RyR2 gene in the patient but did not find 
any aberrancies. This could explain the only mild effect 
of dantrolene being merely based on incomplete block -
ade. In line with the sequence analysis of RyR2, we also 
cross-checked the sequence of DPP6, a gene involved in 
regulation of the transient outward potassium current in 
Purkinje fibers. This because overactivity of this gene due 
to genetic variations has been associated with the occur -
rence of idiopathic VF originating from the Purkinje [37, 
38].
Performing drugs safety and application screenings 
in hiPSC-CMs, especially in engineered tissues, has for 
some drugs been shown to be effective and comparable 
to expected clinical outcome in both healthy and dis -
eased cells [39, 40]. Unfortunately, the drug interventions 
in this study stress the difficulties in testing therapeutic 
options in diseased hiPSC-CMs when there is no known 
or suggested cause of the disease. Not only is it difficult 
to evaluate which class of drugs could be relevant, our 
data also shows that intervening with indistinct calcium 
disturbances could exacerbate the phenotype. Further 
understanding of molecular pathogenesis or genetic 
involvement remains a prerequisite before assessment 
of patient-specific treatment option can be considered. 
In line with that, for an appropriate comparison with the 
calcium handling machinery in adult cardiomyocytes, it 
is of utmost importance that this aspect needs additional 
maturation in hiPSC-CM [41, 42].
Clinical translationability of experimental hiPSC‑CM 
phenotyping
Patient-specific disease phenotyping has become increas-
ingly better and easier with the use and improvements 
of hiPSC-CMs. These cells can be widely implemented 
to investigate molecular and functional consequences 
of novel genetic variations and inherited cardiomyopa -
thies [13, 43–46]. The majority of the experimental stud -
ies are performed to associate a genetic predisposition 
to a general clinical phenotype in a patient population. 
However, this instigates the discussion on the role of 
experimental phenotyping of pathological electrophysiol-
ogy in the absence of a known genetic variation. In our 
case, we have identified an experimental phenotype in 
the hiPSC-CMs derived from the patient that was remi -
niscent of the observed clinical presentation, which could 
aid in the understanding of underlying mechanisms, 
supports the use of prescribed treatment options, and 
assists the vision of patient-tailored care in the future. 
However, the translationability of this disease model can 
partly be hampered by the mentioned immaturity of the 
hiPSC-CMs, or technical limitations such as spontane -
ous beating rates [47]. This is exemplified by the observed 
discrepancy between the interlinked duration of the AP 
and the CaT in the independently performed measure -
ments. While this is relatively common for immature 
hiPSC-CMs that have been cultured for less than 90 days 
post-differentiation [48], future studies would benefit 
greatly from simultaneous optical AP and CaT measure -
ments to study these electrophysiological parameters in 
concordance [49]. Nonetheless, the occurrence of these 
EATs is both pronounced and harmful, and an exten -
sive collaboration between researchers and clinicians is 
required to determine the value of disease modeling and 
experimental phenotyping for patient care.
Proposed future work on this specific case could 
expand on the role of temperature regulation by per -
forming serial measurements, shifting from normo -
thermic to hyperthermic and back, and quantifying the 
changes in EAT incidence. When this becomes feasible, 
hiPSCs could also be differentiated into cardiac Purkinje-
like cells to improve compatibility with the presumed cell 
type origin of the electrical disturbances in the patient 
[50]. Additionally, more extensive pharmacological 
screenings could be performed, using e.g. quinidine and 
verticilide, to further establish a pathological mechanism.
Conclusion
Here, we studied a patient-specific case of scTdP , in 
which the patient has suffered from multiple episodes of 
VF. Generation of hiPSC-CMs of the patient successfully 
recapitulated the clinical electrophysiological phenotype 
that could potentially be explained by the occurrence of 
premature calcium releases in the cardiomyocytes of the 
patient. This study emphasizes the potential of hiPSC-
CMs in studying cellular mechanisms and pharmaco -
logical interventions, while simultaneously describing the 
necessity for a delicate approach in translating the exper -
imental results towards the clinics.
Abbreviations
AP  Action potential
APD  Action potential duration
CaT  Calcium transient

Page 11 of 13
van Ham et al. Stem Cell Research & Therapy          (2024) 15:470 
 
EAD  Early after depolarization
EAT  Early after transient
hiPSC-CMs  Human induced pluripotent stem cell derived cardiomyocytes
ICD  Implantable cardioverter defibrillator
NCX1  Sodium-calcium exchanger
RyR2  Ryanodine receptor
SCD  Sudden cardiac death
scTdP  Short-coupled Torsade de Pointes
SERCA2a  Sarco-endoplasmic reticulum calcium ATPase
SR  Sarco-endoplasmic reticulum
VF  Ventricular fibrillation
Supplementary Information
The online version contains supplementary material available at https:// doi. 
org/ 10. 1186/ s13287- 024- 04074-8.
Additional file 1: Figure S1. Patient hiPSC clones characteristics. Three inde-
pendent patient hiPSC clones were generated from isolated peripheral 
blood mononuclear cells. (A) FACS plots of SSEA4, Nanog, and OCT3/4 
markers. (B) Karyo-sequencing profiles. Figure S2. Example recordings of 
calcium transients in healthy and patient lines. Example calcium transient 
measurements performed in hiPSC-CMs from the patient (red) and 
a healthy control (black) during hyperthermia, indicating the occur-
rence of early after calcium transients. Figure S3. Example recordings of 
action potentials in healthy and patient lines. Example action potential 
measurements performed in hiPSC-CMs from the patient (red) and a 
healthy control (black) during normo- and hyperthermia, indicating the 
shorter action potentials in the patient and both normo- and hyperther-
mia. Figure S4. Gene expression changes underlying disturbed calcium 
handling. Quantification of mRNA expression of genes involved in cardiac 
electrophysiology in hiPSC-CMs from the patient (red) and a healthy con-
trol (black). Generally, mRNA expression of electrophysiologically crucial 
genes was downregulated in the patient. Figure S5. Example recordings 
of calcium transients after pharmacological intervention. Example calcium 
transient measurements performed in hiPSC-CMs from the patient (red) 
and a healthy control (black) during hyperthermia after vehicle (DMSO), 
verapamil (5.5 µM), or dantrolene (10 µM) administration, indicating the 
diminished amplitude of early after calcium transients in the patient.
Acknowledgements
The authors declare that they have not use AI-generated work in this 
manuscript.
Author contributions
F.W.A, M.B., and T.A.B.v.V. Conceived the project. W.B.v.H., E.v.R., and T.A.B.v.V. 
Designed the experiments. J.M.K. and E.v.R. Provided materials. W.B.v.H., 
E.E.M.M., M.L.L., and J.M.K., Performed the experiments and analyzed the data. 
A.S.J.M.t.R., F.W.A, and M.B., Provided patient information and clinical back-
ground. W.B.v.H. and T.A.B.v.V. Wrote the initial manuscript. All authors read and 
approved the final submitted manuscript.
Funding
This work was supported by a grant from the Netherlands Cardio Vascular 
Research Initiative (CVON): the Dutch Heart Foundation, Dutch Federation of 
University Medical Centers, the Netherlands Organization for Health Research 
and Development and the Royal Netherlands Academy of Sciences (CVON-
PREDICT2 2018-30). Further financial support is acknowledged from the 
foundation Vrienden van het UMC Utrecht.
Availability of data and materials
The datasets supporting the conclusions of this article are included within the 
article.
Declarations
Ethics approval and consent to participate
(1) This study was part of the UNRAVEL RDP . (2) The project has been approved 
by the Biobank Board of the Medical Ethics Committee of the University 
Medical Center Utrecht. (3) The approval number is 12-387 UNRAVEL Biobank. 
(4) The project has been approved in 2018.
Informed consent
Informed consent was obtained from the patient for the participation in this 
study, including the production of hiPSC-CMs, performed experiments, and 
publication of the acquired data.
Competing interests
The authors declare that they have no competing interests.
Author details
1 Department of Medical Physiology, University Medical Center Utrecht, 
Utrecht, The Netherlands. 2 Hubrecht Institute, Royal Netherlands Academy 
of Arts and Sciences (KNAW), University Medical Center Utrecht, Utrecht, The 
Netherlands. 3 Department of Cardiology, University Medical Center Utrecht, 
Utrecht, The Netherlands. 4 Department of Cardiology, Amsterdam University 
Medical Center, Amsterdam, The Netherlands. 
Received: 10 September 2024   Accepted: 21 November 2024
References
 1. Jacoby D, McKenna WJ. Genetics of inherited cardiomyopathy. Eur Heart 
J. 2012;33:296–304. https:// doi. org/ 10. 1093/ eurhe artj/ ehr260.
 2. Martinez HR, Beasley GS, Miller N, Goldberg JF, Jefferies JL. Clinical 
insights into heritable cardiomyopathies. Front Genet. 2021;12: 663450. 
https:// doi. org/ 10. 3389/ fgene. 2021. 663450.
 3. Campuzano O, Sarquella-Brugada G, Brugada R, Brugada J. Genetics of 
channelopathies associated with sudden cardiac death. Glob Cardiol Sci 
Pract. 2015;2015:39. https:// doi. org/ 10. 5339/ gcsp. 2015. 39.
 4. Fernandez-Falgueras A, Sarquella-Brugada G, Brugada J, Brugada R, 
Campuzano O. Cardiac channelopathies and sudden death: recent clini-
cal and genetic advances. Biology (Basel). 2017. https:// doi. org/ 10. 3390/ 
biolo gy601 0007.
 5. Li CJ, Chen CS, Yiang GT, Tsai AP , Liao WT, Wu MY. Advanced evolution of 
pathogenesis concepts in cardiomyopathies. J Clin Med. 2019. https:// 
doi. org/ 10. 3390/ jcm80 40520.
 6. Burke MA, Cook SA, Seidman JG, Seidman CE. Clinical and mechanis-
tic insights into the genetics of cardiomyopathy. J Am Coll Cardiol. 
2016;68:2871–86. https:// doi. org/ 10. 1016/j. jacc. 2016. 08. 079.
 7. Coll M, Perez-Serra A, Mates J, Del Olmo B, Puigmule M, Fernandez-Fal-
gueras A, Iglesias A, Pico F, Lopez L, Brugada R, Campuzano O. Incomplete 
penetrance and variable expressivity: hallmarks in channelopathies 
associated with sudden cardiac death. Biology (Basel). 2017. https:// doi. 
org/ 10. 3390/ biolo gy701 0003.
 8. Dainis AM, Ashley EA. Cardiovascular precision medicine in the genomics 
era. JACC Basic Transl Sci. 2018;3:313–26. https:// doi. org/ 10. 1016/j. jacbts. 
2018. 01. 003.
 9. Landstrom AP , Dobrev D, Wehrens XHT. Calcium signaling and cardiac 
arrhythmias. Circ Res. 2017;120:1969–93. https:// doi. org/ 10. 1161/ CIRCR 
ESAHA. 117. 310083.
 10. Eisner DA, Caldwell JL, Kistamas K, Trafford AW. Calcium and excitation-
contraction coupling in the heart. Circ Res. 2017;121:181–95. https:// doi. 
org/ 10. 1161/ CIRCR ESAHA. 117. 310230.
 11. Okita K, Matsumura Y, Sato Y, Okada A, Morizane A, Okamoto S, Hong H, 
Nakagawa M, Tanabe K, Tezuka K, et al. A more efficient method to gener-
ate integration-free human iPS cells. Nat Methods. 2011;8:409–12. https:// 
doi. org/ 10. 1038/ nmeth. 1591.
 12. Bolhaqueiro ACF, Ponsioen B, Bakker B, Klaasen SJ, Kucukkose E, van 
Jaarsveld RH, Vivie J, Verlaan-Klink I, Hami N, Spierings DCJ, et al. Ongoing 
chromosomal instability and karyotype evolution in human colorectal 
cancer organoids. Nat Genet. 2019;51:824–34. https:// doi. org/ 10. 1038/ 
s41588- 019- 0399-6.
 13. van Kampen SJ, Han SJ, van Ham WB, Kyriakopoulou E, Stouthart EW, 
Goversen B, Monshouwer-Kloots J, Perini I, de Ruiter H, van der Kraak 
P , et al. PITX2 induction leads to impaired cardiomyocyte function in 
arrhythmogenic cardiomyopathy. Stem Cell Reports. 2023;18:749–64. 
https:// doi. org/ 10. 1016/j. stemcr. 2023. 01. 015.

Page 12 of 13van Ham et al. Stem Cell Research & Therapy          (2024) 15:470 
 14. Goversen B, van der Heyden MAG, van Veen TAB, de Boer TP . The imma-
ture electrophysiological phenotype of iPSC-CMs still hampers in vitro 
drug screening: special focus on I(K1). Pharmacol Ther. 2018;183:127–36. 
https:// doi. org/ 10. 1016/j. pharm thera. 2017. 10. 001.
 15. Nemec J, Kim JJ, Salama G. The link between abnormal calcium handling 
and electrical instability in acquired long QT syndrome–Does calcium 
precipitate arrhythmic storms? Prog Biophys Mol Biol. 2016;120:210–21. 
https:// doi. org/ 10. 1016/j. pbiom olbio. 2015. 11. 003.
 16. Fink M, Noble PJ, Noble D. Ca(2)(+)-induced delayed afterdepolarizations 
are triggered by dyadic subspace Ca2(2)(+) affirming that increas-
ing SERCA reduces aftercontractions. Am J Physiol Heart Circ Physiol. 
2011;301:H921-935. https:// doi. org/ 10. 1152/ ajphe art. 01055. 2010.
 17. Shiferaw Y, Aistrup GL, Wasserstrom JA. Intracellular Ca2+ waves, afterde-
polarizations, and triggered arrhythmias. Cardiovasc Res. 2012;95:265–8. 
https:// doi. org/ 10. 1093/ cvr/ cvs155.
 18. Katra RP , Laurita KR. Cellular mechanism of calcium-mediated triggered 
activity in the heart. Circ Res. 2005;96:535–42. https:// doi. org/ 10. 1161/ 01. 
RES. 00001 59387. 00749. 3c.
 19. Liu MB, de Lange E, Garfinkel A, Weiss JN, Qu Z. Delayed afterdepolari-
zations generate both triggers and a vulnerable substrate promoting 
reentry in cardiac tissue. Heart Rhythm. 2015;12:2115–24. https:// doi. org/ 
10. 1016/j. hrthm. 2015. 06. 019.
 20. Leenhardt A, Glaser E, Burguera M, Nurnberg M, Maison-Blanche P , 
Coumel P . Short-coupled variant of torsade de pointes. A new electrocar-
diographic entity in the spectrum of idiopathic ventricular tachyarrhyth-
mias. Circulation. 1994;89:206–15. https:// doi. org/ 10. 1161/ 01. cir. 89.1. 206.
 21. Wang G, Zhong L, Chu H, Wang C, Zhu X. Short-coupled variant of tor-
sade de pointes: a systematic review of case reports and case series. Front 
Cardiovasc Med. 2022;9: 922525. https:// doi. org/ 10. 3389/ fcvm. 2022. 
922525.
 22. Shiga T, Shoda M, Matsuda N, Fuda Y, Hagiwara N, Ohnishi S, Watanabe 
A, Kasanuki H. Electrophysiological characteristic of a patient exhibit-
ing the short-coupled variant of torsade de pointes. J Electrocardiol. 
2001;34:271–5. https:// doi. org/ 10. 1054/ jelc. 2001. 24380.
 23. Guillen RH, Chort C, Mantilla L, Sriram CS, Gonzalez MD. Short coupled 
torsade de pointes: critical timing of the ventricular premature beats. J 
Electrocardiol. 2021;65:69–72. https:// doi. org/ 10. 1016/j. jelec troca rd. 2021. 
01. 006.
 24. Bogaard K, van der Steen MS, Tan HL, Tukkie R. Short-coupled variant of 
torsade de pointes. Neth Heart J. 2008;16:246–9. https:// doi. org/ 10. 1007/ 
BF030 86155.
 25. Van den Branden B, Wever E, Boersma L. Torsade de pointes with short 
coupling interval. Acta Cardiol. 2010;65:345–6. https:// doi. org/ 10. 2143/ 
AC. 65.3. 20503 53.
 26. Parikh SS, Blackwell DJ, Gomez-Hurtado N, Frisk M, Wang L, Kim K, Dahl 
CP , Fiane A, Tonnessen T, Kryshtal DO, et al. Thyroid and glucocorticoid 
hormones promote functional t-tubule development in human-induced 
pluripotent stem cell-derived cardiomyocytes. Circ Res. 2017;121:1323–
30. https:// doi. org/ 10. 1161/ CIRCR ESAHA. 117. 311920.
 27. Lundy SD, Zhu WZ, Regnier M, Laflamme MA. Structural and functional 
maturation of cardiomyocytes derived from human pluripotent stem 
cells. Stem Cells Dev. 2013;22:1991–2002. https:// doi. org/ 10. 1089/ scd. 
2012. 0490.
 28. Bannister ML, MacLeod KT, George CH. Moving in the right direction: 
elucidating the mechanisms of interaction between flecainide and the 
cardiac ryanodine receptor. Br J Pharmacol. 2022;179:2558–63. https:// 
doi. org/ 10. 1111/ bph. 15718.
 29. Hilliard FA, Steele DS, Laver D, Yang Z, Le Marchand SJ, Chopra N, Piston 
DW, Huke S, Knollmann BC. Flecainide inhibits arrhythmogenic Ca2+ 
waves by open state block of ryanodine receptor Ca2+ release channels 
and reduction of Ca2+ spark mass. J Mol Cell Cardiol. 2010;48:293–301. 
https:// doi. org/ 10. 1016/j. yjmcc. 2009. 10. 005.
 30. Hwang HS, Hasdemir C, Laver D, Mehra D, Turhan K, Faggioni M, Yin 
H, Knollmann BC. Inhibition of cardiac Ca2+ release channels (RyR2) 
determines efficacy of class I antiarrhythmic drugs in catecholaminer-
gic polymorphic ventricular tachycardia. Circ Arrhythm Electrophysiol. 
2011;4:128–35. https:// doi. org/ 10. 1161/ CIRCEP . 110. 959916.
 31. Do TQ, Knollmann BC. Inhibitors of intracellular RyR2 calcium release 
channels as therapeutic agents in arrhythmogenic heart diseases. Annu 
Rev Pharmacol Toxicol. 2024. https:// doi. org/ 10. 1146/ annur ev- pharm 
tox- 061724- 080739.
 32. Krause T, Gerbershagen MU, Fiege M, Weisshorn R, Wappler F. Dant-
rolene–a review of its pharmacology, therapeutic use and new develop-
ments. Anaesthesia. 2004;59:364–73. https:// doi. org/ 10. 1111/j. 1365- 2044. 
2004. 03658.x.
 33. Paul-Pletzer K, Yamamoto T, Ikemoto N, Jimenez LS, Morimoto H, Williams 
PG, Ma J, Parness J. Probing a putative dantrolene-binding site on the 
cardiac ryanodine receptor. Biochem J. 2005;387:905–9. https:// doi. org/ 
10. 1042/ BJ200 41336.
 34. Jung CB, Moretti A, Mederos y Schnitzler M, Iop L, Storch U, Bellin M, 
Dorn T, Ruppenthal S, Pfeiffer S, Goedel A, et al. Dantrolene rescues 
arrhythmogenic RYR2 defect in a patient-specific stem cell model of 
catecholaminergic polymorphic ventricular tachycardia. EMBO Mol Med. 
2012;4:180–91. https:// doi. org/ 10. 1002/ emmm. 20110 0194.
 35. Kobayashi S, Yano M, Suetomi T, Ono M, Tateishi H, Mochizuki M, Xu X, 
Uchinoumi H, Okuda S, Yamamoto T, et al. Dantrolene, a therapeutic 
agent for malignant hyperthermia, markedly improves the function of 
failing cardiomyocytes by stabilizing interdomain interactions within the 
ryanodine receptor. J Am Coll Cardiol. 2009;53:1993–2005. https:// doi. 
org/ 10. 1016/j. jacc. 2009. 01. 065.
 36. Yamamoto T, Ikemoto N. Spectroscopic monitoring of local conforma-
tional changes during the intramolecular domain-domain interaction of 
the ryanodine receptor. Biochemistry. 2002;41:1492–501. https:// doi. org/ 
10. 1021/ bi015 581z.
 37. Xiao L, Koopmann TT, Ordog B, Postema PG, Verkerk AO, Iyer V, Sampson 
KJ, Boink GJ, Mamarbachi MA, Varro A, et al. Unique cardiac Purkinje fiber 
transient outward current beta-subunit composition: a potential molecu-
lar link to idiopathic ventricular fibrillation. Circ Res. 2013;112:1310–22. 
https:// doi. org/ 10. 1161/ CIRCR ESAHA. 112. 300227.
 38. Ten Sande JN, Postema PG, Boekholdt SM, Tan HL, van der Heijden JF, de 
Groot NM, Volders PG, Zeppenfeld K, Boersma LV, Nannenberg EA, et al. 
Detailed characterization of familial idiopathic ventricular fibrillation 
linked to the DPP6 locus. Heart Rhythm. 2016;13:905–12. https:// doi. org/ 
10. 1016/j. hrthm. 2015. 12. 006.
 39. Harris K, Aylott M, Cui Y, Louttit JB, McMahon NC, Sridhar A. Comparison 
of electrophysiological data from human-induced pluripotent stem cell-
derived cardiomyocytes to functional preclinical safety assays. Toxicol Sci. 
2013;134:412–26. https:// doi. org/ 10. 1093/ toxsci/ kft113.
 40. Goldfracht I, Efraim Y, Shinnawi R, Kovalev E, Huber I, Gepstein A, Arbel G, 
Shaheen N, Tiburcy M, Zimmermann WH, et al. Engineered heart tissue 
models from hiPSC-derived cardiomyocytes and cardiac ECM for disease 
modeling and drug testing applications. Acta Biomater. 2019;92:145–59. 
https:// doi. org/ 10. 1016/j. actbio. 2019. 05. 016.
 41. Seibertz F, Sutanto H, Dulk R, Pronto JRD, Springer R, Rapedius M, Liutkute 
A, Ritter M, Jung P , Stelzer L, et al. Electrophysiological and calcium-han-
dling development during long-term culture of human-induced pluri-
potent stem cell-derived cardiomyocytes. Basic Res Cardiol. 2023;118:14. 
https:// doi. org/ 10. 1007/ s00395- 022- 00973-0.
 42. Joshi J, Albers C, Smole N, Guo S, Smith SA. Human induced pluripotent 
stem cell-derived cardiomyocytes (iPSC-CMs) for modeling cardiac 
arrhythmias: strengths, challenges and potential solutions. Front Physiol. 
2024;15:1475152. https:// doi. org/ 10. 3389/ fphys. 2024. 14751 52.
 43. Stutzman MJ, Kim CSJ, Tester DJ, Hamrick SK, Dotzler SM, Giudicessi JR, 
Miotto MC, Gc JB, Frank J, Marks AR, Ackerman MJ. Characterization of 
N-terminal RYR2 variants outside CPVT1 hotspot regions using patient 
iPSCs reveal pathogenesis and therapeutic potential. Stem Cell Rep. 
2022;17:2023–36. https:// doi. org/ 10. 1016/j. stemcr. 2022. 07. 002.
 44. Zhou Y, Huang W, Liu L, Li A, Jiang C, Zhou R, Wang J, Tan X, Huang CL, 
Zhang Y. Patient-specific induced pluripotent stem cell properties impli-
cate Ca(2+)-homeostasis in clinical arrhythmia associated with combined 
heterozygous RYR2 and SCN10A variants. Philos Trans R Soc Lond B Biol 
Sci. 2023;378:20220175. https:// doi. org/ 10. 1098/ rstb. 2022. 0175.
 45. Badone B, Ronchi C, Lodola F, Knaust AE, Hansen A, Eschenhagen T, Zaza 
A. Characterization of the PLN p.Arg14del mutation in human induced 
pluripotent stem cell-derived cardiomyocytes. Int J Mol Sci. 2021. https:// 
doi. org/ 10. 3390/ ijms2 22413 500.
 46. Simons E, Loeys B, Alaerts M. iPSC-derived cardiomyocytes in inherited 
cardiac arrhythmias: pathomechanistic discovery and drug development. 
Biomedicines. 2023. https:// doi. org/ 10. 3390/ biome dicin es110 20334.
 47. van Mil A, Balk GM, Neef K, Buikema JW, Asselbergs FW, Wu SM, Doev-
endans PA, Sluijter JPG. Modelling inherited cardiac disease using human 
induced pluripotent stem cell-derived cardiomyocytes: progress, pitfalls, 

Page 13 of 13
van Ham et al. Stem Cell Research & Therapy          (2024) 15:470 
 
and potential. Cardiovasc Res. 2018;114:1828–42. https:// doi. org/ 10. 1093/ 
cvr/ cvy208.
 48. Pioner JM, Santini L, Palandri C, Martella D, Lupi F, Langione M, Querceto 
S, Grandinetti B, Balducci V, Benzoni P , et al. Optical investigation of action 
potential and calcium handling maturation of hiPSC-cardiomyocytes on 
biomimetic substrates. Int J Mol Sci. 2019. https:// doi. org/ 10. 3390/ ijms2 
01537 99.
 49. Yang H, Yang Y, Lu Z, Zhang JZ. Simultaneous optical imaging of action 
potentials and calcium transients in human induced pluripotent stem 
cell-derived cardiomyocytes. Curr Protoc. 2024;4: e1101. https:// doi. org/ 
10. 1002/ cpz1. 1101.
 50. Prodan N, Ershad F, Reyes-Alcaraz A, Li L, Mistretta B, Gonzalez L, Rao Z, 
Yu C, Gunaratne PH, Li N, et al. Direct reprogramming of cardiomyocytes 
into cardiac Purkinje-like cells. iScience. 2022;25: 105402. https:// doi. org/ 
10. 1016/j. isci. 2022. 105402.
Publisher’s Note
Springer Nature remains neutral with regard to jurisdictional claims in pub-
lished maps and institutional affiliations.