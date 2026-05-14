---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-10T04:45:41.218315'
end_time: '2026-05-10T04:58:42.174689'
duration_seconds: 780.96
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Metastatic Renal Cell Carcinoma
  mondo_id: ''
  category: ''
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 34
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Metastatic Renal Cell Carcinoma
- **MONDO ID:**  (if available)
- **Category:**

## Research Objectives

Please provide a comprehensive research report on **Metastatic Renal Cell Carcinoma** covering all of the
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
- **Disease Name:** Metastatic Renal Cell Carcinoma
- **MONDO ID:**  (if available)
- **Category:**

## Research Objectives

Please provide a comprehensive research report on **Metastatic Renal Cell Carcinoma** covering all of the
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


## Comprehensive Research Report: Metastatic Renal Cell Carcinoma (mRCC)

### Target Disease
- **Disease name:** Metastatic renal cell carcinoma (mRCC)
- **Category:** Malignant neoplasm; metastatic solid tumor (kidney primary)
- **MONDO ID:** Not directly retrieved for the *metastatic* entity in the current tool context. (A related kidney cancer term in the retrieved OpenTargets context is **MONDO_0007763** “nonpapillary renal cell carcinoma”, but this is not specific to metastasis.) (OpenTargets Search: renal cell carcinoma)

---

## 1. Disease Information

### 1.1 Overview / definition
Metastatic renal cell carcinoma (mRCC) refers to renal cell carcinoma that has spread beyond the kidney to distant organs (stage IV disease), typically requiring systemic therapy and multidisciplinary management; it remains “mainly treated palliatively” despite major therapeutic advances. (ivanyi2024thetreatmentof pages 1-2)

A clinically important modern framing is that mRCC treatment is dominated by **immune checkpoint inhibitor (ICI) combinations** (ICI–ICI or ICI–TKI), with additional local therapies (e.g., cytoreductive nephrectomy, metastasectomy, radiotherapy) considered case-by-case by a multidisciplinary tumor board. (ivanyi2024thetreatmentof pages 1-2, bloise2024firstlinetreatmentsand pages 2-4)

**Primary histology context:** RCC encompasses many subtypes; a 2024 review notes the WHO classification includes **39 RCC subtypes**, and **clear-cell RCC** is the most common (~80%). (ivanyi2024thetreatmentof pages 1-2)

**Abstract quote (definition/setting):** “in 20–30% of cases, metastatic RCC (mRCC) is already present at the time of diagnosis. This disease in the metastatic stage is still mainly treated palliatively…” (ivanyi2024thetreatmentof pages 1-2)

### 1.2 Key identifiers / coding systems
Within retrieved evidence, explicit ICD-10/ICD-11, MeSH, Orphanet, or OMIM identifiers for the metastatic entity were **not** present. OpenTargets returned disease IDs for broader RCC entities (e.g., EFO_0000681 “renal cell carcinoma”, EFO_0005708 “renal cell adenocarcinoma”). (OpenTargets Search: renal cell carcinoma)

### 1.3 Synonyms / alternative names
Commonly used equivalents in the retrieved literature include:
- “advanced renal cell carcinoma” (aRCC) (powles2024nivolumabpluscabozantinib pages 1-2, yanagisawa2024updatedsystematicreview pages 4-4)
- “advanced or metastatic renal cell carcinoma” (powles2024nivolumabpluscabozantinib pages 1-2)
- “metastatic clear cell RCC (mccRCC)” (meng2023emergingimmunotherapyapproaches pages 5-6)

### 1.4 Evidence source types
This report integrates:
- **Aggregated disease-level resources and reviews** (systematic reviews/meta-analyses; guideline-focused reviews) (yanagisawa2024updatedsystematicreview pages 4-4, ivanyi2024thetreatmentof pages 1-2)
- **Randomized phase III trials and updates** (CheckMate 9ER, CLEAR, COSMIC-313) (powles2024nivolumabpluscabozantinib pages 1-2, choueiri2023cabozantinibplusnivolumab pages 1-3, yanagisawa2024updatedsystematicreview pages 4-4)
- **Regulatory evidence** (FDA approval summary for belzutifan) (fallah2024fdaapprovalsummary pages 1-3)
- **Real-world observational cohorts** (metastatic site frequencies; real-world survival) (lee2024sitesofmetastasis pages 1-2, almansour2024realworldsurvivaloutcomes pages 1-2)
- **Single-cell translational studies** (bone-metastatic microenvironment) (ma2024singlecellprofilingof pages 1-2)

---

## 2. Etiology

