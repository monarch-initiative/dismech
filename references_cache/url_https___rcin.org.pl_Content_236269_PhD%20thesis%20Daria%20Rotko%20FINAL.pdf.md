---
reference_id: url:https://rcin.org.pl/Content/236269/PhD%20thesis%20Daria%20Rotko%20FINAL.pdf
extractor_version: 1
title: "https://rcin.org.pl/Content/236269/PhD%20thesis%20Daria%20Rotko%20FINAL.pdf"
content_type: full_text_pdf
full_text_url: "https://rcin.org.pl/Content/236269/PhD%20thesis%20Daria%20Rotko%20FINAL.pdf"
---

# https://rcin.org.pl/Content/236269/PhD%20thesis%20Daria%20Rotko%20FINAL.pdf

## Content




New insights into the modulation of the mitochondrial large-
conductance calcium-activated potassium channel: interaction with
cytochrome c oxidase and carbon monoxide

by Daria Rotko

A thesis submitted for the degree of
Doctor of Philosophy in the discipline of Biological Sciences


Completed in the Laboratory of Intracellular Ion
Channels of the Nencki Institute of Experimental
Biology, Polish Academy of Sciences,
and in the Division of Neurochemistry, Institute of
Experimental Epilepto logy and Cognition Research,
Life & Brain Center, University of Bonn

Supervisors:
Supervisor: Prof. Dr. hab. Adam Szewczyk
Co-supervisor: Prof. Dr. Wolfram S. Kunz
Auxiliary supervisor: Dr. Bogusz Kulawiak

Warsaw, 2022



2






























This study was supported by the European Union’s Horizon 2020 research and innovation
program under the Marie Skłodowska–Curie grant agreement No. 665735 (Bio4Med).


3




















I would like to express my gratitude to the supervisors Prof. Adam Szewczyk,
Prof. Wolfram Kunz, and Dr. Bogusz Kulawiak, for the guidance and support
they have offered me at all stages of the preparation of this thesis.
Thank you for your dedication, sharing your expert knowledge, and providing
numerous opportunities for professional development.

I would also like to thank my colleagues from the Nencki Institute of
Experimental Biology and from the University of Bonn for the friendly and
collaborative working environment.


4




















I would like to thank my family, my partner and friends for their unwavering
support. Особлива подяка моїй мамі за всі твої зусилля та любов.

As I am writing this thesis, my homeland is being attacked by Russia in the
unprovoked and atrociously brutal war that already resulted in the deaths of
tens of thousands of innocent people and brought insurmountable suffering.
I would like to express my deepest gratitude to Ukrainian army for defending
everything I hold dear, and to everyone who is helping Ukraine in this fight.


5

TABLE OF CONTENTS

List of abbreviations ................................................................................................................... 9
1. ABSTRACT ......................................................................................................................... 11
2. STRESZCZENIE (ABSTRACT IN POLISH) .................................................................... 12
3. INTRODUCTION ................................................................................................................ 14
3.1. Biophysics of mitochondrial function ........................................................................... 14
3.2. Organization of respiratory chain complexes ................................................................ 18
3.2.1. Cytochrome c oxidase structure and assembly ....................................................... 22
3.3. Ion channels of the inner mitochondrial membrane ...................................................... 26
3.4. Mitochondrial large-conductance calcium-regulated potassium channels (mitoBK) ... 30
3.4.1. Molecular identity of mitoBK channels .................................................................. 30
3.4.2. Biophysical properties of mitoBK channels ........................................................... 32
3.5. Functional interplay between the mitoBK channels and the respiratory chain ............. 36
3.6. MitoBK channels in mitochondrial signaling ................................................................ 39
3.6.1. Mitochondrial retrograde signaling pathways ........................................................ 39
3.6.2. MitoBK channels in heme and carbon monoxide signaling ................................... 42
3.6.3. The role of mitoBK channels in cytoprotective signaling ...................................... 43
4. AIMS OF THE STUDY ....................................................................................................... 45
5. MATERIALS AND METHODS ......................................................................................... 47
5.1. Chemicals ...................................................................................................................... 47
5.2. Cellular models .............................................................................................................. 49
5.3. Depletion of mtDNA in the astrocytoma cells .............................................................. 49
5.4. Induction of COX8A deficiency in HEK293T cells with CRISPR/Cas9 ..................... 49
5.5. Nucleic acid isolation .................................................................................................... 50
5.6. Thermal cycling-based gene expression evaluation ...................................................... 52
5.7. Sanger sequencing ......................................................................................................... 55


6

5.8. High-throughput whole-transcriptome sequencing ....................................................... 56
5.9. Isolation of mitochondria from cultured cells ............................................................... 56
5.10. Western blot assessment of the amount and composition of proteins and protein
complexes ............................................................................................................................. 57
5.11. Confocal microscopy cell imaging .............................................................................. 60
5.12. Patch-clamp on the ion channels of the inner mitochondrial membrane .................... 61
5.13. Measurement of respiration of astrocytoma cells ........................................................ 62
5.14. Perfusion with CO and confirmation of the CO presence with myoglobin assay ....... 62
5.15. Determination of mitochondrial enzymatic activities ................................................. 63
5.16. Data analysis ................................................................................................................ 63
6. RESULTS ............................................................................................................................. 65
6.1. Molecular identity of mitoBK channels in human astrocytoma and fibroblast cells .... 65
6.2. Single -channel electrophysiological properties of mitoBK channels in isolated
mitochondria of astrocytoma cells ........................................................................................ 71
6.3. Analysis of interaction of mitoBK channel with the respiratory chain in the model of
mtDNA-depleted astrocytoma cells ...................................................................................... 75
6.3.1. Generation of mtDNA-depleted astrocytoma cell line ........................................... 75
6.3.1.1. Confocal microscopy imaging of the mitochondrial network of astrocytoma cells
upon mtDNA depletion ................................................................................................. 76
6.3.1.2. Determination of cellular respiration of ddC-treated astrocytoma cells .......... 77
6.3.1.3. Characterization of the expression of the mitochondrial genes in mtDNA
depleted line with RNA sequencing .............................................................................. 78
6.3.2. Analysis of complexes of mitoBK channels with the respiratory chain proteins in
astrocytoma cells ............................................................................................................... 82
6.3.2.1. Assessment of protein complexes of mitoBK channels with the respiratory chain
in astrocytoma cells ....................................................................................................... 82
6.3.2.2. Determination of mitoBK protein amount upon mtDNA depletion of
astrocytoma cells ........................................................................................................... 85


7

6.3.2.3. Transcriptome profiling in mtDNA -depleted astrocytoma cells with high -
throughput RNA sequencing ......................................................................................... 87
6.4. Evaluation of the effects of COX8A deficiency on the respiratory chain complexes and
mitoBK channels .................................................................................................................. 94
6.4.1. Characterization of the respiratory chain in COX8A-deficient fibroblasts ............ 94
6.4.1.1. Organization of the respiratory chain protein complexes upon COX8A
deficiency in fibroblasts ................................................................................................ 94
6.4.1.2. Evaluation of the protein content of the residual complex IV subunits in
COX8A-deficient fibroblasts ........................................................................................ 96
6.4.1.3. Analysis of the expression of protein subunits of complex IV and other
respiratory chain complexes in COX8A-deficient fibroblasts ...................................... 96
6.4.2. The effects of the induced COX8A deficiency on the respiratory chain in HEK293T
cells ................................................................................................................................... 98
6.4.2.1. CRISPR/Cas9 induction of COX8A deficiency in HEK293T cells................. 98
6.4.2.2. The impact of COX8A deficiency on the organization of the respiratory chain
complexes in HEK293T cells ...................................................................................... 100
6.4.2.3. Evaluation of the protein amount of the residual complex IV subunits upon
COX8A deficiency in HEK293T cells ........................................................................ 101
6.4.2.4. Analysis of the expression of protein subunits of complex IV and other
respiratory chain complexes in COX8A-deficient HEK293T cells ............................ 102
6.4.3. Estimation of the impact of the COX8A deficiency on mitoB K channels in human
fibroblasts ........................................................................................................................ 103
6.4.3.1. Assessment of the protein complexes of mitoBK with complex IV .............. 104
6.4.3.2. Evaluation of mitoBK protein amount in fibroblasts with COX8A deficiency
 ..................................................................................................................................... 105
6.4.3.3. Analysis of the expression of mitoBK subunits in fibroblasts with COX8A
deficiency .................................................................................................................... 106
6.4.3.4. Transcriptome profiling of the COX8A -deficient fibroblasts with high -
throughput RNA sequencing ....................................................................................... 108


8

6.5. Patch -clamp study of the molecular mechanisms of carbon monoxide modulation of
mitoBK channel activity ..................................................................................................... 111
6.5.1. The effects of structurally different CO -releasing molecules on mitoBK channel
activity ............................................................................................................................. 111
6.5.2. Evaluation of the CO gas modulation of mitoBK activity .................................... 115
6.5.3. Analysis of complex regulation of mitoBK channels by heme and CO gas ......... 118
7. DISCUSSION .................................................................................................................... 121
7.1. Signaling pathways activated upon mtDNA depletion in astrocytoma cells ............... 121
7.2. Molecular and functional effects of the loss of cytochrome c oxidase subunit 8A ..... 128
7.3. Interaction of the mitoBK channel with the cytochrome c oxidase ............................ 132
7.4. Mechanisms of modulation of mitoBK channels by the CO and heme signaling ....... 135
8. CONCLUSIONS AND SUMMARY ................................................................................. 139
9. LIST OF PUBLICATIONS ............................................................................................... 141
10. REFERENCES ................................................................................................................. 143




9

List of abbreviations

ADP   Adenosine diphosphate
ANT  Adenine nucleotide transporter
ATP  Adenosine triphosphate
Bp  Base pair
BK  Large-conductance calcium-activated potassium channel
BN-PAGE Blue native polyacrylamide gel electrophoresis
Cas  CRISPR-associated protein
cDNA  Complementary deoxyribonucleic acid
cGMP   Cyclic guanosine monophosphate
CO  Carbon monoxide
CORM CO-releasing molecule
COX  Cytochrome c oxidase
CRISPR Clustered Regularly Interspaced Short Palindromic Repeats
Cryo-EM  Cryogenic electron microscopy
CS  Citrate synthase
ddC  2’,3’-dideoxycytidine
DMEM Dulbecco’s modified Eagle’s medium
DMSO  Dimethyl sulfoxide
DNA  Deoxyribonucleic acid
eIF2α  Eukaryotic translation initiation factor 2 alpha
ER  Endoplasmatic reticulum
ETC  Electron transport chain
HBD  Heme binding domain
Hsp  Heat shock protein
IMM  Inner mitochondrial membrane
IMS  Intermembrane space
ISR  Integrated stress response
Kv  Voltage-gated potassium channel
MCU  Mitochondrial calcium uniporter


10

mitoBK Mitochondrial large-conductance calcium-activated potassium channel
mitoKATP Mitochondrial ATP-regulated potassium channel
mRNA  Messenger RNA
mtDNA Mitochondrial deoxyribonucleic acid
MTS  Mitochondrial targeting sequence
mtUPR Mitochondrial unfolded protein response
NADH  Reduced nicotinamide adenine dinucleotide
Nrf2  Nuclear factor E2-related factor 2
OD  Optical density
OMM  Outer mitochondrial membrane
OXPHOS Oxidative phosphorylation
PAGE  Polyacrylamide gel electrophoresis
PCR  Polymerase chain reaction
POLG  Polymerase gamma
qRT-PCR Real-time reverse transcription polymerase chain reaction
RC  Respiratory chain
RCK  Domains regulating calcium conductance
RNA  Ribonucleic acid
ROS  Reactive oxygen species
RT  Room temperature
RT-PCR Reverse transcription polymerase chain reaction
SDS  Sodium dodecyl sulfate
sgRNA Single guide RNA
TIM  Translocase of inner membrane
TM  Transmembrane domains
TOM  Translocase of outer membrane
UPR  Unfolded protein response
VDAC  Voltage-dependent anion channel
WT  Wild type



11

1. ABSTRACT

The defining property of mitochondria – generation of mitochondrial membrane potentia l –
interlinks the metabolic and signaling functions of this organelle. Mitochondrial large -
conductance calcium -activated potassium channels (mitoBK) execute its fine regulation by
allowing the controlled influx of potassium  ions into the mitochondrial mat rix. This function
endows them with unique properties, resulting in a cytoprotective phenomenon of mitoBK
activation in ischemia-reperfusion injury. The functional and structural interaction of mitoBK
channels with the electron transfer chain, and in parti cular, its terminal enzyme cytochrome c
oxidase (COX), can be one of its molecular mechanisms.
To investigate the interaction between the COX and mitoBK channels, different COX-deficient
cellular models were employed. Specifically, human astrocytoma cells  were depleted of
mitochondrial DNA (mtDNA) by the treatment with 2’,3’-dideoxycytidine. The comparison of
the protein complexes formed by the mitoBK and COX in the mtDNA -depleted and WT
astrocytoma cells identified the interaction of the pore-forming mitoBK subunit with the COX-
containing complexes and respirasomes. Furthermore, downregulation of mitoBK -α subunits
on both protein and mRNA levels occurred upon mtDNA -induced COX deficiency. The
analysis of the retrograde signaling pathways induced by the mtDNA depletion in the mtDNA-
depleted astrocytoma cells showed activation of the integrated stress response signaling.
Human dermal fibroblasts with a mutation in the structural COX subunit – COX8A – were used
as another cellular model with a deficiency in COX. The organization of the electron transport
chain was characterized in the COX8A -deficient fibroblasts and HEK293T cells with
CRISPR/Cas9 induced mutations in COX8A and ensuing COX deficiency, identifying that the
residual COX was stabilized in the respirasomes. The decrease in the protein amount of mitoBK
pore-forming subunit, as well as its protein complexes, was observed.
To follow the systemic implications of this coupling, the effect of a gaseous transmitter carbon
monoxide (CO), putatively targeting both COX and mitoBK, was assessed in the patch-clamp
studies. While direct application of CO -saturated solution has not exerted significant
modulation of the mitoBK channel activity, patch perfusion with CO -releasing molecules
induced pleiotropic effects. Perfusion with heme  and hemin inhibited mitoBK channels. The
subsequent application of CO -saturated solution released this inhibition, activating mitoBK
channels in the presence of heme.



12

2. STRESZCZENIE (ABSTRACT IN POLISH)

Podstawowa właściwość mitochondriów – generowanie potencjału w poprzek  wewnętrznej
błony mitochondrialnej – łączy funkcje metaboliczne i sygnalizacyjne tej organelli.
Mitochondrialne kanały potasowe o dużym przewodnictwie aktywowane jonami wapnia
(mitoBK) dzięki precyzyjnej regulacji ich aktywności umożliwiają kontrolowany n apływ
jonów K+ do macierzy mitochondrialnej. Dzięki unikatowym mechanizmom regulacyjnym
aktywacja kanału mitoBK indukuje mechanizmy cytoprotekcyjne w uszkodzeniu
niedokrwienno-reperfuzyjnym. Funkcjonalne i strukturalne oddziaływanie kanałów mitoBK z
łańcuchem transportu elektronów, a w szczególności z jego terminalnym enzymem oksydazą
cytochromu c (COX), może być elementem mechanizmu cytoprotekcyjnego.
Do zbadania interakcji między kanałami mitoBK oraz COX wykorzystano różne modele
komórkowe z obniżonym poz iomem tego enzymu. W ludzkich komórkach gwiaździaka
indukowano obniżenie liczby kopii mitochondrialnego DNA (mtDNA) przez traktowanie 2',3'-
dideoksycytydyną. Porównanie kompleksów białkowych tworzonych przez mitoBK i COX w
komórkach gwiaździaka z obniżoną iością mtDNA i w komórkach dzikiego typu wskazało na
możliwe oddziaływanie podjednostki tworzącej por kanału z kompleksami i respirasomami
zawierającymi COX. Ponadto, w przypadku niedoboru COX indukowanego obniżeniem ilości
mtDNA wystąpił spadek poziomu po djednostki α kanału mitoBK. Efekt ten był widoczny
zarówno na poziomie białka, jak i mRNA. Analiza szlaków sygnałowych indukowanych przez
deplecję mtDNA w komórkach gwiaździaka pozbawionych mtDNA wykazała aktywację
zintegrowanej sygnalizacji odpowiedzi na stres.
Ludzkie fibroblasty skórne z mutacją w podjednostce strukturalnej COX – COX8A – zostały
wykorzystane jako kolejny model komórkowy z niedoborem COX. W fibroblastach z
niedoborem COX8A i komórkach HEK293T z mutacjami wywołanymi CRISPR/Cas9 w genie
kodującym COX8A scharakteryzowano organizację mitochondrialnego łańcucha
oddechowego. Uzyskane wyniki wskazały, że kompleks IV w uzyskanych mutantach był
obecny w respirasomach. Ponadto, zaobserwowano zmniejszenie ilości białka podjednostki
tworzącej pory mitoBK oraz jej kompleksów białkowych.
Aby prześledzić ogólnokomórkowe implikacje sprzężenia między łańcuchem oddechowym, w
tym COX, a kanałem mitoBK, przeprowadzono doświadczenia elektrofizjologiczne. W
badaniach z wykorzystaniem techniki patch -clamp ocenion o wpływ gazowego przekaźnika
tlenku węgla (CO), przypuszczalnie oddziałującego zarówno z COX, jak i mitoBK. O ile


13

bezpośrednie zastosowanie roztworu nasyconego CO nie spowodowało znaczącej modulacji
aktywności kanałów mitoBK, o tyle zastosowanie związków u walniających CO wywoływało
efekty plejotropowe. Zastosowanie hemu i heminy hamowało aktywność kanałów mitoBK.
Wykazano, że zastosowanie roztworu nasyconego CO reaktywowało aktywność kanału
zahamowanego cząsteczkami hemu.



14

3. INTRODUCTION

3.1. Biophysics of mitochondrial function

Mitochondria are organelles of endosymbiotic origin that are present in most eukaryotic cells.
One to two billion years ago, a host related to the Asgard group of Archea acquired an α-
proteobacterial endosymbiont, what is considered to be the key evolutionary event in the origin
of mitochondria 1. Subsequent consolidation of endosymbiosis  has occurred  through the
integration of metabolic and signaling pathways between an  endosymbiont and a host . Yet
remarkably, some of the features of this primeval interaction persisted through millennia and
can be traced in the modern morphology of mitochondria of its eukaryote clade.
Firstly, despite the incremental transfer of the majority of the genes from an α-proteobacterial
endosymbiont to a proto-eukaryotic nucleus during symbiotic integration, modern
mitochondria have retained their genome and translation machinery with certain properties
characteristic of its α-proteobacterial ancestor. Mitochondrial DNA ( mtDNA) in mammalian
cells is circular, devoid of introns, and contains 37 genes encoding 22 tRNAs, 2 rRNAs, and 13
subunits of multiprotein oxidative phosphorylation (OXPHOS) complexes. Interestingly, there
is a substantial diversity of mitochondrial genom e between eukaryotic groups 2, and due to its
rapid evolution rate, mitochondrial DNA (mtDNA) is considered to b e one of the drivers of
evolution 3.
Secondly, mitochondria possess a double membrane -bound structure with four functionally
different compartments: the outer mitochondrial membrane (OMM) stemming from an
endosymbiont-engulfing envelope, the intermembrane space (IMS), the  inner mitochondrial
membrane (IMM) originating from an α-proteobacterial membrane, and the mitochondrial
matrix enclosed by IMM. In the process of endosymbiotic integration, structures similar to
intracytoplasmic membranes of α-proteobacteria have likely evolved into morphologically
distinct folds of IMM – the cristae, thus providing an additional level of compartmentalization
4. Such a peculiar morphology has facilitated the evolution of highly efficient bioenergetic and
metabolic OXPHOS processes in mitochondria (Figure 1).


15


Figure 1. Mitochondrial physiology endows this org anelle with various functions.
Mitochondria are double-membrane organelles that possess mtDNA and contain  four distinct
compartments: outer mitochondrial membrane, intermembrane space, inner mitochondrial
membrane, and matrix. Numerous processes occurring in mitochondria are associated with this
structure, including mitochondrial protein import, respiration, calciu m ion buffering, and
quality control of mitochondrial proteome.

Russell’s concept of the origin of life at alkaline hydrothermal vents dates the evolution of the
first electron transport systems at the emergence of complex biological processes 5. According
to this hypothesis, alkaline vents there were, in essence, functioning like bioreactors: providing
a compartmentalized surface with a constant supply of molecular hydrogen, c arbon dioxide,
and clay minerals, thus catalyzing the formation of the first biopolymers four billion years ago.
Another peculiarity of the hydrothermal vents was their alkalization compared to the generally
acidic environment of CO 2-rich oceans, estimated  to differ by up to 4 pH units. Thus, the
anticipated proton gradient of  the positively charged environment versus the alkaline inner
compartment could prompt the evolution of the first electron transport systems.



16

According to the chemiosmotic Mitchell th eory, energy synthesis via OXPHOS requires the
initial generation of a gradient of electrochemical potential. Following oxidation of respiratory
substrates by the electron transport chain (ETC) complexes I and II harbored in the IMM, the
entailed activity of the proton pumps of ETC complexes I, III , and IV generates the
electrochemical H+ gradient across the IMM (ΔμH+). ΔμH + consists of the electric component,
ΔΨM, and the proton concentration gradient, ΔpH:
𝛥𝜇𝐻+ =  −𝐹∆𝛹𝑀 + 2.3∆𝑝𝐻
where F is the Faraday constant.  Mitochondrial ΔμH+ is next dissipated by the movement of
protons through ATP-synthase residing across the IMM and is thereby harnessed as the driving
force for ATP synthesis by this protein complex. ETC activity generates as byproduct reactive
oxygen species (ROS) : superoxide (O 2●−) and hydrogen peroxide (H 2O2), which have a
signaling role under control led physiological conditions but are linked to pathology  when
overproduced 6.
Besides its role in oxidative phosphorylation, maintenance of mitochondrial membrane
potential ΔΨM is crucial for other processes of mitochondrial physiology. Due to the charge
separation, the matrix side of IMM is highly negatively charged, and in the physiological
conditions, ΔΨM values are estimated to reach from -140 to -200 mV. Consequently,
mitochondrial membrane potential acts as a driving force for the Ca 2+ and Fe2+ uptake by the
electrogenic transporters of IMM. Besides a buffering function, changes in Ca2+ concentration
control mitochondrial substrate oxidation and respiration t hrough regulation of mitochondrial
dehydrogenases and complex IV of ETC. The uptake of Fe 2+ is necessary for the synthesis of
iron-sulfur clusters  in mitochondria , which are the cofactors of numerous metalloproteins
involved in electron transport and catalysis.
In the course of proto-mitochondrial genesis, crucial adaptive events involved the insertion of
metabolite transporter  proteins into the IMM. The modern mitochondrial carrier family
comprising a plethora of solute transporters in the IMM is estimated to origina te from a single
adenine nucleotide transporter (ANT) 7. The equimolar exchange of ADP from the cytosol for
matrix ATP facilitated by ANT has a net positive (+1) charge and is driven by the ΔΨM.
The development of mitochondrial protein import machinery, which was likely initially allotted
to facilitate the insertion of the protein transporters , became another key symbiotic event in
mitochondrial evolution . According to the MitoCarta2.0 study,  the current mitochondrial
proteome in humans and mice is comprised of 1158 proteins, and only 13 of them are encoded


17

by mtDNA 8. The rest of the mitochondrial proteins are encoded in the nucleus, and in order to
reach the proper mitochondrial compartment, coordinated peptide targeting, recognition  and
translocation systems are necessary.  In certain protein import pathways, the mitochondrial
protein targeting by transporter proteins is electrogenic and requires ΔΨM 9. Specifically, it has
been estimated that up to 70% of mitochondrial proteins possess an N -terminal mitochondrial
targeting sequence (MTS) consisting of up to 55 amino acids that form an amphipathic α-helix
with a net positive charge (from +3 to +6) 10. The MTS is recognized by the translocase of outer
membrane (TOM)  proteins TOM20 and TOM22 and is next transported through the TOM
complex. In the proteins destined for IMM, a peptide is thereupon electrophoretically pulled by
the MTS through the translocase of inner membrane (TIM) proteins TIM22 or TIM23.
Therefore, the generation of membrane potential may be considered the defining biophysical
property of mitochondria, which interlinks their metabolic and signaling functions. In order to
maintain ΔΨM, the permeability of IMM to ions is strictly controlled. The plethora of
mitochondrial proteins that regulate ion transport through IMM is comprised of mitochondrial
metabolite and ion transporters, uncoupling proteins, and mitochondrial ion channels: K+, Ca2+,
Mg2+, and Cl- channels. By enabling fine control over the mitochondrial ΔΨM, mitochondrial
potassium channels act as important regulators of mitochondrial functions.



18

3.2. Organization of respiratory chain complexes

Oxidative phosphorylation is a metabolic pathway of aerobic generation of ATP that employs
five protein complexes (in mammalian cells) embedded in the inner mitochondrial membrane.
Four of these protein complexes are involved in the electron transport and are termed the
respiratory chain (RC), or electron transport chain (ETC), consisting of:
- complex I (CI) - NADH: ubiquinone oxidoreductase,
- complex II (CII) - succinate: ubiquinone oxidoreductase,
- complex III (CIII) - cytochrome bc1 complex,
- complex IV (CIV) - cytochrome c oxidase,
- two mobile electron carriers - coenzyme Q and cytochrome c 11.
The respiratory substrates - NADH or succinate - are supplied to the RC by mitochondrial
substrate oxidizing  activity, specifically the Krebs cycle. The RC enzymes subsequently
catalyze a series of redox reactions that drive the transfer of electrons down the electrochemical
gradient from CI or CII through CIII and terminate in the CIV, which reduces molecular oxygen
to water. The ensued decline in the redox potentials of the CI, CIII , and CIV promotes t he
translocation of protons across the IMM. Complex V (CV) – ATP synthase – then harnesses
the generated transmembrane proton gradient for chemiosmotic ATP synthesis.
In mammalian cells, OXPHOS is the only metabolic network that is comprised of the proteins
encoded jointly by the nuclear and mitochondrial genomes. While the majority of these proteins
are the products of the nuclear genome, the few mtDNA-encoded subunits of the electron chain
CI, CIII, CIV, and ATP synthase CV are essential to the electron transport and OXPHOS. Since
each RC protein complex contai ns highly redox -active cofactors within their structure, the
assembly between the cofactors, nuclear - and mitochondrial-encoded subunits proceeds in a
highly controlled manner involving specific assembly factors  12. Regulation of the ETC
biogenesis by the availability of the subunit-encoding transcripts and their products introduces
another layer of complexity to this intricate process.
The o rganization of the OXPHOS complexes in the IMM has been a subject of extensive
research. An early “fluid” model postulated that the RC complexes were residing in the IMM
independently as separate entities and interacted by random collision evoked by thei r lateral
diffusion in the IMM 13. However, recent studies of structural and functional characteristics of
the ETC have demonstrated that RC complexes can arrange into defined supramolecular


19

assemblies stabilized by the weak interactions that coexist with the individual complexes. The
dynamic nature of the ETC organization is reflected by different stoichiometries of such RC
protein supercomplexes: a dimer of complex III interacting with complex IV (III 2 + IV),
complex I in association with a dimer of complex III (I + III 2), and a supercomplex termed
respirasome that consists of complex I, a dimer of complex III and complex IV (I + III 2 + IV)
14,15. A respirasome can be considered the minimal discreet entity that possesses the full
functionality of ETC.
The molecular architecture o f respirasome was solved in the recent cryogenic electron
microscopy (cryo-EM) studies 11,16,17 (Figure 2). In mammalian mitochondria, supercomplexes
are located on the “ flat” sides of cristae, which can be topologically relevant in the events o f
cristae remodeling 18. Although the interaction between complexes within the respirasome is
nonrestrictive, their close positioning minimizes the distance required for the diffusion of
mobile carriers 19. Notably, the organization of this supramolecular complex is nonrandom: the
membrane “leg” of complex I wraps  around the dimer of complex III, while complex IV is
positioned between them  11,16,17. Most of the RC subunits involved in the stabilization of the
supercomplexes are supernumerary – they are not essential for enzymatic activity and have
been a later evolutionary addition to the catalytically active part 17.
While the RC complexes exist in both discrete and respirasome -bound forms, there is no
absolute requirement for them to associate in to supercomplexes for respiration to proceed  20.
However, the defined stoichiometries of supercomplexes conserved b etween different species
indicate that such supramolecular entities confer certain evolutionary benefits to the ETC
organization. Thus, several possible functions of the respiratory supercomplexes have been
proposed 20,21.
The close spatial proximity of the ETC complexes might facilitate efficient electron transport.
The IMM has one of the highest protein -to-lipid ratios among biological membrane s, and the
assembly of ETC complexes into higher -order structures could avoid unfavorable protein
interactions in this environment 19. Respirasomes may structurally mitigate ROS synthesis, in
particular by complex I since the access of the molecular oxygen to the multiprotein-clad redox-
active centers of the complex I would be physically hindered 22. However, a hypothesis that
respirasomes have a potential catalytic advantage through channeling a local pool of ubiquinone
between the ETC complexes has been recently refute d by a study demonstrating that its
availability to the competing enzymes isn’t decreased 21,23.



20


Figure 2. The electron transfer reactions through complexes I, III and IV are shown
within the molecular arch itecture of the mammalian respirasome  24. Following the
oxidation of NADH, complex I (protein structure illustrated in blue) catalyzes the reduction of
ubiquinone (Q) to ubiquinol (QH 2). QH2 is then oxidized by complex III (in green), resulti ng
in cytochrome c reduction (in orange). The terminal reduction of molecular oxygen to water
occurs as a result of two successive cytochrome c oxidation reactions catalyzed by complex IV
(in pink). Reprinted by permission from Springer Nature: Springer Nature, Nature Structural &
Molecular Biology, reference 24, copyright 2017.

A particularly interesting potential role of respirasomes is providing a scaffold for individual
RC complexes in the event of RC deficiencies and impaired nuclear-mitochondrial coordination
of ETC biogenesis. In the studies of the RC organization with the com plex I, III , and IV
deficiencies, the architecture of respirasomes was shown to stabilize the individual protein
complexes and provide compensatory effects 25–27.
Respirasomes can serve as  a physical p latform for signaling between complexes  since the
metabolic and oxidative state of the ETC can be reflected in the  dynamic balance and ratio of
supercomplexes to discrete RC complexes, as well as  their composition. It may provide an



21

additional layer of physiological feedback on the state of individual complexes, rendering the
respirasomes indicators of the ETC functional state.



22

3.2.1. Cytochrome c oxidase structure and assembly

Cytochrome c oxidase (COX) is the terminal enzyme (EC 1.9.3.1) of the ETC, which catalyzes
the transfer of the electrons from cytochrome c to oxygen in the rate-limiting reaction of ETC
– the reduction of molecular oxygen to water:
O2 + 4e− + 4H+ → 2H2O
Oxidation of one O 2 molecule requires 4 sequential events of binding the electron donor –
reduced cytochrome c – to COX. This reaction is also coupled to the transfer of  protons
contributing to the generation of a mitochondrial electrochemical gradient. During one cycle of
activity of COX, eight protons are translocated from the matrix : four of them are used in the
reduction reaction, and the remaining four are pumped out into the IMS.
In mammalian cells, t he holoenzyme of COX is comprised of an apoenzyme containing 14
protein subunits and prosthetic groups involved in the redox center formation: two heme groups
– heme a and heme a3, and two copper ions – CuA and CuB. While heme a is fully ligated to
four histidine residues, heme a3 has one spare coordination position that can bind molecular
oxygen or COX inhibitors such as carbon monoxide (CO), cyanide, and azide.
The catalytic core of COX is formed by the three highly hydrophobic transmembrane subunits
that are encoded by the mitochondria l DNA: COX1 and COX2, which incorporate prosthetic
groups, and COX3. A cytochrome c - docking pocket is located on the N -side of COX2 in
proximity to the two copper ions of the Cu A center. The electrons from cytochrome c are
initially accepted by the CuA center and are transferred to the heme a bound to COX1. After the
subsequent transfer of electrons to the binuclear CuB - heme a3 center containing a bound and
split O2 molecule, the reduction of oxygen to water occurs . Interestingly, while COX directly
interacts with molecular oxygen, it generates a relatively low amount of ROS: a fully functional
COX is estimated to produce superoxide anion (O2•−) in a mono-electronic reaction out of only
1-3% of oxygen 28.
The remaining eleven protein subunits of COX are encoded by the nuclear genome:  COX4,
COX5A, COX5B, COX6A, COX6B, COX6C, COX7A, COX7B, COX7C, COX8A, NDUFA4
(also known as COXFA4). The nuclear -encoded subunits do not directly partic ipate in the
catalytic reaction but are instead involved in the assembly, stabilization and regulation of COX.
Biogenesis of COX is a highly controlled process, which is regulated by  more than thirty
nuclear-encoded assembly factors that are involved in the membrane insertion of the proteins,


23

synthesis and delivery of prosthetic groups and cofactors  29. The initial linear model of COX
assembly postulated it as a stepwise process of incorporation of the individual protein subunits
into the assembly intermediates 30. However, an updated modular model was proposed recently,
which described COX assembly as a modular process  31. According to this model, the initial
protein seed is formed around subunits COX4 and COX5A with an assembly factor HIGD1A,
which is then joined by COX1 with accompanying chaperones forming the first COX module.
Two additional protein modules assemble  around the remaining catalytic core COX subunits,
each containing supernumerary subunits with a set of assembly factors : a COX2 module
containing subunits COX5B, COX6C, COX7B, COX7C, COX8, and a COX3 module
containing subunits COX6A, COX6B, COX7A, with NDUFA4 being added last 32 (Figure 3).



Figure 3. A schematic illustration of the assembly of COX structural subunits according
to the modular assembly model.  COX1 (MT-CO1) joins the protein seed formed by subunits
COX4 and COX5A. Two other COX assembly modules are formed around the remaining
catalytic core  subunits: COX2 (MT -CO2) module  and COX3 (MT -CO3) module.  The
schematic depiction of the COX subunits is based on the structural data deposited in the Protein
Data Bank under entry 5Z62, as reported by Zong et al. (2018) 33.

COX can exist in two forms in the IMM as a functional enzyme: either discretely as a singular
CIV or its homodimer (CIV2), or as a part of the supercomplex with the dimer of complex III
(CIII2-CIV) or a respirasome containing  complex I, complex III dimer and complex IV (CI-



24

CIII2-CIV) 34. The structural data obtained with cryo -EM show that COX is incorporated into
the supercomplexes as a monomer 35. However, whether COX is incorporated into the
supercomplexes as a fully assembled enzyme or at its subassemblies stages is still an open
question, with different studies supporting both pa thways 29. Certain super numerary COX
subunits are involved in the formation of the supercomplexes. Specifically, subunits COX8 and
COX7C are directly interacting wit h complex I in the respirasomes. T he subunit COX7A
interacts with complex III subunits , and the subunit COX6A1 is also implicated in the
stabilization of COX with in this supercomplex  36. An isoform of COX7A - COX7A2L,
containing both complex I and complex III contact site s, has a key role in the stabilization of
respirasomes.
Regulation of COX activity is a complex process that occurs on different levels. Firstly, a
number of  supernumerary subunits are expressed in a tissue-specific manner to optimize
electron transfer in response to the  different metabolic and environmental conditions 37.
Secondly, the expression of COX4 isoforms COX4 -1 and COX4 -2 is regulated by oxygen
availability under transcriptional control th rough a hypoxia inducing factor 1 (HIF-1) 38.
Moreover, COX can modulate the activity of other ETC complexes in a respirasome under
hypoxia: a transcriptional induction of NDUFA4L2 – a hypoxia-induced isoform of NDUFA4
– by HIF-1 decreased the activities of both complexes I and IV by a molecular mechanism that
remains to be elucidated  39. Thirdly, a llosteric regulation of COX by the change in the
ADP/ATP ratio controls a  crucial step in the electron transfer activity: the binding affinity of
cytochrome c to COX 2 is decre ased following the binding of ATP to the ma trix-exposed
domains of the COX 40. Fourthly, various types of post-translational modifications of COX that
exhibit a modulatory effect on its activity  have been reported, including phosphorylation ,
methylation, acetylation, nitrosylation, and sulfoxidation 41.
While impairments in the mtDNA maintenance machinery can negatively affect  OXPHOS,
COX deficiencies sensu stricto caused by the defects in assembly and/or function  of COX are
classified as a distinct class of mitochondrial disorders. Genetic conditions of different severity
leading to COX deficiencies have been reported, including mutations in COX assembly factors
and structural subunits of mitochondrial as well as nuclear origin 35. Moreover, patients with
mutations in mtDNA -encoded subunits may have mitochondrial he teroplasmy in different
tissues, which further complicate s the clinical picture. Due to such heterogeneity, COX
deficiency can have different clinical manifestations and lethality, although certain biochemical
and physiological patterns are commonly observed. These may include myopathy and acidosis


