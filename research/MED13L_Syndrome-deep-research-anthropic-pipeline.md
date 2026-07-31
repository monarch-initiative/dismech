# MED13L Syndrome — Anthropic systematic-review pipeline output

**Provider:** Anthropic Claude systematic-review pipeline (multi-phase: literature
retrieval, structured curation, claim-triple verification).
**Subject:** MED13L syndrome (MRFACD), MONDO:0014773
**Run date:** 2026-06-24 (MED13) / 2026-06-23 (MED13L); artifacts received 2026-07-09.
**Deposited:** 2026-07-30, as the source artifact for dismech PR #7186.

> **AI-Generated Content — Not Medical Advice.** This document was generated with
> substantial AI assistance and is not medical advice. It is a research literature
> synthesis intended for scientific and educational use. It has not been independently
> reviewed by a licensed physician for clinical accuracy and must not be used as a
> substitute for professional medical advice, diagnosis, or treatment. AI systems can
> produce errors, including plausible-sounding statements that are incorrect; verify
> every claim against the cited primary literature before use.

## How this artifact was used

The dismech repository was **held out** during this pipeline run — no sub-agent fetched
or read `kb/disorders/MED13_Syndrome.yaml` or the rendered dismech site. The two
curations are therefore independent, and their overlap is convergent evidence rather
than derivation.

**Critical caveat for anyone reusing this file.** The pipeline's own provenance block
states its evidence snippets are *"verbatim spans from the post-P19 review.md, not from
source abstracts"*. They are therefore **not** valid dismech evidence snippets and must
not be copied into a KB entry. Every claim curated into dismech from this artifact was
re-derived against PubMed abstracts (and cached full text where available) using
`linkml-reference-validator`. Claims whose only support was a pipeline snippet absent
from the cited source were dropped rather than reworded. See PR #7186 for the full
list of what was dropped and why.

References here are given as DOIs; dismech requires PMIDs. 74 of 78 DOIs resolved to
PubMed records; the four that did not are listed in the PR description.

---

# Part 1 — Curation preview (DisMech format)

## Description AI-GENERATED 

MED13L syndrome is an autosomal dominant neurodevelopmental disorder caused by heterozygous, predominantly de novo, loss-of-function or missense variants in MED13L, which encodes a subunit of the CDK8 kinase module of the Mediator transcriptional coactivator complex. The phenotype comprises moderate intellectual disability, marked speech delay, hypotonia, a recognisable facial gestalt, and variable congenital heart defects. Missense variants are associated with a more severe presentation including epilepsy, and the disorder belongs to the broader CDK8-module Mediatorpathy spectrum.

Parents: MONDO:0002320MONDO:0015159MONDO:0100547MONDO:0100601

## AI-generated mechanistic hypotheses AI-GENERATED (5)

These 5 hypotheses are the pipeline's integrative reasoning layer: each synthesises across the mechanism nodes below to propose a testable claim. Per-citation context (DisMech explanation) is collapsed under each evidence item, not shown as headline reasoning.

### MED13L haploinsufficiency (dosage loss) is the primary disease mechanismCANONICALAI reasoning

Heterozygous deletion, frameshift, nonsense and canonical-splice variants reduce functional MED13L dosage below a developmental threshold, dysregulating CKM-gated Mediator transcription. Supported by the predominance of LoF alleles in patients, the recognisable phenotype across deletion and truncating cases, and recapitulation in Med13l+/- mice with embryonic lethality of the null.

Applies to: LoF (deletion/truncating/splice)

Evidence: for 4 · against 1

4 supporting citations

“Results: The 17 kb out-of-frame de novo deletion encompassing exon 2 of MED13L (MIM *608771) in patient 56366, together with overlapping cases, were instrumental to define a recognisable haploinsufficiency syndrome that we reported and discussed in detail elsewhere.”
de novo intragenic deletion defines recognisable haploinsufficiency syndrome
literature · 10.1136/jmedgenet-2014-102588

“The first patient has a de novo mutation in the splice acceptor site of exon 5 of MED13L. cDNA analysis showed this mutation results in an in-frame deletion, removing 15 amino acids in middle of the conserved MED13L N-terminal domain.”
splice and exonic deletion alleles confirm haploinsufficiency phenotype
literature · 10.1038/ejhg.2014.69

“Results: Due to embryonic lethality, we characterize the Med13l heterozygous germline deletion (Figure 1E).”
Med13l null is embryonic lethal; heterozygote phenocopies syndrome
literature · 10.1002/dvdy.70079

“Congenital cardiac and neurodevelopmental deficits have been recently linked to the mediator complex subunit 13-like protein MED13L, a subunit of the CDK8-associated mediator complex that functions in transcriptional regulation through DNA-binding transcription factors and RNA polymerase II.”
haploinsufficiency causes the cardiac+neurodevelopmental phenotype
literature · 10.1038/ejhg.2015.26

1 contrary citation

“We found that patients carrying missense mutations had more frequently epilepsy and showed a more severe phenotype.”
missense carriers show a more severe phenotype than expected from pure dosage loss
literature · 10.1007/s10048-018-0541-0

### Subset of recurrent missense variants act via dominant-negative or neomorphic gain-of-functionEMERGINGAI reasoning

Recurrent missense variants (notably p.Pro869Ser) retain stable nuclear expression yet associate with a more severe, epilepsy-enriched phenotype than truncating alleles, consistent with a dominant-negative or neomorphic effect on the assembled CKM rather than simple dosage loss.

Applies to: missense (exon-15 hotspot, C-terminal)

Evidence: for 3 · against 2

3 supporting citations

“Discussion: We observed that the p.Pro866Leu mutant variant shared similarities with the other studied variants—p.Cys1131Tyr, p.Gly1899Arg, and p.Thr2162Met—with cytoplasmic localization and protein instability, consistent with a loss-of-function pathogenic mechanism, while p.Pro869Ser exhibited more stable protein expression and partial nuclear localization, closely resembling the WT condition, arguing for the dominant-negative effect of the mutant protein or the possibility of a neomorphic effect with dominant or semi-dominant properties.”
p.Pro869Ser stable+nuclear, arguing for dominant-negative/neomorphic effect
literature · 10.1016/j.xhgg.2025.100467

“We found that patients carrying missense mutations had more frequently epilepsy and showed a more severe phenotype.”
missense → more frequent epilepsy and more severe phenotype
literature · 10.1007/s10048-018-0541-0

“Discussion: Our case further demonstrates that Pro869Ser is a hotspot mutation of the MED13L gene.”
Pro869Ser is a recurrent hotspot mutation
literature · 10.1186/s13052-020-00847-y

2 contrary citations

“Discussion: We observed that the p.Pro866Leu mutant variant shared similarities with the other studied variants—p.Cys1131Tyr, p.Gly1899Arg, and p.Thr2162Met—with cytoplasmic localization and protein instability, consistent with a loss-of-function pathogenic mechanism, while p.Pro869Ser exhibited more stable protein expression and partial nuclear localization, closely resembling the WT condition, arguing for the dominant-negative effect of the mutant protein or the possibility of a neomorphic effect with dominant or semi-dominant properties.”
four other missense variants behave as LoF (cytoplasmic, unstable)
literature · 10.1016/j.xhgg.2025.100467

“Notably, our in silico modelling predicted this missense mutation to decrease the stability of an alpha-helix and thereby affecting the MED13L secondary structure, while the majority of published missense mutations remain variants of uncertain significance.”
missense variant predicted to destabilise structure (LoF-like)
literature · 10.1016/j.ejmg.2017.06.004

### MED13L missense variants cause isolated dextro-transposition of the great arteriesREFUTEDAI reasoning

The founding 2003 PROSIT240 study reported MED13L missense variants in 3/97 isolated d-TGA patients, proposing MED13L as a conotruncal-CHD gene. Subsequent syndromic cohorts show low CHD penetrance, no isolated-d-TGA enrichment, and the original missense alleles are now classified as VUS — the association has not replicated and is regarded as the historical entry point to the gene.

Applies to: isolated d-TGA

Evidence: for 1 · against 3

1 supporting citation

“In addition, we identify as Mediator-associated proteins the CDK8-like cyclin-dependent kinase CDK11 and the TRAP240-like KIAA1025 protein (MED13L), which is mutated in patients with the congenital heart defect transposition of the great arteries (TGA).”
MED13L (KIAA1025) noted as mutated in TGA patients (citing the founding study)
literature · 10.1016/j.molcel.2004.05.006

3 contrary citations

“Congenital cardiac and neurodevelopmental deficits have been recently linked to the mediator complex subunit 13-like protein MED13L, a subunit of the CDK8-associated mediator complex that functions in transcriptional regulation through DNA-binding transcription factors and RNA polymerase II.”
redefinition of MED13L syndrome as a neurodevelopmental haploinsufficiency disorder; cardiac defects variable
literature · 10.1038/ejhg.2015.26

“Notably, our in silico modelling predicted this missense mutation to decrease the stability of an alpha-helix and thereby affecting the MED13L secondary structure, while the majority of published missense mutations remain variants of uncertain significance.”
majority of published missense variants remain VUS
literature · 10.1016/j.ejmg.2017.06.004

