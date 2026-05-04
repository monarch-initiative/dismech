---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-04T15:41:53.839822'
end_time: '2026-05-04T16:01:43.216037'
duration_seconds: 1189.38
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Acute Hepatitis C Virus Infection
  mondo_id: ''
  category: Infectious
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 50
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Acute Hepatitis C Virus Infection
- **MONDO ID:**  (if available)
- **Category:** Infectious

## Research Objectives

Please provide a comprehensive research report on **Acute Hepatitis C Virus Infection** covering all of the
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
- **Disease Name:** Acute Hepatitis C Virus Infection
- **MONDO ID:**  (if available)
- **Category:** Infectious

## Research Objectives

Please provide a comprehensive research report on **Acute Hepatitis C Virus Infection** covering all of the
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


## Comprehensive Research Report: Acute Hepatitis C Virus (HCV) Infection (Infectious)

### Executive summary
Acute (recently acquired) hepatitis C is the first ~6 months after HCV exposure, a period during which infection may spontaneously clear but still frequently progresses to chronic hepatitis C (persistent viremia >6 months). Diagnosis is challenging because most cases are asymptomatic and anti-HCV serology has a window period; nucleic acid testing (NAT) is therefore central. Current expert consensus in major guidance documents supports a “test-and-treat” approach (treat acute infection with standard DAA regimens rather than waiting for spontaneous clearance), while abbreviated short-course regimens (e.g., 6 weeks) are generally not recommended outside trials because of inferior outcomes. (fasano2024acutehepatitisc pages 1-2, liu2023acutehepatitisc pages 5-6, fasano2024acutehepatitisc pages 2-4, panel2023idsaguidelines pages 9-10)

| Domain | Key points (with numbers) | Evidence type | Key source (first author, year, journal) | URL | PubMed ID |
|---|---|---|---|---|---|
| Disease definition | Acute/recently acquired HCV refers to the early phase of infection, generally the first **6 months after exposure**; chronic infection is defined by **persistence of viremia >6 months**. Terminology in use includes “acute hepatitis C,” “recently acquired hepatitis C,” and “early phase of HCV infection.” (fasano2024acutehepatitisc pages 1-2, fasano2024acutehepatitisc pages 4-5, liu2023acutehepatitisc pages 5-6) | Review | Fasano, 2024, *Viruses* | https://doi.org/10.3390/v16111739 |  |
| Diagnostic windows | **HCV RNA** becomes detectable about **1–2 weeks after exposure**; **anti-HCV antibodies** usually appear after **4–12 weeks**. Third-generation EIAs detect seroconversion at about **7–10 weeks**; fourth-generation Ag/Ab assays can shorten the window to about **26 days** or by **2.2–21.9 days** compared with Ab-only assays. (fasano2024acutehepatitisc pages 2-4, zilouchian2025currentandfuture pages 4-6, liu2023acutehepatitisc pages 5-6, bui2024comparisonofa pages 1-2, galli2025hcvserologyan pages 12-13) | Review / diagnostic study | Fasano, 2024, *Viruses*; Bui, 2024, *J Clin Microbiol* | https://doi.org/10.3390/v16111739 ; https://doi.org/10.1128/jcm.00832-24 |  |
| Primary diagnostic criteria | Most reliable evidence of acute infection: **HCV RNA positive with anti-HCV negative** (seronegative window) or **documented anti-HCV seroconversion within 6 months**; proposed primary criteria also include **HCV RNA positivity in a previously RNA-negative patient**. Anti-HCV + HCV RNA indicates active infection but **does not distinguish acute from chronic**. (fasano2024acutehepatitisc pages 2-4) | Review | Fasano, 2024, *Viruses* | https://doi.org/10.3390/v16111739 |  |
| Secondary diagnostic criteria | Supportive criteria include **ALT >5× upper limit of normal**, **known/suspected exposure within preceding 6 months**, **exclusion of other causes of acute liver injury**, **sudden onset of liver disease**, and compatible symptoms/signs such as **jaundice**. About **80%** of acute infections are asymptomatic. (fasano2024acutehepatitisc pages 2-4, liu2023acutehepatitisc pages 5-6) | Review | Fasano, 2024, *Viruses*; Liu, 2023, *Clin Mol Hepatol* | https://doi.org/10.3390/v16111739 ; https://doi.org/10.3350/cmh.2022.0349 |  |
| Spontaneous clearance / progression | Spontaneous clearance is reported at roughly **10–45%** or **30–50%**; progression to chronic infection is reported at about **50–70%**, **60–85%**, or approximately **80%** in some reviews, reflecting heterogeneity by population and case definition. Acute liver failure is **<1%**. (fasano2024acutehepatitisc pages 4-5, sallam2024contemporaryinsightsinto pages 10-11, fasano2024acutehepatitisc pages 7-8, liu2023acutehepatitisc pages 5-6, fasano2024acutehepatitisc pages 1-2) | Review | Fasano, 2024, *Viruses*; Liu, 2023, *Clin Mol Hepatol* | https://doi.org/10.3390/v16111739 ; https://doi.org/10.3350/cmh.2022.0349 |  |
| Host factors linked to clearance | Higher spontaneous clearance is associated with **female sex**, **younger age**, symptomatic presentation, absence of HIV coinfection, and host genetics including **IL28B/IFNL3 rs12979860 CC**, **rs8099917 TT**, and HLA class II alleles such as **DQB1*02, DQB1*03, DRB1*04, DRB1*11**; strong HCV-specific CD4+/CD8+ responses also favor clearance. (liu2023acutehepatitisc pages 5-6, fasano2024acutehepatitisc pages 4-5, kaur2025anexhaustiveupdate pages 4-6) | Review | Liu, 2023, *Clin Mol Hepatol* | https://doi.org/10.3350/cmh.2022.0349 |  |
| Key risk groups / transmission routes | Main routes are **parenteral exposure**, especially **people who inject drugs (PWID)** and unsafe healthcare procedures. Other at-risk groups/routes include **intranasal illicit drug users**, **MSM**, **people living with HIV**, **blood transfusion/transplant recipients before 1992**, **persons on long-term hemodialysis**, **incarcerated persons**, **vertical transmission**, and occupational exposure. In one Italian surveillance report, 2022 acute HCV incidence was **0.11/100,000** with **55 new cases**. (liu2023acutehepatitisc pages 1-3, liu2023acutehepatitisc pages 5-6, fasano2024acutehepatitisc pages 1-2, fasano2024acutehepatitisc pages 2-4) | Review / surveillance summary | Fasano, 2024, *Viruses*; Liu, 2023, *Clin Mol Hepatol* | https://doi.org/10.3390/v16111739 ; https://doi.org/10.3350/cmh.2022.0349 |  |
| Guideline treatment principle | AASLD-IDSA 2023 recommends **test-and-treat**: persons with **confirmed acute HCV infection (HCV RNA positive)** should be treated **the same as chronic HCV** and **should not wait for spontaneous clearance**. Universal DAA treatment is recommended for essentially all acute or chronic HCV except those with very limited life expectancy. **Abbreviated 6-week DAA regimens are not recommended** because response rates were inferior. (panel2023idsaguidelines pages 9-10, panel2023idsaguidelines pages 4-5) | Guideline | AASLD-IDSA Guidance Panel, 2023 |  |  |
| Recommended regimens / durations | Simplified AASLD-IDSA-aligned regimens suitable for acute or chronic treatment-naive infection include **glecaprevir/pibrentasvir for 8 weeks** and **sofosbuvir/velpatasvir for 12 weeks**; EASL-based reviews discuss **8-week** pangenotypic courses for acute infection, but AASLD-IDSA treats acute HCV with **standard chronic regimens**. (fasano2024acutehepatitisc pages 5-7, fasano2024acutehepatitisc pages 4-5, pan2024revampinghepatitisc pages 2-4, pan2024revampinghepatitisc pages 1-2, liu2023acutehepatitisc pages 12-13) | Guideline / review | Pan, 2024, *Transl Gastroenterol Hepatol*; Fasano, 2024, *Viruses* | https://doi.org/10.21037/tgh-23-104 ; https://doi.org/10.3390/v16111739 |  |
| Trial examples supporting regimen selection | Examples of acute/recent HCV DAA trials: **NCT04903626** phase 3, **8 weeks** glecaprevir/pibrentasvir, enrollment **286**; **NCT04042740** phase 2, **4 weeks** glecaprevir/pibrentasvir, enrollment **45**; **NCT03818308** phase 2, **8 weeks** sofosbuvir/velpatasvir, enrollment **20**; **NCT02634008** phase 3, recent HCV, **4–8 weeks** DAA strategies, enrollment **83**. (NCT03818308 chunk 1, NCT02634008 chunk 1, NCT04903626 chunk 1, NCT04042740 chunk 1) | Trial registry | ClinicalTrials.gov records, 2014–2021 | https://clinicaltrials.gov/study/NCT04903626 ; https://clinicaltrials.gov/study/NCT04042740 ; https://clinicaltrials.gov/study/NCT03818308 ; https://clinicaltrials.gov/study/NCT02634008 |  |


