---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-09T09:26:22.597796'
end_time: '2026-05-09T09:57:54.705915'
duration_seconds: 1892.11
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Central Nervous System Teratoma
  mondo_id: ''
  category: ''
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
- **Disease Name:** Central Nervous System Teratoma
- **MONDO ID:**  (if available)
- **Category:** 

## Research Objectives

Please provide a comprehensive research report on **Central Nervous System Teratoma** covering all of the
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
- **Disease Name:** Central Nervous System Teratoma
- **MONDO ID:**  (if available)
- **Category:** 

## Research Objectives

Please provide a comprehensive research report on **Central Nervous System Teratoma** covering all of the
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


# Central Nervous System Teratoma — Comprehensive Disease Characteristics Report

## Target disease
- **Disease name:** Central nervous system (CNS) teratoma (intracranial and intraspinal)
- **Category:** CNS germ cell tumor; typically classified within **non‑germinomatous germ cell tumors (NGGCT)**, though “teratoma” itself is a distinct histologic entity. (zygourakis2015managementofcentral pages 1-2)
- **MONDO ID / OMIM / Orphanet / MeSH / ICD-10/ICD-11:** Not retrievable with the available tools and evidence in this run; below content is derived from **peer‑reviewed literature and clinical trial/guideline sources** rather than ontology registries.

---

## 1. Disease information
### Overview (current understanding)
A CNS teratoma is a rare tumor arising in the brain or spinal axis composed of tissues derived from **two or more embryonic germ layers** (often all three: ectoderm, mesoderm, endoderm). CNS teratomas are generally categorized into **mature teratoma**, **immature teratoma**, and **malignant teratoma/teratoma with malignant (somatic-like) transformation**, and are part of the broader spectrum of CNS germ cell tumors (GCTs). (zygourakis2015managementofcentral pages 1-2, challa2010teratomasincentral pages 1-2, nowacka2025matureteratomaof pages 5-7)

### Synonyms and alternative names
- Intracranial teratoma; pineal teratoma; suprasellar teratoma; intraventricular teratoma
- Spinal teratoma; intradural teratoma; intramedullary teratoma; mature cystic teratoma of the spine
- “Growing teratoma syndrome” when a mature teratoma component enlarges during/after chemotherapy with normalized tumor markers (see Treatment). (michaiel2020intracranialgrowingteratoma pages 1-2, satake2024successfulmultimodaltreatment pages 1-3)

### Evidence provenance
The evidence used here is primarily **aggregated disease-level resources** (guidelines, multi-institution cohorts, case series) and some **case reports** for rare molecular findings and spinal disease presentations. (nakamura2022thejapansociety pages 7-8, takami2023impactoftumor pages 1-2, giron2024primarycentralnervous pages 1-2, zavalaromero2024matureteratomaat pages 1-2)

---

## 2. Etiology
### Disease causal factors (developmental/mechanistic)
**Embryologic origin hypothesis:** CNS GCTs (including teratoma) are widely considered to arise from **mismigrated primordial germ cells (PGCs)** that become sequestered in midline CNS structures, later undergoing malignant transformation; germinomas and PGCs share global DNA hypomethylation patterns supporting this model. (yeo2023primarycentralnervous pages 1-2, tengattini2024primarycooccurrenceof pages 1-2)

**Spinal teratoma hypotheses:** spinal teratomas are described with two main theories: (1) **dysembryogenic theory** (disordered local development with pluripotent cells differentiating chaotically) and (2) **misplaced germ cell theory** (mis-migration of primordial germ cells from yolk sac to gonad), with some authors considering the misplaced germ cell theory more plausible for adult intraspinal teratomas. (ferdause2023spinalintraduralextramedullary pages 3-3)

### Risk factors
Robust environmental risk factors are not established in the extracted evidence. Reported **syndromic/germline associations** and predispositions include:
- **Down syndrome**, **Klinefelter syndrome**, and **JMJD1C variants** reported in CNS GCT literature. (yeo2023primarycentralnervous pages 2-3)
- Rare clinical observation of **testicular dysgenesis syndrome** and Down syndrome among cases with co‑occurring gonadal and CNS GCTs. (tengattini2024primarycooccurrenceof pages 1-2)
- A **PTEN germline variant** has been reported as a pediatric cancer predisposition in the context of intracranial GCT biology (evidence in a recent iGTS case report discussion). (satake2024successfulmultimodaltreatment pages 5-7)

### Protective factors / Gene–environment interactions
No protective factors or gene–environment interactions specific to CNS teratoma were identified in the retrieved evidence.

---

## 3. Phenotypes
CNS teratoma phenotypes are largely driven by **tumor location**, mass effect, hydrocephalus, and endocrine involvement (suprasellar/hypothalamic–pituitary region). Population-level frequencies are most available for CNS GCT cohorts rather than teratoma-only cohorts.

| Phenotype | Phenotype type | Suggested HPO term | HPO ID | Frequency / count | Typical context / location | Source citation |
|---|---|---|---|---|---|---|
| Headache | Symptom | Headache | HP:0002315 | 24/48 (50.0%) | Common presenting symptom in pediatric CNS GCTs; often associated with pineal/suprasellar mass effect and hydrocephalus | (giron2024primarycentralnervous pages 1-2, giron2024primarycentralnervous pages 2-3) |
| Visual disturbance | Symptom | Abnormality of vision / Visual impairment | HP:0000505 | 17/48 (35.4%) | Frequently reported in suprasellar and pineal region tumors | (giron2024primarycentralnervous pages 1-2, giron2024primarycentralnervous pages 2-3) |
| Vomiting | Symptom | Vomiting | HP:0002013 | 12/48 (25.0%) | Often occurs with raised intracranial pressure or obstructive hydrocephalus | (giron2024primarycentralnervous pages 1-2, giron2024primarycentralnervous pages 2-3) |
| Nausea | Symptom | Nausea | HP:0002018 | 8/48 (16.7%) | Often accompanies increased intracranial pressure | (giron2024primarycentralnervous pages 1-2, giron2024primarycentralnervous pages 2-3) |
| Diabetes insipidus | Endocrine manifestation | Diabetes insipidus | HP:0000873 | 7/48 (14.6%) | Characteristic of suprasellar/hypothalamic-pituitary involvement | (giron2024primarycentralnervous pages 1-2, giron2024primarycentralnervous pages 2-3, yeo2023primarycentralnervous pages 2-3) |
| Precocious puberty | Endocrine manifestation | Precocious puberty | HP:0000826 | 2/48 (4.2%) | Reported in NGGCT patients; may reflect β-hCG secretion | (giron2024primarycentralnervous pages 1-2, giron2024primarycentralnervous pages 2-3) |
| Hydrocephalus | Clinical sign / imaging finding | Hydrocephalus | HP:0000238 | 74/80 | Dominant presenting feature in pediatric pineal region surgical series; especially relevant for pineal tumors | (tomita2023pediatricpinealregion pages 1-2) |
| Parinaud sign / Parinaud syndrome | Clinical sign | Parinaud syndrome | HP:0001108 | 24/80 | Typical of pineal region / dorsal midbrain compression; 16 cases were transient postoperatively in the series | (tomita2023pediatricpinealregion pages 1-2) |
| Hemiparesis | Clinical sign | Hemiparesis | HP:0001269 | 2/80 postoperative transient cases in surgical series; frequency at presentation not fully reported | Can occur with pineal region tumor manipulation or with basal ganglia/thalamic GCTs | (tomita2023pediatricpinealregion pages 1-2, yeo2023primarycentralnervous pages 2-3) |
| Cerebellar ataxia | Clinical sign | Cerebellar ataxia | HP:0001251 | 2/80 postoperative transient cases | Seen as postoperative neurological morbidity in pineal region surgery; cerebellar dysfunction can also occur with posterior fossa/cerebellar lesions | (tomita2023pediatricpinealregion pages 1-2) |
| Hemiballismus | Clinical sign / movement disorder | Hemiballismus | HP:0011446 | 1/80 postoperative transient case | Rare postoperative complication in pineal region tumor surgery | (tomita2023pediatricpinealregion pages 1-2) |
| Bilateral oculomotor palsy | Clinical sign | Oculomotor nerve palsy | HP:0007009 | 1/80 permanent postoperative case | Brainstem / pineal region operative morbidity | (tomita2023pediatricpinealregion pages 1-2) |
| Hemisensory loss | Clinical sign | Hemihypesthesia / Hemisensory loss | not confirmed | 1/80 permanent postoperative case | Reported as permanent deficit after pineal region surgery | (tomita2023pediatricpinealregion pages 1-2) |
| Cranial neuropathy | Clinical sign | Cranial nerve abnormality | HP:0001291 | Frequency not reported | More typical of basal ganglia/thalamic lesions in CNS GCT review | (yeo2023primarycentralnervous pages 2-3) |
| Hemianopia / visual field defect | Clinical sign | Hemianopia | HP:0007343 | 2/80 postoperative cases, transient | Reported after pineal region surgery | (tomita2023pediatricpinealregion pages 1-2) |
| Neurocognitive decline | Behavioral / neurodevelopmental manifestation | Neurocognitive impairment | not confirmed | Frequency not reported | Described particularly with basal ganglia lesions and prolonged disease course | (yeo2023primarycentralnervous pages 2-3) |


