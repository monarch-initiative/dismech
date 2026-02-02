---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-01-31T17:15:42.089985'
end_time: '2026-01-31T17:20:40.456982'
duration_seconds: 298.37
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Breast Fibroadenoma
  mondo_id: ''
  category: Benign Tumor
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 12
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Breast Fibroadenoma
- **MONDO ID:**  (if available)
- **Category:** Benign Tumor

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Breast Fibroadenoma**.
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
- **Disease Name:** Breast Fibroadenoma
- **MONDO ID:**  (if available)
- **Category:** Benign Tumor

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Breast Fibroadenoma**.
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


# Disease Pathophysiology Research Report

## Target Disease
- Disease Name: Breast Fibroadenoma
- MONDO ID: 
- Category: Benign Tumor

## Executive Summary
Breast fibroadenoma (FA) is a benign, biphasic fibroepithelial neoplasm driven predominantly by stromal genetic alterations—most notably recurrent MED12 exon 2 hotspot mutations—that reprogram transcription via the Mediator kinase module and alter stromal–epithelial crosstalk. Progression within the fibroepithelial spectrum (from FA-like lesions to phyllodes tumor, PT) correlates with acquisition of additional hits such as TERT promoter mutations, with broader pathway involvement (e.g., PI3K–AKT, TP53, RB1, EGFR) in borderline/malignant PTs. Clinically, FAs occur in reproductive-age women, are hormone-responsive, and present as well-circumscribed, mobile masses; histologic architecture (intracanalicular vs pericanalicular) reflects stromal proliferation patterns directed by the stromal driver genotype. (loke2018geneticsandgenomics pages 1-1, loke2018geneticsandgenomics pages 3-5, chang2020med12tertand pages 2-2, waitzberg2023arebothdistinct pages 9-11)


