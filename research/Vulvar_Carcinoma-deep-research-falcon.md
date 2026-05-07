---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-07T15:00:50.520019'
end_time: '2026-05-07T15:26:17.300658'
duration_seconds: 1526.78
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Vulvar Carcinoma
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

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Vulvar Carcinoma
- **MONDO ID:**  (if available)
- **Category:** 

## Research Objectives

Please provide a comprehensive research report on **Vulvar Carcinoma** covering all of the
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
- **Disease Name:** Vulvar Carcinoma
- **MONDO ID:**  (if available)
- **Category:** 

## Research Objectives

Please provide a comprehensive research report on **Vulvar Carcinoma** covering all of the
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


# Vulvar Carcinoma (Vulvar Cancer): Disease Characteristics Research Report

## Target Disease
- **Disease name:** Vulvar carcinoma (vulvar cancer)
- **Category:** Malignant neoplasm of the vulva (female genital tract cancer)
- **MONDO ID:** Not available from the retrieved sources in this run (would require dedicated ontology lookup).

---

## 1. Disease Information

### Overview (what is the disease?)
Vulvar carcinoma is an uncommon malignant tumor arising in vulvar tissues; **vulvar squamous cell carcinoma (VSCC)** is the predominant histologic subtype (≈90% of vulvar cancers in multiple reviews). (corte2024currentpreoperativemanagement pages 1-2)

### Key identifiers and terminologies
- **ICD-10:** **C51 (vulval/vulvar cancer)** is explicitly used in health system cost and epidemiology analyses. (steinkasserer2023characterizationofpatients pages 1-2)
- **ICD-O-3 site coding:** HPV-related cancer epidemiology work referenced **ICD-O-3 site codes including C51.0** for vulvar cancer. (adekanmbi2024humanpapillomavirusvaccination pages 1-2)
- **MeSH (term):** A 2024 imaging review searched PubMed using MeSH terms including **“vulval neoplasm”** (and “diagnostic imaging”). (ha2024imaginginvulval pages 1-2)
- **FIGO staging:** The **FIGO 2021 revision** is data-derived and explicitly **allows incorporation of cross-sectional imaging findings** into staging. (olawaiye2021figostagingfor pages 1-2)

### Common synonyms / alternative names
- Vulvar carcinoma; vulval cancer; vulvar cancer; vulvar squamous cell carcinoma (VSCC) (dominant histology). (corte2024currentpreoperativemanagement pages 1-2)

### Evidence-source note (individual patient vs aggregated)
This report is derived from **aggregated disease-level resources** (reviews, guidelines syntheses, cohort/registry studies, and clinical trial registry entries) plus some **single-center retrospective cohorts** and **experimental model studies**. (corte2024currentpreoperativemanagement pages 1-2, dongre2024tp53mutationand pages 1-2, meng2024overallsurvivalassociated pages 1-2, dongre2020establishmentofa pages 1-7)

---

## 2. Etiology

### Core causal pathways (current understanding)
Modern classification recognizes two main etiologic pathways for VSCC:
1. **HPV-associated VSCC:** often basaloid/warty morphology; typically p16 “block” positive; generally occurs in younger patients and is associated with precursor high-grade squamous intraepithelial lesions (HSIL/usual VIN). (dongre2024tp53mutationand pages 1-2, horn2024molecularsubtypesof pages 12-14, hohn20212020whoclassification pages 4-6)
2. **HPV-independent VSCC:** often keratinizing morphology; frequently linked to chronic inflammatory vulvar dermatoses (notably lichen sclerosus) and to differentiated VIN (dVIN); commonly shows aberrant p53 patterns consistent with TP53 alteration; generally associated with poorer prognosis. (dongre2024tp53mutationand pages 1-2, horn2024molecularsubtypesof pages 12-14, horn2024molecularsubtypesof pages 16-18)

A recent focus is the less common **HPV-independent/p53-wild-type subtype**, emphasizing that not all HPV-independent tumors are p53-abnormal. (horn2024molecularsubtypesof pages 12-14)

### Risk factors
**Infectious:** high-risk HPV infection is a major risk factor for HPV-associated disease; HPV16 is predominant among HPV-positive high-grade vulvar lesions in one 2024 review (HPV16 ≈80% of HPV-positive cases). (scurtu2024squamouscellcarcinoma pages 5-7)

**Inflammatory/dermatologic:** **lichen sclerosus (LS)** is strongly associated with HPV-independent precancers and cancer and can lead to SCC development; LS causes chronic inflammation and tissue remodeling that may support carcinogenesis. (luca2023lichensclerosusthe pages 1-2, scurtu2024squamouscellcarcinoma pages 5-7)

**Precursor lesions:** differentiated VIN (dVIN) is a high-risk HPV-independent precursor; one 2024 review reports much higher progression for dVIN than HSIL (43.2% vs 9.7%). (scurtu2024squamouscellcarcinoma pages 4-5)

**Host factors:** immunosuppression is highlighted as a critical cofactor for HPV-associated lesions in a recent review. (scurtu2024squamouscellcarcinoma pages 5-7)

### Protective factors
**HPV vaccination:** Multiple sources support prophylactic HPV vaccination as a key protective factor against HPV-associated disease, with very high efficacy in HPV-naïve individuals.
- A large 2024 cross-sectional study notes vaccine efficacy “close to 100%” for preventing HPV-associated cancers among those without prior infection with vaccine HPV types. (adekanmbi2024humanpapillomavirusvaccination pages 1-2)
- A 2024 review of HPV vaccine strategies states that vaccination blocks transmission and prevents HPV-related cancers and reports global implementation but limited coverage (143 member states by end of 2023; ~15% of young girls vaccinated). (cai2024humanpapillomavirusrelatedcancer pages 1-2)

**Management of lichen sclerosus (risk reduction plausibility):** LS reviews and cohorts emphasize the need for early diagnosis, adequate treatment, and follow-up to reduce malignant evolution risk.
- A 2024 LS review reports markedly elevated vulvar cancer risk in LS (example population-based SIR 33.6 for vulvar cancer) and suggests that consistent long-term potent topical corticosteroid (TCS) use may reduce recurrence compared with historical recurrence rates. (popa2024vulvarlichensclerosus pages 21-22)

