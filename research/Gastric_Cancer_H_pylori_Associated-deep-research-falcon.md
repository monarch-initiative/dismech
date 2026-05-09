---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-08T16:36:39.316492'
end_time: '2026-05-08T16:51:35.317634'
duration_seconds: 896.0
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Gastric Cancer H. pylori Associated
  mondo_id: ''
  category: ''
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 40
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Gastric Cancer H. pylori Associated
- **MONDO ID:**  (if available)
- **Category:**

## Research Objectives

Please provide a comprehensive research report on **Gastric Cancer H. pylori Associated** covering all of the
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
- **Disease Name:** Gastric Cancer H. pylori Associated
- **MONDO ID:**  (if available)
- **Category:**

## Research Objectives

Please provide a comprehensive research report on **Gastric Cancer H. pylori Associated** covering all of the
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


## Comprehensive Research Report: *Helicobacter pylori*–Associated Gastric Cancer

### Target disease
- **Disease name:** Gastric cancer, *H. pylori* associated (primarily non-cardia gastric adenocarcinoma developing in the setting of chronic *Helicobacter pylori* infection) (shirani2024theimmunopathogenesisof pages 1-2, burz2024helicobacterpyloriinfection pages 1-2).
- **Category:** Infection-associated malignancy (bacterial carcinogen-associated), digestive system cancer (stomach).
- **MONDO ID / MeSH / ICD-10/ICD-11:** Not retrievable from the provided tool evidence. The retrieved texts mention that *H. pylori* infection is recognized in ICD-11 contexts, but the specific ICD-11 entity code(s) for “*H. pylori*–associated gastric cancer” were not extractable from the available excerpts (rugge2020gastritisanupdate pages 1-4, burz2024helicobacterpyloriinfection pages 1-2).
- **Common synonyms / alternative names (used in practice/literature):**
  - *H. pylori*–associated gastric cancer; *Helicobacter pylori*–associated gastric adenocarcinoma (shirani2024theimmunopathogenesisof pages 1-2)
  - Infection-associated gastric cancer; inflammation-associated gastric cancer (conceptual framing) (rugge2020gastritisanupdate pages 1-4)
  - Non-cardia gastric cancer arising via the Correa cascade (sun2024overallandcausespecific pages 1-2)
- **Evidence source type in this report:** Primarily aggregated evidence (systematic reviews/meta-analyses, guidelines, large registry/GBD studies), plus large human cohort data; limited mechanistic inference from narrative reviews. No EHR-level patient records were used.

---

## 1. Disease information (overview and current understanding)

### What is the disease?
*H. pylori*–associated gastric cancer refers to gastric carcinoma—most often **non-cardia gastric adenocarcinoma**—arising as a long-term consequence of chronic gastric colonization by *Helicobacter pylori* and the resulting chronic inflammation and mucosal remodeling. Contemporary reviews emphasize that carcinogenesis typically follows a multistep mucosal progression (often termed the **Correa cascade**) from chronic gastritis to atrophy, intestinal metaplasia, dysplasia, and eventually invasive cancer (sun2024overallandcausespecific pages 1-2, areiaUnknownyeargastricprecancerousconditions pages 1-3).

### Key concept definitions
- **Correa cascade (intestinal-type, non-cardia pathway):** A stepwise histopathologic sequence from chronic gastritis → atrophic gastritis → intestinal metaplasia → dysplasia → non-cardia gastric cancer (sun2024overallandcausespecific pages 1-2).
- **Precancerous conditions:** Chronic atrophic gastritis and gastric intestinal metaplasia are repeatedly identified as the principal gastric precancerous states requiring risk stratification and (in selected patients) endoscopic surveillance (pimentelnunes2019managementofepithelial pages 5-6, rugge2020gastritisanupdate pages 1-4).
- **OLGA/OLGIM:** Histology-based staging systems used to grade risk based on extent/severity of atrophy (OLGA) and intestinal metaplasia (OLGIM); advanced stages (III/IV) are used in guidelines to define higher-risk strata and surveillance needs (pimentelnunes2019managementofepithelial pages 13-14, pimentelnunes2019managementofepithelial pages 5-6).

---

## 2. Etiology

### Primary causal factor (infectious)
- *H. pylori* infection is repeatedly described as a major etiologic driver of gastric carcinogenesis, with emphasis on chronic inflammation and bacterial virulence determinants (shirani2024theimmunopathogenesisof pages 1-2, burz2024helicobacterpyloriinfection pages 1-2).