### 2.1 Disease causal factors (mechanistic)
Clear-cell RCC is strongly linked to dysregulation of hypoxia/angiogenesis programs (VHL–HIF signaling), which underlies the historic and current success of anti-angiogenic therapy and the newer HIF-2α inhibitor class. (OpenTargets Search: renal cell carcinoma, fallah2024fdaapprovalsummary pages 1-3)

OpenTargets disease–target associations highlight canonical RCC genes/targets (e.g., **VHL, PBRM1, TP53, MET, MTOR**) associated with renal cell carcinoma/adenocarcinoma. (OpenTargets Search: renal cell carcinoma)

### 2.2 Risk factors (recent quantitative data)
Although these risk-factor studies are not restricted to metastatic disease, they inform upstream RCC incidence (and therefore mRCC burden).

**Metabolic syndrome and components (UK Biobank, 2024):**
- Cohort: **355,678** participants, median follow-up **11 years**, **1,203** kidney cancer cases. (wang2024associationbetweenmetabolic pages 1-2)
- Risk vs metabolically healthy:
  - **pre-MetS** HR **1.36** (95% CI **1.06–1.74**) (wang2024associationbetweenmetabolic pages 1-2)
  - **MetS** HR **1.70** (95% CI **1.30–2.23**) (wang2024associationbetweenmetabolic pages 1-2)
- Highest-risk component pattern reported: **BP + HDL + WC** HR **3.03** (95% CI **1.91–4.80**). (wang2024associationbetweenmetabolic pages 5-6)
- Joint effect with genetics: MetS + high polygenic risk score (PRS) HR **1.74** (95% CI **1.41–2.14**) vs non‑MetS + low PRS, suggesting combined contribution of metabolic and inherited susceptibility. (wang2024associationbetweenmetabolic pages 1-2, wang2024associationbetweenmetabolic pages 5-6)

**Dietary pattern (ultra-processed foods; PLCO cohort, 2024):**
- Cohort: ~**101,688** participants; **410** RCC cases over **899,731 person-years** (median follow-up **9.41 years**) and **230** RCC deaths over **1,533,930 person-years** (median follow-up **16.85 years**). (li2024ultraprocessedfoodconsumption pages 1-2)
- Highest vs lowest quartile of ultra-processed food consumption:
  - RCC incidence HR **1.42** (95% CI **1.06–1.91**) (li2024ultraprocessedfoodconsumption pages 1-2)
  - RCC mortality HR **1.64** (95% CI **1.10–2.43**) (li2024ultraprocessedfoodconsumption pages 1-2)

**Air pollution (systematic review/meta-analysis, 2024; search through March 23, 2023):**
- Per **10 µg/m³** increase:
  - PM10 HR **1.29** (95% CI **1.10–1.51**) (dahman2024airpollutionand pages 1-3)
  - NO2 HR **1.10** (95% CI **1.03–1.18**) (dahman2024airpollutionand pages 1-3)

### 2.3 Protective factors
No specific protective factors with effect sizes were identified in the retrieved texts.

### 2.4 Gene–environment interactions
The UK Biobank analysis explicitly evaluated combined MetS and genetic risk. It reported that **MetS plus high PRS** conferred higher kidney cancer risk (HR **1.74**, 95% CI **1.41–2.14**), consistent with a joint contribution of metabolic exposures and polygenic risk to kidney cancer incidence. (wang2024associationbetweenmetabolic pages 1-2, wang2024associationbetweenmetabolic pages 5-6)

---

## 3. Phenotypes (clinical presentation)
**Note:** The retrieved evidence set is treatment- and outcomes-focused and contains limited structured symptom/lab phenotype frequencies for mRCC. Below is a minimal phenotype set consistent with clinical context, plus ontology suggestions.

### 3.1 Common clinical features (limited evidence in retrieved texts)
A 2024 review notes that only ~**20%** of RCC patients have “typical symptoms” at presentation (implying many are asymptomatic until advanced). (ivanyi2024thetreatmentof pages 1-2)

### 3.2 Suggested phenotype ontology mappings (HPO suggestions)
(These are ontology suggestions for knowledge-base structuring; frequencies were not extractable from retrieved sources.)
- Hematuria — **HP:0000790**
- Flank pain — **HP:0030765**
- Abdominal mass — **HP:0003278**
- Weight loss — **HP:0001824**
- Fatigue — **HP:0012378**
- Anemia (common on therapy and in advanced disease) — **HP:0001903**
- Bone pain (bone metastasis) — **HP:0002653**
- Dyspnea (lung metastasis or treatment toxicity) — **HP:0002094**

### 3.3 Quality of life impact
Not directly quantified in retrieved texts; however, mRCC therapy is associated with high adverse-event burdens (e.g., grade ≥3 AEs) which plausibly affects QoL. (powles2024nivolumabpluscabozantinib pages 1-2, choueiri2023cabozantinibplusnivolumab pages 1-3, fallah2024fdaapprovalsummary pages 1-3)

