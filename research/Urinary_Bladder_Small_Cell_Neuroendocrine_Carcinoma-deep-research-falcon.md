---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-11T11:01:05.799622'
end_time: '2026-05-11T11:09:25.434112'
duration_seconds: 499.63
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Urinary Bladder Small Cell Neuroendocrine Carcinoma
  mondo_id: ''
  category: ''
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 30
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Urinary Bladder Small Cell Neuroendocrine Carcinoma
- **MONDO ID:**  (if available)
- **Category:** 

## Research Objectives

Please provide a comprehensive research report on **Urinary Bladder Small Cell Neuroendocrine Carcinoma** covering all of the
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
- **Disease Name:** Urinary Bladder Small Cell Neuroendocrine Carcinoma
- **MONDO ID:**  (if available)
- **Category:** 

## Research Objectives

Please provide a comprehensive research report on **Urinary Bladder Small Cell Neuroendocrine Carcinoma** covering all of the
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


# Comprehensive Research Report: Urinary Bladder Small Cell Neuroendocrine Carcinoma (SCCNEC)

## Target Disease
- **Disease name:** Urinary bladder small cell neuroendocrine carcinoma
- **Common abbreviations:** SCCB, SCBC, bladder small cell carcinoma
- **Category:** High-grade neuroendocrine carcinoma (extrapulmonary small cell carcinoma)
- **MONDO / Orphanet / OMIM / MeSH / ICD-10/ICD-11 identifiers:** Not explicitly available in the retrieved primary texts for this run; therefore, specific codes cannot be asserted with evidence-grade citations here.

---

## 1. Disease Information

### 1.1 Overview (what is the disease?)
Urinary bladder small cell neuroendocrine carcinoma (often termed **small cell carcinoma of the bladder**, SCCB/SCBC) is a **rare, aggressive, poorly differentiated, high-grade neuroendocrine carcinoma** of the urinary bladder that is histomorphologically similar to small cell carcinomas arising in other organs (notably lung). (akbulut2024updatesonurinary pages 1-3, simon2025smallcellcarcinoma pages 4-5)

It comprises **<1% of bladder malignancies/cancers** in multiple authoritative sources. (akbulut2024updatesonurinary pages 1-3, gu2024pd1blockadeplus pages 1-3, simon2025smallcellcarcinoma pages 1-2)

### 1.2 Synonyms / alternative names
- Small cell carcinoma of the bladder (SCCB) (lu2024treatmentandsurvival pages 1-2, gu2024pd1blockadeplus pages 1-3)
- Small cell bladder cancer (SCBC) (oh2021smallcellcarcinoma pages 1-2, gu2024pd1blockadeplus pages 1-3)
- Small cell neuroendocrine carcinoma of the bladder / urinary bladder (NCT05312671 chunk 1, NCT06091124 chunk 1)
- High-grade neuroendocrine carcinoma (urinary tract), when grouped with LCNEC (NCT06228066 chunk 1)

### 1.3 Aggregated vs individual-patient sources
The evidence base for SCCB is **predominantly aggregated/retrospective** (population registries, retrospective cohorts, pathology reviews) because of rarity, with relatively few prospective trials. For example, SEER-based incidence analyses (dores2015apopulationbasedstudy pages 1-2) and population-based outcomes cohorts (British Columbia registry) (oh2021smallcellcarcinoma pages 1-2) contrast with smaller multi-center retrospective cohorts (n=20) (lu2024treatmentandsurvival pages 1-2) and early-phase prospective immunotherapy-combination trials (n=15) (gu2024pd1blockadeplus pages 1-3).

---

## 2. Etiology

### 2.1 Disease causal factors (mechanistic/biologic)
SCCB is frequently **mixed with urothelial carcinoma (UC)** and is widely interpreted as arising via **divergent differentiation/transdifferentiation from a urothelial precursor**, supported by overlap in genomic features with UC. (akbulut2024updatesonurinary pages 1-3, akbulut2024updatesonurinary pages 3-4)

Genetically, SCCB commonly shows **inactivation of tumor suppressors TP53 and RB1**, a recurring hallmark of small cell carcinomas. (gu2024pd1blockadeplus pages 1-3, akbulut2024updatesonurinary pages 3-4)

### 2.2 Risk factors
- **Tobacco exposure:** A 2025 review summarizes smoking as the **principal modifiable risk factor**, with **50%–79%** of SCCB patients being current/former smokers. (simon2025smallcellcarcinoma pages 1-2)
- **Sex/age:** SCCB disproportionately affects **older men**, which functions as a demographic risk correlate. (simon2025smallcellcarcinoma pages 1-2, lu2024treatmentandsurvival pages 1-2)

> Evidence note: SEER-based epidemiology also notes marked male predominance for urinary bladder extrapulmonary small cell carcinoma (male/female IRR 4.91). (dores2015apopulationbasedstudy pages 1-2)

### 2.3 Protective factors
No evidence for genetic or environmental protective factors specific to SCCB was identified in the retrieved sources.

### 2.4 Gene–environment interactions
No explicit gene–environment interaction analyses for SCCB (e.g., specific variants interacting with smoking exposure) were identified in the retrieved sources.

---

## 3. Phenotypes (clinical presentation)

### 3.1 Common presenting features
SCCB often presents similarly to urothelial carcinoma, with hematuria as the dominant symptom.
- The 2025 review reports **gross or microscopic hematuria in 68%–90%** of patients. (simon2025smallcellcarcinoma pages 4-5)
- Additional urinary symptoms include **dysuria and frequency**; UTIs and suprapubic discomfort are also noted. (simon2025smallcellcarcinoma pages 4-5)
- Many patients present with **nodal or metastatic involvement** at diagnosis in some series/reviews. (liao2024emerginginsightsin pages 1-2, simon2025smallcellcarcinoma pages 4-5)

### 3.2 Phenotype characteristics (onset, severity, progression)
- **Typical onset:** adult/older adult (median age ~73 in SEER-referenced cohorts/reviews). (simon2025smallcellcarcinoma pages 1-2, lu2024treatmentandsurvival pages 1-2)
- **Severity/progression:** clinically aggressive with early metastasis and relapse after initial chemotherapy response (modeled after SCLC behavior). (gu2024pd1blockadeplus pages 1-3, liao2024emerginginsightsin pages 1-2)

