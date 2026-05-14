---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-10T00:57:11.615681'
end_time: '2026-05-10T01:24:07.978161'
duration_seconds: 1616.36
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Metastatic Non-Small Cell Lung Cancer
  mondo_id: ''
  category: ''
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 75
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Metastatic Non-Small Cell Lung Cancer
- **MONDO ID:**  (if available)
- **Category:**

## Research Objectives

Please provide a comprehensive research report on **Metastatic Non-Small Cell Lung Cancer** covering all of the
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
- **Disease Name:** Metastatic Non-Small Cell Lung Cancer
- **MONDO ID:**  (if available)
- **Category:**

## Research Objectives

Please provide a comprehensive research report on **Metastatic Non-Small Cell Lung Cancer** covering all of the
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


# Comprehensive Research Report: Metastatic Non-Small Cell Lung Cancer (mNSCLC)

## Target Disease
- **Disease name:** Metastatic non-small cell lung cancer (mNSCLC)
- **MONDO ID:** Not found in retrieved evidence for the metastatic-stage entity (see “Identifiers” below). Related entities retrieved include *non-small cell squamous lung carcinoma* **MONDO_0056806** via Open Targets; NSCLC itself appeared as EFO_0003060 in Open Targets (EFO is not MONDO). (OpenTargets Search: Non-small cell lung carcinoma,Lung adenocarcinoma,Lung squamous cell carcinoma, apter2024realworldtreatmentpatterns pages 1-2)
- **Category:** Metastatic (stage IV) thoracic malignancy; solid tumor.

---

## 1. Disease Information

### Overview / definition
mNSCLC refers to non-small cell lung cancers that have spread beyond the lung/hemithorax to distant organs (clinically aligned with **stage IV/M1** disease in many registries and studies). Contemporary studies use “metastatic NSCLC,” “advanced NSCLC,” and “stage IV NSCLC” as overlapping operational terms depending on inclusion criteria and data source. (apter2024realworldtreatmentpatterns pages 1-2, uprety2024racialandsocioeconomic pages 3-4, yang2024disparitiesinutilization pages 1-2)

### Key identifiers (as available in retrieved sources)
- **Open Targets / EFO:** non-small cell lung carcinoma **EFO_0003060**. (OpenTargets Search: Non-small cell lung carcinoma,Lung adenocarcinoma,Lung squamous cell carcinoma)
- **MONDO:** non-small cell squamous lung carcinoma **MONDO_0056806** (related histology entity). (OpenTargets Search: Non-small cell lung carcinoma,Lung adenocarcinoma,Lung squamous cell carcinoma)
- **MeSH / ICD-10 / ICD-11 / OMIM / Orphanet:** Not found in the retrieved evidence for mNSCLC or stage IV NSCLC; these would typically be obtained from ontology resources (e.g., MeSH browser, ICD-10/11, MONDO) outside the currently retrieved corpus.

### Common synonyms
- Metastatic NSCLC, advanced NSCLC (when metastatic), stage IV NSCLC, M1 NSCLC. (apter2024realworldtreatmentpatterns pages 1-2, uprety2024racialandsocioeconomic pages 3-4, yang2024disparitiesinutilization pages 1-2)

### Evidence source types
- **Aggregated disease-level resources:** SEER/SEER-Medicare population datasets and national registries (Norway). (hektoen2024realworldevidencefor pages 1-2, uprety2024racialandsocioeconomic pages 3-4)
- **Real-world evidence (RWE):** health system cohorts and EMR datasets. (apter2024realworldtreatmentpatterns pages 1-2, hektoen2024realworldevidencefor pages 5-6)
- **Clinical trials:** phase 3 biomarker-selected trials (e.g., EGFR-mutant MARIPOSA). (cho2024amivantamabpluslazertinib pages 8-9)

---

## 2. Etiology

### Primary causal factors (multifactorial)
NSCLC (and thus mNSCLC) arises through a combination of carcinogen exposures and acquired somatic genomic alterations (driver mutations/fusions), with strong contributions from tobacco smoke and additional environmental/occupational carcinogens.

#### Tobacco smoking
Tobacco is the dominant risk factor in Western settings; a 2024 review of geographic differences states tobacco accounts for “**up to 80–90% of cases**” in Western societies. (laguna2024geographicdifferencesin pages 1-3)

#### Ambient air pollution (particulate matter)
Air pollution is classified as carcinogenic to humans, and long-term PM2.5 exposure shows dose–response associations with lung cancer risk and mortality. A 2024 review reports, for example, **AHSMOG-2**: a **10 μg/m³** PM2.5 increase associated with **HR 1.43** (95% CI 1.03–2.00) for lung cancer. (yoo2024updateinassociation pages 2-3)

**Mechanistic plausibility** described in the same review includes oxidative stress, inflammation, and DNA damage/mutagenesis pathways induced by PM components (e.g., PAHs, metals) and ROS signaling. (yoo2024updateinassociation pages 2-3)

#### Occupational carcinogens: cadmium (example with quantitative meta-analysis)
A 2024 systematic review/meta-analysis reported higher cadmium exposure associated with increased lung cancer risk: **OR 1.31** (95% CI 1.06–1.62; p=0.024), interpreted as a 31% increase. (farahmandian2024investigatingtherelationship pages 1-2)

#### Radon
Radon is commonly described as a leading non-tobacco cause (particularly in the US) and has no known safe level; the EPA remediation threshold **4 pCi/L (148 Bq/m³)** is cited in a 2024 review. (laguna2024geographicdifferencesin pages 1-3)

### Protective factors
Direct protective-factor estimates were not retrieved in the current evidence set. In practice, major protective factors include tobacco cessation and reduction of carcinogen exposures; smoking cessation is emphasized as a key preventive action within screening guidelines. (wolf2024screeningforlung pages 7-7)

### Gene–environment interactions
A 2024 review notes associations between exposure patterns and driver distributions: EGFR mutations are more common in never-smokers and some populations, while **KRAS G12C** is associated with smoking history. (laguna2024geographicdifferencesin pages 1-3)

---

## 3. Phenotypes

### Clinical presentation (metastatic disease)
mNSCLC can present with pulmonary symptoms (cough, dyspnea), systemic symptoms (weight loss), and/or organ-specific symptoms from metastases. In a SEER-M1 analysis, common metastatic organs vary by histology (see “Anatomical structures affected”). (xie2024distantmetastasispatterns pages 1-2, xie2024distantmetastasispatterns pages 2-3)

### Metastasis-associated phenotypes & HPO term suggestions
Below are common metastasis-related phenotype groupings relevant to mNSCLC knowledge-base annotation. Frequencies are not uniformly available across all studies in the retrieved evidence; where available, they are provided.

1. **Bone metastasis / skeletal complications**
   - Evidence of frequency/pattern: In SEER M1 lung cancer, bone metastasis was most common in lung adenocarcinoma (ADC), squamous (SCC), adenosquamous (ASC), and large cell carcinoma (LCC) (e.g., ADC bone metastasis 35.15%). (xie2024distantmetastasispatterns pages 2-3)
   - EGFR-mutant cohort: vertebrae (76.3%) and pelvis (60.9%) were frequent bone sites. (tanaka2024femoralbonemetastasis pages 1-3)
   - Suggested HPO: **HP:0002652** (Skeletal metastasis), **HP:0002653** (Bone pain), **HP:0012655** (Pathologic fracture).

2. **Brain metastasis / neurologic manifestations**
   - Epidemiology note: brain metastases present in a meaningful subset; a real-world US cohort reported brain metastases present in **22.9%** of advanced NSCLC patients at treatment initiation. (hektoen2024realworldevidencefor pages 3-5)
   - Suggested HPO: **HP:0002506** (Brain metastasis), **HP:0001288** (Gait disturbance), **HP:0001250** (Seizures), **HP:0002315** (Headache).

3. **Liver metastasis / hepatic dysfunction**
   - In SEER, liver metastases were particularly common in SCLC rather than NSCLC, but liver involvement in advanced NSCLC is prognostically important (see prognosis section). (xie2024distantmetastasispatterns pages 2-3, brown2024sitespecificresponseand pages 11-12)
   - Suggested HPO: **HP:0001410** (Hepatomegaly), **HP:0001397** (Hepatic metastasis), **HP:0002904** (Elevated hepatic transaminases) (laboratory abnormality).

4. **Adrenal metastasis**
   - Mentioned as a common extrathoracic site in advanced NSCLC cohorts. (brown2024sitespecificresponseand pages 1-2)
   - Suggested HPO: **HP:0031909** (Adrenal metastasis) (if available in HPO; otherwise annotate as adrenal mass + cancer).

### Quality of life impact
Direct QoL instrument data (e.g., EQ-5D, SF-36) specific to metastatic NSCLC were not retrieved in the current evidence set; however, the metastatic burden and organ involvement (bone/brain) are consistently associated with poorer survival and often correlate with functional decline. (brown2024sitespecificresponseand pages 11-12, tanaka2024femoralbonemetastasis pages 1-3)

---

## 4. Genetic / Molecular Information

### Core concept: actionable somatic drivers and biomarkers
Modern mNSCLC management is biomarker-driven: actionable genomic alterations and immune biomarkers (PD-L1, sometimes TMB) are used to select targeted therapy or immunotherapy.

A 2024 review lists actionable first-line targets in unresectable/advanced/metastatic NSCLC including **EGFR**, **ALK**, **ROS1**, **RET**, **NTRK1/2/3** fusions, **BRAF V600E**, and **MET exon 14** skipping; immune selection includes **PD-L1 TPS ≥50%** for PD-1/PD-L1 monotherapy when no sensitizing EGFR/ALK alterations are present. (li2024evolvingprecisionfirstline pages 1-2)

A separate 2024 review emphasizes broad panels and includes additional emerging targets such as **ERBB2 (HER2)** and **KRAS G12C**. (li2024evolvingprecisionfirstline pages 4-6)