| Entity type | Name and ontology ID | Mechanistic role in fibroadenoma | Evidence and key findings | Primary citations |
|---|---|---|---|---|
| Gene | MED12 (HGNC:16025) | Recurrent stromal hotspot mutations (exon 2, codon 44) drive stromal proliferation via disrupted Mediator/CDK activity | MED12 mutations are the dominant recurrent alteration in FAs, localized to stromal compartment and linked to stromal-driven phenotype and possible progression to PTs | (loke2018geneticsandgenomics pages 3-5, loke2018geneticsandgenomics pages 7-7, waitzberg2023arebothdistinct pages 9-11) |
| Gene | TERT promoter (TERT, HGNC:11730) | Telomere maintenance activation associated with progression (enriched in PTs vs FAs) | TERT promoter mutations/amplification frequently observed in phyllodes tumors and implicated as progression-associated hits | (chang2020med12tertand pages 2-2, waitzberg2023arebothdistinct pages 9-11) |
| Gene | RARA (HGNC:9864) | Recurrent mutations reported in FELs panel; potential transcriptional regulator in stromal cells | RARA included among top recurrently mutated genes in fibroepithelial lesion sequencing panels | (chang2020med12tertand pages 1-1, loke2018geneticsandgenomics pages 5-6) |
| Gene | HMGA2 (HGNC:5009) | Historical chromosomal rearrangements (12q15) associated with benign tumorigenesis / ECM regulation | HMGA2 rearrangements identified in early cytogenetic studies as a recurrent alteration in benign breast lesions | (loke2018geneticsandgenomics pages 1-1) |
| Gene | PIK3CA (HGNC:8975) | Oncogenic PI3K pathway mutations more common in borderline/malignant PTs; uncommon in typical FAs | PIK3CA/PI3K–AKT alterations enriched in progressed PTs but not a frequent driver in conventional fibroadenomas | (chang2020med12tertand pages 2-2, loke2018geneticsandgenomics pages 5-6) |
| Gene | EGFR (HGNC:3236) | Receptor tyrosine kinase alterations seen in higher-grade PTs; may contribute to malignant transformation | EGFR mutations/alterations reported in malignant PTs and associated with progression features | (chang2020med12tertand pages 2-2) |
| Gene | TP53 (HGNC:11998) | Tumor suppressor loss/mutation linked to borderline/malignant PTs rather than typical FAs | TP53 alterations enriched in higher-grade fibroepithelial tumors and correlate with malignant histology | (chang2020med12tertand pages 2-2) |
| Gene | RB1 (HGNC:9884) | Cell-cycle control gene altered in PTs; associated with progression and increased genomic instability | RB1 mutations/loss noted more commonly in PTs versus FAs and linked to progression | (chang2020med12tertand pages 2-2) |
| Pathway | Wnt/beta-catenin signaling (GO:0016055) | Mediates epithelial–stromal crosstalk and may be dysregulated during fibroepithelial evolution | Wnt pathway components implicated in epithelial–stromal interactions relevant to lesion biology | (waitzberg2023arebothdistinct pages 9-11) |
| Pathway | Mediator kinase / CDK8-CDK19 complex (GO:0090543) | MED12 mutations impair Mediator-associated CDK activity altering transcriptional programs in stroma | Disruption of MED12–Cyclin C–CDK8/19 axis described as mechanistic consequence of exon 2 mutations | (loke2018geneticsandgenomics pages 3-5) |
| Pathway | PI3K–AKT signaling (GO:0043491) | Downstream growth/survival signaling; activated in progressed PTs and some related lesions | PI3K–AKT pathway alterations (including PIK3CA) observed in PTs; not predominant in typical FAs | (loke2018geneticsandgenomics pages 5-6, loke2018geneticsandgenomics pages 6-7) |
| Pathway | Telomere maintenance (GO:0000723) | TERT promoter changes enable replicative longevity during progression to PTs | TERT promoter mutations/amplifications are recurrent in phyllodes tumors and mark progression-associated genomic hits | (chang2020med12tertand pages 2-2) |
| Process | Stromal–epithelial signaling (GO:0048731) | Bidirectional paracrine signaling drives stromal proliferation and epithelial morphology changes | Stromal-driver model (stromal clonality, stromal mutations) and coordinated epithelial–stromal gene expression underpin lesion phenotype | (loke2018geneticsandgenomics pages 1-1, waitzberg2023arebothdistinct pages 9-11) |
| Cell type | Breast stromal fibroblast (CL:0002553) | Primary compartment bearing driver mutations (e.g., MED12); source of stromal overgrowth/ECM production | Laser microdissection and sequencing show MED12 mutations localized to stromal cells; stromal cellularity correlates with mutation status | (loke2018geneticsandgenomics pages 3-5, loke2018geneticsandgenomics pages 5-6) |
| Cell type | Luminal epithelial cell of mammary gland (CL:0002327) | Participates in epithelial–stromal crosstalk; morphology (intracanalicular vs pericanalicular) correlates with stromal genotype | Epithelial features influenced by stromal genotype; hormone receptor expression and epithelial signals interact with stromal drivers | (loke2018geneticsandgenomics pages 1-1, waitzberg2023arebothdistinct pages 9-11) |
| Cell type | Myoepithelial cell (CL:0002319) | Structural/contractile compartment influencing duct architecture and tumor histology | Myoepithelial layer contributes to lesion architecture and is part of biphasic lesion composition | (loke2018geneticsandgenomics pages 1-1) |
| Anatomy | Breast (UBERON:0000310) | Tissue context where biphasic fibroepithelial lesions arise; hormone-responsive microenvironment | FAs are benign breast fibroepithelial tumors of reproductive-age women and show hormone dependence | (loke2018geneticsandgenomics pages 1-1) |
| Anatomy | Mammary gland duct (UBERON:0008298) | Site of epithelial–stromal interactions; intracanalicular pattern often linked to MED12-mutant FAs | Intracanalicular fibroadenomas commonly harbor MED12 exon 2 mutations, linking ductal architecture to stromal genotype | (loke2018geneticsandgenomics pages 3-5, loke2018geneticsandgenomics pages 1-1) |
| Chemical | Estrogen (CHEBI:50114) | Hormonal driver/modulator of growth; interacts with Mediator complex and ER signaling in lesion biology | Fibroadenomas are hormone-responsive; Mediator complex (MED12) interfaces with estrogen receptor coactivation pathways | (loke2018geneticsandgenomics pages 1-1, loke2018geneticsandgenomics pages 7-7) |
| Chemical | Progesterone (CHEBI:17026) | Hormonal regulator of mammary proliferation and lesion dynamics | Progesterone contributes to reproductive-age growth patterns of FAs; stromal/epithelial receptors modulate response | (loke2018geneticsandgenomics pages 1-1) |


