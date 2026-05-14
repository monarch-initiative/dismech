---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-12T17:36:27.843341'
end_time: '2026-05-12T17:59:03.232606'
duration_seconds: 1355.39
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Cervical Squamous Cell Carcinoma
  mondo_id: ''
  category: Complex
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 38
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Cervical Squamous Cell Carcinoma
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Cervical Squamous Cell Carcinoma** covering all of the
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
- **Disease Name:** Cervical Squamous Cell Carcinoma
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Cervical Squamous Cell Carcinoma** covering all of the
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


## Comprehensive Research Report: Cervical Squamous Cell Carcinoma (CSCC)

### Scope and evidence note
This report synthesizes evidence retrieved in the current tool session (peer‑reviewed primary studies, systematic reviews, guidelines, and OpenTargets associations). Where ontology IDs (e.g., MONDO, MeSH) were not explicitly available in retrieved sources, they are reported as “not found” rather than inferred. Evidence types are labeled when possible (human epidemiology/clinical trial/guideline/translational). 

---

## 1. Disease Information

### 1.1 Definition and current understanding
Cervical squamous cell carcinoma (CSCC) is the most common histologic subtype of cervical cancer, arising from squamous epithelium of the cervix and strongly linked to persistent high‑risk human papillomavirus (hrHPV) infection. CSCC accounts for ~85% of cervical cancers in a recent clinical review spanning 2018–2025, consistent with long‑standing epidemiology. (nagdev2026advancesinscreening pages 1-2)

### 1.2 Key identifiers and classification
A structured summary of identifiers and nomenclature supported by retrieved sources is provided in the embedded artifact. 

| Identifier type | Code/ID | Preferred label | Synonyms/alternate names | Source/URL/date |
|---|---|---|---|---|
| OpenTargets / EFO proxy | EFO_1000172 | cervical squamous cell carcinoma | CSCC; cervical SCC | OpenTargets disease-target association result for “cervical squamous cell carcinoma” (OpenTargets Search: cervical squamous cell carcinoma) |
| MONDO | not found in retrieved sources | Cervical squamous cell carcinoma | CSCC | No MONDO identifier explicitly reported in retrieved evidence; OpenTargets EFO proxy available instead (OpenTargets Search: cervical squamous cell carcinoma) |
| MeSH | not found in retrieved sources | not found in retrieved sources | “Uterine Cervical Neoplasms” mentioned as MeSH search terminology in cervical cancer literature, but no explicit MeSH ID for CSCC in retrieved evidence | Bobdey et al., *Burden of cervical cancer and role of screening in India*; https://doi.org/10.4103/0971-5851.195751; 2016 (snippet notes use of MeSH terms) (OpenTargets Search: cervical squamous cell carcinoma) |
| ICD-10 | C53 | cervical cancer / cervix uteri cancer | invasive cervical cancer | Noguchi et al., *Recent Increasing Incidence of Early-Stage Cervical Cancers of the Squamous Cell Carcinoma Subtype among Young Women*; https://doi.org/10.3390/ijerph17207401; 2020 (“invasive cancer (C53 in ICD-10)”) (OpenTargets Search: cervical squamous cell carcinoma) |
| WHO 2020 classification concept | not an external code in retrieved sources | HPV-associated squamous cell carcinoma of the cervix | HPV-associated cervical SCC | Höhn et al., *2020 WHO Classification of Female Genital Tumors*; https://doi.org/10.1055/a-1545-4279; 2021 (WHO distinguishes HPV-associated vs HPV-independent SCC) (hohn20212020whoclassification pages 1-2, hohn20212020whoclassification pages 2-4) |
| WHO 2020 classification concept | not an external code in retrieved sources | HPV-independent squamous cell carcinoma of the cervix | HPV-independent cervical SCC; squamous cell carcinoma, NOS acceptable if classification unavailable | Höhn et al., *2020 WHO Classification of Female Genital Tumors*; https://doi.org/10.1055/a-1545-4279; 2021; and Polish Society guidelines summarizing WHO-style classification; https://doi.org/10.3390/jcm13154351; 2024 (hohn20212020whoclassification pages 1-2, sznurkowski2024thepolishsociety pages 3-4, hohn20212020whoclassification pages 2-4) |
| Pathology surrogate marker | p16 (block-type expression) | surrogate marker for HPV association in cervical SCC | p16 IHC; strong diffuse “block” staining | Höhn et al., *2020 WHO Classification of Female Genital Tumors*; https://doi.org/10.1055/a-1545-4279; 2021 (p16 is a reliable, though imperfect, surrogate for HPV association) (hohn20212020whoclassification pages 1-2, hohn20212020whoclassification pages 2-4) |
| Histopathologic reporting term | NOS | squamous cell carcinoma, NOS | SCC, NOS | WHO 2020 summary indicates SCC, NOS is acceptable when HPV-association cannot be established by p16 and/or HPV testing (hohn20212020whoclassification pages 4-6, hohn20212020whoclassification pages 2-4) |
| Histologic subtype / nomenclature | not a code | non-keratinizing squamous cell carcinoma | non-keratinizing SCC | Mehla, *Study of Cervical Carcinomas Diagnosed in 2015-2022...*; 2025 (summarizes WHO-recognized morphologic subtypes including keratinizing, non-keratinizing, papillary) (mehla2025studyofcervical pages 10-12) |
| Histologic subtype / nomenclature | not a code | keratinizing squamous cell carcinoma | keratinizing SCC | Mehla, *Study of Cervical Carcinomas Diagnosed in 2015-2022...*; 2025; Polish Society guideline notes HPV-independent tumors are often keratinizing (sznurkowski2024thepolishsociety pages 2-3, mehla2025studyofcervical pages 10-12) |


*Table: This table summarizes the key identifiers, classification concepts, and nomenclature for cervical squamous cell carcinoma supported by the retrieved evidence. It highlights where formal identifiers were not explicitly found and preserves WHO 2020 terminology relevant for pathology reporting.*

