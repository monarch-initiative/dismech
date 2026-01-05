---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2025-12-18T13:46:52.783169'
end_time: '2025-12-18T13:54:24.000344'
duration_seconds: 451.22
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: You-Hoover-Fong Syndrome
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 22
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** You-Hoover-Fong Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **You-Hoover-Fong Syndrome**.
Focus on the molecular and cellular mechanisms underlying disease progression.

### Required Information

#### 1. Core Pathophysiology
- What are the primary pathophysiological mechanisms?
- What molecular pathways are dysregulated?
- What cellular processes are affected?

#### 2. Key Molecular Players
- **Genes/Proteins**: Which genes are causally involved or implicated?
- **Chemical Entities**: What metabolites, drugs, or small molecules are relevant?
- **Cell Types**: Which cell types are primarily affected?
- **Anatomical Locations**: Which tissues/organs are involved?

#### 3. Biological Processes (for GO annotation)
- What biological processes (GO terms) are disrupted?
- Consider: signaling pathways, metabolic processes, cellular responses, transport, etc.

#### 4. Cellular Components
- Where in the cell do key processes occur?
- Consider: organelles, membrane compartments, extracellular space, etc.

#### 5. Disease Progression
- What is the sequence of events from initial trigger to clinical manifestation?
- Are there distinct stages or phases?

#### 6. Phenotypic Manifestations
- What are the key clinical phenotypes?
- How do they relate to the underlying mechanisms?

### Citation Requirements

- Cite primary literature (PMID preferred) for all mechanistic claims
- Prioritize recent reviews and landmark papers
- Include direct quotes where possible to support key statements

### Output Format

Structure your response as a narrative that could be used to populate a disease knowledge base entry with:
- Pathophysiology description
- Gene/protein annotations with ontology terms (HGNC, GO)
- Phenotype associations (HP terms)
- Cell type involvement (CL terms)
- Anatomical locations (UBERON terms)
- Chemical entities (CHEBI terms)
- Evidence items with PMIDs


## Output

Question: You are an expert researcher providing comprehensive, well-cited information.

Provide detailed information focusing on:
1. Key concepts and definitions with current understanding
2. Recent developments and latest research (prioritize 2023-2024 sources)
3. Current applications and real-world implementations
4. Expert opinions and analysis from authoritative sources
5. Relevant statistics and data from recent studies

Format as a comprehensive research report with proper citations. Include URLs and publication dates where available.
Always prioritize recent, authoritative sources and provide specific citations for all major claims.

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** You-Hoover-Fong Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **You-Hoover-Fong Syndrome**.
Focus on the molecular and cellular mechanisms underlying disease progression.

### Required Information

#### 1. Core Pathophysiology
- What are the primary pathophysiological mechanisms?
- What molecular pathways are dysregulated?
- What cellular processes are affected?

#### 2. Key Molecular Players
- **Genes/Proteins**: Which genes are causally involved or implicated?
- **Chemical Entities**: What metabolites, drugs, or small molecules are relevant?
- **Cell Types**: Which cell types are primarily affected?
- **Anatomical Locations**: Which tissues/organs are involved?

#### 3. Biological Processes (for GO annotation)
- What biological processes (GO terms) are disrupted?
- Consider: signaling pathways, metabolic processes, cellular responses, transport, etc.

#### 4. Cellular Components
- Where in the cell do key processes occur?
- Consider: organelles, membrane compartments, extracellular space, etc.

#### 5. Disease Progression
- What is the sequence of events from initial trigger to clinical manifestation?
- Are there distinct stages or phases?

#### 6. Phenotypic Manifestations
- What are the key clinical phenotypes?
- How do they relate to the underlying mechanisms?

### Citation Requirements

- Cite primary literature (PMID preferred) for all mechanistic claims
- Prioritize recent reviews and landmark papers
- Include direct quotes where possible to support key statements

### Output Format

Structure your response as a narrative that could be used to populate a disease knowledge base entry with:
- Pathophysiology description
- Gene/protein annotations with ontology terms (HGNC, GO)
- Phenotype associations (HP terms)
- Cell type involvement (CL terms)
- Anatomical locations (UBERON terms)
- Chemical entities (CHEBI terms)
- Evidence items with PMIDs


Plan
Objective 1: Identify recent literature (2023–2024) and key mechanistic sources on TELO2/TTT and You‑Hoover‑Fong syndrome (YHFS). Result: Located 2023 case report with literature review on TELO2‑related YHFS; 2023 mechanistic reviews on TTT–PIKK biology; and experimental NMD evidence for TELO2/CLK‑2 (C. elegans and mammalian links). (zhao2023novelcompoundheterozygous pages 1-2, bhadra2023ttt(tel2tti1tti2)complex pages 2-4, bhadra2023ttt(tel2tti1tti2)complex pages 7-9, feng2023exploringthefunctional pages 10-11, guo2021clk2tel2isa pages 6-9, guo2021clk2tel2isa pages 14-15, guo2021clk2tel2isa pages 4-6)
Objective 2: Extract core pathophysiology and molecular players. Result: TELO2 combines with TTI1/TTI2 to form the TTT co‑chaperone critical for co‑translational maturation and stability of PIKKs (ATM, ATR, PRKDC/DNA‑PKcs, MTOR, SMG1, TRRAP); CK2 phosphorylation tunes specificity (mTOR, SMG1). TELO2/CLK‑2 contributes to NMD primarily by stabilizing SMG1. (bhadra2023ttt(tel2tti1tti2)complex pages 2-4, bhadra2023ttt(tel2tti1tti2)complex pages 7-9, guo2021clk2tel2isa pages 14-15)
Objective 3: Map ontology-ready annotations. Result: See embedded artifact summarizing genes (HGNC names), processes (GO concept names), phenotypes (HP names), cell types (CL concept names), anatomical structures (UBERON names), and chemical entities (CHEBI names) with citations. (zhao2023novelcompoundheterozygous pages 1-2, ciaccio2021milderpresentationof pages 1-3, wang2019novelcompoundheterozygous pages 1-2, ciaccio2021milderpresentationof pages 5-6, guo2021clk2tel2isa pages 6-9, bhadra2023ttt(tel2tti1tti2)complex pages 2-4, guo2021clk2tel2isa pages 14-15, bhadra2023ttt(tel2tti1tti2)complex pages 7-9, feng2023exploringthefunctional pages 10-11, guo2021clk2tel2isa pages 4-6)
Objective 4: Synthesize disease progression sequence and phenotypic manifestations. Result: Constructed mechanistic narrative linking TELO2 loss‑of‑function to TTT destabilization, selective PIKK instability (especially SMG1 and mTOR via CK2‑regulated TELO2), impaired NMD and checkpoint/growth signaling, and neurodevelopmental phenotypes (ID/GDD, microcephaly), plus cataract and congenital malformations. (zhao2023novelcompoundheterozygous pages 1-2, ciaccio2021milderpresentationof pages 1-3, guo2021clk2tel2isa pages 6-9, guo2021clk2tel2isa pages 14-15)
Objective 5: Create artifact. Result: Artifact-00 table produced (ontology-ready). (see below)
Objective 6: Write comprehensive report with citations, URLs, and publication dates; embed artifact. Result: Provided below.
Objective 7: Submit final answer. Result: Complete.