*Table: This table summarizes common presenting symptoms, neurological signs, and endocrine manifestations relevant to CNS teratoma within the broader CNS germ cell tumor literature. It maps each feature to a suggested HPO term and gives frequencies and anatomical context from recent pediatric series and reviews.*

Additional phenotype/location patterns:
- **Pineal region lesions** commonly present with obstructive hydrocephalus and dorsal midbrain signs (Parinaud syndrome). (tomita2023pediatricpinealregion pages 1-2, nowacka2025matureteratomaof pages 5-7)
- **Suprasellar lesions** commonly present with hypothalamic–pituitary dysfunction including diabetes insipidus. (giron2024primarycentralnervous pages 1-2, yeo2023primarycentralnervous pages 2-3)
- **Basal ganglia/thalamic lesions** may present with hemiparesis, cranial neuropathy, and protracted neurocognitive decline. (yeo2023primarycentralnervous pages 2-3)

Quality-of-life impacts: neurologic and endocrine sequelae (e.g., motor/sensory deficits, sphincter dysfunction in spinal disease) can persist and affect long-term function, motivating long-term follow-up. (zavalaromero2024matureteratomaat pages 8-9)

---

## 4. Genetic / molecular information
### Key molecular themes (CNS GCTs with relevance to teratoma)
- **Chromosome 12p gain** occurs in ~30% of CNS GCT overall and ~50% of NGGCT; it is associated with shorter progression-free and overall survival and appears shared across histologic components, implying an early event. (yeo2023primarycentralnervous pages 1-2)
- **MAPK pathway** and **PI3K/AKT/mTOR pathway** alterations (including KIT/RAS and PI3K/AKT1 changes) are common in CNS germinomas; NGGCTs show distinct programs (neuronal differentiation/EMT) and may show Wnt/β‑catenin–associated gene activity. (yeo2023primarycentralnervous pages 1-2, yeo2023primarycentralnervous pages 5-6)
- **KIT** is commonly overexpressed in pure germinomas and is largely absent in NGGCTs without germinomatous components, supporting biology-driven stratification and targeted-therapy interest (mostly germinoma-focused). (yeo2023primarycentralnervous pages 5-6)

### Teratoma-relevant biomarker behavior
In a large international, histology-verified cohort, **AFP was often elevated even without yolk sac tumor**, especially in **immature teratoma**; and **HCG elevation** was restricted to tumors with germinoma or choriocarcinoma components (with a discernible cut‑off separating those). (takami2023impactoftumor pages 1-2)

### Notable recent molecular case evidence (2024)
A recent intracranial growing teratoma syndrome case with malignant features reported:
- DNA methylation classifier confirming **teratoma** (high calibrated score)
- Copy-number alterations including **DMRT1 loss** and **12p gain**; authors discuss DMRT1’s role in primordial germ cells and teratomagenesis evidence from mouse models. (satake2024successfulmultimodaltreatment pages 3-5, satake2024successfulmultimodaltreatment pages 5-7)

### Liquid biopsy and emerging biomarkers (state of the field)
Recent reviews highlight developing noninvasive diagnostics for intracranial GCTs using **CSF ctDNA**, **microRNA clusters (miR‑371‑373, miR‑302/367)**, and methylation profiling, but CNS-specific validation and clinical integration remain ongoing. (yeo2023primarycentralnervous pages 2-3, yeo2025intracranialgermcell pages 3-4)

---

## 5. Environmental information
No specific environmental, lifestyle, toxicologic, or infectious causal factors were identified in the retrieved CNS teratoma-focused evidence.

---

## 6. Mechanism / pathophysiology
### Causal chain (high-level)
1. **Developmental cell-of-origin event:** sequestration/mis-migration of pluripotent germ cell–like precursors in CNS midline structures. (yeo2023primarycentralnervous pages 1-2, tengattini2024primarycooccurrenceof pages 1-2)
2. **Oncogenic transformation:** acquisition of chromosomal and pathway alterations (e.g., 12p gain; MAPK/PI3K pathway changes) promoting survival/proliferation and resisting apoptosis. (yeo2023primarycentralnervous pages 1-2, tengattini2024primarycooccurrenceof pages 8-10)
3. **Differentiation into multiple tissue types:** teratoma tissue composition leads to heterogeneous imaging features (fat, calcification, cysts) and variable marker secretion. (nowacka2025matureteratomaof pages 5-7, takami2023impactoftumor pages 1-2)
4. **Clinical manifestations:** local compression (hydrocephalus, brainstem dysfunction, visual/endocrine deficits) and/or dissemination (CSF cytology positivity in some patients). (tomita2023pediatricpinealregion pages 1-2, yeo2023primarycentralnervous pages 3-4, giron2024primarycentralnervous pages 1-2)

### Growing teratoma syndrome (treatment-related biological phenomenon)
Intracranial growing teratoma syndrome (iGTS) is defined as paradoxical growth of a (mature) teratoma component during/after therapy for malignant CNS GCT **despite normalization of markers**; it likely reflects selection/enrichment of mature teratomatous elements not responsive to chemotherapy/radiotherapy and requires surgery. (michaiel2020intracranialgrowingteratoma pages 1-2, nakamura2022thejapansociety pages 5-7)

Suggested ontology terms (examples):
- **GO biological processes:** “cell proliferation”, “germ cell development”, “DNA methylation”, “PI3K signaling”, “MAPK cascade” (IDs not retrieved in this run)
- **Cell Ontology (CL):** “primordial germ cell” (CL term name; ID not retrieved in this run)