Key classification concept: The WHO 2020 classification emphasizes reporting cervical squamous carcinomas as HPV‑associated versus HPV‑independent, using p16 immunohistochemistry (IHC) block‑type positivity as a surrogate marker for HPV association; when classification cannot be established, “squamous cell carcinoma, NOS” is acceptable. (hohn20212020whoclassification pages 2-4, hohn20212020whoclassification pages 1-2)

### 1.3 Synonyms/alternative names
Common terms in the retrieved literature include “cervical SCC” and “cervical squamous cell carcinoma (CSCC).” (nagdev2026advancesinscreening pages 1-2)

### 1.4 Evidence provenance (aggregated vs patient-level)
Most disease-level facts in this report derive from aggregated resources (GBD analyses, guideline consortia, and narrative/systematic reviews). (ma2025globalregionaland pages 2-3, fischerova2024theroleof pages 1-2, zhou2025globalcervicalcancer pages 1-2)

---

## 2. Etiology

### 2.1 Primary causal factors
Persistent infection with hrHPV is the dominant etiologic driver of cervical cancer: one 2024 screening-focused review states “over 95% of cervical cancers are attributable to HPV.” (goldstein2024thefutureof pages 1-2)

HPV16 and HPV18 contribute the majority of cases globally: estimates in retrieved sources include ~70% (review) and ~71% (global screening review). (nagdev2026advancesinscreening pages 1-2, goldstein2024thefutureof pages 1-2)

### 2.2 Risk factors (human epidemiology)
A concise, quantitative risk-factor table (restricted to effects explicitly present in retrieved evidence) is embedded below.

| Factor (etiologic/risk/protective) | Evidence type | Quantitative effect (RR/HR/% attributable) if available | Key notes (HPV types, cofactors) | Best supporting citation info |
|---|---|---|---|---|
| Persistent high-risk HPV infection | Review / epidemiology | ">95%" of cervical cancers attributable to HPV | Persistent hrHPV infection is the necessary/near-universal cause; CSCC is the dominant histology | Goldstein et al., 2024, DOI: 10.2147/IJWH.S474571 (goldstein2024thefutureof pages 1-2) |
| HPV16/18 attribution | Review / epidemiology | "~70%" of cases; alternatively "~71%" globally | HPV16 and HPV18 account for the majority of cervical cancers worldwide | Nagdev & Chittilla, 2026, DOI: 10.3390/curroncol33010048; Goldstein et al., 2024, DOI: 10.2147/IJWH.S474571 (nagdev2026advancesinscreening pages 1-2, goldstein2024thefutureof pages 1-2) |
| Smoking (current vs never) | Human epi / meta-analysis | Invasive cervical cancer RR 1.70 (95% CI 1.53–1.88) | Association persists independently of HPV infection; stronger for preinvasive disease | Malevolti et al., 2023, DOI: 10.1097/CEJ.0000000000000773 (malevolti2023doseriskrelationshipsbetween pages 5-6, malevolti2023doseriskrelationshipsbetween pages 1-2) |
| Smoking (former vs never) | Human epi / meta-analysis | Invasive cervical cancer RR 1.13 (95% CI 1.02–1.24) | Risk remains elevated after cessation but lower than for current smokers | Malevolti et al., 2023, DOI: 10.1097/CEJ.0000000000000773 (malevolti2023doseriskrelationshipsbetween pages 5-6, malevolti2023doseriskrelationshipsbetween pages 1-2) |
| Smoking intensity | Human epi / meta-analysis | 10 cigarettes/day: RR 1.72 (95% CI 1.34–2.20); 20/day: RR 1.91 (1.46–2.49) | Dose-response relationship for invasive cervical cancer | Malevolti et al., 2023, DOI: 10.1097/CEJ.0000000000000773 (malevolti2023doseriskrelationshipsbetween pages 5-6) |
| Smoking cessation | Human epi / meta-analysis | Former vs current RR 0.72 at 10 years quit; 0.53 at 20 years quit; risk approaches never-smokers after ~15–16.5 years | Supports smoking cessation as a protective/risk-reducing intervention | Malevolti et al., 2023, DOI: 10.1097/CEJ.0000000000000773 (malevolti2023doseriskrelationshipsbetween pages 5-6, malevolti2023doseriskrelationshipsbetween pages 1-2, malevolti2023doseriskrelationshipsbetween pages 6-7) |
| HIV infection | Review / epidemiology | Quantitative estimate not given in retrieved context; described as "several-fold increases in incidence among HIV-positive women" | Major cofactor promoting HPV persistence/progression; also highlighted in recent reviews/guidelines | Jouya et al., 2026, DOI: 10.3390/jcm15031079; Nagdev & Chittilla, 2026, DOI: 10.3390/curroncol33010048 (jouya2026cervicalcancerepidemiology pages 12-13, nagdev2026advancesinscreening pages 1-2) |
| High parity | Review / epidemiology | Quantitative estimate not given in retrieved context | Reproductive cofactor associated with higher risk; often grouped with early sexual debut/multiple partners | Jouya et al., 2026, DOI: 10.3390/jcm15031079 (jouya2026cervicalcancerepidemiology pages 12-13) |
| Unsafe sex / sexual exposure | Population burden analysis | Identified as a principal attributable risk factor for DALYs; no numeric fraction in retrieved excerpt | Captures HPV acquisition risk and broader sexual-behavior contribution | Shao et al., 2026, DOI: 10.3389/fpubh.2026.1702186 (shao2026globaltrendsand pages 1-2) |
| HPV vaccination | Guideline / prevention review | WHO target: 90% of girls vaccinated by age 15 | Primary prevention; recent guidance also notes single-dose strategies under evaluation/implementation | Zhou et al., 2025, DOI: 10.1186/s12916-025-03897-3; Jouya et al., 2026, DOI: 10.3390/jcm15031079 (zhou2025globalcervicalcancer pages 1-2, jouya2026cervicalcancerepidemiology pages 12-13) |
| Organized cervical screening | Guideline / prevention review | WHO target: 70% screened with high-performance tests by ages 35 and 45 | Secondary prevention; primary HPV testing, self-sampling, methylation triage and AI-assisted tools are emerging | Zhou et al., 2025, DOI: 10.1186/s12916-025-03897-3; Goldstein et al., 2024, DOI: 10.2147/IJWH.S474571 (zhou2025globalcervicalcancer pages 1-2, goldstein2024thefutureof pages 1-2) |
| Treatment of screen-detected disease | Guideline / prevention | WHO target: 90% of women with cervical disease receiving appropriate treatment | Tertiary/secondary prevention bridge in WHO elimination framework | Zhou et al., 2025, DOI: 10.1186/s12916-025-03897-3 (zhou2025globalcervicalcancer pages 1-2) |
| Elimination threshold | Guideline / global strategy | Incidence target: <4 new cases per 100,000 women per year | Defines cervical cancer elimination as a public health problem | Zhou et al., 2025, DOI: 10.1186/s12916-025-03897-3; Shao et al., 2026, DOI: 10.3389/fpubh.2026.1702186 (zhou2025globalcervicalcancer pages 1-2, shao2026globaltrendsand pages 1-2) |