#### Suggested genes (HGNC symbols)
EGFR, KRAS, ALK, ROS1, MET, RET, ERBB2, BRAF, NTRK1, NTRK2, NTRK3, TP53, STK11, KEAP1.

### Pathogenic variants (somatic)
- **EGFR** activating variants: exon 19 deletions, L858R (used as eligibility in EGFR-mutant metastatic trials). (cho2024amivantamabpluslazertinib pages 1-4)
- **KRAS G12C**: occurs in ~13% of lung adenocarcinomas; KRAS mutations overall ~25–30% of NSCLC; G12C ~40% of KRAS-mutated NSCLC. (chour2024mechanismsofresistance pages 1-2, warnecke2024adagrasibinthe pages 1-2)
- **ERBB2 (HER2)**: HER2 mutations occur in ~4% of NSCLC; common exon 20 insertion A775_G776insYVMA ~34% of HER2 mutations. (ferrari2024her2alterednonsmallcell pages 1-2)

### Molecular biomarkers (immune)
- **PD-L1 TPS ≥50%**: used to select PD-1/PD-L1 monotherapy as standard of care in biomarker-driven algorithms. (li2024evolvingprecisionfirstline pages 1-2)
- A large combined trial + real-world analysis found tumor **PD-L1 ≥50%** specifically associated with CPI response, and **TMB ≥10.44 mut/Mb** associated with durable CPI response; combined high TMB + high PD-L1 was the strongest predictor reported (OR 0.04). (hektoen2024realworldevidencefor pages 3-5, cho2024amivantamabpluslazertinib pages 7-8)

### Resistance mechanisms (selected examples)
- **KRAS G12C inhibitors:** resistance frequently acquired; includes on-target KRAS mutations affecting inhibitor binding and off-target bypass via NRAS, BRAF, RET activation, PTEN loss, EMT, and histologic transformation. (chour2024mechanismsofresistance pages 1-2)

### Epigenetic / chromosomal abnormalities
Specific epigenetic or chromosomal-abnormality datasets were not retrieved in the current evidence set.

---

## 5. Environmental Information

### Environmental and lifestyle factors
- **Ambient PM2.5** exposure shows increased risk and mortality with mechanistic links to ROS/oxidative stress and DNA damage. (yoo2024updateinassociation pages 2-3)
- **Cadmium** exposure is associated with increased risk (meta-analysis OR 1.31). (farahmandian2024investigatingtherelationship pages 1-2)
- **Radon** exposure is emphasized as a major residential risk and policy target (EPA action level 4 pCi/L). (laguna2024geographicdifferencesin pages 1-3)

### Infectious agents
No specific infectious causal agents for NSCLC were retrieved in the current evidence set.

---

## 6. Mechanism / Pathophysiology

### Core oncogenic signaling pathways
- **EGFR pathway** and downstream MAPK/PI3K signaling drive EGFR-mutant NSCLC; EGFR-directed therapies improve outcomes in biomarker-selected metastatic disease (see Treatments). (cho2024amivantamabpluslazertinib pages 1-4)
- **KRAS** is a small GTPase cycling between GDP/GTP states; KRAS G12C inhibitors covalently target the inactive GDP-bound state and suppress downstream **MAPK** and **PI3K** signaling. (chour2024mechanismsofresistance pages 1-2)

### Tumor microenvironment (TME) and immune evasion
Organ-specific microenvironments influence immunotherapy response: bone and liver metastases are associated with lower response and worse outcomes, suggesting site-specific immune resistance. (brown2024sitespecificresponseand pages 11-12, brown2024sitespecificresponseand pages 1-2)

### Mechanistic chain (example: KRAS G12C targeted therapy)
1) KRAS G12C mutation → accumulation of KRAS(GDP)-bound fraction amenable to covalent inhibitors → initial MAPK/PI3K suppression → tumor response. (chour2024mechanismsofresistance pages 1-2)
2) Adaptive feedback and bypass signaling (e.g., NRAS/BRAF/RET activation; PTEN loss) and phenotypic shifts (EMT, transformation) → acquired resistance and progression. (chour2024mechanismsofresistance pages 1-2)

### Suggested GO biological process terms (illustrative)
- **GO:0007169** (transmembrane receptor protein tyrosine kinase signaling pathway)
- **GO:0000165** (MAPK cascade)
- **GO:0008285** (negative regulation of cell population proliferation) / dysregulation in cancer
- **GO:0042110** (T cell activation) (immune context)

### Suggested Cell Ontology (CL) terms (illustrative)
- **CL:0000182** (T cell)
- **CL:0000236** (B cell)
- **CL:0000624** (CD4-positive, alpha-beta T cell)
- **CL:0000625** (CD8-positive, alpha-beta T cell)
- **CL:0000451** (dendritic cell)
- **CL:0000235** (macrophage)

(These ontology suggestions are generic to tumor/immune interactions; the retrieved evidence supports immune and microenvironment involvement but does not enumerate CL/GO terms explicitly.) (yoo2024updateinassociation pages 2-3, brown2024sitespecificresponseand pages 11-12)

---

## 7. Anatomical Structures Affected

### Organ-level sites (metastases)
A SEER-based analysis (2010–2019; 77,827 M1 cases) found histology-specific metastatic patterns:
- **Bone**: most common in ADC, SCC, ASC, LCC (e.g., ADC 35.15%). (xie2024distantmetastasispatterns pages 2-3)
- **Brain**: particularly common in LCNEC. (xie2024distantmetastasispatterns pages 1-2)
- **Liver**: particularly common in SCLC (included here for lung cancer context). (xie2024distantmetastasispatterns pages 2-3)
- **Lung-to-lung (intrapulmonary)**: common in carcinoid tumors and SCC. (xie2024distantmetastasispatterns pages 1-2)

### UBERON term suggestions (common sites)
- Lung: **UBERON:0002048**
- Bone tissue: **UBERON:0002481**
- Brain: **UBERON:0000955**
- Liver: **UBERON:0002107**
- Adrenal gland: **UBERON:0002369**

---

## 8. Temporal Development

### Onset and progression
Most lung cancer is diagnosed at advanced stages in many populations; a review notes that “most cases are diagnosed in advanced stages,” emphasizing prevention/early diagnosis importance. (laguna2024geographicdifferencesin pages 1-3)

### Disease stages
mNSCLC corresponds to metastatic (M1) disease; SEER data indicate substantial proportion present with metastasis at diagnosis (e.g., 41.22% M1 lung cancers with distant metastasis at presentation in one SEER analysis). (xie2024distantmetastasispatterns pages 1-2)

---

## 9. Inheritance and Population

### Epidemiology (selected, recent population-based data)
- **SEER-Medicare metastatic NSCLC (2015–2019; n=17,134):** overall median OS **7 months**, 1-year OS **34%**, 2-year OS **21%**. (uprety2024racialandsocioeconomic pages 3-4)
- **ICI utilization:** ~**39%** received an immune checkpoint inhibitor; utilization increased from **21.9% (2015)** to **55.4% (2019)**. (uprety2024racialandsocioeconomic pages 3-4)
- **Survival disparity:** 2-year OS from diagnosis differed by race (White 22%, Asian 23%, Black 15%, Hispanic 17%); among ICI recipients, racial differences in survival were not statistically significant, suggesting access/utilization drives disparity. (uprety2024racialandsocioeconomic pages 1-2)

### Genetic etiology and inheritance
mNSCLC is primarily driven by **somatic** alterations; a 2024 review notes pathogenic germline variants in high/moderate penetrance genes in **4.3%** of a cohort (germline susceptibility signal, not typically a Mendelian inheritance pattern for mNSCLC). (laguna2024geographicdifferencesin pages 1-3)

---

## 10. Diagnostics

### Tissue diagnosis and immunohistochemistry
Histologic classification in small biopsies often uses IHC panels: **TTF-1 / napsin A** (adenocarcinoma) and **p40 / p63** (squamous). (li2024evolvingprecisionfirstline pages 2-4)

### Molecular testing (tissue NGS and fusions)
CAP/IASLC/AMP guidance (as summarized in a 2024 review) recommends testing all advanced lung cancers for sensitizing **EGFR** and **ALK**, with expansion to **ROS1** and **BRAF** and then **RET, MET, ERBB2, KRAS** if earlier drivers are negative; NGS is emphasized for SNVs/CNVs/fusions and high yield. (li2024evolvingprecisionfirstline pages 2-4)

RNA-based NGS can improve fusion detection (ALK/ROS1/RET/NTRK). (li2024evolvingprecisionfirstline pages 4-6)

### Immune biomarker testing
**PD-L1 IHC** is used for PD-1/PD-L1 selection; PD-L1 **TPS ≥50%** is used as a key threshold for monotherapy selection in biomarker algorithms. (li2024evolvingprecisionfirstline pages 1-2)

### Liquid biopsy / ctDNA
When tissue is insufficient or re-biopsy may delay care, plasma ctDNA can accelerate profiling and capture alterations from primary and metastatic sites. (li2024evolvingprecisionfirstline pages 4-6)

ctDNA is also used for resistance monitoring (e.g., EGFR T790M) and treatment decision support. (restrepo2024identificationandapplication pages 15-16)

### MET amplification testing thresholds (example of concrete numeric definitions)
A 2024 review of MET amplification reports:
- Primary METamp prevalence ~**4.8%**; secondary (post-EGFR-TKI) METamp ~**15%**. (yang2024nonsmallcelllung pages 1-2)
- Definition variability: FISH ratios (MET:CEP7 ≥1.8 to ≥3.0) or gene copy number (GCN ≥5 to ≥10); NGS tissue thresholds (GCN ≥6); liquid biopsy thresholds reported (MET copy number ≥2.1 to >5). (yang2024nonsmallcelllung pages 1-2)
- NCCN notes copy number **>10** consistent with high-level MET amplification (NGS). (yang2024nonsmallcelllung pages 3-5)

### Differential diagnosis
Specific differential-diagnosis algorithms were not retrieved in the current evidence set.

---

