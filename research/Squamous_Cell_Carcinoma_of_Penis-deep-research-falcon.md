---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-10T14:47:39.371876'
end_time: '2026-05-10T15:03:50.367906'
duration_seconds: 971.0
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Squamous Cell Carcinoma of Penis
  mondo_id: ''
  category: ''
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 30
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Squamous Cell Carcinoma of Penis
- **MONDO ID:**  (if available)
- **Category:** 

## Research Objectives

Please provide a comprehensive research report on **Squamous Cell Carcinoma of Penis** covering all of the
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
- **Disease Name:** Squamous Cell Carcinoma of Penis
- **MONDO ID:**  (if available)
- **Category:** 

## Research Objectives

Please provide a comprehensive research report on **Squamous Cell Carcinoma of Penis** covering all of the
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


# Squamous Cell Carcinoma of Penis (Penile Squamous Cell Carcinoma; PSCC) — Disease Characteristics Research Report (2023–2024 prioritized)

## Target Disease
- **Disease name:** Squamous Cell Carcinoma of Penis (Penile squamous cell carcinoma; PSCC)
- **MONDO ID:** **MONDO:0018352** “squamous cell carcinoma of penis” (via OpenTargets disease ontology listing) (OpenTargets Search: penile squamous cell carcinoma)
- **Category:** Malignant neoplasm; genitourinary squamous cell carcinoma

## High-yield quantitative evidence summary
The table below aggregates the most quantitatively specific findings retrieved in this run.