*Table: This table summarizes the main etiologic drivers, established risk cofactors, and protective/preventive measures for cervical squamous cell carcinoma using only quantitative findings explicitly available in the retrieved evidence. It is useful for quickly separating causal HPV biology from modifiable cofactors and current WHO-aligned prevention strategies.*

**Smoking:** A 2023 systematic review/meta‑analysis (109 studies) reported pooled RR 1.70 (95% CI 1.53–1.88) for invasive cervical cancer in current vs never smokers, and RR 1.13 (95% CI 1.02–1.24) for former vs never smokers, with dose–response and risk reduction after cessation (risk approaching never smokers after ~15–16.5 years). (malevolti2023doseriskrelationshipsbetween pages 1-2, malevolti2023doseriskrelationshipsbetween pages 5-6)

**HIV/immunosuppression:** A 2026 epidemiology review reports “several‑fold increases in incidence among HIV‑positive women,” supporting HIV as a major cofactor that accelerates HPV persistence/progression. (jouya2026cervicalcancerepidemiology pages 12-13)

**Reproductive/sexual cofactors:** Early sexual debut, multiple partners, and high parity are cited as important cofactors in a 2026 epidemiology review. (jouya2026cervicalcancerepidemiology pages 12-13)

### 2.3 Protective factors
**HPV vaccination** is the major primary preventive factor within the WHO elimination framework (targets described below). (zhou2025globalcervicalcancer pages 1-2)

**Smoking cessation** is protective: dose–response meta-analysis indicates risk declines with time since quitting and approximates never-smoker risk after ~15–16.5 years. (malevolti2023doseriskrelationshipsbetween pages 5-6, malevolti2023doseriskrelationshipsbetween pages 6-7)

### 2.4 Gene–environment interactions
Direct quantitative gene–environment interaction estimates were not identified in the retrieved sources during this tool session. Mechanistically, HPV-driven oncogenesis interacts with host immune status (e.g., HIV) and tobacco exposure, consistent with multi-factorial progression models discussed in reviews. (jouya2026cervicalcancerepidemiology pages 12-13, malevolti2023doseriskrelationshipsbetween pages 1-2)

---

## 3. Phenotypes (clinical presentation) 

### 3.1 Common phenotypes (signs/symptoms)
Recent guideline and clinical review materials in the retrieved set describe typical presenting features including abnormal vaginal bleeding/discharge and pelvic pain (not always CSCC‑specific but common across cervical cancer). (nagdev2026advancesinscreening pages 1-2)

### 3.2 Suggested HPO terms (not exhaustive)
Because structured phenotype-frequency estimates were not retrieved in this session, the following HPO terms are suggested as standard mappings (frequency requires additional sourcing):
- Abnormal uterine bleeding / postcoital bleeding: **HP:0000132** (Abnormality of menstruation) or **HP:0000858** (Menorrhagia) depending on context.
- Vaginal discharge: **HP:0000146** (Vaginal discharge).
- Pelvic pain: **HP:0002027** (Abdominal pain) / pelvic pain term where available in HPO.
- Anemia (from bleeding): **HP:0001903** (Anemia).

### 3.3 Quality-of-life impact
Direct QoL instrument values specific to CSCC were not extracted from the retrieved evidence in this session; however, guideline and review sources emphasize substantial morbidity in advanced disease and the importance of palliative care access. (zhou2025globalcervicalcancer pages 1-2)

---

## 4. Genetic / Molecular Information

### 4.1 Somatic driver landscape (high-level)
OpenTargets disease–target associations for “cervical squamous cell carcinoma” highlight recurrently implicated cancer genes including **PIK3CA, FBXW7, KMT2C, EP300, KMT2D, MAPK1, TP53, PTEN, STK11, NOTCH1, ERBB2**, among others. This provides a curated pointer to commonly altered pathways in CSCC but is not itself a sequencing cohort analysis. (OpenTargets Search: cervical squamous cell carcinoma)

### 4.2 HPV-associated vs HPV-independent molecular patterns
A 2024 national guideline summary reports that HPV-associated cervical SCC is the dominant category (~90–95%), while HPV-independent SCC constitutes a minority (~5–7%) and is often associated with abnormal p53 staining and distinct molecular associations (e.g., KRAS, ARID1A, PTEN). (sznurkowski2024thepolishsociety pages 2-3)

### 4.3 Epigenetics
WHO 2020 discussions note p16 as a surrogate and acknowledge false negatives (e.g., p16 hypermethylation in a small fraction of CIN3), but systematic CSCC epigenomic signatures were not comprehensively extracted in this session. (hohn20212020whoclassification pages 6-8)

