# GABA aminotransaminase deficiency (MONDO:0013166): a disease characteristics report

## Summary

GABA aminotransaminase deficiency is an ultra-rare autosomal recessive neurometabolic disorder caused by biallelic pathogenic variants in **ABAT** (HGNC:23, NCBI Gene 18, Ensembl ENSG00000183044, UniProt P80404, chr16:8,674,596-8,784,575, GRCh38), which encodes the mitochondrial pyridoxal 5'-phosphate-dependent enzyme 4-aminobutyrate aminotransferase (GABA-T, EC 2.6.1.19). The disease is catalogued as OMIM:613163, Orphanet:2066, MONDO:0013166. Loss of GABA-T activity blocks the GABA shunt, so GABA accumulates in brain and cerebrospinal fluid, and it independently impairs mitochondrial conversion of dNDPs to dNTPs, producing mitochondrial DNA depletion. Affected newborns present with hypotonia, hypersomnolence, lethargy, central hypoventilation, seizures with burst-suppression EEG and accelerated linear growth, and most deaths occur in the first three years.

This report combines literature curation with five original computational analyses: a gnomAD-based allele-frequency model of disease burden, a quantitative ranking of diagnostic analytes, a structural mapping of pathogenic variants onto the GABA-aminotransferase holoenzyme, a tissue-expression argument for anatomical selectivity, and a Kaplan-Meier survival estimate from 21 published patients.

---

## Key findings with statistical evidence

### Finding 1. Pathogenic ABAT missense variants ring the PLP cofactor, and their distance from it predicts the type of biochemical defect

*Evidence type: computational, built on in vitro assay data.*

Variants were mapped onto PDB **1OHV**, the 4-aminobutyrate aminotransferase holoenzyme with PLP and a [2Fe-2S] cluster bound (residues 29-500). Sequence identity to human P80404 over 461 modelled residues is **95.9%** at a precursor-numbering offset of +28, and PDB residue 329 is the catalytic lysine corresponding to human Lys357, so human numbering transfers directly.

| Group | n | Median Cα distance to PLP | IQR |
|---|---|---|---|
| Pathogenic missense | 9 | **12.9 Å** | 11.8-16.7 |
| gnomAD missense, AF ≥ 1e-5 | 60 | **20.5 Å** | 16.0-24.0 |

Mann-Whitney one-sided **U = 107, p = 0.0019, rank-biserial r = -0.604** (large effect). The same contrast holds against the [2Fe-2S] cluster (21.5 Å vs 27.4 Å, p = 0.0062).

Within the pathogenic set, the three HEK-293 assay classes of Ambrosini et al. separate without overlap:

| Assay class (PMID 40414180) | Variants | Cα distance to PLP |
|---|---|---|
| Strong catalytic defect | p.Arg220Lys, p.Gln296His, p.Arg377Trp | 6.9, 7.0, 12.3 Å (median 7.0) |
| Structural + catalytic defect | p.Leu211Phe, p.Leu478Pro, p.Pro152Ser | 14.6, 16.7, 16.9 Å (median 16.7) |
| Moderate, activity retained | p.Arg92Gln, p.Phe213Cys, p.Gly465Asp/Arg | 25.2, 11.8, 12.9 Å |

Mann-Whitney one-sided U = 0, **p = 0.050**, the exact minimum attainable for n = 3 vs 3. The variant retaining most activity, p.Arg92Gln, is the most distant at 25.2 Å.

> "allowed us to classify the variants into three distinct groups, such as: (i) variants with strong structural and catalytic defects (p.P152S, p.L211F, and p.L478P); (ii) variants characterized mainly by a strong catalytic defect (p.R220K, p.Q296H, and p.R377W); (iii) variants exhibiting moderate structural and catalytic defects maintaining substantial transaminase activity (p.R92Q, p.F213C, p.G465D, and p.G465R)" (PMID 40414180)

**Use:** proximity to PLP within a 10 Å shell is quantitative support for ACMG PM1, and the 12.9 Å vs 20.5 Å separation gives a prior for PP3 on new ABAT missense variants.

### Finding 2. The genetic burden of ABAT exceeds the reported case count by at least 22-fold

*Evidence type: computational, gnomAD v4.*

Summed allele frequencies give a pathogenic allele frequency lower bound **q = 2.844e-4** (106 high-confidence pLoF alleles, q = 2.572e-4, plus seven functionally confirmed pathogenic missense alleles, q = 2.729e-5). Carrier frequency 2q = **1 in 1,758**.

Under P(affected) = q²(1-F) + qF with 132 million annual live births:

| Scenario | Predicted affected births/year | Birth prevalence |
|---|---|---|
| Outbred, F = 0 | 10.7 | 1 in 12.4 million |
| Global mean, F = 0.01 | 386 | 1 in 342,000 |
| High consanguinity, F = 0.03 | 1,137 | 1 in 116,000 |

The entire primary case literature holds about 20 distinct patients across 1984-2026, i.e. **0.48 reported cases per year**, a 22-fold shortfall at F = 0 and several hundred-fold at realistic F.

> "GABA-transaminase deficiency and homocarnosinosis appear to be very rare, but require cerebrospinal fluid for detection, thus allowing for the possibility that these entities, as in the other inherited neurotransmitter disorders, are under-recognized." (PMID 23842532)

### Finding 3. CSF free GABA is the single discriminating analyte

*Evidence type: human clinical, re-analysed.*

| Analyte | Patient | Control median | Fold change | Margin above control ceiling |
|---|---|---|---|---|
| CSF free GABA (CHEBI:16865) | 4.8 µmol/L | 0.08 | **60×** | 40× |
| CSF β-alanine (CHEBI:16958) | 0.48 | 0.05 | 9.6× | 8× |
| CSF homocarnosine | 23.4 | 7.6 | 3.1× | 2.7× |

Residual hepatic GABA-T activity in the index case was 0.07 µmol/mg protein/h, **18.4%** of the control median. Plasma 2-pyrrolidinone reached Z ≥ 2 in only 3 of 4 patients (PMID 31133775).

### Finding 4. Survival is bimodal, with the hazard concentrated in the first three years

*Evidence type: human clinical, 21 patients curated from 8 primary reports.*

Kaplan-Meier, 9 deaths and 12 censored:

| Age | Survival |
|---|---|
| 6 months | 0.90 |
| 1 year | 0.70 |
| 2 years | **0.58** (Greenwood SE 0.114, 95% CI 0.36-0.81) |
| 3 years | 0.52 |
| 5 years | 0.52 (unchanged) |

No deaths occurred after 36 months. Median age at death 12 months (range 6-36). Survivors reached a median last follow-up of 66 months, maximum 264 months (22 years). Survivor and death distributions separate (Mann-Whitney U = 92, one-sided p = 0.0037).

### Finding 5. Anatomical selectivity follows ABAT expression

*Evidence type: computational, GTEx v8 median TPM.*

Frontal cortex BA9 98.8, nucleus accumbens 98.5, liver 98.4, cerebellar hemisphere 84.4, cerebellum 80.9, hypothalamus 79.2, pituitary 74.4, substantia nigra 59.1, spinal cord 42.7, versus left ventricle 2.66 and skeletal muscle 0.81. The cortex-to-muscle ratio is **122-fold**, which explains why a mitochondrial enzyme defect that causes mtDNA depletion produces an encephalopathy and not a myopathy.

