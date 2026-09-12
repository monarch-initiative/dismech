---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-08-10T03:44:28.130694'
end_time: '2026-08-10T03:49:50.779049'
duration_seconds: 322.65
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Pulmonary Embolism
  mondo_id: ''
  category: Acquired
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
  - claude-haiku-4-5-20251001
  - claude-sonnet-5
  web_search_requests: 17
  num_turns: 18
  total_cost_usd: 1.6775373
  session_id: ccd9973f-d61b-50a6-8cfe-0a77b122d0f2
  stop_reason: end_turn
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Pulmonary Embolism
- **MONDO ID:**  (if available)
- **Category:** Acquired

## Research Objectives

Please provide a comprehensive research report on **Pulmonary Embolism** covering all of the
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

For each treatment, suggest NCIT (NCI Thesaurus) clinical-intervention terms where applicable.

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
- Ontology term suggestions (HPO, GO, CL, UBERON, CHEBI, NCIT, MONDO) where applicable
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
- Treatment annotations (NCIT terms)
- Evidence items with PMIDs and exact abstract quotes
- Epidemiology, prognosis, diagnostic, and prevention information
- Animal model descriptions with phenotype recapitulation details


## Output

# Pulmonary Embolism (PE): Comprehensive Disease Characteristics Research Report

## 1. Disease Information

**Overview:** Pulmonary embolism (PE) is an acquired cardiovascular emergency caused by the acute obstruction of the pulmonary arterial circulation by embolic material — most commonly a thrombus (thromboembolism) that has dislodged from the deep venous system, though fat, air, amniotic fluid, tumor, and septic emboli are recognized non-thrombotic variants. PE and deep vein thrombosis (DVT) are the two principal clinical manifestations of venous thromboembolism (VTE), a single underlying disease process; roughly 90% of PE thrombi originate in the proximal deep veins of the lower extremities, pelvis, or (less commonly) upper extremities/right heart. Acute obstruction increases pulmonary vascular resistance and right ventricular (RV) afterload, and it is this hemodynamic consequence — not the embolus itself — that drives short-term mortality risk.

**Key identifiers:**
- **MONDO:** MONDO:0005279 (pulmonary embolism)
- **ICD-10-CM:** I26 (Pulmonary embolism); I26.0 (with acute cor pulmonale); I26.9 (without acute cor pulmonale); O88.2 (obstetric PE)
- **ICD-11:** BB00 (Pulmonary embolism)
- **MeSH:** D011655 (Pulmonary Embolism)
- **HPO:** HP:0002204 (Pulmonary embolism)
- **SNOMED CT:** 59282003 (Pulmonary embolism)
- **OMIM:** PE itself is a multifactorial acquired condition without a dedicated OMIM disease number; monogenic thrombophilias predisposing to it are separately cataloged — Factor V Leiden thrombophilia (OMIM 188055), Prothrombin-related thrombophilia (OMIM 176930), Protein C deficiency (OMIM 176860), Protein S deficiency (OMIM 176880), Antithrombin III deficiency (OMIM 613118).
- **Orphanet:** Idiopathic/inherited thrombophilias are separately coded (e.g., ORPHA:325 Hereditary antithrombin deficiency); PE as an acquired event does not carry a distinct Orphanet number given its high population prevalence.

**Synonyms/alternative names:** Pulmonary thromboembolism (PTE), acute pulmonary embolism, lung embolism, pulmonary infarction (when tissue necrosis occurs distally), massive/submassive PE (older, now-discouraged severity nomenclature — see §11), venous thromboembolism (VTE) when referring to the combined DVT/PE spectrum.

**Data provenance:** Most PE knowledge derives from aggregated, disease-level clinical resources — large multicenter cohorts (e.g., RIETE registry), national/administrative databases (WHO mortality database, US National Inpatient Sample), randomized controlled trials of anticoagulants, and systematic reviews/meta-analyses — rather than single-patient EHR mining, though EHR-based case-finding algorithms (Wells/YEARS/Geneva scores) are themselves embedded in routine care and increasingly captured in real-world data.

---

## 2. Etiology

### Disease Causal Factors
PE's proximate cause is thrombus formation in the venous circulation followed by embolization to the pulmonary arterial tree. Thrombogenesis is classically explained by **Virchow's triad**: (1) endothelial/vascular wall injury, (2) blood stasis, and (3) a hypercoagulable state. Modern reviews frame these three factors as converging mechanistic axes rather than independent causes — thrombosis typically begins as a platelet-fibrin nidus on venous valve pockets in the lower-extremity deep veins, propagates, and can embolize (Stone et al., *Cardiovasc Diagn Ther*, review of DVT pathogenesis; Chung, Lip, *J Thromb Haemost* 2003, PMC3006583 — "Virchow's Contribution to the Understanding of Thrombosis and Cellular Biology"). Non-thrombotic causes (fat embolism after long-bone fracture, air embolism from vascular procedures, amniotic fluid embolism in pregnancy, tumor embolism, septic embolism from infective endocarditis or IV drug use) share the same anatomical endpoint but distinct triggering mechanisms.

### Risk Factors — Genetic
- **Factor V Leiden (F5 R506Q, rs6025)** — the single most common inherited thrombophilia (~5% of the general European-ancestry population); heterozygotes have ~3-fold increased VTE risk, homozygotes 50–80-fold (PMID: 22329698, meta-analysis of FVL/PT G20210A in symptomatic PE/DVT). HGNC: F5 (HGNC:3542).
- **Prothrombin G20210A (F2 20210G>A)** — affects 1–4% of US/European populations; increases prothrombin levels ~70% in homozygotes; independent VTE risk factor, with a disproportionately higher relative risk for isolated PE than FVL (15% isolated PE in G20210A carriers vs. 6% in FVL carriers and 6% in non-thrombophilic patients) (PMID: 18796457). HGNC: F2 (HGNC:3535).
- **Combined FVL + G20210A heterozygosity** — synergistic risk, OR ≈20.0 (95% CI 11.1–36.1) for venous thrombosis versus neither mutation (pooled analysis, PMID: 11583312).
- **Protein C deficiency (PROC, OMIM 176860), Protein S deficiency (PROS1, OMIM 176880), Antithrombin III deficiency (SERPINC1, OMIM 613118)** — rarer but higher-penetrance autosomal dominant thrombophilias; antithrombin deficiency confers the highest relative risk among classic thrombophilias.
- **ABO blood group** — non-O blood groups (especially A) confer ~1.5–2× VTE risk via elevated von Willebrand factor/Factor VIII.
- **Polygenic risk** — a 2023 genome-wide meta-analysis of 81,190 VTE cases and >1.4 million controls identified **93 risk loci (62 novel)**, with a polygenic risk score whose top 0.1% carries VTE risk comparable to monogenic FVL/prothrombin carriers (Klarin et al., *Nat Genet* 2023, PMID: 36658437). Many loci map to coagulation-cascade or platelet-function genes. A 2024–2025 multipopulation GWAS across 9 international cohorts identified 38 genome-wide-significant loci including 2 novel loci (NME7, FOXK2) among FVL/prothrombin carriers, implying modifier loci beyond the classic monogenic mutations (Blood 2024 abstract; Blood Advances 2025, PMID: 40554366).
- **Proteome-wide Mendelian randomization** implicates 20 causally associated circulating proteins (F2, F11, ABO, PLCG2, LRP4, PLEK, KLKB1, PROC, KNG1, THBS2, SERPINA1, RARRES2, CEL, GP6, SERPINE2, SERPINA10, OBP2B, EFEMP1, F5, MSR1) — nominating novel druggable targets (PMC10678328).
- **Dysfibrinogenemia, plasminogen deficiency, elevated Factor VIII/IX/XI** — additional, lower-penetrance heritable contributors.