Disease Pathophysiology Research Report

Target Disease
- Disease Name: You‑Hoover‑Fong Syndrome (TELO2‑related neurodevelopmental disorder; OMIM 616954)
- MONDO ID: Not specified in sources identified
- Category: Mendelian

1) Core Pathophysiology (key concepts, definitions, current understanding)
You‑Hoover‑Fong syndrome (YHFS) is an autosomal‑recessive neurodevelopmental disorder caused by biallelic loss‑of‑function variants in TELO2, which encodes a core subunit of the TTT (TELO2‑TTI1‑TTI2) co‑chaperone complex. TTT operates with R2TP and HSP90 to promote co‑translational maturation and stability of the phosphatidylinositol 3‑kinase–related kinase (PIKK) family, including ATM, ATR, PRKDC/DNA‑PKcs, MTOR, SMG1, and TRRAP. TELO2 deficiency destabilizes the TTT complex and reduces PIKK protein levels, leading to defects in DNA damage/replication checkpoints (ATM/ATR/PRKDC), growth signaling (mTOR), and mRNA surveillance (SMG1/NMD). Mechanistically, casein kinase 2 (CK2)‑mediated phosphorylation of TELO2 and TTI1 modulates TTT interactions and can selectively affect SMG1 and mTOR stability, implying pathway‑specific sensitivity to TELO2 perturbation. In vivo experimental evidence in C. elegans shows that CLK‑2 (TELO2 ortholog) is “a genuine player in the NMD pathway,” with genetic and reporter assays demonstrating NMD impairment upon clk‑2 loss; mammalian studies indicate that CK2‑dependent TELO2 phosphorylation augments NMD by increasing SMG1 stability. Together, these data support a model where TELO2 loss compromises PIKK proteostasis and NMD, producing a multisystem neurodevelopmental phenotype. (bhadra2023ttt(tel2tti1tti2)complex pages 2-4, bhadra2023ttt(tel2tti1tti2)complex pages 7-9, guo2021clk2tel2isa pages 6-9, guo2021clk2tel2isa pages 14-15)
- Key quotes:
  - “CLK‑2/TEL2 is a conserved component of the nonsense‑mediated mRNA decay pathway.” (PLoS ONE, Jan 2021) (guo2021clk2tel2isa pages 13-14) URL: https://doi.org/10.1371/journal.pone.0244505 (Jan 2021)
  - “CK2‑mediated TEL2 phosphorylation augments nonsense‑mediated mRNA decay (NMD) by increase of SMG1 stability.” (PLoS ONE, Jan 2021) (guo2021clk2tel2isa pages 14-15) URL: https://doi.org/10.1371/journal.pone.0244505 (Jan 2021)
  - “Conditional Tel2 deletion… causes checkpoint defects that correlate with reduced protein levels (but not mRNA levels) of all six mammalian PIKKs.” (IJMS, May 2023) (bhadra2023ttt(tel2tti1tti2)complex pages 2-4) URL: https://doi.org/10.3390/ijms24098268 (May 2023)
  - “TTT… promotes co‑translational maturation of the PIKKs” and Tel2 CK2‑site mutations “selectively reduce mTOR and SMG1 protein levels.” (IJMS, May 2023) (bhadra2023ttt(tel2tti1tti2)complex pages 7-9) URL: https://doi.org/10.3390/ijms24098268 (May 2023)

2) Recent developments and latest research (prioritizing 2023–2024)
- Clinical: A 2023 case report with literature review expanded the TELO2 variant spectrum by identifying novel compound heterozygous variants (p.K749X, p.R767C) in an infant with severe YHFS, and summarized characteristic features including severe neurodevelopmental delay, microcephaly, cataract, hearing impairment, growth failure, cleft palate, congenital heart defect (ASD), and brain hypoplasia/atrophy; authors noted that “the specific pathogenic mechanisms remain to be elucidated,” but compiled evidence that TELO2 mutations reduce TTT component levels and PIKK stability without affecting telomere length in human cells. (Open Life Sciences, Jan 2023) (zhao2023novelcompoundheterozygous pages 1-2) URL: https://doi.org/10.1515/biol-2022-0602
- Mechanistic: 2023 reviews provide updated structural/functional insights into TTT as a co‑chaperone for PIKKs, its co‑translational binding to the FATKIN region, and CK2‑regulated specificity that particularly impacts SMG1 and mTOR—mechanisms relevant to neurodevelopmental phenotypes in TELO2 deficiency. (IJMS reviews, May 2023) (bhadra2023ttt(tel2tti1tti2)complex pages 2-4, bhadra2023ttt(tel2tti1tti2)complex pages 7-9) URLs: https://doi.org/10.3390/ijms24098268; https://doi.org/10.3390/ijms24119256
- Oncology context informing mechanism: A 2023 GBM study demonstrated TELO2 knockdown reduces PIKK levels and modulates cell‑cycle, EMT, ROS, apoptosis, and telomerase activity and explored crosstalk of TELO2–TTI1–TTI2 with p53 and mitochondrial signaling, supporting TELO2’s role as a common stabilizer of PIKK signaling. Although not a YHFS study, these data substantiate TTT’s role in PIKK proteostasis. (IJMS, May 2023) (feng2023exploringthefunctional pages 10-11) URL: https://doi.org/10.3390/ijms24119256

