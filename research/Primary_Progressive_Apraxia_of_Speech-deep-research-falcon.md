---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-05T23:12:16.511317'
end_time: '2026-05-05T23:25:58.012495'
duration_seconds: 821.5
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Primary Progressive Apraxia of Speech
  mondo_id: ''
  category: Neurodegenerative Disease
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 57
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Primary Progressive Apraxia of Speech
- **MONDO ID:**  (if available)
- **Category:** Neurodegenerative Disease

## Research Objectives

Please provide a comprehensive research report on **Primary Progressive Apraxia of Speech** covering all of the
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
- **Disease Name:** Primary Progressive Apraxia of Speech
- **MONDO ID:**  (if available)
- **Category:** Neurodegenerative Disease

## Research Objectives

Please provide a comprehensive research report on **Primary Progressive Apraxia of Speech** covering all of the
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


# Comprehensive Research Report: Primary Progressive Apraxia of Speech (PPAOS)

## Executive summary
Primary progressive apraxia of speech (PPAOS) is a neurodegenerative clinical syndrome in which apraxia of speech (AOS)—a disorder of speech motor planning/programming—presents as the dominant deficit, with no more than equivocal aphasia at diagnosis. It is strongly associated with degeneration of premotor/supplementary motor speech networks and is most commonly linked to 4-repeat (4R) tauopathies (notably PSP/CBD), although rare cases can arise from TDP‑43 pathology. Recent (2023–2024) work has added: (i) the first population-based incidence estimate; (ii) expanded PET biomarker characterization (amyloid/tau) with clinicopathologic correlation; (iii) longitudinal data describing evolution to corticobasal syndrome (CBS) and PSP-like phenotypes; and (iv) early “digital biomarker” approaches (automatic speech recognition) for severity quantification. (duffy2021primaryprogressiveapraxia pages 4-6, josephs2012characterizinganeurodegenerative pages 1-2, turcano2024incidenceofprimary pages 2-4, tetzloff2023amyloidandtau pages 1-3, garciaguaqueta2024progressiontocorticobasal pages 1-3, tetzloff2024automaticspeechrecognition pages 1-2)

---

## 1. Disease information
### 1.1 Concise overview (current understanding)
**PPAOS** is a progressive neurodegenerative syndrome defined by an insidious onset and gradual worsening of apraxia of speech, in which **AOS is the primary or dominant feature** and **aphasia is absent or no more than equivocal** at diagnosis. Dysarthria may co-occur but should not be more severe than AOS at presentation. (duffy2021primaryprogressiveapraxia pages 4-6, duffy2021primaryprogressiveapraxia pages 1-4)

In foundational work establishing PPAOS as a distinct syndrome, Josephs et al. identified individuals with progressive AOS **without signs of aphasia**, supporting that motor-speech neurodegeneration can present outside the formal primary progressive aphasia (PPA) construct; neuroimaging localized changes to **superior lateral premotor cortex and supplementary motor area (SMA)**. (josephs2012characterizinganeurodegenerative pages 1-2, josephs2012characterizinganeurodegenerative media 644ff289)

**Direct abstract-supported quote (foundational definition):** Josephs et al. (2012) state that they identified subjects with AOS “**without any signs of aphasia** … hence, none met criteria for primary progressive aphasia,” supporting PPAOS as a distinct syndrome. (josephs2012characterizinganeurodegenerative pages 1-2)

### 1.2 Key identifiers (OMIM/Orphanet/ICD/MeSH/MONDO)
Within the retrieved primary literature and clinical-trial record used here, explicit **MONDO, OMIM, Orphanet, ICD‑10/ICD‑11, or MeSH identifiers were not reported**. Therefore, these identifiers cannot be reliably provided from tool-retrieved evidence in this run. (duffy2021primaryprogressiveapraxia pages 4-6, josephs2012characterizinganeurodegenerative pages 1-2)

### 1.3 Synonyms / alternative names
Commonly used related labels include **progressive apraxia of speech (PAOS)** as a broader category (AOS due to neurodegeneration) and **primary progressive apraxia of speech (PPAOS)** when AOS occurs without more than equivocal aphasia at diagnosis. (duffy2021primaryprogressiveapraxia pages 4-6, duffy2021primaryprogressiveapraxia pages 1-4)

### 1.4 Evidence source types
Evidence summarized here derives from:
- **Human clinical cohorts** with longitudinal follow-up and multimodal neuroimaging. (josephs2012characterizinganeurodegenerative pages 1-2, josephs2014theevolutionof pages 1-2)
- **Population-based epidemiology** (Rochester Epidemiology Project). (turcano2024incidenceofprimary pages 2-4)
- **Clinicopathologic/autopsy studies** and PET-to-pathology comparisons. (tetzloff2023amyloidandtau pages 3-4, turcano2024incidenceofprimary pages 6-7)
- **ClinicalTrials.gov interventional record** for neuromodulation. (NCT03028324 chunk 1)

---

## 2. Etiology
### 2.1 Primary causal factors (mechanistic/biologic)
PPAOS is most commonly considered a **frontotemporal lobar degeneration (FTLD)-spectrum** syndrome with frequent association to **4R tauopathies**, particularly **progressive supranuclear palsy (PSP)** and **corticobasal degeneration (CBD)**. (botha2019primaryprogressiveaphasias pages 9-11, tetzloff2023amyloidandtau pages 1-3, turcano2024incidenceofprimary pages 6-7)

However, etiologic heterogeneity exists: a 2024 autopsy case demonstrated **TDP‑43 Type A** as the primary pathology producing a PPAOS phenotype, showing that PPAOS is **not pathognomonic for 4R tau**. (meade2024primaryprogressiveapraxia pages 1-3)

### 2.2 Risk factors
**Age:** Onset is typically later-life; in cohort summaries, about **two-thirds report onset after age 65**, though reported range spans the 3rd to 9th decades. (duffy2021primaryprogressiveapraxia pages 6-8)

**Sex:** Review-level evidence suggests **men and women are affected about equally**, although small population-based samples can deviate (e.g., 2/2 male in one incidence cohort). (duffy2021primaryprogressiveapraxia pages 6-8, turcano2024incidenceofprimary pages 2-4)

**Family history/genetic predisposition:** Cohort synthesis notes ~**25%** report a family history of neurodegenerative disease, but only ~**5%** have multiple affected first-degree relatives; and at the time of that synthesis, no clear evidence supported increased likelihood of a causal mutation. (duffy2021primaryprogressiveapraxia pages 6-8)

### 2.3 Protective factors
No protective genetic variants or environmental protective factors were identified in the retrieved evidence. (duffy2021primaryprogressiveapraxia pages 6-8)

### 2.4 Gene–environment interactions
No gene–environment interaction data were identified in the retrieved evidence. (duffy2021primaryprogressiveapraxia pages 6-8)

---