### 3.3 HPO term suggestions (non-exhaustive)
*(Ontology IDs are provided as standard mappings; the retrieved sources did not themselves provide HPO codes.)*
- Hematuria — **HP:0000790** (supported by clinical presentation evidence) (simon2025smallcellcarcinoma pages 4-5)
- Dysuria — **HP:0100584** (simon2025smallcellcarcinoma pages 4-5)
- Urinary frequency — **HP:0000010** (simon2025smallcellcarcinoma pages 4-5)
- Recurrent urinary tract infections — **HP:0002719** (simon2025smallcellcarcinoma pages 4-5)
- Bone pain (via bone metastasis) — **HP:0002653** (metastatic patterns discussed) (lu2024treatmentandsurvival pages 1-2)

### 3.4 Quality-of-life impact
Specific validated HRQoL instruments (e.g., EQ-5D/SF-36) for SCCB were not found in the retrieved sources. Given frequent hematuria, urinary symptoms, and need for multimodal therapy (cystectomy/chemoradiation), significant QoL impact is expected, but this inference is not quantified in the evidence set.

---

## 4. Genetic / Molecular Information

### 4.1 Causal genes (germline)
No germline causal genes or Mendelian inheritance patterns are established for SCCB in the retrieved evidence; SCCB is primarily characterized as a **somatic, acquired malignancy**.

### 4.2 Somatic genomic alterations (pathogenic variants in tumors)
A 2024 pathology review summarizes SCCB genomic features including:
- **Frequent inactivating TP53 and RB1 mutations** (tumor suppressor loss) (akbulut2024updatesonurinary pages 3-4)
- **TERT promoter mutations** (akbulut2024updatesonurinary pages 3-4, simon2025smallcellcarcinoma pages 15-16)
- **Absence of FGFR3 alterations** (contrasting with subsets of urothelial carcinoma) (akbulut2024updatesonurinary pages 3-4)
- **APOBEC mutational signature** (akbulut2024updatesonurinary pages 3-4)
- Alterations in epigenetic regulators **ARID1A, KDM6A, CREBBP, EP300** (akbulut2024updatesonurinary pages 3-4)
- Potentially targetable alterations: **PIK3CA hotspot mutations** and occasional **ERBB2 amplification** (akbulut2024updatesonurinary pages 3-4)

A mechanistic/biologic convergence across small cell carcinomas is also emphasized: the 2024 clinical trial report states small cell carcinomas across tissues share high rates of **TP53 and RB1 inactivation**. (gu2024pd1blockadeplus pages 1-3)

### 4.3 Epigenetic information
The 2024 pathology review reports that RB protein loss can sometimes reflect **epigenetic RB1 silencing** and highlights alterations in epigenetic regulators (ARID1A, KDM6A, CREBBP, EP300). (akbulut2024updatesonurinary pages 3-4)

### 4.4 Transcriptomic / expression programs
RNA/miRNA findings summarized in the pathology review include **loss of urothelial differentiation**, **activation of neural/neuroendocrine programs**, dysregulated EMT, and immune-suppressive/pro-metastatic expression profiles. (akbulut2024updatesonurinary pages 3-4)

### 4.5 Molecular subtypes (transcription-factor-defined)
SCCB heterogeneity has been stratified using transcription factors **ASCL1, NEUROD1, POU2F3**, with reported subgroup frequencies (ASCL1+ 34%, NEUROD1+ 23%, ASCL1+/NEUROD1+ 16%, POU2F3+ 21%, double-negative 6%). (akbulut2024updatesonurinary pages 3-4)

### 4.6 GO (biological process) and CL (cell type) term suggestions
*(Not explicitly enumerated in the retrieved sources; provided as standard structured suggestions aligned to the evidence.)*
- GO: neuroendocrine differentiation (general); cell cycle dysregulation (TP53/RB1 loss); epithelial-to-mesenchymal transition (EMT) (akbulut2024updatesonurinary pages 3-4)
- CL: epithelial cell (urothelial lineage) and neuroendocrine-like tumor cell state (akbulut2024updatesonurinary pages 3-4, akbulut2024updatesonurinary pages 1-3)

---

## 5. Environmental Information

### 5.1 Environmental/lifestyle factors
Smoking is repeatedly identified as a major modifiable risk factor for SCCB in contemporary reviews. (simon2025smallcellcarcinoma pages 1-2)

No specific occupational toxins, radiation exposures, or infectious triggers were identified in the retrieved SCCB-specific evidence.

---

## 6. Mechanism / Pathophysiology (causal chain)

### 6.1 High-level causal chain (evidence-supported)
1. **Urothelial precursor tumor** (often conventional urothelial carcinoma component) (akbulut2024updatesonurinary pages 1-3)
2. Acquisition/selection of a **small-cell neuroendocrine differentiation program** with characteristic morphology and neuroendocrine marker expression (CD56/synaptophysin/chromogranin/INSM1) (akbulut2024updatesonurinary pages 1-3)
3. Underlying genomic drivers frequently include **TP53/RB1 inactivation** (cell-cycle checkpoint loss) and **TERT promoter mutation** (replicative immortality), plus epigenetic regulator alterations and APOBEC mutagenesis (akbulut2024updatesonurinary pages 3-4, gu2024pd1blockadeplus pages 1-3)
4. Clinical consequence: **rapid progression, early metastasis, transient chemosensitivity with relapse**, and poor survival in advanced/extensive disease (gu2024pd1blockadeplus pages 1-3, liao2024emerginginsightsin pages 1-2)

---

## 7. Anatomical Structures Affected

### 7.1 Organ/tissue level
- Primary site: **urinary bladder** (urothelial mucosa and bladder wall). (akbulut2024updatesonurinary pages 1-3)
- Common metastatic sites noted in SCCB literature synthesized in the 2024 cohort paper include **pelvic/retroperitoneal lymph nodes, liver, and bone**. (lu2024treatmentandsurvival pages 1-2)

### 7.2 UBERON term suggestions
- Urinary bladder — **UBERON:0001255**
- Pelvic lymph node (regional nodes) — mapped generally to lymph node structures
- Liver — **UBERON:0002107**
- Bone tissue — **UBERON:0001474**

---

## 8. Temporal Development (natural history)