---

## 4. Genetic / Molecular Information

### 4.1 Key genes (somatic drivers and hereditary predisposition; from OpenTargets)
OpenTargets RCC associations include genes central to RCC biology and hereditary syndromes, including **VHL**, **PBRM1**, **FLCN**, **MET**, **MTOR**, **SETD2**, **KDM5C**, **TFE3**, and **BAP1** (depending on RCC subtype mapping in OpenTargets). (OpenTargets Search: renal cell carcinoma)

**Ontology suggestions:**
- HGNC symbols: VHL, PBRM1, BAP1, SETD2, MTOR, MET

### 4.2 Pathways (mechanistic anchors)
- Hypoxia signaling / HIF-2α axis (targeted by belzutifan) (fallah2024fdaapprovalsummary pages 1-3)
- Angiogenesis (VEGF pathway; inferred from clinical efficacy of VEGFR-TKI combinations in first-line trials) (powles2024nivolumabpluscabozantinib pages 1-2, yanagisawa2024updatedsystematicreview pages 4-4)
- Immune evasion / immune checkpoint pathways (PD-1/PD-L1, CTLA-4 targeted by nivolumab, pembrolizumab, ipilimumab) (powles2024nivolumabpluscabozantinib pages 1-2, choueiri2023cabozantinibplusnivolumab pages 1-3, yanagisawa2024updatedsystematicreview pages 4-4)

**GO suggestions (biological process):**
- Angiogenesis — GO:0001525
- Response to hypoxia — GO:0001666
- T cell activation — GO:0042110

---

## 5. Mechanism / Pathophysiology (metastasis and treatment response)

### 5.1 Metastatic niche and immune microenvironment (single-cell evidence; 2024)
A 2024 single-cell study of **bone metastatic RCC** profiled 6 primary and 9 bone metastatic tumors from 14 ccRCC patients, reporting extensive immune dysfunction in bone metastases and a macrophage/MDSC axis. (ma2024singlecellprofilingof pages 1-2)

Key quantitative/biological statements from the excerpt include:
- “More than one-third of metastatic RCC patients were accompanied by bone metastases.” (ma2024singlecellprofilingof pages 1-2)
- “The progression-free survival of BMRCC remains low of **4.7 months** versus **11.2 months** for those without bone metastases.” (ma2024singlecellprofilingof pages 1-2)
- Bone metastatic tumors show “multifaceted immune deficiency” with macrophages exhibiting “malignant and pro-angiogenic features,” dominance of “immune inhibitory T cells,” and MDSCs as macrophage progenitors. (ma2024singlecellprofilingof pages 1-2)

**Cell Ontology (CL) suggestions (key cell types):**
- CD8-positive, alpha-beta T cell — CL:0000625
- Regulatory T cell — CL:0000815
- Macrophage — CL:0000235
- Myeloid-derived suppressor cell — CL:0000867
- Cancer-associated fibroblast — (no single CL term universally used; often modeled as fibroblast CL:0000057 with “activated” state)

### 5.2 Treatment response/resistance conceptual model
mRCC outcomes reflect interplay between:
- Angiogenesis dependence (TKI sensitivity)
- Immune microenvironment state (ICI sensitivity)
- Organ-specific niches (e.g., bone metastasis immune suppression)
- Emerging targeting of HIF-2α as an upstream axis in clear-cell RCC biology. (powles2024nivolumabpluscabozantinib pages 1-2, yanagisawa2024updatedsystematicreview pages 4-4, ma2024singlecellprofilingof pages 1-2, fallah2024fdaapprovalsummary pages 1-3)

---

## 6. Anatomical Structures Affected

### 6.1 Common metastatic sites (frequency; 2024 multicenter cohort)
A large Korean multicenter database study (n=1,761) reported the most common metastatic sites at mRCC diagnosis: lung **70.9%**, lymph nodes **37.9%**, bone **30.7%**, liver **12.7%**, adrenal gland **9.8%**, brain **8.2%**. (lee2024sitesofmetastasis pages 1-2)

Median cancer-specific survival (CSS) varied by site, ranging from **13.9 months (liver)** to **29.1 months (lung)** among common sites (>5%); liver, bone, and pleural metastases were associated with the shortest median CSS (<19 months). (lee2024sitesofmetastasis pages 1-2)

**UBERON suggestions:**
- Kidney — UBERON:0002113
- Lung — UBERON:0002048
- Bone — UBERON:0002481
- Liver — UBERON:0002107
- Brain — UBERON:0000955
- Adrenal gland — UBERON:0002369

---

