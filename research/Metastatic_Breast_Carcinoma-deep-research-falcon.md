---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-09T12:23:25.717697'
end_time: '2026-05-09T12:41:04.755620'
duration_seconds: 1059.04
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Metastatic Breast Carcinoma
  mondo_id: ''
  category: ''
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 29
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Metastatic Breast Carcinoma
- **MONDO ID:**  (if available)
- **Category:**

## Research Objectives

Please provide a comprehensive research report on **Metastatic Breast Carcinoma** covering all of the
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

Question: You are an expert researcher providing comprehensive, well-cited information.

Provide detailed information focusing on:
1. Key concepts and definitions with current understanding
2. Recent developments and latest research (prioritize 2023-2024 sources)
3. Current applications and real-world implementations
4. Expert opinions and analysis from authoritative sources
5. Relevant statistics and data from recent studies

Format as a comprehensive research report with proper citations. Include URLs and publication dates where available.
Always prioritize recent, authoritative sources and provide specific citations for all major claims.

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Metastatic Breast Carcinoma
- **MONDO ID:**  (if available)
- **Category:**

## Research Objectives

Please provide a comprehensive research report on **Metastatic Breast Carcinoma** covering all of the
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


# Metastatic Breast Carcinoma (Metastatic Breast Cancer): Disease Characteristics Research Report

**Scope and evidence note:** This report is limited to sources successfully retrieved in the tool run. Several requested ontology identifiers (e.g., specific MONDO term for *metastatic breast carcinoma*, ICD-10/ICD-11 codes, MeSH tree numbers) were not directly retrievable from the available corpus; where absent, this is stated explicitly.

## Target disease
- **Disease name:** Metastatic breast carcinoma (metastatic breast cancer; stage IV breast cancer)
- **Category:** Malignant neoplasm (carcinoma) with distant metastasis
- **MONDO ID:** Not confirmed for the specific entity “metastatic breast carcinoma” in the retrieved sources. (The OpenTargets query returned MONDO_0007254 for “breast cancer” rather than a metastatic-specific MONDO term.) (OpenTargets Search: metastatic breast carcinoma)

## 1. Disease information
### 1.1 Definition and current understanding
Metastatic breast carcinoma refers to breast carcinoma that has spread beyond the breast and regional lymph nodes to distant organs (distant metastasis). It is clinically aligned with **stage IV breast cancer**, including both **de novo metastatic disease** (metastatic at first diagnosis) and **recurrent metastatic disease** (metastasis after earlier-stage treatment). Population-based analyses use SEER “distant metastasis” indicators and commonly track organ sites including **bone, lung, liver, and brain** (zhang2025patternsandprognostic pages 1-2, zhang2025patternsandprognostic pages 2-4).

### 1.2 Synonyms / alternative names
Commonly used synonyms in the retrieved literature include:
- metastatic breast cancer (mBC)
- de novo metastatic breast cancer
- stage IV breast cancer
- advanced breast cancer (often includes locally advanced + metastatic; context dependent)
(OpenTargets Search: metastatic breast carcinoma, varghese2025epidemiologyandoutcomes pages 1-2)

### 1.3 Key identifiers
- **MONDO:** not confirmed for metastatic-specific entity from retrieved sources (see Scope note).
- **MeSH/ICD-10/ICD-11/OMIM/Orphanet:** not retrieved in this run.

### 1.4 Evidence source types represented
- **Aggregated registry data:** SEER population studies of de novo metastatic disease and metastatic patterns (OpenTargets Search: metastatic breast carcinoma, zhang2025patternsandprognostic pages 8-10, zhang2025patternsandprognostic pages 1-2).
- **Aggregated EHR real-world data:** Flatiron Health EHR cohort for brain metastases outcomes (varghese2025epidemiologyandoutcomes pages 1-2).
- **Randomized controlled trials (RCTs):** CAPItello-291, EVER-132-002; summarized directly from primary publications/figures (turner2023capivasertibinhormone media c3df1a43, turner2023capivasertibinhormone media 7aa4aaf1, evangelou2025updatesinadvanced pages 3-4).
- **Regulatory science:** FDA approval summary for elacestrant (shah2024usfoodand pages 1-2).
- **Real-world observational cohorts:** nationwide French cohort and single-center series for trastuzumab deruxtecan (T-DXd) (jourdain2024useandoutcomes pages 1-2, lazaratos2024therealworldclinical pages 1-2).

## 2. Etiology
Metastatic breast carcinoma represents progression of breast carcinoma via biological programs enabling invasion, dissemination, and colonization of distant sites. In the retrieved corpus, etiology is most directly addressed through **genomic correlates of endocrine resistance** and **treatment-driven selection**.

### 2.1 Disease causal factors (mechanistic/biologic)
A central mechanistic theme in HR+/HER2− metastatic disease is endocrine therapy resistance associated with acquired **ESR1 mutations** (shah2024usfoodand pages 1-2, bhave2024comprehensivegenomicprofiling pages 1-2).