### Bacterial (pathogen) risk determinants
- **CagA/T4SS (cag pathogenicity island):** A 2024 meta-analysis notes that CagA is delivered into host cells by a type IV secretion system (T4SS) “needle-like pilus” mechanism, supporting its role as a virulence effector associated with more severe gastric inflammation and carcinogenesis (naing2024cagatoxinand pages 1-2).
- **Quantified association (CagA positivity):** In observational studies across Indo-Pacific countries, pooled CagA positivity among *H. pylori*–infected gastric disorders was **83%**, and CagA positivity was associated with higher odds of gastric cancer vs gastritis (**OR 2.53, 95% CI 1.15–5.55**) (Naing et al., PLOS ONE, published Aug 2024; DOI: https://doi.org/10.1371/journal.pone.0307172) (naing2024cagatoxinand pages 1-2).
- **Other virulence factors frequently highlighted in recent reviews:** VacA, BabA, SabA, OipA, urease, flagella-mediated motility—important for colonization, persistence, and host pathway perturbation (shirani2024theimmunopathogenesisof pages 1-2).

### Host and environmental risk modifiers (gene–environment and environment)
- The available evidence in this run supports that risk is modulated by population and environmental context (e.g., socioeconomic factors/crowding linked to higher infection prevalence and non-cardia cancer association) (burz2024helicobacterpyloriinfection pages 1-2).
- **Environmental/lifestyle co-factors** (not exhaustively quantified in the provided excerpts) are noted as contributors in reviews: smoking, diet, obesity and other exposures (burz2024helicobacterpyloriinfection pages 1-2).

### Protective factors
- **Eradication of *H. pylori*** is the most consistently supported protective intervention, with randomized trial evidence summarized in meta-analyses showing reduced gastric cancer incidence (wu2025therelationshipbetween pages 1-2).

### Gene–environment interactions
- Mechanistic and immune-pathway reviews emphasize an interaction among bacterial virulence programs, host innate/adaptive immune responses (TLRs/cytokines), and downstream epithelial genetic/epigenetic alterations (shirani2024theimmunopathogenesisof pages 1-2). Specific human susceptibility loci were not extractable from the provided excerpts.

---

## 3. Phenotypes (clinical presentation and natural history)

### Natural history and phenotypic sequence
- **Correa cascade and its clinical significance:** A large population-based Swedish cohort study explicitly frames Correa’s cascade as “chronic non-atrophic gastritis, atrophic gastritis, intestinal metaplasia, and dysplasia” as the “well-recognized pathway for the development of non-cardia gastric cancer” (Sun et al., BMC Medicine, Aug 2024; DOI: https://doi.org/10.1186/s12916-024-03554-1) (sun2024overallandcausespecific pages 1-2).
- **Mortality gradient across lesions:** In that cohort (306,117 patients; ~3.0 million person-years), gastric cancer mortality increased stepwise along the cascade, with “excess risk rising from **105%** for patients with chronic gastritis to **more than 600%** for the dysplasia group” (sun2024overallandcausespecific pages 1-2).
- **Clinical implication (secondary prevention):** The authors conclude that “early recognition and intervention of gastric precancerous lesions probably benefit the patients” (sun2024overallandcausespecific pages 1-2).

### Suggested HPO terms (for KB population)
Because the report is for a disease KB entry, below are suggested phenotype mappings commonly relevant to gastric cancer and/or the precancerous stages; the provided excerpts do not quantify symptom frequencies:
- **Epigastric pain** (HP:0033052)
- **Dyspepsia** (HP:0100544)
- **Nausea** (HP:0002018)
- **Vomiting** (HP:0002013)
- **Weight loss** (HP:0001824)
- **Anemia** (HP:0001903) (often in malignancy/bleeding; not quantified here)
- **Gastrointestinal bleeding** (HP:0002239) / **Melena** (HP:0002249) (context-dependent)
- **Gastritis (histologic/clinical)** (can be represented via relevant ontologies; HPO has “Gastritis” HP:0002032)
- **Intestinal metaplasia** (may be represented via pathology ontologies; HPO has limited granularity for histology)

### Staging frameworks to reference
- Correa cascade (histopathologic)
- OLGA/OLGIM (risk staging) (pimentelnunes2019managementofepithelial pages 13-14)
- Dysplasia grading (low-grade vs high-grade) for management decisions (pimentelnunes2019managementofepithelial pages 10-11)

---

## 4. Genetic / molecular information

### Mechanism/pathophysiology: causal chain (infection → cancer)
A 2024 immunopathogenesis review describes a multi-component cascade involving bacterial colonization factors, virulence determinants, chronic immune activation, and downstream epithelial remodeling/genomic/epigenomic change (shirani2024theimmunopathogenesisof pages 1-2):
1. **Colonization & persistence:** Motility, urease-mediated acid adaptation, and adhesins (e.g., BabA/SabA) support stable mucosal colonization (shirani2024theimmunopathogenesisof pages 1-2).
2. **Delivery of oncogenic/inflammatory effectors:** CagA is injected into host cells via T4SS, and CagA-positive strains are linked to more severe inflammation (naing2024cagatoxinand pages 1-2).
3. **Chronic inflammation and immune dysregulation:** Reviews emphasize innate/adaptive signaling, including TLRs and cytokines, as central mediators that sustain tissue injury and pro-tumor microenvironments (shirani2024theimmunopathogenesisof pages 1-2).
4. **Tissue remodeling and precancerous lesion formation:** Development of atrophic gastritis and intestinal metaplasia creates a “field” permissive for neoplasia; advanced atrophy/metaplasia stages define higher-risk states for surveillance (pimentelnunes2019managementofepithelial pages 5-6, rugge2020gastritisanupdate pages 1-4).
5. **Genetic/epigenetic alteration accumulation:** The immunopathogenesis review highlights “abnormal DNA methylation” and mutation accumulation in carcinogenesis/field cancerization (shirani2024theimmunopathogenesisof pages 1-2).

### Pathways and ontology suggestions (for annotation)
Given the evidence emphasizes inflammation, innate recognition, cytokines, and epithelial remodeling, plausible **GO Biological Process** targets for annotation include:
- **Inflammatory response** (GO:0006954)
- **Innate immune response** (GO:0045087)
- **Toll-like receptor signaling pathway** (e.g., GO:0002224)
- **Cytokine-mediated signaling pathway** (GO:0019221)
- **Regulation of epithelial cell proliferation** (GO:0050673)
- **DNA methylation** (GO:0006306)

**Cell Ontology (CL) suggestions** (prominent in gastric mucosa inflammation/carcinogenesis):
- **Gastric epithelial cell** (context-specific CL term)
- **Macrophage** (CL:0000235)
- **T cell** (CL:0000084)
- **B cell** (CL:0000236)

**Anatomy (UBERON) suggestions:**
- **Stomach** (UBERON:0000945)
- **Gastric mucosa** (UBERON:0001199)
- **Gastric antrum** (UBERON:0001165)
- **Gastric body/corpus** (UBERON:0001163)

### Causal genes / pathogenic variants (host)
Specific germline causal genes/variants for “*H. pylori*–associated gastric cancer” were not extractable from the provided excerpts, which focus on infection-driven carcinogenesis and population risk stratification.

---

## 5. Environmental information

- **Socioeconomic/environmental context:** A 2024 review notes higher *H. pylori* prevalence in crowded/low-socioeconomic settings and links this context particularly to non-cardia gastric cancer risk (burz2024helicobacterpyloriinfection pages 1-2).

---

## 6. Mechanism / pathophysiology (expanded)

### Immune involvement
A 2024 narrative review frames immunopathogenesis as involving bacterial virulence determinants (CagA, VacA, BabA, SabA), TLRs, cytokines, and immune evasion mechanisms as key contributors to chronicity and carcinogenesis (Frontiers in Microbiology, Jul 2024; DOI: https://doi.org/10.3389/fmicb.2024.1395403) (shirani2024theimmunopathogenesisof pages 1-2).

### Epigenetics
The same review highlights epigenetic alterations—particularly abnormal DNA methylation—as part of the progression toward malignant transformation (shirani2024theimmunopathogenesisof pages 1-2).

---

## 7. Anatomical structures affected

- **Primary organ:** Stomach (UBERON:0000945), with emphasis on gastric mucosa and the antrum/corpus compartments for biopsy-based risk staging (pimentelnunes2019managementofepithelial pages 5-6, dinisribeiro2025managementofepithelial pages 6-7).
- **Disease localization:** The Correa cascade is explicitly described as the pathway to **non-cardia gastric cancer** (sun2024overallandcausespecific pages 1-2).

---

## 8. Temporal development

- **Onset pattern:** Chronic, often acquired earlier in life and progressing over decades to precancerous lesions and cancer in a minority of infected individuals; the provided evidence emphasizes multiyear/decade progression rather than acute onset (sun2024overallandcausespecific pages 1-2, areiaUnknownyeargastricprecancerousconditions pages 1-3).
- **Critical periods / intervention window:** Reviews describe a practical “point of no return,” emphasizing that earlier eradication is more likely to prevent irreversible precancerous change (burz2024helicobacterpyloriinfection pages 1-2).

---

## 9. Inheritance and population

### Epidemiology (recent quantitative data)
- **Global burden (GBD 2021, reported in 2024 analysis):** In 2021 there were **1.23 million** new gastric cancer cases and **0.95 million** deaths globally, with **22.79 million DALYs** (Zhang et al., Frontiers in Oncology, Dec 2024; DOI: https://doi.org/10.3389/fonc.2024.1468488) (zhang2024globalregionaland pages 1-2).
- **Sex disparity:** Age-standardized rates in 2021 were substantially higher in men (ASIR **20.9/100,000**) than women (ASIR **8.6/100,000**) (zhang2024globalregionaland pages 1-2).
- **GLOBOCAN 2022 (reported in 2024 early-onset burden paper):** Estimated **968,000** new cases and **660,000** deaths in 2022; East Asia contributed **53.8% of cases** and **48.2% of deaths** (Tan et al., Cancer Biology & Medicine, Aug 2024; DOI: https://doi.org/10.20892/j.issn.2095-3941.2024.0159) (tan2024globalregionaland pages 1-2).

### Infection prevalence context
A 2024 review reiterates global *H. pylori* infection prevalence as ~50% (“Nearly 50% of the global population is infected”) (Burz et al., Cancers, May 2024; DOI: https://doi.org/10.3390/cancers16111958) (burz2024helicobacterpyloriinfection pages 1-2).

---

## 10. Diagnostics

### Diagnosis of *H. pylori* (relevant to cancer prevention)
The MAPS III guideline update emphasizes that first-time diagnostic endoscopy should include gastric biopsies for *H. pylori* diagnosis and for identification/stratification of advanced atrophic gastritis (dinisribeiro2025managementofepithelial pages 6-7).

### Biomarkers / risk stratification tests
- **Pepsinogen (PG I and PG I/II ratio):** MAPS II summarizes that serum pepsinogen testing is among the best-evaluated non-invasive options to detect advanced atrophic gastritis; low PG I and low PG I/II ratio are discussed as thresholds from meta-analytic evaluations, and low PG I (especially with *H. pylori* serology negative) may identify individuals who should be offered endoscopy (pimentelnunes2019managementofepithelial pages 10-11).

### Endoscopic biopsy protocols (guideline-based)
- **MAPS II biopsy concept:** At minimum, biopsies should include at least antrum and corpus sampling; the guideline text also emphasizes chromoendoscopy-guided biopsies for staging and for lesions (pimentelnunes2019managementofepithelial pages 5-6).
- **MAPS III adds implementation detail and virtual chromoendoscopy:** High-quality endoscopy including **virtual chromoendoscopy (VCE)** is recommended for screening/diagnosis/staging of precancerous conditions, and VCE should guide sampling; random biopsies should be taken in the absence of endoscopically suspected changes (dinisribeiro2025managementofepithelial pages 6-7).

### Differential diagnosis
Not explicitly detailed in the retrieved excerpts (e.g., EBV-associated gastric cancer is mentioned elsewhere in the broader corpus but is outside the scope of evidence extracted here).

---

## 11. Outcome / prognosis

- **Lesion severity correlates with elevated mortality risk:** In the Swedish cohort, overall mortality increased with lesion severity (SMR up to **1.54** for dysplasia vs general population), and gastric-cancer–specific mortality rose sharply across the Correa cascade (sun2024overallandcausespecific pages 1-2).

---

## 12. Treatment

### Prevention-relevant treatment: *H. pylori* eradication
Randomized trial evidence summarized in a 2025 meta-analysis (RCT-only) supports eradication as a preventive intervention:
- Overall reduction in gastric cancer incidence: **RR 0.61 (95% CI 0.47–0.79)**; **NNT = 332** (Wu et al., BMC Gastroenterology, Apr 2025; DOI: https://doi.org/10.1186/s12876-025-03886-z) (wu2025therelationshipbetween pages 1-2).
- Healthy adult subgroup: **RR 0.67 (95% CI 0.48–0.93)**; **NNT = 476** (wu2025therelationshipbetween pages 1-2).
- Post-endoscopic mucosal resection subgroup: **RR 0.51 (95% CI 0.36–0.71)**; **NNT = 21** (wu2025therelationshipbetween pages 1-2).

### Post-endoscopic resection (metachronous lesions)
A 2024 systematic review/meta-analysis focusing on Japan and Korea supports reduced metachronous gastric lesions after successful eradication vs persistent infection (**RR 0.54, 95% CI 0.44–0.65**) (Yu et al., Frontiers in Medicine, Sep 2024; DOI: https://doi.org/10.3389/fmed.2024.1393498) (wu2025therelationshipbetween pages 1-2).

### MAXO (Medical Action Ontology) suggestions
- **Antibiotic therapy** (eradication regimens; MAXO term to be mapped)
- **Endoscopic surveillance**
- **Upper gastrointestinal endoscopy**
- **Endoscopic mucosal resection / endoscopic submucosal dissection** (for early neoplasia/precursor lesions per MAPS guidelines)

*Note:* Detailed systemic therapy for established gastric cancer (e.g., specific chemotherapy regimens, anti-HER2, anti-VEGFR2, PD-1 inhibitors) was not supported by the retrieved excerpts in this run; therefore, it is not asserted here.

---

## 13. Prevention

### Primary prevention
- **Eradication of confirmed *H. pylori* infection** is repeatedly framed as the leading strategy for primary prevention of gastric cancer (rugge2020gastritisanupdate pages 1-4, wu2025therelationshipbetween pages 1-2).

### Secondary prevention (screening/surveillance of precancerous lesions)
Guidelines emphasize risk stratification and targeted surveillance:
- **MAPS II (2019) surveillance principles:**
  - “For patients with mild to moderate atrophy restricted to the antrum there is no evidence to recommend surveillance.” (Endoscopy, Mar 2019; DOI: https://doi.org/10.1055/a-0859-1883) (pimentelnunes2019managementofepithelial pages 5-6).
  - Surveillance may be considered at **3 years** for single-location intestinal metaplasia with risk factors (family history, incomplete IM, persistent *H. pylori*) (pimentelnunes2019managementofepithelial pages 5-6).
  - For dysplasia without a visible lesion, high-quality reassessment with chromoendoscopy is recommended; if no lesion is found, surveillance at **6 months (HGD)** and **12 months (LGD)** is recommended (pimentelnunes2019managementofepithelial pages 10-11).
- **MAPS III (2025) population screening stratification:**
  - High-risk regions (gastric cancer ASR **>20/100,000 person-years**): screening every **2–3 years**; intermediate risk (ASR **10–20**): every **5 years** (Dinis-Ribeiro et al., Endoscopy, 2025; DOI: https://doi.org/10.1055/a-2529-5025) (dinisribeiro2025managementofepithelial pages 16-17).
  - Screening/surveillance in asymptomatic individuals **>80 years** should be discontinued or not started (dinisribeiro2025managementofepithelial pages 6-7).

### Real-world implementations and uptake
- **European implementation evidence (practice audit):** After MAPS I/II introduction, virtual chromoendoscopy adoption rose (4 of 9 centers using it in **>50%** of endoscopies), and systematic biopsies (antrum/corpus ± incisura) increased (4 centers performing antrum+corpus+incisura biopsies in **>90%** of cases) (Fontes et al., Endoscopy, Sep 2025; DOI: https://doi.org/10.1055/a-2695-1376) (fontes2025adherencetoclinical pages 1-2).
- **Country-level early detection performance (implementation proxy):** A GLOBOCAN 2022-based report notes early diagnosis rates **>70%** in Japan and South Korea vs ~**20%** in China (lu2025globalepidemiologyof pages 1-4).

---

## 14. Other species / natural disease
Not addressed in the retrieved evidence excerpts.

---

## 15. Model organisms
Not fully developed in the retrieved evidence excerpts in this run. (The paper search retrieved an animal-model review, but supporting evidence passages were not extracted with tool citations in this run.)

---

## Key quantitative findings and guideline recommendations (summary table)

| Domain | Key finding (with numbers) | Population/context | Source (first author, journal, year) | Publication date (month/year) | URL/DOI | Tool citation id |
|---|---|---|---|---|---|---|
| Epidemiology | 2021 global burden: **1.23 million new cases**, **0.95 million deaths**, **22.79 million DALYs** | Global gastric cancer burden, GBD 2021 | Zhang, *Frontiers in Oncology*, 2024 | 12/2024 | https://doi.org/10.3389/fonc.2024.1468488 | (zhang2024globalregionaland pages 1-2) |
| Epidemiology | Male burden exceeded female burden: **ASIR 20.9 vs 8.6/100,000**, **ASMR 16.0 vs 7.1/100,000**, age-standardized DALY rate **371.2 vs 165.6/100,000** | Global, sex-stratified GBD 2021 estimates | Zhang, *Frontiers in Oncology*, 2024 | 12/2024 | https://doi.org/10.3389/fonc.2024.1468488 | (zhang2024globalregionaland pages 1-2) |
| Epidemiology | 2022 global estimates: **968,194 new cases** and **659,944 deaths**; male ASIR **12.8/100,000** vs female **6.0/100,000** | Global gastric cancer burden, GLOBOCAN 2022-based analysis | Lu, preprint/unknown journal, 2025 | 12/2025 | https://doi.org/10.21203/rs.3.rs-8058648/v1 | (lu2025globalepidemiologyof pages 1-4) |
| Epidemiology | East Asia accounted for **53.8% of cases** and **48.2% of deaths** globally | Geographic distribution, GLOBOCAN 2022-based analysis | Tan, *Cancer Biology & Medicine*, 2024 | 08/2024 | https://doi.org/10.20892/j.issn.2095-3941.2024.0159 | (tan2024globalregionaland pages 1-2) |
| Virulence-factor risk | Among H. pylori-infected gastric disorders, pooled **CagA positivity was 83%** overall; **78%** in gastritis, **86%** in peptic ulcer disease, **83%** in gastric cancer | 24 observational studies from 8 Indo-Pacific countries | Naing, *PLOS ONE*, 2024 | 08/2024 | https://doi.org/10.1371/journal.pone.0307172 | (naing2024cagatoxinand pages 1-2) |
| Virulence-factor risk | **CagA-positive** infection was associated with increased odds of gastric cancer vs gastritis: **OR 2.53 (95% CI 1.15–5.55)** | H. pylori-infected individuals in Indo-Pacific observational studies | Naing, *PLOS ONE*, 2024 | 08/2024 | https://doi.org/10.1371/journal.pone.0307172 | (naing2024cagatoxinand pages 1-2) |
| Eradication benefit | Eradication reduced gastric cancer incidence: **RR 0.61 (95% CI 0.47–0.79)**; **NNT 332** | 11 RCTs, **104,786** participants | Wu, *BMC Gastroenterology*, 2025 | 04/2025 | https://doi.org/10.1186/s12876-025-03886-z | (wu2025therelationshipbetween pages 1-2) |
| Eradication benefit | In healthy adults, eradication reduced gastric cancer risk: **RR 0.67 (95% CI 0.48–0.93)**; **NNT 476** | Healthy H. pylori-positive adults in RCT subgroup | Wu, *BMC Gastroenterology*, 2025 | 04/2025 | https://doi.org/10.1186/s12876-025-03886-z | (wu2025therelationshipbetween pages 1-2) |
| Eradication benefit | After endoscopic mucosal resection, eradication reduced gastric cancer risk: **RR 0.51 (95% CI 0.36–0.71)**; **NNT 21** | Post-EMR patients in RCT subgroup | Wu, *BMC Gastroenterology*, 2025 | 04/2025 | https://doi.org/10.1186/s12876-025-03886-z | (wu2025therelationshipbetween pages 1-2) |
| Eradication benefit | After endoscopic resection, successful eradication lowered metachronous gastric lesion risk vs persistent infection: **RR 0.54 (95% CI 0.44–0.65)** | 21 studies, **82,256** observations from Japan/Korea | Yu, *Frontiers in Medicine*, 2024 | 09/2024 | https://doi.org/10.3389/fmed.2024.1393498 | (wu2025therelationshipbetween pages 1-2) |
| Surveillance guideline | **No surveillance** recommended for mild-to-moderate atrophy restricted to the antrum | MAPS II management of gastric precancerous lesions | Pimentel-Nunes, *Endoscopy*, 2019 | 03/2019 | https://doi.org/10.1055/a-0859-1883 | (pimentelnunes2019managementofepithelial pages 5-6) |
| Surveillance guideline | For single-location intestinal metaplasia with family history, incomplete IM, or persistent H. pylori, surveillance with chromoendoscopy and guided biopsies may be considered at **3 years** | Higher-risk intestinal metaplasia | Pimentel-Nunes, *Endoscopy*, 2019 | 03/2019 | https://doi.org/10.1055/a-0859-1883 | (pimentelnunes2019managementofepithelial pages 5-6) |
| Surveillance guideline | Patients with advanced atrophic gastritis / OLGA-OLGIM **III/IV** should undergo high-quality endoscopy every **3 years** | Advanced precancerous lesions | Pimentel-Nunes, *Endoscopy*, 2019 | 03/2019 | https://doi.org/10.1055/a-0859-1883 | (pimentelnunes2019managementofepithelial pages 13-14, pimentelnunes2019managementofepithelial pages 5-6, pimentelnunes2019managementofepithelial pages 1-2) |
| Surveillance guideline | If dysplasia is present without a visible lesion: repeat high-quality endoscopy with chromoendoscopy; if still no lesion, surveillance at **6 months for high-grade dysplasia** and **12 months for low-grade dysplasia** | Non-visible gastric dysplasia | Pimentel-Nunes, *Endoscopy*, 2019 | 03/2019 | https://doi.org/10.1055/a-0859-1883 | (pimentelnunes2019managementofepithelial pages 10-11) |
| Screening implementation | Population endoscopic screening suggested every **2–3 years** in high-risk regions with gastric cancer **ASR >20/100,000 person-years**, and every **5 years** in intermediate-risk regions with **ASR 10–20/100,000** | MAPS III population-level screening framework | Dinis-Ribeiro, *Endoscopy*, 2025 | 03/2025 | https://doi.org/10.1055/a-2529-5025 | (dinisribeiro2025managementofepithelial pages 16-17) |
| Screening implementation | For first-degree relatives of gastric cancer patients: noninvasive H. pylori screening/eradication at ages **20–30**; endoscopic screening at age **45** or **10 years before** the relative’s diagnosis | Familial-risk strategy | Dinis-Ribeiro, *Endoscopy*, 2025 | 03/2025 | https://doi.org/10.1055/a-2529-5025 | (dinisribeiro2025managementofepithelial pages 6-7) |
| Screening implementation | Screening/surveillance in asymptomatic individuals **>80 years** should be discontinued or not started | MAPS III age threshold | Dinis-Ribeiro, *Endoscopy*, 2025 | 03/2025 | https://doi.org/10.1055/a-2529-5025 | (dinisribeiro2025managementofepithelial pages 6-7) |
| Screening implementation | Real-world adherence data: virtual chromoendoscopy use improved in **6 centers**, with **4 centers >50%** use; **4 centers** performed antrum+corpus+incisura biopsies in **>90%** of cases | European multicenter practice audit across 2010/11, 2017/18, 2022/23 | Fontes, *Endoscopy*, 2025 | 09/2025 | https://doi.org/10.1055/a-2695-1376 | (fontes2025adherencetoclinical pages 1-2) |
| Screening implementation | Early diagnosis rates reported as **>70%** in Japan and South Korea vs about **20%** in China | Country-level implementation differences in gastric cancer detection | Lu, preprint/unknown journal, 2025 | 12/2025 | https://doi.org/10.21203/rs.3.rs-8058648/v1 | (lu2025globalepidemiologyof pages 1-4) |


*Table: This table compiles the main numeric findings and actionable guideline points for H. pylori–associated gastric cancer from the retrieved evidence. It is useful for quickly comparing burden estimates, virulence-associated risk, benefits of eradication, and current surveillance/screening recommendations.*

---

## Visual evidence: MAPS II surveillance algorithm
A figure from MAPS II showing an OLGA/OLGIM-based surveillance algorithm (including interval tiers) was retrieved (pimentelnunes2019managementofepithelial media 670f31ad).

---

## Expert synthesis (authoritative interpretation)
1. **Causality plus actionability:** Across guidelines and meta-analyses, the most actionable point is that *H. pylori*–driven gastric carcinogenesis is a long-latency process with identifiable intermediate states (atrophy, intestinal metaplasia, dysplasia) that can be risk-staged and surveilled (pimentelnunes2019managementofepithelial pages 5-6, dinisribeiro2025managementofepithelial pages 6-7, sun2024overallandcausespecific pages 1-2).
2. **Eradication has measurable preventive effect sizes:** RCT-only evidence synthesis supports a meaningful relative reduction in gastric cancer incidence with eradication (RR ~0.61 overall; strong effect after endoscopic resection with low NNT) (wu2025therelationshipbetween pages 1-2).
3. **Implementation gap is narrowing but persists:** Real-world European audits show improved use of guideline-recommended approaches (VCE, biopsy protocols), implying feasible implementation pathways but also remaining gaps in standardized risk scoring and surveillance adherence (fontes2025adherencetoclinical pages 1-2).

---

## Limitations of this evidence package
- **PMIDs:** The tool-extracted snippets largely provided DOIs and journal metadata but did not include PubMed IDs. Consequently, PMID-preferred citations could not be supplied from the available evidence.
- **Ontology IDs (MONDO/MeSH/ICD):** Specific identifiers for the exact disease concept “*H. pylori*–associated gastric cancer” were not retrievable in the current evidence excerpts.
- **Systemic therapy for established gastric cancer:** Not covered by extracted evidence; therefore omitted to avoid uncited claims.



References

1. (shirani2024theimmunopathogenesisof pages 1-2): Maryam Shirani, Saeedeh Shariati, Monireh Bazdar, Faezeh Sojoudi Ghamnak, Melika Moradi, Reyhane Shams Khozani, Elahe Taki, Zahra Arabsorkhi, Mohsen Heidary, and Dorsa Bahrami Eskandari. The immunopathogenesis of helicobacter pylori-induced gastric cancer: a narrative review. Frontiers in Microbiology, Jul 2024. URL: https://doi.org/10.3389/fmicb.2024.1395403, doi:10.3389/fmicb.2024.1395403. This article has 22 citations and is from a peer-reviewed journal.

2. (burz2024helicobacterpyloriinfection pages 1-2): Claudia Burz, Vlad Pop, Ciprian Silaghi, Iulia Lupan, and Gabriel Samasca. Helicobacter pylori infection in patients with gastric cancer: a 2024 update. Cancers, 16:1958, May 2024. URL: https://doi.org/10.3390/cancers16111958, doi:10.3390/cancers16111958. This article has 7 citations.

3. (rugge2020gastritisanupdate pages 1-4): Massimo Rugge, Kentaro Sugano, Diana Sacchi, Marta Sbaraglia, and Peter Malfertheiner. Gastritis: an update in 2020. Current Treatment Options in Gastroenterology, 18:488-503, Aug 2020. URL: https://doi.org/10.1007/s11938-020-00298-8, doi:10.1007/s11938-020-00298-8. This article has 12 citations.

4. (sun2024overallandcausespecific pages 1-2): Yawen Sun, Li Yin, Dariush Nasrollahzadeh Nesheli, Jingru Yu, Joar Franzén, and Weimin Ye. Overall and cause-specific mortality among patients diagnosed with gastric precancerous lesions in sweden between 1979 and 2014: an observational cohort study. BMC Medicine, Aug 2024. URL: https://doi.org/10.1186/s12916-024-03554-1, doi:10.1186/s12916-024-03554-1. This article has 8 citations and is from a domain leading peer-reviewed journal.

5. (areiaUnknownyeargastricprecancerousconditions pages 1-3): M Areia and M Dinis-Ribeiro. Gastric precancerous conditions or lesions and helicobacter pylori. Unknown journal, Unknown year.

6. (pimentelnunes2019managementofepithelial pages 5-6): Pedro Pimentel-Nunes, Diogo Libânio, Ricardo Marcos-Pinto, Miguel Areia, Marcis Leja, Gianluca Esposito, Monica Garrido, Ilze Kikuste, Francis Megraud, Tamara Matysiak-Budnik, Bruno Annibale, Jean-Marc Dumonceau, Rita Barros, Jean-François Fléjou, Fátima Carneiro, Jeanin van Hooft, Ernst Kuipers, and Mario Dinis-Ribeiro. Management of epithelial precancerous conditions and lesions in the stomach (maps ii): european society of gastrointestinal endoscopy (esge), european helicobacter and microbiota study group (ehmsg), european society of pathology (esp), and sociedade portuguesa de endoscopia digestiva (sped) guideli. Endoscopy, 51 4:365-388, Mar 2019. URL: https://doi.org/10.1055/a-0859-1883, doi:10.1055/a-0859-1883. This article has 1252 citations and is from a domain leading peer-reviewed journal.

7. (pimentelnunes2019managementofepithelial pages 13-14): Pedro Pimentel-Nunes, Diogo Libânio, Ricardo Marcos-Pinto, Miguel Areia, Marcis Leja, Gianluca Esposito, Monica Garrido, Ilze Kikuste, Francis Megraud, Tamara Matysiak-Budnik, Bruno Annibale, Jean-Marc Dumonceau, Rita Barros, Jean-François Fléjou, Fátima Carneiro, Jeanin van Hooft, Ernst Kuipers, and Mario Dinis-Ribeiro. Management of epithelial precancerous conditions and lesions in the stomach (maps ii): european society of gastrointestinal endoscopy (esge), european helicobacter and microbiota study group (ehmsg), european society of pathology (esp), and sociedade portuguesa de endoscopia digestiva (sped) guideli. Endoscopy, 51 4:365-388, Mar 2019. URL: https://doi.org/10.1055/a-0859-1883, doi:10.1055/a-0859-1883. This article has 1252 citations and is from a domain leading peer-reviewed journal.

8. (naing2024cagatoxinand pages 1-2): Cho Naing, Htar Htar Aung, Saint Nway Aye, Yong Poovorawan, and Maxine A. Whittaker. Caga toxin and risk of helicobacter pylori-infected gastric phenotype: a meta-analysis of observational studies. PLOS ONE, 19:e0307172, Aug 2024. URL: https://doi.org/10.1371/journal.pone.0307172, doi:10.1371/journal.pone.0307172. This article has 13 citations and is from a peer-reviewed journal.

9. (wu2025therelationshipbetween pages 1-2): Zhouhan Wu, Yi Tang, Meiwen Tang, Zhoutong Wu, and Yonghui Xu. The relationship between the eradication of helicobacter pylori and the occurrence of stomach cancer: an updated meta-analysis and systemic review. BMC Gastroenterology, Apr 2025. URL: https://doi.org/10.1186/s12876-025-03886-z, doi:10.1186/s12876-025-03886-z. This article has 18 citations and is from a peer-reviewed journal.

10. (pimentelnunes2019managementofepithelial pages 10-11): Pedro Pimentel-Nunes, Diogo Libânio, Ricardo Marcos-Pinto, Miguel Areia, Marcis Leja, Gianluca Esposito, Monica Garrido, Ilze Kikuste, Francis Megraud, Tamara Matysiak-Budnik, Bruno Annibale, Jean-Marc Dumonceau, Rita Barros, Jean-François Fléjou, Fátima Carneiro, Jeanin van Hooft, Ernst Kuipers, and Mario Dinis-Ribeiro. Management of epithelial precancerous conditions and lesions in the stomach (maps ii): european society of gastrointestinal endoscopy (esge), european helicobacter and microbiota study group (ehmsg), european society of pathology (esp), and sociedade portuguesa de endoscopia digestiva (sped) guideli. Endoscopy, 51 4:365-388, Mar 2019. URL: https://doi.org/10.1055/a-0859-1883, doi:10.1055/a-0859-1883. This article has 1252 citations and is from a domain leading peer-reviewed journal.

11. (dinisribeiro2025managementofepithelial pages 6-7): M. Dinis-Ribeiro, D. Libânio, Hugo I. Uchima, M. Spaander, Jan Bornschein, Tamara Matysiak-Budnik, G. Tziatzios, J. Santos-Antunes, M. Areia, N. Chapelle, Gianluca Esposito, Glòria Fernández-Esparrach, L. Kunovský, M. Garrido, I. Tachecí, Alexander Link, Pedro Marcos, R. Marcos-Pinto, L. Moreira, Ana Carina Pereira, Pedro Pimentel-Nunes, Marcin Romańczyk, Filipa Fontes, C. Hassan, R. Bisschops, R. Feakins, Christian Schulz, K. Triantafyllou, Fatima Carneiro, and Ernst J Kuipers. Management of epithelial precancerous conditions and early neoplasia of the stomach (maps iii): european society of gastrointestinal endoscopy (esge), european helicobacter and microbiota study group (ehmsg) and european society of pathology (esp) guideline update 2025. Endoscopy, Mar 2025. URL: https://doi.org/10.1055/a-2529-5025, doi:10.1055/a-2529-5025. This article has 130 citations and is from a domain leading peer-reviewed journal.

12. (zhang2024globalregionaland pages 1-2): Tao Zhang, Yiqun Zhang, and Xiaofei Leng. Global, regional, and national trends in gastric cancer burden: 1990-2021 and projections to 2040. Frontiers in Oncology, Dec 2024. URL: https://doi.org/10.3389/fonc.2024.1468488, doi:10.3389/fonc.2024.1468488. This article has 10 citations.

13. (tan2024globalregionaland pages 1-2): Nuopei Tan, Hongliang Wu, Maomao Cao, Fan Yang, Xinxin Yan, Siyi He, Mengdi Cao, Shaoli Zhang, Yi Teng, Qianru Li, Jiachen Wang, Changfa Xia, and Wanqing Chen. Global, regional, and national burden of early-onset gastric cancer. Cancer Biology & Medicine, 21:667-678, Aug 2024. URL: https://doi.org/10.20892/j.issn.2095-3941.2024.0159, doi:10.20892/j.issn.2095-3941.2024.0159. This article has 54 citations.

14. (dinisribeiro2025managementofepithelial pages 16-17): M. Dinis-Ribeiro, D. Libânio, Hugo I. Uchima, M. Spaander, Jan Bornschein, Tamara Matysiak-Budnik, G. Tziatzios, J. Santos-Antunes, M. Areia, N. Chapelle, Gianluca Esposito, Glòria Fernández-Esparrach, L. Kunovský, M. Garrido, I. Tachecí, Alexander Link, Pedro Marcos, R. Marcos-Pinto, L. Moreira, Ana Carina Pereira, Pedro Pimentel-Nunes, Marcin Romańczyk, Filipa Fontes, C. Hassan, R. Bisschops, R. Feakins, Christian Schulz, K. Triantafyllou, Fatima Carneiro, and Ernst J Kuipers. Management of epithelial precancerous conditions and early neoplasia of the stomach (maps iii): european society of gastrointestinal endoscopy (esge), european helicobacter and microbiota study group (ehmsg) and european society of pathology (esp) guideline update 2025. Endoscopy, Mar 2025. URL: https://doi.org/10.1055/a-2529-5025, doi:10.1055/a-2529-5025. This article has 130 citations and is from a domain leading peer-reviewed journal.

15. (fontes2025adherencetoclinical pages 1-2): Filipa Fontes, Noa E. A. Kapteijn, Cesare Hassan, Charlene Deane, Margarida Cristiano, Henrique Fernandes-Mendes, Irina Luzko, Maša Čavlina Sevo, Orlaith Kelly, Gianluca Esposito, I Lisanne Holster, Michiel P. J. van der Horst, Charlotte F. Kweldam, Andrei Voiosu, Ricardo Marcos Pinto, Nuno Almeida, Colm O'Morain, Leticia Moreira, Jan Bornschein, Manon C.W. Spaander, and Mário Dinis-Ribeiro. Adherence to clinical practice guidelines for management of epithelial precancerous conditions and lesions in the stomach in europe. Endoscopy, 57:1338-1347, Sep 2025. URL: https://doi.org/10.1055/a-2695-1376, doi:10.1055/a-2695-1376. This article has 2 citations and is from a domain leading peer-reviewed journal.

16. (lu2025globalepidemiologyof pages 1-4): Bingyun Lu, Dongjing Zhang, Qizhen Liu, Xuanxuan Zuo, and Ye Chen. Global epidemiology of gastric cancer in 2022 and projections for 2050: a comprehensive analysis and forecasts based on globocan data. Unknown journal, Dec 2025. URL: https://doi.org/10.21203/rs.3.rs-8058648/v1, doi:10.21203/rs.3.rs-8058648/v1.

17. (pimentelnunes2019managementofepithelial pages 1-2): Pedro Pimentel-Nunes, Diogo Libânio, Ricardo Marcos-Pinto, Miguel Areia, Marcis Leja, Gianluca Esposito, Monica Garrido, Ilze Kikuste, Francis Megraud, Tamara Matysiak-Budnik, Bruno Annibale, Jean-Marc Dumonceau, Rita Barros, Jean-François Fléjou, Fátima Carneiro, Jeanin van Hooft, Ernst Kuipers, and Mario Dinis-Ribeiro. Management of epithelial precancerous conditions and lesions in the stomach (maps ii): european society of gastrointestinal endoscopy (esge), european helicobacter and microbiota study group (ehmsg), european society of pathology (esp), and sociedade portuguesa de endoscopia digestiva (sped) guideli. Endoscopy, 51 4:365-388, Mar 2019. URL: https://doi.org/10.1055/a-0859-1883, doi:10.1055/a-0859-1883. This article has 1252 citations and is from a domain leading peer-reviewed journal.

18. (pimentelnunes2019managementofepithelial media 670f31ad): Pedro Pimentel-Nunes, Diogo Libânio, Ricardo Marcos-Pinto, Miguel Areia, Marcis Leja, Gianluca Esposito, Monica Garrido, Ilze Kikuste, Francis Megraud, Tamara Matysiak-Budnik, Bruno Annibale, Jean-Marc Dumonceau, Rita Barros, Jean-François Fléjou, Fátima Carneiro, Jeanin van Hooft, Ernst Kuipers, and Mario Dinis-Ribeiro. Management of epithelial precancerous conditions and lesions in the stomach (maps ii): european society of gastrointestinal endoscopy (esge), european helicobacter and microbiota study group (ehmsg), european society of pathology (esp), and sociedade portuguesa de endoscopia digestiva (sped) guideli. Endoscopy, 51 4:365-388, Mar 2019. URL: https://doi.org/10.1055/a-0859-1883, doi:10.1055/a-0859-1883. This article has 1252 citations and is from a domain leading peer-reviewed journal.