“The first patient has a de novo mutation in the splice acceptor site of exon 5 of MED13L. cDNA analysis showed this mutation results in an in-frame deletion, removing 15 amino acids in middle of the conserved MED13L N-terminal domain.”
LoF alleles cause syndromic ID, not isolated d-TGA
literature · 10.1038/ejhg.2014.69

### MED13 paralogue partially compensates for MED13L loss (and vice versa)EMERGINGAI reasoning

MED13 and MED13L are mutually exclusive in the CKM and show compensatory upregulation in knockout models, buffering some MED13L-dependent functions; incomplete compensation may explain variable expressivity (e.g. cardiac penetrance) and is a candidate therapeutic axis.

Applies to: all

Evidence: for 3 · against 2

3 supporting citations

“The difference between these two phenotypes may be explained by the compensatory upregulation of Med13l , a Med13 paralog, which develops in MED13 KOs during a rather long transcriptionally active stage of oocyte growth. However, postimplantation development is not rescued by MED13L [ 31 ].”
Med13l compensatorily upregulates in MED13 KOs during oocyte growth
literature · 10.3390/ijms24119330

“Clones generated for cryo-EM: However, probably because CH12 cells also express med13L , this strategy did not improve the purification and thus was unnecessary and omitted in other mutants.”
MED13L expression buffers MED13 knockout in CH12 cells
literature · 10.1016/j.cell.2019.07.011

“Interestingly, 3 subunits of the kinase module have undergone independent gene duplications in vertebrates to generate the paralog pairs MED12/MED12L, MED13/ MED13L, and CDK8/CDK19.”
MED13/MED13L are vertebrate paralogue pair from independent gene duplication
literature · 10.4172/jpb.s2-004

2 contrary citations

“The difference between these two phenotypes may be explained by the compensatory upregulation of Med13l , a Med13 paralog, which develops in MED13 KOs during a rather long transcriptionally active stage of oocyte growth. However, postimplantation development is not rescued by MED13L [ 31 ].”
MED13L does not rescue postimplantation development in MED13 KO
literature · 10.3390/ijms24119330

“Results: The preponderance of MED13 crosslinks over MED13L ones is likely explained by a report indicating that MED13 preferentially associates with CKM-MED, while MED13L is present in complexes that also contain MED26 35 .”
MED13 preferentially associates with CKM-MED while MED13L is in MED26-containing complexes (non-equivalent roles)
literature · 10.1016/j.molcel.2024.06.006

### Aberrant cytoplasmic cyclin C release drives mitochondrial fragmentation contributing to neuronal dysfunctionEMERGINGAI reasoning

Loss of the MED13L nuclear anchor releases cyclin C to the cytoplasm in unstressed patient fibroblasts, triggering mitochondrial fission, reduced respiration and ATP output; if operative in neurons this would link MED13L haploinsufficiency to a metabolic component of the ID phenotype.

Applies to: LoF (deletion/truncating/splice)

Evidence: for 3 · against 2

3 supporting citations

“Cyclin C exhibits aberrant cytoplasmic localization in unstressed MED13L S1497 F/fs fibroblasts: MED13L +/ fs cells exhibit cyclin C nuclear release and mitochondrial dysfunction”
MED13L+/fs fibroblasts show cytoplasmic cyclin C and mitochondrial dysfunction
literature · 10.1016/j.isci.2022.103823

“5.4. Diseases Associated with MED13 Biology: In MED13L, mutant fibroblast cyclin C is aberrantly released into the cytoplasm, leading to mitochondrial fragmentation and increased mitochondrial dysfunction [ 303 ].”
cyclin C release leads to mitochondrial fragmentation in MED13L mutant fibroblasts
literature · 10.3390/cells14090636

“MED13L syndrome mechanism: It is hypothesized that in MED13L Haploinsufficiency Syndrome, the transcriptional process related to the mediator complex interaction with RNA polymerase II may be disrupted. Cyclin C is aberrantly released into the cytoplasm, increasing susceptibility to cell death through mitochondrial fragmentation, decreased oxygen consumption as well as decreased ATP production. 50 , 53”
cyclin C release decreases oxygen consumption and ATP production
literature · 10.1177/26330040241290252

2 contrary citations

## Pathophysiology AI-CURATED (6 mechanism nodes)

### mn-ckm-hinge high

MED13L (with its paralogue MED13) is the physical hinge of the Mediator CDK8 kinase module (CKM): it carries an Argonaute-like fold whose large intrinsically disordered region forms the sole CKM contact with core Mediator and sterically occludes the RNA Pol II / MED26 binding surface, so MED13L abundance and integrity gate reversible CKM-core docking and the switch between Mediator's repressive and activating states.

Causes →: mn-haploinsufficiencymn-fbw7-turnover

Genes: HGNC:22962HGNC:22474HGNC:11957HGNC:1779HGNC:1581

Gene products: MED13LMED13MED12CDK8Cyclin C

GO process: GO:0006366

GO function: GO:0003713

Complexes: CKM (CDK8 kinase module)Mediator complex

Structures: AF-Q71F56-F1

5 evidence

“The structure of the dissociable CKM: Despite exhibiting low sequence homology to classical Argonaute (Ago) proteins, the Med13 possesses an Ago-like architecture, comprising four globular domains (N, PAZ, MID and PIWI) and two linker domains (L1 and L2) ( Figure 3d )[ 42 ].”
MED13/MED13L has Argonaute-like four-domain architecture forming the CKM hinge
literature · 10.1016/j.sbi.2024.102892

“Architecture of human CKM: Notably, MED13 harbors a large and unique insertion between its PAZ and L2 domains, corresponding to its large IDR (residues 350 – 1069) ( Figures 2A and 2C ).”
MED13 IDR occludes Pol II/MED26 binding surface on core Mediator
literature · 10.1016/j.molcel.2024.09.001

“Kinase module function and regulation The Mediator kinase module (~430 kDa in yeast; ~560 kDa in humans) is nominally comprised of four subunits: MED13, MED12, CycC and CDK8, with paralogs of all but CycC identified in humans and some vertebrates (discussed below) ( Borggrefe et al. , 2002 ; Bourbon, 2008 ; Hengartner et al. , 1995 ; Sato et al. , 2004 ).”
kinase module = MED13/MED12/CycC/CDK8 with vertebrate paralogues
literature · 10.3109/10409238.2015.1064854

“Congenital cardiac and neurodevelopmental deficits have been recently linked to the mediator complex subunit 13-like protein MED13L, a subunit of the CDK8-associated mediator complex that functions in transcriptional regulation through DNA-binding transcription factors and RNA polymerase II.”
MED13L is a CDK8-associated Mediator subunit linked to cardiac and neurodevelopmental deficits
literature · 10.1038/ejhg.2015.26

AlphaFold model for UniProt:Q71F56 (MED13L, mediator complex subunit 13L)
structure of MED13L
database · alphafold · AF-Q71F56-F1

### mn-haploinsufficiency high

Heterozygous loss-of-function alleles (whole-gene/intragenic deletions, frameshift, nonsense, canonical splice) halve functional MED13L dosage, reducing the pool of intact CKM available to dock with core Mediator and dysregulating Pol II-dependent transcriptional programmes during development. Heterozygous deletion is sufficient to produce the phenotype in mouse, while homozygous loss is embryonic lethal.

Causes →: mn-neurodev-transcriptionmn-ncc-cardiac

Genes: HGNC:22962

Gene products: MED13L

GO process: GO:0006366GO:0006357

Complexes: CKM (CDK8 kinase module)

5 evidence

“Results: The 17 kb out-of-frame de novo deletion encompassing exon 2 of MED13L (MIM *608771) in patient 56366, together with overlapping cases, were instrumental to define a recognisable haploinsufficiency syndrome that we reported and discussed in detail elsewhere.”
de novo intragenic deletion defines a recognisable haploinsufficiency syndrome
literature · 10.1136/jmedgenet-2014-102588

“The first patient has a de novo mutation in the splice acceptor site of exon 5 of MED13L. cDNA analysis showed this mutation results in an in-frame deletion, removing 15 amino acids in middle of the conserved MED13L N-terminal domain.”
de novo splice/exonic LoF variants confirm haploinsufficiency
literature · 10.1038/ejhg.2014.69

“Results: Due to embryonic lethality, we characterize the Med13l heterozygous germline deletion (Figure 1E).”
homozygous Med13l KO is embryonic lethal; heterozygous mice model the syndrome
literature · 10.1002/dvdy.70079

“MED13L syndrome mechanism: It is hypothesized that in MED13L Haploinsufficiency Syndrome, the transcriptional process related to the mediator complex interaction with RNA polymerase II may be disrupted. Cyclin C is aberrantly released into the cytoplasm, increasing susceptibility to cell death through mitochondrial fragmentation, decreased oxygen consumption as well as decreased ATP production. 50 , 53”
haploinsufficiency disrupts Mediator–Pol II transcription and cyclin C retention
literature · 10.1177/26330040241290252

pLI=1; LOEUF=0.060; mis_z=6.46
extreme LoF constraint consistent with haploinsufficiency
database · gnomad · gene/MED13L

### mn-missense-destabilisation medium

