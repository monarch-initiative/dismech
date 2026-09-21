---
reference_id: DOI:10.1101/2020.07.13.196709
title: DHX30 coordinates cytoplasmic translation and mitochondrial function contributing to cancer cell survival
authors:
- Bartolomeo Bosco
- Annalisa Rossi
- Dario Rizzotto
- Sebastiano Giorgetta
- Alicia Perzolli
- Francesco Bonollo
- Angeline Gaucherot
- Frédéric Catez
- Jean-Jacques Diaz
- Erik Dassi
- Alberto Inga
year: '2020'
doi: 10.1101/2020.07.13.196709
content_type: full_text_pdf
is_preprint: true
peer_review_status: preprint
full_text_attempted: true
full_text_provider: epmc_preprint
full_text_url: "https://www.biorxiv.org/content/biorxiv/early/2020/12/10/2020.07.13.196709.full.pdf"
oa_status: green
local_pdf_path: files/DOI_10.1101_2020.07.13.196709.pdf
---

# DHX30 coordinates cytoplasmic translation and mitochondrial function contributing to cancer cell survival
**Authors:** Bartolomeo Bosco, Annalisa Rossi, Dario Rizzotto, Sebastiano Giorgetta, Alicia Perzolli, Francesco Bonollo, Angeline Gaucherot, Frédéric Catez, Jean-Jacques Diaz, Erik Dassi, Alberto Inga
**DOI:** [10.1101/2020.07.13.196709](https://doi.org/10.1101/2020.07.13.196709)

## Content

Abstract
DHX30 was recently implicated in the translation control of mRNAs involved in p53-dependent apoptosis. Here we show that DHX30 exhibits a more general function by integrating the activities of its cytoplasmic isoform and of the more abundant mitochondrial one. The depletion of both DHX30 isoforms in HCT116 cells leads to constitutive changes in polysome-associated mRNAs, enhancing the translation of mRNAs coding for cytoplasmic ribosomal proteins while reducing the translational efficiency of the nuclear-encoded mitoribosome mRNAs. Furthermore, depletion of both DHX30 isoforms exhibits higher global translation but slower proliferation, and reduced mitochondrial energy metabolism. Isoform-specific silencing established a role for cytoplasmic DHX30 in modulating global translation. The impact on global translation and proliferation were confirmed in U2OS and MCF7 cells, although the effect of DHX30 depletion on mitochondrial gene expression was observed only in MCF7 cells. Exploiting RIP, eCLIP, and gene expression data, we identified a gene signature comprising DHX30 and fourteen mitoribosome transcripts that we candidate as direct targets: this signature shows prognostic value in several TCGA cancer types, with higher expression associated with reduced overall survival. We propose that DHX30 contributes to cell homeostasis by coordinating ribosome biogenesis, global translation, and mitochondrial metabolism. Targeting DHX30 could, thus, expose a vulnerability in cancer cells.

Author summary
Translation occurs in the cell both through cytoplasmic and mitochondrial ribosomes, respectively translating mRNAs encoded by the nuclear and the mitochondrial genome. Here we found that DHX30, an RNA-binding protein implicated in p53-dependent apoptosis, enhances the translation of mRNAs coding for cytoplasmic ribosomal proteins while reducing that of the mitoribosome mRNAs when silenced. This coordination of the cytoplasmic and mitochondrial translation machineries affected both cell proliferation and energy metabolism, suggesting an important role for this mechanism in determining the fitness of cancer cells. Indeed, the analysis of publicly available cancer datasets led us to define a 15-genes signature that is able to affect the prognosis of a subset of cancer types. In this subset, we found that higher expression of the genes composing the signature is associated with a worse prognosis. We thus propose DHX30 as a potential vulnerability in cancer cells, that could be targeted to develop novel therapeutic strategies.

 1 
 1 
 2 
 3 
DHX30 coordinates cytoplasmic translation and mitochondrial function 4 
contributing to cancer cell survival   5 
 6 
 7 
 8 
 9 
Bartolomeo Bosco1, Annalisa Rossi1, Dario Rizzotto1^, Sebastiano 10 
Giorgetta1, Alicia Perzolli1, Francesco Bonollo1, Angeline Gaucherot2, 11 
Frédéric Catez2, Jean-Jacques Diaz2, Erik Dassi1#, Alberto Inga1# 12 
 13 
 14 
 15 
 16 
1Department of Cellular, Computational and Integrative Biology, CIBIO, University of Trento, 17 
via Sommarive 9, 38123, Trento, Italy 18 
2Inserm U1052, CNRS UMR5286 Centre de Recherche en Cancérologie de Lyon, F-69000 19 
Lyon, France. Centre Léon Bérard, F-69008 Lyon, France, Université de Lyon 1, F-69000 Lyon, 20 
France 21 
 22 
 23 
^present address: CeMM Research Center for Molecular Medicine of the Austrian Academy of 24 
Sciences, Vienna, Austria 25 
 26 
#corresponding authors: 27 
erik.dassi@unitn.it 28 
alberto.inga@unitn.it 29 
 30 
 31 
 32 
Running title: DHX30 controls global translation  33 
 34 
 35 
 36 
Keywords: DHX30, translation efficiency, polysomal profiling, mitoribosome, ribosome 37 
biogenesis, RNA binding proteins 38 
  39 
preprint (which was not certified by peer review) is the author/funder. All rights reserved. No reuse allowed without permission. 
The copyright holder for thisthis version posted December 10, 2020. ; https://doi.org/10.1101/2020.07.13.196709doi: bioRxiv preprint 

 2 
Abstract  40 
DHX30 was recently implicated in the translation control of mRNAs involved in p53-dependent apoptosis. 41 
Here we show that DHX30 exhibits a more general function by integrating the activities of its cytoplasmic 42 
isoform and of the more abundant mitochondrial one. The depletion of both DHX30 isoforms in HCT116 43 
cells leads to constitutive changes in polysome -associated mRNAs, enhancing the translation of mRNAs 44 
coding for cytoplasmic ribosomal proteins while reducing the translational efficiency of  the nuclear-45 
encoded mitoribosome mRNAs. Furthermore, depletion of both  DHX30 isoforms exhibits higher global 46 
translation but slower proliferation, and reduced mitochondrial energy metabolism. Isoform -specific 47 
silencing established a role for cytoplasmic DHX30 in modulating global translation. The impact on global 48 
translation and proliferation were confirmed in U2OS and MCF7 cells, although the effect of DHX30 49 
depletion on mitochondrial gene expression was observed only in MCF7 cells. Exploiting RIP, eCLIP, and 50 
gene expression data, w e identified a gene signature comprising DH X30 and fourteen mitoribosome 51 
transcripts that we candidate as direct targets: this signature shows prognostic value in several TCGA cancer 52 
types, with higher expression associated with reduced overall survival. We propose that DHX30 contributes 53 
to cell homeostasis by coordinating ribosome biogenesis, global translation, and mitochondrial metabolism. 54 
Targeting DHX30 could, thus, expose a vulnerability in cancer cells. 55 
 56 
Author summary57 
Translation occurs in the cell both through cytoplasmic and mitochondrial ribosomes, respectively 58 
translating mRNAs encoded by the nuclear and the mitochondrial genome . Here we found that 59 
DHX30, an RNA-binding protein implicated in p53-dependent apoptosis, enhances the translation 60 
of mRNAs coding for cytoplasmic ribosomal proteins while reducing that of the mitoribosome 61 
mRNAs when silenced . This coordination of the cytoplasmic and mitochondrial translation 62 
machineries affected both cell proliferation and energy metabolism, suggesting an important role 63 
for this mechanism in  determining the fitness of  cancer cells. Indeed,  the analysis of publicly 64 
available cancer datasets led us to define a 15 -genes signature that is able to affect the prognosis 65 
of a subset of cancer types. In this subset, we found that higher expression of the genes composing 66 
preprint (which was not certified by peer review) is the author/funder. All rights reserved. No reuse allowed without permission. 
The copyright holder for thisthis version posted December 10, 2020. ; https://doi.org/10.1101/2020.07.13.196709doi: bioRxiv preprint 

 3 
the signature is associated with a worse prognosis. We thus propose DHX30 as a potential 67 
vulnerability in cancer cells, that could be targeted to develop novel therapeutic strategies. 68 
 69 
 70 
Introduction71 
The DHX30 RNA binding protein (RBP) is an ATP-dependent RNA helicase highly expressed in neural 72 
cells and somites during embryogenesis in mice. It plays an important role in development and its 73 
homozygous deletion is lethal for embryos [1]. In humans, DHX30 is involved in the antiviral function of 74 
the zinc-finger ZAP protein. Indeed, it was demonstrated that these two proteins directly interact with each 75 
other via the N-terminal domain and that DHX30 is necessary for the optimal antiviral activity of ZAP [2]. 76 
Recently, six de novo missense mutations were identified in DHX30 in twelve unrelated patients affected 77 
by global developmental delay (GDD), intellectual disability (ID), severe speech impairment and gait 78 
abnormalities [3]. All mutations caused amino acid changes in the highly conserved hel icase motif, 79 
impairing the protein’s ATPase activity or RNA recognition. Moreover, overexpression of those DHX30 80 
mutants led to increased propensity to trigger stress granules (SG) formation and decreased global 81 
translation [3]. It was shown that DHX30 could play an important role also in human fibroblast and 82 
osteosarcoma mitochondria. Indeed, in that compartment it interacts with a Fas-activated serine-threonine 83 
kinase (FASTKD2), modulating mitochondrial ribosome maturation and assembly [4].84 
Our group and collaborators recently compared p53-mediated responses to Nutlin-3 treatment in three 85 
different cancer cell lines: HCT116, SJSA1 and MCF7 [5,6]. It was observed that p53 activation caused 86 
cell cycle arrest in HCT116, massive apoptosis in SJSA1 and an intermediate phenotype in MCF7, 87 
consistent with earlier reports [7]. By analyzing the cell lines’ translatomes (i.e. transcripts loaded on 88 
polysomes and in active translation), we discovered that only 0.2% of the genes were commonly 89 
differentially expressed  (DEGs). Furthermore, the polysome profiling of SJSA1 revealed  an enrichment 90 
of pro-apoptotic transcripts [6] in the fraction corresponding to polysomes. Those featured instances of a 91 
specific cis-element in their 3’UTR, labeled as CGPD, standing for CG-rich motif for p53-dependent death. 92 
The DExH box RNA helicase DHX30 was found to be one RBP whose binding to the CGPD motif 93 
correlated with a specific cell fate. Indeed, DHX30 was expressed at higher levels in HCT116 than SJSA1, 94 
preprint (which was not certified by peer review) is the author/funder. All rights reserved. No reuse allowed without permission. 
The copyright holder for thisthis version posted December 10, 2020. ; https://doi.org/10.1101/2020.07.13.196709doi: bioRxiv preprint 

 4 
resulting in a lower translation  of GCPD -motif-containing transcripts in HCT116 cells. D epletion of 95 
DHX30 in HCT116 by stable shRNA increased the translation potential of mRNAs containing the CGPD 96 
motif, resulting in higher levels of apoptosis after p53 activation by Nutlin treatment, mimicking in part the 97 
apoptotic phenotype of SJSA1 [6].  98 
In this work, we set to determine the broader phenotypic role of DHX30 in the colorectal cancer cell line 99 
HCT116. By virtue of two alternative promoters leading to the production isoforms containing or not a 100 
mitochondrial localization signal , DHX30 can couple mitochondrial function, ribosome biogenesis and 101 
global translation. Depleting DHX30 in HCT116 cells reduced cell proliferation and sensitised cells to 102 
small molecules targeting mitochondrial function.  Results were extended to two differe nt cancer cell 103 
models and their implications explored using TGCA data. 104 
 105 
Results 106 
DHX30 depletion enhances translation in HCT116 cells 107 
We previously identified DHX30 as a negative modulator of p53 -dependent apoptosis, performing 108 
polysomal profiling followed by RNA-seq of HCT116 cells clones stably depleted for DHX30 and treated 109 
with the MDM2 inhibitor Nutlin-3 [7]. Here we reanalyzed this dataset (GSE95024), complementing it by 110 
performing a total-cytoplasmic RNA profiling of the same cells by RNA -seq (GSE154065), and focusing 111 
on the comparison between DHX30-depleted (shDHX30) and control (shNT) HCT116 cells in the untreated 112 
control.  113 
We compared the gene expression changes at the polysomal or total cytoplasmic RNA levels and 114 
performed a gene set enrichment analysis [8]. This revealed an increased abundance of ribosomal proteins 115 
and ribosome biogenesis genes in shDHX30 cells , only at the polysomal level ( Figure 1A, Table S1). 116 
Consistently, analysis of translation efficiency (TE), measured as the ratio between relative RNA abundance 117 
in polysomal and total cytoplasmic fractions, revealed that DHX30 depletion is associated with higher TE 118 
for transcripts coding for ribosomal protein subunits (RPL, RPS, Figure 1B). On the other end , nuclear 119 
transcripts coding mitochondrial ribosomal proteins exhibited reduced TE in DHX30-depleted cells, despite 120 
showing higher constitutive TE compared to the cytoplasmic ribosomal transcripts (mRPL, mRPS, Figure 121 
1B). Validation by qPCR was performed for four RPs and four MRPs transcripts (Figure S1A). The basal 122 
preprint (which was not certified by peer review) is the author/funder. All rights reserved. No reuse allowed without permission. 
The copyright holder for thisthis version posted December 10, 2020. ; https://doi.org/10.1101/2020.07.13.196709doi: bioRxiv preprint 

 5 
differences in TE between ribosome and mitoribosome transcripts was confirmed in all cases, and for five 123 
of them results reproduced the effect of DHX30 depletion on TE that was observed from the RNA-seq data. 124 
A trend for higher expression of RPL and RPS  transcripts and lower expression of MRPL and MRPS 125 
transcripts in DHX30-depleted cells was also apparent (Figure S1B).  126 
We thus sought to understand if DHX30 could be directly regulating this class of genes and exploited the  127 
data of DHX30 eCLIP  assay performed in K562 cells  as part of the ENCODE project [9]. Despite the 128 
different cell line, the eCLIP data indicate that DHX30 can bind 67 ribosomal (36 RPLs and 31 RPSs) and 129 
23 mitoribosomal (16 MRPLs and 7 MRPSs) protein transcripts (Table S1) [9].  130 
 Consistent with the higher TE for RPL and RPS transcripts, DHX30 depletion in HCT116 cells 131 
was associated with higher relative amounts of ribosomes extracted and quantified from a sucrose cushion 132 
(Figure 1C), and higher rRNA levels (Figure 1D, E). Furthermore, DHX30-depleted cells not only showed 133 
evidence of increased ribosome biogenesis, but also of higher global translation ( Figure 1F, 1G). The 134 
higher global translation does not appear to be related to an increase in MYC expression or activity (Figure 135 
S1C), nor to a significant increase in the activity mTOR pathway ( Figure S1D). Finally, DHX30 protein 136 
was found to be associated with ribosomal subunits, 80S monosomes as well as with low molecular-weight 137 
polysomes in HCT116, MCF7 and U2OS cells (Figure S1F). 138 
Hence, DHX30 appears to negatively influence ribosome biogenesis, global translation and also 139 
the translation of s pecific mRNAs. It is important to emphasize that these are not necessarily dissociated 140 
events, as a change in ribosome number could be sufficient to impact on translation specificity [10]. 141 
 142 
DHX30 depletion alters the expression of mitoribosomal transcripts 143 
The impact of DHX30 depletion on the expression and translation efficiency of nuclear -encoded 144 
mitoribosomal proteins caught our attention, as it showed the opposite trend compared to ribosomal protein 145 
transcripts (Figure 1B, Figure S1). First, we established the potential for DHX30 to bind to mitoribosomal 146 
protein transcripts by RIP assays, choosing MRPL11 (UL11m), that was previously evaluated in cancer 147 
cells [3], and MRPS22 (mS22), as a representative of the large and small subunits, respectively ( Figure 148 
2A). Next, we observed that DHX30-depleted cells showed reduced expression of these two genes at both 149 
the RNA and protein levels (Figure 2B, C). These findings suggest that DHX30 directly promotes stability 150 
preprint (which was not certified by peer review) is the author/funder. All rights reserved. No reuse allowed without permission. 
The copyright holder for thisthis version posted December 10, 2020. ; https://doi.org/10.1101/2020.07.13.196709doi: bioRxiv preprint 

 6 
and/or translation of mitoribosome transcripts. The modulation of mitoribosome proteins expression might 151 
impact on mitochondrial translation and contribute to the functions described for DHX30 in the 152 
mitochondrial matrix [4,11]. Notably, the DHX30 gene contains two promoters, and the transcript resulting 153 
from the internal , more 3’- one (ENST00000457607.1) includes an alternative first exon that contains a 154 
predicted mitochondri al targeting sequence [12,13]. Mitochondrial localization of the protein was 155 
confirmed by immunofluorescence (Figure 2D), consistent with previous results in human fibroblasts [4] 156 
and APEX-seq data [14]. We checked the relative levels of the DHX30 transcripts from the two promoters 157 
and found the putative mitochondrial isoform to be about four times mor e abundant ( Figure 2E ), as 158 
indicated also by western blot analysis on extracts of mitochondrial and cytoplasmic fractions (Figure 2F).  159 
Stable DHX30 -silencing was obtained using three different shRNAs [6] that targeted both 160 
cytoplasmic and mitochondrial transcripts (from here on labeled cDHX30  and mDHX30) (Figure S2A), 161 
and isolating single clones . To confirm results , we also employed transient silencing using one siRNA 162 
specific for cDHX30 (labeled siDHX30-C) or an siRNA targeting transcripts from both promoters (labeled 163 
siDHX30-C+M). The activity and specificity of the two siRNAs was assessed by qRT-PCR 48 and 96 hours 164 
post-silencing ( Figure S2B , Figure 3A). Transient silencing of just cDHX30 or bo th cDHX30 and 165 
mDHX30 for 96 hours led to an increase in global translation (Figure 3B) that was not associated with an 166 
increase in the activity mTOR pathway (Figure S1E), thus confirming the observations obtained with the 167 
different stable clones, but indicating that cDHX30 modulates global translation.  168 
Transient silencing of both cDHX30 and mDHX30 resulted in a reduction of the expression of 169 
MRPL11 and MRPS22 (Figure 3C, D) similar  to wh at we previously observed with stable depletion of 170 
both isoforms (Figure 2), while cDHX30 silencing was ineffective, considering the results at both RNA and 171 
protein levels.  172 
DHX30 stable or transient silencing was extended to U2OS, osteosarcoma -derived cells that 173 
express relatively high levels of DHX30  (Figure S2 C, S2D). Stable depletion of both cDHX30 and 174 
mDHX30 was associated with a significant reduction of MRPL11 (RNA and protein)  and of MRPS22 175 
mRNA expression (Figure S2E, S2F), while transient depletion by siRNAs did not significantly impact on 176 
the expression of the two mitoribosome transcripts ( Figure S2G), although MRPL11 protein levels were 177 
reduced by siDHX30-C+M (Figure S2H).  178 
preprint (which was not certified by peer review) is the author/funder. All rights reserved. No reuse allowed without permission. 
The copyright holder for thisthis version posted December 10, 2020. ; https://doi.org/10.1101/2020.07.13.196709doi: bioRxiv preprint 

 7 
Transient silencing of both cDHX30 and mDHX30 was also performed in the breast cancer-derived 179 
MCF7 cells (Figure S3A) and led to a reduction in the expression of both MRPL11 and MRPS22 mRNAs 180 
(Figure S3B), although only for MRPL11 the effect was consistent also at protein level ( Figure S3C). 181 
Cytoplasmic DHX30 transient silencing in U2OS and MCF7 also led to higher global translation , 182 
confirming the results obtained in HCT116 cells (Figure S3D, S3E). 183 
 184 
DHX30 depletion impacts mitochondrial gene expression and function 185 
We next focused on the expression of mitochondrially encoded genes. First of all , we established 186 
that DHX30 depletion did not impact on the number of mitochondrial genomes by digital PCR in HCT116 187 
cells (Figure 4A). Instead, the expression of several mitochondrially encoded transcripts was significanly 188 
reduced (Figure 4B). The steady-state expression of two mitochondrially encoded proteins, MT-ATP6 and 189 
MT-ATP8, was investigated and shown to be reduced in HCT116_shDHX30 cells (Figure 4C, S3F). We 190 
pursued the same analysis after transient silencing, confirming the lower expression of mito chondrially 191 
encoded genes at the RNA and protein levels, but only when the DHX30 mitochondrial variant (siDHX30-192 
C+M) was silenced and analysed 96 hours post silencing ( Figure 4D, 4E). In fact, although DHX30 193 
depletion was visible already after 48 hours (Figure S2B) from the addition of the siRNAs, more time was 194 
needed to appreciate a reduction in the expression of mitochondrially encoded genes. The expression of 195 
mitochondrially encoded genes was checked also after DHX30 silencing in U2OS and MCF7 cells (Figure 196 
S4). In U2OS _shDHX30 cells, all of the tested transcripts , with the exception of MT -ND6, were down-197 
modulated compared to the U2OS_shNT control (Figure S4A, left panel). Instead, none of the seven tested 198 
transcripts were down -modulated by transient DHX30 silencing, regardless of the siRNA used  (Figure 199 
S4A, right panel). In fact, three of them were slightly upregulated.  This latter result is consistent with the 200 
observation of a slightly lower efficacy of DHX30 depletion by siRNAs and with the lack of an impact on 201 
MRPL11 or MRPS22 expression (Figure S2). MT-ATP6 was also examined by western blot and its amount 202 
was reduced in U2OS_shDHX30 cells (Figure S4C), but not in U2OS cells that were transiently silenced 203 
for DHX30  (Figure S4D ). Transient DHX30 depletion (by siDHX30 C+M) in MCF7 cells led to a 204 
significant reduction in the expression of all tested mitochondrial transcripts, although for MT -ATP6 the 205 
reduction was not significant at protein levels (Figure S4B, S4E). 206 
preprint (which was not certified by peer review) is the author/funder. All rights reserved. No reuse allowed without permission. 
The copyright holder for thisthis version posted December 10, 2020. ; https://doi.org/10.1101/2020.07.13.196709doi: bioRxiv preprint 

 8 
Finally, we evaluated markers of carbon metabolism and mitochondrial respiration capacity by an 207 
Agilent SeahorseXF real-time analyzer. HCT116_shDHX30 cells had a significantly lower basal oxygen 208 
consumption rate compared to the control cell line. Notably, DHX30 -depleted cells did not show 209 
compensatory glycolysis in basal culture condition, not even when we chemically abolished mitochondrial 210 
respiration.  We indeed observed a lower compensatory glycolysis compared with the control (Figure 4F). 211 
These results suggest that HCT116_shDHX30 cells do not show a typical Warburg effect  [15], and are 212 
expected to produce less energy due to reduced mitochondrial respiration.      213 
Collectively, the depletion of DHX30 seems to generate an imbalance in cell homeostasis, with higher 214 
demand of chemical energy from ribosome biogenesis and cytoplasmic translation but lower mitochondrial 215 
activity.216 
 217 
DHX30 depletion impaired cell proliferation rate and increased apoptosis proneness.218 
Next, we characterized the phenotypic impact of DHX30 depletion in HCT116. Consistent with the lower 219 
mitochondrial oxygen consumption rate, HCT116_shDHX30 cells showed a significantly lower 220 
proliferation rate compared to the control cell clone. This was observed by colony formation assay and 221 
confirmed through time -course proliferation by cell count via high -content microscopy or using a Real -222 
Time Cell Analyzer xCELLigence (Figure 5A-C). Interestingly, we observed a reduction in proliferation 223 
after DHX30 silencing also in a spheroid assay ( Figure 5D). The lower growth rate in D HX30 depleted 224 
cells cannot be attributed to an arrest in a particular phase of the cell cycle (Figure 5E). Instead, it could be 225 
associated with a moderate increase in the phosphorylation of eIF2alpha (Figure 5F), but not to an obvious 226 
ER-stress response, based on the expression of CHOP, DDIT4, TRIB3 , and on the XBP1 splicing pattern 227 
(Figure S5A). 228 
A reduction in proliferation was confirmed also by cell counting upon transient silencing of cDHX30 and, 229 
particularly, of both cDHX30 and mDHX30 ( Figure 5G). The impact on cell proliferation was also 230 
examined using U2OS cells stably depleted for DHX30 that showed a significant reduction of proliferation 231 
compared to the U2OS_shNT control (Figure S5B). Transient silencing did not impact on the proliferation 232 
of U2OS cells , consistent with the results observed on DHX30 target gene expression,  while it led to a 233 
significant reduction in MCF7 cells (Figure S5B). 234 
preprint (which was not certified by peer review) is the author/funder. All rights reserved. No reuse allowed without permission. 
The copyright holder for thisthis version posted December 10, 2020. ; https://doi.org/10.1101/2020.07.13.196709doi: bioRxiv preprint 

 9 
Furthermore, DHX30 depletion was associated with increased apo ptosis after 48 hours of Nutlin 235 
treatment, as expected by our previous results [6], but also when cells were treated with the topoisomerase 236 
inhibitor doxorubicin and with FCCP, an agent that causes mitochondrial membrane depolarization (Figure 237 
5H). 238 
 239 
DHX30 signature and cancer outcome  240 
Our results suggest that DHX30 exerts a constitutive function that improves cellular fitness by balancing 241 
energy metabolism and global translation potential. Furthermore, our previous study identified DHX30 as 242 
a negative modulator of the translation of specific mRNAs, thus cont rolling p53-dependent apoptosis [6]. 243 
Both these functions suggest that DHX30 could be a modifier of cancer cell properties potentially impacting 244 
on clinical variables.  245 
Although total RNA-seq data are not a good prox y for investigating translation controls  [16], in 246 
this study we showed that DHX30 depletion impacts on steady -state levels of nuclear -encoded 247 
mitoribosomal transcripts. MRPL11 and, particularly, MRPS22 can be considered direct DHX30 targets. 248 
We next cross-referenced our TE and GSEA data with the RIP results and DHX30 eCLIP data in ENCODE 249 
[9] and compiled a list of 14 mitoribosomal protein (MRP) transcripts considered DHX30 direct target 250 
candidates (Figure 6, Figure S6). Interrogating RNA-seq data of TGCA tumors through the GEPIA web 251 
resource [17,18], the expression of DHX30, and of each MRP transcript or of the group of 14 candidate 252 
target MRPs appeared to be positively correlated in several cancer types (Figure 6, Figure S6), including 253 
adrenocortical carcinoma, and hepatocellular carcinomas. No such correlation was instead apparent for 254 
other cancer types, including breast or colon adenocarcinomas. We next used this gene signature to stratify 255 
patients’ clinical outcome. Interestingly, for the cancer types where a positive correlation in the expression 256 
of DHX30 and the 14 MRPs was observed, the combined 15-gene signature (i.e. including DHX30) showed 257 
a prognostic value. In particular, higher expression was associated w ith reduced Overall Survival or 258 
Disease-Free Survival ( Figure 6). Instead, the comparison of DHX30 expression between tumors and 259 
matched controls did not show a consistent trend but confirmed a rather wide variation among samples, and 260 
tissue-specific effects including both cases of over-expression and down-regulation (Figure S7). Finally, a 261 
pan-tissue view revealed a general positive correlation between the expression of ribosome and 262 
preprint (which was not certified by peer review) is the author/funder. All rights reserved. No reuse allowed without permission. 
The copyright holder for thisthis version posted December 10, 2020. ; https://doi.org/10.1101/2020.07.13.196709doi: bioRxiv preprint 

 10 
mitoribosome protein transcripts in normal samples, that is lost in cancer ( Figure S8). These preliminary 263 
analyses suggest that a functional signat ure could be developed to predict aggressiveness in cancer types 264 
where DHX30 appears to stimulate mitoribosomal proteins expression. 265 
 266 
Discussion 267 
Ribosome biogenesis and translation impose a high metabolic demand on the cell  [19,20]. Hence, a 268 
coordination between translational control and metabolic output ultimately involving mitochondrial 269 
respiratory functions is expected to contribute to cell homeostasis and fitness [21,22]. However, relatively 270 
few proteins and pathways have been established to exert a direct role in balancing cytoplasmic translation 271 
initiation with mitochondrial metabolism  [23,24]. eIF6 represents a significant example, as it has been 272 
clearly shown that it negatively controls 80S monosome assembly, a necessary step for translation initiation, 273 
while at the same time playing a critical positive role in mitochondrial functions, as revealed by broad 274 
changes in the mitochondrial proteome in eIF6 hemizygous mice [25–27]. 275 
We propose that DHX30 can also exert an important housekeeping role in coordinating ribosome 276 
biogenesis, translation, and mitochondrial respiration. DHX30 depletion in HCT116, stable or transient, 277 
leads to a modest but significant increase in ribosome biogenesis as well as in global translation; on the 278 
contrary, mito -ribosome transcripts, particularly of the large subunits, exhibit reduced translation 279 
efficiency. Furthermore, DHX30 can also exert a more dire ct role on mitochondria, as the protein can 280 
directly localize to the organelle, thanks to an alternative first exon that features a localization signal. The 281 
steady state expression of several mitochondrially encoded genes was reduced following the d epletion of 282 
both DHX30 transcripts and perhaps more effectively, by the reduction of the mitochondrial isoform.  A 283 
previous study provided clear evidence that DHX30 together with DDX28, FASTKD2, and FASTKD5 can 284 
promote the assembly of 55S mito -monosome and transl ation [4]. Consistent with the r elevance of a 285 
mitochondrial and translation function, the DHX30 transcript has been shown to be located and locally 286 
translated at the ER -Outer Mitochondrial membrane interface, by APEX -seq [14]. In fact, none of the 287 
DHX30 closer homologs showed strong evidence of such localized translation, or other evidence of 288 
mitochondrial localization. 289 
preprint (which was not certified by peer review) is the author/funder. All rights reserved. No reuse allowed without permission. 
The copyright holder for thisthis version posted December 10, 2020. ; https://doi.org/10.1101/2020.07.13.196709doi: bioRxiv preprint 

 11 
A previous report also showed evidence for  DHX30 interaction with mitochondrial transcripts in 290 
human fibroblasts by RIP -seq [4]. Our data instead point to a direct interaction with mitoribosome 291 
transcripts and their positive modulation as another means by which DHX30 can indirectly affect 292 
mitochondrial translation. We validated by RIP the binding of DHX30 to MRPL11 and MRPS22. 293 
Leveraging public data from eCLIP experiments in ENCODE and our polysomal profiling, RNA-seq, and 294 
GSEA analysis, we propose that DHX30 could directly interact with fourteen mito -ribosome protein 295 
transcripts. An even larger set of ribosomal protein transcripts are nominated as direct DHX30 targets by 296 
eCLIP [9] and are showing changes in translation efficiency upon DHX30 depletion in HCT116 cells.  297 
We observed that these two groupings of transcripts ma rkedly differed for their basal translation 298 
efficiency, which was low for cytoplasmic ribosomal protein transcripts. Those mRNAs are known to 299 
contain particularly structured 5’-UTR and to be strongly regulated at the level of translation initiation by 300 
mTOR and MYC-regulated pathways [28–30]. The mechanism by which DHX30 can control ribosomal 301 
protein (RP) transcripts remains to be established. In a recent study, we discovered an RNA sequence motif 302 
in 3’UTRs, labeled CGPD, that is targeted by DHX30 and can mediate higher translation levels [6]. While 303 
we cannot exclude that the CGPD motif could be implicated, only a subset of RP transcripts harbors 304 
instances of it. Our de novo search for over-represented motifs did not retrieve another prominent candidate 305 
cis-element. An even lower number of mito -RP transcripts were found to harbor instances of th e CGPD-306 
motif. This was expected, as DHX30 is inferred to have an opposite role on RP and mito -RP transcripts 307 
based on the direction of changes in their TE observed in HCT116  shDHX30 cells. For the mito-RP gene 308 
group, a de novo motif over-representation search did not identify a strongly enriched cis-element.  309 
The magnitude of fold -change and translation efficiency changes for both ribosomal and 310 
mitoribosomal transcripts in response to DHX30 silencing is modest in absolute value. This could be in 311 
part due to a limitation of the experimental approach. As reported in our earlier study, a complete knock -312 
out of DHX30 does not seem to be attainable in HCT116 cells.  Both our siRNA and even more so the 313 
shRNA clones retain partial DHX30 expression. Furthermore, it is important to emphasize that changes in 314 
the expression or even polysomal association of ribosomal protein transcripts do not necessarily predict 315 
translation rate changes. However, several endpoints consistently suggested that HCT116  shDHX30 cells 316 
exhibited higher ribosome number and increased global translation. When treated with an MDM2 inhibitor 317 
preprint (which was not certified by peer review) is the author/funder. All rights reserved. No reuse allowed without permission. 
The copyright holder for thisthis version posted December 10, 2020. ; https://doi.org/10.1101/2020.07.13.196709doi: bioRxiv preprint 

 12 
inducing strong p53-dependent transcriptional response, those cells were also shown to markedly alter their 318 
translatome [6]. Our results pointed to a direct role of DHX30 on translation specificit y. However, we 319 
cannot exclude that the global effect on ribosome biogenesis we propose represents a constitutive, 320 
housekeeping function for  DHX30. This function  would also contribute to the observed changes in 321 
translation specificity, under the notion that a change in global translation potential or in the modulation of 322 
translation initiation is not expected to impact equally every available transcript in a cell [10,22].  323 
Depletion of DHX30 reduced cell proliferation in various assays. This effect was visible also by 324 
transient silencing of just the cytoplasmic transcript, although it was more evident when both cytoplasmic 325 
and  mitochondrial isoforms were targeted. Although we cannot exclude that the lower proliferation results 326 
from a checkpoint activation, as we have seen that in the siRNA experiments the lack of p53 can reduce the 327 
proliferation lag (Figure S9), cells did not show evidence f or overt cell cycle arrest. This is not entirely 328 
unexpected, due to the residual levels of DHX30 expression in the cell models we used, as noted above, 329 
and also for the possible selective pressure for compensatory effects given the central nature of the processes 330 
involved. Transient silencing of DHX30 in HCT116 p53 null cells besides having a reduced impact on 331 
proliferation also did not significantly alter the expression of MRPS22, MRPL11 or of mitochondrial 332 
transcripts. While this may be suggestive of a functional interaction between DHX30 and p53, results may 333 
be affected by the lower efficiency of DHX30 depletion in HCT116 p53-/- cells (Figure S9). 334 
As several other RBPs, m ito-ribosomal proteins have been proposed to have additional, 335 
moonlighting functions unrelated to mito-ribosome biogenesis, in particular in the modulation of apoptosis. 336 
For example, MRPS29, also known as DAP3,  was reported to influence the extrinsic apoptosis pathway   337 
[31,32], while MRPL41 was proposed to modulate p53-dependent intrinsic apoptosis [33]. It is, however, 338 
unlikely that these potential pro -apoptotic functions can contribute to the proliferation defects seen after 339 
DHX30 depletion, given that their expression is not significantly modified. The expression of several mito-340 
ribosome components has been evaluated as potential biomarkers associated with cancer clinical variables 341 
[34].  342 
Hence, we reasoned that changes in DHX30 levels to an extent that would not lead to overt stress 343 
responses could provide opportunities for increased fitness due to the coordination between mitochondrial 344 
function and translation potential, which could be a balancing function between energy supply and demand. 345 
preprint (which was not certified by peer review) is the author/funder. All rights reserved. No reuse allowed without permission. 
The copyright holder for thisthis version posted December 10, 2020. ; https://doi.org/10.1101/2020.07.13.196709doi: bioRxiv preprint 

 13 
If any, the effects would be expected to reflect tissue -specific differences in metabolism. We explored 346 
TGCA data, first evaluating if a positive correlation could be observed in normal tissue and/or pri mary 347 
cancer samples for DHX30 and mito -ribosome gene expression. Cross -referencing eCLIP data, with our 348 
polysomal profiling, RNA-seq, RIP results, and GSEA data we compiled a list of fourteen mitoribosomal 349 
transcripts as candidate direct DHX30 targets. Int erestingly DHX30 and this 14 -gene list showed a 350 
prognostic significance in cancer types where a positive correlation in their expression was observed. 351 
Instead, copy number alterations or mutations in DHX30 were a rare event in cancer (8.6%), were not 352 
associated with specific tissue or cancer types, and, although based on a few cases, seemed to be mutually 353 
exclusive with mitochondrial genome changes (Figure S10).  354 
In conclusion, our study demonstrate s the role of  DHX30 in the coordination between global 355 
cytoplasmic translation and mitochondrial functions . This role  contributes to the oncogenic potential of 356 
cancer cells, and appears to correlate with tumor aggressiveness and clinical outcome. Furthermore, during 357 
stress responses activating p53, DHX30 can reduce the apoptotic commitment of cancer cells by acting on 358 
specific pro-apoptotic transcripts, thus providing a potential actionable target for therapeutic purposes [6].   359 
 360 
Materials and Methods 361 
RNA-seq library preparation and sequencing 362 
shDHX30 and control cells were either kept untreated or treated with 10µM Nutlin, and processed after 363 
12h. Polysomal profiling and RNA extraction of reconstituted total cytoplasmic fractions was performed 364 
as recently described [6]. Sequencing libraries were obtained following the manufacturer instructions of the 365 
TruSeq RNA Library preparation kit v2. We used 1.5 µg of RNA as input, and assessed the input RNA 366 
quality by the Agilent RNA 6000 Nano kit on a Agilent 2100 Bioanalyzer instrument. Four replicates were 367 
generated for each condition. The resulting 16 samples were sequenced on a HiSeq 2500 machine producing 368 
~25M raw reads per each sample. 369 
 370 
RNA-seq data analysis 371 
Reads were first quality filtered and trimmed with trimmomatic (minimum quality 30, minimum length 372 
36nt) [35]. Then, each Gencode v27 (http://www.gencodegenes.org/releases/) transcript was quantified 373 
preprint (which was not certified by peer review) is the author/funder. All rights reserved. No reuse allowed without permission. 
The copyright holder for thisthis version posted December 10, 2020. ; https://doi.org/10.1101/2020.07.13.196709doi: bioRxiv preprint 

 14 
with Salmon [36]. Eventually, edgeR [37] was used to call Differentially Expressed Genes (DEGs) between 374 
conditions at the polysomal and total levels (shDHX30 DMSO vs shNT DMSO), using a 0.05 threshold on 375 
the adjusted p-value. GSEA was performed with the fgsea R package [8], including the Hallmark, Canonical 376 
Pathways, and GO gene sets. We used 1000 permutations to compute the significance p -value and used a 377 
BH adjusted p -value threshold of 0.05. Translational efficiency (TE) was computed on normalized 378 
expression data (counts per million reads, CPM) as the ratio of polysomal CPMs over total CPMs for each 379 
replicate and transcript in the annotation. Differences in TE (between conditions and groups of genes) and 380 
between polysomal and total samples were assessed by the Wilcoxon test. Motifs in ribosomal and 381 
mitoribosomal genes 5’- and 3’-UTRs were obtained with DREME [38] using a 1.0E-04 p-value threshold 382 
and shuffled input sequences as controls. 383 
 384 
Cell lines and culture conditions 385 
HCT116 and U2OS shNT  control or shDHX30 clones were obtained as recently described  [6].  Briefly, 386 
cells were transduced with lentiviral vectors containing a pLK0.1 plasmid expressing shRNA s. DHX30 387 
targeting s equences are: TRCN0000052028 (GCACACAAATGGACCGAAGAA) TRCN0000052031 388 
(CCGATGGCTGACGTATTTCAT), TRCN0000052032 (GAGTTGTTTG  ACGCAGCCAAA). Stable 389 
clones were selected exploiting the puromycin resistance marker. Single clone isolates were obtained and 390 
characterized for DHX30 protein depletion. Consistent results were obtained using the three diff erent 391 
shRNAs  HCT116 p53-/- cells were obtained from the Vogelstein lab (Sur S. et al, 2009). MCF7 cells were 392 
purchased from ICLC (IRCCS San Martino Hospital, Genoa, Italy).  All cell lines were cultured in RPMI 393 
(Gibco, Thermo Fisher Scientific, Waltham, MA , USA) supplemented with 10% Fetal Bovine Serum 394 
(Gibco, Thermo Fisher Scientific), 1X L-Glutamine and Pen/Strep (Gibco, Thermo Fisher Scientific) at 37 395 
°C with 5% CO2 in a humidified atmosphere. U2OS cells were cultured in DMEM pH 7.4 (Gibco, Thermo 396 
Fisher Scientific) supplemented with 10% Fetal Bovine Serum (Gibco, Thermo Fisher Scientific), 1X L -397 
Glutamine and Pen/Strep (Gibco, Thermo Fisher Scientific) at 37 °C with 5% CO2 in a humidified 398 
atmosphere. For routine culture of depleted clones and controls, 0. 2 µg/mL Puromycin was added to the 399 
culture medium to maintain selection of the vectors. Puromycin was removed 24 hours before starting a 400 
specific experiment to avoid confounding effects. MCF-7, U2OS and HCT116 parental and p53-/- cells were 401 
preprint (which was not certified by peer review) is the author/funder. All rights reserved. No reuse allowed without permission. 
The copyright holder for thisthis version posted December 10, 2020. ; https://doi.org/10.1101/2020.07.13.196709doi: bioRxiv preprint 

 15 
silenced for cytoplasmic or cytoplasmic + mitochondrial DHX30 variants using 25nM siRNAs (Trife cta, 402 
IDT, Coralville, IA, USA) (Table S2) transfected with Interferin (Polyplus-transfection, Illkirch, France). 403 
All experiments were performed at least 24 hours post-silencing. 404 
 405 
Western Blot 406 
Cells were cultured in 6-well tissue culture plates. Cells were collected with trypsin-EDTA after 24 hours,  407 
centrifuged and washed with PBS. Samples were then lysed with RIPA buffer and the proteins were 408 
quantified by BCA assay (EUROCLONE, Milan, Italy). 30 µg of extracted proteins were loaded on 12% 409 
or 15% Tris-glycine Gel and then transferred onto a nitrocellulose membrane using  Tris -Glycine buffer. 410 
Blocking was performed overnight with 5% not-fat dry milk, 0.1% TWEEN and PBS 1X. Immunodetection 411 
was obtained using primary and secondary antibodies reported in Table S3. Membranes were analyzed by 412 
ECL and detected with ChemiDocTM XRS+ (Bio -Rad, Hercules, CA, USA) using ImageLab software 413 
(Bio-Rad). 414 
 415 
Polysome profiling 416 
Polyribosome analysis was performed as described in [39–41]. Briefly, HCT116 cells were grown on 15 417 
cm Petri dishes with standard media and serum. When the cells reached 80% of confluence, cycloheximide 418 
(0.01 mg/ml, Sigma Aldrich) was added and kept in incubation for 10 min. Then cells were washed two 419 
times with cold PBS containing cycloheximide (0.01 mg/ml) and lysed with the following lysis buffer: 20 420 
mM Tris-HCl (pH 7.5), 100 mM KCl, 5 mM MgCl2, 0.5% Nonidet P -40, 100 U/ml RNase inhibitors. 421 
Mitochondria and nuclei -free lysates were loaded onto 15 –50% (w/v) density sucrose gradients in salt 422 
solution (100 mM NaCl, 5 mM MgCl2, 20 mM Tris–HCl pH 7.5), and ultracentrifuged at 180 000 × g for 423 
100 min at 4°C. The sedimentation profiles were monitored by absorbance at 254 nm using a Teledyne 424 
ISCO UA-6 fractionator coupled to UV detector, collecting thirteen 1 ml frac tions. RNA from pooled 425 
polysomal fraction was extracted and processed as described in [6]. For Western blot analysis, 100 ul of 426 
100% TCA and 1 ml of ice-cold acetone were added to 1 ml of each fraction. Then samples were put at −80 427 
°C overnight to induce protein precipitation.  Subsequently samples were centrifuged at 16,000 × g for 10 428 
preprint (which was not certified by peer review) is the author/funder. All rights reserved. No reuse allowed without permission. 
The copyright holder for thisthis version posted December 10, 2020. ; https://doi.org/10.1101/2020.07.13.196709doi: bioRxiv preprint 

 16 
min at 4 °C and washed three times with 1 mL of ice -cold acetone. Finally, the pellets were solubilized 429 
directly in Laemmli buffer pH 8. 430 
 431 
Ribosome isolation 432 
Ribosome isolation was performed fo llowing a protocol previously described [42]. Briefly, 8 x 10 6 cells 433 
were seeded in a T150 flask, 48 hours before the procedure. At 80% of confluence, cells were detached and 434 
counted. 1 x 107 cells were pelleted by 500 x g centrifugation for 5 minutes at 4°C and washed once with 435 
cold PBS. Supernatant was discarded and the pellet was resuspended gently with 300µL of cold buffer A 436 
(sucrose 250mM, KCl 250mM, MgCl2 5mM, and Tris-Cl 50 mM pH 7.4), added in three sequential steps, 437 
pipetting after every addition. To perform cell lysis, an appropriate volume of NP -40 was added to the 438 
homogenized cellular solution, in order to obtain a 0.7% (v/v) final concentration of the detergent, and cells 439 
were incubated on ice for 15 minutes, homogenizing the suspension by gentle pipetting every 5 minutes. 440 
Then the cell lysate was centrifuged at 750 x g for 10 minutes at 4°C to pellet nuclei; the recovered 441 
cytoplasmic fraction (supernatant) was centrifuged again at 12.500 x g  for 10 minutes at 4°C to obtain a 442 
mitochondria pellet. Supernatant containing ribosomes was collected and its volume was accurately 443 
measured using a graduated pipet. KCl 4M solution was then slowly added in order to reach a final 444 
concentration of 0.5M. Meanwhile, 1mL of the sucrose cushion solution (sucrose 1M, KCl 0.5M, MgCl2 445 
5mM and Tris-Cl 50mM pH 7.4) was added into 3-mL polycarbonate tube for an ultracentrifuge TL100.3 446 
rotor (Beckman Coulter, Brea, CA, USA). The KCl -adjusted ribosome-containing solution was carefully 447 
added above the sucrose cushion and tubes were balanced by weight using buffer B (sucrose 250mM, KCl 448 
0.5M, MgCl2 5mM and Tris-Cl 50mM pH 7.4). Then, they were ultracentrifuged at 250.000 x g for 2 hours 449 
at 4°C. At the end of the centrifuga tion, the supernatant was discarded and a very compact and dense 450 
translucent pellet containing ribosomes was quickly rinsed twice by carefully adding 200µL of cold water.  451 
Then, pellet was resuspended in 300µL of buffer C (KCl 25mM, MgCl2 5mM and Tris-Cl 50mM pH 7.4), 452 
adding the solution in three sequential steps and gently homogenized by pipetting after every 100µL 453 
addition. Finally, to estimate the amounts of ribosomes, absorbance at 260nm of the suspensions was 454 
measured by a nanodrop spectrophotometer (ThermoFisher). 455 
 456 
preprint (which was not certified by peer review) is the author/funder. All rights reserved. No reuse allowed without permission. 
The copyright holder for thisthis version posted December 10, 2020. ; https://doi.org/10.1101/2020.07.13.196709doi: bioRxiv preprint 

 17 
Global Translation 457 
Global translation assay was performed using Click -iT® AHA Alexa Fluor ® 488 Protein Synthesis HCS 458 
Assay (Thermo Fisher Scientific). Briefly, HCT116 shNT and shDHX30 cells were cultured in 96 -well 459 
tissue culture plate and treated with 100mM 5 -Fluorouracil (Sigma Aldrich) as positive control. After 24 460 
hours of treatment, the cu lture medium was removed and 50µM L -azidohomoalanine prepared in pre -461 
warmed L-methionine-free medium (Lonza) was added and cells were incubated for 1 hour. Cell fixation 462 
was performed using 3.7% formaldehyde (Sigma Aldrich) incubating the plate at room temperature for 15 463 
minutes. After two washing with 3% BSA in PBS 1X cells were permeabilized with 0.5% Triton ® X-100 464 
(Sigma Aldrich) and incubated for 15 minutes at room temperature. Cells were washed twice with 3% BSA 465 
in PBS 1X and Click -iT® reaction cocktail was added incubating for 30 minutes at room temperature, 466 
protected from light. After the incubation reaction cocktail was removed, cells were washed twice with 3% 467 
BSA in PBS 1X and stained with 5µg/mL Hoechst (Sigma Aldrich). Samples’ images were acquire d and 468 
analysed by high content fluorescence microscope Operetta® (PerkinElmer, Waltham, MA, USA) using the 469 
following filter set: Alexa Fluor® 488: Ex495/Em519 nm; Hoechst: Ex350/Em461 nm.  470 
 471 
Fluorescent In Situ Hybridization (FISH) on rRNA precursors 472 
Cells were cultured on a coverslip place onto a 48-well plate and after 48 hours they were washed with PBS 473 
and fixed with 4% Paraformaldehyde (PFA) (Sigma Aldrich) for 30 minutes at RT. Then, cells were washed 474 
twice with PBS 1X and incubated in 70% ethanol overn ight at 4°C. The day after, cells were rehydrated 475 
with 10% formamide in 2X SSC (Sigma Aldrich), twice for 5 minutes at RT. Meanwhile, buffer A [5µL 476 
formamide, 2.5µL SSC 2X, 2.5µL tRNA (10 ng/µL), water up to 20.25µL and then 2.5µL of each probe 477 
(10 ng/µL)] was incubated for 5 minutes at 90°C and then mixed quickly together with buffer B [25µL 478 
Dextran sulfate 20% in SSC 4X, 1.25µL Bovine Serum Albumin (BSA) (10ng/µL) and 2.5µL 479 
ribonucleoside vanadyl complex (RVC) (200mM)]. Then, 50µL A+B probe solution was dropped onto the 480 
coverslip and it was incubated in a humidified chamber for 3 hours at 37°C. When the incubation was 481 
finished, the coverslip was washed twice with 10% formamide in SSC 2X for 30 minutes at RT and once 482 
with PBS 1X for 5 minutes. Cells were stained with a solution of 0.5µg/mL DAPI (Sigma Aldrich) in PBS 483 
1X for 5 minutes, washed three times with PBS 1X and the coverslip was finally placed with mounting 484 
preprint (which was not certified by peer review) is the author/funder. All rights reserved. No reuse allowed without permission. 
The copyright holder for thisthis version posted December 10, 2020. ; https://doi.org/10.1101/2020.07.13.196709doi: bioRxiv preprint 

 18 
medium on glass slide. Finally, images were acquired using Zeiss Observer z1 fluorescent microscope (Carl 485 
Zeiss, Oberokochen, Germany) with ZEN 2 blue edition software ver. 2.3 (Carl Zeiss). Images’ 486 
fluorescence intensity was measured using Cell Profiler software ver. 3.1.9 (Broad Institute, Cambridge, 487 
MA, USA).  488 
 489 
rRNA biogenesis 490 
rRNA biogenesis was performed following the protocol described by [43,44]. Briefly, cells were cultured 491 
in 96-well tissue culture plates and after 24 hours were treated with Actinomycin D 100nM (Sigma Aldrich) 492 
as positive control. After 24 hours of treatment, 1mM 5-Ethynyluridine (Sigma Aldrich) was added to the 493 
culture medium and the plate was incubated for 2 hours. This short incubation with 5 -EU allows a higher 494 
rate of incorporation in rRNAs than mRNAs, reducing the background signal. Then, cells were fixed using 495 
a working solution 1 (WR1) composed by 125 mM Pipes pH 6.8 (Sigma Aldrich), 10mM EGTA (Sigma 496 
Aldrich), 1mM MgCl2 (Merck Millipore, Burlington, MA, USA), 0.2% Triton® X -100 (Sigma Aldrich) 497 
and 3.7% formaldehyde (Sigma Aldrich). Cells were washed twice with TBS 1X and stained for 30 minutes 498 
at room t emperature using a working solution 2 (WR2) composed by 100mM Tris -HCl pH 8.5 (Sigma 499 
Aldrich), 1mM CuSO4 (Merck Millipore), 10µM fluorescent azide (Sigma Aldrich) and 100mM ascorbic 500 
acid (Merck Millipore). After four washes with TBS containing 0.5% Triton X-100, cells were stained with 501 
0.5µg/mL Hoechst (Sigma Aldrich) and samples’ images were acquired and analysed by high content 502 
fluorescent microscope Operetta® (PerkinElmer) using the following filter set: Alexa Fluor® 488: 503 
Ex495/Em519 nm; Hoechst: Ex350/E m461 nm and setting a threshold on Alexa Fluor® 488 at 500 504 
fluorescent units to plot the percentage of cells with high nucleolar signal intensity. 505 
 506 
Colony formation 507 
1.0x103 HCT116 shNT and shDHX30 cells per well were seeded in a 6-well plate and incubated. Culture 508 
medium was changed every three days. Colonies were ex fixed with 3.7% formaldehyde and stained with 509 
a solution containing 30% Methylene blue (Sigma Aldrich) in water, then washed five times for 5 minutes. 510 
Images were acquired and analysed using Im ageJ software 1.8.0 (National Institute of Health, Bethesda, 511 
MD, USA). 512 
preprint (which was not certified by peer review) is the author/funder. All rights reserved. No reuse allowed without permission. 
The copyright holder for thisthis version posted December 10, 2020. ; https://doi.org/10.1101/2020.07.13.196709doi: bioRxiv preprint 

 19 
 513 
Cell Count in High-Content analysis and Real Time Cell Index Analysis 514 
To analyze cell proliferation by cell count, 1.0x10 3 cells per well were seeded in 96 -well plates and 515 
incubated. Images were acquired by high content fluorescent microscope Operetta® (PerkinElmer) in digital 516 
phase contrast for three days. To analyse cell proliferation by Real Time Cell Analyser xCELLigence ® 517 
(RTCA) (Roche, Basel, Switzerland) the background was set adding the only cell culture medium in each 518 
well of E-plate and incubating 30 minutes. After incubation, background was read. Then 1.0x103 cells per 519 
well were seeded and incubated for 30 minutes and then the E -plate was inserted in the RTCA and 520 
impedance-based cell proliferation was estimated by RTCA readings every 15 minutes in the course of 521 
three days.  522 
 523 
Spheroid assay formation 524 
3.0x103 HCT116 shNT and shDHX30 cells per well were seeded in U-bottom ultra-low attachment 96-well 525 
plate (Corning Incorporated, Corning, NY, USA), centrifuged at 3000 rpm for 5 minutes and incubated. 526 
Starting after three days of incubation, images were acquired every 24 hou rs for eight additional days by 527 
microscope (Leica, Wetzlar, Germany). Spheroids’ area was measured by ImageJ software. 528 
 529 
Immunofluorescence 530 
3.0x105 cells per well were seeded on glass coverslip inserted in 6-well plates and incubated overnight. The 531 
days after, cells were fixed in 4% Paraformaldehyde (PFA) for 15 min. Then the PFA solution was removed 532 
and cells were rinsed twice with PBS 1X. After washing, cells were incubated for 1 hour with blocking 533 
solution (PBS 1X, 5% BSA and 0.5% Triton X -100). Next, cel ls were incubated overnight at 4°C with 534 
primary antibodies (Table 2.4) diluted in blocking solution. The following day, after three washes with PBS 535 
1X, the anti -mouse and anti -rabbit secondary antibodies conjugated with AlexaFluor 488 or AlexaFluor 536 
594 (Invitrogen, Carlsbad, CA, USA) (diluted 1:1000) were added to the samples and incubated for 1 hour 537 
at RT under agitation. Cells were washed with PBS 1X three times and cell nuclei were stained with 538 
0.5µg/mL Hoechst (Sigma Aldrich) (diluted 1:5000). Finally, coverslips were mounted on glass slides and 539 
preprint (which was not certified by peer review) is the author/funder. All rights reserved. No reuse allowed without permission. 
The copyright holder for thisthis version posted December 10, 2020. ; https://doi.org/10.1101/2020.07.13.196709doi: bioRxiv preprint 

 20 
images were acquired using Zeiss Observer Z1 fluorescent microscope and Zen 2012® software (Carl Zeiss 540 
Jena, Germany). The list of primary antibodies used are reported in Table S3. 541 
 542 
Compensatory Glycolytic Test 543 
3.0x103 cells per well were seeded in Xfp cell culture microplate (Agilent Technologies, Santa Clara, CA, 544 
USA) and incubated overnight while XF calibrant solution was added in each well of extracellular flux 545 
cartridge and incubated overnight without CO 2. Th e day after, culture media was removed from cells, 546 
replaced with assay medium and microplate was incubated 45 minutes at 37°C without CO2. Extracellular 547 
flux cartridge was prepared adding 0.5µM rotenone/antimycin A in port A and 50mM 2 -Deoxyglucose in 548 
port B diluted in Xfp assay medium and the cartridge was calibrated by Seahorse XFp analyser setting 549 
Glycolysis Test program. When the calibration was finished, cell microplate was inserted in a Seahorse 550 
XFp analyser starting the analysis.    551 
 552 
RNA extraction and qRT-PCR 553 
3.0x105 cells per well were seeded in a 6 -well plate and incubated overnight. The day after, cells were 554 
starved and lysed with β -mercaptoethanol and RNA was extracted using Illustra RNAspin Mini RNA 555 
Isolation kit (GE -Healthcare, Chicago, IL, USA ) following the kit protocol. Then, RNA was retro -556 
transcribed using the RevertAid RT Kit (Thermo Fisher Scientific). Finally, RT-qPCR was performed using 557 
25ng and 2x qPCR SyGreen (PCR Biosystem, London, England) in Cfx96 TM Real-Time System or 558 
Cfx384TM Real-Time System Thermocyclers (Bio -Rad). The sequence of all primers used is reported in 559 
Table S2.   560 
 561 
Digital droplet PCR 562 
Digital droplet PCR was performed based on the protocol developed by Bio-Rad. Briefly, 1x105 cells were 563 
seeded in 6 -well plate and grown for 1 day. Next cells were detached, counted and solubilized in 564 
DireCtQuant 100ST solubilization reagent (DireCtQuant, Lleida, Spain) at the concentration of 1000 565 
cells/µL, incubating for 3 minutes at 90°C with shaking at 750 rpm and then centrifuged for 1 minute at 566 
10000 g. Lysates were obtained by incubation for 3 minutes at 90°C under shaking at 750 rpm and then 567 
preprint (which was not certified by peer review) is the author/funder. All rights reserved. No reuse allowed without permission. 
The copyright holder for thisthis version posted December 10, 2020. ; https://doi.org/10.1101/2020.07.13.196709doi: bioRxiv preprint 

 21 
centrifuged for 1 minute at 10000 g. Lysate was diluted 1:4 in solubilization reagent and for every target to 568 
analyze, PCR mix was prepared comprising 2µL of diluted sample, forward and reverse primers at 10µM 569 
final concentration in a final volume of 95µL. PCR mix without lysate was used as negative control. Then, 570 
10.5µL of each PCR reaction was mixed w ith 11µL of 2xQX200 ddPCR EvaGreen SuperMix (Bio -Rad) 571 
and 0.5µL of HindIII restriction enzyme (NEB, Ipswich, MA, USA). Sample DNA was digested at 37°C 572 
for 15 minutes and loaded in ddPCR DG8™ Cartridge with QX200™ droplet generation oil (Bio -Rad). 573 
Droplets were made using QX200™ droplet generator (Bio-Rad) and then loaded in a 96-well PCR plate. 574 
Sample DNA was amplified and finally, droplets with amplified DNA were analyzed using the QX200™ 575 
droplet reader and QuantaSoft 1.7.4 (Bio-Rad).      576 
 577 
RNA Immunoprecipitation  578 
HCT116 cells were cultured in standard medium in P150 plates till they reached ~80% confluence. ~10 7 579 
cells were lysed in 1mL of Lysis buffer (100mM KCl, 5mM MgCl 2, 10mM HEPES pH 7, 0.5% NP -40, 580 
1mM DTT, 1U/ul RNase Inhibitors, 1X Protease Inhibito r Cocktail) using a scraper. Lysates were 581 
transferred in a falcon tube, placed for at least two hours at -80°C, and centrifuged at 10000 rpm for 30 582 
minutes. Supernatants were collected in a new tube. Dynabeads ProteinA or ProteinG (depending on the 583 
antibody species, Thermo Fisher scientific) were prepared by washing them twice with NT2 Buffer (50mM 584 
Tris-HCl pH7.4, 150mM NaCl, 1mM MgCl 2; 0.05% NP40) and resuspended in NT2 buffer. Beads were 585 
distributed in different tubes, supplemented with twice their initia l volume of NT2 Buffer. The DHX30 586 
specific antibody (5 µg -A302-218A, Bethyl) or IgGs were added to the beads and incubated for 2 hours 587 
on a rotating wheel at 4°C. Lysates were pre -cleared by adding a mix containing ProteinA and ProteinG 588 
Dynabeads in equal  amounts and incubating for 1 hour at 4°C on a wheel. After placing the tubes on a 589 
magnet, supernatants were collected and 1% of their volume was used as input to be directly extracted with 590 
TRIzol. The remaining supernatant was added to the antibody -coated beads and incubated overnight on a 591 
wheel at 4°C. The day after, beads were washed with 1ml NT2 buffer for 10 minutes on a wheel at 4°C. 592 
Three additional washes were performed again with 1ml NT2 Buffer supplemented with 0.1% Urea + 593 
50mM NaCl (10 minutes ea ch at 4°C on a wheel). Beads were washed one more time in 500µl of NT2 594 
buffer, 50µl were collected for WB analysis and the remaining supernatant was discarded. RNA was 595 
preprint (which was not certified by peer review) is the author/funder. All rights reserved. No reuse allowed without permission. 
The copyright holder for thisthis version posted December 10, 2020. ; https://doi.org/10.1101/2020.07.13.196709doi: bioRxiv preprint 

 22 
extracted by adding TRIzol to the beads, according to the manufacturer’s protocol. The RNA pellets were 596 
resuspended in 15µl DEPC water and cDNAs were synthesized using the RevertAid First Strand cDNA 597 
Synthesis Kit (Thermo Fisher Scientific). 598 
 599 
Cytoplasm-Mitochondria fractionation 600 
For cytoplasm-mitochondria fractionation, 2x106 cells were seeded in a P150 Petri dish and incubated for 601 
2 day. Then, they were detached using trypsin and re-suspended in 750µL of Mitochondrial Isolation Buffer 602 
(MIB) (0.32M Sucrose, 1mM EGTA pH 8.0, 20mM Tris-HCl pH 7.2) with 0.1% fatty acid-free BSA. Cells 603 
were homogenized in a Potter -Elvehjem homogenizer (DWK Life Sciences, Mainz, Germany) applying 604 
more than 60 strokes. Homogenate (A) was centrifuged for 5 minutes at 1000g at 4°C and supernatant was 605 
collected. Cell debris were resuspended in 750µL of MIB + BSA and re-homogenized with more than 20 606 
strokes. New homogenate (B) was centrifuged for 5 minutes at 1000g at 4°C and the supernatant was 607 
collected and pooled with supernatant A. Two mixed supernatants (A+B) were centrifuged at 12000g for 608 
10 minutes at 4°C to pellet the mitochondria. Supernatant was discarded and mitochondria were washed 609 
twice with 1mL of MIB + BSA and once with 1mL of MIB, centrifuging the mitochondrial pellet every 610 
time at 12000g for 10 minutes at 4°C. Finally, supernatant was disc arded and mitochondria were lysed in 611 
RIPA buffer and mitochondrial proteins were quantified by BCA assay.            612 
 613 
Apoptosis assay 614 
Apoptosis analysis was based on FITC Annexin-V Apoptosis Detection Kit protocol (BD Biosciences, San 615 
Jose, CA, USA). Briefly, 3x105 cells per well were seeded in a 6-well plate, incubated for one day and then 616 
treated with drugs under investigation for 48 hours. 0.1% DMSO was used as negative control. Cells were 617 
detached using trypsin and washed twice with PBS 1X. Then, 1.5x105 cells were resuspended in 100µL of 618 
Binding Buffer 1X, stained with FITC-Annexin V and PI and incubated for 15 minutes at room temperature 619 
in the dark. Finally, samples were analyzed by FACSCanto™ flow cytometer and BD Diva Software 6.1.3. 620 
Unstained, PI-only and FITC-only stained samples were used to set the cytometer’s parameters.  621 
 622 
Cell cycle analysis 623 
preprint (which was not certified by peer review) is the author/funder. All rights reserved. No reuse allowed without permission. 
The copyright holder for thisthis version posted December 10, 2020. ; https://doi.org/10.1101/2020.07.13.196709doi: bioRxiv preprint 

 23 
HCT shNT or shDHX30 were seeded in 6-well plates at a concentration of 3x105 cell/well. 48 hours after 624 
seeding, cells were trypsinized, washed with 1X PBS and counted for subsequent staining according to BD 625 
Cycletest™ Plus DNA Kit protocol. Briefly, 5x10 5cells were centrifuged, superantant was removed and 626 
250µl of Solution A were added. Cells were resuspended and incubated for 10 minutes before adding 200 627 
µl of Solution B. After 10 minutes of incubation, 200 µl of ice-cold Solution C were added to the samples 628 
and cells were incubated for 10 minutes at 4°C in the dark before analysis with FACS CantoA (BD). The 629 
percentage of cells in each stage of the cell cycl e (G1, S or G2) was computed using the ModFIT LT 4.0 630 
software (Verity Software House).  631 
 632 
Exploration of TGCA data using the GEPIA web resource 633 
The GEPIA API [17,18] was used to extract correlations between DHX30 and mitoribosomal genes (either 634 
as individual genes or for the 14-genes signature) in all available TCGA tumor datasets (correlation mode). 635 
The same analysis was performed to correlate cytoplasmic ribosome and mitochondrial ribosome genes 636 
expression, on TCGA tumor samples, matched TCGA normal sam ples, and GTEX healthy tissues RNA -637 
seq data. Survival analysis was performed with the same tool and in the same datasets, using the survival 638 
mode. Only results within the p-value threshold of 0.05 were considered, with the others being set to R=0 639 
and HR=1 in the heatmap for visualization purposes. 640 
Statistical analysis 641 
Data are presented as mean ± SD of three independent biological experiments, unless stated otherwise. 642 
GraphPad Prism 5 or 9 software (GraphPad software, La Jolla, CA, USA) were used and either a two-way 643 
anova with Tukey’s multiple comparison test or a two -tailed Student’s t -test was performed, unless 644 
specified otherwise.  645 
 646 
Data availability 647 
The RNA-seq datasets are available in GEO with ID GSE95024 and GSE154065. 648 
 649 
preprint (which was not certified by peer review) is the author/funder. All rights reserved. No reuse allowed without permission. 
The copyright holder for thisthis version posted December 10, 2020. ; https://doi.org/10.1101/2020.07.13.196709doi: bioRxiv preprint 

 24 
Acknowledgements 650 
We thank Pamela Gatto, Viktoryia Sirarovich and Michael Pancher of the HTS CIBIO core facility for 651 
assistance with droplet digital PCR experiments, high -content as well as impedance -based proliferation 652 
assays. We thank Nicoletta di Bernard o for technical assistance for the apoptosis assays. This work was 653 
supported by the Italian Association for Cancer Research (Fondazione AIRC, IG grant #18985 to AI). JJD 654 
laboratory is supported by grants by the Institut National du Cancer (INCa, grant PRT-K program n°2018-655 
024 EMT-CoNCEPT) and Agence Nationale de la Recherche (ANR, grant RiboCard ANR-18-CE11-0020, 656 
and grant ActiMeth ANR-19-CE12-0004). 657 
 658 
Competing Interests 659 
The Authors declare no competing interest. 660 
 661 
Authors contributions 662 
B.B. perfomed most experiments and wrote the first draft of the paper. A.R., D.R., S.G., A.P., F.B., and, 663 
A.G. helped in some experimental procedure s. F.C. and J -J.D. helped to design some experiments . E.D. 664 
performed all data analysis. E.D. and A.I. designed the study. A.I. co-wrote the first draft of the manuscript. 665 
 666 
References 667 
 668 
1.  Zheng HJ, Tsukahara M, Liu E, Ye L, Xiong H, Noguchi S, et al. The novel helicase helG (DHX30) 669 
is expressed during gastrulation in mice and has a structure similar to a human DExH box helicase. 670 
Stem Cells Dev. 2015;24: 372–383. doi:10.1089/scd.2014.0077 671 
2.  Ye P, Liu S, Zhu Y, Chen G, Gao G. DEXH -Box protein DHX30 is required for optimal function 672 
of the zinc-finger antiviral protein. Protein Cell. 2010; doi:10.1007/s13238-010-0117-8 673 
3.  Lessel D, Schob C, Kury S, Reijnders MRF, Harel T, Eldomery MK, et al. De Novo Missense 674 
Mutations in DHX30 Impair Global Translation and Cause a Neurodevelopmental Disorder. Am J 675 
Hum Genet. 2017;101: 716–724. doi:10.1016/j.ajhg.2017.09.014 676 
4.  Antonicka H, Shoubridge EA. Mitochondrial RNA Granules Are Centers for Posttranscriptional 677 
RNA Processing and Ribosome Biogenesis. Cell Rep. 2015;10: 920 –932. 678 
doi:10.1016/j.celrep.2015.01.030 679 
5.  Andrysik Z, Galbraith MD, Guarnieri AL, Zaccara S, Sullivan KD, Pandey A, et al. Identification 680 
of a core TP53 transcriptional program with highly distributed tumor suppressive activity. Genome 681 
Res. 2017;27. doi:10.1101/gr.220533.117 682 
6.  Rizzotto D, Zaccara S, Rossi A, Galbraith MD., Andrysik Z, Pandey A, et al. Nutlin-Induced 683 
Apoptosis is Specified by a Translation Program Regulated by PCBP2 and DHX30. Cell Rep. 684 
2020;30: 1–15.  685 
7.  Tovar C, Rosinski J, Filipovic Z, Higgins B, Kolinsky K, Hilton H, et al. Small -molecule MDM2 686 
antagonists reveal aberrant p53 signaling in cancer: implications for therapy. Proc Natl Acad Sci U 687 
S A. 2006;103: 1888–1893. doi:10.1073/pnas.0507493103 688 
8.  Sergushichev AA. An algorithm for fast preranked gene set enr ichment analysis using cumulative 689 
preprint (which was not certified by peer review) is the author/funder. All rights reserved. No reuse allowed without permission. 
The copyright holder for thisthis version posted December 10, 2020. ; https://doi.org/10.1101/2020.07.13.196709doi: bioRxiv preprint 

 25 
statistic calculation. bioRxiv. 2016; doi:10.1101/060012 690 
9.  Van Nostrand EL, Pratt GA, Shishkin AA, Gelboin-Burkhart C, Fang MY, Sundararaman B, et al. 691 
Robust transcriptome-wide discovery of RNA -binding protein binding si tes with enhanced CLIP 692 
(eCLIP). Nat Methods. 2016;13: 508–514. doi:10.1038/nmeth.3810 693 
10.  Mills EW, Green R. Ribosomopathies: There’s strength in numbers. Science. 2017. p. eaan2755. 694 
doi:10.1126/science.aan2755 695 
11.  Wang Y, Bogenhagen DF. Human mitochondr ial DNA nucleoids are linked to protein folding 696 
machinery and metabolic enzymes at the mitochondrial inner membrane. J Biol Chem. 2006;281: 697 
25791–802. doi:10.1074/jbc.M604501200 698 
12.  Smith AC, Robinson AJ. MitoMiner v3.1, an update on the mitochondrial pro teomics database. 699 
Nucleic Acids Res. Oxford University Press; 2016;44: D1258–D1261. doi:10.1093/nar/gkv1001 700 
13.  Armenteros JJA, Salvatore M, Emanuelsson O, Winther O, Von Heijne G, Elofsson A, et al. 701 
Detecting sequence signals in targeting peptides using deep learning. Life Sci Alliance. Rockefeller 702 
University Press; 2019;2. doi:10.26508/lsa.201900429 703 
14.  Fazal FM, Han S, Parker KR, Kaewsapsak P, Xu J, Boettiger AN, et al. Atlas of Subcellular RNA 704 
Localization Revealed by APEX-Seq. Cell. 2019; doi:10.1016/j.cell.2019.05.027 705 
15.  Heiden MGV, Cantley LC, Thompson CB. Understanding the warburg effect: The metabolic 706 
requirements of cell proliferation. Science. 5930: 1029 -1033; 2009. p. 324. 707 
doi:10.1126/science.1160809 708 
16.  Schwanhüusser B, Busse D, Li N, Dittmar G, Schuchhardt J, Wolf J, et al. Global quantification of 709 
mammalian gene expression control. Nature. 2011;473: 337–342. doi:10.1038/nature10098 710 
17.  Tang Z, Li C, Kang B, Gao G, Li C, Zhang Z. GEPIA: A web server for cancer and normal gene 711 
expression profiling and interactive analyses. Nucleic Acids Res. 2017;45: W98 –W102. 712 
doi:10.1093/nar/gkx247 713 
18.  Tang Z, Kang B, Li C, Chen T, Zhang Z. GEPIA2: an enhanced web server for large -scale 714 
expression profiling and interactive analysis. Nucleic Acids Res.  2019;47: W556 –W560. 715 
doi:10.1093/nar/gkz430 716 
19.  Wieser W, Krumschnabel G. Hierarchies of ATP -consuming processes: Direct compared with 717 
indirect measurements, and comparative aspects. Biochem J. 2001; 389 –95. doi:10.1042/0264 -718 
6021:3550389 719 
20.  Buttgereit F, Brand MD. A hierarchy of ATP -consuming processes in mammalian cells. Biochem 720 
J. 1995; 163–7. doi:10.1042/bj3120163 721 
21.  Couvillion MT, Soto IC, Shipkovenska G, Churchman LS. Synchronized mitochondrial and 722 
cytosolic translation programs. Nature. 2016;533: 499–503. doi:10.1038/nature18015 723 
22.  Calamita P, Gatti G, Miluzio A, Scagliola A, Biffo S. Translating the game: Ribosomes as active 724 
players. Front Genet. 2018;15: 533. doi:10.3389/fgene.2018.00533 725 
23.  Pla‐Martín D, Schatton D, Wiederstein JL, Marx M, K hiati S, Krüger M, et al. CLUH granules 726 
coordinate translation of mitochondrial proteins with mTORC1 signaling and mitophagy. EMBO J. 727 
2020;39: e102731. doi:10.15252/embj.2019102731 728 
24.  Morita M, Prudent J, Basu K, Goyon V, Katsumura S, Hulea L, et al. mTOR Controls Mitochondrial 729 
Dynamics and Cell Survival via MTFP1. Mol Cell. 2017;67: 922 –935. 730 
doi:10.1016/j.molcel.2017.08.013 731 
25.  Clarke K, Ricciardi S, Pearson T, Bharudin I, Davidsen PK, Bonomo M, et al. The Role of Eif6 in 732 
Skeletal Muscle Homeostasis Revealed by Endurance Training Co-expression Networks. Cell Rep. 733 
2017; doi:10.1016/j.celrep.2017.10.040 734 
26.  Biffo S, Manfrini N, Ricciardi S. Crosstalks between translation and metabolism in cancer. Current 735 
Opinion in Genetics and Development. 2018. doi:10.1016/j.gde.2017.10.011 736 
27.  Ricciardi S, Manfrini N, Alfieri R, Calamita P, Crosti MC, Gallo S, et al. The Translational 737 
Machinery of Human CD4 + T Cells Is Poised for Activation and Controls the Switch from 738 
Quiescence to Metabolic Remodeling. Cell Metab. C ell Press; 2018;28: 895 -906.e5. 739 
doi:10.1016/j.cmet.2018.08.009 740 
28.  Pourdehnad M, Truitt ML, Siddiqi IN, Ducker GS, Shokat KM, Ruggero D. Myc and mTOR 741 
converge on a common node in protein synthesis control that confers synthetic lethality in Myc -742 
driven cancers. Proc Natl Acad Sci U S A. 2013;110: 11988–93. doi:10.1073/pnas.1310230110 743 
29.  Hong S, Freeberg MA, Han T, Kamath A, Yao Y, Fukuda T, et al. LARP1 functions as a molecular 744 
switch for mTORC1-mediated translation of an essential class of mRNAs. Elife. 2017;6: e25237. 745 
preprint (which was not certified by peer review) is the author/funder. All rights reserved. No reuse allowed without permission. 
The copyright holder for thisthis version posted December 10, 2020. ; https://doi.org/10.1101/2020.07.13.196709doi: bioRxiv preprint 

 26 
doi:10.7554/eLife.25237 746 
30.  Amaldi F, Pierandrei -Amaldi P. TOP genes: a translationally controlled class of genes including 747 
those coding for ribosomal proteins. Progress in molecular and subcellular biology. 1997. pp. 1–17. 748 
doi:10.1007/978-3-642-60471-3_1 749 
31.  Gressner O, Schilling T, Lorenz K, Schulze Schleithoff E, Koch A, Schulze -Bergkamen H, et al. 750 
TAp63alpha induces apoptosis by activating signaling via death receptors and mitochondria. Embo 751 
J. 2005;24: 2458–2471. doi:10.1038/sj.emboj.7600708 752 
32.  Kissil JL, Deiss LP, Bayewitch M, Raveh T, Khaspekov G, Kimchi A. Isolation of DAP3, a novel 753 
mediator of interferon -γ-induced cell death. J Biol Chem. 1995;46: 27932 –6. 754 
doi:10.1074/jbc.270.46.27932 755 
33.  Yoo YA, Kim MJ, Park JK, Chung YM, Lee J H, Chi S-G, et al. Mitochondrial Ribosomal Protein 756 
L41 Suppresses Cell Growth in Association with p53 and p27Kip1. Mol Cell Biol. 2005;15: 6603–757 
13. doi:10.1128/mcb.25.15.6603-6616.2005 758 
34.  Kim HJ, Maiti P, Barrientos A. Mitochondrial ribosomes in cancer. Seminars in Cancer Biology. 759 
2017. pp. 67–81. doi:10.1016/j.semcancer.2017.04.004 760 
35.  Bolger AM, Lohse M, Usadel B. Trimmomatic: a flexible trimmer for Illumina sequence data. 761 
Bioinformatics. 2014;30: 2114–2120. doi:10.1093/bioinformatics/btu170 762 
36.  Patro R, Duggal G, Love MI, Irizarry RA, Kingsfor C. Salmonprovides accurate, fast, and bias -763 
aware transcript expression estimates using dual-phase inference. bioRxiv Prepr. 2016;  764 
37.  Robinson MD, McCarthy DJ, Smyth GK. edgeR: a Bioconductor package for differential expression 765 
analysis of digital gene expression data. Bioinformatics. 2010;26: 139 –140. 766 
doi:10.1093/bioinformatics/btp616 767 
38.  Bailey TL. DREME: Motif discovery in transcription factor ChIP -seq data. Bioinformatics. 768 
2011;15: 1653–1659. doi:10.1093/bioinformatics/btr261 769 
39.  Provenzani A, Fronza R, Loreni F, Pascale A, Amadio M, Quattrone A. Global alterations in mRNA 770 
polysomal recruitment in a cell model of colorectal cancer progression to metastasis. 771 
Carcinogenesis. 2006;27: 1323–1333. 772 
40.  Viero G, Lunelli L, Passerini A, Bianchini P, Gilbert RJ, Bernabò P, et al. Three distinct ribosome 773 
assemblies modulated by translation are the building blocks of polysomes. J Cell Biol. 2015;208: 774 
581–96. doi:10.1083/jcb.201406040 775 
41.  Panda A, Martindale J, Gorospe M. Polysome Fractionation to Analyze mRNA Distribution 776 
Profiles. BIO-PROTOCOL. 2017;7: e2126. doi:10.21769/bioprotoc.2126 777 
42.  Belin S, Hacot S, Daudignon L, Therizols G, Pourpe S, Mertani HC, et al. Purification of ribosomes 778 
from hum an cell lines. Current Protocols in Cell Biology. 2010. p. unit 3.40. 779 
doi:10.1002/0471143030.cb0340s49 780 
43.  Cornella N, Tebaldi T, Gasperini L, Singh J, Padgett RA, Rossi A, et al. The hnRNP RALY regulates 781 
transcription and cell proliferation by modulating the expression of specific factors including the 782 
proliferation marker E2F1. J Biol Chem. 2017;292: 19674–19692. doi:10.1074/jbc.M117.795591 783 
44.  Rossi A, Moro A, Tebaldi T, Cornella N, Gasperini L, Lunelli L, et al. Identification and dynamic 784 
changes of RNAs isolated from RALY-containing ribonucleoprotein complexes. Nucleic Acids Res. 785 
2017;45: 6775–6792. doi:10.1093/nar/gkx235 786 
 787 
 788 
 789 
  790 
preprint (which was not certified by peer review) is the author/funder. All rights reserved. No reuse allowed without permission. 
The copyright holder for thisthis version posted December 10, 2020. ; https://doi.org/10.1101/2020.07.13.196709doi: bioRxiv preprint 

 27 
Table S1: RNA-seq Fold Change data and results of GSEA analysis for the comparison between 791 
HCT_shDHX30 and HCT_shNT. 792 
A), B) ID, gene symbol, fold change, F value, P value and FDR based on RNA-seq data of (A) polysomal 793 
RNA, (B) total RNA. GSEA data for polysomal (C) or total (D) RNA-seq data. 794 
 795 
Table S2: siRNAs, FISH probe, and primers. 796 
Contains information on all primers used in qRT-PCR experiments. 797 
 798 
Table S3: List of primary and secondary antibodies 799 
 800 
 801 
Figure legends 802 
 803 
Figure 1. DHX30 reduces ribosome biogenesis and translation in HCT116 colorectal cancer cells. 804 
A) Most significant terms by Gene Set Enrichment Analysis  of the polysome -bound DEGs 805 
(HCT_shDHX30 vs HCT sh_NT). Bars plot the Normalized Enrichment Score, (NES). Numbers indicate 806 
the number of genes in the leading edge. See Table S1 for full results. B) Box plot of Translation efficiency 807 
for the indicated transcript groups. The RNA-seq CPM in polysomal over total RNA was measured. Results 808 
obtained in HCT116_shDHX30 cells are compared to the shNT control clone ; *p < 0.05, ***p < 0.001. C) 809 
Amounts of ribosomes produced in HCT116_shDHX30 and HCT_shNT. After ribosomes isolation, protein 810 
absorbance was measured at λ 260nm. Data are normalized on shNT and are mean ± SD (n=3); *p < 0.05. 811 
D) Amount of ribosomal RNA estimated based on the fluorescence intensity of 5-ethynyl uridine (5-EU) 812 
incorporated in nascent rRNAs present in the nucleoli. HCT116_shDHX30 cells are compared to the shNT 813 
control clone in untreated condition while Actinomycin-D treatment was used as a control. Data are mean 814 
± SD (n=6); ***p < 0.00 1. E) (Left) Representative images of one of three independent experiments of 815 
Fluorescent In Situ Hybridization (F ISH) for rRNA precursor 18S (red). Immunofluorescence of tubulin 816 
(green) and staining with DAPI (blue) were used to visualize cells.  (Right) Box plot of 18S rRNA intensity 817 
quantification comparing HCT116_shDHX30 with HCT_shNT analyzed with Cell Profiler software. Data 818 
are expressed as mean per well ± SD of three biological replicates in which 10 nuclei were quantified for 819 
each replicate ; *p < 0.05. F) Analysis of global translation based on the fluorescence intensity of L -820 
azidohomoalanine (AHA) incorporated in nascent proteins present in the cytoplasm. HCT116_shDHX30 821 
cells are compared to the shNT control clone in untreated condition while 5 -Fluorouracil treatment was 822 
used as positive control. Data are mean ± SD (n=6 to 9); ***p < 0.005. G) (Left) Polysome profiling of 823 
preprint (which was not certified by peer review) is the author/funder. All rights reserved. No reuse allowed without permission. 
The copyright holder for thisthis version posted December 10, 2020. ; https://doi.org/10.1101/2020.07.13.196709doi: bioRxiv preprint 

 28 