25

in skeletal and cardiac muscle tissue, neurological disorders of the central nervous system such
as Leigh syndrome, and multi-system disorders such as French-Canadian type Leigh syndrome,
which affects the brain, skeletal muscle and liver 42–44.


26

3.3. Ion channels of the inner mitochondrial membrane

Due to the essential role of the mitochondrial membrane potential  in mitochondrial function ,
tight regulation of ion permeability of the IMM is required for the maintenance of bioenergetics
and mitochondrial signaling. Under physiological conditions, modulation of m itochondrial
membrane potential is largely performed by six ions that cross the IMM: H+, K+, Ca2+, Cl-, Na+,
and Mg2+. Ion fluxes are dependent on the mitochondrial membrane  potential and gradients
across the IMM, which are vastly different for each ion species (Table 1). Considering the scope
of this work, the focus of this chapter  will be limited to mitochond rial potassium ion
homeostasis. For the discussion on the remaining ion fluxes in mitochondria, the reader can be
directed to a comprehensive review 45.
Table 1. Concentrations of selected inorganic ions  in different cellular compartments 46–
48.
 Extracellular Cytosolic Matrix
K+ 4 mM 150 mM 150-180 mM
Ca2+ 1 – 2 mM 10-7 – 10-6 M 10-7 – 10-4 M
Na+ 140 mM 8 mM 6 mM

The OMM is highly permeant to K+ due to a high density of voltage-dependent anion channels
(VDAC) containing an approximately 1 nm large pore that can conduct both anions and cations
within its β-barrel structure 49. While the primary function of TOM40 is to facilitate
mitochondrial peptide transport, its transmembrane pore has ion-conductive properties as well
50. However, in the IMM the K+ permeability is tightly regulated. The report on the activity of
ATP-regulated K+ channels in the IMM (mitoKATP) in 1991 was a pioneering work that has led
to a burst of research in the field of the mitochondrial potassium channels 51. Thirty years later,
K+ channels are recognized as  the largest group of ion channels in mitochondria, with eight
types of mitochondrial K + channels having been identified to date.  It is important to consider
that the K+ channel density in the IMM is estimated to be low, and since their expression is
tissue-specific, only certain mitochondrial potassium channel types are present in a
mitochondrion of a given cell type.
The influx of potassium ions into the mitochondrial matrix after an opening of the K+ channels
follows the electrochemical K + gradient across the IMM. The 150 mM concentration of K+ in


27

the mitochondrial matrix is close to the equilibrium with the K+ concentration in cytosol and
IMS. The K+ traffic inside the matrix is driven primarily by the strong electric component of
the electrochemical gradient – the negative mitochondrial membrane potential ∆ΨM= -180 mV
(on average) , what sets mitochondrial K + channels apart from their plasma membrane
counterparts. The influx of K + is accompanied by the entry of osmotically obli gated water
through aquaporins causing mitochondrial swelling. To maintain the potassium ion equilibrium,
accumulated K+ is then extruded from the matrix by the activity of the K+/H+ antiporter, which
leads to H + reentry into the matrix and a decrease in mitochondrial volume. This process is
termed a futile potassium cycle 52.
Unlike the plasma membrane channels, the opening of potassium channels in the IMM results
in mild mitochondrial depolarization. Thus, activation of a large-conductance calcium-activated
potassium channel that has the highest conductance among the mitochondrial K + channels –
approximately 300 pS – is estimated to decrease the ∆ΨM  by about 3 mV 53. The potassium
entry inside the mitochondrial matrix stimulates the activity of ETC, increasing proton pumping
and respiration, and regulates matrix volume and generation of ROS 54,55.
Mitochondrial potassium channels are frequently referred to as the “mirror image” of the
plasma membrane potassium channels since many of them are encoded by the same genes. The
residence of the K+ channels in the unique mitochondrial proteomic, lipid and signaling milieu,
on the other hand,  endows them with a special role in the mit ochondrial signaling networks.
Yet despite advances in the research field, the molecular identity of most mitochondrial channel
isoforms remains unknown , and structural data are instead inferred from their plas ma
membrane counterparts with similar pattern s of activity and responses to the channel
modulators.
While K + channels are a structurally diverse  protein family , they share a high degree of
conservation in the transmembrane pore region, which is thought to have originated from a
common evolutionary ancestor of both eukaryotic and prokaryotic K + channels, possibly of
viral origin 56,57. This structural module consists of two transmembrane domains (TM) and an
α-helix containing the signature amino acid sequence of K+ selectivity filter – TVGYG 58. Gene
duplication and fusions have resulted in greater diversity in the composition of mitochondrial
and plasma membrane K + channels, as well as additional molecular mechanisms controlling
their opening 56.
The voltage -gated group of mitochondrial potassium channels inc ludes mitoKv1.3 of the
Shaker family, mitoKv1.5 and mitoKv7.4 channel s 59. The functional form of the mitoKv


28

channels, based on the similarity of their recorded activity to the plasma membra ne voltage-
gated channels, is likely a tetramer of 6-TM subunits. Each of them contains a 4-TM voltage-
sensing domain (VSD) with a positively charged S4 helix, which is attached to a core 2 -TM
pore domain. Membrane depolarization increases the activity of mitoKv channels.
MitoKv1.3 channels were identified in the IMM of neurons, macrophages, lymphocytes, and
several cancer cell lines: Colo357 pancreatic ductal adenocarcinoma cells, PC-3 prostate cancer
cells, B16F10 melanoma cells  60. Pharmacological modulation of mitoKv1.3 has been
investigated in the context of prospective antitumor therapy 61. MitoKv1.3 channels are
implicated in apoptotic pathway regulation, as the pro -apoptotic fact or Bax interacts with
mitoKv1.3 and inhibits these channels . Heterotetrameres consisting of mitoKv1.5 and
mitoKv1.3 can be formed in the macrophages, where they are linked to the apoptotic signaling
as well 62. MitoKv7.4 channels were identified in the mitochondria of rat cardiac and neuronal
cells, and their activation was shown to be cytoprotective in the ischemic heart injury 63.
Three types of mitochondrial K+ channels are modulated by calcium ions, transducing signals
about the changes in mitochondrial Ca 2+ concentration to the ΔΨM: large -conductance K +
channel, mitoBK, intermediate-conductance K + channel, mitoIK, and small -conductance K +
channel, mitoSK. To provide an accurate feedback signal, Ca 2+ activation thresholds and K +
conductance values differ between these channels.
MitoBK channel is jointly regulated by the IMM  voltage and Ca 2+ binding. A minimal
functional mitoBK channel consists of a tetramer of 7-TM pore-forming subunits, and the Ca2+
sensitivity of mitoBK is conferred by the Ca 2+-binding domains within a C-terminal region of
their pore subunits. Unlike mitoBK, mitoIK and mitoSK are not voltage -gated, and their Ca 2+
sensitivity is conferred by calmodulin associated with the calmodulin-binding domain at the C-
terminus of their 6-TM subunits.
Two-pore-domain K+ channels structurally form a dimer of subunits with a duplicated core 2-
TM pore region. A mitochondrial form of the TWIK -Related Aci d-Sensitive K + Channel 3
(mitoTASK-3) was identified in HaCaT keratinocytes and melanoma cells. MitoTASK -3
activity is controlled by the changes in pH, as it shifts from being active at pH 7.4 to inhibition
upon acidification.
The identity of the mitoKATP channel has been disputed. While a body of research focused on
the mitochondrial isoform of inward-rectifying of Kir1.1b as a potential candidate , a recent
report linked mitoKATP to a 2-TM coiled-coil domain-containing protein 51C (CDC51) protein


29

64, which is yet to be fully characterized . A model assuming the tetrameric organization of
mitoKATP containing a tetramer of pore -forming CCDC51 subunits, each associating with an
ATP-binding subunit, h as been proposed. Interestingly, another study has  recently
demonstrated that the ATP synthase complex can function as a K+-conductive entity with same
biophysical and pharmacological properties as mitoKATP channels, thus proposing it as a new
contender for its molecular identity 65.
The evidence of mitochondrial localization was reported for the sodium-activated potassium
mitoKNa1.2 in cardiomyocytes 66. These channels are heterotetramers of pore-forming subunits
containing 7-TM domains, an ATP-binding cassette, and a Na+-binding region in the C-terminal
part. The physiological significance of the Na+ and Cl--regulated activation of the mitoKNa1.2
channels remains unknown. However, t hese channels are implicated in th e modulation of
mitochondrial metabolism, and their activation by volatile anesthetics confers cardioprotection
in the ischemia-reperfusion injury.



30

3.4. Mitochondrial large-conductance calcium-regulated potassium
channels (mitoBK)

3.4.1. Molecular identity of mitoBK channels

The functional mitoBK channel is formed by a tetramer of  the pore-forming BK-α subunits,
which can associate with the regulatory BK-β subunits. The α subunit  of mitochondrial and
plasma membrane BK channels  is encoded by the KCNMA1 gene. Interestingly, KCNMA1 is
rather conserved among eukaryotic species - a Clustal Omega alignment of the canonical amino
acid sequences indexed for mammalian (human, mouse, rat, rhesus mac aque, dog, pig), avian
(chicken) and amphibian (A frican clawed frog) sp ecies displays ~74% amino acid similarity.
In mammals, KCNMA1 is widely expressed in both excit able and non -excitable cells.  The
presence of the mitoBK channel in particular was reported in mammalian endothelium 67, brain
68, heart 69, skeletal muscle 70, and fibroblasts 71. Mitochondrial BK channel orthologues were
also identified in potatoes 72 and a protozoon amoeboid 73.
According to the database GTEx (release V8) , i n human cells, KCNMA1 is located on
chromosome 10 in region 10q22.3 and contains 57 exons. Therefore, alternative splicing of
KCNMA1 transcripts is the major source of structural variability of the BK channels. As a case
in point, 94 transcripts of the human KCNMA1 were listed in the Ensembl database (release
106), and 66 of them were indexed as protein-forming. However, the high-resolution proteomic
studies typically detect only the small peptide fraction of  all determined alt ernative s plice
variants. Thus, whether all splice variants have functional significance or are translated at all is
a matter of discussion 74. In addition, hundreds of single nuc leotide polymorphisms in the
human BK-α subunit were reported, further contributing to the genetic heterogeneity of BK
channels 75.
A splice variant of the BK-α subunit named VEDEC after the final amino acids of its distinct
C-terminal 50 amino acid signature  is sometimes suggested to be a mitochondria -specific
isoform of BK channels . This observation holds true for the mitoBK channels of mice
cardiomyocytes, where VEDEC was shown to be exclusively targeted to the mitochondria  76.
In HEK293T cells that were heterologously expressing a VEDEC isoform, the presence of BK
channels was observed in mitochondria and endoplasmic reticulum  77. On the contrary, a
VEDEC isoform was specifically localized to the endoplasmic reticulum  in COS 7 cells 78.
Interestingly, another study did not detect the presence of VEDEC isoforms in human


31

astrocytoma cells with confirmed mitoBK channel activity 79. In the N2a neurons, the VEDEC
isoform of BK -α subunits was processed through the endoplasmic reticulum, and the S-
acylation status of the partner BK-β4 subunit determined whether the VEDEC isoform was
retained in the ER or was trafficked to the cell membrane surface 80.
The databases GTEx (release V8) and Ensembl (release 104) show that the canonical splice
variant SAKCA of KCNMA1 in human cells is composed of 28 exons and incorporates an exon
#55 of KCNMA1 as last at its 3’-terminus (Figure 4). Alternatively, the KCNMA1 transcripts
ending with an exon # 57 produce splice variants VYR, VEDEC, or peptides containing a
premature stop codon and subjected to nonsense-mediated decay. The databases GTEx (release
V8) and Ensembl (release 104) list ed 39 KCNMA1 transcripts containing the exon #57 .
Mapping of these transcript models to the corresponding amino acid sequences obtained from
the UNIPROT database (release 2022_01) identified 16 transcripts producing isoforms with a
VEDEC terminal signature that differed in their exon composition and had a varying length of
the encoded 3’ -UTR. Therefore, the VEDEC isoform should be regarded as a group of
transcripts with similarities in the C -terminus, and their structural heterogeneity may account
for the reported different observations. By and large, while in certain cell types VEDEC is
localized to mitochondria as mitoBK, a sole presence of this  terminal amino acid signature
within the BK-α subunit might be not sufficient for universal mitochondrial targeting, and other
molecular mechanisms may be involved. Indeed, the codon bias introduced by the synonymous
codons encoding the alternative splicing products with similar amino acid sequences was shown
to direct the sorting of the potassium channels either to mitochondria or the secretory pathway81.


Figure 4. A gene model  based of KCNMA1 and exon expression in  two transcripts: a
canonical SAKCA isoform and one of the VEDEC isoforms. Considering that KCNMA1 is
located on the minus strand, t he orientation of the gene model is indicated as 3’ ← 5’. In the
gene model, rectangular boxes or vertical lines depict all KCNMA1 exons, and round dots depict
exon-exon junctions. In the transcript models, only the KCNMA1 exons comprising the spliced
transcripts are s hown. The data used for the construction of the gene and transcripts models
shown above were obtained from the GTEx Portal (release V8).




32

There are indications that mitoBK-α follows a typical mitochondrial import pathway mediated
by the TOM and TIM comple xes, and it is likely translated in the cytosol before the protein
import into mitochondria. Namely, in a proteomic screening of heterologously expressed
mitoBK in HEK293T cells, the interaction of mitoBK channels with the components of TOM
complex was sho wn: the receptor subunit TOM22 binding the peptides to be translocated,
TOM70 recognizing and translocating peptides, and TOM40 forming a protein conductive pore
82.  The association of the mitoBK-α subunit with TOM22 did not require the presence of the
C-terminal VEDEC amino acid signature, and a co -immunoprecipitation study indicated that
mitoBK-α subunit interacted with TOM22 via its transmembrane domain. Components of the
TIM complex for the import into the IMM, such as TIM23 and TIM16, were also identified in
the mitoBK-α protein interactome.

3.4.2. Biophysical properties of mitoBK channels

While the structural information on mitoBK channels is not yet available on the atomistic level,
high-resolution X-ray and cryo-EM structures of the BK-α subunit associated with the BK -β4
subunit were solved for the plasma membrane BK channels  83–85. The key structural elements
of mitoBK channels can be inferred from the data on their plasma membrane counterpart.
MitoBK channel has the largest conductance of all described mitochondrial channels. The
unitary conductance for the mitoBK channel in mammalian cells, as recorded with patch-clamp
in a symmetric 150 /150 mM KCl solution containing 100 μM Ca2+, ranges from 190 pS in
mouse cardiac myocytes to 295 pS in a human glioma cell line (LN229) 86.
The conductive pore of BK channels is formed by a tetramer of BK-α subunits. Each of the BK-
α subunits is composed of approximately 1200 amino acids and contains seven TM helices, six
of which – S1-S6 – are conserved between the voltage-gated potassium channel family, and a
remaining α -helix S0 is unique for BK channels (Figure 5).  The 7 -TM channel topology
requires an opposite orientation of the N - and C -termini: the functional studies of mitoBK
channel activity indicate that the N-terminal part of the channels is exposed to the IMS, while
the C-terminal part is oriented towards the mitochondrial matrix.


33


Figure 5. A schematic illustration of k ey structural ele ments of BK -α subunit (left) and
BK-β subunits (right). BK-α subunits contain seven TM helices, with the TM helices S5 and
S6 forming the channel pore. The C -terminal tail of the BK-α subunit s contains several
functional domains, including RCK1, RCK2, and heme-binding domain (HBD). The BK -β
subunits contain two TM helices.

The channel pore is formed by the TM helices S5-S6 that resemble the core 2-TM pore region
for K+ channels containing the signature amino acid sequence of K+ selectivity filter: TVGYG.
The pore -forming domain is physically liked to a voltage -sensing domain (VSD) of BK
channels, which is similar to the one found in K v channels and is formed by four TM helices
S1-S4 87. The regu larly interspaced arginine residues within the VSD have a crucial role in
voltage sensing, leading to conformational changes that activate BK channels at membrane
depolarization 88. Notably, while the opening of the plasma membrane BK channels contributes
to the membrane repolarization, an influx of K+ through mitoBK inside the matrix would further
depolarize the IMM and, accordingly, lead to an increase of mitoBK current density.
While the C-terminal region of the BK-α subunit is its largest and the most structurally diverse
part, it contains several functional domains that are conserved among most subunit isoforms.
The two domains regulating calcium conductance 1 and 2 (RCK1, RCK2) of each of the four
BK-α subunits associate into an octameric BK gating ring. Ca 2+ binds to BK-α subunit in two
sites: to a high -affinity calcium bowl formed by RCK2, and a site within RCK1  88. The
conformational change in this region is transferred to the pore -gating domain directly through
a C -linker region consisting of the 15 amino acids, and indirectly thro ugh non -covalent



34

interactions. The b inding of Ca 2+ to BK -α subunits increases the open probability of BK
channels as a function of Ca2+ concentration 89.
Since the regulatory eleme nts of the BK channels that confer its voltage and Ca 2+-sensitivity
are located within different structural domains, activation of BK channels by Ca2+ can proceed
independently without changes in the membrane potential values and vice versa. However, BK
channel activation with a small probability occurs as an intrinsic event without Ca2+ binding or
perturbation of the VSD, indicating that activation of these sensors is not strictly required for
the channel pore opening 90.
A BK-α subunit can interact with one of the auxiliary β -subunits of four types – BK-β1, BK-
β2, BK -β3, and BK-β4. Multiple domains of BK -α and BK -β subunits are involved in the
assembly of the channel complex, including the transmembrane region and gating d omain of
BK-α, and intracellular regions as well as an extracellular linker of BK -β subunits 91. The
expression of BK -β subunits is tissue -specific 92. Incorporation of BK -β subunits into the
channel complex can impact mitoBK gating behavior, Ca 2+ and voltage sensitivity, channel
activation and deactivation kinetics, induce channel inactivation, or affect the modulation of the
channel by endogenous and pharmacological compounds (Table 2).
In a set of tissues, BK channel complexes include auxiliary leucine -rich repeat containing
(LRRC) BK-γ subunits 93,94. The binding of regulatory subunits to the pore -forming complex
occurs in a competitive manner: only one auxiliary subunit – BK-β or BK-γ –can associate with
a single BK -α subunit. However, all identified BK -γ subunits belong to the e xtracellular
superfamily of LRRC proteins and possess a cleavable N -terminal signal peptide that targets
them by the secretory pathway to the plasma membrane 94. Therefore, it appears unlikely that
mitoBK channels contain auxiliary BK-γ subunits.
Table 2. Tissue expression and biophysical roles of auxiliary BK channel subunits
(modified from 92–94)
Subunit Gene Tissue expression Biophysical role
β1 KCNMB1
Smooth muscle, lungs, brain,
kidneys.
Increases Ca 2+ and voltage
sensitivity.
Slows down activation and
deactivation kinetics.
Confers channel modulation by
17-beta-estradiol .


35

β2 KCNMB2
Cardiovascular system, lungs,
brain, testes, pancreas, adrenal
glands.
Modulates Ca2+ sensitivity.
Negative regulator that co nfers
rapid channel inactivation.
β3 KCNMB3
Kidneys, pancreas, spleen,
liver, lungs, brain.
Isoforms 2, 3 and 4 inactivate the
channel current.
β4 KCNMB4
Central nervous system,
kindeys.
Slows down activation kinetics.
Decreases Ca2+ sensitivity.
Shifts voltage activation to more
negative potential values.
Abolishes channel inhibition by
charybdotoxin.
γ1 LRRC26
Trachea, prostate, thyroid
gland, thymus, salivary gland,
colon, aorta.
Large negative shift in voltage
dependence of channel
activation.
Accelerates activation kinetics.
γ2 LRRC52
Testes, skeletal muscle,
kidneys, placenta.
Shifts voltage dependence of
channel activation to more
negative values at increased Ca2+
concentration.
Accelerates activation kinetics.
γ3 LRRC55
Brain, kidneys, liver, sp leen,
colon, testes.
Shifts the voltage dependence of
BK channel activation to more
negative values.
γ4 LRRC38
Brain, testes, skeletal muscle,
spleen, thymus, adrenal gland.
Small negative shift in voltage
dependence of channel
activation.

Modulatory effects on mitoBK channels by the BK channel openers and blockers are well -
characterized on a single-channel level. In particular, activation of mitoBK channels was shown
following the application of benzimidazole derivatives such as NS1619 and NS004, and
carboxylic indole derivatives such as CGS7184  95,96. The peptides of scorpio n venoms
charybdotoxin and iberiotoxin, as well as an indole derivative alkaloid paxilline, were found to
inhibit mitoBK channel activity 96.


36

3.5. Functional interplay between the mitoBK channels and the respiratory
chain

Mitochondrial ion fluxes and maintenance of mitochondrial ion gradients are essential for
mitochondrial physiology. From the biophysical point of view, the respiratory chain complexes
and mitoBK channels execute opposite regulation of the mitochondrial membrane potential: the
activity of ETC generates it, while mitoBK opening dissipates it (Figure 6).


Figure 6. A schematic depiction of o pposite regulation of mitochondrial membrane
potential by the ETC and mitoBK channels. The activity of the ETC (left box) generates
mitochondrial membrane potential , and the activity of mitoBK channels (right box)  directly
dissipates ΔΨM.

The key physiological functions of the mitoBK channels are mediated through their in fluence
on the activity of ETC via the following molecular mechanisms that will be briefly reviewed
below:
 change in the protonmotive force;
 modulation of ROS synthesis by the RC;
 Ca2+-dependent regulation of ETC function;
 control over the local availability of substrates.
The a ctivity of mitoBK channels controls protonmotive force in both direct and delayed
manners. The influx of K+ through mitoBK exerts mild depolarization and changes the electrical
component of the driving force for ETC. A chemical gradient component of the protonmotive



37

force is regulated indirectly through efflux of excess of K + following the opening of mitoBK.
The exchange of K+ for H+ by the H+/ K+ antiporter acidifies the mitochondrial matrix.
Certain observations indicate that a small controlled change in the protonmotive force can
improve the metabolic efficiency of the ETC. Thus, treatment of guinea pig heart mitochondria
with mitoBK channel op ener NS11021 led to a small depolarization by 5 -10 mV and
mitochondrial swelling.  At the same time , the efficiency of mitochondrial respiration was
enhanced: stage 4 respiration decreased, whereas stage 3 remained unaltered 97. While
benzimidazole derivatives like NS11021 m ay have unspecific effects on other mitochondrial
proteins, this observation was made using a low dose of NS11021 (50 nM) and the effects were
sensitive to inhibition of channels with paxilline and charybdotoxin.
Hyperpolarization of mitochondria is associated with increased ROS synthesis by the ETC. On
the contrary, diminished ROS synthesis due to temporary mild depolarization of mitochondria
is known to be beneficiary for mitochondrial function under physiological conditions, such as
during mild depolarization that occurs at the M-phase of cell cycle progression and leads  to a
decreased generation of ROS by the complex III 98. Studies with the mitoBK channel openers
confirmed a similar effect on the ROS synthesis by the RC enzymes. The  mild mitochondrial
depolarization due to the BK channel opening was reported to reduce the ROS generation by
complex I of the rat brain mitochondria 99. In another study, genetically induced overactivation
of BK channels was used as an approach to elimi nate potential  non-specific effects of the
pharmacological mitoBK modulators: a model of mice with a gain -of-function BK R207Q
mutation of BK channels was developed 100. Similar to the observations in the WT mice, the
BKR207Q channel was targeted exclusively to the mitochondria of cardiomyocytes. An
overactivation of mitoBK channels conferred a cardioprotec tive effect in an
ischemia/reperfusion injury via mild uncoupling and attenuation of ROS synthesis by ETC
complexes I and III.
Therefore, by improving the efficiency of the ETC, mitoBK channels can modulate  ROS
generation. The physiological relevance of this aspect of the interaction of mitoBK and ETC is
highlighted by the feedback loop mechanisms regulating the activity of mitoBK channels by
hypoxia and ROS species.
An indirect effect of activation of mitoBK channels is mediated by their role in the regulation
of Ca 2+ homeostasis and signaling. Decreased mitoBK channel activity , as reported due to
pharmacological inhibition of mitoBK channels by paxilline and genetic deficiency in
KCNMB1, impairs mitochondrial Ca2+ retention capacity in rodent cardiomyocytes 101. Through


38

changes in the mitochondrial Ca2+ retention capacity, mitoBK activity in directly affects the
activity of Ca2+-regulated enzymes, including complex IV of ETC 102,103.
Another mechanism of a delayed modulation of ETC activity by  mitoBK channels can be
executed through control over the availability of respiratory substrates and metabolites. An
entry of osmotically obligated water following the influx of K+ locally dilutes the electrolytes
in the matrix. The physiological relevance of this phenomenon remains to be elucidated.
Considering the complex implications of the functionally related activities of mitoBK channels
and the ETC complexes, their potential physical interaction would be an intriguing possibility.
Indeed, the growing body of research indicates that the mitoBK channel can functionally
interact with the respiratory chain and thereby regulate the mitoBK channel function.
In a patch -clamp study of the functional interaction between mitoBK ch annels and ETC
complexes in  astrocytoma mitochondria, it was shown that mitoBK channel activity was
inhibited after the addition of the respiratory substrates 104 . Structural interaction between
cytochrome c oxidase and the mitoBK-β4 subunit was shown in the same study, which mediated
the functional coupling. Colocalization and interaction of an auxiliary BK-β1 subunit with
COX1 were also confirmed in rat cardiomyocytes 105. Interaction of mitoBK-α with the subunits
of the respiratory chain complexes I, III and IV was detected among other mitochondrial protein
partners in a proteomic study 106.
However, the involvement of the BK-α subunit in the interaction between the respiratory chain
complexes and mitoBK channels is still unclear. The question of the effect of the deficiency of
the ETC on mitoBK channels remains open as well.


39

3.6. MitoBK channels in mitochondrial signaling

3.6.1. Mitochondrial retrograde signaling pathways

Co-evolution of the proto-nuclear and proto-mitochondrial genomes has led to the development
of the anterograde and retrograde signaling pathways, which relay the signals about the altered
functional and  metabolic state of these organelles and coordinate their response to the
environmental changes. The triggers of mitochondrial retrograde signaling comprise various
mitochondrial stressors, such as  a decrease in the mtDNA copy number, changes in
mitochondrial functions caused by mutations in both mitochondrial and nuclear genomes ,
impairment of protein import, and aberrant ROS signaling  107. Transmission of signals from
mitochondria to the nucleus causes alteration in the cellular gene expression profile, which may
serve for cellular adaptation and survival in physiological and pathological conditions. Due to
their significance, the mitochondrial retrograde signaling pathways have been identified
throughout eukaryotic species - from yeast to mammals 108.
While mtDNA encodes only ~1% of the mi tochondrial proteome, the encoded proteins are
crucial to the OXPHOS. Accumulation of isolated subunits, highly reactive assembly
intermediates, or misassembled ETC complexes poses a threat to the proper functioni ng of
mitochondria. Therefore, coordination of the expression of mtDNA with the expression of the
nuclear genes encoding other ETC proteins, as well as the molecular machinery for mtDNA
maintenance and expression, is required. In addition, disruptions in the mitochondrial protein
import, impaired p eptide folding or assembly of multiprotein complexes can become
challenging for the maintenance of proteos tasis 109. An excessive generation of ROS as a by-
product of the activity of the respiratory chain can pose additional challenges to mitochondrial
function.
To coordinate the expression of mitochondrial proteins between the nucleus and mitochondria,
and to communicate changes in the mitochondrial functional state, two major retrograde
signaling mechanisms have evolved, the signaling of which can occasionally converge 110,111.
One of the pathways relaying the signal of mitochondrial stress to the nucleus and triggering a
global transcriptional response is the mitochondria l branch of integrated stress response
signaling (ISR) 112. ISR is a signaling pathway that is initiated in response to various forms of
cellular stress and leads to a global reduction in protein synthesis with selective overexpression
of stress-responsive genes. The broad range of stress conditions, including severe mitochondrial


40

depolarization, is detected by four types of protein kinases, the activities of which converge on
phosphorylation of the eukaryotic translation initiation factor 2 alpha (eIF2α) 113:
- Perk - sensing ER stress;
- Gcn2 – sensing amino acid deficiency, activated by uncharged rRNAs;
- Prk – sensing double -stranded RNAs originating from viral infections, also can
transduce the signal from mitochondrial unfolded protein response (mtUPR);
- HRI – sensing heme deficiency.
A recently described mammalian pathway characterized the central role of the OMA-DELE1-
HRI relay  in the integrated stress response signaling originating from mitochondria  114.
Phosphorylated eIF2α translationally induces expression of the central transcriptional regulator
of ISR - ATF4. A canonical target of ATF4 induced in the early stages of mtUPR is the
transcription factor Chop (encoded by DDIT3) 115. Through a transcriptional control with the
other downstream targets of ATF4, including transcriptional regulators ATF3, CHAC1, PCK2,
and PPP1R15A, Chop globally decreases cytosolic translation 116.
Correct folding of peptides and a ssembly of multiprotein complexes, along with clearance of
the misfolded proteins, is crucial for mitochondrial protein homeostasis. To prevent misfolding
and protein aggregation in mitochondria, a sufficient amount of chaperons must be available
for the newly translated peptides 117. In particular, the genetic defects in the structure of ETC
subunits or deficiencies in the molecular machinery for  the maintenance of mitochondrial
genome can lead to proteotoxic stress and disruption of mitochondrial homeostasis. Detection
of the unfolded protein stress in mitochondria initiates a retrograde mitochondrial unfolded
protein response (mtUPR) pathway to the nucleus. MtUPR leads to  the increase of expression
of nuclear -encoded mitochondrial chaperones to increase mitochondrial protein -folding
capacity, and transcriptional upregulation of mitochondria-specific quality control proteases to
mitigate proteotoxic damage  118. In particular, the transcription factor ATF5 is involved
mitochondria-specific mtUPR signaling, which sets it apart from the ER-specific UPR pathway
119.
The transcription factors DNA damage -inducible transcript 3 protei n and CCAAT/enhancer -
binding protein-β regulate the expression of s everal mitochondrial proteases that are involved
in mtUPR, such as  the mtUPR marker LONP  and other AAA-proteases ClpXP, CLPP, and
LonP1, located within the mitochondrial matrix and primaril y degrading misfolded soluble
proteins 120. Other mitochondrial quality control proteases, such as Paraplegin ( encoded by
SPG7) and YME1L, are anchored within the IMM, and their primary role involves cleavage of


41

misfolded o r misassembled subunits of the ETC. The upregulated transcription of
mitochondrial chaperons to increase mitochondrial protein folding capacity primarily affects
Hsp70 (encoded by HSPA9), Hsp60 (HSPD1) and Hsp10 (HSPE1) 121.
Interestingly, activation of mtUPR can lead to a selective decrease in the expression of mtDNA
and nuclear-encoded OXPHOS genes to unburden the overwhelmed mitochondrial proteostasis
maintenance systems. Disruptions in mtUPR are reported to have a pathophysiological role in
cancer and neurodegenerative diseases such as Alzheimer’s disease, Parkinson’s disease, and
amyotrophic lateral sclerosis 118,122.
The signaling networks conducting the mitochondrial quality control survey multiple
mitochondrial parameters, including the changes in mitochondrial membrane potential.  A loss
of mitochondrial potential is a crucial event in triggering PINK1 -Parkin mitophagy, as
electrophoretic import of the PINK1 into the depolarized mitochondria through the TOM/TIM
complexes is abolished. Accumulation of PINK1 on the surface of OMM leads to mitofusin 2–
mediated recruitment of Parkin and its ubiquitination of peptide chains of OMM proteins, which
are then recognized by the autophagosome 123.
While the vast majority of work in the area of retrograde signaling research addressed the
molecular mechanisms mediating signal transduction and its impact on mitochondrial
metabolic pathways, there is limited research investigating the broader role of  retrograde
signaling on the regulat ion of ion fluxes in mitochondria. To date, no study has looked
specifically into the role of potassium channels in the retrograde signaling mechanisms
triggered by mitochondrial disorders.



42

3.6.2. MitoBK channels in heme and carbon monoxide signaling

Due to the role of mitoBK in the regulation o f mitochondrial functions, the  research of
molecular mechanisms of endogenous modulation of mitoBK channels has gained considerable
interest. Multimodal ways of functional mitoBK channel regulation have been reported with
various classes of biologically ac tive molecules involved , such as hydrogen sulfide, cGMP
(through the action of protein kinase G), flavonoids 124–126. However, considering the limitations
of this work, this chapter will focus on a more detailed overview of the putative role of mitoBK
in the mitochondrial heme signaling pathways.
Heme is a well-known regulator of the activity of plasma membrane BK channels: BK channels
possess the heme-binding motif within their C-terminal part and were shown to be inhibited by
heme 127,128. Interestingly, the binding of an oxidized form of heme – hemin –  was reported to
decrease the channel activity of mitoBK channels  as well, suggesting that they  also likely
possess a heme -binding structural motif 129. Therefore, a potential i nhibition of mitoBK
channels by heme can  be a part of  a cytotoxic phenomenon in the pathological conditions
characterized by an excessive intracellular amount of heme, such as during  stroke, when
neurons and astrocytes can accumulate up to millimolar levels of heme.
Free heme can be eliminated in the heme degradation pathway involving heme oxygenase,
which produces carbon monoxide (CO) as a byproduct 130. Since the chemical reactivity of CO
is low, its primary intracellular targets are confined to metalloprotei ns containing transition
metals - in particular, hemoproteins. Their o xidation status is relevant as another laye r of
regulation of CO signaling since CO only binds to the ferrous (Fe2+) heme 130.
CO has gained growing attention as a signaling molecule in recent years. Currently, the role of
CO as a gaseous transmitter that controls a wide range of physiological processes is well
established 131–133. The putative benefits of therapeutic CO application, however, are negated
by its systemic toxicity due to its interaction with hemoglobin that produces
carboxyhemoglobin. Therefore, CO -releasing molecules (CORMs) have been  developed to
bypass these concerns and allow for the safe and regulated release of CO  134. The currently
available forms of CORMs come in different  chemical classes of compounds and have been
extensively applied as a tool for the controlled CO release in the research of CO signaling
pathways 135,136. Thus, in situ activation of the mitoBK channel in astro cytoma mitochondria
by a direct application of CORM -401 was shown  137. Yet, a growing number of reports are
addressing the unspecific effects of CORMs 138–140.


43

Mitochondria are a major o rganelle target for CO signaling  because they harbor proteins for
heme synthesis and contain a variety of hemoproteins 141. In particular, cytochrome c oxidase
can be inhibited by CO in  physiological concentrations, leading to t he stalling of comple x III
in a reduced state and producing ROS that can initiate oxidative signaling pathways. By binding
mitochondrially produced heme, mitoBK channels can be an interesting target for CO action.

3.6.3. The role of mitoBK channels in cytoprotective signaling