### 8.1 Onset pattern
Typically presents in older adults (median age ~73 in SEER-referenced cohorts). (simon2025smallcellcarcinoma pages 1-2, lu2024treatmentandsurvival pages 1-2)

### 8.2 Progression and staging concepts
SCCB is clinically staged using standard bladder cancer staging systems (AJCC TNM), and many expert sources also use a **two-tier limited vs extensive** framework analogous to small cell lung cancer for treatment planning. (lu2024treatmentandsurvival pages 1-2)

The disease often demonstrates initial chemotherapy responses but frequent relapse/progression, motivating multimodal therapy in non-metastatic disease. (gu2024pd1blockadeplus pages 1-3, oh2021smallcellcarcinoma pages 1-2)

---

## 9. Inheritance and Population

### 9.1 Epidemiology and incidence
- **Rarity:** SCCB is repeatedly described as <1% of bladder cancers. (akbulut2024updatesonurinary pages 1-3, gu2024pd1blockadeplus pages 1-3, simon2025smallcellcarcinoma pages 1-2)
- **SEER extrapulmonary small cell carcinoma incidence:** urinary bladder is among the highest-incidence EPSCC sites, **IR 0.7–0.8 per million person-years** in SEER 1992–2010. (dores2015apopulationbasedstudy pages 1-2)
- **Incidence trend:** SEER-based analysis found the incidence of **small cell carcinoma of the urinary bladder increased** during 1992–2010 with **APC 6.75**. (dores2015apopulationbasedstudy pages 1-2)
- **Demographics:** male predominance is strong (male/female IRR 4.91 in SEER EPSCC analysis; and male:female ~3:1 in SEER-referenced SCCB cohort summaries). (dores2015apopulationbasedstudy pages 1-2, lu2024treatmentandsurvival pages 1-2)

### 9.2 Inheritance
SCCB is not described as an inherited disorder in the retrieved evidence; the molecular data emphasize **somatic** alterations (TP53, RB1, TERT promoter, etc.). (akbulut2024updatesonurinary pages 3-4, gu2024pd1blockadeplus pages 1-3)

---

## 10. Diagnostics

### 10.1 Biopsy and histopathology
Diagnosis is based on **histology** showing classic small cell morphology and supported by neuroendocrine-marker immunohistochemistry. (akbulut2024updatesonurinary pages 1-3)

### 10.2 Immunohistochemistry (IHC)
Typical neuroendocrine markers include **CD56, synaptophysin, chromogranin, and INSM1**. (akbulut2024updatesonurinary pages 1-3)

RB loss by IHC and abnormal p53 staining patterns consistent with TP53 alteration are frequent supportive findings. (akbulut2024updatesonurinary pages 1-3)

### 10.3 Imaging
Staging commonly uses **contrast-enhanced CT and/or MRI**. A consensus approach described in the 2024 cohort paper includes gadolinium-enhanced MRI or contrast-enhanced CT as part of staging and a limited vs extensive system analogous to SCLC. (lu2024treatmentandsurvival pages 1-2)

---

## 11. Outcome / Prognosis

### 11.1 Survival statistics (population-based and cohort)
- In a British Columbia population-based analysis of localized SCBC (1985–2018; n=77), **5-year OS was 29% (radical cystectomy) vs 39% (radiation)** (p=0.51). (oh2021smallcellcarcinoma pages 1-2)
- In the same study, among guideline-concordant patients, **5-year OS was 56% (RC) vs 58% (chemoRT)** (p=0.90), and 5-year CSS was 56% vs 71% (p=0.71). (oh2021smallcellcarcinoma pages 1-2)
- In a 2024 multi-center Chinese non-metastatic SCCB cohort (n=20), reported outcomes were more favorable for radical local treatment: local treatment median OS **65.3 months** vs radical treatment median OS not reached; 3-year OS 54% vs 75%. (lu2024treatmentandsurvival pages 1-2)
- In extensive disease, the 2024 phase 1b trial background summarizes historical outcomes: **median OS 7–13 months** despite initial 40%–60% responses to etoposide/platinum. (gu2024pd1blockadeplus pages 1-3)

### 11.2 Prognostic factors
- In localized SCBC, lack of neoadjuvant chemotherapy was associated with worse OS in multivariable modeling in the population cohort. (oh2021smallcellcarcinoma pages 1-2)
- Molecular subgrouping (e.g., POU2F3/PLCG2 expression) has been associated with poorer PFS/OS in summarized molecular studies. (akbulut2024updatesonurinary pages 3-4)

---

## 12. Treatment

### 12.1 Standard systemic therapy (real-world implementation)
Because of rarity, SCCB regimens are commonly **extrapolated from small cell lung cancer**, centered on **platinum (cisplatin/carboplatin) + etoposide**, used either as definitive systemic therapy in extensive disease or perioperatively/with chemoradiation in limited disease. (lu2024treatmentandsurvival pages 1-2, gu2024pd1blockadeplus pages 1-3, liao2024emerginginsightsin pages 1-2)

### 12.2 Multimodal local therapy (localized disease)
Authoritative population-based evidence indicates **radical cystectomy and bladder-conserving chemoradiotherapy can yield comparable long-term outcomes** in localized disease when delivered in guideline-consistent multimodal frameworks. (oh2021smallcellcarcinoma pages 1-2)

### 12.3 Immunotherapy and emerging combinations (recent developments, 2024)
A notable 2024 development is prospective evidence for adding PD-1 blockade to platinum chemotherapy:
- **Direct abstract quote:** “We report a phase 1b study of pembrolizumab in combination with platinum-based chemotherapy in 15 patients with stage III-IV small cell bladder (cohort 1) or small cell/neuroendocrine prostate cancers (cohort 2). Overall response rate (ORR) is 43% with two-year overall survival (OS) rate of 86% (95% confidence interval [CI]: 0.63, 1.00) for cohort 1 and 57% (95% CI: 0.30, 1.00) for cohort 2.” (gu2024pd1blockadeplus pages 1-3)
This trial also reported grade ≥3 adverse events in 40% with no treatment-related deaths and included extensive immune correlative analyses. (gu2024pd1blockadeplus pages 1-3)