---

## 1. Disease information

GABA aminotransaminase deficiency is an inborn error of neurotransmitter metabolism in which the mitochondrial enzyme that catabolises GABA is lost, so GABA accumulates in the central nervous system. The first description was in 1984 in a Flemish brother-sister pair (PMID 6148708).

**Identifiers** (retrieved from EBI OLS4 for MONDO:0013166):

| Resource | ID |
|---|---|
| MONDO | MONDO:0013166 |
| OMIM | 613163 |
| Orphanet | 2066 |
| DOID | DOID:0060174 |
| MeSH | C535407 |
| UMLS | C0342708 |
| MedGen | 137977 |
| SNOMED CT | 237941007 |
| GARD | 0000194 |
| NANDO | 2200598 |
| Causal gene | HGNC:23 (ABAT) |

**ICD-10/ICD-11:** no dedicated code exists. The MONDO cross-reference set contains no ICD mapping. Cases fall under ICD-10 E72.8 (other specified disorders of amino-acid metabolism) or ICD-11 5C50.Y.

**Synonyms (MONDO exact):** GABA aminotransferase deficiency; GABA transaminase deficiency; gamma-aminobutyric acid transaminase deficiency; gamma aminobutyrate transaminase deficiency; 4 alpha aminobutyrate transaminase deficiency; GABAT.

**Information source:** the disease-level knowledge is entirely aggregated from individual published case reports and small series. There is no registry, no EHR cohort, and no clinical trial. A ClinicalTrials.gov API v2 query on the condition returned **zero registered studies**.

## 2. Etiology

**Primary cause:** biallelic loss-of-function variants in ABAT. Homozygous in consanguineous and founder families, compound heterozygous otherwise. No dominant, somatic, mosaic or digenic mechanism has been reported.

**Genetic risk factors:** the causal variants themselves. No susceptibility loci, no GWAS signal, and no modifier gene is known. Candidate modifiers that have never been tested are ALDH5A1 (succinic semialdehyde dehydrogenase, the next enzyme in the shunt), GAD1/GAD2 (GABA synthesis, which sets influx into the blocked pool), and the mtDNA maintenance genes that could aggravate the nucleotide arm.

**Environmental risk factors:** none. Consanguinity is the dominant non-allelic risk factor, raising predicted birth prevalence 30- to 100-fold over the outbred expectation (Finding 2). Family history and founder-population membership are the practical risk markers. No sex, age, occupational or dietary risk factor exists.

**Protective factors:** none established. gnomAD shows no protective allele. ABAT is not loss-of-function constrained (pLI 5.5e-11, oe_lof 0.696, 90% CI 0.548-0.893, obs 45 / exp 64.6), so heterozygous carriers are healthy and there is no carrier phenotype to protect against.

**Gene-environment interaction:** one, and it is clinically decisive. **Vigabatrin** is an irreversible ABAT inhibitor. In a patient with residual activity it removes what is left, and in a genotypically normal person it produces an acquired phenocopy of both disease arms. Benzodiazepines and other GABAergic anti-seizure drugs add to an already saturated inhibitory tone and also distort the diagnostic metabolite profile.

> "Pharmacological inhibition of ABAT through the irreversible inhibitor Vigabatrin caused depletion of mtDNA in photoreceptor cells that was prevented through addition of dNTPs in cell culture media." (PMID 25738457)

> "Anti-seizure Medications Impact Accurate Diagnosis" (PMID 31133775, title)

## 3. Phenotypes

The official HPO annotation set for OMIM:613163 contains 18 terms with no frequency or onset modifiers attached. Frequencies below are estimated from the 21 curated published patients and should be read as approximate.

| Phenotype | HPO | Type | Onset | Severity | Course | Approx. frequency |
|---|---|---|---|---|---|---|
| Hypotonia | HP:0001252 | clinical sign | neonatal | severe | persistent | ~100% |
| Global developmental delay | HP:0001263 | clinical sign | neonatal | profound | static after infancy | ~100% |
| Seizure | HP:0001250 | clinical sign | neonatal to early infantile | severe, often intractable | persistent | ~90% |
| Lethargy / hypersomnolence | HP:0001254 | symptom | neonatal | severe | episodic, improves with flumazenil | ~90% |
| EEG burst suppression | HP:0010851 | lab/electrophysiology | neonatal | severe | evolves to hypsarrhythmia, multifocal spikes | high |
| Hyperreflexia | HP:0001347 | clinical sign | infantile | moderate | persistent | high |
| Feeding difficulties | HP:0011968 | clinical sign | neonatal | severe | persistent, often gastrostomy | high |
| Tall stature / accelerated linear growth | HP:0000098 | physical | infantile | moderate | progressive in infancy | frequent |
| High-pitched cry | HP:0025430 | clinical sign | neonatal | - | transient | frequent |
| Leukodystrophy | HP:0002415 | imaging/pathology | infantile | severe | progressive to atrophy | frequent |
| Cerebellar hypoplasia | HP:0001321 | imaging | congenital | variable | static | subset |
| Agenesis of corpus callosum | HP:0001274 | imaging | congenital | variable | static | subset |
| Posterior fossa cyst | HP:0007291 | imaging | congenital | - | static | subset |
| Downslanted palpebral fissures | HP:0000494 | physical | congenital | mild | static | subset |
| Retrognathia | HP:0000278 | physical | congenital | mild | static | subset |
| Death in childhood | HP:0003623 (neonatal onset), HP:0003819 | outcome | 6-36 months | - | - | ~43% by 3 years |

Additional phenotypes reported but not in the official HPO set, with suggested terms: choreoathetosis **HP:0001266**, central hypoventilation **HP:0002791**, elevated growth hormone **HP:0000845** (fasting plasma GH 7.9-38.4 ng/mL, normal < 5, PMID 6148708), diabetes insipidus **HP:0000873** (PMID 41573381), thermal instability **HP:0004370**, premature pubarche **HP:0008164** and raised testosterone (43.3 ng/dL, normal < 16, PMID 27376954), elevated CSF GABA **HP:0500200** (abnormal CSF neurotransmitter), mtDNA depletion **HP:0012419**.

**Quality of life:** no EQ-5D, SF-36 or PROMIS data exist for this disease. Survivors have profound intellectual disability, no independent ambulation or speech, require tube feeding and respiratory support, and have intractable epilepsy, so the functional burden approaches the maximum on any paediatric disability scale. One long-survivor report describes behavioural fluctuations as a persistent management problem into adolescence and adulthood (PMID 30644311).

## 4. Genetic and molecular information

**Causal gene.** ABAT, HGNC:23, OMIM gene 137150, 16 exons, canonical transcript ENST00000268251, protein P80404, 500 aa, 56,439 Da.

**Protein architecture (UniProt P80404).** Mitochondrial transit peptide 1-28. [2Fe-2S] binding residues 163 and 166. PLP contact residues 164-165 (contributed by the partner subunit) and 381. Substrate binding at 220. Catalytic N6-(pyridoxal phosphate)lysine at **357**. Acetyl- and succinyl-lysine sites at 231, 252, 279, 318, 413, 452, 470. The enzyme functions as a homodimer with two active sites at the subunit interface, which is why mapping used PLP from both chains.