The signature biophysical characteristics of mitoBK channels, such as large conductance and
joint gating regulation by voltage and calcium ions, endow them with multiple physiological
functions. Over the years, a large amount of research has been devote d to molecular
mechanisms of a cytoprotective role of mitoBK channels in pathological conditions.
In aging cells due to the accumulation of mtDNA mutation and action of ROS, mitochondria
experience significant functional impairments. They are reflected i n the change of
mitochondrial dynamics, glucose metabolism, as well as impairment of the OXPHOS, ROS
signaling, and Ca 2+ overload 142,143. In the cells where oxidative phosphorylation is a major
source of ATP synthesis, such as neurons, mitochondrial  impairments associated with ag ing
can lead to neurodegenerative diseases . Thus, an increased interest has emerged in the
implication of mitoBK in mitochondrial signaling in cardio- and neurodegenerative diseases in
recent years 144.
Alongside mitoK ATP channels, mitoBK channels have been widely studied in the context of
their role in the preconditioning phenomenon against ischemic injury. In the precondit ioning
studies using BK channel openers such as NS11021 and NS1619, prior activation of the BK
channels has decreased the deteriorative effect of ischemia o n the heart function and reduced
the infarct size. The preconditioning effect was abolished by inhib ition of the channels with a
BK inhibitor paxilline. Since only mitoBK channels  are expressed by the cardiomyocytes, the
role of mitochondrial channels was directly implicated in this effect. The molecular
mechanisms mediating a cytoprotective effect of th e mitoBK channel opening involved
modulation of reactive oxygen species generation and signaling, and modulation of
mitochondrial calcium uptake.
In cardiomyocytes , mitoBK channels exerted a cytoprotective effect against ischemia -
reperfusion injury, which  was mediated through ROS signaling  145. Activation of mitoBK


44

channels by CGS7184 in isolated brain mitochondria led to decreased ROS synthesis by
complex I 99.
The immediate protein environment of BK channels in cellular compartments determines their
role in the Ca2+ signaling pathways. Interaction with calcium channels with different regulating
mechanisms determines whether plasma membrane BK channels act as negative feedback
regulators for Ca2+ influx, as in the case when they form protein complexes with CaV channels
in excitable cells, or positive feedback regulators  when BK channels interact with the TRP
channels and P2X purinoreceptors in non -excitable cells. In mitochondria, however,  the
opening of mitoBK channels in response to an increase in the Ca2+ levels and a rapid influx of
potassium ions leads to local depolarization of IMM and decreases the driving force for Ca 2+
entry, thus primarily serving as a negative feedback regulator. As a case in point, deposition of
amyloid beta chara cteristic for Alzheimer’s disease was shown to inhibit mitoBK channels,
what leads to an increase in Ca2+ concentration in mitochondria 86,146. In the study of the effects
of mitoBK channels on the mitochondrial Ca 2+-retention capacity, Ca 2+-activated mPTP
opening was stimulated after inhibition of mitoBK channels with iberiotoxin 147.
The systemic consequences of genetic knockout models are too complex to be attributed solely
to the plasma membrane or mitochondrial forms of BK channels.  Evidence of the KCNMA1
knockout mouse model demonstrated that in mammals the lack of BK channels is not fatal.
However, KCNMA1 deficient mice displayed impairment in learning , and detrimental effects
on the central nervous system were strongly pronounced 148.  Mutations in KCNMA1 have been
linked to epilepsy disorders, which are often accompanied by paroxysmal dy skinesia and
developmental delays 149. Both loss -of-function and gain -of-function BK mutations were
described in epilepsy, often affecting the C-terminal channel part.
A presence of the mitoBK channel was identified in mitochondria of Drosophila melanogaster.
Mutation in the BK channel affected mitochondrial morphology and led to an increase in ROS
generation, which was associated with reduced lifespan 150. Cytoprotective activation of
mitoBK channels ca n be an effector of signaling pathways. In  a study of a cGMP-mediated
signaling pathway, activation of mitoBK channel by protein kinase G was shown, and it had a
cytoprotective effect in the coronary arteries 151.
Therefore, ample evidence supports that activation of mitoBK channels can be cytoprotective
due to its modulatory effects on the OXPHOS, ROS synthesis, and mitochondrial signaling.


45

4. AIMS OF THE STUDY

The general aim of this study was to investigate the interaction of the mitoBK channel with the
cytochrome c oxidase (COX) and to gain insight into the systemic modulation of  the mitoBK
channel by the carbon monoxide (CO).
The specific aims of this study included:
1. Confirmation of the expression of mito BK-α subunit in the studied cell models: human
astrocytoma cells, human dermal fibroblasts.
2. Pharmacological induction of mtDNA depletion in the astrocytoma cells to obtain the cellular
system void of functional respiratory chain ( RC). Confirmation of th e abolishment of
respiration by these cells.
3. Characterization of steady-state protein complexes formed by the mitoBK channels with the
COX in the WT cells and the cells devoid of mtDNA.
4. Evaluation of the steady-state mitoBK-α subunit protein and transcript amount in these cell
lines.
5. Study of the transcriptome to analyze gene signaling pathways activated in the mtDNA -
depleted cells.
6. Modeling of the genetic deficiency in COX8A in the HEK293T cells with a CRISPR/Cas9
gene-editing system. Identification of mutant clonal cell lines by screening.
7. Characterization of the RC protein complexes formed by the human dermal fibroblasts of the
patient with a genetic deficiency in COX8A.
8.  Characterization of the RC protein complexes formed by the HEK293T cells with an induced
deficiency in COX8A.
9. Characterization of steady-state protein complexes formed by the mitoBK channels with the
RC complexes in COX8A-deficient fibroblasts.
10. Evaluation of the steady-state mitoBK-α subunit protein and transcript amount in COX8A-
deficient fibroblasts.
11. Study of the transcriptome of COX8A-deficient fibroblasts and HEK293T to analyze gene
signaling pathways activated upon COX8A deficiency.


46

12. Electrophysiological study to analyze the effects of three struct urally different CORMs on
mitoBK channel activity in the astrocytoma mitochondria.
13. Electrophysiological evaluation of the effects of hemin, heme, and CO on mitoBK channel
activity in the astrocytoma mitochondria.




47

5. MATERIALS AND METHODS

5.1. Chemicals

The chemicals used in this work are indicated in the Table 3.

Table 3. Chemicals and suppliers.
Chemical Manufacturer
2’,3’-dideoxycytidine (ddC) Sigma-Aldrich
4-(2-hydroxyethyl)-1-piperazineethanesulfonic
acid (HEPES)
Sigma-Aldrich
5,5′-Dithiobis(2-nitrobenzoic acid) (DTNB) Sigma-Aldrich
6-aminohexanoic acid (ε-aminocaproic acid) Serva Electrophoresis
Acrylamide Sigma-Aldrich
Acrylamide/Bis solution,  37.5:1 BIO-RAD
Agarose  Sigma-Aldrich
Amersham™ ECL Prime Western Blotting
Detection Reagent
GE Healthcare
Ammonium persulfate (APS)  Carl Roth
Bis(2-hydroxyethyl)amino-
tris(hydroxymethyl)methane (Bis-Tris)
Carl Roth
Bovine serum albumin Sigma-Aldrich
Calcium chloride (CaCl2) Sigma-Aldrich
Carbon monoxide gas (CO) Multax s.c.
Carbonyl cyanide 3-chlorophenylhydrazone
(CCCP)
Sigma-Aldrich
CGS7184 Novartis Pharma
Chloroform Sigma-Aldrich
Coenzyme Q1 (CoQ1)  Sigma-Aldrich
cOmplete, Mini Protease Inhibitor Cocktail Roche
Coomassie Brilliant Blue G BIO-RAD
Coomassie Brilliant Blue R-250 staining
solution
BIO-RAD
CORM-2 (tricarbonyldichlororuthenium(II)
dimer)
Sigma-Aldrich
CORM-401 (tetracarbonyl[N-(dithiocarboxy-
kS, kS′)-N-methylglycine]manganite)
Sigma-Aldrich
CORM-A1 (sodium boranocarbonate)  Sigma-Aldrich
Cytochrome c from bovine heart  Sigma-Aldrich
Digitonin  Serva Electrophoresis
Dimethyl sulfoxide (DMSO) Sigma-Aldrich


48

Dulbecco’s modified Eagle’s medium Thermo Fisher Scientific;
Ludwik Hirszfeld Institute of
Immunology and Experimental Therapy
ECL Prime GE Healthcare
Ethanol Sigma-Aldrich
Ethidium bromide Sigma-Aldrich
Ethylenedinitrilotetraacetic acid (EDTA) Sigma-Aldrich
Fetal bovine serum Gibco
GeneJuice transfection reagent  Sigma-Aldrich
Glycerol  Sigma-Aldrich
Glycine Serva Electrophoresis
Hemin Sigma-Aldrich
HMW Native Marker Kit  GE Healthcare
Hydrochloric acid (HCl)  Sigma-Aldrich
Lauryl maltoside Abcam
L-Glutamine Gibco
Methanol Sigma-Aldrich
Midori Green  Nippon Genetics
Myoglobin from equine heart  Sigma-Aldrich
Normal donkey serum  Abcam
Oxaloacetatic acid Sigma-Aldrich
PageRuler pre-stained protein ladder  Thermo-Fisher
PageRuler™ Prestained Protein Ladder Thermo-Fisher
Paraformaldehyde (PFA)  Sigma-Aldrich
Paxilline Sigma-Aldrich
Penicillin-streptomycin Invitrogen, Sigma-Aldrich
Phenylmethylsulfonyl fluoride (PMSF) Sigma-Aldrich
Phosphate buffer saline (PBS) Invitrogen
Potassium chloride (KCl)  Sigma-Aldrich
Potassium cyanide (KCN) Sigma-Aldrich
Potassium hydroxide (KOH)  Sigma-Aldrich
Protein marker IV (pre-stained), peqGOLD Avantor
PVDF (polyvinylidene difluoride) membranes Carl Roth
Saponin Sigma-Aldrich
Sodium chloride (NaCl) Sigma-Aldrich
Sodium dithionite Merck
Sodium dodecyl sulphate (SDS) Sigma-Aldrich
Sucrose Sigma-Aldrich
SuperSignal West Pico Chemiluminescent
substrate
Thermo Fisher Scientific
Tetramethylethylendiamin (TEMED)  Sigma-Aldrich
The Pierce BCA protein assay kit  Thermo-Fisher
Tris-acetate-EDTA (TAE) Thermo Fisher Scientific


49

Trizma (Tris) Sigma-Aldrich
TRIzol Reagent  Invitrogen
Tween 20 BIO-RAD
Uridine  Sigma-Aldrich
VECTASHIELD Mounting Medium with
DAPI
Vector laboratories
β-mercaptoethanol  Sigma-Aldrich
β-Nicotinamide adenine dinucleotide (NADH) Sigma-Aldrich

5.2. Cellular models

The experiments were performed on U -87 MG human astrocytoma cells , human dermal
fibroblasts, and HEK293T cells. The genetic data for human dermal fibroblasts of a patient with
Leigh syndrome and epilepsy harboring a homozygous splice site mutation in COX8A has been
previously published 152. Fibroblasts of an age-matched donor were used as control cells.
The cells were maintained in a humidified incubation environment at 37°C containing 5% CO2.
The cell growth medium was composed of Dulbecco’s modified Eagle’s medium supplemented
with 10% fetal bovine serum,  2 mM L -glutamine, 100 U/ml penicillin, and 100 μg/ml
streptomycin. The cells were fed every third day and reseeded upon reaching 80% confluence.

5.3. Depletion of mtDNA in the astrocytoma cells

U-87 MG astrocytoma cells were trea ted with the nucleoside analog  2',3'-dideoxycytidine
(ddC), which was shown to inhibit the DNA-polymerase gamma 153. DdC was supplemented to
the standard cell culture medium at  all times, and the cell culture medium  was replaced every
third day. While the addition of ddC to the medium to the final concentration of 20 μM was
tolerable by the cells, an increase to 50 μM or higher values has led to a complete stunt in the
cell growth and a sharp increase in the cell death. Therefore, the final concentration of 20 μM
of ddC has been used in all experiments for mtDNA depletion. Uridine was also supplemented
at the concentration of 50 μg/ml.

5.4. Induction of COX8A deficiency in HEK293T cells with CRISPR/Cas9

CRISPR/Cas9 constructs containing  single guide RNA  (sgRNA) targeting exon 1 of COX8A
were used for gene editing of the HEK293T cells. The c hoice of the sgRNA sequence  for


50

CRISPR/Cas9 constructs was facilitated by the Broad Institute's and Synthego sgRNA designer
programs (Figure 7).


Figure 7. Illustration of the principle of the operation of the designed CRISPR/Cas9
construct targeting COX8A using the Synthego sgRNA designer program.

Cloning of the dsDNA oligonucleotides enc oding gRNA was performed into pSpCas9(BB)-
2A-GFP (Addgene) as described elsewhere 154. GeneJuice transfection reagent (Sigma-Aldrich)
was used to transfect HEK293T cells with the CRISPR/Cas9 construct -containing plasmid
according to the manufacturer's instructions. To isolate single-cell clones, the viable cells were
counted, the cell suspension was diluted for the expected single cell per well density, and seeded
onto 96-well plates 24 hours after transfection. After the establishment of stable clonal colonies,
the cells were split and a fraction o f them was collected for DNA isolation by a commer cially
available kit (The QIAamp DNA Mini Kit, Qiagen) for screening by Sanger sequencing.

5.5. Nucleic acid isolation

5.5.1. RNA isolation
Two methodologically different approaches were used for the RNA isolation, depending on its
downstream application. For the expected applications as a template in RT-PCR and qRT-PCR,
total RNA was extracted from cells with a commercially available spin column-based kit using
a method according to the manufacturer's in structions (RNeasy Mini Kit, Qiagen).  After
spectroscopic evaluation of the purity and yield of collected RNA, t he samples were
immediately utilized for downstream applications.
For the expected application as a template for  the creation of cDNA libraries in the
transcriptome 3'-RNA sequencing study, an additional step was introduced in RNA isolation to



51

improve the purity and stability of yielded RNA. Specifically, prior to the isolation of the silica-
membrane column  of the commercial kit , RNA was extracted  with the standard
phenol/chloroform method. Incubating the cell pellet in TRIzol Reagent (Invitrogen) produced
cellular lysate, which was subsequently subjected to the mechanical lysis  in commercially
available QIAshredder tubes (Qiagen). While the manufa cturer of TRIzol Reagent does not
disclose its protected formula, phenol and guanidine isothiocyanate are contained in the
formulation of this product. Therefore, to facilitate dissociation of the nucleoprotein complexes
by guanidine isothiocyanate at this stage, the collected cellular lysate was incubated at the RT
for 5 min. Afterward, chloroform was added to the lysate, incubated for 15 min at the RT, and
centrifuged for 15 min at 12000 g at 4°C. Phase separation recovered  three phases from the
sample: t he top RNA-containing aqueous phase, the DNA-containing interphase, and the
bottom protein and lipid -containing organic phase. The RNA-containing aqueous phase was
collected, mixed with 70% ethanol, and transferred onto silica -membrane columns  of the
RNeasy Mini Kit. The subsequent steps of RNA isolation were conducted in a regular manner
according to the manufacturer’s instructions.

5.5.2. DNA isolation
The cultivated cells were mechanically scraped off in the cold PBS, and the cell pellets were
recovered by centrifugation at 800 g for 10 minutes. The silica membrane -based spin column
kit (QIAamp DNA Mini Kit, Qiagen) was then used to extract total genomic DNA according
to the manufacturer's protocol. The DNA samples were eluted in water and stored at -20°C until
they were utilized for the downstream application.

5.5.3. Spectrophotometric nucleic acid quantification
The purity and yield of isolated RNA or DNA in the samples were estimated
spectrophotometrically with Cary 60 UV -VIS spectrophotometer (Agile nt Technologies) or
Nanodrop 2000 (Thermo Scientific).
The Lambert-Beer law was applied for the estimation of concentration of isolated DNA or
RNA:
𝐴 =  𝜀𝑐𝑙 ,


52

where A is the absorbance, 𝜀 is the attenuation coefficient (the standard coefficients are 0.020
µg∙mL-1∙cm-1 for dsDNA, 0.025 µg∙mL -1∙cm-1 for RNA), c is the concentration of the
attenuating compound, l is the optical path length.
The absorbance values were measured at the following wavelengths: λ = 230 nm, λ = 260 nm,
λ = 280 nm. For RNA probes, the absorbance ratio A 260/A280 was within the range of 1.8 – 2.0,
what denotes that the DNase treatment step in a commercial kit procedure purified the samples
from DNA. The absorbance ratio A260/A230 was 2.0 or higher, indicating no contamination of the
eluate by phenol and proteins.

5.6. Thermal cycling-based gene expression evaluation

5.6.1. Reverse transcription of total RNA

Reverse transcription of RNA for the downstream PCR applications was performed directly
after RNA isolation and quantification with an iScript Select cDNA Synthesis Kit (Bio-Rad) as
described below, using a random primer set provided in the kit:
Reagents Volume per 1 reaction
Template RNA Corresponding to 1 µg
5x iScript reaction mix 4 µl
Random primers 2 µl
Reverse transcriptase 1 µl
Water Variable
Total volume 20 µl

The reaction mixes were placed into a thermocycler (Bio -Rad) with a following programmed
temperature protocol:
5 min at 25°C
30 min at 42°C
5 min at 85°C
hold on 12°C.


53

5.6.2. Polymerase chain reaction (PCR)

The primers for PCR were designed with the Primer -BLAST software (National Library of
Medicine, USA)  (Table 4). The annealing temperatures for eac h primer pair were selected
through optimization of the predicted temperature in the prior gradient PCR.
Table 4. Primer sequences and annealing temperatures
Gene Primer sequence Designed
product
size, bp
Annealing
temperature,
°C
KCNMA1
(for RT-PCR)
F: CCA TCC ACA GCA AAC CGG CCA
R: TGA GTA AGT AGA CAC ATT CCC
312 60.0
KCNMB1 F: CCA GAA CCA GCA GGT ACT CA
R: CCA GGT CTG TGT CAC TCC AA
160 61.0
KCNMB2 F: CAC TGA AGG CAG GAG AGG AC
R: GTC CAC ACG CTC TGC ATG TA
150 58.4
KCNMB2
(nested outer
primers)
F: CAG TGG CCG GAC CTC TTC
R: GGA ACA GCA CGT TGG AAC TG
578 60.2
KCNMB3 F: ATC ATG GAC GAC TGG CTG GA
R: GTC TGT AAC ATC ACG CTT GGG A
171 61.6
KCNMB4 F: AGG TGA AGG TGC ACT CGA AC
R: GTG GCT TAC GAG TAC ACG CA
205 58.8
GAPDH F: CAA GGT CAT CCA TGA CAA CTT TG
R: GTC CAC CAC CCT GTT GCT GTA G
495 58.0

For the  qualitative detection of gene expression,  cDNA was amplified using the JumpStart
REDTaq Ready Mix (Sigma-Aldrich) according the reaction mix scheme shown below:
Reagents Volume per 1 reaction
Template cDNA 1 µl
Jumpstart REDTaq Ready mix 12.5 µl
Forward primer 1 µl
Reverse primer 1 µl
Water 7 µl
DMSO 0.5


54

5.6.3. Agarose gel electrophoresis

1.5% agarose gel was prepared in Tris-acetate-EDTA (TAE) buffer. 10 µl Midori Green DNA
dye was added to 120 ml of liquid agarose mixture. The reaction products in the REDTaq mix
were directly loaded into a solidified agarose gel and run at a constant voltage of 130 mV for
the duration of time necessary for proper separation (about 60 minutes). For the product  size
identification, a reference 100 bp DNA ladder (NEB) was loaded into the gel alongside the
samples. DNA visualization was performed with the UV -illuminator GelDocTM XR at
excitatory wavelengths between 254 and 365 nm.

5.6.4. Quantitative real-time PCR (qRT-PCR)

To quantify expression  of KCNMA1, qRT-PCR was performed with Sybr Select Master Mix
(Thermo Fisher), with the sequences of the primers used for the qRT-PCR and the composition
of the reaction mix as specified below:
Reagents Volume per 1 reaction
Template cDNA 1 µl
Sybr Select Master Mix 10 µl
Forward primer 1 µl
Reverse primer 1 µl
Water 7 µl
Total volume 20 µl

Gene Primer sequence Designed
product
size, bp
Annealing
temperature,
°C
KCNMA1
(for qRT-PCR)
F: GAG CAT CTC TCA GCC GGT AA
R: CCG CAG ACA CTG GCC AAT AG
166 61.0
GAPDH
(for qRT-PCR)
F: TCA GAC ACC ATG GGG AAG GT
R: GAA TCA TAT TGG AAC ATG TAA
107 61.0

The reaction mixes were placed into the thermal cycler (Bio-Rad) with a following programmed
temperature protocol:
5 min at 95°C,


55

for 45 cycles:
30 sec at 95°C
   1 min at 61°C;
hold on 12°C.

5.7. Sanger sequencing

For amplification of the COX8A genomic DNA fragment for downstream Sanger sequencing,
PCR was performed with JumpStart Accutaq polymerase (Sigma-Aldrich) accor ding to the
protocol described below. The primers for sequencing were designed to be at located least 150
bp away from the gRNA match site with COX8A that constituted a potential Cas9 cutting site.
All the products of PCR were stored at +4°C.
Reagent Volume
AccuTaq LA 10 x Buffer  5 µL
dNTP mix  2.5 µL
Template DNA X µL (total 400 ng)
Forward primer (10 µM) 2 µL
Reverse primer (10 µM) 2 µL
Water, PCR Reagent  (14 – X) µL
Long and Accurate PCR Enzyme (1 unit/µL) 2.5 µL
Total volume 50 µL

Gene Primer sequence Designed
product
size, bp
Annealing
temperature,
°C
COX8A F: GCC ATT TGG GCT TCC TGA CCT T
R: CAG GCA TCC CCC AGT GAA C
491 62

The following thermocycler (Bio-Rad) program was used for amplification of the genomic
fragment of interest:
90 sec at 98 °C,
for 30 cycles:
denaturation 15 sec at 95 °C
annealing 2 min at 62 °C;
10 min at 72°C.


56

The products of amplification were purified from the residual primers and nucleotides with the
ExoSAP-IT PCR (Thermo Scientific) product cleanup reagent (Ther mo Scientific) according
to the manufacturer’s instruction. After spectrophotometric estimation of the concentration of
the final DNA and its dilution in water, the samples were sent for Sanger sequencing by the
commercial company (Eurofins).

5.8. High-throughput whole-transcriptome sequencing

5.8.1. Library preparation and sequencing

To evaluate the expression levels of mitochondria- and nuclear-encoded mitochondrial proteins,
isolated total RNA was analyzed by 3’ -RNA sequencing. RNA integrity number o f the total
RNA was controlled using the Agilent TapeStation  and was higher than 7 in all samples. The
complementary DNA (cDNA) library was prepared from total RNA using the QuantSeq 3’ -
mRNA-Seq Library Prep Kit (Illumina), producing the cDNA library that was enriched in the
sequences in the immediate proximity to the 3’ -end of the transcribed polyadenylated RNA.
The sequencing was performed on a HiSeq 2500 sequencing platform (Illumina) in the high
output mode.

5.8.2. RNAseq data processing

The FASTQ s equencing output files were mapped to the Homo sapiens genome assembly
GRCh38 (hg38) obtained from the Genome Reference Consortium using the UCSC gene
annotation file. The RNA STAR aligner was used on the Galaxy platform in the two-pass mode
following the software instruction manual. The mapped reads were quantified using the
featureCounts algorithm. Normalization of the read counts and statistical evaluation of
differential gene expression was performed by the R/Bioconductor DESeq2 software package.

5.9. Isolation of mitochondria from cultured cells

Standard solation of mitochondria was performed as previously described 104. Briefly, the cells
were harvested and pelleted at 800 g. The cell pellet was resuspended in ice -cold solution A
(250 mM sucrose, 5 mM HEPES, pH = 7.2) and homogenized in a glass potter. The homogenate


57

was centrifuged at 780 g for 10 min at 4°C. The supernatant was collected and centrifuged in
the ice-cold solution A at 9200 g for 10 min at 4°C. The pellet was washed and resuspended in
the ice-cold solution A  and centrifuged at 9200 g for 10 min at 4°C. The pellet containing
mitochondria was resuspended in the ice-cold solution B (150 mM KCl, 10 mM HEPES, pH =
7.2) and kept on ice.
In case the mitochondrial preparation s were to be used for the protein analysis, the protease
inhibitor cocktail was added to solutions A and B (Complete Mini, Roche). However, it was
avoided in the mitochondrial preparations for the patch -clamp analysis in order to minimize
pharmacological interactions with the ion channels and their protein partners.
Isolation of mitochondria with the magnetic beads -based method, the suitability of which was
evaluated for the a ssessment of protein complexes of mitoBK channels with the respiratory
chain in a strocytoma cells , wa s performed with a commercially available mitochondrial
isolation kit according to the manufacturer’s instructions (Miltenyi Biotech).

5.10. Western blot assessment of the amount and composition of proteins
and protein complexes

5.10.1. Determination of protein concentration

Following each mitochondrial isolation for the Western blot experiments, an aliquot of  the
isolated sample was reserved for quantification of protein content. The Pierce BCA protein
assay kit (Thermo Scientific) was selected for estimation of the protein concentration since this
method is not sensitive to a wide range of detergents. For accurate quantification of the
mitochondrial membrane proteins, the content of mitochondrial aliquots was solubilized with
5% SDS (v/v). The measurements were performed according to the manufacturer’s instructions.
Following incubation of the samples, protein concentration was inferred from the absorbance
of the Cu+-bicinchoninic acid complex at 562 nm. The supplied bovine serum albumin was used
to prepare a standard curve, and the sample protein concentration was interpolated on it using
GraphPad Prism 8.





58

5.10.2. SDS-PAGE protein electrophoresis

For SDS-PAGE, aliquots of mitochondrial preparation were solubilized by incubation in  4X
Laemmli sample buffer (Bio-Rad) containing 1% β -mercaptoethanol at 60°C for 15 min. The
samples were then loaded alongside a PageRuler pre-stained protein ladder (Thermo Scientific)
into the 12.5% SDS polyacrylamide gel and separated by electrophoresis.

5.10.3. Blue-native PAGE protein electrophoresis

For BN-PAGE, mitochondrial aliquots were solubilized in a digitonin-containing solution (10%
v/v glycerol, 1% v/v digitonin, 50 mM NaCl, 20 mM Tris-HCl, 0.1 mM EDTA, 1 mM PMSF,
pH = 7.4). The samples were incubated on ice for 1 5 min. The solubilized mitochondria were
centrifuged for 10 min at 9200 g at 4°C, and the supernatant was collected. The loading dye
(1.5 M aminocaproic acid, 50 mM Bis -Tris-HCl, 5% Coomassie brilliant blue, pH = 7.0) was
added to the supernatant to a fina l concentration of 1/3 of the total probe volume. The probe
containing 100 µg protein per lane was next loaded into a 4 -10% gradient blue native
polyacrylamide gel and mitochondrial protein complexes were separated by electrophoresis at
4°C.

5.10.4. Immunostaining and protein detection

Following BN-PAGE or SDS-PAGE, the gels were electroblotted onto polyvinylidene fluoride
(PVDF) membranes. The PVDF membranes were immunoprobed with the primary antibodies
raised against proteins of interest as described in Table 5.
The antibody detection was performed with appropriate secondary antibodies conjugated to
horseradish peroxidase raised against the organism hosting the primary antibody : anti-mouse
(GE Healthcare NA931V) or anti-rabbit (GE Healthcare NA9340V).  The signal was visualized
with chemiluminescent detection reagents according to the manufacturer’s instructions.






59

Table 5. Characteristics of primary antibodies used in the Western blot studies.
Name of the
target
Company/code Clo
nali
ty
Host
organism
Dilution Incubation
time
BK channel subunits
BK-α Neuromab 022, clone
L6/60
M Mouse 1:200 overnight
BK-β3 Neuromab N40B/18,
clone N40B/18
M Mouse 1:200 overnight
BK-β4 Alomone APC 061 P Rabbit 1:200 overnight
Complex IV of respiratory chain
COX5A Thermofischer
PA5-27432
P rabbit 1:1000 overnight
COX1

Invitrogen
1D6E1A8
M Mouse 1:1000 overnight
COX4 Cell signaling
4844s
P rabbit 1:1000 overnight
COX2 Invitrogen
12C4F12
M Mouse 1:1000 overnight
Complex I of respiratory chain
NDUFA9

Abcam ab14713 M Mouse 1:1000 overnight
Complex II of respiratory chain
SDHA  Abcam ab137040 M Rabbit 1:1000 overnight
Complex III of respiratory chain


60

CORE2 Abcam ab14745  M mouse 1:1000 overnight
ATP-synthase
ATP-synthase
subunit c
Abcam ab181243 M Rabbit 1:1000 overnight
Transporters and other proteins
TOM-20 Santa-Cruz 17764 M Mouse 1:500 overnight
VDAC Abcam ab15895 P Rabbit 1:1000 overnight
MCU Sigma HPA016480 P Rabbit 1:200 overnight
HSP75 Abcam ab182775 P Rabbit 1:1000 overnight


5.11. Confocal microscopy cell imaging

5.11.1. Immunocytochemical staining

The cells were seeded onto a glass coverslip in a standard growth medium and grown as a
monolayer in its exponential growth phase. To prepare the sample for immunocytochemical
staining, a residual amount of cell growth medium was removed by triple delicate washing of
the cells for 5 min in 0.5 ml PBS. Next, the cells were fixed in ice -cold 4% paraformaldehyde
(PFA) solution in PBS for 30 min. PFA was removed from the cells by triple washing for 5 min
with 0.5 ml PBS. The free aldehyde groups introduced after the PFA fixation were quenched
by incubating the sample in 50 mM ammonium chloride solution in PBS for 15 min, followed
by the wash in PBS. Next, the cells were permeabilized and blocked by incub ation in the
blocking buffer containing 0.075% saponin, 1% SDS, and 5% normal donkey serum for 30 min
at the room temperature. The cells were then incubated overnight at 4°C with a blocking buffer
containing primary anti -VDAC antibodies (1:500). Following a wash in PBS, the cells were
incubated in the blocking buffer contai ning goat anti -rabbit Alexa Fluor 633 -conjugated
secondary antibodies (1:500, Thermo Scientific) for 1 h at room temperature. After the final
PBS washes, the samples were mounted in a Vectashield DAPI-containing medium and directly
used for visualization.



61

5.11.2. Sample visualization

The microscopical examination of immunostained cells was performed with the confocal
microscope Olympus FluoView 1200 (Olympus, Spain). The laser system se ttings were
selected taking into account the spectral properties of fluorophores: a diode laser emitting at
635 nm for excitation of Alexa Fluor 633, and a diode laser emitting at 405 nm for excitation
of DAPI. The signal detection parameters were adjusted to capture the emission peak of Alexa
Fluor 633 at 650 nm and the emission peak of DAPI at 470 nm. Analysis of microscopy images
was performed with ImageJ version 1.51k (National Institutes of Health, USA).

5.12. Patch-clamp on the ion channels of the inner mitochondrial membrane

Patch-clamp experiments on the ion channels of the inner mitochondrial membrane were
performed as previously described 67,71,155. Briefly, a fraction of the isolated mitochondria was
subjected to osmotic shock by being placed into a hypotonic solution (5 mM HEPES and 100
μM CaCl2, pH = 7.2) for about 1 min. To restore the tonicity of the bath chamber solution to
isotonic conditions (150 mM KCl, 10 mM HEPES, and 100 μM CaCl 2, pH=7.2), hypertonic
solution (750 mM KCl, 30 m M HEPES, and 100 μM CaCl 2, pH=7.2) was added dropwise to
the mitoplast suspension previously obtained. Floating mitoplasts were visually identified using
an inverted microscope and selected by attaching a borosilicate glass patch-clamp pipette. The
pipette was filled with an isotonic solution (150 mM KCl, 10 mM HEPES, and 100 μM CaCl2,
pH= 7.2).
The patch-clamp recordings were made in inside-out mode, in which the matrix-facing the IMM
side was exposed to the perfusion solution. The exchange of the experime ntal solution was
made by positioning the patch pipette into the glass tube openings of a “sewer pipe” perfusion
system (made in -house with a peristaltic pump and tubing from Ismatec, Germany). The
channel modulators were diluted, as indicated, either in t he isotonic solution containing 100
µM free Ca2+ or in the solution containing 1 µM free Ca2+ (10 mM HEPES, 1 mM EGTA, and
0.752 mM CaCl2, pH = 7.2).
The patch-clamp experiments were carried out in the voltage -clamp mode by the patch-clamp
amplifier Axopatch 200B (Molecular Devices Corporation). The borosilicate glass pipettes
were pulled using a PC-10 puller (Narishige) and had a resistance of 15-20 MΩ. The currents
were low-pass filtered at 1 kHz and sampled at a frequency of 100 kHz. The experiments were


62

recorded in single -channel mode. The probability of a channel opening (NP o) was estimated
using the single -channel search mode of the Cl ampfit 10.2 Software (Molecular Devices
Corporation). Statistical analysis was performed with Student’s t-tests, and p-values below 0.05
were considered significant.

5.13. Measurement of respiration of astrocytoma cells

Cellular respiration was measured polarographically with a Clark-type oxygen electrode system
(Oxygraph-2k, Oroboros ). U -87 MG cells were harvested by trypsinization, counted , and
centrifuged at 800 g for 10 min. The cell pellet was then resuspended in respiration medium
(DMEM supplemented with 1 % penicillin/streptomycin and 1 % glutamine) and the cellular
oxygen consumption rate was measured imminently after stabilization of the baseline
parameters. Afterward, the mitochondria of the suspended cells were uncoupled by incremental
addition of 1 μM CCCP to the recording chamber. The oxygen consumption rate was
normalized to the number of cells in the experimental chamber and presented as O 2/min/106
cells. Data acquisition and processing were performed with the DatLab software (Oroboros).

5.14. Perfusion with CO and confirmation of the CO presence with
myoglobin assay

Solutions with CO gas were perfused on the day of the experiment by bubbling the solutions
with CO gas for 30 min and stored in the gastight sealed vials 156. Hemin was reduced to heme
with dithiothreitol and sodium dithionite as previously described 157.
The saturation of solutions with carbon monoxide was evaluated with a hemoglobin assay on a
UV/Vis spectrophotometer (Cary). Myoglobin was dissolved in the experimental buffers
supplemented with an excess of a reducing agent sodium dithionite. The solution was then
layered over with light mineral oil. The b inding of CO to myoglobin changes its t ypical
absorption spectrum by decreasing the values of the peak at λ = 557 nm and the appearance of
the peaks characteristic for carboxymyoglobin at λ = 540 nm and λ = 577 nm. The amount of
carboxymyoglobin can be evaluated by application of the Lambert – Beer law as described
above, using the following attenuation coefficient values: for deoxymyoglobin ε560nm = 13.8
l∙mmol-1∙cm-1, for carboxymyoglobin ε540nm = 15.4 l∙mmol-1∙cm-1.


63

5.15. Determination of mitochondrial enzymatic activities

The samples containing isolated mitochondria were homogenized with a homogenizer in PBS
and centrifuged at 16000 g for 15 min at 4 ℃. The supernatant enriched in the mitochondrial
matrix enzymes was collected and used for the measurement of citrate synthase activity. The
pellets containing mitochondrial membranes were re -suspended in PBS and used for the
determination of the activity of the respiratory complexes I and IV. All measurements were
performed spectrophotometrically using a dual -wavelength spectrophotometer (Aminco DW
2000, SLM Instruments, Rochester, NY, USA) at 30°C.
The activity of complex I was measured at the wavelength pair of 340 nm/380 nm, εred-ox = 5.5
mM-1 cm-1. The total NADH oxidation rate was estimated by the addition of the mitochondrial
probe to the reaction mix consisting of 50 mM KCl, 1 mM EDTA, 1 mM KCN, 100 μM CoQ1,
150 μM NADH, 10 mM Tris-HCl at pH 7.4). After 2 min of recording, the rate of the rotenone-
insensitive NADH oxidation was determined by the addition of 20 μM rotenone to the reaction
mix. The rotenone -sensitive NADH:CoQ oxidoreductase activity was evaluated by the
subtraction of the rotenone -insensitive NADH oxidation r ate from the total NADH oxidation
rate.
The activity of complex IV was determined at the wavelength pair of 510 nm/535 nm, εred-ox =
5.9 mM -1 cm-1. The change in the heme porphyrin -associated β-band of  the cytochrome c
absorption spectrum was monitored. T he mitochondrial probe was added to the reaction mix
containing 100 mM potassium phosphate buffer (pH 7.4), 0.02% laurylmaltoside, and 200 μM
reduced bovine heart cytochrome c.
The activity of citrate synthase was evaluated by a standard method 158. Briefly, the generation
of CoA-SH in the reaction catalyzed by citrate synthase in the presence of oxaloacetate and
acetyl-CoA, and its subsequent reduction of 5’,5’-dithiobis-(2-nitrobenzoic acid) (DTNB) was
measured spectrophotometrically at 412 nm.

