---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-24T13:13:40.973115'
end_time: '2026-04-24T13:37:55.075665'
duration_seconds: 1454.1
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Endometrial Carcinoma
  mondo_id: ''
  category: ''
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 55
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Endometrial Carcinoma
- **MONDO ID:**  (if available)
- **Category:** 

## Research Objectives

Please provide a comprehensive research report on **Endometrial Carcinoma** covering all of the
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
- **Disease Name:** Endometrial Carcinoma
- **MONDO ID:**  (if available)
- **Category:** 

## Research Objectives

Please provide a comprehensive research report on **Endometrial Carcinoma** covering all of the
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


# Comprehensive Research Report: Endometrial Carcinoma (Endometrial Cancer)

## Target Disease
- **Disease Name:** Endometrial carcinoma (endometrial cancer; uterine corpus carcinoma)
- **MONDO ID:** Not retrieved from the accessed full texts in this run (gap noted).
- **Category:** Malignant epithelial tumor of the uterine corpus/endometrium.

## 1. Disease Information

### 1.1 Overview (current understanding)
Endometrial carcinoma (EC) is a heterogeneous malignancy arising from the endometrial lining of the uterine corpus. Contemporary clinical management is increasingly guided by integrated histologic and molecular classification, particularly the four-group TCGA/ProMisE framework (POLE-mutated, mismatch repair deficient, p53-abnormal, and no specific molecular profile), which stratifies prognosis and influences treatment selection. (kuhn2024unsolvedissuesin pages 1-2, kuhn2024unsolvedissuesin pages 5-6, ribeirosantos2024tailoringendometrialcancer pages 2-3)

### 1.2 Synonyms and alternative names
Commonly used synonyms in the literature include **endometrial cancer**, **endometrial carcinoma**, and **uterine corpus cancer** (often grouped under “uterine cancer” in registry statistics and clinical practice discussions). (rodriguez2025trendsinendometrial pages 1-2, guo2025trendsinendometrial pages 15-18)

### 1.3 Key identifiers (ICD/MeSH/MONDO)
The retrieved full-text sources used here did **not** explicitly provide ICD-10/ICD-11 codes, MeSH IDs, or MONDO IDs for endometrial carcinoma. Where ontology identifiers are required for knowledge-base population, an additional targeted ontology lookup (e.g., MONDO/MeSH/ICD browsers) is needed beyond the currently retrieved corpus. (kuhn2024unsolvedissuesin pages 4-5, kuhn2024unsolvedissuesin pages 1-2)

### 1.4 Evidence provenance (patient vs aggregated)
Most information summarized here derives from **aggregated evidence**: randomized phase III trials, national cancer registries (SEER/USCS-based analyses), and systematic reviews/meta-analyses. (tubridy2024treatmentofnodepositive pages 7-8, eskander2023pembrolizumabpluschemotherapy pages 6-7, guo2025trendsinendometrial pages 4-12, clarke2018associationofendometrial pages 1-2)

## 2. Etiology

### 2.1 Causal factors and major mechanistic contributors
A major etiologic axis for many endometrioid endometrial carcinomas is **estrogen-driven proliferative signaling** (classically described in the Bokhman “Type I” pathway), whereas more aggressive non-endometrioid subtypes align with “Type II” biology in the historical dualistic model. (ribeirosantos2024tailoringendometrialcancer pages 2-3)

### 2.2 Risk factors

#### 2.2.1 Genetic risk factors
- **Lynch syndrome / mismatch repair (MMR) genes:** A subset of EC is associated with germline pathogenic variants affecting DNA mismatch repair (MLH1, MSH2, MSH6, PMS2). In a recent molecular-classification review, Lynch syndrome is estimated to account for **~2–5%** of endometrial cancers, while MMR/MSI alterations are much more common at the tumor level. (ribeirosantos2024tailoringendometrialcancer pages 2-3)

#### 2.2.2 Environmental and lifestyle risk factors
- **Obesity:** A large U.S. incidence trends analysis (2001–2021) highlights obesity as a dominant contributor, stating that **~60% of U.S. endometrial cancers are linked to obesity**. (guo2025trendsinendometrial pages 15-18)

### 2.3 Protective factors
Protective factors were not quantified in the retrieved endometrial-cancer-specific sources in this run; additional targeted searches (e.g., for hormonal contraception, parity, metformin/aspirin, weight loss interventions) would be required for evidence-backed estimates.

### 2.4 Gene–environment interactions
The retrieved sources did not provide direct quantitative gene–environment interaction estimates for EC. Mechanistically, interactions are plausible (e.g., obesity/hyperestrogenism interacting with PI3K pathway lesions), but specific GxE statistics were not extractable from the accessed documents.

## 3. Phenotypes (clinical presentation)

### 3.1 Key presenting features and frequencies
**Postmenopausal bleeding (PMB)** is a dominant presenting symptom:
- Meta-analysis: pooled **prevalence of PMB among women with endometrial cancer = 91% (95% CI 87–93%)**. (clarke2018associationofendometrial pages 1-2)
- Meta-analysis: pooled **risk of endometrial cancer among women presenting with PMB = 9% (95% CI 8–11%)**. (clarke2018associationofendometrial pages 1-2)
- Danish nationwide cohort (43,756 PMB patients): **absolute risk of endometrial cancer** after a first-time hospital PMB diagnosis was **4.66% at 1 year** and **5.18% at 5 years**. (bengtsen2019firsttimepostmenopausalbleeding pages 5-6)

### 3.2 Onset and course
Typical onset is **adult/postmenopausal**; however, incidence is rising among younger (premenopausal) women in U.S. registry analyses. (guo2025trendsinendometrial pages 4-12)

### 3.3 Quality of life impact
The retrieved sources did not provide disease-specific quantitative QoL instruments (e.g., EQ-5D, SF-36) or PROMIS metrics for EC in this run; however, symptom-driven care seeking (e.g., response to PMB) has recognized patient-level implications for timely diagnosis. (clarke2018associationofendometrial pages 1-2)

### 3.4 Suggested HPO terms (non-exhaustive)
- **Postmenopausal vaginal bleeding** (HPO suggestion; commonly mapped as abnormal uterine bleeding in ontologies)
- **Abnormal uterine bleeding**
- **Pelvic pain** (noted as common in diagnostic triage datasets) (doll2024endometrialthicknessas pages 1-2)