### 2.2 Risk factors for metastasis / progression (from retrieved evidence)
- **Age and survival gradient in de novo metastatic disease:** In a SEER analysis of de novo metastatic breast cancer (2010–2019), 5-year OS declined with age: **≤40 years 42.1%**, **41–60 years 34.8%**, **61–80 years 28.3%**, **>80 years 11.8%** (OpenTargets Search: metastatic breast carcinoma).
- **Metastatic burden and site pattern:** In SEER-based metastatic patterning, multi-organ metastasis—particularly combinations including brain—was associated with the worst survival (e.g., liver+lung+brain median OS 4.0 months) (zhang2025patternsandprognostic pages 1-2, zhang2025patternsandprognostic pages 6-8).

### 2.3 Protective factors
Not directly retrievable from the available sources.

### 2.4 Gene–environment interactions
Not directly retrievable from the available sources.

## 3. Phenotypes
### 3.1 Common metastatic sites and frequencies
SEER-based patterning (2014–2023) reports that among metastatic cases, **bone was most common (21.3%)**, followed by **lung (16.1%)**, **liver (9.2%)**, and **brain (2.9%)** (zhang2025patternsandprognostic pages 1-2). In the same dataset, specific metastatic patterns had reported median OS values, e.g., **bone-only 16.0 months**, **lung-only 14.0**, **liver-only 12.0**, **brain-only 5.0** (zhang2025patternsandprognostic pages 6-8).

Brain metastases are a clinically important complication: an EHR-derived cohort study emphasizes prevalence and survival penalties associated with brain metastases, including lower median OS among patients with brain metastases versus those without (varghese2025epidemiologyandoutcomes pages 1-2).

### 3.2 Phenotype characteristics (onset, progression, frequency)
- **Onset:** Metastatic disease may be present at diagnosis (de novo stage IV) or emerge after earlier-stage treatment; the SEER de novo metastatic cohort comprised **24,155 patients (4.4% of all patients)** diagnosed 2010–2019 (OpenTargets Search: metastatic breast carcinoma).
- **Progression/organotropism by subtype:** Molecular subtypes show distinct organotropism; HR+/HER2− tumors are more prone to bone-only metastasis, whereas HER2-positive and triple-negative subtypes are more likely to involve visceral and brain metastases (zhang2025patternsandprognostic pages 1-2).

### 3.3 Quality-of-life impact
Direct patient-reported outcome instruments (e.g., EQ-5D, SF-36) were not retrievable in the available sources. However, brain metastases are noted to be associated with worse outcomes and limited uptake of guideline-recommended systemic therapies in practice, suggesting substantial morbidity and care gaps (varghese2025epidemiologyandoutcomes pages 1-2).

### 3.4 Suggested HPO terms (examples)
Because HPO mappings were not present explicitly in retrieved sources, the following are suggested mappings consistent with metastatic patterns and clinical manifestations:
- **Metastatic lesion / distant metastasis:** *Metastatic neoplasm* (HP:0003002; candidate)
- **Bone metastasis-related:** bone pain (HP:0002653; candidate), pathological fracture (HP:0002756; candidate)
- **Lung metastasis-related:** dyspnea (HP:0002094; candidate)
- **Liver metastasis-related:** hepatomegaly (HP:0002240; candidate), abnormal liver function tests (HP:0002910; candidate)
- **Brain metastasis-related:** headache (HP:0002315; candidate), seizures (HP:0001250; candidate), focal neurologic deficits (broad)

*(These are ontology suggestions; frequencies for each symptom were not available in the retrieved literature.)*

## 4. Genetic / molecular information
### 4.1 Actionable and recurrent alterations highlighted in retrieved evidence
#### ESR1 (endocrine resistance)
- FDA approval summary describes elacestrant for **ER+/HER2−, ESR1-mutated advanced/metastatic breast cancer** after progression on endocrine therapy (shah2024usfoodand pages 1-2).
- The FDA summary states EMERALD included 228 ESR1-mutated patients and demonstrated PFS benefit in ESR1-mutant subgroup (HR 0.55) (shah2024usfoodand pages 1-2).

#### PI3K/AKT/PTEN axis (endocrine resistance and targeted therapy)
- CAPItello-291 evaluates **AKT inhibition (capivasertib)** added to fulvestrant, motivated by the concept that “AKT pathway activation is implicated in endocrine-therapy resistance” (abstract background) (turner2023capivasertibinhormone media c3df1a43).
- In a real-world comprehensive genomic profiling study, **~60%** of HR+/HER2− metastatic cases in 1st line harbored ≥1 alteration among **ESR1/PIK3CA/AKT1/PTEN** when measured by tissue biopsy or liquid biopsy with sufficient ctDNA tumor fraction (bhave2024comprehensivegenomicprofiling pages 1-2).

### 4.2 Prevalence across treatment lines (real-world)
In HR+/HER2− metastatic breast cancer:
- **ESR1 mutations** in 1st line: **8.1%** (tissue biopsy), **17.5%** (liquid biopsy, ctDNA tumor fraction ≥1%), **4.9%** (liquid biopsy, tumor fraction <1%), rising to **59%** in 3rd line (liquid biopsy, tumor fraction ≥1%) (bhave2024comprehensivegenomicprofiling pages 1-2).

