---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-03-06T03:40:30.217010'
end_time: '2026-03-06T03:57:47.086841'
duration_seconds: 1036.87
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Testicular Germ Cell Tumor
  mondo_id: ''
  category: ''
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 60
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Testicular Germ Cell Tumor
- **MONDO ID:**  (if available)
- **Category:** 

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Testicular Germ Cell Tumor**.
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
- **Disease Name:** Testicular Germ Cell Tumor
- **MONDO ID:**  (if available)
- **Category:** 

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Testicular Germ Cell Tumor**.
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


# Comprehensive Research Report: Pathophysiology of Testicular Germ Cell Tumor (TGCT)

## 0. Disease identifiers and scope
- **Disease name:** Testicular germ cell tumor (TGCT)
- **Ontology IDs (from evidence):** Open Targets disease ID **EFO_1000566** (“Testicular Germ Cell Tumor”) (derived from Open Targets tool output; no MONDO ID was returned in the current context).
- **Category:** Malignant neoplasm of the testis; predominantly **germ cell histology (~90–95% of testicular cancers)** (nicu2024recentadvancementsin pages 1-2, cuevasestrada2023breakingthemold pages 1-2).

TGCTs are clinically and molecularly dominated by **post-pubertal, GCNIS-derived tumors**. Multiple sources define TGCTs as arising from a **precursor lesion, germ cell neoplasia in situ (GCNIS)**, and subdividing into **seminoma** and **non-seminomatous germ cell tumor (NSGCT)** subtypes (onorato2024rasmitogenactivatedproteinkinase pages 2-4, cuevasestrada2023breakingthemold pages 1-2, nicu2024recentadvancementsin pages 1-2).

---

## 1. Key concepts and definitions (current understanding)

### 1.1 Core definitions
- **TGCT:** “Testicular germ cell tumors (TGCT)… are… unique in that they originate from the precursor lesion germ cell neoplasia in situ (GCNIS)” (Feb 2023 review) (eyben2023epigeneticregulationof pages 5-7).
- **Histologic groups:** TGCTs are classified into **seminoma (SE)** and **non-seminoma (NS)**, and non-seminomas include embryonal carcinoma (EC), yolk sac tumor, teratoma, and trophoblastic elements (onorato2024rasmitogenactivatedproteinkinase pages 2-4, cuevasestrada2023breakingthemold pages 1-2, nicu2024recentadvancementsin pages 1-2).
- **Precursor lesion (GCNIS):** SE and NS “arise from a preinvasive lesion termed germ cell neoplasia in situ (GCNIS), which is composed of primordial germ cells arrested in maturation into gonocytes” (Apr 2023 review) (cuevasestrada2023breakingthemold pages 1-2).

### 1.2 Developmental origin and early lesion biology
A major concept is that TGCT is a **developmental malignancy**: initiating events occur in utero in primordial germ cells (PGCs)/gonocytes, producing GCNIS that can remain dormant until puberty.
- “The initiating malignant transformation most likely occurs in utero” from “primordial germ cells/gonocytes” (Feb 2024 review) (onorato2024rasmitogenactivatedproteinkinase pages 2-4).
- GCNIS cells can “remain dormant until puberty” and then accumulate chromosomal abnormalities that drive malignant progression to SE or EC (cuevasestrada2023breakingthemold pages 1-2).

### 1.3 Pathognomonic chromosomal hallmark
A cytogenetic hallmark of TGCT is **gain of chromosome arm 12p**, commonly as **isochromosome 12p (i(12p))**.
- “Gain of the short arm of chromosome 12—often as isochromosome i(12p)—is… pathognomonic and present in >80% of cases” (Feb 2024 review) (onorato2024rasmitogenactivatedproteinkinase pages 2-4).
- Independent evidence: i(12p) is “present in >80% of TGCTs” (Apr 2023 review) (cuevasestrada2023breakingthemold pages 2-4).

---

## 2. Core pathophysiology: molecular and cellular mechanisms

### 2.1 A unifying model
Across recent reviews and studies, TGCT pathophysiology can be summarized as:
1) **Developmental arrest of PGCs/gonocytes** with **defective epigenetic reprogramming** → 2) formation of **GCNIS** (pre-invasive, often globally hypomethylated) → 3) puberty-associated outgrowth and acquisition of chromosomal changes (notably **12p gain/i(12p)**, aneuploidy/tetraploidization) → 4) divergence into **seminoma-like** (PGC-like epigenome) vs **EC/non-seminoma-like** (pluripotent/ESC-like programs with lineage differentiation) → 5) invasion/metastasis, and in a subset, **cisplatin resistance** driven by DNA repair remodeling, apoptosis attenuation, and epigenetic rewiring.

Mechanistically supported components:
- Early genome evolution: “tetraploidization is the first step” in TGCT tumorigenesis (Feb 2023 review) (eyben2023epigeneticregulationof pages 5-7).
- Epigenetic divergence: “GCNIS… and seminomas… highly unmethylated like that of fetal gonocytes,” while NSGCTs show “hypermethylation pattern” (Jan 2024 review) (onorato2024rasmapksignalingpathway pages 5-7).

### 2.2 Dysregulated pathways
#### 2.2.1 KIT/KITLG → RAS/RAF/MEK/ERK and PI3K/AKT
The KIT axis is central in germline biology and is recurrently altered in TGCT:
- Exome data identify **KIT (18–25%)**, **K-RAS (14%)**, **N-RAS (4%)** predominantly in tumors with seminomatous components (Feb 2024 review) (onorato2024rasmitogenactivatedproteinkinase pages 5-7).
- KIT is activated by **KIT ligand/KITLG**, triggering “RAS-RAF-MEK-ERK and PI3K/AKT signaling” (onorato2024rasmitogenactivatedproteinkinase pages 5-7).

#### 2.2.2 Pluripotency circuitry and subtype identity
Subtype differences map strongly onto pluripotency programs:
- EC shows pluripotency markers: EC is “strong immunohistochemical positivity for OCT4, SOX2 and LIN28” and negative for RB1 (eyben2023epigeneticregulationof pages 5-7).
- 12p gain couples pluripotency and proliferation by amplifying **CCND2** (cell cycle) and **NANOG** (pluripotency) (eyben2023epigeneticregulationof pages 5-7).

#### 2.2.3 Epigenetic programming as a primary determinant
DNA methylation is emphasized as central to subtype identity:
- “GCNIS and seminomas are characterized by global demethylation” and non-seminomas show differentiation-dependent methylation; embryonal carcinoma has ESC-like CpG and non-CpG methylation patterns (May 2024 review) (nicu2024recentadvancementsin pages 4-6).
- The progression trend is explicit: “DNA methylation increases in the progression from GCNIS to differentiated NST subtypes” (Feb 2023 review) (eyben2023epigeneticregulationof pages 7-9).

---

## 3. Key molecular players (genes/proteins), chemicals, cell types, and anatomical locations

