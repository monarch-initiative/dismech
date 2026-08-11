---
provider: claude_code
model: claude-opus-4-8[1m]
cached: false
start_time: '2026-07-10T17:28:03.644697'
end_time: '2026-07-10T17:34:21.245167'
duration_seconds: 377.6
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: ER-Positive Breast Cancer
  mondo_id: ''
  category: ''
provider_config:
  timeout: 1800
  max_retries: 3
  parameters:
    allowed_domains: []
    claude_executable: claude
    skip_permissions: false
    allowed_tools:
    - WebSearch
    - WebFetch
    add_dirs: []
    timeout: 1800
    extra_args: []
run_metadata:
  models_used:
  - claude-opus-4-8[1m]
  num_turns: 24
  total_cost_usd: 2.888869
  session_id: 244ed95c-390a-4c57-9687-8cfd2bb21b17
  stop_reason: end_turn
citation_count: 10
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** ER-Positive Breast Cancer
- **MONDO ID:**  (if available)
- **Category:** 

## Research Objectives

Please provide a comprehensive research report on **ER-Positive Breast Cancer** covering all of the
disease characteristics listed below. This report will be used to populate a disease knowledge
base entry. Be thorough and cite primary literature (PMID preferred) for all claims.

For each section, **suggested databases/resources** are listed. These are the first places
you should search for information on each topic.

---

### 1. Disease Information
> **Search first:** OMIM, Orphanet, ICD-10/ICD-11, MeSH, PubMed

- What is the disease? Provide a concise overview.
- What are the key identifiers? (OMIM, Orphanet, ICD-10/ICD-11, MeSH, Mondo)
- What are the common synonyms and alternative names?
- Is the information derived from individual patients (e.g., EHR) or aggregated disease-level resources?

### 2. Etiology

- **Disease Causal Factors**: What are the primary causes? (genetic, environmental, infectious, mechanistic)
- **Risk Factors**:
  > **Search first:** PubMed, Cochrane Library, UpToDate, clinical guidelines, ClinVar, ClinGen, GWAS Catalog, PheGenI, CTD, CDC, WHO, epidemiological databases
  - Genetic risk factors (causal variants, susceptibility loci, modifier genes)
  - Environmental risk factors (toxins, lifestyle, occupational exposures, age, sex, family history)
- **Protective Factors**:
  > **Search first:** PubMed, Cochrane Library, clinical trial databases, GWAS Catalog, gnomAD, WHO, CDC, nutrition databases
  - Genetic protective factors (protective variants, modifier alleles)
  - Environmental protective factors (diet, lifestyle, exposures that reduce risk)
- **Gene-Environment Interactions**: How do genetic and environmental factors interact to influence disease?
  > **Search first:** CTD, PubMed, PheGenI, GxE databases

### 3. Phenotypes
> **Search first:** HPO (Human Phenotype Ontology), OMIM, Orphanet, PubMed, clinicaltrials.gov, MedDRA, SNOMED CT, DECIPHER, LOINC

For each phenotype, provide:
- **Phenotype type**: symptoms, clinical signs, physical manifestations, behavioral changes, or laboratory abnormalities
  > For symptoms/signs: HPO, OMIM, Orphanet, PubMed
  > For behavioral changes: HPO, DSM, RDoC (Research Domain Criteria), PubMed
  > For laboratory abnormalities: LOINC, SNOMED CT, LabTests Online, PubMed
- **Phenotype characteristics**:
  > **Search first:** OMIM, Orphanet, HPO, PubMed
  - Age of symptom onset (neonatal, childhood, adult-onset, late-onset)
  - Symptom severity (mild, moderate, severe, variable)
  - Symptom progression (stable, progressive, episodic, fluctuating)
  - Frequency among affected individuals (percentage or qualitative)
- **Quality of life impact**: Effects on daily functioning and well-being (per-phenotype when possible)
  > **Search first:** EQ-5D database, SF-36, WHO QOL databases, PubMed
- Suggest HPO (Human Phenotype Ontology) terms for each phenotype

### 4. Genetic/Molecular Information

- **Causal Genes**: Gene mutations or chromosomal abnormalities responsible for disease (gene symbols, OMIM IDs)
  > **Search first:** OMIM, ClinVar, HGMD, Ensembl, NCBI Gene
- **Pathogenic Variants**:
  - Affected genes (gene symbols, HGNC IDs)
    > **Search first:** OMIM, NCBI Gene, Ensembl, HGNC, UniProt, GeneCards
  - Variant classification (pathogenic, likely pathogenic, VUS per ACMG/AMP guidelines)
    > **Search first:** ClinVar, ClinGen, ACMG/AMP guidelines, VarSome
  - Variant type/class (missense, frameshift, nonsense, splice-site, structural)
  - Allele frequency in population databases
    > **Search first:** gnomAD, 1000 Genomes, ExAC, TOPMed, dbSNP
  - Somatic vs germline origin
    > **Search first:** COSMIC (somatic), ClinVar, ICGC, TCGA
  - Functional consequences (loss of function, gain of function, dominant negative)
- **Modifier Genes**: Genes that modify disease severity or expression
- **Epigenetic Information**: DNA methylation, histone modifications, chromatin changes affecting disease
  > **Search first:** ENCODE, Roadmap Epigenomics, MethBase, DiseaseMeth
- **Chromosomal Abnormalities**: Large-scale genetic changes (aneuploidy, translocations, inversions)
  > **Search first:** DECIPHER, ClinVar, ECARUCA, UCSC Genome Browser

### 5. Environmental Information

- **Environmental Factors**: Non-genetic contributing factors (toxins, radiation, pollution, occupational exposure)
  > **Search first:** CTD (Comparative Toxicogenomics Database), TOXNET, PubMed, EPA databases
- **Lifestyle Factors**: Behavioral factors (smoking, diet, exercise, alcohol consumption)
  > **Search first:** CDC databases, WHO, PubMed, NHANES
- **Infectious Agents**: If applicable, pathogens causing or triggering disease (bacteria, viruses, fungi, parasites)
  > **Search first:** NCBI Taxonomy, ViPR, BV-BRC, MicrobeDB, GIDEON

### 6. Mechanism / Pathophysiology

- **Molecular Pathways**: Specific signaling cascades or biochemical pathways involved (Wnt, MAPK, mTOR, PI3K-AKT, etc.)
  > **Search first:** KEGG, Reactome, WikiPathways, PathBank, BioCyc
- **Cellular Processes**: Cell-level mechanisms (apoptosis, autophagy, cell cycle dysregulation, inflammation, etc.)
  > **Search first:** Gene Ontology (GO), Reactome, KEGG, PubMed
- **Protein Dysfunction**: How protein structure or function is altered (misfolding, aggregation, loss of function, gain of function)
  > **Search first:** UniProt, PDB (Protein Data Bank), InterPro, Pfam, AlphaFold
- **Metabolic Changes**: Alterations in metabolic processes (energy metabolism, lipid metabolism, amino acid metabolism)
  > **Search first:** KEGG, BioCyc, HMDB (Human Metabolome Database), BRENDA
- **Immune System Involvement**: Role of immune response (autoimmunity, immunodeficiency, chronic inflammation)
  > **Search first:** ImmPort, Immunome Database, IEDB, Gene Ontology
- **Tissue Damage Mechanisms**: How tissues/ are injured (oxidative stress, ischemia, fibrosis, necrosis)
  > **Search first:** PubMed, Gene Ontology, Reactome
- **Biochemical Abnormalities**: Specific molecular defects (enzyme deficiencies, receptor dysfunction, ion channel defects)
  > **Search first:** BRENDA, UniProt, KEGG, OMIM, PubMed
- **Epigenetic Changes**: DNA methylation, histone modifications affecting gene expression in disease
  > **Search first:** ENCODE, Roadmap Epigenomics, MethBase, DiseaseMeth
- **Molecular Profiling** (if available):
  - Transcriptomics/gene expression changes
    > **Search first:** GEO (Gene Expression Omnibus), ArrayExpress, GTEx, Human Cell Atlas, SRA
  - Proteomics findings
    > **Search first:** PRIDE, ProteomeXchange, Human Protein Atlas, STRING, BioGRID
  - Metabolomics signatures
    > **Search first:** MetaboLights, Metabolomics Workbench, HMDB, METLIN
  - Lipidomics alterations
    > **Search first:** LIPID MAPS, SwissLipids, LipidHome, Metabolomics Workbench
  - Genomic structural features
    > **Search first:** UCSC Genome Browser, Ensembl, NCBI, dbVar, DGV
