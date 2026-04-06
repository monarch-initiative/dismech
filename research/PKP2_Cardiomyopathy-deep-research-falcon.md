---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-04T12:24:59.317043'
end_time: '2026-04-04T12:37:12.791682'
duration_seconds: 733.47
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: PKP2 Cardiomyopathy
  mondo_id: ''
  category: Genetic
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 52
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** PKP2 Cardiomyopathy
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **PKP2 Cardiomyopathy** covering all of the
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
- **Disease Name:** PKP2 Cardiomyopathy
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **PKP2 Cardiomyopathy** covering all of the
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


# PKP2 Cardiomyopathy (PKP2-ACM): Comprehensive Disease Characteristics Report

## Executive summary
PKP2 cardiomyopathy refers to **arrhythmogenic cardiomyopathy (ACM)** driven by pathogenic variants in **PKP2 (plakophilin-2)**, the most commonly implicated desmosomal gene in classical right-dominant ACM/ARVC. Disease is characterized by ventricular arrhythmias and progressive fibro-fatty myocardial replacement, with **highly variable penetrance** influenced by sex and environmental factors (notably endurance/competitive exercise). 2023–2024 research emphasizes (i) refined phenotyping by CMR/strain/ECG, (ii) immune, metabolic, and mechanotransduction pathways beyond “desmosome failure,” and (iii) rapid translation of **AAV-mediated PKP2 gene replacement** from preclinical studies into **first-in-human phase 1/2 trials**. (pilichou2016arrhythmogeniccardiomyopathy pages 1-2, bos2023thearrhythmogeniccardiomyopathy pages 4-6, chua2023understandingarrhythmogeniccardiomyopathy pages 6-8, mundisugih2024exploringthetherapeutic pages 2-4, NCT06976606 chunk 1)

---

## 1. Disease information
### 1.1 What is PKP2 cardiomyopathy?
Arrhythmogenic cardiomyopathy is a heart-muscle disease clinically characterized by life-threatening ventricular arrhythmias and pathologically by progressive dystrophy of ventricular myocardium with **fibro-fatty replacement**. (pilichou2016arrhythmogeniccardiomyopathy pages 1-2)

**Abstract quote (disease definition):** “Arrhythmogenic cardiomyopathy (AC) is a heart muscle disease clinically characterized by life-threatening ventricular arrhythmias and pathologically by an acquired and progressive dystrophy of the ventricular myocardium with fibro-fatty replacement.” (Pilichou et al., 2016) (pilichou2016arrhythmogeniccardiomyopathy pages 1-2)

PKP2 cardiomyopathy (often termed **PKP2-ACM**) is the desmosomal ACM subtype caused by pathogenic **PKP2** variants, typically with right-ventricular predominance but with clinically relevant left-ventricular involvement in a subset. (bos2023thearrhythmogeniccardiomyopathy pages 1-3, bos2023thearrhythmogeniccardiomyopathy pages 4-6)

