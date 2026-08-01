# MED13 Syndrome — Anthropic systematic-review pipeline output

**Provider:** Anthropic Claude systematic-review pipeline (multi-phase: literature
retrieval, structured curation, claim-triple verification).
**Subject:** MED13 syndrome (MRD61), MONDO:0032485
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

Autosomal-dominant intellectual developmental disorder (MRD61) caused by heterozygous (predominantly de novo) variants in MED13, the hinge subunit anchoring the CDK8 kinase module to core Mediator. Universal speech delay/disorder with intellectual disability of variable severity, frequent ASD/ADHD, ophthalmologic involvement in over half, and a low-frequency severe tail of developmental and epileptic encephalopathy and multi-organ disease.

Parents: MONDO:0100038MONDO:0700092

## AI-generated mechanistic hypotheses AI-GENERATED (4)

These 4 hypotheses are the pipeline's integrative reasoning layer: each synthesises across the mechanism nodes below to propose a testable claim. Per-citation context (DisMech explanation) is collapsed under each evidence item, not shown as headline reasoning.

### Fbw7-degron stabilisation as a dosage-restoration strategyEMERGINGAI reasoning

If Fbw7-mediated turnover sets steady-state MED13 protein in human neural progenitors, slowing turnover of the wild-type allele in a haploinsufficient cell could raise MED13 protein toward the diploid level and restore CKM occupancy.

Evidence: for 1 · against 1

1 supporting citation

“SCF–Fbw7 binds CDK8-module-associated Mediator and targets MED13 and MED13L for ubiquitination and proteasomal degradation through a phospho-degron, regulating CKM–core-Mediator association”
SCF–Fbw7 targets MED13/13L through phospho-degron
literature · 10.1101/gad.207720.112

1 contrary citation

“FBXW7 is a tumour suppressor inactivated by mutation in approximately 6 % of human cancers across diverse tumour types”
Fbw7 inhibition carries oncogenic risk; substrate-selectivity required
literature · 10.1158/0008-5472.can-07-1320

### Neural-progenitor migration as a missense-variant functional readoutEMERGINGAI reasoning

Patient missense alleles that fail to rescue Med13-knockdown radial-migration / dendrite-complexity defects are LoF; alleles that rescue are benign/hypomorphic; alleles that worsen the defect are candidate altered-function — a variant classifier currently missing.

Evidence: for 1 · against 0

1 supporting citation

“*In utero* knockdown of *Med13* in mouse neocortex impairs radial migration, callosal projection and dendritic complexity of cortical neurons, with the fraction of electroporated neurons reaching the cortical plate reduced from 43 % to 26 %”
Established assay sensitive to Med13 dosage
literature · 10.1038/s42003-026-09704-w

### Selective-autophagy modulation of MED13 turnoverEMERGINGAI reasoning

If a mammalian orthologue of the yeast Snx4/Ksp1 cargo-hitchhiking autophagy route exists in neurons, autophagy inhibition would be a proteasome-independent lever on MED13 protein level and the cyclin-C stress switch would predict MED13-haploinsufficient neurons are sensitised to stress-induced cyclin-C release.

Evidence: for 1 · against 0

1 supporting citation

“Ssn2/Med13 is removed from the nucleus and degraded after stress by a Snx4-assisted, Ksp1-receptor-dependent cargo-hitchhiking autophagy pathway that is independent of known nucleophagy mechanisms”
Selective-autophagy clearance of Med13 in yeast
literature · 10.1080/15548627.2023.2259708

### miR-208a/MED13 metabolic axis as a systemic-phenotype modifierEMERGINGAI reasoning

If the cardiac-MED13 metabolic axis is dosage-sensitive in humans, variant class might predict growth and cardiac trajectory independently of the neurodevelopmental phenotype.

Evidence: for 2 · against 0

2 supporting citations

“pharmacological inhibition of miR-208a — which targets *Med13* — reduces high-fat-diet body-weight gain from 75 % to 29 %”
miR-208a→MED13 controls systemic energy expenditure
literature · 10.1016/j.cell.2012.03.029

“Growth restriction in five reported MED13 patients was attributed to feeding difficulties and gastrointestinal anomalies”
Growth restriction in MED13 patients
literature · 10.3389/fped.2025.1699544

## Pathophysiology AI-CURATED (8 mechanism nodes)

### node_01_ckm_hinge_anchor high

MED13 is the hinge subunit that physically tethers the four-protein CDK8 kinase module (CKM) to the core Mediator complex; the MED13 IDR is the load-bearing interface and MED13 (not MED12) mediates CKM–core association.

Causes →: node_02_ckm_core_occupancy

Genes: HGNC:22474HGNC:11957HGNC:1779HGNC:1581

Gene products: MED13MED12CDK8Cyclin C

GO process: GO:0006357

GO function: GO:0003712

Complexes: Mediator complexCDK8 kinase module

Structures: AF-Q9UHV7-F1MED13 IDRcMED hook

4 evidence

“a MED13 intrinsically disordered region (IDR) bound to core Mediator at 3.7 Å, showing that the CKM engages core Mediator through multiple interfaces involving the MED13 IDR and the MED12 HEAT repeats”
MED13 IDR is the CKM–core anchoring interface
literature · 10.1016/j.molcel.2024.09.001

“deleting *med13* in yeast dissociates the entire module from Mediator, whereas deleting *med12* or *cdk8* removes only downstream subunits”
MED13 is required for CKM–core association
literature · 10.1016/j.cell.2015.07.059

“MED12 — but not MED13 — is essential for activating CDK8 kinase, while MED13 mediates CKM association with Mediator”
Division of labour: MED13 anchors, MED12 activates kinase
literature · 10.1128/mcb.00993-08

“Med13 adopts an Argonaute-like bi-lobal architecture”
Structural fold of MED13
literature · 10.1126/sciadv.abd4484

### node_02_ckm_core_occupancy high

CKM docking on core Mediator sterically blocks RNA polymerase II recruitment (kinase-independent repression) but the CKM also acts as a context-dependent co-activator, so MED13 dosage perturbation dysregulates transcription bidirectionally at CKM-gated promoters and enhancers.

Causes →: node_06_neurodev_dysregulation

Genes: HGNC:22474

GO process: GO:0045892GO:0045893GO:0006357

GO function: GO:0003712

Complexes: Mediator complexCDK8 kinase module

3 evidence

“Early negative-stain reconstructions positioned the kinase module over the Mediator head and middle domains, sterically blocking the RNA polymerase II docking site independently of CDK8 catalytic activity”
Kinase-independent steric repression
literature · 10.1073/pnas.0607483103

“Med12/Med13 are required for CKM-dependent repression even when CDK8 kinase activity is dispensable”
MED13 required for repression independent of kinase
literature · 10.1101/gad.1767009

“CDK8 also acts as a context-dependent co-activator across Wnt/β-catenin, p53, serum-response and inflammatory programmes”
Context-dependent co-activation
literature · 10.4161/trns.1.1.12373