| Domain | Finding | Source | Publication date | URL |
|---|---|---|---|---|
| Epidemiology | PSCC represents approximately **95%** of penile neoplasms; penile neoplasms represent **0–2%** of cancers worldwide (thumma2024acomprehensivereview pages 1-2) | Thumma 2024, *Frontiers in Oncology* | May 2024 | https://doi.org/10.3389/fonc.2024.1375882 |
| Epidemiology | Global penile cancer age-standardized incidence rate in **2020: 0.8 per 100,000**; U.S. incidence **0.38 per 100,000**; mean age at diagnosis **67 years** (mannam2024hpvandpenile pages 1-2) | Mannam 2024, *Pathogens* | Sep 2024 | https://doi.org/10.3390/pathogens13090809 |
| Epidemiology | U.S. burden estimate: **2,100 new cases** and **500 deaths** annually; penile cancer is **<1%** of male cancers in the U.S. (antar2024theevolvingmolecular pages 17-18) | Antar 2024, *Current Oncology* | Nov 2024 | https://doi.org/10.3390/curroncol31110511 |
| Epidemiology | Regional hotspot examples: India up to **3.32/100,000**; Northeast Brazil **6.1/100,000** and **5.7%** of male neoplasms (mannam2024hpvandpenile pages 1-2) | Mannam 2024, *Pathogens* | Sep 2024 | https://doi.org/10.3390/pathogens13090809 |
| HPV association | Approximately **38.5–40%** of penile tumors are HPV-associated; HPV16 is the predominant serotype (mannam2024hpvandpenile pages 1-2) | Mannam 2024, *Pathogens* | Sep 2024 | https://doi.org/10.3390/pathogens13090809 |
| HPV association | Approximately **30–50%** of PSCC cases have prior HPV infection (pagliaro2024therapeutictargetsin pages 1-2) | Pagliaro 2024, *Cancers* | May 2024 | https://doi.org/10.3390/cancers16112086 |
| HPV association | HPV16 accounts for **46%–62.5%** of HPV-associated penile cancers (mannam2024hpvandpenile pages 5-6) | Mannam 2024, *Pathogens* | Sep 2024 | https://doi.org/10.3390/pathogens13090809 |
| Risk factors | Major risk factors include lack of neonatal circumcision, poor genital hygiene, low socioeconomic status, HPV infection, and penile intraepithelial neoplasia (PeIN) (thumma2024acomprehensivereview pages 1-2) | Thumma 2024, *Frontiers in Oncology* | May 2024 | https://doi.org/10.3389/fonc.2024.1375882 |
| Risk factors | Phimosis and HPV infection are emphasized as primary risk factors; high-risk HPV is implicated in up to **50%** of penile cancer cases (fadigas2024immunotherapyinpenile pages 1-2) | Fadigas 2024, *Archivos Españoles de Urología* | Dec 2024 | https://doi.org/10.56434/j.arch.esp.urol.20247710.154 |
| Diagnostics | Diagnosis is based on clinical examination including lymph node palpation followed by **biopsy**; PET-CT may assess deep nodal spread (thumma2024acomprehensivereview pages 1-2) | Thumma 2024, *Frontiers in Oncology* | May 2024 | https://doi.org/10.3389/fonc.2024.1375882 |
| Diagnostics | p16INK4a overexpression in HPV lesions was reported to have **100% specificity** and **100% positive predictive value** for HPV-related disease classification in the cited review summary (mannam2024hpvandpenile pages 1-2) | Mannam 2024, *Pathogens* | Sep 2024 | https://doi.org/10.3390/pathogens13090809 |
| Molecular alterations | In **108** PSCC tumors, the most common somatic alterations were **TP53 46%**, **CDKN2A 26%**, **PIK3CA 25%** (nazha2023comprehensivegenomicprofiling pages 1-2) | Nazha 2023, *Cancer* | Aug 2023 | https://doi.org/10.1002/cncr.34982 |
| Molecular alterations | Reported incidence ranges across studies: **TP53 15–58%** and **CDKN2A 23–54%**; commonly mutated genes include TP53, CDKN2A, NOTCH1, and PIK3CA (pagliaro2024therapeutictargetsin pages 1-2) | Pagliaro 2024, *Cancers* | May 2024 | https://doi.org/10.3390/cancers16112086 |
| Molecular alterations | In HPV-stratified cases (**n=29**), **KMT2C 33%** and **FGF3 amplification 30.8%** were enriched in HPV16/18-positive tumors; **CDKN2A 37.5%** in HPV16/18-negative tumors (nazha2023comprehensivegenomicprofiling pages 1-2) | Nazha 2023, *Cancer* | Aug 2023 | https://doi.org/10.1002/cncr.34982 |
| Biomarkers | In the 108-case genomic cohort, **PD-L1 positive 51%**, **TMB-high 10.7%**, **dMMR/MSI-high 1.1%** (nazha2023comprehensivegenomicprofiling pages 1-2) | Nazha 2023, *Cancer* | Aug 2023 | https://doi.org/10.1002/cncr.34982 |
| Biomarkers | PD-L1 immunohistochemistry positivity across studies was reported as **33–60%** regardless of HPV status; high TMB in **18–20%** overall; one study found **TMB ≥10 mut/Mb in 30.8%** of HPV-related tumors and **0%** of HPV-unrelated tumors (pagliaro2024therapeutictargetsin pages 1-2) | Pagliaro 2024, *Cancers* | May 2024 | https://doi.org/10.3390/cancers16112086 |
| Biomarkers | Stage-stratified PD-L1 tumor-cell positivity (SP142) in a **222-man** cohort: **12.50% (CIS)**, **25.00% (pT1)**, **31.25% (pT2)**, **31.25% (pT3)** (antar2024theevolvingmolecular pages 17-18) | Antar 2024, *Current Oncology* | Nov 2024 | https://doi.org/10.3390/curroncol31110511 |
| Prognosis | HPV-associated subtypes were associated with a **28-fold increased relative risk** of inguinal lymph node involvement (mannam2024hpvandpenile pages 1-2) | Mannam 2024, *Pathogens* | Sep 2024 | https://doi.org/10.3390/pathogens13090809 |
| Nodal staging DSNB | In clinically node-negative invasive PSCC, occult metastases occur in **20–25%** of patients; DSNB is the preferred nodal staging approach in recent EAU/ASCO guidance for selected patients (vreeburg2024neweauascoguideline pages 102-107) | Vreeburg 2024, *Eur J Nucl Med Mol Imaging* | Jan 2024 | https://doi.org/10.1007/s00259-023-06586-6 |
| Nodal staging DSNB | Large-cohort DSNB performance: false-negative rate **8.7% per groin**; **2-year** probability that a negative DSNB becomes false-negative **2.5%** (**1.4% per groin**) (vreeburg2024neweauascoguideline pages 102-107) | Vreeburg 2024, *Eur J Nucl Med Mol Imaging* | Jan 2024 | https://doi.org/10.1007/s00259-023-06586-6 |
| Nodal staging DSNB | Visualization rates improved with late imaging: **39% vs 92%**, **43% vs 92%**; another study reported **93%** visibility at **30 min** and **88%** during dynamic imaging (vreeburg2024neweauascoguideline pages 110-113) | Vreeburg 2024, *Eur J Nucl Med Mol Imaging* | Jan 2024 | https://doi.org/10.1007/s00259-023-06586-6 |
| Nodal staging DSNB | Reported DSNB morbidity: overall postoperative complications **22%**, major complications **3%**; wound infection **10%**, lymphocele **3%**, reoperation **0.5%** (aydin2024minimallyinvasivemanagement pages 2-4) | Aydin 2024, *Cancers* | Aug 2024 | https://doi.org/10.3390/cancers16172935 |
| Key clinical trials | **NCT04224740 (HERCULES/LACOG 0218)**: Phase II, **37** patients; pembrolizumab **200 mg q3w** + cisplatin **70 mg/m² D1** (or carboplatin **AUC 5**) + 5-FU **1000 mg/m²/day D1–4** for **6 cycles**; completed **2023-11-13** (NCT04224740 chunk 1) | LACOG trial record 2020, *ClinicalTrials.gov* | 2020 registry; completed Nov 13, 2023 | https://clinicaltrials.gov/study/NCT04224740 |
| Key clinical trials | **NCT02837042**: Phase II pembrolizumab **200 mg q3w** after prior chemotherapy; enrolled **6** patients; trial terminated for poor accrual (NCT02837042 chunk 1) | Nabell 2016 trial record, *ClinicalTrials.gov* | 2016 registry; results posted Jun 21, 2022 | https://clinicaltrials.gov/study/NCT02837042 |
| Key clinical trials | **NCT06353906 (PRIAM)**: Phase II induction carboplatin **AUC5** + paclitaxel **175 mg/m²** for **3** cycles with pembrolizumab **400 mg** on cycles 1 and 3; primary endpoint pCR; recruiting (NCT06353906 chunk 1) | Netherlands Cancer Institute 2024, *ClinicalTrials.gov* | 2024 registry | https://clinicaltrials.gov/study/NCT06353906 |
| Key clinical trials | **NCT07054307**: Phase I in EGFR-positive advanced/metastatic PSCC; MRG003 **2.0 mg/kg q3w** + HX008 **200 mg q3w**; planned enrollment **10**; recruiting (NCT07054307 chunk 2) | Liu 2026 trial record, *ClinicalTrials.gov* | 2026 registry | https://clinicaltrials.gov/study/NCT07054307 |


