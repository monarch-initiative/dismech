# Cancer Curation Project

## Overview
Comprehensive curation of cancers for the dismech knowledge base, prioritizing malignancies with **precise genetic etiology** and **well-characterized pathophysiological progression**. This project focuses on cancers where:
1. Single-gene or well-defined fusion gene drivers are established
2. Molecular mechanisms are understood at the pathway level
3. Genotype-phenotype correlations inform treatment decisions
4. Progressive stages of tumorigenesis are documented

## Selection Criteria
Cancers are prioritized based on:
- **Genetic precision**: Clear driver mutations, fusion genes, or germline predisposition
- **Pathway clarity**: Well-understood molecular cascades (e.g., RAS-MAPK, Wnt/β-catenin, HIF/VHL)
- **Therapeutic relevance**: Targeted therapies directly addressing genetic defects
- **Educational value**: Paradigmatic examples of cancer biology (e.g., two-hit hypothesis, oncogene addiction)

## Existing Cancer-Related Entries in KB (4)
| Disease | File | Focus |
|---------|------|-------|
| Lynch Syndrome | Lynch_Syndrome.yaml | MMR deficiency, hereditary CRC |
| Non-Small Cell Lung Cancer | Non-Small_Cell_Lung_Cancer.yaml | EGFR/KRAS/ALK mutations |
| Primary Tonsillar Lymphoma | Primary_Tonsillar_Lymphoma.yaml | Hematologic malignancy |
| Melanoma in Congenital Melanocytic Nevus | Melanoma_in_Congenital_Melanocytic_Nevus.yaml | NRAS/BRAF mutations |
| Fanconi Anemia | Fanconi_Anemia.yaml | DNA repair, cancer predisposition |

## Cancers to Curate

### Tier 1: Paradigmatic Single-Gene Driver Cancers (Highest Priority)
These represent textbook examples of cancer genetics with direct therapeutic implications.

| Cancer | Gene(s) | Mechanism | Therapeutic Target | Status |
|--------|---------|-----------|-------------------|--------|
| Chronic Myeloid Leukemia | BCR-ABL1 | Constitutive tyrosine kinase | Imatinib, TKIs | [ ] |
| Retinoblastoma | RB1 | Two-hit tumor suppressor | - | [ ] |
| Gastrointestinal Stromal Tumor | KIT, PDGFRA | Receptor tyrosine kinase | Imatinib, Avapritinib | [ ] |
| Medullary Thyroid Carcinoma | RET | Oncogenic receptor activation | Selpercatinib | [ ] |
| Clear Cell Renal Cell Carcinoma | VHL | HIF dysregulation | Belzutifan (HIF-2α) | [ ] |
| Ewing Sarcoma | EWS-FLI1 | Aberrant transcription factor | - | [ ] |

### Tier 2: Hereditary Cancer Syndromes (High Priority)
Well-characterized germline mutations with defined progression pathways.

| Syndrome/Cancer | Gene(s) | Associated Cancers | Mechanism | Status |
|----------------|---------|-------------------|-----------|--------|
| Li-Fraumeni Syndrome | TP53 | Sarcomas, breast, brain, adrenal | p53 tumor suppressor loss | [ ] |
| Familial Adenomatous Polyposis | APC | Colorectal cancer | Wnt/β-catenin activation | [ ] |
| Von Hippel-Lindau Disease | VHL | RCC, hemangioblastoma, pheochromocytoma | HIF stabilization | [ ] |
| MEN2A/2B | RET | MTC, pheochromocytoma, parathyroid | RET gain-of-function | [ ] |
| Hereditary Breast/Ovarian Cancer | BRCA1, BRCA2 | Breast, ovarian, pancreatic, prostate | DNA repair deficiency | [ ] |
| Neurofibromatosis Type 1 | NF1 | MPNST, optic glioma, neurofibromas | RAS-MAPK hyperactivation | [ ] |

### Tier 3: Cancers with Clear Molecular Subtypes (Medium Priority)
Defined molecular classifications guiding precision medicine.