### node_03_fbw7_degron_turnover high

SCF–Fbw7 ubiquitin ligase recognises a phospho-degron at MED13 Thr326/Pro327 and targets MED13 (and MED13L) for proteasomal degradation, regulating CKM–core stoichiometry; degron-adjacent missense variants (e.g. p.Pro327Ser) are predicted to stabilise MED13 against turnover.

Causes →: node_01_ckm_hinge_anchor

Genes: HGNC:22474HGNC:16712

Gene products: MED13FBXW7SCF E3 ubiquitin ligase

GO process: GO:0016567GO:0043161

GO function: GO:0004842

Structures: Thr326/Pro327 phospho-degron

Triggers: phosphorylation of Thr326

3 evidence

“Fbw7 binds CDK8-module-containing Mediator and targets both MED13 and MED13L for degradation, and that this degradation regulates CKM association with the core complex”
SCF–Fbw7 controls MED13 abundance
literature · 10.1101/gad.207720.112

“the recurrent p.Pro327Ser substitution sits in the Fbw7 phosphodegron”
Recurrent missense at the degron
literature · 10.1007/s00439-018-1887-y

“The MED13 degron sits at Thr326/Pro327 in the N-terminal region”
Degron position
literature · 10.1007/s00439-018-1887-y

### node_04_haploinsufficiency_lof high

Heterozygous truncating MED13 variants and 17q23.2 whole-gene deletions reduce the pool of CKM available to dock on core Mediator (haploinsufficiency); supported by extreme LoF constraint (pLI=1.00, LOEUF=0.145), de novo enrichment (p=0.00371), and absence of stable truncated protein product.

Causes →: node_02_ckm_core_occupancynode_06_neurodev_dysregulation

Genes: HGNC:22474

GO process: GO:0006357

5 evidence

“seven de novo *MED13* variants in 30,884 alleles from large DD/ID cohorts yielded p = 0.00371”
Statistically significant de novo enrichment
literature · 10.1007/s00439-018-1887-y

“RNA and protein studies on the p.Arg1400* proband detected the mutant transcript with no significant difference in total *MED13* mRNA versus parents (one-way ANOVA p = 0.5913) but no truncated ~150 kDa protein product”
Mutant allele not stably translated
literature · 10.1007/s00439-018-1887-y

“An 800 kb 17q23.2 microdeletion encompassing *MED13* in a child with moderate intellectual disability provides independent whole-gene dosage-loss support”
Whole-gene deletion phenocopy
literature · 10.1002/ajmg.a.34222

pLI=1.0, LOEUF=0.145, mis_z=3.33, obs_lof=23/exp_lof=225.2
Extreme LoF intolerance
database · gnomAD · ENSG00000108510

Gene-disease validity classification: Definitive (AD), MED13–complex neurodevelopmental disorder, ID/Autism GCEP, 2022-05-17
Definitive gene-disease validity
database · ClinGen · CGGV:assertion_e82f63b1-ed0f-4dd0-8168-3aa4e0a4c2a9-2022-05-17T100000.000Z

### node_05_missense_altered_function low

Clustered missense variants — N-terminal Fbw7-degron region, C-terminal cluster, and central-IDR residues 834/835 — are candidate altered-function alleles: most severe phenotypes (DEE, neonatal multi-organ, mitochondrial pathology) reported only with missense or in-frame splice alleles. Mechanism is structured inference, not yet demonstrated.

Causes →: node_06_neurodev_dysregulation

Genes: HGNC:22474

Structures: MED13 IDR residues 834/835Thr326/Pro327 degronC-terminal cluster

4 evidence

“six of seven non-truncating variants in the founding cohort fell in two small terminal regions”
Positional clustering of missense
literature · 10.1007/s00439-018-1887-y

“A de novo p.Tyr834Cys variant produced developmental and epileptic encephalopathy with infantile spasms”
Severe DEE with IDR missense
literature · 10.1016/j.seizure.2022.09.002

“neighbouring 834/835 substitutions produced more severe phenotypes than previously reported *MED13* cases”
Regional severity signal at 834/835
literature · 10.1186/s12920-024-01857-z

“an independent de novo p.Pro835Ser case presented with infantile spasms, cardiomyopathy and autopsy-confirmed mitochondrial abnormalities”
Second p.Pro835Ser DEE case
literature · 10.1038/s41439-025-00327-x

### node_06_neurodev_dysregulation medium

Reduced or altered CKM-gated transcriptional regulation during neurodevelopment dysregulates a context-dependent set of promoters and enhancers, impairing radial neuronal migration, callosal projection and dendritic complexity, producing the MRD61 neurodevelopmental phenotype.

Genes: HGNC:22474

GO process: GO:0021799GO:0007399GO:0016358

2 evidence

“in utero *Med13* knockdown in mouse embryonic neocortex impaired radial migration, callosal projection and dendritic complexity of cortical neurons”
Direct neuronal-migration phenotype on Med13 reduction
literature · 10.1038/s42003-026-09704-w

“about 43% of the GFP-labeled cells successfully migrated to the cortical plate (CP) in the control group, whereas only 26% of Med13-knockdown neurons reached the CP”
Quantitative migration defect
literature · 10.1038/s42003-026-09704-w

### node_07_paralog_redundancy medium

MED13 and MED13L are mutually exclusive at the CKM hinge and partially redundant: combined cardiomyocyte deletion of Med13 and Med13l is lethal where either single knockout is viable, motivating a paralog-compensation hypothesis for tissue-specific severity.

Causes →: node_02_ckm_core_occupancy

Genes: HGNC:22474HGNC:22962

GO process: GO:0006357

2 evidence

“combined cardiomyocyte-specific deletion produces 100% mortality by 10 weeks (median survival 6 weeks)”
Med13/Med13l double-KO lethality
literature · 10.1016/j.jmccpl.2025.100481

“*MED13* and *MED13L* occupy the same structural position”
Same structural slot
literature · 10.1016/j.molcel.2024.09.001

### node_08_stress_autophagy_cycc_release low

Under oxidative/nutrient stress in yeast, Snf1/AMPK and CWI-MAPK degrade Med13, releasing cyclin C from its Med13-dependent nuclear anchor to relocalise to mitochondria and promote fission and regulated cell death; a Snx4/Ksp1 selective-autophagy route clears Med13. Mammalian orthology unestablished.

Genes: HGNC:22474HGNC:1581

GO process: GO:0016236GO:0006979GO:0000266

Triggers: oxidative stressnutrient stress

3 evidence

“Snf1/AMPK and the cell-wall-integrity MAPK pathway cooperate to degrade Med13”
Stress-induced Med13 degradation
literature · 10.15698/mic2018.08.641

“releasing cyclin C from its Med13-dependent nuclear anchor to relocalise to mitochondria and promote fission and regulated cell death”
Cyclin C nuclear→mitochondrial relocalisation
literature · 10.3390/biology8010003