HCT_shNT and HCT_shDHX30, revealed by the measurement of absorbance at a wavelength of 260 nm. 824 
(Right) Box plot of the relative quantification of the area under the curve of fractions corresponding to the 825 
polysomes related to the fractions corresponding to the ribosomal subunits and 80S monosome (POL/SUB, 826 
an estimate of translation efficiency). Data are mean ± SD (n=7); *p < 0.05.  827 
 828 
Figure 2. Cytoplasmic DHX30 modulates the expression of nuclear encoded mito -ribosome 829 
components MRPL11 and MPRS22.  830 
A) RNA immunoprecipitation experiments to study the binding of DHX30 to MRPL11 and MRPS22 831 
transcripts. Results obtained with a primary antibody targeting DHX30 (blue) or the control IgG control 832 
(grey) are plotted relative as % of input. Data are mean and individual points (n=2); p-value was calculated 833 
comparing the amount of each sample with the amount of RNR1 mRNA; *p < 0.05 , ***p < 0.0 01. B) 834 
Relative mRNA levels of MRPL11 and MRPS22 in HCT116_shDHX30 compared to th e shNT control 835 
clone. Data are mean ± SD (n=3); *p < 0.05; **p < 0.01. C) (Left) Protein levels of MRPL11 and MRPS22. 836 
β-Tubulin was used as loading control. Immunoblots represent one of three independent experiments. 837 
(Right) MRPL11 and MRPS22 protein quantification in HCT116_shDHX30 normalized on shNT control 838 
clone. Data are mean ± SD (n=3); *p < 0.05. D) Representative images of one of three independent 839 
immunofluorescence experiments to colocalize DHX30 (red) with MT-ATP6 (green, used as mitochondrial 840 
marker). Staining with Hoechst (blue) was used to visualize cells' nuclei. E) Relative mRNA levels of 841 
cytoplasmic DHX30 (cDHX30) and the mitochondrial variant (mDHX30, set to 1). Data are mean ± SD 842 
(n=3); ***p < 0.001. F) Relative DHX30 protein levels in cytoplasm and mitochondria. β-Tubulin and MT-843 
ATP6 are used as controls of cytoplasmic -mitochondrial fractionation and Ponceau -S staining is used as 844 
loading control. One of three independent experiments is shown.  845 
 846 
