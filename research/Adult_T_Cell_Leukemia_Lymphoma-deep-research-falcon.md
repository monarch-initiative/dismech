---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-08T07:51:29.488570'
end_time: '2026-05-08T08:22:10.434085'
duration_seconds: 1840.95
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Adult T-Cell Leukemia/Lymphoma
  mondo_id: ''
  category: ''
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
- **Disease Name:** Adult T-Cell Leukemia/Lymphoma
- **MONDO ID:**  (if available)
- **Category:**

## Research Objectives

Please provide a comprehensive research report on **Adult T-Cell Leukemia/Lymphoma** covering all of the
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
- **Disease Name:** Adult T-Cell Leukemia/Lymphoma
- **MONDO ID:**  (if available)
- **Category:**

## Research Objectives

Please provide a comprehensive research report on **Adult T-Cell Leukemia/Lymphoma** covering all of the
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


# Adult T-Cell Leukemia/Lymphoma (ATLL/ATL) — Disease Characteristics Research Report

## Target Disease
- **Disease name:** Adult T-cell leukemia/lymphoma (ATL/ATLL) (nosaka2025jshpracticalguidelines pages 1-3, tsukasaki2020diagnosticapproachesand pages 1-2)
- **MONDO ID:** Not retrieved in this run
- **Category:** Mature T-cell neoplasm / peripheral T-cell lymphoma-leukemia, HTLV-1–associated (nosaka2025jshpracticalguidelines pages 1-3, tsukasaki2020diagnosticapproachesand pages 1-2)

## 1. Disease Information

### 1.1 Concise overview
Adult T-cell leukemia/lymphoma (ATLL; also written ATL) is a distinct mature/peripheral T-cell malignancy etiologically caused by human T-cell leukemia/lymphotropic virus type 1 (HTLV-1) (nosaka2025jshpracticalguidelines pages 1-3, tsukasaki2020diagnosticapproachesand pages 1-2). It typically develops after a long latency (≈20–30 years) in a minority of HTLV-1 carriers and is characterized by aggressive clinical behavior in acute and lymphoma subtypes, with frequent immunosuppression and opportunistic infections (altieri2025htlv1andatll pages 7-9).

Abstract quote (etiology/risk): “Human T-cell leukemia virus type-1 (HTLV-1) causes adult T-cell leukemia/lymphoma (ATL). … 5–10% of carriers lose this balance and develop ATL.” (Nakahata et al., Biomolecules, 2023-10; (nakahata2023understandingtheimmunopathology pages 1-2)).

### 1.2 Key identifiers and synonyms
Key naming and identifier fields available from retrieved evidence are summarized here:

| Field | Value | Evidence / notes | ICD-10 | ICD-11 | MeSH | MONDO | Orphanet | OMIM |
|---|---|---|---|---|---|---|---|---|
| Preferred disease name | Adult T-cell leukemia/lymphoma | Distinct mature/peripheral T-cell malignancy caused by HTLV-1; often abbreviated ATL or ATLL (tsukasaki2020diagnosticapproachesand pages 1-2, nosaka2025jshpracticalguidelines pages 1-3) | Not retrieved in this run | Not retrieved in this run | Not retrieved in this run | Not retrieved in this run | Not retrieved in this run | Not retrieved in this run |
| Concise disease overview | Aggressive mature T-cell neoplasm arising after long-latency HTLV-1 infection, with leukemic and/or lymphomatous presentations | Reviews/guidelines describe ATL as HTLV-1-caused, typically after decades of latency; median survival for aggressive disease remains poor (altieri2025htlv1andatll pages 7-9, nakahata2023understandingtheimmunopathology pages 1-2) | Not retrieved in this run | Not retrieved in this run | Not retrieved in this run | Not retrieved in this run | Not retrieved in this run | Not retrieved in this run |
| Common abbreviations | ATL; ATLL | Both forms are used in recent literature and guidelines (nosaka2025jshpracticalguidelines pages 1-3, tsukasaki2020diagnosticapproachesand pages 1-2) | Not retrieved in this run | Not retrieved in this run | Not retrieved in this run | Not retrieved in this run | Not retrieved in this run | Not retrieved in this run |
| Key synonyms / alternative names | Adult T-cell leukaemia-lymphoma; Adult T-cell leukemia-lymphoma; HTLV-1-associated adult T-cell leukemia/lymphoma | British and American spellings both appear; disease is frequently described as HTLV-1-associated ATL/ATLL (o’donnell2023integratedmolecularand pages 3-4, tsukasaki2020diagnosticapproachesand pages 1-2) | Not retrieved in this run | Not retrieved in this run | Not retrieved in this run | Not retrieved in this run | Not retrieved in this run | Not retrieved in this run |
| Causative agent | Human T-cell leukemia/lymphotropic virus type 1 (HTLV-1) | Causal viral etiology is consistently stated across guideline and reviews (nosaka2025jshpracticalguidelines pages 1-3, tsukasaki2020diagnosticapproachesand pages 1-2, nakahata2023understandingtheimmunopathology pages 1-2) | Not retrieved in this run | Not retrieved in this run | Not retrieved in this run | Not retrieved in this run | Not retrieved in this run | Not retrieved in this run |
| Typical target cell / lineage | Mature CD4+ T-cell neoplasm; commonly CD3+, CD4+, CD25+, often CCR4+ | Immunophenotypic description from overview/review sources (altieri2025htlv1andatll pages 7-9, tsukasaki2020diagnosticapproachesand pages 1-2) | Not retrieved in this run | Not retrieved in this run | Not retrieved in this run | Not retrieved in this run | Not retrieved in this run | Not retrieved in this run |
| Canonical clinical classification | Four Shimoyama subtypes: acute, lymphoma, chronic, smoldering | Current guideline retains Shimoyama clinical subtyping; acute/lymphoma and unfavorable chronic are aggressive, favorable chronic and smoldering are indolent (nosaka2025jshpracticalguidelines pages 1-3, altieri2025htlv1andatll pages 7-9, nosaka2025jshpracticalguidelines media 8f3eac9b) | Not retrieved in this run | Not retrieved in this run | Not retrieved in this run | Not retrieved in this run | Not retrieved in this run | Not retrieved in this run |
| Aggressive vs indolent grouping | Aggressive: acute, lymphoma, chronic with unfavorable factors; Indolent: chronic without unfavorable factors, smoldering | Unfavorable chronic defined by abnormal BUN, LDH, or low albumin in guideline summary (nosaka2025jshpracticalguidelines pages 1-3) | Not retrieved in this run | Not retrieved in this run | Not retrieved in this run | Not retrieved in this run | Not retrieved in this run | Not retrieved in this run |
| Latency / temporal development | Usually develops after long latency, about 20-30 years after HTLV-1 infection; many carriers remain asymptomatic for decades | Long latency emphasized in recent reviews; only a minority of carriers progress to ATL/ATLL (altieri2025htlv1andatll pages 7-9, o’donnell2023integratedmolecularand pages 3-4, nakahata2023understandingtheimmunopathology pages 1-2) | Not retrieved in this run | Not retrieved in this run | Not retrieved in this run | Not retrieved in this run | Not retrieved in this run | Not retrieved in this run |
| Mode of knowledge represented here | Aggregated disease-level literature and guidelines, not individual-patient EHR data | Information in this summary comes from reviews, consensus/guideline documents, and cohort studies (nosaka2025jshpracticalguidelines pages 1-3, tsukasaki2020diagnosticapproachesand pages 1-2, iordan2024clinicalfeaturesand pages 1-2) | Not retrieved in this run | Not retrieved in this run | Not retrieved in this run | Not retrieved in this run | Not retrieved in this run | Not retrieved in this run |