| Cancer | Key Mutations/Alterations | Molecular Subtypes | Status |
|--------|--------------------------|-------------------|--------|
| Acute Myeloid Leukemia | FLT3, NPM1, IDH1/2, DNMT3A | ELN risk stratification | [ ] |
| Colorectal Cancer (Sporadic) | APC, KRAS, TP53, BRAF | CMS1-4 subtypes | [ ] |
| Breast Cancer (HER2+) | ERBB2 amplification | HER2-enriched | [ ] |
| Melanoma | BRAF V600E, NRAS, NF1 | BRAF-mutant vs WT | [ ] |
| Glioblastoma | IDH1/2, MGMT, EGFR | IDH-mutant vs wildtype | [ ] |
| Pancreatic Ductal Adenocarcinoma | KRAS, CDKN2A, TP53, SMAD4 | Classical vs basal-like | [ ] |

### Tier 4: Pediatric Cancers with Fusion Genes (Medium Priority)
Defined by characteristic chromosomal translocations.

| Cancer | Fusion Gene | Mechanism | Status |
|--------|-------------|-----------|--------|
| Ewing Sarcoma | EWS-FLI1 (t(11;22)) | Aberrant transcription | [ ] |
| Alveolar Rhabdomyosarcoma | PAX3-FOXO1, PAX7-FOXO1 | Transcription factor fusion | [ ] |
| Synovial Sarcoma | SS18-SSX | Chromatin remodeling | [ ] |
| Acute Lymphoblastic Leukemia (Ph+) | BCR-ABL1 | Tyrosine kinase | [ ] |
| Neuroblastoma | MYCN amplification | Transcription factor | [ ] |

### Tier 5: Molecularly-Defined Breast Cancer Subtypes (High Priority)
Modern oncology treats these as distinct disease entities requiring different therapeutic approaches.

| Cancer | Defining Feature | Key Therapy | Status |
|--------|-----------------|-------------|--------|
| HER2-Positive Breast Cancer | ERBB2 amplification | Trastuzumab, T-DXd | [ ] |
| Triple-Negative Breast Cancer | ER-/PR-/HER2- | Pembrolizumab + chemo, sacituzumab | [ ] |
| ER-Positive/HER2-Negative Breast Cancer | Hormone receptor+ | Aromatase inhibitors, CDK4/6i | [ ] |
| PIK3CA-Mutant Breast Cancer | PIK3CA hotspot mutations | Alpelisib | [ ] |

### Tier 6: Molecularly-Defined Lung Cancer Subtypes (High Priority)
Lung cancer is now treated as multiple distinct molecular diseases.

| Cancer | Defining Feature | Key Therapy | Status |
|--------|-----------------|-------------|--------|
| EGFR-Mutant NSCLC | EGFR exon 19 del, L858R | Osimertinib | [ ] |
| ALK-Rearranged NSCLC | ALK fusions (EML4-ALK) | Alectinib, lorlatinib | [ ] |
| ROS1-Rearranged NSCLC | ROS1 fusions | Crizotinib, entrectinib | [ ] |
| KRAS G12C-Mutant NSCLC | KRAS G12C | Sotorasib, adagrasib | [ ] |
| MET Exon 14 Skipping NSCLC | MET splice mutations | Capmatinib, tepotinib | [ ] |
| RET-Rearranged NSCLC | RET fusions | Selpercatinib | [ ] |
| BRAF V600E-Mutant NSCLC | BRAF V600E | Dabrafenib + trametinib | [ ] |
| Small Cell Lung Cancer | RB1/TP53 loss, neuroendocrine | Platinum + etoposide | [ ] |

### Tier 7: Molecularly-Defined Melanoma and Skin Cancers (High Priority)
| Cancer | Defining Feature | Key Therapy | Status |
|--------|-----------------|-------------|--------|
| BRAF V600-Mutant Melanoma | BRAF V600E/K | Dabrafenib + trametinib | [ ] |
| NRAS-Mutant Melanoma | NRAS Q61 mutations | MEK inhibitors, immunotherapy | [ ] |
| KIT-Mutant Melanoma | KIT mutations (acral/mucosal) | Imatinib | [ ] |
| Uveal Melanoma | GNAQ/GNA11 mutations | Tebentafusp (HLA-A*02:01) | [ ] |
| Basal Cell Carcinoma | PTCH1, SMO (Hedgehog) | Vismodegib, sonidegib | [ ] |
| Merkel Cell Carcinoma | MCPyV, UV-induced | Avelumab, pembrolizumab | [ ] |