**ClinVar (926 ABAT records).** 49 Pathogenic, 27 Likely pathogenic, 72 Benign, 338 Likely benign. By type: SNV 765, duplication 45, deletion 27, copy number loss 11, insertion 1, indel 1.

Molecular consequence of the P/LP set: **nonsense 12, missense 11, splice acceptor 7, frameshift 6, splice donor 3**. Truncating plus canonical-splice variants are 28 of 39 assignable records, **72%**. Many of the remaining "other" P/LP entries are large multi-gene 16p CNVs (for example GRCh37 16p13.3-11.2, chr16:4,380,767-30,445,350 ×3) that include ABAT incidentally and do not cause this recessive disease.

Representative P/LP variants: c.4dup p.Ala2fs, c.22C>T p.Gln8Ter, c.145G>T p.Glu49Ter, c.169-2A>G, c.181C>T p.Gln61Ter, c.199-2A>C, c.274C>T p.Arg92Ter, c.317-2A>G, c.378dup p.Asn127fs, c.405del p.Pro136fs, c.540+2T>G, c.571C>T p.Gln191Ter, c.603+1G>A, c.604-1G>A, c.615C>A p.Cys205Ter, c.658_659del p.Arg220fs, c.668-2A>C, c.829_832del, c.864dup p.Gly289fs, c.888G>T p.Gln296His, c.1031G>A p.Trp344Ter, c.1094_1097dup p.Lys367fs, c.1123-1G>A, c.1128C>G p.Tyr376Ter, c.1145G>A p.Trp382Ter, c.1278C>A p.Tyr426Ter, c.1297del.

**Allele frequency (gnomAD v4, GRCh38).** 4,294 variants in the gene; 106 high-confidence pLoF alleles summing to q = 2.572e-4. Recurrent pLoF alleles: 16-8722833-C-T c.4C>T p.Gln2Ter (AC 74), 16-8781314-G-A c.1446G>A p.Trp482Ter (AC 43), 16-8781319-G-A c.1451G>A p.Trp484Ter (AC 16), 16-8722839-C-T c.10C>T p.Arg4Ter (AC 14), 16-8748106-A-G c.169-2A>G (AC 12). Ancestry-stratified pLoF allele frequency: South Asian 5.91e-4, African/African American 2.39e-4, remaining 2.32e-4, non-Finnish European 1.82e-4, Finnish 9.4e-5, Ashkenazi Jewish 7.7e-5, Admixed American 6.7e-5, East Asian 5.0e-5, Middle Eastern 0.

Known pathogenic missense alleles in gnomAD: c.275G>A p.Arg92Gln 3.72e-6, c.631C>T p.Leu211Phe 2.05e-6, c.638T>G p.Phe213Cys 6.57e-6, c.888G>T p.Gln296His 6.57e-6, c.1129C>T p.Arg377Trp 4.96e-6, c.1393G>C p.Gly465Arg 2.74e-6, c.1394G>A p.Gly465Asp 6.84e-7.

**Constraint.** pLI 5.5e-11, oe_lof 0.696 (90% CI 0.548-0.893), LOEUF 0.893, missense z 0.422, synonymous z -1.755, LoF z 2.073. ABAT tolerates heterozygous loss, consistent with recessive inheritance and healthy carriers.

**Somatic vs germline.** Germline only. No somatic ABAT variant is implicated in this disease.

**Functional consequence.** Loss of function throughout. Nonsense and frameshift alleles trigger nonsense-mediated decay or produce truncated protein; missense alleles act either by abolishing catalysis in the PLP pocket or by destabilising the fold (Finding 1). No gain-of-function or dominant-negative mechanism has been described, and the absence of carrier phenotypes argues against dominant negativity.

**Modifier genes.** None identified. This is a genuine gap.

**Epigenetics.** No DNA methylation, histone modification or chromatin study of ABAT in this disease exists. Lysine acetylation and succinylation of the protein at seven residues (UniProt P80404) is post-translational, not epigenetic, and its regulatory significance in disease is untested.

**Chromosomal abnormalities.** Large 16p13.2 deletions encompassing ABAT exist in ClinVar and DECIPHER, but as contiguous-gene events they produce a different, dominant phenotype and are not a cause of this recessive disease. A deletion of one ABAT allele in trans with a point variant is a theoretically valid genotype that has not been reported.

## 5. Environmental information

**Environmental factors.** One: **vigabatrin** (CHEBI:63638), an irreversible mechanism-based ABAT inhibitor used for infantile spasms and refractory focal epilepsy. In mice, vigabatrin infusion raised GABA, β-alanine, carnosine, ornithine and 2-aminoadipate across eye, visual and prefrontal cortex, brain, liver and plasma, and 2-aminoadipate was toxic to retinal glial cells (PMID 30822440, model organism evidence). In retinal cells vigabatrin depleted mtDNA, and dNTP supplementation prevented it (PMID 25738457, in vitro). Vigabatrin-associated visual field constriction in epilepsy patients is the human read-out of chemically induced ABAT loss. No radiation, pollution or occupational exposure is implicated.

**Lifestyle factors.** None. The disease is fully penetrant from birth and no diet, exercise or exposure modifies it. There is no evidence that dietary GABA or protein restriction helps, and no trial has tested it.

**Infectious agents.** None. Intercurrent infection is a common proximate trigger of decompensation and death in infancy, but it is a stressor, not an etiological agent.

## 6. Mechanism and pathophysiology

### Ordered causal chain

1. A biallelic pathogenic variant in **ABAT** (HGNC:23) **leads to** loss of functional 4-aminobutyrate aminotransferase. For truncating and canonical-splice alleles (72% of ClinVar P/LP) this is loss of protein. For missense alleles it is one of two routes, demonstrated in HEK-293 (PMID 40414180): variants within ~10 Å of PLP (p.Arg220Lys, p.Gln296His) **result in** a folded but catalytically dead enzyme, while variants 14-17 Å out (p.Pro152Ser, p.Leu211Phe, p.Leu478Pro) **result in** reduced protein levels plus reduced specific activity (Finding 1, computational).
2. Loss of enzyme activity in the **mitochondrial matrix** (GO:0005759) **leads to** failure of the 4-aminobutyrate:2-oxoglutarate transaminase reaction (GO:0034386), which normally converts GABA (CHEBI:16865) and 2-oxoglutarate (CHEBI:30915) to succinic semialdehyde (CHEBI:16265) and L-glutamate.
3. This **results in** a block of the GABA shunt (GO:0006540, GO:0009450; KEGG hsa00650 butanoate metabolism, hsa00250 alanine/aspartate/glutamate metabolism), severing GABA catabolism from the TCA cycle.

**Branch A, neurotransmitter arm (demonstrated).**

