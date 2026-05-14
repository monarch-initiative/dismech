---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-11T12:38:04.321862'
end_time: '2026-05-11T12:52:13.276499'
duration_seconds: 848.95
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Carney-Stratakis syndrome
  mondo_id: ''
  category: Genetic
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 31
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Carney-Stratakis syndrome
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Carney-Stratakis syndrome** covering all of the
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
- **Disease Name:** Carney-Stratakis syndrome
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Carney-Stratakis syndrome** covering all of the
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


# Carney–Stratakis Syndrome (CSS) — Disease Characteristics Research Report

## 1. Disease information

### Overview / definition
Carney–Stratakis syndrome (CSS) is a rare hereditary tumor-predisposition syndrome defined by the *dyad* of paraganglioma (PGL) and/or pheochromocytoma (PCC) together with gastrointestinal stromal tumor (GIST), typically a KIT/PDGFRA-wildtype, succinate dehydrogenase (SDH)-deficient GIST. (khurana2019paragangliomasincarney–stratakis pages 1-2, pasini2008clinicalandmolecular pages 1-2, lobato2023threecasesof pages 1-2)

**Synonyms / alternative names** include “Carney–Stratakis dyad,” “dyad of paraganglioma and GIST,” and “hereditary GIST–paraganglioma syndrome.” (khurana2019paragangliomasincarney–stratakis pages 1-2, pasini2008clinicalandmolecular pages 1-2)

**Evidence type**: The syndrome definition and genotype–phenotype associations are derived from aggregated disease-level resources (reviews, guidelines) and from small family series/case reports due to rarity. (pasini2008clinicalandmolecular pages 1-2, lobato2023threecasesof pages 1-2)

### Key identifiers (requested: OMIM/Orphanet/ICD/MeSH/MONDO)
Using the available tools in this run, I was not able to directly retrieve authoritative database identifiers (OMIM, Orphanet, MeSH, ICD-10/11, MONDO) for CSS; therefore these identifiers are not reported here to avoid uncited or incorrect mapping.

## 2. Etiology

### Primary causes
**Genetic (germline) SDH complex loss-of-function** is the established cause of classic CSS. Multiple sources describe CSS as autosomal dominant with incomplete penetrance and as being caused by germline heterozygous loss-of-function pathogenic variants in SDH subunit genes, especially **SDHB, SDHC, SDHD**. (pasini2008clinicalandmolecular pages 1-2, lobato2023threecasesof pages 1-2, pasini2008clinicalandmolecular pages 4-6)

*Abstract-supported definition (example quote)*: Lobato et al. state, “Carney-Stratakis syndrome (CSS) is an autosomal dominant rare syndrome, with incomplete penetrance, characterized by the association of paragangliomas and/or pheochromocytomas and gastrointestinal stromal tumors (GISTs).” (lobato2023threecasesof pages 1-2)

### Risk factors
- **Family history / inherited SDHx pathogenic variants** are the main risk factors; CSS cases can still occur with limited family history due to incomplete penetrance and variable expressivity. (khurana2019paragangliomasincarney–stratakis pages 1-2, pasini2008clinicalandmolecular pages 4-6)
- **Parent-of-origin effects** are noted in SDH-related paraganglioma syndromes (especially SDHD) and can obscure family history patterns (more prominent in the broader SDH-PGL literature than in CSS-specific cohorts). (pitsava2021carneytriadcarneystratakis pages 3-4)

### Protective factors / gene–environment interactions
No protective factors or gene–environment interactions specific to CSS were identified in the retrieved sources.

## 3. Phenotypes (clinical spectrum)

### Core phenotypes
CSS manifests as combinations of:
1) **Paragangliomas (PGLs)** and/or **pheochromocytomas (PCCs)**, often multicentric/multifocal. (khurana2019paragangliomasincarney–stratakis pages 1-2, pasini2008clinicalandmolecular pages 1-2)
2) **Gastrointestinal stromal tumors (GISTs)** that are **SDH-deficient** and usually **KIT/PDGFRA-wildtype**; in CSS, GISTs are frequently multifocal and preferentially gastric. (khurana2019paragangliomasincarney–stratakis pages 3-4, pasini2008clinicalandmolecular pages 1-2, khurana2019paragangliomasincarney–stratakis pages 2-3)

Khurana et al. emphasize that CSS has “greater relative frequency of PGL over GISTs,” and that “PGLs in CSS are multicentric and GISTs are multifocal.” (khurana2019paragangliomasincarney–stratakis pages 1-2)

### Phenotype characteristics
- **Age of onset**: CSS and SDH-deficient GISTs are enriched in younger patients; in the landmark CSS genetic series, affected individuals were young (e.g., earlier series average age reported as ~23 years). (pasini2008clinicalandmolecular pages 1-2)
- **GIST anatomy and pathology**: SDH-deficient GISTs are described as predominantly gastric, often epithelioid or mixed morphology, multinodular/plexiform growth, multiple tumors, lymphovascular invasion, and occasional lymph node metastasis. (khurana2019paragangliomasincarney–stratakis pages 3-4, kim2024pathologicdiagnosisand pages 3-4, kim2024pathologicdiagnosisand pages 1-3)
- **PGL/PCC**: PGLs are neuroendocrine tumors of neural crest origin and are commonly in head/neck or retroperitoneal regions; CSS can present with unusual locations (e.g., bladder PGL described in a CSS case report). (shi2022bladderparagangliomagastrointestinal pages 1-2)