## 11. Outcome / Prognosis

### Survival statistics (recent)
- **Population-based metastatic NSCLC (SEER-Medicare 2015–2019):** median OS **7 months**; 2-year OS **21%**. (uprety2024racialandsocioeconomic pages 3-4)
- **Real-world first-line immunotherapy era (Norway 2012–2021):** median OS improved from **8.0 months** (historical chemo) to **13.8 months** (pembrolizumab monotherapy) and **12.8 months** (pembrolizumab + chemotherapy). (hektoen2024realworldevidencefor pages 1-2)

### Prognostic factors (metastatic site)
- Bone metastases are repeatedly associated with worse outcomes.
  - In a 2024 cohort, bone metastases were linked to shorter OS (median **10 vs 21 months**; HR **1.95**) and shorter PFS (HR **1.70**). (brown2024sitespecificresponseand pages 11-12)
  - A multicenter immunotherapy cohort found presence of bone metastases independently worsened OS (HR **1.26**). (xie2024distantmetastasispatterns pages 2-3)

---

## 12. Treatment

### Current first-line paradigms (conceptual)
For metastatic NSCLC without sensitizing oncogenic drivers, ICIs as monotherapy (PD-L1-high) or chemoimmunotherapy (PD-L1 low/negative) are standard approaches; for biomarker-defined drivers (EGFR/ALK/ROS1/RET/MET/BRAF/etc.) targeted therapies are prioritized. (li2024evolvingprecisionfirstline pages 1-2)

### Recent developments / latest research (prioritizing 2023–2024)

#### EGFR-mutant metastatic NSCLC: MARIPOSA (practice-changing 2024)
**MARIPOSA (NEJM, Oct 2024)** compared **amivantamab + lazertinib** vs **osimertinib** first-line in EGFR exon19del/L858R advanced/metastatic NSCLC.
- **Efficacy:** median PFS **23.7 vs 16.6 months**, HR **0.70** (95% CI 0.58–0.85; P<0.001). ORR **86% vs 85%**; median DoR **25.8 vs 16.8 months**; interim OS HR **0.80** (95% CI 0.61–1.05). (cho2024amivantamabpluslazertinib pages 8-9, cho2024amivantamabpluslazertinib pages 9-11)
- **Safety:** grade ≥3 AEs **75% vs 43%**; infusion reactions **63%**; venous thromboembolism **37% vs 9%**; AE-related discontinuation **35% vs 14%**. (cho2024amivantamabpluslazertinib pages 9-11)

**Figure evidence:** Kaplan–Meier PFS separation and hazard ratio are shown in the extracted figure. (cho2024amivantamabpluslazertinib media ee6afa38)

**Abstract quote:** “*The median progression-free survival was significantly longer in the amivantamab-lazertinib group than in the osimertinib group (23.7 vs. 16.6 months; hazard ratio … 0.70 …; P<0.001).*” (cho2024amivantamabpluslazertinib pages 1-4)

**Suggested MAXO terms** (illustrative): tyrosine kinase inhibitor therapy; monoclonal antibody therapy; combination antineoplastic therapy.

#### KRAS G12C metastatic NSCLC (targeted therapy; resistance-focused 2024 synthesis)
- **Frequency:** KRAS G12C is found in ~**13%** of lung adenocarcinomas. (chour2024mechanismsofresistance pages 1-2)
- **Phase 3 evidence:** in CodeBreaK 200, sotorasib vs docetaxel improved PFS (**5.6 vs 4.5 months**, HR 0.66) and ORR (**28.1% vs 13.2%**) but not OS (10.6 vs 11.3 months). (warnecke2024adagrasibinthe pages 4-5)
- **Adagrasib CNS activity (summary):** intracranial ORR **42%** with intracranial PFS **5.4 months**; systemic ORR **30%**, PFS **5.3 months**. (warnecke2024adagrasibinthe pages 4-5)
- **Mechanisms of resistance:** bypass activation (NRAS/BRAF/RET), PTEN loss, EMT, histologic transformation; on-target KRAS mutations preventing binding. (chour2024mechanismsofresistance pages 1-2)

**Suggested MAXO:** targeted small molecule therapy; molecularly targeted therapy; tumor sequencing-guided therapy.

#### HER2 (ERBB2)-mutant metastatic NSCLC: ADCs (2024 state-of-the-art)
- **Frequency:** HER2 mutations ~**4%** of NSCLC; common exon 20 insertion A775_G776insYVMA ~**34%** of HER2 mutations. (ferrari2024her2alterednonsmallcell pages 1-2)
- **Trastuzumab deruxtecan (T-DXd):** DESTINY-Lung01 (HER2-mutant; N=91) ORR ~**55%**, median PFS **8.2 months**, median OS **17.8–18.6 months**. (lazaratos2024apotentialcentral pages 1-2, wang2024addressingtheunmet pages 3-5)
- **DESTINY-Lung02 (dose cohorts):** ORR around **53.8% vs 42.9%** (5.4 vs 6.4 mg/kg) in one summary. (wang2024addressingtheunmet pages 3-5)
- **Intracranial relevance:** reviews emphasize CNS activity and report subgroup outcomes in patients with stable brain metastases. (lazaratos2024apotentialcentral pages 2-4, ferrari2024her2alterednonsmallcell pages 1-2)

**Suggested MAXO:** antibody–drug conjugate therapy; HER2-targeted therapy.

#### Immunotherapy real-world implementation (effectiveness)
- In a nationwide Norwegian cohort, first-line pembrolizumab OS improved versus historical chemotherapy (median OS **13.8** months for pembrolizumab monotherapy and **12.8** months for pembrolizumab+chemo vs **8.0** months pre-ICI). (hektoen2024realworldevidencefor pages 1-2)
- In an Israeli health-system cohort (mNSCLC), median real-world OS from first-line was **12.5 months** for PD-1 monotherapy and **14.8 months** for PD-1 + chemotherapy among nonsquamous patients without EGFR/ALK/ROS1; outcomes were better in ECOG 0–1 and PD-L1 ≥50% (e.g., median rwOS **25.1 months** for ECOG 0–1 with monotherapy). (apter2024realworldtreatmentpatterns pages 1-2)

**Expert analysis in authoritative sources:** Real-world cohorts repeatedly observe lower OS than pivotal trials but preservation of the relative benefit compared with chemotherapy, supporting generalizability while highlighting trial-to-practice gaps (age, ECOG, comorbidities). (hektoen2024realworldevidencefor pages 1-2)

---

## 13. Prevention

### Primary prevention
- Reduce tobacco exposure and implement smoking-cessation interventions; ACS guideline emphasizes cessation counseling and connection to resources for current smokers. (wolf2024screeningforlung pages 7-7)
- Reduce environmental/occupational exposures (PM2.5 reduction, radon mitigation, carcinogen control) supported by risk estimates and mechanistic plausibility. (yoo2024updateinassociation pages 2-3, laguna2024geographicdifferencesin pages 1-3)

### Secondary prevention: Screening (ACS 2023 update; published Nov 2024)
ACS recommends **annual LDCT** lung cancer screening for asymptomatic individuals:
- **Age:** **50–80 years**
- **Smoking:** **≥20 pack-years**
- **Smoking status:** current or former smokers; **years-since-quitting is not used** as an eligibility criterion. (wolf2024screeningforlung pages 2-3, wolf2024screeningforlung pages 7-7)

**Abstract quote:** “*The ACS recommends annual LCS with low‐dose computed tomography for asymptomatic individuals aged 50–80 years who currently smoke or formerly smoked and have a ≥20 pack‐year smoking history.*” (wolf2024screeningforlung pages 1-2)

---

## 14. Other Species / Natural Disease

Direct comparative pathology or naturally occurring non-human mNSCLC content was not retrieved in the current evidence set.

---

## 15. Model Organisms / Model Systems

### Patient-derived xenografts (PDX)
- A 2024 study established **13 NSCLC-PDXs from 62 patients**, reporting preservation of histology/genetics and concordant chemotherapy responses between PDX and matched patients; an osimertinib-resistant PDX implicated **DUSP6 M62I** and MAPK-ERK overactivation, with trametinib slowing resistant tumor growth. (wang2024utilityofpatientderived pages 1-2)
- TRACERx multi-region analysis generated **48 PDX models from 22 patients**, showing multi-region sampling improves engraftment but individual PDXs often represent a single subclone (genomic bottleneck) and do not fully recapitulate intratumor heterogeneity. (hynds2024representationofgenomic pages 1-2)

### Patient-derived organoids (PDOs)
- Pleural effusion-derived organoids can be used for rapid therapy-response prediction in advanced EGFR-mutant NSCLC: drug-response evaluation within ~1 week and clinically aligned response classification within **10 days** (validated in **14** patients). (lee2024predictionoftki pages 1-2)
- A 2024 Cell Reports Medicine paper describes using LUAD PDOs to model metastases and test resistance mechanisms (e.g., KRASG12C PDOs treated with sotorasib) and notes limitations of PDXs for metastasis biology (rare metastasis in LUAD PDX). (liu2024modelinglungadenocarcinoma pages 1-4)

---

## Evidence tables (for knowledge-base population)