Recurrent missense variants clustering in conserved domains (notably exon 15 hotspot p.Pro866Leu/p.Pro869Ser and C-terminal residues) destabilise MED13L secondary structure, drive cytoplasmic mislocalisation, and impair dendritic growth in cortical neurons; most behave as loss-of-function, but at least p.Pro869Ser retains nuclear localisation and stable expression consistent with a dominant-negative or neomorphic effect, and missense carriers show a more severe phenotype with epilepsy.

Causes →: mn-neurodev-transcription

Genes: HGNC:22962

Gene products: MED13L

GO process: GO:0048813

4 evidence

“Notably, our in silico modelling predicted this missense mutation to decrease the stability of an alpha-helix and thereby affecting the MED13L secondary structure, while the majority of published missense mutations remain variants of uncertain significance.”
in silico modelling predicts alpha-helix destabilisation by missense variant
literature · 10.1016/j.ejmg.2017.06.004

“In overexpression assays using cortical neurons from embryonic mouse cerebral cortices transduced by in utero electroporation-mediated gene transfer, we found that mouse orthologues of human MED13L-p.P866L and -p.T2162M missense variants accumulated in the nucleus, while the p.S2163L and p.S2177Y variants were diffusely distributed in the cytoplasm.”
missense variants alter nuclear/cytoplasmic localisation and impair dendritic growth in mouse cortical neurons
literature · 10.1111/jnc.15783

“Discussion: We observed that the p.Pro866Leu mutant variant shared similarities with the other studied variants—p.Cys1131Tyr, p.Gly1899Arg, and p.Thr2162Met—with cytoplasmic localization and protein instability, consistent with a loss-of-function pathogenic mechanism, while p.Pro869Ser exhibited more stable protein expression and partial nuclear localization, closely resembling the WT condition, arguing for the dominant-negative effect of the mutant protein or the possibility of a neomorphic effect with dominant or semi-dominant properties.”
four missense variants show cytoplasmic mislocalisation/instability (LoF); p.Pro869Ser stable+nuclear (possible DN/neomorph)
literature · 10.1016/j.xhgg.2025.100467

“We found that patients carrying missense mutations had more frequently epilepsy and showed a more severe phenotype.”
missense carriers have more frequent epilepsy and a more severe phenotype
literature · 10.1007/s10048-018-0541-0

### mn-fbw7-turnover high

SCF(FBW7) ubiquitin ligase recognises a CDK8/19-primed phosphodegron on MED13/MED13L and targets both paralogues for proteasomal degradation, providing the only known E3-ligase control of MED13L abundance and thereby the kinetics of CKM dissociation from core Mediator.

Causes →: mn-haploinsufficiency

Genes: HGNC:22962HGNC:16712HGNC:22474HGNC:1779HGNC:19338

Gene products: FBW7 (FBXW7)MED13LMED13

GO process: GO:0006511

Complexes: SCF(FBW7) E3 ubiquitin ligaseCKM (CDK8 kinase module)

2 evidence

“We show that Fbw7, a tumor suppressor and ubiquitin ligase, binds to CDK8-Mediator and targets MED13/13L for degradation.”
Fbw7 binds CDK8-Mediator and targets MED13/13L for degradation
literature · 10.1101/gad.207720.112

“The Clurman lab demonstrated that MED13 and its paralog MED13L are ubiquitylated by the ubiquitin ligase FBW7, and this modification regulates MED13 and MED13L abundance and stability (Davis et al ., 2013 ).”
FBW7 ubiquitylation regulates MED13/MED13L abundance and stability
literature · 10.3109/10409238.2013.840259

### mn-neurodev-transcription high

Reduced or dysfunctional MED13L dysregulates RNA Pol II-dependent neurodevelopmental gene programmes, impairing cortical neurogenesis, radial migration, dendrite outgrowth and callosal axon projection, providing the cellular substrate for intellectual disability, speech impairment and hypotonia.

Causes →: []

Genes: HGNC:22962

Gene products: MED13L

GO process: GO:0021987GO:0048813GO:0006366

3 evidence

“Med13l KO impairs cortical neurogenesis and dendrite development.”
Med13l KO impairs cortical neurogenesis and dendrite development
literature · 10.1038/s42003-025-08532-8

“In overexpression assays using cortical neurons from embryonic mouse cerebral cortices transduced by in utero electroporation-mediated gene transfer, we found that mouse orthologues of human MED13L-p.P866L and -p.T2162M missense variants accumulated in the nucleus, while the p.S2163L and p.S2177Y variants were diffusely distributed in the cytoplasm.”
MED13L missense variants impair dendritic growth in mouse cortical neurons
literature · 10.1111/jnc.15783

“Discussion: Functional validation experiments showed that overexpression of PlxnA4 partially rescued both the radial migration and callosal projection defects in Med13-silencing neurons, establishing PlxnA4 as a critical downstream effector of Med13 for these two processes.”
Med13 silencing impairs radial migration and callosal projection (paralogue evidence)
literature · 10.1038/s42003-026-09704-w

### mn-ncc-cardiac medium

MED13L dosage reduction perturbs neural-crest-dependent cardiac outflow-tract morphogenesis, yielding the variable conotruncal and septal congenital heart defects observed in a minority of patients; supported by neural-crest defects in CKM-mutant zebrafish and craniofacial anomalies in Med13l heterozygous mice.

Causes →: []

Genes: HGNC:22962HGNC:11957

Gene products: MED13L

GO process: GO:0061308GO:0007507

3 evidence

“Congenital cardiac and neurodevelopmental deficits have been recently linked to the mediator complex subunit 13-like protein MED13L, a subunit of the CDK8-associated mediator complex that functions in transcriptional regulation through DNA-binding transcription factors and RNA polymerase II.”
congenital cardiac and neurodevelopmental deficits linked to MED13L
literature · 10.1038/ejhg.2015.26

“Homozygous kto mutant zebrafish embryos show defects in brain, neural crest, and kidney development and die at approximately 6 days postfertilization.”
CKM (med12) mutant zebrafish embryos show neural-crest defects
literature · 10.1073/pnas.0509457102

“Conclusions and Discussion: We classify a Med13l HET mouse model as a possible resource to begin deciphering the correlation between mutations and phenotypes.”
Med13l HET mouse recapitulates craniofacial anomalies (neural-crest-derived)
literature · 10.1002/dvdy.70079

## Genetic (1)

| gene | relationship | inheritance | variant_origin | frequency | Evidence | 

| HGNC:22962 | disease-causing germline mutation in | GENO:0000147 | germline | >95% de novo; rare parental gonadal mosaicism reported | 

4 evidence

“The paper describes three clinical cases of MED13L-associated intellectual disability with an autosomal dominant inheritance.”
MED13L-associated ID with autosomal dominant inheritance
literature · 10.21508/1027-4065-2022-67-1-101-107

“Results: The 17 kb out-of-frame de novo deletion encompassing exon 2 of MED13L (MIM *608771) in patient 56366, together with overlapping cases, were instrumental to define a recognisable haploinsufficiency syndrome that we reported and discussed in detail elsewhere.”
de novo MED13L deletion is causal
literature · 10.1136/jmedgenet-2014-102588

“The first patient has a de novo mutation in the splice acceptor site of exon 5 of MED13L. cDNA analysis showed this mutation results in an in-frame deletion, removing 15 amino acids in middle of the conserved MED13L N-terminal domain.”
de novo splice-site MED13L variant is causal
literature · 10.1038/ejhg.2014.69

symbol=MED13L; name='mediator complex subunit 13L'; uniprot=Q71F56; ensembl=ENSG00000123066
gene identity
database · hgnc · HGNC:22962 | 

### Variants

| gene | hgvs | effect | significance | Evidence | 

| HGNC:22962 | (ClinVar census) | mixed | ClinVar: 235 P/LP, 606 VUS of 1813 total records | 

1 evidence

total=1813; P/LP=235; VUS=606
variant census
database · clinvar · gene=MED13L | 

| HGNC:22962 | c.2597C>T (p.Pro866Leu) | missense (exon-15 hotspot) | Pathogenic | 

1 evidence

“Discussion: We observed that the p.Pro866Leu mutant variant shared similarities with the other studied variants—p.Cys1131Tyr, p.Gly1899Arg, and p.Thr2162Met—with cytoplasmic localization and protein instability, consistent with a loss-of-function pathogenic mechanism, while p.Pro869Ser exhibited more stable protein expression and partial nuclear localization, closely resembling the WT condition, arguing for the dominant-negative effect of the mutant protein or the possibility of a neomorphic effect with dominant or semi-dominant properties.”
p.Pro866Leu shows cytoplasmic localisation and protein instability (LoF mechanism)
literature · 10.1016/j.xhgg.2025.100467 | 

| HGNC:22962 | c.2605C>A (p.Pro869Ser) | missense (exon-15 hotspot) | Pathogenic | 

2 evidence

“Discussion: Our case further demonstrates that Pro869Ser is a hotspot mutation of the MED13L gene.”
Pro869Ser is a recurrent hotspot mutation
literature · 10.1186/s13052-020-00847-y

