---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-04T14:14:04.555103'
end_time: '2026-04-04T14:43:41.230652'
duration_seconds: 1776.68
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Human African trypanosomiasis
  mondo_id: ''
  category: Infectious Disease
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 85
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Human African trypanosomiasis
- **MONDO ID:**  (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Human African trypanosomiasis** covering all of the
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
- **Disease Name:** Human African trypanosomiasis
- **MONDO ID:**  (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Human African trypanosomiasis** covering all of the
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


# Human African trypanosomiasis (HAT) — disease characteristics research report

## Scope, evidence base, and evidence types
This report synthesizes evidence from (i) peer‑reviewed WHO monitoring analyses and expert reviews (2024–2025), (ii) primary clinical trials (NECT and fexinidazole pivotal trials; acoziborole phase 2/3), (iii) primary host‑genetics association studies (APOL1), and (iv) recent field/implementation and diagnostic-technology studies (including 2024 CRISPR-SHERLOCK resistance surveillance). Citations are provided for each major claim.

---

## 1. Disease information

### 1.1 Overview (what is the disease?)
Human African trypanosomiasis (HAT), commonly called **sleeping sickness**, is a neglected tropical disease caused by infection with the protozoan parasite **Trypanosoma brucei**, transmitted by the tsetse fly (**Glossina**). The disease occurs in sub‑Saharan Africa and is classically described as a **two‑stage illness**: an initial haemolymphatic stage followed by a central nervous system (CNS) meningoencephalitic stage that can progress to coma and death if untreated. (franco2024theeliminationof pages 2-4, barrett2025transformingthechemotherapy pages 2-4)

Two epidemiologically distinct forms dominate:
- **gambiense HAT (gHAT)** due to *T. b. gambiense*: slower, often chronic, historically predominantly anthroponotic, in West/Central Africa. (franco2024theeliminationof pages 2-4, barrett2025transformingthechemotherapy pages 2-4)
- **rhodesiense HAT (rHAT)** due to *T. b. rhodesiense*: faster, more acute, zoonotic with livestock/wildlife reservoirs, in East/Southern Africa. (franco2024theeliminationof pages 2-4, barrett2025transformingthechemotherapy pages 2-4)

### 1.2 Key identifiers (OMIM, Orphanet, ICD-10/ICD-11, MeSH, Mondo)
**Identifiers explicitly present in retrieved evidence**:
- **MeSH:** *Trypanosomiasis, African* — **D014353** (listed in ClinicalTrials.gov trial metadata). (NCT03087955 chunk 3, NCT05256017 chunk 3)

**Not found in retrieved corpus for this run (flagged as missing):** ICD‑10, ICD‑11, MONDO ID, Orphanet/ORPHA identifiers were not explicitly present in the retrieved texts. (lindner2020newwhoguidelines pages 1-2, NCT03087955 chunk 3)

### 1.3 Synonyms and alternative names
Synonyms/variants appearing in the evidence include:
- **sleeping sickness** (explicitly used as common name) (barrett2025transformingthechemotherapy pages 1-2)
- **African trypanosomiasis** (imran2022discoverydevelopmentinventions pages 9-11)
- **HAT**, **gHAT**, and **rHAT** (NCT05256017 chunk 3, barrett2024eliminationofhuman pages 1-2)
- French acronym **THA** (*trypanosomiase humaine africaine*) appearing in facility name in trial context (NCT03087955 chunk 3)

### 1.4 Patient-level vs aggregated resources
The WHO monitoring analysis compiles **country programme data** (National Sleeping Sickness Control Programmes; atlas/georeferenced surveillance) and reports **aggregated disease-level metrics** (cases, risk area, screening volumes, facility counts). (franco2024theeliminationof pages 1-2, franco2024theeliminationof pages 9-11)

---

## 2. Etiology

### 2.1 Causal factors
- **Infectious cause:** infection with *Trypanosoma brucei* subspecies (*T. b. gambiense* or *T. b. rhodesiense*). (franco2024theeliminationof pages 2-4)
- **Vector:** tsetse fly (**Glossina**) bite. (franco2024theeliminationof pages 2-4)
- **Reservoir ecology:** gHAT is mainly anthroponotic; rHAT is zoonotic with livestock and wildlife reservoirs, making interruption of rHAT transmission far more dependent on veterinary interventions. (franco2024theeliminationof pages 2-4)

### 2.2 Risk factors
**Environmental/exposure risk**
- Living/working in rural endemic foci with exposure to tsetse bites. (franco2024theeliminationof pages 1-2, franco2024theeliminationof pages 2-4)

**Host genetic factors (protective and susceptibility)**
Evidence strongly implicates **APOL1** (apolipoprotein L1) variants in differential susceptibility/outcomes.

- **APOL1 G2** (rs71785313; in-frame deletion) showed strong protection against *T. b. rhodesiense* HAT in a case-control setting: OR **0.20** (95% CI 0.07–0.48; p=0.0001), consistent with ~5‑fold reduced susceptibility. (cooper2017apol1renalrisk pages 4-5)
- Independent evidence in northern Malawi also found strong protection of **APOL1 G2** against rHAT: OR **0.14** (95% CI 0.05–0.41; Bonferroni-corrected p=0.00068). (kamoto2019associationofapol1 pages 6-7)

For *T. b. gambiense*, APOL1 effects are more complex:
- **APOL1 G1** associated with reduced odds of progressing to clinical gHAT (OR **0.33**, 95% CI 0.17–0.62; p=0.0005), interpreted as increased likelihood of **latent/asymptomatic carriage**. (cooper2017apol1renalrisk pages 4-5)
- **APOL1 G2** associated with increased risk of clinical progression in gHAT (OR **3.08**, 95% CI 1.45–7.06; p=0.0025), strengthening to OR **5.87** (95% CI 2.16–20.01; p=0.0001) after excluding compound heterozygotes. (cooper2017apol1renalrisk pages 4-5)

A rare susceptibility-associated APOL1 variant:
- **APOL1 N264K**: functional evidence suggests this substitution can reduce ApoL1 trypanolytic activity in contexts of atypical infection, potentially increasing risk in populations with high homozygous frequency. (cuypers2016apolipoproteinl1variant pages 1-2)

### 2.3 Protective factors
- **Innate immunity via APOL1** in human serum lyses many non-human African trypanosomes; resistance mechanisms are required for human-infective subspecies. (currier2018decodingthenetwork pages 1-2)
- Specific APOL1 variant **G2** is protective against rHAT in multiple populations (above). (cooper2017apol1renalrisk pages 4-5, kamoto2019associationofapol1 pages 6-7)

### 2.4 Gene–environment interactions
The evidence base in this run supports a conceptual interaction: **vector-borne exposure** determines infection risk, while **APOL1 genotype** modifies susceptibility and/or progression once exposed. However, explicit quantitative G×E interaction models were not retrieved in the available texts. (cooper2017apol1renalrisk pages 4-5, franco2024theeliminationof pages 2-4)

---

## 3. Phenotypes (clinical manifestations)

### 3.1 Stage 1 vs stage 2 (definitions and symptoms)
A consistent modern description separates:

**Stage 1 (haemolymphatic)**
- Parasites multiply in blood and lymphatic system, producing non‑specific systemic symptoms.
- Reported symptoms/signs include intermittent fever, headache, pruritus, lymphadenopathy, weakness, joint and muscle pain, swollen lymph nodes. (mesu2021oralfexinidazolefor pages 1-2, barrett2025transformingthechemotherapy pages 2-4)

**Stage 2 (meningoencephalitic/CNS)**
- Parasites cross the blood–brain barrier and induce CNS changes.
- Manifestations include disturbance of sleep–wake cycle (hallmark), sensory changes, abnormal muscle tone, ataxia, psychiatric symptoms, seizures, coma, and death if untreated. (barrett2025transformingthechemotherapy pages 2-4, mesu2021oralfexinidazolefor pages 1-2)

### 3.2 Temporal development (onset and progression)
- gHAT is typically **chronic**, often lasting months to years; a clinical description notes CNS involvement after “about **1 year or more**” in gambiense infection. (mesu2021oralfexinidazolefor pages 1-2, imran2022discoverydevelopmentinventions pages 1-5)
- rHAT is typically **acute**, often developing over weeks, and is associated with higher parasitaemia, facilitating blood-based detection. (imran2022discoverydevelopmentinventions pages 1-5)

### 3.3 Staging thresholds (CSF WBC)
Cutoffs in use vary by guideline and operational decisions:
- A gHAT cohort study described **early stage 2** as **6–20 CSF WBC/µL** and **late stage 2** as **>20 CSF WBC/µL**. (mesu2021oralfexinidazolefor pages 1-2)
- WHO/operational definitions discussed include second-stage defined by **>5 CSF WBC/µL** (contested) and trial inclusion criteria using **>20 CSF WBC/µL** or trypanosomes in CSF. (capewell2014normalhumanserum pages 210-212, lindner2020newwhoguidelines pages 2-4)
- WHO guideline-linked treatment stratification defines “severe” second stage by **CSF WBC ≥100/µL** for choosing NECT over fexinidazole. (lindner2020newwhoguidelines pages 2-4)

### 3.4 Suggested HPO terms (non-exhaustive, inferred from evidence)
Mapping suggestions (not all explicitly validated by HPO in retrieved texts):
- Fever (HP:0001945)
- Headache (HP:0002315)
- Pruritus (HP:0000989)
- Lymphadenopathy (HP:0002716)
- Sleep disturbance / abnormal sleep-wake cycle (e.g., HP:0002360)
- Ataxia (HP:0001251)
- Seizures (HP:0001250)
- Coma (HP:0001259)
- Psychiatric/behavioral abnormalities (broad category)
Evidence base: symptom lists and stage definitions from clinical reviews and cohort descriptions. (barrett2025transformingthechemotherapy pages 2-4, mesu2021oralfexinidazolefor pages 1-2)

**Phenotype frequencies:** quantitative symptom frequencies were not broadly available in the retrieved clinical phenotype texts; an exception is the dermal-reservoir cohort reporting dermatological symptoms in specific groups, but this is not a generalizable clinical frequency for all HAT. (soumah2024prevalenceofdermal pages 7-8)

---

## 4. Genetic / molecular information

### 4.1 Causal genes
HAT is not a Mendelian genetic disorder; primary causation is infectious. Host genetics influence susceptibility/outcome.

### 4.2 Host susceptibility/protective genes (human)
**APOL1 (HGNC:613)** is the central host gene in retrieved evidence:
- Variants **G1** (rs73885319; rs60910145) and **G2** (rs71785313) show subspecies‑specific associations with rHAT and gHAT clinical outcomes. (cooper2017apol1renalrisk pages 4-5)
- **N264K** is a functional variant associated with reduced ApoL1 lytic activity in a documented atypical infection context. (cuypers2016apolipoproteinl1variant pages 1-2)

### 4.3 Parasite molecular determinants relevant to human infection and therapy
**Human serum resistance (parasite side):**
- *T. b. rhodesiense* resists ApoL1 via **SRA** binding in the endosomal-lysosomal system, preventing pore formation. (currier2018decodingthenetwork pages 1-2)

**Drug resistance determinants and surveillance targets:**
- Melarsoprol/pentamidine cross-resistance is linked to changes in transporters/channels, including an **AQP2/3(814) chimera**; acoziborole resistance can be driven by **CPSF3** single-nucleotide variants (e.g., N232H in vitro). (anton2024anextgeneration pages 1-4)

---

## 5. Environmental information

### 5.1 Infectious agent and vector (primary environmental determinant)
Exposure is driven by tsetse fly presence and vector–human contact in endemic foci. (franco2024theeliminationof pages 2-4)

### 5.2 Non-genetic protective factors
Population-level protection is primarily programmatic (vector control, surveillance, early diagnosis and treatment) rather than individual lifestyle factors. (franco2024theeliminationof pages 2-4, franco2024theeliminationof pages 13-15)

---

## 6. Mechanism / pathophysiology

### 6.1 Causal chain (from exposure to clinical disease)
1. **Tsetse inoculation** introduces parasites into host → bloodstream/lymph multiplication (stage 1 systemic symptoms). (franco2024theeliminationof pages 2-4, barrett2025transformingthechemotherapy pages 2-4)
2. **Immune evasion and survival in human serum:** Human trypanolytic factors contain **ApoL1** which can kill susceptible trypanosomes via pore formation after endocytosis and trafficking through endosomal-lysosomal compartments with pH-dependent activation. (currier2018decodingthenetwork pages 1-2)
3. Human-infective subspecies have evolved resistance; for rHAT, **SRA** binding prevents ApoL1 pore formation. (currier2018decodingthenetwork pages 1-2)
4. **Tissue reservoirs and low-parasitaemia states:** For gHAT, evidence supports an extravascular **skin (dermal) reservoir**, with parasites in basal dermis transmissible to tsetse even when blood parasites are undetectable. (soumah2024prevalenceofdermal pages 2-4)
5. **CNS invasion:** Over time, parasites cross the blood–brain barrier, leading to stage 2 neuropsychiatric and sleep/wake disturbances and potentially seizures/coma/death. (barrett2025transformingthechemotherapy pages 2-4, mesu2021oralfexinidazolefor pages 1-2)

### 6.2 Dermal reservoir as a mechanism relevant to elimination
A 2024 prospective study in Guinea found dermal parasites by PCR and/or immunohistochemistry in up to **71% of confirmed cases** and **41% of unconfirmed seropositive individuals**, supporting a hidden reservoir that could sustain transmission in low-endemic settings. (soumah2024prevalenceofdermal pages 1-2)
Persistence after treatment was reduced but not eliminated in all individuals: skin detection dropped to **17%** in treated confirmed cases and persisted up to **25%** in untreated seropositives at follow-up. (soumah2024prevalenceofdermal pages 1-2)

### 6.3 Suggested ontology mappings (mechanisms)
**GO biological process (suggested):** endocytosis; lysosomal trafficking; pore formation; immune evasion; response to protozoan; blood–brain barrier traversal. Mechanistic basis: ApoL1 uptake and trafficking; CNS stage transition. (currier2018decodingthenetwork pages 1-2, barrett2025transformingthechemotherapy pages 2-4)

**Cell types (CL, suggested):** endothelial cells (blood–brain barrier), mononuclear phagocytes, neurons/astrocytes (CNS manifestations). (barrett2025transformingthechemotherapy pages 2-4)

---

## 7. Anatomical structures affected

**Primary anatomical compartments:**
- Blood and lymphatic system (stage 1) (barrett2025transformingthechemotherapy pages 2-4)
- CNS / brain and cerebrospinal fluid (stage 2) (barrett2025transformingthechemotherapy pages 2-4, mesu2021oralfexinidazolefor pages 1-2)
- Skin dermis as extravascular reservoir (soumah2024prevalenceofdermal pages 2-4, soumah2024prevalenceofdermal pages 1-2)

**Suggested UBERON terms (illustrative):** blood, lymph node, skin dermis, cerebrospinal fluid, brain, blood–brain barrier.

---

## 8. Temporal development (natural history)

- gHAT often progresses slowly; CNS stage is described as occurring after ~1 year or more in one clinical description; rHAT is more acute (weeks). (mesu2021oralfexinidazolefor pages 1-2, imran2022discoverydevelopmentinventions pages 1-5)
- Elimination-phase programs emphasize the need for prolonged surveillance after last case because resurgence is possible. (franco2024theeliminationof pages 13-15, barrett2024eliminationofhuman pages 1-2)

---

## 9. Inheritance and population

### 9.1 Epidemiology and burden (recent)
The WHO monitoring analysis reports:
- **802** global HAT cases in **2021** and **837** in **2022**; **94%** were gambiense. (franco2024theeliminationof pages 1-2)
- Estimated **41.5 million** people live in areas at risk (2018–2022), with **1.5 million** at moderate-or-higher risk. (franco2024theeliminationof pages 9-11)
- Areas reporting ≥1 case/10,000 inhabitants/year (2018–2022) covered **73,134 km²**, with **3,013 km²** at high/very high risk. (franco2024theeliminationof pages 1-2)

For auditability, Figure/Table crops were retrieved for screened numbers and case tables from the WHO monitoring paper. (franco2024theeliminationof media 72eedba2, franco2024theeliminationof media 237c981b, franco2024theeliminationof media 1786e4aa, franco2024theeliminationof media 65382298)

### 9.2 Host genetics (not inheritance of disease)
Host APOL1 variants (G1/G2) exhibit population-specific frequencies and associations; some studies show strong protection (rHAT), while others show no association in certain populations, underscoring heterogeneity. (kamoto2019associationofapol1 pages 6-7, cooper2017apol1renalrisk pages 1-2)

### 9.3 Demographics and geography
- gHAT is concentrated in West/Central Africa; rHAT in East/Southern Africa; risk and remaining high-risk pockets are geographically focal. (franco2024theeliminationof pages 2-4, franco2024theeliminationof pages 9-11)

---

## 10. Diagnostics

### 10.1 Screening and confirmation (gHAT)
A two-step algorithm is described:
1. **Serological screening**: CATT whole blood (CATTwb) or RDTs (examples listed: SD Bioline HAT, Abbott Bioline HAT 2.0, HAT Sero‑K‑SeT). (soumah2024prevalenceofdermal pages 2-4)
2. **Parasitological confirmation**: microscopy on blood using concentration methods such as **mAECT buffy coat**, plus lymph node aspirate when indicated; and CSF examination for staging. (soumah2024prevalenceofdermal pages 2-4)

### 10.2 Staging diagnostics and performance statistics
- Blood parasitaemia can fluctuate to **<100 trypanosomes/mL**, while mAECT on buffy coat has sensitivity about **10 trypanosomes/mL**, explaining missed cases by standard parasitology. (soumah2024prevalenceofdermal pages 12-13)
- WHO criteria often use **>5 CSF WBC/µL** to define second stage, but cutoffs are contested; some settings use 20 WBC/µL. (capewell2014normalhumanserum pages 210-212)
- One molecular staging approach reported **18S PCR** sensitivity **88%** and specificity **83%** for stage determination, but persistence of DNA after cure limits use as a test-of-cure. (capewell2014normalhumanserum pages 210-212)

### 10.3 rHAT diagnostics
Serology is not as developed for rHAT; parasitological detection in blood is often easier because parasitaemia tends to be higher in acute disease. (imran2022discoverydevelopmentinventions pages 1-5, barrett2025transformingthechemotherapy pages 2-4)

### 10.4 Differential diagnosis
A structured differential diagnosis list was not explicitly retrieved in this run; given the non‑specific febrile presentation in stage 1, differential diagnosis typically includes malaria and other febrile illnesses, and for stage 2 includes meningitis/encephalitis and other neuropsychiatric causes, but these statements would require additional sourced evidence beyond the retrieved corpus.

### 10.5 Recent diagnostic development (2024)
A 2024 preprint describes **SHERLOCK (Cas13)** assays to detect known and emergent **drug-resistance genotypes** (AQP2/3(814) chimera; CPSF3 SNV conferring in vitro acoziborole resistance), supporting surveillance in the elimination era. (anton2024anextgeneration pages 1-4)

---

## 11. Outcome / prognosis

Without treatment, HAT is described as **almost invariably fatal**. (franco2024theeliminationof pages 2-4)

During the elimination era, mortality is strongly influenced by access to diagnosis and effective therapy; some legacy therapies carry notable toxicity. For example, melarsoprol is noted as potentially killing up to **5%** of treated patients in one expert elimination commentary. (barrett2024eliminationofhuman pages 1-2)

---

## 12. Treatment

### 12.1 Current standard and emerging regimens (key trials and outcomes)
Therapeutic practice has shifted toward simplified oral regimens where feasible.

- **Fexinidazole (oral)**: In a pivotal randomized non-inferiority trial for late-stage gHAT, 18‑month success was **91% (239/264)** with fexinidazole vs **98% (124/130)** with NECT; difference −6.4% within a −13% non-inferiority margin. (mesu2018oralfexinidazolefor pages 1-2)
  - WHO guideline synthesis indicates fexinidazole is recommended for first-stage and non-severe second-stage (CSF WBC <100/µL), while severe second-stage (CSF WBC ≥100/µL) should receive NECT because failure is higher with fexinidazole. (lindner2020newwhoguidelines pages 2-4)
  - A cohort of stage 1/early stage 2 gHAT reported high success: **99%** at 12 months and **98%** at 18 months. (mesu2021oralfexinidazolefor pages 1-2)

- **NECT (nifurtimox–eflornithine combination therapy)**: In an RCT in Congo, cure was **96.2%** with NECT vs **94.1%** with eflornithine monotherapy (18 months). (priotto2007nifurtimoxeflornithinecombinationtherapy pages 1-2)
  - Field pharmacovigilance across 1,735 treated patients reported ≥1 adverse event in **60.1%**, serious adverse events **1.1%**, and case fatality **0.5%** (2010–2011 routine use). (franco2012monitoringtheuse pages 1-2)

- **Acoziborole (single-dose oral; pipeline/late-stage)**: Phase 2/3 single-arm trial in gHAT showed late-stage success **95.2%** at 18 months (159/167), with evaluable population success **98.1%** (159/162); early/intermediate stage success **100%** (41/41). (kumeso2023efficacyandsafety pages 1-2, kumeso2023efficacyandsafety pages 6-7)
  - Safety signals in that trial: treatment-emergent adverse events in **14%**, all mild/moderate, and serious events not judged drug-related. (kumeso2023efficacyandsafety pages 6-7)

### 12.2 Real-world implementation of treatment
WHO monitoring data for 2021–2022 show among **1,473** treated gambiense cases, **43.52%** received fexinidazole, **35.78%** received NECT, and **20.71%** received pentamidine. (franco2024theeliminationof pages 11-13)

### 12.3 Suggested MAXO terms (illustrative)
- Antiprotozoal drug therapy
- Combination drug therapy (NECT)
- Oral drug administration (fexinidazole; acoziborole)
- Intravenous infusion (eflornithine)
Evidence base: regimen descriptions and implementation constraints. (mesu2018oralfexinidazolefor pages 1-2, priotto2007nifurtimoxeflornithinecombinationtherapy pages 1-2)

---

## 13. Prevention

### 13.1 Primary prevention (vector control)
Vector control is a core elimination pillar alongside case detection and treatment. WHO monitoring notes expansion of tsetse-control activities supporting gHAT control in multiple countries (e.g., Angola, Cameroon, Chad, Côte d’Ivoire, DRC, Guinea, Uganda), and multisectoral/One Health implementation in others. (franco2024theeliminationof pages 11-13)

### 13.2 Secondary prevention (surveillance and screening)
- 2021–2022 screening totals for gHAT were approximately **4.5 million** screened (3.6 million active screening; ~0.9 million passive screening). (franco2024theeliminationof pages 1-2)
- Active screening volume was **3,599,039** in 2021–2022, with a noted decline relative to 2019–2020. (franco2024theeliminationof pages 9-11)

### 13.3 Tertiary prevention (preventing complications)
Timely diagnosis and effective therapy prevent progression to CNS stage and death; programs emphasize maintaining diagnostic capacity and integrating activities into primary care as incidence declines. (franco2024theeliminationof pages 13-15)

### 13.4 Elimination targets and verification
WHO 2021–2030 roadmap: elimination of gambiense transmission aims for **zero reported cases** and verification in **15 countries** by 2030; verification requires **≥5 consecutive years of zero reported T. b. gambiense cases** with evidence of adequate surveillance and dossier submission. (franco2024theeliminationof pages 2-4, franco2024theeliminationof pages 13-15)

---

## 14. Other species / natural disease (reservoirs, zoonotic aspects)

- **rHAT is zoonotic** with livestock and wildlife reservoirs and limited human-to-human transmission, contributing to why interruption is not considered readily achievable without major veterinary interventions. (franco2024theeliminationof pages 2-4, kamoto2019associationofapol1 pages 1-2)
- Potential reservoirs for gHAT include **domestic pigs** (noted as potential reservoir, although some sources suggest infections may clear) and other domestic animals in certain settings. (capewell2014normalhumanserum pages 146-149, chukwudi2025prevalenceofhuman pages 1-2)
- A 2024 Nigeria scoping review reported average prevalence **3.3%** for HAT and **27.3%** for animal African trypanosomiasis (AAT) in compiled studies, and identified cattle, pigs, and dogs as carriers of human-infective trypanosomes in Nigeria. (odebunmi2024prevalenceofhuman pages 1-4)

---

## 15. Model organisms and experimental systems
Commonly referenced research and preclinical systems in the retrieved evidence include:
- **Laboratory rodents/mouse models** to study infection outcomes and serum resistance (noting parallels to “trypanotolerance” and that rhodesiense can be manipulated in rodents). (kamoto2019associationofapol1 pages 1-2, capewell2014normalhumanserum pages 146-149)
- **In vitro assays** of trypanolysis using recombinant APOL proteins and bloodstream-form parasites. (fontaine2017apolswithlow pages 1-2, cooper2016aprimateapol1 pages 1-2)
- Functional genetic screens in *T. brucei* (genome-scale RNAi screen) identifying determinants of ApoL1 sensitivity and endocytic trafficking dependencies. (currier2018decodingthenetwork pages 1-2)

---

## Recent developments (prioritizing 2023–2024)

1. **Elimination monitoring (2024):** WHO-aligned monitoring shows sustained low case counts (802 in 2021; 837 in 2022) with extensive screening and shrinking risk areas; seven countries validated for elimination as a public health problem, and surveillance integration challenges highlighted for the “last mile.” (franco2024theeliminationof pages 1-2, franco2024theeliminationof pages 13-15)
2. **Acoziborole phase 2/3 results (Apr 2023):** single-dose oral efficacy and tolerability for gHAT across stages suggests potential to simplify treatment pathways and reduce staging dependence. (kumeso2023efficacyandsafety pages 1-2, kumeso2023efficacyandsafety pages 6-7)
3. **Dermal reservoir epidemiology (Aug 2024):** quantification of extravascular dermal parasites in confirmed and seropositive unconfirmed individuals adds urgency to address cryptic reservoirs for elimination. (soumah2024prevalenceofdermal pages 1-2, soumah2024prevalenceofdermal pages 12-13)
4. **CRISPR-SHERLOCK resistance surveillance (Sep 2024):** development of field-relevant molecular surveillance assays for resistance genotypes linked to pentamidine/melarsoprol and acoziborole. (anton2024anextgeneration pages 1-4)

---

## Embedded synthesis tables

The following tables consolidate identifiers, epidemiology, and therapeutics for knowledge-base use.

| Identifier system | Identifier | Preferred term | Synonyms/notes | Source | URL |
|---|---|---|---|---|---|
| MeSH | D014353 | Trypanosomiasis, African | Controlled vocabulary term explicitly present in ClinicalTrials.gov-derived excerpt; corresponds to human African trypanosomiasis (NCT03087955 chunk 3, NCT05256017 chunk 3) | ClinicalTrials.gov excerpt for NCT03087955 / NCT05256017 | https://clinicaltrials.gov/study/NCT03087955 |
| Common name / clinical term | Not found in retrieved evidence as coded identifier | Human African trypanosomiasis | Common synonym: sleeping sickness; abbreviation: HAT (barrett2025transformingthechemotherapy pages 1-2, mariotti2025useoffexinidazole pages 11-11, barrett2024eliminationofhuman pages 1-2, imran2022discoverydevelopmentinventions pages 9-11) | Barrett 2025; Mariotti 2025; Barrett 2024; Imran 2022 | https://doi.org/10.1128/cmr.00153-23 |
| Common synonym | Not applicable | African trypanosomiasis | Variant naming used in retrieved texts; overlaps with HAT/sleeping sickness terminology (barrett2025transformingthechemotherapy pages 1-2, n’djetchi2025dermaltrypanosomesin pages 12-12, imran2022discoverydevelopmentinventions pages 9-11) | Barrett 2025; N'Djetchi 2025; Imran 2022 | https://doi.org/10.1128/cmr.00153-23 |
| Clinical abbreviation | Not applicable | gHAT | gambiense human African trypanosomiasis; chronic West/Central African form caused by *Trypanosoma brucei gambiense* (NCT05256017 chunk 3, barrett2024eliminationofhuman pages 1-2, lindner2020newwhoguidelines pages 1-2) | ClinicalTrials.gov excerpt; Barrett 2024; Lindner 2020 | https://clinicaltrials.gov/study/NCT05256017 |
| Clinical abbreviation | Not found explicitly as coded term in retrieved evidence | rHAT | rhodesiense human African trypanosomiasis; acute East/Southern African form caused by *Trypanosoma brucei rhodesiense*; disease form described in retrieved corpus though abbreviation appears less often than full term (barrett2025transformingthechemotherapy pages 1-2, imran2022discoverydevelopmentinventions pages 9-11) | Barrett 2025; Imran 2022 | https://doi.org/10.1128/cmr.00153-23 |
| French abbreviation | Not applicable | THA | French acronym for *trypanosomiase humaine africaine*; appears in facility name in ClinicalTrials.gov-derived excerpt (NCT03087955 chunk 3) | ClinicalTrials.gov excerpt for NCT03087955 | https://clinicaltrials.gov/study/NCT03087955 |
| Causative agent | Not applicable | *Trypanosoma brucei gambiense* | Agent of gambiense HAT / gHAT; named explicitly in trial and review excerpts (NCT03087955 chunk 3, barrett2025transformingthechemotherapy pages 1-2, barrett2024eliminationofhuman pages 1-2, lindner2020newwhoguidelines pages 1-2, imran2022discoverydevelopmentinventions pages 9-11) | ClinicalTrials.gov excerpt; Barrett 2025; Barrett 2024; Lindner 2020; Imran 2022 | https://clinicaltrials.gov/study/NCT03087955 |
| Causative agent | Not applicable | *Trypanosoma brucei rhodesiense* | Agent of rhodesiense HAT / rHAT; named explicitly in review excerpts (barrett2025transformingthechemotherapy pages 1-2, imran2022discoverydevelopmentinventions pages 9-11) | Barrett 2025; Imran 2022 | https://doi.org/10.1128/cmr.00153-23 |
| ICD-10 | Not found in retrieved evidence | Not available from retrieved corpus | No explicit ICD-10 code identified in retrieved evidence (NCT03087955 chunk 3, barrett2024eliminationofhuman pages 1-2, lindner2020newwhoguidelines pages 1-2) | Not reported in retrieved evidence | Not available |
| ICD-11 | Not found in retrieved evidence | Not available from retrieved corpus | No explicit ICD-11 code identified in retrieved evidence (NCT03087955 chunk 3, barrett2024eliminationofhuman pages 1-2, lindner2020newwhoguidelines pages 1-2) | Not reported in retrieved evidence | Not available |
| MONDO | Not found in retrieved evidence | Not available from retrieved corpus | No MONDO identifier identified in retrieved evidence (NCT03087955 chunk 3, lindner2020newwhoguidelines pages 1-2) | Not reported in retrieved evidence | Not available |
| Orphanet / ORPHA | Not found in retrieved evidence | Not available from retrieved corpus | No Orphanet/ORPHA identifier identified in retrieved evidence (NCT03087955 chunk 3, lindner2020newwhoguidelines pages 1-2) | Not reported in retrieved evidence | Not available |


*Table: This table summarizes the identifiers and naming variants for human African trypanosomiasis that were explicitly available in the retrieved evidence. It highlights the MeSH identifier that was found, maps common synonyms and causative agents, and notes identifier systems that were not recoverable from the available corpus.*

| Metric | Value | Year/Period | Notes | Primary source (author year journal) | URL |
|---|---:|---|---|---|---|
| Global reported HAT cases | 802 | 2021 | All forms combined; below WHO elimination-as-a-public-health-problem threshold of <2,000 cases/year (franco2024theeliminationof pages 1-2, franco2024theeliminationof pages 5-7) | Franco et al. 2024, *PLOS Neglected Tropical Diseases* | https://doi.org/10.1371/journal.pntd.0012111 |
| Global reported HAT cases | 837 | 2022 | All forms combined; incidence remained <1,000 annually for the fifth consecutive year by 2023 stakeholder review (franco2024theeliminationof pages 1-2, barrett2024eliminationofhuman pages 1-2) | Franco et al. 2024, *PLOS Neglected Tropical Diseases*; Barrett et al. 2024, *PLOS Neglected Tropical Diseases* | https://doi.org/10.1371/journal.pntd.0012111 |
| Share caused by *T. b. gambiense* | 94% | 2021–2022 update | Majority of reported cases were gambiense HAT (franco2024theeliminationof pages 1-2) | Franco et al. 2024, *PLOS Neglected Tropical Diseases* | https://doi.org/10.1371/journal.pntd.0012111 |
| Active screening volume | 3,599,039 people | 2021–2022 | 2,033,969 in 2021 and 1,565,070 in 2022; lowest in 10 years, 22% below 2019–2020 (franco2024theeliminationof pages 9-11) | Franco et al. 2024, *PLOS Neglected Tropical Diseases* | https://doi.org/10.1371/journal.pntd.0012111 |
| Total gambiense screening volume | 4.5 million people | 2021–2022 | Aggregate screening total; approximately 3.6 million active and 0.9 million passive/serological (franco2024theeliminationof pages 1-2) | Franco et al. 2024, *PLOS Neglected Tropical Diseases* | https://doi.org/10.1371/journal.pntd.0012111 |
| Passive serological screening volume | 900,407 people | 2021–2022 | Gambiense HAT passive screening through fixed facilities (franco2024theeliminationof pages 9-11) | Franco et al. 2024, *PLOS Neglected Tropical Diseases* | https://doi.org/10.1371/journal.pntd.0012111 |
| Fixed diagnostic facilities inventoried | 1,521 facilities | 2022 | Includes 1,294 diagnosis facilities reported for gambiense HAT; 796 were in DRC (franco2024theeliminationof pages 9-11) | Franco et al. 2024, *PLOS Neglected Tropical Diseases* | https://doi.org/10.1371/journal.pntd.0012111 |
| Population at risk | 41.5 million people | 2018–2022 | Estimated total population living in areas at risk of HAT (franco2024theeliminationof pages 9-11, franco2024theeliminationof pages 13-15) | Franco et al. 2024, *PLOS Neglected Tropical Diseases* | https://doi.org/10.1371/journal.pntd.0012111 |
| Population at moderate-or-higher risk | 1.5 million people | 2018–2022 | Approximately 4% of total at-risk population; 40.0 million at low/very low risk (franco2024theeliminationof pages 9-11, franco2024theeliminationof pages 13-15) | Franco et al. 2024, *PLOS Neglected Tropical Diseases* | https://doi.org/10.1371/journal.pntd.0012111 |
| Area with ≥1 case/10,000 inhabitants/year | 73,134 km² | 2018–2022 | Combined HAT risk area used for elimination monitoring; 90% reduction from 2000–2004 baseline (franco2024theeliminationof pages 1-2) | Franco et al. 2024, *PLOS Neglected Tropical Diseases* | https://doi.org/10.1371/journal.pntd.0012111 |
| Very high/high risk area | 3,013 km² | 2018–2022 | Remaining highest-risk surface area only (franco2024theeliminationof pages 1-2) | Franco et al. 2024, *PLOS Neglected Tropical Diseases* | https://doi.org/10.1371/journal.pntd.0012111 |
| Gambiense moderate-or-higher risk area | 58,221 km² | 2018–2022 | 91% reduction versus 2000–2004 baseline (franco2024theeliminationof pages 9-11) | Franco et al. 2024, *PLOS Neglected Tropical Diseases* | https://doi.org/10.1371/journal.pntd.0012111 |
| Rhodesiense moderate-or-higher risk area | 14,913 km² | 2018–2022 | 46% reduction versus 2000–2004 baseline (franco2024theeliminationof pages 9-11) | Franco et al. 2024, *PLOS Neglected Tropical Diseases* | https://doi.org/10.1371/journal.pntd.0012111 |
| Countries validated for elimination as a public health problem | 7 countries | Status by 2022 / reported in 2024 review | Gambiense: Côte d’Ivoire, Togo, Benin, Uganda, Equatorial Guinea, Ghana; Rhodesiense: Rwanda (franco2024theeliminationof pages 11-13, franco2024theeliminationof pages 13-15) | Franco et al. 2024, *PLOS Neglected Tropical Diseases* | https://doi.org/10.1371/journal.pntd.0012111 |
| Formerly endemic countries validated | 7 of 36 | As of June 2023 stakeholder review | Barrett et al. summarize WHO validation count and criterion of <1 per 10,000 in all health districts over previous 5 years (barrett2024eliminationofhuman pages 1-2) | Barrett et al. 2024, *PLOS Neglected Tropical Diseases* | https://doi.org/10.1371/journal.pntd.0012091 |


*Table: This table compiles the main recent epidemiology, surveillance, risk-area, and elimination-validation metrics for human African trypanosomiasis reported in Franco et al. 2024 and contextualized by Barrett et al. 2024. It is useful as a quick reference for populating disease knowledge base fields with quantitative, source-linked values.*

| Therapy | Form / typical regimen | Main indication(s) | Key efficacy outcomes supported by evidence | Major safety / implementation notes | Key supporting publication(s) |
|---|---|---|---|---|---|
| Fexinidazole | Oral 10-day regimen with food; adults ≥35 kg: 1800 mg once daily on days 1–4, then 1200 mg once daily on days 5–10; weight-based lower dosing for 20–<35 kg (neau2020innovativepartnershipsfor pages 5-8, deeks2019fexinidazoleinhuman pages 2-4) | **gambiense HAT (gHAT)**; first-stage and non-severe second-stage, especially CSF WBC <100/µL; can avoid routine lumbar puncture when severe stage 2 is not clinically suspected (lindner2020newwhoguidelines pages 2-4, lindner2020newwhoguidelines pages 1-2) | Late-stage randomized trial: 18-month success **91.2%** vs **97.6%** with NECT; difference **-6.42%** (97.06% CI -11.22 to -1.61), within the prespecified non-inferiority margin of -13% (mesu2018oralfexinidazolefor pages 1-2, mesu2018oralfexinidazolefor pages 6-7). Stage 1 / early stage 2 cohort: **227/230 (99%)** at 12 months and **225/230 (98%)** at 18 months (mesu2021oralfexinidazolefor pages 1-2). Severe stage 2 (CSF WBC ≥100/µL) had higher failure than NECT: **13.1%** vs **1.3%**; with CSF <100/µL failure **2.0%** vs **4.1%** (lindner2020newwhoguidelines pages 2-4). | Adverse events common in both arms; treatment-related AEs **81%** with fexinidazole vs **79%** with NECT in pivotal trial (mesu2018oralfexinidazolefor pages 1-2). Common AEs include vomiting, nausea, asthenia, headache, insomnia, tremor; serious AEs were similar to NECT in guideline review (deeks2019fexinidazoleinhuman pages 4-5, lindner2020newwhoguidelines pages 2-4). Requires reliable food intake and adherence; outpatient use possible only in selected patients (lindner2020newwhoguidelines pages 2-4, neau2020innovativepartnershipsfor pages 5-8). | Mesu et al. 2018, *The Lancet*, https://doi.org/10.1016/S0140-6736(17)32758-7; Mesu et al. 2021, *Lancet Global Health*, https://doi.org/10.1016/S2214-109X(21)00208-4; Lindner et al. 2020, *Lancet Infectious Diseases*, https://doi.org/10.1016/S1473-3099(19)30612-7 (mesu2021oralfexinidazolefor pages 1-2, lindner2020newwhoguidelines pages 2-4, mesu2018oralfexinidazolefor pages 1-2) |
| NECT (nifurtimox–eflornithine combination therapy) | Oral nifurtimox + IV eflornithine; examples: eflornithine 400 mg/kg/day every 12 h for 7 days plus nifurtimox 15 mg/kg/day for 10 days (priotto2007nifurtimoxeflornithinecombinationtherapy pages 1-2, kansiime2018amulticentrerandomised pages 1-2) | **gHAT**, mainly second-stage / late-stage; preferred over fexinidazole for severe stage 2 (CSF WBC ≥100/µL) (lindner2020newwhoguidelines pages 2-4, kansiime2018amulticentrerandomised pages 1-2) | RCT in Congo: cure **96.2%** with NECT vs **94.1%** with eflornithine monotherapy at 18 months (priotto2007nifurtimoxeflornithinecombinationtherapy pages 1-2). Uganda non-inferiority trial: cure **90.9%** vs **88.9%** (NECT vs eflornithine) in ITT/mITT; PP **90.6%** vs **88.5%** (kansiime2018amulticentrerandomised pages 1-2). Field study: **619/629 (98.4%)** discharged alive; 24-month mITT cure **94.1%** (95% CI 91.8–95.7) (kuemmerle2021effectivenessofnifurtimox pages 7-8). | Field pharmacovigilance across 1,735 treated patients: ≥1 AE in **60.1%**, serious AEs **1.1%**, case-fatality **0.5%**; common AEs were gastrointestinal, headache, musculoskeletal pain, vertigo (franco2012monitoringtheuse pages 1-2). In field trial, AEs during treatment were very common (**91.9%–92%**); severe AEs **12.6%** in one report (mordt2015nifurtimoxeflornithinecombination pages 1-1). Logistically burdensome because it requires IV administration and hospitalization, but safer/simpler than eflornithine monotherapy and less toxic than melarsoprol (franco2012monitoringtheuse pages 1-2, schmid2012inhospitalsafetyin pages 2-3). | Priotto et al. 2007, *Clinical Infectious Diseases*, https://doi.org/10.1086/522982; Kansiime et al. 2018, *Parasites & Vectors*, https://doi.org/10.1186/s13071-018-2634-x; Schmid et al. 2012, *PLOS Neglected Tropical Diseases*, https://doi.org/10.1371/journal.pntd.0001920; Franco et al. 2012, *Research and Reports in Tropical Medicine*, https://doi.org/10.2147/RRTM.S34399 (franco2012monitoringtheuse pages 1-2, priotto2007nifurtimoxeflornithinecombinationtherapy pages 1-2, kansiime2018amulticentrerandomised pages 1-2, schmid2012inhospitalsafetyin pages 2-3) |
| Acoziborole | Single oral **960 mg** dose in fasting state in phase 2/3 trial (kumeso2023efficacyandsafety pages 1-2, kumeso2023efficacyandsafety pages 4-4) | **Emerging therapy for gHAT**, intended for both early/intermediate and late stage; stage-independent single-dose strategy under evaluation, including seropositive screen-and-treat approaches (kumeso2023efficacyandsafety pages 1-2, nicco2025thestroghatstudy pages 4-5) | Phase 2/3 single-arm trial: late-stage treatment success **159/167 (95.2%)** in ITT and **159/162 (98.1%)** in evaluable population at 18 months; early/intermediate-stage **41/41 (100%)** at 18 months (kumeso2023efficacyandsafety pages 6-7, kumeso2023efficacyandsafety pages 1-2, nicco2025thestroghatstudy pages 4-5). | No substantial drug-related safety signals reported; TEAEs in **29/208 (14%)**, all mild/moderate and mainly on days 1–5; most frequent drug-related TEAEs were pyrexia **10/208 (5%)** and asthenia **6/208 (3%)** (kumeso2023efficacyandsafety pages 6-7). Serious TEAEs occurred in **21/208 (10%)** but were not considered drug-related; 4 deaths were judged unrelated to treatment/HAT (kumeso2023efficacyandsafety pages 6-7). Remains emerging / under further study (e.g., NCT03087955, NCT05256017, NCT06356974) (nicco2025thestroghatstudy pages 4-5, NCT03087955 chunk 3). | Kumeso et al. 2023, *Lancet Infectious Diseases*, https://doi.org/10.1016/S1473-3099(22)00660-0; NCT03087955; Nicco et al. 2025 protocol, *Open Research Europe*, https://doi.org/10.12688/openreseurope.19077.1 (kumeso2023efficacyandsafety pages 6-7, nicco2025thestroghatstudy pages 4-5, NCT03087955 chunk 3) |
| Pentamidine | Parenteral legacy therapy; exact regimen not provided in retrieved snippets | Legacy first-stage therapy for **gHAT**; largely displaced by fexinidazole in updated WHO guidance where feasible (lindner2020newwhoguidelines pages 1-2) | No head-to-head modern randomized trial versus fexinidazole in provided evidence. Historical comparator data cited in WHO guidance show treatment failure around **3.9–4.6%** (lindner2020newwhoguidelines pages 1-2). In 2021–2022 program data, **305/1,473 (20.71%)** gambiense cases received pentamidine (franco2024theeliminationof pages 11-13). | Main adverse effects highlighted in guideline review are **hypotension** and injection-site effects; use persists where fexinidazole is unsuitable (e.g., young children / low weight) (lindner2020newwhoguidelines pages 1-2). Parenteral administration is a limitation versus oral fexinidazole (mesu2021oralfexinidazolefor pages 1-2, lindner2020newwhoguidelines pages 1-2). | Lindner et al. 2020, *Lancet Infectious Diseases*, https://doi.org/10.1016/S1473-3099(19)30612-7; Franco et al. 2024, *PLOS Neglected Tropical Diseases*, https://doi.org/10.1371/journal.pntd.0012111 (franco2024theeliminationof pages 11-13, lindner2020newwhoguidelines pages 1-2) |
| Suramin | Parenteral legacy therapy; exact regimen not provided in retrieved snippets | Legacy first-stage therapy for **rhodesiense HAT (rHAT)** (franco2024theeliminationof pages 11-13, franco2024theeliminationof pages 2-4) | No trial efficacy numbers were provided in retrieved evidence snippets. In 2021–2022 program data, **26/97 (26.8%)** treated rHAT cases received suramin (franco2024theeliminationof pages 11-13). | Legacy injectable therapy; remains part of stage-specific rHAT treatment paradigm because simpler oral evidence has historically been limited (franco2024theeliminationof pages 2-4, barrett2025transformingthechemotherapy pages 1-2). | Franco et al. 2024, *PLOS Neglected Tropical Diseases*, https://doi.org/10.1371/journal.pntd.0012111; Barrett 2025, *Clinical Microbiology Reviews*, https://doi.org/10.1128/cmr.00153-23 (franco2024theeliminationof pages 11-13, barrett2025transformingthechemotherapy pages 1-2) |
| Melarsoprol | Parenteral arsenical legacy therapy; exact regimen not provided in retrieved snippets | Legacy second-stage therapy for **rHAT** and formerly used in advanced HAT more broadly (franco2024theeliminationof pages 11-13, barrett2025transformingthechemotherapy pages 1-2) | No efficacy numbers were provided in retrieved snippets. In 2021–2022 program data, **60/97 (61.86%)** treated rHAT cases received melarsoprol (franco2024theeliminationof pages 11-13). | Major limitation is toxicity: Barrett et al. note melarsoprol "can kill up to **5%** of patients" (barrett2024eliminationofhuman pages 1-2). Also described as highly toxic and historically problematic, motivating replacement by safer regimens where possible (franco2012monitoringtheuse pages 1-2, barrett2025transformingthechemotherapy pages 1-2). | Barrett et al. 2024, *PLOS Neglected Tropical Diseases*, https://doi.org/10.1371/journal.pntd.0012091; Franco et al. 2024, *PLOS Neglected Tropical Diseases*, https://doi.org/10.1371/journal.pntd.0012111 (franco2024theeliminationof pages 11-13, barrett2024eliminationofhuman pages 1-2) |


*Table: This table summarizes the main current, legacy, and emerging therapies for human African trypanosomiasis, separating evidence-backed indications, outcomes, and safety constraints. It is useful for comparing how oral regimens like fexinidazole and acoziborole contrast with NECT and older injectable therapies in current practice and elimination planning.*

---

## Key quantitative evidence highlights (selected)
- **Cases:** 802 (2021) and 837 (2022); 94% gambiense. (franco2024theeliminationof pages 1-2)
- **Screening:** 3,599,039 actively screened (2021–2022); 900,407 passively screened for gambiense serology (2021–2022). (franco2024theeliminationof pages 9-11)
- **Risk population:** 41.5 million at risk (2018–2022), with 1.5 million at moderate+ risk. (franco2024theeliminationof pages 9-11)
- **Dermal reservoir:** dermal parasites detected up to 71% of confirmed gHAT and 41% of seropositive unconfirmed in one Guinea cohort. (soumah2024prevalenceofdermal pages 1-2)
- **Key trial outcomes:** fexinidazole 91% vs NECT 98% success at 18 months in late-stage gHAT RCT; acoziborole late-stage success 95.2% (ITT) at 18 months. (mesu2018oralfexinidazolefor pages 1-2, kumeso2023efficacyandsafety pages 1-2)

---

## Limitations of this run
- ICD‑10/ICD‑11, MONDO, and Orphanet identifiers were not captured in the retrieved evidence and therefore are not provided as verified, citable codes in this report. (NCT03087955 chunk 3, lindner2020newwhoguidelines pages 1-2)
- Several sections in the template (e.g., detailed differential diagnosis lists, formal QoL instruments and frequencies for many phenotypes, comprehensive biomarker performance statistics) would require additional targeted retrieval beyond the available corpus.


References

1. (franco2024theeliminationof pages 2-4): Jose R. Franco, Gerardo Priotto, Massimo Paone, Giuliano Cecchi, Agustin Kadima Ebeja, Pere P. Simarro, Dieudonne Sankara, Samia B. A. Metwally, and Daniel Dagne Argaw. The elimination of human african trypanosomiasis: monitoring progress towards the 2021–2030 who road map targets. PLOS Neglected Tropical Diseases, 18:e0012111, Apr 2024. URL: https://doi.org/10.1371/journal.pntd.0012111, doi:10.1371/journal.pntd.0012111. This article has 68 citations and is from a domain leading peer-reviewed journal.

2. (barrett2025transformingthechemotherapy pages 2-4): Michael P. Barrett. Transforming the chemotherapy of human african trypanosomiasis. Clinical Microbiology Reviews, Jan 2025. URL: https://doi.org/10.1128/cmr.00153-23, doi:10.1128/cmr.00153-23. This article has 18 citations and is from a highest quality peer-reviewed journal.

3. (NCT03087955 chunk 3):  Efficacy and Safety of Acoziborole (SCYX-7158) in Patients With Human African Trypanosomiasis Due to T.b. Gambiense. Drugs for Neglected Diseases. 2016. ClinicalTrials.gov Identifier: NCT03087955

4. (NCT05256017 chunk 3):  Safety and Tolerability Study of Acoziborole in g-HAT Seropositive Subjects. Drugs for Neglected Diseases. 2021. ClinicalTrials.gov Identifier: NCT05256017

5. (lindner2020newwhoguidelines pages 1-2): Andreas K Lindner, Veerle Lejon, François Chappuis, Jorge Seixas, Leon Kazumba, Michael P Barrett, Erick Mwamba, Olema Erphas, Elie A Akl, Gemma Villanueva, Hanna Bergman, Pere Simarro, Augustin Kadima Ebeja, Gerardo Priotto, and Jose Ramon Franco. New who guidelines for treatment of gambiense human african trypanosomiasis including fexinidazole: substantial changes for clinical practice. The Lancet Infectious Diseases, 20:e38-e46, Feb 2020. URL: https://doi.org/10.1016/s1473-3099(19)30612-7, doi:10.1016/s1473-3099(19)30612-7. This article has 176 citations and is from a highest quality peer-reviewed journal.

6. (barrett2025transformingthechemotherapy pages 1-2): Michael P. Barrett. Transforming the chemotherapy of human african trypanosomiasis. Clinical Microbiology Reviews, Jan 2025. URL: https://doi.org/10.1128/cmr.00153-23, doi:10.1128/cmr.00153-23. This article has 18 citations and is from a highest quality peer-reviewed journal.

7. (imran2022discoverydevelopmentinventions pages 9-11): Mohd Imran, Shah Alam Khan, Mohammed Kanan Alshammari, Ashwaq Muiedh Alqahtani, Turkiah Abdullah Alanazi, Mehnaz Kamal, Talha Jawaid, Mohammed M. Ghoneim, Sultan Alshehri, and Faiyaz Shakeel. Discovery, development, inventions and patent review of fexinidazole: the first all-oral therapy for human african trypanosomiasis. Pharmaceuticals, 15:128, Jan 2022. URL: https://doi.org/10.3390/ph15020128, doi:10.3390/ph15020128. This article has 42 citations.

8. (barrett2024eliminationofhuman pages 1-2): Michael P. Barrett, Gerardo Priotto, Jose R. Franco, Veerle Lejon, and Andreas K. Lindner. Elimination of human african trypanosomiasis: the long last mile. PLOS Neglected Tropical Diseases, 18:e0012091, May 2024. URL: https://doi.org/10.1371/journal.pntd.0012091, doi:10.1371/journal.pntd.0012091. This article has 15 citations and is from a domain leading peer-reviewed journal.

9. (franco2024theeliminationof pages 1-2): Jose R. Franco, Gerardo Priotto, Massimo Paone, Giuliano Cecchi, Agustin Kadima Ebeja, Pere P. Simarro, Dieudonne Sankara, Samia B. A. Metwally, and Daniel Dagne Argaw. The elimination of human african trypanosomiasis: monitoring progress towards the 2021–2030 who road map targets. PLOS Neglected Tropical Diseases, 18:e0012111, Apr 2024. URL: https://doi.org/10.1371/journal.pntd.0012111, doi:10.1371/journal.pntd.0012111. This article has 68 citations and is from a domain leading peer-reviewed journal.

10. (franco2024theeliminationof pages 9-11): Jose R. Franco, Gerardo Priotto, Massimo Paone, Giuliano Cecchi, Agustin Kadima Ebeja, Pere P. Simarro, Dieudonne Sankara, Samia B. A. Metwally, and Daniel Dagne Argaw. The elimination of human african trypanosomiasis: monitoring progress towards the 2021–2030 who road map targets. PLOS Neglected Tropical Diseases, 18:e0012111, Apr 2024. URL: https://doi.org/10.1371/journal.pntd.0012111, doi:10.1371/journal.pntd.0012111. This article has 68 citations and is from a domain leading peer-reviewed journal.

11. (cooper2017apol1renalrisk pages 4-5): Anneli Cooper, Hamidou Ilboudo, V Pius Alibu, Sophie Ravel, John Enyaru, William Weir, Harry Noyes, Paul Capewell, Mamadou Camara, Jacqueline Milet, Vincent Jamonneau, Oumou Camara, Enock Matovu, Bruno Bucheton, and Annette MacLeod. Apol1 renal risk variants have contrasting resistance and susceptibility associations with african trypanosomiasis. eLife, May 2017. URL: https://doi.org/10.7554/elife.25461, doi:10.7554/elife.25461. This article has 153 citations and is from a domain leading peer-reviewed journal.

12. (kamoto2019associationofapol1 pages 6-7): Kelita Kamoto, Harry Noyes, Peter Nambala, Edward Senga, Janelisa Musaya, Benjamin Kumwenda, Bruno Bucheton, Annette Macleod, Anneli Cooper, Caroline Clucas, Christiane Herz-Fowler, Enock Matove, Arthur M. Chiwaya, and John E. Chisi. Association of apol1 renal disease risk alleles with trypanosoma brucei rhodesiense infection outcomes in the northern part of malawi. PLOS Neglected Tropical Diseases, 13:e0007603, Aug 2019. URL: https://doi.org/10.1371/journal.pntd.0007603, doi:10.1371/journal.pntd.0007603. This article has 17 citations and is from a domain leading peer-reviewed journal.

13. (cuypers2016apolipoproteinl1variant pages 1-2): Bart Cuypers, Laurence Lecordier, Conor J. Meehan, Frederik Van den Broeck, Hideo Imamura, Philippe Büscher, Jean-Claude Dujardin, Kris Laukens, Achim Schnaufer, Caroline Dewar, Michael Lewis, Oliver Balmer, Thomas Azurago, Sardick Kyei-Faried, Sally-Ann Ohene, Boateng Duah, Prince Homiah, Ebenezer Kofi Mensah, Francis Anleah, Jose Ramon Franco, Etienne Pays, and Stijn Deborggraeve. Apolipoprotein l1 variant associated with increased susceptibility to trypanosome infection. mBio, May 2016. URL: https://doi.org/10.1128/mbio.02198-15, doi:10.1128/mbio.02198-15. This article has 39 citations and is from a domain leading peer-reviewed journal.

14. (currier2018decodingthenetwork pages 1-2): Rachel B. Currier, Anneli Cooper, Hollie Burrell-Saward, Annette MacLeod, and Sam Alsford. Decoding the network of trypanosoma brucei proteins that determines sensitivity to apolipoprotein-l1. PLOS Pathogens, 14:e1006855, Jan 2018. URL: https://doi.org/10.1371/journal.ppat.1006855, doi:10.1371/journal.ppat.1006855. This article has 31 citations and is from a highest quality peer-reviewed journal.

15. (mesu2021oralfexinidazolefor pages 1-2): V. Kande Betu Ku Mesu, Wilfried Mutombo Kalonji, Clélia Bardonneau, Olaf Valverde Mordt, Digas Ngolo Tete, S. Blesson, F. Simon, Sophie Delhomme, Sonja Bernhard, Hélène Mahenzi Mbembo, Christian Mpia Moke, Steven Lumeya Vuvu, Junior Mudji E'kitiak, Felix Akwaso Masa, Melchias Mukendi Ilunga, Dieudonné Mpoyi Muamba Nzambi, Tim Mayala Malu, Serge Kapongo Tshilumbwa, Franck Botalema Bolengi, Mathieu Nkieri Matsho, C. Lumbala, B. Scherrer, Nathalie Strub-Wourgaft, and A. Tarral. Oral fexinidazole for stage 1 or early stage 2 african trypanosoma brucei gambiense trypanosomiasis: a prospective, multicentre, open-label, cohort study. The Lancet. Global Health, 9:e999-e1008, Jun 2021. URL: https://doi.org/10.1016/s2214-109x(21)00208-4, doi:10.1016/s2214-109x(21)00208-4. This article has 52 citations.

16. (imran2022discoverydevelopmentinventions pages 1-5): Mohd Imran, Shah Alam Khan, Mohammed Kanan Alshammari, Ashwaq Muiedh Alqahtani, Turkiah Abdullah Alanazi, Mehnaz Kamal, Talha Jawaid, Mohammed M. Ghoneim, Sultan Alshehri, and Faiyaz Shakeel. Discovery, development, inventions and patent review of fexinidazole: the first all-oral therapy for human african trypanosomiasis. Pharmaceuticals, 15:128, Jan 2022. URL: https://doi.org/10.3390/ph15020128, doi:10.3390/ph15020128. This article has 42 citations.

17. (capewell2014normalhumanserum pages 210-212): Paul Capewell, Caroline Clucas, William Weir, Nicola Veitch, and Annette MacLeod. Normal human serum lysis of non-human trypanosomes and resistance of t. b. rhodesiense and t. b. gambiense. ArXiv, pages 139-160, Aug 2014. URL: https://doi.org/10.1007/978-3-7091-1556-5\_6, doi:10.1007/978-3-7091-1556-5\_6. This article has 0 citations.

18. (lindner2020newwhoguidelines pages 2-4): Andreas K Lindner, Veerle Lejon, François Chappuis, Jorge Seixas, Leon Kazumba, Michael P Barrett, Erick Mwamba, Olema Erphas, Elie A Akl, Gemma Villanueva, Hanna Bergman, Pere Simarro, Augustin Kadima Ebeja, Gerardo Priotto, and Jose Ramon Franco. New who guidelines for treatment of gambiense human african trypanosomiasis including fexinidazole: substantial changes for clinical practice. The Lancet Infectious Diseases, 20:e38-e46, Feb 2020. URL: https://doi.org/10.1016/s1473-3099(19)30612-7, doi:10.1016/s1473-3099(19)30612-7. This article has 176 citations and is from a highest quality peer-reviewed journal.

19. (soumah2024prevalenceofdermal pages 7-8): Alseny M’mah Soumah, Mariame Camara, Justin Windingoudi Kaboré, Ibrahim Sadissou, Hamidou Ilboudo, Christelle Travaillé, Oumou Camara, Magali Tichit, Jacques Kaboré, Salimatou Boiro, Aline Crouzols, Jean Marc Tsagmo Ngoune, David Hardy, Aïssata Camara, Vincent Jamonneau, Annette MacLeod, Jean-Mathieu Bart, Mamadou Camara, Bruno Bucheton, and Brice Rotureau. Prevalence of dermal trypanosomes in suspected and confirmed cases of gambiense human african trypanosomiasis in guinea. PLOS Neglected Tropical Diseases, 18:e0012436, Aug 2024. URL: https://doi.org/10.1371/journal.pntd.0012436, doi:10.1371/journal.pntd.0012436. This article has 4 citations and is from a domain leading peer-reviewed journal.

20. (anton2024anextgeneration pages 1-4): Elena Pérez Antón, Annick Dujeancourt-Henry, Brice Rotureau, and Lucy Glover. A next generation crispr diagnostic tool to survey drug resistance in human african trypanosomiasis. MedRxiv, Sep 2024. URL: https://doi.org/10.1101/2024.09.15.24313552, doi:10.1101/2024.09.15.24313552. This article has 3 citations.

21. (franco2024theeliminationof pages 13-15): Jose R. Franco, Gerardo Priotto, Massimo Paone, Giuliano Cecchi, Agustin Kadima Ebeja, Pere P. Simarro, Dieudonne Sankara, Samia B. A. Metwally, and Daniel Dagne Argaw. The elimination of human african trypanosomiasis: monitoring progress towards the 2021–2030 who road map targets. PLOS Neglected Tropical Diseases, 18:e0012111, Apr 2024. URL: https://doi.org/10.1371/journal.pntd.0012111, doi:10.1371/journal.pntd.0012111. This article has 68 citations and is from a domain leading peer-reviewed journal.

22. (soumah2024prevalenceofdermal pages 2-4): Alseny M’mah Soumah, Mariame Camara, Justin Windingoudi Kaboré, Ibrahim Sadissou, Hamidou Ilboudo, Christelle Travaillé, Oumou Camara, Magali Tichit, Jacques Kaboré, Salimatou Boiro, Aline Crouzols, Jean Marc Tsagmo Ngoune, David Hardy, Aïssata Camara, Vincent Jamonneau, Annette MacLeod, Jean-Mathieu Bart, Mamadou Camara, Bruno Bucheton, and Brice Rotureau. Prevalence of dermal trypanosomes in suspected and confirmed cases of gambiense human african trypanosomiasis in guinea. PLOS Neglected Tropical Diseases, 18:e0012436, Aug 2024. URL: https://doi.org/10.1371/journal.pntd.0012436, doi:10.1371/journal.pntd.0012436. This article has 4 citations and is from a domain leading peer-reviewed journal.

23. (soumah2024prevalenceofdermal pages 1-2): Alseny M’mah Soumah, Mariame Camara, Justin Windingoudi Kaboré, Ibrahim Sadissou, Hamidou Ilboudo, Christelle Travaillé, Oumou Camara, Magali Tichit, Jacques Kaboré, Salimatou Boiro, Aline Crouzols, Jean Marc Tsagmo Ngoune, David Hardy, Aïssata Camara, Vincent Jamonneau, Annette MacLeod, Jean-Mathieu Bart, Mamadou Camara, Bruno Bucheton, and Brice Rotureau. Prevalence of dermal trypanosomes in suspected and confirmed cases of gambiense human african trypanosomiasis in guinea. PLOS Neglected Tropical Diseases, 18:e0012436, Aug 2024. URL: https://doi.org/10.1371/journal.pntd.0012436, doi:10.1371/journal.pntd.0012436. This article has 4 citations and is from a domain leading peer-reviewed journal.

24. (franco2024theeliminationof media 72eedba2): Jose R. Franco, Gerardo Priotto, Massimo Paone, Giuliano Cecchi, Agustin Kadima Ebeja, Pere P. Simarro, Dieudonne Sankara, Samia B. A. Metwally, and Daniel Dagne Argaw. The elimination of human african trypanosomiasis: monitoring progress towards the 2021–2030 who road map targets. PLOS Neglected Tropical Diseases, 18:e0012111, Apr 2024. URL: https://doi.org/10.1371/journal.pntd.0012111, doi:10.1371/journal.pntd.0012111. This article has 68 citations and is from a domain leading peer-reviewed journal.

25. (franco2024theeliminationof media 237c981b): Jose R. Franco, Gerardo Priotto, Massimo Paone, Giuliano Cecchi, Agustin Kadima Ebeja, Pere P. Simarro, Dieudonne Sankara, Samia B. A. Metwally, and Daniel Dagne Argaw. The elimination of human african trypanosomiasis: monitoring progress towards the 2021–2030 who road map targets. PLOS Neglected Tropical Diseases, 18:e0012111, Apr 2024. URL: https://doi.org/10.1371/journal.pntd.0012111, doi:10.1371/journal.pntd.0012111. This article has 68 citations and is from a domain leading peer-reviewed journal.

26. (franco2024theeliminationof media 1786e4aa): Jose R. Franco, Gerardo Priotto, Massimo Paone, Giuliano Cecchi, Agustin Kadima Ebeja, Pere P. Simarro, Dieudonne Sankara, Samia B. A. Metwally, and Daniel Dagne Argaw. The elimination of human african trypanosomiasis: monitoring progress towards the 2021–2030 who road map targets. PLOS Neglected Tropical Diseases, 18:e0012111, Apr 2024. URL: https://doi.org/10.1371/journal.pntd.0012111, doi:10.1371/journal.pntd.0012111. This article has 68 citations and is from a domain leading peer-reviewed journal.

27. (franco2024theeliminationof media 65382298): Jose R. Franco, Gerardo Priotto, Massimo Paone, Giuliano Cecchi, Agustin Kadima Ebeja, Pere P. Simarro, Dieudonne Sankara, Samia B. A. Metwally, and Daniel Dagne Argaw. The elimination of human african trypanosomiasis: monitoring progress towards the 2021–2030 who road map targets. PLOS Neglected Tropical Diseases, 18:e0012111, Apr 2024. URL: https://doi.org/10.1371/journal.pntd.0012111, doi:10.1371/journal.pntd.0012111. This article has 68 citations and is from a domain leading peer-reviewed journal.

28. (cooper2017apol1renalrisk pages 1-2): Anneli Cooper, Hamidou Ilboudo, V Pius Alibu, Sophie Ravel, John Enyaru, William Weir, Harry Noyes, Paul Capewell, Mamadou Camara, Jacqueline Milet, Vincent Jamonneau, Oumou Camara, Enock Matovu, Bruno Bucheton, and Annette MacLeod. Apol1 renal risk variants have contrasting resistance and susceptibility associations with african trypanosomiasis. eLife, May 2017. URL: https://doi.org/10.7554/elife.25461, doi:10.7554/elife.25461. This article has 153 citations and is from a domain leading peer-reviewed journal.

29. (soumah2024prevalenceofdermal pages 12-13): Alseny M’mah Soumah, Mariame Camara, Justin Windingoudi Kaboré, Ibrahim Sadissou, Hamidou Ilboudo, Christelle Travaillé, Oumou Camara, Magali Tichit, Jacques Kaboré, Salimatou Boiro, Aline Crouzols, Jean Marc Tsagmo Ngoune, David Hardy, Aïssata Camara, Vincent Jamonneau, Annette MacLeod, Jean-Mathieu Bart, Mamadou Camara, Bruno Bucheton, and Brice Rotureau. Prevalence of dermal trypanosomes in suspected and confirmed cases of gambiense human african trypanosomiasis in guinea. PLOS Neglected Tropical Diseases, 18:e0012436, Aug 2024. URL: https://doi.org/10.1371/journal.pntd.0012436, doi:10.1371/journal.pntd.0012436. This article has 4 citations and is from a domain leading peer-reviewed journal.

30. (mesu2018oralfexinidazolefor pages 1-2): Victor Kande Betu Ku Mesu, Wilfried Mutombo Kalonji, Clélia Bardonneau, Olaf Valverde Mordt, Séverine Blesson, François Simon, Sophie Delhomme, Sonja Bernhard, Willy Kuziena, Jean-Pierre Fina Lubaki, Steven Lumeya Vuvu, Pathou Nganzobo Ngima, Hélène Mahenzi Mbembo, Médard Ilunga, Augustin Kasongo Bonama, Josué Amici Heradi, Jean Louis Lumaliza Solomo, Guylain Mandula, Lewis Kaninda Badibabi, Francis Regongbenga Dama, Papy Kavunga Lukula, Digas Ngolo Tete, Crispin Lumbala, Bruno Scherrer, Nathalie Strub-Wourgaft, and Antoine Tarral. Oral fexinidazole for late-stage african trypanosoma brucei gambiense trypanosomiasis: a pivotal multicentre, randomised, non-inferiority trial. The Lancet, 391:144-154, Jan 2018. URL: https://doi.org/10.1016/s0140-6736(17)32758-7, doi:10.1016/s0140-6736(17)32758-7. This article has 303 citations and is from a highest quality peer-reviewed journal.

31. (priotto2007nifurtimoxeflornithinecombinationtherapy pages 1-2): G. Priotto, S. Kasparian, D. Ngouama, S. Ghorashian, U. Arnold, S. Ghabri, and U. Karunakara. Nifurtimox-eflornithine combination therapy for second-stage trypanosoma brucei gambiense sleeping sickness: a randomized clinical trial in congo. Clinical infectious diseases : an official publication of the Infectious Diseases Society of America, 45 11:1435-42, Dec 2007. URL: https://doi.org/10.1086/522982, doi:10.1086/522982. This article has 175 citations.

32. (franco2012monitoringtheuse pages 1-2): J. Franco, P. Simarro, A. Diarra, José A Ruiz-Postigo, M. Samo, and J. Jannin. Monitoring the use of nifurtimox-eflornithine combination therapy (nect) in the treatment of second stage gambiense human african trypanosomiasis. Research and reports in tropical medicine, 3:93-101, Aug 2012. URL: https://doi.org/10.2147/rrtm.s34399, doi:10.2147/rrtm.s34399. This article has 53 citations.

33. (kumeso2023efficacyandsafety pages 1-2): Victor Kande Betu Kumeso, Wilfried Mutombo Kalonji, Sandra Rembry, Olaf Valverde Mordt, Digas Ngolo Tete, Adeline Prêtre, Sophie Delhomme, Médard Ilunga Wa Kyhi, Mamadou Camara, Julie Catusse, Stefan Schneitter, Morgane Nusbaumer, Erick Mwamba Miaka, Hélène Mahenzi Mbembo, Joseph Makaya Mayawula, Mariame Layba Camara, Félix Akwaso Massa, Lewis Kaninda Badibabi, Augustin Kasongo Bonama, Papy Kavunga Lukula, Sylvain Mutanda Kalonji, Phyll Mariero Philemon, Ricardo Mokilifi Nganyonyi, Hugues Embana Mankiara, André Asuka Akongo Nguba, Vincent Kobo Muanza, Ernest Mulenge Nasandhel, Aimée Fifi Nzeza Bambuwu, Bruno Scherrer, Nathalie Strub-Wourgaft, and Antoine Tarral. Efficacy and safety of acoziborole in patients with human african trypanosomiasis caused by trypanosoma brucei gambiense: a multicentre, open-label, single-arm, phase 2/3 trial. The Lancet Infectious Diseases, 23:463-470, Apr 2023. URL: https://doi.org/10.1016/s1473-3099(22)00660-0, doi:10.1016/s1473-3099(22)00660-0. This article has 84 citations and is from a highest quality peer-reviewed journal.

34. (kumeso2023efficacyandsafety pages 6-7): Victor Kande Betu Kumeso, Wilfried Mutombo Kalonji, Sandra Rembry, Olaf Valverde Mordt, Digas Ngolo Tete, Adeline Prêtre, Sophie Delhomme, Médard Ilunga Wa Kyhi, Mamadou Camara, Julie Catusse, Stefan Schneitter, Morgane Nusbaumer, Erick Mwamba Miaka, Hélène Mahenzi Mbembo, Joseph Makaya Mayawula, Mariame Layba Camara, Félix Akwaso Massa, Lewis Kaninda Badibabi, Augustin Kasongo Bonama, Papy Kavunga Lukula, Sylvain Mutanda Kalonji, Phyll Mariero Philemon, Ricardo Mokilifi Nganyonyi, Hugues Embana Mankiara, André Asuka Akongo Nguba, Vincent Kobo Muanza, Ernest Mulenge Nasandhel, Aimée Fifi Nzeza Bambuwu, Bruno Scherrer, Nathalie Strub-Wourgaft, and Antoine Tarral. Efficacy and safety of acoziborole in patients with human african trypanosomiasis caused by trypanosoma brucei gambiense: a multicentre, open-label, single-arm, phase 2/3 trial. The Lancet Infectious Diseases, 23:463-470, Apr 2023. URL: https://doi.org/10.1016/s1473-3099(22)00660-0, doi:10.1016/s1473-3099(22)00660-0. This article has 84 citations and is from a highest quality peer-reviewed journal.

35. (franco2024theeliminationof pages 11-13): Jose R. Franco, Gerardo Priotto, Massimo Paone, Giuliano Cecchi, Agustin Kadima Ebeja, Pere P. Simarro, Dieudonne Sankara, Samia B. A. Metwally, and Daniel Dagne Argaw. The elimination of human african trypanosomiasis: monitoring progress towards the 2021–2030 who road map targets. PLOS Neglected Tropical Diseases, 18:e0012111, Apr 2024. URL: https://doi.org/10.1371/journal.pntd.0012111, doi:10.1371/journal.pntd.0012111. This article has 68 citations and is from a domain leading peer-reviewed journal.

36. (kamoto2019associationofapol1 pages 1-2): Kelita Kamoto, Harry Noyes, Peter Nambala, Edward Senga, Janelisa Musaya, Benjamin Kumwenda, Bruno Bucheton, Annette Macleod, Anneli Cooper, Caroline Clucas, Christiane Herz-Fowler, Enock Matove, Arthur M. Chiwaya, and John E. Chisi. Association of apol1 renal disease risk alleles with trypanosoma brucei rhodesiense infection outcomes in the northern part of malawi. PLOS Neglected Tropical Diseases, 13:e0007603, Aug 2019. URL: https://doi.org/10.1371/journal.pntd.0007603, doi:10.1371/journal.pntd.0007603. This article has 17 citations and is from a domain leading peer-reviewed journal.

37. (capewell2014normalhumanserum pages 146-149): Paul Capewell, Caroline Clucas, William Weir, Nicola Veitch, and Annette MacLeod. Normal human serum lysis of non-human trypanosomes and resistance of t. b. rhodesiense and t. b. gambiense. ArXiv, pages 139-160, Aug 2014. URL: https://doi.org/10.1007/978-3-7091-1556-5\_6, doi:10.1007/978-3-7091-1556-5\_6. This article has 0 citations.

38. (chukwudi2025prevalenceofhuman pages 1-2): Chinwe Chukwudi, Elizabeth Odebunmi, and Chukwuemeka Ibeachu. Prevalence of human and animal african trypanosomiasis in nigeria: a scoping review. Parasitologia, 5:53, Oct 2025. URL: https://doi.org/10.3390/parasitologia5040053, doi:10.3390/parasitologia5040053. This article has 2 citations.

39. (odebunmi2024prevalenceofhuman pages 1-4): Elizabeth O. Odebunmi, Chukwuemeka Ibeachu, and Chinwe U. Chukwudi. Prevalence of human and animal african trypanosomiasis in nigeria: a scoping review. MedRxiv, Apr 2024. URL: https://doi.org/10.1101/2024.04.21.24306055, doi:10.1101/2024.04.21.24306055. This article has 0 citations.

40. (fontaine2017apolswithlow pages 1-2): Frédéric Fontaine, Laurence Lecordier, Gilles Vanwalleghem, Pierrick Uzureau, Nick Van Reet, Martina Fontaine, Patricia Tebabi, Benoit Vanhollebeke, Philippe Büscher, David Pérez-Morga, and Etienne Pays. Apols with low ph dependence can kill all african trypanosomes. Nature Microbiology, 2:1500-1506, Sep 2017. URL: https://doi.org/10.1038/s41564-017-0034-1, doi:10.1038/s41564-017-0034-1. This article has 39 citations and is from a highest quality peer-reviewed journal.

41. (cooper2016aprimateapol1 pages 1-2): Anneli Cooper, Paul Capewell, Caroline Clucas, Nicola Veitch, William Weir, Russell Thomson, Jayne Raper, and Annette MacLeod. A primate apol1 variant that kills trypanosoma brucei gambiense. PLOS Neglected Tropical Diseases, 10:e0004903, Aug 2016. URL: https://doi.org/10.1371/journal.pntd.0004903, doi:10.1371/journal.pntd.0004903. This article has 36 citations and is from a domain leading peer-reviewed journal.

42. (mariotti2025useoffexinidazole pages 11-11): Francesca Mariotti, Riccardo Paggi, Matteo Basilico, Sofia Pettenuzzo, Grant Sebit Benson, Abiodun Amodu, Lorenzo Zammarchi, Stefano Rusconi, Chiara Scanagatta, Giovanni Putoto, Stefano Dacquino, and Elena Gelormino. Use of fexinidazole in gambiense human african trypanosomiasis: a retrospective analysis of cases treated in lui hospital, south sudan (2018–2024). Infection, 53:2847-2857, Sep 2025. URL: https://doi.org/10.1007/s15010-025-02633-6, doi:10.1007/s15010-025-02633-6. This article has 0 citations and is from a peer-reviewed journal.

43. (n’djetchi2025dermaltrypanosomesin pages 12-12): Martial Kassi N’Djetchi, Mélika Barkissa Traoré, Innocent Abé, Bamoro Coulibaly, Valentin Nanan, Thomas Konan, Louis N’Dri, Ibrahim Sadissou, Jean-Mathieu Bart, Bruno Bucheton, Magali Tichit, David Hardy, Salimatou Boiro, Aïssata Camara, Christelle Travaillé, Aline Crouzols, Nathalie Petiot, Adeline Ségard, Lingue Kouakou, Mariame Camara, Mamadou Camara, Dramane Kaba, Mathurin Koffi, Vincent Jamonneau, and Brice Rotureau. Dermal trypanosomes in seropositive suspects of gambiense human african trypanosomiasis in côte d’ivoire. PLOS Neglected Tropical Diseases, 19:e0013027, Aug 2025. URL: https://doi.org/10.1371/journal.pntd.0013027, doi:10.1371/journal.pntd.0013027. This article has 1 citations and is from a domain leading peer-reviewed journal.

44. (franco2024theeliminationof pages 5-7): Jose R. Franco, Gerardo Priotto, Massimo Paone, Giuliano Cecchi, Agustin Kadima Ebeja, Pere P. Simarro, Dieudonne Sankara, Samia B. A. Metwally, and Daniel Dagne Argaw. The elimination of human african trypanosomiasis: monitoring progress towards the 2021–2030 who road map targets. PLOS Neglected Tropical Diseases, 18:e0012111, Apr 2024. URL: https://doi.org/10.1371/journal.pntd.0012111, doi:10.1371/journal.pntd.0012111. This article has 68 citations and is from a domain leading peer-reviewed journal.

45. (neau2020innovativepartnershipsfor pages 5-8): Philippe Neau, Heinz Hänel, Valérie Lameyre, Nathalie Strub-Wourgaft, and Luc Kuykens. Innovative partnerships for the elimination of human african trypanosomiasis and the development of fexinidazole. Tropical Medicine and Infectious Disease, 5:17, Jan 2020. URL: https://doi.org/10.3390/tropicalmed5010017, doi:10.3390/tropicalmed5010017. This article has 45 citations.

46. (deeks2019fexinidazoleinhuman pages 2-4): Emma D. Deeks and Katherine A. Lyseng-Williamson. Fexinidazole in human african trypanosomiasis: a profile of its use. Drugs & Therapy Perspectives, 35:529-535, Sep 2019. URL: https://doi.org/10.1007/s40267-019-00672-2, doi:10.1007/s40267-019-00672-2. This article has 9 citations and is from a peer-reviewed journal.

47. (mesu2018oralfexinidazolefor pages 6-7): Victor Kande Betu Ku Mesu, Wilfried Mutombo Kalonji, Clélia Bardonneau, Olaf Valverde Mordt, Séverine Blesson, François Simon, Sophie Delhomme, Sonja Bernhard, Willy Kuziena, Jean-Pierre Fina Lubaki, Steven Lumeya Vuvu, Pathou Nganzobo Ngima, Hélène Mahenzi Mbembo, Médard Ilunga, Augustin Kasongo Bonama, Josué Amici Heradi, Jean Louis Lumaliza Solomo, Guylain Mandula, Lewis Kaninda Badibabi, Francis Regongbenga Dama, Papy Kavunga Lukula, Digas Ngolo Tete, Crispin Lumbala, Bruno Scherrer, Nathalie Strub-Wourgaft, and Antoine Tarral. Oral fexinidazole for late-stage african trypanosoma brucei gambiense trypanosomiasis: a pivotal multicentre, randomised, non-inferiority trial. The Lancet, 391:144-154, Jan 2018. URL: https://doi.org/10.1016/s0140-6736(17)32758-7, doi:10.1016/s0140-6736(17)32758-7. This article has 303 citations and is from a highest quality peer-reviewed journal.

48. (deeks2019fexinidazoleinhuman pages 4-5): Emma D. Deeks and Katherine A. Lyseng-Williamson. Fexinidazole in human african trypanosomiasis: a profile of its use. Drugs & Therapy Perspectives, 35:529-535, Sep 2019. URL: https://doi.org/10.1007/s40267-019-00672-2, doi:10.1007/s40267-019-00672-2. This article has 9 citations and is from a peer-reviewed journal.

49. (kansiime2018amulticentrerandomised pages 1-2): Freddie Kansiime, Seraphine Adibaku, Charles Wamboga, Franklin Idi, Charles Drago Kato, Lawrence Yamuah, Michel Vaillant, Deborah Kioy, Piero Olliaro, and Enock Matovu. A multicentre, randomised, non-inferiority clinical trial comparing a nifurtimox-eflornithine combination to standard eflornithine monotherapy for late stage trypanosoma brucei gambiense human african trypanosomiasis in uganda. Parasites & Vectors, Feb 2018. URL: https://doi.org/10.1186/s13071-018-2634-x, doi:10.1186/s13071-018-2634-x. This article has 51 citations and is from a peer-reviewed journal.

50. (kuemmerle2021effectivenessofnifurtimox pages 7-8): A Kuemmerle, C Schmid, and S Bernhard. Effectiveness of nifurtimox eflornithine combination therapy (nect) in t. b. gambiense second stage sleeping sickness patients in the democratic republic of …. Unknown journal, 2021.

51. (mordt2015nifurtimoxeflornithinecombination pages 1-1): OV Mordt, S Bernhard, S Ghabri, and V Kande. Nifurtimox eflornithine combination therapy phase iiib field trial (nect field): final effectiveness and safety results. Unknown journal, 2015.

52. (schmid2012inhospitalsafetyin pages 2-3): Caecilia Schmid, Andrea Kuemmerle, Johannes Blum, Salah Ghabri, Victor Kande, Wilfried Mutombo, Medard Ilunga, Ismael Lumpungu, Sylvain Mutanda, Pathou Nganzobo, Digas Tete, Nono Mubwa, Mays Kisala, Severine Blesson, and Olaf Valverde Mordt. In-hospital safety in field conditions of nifurtimox eflornithine combination therapy (nect) for t. b. gambiense sleeping sickness. PLoS Neglected Tropical Diseases, 6:e1920, Nov 2012. URL: https://doi.org/10.1371/journal.pntd.0001920, doi:10.1371/journal.pntd.0001920. This article has 55 citations and is from a domain leading peer-reviewed journal.

53. (kumeso2023efficacyandsafety pages 4-4): Victor Kande Betu Kumeso, Wilfried Mutombo Kalonji, Sandra Rembry, Olaf Valverde Mordt, Digas Ngolo Tete, Adeline Prêtre, Sophie Delhomme, Médard Ilunga Wa Kyhi, Mamadou Camara, Julie Catusse, Stefan Schneitter, Morgane Nusbaumer, Erick Mwamba Miaka, Hélène Mahenzi Mbembo, Joseph Makaya Mayawula, Mariame Layba Camara, Félix Akwaso Massa, Lewis Kaninda Badibabi, Augustin Kasongo Bonama, Papy Kavunga Lukula, Sylvain Mutanda Kalonji, Phyll Mariero Philemon, Ricardo Mokilifi Nganyonyi, Hugues Embana Mankiara, André Asuka Akongo Nguba, Vincent Kobo Muanza, Ernest Mulenge Nasandhel, Aimée Fifi Nzeza Bambuwu, Bruno Scherrer, Nathalie Strub-Wourgaft, and Antoine Tarral. Efficacy and safety of acoziborole in patients with human african trypanosomiasis caused by trypanosoma brucei gambiense: a multicentre, open-label, single-arm, phase 2/3 trial. The Lancet Infectious Diseases, 23:463-470, Apr 2023. URL: https://doi.org/10.1016/s1473-3099(22)00660-0, doi:10.1016/s1473-3099(22)00660-0. This article has 84 citations and is from a highest quality peer-reviewed journal.

54. (nicco2025thestroghatstudy pages 4-5): Elena Nicco, Veerle Lejon, Erick Mwamba Miaka, Dieudonné Mumba, Alain Mpanya, Charles Kambo, Digas Ngolo, Wilfried Mutombo, Stéphane Hugonnet, Sandra Rembry, Craig Tipple, Raquel Inocencio Da Luz, Rian Snijders, Catiane Vander Kelen, Stijn Rogé, Nick Van Reet, Antoine Tarral, Paul Verlé, and Epco Hasker. The stroghat study protocol: an intervention study to evaluate safety, effectiveness and feasibility of treating gambiense hat seropositive subjects with acoziborole. Open Research Europe, 5:23, Jan 2025. URL: https://doi.org/10.12688/openreseurope.19077.1, doi:10.12688/openreseurope.19077.1. This article has 7 citations and is from a peer-reviewed journal.