### Risk Factors — Environmental/Acquired
- **Surgery and trauma** (especially orthopedic — hip/knee arthroplasty, major trauma with immobilization)
- **Malignancy** (see §2/§6 cancer-associated thrombosis; Khorana score risk stratification)
- **Immobilization** (long-haul travel, hospitalization, paralysis)
- **Pregnancy and puerperium** — 5-fold increased VTE risk antepartum, 15–35-fold postpartum (Frontiers Cardiovasc Med 2022 review); incidence of PE in pregnancy ≈1/1,000 pregnancies; PE accounts for ~3.2% of global maternal deaths.
- **Estrogen exposure** — combined oral contraceptives, hormone replacement therapy
- **Obesity, older age, prior VTE, central venous catheters, nephrotic syndrome, inflammatory bowel disease, COVID-19/severe infection** (COVID-19-associated coagulopathy substantially elevates in-hospital VTE risk)
- **Smoking** — modest independent risk factor, particularly synergistic with oral contraceptive use.

### Protective Factors
- No strong genetic "protective allele" is as well established as the risk variants, though the polygenic score distribution (PMID 36658437) implies the low tail carries reduced risk. Regular physical activity, maintenance of normal BMI, and avoidance of prolonged immobilization are the principal modifiable protective/behavioral factors; prophylactic anticoagulation (mechanical or pharmacologic) is protective in high-risk surgical/hospitalized populations.

### Gene-Environment Interactions
Inherited thrombophilia interacts multiplicatively with acquired provoking factors — e.g., FVL carriers taking combined oral contraceptives have markedly higher risk than either factor alone; pregnancy in antithrombin-deficient women confers very high absolute VTE risk. CTD (Comparative Toxicogenomics Database) and PheGenI catalog such gene-chemical-disease interactions for F5/F2/SERPINC1.

---

## 3. Phenotypes

PE phenotypes span symptoms, signs, and laboratory/imaging abnormalities, with substantial heterogeneity — from asymptomatic incidental PE to sudden cardiac arrest.

| Phenotype | Type | Frequency (approx.) | HPO term |
|---|---|---|---|
| Dyspnea (acute-onset) | Symptom | ~50–75% (most common presenting symptom) | HP:0002094 |
| Pleuritic chest pain | Symptom | ~40–70% | HP:0030848 (Pleuritic chest pain) / HP:0100749 (Chest pain) |
| Tachycardia | Sign | ~25–40% | HP:0001649 |
| Tachypnea | Sign | ~50–70% | HP:0002789 |
| Cough | Symptom | ~20–35% | HP:0012735 |
| Hemoptysis | Symptom | ~5–13% (more common with pulmonary infarction) | HP:0002105 |
| Syncope | Symptom/sign | ~5–15% (marker of high-risk PE) | HP:0001279 |
| Hypotension/shock | Sign | ~5% (defines high-risk PE) | HP:0002615 (Hypotension) |
| Lower-limb DVT signs (unilateral leg swelling/pain) | Sign | ~40–50% concurrent DVT on imaging | HP:0030963-adjacent / clinical (DVT itself: HP:0004936, Deep venous thrombosis) |
| Elevated troponin | Lab abnormality | ~30–50% (marker of RV myocardial strain) | HP:0410174 or generic biomarker slot |
| Elevated BNP/NT-proBNP | Lab abnormality | variable, correlates with RV dysfunction | — |
| Elevated D-dimer | Lab abnormality | >95% sensitivity, low specificity | — |
| RV dysfunction on echocardiography | Imaging finding | ~25–50% of normotensive PE | HP:0011675 (Arrhythmia) not applicable; use HP:0025159 (Reduced right ventricular ejection fraction) or free text |
| Hypoxemia | Lab/sign | common | HP:0012418 |
| Fever (low-grade) | Symptom | ~10% | HP:0001945 |

**Characteristics:**
- **Onset:** Acute onset is typical (hours), but subacute/insidious presentations occur with recurrent small emboli or in chronic thromboembolic disease.
- **Severity:** Highly variable — the AHA/ACC 2026 guideline formalizes a 5-tier severity classification (Clinical Categories A–E, low to high risk; see §11) replacing the older informal "massive/submassive/minor" terminology.
- **Progression:** Typically an acute event followed by either resolution (with anticoagulation), recurrence, or (in ~0.1–9% depending on cohort) evolution to chronic thromboembolic pulmonary hypertension (CTEPH) over months (see §6, §11).
- **Frequency in affected individuals:** Classic PIOPED-era data: dyspnea (73%), pleuritic pain (66%), cough (37%), leg swelling (28%), hemoptysis (13%). Up to 30–40% of patients with confirmed DVT have concurrent asymptomatic PE.

**Quality of life impact:** Post-PE syndrome — persistent dyspnea, functional limitation, and reduced exercise capacity — affects an estimated 30–50% of survivors at 1 year even without CTEPH, impairing SF-36/EQ-5D physical-function domains (Klok FA et al., post-PE syndrome literature). Post-thrombotic syndrome (when concurrent DVT) further impairs QoL.

---

## 4. Genetic/Molecular Information

PE itself is not a monogenic disease; genetic contributions act through heritable thrombophilia predisposing to venous thrombosis (upstream cause) rather than through a PE-specific gene.

**Causal/predisposing genes (thrombophilia):**
| Gene | HGNC | Variant | Classification | Mechanism |
|---|---|---|---|---|
| F5 | HGNC:3542 | c.1601G>A (R506Q), "Factor V Leiden" | Pathogenic (established risk factor) | Loss of APC cleavage site → resistance to activated protein C degradation → prothrombotic gain-of-persistence |
| F2 | HGNC:3535 | c.*97G>A (20210G>A, 3′UTR) | Pathogenic (established risk factor) | Increased prothrombin mRNA stability/translation → elevated plasma prothrombin |
| PROC | HGNC:9451 | Various LOF | Pathogenic | Protein C deficiency, loss of anticoagulant surveillance |
| PROS1 | HGNC:9456 | Various LOF | Pathogenic | Protein S deficiency (Protein C cofactor loss) |
| SERPINC1 | HGNC:775 | Various LOF | Pathogenic | Antithrombin deficiency, loss of thrombin/factor Xa inhibition |
| ABO | HGNC:79 | Non-O blood group alleles | Risk-modifying | Elevated vWF/Factor VIII |
| F11, F13, THBD, FGG | various | Various | Risk-modifying | Coagulation cascade modulation |