## 7. Inheritance and Population (Epidemiology and Prognosis)

### 7.1 Incidence / demographics (examples from retrieved evidence)
A 2024 German review reports ~**15,000** RCC diagnoses annually in Germany and notes that **20–30%** present with metastatic disease at diagnosis. (ivanyi2024thetreatmentof pages 1-2)

A real-world Saudi cohort paper provides global framing figures (not limited to mRCC): “nearly **431,000** new RCC cases in 2022 with ~**180,000** deaths,” and states ~**35%** of RCC patients present with unresectable/metastatic disease at diagnosis. (almansour2024realworldsurvivaloutcomes pages 1-2)

### 7.2 Prognosis and risk stratification
A 2024 review summarizes outcomes achievable with prognosis-based sequential systemic therapy: mean **PFS 12–24 months** and **OS ≈50 months** from first-line initiation. (ivanyi2024thetreatmentof pages 1-2)

IMDC risk group survivals reported in that review: **low-risk 43.2 months**, **intermediate 22.5 months**, **high-risk 7.8 months**. (ivanyi2024thetreatmentof pages 1-2)

---

## 8. Diagnostics

### 8.1 Standard diagnostic modalities (high-level)
The retrieved evidence emphasizes systemic-therapy management and does not provide a detailed diagnostic algorithm. In practice, mRCC diagnosis/staging relies on cross-sectional imaging (CT/MRI), histopathology, and risk stratification (IMDC). (ivanyi2024thetreatmentof pages 1-2)

### 8.2 Biomarkers and liquid biopsy (ctDNA) — recent evidence (2024)
In resected RCC (localized/high-risk), tumor-informed ctDNA is emerging as a prognostic marker for recurrence (relevant to identifying patients at risk of progression to metastatic disease).

A 2024 study using a personalized ctDNA assay (Signatera RUO) reported:
- Pre-operative ctDNA detection in **18/36 (50%)** patients. (correa2024associationofcirculating pages 1-2)
- ctDNA positivity associated with inferior relapse-free survival (pre-op HR **2.70**, P=0.046; post-op/any time HR **3.23**, P=0.003). (correa2024associationofcirculating pages 1-2)
- Relapse prediction performance among ctDNA-positive patients: **sensitivity 84%**, **PPV 90%**; post-surgical ctDNA positivity PPV **100%**; NPV **64%**; absence at both timepoints NPV **80%**. (correa2024associationofcirculating pages 1-2)

**Abstract quote (key point):** “Detection of plasma ctDNA using a personalized assay is prognostic of recurrence in patients with resected RCC.” (correa2024associationofcirculating pages 1-2)

---

## 9. Treatment (current applications and real-world implementations)

### 9.1 Current first-line systemic therapy landscape (2023–2024 high-quality sources)
Contemporary 1L mRCC therapy is dominated by ICI-based combinations (IO/TKI or IO/IO). A 2024 review states: “mRCC can be treated with a combination of two immune checkpoint inhibitors (CPIs), a CPI and a tyrosine-kinase inhibitor (TKI) (evidence level IA), or a TKI as monotherapy…” (ivanyi2024thetreatmentof pages 1-2)

A 2024 network meta-analysis excerpt provides comparative phase III outcomes across major 1L regimens versus sunitinib (PFS, OS, ORR, CR rates), reinforcing that multiple regimens improve outcomes with different tradeoffs (e.g., higher PFS/ORR with IO/TKI vs durability with IO/IO). (yanagisawa2024updatedsystematicreview pages 4-4)

### 9.2 Key pivotal trials and updates (artifact)
The following table summarizes major 2023–2024 trial evidence and regulatory developments.