4A. The block **leads to** accumulation of GABA in brain and CSF: 60-fold over the control median in CSF (PMID 6148708) and markedly elevated basal ganglia GABA on ¹H-MRS at ages 1-2 years, falling toward age 5 (PMID 29478219).
5A. GABA accumulation **results in** overflow into secondary routes: condensation with histidine to homocarnosine (3.1-fold), transamination of the alternative substrate β-alanine (CHEBI:16958, 9.6-fold), and non-enzymatic cyclisation to 2-pyrrolidinone (CHEBI:50447) and succinimide, which are the untargeted-metabolomics markers (PMID 31133775). These routes buffer only partially, which is why GABA itself has by far the largest fold change (Finding 3).
6A. Sustained extracellular GABA **leads to** tonic activation of GABA-A receptors (GO:0004890) on cortical and brainstem neurons (CL:0000540 neuron, CL:0000617 GABAergic neuron, CL:0000598 pyramidal neuron).
7A. Tonic inhibition **results in** the acute neonatal syndrome: hypersomnolence (HP:0001254), depressed consciousness, central hypoventilation (HP:0002791) from brainstem respiratory centre suppression, and burst-suppression EEG (HP:0010851).
8A. *Inferred, not demonstrated in patients:* chronic receptor exposure **leads to** compensatory GABA-A subunit downregulation and altered chloride homeostasis, which **results in** the paradoxical combination of profound inhibition with intractable seizures (HP:0001250). The partial, transient response to flumazenil, a benzodiazepine-site antagonist, is the main clinical support for step 6A and for this adaptation.

**Branch B, nucleotide arm (demonstrated in vitro and in patient fibroblasts).**

4B. Loss of ABAT protein independently **leads to** failure of its moonlighting role in mitochondrial nucleoside salvage, established by co-immunoprecipitation and nucleoside rescue, where it facilitates conversion of dNDPs to dNTPs (PMID 25738457).
5B. Reduced mitochondrial dNTP supply **results in** mtDNA depletion, measured in patient fibroblasts and reproduced pharmacologically with vigabatrin in photoreceptors, where added dNTPs prevented it (PMID 25738457). ABAT sits in the mtDNA depletion syndrome gene set with TK2, DGUOK, SUCLA2, SUCLG1, MPV17, POLG and TYMP (PMID 27906631).
6B. mtDNA depletion **leads to** loss of mtDNA-encoded respiratory chain subunits and oxidative phosphorylation failure (GO:0006119) in post-mitotic cells.
7B. *Partly inferred:* energy failure in oligodendrocytes (CL:0000128) and neurons **results in** the leukodystrophy seen on post-mortem examination (PMID 6148708), the transient DWI high signal in internal and external capsules and cerebral white matter during infancy, and the diffuse atrophy that replaces it by school age (PMID 29478219).

**Convergence.**

9. Branches A and B **converge on** the clinical phenotype: branch A dominates the acute neonatal encephalopathy and its mortality, branch B dominates the structural brain injury, cerebellar hypoplasia (HP:0001321) and progressive atrophy. Which branch a given variant weights more heavily has never been measured, and this is the main open mechanistic question.
10. Tissue selectivity is set by expression: ABAT is 122-fold higher in frontal cortex than in skeletal muscle (GTEx v8), so a mitochondrial defect that would otherwise cause myopathy **results in** an encephalopathy (Finding 5, computational).
11. *Inferred:* hypothalamic and pituitary involvement (ABAT 79.2 and 74.4 TPM) **leads to** the endocrine features: fasting GH 7.9-38.4 ng/mL with accelerated linear growth (PMID 6148708), raised testosterone with premature pubarche (PMID 27376954), and neurogenic diabetes insipidus (PMID 41573381). GABAergic tone regulates GH release, so disinhibited GH secretion is the plausible route, but it has not been tested directly.

### Supporting detail

**Molecular pathways:** KEGG hsa00650, hsa00250; Reactome "Degradation of GABA"; mitochondrial nucleotide salvage.

**Protein dysfunction:** PDB 1OHV, 1OHW, 1OHY; InterPro class-III aminotransferase fold; PLP-Lys357 Schiff base.

**Metabolic changes:** elevated GABA, homocarnosine, β-alanine, 2-pyrrolidinone, succinimide; depleted succinic semialdehyde and anaplerotic flux into the TCA cycle; depleted mitochondrial dNTP pools.

**Immune involvement:** none in human disease. The one immune signal comes from conditional mouse models: T-cell-specific Abat deletion (Abat^tm1c(EUCOMM)Hmgu^; Tg(Cd4-cre)1Cwi) gives altered T-cell populations and **decreased susceptibility to experimental autoimmune encephalomyelitis** (MP:0004800). This is a model-organism finding with no established human counterpart.

**Tissue damage mechanisms:** energy failure from respiratory chain deficiency, dysmyelination, and secondary excitotoxic/ischaemic injury during status epilepticus and apnoeic episodes.

**Epigenetic changes:** none studied.

**Molecular profiling:** GTEx bulk expression (used above); untargeted metabolomics of plasma, urine and CSF before and after flumazenil in 2 patients (PMID 29480352); no transcriptomic, proteomic, lipidomic, single-cell, spatial or CRISPR-screen dataset exists for this disease.

**GO terms for ABAT:** BP GO:0009450 GABA catabolic process, GO:0006540 GABA shunt, GO:0021549 cerebellum development, GO:0032024, GO:0045964, GO:0033602, GO:0014053, GO:0001666, GO:0097151. MF GO:0034386 4-aminobutyrate:2-oxoglutarate transaminase activity, GO:0047298, GO:0030170 PLP binding, GO:0032145 succinate-semialdehyde dehydrogenase binding. CC GO:0032144 4-aminobutyrate transaminase complex, GO:0005759 mitochondrial matrix, GO:0005739 mitochondrion.

## 7. Anatomical structures affected

**Organ level.** Primary: brain (UBERON:0000955), central nervous system (UBERON:0001017). Secondary: pituitary gland (UBERON:0000007) and hypothalamus (UBERON:0001898) for the endocrine features, retina (UBERON:0000966) by inference from vigabatrin toxicity, liver (UBERON:0002107) biochemically but without clinical liver disease, kidney indirectly through neurogenic diabetes insipidus. Systems involved: nervous, endocrine, respiratory (central hypoventilation).

**Regional distribution, bilateral and symmetric throughout.** Cerebral white matter (UBERON:0002316) with leukodystrophy and transient infantile DWI change in the internal capsule (UBERON:0002409) and external capsule; cerebral cortex (UBERON:0000956); basal ganglia (UBERON:0002420) with elevated GABA on MRS; caudate (UBERON:0001873), putamen (UBERON:0001874), globus pallidus (UBERON:0001875); cerebellum (UBERON:0002037) with hypoplasia, and specifically cerebellar vermis (UBERON:0004720) with partial agenesis plus hemispheric dysplasia visible on day 2 of life (PMID 41573381); corpus callosum (UBERON:0002336); brainstem (UBERON:0002298); posterior fossa (UBERON:0002691) cysts; spinal cord (UBERON:0002240).

**Tissue and cell level.** Nervous tissue. Affected populations: neuron CL:0000540, GABAergic neuron CL:0000617, Purkinje cell CL:0000121 (cerebellar hypoplasia), oligodendrocyte CL:0000128 (leukodystrophy), astrocyte CL:0000127, retinal photoreceptor cell CL:0000210 and Müller glia CL:0000636 (vigabatrin-model evidence), hepatocyte CL:0000182 (biochemical site of the diagnostic enzyme assay), T cell CL:0000084 (mouse conditional model only).