3) Current applications and real‑world implementations
- Diagnostics: Clinical exome sequencing or genome sequencing to identify biallelic TELO2 variants in individuals with syndromic neurodevelopmental delay and microcephaly. Case reports emphasize variant interpretation with genotype–phenotype correlations: truncating/null variants trend toward more severe phenotypes; specific missense variants (e.g., p.Arg609His) can present milder courses. (Jan 2023; Jan 2021) (zhao2023novelcompoundheterozygous pages 1-2, ciaccio2021milderpresentationof pages 1-3) URLs: https://doi.org/10.1515/biol-2022-0602; https://doi.org/10.1016/j.ejmg.2020.104116
- Clinical management: Cataract surgery improved visual engagement in one reported infant, indicating benefit of routine ophthalmologic evaluation and management. (Jan 2023) (zhao2023novelcompoundheterozygous pages 1-2) URL: https://doi.org/10.1515/biol-2022-0602
- Research tools/targets: Mechanistic literature suggests TELO2/TTT and CK2‑regulated interactions are potential levers to modulate specific PIKK pathways; ivermectin has been reported to bind TELO2 and inhibit PIKK signaling in cellular models, though this is investigational and outside current clinical practice. (May 2023) (bhadra2023ttt(tel2tti1tti2)complex pages 7-9, feng2023exploringthefunctional pages 10-11) URLs: https://doi.org/10.3390/ijms24098268; https://doi.org/10.3390/ijms24119256

4) Expert opinions and analysis from authoritative sources
- The 2021 PLoS ONE study provides experimental evidence and interpretation that “CLK‑2/TEL2 is a conserved component of the NMD pathway,” proposing that TELO2’s contribution to NMD (through SMG1 stabilization and possibly other targets) offers a mechanistic link to the neurodevelopmental phenotype in TELO2‑related disease, consistent with the known association between NMD defects and intellectual disability. (Jan 2021) (guo2021clk2tel2isa pages 6-9, guo2021clk2tel2isa pages 9-10) URL: https://doi.org/10.1371/journal.pone.0244505
- 2023 reviews interpret decades of TTT/PIKK biology to conclude that TTT is essential for PIKK proteostasis and that CK2 phosphorylation of TELO2/TTI1 confers differential effects on PIKKs (notably mTOR and SMG1), providing a plausible basis for tissue‑ and pathway‑specific vulnerabilities in TELO2 deficiency. (May 2023) (bhadra2023ttt(tel2tti1tti2)complex pages 2-4, bhadra2023ttt(tel2tti1tti2)complex pages 7-9) URLs: https://doi.org/10.3390/ijms24098268

5) Relevant statistics and data from recent studies
- Protein-level effects of TTT disruption: In human lymphocytes from individuals with TTI2 mutations (a TTT subunit), TTI2 protein was reduced to ~30–65% of control, with associated decreases in TTI1 (~17–37% of control) and near‑absence of TELO2 protein, illustrating destabilization of the entire TTT complex; the truncating allele was predicted to undergo NMD. Although centered on TTI2, these data demonstrate quantitative destabilization across TTT subunits relevant to TELO2‑related disease. (Frontiers in Genetics, Oct 2019) (wang2019novelcompoundheterozygous pages 6-7) URL: https://doi.org/10.3389/fgene.2019.01060
- Clinical spectrum: The 2023 case report catalogs multisystem features including global developmental delay, microcephaly, cataracts, congenital heart defects, and brain hypoplasia/atrophy; it also notes that human TELO2 variants reduce TTT component protein levels, while telomere length remains comparable to controls. (Open Life Sciences, Jan 2023) (zhao2023novelcompoundheterozygous pages 5-6, zhao2023novelcompoundheterozygous pages 1-2) URL: https://doi.org/10.1515/biol-2022-0602

Detailed Pathophysiology Description
- Primary mechanism: Loss‑of‑function of TELO2 (HGNC: TELO2) destabilizes the TTT complex (TELO2‑TTI1‑TTI2), impairing co‑translational maturation and stability of PIKKs (ATM, ATR, PRKDC/DNA‑PKcs, MTOR, SMG1, TRRAP). This reduces protein abundance and activity of these kinases, compromising DNA damage checkpoints (ATM/ATR), DSB repair (PRKDC), growth and metabolic signaling (mTOR), and mRNA surveillance (SMG1/NMD). CK2‑dependent phosphorylation of TELO2/TTI1 determines interaction with R2TP/HSP90 and selectively affects SMG1 and mTOR levels, possibly conferring selective pathway impairment in neural tissues. (bhadra2023ttt(tel2tti1tti2)complex pages 2-4, bhadra2023ttt(tel2tti1tti2)complex pages 7-9, guo2021clk2tel2isa pages 14-15)
- NMD involvement: Experimental data show that CLK‑2 (TELO2 ortholog) is required for NMD in C. elegans, with reporter de‑repression and transcriptome signatures matching smg‑gene mutants; mammalian data indicate that TELO2 phosphorylation by CK2 stabilizes SMG1, a core NMD kinase. Thus, TELO2 deficiency may cause defective NMD in human tissues, including the developing brain. (guo2021clk2tel2isa pages 4-6, guo2021clk2tel2isa pages 6-9, guo2021clk2tel2isa pages 14-15)
- Cellular processes affected: protein folding and assembly (co‑translational PIKK maturation), protein stability, DNA damage response/checkpoint signaling, mTOR/TOR signaling, RNA surveillance (NMD), apoptosis and oxidative stress responses (supportive cellular models). (bhadra2023ttt(tel2tti1tti2)complex pages 2-4, bhadra2023ttt(tel2tti1tti2)complex pages 7-9, feng2023exploringthefunctional pages 10-11)
- Cellular and anatomical context: Neurons and glia in the CNS are implicated by predominant neurodevelopmental phenotypes (ID/GDD, microcephaly) and white‑matter abnormalities seen in some individuals; lens (congenital cataract) and heart (congenital septal defects) reflect broader developmental requirements for PIKK‑dependent signaling. (zhao2023novelcompoundheterozygous pages 1-2, ciaccio2021milderpresentationof pages 5-6)