“Discussion: We observed that the p.Pro866Leu mutant variant shared similarities with the other studied variants—p.Cys1131Tyr, p.Gly1899Arg, and p.Thr2162Met—with cytoplasmic localization and protein instability, consistent with a loss-of-function pathogenic mechanism, while p.Pro869Ser exhibited more stable protein expression and partial nuclear localization, closely resembling the WT condition, arguing for the dominant-negative effect of the mutant protein or the possibility of a neomorphic effect with dominant or semi-dominant properties.”
p.Pro869Ser stable nuclear expression, possible dominant-negative/neomorphic
literature · 10.1016/j.xhgg.2025.100467 | 

| HGNC:22962 | c.5278C>T (p.Arg1760*) | stop-gain | Pathogenic | 

1 evidence

“As depicted in Figure 2A , a heterozygous stop-gain variant of MED13L c.5278C > T (p.Arg1760 ∗ ) was detected in a female newborn diagnosed with spina bifida.”
heterozygous stop-gain p.Arg1760* identified in spina bifida newborn
literature · 10.3389/fcell.2021.641831 | 

| HGNC:22962 | 17 kb out-of-frame de novo deletion encompassing exon 2 | intragenic out-of-frame deletion | Pathogenic | 

1 evidence

“Results: The 17 kb out-of-frame de novo deletion encompassing exon 2 of MED13L (MIM *608771) in patient 56366, together with overlapping cases, were instrumental to define a recognisable haploinsufficiency syndrome that we reported and discussed in detail elsewhere.”
17 kb out-of-frame de novo deletion of exon 2 defines the haploinsufficiency syndrome
literature · 10.1136/jmedgenet-2014-102588 | 

## Inheritance (1)

| mode | label | penetrance | expressivity | Evidence | 

| HP:0000006 | Autosomal dominant inheritance | complete (assumed; no non-penetrant carriers reported) | variable — wide intrafamilial variability documented; missense (esp. exon 15/17) carriers tend to a more severe phenotype than PTV carriers | 

3 evidence

“, Variants are primarily de novo, autosomal dominant, and considered to be loss-of-function (LoF); thus, MED13L syndrome is historically considered a haploinsufficiency syndrome.”
literature · 10.1177/26330040241290252

“Sixteen of 17 variants were de novo, with inferred germline mosaicism for the two families with affected siblings (Table ).”
literature · 10.1186/s11689-025-09645-1

“Results: 1). We identified the presence of the MED13L mutation in ∼30%–50% of the sperm cells (predicted on the basis of the peak heights on the sequencing electropherograms) accountable for a high recurrence risk in the couple's future pregnancies and advised on either preimplantation genetic diagnosis or insemination with donor sperm cells.”
literature · 10.1101/mcs.a006124 | 

## Phenotypes (22 HPO)

| HPO | Label | Freq | Sev | Dx | Evidence | 

| HP:0001249 | Intellectual disability | 36/36 (100%) | moderate | ✓ | 

2 evidence

“All patients presented with intellectual disability and severe language impairment.”
literature · 10.1007/s10048-018-0541-0

“Neurodevelopmental evaluation: ID severity was classified in 30 of 41 patients with 23% classified as mild, 47% as moderate, and 30% as severe to profound (Table 1).”
literature · 10.1186/s11689-025-09618-4 | 

| HP:0001263 | Global developmental delay | 8/8 (100%) | moderate | ✓ | 

3 evidence

“Phenotypically, they all had intellectual disability, speech and motor delay, and features of the mouth (open mouth appearance, macroglossia, and/or macrostomia).”
literature · 10.1016/j.ejmg.2018.06.014

“MED13L syndrome clinical symptoms: Minimal or absent speech and impaired motor capabilities dominate the presentation of global developmental delay, with 99% (81/82) and 98% (80/82) of individuals presenting with minimal/absent speech or impaired motor capabilities, respectively.”
literature · 10.1177/26330040241290252

frequency=HP:0040281; evidence=PCS
phenotype.hpoa annotation
database · hpoa · OMIM:616789|HP:0001263 | 

| HP:0000750 | Delayed speech and language development | 81/82 (99%) | severe | ✓ | 

3 evidence

“MED13L syndrome clinical symptoms: Minimal or absent speech and impaired motor capabilities dominate the presentation of global developmental delay, with 99% (81/82) and 98% (80/82) of individuals presenting with minimal/absent speech or impaired motor capabilities, respectively.”
literature · 10.1177/26330040241290252

“Discussion: Hypotonia, speech delay and brain abnormalities in MRI are quite common among these patients (70%, 99% and 45%, respectively).”
literature · 10.34763/jmotherandchild.20202403.2021.d-20-00003

frequency=HP:0040281; evidence=TAS
phenotype.hpoa annotation
database · hpoa · ORPHA:369891|HP:0000750 | 

| HP:0001344 | Absent speech | ~33% (minimally/non-verbal beyond age 4y; n=67) | severe |  | 

1 evidence

“Almost all individuals (97%) from the full cohort of 67 reported a diagnosis of language disorder during the developmental history interview, with about a third of children described by their caregivers as minimally verbal or nonverbal beyond the age of 4 years.”
literature · 10.1186/s11689-025-09645-1 | 

| HP:0001270 | Motor delay | 80/82 (98%) | moderate | ✓ | 

3 evidence

“MED13L syndrome clinical symptoms: Minimal or absent speech and impaired motor capabilities dominate the presentation of global developmental delay, with 99% (81/82) and 98% (80/82) of individuals presenting with minimal/absent speech or impaired motor capabilities, respectively.”
literature · 10.1177/26330040241290252

“[SECTION: Motor evaluation] There was no significant difference in the mean age of walking between patients in the GenIDA series ( n = 41) and those in the literature series ( n = 65) with ages of 28 and 27 (SD = 6.59) months, respectively.”
literature · 10.1186/s11689-025-09618-4

frequency=HP:0040281; evidence=PCS
phenotype.hpoa annotation
database · hpoa · OMIM:616789|HP:0001270 | 

| HP:0001290 | Generalized hypotonia | 70% | moderate | ✓ | 

2 evidence

“Discussion: Hypotonia, speech delay and brain abnormalities in MRI are quite common among these patients (70%, 99% and 45%, respectively).”
literature · 10.34763/jmotherandchild.20202403.2021.d-20-00003

frequency=n/a; evidence=TAS
phenotype.hpoa annotation
database · hpoa · OMIM:616789|HP:0001290 | 

| HP:0000729 | Autistic behavior | 55.6% (missense subset); 23% (all variants) |  |  | 

3 evidence

“Case presentation: Behavioral difficulties, such as self-harm and autistic features, were seen in 55.6% of the patients.”
literature · 10.1186/s13052-020-00847-y

“Compared with the overall incidence in all MED13L-related patients summarized by Torring et al. and Smol et al., patients with missense mutations have a higher incidence of seizures (44.4% vs 16%), MRI abnormalities (66.7% vs 45%) and autistic features (55.6% vs 23%)”
literature · 10.1186/s13052-020-00847-y

frequency=HP:0040282; evidence=TAS
phenotype.hpoa annotation
database · hpoa · ORPHA:369891|HP:0000729 | 

| HP:0000708 | Atypical behavior | 55.6% |  |  | 

2 evidence

“Case presentation: Behavioral difficulties, such as self-harm and autistic features, were seen in 55.6% of the patients.”
literature · 10.1186/s13052-020-00847-y

frequency=HP:0040282; evidence=TAS
phenotype.hpoa annotation
database · hpoa · ORPHA:369891|HP:0000708 | 

| HP:0001250 | Seizure | 15/68 (22%) |  |  | 

2 evidence

“Documented seizure presence is about 22% (15/68) in publications. 2 , 8 , 10 , 27 , 32 , 37 , 38 Of these, 17 individuals with missense variants are evaluated, with 10 having seizures. 10 , 39 Most seizure types are not characterized, though absence seizures ( n = 3) are most common. 8 , 32 , 38 The average age of individuals with reported seizures is 12 years.”
literature · 10.1177/26330040241290252

“Compared with the overall incidence in all MED13L-related patients summarized by Torring et al. and Smol et al., patients with missense mutations have a higher incidence of seizures (44.4% vs 16%), MRI abnormalities (66.7% vs 45%) and autistic features (55.6% vs 23%)”
literature · 10.1186/s13052-020-00847-y | 

| HP:0001251 | Ataxia | 20–50% |  |  | 

2 evidence

“Further common signs include abnormal MRI findings of myelination defects and abnormal corpus callosum, ataxia and coordination problems, autistic features, seizures/abnormal EEG, or congenital heart defects, present in about 20-50% of the patients.”
literature · 10.1016/j.ejmg.2017.06.004

frequency=HP:0040283; evidence=PCS
phenotype.hpoa annotation
database · hpoa · OMIM:616789|HP:0001251 | 

| HP:0012443 | Abnormal brain morphology | 45% |  |  | 

2 evidence

“Discussion: Hypotonia, speech delay and brain abnormalities in MRI are quite common among these patients (70%, 99% and 45%, respectively).”
literature · 10.34763/jmotherandchild.20202403.2021.d-20-00003

“Further common signs include abnormal MRI findings of myelination defects and abnormal corpus callosum, ataxia and coordination problems, autistic features, seizures/abnormal EEG, or congenital heart defects, present in about 20-50% of the patients.”
literature · 10.1016/j.ejmg.2017.06.004 | 

| HP:0001627 | Abnormal heart morphology | 15/72 (20.8%) |  |  | 

3 evidence