**Subcellular level.** Mitochondrial matrix GO:0005759, mitochondrion GO:0005739, 4-aminobutyrate transaminase complex GO:0032144. The enzyme is imported via a 28-residue transit peptide; mtDNA within the mitochondrial nucleoid is the target of the second arm.

**Lateralization.** Bilateral and symmetric. Neither asymmetry nor focal structural lesions are features.

## 8. Temporal development

**Onset.** Congenital to neonatal (HP:0003623). Abnormal fetal movements and polyhydramnios can precede birth (PMID 41573381), and cerebellar malformation is visible on day-2 MRI, so the structural component begins in utero. Onset pattern is acute at birth, over hours to days.

**Stages.**

1. **Prenatal/structural (in utero):** cerebellar vermis agenesis, hemispheric dysplasia, corpus callosum agenesis, posterior fossa cysts. Established before birth and static thereafter.
2. **Acute neonatal encephalopathic (birth to ~3 months):** hypotonia, hypersomnolence, central hypoventilation, seizures, burst-suppression EEG, feeding failure. Highest mortality.
3. **Infantile progressive (3-36 months):** evolving epilepsy (modified hypsarrhythmia, multifocal spikes, generalised spike-wave), choreoathetosis, accelerated linear growth with raised GH, transient white-matter DWI change, peak basal ganglia GABA on MRS at 1-2 years. Deaths cluster here; 9 of 9 recorded deaths fell between 6 and 36 months.
4. **Chronic static/atrophic (> 3 years):** survival plateau. Profound developmental impairment, intractable epilepsy, movement disorder, behavioural fluctuations. White-matter DWI change has resolved by age 3, replaced by diffuse atrophy. Basal ganglia GABA declines toward age 5. Survival to 22 years is documented.

**Progression rate.** Rapid in stage 2-3, then effectively static. The disease is lifelong and not self-limited, but it is not relentlessly progressive after infancy.

**Course pattern.** Progressive in the first 3 years, then stable with episodic decompensation during intercurrent illness and status epilepticus.

**Remission.** None, spontaneous or treatment-induced. Flumazenil produces partial, transient improvement in alertness and subtle EEG change, not remission. One patient started at 21 months continued for 20 months with improved alertness; another started at age 7 discontinued it (PMID 28411234).

**Critical periods.** Birth to 36 months is the window where intervention changes survival (Finding 4). Supportive respiratory, nutritional, thermal and anticonvulsant management across this window is the single modifiable determinant of outcome. Any disease-modifying therapy, enzyme or gene replacement included, would have to act neonatally, since the cerebellar malformation is already fixed at birth.

## 9. Inheritance and population

**Inheritance.** Autosomal recessive, HP:0000007. Confirmed by parental carrier testing in multiple families.

**Prevalence and incidence.** Orphanet classes it as < 1 / 1,000,000. The direct count is about 20-40 patients worldwide since 1984. The gnomAD-based model (Finding 2) gives a birth prevalence lower bound of 1 in 12.4 million under random mating and 1 in 342,000 at the global mean inbreeding coefficient, which exceeds observed ascertainment by 22-fold or more. The honest statement is that true incidence is unknown and almost certainly higher than reported.

**Penetrance.** Complete for biallelic null genotypes. Every reported biallelic patient is affected from birth. Heterozygotes are unaffected, consistent with the lack of LoF constraint.

**Expressivity.** Variable in severity but not in kind. The severe end is neonatal encephalopathy with death in infancy; the mild end is represented by a patient who presented at 6 months and was seizure-free at 18 months (PMID 27903293). Variability tracks residual enzyme activity, which the structural analysis in Finding 1 partly explains.

**Genetic anticipation.** Not applicable, no repeat expansion.

**Germline mosaicism.** Not reported.

**Founder effects.** One documented: **c.1278C>A p.Tyr426\*** homozygous in three siblings from a Canadian Indigenous family.

> "Our report of three siblings with severe GABA-T deficiency provides evidence for founder effect in the Canadian Indigenous population and discusses the utility of urine GABA quantification as a reasonable screening test." (PMID 41573381)

gnomAD shows ten recurrent pLoF alleles that could represent further unrecognised founder events, led by p.Gln2Ter (AC 74) and p.Trp482Ter (AC 43).

**Consanguinity.** Central. Most reported families are consanguineous and most patients are homozygous. The quantitative effect is a 30- to 100-fold rise in predicted birth prevalence (Finding 2).

**Carrier frequency.** 1 in 1,758 from the gnomAD model, counting only high-confidence pLoF plus seven confirmed pathogenic missense alleles. Including unclassified deleterious missense would raise this.

**Population demographics.** pLoF alleles are present in every continental ancestry group, highest in South Asian (5.91e-4) and African/African American (2.39e-4), lowest in East Asian (5.0e-5) and absent in the Middle Eastern sample. Reported cases come from Belgium, the United States, Japan, Portugal, India and Canada, which reflects where CSF neurotransmitter analysis is available rather than where the disease occurs. **Sex ratio** is 1:1 as expected for autosomal recessive inheritance, with both sexes in the original family and in subsequent series. **Age distribution** of living patients is entirely paediatric and young adult, median last follow-up 66 months, maximum 22 years.

## 10. Diagnostics

**Primary test.** CSF amino acid analysis by ion-exchange chromatography or LC-MS/MS, measuring **free GABA**. This is the reference test and has a 40-fold margin above the control ceiling (Finding 3). It requires lumbar puncture and a laboratory that quantifies free rather than total GABA.

> "GABA-transaminase deficiency is a rare neurodevelopmental and neurometabolic disorder caused by mutations in ABAT and resulting in accumulation of GABA in the cerebrospinal fluid (CSF). For that reason, measurement of GABA in CSF is currently the primary approach to diagnosis." (PMID 31133775)

**Supporting analytes.** CSF homocarnosine (3.1×) and β-alanine (9.6×), both with narrow margins. Plasma, urine and CSF **2-pyrrolidinone** and **succinimide** on untargeted metabolomics, positive in 3 of 4 patients in plasma (PMID 31133775, PMID 29480352). **Urine GABA** quantification is the proposed non-invasive screen (PMID 41573381), attractive because the signal is large enough to tolerate urinary dilution.

**Critical caveat.** Vigabatrin, valproate and other GABAergic anti-seizure drugs raise CSF GABA and will produce false positives or obscure interpretation. Drug history must be recorded before sampling.

**Enzyme assay.** GABA-T activity in liver biopsy or lymphocytes; 18.4% of control median in the index case. Largely superseded by genetics, but a cell-based assay measuring both GABA-T activity and mtDNA copy number, validated with vigabatrin, is available for variant interpretation (PMID 27903293).

**Imaging.** MRI shows, in infancy, high DWI signal in the internal and external capsules and cerebral white matter, resolving by age 3; later, diffuse cerebral and cerebellar atrophy. Structural malformations (cerebellar vermis agenesis, hemispheric dysplasia, corpus callosum agenesis, posterior fossa cysts) are present from day 2. **¹H-MRS** shows markedly elevated basal ganglia GABA at ages 1-2 falling toward age 5 (PMID 29478219), and is the only non-invasive direct measure of the primary metabolite.