- **Advanced Technologies** (if applicable):
  - Single-cell analysis findings (cell-type specific mechanisms, cellular heterogeneity)
    > **Search first:** Human Cell Atlas, Single Cell Portal, GEO, CELLxGENE
  - Spatial transcriptomics findings
    > **Search first:** GEO, Spatial Research, Vizgen, 10x Genomics data
  - Multi-omics integration results
    > **Search first:** TCGA, ICGC, cBioPortal, LinkedOmics, PubMed
  - Functional genomics screens (CRISPR, RNAi)
    > **Search first:** DepMap, GenomeRNAi, PubMed, BioGRID ORCS

For each mechanism, describe:
- The causal chain from initial trigger to clinical manifestation
- Which mechanisms are upstream vs downstream
- What cell types and biological processes are involved
- Suggest GO terms for biological processes and CL terms for cell types

### 7. Anatomical Structures Affected

- **Organ Level**:
  - Primary organs directly affected
  - Secondary organ involvement (complications, secondary effects)
  - Body systems involved (cardiovascular, nervous, digestive, respiratory, endocrine, etc.)
  > **Search first:** Uberon, FMA (Foundational Model of Anatomy), OMIM, HPO, ICD-11, MeSH, SNOMED CT
- **Tissue and Cell Level**:
  - Specific tissue types affected (epithelial, connective, muscle, nervous)
  - Specific cell populations targeted (with Cell Ontology terms)
  > **Search first:** Uberon, Human Protein Atlas, Cell Ontology, Human Cell Atlas, CellMarker, PanglaoDB
- **Subcellular Level**:
  - Cellular compartments involved (mitochondria, nucleus, ER, lysosomes) (with GO Cellular Component terms)
  > **Search first:** Gene Ontology (Cellular Component), UniProt, Human Protein Atlas
- **Localization**:
  - Specific anatomical sites (with UBERON terms)
    > **Search first:** FMA, Uberon, NeuroNames (for brain), SNOMED CT
  - Lateralization (unilateral, bilateral, asymmetric)
    > **Search first:** HPO, clinical literature, imaging databases

### 8. Temporal Development

- **Onset**:
  - Typical age of onset (congenital, pediatric, adult, geriatric)
  - Onset pattern (acute, subacute, chronic, insidious)
  > **Search first:** OMIM, Orphanet, HPO, PubMed
- **Progression**:
  - Disease stages (early, intermediate, advanced, end-stage)
    > **Search first:** Cancer Staging Manual (AJCC), WHO classifications, PubMed
  - Progression rate (rapid, slow, variable)
  - Disease course pattern (episodic, relapsing-remitting, progressive, stable)
  - Disease duration (self-limited, chronic lifelong)
  > **Search first:** Disease registries, longitudinal cohort databases, natural history studies, PubMed, Orphanet, OMIM
- **Patterns**:
  - Remission patterns (spontaneous, treatment-induced)
    > **Search first:** Clinical trial databases, disease registries, PubMed
  - Critical periods (time windows of vulnerability or opportunity for intervention)
    > **Search first:** PubMed, developmental biology databases, clinical guidelines

### 9. Inheritance and Population

- **Epidemiology**:
  - Prevalence (cases per 100,000 at given time)
  - Incidence (new cases per 100,000 per year)
  > **Search first:** Orphanet, CDC, WHO, GBD (Global Burden of Disease), national registries, SEER, disease registries
- **For Genetic Etiology**:
  - Inheritance pattern (AD, AR, X-linked, mitochondrial, multifactorial, polygenic)
    > **Search first:** OMIM, Orphanet, ClinVar, GTR (Genetic Testing Registry)
  - Penetrance (complete, incomplete, age-dependent)
    > **Search first:** ClinVar, OMIM, PubMed, ClinGen
  - Expressivity (variable, consistent)
    > **Search first:** OMIM, ClinVar, PubMed
  - Genetic anticipation (increasing severity in successive generations)
    > **Search first:** OMIM, PubMed (especially for repeat expansion disorders)
  - Germline mosaicism
    > **Search first:** ClinVar, OMIM, genetic counseling literature, PubMed
  - Founder effects (population-specific mutations)
    > **Search first:** gnomAD, population genetics databases, PubMed
  - Consanguinity role
    > **Search first:** OMIM, population studies, genetic counseling resources
  - Carrier frequency
    > **Search first:** gnomAD, carrier screening databases, GeneReviews, GTR
- **Population Demographics**:
  - Affected populations (ethnic or demographic groups with higher prevalence)
    > **Search first:** gnomAD, 1000 Genomes, PAGE Study, PubMed, population registries
  - Geographic distribution (endemic areas, regional variation)
    > **Search first:** WHO, CDC, GBD, Orphanet, geographic epidemiology databases
  - Geographic distribution of specific variants
  - Sex ratio (male:female)
    > **Search first:** Disease registries, OMIM, PubMed, epidemiological databases
  - Age distribution of affected individuals
    > **Search first:** CDC, disease registries, SEER, Orphanet

### 10. Diagnostics

- **Clinical Tests**:
  - Laboratory tests (blood, urine, tissue chemistry, specific enzyme assays)
    > **Search first:** LOINC, LabTests Online, PubMed
  - Biomarkers (proteins, metabolites, genetic markers, circulating biomarkers)
    > **Search first:** FDA Biomarker List, BEST (Biomarkers, EndpointS, and other Tools), PubMed
  - Imaging studies (X-ray, CT, MRI, PET, ultrasound)
    > **Search first:** RadLex, DICOM, Radiopaedia, imaging databases
  - Functional tests (pulmonary function, cardiac stress tests)
    > **Search first:** LOINC, clinical guidelines, PubMed
  - Electrophysiology (EEG, EMG, ECG, nerve conduction studies)
    > **Search first:** LOINC, clinical neurophysiology databases, PubMed
  - Biopsy findings (histopathology, immunohistochemistry)
    > **Search first:** SNOMED CT, College of American Pathologists resources, PubMed
  - Pathology findings (microscopic examination)
    > **Search first:** SNOMED CT, Digital Pathology databases, PubMed
- **Genetic Testing**:
  > **Search first:** GTR (Genetic Testing Registry), GeneReviews, ClinGen
  - Overview of recommended genetic testing approach
  - Whole genome sequencing (WGS) utility
    > **Search first:** GTR, ClinVar, GEL (Genomics England), gnomAD
  - Whole exome sequencing (WES) utility
    > **Search first:** GTR, ClinVar, OMIM, GeneMatcher
  - Gene panels (which panels, which genes)
    > **Search first:** GTR, ClinVar, laboratory-specific databases
  - Single gene testing
    > **Search first:** GTR, ClinVar, OMIM, GeneReviews
  - Chromosomal microarray (CMA)
    > **Search first:** DECIPHER, ClinVar, dbVar, ECARUCA
  - Karyotyping
    > **Search first:** Chromosome Abnormality Database, ClinVar, cytogenetics resources
  - FISH
    > **Search first:** ClinVar, cytogenetics databases, PubMed
  - Mitochondrial DNA testing
    > **Search first:** MITOMAP, MSeqDR, ClinVar, GTR
  - Repeat expansion testing
    > **Search first:** GTR, ClinVar, repeat expansion databases, PubMed
- **Omics-Based Diagnostics** (if applicable):
  - RNA sequencing / transcriptomics
    > **Search first:** GEO, ArrayExpress, GTEx, RNA-seq databases
  - Proteomics
    > **Search first:** PRIDE, ProteomeXchange, FDA Biomarker database
  - Metabolomics
    > **Search first:** MetaboLights, Metabolomics Workbench, HMDB
  - Epigenomics
    > **Search first:** GEO, ENCODE, Roadmap Epigenomics, MethBase
  - Liquid biopsy
    > **Search first:** COSMIC, ClinVar, liquid biopsy databases, PubMed
- **Clinical Criteria**:
  - Standardized diagnostic criteria (DSM, ICD, society guidelines)
    > **Search first:** DSM-5, ICD-11, clinical society guidelines, UpToDate
  - Differential diagnosis (other conditions to rule out, with distinguishing features)
    > **Search first:** DynaMed, UpToDate, clinical decision support systems