Sequence of Disease Progression (model)
1) Genetic trigger: Biallelic TELO2 pathogenic variants (often truncating/missense combinations) reduce TELO2 protein and destabilize TTI1/TTI2, compromising TTT integrity. (zhao2023novelcompoundheterozygous pages 1-2)
2) Proteostatic failure: Co‑translational maturation/stability of PIKKs declines; CK2‑regulated deficits disproportionately affect SMG1 and mTOR, with broader reduction in ATM/ATR/PRKDC/TRRAP. (bhadra2023ttt(tel2tti1tti2)complex pages 7-9, bhadra2023ttt(tel2tti1tti2)complex pages 2-4)
3) Pathway dysfunctions: Impaired NMD (via reduced SMG1 stability) produces accumulation of aberrant transcripts; impaired ATM/ATR/PRKDC signaling weakens DNA damage response and replication checkpoints; reduced mTOR activity perturbs growth, metabolism, and neurodevelopmental programs. (guo2021clk2tel2isa pages 14-15, guo2021clk2tel2isa pages 6-9, bhadra2023ttt(tel2tti1tti2)complex pages 2-4)
4) Cellular consequences: Neuronal/glial differentiation and survival are affected; potential white‑matter dysmyelination or gliopathy may occur in subsets; ocular lens fiber cell homeostasis is perturbed, producing cataract. (ciaccio2021milderpresentationof pages 5-6, zhao2023novelcompoundheterozygous pages 1-2)
5) Clinical manifestation: Global developmental delay/intellectual disability, microcephaly, growth retardation/failure to thrive, congenital cataracts, congenital heart defects (e.g., atrial septal defect), variable seizures and spasticity; neuroimaging may show brain hypoplasia/atrophy and, in some cases, white‑matter hyperintensities. (zhao2023novelcompoundheterozygous pages 1-2, ciaccio2021milderpresentationof pages 5-6)

Key Molecular Players
- Genes/Proteins: TELO2 (disease gene), TTI1/TTI2 (TTT subunits), PIKKs—ATM, ATR, PRKDC (DNA‑PKcs), MTOR, SMG1, TRRAP; chaperone network—HSP90, RUVBL1/2; regulator—CK2. (bhadra2023ttt(tel2tti1tti2)complex pages 2-4, guo2021clk2tel2isa pages 14-15, bhadra2023ttt(tel2tti1tti2)complex pages 7-9)
- Chemical entities: Ivermectin described as a TELO2‑binding small molecule that reduces PIKK activity in cells; in oncology models, temozolomide and curcumin modulate pathways interacting with TELO2 status. These are research findings, not clinical treatments for YHFS. (bhadra2023ttt(tel2tti1tti2)complex pages 7-9, feng2023exploringthefunctional pages 10-11)
- Cell types: Neurons and glia (brain); lens fiber cells (eye); cardiomyocytes/embryonic heart tissues (development). (zhao2023novelcompoundheterozygous pages 1-2, ciaccio2021milderpresentationof pages 5-6)
- Anatomical locations: Brain (including white matter), eye lens, heart. (zhao2023novelcompoundheterozygous pages 1-2, ciaccio2021milderpresentationof pages 5-6)

Biological Processes (GO concepts; representative names)
- Nonsense‑mediated mRNA decay (NMD); PIKK complex assembly/maturation; protein folding; DNA damage response and checkpoint signaling; TOR/mTOR signaling; co‑translational protein targeting/quality control. (guo2021clk2tel2isa pages 6-9, guo2021clk2tel2isa pages 14-15, bhadra2023ttt(tel2tti1tti2)complex pages 7-9, bhadra2023ttt(tel2tti1tti2)complex pages 2-4)

Cellular Components
- TTT complex (cytoplasmic co‑chaperone with R2TP/HSP90); PIKK complexes (nuclear and cytoplasmic locales—e.g., mTORC1/2, ATM/ATR/DNA‑PKcs at chromatin); ribosome‑proximal co‑translational assembly sites. (bhadra2023ttt(tel2tti1tti2)complex pages 7-9, bhadra2023ttt(tel2tti1tti2)complex pages 2-4)

Phenotypic Manifestations (HP concept names)
- Intellectual disability; global developmental delay; microcephaly; congenital cataract; growth retardation/failure to thrive; congenital heart defect (e.g., atrial septal defect); white‑matter abnormality; seizures; spasticity/ataxia (variable). (zhao2023novelcompoundheterozygous pages 1-2, ciaccio2021milderpresentationof pages 1-3, ciaccio2021milderpresentationof pages 5-6)