### 4.3 Somatic vs germline
The retrieved evidence emphasizes **somatic acquired ESR1** mutations (endocrine resistance) (shah2024usfoodand pages 1-2, bhave2024comprehensivegenomicprofiling pages 1-2). Germline predisposition genes (e.g., BRCA1/2, PALB2) were not characterized in detail within the evidence snippets obtained here.

### 4.4 Epigenetics and chromosomal abnormalities
Not directly retrievable from the available sources.

## 5. Environmental information
Not directly retrievable from the available sources.

## 6. Mechanism / pathophysiology
### 6.1 Causal chains emphasized in retrieved evidence
1. **Endocrine therapy pressure (HR+ disease)** → selection/emergence of **ESR1 mutations** → endocrine resistance → disease progression requiring therapy switch (shah2024usfoodand pages 1-2, bhave2024comprehensivegenomicprofiling pages 1-2).
2. **PI3K/AKT/PTEN pathway activation** contributes to endocrine resistance → **AKT inhibition (capivasertib)** can restore/improve control when combined with fulvestrant (turner2023capivasertibinhormone media c3df1a43, turner2023capivasertibinhormone media 7aa4aaf1).
3. **Brain metastasis development** in metastatic course → worsened OS and a care gap where many patients do not receive guideline-recommended systemic regimens (varghese2025epidemiologyandoutcomes pages 1-2).

### 6.2 Pathway and ontology term suggestions
- **PI3K/AKT signaling:** GO:0014065 (phosphatidylinositol 3-kinase signaling; candidate)
- **AKT signaling:** GO:0043491 (protein kinase B signaling; candidate)
- **Estrogen receptor signaling:** GO:0030520 (intracellular estrogen receptor signaling pathway; candidate)
- **Metastatic dissemination:** GO:0001837 (epithelial to mesenchymal transition; candidate), GO:0016477 (cell migration; candidate)

### 6.3 Cell types (Cell Ontology; examples)
- Breast epithelial cell / mammary gland epithelial cell (CL term candidates)
- Circulating tumor cell (CL:0001063; candidate)
- Tumor-associated macrophage (broad immune cell involvement; candidate)

*(Specific single-cell/spatial transcriptomic findings were not retrievable in this run.)*

## 7. Anatomical structures affected
### 7.1 Organ-level targets (from metastatic patterns)
Common distant sites include:
- **Bone** (most common) (zhang2025patternsandprognostic pages 1-2)
- **Lung** (zhang2025patternsandprognostic pages 1-2)
- **Liver** (zhang2025patternsandprognostic pages 1-2)
- **Brain** (less frequent, but high impact) (zhang2025patternsandprognostic pages 1-2, varghese2025epidemiologyandoutcomes pages 1-2)

### 7.2 UBERON term suggestions (examples)
- Bone tissue (UBERON:0002481; candidate)
- Lung (UBERON:0002048; candidate)
- Liver (UBERON:0002107; candidate)
- Brain (UBERON:0000955; candidate)

## 8. Temporal development
### 8.1 Onset patterns
- De novo metastatic breast cancer represented **4.4%** of cases in one SEER de novo metastasis cohort (2010–2019) (OpenTargets Search: metastatic breast carcinoma).

### 8.2 Progression and metastatic burden
In the SEER metastatic-pattern analysis, increasing metastatic burden correlated with worse median OS, e.g., **single-site median OS 15.0 months**, **double-site 12.0 months**, and specific multi-organ combinations including brain reaching **median OS 4.0 months** (zhang2025patternsandprognostic pages 6-8).

## 9. Inheritance and population
### 9.1 Epidemiology and outcomes (registry/EHR)
- **Metastatic site distribution (metastatic cases):** bone 21.3%, lung 16.1%, liver 9.2%, brain 2.9% (SEER 2014–2023 analysis) (zhang2025patternsandprognostic pages 1-2).
- **Age-stratified survival in de novo metastatic breast cancer:** 5-year OS 42.1% (≤40), 34.8% (41–60), 28.3% (61–80), 11.8% (>80) (OpenTargets Search: metastatic breast carcinoma).
- **Brain metastases in EHR cohort:** prevalence at metastatic diagnosis 12.5% (HER2+) vs 1.7% (HER2−); median OS from metastatic diagnosis 24 vs 37 months (HER2+) and 12 vs 27 months (HER2−) for patients with vs without brain metastases (varghese2025epidemiologyandoutcomes pages 1-2).

### 9.2 Inheritance
Hereditary breast cancer genetics (inheritance patterns, penetrance, founder effects) were not directly retrievable in this run.