Figure 3. Transient DHX30 silencing leads to enhanced translation but reduced mitorobosome gene 847 
expression in HCT116 cells. 848 
A) qRT-PCR to verify the silencing of DHX30 transcripts in HCT116 96 hours after transient transfection 849 
with the indicate d siRNAs. The r elative mRNA levels of cytoplasmic (cDHX30) and mitochondrial 850 
(mDHX30) DHX30 transcripts as well as of total DHX30 (measured with a pair or primers common to all 851 
preprint (which was not certified by peer review) is the author/funder. All rights reserved. No reuse allowed without permission. 
The copyright holder for thisthis version posted December 10, 2020. ; https://doi.org/10.1101/2020.07.13.196709doi: bioRxiv preprint 

 29 
annotated transcripts). Data are mean ± SD (n=3); **p < 0.01; ***p < 0.001.  B) Global translation based 852 
on the fluorescence intensity of L-azidohomoalanine (AHA) incorporated in nascent proteins present in the 853 
cytoplasm. HCT116 were transiently transfected with the indicated siRNAs and  tested after 96 hours. 5-854 
Fluorouracil treatment was used as control treatment leading to translation inhibition. Data are mean ± SD 855 
(n=3); * p < 0.05; **p < 0.01. C) mRNA levels of MRPL11 and MRPS22 in HCT116 silenced transiently 856 
for cytoplasmic DHX30 (HCT_siDHX30 -C) or for both cytoplasmic and mitochondrial variants 857 
(HCT_siDHX30-C+M). Data are compared to the siRNA negative control (HCT_siNC) and are mean ± 858 
SD (n=3); *p < 0.05. D) (Left) MRPL11 and MRPS22 protein levels in HCT116 silenced for cytoplasmic 859 
DHX30 (HCT_siDHX30-C) or for both cytoplasmic and mitochondrial variants (HCT_siDHX30 -C+M). 860 
Immunoblot represents one of three independent experiments. (Right) MRPL11 and MRPS22 protein 861 
quantification in HCT116_siDHX30 -C and HCT116_siDHX30 -C+M normalized on α -actinin and 862 
compared to siNC control. Data are mean ± SD (n=3); *p < 0.05. 863 
 864 
 865 