### Tier 8: Molecularly-Defined GI Cancers (High Priority)
| Cancer | Defining Feature | Key Therapy | Status |
|--------|-----------------|-------------|--------|
| MSI-High Colorectal Cancer | MMR deficiency, high TMB | Pembrolizumab | [ ] |
| BRAF V600E-Mutant Colorectal Cancer | BRAF V600E | Encorafenib + cetuximab | [ ] |
| HER2-Positive Colorectal Cancer | ERBB2 amplification | Trastuzumab + pertuzumab | [ ] |
| HER2-Positive Gastric Cancer | ERBB2 amplification | Trastuzumab, T-DXd | [ ] |
| Claudin 18.2+ Gastric Cancer | CLDN18.2 expression | Zolbetuximab | [ ] |
| Hepatocellular Carcinoma | Multiple pathways | Atezolizumab + bevacizumab | [ ] |
| Cholangiocarcinoma, IDH-Mutant | IDH1/2 mutations | Ivosidenib | [ ] |
| Cholangiocarcinoma, FGFR-Altered | FGFR2 fusions | Pemigatinib, futibatinib | [ ] |

### Tier 9: Molecularly-Defined Brain Tumors (High Priority)
WHO 2021 classification requires molecular markers for diagnosis.

| Cancer | Defining Feature | Key Features | Status |
|--------|-----------------|--------------|--------|
| IDH-Mutant Astrocytoma | IDH1/2 mutation, no 1p/19q | Better prognosis than WT | [ ] |
| IDH-Mutant Oligodendroglioma | IDH1/2 + 1p/19q codeletion | Chemosensitive | [ ] |
| Glioblastoma, IDH-Wildtype | IDH WT, +7/-10, TERT, EGFR | Temozolomide + RT | [ ] |
| H3 K27-Altered Diffuse Midline Glioma | H3K27M mutation | Pediatric, poor prognosis | [ ] |
| Medulloblastoma, WNT-Activated | WNT pathway, CTNNB1 | Excellent prognosis | [ ] |
| Medulloblastoma, SHH-Activated | SHH pathway, PTCH1/SMO | SMO inhibitors | [ ] |

### Tier 10: Molecularly-Defined Hematologic Malignancies (High Priority)
| Cancer | Defining Feature | Key Therapy | Status |
|--------|-----------------|-------------|--------|
| FLT3-Mutant AML | FLT3-ITD or TKD | Midostaurin, gilteritinib | [ ] |
| NPM1-Mutant AML | NPM1 mutation | Favorable risk | [ ] |
| IDH-Mutant AML | IDH1/2 mutations | Ivosidenib, enasidenib | [ ] |
| Core Binding Factor AML | t(8;21), inv(16) | Favorable, GO | [ ] |
| APL (PML-RARA) | t(15;17) PML-RARA | ATRA + ATO (cure ~90%) | [ ] |
| Ph+ ALL | BCR-ABL1 fusion | TKIs + chemo | [ ] |
| Ph-like ALL | ABL-class fusions, JAK/STAT | TKIs, JAK inhibitors | [ ] |
| Chronic Lymphocytic Leukemia | del(17p), TP53, IGHV | BTK inhibitors, venetoclax | [ ] |
| Mantle Cell Lymphoma | t(11;14) CCND1 | BTK inhibitors | [ ] |
| Diffuse Large B-Cell Lymphoma | ABC vs GCB, MYC/BCL2 | R-CHOP, polatuzumab | [ ] |

### Tier 11: Environmental Etiology Cancers (High Priority)
Cancers with strong environmental/infectious causation - important for prevention.