*Table: Concise table mapping genes, pathways, cell types, anatomy, and hormones implicated in breast fibroadenoma with brief mechanistic notes and primary evidence citations (pqac IDs). This synthesizes molecular findings useful for knowledge-base annotation.*


## 1. Core Pathophysiology
- Primary mechanisms
  - Stromal-driver model: Recurrent somatic MED12 mutations (exon 2, often codon 44) occur predominantly in the stromal compartment and are sufficient to drive stromal proliferation and extracellular matrix production that defines the FA phenotype. Mechanistically, MED12 mutations disrupt the MED12–Cyclin C–CDK8/19 Mediator kinase activity, altering transcriptional programs in stromal fibroblasts. (loke2018geneticsandgenomics pages 3-5, loke2018geneticsandgenomics pages 7-7)
  - Hormone-modulated growth: FAs are hormone-responsive lesions in reproductive-age women. MED12 and the Mediator complex interface with estrogen receptor signaling, supporting an endocrine-modulated stromal program without implicating hormone signaling as the sole causal driver. (loke2018geneticsandgenomics pages 1-1, loke2018geneticsandgenomics pages 7-7)
- Dysregulated molecular pathways
  - Mediator kinase/CDK8–CDK19 axis: loss of Mediator-associated CDK activity secondary to MED12 exon 2 mutations. (loke2018geneticsandgenomics pages 3-5)
  - Wnt/β-catenin and epithelial–stromal signaling: implicated in bidirectional crosstalk and fibroepithelial progression. (waitzberg2023arebothdistinct pages 9-11)
  - PI3K–AKT pathway: uncommon in typical FAs but increasingly represented with progression to PT. (loke2018geneticsandgenomics pages 5-6, chang2020med12tertand pages 2-2)
  - Telomere maintenance: TERT promoter hotspot mutations/amplification enriched in PTs, associated with progression from FA-like lesions. (chang2020med12tertand pages 2-2, waitzberg2023arebothdistinct pages 9-11)

## 2. Key Molecular Players
- Genes/proteins
  - MED12 (HGNC:16025): Recurrent stromal hotspot mutations (exon 2) are the dominant driver in FAs; localized to stroma by laser microdissection; strongly associated with intracanalicular architecture. (loke2018geneticsandgenomics pages 3-5)
  - TERT promoter (TERT, HGNC:11730): Hotspot promoter mutations/amplification are common in PTs and mark progression-associated events; less frequent in FAs. (chang2020med12tertand pages 2-2, waitzberg2023arebothdistinct pages 9-11)
  - RARA (HGNC:9864): Recurrently mutated within targeted panels of fibroepithelial lesions; likely contributes to transcriptional regulation in stromal cells; more often represented in PTs than typical FAs. (chang2020med12tertand pages 1-1, loke2018geneticsandgenomics pages 5-6)
  - HMGA2 (HGNC:5009): Classical 12q15 rearrangements historically found in benign breast lesions, indicating alternative stromal chromatin/ECM regulatory routes in a subset. (loke2018geneticsandgenomics pages 1-1)
  - PIK3CA (HGNC:8975): PI3K pathway mutations are not frequent in typical FAs but are enriched with progression to borderline/malignant PTs. (loke2018geneticsandgenomics pages 5-6, chang2020med12tertand pages 2-2)
  - EGFR (HGNC:3236), TP53 (HGNC:11998), RB1 (HGNC:9884): Altered predominantly in borderline/malignant PTs, supporting a stepwise accumulation of genomic hits with progression; rare in conventional FAs. (chang2020med12tertand pages 2-2)