## 3. Phenotypes
### 3.1 Core motor-speech phenotype (symptoms/signs)
AOS in PPAOS is characterized by slow speech rate and motor planning/programming signs including **articulatory distortions**, **distorted sound substitutions**, **syllable segmentation**, and **trial-and-error articulatory groping**. (josephs2012characterizinganeurodegenerative pages 1-2, botha2019primaryprogressiveaphasias pages 6-7)

### 3.2 Subtypes (phonetic vs prosodic predominance)
Clinical subtyping described in cohort synthesis includes **phonetic** and **prosodic** predominant presentations, with potential evolution to **mixed** as severity increases. In one cohort synthesis, subtype proportions were approximately **prosodic 57%**, **phonetic 29%**, **mixed 14%**; dysarthria was present at initial assessment in **~30%**. (duffy2021primaryprogressiveapraxia pages 8-10, duffy2021primaryprogressiveapraxia pages 16-18)

### 3.3 Common comorbid/late-emerging phenotypes
Longitudinal cohorts and case series document evolution beyond isolated AOS:
- **Aphasia** develops in a substantial minority over years (reported ~40–50% by ~5 years in synthesis). (duffy2021primaryprogressiveapraxia pages 18-20)
- **Dysarthria** increases with disease duration (synthesis and case series). (utianski2018clinicalprogressionin pages 6-8, duffy2021primaryprogressiveapraxia pages 18-20)
- **Parkinsonism / Parkinson-plus features** frequently emerge; in one >6-year cohort, **100%** developed Parkinson-plus features and **75%** met probable PSP criteria. (seckin2020theevolutionof pages 1-2)
- **Dysphagia** may develop, often later, and is prominent in PSP-like evolution. (josephs2014theevolutionof pages 1-2, utianski2018clinicalprogressionin pages 6-8)
- **CBS features** (e.g., limb apraxia, nonverbal oral apraxia) can emerge; in a 2024 cohort, **82/140** progressed to possible CBS and **4/140** to probable CBS. (garciaguaqueta2024progressiontocorticobasal pages 1-3)

### 3.4 Quality-of-life / function
Functional communication impact is substantial; in a detailed case series, patients required **augmentative and alternative communication (AAC)** between **7–10 years** post-onset. (utianski2018clinicalprogressionin pages 6-8, duffy2021primaryprogressiveapraxia pages 18-20)

### 3.5 Suggested HPO terms (mapping suggestions)
The retrieved evidence did not provide formal HPO mappings; the following are suggested **based on described clinical features** (conceptual mapping; not asserted as curated HPO annotations):
- Apraxia of speech (concept) (josephs2012characterizinganeurodegenerative pages 1-2)
- Dysarthria (utianski2018clinicalprogressionin pages 6-8)
- Bradykinesia / parkinsonism (seckin2020theevolutionof pages 1-2)
- Dysphagia (josephs2014theevolutionof pages 1-2)
- Aphasia / agrammatism (late-emerging in some) (duffy2021primaryprogressiveapraxia pages 18-20)
- Limb apraxia / ideomotor apraxia (CBS evolution) (turcano2024incidenceofprimary pages 6-7, garciaguaqueta2024progressiontocorticobasal pages 1-3)

---

## 4. Genetic / molecular information
### 4.1 Causal genes and variants
PPAOS is typically sporadic in the cohort syntheses; nevertheless, a 2024 autopsy case of PPAOS due to TDP‑43 Type A reported a **GRN sequence variation: c.1A>C (p.Met1)**, highlighted as a clue to atypical neuropathophysiology. (meade2024primaryprogressiveapraxia pages 1-3)

No additional validated causal genes, variant classes, or allele frequencies were available in the retrieved evidence for PPAOS as a standalone syndrome. (duffy2021primaryprogressiveapraxia pages 6-8, meade2024primaryprogressiveapraxia pages 1-3)

### 4.2 Molecular pathology (proteinopathies)
- **Most common:** 4R tauopathy (PSP, CBD) in clinicopathologic series and cohort syntheses. (botha2019primaryprogressiveaphasias pages 9-11, tetzloff2023amyloidandtau pages 3-4, turcano2024incidenceofprimary pages 6-7)
- **Less common but documented:** TDP‑43 Type A in at least one autopsy-confirmed PPAOS case. (meade2024primaryprogressiveapraxia pages 1-3)

---

## 5. Environmental information
No specific toxins, lifestyle factors, or infectious triggers were identified in the retrieved evidence as causal contributors to PPAOS. A 2021 synthesis reported **no clear socioeconomic, educational, or environmental risk factors**. (duffy2021primaryprogressiveapraxia pages 6-8)

---

## 6. Mechanism / pathophysiology
### 6.1 Neuroanatomic and network-level mechanism (causal chain)
A widely supported mechanistic chain is:
1) Neurodegenerative pathology (often 4R tau) preferentially affects **premotor/SMA** speech-motor planning regions and connected white matter. (josephs2012characterizinganeurodegenerative pages 1-2, josephs2012characterizinganeurodegenerative media 644ff289)
2) Degeneration in these regions disrupts **speech motor planning/programming**, producing hallmark AOS features (distortions, segmentation, groping) and reduced rate. (josephs2012characterizinganeurodegenerative pages 1-2)
3) With spread to motor cortex, basal ganglia, and midbrain, additional motor features emerge (parkinsonism, dysarthria, dysphagia) and some patients develop PSP/CBS phenotypes. (josephs2014theevolutionof pages 1-2, seckin2020theevolutionof pages 1-2)

**Imaging evidence:** Josephs et al. demonstrated focal grey-matter atrophy and hypometabolism in **superior lateral premotor cortex and SMA**, with corresponding white-matter loss extending to inferior premotor cortex and corpus callosum. (josephs2012characterizinganeurodegenerative pages 1-2, josephs2012characterizinganeurodegenerative media 644ff289)

### 6.2 Proposed ontology terms (suggestions)
Because formal GO/CL/UBERON annotations were not provided in retrieved texts, the following are **conceptual suggestions** aligned to reported anatomy/mechanism:
- **UBERON (anatomy) suggestions:** supplementary motor area; premotor cortex; precentral gyrus; basal ganglia; midbrain (josephs2012characterizinganeurodegenerative pages 1-2, josephs2014theevolutionof pages 1-2)
- **GO Biological Process suggestions:** motor planning; speech production; regulation of voluntary motor control; tau-protein related neurodegeneration (supported indirectly via tauopathy association) (tetzloff2023amyloidandtau pages 1-3, turcano2024incidenceofprimary pages 6-7)
- **CL (cell types) suggestions:** cortical excitatory neurons; astrocytes/oligodendrocytes (relevant to tauopathies/white matter changes but not explicitly detailed in retrieved evidence) (josephs2012characterizinganeurodegenerative media 644ff289)