“[4. Discussion] The congenital heart defects, previously highlighted as one of the main features of MED13L haploinsufficiency syndrome, were diagnosed in only 15 (20.8%) individuals (Supplementary Table S2).”
literature · 10.3390/medicina59071225

“Congenital heart defects 12/64 –”
literature · 10.34763/jmotherandchild.20202403.2021.d-20-00003

frequency=HP:0040283; evidence=TAS
phenotype.hpoa annotation
database · hpoa · ORPHA:369891|HP:0001627 | 

| HP:0000414 | Bulbous nose | 75% | mild | ✓ | 

2 evidence

“Common dysmorphic features, seen in at least 50%, are bulbous nasal tip (75%), open mouth appearance (62%), low set ears (52%), and depressed/broad nasal bridge (58%).”
literature · 10.1016/j.ejmg.2018.06.014

frequency=HP:0040282; evidence=TAS
phenotype.hpoa annotation
database · hpoa · OMIM:616789|HP:0000414 | 

| HP:0000194 | Open mouth | 62% | mild | ✓ | 

3 evidence

“Common dysmorphic features, seen in at least 50%, are bulbous nasal tip (75%), open mouth appearance (62%), low set ears (52%), and depressed/broad nasal bridge (58%).”
literature · 10.1016/j.ejmg.2018.06.014

“the syndrome may be suspected in some individuals based on the association of developmental delay, speech impairment, bulbous nasal tip, and macroglossia, macrostomia, or open mouth appearance.”
literature · 10.1016/j.ejmg.2018.06.014

frequency=HP:0040282; evidence=PCS
phenotype.hpoa annotation
database · hpoa · OMIM:616789|HP:0000194 | 

| HP:0000369 | Low-set ears | 52% | mild |  | 

2 evidence

“Common dysmorphic features, seen in at least 50%, are bulbous nasal tip (75%), open mouth appearance (62%), low set ears (52%), and depressed/broad nasal bridge (58%).”
literature · 10.1016/j.ejmg.2018.06.014

frequency=HP:0040282; evidence=PCS
phenotype.hpoa annotation
database · hpoa · OMIM:616789|HP:0000369 | 

| HP:0005280 | Depressed nasal bridge | 58% | mild |  | 

2 evidence

“Common dysmorphic features, seen in at least 50%, are bulbous nasal tip (75%), open mouth appearance (62%), low set ears (52%), and depressed/broad nasal bridge (58%).”
literature · 10.1016/j.ejmg.2018.06.014

frequency=HP:0040283; evidence=TAS
phenotype.hpoa annotation
database · hpoa · OMIM:616789|HP:0005280 | 

| HP:0000341 | Narrow forehead |  |  |  | 

1 evidence

frequency=n/a; reference=PMID:25758992; evidence_code=PCS
HPO annotation file
database · hpoa · OMIM:616789|HP:0000341 | 

| HP:0002465 | Poor speech |  |  |  | 

1 evidence

frequency=n/a; reference=OMIM:616789; evidence_code=TAS
HPO annotation file
database · hpoa · OMIM:616789|HP:0002465 | 

| HP:0000582 | Upslanted palpebral fissure |  |  |  | 

1 evidence

frequency=n/a; reference=OMIM:616789; evidence_code=TAS
HPO annotation file
database · hpoa · OMIM:616789|HP:0000582 | 

| HP:0002342 | Moderate intellectual disability |  |  |  | 

1 evidence

frequency=n/a; reference=PMID:25167861; evidence_code=PCS
HPO annotation file
database · hpoa · OMIM:616789|HP:0002342 | 

| HP:0000486 | Strabismus |  |  |  | 

1 evidence

frequency=n/a; reference=OMIM:616789; evidence_code=TAS
HPO annotation file
database · hpoa · OMIM:616789|HP:0000486 | 

| HP:0003593 | Infantile onset |  |  |  | 

1 evidence

frequency=n/a; reference=OMIM:616789; evidence_code=TAS
HPO annotation file
database · hpoa · OMIM:616789|HP:0003593 | 

## Diagnosis (4)

| MAXO | Label | Expected result | Markers | Evidence | 

| MAXO:0001612 | chromosomal microarray testing | Normal in most; detects 12q24.21 intragenic deletions/duplications in the CNV-associated subset; ACMG-recommended first-tier ID test. | 12q24.21 CNV, MED13L intragenic deletion | 

2 evidence

“A chromosomal microarray, as recommended by the American College of Medical Genetics (ACMG), had been previously conducted and was found to be normal, prompting the decision to proceed with WES.”
literature · 10.7759/cureus.59904

“Using high resolution molecular karyotyping, we identified two intragenic de novo frameshift deletions, likely resulting in haploinsufficiency, in two patients with a similar phenotype of hypotonia, moderate ID, conotruncal heart defect and facial anomalies.”
literature · 10.1038/ejhg.2013.17 | 

| MAXO:0009004 | clinical whole-exome sequencing | Heterozygous de novo MED13L pathogenic variant (PTV, intragenic CNV, or recurrent missense); trio confirmation of de novo status anchors PS2 pathogenicity. | MED13L (NM_015335.5) PTV, MED13L missense (exon 15/17 cluster), de novo status | 

2 evidence

“A six-year-old male patient presenting with heart malformation, ID, and hypotonia was further examined using whole exome sequencing of genomic DNA extracted from a peripheral blood sample.”
literature · 10.1016/j.isci.2022.103823

“However, due to some similarity to other syndromes with ID such as FG syndrome caused by MED12 mutation, 1p36 deletion syndrome or 22q11.2 deletion syndrome and proved variable clinical expression, the use of NGS is recommended for disease differential diagnosis. 6 , 7 Key points Pathogenic variants in MED13L are common in the autosomal dominant form of syndromic intellectual disability.”
literature · 10.34763/jmotherandchild.20202403.2021.d-20-00003 | 

| MAXO:0010203 | echocardiography | Normal in ~80%; detects conotruncal CHD (d-TGA, VSD, persistent foramen ovale) in 19–21%; baseline echocardiogram recommended at diagnosis. | VSD, d-TGA, conotruncal defect | 

2 evidence

“echocardiography showed ventricular septal defect”
literature · 10.7499/j.issn.1008-8830.2017.10.010

“[4. Discussion] The congenital heart defects, previously highlighted as one of the main features of MED13L haploinsufficiency syndrome, were diagnosed in only 15 (20.8%) individuals (Supplementary Table S2).”
literature · 10.3390/medicina59071225 | 

| MAXO:0000932 | electroencephalography | Abnormal in ~20–50% (epileptiform discharges including spike-and-slow-wave) even without clinical seizures; higher yield in missense carriers. | spike-and-slow-wave, absence seizures | 

2 evidence

“She had no clinically observed seizures but had abnormal EEG showing spike and slow wave colligation and multi-spike and slow waves in the bilateral occipital and posterior temporal regions, as well as rapid rhythm distribution in the occipital area (Fig. 2 ).”
literature · 10.1186/s13052-020-00847-y

“Documented seizure presence is about 22% (15/68) in publications. 2 , 8 , 10 , 27 , 32 , 37 , 38 Of these, 17 individuals with missense variants are evaluated, with 10 having seizures. 10 , 39 Most seizure types are not characterized, though absence seizures ( n = 3) are most common. 8 , 32 , 38 The average age of individuals with reported seizures is 12 years.”
literature · 10.1177/26330040241290252 | 

## Differential diagnoses (5)

| disease | label | distinguishing features | Evidence | 

| MONDO:0011929 | chromosome 1p36 deletion syndrome | Overlapping straight eyebrows, deep-set eyes, midface hypoplasia, 1p36 deletion detectable on CMA; MED13L locus is 12q24.21 | 

1 evidence

“Haploinsufficiency for MED13L should be considered in the differential diagnosis of the 1p36 microdeletion syndrome, due to overlapping dysmorphic facial features in some patients.”
literature · 10.1038/ejhg.2015.19 | 

| MONDO:0012455 | Kleefstra syndrome | Facial gestalt resemblance noted in individual MED13L patients, Distinguished by EHMT1 variant / 9q34.3 deletion on molecular testing | 

1 evidence

“The first patient indicates some facial resemblance to Kleefstra syndrome as a novel differential diagnosis, and the second patient shows, for the first time, recurrence of a MED13L missense mutation (p.(Asp860Gly)).”
literature · 10.1016/j.ejmg.2017.06.004 | 

| MONDO:0018923 | 22q11.2 deletion syndrome | Shared ID + conotruncal CHD; 22q11.2 adds palatal anomalies, hypocalcaemia, immune deficiency, 22q11.2 deletion detectable on CMA | 

1 evidence

“However, due to some similarity to other syndromes with ID such as FG syndrome caused by MED12 mutation, 1p36 deletion syndrome or 22q11.2 deletion syndrome and proved variable clinical expression, the use of NGS is recommended for disease differential diagnosis. 6 , 7 Key points Pathogenic variants in MED13L are common in the autosomal dominant form of syndromic intellectual disability.”
literature · 10.34763/jmotherandchild.20202403.2021.d-20-00003 | 