| Cancer | Environmental Factor | Mechanism | Status |
|--------|---------------------|-----------|--------|
| Malignant Mesothelioma | Asbestos | Fiber-induced inflammation | [ ] |
| Cervical Cancer | HPV 16/18 | E6/E7 oncoproteins | [ ] |
| HPV-Positive Head and Neck SCC | HPV 16 | E6/E7 (oropharyngeal) | [ ] |
| HPV-Negative Head and Neck SCC | Tobacco, alcohol | TP53, CDKN2A mutations | [ ] |
| Nasopharyngeal Carcinoma | EBV | LMP1/LMP2 oncogenes | [ ] |
| Gastric Cancer, H. pylori-Associated | H. pylori | CagA, chronic inflammation | [ ] |
| EBV-Associated Gastric Cancer | EBV | CIMP-high, PIK3CA | [ ] |
| Burkitt Lymphoma | EBV (endemic) | MYC translocation | [ ] |
| Kaposi Sarcoma | HHV-8/KSHV | vGPCR, vFLIP | [ ] |
| Adult T-Cell Leukemia/Lymphoma | HTLV-1 | Tax oncoprotein | [ ] |
| Aflatoxin-Related HCC | Aflatoxin B1 + HBV | TP53 R249S hotspot | [ ] |
| Arsenic-Related Cancers | Arsenic in water | Skin, lung, bladder | [ ] |

### Tier 12: Other Molecularly-Defined Solid Tumors (Medium Priority)
| Cancer | Defining Feature | Key Therapy | Status |
|--------|-----------------|-------------|--------|
| FGFR-Altered Urothelial Carcinoma | FGFR3 mutations/fusions | Erdafitinib | [ ] |
| BRCA-Mutant Prostate Cancer | BRCA1/2 somatic | Olaparib, rucaparib | [ ] |
| MSI-High Endometrial Cancer | MMR deficiency | Pembrolizumab + lenvatinib | [ ] |
| NTRK Fusion-Positive Cancers | NTRK1/2/3 fusions | Larotrectinib, entrectinib | [ ] |
| Thyroid Cancer, BRAF-Mutant | BRAF V600E (PTC) | Dabrafenib + trametinib | [ ] |
| Thyroid Cancer, RET-Fusion | RET fusions (PTC) | Selpercatinib | [ ] |
| Pheochromocytoma/Paraganglioma | SDHx, VHL, RET | Surveillance, surgery | [ ] |
| Polycythemia Vera | JAK2 V617F | Ruxolitinib | [ ] |
| Primary Myelofibrosis | JAK2, CALR, MPL | Ruxolitinib, fedratinib | [ ] |
| Essential Thrombocythemia | JAK2, CALR | Anagrelide, hydroxyurea | [ ] |

### Tier 13: Pediatric/Rare Sarcomas (Medium Priority)
| Cancer | Defining Feature | Key Features | Status |
|--------|-----------------|--------------|--------|
| Alveolar Rhabdomyosarcoma | PAX3/7-FOXO1 fusions | Aggressive pediatric | [ ] |
| Embryonal Rhabdomyosarcoma | Loss of 11p15 | Better prognosis | [ ] |
| Synovial Sarcoma | SS18-SSX fusions | Young adults | [ ] |
| Neuroblastoma | MYCN amplification | Risk stratification | [ ] |
| Wilms Tumor | WT1, WTX, CTNNB1 | Excellent outcomes | [ ] |
| Desmoplastic Small Round Cell Tumor | EWSR1-WT1 fusion | Poor prognosis | [ ] |
| Clear Cell Sarcoma | EWSR1-ATF1 fusion | "Melanoma of soft parts" | [ ] |
| Dermatofibrosarcoma Protuberans | COL1A1-PDGFB fusion | Imatinib responsive | [ ] |

## Molecular Subtypes as Discrete Entities

Modern precision oncology recognizes that cancers historically grouped together are actually distinct diseases requiring different treatments. This KB models them as separate entities:

### Breast Cancer Example
Instead of one "Breast Cancer" entry with subtypes, we have:
- **HER2-Positive Breast Cancer**: Defined by ERBB2 amplification; treated with trastuzumab, pertuzumab, T-DXd
- **Triple-Negative Breast Cancer**: ER-/PR-/HER2-; treated with immunotherapy + chemotherapy
- **ER-Positive Breast Cancer**: Hormone receptor-driven; treated with endocrine therapy + CDK4/6 inhibitors
- **PIK3CA-Mutant Breast Cancer**: Specific mutation; treated with alpelisib