“yeast Med13 is cleared by a Snx4/Ksp1-dependent selective-autophagy pathway distinct from canonical proteasomal turnover”
Selective-autophagy clearance route
literature · 10.1080/15548627.2023.2259708

## Genetic (1)

| gene | relationship | inheritance | variant_origin | frequency | Evidence | 

| HGNC:22474 | causal (haploinsufficiency for truncating; possible altered-function for clustered missense) | GENO:0000147 | germline | predominantly de novo (11/12 with parental data); rare familial transmission documented | 

3 evidence

“Eleven of twelve probands with parental data in the founding cohort carried confirmed de novo variants, with one mother-to-daughter transmission of an affected allele”
De novo predominance
literature · 10.1007/s00439-018-1887-y

Gene-disease validity classification: Definitive (AD), MED13–complex neurodevelopmental disorder, ID/Autism GCEP, 2022-05-17
Definitive AD gene-disease validity
database · ClinGen · CGGV:assertion_e82f63b1-ed0f-4dd0-8168-3aa4e0a4c2a9-2022-05-17T100000.000Z

pLI=1.0, LOEUF=0.145, mis_z=3.33
Dosage sensitivity
database · gnomAD · ENSG00000108510 | 

### Variants

| gene | hgvs | effect | significance | Evidence | 

| HGNC:22474 | p.Pro327Ser | missense (Fbw7-degron region) | Pathogenic (recurrent de novo; Kabuki-like phenotype) | 

1 evidence

“p.Pro327Ser, reported in the founding cohort, recurred independently in a patient initially given a clinical diagnosis of Kabuki syndrome”
Recurrent de novo at degron
literature · 10.1002/ajmg.a.61994 | 

| HGNC:22474 | p.Tyr834Cys | missense (central IDR) | Pathogenic (de novo; DEE) | 

1 evidence

“A de novo p.Tyr834Cys variant produced developmental and epileptic encephalopathy with infantile spasms”
DEE phenotype
literature · 10.1016/j.seizure.2022.09.002 | 

| HGNC:22474 | p.Pro835Ser | missense (central IDR) | Likely pathogenic (recurrent de novo; DEE/multi-organ) | 

2 evidence

“a de novo p.Pro835Ser variant in a neonate with multiple congenital anomalies was classified likely pathogenic with concordant in-silico predictions (CADD 26.1; PolyPhen-2 0.996; SIFT 0.0)”
First p.Pro835Ser case
literature · 10.1186/s12920-024-01857-z

“an independent de novo p.Pro835Ser case presented with infantile spasms, cardiomyopathy and autopsy-confirmed mitochondrial abnormalities”
Second p.Pro835Ser case
literature · 10.1038/s41439-025-00327-x | 

| HGNC:22474 | p.Arg1400* | nonsense | Pathogenic (de novo) | 

1 evidence

“RNA and protein studies on the p.Arg1400* proband detected the mutant transcript with no significant difference in total *MED13* mRNA versus parents (one-way ANOVA p = 0.5913) but no truncated ~150 kDa protein product”
Functional study of nonsense allele
literature · 10.1007/s00439-018-1887-y | 

| HGNC:22474 | p.Arg1409Ter | nonsense | Pathogenic (de novo; DLD cohort) | 

1 evidence

“a Swedish severe-developmental-language-disorder cohort independently ascertained a de novo *MED13* nonsense variant (p.Arg1409Ter) in one proband”
Independent ascertainment via DLD
literature · 10.1007/s00439-023-02636-z | 

| HGNC:22474 | c.2691del p.(Asp898IlefsTer14) | frameshift | Pathogenic (PVS1+PS2) | 

1 evidence

“a de novo frameshift c.2691del p.(Asp898IlefsTer14) was classified pathogenic by ACMG criteria PVS1 + PS2”
ACMG-classified frameshift
literature · 10.7759/cureus.99683 | 

| HGNC:22474 | c.5641delinsTC p.(R1882Sfs*9) | frameshift | Likely pathogenic (PVS1+PM2_Supporting; familial) | 

1 evidence

“A maternally inherited frameshift c.5641delinsTC (p.R1882Sfs*9) segregating in a Chinese family provided the second documented vertical transmission of a truncating allele”
Familial frameshift segregation
literature · 10.3389/fped.2025.1699544 | 

| HGNC:22474 | 17q23.2 800kb deletion (incl. MED13) | whole-gene deletion (CNV) | Pathogenic (haploinsufficiency) | 

1 evidence

“An 800 kb 17q23.2 microdeletion encompassing *MED13* in a child with moderate intellectual disability provides independent whole-gene dosage-loss support”
Whole-gene CNV
literature · 10.1002/ajmg.a.34222 | 

| HGNC:22474 | p.Pro42Leufs*6 | frameshift (N-terminal) | Pathogenic (de novo) | 

1 evidence