### 12.4 Active clinical trials (real-world pipeline)
Evidence from ClinicalTrials.gov records in this run includes:
- **NCT05312671**: Atezolizumab + platinum/etoposide followed by cystectomy (localized small cell/neuroendocrine bladder cancer). (NCT05312671 chunk 1)
- **NCT06091124 (NEOBLAST)**: Neoadjuvant adebrelimab + etoposide/cisplatin followed by radical cystectomy. (NCT06091124 chunk 1)
- **NCT06228066 (LASER)**: Lurbinectedin ± avelumab in metastatic SCCB/high-grade neuroendocrine urinary tract tumors after platinum/etoposide. (NCT06228066 chunk 1)
- **NCT06161532 (SMART)**: Sacituzumab govitecan ± atezolizumab in rare metastatic GU tumors including high-grade neuroendocrine carcinomas. (NCT06161532 chunk 1)
- **NCT00756639**: Prophylactic cranial irradiation (PCI) in small cell carcinoma of the urothelium. (NCT00756639 chunk 1)

### 12.5 MAXO term suggestions (non-exhaustive)
- Platinum-based chemotherapy (cisplatin/carboplatin + etoposide)
- Radical cystectomy
- Radiotherapy / chemoradiotherapy
- Immune checkpoint inhibitor therapy (PD-1/PD-L1 blockade)

---

## 13. Prevention

### 13.1 Primary prevention
Given smoking is a major modifiable risk factor, tobacco cessation is the most evidence-supported preventive strategy referenced in SCCB-focused reviews. (simon2025smallcellcarcinoma pages 1-2)

No SCCB-specific screening or chemoprevention strategies were identified in the retrieved sources.

---

## 14. Other Species / Natural Disease
No naturally occurring SCCB analogs in non-human species were identified in the retrieved evidence.

---

## 15. Model Organisms
No SCCB-specific animal models or dedicated model organism resources were identified in the retrieved evidence set for this run.

---

## Recent (2023–2024) and Foundational Evidence Summary Tables
The following evidence-map tables consolidate the most relevant studies and actionable diagnostic/treatment details available in this run.

| Citation (first author, year) | Publication date/month | Study type/data source | Population (n; stage) | Key findings (include incidence/survival/genomics) | URL/DOI | PMID |
|---|---|---|---|---|---|---|
| Dores, 2015 | Mar 2015 | Population-based SEER-13 epidemiology/survival study | Small cell carcinoma cases in SEER 1992–2010; EPSCC n=2,438 overall; urinary bladder site-specific analyses; limited vs distant stage | Urinary bladder was among the highest-incidence extrapulmonary small cell carcinoma sites (IR 0.7–0.8 per million person-years); bladder had strong male predominance (male/female IRR 4.91); incidence of urinary bladder small cell carcinoma increased with APC 6.75 during 1992–2010; distant-to-limited stage IRR for bladder was decreased (0.32–0.46); for nearly all sites with distant stage disease, 3-year relative survival was <10% (dores2015apopulationbasedstudy pages 1-2) | https://doi.org/10.1186/s12885-015-1188-y |  |
| Oh, 2021 | Sep 2021 online; Can Urol Assoc J 2022 | Population-based cohort from British Columbia | Localized SCBC treated with curative intent, n=77; RC n=33, RT n=44; analysis 2 compared RC vs chemoRT per consensus-guideline treatment | Five-year OS was 29% (RC) vs 39% (RT), p=0.51; five-year CSS 35% (RC) vs 52% (RT), p=0.29. In guideline-concordant analysis, 5-year OS was 56% (RC) vs 58% (chemoRT), p=0.90; 5-year CSS 56% vs 71%, p=0.71. Lack of neoadjuvant chemotherapy was associated with worse OS; authors conclude RC and chemoRT offer similar outcomes and NAC should be considered (oh2021smallcellcarcinoma pages 1-2) | https://doi.org/10.5489/cuaj.7411 |  |
| Akbulut, 2024 | Mar 2024 | Narrative pathology/genomics review | Urinary bladder neuroendocrine tumors; summarizes bladder SMC/LCNEC literature and molecular subgroup data | Reviews that bladder SMC/LCNEC comprise <1% of bladder malignancies; most SMCs are pure or mixed with urothelial carcinoma. Histology: small cells with nuclear molding, high mitoses, necrosis/crush artifact. IHC: CD56, synaptophysin, chromogranin, INSM1; frequent RB loss and mutant-pattern p53. Molecularly, bladder SMC shows higher TMB than conventional urothelial carcinoma, frequent TP53/RB1 inactivation, TERT promoter mutations, APOBEC signature, no FGFR3 alterations, and alterations in ARID1A, KDM6A, CREBBP, EP300; potential targetable events include PIK3CA hotspots and occasional ERBB2 amplifications. Molecular subgroups reported using ASCL1/NEUROD1/POU2F3, with POU2F3 and PLCG2 associated with poorer PFS/OS (akbulut2024updatesonurinary pages 1-3, akbulut2024updatesonurinary pages 3-4) | https://doi.org/10.1097/pap.0000000000000433 |  |
| Liao, 2024 | Jan 2024 | ASCO Educational Book review/expert synthesis | GU small-cell carcinomas; bladder-focused review drawing on retrospective series and guidelines | States bladder SCC accounts for ~0.48%–2% of bladder cancers; usually presents with gross hematuria and in the majority with nodal/metastatic involvement (~70%). Pathology/IHC parallels SCLC with epithelial and neuroendocrine markers (chromogranin, synaptophysin, INSM1, CD56). Management is multimodal and extrapolated from SCLC, using platinum-based chemotherapy with surgery and/or radiation; untreated 5-year OS is reported as <10%, and advanced disease remains highly lethal (liao2024emerginginsightsin pages 1-2) | https://doi.org/10.1200/edbk_430336 |  |
| Gu, 2024 | Nov 2024 | Phase 1b clinical trial with correlative biomarker analyses | 15 patients with stage III–IV small cell bladder (cohort 1) or small cell/neuroendocrine prostate cancer (cohort 2) receiving pembrolizumab + platinum chemotherapy | In this mixed bladder/prostate neuroendocrine trial, ORR was 43%; 2-year OS was 86% in cohort 1 and 57% in cohort 2; grade ≥3 adverse events occurred in 40% with no treatment-related deaths. Introductory data summarize SCBC as <1% of bladder cancers, often mixed with urothelial carcinoma (up to 70%), with initial 40%–60% response to etoposide/platinum but median OS 7–13 months in extensive disease. Genomically, SCCs share high rates of TP53 and RB1 inactivation; correlative analyses included PD-L1, TMB, MSI, and targeted 648-gene somatic testing (gu2024pd1blockadeplus pages 1-3, gu2024pd1blockadeplus pages 6-9) | https://doi.org/10.1016/j.xcrm.2024.101824 |  |
| Lu, 2024 | Oct 2024 | Multi-institution retrospective cohort from China | Non-metastatic SCCB, n=20; localized T1–2N0 n=10, locally advanced ≥T3 or N+ n=10 | SCCB accounts for 0.5%–1.0% of bladder cancers; cites SEER trend from 0.3% to 0.6%, male:female 3:1, median age 73. In the cohort, 90% received chemotherapy (neoadjuvant n=5, adjuvant n=13). Median OS was 65.3 months for local treatment and not reached for radical treatment; 3-year OS 54% vs 75%, respectively. Median PFS was 13.8 months for local treatment and not reached for radical treatment. Review within paper notes historical large series with median OS 11–20.7 months and 3-year OS 33%–37% for all stages; common metastases are pelvic/retroperitoneal nodes, liver, and bone; guidelines recommend platinum/etoposide-based multimodality therapy (lu2024treatmentandsurvival pages 1-2, lu2024treatmentandsurvival pages 7-7) | https://doi.org/10.1038/s41598-024-75512-z |  |
| Simon, 2025 | Jun 2025 | Comprehensive review of pathogenesis, presentation, and management | Review of SCCB literature; includes institutional/series summaries rather than a single cohort | Defines SCCB as a rare aggressive neuroendocrine malignancy accounting for <1% of bladder cancers; incidence rose from 0.05 to 0.14 per 100,000 between the 1990s and 2000s. Predominantly affects older men (77.8% male; median age 73). Smoking is the principal modifiable risk factor (50%–79% current/former smokers). Common presentation includes gross/microscopic hematuria (68%–90%), dysuria, frequency, suprapubic discomfort; paraneoplastic syndromes are rare. Pure SCCB represents about one-third of cases; most are mixed with urothelial carcinoma. Shared clonal origin with UC is supported by concordant TP53 mutations; review also notes frequent TP53/RB mutations, high TMB, and frequent TERT promoter mutation in SCCB (simon2025smallcellcarcinoma pages 1-2, simon2025smallcellcarcinoma pages 4-5, simon2025smallcellcarcinoma pages 15-16) | https://doi.org/10.1177/23523735251370956 |  |