*Table: This table compiles high-yield, quantitatively specific facts about penile squamous cell carcinoma across epidemiology, HPV association, diagnostics, molecular biology, nodal staging, and ongoing clinical trials. It is designed as a quick-reference evidence summary using only the provided snippets.*

---

## 1. Disease Information
### 1.1 Definition / overview
Penile cancer is a rare malignancy, and PSCC is the dominant histology. A 2024 review states: “**Neoplasm of the penis is relatively rare in most regions representing 0–2% of cancers worldwide**” and “**Penile Squamous Cell Carcinoma (PSCC) represents approximately 95% of all penile neoplasms**” (thumma2024acomprehensivereview pages 1-2). A 2024 systematic review similarly reports that “**Approximately 95% of PeCa cases are squamous cell carcinomas (SCC)**” (fadigas2024immunotherapyinpenile pages 1-2).

### 1.2 Key identifiers
- **MONDO:** MONDO:0018352 (squamous cell carcinoma of penis) (OpenTargets Search: penile squamous cell carcinoma)
- **Other identifiers (ICD-10/ICD-11/MeSH/OMIM/Orphanet):** Not retrievable from the currently indexed full texts in this tool run; therefore **not reported here** to avoid mislabeling.

### 1.3 Synonyms / alternative names
- Penile squamous cell carcinoma (PSCC) (mannam2024hpvandpenile pages 1-2)
- Penile cancer, penile carcinoma (when specifying SCC histology) (thumma2024acomprehensivereview pages 1-2)

### 1.4 Evidence provenance
The present report is derived from **aggregated** disease-level resources: peer‑reviewed reviews (2023–2024), a large tumor genomic profiling cohort study (2023), and ClinicalTrials.gov trial registry records (nazha2023comprehensivegenomicprofiling pages 1-2, mannam2024hpvandpenile pages 1-2, thumma2024acomprehensivereview pages 1-2, NCT06353906 chunk 1, NCT04224740 chunk 1, NCT02837042 chunk 1).

---

## 2. Etiology
### 2.1 Disease causal factors (mechanistic categories)
PSCC is etiologically heterogeneous and is commonly described as comprising **HPV‑associated** and **HPV‑independent** disease pathways (mannam2024hpvandpenile pages 1-2, pagliaro2024therapeutictargetsin pages 1-2).

### 2.2 Risk factors (human epidemiology/clinical consensus)
**Infectious (HPV):**
- A 2024 HPV-focused review reports “**Approximately 40% of penile tumors are associated with human papillomavirus (HPV) infection**” (abstract wording) (mannam2024hpvandpenile pages 1-2).
- The same review emphasizes HPV16 dominance and provides the HPV16 share among HPV-associated cases (46%–62.5%) (mannam2024hpvandpenile pages 5-6).
- A systematic review notes “**high-risk HPV... implicated in up to 50% of PeCa cases**” (fadigas2024immunotherapyinpenile pages 1-2).

**Genital/dermatologic/clinical:**
- Risk factors summarized in a 2024 review include “**lack of neonatal circumcision, poor genital hygiene, socioeconomic status, history of human papillomavirus (HPV) infection and penile intraepithelial neoplasia (PeIN)**” (thumma2024acomprehensivereview pages 1-2).
- Phimosis is repeatedly highlighted as a major risk factor in contemporary reviews (fadigas2024immunotherapyinpenile pages 1-2, antar2024theevolvingmolecular pages 17-18).

**Behavioral/environmental:**
- Tobacco use and sexual behavior factors (e.g., unsafe sex behavior via HPV transmission) are discussed as risk factors in 2024 summaries (mannam2024hpvandpenile pages 1-2, antar2024theevolvingmolecular pages 17-18).

### 2.3 Protective factors
Protective-factor **effect sizes** (e.g., quantitative risk reduction with circumcision or vaccination) were **not present** in the retrieved evidence set in this run and are therefore not quantified here. However, HPV vaccination is explicitly described as a prevention strategy (see Section 13) (mannam2024hpvandpenile pages 5-6).

