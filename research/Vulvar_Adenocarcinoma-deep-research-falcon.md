---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-09T09:25:01.471836'
end_time: '2026-05-09T09:45:02.379918'
duration_seconds: 1200.91
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Vulvar Adenocarcinoma
  mondo_id: ''
  category: ''
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 43
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Vulvar Adenocarcinoma
- **MONDO ID:**  (if available)
- **Category:** 

## Research Objectives

Please provide a comprehensive research report on **Vulvar Adenocarcinoma** covering all of the
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
- **Disease Name:** Vulvar Adenocarcinoma
- **MONDO ID:**  (if available)
- **Category:** 

## Research Objectives

Please provide a comprehensive research report on **Vulvar Adenocarcinoma** covering all of the
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


# Vulvar Adenocarcinoma — Comprehensive Disease Characteristics Report (2026-05-09)

## Target Disease
- **Disease Name:** Vulvar adenocarcinoma (primary vulvar glandular carcinomas; includes Bartholin gland adenocarcinoma, intestinal-type vulvar adenocarcinoma, mammary-like/mammary gland type adenocarcinoma, and invasive extramammary Paget disease with/without associated adenocarcinoma)
- **MONDO ID:** Not identified from retrieved sources using available tools (gap).
- **Category:** Malignant neoplasm of vulva; non-squamous vulvar cancer; glandular vulvar carcinoma.

## Evidence Scope and Notes
Vulvar adenocarcinoma is rare and heterogeneous; most high-quality evidence and guidelines address **vulvar cancer overall** (predominantly squamous). Consequently, management evidence for vulvar adenocarcinoma subtypes is often based on small series/case reports and extrapolation from broader vulvar cancer guidance. This report prioritizes 2023–2024 sources when available and uses primary and guideline literature retrieved with tools.

---

## 1. Disease Information

### 1.1 What is the disease?
**Vulvar adenocarcinoma** refers to malignant epithelial tumors of the vulva with glandular differentiation. In vulvar cancer, **squamous cell carcinoma (SCC) is predominant (>90%)**, and adenocarcinomas are uncommon. Rarer vulvar histologies explicitly recognized in contemporary guidelines include **extramammary Paget’s disease** and **Bartholin gland adenocarcinoma**, among others. (aburustum2024vulvarcancerversion pages 1-2, ha2024imaginginvulval pages 1-2)

### 1.2 Key identifiers (available from retrieved sources)
- **ICD-10 (vulvar cancer overall):** **C51** (vulvar cancer) used in an administrative-database study. (muigai2018potentialdelayin pages 1-2)
- **ICD-10 related codes used as “pre-diagnosis” mimics/overlaps:** Bartholin gland diseases **N75**; inflammation of vagina/vulva **N76**; other vulvar noninflammatory disorders **N90.5–N90.9**. (muigai2018potentialdelayin pages 1-2)
- **FIGO staging:** **FIGO 2021** applies to vulvar cancers of all morphologic types **except melanoma** and incorporates imaging in staging; depth of invasion measurement is specified. (ha2024imaginginvulval pages 1-2, ha2024imaginginvulval media 862afa93)
- **WHO classification:** Vulvar adenocarcinomas should be diagnosed/subtyped using the **WHO 2020 classification** (as referenced in reporting standards). (faruqi2018standardsanddatasets pages 12-16)

**Unavailable with current tool evidence:** OMIM, Orphanet, MeSH IDs, MONDO ID.

### 1.3 Synonyms / alternative names (subtype-level)
- **Intestinal-type vulvar adenocarcinoma (VAIt):** WHO 2020 describes “**primary villo-glandular mucinous adenocarcinoma exhibiting intestinal differentiation**” and discourages “cloacogenic carcinoma/adenocarcinoma” terminology. (dellino2022“intestinaltype”vulvaradenocarcinoma pages 1-2)
- **Adenocarcinoma of mammary gland type (AMGT)** / **mammary-like gland adenocarcinoma** of vulva. (morais2022diagnosisandmanagement pages 1-2)
- **Extramammary Paget’s disease (EMPD)** of vulva; can be invasive or represent manifestation of underlying vulvar adenocarcinoma per Wilkinson/Brown subclassification. (iacobone2023tipsandtricks pages 2-4)

### 1.4 Evidence source type
- Predominantly **aggregated** resources (NCCN guideline; imaging guideline review; staging/reporting standards) plus **cohort/registry** analyses (SEER metastatic vulvar cancer; EMPD referral-center cohort; Bartholin carcinoma institutional cohort) and **case reports** (mammary-like adenocarcinoma; metastatic HER2+ EMPD WGS). (aburustum2024vulvarcancerversion pages 1-2, ha2024imaginginvulval pages 1-2, meng2024overallsurvivalassociated pages 1-2, iacobone2023tipsandtricks pages 2-4, nazeran2019bartholinglandcarcinoma pages 1-2, morais2022diagnosisandmanagement pages 1-2, lim2024wholegenomesequencing pages 1-2)

---

## 2. Etiology

### 2.1 Disease causal factors (current understanding)
Because “vulvar adenocarcinoma” is a category spanning multiple entities, etiology is **subtype-dependent**:
- **Bartholin gland primaries:** etiologic inference is limited by rarity; HPV appears important for **Bartholin SCC** but not clearly established for adenocarcinoma. In a 13-case series, all Bartholin SCC showed diffuse p16, while the **single adenocarcinoma** showed patchy p16 staining. (nazeran2019bartholinglandcarcinoma pages 1-2)
- **Intestinal-type vulvar adenocarcinoma:** proposed embryologic origins include **cloacal remnants** and other metaplasia hypotheses; inflammation and genetic changes are discussed. (dellino2022“intestinaltype”vulvaradenocarcinoma pages 1-2, dellino2022“intestinaltype”vulvaradenocarcinoma pages 5-6)
- **EMPD:** described as a rare neoplasm arising in apocrine-rich skin regions including vulva; molecular mechanisms include HER2 biology and alternative pathway activation (e.g., FGFR1/TGFβ enrichment in one WGS case). (lim2024wholegenomesequencing pages 1-2)

### 2.2 Risk factors
From NCCN Vulvar Cancer v3.2024 (applies to vulvar cancer overall; includes rare histologies):
- **Increasing age**
- **HPV infection**
- **Cigarette smoking**
- **Inflammatory vulvar conditions**
- **Immunodeficiency** (aburustum2024vulvarcancerversion pages 1-2)

Intestinal-type VAIt review additionally lists exposures/conditions relevant to vulvar carcinogenesis broadly (lichen sclerosus/vulvar dystrophies, smoking, HPV infection) and environmental insults (infections, UV, physical damage), but without quantitative risk estimates for VAIt specifically. (dellino2022“intestinaltype”vulvaradenocarcinoma pages 5-6)