- Chemical entities
  - Estrogen (CHEBI:50114) and progesterone (CHEBI:17026): Modulate lesion growth and phenotype via receptor-mediated effects; FAs are hormone-responsive and regress with menopause. (loke2018geneticsandgenomics pages 1-1)
- Cell types
  - Stromal fibroblasts (primary neoplastic compartment) bearing MED12 mutations; epithelial elements are largely reactive and reflect stromal signaling. (loke2018geneticsandgenomics pages 3-5, loke2018geneticsandgenomics pages 5-6)
  - Luminal and myoepithelial cells (non-neoplastic components) that help shape biphasic histology. (loke2018geneticsandgenomics pages 1-1)
- Anatomical locations
  - Breast parenchyma and mammary gland ducts are the microanatomic sites of epithelial–stromal interactions shaping intracanalicular vs pericanalicular patterns. (loke2018geneticsandgenomics pages 1-1, loke2018geneticsandgenomics pages 3-5)

## 3. Biological Processes (GO)
- Transcriptional regulation via Mediator kinase module (e.g., “RNA polymerase II transcription mediator complex CDK8 module”) perturbed by MED12 exon 2 mutations. (loke2018geneticsandgenomics pages 3-5)
- Stromal–epithelial signaling pathways, including Wnt/β-catenin mediated crosstalk influencing epithelial morphology. (waitzberg2023arebothdistinct pages 9-11)
- Telomere maintenance processes activated in progression (TERT promoter alterations). (chang2020med12tertand pages 2-2)
- PI3K–AKT signaling increased with progression; not typically a core pathway in conventional FAs. (loke2018geneticsandgenomics pages 5-6, chang2020med12tertand pages 2-2)

## 4. Cellular Components
- Nuclear Mediator complex within stromal fibroblasts as a central locus of dysfunction due to MED12 mutations. (loke2018geneticsandgenomics pages 3-5)
- Plasma membrane receptors (ER, growth factor receptors) participating in stromal–epithelial signaling. (loke2018geneticsandgenomics pages 7-7, chang2020med12tertand pages 2-2)
- Extracellular matrix (ECM) and periductal stroma as the pathologic substrate of stromal expansion and ductal deformation. (loke2018geneticsandgenomics pages 1-1)

## 5. Disease Progression
- Initiation: Acquisition of MED12 exon 2 mutations in a stromal fibroblast clone establishes a monoclonal, stromal-driven lesion; intracanalicular architecture is common in MED12-mutant FAs. (loke2018geneticsandgenomics pages 3-5)
- Early lesion biology: Hormone-responsive growth with stromal proliferation compressing epithelial ducts; bidirectional paracrine signaling shapes biphasic histology. (loke2018geneticsandgenomics pages 1-1, waitzberg2023arebothdistinct pages 9-11)
- Potential evolution: A subset of fibroepithelial lesions—molecularly linked by shared MED12 mutations—acquire additional hits (e.g., TERT promoter mutation, and with further progression, PI3K–AKT, TP53/RB1/EGFR alterations), corresponding to transition toward benign/borderline/malignant PT. Shared mutations and genomic studies support clonal relationships in some cases. (chang2020med12tertand pages 2-2, loke2018geneticsandgenomics pages 5-6, loke2018geneticsandgenomics pages 7-7, waitzberg2023arebothdistinct pages 9-11)