Ontology-ready Annotations (summary table)
| Category | Entity (Name) | Ontology | ID | Role / Annotation | Key Process / Location (GO / CL / UBERON / CHEBI) | Evidence |
|---|---|---|---|---|---|---|
| Gene / Protein | TELO2 | HGNC | TELO2 | Core TTT subunit; required for TTT stability and PIKK maturation; disease gene for You-Hoover-Fong syndrome | PIKK co-chaperone activity; cytoplasm / nucleus (assembly) | (zhao2023novelcompoundheterozygous pages 1-2), https://doi.org/10.1515/biol-2022-0602, Jan 2023 |
| Gene / Protein | TTI1 | HGNC | TTI1 | TTT subunit; interacts with TELO2/TTI2; required for PIKK stability | PIKK complex assembly; cytoplasmic co-chaperone function | (bhadra2023ttt(tel2tti1tti2)complex pages 2-4), https://doi.org/10.3390/ijms24098268, May 2023 |
| Gene / Protein | TTI2 | HGNC | TTI2 | TTT subunit; loss-of-function destabilizes TTT and reduces PIKK levels (causes syndromic ID) | PIKK maturation/stability; loss triggers reduced TTT/PIKK protein abundance | (wang2019novelcompoundheterozygous pages 1-2), https://doi.org/10.3389/fgene.2019.01060, Oct 2019 |
| Gene / Protein | ATM | HGNC | ATM | PIKK client of TTT; genome-stability kinase involved in DSB response | DNA damage response (checkpoint signaling) in nucleus | (bhadra2023ttt(tel2tti1tti2)complex pages 2-4), https://doi.org/10.3390/ijms24098268, May 2023 |
| Gene / Protein | ATR | HGNC | ATR | PIKK client of TTT; replication/checkpoint kinase sensitive to TELO2/TTT perturbation | Replication stress response / checkpoint signaling | (bhadra2023ttt(tel2tti1tti2)complex pages 2-4), https://doi.org/10.3390/ijms24098268, May 2023 |
| Gene / Protein | PRKDC (DNA-PKcs) | HGNC | PRKDC | PIKK involved in double-strand break repair; protein stability supported by TTT | Non-homologous end-joining / DSB repair | (bhadra2023ttt(tel2tti1tti2)complex pages 2-4), https://doi.org/10.3390/ijms24098268, May 2023 |
| Gene / Protein | MTOR | HGNC | MTOR | Growth-control PIKK whose stability/mTORC1 regulation can be modulated by TTT/TELO2 | mTOR signaling pathway; cytoplasm (mTORC1/2) | (feng2023exploringthefunctional pages 10-11), https://doi.org/10.3390/ijms24119256, May 2023 |
| Gene / Protein | SMG1 | HGNC | SMG1 | PIKK kinase that phosphorylates UPF1 in nonsense-mediated mRNA decay (NMD); stability regulated by TELO2/TTT | Nonsense-mediated mRNA decay (NMD) pathway | (guo2021clk2tel2isa pages 14-15), https://doi.org/10.1371/journal.pone.0244505, Jan 2021 |
| Gene / Protein | RUVBL1/2 | HGNC | RUVBL1 / RUVBL2 | AAA+ ATPases that cooperate with R2TP/TTT for PIKK assembly and NMD functions | Co-chaperone/R2TP interactions; cytoplasmic/nucleoplasmic roles | (guo2021clk2tel2isa pages 14-15), https://doi.org/10.1371/journal.pone.0244505, Jan 2021 |
| Gene / Protein | CSNK2 (CK2) | HGNC | CSNK2A1 / CSNK2B | Casein kinase II phosphorylates TELO2/TTI1; phosphorylation modulates specificity/stability of select PIKKs (e.g., SMG1, mTOR) | Post-translational regulation of TTT → selective PIKK stability | (bhadra2023ttt(tel2tti1tti2)complex pages 7-9), https://doi.org/10.3390/ijms24098268, May 2023 |
| Process | Nonsense-mediated mRNA decay (NMD) | GO | nonsense-mediated mRNA decay | TELO2/CLK-2 and R2TP/TTT contribute to SMG1 stability and NMD function; CLK-2 shown as NMD component in C. elegans | GO:nonsense-mediated mRNA decay; impacts RNA surveillance | (guo2021clk2tel2isa pages 6-9), https://doi.org/10.1371/journal.pone.0244505, Jan 2021 |
| Process | PIKK maturation / stability | GO | PIKK complex assembly / maturation | TTT (TELO2-TTI1-TTI2) acts as co-chaperone with R2TP/HSP90 to promote co-translational PIKK folding and stability | GO:protein complex assembly; co-translational chaperone activity | (bhadra2023ttt(tel2tti1tti2)complex pages 2-4), https://doi.org/10.3390/ijms24098268, May 2023 |
| Process | DNA damage response | GO | DNA damage response / checkpoint signaling | Loss of TTT/TELO2 can impair ATM/ATR/DNA-PKcs signaling leading to genome-stability defects | GO:DNA damage response; checkpoint signaling | (bhadra2023ttt(tel2tti1tti2)complex pages 2-4), https://doi.org/10.3390/ijms24098268, May 2023 |
| Process | mTOR signaling | GO | mTOR signaling pathway | TELO2/TTT influence mTOR stability and downstream growth signaling; implicated in cell growth and neurodevelopment | GO:mTOR signaling; growth regulation | (feng2023exploringthefunctional pages 10-11), https://doi.org/10.3390/ijms24119256, May 2023 |
| Process | Checkpoint signaling (replication/DSB) | GO | cell-cycle / checkpoint signaling | TTT required for ATR/ATM-mediated checkpoint activation (replication stress, DSB repair) | GO:cell-cycle checkpoint; replication stress response | (bhadra2023ttt(tel2tti1tti2)complex pages 2-4), https://doi.org/10.3390/ijms24098268, May 2023 |
| Cell type | Neuronal cell | CL | neuronal cell | Primary affected cell population inferred from neurodevelopmental phenotypes (ID, microcephaly); TELO2 variants linked to neuronal dysfunction | CL:neuronal cell; central nervous system neurons (brain) | (zhao2023novelcompoundheterozygous pages 1-2), https://doi.org/10.1515/biol-2022-0602, Jan 2023 |
| Cell type | Glial cell | CL | glial cell (astrocyte/oligodendrocyte) | TTT/TELO2 expressed in glia; TELO2 perturbation studied in GBM models (impacts mTOR/PIKK pathways) | CL:glial cell; relevance to white-matter pathology | (feng2023exploringthefunctional pages 10-11), https://doi.org/10.3390/ijms24119256, May 2023 |
| Anatomical site | Brain | UBERON | brain | Principal organ affected in YHFS: neurodevelopmental delay, microcephaly, atrophy/hypoplasia reported | UBERON:brain; CNS | (zhao2023novelcompoundheterozygous pages 1-2), https://doi.org/10.1515/biol-2022-0602, Jan 2023 |
| Anatomical site | White matter | UBERON | cerebral white matter | Symmetric T2 hyperintensities / white-matter abnormalities reported in some TELO2 cases | UBERON:white matter; MRI abnormalities noted | (ciaccio2021milderpresentationof pages 5-6), https://doi.org/10.1016/j.ejmg.2020.104116, Jan 2021 |
| Anatomical site | Eye lens | UBERON | lens of eye | Congenital cataracts reported in multiple TELO2-deficient patients | UBERON:lens; ocular findings | (zhao2023novelcompoundheterozygous pages 1-2), https://doi.org/10.1515/biol-2022-0602, Jan 2023 |
| Anatomical site | Heart | UBERON | heart | Congenital cardiac malformations (e.g., atrial septal defect) reported in YHFS case reports | UBERON:heart; congenital heart defect annotations | (zhao2023novelcompoundheterozygous pages 1-2), https://doi.org/10.1515/biol-2022-0602, Jan 2023 |
| Phenotype (HP) | Intellectual disability | HP | intellectual disability | Core neurodevelopmental phenotype in TELO2-related You-Hoover-Fong syndrome | HP:intellectual disability; developmental defect | (zhao2023novelcompoundheterozygous pages 1-2), https://doi.org/10.1515/biol-2022-0602, Jan 2023 |
| Phenotype (HP) | Microcephaly | HP | microcephaly | Recurrent feature associated with TELO2 biallelic variants; correlates with severity | HP:microcephaly; reduced brain growth | (ciaccio2021milderpresentationof pages 1-3), https://doi.org/10.1016/j.ejmg.2020.104116, Jan 2021 |
| Phenotype (HP) | Cataract | HP | congenital cataract | Reported in multiple cases; surgical correction improves visual responses in at least one case report | HP:cataract; lens opacity | (zhao2023novelcompoundheterozygous pages 1-2), https://doi.org/10.1515/biol-2022-0602, Jan 2023 |
| Phenotype (HP) | Growth retardation / FTT | HP | failure to thrive / growth retardation | Postnatal growth failure reported in case series | HP:failure to thrive; growth retardation | (zhao2023novelcompoundheterozygous pages 1-2), https://doi.org/10.1515/biol-2022-0602, Jan 2023 |
| Phenotype (HP) | Congenital heart defect | HP | congenital heart malformation | ASD and other cardiac anomalies reported in YHFS patients | HP:congenital heart defect | (zhao2023novelcompoundheterozygous pages 1-2), https://doi.org/10.1515/biol-2022-0602, Jan 2023 |
| Phenotype (HP) | Seizures | HP | seizure / epilepsy | Seizures reported in some TELO2-deficient individuals | HP:seizure | (zhao2023novelcompoundheterozygous pages 1-2), https://doi.org/10.1515/biol-2022-0602, Jan 2023 |
| Chemical | Ivermectin | CHEBI | ivermectin | Small molecule reported to bind Tel2 and reduce PIKK activity; proposed repurposing mechanism in cancer models | CHEBI:ivermectin; experimental PIKK inhibition | (bhadra2023ttt(tel2tti1tti2)complex pages 7-9), https://doi.org/10.3390/ijms24098268, May 2023 |
| Chemical | Temozolomide (TMZ) | CHEBI | temozolomide | Chemotherapeutic context where TELO2 expression modulates drug responsiveness in GBM models | CHEBI:temozolomide; drug-response studies | (feng2023exploringthefunctional pages 10-11), https://doi.org/10.3390/ijms24119256, May 2023 |
| Chemical | Curcumin | CHEBI | curcumin | Reported in cell studies to interact with TELO2-related pathways and modify drug response | CHEBI:curcumin; experimental modulator in GBM contexts | (feng2023exploringthefunctional pages 10-11), https://doi.org/10.3390/ijms24119256, May 2023 |