(Exact HPO IDs were not provided in the accessed texts and should be mapped via HPO lookup.)

## 4. Genetic/Molecular Information

### 4.1 Core molecular taxonomy (TCGA/ProMisE)
Endometrial carcinoma is commonly categorized into four major molecular groups used in routine practice: **POLE-mutated**, **MMR-deficient (MSI-hypermutated)**, **p53-abnormal (copy-number high/serous-like)**, and **NSMP (no specific molecular profile; copy-number low)**. (kuhn2024unsolvedissuesin pages 1-2, kuhn2024unsolvedissuesin pages 5-6, ribeirosantos2024tailoringendometrialcancer pages 2-3)

| Molecular subtype | Routine defining biomarker(s)/test(s) | Typical prognostic implication | Notable frequent gene alterations mentioned in retrieved sources | Evidence |
|---|---|---|---|---|
| POLE-mutated / POLE ultramutated (POLEmut) | Pathogenic **POLE exonuclease-domain sequencing**; WHO stepwise approach prioritizes POLE testing before MMR IHC and p53 IHC | **Excellent / extremely favorable prognosis**, even when conventional high-risk features are present | **POLE** exonuclease-domain mutations; may coexist with **TP53** mutations despite favorable outcome | (kuhn2024unsolvedissuesin pages 5-6, kuhn2024unsolvedissuesin pages 1-2, ribeirosantos2024tailoringendometrialcancer pages 2-3) |
| Mismatch repair-deficient / MSI-hypermutated (MMRd) | **MMR IHC** showing loss of **MLH1, MSH2, MSH6, and/or PMS2**; corresponds to MSI-hypermutated group | **Intermediate prognosis** | Loss/alteration of **MLH1, MSH2, MSH6, PMS2**; linked in some cases to **Lynch syndrome** | (kuhn2024unsolvedissuesin pages 5-6, ribeirosantos2024tailoringendometrialcancer pages 2-3, kuhn2024unsolvedissuesin pages 8-9) |
| p53-abnormal / p53-mutated / copy-number high (p53abn) | **p53 IHC** showing abnormal/aberrant pattern (e.g., overexpression or null); mapped to copy-number high / serous-like tumors | **Worst prognosis / poor outcome** | Frequent **TP53** mutations; often associated with **HER2 amplification** in serous-like tumors | (kuhn2024unsolvedissuesin pages 5-6, kuhn2024unsolvedissuesin pages 1-2, ribeirosantos2024tailoringendometrialcancer pages 2-3, kuhn2024unsolvedissuesin pages 8-9) |
| No specific molecular profile (NSMP) / copy-number low | Defined by **absence of pathogenic POLE mutation**, **retained MMR expression**, and **wild-type p53 IHC** after stepwise testing | **Intermediate prognosis**; prognosis also linked to stage | Common **PI3K pathway alterations**; genes mentioned include **PTEN, PIK3CA, KRAS, CTNNB1** | (kuhn2024unsolvedissuesin pages 5-6, ribeirosantos2024tailoringendometrialcancer pages 2-3, kuhn2024unsolvedissuesin pages 4-5) |


*Table: This table summarizes the four TCGA/ProMisE molecular subtypes of endometrial carcinoma, the routine biomarkers/tests used to classify them, their usual prognostic implications, and representative frequent alterations reported in the provided evidence snippets.*

### 4.2 Frequently altered genes and pathways (somatic)
Across subtypes, commonly discussed alterations include:
- **PI3K pathway lesions** and genes including **PTEN, PIK3CA**, and others; NSMP/copy-number low is described as often having PI3K pathway alterations. (ribeirosantos2024tailoringendometrialcancer pages 2-3)
- **TP53** mutations are frequent in the copy-number high/p53-abnormal group and are reported as common in non-endometrioid carcinomas; serous-like tumors may also show **HER2 amplification**. (ribeirosantos2024tailoringendometrialcancer pages 2-3)
- **MMR gene loss** (MLH1, MSH2, MSH6, PMS2) characterizes the MSI/MMRd group. (ribeirosantos2024tailoringendometrialcancer pages 2-3)

### 4.3 Epigenetics
MMR deficiency in EC can be driven by mechanisms including MLH1-related events; however, detailed epigenetic mechanisms (e.g., methylation subtype frequencies, chromatin programs) were not comprehensively extractable from the retrieved endometrial-cancer-specific texts in this run. (ribeirosantos2024tailoringendometrialcancer pages 2-3)

## 5. Environmental Information
This run retrieved limited EC-specific information beyond obesity-related burden. Environmental toxicant exposures and infectious etiologies were not supported by the accessed full texts; additional CTD/epidemiology searches would be required.

## 6. Mechanism / Pathophysiology

### 6.1 Conceptual causal chains (molecular-to-clinical)
- **MMRd/MSI pathway:** Loss of MMR protein function (tumor or germline) → increased mutation burden (MSI/hypermutation) → increased neoantigenicity → enhanced responsiveness to immune checkpoint blockade; clinically, this is reflected by substantially larger chemoimmunotherapy benefit in dMMR tumors versus pMMR in phase III trials. (ribeirosantos2024tailoringendometrialcancer pages 2-3, tubridy2024treatmentofnodepositive pages 7-8, eskander2023pembrolizumabpluschemotherapy pages 6-7)
- **p53-abnormal/copy-number high pathway:** TP53 dysfunction and copy-number alterations → aggressive biology and poorer outcomes, motivating intensified systemic strategies and molecularly informed staging. (kuhn2024unsolvedissuesin pages 1-2, ribeirosantos2024tailoringendometrialcancer pages 2-3, berek2023figostagingof pages 12-14)

### 6.2 Pathways and processes (suggested ontology mappings)
Evidence-supported pathway suggestions (to be mapped to GO/Reactome/KEGG IDs):
- **DNA mismatch repair** (MMRd group) (ribeirosantos2024tailoringendometrialcancer pages 2-3)
- **PI3K/AKT signaling** (common alterations in NSMP/copy-number low) (ribeirosantos2024tailoringendometrialcancer pages 2-3)
- **p53-mediated DNA damage response / cell-cycle control** (p53abn group) (ribeirosantos2024tailoringendometrialcancer pages 2-3)

Suggested GO biological process terms (text-supported but not explicitly enumerated in sources): DNA repair; regulation of cell cycle; apoptotic signaling.