## 10. Diagnostics
### 10.1 Biomarker testing and clinical utility (evidence retrieved)
#### ESR1 mutation testing (tissue and liquid biopsy)
- The FDA approval summary notes elacestrant approval is restricted to **ESR1-mutated** ER+/HER2− advanced/metastatic disease; it describes EMERALD as the basis and highlights that post-aromatase inhibitor treatment, **~20–40%** of patients may develop ESR1 mutations (shah2024usfoodand pages 1-2).
- Real-world genomic profiling supports a testing strategy: tissue biopsy CGP at de novo/recurrent diagnosis, followed by liquid biopsy in later lines to detect acquired alterations; reflex tissue testing should be considered when ctDNA tumor fraction is low (bhave2024comprehensivegenomicprofiling pages 1-2).

#### HER2-low definition (diagnostic concept)
A T-DXd synthesis reports HER2-low definition consistent with modern practice: **IHC 1+ or IHC 2+ with negative ISH** (quaquarini2025trastuzumab–deruxtecanforthe pages 3-4).

### 10.2 Imaging / biopsy
Specific imaging performance metrics were not retrievable in this run; however, registry/EHR studies operationalize metastatic site assignment using structured metastasis variables (SEER) and EHR documentation by line-of-therapy (varghese2025epidemiologyandoutcomes pages 1-2, zhang2025patternsandprognostic pages 1-2).

## 11. Outcome / prognosis
### 11.1 Survival by metastatic pattern (SEER)
In a SEER-based metastatic pattern study, median OS differed by site and combinations:
- Bone-only **16.0 months**; lung-only **14.0**; liver-only **12.0**; brain-only **5.0** (zhang2025patternsandprognostic pages 6-8).
- Liver+lung+brain had the **shortest median OS 4.0 months** (zhang2025patternsandprognostic pages 1-2, zhang2025patternsandprognostic pages 6-8).

### 11.2 Population survival improvement post-CDK4/6 inhibitor era (SEER)
A SEER registry analysis comparing pre-2015 vs post-2015 guideline era in HR+/HER2− de novo metastatic breast cancer found an adjusted **~10% reduction in risk of breast cancer-specific death** post-2015 (HR 0.895; p<0.0001) (OpenTargets Search: metastatic breast carcinoma).

## 12. Treatment
### 12.1 Key recent developments (2023–2024 priority) and trial results

A summary table is provided for rapid reference.