---

## 7. Anatomical structures affected
### Primary sites (intracranial)
Midline structures are typical:
- **Pineal region**, **suprasellar region**, **basal ganglia**, **thalamus**; ventricular involvement may cause hydrocephalus. (zygourakis2015managementofcentral pages 1-2, nowacka2025matureteratomaof pages 5-7)

### Spinal axis
- Intradural lesions are described, often **extramedullary** in some series; other reviews emphasize many adult spinal teratomas are **intramedullary** and often lumbar/conus-predominant. (challa2010teratomasincentral pages 1-2, zavalaromero2024matureteratomaat pages 7-8)

Suggested UBERON examples (names; IDs not retrieved here): pineal gland, hypothalamus, pituitary gland, spinal cord, conus medullaris.

---

## 8. Temporal development
- **Typical onset:** most CNS GCTs present in childhood/adolescence; median age ~16 years is reported for CNS GCT broadly. (yeo2023primarycentralnervous pages 1-2)
- **Spinal disease:** adult spinal teratomas are uncommon but reported; symptoms may be slowly progressive and compression-related, with long regrowth intervals reported years after resection (3–13 years). (zavalaromero2024matureteratomaat pages 8-9)
- **iGTS timing:** in a large international series, iGTS occurred early (median 2 months from diagnosis). (michaiel2020intracranialgrowingteratoma pages 1-2)

---

## 9. Inheritance and population
### Epidemiology (best available quantitative estimates)
- CNS teratomas comprise **~0.5–1% of primary adult intracranial tumors**, and are reported as more frequent in children (~7% in one review). (zygourakis2015managementofcentral pages 1-2)
- Reported regional differences: in Japan/Korea/Taiwan, rates were reported as **1.8–5% in adults** and **up to 15% in children** (proportion among intracranial tumors, per review). (zygourakis2015managementofcentral pages 1-2)
- In an LMIC regional pediatric CNS GCT cohort (AHOPCA, 2001–2021; n=48), there was a male predominance **64.6%** and median age **10.2 years**. (giron2024primarycentralnervous pages 1-2)

### Germline inheritance
CNS teratoma is not established as a classic Mendelian inherited disorder in the retrieved evidence. Reported associations (Down, Klinefelter, JMJD1C) are best viewed as **predisposition associations** within CNS GCT biology rather than a defined inheritance pattern. (yeo2023primarycentralnervous pages 2-3)

---

## 10. Diagnostics
### Clinical and imaging diagnostics
- **MRI brain/spine with contrast** is standard for staging, and **CSF cytology via lumbar puncture** is standard-of-care; positive CSF cytology is considered metastatic even if spine MRI is normal. (yeo2023primarycentralnervous pages 3-4)
- Imaging patterns in intracranial teratoma are heterogeneous and reflect mixed tissue composition; CT can highlight calcification/bone and MRI signal heterogeneity can reflect fat/cystic components. (nowacka2025matureteratomaof pages 5-7)

### Tumor markers (serum and CSF)
- Guidelines strongly recommend measuring **AFP and HCG in both serum and CSF** when CNS GCT is suspected. (nakamura2022thejapansociety pages 4-5)
- Marker sampling site matters: in a large international cohort, **HCG was elevated only in CSF in 3/52 cases**, and **AFP only in serum in 7/49 cases**, supporting routine paired sampling. (takami2023impactoftumor pages 1-2)
- Clinical thresholds are variable across groups, but a commonly used NGGCT threshold is **β‑HCG >50 mIU/mL and/or AFP >10 ng/mL**, also used operationally in recent regional cohorts. (zhang2025cacaguidelinesfor pages 3-5, giron2024primarycentralnervous pages 2-3)

### Marker behavior in immature teratoma (important diagnostic nuance)
AFP can be elevated even without yolk sac tumor histology, **particularly in immature teratoma**, which complicates marker-only inference of histology. (takami2023impactoftumor pages 1-2)

### Pathology
Definitive diagnosis remains histopathologic identification of germ-layer derivatives; immunohistochemistry supports component identification and differentiation from mixed GCT. (zygourakis2015managementofcentral pages 1-2, nowacka2025matureteratomaof pages 5-7)

### Differential diagnosis (examples)
Depends on location and imaging; spinal intradural lesions can mimic schwannoma/meningioma; intracranial parenchymal masses may be misdiagnosed as glioma when heterogeneous. (jeong2023adultintramedullarymature pages 1-3)

---

## 11. Outcome / prognosis
### Histology-driven prognosis
- Mature (benign) teratoma has favorable outcomes with reported **5‑year survival 87–100%**.
- Malignant teratoma has worse outcomes with reported **5‑year survival 33–71%**. (zygourakis2015managementofcentral pages 1-2, zygourakis2015managementofcentral pages 6-7)
- In an international cohort analysis, **immature teratoma had unfavorable prognosis independent of marker status, with 56% 5‑year overall survival**. (takami2023impactoftumor pages 1-2)

### Growing teratoma syndrome outcomes
In the largest extracted multi-institution iGTS series (n=39):
- iGTS frequency **5%** among 777 CNS GCT
- **Gross total resection 79%**
- **95% alive** at median follow-up 5.3 years (michaiel2020intracranialgrowingteratoma pages 1-2)

### Resource setting impacts (2024 AHOPCA)
In the AHOPCA cohort (n=48), **5‑year OS 65% overall** (germinoma 68%, NGGCT 50.6%), substantially lower than high-income country benchmarks, likely reflecting heterogeneous protocols and incomplete staging resources. (giron2024primarycentralnervous pages 1-2)

### Spinal mature teratoma prognosis
Adult spinal teratomas are rare; mature spinal teratomas are reported to have favorable long-term outcomes in reviews (e.g., **10-year survival 92%**) with recurrence/regrowth reported (e.g., **~9–11%** and regrowth intervals **3–13 years**). (zavalaromero2024matureteratomaat pages 8-9)

---

## 12. Treatment
Treatment is driven by (i) mature vs immature/malignant features, (ii) secretory vs nonsecretory markers, and (iii) localized vs disseminated disease.