**Allele frequencies:** FVL ~5% (European ancestry), rare in African/Asian populations; prothrombin G20210A ~1–4% (European ancestry), rare elsewhere — both queryable via gnomAD/1000 Genomes. Antithrombin/Protein C/S deficiencies are individually rare (<0.5% population prevalence) but higher-penetrance.

**Variant classification:** ClinVar and ClinGen curate pathogenicity per ACMG/AMP criteria for PROC/PROS1/SERPINC1 LOF variants; FVL and prothrombin G20210A are long-established "risk allele" (not strict Mendelian pathogenic) classifications given incomplete penetrance.

**Functional consequences:** Predominantly gain-of-function/loss-of-regulation for procoagulant factors (FVL, prothrombin 20210A) versus loss-of-function for natural anticoagulants (Protein C, Protein S, antithrombin) — i.e., the shared endpoint is a shift in the coagulation/anticoagulation balance toward net thrombin generation.

**Polygenic architecture:** The 2023 GWAS meta-analysis (PMID: 36658437) found the 93 identified loci converge on coagulation cascade and platelet function genes; a polygenic risk score (PRS) stratifies risk continuously and rivals monogenic thrombophilia at its extremes — supporting a common-variant, quantitative-trait architecture layered atop rare high-penetrance variants.

**Somatic/acquired hypercoagulability:** JAK2 V617F and other myeloproliferative-neoplasm driver mutations are recognized somatic causes of unusual-site/unprovoked VTE (e.g., splanchnic vein thrombosis, less commonly PE), relevant when working up unprovoked PE in younger patients.

**Epigenetics:** Less well characterized for PE specifically than for other vascular disease; some evidence links DNA methylation changes in coagulation-gene promoters (e.g., F3/tissue factor) to VTE risk, but this is an emerging rather than established area.

**Chromosomal abnormalities:** Not a recognized primary cause of PE; PE is not part of classic aneuploidy/CNV syndromes.

---

## 5. Environmental Information
(See also §2.) Key environmental/exposure categories:
- **Surgical/traumatic tissue injury** — activates tissue factor pathway; ECTO-codeable perioperative immobilization exposure.
- **Prolonged immobility** — long-haul air/car travel ("economy class syndrome"), hospital bed rest, cast immobilization.
- **Hormonal exposures** — estrogen-containing contraceptives, hormone replacement therapy, selective estrogen receptor modulators (tamoxifen).
- **Infectious triggers** — severe infection/sepsis (including COVID-19, which independently and substantially elevates VTE/PE risk via endothelial injury, complement activation, and immunothrombosis) and infective endocarditis (source of septic pulmonary emboli).
- **Toxin/lifestyle exposures** — tobacco smoking (synergistic with estrogen), obesity, dehydration.
- No pathogen directly *causes* thrombotic PE (it is not an infectious disease per se), but septic emboli PE is a distinct infectious-etiology variant (typically Staphylococcus aureus from right-sided endocarditis or IV drug use, or oropharyngeal anaerobes in Lemierre syndrome).

---

## 6. Mechanism / Pathophysiology