5.16. Data analysis

The software used to analyze the data is specified above for each respective method. For other
applications, Microsoft Office Professional 2016 and GraphPad Prism 8 were used for


64

calculation, and CorelDraw 2018 for image processing and depicting artistic illustrati ons.
Unless otherwise noted, n = 3. Statistical analysis was performed with Student’s t-tests, and p-
values below 0.05 were considered significant. The data are presented as the mean ± standard
deviation (S.D.).



65

6. RESULTS

6.1. Molecular identity of mit oBK channels in human astrocytoma and
fibroblast cells

The initial step in addressing the research questions studied in this work was to confirm the
presence of the mitoBK channel in the studied cellular systems and to characteri ze its steady-
state proper ties. Identification of mitoBK channels can be performed using  different
methodological approaches. Taking into consideration the conceptual framework of this study,
the presence of mitoBK channels in the chosen research models was validated by the following
means:
 on the genetic level: confirmation of the expression of transcripts encoding known
mitoBK channel subunits with RT-PCR and RNA sequencing;
 on the protein level: confirm ation of the presence of mitoBK protein subunits in the
mitochondrial fraction with SDS-PAGE followed by immunoblotting;
 on the functional level: characterization of the single-channel mitoBK activity by patch-
clamp.
To obtain a snapshot of the expression of all genes reported for BK channels in the plasma
membrane and IMM, the transcriptome of selected cell lines was profiled using the RNA
sequencing approach (Figure 8). For this purpose, total RNA was isolated from astrocytoma
and dermal fibroblast cell lines. Since the integrity of  the RNA template is of  paramount
importance for the preparation of the cDNA libraries for high throughput sequencing, additional
measures were undertaken during the RNA isolation procedure to prevent RNA degradation at
any moment of sample handling, as described in chapter 5 .4. As a result, the sufficiently high
RNA integrity  number of the samples , computed using the characteristics of the RNA
electropherogram, confirmed the stability of the obtained RNA. Spectrophotometric analysis of
the obtained RNA samples confirm ed their purity from contamination by DNA based on the
A260/280 ratio, and from contamination by phenol and proteins based on the A260/230 ratio.
The cDNA sequencing libraries  were prepared using the 3’-method, thus primarily using
mRNA out of the total isolated RNA as a  template for reverse transcription. An important
advantage of this method is a lack of the transcript length bias – an overrepresentation of the
longer transcripts  in the assigned coverage of reads  that is  derived by the standard cDNA


66

sequencing library preparation , where the mRNA template is fragmented before reverse
transcription. The high -throughput sequencing was  performed by HiSeq2500 (Illumina)  as
described in chapter 5.7 and produced at least 6.5 million 50-bp sequencing reads for each RNA
sample. The obtained data were analyzed using a common RNA sequencing data analysis
workflow as described in chapter 5 .7.2. Following alignment of the sequencing reads to the
human genome, quantification, and normalization of data, at least 9394 transcripts with ≥ 10
assigned read counts were identified in any given sample.


Figure 8. The typical workflow of a transcriptome analysis with RNA sequencing.

The expression of the genes encoding BK-α and BK-β4 subunits was confirmed in both human
dermal fibroblasts and astrocytoma cell li nes (Table 6) . T he presence of a few counts of
transcripts of BK-β3 subunits was noted occasionally in some samples of these cell line s. A
notable divergence from the previously reported data was the complete lack of detectable
transcripts associated with the BK-β2 subunit in dermal fibroblasts. As expected, no transcripts
encoding BK-β1 or any of the four BK-γ subunit types were identified in the transcriptomes of
studied cell lines.




67

Table 6. Evaluation of expression of the genes encoding BK channel subunits by the RNA
sequencing. The gene expression values are shown as average normalized transcript counts (n
= 3). Transcript counts can appear as non-integer numbers due to the data normalization.
Gene
Associated BK
protein subunit
Transcript counts in
astrocytoma
Transcript counts in
fibroblasts
KCNMA1 BK-α 374,39 30,39
KCNMB1 BK-β1 0 0
KCNMB2 BK-β2 0 0
KCNMB3 BK-β3 0,25 0,92
KCNMB4 BK-β4 10,67 13,32
LRRC26 BK-γ1 0 0
LRRC52 BK-γ2 0 0
LRRC55 BK-γ3 0 0
LRRC38 BK-γ4 0 0

In a study of weakly expressed genes , RNA sequencing may have certain  limitations, as the
very low read count values are sometimes associated with noise and can be filtered out during
data normalization . Therefore, to validate the data obtained with RNA sequencing,  the
expression of genes encoding mitoBK subunits was studied with a qualitative RT-PCR. The
isolated RNA was transcribed to cDNA using a commercial ly available  kit under typical
thermocycling conditions as described in chapter 5 .5. The primer annealing temperature was
optimized prior to the assay to obtain a specific and high  yield of the intended product. The
cDNA amplicon was then used as a template in the RT-PCR as described in chapter 5.5.
Since the standard RT-PCR setup of the initial screening has also failed to detect the expression
of BK-β2 subunits previously reported for fibroblasts, the RT-PCR for detection of KCNMB2
was designed in the “nested” configuration using two sets of primers: an outer set producing a
larger product, and an inner set . Thus, weakly expressed or alternatively spliced transcripts
could be detected.



68


Figure 9. Analysis of the expression of BK-α and BK-β subunits in U-87 MG astrocytoma
cells and human dermal fibroblasts with RT-PCR. A. Amplification products of GAPDH,
KCNMA1 (α), KCNMB1 (β1), KCNMB3 (β3), KCNMB4 (β4) from cDNA of astrocytoma cells
(A) or fibroblasts (F); (M) marker 100 bp DNA ladder. B. Amplification products of KCNMB2
in a standard PCR configuration (β2), the first round of nested PCR configuration with outer
primers (β2-N1), and the second round of nested PCR configuration with inner primers (β2 -
N2). The designed PCR product sizes are specified in chapter 5.6.

The RT-PCR reaction has detected the expression of KCNMA1 in both cell types  (Figure 9).
The observed bands were singular, corresponding to the predicted PCR product size, and their
signal was sharp  and strong . The analysis of expression of auxiliary BK-β subunits in
astrocytoma cells confirmed  expression of KCNMB3 and KCNMB4, and a faint band
demonstrating few transcripts of KCNMB1 was present . In fibroblasts,  the expression of
KCNMB3 and KCNMB4 was confirmed. However, t he designed product of  KCNMB2 of
appropriate size was not produced by RT-PCR reactions in regular or nested configurations in
either cell type (the blurred bands sized about 100 bp do not correspond to the intended product
size and are likely an unspecific byproduct of the PCR). Thus, the data obtained with the RNA
sequencing study were in alignment with the findings of RT-PCR.
Next, to identify whether a fraction of  BK channel proteins is targeted to mitochondria, their
presence in the mitochondrial isolation of astrocytoma, control and CO X8A-deficient
fibroblasts was evaluated by a Western blot analysis (Figure 10). Mitochondrial isolation was
performed according to the protocol described in chapter 5.8. Proteins were separated in SDS-
PAGE gels under reducing conditions and subsequently  blotted onto the PVDF membrane as
described in chapter 5.9. The membrane was then subsequently treated in three solutions, with
alternating washing steps in between, according to the procedure covered in detail in chapter
5.9. Briefly, a blocking solution was applied firstly to minimize noise and non-specific antibody
binding; next, a solution containing primary antibodies raised against proteins of interest;
finally, a solution containing appropriate secondary horseradish peroxidase (HRP)-conjugated
antibodies raised against the host species of the primary antibodies. To visualize the signal, a



69

reagent containing chemiluminescent HRP substrate was applied to the membrane, and the blot
signal was captured using either analog (X -ray film) or digital (camera -based charge-coupled
device) technologies.
Western blot analysis identified the presence of the pore-forming BK-α subunit, as well as the
auxiliary BK-β3 and BK -β4 subunits in the mitochondrial fraction of astrocytoma cells and
human dermal fibroblasts (Figure 10). In Western blot analysis, the monoclonal antibody raised
against the cytoplasmic domain of the BK-α subunit has detected two bands: a predicted band
migrating at approximately 130 kDa, and a band migrating below 55 kDa. Interestingly, while
most KCNMA1 protein-coding transcripts encode 100-130 kDa sized peptides, a splice variant
KCNMA1-226 listed in the Ensembl database encodes a smaller 52 kDa peptide that can  be
recognized by this antibody and contains three transmembrane domains. However, because the
composition of this protein band has yet  to be validated , further immunoblotting studies
concentrated on observation of the bands that match the canonical full-sized BK-α protein.


Figure 10. SDS-PAGE and W estern blot analysis of expression of mitoBK protein
subunits in a mitochondrial fraction in U -87 MG astrocytoma cells and human dermal
fibroblasts. Each lane contains 50 µg of protein of mitochondrial preparation  of astrocytoma
cells (AW), control fibroblasts (FW), or fibroblasts with a mutation in COX8A (FM).

Thus, the analysis of gene expression  in the astrocytoma cell line and dermal fibroblasts
confirmed the expression of pore-forming BK-α subunits, as well as a small amount of auxiliary
BK-β3 and BK-β4 subunits. Furthermore, immunochemical analysis has shown that a fraction



70

of translated BK channel proteins is targeted to the mitochondria of these cells.  Notably, the
protein amount of the mitoBK -α subunits was higher in the mitochondria of the astrocytoma
cells than in the dermal fibroblasts, corresponding to the higher expression of KCNMA1 in this
cell type. Therefore, the presence of mitoBK channels in the studied cellular models was
validated.



71

6.2. Single-channel electrophysiological properties  of mitoBK channel s in
isolated mitochondria of astrocytoma cells

After the molecular presence of mitoBK channels in the studied models was confirmed, its
electrical activity was examined by patch clamping the IMM . This method is regarded as a
“golden standard” for studying single-molecule biophysical properties of ion channels. Since it
allows for precise control over the solute environment of a patch of membrane containing ion
channels, it is a perfect tool for ch aracterizing their functional modulation by various
compounds.
Mitochondria isolated from human astrocytoma U-87 MG cells were used as a study model in
the patch -clamp experiments . The primary reason for using this cellular model is that the
mitoBK channels are more abundant in the IMM of astrocytoma cells than in the fibroblasts ,
which increases the chances of finding this channel in a given patch of membrane. Furthermore,
mitochondrial isolation from astrocytoma is relatively efficient, and  a gigaseal be tween the
IMM and the patch pipette glass can be successfully formed in a reasonable number of trials.
The procedure of mitochondrial patch-clamp is well-established, and its schematic depiction is
shown in Figure 11. The access to the IMM is achieved by disruption of the OMM by swelling
through a sequential treatment of an aliquot of isolated mitochondria in hypotonic and
hypertonic solutions as described in chapter 5.11. This procedure leaves a characteristic “cap”-
a remnant of the OMM attached to the m itoplast. The presence of these “caps”, as well as the
size and transparency of the created vesicles, were the criteria for distinguishing mitoplasts
from cellular debris. The purity of the mitochondrial fraction selected by this approach has been
previously confirmed by a variety of techniques, including single -mitoplast PCR, which
confirms the presence of mitochondrial DNA within the patched vesicles 71,159.

Figure 11. A schematic depiction of patch-clamp of inner mitochondrial membrane.



72

Patch-clamp experiments confirmed the m itoBK activity  by its distinct biophysical
characteristics: dual regulation by voltage and Ca2+, conductance, current-voltage relationship,
and a  distinct pattern of BK channel kinetics (Figure 12).  The typical mitoBK channel
conductance, calculated as a slope of the I/V curve, was 289 ± 8 pS.


Figure 12. Biophysical properties of mitoBK channel of astrocytoma mitochondria in the
symmetrical 150/150 mM KCl isotonic solution containing 100 µM Ca 2+. (A) A typical
recoding of single-channel mitoBK channel activity is shown.  (B) V oltage dependence of
mitoBK open probability (Po). (C) Current-voltage relationship of mitoBK channels.

Since the patches of the IMM were p repared in the inside -out patch-clamp configuration, the
matrix side of the IMM was expose d to the perfusion bath containing experimental solutions.
The C-terminal part of the channel, which contains the Ca 2+ binding regions, was facing the



73

matrix compartment of mitochondria, as evidenced by the decrease of mitoBK channel activity
in response to a change in Ca2+ concentration in the perfusion bath (Figure 13 A).  Regulation
of channel activity by the established mitoBK channel modulators further validated their
identity. Thus, the application of a mitoBK opener CGS7184 activated the channels, while the
application of a mitoBK blocker paxilline inhibited channel activity (Figure 13B).
In conclusion, the initial assessment has confirmed the functional activity of the mitoBK
channel in the IMM of the astrocytoma cells. The channels had the characteri stic biophysical
activity profile and dual regulation by voltage and calcium ions. The activity of mitoBK
channels was modulated by paxilline and CGS7184 in the perfusion solutions.




74



Figure 13.  Modulation of mitoBK channel activity. ( A) Ca 2+-dependent regulation of
mitoBK channel activity. (B) Pharmacological modulation of mitoBK channel activity by 1 µM
mitoBK activator CGS7184 and 1 µM inhibitor paxilline. In a representative recording in a
patch-clamp experiment, the perfusion solution s are applied to the matrix s ide of the IMM
patch.



75

6.3. Analysis of interaction of mitoBK channel with the respiratory chain in
the model of mtDNA-depleted astrocytoma cells

One of the questions addressed in this study  was how the mitoBK channel interacts with the
respiratory chain proteins  in the IMM . A cellular model line bereft of mtDNA would be a
particularly valuable research tool  in this investigation . Firstly, it would yield insight into
whether mitochondrial retrograde signaling pathways triggered by mtDNA deple tion impact
the BK channels in mitochondria and cell membrane . Secondly, mtDNA -encoded OXPHOS
subunits are essential for the electron flow through the ETC, and in their absence, the fully
functional ETC complexes I, III, and IV cannot be assembled. Thus, by depleting mtDNA, a
useful cellular model can be established for the study of the multiprotein complexes formed
between the mitoBK channels and the respiratory chain proteins.

6.3.1. Generation of mtDNA-depleted astrocytoma cell line

To accomplish the generation of the mtDNA-void cells, human astrocytoma U-87 MG cell line
was chosen as a study model, considering its metabolic profile  with a proclivity to aerobic
glycolysis. Namely, to provide metabolic support to neurons, normal astrocytes have a high
capacity for surplus glycolytic lactate synthesis, alongside the active respiratory generation of
ATP (a Pasteur effect) 160. Malignantly transformed astrocytes, such as U-87 MG astrocytoma
tumor cells , additionally favor aerobic glycolytic pa thways under normoxic condition s (a
Warburg effect). As a consequence, this cell type was anticipated to have a higher probability
of surviving the mtDNA loss, what might have turned fatal for other cell types.
Treatment with a non -hydrolyzable nucleosid e analog 2′,3′ -dideoxycytidine (ddC), which is
characterized as a high-affinity inhibitor of the mitochondrial DNA polymerase-γ (POLG), was
selected as a method to induce mtDNA deficiency in astrocytoma cells  161. The cell culture
medium was supplemented with uridine as a precursor for pyrimidine salvage synthesis. Thus,
although in vitro treatment with 20 µM ddC impaired the growth rate of U -87 MG cells, their
viability was maintained. However, it is worth noting that  an a ttempt of  increasing the
concentration of ddC in the growth medium to 50 µM had a sharply negative effect on the cell
survival, likely due to the low-affinity binding of ddC to the nuclear DNA polymerases.



76

6.3.1.1. Confocal microscopy imaging of the mito chondrial network of astrocytoma cells
upon mtDNA depletion

To visualize the effect of the ddC treatment on the morphology of U -87 MG cells and their
mitochondrial network, confocal microscopy imaging was employed. The cells were fixed in a
PFA solution, permeabilized in a saponin -containing solution, and immunostained with a
primary antibody raised against VDAC, and Alexa Fluor 633-conjugated secondary antibody.
The protocol of sample preparation and immunostaining is described in detail in chapter 5.10.


Figure 14. Mitochondrial network in the astrocytoma WT (A) and ddC -treated cells (B)
visualized by confocal microscopy.  Nuclei were visualized with DAPI (blue), and
mitochondria were visualized with VDAC (red).

After three weeks of treatment with 20 μM ddC, a pronounced change in the size and shape of
the cells was observed (Figure 14). In comparison to the characteristic polygonal appearance of
U-87 MG cells, the ddC -treated cells had a larger surface and a more rounded and irregular
morphology. Immunofluorescence staining using antibodies against VDAC revealed that
mtDNA-depleted cells retain mitochondrial structures, however, the mitochondrial network
appears to be more fragmented.





77

6.3.1.2. Determination of cellular respiration of ddC-treated astrocytoma cells

To determine whether the depletion of mtDNA has been achieved, several tests were performed
in this study:
 on the functional level: respiration of cells was evaluated by oxygraphy;
 on the genetic level: the transcriptome profile of ddC -treated cells was studied with a
focus on mtDNA-encoded genes;
 on the protein level: Western blot analysis was performed to identify the absence of
mtDNA-encoded ETC subunits.
The progress of mtDNA depletion  can be followed indirectly through  the functional
bioenergetics analysis. Since the key components of th e OXPHOS complexes I, III, IV and V
are compromised in mtDNA-depleted cells, the oxygen consumption rate by their mitochondria
is significantly decreased. Thus, to identify the depletion of mtDNA in U-87 MG astrocytoma
cells, cellular respiration was measured with the Oroboros oxygraph , as described in chapter
5.12.
The basal respiration was studied in the cell culture medium containing glucose, pyruvate, and
glutamine as metabolic energy substrates. Afte r reaching stable basal respiration, sequential 1
μM additions of protonophore CCCP were used to induce uncoupling. In the WT astrocytoma
cells, the additions of CCCP led to an increase in cellular respiration in a dose -dependent
manner (Figure 15). In the astrocytoma cells treated with ddC for 3 weeks, a small level of basal
oxygen consumption was observed, possibly due to the activity of non -mitochondrial
oxygenases. However, the additions of CCCP did not display any significant effect on the
oxygen consumption rates in the ddC-treated cells, what indicated that respiration was virtually
abolished and mtDNA depletion occurred.



78

Figure 15 . Treatment of U -87 MG astrocytoma cells with ddC abolishes cellular
respiration. Oxygraphic evaluation of cellular respiration of one million U-87 MG astrocytoma
cells: WT ( solid lines ) and upon treatment with ddC ( dash-dotted lines ); in blue , O 2
concentration in nmol/ml; in brown, O2 slope in pmol/(s*ml). Arrows indicate the addition of
1 µM CCCP to the oxygraph chamber.

6.3.1.3. Characterization of the expression of the mitochondrial genes in mtDNA depleted
line with RNA sequencing

To confirm depletion of mtDNA, the change in the expression of mtDNA-encoded genes in the
WT and ddC-treated astrocytoma cells was evaluated by RNA sequencing data.
Several statistical tools are available for the analysis of the differential gene expression of the
RNA sequencing data, with R/Bioconductor DESeq2 and EdgeR being among the most widely
used ones 162. The normalization methods in both tools are based on the null hypothesis that no
differential expression occurs for most genes. The statistical model of EdgeR calculates a
general dispersion parameter using the Cox-Reid profile likelihood and then evaluates per-gene
dispersion using the Bayesian model 163. DESeq2 employs a slightly different approach, where
individual values of gene dispersion are first estimated before fitting them to a model. Although
the results obtained by these two statistical strategies are usually well-aligned, the normalization
method of DESeq2 is more robust to the low expressed genes, since to increase the statistical



79

power of EdgeR analysis, it is commonly practiced to apply filtering for the genes with the low
expression values that are considered to have low biological relevance.
A first look at the results of the differential gene expression analysis performed with both
EdgeR and DESeq2 shows that about 7% of differentially expressed transcripts were found by
the EdgeR algorithm, and about 5% were identified as such by DESeq2 (Table 7).

Table 7. Estimation of the numb er of differentially expressed  genes in the U -87 MG
astrocytoma ddC-treated cells versus astrocytoma WT cells using EdgeR or DESeq2.
Statistical tool used for analysis
Upregulated
transcripts
Not differentially
expressed
Downregulated
transcripts
EdgeR 422 12885 476
DESeq2 413 15788 422

Notably, both approaches produce the  mean-difference (MD) plots of the differential gene
expression in the ddC -treated U-87 MG astrocytoma cells, which in the bottom right section
reveal a cluster of the highly expressed  genes that ar e strongly downregulat ed (Figure 16 ).
These genes denote the decreased transcription of mitochondrial genes following the mtDNA
depletion.




80



Figure 16 . The MD plots of differential gene expression in the ddC -treated U -87 MG
astrocytoma cells. (A) The analysis performed with DESeq2 includes all genes with non-zero
mapped read counts.  (B) Using EdgeR analysis, the total gene transcript reads are filtered to
exclude genes with low expression (defined as ≤ 0.5 counts per million in at least two samples).
For both methods, the false discovery rate is defined as < 0.05 . Each identified  sequence is
denoted as a dot, the upregulated transcripts are shown in red, and the downregulated ones are
in blue. Log(FC), the binary logarithm of fold change; log 2(CPM), the binary logarithm of
counts per million.

While the key findings were confirmed with both methods, the rest of this work will refer only
to the results of the differential gene expression analysis conducted with DESeq2.
The read counts of the transcripts of 13 mitochondrial pro tein-encoding genes were identified
among the most downregulated genes in the ddC -treated U-87 MG astrocytoma cells (Figure
17). The evaluated p-values of the differentially expressed mitochondrial-encoded genes were
distributed in the range between p = 2 ∙ 10-13 and p = 2 ∙ 10 -155, and log 2(FC) values – in the
range between log2(FC) = - 4.22 and log2(FC) = - 6.83 (for COX2 and ND1, respectively).




81


Figure 17 . Expression of mtDNA-encoded genes is significantly downregulated in the
ddC-treated U-87 MG astrocytoma cells. The volcano plot graphically identifies differential
expression of genes: the value of –log10(p-value) is plotted on the y -axis against the log2(fold
change) on the x-axis. The change in value for each assigned gene sequence is depicted by one
point. The up regulated transcripts are label ed in red, downregulated – in blue,  and the
transcripts without a statistically significant change in expression (p > 0.05) – in grey.

Therefore, differential gene expression analysis confirmed mtDNA depletion on the level of the
decrease in mtDNA expression in the ddC-treated astrocytoma cells.





82

6.3.2. Analysis of complexes of mitoBK channels  with the respiratory chain
proteins in astrocytoma cells

The previous studies have shown functional interaction of the mitoBK channels with the
electron transport chain. The physical interaction of the mitoBK-β4 subunit with the
cytochrome c oxidase was implicated in this phenomenon  104. However, relatively little is
understood about the interaction of the pore -forming subunit mitoBK-α with the COX within
the respiratory chain supercomplexes.
A number of recent studies examined the molecular mechanisms of mitochondrial retrograde
signaling. Yet, no attempts have been made to investigate the potential invol vement of the
potassium channels, and in particular, of the mitochondrial potassium channels as regulators of
ion fluxes in this organelle.
To address these gaps in the research, the interaction of the mito BK-α pore-forming subunit
with the ETC was investigated, taking advantage of the developed mtDNA-depleted U-87 MG
astrocytoma cell model.

6.3.2.1. Assessment of protein complexes of mitoBK channels with the respiratory chain
in astrocytoma cells

Identification and characterization of multiprotein complexes are immensely importan t in
gaining a greater understanding of protein -protein interaction networks. By allowing  the
separation of protein complexes under non -denaturing conditions, blue -native PAGE (BN -
PAGE) became a versatile tool to study membrane multiprotein complexes in th eir native
conformation in different systems.  This method was used for the evaluation of the steady-state
protein complexes between mitoBK channels and the ETC complexes in the mitochondrial
isolation from human astrocytoma U-87 MG cell line.
In the initi al assay, two approaches for mitochondrial preparation were evaluated for the
downstream application in the separation of mitochondrial proteins: a standard differential
centrifugation-based mitochondrial isolation method was compared to the column -based
magnetic labeling method with anti -TOM22 beads , as described in chapter 5.8. The
mitochondrial sample preparation was pe rformed as reviewed in chapter 5 .9. Due to its
preservation of the native stoichiometry of the respiratory chain SC, a non-ionic mild detergent


83

digitonin was selected for solubilization of the membrane protein complexes. The protein of
mitochondrial samples obtained using these two isolation approaches from the astrocytoma
cells were separated by  the BN-PAGE and identified by  subsequent Western blotting (Figure
18).


Figure 18 . Comparison of the protein complexes of human astrocytoma U -87 MG
mitochondria obtained with the different mitochondrial isolation methods . The
mitochondrial preparations (100 µg protein/lane) of the astrocytoma WT cells were solubilized
with 1% digitonin  and resolved by BN -PAGE followed by Western blotting. M – magnetic
beads-based isolation, C – “classical” differential centrifugation -based method. On the right,
the protein complexes formed with COX: IV – COX monomer, IV2 – COX dimer, III2 + IV –
dimer of complex III and COX, I + III2 + IV – the respirasome.

The strong signals of mitoBK-α and mitoBK-β4 channel subunits were found in mitochondrial
preparations from the astrocytoma WT cells obtained by both methods. A band migrating at the
molecular weight, which corresponded to the tetramer of mito BK-α subunits associated with
mitoBK-β4, was detected in both preparations. However, the mitochondrial isolation obtained
with the magnetic beads-based method had two more apparent signals of the mitoBK-α subunit:
migrating at the MW about 440 kDa, and at the size slightly larger than a mitoBK-α monomer
– about 130 kDa. Both signals of complexes formed by the mitoBK-α subunit corresponded to
the signals detected by an antibody against the mitoBK-β4 subunit.
Unfortunately, it became apparent that the magnetic beads -based mitochondrial isolation had
several crucial drawbacks, which made this method unsuitable for further BN -PAGE studies.



84

Firstly, the column separation was per formed at room temperature, what could affect the
stability of the protein complexes. Secondly, the obtained mitochondrial solution contained
residual magnetic beads, which interfered with the colorimetric methods of protein
quantification and led to  an incorrect estimation of the protein amount. A treatment with
protease to remove the beads would risk damaging the protein complexes in the sample.
Therefore, further studies were limited to using the “classical” isolation method based on the
differential centrifugation.
To address one of the  research questions posed in this work , the interaction of the mitoBK
channel subunits with the ETC proteins was evaluated in two models: mitochondria isolated
from the WT astrocytoma, and mitochondria of mtDNA -depleted astrocytoma cells lacking
crucial subunits of respiratory chain complexes. The protein complexes formed by the mitoBK-
α, mitoBK-β4, and COX4 were resolved with BN-PAGE and immunoblotted (Figure 19).
In the mitochondrial preparation of the WT cells, the mitoBK-α signal was distributed between
three protein complexes. Firstly, due to the high protein amount per lane, it  was possible to
visualize the co-migration of the high molecular weight complexes of mito BK-α subunit with
the COX as a part of respirasomes, which were migrating above 1 MDa. Yet, this protein
complex was the least abundan t form among the three mitoBK -α-containing fractions. The
largest amount of BK-α was present in a protein complex co-migrating with the BK-β4 subunit
at the molecular weight corresponding to the fully assembled channel (consisting of a tetramer
of mitoBK-α subunits associated 1:1 with mitoBK-β4 subunits - about 580 kDa) and higher.
The smeared appearance of this band on the Western blot was also persistent after solubilization
of mitochondrial preparation with another detergent - n-Dodecyl β-D-maltoside (not shown).
Considering that the m itoBK channel was reported to interact with multiple mitochondrial
proteins 82, this signal can actually contain several populations of the  channels with different
protein partners. The third fraction of mitoBK in the WT cells was co -migrating with the BK-
β4 subunit above 440 kDa below the expected size of the fully assembled mitoBK channel, and
co-localized with a COX dimer.



85


Figure 19. MitoBK channel interacts with COX and is a part of the RC supercomplexes.
The mitochondrial preparations (150 µg protein/lane) of the astrocytoma WT and mtDNA -
depleted cells wer e solubilized with 1% digitonin  and resolved by BN -PAGE foll owed by
Western blotting. S.e. – short exposure, l.e. – long exposure.

As predicted, the mtDNA -depleted cells were deficient in COX complexes, and the residual
COX4 signal was contained in one protein complex not characteristic of any typical COX
assemblies in the WT mitocho ndria. Notably, the comparative analysis showed that mtDNA
depletion affects both the abundance and the composition of the protein complexes formed by
the mitoBK-α and mitoBK-β4. Specifically, only a protein complex of the size corresponding
to the tetramer of BK-α subunits associated with the BK-β subunits was visualized. The amount
of this protein complex was markedly lower than in the WT cells. The other two complexes of
the mitoBK-α subunit co-migrating with the COX dimer and COX in the respirasomes wer e
absent. Therefore, these results indicate that the pore-forming mitoBK-α subunit interacts with
the COX and can be a part of the respiratory chain supercomplexes in astrocytoma
mitochondria.

6.3.2.2. Determination of mitoBK protein amount upon mtDNA depletion of astrocytoma
cells

Several potential reasons could underlie the observed decrease in the mitoBK-α protein amount
in the mitochondrial preparation of ddC-treated cells. Since there are indications that mitoBK-
α follows the mitochondrial import pat hway through TOM/TIM complexes, the observed
decreased protein amount could be induced by the impairments in the mitochondrial transport
of nuclear-encoded proteins.



86

Thus, the levels of complexes formed by other nuclear -encoded proteins in the IMM were
visualized in the WT and ddC-treated cells by BN-PAGE/Western blotting (Figure 20).


Figure 20. Downregulation of the  evaluated IMM protein complexes is observed in the
ddC-treated cells. The mitochondrial preparations (100 µg protein/lane) of the astrocyt oma
WT (AW) and mtDNA -depleted cells (AD) were solubilized with 1% digitonin and resolved
by BN-PAGE followed by Western blotting.

The amounts of all evaluated IMM proteins were decreased in the mtDNA-depleted cells, which
may indicate the impaired prote in import due to the loss of the membrane potential generated
by ETC complexes. Nevertheless, the magnitude of the downregulation was different for each
of the tested proteins. The decrease in the total abundance of the mito BK-α signal was more
strongly pronounced than a decrease in another ion channel of the IMM – the mitochondrial
calcium uniporter (MCU). Similarly, the total amount of the protein complexes containing
subunit SDHA of the complex II was decreased to a smalle r extent than the complexes with
subunit COX5A of complex IV , which were likely misassembled and subjected to the
degradation due to the lack of the essential mtDNA-encoded components.
While BN-PAGE is a sensitive method for the study of protein -protein interactions, the SDS-
PAGE is more suitable for the comparative analysis of the total protein levels by enhancing
epitope availability to the antibodies and decreasing the interference of lipids. Thus, to verify
the decrease in the protein amount of the mito BK-α subunit, the SDS-PAGE/Western blotting
was performed (Figure 21).



87


Figure 21 . The total BK-α amount in the mitochondria of the mtDNA -depleted
astrocytoma cells is decreased. SDS-PAGE followed by immunoblotting of the mitochondrial
preparation of the astrocytoma WT (AW) and mtDNA-depleted cells (AD).

The results of the study confirmed the decrease in the total amount of the mitoBK-α protein in
the mitochondria of the mtDNA-treated astrocytoma cells.

6.3.2.3. Transcriptome profiling in mtDNA -depleted astrocytoma cells with high -
throughput RNA sequencing

Another molecular mechanism underlying an observed downregulation in the mitoBK-α protein
amount after the mtDNA depletion can be a  decrease in the KCNMA1 transcription. To
investigate whether the decrease in the amount of the mitoBK-α protein occurs on the level of
gene expression, the transcriptome profiling of the astrocytoma WT and mtDNA-depleted cells
was performed with RNA sequencing.
RNA sequencing detected the expression of three genes encodin g BK channel subunits in the
ddC-treated cells: KCNMA1, KCNMB3,  and KCNMB4 (Figure 22 ). The expression of the
KCNMA1 encoding mitoBK-α subunit was decreased and considered statistically significant:
log2(FC) = -1,30; p < 2 ∙ 10-4. The mean amount of normalized KCNMB4 read counts appeared
higher in the ddC-treated cells, but was not considered statistically significant: log2(FC) = 1,10;
p = 0.15. The expression of KCNMB3 was identified in 2 samples of ddC-treated cells compared
to 1 sample of the WT cells and was not evaluated.




88



Figure 22. Expression of KCNMA1 is significantly downregulated in the ddC -treated U-
87 MG astrocytoma cells.  The volcano plot graphically identifies differential expression of
genes: the value of –log10(p-value) is plotted on the y-axis against the log2(fold change) on the
x-axis. The change in value for each assigned gene sequence is depicted by one point. The
upregulated transcripts are labeled in red, downregulated – in blue, and the transcripts without
a statistically significant change in expression (p > 0.05) – in grey.




89

To validate the results of KCNMA1 decrease obtained with RNA sequencing,  a real-time
reverse-transcription polymerase chain reaction (qRT -PCR) was performed  as described in
chapter 5.5. The decrease in the ex pression of KCNMA1 was confirmed in a qRT -PCR assay
with GAPDH as a reference gene (Figure 23).


Figure 23 . A decrease in KCNMA1 expression in ddC -treated astrocytoma cells  is
confirmed by qRT-PCR. The expression level of KCNMA1 in relation to GAPDH is shown in
astrocytoma cells (n = 3). (*) p < 0.05

Next, to determine whether the decrease in KCNMA1 expression could be a part of the systemic
downregulation of gene expression by transcriptional factors, the activation of mitochondrial
retrograde signaling pathways, and expression of the downstream target genes of known or
suggested regulators of KCNMA1 transcription were characterized by RNA sequencing.
Mitochondrial deficiency can trigger several signaling pathways to evoke a transcriptional
response fr om the nucleus. The key mitochondrial retrograde signaling pathways are the
mitochondrial integrated stress response (ISR) and the mitochondrial unfolded protein response
(mtUPR). To identify the signaling pathways invoked by the mtDNA depletion in the
astrocytoma cells, the expression of the master transcriptional controllers in the ISR and mtUPR
and their primary targets were evaluated.
The regulatory response of the ISR pathway induces a global translational downregulation and
a selective upregulation of transcription favoring the stress response genes. The stress-detecting



90

signaling pathways triggering the ISR converge at the phosphorylation of eIF2α that promotes
translation of the master transcriptional regulator of the ISR - activating transcription factor 4
(ATF4) - and its translocation to the nucleus. To analyze whether the ISR is activated in
response to the mtDNA depletion, the expression of ATF4 and its primary downstream targets
- DDIT3, ATF3, CHAC1, PCK2, PPP1R15A – was evaluated with RNA sequencing (Fi gure
24A). The expression of these genes was markedly upregulated – correspondingly, log2(FC):
1.84, 1.92, 2.19, 4.57, 2.26, 1.28; p -values: 1∙10 -8, 2∙10 -3, 8∙10 -4, 4∙10 -26, 1∙10 -7, 6∙10 -3.
Therefore, the depletion of the mtDNA by ddC treatment activated mitochondrial signaling
pathways triggering the ISR.
Impaired mitochondrial protein import and accumulation of orphaned ETC protein subunits can
induce proteotoxic stress that activates mitochondrial unfolded protein response (mtUPR). To
increase protein quality control and promote protein degradation, the regulatory mechanisms of
mtUPR increase the transcription of mitochondrial proteases such as Lonp1, ClpP, paraplegin,
Clpx, and Yme1l1 164. Additionally, the expression of mitochondrial chaperones Hsp70, Hsp60
and Hsp10 is upregulated in mtUPR to prevent protein aggregation and facilitate protein folding
and assembly into the multiprotein complexes. To identify whether these processes were
initiated following mtDNA depletion, differential expression analysis of genes encoding
mitochondrial proteases ( LONP1, CLPP, SPG7, CLPX, YME1L ) or chaperones ( HSPA2,
HSPD1, HSPE1) was performed. Interestingly, no signs of the transcriptional upregulation
typical for mtUPR were observed (Figure 24B). Thus, the ISR is the main retrograde signaling
pathway initiated by the mtDNA depletion in astrocytoma cells.