Suggested CL (cell types) and UBERON (anatomy) are in Section 7.

## 7. Anatomical Structures Affected

### 7.1 Organ and tissue level
- Primary: **uterine corpus endometrium** (endometrium of the uterus). 
- Spread: clinically relevant metastatic patterns include pelvic/para-aortic lymph nodes and distant sites; orthotopic xenograft models recapitulate metastatic spread to clinically relevant locations. (yildiz2024murinexenograftmodels pages 10-12)

### 7.2 Cell types (CL suggestions)
- **Endometrial glandular epithelial cells** (carcinoma origin)
- **Tumor-associated stromal fibroblasts** (noting stromal replacement by murine stroma in xenografts) (yildiz2024murinexenograftmodels pages 5-6)
- **Tumor-infiltrating lymphocytes (e.g., CD8+ T cells)** in immunotherapy-responsive contexts (supported indirectly through immunotherapy responsiveness; detailed cell ontology mapping not provided in retrieved EC-specific texts).

### 7.3 Subcellular compartments (GO CC suggestions)
- Nucleus (DNA repair defects)
- Cytosol/cell membrane (signaling pathway dysregulation)

(Explicit GO cellular component IDs were not provided in the accessed texts.)

## 8. Temporal Development

### 8.1 Onset
- Rising incidence is documented both in premenopausal and postmenopausal groups in U.S. registry analyses, with particularly notable increases in ages 20–49 and ≥70 years. (guo2025trendsinendometrial pages 4-12)

### 8.2 Progression and staging
- Clinical course spans early-stage (often uterine-confined) through regional/distant spread.
- Modern staging has evolved to incorporate molecular markers for prognostic precision (FIGO 2023). (berek2023figostagingof pages 12-14)

## 9. Inheritance and Population

### 9.1 Epidemiology and disparities (recent registry analyses)
- U.S. incidence is increasing, with disproportionate increases among women of color in SEER-based analyses. In one analysis (2000–2019), early-onset (<50) average annual percent changes were highest in American Indian/Alaska Native women (4.8), followed by Black (3.3), Hispanic/Latina (3.1), and Asian/Pacific Islander women (2.4), with White women lowest (0.9). (rodriguez2025trendsinendometrial pages 1-2)
- Another U.S. registry analysis (2001–2021; hysterectomy-adjusted) reports incidence increases among ages 20–49 (86.8 to 113.8 per 1,000,000) and notes case-count declines in 2020 with an increased proportion of distant-stage cases consistent with pandemic-related diagnostic disruption. (guo2025trendsinendometrial pages 4-12)

### 9.2 Hereditary fraction
Lynch syndrome accounts for a minority of EC cases (estimated ~2–5% in a molecular pathology review), but tumor-level MMR deficiency is substantially more common and clinically actionable. (ribeirosantos2024tailoringendometrialcancer pages 2-3)

## 10. Diagnostics

### 10.1 Symptom-triggered evaluation
Given the high prevalence of PMB among EC cases (91%), PMB is a key clinical trigger for diagnostic workup. (clarke2018associationofendometrial pages 1-2)

### 10.2 Imaging and endometrial thickness (ET) triage
Transvaginal ultrasound (TVUS) ET thresholds are widely used but have limitations:
- A cohort study of women with bleeding found that ET alone did not always provide meaningful stratification for initial PMB presentations; in 593 PMB patients, EC prevalence was 7.9% and EIN 3.0%. (clarke2020riskassessmentof pages 1-2)
- In Black individuals, a JAMA Oncology diagnostic study found that with a <5 mm ET triage threshold, **11.4%** of EC cases would be missed; even at 4 mm the false-negative probability was 9.5%. The authors concluded ET triage is not reliable in this population and stated that with postmenopausal bleeding, **tissue sampling (biopsy) is strongly recommended**. (doll2024endometrialthicknessas pages 1-2)
- Review evidence notes that persistent or recurrent bleeding warrants endometrial examination regardless of ET; it also notes a meaningful fraction (25–34%) of type II cancers may present with thin/unclear endometrial echo, limiting TVUS utility. (asaturova2024advancementsinminimally pages 2-4)

### 10.3 Tissue diagnosis and pathology
- Endometrial biopsy (e.g., pipelle) and/or hysteroscopy with histopathology remain central to diagnosis; recurrent PMB pathways often escalate to hysteroscopy. (ghoubara2018endometrialpathologyin pages 8-12)

### 10.4 Molecular pathology implementation
WHO-endorsed stepwise classification uses **POLE sequencing → MMR IHC → p53 IHC** to assign tumors to POLEmut, MMRd, p53abn, or NSMP. (kuhn2024unsolvedissuesin pages 5-6)

### 10.5 FIGO 2023 staging (molecular integration)
FIGO 2023 integrates molecular classification into staging and recommends complete molecular classification. (berek2023figostagingof pages 12-14)
- In early stages, **POLEmut and p53abn can modify stage** (e.g., IAmPOLEmut; IICmp53abn), while MMRd and NSMP do not by themselves change stage. (berek2023figostagingof pages 12-14)
- Empirical cohort (China, 547 patients): **26.9%** experienced stage shifts under FIGO 2023; 63 FIGO 2009 stage I–II cases were reclassified as **IAmPOLEmut** and 53 as **IICmp53abn**. (yu2024clinicalapplicationof pages 1-2)

### 10.6 Differential diagnosis
Not systematically extractable from the accessed sources in this run; typical differentials include benign causes of abnormal bleeding (atrophy, polyps) and endometrial intraepithelial neoplasia.

## 11. Outcome / Prognosis

### 11.1 Prognostic stratification by molecular class
Molecular subgroup is prognostic: POLEmut is associated with excellent outcomes, p53abn with the worst outcomes, and MMRd/NSMP with intermediate outcomes. (kuhn2024unsolvedissuesin pages 1-2, kuhn2024unsolvedissuesin pages 5-6)

### 11.2 Prognosis in key systemic-therapy settings
In advanced/recurrent settings, randomized trials show substantial improvements in progression-free survival for chemoimmunotherapy, especially in dMMR tumors (see Treatment section). (tubridy2024treatmentofnodepositive pages 7-8, eskander2023pembrolizumabpluschemotherapy pages 6-7)

## 12. Treatment