### 6.3 Biomarkers relevant to mechanism
**Amyloid and tau PET in AOS-PAA spectrum:** In a 2023 cohort (n=65), roughly **half** were positive for at least one biomarker (Aβ or tau), yet biomarker status did not align with clinical presentation, supporting that AD biomarkers may often reflect co-pathology rather than primary cause. (tetzloff2023amyloidandtau pages 1-3)

---

## 7. Anatomical structures affected
### 7.1 Primary structures
Consistent structural/metabolic involvement centers on:
- **Superior lateral premotor cortex** and **supplementary motor area (SMA)**. (josephs2012characterizinganeurodegenerative pages 1-2, josephs2012characterizinganeurodegenerative media 644ff289)

### 7.2 Secondary spread with progression
Longitudinal imaging shows spread to **prefrontal and motor cortex**, **basal ganglia**, and **midbrain**, aligning with emergence of parkinsonism/PSP-like features. (josephs2014theevolutionof pages 1-2)

---

## 8. Temporal development
### 8.1 Onset
PPAOS has **insidious onset** with progressive speech impairment. Onset age is variable; cohort synthesis notes onset commonly after 65, while population-based incidence cases had median onset in the late 70s (noting small-n uncertainty). (duffy2021primaryprogressiveapraxia pages 4-6, turcano2024incidenceofprimary pages 2-4)

### 8.2 Progression and staging (natural history)
Key longitudinal observations include:
- Some patients remain predominantly speech-impaired for years, while others evolve to PSP-like or CBS phenotypes. (josephs2014theevolutionof pages 1-2, garciaguaqueta2024progressiontocorticobasal pages 1-3)
- In one 13-person longitudinal imaging cohort, **5/13** progressed within ~5 years to a **PSP-like syndrome** with severe parkinsonism, near mutism, dysphagia, gaze palsy, and falls. (josephs2014theevolutionof pages 1-2)
- In a >6-year series, **100%** developed Parkinson-plus features; parkinsonism/limb apraxia/ocular impairment tended to emerge around **4–5 years** after onset. (seckin2020theevolutionof pages 1-2)

---

## 9. Inheritance and population
### 9.1 Epidemiology (incidence/prevalence)
**Incidence (2024, population-based):** The first formal incidence estimate (Olmsted County, MN, 2011–2022) reported **PPAOS incidence 0.14 per 100,000 person-years** (95% CI 0.02–0.55), based on **2 identified cases** (rare disease; wide CI). (turcano2024incidenceofprimary pages 2-4, turcano2024incidenceofprimary pages 1-2)

**Prevalence (review estimate):** A synthesis cited prevalence of approximately **2 per 100,000** for PPAOS alone, and **~4.4 per 100,000** when including PAOS with mild aphasia, while noting earlier lack of formal epidemiologic studies. (duffy2021primaryprogressiveapraxia pages 6-8)

### 9.2 Demographics
- **Sex:** Review synthesis suggests roughly equal sex distribution overall, but local incidence cohorts may show skew due to very small numbers. (duffy2021primaryprogressiveapraxia pages 6-8, turcano2024incidenceofprimary pages 2-4)
- **Age distribution:** Onset commonly after 65; population-based PPAOS cases had median onset age **77** (n=2). (duffy2021primaryprogressiveapraxia pages 6-8, turcano2024incidenceofprimary pages 2-4)

---

## 10. Diagnostics
### 10.1 Clinical diagnosis
Clinical diagnosis depends on identifying AOS as the dominant deficit and distinguishing it from dysarthria and aphasia. Core AOS markers include inconsistent speech sound errors/distortions and groping/segmentation phenomena. (duffy2021primaryprogressiveapraxia pages 4-6, josephs2012characterizinganeurodegenerative pages 1-2)

A 2021 synthesis highlights use of the **Apraxia of Speech Rating Scale (ASRS)** as a perceptual tool (13 items, scored 0–4) for quantifying AOS features and tracking progression. (duffy2021primaryprogressiveapraxia pages 8-10)

### 10.2 Neuroimaging
- **MRI/voxel-based morphometry:** focal atrophy in superior lateral premotor cortex and SMA. (josephs2012characterizinganeurodegenerative pages 1-2, josephs2012characterizinganeurodegenerative media 644ff289)
- **FDG-PET:** focal hypometabolism in premotor/SMA regions; in population incidence cases, hypometabolism involved posterior superior frontal regions including premotor cortices and SMA. (turcano2024incidenceofprimary pages 6-7)

### 10.3 Molecular biomarkers and differential diagnosis
Amyloid/tau PET can detect AD co-pathology in some individuals on the AOS-PAA spectrum, but PET positivity may not map cleanly to the clinical syndrome and may reflect co-pathology or tracer limitations. (tetzloff2023amyloidandtau pages 1-3, tetzloff2023amyloidandtau pages 3-4)

### 10.4 Differential diagnosis
Key distinctions are:
- **Aphasia-driven syndromes (PPA variants)** vs AOS-dominant PPAOS; PPAOS may be misclassified as nonfluent PPA if motor-speech impairment is mistaken for language impairment. (duffy2015primaryprogressiveapraxia pages 1-2, botha2019primaryprogressiveaphasias pages 9-11)
- **Dysarthria** vs AOS: dysarthrias lack some hallmark planning/programming signs such as distorted substitutions and trial-and-error groping. (josephs2012characterizinganeurodegenerative pages 1-2)

---

## 11. Outcome / prognosis
### 11.1 Survival / mortality
A cohort synthesis reported **estimated survival about 9 years from symptom onset** for PPAOS (noting that survival varies by spectrum diagnosis). (duffy2021primaryprogressiveapraxia pages 18-20)

### 11.2 Complications
Later-stage complications include severe communication impairment (often requiring AAC), parkinsonism/PSP-like features, dysphagia with choking, falls, and development of CBS features in a subset. (josephs2014theevolutionof pages 1-2, utianski2018clinicalprogressionin pages 6-8, garciaguaqueta2024progressiontocorticobasal pages 1-3)

### 11.3 Prognostic factors
Disease severity relates to mortality risk in synthesis: hazard ratio **1.35 per 1-point increase** on a 0–4 AOS severity scale (as reported in the synthesis). (duffy2021primaryprogressiveapraxia pages 16-18)

---

## 12. Treatment
### 12.1 Pharmacotherapy
No disease-modifying drug therapy has proven efficacy for PPAOS; management is primarily behavioral/supportive. (duffy2021primaryprogressiveapraxia pages 22-24, wauters2024behavioraltreatmentfor pages 2-4)

### 12.2 Supportive and rehabilitative care (real-world implementation)
Behavioral speech-language therapy is considered the mainstay, with goals often focused on maximizing communication rather than restoration; approaches used in progressive AOS/nonfluent PPA include script training and structured oral reading/home practice, with limited but positive small-study evidence. (duffy2021primaryprogressiveapraxia pages 22-24, henry2013treatmentforapraxia pages 1-2)

