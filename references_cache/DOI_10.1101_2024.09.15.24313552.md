---
reference_id: DOI:10.1101/2024.09.15.24313552
extractor_version: 1
title: A next generation CRISPR diagnostic tool to survey drug resistance in Human African Trypanosomiasis
authors:
- Elena Pérez Antón
- Annick Dujeancourt-Henry
- Brice Rotureau
- Lucy Glover
year: '2024'
doi: 10.1101/2024.09.15.24313552
content_type: full_text_pdf
is_preprint: true
peer_review_status: preprint
full_text_attempted: true
full_text_provider: openalex
full_text_url: "https://www.medrxiv.org/content/medrxiv/early/2024/09/17/2024.09.15.24313552.full.pdf"
oa_status: green
license: cc-by-nc-nd
local_pdf_path: files/DOI_10.1101_2024.09.15.24313552.pdf
full_text_access_type: open
---

# A next generation CRISPR diagnostic tool to survey drug resistance in Human African Trypanosomiasis
**Authors:** Elena Pérez Antón, Annick Dujeancourt-Henry, Brice Rotureau, Lucy Glover
**DOI:** [10.1101/2024.09.15.24313552](https://doi.org/10.1101/2024.09.15.24313552)

## Content

Abstract

                  The WHO aims to eliminate the
                  gambiense
                  form of human African trypanosomiasis (HAT) by 2030. With the decline of reported cases, maintaining efficient epidemiological surveillance is essential, including the emergence of drug-resistant strains. We have developed new highly specific diagnostic tools using Specific High-Sensitivity Reporter Enzymatic UnLOCKing (SHERLOCK) technology for monitoring the presence of drug-resistant genotypes that (1) are already circulating, such as the AQP2/3
                  (814)
                  chimera providing resistance to pentamidine and melarsoprol, or (2) could emerge, such as
                  Tb
                  CPSF3 (N
                  232
                  H), associated to acoziborole resistance in lab conditions. The melarsoprol - pentamidine
                  
                    AQP2/3
                    (814)

                  SHERLOCK assay detected RNA from both cultured parasites and field isolated strains from gHAT patients in relapse following treatment. The acoziborole
                  
                    CPSF3
                    (SNV)

                  SHERLOCK assay discriminated between wild-type
                  CPSF3
                  RNA and
                  CPSF3
                  with a single A-C mutation that confers resistance to acoziborole
                  in vitro
                  .

 1 
A next generation CRISPR diagnostic tool to survey drug resistance in Human African 1 
Trypanosomiasis.  2 
 3 
Authors and affiliations 4 
Elena Pérez Antón1, Annick Dujeancourt-Henry1, Brice Rotureau2,3*, Lucy Glover1* 5 
 6 
1Trypanosome Molecular Biology Unit, Institut Pasteur, Université de Paris, Paris, France 7 
2Trypanosome Transmission Group, Trypanosome Cell Biology Unit, INSERM U1201, Institut 8 
Pasteur, Université de Paris, Paris, France 9 
3Parasitology Unit, Institut Pasteur of Guinea, Conakry, Guinea 10 
*Corresponding authors: lucy.glover@pasteur.fr; brice.rotureau@pasteur.fr 11 
 12 
 13 
 14 
 15 
 16 
 17 
 18 
 19 
Keywords  20 
Human African trypanosomiasis, Trypanosoma brucei gambiense , SHERLOCK, crRNA, 21 
Cas13a, drug-resistance, acoziborole, melarsoprol, pentamidine.  22 
 23 
 24 
 25 
 26 
 27 
 28 
 29 
 30 
 31 
 . CC-BY-NC-ND 4.0 International licenseIt is made available under a 
perpetuity. 
 is the author/funder, who has granted medRxiv a license to display the preprint in(which was not certified by peer review)preprint 
The copyright holder for thisthis version posted September 17, 2024. ; https://doi.org/10.1101/2024.09.15.24313552doi: medRxiv preprint 
NOTE: This preprint reports new research that has not been certified by peer review and should not be used to guide clinical practice.

 2 
Abstract 32 
The WHO aims to eliminate the gambiense form of human African trypanosomiasis (HAT) by 33 
2030. With the decline of reported cases, maintaining efficient epidemiological surveillance is 34 
essential, including the emergence of drug -resistant strains. We have developed new highly 35 
specific diagnostic tool s using Specific High -Sensitivity Reporter Enzymatic UnLOCKing 36 
(SHERLOCK) technology for monitoring the presence of drug-resistant genotypes that (1) are 37 
already circulating, such as the AQP2/3 (814) chimera providing resistance to pentamidine and 38 
melarsoprol, or (2) could emerge, such as  TbCPSF3 (N 232H), associated to acoziborole 39 
resistance in lab conditions.  The melarsoprol - pentamidineAQP2/3(814) SHERLOCK assay 40 
detected RNA from both cultured parasites and field isolated strains from gHAT patients in 41 
relapse following treatment. The acoziborole  CPSF3(SNV)SHERLOCK assay discriminated 42 
between wild-type CPSF3 RNA and CPSF3 with a single A-C mutation that confers resistance 43 
to acoziborole in vitro. 44 
 45 
Introduction 46 
Human African trypanosomiasis (HAT), or sleeping sickness, is one of the 21 conditions 47 
identified as a neglected tropical diseases by the World Health Organization (WHO) 1. Caused 48 
by an infection with the extracellular protozoan parasite Trypanosoma (T) brucei (b) gambiense 49 
(gHAT) in West and Central Africa or T. b. rhodesiense (rHAT) in East and Southern Africa. 50 
HAT infections follow a typical clinical pattern, initiating with intermittent fever and 51 
lymphadenopathy during a first step of blood and lymph infection (stage 1) and advancing to 52 
severe neurological symptoms when the parasites invade the cerebrospinal fluid (stage 2), and 53 
ultimately death if untreated. The major difference in disease progression between T. b.  54 
gambiense and T. b. rhodesiense is that the former is chronic lasting over several months to 55 
years and the latter acute, lasting for several weeks. There is currently no prophylactic drug 56 
available for HAT, the approved chemotherapies depend on the parasite species and the stage 57 
of the disease1. For gHAT, children under the age of 6 or less than 20 kg are, as a first choice, 58 
treated with pentamidine for stage 1 or NECT for stage 2. Patients older than 6 years old and 59 
more than 20 kgs are treated with fexinidazole at stage 1, or with fexinidazole (if white blood 60 
cell count in the cerebrospinal fluid is lower than 100/μL) or NECT at stage 2 2. If relapse is 61 
detected, patients are treated with NECT. For rHAT, children under the age of 6 or less than 20 62 
kg are treated with suramin as a first choice for stage 1 or melarsoprol for stage 2, and if relapse 63 
 . CC-BY-NC-ND 4.0 International licenseIt is made available under a 
perpetuity. 
 is the author/funder, who has granted medRxiv a license to display the preprint in(which was not certified by peer review)preprint 
The copyright holder for thisthis version posted September 17, 2024. ; https://doi.org/10.1101/2024.09.15.24313552doi: medRxiv preprint 

 3 
is seen, fexinidazole may be given for compassionate use 2. Patients older than 6 years old and 64 
more than 20 kgs are treated with fexinidazole for both stage 1 and 2, yet if relapse is detected, 65 
patients are treated with suramin or melarsoprol 2. Both suramin and pentamidine require 66 
prolonged intravenous administration, melarsoprol causes encephalopathic syndrome that is 67 
fatal in up to one in ten patients and NECT involves a long and complex dose regime with 68 
intravenous eflornithine alongside oral nifurtimox over the course of two weeks at hospital 3. 69 
These drugs present either with side effects or, are logistically challenging to administer. 	70 
Accurate diagnosis and staging of the disease are key for the selection of the appropriate drug 71 
treatment, but diagnosis is based on a tedious algorithm, including lumbar puncture as a 72 
confirmatory test for the most advanced stage of gHAT4. The high toxicity of some of these 73 
drugs, especially melarsoprol, as well as the complex administration of NECT make access to 74 
treatment challenging and have prevented implementation of mass treatment as a method of 75 
combating the disease 5. 	76 
Fexinidazole was approved in 2019 by the European Medicines Agency 6, as a 10-day oral 77 
treatment regime that must be taken with food for optimal absorption, yet with treatment 78 
emergent adverse events such as vomiting and nausea increases the risk of non-compliance 5,7. 79 
Due to the high-risk of non-compliance leading to the ingestion of suboptimal curative doses, 80 
the possibility of relapse is of concern – especially as it may occur late, up to 24 months post-81 
treatment 5, which could increase the risk of the emergence of drug-resistance. Resistance to 82 
fexinidaxole is readily generated under laboratory conditions 8 and occurs through a similar 83 
mechanism as that to nifurtimox, via mutation of the nitroreductase (NTR) gene 8. Therefore, 84 
there already exists the potential that previous use of nifurtimox in the field may have already 85 
led to the emergence of fexinidazole resistant parasites 9. Fexinadazole is currently the only oral 86 
drug approved for treatment of both stage 1 and 2 gHAT and rHAT 2,5. Drug resistance is not 87 
uncommon in the treatment of HAT, melarsoprol resistance emerged as early as 1970 and was 88 
widespread by 1990 10,11, while resistance to both eflornithine and nifurtimox can be generated 89 
in vitro 3. 90 
In a context where the therapeutic arsenal for treating HAT is limited, the emergence of drug 91 
resistance is possible where a selective pressure to survive is applied to parasites, placing both 92 
existing and potential future drug treatments at risk. Pentamidine and melarsoprol share the 93 
same mechanism of entry into the parasite cell through the adenosine transporters and the 94 
aquaglyceroporin channels (AQPs) 10,12. Among the three aquaglyceroporin genes of T. brucei 95 
(TbAQP1-3) 13, the deletion of the AQP2 locus is related to the melarsoprol-pentamidine cross-96 
resistance in bloodstream-forms, increasing their effective concentrations (EC50) by 2- to 15-97 
 . CC-BY-NC-ND 4.0 International licenseIt is made available under a 
perpetuity. 
 is the author/funder, who has granted medRxiv a license to display the preprint in(which was not certified by peer review)preprint 
The copyright holder for thisthis version posted September 17, 2024. ; https://doi.org/10.1101/2024.09.15.24313552doi: medRxiv preprint 

 4 
fold, respectively 12. Several distinct mutations in the AQP2-AQP3 genes have been associated 98 
with relapse of HAT after treatment with melarsoprol in patients from the Mbuji -Mayi region 99 
of the Democratic Republic of the Congo 14,15 and the Mundri county of South Sudan14,16 . One 100 
specific chimera identified, a chimera containing the first 813 bp from  AQP2 and the last 126 101 
bp from  AQP3, here termed AQP2/AQP3(814), 15, was associated with cross -reactivity to 102 
melarsoprol and pentamidine 14. 103 
Although not a frontline drug yet, acoziborole promises to be key in the efforts to eliminate 104 
HAT. Currently in phase III clinical trials, acoziborole could be approved for the treatment of 105 
both stages of gHAT by 2026 17, it is a single oral dose benzoxaborole derivative that shows 106 
high efficacy and safety. Its approval could eliminate the need for routine lumbar puncture and 107 
would allow the treatment of parasitology-negative suspects, as well as making treatment more 108 
accessible to patients living in remote areas 17,18. The drug molecule binds to the active site of 109 
the Cleavage and Polyadenylation Specificity Factor 3 (CPSF3), which is involved in 110 
trypanosome mRNA processing 19, inhibits polypeptide translation and reduces endocytosis of 111 
haptoglobin-hemoglobin 20. However, resistance to acoziborole can be generated in vitro, 112 
through editing a single nucleotide in the CPSF3 sequence 21.  113 
The CRISPR based diagnostic - Specific High-sensitivity Enzymatic Reporter unLOCKing 114 
(SHERLOCK) - first amplifies nucleic acid using recombinase polymerase amplification 115 
(RPA), which is then combined with the Cas13a nuclease, for target recognition via specific 116 
guides, and a fluorescent reporter linked to a quencher by nucleotides. Target sequence 117 
recognition activates Cas13a’s ‘collateral effect’ of promiscuous ribonuclease activity. So far, 118 
SHERLOCK diagnostic assays have been developed for two protozoan parasites, African 119 
trypanosomes22 and Plasmodium23. SHERLOCK is capable of detecting a few attomoles (10-18 120 
moles) of nucleic acids in a sample and its specificity was demonstrated by distinguishing 121 
between closely related Zika and dengue viruses in clinical isolates, or mutant strains with 122 
unique SNPs 24-26. Here, we developed highly specific SHERLOCK assays that allow detection 123 
of specific drug-resistance associated mutations and that could be essential for epidemiological 124 
surveillance in the context of gHAT elimination and rHAT control. 125 
  126 
 . CC-BY-NC-ND 4.0 International licenseIt is made available under a 
perpetuity. 
 is the author/funder, who has granted medRxiv a license to display the preprint in(which was not certified by peer review)preprint 
The copyright holder for thisthis version posted September 17, 2024. ; https://doi.org/10.1101/2024.09.15.24313552doi: medRxiv preprint 

 5 
Methods 127 
Trypanosome and RNA material 128 
T. b. brucei Lister 427 bloodstream form cells were cultured in HMI -11 medium with 10 % 129 
foetal bovine serum (Sigma -Aldrich) at 37 °C with 5% CO 2. RNA extraction was carried out 130 
from culture harvest at 1x10 6 cell/mL. RNA extraction of T. b. brucei  cells, T. b. gambiense  131 
cell pellets, and human embryonic kidney (HEK) 293T cells were carried using the RNeasy 132 
Mini kit (Qiagen). Lyophilized RNA extracted from T. b. brucei  edited CPSF3 19 was 133 
resuspended in nuclease-free water. 134 
 135 
Table 1: Trypanosome strains and isolates used in this study. 136 
 137 
LwCas13a enzyme expression and purification 138 
The plasmid pC013-Twinstrep-SUMO-huLwCas13a (Addgene plasmid #90097) was used for 139 
the protein expression in Escherichia coli RosettaTM 2(DE3) pLysS competent cells 25. The 140 
protein expression and purification of Leptotrichia wadei Cas13a (LwCas13a) enzyme was 141 
performed as described in27 with slight modifications 22. TB medium was reconstituted by 142 
adding 47.8 g of TB powder to a 1-L flask, adding 8 mL of 100% (wt/vol) glycerol. Cell pellet 143 
was lysed with supplemented lysis buffer composed by 2 complete Ultra EDTA-free tablets 144 
(Roche), 500 mM NaCl, 100 mg lysozyme and 125-625 ng Deoxyribonuclease I from bovine 145 
pancreas (Sigma) to each 100 mL of lysis buffer. The LwCas13a was storage in single-use 146 
aliquots at -80°C to avoid freeze-thaw cycles. 147 
Design of RPA primers and crRNA 148 
     
Species Strain Phenotype Source Ref 
T. b. brucei Wild type -  in vitro  
T. b. brucei AQP2/3 chimera Resistance to melarsoprol in vitro 15 
T. b. brucei CPFS3 A-C mutant Resistanec to acoziborole in vitro 19 
T. b. gambiense Wild type - in vitro  
T. b. gambiense 163AT Resistance to melarsoprol Human 15 
T. b. gambiense 348BT Resistance to melarsoprol Human 15 
T. b. gambiense MBA AQP2/3 chimera – no resistance Human 15 
T. b. gambiense 40AT Resistance to melarsoprol Human 14,15 
T. b. gambiense 349 AT Resistance to melarsoprol Human 14,15 
T. b. gambiense K03048 Resistance to melarsoprol Human 14,16 
T. b. gambiense Wild type - Human 15 
 . CC-BY-NC-ND 4.0 International licenseIt is made available under a 
perpetuity. 
 is the author/funder, who has granted medRxiv a license to display the preprint in(which was not certified by peer review)preprint 
The copyright holder for thisthis version posted September 17, 2024. ; https://doi.org/10.1101/2024.09.15.24313552doi: medRxiv preprint 

 6 
RPA primer pairs were designed using NCBI Primer -BLAST 28 using the custom parameters 149 
specified in 27. For the wild -type CPSF3 SHERLOCK we use the reference sequence 150 
XM_839191.1 (Tb927.4.1340). For targeting the chimeric AQP2/AQP3 (814) the reference 151 
sequence KF564935.1 (T. b. gambiense strain 40AT) was used. The RPA primers used in the 152 
study are included in Supplementary Table 1. RPA forward primers include at the 5' end, the 153 
T7 promoter sequence (5’ -GAAATTAATACGACTCACTATAGGG-3’) that allow in vitro  154 
transcription of the amplified target by T7 polymerase. 155 
The DNA templates used to generate the crRNAs consist of: 1) the target sequence (5'-3') which 156 
will be the variable region between crRNA, also known as the spacer (with variable lengths 157 
from 20 to 28 nt), followed by 2) the direct repeat template common to all LwCas13a crRNAs 158 
(5'-GTTTTAGTCCCCTTCGTTTTTGGGGTAGTCTAGTCTAAATC-3'), followed by 3) the 159 
T7 promoter sequence at the 3' end (5'-CCCTATATAGTGAGTCGTATTAATTTC-3'), which 160 
will allow in vitro transcription of the guides. DNA templates used are listed in Supplementary 161 
Table 1. All of the oligonucleotides mentioned were synthesized by ThermoFisher. 162 
In vitro transcription and purification of crRNAs 163 
The crRNA synthesis was carried out using a DNA template and in vitro transcription mediated 164 
by T7 polymerase according to manufacturer’s instructions using the HiScribe ™ T7 Quick 165 
High Yield RNA Synthesis Kit (NEB), as previously described 27. Briefly, we first annealed 166 
the crRNA DNA template and T7 -3G oligonucleotide (5’ -167 
GAAATTAATACGACTCACTATAGGG-3’) by denaturation for 5 min followed by slow 168 
cooling 22. After in vitro  transcription, the crRNAs were purified using magnetic beads 169 
(Agencourt RNAClean XP) and stored at 300 ng/ µL in single -use aliquots at -80°C to avoid 170 
freeze-thaw cycles.  171 
SHERLOCK assay 172 
The Specific High Sensitivity Enzymatic Reporter unLOCKing (SHERLOCK) assay was 173 
performed as described in27. The SHERLOCK reaction is a combination of a pre-amplification 174 
method by a reverse transcription (RT) recombinase polymerase amplification (RPA) 29 and a 175 
specific RNA -target recognition by Cas13 -CRISPR RNA -guide (crRNA) machinery 176 
(Abudayyeh et al., 2016) . The RT -RPA was carried out using the TwistAmp Basic kit 177 
(TwistDx) following manufacturer’s instructions for 45 min at 42 °C as described by 22. The 178 
amplification step is followed by simultaneous in vitro transcription of the amplified target by 179 
 . CC-BY-NC-ND 4.0 International licenseIt is made available under a 