*Table: This table summarizes the core disease naming, etiology, subtype classification, and latency concepts for adult T-cell leukemia/lymphoma. Identifier fields are included for ontology/database curation and marked as not retrieved where this evidence run did not supply them.*

**Note:** ICD-10/ICD-11/MeSH/MONDO/Orphanet/OMIM codes were not directly retrieved from the full text evidence in this tool run; they should be added via targeted ontology/registry queries.

### 1.3 Evidence sources represented in this report
This report is derived from aggregated disease-level resources: reviews, guidelines/consensus documents, clinical trials, and cohort studies (nosaka2025jshpracticalguidelines pages 1-3, tsukasaki2020diagnosticapproachesand pages 1-2, iordan2024clinicalfeaturesand pages 1-2). It does not include individual EHR-derived patient records.

## 2. Etiology

### 2.1 Primary causes
ATLL is causally linked to HTLV-1 infection, a deltaretrovirus that persists via proviral integration and clonal expansion of infected T cells (nosaka2025jshpracticalguidelines pages 1-3, o’donnell2023integratedmolecularand pages 2-3). Viral proteins Tax and HBZ contribute to oncogenesis and immune dysregulation (o’donnell2023integratedmolecularand pages 3-4, nakahata2023understandingtheimmunopathology pages 1-2).

### 2.2 Risk factors
**Infectious exposure and transmission routes:** Major transmission routes include mother-to-child via breastfeeding, sexual contact, and exposure to infected blood products/transfusion (tsukasaki2020diagnosticapproachesand pages 1-2, branda2025humantlymphotropicvirus pages 10-12).

**High proviral load:** In a 2023 Lancet Haematology review, higher baseline proviral load strongly predicted ATLL risk; proviral load “>4 copies per 100 PBMCs” was associated with **HR 3.57** (95% CI 2.25–5.68) for developing ATLL (o’donnell2023integratedmolecularand pages 3-4).

**Coinfection/host immune state:** Strongyloides coinfection is cited as promoting ATLL development, consistent with the concept that immune status influences progression (nakahata2023understandingtheimmunopathology pages 1-2).

### 2.3 Protective factors
Evidence in this run supports breastfeeding modification as protective against HTLV-1 transmission (see Prevention). Specific genetic protective variants were not retrieved as explicit “protective variants” in the excerpts, although host HLA influences transmission risk and immune control (o’donnell2023integratedmolecularand pages 2-3).

### 2.4 Gene–environment interactions
Host genetics (e.g., HLA concordance between mother and infant) influences HTLV-1 transmission risk, modifying how an environmental exposure (breastfeeding) translates into infection (o’donnell2023integratedmolecularand pages 2-3).

## 3. Phenotypes

### 3.1 Clinical subtypes and defining features (Shimoyama)
ATLL is classically divided into **acute, lymphoma, chronic, and smoldering** subtypes (nosaka2025jshpracticalguidelines pages 1-3, nosaka2025jshpracticalguidelines media 8f3eac9b). A 2023 Lancet Haematology review provides quantitative subtype proportions: smouldering (5–10%), chronic (10–20%), lymphoma (20–25%), with acute accounting for the remainder (o’donnell2023integratedmolecularand pages 5-6).

Smouldering ATL is defined by specific blood and laboratory thresholds: “presence of abnormal T cells with flower cell morphology in peripheral blood (≥5%)”, normal lymphocyte count (≤4×10^9/L), “no hypercalcaemia (corrected calcium concentration <2·74 mmol/L)”, and only mild LDH elevation (o’donnell2023integratedmolecularand pages 5-6).

### 3.2 Common symptoms/signs and lab abnormalities
Across guidelines and reviews, common features include:
- **Leukocytosis** with abnormal “**flower cells**” (nosaka2025jshpracticalguidelines pages 1-3)
- **Lymphadenopathy**, **hepatosplenomegaly**, **skin rash/skin lesions** (nosaka2025jshpracticalguidelines pages 1-3, altieri2025htlv1andatll pages 7-9)
- **Elevated LDH**, **hypercalcemia** (nosaka2025jshpracticalguidelines pages 1-3, tsukasaki2020diagnosticapproachesand pages 1-2)
- **Opportunistic infections** (e.g., Pneumocystis, aspergillosis, candidiasis, CMV; also Strongyloides) (altieri2025htlv1andatll pages 7-9, nosaka2025jshpracticalguidelines pages 1-3)

Real-world complications documented in a 2024 Romanian cohort included cytopenias and infections in all patients; pathogens included Candida albicans, C. difficile, bacterial infections, herpes zoster, SARS-CoV-2, CMV reactivation, and BK virus; symptomatic hypercalcemia was common (iordan2024clinicalfeaturesand pages 5-6).

### 3.3 Suggested HPO terms (examples)
(These are ontology suggestions; IDs should be verified against HPO.)
- Hypercalcemia (HP:0003072) (nosaka2025jshpracticalguidelines pages 1-3, tsukasaki2020diagnosticapproachesand pages 1-2)
- Lymphadenopathy (HP:0002716) (nosaka2025jshpracticalguidelines pages 1-3)
- Hepatosplenomegaly (HP:0001433 / HP:0001744) (nosaka2025jshpracticalguidelines pages 1-3)
- Skin rash / Cutaneous lesion (HP:0000988 / HP:0000951) (nosaka2025jshpracticalguidelines pages 1-3)
- Elevated lactate dehydrogenase (HP:0003236) (nosaka2025jshpracticalguidelines pages 1-3)
- Opportunistic infection (HP:0002719) (altieri2025htlv1andatll pages 7-9, nosaka2025jshpracticalguidelines pages 1-3)
- Leukocytosis (HP:0001974) (nosaka2025jshpracticalguidelines pages 1-3)

### 3.4 Quality-of-life impact
Direct QoL instrument data (EQ-5D/SF-36/PROMIS) were not retrieved in this run; however, severe systemic symptoms, infections, and hypercalcemia complications in aggressive ATLL imply major functional and hospitalization burden (iordan2024clinicalfeaturesand pages 5-6).

## 4. Genetic/Molecular Information

### 4.1 Viral oncogenes and host alterations (core concepts)
Two viral gene products are repeatedly emphasized:
- **Tax:** transiently expressed, highly immunogenic, drives proliferation/anti-apoptotic pathways and host gene dysregulation (o’donnell2023integratedmolecularand pages 3-4, nakahata2023understandingtheimmunopathology pages 1-2).
- **HBZ:** persistently expressed antisense product with low immunogenicity; promotes clonal proliferation and immune evasion (o’donnell2023integratedmolecularand pages 3-4, o’donnell2023integratedmolecularand pages 2-3).

Abstract quote (Tax oncogenesis): “HTLV-1 encodes the viral transcription transactivator, Tax, in the pX region of its genome, which promotes oncogenesis.” (Nakahata et al., Biomolecules, 2023-10; (nakahata2023understandingtheimmunopathology pages 1-2)).

### 4.2 Somatic genomic/epigenetic alterations (host)
From a 2023 immunopathology review:
- “~90% of ATL cases have activating **TCR–NF-κB pathway mutations**” (nakahata2023understandingtheimmunopathology pages 3-5).
- “~40% show CpG island hypermethylation (CIMP)” (nakahata2023understandingtheimmunopathology pages 3-5).
- **HLA class I mutations/deletions** and **PD-L1 3′-UTR structural alterations** that increase PD-L1 mRNA are enriched in ATL (nakahata2023understandingtheimmunopathology pages 3-5).

