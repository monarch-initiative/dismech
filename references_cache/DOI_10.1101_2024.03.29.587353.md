---
reference_id: DOI:10.1101/2024.03.29.587353
title: Neurofilament accumulation disrupts autophagy in giant axonal neuropathy
authors:
- Jean-Michel Paumier
- James Zewe
- Melissa R Pergande
- Meghana Venkatesan
- Eitan Israeli
- Chiranjit Panja
- Natasha Snider
- Jeffrey Savas
- Puneet Opal
year: '2024'
doi: 10.1101/2024.03.29.587353
content_type: full_text_pdf
is_preprint: true
peer_review_status: preprint
full_text_attempted: true
full_text_provider: epmc_preprint
full_text_url: "https://www.biorxiv.org/content/biorxiv/early/2024/03/31/2024.03.29.587353.full.pdf"
oa_status: green
local_pdf_path: files/DOI_10.1101_2024.03.29.587353.pdf
---

# Neurofilament accumulation disrupts autophagy in giant axonal neuropathy
**Authors:** Jean-Michel Paumier, James Zewe, Melissa R Pergande, Meghana Venkatesan, Eitan Israeli, Chiranjit Panja, Natasha Snider, Jeffrey Savas, Puneet Opal
**DOI:** [10.1101/2024.03.29.587353](https://doi.org/10.1101/2024.03.29.587353)

## Content

ABSTRACT
Neurofilament accumulation is a marker of several neurodegenerative diseases, but it is the primary pathology in Giant Axonal Neuropathy (GAN). This childhood onset autosomal recessive disease is caused by loss-of-function mutations in gigaxonin, the E3 adaptor protein that is essential for neurofilament degradation. Using a combination of genetic and RNA interference (RNAi) approaches, we found that dorsal root ganglia from mice lacking gigaxonin have impaired autophagy and lysosomal degradation through two mechanisms. First, neurofilament accumulations interfere with the distribution of autophagic organelles, impairing their maturation and fusion with lysosomes. Second, the accumulations sequester the chaperone 14-3-3, a protein responsible for the localization of the transcription factor EB (TFEB), a key regulator of autophagy. This dual disruption of autophagy likely contributes to the pathogenesis of other neurodegenerative diseases with neurofilament accumulations.

1 
Neurofilament accumulation disrupts autophagy in giant axonal neuropathy 1 
2 
Jean-Michel Paumier1, James Zewe1, Melissa R Pergande1, Meghana Venkatesan1, Eitan 3 
Israeli1,#, Chiranjit Panja1, Natasha Snider2, Jeffrey Savas1 and Puneet Opal1,3 * 4 
5 
1Davee Department of Neurology, Feinberg School of Medicine, Northwestern University, 6 
Chicago, Illinois, USA. 7 
2 Dept. of Cell Biology and Physiology, School of Medicine, University of North Carolina at 8 
Chapel Hill, North Carolina, USA. 9 
3Department of Cell and Molecular Biology, Northwestern University, Chicago, Illinois, USA. 10 
# Present Address: The Barry Skolnick Biosafety Level 3 Unit, Faculty of Medicine, The Hebrew 11 
University-Hadassah Medical School, Jerusalem, Israel. 12 
Address correspondence to: 13 
* Puneet Opal, Davee Department of Neurology, and Department of Cell and Molecular Biology,14 
Northwestern University Feinberg School of Medicine, Chicago, IL 60611 15 
Tel. 312-503-4699; Fax 312-503-0879; E-mail: p-opal@northwestern.edu 16 
17 
18 
Running title: Neurofilament accumulation hinders autophagy. 19 
20 
21 
Key words: giant axonal neuropathy, gigaxonin, neurofilament, lysosomes, Cul3-based E3 22 
ligase, ubiquitin, SILAC, mass spectrometry, proteomics 23 
24 
25 
26 
.CC-BY-ND 4.0 International licenseavailable under a 
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made 
The copyright holder for this preprintthis version posted March 31, 2024. ; https://doi.org/10.1101/2024.03.29.587353doi: bioRxiv preprint 

2 
ABSTRACT 27 
28 
Neurofilament accumulation is a marker of several neurodegenerative diseases, but it is the 29 
primary pathology in Giant Axonal Neuropathy (GAN). This childhood onset autosomal 30 
recessive disease is caused by loss-of-function mutations in gigaxonin, the E3 adaptor protein 31 
that is essential for neurofilament degradation. Using a combination of genetic and RNA 32 
interference (RNAi) approaches, we found that dorsal root ganglia from mice lacking gigaxonin 33 
have impaired autophagy and lysosomal degradation through two mechanisms. First, 34 
neurofilament accumulations interfere with the distribution of autophagic organelles, impairing 35 
their maturation and fusion with lysosomes. Second, the accumulations sequester the 36 
chaperone 14-3-3, a protein responsible for the localization of the transcription factor EB 37 
(TFEB), a key regulator of autophagy. This dual disruption of autophagy likely contributes to the 38 
pathogenesis of other neurodegenerative diseases with neurofilament accumulations. 39 
40 
41 
42 
43 
44 
45 
46 
47 
48 
49 
50 
51 
52 
.CC-BY-ND 4.0 International licenseavailable under a 
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made 
The copyright holder for this preprintthis version posted March 31, 2024. ; https://doi.org/10.1101/2024.03.29.587353doi: bioRxiv preprint 

3 
INTRODUCTION 53 
54 
Giant ax onal neuropathy (GAN) affects virtually every facet of the peripheral and central 55 
nervous systems (1, 2). Patients initially present with weakness, wasting, and sensory deficits in 56 
a glove and stocking distribution. As the disease progresses, patients suffer from cognitive 57 
decline, cranial nerve dysfunction, seizures, spasticity, and cerebellar incoordination. GAN has 58 
no treatment, and most patients do not live beyond the third decade of life.  This distal-to-59 
proximal pattern of deterioration reflects the physical impediment caused by mislocalization and 60 
dysfunction of certain cytoskeletal proteins, which manifests first in those neurons with the 61 
longest axons.  62 
GAN is caused by biallelic loss-of-f unction mutations of the GAN gene (1, 3), which 63 
encodes gigaxonin, a member of the BTB (Bric-a-brac, Tramtrack and Broad)-Kelch family of E3 64 
ligase adaptors that recruit substrates for ubiquitin-mediated proteasomal degradation (4). The 65 
N-terminal BTB domain binds Cullin3, which serves as a bridge to the rest of the ubiquitination66 
machinery (5); the C terminal Kelch domain binds select substrates. The best characterized 67 
GAN substrates are several intermediate filament proteins (IFs), which belong to the larger 68 
family of cytoskeletal proteins (6-8). IFs are so named because their 10 nm diameter places 69 
them intermediate between the sizes of the two other major cytoskeletal proteins, actin and 70 
microtubules (9). They are classified into six major types (I-VI) based on their primary structure 71 
and tissue of expression (9, 10). All IFs share a tripartite structure, including variable globular N- 72 
and C-terminal domains and a central conserved rod domain. It is this central rod domain to 73 
which gigaxonin binds. 74 
Neurons have the most complex repertoire of IFs of any cell type, and they bear the brunt 75 
of GAN pathology. All neurons express three of the type IV proteins: neurofilament triplet 76 
proteins neurofilament heavy (NFH), middle (NFM), and light (NFL), so named based on their 77 
molecular weights. Some neurons also express alpha internexin (a type IV IF), while yet others, 78 
.CC-BY-ND 4.0 International licenseavailable under a 
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made 
The copyright holder for this preprintthis version posted March 31, 2024. ; https://doi.org/10.1101/2024.03.29.587353doi: bioRxiv preprint 

4 
particularly those in the peripheral nervous system, express peripherin, a type III IF (11). The 79 
highly polarized morphology of neurons creates special metabolic and cytoskeletal demands. 80 
Neurons from the spinal cord, for instance, send long axons to skin and muscle at vast 81 
distances from the perikaryon. When neurofilament degradation is stalled, neurofilament 82 
homeostasis is dysregulated, compromising the mechanical properties, and signaling events 83 
that they regulate (11, 12). In GAN, neurofilaments accumulate throughout the cytoplasmic 84 
space but also in discrete foci that are remarkably stable (6). Recent research using 85 
photoactivatable IFs suggests that individual filaments cannot escape from these IF bundles 86 
because of a disruption in their kinesin-based transport along microtubules (13). 87 
We have been interested in the effects of NF accumulation downstream from the obvious 88 
mechanical obstacles because subcellular localization and transport are crucial for many 89 
cellular functions.  Indeed, it has remained unclear whether other dysregulated proteins are 90 
involved in GAN pathogenesis. Previously, we found that NF accumulations interfere with 91 
mitochondrial movement, thereby impairing mitochondrial function (6). Here we report that NF 92 
accumulations also alter the spatial distribution of lysosomes, which impedes autophagic 93 
processes that are spatially orchestrated in neurons (normally, substrates are engulfed by 94 
autophagic vesicles more distally, then are transported retrogradely from the neurites to the 95 
soma, where they are delivered to the lysosomes for degradation) (14). We also show that the 96 
NF foci sequester 14-3-3 proteins, a family of chaperone proteins known to bind IFs, along with 97 
TFEB (the master transcriptional regulator transcription factor EB), thereby preventing TFEB 98 
from shuttling to the nucleus to perform its transcriptional functions. The result is a progressive 99 
loss of quality control of both proteins and organelles, causing cellular deterioration. 100 
101 
102 
103 
104 
.CC-BY-ND 4.0 International licenseavailable under a 
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made 
The copyright holder for this preprintthis version posted March 31, 2024. ; https://doi.org/10.1101/2024.03.29.587353doi: bioRxiv preprint 

5 
RESULTS 105 
106 
Proteomic analysis of mouse dorsal root ganglia with gigaxonin silenced 107 
GAN nul l mice recapitulate the neurofilament aggregates in neurons and the IF aggregates 108 
in other cell types, but because of their small size, they do not manifest overt signs of the 109 
disease until they are very old (6, 15-17). We therefore developed a primary neuronal culture 110 
model using dorsal root ganglia (DRG) neurons (6), which are affected early in the disease 111 
course and display severe neuropathology. DRG neurons isolated from GAN null mice 112 
demonstrate progressive neurofilament accumulation starting from as early as two days in vitro, 113 
both in the cell soma and neurites (Fig 1A). The GAN phenotype is equally well reproduced in 114 
wild-type neurons using small hairpin (sh) RNA based RNAi to reduce gigaxonin expression. 115 
The degree of knockdown achieved is approximately 90% (6). Neurons lacking gigaxonin 116 
degenerate, as evidenced by axonal fragmentation after an additional 8-9 days in culture (Fig 117 
1B). 118 
To gain insight into t he molecular consequences of loss of gigaxonin function, we 119 
performed proteomics with stable isotope labeling using amino acids in cell culture (SILAC) (18). 120 
We quantified 3,507 proteins in DRG cultures (shSCR) and gigaxonin-knockdown cells (shGAN) 121 
under the same experimental conditions (Fig 2A). Of these, 149 proteins had significantly 122 
altered fold change with a false discovery rate (FDR) adjusted with a p value of <0.05 (62 123 
elevated and 87 reduced; see Table S1). As expected, the IF proteins (NFL, NFM, and 124 
peripherin) were among those that were most significantly elevated. 125 
Ingenuity Pathway Analysis (IPA) identified altered biological functions in GAN-s ilenced 126 
DRG cultures (Fig 2B). Several signaling pathways were altered, but PPARa/RXRa, which 127 
regulates cell growth, differentiation, and metabolism, was the only pathway that was 128 
hyperactivated. Several other signaling pathways were downregulated. Interestingly, 129 
phagosome formation and maturation, two key aspects of autophagy (19), were 130 
.CC-BY-ND 4.0 International licenseavailable under a 
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made 
The copyright holder for this preprintthis version posted March 31, 2024. ; https://doi.org/10.1101/2024.03.29.587353doi: bioRxiv preprint 

6 
downregulated, along with IL-7 signaling (which upregulates the expression of anti-apoptotic 131 
genes) and insulin signaling (which inhibits autophagy), which were strongly suppressed. The 132 
overall impression is of a very dysregulated autophagic system. For example, FYN, which is 133 
known to play a role in autophagy by AMPK phosphorylation (19), was strongly downregulated 134 
(Fig 1C), as were PIK3C2A, whose knockdown has been described to decrease autophagy 135 
and the maturation of endocytic vesicles (21); and SOS1, whose deletion has been related to 136 
accumulation of phagosomes and lysosomal bodies (31). ITGA7, which participates in 137 
phagocytosis (30), and WASF2, which is involved in autophagosome and trafficking to 138 
lysosome in human immune cells (24), were moderately upregulated compared to controls. In 139 
the phagosome maturation category (Fig 1D), we had upregulation of cathepsin B (CTSB), 140 
whose deletion impairs autophagy and lysosomal recycling (32), and Syntaxin 1A (STX1A), 141 
which regulates vesicle fusion and trafficking (26); among the downregulated proteins were 142 
cathepsin H (CTSH) (33), which is also involved in vesicle fusion and trafficking, and VPS33B, 143 
which is involved in endosomal recycling and late endosomal-lysosomal fusion events (27, 34). 144 
These results are supported by a recent publication describing the role of gigaxonin in 145 
autophagosome production through Atg16L1 turnover regulation (35).   146 
147 
Neurofilament aggregates alter the spatial distribution, abundance, and morphology of 148 
autophagic organelles 149 
The autophagi c process involves the formation of vesicles around substrates; these 150 
vesicles mature into autophagosomes that fuse with lysosomes, where the substrate is 151 
ultimately degraded (20). These steps require the free movement of autophagic organelles, a 152 
process that we hypothesized would be particularly compromised in neurons by the space-153 
occupying neurofilament aggregates. Therefore, we stained cells for LC3, a small polypeptide 154 
that recruits substrates and is a specific marker for autophagosomes (21). Neurofilaments were 155 
delineated by staining for NFL, a protein that forms the backbone of the neurofilament 156 
.CC-BY-ND 4.0 International licenseavailable under a 
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made 
The copyright holder for this preprintthis version posted March 31, 2024. ; https://doi.org/10.1101/2024.03.29.587353doi: bioRxiv preprint 

7 
heteropolymer (12). In GAN knockout DRG neurons, the autophagosomes were not uniformly 157 
distributed throughout the cytoplasm, as they would normally be, but were now more abundant 158 
at the perimeters of the aggregates (Fig 3A). 159 
Next, we det ermined the location of lysosomes using immunofluorescence microscopy. 160 
Neurofilaments were visualized as before by staining for NFL, while lysosomes were visualized 161 
by staining for LAMP-1, which constitutes approximately 50% of the lysosomal membrane (12, 162 
22) (Fig. 3B). Neurons showed either exclusion of LAMP-1 staining from neurofilament163 
aggregates, or they showed a colocalization. We surmised that these two patterns reflect the 164 
status of different lysosomal populations or their membranous fragments. 165 
To confirm this observation, we  stained additional lysosomal components, both across the 166 
membrane and within the lumen. For the former, we evaluated the distribution of mucolipin 1, a 167 
calcium channel protein and member of the transient receptor potential cation channel mucolipin 168 
subfamily (23, 24), and vacuolar ATPase, which is a protein essential for lysosomal acidification 169 
that pumps protons into  the lumen (25, 26). Both of these co-localized with neurofilament 170 
aggregates (Fig 4A).  To study intraluminal proteins, we stained  for two lysosomal proteases: 171 
cathepsin B and cathepsin D (27). Cathepsin B was typically sequestered in aggregates, while 172 
cathepsin D was typically excluded from them, reminiscent of the two staining patterns of 173 
LAMP-1 (Fig 4B). 174 
We next t racked intact lysosomes in living DRG neurons with lysotracker, a cell-permeable 175 
dye that stains the acidic compartment of lysosomes (28). Since we wished to correlate 176 
lysosomal distribution with neurofilament aggregates, we also infected cells with a lentivirus 177 
expressing GFP-tagged NFL. Lysotracker staining tended to be absent from regions with 178 
aggregates, suggesting that intact lysosomes are spatially excluded from neurofilament 179 
accumulations (Fig 5A). The amount and intensity of lysosomal staining with lysotracker was 180 
greater in GAN DRG cultures (Fig 5A, B), likely because the lysosomes also tended to be larger 181 
(Fig 5C). 182 
.CC-BY-ND 4.0 International licenseavailable under a 
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made 
The copyright holder for this preprintthis version posted March 31, 2024. ; https://doi.org/10.1101/2024.03.29.587353doi: bioRxiv preprint 

8 
Transmission electron microscopy revealed a g reater abundance of autophagic organelles 183 
at different stages of maturation in GAN DRGs: these included large autophagic vacuoles, 184 
multilamellar bodies, and immature autophagosomes (Fig 6). The electron-dense lysosomes 185 
tended to decorate the perimeter of the aggregates. These data demonstrate that NF 186 
aggregates influence the distribution of autophagic organelles. 187 
188 
Lysosomal acidity and autophagic flux are dysregulated in GAN 189 
To addres s lysosomal function, we evaluated lysosomal pH, which is crucial to the ability 190 
to degrade substrates. We used lysosensor, a sensitive dye designed specifically for this 191 
purpose (20). GAN-silenced DRG cultures displayed a significant reduction in lysosensor signal 192 
intensity within lysotracker defined compartments (Fig 7A). These results suggest that 193 
lysosomes in GAN are defective at maintaining a robust acidic internal environment, which 194 
would translate into a reduction in autophagic flux. To test this possibility, we performed live-cell 195 
imaging using an mRFP-GFP tandem-tagged LC3. This protein incorporates into the membrane 196 
of autophagic vacuoles, exhibiting a punctate signal within cells. It fluoresces from fluorophores 197 
as autophagosomes mature before fusing with the lysosome; after fusion, the GFP fluorescence 198 
(which is pH-sensitive) is lost in the acidic lysosomal milieu, while the mRFP fluorescence (not 199 
pH-sensitive) persists until LC3 is fully degraded, providing a quantifiable readout for fusion 200 
delay or lysosomal dysfunction (21). GAN-silenced neurons showed a significantly greater GFP 201 
fluorescence signal within RFP-positive vehicles, suggesting either a greater quantity of 202 
autophagosomes yet to fuse with lysosomes or a loss of lysosomal acidity (Fig 7B). These 203 
autophagic organelles were larger in GAN DRGs than in controls. 204 
To further assess t he functional status of autophagy, we evaluated the levels of p62 (also 205 
known as SQSTM1), an autophagic receptor that recruits cargo to be degraded and is itself 206 
degraded by autophagy (21). By both immunostaining and western blotting, p62 levels were 207 
.CC-BY-ND 4.0 International licenseavailable under a 
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made 
The copyright holder for this preprintthis version posted March 31, 2024. ; https://doi.org/10.1101/2024.03.29.587353doi: bioRxiv preprint 

9 
significantly greater in GAN-silenced DRGs, consistent with the inability of lysosomes to 208 
degrade substrates (Fig 7C, D). 209 
210 
TFEB is sequestered in neurofilament aggregates in GAN 211 
Autophagy is  dependent on the activity of the transcription factor TFEB (29-31), whose 212 
activity is highly dependent on its subcellular location. Under conditions of cellular stress, TFEB 213 
translocate to the nucleus and drive the CLEAR (Coordinated Lysosomal Expression and 214 
Regulation) network of genes responsible for autophagy and lysosomal biogenesis (32). When 215 
phosphorylated, TFEB is bound to the cytoplasmic chaperone 14-3-3 proteins, a family of acidic 216 
phosphoproteins (28-33 kDa in size) that serve as adapters regulating a number of signaling 217 
pathways. Intriguingly, IFs, including neurofilaments, are known to recruit these proteins in a 218 
phosphorylation-dependent manner (33). For these reasons we decided to look for both TFEB 219 
and 14-3-3 localization in GAN silenced DRG neurons.  220 
After co-staining TFEB and NFL, we found that TFEB was enriched in cytoplasmic 221 
neurofilament aggregates when GAN was silenced (Fig 8A, B). Moreover, we found 222 
significantly less TFEB in the nucleus of GAN null neurons (~33% less than wild type). We also 223 
found that 14-3-3 proteins co-aggregate with NFL in GAN-silenced DRGs (Fig 8C). 224 
225 
226
 
227 
228 
229 
230 
231 
232 
233 
.CC-BY-ND 4.0 International licenseavailable under a 
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made 
The copyright holder for this preprintthis version posted March 31, 2024. ; https://doi.org/10.1101/2024.03.29.587353doi: bioRxiv preprint 

10 
DISCUSSION 234 
235 
Neurofilaments accumulate in s everal neurodegenerative syndromes—Alzheimer disease, 236 
Parkinson disease, polyglutamine diseases, and amyotrophic lateral sclerosis (ALS), to name 237 
just a few (12). Yet the role of neurofilament aggregation in disease has been largely overlooked 238 
in favor of disease-specific features. Rare diseases, such as GAN, provides a unique 239 
opportunity to understand the effects of neurofilament aggregation (12). Here we show that 240 
neurofilament accumulations in GAN impair autophagy by disrupting the spatial distribution and 241 
transport of autophagic organelles and the master transcription factor TFEB, which is required 242 
for lysosome biogenesis and autophagic flux. 243 
The first hint t hat impaired autophagy contributes to the pathogenesis of human 244 
degenerative syndromes came from genetically engineered mice. Mice lacking ATG5 or ATG7 245 
(autophagy-related 5 or 7, respectively) in their nervous system, for example, demonstrate 246 
progressive neurological deficits and protein aggregation. Patients have also been described 247 
with mutations in genes directly linked with autophagic processes (34, 35). These diseases are 248 
rare, but there has been a growing appreciation for the role of autophagy in the common 249 
neurodegenerative proteopathies such as Parkinson disease. In GAN, autophagy’s role is more 250 
complex: clearance of disease-specific proteins that resist ubiquitin-proteasome degradation is 251 
attempted via autophagy, while autophagy itself is compromised by a range of cellular events 252 
triggered by the misfolded proteins themselves in pathways yet to be completely elucidated (34, 253 
36, 37). In the normal physiological state, neurofilaments undergo autophagic clearance, and 254 
the autophagic vesicles surrounding NF aggregates in GAN suggest that autophagy might even 255 
be recruited as a salvage pathway to clear neurofilaments (38). But as we show here, 256 
neurofilament accumulations themselves hinder autophagy. It is intriguing that in many of the 257 
common proteopathies, disease proteins such as alpha synuclein, mutant Huntingtin, and 258 
TDP43 are surrounded by neurofilament caps in structures called aggresomes. It is tempting to 259 
.CC-BY-ND 4.0 International licenseavailable under a 
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made 
The copyright holder for this preprintthis version posted March 31, 2024. ; https://doi.org/10.1101/2024.03.29.587353doi: bioRxiv preprint 

11 
speculate that the neurofilament caps contribute to the autophagic impairments in these 260 
disorders as well. Gigaxonin has recently been shown to degrade ATG16L, a protein involved in 261 
autophagosome maturation, and thus might play an independent role as an autophagy regulator 262 
(39). In DRGs we did not observe accumulation of this protein, but we cannot exclude that such 263 
a mechanism might compound the neurofilament-induced autophagic deficits that we observe.  264 
The mec hanisms by which neurofilaments interfere with autophagy—altering the 265 
localization of autophagic vesicles and sequestering TFEB—are in essence distortions of the 266 
normal role of neurofilaments to serve as a docking platform. When aggregated, neurofilaments 267 
have very distinct biophysical properties from well-distributed wild-type polymers: they are tightly 268 
packed, display a lack of dynamic behavior, and even appear to undergo solid-to-liquid phase 269 
transitions (11, 40). Phosphorylation could further affect these properties (11). The 270 
mislocalization of autophagic organelles is reminiscent of what has been previously observed 271 
with mitochondria in GAN (6). It will now be important to determine the full complement of 272 
proteins and organelles affected by neurofilament aggregates in the disease state. Abnormal 273 
interactions are likely to be further compounded by inter-organellar co-dependence, 274 
exacerbating the pathology. For instance, mitochondrial deficits could limit cellular energy 275 
supplies, impairing lysosomal acidification, while abnormal autophagy could affect mitochondrial 276 
quality control through mitophagy. Mitochondrial and lysosomal contact sites could serve as 277 
additional points of cross-talk between these two dynamic organelles (41). Future studies will be 278 
required to tease out the complex interactions between signaling pathways, organelle 279 
dysfunction, and neurofilament aggregation to determine strategies to best treat GAN and other 280 
neurofilament proteopathies. 281 
282 
283 
284 
285 
.CC-BY-ND 4.0 International licenseavailable under a 
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made 
The copyright holder for this preprintthis version posted March 31, 2024. ; https://doi.org/10.1101/2024.03.29.587353doi: bioRxiv preprint 

12 
MATERIAL AND METHODS 286 
Mice 287 
The genera tion of GAN null mice has been previously described (15). The animals were 288 
housed in a specific pathogen free facility at Northwestern University, and experiments were 289 
performed in accordance with the National Institutes of Health’s Guide for the Care and Use of 290 
Laboratory Animals (with protocols approved by Northwestern University’s Institutional Animal 291 
Care and Use Committee).  292 
293 
Dorsal root ganglia cultures 294 
DRG neurons were isolated from post-na tal day 5 mice using a published protocol with 295 
few modifications (6). Briefly, mouse DRG were dissected from their paraspinal location; they 296 
were then placed in cold dissection medium in  a microcentrifuge tube (97.5% HBSS Ca2+ and 297 
Mg2+ free, 1X sodium pyruvate, 0.1% glucose, 10 mM HEPES), pelleted by a 10 s centrifugation 298 
pulse on a table-top centrifuge, and then washed in the same dissection media and finally 299 
harvested by pelleting. Washed ganglia were dissociated at 37oC for 10 min, first in 1 mL of 300 
neurobasal media (Gibco) containing 35 U papain/mL followed by a centrifugation pulse and 301 
then in 1 mL of hibernate medium containing 4 mg/mL collagenase type II and 4.6 mg/mL 302 
dispase II. This was followed by another pulsed centrifugation and wash. The resuspended cells 303 
were triturated by pipetting through a P1000 tip in plating medium (Neurobasal (Gibco) 304 
containing penicillin-streptomycin 100 U/mL-100 µg/mL and 1X GlutaMax). The dissociated cells 305 
were separated from any clumps by filtering them through a 100-micron cell strainer (Corning). 306 
They were then harvested for plating by a low-speed centrifugation for 5 min at 230 x g. 307 
The cells were then cultured on plating medium in 3 5 mm microwells with a 14 mm glass 308 
bottom (MatTek). Each mouse provided sufficient DRGs to plate 5 dishes at approximately 309 
80,000 cells per dish. After allowing the plated cells to settle, the plating media was gently 310 
aspirated and replaced with 2 mL of pre-warmed maintenance medium (plating media 311 
.CC-BY-ND 4.0 International licenseavailable under a 
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made 
The copyright holder for this preprintthis version posted March 31, 2024. ; https://doi.org/10.1101/2024.03.29.587353doi: bioRxiv preprint 

   
 
   
 
13 
supplemented with 1% nerve growth factor). Primary neurons were maintained at 37 °C in a 312 
humidified 5% CO2 atmosphere with addition of 0.5 mL of fresh maintenance media every 3 313 
days. On day 3 in vitro, DRG cultures were transduced with lentivirus encoding shRNA against 314 
gigaxonin (shGAN) or a scrambled control (shSCR) using 10 µL of concentrated lentivirus per 315 
microwell, prepared as described below.  316 
 317 
Lentiviral constructs  318 
 EGFP derived from pEGFP-C1 (Clontech) was cloned in-frame to the N-terminal domain 319 
of the mouse NFL gene (derived from pmNFL; Addgene ID 83127) using the NEBuilder HiFi 320 
DNA Assembly cloning kit (New England Biolabs E5520S). The fusion construct was then 321 
amplified by PCR and inserted into the multiple-cloning site of the lentiviral vector pLEX using 322 
the same NEBuilder cloning kit to generate pLEX-mNFL-GFP. Constructs were validated with 323 
Sanger sequencing using primers to sequence over insertion sites.  324 
 A utophagic flux was measured by an mRFP-GFP-LC3 construct as described previously 325 
(42). Lentiviruses expressing shGAN and shSCR have been described previously and were 326 
obtained from SIGMA MISSION shRNA systems: shGAN (MISSION® vector TRC # 327 
TRCN0000251146, Sigma) and shSCR (#SHC002, Sigma).  328 
 329 
Lentivirus production and transduction 330 
 HEK293T cells were used to produce all the lentiviruses. HEK293T cells were plated in 331 
T75 flasks at a density of 60-80% in a culture medium of high-glucose DMEM (Gibco 11965092) 332 
supplemented with 10% fetal bovine serum (Gibco 16140089) and penicillin/streptomycin (100 333 
U/mL, 100 µg/mL, Gibco 15140122). The lentiviral construct of interest was co-transfected with 334 
the packaging constructs pCMV-VSV-G and pCMV Gag/Pol at a ratio of 10 µg: 4 µg: 6 µg 335 
respectively using Lipofectamine 2000 (60 µL, Invitrogen 11668027). After 4 h, the growth 336 
media of the transfected HEK293T cells was replaced with 10 mL of fresh complete DMEM. 337 
.CC-BY-ND 4.0 International licenseavailable under a 
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made 
The copyright holder for this preprintthis version posted March 31, 2024. ; https://doi.org/10.1101/2024.03.29.587353doi: bioRxiv preprint 

14 
Media was collected 48 h after transfection and clarified by syringe filtration through a 0.45 µm 338 
polyvinylidene difluoride membrane (Millex-HV) before concentrating the virus with a Lenti-X 339 
concentrator (Clontech 631231). The concentrated virus was resuspended in PBS and aliquoted 340 
into single-use tubes stored at -80 °C. The concentrated lentivirus in a volume of 10 µL was 341 
delivered to DRG cultures cultured on glass-bottomed microwells. Each new lot of lentiviruses 342 
was first tested for at least 50% transduction efficacy in wild-type DRG cultures before 343 
experimental use (as measured by fluorescence of tagged constructs or knockdown of shRNA 344 
constructs as determined by qPCR). 345 
346 
SILAC sample preparation and data analysis 347 
DRG neuron s from p3 wild-type mice were isolated and plated as previously described (6). 348 
In brief, the dissociated neurons were plated on poly-D-lysine coverslips and maintained in 349 
Neurobasal media for 13 days. Gigaxonin was silenced using lentivirus expressing shRNA to 350 
gigaxonin (shGAN) or control (scrambled sequence; shSCR) after 3 days in culture. In total, 8 351 
dishes of DRG neurons were cultured for SILAC analysis where a standard label swapping 352 
approach was carried out. Here, two cultures treated with shSCR and two cultures treated with 353 
shGAN were incubated with media containing heavy isotope-enriched arginine and lysine 354 
(13C15N). In parallel, two cultures treated with shSCR and two cultures treated with shGAN were 355 
incubated with normal culture media. On DIV13, cells were lysed with 1% SDS containing 100 356 
mM Tris-Cl and boiled for 10 min. Protein concentrations were determined via a bicinchoninic 357 
assay (BCA, Pierce). Equal amounts of protein (50 µg) from pairs of heavy and light cultures 358 
were mixed at a 1:1 ratio. An in-solution trypsin digestion of proteins was carried out after 359 
reduction with 5 mM dithiothreitol at 55oC for 15 min and alkylation with 15 mM iodoacetamide 360 
for 20 min at room temperature. The resulting peptides were fractionated via HyperSep Strong 361 
Cation Exchange using 25 mM, 50 mM, 500 mM, 1 M, 2 M, and 4 M KCl, and each fraction was 362 
subsequently desalted by C18 ZipTip and dried in vacuo. Each of the samples was 363 
.CC-BY-ND 4.0 International licenseavailable under a 
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made 
The copyright holder for this preprintthis version posted March 31, 2024. ; https://doi.org/10.1101/2024.03.29.587353doi: bioRxiv preprint 

   
 
   
 
15 
resuspended in 0.1% formic acid and analyzed via nano-electrospray ionization on a Thermo 364 
Orbitrap Fusion mass spectrometer, where auto MS/MS data was acquired in positive ion mode. 365 
Here, solvent A was 0.1% formic acid whereas solvent B was acetonitrile with 0.1% formic acid. 366 
Peptides were resolved using a 60 min linear gradient where a single mass spectrometry 367 
analysis was done for each fraction. Data analysis was performed using the Thermo Proteome 368 
Discoverer software. "Light" samples were Lys0, Arg0 and "heavy" samples were Lys8, Arg10. 369 
The database search included fixed modifications, such as carbaminomidomethyl (C), and 370 
variable modifications such as oxidation (M) and deamination (N,Q). Precursor quantification of 371 
pairwise ratios (matched median peptide abundance) and t-test analysis using no missing 372 
channels were used to calculate relative quantification ratios. Significance of shGAN/shSCR 373 
ratios was determined at a threshold of p < 0.05 with Benjamini-Hochberg correction applied to 374 
reduce the false discovery rate. Pathway and biofunction analysis of altered proteins were 375 
performed in Ingenuity Pathway Analysis.  376 
 377 
Immunocytochemistry 378 
 DRG neurons on glass-bottomed microwells were fixed in -20 °C methanol for 7 min, a 379 
method which is ideal for fixation of neurofilaments (43). After fixation the cells were incubated 380 
for 1 h with blocking solution (5% normal goat serum in PBS) and then incubated overnight at 4 381 
°C with the relevant primary antibodies diluted in blocking solution. The microwells were then 382 
washed twice with PBS containing 0.05% Tween 20 followed by a similar wash twice with PBS 383 
(each wash 5 min). The cells were then incubated for an hour at room temperature with Alexa 384 
fluorophore-conjugated secondary antibodies and DAPI (1:500 dilution) diluted in blocking 385 
solution (see antibodies table) and washed again as described above. A drop of mounting 386 
media (Prolong Diamond; Life Technologies) was added to the microwell and a coverslip was 387 
placed.  388 
 389 
.CC-BY-ND 4.0 International licenseavailable under a 
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made 
The copyright holder for this preprintthis version posted March 31, 2024. ; https://doi.org/10.1101/2024.03.29.587353doi: bioRxiv preprint 

   
 
   
 
16 
Live imaging of lysosomes and autophagic flux 390 
 The conditioned media of DRG cultures that would be subjected to lysosomal staining was 391 
first removed and kept aside. The cells were then treated with 50 mM lysotracker (Red DND-99; 392 
L7528 Invitrogen) either alone or in combination with 1 µM lysosensor (Green DND-189; L7535 393 
Invitrogen) in plating media for 30 min, after which the media was replaced with the previously 394 
stored media (to avoid lysotracker cytotoxicity). When we wished to visualize neurofilaments, we 395 
also transduced the cells 3 days before treatment with pLEX-mNFL-GFP. To measure 396 
autophagic flux in living cells, we transduced DRG cultures with mRFP-GFP-LC3 lentivirus 3 397 
days prior to imaging. 398 
 399 
Light microscopy   400 
 Resonant scanning confocal microscopy was performed using a Nikon A1R+ platform 401 
equipped with a 100× oil-immersion objective and PerfectFocus focal drift compensation 402 
mechanism with automated XY stage. The green fluorophores were excited using laser lines set 403 
at 488 nm with emission filters set at 525-550 nm; the red fluorophores were excited using a 404 
laser line set at 561 nm with emission filters set at 600-650 nm. The confocal pinhole size was 405 
fixed at 1.2× the size of the Airy disc of the red channel. For live cell microscopy, images were 406 
captured at a single XYZ position every second for 3 min using 8 frame averages to improve the 407 
signal-to-noise ratio. For fixed cell microscopy, images were acquired in Galvano mode. Image 408 
resolution was optimized using the Nyquist criterion by the Nikon Elements software.  409 
 410 
Transmission electronic microscopy 411 
 DRG cultures were fixed in 0.1 M sodium cacodylate buffer (pH 7.3) containing 2% 412 
paraformaldehyde and 2.5% glutaraldehyde. They were then processed and embedded in resin 413 
blocks which were then sectioned, stained, and imaged as previously described (6). 414 
 415 
.CC-BY-ND 4.0 International licenseavailable under a 
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made 
The copyright holder for this preprintthis version posted March 31, 2024. ; https://doi.org/10.1101/2024.03.29.587353doi: bioRxiv preprint 

   
 
   
 
17 
Antibodies 416 
        The following primary antibodies were used:  417 
Neurofilament NFL chicken polyclonal / CPCA-NF-L / Encor  418 
LC3A/B monoclonal / #12741/ Cell Signaling Technology 419 
LAMP-1 rabbit polyclonal / ab24170 / abcam 420 
GAPDH rabbit monoclonal / #2118 / Cell Signaling Technology 421 
TFEB rabbit polyclonal / SAB2108453 / Labome 422 
TFEB rabbit polyclonal / A303-773A / Bethyl Laboratories 423 
14-3-3 rabbit polyclonal / #51-0700 / Cell Signaling Technology 424 
Cathepsin B mouse monoclonal / ab58802 / abcam 425 
Cathepsin D mouse monoclonal / ab75852 / abcam 426 
 427 
Western blotting 428 
 The DRG media of each microwell culture was aspirated and replaced with 70 µL RIPA 429 
buffer containing 1% protease inhibitor. The cells were gently scraped with the pipette tip and 430 
the lysates were collected in microcentrifuge tubes. To ensure adequate lysates for western 431 
blotting, typically 5 dishes of each experimental sample were pooled. Protein concentrations 432 
were determined using the Pierce BCA assay (Thermo Fisher Scientific). Protein extracts were 433 
prepared with Laemmli buffer, warmed at 95 °C for 5 min, and separated on gradient SDS-434 
polyacrylamide gels by electrophoresis. The proteins were then electrophoretically transferred to 435 
nitrocellulose membranes. Membranes were blocked at room temperature for 1 h using 5% 436 
blocking solution and blotted sequentially with the appropriate primary antibody (overnight 4 °C) 437 
and the horseradish peroxidase-conjugated secondary antibodies (2 h RT). Between primary 438 
and secondary antibody incubation, membranes were washed 3x10 min with PBS with 0.1%. 439 
Tween 20. Similarly, membranes were washed after secondary antibody incubation before 440 
protein detection using SuperSignal West Pico Chemiluminescence Detection kit (Thermo 441 
.CC-BY-ND 4.0 International licenseavailable under a 
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made 
The copyright holder for this preprintthis version posted March 31, 2024. ; https://doi.org/10.1101/2024.03.29.587353doi: bioRxiv preprint 

18 
Fisher Scientific). Images were acquired with a Bio-Rad Chemidoc XRS+ gel imaging system 442 
and analyzed with ImageJ/Fiji software (National Institutes of Health). Relative protein 443 
quantification was carried out by measuring the area under the curve (AUC) normalized to 444 
values of loading controls (GAPDH) as indicated in the figure legends. 445 
446 
Image analysis 447 
All images were quantified with ImageJ/Fiji software ( NIH). For particle analysis (defining 448 
lysosomal compartments and measuring within specific regions of interest (ROIs)), images were 449 
prepared by applying general background subtraction on independent channels before applying 450 
a trous wavelet transformation (Ihor Smal, A Trous Wavelet Filter) on 3 scales. The output was 451 
then converted to a binary mask and Fiji’s built-in particle analysis feature was used to define 452 
ROIs. These ROIs served as measurements of lysosome number and size within a cell and 453 
were used as bounds for measurements of lysosensor intensity within lysotracker-defined 454 
compartments (intensity was determined using the multi-measure plugin). 455 
456 
Statistics 457 
All values represent the means ± SEM of the number of replicates indicated in the figure 458 
legends. All analyses were performed using GraphPad Prism software. Student's t test was 459 
used to compare two groups, ANOVA was used to compare more than two groups, and 460 
statistical significance was defined as p<0.05. See figures legends for more details. 461 
462 
FUNDING 463 
P.O. r eceives grant support from NINDS (1R01NS127204-01 and R01NS082351-09), the 464 
Giddan foundation, and prior seed funding from Hannah’s Hope Fund.  J.S receives support 465 
from R01AG078796 and R21AG080705. Research reported in this publication was also 466 
.CC-BY-ND 4.0 International licenseavailable under a 
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made 
The copyright holder for this preprintthis version posted March 31, 2024. ; https://doi.org/10.1101/2024.03.29.587353doi: bioRxiv preprint 

19 
supported by the National Institutes of Health's National Center for Advancing Translational 467 
Sciences, Grant Number TL1TR001423 (M.R.P) 468 
469 
ACKNOWLEDGMENTS 470 
We thank Abigail Brown and Morgan Pooler for t heir assistance with mouse husbandry 471 
and genotyping. Morgan Pooler also assisted with preparation of samples for electron 472 
microscopy.  Light and electron microscopy imaging was performed at the Northwestern 473 
University Center for Advanced Microscopy, supported by NCI CCSG P30 CA060553 awarded 474 
to the Robert H. Lurie Comprehensive Cancer Center. 475 
476 
AUTHOR CONTRIBUTIONS 477 
  JMP as sisted by JZ and MV performed most of the cell biological experiments; JMP wrote 478 
the first draft of the manuscript; EI, MRP and JS performed the proteomic experiments and data 479 
analysis; CP and NS helped in the conceptual analysis and writing of the manuscript; PO 480 
supervised the entire work, analyzed and interpreted the data and wrote the manuscript with 481 
input from all the authors. 482 
483 
POTENTIAL CONFLICTS OF INTEREST 484 
 The authors have declared that no conflict of interest exists 485 
486 
DATA AVAILABILITY 487 
  The list of proteins identified in mass spectrometry analysis from Database search is 488 
available in Supplementary Table S1 and S2. Any other data will be made available with request 489 
in accordance with Northwestern University data sharing policy. 490 
491 
492 
.CC-BY-ND 4.0 International licenseavailable under a 
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made 
The copyright holder for this preprintthis version posted March 31, 2024. ; https://doi.org/10.1101/2024.03.29.587353doi: bioRxiv preprint 

20 
REFERENCES 493 
494 
1. Op
al P. In: Adam MP, Mirzaa GM, Pagon RA, Wallace SE, Bean LJH, Gripp KW, et al. eds. 495 
GeneReviews((R)). Seattle (WA); 1993. 496 
2. Johnson-Kerner BL, Roth L, Greene JP, Wichterle H, and Sproule DM. Giant Axonal 497 
Neuropathy: An Updated Perspective on Its Pathology and Pathogenesis. Muscle Nerve. 498 
2014;50(4):467-76. 499 
3. Bomont P, Cavalier L, Blondeau F, Ben Hamida C, Belal S, Tazir M, et al. The gene 500 
encoding gigaxonin, a new member of the cytoskeletal BTB/kelch repeat family, is 501 
mutated in giant axonal neuropathy. Nat Genet. 2000;26(3):370-4. 502 
4. Pintard L, Willems A, and Peter M. Cullin-based ubiquitin ligases: Cul3-BTB complexes 503 
join the family. EMBO J. 2004;23(8):1681-7. 504 
5. Hua Z, and Vierstra RD. The cullin-RING ubiquitin-protein ligases. Annu Rev Plant Biol. 505 
2011;62:299-334. 506 
6. Israeli E, Dryanovski DI, Schumacker PT, Chandel NS, Singer JD, Julien JP, et al. 507 
Intermediate filament aggregates cause mitochondrial dysmotility and increase energy 508 
demands in giant axonal neuropathy. Hum Mol Genet. 2016. 509 
7. Mahammad S, Murthy SN, Didonna A, Grin B, Israeli E, Perrot R, et al. Giant axonal 510 
neuropathy-associated gigaxonin mutations impair intermediate filament protein 511 
degradation. The Journal of clinical investigation. 2013;123(5):1964-75. 512 
8. Opal P, and Goldman RD. Explaining intermediate filament accumulation in giant axonal 513 
neuropathy. Rare Dis. 2013;1:e25378. 514 
.CC-BY-ND 4.0 International licenseavailable under a 
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made 
The copyright holder for this preprintthis version posted March 31, 2024. ; https://doi.org/10.1101/2024.03.29.587353doi: bioRxiv preprint 

   
 
   
 
21 
9. Eriksson JE, Dechat T, Grin B, Helfand B, Mendez M, Pallari HM, et al. Introducing 515 
intermediate filaments: from discovery to disease. The Journal of clinical investigation. 516 
2009;119(7):1763-71. 517 
10. Szeverenyi I, Cassidy AJ, Chung CW, Lee BT, Common JE, Ogg SC, et al. The Human 518 
Intermediate Filament Database: comprehensive information on a gene family involved 519 
in many human diseases. Hum Mutat. 2008;29(3):351-60. 520 
11. Yuan A, Rao MV, Veeranna, and Nixon RA. Neurofilaments and Neurofilament Proteins 521 
in Health and Disease. Cold Spring Harb Perspect Biol. 2017;9(4). 522 
12. Didonna A, and Opal P. The role of neurofilament aggregation in neurodegeneration: 523 
lessons from rare inherited neurological disorders. Mol Neurodegener. 2019;14(1):19. 524 
13. Renganathan B, Zewe JP, Cheng Y, Paumier JM, Kittisopikul M, Ridge KM, et al. 525 
Gigaxonin is required for intermediate filament transport. FASEB J. 2023;37(5):e22886. 526 
14. Maday S, and Holzbaur EL. Autophagosome biogenesis in primary neurons follows an 527 
ordered and spatially regulated pathway. Dev Cell. 2014;30(1):71-85. 528 
15. Dequen F, Bomont P, Gowing G, Cleveland DW, and Julien JP. Modest loss of peripheral 529 
axons, muscle atrophy and formation of brain inclusions in mice with targeted deletion 530 
of gigaxonin exon 1. J Neurochem. 2008;107(1):253-64. 531 
16. Ganay T, Boizot A, Burrer R, Chauvin JP, and Bomont P. Sensory-motor deficits and 532 
neurofilament disorganization in gigaxonin-null mice. Mol Neurodegener. 2011;6:25. 533 
17. Nath B, and Julien JP. A New Mouse Model of Giant Axonal Neuropathy with Overt 534 
Phenotypes and Neurodegeneration Driven by Neurofilament Disorganization. J 535 
Neurosci. 2023;43(22):4174-89. 536 
.CC-BY-ND 4.0 International licenseavailable under a 
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made 
The copyright holder for this preprintthis version posted March 31, 2024. ; https://doi.org/10.1101/2024.03.29.587353doi: bioRxiv preprint 

22 
18. Chen X, Wei S, Ji Y, Guo X, and Yang F. Quantitative proteomics using SILAC: Principles, 537 
applications, and developments. Proteomics. 2015;15(18):3175-92. 538 
19. Mizushima N. Autophagy: process and function. Genes Dev. 2007;21(22):2861-73.539 
20. Mizushima N, and Komatsu M. Autophagy: renovation of cells and tissues. Cell.540 
2011;147(4):728-41. 541 
21. Mizushima N, Yoshimori T, and Levine B. Methods in mammalian autophagy research.542 
Cell. 2010;140(3):313-26. 543 
22. Finkbeiner S. The Autophagy Lysosomal Pathway and Neurodegeneration. Cold Spring544 
Harb Perspect Biol. 2020;12(3). 545 
23. Tedeschi V, Petrozziello T, Sisalli MJ, Boscia F, Canzoniero LMT, and Secondo A. The546 
activation of Mucolipin TRP channel 1 (TRPML1) protects motor neurons from L-BMAA 547 
neurotoxicity by promoting autophagic clearance. Sci Rep. 2019;9(1):10743. 548 
24. Scotto Rosato A, Montefusco S, Soldati C, Di Paola S, Capuozzo A, Monfregola J, et al.549 
TRPML1 links lysosomal calcium to autophagosome biogenesis through the activation of 550 
the CaMKKbeta/VPS34 pathway. Nat Commun. 2019;10(1):5630. 551 
25. Song Q, Meng B, Xu H, and Mao Z. The emerging roles of vacuolar-type ATPase-552 
dependent Lysosomal acidification in neurodegenerative diseases. Transl Neurodegener. 553 
2020;9(1):17. 554 
26. Mauvezin C, Nagy P, Juhasz G, and Neufeld TP. Autophagosome-lysosome fusion is555 
independent of V-ATPase-mediated acidification. Nat Commun. 2015;6:7007. 556 
27. Turk B, Turk D, and Turk V. Lysosomal cysteine proteases: more than scavengers.557 
Biochim Biophys Acta. 2000;1477(1-2):98-111. 558 
.CC-BY-ND 4.0 International licenseavailable under a 
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made 
The copyright holder for this preprintthis version posted March 31, 2024. ; https://doi.org/10.1101/2024.03.29.587353doi: bioRxiv preprint 

23 
28. Chazotte B. Labeling lysosomes in live cells with LysoTracker. Cold Spring Harb Protoc. 559 
2011;2011(2):pdb prot5571.560 
29. Settembre C, Di Malta C, Polito VA, Garcia Arencibia M, Vetrini F, Erdin S, et al. TFEB561 
links autophagy to lysosomal biogenesis. Science. 2011;332(6036):1429-33. 562 
30. Settembre C, Zoncu R, Medina DL, Vetrini F, Erdin S, Erdin S, et al. A lysosome-to-563 
nucleus signalling mechanism senses and regulates the lysosome via mTOR and TFEB. 564 
EMBO J. 2012;31(5):1095-108. 565 
31. Medina DL, Di Paola S, Peluso I, Armani A, De Stefani D, Venditti R, et al. Lysosomal566 
calcium signalling regulates autophagy through calcineurin and TFEB. Nat Cell Biol. 567 
2015;17(3):288-99. 568 
32. Palmieri M, Impey S, Kang H, di Ronza A, Pelz C, Sardiello M, et al. Characterization of569 
the CLEAR network reveals an integrated control of cellular clearance pathways. Hum 570 
Mol Genet. 2011;20(19):3852-66. 571 
33. Miao L, Teng J, Lin J, Liao X, and Chen J. 14-3-3 proteins interact with neurofilament572 
protein-L and regulate dynamic assembly of neurofilaments. J Cell Sci. 2013;126(Pt 573 
2):427-36. 574 
34. Garcia-Arencibia M, Hochfeld WE, Toh PP, and Rubinsztein DC. Autophagy, a guardian575 
against neurodegeneration. Semin Cell Dev Biol. 2010;21(7):691-8. 576 
35. Zhao S, Wang JM, Yan J, Zhang DL, Liu BQ, Jiang JY, et al. BAG3 promotes autophagy and577 
glutaminolysis via stabilizing glutaminase. Cell Death Dis. 2019;10(4):284. 578 
36. Griffey CJ, and Yamamoto A. Macroautophagy in CNS health and disease. Nat Rev579 
Neurosci. 2022;23(7):411-27. 580 
.CC-BY-ND 4.0 International licenseavailable under a 
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made 
The copyright holder for this preprintthis version posted March 31, 2024. ; https://doi.org/10.1101/2024.03.29.587353doi: bioRxiv preprint 

24 
37. Son JH, Shim JH, Kim KH, Ha JY, and Han JY. Neuronal autophagy and neurodegenerative 581 
diseases. Exp Mol Med. 2012;44(2):89-98.582 
38. Rao MV, Darji S, Stavrides PH, Goulbourne CN, Kumar A, Yang DS, et al. Autophagy is a583 
novel pathway for neurofilament protein degradation in vivo. Autophagy. 2022:1-16. 584 
39. Scrivo A, Codogno P, and Bomont P. Gigaxonin E3 ligase governs ATG16L1 turnover to585 
control autophagosome production. Nat Commun. 2019;10(1):780. 586 
40. Zhou X, Lin Y, Kato M, Mori E, Liszczak G, Sutherland L, et al. Transiently structured head587 
domains control intermediate filament assembly. Proc Natl Acad Sci U S A. 2021;118(8). 588 
41. Wong YC, Kim S, Peng W, and Krainc D. Regulation and Function of Mitochondria-589 
Lysosome Membrane Contact Sites in Cellular Homeostasis. Trends Cell Biol. 590 
2019;29(6):500-13. 591 
42. Kimura S, Noda T, and Yoshimori T. Dissection of the autophagosome maturation592 
process by a novel reporter protein, tandem fluorescent-tagged LC3. Autophagy. 593 
2007;3(5):452-60. 594 
43. Sillevis Smitt PA, van der Loos C, Vianney de Jong JM, and Troost D. Tissue fixation595 
methods alter the immunohistochemical demonstrability of neurofilament proteins, 596 
synaptophysin, and glial fibrillary acidic protein in human cerebellum. Acta Histochem. 597 
1993;95(1):13-21. 598 
599 
600 
601 
602 
603 
.CC-BY-ND 4.0 International licenseavailable under a 
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made 
The copyright holder for this preprintthis version posted March 31, 2024. ; https://doi.org/10.1101/2024.03.29.587353doi: bioRxiv preprint 

Figures 604 
605 
606 
607 
608 
609 
610 
611 
612 
613 
614 
615 
616 
617 
618 
619 
620 
621 
622 
623 
624 
625 
626 
627 
628 
629 
Fig. 1 Dorsal root ganglia (DRG) neurons model the hallmark pathology of giant axonal 
neuropathy (GAN). (A) Representative fluorescence microscopy images of dorsal root ganglia 
(DRGs) from WT and GAN knockout mice stained for neurofilament light (NFL) after 2, 4, and 7 
days in vitro (DIV). Arrowheads denote NFL aggregation in the soma of GAN DRGs. Note that 
25 
.CC-BY-ND 4.0 International licenseavailable under a 
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made 
The copyright holder for this preprintthis version posted March 31, 2024. ; https://doi.org/10.1101/2024.03.29.587353doi: bioRxiv preprint 

630 
631 
632 
633 
634 
635 
636 
637 
638 
639 
640 
641 
642 
643 
644 
645 
646 
647 
648 
649 
650 
651 
652 
653 
654 
655 
NFL aggregates are already present after 2 DIV. Scale bar, 30 µm. (B) The GAN phenotype can 
be recapitulated by lentiviral delivery of shRNA targeting the Gan gene. Scale bar, 30 µm. After 
12 DIV, axonal fragmentation, a sign of neurodegeneration, occurs in GAN-silenced DRGs, as 
denoted by arrowheads; large aggregate shown in zoom. (C) Quantification of axonal 
fragmentation was accomplished using Fiji’s measurement tool, reported here as the means of 
3 independent experiments +/- SEM. ***p<0.001 by a two-tailed unpaired t-test. 
26 
.CC-BY-ND 4.0 International licenseavailable under a 
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made 
The copyright holder for this preprintthis version posted March 31, 2024. ; https://doi.org/10.1101/2024.03.29.587353doi: bioRxiv preprint 

656 
657 
658 
659 
660 
661 
662 
663 
664 
665 
666 
667 
668 
669 
670 
671 
672 
673 
674 
675 
676 
677 
678 
679 
680 
681 
27
Fig. 2 Mass spectrometry-based proteomic analysis of dorsal root ganglia (DRG) cultures 
silenced for gigaxonin. (A) Volcano plot showing the distribution of measured proteins 
extracted from DRG cultures in which GAN was silenced using shRNA (shGAN). (B) Plot 
showing top-ranked altered pathways in GAN where pathway activation (change in z-score) is 
shown (orange represents up-regulation and blue represents down-regulation). (C-D) Plots 
showing altered proteins for the phagosome formation and phagosome maturation pathways. 
Adjusted p-values denoted by *p<0.05, **p<0.001, and ***p<0.0001. NFL = neurofilament light, 
NFM= neurofilament medium, and PRFN = peripherin. 
.CC-BY-ND 4.0 International licenseavailable under a 
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made 
The copyright holder for this preprintthis version posted March 31, 2024. ; https://doi.org/10.1101/2024.03.29.587353doi: bioRxiv preprint 

28
Fig. 3 Neurofilament aggregates alter autophagosome spatial distribution. (A) 
Representative fluorescence images of DRG neurons from WT or GAN knockout mice co-
stained for the cytoskeleton marker neurofilament light (NFL) and the autophagosome marker 
LC3. Autophagosomes are excluded from neurofilament aggregates, and LC3 puncta are found 
at the periphery of the aggregates (white arrowhead). (B) WT or GAN knockout mouse DRGs 
co-stained for the cytoskeletal marker NFL and the lysosomal marker LAMP-1. Two phenotypes 
are observed in GAN DRG neurons with neurofilament aggregates: lysosomes are either 
excluded (circular dotted line) or co-localized with neurofilament aggregates (arrowhead). Scale 
bar, 30 µm. Representative images from three independent experiments. 
682 
683 
684 
685 
686 
687 
688 
689 
690 
691 
692 
693 
694 
695 
696 
697 
698 
699 
700 
701 
702 
703 
704 
705 
706 
707 
.CC-BY-ND 4.0 International licenseavailable under a 
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made 
The copyright holder for this preprintthis version posted March 31, 2024. ; https://doi.org/10.1101/2024.03.29.587353doi: bioRxiv preprint 

29 
Fig. 4 Spatial distribution of lysosomes is altered by neurofilament aggregates in GAN 
DRG neurons. Rep resentative fluorescence images of DRG neurons silenced for gigaxonin 
(shGAN) and control neurons (shSCR) co-st ained for NFL and (A) mucolipin-1 and vacuolar 
ATPase or (B) cat hepsin B and cathepsin D. While cathepsin D is excluded from neurofilament 
aggregates, the three other lysosomal proteins are sequestered in aggregates in shGA N DRG 
neurons. Scale bar, 30 µm . Arrowheads highlight lysosomal proteins clumped in NFL 
aggregates in the shGAN  condition. 
708 
709 
710 
711 
712 
713 
714 
715 
716 
717 
718 
719 
720 
721 
722 
723 
724 
725 
726 
727 
728 
729 
730 
731 
732 
733 
.CC-BY-ND 4.0 International licenseavailable under a 
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made 
The copyright holder for this preprintthis version posted March 31, 2024. ; https://doi.org/10.1101/2024.03.29.587353doi: bioRxiv preprint 

30 
Fig. 5 Lysosome alterations in GAN DRG neurons. (A) Representative live imaging 
fluorescence images of control and shGAN DRG s transduced with NFL-GFP tagged lentivirus 
and treated with red lysotracker to visualize lysosomes. Expression of the NFL-GFP c onstruct in 
shGAN DRG neurons allowed neurofilament aggr egate visualization in living cells. shGAN 
induces an increase in the number of lysosomes (B) and the surface area covered by these 
organelles (C). Lysotracker mean intensity is also increased in shGAN  cultures (D). Note that as 
observed after NFL and LAMP-1 co-s taining, lysotracker dye is also mainly excluded from 
neurofilament aggregat es (circular dotted line). Scale bar, 30 µm. Quantitative data are 
presented as means +/- SEM, w ith ***p<0.001 by a two-tailed unpaired t-test. Representative 
images from three independent experiments. 
734 
735 
736 
737 
738 
739 
740 
741 
742 
743 
744 
745 
746 
747 
748 
749 
750 
751 
752 
753 
754 
755 
756 
757 
758 
759 
.CC-BY-ND 4.0 International licenseavailable under a 
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made 
The copyright holder for this preprintthis version posted March 31, 2024. ; https://doi.org/10.1101/2024.03.29.587353doi: bioRxiv preprint 

31 
Fig. 6 GAN is associated with abnormal autophagic organelles. Transmission electronic 
microscopy (TE M) microphotographs of control and GAN DRGs showing the presence of a 
variety of autophagic organelles including large autophagic vacuoles, dark dense lysosomes 
(open arrowheads), m ultilamellar bodies, and immature autophagosomes (filled arrowheads). 
760 
761 
762 
763 
764 
765 
766 
767 
768 
769 
770 
771 
772 
773 
774 
775 
776 
777 
778 
779 
780 
781 
782 
783 
784 
785 
.CC-BY-ND 4.0 International licenseavailable under a 
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made 
The copyright holder for this preprintthis version posted March 31, 2024. ; https://doi.org/10.1101/2024.03.29.587353doi: bioRxiv preprint 

32 
Fig. 7 Autophagic flux is altered in GAN DRG cultures. Lysosomal pH is dysregulated in 
GAN DRG cultures. (A)  Representative live imaging microphotographs of control and GAN 
DRG cultures treated with a combination of red lysotracker to visualize lysosomes and green 
lysosensor to evaluate pH alterations. Mean intensity of lysos ensor (pH sensitive probe) is 
786 
787 
788 
789 
790 
791 
792 
793 
794 
795 
796 
797 
798 
799 
800 
801 
802 
803 
804 
805 
806 
807 
808 
809 
810 
811 
.CC-BY-ND 4.0 International licenseavailable under a 
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made 
The copyright holder for this preprintthis version posted March 31, 2024. ; https://doi.org/10.1101/2024.03.29.587353doi: bioRxiv preprint 

33 
decreased in lysosomes from GAN cultures, suggesting lysosomal milieu is less acidic in the 
GAN condition. (B) Representative live imaging microphotographs of control or GAN DRG cells 
transduced with the sensor LC3-G FP-RFP. Individual panels are presented for GFP, RFP, and 
merged signals. The construct is composed of an RFP pH-res istant tag, a GFP pH-sensitive 
tag, and LC3  that targets the tags to nascent autophagosomes. After fusion with lysosomes, 
autophagolysosomes a re formed and the GFP signal is quenched due to the acidic milieu 
provided by lysosomes, conv erting the fluorescent signal from yellow to red. The GAN condition 
is associated with an increase in autophagic organelles positive for both GFP and RFP signals. 
Autophagic organelle size is also increased in GAN. (C) Representative fluorescent images of 
control and GAN DRG neurons co-st
 ained for NFL and p62. (D) Immunoblot of p62 in control 
and GAN DRG cultures. Both p62 mean int ensity and protein levels are increased in GAN DRG 
cultures. Quantitative data are presented as means +/- SEM,  with *p<0.05 or ***p<0.001 the 
two-tailed P values from an unpaired t-t est. Scale bar, 30 µm. 
812 
813 
814 
815 
816 
817 
818 
819 
820 
821 
822 
823 
824 
825 
826 
827 
828 
829 
830 
831 
832 
833 
834 
835 
836 
837 
.CC-BY-ND 4.0 International licenseavailable under a 
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made 
The copyright holder for this preprintthis version posted March 31, 2024. ; https://doi.org/10.1101/2024.03.29.587353doi: bioRxiv preprint 

34 
838 
839 
840 
841 
842 
843 
844 
845 
846 
847 
848 
849 
850 
851 
852 
853 
854 
855 
856 
857 
858 
859 
Fig. 8 Neurofilament aggregates sequester TFEB and impairs its nuclear translocation. 860 
(A) Representative fluorescence images of control and shGAN DRGs co-stained for NFL and861 
TFEB showing sequestering of the transcription factor (arrowhead). Scale bar, 30 µm. (B) 862 
Higher magnification pictures showing decreased TFEB localization in the nuclear compartment 863 
.CC-BY-ND 4.0 International licenseavailable under a 
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made 
The copyright holder for this preprintthis version posted March 31, 2024. ; https://doi.org/10.1101/2024.03.29.587353doi: bioRxiv preprint 

35 
in shGAN DRG neurons. Accompanying plots show that TFEB has decreased intensity, and that 864 
nuclear size is similar between control and shGAN DRG neurons. (C) Representative 865 
fluorescence images of control and shGAN DRG neurons co-stained for NFL and 14-3-3. 866 
Neurofilament aggregates sequester 14-3-3 (arrowhead). Scale bar, 30 µm. 867 
.CC-BY-ND 4.0 International licenseavailable under a 
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made 
The copyright holder for this preprintthis version posted March 31, 2024. ; https://doi.org/10.1101/2024.03.29.587353doi: bioRxiv preprint 