### Rationale
1. **Different biology**: Molecular alterations drive fundamentally different tumor behavior
2. **Different treatment**: Each requires distinct therapeutic approaches
3. **Different prognosis**: Outcomes vary dramatically by molecular subtype
4. **Regulatory recognition**: FDA approvals are increasingly biomarker-specific
5. **Clinical practice**: Oncologists make treatment decisions based on molecular profile

### Environmental Cancers
Cancers with strong environmental/infectious etiology demonstrate:
- Gene-environment interactions (e.g., aflatoxin + HBV → TP53 R249S)
- Prevention opportunities (HPV vaccination, H. pylori eradication)
- Distinct molecular signatures from sporadic counterparts

## Key Pathways to Document

### Tumor Suppressor Pathways
1. **RB1/E2F pathway** - Cell cycle checkpoint control
2. **TP53 pathway** - DNA damage response, apoptosis
3. **APC/Wnt/β-catenin** - Intestinal stem cell regulation
4. **VHL/HIF** - Oxygen sensing, angiogenesis
5. **BRCA/DNA repair** - Homologous recombination

### Oncogenic Signaling Cascades
1. **RAS-RAF-MEK-ERK (MAPK)** - Cell proliferation
2. **PI3K-AKT-mTOR** - Cell growth, survival
3. **JAK-STAT** - Cytokine signaling
4. **Hedgehog** - Developmental signaling
5. **Notch** - Cell fate determination

### Receptor Tyrosine Kinases
1. **BCR-ABL** - CML paradigm
2. **KIT/PDGFRA** - GIST
3. **RET** - MTC, MEN2
4. **EGFR/HER2** - Lung, breast cancer
5. **ALK** - Lung cancer, lymphoma

## Research Sources (2025-2026)