Single-cell features described include upregulation of immunosuppressive molecules (PD-L1, CD73, CD39) and activation markers (CD71, CD25, CD38) (nakahata2023understandingtheimmunopathology pages 3-5).

### 4.3 Suggested gene/protein targets for annotation
- **CCR4** (target of mogamulizumab) (ishida2017mogamulizumabforrelapsed pages 1-2)
- **PD-L1 (CD274)** structural alterations and overexpression (nakahata2023understandingtheimmunopathology pages 3-5)
- **FOXP3** (Treg phenotype association) (nakahata2023understandingtheimmunopathology pages 3-5)

### 4.4 Suggested GO biological process terms (examples)
(IDs should be verified against GO.)
- NF-κB signaling (nakahata2023understandingtheimmunopathology pages 3-5, o’donnell2023integratedmolecularand pages 3-4)
- Regulation of T-cell activation / TCR signaling (nakahata2023understandingtheimmunopathology pages 3-5)
- Immune evasion / negative regulation of immune response (nakahata2023understandingtheimmunopathology pages 3-5, o’donnell2023integratedmolecularand pages 3-4)
- DNA methylation / epigenetic gene regulation (nakahata2023understandingtheimmunopathology pages 3-5)

### 4.5 Suggested CL (Cell Ontology) terms
- CD4-positive, alpha-beta T cell (ATL cell of origin/target) (o’donnell2023integratedmolecularand pages 2-3)
- Regulatory T cell (Treg-like phenotype; FOXP3-associated) (nakahata2023understandingtheimmunopathology pages 3-5, o’donnell2023integratedmolecularand pages 3-4)
- Cytotoxic CD8-positive T cell (Tax-specific CTLs in immune control) (o’donnell2023integratedmolecularand pages 3-4)

## 5. Environmental Information

### 5.1 Infectious agent
HTLV-1 is the infectious agent underlying ATLL (nosaka2025jshpracticalguidelines pages 1-3, tsukasaki2020diagnosticapproachesand pages 1-2).

### 5.2 Lifestyle/environmental exposures
In this run, the key non-genetic exposures relate to transmission opportunities: breastfeeding, sexual exposure, contaminated blood/organ products, and injection-related exposures (altieri2025htlv1andatll pages 12-14, tsukasaki2020diagnosticapproachesand pages 1-2).

## 6. Mechanism / Pathophysiology

### 6.1 Causal chain (high-level)
1) **HTLV-1 acquisition** (breastfeeding/sexual/blood) → 2) **proviral integration and clonal expansion** of infected CD4+ T cells with generally quiescent transcription → 3) episodic **Tax** expression enables spread and promotes proliferative programs but drives immune recognition → 4) selection for immune escape with Tax silencing (e.g., 5′ LTR methylation/deletion) and persistence via **HBZ**-driven proliferation → 5) accumulation of **host genetic and epigenetic lesions** (e.g., TCR–NF-κB pathway mutations, CIMP, HLA/PD-L1 alterations) → 6) emergence of malignant clone with immune evasion and systemic immunodeficiency → clinical ATLL with hypercalcemia, organ infiltration, and opportunistic infections (o’donnell2023integratedmolecularand pages 3-4, nakahata2023understandingtheimmunopathology pages 3-5, nosaka2025jshpracticalguidelines pages 1-3).

### 6.2 Key mechanisms and pathways
- **Tax-driven** activation of proliferative and anti-apoptotic pathways; selection for Tax-silenced clones due to immune pressure (o’donnell2023integratedmolecularand pages 3-4, nakahata2023understandingtheimmunopathology pages 1-2).
- **HBZ-driven** clonal proliferation and immune evasion (low immunogenicity), with promotion of tolerogenic/Treg-like phenotypes (o’donnell2023integratedmolecularand pages 3-4, o’donnell2023integratedmolecularand pages 2-3).
- **TCR–NF-κB pathway** mutations in most cases (nakahata2023understandingtheimmunopathology pages 3-5).
- **Immune checkpoint and antigen presentation alterations**: PD-L1 structural alterations and HLA class I changes contribute to immune escape (nakahata2023understandingtheimmunopathology pages 3-5).

### 6.3 Molecular profiling (selected)
Single-cell transcriptomic observations include ATL cell upregulation of PD-L1, CD73, CD39, CD71, CD25, CD38, and dynamic HLA class II expression patterns during clonal expansion (nakahata2023understandingtheimmunopathology pages 3-5).

## 7. Anatomical Structures Affected

### 7.1 Organ-level involvement
- **Blood and bone marrow** (leukemic manifestations in acute/chronic) (nosaka2025jshpracticalguidelines pages 1-3, tsukasaki2020diagnosticapproachesand pages 1-2)
- **Lymph nodes** (lymphoma subtype and systemic disease) (nosaka2025jshpracticalguidelines pages 1-3)
- **Skin** (skin lesions/rash; common) (nosaka2025jshpracticalguidelines pages 1-3, tsukasaki2020diagnosticapproachesand pages 1-2)
- **Liver/spleen** (hepatosplenomegaly) (nosaka2025jshpracticalguidelines pages 1-3)
- **CNS/GI involvement** can occur, particularly noted for acute subtype (tsukasaki2020diagnosticapproachesand pages 1-2)

### 7.2 Suggested UBERON terms (examples)
(IDs should be verified against UBERON.)
- Peripheral blood; bone marrow; lymph node; skin; liver; spleen; central nervous system; gastrointestinal tract (tsukasaki2020diagnosticapproachesand pages 1-2, nosaka2025jshpracticalguidelines pages 1-3).

## 8. Temporal Development

ATLL typically develops after long latency from infection (20–30 years) (altieri2025htlv1andatll pages 7-9). Aggressive subtypes have a rapid course (months), while indolent subtypes have longer median survivals (years) (nosaka2025jshpracticalguidelines pages 1-3, o’donnell2023integratedmolecularand pages 5-6).

## 9. Inheritance and Population

### 9.1 Epidemiology and demographics
- HTLV-1 carriers: estimated **~10–20 million worldwide**; Japan ~**1.08 million** carriers (nosaka2025jshpracticalguidelines pages 1-3).
- Lifetime risk of ATLL among carriers: **~2–5%** (Japan guideline) (nosaka2025jshpracticalguidelines pages 1-3); another recent review states ATLL occurs in ~3–5% of HTLV-1 infections (altieri2025htlv1andatll pages 7-9).
- Subtype frequencies in Japan (2012–2013): acute 51.9%, lymphoma 24.9%, chronic 12.5%, smoldering 10.7% (nosaka2025jshpracticalguidelines pages 1-3).

## 10. Diagnostics

### 10.1 Diagnostic criteria and subtype classification
Table 1 from the JSH guideline provides ATL diagnostic and subtype classification criteria and can be used as the primary structured reference for smoldering/chronic/lymphoma/acute definitions in routine practice (nosaka2025jshpracticalguidelines media 8f3eac9b).

### 10.2 Laboratory and pathology tests
**HTLV-1 confirmation:** The guideline states serology positive by particle agglutination, ELISA/Western blotting, or line immunoassay; confirmatory tests are recommended (nosaka2025jshpracticalguidelines pages 1-3). Where available, “Institutions capable of performing Southern blotting should do so to confirm integration of HTLV-1 provirus into ATL cells.” (nosaka2025jshpracticalguidelines pages 1-3).

**Molecular assays:** PCR/qPCR proviral testing and clonality analysis are referenced as diagnostic approaches (branda2025humantlymphotropicvirus pages 17-17, stUnknownyearprotocolforthe pages 5-10).