perpetuity. 
 is the author/funder, who has granted medRxiv a license to display the preprint in(which was not certified by peer review)preprint 
The copyright holder for thisthis version posted September 17, 2024. ; https://doi.org/10.1101/2024.09.15.24313552doi: medRxiv preprint 

 7 
T7 polymerase (Biosearch technology) and detection of the LwCas13a-crRNA using the same 180 
condition as described by 22. For this purpose, 4 µL of the RT -RPA product of each replicate 181 
was mixed with the following components in the following concentrations: 20 mM HEPES pH 182 
6. 5, 9 mM MgCl2, 1 mM rNTP mix (NEB), 40 nM of LwCas13a, 2 U of Murine RNase 183 
inhibitor (NEB), 25 U of NxGen T7 RNA Polymerase (Biosearch technology), 25 nM of 184 
crRNA and 125 nM of RNaseAlert probe V2 (Invitrogen), in a final volume of 80 µL. The 185 
reaction was performed in 384-well plates, F-bottom, μClear bottom (Greiner) incubated at 37 186 
°C in a TECAN plate reader (INFINITE F200 PRO M PLEX), in which 20 µL x 3 of each 187 
replicate reaction was distributed. Fluorescence measurements were collected every 10 minutes 188 
up to 3 hours. All SHERLOCK reactions were performed in triplicate and three fluorescence 189 
measurements were taken from each replicate. A negative control template (NCT) was added 190 
in parallel to each independent assay by supplementation nuclease-free water as input. 191 
Statistical analysis 192 
The fluorescence intensity values obtained from the TECAN plate reader were analysed using 193 
Excel. For each triplicate reaction at each timepoint, the mean fluorescence intensity value was 194 
divided by the mean of the fluorescence intensity value of the NCT at the same timepoint, to 195 
obtain the fold-change over background fluorescence. The formula used is as follows: 196 
 197 