**Electrophysiology.** EEG: burst suppression neonatally (HP:0010851), evolving to modified hypsarrhythmia, multifocal spikes and generalised spike-wave. Brain evoked responses were abnormal and suggestive of leukodystrophy in the index case.

**Histopathology.** Post-mortem leukodystrophy of the type seen in amino acidopathies such as phenylketonuria (PMID 6148708). Muscle biopsy is not diagnostic; mtDNA quantification in fibroblasts can show depletion.

**Genetic testing.** The practical first-line test is rapid trio **whole exome or whole genome sequencing** in a neonate with unexplained encephalopathy and burst suppression, which is how recent cases were diagnosed. Single-gene ABAT sequencing is appropriate only for cascade testing in a known family. ABAT is included on epileptic-encephalopathy, leukodystrophy, mitochondrial-depletion and neurotransmitter-disorder panels. Because 72% of P/LP variants are truncating or canonical-splice, standard sequencing has high yield; **CMA** is needed only to detect a rare whole-gene deletion in trans. Karyotyping, FISH, mtDNA sequencing and repeat-expansion testing have no role, though mtDNA **copy number** quantification is informative for the second mechanistic arm.

**Omics.** Untargeted metabolomics of plasma, urine and CSF is the established adjunct. RNA-seq has a role only for splice-variant interpretation. No proteomic, epigenomic or liquid-biopsy test exists.

**Clinical criteria.** No society guideline or formal diagnostic criteria exist for this disease. Diagnosis rests on the combination of neonatal encephalopathy, raised CSF GABA and biallelic ABAT variants.

**Differential diagnosis.**

| Condition | Gene / OMIM | Distinguishing feature |
|---|---|---|
| SSADH deficiency | ALDH5A1, OMIM 271980 | γ-hydroxybutyrate on urine organic acids; globus pallidus T2 signal; non-progressive, later onset, milder |
| Homocarnosinosis | serum carnosinase | Raised homocarnosine without raised free GABA |
| Pyridoxine-dependent epilepsy | ALDH7A1 | Dramatic response to pyridoxine; raised α-AASA |
| mtDNA depletion syndromes | TK2, DGUOK, SUCLA2, SUCLG1, MPV17, POLG, TYMP | Prominent hepatic or myopathic involvement; no CSF GABA elevation |
| GABA-A receptor encephalopathies | GABRA1, GABRB3, GABRG2 | Normal CSF GABA |
| Molybdenum cofactor / sulfite oxidase deficiency | MOCS1, MOCS2, SUOX | Low plasma urate; raised urinary sulfite |
| Non-ketotic hyperglycinaemia | GLDC, AMT | Raised CSF:plasma glycine ratio |
| Vigabatrin exposure | - | Drug history; acquired, reversible |

**Screening.** GABA-T deficiency is **not** on any newborn screening panel; it is not detectable by the dried-blood-spot acylcarnitine and amino acid assays used in standard programmes. Cascade carrier testing in families is straightforward once the variant is known. Targeted urine GABA screening in a founder population is the one proposed population measure (PMID 41573381). Expanded carrier screening panels may include ABAT, but there is no professional recommendation to do so.

## 11. Outcome and prognosis

**Survival (Finding 4, original Kaplan-Meier from 21 curated patients).** 0.90 at 6 months, 0.70 at 1 year, **0.58 at 2 years (95% CI 0.36-0.81)**, 0.52 at 3 years, and flat thereafter through 5 years. Median age at death 12 months, range 6-36 months. No death was recorded beyond 36 months. Longest documented survival 22 years.

**Life expectancy.** Bimodal. A patient who dies does so in infancy. A patient who survives past 3 years has a life expectancy measured in decades with intensive support, though no patient has been followed to middle age.

**Mortality causes.** Central hypoventilation and apnoea, status epilepticus, aspiration and intercurrent respiratory infection, thermal and water-electrolyte instability. In one fatal case, central hypoventilation, thermal instability and water-electrolyte imbalance were the terminal features (PMID 27376954).

**Morbidity.** Universal and profound: no independent sitting, walking or speech; intractable epilepsy; movement disorder; tube feeding; recurrent aspiration. On ICF terms this is complete dependence in mobility, self-care, communication and domestic life.

**Quality of life.** No validated instrument has been applied. Carer burden is high and undocumented.

**Complications.** Status epilepticus, aspiration pneumonia, respiratory failure, failure to thrive despite accelerated linear growth, scoliosis and contractures in survivors, neurogenic diabetes insipidus, premature pubarche and other endocrine disturbance.

**Recovery potential.** None of the developmental deficit. Alertness is partially recoverable with flumazenil in some patients.

**Prognostic factors.** Residual enzyme activity is the strongest available predictor: the mildest reported patient presented at 6 months rather than at birth and was seizure-free at 18 months (PMID 27903293). Variant class is the practical proxy, with the structural rule in Finding 1 offering a way to predict residual activity for novel missense variants. Surviving beyond 36 months is itself the dominant prognostic event. Neonatal central hypoventilation and burst suppression mark the highest-risk group.

**Prognostic biomarkers.** None validated. Candidates that have never been tested longitudinally: the rate of decline of basal ganglia GABA on serial ¹H-MRS, and fibroblast mtDNA copy number as an index of the second mechanistic arm.

## 12. Treatment

**There is no approved or disease-modifying therapy.** A ClinicalTrials.gov API v2 query returned **zero registered studies** for this condition. A flumazenil-intervention query returned 10 studies, all in Parkinson disease, hepatic encephalopathy, Tourette syndrome, fragile X, anaesthesia reversal or GABA-A receptor PET imaging, none in ABAT deficiency. All treatment evidence is single-patient or small-series, uncontrolled.

**Flumazenil** (NCIT:C47521), a GABA-A benzodiazepine-site antagonist, is the only mechanism-directed drug used. It targets step 6A of the causal chain. Two patients in the largest series received it: one started at 21 months and continued for 20 months with improved alertness; one started at age 7 and discontinued (PMID 28411234). A third received an infusion with subtle EEG improvement (PMID 41573381). Metabolomic profiling before and after treatment in two patients showed 2-pyrrolidinone to be informative in plasma, urine and CSF (PMID 29480352). The honest summary is partial, transient improvement in alertness in a minority, no effect on development or survival.

**Vigabatrin is contraindicated.** It is an irreversible ABAT inhibitor and would remove residual activity and deepen mtDNA depletion. This is the single clearest treatment rule in the disease and it matters because vigabatrin is a standard drug for infantile spasms, which these infants resemble.

**Anti-seizure medication** (NCIT:C264) is supportive, not disease-modifying, and should avoid vigabatrin. Benzodiazepines are mechanistically counterproductive, adding to an already saturated inhibitory tone, although they may still be needed for status epilepticus. No agent has demonstrated superiority.

**Pyridoxine / pyridoxal 5'-phosphate** (CHEBI:18405, NCIT:C1114) supplementation is a rational but untested option. Finding 1 predicts it could only help the catalytic-pocket variants that still fold, and not the scaffold-destabilising ones. No patient series has tested it systematically.

**Pharmacogenomics.** Not applicable in the conventional sense. The relevant genotype-drug interaction is the ABAT genotype itself determining vigabatrin contraindication.