For vulvar SCC pathogenesis context (important for mixed histology differential and prevention frameworks): HPV DNA is reported in ~40% of invasive vulvar cancers in one modern review, with HPV-associated tumors tending to occur in younger women and having better outcomes; HPV-independent tumors are associated with chronic dermatoses such as lichen sclerosus. (ayalapeacock2025advancesinvulvar pages 1-3)

### 2.3 Protective factors
No protective genetic or environmental factors specific to vulvar adenocarcinoma subtypes were identified in retrieved sources.

### 2.4 Gene–environment interactions
No explicit gene–environment interaction evidence specific to vulvar adenocarcinoma was identified in retrieved sources.

---

## 3. Phenotypes

### 3.1 Core clinical phenotypes (subtype-aware)
**A. Vulvar EMPD (clinical phenotype and QoL impact)**
- Typical appearance: **“erythematous, scaly or eczematous plaque on the vulva and perineum with occasional erosions or ulcerations, hypopigmentation and nodules”** and symptoms: **“Itching and burning pain”**. (iacobone2023tipsandtricks pages 1-2)
- High relapse burden: persistence/recurrence is common (86% in one cohort), often requiring repeated procedures. (iacobone2023tipsandtricks pages 2-4)
- Cervico-vaginal spread can be clinically silent: **“None reported vaginal bleeding or other suspicious symptoms”** and detection was frequently via abnormal glandular cytology. (iacobone2023tipsandtricks pages 1-2)

**Suggested HPO terms (examples):**
- Vulvar pruritus (HP:0031297; if unavailable, use “Pruritus” HP:0000989) 
- Burning pain (Pain; HP:0012531) 
- Erythematous skin lesion (HP:0025548) 
- Eczematous dermatitis (HP:0000964) 
- Vulvar mass (HP:0030417; if unavailable, “Mass” HP:0100242)

**B. Bartholin-region carcinoma (including adenocarcinoma subtype)**
- Presents as a mass in the Bartholin region; diagnostic delay is common due to misclassification as cyst/abscess, motivating biopsy in women ≥40–45 with persistent/recurrent solid lesions. (kostov2025bartholinglandcarcinoma pages 20-21)

**Suggested HPO terms:**
- Vulvar mass (HP:0030417), Vulvar pain (HP:0031242), Ulceration (HP:0001053)

**C. Intestinal-type vulvar adenocarcinoma (VAIt)**
- Often presents as a solitary lesion in labia/perineal/posterior vulvar structures and may mimic benign lesions. (colalillo2025intestinaltypeadenocarcinomais pages 11-13, dellino2022“intestinaltype”vulvaradenocarcinoma pages 1-2)

### 3.2 Natural history and progression
- **EMPD:** persistent/relapsing course; cervico-vaginal involvement cumulative incidence increased over time (2.5% at 5 years, 6.5% at 10 years, 14.0% at 15 years). (iacobone2023tipsandtricks pages 1-2)
- **FIGO staging and invasion:** FIGO 2021 stage IA includes tumors ≤2 cm with stromal invasion ≤1 mm; stage IB includes >2 cm or invasion >1 mm. (ha2024imaginginvulval pages 1-2, ha2024imaginginvulval media 862afa93)

### 3.3 Quality of life impact
Direct QoL instruments specific to vulvar adenocarcinoma were not retrieved; however, EMPD symptom burden (itching/burning) and high recurrence requiring repeated interventions plausibly affects QoL and sexual function. (iacobone2023tipsandtricks pages 2-4, iacobone2023tipsandtricks pages 1-2)

---

## 4. Genetic/Molecular Information

### 4.1 Causal genes
No germline causal genes specific to “vulvar adenocarcinoma” as a disease category were identified in retrieved sources.

### 4.2 Somatic alterations, biomarkers, and IHC patterns (subtype-level)

**A. Vulvar EMPD / Paget-associated vulvar adenocarcinoma**
- HER2 biology is clinically important. In a WGS case report and literature synthesis, HER2 overexpression in EMPD series was reported as **15–65%**, with ERBB2 amplification **13–43%**; in the case, >90% tumor cells stained HER2+ with ≥40% showing 3+ intensity. (lim2024wholegenomesequencing pages 2-4)
- WGS found copy number gains on chromosomes 7 and 8 (n=81 genes, 92.6% on chr8) and pathway enrichment for **TGFβ** and **FGFR1** signaling; notably **“ERBB2 gene did not exhibit high copy number gain… although 90% of tumor cells stained HER2-positive”**, suggesting overexpression without strong ERBB2 CN gain in that case. (lim2024wholegenomesequencing pages 1-2)

**Mechanistic interpretation (expert analysis):** These findings support a model where HER2 protein overexpression can occur via mechanisms beyond high-level ERBB2 amplification (e.g., regulatory/structural alterations), and where parallel signaling (FGFR1/TGFβ) may modulate response/resistance to HER2-directed therapy. (lim2024wholegenomesequencing pages 1-2)

**B. Mammary-like / mammary gland type adenocarcinoma (AMGT) of the vulva**
- IHC profile can resemble breast carcinoma: strong **ER positivity (reported 90–100%)**, CK7/CAM5.2/GATA3 positivity; typically negative for PR, GCDFP-15, SOX10, p63, CK20. HER2 may be equivocal (2+) with FISH negative in a case. (morais2022diagnosisandmanagement pages 1-2)
- Key diagnostic principle is exclusion of a breast primary by clinical and imaging workup. (morais2022diagnosisandmanagement pages 1-2)

**C. Intestinal-type vulvar adenocarcinoma (VAIt)**
- Characteristic “intestinal” IHC phenotype: frequent **CK20** and **CDX2** positivity, often CEA positive, variable CK7 and p16; requires exclusion of metastatic colorectal primary. (dellino2022“intestinaltype”vulvaradenocarcinoma pages 1-2, colalillo2025intestinaltypeadenocarcinomais pages 11-13)

**D. Bartholin gland carcinoma (with adenocarcinoma subtype)**
- In a 13-case cohort (1984–2017), Bartholin SCC showed diffuse p16; the single adenocarcinoma showed patchy p16 staining. (nazeran2019bartholinglandcarcinoma pages 1-2)
- Reporting standards emphasize diagnosing primary Bartholin gland origin by anatomic region involvement, compatible histology, no other primary identified, and preferably adjacent normal Bartholin gland tissue. (faruqi2018standardsanddatasets pages 12-16)

### 4.3 Epigenetics / chromosomal abnormalities
Not specifically identified for vulvar adenocarcinoma subtypes in retrieved evidence.

