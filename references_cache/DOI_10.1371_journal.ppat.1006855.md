---
reference_id: DOI:10.1371/journal.ppat.1006855
title: Decoding the network of Trypanosoma brucei proteins that determines sensitivity to apolipoprotein-L1
authors:
- Rachel B. Currier
- Anneli Cooper
- Hollie Burrell-Saward
- Annette MacLeod
- Sam Alsford
journal: PLOS Pathogens
year: '2018'
doi: 10.1371/journal.ppat.1006855
content_type: full_text_pdf
is_preprint: false
full_text_attempted: true
full_text_provider: openalex
full_text_url: "https://journals.plos.org/plospathogens/article/file?id=10.1371/journal.ppat.1006855&type=printable"
oa_status: gold
license: cc-by
local_pdf_path: files/DOI_10.1371_journal.ppat.1006855.pdf
---

# Decoding the network of Trypanosoma brucei proteins that determines sensitivity to apolipoprotein-L1
**Authors:** Rachel B. Currier, Anneli Cooper, Hollie Burrell-Saward, Annette MacLeod, Sam Alsford
**Journal:** PLOS Pathogens (2018)
**DOI:** [10.1371/journal.ppat.1006855](https://doi.org/10.1371/journal.ppat.1006855)

## Content

RESEA RCH ARTICL E
Decoding the network of Trypanosoma brucei
proteins that determines sensitivity to
apolipoprotein-L1
Rachel B. Currier
1¤
, Anneli Cooper
2
, Hollie Burrell-Saward
1
, Annette MacLeod
2
,
Sam Alsford
1
*
1 London School of Hygiene and Tropical Medicine, London , United Kingdom, 2 Institute of Biodive rsity,
Animal Health and Comp arative Medicine, University of Glasgow, Glasgow, United Kingdom
¤ Current address: Biochemi stry Centre (BZH), Heidelbe rg Univers ity, Im Neuenhei mer Feld 328,
Heidelbe rg, Germany
* sam.als ford@lshtm.ac .uk
Abstract
In contrast to Trypanosoma brucei gambiense and T. b. rhodesiense (the causative agents
of human African trypanosomiasis), T. b. brucei is lysed by apolipoprote in-L1 (apoL1)-con-
taining human serum trypanolytic factors (TLF), rendering it non-infectious to humans.
While the mechanisms of TLF1 uptake, apoL1 membrane integration, and T. b. gambiense
and T. b. rhodesiense apoL1-resistance have been extensively characterise d, our under-
standing of the range of factors that drive apoL1 action in T. b. brucei is limited. Selecting
our bloodstream-form T. b. brucei RNAi library with recombinan t apoL1 identified an array
of factors that supports the trypanocidal action of apoL1, including six putative ubiquitin
modifiers and several proteins putatively involved in membrane trafficking; we also identified
the known apoL1 sensitivity determinants, TbKIFC1 and the V-ATPase. Most prominent
amongst the novel apoL1 sensitivity determinants was a putative ubiquitin ligase. Intrigu-
ingly, while loss of this ubiquitin ligase reduces parasite sensitivity to apoL1, its loss en-
hances parasite sensitivity to TLF1-dominat ed normal human serum, indicating that free
and TLF1-bound apoL1 have contrasting modes-of-action . Indeed, loss of the known
human serum sensitivity determinants, p67 (lysosomal associated membrane protein) and
the cathepsin-L regulator, ‘inhibitor of cysteine peptidase’, had no effect on sensitivity to free
apoL1. Our findings highlight a complex network of proteins that influences apoL1 action,
with implications for our understanding of the anti-trypanoso mal action of human serum.
Author summary
Expression of the trypanolytic serum component, apolipoprotein-L1 (apoL1), by humans
and the concomitant evolution of countermeasures by two African trypanosome sub-spe-
cies defines their ability to cause disease in humans. A genome-scale RNAi screen identi-
fied more than 60 proteins that sensitise non-human infectious trypanosomes to apoL1.
Comparing these outputs to previous screens that used different selection approaches
PLOS Pathogens | https:// doi.org/10.13 71/journal.p pat.1006 855 January 18, 2018 1 / 26
a1111111111
a1111111111
a1111111111
a1111111111
a1111111111
OPEN ACCESS
Citation: Currier RB, Cooper A, Burrell-Sawar d H,
MacLeod A, Alsford S (2018) Decoding the
network of Trypanosom a brucei proteins that
determines sensitivit y to apolipoprotei n-L1. PLoS
Pathog 14(1): e1006855. https://d oi.org/10.1371 /
journal.ppa t.1006855
Editor: Jayne Raper, Hunter College, CUNY,
UNITED STATES
Received: September 12, 2017
Accepted: January 5, 2018
Published: January 18, 2018
Copyright: © 2018 Currier et al. This is an open
access article distributed under the terms of the
Creative Commons Attribution License, which
permits unrestricte d use, distribu tion, and
reproduction in any medium, provided the original
author and source are credited.
Data Availabilit y Statement: All RITseq data
described herein is publicly accessible via the
European Nucleotide Archive, https://www.e bi.ac.
uk/ena (accession numbers: PRJEB23776 ,
PRJEB23779 ).
Funding: RC, HBS and SA were supporte d by a
Medical Research Council (https://www .mrc.ac.uk /
) project grant awarded to SA (MR/K011 987/1;
jointly funded by the UK MRC and the UK
Department for Internationa l Developm ent (DFID)
under the MRC/DF ID Concordat agreement and is

provides insights into the mode-of-action of human serum-mediated killing of trypano-
somes. The effectiveness of apoL1, and the trypanolytic factors (TLF) that carry it, is
dependent on the parasite’s endocytic system for uptake, intracellular transit and delivery
to target membranes. Comparing our current data to the outputs from previous screens
revealed that apoL1 is able to exploit different routes to access its target membranes,
depending on whether it is free or, as in human serum, complexed with TLF1 or TLF2.
Introduction
Trypanosoma brucei ssp. and the related kinetoplastid parasites, T. congolense and T. vivax, are
endemic to sub-Saharan Africa. T. b. gambiense and T. b. rhodesiense cause an estimated
20,000 cases of human African trypanosomiasis (HAT) per year [1], but as recently as the
1990s there were thought to be up to 500,000 cases per year [2]. While the number of reported
cases has dropped significantly in the last decade, approximately 70 million people still live in
parts of sub-Saharan Africa regarded as risk areas for HAT [3]. T. b. brucei, T. congolense and
T. vivax are the causative agents of the cattle wasting disease, nagana, and continue to have a
significant impact on agricultural development in the region [4]. While treatments for HAT
and animal African trypanosomiasis are available, these exhibit significant toxic side effects,
and resistance is becoming an increasing problem in the field [5, 6], making the development
of novel therapeutic approaches and a detailed understanding of the mode-of-action of current
trypanocidals essential [7].
Most African trypanosomes, including T. congolense, T. vivax and T. b. brucei, are sensitive
to lysis by human serum. However, the human-infective sub-species, T. b. gambiense and T. b.
rhodesiense, have evolved distinct means of evading this innate immunity. Human serum con-
tains two trypanolytic complexes, TLF1 and TLF2 [8–11], both of which include the lytic com-
ponent, apolipoprotein-L1 (apoL1). ApoL1 forms pores in the trypanosome endosomal and
other membranes, a process dependent on conformational change driven by decreasing pH
through the parasite’s endosomal-lysosomal system [12–16]. Recent findings suggest that pore
opening and subsequent lysis is dependent on return to a neutral pH environment [17]. T. b.
rhodesiense is able to evade this lytic attack by expressing the serum resistance-associated
(SRA) protein, which binds apoL1 in the endosomal-lysosomal system and prevents pore for-
mation [18, 19]. In contrast, T. b. gambiense resistance to apoL1 is a multifactorial process
involving reduced TLF1 uptake by a variant form of the parasite’s haptoglobin-haemoglob in
receptor (TbHpHbR) [20–22], T. b. gambiense-specific glycoprotein (TgsGP) mediated endo-
somal membrane stiffening, and possibly increased lysosomal cysteine protease activity [23,
24]. SRA and TgsGP are related to the parasite’s variant surface glycoprotein (VSG), which is
responsible for antigenic variation and immune evasion [25]. However, while the SRA
sequence is associated with a specific sub-telomeric VSG expression site and its expression var-
ies between T. b. rhodesiense isolates [19], expression of TgsGP by group 1 T. b. gambiense is
constitutive, rendering all isolates resistant to lysis by human serum [24].
The efficient uptake of TLF1 by African trypanosomes is dependent on the presence of hap-
toglobin-related protein in the complex and mediated by the parasite’s HpHb receptor [26–
30]. Our understanding of how TLF2 enters the parasite is incomplete. In common with TLF1,
it contains haptoglobin-related protein, and can enter via the parasite’s HpHb receptor,
though much less efficiently than TLF1 [26]. Instead, efficient TLF2 uptake has been proposed
to depend upon an interaction between its component IgM and the trypanosome’s VSG sur-
face coat [31]. Until recently, we knew little about the intracellular factors that determine the
Trypanoso ma brucei apolipopro tein-L1 sensitivity determinants
PLOS Pathogens | https:// doi.org/10.13 71/journal.p pat.1006 855 January 18, 2018 2 / 26
also part of the European and Developing Countr ies
Clinical Trials Partnersh ip (EDCTP) 2 Program,
supported by the European Union). AC and AML
were supporte d by a Wellcome Trust (https://
wellcome.a c.uk/) Senior Research Fellowsh ip
(095201/Z/1 0/Z) awarded to AML. The funders had
no role in study design, data collection and
analysis, decision to publish, or prepara tion of the
manuscript.
Competing interests : The authors have declared
that no competing interests exist.

sensitivity of T. b. brucei to lysis by human serum. Previously, we sought to address this deficit
by selecting our bloodstream-form (BSF) T. b. brucei RNAi library in normal human serum
(NHS), identifying four key sensitivity determinants [32]. Unsurprisingly, the most significant
‘hit’ was TbHpHbR, depleted by more than 70% of the RNAi target fragments in the selected
library. We also identified several other factors: ‘inhibitor of cysteine peptidase’ (ICP) [33], the
lysosomal-associated membrane protein, p67 [34], and a putative transmembrane protein of
unknown function, Tb927.8.5240. We subsequently showed that ICP modulates the function
of TbCATL, a lysosomal cathepsin-L-like cysteine peptidase, and that increased TbCATL
activity in icp null T. b. brucei renders them less sensitive to trypanolysis by human serum [32].
We speculated that this phenotype was due to increased degradation of TLF or apoL1 by the
deregulated lysosomal peptidase [35].
An independent study describing RNAi library screens using NHS and hyperhaptoglobi-
naemic serum as the selective agents was published in the same year [36]. Using freshly iso-
lated NHS at high concentration the authors identified TbHpHbR, though not p67 or ICP.
The addition of high concentration haptoglobin limited the contribution of TbHpHbR to
uptake, so reducing the contribution of TLF1 but enhancing that of TLF2 to parasite lysis, and
potentially enabling the screen to identify TLF2-specific sensitivity determinants. While a
TLF2-specific transporter was not identified in this screen, the role of the parasite’s vacuolar
(V-)ATPase and the kinesin, TbKIFC1, in promoting T. b. brucei sensitivity to human serum
was recognised [36, 37]. The V-ATPase drives progressive acidification of the endosomal-lyso-
somal network, a process required for the apoL1 conformational change that enables subse-
quent integration into the lysosomal membrane and pore formation [12–14]. TbKIFC1 acts to
couple lysosomal and mitochondrial membrane permeabilisation, leading to TbEndoG release
and nuclear DNA laddering [37]. Intriguingly, the NHS and hyperhaptoglobinaemic serum
screens identified non-overlapping sets of proteins, indicating that different selection condi-
tions can have a significant impact on the respective factors identified. This suggests that other
important sensitivity determinants remained undiscovered, particularly those that specifically
influence the action of apoL1. Given this and the dominance of RNAi target fragments deplet-
ing TbHpHbR following selection with NHS [32], we selected our genome-scale BSF T. b. bru-
cei RNAi library in recombinant apoL1, which enters the parasite by non-specific fluid phase
endocytosis [15], so bypassing TbHpHbR. Finally, we used two forms of recombinant apoL1,
human and baboon; both are effective against T. b. brucei, but the latter is lytic to a wider vari-
ety of African trypanosomes, including the human-infective forms, T. b. gambiense and T. b.
rhodesiense [38].
The outputs from apoL1-selection of the T. b. brucei RNAi library were broadly similar,
irrespective of the primate apoL1 used, suggesting that the mechanism of trypanolytic killing,
once either apoL1 has entered the parasite, is indistinguishable. However, comparison with the
previous outputs following RNAi library selection in human serum (either normal or hyper-
haptoglobinaemic) revealed intriguing similarities and differences. We identified parasite fac-
tors that influence T. b. brucei sensitivity to free apoL1 that had previously been implicated in
promoting sensitivity to hyperhaptoglobinaemic serum, such as the V-ATPase and TbKIFC1
[36, 37]. However, this comparison also identified NHS-specific (ICP [33] and p67 [34]) and
apoL1-specific sensitivity factors. The latter included a group of ubiquitin modifiers, and sev-
eral proteins with putative roles in membrane trafficking. We propose that, in contrast to
TLF1-embedded apoL1, the trypanocidal activity of free apoL1 is not dependent on lysosomal
morphology or proteolytic function, as defined by p67 and ICP/TbCATL, respectively. Finally,
we present evidence that ubiquitination has a role to play in the regulation of the network of T.
b. brucei proteins that support the trypanolytic action of apoL1.
Trypanoso ma brucei apolipopro tein-L1 sensitivity determinants
PLOS Pathogens | https:// doi.org/10.13 71/journal.p pat.1006 855 January 18, 2018 3 / 26

Results
A T. b. brucei genome-scale RNAi library identifies apoL1-sensitivity
determinants
Selection of BSF T. b. brucei RNAi libraries has previously been used to identify parasite factors
that drive the ability of human serum to lyse non-human infective African trypanosomes [32,
36]. These screens identified several endosomal-lysosomal proteins that support the action of
TLF; however, neither screen was able to offer direct insight into the proteins that specifically
influence the action of apoL1, the lytic component of primate serum TLF. In order to access
this level of detail, we selected our genome-scale BSF T. b. brucei RNAi library in recombinant
human and baboon (Papio hamadryas and P. papio) apoL1. EC
50
assays confirmed our strain
of T. b. brucei is similarly sensitive to human, P. hamadryas and P. papio recombinant apoL1 at
0.16 μg.ml
-1
, 0.22 μg.ml
-1
and 0.13 μg.ml
-1
, respectively (Fig 1A). In order to enable identifica-
tion of factors whose loss renders T. b. brucei less sensitive to primate apoL1, expression of the
RNAi library was induced for 24 hours prior to the addition of apoL1 at 2X EC
50
, and selection
and induction maintained thereafter (Fig 1B). After approximately four days under selection,
populations with reduced sensitivity to each recombinant apoL1 emerged, and these main-
tained slow but consistent growth under continued selection (Fig 1C). Genomic DNA was iso-
lated from these populations on day eight, and subjected to RNAi construct-specific PCR,
generating indistinguishable banding patterns for the human and P. hamadryas apoL1-se-
lected RNAi libraries, and a dissimilar pattern following selection in P. papio apoL1 (Fig 1D).
Fig 1. An RNAi library screen to identify T. b. brucei apoL1 sensitivit y determ inants. (A) T. b. brucei (MITat1.2; strain 2T1) is similarly sensitive
to human (H. sapiens) and baboon (P. hamadry as and P. papio) apoL1. EC
50
assays were carried out in quadrup licate; error bars, standard deviation.
(B) Schematic showing selection of apoL1- resistant parasites from the RNAi library. (C) Selection of populations with reduced sensitivity to apoL1.
RNAi induced in 1 μg.ml
-1
tetracyclin e (Tet) for 24 hours prior to selection (initiated at day-0); arrows indicate culture dilution, and addition of fresh
apoL1 and tetracycline at 2X EC
50
and 1 μg.ml
-1
, respectively. (D) RNAi target fragment-sp ecific PCR amplificati on from T. b. brucei genomic DNA
extracted after eight days’ selection in apoL1 (Hs, H. sapiens; Ph, P. hamadryas; Pp, P. papio).
https://d oi.org/10.1371/j ournal.ppa t.1006855 .g001
Trypanoso ma brucei apolipopro tein-L1 sensitivity determinants
PLOS Pathogens | https:// doi.org/10.13 71/journal.p pat.1006 855 January 18, 2018 4 / 26

We sequenced the amplified RNAi target fragment populations from the human and P. papio
apoL1 selected RNAi libraries on an Illumina MiSeq platform (sequencing data is available
from the European Nucleotide Archive, www.ebi.ac.uk/ena, accession number PRJEB23779).
Using our established RIT-seq methodology [39], we generated and mapped individual
sequence reads representing the human apoL1-enriched RNAi target fragments, constituting
about 1.65 million reads. Approximately 38% of these reads included the 14-base RNAi con-
struct-specific barcode found at the junction of each gene-specific RNAi target fragment. This
enabled us to identify the ‘high confidence hits’, i.e. those represented by more than 99 reads
per kilobase per predicted transcript (open reading frames plus predicted untranslated regions,
as annotated in the TREU927 reference genome available at www.tritrypdb.org) containing
the RNAi construct barcode, and at least two independent RNAi target fragments. We have
previously applied similarly stringent criteria to define the efficacy determinants of the anti-
HAT drugs [40] and NHS [32]. This analysis revealed that selection in human apoL1 had
enriched for a complex set of RNAi target fragments (Fig 2A and S1 Table). The outputs fol-
lowing T. b. brucei RNAi library selection in P. papio apoL1 constituted 1.68 million reads, of
which approximately 45% included the 14-base RNAi construct-specific barcode.
To enable comparison of the outputs following selection in human and P. papio apoL1, we
converted absolute reads to RPKM (reads per kilobase per transcript per million mapped
reads); the 100-read stringency criteria were also converted to RPKM for each screen (human
apoL1, 158; P. papio apoL1, 132; dashed lines in Fig 2B). Although there were differences in
the patterns obtained following RNAi construct-specific PCR (Fig 1D), high throughput
sequencing revealed that growth in either human or P. papio apoL1 selected for highly similar
sets of RNAi fragments (r
2
= 0.78; Fig 2B). This data, in conjunction with the shared RNAi
construct-specific PCR pattern following RNAi library selection in human or P. hamadryas
apoL1 (Fig 1D), suggests that apoL1 from the three species is dependent on a similar array of
T. b. brucei sensitivity determinants. Therefore, our subsequent analyses focused on the out-
puts obtained following human apoL1-selection of the T. b. brucei RNAi library. These consti-
tuted 63 ‘hits’ represented by more than 99 reads per kilobase per transcript, of which 39
aligned with more than one RNAi target fragment (S1 Table).
ApoL1 selection identifies known TLF2 sensitivity determinants
The top five ‘hits’ identified by apoL1 selection included the kinesin, TbKIFC1, and three sub-
units of the V-ATPase complex (two additional subunits also feature in our ‘hit’ list; Fig 2 and S1
Table). A previous RNAi library screen using hyperhaptoglobinaemic human serum as the selec-
tive agent, to enrich for TLF2-interacting proteins, also identified TbKIFC1 and three V-ATPase
subunits (V
1
-F and -H, and V
0
-a) [36, 37]. Interestingly, though our screen identified five
V-ATPase subunits, V
0
-c and V
1
-B, -C, -D and–H, the latter was the only subunit common to
both screens. Two of the five V-ATPase subunits (Tb927.10.14040 and Tb927.11.11690) identi-
fied following apoL1 selection failed to fulfil our stringency criteria for assignment as high-confi-
dence apoL1 sensitivity determinants, being represented by only one RNAi target fragment each
(Fig 2C; S1 Table). However, identification of RNAi target fragments for multiple V-ATPase
subunits in the selected library, indicate that these likely constitute genuine apoL1 sensitivity
determinants.
A review of our previously published genome-scale phenotyping analysis [41], revealed that
depletion of Tb927.10.14040 (V
0
-c) and Tb927.11.11690 (V
1
-B) led to a significant loss of fit-
ness in BSF T. b. brucei after three days (S1 Table). Therefore, these proteins are likely essential
for parasite survival, contributing to the limited number of independent RNAi target frag-
ments mapping to the cognate genes following selection in apoL1. To confirm the importance
Trypanoso ma brucei apolipopro tein-L1 sensitivity determinants
PLOS Pathogens | https:// doi.org/10.13 71/journal.p pat.1006 855 January 18, 2018 5 / 26

of Tb927.10.14040 for T. b. brucei growth and apoL1 sensitivity, we generated three indepen-
dent 2T1 T. b. brucei cell lines expressing stemloop RNAi cassettes targeting this transcript; the
2T1 strain of BSF T. b. brucei has an integration landing pad on chromosome 2, enabling con-
sistent inducible expression between clones from integrated cassettes [42, 43]. As predicted,
Tb927.10.14040 RNAi knockdown led to a significant growth defect, which we were able to
modulate by reducing the amount of tetracycline used to induce stemloop RNAi cassette
expression (S1A Fig). Depletion of Tb927.10.14040 following induction in 2 ng.ml
-1
tetracy-
cline resulted in increased survival in the presence of 10 μg.ml
-1
apoL1 and 0.1% NHS, con-
firming the contribution of this putative V-ATPase subunit to parasite apoL1 sensitivity (S1B
Fig) and highlighting its general role in determining sensitivity to human serum (S1C Fig).
Fig 2. Selecting a genome-scale T. b. brucei RNAi library identifie s parasite determinan ts of apoL1 sensitiv ity. (A) Genome-
wide human apoL1 RIT-seq profile representi ng 7,398 non-redunda nt predicted transcripts, showing those targeted by 100 or
more reads per kilobase containing the 14-base RNAi construct barcode sequence. ‘Hits’ targeting V-ATP ase subunits and the
kinesin, TbKIFC1, are highlighted in green and red, respectively; novel high confiden ce hits correspond ing to six putative
ubiquitin modifie rs and four putative membran e transport ers are highligh ted in black and blue, respectively (see Fig 4 and S1
Table for further details). (B) RNAi library selection with human or P. papio apoL1 identified similar sets of sensitivity
determinants (r
2
= 0.78); key hits are coloured as in (A), and are similarly abundant in both selected libraries. Data presented as
RPKM (plus 0.1; reads per kilobase of transcrip t per million mapped reads) to correct for variations in read depth between the
respective RNAi library screens (and to enable plotting of zero read outputs on log
10
scales). Dashed lines represent the 100-read
stringency criterion converted to RPKM for each RNAi library screen (human apoL1, 158; P. papio apoL1, 132). (C) RIT-seq
profiles for three of the V-ATPase subunits and for TbKIFC1 ; predicted transcrip ts (open reading frames and untransl ated
regions) are coloured as in (A); total reads (red) and tagged reads (blue; containing the 14-base RNAi construct barcode sequence)
mapped to each predicted transcript are shown in the top right corner of each panel.
https://doi.org/10 .1371/journal.p pat.1006855.g 002
Trypanoso ma brucei apolipopro tein-L1 sensitivity determinants
PLOS Pathogens | https:// doi.org/10.13 71/journal.p pat.1006 855 January 18, 2018 6 / 26

This data further emphasises the importance of the V-ATPase complex to apoL1-mediated
killing of T. b. brucei [36].
TbCATL and p67 do not influence T. b. brucei sensitivity to apoL1
The identification of predicted apoL1-sensitivity determinants (TbKIFC1 and subunits of the
V-ATPase) provides a robust validation of our RNAi library screening approach. However,
our screen did not identify two proteins previously shown to contribute to T. b. brucei sensitiv-
ity to NHS: ‘inhibitor of cysteine peptidase’ (ICP) and the lysosomal-associated membrane
protein, p67 [24, 32, 34]. ICP determines the trypanolytic efficacy of NHS via its regulation of
the parasite’s cathepsin-L-like cysteine protease, TbCATL [32]; this finding led to the hypothe-
sis that lysosomal TbCATL is able to limit human serum efficacy through degradation of
apoL1, TLF or both [35]. In contrast, p67, contributes to the maintenance of lysosomal mor-
phology, and depletion of this protein leads to changes in lysosome structure and a concomi-
tant reduction in sensitivity to lysis by human serum [34].
To enable a comparison with the current data set, we reanalysed the outputs from our origi-
nal NHS RNAi library screen [32] (European Nucleotide Archive, www.ebi.ac.uk/ena, acces-
sion number PRJEB23776), generating reads per kilobase per transcript values for each
annotated gene. Previously, the outputs were expressed as reads per kilobase per CDS; this
reanalysis ensured compatibility with the current data set and recognised that targeted destruc-
tion of any part of a transcript will likely lead to depletion of the cognate protein (no additional
high-confidence ‘hits’ were identified). To correct for differences in read depth between the
two experiments, we converted the NHS and apoL1 data sets to RPKM (Fig 3A); the 100-read
stringency criteria were also converted to RPKM for each screen (human apoL1, 158; NHS,
404; dashed lines in Fig 3A). No RNAi target fragment surpassed the corrected ‘100-read’
stringency criterion in both screens, suggesting that distinct sets of proteins determine the sen-
sitivity of T. b. brucei to apoL1 and NHS (Fig 3A; S2 and S3 Tables).
While it is unsurprising that T. b. brucei sensitivity to apoL1 is unaffected by loss of the
HpHb receptor (uptake of free apoL1 occurs independently of this receptor via non-specific
fluid phase endocytosis [15]), we were surprised that RNAi targeting fragments corresponding
to ICP and p67 were not more prominent following apoL1 selection. Both p67 and ICP failed
to fulfil our stringency criteria for assignment as high-confidence apoL1 sensitivity determi-
nants. Following selection in human (and P. papio) apoL1, the two predicted p67 transcripts
returned RPKM values of 104 (41) and 80 (31), respectively (S2A Fig; S3 Table); while, the pre-
dicted ICP transcript returned an RPKM value of 32 (32) (S2B Fig; S3 Table). In both cases, the
RPKM values were less than the RPKM 99-read stringency cut-off (human apoL1, 158; P.
papio apoL1, 132).
These data strongly suggest that, in contrast to NHS, neither p67 nor ICP has a significant
role in determining the sensitivity of T. b. brucei to apoL1. To test this hypothesis, we revisited
our published p67 stemloop RNAi and icp null cell lines [32, 40]. As predicted, RNAi knock-
down of p67 had no effect on parasite sensitivity to apoL1; however, as previously shown [34],
depletion of p67 had a significant impact on parasite sensitivity to NHS, reducing it more than
two-fold (Fig 3B). Consistent with our previous findings [32], icp null T. b. brucei were approx-
imately ten-fold less sensitive to NHS, but loss of ICP had no significant impact on parasite
sensitivity to apoL1 (Fig 3C). Moreover, while depletion of TbCATL in icp null T. b. brucei
complemented the loss of NHS sensitivity, as previously shown [32], it had no effect on para-
site sensitivity to apoL1 (Fig 3D). These data confirm that free apoL1 is not vulnerable to intra-
cellular TbCATL-mediat ed proteolytic attack, and indicate that lysosomal function, as defined
by p67, ICP and TbCATL, has no significant impact on T. b. brucei killing by free apoL1.
Trypanoso ma brucei apolipopro tein-L1 sensitivity determinants
PLOS Pathogens | https:// doi.org/10.13 71/journal.p pat.1006 855 January 18, 2018 7 / 26

RNAi library selection identifies novel T. b. brucei apoL1 sensitivity
determinants
As well as the known apoL1/TLF2 sensitivity determinants described above, our RNAi library
screens also identified a large number of novel factors, which may contribute to apoL1 action
(S1 Table). Twenty-four of the identified proteins are annotated ‘hypothetical’, making it diffi-
cult to speculate on their mode of interaction with apoL1. Of the remaining proteins with a
functional annotation, two groups stood out: putative ubiquitin modifiers and proteins associ-
ated with vesicle and membrane trafficking (Fig 2A).
We identified six putative ubiquitin modifiers in our screen: two Zn-RING finger E3-ubi-
quitin ligases, an E2-ubiquitin conjugase, two ubiquitin hydrolases (or deubiquitinases,
DUBs), and a PUB-domain containing protein (a putative p97/cdc48 cofactor [44]) (Fig 4A;
S1 Table). Ubiquitination plays a role in determining the efficacy of the anti-HAT drug, sura-
min [40, 45]; however, this is the first report of its involvement in apoL1 action against T. b.
Fig 3. Distinct sets of T. b. brucei proteins determ ine parasite sensitivity to apoL1 and NHS. (A) Reads containi ng the 14-base RNAi construct-spe cific
barcode identified following RNAi library selection in human apoL1 (this study) or NHS [32] plotted as RPKM (plus 0.1) to correct for variations in read
depth between the respective RNAi library screens (and to enable plotting of zero read outputs on log
10
scales); r
2
= 0.016. Dashed lines represent the
100-read stringency criterion converted to RPKM for each RNAi library screen (human apoL1, 158; NHS, 404); apoL1 (purple) and NHS (orang e)-specific
RNAi targets are highlighted and the top hits listed (gene ID and functional annotation; see S2 and S3 Tables for further details). (B-D) Represen tative EC
50
assays carried out in quadruplicate confirming that (B) p67 knockdown, (C) ICP deletion and (D) TbCATL depletion does not affect T. b. brucei sensitivity
to apoL1. Insets, representati ve EC
50
assays carried out in quadrupli cate showing the known impact of the correspond ing manipu lations on sensitiv ity to
NHS. Error bars, standard deviation.
https://doi.org/10 .1371/journal.p pat.1006855.g 003
Trypanoso ma brucei apolipopro tein-L1 sensitivity determinants
PLOS Pathogens | https:// doi.org/10.13 71/journal.p pat.1006 855 January 18, 2018 8 / 26

brucei. The recent finding that apoL1-mediated killing of T. b. brucei involves mitochondrial
membrane permeabilisation [37] highlighted the importance of the transit of apoL1-contain-
ing membrane from the endosomal-lysosoma l system to the mitochondrion. Consistent with
this, we identified four uncharacterised proteins with putative roles in membrane trafficking:
Tb927.5.3560 (vesicle associated membrane protein, VAMP7B), Tb927.11.13230 (‘major
sperm protein’, MSP domain; characteristic of VAMP-associated proteins), Tb927.9.9750
(‘secretory carrier membrane protein’, SCAMP domain) and an aminophospholipid-trans -
porting ATPase (or ‘flippase’; Tb927.11.3350) (Fig 4B; S1 Table).
A putative lysosomal E3-ubiquitin ligase influences T. b. brucei sensitivity
to apoL1 and NHS
The putative Zn RING finger E3-ubiquitin ligase, Tb927.10.12940, was the top ‘hit’ following
RNAi library selection in human apoL1 (and second, following selection in P. papio apoL1); it
was targeted by >700,000 reads, of which >261,000 contained the RNAi construct-specific
barcode (Fig 4A; S1 Table). Targeted knockdown of Tb927.10.12940 by stemloop RNAi in 2T1
T. b. brucei had no detectable effect on parasite population growth (S3A Fig), but resulted in a
more than three-fold increase in apoL1 EC
50
(Fig 5A), confirming that this putative E3-ubiqui-
tin ligase is an apoL1 sensitivity determinant. Interestingly, knockdown of Tb927.10.12940
rendered BSF T. b. brucei approximately two-fold more sensitive to NHS (Fig 5B), explaining
why RNAi library selection in human serum did not identify this protein [32]. Ectopic expres-
sion of a C-terminally GFP-tagged copy of Tb927.10.12940 (12940
GFP
; Fig 5C) revealed a dis-
crete signal between the kinetoplast and nucleus, reminiscent of an endocytic compartment
(S3B Fig), which was confirmed as the lysosome by co-localisation with the lysosomal mem-
brane protein, p67 [34] (Fig 5D).
The validation of Tb927.10.12940 as an apoL1 sensitivity determinant and the presence of
other putative ubiquitin modifiers in the ‘hit’ list (six of 63 ‘hits’; Fig 2A; S1 Table), suggests
Fig 4. RIT-seq profiles of candidate novel apoL1-sensiti vity determinan ts. ApoL1 sensitivity determinant s include (A) putative ubiquitin modifie rs
and (B) putative membran e trafficking proteins. RIT-seq profiles show predicte d transcrip ts (open reading frames and untranslat ed regions of interest in
black) and the RNAi targeting fragment reads mapped; total reads (red) and tagged reads (blue; containing the 14-base RNAi constru ct barcode sequenc e)
mapped to each predicte d transcrip t are shown in the top right corner of each panel. Known or putative annotati ons based on domain organisation are
included beneath each accession number and derived from GeneDB (http://w ww.genedb.org /Homepage /Tbruceibruc ei927). Ub, ubiquitin; DUB,
deubiqui tinase; VAMP, vesicle-assoc iated membran e protein; VAP, VAMP-as sociated protein.
https:// doi.org/10.1371 /journal.ppat.1 006855.g004
Trypanoso ma brucei apolipopro tein-L1 sensitivity determinants
PLOS Pathogens | https:// doi.org/10.13 71/journal.p pat.1006 855 January 18, 2018 9 / 26

that ubiquitination may contribute to T. b. brucei apoL1 sensitivity. At present, it is unclear
which parasite proteins are modified and how this influences apoL1 action. However, using
the online UbPred algorithm [46] we identified high confidence candidate ubiquitination sites
in 23 of the 63 top hits identified following apoL1 selection of our BSF T. b. brucei RNAi library
(S4 Table). Therefore, changes in the ubiquitination status of one or more of these proteins
may underlie the changes in apoL1 sensitivity observed following RNAi-mediated knockdown
of Tb927.10.12940 (Fig 5A and 5B).
Evidence for Tb927.10.12940 and Tb927.9.8000 interdependence
In order to explore whether Tb927.10.12940 acts in concert with any of the other putative ubi-
quitin modifiers identified in our screen or affects the action of other apoL1 sensitivity deter-
minants, we generated a 12940 null 2T1 T. b. brucei following integration of neomycin
phosphotransferase (NPT) and blasticidin-S-deamina se (BSD) selectable markers (Fig 6A). In
contrast to RNAi knockdown, deletion of both copies of the Tb927.10.12940 open reading
frame led to an increased population doubling time (wild type, 7.0±0.07 hours; 12940 null, 8.0
±0.04 hours; Fig 6B). However, consistent with our earlier data, 12940 null T. b. brucei were
less sensitive to apoL1 than wild type parasites (Fig 6C), a phenotype complemented by 12940
re-expression (Fig 6D). Furthermore, deletion of 12940 reduced the speed of parasite killing in
Fig 5. Tb927.10.1294 0 has opposing effects on apoL1 and NHS sensitivity, and localises to the lysosome. Representativ e EC
50
assays carried
out in quadruplicate showing the impact of Tb927.10.1 2940 RNAi knockdown on T. b. brucei sensitivity to (A) apoL1 and (B) NHS. Inset charts
show pooled EC
50
data for three independen t cell lines. Error bars, standard deviation; P-values derived from paired students t-test. (C) Western
blot showing tetracyclin e (tet)-inducibl e expression of Tb927 .10.12940
GFP
. (D) Immunofluo rescence localisation of Tb927.10. 12940
GFP
and the
lysosoma l membran e protein, p67; counter-s taining with the DNA intercalati ng dye, DAPI, reveals the kinetoplast (k) and nucleus (n). A
processed merged image of the region of interest shows the co-localisatio n of Tb927.10 .12940
GFP
and p67. Scale bar, 5 μm.
https://do i.org/10.1371/j ournal.ppa t.1006855.g005
Trypanoso ma brucei apolipopro tein-L1 sensitivity determinants
PLOS Pathogens | https:// doi.org/10.13 71/journal.p pat.1006 855 January 18, 2018 10 / 26

the presence of 10 μg.ml
-1
apoL1 (Fig 6E), a concentration comparable with that found in
human serum [15]; this phenotype was complemented by 12940 re-expression (Fig 6F).
Fig 6. Generati on and complem entation of 12940 null T. b. brucei. (A) Southern blot confirmin g Tb927.10. 12940 deletion; BSD, blasticidin-S -
deaminase; NPT, neomycin phosphotrans ferase. Schematic showing segment deleted from the Tb927.10.12 940 locus (open triangle); positio ns of SalI
restriction sites (arrowheads ), deletion (12940) and flanking (DS) probes highligh ted. (B) Cumulativ e growth of wild type and three independen t 12940
null T. b. brucei cell lines; error bars showing standard deviation are smaller than the plot symbols . (C, D) Representa tive EC
50
assays carried out in
quadruplicate showing the impact of (C) Tb927.1 0.12940 deletion and (D) re-expression on apoL1 sensitivity. Insets, pooled EC
50
data for at least two
independen t cell lines. (E, F) Kinetic analyse s of parasite killing in 10 μg.ml
-1
apoL1 following (E) Tb927.10.1294 0 deletion and (F) re-express ion; each
assay was carried out using three independen t cell lines, re-express ion was induced in 1 μg.ml
-1
tetracycl ine for 24 hours prior to exposure to apoL1.
Error bars, standard deviatio n; P-values derived from paired students t-test.
https://doi.o rg/10.1371/j ournal.ppa t.1006855.g006
Trypanoso ma brucei apolipopro tein-L1 sensitivity determinants
PLOS Pathogens | https:// doi.org/10.13 71/journal.p pat.1006 855 January 18, 2018 11 / 26

E3-ubiquitin ligases act to direct the E2-ubiquitin conjugases to modify specific protein tar-
gets [47]. RNAi library selection in apoL1 identified one putative E2-ubiquitin conjugase,
Tb927.9.8000, leading us to speculate that the influence of Tb927.10.12940 on T. b. brucei
apoL1 and NHS sensitivity would be dependent on this protein. Therefore, these proteins may
exhibit an epistatic interaction. To test this hypothesis, we knocked down Tb927.9.8000 by
stemloop RNAi in wild type and 12940 null 2T1 T. b. brucei. We also N-terminally GFP-tagged
Tb927.9.8000 at the native locus, enabling tracking of protein knockdown (S4A Fig), but
were unable to detect a specific localisation of the fusion protein. RNAi knockdown of
Tb927.9.8000 in either wild type (S4B Fig) or 12940 null 2T1 T. b. brucei (S4C Fig) led to a sig-
nificant growth defect; deletion of Tb927.10.12940 did not enhance the observed growth defect
(wild type, Tb927.9.8000 RNAi, 9.3±1.2 hours; 12940 null, Tb927.9.8000 RNAi, 9.7±0.4 hours;
S5D Fig).
RNAi knockdown of Tb927.9.8000 in wild type 2T1 T. b. brucei led to a slight but significant
reduction in apoL1 sensitivity; however, Tb927.9.8000 RNAi did not further reduce the apoL1
sensitivity of 12940 null 2T1 T. b. brucei (Fig 7A). Tb927.9.8000 depletion also affected NHS
sensitivity, resulting in a three-fold EC
50
decrease, though again, there was no enhancement of
this effect in 12940 null 2T1 T. b. brucei (Fig 7B). The absence of any significant additive effect,
following loss of both proteins, upon growth or apoL1 and NHS sensitivity, suggests that
Tb927.10.12940 and Tb927.9.8000 act together to influence the trypanocidal action of these
agents.
Fig 7. Evidence for interdep endence between Tb927.9. 8000 and Tb927.10 .12940. Represen tative EC
50
assays carried out in quadrup licate showing
the impact of Tb927.9. 8000 RNAi knockdown in wild type (left hand panels) and 12940 null (middle panels) T. b. brucei on (A) apoL1 and (B) NHS
sensitivity. Right hand panels, pooled EC
50
data for at least three independen t cell lines. Error bars, standard deviation.
https://do i.org/10.1371/j ournal.ppa t.1006855.g007
Trypanoso ma brucei apolipopro tein-L1 sensitivity determinants
PLOS Pathogens | https:// doi.org/10.13 71/journal.p pat.1006 855 January 18, 2018 12 / 26

Tb927.10.12940 and TbKIFC1 exhibit trypanocide-specific
interdependence
While Tb927.10.12940 and Tb927.9.8000 may act together to influence the trypanocidal activ-
ity of apoL1 and NHS, they are unlikely to interact directly with TLF or apoL1. Rather, we
hypothesised that their putative ubiquitin ligase and conjugase functions enable them to mod-
ulate the activity of apoL1/TLF-interacting proteins. Given the predominantly lysosomal loca-
lisation of 12940
GFP
(Fig 5D), other proteins localising to this organelle might be functionally
dependent on Tb927.10.12940 and Tb927.9.8000. One such candidate protein is TbKIFC1,
which though not limited to the lysosome, directs apoL1-containing membrane from the lyso-
some to the mitochondrion [37]; this protein is also a putative suramin efficacy determinant
[40]. Our analysis using the UbPred algorithm [46] identified four putative high confidence
ubiquitination sites in TbKIFC1 (S4 Table), suggesting that ubiquitination, possibly mediated
by Tb927.10.12940 and Tb927.9.8000, might play a role in modulating its ability to influence
T. b. brucei apoL1, NHS and suramin sensitivity.
RNAi knockdown of TbKIFC1 in 12940 null 2T1 T. b. brucei had no additive impact on
population growth (S5 Fig), but had different effects on the trypanocidal activity of free apoL1,
NHS and suramin (Fig 8). RNAi knockdown of TbKIFC1 in wild type 2T1 T. b. brucei led to
an approximately six-fold increase in apoL1 EC
50
, while concurrent loss of Tb927.10.12940
had a marginal additive effect (Fig 8A). In contrast, even though 12940 null 2T1 T. b. brucei are
more sensitive to NHS, RNAi knockdown of TbKIFC1 complemented this sensitisation,
reducing NHS sensitivity to the same level seen following TbKIFC1 RNAi knockdown in wild
type 2T1 T. b. brucei (Fig 8B). TbKIFC1 depletion rendered wild type 2T1 T. b. brucei 1.7-fold
less sensitive to suramin, validating its identification following suramin selection of the RNAi
library [40]. Unexpectedly, we found that 12940 null 2T1 T. b. brucei were 1.6-fold less sensi-
tive to suramin than wild type parasites. A reanalysis of our suramin-selected T. b. brucei
RNAi library revealed that RNAi fragments mapping to Tb927.10.12940 were enriched follow-
ing selection, though not to a level that fulfilled our stringency criteria [40]. Even though loss
of either protein leads to a similar reduction in suramin efficacy, TbKIFC1 depletion in 12940
null 2T1 T. b. brucei did not enhance this effect (Fig 8C).
A preliminary western blot analysis of
6MYC
TbKIFC1 expression following Tb927.9.8000 or
Tb927.10.12940 RNAi did not show any detectable differences in expression (S6 Fig), so the
basis for the putative interaction between Tb927.10.12940 and TbKIFC1 is unclear. However,
the EC
50
analyses described above suggest that the role of TbKIFC1 in apoL1 sensitivity and
suramin efficacy is at least partly dependent upon Tb927.10.12940, while its impact on NHS
sensitivity is independent of this putative E3-ubiquitin ligase.
Discussion
T. b. gambiense and T. b. rhodesiense are resistant to lysis by apoL1-containing trypanolytic fac-
tors in human serum, while T. b. brucei is exquisitely sensitive to this attack. We report an
RNAi library screen using recombinant human apoL1, which identified an extensive set of fac-
tors, including 57 novel putative apoL1 sensitivity determinants, as well as several V-ATPase
subunits [36] and TbKIFC1 [37]. Prominent among the novel factors were four membrane
trafficking proteins and six ubiquitin protein modifiers, including the most significant ‘hit’, a
putative RING E3-ubiquitin ligase. Intriguingly, our analyses revealed that the lysosomal fac-
tors previously shown to influence the anti-trypanosomal activity of NHS have no effect on
parasite sensitivity to free apoL1.
As well as the apoL1-focussed RNAi library screens described herein, several other screens
have been carried out using commercially supplied [32] and freshly isolated and haptoglobin-
Trypanoso ma brucei apolipopro tein-L1 sensitivity determinants
PLOS Pathogens | https:// doi.org/10.13 71/journal.p pat.1006 855 January 18, 2018 13 / 26

supplemented NHS [36, 37] as selective agents. These screens led to the identification of multi-
ple T. b. brucei proteins that influence trypanolysis (summarised in Table 1). Below, we discuss
our results in light of the outputs from the preceding screens, and consider the implications of
these data for our understanding of trypanolytic factor mode-of-action.
TbHpHbR-specific RNAi target fragments dominated the outputs from our original NHS
RNAi library screen [32], suggesting that TLF1, which is efficiently taken up by this receptor
[30], was the most abundant TLF in our NHS. To enable the identification of other T. b. brucei
Fig 8. TbKIFC1 depletion compleme nts NHS sensitivity of 12940 null T. b. brucei, but has no additive effect on apoL1 sensitivity or suramin
efficacy. Represen tative EC
50
assays carried out in quadrup licate showing the impact of TbKIFC1 RNAi knockdown in wild type (left hand panels)
and 12940 null (middle panels) T. b. brucei on (A) apoL1, (B) NHS and (C) suramin sensitiv ity. Right hand panels, pooled EC
50
data for at least three
independen t cell lines. Error bars, standard deviatio n.
https://doi.org/10 .1371/journal.p pat.1006855.g 008
Trypanoso ma brucei apolipopro tein-L1 sensitivity determinants
PLOS Pathogens | https:// doi.org/10.13 71/journal.p pat.1006 855 January 18, 2018 14 / 26

factors that promote trypanolysis, especially by TLF2 which dominates the in vivo human
innate response to non-human infectious trypanosomes [48], Lecordier and co-workers used
fresh human serum supplemented with haptoglobin to select their RNAi library [36]. How-
ever, TLF2 can also enter the parasite via the HpHb receptor and TLF1 can enter the parasite
independently of this receptor, though in both cases entry is much less efficient [26]. There-
fore, supplementation with haptoglobin will not completely ablate the effect of TLF1, though it
will significantly reduce its contribution to trypanolysis. Confronted with the same challenge,
we took an alternative approach; instead, selecting our T. b. brucei RNAi library with recombi-
nant apoL1. As with the hyperhaptoglobinaemic serum selection strategy, selection with apoL1
identified TbKIFC1 and components of the V-ATPase complex (seven of the fourteen putative
V-ATPase subunits [49] are now associated with the promotion of trypanolysis). The identifi-
cation of these proteins using distinct screening approaches and the failure to identify them by
RNAi library selection in NHS, highlights their importance to apoL1 and TLF2 action, and
may indicate that they have a less significant role to play in TLF1-mediated trypanolysis. For
example, while TbKIFC1 mediates the transit of apoL1-containing membrane to the mito-
chondrion [37] and its loss led to an approximately 6-fold apoL1 EC
50
increase, there was only
a marginal (approximately 1.4-fold) effect on NHS EC
50
(see Fig 8B), explaining our inability
to identify it in our TLF1-dominated NHS screen [32]. In contrast, RNAi knockdown of the
V-ATPase subunit, Tb927.10.14040, revealed similar effects on sensitivity to apoL1 and our
TLF1-dominated NHS, confirming that decreasing pH through the endocytic system is criti-
cally important to the trypanolytic action of TLF1, as well as apoL1 and TLF2. Therefore, while
the selection of RNAi fragments targeting a specific mRNA indicates that the corresponding
protein may have a role in mediating the efficacy of a selective agent, their absence is not nec-
essarily evidence to the contrary.
The trypanolytic action of TLF1 is not only dependent on the parasite’s HpHb receptor [20,
30] and V-ATPase, but is also influenced by T. b. brucei lysosomal function (Fig 9A). Where
this is impaired due to reduced levels of the lysosomal membrane protein, p67 [34], or
enhanced as a consequence of ICP loss and increased TbCATL activity [24, 32], T. b. brucei
becomes significantly less sensitive to NHS. In contrast, the data presented here demonstrate
that apoL1’s ability to kill T. b. brucei is unaffected by the loss of p67 or ICP, or changes in
TbCATL activity. Interestingly, RNAi fragments targeting p67 and ICP were not reported in
the hyperhaptoglobinaemic human serum RNAi library screen described by Lecordier and co-
workers [36]. Therefore, lysosomal function, as defined by these proteins, also appears to have
little impact on parasite sensitivity to TLF2, as approximated for by hyperhaptoglobinaemic
serum (Fig 9B).
Table 1. T. brucei serum-sensi tivity determin ants identified by RNAi library screening .
NHS (commerc ial)
a
[32] NHS (fresh)
a
[36,
37]
+haptoglo bin
a
[36, 37] ApoL1 (recombinant )
a, b
HpHb receptor HpHb receptor V-ATPase -a, -F and–H V-ATPase -c
(plus four subunits)
Inhibitor of cysteine peptidase KIFC1 KIFC1
Lysosome- associated membran e
protein, p67
V-ATPase assembly factors, PKR1
and RAV1
Putative E3-ubiquitin ligase, Tb9297.1 0.12940, and E2-ubiquitin
conjugase, Tb927.9.80 00
(plus four other putative ubiquitin modifiers )
Putative trans-membra ne protein
(Tb927.8 .5240)
(Four putative membrane-tra fficking proteins)
a
Validat ed hits are detailed under each screen, while key additional hits are in parenthe ses
b
See S1 Table for details
https://do i.org/10.1371/j ournal.ppa t.1006855.t0 01
Trypanoso ma brucei apolipopro tein-L1 sensitivity determinants
PLOS Pathogens | https:// doi.org/10.13 71/journal.p pat.1006 855 January 18, 2018 15 / 26

The finding that parasite sensitivity to NHS is influenced by lysosomal factors led to the
hypothesis that enhanced TbCATL activity as a consequence of ICP loss leads to destruction of
TLF, apoL1 or both [32, 35], limiting the ability of apoL1 to integrate into the lysosomal mem-
brane and form the pores that ultimately lead to trypanolysis. Alternatively, ICP loss and ele-
vated TbCATL activity may increase the rate of TbHpHbR catabolism in the lysosome, leading
to reduced TLF1 uptake. While our current data does not allow us to define the target of lyso-
somal TbCATL, it is clear that free apoL1 (and TLF2) is not subject to this proteolytic attack.
To explain this we suggest that free apoL1 is able to integrate into the membranes of the endo-
cytic system prior to reaching the lysosome. The lumenal pH of the eukaryotic endocytic sys-
tem progressively decreases from 6–6.5 in early endosomes to 4.5–5.5 in the late endosome
and lysosome [50]. Consistent with other eukaryotes, the lumenal pH of the T. b. brucei lyso-
some is approximately 4.8 [51], and it is likely that the pH of the late endosome is close to that
of the lysosome. Hence, free apoL1 may be able to complete membrane integration prior to
reaching the lysosome. Indeed, in vitro assays have shown that apoL1 is able to integrate into
membranes at pH5.3 [17], higher than that recorded in the T. b. brucei lysosome [51]. Pre-lyso-
somal membrane integration by apoL1 would limit its exposure to proteolytic attack by lyso-
somal lumenal proteases, such as TbCATL, but endosomal-lysosomal membrane fusion would
still enable it to accumulate in the lysosomal membrane (Fig 9B).
The hypothesis that apoL1 membrane integration occurs prior to the lysosome is supported
by the identification of homologues of the SNARE protein, VAMP7B (Tb927.5.3560), and a
putative VAMP-associated protein (Tb927.11.13230). In other eukaryotes, VAMP7B is a medi-
ator of endosomal-lysosomal membrane fusion [52], and the VAMP-associated protein,
VAP33, may have a role in vesicle trafficking through its promiscuous binding to SNARE pro-
teins [53]. Therefore, in T. b. brucei these proteins may act in concert to promote the transfer
of apoL1-containing membrane through the parasite’s endocytic system. Intriguingly, G1 and
G2 variants of apoL1, which are associated with increased kidney disease risk in humans [54],
interact with and impair VAMP8 function in human cells leading to changes in autophago-
some-lysosome fusion dynamics that may underlie the observed kidney pathology [55, 56].
Fig 9. RNAi library screens reveal the distinct paths that human serum TLFs follow to instigate trypanoly sis. (A) The anti-tr ypanosomal action of
TLF1 is particular ly vulnerab le to changes in the surface receptor , TbHpHbR , and lysosomal function as defined by the V-ATPase, p67, ICP and
TbCATL. (B) ApoL1 and TLF2 enter T. brucei via fluid phase endocytosis and an unknown mechan ism (represen ted by the black box), respectively, and
are reliant on the support of a network of sensitivity determina nts, including the V-ATPase and vesicle and membran e trafficking proteins, such as
TbKIFC1 and VAMP7B, which may themselv es be regulated by dynamic ubiquitination. The orange bars represent membran e-integrate d apoL1. The
dashed line highlights the recent finding that apoL1 may also form pores in the parasite’s plasma membran e (omitted from panel (B) for clarity) [17].
Ellipses highlight possible regions of influence of the membrane trafficking (VAMP) and ubiquit ination (Ub) proteins described herein.
https://do i.org/10.1371/j ournal.ppa t.1006855.g009
Trypanoso ma brucei apolipopro tein-L1 sensitivity determinants
PLOS Pathogens | https:// doi.org/10.13 71/journal.p pat.1006 855 January 18, 2018 16 / 26

Furthermore, our screen identified an aminophospholipid-transp orting ATPase,
Tb927.11.3350, homologues of which are responsible for maintaining membrane asymmetry,
which is important for efficient vesicle budding and trafficking [57].
Given the absence of free apoL1 in human serum, are these observations physiologically rel-
evant? We do not know when, how or if apoL1 separates from TLF as it passes through the
parasite’s endocytic system, though the acidic pH of the lysosome may promote TLF1-apoL1
dissociation [16]. Alternatively, the TLF1-apoL1 association may persist until TLF1 binding to
the lysosomal membrane enables apoL1 integration [58]. Although TLF2 also delivers apoL1
into the parasite, its mechanism of entry and the point at which it releases its toxic payload is
unknown. In the absence of a specific receptor, TLF2 may be internalised via the binding of its
constituent IgM to the VSG coat and subsequent coat recycling [31, 36]. VSG-antibody com-
plexes are efficiently internalised via hydrodynamic flow and endocytosis [59]. While the
mechanism of sorting and antibody removal remain to be fully elucidated [60], this processing
could conceivably lead to the release of apoL1 much earlier in the endocytic pathway, so expos-
ing T. b. brucei to free apoL1 (Fig 9B).
Beyond the identity of the T. b. brucei proteins directly engaged in promoting the trypano-
lytic action of TLF and apoL1 described above, we know little about their regulation. Promi-
nent among the apoL1 sensitivity determinants identified in our screen was a set of putative
ubiquitin modifiers, including two ubiquitin ligases, a conjugase and two deubiquitinases
(DUB), representing each stage of the ubiquitination and deubiquitination process. Ubiquiti-
nation is a reversible post-translational modification involved in the regulation of numerous
cellular processes in eukaryotes, including protein degradation and subcellular localisation
[61]. We also identified a PUB-domain containing protein (Tb927.11.6340), a candidate p97/
cdc48 AAA+ ATPase cofactor [44]. Although we did not identify the T. b. brucei p97/cdc48
homologue (Tb927.10.5770) in our screen, this is probably unsurprising as it is expected to be
involved in the regulation of many cellular processes, including membrane fusion through its
interactions with various components of the ubiquitination and membrane trafficking
machinery [44], so is likely highly essential. Indeed, RNAi knockdown of Tb927.10.5770 led to
a severe loss of fitness in our earlier high-throughput phenotyping analysis [41].
In T. b. brucei, ubiquitination plays an important role in the regulation of invariant surface
glycoproteins 65 and 75 [62, 63], and ISG75 contributes to the uptake of the anti-HAT drug,
suramin [40], a process influenced by two putative DUBs, TbUsp7 and TbVdu1 [45]. Our data
revealed an interdependence between the RING E3 ubiquitin ligase, Tb927.10.12940, and the
ubiquitin E2 conjugase, Tb927.9.8000. However, we have yet to identify the target(s) of this
putative ubiquitination machinery. We hypothesised that changes in ubiquitination status may
be responsible for the regulation of at least some of the 63 proteins identified in our screen; a
preliminary analysis revealed that 23 of these proteins, including TbKIFC1, contain high-con-
fidence candidate ubiquitination sites. Interestingly, analysis of TbVAMP7B using the Ubpred
algorithm failed to identify any high confidence ubiquitination sites, even though TbVAMP7B
is influenced by TbUsp7; RNAi knockdown of this DUB leads to an approximately 40%
decrease in TbVAMP7B protein levels [45]. Therefore, either the interaction between TbUsp7
and TbVAMP7B is indirect or many more of the candidate apoL1 sensitivity determinants
may be subject to ubiquitination-based regulation.
Proteomic analysis of our existing RNAi (Tb927.9.8000; Tb927.10.12940) and null
(Tb927.10.12940) cell lines, as well as those designed to deplete other elements of the parasite’s
putative ubiquitination machinery identified in our screen, may enable the identification of
their targets. However, the experimental data presented here suggests that these relationships
may be complex. For example, while TbKIFC1 and Tb927.10.12940 promote apoL1 sensitivity
and suramin efficacy, these two proteins have opposing effects on parasite sensitivity to NHS.
Trypanoso ma brucei apolipopro tein-L1 sensitivity determinants
PLOS Pathogens | https:// doi.org/10.13 71/journal.p pat.1006 855 January 18, 2018 17 / 26

Loss of TbKIFC1 reduces parasite sensitivity to NHS, but loss of either the ubiquitin ligase or
the conjugase (Tb927.9.8000) sensitises T. b. brucei to NHS. Therefore, while ubiquitination
may have a role to play in determining sensitivity to NHS, in this case, it does not promote it.
In addition, loss of this putative ubiquitination machinery has no detectable effect on TbKIFC1
protein levels. However, changes in ubiquitination status may lead to subtle changes in protein
levels or may affect protein function in other ways. Our EC
50
data suggests that the influence
of TbKIFC1 on apoL1 sensitivity and suramin efficacy is at least partially dependent on
Tb927.10.12940, and previous work indicates that TbVAMP7B expression is influenced by
ubiquitination [45] (Fig 9B).
At first glance, the identification of 63 putative apoL1 sensitivity determinants in our RNAi
library screen suggests apoL1 is a trypanocide that is vulnerable to the development of resis-
tance via multiple loss-of-function mutations. However, while TbKIFC1 RNAi knockdown led
to an approximately six-fold increase in apoL1 EC
50
, the depletion of other factors had a more
limited effect on apoL1 sensitivity (Tb927.9.8000; Tb927.10.12940), or their loss, while reduc-
ing apoL1 sensitivity, led to a significant growth defect (Tb927.9.8000; Tb927.10.14040;
Tb927.10.14890). Paradoxically, the loss of some of these factors rendered T. b. brucei more
sensitive to NHS. Taken together, these data suggest that T. b. brucei has little opportunity to
evolve significant resistance to apoL1 via loss-of-function mutation. The normal association of
apoL1 with two distinct carrier complexes, TLF1 and TLF2, further enhances its trypanolytic
ability, providing an innate combination therapy that can exploit distinct entry mechanisms
and routes through the parasite’s endocytic system to access a range of target membranes.
Therefore, with the notable exception of TbHpHbR in T. b. gambiense, which has a reduced
affinity for TLF1 [20], the development of human serum resistance in African trypanosomes is
primarily dependent on gain-of-function mutation, such as the evolution of SRA in T. b. rho-
desiense [15, 19] and TgsGP in T. b. gambiense [23, 24].
In summary, we have identified and validated a set of novel T. b. brucei apoL1 sensitivity
determinants, revealing key similarities and differences with those parasite factors that support
the trypanocidal effect of human serum. Further work will be required to establish the contri-
bution of these factors to the trypanolytic action of the individual TLFs. Beyond this, our
screen has highlighted an array of proteins with likely roles in the parasite’s endocytic system.
At present, many of these are annotated hypothetical conserved, but future work will seek to
explore their contribution to apoL1 action and to unravel their roles in the endocytic system of
this divergent eukaryote.
Materials and methods
T. b. brucei strains
MITat1.2/2T1 BSF T. b. brucei [43] were maintained in HMI9 supplemented with 10% foetal
calf serum at 37˚C/5% CO
2
. Transfection was carried out in either cytomix or Tb-BSF buffer
[64], for integration at the 2T1 ‘landing pad’ or native loci, respectively, using a Nucleofector
(Lonza) set to programme X-001. Transformants were selected in 2.5 μg.ml
-1
hygromycin,
1 μg.ml
-1
G418 or 10 μg.ml
-1
blasticidin, as appropriate. The BSF T. b. brucei RNAi library was
maintained in 1 μg.ml
-1
phleomycin and 5 μg.ml
-1
blasticidin. For growth assays, cells were
seeded at ~10
5
ml
-1
, counted using a haemocytometer, and diluted back every 24 hours, as nec-
essary, for up to six days in the absence of antibiotics.
ApoL1 and NHS sensitivity assays
ApoL1 was prepared as previously described [38]. NHS (pooled mixed gender; 0.2 μm filtered;
stored at -80˚C in 1 ml aliquots) was purchased from Sera Laboratories International; this batch
Trypanoso ma brucei apolipopro tein-L1 sensitivity determinants
PLOS Pathogens | https:// doi.org/10.13 71/journal.p pat.1006 855 January 18, 2018 18 / 26

was used in our previous NHS RNAi library screen [32]. To determine the half maximal effective
concentration (EC
50
) of NHS and recombinant apoL1, BSF T. b. brucei were seeded at 2x10
3
ml
-1
in 96-well plates in a 2-fold dilution series of NHS or recombinant apoL1, starting from 0.01% or
10 μg.ml
-1
, respectively; assays were carried out in the absence of antibiotics. After ~3 days growth,
resazurin (Sigma) in PBS was added to a final concentration of 12.5 μg.ml
-1
per well, and the plates
incubated for a further 6 hours at 37˚C. Fluorescence was determined using a fluorescence plate
reader (Molecular Devices) at an excitation wavelength of 530 nm, an emission wavelength of 585
nm and a filter cut-off of 570 nm [65]. Data were processed in Excel, and non-linear regression
analysis carried out in GraphPad Prism. The short-term kinetics of killing in high concentration
apoL1 (10 μg.ml
-1
) was determined as previously described [37].
BSF T. b. brucei RNAi library screening and RIT-seq
RNA library screening was carried out as previously described [39]. Briefly, library expression
was induced in 1 μg.ml
-1
tetracycline for 24 hours prior to selection in 2X EC
50
recombinant
apoL1. Cell density was counted daily using a haemocytometer and the total cell number
diluted to no less than 20 million in 100 ml media; induction and apoL1 selection were main-
tained throughout. Once robust growth had been achieved for at least two days, genomic DNA
was prepared for RNAi target identification. The RNAi cassettes remaining in the apoL1-se-
lected RNAi libraries were specifically amplified from genomic DNA using the LIB2F/LIB2R
primers, and sequenced on an Illumina MiSeq platform.
To prepare sequencing libraries, 300 ng of each RNAi library cassette PCR was fragmented
with a Covaris Ultrasonicator using settings optimised to produce a fragment size of <500 bp
(peak incident factor = 50, duty factor = 20%, cycles per burst = 200, for 3 minutes). Fragment
size was confirmed using a Bioanalyzer and High Sensitivity DNA kit (Agilent). Sequencing
libraries were prepared using the TruSeq Nano DNA library preparation kit (Illumina) accord-
ing to manufacturer’s instructions, including a final PCR step to enrich for DNA fragments
with the sequencing adaptor ligated onto each end of the fragment. The final size range of each
sequencing library was measured on a Bioanalyzer, and quantified using a fluorometric quan-
tification assay (Qubit) and quantitative PCR (KAPA Library Quantification kit). Library
DNA concentration was normalised to 10 nM and individual libraries pooled. The pooled
libraries were denatured and diluted to 5 pM, according to manufacturer’s recommendations
(Ilumina MiSeq Reagents kit v2 500 cycles). Pooled libraries were spiked with 50% PhiX (Illu-
mina) due to the low complexity of the samples and a total of 10 pM DNA was loaded onto a
MiSeq flow cell for paired-end sequencing.
The sequenced RNAi target fragments were mapped against the T. b. brucei strain
TREU927 reference genome (release 8.0) using the ‘alternative protocol’, as described [39].
Briefly, mapping was carried out using Bowtie2 [66] set to ‘very sensitive local’ alignment and
output SAM files were processed using SAMtools [67]. The resultant BAM files were viewed
against the reference genome in the Artemis genome browser [68]. Reads containing the RNAi
construct-specific 14-base barcode were identified using a custom script [39], and this subset
of reads were mapped, as above. Plots were derived using the Artemis graph tool and processed
in Adobe Photoshop Elements 8.0. Stacks of reads that included the 14-base barcode on the
positive strand were used to define RNAi target fragment junctions and to assign high-confi-
dence hits as those identified by >1 RNAi target fragment.
Plasmid and strain construction
Stemloop RNAi constructs targeting Tb927.10.14040, Tb927.10.14890, Tb927.9.8000 and
Tb927.10.12940 were assembled in pRPa
iSL
[42]. RNAi targeting fragments were designed
Trypanoso ma brucei apolipopro tein-L1 sensitivity determinants
PLOS Pathogens | https:// doi.org/10.13 71/journal.p pat.1006 855 January 18, 2018 19 / 26

using the RNAit primer design algorithm to minimise off-target effects [69]. pRPa
iSL
con-
structs were linearised with AscI prior to transfection and targeted integration at the rDNA
spacer ‘landing pad’ locus in 2T1 BSF T. b. brucei [43]. Constructs to enable C- or N-terminal
protein tagging of Tb927.10.14040 (x
12MYC
; NsiI) and Tb927.9.8000 (
GFP
x; Acc65I) at the
endogenous loci were assembled in pNAT
BSD
[42]. TbKIFC1 (Tb927.10.14890) was N-termi-
nally tagged at the endogenous locus using pNAT
BSD 6MYC
TbKIFC1 (SphI); plasmid provided
by Klaus Ersfeld, University of Bayreuth, Germany. All constructs were linearised by digestion
with the respective restriction endonuclease prior to transfection into 2T1 BSF T. b. brucei.
For deletion of both copies of Tb927.10.12940, targeting fragments were cloned into pBSD,
and the blasticidin-S-deamina se cassette was then replaced with a neomycin phosphotransfer-
ase cassette to generate pBSDΔ12940 and pNPTΔ12940 constructs. A full-length copy of
Tb927.10.12940 was cloned into pRPa via HindIII/BglII (full length; untagged) or HindIII/XbaI
(minus stop codon; C-terminal GFP) to enable protein overexpression in wild type and
Tb927.10.12940 null 2T1 BSF T. b. brucei. Details of all primers are available on request.
Expression of tagged protein was analysed by SDS-PAGE and western blotting with rabbit
anti-GFP (Molecular Probes) and mouse anti-cMyc (Source BioScience), using standard pro-
tocols [70]. The subcellular localisation of Tb927.10.12940
GFP
and p67 was assessed following
cell fixation in 2% paraformaldehyde in PBS, permeabilisation in 0.5% triton-X100 and incu-
bation with anti-GFP and anti-p67 (Jay Bangs, SUNY Buffalo); bound primary antibodies
were detected with FITC-anti-rabbit and rhodamine-anti-mouse antibodies (Pierce). Slides
were mounted in vectorshield (Vector Laboratories) containing 4’,6-diamidino-2-phen ylin-
dole (DAPI) to enable visualisation of nuclear and kinetoplast DNA.
cDNA synthesis and qPCR analysis
As Tb927.10.12940 tagged at the native locus was undetectable by western blot, we confirmed
knockdown by RT-qPCR. For each cell line and treatment (uninduced and induced), 2 μg
RNA was DNase-treated and reverse-transcribed using the Superscript VILO cDNA synthesis
kit (Invitrogen). 100 ng (RNA-equivalent) cDNA was subjected to qPCR using the Quantitect
SYBR Green PCR kit (Qiagen) and primer pairs specific for telomerase reverse transcriptase
(TERT; Tb927.11.10190) and Tb927.10.12940 (details of primer sequences are available on
request). TERT was used as a reference for normalisation of gene expression, as previously
described [71]. qPCR reactions were carried out in a Rotor-gene 3000 (Corbett Research),
using the following cycling conditions: 95˚C (15 minutes), followed by 40 cycles of 94˚C (15
seconds), 58˚C (30 seconds), and 72˚C (30 seconds). Standard curves, derived from a series of
10-fold dilutions of the target PCR products, were used to determine reaction efficiency. Fold-
change in gene expression was calculated by the ΔΔCt method [72].
Supporting information
S1 Fig. The putative V
0
c V-ATPase subunit (Tb927.10.14040) promotes apoL1 and NHS-
mediated killing of T. b. brucei. (A) Tb927.10.14040 RNAi knockdown in T. b. brucei leads to
a significant growth defect; data derived from three independent cell lines. Inset shows deple-
tion of Tb927.10.14040
12MYC
following RNAi induction in tetracycline (tet) for 24 hours;
Coomassie-stained gel shown for loading. (B) ApoL1 and (C) NHS sensitivity following
Tb927.10.14040 RNAi depletion. Three independent Tb927.10.14040 RNAi cell lines were
induced for 24 hours in 2 ng.ml
-1
tetracycline before exposure to 10 ug.ml
-1
apoL1 or 0.1%
NHS for 24 hours under the same inducing conditions; cell densities were counted at the indi-
cated times using a haemocytometer. Population growth is presented relative to the corre-
sponding untreated culture; error bars, standard deviation; P-values derived from paired
Trypanoso ma brucei apolipopro tein-L1 sensitivity determinants
PLOS Pathogens | https:// doi.org/10.13 71/journal.p pat.1006 855 January 18, 2018 20 / 26

students t-test.
(TIF)
S2 Fig. p67 and ICP, fail to fulfil the stringency criteria for inclusion in the apoL1 RNAi
library ‘hit’ list. Histograms showing RNAi target fragment mapping to (A) the chromosome-
5 region flanking Tb927.5.1810 and Tb927.5.1830 (lysosomal-associate d membrane protein,
p67) and (B) the chromosome-8 region flanking Tb927.8.6450 (‘inhibitor of cysteine pepti-
dase’, ICP) following RNAi library selection in apoL1 and normal human serum (NHS); RNAi
construct-specific barcode-containing reads presented as RPKM (plus 0.1) as per Fig 3A.
(TIF)
S3 Fig. Tb927.10.12940 depletion and Tb927.10.12940
GFP
subcellular localisation. (A)
Cumulative growth following RNAi knockdown of Tb927.10.12940. Inset shows RT-qPCR
quantification of Tb927.10.12940 depletion following targeted RNAi knockdown; three inde-
pendent cell lines induced in 1 μg.ml
-1
tetracycline; red dashed line corresponds to RNA levels
in the absence of RNAi induction. (B) Immunofluorescence localisation of Tb927.10.12940
GFP
;
counter-staining with the DNA intercalating dye, DAPI, reveals the kinetoplast (k) and nucleus
(n).
(TIF)
S4 Fig. Tb927.9.8000 depletion and Tb927.10.12940 deletion does not have an additive
effect on T. b. brucei population growth. (A) Specific RNAi depletion of
GFP
8000 by western
blotting; Coomassie-stained gel shown for loading. (B) Cumulative growth following RNAi
knockdown of Tb927.9.8000 in wild type 2T1 T. b. brucei; three independent cell lines induced
in 1 μg.ml
-1
tetracycline. (C) Cumulative growth following RNAi knockdown of Tb927.9.8000
in 12940 null 2T1 T. b. brucei; four independent cell lines induced in 1 μg.ml
-1
tetracycline. (D)
Chart summarising the impact on population doubling times of Tb927.9.8000 RNAi knock-
down in wild type and Tb927.10.12940 null 2T1 T. b. brucei; data derived from (B) and (C).
Error bars, standard deviation; P-values derived from paired students t-test.
(TIF)
S5 Fig. TbKIFC1 depletion and Tb927.10.12940 deletion does not have an additive effect
on T. b. brucei population growth. (A) Specific RNAi depletion of
6MYC
TbKIFC1; Coomas-
sie-stained gel shown for loading. (B) Cumulative growth following RNAi knockdown of
TbKIFC1 in 2T1 T. b. brucei; three independent cell lines induced in 1 μg.ml
-1
tetracycline. (C)
Cumulative growth following RNAi knockdown of TbKIFC1 in 12940 null 2T1 T. b. brucei;
four independent cell lines induced in 1 μg.ml
-1
tetracycline. (D) Chart summarising the
impact on population doubling times of TbKIFC1 RNAi knockdown in wild type and
Tb927.10.12940 null 2T1 T. b. brucei; data derived from (B) and (C). Error bars, standard devi-
ation; P-values derived from paired students t-test.
(TIF)
S6 Fig. Depletion of Tb927.9.8000 or Tb927.10.12940 has no significant effect on
6MYC
Tb-
KIFC1 expression.
6MYC
TbKIFC1 expression following (A) Tb927.10.12940 and (B)
Tb927.9.8000 RNAi knockdown; Coomassie-stained gels shown for loading.
(TIF)
S1 Table. Genes represented by >99 RNAi construct-specific barcode-containing reads per
kilobase per transcript following RNAi library selection in 2X EC
50
human apoL1. Col-
oured as per Fig 2.
a
Annotations derived from GeneDB, http://www.genedb.org/Homepa ge/
Tbruceibrucei927, 16
th
November 2016.
b
‘Tagged reads’ incorporate a 14-base RNAi con-
struct barcode, GTGAGGCCTCGCGA.
c
‘Tagged reads/kb/mRNA’ plotted in Fig 2A.
d
BSF T.
Trypanoso ma brucei apolipopro tein-L1 sensitivity determinants
PLOS Pathogens | https:// doi.org/10.13 71/journal.p pat.1006 855 January 18, 2018 21 / 26

b. brucei RNAi library fitness ratio derived from reference [41]; three-day induced read count
divided by uninduced read count; the lower the number the greater the fitness cost following
RNAi depletion, whereas a number >1 indicates a gain of fitness.
(XLSX)
S2 Table. RPKM values for genes detailed in S1 Table following RNAi library selection
with 2X EC
50
human apoL1 or normal human serum (NHS). Coloured as per Fig 3A.
a
Annotations derived from GeneDB, http://www.genedb .org/Homepage/Tbruceibrucei927 ,
16
th
November 2016.
b
‘Tagged reads’ incorporate a 14-base RNAi construct barcode,
GTGAGGCCTCGCGA.
c
Sequencing data from reference [32] reanalysed to quantify the
number of tagged reads per kilobase per predicted transcript; output converted to RPKM.
(XLSX)
S3 Table. RPKM values for the top ‘hits’ identified following RNAi library selection with
2X EC
50
normal human serum (NHS) and the corresponding RPKM values following
selection in human apoL1. Coloured as per Fig 3A, highlighting the previously validated T. b.
brucei determinants of human serum sensitivity described in reference [32].
a
Annotations
derived from GeneDB, http://www.genedb.org/H omepage/Tbruceibrucei927, 16
th
November
2016.
b
‘Tagged reads’ incorporate a 14-base RNAi construct barcode, GTGAGGCCTCGCGA.
c
Sequencing data from reference [32] reanalysed to quantify the number of tagged reads per
kilobase per predicted transcript; output converted to RPKM.
d
Number of independent RNAi
fragments targeting each transcript following BSF T. b. brucei RNAi library selection in NHS;
see reference [32].
(XLSX)
S4 Table. UbPred analysis identifies putative ubiquitination sites in putative apoL1-sensi-
tivity determinants.
a
Annotations derived from GeneDB, http://www.genedb.org/
Homepage/Tbruceibrucei927, 16
th
November 2016.
b
Confidence assigned depending on the
UbPred score for each lysine in a protein sequence; low, 0.62  s  0.69; medium, 0.69  s 
0.84; high, 0.84  s  1.00 [46].
(XLSX)
Acknowledgmen ts
Thanks to Professor Klaus Ersfeld for the generous gift of the TbKIFC1 epitope-tagging plas-
mid pNAT
BSD 6MYC
TbKIFC1 and to Professor Jay Bangs for the generous gift of the mouse
anti-p67 antibody.
Author Contributions
Conceptualization: Rachel B. Currier, Sam Alsford.
Data curation: Sam Alsford.
Formal analysis: Rachel B. Currier, Hollie Burrell-Saward, Sam Alsford.
Funding acquisition: Annette MacLeod, Sam Alsford.
Investigation: Rachel B. Currier, Hollie Burrell-Saward, Sam Alsford.
Project administration: Sam Alsford.
Resources: Anneli Cooper, Annette MacLeod.
Supervision: Sam Alsford.
Trypanoso ma brucei apolipopro tein-L1 sensitivity determinants
PLOS Pathogens | https:// doi.org/10.13 71/journal.p pat.1006 855 January 18, 2018 22 / 26

Visualization: Sam Alsford.
Writing – original draft: Rachel B. Currier, Sam Alsford.
Writing – review & editing: Rachel B. Currier, Anneli Cooper, Annette MacLeod, Sam
Alsford.
References
1. Franco JR, Simarro PP, Diarra A, Ruiz-Postig o JA, Jannin JG. The journey towards elimination of gam-
biense human African trypanoso miasis: not far, nor easy. Parasitology. 2014; 141(6):748 –60. https://
doi.org/10.10 17/S0031182 013002102 PMID: 24709291.
2. Steverding D. The history of African trypanoso miasis . Parasit Vectors. 2008; 1(1):3. https://doi.or g/10.
1186/1756-3 305-1-3 PMID: 182755 94; PubMed Central PMCID: PMCPMC2 270819.
3. Simarro PP, Cecchi G, Franco JR, Paone M, Diarra A, Ruiz-Postig o JA, et al. Estimating and mapping
the population at risk of sleeping sickness. PLoS Negl Trop Dis. 2012; 6(10):e185 9. https://doi.or g/10.
1371/journa l.pntd.00 01859 PMID: 231451 92; PubMed Central PMCID: PMCPMC3 493382.
4. Van den Bossch e P, de La Rocque S, Hendrickx G, Bouyer J. A changing environment and the epidemi -
ology of tsetse-tran smitted livestock trypanoso miasis. Trends Parasitol. 2010; 26(5):236– 43. https://
doi.org/10.10 16/j.pt.2010. 02.010 PMID: 20304707.
5. Baker N, de Koning HP, Maser P, Horn D. Drug resistance in African trypanoso miasis: the melarsoprol
and pentamid ine story. Trends Parasit ol. 2013; 29(3):110– 8. https://doi.o rg/10.1016/j.p t.2012.12 .005
PMID: 233755 41; PubMed Central PMCID: PMCPMC3 831158.
6. Giordani F, Morrison LJ, Rowan TG, De Koning HP, Barrett MP. The animal trypanoso miases and their
chemother apy: a review. Parasitology. 2016; 143(14):18 62–89. https://doi.or g/10.101 7/
S003118201 600126 8 PMID: 27719692.
7. Alsford S, Kelly JM, Baker N, Horn D. Genet ic dissection of drug resistance in trypanoso mes. Parasitol-
ogy. 2013; 140(12):14 78–91. https://do i.org/10.1017 /S00311820 1300022X PMID: 23552488; PubMed
Central PMCID: PMCPM C3759293 .
8. Hajduk SL, Moore DR, Vasudeva charya J, Siqueira H, Torri AF, Tytler EM, et al. Lysis of Trypanoso ma
brucei by a toxic subspec ies of human high density lipoprotein. J Biol Chem. 1989; 264(9):521 0–7.
PMID: 249418 3.
9. Raper J, Fung R, Ghiso J, Nussenzweig V, Tomlinson S. Character ization of a novel trypanoso me lytic
factor from human serum. Infect Immun . 1999; 67(4):1910 –6. PMID: 100850 35; PubMed Central
PMCID: PMCPMC9 6545.
10. Rifkin MR. Identificati on of the trypanocid al factor in normal human serum: high density lipoprotein.
Proc Natl Acad Sci U S A. 1978; 75(7):3450 –4. PMID: 210461; PubMed Central PMCID:
PMCPMC3 92795.
11. Tomlinson S, Jansen AM, Koudinov A, Ghiso JA, Choi-Miura NH, Rifkin MR, et al. High-de nsity-lipopro-
tein-indepe ndent killing of Trypanoso ma brucei by human serum. Mol Biochem Parasitol. 1995; 70(1–
2):131–8. PMID: 7637693.
12. Hager KM, Pierce MA, Moore DR, Tytler EM, Esko JD, Hajduk SL. Endocytos is of a cytotoxic human
high density lipoprotein results in disruption of acidic intracellular vesicles and subsequen t killing of Afri-
can trypanoso mes. J Cell Biol. 1994; 126(1):155 –67. PMID: 8027174; PubMed Central PMCID:
PMCPMC2 120100.
13. Molina-Por tela MP, Lugli EB, Recio-Pint o E, Raper J. Trypanoso me lytic factor, a subclas s of high-den-
sity lipoprotein, forms cation-sele ctive pores in membrane s. Mol Biochem Parasit ol. 2005; 144(2):218 –
26. https://doi. org/10.1016/j .molbiopa ra.2005.08.01 8 PMID: 16202458.
14. Perez-Mo rga D, Vanhollebe ke B, Paturiaux-Han ocq F, Nolan DP, Lins L, Homble F, et al. Apolipopr o-
tein L-I promotes trypanoso me lysis by forming pores in lysoso mal membrane s. Science. 2005; 309
(5733):469 –72. https:// doi.org/10.11 26/science. 1114566 PMID: 16020735 .
15. Vanham me L, Paturiaux -Hanocq F, Poelvoorde P, Nolan DP, Lins L, Van Den Abbeele J, et al. Apolipo-
protein L-I is the trypanoso me lytic factor of human serum. Nature. 2003; 422(6927) :83–7. https://doi.
org/10.1038/ nature01461 PMID: 1262143 7.
16. Pays E, Vanhollebe ke B, Vanha mme L, Paturiaux-H anocq F, Nolan DP, Perez-Morga D. The trypanoly-
tic factor of human serum. Nat Rev Microbiol . 2006; 4(6):477–8 6. https://doi.or g/10.1038/n rmicro1428
PMID: 167103 27.
17. Thomson R, Finkelstein A. Human trypanol ytic factor APOL1 forms pH-gated cation-sel ective channels
in planar lipid bilayers: relevan ce to trypanoso me lysis. Proc Natl Acad Sci U S A. 2015; 112(9):289 4–9.
Trypanoso ma brucei apolipopro tein-L1 sensitivity determinants
PLOS Pathogens | https:// doi.org/10.13 71/journal.p pat.1006 855 January 18, 2018 23 / 26

https://doi.or g/10.107 3/pnas.14 21953112 PMID: 257308 70; PubMed Central PMCID:
PMCPMC4 352821.
18. Stephens NA, Hajduk SL. Endoso mal localizatio n of the serum resistance- associated protei n in African
trypanoso mes confers human infectivity . Eukaryot Cell. 2011; 10(8):1023 –33. https://doi.or g/10.1128 /
EC.05112 -11 PMID: 21705681; PubMed Central PMCID: PMCPM C3165451 .
19. Xong HV, Vanhamme L, Chamekh M, Chimfwembe CE, Van Den Abbeele J, Pays A, et al. A VSG
expression site-assoc iated gene confers resistance to human serum in Trypanoso ma rhodesiens e.
Cell. 1998; 95(6):839– 46. Epub 1998/12 /29. doi: pii: S0092-867 4(00)8170 6-7. PMID: 986570 1.
20. DeJesus E, Kieft R, Albright B, Stephens NA, Hajduk SL. A single amino acid substitution in the group 1
Trypanoso ma brucei gambiense haptoglobin- hemoglo bin receptor abolishes TLF-1 binding. PLoS
Pathogens . 2013; 9(4):e1003 317. https:// doi.org/10.13 71/journal.p pat.1003 317 PMID: 236376 06;
PubMed Central PMCID: PMC363016 2.
21. Kieft R, Capewell P, Turner CM, Veitch NJ, MacLeod A, Hajduk S. Mechanism of Trypanoso ma brucei
gambien se (group 1) resistance to human trypanosome lytic factor. Proc Natl Acad Sci U S A. 2010;
107(37):16 137–41. Epub 2010/09 /02. https://do i.org/10.1073 /pnas.100 7074107 pii: 100707 4107.
PMID: 208055 08.
22. Symula RE, Beade ll JS, Sistrom M, Agbebak un K, Balmer O, Gibson W, et al. Trypanoso ma brucei
gambien se group 1 is distingui shed by a unique amino acid substitution in the HpHb receptor implicated
in human serum resistance. PLoS Negl Trop Dis. 2012; 6(7):e172 8. https://doi.or g/10.1371/ journal.
pntd.000 1728 PMID: 22802982; PubMed Central PMCID: PMCPM C3393672 .
23. Capewell P, Clucas C, Dejesus E, Kieft R, Hajduk S, Veitch N, et al. The TgsGP gene is essential for
resistance to human serum in Trypanoso ma brucei gambien se. PLoS Pathog ens. 2013; 9(10):
e1003686. Epub 2013 Oct 3. https://doi.or g/10.137 1/journal.pp at.10036 86 PMID: 24098129; PubMed
Central PMCID: PMC3 789759.
24. Uzureau P, Uzureau S, Lecordier L, Fontaine F, Tebabi P, Homb le F, et al. Mechanism of Trypanoso ma
brucei gambien se resistance to human serum. Nature. 2013; 501(7467) :430–4. https://doi.or g/10.1038/
nature12516 PMID: 23965626.
25. Horn D. Antigenic variation in African trypanoso mes. Mol Biochem Parasit ol. 2014; 195(2):123 –9.
https://doi.or g/10.101 6/j.molbio para.2014.05 .001 PMID: 24859277; PubMed Central PMCID:
PMCPMC4 155160.
26. Bullard W, Kieft R, Capewell P, Veitch NJ, Macleod A, Hajduk SL. Haptoglob in-hemoglobi n receptor
independent killing of African trypanoso mes by human serum and trypanoso me lytic factors. Virulence.
2012; 3(1):72–6. https:// doi.org/10.41 61/viru.3 .1.18295 PMID: 22286709; PubMed Central PMCID:
PMC333715 3.
27. Drain J, Bishop JR, Hajduk SL. Haptoglob in-related protein mediates trypanoso me lytic factor binding
to trypanoso mes. J Biol Chem. 2001; 276(32):30 254–60. https://do i.org/10.1074 /jbc.M01019 8200
PMID: 113528 98.
28. Higgins MK, Tkach enko O, Brown A, Reed J, Raper J, Carring ton M. Structure of the trypanoso me hap-
toglobin-he moglobi n receptor and implication s for nutrient uptake and innate immunity . Proc Natl Acad
Sci U S A. 2013; 110(5):190 5–10. https:// doi.org/10.10 73/pnas.1 214943110 PMID: 23319650; PubMed
Central PMCID: PMCPM C3562850 .
29. Lane-Ser ff H, MacGregor P, Lowe ED, Carrington M, Higgins MK. Structural basis for ligand and innate
immunity factor uptake by the trypanoso me haptoglobin- haemoglobin receptor . Elife. 2014; 3:e0555 3.
https://doi.or g/10.755 4/eLife.05553 PMID: 25497229; PubMed Central PMCID: PMCPM C4383175 .
30. Vanhollebe ke B, De Muylder G, Nielsen MJ, Pays A, Tebabi P, Dieu M, et al. A haptoglobin- hemoglo bin
receptor convey s innate immunity to Trypanoso ma brucei in humans. Science. 2008; 320(5876) :677–
81. https://doi. org/10.1126/s cience.115 6296 PMID: 18451305.
31. Vanhollebe ke B, Pays E. The trypanolytic factor of human serum: many ways to enter the parasite, a
single way to kill. Mol Microbiol . 2010; 76(4):806– 14. Epub 2010/04 /20. https://doi. org/10.1111/j .1365-
2958.2010. 07156.x pii: MMI71 56. PMID: 20398209.
32. Alsford S, Currier RB, Guerra-As suncao JA, Clark TG, Horn D. Cathepsin- L can resist lysis by human
serum in Trypanoso ma brucei brucei. PLoS Pathogens. 2014; 10(5):e100 4130. https://doi.o rg/10.1371/
journal.ppa t.100413 0 PMID: 24830321; PubMed Central PMCID: PMCPM C4022737 .
33. Santos CC, Coombs GH, Lima AP, Mottram JC. Role of the Trypanoso ma brucei natural cystein e pepti-
dase inhibit or ICP in differentiation and virulence. Mol Microbiol. 2007; 66(4):991– 1002. Epub 2007/10/
20. https://doi. org/10.1111/j .1365-2958. 2007.05970.x pii: MMI5970. PMID: 179448 30.
34. Peck RF, Shiflett AM, Schwartz KJ, McCann A, Hajduk SL, Bangs JD. The LAMP-like protein p67 plays
an essential role in the lysosome of African trypanoso mes. Mol Microbiol . 2008; 68(4):933– 46. Epub
2008/04/ 24. https://doi.or g/10.111 1/j.1365-295 8.2008.06 195.x pii: MMI6195. PMID: 18430083.
Trypanoso ma brucei apolipopro tein-L1 sensitivity determinants
PLOS Pathogens | https:// doi.org/10.13 71/journal.p pat.1006 855 January 18, 2018 24 / 26

35. Alsford S. Increased Trypanoso ma brucei cathepsin- L activity inhibits human serum-med iated trypano-
lysis. Microb Cell. 2014; 1(8):270–2 . https://doi.or g/10.156 98/mic2014 .08.162 PMID: 27441199;
PubMed Central PMCID: PMCPMC4 948671.
36. Lecordier L, Uzureau P, Tebabi P, Perez-Morga D, Nolan D, Schumann Burkard G, et al. Identificati on
of Trypanoso ma brucei components involved in trypanol ysis by normal human serum. Mol Microbiol .
2014; 94(3):625– 36. https://doi.or g/10.1111/ mmi.12783 PMID: 25256834.
37. Vanwall eghem G, Fontaine F, Lecordier L, Tebabi P, Klewe K, Nolan DP, et al. Coupling of lysoso mal
and mitochondr ial membrane permeabiliz ation in trypanolysis by APOL1. Nat Commun . 2015; 6:8078.
https://doi.or g/10.103 8/ncomms 9078 PMID: 26307671 ; PubMed Central PMCID: PMCPMC4 560804.
38. Cooper A, Capewell P, Clucas C, Veitch N, Weir W, Thomson R, et al. A primate APOL1 variant that
kills Trypanoso ma brucei gambien se. PLoS Negl Trop Dis. 2016; 10(8):e000 4903. https://doi.or g/10.
1371/journa l.pntd.00 04903 PMID: 274942 54; PubMed Central PMCID: PMCPMC4 975595.
39. Glover L, Alsford S, Baker N, Turner DJ, Sanche z-Flores A, Hutchi nson S, et al. Genom e-scale RNAi
screens for high-throu ghput phenotyp ing in bloodstream -form African trypanoso mes. Nat Protoc. 2015;
10(1):106– 33. https://d oi.org/10.103 8/nprot.2 015.005 PMID: 25502887 .
40. Alsford S, Eckert S, Baker N, Glover L, Sanchez- Flores A, Leung KF, et al. High-throughp ut decoding of
antitrypa nosomal drug efficacy and resistance. Nature. 2012; 482(7384) :232–6. Epub 2012/01/27.
https://doi.or g/10.103 8/nature1077 1 pii: nature10 771. PMID: 22278056.
41. Alsford S, Turner DJ, Obado SO, Sanche z-Flores A, Glover L, Berriman M, et al. High-thr oughput phe-
notyping using parallel sequencin g of RNA interference targets in the African trypanoso me. Genome
Res. 2011; 21(6):915– 24. Epub 2011/03/03. https:// doi.org/10.11 01/gr.11 5089.110 pii: gr.115089.11 0.
PMID: 213639 68.
42. Alsford S, Horn D. Single-loc us targeting constructs for reliable regulated RNAi and transgene expres-
sion in Trypanoso ma brucei. Mol Biochem Parasi tol. 2008; 161(1):76– 9. Epub 2008/07 /01. https://doi.
org/10.1016/ j.molbiopara.2 008.05.0 06 pii: S0166-685 1(08)0013 6-9. PMID: 1858891 8.
43. Alsford S, Kawahar a T, Glover L, Horn D. Tagging a Trypanoso ma brucei RRNA locus improves stable
transfection efficiency and circumvents inducible expression position effects . Mol Biochem Parasitol.
2005; 144(2):142 –8. Epub 2005/09/27. https:// doi.org/10.10 16/j.molbi opara.2005.0 8.009 pii: S0166-
6851(05)0 0250-1. PMID: 161823 89.
44. Stach L, Freemont PS. The AAA+ ATPase p97, a cellular multitool. Biochem J. 2017; 474(17):29 53–76.
https://doi.or g/10.104 2/BCJ20160 783 PMID: 288190 09.
45. Zoltner M, Leung KF, Alsford S, Horn D, Field MC. Modulatio n of the Surface Proteome through Multiple
Ubiquitylatio n Pathways in African Trypanoso mes. PLoS Pathogens . 2015; 11(10):e10 05236. https://
doi.org/10.13 71/journal.p pat.1005236 PMID: 26492041; PubMed Central PMCID: PMCPM C4619645 .
46. Radivojac P, Vacic V, Haynes C, Cocklin RR, Mohan A, Heyen JW, et al. Identificatio n, analysis, and
prediction of protein ubiquitinatio n sites. Proteins. 2010; 78(2):365– 80. https://doi.or g/10.100 2/prot.
22555 PMID: 197222 69; PubMed Central PMCID: PMCPMC3 006176.
47. Zheng N, Shabek N. Ubiquitin Ligases: Structure, Function, and Regulatio n. Annu Rev Biochem. 2017;
86:129–57. https://doi.or g/10.1146/ annurev-bio chem-060 815-014922 PMID: 28375744 .
48. Raper J, Nussenzweig V, Tomlins on S. Lack of correlation between haptoglobin concentra tion and try-
panolytic activity of normal human serum. Mol Biochem Parasi tol. 1996; 76(1–2):33 7–8. PMID:
8920024.
49. Baker N, Hamilton G, Wilkes JM, Hutchinso n S, Barrett MP, Horn D. Vacuola r ATPase depletion affects
mitochondr ial ATPase function, kinetopla st depend ency, and drug sensitivity in trypanoso mes. Proc
Natl Acad Sci U S A. 2015; 112(29):91 12–7. https:// doi.org/10.10 73/pnas.1 505411112 PMID:
26150481; PubMed Central PMCID: PMCPM C4517229 .
50. Sorkin A, Von Zastrow M. Signal transductio n and endocytosis : close encounters of many kinds. Nat
Rev Mol Cell Biol. 2002; 3(8):600–1 4. https:// doi.org/10.10 38/nrm88 3 PMID: 12154371.
51. McCann AK, Schwartz KJ, Bangs JD. A determination of the steady state lysosoma l pH of bloodstream
stage African trypanoso mes. Mol Biochem Parasitol. 2008; 159(2):146 –9. https://doi.or g/10.101 6/j.
molbiop ara.2008.02.0 03 PMID: 183591 05; PubMed Central PMCID: PMCPMC2 423349.
52. Ward DM, Pevsner J, Scullio n MA, Vaughn M, Kaplan J. Syntaxin 7 and VAMP-7 are soluble N-ethyl-
maleimide -sensitive factor attachment protein receptors required for late endosome-ly sosome and
homotypic lysoso me fusion in alveolar macropha ges. Mol Biol Cell. 2000; 11(7):2327 –33. PMID:
10888671; PubMed Central PMCID: PMCPM C14922.
53. Weir ML, Xie H, Klip A, Trimble WS. VAP-A binds promiscuou sly to both v- and tSNAREs . Biochem Bio-
phys Res Commun. 2001; 286(3):616 –21. https://doi. org/10.1006/b brc.2001 .5437 PMID: 115111 04.
54. Genoves e G, Friedman DJ, Ross MD, Lecordier L, Uzureau P, Freedma n BI, et al. Association of trypa-
nolytic ApoL1 variants with kidney disease in African American s. Science. 2010; 329(5993) :841–5.
Trypanoso ma brucei apolipopro tein-L1 sensitivity determinants
PLOS Pathogens | https:// doi.org/10.13 71/journal.p pat.1006 855 January 18, 2018 25 / 26

https://doi.or g/10.112 6/science.119 3032 PMID: 20647424; PubMed Central PMCID:
PMCPMC2 980843.
55. Beckerman P, Bi-Karchin J, Park AS, Qiu C, Dummer PD, Soomro I, et al. Transgen ic expression of
human APOL1 risk variants in podocyt es induces kidney disease in mice. Nat Med. 2017; 23(4):429–
38. https://doi. org/10.1038/n m.4287 PMID: 2821891 8.
56. Madhavan SM, O’Toole JF, Konieczko wski M, Barison i L, Thomas DB, Ganesa n S, et al. APOL1 vari-
ants change C-termina l conformatio nal dynamics and binding to SNARE protein VAMP8. JCI Insight.
2017; 2(14):e925 81. https://doi.or g/10.1172/ jci.insight.9 2581 PMID: 28724794; PubMed Central
PMCID: PMCPMC5 518555.
57. Andersen JP, Vestergaard AL, Mikkelse n SA, Mogensen LS, Chalat M, Molday RS. P4-ATPases as
Phospho lipid Flippases- Structur e, Function, and Enigmas. Front Physiol. 2016; 7:275. https:// doi.org/
10.3389/ fphys.2016.0 0275 PMID: 274583 83; PubMed Central PMCID: PMCPMC4 937031.
58. Harrington JM, Howell S, Hajduk SL. Membrane permeabilizat ion by trypanoso me lytic factor, a cyto-
lytic human high density lipoprotein. J Biol Chem. 2009; 284(20):13 505–12. https://doi.or g/10.1074/ jbc.
M900151 200 PMID: 19324878; PubMed Central PMCID: PMCPMC2 679451.
59. Engstler M, Pfohl T, Hermingha us S, Boshart M, Wiegertjes G, Hedderg ott N, et al. Hydrodyn amic flow-
mediated protein sorting on the cell surface of trypanosome s. Cell. 2007; 131(3):505 –15. https://doi.
org/10.1016/ j.cell.2007.08 .046 PMID: 17981118.
60. Manna PT, Boehm C, Leung KF, Natesan SK, Field MC. Life and times: synthe sis, trafficking, and evo-
lution of VSG. Trends Parasitol. 2014; 30(5):251– 8. https:// doi.org/10.10 16/j.pt.20 14.03.004 PMID:
24731931; PubMed Central PMCID: PMCPM C4007029 .
61. Kerscher O, Felberba um R, Hochstras ser M. Modification of proteins by ubiquit in and ubiquitin-like pro-
teins. Annu Rev Cell Dev Biol. 2006; 22:159– 80. https://doi.or g/10.114 6/annurev.c ellbio.22.010 605.
093503 PMID: 167530 28.
62. Chung WL, Leung KF, Carrington M, Field MC. Ubiquitylatio n is required for degradat ion of transmem-
brane surface proteins in trypanoso mes. Traffic. 2008; 9(10):1681 –97. https:// doi.org/10.11 11/j.160 0-
0854.2008. 00785.x PMID: 18657071.
63. Leung KF, Riley FS, Carrington M, Field MC. Ubiquitylatio n and develop mental regulation of invariant
surface protein expression in trypanoso mes. Eukaryot Cell. 2011; 10(7):916– 31. https://doi.or g/10.
1128/EC.0 5012-11 PMID: 215719 21; PubMed Central PMCID: PMCPMC3 147413.
64. Schumann Burkard G, Jutzi P, Roditi I. Genome-w ide RNAi screens in bloodstream form trypanoso mes
identify drug transporters. Mol Biochem Parasitol. 2011; 175(1):91– 4. https:/ /doi.org/10.10 16/j.
molbiop ara.2010.09.0 02 PMID: 208517 19.
65. Raz B, Iten M, Grether-Buhl er Y, Kaminsky R, Brun R. The Alamar Blue assay to determine drug sensi-
tivity of African trypanoso mes (T. b. rhodesi ense and T. b. gambiense ) in vitro. Acta Trop. 1997; 68
(2):139–47 . PMID: 938678 9.
66. Langmea d B, Trapnell C, Pop M, Salzberg SL. Ultrafas t and memory-effi cient alignment of short DNA
sequences to the human genome. Genom e biology. 2009; 10(3):R2 5. https://doi.or g/10.118 6/gb-2009-
10-3-r25 PMID: 19261174; PubMed Central PMCID: PMC269 0996.
67. Li H, Handsaker B, Wysoke r A, Fennell T, Ruan J, Homer N, et al. The Sequenc e Alignment/M ap format
and SAMtoo ls. Bioinformat ics. 2009; 25(16):207 8–9. https://doi.or g/10.109 3/bioinforma tics/btp352
PMID: 195059 43; PubMed Central PMCID: PMC272300 2.
68. Rutherfor d K, Parkhill J, Crook J, Horsnell T, Rice P, Rajandream MA, et al. Artemis: sequence visuali-
zation and annotation. Bioinform atics. 2000; 16(10):944 –5. PMID: 111206 85.
69. Redmond S, Vadivel u J, Field MC. RNAit: an automated web-based tool for the selection of RNAi tar-
gets in Trypanoso ma brucei. Mol Biochem Parasitol. 2003; 128(1):115 –8. PMID: 12706807.
70. Ausubel FM, Brent R, Kingston RE, Moore DD, Seidman JG, Smith JA, et al. Current Protocols in
Molecular Biology. USA: John Wiley and Sons, Inc.; 1998.
71. Brenndor fer M, Boshar t M. Selectio n of reference genes for mRNA quantifi cation in Trypanoso ma bru-
cei. Mol Biochem Parasitol. 2010; 172(1):52– 5. https://doi.or g/10.1016/ j.molbiopara.2 010.03.0 07
PMID: 203028 89.
72. Livak KJ, Schmittgen TD. Analysis of relative gene expression data using real-tim e quantitativ e PCR
and the 2(-Delta Delta C(T)) Method. Methods. 2001; 25(4):402– 8. https:// doi.org/10.10 06/meth.20 01.
1262 PMID: 118466 09.
Trypanoso ma brucei apolipopro tein-L1 sensitivity determinants
PLOS Pathogens | https:// doi.org/10.13 71/journal.p pat.1006 855 January 18, 2018 26 / 26