*Table: Concise ontology-ready table summarizing genes, processes, cell types, anatomical sites, phenotypes (HP), and chemicals relevant to You-Hoover-Fong syndrome (TELO2-related), with supporting citations and DOIs for mechanistic and clinical evidence.*

Evidence Items (primary literature with URLs and dates)
- Zhao Y et al. Novel compound heterozygous mutations in TELO2 in an infant with You‑Hoover‑Fong syndrome: A case report and literature review. Open Life Sciences. Jan 2023. DOI: 10.1515/biol-2022-0602. URL: https://doi.org/10.1515/biol-2022-0602 (mechanism/phenotype summary; clinical features; telomere length unaffected; novel variants; surgery outcome). (zhao2023novelcompoundheterozygous pages 1-2, zhao2023novelcompoundheterozygous pages 5-6)
- Guo Y et al. CLK‑2/TEL2 is a conserved component of the nonsense‑mediated mRNA decay pathway. PLoS ONE. Jan 2021. DOI: 10.1371/journal.pone.0244505. URL: https://doi.org/10.1371/journal.pone.0244505 (NMD genetic evidence; CK2‑TELO2‑SMG1 link; tissue specificity). (guo2021clk2tel2isa pages 6-9, guo2021clk2tel2isa pages 13-14, guo2021clk2tel2isa pages 14-15, guo2021clk2tel2isa pages 9-10, guo2021clk2tel2isa pages 4-6)
- Bhadra S, Xu Y‑j. TTT (Tel2‑Tti1‑Tti2) Complex, the Co‑Chaperone of PIKKs and a Potential Target for Cancer Chemotherapy. IJMS. May 2023. DOI: 10.3390/ijms24098268. URL: https://doi.org/10.3390/ijms24098268 (TTT promotes co‑translational PIKK maturation; Tel2 deletion reduces PIKKs; CK2‑site selectivity for SMG1/mTOR; ivermectin interaction). (bhadra2023ttt(tel2tti1tti2)complex pages 2-4, bhadra2023ttt(tel2tti1tti2)complex pages 7-9)
- Feng S‑W et al. Exploring the Functional Roles of TELO2 in GBM and TMZ responsiveness. IJMS. May 2023. DOI: 10.3390/ijms24119256. URL: https://doi.org/10.3390/ijms24119256 (TELO2 as common stabilizer of PIKKs; pathway modulation; oncology context). (feng2023exploringthefunctional pages 10-11)
- Ciaccio C et al. Milder presentation of TELO2‑related syndrome in two sisters homozygous for p.Arg609His. Eur J Med Genet. Jan 2021. DOI: 10.1016/j.ejmg.2020.104116. URL: https://doi.org/10.1016/j.ejmg.2020.104116 (genotype–phenotype; white‑matter abnormalities in some patients; differential diagnosis). (ciaccio2021milderpresentationof pages 6-7, ciaccio2021milderpresentationof pages 1-3, ciaccio2021milderpresentationof pages 5-6)
- Wang R et al. Novel Compound Heterozygous Mutations in TTI2 Cause Syndromic Intellectual Disability. Front Genet. Oct 2019. DOI: 10.3389/fgene.2019.01060. URL: https://doi.org/10.3389/fgene.2019.01060 (TTT destabilization across subunits; predicted NMD of truncating allele; supports TTT mechanism relevant to TELO2 disease). (wang2019novelcompoundheterozygous pages 1-2, wang2019novelcompoundheterozygous pages 6-7)