Recent developments informing this curation:
- [AACR Cancer Progress Report 2025](https://cancerprogressreport.aacr.org/progress/cpr25-contents/cpr25-understanding-the-path-to-cancer-development/) - ecDNA in 17% of cancers
- [Genetic background sets trajectory of cancer evolution (2025)](https://www.biorxiv.org/content/10.1101/2025.01.13.632787v1) - Germline-somatic interactions
- [Blood cancer protective variant (2026)](https://www.statnews.com/2026/01/01/blood-cancer-protective-genetic-variant-found-in-study/) - CHIP protection
- [VHL signaling in ccRCC (2024)](https://www.nature.com/articles/s41585-024-00876-w) - HIF-2α targeting
- [Li-Fraumeni syndrome sperm donor case (2025)](https://en.wikipedia.org/wiki/Li%E2%80%93Fraumeni_syndrome) - 100% female penetrance

---
# STATUS

## Tier 1: Paradigmatic Single-Gene Drivers (6/6) ✓
- [x] Chronic Myeloid Leukemia (BCR-ABL1) - Created 2026-01-24, 60.4% compliance
- [x] Retinoblastoma (RB1) - Created 2026-01-24, 55.9% compliance
- [x] Gastrointestinal Stromal Tumor (KIT/PDGFRA) - Created 2026-01-24, 45.9% compliance
- [x] Medullary Thyroid Carcinoma (RET) - Created 2026-01-24
- [x] Clear Cell Renal Cell Carcinoma (VHL) - Created 2026-01-24
- [x] Ewing Sarcoma (EWS-FLI1) - Created 2026-01-24

## Tier 2: Hereditary Cancer Syndromes (6/6) ✓
- [x] Li-Fraumeni Syndrome (TP53) - Created 2026-01-24
- [x] Familial Adenomatous Polyposis (APC) - Created 2026-01-24
- [x] Von Hippel-Lindau Disease (VHL) - Created 2026-01-24
- [x] Multiple Endocrine Neoplasia Type 2 (RET) - Created 2026-01-24
- [x] Hereditary Breast and Ovarian Cancer Syndrome (BRCA1/2) - Created 2026-01-24
- [x] Neurofibromatosis Type 1 (NF1) - Created 2026-01-24

## Tier 5: Molecularly-Defined Breast Cancer (0/4)
- [ ] HER2-Positive Breast Cancer
- [ ] Triple-Negative Breast Cancer
- [ ] ER-Positive/HER2-Negative Breast Cancer
- [ ] PIK3CA-Mutant Breast Cancer

## Tier 6: Molecularly-Defined Lung Cancer (0/8)
- [ ] EGFR-Mutant NSCLC
- [ ] ALK-Rearranged NSCLC
- [ ] ROS1-Rearranged NSCLC
- [ ] KRAS G12C-Mutant NSCLC
- [ ] MET Exon 14 Skipping NSCLC
- [ ] RET-Rearranged NSCLC
- [ ] BRAF V600E-Mutant NSCLC
- [ ] Small Cell Lung Cancer

## Tier 7: Molecularly-Defined Melanoma/Skin (0/6)
- [ ] BRAF V600-Mutant Melanoma
- [ ] NRAS-Mutant Melanoma
- [ ] KIT-Mutant Melanoma
- [ ] Uveal Melanoma
- [ ] Basal Cell Carcinoma
- [ ] Merkel Cell Carcinoma

## Tier 8: Molecularly-Defined GI Cancers (0/8)
- [ ] MSI-High Colorectal Cancer
- [ ] BRAF V600E-Mutant Colorectal Cancer
- [ ] HER2-Positive Colorectal Cancer
- [ ] HER2-Positive Gastric Cancer
- [ ] Claudin 18.2+ Gastric Cancer
- [ ] Hepatocellular Carcinoma
- [ ] Cholangiocarcinoma, IDH-Mutant
- [ ] Cholangiocarcinoma, FGFR-Altered

## Tier 9: Molecularly-Defined Brain Tumors (0/6)
- [ ] IDH-Mutant Astrocytoma
- [ ] IDH-Mutant Oligodendroglioma
- [ ] Glioblastoma, IDH-Wildtype
- [ ] H3 K27-Altered Diffuse Midline Glioma
- [ ] Medulloblastoma, WNT-Activated
- [ ] Medulloblastoma, SHH-Activated

## Tier 10: Molecularly-Defined Hematologic Malignancies (0/10)
- [ ] FLT3-Mutant AML
- [ ] NPM1-Mutant AML
- [ ] IDH-Mutant AML
- [ ] Core Binding Factor AML
- [ ] APL (PML-RARA)
- [ ] Ph+ ALL
- [ ] Ph-like ALL
- [ ] Chronic Lymphocytic Leukemia
- [ ] Mantle Cell Lymphoma
- [ ] Diffuse Large B-Cell Lymphoma

## Tier 11: Environmental Etiology Cancers (0/12)
- [ ] Malignant Mesothelioma (asbestos)
- [ ] Cervical Cancer (HPV)
- [ ] HPV-Positive Head and Neck SCC
- [ ] HPV-Negative Head and Neck SCC
- [ ] Nasopharyngeal Carcinoma (EBV)
- [ ] Gastric Cancer, H. pylori-Associated
- [ ] EBV-Associated Gastric Cancer
- [ ] Burkitt Lymphoma (EBV)
- [ ] Kaposi Sarcoma (HHV-8)
- [ ] Adult T-Cell Leukemia/Lymphoma (HTLV-1)
- [ ] Aflatoxin-Related HCC
- [ ] Arsenic-Related Cancers

## Tier 12: Other Molecularly-Defined Solid Tumors (0/10)
- [ ] FGFR-Altered Urothelial Carcinoma
- [ ] BRCA-Mutant Prostate Cancer
- [ ] MSI-High Endometrial Cancer
- [ ] NTRK Fusion-Positive Cancers
- [ ] Thyroid Cancer, BRAF-Mutant
- [ ] Thyroid Cancer, RET-Fusion
- [ ] Pheochromocytoma/Paraganglioma
- [ ] Polycythemia Vera
- [ ] Primary Myelofibrosis
- [ ] Essential Thrombocythemia

## Tier 13: Pediatric/Rare Sarcomas (0/8)
- [ ] Alveolar Rhabdomyosarcoma
- [ ] Embryonal Rhabdomyosarcoma
- [ ] Synovial Sarcoma
- [ ] Neuroblastoma
- [ ] Wilms Tumor
- [ ] Desmoplastic Small Round Cell Tumor
- [ ] Clear Cell Sarcoma
- [ ] Dermatofibrosarcoma Protuberans

## Progress Summary
- **Total planned**: 78 cancers (original 28 + 50 expansion)
- **Completed**: 12/78 (15.4%)
- **In progress**: 0

### Expansion Rationale (50 new entries)
1. **Molecularly-defined subtypes as discrete entities** (Tiers 5-10, 12): Modern oncology recognizes that molecular markers define distinct disease entities requiring different treatments. HER2+ breast cancer is a fundamentally different disease from triple-negative breast cancer, not just a "subtype."

2. **Environmental etiology cancers** (Tier 11): Cancers with strong infectious/environmental causation demonstrate gene-environment interactions and are critical for prevention strategies.

3. **WHO classification alignment**: Brain tumors (Tier 9) now require molecular markers for diagnosis per WHO 2021 CNS classification.

4. **Actionable alterations**: Priority given to cancers with FDA-approved targeted therapies or immunotherapies linked to molecular features.

# NOTES

## 2026-01-24 (Tier 2 Evidence Integration Session)

**Tier 2 Evidence Integration Complete:**

Deep research completed and PMID evidence integrated for all 6 Tier 2 hereditary cancer syndromes:

| Syndrome | Evidence PMIDs | Key Evidence |
|----------|---------------|--------------|
| Li-Fraumeni Syndrome | PMID:26014290, PMID:28572266 | French cohort tumor spectrum, Toronto Protocol surveillance |
| Familial Adenomatous Polyposis | PMID:28668823 | Desmoid tumors, two-hit mechanism |
| Von Hippel-Lindau Disease | PMID:34818478 | Belzutifan phase 2 trial results |
| MEN2 | PMID:11786689, PMID:21862994 | RET mutations, prophylactic thyroidectomy |
| HBOC | PMID:22193408, PMID:34081848 | BRCA pathway, OlympiA olaparib trial |
| NF1 | PMID:33395032, PMID:32234870 | SPRINT selumetinib trial, MPNST transformation |

Compliance improvement (weighted scores):
- Li-Fraumeni Syndrome: 37.0% → 47.8%
- FAP: 41.9% → 48.8%
- VHL: 36.7% → 40.8%
- MEN2: 43.2% → 50.0%
- HBOC: 37.5% → 45.0%
- NF1: 43.6% → 51.3%

All 6 files pass validation (schema + terms + references).

---

## 2026-01-24 (Evidence Integration Session)

**Tier 1 Evidence Integration Complete:**

Deep research completed and PMID evidence integrated for all 6 Tier 1 cancers:

| Cancer | Evidence PMIDs | Key Evidence |
|--------|---------------|--------------|
| CML | PMID:11287972, PMID:11423618 | Druker imatinib trial, T315I mutation |
| Retinoblastoma | PMID:5279523 | Knudson two-hit hypothesis |
| GIST | PMID:12181401 | Demetri imatinib NEJM 2002 |
| MTC | PMID:32846061 | LIBRETTO-001 selpercatinib trial |
| ccRCC | PMID:37085424 | VHL/PBRM1/BAP1/SETD2 biomarkers |
| Ewing Sarcoma | PMID:33741715 | EWS-FLI1 transcriptional regulation |

All 6 files pass validation (schema + terms + references).

---

## 2026-01-24 (Initial Session)

**Tier 1 Complete - All 6 paradigmatic cancers curated:**

1. **Chronic Myeloid Leukemia** (BCR-ABL1) - 60.4% compliance
   - Deep research with falcon, key refs: PMID:11287972, PMID:11423618
   - Covers BCR-ABL1 fusion, TKI therapy, disease phases

2. **Retinoblastoma** (RB1) - 55.9% compliance
   - Key ref: PMID:5279523 (Knudson two-hit hypothesis)
   - Paradigm for tumor suppressor gene concept

3. **Gastrointestinal Stromal Tumor** (KIT/PDGFRA) - 45.9% compliance
   - KIT/PDGFRA mutations, imatinib, avapritinib

4. **Medullary Thyroid Carcinoma** (RET)
   - RET proto-oncogene, MEN2 syndromes, selpercatinib/pralsetinib

5. **Clear Cell Renal Cell Carcinoma** (VHL)
   - VHL/HIF pathway, belzutifan (HIF-2α inhibitor)

6. **Ewing Sarcoma** (EWS-FLI1)
   - Fusion transcription factor oncogene

Project created with comprehensive research on cancers with precise genetic etiology.

**Key selection rationale:**
- **Tier 1** represents "textbook" cancers where single genetic events drive disease (BCR-ABL in CML, KIT in GIST, etc.) - ideal for demonstrating oncogene addiction
- **Tier 2** covers hereditary syndromes with germline mutations - demonstrates two-hit hypothesis and cancer predisposition
- **Tier 3** includes common cancers with well-defined molecular subtypes guiding therapy
- **Tier 4** focuses on pediatric cancers defined by fusion genes - often "clean" genetic drivers
- **Tier 5** includes additional genetically-defined cancers for completeness

**Pathway themes to emphasize:**
1. Tumor suppressor loss (RB1, TP53, APC, VHL)
2. Oncogenic kinase activation (BCR-ABL, KIT, RET)
3. Transcription factor fusions (EWS-FLI1, PAX3-FOXO1)
4. DNA repair deficiency (BRCA1/2, MMR genes)
5. Epigenetic dysregulation (IDH1/2 mutations)

**Recommended curation order:**
Start with Tier 1 as these are the clearest examples of genotype-phenotype relationships and have FDA-approved targeted therapies demonstrating mechanism-based treatment.

---

## 2026-01-24 (Schema Enhancements)

**Added NCIT term support:**

1. **BiomarkerDescriptor** with NCIT validation for biochemical entries
2. **GeneProductDescriptor** with NCIT validation (rooted at NCIT:C26548 Gene Product) for pathophysiology
3. **`gene_products` slot** on Pathophysiology class for fusion proteins, oncoproteins, etc.

**Terms added to cancer files:**
- CML: NCIT:C16325 (BCR/ABL1 Fusion Protein)
- GIST: NCIT:C17328 (KIT receptor)
- MTC: NCIT:C18539 (RET receptor)

**Future work - Post-composition for complex aberrations:**

Explore OWL-style post-composition for fusion proteins and complex molecular aberrations that aren't in NCIT:
- EWS-FLI1 fusion protein (Ewing Sarcoma) - not currently in NCIT as protein entity
- VHL/pVHL protein (ccRCC) - gene exists, protein entity not found
- RB1/pRB protein (Retinoblastoma) - gene exists, protein entity not found
- Complex fusions with variant breakpoints (e.g., BCR-ABL p190 vs p210)

Consider using the `qualifiers` slot or creating a dedicated composition mechanism to express:
```yaml
# Example post-composition for missing fusion proteins
gene_products:
- preferred_term: EWS-FLI1 fusion protein
  description: Fusion of EWSR1 and FLI1 gene products
  qualifiers:
    - predicate: has_part
      value: {term: {id: NCIT:C17476, label: RNA-Binding Protein EWS}}
    - predicate: has_part
      value: {term: {id: NCIT:C17770, label: Friend Leukemia Virus Integration 1}}
```

This would allow precise annotation of fusion proteins even when pre-coordinated terms don't exist.

**Added Histopathology Section (2026-01-24):**

New dedicated `histopathology` slot on Disease class for microscopic tissue findings:

1. **HistopathologyFindingTerm** dynamic enum - rooted at:
   - NCIT:C35867 (Morphologic Finding) - patterns, dysplasia, necrosis
   - NCIT:C18000 (Histologic Grade) - Fuhrman, Nottingham, GIST grades
   - HP:0025461 (Abnormal cell morphology) - rosettes, inclusion bodies

2. **HistopathologyFindingDescriptor** class for term binding

3. **HistopathologyFinding** class with: name, finding_term, description, frequency, diagnostic, evidence, notes, context

**Example histopathology entries added:**
- Retinoblastoma: Flexner-Wintersteiner rosettes (HP:0031927), Homer Wright rosettes (HP:0031926), Fleurettes (NCIT:C35950)
- GIST: Spindle Cell Pattern (NCIT:C53643), Low Mitotic Activity (NCIT:C35961)

**Rationale:** Histopathology findings are microscopic observations distinct from clinical phenotypes. They often define tumor subtypes, inform prognosis, and require tissue sampling. Keeping them separate from phenotypes provides cleaner data modeling.