**Evidence gap highlighted in 2024:** A systematic review concluded that although behavioral therapy evidence exists for PPA broadly, **“no studies used the diagnostic label PPAOS”** and “**treatment for PPAOS awaits systematic investigation**.” (wauters2024behavioraltreatmentfor pages 1-2)

### 12.3 Neuromodulation / interventional trials
A PPAOS-specific neuromodulation trial was registered:
- **NCT03028324** (University of Miami): single-group, open-label high-frequency rTMS (10 sessions/2 weeks), **terminated** for recruitment/personnel issues; **enrollment n=4**; primary outcome ASRS change at 4 weeks. (NCT03028324 chunk 1)

### 12.4 Suggested MAXO terms (conceptual)
Formal MAXO terms were not provided in retrieved texts; suggested action concepts include: speech-language therapy; augmentative and alternative communication; repetitive transcranial magnetic stimulation. (utianski2018clinicalprogressionin pages 6-8, NCT03028324 chunk 1)

---

## 13. Prevention
No established primary prevention exists for PPAOS in the retrieved evidence. Secondary/tertiary “prevention” is best framed as early recognition, early referral to speech-language pathology, anticipatory AAC planning, and management of dysphagia/fall risk as parkinsonism/PSP features emerge. (duffy2021primaryprogressiveapraxia pages 22-24, josephs2014theevolutionof pages 1-2)

---

## 14. Other species / natural disease
No naturally occurring non-human PPAOS analogs were identified in the retrieved evidence. (duffy2021primaryprogressiveapraxia pages 4-6)

---

## 15. Model organisms
No PPAOS-specific model organisms were identified in the retrieved evidence. Given frequent links to 4R tauopathies and PSP/CBD, mechanistic work may leverage tauopathy models, but direct recapitulation of human speech motor planning deficits is inherently limited in non-human systems (not directly evidenced in retrieved texts). (tetzloff2023amyloidandtau pages 1-3, turcano2024incidenceofprimary pages 6-7)

---

## Recent developments and “latest research” highlights (2023–2024)
1) **Epidemiology (2024):** first incidence estimate for PPAOS: **0.14 per 100,000 person-years** (Olmsted County, 2011–2022). (turcano2024incidenceofprimary pages 2-4)
2) **Clinicopathology & biomarkers (2023–2024):** PET studies show frequent biomarker positivity but limited clinical correlation; autopsy series support predominant PSP/CBD (4R tau) with heterogeneity, including TDP‑43 Type A in a 2024 PPAOS autopsy case. (tetzloff2023amyloidandtau pages 3-4, meade2024primaryprogressiveapraxia pages 1-3, turcano2024incidenceofprimary pages 6-7)
3) **Progression phenotyping (2024):** large longitudinal cohort quantifies progression to CBS (possible/probable) and identifies common emergent CBS features (asymmetric akinesia, nonverbal oral apraxia, limb apraxia). (garciaguaqueta2024progressiontocorticobasal pages 1-3)
4) **Real-world measurement innovation (2024):** automatic speech recognition (wav2vec 2.0) demonstrates strong discrimination of PPAOS vs controls using WER (0.88 vs 0.33; threshold 0.44) and correlation with severity, supporting feasibility of scalable speech monitoring. (tetzloff2024automaticspeechrecognition pages 5-8, tetzloff2024automaticspeechrecognition pages 1-2)

---