### 4.4 Suggested pathway and ontology terms
**Pathways (GO biological process suggestions):**
- ERBB2 signaling pathway / receptor tyrosine kinase signaling (GO:0007169; broad)
- PI3K-AKT signaling (useful for HER2/PTEN context; supported indirectly via trastuzumab resistance mechanisms and HER2 pathway emphasis) (lim2024wholegenomesequencing pages 1-2)
- TGFβ receptor signaling pathway (GO:0007179) (lim2024wholegenomesequencing pages 1-2)
- FGFR signaling pathway (GO:0008543) (lim2024wholegenomesequencing pages 1-2)

**Cell types (Cell Ontology suggestions):**
- Keratinocyte / epithelial cell (CL:0000312; generic epithelium)
- Glandular epithelial cell / secretory epithelial cell (useful for adenocarcinoma and apocrine-associated EMPD) (lim2024wholegenomesequencing pages 1-2)

---

## 5. Environmental Information

- **Lifestyle/environmental factors (vulvar cancer overall):** smoking is a risk factor per NCCN 2024. (aburustum2024vulvarcancerversion pages 1-2)
- **Inflammatory vulvar conditions:** risk factor per NCCN; HPV-independent pathway often linked to chronic dermatoses (e.g., lichen sclerosus) in SCC literature, relevant for differential diagnosis and prevention frameworks. (aburustum2024vulvarcancerversion pages 1-2, ayalapeacock2025advancesinvulvar pages 1-3)
- **Infectious agents:** HPV infection is a recognized risk factor for vulvar cancer; HPV’s role in VAIt is described as ambiguous in older systematic review, and Bartholin SCC appears HPV-associated by p16. (aburustum2024vulvarcancerversion pages 1-2, nazeran2019bartholinglandcarcinoma pages 1-2, dellino2022“intestinaltype”vulvaradenocarcinoma pages 9-10)

---

## 6. Mechanism / Pathophysiology

### 6.1 Subtype-specific causal chains (high-level)

**A. EMPD / Paget-associated adenocarcinoma**
1) Transformation of apocrine-rich cutaneous epithelium into Paget cells within epidermis.  
2) Potential progression to stromal invasion and/or association with an underlying adenocarcinoma (Wilkinson/Brown Type 1b/1c).  
3) Molecular drivers may include HER2 overexpression; alternative signaling (FGFR1/TGFβ) may contribute to aggressive/metastatic behavior and treatment response/resistance. (iacobone2023tipsandtricks pages 2-4, lim2024wholegenomesequencing pages 1-2)

**B. Intestinal-type vulvar adenocarcinoma**
1) Proposed embryologic substrate (persistent cloacal remnants or metaplastic intestinal epithelium).  
2) Development of colorectal-like glandular neoplasm with intestinal differentiation.  
3) Clinical manifestation as vulvar/perineal lesion; important downstream step is ruling out metastatic colorectal carcinoma. (dellino2022“intestinaltype”vulvaradenocarcinoma pages 1-2, dellino2022“intestinaltype”vulvaradenocarcinoma pages 5-6)

**C. Mammary-like gland adenocarcinoma**
1) Malignant transformation of mammary-like vulvar glands.  
2) Breast-carcinoma-like morphology and ER-driven biology.  
3) Clinical implication: requires exclusion of metastatic breast primary and may suggest endocrine-therapy relevance (inferred from ER positivity; treatment decisions are individualized). (morais2022diagnosisandmanagement pages 1-2)

---

## 7. Anatomical Structures Affected

### 7.1 Organ/tissue level (UBERON suggestions)
- **Vulva** (UBERON:0000997)
- **Labia majora/minora** (UBERON terms)
- **Bartholin gland (greater vestibular gland)** (UBERON term; implicated in Bartholin primaries) (nazeran2019bartholinglandcarcinoma pages 1-2)
- **Perineum / anogenital region** (relevant for EMPD distribution) (lim2024wholegenomesequencing pages 1-2)
- **Cervix and vagina** (for cervico-vaginal involvement in EMPD) (iacobone2023tipsandtricks pages 1-2)

### 7.2 Subcellular
Not specifically addressed in retrieved evidence.

---

## 8. Temporal Development

- **Typical onset:** vulvar cancers are more common with increasing age; EMPD typical age 60–80 years; EMPD cohort mean 63.3 years. (aburustum2024vulvarcancerversion pages 1-2, lim2024wholegenomesequencing pages 1-2, iacobone2023tipsandtricks pages 2-4)
- **Course:** EMPD is often chronic/relapsing (local recurrence after excision reported up to 73% in literature; cohort persistence/recurrence 86%). (iacobone2023tipsandtricks pages 1-2, iacobone2023tipsandtricks pages 2-4)
- **Late events:** cervico-vaginal involvement may occur very late (example: 251 months after initial vulvar EMPD). (iacobone2023tipsandtricks pages 6-9)

---

## 9. Inheritance and Population

### 9.1 Epidemiology
- **Global burden (vulvar cancer overall):** ~47,000 cases in 2022 reported in a 2024 imaging review. (ha2024imaginginvulval pages 1-2)
- **US annual diagnoses (vulvar cancer overall):** NCCN cites ~6,470 annually. (aburustum2024vulvarcancerversion pages 1-2)
- **EMPD incidence:** 0.1–2.4 per million per year; ~20% present with distant metastatic disease. (lim2024wholegenomesequencing pages 1-2)

### 9.2 Sex ratio
- Vulvar cancers occur in individuals with vulvar anatomy; EMPD also occurs in male genital region (case report). (lim2024wholegenomesequencing pages 1-2)

### 9.3 Genetics/inheritance
No Mendelian inheritance pattern is established for vulvar adenocarcinoma in retrieved evidence.

---

## 10. Diagnostics

### 10.1 Clinical and pathology diagnosis
- **Biopsy is required** for definitive diagnosis of vulvar lesions; vulvoscopy helps identify optimal biopsy sites. (corte2024currentpreoperativemanagement pages 1-2, kesic2022earlydiagnosticsof pages 1-2)

**EMPD cervico-vaginal extension diagnostic pathway (referral center practice):**
- **“All cases except one were firstly detected by abnormal glandular cytology.”** (iacobone2023tipsandtricks pages 1-2)
- Abnormal cytology prompted colposcopy and cervical/vaginal biopsies; HPV testing negative in CV EMPD cases; HER2 immunocytochemistry used on cell blocks in some cases. (iacobone2023tipsandtricks pages 6-9)

**Differential diagnosis (key points):**
- Mammary-like vulvar adenocarcinoma requires exclusion of breast primary (mammography/US/PET used in reported cases). (morais2022diagnosisandmanagement pages 1-2)
- Intestinal-type vulvar adenocarcinoma requires exclusion of metastatic colorectal carcinoma; CDX2/CK20/CK7 patterns aid. (dellino2022“intestinaltype”vulvaradenocarcinoma pages 1-2)
- EMPD secondary disease exclusion can use CDX-2 and uroplakin-III (and other panels) to rule out colorectal/urothelial origins. (iacobone2023tipsandtricks pages 9-10)