Fold − change	over	background	fluorescence	198 
= 	 Mean	fluorescence	intensity	of	a	triplicate	sample	reaction	at	time	(x)
Mean	fluorescence	intensity	of	the	triplicate	NCT	at	time	(x) 	 199 
 200 
The graphs and statistical analysis were performed using GraphPad Prism (version 9.3.1) 201 
software. The Shapiro-Wilk normality test was performed to evaluate the type of data 202 
distribution. The non-parametric Mann-Whitney U test or the parametric bilateral unpaired t-203 
test, with Welch’s correction, according to the data distribution results, were used for the 204 
statistical comparison with 95% confidence interval. For multiple comparisons, we applied the 205 
two-stage linear step-up procedure 30. Multiple sequence alignments were performed using 206 
Clustal Omega 31. 207 
 208 
Results  209 
 . CC-BY-NC-ND 4.0 International licenseIt is made available under a 
perpetuity. 
 is the author/funder, who has granted medRxiv a license to display the preprint in(which was not certified by peer review)preprint 
The copyright holder for thisthis version posted September 17, 2024. ; https://doi.org/10.1101/2024.09.15.24313552doi: medRxiv preprint 

 8 
Selection of SHERLOCK targets to detect the AQP2/AQP3(814) chimera.  210 
We adapted our SHERLOCK4HAT 22 workflow for the detection of markers of resistance to 211 
melarsoprol through the formation of an AQP2/3 chimera (Figure 1A). The AQP2/3(814) chimera 212 
independently arose in two distinct HAT foci to currently made up 31.7 % of all known 213 
melarsoprol resistant HAT infections 14,15. The RPA forward primer amplified from nucleotide 214 
position 705 of the AQP2 sequence, and the RPA reverse primer from position 841, which was 215 
specific to the region AQP3 sequence of the chimera (Figure 1B). The sequences of the wild 216 
type (WT) AQP2 and AQP3 (Tb927.10.14170, Tb927.10.14160, respectively) and that of the 217 
AQP2/3(814) chimera (KF564931.1) were aligned to select non -homologous regions between 218 
AQP2 and AQP3 genes for the new primers binding sites (Figure 1B). The crRNA guides were 219 
designed to target the region of the AQP2/3(814) chimera that was analogous to AQP2 (Figure 220 
1B). We evaluated three crRNA for the ability to discriminate between RNAs extracted from 221 
in vitro derived cells where both AQP2 and AQP3 were knocked out and the AQP2/3(814) 222 
chimera was expressed from the rRNA intergenic region 32, and from wild type T. b. gambiense 223 
or T. b. brucei cells (Figure 1C). The three crRNAs specifically detected the cells expressing 224 
the AQP2/3(814) chimera and did not cross-react with the WT trypanosomes or human cells 225 
(Figure 1C).  226 
The AQP2/AQP3(814)-specific SHERLOCK assay can be used to identify samples from 227 
cases of HAT relapses. 228 
After demonstrating that the AQP2/AQP3(814)-specific SHERLOCK assay was able to detect 229 
RNA from in vitro modified cells, we wanted to investigate whether it could also detect 230 
AQP2/AQP3(814)-chimeric RNAs of parasites isolated from patients, from two geographically 231 
distinct locations, showing relapses following treatment with melarsoprol in the Mbuji-Mayi 232 
region of the Democratic Republic of the Congo and Mundri County in South Sudan (Figure 233 
2A), which have been associated with mutations in the AQP2/3 genes14-16 (Figure 2B). We 234 
tested 4 isolates: (1) a WT strain from a patient infected with T. b. gambiense with no mutation 235 
in the AQP2/3 locus and no relapse; (2) the 163AT, 40AT, 349AT and K03048 strains from 236 
patients with HAT relapse infected with T. b. gambiense bearing the AQP2/AQP3(814) 237 
mutation14-16; (3) the MBA strain from a patient with unknown treatment outcome, infected 238 
with T. b. gambiense containing an AQP2/3 chimera with the first 677 bp from  AQP2, 202 bp 239 
of AQP3 and the last 60 bp from  AQP2, termed as  AQP2/3(678–880); and the 348BT strain 240 
isolated from a cured patient that contains both  AQP2/3(814) and AQP2/3(880) (first 879 bp 241 
 . CC-BY-NC-ND 4.0 International licenseIt is made available under a 
perpetuity. 
 is the author/funder, who has granted medRxiv a license to display the preprint in(which was not certified by peer review)preprint 
The copyright holder for thisthis version posted September 17, 2024. ; https://doi.org/10.1101/2024.09.15.24313552doi: medRxiv preprint 

 9 
from AQP2, a point mutation at T869C and the last 60 bp from  AQP3) chimeras (Figure 2B) 242 
15.  243 
The sequences of the wild type AQP2 and 3, the AQP2/3(814) chimera (KF564931.1), 244 
AQP2/3(880) (KM282050) and AQP2/3(678-880) (KM282034) were aligned to select non -245 
homologous regions between AQP2 and AQP3 genes to design a second RPA primer pair 246 
(Figure 2B, Supplementary table 1): the selected RPA forward primer amplified from 247 
nucleotide position 730 of the AQP2 sequence, and the RPA reverse primer from position 829 248 
of the chimera sequence corresponding to the AQP3 sequence. Our crRNA guides should not 249 
target the AQP2/3(880) (KM282050) or AQP2/3(678-880) (KM282034) chimeras (Figure 2B and 250 
C). We first screened the samples using two pairs of RPA primer and two crRNA guides 251 
(Supplementary figure 1A). The crRNA2 and RPA primer pair 1 were selected to assess the 252 
samples and this SHERLOCK assay was shown to accurately discriminate between patient 253 
samples that contained the AQP2/3(814) chimera or not (Figure 2D). As expected, the 163AT, 254 
40AT, 349AT and 348 BT samples showed a robust signal in the SHERLOCK AQP2/3(814) 255 
assay. The K03048 sample from South Sudan scored as positive in the assay, yet it showed a 256 
lower fold-change, likely because the amount of RNA extracted from this sample was low 257 
(Figure 2D). These results confirm that the SHERLOCK AQP2/3(814) assay can detect the 258 
specific mutation associated with melarsoprol resistance from patient samples.  259 
SHERLOCK detection of a single nucleotide variant in the CPSF3 gene. 260 
Taking advantage of the specificity of SHERLOCK, we developed an assay that can 261 
discriminate between the WT and the in vitro derived single nucleotide variant (SNV) of the 262 
CPSF3 gene (CPSF3(SNV), accession number XM_839191: N232H, AAT-CAT), hereon referred 263 
to as CPSF3(SNV) which confers resistance to acoziborole 19,33. We first screened RPA primer 264 
pairs that were either 30 nt or 25 nt long (Supplementary figure 1B) and designed to amplify 265 
the region containing the SNV. The RPA primer pair target amplification was assessed using 266 
four different crRNA guides specific for the detection of CPSF3(SNV). We observed higher fold-267 
change values with the 30 nt RPA primer pair as compared to the 25 nt primer pair 268 
(Supplementary Figure 1B). Therefore, we selected the long RPA primer pair for subsequent 269 
optimization of the SHERLOCK assay. 270 
Then, 12 crRNA guides were screened for detection of the CPSF3(SNV). We designed crRNAs 271 
using the following criteria: 1) setting the SNV complementary base at position 3 (counting 272 
from the 3' end of the crRNA) and the artificial mismatch (if any) at position 5; and 2) setting 273 
 . CC-BY-NC-ND 4.0 International licenseIt is made available under a 
perpetuity. 
 is the author/funder, who has granted medRxiv a license to display the preprint in(which was not certified by peer review)preprint 
The copyright holder for thisthis version posted September 17, 2024. ; https://doi.org/10.1101/2024.09.15.24313552doi: medRxiv preprint 

 10 
the SNV complementary base at position 6 and the mismatch (if any) at position 4 23,25,34 (Figure 274 
3A). In addition, we designed crRNAs with spacer lengths shorter than described as optimal for 275 
LwCas13a (28 nt, 27). Indeed, reducing the spacer length to a maximum of 20 nt reduced the 276 
enzyme activity but maintained, or even improved, its ability to discriminate single mismatches 277 
by reducing background fluorescence in the off-target sample 25,34,35 (Figure 3B). Finally, since 278 
consecutive double substitutions in the spacer have been described as effective in the loss of 279 
collateral cleavage activity of the Cas13a enzyme 35, we also evaluated the efficacy of placing 280 
the synthetic mismatch adjacent to our SNV, in order to generate a double mismatch in the off-281 
target sequence (Figure 3B).  282 
The crRNAs designed to detect the SNV at position 3 showed lower fluorescence emission and 283 
were undetectable when using the crRNAs with a spacer length of 20 or 23 nt (Figure 3B). In 284 
contrast, the crRNAs detecting the SNV at position 6 gave high fluorescence intensity values 285 
with both WT and CPSF3(SNV). The fluorescence was reduced only when the length of the spacer 286 
was limited to 20 nt (Figure 3B). The best performing crRNA guide contained the SNV 287 
complementary base at position 6 and a synthetic mismatch at position 4, with a spacer length 288 
of 20 nt (Figure 3B). We then evaluated whether the nucleotide selected as the artificial 289 
mismatch could improve the specificity of the SHERLOCK CPSF3(SNV) assay. We selected the 290 
best candidate obtained in the first screening (Figure 3B), which used an uracil (U) as the 291 
mismatch (Figure 4A), as well as two other crRNAs, one using cytosine (Figure 4B) and the 292 
other guanine (Figure 4C) as the artificial mismatch.  Using either an uracil or a guanine base 293 
as mismatch, the SHERLOCK assays showed statistically significant difference in fluorescence 294 
intensity when comparing total RNAs from CPSF3(SNV) to WT RNA (Figure 4A and C). Using 295 
a guanine, the fluorescence from the off-target (WT) sequence was reduced to near background 296 
(Figure 4C). These data show that the SHERLOCK assay can be used to detect SNV in T. brucei 297 
cells resistant to acoziborole. 298 
Discussion 299 
Here we describe the development of new drug resistance SHERLOCK assays  for HAT that 300 
could be used for  epidemiological surveillance. There are currently no molecular diagnostics 301 
that can screen for emerging drug resistance in HAT patients, yet resistance to all the currently 302 
approved drugs used to treat HAT has been detected either in the field or can be generated in a 303 
laboratory. The two  SHERLOCK assays described here  can distinguish WT and either gene 304 
chimera’s or SNV  targets. As an RNA diagnostic, these SHERLOCK assays can be used to 305 
 . CC-BY-NC-ND 4.0 International licenseIt is made available under a 
perpetuity. 
 is the author/funder, who has granted medRxiv a license to display the preprint in(which was not certified by peer review)preprint 
The copyright holder for thisthis version posted September 17, 2024. ; https://doi.org/10.1101/2024.09.15.24313552doi: medRxiv preprint 

 11 
screen patients presenting relapse after treatment and could be used to discriminate between 306 
relapse or reinfection, which is critical for adapting drug treatment.  307 
 308 
Although no longer used for the treatment of gHAT, melarsoprol is still recommended by the 309 
WHO for treatment of rHAT at stage 2 in children or as a second option in adults. Unlike gHAT, 310 
rHAT is an acute infection, with disease progression taking from weeks to months. Resistance 311 
to melarsoprol would, therefore, represent a significant obstacle to control rHAT. In this study, 312 
we have developed a SHERLOCK assay targeting mutations in the AQP2/3 locus that were 313 
initially identified in circulating parasites by sequencing samples from patients with relapses 314 
after treatment14,15 . Our high-throughput AQP2/3(814) SHERLOCK assay detected all parasites 315 
involved in relapses without cross reactivity and could be quickly implemented in reference 316 
labs in the field. One limitation of using SHERLOCK for detecting drug resistance is the 317 
intrinsic dependency of the method on prior knowledge of the gene mutations for the design of 318 
RPA primers and crRNAs. However, by using our existing SHERLOCK4HAT workflow 22, 319 
the assay could rapidly be adapted and implemented once a mutation has been identified.  320 
 321 
Acoziborole will likely become the next frontline drug for the treatment of gHAT to move 322 
towards elimination of the disease by 2030 17,36. Like for the other drugs used to treat HAT, 323 
resistance to acoziborole can be generated in the laboratory through a single point mutation in 324 
the CPSF3 gene 19,33. Several SHERLOCK assays have been developed to detect SNV 23,25,34, 325 
and LwCas13a, used in this study, is capable of tolerating mismatches, yet with a reduced 326 
cutting efficient 37. This could be ameliorated by optimising the crRNA guide length, the 327 
positioning of the mismatch, and/or the Cas13 variant used 34. In our CPSF3(SNV) SHERLOCK 328 
assay, we found that the most efficient combination was a 20 nt crRNA, the SNV at position 6 329 
and the synthetic mismatch at position 4. Within the CPSF3(SNV) SHERLOCK assay, there is 330 
still scope for optimisation to improve the specificity of the assay and which Cas13 variant 331 
could provide better on vs. off target discrimination.  In our assays, the nucleotide selected for 332 
the mismatch had the most profound effect on the sensitivity of the assay, especially in the 333 
discrimination between on and off target. Here, the use of a guanine as the mismatch at position 334 
4 showed the best discrimination between the two targets. Should resistance arise from a SNV 335 
or a chimeric gene formation, fully exploiting how the Cas13a-RNA complex is formed will be 336 
key to developing a robust assay for epidemiological surveillance. 337 
 . CC-BY-NC-ND 4.0 International licenseIt is made available under a 
perpetuity. 
 is the author/funder, who has granted medRxiv a license to display the preprint in(which was not certified by peer review)preprint 
The copyright holder for thisthis version posted September 17, 2024. ; https://doi.org/10.1101/2024.09.15.24313552doi: medRxiv preprint 

 12 
This study demonstrates the versatility of the SHERLOCK technology to detect known genetic 338 
modifications directly associated to drug resistance, using existing workflows. The major 339 
challenge to develop a SHERLOCK assay is that the targeted genetic mutation must be both 340 
known and stable. However, for rHAT treatment with melarsoprol, we showed that known 341 
resistance mechanisms through the formation of chimeras, that have arisen in geographically 342 
separated regions, are suitable targets for SHERLOCK. Given the adaptability of SHERLOCK, 343 
generating a HAT antimicrobial resistance toolbox will be an invaluable asset for 344 
epidemiological surveillance to screen any cases of relapse. This will be critical not only to 345 
track the incidence of resistance, but also for subsequent selection of the most individually 346 
adapted drug treatment.  347 
 348 
Abbreviations 349 
AQP: Aquaglyceroporin  350 
CPSF3: Cleavage and polyadenylation specific factor 3 351 
CRISPR: Clustered regularly interspaced short palindromic repeats 352 
crRNA: CRISPR RNA 353 
HAT: Human African trypanosomiasis 354 
HEK: Human embryonic kidney 355 
LwCas13a: Leptotrichia wadei CRISPR-associated protein 13 a 356 
NCT: Negative control template 357 
NECT: Nifurtimox- eflornithine combination therapy 358 
PAM: Protospacer adjacent motif 359 
 . CC-BY-NC-ND 4.0 International licenseIt is made available under a 
perpetuity. 
 is the author/funder, who has granted medRxiv a license to display the preprint in(which was not certified by peer review)preprint 
The copyright holder for thisthis version posted September 17, 2024. ; https://doi.org/10.1101/2024.09.15.24313552doi: medRxiv preprint 

 13 
RPA: Recombinase polymerase amplification 360 
RT: Reverse transcription 361 
SHERLOCK: Specific High-sensitivity Enzymatic Reporter unlocking 362 
SNV: Single nucleotide variant 363 
SUMO: Small ubiquitin-like modifier 364 
WT: Wild-type 365 
Acknowledgments 366 
The authors acknowledge the support of the researchers who made this work possible by 367 
providing the necessary genetic materials: T. b. gambiense ELIANE cell pellets were provided 368 
by Pr. Annette MacLeod (University of Glasgow, UK); lyophilized RNA extracted from 369 
CPSF3-edited T. b. brucei were provided by Pr. David Horn (University of Dundee, UK); RNA 370 
from chimeric AQP2/AQP3 T. b. gambiense isolates were provided by Dr. Nick Van Reet 371 
(Institute of Tropical Medicine, Antwerp) and Pr. Pascal Maeser (Swiss Tropical and Public 372 
Health Institute, Switzerland). 373 
Author contribution 374 
EPA, BR and LG conceived and designed the experiments. EPA and ADH performed the 375 
experiments. EPA, BR and LG analysed the data. BR and LG contributed reagents, materials 376 
and analysis tools. EPA, BR and LG wrote the paper. 377 
Funding 378 
This project has received funding from the Agence Nationale pour la Recherche (ANR-PRC 379 
2021 SherPa). The funders had no role in study design, data collection and analysis, decision 380 
to publish, or preparation of the manuscript. 381 
 . CC-BY-NC-ND 4.0 International licenseIt is made available under a 
perpetuity. 
 is the author/funder, who has granted medRxiv a license to display the preprint in(which was not certified by peer review)preprint 
The copyright holder for thisthis version posted September 17, 2024. ; https://doi.org/10.1101/2024.09.15.24313552doi: medRxiv preprint 

 14 
Figures and Tables 382 
 383 
Figure 1. Detection of the AQP2/3(814) chimera by SHERLOCK. (A) Schematic of the AQP2 384 
and AQP3 wild type locus (left) and the AQP2/AQP3(814) chimera (right). The RPA primers 385 
(arrows) and crRNA target (RNA guide) regions for detection of the AQP2/AQP3(814) chimera 386 
are shown. (B) Alignments of the chimera AQP2/AQP3(814) (KF564931.1), WT AQP2 387 
(Tb927.10.14170) and AQP3 (Tb927.10.14160) sequences are shown with the non -388 
homologous regions highlighted in gray. (C) crRNA screening for the detection of the 389 
AQP2/AQP3(814) chimera using RNA from in vitro derived AQP2/AQP3(814), WT T.b.b. (T. b. 390 
brucei), WT T.b.g. (T. b. gambiense), and human embryonic kidney (HEK) cells. RNA input at 391 
1 ng/µL. Asterisk represents p values at (*) p<0.001 and (**) p<0.0001. 392 
 393 
Figure 2. Evaluation of the  AQP2/AQP3(814) SHERLOCK assay on isolates from HAT 394 
patients with relapses associated with the formation of AQP2/3 chimeras. (A) Map showing 395 
the regions where patient with relapse after treatment was detected (B) Schematics of the AQP2 396 
and AQP3 loci in 4 different strains isolated from patients in the DRC (WT, 163AT, MBA and 397 
348BT) and South Sudan (K03048). The RPA primers (arrows) and crRNA target (RNA guide) 398 
regions for detection of the AQP2/AQP3(814) chimera are shown. (C) Alignments of the WT 399 
AQP2 (Tb927.10.14170) and AQP3 (Tb927.10.14160); AQP2/AQP3(814) (KF564931.1); 400 
AQP2/3(880) (KM282050) and AQP2/3(678-880) (KM282034) sequences are shown with the non-401 
homologous regions highlighted in gray. (D) Kinetic representation of the Cas13a reaction 402 
using the APQ2/3(814)-specific SHERLOCK assay testing the different RNAs extracted from 403 
the 6 strains isolated from DRC patients (163AT, 348BT, 40AT, 349AT, MBA and WT) and 404 
one strain form South Sudan (K03048) (left graph). Representation of the fold-change over 405 
background fluorescence after 180 min (time point taken indicated by black arrow in kinetic 406 
plot) of Cas13a reaction using the APQ2/3(814)-specific SHERLOCK assay analysing the RNAs 407 
from the different isolated strains (right graph).   408 
 409 
Figure 3. Optimization of a SHERLOCK assay for the detection of CPSF3 single 410 
nucleotide variant (SNV). (A) Schematic of the crRNAs design for the detection of the single 411 
nucleotide variant (SNV) in the CPSF3 gene. Position of the SNV in red and the inclusion of 412 
the synthetic mismatch along the crRNA spacer in green. (B) Screening of crRNAs designed 413 
for the detection of CPSF3-edited cells. The target sequence of each crRNA is indicated, as 414 
 . CC-BY-NC-ND 4.0 International licenseIt is made available under a 
perpetuity. 
 is the author/funder, who has granted medRxiv a license to display the preprint in(which was not certified by peer review)preprint 
The copyright holder for thisthis version posted September 17, 2024. ; https://doi.org/10.1101/2024.09.15.24313552doi: medRxiv preprint 

 15 
well as the PFS in brackets. crRNAs used for detection of the CPSF3(SNV): 1) SNV fixed at 415 
position 3, and 2) SNV fixed at position 6. SNV is in underlined and bold character, and 416 
synthetic mismatch is in underlined, bold and italicized character. crRNAs with different spacer 417 
lengths were evaluated (20, 23 and 27 nt). The heat map shows the fold change over background 418 
fluorescence intensity values collected at time zero and after 3 h of LwCas13a detection 419 
reaction. G, guanine; A, adenine; U, uridine; C, cytosine; PFS, protospacer flanking site; 420 
TbCPSF3, Trypanosoma brucei gambiense  cleavage and polyadenylation factor 3; WT, wild 421 
type. 422 
 423 