## 6. Phenotypic Manifestations (Clinical Correlates)
- Typical phenotype: Well-circumscribed, mobile masses in reproductive-age women; hormone-sensitive growth (e.g., enlargement in pregnancy, regression after menopause). These features match stromal-driver biology with endocrine modulation. (loke2018geneticsandgenomics pages 1-1)
- Histopathology: Biphasic proliferation with stromal overgrowth compressing ducts (intracanalicular) or surrounding ducts (pericanalicular). Intracanalicular FA frequently harbors MED12 mutations, linking histology to genotype. (loke2018geneticsandgenomics pages 3-5)
- Differential diagnosis and progression risk: Cellular FAs and benign PTs overlap morphologically; enrichment of TERT promoter and higher mutation burden, plus allelic imbalances, supports PT over FA and aligns with progression biology. (chang2020med12tertand pages 2-2)

## 7. Current Applications and Implementations
- Molecular adjuncts to diagnosis: Targeted panels that include MED12 exon 2 and TERT promoter (often alongside RARA and other recurrently altered genes) aid in distinguishing FA from PT on limited biopsy, prompting re-evaluation when high-risk alterations (e.g., TERTp, TP53) are detected. (chang2020med12tertand pages 2-2)
- Compartment-resolved testing: Recognition that the stromal compartment is the neoplastic driver (MED12 localized to stroma) informs sampling and interpretation on microdissected or stroma-enriched assays. (loke2018geneticsandgenomics pages 3-5)

## 8. Expert Opinions and Recent Research (emphasis 2023–2024)
- 2023 stromal–epithelial analyses emphasize recurrent MED12 mutations in FAs and the role of TERT promoter alterations in PTs, with coordinated yet distinct transcriptional programs in stroma versus epithelium that segregate FA from PT—supporting a progression model in a subset of cases. (waitzberg2023arebothdistinct pages 9-11)
- Contemporary reviews stress that MED12 is the key recurrent driver across fibroepithelial tumors, while TERT/RARA and other events stratify risk and grade, underscoring the practical value of including these loci in diagnostic workflows. (chang2020med12tertand pages 1-1)

## 9. Relevant Statistics and Data
- MED12 mutation frequency: Multiple sequencing studies report MED12 mutations in a substantial fraction of FAs (often around ~60%, with hotspot at codon 44 of exon 2), predominantly in the stromal compartment. (loke2018geneticsandgenomics pages 3-5)
- PT progression markers: TERT promoter mutations and higher overall mutational burden/LOH are enriched in borderline/malignant PTs versus FAs, consistent with a stepwise progression model. (chang2020med12tertand pages 2-2)

## Knowledge Base Annotations
- Genes/proteins (HGNC): MED12 (HGNC:16025); TERT (HGNC:11730); RARA (HGNC:9864); HMGA2 (HGNC:5009); PIK3CA (HGNC:8975); EGFR (HGNC:3236); TP53 (HGNC:11998); RB1 (HGNC:9884). (loke2018geneticsandgenomics pages 3-5, chang2020med12tertand pages 2-2, loke2018geneticsandgenomics pages 1-1, loke2018geneticsandgenomics pages 5-6)
- Biological processes (GO): Wnt signaling pathway (GO:0016055); Mediator complex CDK8 module (GO:0090543); PI3K–AKT signaling (GO:0043491); Telomere maintenance (GO:0000723); Stromal–epithelial signaling (related processes). (loke2018geneticsandgenomics pages 3-5, waitzberg2023arebothdistinct pages 9-11, loke2018geneticsandgenomics pages 5-6, chang2020med12tertand pages 2-2)
- Cellular components: Mediator complex/CDK8 module (nuclear); plasma membrane receptor signaling platforms; extracellular matrix/periductal stroma. (loke2018geneticsandgenomics pages 3-5, chang2020med12tertand pages 2-2, loke2018geneticsandgenomics pages 1-1)
- Cell types (CL): Breast stromal fibroblast; Luminal epithelial cell of mammary gland; Myoepithelial cell. (loke2018geneticsandgenomics pages 3-5, loke2018geneticsandgenomics pages 1-1)
- Anatomical locations (UBERON): Breast (UBERON:0000310); Mammary gland duct (UBERON:0008298). (loke2018geneticsandgenomics pages 1-1)
- Chemical entities (CHEBI): Estrogen (CHEBI:50114); Progesterone (CHEBI:17026). (loke2018geneticsandgenomics pages 1-1)
- Phenotypes (HP, examples): Palpable breast mass; Mobile, well-circumscribed lesion; Hormone-responsive growth—mechanistically linked to stromal drivers and endocrine modulation. (loke2018geneticsandgenomics pages 1-1)