| Intervention | Indication (teratoma subtype context) | Evidence summary | Suggested MAXO term (name; ID if unknown mark not confirmed) | Key sources |
|---|---|---|---|---|
| Gross total resection of mature teratoma | Pure mature intracranial or intraspinal teratoma; especially marker-negative localized disease | Surgery is the primary treatment for mature teratoma; guidelines recommend surgery for mature teratomas, and case series/reviews report excellent long-term outcomes after complete resection, with mature teratoma generally not requiring adjuvant radiotherapy if completely resected. Gross total resection is also the mainstay for spinal mature teratoma. (nakamura2022thejapansociety pages 5-7, zavalaromero2024matureteratomaat pages 1-2, zavalaromero2024matureteratomaat pages 8-9, zygourakis2015managementofcentral pages 1-2) | surgical excision of teratoma; MAXO ID not confirmed | (nakamura2022thejapansociety pages 5-7, zavalaromero2024matureteratomaat pages 1-2, zavalaromero2024matureteratomaat pages 8-9, zygourakis2015managementofcentral pages 1-2) |
| Biopsy for suspected germinoma | Midline CNS GCT suspected to be germinoma when markers are negative/equivocal and aggressive resection is not indicated | For suspected germinoma, biopsy rather than aggressive resection is advised to obtain histology. Histopathology remains the standard principle because marker overlap can misclassify NGGCT/teratoma. Endoscopic, stereotactic, transsphenoidal, or open biopsy approaches may be used depending on site. (nakamura2022thejapansociety pages 5-7, nakamura2022thejapansociety pages 4-5, yeo2023primarycentralnervous pages 3-4) | tumor biopsy; MAXO ID not confirmed | (nakamura2022thejapansociety pages 5-7, nakamura2022thejapansociety pages 4-5, yeo2023primarycentralnervous pages 3-4) |
| Endoscopic third ventriculostomy for hydrocephalus | Obstructive hydrocephalus from pineal/suprasellar tumors, including teratoma-containing masses | Hydrocephalus is common in pineal-region disease. ETV is strongly recommended for hydrocephalus associated with CNS GCTs, often combined with biopsy; VPS carries seeding concerns. In a pediatric pineal series, hydrocephalus occurred in 74/80 and was commonly managed before tumor resection. (nakamura2022thejapansociety pages 7-8, tomita2023pediatricpinealregion pages 1-2, yeo2023primarycentralnervous pages 3-4) | endoscopic third ventriculostomy; MAXO ID not confirmed | (nakamura2022thejapansociety pages 7-8, tomita2023pediatricpinealregion pages 1-2, yeo2023primarycentralnervous pages 3-4) |
| Induction platinum-based chemotherapy (carboplatin/etoposide; cisplatin/ifosfamide/etoposide) | Secretory NGGCT; immature teratoma within NGGCT/mixed GCT; residual-risk stratification before surgery/RT | Platinum-etoposide regimens are standard backbones in CNS GCT management. Trials/guidelines use carboplatin+etoposide and cisplatin/ifosfamide/etoposide for induction, particularly for NGGCT; immature teratoma is treated in risk-adapted multimodal protocols rather than surgery alone when part of NGGCT biology. (nakamura2022thejapansociety pages 7-8, NCT00047320 chunk 1, NCT01424839 chunk 2, NCT01424839 chunk 1, takami2023impactoftumor pages 1-2) | platinum-based chemotherapy; MAXO ID not confirmed | (nakamura2022thejapansociety pages 7-8, NCT00047320 chunk 1, NCT01424839 chunk 2, NCT01424839 chunk 1, takami2023impactoftumor pages 1-2) |
| Whole ventricular irradiation | Nondisseminated germinoma after chemotherapy; selected marker-negative/nonsecretory midline CNS GCT pathways | Whole-ventricular irradiation is strongly recommended for nondisseminated germinoma in combination with chemotherapy, with typical doses around 18–24 Gy plus local boost depending on response. This approach is used to reduce long-term toxicity compared with broader fields. (nakamura2022thejapansociety pages 7-8, yeo2023primarycentralnervous pages 3-4, NCT01424839 chunk 2) | whole ventricular irradiation; MAXO ID not confirmed | (nakamura2022thejapansociety pages 7-8, yeo2023primarycentralnervous pages 3-4, NCT01424839 chunk 2) |
| Craniospinal irradiation | Metastatic germinoma/NGGCT; disseminated disease; some high-risk residual or marker-positive protocols | CSI remains standard for metastatic or disseminated CNS GCT and is used in NGGCT protocols and some post-induction regimens. Trials specify CSI with boosts for metastatic germinoma and NGGCT; Satake 2024 used CSI plus boost for aggressive teratomatous disease with malignant features. (NCT00047320 chunk 1, NCT01424839 chunk 2, NCT01424839 chunk 1, satake2024successfulmultimodaltreatment pages 3-5) | craniospinal irradiation; MAXO ID not confirmed | (NCT00047320 chunk 1, NCT01424839 chunk 2, NCT01424839 chunk 1, satake2024successfulmultimodaltreatment pages 3-5) |
| Second-look surgery for residual mass / growing teratoma syndrome | Residual mass after induction therapy; discordant marker/imaging response; suspected GTS; residual NGGCT/immature teratoma | Second-look surgery is recommended for residual primary mass after induction chemotherapy in NGGCT and is specifically useful to diagnose/resect growing teratoma syndrome or viable residual tumor. iGTS occurs in a minority of CNS GCTs and management is primarily surgical, with gross total resection associated with favorable outcomes. (nakamura2022thejapansociety pages 5-7, yeo2023primarycentralnervous pages 3-4, michaiel2020intracranialgrowingteratoma pages 1-2, NCT00047320 chunk 1, NCT01424839 chunk 1) | second-look surgery; MAXO ID not confirmed | (nakamura2022thejapansociety pages 5-7, yeo2023primarycentralnervous pages 3-4, michaiel2020intracranialgrowingteratoma pages 1-2, NCT00047320 chunk 1, NCT01424839 chunk 1) |
| High-dose chemotherapy with autologous stem cell rescue | High-risk NGGCT; suboptimal response after induction/second-look surgery; aggressive teratomatous lesions with malignant features | In ACNS0122, patients with less than partial response after induction/second-look could receive high-dose thiotepa/etoposide with autologous PBSC rescue before radiotherapy. SIOP CNS GCT II includes dose-intensified courses with stem-cell support for high-risk NGGCT. A 2024 pineal iGTS case with malignant features achieved durable remission after surgery, CSI, ICE chemotherapy, and autologous stem-cell transplantation. (NCT00047320 chunk 1, NCT01424839 chunk 2, NCT01424839 chunk 1, satake2024successfulmultimodaltreatment pages 3-5) | autologous hematopoietic stem cell transplantation after high-dose chemotherapy; MAXO ID not confirmed | (NCT00047320 chunk 1, NCT01424839 chunk 2, NCT01424839 chunk 1, satake2024successfulmultimodaltreatment pages 3-5) |


*Table: This table summarizes major treatment modalities used in CNS teratoma and related CNS germ cell tumor care, linking each intervention to its clinical context, supporting evidence, and a suggested MAXO term. It is useful for structuring treatment annotations in a disease knowledge base.*

### Real-world implementations and expert guidance (selected)
- **Mature teratoma:** surgical resection is primary treatment (strong recommendation in Japanese guideline). (nakamura2022thejapansociety pages 5-7)
- **Germinoma suspected:** biopsy rather than aggressive resection. (nakamura2022thejapansociety pages 4-5)
- **NGGCT/immature teratoma/mixed disease:** multimodality therapy; **resection of residual tumor after chemotherapy** is strongly recommended (Japanese guideline). (nakamura2022thejapansociety pages 5-7)

### Clinical trials relevant to NGGCT/teratoma practice
- **COG ACNS0122 (NCT00047320; published on ClinicalTrials.gov, 2004):** induction carboplatin/etoposide alternating with etoposide/ifosfamide; second-look surgery for <CR; radiotherapy (including CSI with boost) and escalation to high-dose chemotherapy with autologous stem-cell rescue for poor responders; endpoints included 3‑year EFS/PFS/OS and toxicity. (NCT00047320 chunk 1, NCT00047320 chunk 2)
- **SIOP CNS GCT II (NCT01424839; ClinicalTrials.gov, 2011):** prespecified regimens for germinoma vs NGGCT including stem-cell supported intensification for high-risk NGGCT; **resection of residual tumor after 3 courses** when indicated; focal RT 54 Gy for localized NGGCT and CSI with boosts for metastatic disease; primary endpoint 5‑year EFS. (NCT01424839 chunk 1, NCT01424839 chunk 2)

