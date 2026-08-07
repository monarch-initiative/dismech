---
reference_id: DOI:10.1186/s43042-024-00479-5
title: "In silico analysis of mutation spectrum of Ehlers–Danlos, osteogenesis imperfecta, and cutis laxa overlapping phenotypes in Iranian population"
authors:
- Teymoor Khosravi
- Karim Naghipoor
- Fatemeh Vaghefi
- Ali Mohammad Falahati
- Morteza Oladnabi
journal: Egyptian Journal of Medical Human Genetics
year: '2024'
doi: 10.1186/s43042-024-00479-5
content_type: full_text_pdf
full_text_attempted: true
full_text_provider: openalex
full_text_url: "https://jmhg.springeropen.com/counter/pdf/10.1186/s43042-024-00479-5"
oa_status: diamond
license: cc-by
local_pdf_path: files/DOI_10.1186_s43042-024-00479-5.pdf
---

# In silico analysis of mutation spectrum of Ehlers–Danlos, osteogenesis imperfecta, and cutis laxa overlapping phenotypes in Iranian population
**Authors:** Teymoor Khosravi, Karim Naghipoor, Fatemeh Vaghefi, Ali Mohammad Falahati, Morteza Oladnabi
**Journal:** Egyptian Journal of Medical Human Genetics (2024)
**DOI:** [10.1186/s43042-024-00479-5](https://doi.org/10.1186/s43042-024-00479-5)

## Content

AbstractBackgroundEhlers–Danlos syndrome (EDS), osteogenesis imperfecta (OI), and cutis laxa (CL) are three rare and heterogeneous connective tissue disorders. Patients with these syndromes have similar manifestations and unpredictable prognosis, making a misdiagnosis highly probable. Some of their subtypes are inherited in autosomal recessive patterns, so they are expected to be prevalent in populations like Iran, where consanguineous marriages are common. In the current work, a cohort of Iranian patients with overlapping phenotypes of the EDS/OI/CL and their mutation spectrum was defined. Based on this, in silico analysis was conducted to anticipate further probable genetic variations. Pathogenicity of EDS, OI, and CL variants in Iranian patients was evaluated using Web servers. A protein interaction network was created by String database and visualized using a Python-based library. The Iranome database was used to predict other genetic mutations in all reported genes of EDS, OI, and CL syndromes.ResultsIn the EDS/OI/CL overlap phenotype, 32 variants in 18 genes have been involved. At least 59% of patients were from families with consanguineous marriages. Interaction analysis showed thatCOL1A1,COL1A2,CRTAP,LEPRE1,PLOD1, andADAMTS2have the most significant impact within the protein network of EDS/OI/CL overlap phenotype. Analyzing the Iranome database revealed 46 variants of EDS, OI, and CL genes potentially disease causing.ConclusionThe overlapping phenotype of EDS, OI, and CL syndromes requires genetic testing (e.g., whole-exome sequencing) to reveal respective variants, which helps to diagnose more accurately and manage the disease more effectively. Particularly in populations with high rates of consanguineous marriages, such as Iran, genetic screening plays a crucial role in premarital and prenatal counseling to prevent the transmission of these rare connective tissue disorders.

Khosravi et al. 
Egyptian Journal of Medical Human Genetics            (2024) 25:8  
https://doi.org/10.1186/s43042-024-00479-5
RESEARCH Open Access
© The Author(s) 2024. Open Access This article is licensed under a Creative Commons Attribution 4.0 International License, which 
permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the 
original author(s) and the source, provide a link to the Creative Commons licence, and indicate if changes were made. The images or 
other third party material in this article are included in the article’s Creative Commons licence, unless indicated otherwise in a credit line 
to the material. If material is not included in the article’s Creative Commons licence and your intended use is not permitted by statutory 
regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this 
licence, visit http://creativecommons.org/licenses/by/4.0/.
Egyptian Journal of Medical
Human Genetics
In silico analysis of mutation spectrum 
of Ehlers–Danlos, osteogenesis imperfecta, 
and cutis laxa overlapping phenotypes 
in Iranian population
Teymoor Khosravi1, Karim Naghipoor1, Fatemeh Vaghefi1, Ali Mohammad Falahati1 and 
Morteza Oladnabi2,3,4*   
Abstract 
Background Ehlers–Danlos syndrome (EDS), osteogenesis imperfecta (OI), and cutis laxa (CL) are three rare and het-
erogeneous connective tissue disorders. Patients with these syndromes have similar manifestations and unpredictable 
prognosis, making a misdiagnosis highly probable. Some of their subtypes are inherited in autosomal recessive pat-
terns, so they are expected to be prevalent in populations like Iran, where consanguineous marriages are common. In 
the current work, a cohort of Iranian patients with overlapping phenotypes of the EDS/OI/CL and their mutation spec-
trum was defined. Based on this, in silico analysis was conducted to anticipate further probable genetic variations. 
Pathogenicity of EDS, OI, and CL variants in Iranian patients was evaluated using Web servers. A protein interaction 
network was created by String database and visualized using a Python-based library. The Iranome database was used 
to predict other genetic mutations in all reported genes of EDS, OI, and CL syndromes.
Results In the EDS/OI/CL overlap phenotype, 32 variants in 18 genes have been involved. At least 59% of patients 
were from families with consanguineous marriages. Interaction analysis showed that COL1A1, COL1A2, CRTAP, LEPRE1, 
PLOD1, and ADAMTS2 have the most significant impact within the protein network of EDS/OI/CL overlap phenotype. 
Analyzing the Iranome database revealed 46 variants of EDS, OI, and CL genes potentially disease causing.
Conclusion The overlapping phenotype of EDS, OI, and CL syndromes requires genetic testing (e.g., whole-exome 
sequencing) to reveal respective variants, which helps to diagnose more accurately and manage the disease more 
effectively. Particularly in populations with high rates of consanguineous marriages, such as Iran, genetic screening 
plays a crucial role in premarital and prenatal counseling to prevent the transmission of these rare connective tissue 
disorders.
Keywords Ehlers–Danlos syndrome, Osteogenesis imperfecta, Cutis laxa, Genetic database, Mutations, Genetic 
testing, Consanguineous marriages
*Correspondence:
Morteza Oladnabi
oladnabidozin@yahoo.com
Full list of author information is available at the end of the article

Page 2 of 20Khosravi et al. Egyptian Journal of Medical Human Genetics            (2024) 25:8 
Background
Hereditary connective tissue disorders (HCTD) com -
prise a heterogeneous and pleiotropic group of genetic 
conditions with structural and functional disruptions in 
extracellular matrix (ECM) components. Dermal, ocu -
lar, and musculoskeletal manifestations, along with heart 
and lung defects, contribute to the burden of HCTDs 
[2]. From an epidemiological perspective, every HCTD 
is a rare disease, but combined, they are a notable part 
of human congenital disorders [9]. Studying these syn -
dromes enhances our understanding of the nature of 
connective tissue (CT) and has the potential to lead to 
more effective treatments. Connective tissue is one of the 
mesodermal germ layer derivatives that exist in almost 
every part of the body. It connects biological structures 
and establishes the framework necessary for the normal 
functioning of organs. This tissue comprises three basic 
parts: soft CT, which surrounds internal organs; hard 
CT, including bone and cartilage; and liquid CT, which 
is blood. Extracellular matrix in CT consists of four com -
ponents: collagens, elastic fibers, glycoproteins, and gly -
cosaminoglycans [8, 30].
Collagens are fibrillary proteins that account for one-
third of the human body’s total protein. There are five 
types of classical fibrillary collagen: types I, II, III, V, and 
XI, which are different helical conformations of alpha-
chain polypeptide strands coiling around each other. The 
alpha chain is made of an amino acid triplet repeat gly -
cine-X–Y, where X and Y are commonly hydroxyproline 
and proline [12, 36]. While collagen fibrils are responsi -
ble for the strength of the structures, their resiliency is 
provided by elastic fibers. The process of elastin forma -
tion, also referred to as elastogenesis, is complex and 
not yet fully understood. Microfibers are the main build -
ing blocks of elastic fibers. They are a polymerized scaf -
fold of fibrillins, a large protein with a molecular weight 
of 150  kDa [45]. Collagen, elastic fiber, and other ECM 
components like fibronectin and laminin interact to per -
form tissue morphogenesis, cell adhesion, migration, or 
differentiation.
Clinical management of HCTDs is faced with three 
challenges [35]: (1) Ambiguity: The ubiquitous presence 
of connective tissue throughout the human body con -
tributes to the challenge of defining and observing the 
phenotypes of HCTDs in various organs. (2) Variability: 
patients with the same diagnosis of an HCTD can differ, 
even in intra-familial cases. (3) Unpredictability: pheno -
types of an individual with an HCTD can change over 
the lifetime, and also they might have temporal manifes -
tations.  Therefore, a misdiagnosis at the early stages is 
highly probable.
Based on which component of ECM is dysregulated, 
HCTDs are categorized into two major classes: colla -
genopathies, including Ehlers–Danlos syndrome (EDS), 
osteogenesis imperfecta (OI), Alport syndrome, and 
chondrodysplasias. And elastinopathies, including cutis 
laxa (CL), Marfan syndrome, and pseudoxanthoma 
elasticum (PXE).  These diseases are phenotypically 
varied and genetically heterogeneous. These diseases 
exhibit a wide range of phenotypic variations and 
genetic heterogeneity. A total of 20, 16, and 13 genes 
have been responsible for EDS, OI, and CL syndromes, 
up to now.
Ehlers–Danlos syndrome is a soft HTCD character -
ized by skin hyperextensibility, joint hypermobility, bone 
fragility and osteoporosis, atrophic scars, loose skin, and 
cardiovascular problems like mitral valve prolapse [28]. 
The prevalence of different subtypes is about 1 in 5000 to 
1 in 20,000. Based on a 2017 international classification, 
classical EDS, arthrocalasis EDS, and cardiac valvular 
EDS are the three main subtypes of the syndrome [27].
Osteogenesis imperfecta has a prevalence of 1 in 20,000 
live births. It mostly manifests with growth defects, bone 
fragility, osteopenia, dentinogenesis imperfecta, and 
blueish sclera. Up to 90 percent of IO cases are due to 
mutations in COL1A1 and COL1A2. These two are also 
responsible for many EDS cases [24]. The initial step in 
diagnosing these two syndromes is identifying their 
similar clinical signs, which makes it challenging to pro -
vide follow-up care and genetic counseling. There is an 
extremely rare condition called EDS/OI overlap, which 
affects approximately 1 in every 1,000,000 individuals 
(based on Orphanet data). It was first described in 2013 
when patients with combined symptoms were reported. 
Molecular analysis of this overlap revealed an association 
with N-terminal mutations in type 1 collagen [33].
An abnormal synthesis of elastic fibers can result in CL 
syndrome, characterized primarily by loose and redun -
dant skin, developmental emphysema, cardiovascular 
issues like aortic aneurysm, hernia, delayed growth, and 
fragile bones. In some CL cases, patients mimic manifes -
tations of EDS with similar skin hyper-elasticity, scarring, 
and joint laxity [13]. Furthermore, CL cases with muta -
tions in RIN2 and ELN exhibit phenotypic similarities to 
EDS patients, including sparse hair and alopecia. [14, 48].
Genetic defects in CT components mostly manifest 
as phenotypic traits. In these three disorders, in addi -
tion to the CT nature, intermediate clinical phenotypes 
(e.g., blueish sclera in EDS and IO and bone fragility in 
all three) increase the probability of misdiagnosis. Con -
sanguineous marriage (marriage between relatives) is 
commonly performed in Iran. The general rate of that is 
38.6% throughout the country [44]. Thus, it has received 

Page 3 of 20
Khosravi et al. Egyptian Journal of Medical Human Genetics            (2024) 25:8 
 
great attention as a potential risk factor for many genetic-
influenced health outcomes, especially autosomal reces -
sive (AR) disorders.
According to NORD’s database (https:// rared iseas 
es. org/), CL, ESD, and OI have various subtypes and 
inheritance patterns. For CL, subdivisions are as fol -
lows: acquired cutis laxa, ALDH18A1-related cutis 
laxa, ATP6V0A2-related cutis laxa, autosomal domi -
nant cutis laxa (ADCL), autosomal recessive cutis laxa 
type 1A (ARCL1A), autosomal recessive cutis laxa 
type 1B (ARCL1B), autosomal recessive cutis laxa type 
1C (ARCL1C), autosomal recessive cutis laxa type 
2A (ARCL2A), autosomal recessive cutis laxa type 
2B (ARCL2B), autosomal recessive cutis laxa type 3, 
Debre-type cutis laxa, EFEMP2-related cutis laxa, ELN-
related cutis laxa, geroderma osteodyplasticum, LTBP4-
related cutis laxa, MACS syndrome, PYCR1-related cutis 
laxa, RIN2-related cutis laxa, Urban–Rifkin–Davis syn -
drome, wrinkly skin syndrome. Most cases of autosomal 
dominant cutis laxa are caused by mutations in the elastin 
(ELN) gene and are also known as ELN-related cutis laxa 
or autosomal dominant cutis laxa type 1 (ADCL1). One 
case, classified as autosomal dominant cutis laxa type 
2 (ADCL2), was caused by a mutation in the fibulin-5 
(FBLN5) gene. Ehlers–Danlos syndrome subdivisions are 
as follows: classic EDS, classical-like EDS, cardiac valvu -
lar EDS, vascular EDS, hypermobile EDS, anthrochalasia 
EDS, dermatosparaxis EDS, kyphoscoliotic EDS, brittle 
Fig. 1 Genes involved in overlap phenotype of EDS, OI, and CL demonstrated on their respective chromosomal region. None are located 
on chromosomes 4, 13, 16, 18, 21, and Y, while chromosomes 11 and 17 host five genes

Page 4 of 20Khosravi et al. Egyptian Journal of Medical Human Genetics            (2024) 25:8 
Table 1 Function, pathway, and ontology of the genes involved in overlap phenotype of EDS, OI, and CL. All OI-related genes have a role in collagen biosynthesis and function or 
bone development. Elastic fibers biosynthesis and function, different amino acid biosynthesis, and energy production are the main roles of CL-related genes. EDS-related genes 
have similar functions
Gene Full name Function Pathway Ontology
OI COL1A1 Collagen alpha-1(I) chain Type 1 Collagen Structure ECM–receptor interaction, PI3K-Akt sign-
aling pathway, focal adhesion, platelet 
activation, relaxin signaling pathway, 
protein digestion and absorption
Identical protein binding and platelet-
derived growth factor binding
COL1A2 Collagen alpha-2(I) chain Type 1 Collagen Structure ECM–receptor interaction, PI3K-Akt sign-
aling pathway, focal adhesion, platelet 
activation, relaxin signaling pathway, 
protein digestion and absorption
Identical protein binding and protein–mac-
romolecule adaptor activity
BMP1 Bone morphogenetic protein 1 ECM formation Cytokine–cytokine receptor interaction, 
ovarian steroidogenesis
Calcium ion binding and growth factor 
activity
CREB3L1 Cyclic AMP-responsive element-binding 
protein 3-like protein 1
COL1A1 and COL1A2 regulation in bone 
formation
Glucagon signaling pathway, cGMP-PKG 
signaling pathway, cAMP signaling path-
way, PI3K-Akt signaling pathway, AMPK 
signaling pathway, TNF signaling pathway
DNA-binding transcription factor activity 
and chromatin binding
CRTAP Cartilage-associated protein Collagen stabillizing Collagen bisynthesis and modifying 
enzymes
Protein-containing complex binding
FKBP10 FKBP prolyl isomerase 10 Collagen molecule cross-linking PI3K signaling pathway Calcium ion binding and FK506 binding
SP7 Sp7 transcription factor Embryonic bone development RUNX2 regulates osteoblast differentia-
tion
DEAD/H-box RNA helicase binding
WNT1 Wnt family member 1 Osteoblast function, bone development, 
and bone homeostasis
Signaling pathways regulating pluri-
potency of stem cells, mTOR signaling 
pathway, Hippo signaling pathway
Signaling receptor binding and transcrip-
tion cis-regulatory region binding
PLOD2 Procollagen-lysine,2-oxoglutarate 
5-dioxygenase 2
Type 1 collagen synthesis Lysine degradation, metabolic pathways Oxidoreductase activity and oxidoreduc-
tase activity, acting on paired donors, 
with incorporation or reduction of molecu-
lar oxygen
PLS3 Plastin 3 Bone development PI3K/AKT signaling pathway, MAPK signal-
ling pathway, TGF-β signaling pathway
Calcium ion binding and actin binding
PPIB Peptidylprolyl isomerase B Type 1 collagen synthesis and terimeriza-
tion
Collagen bisynthesis and modifying 
enzymes
RNA binding and unfolded protein binding
IFITM5 Interferon-induced transmembrane 
protein 5
Type 1 collagen synthesis/ bone miner-
alization
Collagen synthesis pathway NA
P3H1 Prolyl 3-hydroxylase 1 Type 1 collagen synthesis and terimeriza-
tion
Collagen synthesis pathway Oxidoreductase activity and iron ion bind-
ing
SERPINF1 Serpin family F member 1 Type 1 collagen synthesis Wnt signaling pathway Serine-type endopeptidase inhibitor 
activity
SERPINH1 Serpin family H member 1 Type 1 collagen synthesis and terimeriza-
tion
Collagen bisynthesis and modifying 
enzymes
RNA binding and serine-type endopepti-
dase inhibitor activity
TMEM38B Transmembrane protein 38B Type 1 collagen synthesis/ intracellular 
calcium release
Collagen synthesis pathway Potassium channel activity and cation 
channel activity

Page 5 of 20
Khosravi et al. Egyptian Journal of Medical Human Genetics            (2024) 25:8 
 
Table 1 (continued)
Gene Full name Function Pathway Ontology
CL FBLN4 (EFEMP2) EGF-containing fibulin extracellular matrix 
protein 2
Elastic fiber formation in aorta Extracellular matrix organization and inte-
grin pathway
Calcium ion binding and extracellular 
matrix structural constituent
FBLN5 Fibulin 5 Elastic fiber formation in skin, lung, 
and vasculature
Autophagy pathway and extracellular 
matrix organization
Calcium ion binding and transmembrane 
signaling receptor activity
ATP6V0A2 ATPase H + transporting V0 subunit A2 a2 subunit of the V-type H + ATPase Oxidative phosphorylation, metabolic 
pathways, synaptic vesicle cycle, epithelial 
cell signaling in helicobacter pylori infec-
tion
ATPase binding and proton-transporting 
ATPase activity, rotational mechanism
ALDH18A1 Aldehyde dehydrogenase 18 family 
member A1
P5CS mitochondrial protein Biosynthesis of amino acids, arginine 
and proline metabolism, metabolic 
pathways
RNA binding and NADP binding
LTBP4 Latent transforming growth factor beta 
binding protein 4
Elastic fiber formation Apoptotic pathways in synovial fibro-
blasts and extracellular matrix organiza-
tion
Calcium ion binding and glycosaminogly-
can binding
ELN Elastin Extracellular matrix organization and Inte-
grin Pathway
Protein digestion and absorption Extracellular matrix constituent conferring 
elasticity
GORAB Golgin, RAB6 interacting A protien of golgin family P53 signaling pathway NA
PYCR1 Pyrroline-5-carboxylate reductase 1 Proline synthesis Arginine and proline metabolism, meta-
bolic pathways, biosynthesis of amino 
acids
Identical protein binding and oxidoreduc-
tase activity, acting on the CH-OH group 
of donors, NAD or NADP as acceptor
ATP7A ATPase copper-transporting alpha Cell homeostasis of copper Platinum drug resistance, mineral absorp-
tion
Nucleotide binding and ATPase-coupled 
cation transmembrane transporter activity
RIN2 Ras and Rab interactor 2 Regulates the adhesion of ECs to ECM 
proteins via its Rab5 and Ras binding 
domains
Vesicle-mediated transport and Rab 
regulation of trafficking
GTPase activator activity and GTPase regu-
lator activity
SLC2A10 Solute carrier family 2 member 10 Facilitative glucose transporter required 
for the development of the cardiovascular 
system
Nuclear receptors meta-pathway Transmembrane transporter activity 
and glucose transmembrane transporter 
activity
ATP6V1E1 ATPase H + transporting V1 subunit E1 Acidify intracellular compartments 
in eukaryotic cells
Oxidative phosphorylation, metabolic 
pathways, mTOR signaling pathway, 
epithelial cell signaling in helicobacter 
pylori infection
ATPase binding and P-type proton-export-
ing transporter activity
ATP6V1A ATPase H + transporting V1 subunit A Hydrolyze ATP to provide energy for trans-
porting H + 
Oxidative phosphorylation, metabolic 
pathways, mTOR signaling pathway, 
epithelial cell signaling in helicobacter 
pylori infection
Acyltransferase activity and choline 
O-acetyltransferase activity
EDS COL1A1 Collagen type I alpha 1 chain Type 1 collagen structure ECM–receptor interaction, PI3K-Akt sign-
aling pathway, focal adhesion, platelet 
activation, relaxin signaling pathway, 
protein digestion and absorption
Identical protein binding and platelet-
derived growth factor binding

Page 6 of 20Khosravi et al. Egyptian Journal of Medical Human Genetics            (2024) 25:8 
Table 1 (continued)
Gene Full name Function Pathway Ontology
COL3A1 Collagen type III alpha 1 chain Provides instructions for making type III 
collagen
PI3K-Akt signaling pathway Integrin binding and SMAD binding
PLOD1 Procollagen-lysine,2-oxoglutarate 
5-dioxygenase 1
Encodes the 125-kDa catalytic subunit 
of DNA polymerase delta
Lysine degradation, metabolic pathways Protein homodimerization activity and iron 
ion binding
TNXB Tenascin XB Provides instructions for making a protein 
called tenascin-X
PI3K-Akt signaling pathway and extracel-
lular matrix organization
Heparin binding and collagen binding
COL5A2 Collagen type V alpha 2 chain Provides instructions for making a com-
ponent of type V collagen
PI3K-Akt signaling pathway and collagen 
chain trimerization
Extracellular matrix structural constituent 
and SMAD binding
COL5A1 Collagen type V alpha 1 chain Provides instructions for making a com-
ponent of type V collagen
PI3K-Akt signaling pathway and collagen 
chain trimerization
Heparin binding and extracellular matrix 
structural constituent
COL1A2 Collagen type I alpha 2 chain Type 1 collagen structure ECM–receptor interaction, PI3K-Akt sign-
aling pathway, focal adhesion, platelet 
activation, relaxin signaling pathway, 
protein digestion and absorption
Identical protein binding and platelet-
derived growth factor binding
ADAMTS2 ADAM metallopeptidase with thrombos-
pondin type 1 motif 2
Cleaves the propeptides of type I and II 
collagen prior to fibril assembly
Collagen synthesis pathway, o-glycozila-
tion of TSR domain-containing proteins
Peptidase activity and metallopeptidase 
activity
P3H1 Prolyl 3-hydroxylase 1 Type 1 collagen synthesis and terimeriza-
tion
Collagen synthesis pathway Oxidoreductase activity and iron ion bind-
ing
B4GALT7 Beta-1,4-galactosyltransferase 7 Required for the biosynthesis of the tet-
rasaccharide linkage region of proteogly-
cans, especially for small proteoglycans 
in skin fibroblasts
Glycosaminoglycan biosynthesis—chon-
droitin sulfate / dermatan sulfate, gly-
cosaminoglycan biosynthesis—heparan 
sulfate / heparin, metabolic pathways
Glycosyltransferase activity and galactosyl-
transferase activity
B3GALT6 Beta-1,3-galactosyltransferase 6 Beta-1,3-galactosyltransferase that trans-
fers galactose from UDP-galactose 
to substrates with a terminal beta-linked 
galactose residue
Glycosaminoglycan biosynthesis—chon-
droitin sulfate / dermatan sulfate, gly-
cosaminoglycan biosynthesis—heparan 
sulfate / heparin, metabolic pathways
Galactosyltransferase activity and UDP-
galactosyltransferase activity
CHST14 Carbohydrate sulfotransferase 14 Encodes a member of the HNK-1 family 
of sulfotransferases
Glycosaminoglycan biosynthesis—chon-
droitin sulfate / dermatan sulfate
Culfotransferase activity and N-acetylgalac-
tosamine 4-O-sulfotransferase activity
DSE Dermatan sulfate epimerase Converts D-glucuronic acid to L-iduronic 
acid (IdoUA) residues
Retrograde endocannabinoid signaling, 
glycosaminoglycan biosynthesis—
chondroitin sulfate / dermatan sulfate, 
metabolic pathways
Chondroitin-glucuronate 5-epimerase 
activity
FKBP14 FKBP prolyl isomerase 14 PPIase which accelerates the folding 
of proteins during protein synthesis
IL-6/STAT3 signaling pathway, notch path-
way, Wnt/β-catenin signaling pathway
Calcium ion binding and FK506 binding
SLC39A13 Solute carrier family 39 member 13 Acts as a zinc influx transporter Nuclear receptors meta-pathway 
and metal ion SLC transporters
Protein homodimerization activity and zinc 
ion transmembrane transporter activity
FLNA Filamin A Promotes orthogonal branching of actin 
filaments and links actin filaments 
to membrane glycoproteins
Cytoskeletal signaling, MAPK signaling 
pathway, focal adhesion
RNA binding and transcription factor 
binding

Page 7 of 20
Khosravi et al. Egyptian Journal of Medical Human Genetics            (2024) 25:8 
 
Table 1 (continued)
Gene Full name Function Pathway Ontology
C1S Complement C1s C1s B chain is a serine protease 
that combines with C1q and C1r to form 
C1, the first component of the classical 
pathway of the complement system
NA Calcium ion binding and serine-type endo-
peptidase activity
C1R Complement C1r C1r B chain is a serine protease that com-
bines with C1q and C1s to form C1, 
the first component of the classical path-
way of the complement system
Initial triggering of complement 
and notch signaling
Calcium ion binding and serine-type pepti-
dase activity
ZNF49 Zinc finger protein 546 May be involved in transcriptional regula-
tion
NA Nucleic acid binding and DNA-binding 
transcription factor activity
COL12A1 Collagen type XII alpha 1 chain Encodes the alpha chain of type XII col-
lagen
Protein digestion and absorption Extracellular matrix structural constituent 
conferring tensile strength
CRTAP Cartilage-associated protein Necessary for efficient 3-hydroxylation 
of fibrillar collagen prolyl residues
Collagen synthesis pathway Protein-containing complex binding

Page 8 of 20Khosravi et al. Egyptian Journal of Medical Human Genetics            (2024) 25:8 
cornea syndrome, spondylodysplastic EDS, musculocon -
tractural EDS, myopathic EDS, periodontal EDS. Among 
these syndromes, classical-like, cardiac valvular, dermat -
osparaxis, and kyphoscoliotic types are inherited in an 
AR manner. Myopathic EDS has both AD and AR inher -
itance, while the remaining types are AD.
Osteogenesis imperfecta types I to XXI are subtypes 
of OI. Types I to V exhibit AD inheritance, while the 
remaining types are inherited in an AR manner. These 
three rare HCTDs have multiple AR subtypes, which 
are another complexity next to their clinical overlap. As 
depicted in Fig.  1, a total of 45 genes have been identi -
fied globally to be associated with the overlapping pheno-
type of EDS, OI, and CL. About half are on chromosomes 
1, 11, 12, and 17. Details like function, related pathway, 
and ontology of these genes are listed in Table 1. The aim 
of this study is to address the clinical and genetic com -
plexities of the overlapping phenotypes of Ehlers–Danlos 
syndrome (EDS), osteogenesis imperfecta (OI), and cutis 
laxa (CL). The research question seeks to determine the 
extent to which specific genetic variants contribute to 
the clinical features of these disorders within the Iranian 
population, which is characterized by a high consanguin -
eous marriage rate [16, 49]. It is hypothesized that a clear 
genetic basis of these diseases can aid in the develop -
ment of more precise diagnostic and therapeutic strate -
gies like whole-exome sequencing or RNA therapeutics 
[5, 22]. The genetic diversity of the Iranian population is 
leveraged in this study to fill a critical knowledge gap in 
understanding the pathogenesis of these syndromes and 
to propose potential targets for intervention in popula -
tions with similar genetic backgrounds.
Methods
Data collection
Investigation of EDS, IO, and CL patients in Iranian 
patients to draw a spectrum of their mutation was per -
formed in a systematic search. For that purpose, the 
keywords ‘osteogenesis imperfecta, ’ ‘ehlers danlos, ’ and 
‘cutis laxa’ along with ‘Iran’ (or Iranian) in both English 
and Farsi were used. PUBMED, Web of Science, Sco -
pus, Cochrane Library databases, Google Scholar, and 
Scientific Information Database (SID, an Iranian medi -
cal database) were used as search engines. The search 
for data was up to March 2023, and there was no more 
restriction. Afterward, the manuscripts were filtered to 
reach the ones in which genetic tests reported the vari -
ants. Also, duplicated ones were removed. Moreover, 
the HGMD Professional 2021.4 database was utilized for 
each gene to evaluate the number and types of mutations.
In silico prediction of pathogenicity and stability of single 
nucleotide variants
The obtained spectrum of gene mutations of Iranian 
patients with EDS, CL, and OI was analyzed by in silico 
tools to predict their pathogenicity and protein stability. 
For that purpose, ACMG (https:// frank  lin. genoox. com/ 
clini cal- db), CADD (https:// cadd. gs. washi ngton. edu/), 
SIFT ( https:// sift. bii.a- star. edu. sg/), polyphen-2 (http:// 
genet ics. bwh. harva rd. edu/ pph2/), and Fathmm (http:// 
fathmm. bioco mpute. org. uk/) were used. Also, the effect 
of missense variants on protein stability was evaluated 
using I-Mutant 2.0 (https:// foldi ng. biofo ld. org/i- mutant/ 
i- mutan t2.0. html) and MUpro (https:// mupro. prote 
omics. ics. uci. edu/) Web servers. Moreover, the manu -
scripts were mined and the reported effects of splice site, 
deletion, and duplication variants.
Protein interaction analysis using NetworkX Python 
package
The NetworkX package (https:// github. com/ netwo 
rkx/ netwo rkx), a Python language-based library, was 
employed to explore and visualize complex networks 
[59]. The protein interaction data set was obtained from 
the STRING database, according to the latest NGS panel 
for each syndrome. Subsequently, a list of 50 proteins was 
created. Our model of pairwise relations between pro -
teins of this package was based on the graph theory per -
spective of NetworkX.
Fig. 2 Diagram of Data Collection. In most studies, lack of genetic evaluation was observed

Page 9 of 20
Khosravi et al. Egyptian Journal of Medical Human Genetics            (2024) 25:8 
 
Table 2 Review of Revealed Genes and Variants in Iranian Patients with EDS, OI, or CL Syndromes, up to November 2022
Syndrome Gene Mutation 
(N = novel)
Protein Reported 
disorder
Number 
of 
patients
Type of 
marriage
Genetic test Study
CL FBLN5 c.679 T > C p.Ser227Pro Autosomal 
recessive cutis 
laxa
1 Consanguine-
ous
PCR/ direct 
sequencing
Elahi et al. [11]
PYCR1 c.345delC p.Arg116fs Autosomal 
recessive cutis 
laxa type 2B
1 Consanguine-
ous
PCR/ direct 
sequencing
Nouri et al. [46]
FBLN5 c.544G > C (N) p.Ala182Pro Autosomal 
recessive cutis 
laxa
2 Consanguine-
ous
WES Gharesouran et al. 
[15]
GGCX c.373 + 3G > T (N) p.Phe73_
Gly125del
Cutis laxa 5 Undeclared WES Kariminejad et al. 
[28]
LTBP4 c.533-1G > A NA Autosomal 
recessive cutis 
laxa type 1C
1 Undeclared WES Mazaheri et al. [36]
FBLN5 c.907C > T (N) p. Gln303X Autosomal 
recessive cutis 
laxa type A1
1 Consanguine-
ous
WES Malakan Rad et al. 
[48]
PYCR1 C.797G > A p.Arg266Gln Autosomal 
recessive cutis 
laxa type 2
1 Consanguine-
ous
PCR/ direct 
sequencing
Rahmati et al. [49]
PYCR1 c.722C > A p.Ala241Asp Autosomal 
recessive cutis 
laxa type 2B
1 Consanguine-
ous
WES Nikfar et al. [45]
PYCR1 c.566C > T p.Ala189Val Autosomal 
recessive cutis 
laxa type 2B
5 Consanguine-
ous
Whole-genome 
sequencing
Vahidnezhad et al. 
[61]
RIN2 c.2251dup (N) Leu751Profs*9 RIN2 syndrome 1 Consanguine-
ous
WES Kameli et al. [26]
ATP6V0A2 c.1936_2055del p.E646_685del Autosomal 
recessive cutis 
laxa type 2
1 Undeclared PCR/ direct 
sequencing
Hucthagowder 
et al. [24]
GSN c.654G > A p.Asp187Asn Gelsolin amyloi-
dosis
1 Undeclared Undeclared Shokouhi et al. [3]
ATP6V1E1 c.383 T > C p.Leu128Pro Cutis laxa 2 Undeclared WES Van Damme et al. 
[8]
EDS PLOD1 c.1302 C > G (N) p.Thr434X Ehlers–Danlos 
syndrome 
type VI
1 Consanguine-
ous
WES Kariminejad et al. 
[27]
B3GALT6 c.619G > C p.Asp207His Recessive 
Ehlers–Danlos
1 Consanguine-
ous
PCR/ direct 
sequencing
Malfait et al. [35]
B3GALT6 c.619G > C p.Asp207His Recessive 
Ehlers–Danlos
1 Non-consan-
guineous
B3GALT6 c.649G > A p.Gly217Ser Recessive 
Ehlers–Danlos
1 Non-consan-
guineous
B3GALT6 c.323_344del // 
c.619G > C
p.
Ala108Glyfs ∗ 163 
// p.Asp207His
Recessive 
Ehlers–Danlos
2 Non-consan-
guineous
ADAMTS2 c.669_670dupG (N) p.
(Pro224Argfs*24)
Ehlers–Danlos 
syndrome
1 Consanguine-
ous
PCR/ direct 
sequencing
Van Damme et al. 
[7]
FKBP14 c.143 T > A (N) p.(Met48Lys) Kyphoscoliotic 
Ehlers–Danlos 
syndrome
1 Consanguine-
ous
PCR/ direct 
sequencing
Giunta et al. [16]

Page 10 of 20Khosravi et al. Egyptian Journal of Medical Human Genetics            (2024) 25:8 
Prediction of probable damaging variants using Iranome 
database
The reported genes of CL, EDS, and OI syndromes were 
evaluated using the Iranome Genomic Database (http:// 
www. irano me. ir/) to predict probable damaging variants. 
This database was established by whole-exome sequenc -
ing (WES) data of 800 healthy Iranian individuals from 
eight major Iranian populations, including Iranian Arabs, 
Azeris, Persians, Lurs, Baluchs, Persian Gulf Islanders, 
Kurds, and Turkmen. Iranome discovered more than 
1,500,000 variants, more than 300,000 of which were 
novel  [7, 31]. The pathogenicity of these variants was 
investigated using six tools, including SIFT, Polyphen2, 
MutationTaster, MutationAssessor, FATHMM, and 
FATHMM MKL, as listed on the Iranome Website. Here, 
the missense heterozygous alleles of all reported EDS, 
OI, and CL genes in the database were obtained; then, 
inclusion and exclusion criteria were established to pre -
dict which variant has the most probability of causing 
one of the three syndromes. The criteria are as follows: A 
variant with A) three or more times predicted as damag -
ing via the six mentioned Web servers. B) More than 10 
number of heterozygotes. C) CADD score of 20 or more.
Table 2 (continued)
Syndrome Gene Mutation 
(N = novel)
Protein Reported 
disorder
Number 
of 
patients
Type of 
marriage
Genetic test Study
FKBP14 c.2 T > G NA Kyphoscoliotic 
Ehlers–Danlos 
syndrome
1 Undeclared WES Colman et al. [6]
PLOD1 c.1471–1 G > A NA Kyphoscoliotic 
Ehlers–Danlos 
syndrome
1 Consanguine-
ous
PCR/ direct 
sequencing
Rohrbach et al. 
[52]
COL3A1 c.2194G > A p.Gly732Arg Vascular 
Ehlers–Danlos 
syndrome
1 Consanguine-
ous
WES Colman et al. [5]
B3GALT6 c.545A > G p.Tyr182Cys Spondylodys-
plastic Ehlers–
Danlos
1 Consanguine-
ous
WES Van Damme et al. 
[9]
OI FKBP10 c.976delA (N) p.
Met326Trpfs ∗ 39
Osteogenesis 
imperfecta type 
XI (Bruck syn-
drome)
1 Consanguine-
ous
WES Seyedhassani et al. 
[55]
COL1A1 c.2298 T > C (N) p.Thr766Thr Osteogenesis 
imperfecta
1 Consanguine-
ous
WES Talebi et al. [59]
COL1A1 c.3313delA (p.Arg-
1105GlufsX3
Osteogenesis 
imperfecta
1 Non-consan-
guineous
Conformation-
sensitive gel 
electrophoresis 
(CSGE)
Nwosu et al. [47]
GLUT2 C.685_701del (N) p.A229QfsX19 Osteogenesis 
imperfecta/
Fancoli–Bickel 
syndrome
1 Undeclared WES Shafaghati et al. 
[56]
FKBP10 c.1257-2A > G // 
IVS7-2A > G (N)
p.H420PfsX12 Osteogenesis 
imperfecta type 
XI (Bruck syn-
drome)
1 Consanguine-
ous
WES Maghami et al. 
[32]
COL1A2 c.14929-
14930TG > GT
NA Osteogenesis 
imperfecta
1 Undeclared PCR Moshref et al. [41]
FKBP10 c.204delCinsAAA 
(N)
p.His68Glnfs*92 Osteogenesis 
imperfecta type 
XI (Bruck syn-
drome)
1 Consanguine-
ous
WES Moravej et al. [39]
MESD c.676C > T p.Arg226 ∗ Osteogenesis 
imperfecta type 
XX
1 Undeclared WES Tran et al. [60]

Page 11 of 20
Khosravi et al. Egyptian Journal of Medical Human Genetics            (2024) 25:8 
 
Results
Data collection
Based on initial keyword research in the six search 
engines, 416, 1593, and 1748 manuscripts were found for 
CL, EDS, and IO, respectively. Further in-detailed min -
ing of papers and removing duplicated studies revealed 
that in 13, 8, and 8 manuscripts, homozygous variants of 
cases with CL, EDS, and IO were reported (Fig.  2). Sta-
tistically, 32 variants were found in 18 genes as a result 
of genetic tests in 43 patients. The novelty status of vari -
ants, reported disorders, applied genetic test, and type of 
marriage are summarized in Table 2. HGMD Professional 
2021.4 database also revealed that most of the mutations 
in these genes are missense/nonsense, splicing, and small 
deletion (Table 3).
Pathogenicity and stability of EDS/OI/CL overlap 
phenotype variants
The results of both pathogenicity and stability analysis by 
Web servers are listed in Table  4, divided into two sec -
tions—one for missense variants and another for splice 
site, deletion, and duplication variants. From eight OI 
variants, only one is missense (COL1A1: c.2298T > C). 
Three CL and one EDS variants were inconsistent with 
the reported phenotype. FBLN5: c.544G > C was found 
in two patients and, according to I-Mutant 2.0, has a 
positive effect on protein stability. The Web server also 
reported the same effect for PYCR1: c.722C > A. One 
patient with CL type 2 had PYCR1: c.797G > A, which 
was identified as benign by Polyphen2. It also reported 
FKBP14: c.143T > A as a benign variant in an EDS patient.
Protein interaction analysis using NetworkX Python 
package
A list of 50 proteins involved in EDS/OI/CL overlap phe -
notype was created using NetworkX. Figure  3 shows an 
undirected weighted graph in which the nodes and edges 
represent proteins and their interactions, respectively, so 
that each edge’s length shows the interaction score. The 
degree of the graph (defined as the average number of 
edges connected to each node) equals 4.47. NetworkX 
package applied the concept of ’betweenness centrality’ 
to the graph. It is a measure in graph theory to demon -
strate which nodes are more important (or their absence 
causes more disruption in the network) based on the 
shortest paths. In this graph, the size of the nodes indi -
cates the betweenness centrality. Also, a color range 
from dark green to white indicates the degree; greener 
nodes have more degrees (more connected edges) and 
bigger nodes have more impact on the network. More -
over, an edge with more width and greener color shows 
more interaction scores between a pair of proteins. The 
graph shows that COL1A1, COLA1A2, CRTAP , LEPRE1, 
PLOD1, and ADAMTS2 have the biggest impact on the 
protein network of the overlapping phenotype.
Table 3 Types of Mutations in Genes Involved in Overlap Phenotype of EDS/OI/CL in Iran, According to the HGMD database
Gene Missense/
nonsense
Splicing Regulatory Small deletions Small 
insertions
Small indels Gross 
deletions
Gross 
insertions
Complex Repeat Total
Mutations
ADAMTS6 6 1 – – – – – – – – 7
ATP6V0A2 20 10 – 18 7 – 3 1 – – 59
ATP6V1E1 2 – – – – – – – – – 2
B3GALT6 32 – – 7 1 1 3 2 – – 46
COL1A1 617 274 4 275 83 19 30 4 2 – 1308
COL1A2 523 69 – 28 19 6 19 2 1 2 669
FBLN5 26 – – 1 – – – 1 – – 28
FKBP14 3 – – 5 2 – – – – – 10
GGCX 52 10 – 5 1 1 – – – 1 70
SLC2A2 44 21 7 18 5 4 – 1 1 – 101
GSN 25 1 – 2 3 1 1 – – – 33
LTBP4 17 4 – 7 6 1 – 1 – – 36
MESD 1 – – 3 1 – – – 1 – 6
PLOD1 30 8 – 9 5 – 5 2 1 – 60
PYCR1 33 7 – 5 1 – 2 – – – 48
RIN2 2 – – 3 2 – – – – – 7

Page 12 of 20Khosravi et al. Egyptian Journal of Medical Human Genetics            (2024) 25:8 
Table 4 Evaluation of Pathogenicity and Effect on Protein Stability in Variants of Overlap Phenotype of EDS/OI/CL in Cohort of the Study
Gene Variant Protein ACMG Fathmm CADD SIFT POLY PHEN 2 MUpro I-Mutant 2.0
Missense variants
Cutis laxa FBLN5 c.679 T > C p.Ser227Pro Likely pathogenic Damaging (-3.01) 25.6 Damaging Probably damaging Decrease (DDG: -1.37) Decrease (DDG: -1.08)
FBLN5 c.544G > C p.A182P VUS Damaging (-2.08) 27.9 Damaging Probably damaging Decrease (DDG: -1.31) Increase (DDG: 0.68)
FBLN5 c.907C > T p. Gin303* Likely pathogenic N/A 26.7 Damaging Probably damaging (0.993) N/A N/A
PYCR1 c.797G > A p.Arg266Gln Likely pathogenic Damaging (-1.89) 33 Damaging (0.04) Benign (0.350) Decrease (DDG: -0.57) Decrease (DDG: -0.70)
PYCR1 c.722C > A p.Ala241Asp Likely pathogenic Damaging (-2.42) 26.3 Damaging (N/A) Probably damaging (1.000) Decrease (DDG: -1.07) Increase (DDG: 0.33)
PYCR1 c.566C > T p.Ala189Val VUS Damaging (-1.95) 27 Damaging (N/A) Probably damaging (0.781) Decrease (DDG: -0.75) Decrease (DDG: -0.14)
ATP6V1E1 c.383 T > C p.Leu128Pro VUS N/A 27.1 Damaging (0.03) Probably damaging (1.000) Decrease (DDG: -1.25) Decrease (DDG: -0.23)
Ehlers–Danlos B3GALT6 c.619G > C p.Asp207His VUS Damaging (-3.11) 29.4 Damaging (NA) 0 Probably damaging (1.000) Decrease (DDG: -1.18) Decrease (DDG: -0.37)
B3GALT6 c.619G > C p.Asp207His VUS Damaging (-3.11) 29.4 Damaging (NA) 0 Probably damaging (1.000) Decrease (DDG: -1.18) Decrease (DDG: -0.37)
B3GALT6 c.649G > A p.Gly217Ser VUS Damaging (-4.25) 29.5 Damaging (NA) 0 Probably damaging (1.000) Decrease (DDG: -1.03) Decrease (DDG: -1.62)
B3GALT6 c.545A > G p.Tyr182Cys VUS Damaging (-5.48) 29.5 Damaging (NA) 0 Probably damaging (1.000) Decrease (DDG: -1.17) Decrease (DDG: -0.21)
FKBP14 c.143 T > A p.(Met48Lys) VUS Damaging (-3.01) 26.1 Damaging (NA) 0 Benign (0.000) Decrease (DDG: -1.75) Decrease (DDG: -0.75)
COL3A1 c.2194G > A p.Gly732Arg Pathogenic Damaging (-5.49) 31 Damaging (NA) 0 Probably damaging (1.000) Decrease (DDG: -0.61) Increase (DDG: 0.40)
Osteogenesis COL1A1 c.2298 T > C p.Thr766Thr Benign Tolerated 10.96 Tolerated (1.00) NA N/A N/A
Gene Variant ACMG Reported protein effect MUpro I-Mutant 2.0
Splice site, deletion, and duplication variants
Cutis laxa GSN c.654G > A NA Conformational change in gelsolin protein resulted in aggrega-
tion as amyloid plaques (p.Asp187Asn)
Decrease (DDG: -0.79) Decrease (DDG: -1.57)
GGCX c.373 + 3G > T Likely pathogenic A deletion of 53 amino acids (p.Phe73_Gly125del) N/A N/A
LTBP4 c.533-1G > A NA - N/A N/A
RIN2 c.2251dup Likely pathogenic p.Leu751Profs*9 N/A N/A
ATP6V0A2 c.1936_2055del Uncertain p.E646_685del N/A N/A
PYCR1 c.345delC Pathogenic Frame shift and premature termination of translation N/A N/A
Ehlers–Danlos B3GALT6 c.323_344del // c.619G > C Pathogenic // VUS (p.Ala108Glyfs ∗ 163) // (p.Asp207His) Decrease (DDG: 
-1.87)// decrease 
(DDG: -1.18)
Decrease (DDG: -1.27) 
// decrease (DDG: 
-0.37)
ADAMTS2 c.669_670dupG Likely pathogenic p.Pro224Argfs*24 Decrease (DDG: -0.28) Decrease (DDG: -1.03)
PLOD1 c.1471-1G > A Likely pathogenic Activation of a cryptic splice site within exon 14, causing an out of 
frame deletion of the first 55 bp of exon 14 leading to a prema-
ture stop in exon 17
N/A N/A
FKBP14 c.2 T > G VUS - N/A N/A
PLOD1 c.1302C > G Likely pathogenic p.Thr434X N/A N/A