*Table: This table summarizes high-yield evidence for defining, diagnosing, and managing acute hepatitis C virus infection, including diagnostic windows, natural history, risk groups, and current guideline-based treatment. It is useful as a concise knowledge-base-ready abstraction anchored to the gathered evidence contexts.*

---

## 1. Disease information

### 1.1 Overview / definition (current understanding)
* **Acute / recently acquired HCV infection** is generally defined as the **first 6 months after initial exposure**; **chronic HCV infection** is defined by **persistence of viremia for >6 months**. (fasano2024acutehepatitisc pages 1-2, fasano2024acutehepatitisc pages 4-5, liu2023acutehepatitisc pages 5-6)
* The term “acute hepatitis C” is used variably (biological vs clinical definitions are not completely standardized), and many incident infections are **clinically silent**. (fasano2024acutehepatitisc pages 4-5, liu2023acutehepatitisc pages 5-6)

### 1.2 Key identifiers and controlled vocabularies
* **ICD-10:** **B17.1 = Acute hepatitis C**. (macri2023acuteseverehepatitis pages 2-3)
* **ICD-11:** Not directly retrievable for *acute* hepatitis C from the available sources in this run; one GBD-methods paper indicates ICD-11 codes for *chronic* hepatitis C and sequelae (cirrhosis/HCC), but does not provide a stem code for acute infection. (bai2025globalregionaland pages 1-2)
* **MeSH / MONDO:** Not directly retrievable from the available sources in this run (no authoritative MeSH descriptor record or MONDO ID located in retrieved evidence). (fasano2024acutehepatitisc pages 1-2, fasano2024acutehepatitisc pages 2-4)