## Evidence summary table
| Topic | Key findings (include numeric stats) | Study type/population | Publication (authors, journal) | Year/month | DOI/URL | PMID | Citation context id |
|---|---|---|---|---|---|---|---|
| Definition/criteria | PPAOS defined as a neurodegenerative syndrome in which apraxia of speech is the dominant feature with no more than equivocal aphasia; core signs include slow speech rate, articulatory distortions, distorted substitutions, segmentation, and groping. Initial series identified 12 patients with isolated AOS without aphasia; imaging localized disease to superior lateral premotor cortex and supplementary motor area. | Foundational prospective clinical-imaging cohort; 37 neurodegenerative speech/language cases, 12 classified as PPAOS | Josephs KA et al., *Brain* | 2012/Mar | 10.1093/brain/aws032 / https://doi.org/10.1093/brain/aws032 | PMID not in retrieved text | (josephs2012characterizinganeurodegenerative pages 1-2, josephs2012characterizinganeurodegenerative media 644ff289) |
| Definition/criteria | Review synthesizes recognition, diagnosis, subtypes, care, and distinction from aphasia/dysarthria; notes dysarthria can be present but should not exceed AOS severity at presentation. Reports PPAOS as a recognizable syndrome linked to tauopathies including PSP/CBD. | Narrative review of clinical, imaging, pathology, and care literature | Duffy JR, Utianski RL, Josephs KA, *Aphasiology* | 2021/Jul | 10.1080/02687038.2020.1787732 / https://doi.org/10.1080/02687038.2020.1787732 | PMID not in retrieved text | (duffy2021primaryprogressiveapraxia pages 4-6, duffy2021primaryprogressiveapraxia pages 1-4) |
| Epidemiology | First formal population incidence estimate for PPAOS: 0.14 per 100,000 person-years (95% CI 0.02-0.55) in Olmsted County, MN, 2011-2022; only 2 PPAOS cases identified. Median onset age for PPAOS cases 77 years; both cases male. | Population-based retrospective cohort using Rochester Epidemiology Project; 10 total progressive speech/language cases, 2 PPAOS | Turcano P et al., *Neurology* | 2024/Aug | 10.1212/WNL.0000000000209693 / https://doi.org/10.1212/wnl.0000000000209693 | PMID not in retrieved text | (turcano2024incidenceofprimary pages 2-4, turcano2024incidenceofprimary pages 1-2) |
| Epidemiology | Earlier review noted no formal epidemiologic studies at that time; estimated prevalence about 2 per 100,000 for PPAOS alone and ~4.4 per 100,000 when PPAOS plus PAOS with mild aphasia are included. About two-thirds onset after age 65; men and women affected about equally. | Review summarizing prior cohort evidence | Duffy JR, Utianski RL, Josephs KA, *Aphasiology* | 2021/Jul | 10.1080/02687038.2020.1787732 / https://doi.org/10.1080/02687038.2020.1787732 | PMID not in retrieved text | (duffy2021primaryprogressiveapraxia pages 6-8) |
| Pathology/biomarkers | PPAOS/AOS-PAA spectrum is most often associated with 4R tauopathies (PSP, CBD, Pick disease in some reports). In 65 patients, ~42% were positive on at least one AD biomarker; only 8/65 were amyloid+ and tau+, suggesting AD is often co-pathology rather than primary cause. Autopsy subset showed predominant non-AD pathology, especially PSP (n=8) and CBD (n=6). | Cross-sectional biomarker study; 65 AOS-PAA spectrum patients with PiB and flortaucipir PET; autopsy subset n=19 | Tetzloff KA et al., *Journal of Alzheimer's Disease* | 2023/Dec | 10.3233/JAD-230912 / https://doi.org/10.3233/JAD-230912 | PMID not in retrieved text | (tetzloff2023amyloidandtau pages 1-3, tetzloff2023amyloidandtau pages 3-4, tetzloff2023amyloidandtau pages 7-11) |
| Pathology/biomarkers | Autopsy case demonstrated that PPAOS can be caused by TDP-43 Type A rather than 4R tau. Ante mortem clues included GRN c.1A>C (p.Met1), asymmetric temporoparietal involvement, FDG-PET hypometabolism, and only low-level tau-PET signal. | Single autopsy-confirmed case report with longitudinal clinical/imaging follow-up | Meade G et al., *Neurology Genetics* | 2024/Apr | 10.1212/NXG.0000000000200134 / https://doi.org/10.1212/nxg.0000000000200134 | PMID not in retrieved text | (meade2024primaryprogressiveapraxia pages 1-3) |
| Pathology/biomarkers | In the population-based Olmsted County series, both autopsied PPAOS cases had PSP-type 4R tau pathology; low AD neuropathologic change in all but one, and no alpha-synuclein or TDP-43 pathology. FDG-PET showed left-predominant posterior superior frontal/premotor/SMA hypometabolism. | Population-based cohort with autopsy/imaging subset; 2 autopsied PPAOS cases | Turcano P et al., *Neurology* | 2024/Aug | 10.1212/WNL.0000000000209693 / https://doi.org/10.1212/wnl.0000000000209693 | PMID not in retrieved text | (turcano2024incidenceofprimary pages 6-7) |
| Progression/natural history | Over ~2.4 years, all 13 subjects developed extrapyramidal signs; 5/13 progressed within about 5 years to a PSP-like syndrome with severe parkinsonism, near mutism, dysphagia/choking, gaze palsy/slowing, falls, urinary incontinence. Imaging rates: whole-brain atrophy ~1.5%/year vs 0.4% in controls; ventricular expansion ~8.0%/year vs 3.3%; midbrain atrophy ~1.5%/year vs 0.1%. | Longitudinal imaging-natural history study; 13 PPAOS subjects | Josephs KA et al., *Brain* | 2014/Oct | 10.1093/brain/awu223 / https://doi.org/10.1093/brain/awu223 | PMID not in retrieved text | (josephs2014theevolutionof pages 1-2) |
| Progression/natural history | In four detailed cases followed 5-6 years, all developed aphasia and dysarthria; 3/4 developed mild-moderate parkinsonism; 2/4 developed dysphagia; 1 developed corticobasal syndrome at 15 years. AAC was required between 7 and 10 years post-onset. | Longitudinal case series; 4 PPAOS patients | Utianski RL et al., *American Journal of Speech-Language Pathology* | 2018/Nov | 10.1044/2018_AJSLP-17-0227 / https://doi.org/10.1044/2018_AJSLP-17-0227 | PMID not in retrieved text | (utianski2018clinicalprogressionin pages 6-8, utianski2018clinicalprogressionin pages 1-2, utianski2018clinicalprogressionin pages 8-10) |
| Progression/natural history | In an >6-year cohort, all patients developed a Parkinson-plus syndrome (100%); 75% met probable PSP criteria and 3 met possible CBS. Parkinsonism, limb apraxia, and ocular motor impairment tended to appear ~4-5 years after onset. | Longitudinal cohort; 8 PPAOS patients followed >6 years | Seckin ZI et al., *Parkinsonism & Related Disorders* | 2020/Dec | 10.1016/j.parkreldis.2020.09.039 / https://doi.org/10.1016/j.parkreldis.2020.09.039 | PMID not in retrieved text | (seckin2020theevolutionof pages 1-2) |
| Progression/natural history | In a larger 2024 cohort of PPAOS/nfvPPA, 82/140 progressed to possible CBS and 4/140 to probable CBS. Common emergent CBS features were asymmetric akinesia, nonverbal oral apraxia, and limb apraxia; nfvPPA progressed earlier than PPAOS. | Longitudinal cohort; 140 patients with PPAOS or nfvPPA | Garcia-Guaqueta DP et al., *Journal of Neurology* | 2024/Apr | 10.1007/s00415-024-12344-x / https://doi.org/10.1007/s00415-024-12344-x | PMID not in retrieved text | (garciaguaqueta2024progressiontocorticobasal pages 1-3) |
| Treatment evidence | Systematic review of 103 studies (626 participants) found positive behavioral treatment effects in PPA overall, but explicitly concluded that no studies used the diagnostic label PPAOS and that treatment for PPAOS awaits systematic investigation. Among 45 higher-quality studies, all reported improvement on a primary outcome; many showed generalization, maintenance, and social validity. | Systematic review of behavioral intervention studies in PPA/PPAOS literature | Wauters LD et al., *Neuropsychology Review* | 2024/Oct | 10.1007/s11065-023-09607-1 / https://doi.org/10.1007/s11065-023-09607-1 | PMID not in retrieved text | (wauters2024behavioraltreatmentfor pages 1-2, wauters2024behavioraltreatmentfor pages 27-29, wauters2024behavioraltreatmentfor pages 29-30) |
| Treatment evidence | Review of care notes no disease-modifying drugs for PPAOS/PPA. Behavioral management is mainstay; script training, oral reading/home practice, and AAC are used pragmatically, while evidence for noninvasive brain stimulation remains insufficient beyond behavioral therapy. Estimated survival about 9 years from symptom onset for PPAOS. | Narrative review of diagnosis and care literature | Duffy JR, Utianski RL, Josephs KA, *Aphasiology* | 2021/Jul | 10.1080/02687038.2020.1787732 / https://doi.org/10.1080/02687038.2020.1787732 | PMID not in retrieved text | (duffy2021primaryprogressiveapraxia pages 18-20, duffy2021primaryprogressiveapraxia pages 22-24) |
| Treatment evidence | Preliminary single-case evidence in nonfluent PPA with AOS: structured oral reading reduced speech errors, generalized to repetition and connected speech, and gains were maintained at 1 year post-treatment. | Single-case behavioral intervention in mild AOS/nonfluent PPA | Henry ML et al., *Behavioural Neurology* | 2013 | 10.3233/BEN-2012-120260 / https://doi.org/10.3233/ben-2012-120260 | PMID not in retrieved text | (henry2013treatmentforapraxia pages 1-2) |
| Digital tools | Readily available ASR (wav2vec 2.0) in 45 PPAOS patients vs 22 controls yielded mean word error rate (WER) 0.88 vs 0.33; WER threshold 0.44 best separated patients from controls. WER correlated with AOS severity and human-transcribed error proportion (r=0.71, p<0.0001), but ASR did not distinguish phonetic/prosodic subtypes and showed poor agreement with humans for fine-grained error counts. | Cross-sectional digital biomarker/AI feasibility study; 45 PPAOS, 22 controls | Tetzloff KA et al., *Journal of Speech, Language, and Hearing Research* | 2024/Sep | 10.1044/2024_JSLHR-24-00049 / https://doi.org/10.1044/2024_JSLHR-24-00049 | PMID not in retrieved text | (tetzloff2024automaticspeechrecognition pages 5-8, tetzloff2024automaticspeechrecognition pages 1-2) |