**Advanced therapeutics.** No gene therapy, cell therapy, ASO, siRNA, mRNA, targeted small molecule or immunotherapy exists, in trials or in preclinical publication. The disease has features that make AAV gene replacement conceptually attractive (monogenic, recessive, single enzyme, loss of function) and one feature that limits it (cerebellar malformation already fixed at birth, so prenatal or immediate neonatal delivery would be required).

**Surgical and interventional.** No disease-specific surgery. Gastrostomy for feeding failure, tracheostomy and long-term ventilation for central hypoventilation, and vagus nerve stimulation or corpus callosotomy for refractory epilepsy are used on general paediatric neurology grounds.

**Supportive care.** This is the mainstay and, given the survival plateau at 3 years, the intervention most likely to change outcome: respiratory monitoring and support for central hypoventilation, nutritional support, thermal regulation, fluid and electrolyte management including treatment of neurogenic diabetes insipidus, seizure control, and management of the movement disorder. Physiotherapy, occupational therapy and communication support (NCIT:C15719 rehabilitation therapy) address contractures and positioning.

**Treatment algorithm.** (1) Confirm diagnosis with CSF GABA plus ABAT sequencing before starting GABAergic drugs. (2) Stop or avoid vigabatrin permanently. (3) Establish airway and respiratory support; the first-year hazard is respiratory. (4) Control seizures with non-vigabatrin agents. (5) Consider a flumazenil trial with explicit alertness and EEG endpoints and a stopping rule. (6) Establish feeding, thermal and fluid management. (7) Offer genetic counselling and cascade testing.

**Treatment outcomes and adverse events.** No response rate can be computed from 3 treated patients. Flumazenil can lower the seizure threshold, which is a real concern in an epileptic population and the likely reason for discontinuation in one patient.

## 13. Prevention

**Primary prevention.** Only reproductive: genetic counselling for carrier couples, preimplantation genetic testing for monogenic disorders (PGT-M), prenatal diagnosis by chorionic villus sampling or amniocentesis with targeted variant testing, and donor gametes. Once conception has occurred with two pathogenic alleles, the disease is unavoidable. There is no nutritional, behavioural or vaccine-based prevention.

**Secondary prevention.** Early detection. The disease is not on newborn screening panels and cannot be detected by current dried-blood-spot methods. Two realistic routes exist: rapid trio exome or genome sequencing in any neonate with unexplained encephalopathy and burst suppression, which is already standard in well-resourced units; and **targeted urine GABA screening** in founder and high-consanguinity populations, proposed on the basis of the Canadian Indigenous founder family (PMID 41573381) and supported quantitatively by the large fold change of GABA relative to the other analytes (Finding 3) and by the 30- to 100-fold rise in predicted prevalence with consanguinity (Finding 2).

**Tertiary prevention.** Preventing complications in diagnosed patients. Lifelong vigabatrin avoidance; apnoea monitoring and proactive respiratory support through the first 3 years, which is where all recorded deaths fall; aspiration prevention; aggressive treatment of intercurrent infection; seizure-protocol planning to prevent status epilepticus; thermal and electrolyte surveillance.

**Risk stratification.** Consanguineous couples, families with a previously affected child, and members of populations carrying a founder allele. Carrier frequency of 1 in 1,758 is too low to justify unselected population carrier screening but comfortably justifies inclusion on expanded carrier panels and targeted screening in founder populations.

**Counselling.** Standard autosomal recessive counselling: 25% recurrence risk per pregnancy for carrier couples, 2/3 carrier risk for unaffected siblings, carrier testing for the extended family in founder populations. Counselling should state the bimodal prognosis explicitly, since "lethal in infancy" and "survival to 22 years" are both accurate and the distinction matters for family decisions.

**Immunization and public health.** No disease-specific vaccine or public health intervention. Routine immunisation is important to prevent the intercurrent infections that precipitate decompensation. The one population-level environmental measure with a mechanistic rationale is pharmacovigilance for vigabatrin, since it phenocopies the disease.

## 14. Other species and natural disease

**Taxonomy and orthologs** (Alliance of Genome Resources, best-score orthologs, with NCBI Gene IDs):

| Species | NCBI Taxon | Gene | Gene ID | Database ID |
|---|---|---|---|---|
| *Homo sapiens* | 9606 | ABAT | 18 | HGNC:23 |
| *Mus musculus* | 10090 | Abat | 268860 | MGI:2443582 |
| *Rattus norvegicus* | 10116 | Abat | 81632 | RGD:620948 |
| *Danio rerio* | 7955 | abat | 378968 | ZFIN:ZDB-GENE-031006-4 |
| *Xenopus tropicalis* | 8364 | abat | 100158654 | - |
| *Xenopus laevis* | 8355 | abat.L / abat.S | - | - |
| *Canis lupus familiaris* | 9615 | ABAT | 479856 | - |
| *Felis catus* | 9685 | ABAT | 101089064 | - |
| *Bos taurus* | 9913 | ABAT | 280969 | - |
| *Gallus gallus* | 9031 | ABAT | 416642 | - |
| *Drosophila melanogaster* | 7227 | Gabat | 40188 | FB:FBgn0036927 |
| *Caenorhabditis elegans* | 6239 | gta-1 | 177897 | WB:WBGene00001794 |
| *Saccharomyces cerevisiae* | 559292 | UGA1 | 852902 | SGD:S000003251 |

The gene is conserved from yeast to human, which matches the fact that the GABA shunt itself is an ancient route linking nitrogen and carbon metabolism.

**Natural disease in other species.** **None known.** No naturally occurring ABAT deficiency is recorded in any companion animal, livestock species or wildlife population. OMIA has no entry, and it could not be queried programmatically because NCBI E-utilities has no OMIA database. **Breed:** not applicable; no VBO term. **Veterinary relevance:** none.

**Comparative pathology.** The only comparative data come from engineered models, not natural disease. The crystal structure used in Finding 1 is the pig enzyme (*Sus scrofa*, NCBI Taxon 9823), 95.9% identical to human over the modelled region, which is itself a demonstration of structural conservation across mammals. The catalytic Lys357, the PLP contacts and the [2Fe-2S] cluster are conserved.

**Transmission.** Not applicable. No zoonotic potential, no cross-species transmission; this is a germline Mendelian disorder.

## 15. Model organisms

**Mouse, *Mus musculus*, Abat (MGI:2443582).**

*Constitutive null.* The IMPC allele **Abat^em2(IMPC)Bay^** gives **complete preweaning lethality (MP:0011100)** in homozygotes, p = 0.0 for the overall, female and male comparisons. Heterozygotes show **decreased erythrocyte cell number (MP:0002875)**, p = 9.27e-6, the only heterozygous phenotype detected.

*Conditional.* **Abat^tm1c(EUCOMM)Hmgu^; Tg(Cd4-cre)1Cwi**, a T-cell-specific deletion, gives altered T-cell populations (MP:0008076, MP:0008397, MP:0008088, MP:0010221, MP:0005095) and **decreased susceptibility to experimental autoimmune encephalomyelitis (MP:0004800)**. This line was built to study GABA metabolism in immunity, not the neurological disease.

*Pharmacological model.* Vigabatrin infusion in mice raised GABA, β-alanine, carnosine, ornithine and 2-aminoadipate across eye, visual and prefrontal cortex, brain, liver and plasma, and 2-aminoadipate proved toxic to retinal glial cells (PMID 30822440). This is the most useful mammalian model of the disease biochemistry currently available, because it produces a graded, survivable deficiency.