### 1.3 Synonyms / alternative names
* **Acute hepatitis C**
* **Recent(ly) acquired HCV infection**
* **Incident HCV infection**
* **Early phase of HCV infection** (fasano2024acutehepatitisc pages 1-2, fasano2024acutehepatitisc pages 4-5, fasano2024acutehepatitisc pages 2-4)

### 1.4 Evidence provenance (patient-level vs aggregated)
The information below is derived primarily from **aggregated resources** (reviews/guidelines, surveillance summaries, GBD analyses, and clinical trial registries), rather than individual EHR case series. (fasano2024acutehepatitisc pages 2-4, zou2024epidemiologyofacute pages 1-2, liu2023acutehepatitisc pages 3-5, NCT03818308 chunk 1)

---

## 2. Etiology

### 2.1 Disease causal factors
* **Causative agent:** Hepatitis C virus (HCV), a blood-borne, enveloped RNA virus; acute infection follows exposure and may progress to chronic infection with long-term liver disease. (zilouchian2025currentandfuture pages 1-3, fasano2024acutehepatitisc pages 1-2)

### 2.2 Risk factors
#### 2.2.1 Transmission routes and high-risk populations
Major routes and groups consistently identified:
* **Parenteral exposure**, especially **people who inject drugs (PWID)** and **unsafe medical procedures**. (liu2023acutehepatitisc pages 1-3, liu2023acutehepatitisc pages 5-6, fasano2024acutehepatitisc pages 1-2)
* **Sexual transmission** is particularly important among **men who have sex with men (MSM)** and **people living with HIV (PLWH)**, often linked to sexual risk behavior and recreational drug use. (fasano2024acutehepatitisc pages 1-2, fasano2024acutehepatitisc pages 2-4)
* Additional at-risk groups include: **intranasal illicit drug users**, **blood transfusion/transplant recipients before 1992**, **persons on long-term hemodialysis**, and **people ever incarcerated**. (fasano2024acutehepatitisc pages 2-4)

Quantitative incidence estimates in key populations (examples):
* In MSM: pooled HCV incidence in **HIV-positive MSM ~8.46/1,000 person-years**; in **HIV-negative MSM on PrEP ~14.80/1,000 person-years** (vs **0.12/1,000 person-years** in HIV-negative MSM not on PrEP). (liu2023acutehepatitisc pages 3-5)
* In PWID: incidence can be extremely high early after initiation of injecting (up to **133 per 100 person-years** in the first year in young PWID, as summarized in a clinical review). (liu2023acutehepatitisc pages 3-5)

#### 2.2.2 Host genetic and immunologic risk/clearance modifiers
A 2023 clinical update summarizes host factors associated with spontaneous clearance (SC) versus progression:
* **Higher likelihood of SC:** female sex; white ethnicity; absence of HIV coinfection; HBV coinfection; **IL28B/IFNL3 genotypes rs12979860 CC and rs8099917 TT**; specific **HLA class II alleles** (**DQB1*02, DQB1*03, DRB1*04, DRB1*11**); strong HCV-specific T-cell responses; limited quasispecies diversity. (liu2023acutehepatitisc pages 5-6)

### 2.3 Protective factors
Evidence in the retrieved sources supports that protective factors largely overlap with predictors of spontaneous clearance:
* **IFNL3/IL28B favorable genotypes** and certain **HLA class II alleles** increase odds of clearance in acute infection. (liu2023acutehepatitisc pages 5-6)

### 2.4 Gene–environment interactions
Evidence suggests host genotype interacts with immune context and exposure environment:
* Sex and interferon-lambda genotype can shape intrahepatic antiviral gene networks and immune response patterns in HCV infection (with implications for outcome variability and response to therapy), highlighting a biologically plausible gene–environment/host–pathogen interaction framework. (toma2025hepatitiscvirus pages 1-2)

---

## 3. Phenotypes (clinical features)

### 3.1 Common clinical presentation
* **Asymptomatic** infection is common: ~**80%** of acute infections may be asymptomatic. (liu2023acutehepatitisc pages 5-6)
* Symptomatic acute hepatitis C occurs in a minority; one review reports **~20%** symptomatic (fatigue, anorexia, nausea/vomiting, abdominal pain, jaundice). (fasano2024acutehepatitisc pages 4-5)
* **Incubation period:** ~2–20 weeks (typical ~7 weeks) in reviews. (sallam2024contemporaryinsightsinto pages 10-11)

### 3.2 Laboratory abnormalities and dynamics
* ALT elevation can be a key clue; supportive diagnostic criteria include **ALT >5× ULN**. (fasano2024acutehepatitisc pages 2-4)
* Viral kinetics: an early “pre-ramp-up” phase (2–14 days), “ramp-up” (8–10 days), then a “plateau” (45–68 days) has been described in a clinical update (relevant to early-diagnosis challenges). (liu2023acutehepatitisc pages 5-6)

### 3.3 Rare/severe manifestations
* **Acute liver failure** is rare in acute HCV, reported as **<1%** of cases in a 2024 review. (fasano2024acutehepatitisc pages 4-5)

### 3.4 Suggested HPO terms (mapping suggestions)
These are *ontology mapping suggestions* for knowledge-base use (not asserted as exhaustive):
* **Jaundice** (HP:0000952)
* **Fatigue** (HP:0012378)
* **Nausea** (HP:0002018)
* **Vomiting** (HP:0002013)
* **Abdominal pain** (HP:0002027)
* **Elevated hepatic transaminases** / **Elevated alanine aminotransferase** (often represented via “Abnormal liver function test”; lab-phenotype HPO mapping may vary by curation practice)