**Immunophenotyping (flow cytometry):** Recommended minimal panel includes CD3, CD4, CD7, CD8, CD25; typical tumor phenotype includes CD2/CD4/CD5/CD45RO/CD29/TCR with reduced CD3 and often negative for CD7, CD8, CD26 (bazarbachi2011howitreat pages 2-3).

**Histology requirement at low blood tumor burden:** When circulating abnormal lymphocytes are <5%, histological confirmation of neoplastic lesions is required for smoldering/chronic/acute ATL diagnosis (nosaka2025jshpracticalguidelines pages 1-3).

## 11. Outcome/Prognosis

### 11.1 Survival statistics (recent guideline + recent review)
From a nationwide Japan survey (2010–2011) summarized in the JSH guideline:
- 4-year OS: acute 16.8%, lymphoma 19.6%, chronic unfavorable 26.6%, chronic favorable 62.1%, smoldering 59.8% (nosaka2025jshpracticalguidelines pages 1-3).

From a 2023 Lancet Haematology review (median OS):
- Smouldering: median OS 55 months; 4-year OS 52% (o’donnell2023integratedmolecularand pages 5-6)
- Chronic: median OS 31.5 months; 4-year OS 36% (o’donnell2023integratedmolecularand pages 5-6)

A Japanese cohort (2000–2009) reported median OS: acute 8.3 months; lymphoma 10.6 months; chronic 31.5 months; smoldering 55.0 months (munakata2018adulttcellleukemialymphoma. pages 12-14).

### 11.2 Real-world outcomes (2024)
A 2024 Romanian single-center cohort of aggressive ATLL reported median survival 6.37 months overall; lymphoma-type 8.16 months vs acute-type 3.60 months, with low response to chemotherapy (iordan2024clinicalfeaturesand pages 1-2).

## 12. Treatment

### 12.1 Established and emerging treatments (with quantitative outcomes)
A consolidated treatment evidence table from this run is provided here:

| Treatment modality | Setting | Key efficacy statistics | Safety / limitations | Publication year | URL / DOI | Evidence |
|---|---|---|---|---|---|---|
| Zidovudine + interferon-α (AZT/IFN) | Frontline, combination with chemotherapy, maintenance in selected subtypes | 2023 meta-analysis of 15 studies/1,101 patients: overall response 67% (95% CI 0.50–0.80), CR 33% (95% CI 0.24–0.44), PR 31% (95% CI 0.24–0.39); better responses when used front-line and in indolent disease; aggressive subtype pooled CR 25%, indolent pooled CR 53%; one observational analysis reported HR for death 0.23 (95% CI 0.09–0.60) in aggressive ATLL; one report cited median PFS 48 months with AZT/IFN vs 11 months after chemotherapy in CR patients | Evidence base is heterogeneous and largely non-randomized; interferon availability issues noted; some cohorts reported no significant survival difference vs chemotherapy; detailed pooled AE statistics not robustly available in retrieved evidence | 2023 | https://doi.org/10.1186/s12985-023-02077-0 | (shafiee2023zidovudineandinterferon pages 1-2, shafiee2023zidovudineandinterferon pages 4-6, shafiee2023zidovudineandinterferon pages 8-9, shafiee2023zidovudineandinterferon pages 6-7, shafiee2023zidovudineandinterferon pages 7-8) |
| Intensive multiagent chemotherapy (e.g., VCAP-AMP-VECP, modified LSG15, CHOP/CHOP-like, hyper-CVAD) | Frontline for aggressive acute/lymphoma ATL | In randomized phase II study, adding mogamulizumab to mLSG15 increased CR to 52% vs 33% with mLSG15 alone and ORR to 86% vs 75%; Romanian real-world cohort using CHOP/CHOP-like, modified LSG15, or hyper-CVAD had only 6 responses among 20 patients and median survival 6.37 months overall (8.16 months lymphoma-type, 3.60 months acute-type) | Conventional chemotherapy responses are often short; poor outcomes in aggressive disease; cytopenias/infections common in real-world practice | 2015, 2024 | https://doi.org/10.1111/bjh.13338 ; https://doi.org/10.3390/medicina60060872 | (iordan2024clinicalfeaturesand pages 1-2, iordan2024clinicalfeaturesand pages 9-10, iordan2024clinicalfeaturesand pages 2-4) |
| Mogamulizumab monotherapy | Relapsed/refractory aggressive ATL; also used prospectively in broader ATL population | Phase II relapsed aggressive ATL: median PFS 5.2 months, 1-year PFS 26%, median OS 14.4 months, 3-year OS 23%; outcomes better with rash ≥grade 2: median PFS 11.7 months, median OS 25.6 months; multicenter observational study: ORR 65%, median PFS 7.4 months, median OS 16.0 months; retrospective real-world cohort: ORR 36%, CR 17%, median PFS 1.8 months, OS 4.0 months overall, better with ≥5 courses | Rash is common and may correlate with response; fatal AEs reported; severe cutaneous reactions, HBV reactivation, infusion reactions reported; efficacy varies substantially by population and line of therapy | 2017, 2020 | https://doi.org/10.1111/cas.13343 ; https://doi.org/10.1182/bloodadvances.2020003053 ; https://doi.org/10.1111/ejh.12863 | (ishida2017mogamulizumabforrelapsed pages 1-2, sekine2017effectsofmogamulizumab pages 14-18, sekine2017effectsofmogamulizumab pages 10-14, yonekura2020mogamulizumabforadult pages 12-12) |
| Mogamulizumab + intensive chemotherapy | Frontline newly diagnosed aggressive ATL | Randomized phase II: CR 52% (95% CI 33–71) and ORR 86% with mLSG15 + mogamulizumab vs CR 33% and ORR 75% with mLSG15 alone | More grade ≥3 anemia, thrombocytopenia, lymphopenia, leukopenia, decreased appetite; CMV infection, interstitial lung disease, and skin disorders reported in combination arm | 2015 | https://doi.org/10.1111/bjh.13338 | (wang2024currentstateof pages 12-14) |
| Mogamulizumab before allogeneic HSCT | Pre-transplant exposure in transplant-eligible patients | Not a benefit row: retrieved evidence emphasizes risk rather than efficacy | Significantly increased risks of severe and steroid-refractory GVHD, non-relapse mortality, and overall mortality; 50-day washout before allo-HSCT recommended in 2024 review | 2018, 2024 | https://doi.org/10.1007/978-3-319-99716-2_7 ; https://doi.org/10.3390/v16101616 | (wang2024currentstateof pages 34-35, wang2024currentstateof pages 12-14, munakata2018adulttcellleukemialymphoma. pages 16-17) |
| Allogeneic hematopoietic stem-cell transplantation (allo-HSCT) | Consolidation/curative-intent for eligible aggressive ATL, typically early after remission/response | Considered the only modality with curative potential in recent reviews/guidelines; exact pooled survival statistics not in retrieved 2023–2024 evidence here; Romanian cohort: only 2/20 patients underwent allo-HSCT | Limited to fit/eligible patients; transplant morbidity/mortality substantial; timing complicated by prior mogamulizumab exposure | 2023, 2024, 2025 | https://doi.org/10.3390/biom13101543 ; https://doi.org/10.3390/v16101616 ; https://doi.org/10.3390/medicina60060872 ; https://doi.org/10.1007/s12185-025-04011-2 | (nakahata2023understandingtheimmunopathology pages 2-3, nosaka2025jshpracticalguidelines pages 1-3, wang2024currentstateof pages 34-35, iordan2024clinicalfeaturesand pages 1-2, wang2024currentstateof pages 12-14) |
| Lenalidomide | Relapsed/recurrent ATL; maintenance benefit discussed in review literature | Mentioned as phase II ATLL-002 and case reports of maintenance benefit; no numeric ORR/PFS/OS values available in retrieved evidence | Quantitative efficacy not in retrieved evidence; recognized as an approved/emerging option in reviews | 2024 | https://doi.org/10.3390/v16101616 | (wang2024currentstateof pages 34-35) |
| Brentuximab vedotin | Selected CD30-positive ATL; role discussed in reviews | Not in retrieved evidence for quantitative efficacy statistics | Mentioned as an approved/newer agent in review literature, but no trial outcome numbers captured in this run | 2020 | https://doi.org/10.3389/fmicb.2020.01207 | (tsukasaki2020diagnosticapproachesand pages 1-2) |
| Valemetostat / EZH1/2-directed epigenetic therapy | Relapsed/refractory ATL; investigational/early implementation | Open-label single-arm phase II and preclinical activity mentioned; no numeric ORR/PFS/OS captured in retrieved evidence | Early-phase/limited evidence in this run; quantitative outcomes not retrieved | 2024 | https://doi.org/10.3390/v16101616 | (wang2024currentstateof pages 34-35) |
| Investigational CAR-T / gene-edited cell therapy (e.g., anti-CD7 CAR-T, CD70 allogeneic CRISPR-edited CAR-T) | Relapsed/refractory T-cell malignancies including ATL in early-phase studies | Trial programs identified: anti-CD7 CAR-T (NCT05620680; single-center phase 1, n=20) and CD70-directed allogeneic CRISPR-edited CTX131 (NCT06492304); efficacy statistics not in retrieved evidence | Early-phase, small cohorts, relapsed/refractory setting; immune toxicity and translational challenges remain | 2025 | https://doi.org/10.1016/j.leukres.2025.107642 | (epsteinpeterson2025newtreatmentsfor pages 15-15) |
| CRISPR/ZFN proviral excision / RNA-based or gene-therapy strategies | Preclinical / future therapeutic modality | No clinical efficacy statistics in retrieved evidence | Delivery efficiency, off-target effects, and safety remain major challenges; promising concept rather than established therapy | 2024, 2025 | https://doi.org/10.3390/v16101616 ; https://doi.org/10.3390/v17050664 | (branda2025humantlymphotropicvirus pages 23-25, wang2024currentstateof pages 1-2) |