Figure 4.  Evaluation of selected nucleotides used as synthetic mismatches in the 424 
CPSF3(SNV) SHERLOCK assay. Kinetic representation of LwCas13a reaction for the selected 425 
base for the synthetic mismatch at nt 4: uracil (A), guanine (B) or cytosine (C). The fold-change 426 
over background fluorescence was indicated at different time points of the LwCas13a reaction. 427 
Results from WT cells are shown with open circles and those from edited CPSF3(SNV) cells with 428 
red dots. Box-plots represent fold-change over background fluorescence intensity values using 429 
RNA from WT cells (gray box -plots) or RNA from CPSF3(SNV)-edited cells (red box-plots) at 430 
the selected time-point, here indicated by a red arrow in each kinetic plot. RNA input at 5 ng/µL. 431 
The p values are represented by asterisks as follows: p<0.05 (*), p<0.01 (**) and p<0.001 (***). 432 
 433 
Supplementary Figure 1. RPA primer screening. (A) Representation of the results obtained 434 
in the screening of RPA primers (1 and 2) and crRNAs (2 and 3) for the AQP2/3 (814)-specific 435 
SHERLOCK assay using as input the different RNAs from the extraction of strains isolated 436 
from gHAT patients that contains the AQP2/3(814) (163AT and 384BT) or not (MBA and WT). 437 
(B) Evaluation of the pairs of RPA longer length primers (30 nt) and shorter length primers (25 438 
nt) by SHERLOCK assay using four potential crRNAs (1 to 4) specific for the detection of 439 
genetic material of CPSF3(SNV)-edited cells. The data were represented as the fold-change over 440 
background fluorescence, taking the values obtained after 60 min of LwCas13a detection 441 
reaction. 442 
 443 