## Evidence Items with Citations, URLs, and Dates
- Loke BN et al. Genetics and genomics of breast fibroadenomas. Journal of Clinical Pathology. 2018 Dec;71(5):381–387. URL: https://doi.org/10.1136/jclinpath-2017-204838 (Supports stromal MED12 driver model; hormone dependence; HMGA2 historical rearrangements; intracanalicular association) (loke2018geneticsandgenomics pages 1-1, loke2018geneticsandgenomics pages 3-5, loke2018geneticsandgenomics pages 7-7)
- Chang HY et al. MED12, TERT and RARA in fibroepithelial tumours of the breast. Journal of Clinical Pathology. 2020 Oct;73(1):51–56. URL: https://doi.org/10.1136/jclinpath-2019-206208 (Summarizes recurrent MED12 and enrichment of TERTp/PIK3CA/TP53/RB1/EGFR with PT progression; diagnostic utility of 16-gene panels) (chang2020med12tertand pages 2-2, chang2020med12tertand pages 1-1)
- Waitzberg ÁFL et al. Are both distinct epithelial and stromal cells… Acta Cirúrgica Brasileira. 2023 Dec;38:e202386823. URL: https://doi.org/10.1590/acb386823 (2023 study underscoring MED12 in FAs; TERT promoter mutations in PTs; coordinated yet distinct stromal vs epithelial programs; implications for progression) (waitzberg2023arebothdistinct pages 9-11)

## Limitations and Open Questions
- While MED12-driven stromal initiation is well-supported, the precise downstream transcriptional programs and microenvironmental cues that distinguish stable FAs from those at risk for progression need larger, prospective, compartment-resolved datasets. (waitzberg2023arebothdistinct pages 9-11, chang2020med12tertand pages 2-2)
- PI3K–AKT pathway alterations are uncommon in typical FAs but contribute to higher-grade PTs; their prevalence and functional impact within cellular FAs warrant additional study. (loke2018geneticsandgenomics pages 5-6, chang2020med12tertand pages 2-2)

## Conclusion
A coherent stromal-driver framework—anchored by recurrent MED12 exon 2 mutations perturbing the Mediator kinase module—explains the core pathophysiology of breast fibroadenoma. Hormonal milieu and stromal–epithelial signaling shape the benign biphasic phenotype, while progression toward phyllodes tumor correlates with acquisition of TERT promoter and other pathway alterations. These insights underpin practical molecular adjuncts to diagnosis (e.g., MED12/TERTp testing on core biopsies) and clarify how genotype maps to histology and clinical behavior in fibroepithelial lesions. (loke2018geneticsandgenomics pages 3-5, chang2020med12tertand pages 2-2, waitzberg2023arebothdistinct pages 9-11, loke2018geneticsandgenomics pages 1-1)

References

1. (loke2018geneticsandgenomics pages 1-1): Benjamin Nathanael Loke, Nur Diyana Md Nasir, Aye Aye Thike, Jonathan Yu Han Lee, Cheok Soon Lee, Bin Tean Teh, and Puay Hoon Tan. Genetics and genomics of breast fibroadenomas. Journal of Clinical Pathology, 71:381-387, Dec 2018. URL: https://doi.org/10.1136/jclinpath-2017-204838, doi:10.1136/jclinpath-2017-204838. This article has 57 citations and is from a peer-reviewed journal.