### 3.5 Quality-of-life impact
Direct, acute-phase QoL metrics (e.g., SF-36/EQ-5D) were not retrievable from the sources in this run; however, asymptomatic presentation is common, and symptomatic episodes can reduce functioning transiently (fatigue, nausea, jaundice). (fasano2024acutehepatitisc pages 4-5, liu2023acutehepatitisc pages 5-6)

---

## 4. Genetic / molecular information

### 4.1 Causal genes
Acute hepatitis C is **not** a Mendelian genetic disease; it is caused by **HCV infection**. Host genetics act mainly as **modifiers** of clearance and disease course. (liu2023acutehepatitisc pages 5-6)

### 4.2 Modifier genes / loci supported in retrieved evidence
* **IFNL3 / IL28B** polymorphisms (e.g., **rs12979860**, **rs8099917**) are associated with spontaneous clearance likelihood. (liu2023acutehepatitisc pages 5-6)
* **HLA class II alleles** (e.g., **DQB1*02, DQB1*03, DRB1*04, DRB1*11**) are associated with spontaneous clearance in summarized evidence. (liu2023acutehepatitisc pages 5-6)

### 4.3 Epigenetics and chromosomal abnormalities
Not specifically retrievable for *acute* infection from the sources in this run.

---

## 5. Environmental information

### 5.1 Environmental / healthcare-associated factors
* Unsafe medical procedures (e.g., unsafe injections, invasive procedures) remain important in some regions; a clinical update emphasizes ongoing healthcare-associated transmission in some WHO regions. (liu2023acutehepatitisc pages 1-3)

### 5.2 Lifestyle / behavioral factors
* Injection drug use–related behaviors (shared syringes and preparation equipment, frequent injections, multiple injecting partners) are highlighted as major drivers of transmission. (liu2023acutehepatitisc pages 5-6)

### 5.3 Infectious agent
* **Hepatitis C virus** is the relevant infectious agent. (zilouchian2025currentandfuture pages 1-3)

---

## 6. Mechanism / pathophysiology

### 6.1 Causal chain (high-level)
1. **Exposure and entry:** Blood-borne (primarily) exposure introduces HCV; viremia becomes detectable early. (fasano2024acutehepatitisc pages 2-4, liu2023acutehepatitisc pages 5-6)
2. **Early replication and innate/adaptive response:** Viral RNA rises rapidly; liver inflammation and ALT elevation may follow. (liu2023acutehepatitisc pages 5-6)
3. **Outcome bifurcation (clearance vs persistence):** A subset clears infection spontaneously (linked to robust CD4+/CD8+ responses and favorable host genetics); the remainder progresses to chronic infection. (liu2023acutehepatitisc pages 5-6, fasano2024acutehepatitisc pages 4-5)

### 6.2 Immune system involvement (evidence-based highlights)
* Clearance is associated with **broad, multi-specific CD4+ and CD8+ T-cell responses**; maintenance of virus-specific CD4+ responses and HCV-specific CD8+ T cells correlate with viral clearance in summarized evidence. (fasano2024acutehepatitisc pages 4-5, fasano2024acutehepatitisc pages 8-10)

### 6.3 Suggested GO biological process terms (mechanism-oriented)
Mapping suggestions for knowledge-base annotation:
* **Type I interferon signaling pathway** (GO:0060337) / **response to virus** (GO:0009615)
* **T cell activation** (GO:0042110)
* **antigen processing and presentation** (e.g., GO:0019882)

### 6.4 Suggested Cell Ontology (CL) terms (cell types)
Mapping suggestions:
* **Hepatocyte** (CL:0000182)
* **CD4-positive, alpha-beta T cell** (CL:0000624)
* **CD8-positive, alpha-beta T cell** (CL:0000625)

### 6.5 Molecular profiling / omics
* Intrahepatic transcriptional responses vary by host factors; a liver transcriptomics study in HCV identified sex- and IFNL4/IL28B-associated differences in antiviral modules (supporting biologic heterogeneity relevant to outcomes and therapy response). (toma2025hepatitiscvirus pages 1-2)

---

## 7. Anatomical structures affected

### 7.1 Organ/system level
* Primary organ: **liver** (acute hepatitis). (fasano2024acutehepatitisc pages 4-5)

### 7.2 Suggested UBERON term
* **Liver** (UBERON:0002107)

---

## 8. Temporal development (natural history)

### 8.1 Onset and staging
* Viremia detectable by NAT within **~1–2 weeks** after exposure; seroconversion typically **4–12 weeks**. (fasano2024acutehepatitisc pages 2-4)
* Acute phase is generally defined as **≤6 months** post-exposure. (liu2023acutehepatitisc pages 5-6)

### 8.2 Progression and remission
* Spontaneous clearance occurs in a minority (estimates vary by population and definition), while a large fraction progresses to chronic infection; one review emphasizes **~50–70%** progress to chronic infection (viremia >6 months). (fasano2024acutehepatitisc pages 4-5)

---

## 9. Inheritance and population

### 9.1 Epidemiology (recent statistics)
**Global burden and incidence (GBD/WHO summaries):**
* A 2023 clinical update summarizes WHO estimates of **~1.5 million newly acquired HCV infections in 2019**, with regional distribution noted (e.g., Eastern Mediterranean ~470k, Europe ~300k). (liu2023acutehepatitisc pages 3-5)
* A 2024 GBD-based analysis of reproductive-age women reported that global incidences of acute hepatitis C increased **46.45% from 1990 to 2019** in this demographic. (zou2024epidemiologyofacute pages 1-2)