### 2.4 Gene–environment interactions
Direct, quantitative GxE interaction studies were **not identified** in the retrieved evidence set for this run. Nevertheless, a biologically plausible interaction is implied by HPV-driven carcinogenesis (viral E6/E7 disruption of tumor suppressors) operating alongside host somatic alterations and immune microenvironment features (mannam2024hpvandpenile pages 5-6, nazha2023comprehensivegenomicprofiling pages 1-2).

---

## 3. Phenotypes
### 3.1 Clinical presentation and key phenotypic features
PSCC can present variably; diagnosis is challenging because of “**variety of clinical presentations**” (mannam2024hpvandpenile pages 1-2). A 2024 review notes that diagnosis often occurs late—“**a common trend is for diagnosis to occur late (stage 4)**” (thumma2024acomprehensivereview pages 1-2). Tumors “**most commonly arise on the glans and inner prepuce**” (thumma2024acomprehensivereview pages 1-2).

**Locoregional spread/lymph nodes:** Lymph node involvement is a common concern; “**Lymph node involvement is a common finding at first presentation**” and careful assessment of nodal disease is emphasized (thumma2024acomprehensivereview pages 1-2). Occult nodal metastasis risk in clinically node-negative invasive disease is estimated at **~20–25%** (vreeburg2024neweauascoguideline pages 102-107).

### 3.2 Suggested HPO terms (examples; not exhaustive)
Because the retrieved sources were largely review-level and did not provide structured HPO mappings, the following are **ontology suggestions** consistent with described clinical manifestations and work-up:
- **Penile lesion / penile neoplasm:** *suggested* **HP:0100608 (Penile abnormality)** (term-family suggestion)
- **Pain:** *suggested* **HP:0012531 (Pain)** (general; site-specific terms may be used if available)
- **Inguinal lymphadenopathy:** *suggested* **HP:0002714 (Inguinal lymphadenopathy)**
- **Sexual dysfunction / erectile dysfunction:** *suggested* **HP:0100639 (Erectile dysfunction)** (QoL impact is emphasized in penile cancer care literature) (thumma2024acomprehensivereview pages 1-2)

*Note:* Formal frequencies per phenotype were not provided in the retrieved sources in this run.

### 3.3 Quality of life impact
A 2024 review highlights that surgery can “**lead to severe decrease of quality of life**” and that many individuals experience major QoL impact (thumma2024acomprehensivereview pages 1-2).

---

## 4. Genetic / Molecular Information
### 4.1 Causal genes (germline)
No single-gene germline causal model for PSCC was supported by the retrieved evidence set in this run. PSCC is primarily a malignancy driven by **somatic** alterations and/or HPV-associated oncogenesis (nazha2023comprehensivegenomicprofiling pages 1-2, mannam2024hpvandpenile pages 5-6).

### 4.2 Somatic genomic landscape (primary tumor profiling)
A large NGS cohort study profiled **108** PSCC tumors and found the most common somatic alterations were **TP53 (46%)**, **CDKN2A (26%)**, and **PIK3CA (25%)** (nazha2023comprehensivegenomicprofiling pages 1-2). This supports recurrent disruption of tumor suppression/cell cycle control (TP53, CDKN2A) and PI3K signaling.

**HPV-stratified differences (subset n=29 with HPV16/18 calls):**
- HPV16/18-positive tumors showed enrichment of **KMT2C mutations (33%)** and **FGF3 amplifications (30.8%)**.
- HPV16/18-negative tumors showed more frequent **CDKN2A mutations (37.5%)**.
These subtype differences are reported in the same 2023 cohort analysis (nazha2023comprehensivegenomicprofiling pages 1-2).

### 4.3 Biomarkers relevant to therapy selection
In the 108-case cohort:
- **PD-L1 positive:** **51%**
- **TMB-high (≥10 mut/Mb):** **10.7%**
- **dMMR/MSI-high:** **1.1%**
(nazha2023comprehensivegenomicprofiling pages 1-2)

A 2024 therapeutic-target review summarizes PD-L1 IHC positivity across studies as **33–60%**, and reports that mismatch repair deficiency/MSI-H is rare; it also notes high TMB in **~18–20%** overall and that one study found **TMB ≥10 mut/Mb in 30.8%** of HPV-related tumors and not in HPV-unrelated tumors (pagliaro2024therapeutictargetsin pages 1-2).

### 4.4 Epigenetic / chromosomal abnormalities
No specific PSCC epigenetic maps or recurrent structural variants were extractable from the retrieved evidence set in this run.

### 4.5 Suggested GO biological processes and CL cell types
**Processes (GO term suggestions consistent with described mechanisms):**
- Viral process / viral gene expression (HPV E6/E7) (mannam2024hpvandpenile pages 5-6)
- Cell cycle dysregulation; regulation of apoptotic signaling (TP53 pathway disruption) (mannam2024hpvandpenile pages 5-6, nazha2023comprehensivegenomicprofiling pages 1-2)
- PI3K/AKT signaling pathway activation (via PIK3CA alterations) (nazha2023comprehensivegenomicprofiling pages 1-2)
- Immune evasion / immune exclusion in tumor microenvironment (fadigas2024immunotherapyinpenile pages 1-2)