*Table: This table summarizes key established and emerging treatment strategies for adult T-cell leukemia/lymphoma, including clinical setting, efficacy signals, and major safety limitations. It is useful for quickly comparing frontline, relapsed, transplant, and investigational approaches using only evidence retrieved in this run.*

Key points:
- **AZT/IFN** remains a widely used antiviral/immune-modulating regimen with pooled response estimates in a 2023 meta-analysis (OR 67%, CR 33%) and signals of greater benefit in indolent disease and in frontline combination use (shafiee2023zidovudineandinterferon pages 1-2, shafiee2023zidovudineandinterferon pages 4-6).
- **Mogamulizumab (anti-CCR4)** shows clinically meaningful activity in relapsed aggressive ATL (phase II median OS 14.4 months; PFS 5.2 months) with rash as an immune-related AE correlated with improved outcomes (ishida2017mogamulizumabforrelapsed pages 1-2). Real-world results vary (e.g., ORR 36% and OS 4.0 months in one retrospective cohort) (sekine2017effectsofmogamulizumab pages 10-14).
- **Chemoimmunotherapy (mLSG15 + mogamulizumab)** improved CR rates compared with chemotherapy alone, but with higher toxicity and opportunistic infections (wang2024currentstateof pages 12-14).
- **Allo-HSCT** is emphasized as the only potentially curative approach in recent reviews and depends on eligibility and timing; pretransplant mogamulizumab exposure increases GVHD and mortality risk, motivating washout periods (wang2024currentstateof pages 34-35, wang2024currentstateof pages 12-14).

### 12.2 Suggested MAXO terms (examples)
(IDs should be verified against MAXO.)
- Antiviral therapy (AZT/IFN) (shafiee2023zidovudineandinterferon pages 1-2)
- Combination chemotherapy (iordan2024clinicalfeaturesand pages 1-2)
- Monoclonal antibody therapy (mogamulizumab) (ishida2017mogamulizumabforrelapsed pages 1-2)
- Hematopoietic stem cell transplantation (allo-HSCT) (nakahata2023understandingtheimmunopathology pages 2-3)
- CAR T-cell therapy (investigational) (epsteinpeterson2025newtreatmentsfor pages 15-15)

## 13. Prevention

ATLL prevention is largely **primary prevention of HTLV-1 acquisition**, because disease typically follows long-term infection.

**Breastfeeding modification:** Early cessation of breastfeeding reduces transmission risk “from 14% to 4%” (o’donnell2023integratedmolecularand pages 2-3). A US-focused review states refraining from breastfeeding in HTLV-1-positive mothers can prevent **87% of early-life infections**; short-term breastfeeding up to 3 months is proposed when formula is infeasible (altieri2025htlv1andatll pages 12-14).

**Blood donor screening:** Blood-donor screening is linked to a “significant reduction in transmission through blood transfusions” (branda2025humantlymphotropicvirus pages 10-12).

**Organ donor screening:** Receiving an organ from an HTLV-1-positive donor was described as having “100% risk of infection” (altieri2025htlv1andatll pages 4-5).

**Sexual and injection-related transmission prevention:** Safe-sex practices, partner testing/counseling, and harm-reduction needle exchange programs are recommended in public-health frameworks (altieri2025htlv1andatll pages 12-14).

## 14. Other Species / Natural Disease

This run retrieved animal-model discussions relevant to experimental systems (see Model Organisms) but did not retrieve evidence of naturally occurring ATLL in non-human species.

## 15. Model Organisms

A 2024 HTLV-1 therapeutics review summarizes multiple model systems:
- **Transgenic mice:** Tax transgenic mice established Tax as an oncoprotein but often developed mesenchymal tumors rather than frank ATL-like disease; HBZ transgenic expression in CD4+ T cells induced leukemia/lymphoma after a long latency, aligning with HBZ constitutive expression in ATL (wang2024currentstateof pages 9-11, wang2024currentstateof pages 8-9).
- **Xenografts / patient-derived xenografts:** NOD/SCID and NOG mice engrafted with ATL cells better recapitulate disease; the MET-1 NOD/SCID model demonstrated tumor inhibition and prolonged survival with daclizumab + depsipeptide (HDAC inhibitor) (wang2024currentstateof pages 8-9).
- **Humanized mice:** Models (e.g., huNSG formats) allow HTLV-1 infection with rising proviral load, clonal CD25+CD4+ expansion, and ATL-like pathology; limitations include incomplete recapitulation of long-term persistence and immune context (wang2024currentstateof pages 9-11).

## Limitations of this evidence run
- Formal ICD/MeSH/MONDO/Orphanet/OMIM identifiers were not retrieved from the accessed full texts.
- Several key sources are 2025 (still recent and authoritative), because some 2023 guideline documents were published later; core mechanistic sources prioritized include 2023–2024 reviews.
- Some treatment modalities (lenalidomide, brentuximab, valemetostat) are mentioned but lacked extractable trial efficacy numbers in retrieved excerpts.