### 4.4 Pathogenic variants (germline)
No germline causal variant set (ClinVar/ClinGen-style) was retrieved for CSCC in this session; CSCC is typically infection-driven with predominantly somatic alterations. (goldstein2024thefutureof pages 1-2)

---

## 5. Environmental Information

### 5.1 Lifestyle/environmental contributors
Smoking is a robust, quantitatively supported risk factor with dose–response effects (RRs above). (malevolti2023doseriskrelationshipsbetween pages 5-6, malevolti2023doseriskrelationshipsbetween pages 1-2)

### 5.2 Infectious agents
High-risk HPV is the central infectious cause; HPV16/18 dominate global attribution fractions. (goldstein2024thefutureof pages 1-2, nagdev2026advancesinscreening pages 1-2)

---

## 6. Mechanism / Pathophysiology

### 6.1 Causal chain (HPV to CSCC)
A mechanistic review of HPV-associated lower genital tract cancers describes HPV oncoprotein-driven immune evasion, including upregulation of PD‑1/PD‑L1 axis and other checkpoint pathways (IDO1, LAG3, TIM3/Galectin‑9, TIGIT), providing a link from viral oncogenesis to an immunosuppressive tumor microenvironment and therapeutic vulnerability to checkpoint blockade. (zafar2025advancesandchallenges pages 7-8, zafar2025advancesandchallenges pages 20-21)

### 6.2 Immune microenvironment and checkpoint biology
HPV16 E6 has been described as promoting PD‑L1 expression via a miR‑143/HIF‑1α pathway; HPV-positive cervical cancer cells can also influence exosomal PD‑L1 expression by fibroblasts via CXCL10/CXCR3 and JAK‑STAT signaling, supporting multi-cell mechanisms for immune escape. (zafar2025advancesandchallenges pages 20-21)

### 6.3 Spatial transcriptomics: metabolic states and oncogenic regulators (2024 primary study)
A 2024 Journal of Translational Medicine study used spatial transcriptomics integrated with scRNA‑seq and TCGA analyses to map hypermetabolic versus hypometabolic regions in CSCC and identify regulatory factors. (zhou2024spatialtranscriptomicsreveals pages 1-2, zhou2024spatialtranscriptomicsreveals pages 9-12)

Key reported findings include: 
- Leading edge regions were characterized as uniformly hypermetabolic, whereas tumor core contained mixed hyper‑ and hypometabolic spots. (zhou2024spatialtranscriptomicsreveals pages 9-12)
- APP was identified as a signaling molecule released by cancer cells with higher expression in hypermetabolic regions, and APP expression correlated with transcription factor TRPS1; functional knockdowns reduced proliferation/migration/invasion in vitro. (zhou2024spatialtranscriptomicsreveals pages 1-2, zhou2024spatialtranscriptomicsreveals pages 14-17)
- Immune context differed by region, with PD‑L1 and IDO1 elevated in tumor center in one excerpted analysis, consistent with immune suppression. (zhou2024spatialtranscriptomicsreveals pages 14-17, zhou2024spatialtranscriptomicsreveals pages 6-9)

Visual evidence from the same study illustrating spatial hyper/hypometabolic regions and TRPS1/APP expression patterns is available in retrieved figure crops. (zhou2024spatialtranscriptomicsreveals media 5eccae45, zhou2024spatialtranscriptomicsreveals media 8e0f5cba, zhou2024spatialtranscriptomicsreveals media c108e719, zhou2024spatialtranscriptomicsreveals media f3ff4cda)

### 6.4 Suggested ontology mappings
**GO biological processes (examples):**
- GO:0006915 (apoptotic process)
- GO:0007049 (cell cycle)
- GO:0006955 (immune response)
- GO:0006096 (glycolytic process) / GO:0006119 (oxidative phosphorylation)

**Cell Ontology (CL) cell types (examples):**
- CL:0000066 (epithelial cell)
- CL:0000236 (B cell)
- CL:0000623 (natural killer cell)
- CL:0000904 (macrophage)
- CL:0000451 (dendritic cell)

These ontology suggestions reflect mechanisms described in immune/multi‑omics sources, though specific term-to-claim mappings require additional structured curation beyond retrieved text. (zafar2025advancesandchallenges pages 20-21, zhou2024spatialtranscriptomicsreveals pages 14-17)

---

## 7. Anatomical Structures Affected

### 7.1 Organ and tissue level
Primary site is the cervix uteri, involving squamous epithelium (outer surface). (nagdev2026advancesinscreening pages 1-2)

**Suggested UBERON terms (examples):**
- UBERON:0000002 (uterine cervix)
- UBERON:0000458 (epithelium)

### 7.2 Subcellular/localization (GO-CC suggestions)
- GO:0005634 (nucleus) for transcriptional regulators (e.g., TRPS1)
- GO:0005886 (plasma membrane) for receptor/ligand interactions

---

## 8. Temporal Development (natural history)
The natural history from HPV infection through precancer to invasive carcinoma is described as well characterized in recent reviews, supporting screening and prevention paradigms. (nagdev2026advancesinscreening pages 1-2)

(Explicit quantitative transition probabilities and CIN stage durations were not extracted in the retrieved evidence during this session.)

---

## 9. Inheritance and Population

### 9.1 Epidemiology (recent global statistics)
Global incidence and mortality estimates reported in the retrieved sources include:
- **2022:** 661,021 new cases and 348,189 deaths (global elimination progress analysis). (zhou2025globalcervicalcancer pages 1-2)
- **GLOBOCAN 2022 (as cited in a 2026 clinical review):** 662,000 new cases and 349,000 deaths, with mortality rate 7.1 per 100,000. (nagdev2026advancesinscreening pages 1-2)
- **2021 (GBD-based estimates):** 667,000 incident cases and 297,000 deaths; ~7.44 million DALYs attributed to cervical cancer. (ma2025globalregionaland pages 2-3)