### 1.2 Key identifiers
* **Orphanet**: Arrhythmogenic cardiomyopathy **ORPHA:247** (Pilichou et al., 2016; published 2016-04; https://doi.org/10.1186/s13023-016-0407-1) (pilichou2016arrhythmogeniccardiomyopathy pages 2-3)
* **OMIM**: Arrhythmogenic cardiomyopathy **OMIM #107970** (Pilichou et al., 2016) (pilichou2016arrhythmogeniccardiomyopathy pages 2-3)
* **MONDO / ICD-10/ICD-11 / MeSH**: Not reliably extractable from the retrieved primary sources in this tool run; these identifiers should be mapped via MONDO/ICD/MeSH registries directly (not inferred here).

### 1.3 Synonyms / alternative names
* Arrhythmogenic cardiomyopathy (ACM) (pilichou2016arrhythmogeniccardiomyopathy pages 1-2)
* Arrhythmogenic right ventricular cardiomyopathy/dysplasia (ARVC/ARVD) (pilichou2016arrhythmogeniccardiomyopathy pages 3-5)
* **PKP2-associated ARVC**, **PKP2-ACM**, **desmosome-related ACM (dACM)** (chua2023understandingarrhythmogeniccardiomyopathy pages 31-33, opbergen2024aavmediateddeliveryof pages 7-9)

### 1.4 Evidence sources represented in this report
* Aggregated disease-level resources/reviews: 2016 ACM review (Pilichou et al.) and 2023–2024 reviews (Chua 2023; Vencato 2024; Mundisugih 2024). (pilichou2016arrhythmogeniccardiomyopathy pages 1-2, chua2023understandingarrhythmogeniccardiomyopathy pages 17-19, vencato2024animalmodelsand pages 5-7, mundisugih2024exploringthetherapeutic pages 2-4)
* Human cohort and case evidence: PKP2 founder-variant cohort (Bos 2023), tertiary clinic cohort (Aljehani 2023), PKP2 case report/review (Casian 2024), founder families (Robles‑Mezcua 2023), population biobank analysis (Hylind 2022). (bos2023thearrhythmogeniccardiomyopathy pages 4-6, aljehani2023characterisationofpatients pages 1-2, casian2024arrhythmogenicrightventricular pages 9-10, roblesmezcua2023thenovelvariant pages 6-9, hylind2022populationprevalenceof pages 5-7)
* Model systems: hiPSC-CM/engineered myocardium and animal models (mouse; guinea pig). (chua2023understandingarrhythmogeniccardiomyopathy pages 17-19, kyriakopoulou2023therapeuticefficacyof pages 1-2, wu2024aav9pkp2improvesheart pages 13-14, song2024multiomicsanalysisreveals pages 1-5)

---

## 2. Etiology
### 2.1 Disease causal factors
**Primary cause:** germline pathogenic variants in **PKP2**, which encodes plakophilin-2, an intercalated disc/desmosome component critical for cardiomyocyte mechanical and electrical coupling. Mechanism is frequently consistent with **haploinsufficiency** for truncating/splice variants. (hylind2022populationprevalenceof pages 5-7, vencato2024animalmodelsand pages 2-4)

### 2.2 Risk factors
#### Genetic risk factors
* **Pathogenic/likely pathogenic PKP2 variants** (commonly truncating/splice) are a major cause of desmosomal ACM. (biernacka2021pathogenicvariantsin pages 1-2, bos2023thearrhythmogeniccardiomyopathy pages 4-6)
* Compound/digenic heterozygosity in desmosomal disease is reported in ACM more broadly and is posited to contribute to phenotypic variability. (pilichou2016arrhythmogeniccardiomyopathy pages 1-2)

#### Environmental and demographic risk factors
* **Endurance/competitive exercise** is a strong environmental risk factor and is linked to earlier disease onset/progression in ACM, supporting recommendations for sports restriction. (pilichou2016arrhythmogeniccardiomyopathy pages 2-3, pilichou2016arrhythmogeniccardiomyopathy pages 1-2)
* **Male sex** modifies risk in PKP2 cohorts: in PKP2 c.1211dup carriers, sustained ventricular arrhythmia by age 40 occurred in **33% of men vs 9% of women**, and HF by age 60 reached **21% in men vs 8% in women**. (bos2023thearrhythmogeniccardiomyopathy pages 4-6)

### 2.3 Protective factors
No robust protective genetic variants or protective exposures were identified in the retrieved evidence set. Observationally, many PKP2 truncating-variant carriers in population cohorts do not develop clinically manifest ARVC, implying that additional protective or countervailing factors exist but are not yet well-defined. (hylind2022populationprevalenceof pages 5-7)

### 2.4 Gene–environment interactions
A key contemporary concept is that **PKP2 loss-of-function creates susceptibility**, while environmental stressors (notably **endurance exercise**) interact with the desmosome/intercalated disc to trigger arrhythmias and structural progression. (pilichou2016arrhythmogeniccardiomyopathy pages 2-3, hylind2022populationprevalenceof pages 5-7)

---

## 3. Phenotypes (clinical features)
### 3.1 Core phenotype domains
ACM may present from a concealed phase to overt electrical disorder to RV failure and ultimately biventricular failure; **sudden death can occur at any stage**. (pilichou2016arrhythmogeniccardiomyopathy pages 3-5)

**Abstract quote (clinical variability):** “Clinically, ACM shows wide variability among patients; symptoms can include syncope and ventricular tachycardia but also sudden death, with the latter often being its sole manifestation.” (Vencato et al., 2024) (vencato2024animalmodelsand pages 5-7)

### 3.2 Quantitative phenotype statistics (key recent cohorts)
A cross-study quantitative summary is provided below.

| Study (year, journal) | Population / variant | N | Key phenotype stats | Key diagnostic findings | Notes |
|---|---:|---:|---|---|---|
| Bos et al. (2023, *Netherlands Heart Journal*) | Heterozygous **PKP2 c.1211dup (p.Val406Serfs*4)** founder-variant carriers | 106 analyzed carriers | **44%** diagnosed with ACM/ARVC at mean age **41 y**; by end of follow-up **27%** had sustained VA and **11%** developed HF; **46%** had RV dilatation/dysfunction and **37%** had some LV involvement; by age 40, sustained VA in **33% of men vs 9% of women**; HF by age 60 **21% men vs 8% women**; SCA mainly in males (7 males vs 1 female) (bos2023thearrhythmogeniccardiomyopathy pages 4-6, bos2023thearrhythmogeniccardiomyopathy pages 1-3) | Ambulatory monitoring: **34%** had PVC burden >1% (median **2.6%**); imaging showed RV involvement common, with LV LGE in ~**33%** of appropriately imaged carriers; probands vs relatives had more RV dilatation/dysfunction on CMR (e.g., RV dilatation **95% vs 38%**, RV dysfunction **89% vs 32%**) (bos2023thearrhythmogeniccardiomyopathy pages 4-6, bos2023thearrhythmogeniccardiomyopathy pages 3-4) | Typical right-dominant PKP2-ACM but with appreciable LV involvement; beta-blockers in **45%**, ICD in **33%**; ~**60%** remained asymptomatic by age 60 (bos2023thearrhythmogeniccardiomyopathy pages 4-6, bos2023thearrhythmogeniccardiomyopathy pages 1-3) |
| Hylind et al. (2022, *Circulation: Genomic and Precision Medicine*) | UK Biobank carriers of **PKP2 truncating variants (PKP2tv)** | **190** UKB carriers with PKP2tv | Manifest ARVC features in only **1.6%**; cohort mean age **57 y** vs symptomatic ARVC onset around **33 y** in clinical cohorts; very low observed disease association overall (reported OR **0.047** for ARVC across PKP2tv seen in both cohorts) (hylind2022populationprevalenceof pages 5-7) | No detailed ECG/CMR rates in snippet; molecular evidence supports haploinsufficiency with plakophilin-2 reduced to ~**50%** in myocardium; AF noted as more common in UKB PKP2tv carriers (hylind2022populationprevalenceof pages 5-7) | Strong evidence for **incomplete penetrance** and need for additional genetic/environmental modifiers; example splice acceptor **c.2146-1G>C** seen in **46** UKB carriers but only **1** manifest ARVC case (hylind2022populationprevalenceof pages 5-7) |
| Robles-Mezcua et al. (2023, *Genes*) | Málaga founder cohort with **PKP2 p.Glu259Glyfs*77** | **47** subjects total; **24** variant carriers and **8** index families described | Mean diagnosis age **48.9 ± 18.6 y**; arrhythmic presentation **21.5%** and arrhythmic events during follow-up **20.9%**; HF onset in **25%**; **8.3%** underwent VT ablation; **8.3%** received appropriate ICD therapy; 1 patient required heart transplant; no significant sex differences in follow-up events, though women diagnosed younger (**48.4 ± 17.3 y**) (roblesmezcua2023thenovelvariant pages 6-9) | Specific ECG/CMR metrics not provided in snippet; patients were followed in HF/ICD unit and diagnosed using NGS plus clinical ACM evaluation (roblesmezcua2023thenovelvariant pages 10-12, roblesmezcua2023thenovelvariant pages 6-9) | Variant interpreted as pathogenic truncating PKP2 change with **incomplete penetrance**, variable expressivity, and probable regional founder effect; most affected carriers reportedly >55 y (roblesmezcua2023thenovelvariant pages 10-12, roblesmezcua2023thenovelvariant pages 6-9) |
| Aljehani et al. (2023, *BMC Cardiovascular Disorders*) | Tertiary inherited-cardiac-clinic cohort with suspected ARVC; includes desmosomal-positive cases such as PKP2 | **165** at-risk; **60** definite ARVC; **105** non-definite | Definite ARVC patients more symptomatic: palpitations **57% vs 17%**, syncope **35% vs 6%**, dyspnea **28% vs 5%**; sustained VT **27% vs 2%**; VF **13%** in definite group only; **38/60 (72%)** definite cases carried a pathogenic variant (aljehani2023characterisationofpatients pages 1-2) | T-wave inversion **V1–V3** and epsilon waves seen only in definite group; longer PR (**170 ± 34 ms**) and QRS (**100 ± 19 ms**) than non-definite (**149 ± 25 ms**, **91 ± 14 ms**); larger RVEDA (**27 ± 10 cm²**), lower RVFAC (**37 ± 11%**) and LVEF (**56 ± 12%**) vs non-definite (**18 ± 4 cm²**, **49 ± 6%**, **64 ± 7%**) (aljehani2023characterisationofpatients pages 1-2) | Not PKP2-specific, but useful clinical comparator for phenotype severity and diagnostic yield in real-world ARVC assessment (aljehani2023characterisationofpatients pages 1-2) |
| Casian et al. (2024, *Polish Heart Journal*) | Illustrative ARVC case with likely pathogenic **PKP2 c.1034+1G>C** plus DSP VUS | **1** case | Qualitative phenotype: definite ARVC supported by structural and electrical abnormalities; sustained/complex ventricular arrhythmias prompted primary-prevention ICD decision-making in narrative case (casian2024arrhythmogenicrightventricular pages 9-10, casian2024arrhythmogenicrightventricular pages 3-5) | ECG: anterior T-wave inversion **V3–V4**, epsilon waves **V3–V4**; Holter: frequent PVCs **3% / ~3,500 ectopics per 24 h**; strain echo: RV free-wall strain **−17.8%** with abnormal post-systolic shortening; CMR: RVEDVi **110 mL/m²**, RVEF **44%**, RV free-wall dyskinesia (casian2024arrhythmogenicrightventricular pages 9-10) | Highlights contemporary deep phenotyping, cascade testing, sports restriction, and serial follow-up for PKP2-associated disease with variable penetrance (casian2024arrhythmogenicrightventricular pages 9-10, casian2024arrhythmogenicrightventricular pages 3-5) |


*Table: This table summarizes quantitative phenotype and diagnostic findings for PKP2-related arrhythmogenic cardiomyopathy across key recent cohorts and one illustrative case. It is useful for comparing penetrance, arrhythmic burden, heart failure risk, sex effects, and the ECG/CMR/Holter features most often reported.*

### 3.3 Phenotype-to-ontology mapping (HPO suggestions)
Below are practical HPO mappings for a PKP2-ACM knowledge base (frequencies vary by cohort; use study-specific frequencies where given):
* **Ventricular tachycardia / ventricular fibrillation** → HP:0001663 (Ventricular tachycardia), HP:0001662 (Ventricular fibrillation) (Bos: sustained VA 27%) (bos2023thearrhythmogeniccardiomyopathy pages 1-3)
* **Premature ventricular contractions (PVCs)** → HP:0011705 (Premature ventricular contractions) (Bos: PVC burden >1% in 34%) (bos2023thearrhythmogeniccardiomyopathy pages 4-6)
* **Syncope** → HP:0001279 (Syncope) (Aljehani: 35% definite ARVC; Bos: 12% at presentation) (aljehani2023characterisationofpatients pages 1-2, bos2023thearrhythmogeniccardiomyopathy pages 4-6)
* **Palpitations** → HP:0001962 (Palpitations) (Aljehani: 57% definite ARVC) (aljehani2023characterisationofpatients pages 1-2)
* **Sudden cardiac arrest** → HP:0001699 (Sudden death) / HP:0001645 (Sudden cardiac death) (Bos: SCA enriched in males) (bos2023thearrhythmogeniccardiomyopathy pages 4-6)
* **Right ventricular dilatation/dysfunction** → HP:0001698 (Dilated right ventricle), HP:0033688 (Right ventricular systolic dysfunction) (Bos: 46% RV dilatation/dysfunction) (bos2023thearrhythmogeniccardiomyopathy pages 1-3)
* **Left ventricular involvement / fibrosis (CMR LGE)** → HP:0005162 (Abnormal left ventricular function), HP:0034332 (Myocardial fibrosis) (Bos: LV involvement 37%; LV LGE ~33% among imaged) (bos2023thearrhythmogeniccardiomyopathy pages 4-6)
* **Heart failure** → HP:0001635 (Congestive heart failure) (Bos: 11%; Robles-Mezcua: 25%) (bos2023thearrhythmogeniccardiomyopathy pages 1-3, roblesmezcua2023thenovelvariant pages 6-9)
* **ECG epsilon waves** → (HPO does not consistently include epsilon wave as a standalone term; represent as ECG abnormality HP:0011712 with note) (Aljehani; Casian) (aljehani2023characterisationofpatients pages 1-2, casian2024arrhythmogenicrightventricular pages 9-10)

### 3.4 Quality of life impact
While disease-specific EQ-5D/SF-36 metrics were not retrieved here, clinical impacts are implied by syncope, ICD implantation, arrhythmia burden, and progression to HF/transplant in a subset. (bos2023thearrhythmogeniccardiomyopathy pages 4-6, roblesmezcua2023thenovelvariant pages 6-9)

---

## 4. Genetic/molecular information
### 4.1 Causal gene
* **PKP2 (plakophilin-2)**—intercalated disc/desmosomal component. (vencato2024animalmodelsand pages 2-4)

### 4.2 Pathogenic variant classes (examples from recent cohorts)
* Truncating frameshift founder variants: **PKP2 c.1211dup (p.Val406Serfs*4)** (Bos 2023). (bos2023thearrhythmogeniccardiomyopathy pages 1-3)
* Splice variants: likely pathogenic **PKP2 c.1034+1G>C** in a definite ARVC case. (casian2024arrhythmogenicrightventricular pages 9-10)
* Additional founder/truncating variants: **p.Glu259Glyfs*77** (Robles‑Mezcua 2023). (roblesmezcua2023thenovelvariant pages 6-9)

Variant interpretation standards referenced in clinical genetics include ACMG/AMP variant classification and periodic re-evaluation of VUS. (roblesmezcua2023thenovelvariant pages 10-12, casian2024arrhythmogenicrightventricular pages 9-10)

### 4.3 Population frequency and penetrance considerations
In UK Biobank, **PKP2 truncating variants were present in 193/200,643 (0.10%)**, but ARVC features were present in only **~1.6%**, illustrating a major penetrance gap between population genomics and clinically ascertained cohorts. (hylind2022populationprevalenceof pages 5-7)

---

## 5. Environmental information
The strongest, repeatedly emphasized environmental factor in ACM is **vigorous/endurance exercise**, which can trigger electrical instability and accelerate phenotypic expression; therefore, sports restriction is commonly incorporated into management. (pilichou2016arrhythmogeniccardiomyopathy pages 1-2, pilichou2016arrhythmogeniccardiomyopathy pages 2-3)

Infectious triggers are not established as primary causes, though myocarditis-like presentations and inflammatory infiltrates are reported in ACM and may be part of the pathobiology in subsets. (pilichou2016arrhythmogeniccardiomyopathy pages 2-3, pilichou2016arrhythmogeniccardiomyopathy pages 3-5)

---

## 6. Mechanism / pathophysiology
### 6.1 Current mechanistic model (causal chain)
A synthesis of recent mechanistic work supports a multi-axis causal chain:

1. **PKP2 haploinsufficiency or loss** → impaired intercalated disc/desmosome structure (widened intercalated discs; reduced junctional proteins) (vencato2024animalmodelsand pages 5-7, vencato2024animalmodelsand pages 2-4)
2. **Mechanical uncoupling and mechanosensing defects** → altered actin remodeling (RhoA–ROCK) and reduced MRTF/SRF transcriptional activity, facilitating adipogenic programs (chua2023understandingarrhythmogeniccardiomyopathy pages 17-19)
3. **Electrical remodeling** via “functional triad” disruption (desmosomes–gap junctions–Na channels): reduced Cx43 and NaV1.5 mislocalization/INa reduction → slowed conduction and re-entry propensity (pilichou2016arrhythmogeniccardiomyopathy pages 12-14, vencato2024animalmodelsand pages 5-7)
4. **Signal pathway reprogramming**: plakoglobin nuclear translocation suppresses canonical **Wnt/β-catenin**, and **Hippo/YAP** activation contributes to fibrofatty remodeling (chua2023understandingarrhythmogeniccardiomyopathy pages 6-8, vencato2024animalmodelsand pages 2-4)
5. **Fibrosis and inflammation**: PKP2 deficiency links to **TGF-β1/p38 MAPK** profibrotic signaling and transcriptomic immune/inflammatory signatures (chua2023understandingarrhythmogeniccardiomyopathy pages 31-33, vencato2024animalmodelsand pages 4-5)
6. **Metabolic remodeling/adipogenesis**: PPARα/PPARG programs, lipogenesis/fatty-acid oxidation shifts, ROS and apoptosis (chua2023understandingarrhythmogeniccardiomyopathy pages 17-19, song2024multiomicsanalysisreveals pages 1-5)

### 6.2 Pathways and ontology suggestions
* **Wnt/β-catenin signaling** (GO:0016055) (vencato2024animalmodelsand pages 2-4)
* **Hippo signaling** (GO:0035329; pathway-level) (chua2023understandingarrhythmogeniccardiomyopathy pages 6-8)
* **TGF-β signaling** / fibrosis (GO:0007179; GO:0006468 with p38 MAPK cascade as relevant) (vencato2024animalmodelsand pages 4-5)
* **Cell–cell adhesion** (GO:0098609) (vencato2024animalmodelsand pages 2-4)
* **Cardiac conduction** (GO:0061337) / **gap junction assembly** (GO:1901889) (vencato2024animalmodelsand pages 5-7)

### 6.3 Cell types and anatomical structures (CL/UBERON suggestions)
* **Cardiomyocyte** (CL:0000746)
* **Cardiac fibroblast** (CL:0002548)
* **Monocyte-derived macrophage** (CL:0001054; in broader ACM immune literature, not PKP2-specific in our excerpts)

Primary anatomical sites:
* **Heart** (UBERON:0000948)
* **Right ventricle** (UBERON:0002080)
* **Left ventricle** (UBERON:0002084)
* **Intercalated disc** (GO cellular component: intercalated disc; and desmosome GO:0030057)

---

## 7. Anatomical structures affected
Disease predominantly affects ventricular myocardium (classically RV), but biventricular and LV involvement are clinically relevant in PKP2 cohorts (e.g., LV involvement in 37% for PKP2 c.1211dup carriers). (bos2023thearrhythmogeniccardiomyopathy pages 1-3)

---

## 8. Temporal development
In a PKP2 founder cohort, ventricular arrhythmias were described as early manifestations “from 14 years of age onwards,” while heart failure was “uncommon before the age of 55 years,” supporting an age-dependent progression pattern with early electrical disease and later pump failure. (bos2023thearrhythmogeniccardiomyopathy pages 1-3)

---

## 9. Inheritance and population
### 9.1 Inheritance
ACM is most often familial with **autosomal-dominant inheritance** and **incomplete penetrance**, though recessive forms exist in ACM more broadly. (pilichou2016arrhythmogeniccardiomyopathy pages 1-2, pilichou2016arrhythmogeniccardiomyopathy pages 3-5)

### 9.2 Epidemiology
* Prevalence of ACM is estimated at **1:2000–1:5000**. (pilichou2016arrhythmogeniccardiomyopathy pages 1-2, pilichou2016arrhythmogeniccardiomyopathy pages 2-3)
* Population genomics: PKP2 truncating variants identified in **0.10%** of UK Biobank participants, with ARVC features in only **~1.6%**, underscoring that genotype prevalence exceeds clinical disease prevalence. (hylind2022populationprevalenceof pages 5-7)

---

## 10. Diagnostics
### 10.1 Clinical criteria and diagnostic workup
There is **no single gold standard**; the **2010 Revised Task Force Criteria** integrate imaging (echo/CMR), histology/biopsy, ECG, arrhythmias, and family history/genetics. (pilichou2016arrhythmogeniccardiomyopathy pages 3-5)

Key practical diagnostic markers in contemporary care include:
* ECG: anterior T-wave inversion (V1–V3, or beyond), epsilon waves (minor criterion), conduction intervals (PR/QRS prolongation in definite cases) (aljehani2023characterisationofpatients pages 1-2, casian2024arrhythmogenicrightventricular pages 3-5)
* Holter: frequent PVCs and VT burden (aljehani2023characterisationofpatients pages 1-2, casian2024arrhythmogenicrightventricular pages 9-10)
* Imaging: CMR for RV volumes and function and tissue characterization (LGE) (casian2024arrhythmogenicrightventricular pages 3-5, mo2024describingandmapping pages 7-8)
* Strain imaging: reduced RV free-wall strain can support disease detection (casian2024arrhythmogenicrightventricular pages 9-10)
* Genetics: a pathogenic mutation is a major criterion in 2010 criteria, and genetic testing is embedded in modern diagnostic algorithms. (biernacka2021pathogenicvariantsin pages 1-2, mo2024describingandmapping pages 7-8)

### 10.2 Visual evidence: diagnostic criteria tables
Tables comparing diagnostic criteria frameworks and differential diagnosis ECG/imaging patterns were extracted from Casian et al. (2024). (casian2024arrhythmogenicrightventricular media 2c72158c, casian2024arrhythmogenicrightventricular media 7736dc34)

### 10.3 Genetic testing approach
Genetic testing is used to confirm diagnosis and enable cascade screening; variant interpretation requires periodic re-evaluation (especially for VUS) and segregation analysis. (casian2024arrhythmogenicrightventricular pages 9-10, roblesmezcua2023thenovelvariant pages 10-12)

---

## 11. Outcomes / prognosis
### 11.1 Arrhythmic outcomes
In PKP2 c.1211dup carriers, sustained ventricular arrhythmia occurred in **27%** overall, with strong sex differences by age 40 (33% men vs 9% women). (bos2023thearrhythmogeniccardiomyopathy pages 4-6, bos2023thearrhythmogeniccardiomyopathy pages 1-3)

In affected adults with ACM broadly, a review cites **sudden death incidence 0.08–3.6%/year**. (pilichou2016arrhythmogeniccardiomyopathy pages 3-5)

### 11.2 Heart failure and transplant
In PKP2 c.1211dup carriers, HF developed in **11%** overall and accumulated mostly at older ages; in the Málaga founder series HF onset was **25%**, and transplant occurred in at least one case. (bos2023thearrhythmogeniccardiomyopathy pages 1-3, roblesmezcua2023thenovelvariant pages 6-9)

### 11.3 Genotype-informed prognosis
One cohort analysis suggests PKP2 pathogenic variants may associate with better survival compared with non-PKP2 ARVC genotypes (e.g., less LV progression and lower death/transplant composite). (biernacka2021pathogenicvariantsin pages 1-2)

---

## 12. Treatment
### 12.1 Current applications / real-world implementations
Management is centered on preventing sudden cardiac death and managing arrhythmias and HF, including:
* **ICD therapy**: a core therapy in risk-stratified patients; established for secondary prevention and used for selected primary-prevention cases. (pilichou2016arrhythmogeniccardiomyopathy pages 12-14, mo2024describingandmapping pages 7-8)
* **Antiarrhythmic drug therapy**: used as part of symptomatic control and arrhythmia reduction; details vary by patient and were not fully extractable from the retrieved excerpts. (pilichou2016arrhythmogeniccardiomyopathy pages 1-2)
* **Catheter ablation**: used for VT control; in one PKP2 founder series, VT ablation occurred in 8.3% of patients. (roblesmezcua2023thenovelvariant pages 6-9)
* **Exercise restriction / sport disqualification**: described as life-saving due to effort-triggered electrical instability and acceleration of disease onset/progression. (pilichou2016arrhythmogeniccardiomyopathy pages 1-2)

### 12.2 MAXO suggestions (interventions)
* Implantation of cardioverter-defibrillator → **MAXO:0000508** (implantable cardioverter defibrillator implantation)
* Catheter ablation for VT → **MAXO:0000479** (cardiac ablation procedure; map to local MAXO in implementation)
* Beta-blocker therapy → **MAXO:0000511** (beta-adrenergic antagonist therapy)
* Exercise restriction / activity modification → **MAXO:0000915** (lifestyle modification; use appropriate child term)

(Notes: MAXO IDs may vary by release; verify in your ontology build system.)

---

## 13. Prevention
Primary prevention in genetically susceptible individuals is largely behavioral and surveillance-based:
* **Cascade genetic screening** for at-risk relatives and periodic cardiac evaluation (ECG/Holter/imaging) (casian2024arrhythmogenicrightventricular pages 9-10, pilichou2016arrhythmogeniccardiomyopathy pages 1-2)
* **Restriction from high-intensity endurance/competitive sports** in diagnosed individuals and (often) high-risk carriers (pilichou2016arrhythmogeniccardiomyopathy pages 1-2)

---

## 14. Other species / natural disease
No naturally occurring veterinary PKP2-ACM evidence was retrieved in this tool run.

---

## 15. Model organisms and experimental systems
### 15.1 In vitro (human)
Human iPSC-derived cardiomyocytes and engineered myocardium reproduce PKP2 junctional, conduction, and contractile defects, and demonstrate molecular rescue via PKP2 gene replacement. (kyriakopoulou2023therapeuticefficacyof pages 1-2, mundisugih2024exploringthetherapeutic pages 2-4)

**Abstract quote (hiPSC model value):** “Human induced pluripotent stem cells (hiPSCs) have emerged as a powerful tool for modeling ACM in vitro…” (Chua et al., 2023) (chua2023understandingarrhythmogeniccardiomyopathy pages 31-33)

### 15.2 In vivo (mouse)
Several mouse models show severe arrhythmogenic phenotypes and enable gene-therapy testing:
* Splice-site knock-in model with sudden death beginning at 4 weeks; AAV-PKP2 prevented and rescued disease with **100% survival** in treated windows. (bradford2023plakophilin2gene pages 1-2)
* Tamoxifen-inducible, cardiac-specific Pkp2 knockout used to test AAV9:PKP2 (TN‑401) with dose testing (e.g., 3E13–6E13 vg/kg preventive) and dramatic survival benefit in the model. (wu2024aav9pkp2improvesheart pages 13-14, wu2024aav9pkp2improvesheart pages 2-3)

### 15.3 In vivo (guinea pig)
AAV9-shRNA PKP2 knockdown in guinea pigs recapitulated RV enlargement, sudden death, and lipid accumulation; multi-omics implicated ECM remodeling and metabolic shifts (PI3K-Akt; lipid/TCA changes). (song2024multiomicsanalysisreveals pages 1-5, song2024multiomicsanalysisreveals pages 9-14)

---

## 16. Recent developments (2023–2024): gene therapy and translational pipeline
### 16.1 Preclinical gene replacement (key 2023–2024 findings)
Multiple independent studies show that AAV-mediated PKP2 replacement restores junctional proteins, improves conduction/contractility, reduces remodeling, and improves survival in PKP2-deficient models:
* **Kyriakopoulou et al. (2023-12; Nature Cardiovascular Research; https://doi.org/10.1038/s44161-023-00378-9):** AAV6–PKP2 restored PKP2 and other junction proteins in PKP2c.2013delC/WT iPSC-CMs, improved sodium conduction, and improved engineered human myocardium; systemic AAV9–PKP2 prevented dysfunction in heterozygous knock-in mice at 12 months. (kyriakopoulou2023therapeuticefficacyof pages 1-2)
* **Bradford et al. (2023-12; Nature Cardiovascular Research; https://doi.org/10.1038/s44161-023-00370-3):** neonatal gene therapy restored PKP2 and produced **100% survival** up to 6 months; late-stage administration rescued desmosomal deficits and produced **100% survival** up to 4 months in a severe splice-site model. (bradford2023plakophilin2gene pages 1-2)
* **Wu et al. (2024-03; Communications Medicine; https://doi.org/10.1038/s43856-024-00450-w):** AAV9:PKP2 (TN‑401) prevented disease onset and attenuated established cardiomyopathy; preventive doses included **3E13–6E13 vg/kg** in the mouse model. (wu2024aav9pkp2improvesheart pages 1-2, wu2024aav9pkp2improvesheart pages 13-14)
* **van Opbergen et al. (2024-02; Circulation: Genomic and Precision Medicine; https://doi.org/10.1161/circgen.123.004305):** AAVrh.74-PKP2a arrested progression with survival benefit (100% survival in treated vs 100% mortality in untreated model). (opbergen2024aavmediateddeliveryof pages 7-9)

### 16.2 Expert synthesis (2024 review)
A 2024 review emphasizes PKP2 as a high-priority ARVC gene-therapy target and notes translational hurdles (vector dosing, immune barriers, cardiac specificity). (mundisugih2024exploringthetherapeutic pages 2-4)

**Abstract quote (state of translation):** “Despite notable scientific advancements, the journey towards implementing genetic therapies for ARVC patients in real-world clinical settings is still in its early phases.” (Mundisugih et al., 2024; Biomedicines; published 2024-06; https://doi.org/10.3390/biomedicines12061351) (mundisugih2024exploringthetherapeutic pages 2-4)

---

## 17. Clinical trials and real-world implementations (2024–2025)
### 17.1 PKP2 gene therapy interventional trials (Phase 1/2)
* **TN‑401** (Tenaya Therapeutics) – Phase 1, open-label dose escalation in adults with PKP2 mutation-associated ARVC: **NCT06228924** (Recruiting). (ClinicalTrials.gov) (trial metadata retrieved; details beyond NCT listing not shown in excerpts). 
* **RP‑A601** (Rocket Pharmaceuticals) – Phase 1 dose escalation in PKP2 variant-mediated arrhythmogenic cardiomyopathy: **NCT05885412** (Recruiting). 
* **LX2020** (Lexeo Therapeutics) – Phase 1/2 gene therapy for ACM due to a PKP2 pathogenic variant: **NCT06109181** (Active, not recruiting). 

(These are identified by clinical trial search results in this run; detailed fields were not fully extractable for all NCTs in available excerpts.)

### 17.2 Observational trials/registries supporting implementation
* **SNAPSHOT‑PKP2** (Lexeo) – real-world symptomatic PKP2-ACM registry with AAVrh.10 antibody testing, biomarkers, imaging/ECG, and PVC endpoint. **NCT06976606**; start **2024-01-23**; enrollment **40**; recruiting. (NCT06976606 chunk 1)
* **GRIT‑PKP2 / LX2020-02** – long-term follow-up after receiving LX2020 parent study, safety TEAE/TESAE over 4 years; start **2025-08-29**; enrollment **10**; enrolling by invitation. **NCT07050160**. (NCT07050160 chunk 1)

---

## Data gaps / limitations in this evidence set
* MONDO/ICD/MeSH identifiers were not extractable from retrieved sources in this run.
* Several sections (epigenetics, protective genetic variants, validated QoL scales) are incompletely supported by the retrieved full-text excerpts.
* Some clinical-trial vector/construct details (e.g., exact capsid/promoter) were not present in the extracted NCT excerpts.

---

## Key references (URLs and publication dates)
* Pilichou K, et al. **Arrhythmogenic cardiomyopathy.** *Orphanet J Rare Dis.* **2016-04**. https://doi.org/10.1186/s13023-016-0407-1 (pilichou2016arrhythmogeniccardiomyopathy pages 1-2)
* Bos TA, et al. **PKP2 c.1211dup phenotype.** *Netherlands Heart Journal.* **2023-07**. https://doi.org/10.1007/s12471-023-01791-2 (bos2023thearrhythmogeniccardiomyopathy pages 1-3)
* Casian M, et al. **ARVC diagnostic challenges from imaging to genetics.** *Polish Heart Journal.* **2024-09**. https://doi.org/10.33963/v.phj.102391 (casian2024arrhythmogenicrightventricular pages 9-10)
* Chua CJ, et al. **hiPSC models of ACM.** *Genes.* **2023-09**. https://doi.org/10.3390/genes14101864 (chua2023understandingarrhythmogeniccardiomyopathy pages 31-33)
* Vencato S, et al. **Animal models and pathogenesis.** *Int J Mol Sci.* **2024-06**. https://doi.org/10.3390/ijms25116208 (vencato2024animalmodelsand pages 5-7)
* Wu I, et al. **AAV9:PKP2 in Pkp2-deficient mice.** *Communications Medicine.* **2024-03**. https://doi.org/10.1038/s43856-024-00450-w (wu2024aav9pkp2improvesheart pages 1-2)
* Kyriakopoulou E, et al. **AAV-mediated PKP2 restoration.** *Nature Cardiovascular Research.* **2023-12**. https://doi.org/10.1038/s44161-023-00378-9 (kyriakopoulou2023therapeuticefficacyof pages 1-2)
* Bradford WH, et al. **PKP2 gene therapy in splice-site model.** *Nature Cardiovascular Research.* **2023-12**. https://doi.org/10.1038/s44161-023-00370-3 (bradford2023plakophilin2gene pages 1-2)
* van Opbergen CJM, et al. **AAVrh.74-PKP2a arrests progression.** *Circ Genom Precis Med.* **2024-02**. https://doi.org/10.1161/circgen.123.004305 (opbergen2024aavmediateddeliveryof pages 7-9)
* Mundisugih J, et al. **Gene therapy review.** *Biomedicines.* **2024-06**. https://doi.org/10.3390/biomedicines12061351 (mundisugih2024exploringthetherapeutic pages 2-4)
* ClinicalTrials.gov: **NCT06976606** (start 2024-01-23) (NCT06976606 chunk 1); **NCT07050160** (start 2025-08-29) (NCT07050160 chunk 1)


References

1. (pilichou2016arrhythmogeniccardiomyopathy pages 1-2): Kalliopi Pilichou, Gaetano Thiene, Barbara Bauce, Ilaria Rigato, Elisabetta Lazzarini, Federico Migliore, Martina Perazzolo Marra, Stefania Rizzo, Alessandro Zorzi, Luciano Daliento, Domenico Corrado, and Cristina Basso. Arrhythmogenic cardiomyopathy. Orphanet Journal of Rare Diseases, Apr 2016. URL: https://doi.org/10.1186/s13023-016-0407-1, doi:10.1186/s13023-016-0407-1. This article has 211 citations and is from a peer-reviewed journal.

2. (bos2023thearrhythmogeniccardiomyopathy pages 4-6): Thomas A. Bos, Sebastiaan R. D. Piers, Marja W. Wessels, Arjan C. Houweling, Regina Bökenkamp, Marianne Bootsma, Laurens P. Bosman, Reinder Evertz, Debby M. E. I. Hellebrekers, Yvonne M. Hoedemaekers, Jeroen Knijnenburg, Ronald Lekanne Deprez, Anneke M. van Mil, Anneline S. J. M. te Riele, Marjon A. van Slegtenhorst, Arthur A. M. Wilde, Sing-Chien Yap, Dennis Dooijes, Tamara T. Koopmann, J. Peter van Tintelen, Daniela Q. C. M. Barge-Schaapveld, Arjan C. Houweling, Ronald Lekanne Deprez, Anneline S. J. M. te Riele, Arthur A. M. Wilde, and J. Peter van Tintelen. The arrhythmogenic cardiomyopathy phenotype associated with pkp2 c.1211dup variant. Netherlands Heart Journal, 31:315-323, Jul 2023. URL: https://doi.org/10.1007/s12471-023-01791-2, doi:10.1007/s12471-023-01791-2. This article has 3 citations and is from a peer-reviewed journal.

3. (chua2023understandingarrhythmogeniccardiomyopathy pages 6-8): Christianne J. Chua, Justin Morrissette-McAlmon, Leslie Tung, and Kenneth R. Boheler. Understanding arrhythmogenic cardiomyopathy: advances through the use of human pluripotent stem cell models. Genes, 14:1864, Sep 2023. URL: https://doi.org/10.3390/genes14101864, doi:10.3390/genes14101864. This article has 19 citations.

4. (mundisugih2024exploringthetherapeutic pages 2-4): Juan Mundisugih, Dhanya Ravindran, and Eddy Kizana. Exploring the therapeutic potential of gene therapy in arrhythmogenic right ventricular cardiomyopathy. Biomedicines, 12:1351, Jun 2024. URL: https://doi.org/10.3390/biomedicines12061351, doi:10.3390/biomedicines12061351. This article has 12 citations.

5. (NCT06976606 chunk 1):  A Study to Assess Real-world Patient Characteristics and Clinical Course for Symptomatic Patients With PKP2-ACM. Lexeo Therapeutics. 2024. ClinicalTrials.gov Identifier: NCT06976606

6. (bos2023thearrhythmogeniccardiomyopathy pages 1-3): Thomas A. Bos, Sebastiaan R. D. Piers, Marja W. Wessels, Arjan C. Houweling, Regina Bökenkamp, Marianne Bootsma, Laurens P. Bosman, Reinder Evertz, Debby M. E. I. Hellebrekers, Yvonne M. Hoedemaekers, Jeroen Knijnenburg, Ronald Lekanne Deprez, Anneke M. van Mil, Anneline S. J. M. te Riele, Marjon A. van Slegtenhorst, Arthur A. M. Wilde, Sing-Chien Yap, Dennis Dooijes, Tamara T. Koopmann, J. Peter van Tintelen, Daniela Q. C. M. Barge-Schaapveld, Arjan C. Houweling, Ronald Lekanne Deprez, Anneline S. J. M. te Riele, Arthur A. M. Wilde, and J. Peter van Tintelen. The arrhythmogenic cardiomyopathy phenotype associated with pkp2 c.1211dup variant. Netherlands Heart Journal, 31:315-323, Jul 2023. URL: https://doi.org/10.1007/s12471-023-01791-2, doi:10.1007/s12471-023-01791-2. This article has 3 citations and is from a peer-reviewed journal.

7. (pilichou2016arrhythmogeniccardiomyopathy pages 2-3): Kalliopi Pilichou, Gaetano Thiene, Barbara Bauce, Ilaria Rigato, Elisabetta Lazzarini, Federico Migliore, Martina Perazzolo Marra, Stefania Rizzo, Alessandro Zorzi, Luciano Daliento, Domenico Corrado, and Cristina Basso. Arrhythmogenic cardiomyopathy. Orphanet Journal of Rare Diseases, Apr 2016. URL: https://doi.org/10.1186/s13023-016-0407-1, doi:10.1186/s13023-016-0407-1. This article has 211 citations and is from a peer-reviewed journal.

8. (pilichou2016arrhythmogeniccardiomyopathy pages 3-5): Kalliopi Pilichou, Gaetano Thiene, Barbara Bauce, Ilaria Rigato, Elisabetta Lazzarini, Federico Migliore, Martina Perazzolo Marra, Stefania Rizzo, Alessandro Zorzi, Luciano Daliento, Domenico Corrado, and Cristina Basso. Arrhythmogenic cardiomyopathy. Orphanet Journal of Rare Diseases, Apr 2016. URL: https://doi.org/10.1186/s13023-016-0407-1, doi:10.1186/s13023-016-0407-1. This article has 211 citations and is from a peer-reviewed journal.

9. (chua2023understandingarrhythmogeniccardiomyopathy pages 31-33): Christianne J. Chua, Justin Morrissette-McAlmon, Leslie Tung, and Kenneth R. Boheler. Understanding arrhythmogenic cardiomyopathy: advances through the use of human pluripotent stem cell models. Genes, 14:1864, Sep 2023. URL: https://doi.org/10.3390/genes14101864, doi:10.3390/genes14101864. This article has 19 citations.

10. (opbergen2024aavmediateddeliveryof pages 7-9): Chantal J.M. van Opbergen, Bitha Narayanan, Chester B. Sacramento, Katie M. Stiles, Vartika Mishra, Esther Frenk, David Ricks, Grace Chen, Mingliang Zhang, Paul Yarabe, Jonathan Schwartz, Mario Delmar, Chris D. Herzog, and Marina Cerrone. Aav-mediated delivery of plakophilin-2a arrests progression of arrhythmogenic right ventricular cardiomyopathy in murine hearts: preclinical evidence supporting gene therapy in humans. Circulation: Genomic and Precision Medicine, Feb 2024. URL: https://doi.org/10.1161/circgen.123.004305, doi:10.1161/circgen.123.004305. This article has 55 citations.

11. (chua2023understandingarrhythmogeniccardiomyopathy pages 17-19): Christianne J. Chua, Justin Morrissette-McAlmon, Leslie Tung, and Kenneth R. Boheler. Understanding arrhythmogenic cardiomyopathy: advances through the use of human pluripotent stem cell models. Genes, 14:1864, Sep 2023. URL: https://doi.org/10.3390/genes14101864, doi:10.3390/genes14101864. This article has 19 citations.

12. (vencato2024animalmodelsand pages 5-7): Sara Vencato, Chiara Romanato, Alessandra Rampazzo, and Martina Calore. Animal models and molecular pathogenesis of arrhythmogenic cardiomyopathy associated with pathogenic variants in intercalated disc genes. International Journal of Molecular Sciences, 25:6208, Jun 2024. URL: https://doi.org/10.3390/ijms25116208, doi:10.3390/ijms25116208. This article has 9 citations.

13. (aljehani2023characterisationofpatients pages 1-2): A. Aljehani, T. Kew, S. Baig, H. Cox, L. C. Sommerfeld, B. Ensam, M. Kalla, R. P. Steeds, and L. Fabritz. Characterisation of patients referred to a tertiary-level inherited cardiac condition clinic with suspected arrhythmogenic right ventricular cardiomyopathy (arvc). BMC Cardiovascular Disorders, Jan 2023. URL: https://doi.org/10.1186/s12872-022-03021-w, doi:10.1186/s12872-022-03021-w. This article has 4 citations and is from a peer-reviewed journal.

14. (casian2024arrhythmogenicrightventricular pages 9-10): Mihnea Casian, Michael Papadakis, and Ruxandra Jurcut. Arrhythmogenic right ventricular cardiomyopathies (arvc): diagnostic challenges from imaging to genetics. Polish Heart Journal, Sep 2024. URL: https://doi.org/10.33963/v.phj.102391, doi:10.33963/v.phj.102391. This article has 4 citations.

15. (roblesmezcua2023thenovelvariant pages 6-9): Ainhoa Robles-Mezcua, Amalio Ruíz-Salas, Carmen Medina-Palomo, María Robles-Mezcua, Arancha Díaz-Expósito, María Victoria Ortega-Jiménez, Juan Ramón Gimeno-Blanes, Manuel F. Jiménez-Navarro, and José Manuel García-Pinilla. The novel variant np_00454563.2 (p.glu259glyfs*77) in gene pkp2 associated with arrhythmogenic cardiomyopathy in 8 families from malaga, spain. Genes, 14:1468, Jul 2023. URL: https://doi.org/10.3390/genes14071468, doi:10.3390/genes14071468. This article has 3 citations.

16. (hylind2022populationprevalenceof pages 5-7): Robyn J. Hylind, Alexandre C. Pereira, Daniel Quiat, Stephanie F. Chandler, Thomas M. Roston, William T. Pu, Vassilios J. Bezzerides, Jonathan G. Seidman, Christine E. Seidman, and Dominic J. Abrams. Population prevalence of premature truncating variants in plakophilin-2 and association with arrhythmogenic right ventricular cardiomyopathy: a uk biobank analysis. Circulation: Genomic and Precision Medicine, Jun 2022. URL: https://doi.org/10.1161/circgen.121.003507, doi:10.1161/circgen.121.003507. This article has 19 citations.

17. (kyriakopoulou2023therapeuticefficacyof pages 1-2): Eirini Kyriakopoulou, Danielle Versteeg, Hesther de Ruiter, Ilaria Perini, Fitzwilliam Seibertz, Yannic Döring, Lorena Zentilin, Hoyee Tsui, Sebastiaan J. van Kampen, Malte Tiburcy, Tim Meyer, Niels Voigt, van J. Peter Tintelen, Wolfram H. Zimmermann, Mauro Giacca, and Eva van Rooij. Therapeutic efficacy of aav-mediated restoration of pkp2 in arrhythmogenic cardiomyopathy. Nature Cardiovascular Research, 2:1262-1276, Dec 2023. URL: https://doi.org/10.1038/s44161-023-00378-9, doi:10.1038/s44161-023-00378-9. This article has 66 citations and is from a peer-reviewed journal.

18. (wu2024aav9pkp2improvesheart pages 13-14): Iris Wu, Aliya Zeng, Amara Greer-Short, J. Alex Aycinena, Anley E. Tefera, Reva Shenwai, Farshad Farshidfar, Melissa Van Pell, Emma Xu, Chris Reid, Neshel Rodriguez, Beatriz Lim, Tae Won Chung, Joseph Woods, Aquilla Scott, Samantha Jones, Cristina Dee-Hoskins, Carolina G. Gutierrez, Jessie Madariaga, Kevin Robinson, Yolanda Hatter, Renee Butler, Stephanie Steltzer, Jaclyn Ho, James R. Priest, Xiaomei Song, Frank Jing, Kristina Green, Kathryn N. Ivey, Timothy Hoey, Jin Yang, and Zhihong Jane Yang. Aav9:pkp2 improves heart function and survival in a pkp2-deficient mouse model of arrhythmogenic right ventricular cardiomyopathy. Communications Medicine, Mar 2024. URL: https://doi.org/10.1038/s43856-024-00450-w, doi:10.1038/s43856-024-00450-w. This article has 50 citations and is from a peer-reviewed journal.

19. (song2024multiomicsanalysisreveals pages 1-5): Rui Song, Haiyan Wu, Lihui Yu, Jingning Yu, WenHui Yang, WenJun Wu, Fei Sun, and Haizhen Wang. Multiomics analysis reveals extensive remodeling of the extracellular matrix and cellular metabolism due to plakophilin-2 knockdown in guinea pigs. bioRxiv, Mar 2024. URL: https://doi.org/10.1101/2024.03.11.584401, doi:10.1101/2024.03.11.584401. This article has 1 citations.

20. (vencato2024animalmodelsand pages 2-4): Sara Vencato, Chiara Romanato, Alessandra Rampazzo, and Martina Calore. Animal models and molecular pathogenesis of arrhythmogenic cardiomyopathy associated with pathogenic variants in intercalated disc genes. International Journal of Molecular Sciences, 25:6208, Jun 2024. URL: https://doi.org/10.3390/ijms25116208, doi:10.3390/ijms25116208. This article has 9 citations.

21. (biernacka2021pathogenicvariantsin pages 1-2): Elżbieta K. Biernacka, Karolina Borowiec, Maria Franaszczyk, Małgorzata Szperl, Alessandra Rampazzo, Olgierd Woźniak, Marta Roszczynko, Witold Śmigielski, Anna Lutyńska, and Piotr Hoffman. Pathogenic variants in plakophilin-2 gene (pkp2) are associated with better survival in arrhythmogenic right ventricular cardiomyopathy. Journal of Applied Genetics, 62:613-620, Jun 2021. URL: https://doi.org/10.1007/s13353-021-00647-y, doi:10.1007/s13353-021-00647-y. This article has 25 citations and is from a peer-reviewed journal.

22. (bos2023thearrhythmogeniccardiomyopathy pages 3-4): Thomas A. Bos, Sebastiaan R. D. Piers, Marja W. Wessels, Arjan C. Houweling, Regina Bökenkamp, Marianne Bootsma, Laurens P. Bosman, Reinder Evertz, Debby M. E. I. Hellebrekers, Yvonne M. Hoedemaekers, Jeroen Knijnenburg, Ronald Lekanne Deprez, Anneke M. van Mil, Anneline S. J. M. te Riele, Marjon A. van Slegtenhorst, Arthur A. M. Wilde, Sing-Chien Yap, Dennis Dooijes, Tamara T. Koopmann, J. Peter van Tintelen, Daniela Q. C. M. Barge-Schaapveld, Arjan C. Houweling, Ronald Lekanne Deprez, Anneline S. J. M. te Riele, Arthur A. M. Wilde, and J. Peter van Tintelen. The arrhythmogenic cardiomyopathy phenotype associated with pkp2 c.1211dup variant. Netherlands Heart Journal, 31:315-323, Jul 2023. URL: https://doi.org/10.1007/s12471-023-01791-2, doi:10.1007/s12471-023-01791-2. This article has 3 citations and is from a peer-reviewed journal.

23. (roblesmezcua2023thenovelvariant pages 10-12): Ainhoa Robles-Mezcua, Amalio Ruíz-Salas, Carmen Medina-Palomo, María Robles-Mezcua, Arancha Díaz-Expósito, María Victoria Ortega-Jiménez, Juan Ramón Gimeno-Blanes, Manuel F. Jiménez-Navarro, and José Manuel García-Pinilla. The novel variant np_00454563.2 (p.glu259glyfs*77) in gene pkp2 associated with arrhythmogenic cardiomyopathy in 8 families from malaga, spain. Genes, 14:1468, Jul 2023. URL: https://doi.org/10.3390/genes14071468, doi:10.3390/genes14071468. This article has 3 citations.

24. (casian2024arrhythmogenicrightventricular pages 3-5): Mihnea Casian, Michael Papadakis, and Ruxandra Jurcut. Arrhythmogenic right ventricular cardiomyopathies (arvc): diagnostic challenges from imaging to genetics. Polish Heart Journal, Sep 2024. URL: https://doi.org/10.33963/v.phj.102391, doi:10.33963/v.phj.102391. This article has 4 citations.

25. (pilichou2016arrhythmogeniccardiomyopathy pages 12-14): Kalliopi Pilichou, Gaetano Thiene, Barbara Bauce, Ilaria Rigato, Elisabetta Lazzarini, Federico Migliore, Martina Perazzolo Marra, Stefania Rizzo, Alessandro Zorzi, Luciano Daliento, Domenico Corrado, and Cristina Basso. Arrhythmogenic cardiomyopathy. Orphanet Journal of Rare Diseases, Apr 2016. URL: https://doi.org/10.1186/s13023-016-0407-1, doi:10.1186/s13023-016-0407-1. This article has 211 citations and is from a peer-reviewed journal.

26. (vencato2024animalmodelsand pages 4-5): Sara Vencato, Chiara Romanato, Alessandra Rampazzo, and Martina Calore. Animal models and molecular pathogenesis of arrhythmogenic cardiomyopathy associated with pathogenic variants in intercalated disc genes. International Journal of Molecular Sciences, 25:6208, Jun 2024. URL: https://doi.org/10.3390/ijms25116208, doi:10.3390/ijms25116208. This article has 9 citations.

27. (mo2024describingandmapping pages 7-8): Leitong Mo, Ching‐Hui Sia, Weiqin Lin, Xifeng Zheng, and Kaiyi Peng. Describing and mapping the research trend of scientific publications on arrhythmogenic right ventricular cardiomyopathy across four decades: a bibliometric analysis. Clinical Cardiology, Nov 2024. URL: https://doi.org/10.1002/clc.70051, doi:10.1002/clc.70051. This article has 2 citations and is from a peer-reviewed journal.

28. (casian2024arrhythmogenicrightventricular media 2c72158c): Mihnea Casian, Michael Papadakis, and Ruxandra Jurcut. Arrhythmogenic right ventricular cardiomyopathies (arvc): diagnostic challenges from imaging to genetics. Polish Heart Journal, Sep 2024. URL: https://doi.org/10.33963/v.phj.102391, doi:10.33963/v.phj.102391. This article has 4 citations.

29. (casian2024arrhythmogenicrightventricular media 7736dc34): Mihnea Casian, Michael Papadakis, and Ruxandra Jurcut. Arrhythmogenic right ventricular cardiomyopathies (arvc): diagnostic challenges from imaging to genetics. Polish Heart Journal, Sep 2024. URL: https://doi.org/10.33963/v.phj.102391, doi:10.33963/v.phj.102391. This article has 4 citations.

30. (bradford2023plakophilin2gene pages 1-2): William H. Bradford, Jing Zhang, Erika J. Gutierrez-Lara, Yan Liang, Aryanne Do, Tsui-Min Wang, Lena Nguyen, Nirosh Mataraarachchi, Jie Wang, Yusu Gu, Andrew McCulloch, Kirk L. Peterson, and Farah Sheikh. Plakophilin 2 gene therapy prevents and rescues arrhythmogenic right ventricular cardiomyopathy in a mouse model harboring patient genetics. Nature Cardiovascular Research, 2:1246-1261, Dec 2023. URL: https://doi.org/10.1038/s44161-023-00370-3, doi:10.1038/s44161-023-00370-3. This article has 67 citations and is from a peer-reviewed journal.

31. (wu2024aav9pkp2improvesheart pages 2-3): Iris Wu, Aliya Zeng, Amara Greer-Short, J. Alex Aycinena, Anley E. Tefera, Reva Shenwai, Farshad Farshidfar, Melissa Van Pell, Emma Xu, Chris Reid, Neshel Rodriguez, Beatriz Lim, Tae Won Chung, Joseph Woods, Aquilla Scott, Samantha Jones, Cristina Dee-Hoskins, Carolina G. Gutierrez, Jessie Madariaga, Kevin Robinson, Yolanda Hatter, Renee Butler, Stephanie Steltzer, Jaclyn Ho, James R. Priest, Xiaomei Song, Frank Jing, Kristina Green, Kathryn N. Ivey, Timothy Hoey, Jin Yang, and Zhihong Jane Yang. Aav9:pkp2 improves heart function and survival in a pkp2-deficient mouse model of arrhythmogenic right ventricular cardiomyopathy. Communications Medicine, Mar 2024. URL: https://doi.org/10.1038/s43856-024-00450-w, doi:10.1038/s43856-024-00450-w. This article has 50 citations and is from a peer-reviewed journal.

32. (song2024multiomicsanalysisreveals pages 9-14): Rui Song, Haiyan Wu, Lihui Yu, Jingning Yu, WenHui Yang, WenJun Wu, Fei Sun, and Haizhen Wang. Multiomics analysis reveals extensive remodeling of the extracellular matrix and cellular metabolism due to plakophilin-2 knockdown in guinea pigs. bioRxiv, Mar 2024. URL: https://doi.org/10.1101/2024.03.11.584401, doi:10.1101/2024.03.11.584401. This article has 1 citations.

33. (wu2024aav9pkp2improvesheart pages 1-2): Iris Wu, Aliya Zeng, Amara Greer-Short, J. Alex Aycinena, Anley E. Tefera, Reva Shenwai, Farshad Farshidfar, Melissa Van Pell, Emma Xu, Chris Reid, Neshel Rodriguez, Beatriz Lim, Tae Won Chung, Joseph Woods, Aquilla Scott, Samantha Jones, Cristina Dee-Hoskins, Carolina G. Gutierrez, Jessie Madariaga, Kevin Robinson, Yolanda Hatter, Renee Butler, Stephanie Steltzer, Jaclyn Ho, James R. Priest, Xiaomei Song, Frank Jing, Kristina Green, Kathryn N. Ivey, Timothy Hoey, Jin Yang, and Zhihong Jane Yang. Aav9:pkp2 improves heart function and survival in a pkp2-deficient mouse model of arrhythmogenic right ventricular cardiomyopathy. Communications Medicine, Mar 2024. URL: https://doi.org/10.1038/s43856-024-00450-w, doi:10.1038/s43856-024-00450-w. This article has 50 citations and is from a peer-reviewed journal.

34. (NCT07050160 chunk 1):  Long-term Follow-up Study of Gene Therapy for Arrhythmogenic Cardiomyopathy Due to a Plakophilin-2 Pathogenic Variant. Lexeo Therapeutics. 2025. ClinicalTrials.gov Identifier: NCT07050160