- **Screening**:
  - Screening methods for asymptomatic individuals (newborn screening, carrier screening, cascade screening)
    > **Search first:** ACMG recommendations, CDC newborn screening, GTR

### 11. Outcome/Prognosis

- **Survival and Mortality**:
  - Survival rate (5-year, 10-year, overall)
    > **Search first:** SEER, cancer registries, disease-specific registries, PubMed
  - Life expectancy (with and without treatment if applicable)
    > **Search first:** Orphanet, disease registries, actuarial databases, PubMed
  - Mortality rate
    > **Search first:** CDC, WHO, GBD, national mortality databases
  - Disease-specific mortality (deaths directly attributable to disease)
    > **Search first:** Disease registries, CDC Wonder, GBD, PubMed
- **Morbidity and Function**:
  - Morbidity (disease-related disability and health impacts)
    > **Search first:** GBD, WHO, disability databases, PubMed
  - Disability outcomes (long-term functional impairments)
    > **Search first:** ICF (International Classification of Functioning), disability registries
  - Quality of life measures (EQ-5D, SF-36, PROMIS, disease-specific tools)
    > **Search first:** EQ-5D database, SF-36, PROMIS, PubMed
- **Disease Course**:
  - Complications (secondary problems: infections, organ failure, etc.)
    > **Search first:** ICD codes, disease registries, clinical databases, PubMed
  - Recovery potential (likelihood and extent of recovery, with vs without treatment)
    > **Search first:** Natural history studies, rehabilitation databases, PubMed
- **Prediction**:
  - Prognostic factors (age, disease severity, biomarkers, treatment response)
    > **Search first:** Prognostic models databases, clinical calculators, PubMed
  - Prognostic biomarkers (molecular markers predicting disease course)
    > **Search first:** FDA Biomarker database, PubMed, cancer prognostic databases

### 12. Treatment

- **Pharmacotherapy**:
  - Pharmacological treatments (drug names, drug classes, mechanisms of action)
    > **Search first:** DrugBank, RxNorm, ATC classification, DailyMed, FDA databases
  - Pharmacogenomics (how genetic variants affect drug metabolism, efficacy, toxicity)
    > **Search first:** PharmGKB, CPIC (Clinical Pharmacogenetics), FDA Table of PGx Biomarkers
- **Advanced Therapeutics**:
  - Gene therapy (viral vectors, CRISPR, gene replacement, gene editing)
    > **Search first:** ClinicalTrials.gov, FDA gene therapy database, ASGCT resources
  - Cell therapy (stem cell transplant, CAR-T, cellular therapeutics)
    > **Search first:** ClinicalTrials.gov, FDA cell therapy database, FACT standards
  - RNA-based therapies (ASOs, siRNA, mRNA therapies)
    > **Search first:** ClinicalTrials.gov, FDA approvals, PubMed
  - Targeted therapies (treatments directed at specific molecular targets)
    > **Search first:** My Cancer Genome, OncoKB, ClinicalTrials.gov, FDA approvals
  - Immunotherapies (checkpoint inhibitors, monoclonal antibodies)
    > **Search first:** Cancer Immunotherapy Database, FDA approvals, ClinicalTrials.gov
- **Surgical and Interventional**:
  - Surgical interventions (types of surgery, timing, outcomes)
    > **Search first:** CPT codes, surgical registries, clinical guidelines, PubMed
- **Supportive and Rehabilitative**:
  - Supportive care (symptom management, pain control, nutrition)
    > **Search first:** Clinical guidelines, Cochrane Library, PubMed
  - Rehabilitation (physical therapy, occupational therapy, speech therapy)
    > **Search first:** Rehabilitation medicine databases, clinical guidelines, PubMed
- **Experimental**:
  - Experimental treatments in clinical trials (with NCT identifiers if available)
    > **Search first:** ClinicalTrials.gov, EU Clinical Trials Register, WHO ICTRP
- **Treatment Outcomes**:
  - Treatment response rates
    > **Search first:** Clinical trial databases, FDA reviews, systematic reviews, PubMed
  - Side effects and adverse events
    > **Search first:** FDA Adverse Event Reporting System (FAERS), MedWatch, PubMed
- **Treatment Strategy**:
  - Treatment algorithms (clinical pathways, decision trees)
    > **Search first:** Clinical practice guidelines, NCCN Guidelines, UpToDate
  - Combination therapies
    > **Search first:** ClinicalTrials.gov, treatment guidelines, PubMed
  - Personalized medicine approaches (genotype-guided treatment)
    > **Search first:** My Cancer Genome, CIViC, PharmGKB, precision medicine databases

For each treatment, suggest MAXO (Medical Action Ontology) terms where applicable.

### 13. Prevention

- **Prevention Levels**:
  - Primary prevention (preventing disease occurrence: vaccination, risk factor modification)
    > **Search first:** CDC, WHO, USPSTF recommendations, Cochrane Library
  - Secondary prevention (early detection and treatment: screening programs, early intervention)
    > **Search first:** USPSTF, CDC screening guidelines, WHO
  - Tertiary prevention (preventing complications in those with disease)
    > **Search first:** Clinical guidelines, disease management protocols, PubMed
- **Immunization**: Vaccine strategies (if applicable)
  > **Search first:** CDC vaccine schedules, WHO immunization, FDA vaccine database
- **Screening and Early Detection**:
  - Screening programs (population-based: newborn screening, cancer screening)
    > **Search first:** CDC screening programs, USPSTF, cancer screening databases
  - Genetic screening (carrier screening, preimplantation genetic diagnosis, prenatal testing)
    > **Search first:** ACMG recommendations, ACOG guidelines, GTR
  - Risk stratification (identifying high-risk individuals for targeted prevention)
    > **Search first:** Risk prediction models, clinical calculators, PubMed
- **Behavioral Interventions**: Lifestyle modifications to reduce risk
  > **Search first:** CDC, WHO, behavioral intervention databases, Cochrane Library
- **Counseling**: Genetic counseling (risk assessment, family planning guidance)
  > **Search first:** NSGC resources, ACMG guidelines, GeneReviews
- **Public Health**:
  - Public health interventions (sanitation, vector control, health education)
    > **Search first:** CDC, WHO, public health databases, PubMed
  - Environmental interventions (reducing environmental risk factors)
    > **Search first:** EPA databases, WHO environmental health, PubMed
- **Prophylaxis**: Preventive medications or procedures
  > **Search first:** Clinical guidelines, FDA approvals, PubMed

### 14. Other Species / Natural Disease

- **Taxonomy**: Species affected (with NCBI Taxon identifiers)
  > **Search first:** NCBI Taxonomy
- **Breed**: Specific breeds affected (with VBO identifiers if applicable)
  > **Search first:** VBO (Vertebrate Breed Ontology)
- **Gene**: Orthologous genes in other species (with NCBI Gene IDs)
  > **Search first:** NCBI Gene
- **Natural Disease**:
  - Naturally occurring disease in other species (companion animals, wildlife)
    > **Search first:** OMIA (Online Mendelian Inheritance in Animals), VetCompass, PubMed
  - Veterinary relevance and importance in animal health
    > **Search first:** OMIA, veterinary databases, PubMed
- **Comparative Biology**:
  - Comparative pathology (similarities and differences across species)
    > **Search first:** OMIA, comparative pathology databases, PubMed
  - Evolutionary conservation of disease mechanisms
    > **Search first:** HomoloGene, OrthoMCL, Alliance of Genome Resources
- **Transmission** (if applicable):
  - Zoonotic potential
    > **Search first:** CDC zoonotic diseases, WHO zoonoses, GIDEON
  - Cross-species susceptibility
    > **Search first:** NCBI Taxonomy, veterinary databases, PubMed

### 15. Model Organisms

- **Model Types**:
  - Model organism type (mammalian, invertebrate, cellular, in vitro)
    > **Search first:** Alliance of Genome Resources, model organism databases
  - Specific model systems (mouse, rat, zebrafish, Drosophila, C. elegans, yeast, cell lines, organoids, iPSCs)
    > **Search first:** MGI, RGD, ZFIN, FlyBase, WormBase, SGD, ATCC, Cellosaurus
  - Induced models (drug treatment, surgical intervention, environmental manipulation)
    > **Search first:** MGI, model organism databases, PubMed
- **Genetic Models**:
  - Types available (knockout, knock-in, transgenic, conditional, humanized)
    > **Search first:** MGI, IMPC, KOMP, EuMMCR, IMSR