### 12.1 Key concepts (current standard and rapidly evolving areas)
Systemic therapy is increasingly **molecularly and biomarker guided**, especially by MMR status and integrated TCGA/ProMisE class. The “front-line” (first-line) paradigm for advanced/recurrent disease has shifted toward adding PD-1/PD-L1 blockade to platinum-taxane chemotherapy based on 2023 NEJM phase III trials. (tubridy2024treatmentofnodepositive pages 7-8, eskander2023pembrolizumabpluschemotherapy pages 6-7)

### 12.2 Surgery and radiation (standard of care backbone)
The retrieved sources primarily focused on systemic therapy; they nevertheless describe node-positive management as multimodal with systemic therapy with/without radiation and evolving integration of immunotherapy and IMRT approaches. (tubridy2024treatmentofnodepositive pages 7-8)

### 12.3 Systemic therapy: pivotal trials (2023–2024 prioritized)

#### 12.3.1 Frontline chemoimmunotherapy
**RUBY (dostarlimab + carboplatin/paclitaxel)** (NEJM, Jun 2023; DOI URL in paper record)
- dMMR/MSI-H subgroup: 24-month PFS **61.4%** with dostarlimab vs **15.7%** placebo; HR **0.28** (95% CI 0.16–0.50). (tubridy2024treatmentofnodepositive pages 7-8)
- Overall population: 24-month PFS 36.1% vs 18.1%; HR 0.64; and 24-month OS 71.3% vs 56.0% (as reported in accessible summaries). (ribeirosantos2024tailoringendometrialcancer pages 1-2)
- Regulatory implementation: FDA approval of dostarlimab with carboplatin/paclitaxel followed by single-agent dostarlimab for primary/recurrent **MMRd** EC is reported as **July 31, 2023**. (tubridy2024treatmentofnodepositive pages 8-9)

**NRG-GY018 (pembrolizumab + carboplatin/paclitaxel)** (NEJM, Jun 2023; DOI URL in paper record)
- dMMR cohort: 12-month freedom from progression/death **74%** vs 38%; HR **0.30** (95% CI 0.19–0.48; P<0.001). (eskander2023pembrolizumabpluschemotherapy pages 6-7)
- pMMR cohort: median PFS **13.1 months** vs 8.7 months; HR **0.54** (95% CI 0.41–0.71; P<0.001). (eskander2023pembrolizumabpluschemotherapy pages 6-7)

#### 12.3.2 Immunotherapy + PARP inhibition strategy
**DUO-E (durvalumab + carboplatin/paclitaxel → maintenance durvalumab ± olaparib)** (JCO, Jan 2024; DOI URL in paper record)
- Review-reported primary results: ITT PFS HR **0.71** for durvalumab vs control and **0.55** for durvalumab+olaparib vs control; subgroup PFS benefit was observed in both dMMR and pMMR cohorts. (shim2024majorclinicalresearch pages 3-5)

#### 12.3.3 Second-line / previously treated advanced disease (pMMR emphasis)
**Study 309 / KEYNOTE-775 update (lenvatinib + pembrolizumab vs chemotherapy)** (JCO, Jun 2023)
- Updated efficacy: OS benefit in pMMR (HR 0.70) and all-comers (HR 0.65); PFS benefit in pMMR (HR 0.60) and all-comers (HR 0.56); ORR improved (pMMR 32.4% vs 15.1%; all-comers 33.8% vs 14.7%). (luvero2024oldissuesand pages 5-6)

### 12.4 Real-world implementation examples
- A multicenter retrospective study (Russia; pMMR/MSS recurrent/metastatic EC) reported median PFS **7.75 months** and partial response **24%** with lenvatinib+pembrolizumab; dose reductions occurred in **44%**. (luvero2024oldissuesand pages 5-6)

### 12.5 Treatment ontology suggestions (MAXO; examples)
(Exact MAXO IDs not provided in accessed texts; suggested mappings)
- Hysterectomy / surgical resection
- External beam radiation therapy
- Brachytherapy
- Platinum-based chemotherapy (carboplatin)
- Taxane chemotherapy (paclitaxel)
- PD-1 inhibitor therapy (pembrolizumab, dostarlimab)
- PD-L1 inhibitor therapy (durvalumab)
- Multimodal chemoimmunotherapy
- Tyrosine kinase inhibitor therapy (lenvatinib)
- PARP inhibitor therapy (olaparib)

## 13. Prevention

### 13.1 Primary prevention
Obesity reduction is a major prevention lever given the strong contribution of obesity to EC burden in U.S. analyses. (guo2025trendsinendometrial pages 15-18)

### 13.2 Secondary prevention / early detection
No population-wide screening program is established in the retrieved sources; rather, symptom-triggered evaluation (particularly PMB) is central. PMB-focused strategies can potentially identify ~90% of EC cases because PMB prevalence among EC is ~91%, although most PMB presentations are not cancer. (clarke2018associationofendometrial pages 1-2)

### 13.3 High-risk hereditary prevention
The accessed corpus confirms Lynch syndrome relevance and emphasizes molecular tumor testing (MMR IHC/MSI) as a practical gateway to identify patients who may need genetic counseling/testing; however, detailed prophylaxis timing and guideline algorithms were not fully extractable here. (ribeirosantos2024tailoringendometrialcancer pages 2-3)

## 14. Other Species / Natural Disease
No comparative veterinary natural-disease evidence was retrieved in the accessed documents for this run.

## 15. Model Organisms / Preclinical Models

### 15.1 Xenograft and PDX models
- Uterine corpus malignancy PDX establishment: **52 PDX models from 92 patient tumors (56.5% success)** with similarity of pathology and gene profiles between primary and PDX tumors. (ueda2024consistencybetweenprimary pages 1-2)
- A xenograft-model review reports broad engraftment variability by histology and implantation method; limitations include murine stromal replacement, selection biases, and long timelines. (yildiz2024murinexenograftmodels pages 5-6)

### 15.2 Organoid-based models and organoid-derived xenografts
- Organoid-based patient-derived xenograft (O-PDX) mouse model (Frontiers in Oncology, May 2024) demonstrated that an MRI radiomics signature could predict response over time; reported AUCs increased from **0.38 (baseline)** to **1.0 (endpoint)** in the orthotopic cohort, with external validation AUC **0.85** at day 10/endpoint. (espedal2024mriradiomicscaptures pages 1-2)