Health inequities are substantial: one 2026 review states that over 80% of cervical cancer deaths occur in low-HDI settings. (jouya2026cervicalcancerepidemiology pages 12-13)

### 9.2 Inheritance pattern
CSCC is predominantly infection-associated and not typically inherited as a Mendelian disorder in the retrieved sources. (goldstein2024thefutureof pages 1-2)

---

## 10. Diagnostics

### 10.1 Screening and diagnostic pathway (current practice and developments)
Recent screening developments include primary HPV testing, HPV self‑sampling, and molecular triage strategies (DNA methylation assays, dual-stain cytology), as summarized in a 2024 review on the future of cervical screening. (goldstein2024thefutureof pages 1-2)

### 10.2 Pathology / biomarkers
WHO 2020 recommends distinguishing HPV-associated from HPV-independent squamous carcinomas and identifies p16 block staining as a reliable (imperfect) surrogate for HPV association; when uncertain, SCC NOS is acceptable. (hohn20212020whoclassification pages 2-4)

### 10.3 Imaging/staging (2023 guideline update summarized in 2024)
The ESGO/ESTRO/ESP imaging update (2023) recommends:
- **Pelvic MRI or expert transvaginal/transrectal ultrasound** for local tumor delineation and assessing invasion. (fischerova2024theroleof pages 1-2)
- **Contrast-enhanced CT or 18F‑FDG PET/CT** for extrapelvic spread in locally advanced disease or when suspicious nodes are present. (fischerova2024theroleof pages 1-2)

MRI is emphasized as modality of choice for local staging; PET/CT is valuable for nodal/distant disease detection but less optimal for local staging due to soft tissue limitations. (fischerova2024theroleof pages 7-8)

---

## 11. Outcome / Prognosis

### 11.1 Prognostic biomarkers and microenvironment
Spatial transcriptomics evidence suggests that elevated APP and TRPS1 correlate with poorer survival in TCGA CSCC cohort (p-values reported) and promote aggressive phenotypes in vitro, supporting their candidacy as prognostic/biological markers. (zhou2024spatialtranscriptomicsreveals pages 14-17)

### 11.2 Advanced disease outcomes and unmet need
A 2024 review on advanced/recurrent cervical cancer notes poor prognosis historically and summarizes improved outcomes with immunotherapy-based regimens. (zafar2025advancesandchallenges pages 7-8)

(Registry-derived 5‑year survival stratified by stage/histology was not retrieved in this session.)

---

## 12. Treatment

### 12.1 Standard local therapy (curative intent)
A mechanistic/clinical review notes standard local therapy for cervical cancer includes pelvic external beam radiotherapy (EBRT) with concurrent platinum-based chemotherapy and brachytherapy. (zafar2025advancesandchallenges pages 7-8)

### 12.2 Systemic therapy—immune checkpoint inhibitors (advanced/recurrent/metastatic)
Evidence extracted from an immunotherapy review includes:
- **KEYNOTE‑826** (pembrolizumab + chemotherapy ± bevacizumab): reported hazard ratio for death ~0.64 (36% reduction in risk of death) and survival prolongation by 12.1 months in the cited review excerpt. (dey2025immunotherapyincervical pages 7-8)
- **EMPOWER‑Cervical 1** (cemiplimab vs chemotherapy after platinum): median OS 12 vs 8.5 months; ORR 16.4% vs 6.3% in the cited review excerpt. (dey2025immunotherapyincervical pages 7-8)

A separate checkpoint-focused review reports pembrolizumab median OS 28.6 vs 16.5 months (trial context described) and reiterates cemiplimab OS 12 vs 8.5 months. (zafar2025advancesandchallenges pages 7-8)

### 12.3 Treatment-related toxicity (high level)
The immunotherapy review notes increased toxicities with combination regimens (e.g., anemia, neuropathy) and highlights immune-related adverse events as clinically relevant. (dey2025immunotherapyincervical pages 7-8)

### 12.4 Suggested MAXO mappings (examples)
- MAXO:0000058 (radiotherapy)
- MAXO:0000010 (chemotherapy)
- MAXO term for immune checkpoint inhibitor therapy (e.g., “immune checkpoint inhibitor therapy”)—exact MAXO ID not retrieved in this session.

---

## 13. Prevention

### 13.1 WHO elimination strategy and targets
A 2025 global elimination analysis summarizes WHO’s 90–70–90 strategy by 2030: 
- 90% of girls vaccinated by age 15,
- 70% of women screened with high-performance tests by ages 35 and 45,
- 90% of women with cervical disease treated. (zhou2025globalcervicalcancer pages 1-2)

The elimination threshold is defined as **<4 new cases per 100,000 women per year**. (zhou2025globalcervicalcancer pages 1-2)

### 13.2 Screening technology modernization (2024)
Emerging modalities include rapid low-cost HPV testing, self-sampling, DNA methylation assays, and AI-assisted digital colposcopy interpretation, as summarized in a 2024 screening review. (goldstein2024thefutureof pages 1-2)

---

## 14. Other Species / Natural Disease
No cross-species naturally occurring CSCC analog with comparable HPV-driven etiology was retrieved in this session. Comparative HPV-associated squamous carcinomas across lower genital tract sites are discussed broadly in HPV-related reviews, but not as a dedicated veterinary natural disease section. (zafar2025advancesandchallenges pages 7-8)

---

## 15. Model Organisms
Specific in vivo model organism systems (e.g., HPV transgenic mouse models), organoids, or PDX resources were not retrieved in this session. The spatial transcriptomics CSCC work used human FFPE tumors integrated with scRNA-seq and in vitro functional assays (HeLa knockdowns), which constitutes a human tissue + cell line translational model rather than an animal model. (zhou2024spatialtranscriptomicsreveals pages 14-17, zhou2024spatialtranscriptomicsreveals pages 1-2)