## Key references (URLs/DOIs and publication dates)
- O’Donnell et al. *Lancet Haematology* (2023-07). https://doi.org/10.1016/S2352-3026(23)00087-X (o’donnell2023integratedmolecularand pages 3-4)
- Nakahata et al. *Biomolecules* (2023-10). https://doi.org/10.3390/biom13101543 (nakahata2023understandingtheimmunopathology pages 1-2)
- Wang et al. *Viruses* (2024-10). https://doi.org/10.3390/v16101616 (wang2024currentstateof pages 1-2)
- Shafiee et al. *Virology Journal* (2023-06). https://doi.org/10.1186/s12985-023-02077-0 (shafiee2023zidovudineandinterferon pages 1-2)
- Ishida et al. *Cancer Science* (2017-08). https://doi.org/10.1111/cas.13343 (ishida2017mogamulizumabforrelapsed pages 1-2)
- Iordan et al. *Medicina* (2024-05). https://doi.org/10.3390/medicina60060872 (iordan2024clinicalfeaturesand pages 1-2)
- Nosaka & Fukushima *International Journal of Hematology* (2025-06; “JSH practical guidelines 2023”). https://doi.org/10.1007/s12185-025-04011-2 (nosaka2025jshpracticalguidelines pages 1-3)


References

1. (nosaka2025jshpracticalguidelines pages 1-3): Kisato Nosaka and Takuya Fukushima. Jsh practical guidelines for hematological malignancies, 2023: ii. lymphoma 9—adult t-cell leukemia–lymphoma (atl). International Journal of Hematology, 122:177-189, Jun 2025. URL: https://doi.org/10.1007/s12185-025-04011-2, doi:10.1007/s12185-025-04011-2. This article has 3 citations and is from a peer-reviewed journal.

2. (tsukasaki2020diagnosticapproachesand pages 1-2): Kunihiro Tsukasaki, Ambroise Marçais, Rihab Nasr, Koji Kato, Takahiro Fukuda, Olivier Hermine, and Ali Bazarbachi. Diagnostic approaches and established treatments for adult t cell leukemia lymphoma. Frontiers in Microbiology, Jun 2020. URL: https://doi.org/10.3389/fmicb.2020.01207, doi:10.3389/fmicb.2020.01207. This article has 63 citations and is from a peer-reviewed journal.

3. (altieri2025htlv1andatll pages 7-9): Adrian Altieri, Sean Patrick Reilly, Abu Mansalay, Alan Soo-Beng Khoo, Nettie Johnson, Zafar K. Khan, Amy Leader, Pooja Jain, and Pierluigi Porcu. Htlv-1 and atll: epidemiology, oncogenesis, and opportunities for community-informed research in the united states. Viruses, 17:1333, Sep 2025. URL: https://doi.org/10.3390/v17101333, doi:10.3390/v17101333. This article has 6 citations.

4. (nakahata2023understandingtheimmunopathology pages 1-2): Shingo Nakahata, Daniel Enriquez-Vera, M. Ishrat Jahan, Kenji Sugata, and Yorifumi Satou. Understanding the immunopathology of htlv-1-associated adult t-cell leukemia/lymphoma: a comprehensive review. Biomolecules, 13:1543, Oct 2023. URL: https://doi.org/10.3390/biom13101543, doi:10.3390/biom13101543. This article has 35 citations.

5. (o’donnell2023integratedmolecularand pages 3-4): Jake S O’Donnell, Stewart K Hunt, and Keith J Chappell. Integrated molecular and immunological features of human t-lymphotropic virus type 1 infection and disease progression to adult t-cell leukaemia or lymphoma. The Lancet Haematology, 10:e539-e548, Jul 2023. URL: https://doi.org/10.1016/s2352-3026(23)00087-x, doi:10.1016/s2352-3026(23)00087-x. This article has 23 citations and is from a highest quality peer-reviewed journal.

6. (nosaka2025jshpracticalguidelines media 8f3eac9b): Kisato Nosaka and Takuya Fukushima. Jsh practical guidelines for hematological malignancies, 2023: ii. lymphoma 9—adult t-cell leukemia–lymphoma (atl). International Journal of Hematology, 122:177-189, Jun 2025. URL: https://doi.org/10.1007/s12185-025-04011-2, doi:10.1007/s12185-025-04011-2. This article has 3 citations and is from a peer-reviewed journal.

7. (iordan2024clinicalfeaturesand pages 1-2): Iuliana Iordan, Ana-Maria Vlădăreanu, Cristina Mambet, Minodora Onisâi, Diana Cîșleanu, and Horia Bumbea. Clinical features and survival outcome in aggressive-type adult t-cell leukemia/lymphoma patients: real-life experience of a single center from an htlv-1 endemic country. Medicina, 60:872, May 2024. URL: https://doi.org/10.3390/medicina60060872, doi:10.3390/medicina60060872. This article has 1 citations.

8. (o’donnell2023integratedmolecularand pages 2-3): Jake S O’Donnell, Stewart K Hunt, and Keith J Chappell. Integrated molecular and immunological features of human t-lymphotropic virus type 1 infection and disease progression to adult t-cell leukaemia or lymphoma. The Lancet Haematology, 10:e539-e548, Jul 2023. URL: https://doi.org/10.1016/s2352-3026(23)00087-x, doi:10.1016/s2352-3026(23)00087-x. This article has 23 citations and is from a highest quality peer-reviewed journal.

9. (branda2025humantlymphotropicvirus pages 10-12): Francesco Branda, Chiara Romano, Grazia Pavia, Viola Bilotta, Chiara Locci, Ilenia Azzena, Ilaria Deplano, Noemi Pascale, Maria Perra, Marta Giovanetti, Alessandra Ciccozzi, Andrea De Vito, Angela Quirino, Nadia Marascio, Giovanni Matera, Giordano Madeddu, Marco Casu, Daria Sanna, Giancarlo Ceccarelli, Massimo Ciccozzi, and Fabio Scarpa. Human t-lymphotropic virus (htlv): epidemiology, genetic, pathogenesis, and future challenges. Viruses, 17:664, May 2025. URL: https://doi.org/10.3390/v17050664, doi:10.3390/v17050664. This article has 19 citations.

10. (o’donnell2023integratedmolecularand pages 5-6): Jake S O’Donnell, Stewart K Hunt, and Keith J Chappell. Integrated molecular and immunological features of human t-lymphotropic virus type 1 infection and disease progression to adult t-cell leukaemia or lymphoma. The Lancet Haematology, 10:e539-e548, Jul 2023. URL: https://doi.org/10.1016/s2352-3026(23)00087-x, doi:10.1016/s2352-3026(23)00087-x. This article has 23 citations and is from a highest quality peer-reviewed journal.

11. (iordan2024clinicalfeaturesand pages 5-6): Iuliana Iordan, Ana-Maria Vlădăreanu, Cristina Mambet, Minodora Onisâi, Diana Cîșleanu, and Horia Bumbea. Clinical features and survival outcome in aggressive-type adult t-cell leukemia/lymphoma patients: real-life experience of a single center from an htlv-1 endemic country. Medicina, 60:872, May 2024. URL: https://doi.org/10.3390/medicina60060872, doi:10.3390/medicina60060872. This article has 1 citations.

12. (nakahata2023understandingtheimmunopathology pages 3-5): Shingo Nakahata, Daniel Enriquez-Vera, M. Ishrat Jahan, Kenji Sugata, and Yorifumi Satou. Understanding the immunopathology of htlv-1-associated adult t-cell leukemia/lymphoma: a comprehensive review. Biomolecules, 13:1543, Oct 2023. URL: https://doi.org/10.3390/biom13101543, doi:10.3390/biom13101543. This article has 35 citations.