| Entity | Definition / scope | Synonyms / alternative names | MONDO | MeSH | ICD | Notes / evidence |
|---|---|---|---|---|---|---|
| Metastatic non-small cell lung cancer | Advanced NSCLC with distant metastatic spread; often operationally aligned with stage IV disease in clinical studies and population datasets | mNSCLC; metastatic NSCLC; advanced NSCLC (when metastatic cohort) |  |  |  | Specific MONDO/MeSH/ICD identifier for the metastatic-stage entity was not found in retrieved evidence; studies explicitly use “metastatic NSCLC” terminology (apter2024realworldtreatmentpatterns pages 1-2, uprety2024racialandsocioeconomic pages 3-4) |
| Stage IV non-small cell lung cancer | AJCC/registry stage IV NSCLC; commonly used as a proxy for metastatic disease in epidemiologic and treatment studies | stage IV NSCLC; metastatic stage NSCLC |  |  |  | Used in SEER/SEER-Medicare analyses and real-world treatment datasets; exact ICD/MeSH/MONDO code not reported in retrieved evidence (yang2024disparitiesinutilization pages 1-2, yang2024disparitiesinutilization pages 2-3) |
| Non-small cell lung cancer | Major lung cancer class comprising ~80%–90% of lung cancers; umbrella category including adenocarcinoma and squamous carcinoma | NSCLC; non-small-cell lung cancer; non-small cell lung carcinoma |  |  |  | Disease-level identifiers were not reported in retrieved evidence; Open Targets lists non-small cell lung carcinoma as EFO_0003060 (not MONDO) (apter2024realworldtreatmentpatterns pages 1-2, OpenTargets Search: Non-small cell lung carcinoma,Lung adenocarcinoma,Lung squamous cell carcinoma) |
| Non-squamous NSCLC / lung adenocarcinoma predominant mNSCLC | Common metastatic NSCLC subtype in immunotherapy-era cohorts | NSQ NSCLC; adenocarcinoma-predominant NSCLC |  |  |  | In one mNSCLC real-world cohort, 85% had adenocarcinoma histology; exact ontology identifiers not reported in retrieved evidence (apter2024realworldtreatmentpatterns pages 1-2) |
| Squamous NSCLC | Squamous histologic subtype of NSCLC | squamous cell NSCLC; squamous cell carcinoma of lung (NSCLC context) | MONDO_0056806 (for non-small cell squamous lung carcinoma in Open Targets context) |  |  | Histology-specific related entity rather than the target disease; included because many metastatic cohorts stratify by histology (OpenTargets Search: Non-small cell lung carcinoma,Lung adenocarcinoma,Lung squamous cell carcinoma, apter2024realworldtreatmentpatterns pages 1-2) |

| Setting / population | Biomarker | Intervention | Comparator | Key outcomes (PFS / OS / ORR) | Notable safety | Publication (year, journal) | URL |
|---|---|---|---|---|---|---|---|
| Previously untreated EGFR-mutated locally advanced/metastatic NSCLC (MARIPOSA) | EGFR exon 19 deletion or L858R | Amivantamab + lazertinib | Osimertinib | Median PFS 23.7 vs 16.6 mo; HR 0.70 (95% CI 0.58–0.85); ORR 86% vs 85%; median DoR 25.8 vs 16.8 mo; interim OS HR 0.80 (95% CI 0.61–1.05) (cho2024amivantamabpluslazertinib pages 8-9, cho2024amivantamabpluslazertinib pages 1-4, cho2024amivantamabpluslazertinib pages 9-11) | Grade ≥3 AEs 75% vs 43%; infusion-related reactions 63%; VTE 37% vs 9%; discontinuation due to AEs 35% vs 14%; discontinuation of all agents due to treatment-related AEs 10% vs 3% (cho2024amivantamabpluslazertinib pages 11-12, cho2024amivantamabpluslazertinib pages 9-11, cho2024amivantamabpluslazertinib media ee6afa38) | Cho et al., 2024, *New England Journal of Medicine* | https://doi.org/10.1056/NEJMoa2403614 |
| Nationwide Norway real-world advanced/metastatic NSCLC initiating 1L systemic therapy, 2012–2021 | No targetable mutation required; pembrolizumab-treated cohorts reflect standard clinical selection | Pembrolizumab monotherapy or pembrolizumab + chemotherapy | Historical pre-ICI platinum chemotherapy | Median OS: pembrolizumab mono 13.8 mo; pembrolizumab + chemo 12.8 mo; historical chemo 8.0 mo; 2-year OS increased to ~35% (mono) and ~31% (combo) vs ~19% pre-ICI (hektoen2024realworldevidencefor pages 5-6, hektoen2024realworldevidencefor pages 7-8, hektoen2024realworldevidencefor pages 1-2) | Real-world patients were older and broader than KEYNOTE trial populations; specific PFS not reported in retrieved excerpts (hektoen2024realworldevidencefor pages 5-6, hektoen2024realworldevidencefor pages 1-2) | Hektoen et al., 2024, *British Journal of Cancer* | https://doi.org/10.1038/s41416-024-02895-1 |
| SEER-Medicare metastatic NSCLC, diagnosed 2015–2019 (n=17,134) | Population-level; not biomarker-selected | Immune checkpoint inhibitor exposure (any approved ICI claim) | No ICI / population benchmark | ICI utilization 38.7% (~39%); overall median OS 7 mo; 1-year OS 34%; 2-year OS 21%; 2-year OS from ICI initiation 30% vs 11% without ICI (uprety2024racialandsocioeconomic pages 3-4, uprety2024racialandsocioeconomic pages 1-2, uprety2024racialandsocioeconomic pages 2-3) | Main issue highlighted was access disparity rather than toxicity; lower ICI use in Black, lower-SES, rural, and dual-eligible groups (uprety2024racialandsocioeconomic pages 3-4, uprety2024racialandsocioeconomic pages 1-2) | Uprety et al., 2024, *JNCI Journal of the National Cancer Institute* | https://doi.org/10.1093/jnci/djae118 |
| Previously treated KRAS G12C-mutated advanced/metastatic NSCLC (phase III CodeBreaK 200) | KRAS G12C | Sotorasib | Docetaxel | Median PFS 5.6 vs 4.5 mo; HR 0.66; ORR 28.1% vs 13.2%; median OS 10.6 vs 11.3 mo (not statistically different) (chour2024mechanismsofresistance pages 1-2, warnecke2024adagrasibinthe pages 4-5) | TRAEs common; pooled meta-analysis suggests any-grade trAEs 79.3% and grade ≥3 trAEs 24.4% across KRAS G12C inhibitors; sotorasib had better pooled safety than adagrasib (warnecke2024adagrasibinthe pages 4-5, dang2024efficacyandtoxicity pages 1-2) | Summarized in Warnecke & Nagasaka, 2024, *Drug Design, Development and Therapy*; Chour et al., 2024, *Frontiers in Oncology* | https://doi.org/10.2147/DDDT.S466217 |
| KRAS G12C-mutated advanced/metastatic NSCLC with CNS-active/refractory disease evidence (KRYSTAL program summaries) | KRAS G12C | Adagrasib | Mostly single-arm / some docetaxel comparison in KRYSTAL-12 intracranial subset | Intracranial ORR 42% (95% CI 20–66.5%); intracranial PFS 5.4 mo; intracranial DoR 12.7 mo; systemic ORR 30%; systemic PFS 5.3 mo; KRYSTAL-12 intracranial ORR 40% vs 11% with docetaxel (warnecke2024adagrasibinthe pages 4-5) | Adagrasib generally associated with more toxicity than sotorasib in pooled analyses; resistance common via on-target/off-target bypass mechanisms (chour2024mechanismsofresistance pages 1-2, dang2024efficacyandtoxicity pages 1-2) | Warnecke & Nagasaka, 2024, *Drug Design, Development and Therapy* | https://doi.org/10.2147/DDDT.S466217 |
| Pretreated HER2-mutant metastatic NSCLC (DESTINY-Lung01) | HER2 / ERBB2 mutation | Trastuzumab deruxtecan (T-DXd) 6.4 mg/kg | Single-arm | ORR 54.9–55%; median PFS 8.2 mo; median OS 17.8–18.6 mo; median DoR 10.6 mo; DCR 92% (lazaratos2024apotentialcentral pages 1-2, lazaratos2024apotentialcentral pages 2-4, wang2024addressingtheunmet pages 3-5) | Interstitial lung disease is a major toxicity concern; pooled/summary estimates ~11.6% ILD overall with grade 5 events reported in reviews (lazaratos2024apotentialcentral pages 2-4) | Summarized in Ferrari et al., 2024, *Cancers*; Wang et al., 2024, *Exploration of Targeted Anti-tumor Therapy* | https://doi.org/10.3390/cancers16112018 |
| Pretreated HER2-mutant advanced/metastatic NSCLC (DESTINY-Lung02) | HER2 / ERBB2 mutation | Trastuzumab deruxtecan 5.4 mg/kg (approved dose) | 6.4 mg/kg cohort / non-comparative dose evaluation | ORR 53.8% vs 42.9% (5.4 vs 6.4 mg/kg) in one summary; another review reports approved-dose ORR 49.0%, median DoR 16.8 mo, median PFS 9.9 mo (wang2024addressingtheunmet pages 3-5, li2024shra1811(antibodydrugconjugate) pages 1-2) | ILD/pneumonitis monitoring remains essential; intracranial activity also noted in reviews and brain-metastasis subgroups (lazaratos2024apotentialcentral pages 2-4, ferrari2024her2alterednonsmallcell pages 1-2) | Li et al., 2024, *Signal Transduction and Targeted Therapy*; Ferrari et al., 2024, *Cancers* | https://doi.org/10.1038/s41392-024-01897-y |


*Table: This artifact provides two compact tables: one for disease naming/identifier coverage in the retrieved evidence, and one for pivotal 2024 metastatic NSCLC efficacy and safety figures across major treatment settings. It is useful for quickly mapping terminology and comparing contemporary clinical outcomes across targeted therapy, immunotherapy, and population-level datasets.*

---

## Notes on evidence limitations in this run
1) Several requested ontology identifiers (ICD-10/11, MeSH, metastatic-stage MONDO) were not present in the retrieved full-text corpus and should be added from ontology resources. 2) Some sections (QoL instruments, detailed differential diagnosis, epigenetics) require additional targeted retrieval beyond the current evidence set.


References