**Cell types (CL term suggestions):**
- **Keratinocytes / squamous epithelial cells** (tumor cell of origin)
- **CD8+ T cells**, **FOXP3+ regulatory T cells**, **macrophages (CD163+)** as noted in PSCC immune microenvironment descriptions (fadigas2024immunotherapyinpenile pages 1-2)

---

## 5. Environmental Information
### 5.1 Environmental/lifestyle factors
Reviews list **tobacco use**, hygiene/socioeconomic factors, and sexual behavior risk (as mediated through HPV transmission) (mannam2024hpvandpenile pages 1-2, thumma2024acomprehensivereview pages 1-2, antar2024theevolvingmolecular pages 17-18).

### 5.2 Infectious agents
**High-risk HPV** is the principal infectious contributor. The 2024 HPV-focused review discusses HPV types and states that HPV16 accounts for **46–62.5%** of HPV-associated penile cancers (mannam2024hpvandpenile pages 5-6).

---

## 6. Mechanism / Pathophysiology
### 6.1 HPV-driven carcinogenesis (upstream triggers)
HPV-associated PSCC is driven by viral oncoproteins. The 2024 review summarizes that HPV E6 and E7 “**inhibit p53 and Rb**” (functional description) (mannam2024hpvandpenile pages 5-6). This provides a causal chain from persistent HR-HPV infection → E6/E7 expression → tumor suppressor pathway disruption → uncontrolled proliferation.

### 6.2 Somatic oncogenic pathways (HPV-independent and shared)
Somatic alterations frequently affect TP53, CDKN2A, and PI3K signaling (PIK3CA), consistent with cell-cycle deregulation and growth/survival signaling (nazha2023comprehensivegenomicprofiling pages 1-2). HPV-unrelated tumors are described as having more frequent TP53 mutation/loss and slightly worse prognosis in review synthesis (pagliaro2024therapeutictargetsin pages 1-2).

### 6.3 Immune microenvironment and therapy-relevant biology
A 2024 systematic review describes PSCC as often “**immune excluded**” with stromal enrichment of immune cells, including CD8+ and FOXP3+ cells, and notes higher CD163+ macrophage density in HPV-positive tumors (fadigas2024immunotherapyinpenile pages 1-2). These features motivate investigation of checkpoint inhibitors and combinations (pagliaro2024therapeutictargetsin pages 1-2).

---

## 7. Anatomical Structures Affected
### 7.1 Organ/tissue level
Primary sites commonly include **glans and inner prepuce** (thumma2024acomprehensivereview pages 1-2).

**Regional spread:** predictable stepwise spread to inguinal nodes is emphasized in nodal-management reviews; occult metastases in cN0 invasive cases are ~20–25% (vreeburg2024neweauascoguideline pages 102-107).

### 7.2 Suggested UBERON terms (examples)
- Penis: *suggested* **UBERON:0000989**
- Glans penis: *suggested* UBERON term for glans penis
- Inguinal lymph node: *suggested* **UBERON:0001542** (inguinal lymph node)

---

## 8. Temporal Development
### 8.1 Onset
PSCC is “**most commonly diagnosed in older men**” (review summary) (pagliaro2024therapeutictargetsin pages 1-2), and one review reports mean age at diagnosis **67 years** in the U.S. context (mannam2024hpvandpenile pages 1-2).

### 8.2 Progression / staging-related course
Late presentation is common (“diagnosis… late (stage 4)”) (thumma2024acomprehensivereview pages 1-2). Prognosis is strongly driven by depth of invasion and nodal/metastatic status (mannam2024hpvandpenile pages 1-2).

---

## 9. Inheritance and Population
### 9.1 Epidemiology (recent quantitative points)
- Global penile cancer age-standardized incidence in 2020: **0.8 per 100,000** (mannam2024hpvandpenile pages 1-2).
- U.S. incidence reported as **0.38 per 100,000** (mannam2024hpvandpenile pages 1-2).
- U.S. burden estimate: ~**2,100 new cases** and **500 deaths** annually (antar2024theevolvingmolecular pages 17-18).
- High-incidence examples include India (up to **3.32/100,000**) and Northeast Brazil (**6.1/100,000**; 5.7% of male neoplasms) (mannam2024hpvandpenile pages 1-2).

### 9.2 Genetic inheritance
No Mendelian inheritance pattern is supported for PSCC in the retrieved evidence set; PSCC is primarily sporadic/somatic with infectious contributions (nazha2023comprehensivegenomicprofiling pages 1-2, mannam2024hpvandpenile pages 1-2).

---

## 10. Diagnostics
### 10.1 Clinical and pathology diagnosis
A 2024 review states: “**Diagnosis of PSCC is done through clinical examination… followed by a biopsy, which is essential for the classification**” (thumma2024acomprehensivereview pages 1-2). Nodal evaluation is critical; PET-CT is mentioned as aiding deep-node evaluation (thumma2024acomprehensivereview pages 1-2).