Supplementary Table 1. RPA primers and crRNA templates used in this study.  444 
 445 
References 446 
 . CC-BY-NC-ND 4.0 International licenseIt is made available under a 
perpetuity. 
 is the author/funder, who has granted medRxiv a license to display the preprint in(which was not certified by peer review)preprint 
The copyright holder for thisthis version posted September 17, 2024. ; https://doi.org/10.1101/2024.09.15.24313552doi: medRxiv preprint 

 16 
 447 
1. WHO. Global report on neglected tropical diseases 2024. 2024. 448 
2. WHO. Guidelines 449 
for the treatment of human African trypanosomiasis. WHO 2024. 450 
3. Dickie EA, Giordani F, Gould MK, et al. New Drugs for Human African 451 
Trypanosomiasis: A Twenty First Century Success Story. Trop Med Infect Dis 2020; 5(1). 452 
4. Checchi F, Chappuis F, Karunakara U, Priotto G, Chandramohan D. Accuracy of five 453 
algorithms to diagnose gambiense human African trypanosomiasis. PLoS Negl Trop Dis 2011; 454 
5(7): e1233. 455 
5. Lindner AK, Lejon V, Chappuis F, et al. New WHO guidelines for treatment of 456 
gambiense human African trypanosomiasis including fexinidazole: substantial changes for 457 
clinical practice. Lancet Infect Dis 2020; 20(2): e38-e46. 458 
6. Deeks ED. Fexinidazole: First Global Approval. Drugs 2019; 79(2): 215-20. 459 
7. Pelfrene E, Harvey Allchurch M, Ntamabyaliro N, et al. The European Medicines 460 
Agency's scientific opinion on oral fexinidazole for human African trypanosomiasis. PLoS Negl 461 
Trop Dis 2019; 13(6): e0007381. 462 
8. Wyllie S, Foth BJ, Kelner A, Sokolova AY, Berriman M, Fairlamb AH. 463 
Nitroheterocyclic drug resistance mechanisms in Trypanosoma brucei. J Antimicrob 464 
Chemother 2016; 71(3): 625-34. 465 
9. Barrett MP, Vincent IM, Burchmore RJ, Kazibwe AJ, Matovu E. Drug resistance in 466 
human African trypanosomiasis. Future Microbiol 2011; 6(9): 1037-47. 467 
10. Baker N, de Koning HP, Maser P, Horn D. Drug resistance in African trypanosomiasis: 468 
the melarsoprol and pentamidine story. Trends Parasitol 2013; 29(3): 110-8. 469 
11. Fairlamb AH, Horn D. Melarsoprol Resistance in African Trypanosomiasis. Trends 470 
Parasitol 2018; 34(6): 481-92. 471 
12. Baker N, Glover L, Munday JC, et al. Aquaglyceroporin 2 controls susceptibility to 472 
melarsoprol and pentamidine in African trypanosomes. Proc Natl Acad Sci U S A  2012; 473 
109(27): 10996-1001. 474 
13. Bassarak B, Uzcategui NL, Schonfeld C, Duszenko M. Functional characterization of 475 
three aquaglyceroporins from Trypanosoma brucei in osmoregulation and glycerol transport. 476 
Cell Physiol Biochem 2011; 27(3-4): 411-20. 477 
14. Graf FE, Ludin P, Wenzler T, et al. Aquaporin 2 mutations in Trypanosoma brucei 478 
gambiense field isolates correlate with decreased susceptibility to pentamidine and melarsoprol. 479 
PLoS Negl Trop Dis 2013; 7(10): e2475. 480 
15. Pyana Pati P, Van Reet N, Mumba Ngoyi D, Ngay Lukusa I, Karhemere Bin Shamamba 481 
S, Buscher P. Melarsoprol sensitivity profile of Trypanosoma brucei gambiense isolates from 482 
cured and relapsed sleeping sickness patients from the Democratic Republic of the Congo. 483 
PLoS Negl Trop Dis 2014; 8(10): e3212. 484 
16. Maina NW, Oberle M, Otieno C, et al. Isolation and propagation of Trypanosoma brucei 485 
gambiense from sleeping sickness patients in south Sudan. Trans R Soc Trop Med Hyg  2007; 486 
101(6): 540-6. 487 
17. Betu Kumeso VK, Kalonji WM, Rembry S, et al. Efficacy and safety of acoziborole in 488 
patients with human African trypanosomiasis caused by Trypanosoma brucei gambiense: a 489 
multicentre, open-label, single-arm, phase 2/3 trial. Lancet Infect Dis 2023; 23(4): 463-70. 490 
18. Tarral A, Hovsepian L, Duvauchelle T, et al. Determination of the Optimal Single Dose 491 
Treatment for Acoziborole, a Novel Drug for the Treatment of Human African 492 
Trypanosomiasis: First-in-Human Study. Clin Pharmacokinet 2023; 62(3): 481-91. 493 
19. Wall RJ, Rico E, Lukac I, et al. Clinical and veterinary trypanocidal benzoxaboroles 494 
target CPSF3. Proc Natl Acad Sci U S A 2018; 115(38): 9616-21. 495 
 . CC-BY-NC-ND 4.0 International licenseIt is made available under a 