---

## Recent developments (2023–2024 highlights)
1. **Spatial transcriptomics in CSCC (2024):** identification of spatially resolved metabolic states and regulators (APP/TRPS1), with supporting figure evidence for regional metabolic patterns and gene expression. (zhou2024spatialtranscriptomicsreveals pages 1-2, zhou2024spatialtranscriptomicsreveals pages 14-17, zhou2024spatialtranscriptomicsreveals media 5eccae45, zhou2024spatialtranscriptomicsreveals media f3ff4cda)
2. **Updated European imaging recommendations (2023 update, published 2024):** stronger operational role for expert ultrasound and MRI in local staging and PET/CT or CECT for extrapelvic evaluation in higher-risk scenarios. (fischerova2024theroleof pages 1-2, fischerova2024theroleof pages 7-8)
3. **Smoking risk quantification updated meta-analysis (2023):** robust pooled RRs and cessation timelines relevant to prevention counseling. (malevolti2023doseriskrelationshipsbetween pages 1-2, malevolti2023doseriskrelationshipsbetween pages 5-6)
4. **Screening innovation synthesis (2024):** primary HPV testing, self-sampling, methylation triage, dual stain cytology, and AI-enabled tools highlighted as near-term implementation candidates. (goldstein2024thefutureof pages 1-2)

---

## Embedded figure evidence (spatial transcriptomics)
The following retrieved figure crops from the 2024 CSCC spatial transcriptomics study support claims about metabolic regions and APP/TRPS1 spatial patterns: hyper/hypometabolic region maps and TRPS1/APP spatial expression panels. (zhou2024spatialtranscriptomicsreveals media 5eccae45, zhou2024spatialtranscriptomicsreveals media 8e0f5cba, zhou2024spatialtranscriptomicsreveals media c108e719, zhou2024spatialtranscriptomicsreveals media f3ff4cda)

---

## Key gaps (not found in retrieved sources in this session)
- MONDO and MeSH unique identifiers for CSCC (codes not explicitly captured in retrieved texts). (OpenTargets Search: cervical squamous cell carcinoma)
- Detailed phenotype frequencies mapped to HPO and validated QoL instrument statistics specific to CSCC.
- Comprehensive germline variant catalog and population allele frequencies.
- Dedicated model organism summaries (HPV transgenic mice, organoids, PDX) with citations.

These gaps reflect limitations of the retrieved document set rather than absence of knowledge in the broader literature.


References

1. (nagdev2026advancesinscreening pages 1-2): Priyanka Nagdev and Mythri Chittilla. Advances in screening, immunotherapy, targeted agents, and precision surgery in cervical cancer: a comprehensive clinical review (2018–2025). Current Oncology, Jan 2026. URL: https://doi.org/10.3390/curroncol33010048, doi:10.3390/curroncol33010048. This article has 1 citations.