### Gene–environment interactions
Direct quantitative gene–environment interaction estimates were not present in the retrieved evidence. Mechanistically, LS-associated chronic inflammation/oxidative stress provides an enabling microenvironment for carcinogenesis and can co-occur with TP53 pathway alterations typical of HPV-independent disease. (luca2023lichensclerosusthe pages 1-2, scurtu2024squamouscellcarcinoma pages 5-7)

---

## 3. Phenotypes (clinical presentation, signs/symptoms, QoL)

### Common presenting symptoms/signs (VSCC)
Recent clinical updates emphasize that presentation ranges from asymptomatic lesions detected on exam to symptomatic disease with:
- vulvar **pruritus** (itching)
- **pain/burning**
- **lump/mass**
- **ulcer**
These features are highlighted in recent clinical overviews and updates. (corte2024currentpreoperativemanagement pages 1-2, olawaiye2021cancerofthe pages 1-2)

### Age of onset / demographics
VSCC predominantly affects postmenopausal women with mean/median ages often >65–70 years in clinical series and reviews; HPV-associated cases skew younger. (corte2024currentpreoperativemanagement pages 1-2, cebollaverdugo2024multidisciplinaryvulvarcancer pages 2-4, dongre2024tp53mutationand pages 1-2)

### Quality-of-life impacts
Major QoL burdens stem from symptoms (pain/pruritus), genital functional impairment, and treatment morbidity.
- Conservative approaches (e.g., sentinel node biopsy) are emphasized to reduce long-term morbidity such as chronic lymphedema, wound issues, and sexual dysfunction. (cebollaverdugo2024multidisciplinaryvulvarcancer pages 2-4, kolk2024updateonthe pages 1-2)

### Suggested HPO terms (examples)
(These are ontology suggestions; HPO IDs are provided where commonly used—verify in HPO browser for exact IDs.)
- **Pruritus** (HP:0000989)
- **Vulvar pain** (term exists in HPO; verify exact ID)
- **Genital ulcer** (HP:0000211, general mucosal ulceration; vulvar-specific term should be checked)
- **Vulvar mass** (term exists; verify exact ID)
- **Lymphedema** (HP:0001004) (treatment complication) (cebollaverdugo2024multidisciplinaryvulvarcancer pages 2-4)
- **Dyspareunia** (HP:0000148) (common in LS and survivorship context) (luca2023lichensclerosusthe pages 1-2)

---

## 4. Genetic / Molecular Information

### Molecular classification and defining biomarkers
WHO-era classification of vulvar SCC emphasizes HPV association using p16 as a surrogate marker and p53 immunophenotyping for HPV-independent disease (with a recognized “uncertain” group). (hohn20212020whoclassification pages 4-6, horn2024molecularsubtypesof pages 16-18)

- **HPV-associated:** p16 block-positive; often p53 wild-type pattern; typically better prognosis/radiosensitivity. (hohn20212020whoclassification pages 4-6)
- **HPV-independent:** often p16 negative/non-block; frequently p53 aberrant (overexpression, null, cytoplasmic) consistent with TP53 alteration. (horn2024molecularsubtypesof pages 16-18)

### Recurrent somatic alterations (VSCC)
**2024 Japanese VSCC genomic profiling:** TP53 (52–81%), HRAS (7–26%), CDKN2A (21–24%), PIK3CA (5–10%). (fujii2024genomicprofilesof pages 1-2)

**HPV-status–linked molecular profiles (tumor sequencing cohort):** HPV-independent tumors show high rates of TP53, TERT promoter, CDKN2A, NOTCH1, FAT1 alterations, while HPV-associated tumors are enriched for activating PIK3CA mutations (PI3K pathway). (salama2022molecularlandscapeof pages 1-3)

### Mechanistic/pathway summary (causal chain)
- **HPV-associated pathway:** viral oncoproteins (E6/E7/E5) enable immune evasion and drive carcinogenesis; E6/E7 disrupt tumor suppressor pathways, with downstream cell-cycle dysregulation and p16 overexpression. (scurtu2024squamouscellcarcinoma pages 5-7)
- **HPV-independent pathway:** chronic inflammation (e.g., LS) and precursor dVIN are linked to TP53 mutagenic processes, NOTCH1 loss-of-function, and RTK/RAS/PI3K signaling (including HRAS involvement), driving clonal expansion and invasion. (scurtu2024squamouscellcarcinoma pages 5-7, fujii2024genomicprofilesof pages 1-2)

### Suggested GO biological process terms (examples)
- **Epithelial cell proliferation** (GO:0050673)
- **Keratinocyte differentiation** (GO:0030216)
- **Cell cycle regulation** (GO:0051726)
- **DNA damage response** (GO:0006974)
- **Regulation of apoptotic process** (GO:0042981)
- **Response to virus** (GO:0009615) (HPV-associated)

### Suggested CL (cell type) terms (examples)
- **Keratinocyte** (CL:0000312)
- **Fibroblast / cancer-associated fibroblast** (CL:0000057; CAF is a functional state) (dongre2020establishmentofa pages 1-7)
- **CD8-positive, alpha-beta T cell** (CL:0000625) (prognostic immune infiltrate context) (zhang2023anintegratedmodel pages 1-2)

---

## 5. Environmental Information

### Infectious agents
- **High-risk HPV** is a key infectious driver of the HPV-associated VSCC pathway. (dongre2024tp53mutationand pages 1-2, scurtu2024squamouscellcarcinoma pages 5-7)

### Lifestyle factors
- Smoking is cited as a risk factor in clinical updates and reviews. (olawaiye2021cancerofthe pages 1-2)

### Non-infectious inflammatory conditions
- Chronic inflammatory vulvar dermatoses, especially lichen sclerosus, are strongly linked to HPV-independent carcinogenesis and functional morbidity. (luca2023lichensclerosusthe pages 1-2)

---

## 6. Mechanism / Pathophysiology