### Suggested HPO terms (non-exhaustive)
- Paraganglioma: **HP:0002666**
- Pheochromocytoma: **HP:0002667**
- Gastrointestinal stromal tumor: **HP:0031275** (term name varies by HPO version; use nearest GIST term)
- Gastrointestinal hemorrhage (if present): **HP:0002239**
- Abdominal pain: **HP:0002027**
- Gastrointestinal neoplasm (broad): **HP:0007378**

*Note*: Exact HPO IDs for “GIST” should be verified against the current HPO release when implementing.

## 4. Genetic / molecular information

### Causal genes (CSS)
Classic CSS is most consistently linked to germline loss-of-function variants in:
- **SDHB** (HGNC:10681)
- **SDHC** (HGNC:10682)
- **SDHD** (HGNC:10683)

These genes encode subunits of mitochondrial complex II (SDH), and germline disruption predisposes to the CSS dyad. (pasini2008clinicalandmolecular pages 1-2, lobato2023threecasesof pages 1-2, pasini2008clinicalandmolecular pages 4-6)

**SDHA** is frequently mutated in SDH-deficient GIST overall, but recent review synthesis indicates SDHA germline cases more often present as isolated SDH-deficient GIST rather than classic CSS; co-occurrence with PGL is described as rare. (schipani2023sdhagermlinemutations pages 8-9)

### Pathogenic variants (representative examples)
In the landmark CSS series, Pasini et al. studied 11 patients and reported that in eight (from seven unrelated families) GISTs were caused by germline mutations in SDHB, SDHC, or SDHD, with autosomal-dominant inheritance and incomplete penetrance. (pasini2008clinicalandmolecular pages 1-2)

Reported variants from the Pasini cohort include (examples; not exhaustive):
- **SDHB**: c.72+1G>T, c.423+1G>C, c.45_46insCC, large deletions. (pasini2008clinicalandmolecular pages 4-6, pasini2008clinicalandmolecular pages 1-2)
- **SDHC**: c.43C>T (p.Arg15X), c.405+1G>A (splice), and later a germline SDHC exon 3 deletion reported in a 2023 case series. (pasini2008clinicalandmolecular pages 4-6, lobato2023threecasesof pages 1-2)
- **SDHD**: c.57delG. (pasini2008clinicalandmolecular pages 1-2)

### Inheritance pattern and penetrance
CSS is described as **autosomal dominant with incomplete penetrance**, supported by unaffected mutation carriers in pedigrees (e.g., SDHB/SDHC splice variants inherited from clinically unaffected mothers). (pasini2008clinicalandmolecular pages 4-6, pasini2008clinicalandmolecular pages 1-2, lobato2023threecasesof pages 1-2)

Quantitative penetrance estimates are more available for SDHx carrier cohorts broadly (PPGL predisposition) than for CSS specifically. For example, SDH-related syndromes have subunit-specific penetrance features; one synthesis notes SDHB has lower penetrance but higher metastatic risk, while SDHD often has higher penetrance and head/neck predominance. (pitsava2021carneytriadcarneystratakis pages 3-4)

### Variant type and mechanism
Most CSS variants are consistent with **loss of function** (splice-site, nonsense, frameshift, or large deletion), consistent with tumor-suppressor biology and frequent “second-hit” loss of the wild-type allele (LOH) in tumors. (pasini2008clinicalandmolecular pages 4-6)

## 5. Environmental information
No consistent non-genetic environmental triggers, lifestyle determinants, or infectious agents specific to CSS were identified in the retrieved literature. CSS is primarily genetic. (pasini2008clinicalandmolecular pages 1-2, lobato2023threecasesof pages 1-2)

## 6. Mechanism / pathophysiology

### Core causal chain (from germline SDHx loss to tumors)
1) **Germline SDHx loss-of-function** → reduced SDH (mitochondrial complex II) activity in susceptible tissues. (pasini2008clinicalandmolecular pages 1-2, khurana2019paragangliomasincarney–stratakis pages 2-3)
2) **Succinate accumulation** (oncometabolite) due to impaired conversion of succinate to fumarate. (pitsava2021carneytriadcarneystratakis pages 3-4, khurana2019paragangliomasincarney–stratakis pages 2-3)
3) **Pseudohypoxia**: succinate inhibits prolyl hydroxylases, stabilizing **HIF-1α**, driving hypoxia-like transcriptional programs. (khurana2019paragangliomasincarney–stratakis pages 2-3)
4) **Epigenetic reprogramming**: succinate inhibits TET/JmjC demethylases, promoting DNA/histone hypermethylation and altered differentiation programs. (pitsava2021carneytriadcarneystratakis pages 3-4, khurana2019paragangliomasincarney–stratakis pages 2-3)
5) Downstream signaling changes in SDH-deficient GIST can include VEGF/IGF2 upregulation and activation of PI3K/AKT and MAPK signaling as summarized in a 2024 mini-review. (kim2024pathologicdiagnosisand pages 3-4)