*Table: This table summarizes foundational and recent sources on Primary Progressive Apraxia of Speech, organized by major knowledge-base topics. It highlights definitions, incidence, pathology, progression, treatment evidence gaps, and newer digital assessment tools with numeric findings and citation context IDs.*

---

## Key figure evidence (neuroanatomic correlate)
Josephs et al. (2012) provide imaging evidence of focal atrophy and hypometabolism in superior lateral premotor cortex and SMA in PPAOS versus controls. (josephs2012characterizinganeurodegenerative media 644ff289)

---

## Notes on limitations of this report
- Several ontology identifiers (MONDO/MeSH/ICD/Orphanet/OMIM) and many ontology mappings (HPO/GO/CL/UBERON/MAXO) were **not explicitly present** in the retrieved tool evidence and therefore are provided only as **suggestions** or are left unspecified.
- Many clinical and progression estimates come from specialized referral cohorts; even the 2024 incidence estimate is based on **n=2 PPAOS cases**, leading to wide uncertainty. (turcano2024incidenceofprimary pages 2-4, duffy2021primaryprogressiveapraxia pages 18-20)


References

1. (duffy2021primaryprogressiveapraxia pages 4-6): Joseph R. Duffy, Rene L. Utianski, and Keith A. Josephs. Primary progressive apraxia of speech: from recognition to diagnosis and care. Aphasiology, 35:560-591, Jul 2021. URL: https://doi.org/10.1080/02687038.2020.1787732, doi:10.1080/02687038.2020.1787732. This article has 123 citations and is from a domain leading peer-reviewed journal.

2. (josephs2012characterizinganeurodegenerative pages 1-2): Keith A. Josephs, Joseph R. Duffy, Edythe A. Strand, Mary M. Machulda, Matthew L. Senjem, Ankit V. Master, Val J. Lowe, Clifford R. Jack, and Jennifer L. Whitwell. Characterizing a neurodegenerative syndrome: primary progressive apraxia of speech. Brain, 135:1522-1536, Mar 2012. URL: https://doi.org/10.1093/brain/aws032, doi:10.1093/brain/aws032. This article has 486 citations and is from a highest quality peer-reviewed journal.

3. (turcano2024incidenceofprimary pages 2-4): Pierpaolo Turcano, Jennifer L. Whitwell, Joseph R. Duffy, Mary M. Machulda, Aidan Mullan, Keith A. Josephs, and Rodolfo Savica. Incidence of primary progressive apraxia of speech and primary progressive aphasia in olmsted county, mn, 2011–2022. Neurology, Aug 2024. URL: https://doi.org/10.1212/wnl.0000000000209693, doi:10.1212/wnl.0000000000209693. This article has 12 citations and is from a highest quality peer-reviewed journal.

4. (tetzloff2023amyloidandtau pages 1-3): Katerina A. Tetzloff, Joseph R. Duffy, Heather M. Clark, Nha Trang Thu Pham, Mary M. Machulda, Hugo Botha, Clifford R. Jack, Dennis W. Dickson, Val J. Lowe, Keith A. Josephs, Jennifer L. Whitwell, and Rene L. Utianski. Amyloid and tau pet positivity in progressive agrammatic aphasia and apraxia of speech. Journal of Alzheimer's Disease, 96:1759-1765, Dec 2023. URL: https://doi.org/10.3233/jad-230912, doi:10.3233/jad-230912. This article has 3 citations and is from a peer-reviewed journal.

5. (garciaguaqueta2024progressiontocorticobasal pages 1-3): Danna P. Garcia-Guaqueta, Hugo Botha, Rene L. Utianski, Joseph R. Duffy, Heather M. Clark, Austin W. Goodrich, Nha Trang Thu Pham, Mary M. Machulda, Matt Baker, Rosa Rademakers, Jennifer L. Whitwell, and Keith A. Josephs. Progression to corticobasal syndrome: a longitudinal study of patients with nonfluent primary progressive aphasia and primary progressive apraxia of speech. Journal of neurology, 271:4168-4179, Apr 2024. URL: https://doi.org/10.1007/s00415-024-12344-x, doi:10.1007/s00415-024-12344-x. This article has 12 citations and is from a domain leading peer-reviewed journal.

6. (tetzloff2024automaticspeechrecognition pages 1-2): Katerina A. Tetzloff, Daniela Wiepert, Hugo Botha, Joseph R. Duffy, Heather M. Clark, Jennifer L. Whitwell, Keith A. Josephs, and Rene L. Utianski. Automatic speech recognition in primary progressive apraxia of speech. Journal of Speech, Language, and Hearing Research, 67:2964-2976, Sep 2024. URL: https://doi.org/10.1044/2024\_jslhr-24-00049, doi:10.1044/2024\_jslhr-24-00049. This article has 15 citations and is from a highest quality peer-reviewed journal.

7. (duffy2021primaryprogressiveapraxia pages 1-4): Joseph R. Duffy, Rene L. Utianski, and Keith A. Josephs. Primary progressive apraxia of speech: from recognition to diagnosis and care. Aphasiology, 35:560-591, Jul 2021. URL: https://doi.org/10.1080/02687038.2020.1787732, doi:10.1080/02687038.2020.1787732. This article has 123 citations and is from a domain leading peer-reviewed journal.

8. (josephs2012characterizinganeurodegenerative media 644ff289): Keith A. Josephs, Joseph R. Duffy, Edythe A. Strand, Mary M. Machulda, Matthew L. Senjem, Ankit V. Master, Val J. Lowe, Clifford R. Jack, and Jennifer L. Whitwell. Characterizing a neurodegenerative syndrome: primary progressive apraxia of speech. Brain, 135:1522-1536, Mar 2012. URL: https://doi.org/10.1093/brain/aws032, doi:10.1093/brain/aws032. This article has 486 citations and is from a highest quality peer-reviewed journal.

9. (josephs2014theevolutionof pages 1-2): Keith A. Josephs, Joseph R. Duffy, Edythe A. Strand, Mary M. Machulda, Matthew L. Senjem, Jeffrey L. Gunter, Christopher G. Schwarz, Robert I. Reid, Anthony J. Spychalla, Val J. Lowe, Clifford R. Jack, and Jennifer L. Whitwell. The evolution of primary progressive apraxia of speech. Brain : a journal of neurology, 137 Pt 10:2783-95, Oct 2014. URL: https://doi.org/10.1093/brain/awu223, doi:10.1093/brain/awu223. This article has 187 citations.