2. (loke2018geneticsandgenomics pages 3-5): Benjamin Nathanael Loke, Nur Diyana Md Nasir, Aye Aye Thike, Jonathan Yu Han Lee, Cheok Soon Lee, Bin Tean Teh, and Puay Hoon Tan. Genetics and genomics of breast fibroadenomas. Journal of Clinical Pathology, 71:381-387, Dec 2018. URL: https://doi.org/10.1136/jclinpath-2017-204838, doi:10.1136/jclinpath-2017-204838. This article has 57 citations and is from a peer-reviewed journal.

3. (chang2020med12tertand pages 2-2): Huan Ying Chang, Valerie Cui Yun Koh, Nur Diyana Md Nasir, Cedric Chuan Young Ng, Peiyong Guan, Aye Aye Thike, Bin Tean Teh, and Puay Hoon Tan. Med12, tert and rara in fibroepithelial tumours of the breast. Journal of Clinical Pathology, 73:51-56, Oct 2020. URL: https://doi.org/10.1136/jclinpath-2019-206208, doi:10.1136/jclinpath-2019-206208. This article has 44 citations and is from a peer-reviewed journal.

4. (waitzberg2023arebothdistinct pages 9-11): Ângela Flavia Logullo Waitzberg, Elisa Napolitano e Ferreira, Mabel Pinilla, Paulo Pineda, Andréa Cristina de Moraes Malinverni, Fernando Augusto Soares, and Dirce Maria Carraro. Are both distinct epithelial and stromal cells molecular analysis from phyllodes tumors versus fibroadenoma components affected in breast fibroepithelial progression? Acta Cirúrgica Brasileira, Dec 2023. URL: https://doi.org/10.1590/acb386823, doi:10.1590/acb386823. This article has 2 citations.

5. (loke2018geneticsandgenomics pages 7-7): Benjamin Nathanael Loke, Nur Diyana Md Nasir, Aye Aye Thike, Jonathan Yu Han Lee, Cheok Soon Lee, Bin Tean Teh, and Puay Hoon Tan. Genetics and genomics of breast fibroadenomas. Journal of Clinical Pathology, 71:381-387, Dec 2018. URL: https://doi.org/10.1136/jclinpath-2017-204838, doi:10.1136/jclinpath-2017-204838. This article has 57 citations and is from a peer-reviewed journal.

6. (chang2020med12tertand pages 1-1): Huan Ying Chang, Valerie Cui Yun Koh, Nur Diyana Md Nasir, Cedric Chuan Young Ng, Peiyong Guan, Aye Aye Thike, Bin Tean Teh, and Puay Hoon Tan. Med12, tert and rara in fibroepithelial tumours of the breast. Journal of Clinical Pathology, 73:51-56, Oct 2020. URL: https://doi.org/10.1136/jclinpath-2019-206208, doi:10.1136/jclinpath-2019-206208. This article has 44 citations and is from a peer-reviewed journal.

7. (loke2018geneticsandgenomics pages 5-6): Benjamin Nathanael Loke, Nur Diyana Md Nasir, Aye Aye Thike, Jonathan Yu Han Lee, Cheok Soon Lee, Bin Tean Teh, and Puay Hoon Tan. Genetics and genomics of breast fibroadenomas. Journal of Clinical Pathology, 71:381-387, Dec 2018. URL: https://doi.org/10.1136/jclinpath-2017-204838, doi:10.1136/jclinpath-2017-204838. This article has 57 citations and is from a peer-reviewed journal.

8. (loke2018geneticsandgenomics pages 6-7): Benjamin Nathanael Loke, Nur Diyana Md Nasir, Aye Aye Thike, Jonathan Yu Han Lee, Cheok Soon Lee, Bin Tean Teh, and Puay Hoon Tan. Genetics and genomics of breast fibroadenomas. Journal of Clinical Pathology, 71:381-387, Dec 2018. URL: https://doi.org/10.1136/jclinpath-2017-204838, doi:10.1136/jclinpath-2017-204838. This article has 57 citations and is from a peer-reviewed journal.