### 10.2 Biomarker/pathology adjuncts
p16INK4a is described as an HPV-associated marker; in one 2024 review summary, p16INK4a is reported as overexpressed in HPV lesions and “**has 100% specificity and positive predictive value**” (mannam2024hpvandpenile pages 1-2).

### 10.3 Lymph node staging innovations (real-world implementations)
The 2023 intercontinental EAU/ASCO update is summarized as recommending **dynamic sentinel node biopsy (DSNB)** as the preferred method for nodal staging in selected patients (≥T1b) (vreeburg2024neweauascoguideline pages 102-107). Quantitative DSNB metrics reported in the 2024 review include a large-cohort false-negative rate of “**8.7% per groin**” and a 2-year probability of a negative DSNB later being a false-negative procedure of **2.5% (1.4% per groin)** (vreeburg2024neweauascoguideline pages 102-107). Reported DSNB morbidity metrics include overall complications **22%** and major complications **3%** in one review summary, with wound infection ~10% and lymphocele ~3% (aydin2024minimallyinvasivemanagement pages 2-4).

---

## 11. Outcome / Prognosis
### 11.1 Prognostic factors
A 2024 review indicates that “tumor size, invasion, nodal status, and metastases are primary prognostic factors” (mannam2024hpvandpenile pages 1-2). HPV-associated histologic subtypes are described as conferring markedly higher nodal involvement risk (a “**28-fold increased relative risk of inguinal lymph node involvement**”) (mannam2024hpvandpenile pages 1-2).

### 11.2 Survival statistics
Robust stage-stratified 5- and 10-year OS/CSS statistics were **not extractable** from the retrieved evidence set in this run; therefore they are not reported to avoid inaccuracies.

---

## 12. Treatment
### 12.1 Standard modalities (current understanding)
A 2024 review states: “**Surgical removal of the tumor is considered the most effective**” but can significantly reduce quality of life; chemotherapy is used for “fixed or bulky lymph nodes… and for distant metastasis,” and radiation therapy is “particularly effective in the case of HPV-positive PSCC” (thumma2024acomprehensivereview pages 1-2). Contemporary therapy reviews note that the systemic backbone for unresectable/metastatic disease remains **cisplatin-based chemotherapy or chemoradiotherapy**, with growing exploration of targeted therapy and immune checkpoint inhibition (pagliaro2024therapeutictargetsin pages 1-2).

### 12.2 Immunotherapy evidence and expert synthesis
A 2024 systematic review emphasizes limited trial-result availability and reports that only one qualifying phase-2 study met inclusion criteria, with an “**objective response rate… 6% across nineteen patients**” (basket of histologies; only 6 penile cases) (fadigas2024immunotherapyinpenile pages 1-2). A 2024 therapeutic-target review concludes that antibody–drug conjugates and ICI combinations are promising directions (pagliaro2024therapeutictargetsin pages 1-2).

### 12.3 Real-world implementations: nodal management
Because outcomes are highly dependent on nodal metastasis, DSNB and minimally invasive approaches to inguinal lymph node management are emphasized as pragmatic strategies to reduce morbidity while improving staging accuracy (vreeburg2024neweauascoguideline pages 102-107, aydin2024minimallyinvasivemanagement pages 2-4).

### 12.4 Active/recent clinical trials (ClinicalTrials.gov; key NCTs)
**Pembrolizumab + chemotherapy combinations:**
- **NCT04224740 (HERCULES; LACOG 0218)**: Phase II, single-group; pembrolizumab 200 mg q3w plus platinum (cisplatin 70 mg/m² D1 or carboplatin AUC 5) + 5‑FU (1000 mg/m²/day D1–4) q3w for 6 cycles; **37** participants; completed 2023‑11‑13 (registry) (NCT04224740 chunk 1).
- **NCT06353906 (PRIAM)**: Phase II induction carboplatin/paclitaxel plus pembrolizumab (400 mg on cycles 1 and 3) for node-positive resectable disease, followed by consolidative surgery and adjuvant pembrolizumab; primary endpoint pCR; recruiting (NCT06353906 chunk 1).

**Single-agent pembrolizumab (advanced PSCC):**
- **NCT02837042**: Phase II pembrolizumab after prior chemotherapy; enrolled **6**; terminated for poor accrual (NCT02837042 chunk 1).

**EGFR-directed antibody–drug conjugate + PD-1 combinations (emerging targeted therapy):**
- **NCT07054307**: Phase I in EGFR-positive unresectable/metastatic PSCC; MRG003 (EGFR-ADC) + HX008 (PD‑1); planned n=10; recruiting (NCT07054307 chunk 2).
- **NCT07518979**: Phase II neoadjuvant EGFR-ADC (becotatug vedotin) + PD‑1 inhibitor (pucotenlimab) in advanced PSCC with penile-preservation difficulty or regional nodal metastasis; not yet recruiting (estimated start 2026) (NCT07518979 chunk 1).