---

## 13. Prevention
No primary prevention strategies are established. Secondary prevention largely consists of timely diagnosis and appropriate staging (MRI brain/spine, CSF cytology, serum/CSF markers) to reduce undertreatment/overtreatment. (yeo2023primarycentralnervous pages 3-4, nakamura2022thejapansociety pages 4-5)

---

## 14. Other species / natural disease
No comparative animal natural disease evidence was identified in the retrieved materials.

---

## 15. Model organisms
Model organism systems were not retrieved in the evidence set for this run. One mechanistic clue referenced in the 2024 iGTS report is that **Dmrt1 loss increases teratoma incidence in mouse models**, but detailed model descriptions were not extracted here. (satake2024successfulmultimodaltreatment pages 5-7)

---

## Key quantitative findings (quick reference)
| Study (year) | Population/setting | Key CNS teratoma-related findings (include numeric stats, marker thresholds/values, survival) | Notes/limitations | DOI/URL |
|---|---|---|---|---|
| Takami et al. (2023) | International histopathology-verified intracranial GCT cohort; combined n=161 (biopsy n=85, resection n=76), mostly pediatric/adolescent | HCG elevation was limited to tumors with germinoma or choriocarcinoma components; AFP was often elevated without yolk sac tumor, especially in immature teratoma. HCG was elevated only in CSF in 3/52 cases; AFP only in serum in 7/49 cases, supporting testing both serum and CSF. Germinomas comprise ~50–60% of CNS GCTs with >90% long-term survival; NGGCT long-term survival ~60–70%. Immature teratoma had unfavorable prognosis independent of marker status, with 56% 5-year OS. (takami2023impactoftumor pages 1-2, takami2023impactoftumor pages 9-9) | Cohort spans broader CNS GCTs rather than pure teratoma only; marker findings must be interpreted in mixed-histology context. | https://doi.org/10.1007/s10014-023-00460-x |
| Girón et al. (2024) | AHOPCA retrospective pediatric CNS GCT series, 48 patients, 4 countries in Central America/Caribbean, 2001–2021 | Male 31/48 (64.6%); median age 10.2 years. Symptoms: headache 24 (50%), visual disturbance 17 (35.4%), vomiting 12 (25%), nausea 8 (16.7%), diabetes insipidus 7 (14.6%), precocious puberty in 2 NGGCT patients. Sites: suprasellar 17 (35.4%), pineal 13 (27.1%), thalamus/basal ganglia 5 (10.4%), other 12 (25%), bifocal 1. Eight patients were diagnosed/treated from CSF markers alone: 4 germinomas with β-hCG 11.32–29.41 mIU/mL; 4 NGGCT with β-hCG 84.43–201.97 mIU/mL or AFP >10 IU/mL. Metastatic disease in 4/48 (8.3%); positive CSF in 6; 5-year OS 65% overall, 68% germinoma, 50.6% NGGCT, 85.7% unclassified. (giron2024primarycentralnervous pages 1-2, giron2024primarycentralnervous pages 2-3) | Not teratoma-specific; staging incomplete in 52%, treatment heterogeneous, resource-limited setting likely lowered outcomes versus HIC. | https://doi.org/10.3389/fonc.2024.1393454 |
| Tomita et al. (2023) | Single-institution pediatric pineal region tumor surgical series, 80 patients (1990–2019) treated mainly via occipital transtentorial approach | Hydrocephalus in 74/80. Pre-craniotomy CSF diversion: ETV 33, EVD 26, shunt 15; ETV+biopsy in 9. Pathology included 32 germ cell tumors, of which 18 were teratomas. Extent of resection: 55 gross total, 13 subtotal, 10 partial, 2 biopsy; 1 postoperative death. Morbidity mostly transient: hemiparesis 2, cerebellar ataxia 2, hemiballismus 1; permanent hemisensory loss 1 and bilateral oculomotor palsy 1. Parinaud’s sign in 24 patients (16 transient). Figure/Table content from the paper also notes 8 pineal teratomas and 14 NGGCT with teratoma components in the pathology/location summary. (tomita2023pediatricpinealregion pages 1-2, tomita2023pediatricpinealregion media 78dd21ef) | Surgical series of pineal-region tumors, not all teratomas; no teratoma-specific survival or marker values reported in extracted evidence. | https://doi.org/10.1007/s00381-022-05595-4 |
| Michaiel et al. (2020) | International multicenter iGTS series across 22 institutions; 777 CNS GCTs screened, 39 iGTS cases | Intracranial growing teratoma syndrome (iGTS) frequency 5% (39/777). Strong pineal predilection; occurred early, median 2 months from diagnosis. Initial tissue showed immature teratoma in 50% of available cases. Serum AFP or β-hCG detectable in 87% at diagnosis (median AFP 66 ng/mL; median β-hCG 44 IU/L). Gross total resection achieved in 79%; all underwent surgery. At median 5.3-year follow-up, 95% were alive. MRI may show a characteristic “honeycomb” residual mature teratoma appearance. (michaiel2020intracranialgrowingteratoma pages 1-2) | iGTS is a treatment-related syndrome rather than all CNS teratoma; cohort includes mixed malignant GCT precursors. | https://doi.org/10.1007/s11060-020-03486-9 |
| Zygourakis et al. (2015) | Review/case-series perspective on CNS teratoma management | CNS teratomas account for ~0.5–1% of primary adult intracranial tumors, ~7% in children; incidence higher in East Asia (1.8–5% in adults, up to 15% in children). Typical locations are midline intracranial sites; spinal lesions often extramedullary and thoracolumbar. Reported 5-year survival: mature teratoma 87–100%; malignant teratoma 33–71%. Tumor markers (AFP, β-hCG) are part of workup, although one illustrative case had negative serum/CSF markers. (zygourakis2015managementofcentral pages 1-2, zygourakis2015managementofcentral pages 6-7) | Older review; survival ranges come from heterogeneous historical series and mixed pathology definitions. | https://doi.org/10.1016/j.jocn.2014.03.039 |
| Satake et al. (2024) | Single case of pineal mixed GCT evolving into intracranial GTS with malignant features | 14-year-old boy with ~3.3 cm pineal mass and obstructive hydrocephalus. Initial serum AFP 5 ng/mL and β-hCG 6 mIU/mL (negative/low), but CSF PLAP 1280 pg/mL and CSF β-hCG 15 mIU/mL were elevated. During carboplatin/etoposide, serum AFP transiently rose to 81 ng/mL then normalized despite lesion enlargement. Pathology after gross total resection showed teratoma with malignant features; MIB-1 up to 30%. Molecular profiling: methylation classifier teratoma score 0.99; CNV showed DMRT1 loss and 12p gain. Treated with resection, craniospinal irradiation 30.6 Gy + 23.4 Gy boost, six cycles of ICE, and autologous stem-cell transplant; relapse-free for >3 years. (satake2024successfulmultimodaltreatment pages 3-5, satake2024successfulmultimodaltreatment pages 1-3) | Single case report; useful for molecular/pathophysiologic clues but not frequency estimates. | https://doi.org/10.3390/curroncol31040138 |
| Challa et al. (2010) | Clinico-morphological craniospinal teratoma series, 14 cases | Age range birth–57 years (mean ~15.9). Histology: 11/14 mature cystic teratomas, plus single malignant transformation, teratocarcinoma, and mixed germ cell tumor. Distribution: 6 intracranial and 8 spinal. In the authors’ referral series, teratomas comprised <0.1% of intracranial tumors and ~0.6% of spinal tumors. Surgery was primary treatment; adjuvant radiotherapy used for teratocarcinoma and mixed GCT. (challa2010teratomasincentral pages 1-2) | Older, small institutional series; incidence values are center-specific, not population-based. | https://doi.org/10.4103/0028-3886.73740 |


