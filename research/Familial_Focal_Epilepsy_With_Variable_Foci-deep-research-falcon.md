---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-10T14:46:17.111047'
end_time: '2026-05-10T14:56:20.848178'
duration_seconds: 603.74
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Familial Focal Epilepsy With Variable Foci
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 42
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Familial Focal Epilepsy With Variable Foci
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Familial Focal Epilepsy With Variable Foci** covering all of the
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
- **Disease Name:** Familial Focal Epilepsy With Variable Foci
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Familial Focal Epilepsy With Variable Foci** covering all of the
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


# Familial Focal Epilepsy With Variable Foci (FFEVF): Disease Characteristics Research Report

## Executive summary
Familial focal epilepsy with variable foci (FFEVF; **MIM 604364**) is an autosomal dominant familial focal epilepsy in which affected relatives have focal seizures arising from different cortical regions (e.g., temporal, frontal, parietal, occipital), while each individual typically has a consistent focal onset pattern. It is most commonly caused by germline loss-of-function variants in genes encoding the **GATOR1 complex** (DEPDC5, NPRL2, NPRL3), a negative regulator of **mTORC1** signaling, and it shows **incomplete penetrance** and highly variable expressivity. Key real-world implementations include broad epilepsy gene panel/WES testing, epilepsy-protocol MRI and long-term video-EEG, consideration of epilepsy surgery in drug-resistant cases (especially with focal cortical dysplasia), and increased attention to cardiorespiratory peri-ictal monitoring in some DEPDC5-related presentations. (kaur2013noveldepdc5mutations pages 1-4, dibbens2013mutationsindepdc5 pages 1-2, muller2024gator1mutationsimpair pages 1-2, baulac2015familialfocalepilepsy pages 1-4, meletti2024ictalandpostictal pages 1-3, mcginley2024seizurecontroloutcomes pages 1-2)

## 1. Disease information
### 1.1 Overview / definition
- **Definition (clinical):** FFEVF is an autosomal dominant focal epilepsy syndrome notable because family members have seizures originating from **different cortical regions**. (dibbens2013mutationsindepdc5 pages 1-2)
- **Key defining feature:** intrafamilial variability in seizure focus (temporal/frontal/frontotemporal/parietal/occipital) with often **unremarkable structural MRI** in many cases. (dibbens2013mutationsindepdc5 pages 1-2)

### 1.2 Key identifiers
- **OMIM/MIM:**
  - FFEVF: **MIM 604364** (explicitly cited). (kaur2013noveldepdc5mutations pages 1-4)
  - NPRL3-associated subtype: **FFEVF3, OMIM 617118** (explicitly cited in NPRL3-focused report). (hu2023identificationoftwo pages 1-2)
- **MONDO / Orphanet / MeSH / ICD-10/ICD-11:** Not available from the retrieved documents in this run; these should be filled from OMIM/Orphanet/MONDO/MeSH/ICD lookups outside the present evidence set.

### 1.3 Synonyms / alternative names
- “Familial focal epilepsy with variable foci” (FFEVF). (dibbens2013mutationsindepdc5 pages 1-2)
- Subtype naming by gene is used in the literature and clinical genetics (e.g., **FFEVF3** for NPRL3). (hu2023identificationoftwo pages 1-2)

### 1.4 Evidence source type
The content summarized here is derived from **aggregated disease-level resources within peer-reviewed primary literature** (family studies, case series, surgical cohorts) and from recent reviews/analyses, rather than EHR-only sources. (dibbens2013mutationsindepdc5 pages 1-2, baulac2015familialfocalepilepsy pages 1-4, honke2023deephistopathologygenotype–phenotype pages 1-2)

| Item | Details | Key citations (pqac ids) | URL | Publication year |
|---|---|---|---|---|
| Disease name | Familial focal epilepsy with variable foci (FFEVF) is an autosomal dominant familial focal epilepsy characterized by focal seizures arising from different cortical regions in different affected relatives. | (dibbens2013mutationsindepdc5 pages 1-2, kaur2013noveldepdc5mutations pages 1-4, wang2023theclinicalfeatures pages 1-2) | https://doi.org/10.1038/ng.2599 | 2013 |
| Synonyms | Familial focal epilepsy with variable foci; focal epilepsy with variable foci; FFEVF; FFEVF3 (for NPRL3-related subtype); earlier literature also refers to the same syndrome as FPEVF/partial epilepsy with variable foci. | (dibbens2013mutationsindepdc5 pages 1-2, hu2023identificationoftwo pages 1-2, wang2023theclinicalfeatures pages 1-2) | https://doi.org/10.3389/fgene.2022.1054567 | 2023 |
| OMIM / MIM phenotype numbers | MIM 604364 is explicitly cited for FFEVF; OMIM 617118 is explicitly cited for FFEVF3 / NPRL3-associated disease. | (kaur2013noveldepdc5mutations pages 1-4, hu2023identificationoftwo pages 1-2) | https://doi.org/10.1111/cge.12239 | 2013 |
| Inheritance | Autosomal dominant inheritance with incomplete penetrance and variable expressivity are recurrently reported across DEPDC5-, NPRL2-, and NPRL3-related families. | (kaur2013noveldepdc5mutations pages 1-4, yang2024phenotypicandgenotypic pages 1-2, wang2023theclinicalfeatures pages 1-2) | https://doi.org/10.1371/journal.pone.0284924 | 2023 |
| Key gene | **DEPDC5**; identified as a common cause of familial focal epilepsies/FFEVF, including large linked families; many variants are truncating and support haploinsufficiency. | (dibbens2013mutationsindepdc5 pages 1-2, baulac2014geneticsadvancesin pages 6-9, zhang2021phenotypicandgenotypic pages 1-2) | https://doi.org/10.1038/ng.2599 | 2013 |
| Key gene | **NPRL2**; GATOR1 component implicated in FFEVF, including splice-site variants causing aberrant splicing and exon skipping. | (zhang2022asplicingvariation pages 1-2, muller2024gator1mutationsimpair pages 1-2) | https://doi.org/10.1038/s10038-021-00969-z | 2022 |
| Key gene | **NPRL3**; GATOR1 component implicated in FFEVF3, with nonsense, frameshift, splice, deletion, and other loss-of-function variants reported. | (hu2023identificationoftwo pages 1-2, yang2024phenotypicandgenotypic pages 1-2, nouri2024fromalphathalassemiatrait pages 1-2) | https://doi.org/10.3389/fgene.2022.1054567 | 2023 |
| Brief mechanistic note | DEPDC5, NPRL2, and NPRL3 form the **GATOR1** complex, a negative regulator of the amino-acid sensing branch of **mTORC1** signaling; pathogenic variants generally reduce GATOR1 function, leading to mTORC1 hyperactivation. | (muller2024gator1mutationsimpair pages 1-2, hu2023identificationoftwo pages 1-2, wang2023theclinicalfeatures pages 1-2) | https://doi.org/10.3390/ijms25042068 | 2024 |