### 12.5 Suggested MAXO terms (examples)
- **Surgical excision / penectomy / glansectomy** (local control) (thumma2024acomprehensivereview pages 1-2)
- **Radiotherapy** (organ preservation; HPV-associated radiosensitivity discussion) (thumma2024acomprehensivereview pages 1-2, mannam2024hpvandpenile pages 5-6)
- **Chemotherapy (cisplatin-based)** (advanced disease) (thumma2024acomprehensivereview pages 1-2, NCT04224740 chunk 1)
- **Immune checkpoint inhibitor therapy (anti–PD‑1)** (trialed/ongoing) (NCT02837042 chunk 1, NCT04224740 chunk 1)
- **Sentinel lymph node biopsy / lymph node dissection** (staging/management) (vreeburg2024neweauascoguideline pages 102-107)

---

## 13. Prevention
### 13.1 Primary prevention
**HPV vaccination:** A 2024 review notes prophylactic vaccines protecting against high-risk HPV16/18 (e.g., Gardasil 9) and states ACIP recommends vaccination for boys aged 11–12 with catch-up through 21 (mannam2024hpvandpenile pages 5-6). Given the fraction of PSCC that is HPV-associated (≈38.5–40% in one review), vaccination is a plausible population-level prevention lever (mannam2024hpvandpenile pages 1-2).

### 13.2 Secondary prevention
No population-wide screening program evidence was extractable from this run; however, timely clinical evaluation and biopsy-based diagnosis are emphasized (thumma2024acomprehensivereview pages 1-2).

---

## 14. Other Species / Natural Disease
No naturally occurring veterinary PSCC analogs or zoonotic considerations were identified in the retrieved evidence set in this run.

---

## 15. Model Organisms
No model organism systems (genetically engineered mouse models, organoids, etc.) were identified in the retrieved evidence set in this run.

---

# Notes on evidence gaps (transparent limitations)
1. **ICD/MeSH/OMIM/Orphanet identifiers** were not extractable from the retrieved full texts in this run; only MONDO identifiers were obtained through an ontology resource (OpenTargets). (OpenTargets Search: penile squamous cell carcinoma)
2. **Stage-stratified survival outcomes** (e.g., 5-year OS/CSS by stage) were not present in the retrieved evidence set and thus are not provided.
3. **Protective-factor effect sizes** (circumcision/vaccination quantitative risk reduction) and **gene–environment interaction** studies were not identified in the retrieved evidence set.

# Retrieved visual evidence
A table image summarizing approximate frequencies of PSCC histologic subtypes was retrieved from Thumma et al. 2024 (Frontiers in Oncology) and can be used for knowledge-base subtype frequency curation (thumma2024acomprehensivereview media 89cd9d95).

References