### GO and CL term suggestions (mechanism anchoring)
- GO:0006121 **mitochondrial electron transport, succinate to ubiquinone**
- GO:0006099 **tricarboxylic acid cycle**
- GO:0001666 **response to hypoxia**
- GO:0071559 **response to hypoxia-inducible factor** (or related HIF terms depending on GO version)
- GO:0006325 **chromatin organization**; GO:0043044 **ATP-dependent chromatin remodeling** (as downstream)
- CL (cell types relevant to lesions):
  - Chromaffin cell (adrenal medulla) / paraganglionic cells (CL term mapping should be validated)
  - Interstitial cells of Cajal (cell-of-origin for GIST; CL mapping requires validation)

## 7. Anatomical structures affected

### Primary organs / structures
- **Stomach** (predominant site for SDH-deficient GIST). (khurana2019paragangliomasincarney–stratakis pages 3-4, kim2024pathologicdiagnosisand pages 1-3)
- **Paraganglia** along the paravertebral axis; **adrenal medulla** for PCC. (khurana2019paragangliomasincarney–stratakis pages 1-2, khurana2019paragangliomasincarney–stratakis pages 2-3)

### UBERON term suggestions
- Stomach: **UBERON:0000945**
- Adrenal gland: **UBERON:0002369** (adrenal medulla is a substructure)
- Paraganglion: UBERON mapping should be validated for “paraganglion” specific class

### Subcellular localization
SDH is localized to the **mitochondrial inner membrane** (complex II); dysfunction is therefore a mitochondrial metabolic defect. (khurana2019paragangliomasincarney–stratakis pages 2-3)

## 8. Temporal development

### Onset and course
CSS often presents in **childhood/adolescence/young adulthood**, particularly for SDH-deficient GIST, and can show multifocal tumors and metastatic potential but with variable/indolent clinical courses in some cases. (khurana2019paragangliomasincarney–stratakis pages 3-4, pasini2008clinicalandmolecular pages 1-2)

## 9. Inheritance and population

### Epidemiology
CSS is rare; no robust prevalence/incidence estimates were retrieved in the available texts for this run.

### Sex ratio
Reviews describe CSS as affecting both genders (in contrast to Carney triad, which has female predilection). (pitsava2021carneytriadcarneystratakis pages 3-4)

### Tumor risk statistics (from SDHB carrier surveillance cohorts; not CSS-specific)
A surveillance series summarized in a 2019 SDH-deficient GIST management review reported that among **65 asymptomatic SDHB mutation carriers** undergoing annual abdominal MRI-based surveillance, **25% developed SDHB-related cancers within 6 years**, and **16.6% had an asymptomatic tumor detected on the first surveillance scan**. (neppala2019currentmanagementof pages 6-7)

## 10. Diagnostics

### Pathology and immunohistochemistry
**Loss of SDHB immunohistochemical staining** is a validated surrogate marker of SDH deficiency and helps distinguish SDH-deficient GIST (including CSS-associated tumors) from KIT/PDGFRA-mutant GIST. (gaal2011sdhbimmunohistochemistrya pages 6-8)

A representative example of this real-world diagnostic pattern is shown in Gaal et al. Figure 1 panel (a): a CSS-associated GIST demonstrates **negative SDHB staining in tumor cells**, with endothelial cells serving as internal positive control. (gaal2011sdhbimmunohistochemistrya media 9958076a)