| Intervention/Study | Population | Key biomarker/setting | Primary endpoint result (median PFS, HR, p) | OS result | Notable safety | Publication (journal, month/year), PMID/DOI, URL |
|---|---|---|---|---|---|---|
| Capivasertib + fulvestrant; CAPItello-291 | HR+/HER2− advanced breast cancer after relapse/progression on aromatase inhibitor; 708 randomized; 40.8% AKT-pathway altered; 69.1% prior CDK4/6i | PIK3CA/AKT1/PTEN-altered and overall populations | Overall: median PFS 7.2 vs 3.6 mo; HR 0.60 (95% CI 0.51–0.71); P<0.001. AKT-pathway altered: median PFS 7.3 vs 3.1 mo; HR 0.50 (95% CI 0.38–0.65); P<0.001 (turner2023capivasertibinhormone media c3df1a43, turner2023capivasertibinhormone media 7aa4aaf1) | Not reported in gathered evidence | Grade ≥3 rash 12.1% vs 0.3%; grade ≥3 diarrhea 9.3% vs 0.3%; discontinuation 13.0% vs 2.3% (turner2023capivasertibinhormone media c3df1a43, turner2023capivasertibinhormone media 7aa4aaf1) | *N Engl J Med*, Jun 2023; DOI: 10.1056/NEJMoa2214131; https://doi.org/10.1056/NEJMoa2214131 (turner2023capivasertibinhormone media c3df1a43, turner2023capivasertibinhormone media 7aa4aaf1) |
| Sacituzumab govitecan; EVER-132-002 | Asian patients with HR+/HER2− metastatic breast cancer; SG n=166 vs chemotherapy n=165 | Post-chemotherapy HR+/HER2− mBC | Median PFS 4.3 vs 4.2 mo; HR 0.67 (95% CI 0.52–0.87); P=0.0028 (evangelou2025updatesinadvanced pages 3-4) | Median OS 21.0 vs 15.3 mo; HR 0.64 (95% CI 0.47–0.88); P=0.0061 (evangelou2025updatesinadvanced pages 3-4) | Most common grade ≥3 TEAEs: neutropenia, leukopenia, anemia (evangelou2025updatesinadvanced pages 3-4) | *Nature Medicine*, Oct 2024; DOI: 10.1038/s41591-024-03269-z; https://doi.org/10.1038/s41591-024-03269-z (evangelou2025updatesinadvanced pages 3-4) |
| Elacestrant; FDA approval summary based on EMERALD | ER+/HER2− advanced/metastatic breast cancer; 478 randomized, including 228 ESR1-mutant patients | ESR1-mutated disease after ≥1 prior endocrine therapy; first approved oral ER antagonist for ESR1-mutant setting | ESR1-mutant subgroup: PFS HR 0.55 (95% CI 0.39–0.77); P=.0005. ITT: PFS HR 0.70 (95% CI 0.55–0.88); P=.0018. Median PFS not reported in gathered evidence from this source (shah2024usfoodand pages 1-2) | ESR1-mut subgroup OS HR 0.90 (95% CI 0.63–1.30); OS endpoint not met (shah2024usfoodand pages 1-2) | More nausea, vomiting, dyslipidemia with elacestrant (shah2024usfoodand pages 1-2) | *J Clin Oncol*, Apr 2024; DOI: 10.1200/JCO.23.02112; https://doi.org/10.1200/JCO.23.02112 (shah2024usfoodand pages 1-2) |
| Trastuzumab deruxtecan; French nationwide real-world cohort | 5,890 mBC patients initiating T-DXd in France (2010 HER2+ third-line; 1260 HER2+ second-line; 2620 HER2-low second-line) | HER2+ 2L/3L and HER2-low 2L routine care | Non-randomized real-world outcomes study; PFS not reported in gathered evidence | Median OS 30.2 mo (95% CI 28.1–33.5) for HER2+ 3L; not reached for HER2+ 2L; 16.8 mo (95% CI 14.5–NR) for HER2-low 2L (jourdain2024useandoutcomes pages 1-2) | Interstitial lung disease/pneumonitis can be severe; HER2-low patients had higher hospitalization incidence rates for cardiac/respiratory/digestive/hematologic disorders than HER2+ cohorts (jourdain2024useandoutcomes pages 1-2) | *ESMO Open*, Dec 2024; DOI: 10.1016/j.esmoop.2024.104083; https://doi.org/10.1016/j.esmoop.2024.104083 (jourdain2024useandoutcomes pages 1-2) |
| Trastuzumab deruxtecan; single-centre retrospective series | 38 heavily pretreated mBC patients (15 HER2+, 23 HER2-low); included active CNS metastases | Heavily pretreated HER2+ and HER2-low mBC in routine practice | Non-randomized real-world response study; among 33 evaluable patients, ORR 63%, including 9% complete responses (lazaratos2024therealworldclinical pages 1-2) | OS not reported in gathered evidence | No grade 4–5 toxicities; pneumonitis in 4/38 (10.5%): grade 3 in 2, grade 2 in 1, grade 1 in 1; discontinuation in 3 cases (lazaratos2024therealworldclinical pages 1-2) | *Current Oncology*, Dec 2024; DOI: 10.3390/curroncol32010001; https://doi.org/10.3390/curroncol32010001 (lazaratos2024therealworldclinical pages 1-2) |
| SEER registry survival trend after CDK4/6i introduction | 11,467 women with HR+/HER2− de novo mBC; comparison pre-2015 vs post-2015 guideline era | Population-level HR+/HER2− de novo mBC; epidemiology/outcomes, not a treatment trial | Not a PFS trial; adjusted post-2015 vs pre-2015 breast cancer–specific death HR 0.895; P<0.0001 (OpenTargets Search: metastatic breast carcinoma) | Indicates ~10% reduction in risk of breast cancer–specific death post-2015; no significant BCSS change in HR+/HER2+ comparator population (OpenTargets Search: metastatic breast carcinoma) | Not reported in gathered evidence | *Breast Cancer Research and Treatment*, Aug 2024; DOI: 10.1007/s10549-024-07469-6; https://doi.org/10.1007/s10549-024-07469-6 (OpenTargets Search: metastatic breast carcinoma) |
| De novo metastatic breast cancer by age; SEER | 24,155 de novo metastatic breast cancer patients (2010–2019) | Epidemiology/outcomes by age group, not a trial | Not applicable | 5-year OS: young ≤40 y 42.1%; 41–60 y 34.8%; 61–80 y 28.3%; >80 y 11.8%. Mortality worse vs young: middle-aged aHR 1.18, older 1.42, oldest old 2.15 (OpenTargets Search: metastatic breast carcinoma) | Not reported in gathered evidence | *Frontiers in Endocrinology*, Nov 2023; DOI: 10.3389/fendo.2023.1184895; https://doi.org/10.3389/fendo.2023.1184895 (OpenTargets Search: metastatic breast carcinoma) |
| Brain metastases in mBC; US EHR cohort | 12,644 patients with mBC in US oncology EHR data; HER2+ and HER2− cohorts | Epidemiology/outcomes for brain metastases, not a trial | Not applicable | Median OS from mBC diagnosis with vs without BM: HER2+ 24 vs 37 mo; HER2− 12 vs 27 mo. BM prevalence at mBC diagnosis: HER2+ 12.5%, HER2− 1.7% (varghese2025epidemiologyandoutcomes pages 1-2) | Most patients with BM were not receiving NCCN-recommended systemic therapies; first-line uptake 25.0% in HER2+ BM vs 12.8% in HER2− BM (varghese2025epidemiologyandoutcomes pages 1-2) | *BMC Cancer*, Oct 2025; DOI: 10.1186/s12885-025-14786-6; https://doi.org/10.1186/s12885-025-14786-6 (varghese2025epidemiologyandoutcomes pages 1-2) |