Figure 4. Depletion of DHX30 reduces the expression and function of mitochondrially encoded 866 
OXPHOS components.  867 
A) Relative mitochondrial genome copy number in HCT116_shDHX30 and -shNT measured by droplet 868 
digital PCR. MT -RNR1 and MT -ATP8 were amplified along with the nuclear diploid marker gene 869 
CTDSP1. Bars plot mean ± SD (n=3). B) Relative mRNA levels of mitochondrially encoded OXPHOS 870 
components in HCT116_shDHX30 compared to HCT116_shNT (dashed line, set to 1). For both upper and 871 
lower panel, data are mean ± SD (n=3); *p < 0.05; **p < 0.01. C) Protein levels of MT -ATP6 and MT-872 
ATP8 in mitochondrial lysates of HCT116_shDHX30 and the shNT control clone. Ponceau-S was used as 873 
loading contro l. Immunoblots represent one of two independent qualitative comparisons. D) Relative 874 
mRNA levels of the indicated mitochondrially encoded OXPHOS components in HCT116 transiently 875 
silenced for DHX30 expression (siDHX30 -C, siDHX30-C+M) compared to siNC (dashe d line, set to 1). 876 
Data are mean ± SD (n=3); *p < 0.05; **p < 0.01; ***p < 0.001. E) (Left) Protein levels of MT-ATP6 and 877 
MT-ATP8 in HCT116 transiently silenced as in D). α -actinin was used as loading control. Immunoblots 878 
represent one of three independent experiments. (Right) MT-ATP6 and MT-ATP8 protein quantification in 879 
preprint (which was not certified by peer review) is the author/funder. All rights reserved. No reuse allowed without permission. 
The copyright holder for thisthis version posted December 10, 2020. ; https://doi.org/10.1101/2020.07.13.196709doi: bioRxiv preprint 

 30 