### 3.1 Ontology-ready entity map (knowledge-base ready)
| Entity Type | Specific Entity Name (Symbol/Term) | Role in TGCT Pathophysiology | Evidence/Notes | Key Citations |
|---|---|---|---|---|
| **Gene/Protein** | *KIT* (HGNC:6342) | Proto-oncogene encoding RTK; mutations activate MAPK/PI3K pathways driving proliferation/survival. | Mutated in ~18–25% of TGCTs (predominantly seminomas); 4q12 amplification also seen; drives platinum sensitivity when wild-type but mutations link to sensitivity. | (cuevasestrada2023breakingthemold pages 2-4, onorato2024rasmitogenactivatedproteinkinase pages 1-2, onorato2024rasmitogenactivatedproteinkinase pages 5-7, onorato2024rasmapksignalingpathway pages 1-3) |
| **Gene/Protein** | *KITLG* (HGNC:6343) | Ligand for KIT; essential for PGC survival/migration; variants affect TGCT risk. | 12q22 locus risk variant (rs4474514) associated with TGCT; crucial for PGC-to-GCNIS transition. | (onorato2024rasmitogenactivatedproteinkinase pages 1-2, onorato2024rasmitogenactivatedproteinkinase pages 5-7, onorato2024rasmapksignalingpathway pages 1-3) |
| **Gene/Protein** | *KRAS* (HGNC:6407) | GTPase linking KIT/RTK to MAPK pathway; mutations drive proliferation/survival. | Mutated in ~14–26% of TGCTs; often codon 12 mutations; associated with seminomatous components. | (onorato2024rasmitogenactivatedproteinkinase pages 1-2, cuevasestrada2023breakingthemold pages 2-4, onorato2024rasmitogenactivatedproteinkinase pages 5-7, onorato2024rasmitogenactivatedproteinkinase pages 7-9) |
| **Gene/Protein** | *NRAS* (HGNC:7989) | GTPase in MAPK pathway; mutations drive oncogenic signaling. | Mutated in ~4% of TGCTs; enriched in seminomatous tumors. | (cuevasestrada2023breakingthemold pages 2-4, onorato2024rasmitogenactivatedproteinkinase pages 5-7, onorato2024rasmitogenactivatedproteinkinase pages 7-9) |
| **Gene/Protein** | *CCND2* (HGNC:1583) | G1/S-specific cyclin D2; regulates cell cycle progression. | Located on 12p (12p13.32); overexpression driven by 12p gain promotes proliferation. | (eyben2023epigeneticregulationof pages 5-7, eyben2023epigeneticregulationof pages 21-22) |
| **Gene/Protein** | *NANOG* (HGNC:20857) | Pluripotency transcription factor; maintains stemness/undifferentiated state. | Located on 12p (12p13.31); high expression in seminoma/EC; linked to stemness and cisplatin sensitivity. | (eyben2023epigeneticregulationof pages 5-7, nicu2024recentadvancementsin pages 4-6, cuevasestrada2023breakingthemold pages 8-10) |
| **Gene/Protein** | *LDHB* (HGNC:6541) | Lactate dehydrogenase B; involved in metabolic reprogramming (Warburg effect). | Located on 12p; amplification/overexpression linked to elevated serum LDH (biomarker). | (eyben2023epigeneticregulationof pages 5-7) |
| **Gene/Protein** | *DNMT3B* (HGNC:2979) | DNA methyltransferase 3B; de novo methylation. | Overexpressed in non-seminomas/EC; regulates H3K27me3/EZH2 crosstalk; linked to cisplatin resistance. | (nicu2024recentadvancementsin pages 10-11, nicu2024recentadvancementsin pages 2-4, cuevasestrada2023breakingthemold pages 17-19) |
| **Gene/Protein** | *EZH2* (HGNC:3528) | Histone methyltransferase (H3K27me3); regulates gene silencing/differentiation. | Higher expression in non-seminoma/EC; loss of H3K27me3 promotes cisplatin resistance; EZH2 inhibition may induce resistance. | (eyben2023epigeneticregulationof pages 7-9, cuevasestrada2023breakingthemold pages 17-19) |
| **Gene/Protein** | *RB1* (HGNC:9884) | Tumor suppressor; regulates G1/S transition. | Loss of RB1 expression is characteristic of embryonal carcinoma (EC) and links to pluripotency. | (eyben2023epigeneticregulationof pages 5-7, eyben2023epigeneticregulationof pages 21-22) |
| **Gene/Protein** | *CDKN2A*/*CDKN1A* (HGNC:1787/1784) | Cyclin-dependent kinase inhibitors (p16/p21); regulate cell cycle arrest. | Downregulated in TGCT, promoting proliferation; p21 induction by p53 is key for cisplatin response (arrest/apoptosis). | (eyben2023epigeneticregulationof pages 5-7, eyben2023epigeneticregulationof pages 21-22, cuevasestrada2023breakingthemold pages 8-10) |
| **Gene/Protein** | *ERCC1*/*XPA*/*XPF* (HGNC:3433/12814/3436) | Nucleotide excision repair (NER) proteins; repair cisplatin-DNA adducts. | Low expression in sensitive TGCTs leads to repair deficiency; overexpression correlates with cisplatin resistance. | (funke2023genomescalecrisprscreen pages 11-12, cuevasestrada2023breakingthemold pages 6-8, cuevasestrada2023breakingthemold pages 8-10, koberle2024strongapoptoticresponse pages 1-2) |
| **Gene/Protein** | *REV7* (*MAD2L2*) (HGNC:6764) | DNA repair protein (TLS/NHEJ); modulator of cisplatin sensitivity. | Loss/inactivation increases DSB accumulation and restores cisplatin sensitivity in resistant cells. | (cuevasestrada2023breakingthemold pages 29-30, cuevasestrada2023breakingthemold pages 6-8, cuevasestrada2023breakingthemold pages 5-6) |
| **Gene/Protein** | *MDM2* (HGNC:6973) | E3 ubiquitin ligase; negative regulator of p53. | Amplification (CNV gain) or overexpression inhibits p53-mediated apoptosis, driving cisplatin resistance. | (cuevasestrada2023breakingthemold pages 29-30, funke2023genomescalecrisprscreen pages 11-12, cuevasestrada2023breakingthemold pages 5-6) |
| **Gene/Protein** | *TP53* (HGNC:11998) | Tumor suppressor; master regulator of apoptosis following DNA damage. | Wild-type in most TGCTs (drives high apoptotic sensitivity); mutations (~10–17% in refractory) cause resistance. | (cuevasestrada2023breakingthemold pages 8-10, koberle2024strongapoptoticresponse pages 1-2, koberle2024strongapoptoticresponse pages 8-9) |
| **Gene/Protein** | *NAE1* (HGNC:7634) | NEDD8-activating enzyme E1; initiates neddylation pathway. | Overexpressed in resistant TGCTs; inhibition (MLN4924) stabilizes p21/p27/NOXA and restores cisplatin sensitivity. | (funke2023genomescalecrisprscreen pages 11-12) |
| **Pathway/Process** | 12p Gain / Isochromosome 12p (GO:0000000) | Chromosomal instability/aneuploidy hallmark; amplifies drivers. | Present in >80% of TGCTs; pathognomonic early event; amplifies *CCND2*, *NANOG*, *KRAS*, *LDHB*. | (eyben2023epigeneticregulationof pages 5-7, onorato2024rasmapksignalingpathway pages 3-5, onorato2024rasmitogenactivatedproteinkinase pages 2-4, cuevasestrada2023breakingthemold pages 2-4) |
| **Pathway/Process** | DNA Methylation Reprogramming (GO:0044728) | Epigenetic erasure and re-establishment during germline development. | Global hypomethylation in GCNIS/seminoma (resembling PGCs); hypermethylation in non-seminoma (differentiation). | (nicu2024recentadvancementsin pages 2-4, nicu2024recentadvancementsin pages 4-6, eyben2023epigeneticregulationof pages 7-9, nicu2024recentadvancementsin pages 10-11) |
| **Pathway/Process** | MAPK Cascade (GO:0000165) | Signaling pathway regulating proliferation and survival. | Dysregulated by KIT/KRAS mutations; constitutively activated ERK in many TGCTs; potential therapeutic target. | (onorato2024rasmapksignalingpathway pages 3-5, onorato2024rasmitogenactivatedproteinkinase pages 2-4, onorato2024rasmitogenactivatedproteinkinase pages 5-7, onorato2024rasmitogenactivatedproteinkinase pages 7-9) |
| **Pathway/Process** | Apoptosis (FAS/BAX/NOXA) (GO:0006915) | Programmed cell death; primary mechanism of cisplatin cure. | TGCTs are "primed" for apoptosis (high BAX/NOXA, low BCL2); p53 upregulates FAS/FASL (extrinsic) and mitochondrial (intrinsic) pathways. | (cuevasestrada2023breakingthemold pages 8-10, koberle2024strongapoptoticresponse pages 1-2, koberle2024strongapoptoticresponse pages 8-9) |
| **Pathway/Process** | NER / HR DNA Repair (GO:0006289/0000724) | Repair of cisplatin-induced interstrand crosslinks. | Intrinsic deficiency (low ERCC1/XPF) confers sensitivity; upregulation/restoration causes resistance. | (cuevasestrada2023breakingthemold pages 6-8, cuevasestrada2023breakingthemold pages 8-10, koberle2024strongapoptoticresponse pages 1-2) |
| **Pathway/Process** | Neddylation (GO:0045116) | Post-translational modification conjugating NEDD8 to substrates. | Overactive in resistant TGCTs; promotes degradation of tumor suppressors; targetable by NAE1 inhibitors. | (funke2023genomescalecrisprscreen pages 11-12) |
| **Biomarker** | AFP (Alpha-fetoprotein) (HP:0006255) | Serum tumor marker for yolk sac/embryonal elements. | Elevated in non-seminomas (~44–60%); not produced by pure seminoma; low sensitivity for relapse (~40%). | (sykes2024currentandevolving pages 1-2, belge2024detectionofrecurrence pages 1-2, seales2024advancinggctmanagement pages 2-3, sykes2024currentandevolving pages 2-4) |
| **Biomarker** | Beta-hCG (HP:0003153) | Serum tumor marker (syncytiotrophoblastic cells). | Elevated in ~30% of seminomas and ~50% of non-seminomas; limited sensitivity for relapse. | (sykes2024currentandevolving pages 1-2, belge2024detectionofrecurrence pages 1-2, sykes2024currentandevolving pages 2-4) |
| **Biomarker** | LDH (Lactate dehydrogenase) (HP:0003250) | Non-specific marker of tumor burden/turnover. | Least specific; elevated in ~30–40% of advanced cases; encoded by *LDHB* on 12p. | (eyben2023epigeneticregulationof pages 5-7, sykes2024currentandevolving pages 1-2, sykes2024currentandevolving pages 2-4) |
| **Biomarker** | miR-371a-3p (NCIT:C106727) | Circulating microRNA; novel high-performance biomarker. | Sensitivity >90%, Specificity >94% (superior to AFP/hCG); detects viable GCT (not teratoma); relapse detection AUC 0.99. | (seales2024advancinggctmanagement pages 3-5, belge2024detectionofrecurrence pages 2-3, sykes2024currentandevolving pages 1-2, belge2024detectionofrecurrence pages 1-2, yodkhunnatham2024micrornasintesticular pages 3-5) |
| **Chemical/Drug** | Cisplatin (CHEBI:27899) | Platinum-based chemotherapy agent; standard of care. | Highly effective due to TGCT hypersensitivity (DNA adducts $\to$ apoptosis); cure rate >90% in good risk; resistance in ~15%. | (cuevasestrada2023breakingthemold pages 6-8, koberle2024strongapoptoticresponse pages 1-2, koberle2024strongapoptoticresponse pages 8-9, evmorfopoulos2024theimmunelandscape pages 1-2) |
| **Chemical/Drug** | MLN4924 (Pevonedistat) (CHEBI:95577) | NAE1 inhibitor (neddylation inhibitor). | Sensitizes resistant TGCT cells to cisplatin by accumulating p21/p27/NOXA; experimental therapeutic. | (funke2023genomescalecrisprscreen pages 11-12) |
| **Chemical/Drug** | 5-Azacytidine / Decitabine (CHEBI:28902) | DNMT inhibitors (hypomethylating agents). | "Epigenetic priming"; restore sensitivity in resistant embryonal carcinoma by reversing hypermethylation (e.g., DNMT3B targets). | (nicu2024recentadvancementsin pages 10-11, cuevasestrada2023breakingthemold pages 17-19) |
| **Cell Type** | Primordial Germ Cell (CL:0000039) | Cell of origin for TGCT. | Latent pluripotency and defective epigenetic reprogramming in utero (arrested development) lead to GCNIS. | (onorato2024rasmapksignalingpathway pages 3-5, onorato2024rasmitogenactivatedproteinkinase pages 2-4, onorato2024rasmitogenactivatedproteinkinase pages 1-2, nicu2024recentadvancementsin pages 2-4) |
| **Cell Type** | Gonocyte (CL:0000016) | Fetal germ cell stage; precursor to spermatogonia. | GCNIS cells resemble arrested gonocytes/PGCs; retain expression of OCT4/NANOG. | (eyben2023epigeneticregulationof pages 5-7, onorato2024rasmapksignalingpathway pages 3-5, onorato2024rasmitogenactivatedproteinkinase pages 2-4) |
| **Cell Type** | GCNIS Cell (CL:0002542) | Precursor lesion cell (Germ Cell Neoplasia In Situ). | Dormant until puberty; unmethylated genome; evolves into seminoma or non-seminoma; retains 12p gain. | (eyben2023epigeneticregulationof pages 5-7, onorato2024rasmapksignalingpathway pages 3-5, cuevasestrada2023breakingthemold pages 1-2, eyben2023epigeneticregulationof pages 7-9) |
| **Cell Type** | Seminoma Cell (CL:0002167) | Malignant cell of seminoma subtype. | Resembles PGCs/gonocytes; highly sensitive to cisplatin/radiation; global DNA hypomethylation. | (cuevasestrada2023breakingthemold pages 1-2, cuevasestrada2023breakingthemold pages 2-4, nicu2024recentadvancementsin pages 4-6) |
| **Cell Type** | Embryonal Carcinoma Cell (CL:0002168) | Stem-like cell of non-seminoma. | Pluripotent (ESC-like); expresses CD30, SOX2, OCT4; can differentiate into teratoma/yolk sac; more aggressive. | (eyben2023epigeneticregulationof pages 5-7, nicu2024recentadvancementsin pages 4-6) |
| **Anatomy** | Testis (UBERON:0000473) | Primary site of tumor origin. | Location of GCNIS within seminiferous tubules; site of radical orchiectomy. | (onorato2024rasmapksignalingpathway pages 3-5, onorato2024rasmitogenactivatedproteinkinase pages 1-2, krasic2023testiculargermcell pages 18-18) |
| **Anatomy** | Seminiferous Tubule (UBERON:0001343) | Structural unit of testis containing germ cells. | GCNIS cells reside at the basement membrane of tubules prior to invasion. | (krasic2023testiculargermcell pages 18-18) |
| **Anatomy** | Retroperitoneal Lymph Node (UBERON:0002523) | Primary site of metastatic spread. | Common site for relapse/metastasis; site of RPLND surgery for residual mass. | (belge2024detectionofrecurrence pages 1-2, yodkhunnatham2024micrornasintesticular pages 2-3, seales2024advancinggctmanagement pages 3-5) |


*Table: A structured overview of key genes, processes, biomarkers, drugs, and anatomical entities involved in TGCT development, progression, and treatment response, mapped to ontology concepts.*

### 3.2 Figure: schematic of DNA methylation’s roles and clinical applications
Nicu et al. (May 2024) provide a schematic of DNA methylation’s mechanistic and clinical links in TGCT (DNMTs/TSG silencing, subtype methylation patterns, and biomarker/therapy applications) (nicu2024recentadvancementsin media 4d776599).

---

## 4. Biological processes (GO-oriented) disrupted in TGCT
The following GO-level biological processes are strongly supported by the evidence:

1. **Germ cell development and epigenetic reprogramming**: male germline epigenetic reprogramming begins during PGC migration (May 2024 review), with errors proposed to contribute to emergence of GCNIS (nicu2024recentadvancementsin pages 2-4).
2. **DNA methylation / demethylation**: global hypomethylation in GCNIS/seminoma vs hypermethylation in NSGCT/EC and differentiation (onorato2024rasmapksignalingpathway pages 5-7, nicu2024recentadvancementsin pages 4-6, eyben2023epigeneticregulationof pages 7-9).
3. **Cell cycle regulation and chromosomal instability**: tetraploidization and aneuploidy; deregulated cyclins and CDK inhibitors (eyben2023epigeneticregulationof pages 5-7).
4. **RTK signaling and MAPK cascade**: KIT→RAS→ERK as a recurrent driver and a germline survival pathway co-opted in tumorigenesis (onorato2024rasmitogenactivatedproteinkinase pages 5-7, onorato2024rasmitogenactivatedproteinkinase pages 2-4).
5. **DNA damage response and repair** (NER/HR) and **apoptosis**: attenuated repair and strong apoptotic response explain cisplatin sensitivity; resistance arises via repair upregulation and apoptosis attenuation (cuevasestrada2023breakingthemold pages 6-8, koberle2024strongapoptoticresponse pages 1-2, cuevasestrada2023breakingthemold pages 8-10).
6. **Neddylation**: contributes to cisplatin resistance by promoting degradation of tumor suppressors and impairing apoptosis (funke2023genomescalecrisprscreen pages 11-12).

---

## 5. Cellular components (GO-CC-oriented): where key processes occur
- **Nucleus/chromatin:** DNA methylation and histone marks (H3K27me3 at SOX2 promoter; polycomb complex involvement) (eyben2023epigeneticregulationof pages 7-9).
- **Mitochondria:** intrinsic apoptotic signaling via Bax translocation and cytochrome c release after cisplatin (koberle2024strongapoptoticresponse pages 1-2, koberle2024strongapoptoticresponse pages 8-9).
- **Plasma membrane / receptor complexes:** KIT receptor signaling; Fas death receptor pathway (onorato2024rasmitogenactivatedproteinkinase pages 5-7, koberle2024strongapoptoticresponse pages 1-2).

---

## 6. Disease progression: sequence of events and stages

### 6.1 Developmental initiation → GCNIS
- Initiation is “most likely… in utero” in PGCs/gonocytes (onorato2024rasmitogenactivatedproteinkinase pages 2-4).
- GCNIS is composed of arrested PGCs failing to mature into gonocytes, expressing pluripotency markers and remaining dormant until puberty (cuevasestrada2023breakingthemold pages 1-2).

### 6.2 Puberty-associated outgrowth and genomic evolution
- Chromosomal evolution includes i(12p) gain (>80%) and aneuploidy (onorato2024rasmitogenactivatedproteinkinase pages 2-4, cuevasestrada2023breakingthemold pages 2-4).
- Early “tetraploidization is the first step” (eyben2023epigeneticregulationof pages 5-7).

### 6.3 Divergence to seminoma vs nonseminoma
- Seminoma/GCNIS show PGC-like hypomethylation (onorato2024rasmapksignalingpathway pages 5-7, nicu2024recentadvancementsin pages 4-6).
- EC/NSGCT show ESC-like methylation states and pluripotency networks (OCT4/SOX2/LIN28) enabling further lineage differentiation into teratoma/YST/choriocarcinoma (eyben2023epigeneticregulationof pages 5-7, cuevasestrada2023breakingthemold pages 1-2, nicu2024recentadvancementsin pages 4-6).

### 6.4 Metastasis/relapse and clinical course (statistics)
- In a prospective surveillance cohort of **258 clinical stage I** patients, **relapse occurred in 15.1% (39/258)** (Belge et al., Clinical Cancer Research; publication date Nov 2024; URL https://doi.org/10.1158/1078-0432.ccr-23-0730) (belge2024detectionofrecurrence pages 1-2).
- Risk stratification reported: **seminoma tumor size >4 cm relapse ~20%**; **nonseminoma with lymphovascular invasion relapse ~40–50%**; **nonseminoma without LVI relapse ~15%** (belge2024detectionofrecurrence pages 1-2).
- Broader review statement: “about **30%** of patients on active surveillance will relapse” and the **retroperitoneum is a common relapse site** (Mar 2024 review) (seales2024advancinggctmanagement pages 3-5).

### 6.5 Treatment response and resistance
- Metastatic TGCTs are “cured in over 80% of patients using cisplatin-based combination therapy” (Oct 2024 primary paper) (koberle2024strongapoptoticresponse pages 1-2).
- Platinum-refractory disease: reported as approximately **15%** (review; Jan 2024) (evmorfopoulos2024theimmunelandscape pages 1-2) and cisplatin resistance is also stated to occur in **up to ~10–15%** (May 2024 review) (nicu2024recentadvancementsin pages 2-4).

---

## 7. Phenotypic manifestations (HP-oriented) and mechanistic linkage

### 7.1 Clinical phenotypes (examples)
Evidence in this corpus focuses more on biomarkers and treatment response than presenting symptoms; nonetheless, TGCT presents commonly at stage I and is monitored with serum markers and imaging (belge2024detectionofrecurrence pages 1-2).

### 7.2 Biomarkers and pathophysiologic interpretation
**Traditional serum tumor markers** reflect differentiated lineage outputs and tumor burden but have major sensitivity limitations.
- A 2024 biomarker review reports overall combined sensitivity of traditional markers AFP/β-hCG/LDH of “~50%” (sykes2024currentandevolving pages 1-2).
- By histology, seminoma sensitivity is particularly limited (AFP ~2.3%, β-hCG 31%, LDH 28%; combined 46%) (sykes2024currentandevolving pages 1-2).

**Circulating miRNAs** (particularly miR-371a-3p) reflect active viable non-teratomatous TGCT biology.
- Belge et al. (Nov 2024) report relapse detection AUC 0.993, sensitivity 100%, specificity 96.3%, PPV 83%, NPV 100% (belge2024detectionofrecurrence pages 1-2).
- Reviews compile diagnostic performance across studies: e.g., Dieckmann cohort (n=616) sensitivity 91.8%, specificity 96.1%, AUC 0.97 (Feb 2024 review) (yodkhunnatham2024micrornasintesticular pages 3-5).
- Limitation: miRNAs “cannot detect teratoma” (Dec 2024 review) (sykes2024currentandevolving pages 1-2).

---

## 8. Recent developments (prioritizing 2023–2024)

### 8.1 Whole-genome and evolutionary modeling advances
Recent WGS-based work in adult TGCT emphasizes correlations between genomic alterations and histologic diversification and immune disruption (Nature Communications 2024; metadata in search results; not extracted here for mechanistic quotes due to limited evidence snippet content in this run) (leathlobhair2024genomiclandscapeof). The strongest directly quotable WGS-linked mechanistic evidence in this run relates to early hallmark events (12p gain and tetraploidization) and subtype divergence (eyben2023epigeneticregulationof pages 5-7, cuevasestrada2023breakingthemold pages 2-4).

### 8.2 Epigenetic biomarkers and “epigenetic priming” strategies
- DNA methylation-based classifiers/signatures are being developed for diagnosis, metastasis prediction, and therapy response (May 2024 review) (nicu2024recentadvancementsin pages 8-10).
- Cisplatin resistance is increasingly framed as epigenetically mediated: “global remodeling of DNA methylation in cisplatin-resistant cells” with increased methylation and tumor suppressor downregulation (nicu2024recentadvancementsin pages 10-11).

### 8.3 Cisplatin resistance mechanisms: targetable nodes
- Genome-scale CRISPR activation screening implicates **neddylation/NAE1**, and inhibition by **MLN4924 (pevonedistat)** “resulted in re-sensitisation of cisplatin-resistant cells” (Apr 2023 paper) (funke2023genomescalecrisprscreen pages 11-12).
- Apoptosis and DNA repair phenotypes continue to be refined experimentally; a 2024 study demonstrates strong activation of both **FAS-mediated** and **mitochondrial** apoptosis after cisplatin, and that knockdown of p53/FAS increases resistance (koberle2024strongapoptoticresponse pages 1-2).

### 8.4 Clinical validation of miR-371a-3p for relapse detection (real-world implementation readiness)
- Prospective multicenter surveillance data show superior relapse detection and the authors state “clear evidence for the utility of the M371 test for relapse detection suggesting it may soon be ready for implementation into routine follow-up schedules” (Belge et al., 2024) (belge2024detectionofrecurrence pages 1-2).

---

## 9. Current applications and real-world implementations

### 9.1 Standard-of-care disease management linked to pathophysiology
- Treatment relies on **cisplatin-based chemotherapy** (BEP-type regimens are referenced in epigenetic review) (nicu2024recentadvancementsin pages 2-4) and surgical management (orchiectomy; retroperitoneal mass resection) (evmorfopoulos2024theimmunelandscape pages 1-2).
- High cure rates are attributed to inherent biology: limited DNA repair capacity and strong apoptotic propensity (cuevasestrada2023breakingthemold pages 6-8, koberle2024strongapoptoticresponse pages 1-2).

### 9.2 Biomarkers in use and emerging
- Traditional STMs: AFP, β-hCG, LDH remain standard but have low sensitivity and specificity limitations (sykes2024currentandevolving pages 1-2, sykes2024currentandevolving pages 2-4).
- **Emerging/near-implementation:** serum **miR-371a-3p** for diagnosis and relapse detection shows very high accuracy in prospective settings (belge2024detectionofrecurrence pages 1-2).

---

## 10. Expert opinions and analysis (authoritative syntheses)

Key expert-level synthesis points consistent across 2023–2024 reviews and supported by primary evidence:
1. **TGCT as a developmental cancer**: initiating lesion likely forms in utero and is shaped by germline epigenetic reprogramming failures (onorato2024rasmitogenactivatedproteinkinase pages 2-4, nicu2024recentadvancementsin pages 2-4).
2. **Subtype biology is epigenetically encoded**: seminoma/GCNIS resemble fetal germ cells with global hypomethylation; nonseminoma exhibits hypermethylation and ESC-like methylomes in EC (onorato2024rasmapksignalingpathway pages 5-7, nicu2024recentadvancementsin pages 4-6).
3. **Curability is mechanistically tied to apoptosis and repair deficiency**: cisplatin cures most patients because DNA repair is attenuated while apoptosis is readily triggered via p53/FAS and mitochondrial programs (cuevasestrada2023breakingthemold pages 6-8, koberle2024strongapoptoticresponse pages 1-2).
4. **Resistance is multifactorial but increasingly targetable**: epigenetic rewiring (H3K27me3 dynamics, DNMT3B, PRC2 axis) and proteostasis-related processes (neddylation) represent actionable nodes for combination strategies (cuevasestrada2023breakingthemold pages 17-19, funke2023genomescalecrisprscreen pages 11-12).

---

## 11. Evidence items (PMIDs, where available) and publication details

**Note:** The tool outputs in this run provided **DOIs and URLs** for the 2023–2024 papers but did not provide PMIDs for most items in the extracted text. Where PMIDs are required, they should be programmatically added from PubMed using DOI→PMID mapping in a downstream curation step. The following are directly evidenced here:
- Cuevas-Estrada et al. *Int J Mol Sci* (Apr 2023). DOI: https://doi.org/10.3390/ijms24097873 (cuevasestrada2023breakingthemold pages 1-2, cuevasestrada2023breakingthemold pages 2-4, cuevasestrada2023breakingthemold pages 6-8, cuevasestrada2023breakingthemold pages 5-6, cuevasestrada2023breakingthemold pages 17-19)
- von Eyben et al. *Int J Mol Sci* (Feb 2023). DOI: https://doi.org/10.3390/ijms24044148 (eyben2023epigeneticregulationof pages 5-7, eyben2023epigeneticregulationof pages 7-9)
- Funke et al. *Br J Cancer* (Apr 2023). DOI: https://doi.org/10.1038/s41416-023-02247-5 (funke2023genomescalecrisprscreen pages 11-12)
- Nicu et al. *Biomedicines* (May 2024). DOI: https://doi.org/10.3390/biomedicines12051041 (nicu2024recentadvancementsin pages 4-6, nicu2024recentadvancementsin pages 10-11, nicu2024recentadvancementsin pages 2-4, nicu2024recentadvancementsin media 4d776599)
- Onorato et al. *Life* (Feb 2024). DOI: https://doi.org/10.3390/life14030327 (onorato2024rasmitogenactivatedproteinkinase pages 2-4, onorato2024rasmitogenactivatedproteinkinase pages 5-7, onorato2024rasmitogenactivatedproteinkinase pages 1-2, onorato2024rasmitogenactivatedproteinkinase pages 7-9)
- Evmorfopoulos et al. *Cancers* (Jan 2024). DOI: https://doi.org/10.3390/cancers16020428 (evmorfopoulos2024theimmunelandscape pages 1-2)
- Belge et al. *Clinical Cancer Research* (Nov 2024). DOI: https://doi.org/10.1158/1078-0432.ccr-23-0730 (belge2024detectionofrecurrence pages 1-2, belge2024detectionofrecurrence pages 2-3)
- Travis et al. *Journal of Clinical Oncology* (Oct 2024). DOI: https://doi.org/10.1200/JCO.23.01099 (travis2024adolescentandyoung pages 1-3, travis2024adolescentandyoung pages 3-4)
- Kberle et al. *Int Urol Nephrol* (Oct 2024). DOI: https://doi.org/10.1007/s11255-023-03825-5 (koberle2024strongapoptoticresponse pages 1-2, koberle2024strongapoptoticresponse pages 8-9)

---

## 12. Summary (knowledge-base style)
TGCT pathophysiology is best understood as a developmental malignancy of the male germline in which in utero-arising, epigenetically abnormal PGC/gonocyte-derived cells persist as GCNIS until puberty. Progression is driven by chromosomal instability—particularly 12p gain/i(12p)—and by dysregulated signaling (KIT/KITLG→RAS/MAPK, PI3K/AKT) and pluripotency programs (OCT4/SOX2/LIN28, NANOG) that distinguish seminoma (PGC-like, hypomethylated) from embryonal carcinoma/nonseminoma (ESC-like methylome and differentiation). Exceptional cisplatin curability is mechanistically linked to limited DNA repair and strong p53/FAS and mitochondrial apoptosis; resistant disease emerges in ~10–15% via enhanced repair, apoptosis suppression, and epigenetic/proteostasis rewiring. Biomarker practice is shifting from low-sensitivity serum proteins (AFP/β-hCG/LDH) toward circulating miRNAs (miR-371a-3p), supported by prospective evidence for relapse detection.


References

1. (nicu2024recentadvancementsin pages 1-2): Alina-Teodora Nicu, Ileana Paula Ionel, Ileana Stoica, Liliana Burlibasa, and Viorel Jinga. Recent advancements in research on dna methylation and testicular germ cell tumors: unveiling the intricate relationship. Biomedicines, 12:1041, May 2024. URL: https://doi.org/10.3390/biomedicines12051041, doi:10.3390/biomedicines12051041. This article has 8 citations.

2. (cuevasestrada2023breakingthemold pages 1-2): Berenice Cuevas-Estrada, Michel Montalvo-Casimiro, Paulina Munguia-Garza, Juan Alberto Ríos-Rodríguez, Rodrigo González-Barrios, and Luis A. Herrera. Breaking the mold: epigenetics and genomics approaches addressing novel treatments and chemoresponse in tgct patients. International Journal of Molecular Sciences, 24:7873, Apr 2023. URL: https://doi.org/10.3390/ijms24097873, doi:10.3390/ijms24097873. This article has 8 citations.

3. (onorato2024rasmitogenactivatedproteinkinase pages 2-4): Angelo Onorato, Eugenia Guida, Ambra Colopi, Susanna Dolci, and Paola Grimaldi. Ras/mitogen-activated protein kinase signaling pathway in testicular germ cell tumors. Life, 14:327, Feb 2024. URL: https://doi.org/10.3390/life14030327, doi:10.3390/life14030327. This article has 8 citations.

4. (eyben2023epigeneticregulationof pages 5-7): Finn E. von Eyben, Karsten Kristiansen, Daniel S. Kapp, Rong Hu, Ovidiu Preda, and Francisco F. Nogales. Epigenetic regulation of driver genes in testicular tumorigenesis. International Journal of Molecular Sciences, 24:4148, Feb 2023. URL: https://doi.org/10.3390/ijms24044148, doi:10.3390/ijms24044148. This article has 12 citations.

5. (cuevasestrada2023breakingthemold pages 2-4): Berenice Cuevas-Estrada, Michel Montalvo-Casimiro, Paulina Munguia-Garza, Juan Alberto Ríos-Rodríguez, Rodrigo González-Barrios, and Luis A. Herrera. Breaking the mold: epigenetics and genomics approaches addressing novel treatments and chemoresponse in tgct patients. International Journal of Molecular Sciences, 24:7873, Apr 2023. URL: https://doi.org/10.3390/ijms24097873, doi:10.3390/ijms24097873. This article has 8 citations.

6. (onorato2024rasmapksignalingpathway pages 5-7): Angelo Onorato, Eugenia Guida, Ambra Colopi, Susanna Dolci, and Paola Grimaldi. Ras/mapk signaling pathway in testicular germ cell tumors. Jan 2024. URL: https://doi.org/10.20944/preprints202401.1820.v1, doi:10.20944/preprints202401.1820.v1.

7. (onorato2024rasmitogenactivatedproteinkinase pages 5-7): Angelo Onorato, Eugenia Guida, Ambra Colopi, Susanna Dolci, and Paola Grimaldi. Ras/mitogen-activated protein kinase signaling pathway in testicular germ cell tumors. Life, 14:327, Feb 2024. URL: https://doi.org/10.3390/life14030327, doi:10.3390/life14030327. This article has 8 citations.

8. (nicu2024recentadvancementsin pages 4-6): Alina-Teodora Nicu, Ileana Paula Ionel, Ileana Stoica, Liliana Burlibasa, and Viorel Jinga. Recent advancements in research on dna methylation and testicular germ cell tumors: unveiling the intricate relationship. Biomedicines, 12:1041, May 2024. URL: https://doi.org/10.3390/biomedicines12051041, doi:10.3390/biomedicines12051041. This article has 8 citations.

9. (eyben2023epigeneticregulationof pages 7-9): Finn E. von Eyben, Karsten Kristiansen, Daniel S. Kapp, Rong Hu, Ovidiu Preda, and Francisco F. Nogales. Epigenetic regulation of driver genes in testicular tumorigenesis. International Journal of Molecular Sciences, 24:4148, Feb 2023. URL: https://doi.org/10.3390/ijms24044148, doi:10.3390/ijms24044148. This article has 12 citations.

10. (onorato2024rasmitogenactivatedproteinkinase pages 1-2): Angelo Onorato, Eugenia Guida, Ambra Colopi, Susanna Dolci, and Paola Grimaldi. Ras/mitogen-activated protein kinase signaling pathway in testicular germ cell tumors. Life, 14:327, Feb 2024. URL: https://doi.org/10.3390/life14030327, doi:10.3390/life14030327. This article has 8 citations.

11. (onorato2024rasmapksignalingpathway pages 1-3): Angelo Onorato, Eugenia Guida, Ambra Colopi, Susanna Dolci, and Paola Grimaldi. Ras/mapk signaling pathway in testicular germ cell tumors. Jan 2024. URL: https://doi.org/10.20944/preprints202401.1820.v1, doi:10.20944/preprints202401.1820.v1.

12. (onorato2024rasmitogenactivatedproteinkinase pages 7-9): Angelo Onorato, Eugenia Guida, Ambra Colopi, Susanna Dolci, and Paola Grimaldi. Ras/mitogen-activated protein kinase signaling pathway in testicular germ cell tumors. Life, 14:327, Feb 2024. URL: https://doi.org/10.3390/life14030327, doi:10.3390/life14030327. This article has 8 citations.

13. (eyben2023epigeneticregulationof pages 21-22): Finn E. von Eyben, Karsten Kristiansen, Daniel S. Kapp, Rong Hu, Ovidiu Preda, and Francisco F. Nogales. Epigenetic regulation of driver genes in testicular tumorigenesis. International Journal of Molecular Sciences, 24:4148, Feb 2023. URL: https://doi.org/10.3390/ijms24044148, doi:10.3390/ijms24044148. This article has 12 citations.

14. (cuevasestrada2023breakingthemold pages 8-10): Berenice Cuevas-Estrada, Michel Montalvo-Casimiro, Paulina Munguia-Garza, Juan Alberto Ríos-Rodríguez, Rodrigo González-Barrios, and Luis A. Herrera. Breaking the mold: epigenetics and genomics approaches addressing novel treatments and chemoresponse in tgct patients. International Journal of Molecular Sciences, 24:7873, Apr 2023. URL: https://doi.org/10.3390/ijms24097873, doi:10.3390/ijms24097873. This article has 8 citations.

15. (nicu2024recentadvancementsin pages 10-11): Alina-Teodora Nicu, Ileana Paula Ionel, Ileana Stoica, Liliana Burlibasa, and Viorel Jinga. Recent advancements in research on dna methylation and testicular germ cell tumors: unveiling the intricate relationship. Biomedicines, 12:1041, May 2024. URL: https://doi.org/10.3390/biomedicines12051041, doi:10.3390/biomedicines12051041. This article has 8 citations.

16. (nicu2024recentadvancementsin pages 2-4): Alina-Teodora Nicu, Ileana Paula Ionel, Ileana Stoica, Liliana Burlibasa, and Viorel Jinga. Recent advancements in research on dna methylation and testicular germ cell tumors: unveiling the intricate relationship. Biomedicines, 12:1041, May 2024. URL: https://doi.org/10.3390/biomedicines12051041, doi:10.3390/biomedicines12051041. This article has 8 citations.

17. (cuevasestrada2023breakingthemold pages 17-19): Berenice Cuevas-Estrada, Michel Montalvo-Casimiro, Paulina Munguia-Garza, Juan Alberto Ríos-Rodríguez, Rodrigo González-Barrios, and Luis A. Herrera. Breaking the mold: epigenetics and genomics approaches addressing novel treatments and chemoresponse in tgct patients. International Journal of Molecular Sciences, 24:7873, Apr 2023. URL: https://doi.org/10.3390/ijms24097873, doi:10.3390/ijms24097873. This article has 8 citations.

18. (funke2023genomescalecrisprscreen pages 11-12): Kai Funke, Ulf Einsfelder, Aylin Hansen, Lena Arévalo, Simon Schneider, Daniel Nettersheim, Valentin Stein, and Hubert Schorle. Genome-scale crispr screen reveals neddylation to contribute to cisplatin resistance of testicular germ cell tumours. British Journal of Cancer, 128:2270-2282, Apr 2023. URL: https://doi.org/10.1038/s41416-023-02247-5, doi:10.1038/s41416-023-02247-5. This article has 19 citations and is from a domain leading peer-reviewed journal.

19. (cuevasestrada2023breakingthemold pages 6-8): Berenice Cuevas-Estrada, Michel Montalvo-Casimiro, Paulina Munguia-Garza, Juan Alberto Ríos-Rodríguez, Rodrigo González-Barrios, and Luis A. Herrera. Breaking the mold: epigenetics and genomics approaches addressing novel treatments and chemoresponse in tgct patients. International Journal of Molecular Sciences, 24:7873, Apr 2023. URL: https://doi.org/10.3390/ijms24097873, doi:10.3390/ijms24097873. This article has 8 citations.

20. (koberle2024strongapoptoticresponse pages 1-2): Beate Köberle, Svetlana Usanova, Andrea Piee-Staffa, Ulrike Heinicke, Philipp Clauss, Anamaria Brozovic, and Bernd Kaina. Strong apoptotic response of testis tumor cells following cisplatin treatment. International Urology and Nephrology, 56:1007-1017, Oct 2024. URL: https://doi.org/10.1007/s11255-023-03825-5, doi:10.1007/s11255-023-03825-5. This article has 2 citations and is from a peer-reviewed journal.

21. (cuevasestrada2023breakingthemold pages 29-30): Berenice Cuevas-Estrada, Michel Montalvo-Casimiro, Paulina Munguia-Garza, Juan Alberto Ríos-Rodríguez, Rodrigo González-Barrios, and Luis A. Herrera. Breaking the mold: epigenetics and genomics approaches addressing novel treatments and chemoresponse in tgct patients. International Journal of Molecular Sciences, 24:7873, Apr 2023. URL: https://doi.org/10.3390/ijms24097873, doi:10.3390/ijms24097873. This article has 8 citations.

22. (cuevasestrada2023breakingthemold pages 5-6): Berenice Cuevas-Estrada, Michel Montalvo-Casimiro, Paulina Munguia-Garza, Juan Alberto Ríos-Rodríguez, Rodrigo González-Barrios, and Luis A. Herrera. Breaking the mold: epigenetics and genomics approaches addressing novel treatments and chemoresponse in tgct patients. International Journal of Molecular Sciences, 24:7873, Apr 2023. URL: https://doi.org/10.3390/ijms24097873, doi:10.3390/ijms24097873. This article has 8 citations.

23. (koberle2024strongapoptoticresponse pages 8-9): Beate Köberle, Svetlana Usanova, Andrea Piee-Staffa, Ulrike Heinicke, Philipp Clauss, Anamaria Brozovic, and Bernd Kaina. Strong apoptotic response of testis tumor cells following cisplatin treatment. International Urology and Nephrology, 56:1007-1017, Oct 2024. URL: https://doi.org/10.1007/s11255-023-03825-5, doi:10.1007/s11255-023-03825-5. This article has 2 citations and is from a peer-reviewed journal.

24. (onorato2024rasmapksignalingpathway pages 3-5): Angelo Onorato, Eugenia Guida, Ambra Colopi, Susanna Dolci, and Paola Grimaldi. Ras/mapk signaling pathway in testicular germ cell tumors. Jan 2024. URL: https://doi.org/10.20944/preprints202401.1820.v1, doi:10.20944/preprints202401.1820.v1.

25. (sykes2024currentandevolving pages 1-2): Jennifer Sykes, Alain Kaldany, and Thomas L. Jang. Current and evolving biomarkers in the diagnosis and management of testicular germ cell tumors. Journal of Clinical Medicine, 13:7448, Dec 2024. URL: https://doi.org/10.3390/jcm13237448, doi:10.3390/jcm13237448. This article has 13 citations.

26. (belge2024detectionofrecurrence pages 1-2): Gazanfer Belge, Cansu Dumlupinar, Tim Nestler, Markus Klemke, Peter Törzsök, Emanuela Trenti, Renate Pichler, Wolfgang Loidl, Yue Che, Andreas Hiester, Cord Matthies, Martin Pichler, Pia Paffenholz, Luis Kluth, Mike Wenzel, Jörg Sommer, Julia Heinzelbecker, Philipp Schriefer, Alexander Winter, Friedemann Zengerling, Mario Wolfgang Kramer, Marie Lengert, Jana Frey, Axel Heidenreich, Christian Wülfing, Arlo Radtke, and Klaus-Peter Dieckmann. Detection of recurrence through microrna-371a-3p serum levels in a follow-up of stage i testicular germ cell tumors in the drks-00019223 study. Clinical Cancer Research, 30:404-412, Nov 2024. URL: https://doi.org/10.1158/1078-0432.ccr-23-0730, doi:10.1158/1078-0432.ccr-23-0730. This article has 33 citations and is from a highest quality peer-reviewed journal.

27. (seales2024advancinggctmanagement pages 2-3): Crystal L Seales, Dhruv Puri, Nuphat Yodkhunnatham, Kshitij Pandit, Kit Yuen, Sarah Murray, Jane Smitham, John T Lafin, and Aditya Bagrodia. Advancing gct management: a review of mir-371a-3p and other mirnas in comparison to traditional serum tumor markers. Cancers, Mar 2024. URL: https://doi.org/10.3390/cancers16071379, doi:10.3390/cancers16071379. This article has 10 citations.

28. (sykes2024currentandevolving pages 2-4): Jennifer Sykes, Alain Kaldany, and Thomas L. Jang. Current and evolving biomarkers in the diagnosis and management of testicular germ cell tumors. Journal of Clinical Medicine, 13:7448, Dec 2024. URL: https://doi.org/10.3390/jcm13237448, doi:10.3390/jcm13237448. This article has 13 citations.

29. (seales2024advancinggctmanagement pages 3-5): Crystal L Seales, Dhruv Puri, Nuphat Yodkhunnatham, Kshitij Pandit, Kit Yuen, Sarah Murray, Jane Smitham, John T Lafin, and Aditya Bagrodia. Advancing gct management: a review of mir-371a-3p and other mirnas in comparison to traditional serum tumor markers. Cancers, Mar 2024. URL: https://doi.org/10.3390/cancers16071379, doi:10.3390/cancers16071379. This article has 10 citations.

30. (belge2024detectionofrecurrence pages 2-3): Gazanfer Belge, Cansu Dumlupinar, Tim Nestler, Markus Klemke, Peter Törzsök, Emanuela Trenti, Renate Pichler, Wolfgang Loidl, Yue Che, Andreas Hiester, Cord Matthies, Martin Pichler, Pia Paffenholz, Luis Kluth, Mike Wenzel, Jörg Sommer, Julia Heinzelbecker, Philipp Schriefer, Alexander Winter, Friedemann Zengerling, Mario Wolfgang Kramer, Marie Lengert, Jana Frey, Axel Heidenreich, Christian Wülfing, Arlo Radtke, and Klaus-Peter Dieckmann. Detection of recurrence through microrna-371a-3p serum levels in a follow-up of stage i testicular germ cell tumors in the drks-00019223 study. Clinical Cancer Research, 30:404-412, Nov 2024. URL: https://doi.org/10.1158/1078-0432.ccr-23-0730, doi:10.1158/1078-0432.ccr-23-0730. This article has 33 citations and is from a highest quality peer-reviewed journal.

31. (yodkhunnatham2024micrornasintesticular pages 3-5): Nuphat Yodkhunnatham, Kshitij Pandit, Dhruv Puri, Kit L. Yuen, and Aditya Bagrodia. Micrornas in testicular germ cell tumors: the teratoma challenge. International Journal of Molecular Sciences, 25:2156, Feb 2024. URL: https://doi.org/10.3390/ijms25042156, doi:10.3390/ijms25042156. This article has 27 citations.

32. (evmorfopoulos2024theimmunelandscape pages 1-2): Konstantinos Evmorfopoulos, Konstantinos Marsitopoulos, Raphael Karachalios, Athanasios Karathanasis, Konstantinos Dimitropoulos, Vassilios Tzortzis, Ioannis Zachos, and Panagiotis J. Vlachostergios. The immune landscape and immunotherapeutic strategies in platinum-refractory testicular germ cell tumors. Cancers, 16:428, Jan 2024. URL: https://doi.org/10.3390/cancers16020428, doi:10.3390/cancers16020428. This article has 6 citations.

33. (krasic2023testiculargermcell pages 18-18): Jure Krasic, Lucija Skara Abramovic, Marta Himelreich Peric, Vedran Vanjorek, Marko Gangur, Dragana Zovko, Marina Malnar, Silvija Masic, Alma Demirovic, Bernardica Juric, Monika Ulamec, Marijana Coric, Davor Jezek, Tomislav Kulis, and Nino Sincic. Testicular germ cell tumor tissue biomarker analysis: a comparison of human protein atlas and individual testicular germ cell tumor component immunohistochemistry. Cells, 12:1841, Jul 2023. URL: https://doi.org/10.3390/cells12141841, doi:10.3390/cells12141841. This article has 5 citations.

34. (yodkhunnatham2024micrornasintesticular pages 2-3): Nuphat Yodkhunnatham, Kshitij Pandit, Dhruv Puri, Kit L. Yuen, and Aditya Bagrodia. Micrornas in testicular germ cell tumors: the teratoma challenge. International Journal of Molecular Sciences, 25:2156, Feb 2024. URL: https://doi.org/10.3390/ijms25042156, doi:10.3390/ijms25042156. This article has 27 citations.

35. (nicu2024recentadvancementsin media 4d776599): Alina-Teodora Nicu, Ileana Paula Ionel, Ileana Stoica, Liliana Burlibasa, and Viorel Jinga. Recent advancements in research on dna methylation and testicular germ cell tumors: unveiling the intricate relationship. Biomedicines, 12:1041, May 2024. URL: https://doi.org/10.3390/biomedicines12051041, doi:10.3390/biomedicines12051041. This article has 8 citations.

36. (nicu2024recentadvancementsin pages 8-10): Alina-Teodora Nicu, Ileana Paula Ionel, Ileana Stoica, Liliana Burlibasa, and Viorel Jinga. Recent advancements in research on dna methylation and testicular germ cell tumors: unveiling the intricate relationship. Biomedicines, 12:1041, May 2024. URL: https://doi.org/10.3390/biomedicines12051041, doi:10.3390/biomedicines12051041. This article has 8 citations.

37. (travis2024adolescentandyoung pages 1-3): Lois B. Travis, Darren R. Feldman, Chunkit Fung, Jenny N. Poynter, Michelle Lockley, and A. Lindsay Frazier. Adolescent and young adult germ cell tumors: epidemiology, genomics, treatment, and survivorship. Journal of clinical oncology : official journal of the American Society of Clinical Oncology, pages JCO2301099, Oct 2024. URL: https://doi.org/10.1200/jco.23.01099, doi:10.1200/jco.23.01099. This article has 29 citations.

38. (travis2024adolescentandyoung pages 3-4): Lois B. Travis, Darren R. Feldman, Chunkit Fung, Jenny N. Poynter, Michelle Lockley, and A. Lindsay Frazier. Adolescent and young adult germ cell tumors: epidemiology, genomics, treatment, and survivorship. Journal of clinical oncology : official journal of the American Society of Clinical Oncology, pages JCO2301099, Oct 2024. URL: https://doi.org/10.1200/jco.23.01099, doi:10.1200/jco.23.01099. This article has 29 citations.