2. (OpenTargets Search: cervical squamous cell carcinoma): Open Targets Query (cervical squamous cell carcinoma, 39 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

3. (hohn20212020whoclassification pages 1-2): Anne Kathrin Höhn, Christine E. Brambs, Grit Gesine Ruth Hiller, Doris May, Elisa Schmoeckel, and Lars-Christian Horn. 2020 who classification of female genital tumors. Geburtshilfe und Frauenheilkunde, 81:1145-1153, Oct 2021. URL: https://doi.org/10.1055/a-1545-4279, doi:10.1055/a-1545-4279. This article has 495 citations and is from a peer-reviewed journal.

4. (hohn20212020whoclassification pages 2-4): Anne Kathrin Höhn, Christine E. Brambs, Grit Gesine Ruth Hiller, Doris May, Elisa Schmoeckel, and Lars-Christian Horn. 2020 who classification of female genital tumors. Geburtshilfe und Frauenheilkunde, 81:1145-1153, Oct 2021. URL: https://doi.org/10.1055/a-1545-4279, doi:10.1055/a-1545-4279. This article has 495 citations and is from a peer-reviewed journal.

5. (sznurkowski2024thepolishsociety pages 3-4): Jacek J. Sznurkowski, Lubomir Bodnar, Łukasz Szylberg, Agnieszka Zołciak-Siwinska, Anna Dańska-Bidzińska, Dagmara Klasa-Mazurkiewicz, Agnieszka Rychlik, Artur Kowalik, Joanna Streb, Mariusz Bidziński, and Włodzimierz Sawicki. The polish society of gynecological oncology guidelines for the diagnosis and treatment of cervical cancer (v2024.0). Journal of Clinical Medicine, 13:4351, Jul 2024. URL: https://doi.org/10.3390/jcm13154351, doi:10.3390/jcm13154351. This article has 10 citations.

6. (hohn20212020whoclassification pages 4-6): Anne Kathrin Höhn, Christine E. Brambs, Grit Gesine Ruth Hiller, Doris May, Elisa Schmoeckel, and Lars-Christian Horn. 2020 who classification of female genital tumors. Geburtshilfe und Frauenheilkunde, 81:1145-1153, Oct 2021. URL: https://doi.org/10.1055/a-1545-4279, doi:10.1055/a-1545-4279. This article has 495 citations and is from a peer-reviewed journal.

7. (mehla2025studyofcervical pages 10-12): S Mehla. Study of cervical carcinomas diagnosed in 2015-2022 at the pathological anatomy clinic of hospital of luhs kauno clinics. Unknown journal, 2025.

8. (sznurkowski2024thepolishsociety pages 2-3): Jacek J. Sznurkowski, Lubomir Bodnar, Łukasz Szylberg, Agnieszka Zołciak-Siwinska, Anna Dańska-Bidzińska, Dagmara Klasa-Mazurkiewicz, Agnieszka Rychlik, Artur Kowalik, Joanna Streb, Mariusz Bidziński, and Włodzimierz Sawicki. The polish society of gynecological oncology guidelines for the diagnosis and treatment of cervical cancer (v2024.0). Journal of Clinical Medicine, 13:4351, Jul 2024. URL: https://doi.org/10.3390/jcm13154351, doi:10.3390/jcm13154351. This article has 10 citations.

9. (ma2025globalregionaland pages 2-3): Yidi Ma, Xiaozhen Lai, and Hai Fang. Global, regional, and national disease burden and economic costs of cervical cancer (1991–2021): a multidimensional data synthesis analysis. Frontiers in Public Health, Sep 2025. URL: https://doi.org/10.3389/fpubh.2025.1633975, doi:10.3389/fpubh.2025.1633975. This article has 3 citations.

10. (fischerova2024theroleof pages 1-2): Daniela Fischerova, Filip Frühauf, Andrea Burgetova, Ingfrid S. Haldorsen, Elena Gatti, and David Cibula. The role of imaging in cervical cancer staging: esgo/estro/esp guidelines (update 2023). Cancers, 16:775, Feb 2024. URL: https://doi.org/10.3390/cancers16040775, doi:10.3390/cancers16040775. This article has 50 citations.

11. (zhou2025globalcervicalcancer pages 1-2): Liangru Zhou, Yi Li, Hongyun Wang, Ruixi Qin, Zhen Han, and Ruifeng Li. Global cervical cancer elimination: quantifying the status, progress, and gaps. BMC Medicine, Feb 2025. URL: https://doi.org/10.1186/s12916-025-03897-3, doi:10.1186/s12916-025-03897-3. This article has 44 citations and is from a domain leading peer-reviewed journal.

12. (goldstein2024thefutureof pages 1-2): Amelia R Goldstein, Mallory Gersh, Gabriela Skovronsky, and Chailee Moss. The future of cervical cancer screening. International Journal of Women's Health, 16:1715-1731, Oct 2024. URL: https://doi.org/10.2147/ijwh.s474571, doi:10.2147/ijwh.s474571. This article has 43 citations and is from a peer-reviewed journal.

13. (malevolti2023doseriskrelationshipsbetween pages 5-6): Maria Chiara Malevolti, Alessandra Lugo, Marco Scala, Silvano Gallus, Giuseppe Gorini, Alessio Lachi, and Giulia Carreras. Dose-risk relationships between cigarette smoking and cervical cancer: a systematic review and meta-analysis. European Journal of Cancer Prevention, 32:171-183, Nov 2023. URL: https://doi.org/10.1097/cej.0000000000000773, doi:10.1097/cej.0000000000000773. This article has 50 citations and is from a peer-reviewed journal.

14. (malevolti2023doseriskrelationshipsbetween pages 1-2): Maria Chiara Malevolti, Alessandra Lugo, Marco Scala, Silvano Gallus, Giuseppe Gorini, Alessio Lachi, and Giulia Carreras. Dose-risk relationships between cigarette smoking and cervical cancer: a systematic review and meta-analysis. European Journal of Cancer Prevention, 32:171-183, Nov 2023. URL: https://doi.org/10.1097/cej.0000000000000773, doi:10.1097/cej.0000000000000773. This article has 50 citations and is from a peer-reviewed journal.

15. (malevolti2023doseriskrelationshipsbetween pages 6-7): Maria Chiara Malevolti, Alessandra Lugo, Marco Scala, Silvano Gallus, Giuseppe Gorini, Alessio Lachi, and Giulia Carreras. Dose-risk relationships between cigarette smoking and cervical cancer: a systematic review and meta-analysis. European Journal of Cancer Prevention, 32:171-183, Nov 2023. URL: https://doi.org/10.1097/cej.0000000000000773, doi:10.1097/cej.0000000000000773. This article has 50 citations and is from a peer-reviewed journal.

16. (jouya2026cervicalcancerepidemiology pages 12-13): Sara Jouya, Zahra Shahabinia, Afrooz Mazidimoradi, Leila Allahqoli, Hamid Salehiniya, and Do-Youn Lee. Cervical cancer epidemiology: global incidence, mortality, survival, risk factors, and equity in hpv screening and vaccination. Journal of Clinical Medicine, 15:1079, Jan 2026. URL: https://doi.org/10.3390/jcm15031079, doi:10.3390/jcm15031079. This article has 4 citations.

17. (shao2026globaltrendsand pages 1-2): Dongxuan Shao, Ping Wu, Huici Jiang, and Zhijie Wang. Global trends and future projections of cervical cancer burden: an integrated analysis of gbd 2021, un population and who hpv vaccination data. Frontiers in Public Health, Jan 2026. URL: https://doi.org/10.3389/fpubh.2026.1702186, doi:10.3389/fpubh.2026.1702186. This article has 3 citations.

18. (hohn20212020whoclassification pages 6-8): Anne Kathrin Höhn, Christine E. Brambs, Grit Gesine Ruth Hiller, Doris May, Elisa Schmoeckel, and Lars-Christian Horn. 2020 who classification of female genital tumors. Geburtshilfe und Frauenheilkunde, 81:1145-1153, Oct 2021. URL: https://doi.org/10.1055/a-1545-4279, doi:10.1055/a-1545-4279. This article has 495 citations and is from a peer-reviewed journal.

19. (zafar2025advancesandchallenges pages 7-8): Marhama Zafar, Narjes Sweis, Hitesh Kapoor, and Gerald Gantt. Advances and challenges in the treatment of hpv-associated lower genital tract cancers by immune checkpoint blockers: insights from basic and clinical science. Cancers, 17:1260, Apr 2025. URL: https://doi.org/10.3390/cancers17081260, doi:10.3390/cancers17081260. This article has 3 citations.

20. (zafar2025advancesandchallenges pages 20-21): Marhama Zafar, Narjes Sweis, Hitesh Kapoor, and Gerald Gantt. Advances and challenges in the treatment of hpv-associated lower genital tract cancers by immune checkpoint blockers: insights from basic and clinical science. Cancers, 17:1260, Apr 2025. URL: https://doi.org/10.3390/cancers17081260, doi:10.3390/cancers17081260. This article has 3 citations.

21. (zhou2024spatialtranscriptomicsreveals pages 1-2): Limin Zhou, Jiejie Liu, Peipei Yao, Xing Liu, Fei Chen, Yu Chen, Li Zhou, Chao Shen, You Zhou, Xin Du, and Junbo Hu. Spatial transcriptomics reveals unique metabolic profile and key oncogenic regulators of cervical squamous cell carcinoma. Journal of Translational Medicine, Dec 2024. URL: https://doi.org/10.1186/s12967-024-06011-y, doi:10.1186/s12967-024-06011-y. This article has 8 citations and is from a peer-reviewed journal.

22. (zhou2024spatialtranscriptomicsreveals pages 9-12): Limin Zhou, Jiejie Liu, Peipei Yao, Xing Liu, Fei Chen, Yu Chen, Li Zhou, Chao Shen, You Zhou, Xin Du, and Junbo Hu. Spatial transcriptomics reveals unique metabolic profile and key oncogenic regulators of cervical squamous cell carcinoma. Journal of Translational Medicine, Dec 2024. URL: https://doi.org/10.1186/s12967-024-06011-y, doi:10.1186/s12967-024-06011-y. This article has 8 citations and is from a peer-reviewed journal.

23. (zhou2024spatialtranscriptomicsreveals pages 14-17): Limin Zhou, Jiejie Liu, Peipei Yao, Xing Liu, Fei Chen, Yu Chen, Li Zhou, Chao Shen, You Zhou, Xin Du, and Junbo Hu. Spatial transcriptomics reveals unique metabolic profile and key oncogenic regulators of cervical squamous cell carcinoma. Journal of Translational Medicine, Dec 2024. URL: https://doi.org/10.1186/s12967-024-06011-y, doi:10.1186/s12967-024-06011-y. This article has 8 citations and is from a peer-reviewed journal.

24. (zhou2024spatialtranscriptomicsreveals pages 6-9): Limin Zhou, Jiejie Liu, Peipei Yao, Xing Liu, Fei Chen, Yu Chen, Li Zhou, Chao Shen, You Zhou, Xin Du, and Junbo Hu. Spatial transcriptomics reveals unique metabolic profile and key oncogenic regulators of cervical squamous cell carcinoma. Journal of Translational Medicine, Dec 2024. URL: https://doi.org/10.1186/s12967-024-06011-y, doi:10.1186/s12967-024-06011-y. This article has 8 citations and is from a peer-reviewed journal.

25. (zhou2024spatialtranscriptomicsreveals media 5eccae45): Limin Zhou, Jiejie Liu, Peipei Yao, Xing Liu, Fei Chen, Yu Chen, Li Zhou, Chao Shen, You Zhou, Xin Du, and Junbo Hu. Spatial transcriptomics reveals unique metabolic profile and key oncogenic regulators of cervical squamous cell carcinoma. Journal of Translational Medicine, Dec 2024. URL: https://doi.org/10.1186/s12967-024-06011-y, doi:10.1186/s12967-024-06011-y. This article has 8 citations and is from a peer-reviewed journal.

26. (zhou2024spatialtranscriptomicsreveals media 8e0f5cba): Limin Zhou, Jiejie Liu, Peipei Yao, Xing Liu, Fei Chen, Yu Chen, Li Zhou, Chao Shen, You Zhou, Xin Du, and Junbo Hu. Spatial transcriptomics reveals unique metabolic profile and key oncogenic regulators of cervical squamous cell carcinoma. Journal of Translational Medicine, Dec 2024. URL: https://doi.org/10.1186/s12967-024-06011-y, doi:10.1186/s12967-024-06011-y. This article has 8 citations and is from a peer-reviewed journal.

27. (zhou2024spatialtranscriptomicsreveals media c108e719): Limin Zhou, Jiejie Liu, Peipei Yao, Xing Liu, Fei Chen, Yu Chen, Li Zhou, Chao Shen, You Zhou, Xin Du, and Junbo Hu. Spatial transcriptomics reveals unique metabolic profile and key oncogenic regulators of cervical squamous cell carcinoma. Journal of Translational Medicine, Dec 2024. URL: https://doi.org/10.1186/s12967-024-06011-y, doi:10.1186/s12967-024-06011-y. This article has 8 citations and is from a peer-reviewed journal.

28. (zhou2024spatialtranscriptomicsreveals media f3ff4cda): Limin Zhou, Jiejie Liu, Peipei Yao, Xing Liu, Fei Chen, Yu Chen, Li Zhou, Chao Shen, You Zhou, Xin Du, and Junbo Hu. Spatial transcriptomics reveals unique metabolic profile and key oncogenic regulators of cervical squamous cell carcinoma. Journal of Translational Medicine, Dec 2024. URL: https://doi.org/10.1186/s12967-024-06011-y, doi:10.1186/s12967-024-06011-y. This article has 8 citations and is from a peer-reviewed journal.

29. (fischerova2024theroleof pages 7-8): Daniela Fischerova, Filip Frühauf, Andrea Burgetova, Ingfrid S. Haldorsen, Elena Gatti, and David Cibula. The role of imaging in cervical cancer staging: esgo/estro/esp guidelines (update 2023). Cancers, 16:775, Feb 2024. URL: https://doi.org/10.3390/cancers16040775, doi:10.3390/cancers16040775. This article has 50 citations.

30. (dey2025immunotherapyincervical pages 7-8): Treshita Dey and Sushma Agrawal. Immunotherapy in cervical cancer: an innovative approach for better treatment outcomes. Exploration of Targeted Anti-tumor Therapy, Mar 2025. URL: https://doi.org/10.37349/etat.2025.1002296, doi:10.37349/etat.2025.1002296. This article has 21 citations.