13. (ishida2017mogamulizumabforrelapsed pages 1-2): Takashi Ishida, Atae Utsunomiya, Tatsuro Jo, Kazuhito Yamamoto, Koji Kato, Shinichiro Yoshida, Shigeki Takemoto, Hitoshi Suzushima, Yukio Kobayashi, Yoshitaka Imaizumi, Kenichi Yoshimura, Kouichi Kawamura, Takeshi Takahashi, Kensei Tobinai, and Ryuzo Ueda. Mogamulizumab for relapsed adult t‐cell leukemia–lymphoma: updated follow‐up analysis of phase i and ii studies. Cancer Science, 108:2022-2029, Aug 2017. URL: https://doi.org/10.1111/cas.13343, doi:10.1111/cas.13343. This article has 82 citations and is from a peer-reviewed journal.

14. (altieri2025htlv1andatll pages 12-14): Adrian Altieri, Sean Patrick Reilly, Abu Mansalay, Alan Soo-Beng Khoo, Nettie Johnson, Zafar K. Khan, Amy Leader, Pooja Jain, and Pierluigi Porcu. Htlv-1 and atll: epidemiology, oncogenesis, and opportunities for community-informed research in the united states. Viruses, 17:1333, Sep 2025. URL: https://doi.org/10.3390/v17101333, doi:10.3390/v17101333. This article has 6 citations.

15. (branda2025humantlymphotropicvirus pages 17-17): Francesco Branda, Chiara Romano, Grazia Pavia, Viola Bilotta, Chiara Locci, Ilenia Azzena, Ilaria Deplano, Noemi Pascale, Maria Perra, Marta Giovanetti, Alessandra Ciccozzi, Andrea De Vito, Angela Quirino, Nadia Marascio, Giovanni Matera, Giordano Madeddu, Marco Casu, Daria Sanna, Giancarlo Ceccarelli, Massimo Ciccozzi, and Fabio Scarpa. Human t-lymphotropic virus (htlv): epidemiology, genetic, pathogenesis, and future challenges. Viruses, 17:664, May 2025. URL: https://doi.org/10.3390/v17050664, doi:10.3390/v17050664. This article has 19 citations.

16. (stUnknownyearprotocolforthe pages 5-10): P St and SE London. Protocol for the use of zidovudine and interferon-alpha in the management of acute adult t-cell leukaemia/lymphoma (atll). Unknown journal, Unknown year.

17. (bazarbachi2011howitreat pages 2-3): Ali Bazarbachi, Felipe Suarez, Paul Fields, and Olivier Hermine. How i treat adult t-cell leukemia/lymphoma. Blood, 118 7:1736-45, Aug 2011. URL: https://doi.org/10.1182/blood-2011-03-345702, doi:10.1182/blood-2011-03-345702. This article has 225 citations and is from a highest quality peer-reviewed journal.

18. (munakata2018adulttcellleukemialymphoma. pages 12-14): Wataru Munakata and Kensei Tobinai. Adult t-cell leukemia-lymphoma. Cancer treatment and research, 176:145-161, Dec 2018. URL: https://doi.org/10.1007/978-3-319-99716-2\_7, doi:10.1007/978-3-319-99716-2\_7. This article has 12 citations.

19. (shafiee2023zidovudineandinterferon pages 1-2): Arman Shafiee, Niloofar Seighali, Nooshin Taherzadeh-ghahfarokhi, Shayan Mardi, Sorour Shojaeian, Shahrzad Shadabi, Mahsa Hasani, Sabahat Haghi, and Sayed-Hamidreza Mozhgani. Zidovudine and interferon alfa based regimens for the treatment of adult t-cell leukemia/lymphoma (atll): a systematic review and meta-analysis. Virology Journal, Jun 2023. URL: https://doi.org/10.1186/s12985-023-02077-0, doi:10.1186/s12985-023-02077-0. This article has 13 citations and is from a peer-reviewed journal.

20. (shafiee2023zidovudineandinterferon pages 4-6): Arman Shafiee, Niloofar Seighali, Nooshin Taherzadeh-ghahfarokhi, Shayan Mardi, Sorour Shojaeian, Shahrzad Shadabi, Mahsa Hasani, Sabahat Haghi, and Sayed-Hamidreza Mozhgani. Zidovudine and interferon alfa based regimens for the treatment of adult t-cell leukemia/lymphoma (atll): a systematic review and meta-analysis. Virology Journal, Jun 2023. URL: https://doi.org/10.1186/s12985-023-02077-0, doi:10.1186/s12985-023-02077-0. This article has 13 citations and is from a peer-reviewed journal.

21. (shafiee2023zidovudineandinterferon pages 8-9): Arman Shafiee, Niloofar Seighali, Nooshin Taherzadeh-ghahfarokhi, Shayan Mardi, Sorour Shojaeian, Shahrzad Shadabi, Mahsa Hasani, Sabahat Haghi, and Sayed-Hamidreza Mozhgani. Zidovudine and interferon alfa based regimens for the treatment of adult t-cell leukemia/lymphoma (atll): a systematic review and meta-analysis. Virology Journal, Jun 2023. URL: https://doi.org/10.1186/s12985-023-02077-0, doi:10.1186/s12985-023-02077-0. This article has 13 citations and is from a peer-reviewed journal.

22. (shafiee2023zidovudineandinterferon pages 6-7): Arman Shafiee, Niloofar Seighali, Nooshin Taherzadeh-ghahfarokhi, Shayan Mardi, Sorour Shojaeian, Shahrzad Shadabi, Mahsa Hasani, Sabahat Haghi, and Sayed-Hamidreza Mozhgani. Zidovudine and interferon alfa based regimens for the treatment of adult t-cell leukemia/lymphoma (atll): a systematic review and meta-analysis. Virology Journal, Jun 2023. URL: https://doi.org/10.1186/s12985-023-02077-0, doi:10.1186/s12985-023-02077-0. This article has 13 citations and is from a peer-reviewed journal.

23. (shafiee2023zidovudineandinterferon pages 7-8): Arman Shafiee, Niloofar Seighali, Nooshin Taherzadeh-ghahfarokhi, Shayan Mardi, Sorour Shojaeian, Shahrzad Shadabi, Mahsa Hasani, Sabahat Haghi, and Sayed-Hamidreza Mozhgani. Zidovudine and interferon alfa based regimens for the treatment of adult t-cell leukemia/lymphoma (atll): a systematic review and meta-analysis. Virology Journal, Jun 2023. URL: https://doi.org/10.1186/s12985-023-02077-0, doi:10.1186/s12985-023-02077-0. This article has 13 citations and is from a peer-reviewed journal.

24. (iordan2024clinicalfeaturesand pages 9-10): Iuliana Iordan, Ana-Maria Vlădăreanu, Cristina Mambet, Minodora Onisâi, Diana Cîșleanu, and Horia Bumbea. Clinical features and survival outcome in aggressive-type adult t-cell leukemia/lymphoma patients: real-life experience of a single center from an htlv-1 endemic country. Medicina, 60:872, May 2024. URL: https://doi.org/10.3390/medicina60060872, doi:10.3390/medicina60060872. This article has 1 citations.

25. (iordan2024clinicalfeaturesand pages 2-4): Iuliana Iordan, Ana-Maria Vlădăreanu, Cristina Mambet, Minodora Onisâi, Diana Cîșleanu, and Horia Bumbea. Clinical features and survival outcome in aggressive-type adult t-cell leukemia/lymphoma patients: real-life experience of a single center from an htlv-1 endemic country. Medicina, 60:872, May 2024. URL: https://doi.org/10.3390/medicina60060872, doi:10.3390/medicina60060872. This article has 1 citations.