*Table: This table summarizes pivotal 2023–2024 trials and selected registry/real-world studies relevant to metastatic breast carcinoma, emphasizing efficacy, survival, and safety outcomes. It is useful for quickly comparing biomarker-defined treatment evidence with real-world epidemiology and outcome data.*

#### 12.1.1 Targeting PI3K/AKT/PTEN axis: Capivasertib + fulvestrant (CAPItello-291)
CAPItello-291 (NCT04305496) showed statistically significant PFS improvements:
- Overall: **median PFS 7.2 vs 3.6 months; HR 0.60 (95% CI 0.51–0.71); P<0.001** (turner2023capivasertibinhormone media c3df1a43).
- AKT pathway–altered: **median PFS 7.3 vs 3.1 months; HR 0.50 (95% CI 0.38–0.65); P<0.001** (turner2023capivasertibinhormone media 7aa4aaf1).
Notable grade ≥3 AEs included rash and diarrhea; discontinuations were higher in the capivasertib arm (turner2023capivasertibinhormone media c3df1a43).

#### 12.1.2 Antibody–drug conjugate for HR+/HER2− metastatic disease: Sacituzumab govitecan (EVER-132-002)
EVER-132-002 (NCT04639986) reported:
- **PFS HR 0.67** with median **4.3 vs 4.2 months** (P=0.0028)
- **OS HR 0.64** with median **21.0 vs 15.3 months** (P=0.0061)
with common grade ≥3 hematologic toxicities (evangelou2025updatesinadvanced pages 3-4).

#### 12.1.3 ESR1-mutated ER+/HER2−: Elacestrant (FDA approval summary of EMERALD)
From the FDA approval summary:
- ESR1-mutant subgroup PFS benefit: **HR 0.55 (95% CI 0.39–0.77); P=.0005**
- OS endpoint not met; no OS detriment signal: **HR 0.90 (95% CI 0.63–1.30)**
- More nausea, vomiting, dyslipidemia with elacestrant (shah2024usfoodand pages 1-2).

#### 12.1.4 HER2-positive and HER2-low metastatic disease: Trastuzumab deruxtecan (T-DXd) real-world implementation
- **French nationwide cohort (ESMO Open 2024):** median OS **30.2 months** in HER2+ third-line and **16.8 months** in HER2-low second-line; brain metastases were common (e.g., 16% in HER2-low second-line cohort). The cohort highlights routine-care populations being older/more comorbid than trials and underscores severe ILD/pneumonitis risk requiring surveillance (jourdain2024useandoutcomes pages 1-2).
- **Single-center series (Current Oncology 2024):** among 33 evaluable patients, ORR **63%** with **10.5% pneumonitis** (including grade 3 cases), no grade 4–5 toxicities (lazaratos2024therealworldclinical pages 1-2).

### 12.2 MAXO term suggestions (examples)
- Endocrine therapy (MAXO: endocrine therapy; candidate)
- Cyclin-dependent kinase inhibitor therapy (MAXO: CDK inhibitor therapy; candidate)
- AKT inhibitor therapy (MAXO: targeted molecular therapy; candidate)
- Antibody–drug conjugate therapy (MAXO: antibody therapy + chemotherapy conjugate; candidate)
- Liquid biopsy testing / ctDNA testing (MAXO: diagnostic procedure; candidate)

*(Exact MAXO identifiers were not retrievable in this run; these are semantic suggestions.)*

## 13. Prevention
Not directly retrievable from the available sources.

## 14. Other species / natural disease
Not directly retrievable from the available sources.

## 15. Model organisms
Not directly retrievable from the available sources.

---

## Direct abstract quotations supporting key claims (selected)
- CAPItello-291 mechanistic rationale: “**AKT pathway activation is implicated in endocrine-therapy resistance**.” (turner2023capivasertibinhormone media c3df1a43)
- EMERALD/elacestrant regulatory conclusion: “**The approval of elacestrant in ER+, HER2– advanced or metastatic breast cancer was restricted to patients with ESR1 mutations**.” (shah2024usfoodand pages 1-2)
- EVER-132-002 conclusion: “**SG demonstrated significant and clinically meaningful improvement in PFS and OS versus chemotherapy, with a manageable safety profile** …” (evangelou2025updatesinadvanced pages 3-4)

## Key real-world/practice gaps highlighted
In a large EHR cohort, “most [patients with brain metastases] were not receiving NCCN Guideline®-recommended systemic therapies,” with poorer OS in those with brain metastases (varghese2025epidemiologyandoutcomes pages 1-2).