| MONDO:0100000 | MED12-related intellectual disability syndrome | X-linked inheritance (FG/Opitz-Kaveggia, Lujan, Ohdo MKB) vs autosomal-dominant de novo for MED13L, Congenital diaphragmatic hernia in 42% (3/7) of female MED12 LoF — not reported in MED13L | 

1 evidence

“However, due to some similarity to other syndromes with ID such as FG syndrome caused by MED12 mutation, 1p36 deletion syndrome or 22q11.2 deletion syndrome and proved variable clinical expression, the use of NGS is recommended for disease differential diagnosis. 6 , 7 Key points Pathogenic variants in MED13L are common in the autosomal dominant form of syndromic intellectual disability.”
literature · 10.34763/jmotherandchild.20202403.2021.d-20-00003 | 

| MONDO:0016033 | Cornelia de Lange syndrome | MED13L LoF variants identified in cohesinopathy-negative CdLS-suspected cohorts, CdLS classically has synophrys, limb-reduction defects, growth restriction — not core MED13L features | 

1 evidence

“Furthermore, pathogenic CNVs were detected in NIPBL, MED13L, and EHMT1, along with pathogenic SNVs in ZMYND11, MED13L, and PHIP.”
literature · 10.1038/s10038-019-0643-z | 

## Treatments (9)

### speech therapy developmental therapy

Recommendation with broadest support across reports; addresses near-universal expressive-language impairment and articulatory deficits; consider AAC for minimally/non-verbal children.

MAXO: MAXO:0000930

Regimen: Early referral (before age 3) and ongoing

Addresses: HP:0000750HP:0001344

2 evidence

“First, children with known P/LP variants in MED13L would benefit from early referrals to speech therapy to assess their speech, language, and support needs.”
literature · 10.1186/s11689-025-09645-1

“A prominent feature of the MED13L neurocognitive presentation is profound language impairment, often in combination with articulatory deficits.”
literature · 10.1038/ejhg.2015.26

### physical therapy developmental therapy

Addresses hypotonia, motor delay (mean walking age 27–28 mo) and coordination/balance problems.

MAXO: MAXO:0000011

Regimen: From infancy; standard early-intervention schedule

Addresses: HP:0001270HP:0001290HP:0001251

1 evidence

“[SECTION: Motor evaluation] There was no significant difference in the mean age of walking between patients in the GenIDA series ( n = 41) and those in the literature series ( n = 65) with ages of 28 and 27 (SD = 6.59) months, respectively.”
literature · 10.1186/s11689-025-09618-4

### occupational therapy developmental therapy

Part of multidisciplinary developmental-therapy package alongside speech and physical therapy.

MAXO: MAXO:0001351

Regimen: Standard early-intervention schedule

Addresses: HP:0001270HP:0001263

1 evidence

“[Discussion] Audiovestibular rehabilitation should be prompt, appropriate, and effective and should be part of a holistic multidisciplinary effort for a maximally favorable outcome.”
literature · 10.5152/iao.2024.231284

### vision assessment surveillance

Visual disorders reported in 78% (32/41) by caregivers (strabismus, hypermetropia); registry-recommended.

MAXO: MAXO:0000971

Regimen: Baseline at diagnosis; periodic ophthalmologic review

Addresses: HP:0000486HP:0000540HP:0000504

1 evidence

“[Discussion] Hearing and visual screening are recommended to improve the management of these patients.”
literature · 10.1186/s11689-025-09618-4

### hearing examination surveillance

Hearing problems in 32% (13/41) GenIDA; audiovestibular rehabilitation when hearing loss/balance dysfunction present.

MAXO: MAXO:0000873

Regimen: Baseline at diagnosis; audiometric testing (MAXO:0000125) as indicated

Addresses: HP:0000365

2 evidence

“[Discussion] Hearing and visual screening are recommended to improve the management of these patients.”
literature · 10.1186/s11689-025-09618-4

“[Discussion] Audiovestibular rehabilitation should be prompt, appropriate, and effective and should be part of a holistic multidisciplinary effort for a maximally favorable outcome.”
literature · 10.5152/iao.2024.231284

### echocardiography surveillance

CHD in ~20% (15/72); calibrated to a minority feature — baseline screen rather than intensive surveillance.

MAXO: MAXO:0010203

Regimen: Baseline echocardiogram at diagnosis; cardiology follow-up if abnormal

Addresses: HP:0001627HP:0001669

2 evidence

“[4. Discussion] The congenital heart defects, previously highlighted as one of the main features of MED13L haploinsufficiency syndrome, were diagnosed in only 15 (20.8%) individuals (Supplementary Table S2).”
literature · 10.3390/medicina59071225

“echocardiography showed ventricular septal defect”
literature · 10.7499/j.issn.1008-8830.2017.10.010

### electroencephalography surveillance

Seizures in 14–22%; EEG abnormalities can be present without clinical seizures; lower threshold in missense (esp. exon 15/17) carriers.

MAXO: MAXO:0000932

Regimen: Baseline EEG; repeat on clinical suspicion of seizures

Addresses: HP:0001250

2 evidence

“Documented seizure presence is about 22% (15/68) in publications. 2 , 8 , 10 , 27 , 32 , 37 , 38 Of these, 17 individuals with missense variants are evaluated, with 10 having seizures. 10 , 39 Most seizure types are not characterized, though absence seizures ( n = 3) are most common. 8 , 32 , 38 The average age of individuals with reported seizures is 12 years.”
literature · 10.1177/26330040241290252

“She had no clinically observed seizures but had abnormal EEG showing spike and slow wave colligation and multi-spike and slow waves in the bilateral occipital and posterior temporal regions, as well as rapid rhythm distribution in the occipital area (Fig. 2 ).”
literature · 10.1186/s13052-020-00847-y

### anticonvulsant agent therapy symptom-directed pharmacotherapy

Valproic acid initiated for focal bilateral abnormal EEG in one report; no MED13L-specific ASM trial data.

MAXO: MAXO:0000167

Regimen: Standard anti-seizure medication per seizure type

Addresses: HP:0001250

1 evidence

“[Results] Focal bilateral abnormal waves on electroencephalogram (EEG) necessitated the initiation of valproic acid.”
literature · 10.1101/mcs.a006124

### genetic counseling counselling

De novo in 94–100% of cases but parental gonadal mosaicism documented in ≥4 families; offer prenatal/preimplantation diagnosis to exclude recurrence.

MAXO: MAXO:0000079

Regimen: At diagnosis and pre-conception

2 evidence

“Given the de novo nature of the mutation and the autosomal dominant inheritance model of MED13L , we suggested that her mother receive a molecular prenatal diagnosis by amniocentesis to rule out gonadal mosaicism and prevent the recurrence of another affected child, despite the low risk of recurrence.”
literature · 10.3389/fgene.2025.1669849

“We assume the presence of gonadal mosaicism in the mother, which allows to recommend families with confirmed cases of MED13L-associated intellectual disability to plan pregnancies with prenatal or preimplantational diagnostics.”
literature · 10.21508/1027-4065-2022-67-1-101-107

## Prevalence (2)

global (published cases) — Unknown; ~100 patients described in the literature as of 2025; <1/1,000,000 (Orphanet category)

“There are currently around 100 patients described in the scientific literature, either in case reports or in the form of series of patients who have undergone gene panel, exome or genome analysis, with brief clinical descriptions [ 4 – 6 ].”
literature · literature · caumes2025

global — Unknown; <1/1,000,000 (Orphanet point prevalence class)

Orphanet prevalence class for ORPHA:369891
prevalence
orphadata · orphadata · ORPHA:369891 (epidemiology)

## Clinical trials (1)

| nct | phase | status | intervention | 

| NCT01238250 | Observational | RECRUITING | Observational (Simons Searchlight online registry; no intervention) | 

## Animal/experimental models (8)

| organism | model | models_node | 

| NCBITaxon:10090 | Germline heterozygous Med13l mouse — postnatal growth delay, midfacial skeletal anomalies (~61% by micro-CT at 9 mo); no significant cardiac functional defect | mn-haploinsufficiency | 

| NCBITaxon:10090 | Conditional Med13l knockout in developing cerebral cortex — loss of transcriptional priming of neurogenesis genes (proteomics + bulk/scRNA-seq) | mn-neurodev-transcription | 

| NCBITaxon:10090 | In-utero electroporation of mouse cortex (shRNA knockdown ± WT/missense rescue) — dendritic growth and spine-formation readouts for variant-level function | mn-neurodev-transcription | 

| NCBITaxon:7955 | Zebrafish med13b morpholino knockdown (morphant) — defective cranial neural-crest-cell migration and craniofacial cartilage deformities at embryonic/larval stages | mn-ncc-cardiac | 

| NCBITaxon:7227 | Drosophila CDK8–Cyclin C kinase-module manipulation in wing disc — Mad-dependent Dpp-target transcription; demonstrates context-dependent direction of CKM effect | mn-ckm-hinge | 

| system | description | models_node | 

| CL:0000057 | Patient-derived MED13L+/− skin fibroblasts (single +/fs line {chang2022}; 12-line/11-variant collection {campbell2026}) — cyclin-C localisation and mitochondrial-morphology readouts | mn-ckm-hinge | 

| CL:0011020 | Human iPSC-derived neurons / neural progenitors carrying MED13L variants (CRISPR-perturbation neural-development platform {wang2024}) | mn-neurodev-transcription | 