### 10.2 Imaging and staging
**FIGO 2021 staging table (visual evidence):** see Table 1 image (ha2024imaginginvulval media 862afa93).

**Imaging recommendations by stage (guideline-synthesis):**
- No routine imaging for clinically FIGO **stage IA**. (ha2024imaginginvulval pages 2-4)
- **Pelvic MRI** for local staging in tumors with invasion >1 mm, larger size (e.g., >4 cm), or suspected extension to urethra/vagina/anus. (ha2024imaginginvulval pages 2-4)
- For advanced or metastatic disease: **CT chest/abdomen/pelvis or FDG-PET/CT**. (ha2024imaginginvulval pages 2-4)

**Imaging performance statistics (vulvar cancer literature; mostly SCC but used clinically across histologies):**
- MRI nodal sensitivity highly variable (≈40–52% up to 86–89%), specificity generally high (≈82–100%). CT sensitivity low (≈43–58%). (ha2024imaginginvulval pages 4-5)
- Meta-analysis referenced in imaging review: PET/CT per-patient sensitivity 70%, specificity 90%. (ha2024imaginginvulval pages 5-7)
- Vulvoscopy diagnostic metrics in a 2024 overview: sensitivity 98%, specificity 40%, NPV 98% for malignant lesions. (corte2024currentpreoperativemanagement pages 1-2)

---

## 11. Outcome/Prognosis

### 11.1 EMPD outcomes
- In a 94-woman vulvar EMPD cohort: **5-year OS 90.5% (95% CI 81.8–95.1%)**, persistence/recurrence **86%**, median 2 surgeries (0–11). (iacobone2023tipsandtricks pages 2-4)

### 11.2 Nodal status prognostic impact (vulvar cancer overall)
- 2-year disease-free survival reported as **88%** (node-negative) vs **60% / 43% / 29%** for 1 / 2 / >2 positive nodes, respectively. (ha2024imaginginvulval pages 1-2)

### 11.3 Bartholin gland carcinoma outcomes
- In a 13-case cohort: 9 (75%) disease-free at mean follow-up 53.7 months; 3 recurrences; 2 disease-specific deaths among those with recurrence, including the adenocarcinoma case. (nazeran2019bartholinglandcarcinoma pages 1-2)

### 11.4 Metastatic vulvar cancer (SEER)
- Chemoradiotherapy associated with improved OS vs radiotherapy alone in propensity-matched cohort (HR **0.7367**, 95% CI 0.5906–0.9190; P=0.0049). (meng2024overallsurvivalassociated pages 1-2)

---

## 12. Treatment

### 12.1 Guideline-based management framework (vulvar cancer overall; rare histologies acknowledged)
NCCN v3.2024 provides stage-based management for vulvar cancer and explicitly includes rare histologies such as **extramammary Paget’s disease** and **Bartholin gland adenocarcinoma** in its scope of “rarer histologies”. (aburustum2024vulvarcancerversion pages 1-2)

### 12.2 Subtype-oriented treatments and real-world implementations

**A. EMPD (including noninvasive disease) — local and topical treatments**
- In practice, surgery is common (92/94 in one cohort), and relapse management includes topical imiquimod (63%), photodynamic therapy (5%), and radiotherapy (12%). (iacobone2023tipsandtricks pages 2-4, iacobone2023tipsandtricks pages 4-6)

**B. HER2-directed systemic therapy for metastatic EMPD**
- A WGS case report described rapid response to paclitaxel plus trastuzumab in HER2+ de novo metastatic EMPD. (lim2024wholegenomesequencing pages 2-4)

**C. Bartholin gland carcinoma/adenocarcinoma**
- Management is often extrapolated from vulvar cancer; experts emphasize molecular profiling (DNA panels with CNV, RNA fusions, MSI/TMB/PD-L1) to reduce misclassification and enable targeted/immunotherapy in advanced disease. (kostov2025bartholinglandcarcinoma pages 20-21)

### 12.3 Clinical trials (selected; real-world implementability)

**Topical imiquimod trials (noninvasive vulvar Paget/EMPD):**
- **NCT02385188** (Phase 3; completed; n=25): topical 5% imiquimod 3×/week for 16 weeks; primary endpoint clinical response 12 weeks after end of treatment; includes QoL instruments (EQ-5D, DLQI, FSDS). (NCT02385188 chunk 1)
- **NCT00504023** (pilot; completed; n=8): imiquimod 3×/week up to 12 weeks; biopsies at baseline and 12 weeks; follow-up every 3 months for ≥2 years. (NCT00504023 chunk 1)

**Photodynamic therapy device trial:**
- **NCT03713203** (Phase II; recruiting; n=24): PAGETEX® device with Metvixia; 2–4 PDT sessions; primary endpoint disease control rate at 3 months; excludes invasive disease/underlying adenocarcinoma. (NCT03713203 chunk 1)

**Systemic/advanced vulvar cancer trial example:**
- **NCT03452332** (Phase 1; completed): SBRT + tremelimumab + durvalumab in recurrent/metastatic cervical/vaginal/vulvar cancers. (trial record retrieved but not evidence-extracted in provided snippets; use cautiously)

### 12.4 MAXO term suggestions (examples)
- Surgical excision/vulvectomy: **MAXO: surgical excision** (generic)
- Radiotherapy: **MAXO: radiotherapy**
- Chemotherapy (platinum/taxane): **MAXO: chemotherapy**
- HER2-directed therapy (trastuzumab): **MAXO: targeted therapy** / **monoclonal antibody therapy**
- Topical imiquimod: **MAXO: topical immunotherapy**
- Photodynamic therapy: **MAXO: photodynamic therapy**

---

## 13. Prevention

- **Risk factor modification (general vulvar cancer):** NCCN identifies smoking, HPV, inflammatory vulvar conditions, and immunodeficiency as risk factors; these support prevention via smoking cessation, HPV prevention/control, and treatment of chronic vulvar inflammatory disease, although explicit preventive recommendations were not present in the retrieved NCCN excerpt. (aburustum2024vulvarcancerversion pages 1-2)
- **Secondary prevention:** early biopsy of suspicious vulvar lesions and careful evaluation of VIN/lichen sclerosus are emphasized in diagnostic reviews; brush cytology is investigated as triage for VIN but biopsy remains gold standard. (kesic2022earlydiagnosticsof pages 1-2)

Evidence gap: explicit HPV vaccination impact on vulvar adenocarcinoma or adenocarcinoma-specific prevention strategies were not retrieved.