*Table: This table compiles major recent and foundational studies/resources on urinary bladder small cell neuroendocrine carcinoma, emphasizing epidemiology, pathology/genomics, treatment, and survival. It is useful as a quick evidence map for building a disease knowledge base entry and identifying where recent advances complement older population-based outcome data.*

| Domain | Item (test/marker/therapy) | Details | Evidence type | Key quantitative data | Source (first author/year or NCT) | URL/DOI |
|---|---|---|---|---|---|---|
| Diagnostic | Histopathology | Small-cell morphology: cells smaller than ~3 lymphocytes, high nuclear-to-cytoplasmic ratio, scant cytoplasm, inconspicuous nucleoli, vesicular chromatin, nuclear molding, frequent mitoses, geographic/single-cell necrosis, crush artifact; growth in solid sheets, trabeculae, acinar patterns (akbulut2024updatesonurinary pages 1-3) | Review | No single performance metric reported | Akbulut 2024 | https://doi.org/10.1097/pap.0000000000000433 |
| Diagnostic | Immunohistochemistry panel | Typical neuroendocrine markers: CD56, synaptophysin, chromogranin, INSM1; keratin often limited/dot-like perinuclear in SMC; frequent RB loss by IHC and abnormal p53 staining supporting TP53 alteration (akbulut2024updatesonurinary pages 1-3) | Review | No sensitivity/specificity stated; Ki-67 described as high in SMC/LCNEC (akbulut2024updatesonurinary pages 1-3) | Akbulut 2024 | https://doi.org/10.1097/pap.0000000000000433 |
| Diagnostic | Expanded marker panel | SCCB can express synaptophysin, chromogranin, INSM1, neuron-specific enolase, CD56, pancytokeratin, CK8, CK19; up to 40% may stain TTF-1; electron microscopy may show dense-core neurosecretory granules and desmosomes (simon2025smallcellcarcinoma pages 4-5, gu2024pd1blockadeplus pages 1-3) | Review + trial background | TTF-1 positivity up to 40% (simon2025smallcellcarcinoma pages 4-5) | Simon 2025; Gu 2024 | https://doi.org/10.1177/23523735251370956 ; https://doi.org/10.1016/j.xcrm.2024.101824 |
| Diagnostic | Molecular/IHC subtype markers | Novel transcription-factor markers NEUROD1, ASCL1, POU2F3 identify subgroups; reported groups: ASCL1+ 34%, NEUROD1+ 23%, ASCL1+/NEUROD1+ 16%, POU2F3+ 21%, double-negative 6%; POU2F3 and PLCG2 associated with worse PFS/OS (akbulut2024updatesonurinary pages 3-4, akbulut2024updatesonurinary pages 1-3) | Review | Subtype proportions: 34%, 23%, 16%, 21%, 6%; PLCG2 expressed in 32% (akbulut2024updatesonurinary pages 3-4) | Akbulut 2024 | https://doi.org/10.1097/pap.0000000000000433 |
| Diagnostic | Imaging for staging | Recommended staging includes gadolinium-enhanced MRI or contrast-enhanced CT; CT urography commonly used; whole-body FDG PET/CT mentioned for metastatic detection (lu2024treatmentandsurvival pages 1-2, simon2025smallcellcarcinoma pages 15-16) | Cohort/review | CT urography accuracy cited in review: 40%–92% for perivesical invasion and 40%–85% for nodal metastasis (simon2025smallcellcarcinoma pages 4-5) | Lu 2024; Simon 2025 | https://doi.org/10.1038/s41598-024-75512-z ; https://doi.org/10.1177/23523735251370956 |
| Diagnostic | Genomic profiling | Frequent inactivating TP53 and RB1 mutations, TERT promoter mutations, higher tumor mutation burden than conventional urothelial carcinoma, APOBEC signature; additional alterations in ARID1A, KDM6A, CREBBP, EP300; occasional PIK3CA hotspot mutations and ERBB2 amplification (akbulut2024updatesonurinary pages 3-4, simon2025smallcellcarcinoma pages 15-16) | Review | No test performance metric reported | Akbulut 2024; Simon 2025 | https://doi.org/10.1097/pap.0000000000000433 ; https://doi.org/10.1177/23523735251370956 |
| Treatment | Platinum-etoposide systemic therapy | Standard frontline approach extrapolated from SCLC: cisplatin or carboplatin plus etoposide for extensive disease; also used neoadjuvantly/adjuvantly in limited disease (lu2024treatmentandsurvival pages 1-2, liao2024emerginginsightsin pages 1-2, gu2024pd1blockadeplus pages 1-3) | Guideline-informed review + cohort + trial background | Initial response rate 40%–60% in SCBC; median OS 7–13 months in extensive disease (gu2024pd1blockadeplus pages 1-3) | Liao 2024; Lu 2024; Gu 2024 | https://doi.org/10.1200/edbk_430336 ; https://doi.org/10.1038/s41598-024-75512-z ; https://doi.org/10.1016/j.xcrm.2024.101824 |
| Treatment | Multimodal local therapy | For limited/localized disease, reviews/guidelines support concurrent chemoradiotherapy or neoadjuvant chemotherapy followed by local treatment (radical cystectomy or radiotherapy) (lu2024treatmentandsurvival pages 1-2, oh2021smallcellcarcinoma pages 1-2) | Cohort + guideline-informed review | In BC population study, lack of neoadjuvant chemotherapy associated with worse OS; 5-year OS 56% RC vs 58% chemoRT in guideline-concordant patients (oh2021smallcellcarcinoma pages 1-2) | Lu 2024; Oh 2021 | https://doi.org/10.1038/s41598-024-75512-z ; https://doi.org/10.5489/cuaj.7411 |
| Treatment | Radical cystectomy (RC) | Used after neoadjuvant chemotherapy or as radical local treatment in selected non-metastatic patients (lu2024treatmentandsurvival pages 1-2, oh2021smallcellcarcinoma pages 1-2) | Cohort | Five-year OS 29% and CSS 35% in all curative-intent RC patients; in guideline-concordant subgroup, 5-year OS 56% and CSS 56% (oh2021smallcellcarcinoma pages 1-2) | Oh 2021 | https://doi.org/10.5489/cuaj.7411 |
| Treatment | Definitive chemoradiotherapy / radiotherapy | Curative-intent RT used with platinum-based chemotherapy for localized disease; consensus-guideline analysis used ~60 Gy EQD2; hypofractionated 45 Gy/15 fractions over 3 weeks and conventional 60–66 Gy regimens referenced; RT dose ≥54 Gy associated with improved OS in cited series (oh2021smallcellcarcinoma pages 1-2, lu2024treatmentandsurvival pages 7-7) | Population cohort + retrospective synthesis | Five-year OS 39% and CSS 52% for all RT patients; in guideline-concordant chemoRT subgroup, 5-year OS 58% and CSS 71% (oh2021smallcellcarcinoma pages 1-2); no OS difference between RC and RT in organ-confined disease in pooled data (26.7 vs 30.0 months) (lu2024treatmentandsurvival pages 7-7) | Oh 2021; Lu 2024 | https://doi.org/10.5489/cuaj.7411 ; https://doi.org/10.1038/s41598-024-75512-z |
| Treatment | Chinese multi-center real-world treatment | In non-metastatic SCCB, 90% received chemotherapy; 13 had local treatment (PC/TURBT), 7 radical treatment (RC/RT) (lu2024treatmentandsurvival pages 1-2) | Cohort | Local-treatment median OS 65.3 months; radical-treatment median OS not reached; 3-year OS 54% vs 75%; local-treatment median PFS 13.8 months; radical-treatment median PFS not reached (lu2024treatmentandsurvival pages 1-2) | Lu 2024 | https://doi.org/10.1038/s41598-024-75512-z |
| Treatment | Pembrolizumab + platinum-based chemotherapy | Phase 1b regimen for stage III-IV small cell bladder/prostate neuroendocrine cancers (trial registered NCT03582475); explored immunologic correlates with serial single-cell PBMC analyses (gu2024pd1blockadeplus pages 1-3, gu2024pd1blockadeplus pages 6-9) | Prospective phase 1b trial | ORR 43%; 2-year OS 86% in bladder cohort and 57% in prostate cohort; grade ≥3 adverse events 40%; no treatment-related deaths or cessation due to toxicity (gu2024pd1blockadeplus pages 1-3) | Gu 2024 | https://doi.org/10.1016/j.xcrm.2024.101824 |
| Treatment | Atezolizumab + platinum + etoposide followed by cystectomy | Ongoing phase II trial in localized small cell/neuroendocrine bladder cancer; atezolizumab 1200 mg day 1 + etoposide 100 mg/m2 days 1–3 + cisplatin 70 mg/m2 day 1 or carboplatin AUC 5 day 1, every 21 days ×4; then cystectomy and atezolizumab maintenance up to 1 year (NCT05312671 chunk 1) | ClinicalTrials.gov | Enrollment 63 planned; primary endpoint pathologic complete response at cystectomy (NCT05312671 chunk 1) | NCT05312671 | https://clinicaltrials.gov/study/NCT05312671 |
| Treatment | Neoadjuvant adebrelimab + etoposide + cisplatin followed by radical cystectomy | Ongoing phase II single-arm study for neuroendocrine bladder carcinoma; adebrelimab 1200 mg day 1 + etoposide 0.1 g days 1–3 + cisplatin 35 mg/m2 days 1–2 every 21 days for up to 4 cycles, then RC (NCT06091124 chunk 1) | ClinicalTrials.gov | Enrollment 22 planned; primary endpoints: ypCR and safety/tolerability (NCT06091124 chunk 1) | NCT06091124 | https://clinicaltrials.gov/study/NCT06091124 |
| Treatment | Lurbinectedin ± avelumab (LASER) | Ongoing phase II study in metastatic SCCB/HGNET after prior platinum/etoposide or ineligible/refused; lurbinectedin 3.2 mg/m2 IV q21d ± avelumab 800 mg IV q21d (NCT06228066 chunk 1) | ClinicalTrials.gov | Enrollment 45 planned; primary endpoint ORR; background notes average survival about 1 year and lurbinectedin ORR 35% in second-line SCLC (NCT06228066 chunk 1) | NCT06228066 | https://clinicaltrials.gov/study/NCT06228066 |
| Treatment | Sacituzumab govitecan ± atezolizumab (SMART) | Ongoing phase II in rare metastatic GU tumors including high-grade neuroendocrine bladder/urinary tract cancers; sacituzumab govitecan 10 mg/kg IV days 1 and 8 q21d ± atezolizumab 1200 mg day 1 q21d (NCT06161532 chunk 1) | ClinicalTrials.gov | Enrollment 60 planned; primary endpoint ORR (NCT06161532 chunk 1) | NCT06161532 | https://clinicaltrials.gov/study/NCT06161532 |
| Treatment | Prophylactic cranial irradiation (PCI) | Phase II MD Anderson study of whole-brain RT after chemotherapy/surgery in locally advanced/metastatic small cell carcinoma of the urothelium; PCI 30 Gy in 2 Gy fractions over 3 weeks (NCT00756639 chunk 1) | ClinicalTrials.gov | Enrollment 31 actual; primary endpoint brain-metastasis-free survival at 1 year (NCT00756639 chunk 1) | NCT00756639 | https://clinicaltrials.gov/study/NCT00756639 |