| CL:0000010 | HEK293 transfection with FLAG-tagged WT vs MED13L missense variants — protein stability (Western) and subcellular localisation (immunofluorescence) {smol2025} | mn-haploinsufficiency | 

## External assertions (3)

gnomAD: MED13L pLI=1, LOEUF=0.060 · link

ClinVar: 235 P/LP and 606 VUS of 1813 MED13L records · link

Reactome: MED13L mapped to: PPARA activates gene expression; Transcriptional regulation of white adipocyte differentiation; RSV-host interactions · link

## References (18 cited in this entry)

10.1186/s11689-025-09618-4

10.1177/26330040241290252

10.1002/dvdy.70079

10.1101/2024.09.25.614184

10.1016/j.isci.2022.103823

10.64898/2026.06.01.729270

10.1371/journal.pgen.1008832

10.1186/s11689-025-09645-1

10.4172/jpb.s2-004

10.1038/ejhg.2013.17

10.1016/j.ejmg.2018.06.014

10.1016/j.xhgg.2025.100467

10.1101/gad.207720.112

10.1016/j.jmccpl.2025.100481

10.1002/humu.22636

10.1111/jnc.15783

10.1101/2022.03.30.486486

10.1038/s42003-025-08532-8

## Provenance 

{
  "creation_date": "2026-06-23 18:39:36.509614+00:00",
  "updated_date": "2026-06-23 18:39:36.509614+00:00",
  "curation_history": [
    {
      "date": "2026-06-23 18:39:36.509614+00:00",
      "agent": "`pipeline module ` / Anthropic Claude (frame 5f9723cd)",
      "change": "Initial curation entry generated from systematic review run (pipeline run directory)"
    },
    {
      "date": "2026-06-23 18:39:36.509614+00:00",
      "agent": "data-validation db-fetch",
      "change": "Database evidence injected: MONDO/HGNC/gnomAD/ClinVar/AlphaFold/Reactome/HPOA/Orphadata."
    }
  ],
  "notes": [
    "research.clinical_trials: ClinicalTrials.gov search for 'MED13L' returned 1 record at curation time; gap recorded.",
    "Monarch Initiative API blocked by sandbox allowlist (non-critical; MONDO resolved via OLS4).",
    "ClinGen gene-validity API endpoint returned non-JSON / 404 for direct query; assertion not retrieved (gap).",
    "completeness_honesty: mechanism.biochemical, mechanism.histopathology, mechanism.environmental, mechanism.infectious, clinical.stages, research.computational_models, research.surrogate_endpoints \u2014 not applicable / no curatable evidence; intentionally omitted.",
    "validity.reference_validity: all literature snippets sourced verbatim from Phase-5 evidence_package claim_source_sentence fields, which were extracted from abstracts/full-text in Phase 2 with COMPLIANCE_RATE 0.9982."
  ],
  "review_notes": [
    "Missense vs PTV mechanism (hyp-missense-dn-gof) is EMERGING and contested; treat severity stratification as preliminary.",
    "FBXW7/SCF dosage-modulation hypothesis carries an oncogene-substrate safety caveat (see hypothesis packet hyp-haploinsufficiency / mn-fbw7-turnover)."
  ]
}

---

# Part 2 — Post-hoc comparison against the held-out dismech entry

> **⚠️ AI—Generated Content — Not Medical Advice**
>
> This document was generated with substantial AI assistance and is not medical advice. It is a research literature synthesis intended for scientific and educational use. It has not been independently reviewed by a licensed physician for clinical accuracy and must not be used as a substitute for professional medical advice, diagnosis, or treatment. Patients, caregivers, and clinicians should rely on qualified healthcare providers and primary sources for any decision regarding a medical condition. AI systems can produce errors, including plausible-sounding statements that are incorrect; verify every claim against the cited primary literature before use. We are pursuing this work with our research partners because we want AI to become more useful in helping people learn about health and medical topics. One day, further research and testing may bring us to a different point — but today is not that day. This is early-stage work, and AI should not be interpreted as providing medical advice or as any substitute for qualified professional care.

# Unbiased comparison — the pipeline MED13L outputs vs DisMech `MED13_Syndrome` page

**Generated** 2026-06-23T23:40:18Z · this report is a static comparison; per the user's instruction, **nothing in the pipeline  review was modified based on DisMech content**.

## 0. Subject-identity caveat (read first)

| | the pipeline (this run) | DisMech page linked |
|---|---|---|
| Disease | **MED13L syndrome** | **MED13 syndrome** (MRD61) |
| MONDO | MONDO:0014773 | MONDO:0032485 |
| Gene | *MED13L* (HGNC:22962, 12q24.21) | *MED13* (HGNC:22474, 17q23.2) |
| OMIM | 616789 | 618009 |
| Reported cases | >300 (registry + cohort) | ~26 (per the DisMech `description` field) |

The page at <https://dismech.monarchinitiative.org/pages/disorders/MED13_Syndrome.html> covers the **paralog gene** *MED13*, not *MED13L*. A `MED13L` page does **not** exist in DisMech: probes of `kb/disorders/MED13L*.yaml` (repo) and `pages/disorders/MED13L*.html` (site) all returned 404 against the 1391-disorder kb. The two are sister CKM-hinge disorders with substantial mechanistic and clinical overlap, so a *format-and-method* comparison is informative — but every **content** divergence below must be read as **paralog biology, not pipeline disagreement**.

For an apples-to-apples comparison on structure and evidence model, the pipeline  side uses **two artifacts**:
- the **narrative review** ([med13l_review_v3.pdf](—), 67 pp, 11 394 body-prose words, 120 cited references), and
- the **structured curation entry** ([curation-entry.yaml](—), 87 KB) + [pathograph.json](—) — these are the pipeline  artefacts that occupy the same role as a DisMech YAML.

## 1. Format and scope

| Dimension | the pipeline MED13L (review v3 + curation-entry) | DisMech MED13_Syndrome |
|---|---|---|
| Artifact type | Systematic narrative review (PDF/HTML/MyST) **plus** schema-backed YAML curation entry | Schema-backed YAML rendered to a single HTML page |
| Source file size | review_v3.md ≈ 18.9k words (16.1k pre-Methods); curation-entry.yaml 87 KB | YAML 59 429 B; rendered HTML 612 KB |
| Page count | 67 pp PDF | single scrolling page |
| Top-level YAML sections | 6 (identity, mechanism, clinical, research, provenance, companion_artifacts) | 12 (name, creation_date, category, synonyms, description, disease_term, parents, pathophysiology, phenotypes, genetic, treatments, datasets) |
| Rendered prose sections | Intro + §1–§10 + §6b + conclusion + Methods | Pathophysiology, Pathograph, Phenotypes, Genetic Associations, Medical Actions, Related Datasets, Source YAML, References & Deep Research (which embeds two 15-section "deep research" reports) |
| Structured pathograph | 12 nodes / 12 edges (6 mechanism + 6 phenotype), JSON | 7 pathophysiology nodes with `downstream` edges; CX2/NDEx export linked |
| Figures | 3 body + 2 Methods | 0 (renderer-generated pathograph only) |
| Tables | 12 | 1 phenotype table + 1 medical-actions table (renderer-generated) |
| Authoring date range | 2026-06-19 → 2026-06-23 | 2026-04-11 → 2026-06-19 (3 commits) |
| Authoring agent | Anthropic Claude (literature-review/data-validation/clinical-critic roles) | per-repo Claude Code `/curate` workflow (cmungall + bot, per commit log) |

**Interpretation.** DisMech is a **structured KB record**: terse, ontology-bound, slot-per-claim, designed for cross-disease query and programmatic export (Mondo EMC, NDEx, ontology-score browser). the pipeline is a **PRISMA-style narrative review** with a structured KB record alongside — the narrative carries argument, conflict adjudication, and a Methods section the DisMech page does not attempt.

## 2. Evidence model

| | the pipeline review v3 | the pipeline curation-entry.yaml | DisMech MED13 YAML |
|---|---|---|---|
| Reference identifier | DOI (cite-key → bib) | `DOI:` CURIE in `evidence[*].source` | `PMID:` in `evidence[*].reference` |
| Distinct cited references | **120** | 34 distinct DOIs across 113 evidence items | **12 PMIDs** across 49 evidence items |
| Evidence items (slot-level) | n/a (prose) | **113** (83 with verbatim snippet, 5 empty stubs) | **49** (49 with snippet) |
| Snippet-to-source verification | 1 149 claim–citation triples → 91.7 % CLEAN (0 hallucinated, 0 chimeric, 0 broken-DOI) via 5-step blinded protocol | 110/110 snippets matched verbatim against the Phase-5 evidence corpus ([gate](—)) | per-snippet "validated against PubMed abstracts" (DisMech reference-validator); pass status not exposed on the page |
| Reference *titles* stored inline | no (resolved at build from `references.bib`) | no | yes (`reference_title` on every evidence item) |
| Evidence typing | n/a | `kind: literature` only | `evidence_source` enum (e.g. `HUMAN_CLINICAL`) + `supports` enum (e.g. `SUPPORT`) |