### 15.3 Limitations noted by experts
Preclinical model limitations include long establishment times, incomplete immune microenvironment representation (especially in xenografts), and potential divergence over passages; therefore, continued development of immunocompetent or humanized models is highlighted as a major need. (yildiz2024murinexenograftmodels pages 5-6, yildiz2024murinexenograftmodels pages 17-19)

---

## Expert synthesis (2023–2024 emphasis)
A convergent theme across 2023–2024 literature is that EC is no longer best conceptualized as a single disease entity; instead, integrated histo-molecular classification and FIGO 2023 staging are driving risk stratification and therapeutic personalization. The magnitude of benefit seen in dMMR tumors in frontline chemoimmunotherapy (e.g., NRG-GY018 and RUBY) provides clinical proof that mechanistic tumor features (MMR status) are predictive and actionable. (eskander2023pembrolizumabpluschemotherapy pages 6-7, tubridy2024treatmentofnodepositive pages 7-8, berek2023figostagingof pages 12-14)

## URLs and publication dates (examples of core sources used)
- Eskander RN et al. **“Pembrolizumab plus Chemotherapy in Advanced Endometrial Cancer.”** *NEJM* (Jun 2023). https://doi.org/10.1056/NEJMoa2302312 (eskander2023pembrolizumabpluschemotherapy pages 6-7)
- Mirza MR et al. **“Dostarlimab for Primary Advanced or Recurrent Endometrial Cancer.”** *NEJM* (Jun 2023). https://doi.org/10.1056/NEJMoa2216334 (ribeirosantos2024tailoringendometrialcancer pages 1-2)
- Westin SN et al. **DUO-E trial report.** *JCO* (Jan 2024). https://doi.org/10.1200/JCO.23.02132 (westin2024durvalumabpluscarboplatinpaclitaxel pages 2-4)
- Makker V et al. **KEYNOTE-775 update.** *JCO* (Jun 2023). https://doi.org/10.1200/JCO.22.02152 (luvero2024oldissuesand pages 5-6)
- Berek JS et al. **“FIGO staging of endometrial cancer: 2023.”** *Int J Gynecol Obstet* (Jun 2023). https://doi.org/10.1002/ijgo.14923 (berek2023figostagingof pages 12-14)
- Doll KM et al. **Endometrial thickness triage in Black individuals.** *JAMA Oncology* (Aug 2024). https://doi.org/10.1001/jamaoncol.2024.1891 (doll2024endometrialthicknessas pages 1-2)
- Clarke MA et al. **PMB meta-analysis.** *Obstet Gynecol Surv* (Dec 2018). https://doi.org/10.1097/OGX.0000000000000623 (clarke2018associationofendometrial pages 1-2)

## Notable evidence gaps in this run (for knowledge-base completion)
- Formal **ICD/MeSH/MONDO identifiers** were not found in the accessed full texts.
- Comprehensive, evidence-backed **protective factors**, **environmental toxicants**, **differential diagnosis lists**, and **QoL instrument statistics** were not retrievable from the current document set and require targeted retrieval.


References

1. (kuhn2024unsolvedissuesin pages 1-2): Elisabetta Kuhn, Donatella Gambini, Letterio Runza, Stefano Ferrero, Giovanna Scarfone, Gaetano Bulfamante, and Ayse Ayhan. Unsolved issues in the integrated histo-molecular classification of endometrial carcinoma and therapeutic implications. Cancers, 16:2458, Jul 2024. URL: https://doi.org/10.3390/cancers16132458, doi:10.3390/cancers16132458. This article has 7 citations.

2. (kuhn2024unsolvedissuesin pages 5-6): Elisabetta Kuhn, Donatella Gambini, Letterio Runza, Stefano Ferrero, Giovanna Scarfone, Gaetano Bulfamante, and Ayse Ayhan. Unsolved issues in the integrated histo-molecular classification of endometrial carcinoma and therapeutic implications. Cancers, 16:2458, Jul 2024. URL: https://doi.org/10.3390/cancers16132458, doi:10.3390/cancers16132458. This article has 7 citations.

3. (ribeirosantos2024tailoringendometrialcancer pages 2-3): Pedro Ribeiro-Santos, Carolina Martins Vieira, Gilson Gabriel Viana Veloso, Giovanna Vieira Giannecchini, Martina Parenza Arenhardt, Larissa Müller Gomes, Pedro Zanuncio, Flávio Silva Brandão, and Angélica Nogueira-Rodrigues. Tailoring endometrial cancer treatment based on molecular pathology: current status and possible impacts on systemic and local treatment. International Journal of Molecular Sciences, 25:7742, Jul 2024. URL: https://doi.org/10.3390/ijms25147742, doi:10.3390/ijms25147742. This article has 21 citations.

4. (rodriguez2025trendsinendometrial pages 1-2): Victoria E Rodriguez, Sora Park Tanjasiri, Annie Ro, Michael A Hoyt, Robert E Bristow, and Alana M W LeBrón. Trends in endometrial cancer incidence in the united states by race/ethnicity and age of onset from 2000 to 2019. American journal of epidemiology, 194:103-113, Jul 2025. URL: https://doi.org/10.1093/aje/kwae178, doi:10.1093/aje/kwae178. This article has 19 citations and is from a domain leading peer-reviewed journal.

5. (guo2025trendsinendometrial pages 15-18): Fangjian Guo, Victor Adekanmbi, Christine D. Hsu, Thao N. Hoang, Pamela T. Soliman, Jacques G. Baillargeon, and Abbey B. Berenson. Trends in endometrial cancer incidence among premenopausal and postmenopausal women in the united states between 2001 and 2021. Cancers, 17:1035, Mar 2025. URL: https://doi.org/10.3390/cancers17061035, doi:10.3390/cancers17061035. This article has 11 citations.

6. (kuhn2024unsolvedissuesin pages 4-5): Elisabetta Kuhn, Donatella Gambini, Letterio Runza, Stefano Ferrero, Giovanna Scarfone, Gaetano Bulfamante, and Ayse Ayhan. Unsolved issues in the integrated histo-molecular classification of endometrial carcinoma and therapeutic implications. Cancers, 16:2458, Jul 2024. URL: https://doi.org/10.3390/cancers16132458, doi:10.3390/cancers16132458. This article has 7 citations.