*Table: This table summarizes the core disease identity, identifiers, inheritance, major genes, and shared GATOR1–mTORC1 mechanism for familial focal epilepsy with variable foci. It is useful as a compact reference for knowledge-base curation grounded only in the cited evidence.*

## 2. Etiology
### 2.1 Primary causal factors
**Genetic (major):** Heterozygous pathogenic variants in **DEPDC5**, and also **NPRL2**/**NPRL3**, are repeatedly implicated in FFEVF and related focal epilepsy spectra. (dibbens2013mutationsindepdc5 pages 1-2, zhang2022asplicingvariation pages 1-2, hu2023identificationoftwo pages 1-2)

**Illustrative primary-literature statement (DEPDC5 discovery):** Dibbens et al. report that exome sequencing identified DEPDC5 mutations in linked FFEVF families and that “Study of families with focal epilepsy that were too small for conventional clinical diagnosis with FFEVF identified DEPDC5 mutations in approximately 12% of families (10/82).” (Nature Genetics; published online 31 Mar 2013; https://doi.org/10.1038/ng.2599) (dibbens2013mutationsindepdc5 pages 1-2)

### 2.2 Risk factors
- **Family history / inherited variants:** autosomal dominant inheritance is typical. (dibbens2013mutationsindepdc5 pages 1-2, kaur2013noveldepdc5mutations pages 1-4)
- **Two-hit biology as risk modifier for malformations:** in DEPDC5-associated focal cortical dysplasia (FCD), evidence supports a “two-hit” model in which a germline DEPDC5 variant plus a second (somatic) DEPDC5 variant in brain tissue may contribute to lesion formation and severe drug-resistant epilepsy. (baulac2015familialfocalepilepsy pages 1-4)

**Environmental risk factors:** Not specifically established for this Mendelian syndrome in the retrieved evidence set.

### 2.3 Protective factors
No validated protective genetic or environmental factors specific to FFEVF were found in the retrieved corpus.

### 2.4 Gene–environment interactions
No direct gene–environment interaction studies specific to FFEVF were found in the retrieved corpus.

## 3. Phenotypes (clinical spectrum)
### 3.1 Core seizure phenotypes
- **Variable cortical foci across relatives:** frontal, temporal, frontotemporal, parietal, occipital regions. (dibbens2013mutationsindepdc5 pages 1-2)
- **Age of onset:** reported to vary from **infancy to adult life**. (dibbens2013mutationsindepdc5 pages 1-2)
- **DEPDC5 cohorts:** in one Nature Genetics family-based series, mean seizure onset with DEPDC5 mutations was **12.5 years** with a wide range (**6 weeks to 52 years**). (dibbens2013mutationsindepdc5 pages 1-2)
- **NPRL3 family example (China):** onset age ranged **4 months to 31 years**, with variable foci (frontal/temporal), variable timing (day/night), and outcomes spanning refractory epilepsy to near seizure freedom. (PLOS ONE; Apr 2023; https://doi.org/10.1371/journal.pone.0284924) (wang2023theclinicalfeatures pages 1-2)
- **NPRL2 variant family:** multiple seizure types including “febrile seizures, infantile spasms, focal seizures, or focal to generalized tonic-clonic seizures.” (Journal of Human Genetics; 2022; https://doi.org/10.1038/s10038-021-00969-z) (zhang2022asplicingvariation pages 1-2)

### 3.2 EEG, imaging, and lesion-associated phenotypes
- **MRI often unremarkable in non-lesional familial presentations** (structural MRI “usually unremarkable” in the large family description). (dibbens2013mutationsindepdc5 pages 1-2)
- **Focal cortical dysplasia (FCD) association (DEPDC5):** Seven patients from four families with truncating DEPDC5 variants had focal epilepsy associated with FCD (types included FCD IIa and FCD I); MRI could be negative/atypical, and favorable surgical outcomes occurred in several patients. (Annals of Neurology; Apr 2015; https://doi.org/10.1002/ana.24368) (baulac2015familialfocalepilepsy pages 1-4)
- **Genotype–histopathology correlation (brain-tissue genetics, 2023):** In a 17-individual surgical cohort, **GATOR1 loss-of-function variants** (DEPDC5 n=7; NPRL3 n=3) were associated with **FCDIIa** and often **subtle/negative MRI** (seven individuals), and 50% showed a vacuolizing phenotype with p62 aggregates in autophagosomes. (Acta Neuropathologica Communications; Nov 2023; https://doi.org/10.1186/s40478-023-01675-x) (honke2023deephistopathologygenotype–phenotype pages 1-2)

### 3.3 Comorbidities / neurodevelopment
- Most affected individuals in the initial Nature Genetics description “typically have normal intellect,” but some relatives can have “intellectual disability, psychiatric disorders … or autism spectrum disorders.” (dibbens2013mutationsindepdc5 pages 1-2)

### 3.4 Cardiorespiratory and SUDEP-relevant phenotypes (recent development)
A 2024 Neurology Genetics cohort study evaluated ictal central apnea (ICA) in focal epilepsy patients undergoing long-term video-EEG with cardiorespiratory polygraphy and found DEPDC5 variants enriched among those with ICA: **5/14 (35%)** of ICA patients had pathogenic DEPDC5 variants vs **0/15** without ICA. In DEPDC5 patients, ICA occurred in **all recorded seizures (n=15)** with apnea durations **20 seconds to >1 minute**, with temporal EEG involvement in all events and severe oxygen desaturation in 2 cases. (Neurology Genetics; Oct 2024; https://doi.org/10.1212/nxg.0000000000200183) (meletti2024ictalandpostictal pages 1-3)

Visual evidence from this paper (pedigrees/variant schematic/clinical table) is available in extracted figure/table crops. (meletti2024ictalandpostictal media 949a04e5, meletti2024ictalandpostictal media 1e3201ae)

### 3.5 Suggested HPO terms (examples)
(ontology suggestions; not exhaustive)
- Focal seizures: **HP:0007359**
- Focal to bilateral tonic-clonic seizures: **HP:0007334**
- Febrile seizures: **HP:0002373**
- Infantile spasms: **HP:0012469**
- Abnormal EEG: **HP:0002353**
- Epileptiform discharges: **HP:0002350**
- Focal cortical dysplasia: **HP:0010636**
- Hemimegalencephaly: **HP:0007315** (noted as part of NPRL3 phenotypic expansion in broader literature; not directly extracted in this run)
- Developmental delay: **HP:0001263**
- Autism: **HP:0000717**

## 4. Genetic / molecular information
### 4.1 Causal genes
Causal genes in this disorder cluster in the **GATOR1 complex**:
- **DEPDC5** (most commonly reported in familial focal epilepsies/FFEVF). (dibbens2013mutationsindepdc5 pages 1-2, baulac2014geneticsadvancesin pages 6-9)
- **NPRL2** (splicing variants reported; functional splicing assays used). (zhang2022asplicingvariation pages 1-2)
- **NPRL3** (nonsense, frameshift, splice, deletion). (hu2023identificationoftwo pages 1-2, nouri2024fromalphathalassemiatrait pages 1-2)

### 4.2 Variant classes and functional consequences
- DEPDC5: multiple nonsense/truncating variants and deletions have been described; the 2014 review notes that “≈two-thirds” are loss-of-function (premature stop/frameshift/splice) with evidence for nonsense-mediated decay in patient lymphoblasts, consistent with **haploinsufficiency**. (Progress in Brain Research; 2014; https://doi.org/10.1016/b978-0-444-63326-2.00007-7) (baulac2014geneticsadvancesin pages 6-9)
- NPRL2: splicing variant c.339+2T>C causes exon skipping (minigene assay) and is linked to FFEVF phenotypes. (zhang2022asplicingvariation pages 1-2)
- NPRL3: truncating variants (e.g., c.954C>A p.Tyr318*; c.1545-1G>C splice) can be inherited from unaffected mothers (illustrating incomplete penetrance). (Frontiers in Genetics; Jan 2023; https://doi.org/10.3389/fgene.2022.1054567) (hu2023identificationoftwo pages 1-2)

### 4.3 Penetrance and expressivity
- Penetrance is explicitly described as **incomplete** and **variable**. (kaur2013noveldepdc5mutations pages 1-4, yang2024phenotypicandgenotypic pages 1-2)
- A family-based estimate cited in a commentary summary of the 2013 discovery work reported penetrance ~66% (69/105) in seven large families (secondary summary of Dibbens/Ishida studies). (kaur2013noveldepdc5mutations pages 1-4)
- For NPRL3, literature review notes “the penetrance of NPRL3-related epilepsy is incomplete.” (Epilepsia Open; 2024; https://doi.org/10.1002/epi4.12856) (yang2024phenotypicandgenotypic pages 1-2)

### 4.4 Genotype–phenotype correlations (selected)
- DEPDC5 variants can present as non-lesional familial focal epilepsy or as focal epilepsy with FCD; in DEPDC5-associated FCD, brain somatic second hits have been detected, consistent with a two-hit lesion model. (baulac2015familialfocalepilepsy pages 1-4)
- Brain-tissue sequencing in FCDII suggests GATOR1 variants correlate with FCDIIa subtype and an autophagy-altered phenotype (p62 aggregates), contrasting with MTOR-associated lesions. (honke2023deephistopathologygenotype–phenotype pages 1-2)

## 5. Environmental information
No consistent non-genetic environmental contributors specific to FFEVF were identified in the retrieved evidence.

## 6. Mechanism / pathophysiology
### 6.1 Current mechanistic model (GATOR1–mTORC1)
GATOR1 (DEPDC5–NPRL2–NPRL3) is a GTPase-activating protein complex regulating mTORC1 in response to amino acids and other upstream signals; epilepsy-associated mutations in GATOR1 subunits are linked to dysregulated mTORC1 activity. (muller2024gator1mutationsimpair pages 1-2, hu2023identificationoftwo pages 1-2)

**Direct abstract quote (cell biology; Feb 2024):** “GATOR1 … controls the activity of mTORC1 … in response to amino acid availability… epilepsy-linked mutations in the NPRL2 subunit … increase basal mTORC1 signal transduction…” and “NPRL2-L105P is a loss-of-function mutation that disrupts protein interactions with NPRL3 and DEPDC5, impairing GATOR1 complex assembly and resulting in high mTORC1 activity…” (Int J Mol Sci; published 8 Feb 2024; https://doi.org/10.3390/ijms25042068) (muller2024gator1mutationsimpair pages 1-2)

### 6.2 From molecular defect to seizures (causal chain; synthesis)
1) Germline loss-of-function variant in DEPDC5/NPRL2/NPRL3 → 2) impaired GATOR1 inhibition → 3) relative mTORC1 hyperactivation → 4) altered neurodevelopmental processes and/or cortical network excitability; in some patients, second-hit/somatic events in brain tissue contribute to focal malformations such as FCD → 5) focal seizure generation with variable anatomic foci within families. Evidence for steps 1–3 is supported by GATOR1 mechanistic studies and genetic association; steps 4–5 are supported by surgical pathology/genetic “two-hit” observations. (muller2024gator1mutationsimpair pages 1-2, baulac2015familialfocalepilepsy pages 1-4, honke2023deephistopathologygenotype–phenotype pages 1-2)

### 6.3 Cellular/tissue processes implicated
- **mTOR pathway activation markers in dysmorphic neurons:** pS6 immunoreactivity is noted as indicating constitutive mTOR pathway activation in FCDII. (honke2023deephistopathologygenotype–phenotype pages 1-2)
- **Autophagy-related phenotype in GATOR1-positive FCDIIa:** 50% vacuolizing phenotype with p62 aggregates in autophagosomes. (honke2023deephistopathologygenotype–phenotype pages 1-2)

### 6.4 Suggested GO / CL terms (examples)
(ontology suggestions)
- GO biological process: “mTOR signaling” (e.g., **GO:0048015**), “autophagy” (e.g., **GO:0006914**), “regulation of synaptic transmission” (broad)
- CL terms: “cortical pyramidal neuron” (broad), “GABAergic interneuron” (broad; mechanistic neurophysiology studies suggest hyperexcitability without direct GABA inhibition changes in some carriers—see below)

### 6.5 Neurophysiology (recent development)
A 2023 multimodal study in DEPDC5/NPRL3 mutation carriers reported no effect on cortical GABAergic receptor-mediated inhibition or GABA concentration by TMS/MRS, but stronger EEG theta and stronger/more synchronous gamma oscillations, interpreted as increased neural entrainment consistent with cortical hyperexcitability mediated by increased mTORC1 signaling. (Orphanet Journal of Rare Diseases; Jan 2023; https://doi.org/10.1186/s13023-022-02600-6) (meletti2024ictalandpostictal pages 1-3)

## 7. Anatomical structures affected
### 7.1 Organ/system
- **Primary system:** central nervous system. (dibbens2013mutationsindepdc5 pages 1-2)

### 7.2 Brain regions (variable by individual/family)
- Temporal, frontal, frontotemporal, parietal, occipital cortical regions. (dibbens2013mutationsindepdc5 pages 1-2)
- In surgical FCD cohorts with GATOR1 variants, lesions often involve the frontal lobe and may be confined to cortical ribbon. (honke2023deephistopathologygenotype–phenotype pages 1-2)

### 7.3 Suggested UBERON terms (examples)
(ontology suggestions)
- Cerebral cortex: **UBERON:0000956**
- Frontal lobe: **UBERON:0001870**
- Temporal lobe: **UBERON:0001874**
- Hippocampus: **UBERON:0001954** (e.g., hippocampal sclerosis noted in a 2024 NPRL3 deletion case). (nouri2024fromalphathalassemiatrait pages 1-2)

## 8. Temporal development
- **Onset:** infancy through adulthood reported; mean onset ~12.5 years in one DEPDC5 series, but range extends to 6 weeks. (dibbens2013mutationsindepdc5 pages 1-2)
- **Course:** highly variable; some patients are near seizure-free on ASMs while others are drug-resistant and may require surgery. (wang2023theclinicalfeatures pages 1-2, baulac2015familialfocalepilepsy pages 1-4)

## 9. Inheritance and population
### 9.1 Inheritance
- Autosomal dominant inheritance with incomplete penetrance and variable expressivity. (dibbens2013mutationsindepdc5 pages 1-2, kaur2013noveldepdc5mutations pages 1-4, yang2024phenotypicandgenotypic pages 1-2)

### 9.2 Epidemiology
FFEVF-specific incidence/prevalence estimates were not found in the retrieved corpus.

For context (epilepsy overall):
- A large 2024 exome-sequencing study introduction states epilepsy prevalence is **4–10 per 1,000 individuals worldwide**. (Nat Neurosci; Oct 2024; https://doi.org/10.1038/s41593-024-01747-8) (anders2024exomesequencingof pages 1-2)
- SUDEP background incidence is cited as **0.22 to 1.2 per 1,000 individuals per year** and may account for up to 17% of deaths among people with epilepsy (general estimate; not specific to FFEVF). (Neurology Genetics; Oct 2024; https://doi.org/10.1212/nxg.0000000000200183) (meletti2024ictalandpostictal pages 1-3)

### 9.3 Demographics / founder effects
No population-specific founder effects for FFEVF variants were extractable from the retrieved text (some shared ancestry is discussed in the 2013 DEPDC5 paper but not fully extracted here). (dibbens2013mutationsindepdc5 pages 1-2)

## 10. Diagnostics
### 10.1 Clinical tests and findings
- **EEG:** abnormal EEG findings are common but variable; examples include epileptiform discharges and slow waves (NPRL3 family report). (wang2023theclinicalfeatures pages 1-2)
- **MRI:** may be normal in many; in lesion-associated cases, epilepsy-protocol MRI and advanced review/post-processing can identify subtle FCD or hippocampal sclerosis (NPRL3 deletion case review). (nouri2024fromalphathalassemiatrait pages 1-2)
- **Long-term video-EEG with cardiorespiratory polygraphy:** recommended/clinically motivated in DEPDC5-related focal epilepsy when ictal apnea is suspected. (meletti2024ictalandpostictal pages 1-3)

### 10.2 Genetic testing
- **WES / epilepsy gene panels:** used to identify germline variants in DEPDC5/NPRL2/NPRL3; trio-WES and targeted pipelines are reported. (hu2023identificationoftwo pages 1-2, zhang2022asplicingvariation pages 1-2)
- **Variant interpretation:** ACMG-guided variant assessment is explicitly mentioned in NPRL3 WES report. (hu2023identificationoftwo pages 1-2)
- **Brain tissue sequencing (selected surgical cases):** brain-derived DNA sequencing can identify somatic “second hits” in FCD contexts. (baulac2015familialfocalepilepsy pages 1-4, honke2023deephistopathologygenotype–phenotype pages 1-2)

### 10.3 Differential diagnosis
Differential diagnoses include other genetic focal epilepsies and malformations of cortical development (e.g., MTOR-pathway focal cortical dysplasia not driven by GATOR1). (honke2023deephistopathologygenotype–phenotype pages 1-2)

## 11. Outcomes / prognosis
### 11.1 Drug resistance
- A DEPDC5-focused 2024 cohort (ictal apnea study) reported drug resistance in 4/5 DEPDC5 patients. (meletti2024ictalandpostictal pages 1-3)
- DEPDC5-related FCD family series emphasized drug-resistant focal epilepsy in all seven reported patients. (baulac2015familialfocalepilepsy pages 1-4)

### 11.2 Surgical outcomes (real-world implementation)
- DEPDC5-FCD family series: after surgery, multiple patients achieved seizure freedom or worthwhile improvement; authors conclude surgery is valuable even with normal MRI. (baulac2015familialfocalepilepsy pages 1-4)
- Systematic review / individual patient data (2024): Among 44 DEPDC5-variant patients undergoing surgery, **37/40 (92.5%)** with reported seizure-frequency outcomes improved; **29/38 (78.4%)** undergoing focal resection achieved **Engel class I** postoperatively. (Neuropediatrics; online Dec 2023 / print 2024; https://doi.org/10.1055/a-2213-8584) (mcginley2024seizurecontroloutcomes pages 1-2)

## 12. Treatment
### 12.1 Pharmacotherapy (ASMs)
No FFEVF gene-specific randomized controlled trials were found in the retrieved corpus; management follows standard focal epilepsy approaches.

- Case and cohort evidence supports use of standard ASMs (e.g., levetiracetam, valproate, lamotrigine, carbamazepine, lacosamide), with variable response. (meletti2024ictalandpostictal pages 1-3)
- NPRL2 splicing variant case series reported “a favorable prognosis … in response to vitamin B6 and topiramate” in an infant. (zhang2022asplicingvariation pages 1-2)

**MAXO suggestions (examples):**
- Anti-seizure medication therapy: **MAXO:0000744** (anticonvulsant therapy; approximate)
- Vitamin B6 supplementation: (MAXO term for pyridoxine supplementation)

### 12.2 Surgical and interventional
- For drug-resistant focal epilepsy with DEPDC5 variants and FCD, focal resection is commonly used and frequently beneficial. (mcginley2024seizurecontroloutcomes pages 1-2)

**MAXO suggestions:** epilepsy surgery / focal resection.

### 12.3 Monitoring and SUDEP-risk mitigation
Given evidence that ictal central apnea may be common in some DEPDC5-related seizures and that the cohort authors support respiratory polygraphy during LTVM, implementation includes cardiorespiratory monitoring during presurgical evaluation and consideration of genetic testing in focal epilepsy with unexplained ictal apnea. (meletti2024ictalandpostictal pages 1-3)

## 13. Prevention
No primary prevention strategies specific to FFEVF are established in the retrieved evidence.

Secondary/tertiary prevention in practice includes:
- **Cascade genetic testing and counseling** in families once a pathogenic GATOR1 variant is identified (implied by autosomal dominant inheritance and use of family testing in reports). (hu2023identificationoftwo pages 1-2, dibbens2013mutationsindepdc5 pages 1-2)
- Early identification of drug resistance and timely referral for surgical evaluation in appropriate candidates. (baulac2015familialfocalepilepsy pages 1-4, mcginley2024seizurecontroloutcomes pages 1-2)

## 14. Other species / natural disease
No naturally occurring non-human disease analogs were identified in the retrieved evidence set.

## 15. Model organisms
No organismal model studies were directly extracted in this run; however, mechanistic cellular studies of GATOR1 complex function and mTORC1 regulation provide functional context for epilepsy-associated variants. (muller2024gator1mutationsimpair pages 1-2)

## Recent developments (prioritizing 2023–2024)
1) **Brain-tissue genotype–histopathology**: GATOR1 variants correlate with FCDIIa and autophagy-altered pathology (p62 aggregates) and subtle MRI findings in many cases, supporting integrated molecular neuropathology workflows. (Honke et al., Nov 2023; https://doi.org/10.1186/s40478-023-01675-x) (honke2023deephistopathologygenotype–phenotype pages 1-2)
2) **Cardiorespiratory phenotyping**: ICA enrichment among DEPDC5 pathogenic variant carriers during LTVM suggests new clinical attention to respiratory monitoring and genetic testing in ICA presentations. (Meletti et al., Oct 2024; https://doi.org/10.1212/nxg.0000000000200183) (meletti2024ictalandpostictal pages 1-3, meletti2024ictalandpostictal media 949a04e5)
3) **Surgery outcomes synthesis**: Systematic review indicates high postoperative improvement and substantial Engel class I rates among DEPDC5-variant patients with cortical dysplasia undergoing resection. (McGinley et al., 2024; https://doi.org/10.1055/a-2213-8584) (mcginley2024seizurecontroloutcomes pages 1-2)
4) **Mechanistic refinement**: Cell-signaling work shows epilepsy-linked NPRL2 mutations can disrupt GATOR1 assembly and impair mTORC1 regulation by amino acids and PI3K-dependent growth factor signaling. (Muller et al., Feb 2024; https://doi.org/10.3390/ijms25042068) (muller2024gator1mutationsimpair pages 1-2)
5) **Genomic diagnostic odysseys / syndromic overlap**: A 2024 report highlights that deletions encompassing NPRL3 can co-present with α-thalassemia trait due to regulatory-region overlap, and that delayed diagnosis can occur without early comprehensive genetic assessment. (Nouri et al., Jun 2024; https://doi.org/10.3390/genes15070836) (nouri2024fromalphathalassemiatrait pages 1-2)

## Current applications and real-world implementations
- **Diagnostic pipelines:** epilepsy-protocol MRI + EEG + WES/panels; in surgical cases, brain-tissue sequencing for somatic variants/second hits. (hu2023identificationoftwo pages 1-2, baulac2015familialfocalepilepsy pages 1-4, honke2023deephistopathologygenotype–phenotype pages 1-2)
- **Precision monitoring:** LTVM with cardiorespiratory polygraphy when ictal apnea is suspected, particularly in DEPDC5-related epilepsy. (meletti2024ictalandpostictal pages 1-3)
- **Surgical programs:** focal resection for drug-resistant FCD in DEPDC5 variant carriers, often with good outcomes. (mcginley2024seizurecontroloutcomes pages 1-2)

## Clinical trials (latest; real-world precision-medicine implementation)
**NCT05450822 — “Precision Medicine in the Treatment of Epilepsy” (BrainDrugs-Epilepsy Study; Denmark)**
- **Study type/status:** observational, recruiting; first posted **2022-07-11**, last update posted **2024-04-11**. (NCT05450822 chunk 1)
- **Design:** prospective cohort with multimodal biomarkers (EEG/MRI; subset PET) and ASM initiation with **lamotrigine or levetiracetam**; genetic biomarkers list includes **DEPDC5, NPRL2, NPRL3** (among many). (NCT05450822 chunk 1)
- **URL:** https://clinicaltrials.gov/study/NCT05450822 (derived from NCT ID; trial record text in context) (NCT05450822 chunk 1)

## Limitations of this report (evidence availability)
- Many papers in this corpus do not display PMIDs in the extracted text, so **PMID-based referencing could not be reliably completed** for several key sources despite strong DOI/venue metadata. Claims are therefore cited to the retrieved full-text context IDs and DOIs. (wang2023theclinicalfeatures pages 1-2, meletti2024ictalandpostictal pages 1-3, mcginley2024seizurecontroloutcomes pages 1-2)
- MONDO/Orphanet/MeSH/ICD identifiers were not retrievable with the available tools in this run and should be filled using the specified databases.

## Cited figure/table evidence available
- Meletti et al. 2024 extracted: flowchart/pedigrees/variant schematic and clinical features table. (meletti2024ictalandpostictal media 949a04e5, meletti2024ictalandpostictal media 1e3201ae)


References

1. (kaur2013noveldepdc5mutations pages 1-4): A. Kaur. Novel depdc5 mutations causing familial focal epilepsy with variable foci identified. Clinical Genetics, 84:341-342, Oct 2013. URL: https://doi.org/10.1111/cge.12239, doi:10.1111/cge.12239. This article has 7 citations and is from a peer-reviewed journal.

2. (dibbens2013mutationsindepdc5 pages 1-2): Leanne M Dibbens, Boukje de Vries, Simona Donatello, Sarah E Heron, Bree L Hodgson, Satyan Chintawar, Douglas E Crompton, James N Hughes, Susannah T Bellows, Karl Martin Klein, Petra M C Callenbach, Mark A Corbett, Alison E Gardner, Sara Kivity, Xenia Iona, Brigid M Regan, Claudia M Weller, Denis Crimmins, Terence J O'Brien, Rosa Guerrero-López, John C Mulley, Francois Dubeau, Laura Licchetta, Francesca Bisulli, Patrick Cossette, Paul Q Thomas, Jozef Gecz, Jose Serratosa, Oebele F Brouwer, Frederick Andermann, Eva Andermann, Arn M J M van den Maagdenberg, Massimo Pandolfo, Samuel F Berkovic, and Ingrid E Scheffer. Mutations in depdc5 cause familial focal epilepsy with variable foci. Nature Genetics, 45:546-551, Mar 2013. URL: https://doi.org/10.1038/ng.2599, doi:10.1038/ng.2599. This article has 457 citations and is from a highest quality peer-reviewed journal.

3. (muller2024gator1mutationsimpair pages 1-2): Maéline Muller, Jasmine Bélanger, Imane Hadj-Aissa, Conghao Zhang, Chantelle F. Sephton, and Paul A. Dutchak. Gator1 mutations impair pi3 kinase-dependent growth factor signaling regulation of mtorc1. International Journal of Molecular Sciences, 25:2068, Feb 2024. URL: https://doi.org/10.3390/ijms25042068, doi:10.3390/ijms25042068. This article has 9 citations.

4. (baulac2015familialfocalepilepsy pages 1-4): Stéphanie Baulac, Saeko Ishida, Elise Marsan, Catherine Miquel, Arnaud Biraben, Dang Khoa Nguyen, Doug Nordli, Patrick Cossette, Sylvie Nguyen, Virginie Lambrecq, Mihaela Vlaicu, Maïlys Daniau, Franck Bielle, Eva Andermann, Frederick Andermann, Eric Leguern, Francine Chassoux, and Fabienne Picard. Familial focal epilepsy with focal cortical dysplasia due to depdc5 mutations. Annals of Neurology, 77:675-683, Apr 2015. URL: https://doi.org/10.1002/ana.24368, doi:10.1002/ana.24368. This article has 351 citations and is from a highest quality peer-reviewed journal.

5. (meletti2024ictalandpostictal pages 1-3): Stefano Meletti, Gian Marco Duma, Margherita Burani, Alberto Danieli, Giada Giovannini, Elisa Osanni, Elisa Micalizzi, Fabiana Mambretti, Matteo Pugnaghi, Anna E. Vaudano, and Paolo Bonanni. Ictal and postictal central apnea in <i>depdc5</i> -related epilepsy. Neurology Genetics, Oct 2024. URL: https://doi.org/10.1212/nxg.0000000000200183, doi:10.1212/nxg.0000000000200183. This article has 7 citations.

6. (mcginley2024seizurecontroloutcomes pages 1-2): Christopher McGinley, Saige Teti, Katherine Hofmann, John M. Schreiber, Nathan T. Cohen, William D. Gaillard, and Chima O. Oluigbo. Seizure control outcomes following resection of cortical dysplasia in patients with depdc5 variants: a systematic review and individual patient data analysis. Neuropediatrics, 55:001-008, Nov 2024. URL: https://doi.org/10.1055/a-2213-8584, doi:10.1055/a-2213-8584. This article has 4 citations and is from a peer-reviewed journal.

7. (hu2023identificationoftwo pages 1-2): Junji Hu, Xueping Gao, Longchang Chen, Yuling Kan, Zhaoli Du, Shuangqing Xin, Wenkai Ji, Qiang Yu, and Li-ru Cao. Identification of two rare nprl3 variants in two chinese families with familial focal epilepsy with variable foci 3: ngs analysis with literature review. Frontiers in Genetics, Jan 2023. URL: https://doi.org/10.3389/fgene.2022.1054567, doi:10.3389/fgene.2022.1054567. This article has 10 citations and is from a peer-reviewed journal.

8. (honke2023deephistopathologygenotype–phenotype pages 1-2): Jonas Honke, Lucas Hoffmann, Roland Coras, Katja Kobow, Costin Leu, Tom Pieper, Till Hartlieb, Christian G. Bien, Friedrich Woermann, Thomas Cloppenborg, Thilo Kalbhenn, Ahmed Gaballa, Hajo Hamer, Sebastian Brandner, Karl Rössler, Arnd Dörfler, Stefan Rampp, Johannes R. Lemke, Sara Baldassari, Stéphanie Baulac, Dennis Lal, Peter Nürnberg, and Ingmar Blümcke. Deep histopathology genotype–phenotype analysis of focal cortical dysplasia type ii differentiates between the gator1-altered autophagocytic subtype iia and mtor-altered migration deficient subtype iib. Acta Neuropathologica Communications, Nov 2023. URL: https://doi.org/10.1186/s40478-023-01675-x, doi:10.1186/s40478-023-01675-x. This article has 20 citations and is from a peer-reviewed journal.

9. (wang2023theclinicalfeatures pages 1-2): Yue Wang, Peimin Yu, Guoxing Zhu, Xunyi Wu, Ding Ding, and Zhen Hong. The clinical features of familial focal epilepsy with variable foci and nprl3 gene variant. PLOS ONE, 18:e0284924, Apr 2023. URL: https://doi.org/10.1371/journal.pone.0284924, doi:10.1371/journal.pone.0284924. This article has 1 citations and is from a peer-reviewed journal.

10. (yang2024phenotypicandgenotypic pages 1-2): Dongling Yang, Jinqiu Wang, Zailong Qin, Juntan Feng, Chengyun Mao, Yuyi Chen, Xuelin Huang, and Yiyan Ruan. Phenotypic and genotypic characterization of <i>nprl3</i>‐related epilepsy: two case reports and literature review. Epilepsia Open, 9:33-40, Nov 2024. URL: https://doi.org/10.1002/epi4.12856, doi:10.1002/epi4.12856. This article has 5 citations and is from a peer-reviewed journal.

11. (baulac2014geneticsadvancesin pages 6-9): Stéphanie Baulac. Genetics advances in autosomal dominant focal epilepsies: focus on depdc5. Progress in brain research, 213:123-39, Jan 2014. URL: https://doi.org/10.1016/b978-0-444-63326-2.00007-7, doi:10.1016/b978-0-444-63326-2.00007-7. This article has 43 citations and is from a peer-reviewed journal.

12. (zhang2021phenotypicandgenotypic pages 1-2): Xuan Zhang, Zhaoyang Huang, Jianghong Liu, Mingyu Li, Xiaoling Zhao, Jing Ye, and Yuping Wang. Phenotypic and genotypic characterization of depdc5-related familial focal epilepsy: case series and literature review. Frontiers in Neurology, Jun 2021. URL: https://doi.org/10.3389/fneur.2021.641019, doi:10.3389/fneur.2021.641019. This article has 17 citations and is from a peer-reviewed journal.

13. (zhang2022asplicingvariation pages 1-2): Jia Zhang, Yajun Shen, Zuozhen Yang, Fan Yang, Yang Li, Bo Yu, Wanlin Chen, and Jing Gan. A splicing variation in nprl2 causing familial focal epilepsy with variable foci: additional cases and literature review. Journal of Human Genetics, 67:79-85, Aug 2022. URL: https://doi.org/10.1038/s10038-021-00969-z, doi:10.1038/s10038-021-00969-z. This article has 17 citations and is from a peer-reviewed journal.

14. (nouri2024fromalphathalassemiatrait pages 1-2): Maryam Nabavi Nouri, Lama Alandijani, Kalene van Engelen, Soumitra Tole, Emilie Lalonde, and Tugce B. Balci. From alpha-thalassemia trait to nprl3-related epilepsy: a genomic diagnostic odyssey. Genes, 15:836, Jun 2024. URL: https://doi.org/10.3390/genes15070836, doi:10.3390/genes15070836. This article has 0 citations.

15. (meletti2024ictalandpostictal media 949a04e5): Stefano Meletti, Gian Marco Duma, Margherita Burani, Alberto Danieli, Giada Giovannini, Elisa Osanni, Elisa Micalizzi, Fabiana Mambretti, Matteo Pugnaghi, Anna E. Vaudano, and Paolo Bonanni. Ictal and postictal central apnea in <i>depdc5</i> -related epilepsy. Neurology Genetics, Oct 2024. URL: https://doi.org/10.1212/nxg.0000000000200183, doi:10.1212/nxg.0000000000200183. This article has 7 citations.

16. (meletti2024ictalandpostictal media 1e3201ae): Stefano Meletti, Gian Marco Duma, Margherita Burani, Alberto Danieli, Giada Giovannini, Elisa Osanni, Elisa Micalizzi, Fabiana Mambretti, Matteo Pugnaghi, Anna E. Vaudano, and Paolo Bonanni. Ictal and postictal central apnea in <i>depdc5</i> -related epilepsy. Neurology Genetics, Oct 2024. URL: https://doi.org/10.1212/nxg.0000000000200183, doi:10.1212/nxg.0000000000200183. This article has 7 citations.

17. (anders2024exomesequencingof pages 1-2): Siwei Bassel W. Zaid Quratulain Zulfiqar Elisabetta Alis Chen Abou-Khalil Afawi Ali Amadori Anderson Anders, Siwei Chen, B. Abou-Khalil, Z. Afawi, Q. Z. Ali, Elisabetta Amadori, A. Anderson, Joseph Anderson, Danielle M. Andrade, G. Annesi, M. Arslan, P. Auce, Melanie Bahlo, Mark D. Baker, G. Balagura, S. Balestrini, E. Banks, Carmen Barba, Karen Barboza, F. Bartolomei, N. Bass, L. Baum, Tobias H. Baumgartner, B. Baykan, N. Bebek, F. Becker, C. A. Bennett, A. Beydoun, C. Bianchini, F. Bisulli, D. Blackwood, Ilan Blatt, Ingo Borggräfe, C. Boßelmann, V. Braatz, Harrison Brand, K. Brockmann, Russell J Buono, R. M. Busch, S. Caglayan, L. Canafoglia, Christina Canavati, B. Castellotti, G. Cavalleri, Felecia Cerrato, F. Chassoux, Christina Cherian, S. Cherny, Ching-Lung Cheung, I. Chou, S. Chung, C. Churchhouse, V. Ciullo, Peggy O. Clark, Andrew J. Cole, M. Cosico, P. Cossette, C. Cotsapas, C. Cusick, M. Daly, Lea K. Davis, P. Jonghe, N. Delanty, D. Dennig, C. Depondt, Philippe Derambure, Orrin Devinsky, Lidia Di Vito, Faith B Dickerson, Dennis J. Dlugos, Viola Doccini, Colin P. Doherty, Hany El-Naggar, Colin A. Ellis, Leon Epstein, Meghan Evans, Annika B. Faucon, Yen-Chen Anne Feng, Lisa Ferguson, Thomas N. Ferraro, Izabela Ferreira Da Silva, Lorenzo Ferri, Martha Feucht, M. Fields, Mark Fitzgerald, B. Fonferko-Shadrach, Francesco Fortunato, S. Franceschetti, Jacqueline A. French, E. Freri, Jack M. Fu, Stacey B. Gabriel, M. Gagliardi, A. Gambardella, L. Gauthier, T. Giangregorio, T. Gili, Tracy A. Glauser, Ethan Goldberg, A. Goldman, David B. Goldstein, Tiziana Granata, R. Grant, David A. Greenberg, Renzo Guerrini, Aslı Gundogdu-Eken, Namrata Gupta, Kevin Haas, H. Hakonarson, Garen Haryanyan, Martin Häusler, Manu Hegde, E. Heinzen, Ingo Helbig, Christian Hengsbach, H. Heyne, Shinichi Hirose, Edouard Hirsch, Chen-Jui Ho, Olivia Hoeper, D. Howrigan, Donald Hucks, Po-Chen Hung, M. Iacomino, Yushi Inoue, L. M. Inuzuka, A. Ishii, L. Jehi, Michael R. Johnson, M. Johnstone, Reetta Kälviäinen, Moien Kanaan, Bulent Kara, S. Kariuki, J. Kegele, Y. Kesim, Nathalie Khoueiry-Zgheib, Jean Khoury, Chontelle King, K. M. Klein, G. Kluger, S. Knake, Fernando Kok, Amos D. Korczyn, Rudolf Korinthenberg, Andreas Koupparis, I. Kousiappa, Roland Krause, M. Krenn, H. Krestel, Ilona Krey, W. Kunz, Gerhard Kurlemann, R. Kuzniecky, Patrick Kwan, Maite La Vega-Talbott, A. Labate, Austin Lacey, Dennis Lal, P. Laššuthová, S. Lauxmann, Charlotte Lawthom, Stephanie L. Leech, A. Lehesjoki, J. Lemke, Holger Lerche, G. Lesca, C. Leu, Naomi Lewin, D. Lewis-Smith, Gloria H.-Y. Li, Calwing Liao, L. Licchetta, Chih-Hsiang Lin, Kuang-Lin Lin, T. Linnankivi, Warren Lo, D. Lowenstein, Chelsea Lowther, Laura S. Lubbers, C. Lui, Lúcia I Macedo-Souza, R. Madeleyn, F. Madia, S. Magri, Louis Maillard, L. Marcuse, Paula Marques, A. G. Marson, Abigail G Matthews, Patrick May, Thomas Mayer, W. McArdle, Steven McCarroll, P. McGoldrick, C. McGraw, A. McIntosh, A. McQuillan, K. Meador, D. Mei, V. Michel, J. Millichap, R. Minardi, Martino Montomoli, B. Mostacci, L. Muccioli, H. Muhle, K. Müller-Schlüter, I. Najm, W. Nasreddine, S. Neaves, Bernd A. Neubauer, C. R. Newton, J. Noebels, K. Northstone, Sam Novod, Terence J. O’Brien, Seth Owusu-Agyei, Ç. Özkara, A. Palotie, S. Papacostas, E. Parrini, C. Pato, M. Pato, M. Pendziwiat, P. Pennell, S. Petrovski, W. O. Pickrell, Rebecca Pinsky, D. Pinto, T. Pippucci, F. Piras, F. Piras, A. Poduri, Federica Pondrelli, Danielle Posthuma, R. Powell, Michael D Privitera, Annika Rademacher, F. Ragona, Byron Ramirez-Hamouz, S. Rau, Hillary R. Raynes, M. I. Rees, Brigid M. Regan, A. Reif, E. Reinthaler, S. Rheims, Susan M. Ring, Antonella Riva, E. Rojas, Felix Rosenow, Philippe Ryvlin, Anni Saarela, L. Sadleir, Barış Salman, Andrea Salmon, Vincenzo Salpietro, I. Sammarra, Marcello Scala, Steven C. Schachter, André Schaller, C. Schankin, I. Scheffer, Natascha Schneider, S. Schubert-Bast, A. Schulze-Bonhage, P. Scudieri, L. Sedláčková, Catherine Shain, P. C. Sham, Beth R. Shiedley, S. Siena, G. Sills, S. Sisodiya, J. Smoller, M. Solomonson, G. Spalletta, K. Sparks, Michael R. Sperling, H. Stamberger, Bernhard J. Steinhoff, U. Stephani, K. Sterbova, W. Stewart, Carlotta Stipa, P. Striano, A. Strzelczyk, Rainer Surges, Toshimitsu Suzuki, Mariagrazia Talarico, M. Talkowski, Randip S. Taneja, G. Tanteles, Oskari Timonen, N. Timpson, P. Tinuper, M. Todaro, P. Topaloğlu, Meng-Han Tsai, Birutė Tumienė, D. Turkdoğan, Sibel Uğur-İşeri, A. Utkus, Priya Vaidiswaran, L. Valton, A. van Baalen, M. Vari, Annalisa Vetro, M. Vlčková, Sophie von Brauchitsch, Sarah von Spiczak, Ryan G. Wagner, Nick Watts, Y. Weber, S. Weckhuysen, P. Widdess-Walsh, S. Wiebe, S. Wolf, M. Wolff, S. Wolking, Isaac Wong, R. von Wrede, David Wu, Kazuhiro Yamakawa, Z. Yapıcı, U. Yiş, R. Yolken, Emrah Yücesan, S. Zagaglia, F. Zahnert, Federico Zara, F. Zimprich, Milena Zizovic, G. Zsurka, B. Neale, and S. Berkovic. Exome sequencing of 20,979 individuals with epilepsy reveals shared and distinct ultra-rare genetic risk across disorder subtypes. Nature Neuroscience, 27:1864-1879, Oct 2024. URL: https://doi.org/10.1038/s41593-024-01747-8, doi:10.1038/s41593-024-01747-8. This article has 52 citations and is from a highest quality peer-reviewed journal.

18. (NCT05450822 chunk 1): Gitte Moos Knudsen. Precision Medicine in the Treatment of Epilepsy. Gitte Moos Knudsen. 2022. ClinicalTrials.gov Identifier: NCT05450822