### Key mechanisms and pathways
- **PI3K/AKT/mTOR signaling:** implicated particularly in HPV-associated tumors via PIK3CA activating mutations, and in a subset of HPV-independent cases. (salama2022molecularlandscapeof pages 1-3, fujii2024genomicprofilesof pages 1-2)
- **RAS/MAPK signaling:** HRAS mutations occur in a subset of VSCC. (fujii2024genomicprofilesof pages 1-2)
- **TP53 tumor suppressor pathway:** frequently altered in HPV-independent VSCC and linked to worse prognosis. (dongre2024tp53mutationand pages 1-2, fujii2024genomicprofilesof pages 1-2)
- **NOTCH pathway:** frequently altered in HPV-independent disease in sequencing cohorts, consistent with altered squamous differentiation programs. (salama2022molecularlandscapeof pages 1-3)

### Tumor microenvironment and stromal dependence
Experimental evidence supports a strong role for tumor–stroma interaction: a LS-associated VSCC cell line (VCC1) showed **fibroblast-dependent invasion and tumor formation** in 3D organotypic models and xenografts. (dongre2020establishmentofa pages 1-7)

---

## 7. Anatomical Structures Affected

### Organ / tissue level
- Primary site: **vulva** (labia majora/minora, clitoris, perineum, mons). (corte2024currentpreoperativemanagement pages 1-2)
- Regional spread: lymphatic drainage primarily to **inguinofemoral nodes**, secondarily to pelvic nodes. (olawaiye2021cancerofthe pages 1-2)

### Suggested UBERON terms (examples)
- Vulva (UBERON:0000997)
- Labium majus (UBERON:0003185)
- Labium minus (UBERON:0003186)
- Clitoris (UBERON:0002256)
- Inguinal lymph node (UBERON:0001542)

---

## 8. Temporal Development

- **Onset:** typically adult/geriatric; HPV-associated pathway tends to present earlier than HPV-independent. (dongre2024tp53mutationand pages 1-2)
- **Progression and precursors:** HSIL/uVIN and dVIN are recognized precursors; dVIN has higher malignant potential and faster progression than HSIL in comparative data summarized by reviews. (scurtu2024squamouscellcarcinoma pages 4-5)

---

## 9. Inheritance and Population

### Epidemiology (selected recent statistics)
- A 2024 imaging review cites **47,000 global vulvar cancer cases in 2022**. (ha2024imaginginvulval pages 1-2)
- A single-center “patterns of care” study cites GLOBOCAN 2020 estimates (45,240 cases; 17,427 deaths). (singhal2024patternsofcare pages 1-2)

Genetic inheritance is not applicable in a Mendelian sense for most vulvar carcinoma; this is primarily a sporadic, multifactorial cancer with somatic driver alterations.

---

## 10. Diagnostics

### Diagnostic approach
- **Biopsy** of any suspicious vulvar lesion is emphasized as essential for diagnosis; vulvoscopy is a key clinical tool. (corte2024currentpreoperativemanagement pages 1-2, olawaiye2021cancerofthe pages 1-2)

### Biomarkers used in practice
- **p16 immunohistochemistry** is used as a surrogate for HPV association; diffuse “block” staining supports HPV-associated neoplasia. (dongre2024tp53mutationand pages 1-2, hohn20212020whoclassification pages 4-6)
- **p53 immunohistochemistry** helps identify HPV-independent/TP53-altered tumors and precursor lesions such as dVIN. (horn2024molecularsubtypesof pages 16-18)

### Imaging (preoperative and staging)
Imaging recommendations vary by stage and clinical question; a 2024 preoperative management review identifies **MRI and PET** as gold-standard imaging for local extension and nodal evaluation, with expert-performed **ultrasound** increasingly used for groin node assessment. (corte2024currentpreoperativemanagement pages 1-2)

The FIGO 2021 staging revision explicitly allows staging to incorporate cross-sectional imaging findings. (olawaiye2021figostagingfor pages 1-2)

The following table (from the 2024 imaging review) summarizes FIGO 2021 staging.

(ha2024imaginginvulval media e360c86b)

### Differential diagnosis (selected)
Vulvar lesions that can mimic malignant or premalignant disease include inflammatory dermatoses (e.g., lichen sclerosus) and premalignant vulvar intraepithelial lesions; biopsy is required when neoplasia is suspected. (luca2023lichensclerosusthe pages 1-2)

---

## 11. Outcome / Prognosis

### Prognostic factors
- **Nodal status** is critical: one systematic review states 5-year OS is **>80% node-negative**, **<40% with inguinal node involvement**, and **10–15% with pelvic nodes**. (ferrari2024adjuvantradiotherapyfor pages 1-2)
- Molecular subtype impacts prognosis: TP53 mutation status is an independent adverse prognostic factor for progression-free survival, and transcriptionally active hrHPV is associated with improved outcomes in a 2024 cohort. (dongre2024tp53mutationand pages 1-2)

### Recent quantitative survival / outcome statistics
- SEER-derived survival cited in a guideline comparison: **5-year survival 85.6% localized**, **47.5% regional**, **23.3% distant (stage IVB)**. (restaino2025managementofpatients pages 2-4)
- A single-center cohort (n=82) reported: disease-specific recurrence **32.9%**, mortality **30.5%**, median DFS **17 months**, median OS **27 months**. (singhal2024patternsofcare pages 1-2)
- In metastatic vulvar cancer (SEER 2000–2019), chemoradiotherapy improved OS vs radiotherapy alone (matched cohort HR **0.7367**, 95% CI 0.5906–0.9190). (meng2024overallsurvivalassociated pages 1-2)

---

## 12. Treatment

### Current standard-of-care (real-world implementations)
**Surgery**
- Early-stage disease: local excision / radical local excision with attention to margins, plus groin staging when indicated. (kolk2024updateonthe pages 1-2, ferrari2024adjuvantradiotherapyfor pages 1-2)

**Sentinel lymph node biopsy (SLNB)**
- SLNB is an established, less morbid alternative to inguinofemoral lymphadenectomy in selected early-stage VSCC; it reduces complications such as lymphedema while maintaining oncologic safety. (kolk2024updateonthe pages 1-2)