perpetuity. 
 is the author/funder, who has granted medRxiv a license to display the preprint in(which was not certified by peer review)preprint 
The copyright holder for thisthis version posted September 17, 2024. ; https://doi.org/10.1101/2024.09.15.24313552doi: medRxiv preprint 

 17 
20. Sharma A, Cipriano M, Ferrins L, Hajduk SL, Mensa-Wilmot K. Hypothesis-generating 496 
proteome perturbation to identify NEU -4438 and acoziborole modes of action in the African 497 
Trypanosome. iScience 2022; 25(11): 105302. 498 
21. Kovarova J, Novotna M, Faria J, et al. CRISPR/Cas9-based precision tagging of 499 
essential genes in bloodstream form African trypanosomes. Mol Biochem Parasitol 2022; 249: 500 
111476. 501 
22. Sima ND -H, A.; Perlaza, BL.; Ungeheuer, MN.;  Rotureau, B.; Glover, L. 502 
SHERLOCK4HAT: a CRISPR -based tool kit for diagnosis of Human African 503 
Trypanosomiasis. medRxiv 2022. 504 
23. Cunningham CH, Hennelly CM, Lin JT, et al. A novel CRISPR -based malaria 505 
diagnostic capable of Plasmodium detection, species differentiation, and drug -resistance 506 
genotyping. EBioMedicine 2021; 68: 103415. 507 
24. Gootenberg JS, Abudayyeh OO, Kellner MJ, Joung J, Collins JJ, Zhang F. Multiplexed 508 
and portable nucleic acid detection platform with Cas13, Cas12a, and Csm6. Science 2018; 509 
360(6387): 439-44. 510 
25. Gootenberg JS, Abudayyeh OO, Lee JW, et al. Nucleic acid detection with CRISPR -511 
Cas13a/C2c2. Science 2017; 356(6336): 438-42. 512 
26. Myhrvold C, Freije CA, Gootenberg JS, et al. Field -deployable viral diagnostics using 513 
CRISPR-Cas13. Science 2018; 360(6387): 444-8. 514 
27. Kellner MJ, Koob JG, Gootenberg JS, Abudayyeh OO, Zhang F. SHERLOCK: nucleic 515 
acid detection with CRISPR nucleases. Nat Protoc 2019; 14(10): 2986-3012. 516 
28. Ye J, Coulouris G, Zaretskaya I, Cutcutache I, Rozen S, Madden TL. Primer -BLAST: 517 
a tool to design target -specific primers for polymerase chain reaction. BMC Bioinformatics  518 
2012; 13: 134. 519 
29. Piepenburg O, Williams CH, Stemple DL, Armes NA. DNA detection using 520 
recombination proteins. PLoS Biol 2006; 4(7): e204. 521 
30. Benjamini YaH, Y. Controlling the False Discovery Rate: a Practical and Powerful 522 
Approach to Multiple Testing. The Journal of the Royal Statistical Society, Series B (Statistical 523 
Methodology) 1995; 57(1): 289-300. 524 
31. Sievers F, Higgins DG. Clustal Omega for making accurate alignments of many protein 525 
sequences. Protein Sci 2018; 27(1): 135-45. 526 
32. Graf FE, Baker N, Munday JC, de Koning HP, Horn D, Maser P. Chimerization at the 527 
AQP2-AQP3 locus is the genetic basis of melarsoprol-pentamidine cross-resistance in clinical 528 
Trypanosoma brucei gambiense isolates. Int J Parasitol Drugs Drug Resist 2015; 5(2): 65-8. 529 
33. Altmann S, Rico E, Carvalho S, et al. Oligo targeting for profiling drug resistance 530 
mutations in the parasitic trypanosomatids. Nucleic Acids Res 2022; 50(14): e79. 531 
34. Molina Vargas AM, Sinha S, Osborn R, et al. New design strategies for ultra -specific 532 
CRISPR-Cas13a-based RNA detection with single -nucleotide mismatch sensitivity. Nucleic 533 
Acids Res 2024; 52(2): 921-39. 534 
35. Abudayyeh OO, Gootenberg JS, Essletzbichler P, et al. RNA targeting with CRISPR -535 
Cas13. Nature 2017; 550(7675): 280-4. 536 
36. Franco JR, Priotto G, Paone M, et al. The elimination of human African 537 
trypanosomiasis: Monitoring progress towards the 2021 -2030 WHO road map targets. PLoS 538 
Negl Trop Dis 2024; 18(4): e0012111. 539 
37. Mantena S, Pillai PP, Petros BA, et al. Model-directed generation of CRISPR -Cas13a 540 
guide RNAs designs artificial sequences that improve nucleic acid detection. bioRxiv 2023. 541 
 542 
 543 
 . CC-BY-NC-ND 4.0 International licenseIt is made available under a 