*Table: This table summarizes selected quantitative findings from major CNS teratoma and CNS germ cell tumor studies relevant to diagnosis, epidemiology, treatment, and outcomes. It is useful for quickly comparing marker data, survival estimates, and clinical series characteristics across recent and foundational publications.*

---

## Visual evidence (figures/tables)
- A representative **pineal teratoma imaging + intraoperative view** and a **pathology/location table** from a large pediatric pineal region surgical series were retrieved and can be used for knowledge-base curation. (tomita2023pediatricpinealregion media 78dd21ef)

---

## Direct abstract-supported statements (selected)
- Tumor markers guide diagnosis/treatment: Takami et al. (2023) state that tumor markers AFP/HCG have “significant diagnostic implications” and that elevation of either can lead to clinical diagnosis of NGGCT without histopathologic confirmation. (takami2023impactoftumor pages 1-2)
- Regional outcomes gap: Girón et al. (2024) report “Overall survival (OS) is above 90% for germinomas and 70%–80% for NGGCT in high-income countries,” but their cohort’s OS was lower, highlighting implementation disparities. (giron2024primarycentralnervous pages 1-2)

---

## Limitations of this report (data gaps)
- Formal identifiers (MONDO/MeSH/ICD/Orphanet/OMIM) could not be retrieved with the available tools.
- Many quantitative epidemiology and survival estimates are derived from CNS GCT cohorts and reviews rather than teratoma-only population registries.
- HPO/GO/CL/UBERON/MAXO IDs were not programmatically validated in this run; where included, they should be verified against the respective ontology releases.


References

1. (zygourakis2015managementofcentral pages 1-2): Corinna C. Zygourakis, Jessica L. Davis, Gurvinder Kaur, Christopher P. Ames, Nalin Gupta, Kurtis I. Auguste, and Andrew T. Parsa. Management of central nervous system teratoma. Journal of Clinical Neuroscience, 22:98-104, Jan 2015. URL: https://doi.org/10.1016/j.jocn.2014.03.039, doi:10.1016/j.jocn.2014.03.039. This article has 24 citations and is from a peer-reviewed journal.

2. (challa2010teratomasincentral pages 1-2): Sundaram Challa, Meetu Agrawal, MeghaS Uppin, MohanaR Patibandla, Suchanda Bhattacharjee, ManasK Panigrahi, Vijay Saradhi, JyotsnaY Rani, and AK Purohit. Teratomas in central nervous system: a clinico-morphological study with review of literature. Neurology India, 58 6:841-6, Nov 2010. URL: https://doi.org/10.4103/0028-3886.73740, doi:10.4103/0028-3886.73740. This article has 61 citations and is from a peer-reviewed journal.

3. (nowacka2025matureteratomaof pages 5-7): Agnieszka Nowacka, Ewa Ziółkowska, Wojciech Smuczyński, Dominika Bożiłow, and Maciej Śniegocki. Mature teratoma of the cerebellum with formed extracranial component. Journal of Clinical Medicine, 14:1994, Mar 2025. URL: https://doi.org/10.3390/jcm14061994, doi:10.3390/jcm14061994. This article has 0 citations.

4. (michaiel2020intracranialgrowingteratoma pages 1-2): George Michaiel, Douglas Strother, Nicholas Gottardo, Ute Bartels, Hallie Coltin, Juliette Hukin, Beverly Wilson, Shayna Zelcer, Jordan R. Hansford, Timothy Hassall, Mohamed S. AbdelBaki, Kristina A. Cole, Lindsey Hoffman, Natasha P. Smiley, Amy Smith, Anna Vinitsky, Nicholas A. Vitanza, Avery Wright, Kee K. Yeo, Lionel M. L. Chow, Magimairajan I. Vanan, Girish Dhall, Eric Bouffet, and Lucie Lafay-Cousin. Intracranial growing teratoma syndrome (igts): an international case series and review of the literature. Journal of Neuro-Oncology, 147:721-730, Apr 2020. URL: https://doi.org/10.1007/s11060-020-03486-9, doi:10.1007/s11060-020-03486-9. This article has 41 citations and is from a peer-reviewed journal.

5. (satake2024successfulmultimodaltreatment pages 1-3): Daiken Satake, Manabu Natsumeda, Kaishi Satomi, Mari Tada, Taro Sato, Noritaka Okubo, Keita Kawabe, Haruhiko Takahashi, Yoshihiro Tsukamoto, Masayasu Okada, Masakazu Sano, Haruko Iwabuchi, Nao Shibata, Masaru Imamura, Chihaya Imai, Hirokazu Takami, Koichi Ichimura, Ryo Nishikawa, Hajime Umezu, Akiyoshi Kakita, and Makoto Oishi. Successful multimodal treatment of intracranial growing teratoma syndrome with malignant features. Current Oncology, 31:1831-1838, Mar 2024. URL: https://doi.org/10.3390/curroncol31040138, doi:10.3390/curroncol31040138. This article has 4 citations.

6. (nakamura2022thejapansociety pages 7-8): Hideo Nakamura, Hirokazu Takami, Takaaki Yanagisawa, Toshihiro Kumabe, Takamitsu Fujimaki, Yoshiki Arakawa, Katsuyuki Karasawa, Keita Terashima, Hideaki Yokoo, Kohei Fukuoka, Yukihiko Sonoda, Kaori Sakurada, Yohei Mineharu, Toshinori Soejima, Motoaki Fujii, Naoki Shinojima, Junichi Hara, Kai Yamasaki, Junya Fujimura, Fumiyuki Yamasaki, Mayu Takahashi, Tomonari Suzuki, Iori Sato, Ryo Nishikawa, and Kazuhiko Sugiyama. The japan society for neuro-oncology guideline on the diagnosis and treatment of central nervous system germ cell tumors. Neuro-oncology, 24:503-515, Oct 2022. URL: https://doi.org/10.1093/neuonc/noab242, doi:10.1093/neuonc/noab242. This article has 76 citations and is from a domain leading peer-reviewed journal.

7. (takami2023impactoftumor pages 1-2): Hirokazu Takami, Christopher S. Graffeo, Avital Perry, Caterina Giannini, Yoichi Nakazato, Nobuhito Saito, Masao Matsutani, Ryo Nishikawa, David J. Daniels, and Koichi Ichimura. Impact of tumor markers on diagnosis, treatment and prognosis in cns germ cell tumors: correlations with clinical practice and histopathology. Brain Tumor Pathology, 40:124-132, Mar 2023. URL: https://doi.org/10.1007/s10014-023-00460-x, doi:10.1007/s10014-023-00460-x. This article has 15 citations and is from a peer-reviewed journal.

8. (giron2024primarycentralnervous pages 1-2): Ana Verónica Girón, Jessica Blanco-Lopez, Patricia Calderon, Reyna Jiron, Estuardo Pineda, Margarita Montero, Yamel Lizardo, Ute Bartels, and Diana S. Osorio. Primary central nervous system germ cell tumors in central america and the caribbean region: an ahopca 20-year experience. Frontiers in Oncology, Jul 2024. URL: https://doi.org/10.3389/fonc.2024.1393454, doi:10.3389/fonc.2024.1393454. This article has 3 citations.