Page 13 of 20
Khosravi et al. Egyptian Journal of Medical Human Genetics            (2024) 25:8 
 
Table 4 (continued)
Gene Variant ACMG Reported protein effect MUpro I-Mutant 2.0
Osteogenesis COL1A1 c.3313delA Likely pathogenic p.Arg1105GlufsX3 N/A N/A
SCL2A2 (GLUT2) C.685_701del Likely pathogenic p.A229QfsX19 N/A N/A
FKBP10 c.1257-2A > G // IVS7-2A > G NA p.H420PfsX12 N/A N/A
COL1A2 c.14929-14930TG > GT NA – N/A N/A
FKBP10 c.204delCinsAAA Likely pathogenic p.His68Glnfs*92 N/A N/A
FKBP10 c.976delA Pathogenic p.Met326Trpfs ∗ 39 N/A N/A
MESD c.676C > T VUS p.Arg226 ∗ N/A N/A

Page 14 of 20Khosravi et al. Egyptian Journal of Medical Human Genetics            (2024) 25:8 
Iranome database reveals 46 probable disease-causing 
variants for EDS, OI and CL
A total number of 46 genes were investigated using the 
Iranome Database. They were previously reported to be 
related to CL, EDS, and OI syndromes. Searching a gene 
in Iranome provides all discovered variants—deletion, 
duplication, splice region, intronic, and single-nucleotide 
variants. Later on, missense variants of each gene were 
selected for further evaluation. Missense variants with 
more than 10 heterozygotes, a CADD score of at least 20 
(which indicates the variant is one of the 1% most del -
eterious variants in the genome) [41], and at least three 
times reported as damaging in pathogenicity Web serv -
ers are considered as probable damaging variants. From 
all evaluated genes, 46 variants in 18 genes were found 
to have a probable damaging effect. They are listed in 
Table 5, along with populations with the most and the 
least frequency of the alleles in Iran.
Fig. 3 Protein Interaction Network in EDS/OI/CL Overlap Phenotype. Using NetworkX Python Library, an Undirected Unweighted Graph 
is Visualized Based on the Betweenness Centrality