7. (tubridy2024treatmentofnodepositive pages 7-8): Elizabeth A. Tubridy, Neil K. Taunk, and Emily M. Ko. Treatment of node-positive endometrial cancer: chemotherapy, radiation, immunotherapy, and targeted therapy. Current Treatment Options in Oncology, 25:330-345, Jan 2024. URL: https://doi.org/10.1007/s11864-023-01169-x, doi:10.1007/s11864-023-01169-x. This article has 21 citations and is from a peer-reviewed journal.

8. (eskander2023pembrolizumabpluschemotherapy pages 6-7): Ramez N. Eskander, Michael W. Sill, Lindsey Beffa, Richard G. Moore, Joanie M. Hope, Fernanda B. Musa, Robert Mannel, Mark S. Shahin, Guilherme H. Cantuaria, Eugenia Girda, Cara Mathews, Juraj Kavecansky, Charles A. Leath, Lilian T. Gien, Emily M. Hinchcliff, Shashikant B. Lele, Lisa M. Landrum, Floor Backes, Roisin E. O’Cearbhaill, Tareq Al Baghdadi, Emily K. Hill, Premal H. Thaker, Veena S. John, Stephen Welch, Amanda N. Fader, Matthew A. Powell, and Carol Aghajanian. Pembrolizumab plus chemotherapy in advanced endometrial cancer. New England Journal of Medicine, 388:2159-2170, Jun 2023. URL: https://doi.org/10.1056/nejmoa2302312, doi:10.1056/nejmoa2302312. This article has 768 citations and is from a highest quality peer-reviewed journal.

9. (guo2025trendsinendometrial pages 4-12): Fangjian Guo, Victor Adekanmbi, Christine D. Hsu, Thao N. Hoang, Pamela T. Soliman, Jacques G. Baillargeon, and Abbey B. Berenson. Trends in endometrial cancer incidence among premenopausal and postmenopausal women in the united states between 2001 and 2021. Cancers, 17:1035, Mar 2025. URL: https://doi.org/10.3390/cancers17061035, doi:10.3390/cancers17061035. This article has 11 citations.

10. (clarke2018associationofendometrial pages 1-2): Megan A. Clarke, Beverly J. Long, Arena Del Mar Morillo, Marc Arbyn, Jamie N. Bakkum-Gamez, and Nicolas Wentzensen. Association of endometrial cancer risk with postmenopausal bleeding in women: a systematic review and meta-analysis. Obstetrical &amp; Gynecological Survey, 73:687-688, Dec 2018. URL: https://doi.org/10.1097/ogx.0000000000000623, doi:10.1097/ogx.0000000000000623. This article has 553 citations and is from a peer-reviewed journal.

11. (bengtsen2019firsttimepostmenopausalbleeding pages 5-6): Maria B. Bengtsen, Katalin Veres, and Mette Nørgaard. First-time postmenopausal bleeding as a clinical marker of long-term cancer risk: a danish nationwide cohort study. British Journal of Cancer, 122:445-451, Dec 2019. URL: https://doi.org/10.1038/s41416-019-0668-2, doi:10.1038/s41416-019-0668-2. This article has 29 citations and is from a domain leading peer-reviewed journal.

12. (doll2024endometrialthicknessas pages 1-2): Kemi M. Doll, Mindy Pike, Julianna Alson, Patrice Williams, Erin Carey, Til Stürmer, Mollie Wood, Erica E. Marsh, Ronit Katz, and Whitney R. Robinson. Endometrial thickness as diagnostic triage for endometrial cancer among black individuals. JAMA Oncology, 10:1068, Aug 2024. URL: https://doi.org/10.1001/jamaoncol.2024.1891, doi:10.1001/jamaoncol.2024.1891. This article has 25 citations and is from a highest quality peer-reviewed journal.

13. (kuhn2024unsolvedissuesin pages 8-9): Elisabetta Kuhn, Donatella Gambini, Letterio Runza, Stefano Ferrero, Giovanna Scarfone, Gaetano Bulfamante, and Ayse Ayhan. Unsolved issues in the integrated histo-molecular classification of endometrial carcinoma and therapeutic implications. Cancers, 16:2458, Jul 2024. URL: https://doi.org/10.3390/cancers16132458, doi:10.3390/cancers16132458. This article has 7 citations.

14. (berek2023figostagingof pages 12-14): Jonathan S. Berek, Xavier Matias‐Guiu, Carien Creutzberg, Christina Fotopoulou, David Gaffney, Sean Kehoe, Kristina Lindemann, David Mutch, and Nicole Concin. Figo staging of endometrial cancer: 2023. International Journal of Gynecology & Obstetrics, 162:383-394, Jun 2023. URL: https://doi.org/10.1002/ijgo.14923, doi:10.1002/ijgo.14923. This article has 1270 citations and is from a peer-reviewed journal.

15. (yildiz2024murinexenograftmodels pages 10-12): Merve Yildiz, Andrea Romano, and Sofia Xanthoulea. Murine xenograft models as preclinical tools in endometrial cancer research. Cancers, 16:3994, Nov 2024. URL: https://doi.org/10.3390/cancers16233994, doi:10.3390/cancers16233994. This article has 1 citations.

16. (yildiz2024murinexenograftmodels pages 5-6): Merve Yildiz, Andrea Romano, and Sofia Xanthoulea. Murine xenograft models as preclinical tools in endometrial cancer research. Cancers, 16:3994, Nov 2024. URL: https://doi.org/10.3390/cancers16233994, doi:10.3390/cancers16233994. This article has 1 citations.

17. (clarke2020riskassessmentof pages 1-2): Megan A. Clarke, Beverly J. Long, Mark E. Sherman, Maureen A. Lemens, Karl C. Podratz, Matthew R. Hopkins, Lisa J. Ahlberg, Lois J. Mc Guire, Shannon K. Laughlin-Tommaso, Jamie N. Bakkum-Gamez, and Nicolas Wentzensen. Risk assessment of endometrial cancer and endometrial intraepithelial neoplasia in women with abnormal bleeding and implications for clinical management algorithms. American Journal of Obstetrics and Gynecology, 223:549.e1-549.e13, Oct 2020. URL: https://doi.org/10.1016/j.ajog.2020.03.032, doi:10.1016/j.ajog.2020.03.032. This article has 106 citations and is from a highest quality peer-reviewed journal.