91



Figure 24. The integrated stress response pathway is activated in the mtDNA -depleted
astrocytoma cells. The volcano plots  of differential expression analysis with a focus on  the
following genes: (A) transcriptional regulators of the ISR and their primary downstream targets;
(B) genes mediating the mtUPR. The value of –log10(p-value) is plotted on the y -axis against
the log2(fold change) on the x -axis. Each identified gene is depicted as a dot, the upregulated
genes are shown in red, the downregulated ones – in blue, and the genes without a statistically
significant change in expression (p > 0.05) – in grey.

The expression of nuclear factor E2 -related factor 2 (Nrf2) is one of the signal ing branches
downstream of ATF4.  A functional network of the Nrf2-coregulated genes involves key
mediators of cytoprotecti ve antioxidant signaling. Specif ically, Nrf2 regulates  the expression
of the genes encoding the components of the glutathione antioxidant system, such as glutamate-
cysteine ligase subunits ( GCLC, GCLM ); thioredoxin-based enzyme system, such as
thioredoxin (TXN), thioredoxin reductase 1 ( TXNRD1) and sulfiredoxin ( SRXN1); an enzyme
involved in heme catabolism - heme oxygenase 1 ( HMOX1) 165. Interestingly, the expression
of KCNMA1 is a known target of transcriptional regulation by Nrf2 in the coronary smooth
muscle cells. To identify whether KCNMA1 is co -regulated with these downstream effectors
of Nrf2, differential expression analysis with a focus on the genes involved in a functional
antioxidant system was performed. In mtDNA -depleted cells, the expression of most of the
analyzed genes under the transcriptional regulation of  Nrf2 was markedly upregulated,
indicating that Nrf2 is activated in response to oxidative stress (Figure 25A). However, since in



92

the arterial smooth muscle cells Nrf2 positively regulates the  expression of KCNMA1, other
molecular mechanisms are likely involved in the downregulation of KCNMA1 expression in the
mtDNA-depleted astrocytoma cells.
Low availability of NAD+ is a hallmark of mitochondrial dysfunction, and through the NAD+-
containing transcription factors it affects expression of their gene target s, such as sirtuin -1
(Sirt1). Through the interaction with the peroxisome proliferator -activated receptor gamma
coactivator-1α (PGC1α), Sirt1 cont rols mitochondrial biogenesis. The Sirt1/PGC1α-mediated
impairment in the oxidative metabolism and decrease in the expression of genes regulating
calcium homeostasis was des cribed in the SCA7 mice model 166,167. KCNMA1 is positively
regulated by PGC-1α due to the presence of PPAR response elements (PPRE) in the promotor
region, and it was reported as one of the downregulated genes under the Sirt1/PGC1α control
that were involved in calcium signaling 167. mtDNA depletion could potentially disrupt the
supply of NAD+ due to the lack of complex I activity. Thus, the expression of SIRT1 and the
primary downstream targets of  Sirt1/PGC1α-dependent regulation, such as NRF1, TFAM,
FOXO1, and ESRRA, was evalua ted in the ddC -treated astrocytoma cells (Figure 25B).
However, no significant change was observed in the differential expression analysis of these
genes. This result can indicate that the NAD+ pool was not affected in the mtDNA -depleted
cells, likely due to its regeneration in the glycolytic reduction of pyruvate.






93


Figure 25. Expression of genes under the control of Nrf2 is upregulated in the mtDNA -
depleted astrocytoma cells. The volcano plots of differential expression analysis with a focus
on the f ollowing genes: (A) antioxidant enzymatic functional network under the common
transcriptional control by Nrf2; (B) primary downstream targets of Sirt1/PGC1α transcriptional
co-activation. The value of –log10(p-value) is plotted on the y-axis against the log2(fold change)
on the x-axis. Each identified gene is depicted as a dot, the upregulated genes are shown in red,
the downregulated ones – in blue, and the genes without a statistically significant change in
expression (p > 0.05) – in grey.

To summarize, differential expression analysis in the mtDNA -depleted astrocytoma cells has
identified the following features of their transcriptome profile:
 the expression of the gene encoding mitoBK-α was downregulated;
 the depletion of mtDNA initiated the integrated stress signaling pathway;
 a lack of evidence indicating mitochondrial unfolded protein response signaling was
observed;
 the transcriptional upregulation of antioxidant enzymatic functi onal network under the
common transcriptional control by Nrf2 occurred;
 no change in the expression of the primary downstream targets of Sirt1/PGC1α
transcriptional co-activation was identified.




94

6.4. Evaluation of the effects of COX8A deficiency on the r espiratory chain
complexes and mitoBK channels

The results of the study of the interaction of the mitoBK channel with the ETC complexes  in
the cellular model lacking mtDNA revealed that the mitoBK channel interacts with the complex
IV through its α and β4 subunits and that the genetically induced downregulation of the channel
amount occurs. To further investigate how a deficiency in the partner ETC protein complex
affects the mitoBK channel, a different approach based on the model with an isolated deficiency
in COX was employed. Namely, human dermal fibroblasts derived from a patient with a
mutation in a nuclear-encoded structural subunit COX8A were used as a study model.
COX8A is the smallest nuclear -encoded protein subunit of COX. In the human cells, it
substitutes the subunit COX8B (COXVIIIH) commonly expressed in the most primate clades,
and the ubiquitous expression of COX8A is considered an adaptive evolutionary change in the
anthropoid RC machinery for optimized aerobic energy metabolism 168. However, the
molecular role of COX8A in the function of COX is still unknown. The model in  the focus of
this study is the single reported case of COX8A deficiency in a patient with Leigh syndrome
152.

6.4.1. Characterization of the respiratory chain in COX8A -deficient
fibroblasts

Since there was no available information of how the impairment of COX8A affects the COX
assembly and how the remaining COX was stabilized, in the first part of this work, the
functional effects of the loss in COX8A on the COX and its complexes with the other
respiratory chain enzymes were investigated.

6.4.1.1. Organization of the respiratory chain protein complexes upon COX8A deficiency
in fibroblasts

To identify the impact of the isolated COX deficiency on the ETC enzymes, the protein
complexes in the mitochondrial preparations of fibroblasts were resolved using BN-PAGE, and


95

subsequently immunoprobed with the antibodies for the subunits NDUFA9, SDHA, CORE2,
COX4 of the respiratory chain complexes I, II, III and IV.
In the control fibroblast cells, the subunit COX4 was contained in four distinct fully assembled
COX complexes (Figure 26 ). COX was distributed between the COX monomer form and the
respirasomes, while a smaller amount was also present in the SC containing CIII2 + CIV. In the
patient fibroblasts, the residual COX was largely stabili zed in the respirasomes, and no
monomer or supercomplex (CIII2 + CIV) forms of COX were detectable. Interestingly, in the
COX8A-deficient fibroblasts, an increase in the abundance of the remaining RC complexes was
observed.


Figure 26. COX is stabilized  in the supercomplexes in the COX8A -deficient fibroblasts.
BN-PAGE with subsequent immunostaining, digitonin 1%. Mitochondrial preparation of
control (C) and COX8A patient (P) fibroblasts, 100 µg protein/lane. On the right, COX -
containing protein complexes: IV – COX monomer, III2 + IV – supercomplex containing COX
and dimer of complex III, I + III2 + IVn – respirasomes.






96

6.4.1.2. Evaluation of the protein content of the residual complex IV subunits in COX8A-
deficient fibroblasts

Steady-state protein levels of the selected RC subunits were evaluated using SDS -PAGE with
subsequent immunoblotting. Consistent with the observed decrease in the COX protein
complexes in the COX8A-deficient patient fibroblasts, the protein amount of subunits COX1,
COX2, COX4, and COX5A was decreased to various degrees (Figure 27 ). Specifically, the
COX1 and COX5A protein signals were virtually not detectable, while the subunit COX4 was
the least downregulated one. The subunits of other respiratory chain complexes were not
compromised, and an increase in the amount of CORE2 was observed, in the line with the
increased amount of complex III protein shown with BN-PAGE.

Figure 27. Steady-state levels of the selected subunits of respiratory chain complexes in
the COX8A-deficient cells. SDS-PAGE with subsequent immunostaining: a) mitochondrial
preparation of control (C) and COX8A-deficient patient (P) fibroblasts, 50 μg protein/lane.

6.4.1.3. Analysis of the expression of protein subunits of complex IV and other respiratory
chain complexes in COX8A-deficient fibroblasts

To identify whether the changes in the RC protein levels can be explained by transcriptional
regulation, the effects of COX8A deficiency on the expression of the genes encoding OXPHOS
proteins were investigated with RN A sequencing. The analysis of  the transcriptome of
fibroblasts with COX8A deficiency identified a few diff erentially expressed RC protein -
encoding genes (Figure 28 ). Namely, a small decrease in the transcription levels of mtDNA -



97

encoded COX3 subunit and ATP synthase subunits A6L and A was observed (log2(FC): -0.91,
-0.87; p-value: 0.03, 0.01, correspondingly), while the expression of nuclear-encoded subunits
COX7A1 and COX7B of COX, and the amount of transcripts encoding complex III subunit 6,
and subunits C3 and DAPIT of complex V was slightly increased (log 2(FC): 1.16, 0.86, 0.73,
0.68, 0.74; p-value: 6*10-5, 0.02, 0.04, 0.03, 0.04, correspondingly).


Figure 28. Differentially expressed genes encoding OXPHOS complexes in the COX8A -
deficient fibroblasts.  Volcano plot of gene expression in the COX8A patient fibroblasts
compared to the control fibroblasts. Each identified gene sequence is represented by one point
on the graph. The identified differentially expressed genes encoding subunits of RC complexes
are shown in boxes.  The horizontal axis is log 2(fold change) between the sample means, the
vertical axis is -log10(P-value). Grey points are not statistically significant (p > 0.05), red points
show the upregulated genes (p < 0.05), blue points show the downregulated genes (p < 0.05).





98

6.4.2. The effects of the induced COX8A deficiency on the respiratory chain
in HEK293T cells

To further characterize the effects of the loss of COX8A on COX and ETC, a cellular model
was developed using the CRISPR/Cas9 genome editing system on HEK293T cells with the aim
of obtain a stable cell line containing mutations in COX8A.

6.4.2.1. CRISPR/Cas9 induction of COX8A deficiency in HEK293T cells

CRISPR/Cas9 is a modern gene-editing method that has gained wide use due to it s well-
characterized mode of action and efficiency. This technique allows introducing a mutation into
the target gene of interest, as the single guide RNA (sgRNA) directs the Cas9 enzyme with an
endonuclease activity to introduce a double-stand break to the bound DNA region . The break
is then repaired by non-homologous end joining, which tends to be imprecise and can lead to
deletions or insertions. In principle, any nuclear gene can be targeted by CRISPR/Cas9 system
in the immediate proximity to a region c ontaining protospacer adjacent motifs, which are
recognized by the sgRNA. For the purpose of this study, the dsDNA oligonucleotides encoding
sgRNA targeting exon 1 of COX8A were designed and cloned into the commercially available
plasmid as described in chapter 5.4.
HEK293T cells were transfected with the plasmid for CRISPR/Cas9, seeded as single-cell
colonies, and allowed to grow, as described in chapter 5.4. Following the establishment of stable
clonal colonies, screening for the mutants with a sought-after mutation in COX8A was
performed taking advantage of Sanger sequencing as described in chapter 5.6.
While no viable mutant cell line was characterized as a full COX8A knockout, two clonal
HEK293T cell lines were identified that harbored mutations in COX 8A, and were marked as
clone #13 and clone #14 (Figure 29).



99


Figure 29 . Characterization of the CRISPR/Cas9 -induced mutations in COX8A in the
HEK293T cells. Top panel, a fragment of the genomic DNA sequence of the WT COX8A exon
1 and translated peptide. The amino acids (AA) 1-25 form the mitochondrial targeting sequence
of COX8A, and are marked with a line. Bottom panel, corresponding COX8A genomic
sequences and translated peptide in the genetically modified HEK293T clones #13 and #14.
The mutated nucleotide positions are highlighted in red.

In clone #13, allele 1 contained a frameshift mutation by a 14-nt deletion, producing an aberrant
peptide from the amino acid position 22. In the second allele of clone #13 a 24 -nt deletion has
caused an in-frame deletion of the residues Pro22, Arg23, Ala24, Lys25, Ile26, His27, Ser28,
and Leu29. The amino acids at the positions 22 -25 are a structural part of the COX8A N -
terminal mitochondrial targeting sequence (MTS).
In clone #14, a 24 -nt in -frame deletion in allele  1 affects the MTS of COX8A, due to the
deletion of the residues Ala16, Arg17, Arg18, Leu19, Pro20, Val21, Pro22, Arg23. Notably, by
elimination of three out of four Arg residues in the COX8A MTS , this mutation disrupts a
positively charged amphipathic helix that is required for mitochondrial import of the COX8A
peptide. Moreover, four single -base substitutions in allele 1 result in a replacement of three
amino acids: Ile26Met, His27Leu, Ser28Pro. In allele 2 of clone #14 a 1 -nt insertion has
occurred, leading to the frameshift mutation in COX8A generating an aberrant peptide from
amino acid position 24.





100

6.4.2.2. The impact of COX8A deficiency on the organization of the respiratory chain
complexes in HEK293T cells