10. (tetzloff2023amyloidandtau pages 3-4): Katerina A. Tetzloff, Joseph R. Duffy, Heather M. Clark, Nha Trang Thu Pham, Mary M. Machulda, Hugo Botha, Clifford R. Jack, Dennis W. Dickson, Val J. Lowe, Keith A. Josephs, Jennifer L. Whitwell, and Rene L. Utianski. Amyloid and tau pet positivity in progressive agrammatic aphasia and apraxia of speech. Journal of Alzheimer's Disease, 96:1759-1765, Dec 2023. URL: https://doi.org/10.3233/jad-230912, doi:10.3233/jad-230912. This article has 3 citations and is from a peer-reviewed journal.

11. (turcano2024incidenceofprimary pages 6-7): Pierpaolo Turcano, Jennifer L. Whitwell, Joseph R. Duffy, Mary M. Machulda, Aidan Mullan, Keith A. Josephs, and Rodolfo Savica. Incidence of primary progressive apraxia of speech and primary progressive aphasia in olmsted county, mn, 2011–2022. Neurology, Aug 2024. URL: https://doi.org/10.1212/wnl.0000000000209693, doi:10.1212/wnl.0000000000209693. This article has 12 citations and is from a highest quality peer-reviewed journal.

12. (NCT03028324 chunk 1): Joyce Rios Gomes Osman. Transcranial Magnetic Stimulation (TMS) for Primary Progressive Apraxia of Speech (PPAOS). University of Miami. 2017. ClinicalTrials.gov Identifier: NCT03028324

13. (botha2019primaryprogressiveaphasias pages 9-11): Hugo Botha and Keith A. Josephs. Primary progressive aphasias and apraxia of speech. CONTINUUM: Lifelong Learning in Neurology, 25:101–127, Feb 2019. URL: https://doi.org/10.1212/con.0000000000000699, doi:10.1212/con.0000000000000699. This article has 126 citations.

14. (meade2024primaryprogressiveapraxia pages 1-3): PhD Gabriela Meade, PhD Jennifer L. Whitwell, MD Dennis W. Dickson, PhD Joseph R. Duffy, PhD Heather M. Clark, PhD MD J. Eric Ahlskog, PhD Mary M. Machulda, MD Keith A. Josephs, and PhD Rene L. Utianski. Primary progressive apraxia of speech caused by tdp-43. Neurology Genetics, Apr 2024. URL: https://doi.org/10.1212/nxg.0000000000200134, doi:10.1212/nxg.0000000000200134. This article has 4 citations.

15. (duffy2021primaryprogressiveapraxia pages 6-8): Joseph R. Duffy, Rene L. Utianski, and Keith A. Josephs. Primary progressive apraxia of speech: from recognition to diagnosis and care. Aphasiology, 35:560-591, Jul 2021. URL: https://doi.org/10.1080/02687038.2020.1787732, doi:10.1080/02687038.2020.1787732. This article has 123 citations and is from a domain leading peer-reviewed journal.

16. (botha2019primaryprogressiveaphasias pages 6-7): Hugo Botha and Keith A. Josephs. Primary progressive aphasias and apraxia of speech. CONTINUUM: Lifelong Learning in Neurology, 25:101–127, Feb 2019. URL: https://doi.org/10.1212/con.0000000000000699, doi:10.1212/con.0000000000000699. This article has 126 citations.

17. (duffy2021primaryprogressiveapraxia pages 8-10): Joseph R. Duffy, Rene L. Utianski, and Keith A. Josephs. Primary progressive apraxia of speech: from recognition to diagnosis and care. Aphasiology, 35:560-591, Jul 2021. URL: https://doi.org/10.1080/02687038.2020.1787732, doi:10.1080/02687038.2020.1787732. This article has 123 citations and is from a domain leading peer-reviewed journal.

18. (duffy2021primaryprogressiveapraxia pages 16-18): Joseph R. Duffy, Rene L. Utianski, and Keith A. Josephs. Primary progressive apraxia of speech: from recognition to diagnosis and care. Aphasiology, 35:560-591, Jul 2021. URL: https://doi.org/10.1080/02687038.2020.1787732, doi:10.1080/02687038.2020.1787732. This article has 123 citations and is from a domain leading peer-reviewed journal.

19. (duffy2021primaryprogressiveapraxia pages 18-20): Joseph R. Duffy, Rene L. Utianski, and Keith A. Josephs. Primary progressive apraxia of speech: from recognition to diagnosis and care. Aphasiology, 35:560-591, Jul 2021. URL: https://doi.org/10.1080/02687038.2020.1787732, doi:10.1080/02687038.2020.1787732. This article has 123 citations and is from a domain leading peer-reviewed journal.

20. (utianski2018clinicalprogressionin pages 6-8): Rene L. Utianski, Joseph R. Duffy, Heather M. Clark, Edythe A. Strand, Sarah M. Boland, Mary M. Machulda, Jennifer L. Whitwell, and Keith A. Josephs. Clinical progression in four cases of primary progressive apraxia of speech. American journal of speech-language pathology, 27 4:1303-1318, Nov 2018. URL: https://doi.org/10.1044/2018\_ajslp-17-0227, doi:10.1044/2018\_ajslp-17-0227. This article has 47 citations and is from a domain leading peer-reviewed journal.

21. (seckin2020theevolutionof pages 1-2): Zeynep Idil Seckin, Joseph R. Duffy, Edythe A. Strand, Heather M. Clark, Rene L. Utianski, Mary M. Machulda, Hugo Botha, Farwa Ali, Nha Trang Thu Pham, Val J. Lowe, Jennifer L. Whitwell, and Keith A. Josephs. The evolution of parkinsonism in primary progressive apraxia of speech: a 6-year longitudinal study. Parkinsonism &amp; Related Disorders, 81:34-40, Dec 2020. URL: https://doi.org/10.1016/j.parkreldis.2020.09.039, doi:10.1016/j.parkreldis.2020.09.039. This article has 38 citations and is from a peer-reviewed journal.

22. (turcano2024incidenceofprimary pages 1-2): Pierpaolo Turcano, Jennifer L. Whitwell, Joseph R. Duffy, Mary M. Machulda, Aidan Mullan, Keith A. Josephs, and Rodolfo Savica. Incidence of primary progressive apraxia of speech and primary progressive aphasia in olmsted county, mn, 2011–2022. Neurology, Aug 2024. URL: https://doi.org/10.1212/wnl.0000000000209693, doi:10.1212/wnl.0000000000209693. This article has 12 citations and is from a highest quality peer-reviewed journal.