18. (asaturova2024advancementsinminimally pages 2-4): Aleksandra Asaturova, Andrew Zaretsky, Aleksandra Rogozhina, Anna Tregubova, and Alina Badlaeva. Advancements in minimally invasive techniques and biomarkers for the early detection of endometrial cancer: a comprehensive review of novel diagnostic approaches and clinical implications. Journal of Clinical Medicine, 13:7538, Dec 2024. URL: https://doi.org/10.3390/jcm13247538, doi:10.3390/jcm13247538. This article has 10 citations.

19. (ghoubara2018endometrialpathologyin pages 8-12): A. Ghoubara, S. Sundar, and A. A. A. Ewies. Endometrial pathology in recurrent postmenopausal bleeding: observational study of 385 women. Climacteric, 21:391-396, May 2018. URL: https://doi.org/10.1080/13697137.2018.1461825, doi:10.1080/13697137.2018.1461825. This article has 24 citations and is from a peer-reviewed journal.

20. (yu2024clinicalapplicationof pages 1-2): Changmin Yu, Xinhui Yuan, Qianlan Yao, Yuyin Xu, Xiaoyan Zhou, Xin Hu, Huijuan Yang, Huaying Wang, Xiaoli Zhu, and Yulan Ren. Clinical application of figo 2023 staging system of endometrial cancer in a chinese cohort. BMC Cancer, Jul 2024. URL: https://doi.org/10.1186/s12885-024-12633-8, doi:10.1186/s12885-024-12633-8. This article has 12 citations and is from a peer-reviewed journal.

21. (ribeirosantos2024tailoringendometrialcancer pages 1-2): Pedro Ribeiro-Santos, Carolina Martins Vieira, Gilson Gabriel Viana Veloso, Giovanna Vieira Giannecchini, Martina Parenza Arenhardt, Larissa Müller Gomes, Pedro Zanuncio, Flávio Silva Brandão, and Angélica Nogueira-Rodrigues. Tailoring endometrial cancer treatment based on molecular pathology: current status and possible impacts on systemic and local treatment. International Journal of Molecular Sciences, 25:7742, Jul 2024. URL: https://doi.org/10.3390/ijms25147742, doi:10.3390/ijms25147742. This article has 21 citations.

22. (tubridy2024treatmentofnodepositive pages 8-9): Elizabeth A. Tubridy, Neil K. Taunk, and Emily M. Ko. Treatment of node-positive endometrial cancer: chemotherapy, radiation, immunotherapy, and targeted therapy. Current Treatment Options in Oncology, 25:330-345, Jan 2024. URL: https://doi.org/10.1007/s11864-023-01169-x, doi:10.1007/s11864-023-01169-x. This article has 21 citations and is from a peer-reviewed journal.

23. (shim2024majorclinicalresearch pages 3-5): Seung-Hyuk Shim, Jung-Yun Lee, Yoo-Young Lee, Jeong-Yeol Park, Yong Jae Lee, Se Ik Kim, Gwan Hee Han, Eun Jung Yang, Joseph J Noh, Ga Won Yim, Joo-Hyuk Son, Nam Kyeong Kim, Tae-Hyun Kim, Tae-Wook Kong, Youn Jin Choi, Angela Cho, Hyunji Lim, Eun Bi Jang, Hyun Woong Cho, and Dong Hoon Suh. Major clinical research advances in gynecologic cancer in 2023: a tumultuous year for endometrial cancer. Journal of Gynecologic Oncology, Jan 2024. URL: https://doi.org/10.3802/jgo.2024.35.e66, doi:10.3802/jgo.2024.35.e66. This article has 9 citations and is from a peer-reviewed journal.

24. (luvero2024oldissuesand pages 5-6): Daniela Luvero, Gianna Barbara Cundari, Fernando Ficarola, Francesco Plotti, Corrado Terranova, Roberto Montera, Giorgio Bogani, Adele Silvagni, Federica Celoro, and Roberto Angioli. Old issues and new perspectives on endometrial cancer therapy: how molecular characteristics are changing the therapeutic pathway. Cancers, 16:1866, May 2024. URL: https://doi.org/10.3390/cancers16101866, doi:10.3390/cancers16101866. This article has 3 citations.

25. (ueda2024consistencybetweenprimary pages 1-2): Shoko Ueda, Tomohito Tanaka, Kensuke Hirosuna, Shunsuke Miyamoto, Hikaru Murakami, Ruri Nishie, Hiromitsu Tsuchihashi, Akihiko Toji, Natsuko Morita, Sousuke Hashida, Atsushi Daimon, Shinichi Terada, Hiroshi Maruoka, Yuhei Kogata, Kohei Taniguchi, Kazumasa Komura, and Masahide Ohmichi. Consistency between primary uterine corpus malignancies and their corresponding patient-derived xenograft models. International Journal of Molecular Sciences, 25:1486, Jan 2024. URL: https://doi.org/10.3390/ijms25031486, doi:10.3390/ijms25031486. This article has 0 citations.

26. (espedal2024mriradiomicscaptures pages 1-2): Heidi Espedal, Kristine E. Fasmer, Hege F. Berg, Jenny M. Lyngstad, Tomke Schilling, Camilla Krakstad, and Ingfrid S. Haldorsen. Mri radiomics captures early treatment response in patient-derived organoid endometrial cancer mouse models. Frontiers in Oncology, May 2024. URL: https://doi.org/10.3389/fonc.2024.1334541, doi:10.3389/fonc.2024.1334541. This article has 6 citations.

27. (yildiz2024murinexenograftmodels pages 17-19): Merve Yildiz, Andrea Romano, and Sofia Xanthoulea. Murine xenograft models as preclinical tools in endometrial cancer research. Cancers, 16:3994, Nov 2024. URL: https://doi.org/10.3390/cancers16233994, doi:10.3390/cancers16233994. This article has 1 citations.