Notes and limitations
- While 2023–2024 clinical expansions are referenced in some sources, detailed cohort statistics were not available in the evidence set retrieved here; therefore, quantitative prevalence or penetrance estimates beyond individual case and small series reports are limited. Where oncology or model‑organism data are cited, they are used to support mechanistic plausibility of TTT‑PIKK‑NMD biology relevant to TELO2‑related neurodevelopmental disease. (zhao2023novelcompoundheterozygous pages 1-2, guo2021clk2tel2isa pages 6-9, bhadra2023ttt(tel2tti1tti2)complex pages 2-4)

References

1. (zhao2023novelcompoundheterozygous pages 1-2): Yong Zhao, Yu Han, Nuo Li, Wen-jie Fu, Guanjun Luo, Yuan Tan, and Xu-guang Qian. Novel compound heterozygous mutations in telo2 in an infant with you-hoover-fong syndrome: a case report and literature review. Open Life Sciences, Jan 2023. URL: https://doi.org/10.1515/biol-2022-0602, doi:10.1515/biol-2022-0602. This article has 1 citations and is from a peer-reviewed journal.

2. (bhadra2023ttt(tel2tti1tti2)complex pages 2-4): Sankhadip Bhadra and Yong-jie Xu. Ttt (tel2-tti1-tti2) complex, the co-chaperone of pikks and a potential target for cancer chemotherapy. International Journal of Molecular Sciences, 24:8268, May 2023. URL: https://doi.org/10.3390/ijms24098268, doi:10.3390/ijms24098268. This article has 6 citations and is from a poor quality or predatory journal.

3. (bhadra2023ttt(tel2tti1tti2)complex pages 7-9): Sankhadip Bhadra and Yong-jie Xu. Ttt (tel2-tti1-tti2) complex, the co-chaperone of pikks and a potential target for cancer chemotherapy. International Journal of Molecular Sciences, 24:8268, May 2023. URL: https://doi.org/10.3390/ijms24098268, doi:10.3390/ijms24098268. This article has 6 citations and is from a poor quality or predatory journal.

4. (feng2023exploringthefunctional pages 10-11): Shao-Wei Feng, Zih-Syuan Wu, Yi-Lin Chiu, and Shih-Ming Huang. Exploring the functional roles of telomere maintenance 2 in the tumorigenesis of glioblastoma multiforme and drug responsiveness to temozolomide. International Journal of Molecular Sciences, 24:9256, May 2023. URL: https://doi.org/10.3390/ijms24119256, doi:10.3390/ijms24119256. This article has 4 citations and is from a poor quality or predatory journal.

5. (guo2021clk2tel2isa pages 6-9): Yanwu Guo, Cristina Tocchini, and Rafal Ciosk. Clk-2/tel2 is a conserved component of the nonsense-mediated mrna decay pathway. PLoS ONE, 16:e0244505, Jan 2021. URL: https://doi.org/10.1371/journal.pone.0244505, doi:10.1371/journal.pone.0244505. This article has 10 citations and is from a peer-reviewed journal.

6. (guo2021clk2tel2isa pages 14-15): Yanwu Guo, Cristina Tocchini, and Rafal Ciosk. Clk-2/tel2 is a conserved component of the nonsense-mediated mrna decay pathway. PLoS ONE, 16:e0244505, Jan 2021. URL: https://doi.org/10.1371/journal.pone.0244505, doi:10.1371/journal.pone.0244505. This article has 10 citations and is from a peer-reviewed journal.

7. (guo2021clk2tel2isa pages 4-6): Yanwu Guo, Cristina Tocchini, and Rafal Ciosk. Clk-2/tel2 is a conserved component of the nonsense-mediated mrna decay pathway. PLoS ONE, 16:e0244505, Jan 2021. URL: https://doi.org/10.1371/journal.pone.0244505, doi:10.1371/journal.pone.0244505. This article has 10 citations and is from a peer-reviewed journal.