**Radiotherapy / chemoradiotherapy**
- Adjuvant radiotherapy for nodal disease has limited RCT evidence but suggests reduction in cancer-related deaths and groin recurrences; one RCT reported 6-year cancer-related deaths 29% vs 51% (HR 0.49) and groin recurrences 5.3% vs 24.1% favoring radiotherapy. (ferrari2024adjuvantradiotherapyfor pages 1-2)
- For locally advanced unresectable disease, multiple guideline sets recommend definitive chemoradiation. (restaino2025managementofpatients pages 14-16)

**Systemic therapy and immunotherapy (emerging)**
- Modern guidance notes emerging immunotherapy options for advanced disease, but evidence remains limited and often extrapolated from other SCC sites; clinical trials are ongoing. (restaino2025managementofpatients pages 2-4)

### Active / planned clinical trials (selected)
- **NCT07101848 (BRAVA VULVAR)**: Phase II randomized maintenance **cemiplimab vs best supportive care** after 1st-line platinum chemotherapy in advanced/recurrent vulvar cancer; primary endpoint PFS at week 24; not yet recruiting; estimated start 2025-11-01. URL: https://clinicaltrials.gov/study/NCT07101848 (NCT07101848 chunk 1)
- **NCT05903833**: Phase II single-arm **pembrolizumab + lenvatinib** in recurrent/metastatic/locally advanced VSCC not amenable to curative surgery/radiotherapy; primary endpoint ORR within 24 weeks; recruiting; start 2025-06-24. URL: https://clinicaltrials.gov/study/NCT05903833 (NCT05903833 chunk 1)
- **NCT07290894 (MITO VULVA-01)**: Phase II single-arm multi-cohort **pembrolizumab + lenvatinib** across unresectable locally advanced, chemo-naïve metastatic, and post-chemo recurrent/metastatic cohorts; primary endpoint ORR by RECIST 1.1; recruiting; start 2026-03-12. URL: https://clinicaltrials.gov/study/NCT07290894 (NCT07290894 chunk 1)

### MAXO (Medical Action Ontology) suggestions (examples)
(Provide as ontology suggestions; confirm IDs in MAXO.)
- Surgical excision / wide local excision; radical vulvectomy
- Sentinel lymph node biopsy
- External beam radiotherapy
- Concurrent chemoradiotherapy
- Immune checkpoint inhibitor therapy (anti–PD-1)

---

## 13. Prevention

### Primary prevention
- **HPV vaccination** is the primary preventive tool for HPV-associated vulvar precancers/cancers, with very high efficacy in HPV-naïve individuals and broad global adoption but incomplete coverage. (adekanmbi2024humanpapillomavirusvaccination pages 1-2, cai2024humanpapillomavirusrelatedcancer pages 1-2)

### Secondary/tertiary prevention
- There is **no population screening program** for vulvar cancer; prevention relies on early identification and management of predisposing conditions/precursors and biopsy of suspicious lesions. (olawaiye2021cancerofthe pages 1-2)
- For LS, long-term potent topical corticosteroids are standard and cohorts/reviews emphasize surveillance; LS has strong symptom burden and elevated malignancy risk. (luca2023lichensclerosusthe pages 1-2, popa2024vulvarlichensclerosus pages 21-22)

---

## 14. Other Species / Natural Disease
No naturally occurring non-human species disease data were identified in the retrieved sources for vulvar carcinoma specifically.

---

## 15. Model Organisms / Experimental Models

### Cell lines, organotypic models, xenografts
- A LS-associated VSCC cell line (**VCC1**) was established and shown to have **fibroblast-dependent tumorigenic and invasive behavior** in 3D collagen co-culture/organotypic assays and xenografts, highlighting cancer-associated fibroblast contributions. URL: https://doi.org/10.1016/j.yexcr.2019.111684 (Published Jan 2020). (dongre2020establishmentofa pages 1-7)
- The **A431** cell line is used as a vulvar SCC model in mechanistic studies; one report shows miR-4712-5p promotes proliferation/invasion by targeting PTEN and activating AKT/cyclin D1 signaling. URL: https://doi.org/10.3892/or.2019.7320 (Published Sep 2019). (yang2019microrna47125ppromotesproliferation pages 1-2)

### Suggested uses
- Tumor–stroma interaction experiments (CAF co-culture)
- Pathway perturbation (PI3K/AKT, RAS/MAPK)
- Immunotherapy biomarker exploration (PD-L1, TILs) and radiosensitivity hypotheses by subtype

---

## Summary artifact (identifiers, subtypes, genomics)