HCT116_siDHX30-C and HCT116_siDHX30 -C+M normalized on α -actinin and compared to siNC 880 
control. Data are mean ± SD (n=3); **p < 0.01; ***p < 0.001 .  F) (Left) Measurement of the oxygen 881 
consumption rate (OCR) to evaluate mitochondrial respiration by Seahorse XF analyzer. Points before the 882 
Rotenone/Antimycin-A (Rot/AA) treatment correspond to the basal mitochondrial respiration. (Right) 883 
Extracellular acidification rate (ECAR) measurement was used as a means to measure glycolysis. Points 884 
before and after the Rotenone/Antimycin -A (Rot/AA) treatment correspond respectively to basal and 885 
compensatory glycolysis -in response to the block of mitochondrial respiration -. 2-Deoxyglucose (2-DG) 886 
is then used to block glycolysis. For both panels, one of three independent replicates is presented. Data are 887 
mean ± SD (n=3 wells in the Seahorse cartridge); *p < 0.05.        888 
 889 
Figure 5. Depletion of DHX30 reduces proliferation and survival in basal and treatment conditions 890 
A) (Left) Representative image of colony formation assays. (Right) Colony quantification by ImageJ 891 
software. Data are mean ± SD (n=3). B) Relative cell proliferation measured by high-content microscopy 892 
in digital phase contrast. Data are mean ± SD (n=3). C) Estimate of relative proliferation by an impedance-893 
based Real-Time Cell Analyzer. Data are mean ± SD (n=3). D) Spheroid formation and growth assay. (Left) 894 
A representative image at the indicated time points is shown in the left panel. (Right) Sp heroid area 895 
measured by ImageJ software. Data are mean ± SD (n=3). E) (Left) Representative image of 896 
HCT116_shNT and shDHX30 cell cycle profiles. (Right) Quantification of cell cycle profile in HCT116 897 
DHX30 depleted cells compared to shNT control. Data are  mean ± SD (n=3). F) Lef panel: r elative 898 
expression of eIF2alpha and phosho-eIF2alpha in HCT116 cells stably depleted for DHX30 expression or 899 
control. A representative immunodetection image is shown. Right panel: relative average protein 900 
quantification and SD of three replicates is presented in the bar graph; n = 3, *p < 0.05 . G) Relative 901 
proliferation measured as in B) but starting 24 hours after tran sient silencing DHX30 with the indicated 902 
siRNAs. H) Relative expression of the annexin-V apoptosis markers in cells treated for 48 hours with the 903 
indicated drugs or DMSO control. For all panels, data are mean ± SD (n=3); *p < 0.05; **p < 0.01. 904 
 905 