8. (ciaccio2021milderpresentationof pages 1-3): Claudia Ciaccio, Valentina Duga, Chiara Pantaleoni, Silvia Esposito, Isabella Moroni, Michele Pinelli, Raffaele Castello, Vincenzo Nigro, Luisa Chiapparini, Stefano D'Arrigo, Annalaura Torella, Gerarda Cappuccio, Francesco Musacchia, Margherita Mutarelli, Diego Carrella, Giuseppina Vitiello, Giancarlo Parenti, Valeria Capra, Vincenzo Leuzzi, Angelo Selicorni, Silvia Maitz, Nicola Brunetti-Pierri, Sandro Banfi, Marcella Zollino, Martino Montomoli, Donatella Milani, Corrado Romano, Albina Tummolo, Daniele De Brasi, Antonietta Coppola, and Claudia Santoro. Milder presentation of telo2-related syndrome in two sisters homozygous for the p.arg609his pathogenic variant. European Journal of Medical Genetics, 64:104116, Jan 2021. URL: https://doi.org/10.1016/j.ejmg.2020.104116, doi:10.1016/j.ejmg.2020.104116. This article has 7 citations and is from a peer-reviewed journal.

9. (wang2019novelcompoundheterozygous pages 1-2): Rongrong Wang, Shirui Han, Hong-yan Liu, Amjad Khan, Habulieti Xiaerbati, Xueping Yu, Jia Huang, and Xue Zhang. Novel compound heterozygous mutations in tti2 cause syndromic intellectual disability in a chinese family. Frontiers in Genetics, Oct 2019. URL: https://doi.org/10.3389/fgene.2019.01060, doi:10.3389/fgene.2019.01060. This article has 7 citations and is from a peer-reviewed journal.

10. (ciaccio2021milderpresentationof pages 5-6): Claudia Ciaccio, Valentina Duga, Chiara Pantaleoni, Silvia Esposito, Isabella Moroni, Michele Pinelli, Raffaele Castello, Vincenzo Nigro, Luisa Chiapparini, Stefano D'Arrigo, Annalaura Torella, Gerarda Cappuccio, Francesco Musacchia, Margherita Mutarelli, Diego Carrella, Giuseppina Vitiello, Giancarlo Parenti, Valeria Capra, Vincenzo Leuzzi, Angelo Selicorni, Silvia Maitz, Nicola Brunetti-Pierri, Sandro Banfi, Marcella Zollino, Martino Montomoli, Donatella Milani, Corrado Romano, Albina Tummolo, Daniele De Brasi, Antonietta Coppola, and Claudia Santoro. Milder presentation of telo2-related syndrome in two sisters homozygous for the p.arg609his pathogenic variant. European Journal of Medical Genetics, 64:104116, Jan 2021. URL: https://doi.org/10.1016/j.ejmg.2020.104116, doi:10.1016/j.ejmg.2020.104116. This article has 7 citations and is from a peer-reviewed journal.

11. (guo2021clk2tel2isa pages 13-14): Yanwu Guo, Cristina Tocchini, and Rafal Ciosk. Clk-2/tel2 is a conserved component of the nonsense-mediated mrna decay pathway. PLoS ONE, 16:e0244505, Jan 2021. URL: https://doi.org/10.1371/journal.pone.0244505, doi:10.1371/journal.pone.0244505. This article has 10 citations and is from a peer-reviewed journal.

12. (guo2021clk2tel2isa pages 9-10): Yanwu Guo, Cristina Tocchini, and Rafal Ciosk. Clk-2/tel2 is a conserved component of the nonsense-mediated mrna decay pathway. PLoS ONE, 16:e0244505, Jan 2021. URL: https://doi.org/10.1371/journal.pone.0244505, doi:10.1371/journal.pone.0244505. This article has 10 citations and is from a peer-reviewed journal.

13. (wang2019novelcompoundheterozygous pages 6-7): Rongrong Wang, Shirui Han, Hong-yan Liu, Amjad Khan, Habulieti Xiaerbati, Xueping Yu, Jia Huang, and Xue Zhang. Novel compound heterozygous mutations in tti2 cause syndromic intellectual disability in a chinese family. Frontiers in Genetics, Oct 2019. URL: https://doi.org/10.3389/fgene.2019.01060, doi:10.3389/fgene.2019.01060. This article has 7 citations and is from a peer-reviewed journal.

14. (zhao2023novelcompoundheterozygous pages 5-6): Yong Zhao, Yu Han, Nuo Li, Wen-jie Fu, Guanjun Luo, Yuan Tan, and Xu-guang Qian. Novel compound heterozygous mutations in telo2 in an infant with you-hoover-fong syndrome: a case report and literature review. Open Life Sciences, Jan 2023. URL: https://doi.org/10.1515/biol-2022-0602, doi:10.1515/biol-2022-0602. This article has 1 citations and is from a peer-reviewed journal.

15. (ciaccio2021milderpresentationof pages 6-7): Claudia Ciaccio, Valentina Duga, Chiara Pantaleoni, Silvia Esposito, Isabella Moroni, Michele Pinelli, Raffaele Castello, Vincenzo Nigro, Luisa Chiapparini, Stefano D'Arrigo, Annalaura Torella, Gerarda Cappuccio, Francesco Musacchia, Margherita Mutarelli, Diego Carrella, Giuseppina Vitiello, Giancarlo Parenti, Valeria Capra, Vincenzo Leuzzi, Angelo Selicorni, Silvia Maitz, Nicola Brunetti-Pierri, Sandro Banfi, Marcella Zollino, Martino Montomoli, Donatella Milani, Corrado Romano, Albina Tummolo, Daniele De Brasi, Antonietta Coppola, and Claudia Santoro. Milder presentation of telo2-related syndrome in two sisters homozygous for the p.arg609his pathogenic variant. European Journal of Medical Genetics, 64:104116, Jan 2021. URL: https://doi.org/10.1016/j.ejmg.2020.104116, doi:10.1016/j.ejmg.2020.104116. This article has 7 citations and is from a peer-reviewed journal.