perpetuity. 
 is the author/funder, who has granted medRxiv a license to display the preprint in(which was not certified by peer review)preprint 
The copyright holder for thisthis version posted September 17, 2024. ; https://doi.org/10.1101/2024.09.15.24313552doi: medRxiv preprint 

Figure 1
A
B
C
AQP2/AQP3(814)
Tbb WT
Tbg WT
HEK
5
10
15
1
Fold change over
background fluorescence
✱✱
✱✱
✱✱
AQP2/AQP3(814)
Tbb WT
Tbg WT
HEK
5
10
15
1
Fold change over
background fluorescence
✱
✱
✱
AQP2/AQP3(814)
Tbb WT
Tbg WT
HEK
5
10
15
1
Fold change over
background fluorescence
✱
✱
✱
crRNA 1 crRNA 2 crRNA 3
Sequence            Forward RPA Primer                      crRNA target region                               Reverse RPA Primer 
 
AQP2/AQP3(814) GTACGAAACGGTAGCTATTGGTGC[…]ATGGTCAACAACTTCGGCTTAGCGTCTC[…]CTCTTCTTTTCTTTATGGTGGGGAGGTGT 841  
WT.AQP2      GTACGAAACGGTAGCTATTGGTGC[…]ATGGTCAACAACTTCGGCTTAGCGTCTC[…]CGGTGCGATCCTTCTCGGGGGGGAAGTTC 841  
WT.AQP3      ACACGAGCCGTTGGCAGTTGGTGC[…]ATTGGCAATAACATCGGTTACTCAACGG[…]CTCTTCTTTTCTTTATGGTGGGAAGGTGT 817  
              