| Trial (NCT) | Population/line | Regimens | Key efficacy outcomes | Key safety notes | Publication (journal, date, URL) | Evidence |
|---|---|---|---|---|---|---|
| CheckMate 9ER (NCT03141177) | Treatment-naïve advanced/metastatic clear-cell RCC; 1L; n=323 nivolumab+cabozantinib vs n=328 sunitinib | Nivolumab 240 mg IV q2w + cabozantinib 40 mg daily vs sunitinib 50 mg (4 weeks on, 6-week cycles) | Median PFS 16.6 vs 8.4 mo; HR 0.59 (95% CI 0.49–0.71). Median OS 49.5 vs 35.5 mo; HR 0.70 (95% CI 0.56–0.87). ORR 56% vs 28%; CR 13% vs 5%; median duration of response 22.1 vs 16.1 mo. | Treatment-related AEs any-grade/grade 3: 97%/67% vs 93%/55% with sunitinib. | *ESMO Open*, May 2024. https://doi.org/10.1016/j.esmoop.2024.102994 | (powles2024nivolumabpluscabozantinib pages 1-2) |
| CLEAR final OS analysis (NCT02811861) | Treatment-naïve advanced RCC; 1L; lenvatinib+pembrolizumab vs sunitinib | Lenvatinib 20 mg daily + pembrolizumab 200 mg IV q3w vs sunitinib | OS HR 0.79 (95% CI 0.63–0.99); median OS 53.7 vs 54.3 mo; 36-mo OS 66.4% vs 60.2%. Median PFS 23.9 vs 9.2 mo; HR 0.47 (95% CI 0.38–0.57). ORR 71.3% vs 36.7%. | Treatment-emergent AEs occurred in >90% of patients in both groups. | *Journal of Clinical Oncology*, Apr 2024. https://doi.org/10.1200/jco.23.01569 | (yanagisawa2024updatedsystematicreview pages 4-4) |
| COSMIC-313 (NCT03937219) | Previously untreated advanced clear-cell RCC with IMDC intermediate/poor risk; triplet intensification of IO/IO backbone; overall n=855 randomized | Cabozantinib 40 mg daily + nivolumab/ipilimumab vs placebo + nivolumab/ipilimumab | In first 550 randomized patients: 12-mo PFS probability 0.57 vs 0.49; HR for progression/death 0.73 (95% CI 0.57–0.94; P=0.01). ORR 43% vs 36%. OS follow-up ongoing. | Grade 3–4 AEs 79% vs 56%. | *New England Journal of Medicine*, May 2023. https://doi.org/10.1056/NEJMoa2212851 | (choueiri2023cabozantinibplusnivolumab pages 1-3) |
| LITESPARK-005 (NCT04195750) | Advanced RCC after prior PD-1/PD-L1 inhibitor and VEGF-TKI; randomized 1:1; n=746 | Belzutifan 120 mg daily vs everolimus 10 mg daily | PFS HR 0.75 (95% CI 0.63–0.90; 1-sided p=0.0008). Median PFS 5.6 vs 5.6 mo. OS HR 0.88 (95% CI 0.73–1.07), immature. Confirmed ORR 22% vs 3.6%. Led to FDA approval in Dec 2023 for post–PD-(L)1 and VEGF-TKI advanced RCC. | Toxicities differed by arm; discontinuations and interruptions due to treatment-emergent AEs were lower with belzutifan; PRO analyses suggested favorable tolerability. | *Clinical Cancer Research* (FDA Approval Summary), Sep 2024. https://doi.org/10.1158/1078-0432.CCR-24-1199 | (fallah2024fdaapprovalsummary pages 1-3) |
| CBM588 microbiome phase 1 (NCT05122546) | Treatment-naïve locally advanced or metastatic RCC; randomized phase 1; 30 participants; cabo+nivo ± live bacterial supplementation | Cabozantinib + nivolumab with or without CBM588 | Primary microbiome endpoint not met. ORR 74% (14/19) with CBM588 vs 20% (2/10) control; P=0.01. PFS at 6 mo 84% (16/19) vs 60% (6/10). | No significant difference in toxicity profile between study arms. | *Nature Medicine*, Jun 2024. https://doi.org/10.1038/s41591-024-03086-4 | (ma2024singlecellprofilingof pages 1-2) |


*Table: This table summarizes key 2023-2024 systemic therapy evidence in metastatic or advanced renal cell carcinoma, including pivotal first-line and later-line studies. It highlights efficacy, safety, and publication details for quick comparison across major regimens.*

### 9.3 Later-line therapy: HIF-2α inhibition (belzutifan)
FDA granted traditional approval (Dec 14, 2023) for **belzutifan** in advanced RCC after prior PD-(L)1 inhibitor and VEGF-TKI, based on LITESPARK-005 demonstrating PFS benefit vs everolimus (HR **0.75**, 95% CI 0.63–0.90) and ORR **22%** vs **3.6%**. (fallah2024fdaapprovalsummary pages 1-3)

### 9.4 Real-world implementation examples
A 2024 retrospective real-world cohort of metastatic clear-cell RCC (n=84) reported median first-line PFS **9.7 months** and median OS **42.0 months**, with ORR **41%** for ICI-based combinations (in that cohort) and identified liver metastasis and lower performance status as adverse prognostic factors. (almansour2024realworldsurvivaloutcomes pages 1-2)

### 9.5 Local therapies in metastatic disease
A 2024 algorithm-focused review emphasizes multidisciplinary selection of cytoreductive nephrectomy and metastasectomy; it reports trial/observational signals that delayed nephrectomy strategies and complete metastasectomy can improve OS in selected patients (e.g., SURTIME mOS 32.5 vs 15 months; complete metastasectomy mOS 40.7 vs 14.8 months in the cited context). (bloise2024firstlinetreatmentsand pages 2-4)