Page 15 of 20
Khosravi et al. Egyptian Journal of Medical Human Genetics            (2024) 25:8 
 
Table 5 Probable Disease-Causing Variants of EDS/OI/CL Overlap Phenotype based on Iranome Database
Syndrome Gene Variant Number of 
heterozygotes
CADD score N of 6 
damaging 
prediction
Population with the least 
frequency of allele
Population with the least 
frequency of allele
OI P3H1 (LEPRE1) c.1045G > A 77 31 6 Persian (0.025) Persian (0.025)
SERPINF1 c.395C > G 52 22 3 Baloch (0.005) Lur (0.055)
CL GSN c.385G > A 47 34 5 N/A Turkmen (0.075)
GSN c.1688C > G 67 21.8 4 N/A Azeri (0.07)
ATP6V0A2 c.440C > T 10 23.3 3 N/A Persian Gulf Islander (0.045)
ATP6V0A2 c.2438C > T 55 35 6 Lur, Persian, Turkmen 
(0.015)
Arab, Azeri, Persian Gulf 
Islander (0.07)
ALD18A1 c.1115C > A 68 24.8 4 Baloch (0.005) Arab, Kurd (0.065)
ALD18A1 c.896C > T 177 25.4 3 Baloch (0.06) Kurd (0.18)
LTBP4 c.1903C > G 10 29.6 4 N/A Turkmen (0.03)
LTBP4 c.3419C > T 388 20.7 - Kurd (0.36) Baloch (0.525)
LTBP4 c.4496A > T 23 23.4 - Turkmen (0) Arab (0.04)
GORAB c.958G > A 400 25.9 - Persian Gulf Islander (0.36) Turkmen (0.575)
PYCR1 c.685C > T 127 28.2 5 Persian Gulf Islander (0.45( Persian (0.135)
ATP7A c.2299G > C 185 26.7 5 Arab (0.285) Persian Gulf Islander (0.45(
RIN2 c.232G > A 13 28.4 5 Baloch (0) Lur (0.02)
RIN2 c.1789G > A 14 28..4 5 Baloch (0) Lur (0.02)
EDS COL3A1 c.1804C > A 23 23.2 4 Lur (0) Arab, Azeri, Persian Gulf 
Islander, Turkmen (0.02)
COL3A1 c.2002C > A 10 23.5 6 Persian, Persian gulf 
Islander (0)
Azeri, Kurd, Lur, Turkmen 
(0.01)
PLOD1 c.391G > A 31 23.1 5 Turkmen (0.005) Persian Gulf Islander (0.04)
PLOD1 c.1675C > T 10 24.2 4 Lur, Turkmen (0) Azeri (0.015)
TNXB c.12547G > A 76 33 5 Turkmen (0.01515) Persian Gulf Islander (0.1222)
TNXB c.12520G > A 89 31 6 Persian (0.0641) Tukrmen (0.25)
TNXB c.12224G > A 14 34 6 Baloch, Turkmen (0) Lur (0.02)
TNXB c.12170A > T 335 22.4 4 Baloch (0.18) Azeri (0.43)
TNXB c.11962C > A 32 23.5 4 Persian, Turkmen (0) Persian Gulf Islander (0.1316)
TNXB c.11539G > A 29 24.9 3 Turkmen (0) Azeri (0.05618)
TNXB c.10723 T > C 261 23.7 4 Turkmen (0.135) Persian Gulf Islander (0.22)
TNXB c.8740G > A 11 33 5 Arab, Lur, Azeri, Persian, 
Persian Gulf Islander (0)
Baloch (0.045)
TNXB c.8542G > A 16 28.7 5 Persian Gulf Islander, Turk-
men (0)
Baloch (0.05)
TNXB c.8111G > A 80 26.7 4 Arab (0.025) Baloch (0.115)
TNXB c.7235C > T 73 29.5 5 Arab (0.025) Baloch (0.115)
TNXB c.6379G > A 298 25.3 3 Turkmen (0.1758) Baloch (0.385)
TNXB c.2485G > A 18 25.4 3 Persian Gulf Islander (0) Arab, Lur, Persian (0.2)
TNXB c.607G > A 140 24 4 Persian Gulf Islander (0.08) Arab (0.135)
COL5A2 c.1081A > C 41 23.7 3 Kurd, Lur (0.015) Arab (0.05)
COL5A2 c.1378C > T 22 24.6 3 Azeri (0) Arab, Persian, Persian Gulf 
Islander (0.2)

Page 16 of 20Khosravi et al. Egyptian Journal of Medical Human Genetics            (2024) 25:8 
Discussion
Due to the clinical overlap between CL, EDS, and OI, it 
is difficult to provide proper follow-up care and genetic 
counseling. Their similar phenotypes increase the likeli -
hood of misdiagnosis. The phenotypic overlap is likely 
due to the functional roles and interactions of genes asso-
ciated with these syndromes. Consequently, traditional 
clinical guidelines and methods are no longer sufficient 
to differentiate between them. Whole-exome sequenc -
ing (WES) has the potential to enhance diagnostic capa -
bilities significantly. This widely used next-generation 
sequencing (NGS) method is cost-effective, requires 
fewer sequencing reagents, and enables faster bioinfor -
matic analysis compared to whole genome sequencing. 
Data collection revealed that genetic tests such as WES 
are rarely conducted in case studies, despite their poten -
tial to facilitate more precise diagnosis and more effec -
tive patient management. This study included 43 patients 
exhibiting the overlap phenotype of EDS/OI/CL, with 
a total of 32 genetic variants. Among these unrelated 
families, the rate of consanguineous marriage (CMR) 
was approximately 59%, with 12.5% reporting non-con -
sanguineous marriages and 28.5% not disclosing their 
marital status. Out of the 32 variants identified, 12 were 
previously unreported and considered novel. In approxi -
mately 94% of cases, a sequencing method (direct, whole 
exome, or whole genome) was employed, successfully 
identifying the genetic variant. Figure 4 provides a graph-
ical representation of all the reported variants in this 
cohort. Variants of PYCR1  (a protein that helps mito -
chondrial proper functioning and synthesis of proline), 
B3GALT6  (an enzyme essential for the manufacturing 
of ECM components), FKBPs  (a family of chaperons that 
perform folding on proline-containing proteins), FBLN5  
(which has a variety of roles in ECM and also play a role 
in arteries development), and collagen genes were identi -
fied in more patients than others. There were 8, 6, 5, and 
4 patients with mutations in PYCR1 , B3GALT6 , FKBPs, 
and collagen genes, respectively. The result of NetworkX 
interaction analysis also showed that these genes, along 
with ADAMTS2, COL1A1, COLA1A2, CRTAP, LEPRE1, 
FBLN5, ATP6V0A2, and PLOD1, have the most impact 
on their protein network. In addition to the direct roles 
these genes play in the production and structure of con -
nective tissues, they also exert regulatory influence over 
each other’s expression and function. This intricate net -
work of regulatory interactions highlights the complex -
ity of connective tissue homeostasis and the challenges 
in pinpointing the specific genetic defect responsible for 
each case. PYCR1, a transcription factor, orchestrates the 
expression of genes involved in collagen synthesis and 
remodeling. Mutations in PYCR1  are linked to hyper -
mobile Ehlers–Danlos syndrome (hEDS), characterized 
by loose joints and hyperextensibility, as well as Cutis 
Laxa type 2B [42]. B3GALT6, encoding beta-galactoside 
3-O-acetyltransferase, contributes to the synthesis of 
glycosaminoglycans (GAGs), essential components of 
the extracellular matrix. Deficiencies in B3GALT6 lead 
to brittle bone disease with severe skin, joint, and eye 
involvement (BBSJI), demonstrating the intricate rela -
tionship between GAGs and connective tissue health 
[37]. FKBPs, a family of heat shock protein (HSP) bind -
ers, safeguard cells from stress-induced damage. Muta -
tions in FKBP  genes are associated with Ehlers–Danlos 
Table 5 (continued)
Syndrome Gene Variant Number of 
heterozygotes
CADD score N of 6 
damaging 
prediction
Population with the least 
frequency of allele
Population with the least 
frequency of allele
COL5A2 c.1535 T > C 21 22.8 3 Persian Gulf Islander (0) Kurd (0.035)
COL5A2 c.2498C > T 22 25.9 6 Persian Gulf Islander (0) Kurd (0.04)
COL5A1 c.4135C > T 14 25.8 5 Baloch, Lur (0) Kurd (0.2)
COL5A1 c.1588G > A 61 24.9 4 Persian Gulf Islander (0.2) Persian (0.07)
DSE c.158C > T 68 28.5 3 Baloch (0.02) Turkmen (0.07)
DSE c.266G > A 12 19.57 4 Persian, Kurd (0) Arab, Baloch (0.015)
DSE c.901A > G 41 23.6 3 Turkmen (0.01) Arab, Baloch (0.05)
C1S c.356G > A 138 25.1 5 Baloch (0.035) Kurd (0.12)
COL12A1 c.9172G > A 345 27.8 6 Baloch (0.57) Turkmen (0.69)
COL12A1 c.6479A > T 35 26.8 5 Baloch (0) Kurd (0.045)

Page 17 of 20
Khosravi et al. Egyptian Journal of Medical Human Genetics            (2024) 25:8 
 
syndrome type VII, highlighting the importance of HSPs 
in connective tissue homeostasis [58]. ADAMTS2, encod-
ing a collagen-cleaving enzyme, regulates collagen fiber 
degradation, influencing tissue flexibility and strength. 
Mutations in ADAMTS2  are linked to classical Ehlers–
Danlos syndrome (cEDS), characterized by hyperexten -
sibility, easy bruising, and fragile skin [3]. COL1A1 and 
COLA1A2, encoding the alpha 1 and alpha 2 chains of 
type I collagen, the most abundant type of collagen in 
the body, are essential for connective tissue integrity. 
Mutations in these genes are associated with various 
EDS subtypes, including cEDS, dermatosparaxis, and 
osteogenesis imperfecta type VI, emphasizing the critical 
role of type I collagen in connective tissue function [18]. 
Moreover, our investigation of all reported EDS, OI, and 
CL genes using the Iranome database reveals 46 variants 
that are dormant in heterozygous carriers with different 
frequencies in each ethnic group. Considering the high 
CMR in the country, it is probable for these heterozygous 
variants to rise in the next generation as a homozygous 
form, especially for populations with a high frequency of 
disease-causing alleles [1, 15]. For example, Baloch, Ira -
nian Arab, and Kurd populations have the highest allele 
frequency for more than 6 variants of EDS. In this regard, 
carrier screening could be an effective strategy to prevent 
the birth of affected offspring [23]. Also, less than 1 per -
cent of reported patients have undergone genetic study. 
This fact, which limited our cohort number, necessitates 
Fig. 4 Schematic Illustration of Genes and Variants Involved in EDS/OI/CL Overlapping Phenotype. (Red lines show the position of variants 
at the protein domains)

Page 18 of 20Khosravi et al. Egyptian Journal of Medical Human Genetics            (2024) 25:8 
performing genetic tests on more patients in future 
studies.
The literature data on EDS, OI, and CL overlap phe -
notypes are limited and may have some biases, as 
studies may have been conducted in specific popula -
tions or may have focused on particular clinical pres -
entations. Future studies should aim to recruit more 
diverse patient cohorts and utilize standardized clini -
cal diagnostic criteria to enhance the generalizability of 
findings.
While in silico tools and databases can serve as valu -
able resources for identifying potential disease-causing 
variants, it is crucial to acknowledge their limitations. 
These tools are still under development and may not 
always accurately predict pathogenicity, particularly 
for rare or novel variants. The reliability of these pre -
dictions can be enhanced by validation through experi -
mental data, such as functional studies or animal 
models. It is important to note that the present study 
primarily encompasses the Iranian population. There -
fore, the findings may not be entirely representative of 
other ethnic or geographical groups. Future research 
endeavors should aim to investigate these phenotypes 
in a broader range of populations to enhance the uni -
versality and applicability of the results. This will con -
tribute to a more comprehensive understanding of 
EDS, OI, and CL overlap phenotypes across diverse 
populations.
Acknowledgements
Thanks to Human Genetics department of Golestan University of Medical 
Sciences for their support.
Author contributions
TK involved in methodology, investigation, formal analysis, software, visualiza-
tion, writing of original draft. KN took part in investigation, software, formal 
analysis. FV involved in methodology, investigation, writing of original draft. 
AMF took part in methodology. MO involved in conceptualization, supervi-
sion, writing (review & editing), validation, data curation.
Funding
This study was financially supported by Golestan University of Medical Sci-
ences (Grant Number: 111672).
Availability of data and materials
The datasets generated during and/or analyzed during the current study are 
available upon request.
Declarations
Ethics approval and consent to participate
The present study is approved by Ethics Committee of Golestan University of 
Medical Sciences (Code: IR.GOUMS.REC.1399.382).
Consent for publication
The consent for publication is not applicable for this study.
Competing interests
Authors of the study declared no conflict of interest.
Author details
1 Golestan University of Medical Sciences, Gorgan, Iran. 2 Congenital Malforma-
tions Research Center, Golestan University of Medical Sciences, Gorgan, Iran. 
3 Ischemic Disorders Research Center, Golestan University of Medical Sciences, 
Gorgan, Iran. 4 Department of Medical Genetics, School of Advanced Technolo-
gies in Medicine, Golestan University of Medical Sciences, Gorgan, Iran. 
Received: 6 May 2023   Accepted: 16 January 2024
References
 1. Abouelhoda M, Sobahy T, El-Kalioby M, Patel N, Shamseldin H, Monies D, 
Al-Tassan N, Ramzan K, Imtiaz F, Shaheen R (2016) Clinical genomics can 
facilitate countrywide estimation of autosomal recessive disease burden. 
Genet Med 18(12):1244–1249
 2. Alazami AM, Al-Qattan SM, Faqeih E, Alhashem A, Alshammari M, Alzah-
rani F, Al-Dosari MS, Patel N, Alsagheir A, Binabbas B (2016) Expanding the 
clinical and genetic heterogeneity of hereditary disorders of connective 
tissue. Hum Genet 135(5):525–540
 3. Colige A, Nuytinck L, Hausser I, Van Essen AJ, Thiry M, Herens C, Adès LC, 
Malfait F, De Paepe A, Franck P (2004) Novel types of mutation responsi-
ble for the dermatosparactic type of Ehlers-Danlos syndrome (Type VIIC) 
and common polymorphisms in the ADAMTS2 gene. J Investig Dermatol 
123(4):656–663
 4. Colman M, Vroman R, Dhooge T, Malfait Z, Symoens S, Burnyté B et al 
(2022) Kyphoscoliotic Ehlers-Danlos syndrome caused by pathogenic 
variants in FKBP14: Further insights into the phenotypic spectrum and 
pathogenic mechanisms. Human Mutat 43(12):1994–2009
 5. Dorgaleleh S, Naghipoor K, Khosravi T, Tadayoni Nia A, SheikhiGhayur E, 
Aziz HA, Oladnabi M (2022) Whole exome sequencing reveals the first 
c 7456C> T p Arg2486X mutation in ATM gene in Iranian population. 
Health Biotechnol Biopharma (HBB) 6(3):57–72
 6. Elahi E, Kalhor R, Banihosseini SS, Torabi N, Pour-Jafari H, Houshmand M 
et al (2006) Homozygous missense mutation in fibulin-5 in an Iranian 
autosomal recessive cutis laxa pedigree and associated haplotype. J 
Investig Dermatol 126(7):1506–1509
 7. Fattahi Z, Beheshtian M, Mohseni M, Poustchi H, Sellars E, Nezhadi 
SH, Amini A, Arzhangi S, Jalalvand K, Jamali P (2019) Iranome: A 
catalog of genomic variations in the Iranian population. Hum Mutat 
40(11):1968–1984
 8. Freedman BR, Mooney DJ (2019) Biomaterials to mimic and heal connec-
tive tissues. Adv Mater 31(19):1806695
 9. Gaubitz M (2006) Epidemiology of connective tissue disorders. Rheuma-
tology 45:iii3–iii4
 10. Gharesouran J, Hosseinzadeh H, Ghafouri-Fard S, Jabbari Moghadam Y, 
AhmadianHeris J, Jafari-Rouhi AH et al (2021) New insight into clinical 
heterogeneity and inheritance diversity of FBLN5-related cutis laxa. 
Orphanet J Rare Dis 16(1):1–13
 11. Giunta C, Baumann M, Fauth C, Lindert U, Abdalla EM, Brady AF et al 
(2018) A cohort of 17 patients with kyphoscoliotic Ehlers-Danlos syn-
drome caused by biallelic mutations in FKBP14: expansion of the clinical 
and mutational spectrum and description of the natural history. Genet 
Med 20(1):42–54
 12. Gordon MK, Hahn RA (2010) Collagens. Cell Tissue Res 339(1):247–257
 13. Greally MT, Kalis NN, Agab W, Ardati K, Giurgea S, Kornak U, Van 
Maldergem L (2014) Autosomal recessive cutis laxa type 2A (ARCL2A) 
mimicking Ehlers-Danlos syndrome by its dermatological manifestations: 
report of three affected patients. Am J Med Genet A 164(5):1245–1253
 14. Hadj-Rabia S, Callewaert BL, Bourrat E, Kempers M, Plomp AS, Layet V, 
Bartholdi D, Renard M, Backer JD, Malfait F (2013) Twenty patients includ-
ing 7 probands with autosomal dominant cutis laxa confirm clinical and 
molecular homogeneity. Orphanet J Rare Dis 8(1):1–8
 15. Hamamy H, Antonarakis SE, Cavalli-Sforza LL, Temtamy S, Romeo G, Ten 
Kate LP , Bennett RL, Shaw A, Megarbane A, van Duijn C (2011) Consan-
guineous marriages, pearls and perils: Geneva international consanguin-
ity workshop report. Genet Med 13(9):841–847
 16. Hu H, Kahrizi K, Musante L, Fattahi Z, Herwig R, Hosseini M, Oppitz C, 
Abedini SS, Suckow V, Larti F, Beheshtian M, Lipkowitz B, Akhtarkhavari 
T, Mehvari S, Otto S, Mohseni M, Arzhangi S, Jamali P , Mojahedi F, 

Page 19 of 20
Khosravi et al. Egyptian Journal of Medical Human Genetics            (2024) 25:8 
 
Najmabadi H (2019) Genetics of intellectual disability in consanguine-
ous families. Mol Psychiatry 24(7):1027–1039. https:// doi. org/ 10. 1038/ 
s41380- 017- 0012-2
 17. Hucthagowder V, Morava E, Kornak U, Lefeber DJ, Fischer B, Dimopoulou 
A et al (2009) Loss-of-function mutations in ATP6V0A2 impair vesicular 
trafficking, tropoelastin secretion and cell survival. Hum Mol Genet 
18(12):2149–2165
 18. Jobling R, D’Souza R, Baker N, Lara-Corrales I, Mendoza-Londono R, 
Dupuis L, Savarirayan R, Ala-Kokko L, Kannu P (2014) The collagenopa-
thies: review of clinical phenotypes and molecular correlations. Curr 
Rheumatol Rep 16:1–13
 19. Kameli R, Ashrafi MR, Ehya F, Alizadeh H, Hosseinpour S, Garshasbi M et al 
(2020) Leukoencephalopathy in RIN2 syndrome: novel mutation and 
expansion of clinical spectrum. Eur J Med Genet 63(1):103629
 20. Kariminejad A, Bozorgmehr B, Khatami A, Kariminejad M-H, Giunta C, 
Steinmann B (2010) Ehlers-Danlos syndrome type VI in a 17-year-old 
Iranian boy with severe muscular weakness–a diagnostic challenge? Iran 
J Pediatr 20(3):358
 21. Kariminejad A, Bozorgmehr B, Najafi A, Khoshaeen A, Ghalandari M, 
Najmabadi H et al (2014) Retinitis pigmentosa, cutis laxa, and pseudox-
anthoma elasticum-like skin manifestations associated with GGCX muta-
tions. J Investig Dermatol 134(9):2331–2338
 22. Khosravi T, Oladnabi M (2023) The role of miRNAs and lncRNAs in neurofi-
bromatosis type 1. J Cell Biochem 124(1):17–30. https:// doi. org/ 10. 1002/ 
jcb. 30349
 23. Kiseleva AV, Klimushina MV, Sotnikova EA, Divashuk MG, Ershova AI, Skirko 
OP , Kurilova OV, Zharikova AA, Khlebus EY, Efimova IA (2020) A data-
driven approach to carrier screening for common recessive diseases. J 
Pers Med 10(3):140
 24. Lin Z, Zeng J, Wang X (2019) Compound phenotype of osteogenesis 
imperfecta and Ehlers-Danlos syndrome caused by combined mutations 
in COL1A1 and COL5A1. Biosci Rep 39(7):BSR20181409
 25. Maghami F, Tabei SMB, Moravej H, Dastsooz H, Modarresi F, Silawi M et al 
(2018) Splicing defect in FKBP10 gene causes autosomal recessive osteo-
genesis imperfecta disease: a case report. BMC Med Genet 19(1):1–7
 26. Malfait F, Kariminejad A, Van Damme T, Gauche C, Syx D, Merhi-Soussi F 
et al (2013) Defective initiation of glycosaminoglycan synthesis due to 
B3GALT6 mutations causes a pleiotropic Ehlers-Danlos-syndrome-like 
connective tissue disorder. Am J Human Genet 92(6):935–945
 27. Malfait F, Francomano C, Byers P , Belmont J, Berglund B, Black J, Bloom L, 
Bowen JM, Brady AF, Burrows NP (2017) The 2017 international classifica-
tion of the Ehlers-Danlos syndromes. Am J Med Genet Part C 175:8–26
 28. Malfait F, Castori M, Francomano CA, Giunta C, Kosho T, Byers PH (2020) 
The ehlers–danlos syndromes. Nat Rev Dis Primers 6(1):1–25
 29. Mazaheri M, Jahantigh HR, Yavari M, Mirjalili SR, Vahidnezhad H (2022) 
Autosomal recessive cutis laxa type 1C with a homozygous LTBP4 
splicing variant: a case report and update of literature. Mol Biol Rep 
49(5):4135–4140
 30. McKee TJ, Perlman G, Morris M, Komarova SV (2019) Extracellular matrix 
composition of connective tissues: a systematic review and meta-analy-
sis. Sci Rep 9(1):1–15
 31. Mehrjoo Z, Fattahi Z, Beheshtian M, Mohseni M, Poustchi H, Ardalani F, 
Jalalvand K, Arzhangi S, Mohammadi Z, Khoshbakht S (2019) Distinct 
genetic variation and heterogeneity of the Iranian population. PLoS 
Genet 15(9):e1008385
 32. Moravej H, Karamifar H, Karamizadeh Z, Amirhakimi G, Atashi S, Nasir-
abadi S (2015) Bruck syndrome—a rare syndrome of bone fragility and 
joint contracture and novel homozygous FKBP10 mutation. Endokrynol 
Pol 66(2):170–174
 33. Morlino S, Micale L, Ritelli M, Rohrbach M, Zoppi N, Vandersteen A, Mac-
kay S, Agolini E, Cocciadiferro D, Sasaki E (2020) COL1-related overlap dis-
order: a novel connective tissue disorder incorporating the osteogenesis 
imperfecta/Ehlers-Danlos syndrome overlap. Clin Genet 97(3):396–406
 34. Moshref M, Khojasteh A, Kazemi B, Roudsari MV, Varshowsaz M, Eslami 
B (2008) Autosomal dominant gigantiform cementoma associated with 
bone fractures. Am J Med Genet A 146(5):644–648
 35. Murphy-Ryan M, Psychogios A, Lindor NM (2010) Hereditary disorders of 
connective tissue: a guide to the emerging differential diagnosis. Genet 
Med 12(6):344–354
 36. Naghipoor K, Khosravi T, Oladnabi M (2023) Whole exome sequencing 
identifies a novel variant in the COL12A1 gene in a family with Ullrich 
congenital muscular dystrophy 2. Mol Biol Rep 50(9):7427–7435. https:// 
doi. org/ 10. 1007/ s11033- 023- 08644-6
 37. Nakajima M, Mizumoto S, Miyake N, Kogawa R, Iida A, Ito H, Kitoh H, 
Hirayama A, Mitsubuchi H, Miyazaki O (2013) Mutations in B3GALT6, 
which encodes a glycosaminoglycan linker region enzyme, cause a 
spectrum of skeletal and connective tissue disorders. Am J Human Genet 
92(6):927–934
 38. Nouri N, Aryani O, Nouri N, Kamalidehghan B, Houshmand M (2013) Cutis 
Laxa type II with mutation in the pyrroline-5-carboxylate reductase 1 
gene. Pediatr Dermatol 30(6):e265–e267
 39. Nwosu BU, Raygada M, Tsilou ET, Rennert OM, Stratakis CA (2005) Rieger’s 
anomaly and other ocular abnormalities in association with osteogenesis 
imperfecta and a COL1A1 mutation. Ophthalmic Genet 26(3):135–138
 40. Rahmati M, Yazdanparast M, Jahanshahi K, Zakeri M (2015) Congenital 
cutis laxa type 2 associated with recurrent aspiration pneumonia and 
growth delay: Case report. Electron Physician 7(6):1391
 41. Rentzsch P , Witten D, Cooper GM, Shendure J, Kircher M (2019) CADD: 
predicting the deleteriousness of variants throughout the human 
genome. Nucleic Acids Res 47(D1):D886–D894
 42. Ritelli M, Palit A, Giacopuzzi E, Inamadar AC, Dordoni C, Mujja A, Murgude 
MS, Colombi M (2017) Clinical and molecular characterization of a 
13-year-old Indian boy with cutis laxa type 2B: Identification of two novel 
PYCR1 mutations by amplicon-based semiconductor exome sequencing. 
J Dermatol Sci 88(1):141–143
 43. Rohrbach M, Vandersteen A, Yiş U, Serdaroglu G, Ataman E, Chopra M 
et al (2011) Phenotypic variability of the kyphoscoliotic type of Ehlers-
Danlos syndrome (EDS VIA): clinical, molecular and biochemical delinea-
tion. Orphanet J Rare Dis 6(1):1–9
 44. Saadat M, Ansari-Lari M, Farhud D (2004) Short report consanguineous 
marriage in Iran. Ann Hum Biol 31(2):263–269
 45. Schmelzer CE, Duca L (2022) Elastic fibers: formation, function, and fate 
during aging and disease. FEBS J 289(13):3704–3730
 46. Seyedhassani SM, Hashemi-Gorji F, Yavari M, Harazi F, Yassaee VR (2016) 
Novel FKBP10 Mutation in a Patient with Osteogenesis Imperfecta Type 
XI. Fetal Pediatr Pathol 35(5):353–358
 47. Shafaghati Y, Sarkheil P , Baghdadi T, Hadipour F, Hadipour Z, Noruzinia M 
(2017) Osteogenesis imperfecta or Fanconi-Bickel syndrome?(report of a 
very rare disease due to new mutation on GLUT2 gene). Sarem J Med Res 
2(1):73–76
 48. Syx D, Malfait F, Van Laer L, Hellemans J, Hermanns-Lê T, Willaert A, 
Benmansour A, De Paepe A, Verloes A (2010) The RIN2 syndrome: a new 
autosomal recessive connective tissue disorder caused by deficiency of 
Ras and Rab interactor 2 (RIN2). Hum Genet 128(1):79–88
 49. Tahamtan A, Rezaiy S, Samadizadeh S, Moradi A, Tabarraei A, Javid N, 
Oladnabi M, Naeimi MH (2020) Cannabinoid CB2 receptor functional vari-
ation (Q63R) is associated with multiple sclerosis in Iranian subjects. J Mol 
Neurosci 70(1):26–31. https:// doi. org/ 10. 1007/ s12031- 019- 01395-9
 50. Talebi F, Mardasi FG, Asl JM, Bavarsad AH, Kambo MS (2017) Next-genera-
tion sequencing reveals one novel missense mutation in COL1A2 gene in 
an Iranian family with osteogenesis imperfecta. Iran Biomed J 21(5):338
 51. Tran TT, Keller RB, Guillemyn B, Pepin M, Corteville JE, Khatib S et al 
(2021) Biallelic variants in MESD, which encodes a WNT-signaling-related 
protein, in four new families with recessively inherited osteogenesis 
imperfecta. Human Genet Genom Adv 2(4):100051
 52. Vahidnezhad H, Karamzadeh R, Saeidian AH, Youssefian L, Sotoudeh S, 
Zeinali S et al (2017) Molecular dynamics simulation of the consequences 
of a PYCR1 mutation (p Ala189Val) in patients with complex connec-
tive tissue disorder and severe intellectual disability. J Investig Dermatol 
137(2):525–528
 53. Van Damme T, Colige A, Syx D, Giunta C, Lindert U, Rohrbach M et al 
(2016) Expanding the clinical and mutational spectrum of the Ehlers-
Danlos syndrome, dermatosparaxis type. Genet Med 18(9):882–891
 54. Van Damme T, Gardeitchik T, Mohamed M, Guerrero-Castillo S, Freisinger 
P , Guillemyn B et al (2017) Mutations in ATP6V1E1 or ATP6V1A cause 
autosomal-recessive cutis laxa. Am J Human Genet 100(2):216–227
 55. Van Damme T, Pang X, Guillemyn B, Gulberti S, Syx D, De Rycke R et al 
(2018) Biallelic B3GALT6 mutations cause spondylodysplastic Ehlers-
Danlos syndrome. Hum Mol Genet 27(20):3475–3487
 56. Ardalan M, Shoja M, Paunio T, Tanskanen S, Kiuru-Enari S, Rastegar A, 
et al., editors. Hereditary gelsolin amyloidosis in an Iranian family: the first 

Page 20 of 20Khosravi et al. Egyptian Journal of Medical Human Genetics            (2024) 25:8 
report from the Middle East. XIth International Symposium on Amyloido-
sis; 2007: CRC Press London & New York.
 57. Colman M, editor Further insights in the FKBP14-related kyphoscoliotic 
Ehlers-Danlos syndrome: report of 3 unrelated individuals and 2 new 
pathogenic variants2021.
 58. Giunta, C., Rohrbach, M., Fauth, C., & Baumann, M. (2019). FKBP14 
kyphoscoliotic Ehlers-Danlos syndrome.
 59. Hagberg, A., Swart, P ., & S Chult, D. (2008). Exploring network structure, 
dynamics, and function using NetworkX.
 60. Nikfar A, Mansouri M, Abhari GF. Whole exome sequencing identifies 
a homozygous pycr1 missense variant in a patient with autosomal 
recessive cutis laxa type 2b: A case report. Journal of Comprehensive 
Pediatrics. 2019;10(4).
 61. Rad EM, Zeinaloo A-A, Kariminejad A, Kornak U, Fischer-Zirnsak B, 
Mohamadpour M. Novel FBLN5 mutation of congenital autosomal reces-
sive cutis Laxa with isolated right ventricular non-compaction (RVNC): 
new findings on echocardiographic speckle-tracking strain imaging of 
RVNC. Iranian Journal of Pediatrics. 2016;26(6).
Publisher’s Note
Springer Nature remains neutral with regard to jurisdictional claims in pub-
lished maps and institutional affiliations.