Figure 6. D HX30 expression positively correlates with the expression of mitoribosomal protein 906 
transcripts and can have prognostic significance. 907 
preprint (which was not certified by peer review) is the author/funder. All rights reserved. No reuse allowed without permission. 
The copyright holder for thisthis version posted December 10, 2020. ; https://doi.org/10.1101/2020.07.13.196709doi: bioRxiv preprint 

 31 
The table presents the expression correlation data (R value and p value) between DHX30 and the combined 908 
group of 14 mitoribosomal protein transcripts is listed for each cancer type (see also  Figure S6). Data from 909 
Kaplan-Meier survival analysis for the aggregated 15 -gene signature (DHX30 + the 14 mitoribosomal 910 
protein transcripts) are shown. Significant differences are highlighted in bold font. The tumor type acronym 911 
and extended name are also shown. The graphs below the table presents t wo examples among the cluster 912 
of eleven cancer types where a positive correlation is apparent . Left panels: Pearson correlation. Right 913 
panels: Overall Survival Kaplan-Meier. The correlation value, the Hazardous Ratio, p values and sample 914 
sizes are shown. 915 
  916 
preprint (which was not certified by peer review) is the author/funder. All rights reserved. No reuse allowed without permission. 
The copyright holder for thisthis version posted December 10, 2020. ; https://doi.org/10.1101/2020.07.13.196709doi: bioRxiv preprint 

 32 