26. (sekine2017effectsofmogamulizumab pages 14-18): Masaaki Sekine, Yoko Kubuki, Takuro Kameda, Masanori Takeuchi, Takanori Toyama, Noriaki Kawano, Kouichi Maeda, Seiichi Sato, Junzo Ishizaki, Hiroshi Kawano, Ayako Kamiunten, Keiichi Akizuki, Yuki Tahira, Haruko Shimoda, Kotaro Shide, Tomonori Hidaka, Akira Kitanaka, Kiyoshi Yamashita, Hitoshi Matsuoka, and Kazuya Shimoda. Effects of mogamulizumab in adult t‐cell leukemia/lymphoma in clinical practice. European Journal of Haematology, 98:501-507, May 2017. URL: https://doi.org/10.1111/ejh.12863, doi:10.1111/ejh.12863. This article has 19 citations and is from a peer-reviewed journal.

27. (sekine2017effectsofmogamulizumab pages 10-14): Masaaki Sekine, Yoko Kubuki, Takuro Kameda, Masanori Takeuchi, Takanori Toyama, Noriaki Kawano, Kouichi Maeda, Seiichi Sato, Junzo Ishizaki, Hiroshi Kawano, Ayako Kamiunten, Keiichi Akizuki, Yuki Tahira, Haruko Shimoda, Kotaro Shide, Tomonori Hidaka, Akira Kitanaka, Kiyoshi Yamashita, Hitoshi Matsuoka, and Kazuya Shimoda. Effects of mogamulizumab in adult t‐cell leukemia/lymphoma in clinical practice. European Journal of Haematology, 98:501-507, May 2017. URL: https://doi.org/10.1111/ejh.12863, doi:10.1111/ejh.12863. This article has 19 citations and is from a peer-reviewed journal.

28. (yonekura2020mogamulizumabforadult pages 12-12): Kentaro Yonekura, Shigeru Kusumoto, Ilseung Choi, Nobuaki Nakano, Asahi Ito, Youko Suehiro, Yoshitaka Imaizumi, Makoto Yoshimitsu, Kisato Nosaka, Eiichi Ohtsuka, Michihiro Hidaka, Tatsuro Jo, Hidenori Sasaki, Yukiyoshi Moriuchi, Masao Ogata, Hiro Tatetsu, Kenji Ishitsuka, Yasushi Miyazaki, Ryuzo Ueda, Atae Utsunomiya, and Takashi Ishida. Mogamulizumab for adult t-cell leukemia-lymphoma: a multicenter prospective observational study. Blood advances, 4 20:5133-5145, Oct 2020. URL: https://doi.org/10.1182/bloodadvances.2020003053, doi:10.1182/bloodadvances.2020003053. This article has 43 citations and is from a peer-reviewed journal.

29. (wang2024currentstateof pages 12-14): Tiana T. Wang, Ashley Hirons, Marcel Doerflinger, Kevin V. Morris, Scott Ledger, Damian F. J. Purcell, Anthony D. Kelleher, and Chantelle L. Ahlenstiel. Current state of therapeutics for htlv-1. Viruses, 16:1616, Oct 2024. URL: https://doi.org/10.3390/v16101616, doi:10.3390/v16101616. This article has 21 citations.

30. (wang2024currentstateof pages 34-35): Tiana T. Wang, Ashley Hirons, Marcel Doerflinger, Kevin V. Morris, Scott Ledger, Damian F. J. Purcell, Anthony D. Kelleher, and Chantelle L. Ahlenstiel. Current state of therapeutics for htlv-1. Viruses, 16:1616, Oct 2024. URL: https://doi.org/10.3390/v16101616, doi:10.3390/v16101616. This article has 21 citations.

31. (munakata2018adulttcellleukemialymphoma. pages 16-17): Wataru Munakata and Kensei Tobinai. Adult t-cell leukemia-lymphoma. Cancer treatment and research, 176:145-161, Dec 2018. URL: https://doi.org/10.1007/978-3-319-99716-2\_7, doi:10.1007/978-3-319-99716-2\_7. This article has 12 citations.

32. (nakahata2023understandingtheimmunopathology pages 2-3): Shingo Nakahata, Daniel Enriquez-Vera, M. Ishrat Jahan, Kenji Sugata, and Yorifumi Satou. Understanding the immunopathology of htlv-1-associated adult t-cell leukemia/lymphoma: a comprehensive review. Biomolecules, 13:1543, Oct 2023. URL: https://doi.org/10.3390/biom13101543, doi:10.3390/biom13101543. This article has 35 citations.

33. (epsteinpeterson2025newtreatmentsfor pages 15-15): Zachary D. Epstein-Peterson, Ashwath Gurumurthi, and Steven M. Horwitz. New treatments for adult t-cell leukemia/lymphoma. Leukemia Research, 149:107642, Feb 2025. URL: https://doi.org/10.1016/j.leukres.2025.107642, doi:10.1016/j.leukres.2025.107642. This article has 9 citations and is from a peer-reviewed journal.

34. (branda2025humantlymphotropicvirus pages 23-25): Francesco Branda, Chiara Romano, Grazia Pavia, Viola Bilotta, Chiara Locci, Ilenia Azzena, Ilaria Deplano, Noemi Pascale, Maria Perra, Marta Giovanetti, Alessandra Ciccozzi, Andrea De Vito, Angela Quirino, Nadia Marascio, Giovanni Matera, Giordano Madeddu, Marco Casu, Daria Sanna, Giancarlo Ceccarelli, Massimo Ciccozzi, and Fabio Scarpa. Human t-lymphotropic virus (htlv): epidemiology, genetic, pathogenesis, and future challenges. Viruses, 17:664, May 2025. URL: https://doi.org/10.3390/v17050664, doi:10.3390/v17050664. This article has 19 citations.

35. (wang2024currentstateof pages 1-2): Tiana T. Wang, Ashley Hirons, Marcel Doerflinger, Kevin V. Morris, Scott Ledger, Damian F. J. Purcell, Anthony D. Kelleher, and Chantelle L. Ahlenstiel. Current state of therapeutics for htlv-1. Viruses, 16:1616, Oct 2024. URL: https://doi.org/10.3390/v16101616, doi:10.3390/v16101616. This article has 21 citations.

36. (altieri2025htlv1andatll pages 4-5): Adrian Altieri, Sean Patrick Reilly, Abu Mansalay, Alan Soo-Beng Khoo, Nettie Johnson, Zafar K. Khan, Amy Leader, Pooja Jain, and Pierluigi Porcu. Htlv-1 and atll: epidemiology, oncogenesis, and opportunities for community-informed research in the united states. Viruses, 17:1333, Sep 2025. URL: https://doi.org/10.3390/v17101333, doi:10.3390/v17101333. This article has 6 citations.

37. (wang2024currentstateof pages 9-11): Tiana T. Wang, Ashley Hirons, Marcel Doerflinger, Kevin V. Morris, Scott Ledger, Damian F. J. Purcell, Anthony D. Kelleher, and Chantelle L. Ahlenstiel. Current state of therapeutics for htlv-1. Viruses, 16:1616, Oct 2024. URL: https://doi.org/10.3390/v16101616, doi:10.3390/v16101616. This article has 21 citations.

38. (wang2024currentstateof pages 8-9): Tiana T. Wang, Ashley Hirons, Marcel Doerflinger, Kevin V. Morris, Scott Ledger, Damian F. J. Purcell, Anthony D. Kelleher, and Chantelle L. Ahlenstiel. Current state of therapeutics for htlv-1. Viruses, 16:1616, Oct 2024. URL: https://doi.org/10.3390/v16101616, doi:10.3390/v16101616. This article has 21 citations.