The COX activity was assessed in the mit ochondrial preparations of the fibroblasts and
HEK293T cells with COX8A deficiency and the respective controls (Table 8 ). COX activity
was evaluated relative to the citrate synthase (CS) activity 158. In all COX8A-deficient cell lines,
enzymatic activity of compl ex IV was decrease d, however, residual COX activity was still
detectable. The COX/CS activity ratio in the fibroblasts with the COX8A deficiency was
decreased 5-fold. In each of the HEK293T clones (#13 and #14) with different deletions of
COX8A mitochondrial targeting seque nce the COX/CS activity ratio was decreased about 3 -
fold.
Table 8. Enzymatic activities of COX8A-deficient cell lines

To identify how the mutations in COX8A in the gene -edited HEK293T cells affected the
organization of the respiratory chain, the protein complexes in the mitochondrial preparations
of HEK293T cells were resolved using BN -PAGE, and subsequently immunoprobed with the
antibodies for the subunits NDUFA9, CORE2, COX4 of the respiratory chain complexes I, III
and IV. In the WT HEK293T cells , the COX4 signal was distributed between four fully
assembled protein complexes as well: COX monomers, dimers, CIII2 + CIV, and respirasomes
(Figure 30). The largest amount of COX was incorporated into the respirasomes, and the COX
monomer was the least abundant form. In the COX8A -deficient HEK293T clone #13 with a
shorter deletion in the COX8A MTS, the largest amount of CO X was incorporated into
respirasomes. However, a significant fraction of COX was also contained within the SC of CIII2
Enzymatic activities (mU/mg
protein)
Control
fibroblasts
COX8A-
mutant
fibroblasts
HEK293T
WT
HEK293T
COX8A-
KD clone
13
HEK293T
COX8A-
KD clone
14
Citrate synthase 61,5 79,8 158,6 189,3 172,6
NADH:ubiquinone
oxidoreductase 11 3 5,2 4,1 1,6
Complex I/citrate synthase 0,17 0,04 0,03 0,02 0,01
Cytochrome c oxidase 81,4 20,6 81,3 32,5 27,3
Complex IV/citrate synthase 1,32 0,27 0,51 0,17 0,16


101

+ CIV, and to a smaller extent, in COX dimers. The monomer form of COX was practically
undetectable. The abundance of protein complexes c ontaining COX in the COX8A -deficient
clone #14 of HEK293T cells was significantly smaller than in both WT and clone #13 cells.
Most of the residual COX proteins were largely contained within the respirasomes, while only
trace amounts could be detectable wi thin the supercomplex of CIII 2 + CIV or the COX
monomer and dimer forms.


Figure 30. Organization of the respiratory chain in the CRISPR/Cas9 induced COX8A -
deficient HEK293T cells . BN-PAGE with subsequent immunostaining, digitonin 1%.
Mitochondrial preparation of the WT and COX8A-deficient HEK293T cells – clone #13 (C13)
and clone #14 (C14), 100 µg protein/lane. S.e. and l.e. – short exposure and long exposure. On
the right, COX-containing protein complexes: IV – COX monomer, IV2 – COX dimer, III2 +
IV – supercomplex containing COX and dimer of complex III, I + III2 + IV – respirasomes.

6.4.2.3. Evaluation of the protein amount of the residual complex IV subunits upon
COX8A deficiency in HEK293T cells

Steady-state protein levels of selected RC subunits were evaluated with SDS -PAGE with
subsequent immunoblotting.
In the HEK293T cell lines with a smaller (clone #13) and larger (clone #14) deletions in
COX8A MTS, the COX protein levels were considerably reduced (Fig ure 31). Similar to the
fibroblasts, the strongest decrease was observed for the subunits COX1 and COX5A, while the
subunit COX4 was the least affected. Notably, the decrease in the COX subunits amount was



102

more pronounced in the clone #14 with the larger deletion in the COX8A MTS. However, no
upregulation in the protein levels of the subunits of other OXPHOS complexes was observed.


Figure 31 . Steady -state levels of selected subunits of respiratory chain complexes in
COX8A-deficient cells  HEK293T cells . SDS -PAGE with subsequent immunostaining,
mitochondrial preparation of the WT and COX8A-deficient HEK293T cells – clone #14 (C14)
and clone #13 (C13), 50 µg protein/lane.

6.4.2.4. Analysis of the expression of protein subunits of complex IV and other respiratory
chain complexes in COX8A-deficient HEK293T cells

To identify whether the changes in the RC protein levels can be explained by transcriptional
regulation, the effects of COX8A deficiency on the expression of the genes encoding OXPHOS
proteins were investigated with RNA sequencing. The analysis of transcriptome of the COX8A-
deficient clone #14 HEK293T cells identified multiple genes encoding subunits of RC
complexes that were differentially expressed (Figure 32). Specifically, the expression of all but
one mtDNA genes encoding RC proteins w as increased: subunits ND1, ND2, ND3, ND4,
ND4L of complex I (log2(FC): 0.45, 0.47, 0.63, 0.42, 0.61; p-value: 2*10-3, 1*10-3, 4*10-6, 0.01,
4*10-5, correspondingly), cytochrome b of complex III (log 2(FC): 1.4; p -value: 1*10 -21,
correspondingly), subunits A and A6L of complex V (log2(FC): 0.8, 0.65; p-value: 3*10-8, 2*10-
6, correspondingly), and COX2 and COX3 of complex IV (log2(FC): 0.34, 0.61; p-value: 0.03,
9*10-5, correspondingly). The expression of the nuclear -encoded subunits A, B1 and γ of
complex V was upregulated as well (log 2(FC): 0.72, 0.66, 0.79; p-value: 4*10-4, 7*10-3, 2*10-
4, correspondingly). However, the transcript amounts of the nuclear -encoded COX subunits



103

COX4I1, COX6A1, COX6C, COX7A2, COX7A2L, COX7C (log 2(FC): -0.48, -0.52, -0.41, -
0.6, -0.6, -0.4; p -value: 6*10 -3, 6*10 -3, 0.03, 6*10 -4, 4*10 -3, 0.03, correspondingly), and
complex I subunits NDUFA1, NDUFS8, NDUFB10 were decreased (log 2(FC): -0.67, -0.7, -
0.51; p-value: 2*10-3, 1*10-3, 0.04, correspondingly).

Figure 32. Differentially ex pressed genes encoding OXPHOS complexes in the COX8A -
deficient fibroblasts. Volcano plot of gene expression in the COX8A patient fibroblasts
compared to the control fibroblasts. Each identified gene sequence is represented by one point
on the graph. The identified differentially expressed genes encoding subunits of RC complexes
are shown in boxes.  The horizontal axis is log 2(fold change) between the sample means, the
vertical axis is -log10(P-value). Grey points are not statistically significant (p > 0.05), red points
show the upregulated genes (p < 0.05), blue points show the downregulated genes (p < 0.05).

6.4.3. Estimation of the impact of the COX8A deficiency on mitoBK channels
in human fibroblasts

The COX8A -deficient cells provided an intriguing model of the isolated COX deficiency,
where the residual COX was still present and was largely restricted to respirasomes, while other



104

ETC complexes remained largely structurally intact. Thus, the interaction of mitoBK channels
with the defect COX in this sys tem was the next question addressed in this work. The study
model was limited only to fibroblasts with COX8A deficiency, since HEK293T cells are
recognized for not expressing any functional K+ channels in the IMM 77.

6.4.3.1. Assessment of the protein complexes of mitoBK with complex IV

To identify an impact of the COX8A deficiency on the protein complexes formed by mitoBK-
α subunit and the ETC  in the mitochondria of fibroblasts , multiprotein complexes in
mitochondria of COX8A-deficient patient’s fibroblasts and matched control cells were resolved
and identified using BN-PAGE followed by Western blotting.
In the mitochondrial preparation of both cell types , the mitoBK-α signal was detected only in
the same type of protein complexes, likely formed by a tetramer of mitoBK-α subunits and the
associated mitoBK-β subunits. Notably, the amount of the complexes formed by the mitoBK-α
was lower in the COX8A -deficient cells. The presence of mito BK-α subunit in a band co -
migrating with the respirasome, as observed in the astrocytoma WT cells, could not be detected.
However, it should be noted that the gene expression and protein amo unt of mito BK-α is
noticeably lower in fibroblasts than in astrocytoma cells . Thus, it cannot be ruled out that a
subpopulation of mitoBK channels exists in a respirasome -associated state, but is not
discernible by this method due to their low abundance.





105


Figure 33. The amount of protein complexes formed by the mitoBK-α subunit is decreased
in COX8A -deficient cells. BN-PAGE with subsequent immunostaining, digitonin 1%.
Mitochondrial preparation of control (C) and COX8A patient (P) fibroblasts, 100 µg
protein/lane. S.e. and l.e. – short exposure and long exposure. On the right, COX -containing
protein complexes: IV – COX monomer, IV 2 – COX dimer, III 2 + IV – supercomplex
containing COX and dimer of complex III, I + III2 + IV – respirasomes.

6.4.3.2. Evaluation of mitoBK protein amount in fibroblasts with COX8A deficiency

To verify the  decrease in the protein amount of the mito BK-α subunit observed with BN -
PAGE/Western blotting , the  comparative analysis of the total protein levels of mito BK-α
subunit in mitochondria isolated from the control and COX8A -deficient fibroblasts was
performed by SDS-PAGE/Western blotting.


Figure 34. The amount of mitoBK -α channel is downregulated in the mitochondria of
COX8A-deficient fibroblasts.  SDS-PAGE with subsequent immunostaining of total cell
homogenate (H) and mitochondrial preparations (M) of control (C) and COX8A patient (P)
fibroblasts, 100 µg protein/lane.



106


The results of the study confirmed the decrease in the total amount of the total full-sized BK-α
protein in cell lysate, and in particular mitoBK -α protein in the mitochondria of COX8A -
deficient fibroblasts (Figure 34).

6.4.3.3. An alysis of the expression of mitoBK subunits in fibroblasts with COX8A
deficiency

As a conclusion of the analyses on the protein level, the decrease in the mitoBK-α subunit was
observed in both COX-deficient models: with the large-scale impairment of ETC caused by the
mtDNA depletion, and in a model with isolated COX deficiency due to the mutation in COX8A
subunit. In addition, it was shown that the amount of mito BK-α is downregulated on the level
of gene expression in the mtDNA -depleted cells. These obser vations raise the  question of
whether the observed decrease in the mito BK-α amount is transcriptionally regulated in the
COX8A-deficient fibroblasts as well. To address it, differential gene expression analysis was
performed using the RNA sequencing data.
RNA sequencing detected the expression of three genes encoding BK channel subunits in both
control and patient fibroblasts: KCNMA1, KCNMB3, and KCNMB4. However, no statistically
significant change in the expression of these genes was observed (Figure 35).
To confirm a lack of the change in the expression of KCNMA1 observed with RNA sequencing,
real-time reverse -transcription polymerase chain reaction (qRT -PCR) was performed. No
statistically significant decrease in the expression of KCNMA1 was detected in a qRT-PCR
assay with GAPDH as a reference gene (Figure 36).



107



Figure 35. No statistically significant change in the expression of genes encoding mitoBK
subunits is observed in COX8A-deficient fibroblasts. The volcano plot graphically identifies
differential expression of genes: the value of –log10(p-value) is plotted on the y-axis against the
log2(fold change) on the x -axis. The change in value for each assigned gene sequence is
depicted by one point. The upregulated transcripts are labeled in red, downregulated – in blue,
and the transcripts without a statistically significant change in expression (p > 0.05) – in grey.




108


Figure 36. No significant change in KCNMA1 expression in fibroblasts with a mutation in
COX8A is detected by qRT-PCR. Expression level of KCNMA1 gene is shown in relation to
GAPDH (n = 3).

6.4.3.4. Transcriptome profiling of the COX8A-deficient fibroblasts with high-throughput
RNA sequencing

To analyze whether a deficiency in COX8A in the patient fibroblasts led to a change in the gene
expression of other OXPHOS proteins, the differential gene analysis was performed with a
focus on this group of genes.
The analysis of the transcriptome of fibroblasts with COX8A deficiency identified a few
differentially expressed RC protein -encoding genes (Figure 37). Namely, a small decrease in
the transcription levels of mtDNA-encoded COX3 subunit and ATP synthase subunits A6L and
A was observed (log 2(FC): -0.91, -0.87; p -value: 0.03, 0.01, correspondingly), while the
expression of nuclear -encoded sub units COX7A1 and COX7B of COX, and the amount of
transcripts encoding cytochrome b -c1 complex subunit 6, and subunits C3 and DAPIT of
complex V was slightly increased (log2(FC): 1.16, 0.86, 0.73, 0.68, 0.74; p-value: 6*10-5, 0.02,
0.04, 0.03, 0.04, correspondingly).



109


Figure 37. Differentially expressed genes encoding OXPHOS complexes in the COX8A -
deficient fibroblasts . Volcano plot of gene expression in the COX8A patient fibroblasts
compared to the control fibroblasts. Each identified gene sequence is represented by one point
on the graph. The identified differentially expressed genes encoding subunits of RC complexes
are shown in boxes.  The horizontal axis is log 2(fold change) between the sample means, the
vertical axis is -log10(P-value). Grey points are not statistically significant (p > 0.05), red points
show the upregulated genes (p < 0.05), blue points show the downregulated genes (p < 0.05).

According to the modular COX biogenesis paradigm, the subunit COX8A is joining the
assembly process in the CO X2-containing second module. The identified decrease in the
amount of the COX monomers in the COX8A -deficient cells can indicate that thi s protein
complex is not stable and that orphaned subunits of the first or second COX assembly module
may exist and pot entially accumulate in mitochondria. To determine whether a COX8A
deficiency triggers mitochondrial retrograde signaling, expression of the key transcriptional
regulators and their downstream targets of the mitochondrial unfolded protein response
(mtUPR) a nd the integrated stress response (ISR) pathways were evaluated with RNA
sequencing.



110

In the transcriptome profile of fibrob lasts with the COX8A deficiency, no upregulation of the
genes encoding the mitochondrial proteases ClpP, ClpX, Lonp1, paraplegin , and YME1L
(CLPP, CLPX, LONP1, SPG7  and YME1L, correspondingly) has been observed (Fig ure 38).
The expression of the genes HSPA9 and HSPD1 encoding mitochondrial chaperones was
unaltered in the COX8A patient fibroblasts  as well.  In th e ISR, the phosphorylated  eIF2α
induces the expression of the central transcriptional regulators of ISR - ATF4 and its canonical
target CHOP. However, no increase in the expression of ATF4 and CHOP was observed in the
COX8A-deficient fibroblasts (Figure 38).


Figure 38. mtUPR and ISR are not activated in the COX8A-deficient fibroblasts. Volcano
plot of gene expression in the COX8A patient fibroblasts compared to the control fibroblasts.
Each identified gene sequence is represented by one point on the graph. The selected gene
names are shown in boxes.  The horizontal axis is log2(fold change) between the sample means,
the vertical axis is -log10(P-value). Grey points are not statistically significant (p > 0.05), red
points show the upregulated genes (p < 0.05), blue points show the  downregulated genes (p <
0.05).



111

6.5. Patch -clamp study of the molecular mechanisms of carbon monoxide
modulation of mitoBK channel activity

6.5.1. The effects of structurally different CO-releasing molecules on mitoBK
channel activity

Mitochondria is olated from astrocytoma cells with established characteristics of mitoBK
channel activity were used in the patch -clamp study of the mitoBK channel as a signaling
effector of carbon monoxide (CO). In the first part of this study, three structurally distinct
CORMs were applied to the mitoBK channels to study the effects of CO donors.
First, the effects of CORM -401 were investigated, as this CO donor had been previously
reported as a mitoBK channel opener in a patch -clamp study on mitochondria of endothelial
cells 137. The single-channel mitoBK channel activity recordings following the application of
10 µM CORM -401 are shown in Figure 39A and Figure 39B at -40 mV and +40 mV,
respectively. As previously stated, the inside -out configuration of the patch requires that the
perfusion solution be administered to the mitochondrial matrix side of the IMM with an exposed
C-terminal part of the channel. Interestingly, perfusion with 10 μM CORM -401 in 1 μM Ca 2+
solution did not exhibit an apparent modulatory effect on the mitoBK channel activity ( Figure
39).
Since the findings of this study diverged from those previously reported, a structurally different
class of CORMs was selected to validate the results. The mitoBK channel -containing patches
were perfused with a ruthenium carbonyl CORM-2 (Figure 40). During the first minute of patch
perfusion with 30 μM CORM-2 in 1 μM Ca2+ solution, two different types of initial responses
of the mitoBK channels were observed ( Figure 40 , insert). One set of responses (group 1)
indicated transient activation of channels upon CORM-2 application (n = 4): the channel P(o) at
-40 mV increased from 0% to 12% ± 7%, and from 7% ± 3% to 46% ± 17%, at +40 mV.
However, continuous perfusion showed a biphasic characteristic of the CORM -2 action, in
which the initial activation was  followed by the channel inhibition in all recordings taken ~5
min after the 30 μM CORM -2 application. The other set of responses (group 2) was
characterized by no significant change in channel activity in the presence of CORM -2 during
the 1 st and 5 th minutes of continuous perfusion (n = 6). At +40 mV, the relative P (o) of the
channels was 2% ± 2% under high -calcium conditions, and it changed to 1% ± 1% that of the
control P(o), after perfusion with CORM-2.



112


Figure 39. Lack of apparent effect of CORM-401 on the mitoBK channels. Representative
traces of mitoBK single-channel recordings at -40 mV (A) and +40 mV (B) after perfusion with
symmetric 150/150 mM KCl solutions: the high calcium control solution (100 μM Ca 2+), the
low calcium solution (1 μM Ca2+), and the low-calcium solution containing 10 μM CORM-401.
Changes in the mean P (o) values upon perfusion with the low calcium solution  and that with
CORM-401 at -40 mV (A) and +40 mV (B) were evaluated for individual experiments.




113





114

Figure 40. Complex CORM -2 modulation of the mitoBK channels. Representative traces
of the mitoBK single-channel recordings at -40 mV (A) and +40 mV (B) afte r perfusion with
symmetric 150/150 mM KCl solutions: the high -calcium control solution (100 μM Ca 2+), the
low-calcium solution (1 μM Ca 2+), and the low-calcium solution containing 30 μM CORM -2.
Changes in the mean P (o) values upon perfusion with the low -calcium solution with CORM -2
at -40 mV (A) and +40 mV (B) were evaluated for individual experiments. The biphasic effect
of the application of CORM -2 can be observed in the course of the experiment, as illustrated
by the changes in mean P (o) values at the st art (1 st minute) and the end (5 th minute) of the
perfusion.

Due to the discrepancies between the observed effects of CORM -401 and CORM -2, the
modulation of the mitoBK channels was assessed with yet another CO -donor of different
chemistry, sodium boranocarbonate CORM-A1 (Figure 41). In this case, perfusion with 30 μM
CORM-A1 in the 1 μM Ca 2+ solution resulted in a slight decrease in the channel P (o) from 8%
to 2%, compared to the P(o) of the control, at +40 mV (n = 4) (Figure 41A). The activity of the
channel recorded at -40 mV with the 1 μM Ca 2+ solution was unchanged after p erfusion with
CORM-A1 (Figure 41B).


115


Figure 41. Lack of stimulation of the mitoBK channels by CORM-A1. Representative traces
of mitoBK single-channel recordings at -40 mV (A) and +40 m V (B) after perfusion with
symmetric 150/150 mM KCl solutions: the high -calcium control solution (100 μM Ca 2+), the
low-calcium solution (1 μM Ca 2+), the low -calcium solution containing 30 μM CORM -A1.
Changes in the mean P(o) values upon perfusion with the low-calcium solution with CORM-A1
at -40 mV (A) and +40 mV (B) were evaluated for the individual experiments.

6.5.2. Evaluation of the CO gas modulation of mitoBK activity

To ultimately clarify the contribution of CO to the effects observed after CORMs application,
IMM patches with mitoBK channels were perfused with solutions saturated with the CO gas.
The concentration of the CO gas in the CO-bubbled solutions was estimated to be ~1 mM. The
presence of the CO in the CO-bubbled solution was confirmed by the change in the myoglobin
absorption spectrum in the CO -containing solution as described in chapter 5.13. Specifically,



116

two peaks were observed in the proximity of the wavelengths characteristic for
carboxymyoglobin - λ1 = 540 nm and λ2 = 577 nm (Figure 42).

Figure 42. The change in the absorption spectrum of myoglobin in a solution perfused
with CO indicates the formation of carboxymyoglobin.  DeoxyMb (in black) – myoglobin
in a control solution; Mb-CO (in pink) – myoglobin in a CO-saturated solution.

The first set of experiments showed that the low activity of the channel in 1 µM Ca2+ solution
was not increased after perfusion with the 1 μM Ca 2+ solution saturated with CO ( Figure 43).
Upon the subsequent change to a CO-saturated solution with 100 μM Ca2+, the channel P(o) was
increased to the levels, which were not significantly differ ent from those observed for the
control conditions with 100 μM Ca 2+, which were 99% ± 2% and 92% ± 4% at +40 mV and -
40 mV, respectively (n = 4). These observations suggest a lack of CO effect when carbon
monoxide was applied alone in all tested conditions.





117


Figure 43. Absence of modulation of the mitoBK channels by CO gas alone. Representative
traces of mitoBK single-channel recordings at -40 mV (A) and +40 mV (B) after perfusion with
the symmetric 150/150 mM KCl solutions: the high -calcium control solution (100 μM Ca 2+),
the low-calcium solution (1 μM Ca2+), the low-calcium solution bubbled with CO, and the high-
calcium solution bubbled with CO. Changes in the mean P (o) values upon perfusion with the
low-calcium solution and the CO -containing solutions at -40 mV (A) and +40 mV (B) were
evaluated for individual experiments.






118

6.5.3. Analysis of complex regulation of mitoBK channels by heme and CO
gas

According to the existing data, heme is a primary CO -sensing element in proteins targeted by
carbon mono xide 169, including BK channels. Although mitoBK channels have the heme -
binding structural domain (HBD), heme and its oxidized form hemin appear to be onl y
transiently bound to the channel. It is currently unknown what fraction of the mitoBK channel
population comprises hemoproteins under physiological conditions. Thus, channel modulation
by heme was modeled by the exogenous application of heme to the mitoBK channels in patches
(Figure 44 ). Since heme was expected to inhibit the channel activity, the effects of heme
application were studied in high-calcium solutions. Perfusion with 300 nM heme resulted in a
decrease in the open channel probability to 52% ± 9 %, compared to that of the control, at -40
mV (Figure 44A) and to 39% ± 6%, compared to that of the control, at +40 mV ( Figure 44B)
(n = 4).
To study whether the addition of CO could modify the inhibitory effect of heme on the mitoBK
channels, the channels were perfused with a high-calcium solution containing both heme and
carbon monoxide (Figure 44).  The addition of CO resulted in the significant (p < 0.05) release
of the channel inhibition by 300 nM heme  - as indicated by the increase in the open channel
probability from 40 % ± 13% to 77% ± 8% compared to that of the control at -40 mV, and from
25 % ± 11% to 83% ± 23% at +40 mV (n = 3).


119



Figure 44. Reactivation of heme -inhibited mitoBK channels by CO gas.  Representative
traces of mitoBK single-channel recordings at -40 mV (A) and +40 mV (B) after perfusion with
the symmetric 150/150 mM KCl solutions: the high -calcium control solution (100 μM Ca 2+),
the high-calcium solution containing 300 nM heme, the CO -containing high-calcium solution
containing 300 nM heme. Changes in the mean P (o) values upon perfusion with the hem e, CO
and heme, at -40 mV (A) and +40 mV (B) were evaluated for individual experiments.

It is well -established that CO binds only to the ferrous (Fe 2+) heme. In order to confirm the
heme-mediated molecular mechanism of CO reactivation of the channels, mitoBK -containing
patches were inhibited with the ferric (Fe3+) form of heme – hemin. The subsequent perfusion
of the channels with CO did not release the channel inhibition by hemin (Figure 45).




120



Figure 45 . Lack of reactivation of hemin -inhibited mitoBK channels by CO gas.
Representative traces of mitoBK single-channel recordings at -40 mV (A) and +40 mV (B) after
perfusion with the symmetric 150/150 mM KCl solutions: the high -calcium control solution
(100 μM Ca2+), the high-calcium solution containing 100 μM CO, the low-calcium solution (1
μM Ca 2+), high-calcium solution containing 1 μM hemin , the CO -containing high -calcium
solution containing 1 μM hemin . Changes in the mean P (o) values upon perfusion with the
hemin, and CO with hemin , at -40 mV (A) and +40 mV (B) were evaluated for individual
experiments.



121

7. DISCUSSION

The results presented in this work can be divided into four distinctive parts.
The first part investigates the effects caused by the depletion of mtDNA in astrocytoma cells
on mitochondrial signaling. The retrograde signaling networks initi ated by this mitochondrial
dysfunction are evaluated. The particular focus of the study is dedicated to the transcriptional
regulation of mitoBK channels.
The second part addresses the molecular functional effects of the deficiency of the smallest
nuclear-encoded subunit of COX – COX8A – on the electron transport chain and cytochrome
c oxidase in particular. The results are evaluated in the patient cells with a characterized
mutation in COX8A and the HEK293T cells with functional COX8A deficiency introduced by
CRISPR/Cas9 gene-editing technique.
The third part of this study is dedicated to the issue of  the structural interaction of mitoBK
channels with COX. In particular, the complexes between the mitoBK-α subunit and the COX
are analyzed in the cell models with COX deficiency qualitatively and quantitatively.
The fourth part of this work is performed to elucidate the role of mitoBK channels in carbon
monoxide (CO) signaling. The effects of various CO donors on the channel activity are
compared to the modulation of t he channels by a pure CO gas. The role of hemin binding in
CO regulation of mitoBK channels is addressed in particular.

7.1. Signaling pathways activated upon mtDNA depletion in astrocytom a
cells

Over the years, a large number of studies have explored the implication of mtDNA mutations
in aging, neurodegenerative diseases 170, endocrine dysfunction 171, and cancer 172. The
accumulated oxidative damage to mtDNA has been suggested as one of the drivers of cellular
aging 173.  Yet, high heterogeneity of mitochondrial diseases and various genetic background s
confound the application of the cells derived from patients as a study model to investigate the
molecular role of mtDNA. Cell lines devoid of mtDNA with available maternal controls can be
employed instead in different studies of the pathogenesis of mitochondri al diseases or


122

investigation of the fundamental mitochondrial physiology. Hence, several different approaches
to obtain cell lines devoid of mtDNA or mtDNA-encoded proteins have been developed.
Treatment with ethidium bromide (EtBr) was one of the earliest  characterized techniques for
producing mtDNA-void cells. While it is still commonly used for this purpose, induction of
mtDNA depletion with EtBr is either associated with a mutagenic effect on the nuclear DNA
or has a very long duration that hampers its practicality. A different approach for the depletion
of mtDNA involves overexpression of the products of fusion of EcoRI or ExoIII restriction
endonucleases with the mitochondrial targeting sequence, such as the one of COX8A 174,175.
However, their overexpression is associated with concerns over occasional mistargeting to the
nucleus and the ensued unintended endonuclease activity on the nuclear -encoded genes. In
addition, targeting of these proteins to mitochondria can negatively affe ct the capacity of
mitochondrial protein import systems for trafficking nuclear-encoded proteins, thus disrupting
mitochondrial proteostasis. While another strategy is not inducing a deficiency in mtDNA sensu
stricto, a commonly used approach in the proteomic studies investigating the effects of the lack
of mitochondrial -encoded proteins relies on the inhibition of the mitochondrial protein
synthesis with certain compounds. In particular, the bacteriostatic action of a number of
antibiotics, e.g., chloramph enicol or tetracycline, is exerted by their binding to the bacterial
ribosomes and blocking the binding of aminoacyl tRNA. Due to the structural similarity of
mitochondrial ribosomes to the prokaryotic ones, these drugs were also shown to downregulate
protein synthesis in mitochondria.
With the  development of high -throughput sequencing technologies, a growing nu mber of
studies suggest a major role of functional impairments of the mitochondrial DNA polymerase
γ (POLG) in mutagenesis of mtDNA. In particular, the mice mutator model that lack s the
proofreading exonuclease activity of POLG, thus containing a higher nu mber of mutations in
their mtDNA, has a phenotyp e characterized by premature ag ing. Mutations in POLG are
associated with disorders such as myoclonic epilepsy, ataxia neuropathy spectrum, autosomal
recessive and autosomal dominant progressive external opht halmoplegia, childhood
myocerebrohepatopathy spectrum, and Alpers –Huttenlocher syndrome 176. In this work,
treatment of the cells with a non -hydrolyzable nucleoside analog 2′,3′-dideoxycytidine (ddC)
as an inhibitor of POLG was selected to achieve depletion of mtDNA.
DdC has been extensively researched as a reverse transcriptase inhibitor, which was initially
approved as antiretroviral treatment for HIV -infected patients. The therapeutic use of this
compound was later suspended due to the reports of significant adverse effects including


123

peripheral neuropathy and myopathy, which were associated with the mitochondrial toxicity of
ddC 177.  DdC is imported into the cells by nucleoside transporters hCNT1 and hENT2 and
sequentially phospho rylated in the cytoplasm by nucleotide salvage route enzymes to form
2′,3′-dideoxycytidine triphosphate (ddCTP) 178. Following the import of ddCTP into the
mitochondria, it inhibits the mitochondrial DNA polymerase-γ (POLG). Importantly, the POLG
is inhibited by ddCTP with a much higher affinity than the nuclear DNA polymerases α, β, and
, with Ki of a 100 – 1000-fold higher value 153.
Induction of the mtDNA depletion can be fatal to the cells due to the lack of ATP synthesis by
OXPHOS, yet the lack of precursors for pyrimidine salvage synthesis can further aggravate the
damage to cell viability. The activi ty of an enzyme in the de novo pyrimidine biosynthesis
pathway -  dihydroorotate dehydrogenase - is inhibited due to the loss of ETC, with which it is
linked through coenzyme Q. To compensate for it, the cell culture medium was supplemented
with uridine, what is a commonly used approach to increase the viability of cultivated cells with
various ETC deficiencies. Thus, while the growth of ddC-treated astrocytoma cells was stunted,
due to their proclivity to g lycolysis (as described above) they withstood this intervention in
their metabolism.
In this study, the achievement of the depletion in mtDNA by the ddC treatment of astrocytoma
cells was confirmed on different levels. Functionally, the abolished respiration of ddC -treated
cells indicated a major loss of OXPHOS. On the protein level, a loss of the ETC complexes -
in particular, complex IV, caused by  the unavailability of the essential mtDNA -encoded
subunits was confirmed. On the level of gene expression, the abundance of transcripts of all
protein-coding mtDNA genes was significantly decreased. While this study did not address
mitophagy in ddC-treated cells, the mitochondrial network was observed in mtDNA -depleted
astrocytoma cells and appeared more disrupted than in the WT cells.
To investigate mtDNA depletion-initiated transcriptional regulation, the transcriptome of these
cells was analyzed with a focus on mitochondrial retrograde signaling pathways. In particular,
it was found that the expression of the genes under transcriptional control of integrated stress
response (ISR) was upregulated. At the same time, no indications of activation of the
mitochondrial unfolded protein response (mtUPR) were observed, what indicated that no
proteotoxic stress signaling was elicited in a response to a disruption in proteostasis.
This observation is in agreement with the previous findings reporting initiation of ISR by
deletions in mtDNA in different tissues. Thus, an increase in the transcription of the ISR master
transcriptional regulator ATF4 was observed in  the skeletal muscle of the mice harboring a


124

mutation in mtDNA helicase 179. In the mice model of mtDNA -associated mitochondrial
myopathy, induction of ISR was shown in myoblasts with particular involvement of fibroblast
growth factor 21 (Fgf21) 180. In another study of mitochondrial myopathy, Fgf21-mediated ISR
was initiated only in response to mtDNA deletions or dysfunction in mitochondrial translation,
and not in the myoblasts of patients with mitochondrial myopathy caused by the deficiencies in
the nuclear -encoded structural ETC subunits or assembly factors 181. However, Fgf -21-
mediated signaling is likely specific to a tissue type since expression of Fgf21 was virtually
undetectable in the RNA sequencing tra nscriptome profile of astrocytoma cells. Various
triggers of ISR activation were described in a study where the ISR was induced by inhibiting
ETC or ATP synthase activity in myoblasts and myotubes 182. Following E TC inhibition, a
disruption in aspartate synthesis activated kinase GCN2, whereas inhibition of the ATP
synthase resulted in hyperpolarization of the IMM, which was implicated in the ISR signal
relay.
Few studies have attempted to characterize the impact of mitochondrial retrograde signaling on
the ion channels in the cell membrane and the IMM. Thus, another objective of this work was
to investigate how the mitoBK channel is affected by the mitochondrial retrograde signaling in
mtDNA-depleted astrocytoma c ells. Analysis of expression of mitoBK -encoding genes has
revealed that the amount of the KCNMA1 transcripts was significantly downregulated in this
cell model. The decrease in the transcript amount was also reflected in the decrease of the
mitoBK-α protein complexes. To date, there has been no research demonstrating the decrease
in the mito BK-α on the transcriptional or protein level upon mitochondrial deficiencies.
However, d ifferent studies demonstrated changes in the amount of BK channels und er
transcriptional regulations under various pathological conditions.
The disruption of transcription of genes involved in calcium homeostasis was identified in a
transcriptome investigation of spinocerebellar ataxia type 7 (SCA7) mice suffering from
cerebellar and retinal degeneration. In particular, downregulation of Kcnma1 expression was
observed, which was manifested in altered spiking patterns of Purkinje neurons. Furthermore,
mitochondrial dysfunction was a major factor in SCA7 pathogenesis, as both m itochondrial
morphology and oxidative metabolism were disrupted in the SCA7 mice model 166.
A decrease in the NAD+ levels is a hallmark of mitochondrial disorders, and treatment with the
precursors or stimulators of de novo NAD+ synthesis has been a subject of extensive research
towards therapy for mitochondrial dysfunctions 183,184. Sirt-1 is a NAD+ dependent deacetylase,
and the low availability of its cofactor NAD + impairs the regulation of PGC -1α by Sirt1.


125

Kcnma1 contains PPAR response elements in the promotor region and is  positively regulated
by PGC-1α. Interestingly, Sirt1 overexpression, as well as NAD + supplementation, proved to
have a neuroprotective effect in SCA7 mice  166,167. Thus, the NAD +-dependent deficiency in
the Kcnma1 could contribute to the mitochondrial pathology in SCA7. In the mtDNA-depleted
astrocytoma cells, however, no change in the gene expression of PGC -1α and its downstream
effectors was identified, suggesting that another mechan ism is involved in the  regulation of
KCNMA1 expression. It is likely that under the experimental conditions of this study, the NAD+
pool was restored by the reduction of pyruvate to lactate in a reaction catalyzed by lactate
dehydrogenase, the former being available due to its presence in the composition of DMEM in
the cell culture medium.
One of the branches of the homeostatic responses in the mitochondrial retrograde signaling
involves a cross-talk of the mitochondrial ISR with the nuclear factor erythroid-2–related factor
2 (Nrf2) signaling pathway, which is a master regulator of the oxidative stress response.
Activation of Nrf2 leads to an upregulation of genes encoding protein s that confer antioxidant
protection, including heme oxygenase -1 (HO -1), superoxide dismutase, thioredoxin,
thioredoxin reductase 1, glutathione -disulfide reductase, glutathione translocase, and
glutathione peroxidase. The results of this study suggest that Nrf2 was activated in the mtDNA-
depleted cells and upregulated the expression of its target network of the antioxidant enzymes.
Expression of KCNMA1 was reported to be positively regulated by Nrf2 in the coronary smooth
muscle cells 185. However, the decrease in KCNMA1 transcripts with a general upregulation of
primary Nrf2 targets in ddC -treated cells suggests that a diffe rent regulatory mechanism is
involved in mtDNA-depleted astrocytoma cells.
Besides regulation by transcription factors, other molecular mechanisms may be implicated in
the control of KCNMA1 expression in the mtDNA-depleted astrocytoma cells, but their stu dy
requires different methodological approaches from those used in this work. Thus, they will be
only briefly outlined below:
 Different availability of the methyl group donor pool due to the alterations in the
mitochondrial metabolic activity can affect the methylation of DNA. As a result,
changes in the mtDNA levels can impact nuclear DNA methylation patterns across the
genome 186. In rat and human colorectal cancer cells, epigenetic control of BK channel
expression, namely by hypermethylation of the KCNMA1 promoter, was described 7.


126

 Histone remodeling by methylation or acetylation can be inv olved in epigenetic
regulation. During mitochondrial stress, certain metabolic enzymes can be translocated
from mitochondria to the nucleus - such as the pyruvate dehydrogenase complex, which
then affects acetyl -CoA availability for histone acetylation 187. A disruption in the
methyl donor group supply can affect chromatin remodeling as well.
 Posttranscriptional RNA silencing by microRNA  was implica ted in the control of
KCNMA1 transcript amount in tumor cells: in particular, by  mir-17-5p in colorectal
cancer and pleural mesothelioma  188,189, mir-31 – in ovarian cancer 190, mir-211 – in
melanoma cells 191.
 Regulation of splicing can be impaired by a decreased availability of ATP following
disruption of its mitochondrial supply 192.
 Genomic instability is linked to mitochondrial depolarization,  which impairs  the
synthesis of iron-sulfur clusters that are required as cofactors for the enzymes involved
maintenance of genome integrity 193.
The amount of the functional BK channels regulated on the transcriptional level can be
important in the pathophysiological context . While the role of mutations of BK channels in
epilepsy is well -recognized, an acquired BK channelopathy caused  by a decrease of the
functional BK channels is emerging as a novel molecular mechanism that aggravates the
disease. Thus, in a pilocarpine model of epilepsy, the amount of BK-α transcripts and proteins
were decreased in the cortex and hippocampus of rats experiencing chronic seizures 194 . A
decrease in vascular BK-β1 expression  is observed  in diabetes and  at high-glucose culture
conditions 195,196.  mRNA amount of BK-α subunits, as well as their protein amount , were
decreased in the rat artery calcification models, and pharmacological activation of the channels
diminished the severity of calcification  197. In a study of the molecular mechanisms of
neuropathic pain, the constriction of the spinal nerve led to a persistent transcriptional
downregulation of the expression of BK channels, and a corresponding decrease in the protein
amount of the BK channels in the dorsal root ganglion neurons of rats 198,199. A release of brain-
derived neurotrophic factor BDNF following nerve injury in rats was implicated in the
transcriptional downregulation of BK-α in the primary sensory neurons, leading to aberrant
cellular excitability and nociception 200.
One of the limitations of this study is that it is performed on a tumor cell line with its metabolic
and signaling profile. Since not many cell types can sustain such a d rastic change in their


127

metabolic pathways, a tumor cell line with typical metabolic lability and adaption to survival
in hypoxic environments has been chosen. Distinct cancer types are characterized by different
metabolic profiles, such as aerobic glycolys is phenotype, a phenotype with prevailing
OXPHOS, or a combination of both, and they can be further altered throughout carcinogenesis
and metastasis. However, metabolic lability of the cancer cells is pleiotropic, arising not only
due to tumorigenic gene m utations but also from metabolic reprogramming to accommodate
the unique metabolic requirements during tumor development. T he model ed system is
physiologically relevant since a change in the mtDNA copy number is implicated in malignant
transformation and tumorigenesis. Thus, a decrease in the mtDNA copy number in colorectal
and prostate cancer cells was associated with their metabolic reprogramming and increased cell
invasiveness. MtDNA depletion that initiates metabolic reprogramming has been attributed to
the start of epithelial -mesenchymal transition. The ensued activation of retrograde signaling
pathways in epithelial cells led, in particular, to Ca2+/calcineurin-dependent re-profiling with a
decrease in epithelial markers and overexpression of mesenchymal markers 201.
In carcinogenesis, changes in the KCNMA1 transcript and protein abundance are associated
with tumor growth through different mechanisms. Downregulation of KCNMA1 by siRNA gene
silencing was observed in colorectal cancer, pleural mesothelioma, ovarian cancer, and
melanoma 188–191. However, in prostate cancer, a mplification of chromosomal region 10q22
containing KCNMA1 drew BK-α overexpression and increased current density, promoting the
proliferation of PC -3 cells  202. Similarly, amplification of KCNMA1 and increase in protein
expression were related to a poor prognosis and a high tumor stage and grade in breast cancer
203. Expression of KCNMA1 was shown as an early marker of cervical cancer 204.
In conclusion, treatment of astrocytoma cells with a POLG inhibitor ddC led to the depletion
of mtDNA. This disruption in mitochondrial function initiated ISR signaling, and an associated
branch of the transcriptional antioxidant response by Nrf2 was activated. The downregulation
in the KCNMA1 expression was identified as well. The  observed link between the retrograde
signaling in mtDNA-depleted astrocytoma cells and a change in KCNMA1 expression leading
to a decreased amount of mitoBK-α can be particularly interesting in the context of astrocytoma
tumorigenesis. Further research can address open questions, such as whether the
downregulation of the mito BK-α is ob served in the normal mtDNA-depleted cells, what
molecular mechanisms are implicated in the regulation of this phenomenon , and how it is
functionally relevant in the normal and pathophysiology.



128

7.2. Molecular and functional effects of the loss of cytochrome c oxidase
subunit 8A

In the second part of the study, the consequences of the COX8A deficiency on the assembly of
COX as a discrete respiratory chain constituent and a part of the ETC protein supercomplexes
were evaluated.
The effects observed in the human dermal fibroblasts with an identified COX8A deficiency
leading to a  virtual loss of COX8A were evaluated alongside observations in the cellular
systems of HEK293T cells with the CRISPR/Cas9-induced mutations in COX8A. A deficiency
in COX8A was modeled with CRISPR/Cas9-mediated gene editing in HEK293T cells. COX8A
exon 1 e ncoding a 25 amino acids -containing mitochondrial targeting sequence was targeted
by the CRISPR/Cas9 system. Thus, two HEK293T cell lines containing deletions in the
COX8A targeting sequence were generated. The protein amounts of selected COX subunits
were compared with SDS -PAGE and BN-PAGE with subsequent Western blotting, followed
by the measurement of enzymatic activities of COX. To identify whether the deficiency in
COX8A affects the expression of OXPHOS complex subunits, or initiates mitochondrial
retrograde signaling pathways, the transcriptome profiles were analyzed in the COX8A
deficient cells.
To protect the mitochondria from exposure to the highly reactive intermediates, assembly of a
COX holoenzyme proceeds in a strictly controlled manner involvi ng numerous nuclear -
encoded assembly factors  29. The current modular mo del of COX assembly stipulates that
COX8A is incorporated at the intermediate stage of COX assembly in the COX2 -containing
module 31.  Interestingly, recent data indicate that  the biogenesis of COX as a component of
respirasome occurs in a divergent pathway proceeding through non -canonical subas sembly
complexes 205.
In accordance with the previously reported data  152, the mutation in COX8A in the patient
fibroblasts led to the nonsense-mediated mRNA decay resulting in a sharp decrease in COX8A
transcript abundance. The functional evaluation has shown that the COX enzymatic activity
levels in the patie nt fibroblasts were about 20% of the levels in the control cells.
Correspondingly, the levels of COX activity in the HEK293 cell lines containing mutations in
COX8A MTS were approaching 30% of the levels in the WT cells. These results suggest that
the loss of COX8A is detrimental to the enzymatic activity of COX.


129

Analysis of protein complexes formed by COX has shown a significant decrease in the total
amount of COX in the COX8A -deficient fibroblasts and HEK293T cells, which was
corresponding to the observed decrease in the COX enzymatic activity. Notably, the BN-PAGE
followed by immunodetection has shown a sharp decrease of the monomeric form of COX in
the COX8A-deficient cells, while the residual COX was largely contained in the respirasomes.
The downregulation of observable monomeric form of COX suggests that COX8A is involved
in the stabilization of COX monomers. Interestingly, the residual COX as a constituent of
respirasomes was not affected, suggesting that being contained within a SC could be shield a
deficient COX protein complex from degradation. Considering the dramatic difference between
the abundance of monomeric and respirasome -bound COX forms, and the recently reported
data on alternative assembly pathways for COX incorporated into the respiras omes 205, this
observation could indicate that COX8A is not strictly required for the biogenesis of COX as a
part of respirasomes.
Stabilization of COX in the ETC supercomplexes and respirasomes has been reported for the
cells harboring mutati ons in the nuclear -encoded COX assembly factors, such as COA6 and
SURF1, while the stability and abundance of the monomeric form of COX were significantly
affected in these cells 206,207.  In a similar manner, the stability of COX monomers was decreased
in cells harboring a missense mutation of the nuclear-encoded structural subunit COX5A, while
the levels of COX within the respirasomes were more robust  208. Taken together, these
observations support the hypothesis that the protein environment of respirasome provides
additional stabilization and protection from protein degradation to the COX with an impaired
assembly and diminished stability, which could constitute one of the main physiological roles
of respirasomes 209.
Interestingly, the ETC complexes I and III were not imperiled in the COX8A -deficient cells,
and on the contrary, their abundance appeared rather elevated. Similarly, a distinguishable
increase in the amounts of ETC complexes I and III have been reported for the fibroblasts
harboring mutations in COA6 and SURF1 206,207. Therefore, this phenomenon may occur as an
adaptive event to provide higher compensatory availability of the protein partner complexes to
stabilize the residual COX in the respirasomes.
The analysis of total protein levels of selected COX subun its by SDS-PAGE/immunoblotting
has confirmed the decrease of the levels  of all evaluated COX subunits – COX1, COX2,
COX5A, COX4 – in the patient fibroblasts. In a similar manner, the amount of proteins of
complex I and complex III was increased, corresponding to the observed increase in the amount


130

of corresponding complexes. To identify if the observed changes in the protein amount levels
occur due to transcriptional upregulation, differential gene expression analysis by RNA
sequencing was conducted.
No discernable pattern of changes in expression of genes encoding the OXPHOS proteins was
observed in the fibroblasts con taining the mutation in COX8A. The e xpression of certain
mitochondrially-encoded genes such as ATP6, ATP8 and COX3 was downregulated. The
statistically significant change in the gene expression affected subunits of COX contained in
the 2 nd (COX7B) and 3 rd (COX3 and COX7A1) assembly module to a different extent. No
systemic upregulation of the genes encoding proteins of complex I and III was de tectable.
Therefore, these observations suggest that the molecular events controlling the abundance of
ETC proteins in the COX8A -deficient fibroblasts occur at the post -transcriptional level.
Interestingly, in the COX8A-deficient HEK293 cells different regulatory events have occurred:
the increase of expression of almost all mitochondrially -encoded proteins was prominent,
combined with the decrease of multiple nuclear-encoded COX subunits contained in each COX
assembly module.
To identify whether the mutation in COX8A led to proteotoxic stress in mitochondria due to the
buildup of the misassembled COX intermediates, the transcriptome was analyzed for the
hallmarks of mtUPR activation. The mechanisms of restoring protein homeostasis by mtUPR
signaling involve an increase in the expression of mitochondrial quality control proteases, such
as YME1L, ClpP, ClpX, and Lonp1  120. Analysis of gene e xpression has shown a lack of
upregulation of mitochondrial proteases in COX8A -deficient fibroblasts and HEK293T cells.
On the other hand, mtUPR signaling pathways increase the availability of the mitochondrial
chaperone pool to aid in folding the mitochondrial peptides 109. Upregulation of mitochondrial
chaperone expression observed in the COX8A -deficient HEK293T cells could, however, be
ascribed to the increased transcription of mitochondrial genes requiring a higher abundance of
mitochondrial chaperones to assist in  the folding of a larger p eptide pool. No increase in the
expression of genes encoding mitochondrial chaperones was observed in COX8A -deficient
fibroblasts.
To investigate whether the COX deficiency induced by the mutations in COX8A triggers the
mitochondrial dysfunction -associated retrograde signaling pathways such as ISR, the
expression of the downstream targets of the master transcriptional regulator of ISR – ATF4 -
was analyzed  210,211. Combined, the ob served absence of activation of ISR and mtUPR in
COX8A-deficient fibroblasts and HEK293T cells indicates that there is likely no underlying


131

deleterious accumulation of orphaned misassembled COX intermediates, suggesting that an
efficient turnover of COX su bassemblies takes places. Considering the occurrence of the
alternative COX assembly pathways as a part of the respirasomes, the COX intermediates
lacking COX8A could alternatively be incorporated into the respirasomes and stabilized in the
multiprotein complexes.
Therefore, the role of COX8A suggested in the observations on the COX8A-deficient cells is
to stabilize the COX monomers. The deficiency in COX8A is detrimental to COX resulting in
the loss of the protein stability, and therefore its abundance an d enzymatic activity. However,
the remaining COX can be salvaged as a part of respirasome complexes, thus avoiding the
potential proteotoxic accumulation of the misassembled intermediates. Additionally, a
compensative increase of availability of the ETC pr otein partners occurs likely to promote
stabilization of the residual COX in COX8A-deficient cells.



132

7.3. Interaction of the mitoBK channel with the cytochrome c oxidase

In the third part of the study, the structural interaction of mitoBK channels with  COX was
evaluated with BN -PAGE using mitochondrial isolations of the WT and mtDNA -depleted
astrocytoma cells, as well as fibroblasts from a patient harboring a genetic deficiency in COX8A
and a matching control.
The results of this study suggest that in a strocytoma mitochondria mitoBK channel forms a
structural complex with the ETC through an interaction of the mito BK-α subunits with COX.
In the mtDNA-depleted cells, the higher-order complexes between mitoBK-α and COX within
respirasomes are not observed, and the abundance of the mitoBK channel complexes
corresponding to a fully assembled tetramer of mito BK-α subunits associated with mito BK-β
subunits is significantly decreased. A similar downregulation of the mitoBK channel complex
amount is observed in the fibroblasts with a COX deficiency due to the mutation in COX8A.
These results are in alignment with the previously reported structural and functional coupling
of mitoBK channels with COX through the mito BK-β4 subunits. In a previous patch -clamp
study of the functional interaction between mitoBK channels and protein complexes of the
respiratory chain of astrocytoma mitochondria, it was shown that mitoBK channel activity was
inhibited after the addition of the respiratory substrates 104. Notably, this effect persisted after
the removal of the respiratory substrates and was abolished by the addition of the specific
inhibitors of the respiratory complexes. Therefore, it was suggested that the activity of the
mitoBK complexes is regulated by  the redox status of the respiratory chain. Structural
interaction between cytochrome c oxidase and the auxiliary mitoBK-β4 subunit has been
suggested to mediate the functional coupling. An interaction of another mito BK-β subunit –
mitoBK-β1 – with COX1 has been shown in a yeast two-hybrid screening in cardiac myocytes
105.  In  the current study, however, the role of mito BK-α in the mitoBK -COX interaction is
confirmed directly with the BN -PAGE technique. In particular,  the results presented here
indicate that mitoBK channels are associated with COX in the respirasomes, thus forming a
multiprotein complex of a higher order. At the same time, the results presented in this work are
in agreement with the identification of mitoBK-β4 as the most commonly expressed auxiliary
mitoBK-β subunit in astrocytoma cells 104.
A proteomic study of the protein interactome of mitoBK channels expressed in the HEK293T
cell line has identified 151 mitochondrial protein partners 82. Among them, 28 OXPHOS
proteins of complexes I, III, IV , and V were found, which would agree with the finding of a


133

mitoBK channel population in a respirasome-associated state. The subunits of COX reported in
the interaction of mitoBK channels – COX1, COX4, COX7A2, COX6A2, COX6C – comprise
the subunits of all COX assembly models. Notably, one of these subunits, COX7A2, has a high
degree of structural similarity in the C -terminal region with COX7A2L, which is directly
involved in the stabilization of respirasomes.
Some of the key physiological functions of the mitoBK channels are mediated through their
influence on the activity of ETC. The respiratory chain complexes and mitoBK channels
execute opposite regulation of the mitochondri al membrane potential: the activity of the RC
generates it, while mitoBK opening dissipates it. Thus, an open question is the localization of
the complexes of mitoBK channels with the respirasomes within the IMM. From a biophysical
perspective, the curvatu re of IMM affects charge density and local pH. The strength of the
electrostatic field is the highest in the membrane segments with the highest  curvature: in a
simulation of the electric field on the surface of IMM, the surface charge density in the curved
segments of cristae was evaluated to be 3.5 times higher compared to the straight segments 212.
Thus, the local biophysical regulation of ETC by a mitoBK channel opening within immediate
proximity would have a different impact in this environment.
Evidence of f unctional networks linking bioenergetics and various mitochon drial processes
through a physical interaction with the respiratory chain complexes has been shown in the
previous studies. Thus, interaction between the protein import system and the respiratory chain
was shown by the physical contact between an ETC supercomplex CIII2 + CIV with the TIM23
protein translocase complex 213,214. A formation of supramolecular complexes has been reported
for OXPHOS complexes and IMM transport proteins, such as between COX and adenine
nucleotide transporter (ANT) in yeast mitochondria, and LDH and monocarboxylate
transporters MCT1 and MCT2 in rat neurons 215. Another interesting question is whether a
functional protein module of a higher order can be formed. In particular, the interaction of
mitoBK with ANT through VEDEC terminal motif was shown 82. Exploring whether mitoBK
can interact with both respirasomes and ANT would be an interesting challenge.
In a study of the molecular mechanisms of ataxia in cells harboring a mutation in the KCNMA1
BKG354S that impaired channel gating, the amount of the subunits CORE2 of complex III, COX2
of complex V, NDUFB8 of complex I was negatively affected 216. On the other side, no link
between the observed decreased amount of mito BK-α and the structural impairment of COX
has been reported to date. A phenomenon of the dec rease in the amount of mito BK-α-formed
complexes could be explained on several levels. Firstly, KCNMA1 was transcriptionally


134

downregulated in mtDNA -depleted cells. However, no significant decrease in the KCNMA1
transcript amount was observed in COX8A-deficient fibroblasts. Secondly, a lack of functional
ETC in the mtDNA -depleted cells, as well as the impairment in COX activity in COX8A -
deficient cells, can lead to th e loss of the mitochondrial potential. Therefore, the electrogenic
mitochondrial protein import into the IMM through the TOM/TIM complexes can be hindered.
However, the BN-PAGE results in the mtDNA-depleted cell indicated that while various IMM
protein complexes were affected, the extent of their downregulation was different. In particular,
the import of another IMM ion channel – the MCU complex – appeared to be affected to a
lesser degree. Thirdly, protein turnover can be higher in mitochondria with functi onal
impairments. Yet, no indication of transcriptional upregulation of mitochondrial proteases in
both mtDNA -depleted cells and COX8A -deficient fibroblasts was observed. Fourthly, a
molecular mechanism targeting mitoBK channel subunits to mitochondria could be affected by
the deficiencies in ETC or COX in particular.



135

7.4. Mechanisms of modulation of mitoBK channels by the CO and heme
signaling

Due to the abundance of the heme proteins, as well as the presence of the enzymes indispensable
in the heme bio synthesis, mitochondria are one of the major key targets of the CO signaling
pathways 141. Similar to plasma membrane BK channels, mitoBK channels possess the heme-
binding domain and have been shown to be inhibited by hemin  129. However, the modulation
of mitoBK channels by CO has not been extensively studied. The CORMs are widely used as
a CO delivery tool to study its biological effects. Considering the growing number of the data
reporting discrepant molecular mechanisms of plasma membrane BK channel modulation by
CO that were obtained with the use of CORMS 138,217,218, as well as recent reports highlighting
pleiotropic effects of CORMs in different biological systems  140,156,219, the effects of three
structurally different CORMs on the mitoBK channel activity were compared to the application
of the CO gas in the present study.
A fast CO releaser CORM -2 containing a ruthenium moiety has been one of the most widely
used tools for studying the CO effects in vitro 220,221. Notably, a recent report has identified that
CORM-2 is prone to form an adduct in a reaction with histidine 156. Moreover, activation of the
plasma BK channels by CORM -2 was substantially diminished by the external addition of
histidine. In a study of the modulation of Kv2.1 channels by CORM-2, the inhibitory action of
this compound was similar to the effect on the channels observed after the CO application  222.
However, the effects of CORM -2 on the mitoBK channels could n ot be reproduced by the
application of the CO and therefore cannot be further attributed to the activity of the CO gas
released by this delivery vehicle. Specifically, CORM-2 exerted two types of effects on mitoBK
channels: transient activation followed by inhibition, or direct inhibition of the channel activity.
Such a phenomenon could be explained by heterogeneity of mitoBK channels: due to the
various alternatively spliced mitoBK-α subunits that can localize in mitochondria , or protein
complexes of mitoBK with other proteins in IMM, including the respiratory chain  104,106.
Different interactions of CORM-2 with the histidine residues of mitoBK subunits or its protein
partners in the IMM with high protein density could be responsible for pleiotropic mechanisms
of mitoBK modulation by CORM-2.
A structurally different slow releaser CORM studied in the context of mitoBK modulation is a
manganese–containing CORM -401 223. Pre viously, direct activation of mitoBK channels in
EA.hy926 cells after application of CORM -401 was reported  137. CORM-401 exerted


136

multimodal modulation of mitochondrial function, affecting respiration, generation of ATP,
and proton uncoupling. Interestingly, in the current study application of CORM-401 in a similar
experimental setting has not induced an observable modulation in the mitoBK channel activity
in astrocytoma cells. In a similar manner, while CORM -401 has increased the respiration of
microglial cells, mitoBK channels were not involved in this effect  224. However, it should be
noted that the mitoBK channels in these cell types are comprised of different auxiliary beta -
subunits: BK-β2 subunit in the endothelial cells  67, BK-β3 subunit in the microglial cells  225,
and mostly BK-β4 in the astrocytoma mitochondria. Thus, the different structural compositions
of mitoBK channels could underlie the variations in its pharmacological modulation by CORM-
401. Notably, CORM-401 has displayed CO-independent effects in a study on E. coli, having
an uncoupling effect and stimulating bacterial respiration 219.
Next, the effects of a slow CO-releaser CORM-A1 containing sodium boranocarbonate on the
mitoBK channels were analyzed. While CORM-A1 does not contain a transition metal ion in
its structure, and therefore, could be less likely to have a CO-independent biological activity, it
hasn’t been widely studied in the context of modulation of potassium ion channels. In this work,
perfusion of a patch with a CORM -A1-containing solution did not affect mitoBK channel
activity. In a study where structurally different CORMs were administered in the endothelial
cellular model of oxidative stress, CORM -2 and CORM -A1 had differe nt molecular
mechanisms of the antioxidative effects - in particular, CORM -A1 did not modulate the
generation of ROS in mitochondria  226,227. While these compounds have different water
solubility, the released CO molecules easily traverse mitoc hondrial membranes by diffusion.
Thus, the differences in the biological effects between CORM-A1 and CORM-2 are at least in
part caused by the activity of their metal complex-containing cores.
Therefore, caution should be exercised when CORMs are used a tool for the study of the
biological properties of CO. The process of the release of CO by CORMs involves a stepwise
degradation with a formation of intermediate or final degradation products with a variable
number of carbonyls substituted with water or DMSO, which could possess different biological
activities. However, since the aim of the current study was to identify whether endogenous CO
modulates the activity of the mitoBK channel, the molecular mechanisms of the diverse effects
(or lack thereof) of structurally different CORMs is outside the scope of this work.
To identify the direct effects of the CO application to mitoBK channels, the patches containing
these channels were perfused with a solution saturated in the CO gas. No change in the channel
activity was observed after direct application of CO, endorsing the previously reported concept


137

that BK channels require prior binding of heme for the CO modulation 157. Specifically, as most
isoforms of pore -forming mitoBK-α subunits encoded by KCNMA1 contain the C -terminal
structural motif -CXXCH- between the two RCK domains, mitoBK channels can bind heme,
similar to the plasma membrane BK channels.
Heme is distributed between two cellular pools: a fraction bound to the so -called
“housekeeping” heme proteins (including cytochrome c oxidase, hemoglobin, peroxidases ,
etc.), and a smaller “labile” pool of heme acting as a signaling mediator 228. Heme c is covalently
bound to COX via thioether bonds between the heme and Cys residues within the HBD  229. In
contrast, plasma membrane BK channels interact with heme b, and the binding of CO to
mitoBK channels would be an event of the transient and reversible nature 127. Binding of heme
modifies the gating ring confirmation, thus disrupting the Ca 2+ and voltage gating, and
inhibiting the channel activity. A functional proof of the inhibition of the mitoBK channels by
the oxidized heme – hemin – has been previously obtained 155. Inhibition of mitoBK channels
by heme reported in the present work supports the notion that mitoBK channels possess HBD
and are modulated by binding heme or hemin.
Hemin is a metalloporphyrin containing a ferric Fe3+ atom, which cannot bind CO. In this study,
inhibition of the mitoBK channel activity with hemin could not be released with CO. However,
application of CO after the perfusion of the channels with the ferrous Fe 2+ heme has released
the channel inhibition. This functional observation confirms that heme is a receptor for the CO
action in the mitoBK channels, acting in a similar manner to the observations reported on the
plasma membrane BK channels 157. Notably, heme and CO signaling pathways target KATP ion
channels by an equivalent molecular mechanism: the channel comprised of Kir6.2 and SUR2A
is activated by CO exclusively following the binding of heme to the SUR2A subunit 230.
Several interesting other open questions arise from this observation. A presence of the Cys
thiol-disulfide switch has been reported within the HBD of the plasma membrane BK channels,
which regulates the affinity of the channels to heme in a redox -sensitive manner 231. Whether
this structural element is present in mitoBK remains to be identified, however, its presence
could introduce another dimension to the heme/CO signaling in the context of mi tochondrial
redox signaling functions.
Heme turnover is a regulated process, as in the free form it is a highly reactive molecule. The
iron bound to porphyrin is involved in pathophysiological processes due to its role in the
generation of the reactive ox ygen species – specifically, the synthesis of hydroxyl radicals in
the Fenton reaction 232. Heme oxygenase is a crucial enzyme in heme catabolism, acting as one


138

of the cytoprotective proteins in the events of ischemia -reperfusion injury. Following the
elimination of heme by heme oxygenases, CO, Fe 2+, and bilirubin are produced. Interestingly,
it was shown that plasma membrane BK channels and HO -2 co -localize in the plasma
membrane, forming a multiprotein signaling unit  233. Interaction of the mitoBK channels with
CO can be regulated by the local synthesis of CO in mi tochondria by the HO -1, which can
translocate to this organelle 234. The expression of heme oxygenase 1 is induced by the oxidative
stress signaling, in particular, in the mtDNA -depleted astrocytoma cells, and can be linked to
the ROS synthesis following the mitochondrial dysfunction. Therefore, degradation of heme by
the mitochondrial HO -1 decreases the available pool of heme and produces CO. A resulting
higher activation of the mitoBK channels thus provides feedback control of generation of ROS
in mitochondria, what could be particularly relevant in the cytoprotective signaling conferred
by the mitoBK channel activation.
An additional layer of regulation of the mitoBK channel by the CO is conferred by the
downstream effects of activation of other molecular targets of this mediator, such as increased
synthesis of cGMP following the activation of guanylyl cyclase by CO  235. An observation of
the increased activity of mitoBK channels after addition of cGMP together with a protein kinase
G further supports an activatory role of CO on these channels 125.



139

8. CONCLUSIONS AND SUMMARY

I. In human astrocytoma cells and dermal fibroblasts, the expression of genes encoding mitoBK
channel subunits – KCNMA1, KCNMB3, KCNMB4 – as well as translated proteins localized to
the mitochondria was confirmed. The mitoBK channel activity in mitoplasts of astrocytoma
cells was characterized on the single-channel level.
II. The pore-forming mitoBK-α subunit interacts with the cytochrome c oxidase (COX) and can
be a part of the respiratory chain supercomplexes in astrocytoma mitochondria.  Depletion of
mtDNA triggers the integrated stress response (ISR) signaling in the human astrocytoma cells.
1. A cell line devoid of mtDNA was developed by the treatment of hu man astrocytoma
cells with 2′,3′-dideoxycytidine (ddC). A sharp decre ase in the amount of transcripts
encoded by the mtDNA was observed, alongside the absence of the properly formed
multiprotein complexes of the electron transport chain. On the functional level, the
depletion of mtDNA was confirmed by the abolishment of respiration of these cells.
2. The interaction of the pore-forming mitoBK-α subunit with the COX in mitochondria
of the human ast rocytoma cells occurs on the level of the respiratory chain
supercomplexes.
3. The amount of the complexes formed by the mitoBK -α subunit, as well as its total
protein amount was significantly downregulated in the m tDNA-depleted astrocytoma
cells. A downregulation of the expression of KCNMA1 was observed.
4. About 5% of genes were differentially expressed in the mtDNA -depleted cells. The
depletion of mtDNA initiated the ISR. In addition, the transcriptional upregulation of
the antioxidant enzymatic functional network under the common transcriptional control
by Nrf2 occurred.
III. The nuclear -encoded COX subunit COX8A is required for the maintenance of the
structural stability of COX. The loss of COX8A leads to COX deficiency, which is
manifested by the reduced am ount of COX protein complexes and a decrease in its
enzymatic activity. The residual COX in the COX8A-deficient cells is stabilized within the
respirasomes, and ISR or mtUPR caused by the misassembled intermediates of the COX
monomer does not occur.
1. The pr otein amount of all evaluated COX subunits was decreased in the COX8A -
deficient fibroblasts. The residual COX was stabilized in the respirasomes.


140

2. Induction of the COX8A deficiency in HEK293T cells by CRISPR/Cas9 generated two
clonal cell lines with mutations in COX8A, each containing in-frame deletions affecting
the mitochondrial targeting sequence in one allele, and frameshift mutations in another
one. The protein amount of COX subunits amount was decreased in both cell lines. In
the cell line with a larger deletion of the COX8A mitochondrial targeting sequence, the
residual COX was stabilized largely in the respirasomes.
3. No evidence of the ISR or mitochondrial unfolded protein response  signaling was
observed in the transcriptome of both COX8A-deficient cell lines.
4. In the COX8A-deficient fibroblasts, the amount of the protein complexes formed by the
mitoBK-α subunits was decreased, yet it was not regulated on the transcriptional level.
IV. CO activates mitoBK channels in astrocytoma cells , however, prior he me binding to
mitoBK is required as a receptor for the CO action.
1. In a study of the regulation of mitoBK channel activity by CO, the effects of different
CORMs did not necessarily replicate those of the CO gas applied to mitoBK channels
in astrocytoma mitochondria.
2. Application of heme and hemin inhibited mitoBK channel activity.
3. No effect of the CO gas applied alone was observed on the mitoBK channel activity ,
despite a known interaction of CO with the COX.
4. Following the inhibition of the mitoBK channels w ith heme, the application of CO
reactivated mitoBK channel activity.




141

9. LIST OF PUBLICATIONS

The results included in the thesis are presented in the following publications:
 Rotko D ., Kudin A. P., Zsurka G., Kulawiak B., Szewczyk A., Kunz W. S. (2021).
Molecular and functional effects of loss of cytochrome c oxidase subunit 8A. Biochemistry
(Moscow), 86(1), 33-43.
 Rotko D., Bednarczyk P., Koprowski P., Kunz W. S., Szewczyk A., Kulawiak B. (2020).
Heme is required for carbon monoxide activation of mitochondrial BKCa channel. European
Journal of Pharmacology, 173191.
 Augustynek B., Koprowski P., Rotko D., Kunz W. S., Szewczyk A., Kulawiak B. (2018).
Mitochondrial BK channel openers CGS7181 and CGS7184 exhibit cytotoxic properties.
International journal of molecular sciences, 19(2), 353.
 Rotko D., Kunz W. S., Szewczyk A., Kulawiak B. (2020). Signaling pathways targeting
mitochondrial potassium channels. The international journal of biochemistry & cell
biology, 105792. (Review paper)

The additional author’s publications include:
 Szewczyk A., Bednarczyk P., Jędraszko J., Kampa R.P., Koprowski P., Krajewska M.,
Kucman S., Kulawiak B., Laskowski M., Rotko D., Sęk A., Walewska A., Żochowska M.,
Wrzosek A. (2018). Mitochondrial potassium channels - an overview. Postępy biochemii,
64(3): 196-212.

The results were disseminated at the scientific meetings as oral presentations:
 9th Mitochondrion Conference, Poland, January 2021: RNA sequencing analysis of
transcriptome changes upon mtDNA depletion with the focus on potassium ion channels.
 Rheinland Redox Research Meeting, Cologne, Germany, March 2019: Interaction of
mitochondrial BKCa channel with cytochrome c oxidase.
 FEBS3+ Meeting – XI Parnas Conference, Kyiv, Ukraine, September 2018: Mitochondrial
potassium channels and carbon monoxide signaling.
 6th Mitochondrion Conference, Poznań, Poland, December 2017: Diverse pharmacological
effects of carbon-monoxide releasing molecules on mitochondrial BK channel.


142

The poster presentations were made at the following international conferences:
 Rotko D., Kulawiak B., Kunz W. S., Szewczyk  A. (2018). Role of subunit COX8A in
biogenesis of cytochrome c oxidase in human fibroblasts. Biochimica et Biophysica Acta
(BBA) – Bioenergetics, 1859: e71-e72. 20th European Bioenergetics Conference, Budapest,
Hungary, 2018.
 Rotko D., Kulawiak B., Kunz W. S., Szewczyk A. (2018). Organization of respiratory chain
in human fibroblasts with cytochrome c oxidase deficiency caused by loss of COX8A
subunit. FEBS Open Bio , 8: P.09­037. 43rd FEBS Congress and FEBS Young Scientist
Forum, Prague, Czech Republic, 2018.
 Rotko D., Bednarczyk P., Szewczyk A. (2018). Diverse pharmacological effects of carbon
monoxide-releasing molecules on mitochondrial BK channel. Biophysical Journal, 114(3),
488a. 62nd Annual Meeting of Biophysical Society, San Francisco, USA, 2018.
 Rotko D., Bednarczyk P., Koprowski P., Szewczyk A. (2016). “New properties of the
mitochondrial large -conductance Ca2+ -activated K+ channel from astrocytoma
mitochondria”. Biochimica et Biophysica Acta (BBA) – Bioenergetics, 1857: e70-e71. 19th
European Bioenergetics Conference, Riva del Garda, Italy, 2016.



143

10. REFERENCES

1.  Roger AJ, Muñoz -Gómez SA, Kamikawa R. The Origin and Diversification of
Mitochondria. Curr Biol. 2017;27(21):R1177-R1192. doi:10.1016/j.cub.2017.09.015
2.  Gray MW. Mosaic nature of the mitochondrial proteome: Implications for the origin and
evolution of mitochondria. Proc Natl Acad Sci U S A . 2015;112(33):10133 -10138.
doi:10.1073/pnas.1421379112
3.  Wallace DC. Bioenergetics, the origins of complexity, and the ascent of man. Proc Natl
Acad Sci U S A. 2010;107(SUPPL. 2):8947-8953. doi:10.1073/pnas.0914635107
4.  Muñoz-Gómez SA, Wideman JG, Roger AJ, Slamovits CH, Agashe D. The origin of
mitochondrial cristae from alphaproteobacteria. Mol Bi ol Evol . 2017;34(4):943 -956.
doi:10.1093/molbev/msw298
5.  Martin W, Russell MJ. On the origin of biochemistry at an alkaline hydrothermal vent.
Philos Trans R Soc Lond B Biol Sci . 2007;362(1486):1887 -1925.
doi:10.1098/RSTB.2006.1881
6.  Mailloux RJ. An up date on mitochondrial reactive oxygen species production.
Antioxidants. 2020;9(6):472. doi:10.3390/antiox9060472
7.  Embley TM, Martin W. Eukaryotic evolution, changes and challenges. Nat 2006
4407084. 2006;440(7084):623-630. doi:10.1038/nature04546
8.  Calvo SE, Clauser KR, Mootha VK. MitoCarta2.0: An updated inventory of mammalian
mitochondrial proteins. Nucleic Acids Res . 2016;44(D1):D1251 -D1257.
doi:10.1093/nar/gkv1003
9.  Kulawiak B, Höpker J, Gebert M, Guiard B, Wiedemann N, Gebert N. The mitochondrial
protein import machinery has multiple connections to the respiratory chain. Biochim
Biophys Acta - Bioenerg. 2013;1827(5):612-626. doi:10.1016/j.bbabio.2012.12.004
10.  Vögtle FN, Wortelkamp S, Zahedi RP, et al. Global Analysis of the Mitochondrial N -
Proteome Identifies a Processing Peptidase Critical for Protein Stability. Cell.
2009;139(2):428-439. doi:10.1016/j.cell.2009.07.045
11.  Letts JA, Fiedorczuk K, Sazanov LA. The architecture of respiratory supercomplexes.
Nature. 2016;537(7622):644-648. doi:10.1038/nature19774


144

12.  Barros MH, McStay GP. Modular biogenesis of mitochondrial respiratory complexes.
Mitochondrion. 2020;50(October 2019):94-114. doi:10.1016/j.mito.2019.10.008
13.  Hackenbrock CR, Chazotte B, Gupte SS. The random collision model and a  critical
assessment of diffusion and collision in mitochondrial electron transport. J Bioenerg
Biomembr. 1986;18(5):331-368. doi:10.1007/BF00743010
14.  Schägger H, Pfeiffer K. The Ratio of Oxidative Phosphorylation Complexes I -V in
Bovine Heart Mitochondria and the Composition of Respiratory Chain Supercomplexes.
J Biol Chem. 2001;276(41):37861-37867. doi:10.1074/jbc.M106474200
15.  Greggio C, Jha P, Kulkarni SS, et al. Enhanced Respiratory Chain Supercomplex
Formation in Response to Exercise in Human Ske letal Muscle. Cell Metab .
2017;25(2):301-311. doi:10.1016/j.cmet.2016.11.004
16.  Gu J, Wu M, Guo R, et al. The architecture of the mammalian respirasome. Nature.
2016;537(7622):639-643. doi:10.1038/nature19359
17.  Sousa JS, Mills DJ, Vonck J, Kühlbrandt W. Functional asymmetry and electron flow in
the bovine respirasome. Elife. 2016;5(NOVEMBER2016). doi:10.7554/eLife.21290
18.  Cogliati S, Frezza C, Soriano ME, et al. Mitochondrial cristae shape determines
respiratory chain supercomplexes assembly and res piratory efficiency. Cell.
2013;155(1):160-171. doi:10.1016/J.CELL.2013.08.032
19.  Hirst J. Open questions: Respiratory chain supercomplexes-why are they there and what
do they do? BMC Biol. 2018;16(1):5-8. doi:10.1186/s12915-018-0577-5
20.  Acin-Perez R,  Enriquez JA. The function of the respiratory supercomplexes: The
plasticity model. Biochim Biophys Acta - Bioenerg. 2014;1837(4):444 -450.
doi:10.1016/J.BBABIO.2013.12.009
21.  Fedor JG, Hirst J. Mitochondrial Supercomplexes Do Not Enhance Catalysis by Quinone
Channeling. Cell Metab. 2018;28(3):525-531.e4. doi:10.1016/j.cmet.2018.05.024
22.  Maranzana E, Barbero G, Falasca AI, Lenaz G, Genova ML. Mitochondrial respiratory
supercomplex association limits production of reactive oxygen species from complex i.
Antioxidants Redox Signal. 2013;19(13):1469-1480. doi:10.1089/ars.2012.4845
23.  Blaza JN, Serreli R, Jones AJY, Mohammed K, Hirst J. Kinetic evidence against
partitioning of the ubiquinone pool and the catalytic relevance of respiratory -chain


145

supercomplexes. Proc Natl Acad Sci U S A . 2014;111(44):15735 -15740.
doi:10.1073/pnas.1413855111
24.  Letts JA, Sazanov LA. Clarifying the supercomplex: the higher-order organization of the
mitochondrial electron transport chain. Nat Struct Mol Biol 2017 2410. 2017;24(10):800-
808. doi:10.1038/nsmb.3460
25.  Calvaruso MA, Willems P, Van den brand M, et al. Mitochondrial complex III stabilizes
complex I in the absence of NDUFS4 to provide partial activity. Hum Mol Genet .
2012;21(1):115-120. doi:10.1093/hmg/ddr446
26.  Schägger H, De Coo R, Bauer MF, Hofmann S, Godino C, Brandt U. Significance of
respirasomes for the assembly/stability of human respiratory chain complex I. J Biol
Chem. 2004;279(35):36349-36353. doi:10.1074/jbc.M404033200
27.  Tropeano C V., Aleo SJ, Zanna C , et al. Fine -tuning of the respiratory complexes
stability and supercomplexes assembly in cells defective of complex III. Biochim
Biophys Acta - Bioenerg. 2020;1861(2):148133. doi:10.1016/j.bbabio.2019.148133
28.  Bindoli A, Rigobello MP. Electrons and Pr otons | Peroxidase Biochemistry and Redox
Signaling. Encycl Biol Chem Third Ed . 2021;2:579 -585. doi:10.1016/B978 -0-12-
809633-8.21402-7
29.  Timón-Gómez A, Nývltová E, Abriata LA, Vila AJ, Hosler J, Barrientos A.
Mitochondrial cytochrome c oxidase biogenesis: Recent developments. Semin Cell Dev
Biol. 2018;76:163-178. doi:10.1016/j.semcdb.2017.08.055
30.  Stiburek L, Vesela K, Hansikova H, et al. Tissue-specific cytochrome c oxidase assembly
defects due to mutations in SCO2 and SURF1. Biochem J . 2005;392(3):6 25-632.
doi:10.1042/BJ20050807
31.  Bourens M, Boulet A, Leary SC, Barrientos A. Human COX20 cooperates with SCO1
and SCO2 to mature COX2 and promote the assembly of cytochrome c oxidase. Hum
Mol Genet. 2014;23(11):2901-2913. doi:10.1093/hmg/ddu003
32.  Vidoni S, Harbour ME, Guerrero -Castillo S, et al. MR -1S Interacts with PET100 and
PET117 in Module -Based Assembly of Human Cytochrome c Oxidase. Cell Rep .
2017;18(7):1727-1738. doi:10.1016/j.celrep.2017.01.044
33.  Zong S, Wu M, Gu J, Liu T, Guo R, Yang M. S tructure of the intact 14-subunit human


146

cytochrome c oxidase. Cell Res . 2018;28(10):1026 -1034. doi:10.1038/s41422 -018-
0071-1
34.  Timón-Gómez A, Nývltová E, Abriata LA, Vila AJ, Hosler J, Barrientos A.
Mitochondrial cytochrome c oxidase biogenesis: Recent developments. Semin Cell Dev
Biol. 2018;76:163-178. doi:10.1016/j.semcdb.2017.08.055
35.  Brischigliaro M, Zeviani M. Cytochrome c oxidase deficiency. Biochim Biophys Acta -
Bioenerg. 2021;1862(1):148335. doi:10.1016/J.BBABIO.2020.148335
36.  Cogliati S, C alvo E, Loureiro M, et al. Mechanism of super -assembly of respiratory
complexes III and IV. Nat 2016 5397630 . 2016;539(7630):579 -582.
doi:10.1038/nature20157
37.  Kovářová N, Pecina P, Nůsková H, et al. Tissue - and species -specific differences in
cytochrome c oxidase assembly induced by SURF1 defects. Biochim Biophys Acta - Mol
Basis Dis. 2016;1862(4):705-715. doi:10.1016/j.bbadis.2016.01.007
38.  Fukuda R, Zha ng H, Kim J whan, Shimoda L, Dang C V., Semenza GLL. HIF -1
regulates cytochrome oxidase subunits to optimize efficiency of respiration in hypoxic
cells. Cell. 2007;129(1):111-122. doi:10.1016/J.CELL.2007.01.047
39.  Tello D, Balsa E, Acosta -Iborra B, et al . Induction of the Mitochondrial NDUFA4L2
Protein by HIF -1α Decreases Oxygen Consumption by Inhibiting Complex I Activity.
Cell Metab. 2011;14(6):768-779. doi:10.1016/J.CMET.2011.10.008
40.  Napiwotzki J, Shinzawa -Itoh K, Yoshikawa S, Kadenbach B. ATP and ADP bind to
cytochrome c oxidase and regulate its activity. Biol Chem . 1997;378(9):1013 -1021.
doi:10.1515/bchm.1997.378.9.1013
41.  Kalpage HA, Bazylianska V, Recanati MA, et al. Tissue-specific regulation of
cytochrome c by post -translational modification s: respiration, the mitochondrial
membrane potential, ROS, and apoptosis. FASEB J . 2019;33(2):1540.
doi:10.1096/FJ.201801417R
42.  Diaz F. Cytochrome c oxidase deficiency: Patients and animal models. Biochim Biophys
Acta - Mol Basis Dis. 2010;1802(1):100-110. doi:10.1016/J.BBADIS.2009.07.013
43.  Rak M, Bénit PP, Chrétien D, et al. Mitochondrial cytochrome c oxidase deficiency. Clin
Sci. 2016;130(6):393-407. doi:10.1042/CS20150707


147

44.  Dimauro S, Tanji K, Schon EA. The Many Clinical Faces of Cytochrome  Oxi dase
Deficiency. Adv Exp Med Biol. 2012;748:341-357. doi:10.1007/978-1-4614-3573-0_14
45.  Szabo I, Zoratti M. Mitochondrial channels: Ion fluxes and more. Physiol Rev .
2014;94(2):519-608. doi:10.1152/physrev.00021.2013
46.  Jasielec JJ, Filipek R, Dołowy K, Lewenstam A. Precipitation of Inorganic Salts in
Mitochondrial Matrix. Membr 2020, Vol 10, Page 81 . 2020;10(5):81.
doi:10.3390/MEMBRANES10050081
47.  Killilea DW, Killilea AN. Mineral requirements for mitochondrial fu nction: A
connection to redox balance and cellular differentiation. Free Radic Biol Med .
2022;182:182-191. doi:10.1016/J.FREERADBIOMED.2022.02.022
48.  Santo-Domingo J, Demaurex N. Calcium uptake mechanisms of mitochondria. Biochim
Biophys Acta - Bioenerg. 2010;1797(6-7):907-912. doi:10.1016/J.BBABIO.2010.01.005
49.  Colombini M. VDAC structure, selectivity, and dynamics. Biochim Biophys Acta -
Biomembr. 2012;1818(6):1457-1465. doi:10.1016/J.BBAMEM.2011.12.026
50.  Hill K, Model K, Ryan MT, et al. Tom40 for ms the hydrophilic channel of the
mitochondrial import pore for preproteins. Nat 1998 3956701. 1998;395(6701):516-521.
doi:10.1038/26780
51.  Inoue I, Nagase H, Kishi K, Higuti T. ATP -sensitive K+ channel in the mitochondrial
inner membrane. Nature. 1991;352(6332):244-247. doi:10.1038/352244a0
52.  Garlid KD. Cation transport in mitochondria - The potassium cycle. In: Biochimica et
Biophysica Acta - Bioenergetics. Vol 1275. Elsevier B.V.; 1996:123 -126.
doi:10.1016/0005-2728(96)00061-8
53.  Skalska J, Piwońska M, Wyroba E, et al. A novel potassium channel in skeletal muscle
mitochondria. Biochim Biophys Acta - Bioenerg. 2008;1777(7 -8):651-659.
doi:10.1016/j.bbabio.2008.05.007
54.  Heinen A, Camara AKS, Aldakkak M, Rhodes SS, Riess ML, Stowe DF. Mitochondrial
Ca2+-induced K+ influx increases respiration and enhances ROS production while
maintaining membrane potential. Am J Physiol - Cell Physiol . 2007;292(1):148 -156.
doi:10.1152/ajpcell.00215.2006
55.  O’Rourke B. Mitochondrial ion channel s. Annu Rev Physiol . 2007;69:19 -49.


148

doi:10.1146/annurev.physiol.69.031905.163804
56.  Anderson PAV, Greenberg RM. Phylogeny of ion channels: Clues to structure and
function. Comp Biochem Physiol - B Biochem Mol Biol . 2001;129(1):17 -28.
doi:10.1016/S1096-4959(01)00376-1
57.  Thiel G, Moroni A, Blanc G, Van Etten JL. Potassium Ion Channels: Could They Have
Evolved from Viruses? Plant Physiol. 2013;162(3):1215. doi:10.1104/PP.113.219360
58.  Ye S, Li Y, Jiang Y. Novel insights into K+ selectivity from high -resolution structures
of an open K+ channel pore. Nat Struct Mol Biol 2010 178 . 2010;17(8):1019 -1023.
doi:10.1038/nsmb.1865
59.  Szewczyk A, Jędraszko J, Kampa RP, et al. Mitochondrial potassium channels - an
overview. Postepy Biochem. 2018;64(3):196-212. doi:10.18388/pb.2018_132
60.  Checchetto V, Prosdocimi E, Leanza L. Mitochondrial Kv1.3: a New Target in Cancer
Biology? Cell Physiol Biochem. 2019;53(S1):52-62. doi:10.33594/000000195
61.  Checchetto V, Azzolini M, Peruzzo R, Capitanio P, Leanza L. Mitochondrial potassium
channels in cell death. Biochem Biophys Res Commun . 2018;500(1):51 -58.
doi:10.1016/j.bbrc.2017.06.095
62.  Bonnet S, Archer SL, Allalunis -Turner J, et al. A Mitochondria -K+ Channel Axis Is
Suppressed in Cancer and Its Normalization Promotes Apoptosis and Inhibits Cancer
Growth. Cancer Cell. 2007;11(1):37-51. doi:10.1016/j.ccr.2006.10.020
63.  Testai L, Barrese V, Soldovieri MV, et al. Expression and function of Kv7.4 channels in
rat cardiac mitochondria: Possible targets for cardioprotection. Cardiovasc Res .
2016;110(1):40-50. doi:10.1093/cvr/cvv281
64.  Paggio A, Checchetto V, Campo A, et al. Identification of  an ATP-sensitive potassium
channel in mitochondria. Nat 2019 5727771 . 2019;572(7771):609 -613.
doi:10.1038/s41586-019-1498-3
65.  Juhaszova M, Kobrinsky E, Zorov DB, et al. ATP Synthase K+- and H+-fluxes Drive
ATP Synthesis and Enable Mitochondrial K+ -“Uniporter” Function: II. Ion and ATP
Synthase Flux Regulation. Function. 2022;3(2). doi:10.1093/function/zqac001
66.  Smith CO, Wang YT, Nadtochiy SM, et al. Cardiac metabolic effects of KNa1.2 channel
deletion and evidence for its mitochondrial localization.  FASEB J. 2018;32(11):6135-


149

6149. doi:10.1096/fj.201800139R
67.  Bednarczyk P, Koziel A, Jarmuszkiewicz W, Szewczyk A. Large -conductance Ca 2+-
activated potassium channel in mitochondria of endothelial EA.hy926 cells. Am J
Physiol Heart Circ Physiol. 2013;304(11). doi:10.1152/AJPHEART.00976.2012
68.  Piwonska M, Wilczek E, Szewczyk A, Wilczynski GM. Differential distribution of
Ca2+-activated potassium channel β4 subunit in rat brain: Immunolocalization in
neuronal mitochondria. Neuroscience. 2008;153(2):446 -460.
doi:10.1016/j.neuroscience.2008.01.050
69.  Xu W, Liu Y, Wang S, et al. Cytoprotective role of Ca2+ -activated K+ channels in the
cardiac inner mitochondrial membrane. Science (80 - ). 2002;298(5595):1029 -1033.
doi:10.1126/science.1074360
70.  Skalska J, Piwońska M, Wyroba E, et al. A novel potassium channel in skeletal muscle
mitochondria. Biochim Biophys Acta . 2008;1777(7 -8):651-659.
doi:10.1016/J.BBABIO.2008.05.007
71.  Kicinska A, Augustynek B, Kulawiak B, Jarmuszkiewicz W, Szewczyk A, Bednarczyk
P. A large -conductance calcium -regulated K + channel in human dermal fibroblast
mitochondria. Biochem J. 2016;473(23):4457-4471. doi:10.1042/BCJ20160732
72.  Koszela-Piotrowska I, Matkovic K, Szewczyk A, Jarmuszkiewicz W. A large -
conductance calcium-activated potassium channel in potato (Solanum tuberosum) tuber
mitochondria. Biochem J. 2009;424(2):307-316. doi:10.1042/BJ20090991
73.  Laskowski M, Kicinska A, Szewczyk A, Jarmuszkiewicz W. Mitochondrial large -
conductance potassium channel from Dictyostelium dis coideum. Int J Biochem Cell
Biol. 2015;60:167-175. doi:10.1016/J.BIOCEL.2015.01.006
74.  Tress ML, Abascal F, Valencia A. Alternative Splicing May Not Be the Key to Proteome
Complexity. Trends Biochem Sci. 2017;42(2):98-110. doi:10.1016/j.tibs.2016.08.008
75.  Miller JP, Moldenhauer HJ, Keros S, Meredith AL. An emerging spectrum of variants
and clinical features in KCNMA1 -linked channelopathy.
https://doi.org/101080/1933695020211938852. 2021;15(1):447 -464.
doi:10.1080/19336950.2021.1938852
76.  Singh H, Lu R, Bopassa JC, Meredith AL, Stefani E, Toro L. MitoBKCa is encoded by


150

the Kcnma1 gene, and a splicing sequence defines its mitochondrial location. Proc Natl
Acad Sci U S A. 2013;110(26):10836-10841. doi:10.1073/pnas.1302028110
77.  Gałecka S, Kulawiak B, Bednarczyk P, Singh H, Szewczyk A. Single channel properties
of mitochondrial large conductance potassium channel formed by BK -VEDEC splice
variant. Sci Reports 2021 111. 2021;11(1):1-12. doi:10.1038/s41598-021-90465-3
78.  Ma D, Nakata T, Zhang G, Hoshi T, Li M, Shikano S. Differential trafficking of carboxyl
isoforms of Ca2+-gated (Slo1) potassium channels. FEBS Lett. 2007;581(5):1000-1008.
doi:10.1016/J.FEBSLET.2007.01.077
79.  Walewska A, Kulawiak B, Szewczyk A, Koprowski P. Mechanosensitivity of
mitochondrial large -conductance calcium -activated potassium channels. Biochim
Biophys Acta - Bioenerg. 2018;1859(9):797-805. doi:10.1016/j.bbabio.2018.05.006
80.  Chen L, Bi D, Tian L, et al. Palmitoylation of the β4-subunit regulates surface expression
of large conductance calcium-activated potassium channel splice variants. J Biol Chem.
2013;288(18):13136-13144. doi:10.1074/jbc.M113.461830
81.  Engel AJ, Kithil M, Langhans M, et al. Codon Bias Can Determine Sorting of a
Potassium Channel Protein. Cells. 2021;10(5):1128. doi:10.3390/cells10051128
82.  Zhang J, Li M, Zhang Z, et al. The mitochondrial BKCa channel cardiac interactome
reveals BKCa association with the mitochondrial import receptor subunit Tom22, and
the adenine nucleotide translocator. Mitochondrion. 2017;33:84-101.
doi:10.1016/j.mito.2016.08.017
83.  Wang L, Sigworth FJ. Structure of the BK potassium channel in a lipid membrane from
electron cryomicroscopy. Nat 2009 4617261 . 2009;461(7261):292 -295.
doi:10.1038/nature08291
84.  Tao X, Mackinnon R. Mol ecular structures of the human slo1 k+ channel in complex
with b4. Elife. 2019;8. doi:10.7554/ELIFE.51409
85.  Peng Yuan, Leonetti MD, Pico AR, Hsiung Y, MacKinnon R. Structure of the Human
BK Channel Ca2+ -Activation Apparatus at 3.0 Å Resolution. Science (80- ).
2010;329(5988):182-186. doi:10.1126/science.1190414
86.  González-Cota AL, Santana-Calvo C, Servín-Vences R, Orta G, Balderas E. Regulatory
mechanisms of mitochondrial BKCa channels. Channels. 2021;15(1):424 -437.


151

doi:10.1080/19336950.2021.1919463
87.  Lee US, Cui J. BK channel activation: Structural and functional insights. Trends
Neurosci. 2010;33(9):415-423. doi:10.1016/j.tins.2010.06.004
88.  Yang H, Zhang G, Cui J. BK channels: Multiple sensors, one activation gate. Front
Physiol. 2015;6(FEB):29. doi:10.3389/fphys.2015.00029
89.  Latorre R, Castillo K, Carrasquel -Ursulaez W, et al. Molecular determinants of BK
channel functional diversity and functioning. Physiol Rev . 2017;97(1):39 -87.
doi:10.1152/physrev.00001.2016
90.  Lee US, Cui J. BK channel  activation: structural and functional insights. Trends
Neurosci. 2010;33(9):415-423. doi:10.1016/J.TINS.2010.06.004
91.  Hoshi T, Pantazis A, Olcese R. Transduction of voltage and Ca2+ signals by Slo1 BK
channels. Physiology. 2013;28(3):172-189. doi:10.1152/physiol.00055.2012
92.  Gonzalez-Perez V, Lingle CJ. Regulation of BK Channels by Beta and Gamma Subunits.
Annu Rev Physiol. 2019;81:113. doi:10.1146/ANNUREV-PHYSIOL-022516-034038
93.  Hu S, Han R, Chen L, et al. Upregulated LRRC55 promotes BK channel a ctivation and
aggravates cell injury in podocytes. J Exp Med . 2021;218(2).
doi:10.1084/JEM.20192373/211626
94.  Yan J, Aldrich RW. BK potassium channel modulation by leucine-rich repeat-containing
proteins. Proc Natl Acad Sci U S A . 2012;109(20):7917 -7922.
doi:10.1073/pnas.1205435109
95.  Szewczyk A, Kajma A, Malinska D, et al. Pharmacology of mitochondrial potassium
channels: dark side of the field. FEBS Lett . 2010;584(10):2063 -2069.
doi:10.1016/J.FEBSLET.2010.02.048
96.  Augustynek B, Kunz WS, Szewczyk A.  Guide to the Pharmacology of Mitochondrial
Potassium Channels. Handb Exp Pharmacol . 2016;240:103 -127.
doi:10.1007/164_2016_79
97.  Aon MA, Cortassa S, Wei AC, Grunnet M, O’Rourke B. Energetic performance is
improved by specific activation of K+ fluxes thr ough K(Ca) channels in heart
mitochondria. Biochim Biophys Acta . 2010;1797(1):71 -80.
doi:10.1016/J.BBABIO.2009.08.002


152

98.  Hirusaki K, Yokoyama K, Cho K, Ohta Y. Temporal depolarization of mitochondria
during M phase. Sci Rep. 2017;7(1). doi:10.1038/S41598-017-15907-3
99.  Kulawiak B, Kudin AP, Szewczyk A, Kunz WS. BK channel openers inhibit ROS
production of isolated rat brain mitochondria. Exp Neurol . 2008;212(2):543 -547.
doi:10.1016/j.expneurol.2008.05.004
100.  Goswami S, Ponnalagu D, Hussain A, et al. Expression and activation of BKCa channels
in mice protects against ischemia -reperfusion injury of isolated hearts by modulating
mitochondrial function. Front Cardiovasc Med . 2019;5:194.
doi:10.3389/fcvm.2018.00194
101.  Balderas E, Torres NS, Rosa -Garrido M, et al. MitoBK Ca channel is functionally
associated with its regulatory β1 subunit in cardiac mitochondria. J Physiol .
2019;597(15):3817-3832. doi:10.1113/JP277769
102.  Vygodina T, Kirichenko A, Konstantinov AA. Direct Regulation of Cytochrome c
Oxidase by Calcium Ions. PLoS One . 2013;8(9):e74436.
doi:10.1371/JOURNAL.PONE.0074436
103.  Brookes PS, Yoon Y, Robotham JL, Anders MW, Sheu SS. Calcium, ATP, and ROS: a
mitochondrial love -hate triangle. Am J Physiol Cell Physiol . 2004;287(4).
doi:10.1152/AJPCELL.00139.2004
104.  Bednarczyk P, Wieckowski MR, Broszkiewicz M, Skowronek K, Siemen D, Szewczyk
A. Putative Structural and Functional Coupling of the Mitochondrial BKCa Channel to
the Respiratory Chain. PLoS One. 2013;8(6). doi:10.1371/journal.pone.0068125
105.  Ohya S, Kuwata Y, Sakamoto K, Muraki K, Imaizumi Y. Cardioprotective effects of
estradiol include the activation of large -conductance Ca2+ -activated K+ channels in
cardiac mitochondria. Am J Physiol - Hear Circ Physiol. 2005;289(4 58-4):1635-1642.
doi:10.1152/ajpheart.00016.2005
106.  Singh H, Li M, Hall L, et al. MaxiK channel interactome reveals its interaction with
GABA transporter 3 and heat shock protein 60 in the mammalian brain. Neuroscience.
2016;317:76-107. doi:10.1016/j.neuroscience.2015.12.058
107.  Da Cunha FM, Torelli NQ, Kowaltowski AJ. Mitochondrial Retrograde Signaling:
Triggers, Pathways, and Outcomes. Oxid Med Cell Longev . 2015;2015.
doi:10.1155/2015/482582


153

108.  Pfannschmidt T, Terry MJ, Van Aken O, Quiros PM. Retrograde signals fr om
endosymbiotic organelles: a common control principle in eukaryotic cells. Philos Trans
R Soc B. 2020;375(1801). doi:10.1098/RSTB.2019.0396
109.  Pellegrino MW, Nargund AM, Haynes CM. Signaling the mitochondrial unfolded
protein response. Biochim Biophys  Acta - Mol Cell Res . 2013;1833(2):410 -416.
doi:10.1016/j.bbamcr.2012.02.019
110.  Vögtle FN. Open questions on the mitochondrial unfolded protein response. FEBS J.
2021;288(9):2856-2869. doi:10.1111/FEBS.15569
111.  Anderson NS, Haynes CM. Folding the Mit ochondrial UPR into the Integrated Stress
Response. Trends Cell Biol. 2020;30(6):428-439. doi:10.1016/j.tcb.2020.03.001
112.  Quirós PM, Mottis A, Auwerx J. Mitonuclear communication in homeostasis and stress.
Nat Rev Mol Cell Biol. 2016;17(4):213-226. doi:10.1038/nrm.2016.23
113.  Taniuchi S, Miyake M, Tsugawa K, Oyadomari M, Oyadomari S. Integrated stress
response of vertebrates is regulated by four eIF2 α kinases. Sci Rep . 2016;6.
doi:10.1038/srep32886
114.  Guo X, Aviles G, Liu Y, et al. Mitochondrial st ress is relayed to the cytosol by an
OMA1–DELE1–HRI pathway. Nature. 2020;579(7799):427-432. doi:10.1038/s41586-
020-2078-2
115.  Haynes CM, Ron D. The mitochondrial UPR - Protecting organelle protein homeostasis.
J Cell Sci. 2010;123(22):3849-3855. doi:10.1242/jcs.075119
116.  Michel S, Canonne M, Arnould T, Renard P. Inhibition of mitochondrial genome
expression triggers the activation of CHOP -10 by a cell signaling dependent on the
integrated stress response but not the mitochondrial unfolded protein resp onse.
Mitochondrion. 2015;21:58-68. doi:10.1016/j.mito.2015.01.005
117.  Qureshi MA, Haynes CM, Pellegrino MW. The mitochondrial unfolded protein
response: Signaling from the powerhouse. J Biol Chem . 2017;292(33):13500 -13506.
doi:10.1074/jbc.R117.791061
118.  Wang G, Fan Y, Cao P, Tan K. Insight into the mitochondrial unfolded protein response
and cancer: opportunities and challenges. Cell Biosci . 2022;12(1):1 -23.
doi:10.1186/s13578-022-00747-0


154

119.  Fiorese CJ, Schulz AM, Lin YF, Rosin N, Pellegrino MW, Ha ynes CM. The
Transcription Factor ATF5 Mediates a Mammalian Mitochondrial UPR. Curr Biol .
2016;26(15):2037-2043. doi:10.1016/j.cub.2016.06.002
120.  Quirós PM, Langer T, López -Otín C. New roles for mitochondrial proteases in health,
ageing and disease. Nat Rev Mol Cell Biol. 2015;16(6):345-359. doi:10.1038/nrm3984
121.  Pellegrino MW, Nargund AM, Haynes CM. Signaling the mitochondrial unfolded
protein response. Biochim Biophys Acta - Mol Cell Res . 2013;1833(2):410 -416.
doi:10.1016/j.bbamcr.2012.02.019
122.  Wodrich APK, Scott AW, Shukla AK, Harris BT, Giniger E. The Unfolded Protein
Responses in Health, Aging, and Neurodegeneration: Recent Advances and Future
Considerations. Front Mol Neurosci. 2022;15:37. doi:10.3389/fnmol.2022.831116
123.  Chen Y, Dorn GW.  PINK1-phosphorylated mitofusin 2 is a parkin receptor for culling
damaged mitochondria. Science (80 - ). 2013;340(6131):471 -475.
doi:10.1126/science.1231031
124.  Walewska A, Szewczyk A, Krajewska M, Koprowski P. Targeting Mitochondrial Large-
Conductance Calcium-Activated Potassium Channel by Hydrogen Sulfide via Heme -
Binding Site. J Pharmacol Exp Ther . 2022;381(2):137 -150.
doi:10.1124/JPET.121.001017
125.  Frankenreiter S, Bednarczyk P, Kniess A, et al. cGMP -Elevating Compounds and
Ischemic Conditioning Pr ovide Cardioprotection Against Ischemia and Reperfusion
Injury via Cardiomyocyte-Specific BK Channels. Circulation. 2017;136(24):2337-2355.
doi:10.1161/CIRCULATIONAHA.117.028723
126.  Kampa RP, Kicinska A, Jarmuszkiewicz W, et al. Naringenin as an opener o f
mitochondrial potassium channels in dermal fibroblasts. Exp Dermatol. 2019;28(5):543-
550. doi:10.1111/exd.13903
127.  Tang XD, Xu R, Reynolds MF, Garcia ML, Heinemann SH, Hoshi T. Haem can bind to
and inhibit mammalian calcium -dependent Slo1 BK channels.  Nature.
2003;425(6957):531-535. doi:10.1038/nature02003
128.  Horrigan FT, Heinemann SH, Hoshi T. Heme regulates allosteric activation of the Slo1
BK channel. J Gen Physiol. 2005;126(1):7-21. doi:10.1085/jgp.200509262


155

129.  Augustynek B, Kudin AP, Bednarc zyk P, Szewczyk A, Kunz WS. Hemin inhibits the
large conductance potassium channel in brain mitochondria: a putative novel mechanism
of neurodegeneration. Exp Neurol . 2014;257:70 -75.
doi:10.1016/J.EXPNEUROL.2014.04.022
130.  Ryter SW, Alam J, Choi AMK. Hem e oxygenase -1/carbon monoxide: From basic
science to therapeutic applications. Physiol Rev . 2006;86(2):583 -650.
doi:10.1152/physrev.00011.2005
131.  Piantadosi CA, Carraway MS, Babiker A, Suliman HB. Heme oxygenase -1 regulates
cardiac mitochondrial biogene sis via Nrf2 -mediated transcriptional control of nuclear
respiratory factor -1. Circ Res . 2008;103(11):1232 -1240.
doi:10.1161/01.RES.0000338597.71702.AD
132.  Motterlini R, Otterbein LE. The therapeutic potential of carbon monoxide. Nat Rev Drug
Discov. 2010;9(9):728-743. doi:10.1038/NRD3228
133.  Ryter SW, Otterbein LE. Carbon monoxide in biology and medicine. BioEssays.
2004;26(3):270-280. doi:10.1002/bies.20005
134.  García-Gallego S, Bernardes GJL. Carbon -monoxide-releasing molecules for the
delivery of therapeutic co in vivo. Angew Chemie - Int Ed . 2014;53(37):9712 -9721.
doi:10.1002/anie.201311225
135.  Zobi F. CO and CO -releasing molecules in medicinal chemistry. Future Med Chem .
2013;5(2):175-188. doi:10.4155/fmc.12.196
136.  Kautz AC, Kunz PC, Janiak C. CO-releasing molecule (CORM) conjugate systems. Dalt
Trans. 2016;45(45):18045-18063. doi:10.1039/C6DT03515A
137.  Kaczara P, Motterlini R, Rosen GM, et al. Biochimica et Biophysica Acta Carbon
monoxide released by CORM -401 uncouples mitochondrial respir ation and inhibits
glycolysis in endothelial cells : A role for mitoBK Ca channels. BBA - Bioenerg.
2015;1847(10):1297-1309. doi:10.1016/j.bbabio.2015.07.004
138.  Decaluwé K, Pauwels B, Verpoest S, Van De Voorde J. Divergent mechanisms involved
in CO and CORM-2 induced vasorelaxation. Eur J Pharmacol. 2012;674(2-3):370-377.
doi:10.1016/J.EJPHAR.2011.11.004
139.  Gessner G, Sahoo N, Swain SM, et al. CO-independent modification of K+ channels by


156

tricarbonyldichlororuthenium(II) dimer (CORM -2). Eur J Pharmaco l. 2017;815:33.
doi:10.1016/J.EJPHAR.2017.10.006
140.  Dong DL, Chen C, Huang W, et al. Tricarbonyldichlororuthenium (II) dimer (CORM2)
activates non-selective cation current in human endothelial cells independently of carbon
monoxide releasing. Eur J Phar macol. 2008;590(1 -3):99-104.
doi:10.1016/J.EJPHAR.2008.05.042
141.  Almeida AS, Figueiredo -Pereira C, Vieira HLA. Carbon monoxide and mitochondria -
modulation of cell metabolism, redox response and cell death. Front Physiol .
2015;6(FEB):1-6. doi:10.3389/fphys.2015.00033
142.  Calvo-Rodríguez M, García-Durillo M, Villalobos C, Núñez L. In vitro aging promotes
endoplasmic reticulum (ER) -mitochondria Ca2 + cross talk and loss of store -operated
Ca2 + entry (SOCE) in rat hippocampal neurons. Biochim Biophys Acta - Mol Cell Res.
2016;1863(11):2637-2649. doi:10.1016/j.bbamcr.2016.08.001
143.  Bereiter-Hahn J. Mitochondrial dynamics in aging and disease. In: Progress in
Molecular Biology and Translational Science . Vol 127. Elsevier B.V.; 2014:93 -131.
doi:10.1016/B978-0-12-394625-6.00004-0
144.  Trombetta-Lima M, Krabbendam IE, Dolga AM. Calcium-activated potassium channels:
implications for aging and age -related neurodegeneration. Int J Biochem Cell Biol .
2020;123:105748. doi:10.1016/j.biocel.2020.105748
145.  Soltysinska E, Bentzen BH, Barthmes M, et al. KCNMA1 Encoded Cardiac BK
Channels Afford Protection against Ischemia -Reperfusion Injury. PLoS One .
2014;9(7):e103402. doi:10.1371/JOURNAL.PONE.0103402
146.  Kravenska Y, Nieznanska H, Nieznanski K, Lukyanetz E, Szewc zyk A, Koprowski P.
The monomers, oligomers, and fibrils of amyloid -β inhibit the activity of mitoBK Ca
channels by a membrane -mediated mechanism. Biochim Biophys acta Biomembr .
2020;1862(9). doi:10.1016/J.BBAMEM.2020.183337
147.  Cheng Y, Gu XQ, Bednarczy k P, Wiedemann FR, Haddad GG, Siemen D. Hypoxia
increases activity of the BK -channel in the inner mitochondrial membrane and reduces
activity of the permeability transition pore. Cell Physiol Biochem . 2008;22(1 -4):127-
136. doi:10.1159/000149790
148.  Typlt M, Mirkowski M, Azzopardi E, Ruettiger L, Ruth P, Schmid S. Mice with


157

Deficient BK Channel Function Show Impaired Prepulse Inhibition and Spatial
Learning, but Normal Working and Spatial Reference Memory. Ceña V, ed. PLoS One.
2013;8(11):e81270. doi:10.1371/journal.pone.0081270
149.  Wang J, Yu S, Zhang Q, Chen Y, Bao X, Wu X. KCNMA1 mutation in children with
paroxysmal dyskinesia and epilepsy: Case report and literature review. Transl Sci Rare
Dis. 2017;2(3-4):165-173. doi:10.3233/trd-170018
150.  Gururaja Rao S, Bednarczyk P, Towheed A, et al. BKCa (Slo) Channel Regulates
Mitochondrial Function and Lifespan in Drosophila melanogaster. Cells. 2019;8(9):945.
doi:10.3390/cells8090945
151.  Frankenreiter S, Bednarczyk P, Kniess A, et al. cGMP -Elevating Compou nds and
Ischemic Conditioning Provide Cardioprotection Against Ischemia and Reperfusion
Injury via Cardiomyocyte-Specific BK Channels. Circulation. 2017;136(24):2337-2355.
doi:10.1161/CIRCULATIONAHA.117.028723
152.  Hallmann K, Kudin AP, Zsurka G, et al. L oss of the smallest subunit of cytochrome c
oxidase, COX8A, causes Leigh -like syndrome and epilepsy. Brain. 2016;139(2):338-
345. doi:10.1093/brain/awv357
153.  Martin JL, Brown CE, Matthews -Davis N, Reardon JE. Effects of antiviral nucleoside
analogs on hu man DNA polymerases and mitochondrial DNA synthesis. Antimicrob
Agents Chemother. 1994;38(12):2743-2749. doi:10.1128/AAC.38.12.2743
154.  Ran FA, Hsu PD, Wright J, Agarwala V, Scott DA, Zhang F. Genome engineering using
the CRISPR -Cas9 system. Nat Protoc . 2013;8(11):2281-2308.
doi:10.1038/nprot.2013.143
155.  Augustynek B, Kudin AP, Bednarczyk P, Szewczyk A, Kunz WS. Hemin inhibits the
large conductance potassium channel in brain mitochondria: A putative novel
mechanism of neurodegeneration. Exp Neurol . 201 4;257:70-75.
doi:10.1016/j.expneurol.2014.04.022
156.  Gessner G, Sahoo N, Swain SM, et al. CO-independent modification of K + channels by
tricarbonyldichlororuthenium(II) dimer (CORM -2). Eur J Pharmacol .
2017;815(September):33-41. doi:10.1016/j.ejphar.2017.10.006
157.  Jaggar JH, Li A, Parfenova H, et al. Heme is a carbon monoxide receptor for large -
conductance Ca2+ -activated K+ channels. Circ Res . 2005;97(8):805 -812.


158

doi:10.1161/01.RES.0000186180.47148.7B
158.  Wiedemann FR, Vielhaber S, Schröder R, Elger CE, Kunz WS. Evaluation of methods
for the determination of mitochondrial respiratory chain enzyme activities in human
skeletal muscle samples. Anal Biochem . 2000;279(1):55 -60.
doi:10.1006/abio.1999.4434
159.  Bednarczyk P, Kicinska A, Laskowski M, et al. Evidence for a mitochondrial ATP -
regulated potassium channel in human dermal fibroblasts. Biochim Biophys acta
Bioenerg. 2018;1859(5):309-318. doi:10.1016/J.BBABIO.2018.02.005
160.  Kim J, Han J, Jang Y, e t al. High -capacity glycolytic and mitochondrial oxidative
metabolisms mediate the growth ability of glioblastoma. Int J Oncol. 2015;47(3):1009-
1016. doi:10.3892/ijo.2015.3101
161.  Martin JL, Brown CE, Matthews -Davis N, Reardon JE. Effects of antiviral nu cleoside
analogs on human DNA polymerases and mitochondrial DNA synthesis. Antimicrob
Agents Chemother. 1994;38(12):2743-2749. doi:10.1128/AAC.38.12.2743
162.  Dillies MA, Rau A, Aubert J, et al. A comprehensive evaluation of normalization
methods for Illumina high-throughput RNA sequencing data analysis. Brief Bioinform.
2013;14(6):671-683. doi:10.1093/bib/bbs046
163.  Lin Y, Golovnina K, Chen ZX, et al. Comparison of normalization and differential
expression analyses using RNA-Seq data from 726 individual Drosophila melanogaster.
BMC Genomics. 2016;17(1):28. doi:10.1186/s12864-015-2353-z
164.  Jovaisaite V, Mouchiroud L, Auwerx J. The mitochondrial unfolded protein response, a
conserved stress response pathway with implications in health and disease. J Exp Biol.
2014;217(1):137-143. doi:10.1242/jeb.090738
165.  Tonelli C, Chio IIC, Tuveson DA. Transcriptional Regulation by Nrf2. Antioxidants
Redox Signal. 2018;29(17):1727-1745. doi:10.1089/ars.2017.7342
166.  Ward JM, Stoyas CA, Switonski PM, et al. Metabol ic and Organelle Morphology
Defects in Mice and Human Patients Define Spinocerebellar Ataxia Type 7 as a
Mitochondrial Disease. Cell Rep . 2019;26(5):1189 -1202.e6.
doi:10.1016/j.celrep.2019.01.028
167.  Stoyas CA, Bushart DD, Switonski PM, et al. Nicotinami de Pathway-Dependent Sirt1


159

Activation Restores Calcium Homeostasis to Achieve Neuroprotection in
Spinocerebellar Ataxia Type 7. Neuron. 2020;105(4):630 -644.e9.
doi:10.1016/j.neuron.2019.11.019
168.  Goldberg A, Wildman DE, Schmidt TR, et al. Adaptive evolu tion of cytochrome c
oxidase subunit VIII in anthropoid primates. Proc Natl Acad Sci U S A .
2003;100(10):5873-5878. doi:10.1073/pnas.0931463100
169.  Shimizu T, Huang D, Yan F, et al. Gaseous O2, NO, and CO in signal transduction:
structure and function relationships of heme-based gas sensors and heme-redox sensors.
Chem Rev. 2015;115(13):6491-6533. doi:10.1021/acs.chemrev.5b00018
170.  Cha MY, Kim DK y., Mook -Jung I. The role of mitochondrial DNA mutation on
neurodegenerative diseases. Exp Mol Med 2015 473 . 2015;47(3):e150 -e150.
doi:10.1038/emm.2014.122
171.  Chow J, Rahman J, Achermann JC, Dattani MT, Rahman S. Mitochondrial disease and
endocrine dysfunction. Nat Rev Endocrinol . 2017;13(2):92 -104.
doi:10.1038/NRENDO.2016.151
172.  Wallace DC. Mitochondria and cancer. Nat Rev Cancer . 2012;12(10):685 -698.
doi:10.1038/nrc3365
173.  Kirkwood TBL, Korolchuk VI, Szczepanowska K, Trifunovic A. Origins of mtDNA
mutations in ageing. Essays Biochem. 2017;61(3):325-337. doi:10.1042/EBC20160090
174.  Spadafora D, Kozhu khar N, Chouljenko VN, Kousoulas KG, Alexeyev MF. Methods
for Efficient Elimination of Mitochondrial DNA from Cultured Cells. PLoS One .
2016;11(5):e0154684. doi:10.1371/JOURNAL.PONE.0154684
175.  Kukat A, Kukat C, Brocher J, et al. Generation of ρ 0 cells utilizing a mitochondrially
targeted restriction endonuclease and comparative analyses. Nucleic Acids Res .
2008;36(7):e44-e44. doi:10.1093/NAR/GKN124
176.  Rahman S, Copeland WC. POLG -related disorders and their neurological
manifestations. Nat Rev Neurol. 2019;15(1):40. doi:10.1038/S41582-018-0101-0
177.  Lewis W, Copeland WC, Day BJ. Mitochondrial DNA depletion, oxidative stress, and
mutation: Mechanisms of dysfunction from nucleoside rever se transcriptase inhibitors.
Lab Investig. 2001;81(6):777-790. doi:10.1038/labinvest.3780288


160

178.  Chen CH, Cheng YC. The role of cytoplasmic deoxycytidine kinase in the mitochondrial
effects of the antihuman immunodeficiency virus compound, 2’,3’ -dideoxycytidine. J
Biol Chem. 1992;267(5):2856-2859. doi:10.1016/s0021-9258(19)50661-5
179.  Khan NA, Nikkanen J, Yatsuga S, et al. mTORC1 Regulates Mitochondrial Integrated
Stress Response and Mitochondrial Myopathy Progression. Cell Metab. 2017;26(2):419-
428.e5. doi:10.1016/j.cmet.2017.07.007
180.  Forsström S, Jackson CB, Carroll CJ, et al. Fibroblast Growth Factor 21 Drives
Dynamics of Local and Systemic Stress Responses in Mitochondrial Myopathy with
mtDNA Deletions. Cell Metab . 2019;30(6):1040 -1054.e7.
doi:10.1016/j.cmet.2019.08.019
181.  Lehtonen JM, Forsström S, Bottani E, et al. FGF21 is a biomarker for mitochondrial
translation and mtDNA maintenance disorders. Neurology. 2016;87(22):2290.
doi:10.1212/WNL.0000000000003374
182.  Mick E, Titov D V., Skinner O S, Sharma R, Jourdain AA, Mootha VK. Distinct
mitochondrial defects trigger the integrated stress response depending on the metabolic
state of the cell. Elife. 2020;9. doi:10.7554/ELIFE.49178
183.  Wang P, Deng J, Dong J, et al. TDP-43 Induces Mitochondrial Damage and Activates
the Mitochondrial Unfolded Protein Response . Vol 15.; 2019.
doi:10.1371/journal.pgen.1007947
184.  Srivastava S. Emerging therapeutic roles for NAD+ metabolism in mitochondrial and
age-related disorders. Clin Transl Med. 2016;5(1). doi:10.1186/S40169-016-0104-7
185.  Sun X, Qian LL, Li Y, et al. Regulation of KCNMA1 Transcription by Nrf2 in Coronary
Arterial Smooth Muscle Cells. J Mol Cell Cardiol . 2020;140:68.
doi:10.1016/J.YJMCC.2020.03.001
186.  Vivian CJ, Brinker AE, Graw S, et al . Mitochondrial Genomic Backgrounds Affect
Nuclear DNA Methylation and Gene Expression. Cancer Res. 2017;77(22):6202-6214.
doi:10.1158/0008-5472.CAN-17-1473
187.  Sutendra G, Kinnaird A, Dromparis P, et al. A nuclear pyruvate dehydrogenase complex
is impor tant for the generation of acetyl -CoA and histone acetylation. Cell.
2014;158(1):84-97. doi:10.1016/J.CELL.2014.04.046


161

188.  Basile MS, Fagone P, Mangano K, et al. KCNMA1 Expression Is Downregulated in
Colorectal Cancer via Epigenetic Mechanisms. Cancers 2 019, Vol 11, Page 245 .
2019;11(2):245. doi:10.3390/CANCERS11020245
189.  Cheng YY, Wright CM, Kirschner MB, et al. KCa1.1, a calcium -activated potassium
channel subunit alpha 1, is targeted by miR -17-5p and modulates cell migration in
malignant pleural mes othelioma. Mol Cancer . 2016;15(1). doi:10.1186/S12943 -016-
0529-Z
190.  Samuel P, Pink RC, Caley DP, Currie JMS, Brooks SA, Carter DRF. Over -expression
of miR-31 or loss of KCNMA1 leads to increased cisplatin resistance in ovarian cancer
cells. Tumour Biol. 2016;37(2):2565-2573. doi:10.1007/S13277-015-4081-Z
191.  Mazar J, de Young K, Khaitan D, et al. The regulation of miRNA-211 expression and its
role in melanoma cell invasiveness. PLoS One . 2010;5(11).
doi:10.1371/JOURNAL.PONE.0013779
192.  Muir R, Diot A, Poulton J. Mitochondrial content is central to nuclear gene expression:
Profound implications for human health. BioEssays. 2016;38(2):150 -156.
doi:10.1002/BIES.201500105
193.  Veatch JR, McMurray MA, Nelson ZW, Gottschling DE. Mitochondrial dysfunction
leads to nuclear genome instability via an iron -sulfur cluster defect. Cell.
2009;137(7):1247-1258. doi:10.1016/J.CELL.2009.04.014
194.  Pacheco Otalora LF, Hernandez EF, Arshadmansab MF, et al. Down -regulation of BK
channel expression in the pilocarpine mo del of temporal lobe epilepsy. Brain Res .
2008;1200:116-131. doi:10.1016/J.BRAINRES.2008.01.017
195.  Lu T, Zhang DM, Wang XL, et al. Regulation of coronary arterial bk channels by
caveolae-mediated angiotensin II signaling in diabetes mellitus. Circ Res .
2010;106(6):1164-1173. doi:10.1161/CIRCRESAHA.109.209767
196.  Zhang DM, He T, Katusic ZS, Lee HC, Lu T. Muscle -specific f -box only proteins
facilitate bk channel β(1) subunit downregulation in vascular smooth muscle cells of
diabetes mellitus. Circ Res . 2 010;107(12):1454-1459.
doi:10.1161/CIRCRESAHA.110.228361
197.  Ning F ling, Tao J, Li D dan, et al. Activating BK channels ameliorates vascular smooth
muscle calcification through Akt signaling. Acta Pharmacol Sin . 2022;43(3):624-633.


162

doi:10.1038/s41401-021-00704-6
198.  Chen SR, Cai YQ, Pan HL. Plasticity and emerging role of BKCa channels in nociceptive
control in neuropathic pain. J Neurochem . 2009;110(1):352 -362. doi:10.1111/J.1471 -
4159.2009.06138.X
199.  Cheng KI, Yang KT, Kung CL, et al. BKCa Channel Inhibition by Peripheral Nerve
Injury Is Restored by the Xanthine Derivative KMUP -1 in Dorsal Root Ganglia. Cells
2021, Vol 10, Page 949. 2021;10(4):949. doi:10.3390/CELLS10040949
200.  Cao XH, Chen SR, Li L, Pan HL. Nerve injury increases brain -derived ne urotrophic
factor levels to suppress BK channel activity in primary sensory neurons. J Neurochem.
2012;121(6):944-953. doi:10.1111/J.1471-4159.2012.07736.X
201.  Yang D, Kim J. Mitochondrial Retrograde Signalling and Metabolic Alterations in the
Tumour Microenvironment. Cells. 2019;8(3):275. doi:10.3390/CELLS8030275
202.  Bloch M, Ousingsawat J, Simon R, et al. KCNMA1 gene amplification promotes tumor
cell proliferation in human prostate cancer. Oncogene. 2007;26(17):2525 -2534.
doi:10.1038/SJ.ONC.1210036
203.  Oeggerli M, Tian Y, Ruiz C, et al. Role of KCNMA1 in Breast Cancer. PLoS One .
2012;7(8):e41664. doi:10.1371/JOURNAL.PONE.0041664
204.  Ramírez A, Vera E, Gamboa -Domínguez A, Lambert P, Gariglio P, Camacho J.
Calcium-activated potassium channels as pote ntial early markers of human cervical
cancer. Oncol Lett. 2018;15(5):7249-7254. doi:10.3892/OL.2018.8187/HTML
205.  Lobo‐Jarne T, Pérez‐Pérez R, Fontanesi F, et al. Multiple pathways coordinate assembly
of human mitochondrial complex IV and stabilization o f respiratory supercomplexes.
EMBO J. 2020;39(14). doi:10.15252/embj.2019103912
206.  Kovářová N, Čížková Vrbacká A, Pecina P, et al. Adaptation of respiratory chain
biogenesis to cytochrome c oxidase deficiency caused by SURF1 gene mutations.
Biochim Biop hys Acta - Mol Basis Dis . 2012;1822(7):1114 -1124.
doi:10.1016/j.bbadis.2012.03.007
207.  Baertling F, A.M. van den Brand M, Hertecant JL, et al. Mutations in COA6 cause
cytochrome c oxidase deficiency and neonatal hypertrophic cardiomyopathy. Hum
Mutat. 2015;36(1):34-38. doi:10.1002/humu.22715


163

208.  Baertling F, Al -Murshedi F, Sánchez -Caballero L, et al. Mutation in mitochondrial
complex IV subunit COX5A causes pulmonary arterial hypertension, lactic acidemia,
and failure to thrive. Hum Mutat. 2017;38(6):692-703. doi:10.1002/humu.23210
209.  Schäfer E, Seelert H, Reifschneider NH, Krause F, Dencher NA, Vonck J. Architecture
of active mammalian respiratory chain supercomplexes. J Biol Chem .
2006;281(22):15370-15375. doi:10.1074/JBC.M513525200
210.  Fessler E,  Eckl EM, Schmitt S, et al. A pathway coordinated by DELE1 relays
mitochondrial stress to the cytosol. Nature. 2020;579(7799):433 -437.
doi:10.1038/s41586-020-2076-4
211.  Palam LR, Baird TD, Wek RC. Phosphorylation of eIF2 facilitates ribosomal bypass of
an inhibitory upstream ORF to enhance CHOP translation. J Biol Chem .
2011;286(13):10939-10949. doi:10.1074/jbc.M110.216093
212.  Strauss M, Hofhaus G, Schröder RR, Kühlbrandt W. Dimer ribbons of ATP synthase
shape the inner mitochondrial membrane. EMBO J . 2 008;27(7):1154-1160.
doi:10.1038/EMBOJ.2008.35
213.  Wiedemann N, Van Der Laan M, Hutu DP, Rehling P, Pfanner N. Sorting switch of
mitochondrial presequence translocase involves coupling of motor module to respiratory
chain. J Cell Biol. 2007;179(6):1115-1122. doi:10.1083/JCB.200709087
214.  Pfanner N, Warscheid B, Wiedemann N. Mitochondrial proteins: from biogenesis to
functional networks. Nat Rev Mol Cell Biol . 2019;20(5):267-284. doi:10.1038/s41580-
018-0092-0
215.  Hashimoto T, Hussien R, Cho HS, Kaufer D, Brooks GA. Evidence for the mitochondrial
lactate oxidation complex in rat neurons: Demonstration of an essential component of
brain lactate shuttles. PLoS One. 2008;3(8). doi:10.1371/journal.pone.0002915
216.  Du X, Carvalho -De-Souza JL, Wei C, et al. Loss-of-function BK channel mutation
causes impaired mitochondria and progressive cerebellar ataxia. Proc Natl Acad Sci U S
A. 2020;117(11):6023-6034. doi:10.1073/pnas.1920008117
217.  Hou S, Xu R, Heinemann SH, Hoshi T. The RCK1 high -affinity Ca2+ sensor confers
carbon monoxide sensitivity to Slo1 BK channels. Proc Natl Acad Sci U S A .
2008;105(10):4039-4043. doi:10.1073/pnas.0800304105


164

218.  Williams SE, Brazier SP, Baban N, et al. A structural motif in the C-terminal tail of slo1
confers carbon monoxide sensitivity to human BKCa channels. Pflugers Arch Eur J
Physiol. 2008;456(3):561-572. doi:10.1007/s00424-007-0439-4
219.  Wilson JL, Wareham LK, McLean S, et al. CO -Releasing Molecules Have Nonheme
Targets in Bacteria: Transcriptomic, Mathematical Modeling and Biochemical Analyses
of CORM -3 [Ru(CO)3Cl(glycinate)] Actions on a Heme -Deficient Mutant of
Escherichia coli. Antioxidants Redox Signal . 2015;23(2):148 -162.
doi:10.1089/ars.2014.6151
220.  Ling K, Men F, Wang WC, Zhou YQ, Zhang HW, Ye DW. Carbon Monox ide and Its
Controlled Release: Therapeutic Application, Detection, and Development of Carbon
Monoxide Releasing Molecules (CORMs). J Med Chem . 2018;61(7):2611 -2635.
doi:10.1021/ACS.JMEDCHEM.6B01153
221.  Mann BE. CO -releasing molecules: A personal view. Organometallics.
2012;31(16):5728-5735. doi:10.1021/OM300364A/
222.  Dallas ML, Boyle JP, Milligan CJ, et al. Carbon monoxide protects against oxidant -
induced apoptosis via inhibition of Kv2.1. FASEB J . 2011;25(5):1519 -1530.
doi:10.1096/FJ.10-173450
223.  Crook SH, Mann BE, Meijer AJHM, et al. [Mn(CO)4{S2CNMe(CH2CO2H)}], a new
water-soluble CO -releasing molecule. Dalt Trans . 2011;40(16):4230 -4235.
doi:10.1039/c1dt10125k
224.  Motterlini R, Foresti R. Biological signaling by carbon monoxide and carbon monoxide-
releasing molecules. Am J Physiol - Cell Physiol . 2017;312(3):C302 -C313.
doi:10.1152/ajpcell.00360.2016
225.  Hayashi Y, Morinaga S, Zhang J, et al. BK channels in microglia are required for
morphine-induced hyperalgesia. Nat Commun. 2016;7. doi:10.1038/NCOMMS11697
226.  Babu D, Leclercq G, Goossens V, et al. Antioxidant potential of CORM -A1 and
resveratrol during TNF -α/cycloheximide-induced oxidative stress and apoptosis in
murine intestinal epithelial MODE-K cells. Toxicol Appl Pharmacol. 2015;288(2):161-
178. doi:10.1016/J.TAAP.2015.07.007
227.  Babu D, Leclercq G, Motterlini R, Lefebvre RA. Differential effects of CORM -2 and
CORM-401 in murine intestinal epithelial MODE -K cells under oxidative stress. Front


165

Pharmacol. 2017;8(FEB):1-17. doi:10.3389/fphar.2017.00031
228.  Gallio AE, Fung SS-P, Cammack-Najera A, Hudson AJ, Raven EL. Understanding the
Logistics for the Distribution of Heme in Cells. JACS Au . 2021;1(10):1541 -1555.
doi:10.1021/JACSAU.1C00288
229.  Mavridou DAI, Ferguson SJ, Stevens JM. Cytochr ome c assembly. IUBMB Life .
2013;65(3):209-216. doi:10.1002/IUB.1123
230.  Kapetanaki SM, Burton MJ, Basran J, et al. A mechanism for CO regulation of ion
channels. Nat Commun. 2018;9(1). doi:10.1038/s41467-018-03291-z
231.  Yi L, Morgan JT, Ragsdale SW. I dentification of a thiol/disulfide redox switch in the
human BK channel that controls its affinity for heme and CO. J Biol Chem .
2010;285(26):20117-20127. doi:10.1074/jbc.M110.116483
232.  Gozzelino R, Jeney V, Soares MP. Me chanisms of cell protection by heme oxygenase -
1. Annu Rev Pharmacol Toxicol . 2010;50:323 -354.
doi:10.1146/ANNUREV.PHARMTOX.010909.105600
233.  Williams SEJ, Wootton P, Mason HS, et al. Hemoxygenase-2 is an oxygen sensor for a
calcium-sensitive potassium ch annel. Science. 2004;306(5704):2093 -2097.
doi:10.1126/SCIENCE.1105010
234.  Bindu S, Pal C, Dey S, et al. Translocation of heme oxygenase -1 to mitochondria is a
novel cytoprotective mechanism against non -steroidal anti-inflammatory drug-induced
mitochondrial oxidative stress, apoptosis, and gastric mucosal injury. J Biol Chem .
2011;286(45):39387-39402. doi:10.1074/jbc.M111.279893
235.  Ma X, Sayed N, Beuve A, Van Den Akker F. NO and CO differentially activate soluble
guanylyl cyclase via a heme pivot -bend m echanism. EMBO J . 2007;26(2):578.
doi:10.1038/SJ.EMBOJ.7601521