| Section | Item | Summary | Notes/Citations |
|---|---|---|---|
| Identifiers/terminology | Standard disease name | **Vulvar carcinoma / vulval cancer**; most cases are **vulvar squamous cell carcinoma (VSCC)**, the predominant histology (~90%). | ICD-10 **C51** is reported for vulval cancer; VSCC predominance noted in recent reviews (corte2024currentpreoperativemanagement pages 1-2) |
| Identifiers/terminology | Controlled vocabulary / search term | A 2024 imaging review explicitly used the MeSH search terms **“vulval neoplasm”** and **“diagnostic imaging.”** | Useful for literature retrieval, though no MeSH UID was provided in retrieved text (ha2024imaginginvulval pages 1-2) |
| Identifiers/terminology | Staging/classification | **FIGO 2021** is the current staging framework for vulvar carcinoma and **permits incorporation of cross-sectional imaging** into staging. | Data-derived revision; imaging incorporation specifically noted (olawaiye2021figostagingfor pages 1-2, ha2024imaginginvulval pages 1-2, faruqiUnknownyear2021figostaging pages 1-5) |
| Identifiers/terminology | ICD-related coding context | Additional ICD-related references in retrieved literature include ICD-10 groupings for vulvar cancer and ICD-O-3 site code **C51.0** in HPV-related cancer analyses. | ICD-10 C51 reported in economic analysis; ICD-O-3 C51.0 cited in HPV-related cancer rate study (steinkasserer2023characterizationofpatients pages 1-2, adekanmbi2024humanpapillomavirusvaccination pages 1-2) |
| Molecular subtype | HPV-associated VSCC | Typically younger women; often basaloid/warty morphology; precursor lesions are **HSIL/uVIN (usual-type VIN)**; usually **block-positive p16**, generally non-aberrant/wild-type p53 pattern; often better prognosis and better radiotherapy response. | HPV-associated tumors usually occur in younger patients and have improved prognosis/radiosensitivity (dongre2024tp53mutationand pages 1-2, horn2024molecularsubtypesof pages 12-14, hohn20212020whoclassification pages 4-6, scurtu2024squamouscellcarcinoma pages 5-7) |
| Molecular subtype | HPV-independent, p53-abnormal VSCC | Typically older/postmenopausal women; usually keratinizing morphology; precursor lesions are **dVIN** and often **lichen sclerosus**; usually **p16 negative/non-block** with **aberrant p53** (overexpression, null, or cytoplasmic pattern); generally worse prognosis and less radiosensitive. | Strongly associated with TP53 alterations, poorer outcomes, and lower radiosensitivity (dongre2024tp53mutationand pages 1-2, hohn20212020whoclassification pages 4-6, horn2024molecularsubtypesof pages 16-18) |
| Molecular subtype | HPV-independent, p53-wild-type VSCC | Uncommon third molecular subtype within HPV-independent disease; lacks HPV association and lacks classic p53-abnormal pattern; still falls within the HPV-independent spectrum but is molecularly distinct and under active study. | Recent 2024 review emphasizes diagnostic/treatment significance of this subtype (horn2024molecularsubtypesof pages 12-14, horn2024molecularsubtypesof pages 1-5) |
| Biomarker framework | p16 / p53 interpretation | **p16** is a surrogate marker of HPV-driven disease; **p53** IHC helps identify HPV-independent/TP53-altered disease. Combined p16/p53 stratification supports classification into clinically meaningful subgroups. | WHO/CAP-aligned approach summarized in recent reviews and cohort work (dongre2024tp53mutationand pages 1-2, hohn20212020whoclassification pages 4-6, horn2024molecularsubtypesof pages 16-18, hohn20212020whoclassification pages 1-2) |
| Genomics: 2024 Japanese cohort | TP53 | Most common alteration in Japanese VSCC cohorts: **52–81%**. | 2024 Scientific Reports cohort; predominantly HPV-independent tumors (fujii2024genomicprofilesof pages 1-2) |
| Genomics: 2024 Japanese cohort | HRAS | Recurrent alteration: **7–26%**. | Suggests RTK/RAS pathway involvement in a subset (fujii2024genomicprofilesof pages 1-2) |
| Genomics: 2024 Japanese cohort | CDKN2A | Recurrent alteration: **21–24%**. | Cell-cycle dysregulation signal (fujii2024genomicprofilesof pages 1-2) |
| Genomics: 2024 Japanese cohort | PIK3CA | Recurrent alteration: **5–10%**. | Supports PI3K pathway targetability in a subset (fujii2024genomicprofilesof pages 1-2) |
| Genomics: 2022 MSK cohort | HPV-associated profile | Enriched for **PIK3CA activating mutations 7/11 (64%)**; NOTCH-pathway alterations also present **6/11 (55%)** but involving different genes than HPV-independent tumors. | HPV-associated tumors favor PI3K-pathway activation (salama2022molecularlandscapeof pages 4-6, salama2022molecularlandscapeof pages 8-10, salama2022molecularlandscapeof pages 1-3) |
| Genomics: 2022 MSK cohort | HPV-independent profile | Strong enrichment for **TERT alterations 14/15 (93%)**, **TP53 13/15 (87%)**, **CDKN2A 10/15 (67%)**, **NOTCH1 7/15 (47%)**, **FAT1 7/15 (47%)**; NOTCH-pathway alterations overall **10/15 (67%)**. | Distinct molecular program from HPV-associated tumors; TERT/TP53/CDKN2A/NOTCH1 argue against HPV-driven etiology (salama2022molecularlandscapeof pages 4-6, salama2022molecularlandscapeof pages 8-10, salama2022molecularlandscapeof pages 1-3) |
| Genomics: additional recent cohort | HPV-independent vs HPV-associated differences | In an additional recent cohort, HPV-negative tumors showed **TP53 86% vs 0%**, **POLE 50% vs 6%**, **NOTCH1 43% vs 19%**, **CDKN2A 36% vs 0%**; HPV-associated tumors more often had CNVs, especially **cMYC**, plus **CDK2/CDK4** amplifications. | Useful supporting comparison for subtype-specific molecular architecture (farkas2025pathologicalvariantsin pages 8-9, farkas2025pathologicalvariantsin pages 7-8) |


*Table: This table compiles core identifiers, current subtype terminology, biomarker definitions, and recurrent genomic alterations for vulvar carcinoma/VSCC. It is useful as a compact reference for disease ontology, clinicopathologic stratification, and precision-oncology annotation.*

References

1. (corte2024currentpreoperativemanagement pages 1-2): Luigi Della Corte, Valeria Cafasso, Maria Chiara Guarino, Giuseppe Gullo, Gaspare Cucinella, Alessandra Lopez, Simona Zaami, Gaetano Riemma, Pierluigi Giampaolino, and Giuseppe Bifulco. Current preoperative management of vulvar squamous cell carcinoma: an overview. Cancers, 16:1846, May 2024. URL: https://doi.org/10.3390/cancers16101846, doi:10.3390/cancers16101846. This article has 12 citations.

2. (steinkasserer2023characterizationofpatients pages 1-2): L. Steinkasserer, J. Hachenberg, P. Hillemanns, and M. Jentschke. Characterization of patients with vulvar lichen sclerosus and association to vulvar carcinoma: a retrospective single center analysis. Archives of Gynecology and Obstetrics, 307:1921-1928, Nov 2023. URL: https://doi.org/10.1007/s00404-022-06848-y, doi:10.1007/s00404-022-06848-y. This article has 20 citations and is from a peer-reviewed journal.

3. (adekanmbi2024humanpapillomavirusvaccination pages 1-2): Victor Adekanmbi, Itunu Sokale, Fangjian Guo, Jessica Ngo, Thao N. Hoang, Christine D. Hsu, Abiodun Oluyomi, and Abbey B. Berenson. Human papillomavirus vaccination and human papillomavirus–related cancer rates. JAMA Network Open, 7:e2431807, Sep 2024. URL: https://doi.org/10.1001/jamanetworkopen.2024.31807, doi:10.1001/jamanetworkopen.2024.31807. This article has 13 citations and is from a peer-reviewed journal.