*Table: This table summarizes evidence-supported diagnostic modalities and current treatment approaches for urinary bladder small cell neuroendocrine carcinoma, including marker panels, staging tools, standard multimodal therapy, and active clinical trials. It is useful as a compact evidence map for clinical and knowledge-base curation.*

---

## Abstract-Supported Key Statistics and Direct Quotes (selected)

1. **SEER EPSCC incidence and trends (direct abstract quote):** “Of the EPSCC sites, urinary bladder, prostate, and uterine cervix had the highest incidence (IRs = 0.7-0.8)… During 1992–2010, significant changes in IRs were observed for… small cell carcinoma of the urinary bladder (APC = 6.75).” (dores2015apopulationbasedstudy pages 1-2)

2. **Prospective immunotherapy + chemotherapy signal (direct abstract quote):** “Overall response rate (ORR) is 43% with two-year overall survival (OS) rate of 86%… for cohort 1…” (pembrolizumab + platinum; SCBC cohort). (gu2024pd1blockadeplus pages 1-3)

3. **Non-metastatic multi-center China cohort (direct abstract quote):** “A total of 20 patients were included… A total of 18 patients (90%) received chemotherapy… The median OS for the receiving local treatment was 65.3 months… The median OS for the receiving radical treatment was not reached…” (lu2024treatmentandsurvival pages 1-2)