Figure 1 917 
  918 
0 .0
0 .5
1 .0
1 .5
2 .0 **
HCT: shNT shDHX30
0.3
0.0
0.1
0.218S rRNA intensity
*
HCT_sh
NT
HCT_sh
DHX30
0
500
1000
1500
2000
2500
AHA intensity
DMSO 5-FU
***
(fluorescenceu n its)
HCT_shNT HCT_shDHX30
5-EU rRNA amount
HCT_shNT HCT_shDHX30
0
1
2
3POL/SUB
*
A B C
D E
F G
DAPI Tubulin
0.5
1.0
1.5
2.0
*** ****
RPL
Translation Efficiency
(POL/TOT)
RPS MRP L MRPS
shNT + ++ +
shDHX30 + + + +
HCT:
18S
HCT_shNTHCT_shDHX30
A260nm
Fractions
HCT_shDHX30
HCT: shNT shDHX30
GO RIBOSOME
KEGG RIBOSOME
Normalized Enrichment Score
Pathway
GO RIBOSOMAL
SUBUNITS
GO OF PROTEIN
LOCALIZATION IN ER
CYTOSOLIC RIBOSOME
GO MRNA CATABOLIC
PROCESS DECAY
GO LARGE RIBOSOMAL
SUBUNIT
GO CYTOSOLIC LARGE
RIBOSOMAL SUBUNIT
GO CELLULAR
GLUCORONIDATION
GO GLUCORONOSYL
TRANSFERASE ACTIVITY
-2 -1 0 1 2
4
4
48
72
142
81
84
120
77
78
A260nm
Fractions
HCT_shNT
SUB POL
SUB POL
Relarive ribosome amount(Abs mesured at 260nm)
100
80
0
20
40
60
DMSO Act-D
%o fh i g hn u c l e o l a ri n t e n s i t yc e l l s
(threshold 500 FU)
***
preprint (which was not certified by peer review) is the author/funder. All rights reserved. No reuse allowed without permission. 
The copyright holder for thisthis version posted December 10, 2020. ; https://doi.org/10.1101/2020.07.13.196709doi: bioRxiv preprint 

 33 