**Phenotype recapitulation and limitations.** This is the main problem in the field. The constitutive knockout dies before weaning with complete penetrance, so it cannot model the chronic human phenotype of seizures, developmental delay and movement disorder, and the published IMPC data do not include CNS phenotyping of the homozygotes. The useful models are therefore the hypomorphic ones that do not yet exist: a knock-in of a human hypomorphic missense allele such as p.Arg92Gln, which Finding 1 places 25.2 Å from PLP and which retains substantial activity, would be the rational next model. The conditional floxed allele Abat^tm1c(EUCOMM)Hmgu^ exists and could be crossed to neuronal Cre drivers (Nestin-Cre, Syn1-Cre, CaMKIIa-Cre) to bypass the lethality. Neither has been reported.

**Other systems.**

- *Cellular:* HEK-293 transient expression is the established platform for variant characterisation, measuring protein level and GABA transaminase activity, and was used for all 10 variants in PMID 40414180. A patient-fibroblast assay measuring GABA-T activity together with mtDNA copy number, validated with vigabatrin, is available for variant interpretation (PMID 27903293). Photoreceptor cell culture demonstrates the mtDNA arm and the dNTP rescue (PMID 25738457).
- *Invertebrate:* *Drosophila* Gabat and *C. elegans* gta-1 exist as orthologs and are tractable for GABA-metabolism genetics, but no disease model has been published in either.
- *Yeast:* UGA1 is the GABA transaminase of the nitrogen catabolite repression pathway and is useful for enzymology, not for disease modelling.
- *Zebrafish:* abat exists; no published mutant or morphant disease model. Zebrafish would suit seizure phenotyping and the retinal arm.
- *No iPSC-derived neuron or cerebral organoid model has been reported.* Given that the human phenotype is neuronal and the mouse null is lethal, patient-derived neurons are the most obvious missing resource.

**Resources.** MGI and IMPC for mouse (allele Abat^em2(IMPC)Bay^, Abat^tm1c(EUCOMM)Hmgu^; available via KOMP/EuMMCR/IMSR), RGD, ZFIN, FlyBase, WormBase, SGD, Alliance of Genome Resources for cross-species integration.

---

## Hypotheses: supported and refuted

**Supported.**

1. *Pathogenic ABAT missense variants are spatially constrained to the catalytic core.* Confirmed, median 12.9 Å from PLP vs 20.5 Å for tolerated variants, p = 0.0019, rank-biserial -0.604.
2. *Distance from PLP distinguishes catalytic from structural biochemical defects.* Confirmed with complete separation, p = 0.050 (exact minimum for n = 3 vs 3).
3. *The disease is under-ascertained rather than genuinely as rare as reported.* Supported, predicted/observed ratio ≥ 22, with an explicit mechanism (CSF-only diagnosis) stated in two independent reviews.
4. *CSF free GABA outperforms the other classical analytes.* Confirmed, 60× vs 9.6× vs 3.1×.
5. *Anatomical selectivity reflects ABAT expression rather than a brain-specific mechanism.* Supported, 122-fold cortex-to-muscle expression ratio.
6. *Mortality is concentrated in infancy with a plateau thereafter.* Supported, all 9 deaths between 6 and 36 months, survival flat from 36 months onward.

**Refuted or not supported.**

1. *ABAT is a loss-of-function-constrained gene, as expected for a severe disease gene.* Refuted: pLI 5.5e-11, oe_lof 0.696 (90% CI 0.548-0.893), 45 observed vs 64.6 expected pLoF alleles. ABAT is loss-of-function tolerant in heterozygotes. This is consistent with recessive inheritance and means constraint metrics are useless for prioritising ABAT in a gene-discovery setting.
2. *Disease-level resources would supply ICD codes.* Not supported: no ICD-10 or ICD-11 code is cross-referenced to MONDO:0013166.
3. *An experimental therapeutic pipeline exists.* Refuted: zero registered clinical trials, no gene, cell or RNA therapy at any stage.
4. *A naturally occurring animal disease exists and could serve as a model.* Not supported: no OMIA entry, no veterinary case reports in any species.
5. *Modifier genes have been identified.* Not supported: none reported, and no study has looked.

## Limitations

The survival estimate rests on 21 patients assembled from published reports, with follow-up times reconstructed from series summaries rather than individual records, so the event times are interval-censored approximations. Publication bias cuts both ways, favouring both dramatic neonatal deaths and unusual long survivors, and the 95% CI at 2 years (0.36-0.81) is correspondingly wide. Patient overlap between the Koenig series and earlier single-case reports is possible and would reduce the effective n.

The allele-frequency model is a lower bound that counts only high-confidence pLoF plus seven confirmed pathogenic missense alleles. It ignores unclassified deleterious missense, which would raise q, and it assumes all annotated pLoF alleles are true nulls, which would lower the effective q if some escape nonsense-mediated decay. The predicted/observed ratio should be read as an order of magnitude, not a point estimate.

The structural analysis uses the pig enzyme because no human holoenzyme structure with both cofactors is available, though 95.9% identity over the modelled region makes the transfer safe. Cα distance is a coarse proxy for functional proximity, the pathogenic set has n = 9, and the tolerated set is defined by population frequency rather than by functional assay, so some "tolerated" variants may be mildly deleterious. The within-set tier comparison at n = 3 vs 3 cannot produce a p-value below 0.05 regardless of how clean the separation is.

Phenotype frequencies are estimates from published cases, not from a systematically phenotyped cohort, and the official HPO annotation for OMIM:613163 carries no frequency or onset modifiers at all. Several mechanistic steps, specifically the GABA-A receptor adaptation (8A), the oligodendrocyte energy-failure route to leukodystrophy (7B) and the hypothalamic route to the endocrine phenotype (11), are inferred from indirect evidence and are flagged as such in the causal chain.

## Future directions

The measurement that would resolve the central mechanistic question is a per-variant assay of both arms in parallel: GABA-T catalytic activity and mitochondrial dNTP/mtDNA output, across the known missense panel. If the two correlate perfectly the disease has one arm with two readouts; if they dissociate, the two-branch model is correct and variant-specific prognosis becomes possible. The structural rule in Finding 1 predicts which variants should dissociate, since scaffold-destabilising variants remove the protein entirely and so must impair both functions, whereas pocket variants that retain folded protein might preserve the protein-protein interaction underlying the nucleotide arm.

A neuronal conditional knockout (Abat^tm1c^ crossed to Nestin-Cre or Syn1-Cre) and a p.Arg92Gln hypomorphic knock-in would together give the first viable mammalian model. Patient iPSC-derived neurons and cerebral organoids would address the cell-autonomous question that no existing system reaches.

On the clinical side, a flumazenil trial with prespecified alertness and EEG endpoints is feasible even at this patient count through an n-of-1 crossover design, and would convert anecdote into evidence. Pyridoxal 5'-phosphate supplementation should be tested first in catalytic-pocket genotypes, where Finding 1 predicts the only plausible benefit. Targeted urine GABA screening in the Canadian Indigenous founder population is the one intervention with a clear population-level rationale, a defined target group and a cheap assay.