---

## Expert synthesis / analysis (evidence-based)
Across recent authoritative pathology and oncology sources, SCCB is best conceptualized as a **urothelial-lineage malignancy that adopts a small-cell neuroendocrine state**, driven by recurrent **TP53/RB1 loss** and associated molecular programs (loss of urothelial differentiation and activation of neural/neuroendocrine transcriptional programs). (akbulut2024updatesonurinary pages 3-4, akbulut2024updatesonurinary pages 1-3, gu2024pd1blockadeplus pages 1-3)

Clinically, the strongest real-world management pattern is **multimodal therapy** (platinum-etoposide-based systemic therapy integrated with cystectomy or chemoradiation), with population-based evidence showing **comparable long-term survival** for guideline-concordant cystectomy-based vs chemoRT-based strategies in localized disease. (oh2021smallcellcarcinoma pages 1-2)

The most notable 2024 therapeutic development in the retrieved evidence is early-phase prospective support for **checkpoint blockade combined with platinum chemotherapy**, which—if validated—could shift frontline systemic therapy for advanced SCCB toward immunochemotherapy paradigms similar to small cell lung cancer. (gu2024pd1blockadeplus pages 1-3)


References

1. (akbulut2024updatesonurinary pages 1-3): Dilara Akbulut and Hikmat Al-Ahmadie. Updates on urinary bladder tumors with neuroendocrine features. Advances In Anatomic Pathology, 31:169-177, Mar 2024. URL: https://doi.org/10.1097/pap.0000000000000433, doi:10.1097/pap.0000000000000433. This article has 12 citations and is from a domain leading peer-reviewed journal.

2. (simon2025smallcellcarcinoma pages 4-5): Nicholas I Simon, Andre R Kydd, Dilara Akbulut, David Takeda, Jaydira Del Rivero, Maria Merino, Bernadette Redd, Liza Lindenberg, Esther Mena, Elias Chandran, Sandeep Gurram, Salah Boudjadi, Scot Niglio, Parth Sharma, Anish Thomas, and Andrea B Apolo. Small cell carcinoma of the bladder: review of pathogenesis, presentation, and management. Bladder Cancer, Jun 2025. URL: https://doi.org/10.1177/23523735251370956, doi:10.1177/23523735251370956. This article has 1 citations.

3. (gu2024pd1blockadeplus pages 1-3): Yiqian Gu, Ann Ly, Sara Rodriguez, Hanwei Zhang, Jiyoon Kim, Zhiyuan Mao, Ankush Sachdeva, Nazy Zomorodian, Matteo Pellegrini, Gang Li, Sandy Liu, Alexandra Drakaki, Matthew B. Rettig, and Arnold I. Chin. Pd-1 blockade plus cisplatin-based chemotherapy in patients with small cell/neuroendocrine bladder and prostate cancers. Cell Reports Medicine, 5:101824, Nov 2024. URL: https://doi.org/10.1016/j.xcrm.2024.101824, doi:10.1016/j.xcrm.2024.101824. This article has 16 citations and is from a peer-reviewed journal.

4. (simon2025smallcellcarcinoma pages 1-2): Nicholas I Simon, Andre R Kydd, Dilara Akbulut, David Takeda, Jaydira Del Rivero, Maria Merino, Bernadette Redd, Liza Lindenberg, Esther Mena, Elias Chandran, Sandeep Gurram, Salah Boudjadi, Scot Niglio, Parth Sharma, Anish Thomas, and Andrea B Apolo. Small cell carcinoma of the bladder: review of pathogenesis, presentation, and management. Bladder Cancer, Jun 2025. URL: https://doi.org/10.1177/23523735251370956, doi:10.1177/23523735251370956. This article has 1 citations.