1. (OpenTargets Search: penile squamous cell carcinoma): Open Targets Query (penile squamous cell carcinoma, 0 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

2. (thumma2024acomprehensivereview pages 1-2): Nishanth Thumma, Neharaj Pitla, Vasavi Gorantla, and Maira du Plessis. A comprehensive review of current knowledge on penile squamous cell carcinoma. Frontiers in Oncology, May 2024. URL: https://doi.org/10.3389/fonc.2024.1375882, doi:10.3389/fonc.2024.1375882. This article has 21 citations.

3. (mannam2024hpvandpenile pages 1-2): Gowtam Mannam, Justin W. Miller, Jeffrey S. Johnson, Keerthi Gullapalli, Adnan Fazili, Philippe E. Spiess, and Jad Chahoud. Hpv and penile cancer: epidemiology, risk factors, and clinical insights. Pathogens, 13:809, Sep 2024. URL: https://doi.org/10.3390/pathogens13090809, doi:10.3390/pathogens13090809. This article has 26 citations.

4. (antar2024theevolvingmolecular pages 17-18): Ryan Michael Antar, Christopher Fawaz, Diego Gonzalez, Vincent Eric Xu, Arthur Pierre Drouaud, Jason Krastein, Faozia Pio, Andeulazia Murdock, Kirolos Youssef, Stanislav Sobol, and Michael J. Whalen. The evolving molecular landscape and actionable alterations in urologic cancers. Current Oncology, 31:6909-6937, Nov 2024. URL: https://doi.org/10.3390/curroncol31110511, doi:10.3390/curroncol31110511. This article has 6 citations.

5. (pagliaro2024therapeutictargetsin pages 1-2): Lance C Pagliaro, Burak Tekin, Sounak Gupta, and Loren P Herrera Hernandez. Therapeutic targets in advanced penile cancer: from bench to bedside. Cancers, 16:2086, May 2024. URL: https://doi.org/10.3390/cancers16112086, doi:10.3390/cancers16112086. This article has 15 citations.

6. (mannam2024hpvandpenile pages 5-6): Gowtam Mannam, Justin W. Miller, Jeffrey S. Johnson, Keerthi Gullapalli, Adnan Fazili, Philippe E. Spiess, and Jad Chahoud. Hpv and penile cancer: epidemiology, risk factors, and clinical insights. Pathogens, 13:809, Sep 2024. URL: https://doi.org/10.3390/pathogens13090809, doi:10.3390/pathogens13090809. This article has 26 citations.

7. (fadigas2024immunotherapyinpenile pages 1-2): Filipe Fadigas, Diana Martins, and Fernando Mendes. Immunotherapy in penile cancer: a systematic review. Archivos espanoles de urologia, 77 10:1102-1111, Dec 2024. URL: https://doi.org/10.56434/j.arch.esp.urol.20247710.154, doi:10.56434/j.arch.esp.urol.20247710.154. This article has 0 citations.

8. (nazha2023comprehensivegenomicprofiling pages 1-2): Bassel Nazha, Tony Zhuang, Sharon Wu, Jacqueline T. Brown, Daniel Magee, Bradley C. Carthon, Omer Kucuk, Chadi Nabhan, Pedro C. Barata, Elisabeth I. Heath, Charles J. Ryan, Rana R. McKay, Viraj A. Master, and Mehmet Asim Bilen. Comprehensive genomic profiling of penile squamous cell carcinoma and the impact of human papillomavirus status on immune‐checkpoint inhibitor‐related biomarkers. Cancer, 129:3884-3893, Aug 2023. URL: https://doi.org/10.1002/cncr.34982, doi:10.1002/cncr.34982. This article has 45 citations and is from a domain leading peer-reviewed journal.

9. (vreeburg2024neweauascoguideline pages 102-107): Manon T. A. Vreeburg, Maarten L. Donswijk, Maarten Albersen, Arie Parnham, Benjamin Ayres, Chris Protzel, Curtis Pettaway, Philippe E. Spiess, and Oscar R. Brouwer. New eau/asco guideline recommendations on sentinel node biopsy for penile cancer and remaining challenges from a nuclear medicine perspective. European journal of nuclear medicine and molecular imaging, 51:2861-2868, Jan 2024. URL: https://doi.org/10.1007/s00259-023-06586-6, doi:10.1007/s00259-023-06586-6. This article has 7 citations and is from a highest quality peer-reviewed journal.

10. (vreeburg2024neweauascoguideline pages 110-113): Manon T. A. Vreeburg, Maarten L. Donswijk, Maarten Albersen, Arie Parnham, Benjamin Ayres, Chris Protzel, Curtis Pettaway, Philippe E. Spiess, and Oscar R. Brouwer. New eau/asco guideline recommendations on sentinel node biopsy for penile cancer and remaining challenges from a nuclear medicine perspective. European journal of nuclear medicine and molecular imaging, 51:2861-2868, Jan 2024. URL: https://doi.org/10.1007/s00259-023-06586-6, doi:10.1007/s00259-023-06586-6. This article has 7 citations and is from a highest quality peer-reviewed journal.

11. (aydin2024minimallyinvasivemanagement pages 2-4): Ahmet Murat Aydin, Emily Biben, Alice Yu, Nicholas H. Chakiryan, Reza Mehrazin, and Philippe E. Spiess. Minimally invasive management of inguinal lymph nodes in penile cancer: recent progress and remaining challenges. Cancers, 16:2935, Aug 2024. URL: https://doi.org/10.3390/cancers16172935, doi:10.3390/cancers16172935. This article has 6 citations.

12. (NCT04224740 chunk 1):  Pembrolizumab Combined With Cisplatin-based Chemotherapy as First-line Systemic Therapy in Advanced Penile Cancer. Latin American Cooperative Oncology Group. 2020. ClinicalTrials.gov Identifier: NCT04224740

13. (NCT02837042 chunk 1): Lisle Nabell. Trial of Pembrolizumab for Advanced Penile Squamous Cell Carcinoma. University of Alabama at Birmingham. 2016. ClinicalTrials.gov Identifier: NCT02837042

14. (NCT06353906 chunk 1):  Carboplatin/Paclitaxel + Pembrolizumab for Locoregionally Advanced Penile Cancer. The Netherlands Cancer Institute. 2024. ClinicalTrials.gov Identifier: NCT06353906

15. (NCT07054307 chunk 2): Jiyan Liu. MRG003 Plus HX008 as First-Line Treatment for EGFR-Positive Locally Advanced or Metastatic Penile Squamous Cell Carcinoma. Jiyan Liu. 2026. ClinicalTrials.gov Identifier: NCT07054307

16. (NCT07518979 chunk 1): Jiyan Liu. EGFR-ADC (Becotatug Vedotin) Combined With PD-1 Inhibitor (Pucotenlimab) in Neoadjuvant Treatment of Advanced Penile Cancer. Jiyan Liu. 2026. ClinicalTrials.gov Identifier: NCT07518979

17. (thumma2024acomprehensivereview media 89cd9d95): Nishanth Thumma, Neharaj Pitla, Vasavi Gorantla, and Maira du Plessis. A comprehensive review of current knowledge on penile squamous cell carcinoma. Frontiers in Oncology, May 2024. URL: https://doi.org/10.3389/fonc.2024.1375882, doi:10.3389/fonc.2024.1375882. This article has 21 citations.