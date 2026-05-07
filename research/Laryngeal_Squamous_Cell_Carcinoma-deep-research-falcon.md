---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-07T11:59:08.191230'
end_time: '2026-05-07T12:24:32.473383'
duration_seconds: 1524.29
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Laryngeal Squamous Cell Carcinoma
  mondo_id: ''
  category: ''
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 41
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Laryngeal Squamous Cell Carcinoma
- **MONDO ID:**  (if available)
- **Category:** 

## Research Objectives

Please provide a comprehensive research report on **Laryngeal Squamous Cell Carcinoma** covering all of the
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
- **Disease Name:** Laryngeal Squamous Cell Carcinoma
- **MONDO ID:**  (if available)
- **Category:** 

## Research Objectives

Please provide a comprehensive research report on **Laryngeal Squamous Cell Carcinoma** covering all of the
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


## Comprehensive Research Report: Laryngeal Squamous Cell Carcinoma (LSCC)

### Target disease
- **Disease name:** Laryngeal squamous cell carcinoma (LSCC)
- **Category:** Head and neck squamous cell carcinoma (HNSCC) subsite/histology (larynx)
- **Ontology identifiers (retrieved in this evidence set):**
  - **EFO:** EFO_0006352 “laryngeal squamous cell carcinoma” (OpenTargets) (OpenTargets Search: laryngeal squamous cell carcinoma)
  - **MONDO parent concept:** MONDO_0002358 “laryngeal carcinoma” (OpenTargets) (OpenTargets Search: laryngeal squamous cell carcinoma)