5. (lu2024treatmentandsurvival pages 1-2): Jiawei Lu, Jiaomei Zhou, Yueping Liu, Yexiong Li, Yuan Tang, Ning Li, Shulian Wang, Yongwen Song, Wenjue Zhang, Xiaoyong Xiang, and Jing Jin. Treatment and survival of non-metastatic small cell carcinoma of the bladder from multiple centers in china. Scientific Reports, Oct 2024. URL: https://doi.org/10.1038/s41598-024-75512-z, doi:10.1038/s41598-024-75512-z. This article has 3 citations and is from a peer-reviewed journal.

6. (oh2021smallcellcarcinoma pages 1-2): Justin Oh, Bernhard Eigl, Peter C. Black, Tom Pickles, Carlos Villamil, Katherine Sunderland, and Scott Tyldesley. Small cell carcinoma of the bladder: a population-based analysis of long-term outcomes after radical cystectomy and bladder conservation with chemoradiotherapy. Canadian Urological Association Journal, Jul 2021. URL: https://doi.org/10.5489/cuaj.7411, doi:10.5489/cuaj.7411. This article has 0 citations.

7. (NCT05312671 chunk 1):  Atezolizumab Plus Etoposide and Platinum in Small Cell Bladder Cancer. Sidney Kimmel Comprehensive Cancer Center at Johns Hopkins. 2022. ClinicalTrials.gov Identifier: NCT05312671

8. (NCT06091124 chunk 1):  Neoadjuvant Adebrelimab Plus Etoposide and Cisplatin in Neuroendocrine Bladder Carcinoma. RenJi Hospital. 2023. ClinicalTrials.gov Identifier: NCT06091124

9. (NCT06228066 chunk 1):  Lurbinectedin With or Without Avelumab in Small Cell Carcinoma of the Bladder (LASER). National Cancer Institute (NCI). 2024. ClinicalTrials.gov Identifier: NCT06228066

10. (dores2015apopulationbasedstudy pages 1-2): Graça M Dores, Osama Qubaiah, Ankur Mody, Bassam Ghabach, and Susan S Devesa. A population-based study of incidence and patient survival of small cell carcinoma in the united states, 1992–2010. BMC Cancer, Mar 2015. URL: https://doi.org/10.1186/s12885-015-1188-y, doi:10.1186/s12885-015-1188-y. This article has 54 citations and is from a peer-reviewed journal.

11. (akbulut2024updatesonurinary pages 3-4): Dilara Akbulut and Hikmat Al-Ahmadie. Updates on urinary bladder tumors with neuroendocrine features. Advances In Anatomic Pathology, 31:169-177, Mar 2024. URL: https://doi.org/10.1097/pap.0000000000000433, doi:10.1097/pap.0000000000000433. This article has 12 citations and is from a domain leading peer-reviewed journal.

12. (liao2024emerginginsightsin pages 1-2): Ross S. Liao, Hui Ting Ruan, Albert Jang, Melissa Huynh, Rosa Nadal Rios, Jean H. Hoffman-Censits, Shuanzeng Wei, Omar Y. Mian, and Pedro C. Barata. Emerging insights in small-cell carcinoma of the genitourinary tract: from diagnosis to novel therapeutic horizons. American Society of Clinical Oncology educational book. American Society of Clinical Oncology. Annual Meeting, 44:e430336, Jan 2024. URL: https://doi.org/10.1200/edbk\_430336, doi:10.1200/edbk\_430336. This article has 12 citations.

13. (simon2025smallcellcarcinoma pages 15-16): Nicholas I Simon, Andre R Kydd, Dilara Akbulut, David Takeda, Jaydira Del Rivero, Maria Merino, Bernadette Redd, Liza Lindenberg, Esther Mena, Elias Chandran, Sandeep Gurram, Salah Boudjadi, Scot Niglio, Parth Sharma, Anish Thomas, and Andrea B Apolo. Small cell carcinoma of the bladder: review of pathogenesis, presentation, and management. Bladder Cancer, Jun 2025. URL: https://doi.org/10.1177/23523735251370956, doi:10.1177/23523735251370956. This article has 1 citations.

14. (NCT06161532 chunk 1):  Sacituzumab Govitecan With or Without Atezolizumab Immunotherapy in Rare Genitourinary Tumors (SMART) Such as High Grade Neuroendocrine Carcinomas, Adenocarcinoma, and Squamous Cell Bladder/Urinary Tract Cancer, Renal Medullary Carcinoma and Penile C.... National Cancer Institute (NCI). 2024. ClinicalTrials.gov Identifier: NCT06161532

15. (NCT00756639 chunk 1):  Prophylactic Cranial Irradiation (PCI) for Small Cell Carcinoma of the Urothelium. M.D. Anderson Cancer Center. 2008. ClinicalTrials.gov Identifier: NCT00756639

16. (gu2024pd1blockadeplus pages 6-9): Yiqian Gu, Ann Ly, Sara Rodriguez, Hanwei Zhang, Jiyoon Kim, Zhiyuan Mao, Ankush Sachdeva, Nazy Zomorodian, Matteo Pellegrini, Gang Li, Sandy Liu, Alexandra Drakaki, Matthew B. Rettig, and Arnold I. Chin. Pd-1 blockade plus cisplatin-based chemotherapy in patients with small cell/neuroendocrine bladder and prostate cancers. Cell Reports Medicine, 5:101824, Nov 2024. URL: https://doi.org/10.1016/j.xcrm.2024.101824, doi:10.1016/j.xcrm.2024.101824. This article has 16 citations and is from a peer-reviewed journal.

17. (lu2024treatmentandsurvival pages 7-7): Jiawei Lu, Jiaomei Zhou, Yueping Liu, Yexiong Li, Yuan Tang, Ning Li, Shulian Wang, Yongwen Song, Wenjue Zhang, Xiaoyong Xiang, and Jing Jin. Treatment and survival of non-metastatic small cell carcinoma of the bladder from multiple centers in china. Scientific Reports, Oct 2024. URL: https://doi.org/10.1038/s41598-024-75512-z, doi:10.1038/s41598-024-75512-z. This article has 3 citations and is from a peer-reviewed journal.