### Causal chain (initiating trigger → clinical manifestation)
1. **Trigger (upstream):** Endothelial injury / venous stasis / hypercoagulable state (Virchow's triad) in the deep venous system, most often the calf/popliteal/femoral/iliac veins.
2. **Thrombogenesis:** Platelet adhesion/activation at a venous valve pocket nidus → coagulation cascade activation → thrombin generation → fibrin polymerization → occlusive/non-occlusive venous thrombus (shared logic with the dismech `thrombogenesis` module: platelet adhesion/activation → coagulation cascade activation and thrombin-driven fibrin formation → pathological fibrin-platelet thrombus).
3. **Embolization:** Thrombus fragment dislodges (spontaneously or with mechanical perturbation) and travels via the inferior vena cava → right atrium → right ventricle → pulmonary arterial tree, lodging according to size (large thrombi can saddle the main pulmonary artery bifurcation; smaller emboli occlude segmental/subsegmental branches).
4. **Acute pulmonary vascular obstruction:** Mechanical obstruction plus hypoxic and serotonin/thromboxane-mediated pulmonary vasoconstriction → abrupt rise in pulmonary vascular resistance (PVR).
5. **RV afterload mismatch:** The thin-walled RV, unaccustomed to acute afterload, dilates and its wall tension rises → RV ischemia (reduced coronary perfusion pressure gradient) → contractile dysfunction → RV free-wall hypokinesis/dilation, interventricular septal bowing into the LV → reduced LV preload and cardiac output → hypotension/shock in severe cases. This RV-failure cascade is the proximate mechanism of hemodynamic collapse and early death, not the pulmonary infarct itself.
6. **Gas exchange abnormality:** Ventilation-perfusion (V/Q) mismatch and increased alveolar dead space → hypoxemia and hypocapnia (compensatory hyperventilation); true shunt can occur via atelectasis or patent foramen ovale reopening under RV pressure overload (paradoxical embolism risk).
7. **Neurohormonal/inflammatory amplification:** RV wall stress triggers natriuretic peptide release (BNP/NT-proBNP); myocardial stretch/microinfarction releases troponin; systemic inflammatory mediators (IL-6, TNF-α) are elevated and correlate with severity.
8. **Resolution vs. persistence:** Endogenous fibrinolysis (plasmin-mediated) and anticoagulant-assisted clot organization typically resolve most emboli over weeks; incomplete resolution with fibrotic remodeling of the pulmonary vascular intima can produce **chronic thromboembolic pulmonary hypertension (CTEPH)** — pooled incidence ~2.5–2.8% after acute PE (meta-analyses, ERJ 2023 update; higher in Asian populations, 5.08% vs. 1.96% in Europeans), risk-amplified by unprovoked PE, recurrent VTE, and baseline RV dysfunction.

### Molecular pathways
- **Coagulation cascade:** Extrinsic (tissue factor/Factor VIIa) and intrinsic (contact activation) pathways converge on Factor Xa → prothrombinase complex → thrombin → fibrin. KEGG: hsa04610 (Complement and coagulation cascades). Reactome: R-HSA-140877 (Formation of Fibrin Clot).
- **Platelet activation:** GPIb-vWF and GPVI-collagen interactions, thromboxane A2/ADP amplification — relevant KEGG hsa04611 (Platelet activation).
- **Fibrinolysis:** tPA/uPA–plasminogen–plasmin axis governs clot resolution; impaired fibrinolytic capacity (elevated PAI-1) is linked to recurrent VTE and CTEPH risk.
- **Pulmonary vasoconstriction:** Serotonin (5-HT) and thromboxane A2 released from activated platelets acutely worsen V/Q mismatch and pulmonary hypertension independent of mechanical obstruction.
- **RV pressure-overload signaling:** Neurohormonal activation (renin-angiotensin, natriuretic peptide systems), myocardial stretch-induced BNP transcription, and RV ischemia-driven troponin release.

### Cellular processes
Endothelial activation/dysfunction, platelet activation and aggregation, neutrophil extracellular trap (NET) formation (immunothrombosis — increasingly recognized, especially in infection/cancer-associated and COVID-19-associated PE), cardiomyocyte stretch and stress response, and (in CTEPH) pulmonary artery smooth muscle cell proliferation/vascular remodeling analogous to the dismech `pulmonary_vascular_remodeling` and `thrombogenesis` modules.

### Protein dysfunction
Loss-of-function in natural anticoagulants (Protein C, Protein S, antithrombin) or gain-of-persistence in procoagulant factors (Factor V Leiden resisting APC-mediated inactivation; elevated prothrombin from the G20210A variant) shift the coagulation-anticoagulation equilibrium.

### Immune system involvement
Immunothrombosis — the coupling of innate immune activation (complement, neutrophils/NETs, monocyte tissue factor expression) to coagulation — is now recognized as a major mechanism in infection- and cancer-associated PE, exemplified dramatically by COVID-19-associated coagulopathy.

### Tissue damage mechanisms
RV ischemia from afterload mismatch and reduced coronary perfusion gradient; pulmonary infarction (hemorrhagic, wedge-shaped, typically peripheral/subpleural) occurs in a minority (~10–15%) of PE cases, more often with smaller distal emboli and pre-existing cardiopulmonary disease limiting collateral bronchial arterial flow.

### Biochemical abnormalities
Elevated D-dimer (fibrin degradation product — sensitive but nonspecific marker of ongoing fibrinolysis), elevated cardiac troponin I/T (myocardial strain/microinjury; associated with 5.4-fold higher odds of in-hospital mortality and 3.4-fold higher odds of RV dysfunction in meta-analysis), elevated BNP/NT-proBNP (ventricular wall stress; higher sensitivity for RV overload than troponin), arterial blood gas hypoxemia/hypocapnia.

### Molecular/omics profiling
- **Genomics:** GWAS loci as above (PMID: 36658437).
- **Metabolomics:** A 2022 Mendelian randomization study linked specific blood metabolites to genetically predicted PE risk (PMC9422150), nominating novel metabolic biomarkers, though causal directionality requires further validation.
- **Proteomics:** Proteome-wide MR nominates F2, F11, ABO, PROC, KNG1, SERPINC1, F5, and others as causal circulating proteins (PMC10678328).
- **Single-cell/spatial:** Not yet a mature area for PE specifically (contrast with atherosclerosis); most single-cell work on venous thrombosis mechanism is in animal models of the thrombus microenvironment (neutrophils, monocytes, platelets).

### Suggested ontology terms
- **GO (Biological Process):** GO:0007596 (blood coagulation), GO:0030193 (regulation of blood coagulation), GO:0002576 (platelet degranulation), GO:0042730 (fibrinolysis), GO:0001525 (angiogenesis, for CTEPH vascular remodeling), GO:0002544 (chronic inflammatory response)
- **GO (Molecular Function):** GO:0004252 (serine-type endopeptidase activity, for thrombin/Factor Xa), GO:0005515 (protein binding)
- **CL (Cell Type):** CL:0000767 (platelet-precursor/megakaryocyte lineage), CL:0000233 (platelet — note CL commonly uses "platelet" CL:0000233), CL:0000094 (granulocyte/neutrophil, NETs), CL:0000115 (endothelial cell), CL:0000746 (cardiac muscle cell, RV myocyte)
- **UBERON:** UBERON:0001004 (respiratory system), UBERON:0002048 (lung), UBERON:0002012 (pulmonary artery), UBERON:0002080 (heart right ventricle), UBERON:0001638 (vein), UBERON:0001211 (deep vein — approximate)
- **CHEBI:** CHEBI:9754 (thrombin substrate context), relevant drug CHEBI IDs listed in §12

---

## 7. Anatomical Structures Affected

**Organ level:**
- **Primary:** Lung (pulmonary arterial vasculature — main, lobar, segmental, or subsegmental branches depending on embolus size) — UBERON:0002048 (lung), UBERON:0002012 (pulmonary artery).
- **Secondary:** Heart, specifically the right ventricle (afterload-mediated dysfunction) — UBERON:0002080; systemic circulation (via hypotension/shock, end-organ hypoperfusion); the source deep veins (lower-extremity/pelvic) remain co-affected as the origin site — UBERON:0001638.
- **Body systems:** Cardiovascular system (primary), respiratory system (primary), and secondarily hematologic (coagulation system), and in shock states, renal/hepatic (hypoperfusion injury).

**Tissue/cell level:**
- Pulmonary arterial endothelium (CL:0002544 or CL:0000115, vein/artery endothelial cell), vascular smooth muscle (CL:0000359, in CTEPH remodeling), platelets (CL:0000233), neutrophils (CL:0000775), cardiomyocytes of the RV free wall (CL:0000746), alveolar epithelium (secondary V/Q mismatch effects, not primarily destroyed except in infarction).

**Subcellular level:**
- Platelet granules (dense/alpha granules) releasing procoagulant/proinflammatory mediators — GO:0031091 (platelet alpha granule); mitochondria of ischemic RV cardiomyocytes; endothelial Weibel-Palade bodies releasing vWF.

**Localization:**
- Central (saddle/main pulmonary artery) emboli are hemodynamically most dangerous; peripheral (segmental/subsegmental) emboli more often cause infarction and are more often incidental. PE can be unilateral or bilateral; bilateral, especially central, disease correlates with higher clinical severity.

---

## 8. Temporal Development

- **Onset:** PE has no fixed "typical age" the way a congenital disease does — incidence rises steeply with age (from <1/10,000/year in young adults to >1/1,000/year in the elderly). Onset is classically **acute** (minutes to hours), though presentations can be **subacute** with slowly enlarging/recurrent emboli, and rarely **insidious/chronic** in the CTEPH spectrum with progressive dyspnea over months to years.
- **Progression:** Untreated, acute PE carries substantial early mortality risk concentrated in the first hours to days (RV failure/shock); with anticoagulation, most patients stabilize and the embolic burden resolves over 3–6 months, tracked by follow-up imaging/echocardiography.
- **Stages:** The new 2026 AHA/ACC guideline formalizes 5 severity-based clinical categories (A–E, low → cardiopulmonary failure with persistent hypotension) explicitly replacing the older "massive/submassive/low-risk" nomenclature (see §11), integrating clinical severity score, biomarkers, and RV function.
- **Course pattern:** Predominantly a single acute event followed by resolution on anticoagulation; a minority experience recurrence (annualized recurrence risk after stopping anticoagulation ranges from ~3%/year for provoked PE to ~10%/year for unprovoked PE in some cohorts) or evolve into CTEPH (~2.5–2.8% cumulative incidence).
- **Duration:** Acute PE itself is self-limited with treatment (typically 3–6 months of anticoagulation for a first provoked event); however, some patients require extended/indefinite anticoagulation (unprovoked PE, persistent risk factors, cancer-associated thrombosis), and post-PE syndrome/CTEPH represent chronic sequelae.
- **Remission:** Full radiographic/functional resolution occurs in the majority of low-risk patients; incomplete clot resolution (residual pulmonary vascular obstruction) is documented in 20–50% by perfusion scan at follow-up in some series, though most remain asymptomatic.
- **Critical periods:** The first 1–2 weeks post-diagnosis carry the highest risk of clinical deterioration and death; the first 3–6 months carry highest recurrence risk after anticoagulation discontinuation; CTEPH diagnosis typically clusters at 3 months to several years post-index PE.

---

## 9. Inheritance and Population

### Epidemiology
- **Incidence:** Highly variable by population and ascertainment method — ~14/100,000/year in China, ~39/100,000/year in Hong Kong, up to ~115/100,000/year in the United States (per recent epidemiological syntheses). Overall global annual VTE incidence is commonly cited around 1–2 per 1,000 adults, rising sharply with age.
- **Mortality trends:** A 2025 analysis of WHO mortality data (2001–2023) found global age-standardized PE mortality declined from 3.49 to 2.42 per 100,000, with Europe declining sharply (5.24 → 2.25/100,000) but low/middle-income regions (notably parts of Africa and lower-middle-income countries broadly) showing stagnant or rising rates (0.92 → 4.82/100,000 in lower-middle-income countries) — reflecting disparities in diagnostic access and treatment (eClinicalMedicine 2025, PMC12336653).
- PE is the third most common cause of cardiovascular death after myocardial infarction and stroke in most high-income-country statistics, and a leading preventable cause of in-hospital death.

### Inheritance pattern (for genetic thrombophilia contributors)
- Factor V Leiden and Prothrombin G20210A: autosomal dominant with **incomplete penetrance** — most carriers never develop clinical VTE without a superimposed acquired trigger.
- Protein C, Protein S, Antithrombin deficiencies: autosomal dominant, generally higher penetrance than FVL/prothrombin, especially for antithrombin deficiency.
- Homozygous protein C or protein S deficiency: can cause neonatal purpura fulminans (severe, distinct from typical adult PE).
- The broader liability is **polygenic/multifactorial** — PE/VTE overall behaves as a complex trait with both monogenic high-penetrance and common polygenic contributions layered on strong environmental/provoking triggers (PMID: 36658437).

### Penetrance/Expressivity
- FVL heterozygote lifetime VTE penetrance is estimated at roughly 10% or less without additional provoking factors; penetrance rises substantially with combined thrombophilias, pregnancy, or estrogen exposure.
- Expressivity is variable — same genotype can manifest as isolated DVT, isolated PE, or both, and severity ranges from asymptomatic incidental finding to fatal.

### Genetic anticipation
Not a recognized feature of PE-associated thrombophilias (these are not repeat-expansion disorders).

### Founder effects / population variation
- FVL and prothrombin G20210A show marked ancestry-specific frequency differences — common in European-ancestry populations, rare in African, Asian, and Indigenous American populations, consistent with founder mutations arising after early human population divergence (~20,000–30,000 years ago for FVL).
- CTEPH after PE shows a geographic disparity: pooled Asian incidence (5.08%) is roughly 2.5× European incidence (1.96%) in meta-analysis (PMC8575791).

### Demographics
- **Sex:** PE incidence is roughly similar between sexes overall but shows sex-specific peaks — increased risk in women of reproductive age (pregnancy/oral contraceptives) and increased risk in men at older ages; some registries report a slight male predominance in unprovoked PE.
- **Age distribution:** Incidence rises exponentially with age, from rare in children/young adults (usually with a strong provoking factor or thrombophilia when it occurs) to a leading cause of sudden death in the elderly.
- **Consanguinity/carrier frequency:** Not classically relevant for FVL/prothrombin (common polymorphisms); more relevant for rare recessive natural-anticoagulant deficiencies, though most reported deficiencies are dominantly inherited with variable severity by zygosity.

---

## 10. Diagnostics

### Clinical decision rules and pretest probability
- **Wells score** (original and modified/simplified 3-level and 2-level versions) — clinical prediction rule combining signs of DVT, PE as most likely diagnosis, heart rate >100, immobilization/surgery, prior VTE, hemoptysis, malignancy. Combined with D-dimer, sensitivity/specificity improve substantially over Wells alone (one 2024 study: Wells alone 61.6% sensitivity/85.5% specificity; Wells + D-dimer cutoff 73.2%/92.1%).
- **YEARS algorithm** — a simplified, D-dimer-threshold-adaptive rule (three items: clinical DVT signs, hemoptysis, PE as most likely diagnosis) that reduces CTPA utilization; sensitivity ~86–90%, specificity ~33–65% depending on cohort (van Es et al., *Lancet* 2017).
- **Revised Geneva score** — an alternative, more objective (less subjective-judgment-dependent) clinical rule.

### Laboratory
- **D-dimer** (LOINC-codeable fibrin degradation product assay) — modern quantitative assays have pooled sensitivity ~97% (95% CI 96–98%) but low specificity ~41% (95% CI 36–46%); age-adjusted D-dimer thresholds improve specificity to ~47% while maintaining ~99% sensitivity, reducing unnecessary imaging in older patients.
- **Troponin I/T and BNP/NT-proBNP** — not diagnostic but essential prognostic/risk-stratification biomarkers (see §6, §11).
- **Arterial blood gas** — hypoxemia, widened A-a gradient, respiratory alkalosis (nonspecific).

### Imaging
- **CT pulmonary angiography (CTPA)** — first-line definitive imaging; pooled sensitivity ~94% (95% CI 89–97%), specificity ~98% (95% CI 97–99%); PIOPED II established CTPA as the diagnostic reference standard (Stein PD et al., *N Engl J Med* 2006).
- **Ventilation-perfusion (V/Q) scintigraphy** — alternative when CTPA contraindicated (renal impairment, contrast allergy, pregnancy — preferred in pregnancy due to lower breast radiation dose than CTPA in some protocols).
- **Compression ultrasonography of the lower extremities** — confirms concurrent/source DVT, can support PE diagnosis without further imaging in appropriate clinical context.
- **Transthoracic echocardiography** — bedside assessment of RV size/function (RV/LV ratio, McConnell sign, tricuspid annular plane systolic excursion — TAPSE); central to risk stratification and can support diagnosis in unstable patients too sick for CTPA.
- **Pulmonary angiography** — historic gold standard, now rarely needed given CTPA accuracy; retained as part of catheter-directed interventional procedures.

### Genetic testing
Not indicated for routine PE evaluation. Selective thrombophilia panel testing (FVL, prothrombin G20210A, protein C/S, antithrombin, antiphospholipid antibodies) is considered for: unprovoked PE in patients <50 years, recurrent VTE, unusual-site thrombosis, strong family history, or before stopping anticoagulation in select unprovoked cases — though guideline enthusiasm for broad testing has declined because results rarely change management in an isolated first VTE event.

### Clinical criteria / risk scores for prognosis (see §11)
PESI/sPESI, the AHA/ACC 2026 Clinical Categories (A–E).

### Screening
No population-level screening program exists for PE (unlike, e.g., cancer screening); "screening" in practice means risk-based VTE prophylaxis protocols in hospitalized/surgical patients (mechanical and/or pharmacologic), and Khorana-score-guided consideration of primary thromboprophylaxis in ambulatory cancer patients initiating chemotherapy.

### Differential diagnosis
Acute coronary syndrome, pneumonia, pericarditis, pneumothorax, aortic dissection, musculoskeletal chest pain, anxiety/panic disorder (for milder presentations), and COPD/asthma exacerbation (which can also coexist with PE, complicating decision rules — a 2024 study found Wells+D-dimer remained accurate in hospitalized COPD-exacerbation patients).

---

## 11. Outcome/Prognosis

### Mortality
- All-cause 30-day mortality in confirmed PE ranges widely by severity, roughly 1–2% in low-risk (sPESI 0) patients up to >30–50% in high-risk PE presenting with shock/cardiac arrest.
- Elevated troponin is associated with ~5.4-fold higher odds of in-hospital mortality and ~4.4-fold higher odds of 30-day mortality (meta-analysis).
- Global age-standardized PE mortality has declined substantially in high-income countries (3.68 → 2.20/100,000, 2001–2023) but is rising in lower-middle-income countries (0.92 → 4.82/100,000) — a striking disparity attributed to differential access to modern diagnostics/anticoagulants (eClinicalMedicine 2025).

### Risk stratification tools
- **PESI/simplified PESI (sPESI):** the most extensively validated clinical prognostic score, integrating age, sex, cancer, heart failure, chronic lung disease, heart rate, systolic BP, respiratory rate, temperature, altered mental status, and oxygen saturation; sPESI = 0 reliably identifies low-risk PE suitable for outpatient management.
- **2019 ESC risk stratification algorithm** (still widely used, PMID: 31504429) combines hemodynamic status, PESI/sPESI, RV dysfunction on imaging, and cardiac biomarkers into high/intermediate-high/intermediate-low/low risk categories.
- **2026 AHA/ACC Clinical Categories (A–E):** the newly published first dedicated US multisociety guideline (AHA/ACC/ACCP/ACEP/CHEST/SCAI/SHM/SIR/SVM/SVN) introduces a five-tier "Acute Pulmonary Embolism Clinical Categories" scheme spanning low risk through cardiopulmonary failure with persistent hypotension, intended to standardize severity assessment, prognosis, and therapy selection, explicitly retiring "massive/submassive" terminology (JACC/Circulation, April 2026; PMID: 41712898).

### Morbidity/functional outcomes
- **Post-PE syndrome:** persistent dyspnea/functional limitation without frank pulmonary hypertension, reported in roughly a third to half of survivors at 1 year.
- **CTEPH:** pooled incidence 2.5–2.8% after acute PE (updated 2023 ERJ meta-analysis), with higher rates in Asian populations and after RV dysfunction/unprovoked/recurrent PE; the original defining incidence study found CTEPH-consistent pulmonary hypertension in ~3.8% of PE survivors at 2 years (Pengo V et al., *N Engl J Med* 2004).
- **Recurrence:** highest for unprovoked PE and persistent risk factors (e.g., active cancer); recurrence risk after stopping anticoagulation is a major determinant of extended-therapy decisions.

### Prognostic biomarkers
Troponin, BNP/NT-proBNP, RV/LV diameter ratio on CTPA or echocardiography, lactate, and the composite PESI/sPESI/ESC risk categories.

---

## 12. Treatment

### Pharmacotherapy — Anticoagulation (mainstay)
- **Direct oral anticoagulants (DOACs)** — apixaban, rivaroxaban, edoxaban, dabigatran — now preferred over vitamin K antagonists (warfarin) for most patients given comparable/superior efficacy, lower major bleeding, and no routine monitoring requirement. Key trials: **EINSTEIN-PE** (rivaroxaban, *NEJM* 2012, PMID 22449293) and **AMPLIFY** (apixaban, *NEJM* 2013, PMID 23808982).
  - NCIT: C15986 (Pharmacotherapy); therapeutic_agent CHEBI: rivaroxaban CHEBI:68579, apixaban CHEBI:66989, edoxaban CHEBI:83495, dabigatran CHEBI:70746.
- **Extended-phase (reduced-dose) DOAC therapy** — CHEST and ESC/ERS guidelines both support low-intensity apixaban 2.5 mg twice daily or rivaroxaban 10 mg once daily for extended secondary prevention beyond the initial 3–6 months in appropriate patients.
- **LMWH/UFH** — first-line in pregnancy (DOACs contraindicated due to placental transfer/fetal risk), in cancer-associated thrombosis historically (though DOACs — apixaban preferentially — are now recommended by CHEST/NICE for most non-luminal-GI cancer PE, with apixaban or LMWH preferred specifically in luminal GI malignancy given DOAC-associated GI bleeding risk), and in hemodynamically unstable patients needing rapid reversibility.
- **Warfarin (vitamin K antagonist)** — retained for mechanical heart valves, antiphospholipid syndrome (triple-positive), and severe renal impairment where DOACs are contraindicated.

### Reperfusion therapy (high-risk/select intermediate-high-risk PE)
- **Systemic thrombolysis** (alteplase, tenecteplase) — indicated for high-risk PE with hemodynamic instability; PEITHO trial (*NEJM* 2014, PMID 24716681) showed reduced hemodynamic decompensation but increased major/intracranial bleeding with thrombolysis in intermediate-risk PE, informing more selective use.
- **Catheter-directed thrombolysis (CDT) / mechanical thrombectomy** — increasingly used for intermediate-high and high-risk PE, especially where PERT (Pulmonary Embolism Response Team) involvement is available; PERT-managed patients show higher use of catheter-directed interventions (36% vs 22% CDT; 16% vs 7% thrombectomy) and lower IVC filter use (1% vs 5%), with meta-analyses suggesting decreased mortality/length of stay under PERT-guided care. The FLARE registry (FlowTriever mechanical thrombectomy) reported 0.3% 48-hour and 0.8% 30-day all-cause mortality with favorable safety in intermediate/high-risk PE, supporting FDA clearance expansion in late 2023.
- **Surgical embolectomy** — reserved for high-risk PE with thrombolysis contraindication or failure, or for large central thrombi in centers with surgical expertise.

### Devices/interventional
- **Inferior vena cava (IVC) filters** — Class I indication limited to absolute anticoagulation contraindication with acute VTE, or recurrent PE despite adequate anticoagulation; evidence for mortality benefit is weak/mixed, though filters do reduce recurrent PE incidence without clearly increasing DVT/bleeding in trial meta-analyses; not indicated when anticoagulation is feasible. NCIT: device-category treatment, `therapeutic_modality: DEVICE`.

### Supportive/other
- Supplemental oxygen, vasopressor/inotropic support for RV failure/shock, extracorporeal membrane oxygenation (ECMO, especially veno-arterial) as a bridge in refractory high-risk PE.
- Compression therapy for concurrent DVT/prevention of post-thrombotic syndrome.

### CTEPH-specific therapy
- **Pulmonary endarterectomy (PEA)** — potentially curative surgical treatment for operable proximal CTEPH.
- **Balloon pulmonary angioplasty (BPA)** — for inoperable/distal disease.
- **Riociguat** (soluble guanylate cyclase stimulator) — approved pharmacotherapy for inoperable/residual CTEPH (CHEST-1 trial).

### Pharmacogenomics
Warfarin dosing is the principal pharmacogenomic-relevant example (CYP2C9, VKORC1 variants affecting warfarin sensitivity/dosing requirements) — captured in CPIC/PharmGKB guidelines; DOACs have comparatively limited established pharmacogenomic dosing algorithms, though P-glycoprotein (ABCB1) and CYP3A4 polymorphisms modestly affect exposure.

### Treatment algorithm summary
Risk-stratify (§11) → hemodynamically unstable (high-risk): reperfusion (thrombolysis/catheter-directed/surgical) + anticoagulation + hemodynamic support → hemodynamically stable with RV dysfunction/biomarker elevation (intermediate risk): anticoagulation, monitor, consider escalation if deteriorating → low-risk (sPESI 0, no RV dysfunction): anticoagulation, consider early discharge/outpatient management.

---

## 13. Prevention

### Primary prevention
- **Mechanical prophylaxis** — intermittent pneumatic compression devices, graduated compression stockings, particularly for surgical/immobilized patients with bleeding contraindications to pharmacologic prophylaxis.
- **Pharmacologic prophylaxis** — LMWH, unfractionated heparin, or (increasingly) DOACs in defined high-risk hospitalized medical/surgical populations, guided by validated risk-assessment models (e.g., Caprini score for surgical patients, Padua score for medical inpatients).
- **Behavioral/lifestyle** — early ambulation post-surgery/illness, hydration and leg movement during long-haul travel, weight management, smoking cessation.

### Secondary prevention (cancer-associated thrombosis)
- Khorana-score-guided consideration of primary pharmacologic thromboprophylaxis in ambulatory cancer patients initiating systemic therapy who are at elevated VTE risk (score ≥2–3), though the Khorana score's discriminative performance is notably weaker in lung cancer than in pancreatic/gastric/colorectal/ovarian/brain/bladder cancer.

### Pregnancy-specific prevention
Risk-based LMWH thromboprophylaxis in pregnant/postpartum women with prior VTE history or high-risk thrombophilia.

### Prophylaxis after index PE
Extended (beyond 3–6 months) anticoagulation in unprovoked PE or persistent major risk factors, per individualized bleeding-risk/recurrence-risk assessment; reduced-dose DOAC regimens specifically designed to balance extended prevention against bleeding risk.

### Genetic counseling / screening
Selective thrombophilia testing and counseling for at-risk family members after a proband is identified with a high-penetrance deficiency (protein C/S, antithrombin); routine population carrier screening for FVL/prothrombin G20210A is not recommended given low absolute penetrance.

### Public health
Hospital-based VTE-prevention quality metrics/protocols (a major patient-safety focus given PE's status as a leading preventable cause of in-hospital death), and clinical decision support tools embedded in EHRs to prompt risk assessment and appropriate prophylaxis ordering.

---

## 14. Other Species / Natural Disease

- **Taxonomy:** PE occurs across mammalian species; naturally occurring VTE/PE is documented in domestic dogs and cats, especially secondary to protein-losing nephropathy/enteropathy, hyperadrenocorticism, immune-mediated hemolytic anemia, neoplasia, and pancreatitis — paralleling many acquired human risk factors (OMIA and veterinary case-series literature; NCBI Taxonomy: Canis lupus familiaris NCBITaxon:9615, Felis catus NCBITaxon:9685).
- **Orthologous genes:** F5, F2, PROC, PROS1, and SERPINC1 orthologs are broadly conserved across mammals (NCBI Gene cross-species records exist for each); canine and feline coagulation biology is used comparatively to understand thrombophilia mechanisms, though naturally occurring FVL-equivalent thrombophilia is not a major recognized entity in companion animals the way it is in humans.
- **Comparative pathology:** Veterinary PE parallels human disease in gross/histopathologic appearance (occlusive pulmonary arterial thrombus, RV strain) but is typically secondary to an identifiable underlying illness rather than idiopathic/inherited thrombophilia, reflecting differences in typical case ascertainment (symptomatic veterinary presentation vs. broader human screening).
- **Zoonotic potential:** Not applicable — PE is not a transmissible/infectious disease in the conventional sense (septic PE is secondary to an infectious source, not itself transmissible as PE).

---

## 15. Model Organisms

**Important overarching limitation:** Well-characterized rodent models recapitulate venous *thrombosis* (DVT) far better than *pulmonary embolism* itself — a 2012 critical review of mouse venous thrombosis models notes that essentially none of the standard mouse VTE models reliably produce spontaneous pulmonary embolism, and survival in these models is close to 100% (Diaz JA et al., *Arterioscler Thromb Vasc Biol* 2012, PMID: 22345593; Grover SP & Mackman N, "Mouse models of deep vein thrombosis," PMID: 28715512). This is a significant translational gap: most mechanistic PE research either extrapolates from DVT models or uses direct pulmonary-artery embolization/injection models to study the embolic and RV-failure phase specifically.

**Genetic/induced mouse models (DVT-focused, upstream of embolization):**
- **Inferior vena cava (IVC) stasis/stenosis and ligation models** — surgical flow restriction inducing stasis-driven thrombosis; widely used to study leukocyte/platelet contributions to thrombus initiation and resolution.
- **Ferric chloride (FeCl₃) injury model** — chemical endothelial injury inducing occlusive thrombosis in a defined vessel segment; models the vessel-injury arm of Virchow's triad.
- **Electrolytic IVC model** — controlled endothelial denudation without complete flow occlusion, considered more physiologically representative of clinical DVT initiation.
- **Genetically engineered models** — F5 Leiden knock-in mice, Proc/Pros1/Serpinc1 knockout or hypomorphic mice (complete knockouts of natural anticoagulants are often embryonic lethal or require conditional/hypomorphic alleles), tissue factor overexpression models — used to dissect specific coagulation-factor contributions.

**Direct PE models (embolic/RV-failure phase):**
- **Autologous or homologous clot injection / microsphere embolization** into the pulmonary circulation (mouse, rat, rabbit, and larger animal models) to directly study acute RV pressure overload, hemodynamic collapse, and reperfusion/thrombolysis pharmacology without relying on spontaneous embolization from a DVT source.
- **Porcine models** — a 2021 paper describes a new experimental porcine model of venous thromboembolism (PMC8123404), valued for cardiovascular anatomic/physiologic similarity to humans, supporting device (catheter-directed thrombectomy, IVC filter) and hemodynamic studies more translatable to clinical intervention design than rodent models.
- **Zebrafish** — used in a 2025 multipopulation VTE GWAS for experimental validation of novel candidate loci (PMID: 40554366), leveraging the zebrafish's genetically tractable, visually accessible coagulation system for rapid functional variant screening, though this models the upstream thrombogenesis pathway rather than pulmonary embolization anatomy (zebrafish lack a pulmonary circulation analogous to mammals).

**Applications and limitations:**
- Rodent DVT models: excellent for dissecting the molecular/cellular biology of thrombus initiation, propagation, and natural resolution, and for early pharmacologic screening of novel anticoagulants; poor for modeling the hemodynamic RV-failure phenotype that drives human PE mortality.
- Direct pulmonary embolization/injection models: better recapitulate acute RV pressure overload and reperfusion pharmacology but bypass the "spontaneous embolization" biology, so they cannot inform prevention-of-embolization research.
- Porcine/large-animal models: best anatomic/hemodynamic translatability for interventional device testing (catheter thrombectomy, filters) but are costly and lower-throughput.
- No single model recapitulates the full human PE phenotype spectrum (thrombogenesis → embolization → RV failure → resolution/CTEPH); most research programs combine a DVT-genesis model with a separate direct-embolization hemodynamic model.

**Resources:** MGI (Mouse Genome Informatics) for F5/F2/Proc/Pros1/Serpinc1 mouse alleles, ZFIN for zebrafish coagulation-gene models, IMPC for systematic knockout phenotyping data on coagulation genes.

---

## Ontology Term Summary for KB Curation

| Category | Suggested terms |
|---|---|
| Disease | MONDO:0005279 (pulmonary embolism); HP:0002204 (Pulmonary embolism) |
| Causal/risk genes | F5 (hgnc:3542), F2 (hgnc:3535), PROC (hgnc:9451), PROS1 (hgnc:9456), SERPINC1 (hgnc:775), ABO (hgnc:79) |
| Key phenotypes | HP:0002094 (Dyspnea), HP:0030848 (Pleuritic chest pain), HP:0001649 (Tachycardia), HP:0002789 (Tachypnea), HP:0002105 (Hemoptysis), HP:0001279 (Syncope), HP:0002615 (Hypotension), HP:0004936 (Deep venous thrombosis) |
| GO biological processes | GO:0007596 (blood coagulation), GO:0042730 (fibrinolysis), GO:0002576 (platelet degranulation), GO:0030193 (regulation of blood coagulation) |
| Cell types | CL:0000233 (platelet), CL:0000115 (endothelial cell), CL:0000775 (neutrophil), CL:0000746 (cardiac muscle cell) |
| Anatomy | UBERON:0002048 (lung), UBERON:0002012 (pulmonary artery), UBERON:0002080 (right cardiac ventricle), UBERON:0001638 (vein) |
| Treatments (NCIT) | NCIT:C15986 (Pharmacotherapy), NCIT:C15632 (Chemotherapy — N/A here), NCIT:C15313 (Radiation Therapy — N/A), catheter-directed therapy/device-classified as `therapeutic_modality: DEVICE`, surgical embolectomy → NCIT:C15329 (Surgical Procedure) |
| Therapeutic agents (CHEBI) | rivaroxaban CHEBI:68579, apixaban CHEBI:66989, edoxaban CHEBI:83495, dabigatran CHEBI:70746, alteplase/tenecteplase (protein therapeutics, may lack CHEBI; use NCIT) |

---

## Selected Citations

1. Klarin D et al. Genome-wide meta-analysis identifies 93 risk loci and enables risk prediction equivalent to monogenic forms of venous thromboembolism. *Nat Genet* 2023. PMID: 36658437.
2. Multipopulation GWAS for venous thromboembolism identifies novel loci followed by experimental validation in zebrafish. *Blood Advances* 2025. PMID: 40554366.
3. Combined effect of factor V Leiden and prothrombin 20210A on the risk of venous thromboembolism — pooled analysis of 8 case-control studies. PMID: 11583312.
4. Role of factor V Leiden or G20210A prothrombin mutation in patients with symptomatic pulmonary embolism and deep vein thrombosis: a meta-analysis. PMID: 22329698.
5. Type and location of venous thromboembolism in carriers of Factor V Leiden or prothrombin G20210A mutation versus patients with no mutation. PMID: 18796457.
6. Konstantinides SV et al. 2019 ESC Guidelines for the diagnosis and management of acute pulmonary embolism. *Eur Heart J* 2020;41(4):543-603. PMID: 31504429.
7. 2026 AHA/ACC/ACCP/ACEP/CHEST/SCAI/SHM/SIR/SVM/SVN Guideline for the Evaluation and Management of Acute Pulmonary Embolism in Adults. *Circulation/JACC* 2026. PMID: 41712898.
8. EINSTEIN-PE Investigators. Oral rivaroxaban for symptomatic venous thromboembolism. *N Engl J Med* 2012;366:1287-97. PMID: 22449293.
9. Agnelli G et al. (AMPLIFY). Oral apixaban for the treatment of acute venous thromboembolism. *N Engl J Med* 2013;369:799-808. PMID: 23808982.
10. Meyer G et al. (PEITHO). Fibrinolysis for patients with intermediate-risk pulmonary embolism. *N Engl J Med* 2014;370:1402-11. PMID: 24716681.
11. Stein PD et al. (PIOPED II). Multidetector computed tomography for acute pulmonary embolism. *N Engl J Med* 2006;354:2317-27. PMID: 16738268.
12. Pengo V et al. Incidence of chronic thromboembolic pulmonary hypertension after pulmonary embolism. *N Engl J Med* 2004;350:2257-64.
13. Incidence of chronic thromboembolic pulmonary hypertension after acute pulmonary embolism: updated systematic review and meta-analysis. *Eur Respir J* 2023. 
14. Higher incidence of CTEPH after acute PE in Asians than Europeans: a meta-analysis. PMC8575791.
15. Global trends in mortality related to pulmonary embolism: WHO mortality database 2001–2023. *eClinicalMedicine* 2025. PMC12336653.
16. Diaz JA et al. Critical review of mouse models of venous thrombosis. *Arterioscler Thromb Vasc Biol* 2012. PMID: 22345593.
17. Grover SP, Mackman N. Mouse models of deep vein thrombosis. PMID: 28715512.
18. Impact of pulmonary embolism response teams on acute pulmonary embolism: systematic review and meta-analysis. *Eur Respir Rev* 2023.
19. Prognostic value of right ventricular dysfunction or elevated cardiac biomarkers in low-risk pulmonary embolism: systematic review and meta-analysis. *Eur Heart J* 2019;40(11):902.
20. Pulmonary embolism and 529 human blood metabolites: genetic correlation and two-sample Mendelian randomization study. PMC9422150.
21. Proteome-wide Mendelian randomization identifies causal plasma proteins in venous thromboembolism development. PMC10678328.

---

**Note on completeness:** This report synthesizes findings from a targeted literature and guideline search (2023–2026 emphasis, per instructions) combined with well-established foundational PE literature. Several sub-areas (single-cell/spatial transcriptomics of pulmonary thrombus tissue, detailed epigenomic profiling, and comprehensive veterinary comparative-pathology datasets) have sparse dedicated primary literature for PE specifically and are flagged above as emerging/limited rather than fabricated to appear complete.