### 9.6 MAXO suggestions (treatment actions)
- Immune checkpoint inhibitor therapy — **MAXO:0000647** (suggested)
- Tyrosine kinase inhibitor therapy — **MAXO:0000704** (suggested)
- Nephrectomy — **MAXO:0000897** (suggested)
- Metastasectomy — **MAXO:0000934** (suggested)
- Radiation therapy — **MAXO:0000014** (suggested)

---

## 10. Prevention

### 10.1 Primary prevention (risk reduction)
Recent epidemiologic evidence supports risk reduction focusing on metabolic health, diet patterns, and environmental exposures:
- Metabolic syndrome and combinations of metabolic abnormalities are associated with increased kidney cancer risk (e.g., MetS HR **1.70**, BP+HDL+WC HR **3.03**). (wang2024associationbetweenmetabolic pages 1-2, wang2024associationbetweenmetabolic pages 5-6)
- Higher ultra-processed food intake is associated with higher RCC incidence and mortality (HR **1.42** and **1.64** for highest vs lowest quartile). (li2024ultraprocessedfoodconsumption pages 1-2)
- Air pollution exposures PM10 and NO2 show positive associations with kidney cancer incidence in meta-analysis (PM10 HR **1.29**; NO2 HR **1.10** per 10 µg/m³). (dahman2024airpollutionand pages 1-3)

### 10.2 Secondary prevention / surveillance
No surveillance guideline text for hereditary RCC syndromes was retrieved in the current evidence set.

---

## 11. Other Species / Natural Disease
Not addressed in the retrieved evidence set.

---

## 12. Model Organisms
Not addressed in the retrieved evidence set (no murine/xenograft/organoid model papers were retrieved).

---

## 13. Key Statistics (quick reference)
- **Metastatic at diagnosis:** 20–30% (Germany review) (ivanyi2024thetreatmentof pages 1-2)
- **Common metastatic sites and frequencies:** lung 70.9%, LN 37.9%, bone 30.7%, liver 12.7%, adrenal 9.8%, brain 8.2% (Korean cohort, n=1,761) (lee2024sitesofmetastasis pages 1-2)
- **IMDC median survivals:** favorable 43.2 mo; intermediate 22.5 mo; poor 7.8 mo (review) (ivanyi2024thetreatmentof pages 1-2)
- **CheckMate 9ER (44 mo follow-up):** median OS 49.5 vs 35.5 mo; median PFS 16.6 vs 8.4 mo (nivolumab+cabozantinib vs sunitinib) (powles2024nivolumabpluscabozantinib pages 1-2)
- **CLEAR final OS analysis:** OS HR 0.79; median PFS 23.9 vs 9.2 mo; ORR 71.3% vs 36.7% (lenvatinib+pembrolizumab vs sunitinib) (yanagisawa2024updatedsystematicreview pages 4-4)
- **Belzutifan (LITESPARK-005):** PFS HR 0.75; ORR 22% vs 3.6% vs everolimus (fallah2024fdaapprovalsummary pages 1-3)

---

## Limitations of the retrieved evidence set (transparency)
- Explicit ontology identifiers (ICD-10/ICD-11, MeSH, Orphanet, dedicated MONDO for *metastatic RCC*) were not present in retrieved texts and thus could not be verified here. (OpenTargets Search: renal cell carcinoma)
- Detailed phenotype frequencies (symptoms/labs) and hereditary-syndrome surveillance guidance were not captured in the available evidence snippets.
- Model organism and comparative oncology coverage was not available from retrieved sources.



References