9. (zavalaromero2024matureteratomaat pages 1-2): Lilian Zavala-Romero, Eliezer Villanueva-Castro, Rudradeep Datta-Banik, Alexis Genaro Ortiz-Altamirano, María Magdalena Rodriguez-Esquivel, Jesús Cienfuegos-Meza, and Juan Nicasio Arriada-Mendicoa. Mature teratoma at the lumbar spinal cord: a case report and literature review. Cureus, Jan 2024. URL: https://doi.org/10.7759/cureus.52307, doi:10.7759/cureus.52307. This article has 3 citations.

10. (yeo2023primarycentralnervous pages 1-2): Kee Kiat Yeo, Sumanth Nagabushan, Girish Dhall, and Mohamed S. Abdelbaki. Primary central nervous system germ cell tumors in children and young adults: a review of controversies in diagnostic and treatment approach. Neoplasia, 36:100860, Feb 2023. URL: https://doi.org/10.1016/j.neo.2022.100860, doi:10.1016/j.neo.2022.100860. This article has 26 citations and is from a domain leading peer-reviewed journal.

11. (tengattini2024primarycooccurrenceof pages 1-2): Francesco Tengattini, Cesare Francesco Soffiati, Pier Paolo Panciani, Marco Zeppieri, Tamara Ius, Shahan Momjian, Karl Schaller, Marco Maria Fontanella, and Lucio De Maria. Primary co-occurrence of gonadal and extragonadal central nervous system (cns) germ cell tumors (gcts): case report and review of the literature. Neuroglia, 5:50-62, Mar 2024. URL: https://doi.org/10.3390/neuroglia5010004, doi:10.3390/neuroglia5010004. This article has 1 citations.

12. (ferdause2023spinalintraduralextramedullary pages 3-3): Jannatul Ferdause, Ariful Islam, Taslima Rahman, Sura Jukrup Momtahena, Zillur Rahman, Tarim Mahmood, and Tasnim Mahmud. Spinal intradural extramedullary mature cystic teratoma at cervical location in an elderly person: a rare case report with review of literature. International Journal on Oncology and Radiotherapy, Apr 2023. URL: https://doi.org/10.51626/ijor.2023.04.00024, doi:10.51626/ijor.2023.04.00024. This article has 1 citations.

13. (yeo2023primarycentralnervous pages 2-3): Kee Kiat Yeo, Sumanth Nagabushan, Girish Dhall, and Mohamed S. Abdelbaki. Primary central nervous system germ cell tumors in children and young adults: a review of controversies in diagnostic and treatment approach. Neoplasia, 36:100860, Feb 2023. URL: https://doi.org/10.1016/j.neo.2022.100860, doi:10.1016/j.neo.2022.100860. This article has 26 citations and is from a domain leading peer-reviewed journal.

14. (satake2024successfulmultimodaltreatment pages 5-7): Daiken Satake, Manabu Natsumeda, Kaishi Satomi, Mari Tada, Taro Sato, Noritaka Okubo, Keita Kawabe, Haruhiko Takahashi, Yoshihiro Tsukamoto, Masayasu Okada, Masakazu Sano, Haruko Iwabuchi, Nao Shibata, Masaru Imamura, Chihaya Imai, Hirokazu Takami, Koichi Ichimura, Ryo Nishikawa, Hajime Umezu, Akiyoshi Kakita, and Makoto Oishi. Successful multimodal treatment of intracranial growing teratoma syndrome with malignant features. Current Oncology, 31:1831-1838, Mar 2024. URL: https://doi.org/10.3390/curroncol31040138, doi:10.3390/curroncol31040138. This article has 4 citations.

15. (giron2024primarycentralnervous pages 2-3): Ana Verónica Girón, Jessica Blanco-Lopez, Patricia Calderon, Reyna Jiron, Estuardo Pineda, Margarita Montero, Yamel Lizardo, Ute Bartels, and Diana S. Osorio. Primary central nervous system germ cell tumors in central america and the caribbean region: an ahopca 20-year experience. Frontiers in Oncology, Jul 2024. URL: https://doi.org/10.3389/fonc.2024.1393454, doi:10.3389/fonc.2024.1393454. This article has 3 citations.

16. (tomita2023pediatricpinealregion pages 1-2): Tadanori Tomita, Tord D. Alden, and Arthur J. Dipatri. Pediatric pineal region tumors: institutional experience of surgical managements with posterior interhemispheric transtentorial approach. Child's Nervous System, 39:2293-2305, Jul 2023. URL: https://doi.org/10.1007/s00381-022-05595-4, doi:10.1007/s00381-022-05595-4. This article has 22 citations.

17. (zavalaromero2024matureteratomaat pages 8-9): Lilian Zavala-Romero, Eliezer Villanueva-Castro, Rudradeep Datta-Banik, Alexis Genaro Ortiz-Altamirano, María Magdalena Rodriguez-Esquivel, Jesús Cienfuegos-Meza, and Juan Nicasio Arriada-Mendicoa. Mature teratoma at the lumbar spinal cord: a case report and literature review. Cureus, Jan 2024. URL: https://doi.org/10.7759/cureus.52307, doi:10.7759/cureus.52307. This article has 3 citations.

18. (yeo2023primarycentralnervous pages 5-6): Kee Kiat Yeo, Sumanth Nagabushan, Girish Dhall, and Mohamed S. Abdelbaki. Primary central nervous system germ cell tumors in children and young adults: a review of controversies in diagnostic and treatment approach. Neoplasia, 36:100860, Feb 2023. URL: https://doi.org/10.1016/j.neo.2022.100860, doi:10.1016/j.neo.2022.100860. This article has 26 citations and is from a domain leading peer-reviewed journal.

19. (satake2024successfulmultimodaltreatment pages 3-5): Daiken Satake, Manabu Natsumeda, Kaishi Satomi, Mari Tada, Taro Sato, Noritaka Okubo, Keita Kawabe, Haruhiko Takahashi, Yoshihiro Tsukamoto, Masayasu Okada, Masakazu Sano, Haruko Iwabuchi, Nao Shibata, Masaru Imamura, Chihaya Imai, Hirokazu Takami, Koichi Ichimura, Ryo Nishikawa, Hajime Umezu, Akiyoshi Kakita, and Makoto Oishi. Successful multimodal treatment of intracranial growing teratoma syndrome with malignant features. Current Oncology, 31:1831-1838, Mar 2024. URL: https://doi.org/10.3390/curroncol31040138, doi:10.3390/curroncol31040138. This article has 4 citations.

20. (yeo2025intracranialgermcell pages 3-4): Kee Kiat Yeo, Joanna Gell, Girish Dhall, and Ching Lau. Intracranial germ cell tumors: advancement in genomic diagnostics and the need for novel therapeutics. Frontiers in Oncology, Jan 2025. URL: https://doi.org/10.3389/fonc.2025.1513258, doi:10.3389/fonc.2025.1513258. This article has 1 citations.