- **Model Characteristics**:
  - Phenotype recapitulation (how well model reproduces human disease features)
    > **Search first:** Model organism databases, comparative studies, PubMed
  - Model limitations (aspects of human disease not captured)
    > **Search first:** Model organism databases, PubMed, review articles
- **Applications**:
  - Research applications (what aspects of disease can be studied)
    > **Search first:** Model organism databases, PubMed
- **Resources**:
  - Model databases
    > **Search first:** MGI, RGD, ZFIN, FlyBase, WormBase, IMSR, EMMA, MMRRC

---

## Citation Requirements

- Cite primary literature (PMID preferred) for all mechanistic and clinical claims
- Prioritize recent reviews and landmark papers
- Include direct quotes from abstracts where possible to support key statements
- Distinguish evidence source types: human clinical, model organism, in vitro, computational

## Output Format

Structure your response as a comprehensive narrative organized by the sections above.
For each section, provide:
- Factual content with specific details (numbers, percentages, gene names, variant nomenclature)
- Ontology term suggestions (HPO, GO, CL, UBERON, CHEBI, MAXO, MONDO) where applicable
- Evidence citations with PMIDs
- Direct quotes from abstracts to support key claims
- Clear indication when information is not available or not applicable for this disease

This report will be used to populate a disease knowledge base entry with:
- Pathophysiology descriptions with causal chains
- Gene/protein annotations (HGNC, GO terms)
- Phenotype associations (HP terms) with frequencies
- Cell type involvement (CL terms)
- Anatomical locations (UBERON terms)
- Chemical entities (CHEBI terms)
- Treatment annotations (MAXO terms)
- Evidence items with PMIDs and exact abstract quotes
- Epidemiology, prognosis, diagnostic, and prevention information
- Animal model descriptions with phenotype recapitulation details


## Output

I now have verified PMIDs, exact abstract quotes, and confirmed ontology identifiers. Writing the complete report.

---

# Comprehensive Research Report: ER-Positive Breast Cancer

**Prepared:** 2026-07-10 · For dismech knowledge-base curation

> **Attribution:** Landmark clinical and molecular claims below are drawn from articles retrieved via **PubMed**; DOI links are provided inline for each PubMed-sourced reference, per PubMed's terms of use. Where I rely on established domain knowledge rather than a specific retrieved abstract, this is noted or cited to the canonical primary source.

> **Scope note / curation caveat:** "ER-positive breast cancer" (ER+ BC) is a *molecular-subclass* entity defined by a biomarker (estrogen receptor expression), not a distinct Mendelian disorder. It is highly heterogeneous and overlaps the luminal A/B intrinsic subtypes. Treat it as a **disease subtype entry** whose pathophysiology centers on estrogen-receptor (ER/ESR1) signaling dependence and endocrine-therapy response/resistance. Many template fields designed for monogenic disorders (penetrance, anticipation, germline mosaicism, model-organism knockouts of a single causal gene) are **not applicable** and are marked as such.

---

## 1. Disease Information