**Europe (surveillance context):**
* EU/EEA crude reported hepatitis C rate in 2022 was about **6.2 per 100,000** (23,273 cases), with a COVID-era dip and 2022 rebound. (simao2024hepatitiscvirus pages 1-2)

**Key populations (PWID):**
* In 25 European countries, civil-society monitoring notes HCV seroprevalence among PWID ranging **16%–86%** and identifies PWID as the main source of new cases. (maticic2024howfarare pages 1-2)

### 9.2 Demographics
* Males accounted for about **54.6% of new infections** in 2019 in summarized global estimates. (liu2023acutehepatitisc pages 3-5)

---

## 10. Diagnostics

### 10.1 Diagnostic concepts and definitions (acute vs chronic)
* Acute diagnosis is most robust when there is **HCV RNA positivity with negative anti-HCV** (window period) or **documented anti-HCV seroconversion within 6 months**. (fasano2024acutehepatitisc pages 2-4)
* Anti-HCV positive + HCV RNA positive confirms active infection but **does not distinguish acute from chronic** without prior testing history. (fasano2024acutehepatitisc pages 2-4)

### 10.2 Testing windows and algorithms (key data)
* **HCV RNA detectability:** ~**1–2 weeks post-exposure**. (fasano2024acutehepatitisc pages 2-4, liu2023acutehepatitisc pages 5-6)
* **Anti-HCV antibodies:** typically **4–12 weeks**, and may be **delayed/absent** in PLWH, hemodialysis, and transplant recipients—necessitating RNA-based testing. (fasano2024acutehepatitisc pages 2-4)

### 10.3 Diagnostic algorithm (visual)
Figure evidence for the acute HCV diagnostic algorithm is available here: (fasano2024acutehepatitisc media 039e3907)

### 10.4 Emerging / improved diagnostics (2023–2024 emphasis)
* A 2024 clinical microbiology study evaluated a **dual antibody/core antigen assay** (Roche Elecsys HCV Duo) vs standard antibody + NAAT algorithms, noting fourth-generation Ab/Ag assays can shorten the diagnostic window by **2.2–21.9 days** vs Ab-only assays; NAAT still detects some Ab−/RNA+ infections missed by serology/Ag. (bui2024comparisonofa pages 2-4, bui2024comparisonofa pages 1-2)

### 10.5 Differential diagnosis
Acute hepatitis C diagnostic criteria explicitly include **exclusion of other causes of acute hepatitis** (HAV, HBV, HDV in chronic HBV, autoimmune hepatitis). (fasano2024acutehepatitisc pages 2-4)

---

## 11. Outcome / prognosis

### 11.1 Clearance vs chronicity
* Progression to chronic infection is common; multiple sources report ranges (e.g., **50–70%** progressing to chronic, with spontaneous clearance in the remainder). (fasano2024acutehepatitisc pages 4-5, sallam2024contemporaryinsightsinto pages 10-11, liu2023acutehepatitisc pages 5-6)

### 11.2 Complications
* Acute liver failure is rare (<1%), but untreated chronic infection drives long-term fibrosis/cirrhosis/HCC risk (contextualized in reviews). (fasano2024acutehepatitisc pages 4-5, zilouchian2025currentandfuture pages 1-3)

---

## 12. Treatment

### 12.1 Current guideline position (expert consensus)
* **AASLD–IDSA 2023 guidance:** treat **confirmed acute HCV infection** the same as chronic infection and **do not wait** for spontaneous clearance (“test-and-treat”). (panel2023idsaguidelines pages 9-10)
* The guidance does **not recommend abbreviated 6-week DAA courses** for acute infection because trials showed inferior responses. (panel2023idsaguidelines pages 9-10)

### 12.2 Simplified pangenotypic regimens used in practice (including acute)
A 2024 article summarizing AASLD–IDSA 2023 simplified guidance states that the following regimens are suitable for **acute or chronic** treatment-naive infection under simplified pathways (with standard exclusions such as pregnancy and decompensated cirrhosis):
* **Glecaprevir/pibrentasvir (G/P): 8 weeks**
* **Sofosbuvir/velpatasvir (SOF/VEL): 12 weeks** (pan2024revampinghepatitisc pages 1-2, pan2024revampinghepatitisc pages 2-4)

### 12.3 Clinical trials and real-world implementation examples (NCT identifiers)
Recent/important acute-HCV DAA trials in ClinicalTrials.gov (illustrative, not exhaustive):
* **NCT04903626** (AbbVie): Phase 3, single-arm, **G/P 8 weeks**, **n=286**, completed 2024-09-17; primary endpoint SVR12. (NCT04903626 chunk 1)
* **NCT04042740** (ACTG PURGE-C): Phase 2, **G/P 4 weeks**, **n=45**, completed; SVR12 primary endpoint; results posted July 2024. (NCT04042740 chunk 1)
* **NCT03818308** (HepNet-aHCV-V): Phase 2, **SOF/VEL 8 weeks**, **n=20**, completed. (NCT03818308 chunk 1)
* **NCT02128217** (SWIFT-C): Phase 1, HIV-coinfected adults; sofosbuvir-based regimens (SOF+RBV 12 weeks; LDV/SOF 8 weeks), **n=44**. (NCT02128217 chunk 1)

### 12.4 MAXO (Medical Action Ontology) term suggestions
Mapping suggestions for curation:
* Direct-acting antiviral therapy (MAXO term selection depends on local MAxO release; suggested concept: “antiviral therapy” / “direct-acting antiviral therapy”)
* HCV RNA testing (diagnostic action)
* Harm-reduction intervention (preventive action)