23. (duffy2015primaryprogressiveapraxia pages 1-2): Joseph R. Duffy, Edythe A. Strand, Heather Clark, Mary Machulda, Jennifer L. Whitwell, and Keith A. Josephs. Primary progressive apraxia of speech: clinical features and acoustic and neurologic correlates. American journal of speech-language pathology, 24 2:88-100, May 2015. URL: https://doi.org/10.1044/2015\_ajslp-14-0174, doi:10.1044/2015\_ajslp-14-0174. This article has 107 citations and is from a domain leading peer-reviewed journal.

24. (duffy2021primaryprogressiveapraxia pages 22-24): Joseph R. Duffy, Rene L. Utianski, and Keith A. Josephs. Primary progressive apraxia of speech: from recognition to diagnosis and care. Aphasiology, 35:560-591, Jul 2021. URL: https://doi.org/10.1080/02687038.2020.1787732, doi:10.1080/02687038.2020.1787732. This article has 123 citations and is from a domain leading peer-reviewed journal.

25. (wauters2024behavioraltreatmentfor pages 2-4): Lisa D. Wauters, Karen Croot, Heather R. Dial, Joseph R. Duffy, Stephanie M. Grasso, Esther Kim, Kristin Schaffer Mendez, Kirrie J. Ballard, Heather M. Clark, Leeah Kohley, Laura L. Murray, Emily J. Rogalski, Mathieu Figeys, Lisa Milman, and Maya L. Henry. Behavioral treatment for speech and language in primary progressive aphasia and primary progressive apraxia of speech: a systematic review. Neuropsychology Review, 34:882-923, Oct 2024. URL: https://doi.org/10.1007/s11065-023-09607-1, doi:10.1007/s11065-023-09607-1. This article has 70 citations and is from a domain leading peer-reviewed journal.

26. (henry2013treatmentforapraxia pages 1-2): Maya L. Henry, M. Meese, S. Truong, Miranda Babiak, Bruce L. Miller, and M. Gorno-Tempini. Treatment for apraxia of speech in nonfluent variant primary progressive aphasia. Behavioural Neurology, 26:77-88, 2013. URL: https://doi.org/10.3233/ben-2012-120260, doi:10.3233/ben-2012-120260. This article has 106 citations and is from a peer-reviewed journal.

27. (wauters2024behavioraltreatmentfor pages 1-2): Lisa D. Wauters, Karen Croot, Heather R. Dial, Joseph R. Duffy, Stephanie M. Grasso, Esther Kim, Kristin Schaffer Mendez, Kirrie J. Ballard, Heather M. Clark, Leeah Kohley, Laura L. Murray, Emily J. Rogalski, Mathieu Figeys, Lisa Milman, and Maya L. Henry. Behavioral treatment for speech and language in primary progressive aphasia and primary progressive apraxia of speech: a systematic review. Neuropsychology Review, 34:882-923, Oct 2024. URL: https://doi.org/10.1007/s11065-023-09607-1, doi:10.1007/s11065-023-09607-1. This article has 70 citations and is from a domain leading peer-reviewed journal.

28. (tetzloff2024automaticspeechrecognition pages 5-8): Katerina A. Tetzloff, Daniela Wiepert, Hugo Botha, Joseph R. Duffy, Heather M. Clark, Jennifer L. Whitwell, Keith A. Josephs, and Rene L. Utianski. Automatic speech recognition in primary progressive apraxia of speech. Journal of Speech, Language, and Hearing Research, 67:2964-2976, Sep 2024. URL: https://doi.org/10.1044/2024\_jslhr-24-00049, doi:10.1044/2024\_jslhr-24-00049. This article has 15 citations and is from a highest quality peer-reviewed journal.

29. (tetzloff2023amyloidandtau pages 7-11): Katerina A. Tetzloff, Joseph R. Duffy, Heather M. Clark, Nha Trang Thu Pham, Mary M. Machulda, Hugo Botha, Clifford R. Jack, Dennis W. Dickson, Val J. Lowe, Keith A. Josephs, Jennifer L. Whitwell, and Rene L. Utianski. Amyloid and tau pet positivity in progressive agrammatic aphasia and apraxia of speech. Journal of Alzheimer's Disease, 96:1759-1765, Dec 2023. URL: https://doi.org/10.3233/jad-230912, doi:10.3233/jad-230912. This article has 3 citations and is from a peer-reviewed journal.

30. (utianski2018clinicalprogressionin pages 1-2): Rene L. Utianski, Joseph R. Duffy, Heather M. Clark, Edythe A. Strand, Sarah M. Boland, Mary M. Machulda, Jennifer L. Whitwell, and Keith A. Josephs. Clinical progression in four cases of primary progressive apraxia of speech. American journal of speech-language pathology, 27 4:1303-1318, Nov 2018. URL: https://doi.org/10.1044/2018\_ajslp-17-0227, doi:10.1044/2018\_ajslp-17-0227. This article has 47 citations and is from a domain leading peer-reviewed journal.

31. (utianski2018clinicalprogressionin pages 8-10): Rene L. Utianski, Joseph R. Duffy, Heather M. Clark, Edythe A. Strand, Sarah M. Boland, Mary M. Machulda, Jennifer L. Whitwell, and Keith A. Josephs. Clinical progression in four cases of primary progressive apraxia of speech. American journal of speech-language pathology, 27 4:1303-1318, Nov 2018. URL: https://doi.org/10.1044/2018\_ajslp-17-0227, doi:10.1044/2018\_ajslp-17-0227. This article has 47 citations and is from a domain leading peer-reviewed journal.

32. (wauters2024behavioraltreatmentfor pages 27-29): Lisa D. Wauters, Karen Croot, Heather R. Dial, Joseph R. Duffy, Stephanie M. Grasso, Esther Kim, Kristin Schaffer Mendez, Kirrie J. Ballard, Heather M. Clark, Leeah Kohley, Laura L. Murray, Emily J. Rogalski, Mathieu Figeys, Lisa Milman, and Maya L. Henry. Behavioral treatment for speech and language in primary progressive aphasia and primary progressive apraxia of speech: a systematic review. Neuropsychology Review, 34:882-923, Oct 2024. URL: https://doi.org/10.1007/s11065-023-09607-1, doi:10.1007/s11065-023-09607-1. This article has 70 citations and is from a domain leading peer-reviewed journal.

33. (wauters2024behavioraltreatmentfor pages 29-30): Lisa D. Wauters, Karen Croot, Heather R. Dial, Joseph R. Duffy, Stephanie M. Grasso, Esther Kim, Kristin Schaffer Mendez, Kirrie J. Ballard, Heather M. Clark, Leeah Kohley, Laura L. Murray, Emily J. Rogalski, Mathieu Figeys, Lisa Milman, and Maya L. Henry. Behavioral treatment for speech and language in primary progressive aphasia and primary progressive apraxia of speech: a systematic review. Neuropsychology Review, 34:882-923, Oct 2024. URL: https://doi.org/10.1007/s11065-023-09607-1, doi:10.1007/s11065-023-09607-1. This article has 70 citations and is from a domain leading peer-reviewed journal.