---

## 14. Other Species / Natural Disease
No evidence identified in retrieved sources.

---

## 15. Model Organisms
A trastuzumab-resistant EMPD model is reported with PTEN loss as a potential resistance mechanism (supporting mechanistic research and therapy optimization), but detailed model description was not extracted in current evidence snippets. (dellino2022“intestinaltype”vulvaradenocarcinoma pages 1-2, lim2024wholegenomesequencing pages 1-2)

---

## Key Recent Developments (prioritizing 2023–2024)
1. **NCCN Vulvar Cancer v3.2024** explicitly contextualizes rarer histologies including Bartholin gland adenocarcinoma and EMPD within a unified management framework and lists key risk factors. Publication: **Mar 2024**; URL: https://doi.org/10.6004/jnccn.2024.0013 (aburustum2024vulvarcancerversion pages 1-2)
2. **Imaging and FIGO 2021 staging implementation (2024)**: staging applicability to non-melanoma vulvar cancers and imaging recommendations by stage; provides pooled PET/CT performance and highlights limitations. Publication: **Jun 2024**; URL: https://doi.org/10.3390/cancers16122269 (ha2024imaginginvulval pages 1-2, ha2024imaginginvulval pages 2-4, ha2024imaginginvulval pages 5-7, ha2024imaginginvulval media 862afa93)
3. **Genomics-enabled precision approaches in EMPD (2024):** WGS of HER2+ metastatic EMPD documents CNV landscape, pathway enrichment (FGFR1/TGFβ), and clinical response to HER2-directed therapy combined with chemotherapy. Publication: **Jun 2024**; URL: https://doi.org/10.1186/s13023-024-03169-y (lim2024wholegenomesequencing pages 2-4, lim2024wholegenomesequencing pages 1-2)
4. **Refined long-term surveillance concept for vulvar EMPD (2023):** referral-center data quantify recurrence and late cervico-vaginal involvement; supports lifelong follow-up and cytology/biopsy-based detection. Publication: **Jan 2023**; URL: https://doi.org/10.3390/diagnostics13030464 (iacobone2023tipsandtricks pages 2-4, iacobone2023tipsandtricks pages 1-2)

---

## Summary Table (Subtype comparison)
| Entity/subtype | Key definition/notes | Typical age/presentation | Key diagnostic IHC/biomarkers | Key management | Key quantitative outcomes/statistics | Key citations |
|---|---|---|---|---|---|---|
| Invasive extramammary Paget disease (EMPD) / Paget-associated vulvar adenocarcinoma | Primary vulvar EMPD is classified as cutaneous-origin disease; Wilkinson/Brown subtypes include type 1a (intraepithelial), 1b (stromal invasion), and 1c (manifestation of primary vulvar adenocarcinoma). Paget-associated invasive adenocarcinoma can show strong HER2 expression. | Mean age 63.3 years (range 31–88) in a 94-patient vulvar EMPD cohort; lesions may recur/persist and cervico-vaginal spread can be clinically silent, often first detected by abnormal glandular cytology. | HER2 overexpression reported in Paget-associated vulvar adenocarcinoma; cervical/vaginal involvement diagnosis used cytology with immunocytochemistry plus biopsy confirmation of Paget cells. | Surgery is mainstay; recurrent/persistent disease may also be treated with topical imiquimod, photodynamic therapy, or radiotherapy; lifelong surveillance is important, including annual cervical/vaginal assessment in long-standing disease. | In 94 women: 81% type 1a; invasive EMPD in 36%; persistence/recurrence 86%; median 2 surgeries (range 0–11); 5-year OS 90.5% (95% CI 81.8–95.1%). Cervico-vaginal involvement cumulative incidence 2.5% at 5 years, 6.5% at 10 years, 14.0% at 15 years. (iacobone2023tipsandtricks pages 2-4, aburustum2024vulvarcancerversion pages 1-2) | (iacobone2023tipsandtricks pages 2-4, aburustum2024vulvarcancerversion pages 1-2) |
| Intestinal-type vulvar adenocarcinoma (primary villo-glandular mucinous adenocarcinoma with intestinal differentiation) | Extremely rare primary vulvar adenocarcinoma; WHO 2020 describes this as primary villo-glandular mucinous adenocarcinoma with intestinal differentiation and discourages “cloacogenic” terminology. Histology resembles mucinous colorectal carcinoma with villo-glandular architecture, goblet/Paneth cells, and mucin. Must exclude metastatic gastrointestinal primary. | Median age 58 years; reported range 31–92 years; commonly arises in labia/perineal or posterior vulvar structures and may mimic benign lesions. | Intestinal phenotype with CK20 and CDX2 positivity, often CEA positive and variable CK7/p16; diagnosis requires radiologic/clinical exclusion of another primary site. | Surgical excision with tumor-free margins is standard; lymph-node staging is considered/recommended especially for tumors >2 cm or when imaging suggests nodal disease; adjuvant or systemic therapy reported in selected advanced/recurrent cases. | 2022 review found 29 cases; 2025 review found 40 cases overall (41 including authors’ case in another excerpt). Nodal metastases in ~31.2%–31.5%; mortality due to disease about 10%; FIGO stage IA most frequent at diagnosis. (dellino2022“intestinaltype”vulvaradenocarcinoma pages 2-5, dellino2022“intestinaltype”vulvaradenocarcinoma pages 1-2, colalillo2025intestinaltypeadenocarcinomais pages 11-13, colalillo2025intestinaltypeadenocarcinomais pages 1-2, colalillo2025intestinaltypeadenocarcinomais pages 10-11) | (dellino2022“intestinaltype”vulvaradenocarcinoma pages 2-5, dellino2022“intestinaltype”vulvaradenocarcinoma pages 1-2, colalillo2025intestinaltypeadenocarcinomais pages 11-13, colalillo2025intestinaltypeadenocarcinomais pages 1-2, colalillo2025intestinaltypeadenocarcinomais pages 10-11) |
| Vulvar adenocarcinoma of mammary gland type / mammary-like glands | Extremely rare adenocarcinoma thought to arise from mammary-like vulvar glands; pathology can resemble invasive ductal breast carcinoma, and breast primary must be excluded clinically/radiologically. | Postmenopausal presentation in reported cases; may present as vulvar mass/lump. | Strong ER positivity reported in 90%–100%; CK7, CAM5.2, GATA3 positive; typically negative for PR, GCDFP-15, SOX10, p63, CK20. HER2 may be equivocal (2+) with negative FISH in a reported case. | Radical vulvectomy or radical local excision; nodal assessment by sentinel lymph node biopsy or lymphadenectomy; adjuvant therapy tailored to IHC profile and stage. | Evidence base is limited to case reports/small series; quantitative outcome estimates are not established in the gathered evidence. (morais2022diagnosisandmanagement pages 1-2) | (morais2022diagnosisandmanagement pages 1-2) |
| Bartholin gland adenocarcinoma / Bartholin gland carcinoma (general, including adenocarcinoma subtype) | Rare vulvar cancer arising in the Bartholin gland region; adenocarcinoma is one of the three most common Bartholin gland carcinoma histotypes. Diagnosis requires compatible location/histology and exclusion of another primary; many cases are initially mistaken for benign Bartholin cyst/abscess. | Often presents as a solid, persistent, or recurrent Bartholin-region mass; delayed diagnosis is common, prompting low threshold for biopsy in women aged ≥40–45 years. | Suggested histotype-specific markers include CK20/CDX2/SATB2 for intestinal-type adenocarcinoma; HPV/p16/p53, MYB/MYBL1 fusions (for adenoid cystic carcinoma), and broader molecular testing (MMR/MSI, TMB, PD-L1, targeted DNA/RNA assays) are proposed in modern workup. | Complete surgical excision with 2–3 mm margins and bilateral groin evaluation; adjuvant therapy tailored by histology; advanced disease may receive radiotherapy ± chemotherapy, systemic therapy, immunotherapy, or targeted agents; management largely extrapolated from general vulvar cancer guidelines. | BGC comprises 3%–7% of vulvar cancers and <1% of gynecologic tumors; ~50% diagnosed at advanced stage; nodal metastasis occurs in >40%; adenocarcinoma histology and node-positive disease predict worse survival. (kostov2025bartholinglandcarcinoma pages 24-25, kostov2025bartholinglandcarcinoma pages 20-21, faruqi2018standardsanddatasets pages 12-16, aburustum2024vulvarcancerversion pages 1-2) | (kostov2025bartholinglandcarcinoma pages 24-25, kostov2025bartholinglandcarcinoma pages 20-21, faruqi2018standardsanddatasets pages 12-16, aburustum2024vulvarcancerversion pages 1-2) |