4. (ha2024imaginginvulval pages 1-2): Minah Ha and Lois Eva. Imaging in vulval cancer. Cancers, 16:2269, Jun 2024. URL: https://doi.org/10.3390/cancers16122269, doi:10.3390/cancers16122269. This article has 5 citations.

5. (olawaiye2021figostagingfor pages 1-2): A. Olawaiye, J. Cotler, M. Cuello, N. Bhatla, A. Okamoto, S. Wilailak, C. Purandare, G. Lindeque, J. Berek, S. Kehoe, S. Kehoe, A. Olawaiye, M. Cuello, N. Bhatla, A. Okamoto, S. Wilailak, G. Lindeque, J. Berek, C. Purandare, and J. Cain. Figo staging for carcinoma of the vulva: 2021 revision. International Journal of Gynaecology and Obstetrics, 155:43-47, Sep 2021. URL: https://doi.org/10.1002/ijgo.13880, doi:10.1002/ijgo.13880. This article has 129 citations.

6. (dongre2024tp53mutationand pages 1-2): Harsh Nitin Dongre, Rammah Elnour, Stian Tornaas, Siren Fromreide, Liv Cecilie Vestrheim Thomsen, Ingrid Benedicte Moss Kolseth, Elisabeth Sivy Nginamau, Anne Christine Johannessen, Olav Karsten Vintermyr, Daniela Elena Costea, and Line Bjørge. Tp53 mutation and human papilloma virus status as independent prognostic factors in a norwegian cohort of vulva squamous cell carcinoma. Acta Obstetricia et Gynecologica Scandinavica, 103:165-175, Oct 2024. URL: https://doi.org/10.1111/aogs.14689, doi:10.1111/aogs.14689. This article has 14 citations and is from a domain leading peer-reviewed journal.

7. (meng2024overallsurvivalassociated pages 1-2): Xiaolin Meng, Shuaiqingying Guo, Xue Feng, Jihui Ai, and Jie Yang. Overall survival associated with surgery, radiotherapy, and chemotherapy in metastatic vulvar cancer: a retrospective cohort study based on the seer database. Cancer Pathogenesis and Therapy, 2:195-204, Jul 2024. URL: https://doi.org/10.1016/j.cpt.2023.08.003, doi:10.1016/j.cpt.2023.08.003. This article has 6 citations.

8. (dongre2020establishmentofa pages 1-7): Harsh Dongre, Neha Rana, Siren Fromreide, Saroj Rajthala, Ingeborg Bøe Engelsen, Justine Paradis, J. Silvio Gutkind, Olav Karsten Vintermyr, Anne Christine Johannessen, Line Bjørge, and Daniela Elena Costea. Establishment of a novel cancer cell line derived from vulvar carcinoma associated with lichen sclerosus exhibiting a fibroblast-dependent tumorigenic potential. Experimental Cell Research, 386:111684, Jan 2020. URL: https://doi.org/10.1016/j.yexcr.2019.111684, doi:10.1016/j.yexcr.2019.111684. This article has 12 citations and is from a peer-reviewed journal.

9. (horn2024molecularsubtypesof pages 12-14): Lars-Christian Horn, Christine E. Brambs, Blake Gilks, Lien Hoang, Naveena Singh, Ruth GG Hiller, Hering Kathrin, Jessica N McAlpine, Mona Alfaraidi, Bahriye Aktas, Nadja DORNHÖFER, Amy Jamieson, and Anne Kathrin Höhn. Molecular subtypes of vulvar squamous cell carcinoma: the significance of hpv-independent/p53 wild type. Cancers, Dec 2024. URL: https://doi.org/10.3390/cancers16244216, doi:10.3390/cancers16244216. This article has 11 citations.

10. (hohn20212020whoclassification pages 4-6): Anne Kathrin Höhn, Christine E. Brambs, Grit Gesine Ruth Hiller, Doris May, Elisa Schmoeckel, and Lars-Christian Horn. 2020 who classification of female genital tumors. Geburtshilfe und Frauenheilkunde, 81:1145-1153, Oct 2021. URL: https://doi.org/10.1055/a-1545-4279, doi:10.1055/a-1545-4279. This article has 487 citations and is from a peer-reviewed journal.

11. (horn2024molecularsubtypesof pages 16-18): Lars-Christian Horn, Christine E. Brambs, Blake Gilks, Lien Hoang, Naveena Singh, Ruth GG Hiller, Hering Kathrin, Jessica N McAlpine, Mona Alfaraidi, Bahriye Aktas, Nadja DORNHÖFER, Amy Jamieson, and Anne Kathrin Höhn. Molecular subtypes of vulvar squamous cell carcinoma: the significance of hpv-independent/p53 wild type. Cancers, Dec 2024. URL: https://doi.org/10.3390/cancers16244216, doi:10.3390/cancers16244216. This article has 11 citations.

12. (scurtu2024squamouscellcarcinoma pages 5-7): Lucian G. Scurtu, Francesca Scurtu, Sebastian Catalin Dumitrescu, and Olga Simionescu. Squamous cell carcinoma in situ—the importance of early diagnosis in bowen disease, vulvar intraepithelial neoplasia, penile intraepithelial neoplasia, and erythroplasia of queyrat. Diagnostics, 14:1799, Aug 2024. URL: https://doi.org/10.3390/diagnostics14161799, doi:10.3390/diagnostics14161799. This article has 11 citations.

13. (luca2023lichensclerosusthe pages 1-2): David A. De Luca, Cristian Papara, Artem Vorobyev, Hernán Staiger, Katja Bieber, Diamant Thaçi, and Ralf J. Ludwig. Lichen sclerosus: the 2023 update. Frontiers in Medicine, Feb 2023. URL: https://doi.org/10.3389/fmed.2023.1106318, doi:10.3389/fmed.2023.1106318. This article has 234 citations.