21. (tengattini2024primarycooccurrenceof pages 8-10): Francesco Tengattini, Cesare Francesco Soffiati, Pier Paolo Panciani, Marco Zeppieri, Tamara Ius, Shahan Momjian, Karl Schaller, Marco Maria Fontanella, and Lucio De Maria. Primary co-occurrence of gonadal and extragonadal central nervous system (cns) germ cell tumors (gcts): case report and review of the literature. Neuroglia, 5:50-62, Mar 2024. URL: https://doi.org/10.3390/neuroglia5010004, doi:10.3390/neuroglia5010004. This article has 1 citations.

22. (yeo2023primarycentralnervous pages 3-4): Kee Kiat Yeo, Sumanth Nagabushan, Girish Dhall, and Mohamed S. Abdelbaki. Primary central nervous system germ cell tumors in children and young adults: a review of controversies in diagnostic and treatment approach. Neoplasia, 36:100860, Feb 2023. URL: https://doi.org/10.1016/j.neo.2022.100860, doi:10.1016/j.neo.2022.100860. This article has 26 citations and is from a domain leading peer-reviewed journal.

23. (nakamura2022thejapansociety pages 5-7): Hideo Nakamura, Hirokazu Takami, Takaaki Yanagisawa, Toshihiro Kumabe, Takamitsu Fujimaki, Yoshiki Arakawa, Katsuyuki Karasawa, Keita Terashima, Hideaki Yokoo, Kohei Fukuoka, Yukihiko Sonoda, Kaori Sakurada, Yohei Mineharu, Toshinori Soejima, Motoaki Fujii, Naoki Shinojima, Junichi Hara, Kai Yamasaki, Junya Fujimura, Fumiyuki Yamasaki, Mayu Takahashi, Tomonari Suzuki, Iori Sato, Ryo Nishikawa, and Kazuhiko Sugiyama. The japan society for neuro-oncology guideline on the diagnosis and treatment of central nervous system germ cell tumors. Neuro-oncology, 24:503-515, Oct 2022. URL: https://doi.org/10.1093/neuonc/noab242, doi:10.1093/neuonc/noab242. This article has 76 citations and is from a domain leading peer-reviewed journal.

24. (zavalaromero2024matureteratomaat pages 7-8): Lilian Zavala-Romero, Eliezer Villanueva-Castro, Rudradeep Datta-Banik, Alexis Genaro Ortiz-Altamirano, María Magdalena Rodriguez-Esquivel, Jesús Cienfuegos-Meza, and Juan Nicasio Arriada-Mendicoa. Mature teratoma at the lumbar spinal cord: a case report and literature review. Cureus, Jan 2024. URL: https://doi.org/10.7759/cureus.52307, doi:10.7759/cureus.52307. This article has 3 citations.

25. (nakamura2022thejapansociety pages 4-5): Hideo Nakamura, Hirokazu Takami, Takaaki Yanagisawa, Toshihiro Kumabe, Takamitsu Fujimaki, Yoshiki Arakawa, Katsuyuki Karasawa, Keita Terashima, Hideaki Yokoo, Kohei Fukuoka, Yukihiko Sonoda, Kaori Sakurada, Yohei Mineharu, Toshinori Soejima, Motoaki Fujii, Naoki Shinojima, Junichi Hara, Kai Yamasaki, Junya Fujimura, Fumiyuki Yamasaki, Mayu Takahashi, Tomonari Suzuki, Iori Sato, Ryo Nishikawa, and Kazuhiko Sugiyama. The japan society for neuro-oncology guideline on the diagnosis and treatment of central nervous system germ cell tumors. Neuro-oncology, 24:503-515, Oct 2022. URL: https://doi.org/10.1093/neuonc/noab242, doi:10.1093/neuonc/noab242. This article has 76 citations and is from a domain leading peer-reviewed journal.

26. (zhang2025cacaguidelinesfor pages 3-5): Chao Zhang, Xiang Huang, Yijin Gao, Yang Wang, Hongying Ye, Hong Chen, Junping Zhang, Linbo Cai, Chunde Li, Yuqi Zhang, Jingsheng Wang, Songtao Qi, Shuguang Chu, Yuanyuan Huang, Bei Zhang, Zhongping Chen, and Rong Zhang. Caca guidelines for holistic integrative management of central nervous system germ cell tumor. Holistic Integrative Oncology, Jun 2025. URL: https://doi.org/10.1007/s44178-025-00168-2, doi:10.1007/s44178-025-00168-2. This article has 1 citations.

27. (jeong2023adultintramedullarymature pages 1-3): Sun-Jun Jeong, Jong-Hyeok Park, and Sun-Young Jun. Adult intramedullary mature teratoma of the spinal cord: an unusual case with a review of the literature. The Nerve, 9:161-166, Oct 2023. URL: https://doi.org/10.21129/nerve.2023.00353, doi:10.21129/nerve.2023.00353. This article has 1 citations.

28. (zygourakis2015managementofcentral pages 6-7): Corinna C. Zygourakis, Jessica L. Davis, Gurvinder Kaur, Christopher P. Ames, Nalin Gupta, Kurtis I. Auguste, and Andrew T. Parsa. Management of central nervous system teratoma. Journal of Clinical Neuroscience, 22:98-104, Jan 2015. URL: https://doi.org/10.1016/j.jocn.2014.03.039, doi:10.1016/j.jocn.2014.03.039. This article has 24 citations and is from a peer-reviewed journal.

29. (NCT00047320 chunk 1):  Neoadjuvant Chemotherapy With or Without Second-Look Surgery Followed by Radiation Therapy With or Without Peripheral Stem Cell Transplantation in Treating Patients With Intracranial Germ Cell Tumors. Children's Oncology Group. 2004. ClinicalTrials.gov Identifier: NCT00047320

30. (NCT01424839 chunk 2):  Prospective Trial for the Diagnosis and Treatment of Intracranial Germ Cell Tumors. University Hospital Muenster. 2011. ClinicalTrials.gov Identifier: NCT01424839

31. (NCT01424839 chunk 1):  Prospective Trial for the Diagnosis and Treatment of Intracranial Germ Cell Tumors. University Hospital Muenster. 2011. ClinicalTrials.gov Identifier: NCT01424839

32. (NCT00047320 chunk 2):  Neoadjuvant Chemotherapy With or Without Second-Look Surgery Followed by Radiation Therapy With or Without Peripheral Stem Cell Transplantation in Treating Patients With Intracranial Germ Cell Tumors. Children's Oncology Group. 2004. ClinicalTrials.gov Identifier: NCT00047320

33. (takami2023impactoftumor pages 9-9): Hirokazu Takami, Christopher S. Graffeo, Avital Perry, Caterina Giannini, Yoichi Nakazato, Nobuhito Saito, Masao Matsutani, Ryo Nishikawa, David J. Daniels, and Koichi Ichimura. Impact of tumor markers on diagnosis, treatment and prognosis in cns germ cell tumors: correlations with clinical practice and histopathology. Brain Tumor Pathology, 40:124-132, Mar 2023. URL: https://doi.org/10.1007/s10014-023-00460-x, doi:10.1007/s10014-023-00460-x. This article has 15 citations and is from a peer-reviewed journal.

34. (tomita2023pediatricpinealregion media 78dd21ef): Tadanori Tomita, Tord D. Alden, and Arthur J. Dipatri. Pediatric pineal region tumors: institutional experience of surgical managements with posterior interhemispheric transtentorial approach. Child's Nervous System, 39:2293-2305, Jul 2023. URL: https://doi.org/10.1007/s00381-022-05595-4, doi:10.1007/s00381-022-05595-4. This article has 22 citations.