---

## 13. Prevention

### 13.1 Primary prevention
* Universal precautions, safe injection practices, and harm reduction are repeatedly emphasized in clinical reviews for reducing acute transmission. (liu2023acutehepatitisc pages 1-3, liu2023acutehepatitisc pages 5-6)

### 13.2 Secondary prevention (screening / early detection)
* AASLD–IDSA-aligned summaries emphasize **universal one-time adult screening** and repeat/annual screening in high-risk groups, with reflex HCV RNA after antibody testing. (pan2024revampinghepatitisc pages 1-2)

### 13.3 Vaccine landscape
* **No prophylactic HCV vaccine is currently available**, and major scientific obstacles include HCV genetic diversity and limited animal models. (liu2023acutehepatitisc pages 1-3, fasano2024acutehepatitisc pages 7-8)

---

## 14. Other species / natural disease
Not specifically addressed in retrieved sources for acute infection in this run. (The broader literature includes non-human primate and humanized mouse systems for HCV, but authoritative citations were not retrieved here.)

---

## 15. Model organisms
Not specifically addressed in retrieved sources for acute infection in this run.

---

## Notes on evidence gaps (transparent limitations)
* **MONDO ID** and **MeSH descriptor IDs** for acute hepatitis C were not found in the retrieved corpus for this run; these would normally be sourced from MONDO/MeSH browser records rather than primary clinical studies. (fasano2024acutehepatitisc pages 2-4)
* ICD-11 **acute** hepatitis C stem code was not located in the retrieved evidence; ICD-11 was referenced primarily in the context of chronic/sequelae coding in a GBD methods paper. (bai2025globalregionaland pages 1-2)

---

## Key sources (with URLs and publication dates)
* Liu & Kao. *Clinical and Molecular Hepatology*. **July 2023**. “Acute hepatitis C virus infection: clinical update and remaining challenges.” https://doi.org/10.3350/cmh.2022.0349 (liu2023acutehepatitisc pages 1-3)
* Fasano et al. *Viruses*. **Nov 2024**. “Acute Hepatitis C: Current Status and Future Perspectives.” https://doi.org/10.3390/v16111739 (fasano2024acutehepatitisc pages 1-2)
* Pan & Park. *Translational Gastroenterology and Hepatology*. **Apr 2024**. “Revamping hepatitis C global eradication efforts: towards simplified and enhanced screening, prevention, and treatment.” https://doi.org/10.21037/tgh-23-104 (pan2024revampinghepatitisc pages 1-2)
* Bui et al. *Journal of Clinical Microbiology*. **Oct 2024**. “Comparison of a dual antibody and antigen HCV immunoassay to standard of care algorithmic testing.” https://doi.org/10.1128/jcm.00832-24 (bui2024comparisonofa pages 2-4)
* Zou et al. *Journal of Global Health*. **Apr 2024**. “Epidemiology of acute hepatitis C … in reproductive-age women, 1990–2019 (GBD).” https://doi.org/10.7189/jogh.14.04077 (zou2024epidemiologyofacute pages 1-2)


References

1. (fasano2024acutehepatitisc pages 1-2): Massimo Fasano, Francesco Ieva, Marianna Ciarallo, Bruno Caccianotti, and Teresa Antonia Santantonio. Acute hepatitis c: current status and future perspectives. Viruses, 16:1739, Nov 2024. URL: https://doi.org/10.3390/v16111739, doi:10.3390/v16111739. This article has 21 citations.

2. (liu2023acutehepatitisc pages 5-6): Chen-Hua Liu and Jia-Horng Kao. Acute hepatitis c virus infection: clinical update and remaining challenges. Clinical and Molecular Hepatology, 29:623-642, Jul 2023. URL: https://doi.org/10.3350/cmh.2022.0349, doi:10.3350/cmh.2022.0349. This article has 93 citations.

3. (fasano2024acutehepatitisc pages 2-4): Massimo Fasano, Francesco Ieva, Marianna Ciarallo, Bruno Caccianotti, and Teresa Antonia Santantonio. Acute hepatitis c: current status and future perspectives. Viruses, 16:1739, Nov 2024. URL: https://doi.org/10.3390/v16111739, doi:10.3390/v16111739. This article has 21 citations.

4. (panel2023idsaguidelines pages 9-10): AIHCVG Panel. Idsa guidelines. Unknown journal, 2023.

5. (fasano2024acutehepatitisc pages 4-5): Massimo Fasano, Francesco Ieva, Marianna Ciarallo, Bruno Caccianotti, and Teresa Antonia Santantonio. Acute hepatitis c: current status and future perspectives. Viruses, 16:1739, Nov 2024. URL: https://doi.org/10.3390/v16111739, doi:10.3390/v16111739. This article has 21 citations.

6. (zilouchian2025currentandfuture pages 4-6): Hussein Zilouchian, Omair Faqah, Md Alamgir Kabir, Dennis Gross, Rachel Pan, Shane Shaifman, Muhammad Awais Younas, Muhammad Abdul Haseeb, Emmanuel Thomas, and Waseem Asghar. Current and future diagnostics for hepatitis c virus infection. Chemosensors, 13:31, Jan 2025. URL: https://doi.org/10.3390/chemosensors13020031, doi:10.3390/chemosensors13020031. This article has 7 citations.