## References (URLs and publication dates)
URLs and dates are provided inline in each cited publication row and in the trial table artifact. Key examples include:
- Turner et al., *N Engl J Med*, Jun 2023, CAPItello-291. https://doi.org/10.1056/NEJMoa2214131 (turner2023capivasertibinhormone media c3df1a43, turner2023capivasertibinhormone media 7aa4aaf1)
- Xu et al., *Nature Medicine*, Oct 2024, EVER-132-002. https://doi.org/10.1038/s41591-024-03269-z (evangelou2025updatesinadvanced pages 3-4)
- Shah et al., *J Clin Oncol*, Apr 2024, FDA summary for elacestrant. https://doi.org/10.1200/jco.23.02112 (shah2024usfoodand pages 1-2)
- Jourdain et al., *ESMO Open*, Dec 2024, French nationwide T-DXd cohort. https://doi.org/10.1016/j.esmoop.2024.104083 (jourdain2024useandoutcomes pages 1-2)
- Lazaratos et al., *Current Oncology*, Dec 2024, single-center T-DXd series. https://doi.org/10.3390/curroncol32010001 (lazaratos2024therealworldclinical pages 1-2)

---

### Items not available in retrieved evidence (explicitly)
- Metastatic-breast-carcinoma-specific MONDO ID; ICD-10/ICD-11 codes; MeSH ID; OMIM/Orphanet IDs.
- Detailed environmental/lifestyle risk factors, protective factors.
- Systematic coverage of germline predisposition variants and allele frequencies (ClinVar/gnomAD), epigenetic mechanisms, and animal models.
- Formal diagnostic test performance statistics for imaging modalities.


References