### Molecular testing
- CSS workup commonly includes tumor and germline testing of SDHx genes by **NGS**, with **copy-number analysis (e.g., MLPA)** when sequencing is negative but suspicion remains. A 2023 case series illustrates that NGS/MLPA may be negative in clinically consistent CSS, highlighting genetic heterogeneity and potential underdiagnosis; they also report an SDHC exon 3 deletion not previously reported. (lobato2023threecasesof pages 1-2)
- In CSS-associated tumors, GISTs typically lack common **KIT**/**PDGFRA** driver mutations. (pasini2008clinicalandmolecular pages 1-2)

### Biochemical testing (PPGL)
Biochemical evaluation for catecholamine excess (e.g., plasma metanephrines/normetanephrines) is used in real-world CSS/PCC evaluation and perioperative planning (α-blockade). (lobato2023threecasesof pages 1-2)

### Imaging
Cross-sectional imaging (CT/MRI) and functional imaging (e.g., PET/CT) are used for tumor localization and staging in CSS cases and broader SDHx syndromes. (lobato2023threecasesof pages 1-2, khurana2019paragangliomasincarney–stratakis pages 2-3)

### Differential diagnosis
Key distinctions include:
- **Carney triad** (PGL + GIST + pulmonary chondroma), often associated with SDHC promoter hypermethylation and female predominance, and frequently non-hereditary/mosaic rather than classic autosomal dominant inheritance. (pitsava2021carneytriadcarneystratakis pages 3-4)
- Sporadic KIT/PDGFRA-mutant GIST (typically SDHB-positive by IHC). (gaal2011sdhbimmunohistochemistrya pages 6-8)

## 11. Outcome / prognosis
No CSS-specific survival rates were identified in retrieved sources. SDH-deficient GIST can metastasize (including nodal metastasis) yet may have relatively indolent behavior compared with other GIST subsets, with clinical course varying substantially. (khurana2019paragangliomasincarney–stratakis pages 3-4, kim2024pathologicdiagnosisand pages 3-4)

## 12. Treatment

### Surgical management (current standard)
For localized CSS-associated tumors, **complete surgical resection** is a primary approach, particularly because SDH-deficient GIST is often not responsive to standard KIT-directed tyrosine kinase inhibitors. (shi2022bladderparagangliomagastrointestinal pages 1-2, neppala2019currentmanagementof pages 1-2)

### Systemic therapy considerations
- **Imatinib**: SDH-deficient GISTs are generally described as poorly responsive, which is clinically important in CSS because these tumors are frequently KIT/PDGFRA-wildtype. (khurana2019paragangliomasincarney–stratakis pages 4-4, neppala2019currentmanagementof pages 1-2)
- **Anti-angiogenic TKIs** (e.g., sunitinib, regorafenib, pazopanib) and other systemic options are discussed in reviews for SDH-deficient tumors, but evidence remains limited and often extrapolated from broader SDH-deficient GIST/PPGL experiences. (khurana2019paragangliomasincarney–stratakis pages 3-4, schipani2023sdhagermlinemutations pages 8-9)

### Surveillance / follow-up (real-world implementation)
For completely resected SDH-deficient GIST, a commonly cited follow-up framework includes physical exams and cross-sectional abdominal/pelvic imaging **every 3–6 months for 5 years, then annually**, as summarized in a management review discussing guideline-consistent practices. (neppala2019currentmanagementof pages 6-7)

### Relevant clinical trials
- **Guadecitabine (SGI-110) DNMT inhibitor** for SDH-deficient tumors: Phase II trial **NCT03165721** (ClinicalTrials.gov; first posted 2017; start date 2017-08-16; primary completion 2020-02-24) evaluated guadecitabine in wt/SDH-deficient GIST and SDH-mutant PPGL strata; the study was **terminated due to low accrual**. URL: https://clinicaltrials.gov/study/NCT03165721 (NCT03165721 chunk 1, NCT03165721 chunk 2)
- **Natural history / biospecimen study**: **NCT03739827** (recruiting; sponsor NCI; primary completion 2028-05-31) includes “SDH deficient GIST” and “Paraganglioma,” enrolling germline variant carriers and relatives to collect biospecimens, imaging, and longitudinal clinical data. URL: https://clinicaltrials.gov/study/NCT03739827 (NCT03739827 chunk 1)

### Suggested MAXO terms
- Surgical resection: **MAXO:0000011** (surgery; verify exact child term)
- Genetic counseling: **MAXO:0000075** (verify)
- Tumor surveillance / screening: **MAXO:0000127** (verify)
- α-adrenergic blockade for PCC: MAXO mapping should be validated

## 13. Prevention

Primary prevention is not established for CSS because it is an inherited tumor predisposition syndrome. Secondary/tertiary prevention relies on **genetic counseling**, **cascade testing**, and **surveillance imaging/biochemical monitoring** for early tumor detection and management in SDHx variant carriers. (neppala2019currentmanagementof pages 6-7, lobato2023threecasesof pages 1-2)

## 14. Other species / natural disease
No naturally occurring CSS analog in non-human species was identified in retrieved sources.

## 15. Model organisms
The retrieved sources for this run did not provide explicit descriptions of CSS-specific model organisms (e.g., SDHx mouse models reproducing the dyad phenotype). Mechanistic descriptions strongly implicate mitochondrial metabolism and epigenetic dysregulation in SDH-deficient tumors, but dedicated model-system evidence should be curated from additional experimental literature beyond the documents retrieved here. (pitsava2021carneytriadcarneystratakis pages 3-4, khurana2019paragangliomasincarney–stratakis pages 2-3)

---

## High-level synthesis (2023–2024 emphasis)
Recent case-based and pathology-focused literature reinforces that CSS should be considered when encountering **SDH-deficient, KIT/PDGFRA-wildtype gastric GIST** and/or **PGL/PCC**, and that SDHx testing should include deletion/duplication analysis when sequencing is negative. (lobato2023threecasesof pages 1-2, kim2024pathologicdiagnosisand pages 3-4)

A 2024 mini-review summarizes modern diagnostic practice for molecularly diverse GIST, emphasizing that ancillary testing (IHC, NGS) is essential because some epithelioid/mixed tumors may lose canonical KIT/DOG1 signals, and that SDH-deficient GIST (including CSS-associated) behaves as a distinct subgroup with TKI resistance. (kim2024pathologicdiagnosisand pages 3-4)

---

## Summary table

| Domain | Core fact | Recent source(s) with DOI/URL and publication date | Key evidence source (author-year) |
|---|---|---|---|
| Definition / synonyms | Carney–Stratakis syndrome (CSS) is a rare hereditary tumor-predisposition syndrome defined by the dyad of paraganglioma/pheochromocytoma and gastrointestinal stromal tumor (GIST); synonyms include **Carney–Stratakis dyad**, **dyad of paraganglioma and GIST**, and **hereditary GIST-paraganglioma syndrome**. It is distinct from Carney triad. (khurana2019paragangliomasincarney–stratakis pages 1-2, pasini2008clinicalandmolecular pages 1-2, lobato2023threecasesof pages 1-2) | Lobato et al., *JCEM Case Reports* (Nov 2023), DOI: 10.1210/jcemcr/luad139, https://doi.org/10.1210/jcemcr/luad139; Kim & Lee, *Front Oncol* (Nov 2024), DOI: 10.3389/fonc.2024.1487467, https://doi.org/10.3389/fonc.2024.1487467 | Pasini-2008; Lobato-2023 |
| Causal genes | Canonical causal genes are germline loss-of-function variants in **SDHB, SDHC, and SDHD**; these explain most molecularly confirmed CSS families. **SDHA** is part of the SDH-deficient GIST spectrum, but recent reviews emphasize SDHA more often causes isolated SDH-deficient GIST rather than classic CSS. (pasini2008clinicalandmolecular pages 1-2, schipani2023sdhagermlinemutations pages 8-9, lobato2023threecasesof pages 1-2, pasini2008clinicalandmolecular pages 4-6) | Schipani et al., *Genes* (Mar 2023), DOI: 10.3390/genes14030646, https://doi.org/10.3390/genes14030646; Lobato et al., *JCEM Case Reports* (Nov 2023), DOI: 10.1210/jcemcr/luad139, https://doi.org/10.1210/jcemcr/luad139 | Pasini-2008; Schipani-2023 |
| Representative reported variants | Reported CSS-associated variants include **SDHB c.72+1G>T, c.423+1G>C, c.45_46insCC, large deletions; SDHC c.43C>T, c.405+1G>A, exon 3 deletion; SDHD c.57delG**. Variable family expression and unaffected carriers have been documented. (pasini2008clinicalandmolecular pages 4-6, pasini2008clinicalandmolecular pages 1-2, lobato2023threecasesof pages 1-2) | Lobato et al., *JCEM Case Reports* (Nov 2023), DOI: 10.1210/jcemcr/luad139, https://doi.org/10.1210/jcemcr/luad139 | Pasini-2008; Lobato-2023 |
| Inheritance / penetrance | CSS is generally described as **autosomal dominant with incomplete penetrance** and variable expressivity. Family studies show mutation-positive but clinically unaffected relatives, supporting reduced penetrance. (khurana2019paragangliomasincarney–stratakis pages 1-2, pasini2008clinicalandmolecular pages 1-2, lobato2023threecasesof pages 1-2) | Lobato et al., *JCEM Case Reports* (Nov 2023), DOI: 10.1210/jcemcr/luad139, https://doi.org/10.1210/jcemcr/luad139 | Pasini-2008; Khurana-2019; Lobato-2023 |
| Key tumor types | Hallmark tumors are **paragangliomas/pheochromocytomas (often multicentric/multifocal)** and **SDH-deficient wild-type GISTs (often multifocal, usually gastric)**. PGL may be more frequent than GIST in CSS cohorts/reviews. (shi2022bladderparagangliomagastrointestinal pages 1-2, khurana2019paragangliomasincarney–stratakis pages 1-2, khurana2019paragangliomasincarney–stratakis pages 3-4, lobato2023threecasesof pages 1-2, schipani2023sdhagermlinemutations pages 1-2) | Kim & Lee, *Front Oncol* (Nov 2024), DOI: 10.3389/fonc.2024.1487467, https://doi.org/10.3389/fonc.2024.1487467; Lobato et al., *JCEM Case Reports* (Nov 2023), DOI: 10.1210/jcemcr/luad139, https://doi.org/10.1210/jcemcr/luad139 | Khurana-2019; Shi-2022; Kim-2024 |
| Typical clinicopathologic pattern | CSS-associated GISTs are usually **KIT/PDGFRA-wildtype**, gastric, often epithelioid or mixed, multinodular/plexiform, with lymphovascular invasion and occasional nodal/liver metastases; despite metastatic potential, some cases behave relatively indolently. (khurana2019paragangliomasincarney–stratakis pages 4-4, khurana2019paragangliomasincarney–stratakis pages 3-4, kim2024pathologicdiagnosisand pages 3-4, schipani2023sdhagermlinemutations pages 1-2, kim2024pathologicdiagnosisand pages 1-3) | Kim & Lee, *Front Oncol* (Nov 2024), DOI: 10.3389/fonc.2024.1487467, https://doi.org/10.3389/fonc.2024.1487467; Schipani et al., *Genes* (Mar 2023), DOI: 10.3390/genes14030646, https://doi.org/10.3390/genes14030646 | Khurana-2019; Kim-2024; Schipani-2023 |
| Diagnostic hallmarks | Key hallmarks are **loss of SDHB expression by immunohistochemistry** (marker of SDH deficiency) and **absence of KIT/PDGFRA driver mutations**. SDHA IHC loss can point to SDHA-mutant GIST, while retained SDHB is typical of KIT/PDGFRA-mutant GIST. (khurana2019paragangliomasincarney–stratakis pages 2-3, gaal2011sdhbimmunohistochemistrya pages 6-8, kim2024pathologicdiagnosisand pages 3-4, schipani2023sdhagermlinemutations pages 1-2, gaal2011sdhbimmunohistochemistrya media 9958076a) | Kim & Lee, *Front Oncol* (Nov 2024), DOI: 10.3389/fonc.2024.1487467, https://doi.org/10.3389/fonc.2024.1487467; Schipani et al., *Genes* (Mar 2023), DOI: 10.3390/genes14030646, https://doi.org/10.3390/genes14030646 | Gaal-2011; Kim-2024; Schipani-2023 |
| Mechanistic concepts | SDH loss causes **succinate accumulation**, which inhibits **prolyl hydroxylases** and stabilizes **HIF-1α** (pseudohypoxia), and inhibits **TET/JmjC demethylases**, promoting **global DNA/histone hypermethylation**. These mechanisms help explain CSS tumorigenesis and reduced sensitivity of SDH-deficient GIST to standard KIT-directed therapy. (shi2022bladderparagangliomagastrointestinal pages 1-2, pitsava2021carneytriadcarneystratakis pages 3-4, khurana2019paragangliomasincarney–stratakis pages 2-3, kim2024pathologicdiagnosisand pages 3-4) | Schipani et al., *Genes* (Mar 2023), DOI: 10.3390/genes14030646, https://doi.org/10.3390/genes14030646; Kim & Lee, *Front Oncol* (Nov 2024), DOI: 10.3389/fonc.2024.1487467, https://doi.org/10.3389/fonc.2024.1487467 | Pitsava-2021; Khurana-2019; Kim-2024 |
| Molecular testing / workup | Current practice-oriented reviews and guidelines support **SDHB IHC in wild-type GIST**, followed by **germline SDHx testing** and consideration of copy-number analysis (e.g., **MLPA**) when NGS is negative but clinical suspicion remains high. Ancillary tests may include CT/MRI, PET/CT, catecholamine/metanephrine testing, and pathology review. (neppala2019currentmanagementof pages 6-7, florou2025areviewof pages 4-4, lobato2023threecasesof pages 1-2) | Lobato et al., *JCEM Case Reports* (Nov 2023), DOI: 10.1210/jcemcr/luad139, https://doi.org/10.1210/jcemcr/luad139; Kim & Lee, *Front Oncol* (Nov 2024), DOI: 10.3389/fonc.2024.1487467, https://doi.org/10.3389/fonc.2024.1487467 | Lobato-2023; Kim-2024 |
| Recent clinical relevance (2023–2024) | 2023–2024 literature reinforces that CSS belongs within the **SDH-deficient GIST / PPGL spectrum**, that **imatinib is generally ineffective** in SDH-deficient GIST, and that **genetic counseling/surveillance** are important because syndromic disease may be missed if only tumor sequencing is performed. (schipani2023sdhagermlinemutations pages 8-9, kim2024pathologicdiagnosisand pages 3-4, neppala2019currentmanagementof pages 6-7, lobato2023threecasesof pages 1-2) | Schipani et al., *Genes* (Mar 2023), DOI: 10.3390/genes14030646, https://doi.org/10.3390/genes14030646; Lobato et al., *JCEM Case Reports* (Nov 2023), DOI: 10.1210/jcemcr/luad139, https://doi.org/10.1210/jcemcr/luad139; Kim & Lee, *Front Oncol* (Nov 2024), DOI: 10.3389/fonc.2024.1487467, https://doi.org/10.3389/fonc.2024.1487467 | Schipani-2023; Lobato-2023; Kim-2024 |


*Table: This table condenses the key definitional, genetic, mechanistic, and diagnostic facts about Carney–Stratakis syndrome for rapid knowledge-base entry. It highlights the SDHx basis of the syndrome, classic tumor dyad, hallmark pathology, and the most relevant 2023–2024 sources.*

---

## Key visual evidence

- SDHB-negative immunohistochemistry pattern in CSS-associated GIST (diagnostic hallmark): (gaal2011sdhbimmunohistochemistrya media 9958076a)


References

1. (khurana2019paragangliomasincarney–stratakis pages 1-2): Arushi Khurana, Lin Mei, Anthony C. Faber, Steven C. Smith, and Sosipatros A. Boikos. Paragangliomas in carney–stratakis syndrome. Hormone and Metabolic Research, 51:437-442, Jun 2019. URL: https://doi.org/10.1055/a-0918-8340, doi:10.1055/a-0918-8340. This article has 6 citations and is from a peer-reviewed journal.

2. (pasini2008clinicalandmolecular pages 1-2): Barbara Pasini, Sarah R McWhinney, Thalia Bei, Ludmila Matyakhina, Sotirios Stergiopoulos, Michael Muchow, Sosipatros A Boikos, Barbara Ferrando, Karel Pacak, Guillaume Assie, Eric Baudin, Agnes Chompret, Jay W Ellison, Jean-Jacques Briere, Pierre Rustin, Anne-Paule Gimenez-Roqueplo, Charis Eng, J Aidan Carney, and Constantine A Stratakis. Clinical and molecular genetics of patients with the carney–stratakis syndrome and germline mutations of the genes coding for the succinate dehydrogenase subunits sdhb, sdhc, and sdhd. European Journal of Human Genetics, 16:79-88, Aug 2008. URL: https://doi.org/10.1038/sj.ejhg.5201904, doi:10.1038/sj.ejhg.5201904. This article has 581 citations and is from a domain leading peer-reviewed journal.

3. (lobato2023threecasesof pages 1-2): Eduardo C Lobato, Felipe F Castro, Lucas S Santana, Ibere C Soares, Gustavo F C Fagundes, and Madson Q Almeida. Three cases of carney-stratakis syndrome: a genetically heterogeneous disease. JCEM Case Reports, Nov 2023. URL: https://doi.org/10.1210/jcemcr/luad139, doi:10.1210/jcemcr/luad139. This article has 2 citations.

4. (pasini2008clinicalandmolecular pages 4-6): Barbara Pasini, Sarah R McWhinney, Thalia Bei, Ludmila Matyakhina, Sotirios Stergiopoulos, Michael Muchow, Sosipatros A Boikos, Barbara Ferrando, Karel Pacak, Guillaume Assie, Eric Baudin, Agnes Chompret, Jay W Ellison, Jean-Jacques Briere, Pierre Rustin, Anne-Paule Gimenez-Roqueplo, Charis Eng, J Aidan Carney, and Constantine A Stratakis. Clinical and molecular genetics of patients with the carney–stratakis syndrome and germline mutations of the genes coding for the succinate dehydrogenase subunits sdhb, sdhc, and sdhd. European Journal of Human Genetics, 16:79-88, Aug 2008. URL: https://doi.org/10.1038/sj.ejhg.5201904, doi:10.1038/sj.ejhg.5201904. This article has 581 citations and is from a domain leading peer-reviewed journal.

5. (pitsava2021carneytriadcarneystratakis pages 3-4): Georgia Pitsava, Nikolaos Settas, Fabio R. Faucz, and Constantine A. Stratakis. Carney triad, carney-stratakis syndrome, 3pas and other tumors due to sdh deficiency. Frontiers in Endocrinology, May 2021. URL: https://doi.org/10.3389/fendo.2021.680609, doi:10.3389/fendo.2021.680609. This article has 54 citations.

6. (khurana2019paragangliomasincarney–stratakis pages 3-4): Arushi Khurana, Lin Mei, Anthony C. Faber, Steven C. Smith, and Sosipatros A. Boikos. Paragangliomas in carney–stratakis syndrome. Hormone and Metabolic Research, 51:437-442, Jun 2019. URL: https://doi.org/10.1055/a-0918-8340, doi:10.1055/a-0918-8340. This article has 6 citations and is from a peer-reviewed journal.

7. (khurana2019paragangliomasincarney–stratakis pages 2-3): Arushi Khurana, Lin Mei, Anthony C. Faber, Steven C. Smith, and Sosipatros A. Boikos. Paragangliomas in carney–stratakis syndrome. Hormone and Metabolic Research, 51:437-442, Jun 2019. URL: https://doi.org/10.1055/a-0918-8340, doi:10.1055/a-0918-8340. This article has 6 citations and is from a peer-reviewed journal.

8. (kim2024pathologicdiagnosisand pages 3-4): Younghoon Kim and Sung Hak Lee. Pathologic diagnosis and molecular features of gastrointestinal stromal tumors: a mini-review. Frontiers in Oncology, Nov 2024. URL: https://doi.org/10.3389/fonc.2024.1487467, doi:10.3389/fonc.2024.1487467. This article has 10 citations.

9. (kim2024pathologicdiagnosisand pages 1-3): Younghoon Kim and Sung Hak Lee. Pathologic diagnosis and molecular features of gastrointestinal stromal tumors: a mini-review. Frontiers in Oncology, Nov 2024. URL: https://doi.org/10.3389/fonc.2024.1487467, doi:10.3389/fonc.2024.1487467. This article has 10 citations.

10. (shi2022bladderparagangliomagastrointestinal pages 1-2): Yihang Shi, Li Ding, Chengqiang Mo, Yanji Luo, Shaoqing Huang, Shirong Cai, Yanzhe Xia, and Xinhua Zhang. Bladder paraganglioma, gastrointestinal stromal tumor, and sdhb germline mutation in a patient with carney-stratakis syndrome: a case report and literature review. Frontiers in Oncology, Oct 2022. URL: https://doi.org/10.3389/fonc.2022.1030092, doi:10.3389/fonc.2022.1030092. This article has 6 citations.

11. (schipani2023sdhagermlinemutations pages 8-9): Angela Schipani, Margherita Nannini, Annalisa Astolfi, and Maria A. Pantaleo. Sdha germline mutations in sdh-deficient gists: a current update. Genes, 14:646, Mar 2023. URL: https://doi.org/10.3390/genes14030646, doi:10.3390/genes14030646. This article has 24 citations.

12. (neppala2019currentmanagementof pages 6-7): Pushpa Neppala, Sudeep Banerjee, Paul T. Fanta, Mayra Yerba, Kevin A. Porras, Adam M. Burgoyne, and Jason K. Sicklick. Current management of succinate dehydrogenase–deficient gastrointestinal stromal tumors. Cancer and Metastasis Reviews, 38:525-535, Sep 2019. URL: https://doi.org/10.1007/s10555-019-09818-0, doi:10.1007/s10555-019-09818-0. This article has 62 citations and is from a peer-reviewed journal.

13. (gaal2011sdhbimmunohistochemistrya pages 6-8): José Gaal, Constantine A Stratakis, J Aidan Carney, Evan R Ball, Esther Korpershoek, Maya B Lodish, Isaac Levy, Paraskevi Xekouki, Francien H van Nederveen, Michael A den Bakker, Maureen O'Sullivan, Winand NM Dinjens, and Ronald R de Krijger. Sdhb immunohistochemistry: a useful tool in the diagnosis of carney–stratakis and carney triad gastrointestinal stromal tumors. Modern Pathology, 24:147-151, Jan 2011. URL: https://doi.org/10.1038/modpathol.2010.185, doi:10.1038/modpathol.2010.185. This article has 252 citations and is from a domain leading peer-reviewed journal.

14. (gaal2011sdhbimmunohistochemistrya media 9958076a): José Gaal, Constantine A Stratakis, J Aidan Carney, Evan R Ball, Esther Korpershoek, Maya B Lodish, Isaac Levy, Paraskevi Xekouki, Francien H van Nederveen, Michael A den Bakker, Maureen O'Sullivan, Winand NM Dinjens, and Ronald R de Krijger. Sdhb immunohistochemistry: a useful tool in the diagnosis of carney–stratakis and carney triad gastrointestinal stromal tumors. Modern Pathology, 24:147-151, Jan 2011. URL: https://doi.org/10.1038/modpathol.2010.185, doi:10.1038/modpathol.2010.185. This article has 252 citations and is from a domain leading peer-reviewed journal.

15. (neppala2019currentmanagementof pages 1-2): Pushpa Neppala, Sudeep Banerjee, Paul T. Fanta, Mayra Yerba, Kevin A. Porras, Adam M. Burgoyne, and Jason K. Sicklick. Current management of succinate dehydrogenase–deficient gastrointestinal stromal tumors. Cancer and Metastasis Reviews, 38:525-535, Sep 2019. URL: https://doi.org/10.1007/s10555-019-09818-0, doi:10.1007/s10555-019-09818-0. This article has 62 citations and is from a peer-reviewed journal.

16. (khurana2019paragangliomasincarney–stratakis pages 4-4): Arushi Khurana, Lin Mei, Anthony C. Faber, Steven C. Smith, and Sosipatros A. Boikos. Paragangliomas in carney–stratakis syndrome. Hormone and Metabolic Research, 51:437-442, Jun 2019. URL: https://doi.org/10.1055/a-0918-8340, doi:10.1055/a-0918-8340. This article has 6 citations and is from a peer-reviewed journal.

17. (NCT03165721 chunk 1): John Glod. A Phase II Trial of the DNA Methyl Transferase Inhibitor, Guadecitabine (SGI-110), in Children and Adults With Wild Type GIST,Pheochromocytoma and Paraganglioma Associated With Succinate Dehydrogenase Deficiency and HLRCC-associated Kidney Cancer. National Cancer Institute (NCI). 2017. ClinicalTrials.gov Identifier: NCT03165721

18. (NCT03165721 chunk 2): John Glod. A Phase II Trial of the DNA Methyl Transferase Inhibitor, Guadecitabine (SGI-110), in Children and Adults With Wild Type GIST,Pheochromocytoma and Paraganglioma Associated With Succinate Dehydrogenase Deficiency and HLRCC-associated Kidney Cancer. National Cancer Institute (NCI). 2017. ClinicalTrials.gov Identifier: NCT03165721

19. (NCT03739827 chunk 1):  Natural History and Biospecimen Acquisition for Children and Adults With Rare Solid Tumors. National Cancer Institute (NCI). 2019. ClinicalTrials.gov Identifier: NCT03739827

20. (schipani2023sdhagermlinemutations pages 1-2): Angela Schipani, Margherita Nannini, Annalisa Astolfi, and Maria A. Pantaleo. Sdha germline mutations in sdh-deficient gists: a current update. Genes, 14:646, Mar 2023. URL: https://doi.org/10.3390/genes14030646, doi:10.3390/genes14030646. This article has 24 citations.

21. (florou2025areviewof pages 4-4): Vaia Florou, Michelle F. Jacobs, Ruth Casey, Denisse Evans, Becky Owens, Margarita Raygada, Sara Rothschild, and Samantha E. Greenberg. A review of genomic testing and sdh‐ deficiency in gastrointestinal stromal tumors: getting to the gist. Cancer Medicine, Feb 2025. URL: https://doi.org/10.1002/cam4.70669, doi:10.1002/cam4.70669. This article has 8 citations and is from a peer-reviewed journal.