“Five of those variants were truncating (three nonsense — p.Leu131*, p.Leu582*, p.Arg1400* — and two frameshift, p.Pro42Leufs*6 and p.Thr1496Metfs*11”
Founding-cohort truncating set
literature · 10.1007/s00439-018-1887-y | 

## Inheritance (1)

| mode | label | penetrance | expressivity | Evidence | 

| HP:0000006 | Autosomal dominant inheritance | incomplete (asymptomatic carrier parent documented) | variable (IQ 85 to 35–50 in founding cohort; severe DEE tail) | 

3 evidence

“a pathogenic *MED13* variant inherited from an asymptomatic parent (in whom it had arisen de novo) has been documented”
Incomplete penetrance
literature · 10.1016/j.ejmg.2024.104932

“Formal testing in the founding cohort returned total IQ from 85 (lower-normal) down to 35–50 (moderate ID)”
Variable expressivity
literature · 10.1007/s00439-018-1887-y

HP:0000006 Autosomal dominant inheritance
HPOA inheritance annotation
database · HPO_OMIM · OMIM:618009 | 

## Phenotypes (32 HPO)

| HPO | Label | Freq | Sev | Dx | Evidence | 

| HP:0000750 | Delayed speech and language development | 13/13 (100%); 22/22 in 2025 aggregate |  |  | 

2 evidence

“Speech delay or disorder is the only feature reported in every published *MED13* proband”
Universal speech impairment
literature · 10.1007/s00439-018-1887-y

HP:0000750 Delayed speech and language development frequency=13/13
HPOA-curated frequency
database · HPO_OMIM · OMIM:618009 | 

| HP:0001263 | Global developmental delay | 13/13; 23/23 in 2025 aggregate |  |  | 

2 evidence

“intellectual disability and/or developmental delay in 23/23 individuals with available data”
Universal ID/DD in aggregate
literature · 10.3389/fped.2025.1699544

HP:0001263 Global developmental delay frequency=13/13
HPOA-curated frequency
database · HPO_OMIM · OMIM:618009 | 

| HP:0001249 | Intellectual disability | ≥9/13 (69%); 23/23 in 2025 aggregate |  |  | 

1 evidence

“speech difficulties (13/13), intellectual disability (at least 9/13), and eye or vision problems (8/13)”
Founding-cohort frequencies
literature · 10.1007/s00439-018-1887-y | 

| HP:0011098 | Speech apraxia | 3/13 (23%) |  |  | 

2 evidence

“three of those thirteen showed characteristics of speech apraxia”
Speech apraxia frequency
literature · 10.1007/s00439-018-1887-y

HP:0011098 Speech apraxia frequency=3/13
HPOA-curated frequency
database · HPO_OMIM · OMIM:618009 | 

| HP:0000729 | Autistic behavior | 5/13; recurrent across reports |  |  | 

2 evidence

“Autism-spectrum disorder and attention-deficit/hyperactivity disorder were among the recurrent behavioural features in the founding cohort”
ASD recurrent in founding cohort
literature · 10.1007/s00439-018-1887-y

HP:0000729 Autistic behavior frequency=5/13
HPOA-curated frequency
database · HPO_OMIM · OMIM:618009 | 

| HP:0007018 | Attention deficit hyperactivity disorder | 3/13; recurrent |  |  | 

2 evidence

“Autism-spectrum disorder and attention-deficit/hyperactivity disorder were among the recurrent behavioural features in the founding cohort”
ADHD recurrent
literature · 10.1007/s00439-018-1887-y

HP:0007018 Attention deficit hyperactivity disorder frequency=3/13
HPOA-curated frequency
database · HPO_OMIM · OMIM:618009 | 

| HP:0001250 | Seizure | 1/19 (pre-2022); DEE subset |  |  | 

1 evidence

“a 2022 literature review found epilepsy in only 1/19 previously reported individuals”
Low overall epilepsy frequency
literature · 10.1016/j.seizure.2022.09.002 | 

| HP:0011170 | Generalized myoclonic-atonic seizure | 1/13 |  |  | 

2 evidence

“Only 1/13 founding-cohort patients had seizures — drug-resistant myoclonic-atonic epilepsy with onset at 4 years”
Founding-cohort epilepsy case
literature · 10.1007/s00439-018-1887-y

HP:0011170 Generalized myoclonic-atonic seizure frequency=1/13
HPOA-curated frequency
database · HPO_OMIM · OMIM:618009 | 

| HP:0012469 | Infantile spasms | ≥2 cases (DEE tail) |  |  | 

1 evidence

“tonic seizures at 2 months evolving to epileptic spasms at 4 months, with seizure control achieved on vigabatrin”
DEE infantile-spasms phenotype
literature · 10.1038/s41439-025-00327-x | 

| HP:0001252 | Hypotonia | 3/13 (23%) |  |  | 

2 evidence

“Hypotonia was present in 3/13 of the founding cohort”
Hypotonia frequency
literature · 10.1007/s00439-018-1887-y

HP:0001252 Hypotonia frequency=3/13
HPOA-curated frequency
database · HPO_OMIM · OMIM:618009 | 

| HP:0002194 | Delayed gross motor development | 7/13 (54%); 14/20 in aggregate |  |  | 

2 evidence

“Motor delay is frequent but not universal — 7/13 in the founding cohort, predominantly gross-motor”
Motor delay frequency
literature · 10.1007/s00439-018-1887-y

HP:0002194 Delayed gross motor development frequency=6/13
HPOA-curated frequency
database · HPO_OMIM · OMIM:618009 | 

| HP:0001999 | Abnormal facial shape | 16/21 (76%) |  |  | 

1 evidence

“Dysmorphic facial features are frequent — 16/21 (76%) in the 2025 aggregate”
Dysmorphic features aggregate frequency
literature · 10.3389/fped.2025.1699544 | 

| HP:0000316 | Hypertelorism | recurrent |  |  | 

2 evidence

“hypertelorism, broad nasal tip, low-set simple ears and wide-spaced nipples in a de novo missense neonate”
Hypertelorism reported
literature · 10.1186/s12920-024-01857-z

HP:0000316 Hypertelorism frequency=
HPOA-curated frequency
database · HPO_OMIM · OMIM:618009 | 

| HP:0000431 | Wide nasal bridge | recurrent |  |  | 

2 evidence

“a broad/high nasal bridge, full nasal tip, synophrys, a flat philtrum and a wide mouth”
Founding-cohort facial features
literature · 10.1007/s00439-018-1887-y

HP:0000431 Wide nasal bridge frequency=
HPOA-curated frequency
database · HPO_OMIM · OMIM:618009 | 

| HP:0000664 | Synophrys | recurrent |  |  | 

2 evidence

“a broad/high nasal bridge, full nasal tip, synophrys, a flat philtrum and a wide mouth”
Synophrys in facial gestalt
literature · 10.1007/s00439-018-1887-y

HP:0000664 Synophrys frequency=
HPOA-curated frequency
database · HPO_OMIM · OMIM:618009 | 

| HP:0000154 | Wide mouth | recurrent |  |  | 

2 evidence

“a broad/high nasal bridge, full nasal tip, synophrys, a flat philtrum and a wide mouth”
Wide mouth in facial gestalt
literature · 10.1007/s00439-018-1887-y

HP:0000154 Wide mouth frequency=
HPOA-curated frequency
database · HPO_OMIM · OMIM:618009 | 

| HP:0009921 | Duane anomaly | 2/13 (15%) |  |  | 

2 evidence

“Duane anomaly — a congenital strabismus with non-progressive horizontal ophthalmoplegia and globe retraction on attempted adduction — was reported in two founding-cohort patients”
Duane anomaly frequency
literature · 10.1007/s00439-018-1887-y

HP:0009921 Duane anomaly frequency=2/13
HPOA-curated frequency
database · HPO_OMIM · OMIM:618009 | 

| HP:0000478 | Abnormality of the eye | 8/13 (62%); 11/19 (58%) |  |  | 

1 evidence

“Eye and vision abnormalities are the most consistent non-neurological finding. They were present in 8/13 (62%) of the founding cohort”
Eye/vision abnormality frequency
literature · 10.1007/s00439-018-1887-y | 

| HP:0012450 | Chronic constipation | 4/13; 6/17 (35%) |  |  | 

2 evidence

“Gastrointestinal involvement is led by chronic obstipation — 4/13 in the founding cohort”
Constipation frequency
literature · 10.1007/s00439-018-1887-y

HP:0012450 Chronic constipation frequency=4/13
HPOA-curated frequency
database · HPO_OMIM · OMIM:618009 | 

| HP:0001508 | Failure to thrive | 5 cases |  |  | 

1 evidence

“Five individuals in the literature aggregate exhibited growth restriction, co-occurring with feeding difficulties and gastrointestinal anomalies”
Growth restriction with feeding difficulty
literature · 10.3389/fped.2025.1699544 | 

| HP:0001511 | Intrauterine growth retardation | ≥2 cases |  |  | 

1 evidence

“Intrauterine growth restriction with birth weight at the 2nd centile (2132 g) and normal birth length was documented in a de novo missense neonate”
IUGR documented
literature · 10.1186/s12920-024-01857-z | 

| HP:0004322 | Short stature | minority |  |  | 

1 evidence

“Postnatal growth retardation with short stature (height 80 cm, <−2 SD) at 2 years 3 months was recorded in a frameshift proband”
Short stature documented
literature · 10.3389/fped.2025.1699544 | 

| HP:0001627 | Abnormal heart morphology | 2/13; 4/18 (22%) |  |  | 

1 evidence

“Congenital heart abnormalities occur in a minority — 2/13 in the founding cohort”
CHD frequency
literature · 10.1007/s00439-018-1887-y | 

| HP:0000365 | Hearing impairment | 4/19 (21%) |  |  | 

1 evidence

“Hearing loss was recorded in 4/19 (21%) of the aggregate”
Hearing loss frequency
literature · 10.3389/fped.2025.1699544 | 

| HP:0002650 | Scoliosis | ≥2 cases |  |  | 

1 evidence

“scoliosis in both previously published p.Pro327Ser carriers”
Scoliosis in p.Pro327Ser carriers
literature · 10.1186/s12920-024-01857-z | 

| HP:0002119 | Ventriculomegaly | case-level (severe tail) |  |  | 

1 evidence

“corpus-callosum hypoplasia and bilateral ventricular enlargement”
Ventricular enlargement on MRI
literature · 10.1038/s41439-025-00327-x | 

| HP:0002079 | Hypoplasia of the corpus callosum | case-level (severe tail) |  |  | 

1 evidence

“corpus-callosum hypoplasia and bilateral ventricular enlargement”
Corpus callosum hypoplasia on MRI
literature · 10.1038/s41439-025-00327-x | 

| HP:0000256 | Macrocephaly | case-level |  |  | 

1 evidence

“severe global DD, marked dysmorphism, macrocephaly and short stature”
Macrocephaly with severe DD
literature · 10.1002/ajmg.a.62238 | 

| HP:0000252 | Microcephaly | case-level |  |  | 

1 evidence

“Microcephaly with dysmorphic features was recorded in the 2022 DEE case”
Microcephaly in DEE case
literature · 10.1016/j.seizure.2022.09.002 | 

| HP:0002463 | Language impairment | 22/22 (100%) |  |  | 

1 evidence

“in 22/22 individuals with language data in the pooled compilation, about half of whom were judged to have a significant language disorder”
Language impairment universal
literature · 10.3389/fped.2025.1699544 | 

| HP:0410263 | Brain imaging abnormality | 5/16 (31%) |  |  | 

1 evidence

“the 2025 aggregate records brain-MRI abnormalities in 5/16 imaged individuals”
MRI abnormality frequency
literature · 10.3389/fped.2025.1699544 | 

| HP:0002817 | Abnormality of the upper limb | 8/18 (44%) |  |  | 

1 evidence

“Skeletal/limb abnormalities were tabulated in 8/18 (44%)”
Skeletal/limb abnormality frequency
literature · 10.3389/fped.2025.1699544 | 

## Diagnosis (3)

| MAXO | Label | Expected result | Markers | Evidence | 

| MAXO:0009004 | clinical whole-exome sequencing | Heterozygous pathogenic/likely-pathogenic MED13 variant (de novo or inherited) | MED13 (HGNC:22474) | 

2 evidence

“We strongly recommend that ES/GS be considered as a first- or second-tier test for patients with CA/DD/ID.”
ACMG first-tier ES/GS recommendation
literature · 10.1038/s41436-021-01242-6

“Every reported *MED13* diagnosis has been made by trio (or proband) exome or genome sequencing”
All diagnoses via ES/GS
literature · 10.1007/s00439-018-1887-y | 

| MAXO:0001612 | chromosomal microarray testing | 17q23.2 microdeletion encompassing MED13 (CNV class only) | 17q23.2 | 

2 evidence

“an 800 kb 17q23.2 deletion encompassing *MED13* (then *THRAP1*) detected by array-CGH and proposed *MED13* haploinsufficiency as the principal driver”
CNV detection by aCGH
literature · 10.1002/ajmg.a.34222

“The 2010 ISCA consensus recommended chromosomal microarray as the first-tier cytogenetic test on the basis of a 15–20% diagnostic yield”
CMA role
literature · 10.1016/j.ajhg.2010.04.006 | 

| MAXO:0000533 | molecular genetic testing | PVS1+PS2 (truncating de novo); PM1/PS4 candidate for clustered missense; PP3 via REVEL/BayesDel/MISTIC | PVS1, PS2, PM2, PM1, PP3 | 

3 evidence

“Interpretation follows the ACMG/AMP five-tier framework”
ACMG/AMP framework
literature · 10.1038/gim.2015.30

“recent clinical reports have classified de novo *MED13* frameshift alleles as Pathogenic via PVS1 plus PS2”
PVS1+PS2 classification
literature · 10.7759/cureus.99683

“The ClinGen SVI PVS1 decision tree, however, conditions PVS1 strength on the gene–disease validity level”
PVS1 strength conditioning
literature · 10.1002/humu.23626 | 

## Differential diagnoses (6)

| disease | label | distinguishing features | Evidence | 

| MONDO:0014773 | cardiac anomalies - developmental delay - facial dysmorphism syndrome | Recognisable facial gestalt; larger cohort (>100); CHD historically associated | 

1 evidence

“*MED13L* haploinsufficiency syndrome — moderate ID, hypotonia and a recognisable facial gestalt without obligatory cardiac defects”
MED13L paralog disorder
literature · 10.1038/ejhg.2014.69 | 

| MONDO:0100000 | MED12-related intellectual disability syndrome | X-linked allelic series (FG/Lujan/Ohdo-MKB in males; Hardikar in females) | 

1 evidence

“explicitly situate *MED13* alongside *MED12* and *MED13L* as kinase-module subunits whose mutation produces overlapping intellectual-disability syndromes”
CKM-family overlap
literature · 10.1016/j.ajhg.2019.02.006 | 

| MONDO:0030030 | Nizon-Isidor syndrome | Corpus-callosum agenesis prominent | 

1 evidence

“*MED12L* (ID/DD in 7/7 affected individuals across seven families)”
MED12L disorder
literature · 10.1038/s41436-019-0557-3 | 

| MONDO:0032897 | intellectual developmental disorder with hypotonia and behavioral abnormalities | Kinase-domain missense clustering; biochemical kinase-hypomorph readout | 

1 evidence

“*CDK8* (de novo missense variants in 12 unrelated individuals with overlapping ID, hypotonia and dysmorphism)”
CDK8 disorder
literature · 10.1016/j.ajhg.2019.02.006 | 

| MONDO:0030059 | developmental and epileptic encephalopathy, 87 | Epileptic-encephalopathy / infantile-spasms enrichment | 

1 evidence

“*CDK19* by epileptic-encephalopathy/infantile-spasms enrichment”
CDK19 disorder
literature · 10.1016/j.ajhg.2020.04.001 | 

| MONDO:0016512 | Kabuki syndrome | KMT2D/KDM6A-positive on testing; MED13 should be considered in sequencing-negative Kabuki-like presentations | 

1 evidence

“a Kabuki-like facial presentation in a girl with prior negative *KMT2D*/*KDM6A* testing was resolved by exome sequencing as a de novo *MED13* p.Pro327Ser missense variant”
MED13 mimics Kabuki
literature · 10.1002/ajmg.a.61994 | 

## Treatments (8)

### speech therapy developmental

Highest-priority developmental intervention; screen specifically for speech apraxia.

MAXO: MAXO:0000930

Addresses: HP:0000750HP:0011098

Targets: node_06_neurodev_dysregulation

2 evidence

“The current treatment for this syndrome is occupational, speech, and psychological therapy.”
Core therapy set
literature · 10.7759/cureus.59904

“speech-language assessment should specifically screen for apraxia so that motor-speech techniques can be incorporated where indicated”
Apraxia screening
literature · 10.1007/s00439-018-1887-y

### occupational therapy developmental

Occupational and psychomotor therapy delivered alongside structured educational programme.

MAXO: MAXO:0001351

Addresses: HP:0001263HP:0001249

Targets: node_06_neurodev_dysregulation

1 evidence

“early enrolment in occupational therapy, physiotherapy/psychomotor therapy and structured educational support the second pillar of routine care”
OT/psychomotor pillar
literature · 10.7759/cureus.99683

### physical therapy developmental

Physiotherapy / psychomotor therapy for gross-motor delay and hypotonia.

MAXO: MAXO:0000011

Addresses: HP:0002194HP:0001252

1 evidence

“ongoing follow-up across neurodevelopmental paediatrics, otolaryngology, and physical medicine and rehabilitation”
PMR follow-up
literature · 10.7759/cureus.99683

### anticonvulsant agent therapy pharmacologic

When MED13-related epilepsy presents as infantile spasms/DEE, vigabatrin is reasonable to consider, particularly after first-line failure; anticipate drug resistance.

MAXO: MAXO:0000167

Addresses: HP:0012469HP:0001250HP:0011170

1 evidence

“While treatment with sodium valproate, phenobarbital, high-dose steroids and potassium bromide was ineffective, seizure control was finally achieved with vigabatrin.”
Vigabatrin response (n=1)
literature · 10.1038/s41439-025-00327-x

### echocardiography surveillance

Baseline transthoracic echocardiography after molecular diagnosis.

MAXO: MAXO:0010203

Addresses: HP:0001627

1 evidence

“their patient underwent transthoracic echocardiography, renal ultrasonography and ophthalmological evaluation — all normal in that case”
Baseline surveillance set
literature · 10.7759/cureus.99683

### ophthalmologist evaluation surveillance

Baseline ophthalmological evaluation; refractive correction as indicated.

MAXO: MAXO:0000703

Addresses: HP:0000478HP:0009921

1 evidence

“early corrective treatment of eye/vision abnormalities can improve prognosis”
Early ophthalmologic correction (expert extrapolation)
literature · 10.3389/fped.2025.1699544

### genetic counseling counselling

Recurrence-risk counselling: predominantly de novo (low risk with parental-mosaicism residual); 50% per-pregnancy risk in inherited minority with incomplete penetrance.

MAXO: MAXO:0000079

1 evidence

“MED13 syndrome is an autosomal-dominant condition in which pathogenic variants are predominantly de novo, but a small, well-documented minority of cases are vertically transmitted”
Inheritance counselling basis
literature · 10.1007/s00439-018-1887-y

### behavioral intervention behavioural

ASD/ADHD management extrapolated from idiopathic practice; consider video-EEG before escalating ASM if seizure semiology atypical (PNES).

MAXO: MAXO:0000882

Addresses: HP:0000729HP:0007018

1 evidence

“psychogenic non-epileptic seizures (PNES) diagnosed at age 17 and managed pharmacologically under psychiatry”
PNES recognised; psychiatry management
literature · 10.7759/cureus.59904

## Prevalence (2)

Worldwide (literature) — <1/1,000,000 (ultra-rare; ~28 individuals from 26 families reported)

“To date, only 26 patients carrying MED13 variants have been documented in the literature”
Cumulative literature count
10.3389/fped.2025.1699544 · 10.3389/fped.2025.1699544

DD/ID cohorts (de novo enrichment) — 7 de novo / 30,884 alleles (p=0.00371)

“seven de novo *MED13* variants in 30,884 alleles from large DD/ID cohorts yielded p = 0.00371”
Enrichment in DD/ID cohorts
10.1007/s00439-018-1887-y · 10.1007/s00439-018-1887-y

## Clinical trials (1)

| nct | phase | status | intervention | 

| NCT01238250 | N/A (observational) | RECRUITING | Observational natural-history registry (Simons Searchlight) | 

## Datasets (15)

| accession | repository | title | description | 

| GSE298801 | GEO |  | Cardiomyocyte-specific Med13/Med13l double-KO RNA-seq (mouse) | 

| GSE275182 | GEO |  | Drosophila wing-disc CKM-subunit (incl. Med13) clonal RNA-seq | 

| GSE250492 | GEO |  | MED13 IDR overexpression in human U2OS cells | 

| GSE147366 | GEO |  | RNA-seq of HAP1 WT vs MED13 KO clones (human) | 

| GSE90710 | GEO |  | MED13 in zygotic genome activation (porcine/mouse) | 

| GSE124117 | GEO |  | Regulation of cardiac transcription by thyroid hormone and Med13 (mouse) | 

| GSE62450 | GEO |  | MED13cTg heart ventricles and epididymal fat (mouse) | 

| GSE52343 | GEO |  | Cdk8/CycC/Med12/Med13 depletion expression (Drosophila) | 

| GSE35902 | GEO |  | Cardiac over-expression of Med13 (mouse) | 

| GSE35903 | GEO |  | Cardiac over-expression of Med13, non-cardiac tissue (mouse) | 

| GSE35904 | GEO |  | Med13 overexpression (mouse) | 

| GSE165033 | GEO |  | Mediator kinase module necessary for fructose regulation of liver glycogen (mouse hepatocyte Med13 KO) | 

| GSE188551 | GEO |  | CDK-Mediator dual role in Polycomb topology and ESC priming (mouse ESC) | 

| GSE233372 | GEO |  | IDR-dependent mechanism for nuclear-receptor control of Mediator interaction | 

| AF-Q9UHV7-F1 | AlphaFold |  | AlphaFold predicted structure of human MED13 (Q9UHV7), 2174 aa, model v6 | 

## Animal/experimental models (10)

| organism | model | models_node | 

| NCBITaxon:10090 | In utero shRNA knockdown of Med13 in embryonic neocortex (E14.5→E17.5) | node_06_neurodev_dysregulation | 

| NCBITaxon:10090 | Cardiomyocyte-specific Med13/Med13l double conditional knockout (tamoxifen-inducible) | node_07_paralog_redundancy | 

| NCBITaxon:10090 | Cardiac-specific Med13 transgenic overexpression and conditional deletion (miR-208a axis) | node_04_haploinsufficiency_lof | 

| NCBITaxon:7227 | skuld (skd/Med13) loss-of-function and clonal CKM-subunit depletion | node_01_ckm_hinge_anchor | 

| NCBITaxon:6239 | let-19/mdt-13 mutants in axon-guidance, vulval-fate and proneural-factor assays | node_06_neurodev_dysregulation | 

| NCBITaxon:7955 | med13a / med13b orthologs (Alliance high-confidence) | node_01_ckm_hinge_anchor | 

| NCBITaxon:4932 | SSN2/Med13 deletion and stress-induced degradation models | node_08_stress_autophagy_cycc_release | 

| NCBITaxon:10090 | Med13l+/- heterozygous mouse (paralog model) | node_07_paralog_redundancy | 

| system | description | models_node | 

| CL:0002319 | MED13+/- human iPSC line differentiated to cortical neural progenitors and organoids — proposed minimal model; not yet generated. | node_06_neurodev_dysregulation | 

| CL:0002322 | Mouse ESC CKM-composition manipulation shifts pluripotency state. | node_02_ckm_core_occupancy | 

## External assertions (2)

ClinGen Gene-Disease Validity: MED13 — complex neurodevelopmental disorder (MONDO:0100038), AD, classification Definitive (SOP9), Intellectual Disability and Autism GCEP, released 2022-05-17 · link

MONDO/OLS4: MONDO:0032485 'intellectual developmental disorder 61'; xrefs: DOID:0061034, GARD:0018514, MEDGEN:1684867, OMIM:618009, UMLS:C5231400 · link

## References (40 cited in this entry)

10.1002/ajmg.a.34222

10.1002/ajmg.a.61994

10.1002/ajmg.a.62238

10.1002/dvdy.70079

10.1002/humu.23626

10.1007/s00439-018-1887-y

10.1007/s00439-023-02636-z

10.1016/j.ajhg.2010.04.006

10.1016/j.ajhg.2019.02.006

10.1016/j.ajhg.2020.04.001

10.1016/j.cell.2012.03.029

10.1016/j.cell.2015.07.059

10.1016/j.ejmg.2024.104932

10.1016/j.jmccpl.2025.100481

10.1016/j.molcel.2024.09.001

10.1016/j.seizure.2022.09.002

10.1016/j.xhgg.2025.100467

10.1016/j.ydbio.2013.02.009

10.1016/j.yexcr.2020.112215

10.1038/ejhg.2014.69

10.1038/gim.2015.30

10.1038/s41436-019-0557-3

10.1038/s41436-021-01242-6

10.1038/s41439-025-00327-x

10.1038/s42003-026-09704-w

10.1073/pnas.0607483103

10.1080/15548627.2023.2259708

10.1101/gad.1767009

10.1101/gad.207720.112

10.1126/sciadv.abd4484

10.1128/mcb.00993-08

10.1158/0008-5472.can-07-1320

10.1186/s12920-024-01857-z

10.1242/dev.00607

10.15698/mic2018.08.641

10.3389/fped.2025.1699544

10.3390/biology8010003

10.4161/trns.1.1.12373

10.7759/cureus.59904

10.7759/cureus.99683

## Provenance 

{
  "creation_date": "2026-06-24",
  "updated_date": "2026-06-24",
  "curation_history": [
    {
      "date": "2026-06-24",
      "agent": "data-validation (the pipeline  P19\u2192Deliverable-2)",
      "change": "Initial curation entry generated from review.md (post-P19) + db_evidence; DisMech kb/disorders/MED13_Syndrome.yaml HELD OUT (not consulted)."
    }
  ],
  "notes": [
    "DisMech kb/disorders/MED13_Syndrome.yaml HELD OUT \u2014 this entry was generated independently for post-hoc comparison.",
    "No Orphanet entry exists for MED13 syndrome (verified via OLS4 obo_xref on MONDO:0032485).",
    "snippet validity: all literature evidence snippets are verbatim spans from the post-P19 review.md, not from source abstracts.",
    "applicable-but-uncurated gaps: biochemical (no analyte readouts established), histopathology (single autopsy report only), computational_models (none published), surrogate_endpoints (none defined)."
  ]
}

---

# Part 2 — Post-hoc comparison against the held-out dismech entry

> **⚠️ AI—Generated Content — Not Medical Advice**
>
> This document was generated with substantial AI assistance and is not medical advice. It is a research literature synthesis intended for scientific and educational use. It has not been independently reviewed by a licensed physician for clinical accuracy and must not be used as a substitute for professional medical advice, diagnosis, or treatment. Patients, caregivers, and clinicians should rely on qualified healthcare providers and primary sources for any decision regarding a medical condition. AI systems can produce errors, including plausible-sounding statements that are incorrect; verify every claim against the cited primary literature before use. We are pursuing this work with our research partners because we want AI to become more useful in helping people learn about health and medical topics. One day, further research and testing may bring us to a different point — but today is not that day. This is early-stage work, and AI should not be interpreted as providing medical advice or as any substitute for qualified professional care.

# DisMech vs the pipeline — MED13 syndrome (post-hoc comparison)

**Generated:** 2026-06-24T04:54:22Z
**Hold-out discipline:** The DisMech `kb/disorders/MED13_Syndrome.yaml` page (and its rendered HTML
at dismech.monarchinitiative.org) were declared `held_out_sources` in `scope.json` and embedded in
every Phase-2→19 task; no the pipeline sub-agent fetched or read them. This document is the *first* read
of that page in the MED13 run, for comparison only — neither the review nor the curation entry was
edited in light of it.

## 1. The two products

| | the pipeline MED13 (this run) | DisMech `MED13_Syndrome` |
|---|---|---|
| Format | 72-pp narrative review (PDF/HTML/MD) + structured `med13_curation-entry.yaml` | 59 KB structured YAML page |
| Disease term | MONDO:0032485 | MONDO:0032485 |
| Gene term | HGNC:22474 | HGNC:22474 |
| Reference base | **130 DOIs** (review body); 147-DOI Phase-2 corpus | **12 PMIDs** |
| Evidence items (snippet-backed) | 1,010 claim–citation triples (P15); 109 in curation-entry | 49 |
| Mechanism / pathophysiology nodes | 8 (curation-entry) + §02 narrative | 7 |
| HPO phenotypes | 33 (curation-entry); 23 (HPO/OMIM:618009) + literature n/N(%) tabulated | 22 |
| Treatments | MAXO terms (curation-entry) | 4 |
| Datasets | 14 curated GEO (curation-entry); 53 GEO + 1 ClinicalTrials (db_evidence) | 2 (clinicaltrials:NCT01238250, geo:GSE298801) |
| Model organisms | Alliance: MGI/ZFIN/FlyBase + literature §08/§10 | (none — `genetic` block only) |
| Verification | 1,010-triple 5-step deep check, 96.5% CLEAN, 0 hallucinated/chimeric/broken-DOI | repo `validate_hook.py` |

## 2. Reference overlap

The 12 DisMech PMIDs resolve via NCBI eutils to 12 DOIs. **11 of 12 (92%) are in the pipeline 
130-DOI review body** (PMID:29325037, PMID:29740699, PMID:33258286, PMID:33390853, PMID:36087421, PMID:38745205, PMID:38854223, PMID:40989238, PMID:41195223, PMID:41561257, PMID:41663567). The one not in the review:

- **PMID:25422356 (DOI 10.15252/emmm.201404218)** — *"MED13-dependent signaling from the heart confers leanness by enhancing metabolism in adipose tissue and liver."* (Baskin et al. 2014, *EMBO Mol Med*). A mouse
  cardiac-Med13 metabolic-signalling paper from the Olson laboratory; the pipeline's basic-biology
  cluster covers the same mechanistic axis through Grueter et al. 2012 (`grueter2012`,
  miR-208a/Med13) and the §09 Hypothesis 4 (miR-208a/MED13 metabolic axis), but did not pull this
  specific follow-up paper. It is also absent from the 147-DOI Phase-2 corpus, so it was filtered
  at scoping rather than at synthesis.

| Set | n |
|---|---|
| the pipeline review DOIs | 130 |
| DisMech PMIDs | 12 |
| In both | 11 |
| DisMech-only | 1 |
| `pipeline module ` | **119** |

## 3. HPO overlap

The the pipeline `med13_curation-entry.yaml` carries **33 HPO terms** (literature + OMIM-HPO).
Against DisMech's 22, **9 overlap** (HP:0000252, HP:0000750, HP:0001249, HP:0001250, HP:0001252, HP:0001263, HP:0001627, HP:0007018, HP:0009921).
DisMech-only: 13 terms (HP:0000238, HP:0000271, HP:0000407, HP:0000587, HP:0000717, HP:0000924, HP:0001105, HP:0001270, HP:0001273, HP:0001510, HP:0002019, HP:0002251, HP:0011069). The two HPO sets are drawn from
different curation methods (DisMech curators vs literature-extracted with n/N traceability), and
the pipeline  review additionally tabulates literature n/N(%) per phenotype (§03/§05) rather than
VERY_FREQUENT/FREQUENT/OCCASIONAL bins.

The OMIM-HPO official annotation for OMIM:618009 (23 terms) overlaps DisMech
on only 5 terms — both pipelines extend well beyond the official annotation.

## 4. Dataset overlap

DisMech lists 2 datasets: `geo:GSE298801` and `clinicaltrials:NCT01238250`. **Both are in
the pipeline `db_evidence`** (GSE298801 among 53 GEO accessions; NCT01238250 = Simons Searchlight,
identified independently). the pipeline's curation-entry curates **14** of the 53 to MED13/CKM-perturbation experiments; the 53-accession list is the result of running GEO
unconditionally (the pipeline-fix carried forward from the MED13L run, where conditional
GEO querying left `research.datasets` empty).

## 5. What the pipeline  review adds beyond the DisMech page

1. **Reference depth.** 130 vs 12 references; 119 references not in DisMech, including the
   2024–2026 case series (yang2025, fazio2025, pintoalberto2025, harada2025, tolmacheva2024), the
   cross-CKM mechanistic literature (Davis 2013 Fbw7-degron, Hanley 2024 selective autophagy,
   Chao 2024 cryo-EM), and the model-organism literature.
2. **Quantitative phenotype frequencies.** the pipeline §03/§05 give literature-derived n/N(%) per
   phenotype with claim-source-sentence traceability (e.g. MRI abnormality 5/16; gross motor delay
   7/13); DisMech uses Orphanet-style frequency enums.
3. **Cross-CKM-disorder inference (§08).** No DisMech analogue: the pipeline  review's principal
   thesis (substituting cross-paralog inference for cohort scale at n≈28) and the §08 transferable
   / non-transferable feature table have no slot in the DisMech schema.
4. **Translational hypotheses (§09).** Four labelled hypotheses (Fbw7-degron stabilisation;
   neural-progenitor migration as missense readout; selective-autophagy modulation of MED13
   turnover; miR-208a/MED13 metabolic axis as systemic-phenotype modifier) — DisMech has no
   hypothesis block.
5. **Model organisms.** the pipeline §08/§10 + db_evidence (Alliance: MGI:3029632 Med13, ZFIN
   med13a/med13b, FB:FBgn0003415 *skd*) — DisMech's MED13 page has no model-organism block.
6. **Integrity provenance.** Every numeric claim has a P16-verified claim_source_sentence + DOI;
   the run carries `verification_triples.json` (n=1,010), `gate_verification.json`, and
   `fix_ledger.json` (35/35 fixes applied, 0 unresolved).

## 6. What DisMech captures that the pipeline did not

1. **PMID:25422356** (Baskin 2014, *EMBO Mol Med*) — cardiac Med13 → systemic-metabolism mouse
   study. the pipeline's §09 Hypothesis 4 covers the same axis via grueter2012; adding baskin2014 to a
   future revision would strengthen that hypothesis's evidence base.
2. **13 HPO terms** present in DisMech but not in the pipeline  `med13_curation-entry.yaml`
   (33 terms). (Separately, 17 of DisMech's 22 terms are absent from the official
   OMIM:618009 HPO annotation — both pipelines extend beyond it; see §3.) These 13 are the
   actionable cross-check set against the pipeline  phenotype tables.


## 7. Assessment

The the pipeline MED13 review is a **strict superset on references** (11/12 DisMech PMIDs included; 119
additional DOIs), a **strict superset on datasets** (both DisMech entries plus 51 additional GEO
accessions), and **adds analytical layers** (cross-CKM inference, quantitative phenotype
frequencies, four labelled hypotheses, model-organism coverage, claim-triple verification) that the
DisMech schema does not accommodate. The one DisMech-only reference is a basic-biology mouse paper
whose mechanistic content the pipeline  review reaches via a different paper from the same group. On
HPO terms the two curations are complementary rather than nested.

The hold-out was effective: the 11/12 PMID and 2/2 dataset overlaps arise because both
pipelines independently retrieved the core MED13-syndrome literature and the same two structured
resources, not because one was derived from the other.

## 8. Provenance

| Artifact | vid |
|---|---|
| the pipeline review.md (P19) | — |
| the pipeline med13_review_v1.pdf | — |
| references.bib (130) | — |
| db_evidence.json | — |
| DisMech MED13_Syndrome.yaml (read-only snapshot) | — |
| gate_verification (P16) | — |
| comparison computed data | `handoff/cmp_data.json` |

*DisMech page first commit 2026-04-15, last commit 2026-06-19. the pipeline MED13 run 2026-06-24.*