1. (OpenTargets Search: metastatic breast carcinoma): Open Targets Query (metastatic breast carcinoma, 50 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

2. (zhang2025patternsandprognostic pages 1-2): Maoquan zhang, Hanqing Deng, Rihua Hu, Fuwei Chen, Shiwen Dong, Shiyi Zhang, Wenyan Guo, Wen Yang, and Wenxin Chen. Patterns and prognostic implications of distant metastasis in breast cancer based on seer population data. Scientific Reports, Jul 2025. URL: https://doi.org/10.1038/s41598-025-12883-x, doi:10.1038/s41598-025-12883-x. This article has 34 citations and is from a peer-reviewed journal.

3. (zhang2025patternsandprognostic pages 2-4): Maoquan zhang, Hanqing Deng, Rihua Hu, Fuwei Chen, Shiwen Dong, Shiyi Zhang, Wenyan Guo, Wen Yang, and Wenxin Chen. Patterns and prognostic implications of distant metastasis in breast cancer based on seer population data. Scientific Reports, Jul 2025. URL: https://doi.org/10.1038/s41598-025-12883-x, doi:10.1038/s41598-025-12883-x. This article has 34 citations and is from a peer-reviewed journal.

4. (varghese2025epidemiologyandoutcomes pages 1-2): Della Varghese, Jenna Collins, Beth Nordstrom, Miguel Miranda, Brian Murphy, and David Harland. Epidemiology and outcomes associated with brain metastases among patients with metastatic breast cancer – a cohort study in us electronic health record data. BMC Cancer, Oct 2025. URL: https://doi.org/10.1186/s12885-025-14786-6, doi:10.1186/s12885-025-14786-6. This article has 1 citations and is from a peer-reviewed journal.

5. (zhang2025patternsandprognostic pages 8-10): Maoquan zhang, Hanqing Deng, Rihua Hu, Fuwei Chen, Shiwen Dong, Shiyi Zhang, Wenyan Guo, Wen Yang, and Wenxin Chen. Patterns and prognostic implications of distant metastasis in breast cancer based on seer population data. Scientific Reports, Jul 2025. URL: https://doi.org/10.1038/s41598-025-12883-x, doi:10.1038/s41598-025-12883-x. This article has 34 citations and is from a peer-reviewed journal.

6. (turner2023capivasertibinhormone media c3df1a43): Nicholas C. Turner, Mafalda Oliveira, Sacha J. Howell, Florence Dalenc, Javier Cortes, Henry L. Gomez Moreno, Xichun Hu, Komal Jhaveri, Petr Krivorotko, Sibylle Loibl, Serafin Morales Murillo, Meena Okera, Yeon Hee Park, Joohyuk Sohn, Masakazu Toi, Eriko Tokunaga, Samih Yousef, Lyudmila Zhukova, Elza C. de Bruin, Lynda Grinsted, Gaia Schiavon, Andrew Foxley, and Hope S. Rugo. Capivasertib in hormone receptor-positive advanced breast cancer. The New England journal of medicine, 388 22:2058-2070, Jun 2023. URL: https://doi.org/10.1056/nejmoa2214131, doi:10.1056/nejmoa2214131. This article has 832 citations and is from a highest quality peer-reviewed journal.

7. (turner2023capivasertibinhormone media 7aa4aaf1): Nicholas C. Turner, Mafalda Oliveira, Sacha J. Howell, Florence Dalenc, Javier Cortes, Henry L. Gomez Moreno, Xichun Hu, Komal Jhaveri, Petr Krivorotko, Sibylle Loibl, Serafin Morales Murillo, Meena Okera, Yeon Hee Park, Joohyuk Sohn, Masakazu Toi, Eriko Tokunaga, Samih Yousef, Lyudmila Zhukova, Elza C. de Bruin, Lynda Grinsted, Gaia Schiavon, Andrew Foxley, and Hope S. Rugo. Capivasertib in hormone receptor-positive advanced breast cancer. The New England journal of medicine, 388 22:2058-2070, Jun 2023. URL: https://doi.org/10.1056/nejmoa2214131, doi:10.1056/nejmoa2214131. This article has 832 citations and is from a highest quality peer-reviewed journal.

8. (evangelou2025updatesinadvanced pages 3-4): Christos Evangelou. Updates in advanced hormone receptor-positive breast cancer: from circulating tumor dna-guided therapy to precision medicine. American Medical Journal Oncology, pages 40-49, Jul 2025. URL: https://doi.org/10.33590/oncolamj/ctrc4560, doi:10.33590/oncolamj/ctrc4560. This article has 1 citations.

9. (shah2024usfoodand pages 1-2): Mirat Shah, Hima Lingam, Xin Gao, Haley Gittleman, Mallorie H. Fiero, Danielle Krol, Nikolett Biel, Tiffany K. Ricks, Wentao Fu, Salaheldin Hamed, Fang Li, Jillian (Jielin) Sun, Jianghong Fan, Robert Schuck, Manuela Grimstein, Liuya Tang, Shyam Kalavar, Abdelrahmman Abukhdeir, Anand Pathak, Soma Ghosh, Ilynn Bulatao, Amy Tilley, William F. Pierce, Bronwyn D. Mixter, Shenghui Tang, Richard Pazdur, Paul Kluetz, and Laleh Amiri-Kordestani. Us food and drug administration approval summary: elacestrant for estrogen receptor–positive, human epidermal growth factor receptor 2–negative, <i>esr1</i>-mutated advanced or metastatic breast cancer. Journal of Clinical Oncology, 42:1193-1201, Apr 2024. URL: https://doi.org/10.1200/jco.23.02112, doi:10.1200/jco.23.02112. This article has 39 citations and is from a highest quality peer-reviewed journal.

10. (jourdain2024useandoutcomes pages 1-2): H. Jourdain, A. Di Meglio, I. Mansouri, D. Desplas, M. Zureik, and N. Haddy. Use and outcomes of trastuzumab deruxtecan in her2-positive and her2-low metastatic breast cancer in a real-world setting: a nationwide cohort study. ESMO Open, 9:104083, Dec 2024. URL: https://doi.org/10.1016/j.esmoop.2024.104083, doi:10.1016/j.esmoop.2024.104083. This article has 15 citations and is from a domain leading peer-reviewed journal.

11. (lazaratos2024therealworldclinical pages 1-2): Anna-Maria Lazaratos, Matthew Dankner, Aalya Hamouda, Soumaya Labidi, Victor Cohen, Lawrence Panasci, Jennifer E. Friedmann, François Patenaude, Cristiano Ferrario, Mark Basik, April A. N. Rose, and Parvaneh Fallah. The real-world clinical outcomes of heavily pretreated her2+ and her2-low metastatic breast cancer patients treated with trastuzumab deruxtecan at a single centre. Current Oncology, 32:1, Dec 2024. URL: https://doi.org/10.3390/curroncol32010001, doi:10.3390/curroncol32010001. This article has 9 citations.

12. (bhave2024comprehensivegenomicprofiling pages 1-2): Manali A. Bhave, Julia C. F. Quintanilha, Hanna Tukachinsky, Gerald Li, Takara Scott, Jeffrey S. Ross, Lincoln Pasquina, Richard S. P. Huang, Heather McArthur, Mia A. Levy, Ryon P. Graf, and Kevin Kalinsky. Comprehensive genomic profiling of esr1, pik3ca, akt1, and pten in hr(+)her2(−) metastatic breast cancer: prevalence along treatment course and predictive value for endocrine therapy resistance in real-world practice. Breast Cancer Research and Treatment, 207:599-609, Jun 2024. URL: https://doi.org/10.1007/s10549-024-07376-w, doi:10.1007/s10549-024-07376-w. This article has 50 citations and is from a peer-reviewed journal.

13. (zhang2025patternsandprognostic pages 6-8): Maoquan zhang, Hanqing Deng, Rihua Hu, Fuwei Chen, Shiwen Dong, Shiyi Zhang, Wenyan Guo, Wen Yang, and Wenxin Chen. Patterns and prognostic implications of distant metastasis in breast cancer based on seer population data. Scientific Reports, Jul 2025. URL: https://doi.org/10.1038/s41598-025-12883-x, doi:10.1038/s41598-025-12883-x. This article has 34 citations and is from a peer-reviewed journal.

14. (quaquarini2025trastuzumab–deruxtecanforthe pages 3-4): Erica Quaquarini, Federica Luelli, Angioletta Lasagna, Gianpiero Rizzo, Lorenzo Perrone, Simone Figini, Raffaella Achille, and Paolo Pedrazzoli. Trastuzumab–deruxtecan for the treatment of metastatic breast cancer patients: data from real world studies. Cancers, 17:3505, Oct 2025. URL: https://doi.org/10.3390/cancers17213505, doi:10.3390/cancers17213505. This article has 4 citations.