N: non-homologous region 
Sequence         Forward RPA Primer                crRNA target region                        Reverse RPA Primer
N: non-homologous region
 . CC-BY-NC-ND 4.0 International licenseIt is made available under a 
perpetuity. 
 is the author/funder, who has granted medRxiv a license to display the preprint in(which was not certified by peer review)preprint 
The copyright holder for thisthis version posted September 17, 2024. ; https://doi.org/10.1101/2024.09.15.24313552doi: medRxiv preprint 

Figure 2
A
C
D
Sequence           Forward RPA Primer              crRNA target region                          Reverse RPA Primer
N: non-homologous region
WT
163AT; K03048;
40AT; 349AT
348BT
MBA
South 
Sudan
Democratic 
Republic of 
Congo
Mundri 
County
Mbuji-Mayi 
region
0 10 20 30 40 60 90 120 150 180
0
5
10
15
20
Time (minutes)
Fold change over 
background fluorescence
163AT
348BT
MBA
40AT
369AT
KO3048
WT
B
163AT348BT40AT349ATK03048MBAWT
0
5
10
15
20
Fold change over 
background fluorescence
***
****
*
**
 . CC-BY-NC-ND 4.0 International licenseIt is made available under a 
perpetuity. 
 is the author/funder, who has granted medRxiv a license to display the preprint in(which was not certified by peer review)preprint 
The copyright holder for thisthis version posted September 17, 2024. ; https://doi.org/10.1101/2024.09.15.24313552doi: medRxiv preprint 

Figure 3 
SNVs in nt 3 à synthetic mismatch in nt 5 or 4
0 180 0 180
GAUAUUCUCAUUGCAGAGAGUACAAAU(G)
AUUCUCAUUGCAGAGAGUACAAAUGGU(A)
GAUAUUCUCAUUGCAGAGAGUACACAU(G)
GAUAUUCUCAUUGCAGAGAGUAGACAU(G)
UUCUCAUUGCAGAGAGUAGACAU(G)
UCAUUGCAGAGAGUAGACAU(G)
UUCUCAUUGCAGAGAGUACUCAU(G)
UCAUUGCAGAGAGUACUCAU(G)
AUUCUCAUUGCAGAGAGUACACAUGGU(A)
AUUCUCAUUGCAGAGAGUACACAAGGU(A)
UCAUUGCAGAGAGUACACAAGGU(A)
UUGCAGAGAGUACACAAGGU(A)
UCAUUGCAGAGAGUACACUUGGU(A)
UUGCAGAGAGUACACUUGGU(A)
5
WT A7.1
Time (min):
Fold Change over background 
fluorescence (a.u.)
10
15
20
Short spacer
0 180 0 180
GAUAUUCUCAUUGCAGAGAGUACAAAU(G)
AUUCUCAUUGCAGAGAGUACAAAUGGU(A)
GAUAUUCUCAUUGCAGAGAGUACACAU(G)
GAUAUUCUCAUUGCAGAGAGUAGACAU(G)
UUCUCAUUGCAGAGAGUAGACAU(G)
UCAUUGCAGAGAGUAGACAU(G)
UUCUCAUUGCAGAGAGUACUCAU(G)
UCAUUGCAGAGAGUACUCAU(G)
AUUCUCAUUGCAGAGAGUACACAUGGU(A)
AUUCUCAUUGCAGAGAGUACACAAGGU(A)
UCAUUGCAGAGAGUACACAAGGU(A)
UUGCAGAGAGUACACAAGGU(A)
UCAUUGCAGAGAGUACACUUGGU(A)
UUGCAGAGAGUACACUUGGU(A)
5
WT A7.1
Time (min):
Fold Change over background 
fluorescence (a.u.)
10
15
20
SNVs in nt 6 à synthetic mismatch in nt 4 or 5
Short spacer
crRNAs for detection of CPFS3(SNV)
0 180 0 180
GAUAUUCUCAUUGCAGAGAGUACAAAU(G)
AUUCUCAUUGCAGAGAGUACAAAUGGU(A)
GAUAUUCUCAUUGCAGAGAGUACACAU(G)
GAUAUUCUCAUUGCAGAGAGUAGACAU(G)
UUCUCAUUGCAGAGAGUAGACAU(G)
UCAUUGCAGAGAGUAGACAU(G)
UUCUCAUUGCAGAGAGUACUCAU(G)
UCAUUGCAGAGAGUACUCAU(G)
AUUCUCAUUGCAGAGAGUACACAUGGU(A)
AUUCUCAUUGCAGAGAGUACACAAGGU(A)
UCAUUGCAGAGAGUACACAAGGU(A)
UUGCAGAGAGUACACAAGGU(A)
UCAUUGCAGAGAGUACACUUGGU(A)
UUGCAGAGAGUACACUUGGU(A)
5
WT A7.1
Time (min):
Fold Change over 
background 
fluorescence (a.u.)
10
15
20
WT edit WT edit WT edit
0
5
10
15
20
25
30
Fold-chage over 
background fluorescence
****
****
A C G
A
B
-3’	5’- AG U U U A G A C U A
C
C
C
C
G
G
G
G
A
A
A
A A
A
C
G
A
A C U A A A A C
Direct	repeat	(DR)	for	LwCas13a
A C U GC U U G U A C UCU C U G C AA
Spacer ,	complementary	to	target
(variable	sequence)
1 20
A A UU G G A
236 (nt)
U GG U AA A C A U G A G A G A C G U U A C U C U U AA3’- -5’
OFF - Target	sequence
WT	(TbCPSF3)PFS
U GG U CA A C A U G A G A G A C G U U A C U C U U AA
PFS
3’- -5’
ON - Target	sequence
Acoziborole drug-resistant
(A-C	editing of TbCPSF3)
SNV at nt 6 à synthetic mismatch at nt 4
4
SNV
mismatch
Example:
crRNA guide
RNA target
sequences
 . CC-BY-NC-ND 4.0 International licenseIt is made available under a 
perpetuity. 
 is the author/funder, who has granted medRxiv a license to display the preprint in(which was not certified by peer review)preprint 
The copyright holder for thisthis version posted September 17, 2024. ; https://doi.org/10.1101/2024.09.15.24313552doi: medRxiv preprint 

Figure 4
C
A
B
0 10203040 60 90 120 150 180
0
5
10
15
20
25
Time (minutes)
Fold-chage over 
background fluorescence
CPSF3mut
WT
*
**
**
**
** ** ** **
0 10203040 60 90 120 150 180
0
5
10
15
20
25
Time (minutes)
Fold-chage over 
background fluorescence
CPSF3mut
WT
**
**
*** *** *** ***
10203040 60 90 120 150 1800
0
5
10
15
20
25
Time (minutes)
Fold-chage over 
background fluorescence
CPSF3mut
WT
WT CPSF3mut
0
5
10
15
20
25
30
Fold-chage over
background fluorescence ✱✱
WT CPSF3mut
0
5
10
15
20
25
30
Fold-chage over
background fluorescence
✱✱✱
WT CPFS3 (SNV)
WT CPFS3 (SNV)
CPFS3(SNV)
CPFS3(SNV)
CPFS3(SNV)
WT CPSF3mut
0
5
10
15
20
25
30
Fold-chage over
background fluorescence
WT CPFS3 (SNV)
 . CC-BY-NC-ND 4.0 International licenseIt is made available under a 
perpetuity. 
 is the author/funder, who has granted medRxiv a license to display the preprint in(which was not certified by peer review)preprint 
The copyright holder for thisthis version posted September 17, 2024. ; https://doi.org/10.1101/2024.09.15.24313552doi: medRxiv preprint 