Figure 2 919 
  920 
Cyto MitoF HCT:
MRPL11
MRPS22
HCT: shNT shDHX30
0.0
0.5
1.0
1.5
Relative Protein
level
* *
HCT_shNT HCT_shDHX30
Merge
0. 0
0. 5
1. 0
1. 5Fold Change
Hoechst Anti-MT-ATP6Anti-DHX30
A B
***
D E
** *
0.0
0.5
1.0
1.5Fold Change
HCT_shNT
HCT_shDHX30
mDHX30
IgG
DHX30
MRPL11 MRPS22
MRPL11 MRPS22
40 KDa
21 KDa
55 KDa
55 KDa
25 KDa
130 KDaDHX30
β-Tubulin
MT-ATP6
Ponceau-S
β-Tubulin
C
10um 10um 10um 10um
cDHX30
MRPL11MRPS22MT-RNR10.00
0.01
0.02
1
2
3
%input
✱
✱✱✱
preprint (which was not certified by peer review) is the author/funder. All rights reserved. No reuse allowed without permission. 
The copyright holder for thisthis version posted December 10, 2020. ; https://doi.org/10.1101/2020.07.13.196709doi: bioRxiv preprint 

 34 
Figure 3 921 
  922 
siNC
siDHX30-C
siDHX30-C+M
A
1500
1000
500
0
DMSO 5-FU
AHA Intensity
(Fluorescence Units)
*
** **
*** ***
1.5
0.0
0.5
1.0Fold change
cDHX30 mDHX30DHX30
HCT- 96h
nsns
B
C
0 .0
0 .5
1 .0
1 .5
Fold Change
* *
MRPL11 MRPS22
*
ns
D
HCT_siDHX30-C
HCT_siDHX30-C+M
2.0
0.5
1.0
1.5
0.0
MRPL11 MRPS22
* *
siNCsiDHX30-CHCT116: siDHX30-C+M
40 KDa
21 KDa
105 KDa
MRPS22
MRPL11
α-actinin
Relative Protein
level
ns
ns
siNC
siDHX30-C
siDHX30-C+M
**
preprint (which was not certified by peer review) is the author/funder. All rights reserved. No reuse allowed without permission. 
The copyright holder for thisthis version posted December 10, 2020. ; https://doi.org/10.1101/2020.07.13.196709doi: bioRxiv preprint 

 35 
Figure 4 923 
  924 
HCT:
MT-ATP6
MT-ATP8
shNT shDHX30
Ponceau-S
MT-RNR1 MT-ATP8
0.0
0.5
1.0
1.5
Relative mitochondrial genome
copy number(shDHX30/shNT)
A B
0.0
0.5
1.0
1.5
Fold Change
(shDHX30/shNT)
0.0
0.5
1.0
1.5
Fold Change
(shDHX30/shNT)
ECAR (mpH/min)
*
Rot/AA
2-DG
OCR (pmol/min)
*
Rot/AA
2-DG
Fold Change
(siDHX30/siNC)
*
** **
**
***
**
***
C
D E
F
25 KDa
12 KDa
HCT_shNT
HCT_shDHX30
HCT_shNT
HCT_shDHX30350
300
250
200
150
100
50
0
0 10 20 30 40 50 60 70 80
Time (min) Time (min)
0 10 20 30 40 50 60 70 80
160
140
120
100
80
60
40
0
20
*
MT-ATP6 MT-ATP8
2.0
0.0
0.5
1.0
1.5
HCT_siDHX30-C
HCT_siDHX30-C+M
Relative Protein
level
MT-ATP6
HCT_siDHX30-C HCT_siDHX30-C+M
1.5
0.0
0.5
1.0
MT-CYBMT-COX3MT-RNR2MT-ND3MT-ND4MT-ATP6MT-ATP8
MT-ATP8
α-actinin
HCT: siNCsiDHX30-CsiDHX30-C+M
25 KDa
12 KDa
105 KDa ***
**
ns
nsnsns
ns
ns
MT-ND1MT-ND2MT-ND3MT-ND4
MT-ND4LMT-ND5MT-ND6
MT-ATP6MT-ATP8
ns ns
ns
ns
* * * * *
**** * **
ns
MT-COX1MT-COX2MT-COX3MT-RNR1MT-RNR2 MT-CYB
preprint (which was not certified by peer review) is the author/funder. All rights reserved. No reuse allowed without permission. 
The copyright holder for thisthis version posted December 10, 2020. ; https://doi.org/10.1101/2020.07.13.196709doi: bioRxiv preprint 

 36 
Figure 5 925 
 926 
927 
0
2000
4000
6000
8000
10000
**
0
200
400
600 ***
A B
C
Spheroidsarea(μm2)4x10⁵
1x10⁵
2x10⁵
3x10⁵
***
**
*
D
HCT_shDHX30 HCT_shNT
72 98 120
DMSO
Doxorubicin
FCCP Nutlin
0
20
40
60
80
100
*
*
**
G H
24 48 72 96 120
0
2000
4000
6000
8000
HCT_NC
HCT_siDHX30-C
HCT_siDHX30-C+M
*
*
*
shNT shDHX30HCT:
Cellcount
HCT: shNT shDHX30
NormalizedCellIndex
45
455
15
25
35
0 30 45 60
HCT_shNT HCT_shDHX30
Numberofcolonies
Time(hrs)
Time(hrs)
Hourspostseeding
HCT_shNT HCT_shDHX30
HCT_shNT HCT_shDHX30
HCT_shNT HCT_shDHX30
00 50 100 150 200
02 0 4 06 0 8 0
Hourspostseeding
Apoptosis(%)
Cellcount
0
75
***
E
0
20
40
60
80
G105 0 K 1 0 0 K 1 5 0 K S G2/M
Cellcyclephase
Relativeproportion(%)
HCT_shNT
HCT_shDHX30
PerCP-A
Eventsnumber
Time(hrs)
HCT_shNT HCT_shDHX30
ns
ns
ns
ns
eIF2α
ß-tubulin
p-eIF2α
α-actinin
50KDa
36KDa
105KDa
36KDa
HCT: shNTshDHX30 2.0
0.5
1.0
1.5
0.0RelativeProteinlevel
p-eIF2α/eIF2α
HCT_shNT HCT_shDHX30
*
F
preprint (which was not certified by peer review) is the author/funder. All rights reserved. No reuse allowed without permission. 
The copyright holder for thisthis version posted December 10, 2020. ; https://doi.org/10.1101/2020.07.13.196709doi: bioRxiv preprint 

 37 
Figure 6 928 
 929 
clusteringtumortypeRp-valueHR(high)Logrankp
valuep(HR) n tumortypename
LAML 0.53.10E-122.40.0160.0254AcuteMyeloidL e ukemia
KIRC 0.39 00.690.0170.017516Kidneyrenalclearcellcarcinoma
KIRP 0.44 8.90E-150.87 0.65 0.65 282Kidneyrenalpapillarycellcarcinoma
LIHC 0.49 01.90.00027 0.00035364Liverhepatocellularcarcinoma
PRAD 0.44 02.1 0.00063 0.00083 492Prostatea d e n ocarcinoma
UCEC 0.45.70E-110.64 0.21 0.22 172UterineCorpusEndometrialCarcinoma
LGG 0.42 01.70.00450.005514BrainL owerGradeGlioma
PCPG 0.52 3.60E-141.2 0.74 0.74 182Pheochromocytomaa n dParaganglioma
THCA 0.59 00.66 0.16 0.16 510Thyroidcarcinoma
ACC 0.67 2.40E-113.30.00350.005576 Adrenocorticalcarcinoma
KICH 0.66 1.70E-099.50.00960.003464KidneyChromophobe
DLBC 0.37 1.00E-020.65 0.56 0.56 46LymphoidNeoplasmDiffuseL argeB-cellLymphoma
THYM 0.21 2.20E-021.5 0.37 0.37 119Thymoma
GBM 0.13 9.30E-020.98 0.86 0.9 162Glioblastomamultiforme
UVM 0.04 7.30E-0130.0250.03378UvealMelanoma
PAAD 0.41 1.70E-081.3 0.21 0.22 178Pancreaticadenocarcinoma
ESCA 0.31 2.30E-051 0.99 1 182Esophagealcarcinoma
SKCM 0.44 0.00E+001.40.0270.028458SkinCutaneousMelanoma
OV 0.17 3.70E-040.85 0.18 0.19 424Ovarianserousc y stadenocarcinoma
STAD 0.35 3.00E-130.82 0.21 0.22 384Stomacha d e n ocarcinoma
CESC 0.21 3.10E-041.1 0.75 0.75 292Cervicalsquamouscellcarcinomaa n de n d ocervicaladenocarcinoma
BLCA 0.31 2.80E-101.1 0.63 0.63 402BladderU rothelialCarcinoma
HNSC 0.22 2.70E-071.1 0.32 0.33 518Head andNeck squamouscellcarcinoma
COAD 0.17 4.90E-030.79 0.33 0.34 270Colon adenocarcinoma
READ 0.37 2.80E-040.74 0.53 0.53 92Rectumadenocarcinoma
BRCA 0.22 1.70E-131.3 0.13 0.13 1070Breastinvasivecarcinoma
LUAD 0.16 6.10E-041.60.00270.003478Lung adenocarcinoma
LUSC 0.26.80E-060.86 0.27 0.27 482Lungsquamouscellcarcinoma
TGCT 0.17 5.40E-021.4 0.34 0.34 136TesticularGermCell Tumors
CHOL -0.163.70E-011.1 0.79 0.8 36Cholangiocarcinoma
MESO 0.05 6.60E-011.5 0.0970.098 82Mesothelioma
SARC 0.12 6.20E-021.3 0.25 0.25 262Sarcoma
UCS 0.03 8.50E-011.2 0.54 0.53 56UterineCarcinosarcoma
^http://gepia2.cancer-pku.cn/#index
DataextractedfromtheGEPIA2webserver^
*b etweenDXH30 and14mitoribosomaltranscriptsthatared erivedfromthe intersectionofTranslationEfficiencydata,LeadingEdge insignificanttermsinGSEA
and DH30eCLIPdatai nENCODE:MRPL1,MRPL12,MRPL3,MRPL30,MRPL35,MRPL37,MRPL4,MRPL41,MRPL49,MRPL51,MRPS15,MRPS24,MRPS22,
MRPL11
nreferstothetotalnumberofsamples.Thesew eresplitatmedianfortheK-Manalysis.
Numberin italicsindicatetheDFSinstead ofOSdataw asused.
Cluster1
Cluster2
OutcomeExpression
Correlation*
050100150
0.00.20.40.60.81.0
Overall Survival
Months
Percent survival
Low1 5 - g e n es i g n a t u r eHigh 15-gene signatureLogrank p=0.0035HR(high)=3.3p(HR)=0.0055
n(high)=38
n(low)=38
020406080100120
0.00.20.40.60.81.0
Overall Survival
Months
Percent survival
Low1 5 - g e n es i g n a t u r eHigh15-gene signatureLogrank p=0.00027HR(high)=1.9p(HR)=0.00035
n(high)=182
n(low)=182
●
● ●
●●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●●
●●
●●
●●
●
●
●
● ●
●
●
●
●
●
●
●
●
●
●
●
●
●●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
2.22.42.62.8
23456
log2(14 Signatures TPM)
log2(DHX30 TPM)
p−value = 2.4e−11R=0 . 6 7
Gene expression correlation
●●●●
●
●
●
●
● ●
●
●
●
●●
●
●
●
●
●
●
●
●
●
●
●
●● ●
●●●
●
●
●
●
●
●
●●
●
●●
●
●●
●
●
●
●
●
●
●
●
●
●●
●●
●
● ●
●
●●
●●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●●●
●
●
●●
● ●
●
●
●●
●
●
●
●
●
●
●
●
●
●
●
●●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●●
●
●
●
●●
●
●
●
●
●
●
●
●
●
●
●
●●
●
●
●
●
●
●
●
●
●●
●
●
● ●
●
●●
●
●
●
●
●
●
●
●
●●
●
●
●● ●
●
●
●
●
●
●
●
●●
●
●
●
●
●
●
●●
●
●
●
●
●
●
●
●
●
● ●
●
●
●
●●
●
●
●●
●
●
●
●
●
●
●
●
●
●
●
●
●●
●
●
●
●
●
●
●
●
●
●
●
● ●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●●●●
●
●
●
●
●
●
●
●
●●
●
●
●
●
●
●
●
●
●
●
●●
●
●
●
●●
●●
●●
●
●●
●●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
● ● ● ●
●
●●
●
●
●
●
●
●
● ● ●
●
●
●
●
●
●
●
●
●● ●
●●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
2.62.72.82.9
3.03.54.04.55.05.56.0
log2(14 Signatures TPM)
log2(DHX30 TPM)
p−value = 0R=0 . 4 9
Gene expression correlation
ACC
LIHC
preprint (which was not certified by peer review) is the author/funder. All rights reserved. No reuse allowed without permission. 
The copyright holder for thisthis version posted December 10, 2020. ; https://doi.org/10.1101/2020.07.13.196709doi: bioRxiv preprint 