7. (bui2024comparisonofa pages 1-2): Tina I. Bui, Abigail P. Brown, Meghan Brown, Sydney Lawless, Brittany Roemmich, Neil W. Anderson, and Christopher W. Farnsworth. Comparison of a dual antibody and antigen hcv immunoassay to standard of care algorithmic testing. Journal of Clinical Microbiology, Oct 2024. URL: https://doi.org/10.1128/jcm.00832-24, doi:10.1128/jcm.00832-24. This article has 7 citations and is from a peer-reviewed journal.

8. (galli2025hcvserologyan pages 12-13): Claudio Galli and M. Plebani. Hcv serology: an unfinished agenda. Clinical chemistry and laboratory medicine, Aug 2025. URL: https://doi.org/10.1515/cclm-2025-0501, doi:10.1515/cclm-2025-0501. This article has 0 citations and is from a peer-reviewed journal.

9. (sallam2024contemporaryinsightsinto pages 10-11): Malik Sallam and Roaa Khalil. Contemporary insights into hepatitis c virus: a comprehensive review. Microorganisms, 12:1035, May 2024. URL: https://doi.org/10.3390/microorganisms12061035, doi:10.3390/microorganisms12061035. This article has 63 citations.

10. (fasano2024acutehepatitisc pages 7-8): Massimo Fasano, Francesco Ieva, Marianna Ciarallo, Bruno Caccianotti, and Teresa Antonia Santantonio. Acute hepatitis c: current status and future perspectives. Viruses, 16:1739, Nov 2024. URL: https://doi.org/10.3390/v16111739, doi:10.3390/v16111739. This article has 21 citations.

11. (kaur2025anexhaustiveupdate pages 4-6): Kulvinder Kochar Kaur, Gautam Nand Allahbadia, and Mandeep Singh. An exhaustive update on eradication of hepatitis c virus (hcv) with the objective of eradicating chronic hepatitis by 2030- a narrative review. Journal of Infectious Diseases &amp; Treatments, pages 1-21, Dec 2025. URL: https://doi.org/10.61440/jidt.2025.v3.48, doi:10.61440/jidt.2025.v3.48. This article has 0 citations.

12. (liu2023acutehepatitisc pages 1-3): Chen-Hua Liu and Jia-Horng Kao. Acute hepatitis c virus infection: clinical update and remaining challenges. Clinical and Molecular Hepatology, 29:623-642, Jul 2023. URL: https://doi.org/10.3350/cmh.2022.0349, doi:10.3350/cmh.2022.0349. This article has 93 citations.

13. (panel2023idsaguidelines pages 4-5): AIHCVG Panel. Idsa guidelines. Unknown journal, 2023.

14. (fasano2024acutehepatitisc pages 5-7): Massimo Fasano, Francesco Ieva, Marianna Ciarallo, Bruno Caccianotti, and Teresa Antonia Santantonio. Acute hepatitis c: current status and future perspectives. Viruses, 16:1739, Nov 2024. URL: https://doi.org/10.3390/v16111739, doi:10.3390/v16111739. This article has 21 citations.

15. (pan2024revampinghepatitisc pages 2-4): Calvin Q. Pan and James S. Park. Revamping hepatitis c global eradication efforts: towards simplified and enhanced screening, prevention, and treatment. Translational Gastroenterology and Hepatology, 9:30-30, Apr 2024. URL: https://doi.org/10.21037/tgh-23-104, doi:10.21037/tgh-23-104. This article has 5 citations and is from a peer-reviewed journal.

16. (pan2024revampinghepatitisc pages 1-2): Calvin Q. Pan and James S. Park. Revamping hepatitis c global eradication efforts: towards simplified and enhanced screening, prevention, and treatment. Translational Gastroenterology and Hepatology, 9:30-30, Apr 2024. URL: https://doi.org/10.21037/tgh-23-104, doi:10.21037/tgh-23-104. This article has 5 citations and is from a peer-reviewed journal.

17. (liu2023acutehepatitisc pages 12-13): Chen-Hua Liu and Jia-Horng Kao. Acute hepatitis c virus infection: clinical update and remaining challenges. Clinical and Molecular Hepatology, 29:623-642, Jul 2023. URL: https://doi.org/10.3350/cmh.2022.0349, doi:10.3350/cmh.2022.0349. This article has 93 citations.

18. (NCT03818308 chunk 1):  Trial for the Treatment of Acute Hepatitis C for 8 Weeks With Sofosbuvir/Velpatasvir. Hannover Medical School. 2019. ClinicalTrials.gov Identifier: NCT03818308

19. (NCT02634008 chunk 1):  Treatment of Recently Acquired Hepatitis C With the 3D Regimen or G/P. Kirby Institute. 2016. ClinicalTrials.gov Identifier: NCT02634008

20. (NCT04903626 chunk 1):  Study to Evaluate Adverse Events and Change in Disease Activity in Adult and Adolescent Participants With Acute Hepatitis C Virus (HCV) Infection on Treatment With Oral Tablets of Glecaprevir (GLE)/Pibrentasvir (PIB). AbbVie. 2021. ClinicalTrials.gov Identifier: NCT04903626

21. (NCT04042740 chunk 1):  Glecaprevir/Pibrentasvir Fixed-dose Combination Treatment for Acute Hepatitis C Virus Infection. Advancing Clinical Therapeutics Globally for HIV/AIDS and Other Infections. 2019. ClinicalTrials.gov Identifier: NCT04042740