14. (scurtu2024squamouscellcarcinoma pages 4-5): Lucian G. Scurtu, Francesca Scurtu, Sebastian Catalin Dumitrescu, and Olga Simionescu. Squamous cell carcinoma in situ—the importance of early diagnosis in bowen disease, vulvar intraepithelial neoplasia, penile intraepithelial neoplasia, and erythroplasia of queyrat. Diagnostics, 14:1799, Aug 2024. URL: https://doi.org/10.3390/diagnostics14161799, doi:10.3390/diagnostics14161799. This article has 11 citations.

15. (cai2024humanpapillomavirusrelatedcancer pages 1-2): Xia Cai and Ling Xu. Human papillomavirus-related cancer vaccine strategies. Vaccines, 12 11:1291, Nov 2024. URL: https://doi.org/10.3390/vaccines12111291, doi:10.3390/vaccines12111291. This article has 14 citations.

16. (popa2024vulvarlichensclerosus pages 21-22): Adelina Popa, Mihai Dumitrascu, Aida Petca, Razvan-Cosmin Petca, and Florica Sandru. Vulvar lichen sclerosus: navigating sex hormone dynamics and pioneering personalized treatment paradigm. Journal of Personalized Medicine, 14:76, Jan 2024. URL: https://doi.org/10.3390/jpm14010076, doi:10.3390/jpm14010076. This article has 21 citations.

17. (olawaiye2021cancerofthe pages 1-2): Alexander B. Olawaiye, Mauricio A. Cuello, and Linda J. Rogers. Cancer of the vulva: 2021 update. International Journal of Gynaecology and Obstetrics, 155:7-18, Oct 2021. URL: https://doi.org/10.1002/ijgo.13881, doi:10.1002/ijgo.13881. This article has 247 citations.

18. (cebollaverdugo2024multidisciplinaryvulvarcancer pages 2-4): Marta Cebolla-Verdugo, Victor Alfredo Cassini-Gómez de Cádiz, Juan Pablo Velasco-Amador, María Zulaika-Lloret, Francisco Manuel Almazán-Fernández, and Ricardo Ruiz-Villaverde. Multidisciplinary vulvar cancer management: the dermatologist’s perspective. Life, 15:19, Dec 2024. URL: https://doi.org/10.3390/life15010019, doi:10.3390/life15010019. This article has 1 citations.

19. (kolk2024updateonthe pages 1-2): Willemijn L. van der Kolk, Joost Bart, Ate J.G. van der Zee, and Maaike H.M. Oonk. Update on the sentinel node procedure in vulvar cancer. Journal of the National Comprehensive Cancer Network : JNCCN, Mar 2024. URL: https://doi.org/10.6004/jnccn.2024.7002, doi:10.6004/jnccn.2024.7002. This article has 2 citations.

20. (fujii2024genomicprofilesof pages 1-2): Erisa Fujii, Mayumi Kobayashi Kato, Maiko Yamaguchi, Daiki Higuchi, Takafumi Koyama, Masaaki Komatsu, Ryuji Hamamoto, Mitsuya Ishikawa, Tomoyasu Kato, Takashi Kohno, Kouya Shiraishi, and Hiroshi Yoshida. Genomic profiles of japanese patients with vulvar squamous cell carcinoma. Scientific Reports, Jun 2024. URL: https://doi.org/10.1038/s41598-024-63913-z, doi:10.1038/s41598-024-63913-z. This article has 1 citations and is from a peer-reviewed journal.

21. (salama2022molecularlandscapeof pages 1-3): Abeer M. Salama, Amir Momeni-Boroujeni, Chad Vanderbilt, Marc Ladanyi, and Robert Soslow. Molecular landscape of vulvovaginal squamous cell carcinoma: new insights into molecular mechanisms of hpv-associated and hpv-independent squamous cell carcinoma. Modern Pathology, 35:274-282, Feb 2022. URL: https://doi.org/10.1038/s41379-021-00942-3, doi:10.1038/s41379-021-00942-3. This article has 44 citations and is from a domain leading peer-reviewed journal.

22. (zhang2023anintegratedmodel pages 1-2): Tao Zhang, Yingfan Zhu, Jie Luo, Juanqing Li, Shuang Niu, Hao Chen, and Feng Zhou. An integrated model for prognosis in vulvar squamous cell carcinoma. BMC Cancer, Jun 2023. URL: https://doi.org/10.1186/s12885-023-11039-2, doi:10.1186/s12885-023-11039-2. This article has 9 citations and is from a peer-reviewed journal.

23. (singhal2024patternsofcare pages 1-2): Seema Singhal, Daya Nand Sharma, Sandeep Mathur, Swati Tomar, Jyoti Meena, Anju Singh, and Neerja Bhatla. Patterns of care for vulvar cancer and insights from revised figo staging: a retrospective study. World Journal of Surgical Oncology, Dec 2024. URL: https://doi.org/10.1186/s12957-024-03612-1, doi:10.1186/s12957-024-03612-1. This article has 3 citations and is from a peer-reviewed journal.

24. (ha2024imaginginvulval media e360c86b): Minah Ha and Lois Eva. Imaging in vulval cancer. Cancers, 16:2269, Jun 2024. URL: https://doi.org/10.3390/cancers16122269, doi:10.3390/cancers16122269. This article has 5 citations.

25. (ferrari2024adjuvantradiotherapyfor pages 1-2): Federico Ferrari, Lamiese Ismail, Ahmad Sabbagh, Kieran Hardern, Robert Owens, Elisa Gozzini, and Hooman Soleymani Majd. Adjuvant radiotherapy for groin node metastases following surgery for vulvar cancer: a systematic review. Oncology Reviews, May 2024. URL: https://doi.org/10.3389/or.2024.1389035, doi:10.3389/or.2024.1389035. This article has 3 citations.

26. (restaino2025managementofpatients pages 2-4): Stefano Restaino, Giulia Pellecchia, Martina Arcieri, Giorgio Bogani, Cristina Taliento, Pantaleo Greco, Lorenza Driul, Vito Chiantera, Rosa Pasqualina De Vincenzo, Giorgia Garganese, Francesco Sopracordevole, Violante Di Donato, Andrea Ciavattini, Paolo Scollo, Giovanni Scambia, and Giuseppe Vizzielli. Management of patients with vulvar cancers: a systematic comparison of international guidelines (nccn–asco–esgo–bgcs–igcs–figo–french guidelines–rcog). Cancers, 17:186, Jan 2025. URL: https://doi.org/10.3390/cancers17020186, doi:10.3390/cancers17020186. This article has 23 citations.