1. (OpenTargets Search: Non-small cell lung carcinoma,Lung adenocarcinoma,Lung squamous cell carcinoma): Open Targets Query (Non-small cell lung carcinoma,Lung adenocarcinoma,Lung squamous cell carcinoma, 40 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

2. (apter2024realworldtreatmentpatterns pages 1-2): Lior Apter, Sarah Sharman Moser, Ashwini Arunachalam, Sivan Gazit, Moshe Hoshen, Gabriel Chodick, and Nava Siegelmann-Danieli. Real-world treatment patterns, biomarker testing, and clinical outcomes of metastatic non-small cell lung cancer patients in the immunotherapy era. Frontiers in Oncology, Oct 2024. URL: https://doi.org/10.3389/fonc.2024.1442909, doi:10.3389/fonc.2024.1442909. This article has 2 citations.

3. (uprety2024racialandsocioeconomic pages 3-4): Dipesh Uprety, Randell Seaton, Tarik Hadid, Hirva Mamdani, Ammar Sukari, Julie J Ruterbusch, and Ann G Schwartz. Racial and socioeconomic disparities in survival among patients with metastatic non–small cell lung cancer. JNCI Journal of the National Cancer Institute, 116:1697-1704, Jun 2024. URL: https://doi.org/10.1093/jnci/djae118, doi:10.1093/jnci/djae118. This article has 17 citations.

4. (yang2024disparitiesinutilization pages 1-2): Danting Yang, Shama D. Karanth, Hyung-Suk Yoon, Jae Jeong Yang, Xiwei Lou, Jiang Bian, Dongyu Zhang, Yi Guo, Lusine Yaghjyan, Tomi Akinyemiju, Estelamari Rodriguez, Hiren J. Mehta, and Dejana Braithwaite. Disparities in utilization of immune checkpoint inhibitor therapy among older patients with advanced non–small cell lung cancer: a seer-medicare analysis. JCO Oncology Advances, Dec 2024. URL: https://doi.org/10.1200/oa.24.00008, doi:10.1200/oa.24.00008. This article has 6 citations.

5. (hektoen2024realworldevidencefor pages 1-2): Helga H. Hektoen, Kaitlyn M. Tsuruda, Lars Fjellbirkeland, Yngvar Nilssen, Odd Terje Brustugun, and Bettina K. Andreassen. Real-world evidence for pembrolizumab in non-small cell lung cancer: a nationwide cohort study. British Journal of Cancer, 132:93-102, Nov 2024. URL: https://doi.org/10.1038/s41416-024-02895-1, doi:10.1038/s41416-024-02895-1. This article has 27 citations and is from a domain leading peer-reviewed journal.

6. (hektoen2024realworldevidencefor pages 5-6): Helga H. Hektoen, Kaitlyn M. Tsuruda, Lars Fjellbirkeland, Yngvar Nilssen, Odd Terje Brustugun, and Bettina K. Andreassen. Real-world evidence for pembrolizumab in non-small cell lung cancer: a nationwide cohort study. British Journal of Cancer, 132:93-102, Nov 2024. URL: https://doi.org/10.1038/s41416-024-02895-1, doi:10.1038/s41416-024-02895-1. This article has 27 citations and is from a domain leading peer-reviewed journal.

7. (cho2024amivantamabpluslazertinib pages 8-9): Byoung C. Cho, Shun Lu, Enriqueta Felip, Alexander I. Spira, Nicolas Girard, Jong-Seok Lee, Se-Hoon Lee, Yurii Ostapenko, Pongwut Danchaivijitr, Baogang Liu, Adlinda Alip, Ernesto Korbenfeld, Josiane Mourão Dias, Benjamin Besse, Ki-Hyeong Lee, Hailin Xiong, Soon-Hin How, Ying Cheng, Gee-Chen Chang, Hiroshige Yoshioka, James C.-H. Yang, Michael Thomas, Danny Nguyen, Sai-Hong I. Ou, Sanjay Mukhedkar, Kumar Prabhash, Manolo D’Arcangelo, Jorge Alatorre-Alexander, Juan C. Vázquez Limón, Sara Alves, Daniil Stroyakovskiy, Marina Peregudova, Mehmet A.N. Şendur, Ozan Yazici, Raffaele Califano, Vanesa Gutiérrez Calderón, Filippo de Marinis, Antonio Passaro, Sang-We Kim, Shirish M. Gadgeel, John Xie, Tao Sun, Melissa Martinez, Mariah Ennis, Elizabeth Fennema, Mahesh Daksh, Dawn Millington, Isabelle Leconte, Ryota Iwasawa, Patricia Lorenzini, Mahadi Baig, Sujay Shah, Joshua M. Bauml, S. Martin Shreeve, Seema Sethi, Roland E. Knoblauch, and Hidetoshi Hayashi. Amivantamab plus lazertinib in previously untreated <i>egfr</i> -mutated advanced nsclc. New England Journal of Medicine, 391:1486-1498, Oct 2024. URL: https://doi.org/10.1056/nejmoa2403614, doi:10.1056/nejmoa2403614. This article has 450 citations and is from a highest quality peer-reviewed journal.

8. (laguna2024geographicdifferencesin pages 1-3): Juan Carlos Laguna, Miguel García-Pardo, Joao Alessi, Carlos Barrios, Navneet Singh, Humaid O. Al-Shamsi, Herbert Loong, Miquel Ferriol, Gonzalo Recondo, and Laura Mezquita. Geographic differences in lung cancer: focus on carcinogens, genetic predisposition, and molecular epidemiology. Therapeutic Advances in Medical Oncology, Jan 2024. URL: https://doi.org/10.1177/17588359241231260, doi:10.1177/17588359241231260. This article has 64 citations and is from a peer-reviewed journal.

9. (yoo2024updateinassociation pages 2-3): Jiye Yoo, Yongchan Lee, Youngil Park, Jongin Lee, Joon Young Choi, Heekwan Lee, and Jeong Uk Lim. Update in association between lung cancer and air pollution. Tuberculosis and Respiratory Diseases, 88:228-236, Dec 2024. URL: https://doi.org/10.4046/trd.2024.0092, doi:10.4046/trd.2024.0092. This article has 10 citations.

10. (farahmandian2024investigatingtherelationship pages 1-2): Parisa Farahmandian, Abdollah Mohammadian-Hafshejani, Abdolmajid Fadaei, and Ramezan Sadeghi. Investigating the relationship between exposure to cadmium and lung cancer risk: a systematic review and meta-analysis. Journal of Health and Safety at Work, Dec 2024. URL: https://doi.org/10.18502/jhsw.v14i1.17131, doi:10.18502/jhsw.v14i1.17131. This article has 4 citations.

11. (wolf2024screeningforlung pages 7-7): Andrew M. D. Wolf, Kevin C. Oeffinger, Tina Ya‐Chen Shih, Louise C. Walter, Timothy R. Church, Elizabeth T. H. Fontham, Elena B. Elkin, Ruth D. Etzioni, Carmen E. Guerra, Rebecca B. Perkins, Karli K. Kondo, Tyler B. Kratzer, Deana Manassaram‐Baptiste, William L. Dahut, and Robert A. Smith. Screening for lung cancer: 2023 guideline update from the american cancer society. CA: A Cancer Journal for Clinicians, 74:50-81, Nov 2024. URL: https://doi.org/10.3322/caac.21811, doi:10.3322/caac.21811. This article has 425 citations and is from a domain leading peer-reviewed journal.

12. (xie2024distantmetastasispatterns pages 1-2): Tian Xie, Bing-Mei Qiu, Jing Luo, Yi-Fei Diao, Li-Wen Hu, Xiao-Long Liu, and Yi Shen. Distant metastasis patterns among lung cancer subtypes and impact of primary tumor resection on survival in metastatic lung cancer using seer database. Scientific Reports, Sep 2024. URL: https://doi.org/10.1038/s41598-024-73389-6, doi:10.1038/s41598-024-73389-6. This article has 25 citations and is from a peer-reviewed journal.

13. (xie2024distantmetastasispatterns pages 2-3): Tian Xie, Bing-Mei Qiu, Jing Luo, Yi-Fei Diao, Li-Wen Hu, Xiao-Long Liu, and Yi Shen. Distant metastasis patterns among lung cancer subtypes and impact of primary tumor resection on survival in metastatic lung cancer using seer database. Scientific Reports, Sep 2024. URL: https://doi.org/10.1038/s41598-024-73389-6, doi:10.1038/s41598-024-73389-6. This article has 25 citations and is from a peer-reviewed journal.

14. (tanaka2024femoralbonemetastasis pages 1-3): Ichidai Tanaka, Kazumi Hori, Junji Koyama, Soei Gen, Masahiro Morise, Yuta Kodama, Akira Matsui, Ayako Miyazawa, Tetsunari Hase, Yoshitaka Hibino, Toshihiko Yokoyama, Tomoki Kimura, Norio Yoshida, Mitsuo Sato, and Makoto Ishii. Femoral bone metastasis is a poor prognostic factor in egfr-tkis-treated patients with egfr-mutated non-small-cell lung cancer: a retrospective, multicenter cohort study. Therapeutic Advances in Medical Oncology, Jan 2024. URL: https://doi.org/10.1177/17588359241303090, doi:10.1177/17588359241303090. This article has 2 citations and is from a peer-reviewed journal.

15. (hektoen2024realworldevidencefor pages 3-5): Helga H. Hektoen, Kaitlyn M. Tsuruda, Lars Fjellbirkeland, Yngvar Nilssen, Odd Terje Brustugun, and Bettina K. Andreassen. Real-world evidence for pembrolizumab in non-small cell lung cancer: a nationwide cohort study. British Journal of Cancer, 132:93-102, Nov 2024. URL: https://doi.org/10.1038/s41416-024-02895-1, doi:10.1038/s41416-024-02895-1. This article has 27 citations and is from a domain leading peer-reviewed journal.

16. (brown2024sitespecificresponseand pages 11-12): Lauren Julia Brown, Julie Ahn, Bo Gao, Harriet Gee, Adnan Nagrial, Eric Hau, and Inês Pires da Silva. Site-specific response and resistance patterns in patients with advanced non-small-cell lung cancer treated with first-line systemic therapy. Cancers, 16:2136, Jun 2024. URL: https://doi.org/10.3390/cancers16112136, doi:10.3390/cancers16112136. This article has 4 citations.

17. (brown2024sitespecificresponseand pages 1-2): Lauren Julia Brown, Julie Ahn, Bo Gao, Harriet Gee, Adnan Nagrial, Eric Hau, and Inês Pires da Silva. Site-specific response and resistance patterns in patients with advanced non-small-cell lung cancer treated with first-line systemic therapy. Cancers, 16:2136, Jun 2024. URL: https://doi.org/10.3390/cancers16112136, doi:10.3390/cancers16112136. This article has 4 citations.

18. (li2024evolvingprecisionfirstline pages 1-2): Tianhong Li, Weijie Ma, and Ebaa Al-Obeidi. Evolving precision first-line systemic treatment for patients with unresectable non-small cell lung cancer. Cancers, 16:2350, Jun 2024. URL: https://doi.org/10.3390/cancers16132350, doi:10.3390/cancers16132350. This article has 14 citations.

19. (li2024evolvingprecisionfirstline pages 4-6): Tianhong Li, Weijie Ma, and Ebaa Al-Obeidi. Evolving precision first-line systemic treatment for patients with unresectable non-small cell lung cancer. Cancers, 16:2350, Jun 2024. URL: https://doi.org/10.3390/cancers16132350, doi:10.3390/cancers16132350. This article has 14 citations.

20. (cho2024amivantamabpluslazertinib pages 1-4): Byoung C. Cho, Shun Lu, Enriqueta Felip, Alexander I. Spira, Nicolas Girard, Jong-Seok Lee, Se-Hoon Lee, Yurii Ostapenko, Pongwut Danchaivijitr, Baogang Liu, Adlinda Alip, Ernesto Korbenfeld, Josiane Mourão Dias, Benjamin Besse, Ki-Hyeong Lee, Hailin Xiong, Soon-Hin How, Ying Cheng, Gee-Chen Chang, Hiroshige Yoshioka, James C.-H. Yang, Michael Thomas, Danny Nguyen, Sai-Hong I. Ou, Sanjay Mukhedkar, Kumar Prabhash, Manolo D’Arcangelo, Jorge Alatorre-Alexander, Juan C. Vázquez Limón, Sara Alves, Daniil Stroyakovskiy, Marina Peregudova, Mehmet A.N. Şendur, Ozan Yazici, Raffaele Califano, Vanesa Gutiérrez Calderón, Filippo de Marinis, Antonio Passaro, Sang-We Kim, Shirish M. Gadgeel, John Xie, Tao Sun, Melissa Martinez, Mariah Ennis, Elizabeth Fennema, Mahesh Daksh, Dawn Millington, Isabelle Leconte, Ryota Iwasawa, Patricia Lorenzini, Mahadi Baig, Sujay Shah, Joshua M. Bauml, S. Martin Shreeve, Seema Sethi, Roland E. Knoblauch, and Hidetoshi Hayashi. Amivantamab plus lazertinib in previously untreated <i>egfr</i> -mutated advanced nsclc. New England Journal of Medicine, 391:1486-1498, Oct 2024. URL: https://doi.org/10.1056/nejmoa2403614, doi:10.1056/nejmoa2403614. This article has 450 citations and is from a highest quality peer-reviewed journal.

21. (chour2024mechanismsofresistance pages 1-2): Ali Chour, Anne-Claire Toffart, Elodie Berton, and Michael Duruisseaux. Mechanisms of resistance to krasg12c inhibitors in krasg12c-mutated non-small cell lung cancer. Frontiers in Oncology, Sep 2024. URL: https://doi.org/10.3389/fonc.2024.1328728, doi:10.3389/fonc.2024.1328728. This article has 21 citations.

22. (warnecke2024adagrasibinthe pages 1-2): Brian Warnecke and Misako Nagasaka. Adagrasib in the treatment of kras p.g12c positive advanced nsclc: design, development and place in therapy. Drug Design, Development and Therapy, 18:5673-5683, Dec 2024. URL: https://doi.org/10.2147/dddt.s466217, doi:10.2147/dddt.s466217. This article has 5 citations.

23. (ferrari2024her2alterednonsmallcell pages 1-2): Giorgia Ferrari, Benedetta Del Rio, Silvia Novello, and Francesco Passiglia. Her2-altered non-small cell lung cancer: a journey from current approaches to emerging strategies. Cancers, 16:2018, May 2024. URL: https://doi.org/10.3390/cancers16112018, doi:10.3390/cancers16112018. This article has 18 citations.

24. (cho2024amivantamabpluslazertinib pages 7-8): Byoung C. Cho, Shun Lu, Enriqueta Felip, Alexander I. Spira, Nicolas Girard, Jong-Seok Lee, Se-Hoon Lee, Yurii Ostapenko, Pongwut Danchaivijitr, Baogang Liu, Adlinda Alip, Ernesto Korbenfeld, Josiane Mourão Dias, Benjamin Besse, Ki-Hyeong Lee, Hailin Xiong, Soon-Hin How, Ying Cheng, Gee-Chen Chang, Hiroshige Yoshioka, James C.-H. Yang, Michael Thomas, Danny Nguyen, Sai-Hong I. Ou, Sanjay Mukhedkar, Kumar Prabhash, Manolo D’Arcangelo, Jorge Alatorre-Alexander, Juan C. Vázquez Limón, Sara Alves, Daniil Stroyakovskiy, Marina Peregudova, Mehmet A.N. Şendur, Ozan Yazici, Raffaele Califano, Vanesa Gutiérrez Calderón, Filippo de Marinis, Antonio Passaro, Sang-We Kim, Shirish M. Gadgeel, John Xie, Tao Sun, Melissa Martinez, Mariah Ennis, Elizabeth Fennema, Mahesh Daksh, Dawn Millington, Isabelle Leconte, Ryota Iwasawa, Patricia Lorenzini, Mahadi Baig, Sujay Shah, Joshua M. Bauml, S. Martin Shreeve, Seema Sethi, Roland E. Knoblauch, and Hidetoshi Hayashi. Amivantamab plus lazertinib in previously untreated <i>egfr</i> -mutated advanced nsclc. New England Journal of Medicine, 391:1486-1498, Oct 2024. URL: https://doi.org/10.1056/nejmoa2403614, doi:10.1056/nejmoa2403614. This article has 450 citations and is from a highest quality peer-reviewed journal.

25. (uprety2024racialandsocioeconomic pages 1-2): Dipesh Uprety, Randell Seaton, Tarik Hadid, Hirva Mamdani, Ammar Sukari, Julie J Ruterbusch, and Ann G Schwartz. Racial and socioeconomic disparities in survival among patients with metastatic non–small cell lung cancer. JNCI Journal of the National Cancer Institute, 116:1697-1704, Jun 2024. URL: https://doi.org/10.1093/jnci/djae118, doi:10.1093/jnci/djae118. This article has 17 citations.

26. (li2024evolvingprecisionfirstline pages 2-4): Tianhong Li, Weijie Ma, and Ebaa Al-Obeidi. Evolving precision first-line systemic treatment for patients with unresectable non-small cell lung cancer. Cancers, 16:2350, Jun 2024. URL: https://doi.org/10.3390/cancers16132350, doi:10.3390/cancers16132350. This article has 14 citations.

27. (restrepo2024identificationandapplication pages 15-16): Juan Carlos Restrepo, Darly Martínez Guevara, Andrés Pareja López, John Fernando Montenegro Palacios, and Yamil Liscano. Identification and application of emerging biomarkers in treatment of non-small-cell lung cancer: systematic review. Cancers, 16:2338, Jun 2024. URL: https://doi.org/10.3390/cancers16132338, doi:10.3390/cancers16132338. This article has 33 citations.

28. (yang2024nonsmallcelllung pages 1-2): Mo Yang, Erin Mandal, Frank X. Liu, Richard M. O’Hara, Beth Lesher, and Rachel E. Sanborn. Non-small cell lung cancer with met amplification: review of epidemiology, associated disease characteristics, testing procedures, burden, and treatments. Frontiers in Oncology, Jan 2024. URL: https://doi.org/10.3389/fonc.2023.1241402, doi:10.3389/fonc.2023.1241402. This article has 19 citations.

29. (yang2024nonsmallcelllung pages 3-5): Mo Yang, Erin Mandal, Frank X. Liu, Richard M. O’Hara, Beth Lesher, and Rachel E. Sanborn. Non-small cell lung cancer with met amplification: review of epidemiology, associated disease characteristics, testing procedures, burden, and treatments. Frontiers in Oncology, Jan 2024. URL: https://doi.org/10.3389/fonc.2023.1241402, doi:10.3389/fonc.2023.1241402. This article has 19 citations.

30. (cho2024amivantamabpluslazertinib pages 9-11): Byoung C. Cho, Shun Lu, Enriqueta Felip, Alexander I. Spira, Nicolas Girard, Jong-Seok Lee, Se-Hoon Lee, Yurii Ostapenko, Pongwut Danchaivijitr, Baogang Liu, Adlinda Alip, Ernesto Korbenfeld, Josiane Mourão Dias, Benjamin Besse, Ki-Hyeong Lee, Hailin Xiong, Soon-Hin How, Ying Cheng, Gee-Chen Chang, Hiroshige Yoshioka, James C.-H. Yang, Michael Thomas, Danny Nguyen, Sai-Hong I. Ou, Sanjay Mukhedkar, Kumar Prabhash, Manolo D’Arcangelo, Jorge Alatorre-Alexander, Juan C. Vázquez Limón, Sara Alves, Daniil Stroyakovskiy, Marina Peregudova, Mehmet A.N. Şendur, Ozan Yazici, Raffaele Califano, Vanesa Gutiérrez Calderón, Filippo de Marinis, Antonio Passaro, Sang-We Kim, Shirish M. Gadgeel, John Xie, Tao Sun, Melissa Martinez, Mariah Ennis, Elizabeth Fennema, Mahesh Daksh, Dawn Millington, Isabelle Leconte, Ryota Iwasawa, Patricia Lorenzini, Mahadi Baig, Sujay Shah, Joshua M. Bauml, S. Martin Shreeve, Seema Sethi, Roland E. Knoblauch, and Hidetoshi Hayashi. Amivantamab plus lazertinib in previously untreated <i>egfr</i> -mutated advanced nsclc. New England Journal of Medicine, 391:1486-1498, Oct 2024. URL: https://doi.org/10.1056/nejmoa2403614, doi:10.1056/nejmoa2403614. This article has 450 citations and is from a highest quality peer-reviewed journal.

31. (cho2024amivantamabpluslazertinib media ee6afa38): Byoung C. Cho, Shun Lu, Enriqueta Felip, Alexander I. Spira, Nicolas Girard, Jong-Seok Lee, Se-Hoon Lee, Yurii Ostapenko, Pongwut Danchaivijitr, Baogang Liu, Adlinda Alip, Ernesto Korbenfeld, Josiane Mourão Dias, Benjamin Besse, Ki-Hyeong Lee, Hailin Xiong, Soon-Hin How, Ying Cheng, Gee-Chen Chang, Hiroshige Yoshioka, James C.-H. Yang, Michael Thomas, Danny Nguyen, Sai-Hong I. Ou, Sanjay Mukhedkar, Kumar Prabhash, Manolo D’Arcangelo, Jorge Alatorre-Alexander, Juan C. Vázquez Limón, Sara Alves, Daniil Stroyakovskiy, Marina Peregudova, Mehmet A.N. Şendur, Ozan Yazici, Raffaele Califano, Vanesa Gutiérrez Calderón, Filippo de Marinis, Antonio Passaro, Sang-We Kim, Shirish M. Gadgeel, John Xie, Tao Sun, Melissa Martinez, Mariah Ennis, Elizabeth Fennema, Mahesh Daksh, Dawn Millington, Isabelle Leconte, Ryota Iwasawa, Patricia Lorenzini, Mahadi Baig, Sujay Shah, Joshua M. Bauml, S. Martin Shreeve, Seema Sethi, Roland E. Knoblauch, and Hidetoshi Hayashi. Amivantamab plus lazertinib in previously untreated <i>egfr</i> -mutated advanced nsclc. New England Journal of Medicine, 391:1486-1498, Oct 2024. URL: https://doi.org/10.1056/nejmoa2403614, doi:10.1056/nejmoa2403614. This article has 450 citations and is from a highest quality peer-reviewed journal.

32. (warnecke2024adagrasibinthe pages 4-5): Brian Warnecke and Misako Nagasaka. Adagrasib in the treatment of kras p.g12c positive advanced nsclc: design, development and place in therapy. Drug Design, Development and Therapy, 18:5673-5683, Dec 2024. URL: https://doi.org/10.2147/dddt.s466217, doi:10.2147/dddt.s466217. This article has 5 citations.

33. (lazaratos2024apotentialcentral pages 1-2): Anna-Maria Lazaratos, David J. H. Bian, Kevin Petrecca, Marie-Christine Guiot, and Matthew Dankner. A potential central nervous system niche for trastuzumab deruxtecan in patients with her2-expressing non-small cell lung cancer. Translational Lung Cancer Research, 13:3824-3830, Dec 2024. URL: https://doi.org/10.21037/tlcr-24-856, doi:10.21037/tlcr-24-856. This article has 0 citations and is from a peer-reviewed journal.

34. (wang2024addressingtheunmet pages 3-5): Kinsley Wang, Alexis Leyba, and Robert Hsu. Addressing the unmet need in nsclc progression with advances in second-line therapeutics. Exploration of Targeted Anti-tumor Therapy, 5:1297-1320, Nov 2024. URL: https://doi.org/10.37349/etat.2024.00277, doi:10.37349/etat.2024.00277. This article has 4 citations.

35. (lazaratos2024apotentialcentral pages 2-4): Anna-Maria Lazaratos, David J. H. Bian, Kevin Petrecca, Marie-Christine Guiot, and Matthew Dankner. A potential central nervous system niche for trastuzumab deruxtecan in patients with her2-expressing non-small cell lung cancer. Translational Lung Cancer Research, 13:3824-3830, Dec 2024. URL: https://doi.org/10.21037/tlcr-24-856, doi:10.21037/tlcr-24-856. This article has 0 citations and is from a peer-reviewed journal.

36. (wolf2024screeningforlung pages 2-3): Andrew M. D. Wolf, Kevin C. Oeffinger, Tina Ya‐Chen Shih, Louise C. Walter, Timothy R. Church, Elizabeth T. H. Fontham, Elena B. Elkin, Ruth D. Etzioni, Carmen E. Guerra, Rebecca B. Perkins, Karli K. Kondo, Tyler B. Kratzer, Deana Manassaram‐Baptiste, William L. Dahut, and Robert A. Smith. Screening for lung cancer: 2023 guideline update from the american cancer society. CA: A Cancer Journal for Clinicians, 74:50-81, Nov 2024. URL: https://doi.org/10.3322/caac.21811, doi:10.3322/caac.21811. This article has 425 citations and is from a domain leading peer-reviewed journal.

37. (wolf2024screeningforlung pages 1-2): Andrew M. D. Wolf, Kevin C. Oeffinger, Tina Ya‐Chen Shih, Louise C. Walter, Timothy R. Church, Elizabeth T. H. Fontham, Elena B. Elkin, Ruth D. Etzioni, Carmen E. Guerra, Rebecca B. Perkins, Karli K. Kondo, Tyler B. Kratzer, Deana Manassaram‐Baptiste, William L. Dahut, and Robert A. Smith. Screening for lung cancer: 2023 guideline update from the american cancer society. CA: A Cancer Journal for Clinicians, 74:50-81, Nov 2024. URL: https://doi.org/10.3322/caac.21811, doi:10.3322/caac.21811. This article has 425 citations and is from a domain leading peer-reviewed journal.

38. (wang2024utilityofpatientderived pages 1-2): Xiaoqing Wang, Ju Zhu, Lingling Li, Qilin Zhao, Yutang Huang, Chunjie Wen, Dan Chen, and Lanxiang Wu. Utility of patient-derived xenografts to evaluate drug sensitivity and select optimal treatments for individual non-small-cell lung cancer patients. Molecular Medicine, Nov 2024. URL: https://doi.org/10.1186/s10020-024-00934-4, doi:10.1186/s10020-024-00934-4. This article has 6 citations and is from a peer-reviewed journal.

39. (hynds2024representationofgenomic pages 1-2): R. Hynds, A. Huebner, D. Pearce, M. Hill, A. Akarca, David A Moore, S. Ward, K. Gowers, Takahiro Karasaki, M. Al Bakir, G. Wilson, O. Pich, Carlos Martínez-Ruiz, A. M. Hossain, S. Pearce, Monica Sivakumar, Assma Ben Aissa, E. Grönroos, Deepak P Chandrasekharan, K. Kolluri, Rebecca Towns, Kaiwen Wang, Daniel E. Cook, Leticia Bosshard-Carter, C. Naceur-Lombardelli, Andrew Rowan, S. Veeriah, K. Litchfield, Philip A J Crosbie, C. Dive, Sergio A Quezada, S. Janes, M. Jamal-Hanjani, T. Marafioti, Maise Jason F. Amrita Apostolos Azmina Mohamad Molly Reb Al Bakir Lester Bajaj Nakas Sodha-Ramdeen Tufail S, Jason Lester, A. Bajaj, A. Nakas, Azmina Sodha-Ramdeen, M. Tufail, M. Scotland, R. Boyles, S. Rathinam, C. Wilson, Domenic Marrone, S. Dulloo, D. Fennell, Gurdeep Matharu, J. Shaw, E. Boleti, Heather Cheyne, Mohammed Khalil, S. Richardson, Tracey Cruickshank, Gillian Price, K. M. Kerr, Sarah Benafif, Jack French, Kayleigh Gilbert, B. Naidu, Akshay J. Patel, A. Osman, Carol Enstone, G. Langman, Helen Shackleford, M. Djearaman, S. Kadiri, Gary Middleton, Angela E. Leek, Jack Davies Hodgkinson, Nicola Totton, A. Montero, E. Smith, E. Fontaine, F. Granato, A. Paiva-Correia, Juliette Novasio, K. Rammohan, L. Joseph, P. Bishop, Rajesh Shah, Stuart Moss, Vijay Joshi, Katherine D. Brown, M. Carter, A. Chaturvedi, Pedro Oliveira, C. Lindsay, Fiona H. Blackhall, Matthew G. Krebs, Yvonne Summers, A. Clipson, J. Tugwood, Alastair Kerr, D. Rothwell, H. Aerts, R. Schwarz, Tom L. Kaufmann, R. Rosenthal, P. Van Loo, Nicolai J. Birkbak, Zoltan Szallasi, Judit Kisistók, M. Sokač, R. Salgado, M. Dióssy, J. Demeulemeester, Abigail Bunkum, Angela Dwornik, Alastair Magness, A. Frankell, Angeliki Karamani, A. Toncheva, B. Chain, C. Castignani, Chris Bailey, C. Abbosh, C. Puttick, C. Weeden, Claudia Lee, Corentin Richard, C. Hiley, D. Karagianni, D. Biswas, D. Levi, E. L. Cadieux, Emilia L. Lim, Emma C Colliver, E. Nye, F. Gálvez-Cancino, F. Gimeno-Valiente, G. Kassiotis, Georgia Stavrou, Gerasimos Mastrokalos, H. Lowe, Ignacio Matos, I. Noorani, J. Goldman, J. Reading, James R. M. Black, J. Rane, J. Nicod, John A. Hartley, K. Peggs, Katey S. S. Enfield, Kayalvizhi Selvaraju, K. Thol, Kevin Ng, Kezhong Chen, K. Dijkstra, Kristiana Grigoriadis, Krupa Thakkar, L. Ensell, Mansi Shah, Maria Litovchenko, M. W. Sunderland, M. Huska, M. Dietzen, Michelle M Leung, M. Escudero, Mihaela Angelova, M. Tanić, N. Kanu, O. Chervova, Olivia Lucas, Othman Al-Sawaf, Paulina Prymas, Philip S Hobson, Piotr Pawlik, R. Stone, R. Bentham, R. Vendramin, S. Saghafinia, Samuel Gamble, S. Ung, Sharon P. Vanloo, S. Zaccaria, S. Hessey, Sian Harries, S. Boeing, Stephan Beck, S. Bola, Tamara Denner, T. Watkins, Thomas P. Jones, V. Spanswick, Vittorio Barbè, Wei-Ting Lu, William Hill, W. K. Liu, Yin Wu, Yutaka Naito, Zoe Ramsden, C. Veiga, G. Royle, C. Collins-Fekete, Francesco Fraioli, Paul Ashford, Martin D. Forster, Siow-Ming Lee, E. Borg, M. Falzon, D. Papadatos-Pastos, James Wilson, T. Ahmad, A. Procter, Asia Ahmed, Magali N. Taylor, Arjun Nair, David S. Lawrence, D. Patrini, Neal Navani, R. Thakrar, E. Hoogenboom, Fleur Monk, James W. Holding, Junaid Choudhary, Kunal Bhakhri, M. Scarci, Pat Gorman, Reena Khiroya, Robert C. M. Stephens, Y. Wong, Zoltán Káplár, S. Bandula, A. Hackshaw, A. Hacker, A. Sharp, Sean Smith, H. Dhanda, Camilla Pilotti, R. Leslie, Anca-Ioana Grapa, Hanyun Zhang, K. AbdulJabbar, Xiaoxi Pan, Yinyin Yuan, David Chuter, M. Mackenzie, S. Chee, A. Alzetani, Judith Cave, J. Richards, Eric Lim, Paulo De Sousa, S. Jordan, A. Rice, H. Raubenheimer, H. Bhayani, L. Ambrose, A. Devaraj, Hema Chavan, S. Begum, Silviu I. Buderi, Daniel Kaniu, Mpho Malima, S. Booth, Andrew G. Nicholson, Nádia Fernandes, Pratibha Shah, C. Proli, M. Hewish, S. Danson, M. Shackcloth, Lily Robinson, P. Russell, Kevin G. Blyth, A. Kidd, C. Dick, J. Le Quesne, Alan Kirk, Mohd. Asif, Rocco Bilancia, N. Kostoulas, Mathew Thomas, N. Mcgranahan, and C. Swanton. Representation of genomic intratumor heterogeneity in multi-region non-small cell lung cancer patient-derived xenograft models. Nature Communications, May 2024. URL: https://doi.org/10.1038/s41467-024-47547-3, doi:10.1038/s41467-024-47547-3. This article has 24 citations and is from a highest quality peer-reviewed journal.

40. (lee2024predictionoftki pages 1-2): Sang-Hyun Lee, Kyuhwan Kim, Eunyoung Lee, Kyungmin Lee, Kyeong Hwan Ahn, Hansom Park, Yelim Kim, Soeun Shin, Sang Youl Jeon, Yongki Hwang, Dong Hyuck Ahn, Yong-Jun Kwon, Seok Whan Moon, Mi Hyoung Moon, Kyung Soo Kim, Kwanyong Hyun, Tae-Jung Kim, Yeoun Eun Sung, Joon Young Choi, Chan Kwon Park, Sung Won Kim, Chang Dong Yeo, Hyun-Jung Sohn, You-Seok Hyun, Tai-Gyu Kim, Bosung Ku, Jeong Uk Lim, and Seung Joon Kim. Prediction of tki response in egfr-mutant lung cancer patients-derived organoids using malignant pleural effusion. NPJ Precision Oncology, May 2024. URL: https://doi.org/10.1038/s41698-024-00609-7, doi:10.1038/s41698-024-00609-7. This article has 19 citations and is from a peer-reviewed journal.

41. (liu2024modelinglungadenocarcinoma pages 1-4): Yuan Liu, Manendra Lankadasari, Joel Rosiene, Kofi E. Johnson, Juan Zhou, Samhita Bapat, Lai-Fong L. Chow-Tsang, Huasong Tian, Brooke Mastrogiacomo, Di He, James G. Connolly, Harry B. Lengel, Raul Caso, Elizabeth G. Dunne, Cameron N. Fick, Gaetano Rocco, Smita Sihag, James M. Isbell, Mathew J. Bott, Bob T. Li, Piro Lito, Cameron W. Brennan, Mark H. Bilsky, Natasha Rekhtman, Prasad S. Adusumilli, Marty W. Mayo, Marcin Imielinski, and David R. Jones. Modeling lung adenocarcinoma metastases using patient-derived organoids. Cell Reports Medicine, 5:101777, Oct 2024. URL: https://doi.org/10.1016/j.xcrm.2024.101777, doi:10.1016/j.xcrm.2024.101777. This article has 25 citations and is from a peer-reviewed journal.

42. (yang2024disparitiesinutilization pages 2-3): Danting Yang, Shama D. Karanth, Hyung-Suk Yoon, Jae Jeong Yang, Xiwei Lou, Jiang Bian, Dongyu Zhang, Yi Guo, Lusine Yaghjyan, Tomi Akinyemiju, Estelamari Rodriguez, Hiren J. Mehta, and Dejana Braithwaite. Disparities in utilization of immune checkpoint inhibitor therapy among older patients with advanced non–small cell lung cancer: a seer-medicare analysis. JCO Oncology Advances, Dec 2024. URL: https://doi.org/10.1200/oa.24.00008, doi:10.1200/oa.24.00008. This article has 6 citations.

43. (cho2024amivantamabpluslazertinib pages 11-12): Byoung C. Cho, Shun Lu, Enriqueta Felip, Alexander I. Spira, Nicolas Girard, Jong-Seok Lee, Se-Hoon Lee, Yurii Ostapenko, Pongwut Danchaivijitr, Baogang Liu, Adlinda Alip, Ernesto Korbenfeld, Josiane Mourão Dias, Benjamin Besse, Ki-Hyeong Lee, Hailin Xiong, Soon-Hin How, Ying Cheng, Gee-Chen Chang, Hiroshige Yoshioka, James C.-H. Yang, Michael Thomas, Danny Nguyen, Sai-Hong I. Ou, Sanjay Mukhedkar, Kumar Prabhash, Manolo D’Arcangelo, Jorge Alatorre-Alexander, Juan C. Vázquez Limón, Sara Alves, Daniil Stroyakovskiy, Marina Peregudova, Mehmet A.N. Şendur, Ozan Yazici, Raffaele Califano, Vanesa Gutiérrez Calderón, Filippo de Marinis, Antonio Passaro, Sang-We Kim, Shirish M. Gadgeel, John Xie, Tao Sun, Melissa Martinez, Mariah Ennis, Elizabeth Fennema, Mahesh Daksh, Dawn Millington, Isabelle Leconte, Ryota Iwasawa, Patricia Lorenzini, Mahadi Baig, Sujay Shah, Joshua M. Bauml, S. Martin Shreeve, Seema Sethi, Roland E. Knoblauch, and Hidetoshi Hayashi. Amivantamab plus lazertinib in previously untreated <i>egfr</i> -mutated advanced nsclc. New England Journal of Medicine, 391:1486-1498, Oct 2024. URL: https://doi.org/10.1056/nejmoa2403614, doi:10.1056/nejmoa2403614. This article has 450 citations and is from a highest quality peer-reviewed journal.

44. (hektoen2024realworldevidencefor pages 7-8): Helga H. Hektoen, Kaitlyn M. Tsuruda, Lars Fjellbirkeland, Yngvar Nilssen, Odd Terje Brustugun, and Bettina K. Andreassen. Real-world evidence for pembrolizumab in non-small cell lung cancer: a nationwide cohort study. British Journal of Cancer, 132:93-102, Nov 2024. URL: https://doi.org/10.1038/s41416-024-02895-1, doi:10.1038/s41416-024-02895-1. This article has 27 citations and is from a domain leading peer-reviewed journal.

45. (uprety2024racialandsocioeconomic pages 2-3): Dipesh Uprety, Randell Seaton, Tarik Hadid, Hirva Mamdani, Ammar Sukari, Julie J Ruterbusch, and Ann G Schwartz. Racial and socioeconomic disparities in survival among patients with metastatic non–small cell lung cancer. JNCI Journal of the National Cancer Institute, 116:1697-1704, Jun 2024. URL: https://doi.org/10.1093/jnci/djae118, doi:10.1093/jnci/djae118. This article has 17 citations.

46. (dang2024efficacyandtoxicity pages 1-2): Shoutao Dang, Shuyang Zhang, Jingyang Zhao, and Wei Li. Efficacy and toxicity of krasg12c inhibitors in advanced solid tumors: a meta-analysis. World Journal of Surgical Oncology, Jul 2024. URL: https://doi.org/10.1186/s12957-024-03449-8, doi:10.1186/s12957-024-03449-8. This article has 7 citations and is from a peer-reviewed journal.

47. (li2024shra1811(antibodydrugconjugate) pages 1-2): Ziming Li, Zhengbo Song, Wei Hong, N. Yang, Yongsheng Wang, H. Jian, Zibin Liang, Shengxiang Hu, Min Peng, Yan Yu, Yan Wang, Zicong Jiao, Kaijing Zhao, Ke Song, You Li, Wei Shi, and Shun Lu. Shr-a1811 (antibody-drug conjugate) in advanced her2-mutant non-small cell lung cancer: a multicenter, open-label, phase 1/2 study. Signal Transduction and Targeted Therapy, Jul 2024. URL: https://doi.org/10.1038/s41392-024-01897-y, doi:10.1038/s41392-024-01897-y. This article has 38 citations and is from a peer-reviewed journal.