**Interpretation.** the pipeline cites an order of magnitude more sources (120 vs 12) — expected, since MED13L has ~10× the literature MED13 has, and a narrative review's job is comprehensive coverage rather than a curated minimum. DisMech's evidence model is *richer per item* (typed `evidence_source` + `supports` enum + inline `reference_title` + `explanation`) and PMID-native; the pipeline's is DOI-native with a separate bibliography resolution step. Both store verbatim supporting snippets; both verify them, but against different oracles (DisMech: PubMed abstract text; the pipeline: its own full-text/abstract evidence corpus, then a separate CrossRef metadata check). the pipeline's curation-entry has **5 empty evidence stubs** (e.g. `animal_models[0]` — source/snippet blank) that DisMech's validator would flag.

## 3. Ontology binding

| Slot | the pipeline curation-entry | DisMech MED13 |
|---|---|---|
| Disease term | MONDO:0014773 (+ OMIM/ORPHA/GARD/ICD-10 in [crossrefs.yaml](—)) | MONDO:0032485 |
| Gene term | HGNC:22962 (+ UniProt, Ensembl, Entrez, AlphaFold) | HGNC:22474 |
| Phenotype HPO | 22 terms (numeric `n/N (%)` frequencies) | 22 terms (Orphanet `VERY_FREQUENT/FREQUENT/OCCASIONAL` enum) |
| Treatment MAXO | 9 terms | 4 terms (1 with `therapeutic_modality`) |
| Biological process GO | per-node lists (e.g. GO:0006366) | per-node `biological_processes` lists |
| Cell type CL | none in YAML (covered in prose) | per-node `cell_types` lists |
| Differential MONDO | 5 terms | — (slot absent) |
| Model organism NCBITaxon | 5 (mouse×3, zebrafish, Drosophila) | 1 (mouse, via `datasets` only) |
| Mappings (`mondo_mappings`) | not populated under that key (xrefs in separate file) | not populated |

**HPO overlap** (despite being different diseases): 6/22 shared — HP:0000750, HP:0001249, HP:0001250, HP:0001263, HP:0001270, HP:0001627. This is exactly the CKM-disorder core triad (ID, GDD, speech delay, motor delay, seizures, abnormal heart morphology). The remaining 16-per-side reflect genuine paralog divergence: DisMech-MED13 carries Duane anomaly (HP:0009921), supernumerary tooth (HP:0011069), aganglionic megacolon (HP:0002251), retinal atrophy (HP:0001105) — none reported as MED13L features. `pipeline module ` carries the dysmorphism granularity (bulbous nose HP:0000414, open mouth HP:0000194, depressed nasal bridge HP:0005280, low-set ears HP:0000369) and ataxia (HP:0001251) — the MED13L gestalt. **Neither side is "wrong"; they describe sister disorders.**

**Frequency encoding** is the sharper methodological difference: DisMech uses the Orphanet-style 5-band enum; the pipeline records the **observed numerator/denominator** (e.g. `15/72 (20.8%)`) plus per-variant-subset splits (`55.6% (missense subset); 23%…`). The numeric form preserves the underlying cohort sizes and the ascertainment-method dependence the review's Act-II argument turns on; the enum form is what cross-KB queries and the Orphanet frequency model expect.

## 4. Mechanism / pathophysiology

| | the pipeline | DisMech MED13 |
|---|---|---|
| Mechanism nodes | 6 (`mn-ckm-hinge`, `mn-haploinsufficiency`, `mn-missense-destabilisation`, `mn-fbw7-turnover`, `mn-neurodev-transcription`, `mn-ncc-cardiac`) | 7 (Mediator transcriptional dysregulation, MED13 phosphodegron disruption, neurodev transcriptional dysreg, brain-structural/excitability, cardiac dev dysreg, craniofacial/ocular/sensory, somatic-growth/skeletal) |
| Node identifiers | stable `mn-*` ids (machine-referenced from treatments/models/hypotheses) | `name` strings only |
| Causal edges | explicit `causes:` lists → 12-edge pathograph JSON | `downstream:` lists per node → CX2/NDEx pathograph |
| Mechanism hypotheses (separate from established nodes) | 5 ranked hypotheses (separate `mechanistic_hypotheses` slot + 5 standalone hypothesis-packet artifacts) | — (no hypothesis slot in DisMech schema) |
| Variant-class mechanism split | 5-row `variants` block (PTV, missense-hotspot, intragenic del/dup, whole-gene CNV, d-TGA-associated noncoding) | encoded as a 529-char free-text `genetic[0].features` string |

**Interpretation.** Coverage is comparable (6 vs 7 nodes; both span the CKM-hinge → tissue-specific dysregulation chain). DisMech's nodes carry richer per-node ontology context (`cell_types`, `biological_processes` on every node); the pipeline's carry richer cross-linking (`causes` ids, `confidence`, GO+MF+complex+structure lists, and a separate testable-hypothesis layer). DisMech encodes the variant-mechanism split as prose in a string slot; the pipeline as a typed list — neither is the Disease-class `genetic` shape the dismech schema *prefers* (which is per-feature dicts, as in larger entries like Kabuki).

## 5. Coverage gaps (slots one side populates and the other does not)

**Populated by the pipeline, absent in DisMech MED13 YAML:**
- `differential_diagnoses` (5 MONDO-bound entries with distinguishing features)
- `diagnosis` (4 entries — diagnostic pathway / criteria)
- `prevalence` / `epidemiology` (2 entries; numeric estimates with source)
- `animal_models` / `experimental_models` (5 + 3 entries)
- `mechanistic_hypotheses` (5, ranked, with experiment-design packets)
- `clinical_trials` (1)
- `progression` / natural-history narrative
- Separate Methods, PRISMA flow, verification ledger, conflict adjudication
- `mappings` to OMIM/ORPHA/GARD/ICD-10/UniProt/Ensembl/AlphaFold

**Populated by DisMech MED13, absent in the pipeline curation-entry:**
- `parents` (3 disease-ontology parents — the pipeline has `identity.parents` 4× but as labels, not MONDO-bound parent terms in DisMech's sense)
- `datasets` (1 GEO accession `geo:GSE298801` + 1 ClinicalTrials.gov record `clinicaltrials:NCT01238250`, each with organism/data-type binding) — the pipeline's `research.datasets` slot is the literal string `'[]'`, not a structured list
- per-evidence `evidence_source` enum and `supports` enum
- per-evidence inline `reference_title`
- per-node `cell_types` (CL terms)
- the page-embedded "References & Deep Research" report (two 15-section research dossiers rendered alongside the structured data)

## 6. Quality-control surface

| Check | the pipeline | DisMech |
|---|---|---|
| Schema validation | `gate_curation_entry` (term_validity 22/22 HPO, 10/10 MONDO, 11/11 MAXO; reference_validity 110/110 snippet-match; pass) | `linkml-validate --target-class Disease` (PR-time hook); per-file compliance score in QC dashboard |
| Reference validation | 5-step blinded triple verification (DOI resolve → title → author → metadata → claim), 1 149 triples, 91.7 % clean | `linkml-reference-validator` against PubMed abstracts (pass implied by merge) |
| Ontology-term validation | OLS4 lookups at build; 0 bad terms | dismech-terms skill (OAK-backed term resolution) |
| Human review | story-coherence + clinical-critic (7-check clinical critic) — automated, no human in loop | PR review by Monarch curators (cmungall et al., per commit log) |
| Audit trail | phase_ledger.json (16 versions), gate_* JSONs, fix_ledger | git history (3 commits) + per-PR review threads |

**Interpretation.** the pipeline's QC is *deeper per claim* (every numeric/citation triple individually verified) but *entirely automated*; DisMech's QC is *lighter per claim* but ends in *human curator review*, which catches things automated checks do not (the Delpire–McNeill PR thread shows reviewers catching a GoF/LoF mislabel and a too-generic CL term — exactly the class of error clinical-critic also targets).

## 7. Net assessment

- **As a structured KB record**, the pipeline  curation-entry is a **near-superset** of the DisMech slot inventory (it populates 8 slot families DisMech-MED13 leaves empty), with two real gaps to close before it would pass a DisMech PR review: (a) PMID identifiers alongside DOIs, (b) structured `datasets` with GEO/SRA accessions, plus the 5 empty evidence stubs.
- **As a reader-facing page**, DisMech is **leaner and more ontology-navigable** — every term is a hyperlink into MONDO/HPO/GO/CL/MAXO and the pathograph is exportable to NDEx; the pipeline  review is **far more comprehensive and argued** (120 vs 12 sources; conflict adjudication; ascertainment-bias analysis; ranked research priorities) but the curation-entry is not yet rendered as a standalone clickable page.
- **Subject-identity** remains the dominant caveat: the only valid scientific-content comparison is mechanism-node *structure*, not *content*, because MED13 ≠ MED13L. A like-for-like content comparison would require a `kb/disorders/MED13L_Syndrome.yaml` in DisMech — which does not yet exist.

---
*Sources read for this comparison:* `kb/disorders/MED13_Syndrome.yaml` @ main (59 429 B), rendered page (612 KB), `src/dismech/schema/dismech.yaml`, `app/data.js` MED13 row, repo commit log; the pipeline [review_v3.md](—), [curation-entry.yaml](—), [pathograph.json](—), [crossrefs.yaml](—), [gate_curation_entry.json](—).