*Table: This table compares the main vulvar adenocarcinoma-related entities identified in the gathered evidence, emphasizing diagnostic markers, management patterns, and quantitative outcomes. It is useful for quickly distinguishing subtype-specific features while keeping evidence provenance explicit through context-ID citations.*

---

## Visual Evidence: FIGO 2021 staging
The FIGO 2021 staging table for vulvar carcinoma (applies to all morphologic types except melanoma) is shown in the extracted Table 1 image. (ha2024imaginginvulval media 862afa93)

---

## Limitations and Data Gaps
- **Ontology IDs (MONDO/MeSH/Orphanet/OMIM):** Not retrievable from current tool outputs for “vulvar adenocarcinoma” and will need direct ontology database lookup outside this toolchain.
- **Adenocarcinoma-specific population incidence/survival:** Most quantitative epidemiology is for vulvar cancer overall or for specific rare entities (EMPD, Bartholin cohorts, VAIt systematic reviews). Large 2023–2024 population studies stratified by vulvar adenocarcinoma subtypes were not available in retrieved evidence.
- **Genetic predisposition and protective factors:** Not identified in retrieved sources.



References

1. (aburustum2024vulvarcancerversion pages 1-2): Nadeem R. Abu-Rustum, Catheryn M. Yashar, Rebecca Arend, Emma Barber, Kristin Bradley, Rebecca Brooks, Susana M. Campos, Junzo Chino, Hye Sook Chon, Marta Ann Crispens, Shari Damast, Christine M. Fisher, Peter Frederick, David K. Gaffney, Stephanie Gaillard, Robert Giuntoli, Scott Glaser, Jordan Holmes, Brooke E. Howitt, Kari Kendra, Jayanthi Lea, Nita Lee, Gina Mantia-Smaldone, Andrea Mariani, David Mutch, Christa Nagel, Larissa Nekhlyudov, Mirna Podoll, Kerry Rodabaugh, Ritu Salani, John Schorge, Jean Siedel, Rachel Sisodia, Pamela Soliman, Stefanie Ueda, Renata Urban, Stephanie L. Wethington, Emily Wyse, Kristine Zanotti, Nicole McMillian, and Sara Espinosa. Vulvar cancer, version 3.2024, nccn clinical practice guidelines in oncology. Journal of the National Comprehensive Cancer Network : JNCCN, 22 2:117-135, Mar 2024. URL: https://doi.org/10.6004/jnccn.2024.0013, doi:10.6004/jnccn.2024.0013. This article has 88 citations.

2. (ha2024imaginginvulval pages 1-2): Minah Ha and Lois Eva. Imaging in vulval cancer. Cancers, 16:2269, Jun 2024. URL: https://doi.org/10.3390/cancers16122269, doi:10.3390/cancers16122269. This article has 5 citations.

3. (muigai2018potentialdelayin pages 1-2): Jennifer Muigai, Louis Jacob, Konstantinos Dinas, Karel Kostev, and Matthias Kalder. Potential delay in the diagnosis of vulvar cancer and associated risk factors in women treated in german gynecological practices. Oncotarget, 9:8725-8730, Jan 2018. URL: https://doi.org/10.18632/oncotarget.23848, doi:10.18632/oncotarget.23848. This article has 45 citations.

4. (ha2024imaginginvulval media 862afa93): Minah Ha and Lois Eva. Imaging in vulval cancer. Cancers, 16:2269, Jun 2024. URL: https://doi.org/10.3390/cancers16122269, doi:10.3390/cancers16122269. This article has 5 citations.

5. (faruqi2018standardsanddatasets pages 12-16): A Faruqi and B Rous. Standards and datasets for reporting cancers. Unknown journal, 2018.

6. (dellino2022“intestinaltype”vulvaradenocarcinoma pages 1-2): Miriam Dellino, Stefania Cicogna, Francesca Falcone, Marco Mitidieri, Roberta Mazzeo, Sandro Pignata, Giorgia Mangili, and Gennaro Cormio. “intestinal-type” vulvar adenocarcinoma: a review of the mito rare tumors group. Cancers, 14:5171, Oct 2022. URL: https://doi.org/10.3390/cancers14205171, doi:10.3390/cancers14205171. This article has 9 citations.

7. (morais2022diagnosisandmanagement pages 1-2): Mariana Morais, Joao Vaz Silva, and Mariana Vide Tavares. Diagnosis and management of primary vulvar adenocarcinoma of mammary gland type: report of two distinct cases. BMJ Case Reports, 15:e245580, Jun 2022. URL: https://doi.org/10.1136/bcr-2021-245580, doi:10.1136/bcr-2021-245580. This article has 15 citations and is from a peer-reviewed journal.