**Overview.** ER-positive breast cancer is invasive (or in situ) breast carcinoma in which tumor cell nuclei express the estrogen receptor alpha (ERα, encoded by *ESR1*), detected by immunohistochemistry (IHC). By ASCO/CAP 2020 guidance, a tumor is scored ER-positive when **≥1% of tumor nuclei stain**, with 1–10% designated "ER-low-positive." ER positivity indicates that tumor growth is at least partly driven by estrogen–ERα signaling and predicts benefit from endocrine (anti-estrogen) therapy. ER+ disease is the **largest breast-cancer subgroup — roughly 70–80% of all invasive breast cancers** — and most ER+ tumors are also progesterone-receptor (PR)-positive and HER2-negative (the "HR+/HER2−" clinical class), corresponding largely to the **luminal A** and **luminal B** intrinsic molecular subtypes (Perou/Sørlie classification; TCGA, PMID:23000897, [DOI](https://doi.org/10.1038/nature11412)).

**Key identifiers (verified via OLS):**
- **MONDO:** `MONDO:0006512` — *estrogen-receptor positive breast cancer* (primary). Related: `MONDO:0700079` (hormone receptor-positive breast cancer), `MONDO:0021116` (luminal A breast carcinoma), `MONDO:0021115` (luminal B breast carcinoma), `MONDO:0700078` (triple-positive breast carcinoma).
- **DOID:** `DOID:0060075` (estrogen-receptor positive breast cancer); `DOID:0070780` (HR+/HER2− breast cancer).
- **ICD-10:** C50.- (malignant neoplasm of breast); ER status captured separately by Z17.0 (estrogen receptor positive status). **ICD-11:** 2C6- (carcinoma of breast) with molecular-marker extension codes.
- **ICD-O-3 morphology:** most commonly 8500/3 (infiltrating duct carcinoma, NST) and 8520/3 (lobular carcinoma).
- **NCIT:** C53554 (Luminal A), C53555 (Luminal B); estrogen-receptor-positive breast carcinoma is coded in NCIT under the ER-positive neoplasm hierarchy.
- **MeSH:** D001943 (Breast Neoplasms) + "Receptors, Estrogen" (D011960); "Neoplasms, Hormone-Dependent" (D009376).
- **OMIM:** 114480 (Breast cancer, susceptibility) — a phenotype series, not subtype-specific.
- **Orphanet:** breast cancer is generally common (not a rare disease); rare hereditary breast-cancer syndromes carry separate ORPHA codes.

**Synonyms / alternative names:** ER+ breast cancer; estrogen receptor-positive breast carcinoma; hormone receptor-positive breast cancer (when grouped with PR); hormone-dependent / hormone-responsive breast cancer; luminal breast cancer (approximate molecular equivalent); HR+/HER2− breast cancer (clinical usage).

**Data derivation.** Disease-level aggregate resource (registries: SEER, national cancer registries; molecular atlases: TCGA, METABRIC). Individual-patient EHR data exist but the canonical characterization is aggregate.

---

## 2. Etiology

**Primary causal factors.** ER+ breast cancer is a **multifactorial somatic disease** driven by lifetime cumulative estrogen exposure acting on mammary luminal epithelial cells that acquire somatic driver mutations. There is no single causal agent. The dominant mechanistic theme is **estrogen-driven proliferation of ERα-expressing luminal cells**, on which oncogenic lesions (most commonly *PIK3CA*, *GATA3*, *TP53*, *MAP3K1*, *CDH1*, *ESR1* amplification) are superimposed (TCGA, PMID:23000897, [DOI](https://doi.org/10.1038/nature11412) — *"Somatic mutations in only three genes (TP53, PIK3CA and GATA3) occurred at >10% incidence… enrichment of specific mutations in GATA3, PIK3CA and MAP3K1 with the luminal A subtype"*).

**Risk factors — reproductive/hormonal (the ER+-specific axis):**
- **Early menarche, late menopause** → longer cumulative ovarian estrogen exposure.
- **Nulliparity / late first full-term pregnancy** (>30 y).
- **Menopausal hormone therapy (MHT)**, especially combined estrogen–progestin (Women's Health Initiative; PMID:12117397 — combined MHT increases invasive breast cancer risk).
- **Obesity in postmenopausal women** — adipose aromatase raises circulating/local estrogen; specifically elevates ER+ risk. (Premenopausal obesity is paradoxically weakly protective.)
- **Alcohol consumption** — dose-dependent increase, most consistent for ER+ disease.
- **Higher endogenous estrogen/androgen levels** (EPIC, Endogenous Hormones and Breast Cancer Collaborative Group; PMID:12189224).
- **Increased mammographic breast density.**

**Genetic risk factors:**
- **High-penetrance germline:** *BRCA2* pathogenic variants predispose predominantly to **ER+** breast cancer (contrast: *BRCA1* → mostly triple-negative). Also *PALB2*, *ATM*, *CHEK2* — the latter two enrich for ER+ disease. *CDH1* (lobular), *TP53* (Li-Fraumeni), *PTEN*.
- **Polygenic susceptibility:** >180 common low-penetrance loci from GWAS; a substantial subset are **subtype-specific for ER+ disease** (e.g., *FGFR2*, *TOX3/TNRC9*, *MAP3K1*, *ESR1* locus, *CCND1*, *8q24*). Breast Cancer Association Consortium (BCAC) GWAS (PMID:29059683). Polygenic risk scores (PRS) predict ER+ risk more strongly than ER− risk.

**Protective factors:**
- **Parity and breastfeeding** (each reduces risk; breastfeeding disproportionately protects against ER−, but parity protects against ER+ long-term).
- **Physical activity**; **maintaining healthy postmenopausal body weight**.
- **Chemoprevention with SERMs/AIs** in high-risk women reduces ER+ incidence specifically (tamoxifen, raloxifene — NSABP P-1/STAR; exemestane — MAP.3; anastrozole — IBIS-II).
- **Genetic protective alleles:** protective (risk-reducing) alleles at the same GWAS loci; no single strong Mendelian protective variant.

**Gene–environment interactions.** PRS × hormonal exposure is broadly multiplicative; MHT and obesity amplify absolute risk most in women with high genetic risk. *CYP19A1* (aromatase) and estrogen-metabolism gene variants modulate the estrogen-exposure effect. (CTD/PheGenI/GWAS Catalog.)

---

## 3. Phenotypes

ER+ breast cancer's "phenotype" is a combination of **clinical/pathological tumor features**, **laboratory/biomarker abnormalities**, and **symptoms/signs of local and metastatic disease**.

**Pathological & molecular phenotype (defining):**
- **Estrogen receptor positivity by IHC** (≥1% nuclei). Suggested HPO: `HP:0020325` *Increased breast-tissue estrogen receptor expression*. Frequency: 100% (definitional).
- Frequently PR-positive and HER2-negative; typically **lower histologic grade**, lower Ki-67 proliferation index (especially luminal A), and **hormone-dependent (well-differentiated luminal)** morphology.
- **Histology:** invasive ductal (NST) most common; **invasive lobular carcinoma is strongly enriched (~95% ER+)**, associated with *CDH1* (E-cadherin) loss.

**Clinical symptoms/signs (shared with breast cancer generally; HPO terms):**
- **Breast mass / lump** — `HP:0031093` (Breast mass). Most common presenting sign; frequency very frequent.
- **Breast neoplasm** — `HP:0100013`.
- **Nipple discharge / retraction, skin dimpling (peau d'orange), axillary lymphadenopathy** — `HP:0002716` (Lymphadenopathy).
- **Metastatic phenotypes** (ER+ has a characteristic **bone-predominant** tropism): bone pain and pathological fracture — `HP:0002659`/`HP:0002754`; hepatic metastasis; pulmonary metastasis; and, notably for ER+/lobular, serosal/GI/leptomeningeal spread.

**Phenotype characteristics:**
- **Age of onset:** predominantly **adult / postmenopausal**; median age at diagnosis ~62–63 y; ER+ proportion rises with age.
- **Severity/course:** variable. Luminal A → indolent, favorable; luminal B → more proliferative, higher recurrence. Distinctive feature: **prolonged risk of late recurrence** — ER+ tumors recur at a roughly constant rate for **>20 years** after diagnosis (EBCTCG, PMID:29860917 context; Pan et al., NEJM 2017, PMID:29131280).
- **Progression:** typically slow-to-intermediate; often **relapsing over a long horizon** rather than early aggressive relapse.

**Quality-of-life impact.** Long-term endocrine therapy (5–10 y) causes menopausal symptoms (hot flashes, arthralgia, sexual dysfunction, bone loss) materially affecting QoL and adherence; QoL measured with EORTC QLQ-C30/BR23, FACT-B, EQ-5D.

---

## 4. Genetic / Molecular Information

ER+ breast cancer is a **somatic (acquired) genomic disease**; germline variants contribute susceptibility (Section 2) but the tumors are defined by somatic drivers.

**Central gene — *ESR1* (ERα):**
- **HGNC:3467**, gene symbol *ESR1*, chromosome 6q25.1; OMIM 133430; UniProt P03372.
- ERα is the therapeutic target and dependency. Suggested GO: `GO:0030520` (intracellular estrogen receptor signaling pathway); molecular function `GO:0030284` (nuclear estrogen receptor activity).
- **Somatic *ESR1* alterations** are largely a **resistance** phenomenon: *ESR1* **ligand-binding-domain missense mutations** (hotspots **Y537S, Y537N, Y537C, D538G**, also E380Q, L536) produce **constitutive, ligand-independent ER activation** and confer resistance to estrogen deprivation (aromatase inhibitors). These are **rare in primary tumors (<1–3%) but present in ~20–40% of AI-pretreated metastatic tumors** (Jeselsohn et al.; review PMID:34392831, [DOI](https://doi.org/10.1186/s13058-021-01462-3) — *"ESR1 mutations are a common cause of acquired resistance to the backbone of therapy, estrogen deprivation by aromatase inhibition"*). ***ESR1* gene fusions and amplification** also occur.

**Most frequent somatic driver mutations in ER+/luminal disease** (TCGA, PMID:23000897, [DOI](https://doi.org/10.1038/nature11412); METABRIC):
- ***PIK3CA*** (HGNC:8975; ~**40%** of HR+ tumors) — activating hotspots E542K, E545K, H1047R → PI3K–AKT–mTOR activation. Actionable (alpelisib).
- ***GATA3*** (HGNC:4172) — luminal-lineage transcription factor; enriched in luminal A.
- ***MAP3K1*** and ***MAP2K4*** — MAPK pathway; enriched luminal A.
- ***CDH1*** (HGNC:1748) — E-cadherin loss defining **invasive lobular carcinoma**.
- ***TP53*** — more frequent in luminal B / higher grade.
- ***AKT1*** (E17K), ***PTEN*** loss, ***NF1***, ***RB1*** loss (associated with CDK4/6-inhibitor resistance), ***CCND1*** amplification (11q13), ***FGFR1*** amplification (8p11), ***MYC*** amplification.
- ***MAP3K1/GATA3/PIK3CA*** define the "luminal" driver landscape.

**Variant classification / origin.** Driver events are **somatic**; classification per AMP/ASCO/CAP oncology tiers (Tier I actionable: *PIK3CA*, *ESR1*, *AKT1/PTEN*, *ERBB2* mutations, *BRCA1/2*). Germline *BRCA2/PALB2/ATM/CHEK2* per ACMG. Somatic frequencies documented in **COSMIC, cBioPortal (TCGA, METABRIC), ICGC**.

**Modifier genes.** *RB1* status and *CCNE1* amplification modify CDK4/6-inhibitor response; *ESR1* mutation modifies endocrine response; *PIK3CA/AKT1/PTEN* modify PI3K/AKT-inhibitor benefit.

**Epigenetics.** ER+ tumors show characteristic DNA-methylation programs (TCGA CIMP-like luminal cluster); ER target-gene enhancer reprogramming, FOXA1-dependent pioneer chromatin remodeling, and methylation-mediated silencing (e.g., of *ESR1* itself in a minority → ER-loss/resistance). Histone modifications and enhancer hijacking underpin acquired endocrine resistance.

**Chromosomal features.** Recurrent CNAs: 1q gain, 16q loss (hallmark of low-grade luminal / lobular), 8q24 (*MYC*) gain, 11q13 (*CCND1*) amplification, 8p11 (*FGFR1*) amplification. Luminal A is relatively genomically quiet; luminal B is more aneuploid.

---

## 5. Environmental Information

- **Endocrine-disrupting / hormonal exposures:** exogenous estrogens (combined MHT), and debated roles for environmental xenoestrogens.
- **Alcohol** (dose-dependent, ER+-specific signal), **postmenopausal obesity/adiposity** (aromatase-driven local estrogen), **physical inactivity**, **Western/high-caloric diet**.
- **Ionizing radiation** (therapeutic chest RT in youth, e.g., Hodgkin lymphoma; atomic-bomb survivor data) increases overall breast-cancer risk.
- **Infectious agents:** **None established.** ER+ breast cancer is not an infectious/oncoviral disease (unlike some cancers). Not applicable.

---

## 6. Mechanism / Pathophysiology

**Core causal chain (upstream → downstream):**

1. **Estrogen (17β-estradiol; CHEBI:16469) binds ERα** in luminal mammary epithelial cells → receptor dimerization, nuclear translocation, binding to estrogen response elements (EREs). Pioneer factor **FOXA1** and cofactor **GATA3** license ER chromatin binding.
2. **ER-driven transcription** activates proliferation and survival genes — **CCND1 (cyclin D1)**, MYC, *TFF1/pS2*, *GREB1*, *PGR* (progesterone receptor, itself an ER target — hence PR positivity is a marker of intact ER signaling).
3. **Cyclin D1–CDK4/6 activation → RB phosphorylation → E2F release → G1/S cell-cycle progression.** This is the proliferative engine and the rationale for **CDK4/6 inhibitors** (palbociclib, ribociclib, abemaciclib).
4. **Cross-talk with growth-factor/PI3K–AKT–mTOR and MAPK pathways** amplifies and can bypass ER signaling; *PIK3CA*/*AKT1* activation and *PTEN* loss drive both proliferation and endocrine resistance.
5. **Clinical manifestation:** clonal expansion → invasive carcinoma → lymphatic/hematogenous dissemination (bone-tropic).

**Molecular pathways (KEGG/Reactome):** Estrogen signaling (KEGG hsa04915; Reactome "ESR-mediated signaling" R-HSA-8939211); PI3K–AKT (hsa04151); cell cycle (hsa04110); MAPK (hsa04010); mTOR.

**Cellular processes (GO):** `GO:0030520` (intracellular estrogen receptor signaling pathway); `GO:0008283` (cell population proliferation); `GO:0000082` (G1/S transition of mitotic cell cycle); `GO:0043066` (negative regulation of apoptosis). Cell type of origin (CL): **luminal epithelial cell of mammary gland** — `CL:0002326`; broadly `CL:0000066` (epithelial cell).

**Protein dysfunction.** ERα gain-of-function via LBD mutation (constitutive activity independent of ligand). PI3Kα (p110α) hyperactivation. Cyclin D1 overexpression. RB1 loss (loss of function). E-cadherin (CDH1) loss → discohesive lobular growth.

**Metabolic changes.** ER+ tumors are relatively less glycolytic than basal tumors; estrogen regulates lipid and glucose metabolism; endocrine resistance can involve metabolic reprogramming and lipid-metabolism/cholesterol (27-hydroxycholesterol as an endogenous SERM) contributions.

**Immune involvement.** ER+ (luminal) tumors are typically **"immune cold"** — low tumor-infiltrating lymphocytes and low PD-L1 relative to TNBC — explaining limited single-agent immunotherapy benefit in most HR+ disease.

**Molecular profiling.** Transcriptomic signatures define prognosis and chemo-benefit: **PAM50** (luminal A vs B, ROR score), **Oncotype DX 21-gene Recurrence Score**, **MammaPrint 70-gene**, **EndoPredict**, **Breast Cancer Index**. Proteomic (RPPA in TCGA), and single-cell/spatial studies reveal luminal-hormone-sensing vs luminal-progenitor cell states and microenvironmental heterogeneity.

**Suggested GO/CL summary for KB:** biological processes `GO:0030520`, `GO:0000082`, `GO:0008283`; cell type `CL:0002326` (luminal epithelial cell of mammary gland).

---

## 7. Anatomical Structures Affected

- **Primary organ:** **breast / mammary gland** — UBERON:0000310 (breast); UBERON:0001911 (mammary gland). Ductal-lobular epithelium — UBERON:0002518 (mammary duct region).
- **Tissue/cell level:** mammary **luminal epithelium** (glandular epithelial cells lining ducts/lobules). CL:0002326 (luminal epithelial cell of mammary gland).
- **Regional spread:** axillary lymph nodes — UBERON:0002439 (axillary lymph node).
- **Metastatic sites (organ-tropism, characteristic for ER+):** **bone** (UBERON:0002481; most common ER+ metastatic site), **liver** (UBERON:0002107), **lung** (UBERON:0002048), and less commonly brain; ER+ **lobular** carcinoma uniquely spreads to peritoneum/GI tract, ovary, and leptomeninges.
- **Subcellular (GO cellular component):** nucleus (`GO:0005634`) — site of ER transcriptional activity; also cytoplasm/plasma membrane (non-genomic ER signaling).
- **Lateralization:** unilateral typical; bilateral/contralateral risk elevated (metachronous), especially with germline predisposition and lobular histology.

---

## 8. Temporal Development

- **Onset:** adult; predominantly **peri-/postmenopausal**; insidious (asymptomatic screen-detected mass or symptomatic lump). Median diagnosis ~62 y.
- **Staging:** AJCC 8th edition **anatomic + prognostic** staging incorporates ER/PR/HER2 and grade (ER positivity down-stages prognostic group). Stages 0 (DCIS)/I–IV.
- **Progression rate:** generally **slow (luminal A) to intermediate (luminal B)**.
- **Course pattern:** the hallmark of ER+ disease is a **persistent, roughly constant late-recurrence hazard extending beyond 10–20 years** — distinct from ER− disease, whose recurrence risk peaks early (~2–3 y) then falls. This underpins **extended endocrine therapy** (up to 10 y). (Pan et al., NEJM 2017, PMID:29131280; EBCTCG analyses.)
- **Remission:** treatment-induced; early-stage ER+ is often curable, but micrometastatic dormancy explains late relapse.
- **Critical intervention windows:** adjuvant endocrine therapy years 0–10; ovarian suppression in high-risk premenopausal women; the window before acquired *ESR1*/PI3K resistance in the metastatic setting.

---

## 9. Inheritance and Population

**Epidemiology (According to PubMed — ACS Breast Cancer Statistics 2024, Giaquinto et al., PMID:39352042, [DOI](https://doi.org/10.3322/caac.21863)):**
- Breast cancer is the most common invasive cancer in women. US incidence rose **~1% annually 2012–2021, "largely confined to localized-stage and hormone receptor-positive disease"**, with a **steeper rise in women <50 (1.4%/y vs 0.7%/y)**.
- **Overall breast-cancer death rate fell 44% (1989–2022)**, ≈517,900 fewer deaths — reflecting screening and effective endocrine/systemic therapy.
- ER+ constitutes **~70–80%** of invasive breast cancers (rising proportion in older women).
- **Disparities:** *"Black women have 38% higher mortality than White women despite 5% lower incidence… Black women have the lowest survival for every breast cancer subtype and stage except localized disease."* Fastest incidence rise in Asian American/Pacific Islander women.

**Global:** breast cancer ~2.3 million new cases/year worldwide (GLOBOCAN 2020/2022, IARC); leading cause of cancer death in women globally.

**Inheritance.** ER+ breast cancer is **not Mendelian**; it is **multifactorial/polygenic** with a minority (~5–10%) attributable to high-penetrance germline predisposition (*BRCA2* > *BRCA1* for ER+, *PALB2*, *ATM*, *CHEK2*, *CDH1*, *TP53*, *PTEN*). Penetrance is age-dependent and gene/variant-specific (e.g., *BRCA2* ~45–55% lifetime breast-cancer risk). Founder effects: *BRCA1/2* Ashkenazi Jewish founder alleles (185delAG, 5382insC, 6174delT); Icelandic *BRCA2* 999del5. Anticipation/germline mosaicism: **not applicable** to this somatic subtype.

**Demographics.** **Sex ratio:** overwhelmingly female (~99%); **male breast cancer is disproportionately ER+ (>90%)**. Age distribution skews older; ER+ fraction increases with age.

---

## 10. Diagnostics

**Core pathological diagnosis:**
- **Biopsy + histopathology** (core-needle or excisional) with invasive carcinoma confirmation.
- **ER IHC** (nuclear staining, ≥1% positive = ER+; ASCO/CAP 2020) — the defining test. Companion **PR IHC** and **HER2 IHC/ISH**; **Ki-67** proliferation index (luminal A vs B surrogate). LOINC/SNOMED-coded pathology.
- **Grade** (Nottingham/Elston-Ellis).

**Biomarkers / molecular assays:**
- **Multigene prognostic/predictive assays:** Oncotype DX 21-gene Recurrence Score, MammaPrint 70-gene, PAM50/Prosigna ROR, EndoPredict, Breast Cancer Index (predicts extended-endocrine benefit).
- **Genomic testing** (metastatic): *PIK3CA* (tissue or ctDNA — companion diagnostic for alpelisib), *ESR1* mutation (ctDNA/liquid biopsy — companion for elacestrant), *AKT1/PTEN* (capivasertib), *BRCA1/2* germline (PARP inhibitors), *ERBB2* mutations, MSI/TMB, *NTRK*.
- **Liquid biopsy (ctDNA):** increasingly used to detect *ESR1*/*PIK3CA* mutations and monitor resistance (SERD selection).

**Imaging:** mammography (screening/diagnostic), breast ultrasound, breast MRI (high-risk/lobular). Staging: CT, bone scan, FDG-PET/CT (note ER+/lobular can be FDG-low); **FES-PET (18F-fluoroestradiol)** images ER expression functionally.

**Genetic testing.** Germline multigene panel (BRCA1/2, PALB2, ATM, CHEK2, CDH1, TP53, PTEN) per NCCN criteria; cascade testing of relatives. WES/WGS not routine clinically.

**Clinical criteria / differential.** Differential: benign breast disease (fibroadenoma, cyst), other subtypes (TNBC, HER2+), phyllodes, lymphoma; ER-low-positive tumors behave biologically more like ER− and warrant caution.

**Screening.** Population mammographic screening (USPSTF now recommends biennial screening starting age 40); high-risk MRI; genetic/carrier screening in familial cases.

---

## 11. Outcome / Prognosis

- **Prognosis is comparatively favorable** among breast-cancer subtypes; ER positivity is an independent favorable prognostic factor and a predictive marker of endocrine benefit. 5-year relative survival for **localized ER+/HR+ disease exceeds 90–99%**; regional ~86%; **distant/metastatic ~30% (5-yr)** but improving with CDK4/6 inhibitors.
- **Distinctive late-recurrence risk:** durable relapse hazard for >20 years (Pan et al., PMID:29131280) — cumulative distant recurrence continues even for node-negative disease.
- **Metastatic ER+ is treatable but generally incurable**; median overall survival in first-line endocrine + CDK4/6-inhibitor era now **~5+ years** for many patients (MONALEESA/PALOMA/MONARCH OS data).

**Prognostic factors:** tumor stage/nodal burden, grade, Ki-67/proliferation, PR status (PR-negativity worse), genomic risk score, luminal A vs B, and (metastatic) acquired *ESR1*/*PIK3CA*/*RB1* alterations. Predictive biomarkers: *PIK3CA*, *ESR1*, *AKT1/PTEN*, *BRCA1/2*, HER2-low status.

**Morbidity:** treatment-related (endocrine-therapy menopausal symptoms, arthralgia, osteoporosis, thromboembolism/endometrial risk with tamoxifen; CDK4/6-inhibitor neutropenia/diarrhea). Metastatic morbidity is bone-dominant (fractures, hypercalcemia, cord compression).

---

## 12. Treatment

ER+ breast cancer is the paradigm of **targeted endocrine therapy**. Suggested MAXO terms noted inline.

**A. Endocrine (anti-estrogen) therapy — backbone** (MAXO: pharmacotherapy; NCIT:C15986):
- **Selective estrogen receptor modulators (SERMs): tamoxifen** (CHEBI:41774) — pre- and postmenopausal; 5–10 y adjuvant. Extended 10-y tamoxifen (ATLAS/aTTom) reduces late recurrence.
- **Aromatase inhibitors (AIs): anastrozole, letrozole, exemestane** — postmenopausal (block peripheral estrogen synthesis; CYP19A1 target). Superior to tamoxifen in postmenopausal adjuvant (EBCTCG AI meta-analysis).
- **Ovarian function suppression (OFS): GnRH agonists (goserelin/leuprolide)** — high-risk premenopausal, combined with AI or tamoxifen (**SOFT/TEXT** trials established OFS + exemestane benefit in high-risk young women).
- **Selective estrogen receptor degraders (SERDs): fulvestrant** (injectable; CHEBI:31638) and the first **oral SERD, elacestrant** — FDA-approved Jan 2023 for **ESR1-mutant** HR+/HER2− metastatic BC after prior endocrine therapy (EMERALD trial; PMID:37314500, [DOI](https://doi.org/10.1007/s00280-023-04550-7) — *"the first orally bioavailable SERD approved by the FDA… whose tumors harbor an ESR1 missense mutation"*).

**B. Targeted agents added to endocrine therapy:**
- **CDK4/6 inhibitors — palbociclib, ribociclib, abemaciclib.** Standard first-line partner with AI/fulvestrant in metastatic HR+/HER2−; roughly double PFS and improve OS (MONALEESA, PALOMA, MONARCH). In **adjuvant** high-risk early disease, **abemaciclib** improved invasive disease-free survival (**monarchE**; PMID:32954927, [DOI](https://doi.org/10.1200/JCO.20.02514) — *"the first CDK4/6 inhibitor to demonstrate a significant improvement in IDFS… HR 0.75… 2-year IDFS 92.2% vs 88.7%"*); ribociclib (NATALEE) subsequently added a broader adjuvant indication.
- **PI3K inhibitor — alpelisib** (+ fulvestrant) for **PIK3CA-mutant** disease (**SOLAR-1**; PMID:31091374, [DOI](https://doi.org/10.1056/NEJMoa1813904) — PFS **11.0 vs 5.7 months, HR 0.65** in PIK3CA-mutated cohort; key toxicity hyperglycemia).
- **AKT inhibitor — capivasertib** (+ fulvestrant) after AI ± CDK4/6-inhibitor progression, benefit in overall and **AKT-pathway-altered (PIK3CA/AKT1/PTEN)** populations (**CAPItello-291**; PMID:37256976, [DOI](https://doi.org/10.1056/NEJMoa2214131) — PFS **7.3 vs 3.1 months, HR 0.50** in altered population).
- **mTOR inhibitor — everolimus** (+ exemestane) after AI resistance (BOLERO-2).
- **PARP inhibitors — olaparib, talazoparib** for **germline BRCA1/2-mutant** HR+ disease (OlympiA adjuvant; OlympiAD metastatic).

**C. Antibody–drug conjugates (later-line):**
- **Trastuzumab deruxtecan** for **HER2-low** (IHC 1+/2+ ISH−) HR+ metastatic disease (**DESTINY-Breast04**; PMID:35665782, [DOI](https://doi.org/10.1056/NEJMoa2203690) — HR+ cohort PFS **10.1 vs 5.4 months**, OS **23.9 vs 17.5 months**; watch interstitial lung disease).
- **Sacituzumab govitecan** (Trop-2 ADC) in endocrine-refractory HR+ metastatic disease (TROPiCS-02).

**D. Chemotherapy** — reserved for high genomic-risk early disease and endocrine-refractory/visceral-crisis metastatic disease. Genomic assays spare most low-risk patients: **TAILORx** (PMID:29860917, [DOI](https://doi.org/10.1056/NEJMoa1804710)) showed endocrine therapy **noninferior** to chemoendocrine therapy for node-negative, RS 11–25 (with some benefit in women ≤50, RS 16–25); **RxPONDER** (PMID:34914339, [DOI](https://doi.org/10.1056/NEJMoa2108873)) showed node-positive (1–3), RS ≤25 **postmenopausal women derive no chemo benefit, whereas premenopausal women do** (HR 0.60).

**E. Local therapy:** surgery (breast-conserving surgery or mastectomy; MAXO:0000004/NCIT surgical procedure) + sentinel/axillary node evaluation; **radiotherapy** (MAXO:0000014) as indicated.

**F. Supportive/preventive adjuncts:** bone-targeted agents (bisphosphonates/denosumab) for bone metastases and to reduce recurrence (adjuvant zoledronic acid in postmenopausal women, EBCTCG).

**Pharmacogenomics:** **CYP2D6** poor-metabolizer status reduces conversion of tamoxifen to active **endoxifen** (CPIC guidance; clinical impact debated). *PIK3CA*/*ESR1*/*BRCA* genotype-guided therapy selection is now standard (My Cancer Genome, OncoKB, CIViC).

---

## 13. Prevention

- **Primary prevention / chemoprevention (ER+-specific):** SERMs **tamoxifen, raloxifene** (NSABP P-1, STAR) and AIs **exemestane** (MAP.3), **anastrozole** (IBIS-II) reduce **ER+** breast-cancer incidence ~50–65% in high-risk women (USPSTF endorses risk-reducing medication for high-risk women). MAXO: pharmacotherapy / chemoprevention.
- **Risk-reducing surgery:** bilateral risk-reducing mastectomy and/or salpingo-oophorectomy in high-penetrance carriers (*BRCA1/2*, etc.); oophorectomy reduces estrogen exposure.
- **Lifestyle:** weight control, alcohol reduction, physical activity, limiting combined MHT.
- **Secondary prevention:** population **mammographic screening** (USPSTF biennial from 40), supplemental MRI in high-risk; risk stratification with models (Tyrer-Cuzick/IBIS, Gail, BOADICEA/CanRisk incorporating PRS).
- **Genetic counseling / cascade testing** for hereditary predisposition; PGD/prenatal options for high-penetrance syndromes.
- **Immunization / public-health / environmental interventions:** not applicable (non-infectious).

---

## 14. Other Species / Natural Disease

- **Taxonomy:** primary human disease — *Homo sapiens* (NCBITaxon:9606). Naturally occurring mammary carcinoma also in **domestic dog** (*Canis lupus familiaris*, NCBITaxon:9615), **domestic cat** (*Felis catus*, NCBITaxon:9685), and lab rodents.
- **Comparative/veterinary:** **Canine mammary tumors** are a leading canine neoplasm; a subset are **ER-positive and hormone-dependent** (ovariohysterectomy before first estrus is strongly protective), providing a spontaneous large-animal comparative model. **Feline mammary carcinoma** tends to be more aggressive and frequently **ER-negative/HER2-driven** (models aggressive human disease). (OMIA; comparative oncology literature.)
- **Evolutionary conservation:** *ESR1*/estrogen signaling and mammary developmental programs are conserved across mammals; orthologs — mouse *Esr1* (NCBI Gene 13982), rat *Esr1* (Gene 24890), dog *ESR1* (Gene 403640).
- **Transmission / zoonosis:** not applicable.

---

## 15. Model Organisms

- **Cell lines (in vitro; workhorses of ER+ research):** **MCF-7** (Cellosaurus CVCL_0031; ER+ luminal, estrogen-responsive), **T-47D** (CVCL_0553; ER+/PR+), **ZR-75-1** (CVCL_0588), **BT-474** (ER+/HER2+), and **CAMA-1**. Derivatives model endocrine resistance (long-term estrogen-deprived MCF-7, tamoxifen-resistant lines) and *ESR1*-mutant knock-in lines (Y537S, D538G).
- **Organoids / PDX:** patient-derived ER+ organoids and PDX models (though ER+ PDX engraftment is historically harder than TNBC); estrogen-supplementation-dependent PDXs. iPSC/3D models emerging.
- **Genetically engineered mouse models (GEMMs):** ER+ luminal tumorigenesis is harder to model than basal disease. Relevant models: **MMTV-PyMT** (luminal-like progression, though ER expression declines with progression), *Pik3ca^H1047R* conditional models, *Esr1*-driven and *Wnt1* models; hormone (estrogen-pellet)-dependent models. **Model limitation:** mouse mammary tumors poorly recapitulate the sustained ERα-dependence and estrogen-driven growth of human luminal disease — a recognized translational gap (relevant `HUMAN_MODEL_MISMATCH` framing for KB).
- **Induced models:** chemical carcinogen (DMBA/MNU) rat mammary carcinomas are classically **ER-positive and hormone-responsive** — historically important for endocrine-therapy and chemoprevention testing (e.g., tamoxifen, AIs). Rat (*Rattus norvegicus*) NMU model is a strong ER+ phenotype-recapitulating system.
- **Applications:** endocrine-therapy mechanism/resistance, CDK4/6 and PI3K/AKT combination testing, *ESR1*-mutation biology, chemoprevention.
- **Resources:** Cellosaurus, ATCC, MGI, RGD, DepMap (dependency/CRISPR screens: *ESR1*, *FOXA1*, *GATA3*, *CDK4/6* dependencies in luminal lines), Alliance of Genome Resources.

---

## Curation Notes & Ontology Summary (for dismech entry)

| Field | Suggested value |
|---|---|
| **MONDO** | `MONDO:0006512` (estrogen-receptor positive breast cancer); luminal A `MONDO:0021116`, luminal B `MONDO:0021115` |
| **Cell of origin (CL)** | `CL:0002326` luminal epithelial cell of mammary gland |
| **Anatomy (UBERON)** | `UBERON:0000310` breast; `UBERON:0003244` epithelium of mammary gland; metastasis: `UBERON:0002481` bone, `UBERON:0002107` liver, `UBERON:0002048` lung |
| **Defining phenotype (HPO)** | `HP:0020325` Increased breast-tissue estrogen receptor expression; `HP:0031093` Breast mass; `HP:0100013` Neoplasm of the breast |
| **Key genes (HGNC)** | *ESR1* (HGNC:3467), *PIK3CA* (HGNC:8975), *GATA3* (HGNC:4172), *CDH1* (HGNC:1748), *AKT1*, *ESR2* (HGNC:3468), *CCND1*, *TP53*, *MAP3K1* |
| **Biological process (GO)** | `GO:0030520` intracellular estrogen receptor signaling; `GO:0000082` G1/S transition; `GO:0008283` cell proliferation |
| **Chemicals (CHEBI)** | 17β-estradiol `CHEBI:16469`; tamoxifen `CHEBI:41774`; fulvestrant `CHEBI:31638` |
| **Treatments (MAXO/NCIT)** | Pharmacotherapy `NCIT:C15986` (with therapeutic agents tamoxifen/AI/SERD/CDK4-6i); surgery `MAXO:0000004`; radiotherapy `MAXO:0000014` |

**Highest-value, verified PMIDs for evidence items** (all abstracts retrieved and quotes confirmed via PubMed):

| PMID | Topic | DOI |
|---|---|---|
| 23000897 | TCGA molecular portraits (luminal drivers) | [10.1038/nature11412](https://doi.org/10.1038/nature11412) |
| 39352042 | ACS Breast Cancer Statistics 2024 (epidemiology) | [10.3322/caac.21863](https://doi.org/10.3322/caac.21863) |
| 34392831 | ESR1 mutation as resistance biomarker (review) | [10.1186/s13058-021-01462-3](https://doi.org/10.1186/s13058-021-01462-3) |
| 32954927 | monarchE — adjuvant abemaciclib | [10.1200/JCO.20.02514](https://doi.org/10.1200/JCO.20.02514) |
| 31091374 | SOLAR-1 — alpelisib (PIK3CA) | [10.1056/NEJMoa1813904](https://doi.org/10.1056/NEJMoa1813904) |
| 37256976 | CAPItello-291 — capivasertib (AKT) | [10.1056/NEJMoa2214131](https://doi.org/10.1056/NEJMoa2214131) |
| 35665782 | DESTINY-Breast04 — T-DXd (HER2-low) | [10.1056/NEJMoa2203690](https://doi.org/10.1056/NEJMoa2203690) |
| 29860917 | TAILORx — 21-gene, node-negative | [10.1056/NEJMoa1804710](https://doi.org/10.1056/NEJMoa1804710) |
| 34914339 | RxPONDER — 21-gene, node-positive | [10.1056/NEJMoa2108873](https://doi.org/10.1056/NEJMoa2108873) |
| 37314500 | Elacestrant (oral SERD) pharmacology/EMERALD | [10.1007/s00280-023-04550-7](https://doi.org/10.1007/s00280-023-04550-7) |

**Additional canonical PMIDs cited from domain knowledge (verify snippets before use as evidence):** 29131280 (Pan et al., 20-year recurrence risk, NEJM 2017); 12117397 (WHI combined MHT); 12189224 (endogenous hormones meta-analysis); 29059683 (BCAC GWAS, 65 new loci).

---

### Important caveats for the KB curator
1. **Verify every snippet against the fetched cache** (`just fetch-reference PMID:…` → `just validate-references`). Quotes above are transcribed from PubMed abstracts but must pass the exact-substring check. The abstracts for SOLAR-1 (PMID:31091374) rendered with dropped gene symbols in the PubMed feed (e.g., "*-mutated*" for *PIK3CA*-mutated); re-fetch and quote a clean substring.
2. **This is a subtype/molecular-class entry, not a Mendelian disorder** — omit inapplicable template fields (anticipation, mosaicism, single-gene knockout recapitulation) or record them explicitly as *not applicable*.
3. **HER2-low and ER-low-positive** are evolving biomarker categories — flag as active-research (`KNOWLEDGE_GAP`).
4. Consider `conforms_to` links to relevant dismech cancer-hallmark modules — especially **`sustaining_proliferative_signaling`** (ER→cyclin D1→CDK4/6), **`evading_growth_suppressors`** (RB axis / CDK4/6-inhibitor target), and **`resisting_cell_death`** — and the endocrine-therapy drug-mechanism pattern (ER as target of SERM/SERD/AI).