22. (macri2023acuteseverehepatitis pages 2-3): Jennifer Macri, Vanessa Morton, Megan Hame, Pierre-Luc Trépanier, and Marina Salvadori. Acute severe hepatitis of unknown origin in children in canada. Canada Communicable Disease Report, 49:256-262, Jun 2023. URL: https://doi.org/10.14745/ccdr.v49i06a02, doi:10.14745/ccdr.v49i06a02. This article has 3 citations.

23. (bai2025globalregionaland pages 1-2): Junzhu Bai, Hengliang Lv, Longhao Wang, Shumeng You, Dan Liu, Lilin Wang, Yuanyong Xu, Junfeng Lu, and Wenyi Zhang. Global, regional, and national burden of hepatitis c from 1990 to 2021 and projections until 2030. BMC Infectious Diseases, Dec 2025. URL: https://doi.org/10.1186/s12879-025-12396-y, doi:10.1186/s12879-025-12396-y. This article has 0 citations and is from a peer-reviewed journal.

24. (zou2024epidemiologyofacute pages 1-2): Yanzheng Zou, Ming Yue, Xiangyu Ye, Yifan Wang, Xinyan Ma, Amei Zhang, Xueshan Xia, Hongbo Chen, Rongbin Yu, Sheng Yang, and Peng Huang. Epidemiology of acute hepatitis c and hepatitis c virus-related cirrhosis in reproductive-age women, 1990–2019: an analysis of the global burden of disease study. Journal of Global Health, Apr 2024. URL: https://doi.org/10.7189/jogh.14.04077, doi:10.7189/jogh.14.04077. This article has 11 citations and is from a peer-reviewed journal.

25. (liu2023acutehepatitisc pages 3-5): Chen-Hua Liu and Jia-Horng Kao. Acute hepatitis c virus infection: clinical update and remaining challenges. Clinical and Molecular Hepatology, 29:623-642, Jul 2023. URL: https://doi.org/10.3350/cmh.2022.0349, doi:10.3350/cmh.2022.0349. This article has 93 citations.

26. (zilouchian2025currentandfuture pages 1-3): Hussein Zilouchian, Omair Faqah, Md Alamgir Kabir, Dennis Gross, Rachel Pan, Shane Shaifman, Muhammad Awais Younas, Muhammad Abdul Haseeb, Emmanuel Thomas, and Waseem Asghar. Current and future diagnostics for hepatitis c virus infection. Chemosensors, 13:31, Jan 2025. URL: https://doi.org/10.3390/chemosensors13020031, doi:10.3390/chemosensors13020031. This article has 7 citations.

27. (toma2025hepatitiscvirus pages 1-2): Daniela Toma, Lucreția Anghel, Diana Patraș, and A. Ciubara. Hepatitis c virus: epidemiological challenges and global strategies for elimination. Viruses, Jul 2025. URL: https://doi.org/10.3390/v17081069, doi:10.3390/v17081069. This article has 18 citations.

28. (fasano2024acutehepatitisc pages 8-10): Massimo Fasano, Francesco Ieva, Marianna Ciarallo, Bruno Caccianotti, and Teresa Antonia Santantonio. Acute hepatitis c: current status and future perspectives. Viruses, 16:1739, Nov 2024. URL: https://doi.org/10.3390/v16111739, doi:10.3390/v16111739. This article has 21 citations.

29. (simao2024hepatitiscvirus pages 1-2): Margarida Simão and Cristina Gonçalves. Hepatitis c virus infection in europe. Pathogens, 13:841, Sep 2024. URL: https://doi.org/10.3390/pathogens13100841, doi:10.3390/pathogens13100841. This article has 7 citations.

30. (maticic2024howfarare pages 1-2): Mojca Maticic, J. Cernosa, C. Loboda, J. Tamse, R. Rigoni, E. Duffell, I. Indave, R. Zimmermann, L. Darragh, J. Moura, A. Leicht, T. Windelinckx, M. Jauffret-Roustide, K. Schiffer, and T. Tammi. How far are we? assessing progress in hepatitis c response towards the who 2030 elimination goals by the civil society monitoring in 25 european countries, period 2020 to 2023. Harm Reduction Journal, Nov 2024. URL: https://doi.org/10.1186/s12954-024-01115-6, doi:10.1186/s12954-024-01115-6. This article has 3 citations and is from a peer-reviewed journal.

31. (fasano2024acutehepatitisc media 039e3907): Massimo Fasano, Francesco Ieva, Marianna Ciarallo, Bruno Caccianotti, and Teresa Antonia Santantonio. Acute hepatitis c: current status and future perspectives. Viruses, 16:1739, Nov 2024. URL: https://doi.org/10.3390/v16111739, doi:10.3390/v16111739. This article has 21 citations.

32. (bui2024comparisonofa pages 2-4): Tina I. Bui, Abigail P. Brown, Meghan Brown, Sydney Lawless, Brittany Roemmich, Neil W. Anderson, and Christopher W. Farnsworth. Comparison of a dual antibody and antigen hcv immunoassay to standard of care algorithmic testing. Journal of Clinical Microbiology, Oct 2024. URL: https://doi.org/10.1128/jcm.00832-24, doi:10.1128/jcm.00832-24. This article has 7 citations and is from a peer-reviewed journal.

33. (NCT02128217 chunk 1):  Sofosbuvir-Containing Regimens Without Interferon For Treatment of Acute Hepatitis C Virus (HCV) Infection. Advancing Clinical Therapeutics Globally for HIV/AIDS and Other Infections. 2014. ClinicalTrials.gov Identifier: NCT02128217