8. (iacobone2023tipsandtricks pages 2-4): Anna Daniela Iacobone, Maria Elena Guerrieri, Eleonora Petra Preti, Noemi Spolti, Gianluigi Radici, Giulia Peveri, Vincenzo Bagnardi, Giulio Tosti, Angelo Maggioni, Fabio Bottari, Chiara Scacchi, and Mariacristina Ghioni. Tips and tricks for early diagnosis of cervico-vaginal involvement from extramammary paget’s disease of the vulva: a referral center experience. Diagnostics, 13:464, Jan 2023. URL: https://doi.org/10.3390/diagnostics13030464, doi:10.3390/diagnostics13030464. This article has 3 citations.

9. (meng2024overallsurvivalassociated pages 1-2): Xiaolin Meng, Shuaiqingying Guo, Xue Feng, Jihui Ai, and Jie Yang. Overall survival associated with surgery, radiotherapy, and chemotherapy in metastatic vulvar cancer: a retrospective cohort study based on the seer database. Cancer Pathogenesis and Therapy, 2:195-204, Jul 2024. URL: https://doi.org/10.1016/j.cpt.2023.08.003, doi:10.1016/j.cpt.2023.08.003. This article has 6 citations.

10. (nazeran2019bartholinglandcarcinoma pages 1-2): Tayyebeh Nazeran, Angela S. Cheng, Anthony N. Karnezis, Anna V. Tinker, and C. Blake Gilks. Bartholin gland carcinoma: clinicopathologic features, including p16 expression and clinical outcome. International Journal of Gynecological Pathology, 38:189-195, Mar 2019. URL: https://doi.org/10.1097/pgp.0000000000000489, doi:10.1097/pgp.0000000000000489. This article has 40 citations and is from a peer-reviewed journal.

11. (lim2024wholegenomesequencing pages 1-2): Boon Yee Lim, Zexi Guo, Jing Quan Lim, Tun Kiat Ko, Elizabeth Chun Yong Lee, Bavani Kannan, Jing Yi Lee, Abner Herbert Lim, Zhimei Li, Cedric Chuan-Young Ng, Inny Busmanis, and Jason Yongsheng Chan. Whole genome sequencing of her2-positive metastatic extramammary paget’s disease: a case report. Orphanet Journal of Rare Diseases, Jun 2024. URL: https://doi.org/10.1186/s13023-024-03169-y, doi:10.1186/s13023-024-03169-y. This article has 1 citations and is from a peer-reviewed journal.

12. (dellino2022“intestinaltype”vulvaradenocarcinoma pages 5-6): Miriam Dellino, Stefania Cicogna, Francesca Falcone, Marco Mitidieri, Roberta Mazzeo, Sandro Pignata, Giorgia Mangili, and Gennaro Cormio. “intestinal-type” vulvar adenocarcinoma: a review of the mito rare tumors group. Cancers, 14:5171, Oct 2022. URL: https://doi.org/10.3390/cancers14205171, doi:10.3390/cancers14205171. This article has 9 citations.

13. (ayalapeacock2025advancesinvulvar pages 1-3): Diandra N. Ayala-Peacock and Manjeet Chadha. Advances in vulvar cancer: a radiation oncology perspective. Cancers, 17:2415, Jul 2025. URL: https://doi.org/10.3390/cancers17152415, doi:10.3390/cancers17152415. This article has 1 citations.

14. (iacobone2023tipsandtricks pages 1-2): Anna Daniela Iacobone, Maria Elena Guerrieri, Eleonora Petra Preti, Noemi Spolti, Gianluigi Radici, Giulia Peveri, Vincenzo Bagnardi, Giulio Tosti, Angelo Maggioni, Fabio Bottari, Chiara Scacchi, and Mariacristina Ghioni. Tips and tricks for early diagnosis of cervico-vaginal involvement from extramammary paget’s disease of the vulva: a referral center experience. Diagnostics, 13:464, Jan 2023. URL: https://doi.org/10.3390/diagnostics13030464, doi:10.3390/diagnostics13030464. This article has 3 citations.

15. (kostov2025bartholinglandcarcinoma pages 20-21): Stoyan Kostov, Yavor Kornovski, Vesela Ivanova, Dimitar Metodiev, Angel Yordanov, Stanislav Slavchev, Yonka Ivanova, Anke Seidel, Ingolf Juhasz-Böss, Ihsan Hasan, Ibrahim Alkatout, and Rafał Watrowski. Bartholin gland carcinoma: a state-of-the-art review of epidemiology, histopathology, molecular testing, and clinical management. Cancers, 17:3819, Nov 2025. URL: https://doi.org/10.3390/cancers17233819, doi:10.3390/cancers17233819. This article has 2 citations.

16. (colalillo2025intestinaltypeadenocarcinomais pages 11-13): Alessio Colalillo, Dominga Boccia, Luigi Della Corte, Daniele Neola, Federica Rosato, Silvia D’Ippolito, Maria De Ninno, Damiano Arciuolo, Maurizio Guida, Giuseppe Bifulco, and Francesco Cosentino. Intestinal-type adenocarcinoma is a rare histotype of vulvar neoplasm: systematic review of the literature. Cancers, 17:3989, Dec 2025. URL: https://doi.org/10.3390/cancers17243989, doi:10.3390/cancers17243989. This article has 0 citations.

17. (lim2024wholegenomesequencing pages 2-4): Boon Yee Lim, Zexi Guo, Jing Quan Lim, Tun Kiat Ko, Elizabeth Chun Yong Lee, Bavani Kannan, Jing Yi Lee, Abner Herbert Lim, Zhimei Li, Cedric Chuan-Young Ng, Inny Busmanis, and Jason Yongsheng Chan. Whole genome sequencing of her2-positive metastatic extramammary paget’s disease: a case report. Orphanet Journal of Rare Diseases, Jun 2024. URL: https://doi.org/10.1186/s13023-024-03169-y, doi:10.1186/s13023-024-03169-y. This article has 1 citations and is from a peer-reviewed journal.

18. (dellino2022“intestinaltype”vulvaradenocarcinoma pages 9-10): Miriam Dellino, Stefania Cicogna, Francesca Falcone, Marco Mitidieri, Roberta Mazzeo, Sandro Pignata, Giorgia Mangili, and Gennaro Cormio. “intestinal-type” vulvar adenocarcinoma: a review of the mito rare tumors group. Cancers, 14:5171, Oct 2022. URL: https://doi.org/10.3390/cancers14205171, doi:10.3390/cancers14205171. This article has 9 citations.