1. (OpenTargets Search: renal cell carcinoma): Open Targets Query (renal cell carcinoma, 48 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

2. (ivanyi2024thetreatmentof pages 1-2): Philipp Ivanyi, Tabea Fröhlich, Viktor Grünwald, Stefanie Zschäbitz, Jens Bedke, and Christian Doehn. The treatment of metastatic renal cell carcinoma. Deutsches Arzteblatt international, Aug 2024. URL: https://doi.org/10.3238/arztebl.m2024.0147, doi:10.3238/arztebl.m2024.0147. This article has 19 citations and is from a peer-reviewed journal.

3. (bloise2024firstlinetreatmentsand pages 2-4): Francesco Bloise, Fiorella Manfredi, Luca Zatteri, Giovanni Dima, Chiara Carli, Rosanna Di Vita, Maria Olivieri, Enrico Sammarco, Marco Ferrari, Alessia Salfi, Adele Bonato, Debora Serafin, Natalia Coccia, Laura Doni, Luca Galli, Michele Sisani, Giandomenico Roviello, Martina Catalano, and Federico Paolieri. First-line treatments and management of metastatic renal cell carcinoma patients: an italian interdisciplinary uro-oncologic group algorithm. Cells, 13:961, Jun 2024. URL: https://doi.org/10.3390/cells13110961, doi:10.3390/cells13110961. This article has 3 citations.

4. (powles2024nivolumabpluscabozantinib pages 1-2): T. Powles, M. Burotto, B. Escudier, A. Apolo, M. Bourlon, A. Shah, C. Suárez, C. Porta, C. Barrios, M. Richardet, H. Gurney, E. R. Kessler, Y. Tomita, J. Bedke, S. George, C. Scheffold, P. Wang, V. Fedorov, R. Motzer, T. Choueiri, and Prof. Thomas Powles. Nivolumab plus cabozantinib versus sunitinib for first-line treatment of advanced renal cell carcinoma: extended follow-up from the phase iii randomised checkmate 9er trial. ESMO Open, 9:102994, May 2024. URL: https://doi.org/10.1016/j.esmoop.2024.102994, doi:10.1016/j.esmoop.2024.102994. This article has 105 citations and is from a domain leading peer-reviewed journal.

5. (yanagisawa2024updatedsystematicreview pages 4-4): Takafumi Yanagisawa, Keiichiro Mori, Akihiro Matsukawa, Tatsushi Kawada, Satoshi Katayama, Kensuke Bekku, Ekaterina Laukhtina, Pawel Rajwa, Fahad Quhal, Benjamin Pradere, Wataru Fukuokaya, Kosuke Iwatani, Masaya Murakami, Karim Bensalah, Viktor Grünwald, Manuela Schmidinger, Shahrokh F. Shariat, and Takahiro Kimura. Updated systematic review and network meta-analysis of first-line treatments for metastatic renal cell carcinoma with extended follow-up data. Cancer Immunology, Immunotherapy : CII, Jan 2024. URL: https://doi.org/10.1007/s00262-023-03621-1, doi:10.1007/s00262-023-03621-1. This article has 38 citations.

6. (meng2023emergingimmunotherapyapproaches pages 5-6): Lingbin Meng, Katharine A. Collier, Peng Wang, Zihai Li, Paul Monk, Amir Mortazavi, Zhiwei Hu, Daniel Spakowicz, Linghua Zheng, and Yuanquan Yang. Emerging immunotherapy approaches for advanced clear cell renal cell carcinoma. Cells, 13:34, Dec 2023. URL: https://doi.org/10.3390/cells13010034, doi:10.3390/cells13010034. This article has 72 citations.

7. (choueiri2023cabozantinibplusnivolumab pages 1-3): Toni K. Choueiri, Thomas Powles, Laurence Albiges, Mauricio Burotto, Cezary Szczylik, Bogdan Zurawski, Eduardo Yanez Ruiz, Marco Maruzzo, Alberto Suarez Zaizar, Luis E. Fein, Fabio A. Schutz, Daniel Y.C. Heng, Fong Wang, Fabio Mataveli, Yu-Lin Chang, Maximiliano van Kooten Losio, Cristina Suarez, and Robert J. Motzer. Cabozantinib plus nivolumab and ipilimumab in renal-cell carcinoma. The New England journal of medicine, 388 19:1767-1778, May 2023. URL: https://doi.org/10.1056/nejmoa2212851, doi:10.1056/nejmoa2212851. This article has 188 citations and is from a highest quality peer-reviewed journal.

8. (fallah2024fdaapprovalsummary pages 1-3): Jaleh Fallah, Brian L. Heiss, Hee-Koung Joeng, Chana Weinstock, Xin Gao, William F. Pierce, Benjamin Chukwurah, Vishal Bhatnagar, Mallorie H. Fiero, Laleh Amiri-Kordestani, Richard Pazdur, Paul G. Kluetz, and Daniel L. Suzman. Fda approval summary: belzutifan for patients with advanced renal cell carcinoma. Clinical cancer research : an official journal of the American Association for Cancer Research, 30:5003-5008, Sep 2024. URL: https://doi.org/10.1158/1078-0432.ccr-24-1199, doi:10.1158/1078-0432.ccr-24-1199. This article has 23 citations.

9. (lee2024sitesofmetastasis pages 1-2): Chan Ho Lee, Minyong Kang, Cheol Kwak, Young Hwii Ko, Jung Kwon Kim, Jae Young Park, Seokhwan Bang, Seong Il Seo, Jungyo Suh, Wan Song, Cheryn Song, Hyung Ho Lee, Jinsoo Chung, Chang Wook Jeong, Jung Ki Jo, Seock Hwan Choi, Joongwon Choi, Changil Choi, Seol Ho Choo, Jang Hee Han, Sung-Hoo Hong, and Eu Chang Hwang. Sites of metastasis and survival in metastatic renal cell carcinoma: results from the korean renal cancer study group database. Journal of Korean Medical Science, Sep 2024. URL: https://doi.org/10.3346/jkms.2024.39.e293, doi:10.3346/jkms.2024.39.e293. This article has 19 citations and is from a peer-reviewed journal.

10. (almansour2024realworldsurvivaloutcomes pages 1-2): Mubarak M. Al-Mansour, Syed Sameer Aga, Hanin A. Alharbi, Maria N. Alsulami, Halah A. Fallatah, Tarfah B. Albedaiwi, Lujain K. Anbari, Taleen R. Surrati, Ashwag A. Algethami, Alaa Althubaiti, Turki M. Alfayea, and Ashwaq Alolayan. Real-world survival outcomes of first-line therapies in patients with metastatic clear cell renal cell carcinoma: a retrospective analysis from two centres in saudi arabia. Cancers, 16:3234, Sep 2024. URL: https://doi.org/10.3390/cancers16183234, doi:10.3390/cancers16183234. This article has 2 citations.

11. (ma2024singlecellprofilingof pages 1-2): Fen Ma, Shuoer Wang, Lun Xu, Wending Huang, Guohai Shi, Zhengwang Sun, Weiluo Cai, Zhiqiang Wu, Yiming Huang, Juan Meng, Yining Sun, Meng Fang, Mo Cheng, Yingzheng Ji, Tu Hu, Yunkui Zhang, Bingxin Gu, Jiwei Zhang, Shaoli Song, Yidi Sun, and Wangjun Yan. Single-cell profiling of the microenvironment in human bone metastatic renal cell carcinoma. Communications Biology, Jan 2024. URL: https://doi.org/10.1038/s42003-024-05772-y, doi:10.1038/s42003-024-05772-y. This article has 12 citations and is from a peer-reviewed journal.

12. (wang2024associationbetweenmetabolic pages 1-2): Lin Wang, Han Du, Chao Sheng, Hongji Dai, and Kexin Chen. Association between metabolic syndrome and kidney cancer risk: a prospective cohort study. Lipids in Health and Disease, May 2024. URL: https://doi.org/10.1186/s12944-024-02138-5, doi:10.1186/s12944-024-02138-5. This article has 12 citations and is from a peer-reviewed journal.

13. (wang2024associationbetweenmetabolic pages 5-6): Lin Wang, Han Du, Chao Sheng, Hongji Dai, and Kexin Chen. Association between metabolic syndrome and kidney cancer risk: a prospective cohort study. Lipids in Health and Disease, May 2024. URL: https://doi.org/10.1186/s12944-024-02138-5, doi:10.1186/s12944-024-02138-5. This article has 12 citations and is from a peer-reviewed journal.

14. (li2024ultraprocessedfoodconsumption pages 1-2): Ya-Dong Li, Yong-Xin Fu, Le-Lan Gong, Ting Xie, Wei Tan, Hao Huang, Sheng-Jie Zeng, Chuan Liu, and Zheng-Ju Ren. Ultra-processed food consumption and renal cell carcinoma incidence and mortality: results from a large prospective cohort. BMC Medicine, Oct 2024. URL: https://doi.org/10.1186/s12916-024-03677-5, doi:10.1186/s12916-024-03677-5. This article has 9 citations and is from a domain leading peer-reviewed journal.

15. (dahman2024airpollutionand pages 1-3): Lina Dahman, Victoria Gauthier, Aurore Camier, Jean Joel Bigna, François Glowacki, Philippe Amouyel, Luc Dauchet, and Aghiles Hamroun. Air pollution and kidney cancer risk: a systematic review and meta-analysis. Journal of Nephrology, 37:1779-1790, Jun 2024. URL: https://doi.org/10.1007/s40620-024-01984-x, doi:10.1007/s40620-024-01984-x. This article has 16 citations and is from a peer-reviewed journal.

16. (correa2024associationofcirculating pages 1-2): Andres F Correa, Ekaterina Kalashnikova, Hsin-Ta Wu, Ryan M Winters, Mustafa Balcioglu, Sumedha Sudhaman, Denise C Connolly, Yulan Gong, Robert G Uzzo, Himanshu Sethi, Adam C ElNaggar, Alexey Aleshin, Minetta C Liu, and Philip H Abbosh. Association of circulating tumor dna with patient prognosis in surgically resected renal cell carcinoma. The Oncologist, 29:887-893, Jul 2024. URL: https://doi.org/10.1093/oncolo/oyae180, doi:10.1093/oncolo/oyae180. This article has 26 citations.