28. (westin2024durvalumabpluscarboplatinpaclitaxel pages 2-4): Shannon N. Westin, Kathleen Moore, Hye Sook Chon, Jung-Yun Lee, Jessica Thomes Pepin, Michael Sundborg, Ayelet Shai, Joseph de la Garza, Shin Nishio, Michael A. Gold, Ke Wang, Kristi McIntyre, Todd D. Tillmanns, Stephanie V. Blank, Ji-Hong Liu, Michael McCollum, Fernando Contreras Mejia, Tadaaki Nishikawa, Kathryn Pennington, Zoltan Novak, Andreia Cristina De Melo, Jalid Sehouli, Dagmara Klasa-Mazurkiewicz, Christos Papadimitriou, Marta Gil-Martin, Birute Brasiuniene, Conor Donnelly, Paula Michelle del Rosario, Xiaochun Liu, Els Van Nieuwenhuysen, Sophia Frentzas, Kichendasse Ganessan, Bo Gao, Tarek Meniawy, Linda Mileshkin, Gary Richardson, Felicia Roncolato, Jean-Francois Baurain, Maryam Bourhaba, Eveline De Cuypere, Philip Debruyne, Hannelore Denys, Frederic Forget, Brigitte Honhon, Eric Joosens, Els Van Nieuwenhuysen, Vanessa da Costa Miranda, Andreia Cristina De Melo, Joao Daniel Guedes, Charles Andree Joseph de Padua, Nicolas Lazaretti, Carolina Martins Vieira, Andre Mattar, Daniela Neves Palmeiro, Christina Pimentel Oppermann Kussler, Pedro Emanuel Rubini Liedke, Joao Soares Nunes, Katsuki Arima Tiscoski, Allan Covens, Lara De Guerke, Prafull Ghatage, Lucy Gilbert, Susie Lau, Amit Oza, Diane Provencher, Omar Touhami, Li Congzhu, Wang Danbo, Lou Ge, Zhu Gen-Hai, Li Guiling, Shi Hong, Zheng Hong, Wen Hongwu, Liu Ji-Hong, Wang Jing, Wang Ke, Jiang Kui, Li Li, Wang Li, Hao Min, Zhou Qi, Gao Qinglei, Liao Sihai, Zhang Songling, Zhao Weidong, Xiaohua Wu, Wang Wuliang, Rutie Yin, Cheng Ying, Zhang Yu, Liang Zhiqing, Fernando Contreras Mejia, Angel Luis Hernandez, Carolina Ortiz Lopez, Carlos Javier Pacheco, Pedro Luis Ramos Guette, Jaime Rendon Pereira, Julian Rivera Diaz, Tomas Sanchez Villegas, Juan Pablo Suso, Marco Antonio Torregroza Otero, Karin Grisan, Elen Vettus, Bahriye Aktas, Eva Egger, Petra Krabisch, Andreas Muller, Joachim Rom, Jalid Sehouli, Antje Sperfeld, Pauline Wimberger, Andreas Zorr, George Fountzilas, Sofia Karageorgopoulou, Christos Papadimitriou, Amanda Psyrri, Florai Zagour, Karen Kar Loen Chan, Wing Ming Ho, Tibor Csoszi, Laszlo Landherr, Zoltan Novak, Zsuzsanna Papai, Robert Poka, Istvan Sipocz, Paul Devinder, Lovenish Goyal, Sudeep Gupta, Radheshyam Naik, Tushar Patil, S.P. Somashekhar, Ilan Bruchim, Svetlana Kovel, Anca Leibovici, Ora Rosengarten, Tamar Safra, Wataru Yamagami, Junzo Hamanishi, Yuichi Imai, Nobuhiro Kado, Shoji Kamiura, Hienori Kato, Eiji Kondo, Wataru Kudaka, Takashi Matsumoto, Masahiko Mori, Tadaaki Nishikawa, Shin Nishio, Aikou Okamoto, Mayu Yunokawa, Masayuki Sekine, Toshiyuki Sumi, Hirokuni Takano, Kazuhiro Takehara, Birute Brasiuniene, Arturas Inciura, Goda Jonuskiene, Jesus Elvis Cabrera Luviano, Adriana Dominguez-Andrade, Raquel Gerson-Cwilich, Carlos Hernandez Hernandez, Jesus Lopez Hernandez, Jose Luis Martinez Lira, Jaime Esteban Navarrete Aleman, Jessica Reyes Contreras, Vanessa Rosas Camargo, Wieslawa Bednarek, Dagmara Klasa-Mazurkiewicz, Tomasz Kubiatowski, Piotr Potemski, Magdalena Sikorska, Suk-Joon Chang, Sook Hee Hong, Sokbom Kang, Byoung-Gie Kim, Jan-Weon Kim, Yong Man Kim, Jung-Yun Lee, Sang Young Ryu, Yong Jung Song, Dmitriy Kirtbaya, Julya Kreynina, Alla Lisyanskaya, Yulia Makarova, Rashida Orlova, Albert Pirmagomedov, Valeria Saevets, Sufia Safina, Pavel Skopin, Alexandra Tyulyandina, Sheow Lei Lim, Lynette Ngo Su Mien, David Tan Shao Peng, Lay Tin Soh, Jesus Alarcon Company, Pilar Barretina, Purificacion Estevez-Garcia, Isaura Fernandez Perez, Fernando Galvez, Yolanda Garcia, Marta Gil-Martin, Jeronimo Martinez, Andres Redondo-Sanchez, Charles Anderson, Tara Berman, Stephanie Blank, William Bradley, James Burke, Fabio Cappuccini, Michael Carney, Setsuko Chambers, Lee-May Chen, Hye Sook Chon, Joseph de la Garza, Stephen Depasquale, Paul DiSilvestro, Babak Edraki, Evelyn Fleming, Jenny Fox, Michael Gold, Mary Gordinier, Michael Guy, Ellen Hartenbach, Chisten Haygood, Scott Jordan, Larry Kilgore, Young Kim, Joseph Lucci, Michael McCollum, Michael Mchale, Kristi McIntyre, Mark Messing, Eirwen Miller, Kathleen Moore, John Moroney, Michaela Onstad, Taylor Ortiz, Sobia Ozair, Kathryn Pennington, Krista Pfaendler, Anna Priebe, Terri Pustilnik, Kimberly Resnick, Peter Rose, Erin Salinas, Sudarshan Sharma, Urszula Sobol, Pamela Soliman, David Starks, Michael Sundborg, Eleonora Teplinsky, Jessica Thomes-Pepin, Todd Tillmanns, David Warshal, Shannon N. Westin, and Thomas Woliver. Durvalumab plus carboplatin/paclitaxel followed by maintenance durvalumab with or without olaparib as first-line treatment for advanced endometrial cancer: the phase iii duo-e trial. Journal of Clinical Oncology, 42:283-299, Jan 2024. URL: https://doi.org/10.1200/jco.23.02132, doi:10.1200/jco.23.02132. This article has 384 citations and is from a highest quality peer-reviewed journal.