19. (iacobone2023tipsandtricks pages 6-9): Anna Daniela Iacobone, Maria Elena Guerrieri, Eleonora Petra Preti, Noemi Spolti, Gianluigi Radici, Giulia Peveri, Vincenzo Bagnardi, Giulio Tosti, Angelo Maggioni, Fabio Bottari, Chiara Scacchi, and Mariacristina Ghioni. Tips and tricks for early diagnosis of cervico-vaginal involvement from extramammary paget’s disease of the vulva: a referral center experience. Diagnostics, 13:464, Jan 2023. URL: https://doi.org/10.3390/diagnostics13030464, doi:10.3390/diagnostics13030464. This article has 3 citations.

20. (corte2024currentpreoperativemanagement pages 1-2): Luigi Della Corte, Valeria Cafasso, Maria Chiara Guarino, Giuseppe Gullo, Gaspare Cucinella, Alessandra Lopez, Simona Zaami, Gaetano Riemma, Pierluigi Giampaolino, and Giuseppe Bifulco. Current preoperative management of vulvar squamous cell carcinoma: an overview. Cancers, 16:1846, May 2024. URL: https://doi.org/10.3390/cancers16101846, doi:10.3390/cancers16101846. This article has 12 citations.

21. (kesic2022earlydiagnosticsof pages 1-2): Vesna Kesić, Pedro Vieira-Baptista, and Colleen K. Stockdale. Early diagnostics of vulvar intraepithelial neoplasia. Cancers, 14:1822, Apr 2022. URL: https://doi.org/10.3390/cancers14071822, doi:10.3390/cancers14071822. This article has 38 citations.

22. (iacobone2023tipsandtricks pages 9-10): Anna Daniela Iacobone, Maria Elena Guerrieri, Eleonora Petra Preti, Noemi Spolti, Gianluigi Radici, Giulia Peveri, Vincenzo Bagnardi, Giulio Tosti, Angelo Maggioni, Fabio Bottari, Chiara Scacchi, and Mariacristina Ghioni. Tips and tricks for early diagnosis of cervico-vaginal involvement from extramammary paget’s disease of the vulva: a referral center experience. Diagnostics, 13:464, Jan 2023. URL: https://doi.org/10.3390/diagnostics13030464, doi:10.3390/diagnostics13030464. This article has 3 citations.

23. (ha2024imaginginvulval pages 2-4): Minah Ha and Lois Eva. Imaging in vulval cancer. Cancers, 16:2269, Jun 2024. URL: https://doi.org/10.3390/cancers16122269, doi:10.3390/cancers16122269. This article has 5 citations.

24. (ha2024imaginginvulval pages 4-5): Minah Ha and Lois Eva. Imaging in vulval cancer. Cancers, 16:2269, Jun 2024. URL: https://doi.org/10.3390/cancers16122269, doi:10.3390/cancers16122269. This article has 5 citations.

25. (ha2024imaginginvulval pages 5-7): Minah Ha and Lois Eva. Imaging in vulval cancer. Cancers, 16:2269, Jun 2024. URL: https://doi.org/10.3390/cancers16122269, doi:10.3390/cancers16122269. This article has 5 citations.

26. (iacobone2023tipsandtricks pages 4-6): Anna Daniela Iacobone, Maria Elena Guerrieri, Eleonora Petra Preti, Noemi Spolti, Gianluigi Radici, Giulia Peveri, Vincenzo Bagnardi, Giulio Tosti, Angelo Maggioni, Fabio Bottari, Chiara Scacchi, and Mariacristina Ghioni. Tips and tricks for early diagnosis of cervico-vaginal involvement from extramammary paget’s disease of the vulva: a referral center experience. Diagnostics, 13:464, Jan 2023. URL: https://doi.org/10.3390/diagnostics13030464, doi:10.3390/diagnostics13030464. This article has 3 citations.

27. (NCT02385188 chunk 1): Joanne A. de Hullu, MD, PhD. Topical 5% Imiquimod Cream for Vulvar Paget's Disease. University Medical Center Nijmegen. 2015. ClinicalTrials.gov Identifier: NCT02385188

28. (NCT00504023 chunk 1):  Topical Imiquimod in Treating Patients With Recurrent Paget's Disease of the Vulva. Memorial Sloan Kettering Cancer Center. 2007. ClinicalTrials.gov Identifier: NCT00504023

29. (NCT03713203 chunk 1):  PAGETEX® Photodynamic Therapy Device for the Treatment of Extra Mammary Paget's Disease of the Vulva (EMPV).. University Hospital, Lille. 2019. ClinicalTrials.gov Identifier: NCT03713203

30. (dellino2022“intestinaltype”vulvaradenocarcinoma pages 2-5): Miriam Dellino, Stefania Cicogna, Francesca Falcone, Marco Mitidieri, Roberta Mazzeo, Sandro Pignata, Giorgia Mangili, and Gennaro Cormio. “intestinal-type” vulvar adenocarcinoma: a review of the mito rare tumors group. Cancers, 14:5171, Oct 2022. URL: https://doi.org/10.3390/cancers14205171, doi:10.3390/cancers14205171. This article has 9 citations.

31. (colalillo2025intestinaltypeadenocarcinomais pages 1-2): Alessio Colalillo, Dominga Boccia, Luigi Della Corte, Daniele Neola, Federica Rosato, Silvia D’Ippolito, Maria De Ninno, Damiano Arciuolo, Maurizio Guida, Giuseppe Bifulco, and Francesco Cosentino. Intestinal-type adenocarcinoma is a rare histotype of vulvar neoplasm: systematic review of the literature. Cancers, 17:3989, Dec 2025. URL: https://doi.org/10.3390/cancers17243989, doi:10.3390/cancers17243989. This article has 0 citations.

32. (colalillo2025intestinaltypeadenocarcinomais pages 10-11): Alessio Colalillo, Dominga Boccia, Luigi Della Corte, Daniele Neola, Federica Rosato, Silvia D’Ippolito, Maria De Ninno, Damiano Arciuolo, Maurizio Guida, Giuseppe Bifulco, and Francesco Cosentino. Intestinal-type adenocarcinoma is a rare histotype of vulvar neoplasm: systematic review of the literature. Cancers, 17:3989, Dec 2025. URL: https://doi.org/10.3390/cancers17243989, doi:10.3390/cancers17243989. This article has 0 citations.

33. (kostov2025bartholinglandcarcinoma pages 24-25): Stoyan Kostov, Yavor Kornovski, Vesela Ivanova, Dimitar Metodiev, Angel Yordanov, Stanislav Slavchev, Yonka Ivanova, Anke Seidel, Ingolf Juhasz-Böss, Ihsan Hasan, Ibrahim Alkatout, and Rafał Watrowski. Bartholin gland carcinoma: a state-of-the-art review of epidemiology, histopathology, molecular testing, and clinical management. Cancers, 17:3819, Nov 2025. URL: https://doi.org/10.3390/cancers17233819, doi:10.3390/cancers17233819. This article has 2 citations.