- **ICD-10 subsite examples (used in clinical literature):** glottic cancer **C32.0**; supraglottic cancer **C32.1**; other laryngeal codes (e.g., C32.8/C32.9) used for supraglottic/non-glottic groupings in one 2007–2020 early-stage cohort (publication date 2024-09; URL https://doi.org/10.3390/biomedicines12092136) (wald2024outcomedisparitiesin pages 11-12)
- **MeSH / ICD-11 / Orphanet / OMIM:** not retrieved in the tool-accessible corpus used for this report; therefore not asserted here.

---

## 1. Disease information (overview, definitions, synonyms)

**Definition and classification.** LSCC is the predominant malignant epithelial neoplasm of the larynx; multiple sources emphasize that most laryngeal cancers are squamous cell carcinomas (>90%). A 2024 review states: “over 90% are squamous cell carcinomas” (publication date 2024-10; URL https://doi.org/10.3390/jpm14101048) (maniaci2024personalizedtreatmentstrategies pages 1-2). Laryngeal tumors are clinically stratified by **anatomic subsite**—**supraglottic, glottic, subglottic**—because subsite affects lymphatic drainage, symptom onset, patterns of nodal metastasis, and outcomes (macneil2021survivaltrendsof pages 20-25, macneil2021survivaltrendsof pages 25-30).

**Common synonyms/alternative names.**
- Laryngeal cancer (when SCC histology is implied) (mousavi2024laryngealcancerincidence pages 1-2, mousavi2024laryngealcancerincidence pages 2-4)
- Squamous cell carcinoma of the larynx
- Laryngeal carcinoma, SCC histology

**Evidence source type.** This report integrates:
- Population-level registry analyses (SEER) (mousavi2024laryngealcancerincidence pages 2-4, mousavi2024laryngealcancerincidence pages 4-6)
- Prospective human cohort biomarker data (PD-L1 in LSCC) (verro2024cancerandimmune pages 1-2)
- Single-cell transcriptomics (human tumor tissues) (sun2024singlecelltranscriptomicanalyses pages 1-2, li2024characterizationofcancer pages 1-2)
- Clinical trial registry records (ClinicalTrials.gov) (NCT06137378 chunk 1, NCT04943445 chunk 1)
- Narrative/review syntheses (maniaci2024personalizedtreatmentstrategies pages 1-2, fuereder2025systemictherapyfor pages 2-4)

---

## 2. Etiology

### 2.1 Disease causal factors and major risk factors
**Tobacco and alcohol.** A 2024 review summarizes that tobacco and alcohol are major etiologic drivers, stating they “together account for around 75% of cases” (2024-10; https://doi.org/10.3390/jpm14101048) (maniaci2024personalizedtreatmentstrategies pages 1-2). A population-based cohort excerpt similarly states tobacco and alcohol account for the majority (≈85%) and notes current smoking is associated with very large risk increases (10–20×) (macneil2021survivaltrendsof pages 25-30).

**HPV infection.** HPV is cited as a contributor/risk factor in laryngeal cancer/LSCC, but with lower prevalence than in HPV-driven oropharyngeal cancer; the cohort excerpt notes HPV in a minority (≈20–30%) with uncertain clinical relevance (macneil2021survivaltrendsof pages 25-30), and a 2024 review lists HPV infection as an additional risk factor (maniaci2024personalizedtreatmentstrategies pages 1-2).

**Occupational/dietary exposures.** Reviews highlight additional contributions from occupational exposures and dietary factors, but with less detailed quantification in the retrieved sources (maniaci2024personalizedtreatmentstrategies pages 1-2, macneil2021survivaltrendsof pages 25-30).

### 2.2 Protective factors
No specific protective genetic variants or protective environmental factors (with quantitative effect estimates) were retrieved in this evidence set; therefore not asserted.

### 2.3 Gene–environment and inflammation–tumor interactions (examples)
**Smoking and immune biomarker expression.** In a prospective LSCC cohort (n=58), PD-L1 CPS correlated significantly with **smoking habits** and **N stage**, and elevated CRP correlated with CPS, suggesting links among tobacco exposure, systemic inflammation, and immune checkpoint biomarker expression (2024-07; https://doi.org/10.1007/s00405-024-08822-7) (verro2024cancerandimmune pages 1-2).

**Tobacco mutational processes and TMB.** A 2024 review highlights a tobacco-related mutational signature and discusses tumor mutational burden (TMB) as potentially influencing immunotherapy response, providing a mechanistic link between carcinogen exposure and therapeutic sensitivity (maniaci2024personalizedtreatmentstrategies pages 3-5, maniaci2024personalizedtreatmentstrategies pages 9-11).

---

## 3. Phenotypes (clinical presentation) and HPO suggestions

### 3.1 Common symptoms and signs
A population-based cohort excerpt provides a clinically typical spectrum of presenting and progressive symptoms:
- **Early/common:** hoarseness/voice changes, throat discomfort, foreign-body sensation (macneil2021survivaltrendsof pages 25-30)
- **Progressive/advanced:** dyspnea, dysphagia, odynophagia, hemoptysis, referred ear pain, weight loss, stridor (macneil2021survivaltrendsof pages 25-30)

**Subsite-specific presentation (clinical heuristic).**
- **Glottic** tumors often present earlier with hoarseness (macneil2021survivaltrendsof pages 25-30)
- **Supraglottic** tumors may present with pressure symptoms and neck mass (macneil2021survivaltrendsof pages 25-30)
- **Subglottic** tumors often present later with stridor/dyspnea and are more frequently advanced at diagnosis (macneil2021survivaltrendsof pages 25-30)

### 3.2 Tumor characteristics observed in recent patient cohorts
- Prospective LSCC cohort (n=58): mean age **63.55±10.09**, **31.03% female**, most common subsite **glottic 46.55%**, and **75.86% moderately differentiated** (2024-07; https://doi.org/10.1007/s00405-024-08822-7) (verro2024cancerandimmune pages 1-2).

### 3.3 Quality-of-life impact
The larynx is central to voice, swallowing, and airway protection; the cohort excerpt notes QoL/voice outcomes are an important topic (citing studies of voice/QoL after early glottic treatment), but this evidence set did not retrieve quantitative QoL instrument results (macneil2021survivaltrendsof pages 113-115, macneil2021survivaltrendsof pages 20-25).

### 3.4 Suggested HPO terms (examples; not exhaustive)
(Phenotype frequencies not available in the retrieved sources.)
- Hoarseness: **HP:0001609**
- Dysphagia: **HP:0002015**
- Odynophagia: **HP:0033050**
- Dyspnea: **HP:0002094**
- Stridor: **HP:0001738**
- Hemoptysis: **HP:0002105**
- Otalgia (ear pain): **HP:0030766**
- Weight loss: **HP:0001824**

---

## 4. Genetic / molecular information

### 4.1 Somatic driver landscape and pathways (current understanding)
A 2024 molecular profiling review emphasizes recurrent alterations:
- **TP53**: “mutations in as many as **70%** of instances” (2024-10; https://doi.org/10.3390/jpm14101048) (maniaci2024personalizedtreatmentstrategies pages 3-5)
- Recurrent alterations also involve **CDKN2A**, **PIK3CA**, **NOTCH1**, and other genes (e.g., FAT1, LRP1B) (maniaci2024personalizedtreatmentstrategies pages 3-5, maniaci2024personalizedtreatmentstrategies pages 1-2)

**PI3K/AKT/mTOR signaling.** Altered **PIK3CA** is highlighted as driving hyperactivation of **PI3K/AKT/mTOR** signaling (maniaci2024personalizedtreatmentstrategies pages 3-5, maniaci2024personalizedtreatmentstrategies pages 1-2).

**Copy-number alterations.** CNV patterns highlighted include:
- **Loss** at **CDKN2A (9p21)**
- **Gains/amplifications** at **CCND1 (11q13)**, **EGFR (7p11)**, **MYC (8q24)**
- 11q13 amplification (CCND1/FADD region) associated with adverse features (poor prognosis, nodal metastasis) in the review synthesis (maniaci2024personalizedtreatmentstrategies pages 3-5).

**Epigenetics.** MGMT promoter methylation is noted as a relevant epigenetic alteration considered in molecular profiling discussions (maniaci2024personalizedtreatmentstrategies pages 1-2).

### 4.2 Immune-related biomarkers and MSI/TMB
The 2024 review discusses integrating **TILs, PD-L1, TMB, MSI** for immunotherapy prediction and notes: “Just **3%** of HNSCC patients, including laryngeal malignancies, had MSI-H status” (maniaci2024personalizedtreatmentstrategies pages 9-11).

### 4.3 OpenTargets disease–target associations (aggregated)
OpenTargets lists disease–target associations for LSCC and related parent concepts, including **XRCC1, CDKN2A, FAT1, TP53** (as a broader laryngeal carcinoma association), and others (OpenTargets Search: laryngeal squamous cell carcinoma). These reflect aggregated evidence links rather than effect sizes or actionable clinical biomarkers.

---

## 5. Mechanism / pathophysiology

### 5.1 Tumor ecosystem and immunosuppressive TME (single-cell evidence; 2024)
A 2024 scRNA-seq atlas of LSCC profiled “**89,406 single cells**” and identified major cell types: “epithelial-derived cells (EpCs), myeloid cells, T cells, B cells, NK cells, endothelial cells, and cancer-associated fibroblasts (CAFs)” (2024-01; https://doi.org/10.1038/s42003-024-05765-x) (sun2024singlecelltranscriptomicanalyses pages 1-2). The abstract explicitly states: “**Inﬁl-tration of a large number of regulatory T cells, dysplastic plasma cells, and macrophages that are at the early development stage in the cancerous tissue indicates an immunosuppressive state**.” It also notes: “**Abundant neutrophils detected at the cancer margins reflect the inflammatory microenvironment**.” (sun2024singlecelltranscriptomicanalyses pages 1-2).

The same study reports cell–cell signaling complexity: “strong interactions existed between the tumor cells and B cells, CD4+ T cells, CD8+ T cells or Tregs through the lymphotoxin and lymphotoxin beta receptor (LTB-LTBR)” and implicates immune regulation/suppression (sun2024singlecelltranscriptomicanalyses pages 10-12).

### 5.2 Stromal autophagy as a nutrient-support mechanism
The scRNA-seq study notes “enhanced autophagy in endothelial cells and fibroblasts implies a role in nutrient supply” (sun2024singlecelltranscriptomicanalyses pages 1-2) and reports that GSEA “uncovered enhanced autophagy” in comparisons relevant to tumor/margin regions (sun2024singlecelltranscriptomicanalyses pages 10-12). This supports a causal chain: tumor-associated stress → stromal autophagy programs → nutrient support → invasion/metastasis (hypothesis consistent with their interpretation).

### 5.3 Cancer stem cell (CSC) programs (single-cell evidence; 2024)
A 2024 scRNA-seq study focusing on CSCs in LSCC identified CSC-like stem clusters with high expression of markers and oncogenic programs:
- CSC cluster showed upregulation including “PROM1… SOX4” and displayed “heightened activity of **Wnt/β-catenin signaling, Notch signaling, hypoxia**” (2024-08; https://doi.org/10.1093/gpbjnl/qzae056) (li2024characterizationofcancer pages 3-4).
- CSC-specific gene sets included PROM1 and additional markers (e.g., FOLR1, DMBT1), with immunofluorescence co-localization and prognostic modeling; candidate drugs predicted to repress CSC gene programs included “erlotinib, OSI-027, and ibrutinib (PCI-32765)” (li2024characterizationofcancer pages 6-8, li2024characterizationofcancer pages 9-10).

### 5.4 Suggested ontology terms for mechanisms
**GO biological process (examples):**
- Immune response / regulation: GO:0006955, GO:0050776
- T cell activation/exhaustion-related processes: GO:0042110 (T cell activation)
- Autophagy: GO:0006914
- Epithelial–mesenchymal transition: GO:0001837
- Wnt signaling: GO:0016055
- Notch signaling: GO:0007219
- Response to hypoxia: GO:0001666

**Cell Ontology (CL) cell types implicated (examples):**
- Regulatory T cell: **CL:0000815**
- Macrophage: **CL:0000235**
- Neutrophil: **CL:0000775**
- Plasma cell: **CL:0000786**
- Cancer-associated fibroblast (CAF): represented under fibroblast lineage; CAF state not always a distinct CL class in all releases
- Endothelial cell: **CL:0000115**

---

## 6. Environmental information

**Lifestyle exposures:** tobacco and alcohol are dominant risk factors (maniaci2024personalizedtreatmentstrategies pages 1-2, macneil2021survivaltrendsof pages 25-30). 
**Occupational exposures:** mentioned as contributors in reviews/cohort excerpts, but without detailed effect estimates in retrieved sources (maniaci2024personalizedtreatmentstrategies pages 1-2, macneil2021survivaltrendsof pages 25-30).
**Infectious:** HPV is cited as an additional etiologic factor in a subset (maniaci2024personalizedtreatmentstrategies pages 1-2, macneil2021survivaltrendsof pages 25-30).

---

## 7. Anatomical structures affected (UBERON suggestions)

### 7.1 Organ/subsite
- Larynx (**UBERON:0001737**)
- Supraglottis / glottis / subglottis (subsite framework; anatomic distinctions described in detail) (macneil2021survivaltrendsof pages 20-25)

### 7.2 Regional spread and spaces
- Cervical lymph nodes / central compartment nodes: subsite-specific lymphatic drainage noted (supraglottis → bilateral lateral neck; subglottis → central compartment nodes; glottis relatively sparse lymphatics) (macneil2021survivaltrendsof pages 20-25).
- Preepiglottic and paraglottic spaces facilitate spread (macneil2021survivaltrendsof pages 20-25).

---

## 8. Temporal development (onset and progression)

**Typical onset.** Population-based data show predominant incidence in older adults; in SEER 2000–2019, the largest age-group share was 55–69 years and incidence rises with age (mousavi2024laryngealcancerincidence pages 1-2, mousavi2024laryngealcancerincidence pages 4-6).

**Progression.** Symptoms and subsite anatomy support typical progression patterns: glottic tumors often detected earlier due to early voice symptoms; subglottic more often advanced at presentation (macneil2021survivaltrendsof pages 25-30, macneil2021survivaltrendsof pages 20-25).

**Staging.** Detailed AJCC TNM definitions were not retrieved in this evidence set, but stage III/IV presentation frequency is noted in the cohort excerpt (≈40% present stage III/IV) (macneil2021survivaltrendsof pages 25-30).

---

## 9. Inheritance and population

### 9.1 Epidemiology (recent statistics; prioritize 2024)
A 2024 SEER-22 analysis (Mousavi et al., publication date 2024-07; https://doi.org/10.1186/s13690-024-01333-1) identified **104,991** laryngeal cancer cases (2000–2019), with SCC comprising **94.53%** (mousavi2024laryngealcancerincidence pages 1-2, mousavi2024laryngealcancerincidence pages 2-4). Key incidence statistics (delay-adjusted):
- **ASIR per 100,000:** men **5.98** (95% CI 5.94–6.02), women **1.25** (1.23–1.27) (mousavi2024laryngealcancerincidence pages 2-4, mousavi2024laryngealcancerincidence pages 4-6)
- **Trend:** overall incidence declined, overall **AAPC −2.50%**; men **AAPC −2.70%**, women **AAPC −2.26%** (mousavi2024laryngealcancerincidence pages 2-4, mousavi2024laryngealcancerincidence pages 4-6)
- **Race/ethnicity disparity:** **Non-Hispanic Black men** had the highest ASIR (**9.13**) and the largest decline (**AAPC −3.26%**) (mousavi2024laryngealcancerincidence pages 1-2, mousavi2024laryngealcancerincidence pages 4-6)

(See SEER Table 1 image excerpts for the stratified rates and AAPCs.) (mousavi2024laryngealcancerincidence media a846858a, mousavi2024laryngealcancerincidence media 9610280e)

### 9.2 Demographics
SEER patterns show strong male predominance and concentration among non-Hispanic White individuals and older ages (mousavi2024laryngealcancerincidence pages 1-2, mousavi2024laryngealcancerincidence pages 4-6). Prospective cohort demographics similarly indicate older adult predominance (mean age ~63.6) (verro2024cancerandimmune pages 1-2).

### 9.3 Inheritance
LSCC is not typically a Mendelian inherited disease entity; in this evidence set, no germline causal variants, inheritance patterns, or penetrance data specific to LSCC were retrieved.

---

## 10. Diagnostics

### 10.1 Standard clinical and pathology workflow
A population-based cohort excerpt describes a typical diagnostic workup:
- History and complete head/neck examination
- Outpatient **fiberoptic laryngoscopy** and videolaryngoscopy with stroboscopy for vocal fold function
- Examination under anesthesia with **direct laryngoscopy and biopsy** for histologic confirmation
- Imaging: contrast **CT** or **MRI** to assess cartilage invasion, submucosal disease, nodal disease, and extralaryngeal spread (macneil2021survivaltrendsof pages 25-30).

### 10.2 Biomarkers and testing approaches (current practice + emerging)
**PD-L1 (CPS) IHC workflow.** A prospective LSCC study used PD-L1 IHC 22C3 pharmDx, requiring at least 100 viable tumor cells for assessment, and reported that CPS correlated with smoking and N stage (2024-07; https://doi.org/10.1007/s00405-024-08822-7) (verro2024cancerandimmune pages 1-2).

**Emerging biomarker approaches.** A 2024 review discusses immune biomarkers (PD-L1, TMB, MSI) and other molecular markers, including MGMT methylation and CSC-associated markers (CD44/ALDH1A1), while emphasizing the need for standardized testing and interpretation (maniaci2024personalizedtreatmentstrategies pages 1-2, maniaci2024personalizedtreatmentstrategies pages 9-11).

**Single-cell/spatial profiling as translational diagnostics.** Recent single-cell studies provide cell-type resolved atlases that may yield biomarkers/targets for metastasis or immune therapy selection (sun2024singlecelltranscriptomicanalyses pages 1-2, li2024characterizationofcancer pages 1-2).

### 10.3 Differential diagnosis
No specific differential diagnosis list (e.g., benign vocal fold lesions, other laryngeal malignancies) was retrieved in this evidence set; therefore not asserted.

---

## 11. Outcome / prognosis

### 11.1 Population prognosis trends
The SEER incidence analysis notes long-term declines in incidence but does not provide detailed stage-stratified LSCC survival in the excerpts retrieved (mousavi2024laryngealcancerincidence pages 2-4, mousavi2024laryngealcancerincidence pages 4-6).

### 11.2 Prognostic biomarkers and factors
- Smoking burden (>10 pack-years) and localization (glottic vs supraglottic) were reported as independent prognostic factors for overall survival in an early-stage cohort (2024-09; https://doi.org/10.3390/biomedicines12092136) (wald2024outcomedisparitiesin pages 11-12).
- PD-L1 CPS associations with smoking and nodal status suggest prognostic/predictive relevance, though the prospective study primarily reports correlations rather than survival modeling (verro2024cancerandimmune pages 1-2).

---

## 12. Treatment (current applications and real-world implementations)

### 12.1 Standard-of-care by stage (practice synthesis)
A 2025 systemic therapy review summarizes the conventional stage-based approach:
- **Early-stage (T1–T2, N0):** treated with **single-modality therapy** (radiotherapy or organ-preserving surgery) (2025-03; https://doi.org/10.3389/fonc.2025.1541385) (fuereder2025systemictherapyfor pages 1-2)
- **Locally advanced:** typically **multimodality** management (e.g., surgery plus chemoradiation) guided by ESMO recommendations (fuereder2025systemictherapyfor pages 1-2)

### 12.2 Systemic therapy for recurrent/metastatic disease (quantitative evidence)
**Historical comparator (EXTREME).** In 442 R/M HNSCC patients (including 111 LSCC), EXTREME improved:
- OS **10.1 vs 7.4 months** (HR 0.80; p=0.04)
- PFS **5.6 vs 3.3 months** (HR 0.54; p<0.001) (fuereder2025systemictherapyfor pages 1-2)

**Pembrolizumab-based first-line standard (KEYNOTE-048 long-term).** The 2025 review reports KEYNOTE-048 outcomes and 5-year survival rates, including:
- Pembrolizumab vs EXTREME: OS **14.9 vs 10.7 months** in CPS ≥20 (HR 0.61)
- 5-year OS in CPS ≥20: pembrolizumab **19.9%** vs EXTREME **7.4%**
- Pembrolizumab+chemo 5-year OS in CPS ≥20: **23.9%** vs comparator **6.4%** (fuereder2025systemictherapyfor pages 2-4)

**Real-world/retrospective chemoimmunotherapy in larynx/hypopharynx SCC (2024).** A single-center retrospective cohort (50 eligible patients) treated with PD-1 inhibitor + albumin-bound paclitaxel + cisplatin reported:
- ORR **56.0% (28/50)**
- 1-year OS **80.2%**; 2-year OS **68.6%**
- Median PFS **11.67 months**; 1-year PFS **44.7%**
- Common AEs included rash and neutropenia; hypothyroidism occurred and was treated with levothyroxine in some patients (2024-05; https://doi.org/10.3389/fimmu.2024.1353435) (fang2024pd1inhibitorcombined pages 1-2, fang2024pd1inhibitorcombined pages 4-6).

### 12.3 Ongoing clinical trials and real-world implementation: organ preservation strategies (selected examples)
(ClinicalTrials.gov records; include status and key endpoints.)
- **ELOS / MK-3475-C44 (NCT06137378)** – Phase 2, randomized, open-label, multicenter; **pembrolizumab** added to induction docetaxel/cisplatin and RT strategy; **primary endpoint:** laryngectomy-free survival; **status:** recruiting; **start:** 2024-04-17; URL: https://clinicaltrials.gov/study/NCT06137378 (NCT06137378 chunk 1).
- **SMART-KEY (NCT04943445)** – Phase 2 single-arm; induction carboplatin/paclitaxel + pembrolizumab → concurrent RT + pembrolizumab → consolidation pembrolizumab; **primary endpoint:** 2-year laryngectomy-free survival; **status:** active not recruiting; **start:** 2022-02-22; URL: https://clinicaltrials.gov/study/NCT04943445 (NCT04943445 chunk 1).
- **CRT + pembrolizumab in locally advanced LSCC (NCT02759575)** – Phase I/II single-arm; pembrolizumab with definitive cisplatin chemoradiation; small enrollment (n=9); **status:** completed; results posted 2021-03; URL: https://clinicaltrials.gov/study/NCT02759575 (NCT02759575 chunk 1).
- **SBRT → toripalimab + docetaxel/cisplatin organ preservation (NCT06611137)** – Phase 2 single-group; **primary endpoint:** objective response rate post-neoadjuvant; **status:** recruiting; **start:** 2024-09-11; URL: https://clinicaltrials.gov/study/NCT06611137 (NCT06611137 chunk 1).
- **WOLF window-of-opportunity trial (NCT07423078)** – Phase 2 sequential nonrandomized; toripalimab + platinum + paclitaxel induction with response-based assignment; **primary endpoint:** 1-year DFS; **status:** recruiting; **start:** 2026-04-06; URL: https://clinicaltrials.gov/study/NCT07423078 (NCT07423078 chunk 1).

### 12.4 Suggested MAXO terms (examples)
- Surgical excision / laryngectomy / organ-preserving surgery: **MAXO:0000004** (surgical procedure; generic)
- Radiotherapy: **MAXO:0000136**
- Chemotherapy: **MAXO:0000647**
- Immune checkpoint inhibitor therapy (PD-1 blockade): **MAXO:0001026** (immunotherapy; generic mapping)

---

## 13. Prevention

**Primary prevention.** The dominant preventable exposures are tobacco and alcohol (maniaci2024personalizedtreatmentstrategies pages 1-2, macneil2021survivaltrendsof pages 25-30). This supports public health and clinical interventions for smoking cessation and alcohol risk reduction as primary prevention levers.

**HPV-related prevention.** HPV is a cited risk factor in a subset (maniaci2024personalizedtreatmentstrategies pages 1-2, macneil2021survivaltrendsof pages 25-30). The evidence set does not include direct guideline statements on HPV vaccination effects specifically on LSCC incidence; therefore not asserted beyond plausibility.

**Secondary prevention/screening.** No population screening program evidence or recommendations for asymptomatic screening were retrieved in this evidence set.

---

## 14. Other species / natural disease

No primary sources on naturally occurring LSCC in non-human species or zoonotic aspects were retrieved in this evidence set; therefore not asserted.

---

## 15. Model organisms

No primary sources describing specific LSCC animal models, organoids, or engineered model organisms were retrieved in this evidence set; therefore not asserted.

---

## Recent developments (2023–2024 priority highlights)

1. **Large-scale US incidence trend analysis (2024):** SEER-22 shows SCC accounts for ~94.5% of laryngeal cancers, strong male predominance, racial disparities (NHB men highest ASIR), and sustained incidence declines from 2000–2019 (Mousavi et al., 2024-07; https://doi.org/10.1186/s13690-024-01333-1) (mousavi2024laryngealcancerincidence pages 1-2, mousavi2024laryngealcancerincidence pages 4-6).
2. **Single-cell atlases (2024):** scRNA-seq in LSCC identifies immunosuppressive TME states (Tregs, early-stage macrophages, dysplastic plasma cells) and stromal autophagy as a putative nutrient-support mechanism (Sun et al., 2024-01; https://doi.org/10.1038/s42003-024-05765-x) (sun2024singlecelltranscriptomicanalyses pages 1-2).
3. **CSC programs and candidate targeting (2024):** scRNA-seq CSC characterization implicates PROM1/SOX4 and Wnt/Notch/hypoxia programs and nominates candidate drugs (erlotinib, OSI-027, ibrutinib) that may repress CSC gene programs (Li et al., 2024-08; https://doi.org/10.1093/gpbjnl/qzae056) (li2024characterizationofcancer pages 3-4, li2024characterizationofcancer pages 6-8).
4. **Organ preservation trials integrating immunotherapy (2022–2026 ongoing):** multiple phase II strategies add pembrolizumab or toripalimab to induction and RT/CRT workflows with laryngectomy-free survival or larynx preservation endpoints (NCT06137378 chunk 1, NCT04943445 chunk 1, NCT06611137 chunk 1).

---

## Evidence table (for structured extraction)

| Finding | Value/Statement | Source (year, DOI/URL) | Evidence type |
|---|---|---|---|
| US laryngeal cancer cases, SEER 2000–2019 | 104,991 laryngeal cancer cases identified in SEER-22; analysis excluded 2020 from trend modeling to reduce COVID-19 bias (mousavi2024laryngealcancerincidence pages 2-4, mousavi2024laryngealcancerincidence pages 1-2) | Mousavi et al., 2024, https://doi.org/10.1186/s13690-024-01333-1 | Population-based registry analysis |
| SCC proportion | Squamous cell carcinoma comprised 94.53% of laryngeal cancers in SEER 2000–2019 (mousavi2024laryngealcancerincidence pages 2-4, mousavi2024laryngealcancerincidence pages 1-2) | Mousavi et al., 2024, https://doi.org/10.1186/s13690-024-01333-1 | Population-based registry analysis |
| ASIR by sex | Age-standardized incidence rate (ASIR) per 100,000: men 5.98 (95% CI 5.94–6.02), women 1.25 (95% CI 1.23–1.27) (mousavi2024laryngealcancerincidence pages 4-6, mousavi2024laryngealcancerincidence pages 2-4) | Mousavi et al., 2024, https://doi.org/10.1186/s13690-024-01333-1 | Population-based registry analysis |
| Incidence trend decline by sex | Average annual percent change (AAPC) in incidence over 2000–2019: men −2.70%, women −2.26%; overall AAPC −2.50% (mousavi2024laryngealcancerincidence pages 4-6, mousavi2024laryngealcancerincidence pages 2-4) | Mousavi et al., 2024, https://doi.org/10.1186/s13690-024-01333-1 | Population-based registry analysis |
| Race/ethnicity: highest-risk subgroup | Non-Hispanic Black men had the highest ASIR: 9.13 per 100,000 (95% CI 8.96–9.31) and the largest decline: AAPC −3.26% (mousavi2024laryngealcancerincidence pages 4-6, mousavi2024laryngealcancerincidence pages 1-2) | Mousavi et al., 2024, https://doi.org/10.1186/s13690-024-01333-1 | Population-based registry analysis |
| Race/ethnicity comparator groups | Non-Hispanic White men: ASIR 6.16, AAPC −2.42%; Hispanic men: ASIR 5.00, AAPC −2.9%; NHB women: ASIR 1.74, AAPC −2.49%; NHW women: ASIR 1.40, AAPC −1.76% (mousavi2024laryngealcancerincidence pages 4-6) | Mousavi et al., 2024, https://doi.org/10.1186/s13690-024-01333-1 | Population-based registry analysis |
| TP53 alteration | TP53 is described as the most commonly altered gene in laryngeal cancer/LSCC, with mutations in “as many as 70% of instances” (maniaci2024personalizedtreatmentstrategies pages 3-5) | Maniaci et al., 2024, https://doi.org/10.3390/jpm14101048 | Review synthesizing molecular profiling studies |
| PI3K/AKT/mTOR pathway | Recurrent PIK3CA alterations drive hyperactivation of the PI3K/AKT/mTOR pathway in laryngeal cancer (maniaci2024personalizedtreatmentstrategies pages 3-5, maniaci2024personalizedtreatmentstrategies pages 1-2) | Maniaci et al., 2024, https://doi.org/10.3390/jpm14101048 | Review synthesizing molecular profiling studies |
| Copy-number alterations | Common CNVs include CDKN2A loss at 9p21 and gains/amplifications of CCND1 (11q13), EGFR (7p11), and MYC (8q24); 11q13 amplification is linked to poor prognosis/nodal metastasis (maniaci2024personalizedtreatmentstrategies pages 3-5) | Maniaci et al., 2024, https://doi.org/10.3390/jpm14101048 | Review synthesizing molecular profiling studies |
| Epigenetic biomarker | MGMT promoter methylation is highlighted as a relevant epigenetic alteration in laryngeal cancer molecular profiling (maniaci2024personalizedtreatmentstrategies pages 1-2) | Maniaci et al., 2024, https://doi.org/10.3390/jpm14101048 | Review synthesizing molecular profiling studies |
| Immune biomarkers | PD-L1, TMB, and MSI are discussed as biomarkers for immunotherapy selection; elevated TMB may associate with improved anti-PD-1/PD-L1 outcomes, while MSI-H is uncommon at about 3% of HNSCC including laryngeal cancers (maniaci2024personalizedtreatmentstrategies pages 9-11) | Maniaci et al., 2024, https://doi.org/10.3390/jpm14101048 | Review synthesizing molecular profiling studies |
| PD-L1 clinical correlation in LSCC | In a prospective LSCC cohort (n=58), PD-L1 CPS correlated significantly with smoking, nodal stage, and elevated CRP, supporting biomarker relevance in LSCC (verro2024cancerandimmune pages 1-2) | Verro et al., 2024, https://doi.org/10.1007/s00405-024-08822-7 | Prospective human clinical study |


*Table: This table compiles compact 2024–2025 evidence on LSCC/laryngeal cancer epidemiology from SEER and key molecular features relevant to biomarker-driven care. It is useful for quick extraction of incidence, disparities, and major genomic/immune alterations with citeable sources.*

---

## Limitations of this report (based on accessible evidence set)
- Several requested identifier systems (MeSH, ICD-11, OMIM, Orphanet) were not retrieved with tool-accessible sources; only EFO and MONDO parent concept were available via OpenTargets (OpenTargets Search: laryngeal squamous cell carcinoma).
- Differential diagnosis lists, guideline-grade screening recommendations, and quantitative QoL outcomes were not retrieved.
- Germline inheritance/penetrance data are generally not applicable to LSCC as a primarily somatic malignancy; no LSCC-specific germline evidence was retrieved.



References

1. (OpenTargets Search: laryngeal squamous cell carcinoma): Open Targets Query (laryngeal squamous cell carcinoma, 25 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

2. (wald2024outcomedisparitiesin pages 11-12): Theresa Wald, Tim-Jonathan Koppe, Markus Pirlich, Veit Zebralla, Viktor Kunz, Andreas Dietz, Matthaeus Stoehr, and Gunnar Wichmann. Outcome disparities in patients with early-stage laryngeal cancer depending on localization, tobacco consumption, and treatment modality. Biomedicines, 12:2136, Sep 2024. URL: https://doi.org/10.3390/biomedicines12092136, doi:10.3390/biomedicines12092136. This article has 2 citations.

3. (maniaci2024personalizedtreatmentstrategies pages 1-2): Antonino Maniaci, Giovanni Giurdanella, Carlos Chiesa Estomba, Simone Mauramati, Andy Bertolin, Marco Lionello, Miguel Mayo-Yanez, Paolo Boscolo Rizzo, Jerome R. Lechien, and Mario Lentini. Personalized treatment strategies via integration of gene expression biomarkers in molecular profiling of laryngeal cancer. Journal of Personalized Medicine, 14:1048, Oct 2024. URL: https://doi.org/10.3390/jpm14101048, doi:10.3390/jpm14101048. This article has 9 citations.

4. (macneil2021survivaltrendsof pages 20-25): D MacNeil. Survival trends of patients with subglottic squamous cell carcinoma: a population based cohort study. Unknown journal, 2021.

5. (macneil2021survivaltrendsof pages 25-30): D MacNeil. Survival trends of patients with subglottic squamous cell carcinoma: a population based cohort study. Unknown journal, 2021.

6. (mousavi2024laryngealcancerincidence pages 1-2): Seyed Ehsan Mousavi, Mehran Ilaghi, Armin Aslani, Morvarid Najafi, Zahra Yekta, and Seyed Aria Nejadghaderi. Laryngeal cancer incidence trends in the united states over 2000–2020: a population-based analysis. Archives of Public Health, Jul 2024. URL: https://doi.org/10.1186/s13690-024-01333-1, doi:10.1186/s13690-024-01333-1. This article has 22 citations and is from a peer-reviewed journal.

7. (mousavi2024laryngealcancerincidence pages 2-4): Seyed Ehsan Mousavi, Mehran Ilaghi, Armin Aslani, Morvarid Najafi, Zahra Yekta, and Seyed Aria Nejadghaderi. Laryngeal cancer incidence trends in the united states over 2000–2020: a population-based analysis. Archives of Public Health, Jul 2024. URL: https://doi.org/10.1186/s13690-024-01333-1, doi:10.1186/s13690-024-01333-1. This article has 22 citations and is from a peer-reviewed journal.

8. (mousavi2024laryngealcancerincidence pages 4-6): Seyed Ehsan Mousavi, Mehran Ilaghi, Armin Aslani, Morvarid Najafi, Zahra Yekta, and Seyed Aria Nejadghaderi. Laryngeal cancer incidence trends in the united states over 2000–2020: a population-based analysis. Archives of Public Health, Jul 2024. URL: https://doi.org/10.1186/s13690-024-01333-1, doi:10.1186/s13690-024-01333-1. This article has 22 citations and is from a peer-reviewed journal.

9. (verro2024cancerandimmune pages 1-2): Barbara Verro, Giuseppe Saraniti, Gaetano Ottoveggio, and Carmelo Saraniti. Cancer and immune response: the role of pd-1/pd-l1 checkpoint in laryngeal carcinoma. preliminary results. European Archives of Oto-Rhino-Laryngology, 281:5411-5417, Jul 2024. URL: https://doi.org/10.1007/s00405-024-08822-7, doi:10.1007/s00405-024-08822-7. This article has 3 citations and is from a peer-reviewed journal.

10. (sun2024singlecelltranscriptomicanalyses pages 1-2): Yuanyuan Sun, Sheng Chen, Yongping Lu, Zhenming Xu, Weineng Fu, and Wei Yan. Single-cell transcriptomic analyses of tumor microenvironment and molecular reprograming landscape of metastatic laryngeal squamous cell carcinoma. Communications Biology, Jan 2024. URL: https://doi.org/10.1038/s42003-024-05765-x, doi:10.1038/s42003-024-05765-x. This article has 36 citations and is from a peer-reviewed journal.

11. (li2024characterizationofcancer pages 1-2): Yanguo Li, Chen Lin, Yidian Chu, Zhengyu Wei, Qi Ding, Shanshan Gu, Hongxia Deng, Qi Liao, and Zhisen Shen. Characterization of cancer stem cells in laryngeal squamous cell carcinoma by single-cell rna sequencing. Genomics, Proteomics &amp; Bioinformatics, Aug 2024. URL: https://doi.org/10.1093/gpbjnl/qzae056, doi:10.1093/gpbjnl/qzae056. This article has 12 citations and is from a peer-reviewed journal.

12. (NCT06137378 chunk 1): Andreas Dietz. European Larynx Organ Preservation Study (ELOS) [MK-3475-C44]. University of Leipzig. 2024. ClinicalTrials.gov Identifier: NCT06137378

13. (NCT04943445 chunk 1):  Study of a Pembrolizumab-based Organ Preservation Strategy for Locally Advanced Larynx Cancers. Latin American Cooperative Oncology Group. 2022. ClinicalTrials.gov Identifier: NCT04943445

14. (fuereder2025systemictherapyfor pages 2-4): Thorsten Fuereder, Florian Kocher, and Jan Baptist Vermorken. Systemic therapy for laryngeal carcinoma. Frontiers in Oncology, Mar 2025. URL: https://doi.org/10.3389/fonc.2025.1541385, doi:10.3389/fonc.2025.1541385. This article has 9 citations.

15. (maniaci2024personalizedtreatmentstrategies pages 3-5): Antonino Maniaci, Giovanni Giurdanella, Carlos Chiesa Estomba, Simone Mauramati, Andy Bertolin, Marco Lionello, Miguel Mayo-Yanez, Paolo Boscolo Rizzo, Jerome R. Lechien, and Mario Lentini. Personalized treatment strategies via integration of gene expression biomarkers in molecular profiling of laryngeal cancer. Journal of Personalized Medicine, 14:1048, Oct 2024. URL: https://doi.org/10.3390/jpm14101048, doi:10.3390/jpm14101048. This article has 9 citations.

16. (maniaci2024personalizedtreatmentstrategies pages 9-11): Antonino Maniaci, Giovanni Giurdanella, Carlos Chiesa Estomba, Simone Mauramati, Andy Bertolin, Marco Lionello, Miguel Mayo-Yanez, Paolo Boscolo Rizzo, Jerome R. Lechien, and Mario Lentini. Personalized treatment strategies via integration of gene expression biomarkers in molecular profiling of laryngeal cancer. Journal of Personalized Medicine, 14:1048, Oct 2024. URL: https://doi.org/10.3390/jpm14101048, doi:10.3390/jpm14101048. This article has 9 citations.

17. (macneil2021survivaltrendsof pages 113-115): D MacNeil. Survival trends of patients with subglottic squamous cell carcinoma: a population based cohort study. Unknown journal, 2021.

18. (sun2024singlecelltranscriptomicanalyses pages 10-12): Yuanyuan Sun, Sheng Chen, Yongping Lu, Zhenming Xu, Weineng Fu, and Wei Yan. Single-cell transcriptomic analyses of tumor microenvironment and molecular reprograming landscape of metastatic laryngeal squamous cell carcinoma. Communications Biology, Jan 2024. URL: https://doi.org/10.1038/s42003-024-05765-x, doi:10.1038/s42003-024-05765-x. This article has 36 citations and is from a peer-reviewed journal.

19. (li2024characterizationofcancer pages 3-4): Yanguo Li, Chen Lin, Yidian Chu, Zhengyu Wei, Qi Ding, Shanshan Gu, Hongxia Deng, Qi Liao, and Zhisen Shen. Characterization of cancer stem cells in laryngeal squamous cell carcinoma by single-cell rna sequencing. Genomics, Proteomics &amp; Bioinformatics, Aug 2024. URL: https://doi.org/10.1093/gpbjnl/qzae056, doi:10.1093/gpbjnl/qzae056. This article has 12 citations and is from a peer-reviewed journal.

20. (li2024characterizationofcancer pages 6-8): Yanguo Li, Chen Lin, Yidian Chu, Zhengyu Wei, Qi Ding, Shanshan Gu, Hongxia Deng, Qi Liao, and Zhisen Shen. Characterization of cancer stem cells in laryngeal squamous cell carcinoma by single-cell rna sequencing. Genomics, Proteomics &amp; Bioinformatics, Aug 2024. URL: https://doi.org/10.1093/gpbjnl/qzae056, doi:10.1093/gpbjnl/qzae056. This article has 12 citations and is from a peer-reviewed journal.

21. (li2024characterizationofcancer pages 9-10): Yanguo Li, Chen Lin, Yidian Chu, Zhengyu Wei, Qi Ding, Shanshan Gu, Hongxia Deng, Qi Liao, and Zhisen Shen. Characterization of cancer stem cells in laryngeal squamous cell carcinoma by single-cell rna sequencing. Genomics, Proteomics &amp; Bioinformatics, Aug 2024. URL: https://doi.org/10.1093/gpbjnl/qzae056, doi:10.1093/gpbjnl/qzae056. This article has 12 citations and is from a peer-reviewed journal.

22. (mousavi2024laryngealcancerincidence media a846858a): Seyed Ehsan Mousavi, Mehran Ilaghi, Armin Aslani, Morvarid Najafi, Zahra Yekta, and Seyed Aria Nejadghaderi. Laryngeal cancer incidence trends in the united states over 2000–2020: a population-based analysis. Archives of Public Health, Jul 2024. URL: https://doi.org/10.1186/s13690-024-01333-1, doi:10.1186/s13690-024-01333-1. This article has 22 citations and is from a peer-reviewed journal.

23. (mousavi2024laryngealcancerincidence media 9610280e): Seyed Ehsan Mousavi, Mehran Ilaghi, Armin Aslani, Morvarid Najafi, Zahra Yekta, and Seyed Aria Nejadghaderi. Laryngeal cancer incidence trends in the united states over 2000–2020: a population-based analysis. Archives of Public Health, Jul 2024. URL: https://doi.org/10.1186/s13690-024-01333-1, doi:10.1186/s13690-024-01333-1. This article has 22 citations and is from a peer-reviewed journal.

24. (fuereder2025systemictherapyfor pages 1-2): Thorsten Fuereder, Florian Kocher, and Jan Baptist Vermorken. Systemic therapy for laryngeal carcinoma. Frontiers in Oncology, Mar 2025. URL: https://doi.org/10.3389/fonc.2025.1541385, doi:10.3389/fonc.2025.1541385. This article has 9 citations.

25. (fang2024pd1inhibitorcombined pages 1-2): Qi Fang, Xiaodi Li, Pengfei Xu, Fei Cao, Di Wu, Xinrui Zhang, Chunyan Chen, Jianming Gao, Yong Su, and Xuekui Liu. Pd-1 inhibitor combined with paclitaxel and cisplatin in the treatment of recurrent and metastatic hypopharyngeal/laryngeal squamous cell carcinoma: efficacy and survival outcomes. Frontiers in Immunology, May 2024. URL: https://doi.org/10.3389/fimmu.2024.1353435, doi:10.3389/fimmu.2024.1353435. This article has 10 citations and is from a peer-reviewed journal.

26. (fang2024pd1inhibitorcombined pages 4-6): Qi Fang, Xiaodi Li, Pengfei Xu, Fei Cao, Di Wu, Xinrui Zhang, Chunyan Chen, Jianming Gao, Yong Su, and Xuekui Liu. Pd-1 inhibitor combined with paclitaxel and cisplatin in the treatment of recurrent and metastatic hypopharyngeal/laryngeal squamous cell carcinoma: efficacy and survival outcomes. Frontiers in Immunology, May 2024. URL: https://doi.org/10.3389/fimmu.2024.1353435, doi:10.3389/fimmu.2024.1353435. This article has 10 citations and is from a peer-reviewed journal.

27. (NCT02759575 chunk 1): Vinita Takiar. A Study of Chemoradiation Plus Pembrolizumab for Locally Advanced Laryngeal Squamous Cell Carcinoma. Vinita Takiar. 2016. ClinicalTrials.gov Identifier: NCT02759575

28. (NCT06611137 chunk 1): Fang-Yun Xie. SBRT Followed by Chemoimmunotherapy of Toripalimab Plus Docetaxel and Cisplatin for Larynx Preservation in Patients with Locally Regionally Advanced Squamous Cell Carcinoma of the Larynx and Hypopharynx. Sun Yat-sen University. 2024. ClinicalTrials.gov Identifier: NCT06611137

29. (NCT07423078 chunk 1): Matthew Spector. Window of Opportunity in Preserving Laryngeal Function Trial. Matthew Spector. 2026. ClinicalTrials.gov Identifier: NCT07423078