27. (restaino2025managementofpatients pages 14-16): Stefano Restaino, Giulia Pellecchia, Martina Arcieri, Giorgio Bogani, Cristina Taliento, Pantaleo Greco, Lorenza Driul, Vito Chiantera, Rosa Pasqualina De Vincenzo, Giorgia Garganese, Francesco Sopracordevole, Violante Di Donato, Andrea Ciavattini, Paolo Scollo, Giovanni Scambia, and Giuseppe Vizzielli. Management of patients with vulvar cancers: a systematic comparison of international guidelines (nccn–asco–esgo–bgcs–igcs–figo–french guidelines–rcog). Cancers, 17:186, Jan 2025. URL: https://doi.org/10.3390/cancers17020186, doi:10.3390/cancers17020186. This article has 23 citations.

28. (NCT07101848 chunk 1):  A PHASE II, RANDOMIZED TRIAL TO ASSESS MAINTENANCE THERAPY WITH CEMIPLIMAB VERSUS BEST SUPPORTIVE CARE AFTER 1ST LINE PLATINUM-BASED CHEMOTHERAPY IN ADVANCED/RECURRENT VULVAR CANCER. Hospital Israelita Albert Einstein. 2025. ClinicalTrials.gov Identifier: NCT07101848

29. (NCT05903833 chunk 1):  Pembrolizumab Combination With Lenvatinib in Pts With Recurrent,Persistent,Metastatic or Locally Advanced Vulvar Cancer Not Amenable to Curative Surgery or Radiotherapy. AGO Research GmbH. 2025. ClinicalTrials.gov Identifier: NCT05903833

30. (NCT07290894 chunk 1):  Pembrolizumab Plus Lenvatinib in Vulvar Cancer Patients: MITO VULVA-01. National Cancer Institute, Naples. 2026. ClinicalTrials.gov Identifier: NCT07290894

31. (yang2019microrna47125ppromotesproliferation pages 1-2): Shaojie Yang, Yanyan Zhao, Lufang Wang, Chang Liu, Ye Lu, Zhidong Fang, Hongshuang Shi, Wenyi Zhang, and Xin Wu. Microrna-4712-5p promotes proliferation of the vulvar squamous cell carcinoma cell line a431 by targeting pten through the akt/cyclin d1 signaling pathways. Oncology Reports, 42:1689-1698, Sep 2019. URL: https://doi.org/10.3892/or.2019.7320, doi:10.3892/or.2019.7320. This article has 13 citations and is from a peer-reviewed journal.

32. (faruqiUnknownyear2021figostaging pages 1-5): BRRGA Faruqi, M Eden, and SSANW Glenn. 2021 figo staging system for vulvar cancer: summary and comparison with 2009 figo staging system. Unknown journal, Unknown year.

33. (horn2024molecularsubtypesof pages 1-5): Lars-Christian Horn, Christine E. Brambs, Blake Gilks, Lien Hoang, Naveena Singh, Ruth GG Hiller, Hering Kathrin, Jessica N McAlpine, Mona Alfaraidi, Bahriye Aktas, Nadja DORNHÖFER, Amy Jamieson, and Anne Kathrin Höhn. Molecular subtypes of vulvar squamous cell carcinoma: the significance of hpv-independent/p53 wild type. Cancers, Dec 2024. URL: https://doi.org/10.3390/cancers16244216, doi:10.3390/cancers16244216. This article has 11 citations.

34. (hohn20212020whoclassification pages 1-2): Anne Kathrin Höhn, Christine E. Brambs, Grit Gesine Ruth Hiller, Doris May, Elisa Schmoeckel, and Lars-Christian Horn. 2020 who classification of female genital tumors. Geburtshilfe und Frauenheilkunde, 81:1145-1153, Oct 2021. URL: https://doi.org/10.1055/a-1545-4279, doi:10.1055/a-1545-4279. This article has 487 citations and is from a peer-reviewed journal.

35. (salama2022molecularlandscapeof pages 4-6): Abeer M. Salama, Amir Momeni-Boroujeni, Chad Vanderbilt, Marc Ladanyi, and Robert Soslow. Molecular landscape of vulvovaginal squamous cell carcinoma: new insights into molecular mechanisms of hpv-associated and hpv-independent squamous cell carcinoma. Modern Pathology, 35:274-282, Feb 2022. URL: https://doi.org/10.1038/s41379-021-00942-3, doi:10.1038/s41379-021-00942-3. This article has 44 citations and is from a domain leading peer-reviewed journal.

36. (salama2022molecularlandscapeof pages 8-10): Abeer M. Salama, Amir Momeni-Boroujeni, Chad Vanderbilt, Marc Ladanyi, and Robert Soslow. Molecular landscape of vulvovaginal squamous cell carcinoma: new insights into molecular mechanisms of hpv-associated and hpv-independent squamous cell carcinoma. Modern Pathology, 35:274-282, Feb 2022. URL: https://doi.org/10.1038/s41379-021-00942-3, doi:10.1038/s41379-021-00942-3. This article has 44 citations and is from a domain leading peer-reviewed journal.

37. (farkas2025pathologicalvariantsin pages 8-9): Sanja A. Farkas, Alvida Qvick, Gisela Helenius, and Gabriella Lillsunde-Larsson. Pathological variants in hpv-independent vulvar tumours. Scientific Reports, Jan 2025. URL: https://doi.org/10.1038/s41598-024-84688-3, doi:10.1038/s41598-024-84688-3. This article has 3 citations and is from a peer-reviewed journal.

38. (farkas2025pathologicalvariantsin pages 7-8): Sanja A. Farkas, Alvida Qvick, Gisela Helenius, and Gabriella Lillsunde-Larsson. Pathological variants in hpv-independent vulvar tumours. Scientific Reports, Jan 2025. URL: https://doi.org/10.1038/s41598-024-84688-3, doi:10.1038/s41598-024-84688-3. This article has 3 citations and is from a peer-reviewed journal.