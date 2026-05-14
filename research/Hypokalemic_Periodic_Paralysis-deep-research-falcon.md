---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-09T11:17:20.783000'
end_time: '2026-05-09T11:33:40.766250'
duration_seconds: 979.98
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Hypokalemic Periodic Paralysis
  mondo_id: ''
  category: Genetic
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
- **Disease Name:** Hypokalemic Periodic Paralysis
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Hypokalemic Periodic Paralysis** covering all of the
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
- **Disease Name:** Hypokalemic Periodic Paralysis
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Hypokalemic Periodic Paralysis** covering all of the
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


# Hypokalemic Periodic Paralysis (HypoPP) — Disease Characteristics Research Report (Genetic)

## 1. Disease information

### Overview (current understanding)
Hypokalemic periodic paralysis (HypoPP) is a rare, primarily inherited skeletal muscle ion-channel disorder characterized by episodic, painless flaccid weakness/paralysis occurring with low serum potassium during attacks; interictal potassium is usually normal. Attacks may be focal or generalized and typically last hours to days. (cristina2022hypokalemicperiodicparalysis pages 1-2, statland2018reviewofthe pages 7-11)

A commonly used definition from a 2023 pediatric case report states HypoPP is “**a rare skeletal muscle disorder characterized by episodic muscle weakness associated with decreased serum potassium levels**.” (zhou2023anovelcacna1s pages 1-2)

### Key identifiers (ontology/registry)
The current tool-based retrieval in this run did **not** directly return OMIM, Orphanet, ICD-10/ICD-11, MeSH, or MONDO records for HypoPP; therefore, those identifiers cannot be cited from evidence here and should be filled from the relevant curated databases in a subsequent pass. (Evidence limitation)

### Synonyms / alternative names
Commonly used names in the literature retrieved here include:
- **Primary hypokalemic periodic paralysis / familial hypokalemic periodic paralysis** (statland2018reviewofthe pages 7-11, brown2024familialhypokalemicperiodic pages 1-2)
- **Hypokalemic periodic paralysis type 1** (CACNA1S-related) and **type 2** (SCN4A-related) (luo2026clinicalfeaturesand pages 5-6)

### Evidence sources
Information in this report is derived from aggregated disease-level resources (reviews, cohort/natural history studies, clinical trials/registries) and individual patient-level case reports. (statland2018reviewofthe pages 15-20, statland2018reviewofthe pages 7-11, holmyildiz2023hypokalemicperiodicparalysis pages 1-2, zhou2023anovelcacna1s pages 1-2, brown2024familialhypokalemicperiodic pages 1-2)


## 2. Etiology

### Disease causal factors
**Primary HypoPP** is a skeletal muscle channelopathy most commonly caused by pathogenic variants in:
- **CACNA1S** (skeletal muscle L-type calcium channel Cav1.1 α1S subunit) and
- **SCN4A** (skeletal muscle sodium channel Nav1.4). (statland2018reviewofthe pages 7-11, cammaratascalisi2026covid19infectionand pages 2-4)

In a widely cited review, CACNA1S accounts for ~**60% of kindreds** and SCN4A ~**20% of kindreds**. (statland2018reviewofthe pages 7-11)

### Risk factors (genetic and environmental/physiologic triggers)
**Genetic risk factors**
- Autosomal dominant inheritance with incomplete penetrance is typical; reduced penetrance in females is reported in management literature. (levitt2008practicalaspectsin pages 6-8)
- Several disease-associated variants are located in voltage-sensor S4 segments; for example, the **SCN4A p.R1135H** variant is located in the S4 segment of domain III and is discussed as neutralizing an arginine residue and contributing to aberrant gating-pore leak currents. (zhang2023casereportscn4a pages 3-4)

**Environmental/physiologic triggers (attack precipitants)**
Triggers repeatedly reported across reviews and case reports include:
- **High-carbohydrate meals** and **rest after strenuous exercise** (statland2018reviewofthe pages 34-39, statland2018reviewofthe pages 7-11)
- **Alcohol** and **stress** (statland2018reviewofthe pages 7-11)
- **High sodium/salt intake** (illustrated in a 2024 case after a high-salt meal) (brown2024familialhypokalemicperiodic pages 1-2)
- Additional reported triggers include cold exposure, corticosteroids, infections, and anesthesia-related events (reported in a 2023 case literature synthesis). (zhou2023anovelcacna1s pages 2-5)

**Secondary (non-genetic) causes of hypokalemic paralysis**
HypoPP-like episodes can occur secondary to disorders such as thyrotoxicosis (thyrotoxic periodic paralysis), renal tubular disorders, diuretics, and other systemic conditions. (cristina2022hypokalemicperiodicparalysis pages 1-2, zhang2023casereportscn4a pages 1-2)

### Protective factors
Direct evidence for “protective factors” (genetic or environmental) specific to HypoPP was not identified in the retrieved evidence set.

### Gene–environment interactions
The classic interaction is genotype-based susceptibility plus physiologic potassium shifts. A mechanistic summary in a review describes attack triggers such as high-carbohydrate meals and rest after exercise acting via insulin-mediated intracellular potassium shifts (Na+/K+-ATPase activation), which precipitate weakness in genetically susceptible muscle. (cristina2022hypokalemicperiodicparalysis pages 1-2)


## 3. Phenotypes (clinical, laboratory, QoL) and HPO mapping

### Core phenotype spectrum
**Episodic weakness/paralysis**
- Clinical syndrome: episodic flaccid weakness/paralysis (often proximal, can be generalized). (statland2018reviewofthe pages 7-11)
- Typical onset: **5–35 years**, often first/second decade; attacks may occur at night/on awakening. (statland2018reviewofthe pages 34-39, luo2026clinicalfeaturesand pages 2-5)
- Typical duration: often **>2 hours**. (statland2018reviewofthe pages 34-39)

**Laboratory abnormalities during attacks**
- Documented hypokalemia is central; supportive criteria include serum K+ **<3.5 mEq/L** during attacks. (statland2018reviewofthe pages 34-39)
- Case-based data show severe ictal hypokalemia: e.g., potassium **1.8–2.1 mmol/L** in a pediatric CACNA1S case; CK elevation **211–1036 U/L** was also reported. (zhou2023anovelcacna1s pages 2-5, zhou2023anovelcacna1s pages 1-2)

**Permanent weakness / progressive myopathy**
HypoPP can evolve beyond episodic attacks to fixed weakness and fatty replacement on MRI.
- A 2023 3-year follow-up study in **37 CACNA1S** mutation carriers reported baseline phenotypes: **21 periodic paralysis (PP)**, **12 mixed weakness (MW)**, **2 permanent weakness (PW)**, and **2 asymptomatic**. Over follow-up, **muscle strength declined in 11/37** and **MRI fat replacement increased in 27/37**, including progression in some individuals without attacks during follow-up. (holmyildiz2023hypokalemicperiodicparalysis pages 1-2)

### Quality-of-life impact
The evidence set includes that quality-of-life instruments (e.g., EQ-5D-5L, INQoL) are used as outcomes in an ongoing training intervention trial in periodic paralysis (including HypoPP). (NCT07194174 chunk 1) Disease-specific QoL statistics were not directly extractable from the retrieved sources.

### Suggested HPO terms (examples)
Based on phenotypes explicitly supported in the evidence:
- Episodic muscle weakness/paralysis: **Muscle weakness (HP:0001324)**; **Acute flaccid paralysis (HP:0002016)** (conceptual mapping; attacks described as flaccid weakness) (statland2018reviewofthe pages 7-11)
- Hypokalemia: **Hypokalemia (HP:0002900)** (statland2018reviewofthe pages 34-39)
- Elevated creatine kinase (during attacks): **Elevated circulating creatine kinase concentration (HP:0003236)** (zhou2023anovelcacna1s pages 1-2)
- Respiratory muscle paralysis (rare/severe cases): **Respiratory insufficiency (HP:0002093)** / **Respiratory muscle weakness (HP:0002747)** (supported by case with intubation) (zhang2023casereportscn4a pages 2-3)
- Abnormal muscle MRI fat replacement: **Abnormal muscle MRI (HP:0033783)** (conceptual mapping; MRI fat replacement progression described) (holmyildiz2023hypokalemicperiodicparalysis pages 1-2)


## 4. Genetic / molecular information

### Causal genes
- **CACNA1S** (major gene) (statland2018reviewofthe pages 7-11)
- **SCN4A** (second major gene) (statland2018reviewofthe pages 7-11)

### Pathogenic variants and variant classes (examples from recent literature in this run)
- **CACNA1S c.1583G>A (p.R528H)**: identified as pathogenic in a 2024 familial HypoPP case with concurrent Graves’ disease; sequencing in that report was normal for SCN4A, KCNJ2, KCNJ18. (brown2024familialhypokalemicperiodic pages 1-2)
- **CACNA1S c.497C>A (p.Ala166Asp)**: novel heterozygous variant in a pediatric case; classified “likely pathogenic” per ACMG in the report and mapped to an S4 voltage-sensor segment (domain I). (zhou2023anovelcacna1s pages 1-2)
- **SCN4A c.3404G>A (p.R1135H)**: missense variant associated with HPP; in a 2023 report, co-occurred with Graves’ disease and severe hypokalemia (nadir 1.59 mmol/L) with respiratory paralysis. (zhang2023casereportscn4a pages 1-2, zhang2023casereportscn4a pages 2-3)

### Functional consequences (current model)
A key current mechanistic concept is that many HypoPP mutations create an abnormal “leak” (gating-pore current) in the voltage sensor, leading to paradoxical depolarization and muscle fiber inexcitability in the setting of low extracellular potassium. (statland2018reviewofthe pages 7-11, zhang2023casereportscn4a pages 3-4)

### Modifier genes / epigenetics / chromosomal abnormalities
No specific modifier genes, epigenetic mechanisms, or chromosomal abnormalities were identified in the retrieved evidence set.


## 5. Mechanism / pathophysiology (causal chain) + ontology mapping

### Causal chain (upstream → downstream)
1. **Inherited ion-channel variant** (CACNA1S or SCN4A) alters voltage-sensor function and permits anomalous leak currents (gating-pore current). (statland2018reviewofthe pages 7-11, zhang2023casereportscn4a pages 3-4)
2. **Trigger** (e.g., high-carbohydrate meal, rest after exercise) drives intracellular potassium shift (insulin/Na+/K+-ATPase related), lowering extracellular potassium. (cristina2022hypokalemicperiodicparalysis pages 1-2)
3. In low extracellular K+, affected fibers undergo **paradoxical depolarization** with inactivation of sodium channels → **reduced excitability** → **flaccid weakness/paralysis**. (statland2018reviewofthe pages 7-11)
4. Over time, some patients develop **progressive myopathy** with **fat replacement on muscle MRI**, which may progress even without frequent attacks. (holmyildiz2023hypokalemicperiodicparalysis pages 1-2)

### Suggested GO (biological process) terms (examples)
- **Regulation of membrane potential (GO:0042391)** (conceptual mapping to excitability changes) (statland2018reviewofthe pages 7-11)
- **Skeletal muscle contraction (GO:0003009)** (downstream functional impairment) (holmyildiz2023hypokalemicperiodicparalysis pages 1-2)
- **Potassium ion transmembrane transport (GO:0071805)** (trigger-related shifts) (cristina2022hypokalemicperiodicparalysis pages 1-2)

### Suggested CL (cell types)
- **Skeletal muscle cell / skeletal muscle fiber (CL:0000187)** (primary affected cell type) (statland2018reviewofthe pages 7-11)

### Suggested UBERON (anatomy)
- **Skeletal muscle tissue (UBERON:0001134)** (statland2018reviewofthe pages 7-11)

### Molecular profiling / omics / advanced technologies
Quantitative MRI is increasingly used as a biomarker of muscle involvement and progression (fat replacement). A 2023 cohort used whole-body muscle MRI with Mercuri scoring and observed progression in 27/37 over ~42 months. (holmyildiz2023hypokalemicperiodicparalysis pages 1-2)
An ongoing training trial uses MRI fat fraction (Dixon) as an outcome, reflecting movement toward quantitative imaging endpoints. (NCT07194174 chunk 1)


## 6. Inheritance and population

### Inheritance pattern
Autosomal dominant inheritance with incomplete penetrance is typical for primary HypoPP. (levitt2008practicalaspectsin pages 6-8, zhou2023anovelcacna1s pages 5-6)

### Epidemiology (statistics in retrieved evidence)
A review in the evidence set reports HypoPP prevalence around **~1/100,000**, and cites a UK estimate of **0.17/100,000** (as reported within the review text). (cristina2022hypokalemicperiodicparalysis pages 1-2)

Sex ratio: male predominance is reported (including reduced penetrance in females in older management literature), and some clinical literature notes higher frequency in males. (levitt2008practicalaspectsin pages 6-8, cristina2022hypokalemicperiodicparalysis pages 1-2)


## 7. Diagnostics

### Clinical diagnostic criteria (structured)
A consensus-style diagnostic framework summarized in Statland et al. includes:
- **≥2 attacks** with documented serum K+ **<3.5 mEq/L**, or
- 1 attack plus an affected relative with documented low K+, or
- **3 of 6** features: early onset, duration >2 h, typical triggers, improvement with potassium, family history/genetic confirmation, positive long exercise test; plus exclusion of other causes of hypokalemia and absence of myotonia (except possibly eyelids). (statland2018reviewofthe pages 34-39)

### Electrophysiology
- Long exercise testing supports diagnosis; a **≥40% CMAP decrement** is cited as supportive in a review. (cristina2022hypokalemicperiodicparalysis pages 1-2)

### Laboratory and secondary-cause evaluation
Practical management guidance emphasizes evaluating for endocrine/renal causes (e.g., thyroid function tests) and ECG monitoring; ECG monitoring is described as standard of care given hypokalemia-associated arrhythmia risk. (levitt2008practicalaspectsin pages 6-8)

### Genetic testing (real-world implementation)
- A positive genetic test with compatible symptoms is considered a gold standard in management literature; however, older management literature cautions that genetic testing can have high specificity but limited sensitivity (negative test does not exclude). (levitt2008practicalaspectsin pages 6-8)
- Recent case reports demonstrate real-world genetic workup distinguishing familial HypoPP (CACNA1S pathogenic variant) from thyrotoxic periodic paralysis patterns. (brown2024familialhypokalemicperiodic pages 1-2)

### Differential diagnosis
Secondary hypokalemic paralysis due to thyrotoxicosis is an important differential; overlap in attack characteristics is reported, and in new-onset hypokalemic paralysis, thyroid testing is emphasized. (zhang2023casereportscn4a pages 2-3, luo2026clinicalfeaturesand pages 2-5)


## 8. Outcomes / prognosis

### Natural history and progression
A key recent development is prospective documentation that HypoPP can behave as a **progressive myopathy**.
- In a 2023 3-year follow-up of genetically confirmed CACNA1S HypoPP (n=37), strength decline occurred in **11/37** and fat replacement increased in **27/37**, including in some participants without attacks during follow-up. (holmyildiz2023hypokalemicperiodicparalysis pages 1-2)

### Complications
- Cardiac arrhythmia risk during hypokalemia is emphasized (ECG monitoring; U-waves). (levitt2008practicalaspectsin pages 6-8)
- Severe respiratory involvement is rare but documented (case requiring intubation with K nadir 1.59 mmol/L in SCN4A p.R1135H with thyrotoxicosis). (zhang2023casereportscn4a pages 2-3)


## 9. Treatment

### Acute management
- **Potassium chloride** is the mainstay for acute attacks; practical dosing guidance includes **0.5–1.0 mEq/kg**, typically oral. (levitt2008practicalaspectsin pages 6-8)
- Careful monitoring is required to prevent rebound hyperkalemia; a severe hyperkalemia event after massive KCl ingestion was reported in a dichlorphenamide trial publication, underscoring safety needs. (tawil2000randomizedtrialsof pages 3-5)

### Preventive pharmacotherapy (and genotype-guided practice)
- **Carbonic anhydrase inhibitors (CAIs)** (acetazolamide, dichlorphenamide) are central preventive medications. (statland2018reviewofthe pages 15-20)
- **Genotype matters**: acetazolamide response differs markedly by gene—overall response **46%** in one genotyped cohort, with **CACNA1S 56%** vs **SCN4A 16%**; some SCN4A variants can worsen on CAIs. (statland2018reviewofthe pages 15-20)

### Dichlorphenamide evidence (primary literature)
A key placebo-controlled crossover trial in HypoPP (Annals of Neurology, 2000; DOI below) randomized **42** subjects (34 completed both phases) and found significant benefit:
- Among subjects expressing preference, **11 preferred dichlorphenamide vs 2 placebo (p=0.02)** (tawil2000randomizedtrialsof pages 3-5)
- In subjects with complete attack-rate data, mean improvement was **0.9 ± 1.4 attacks/week (p=0.02)** and severity-weighted improvement **1.1 ± 1.5 (p=0.01)** (tawil2000randomizedtrialsof pages 3-5)

Adverse effects included cognitive/mental status changes and paresthesias; cognitive effects were a common reason for dose reduction and dropouts. (tawil2000randomizedtrialsof pages 6-8, tawil2000randomizedtrialsof pages 3-5)

### Recent developments (2023–2024)
- **Progressive myopathy quantified by longitudinal MRI and strength testing** (Holm-Yildiz et al., 2023). (holmyildiz2023hypokalemicperiodicparalysis pages 1-2)
- **Genetic diagnosis and lifestyle prevention emphasized** in recent case reports and pediatric literature; e.g., the pediatric CACNA1S A166D report states: “**The attacks of the patient are prevented by lifestyle changes and nutritional counseling**.” (zhou2023anovelcacna1s pages 1-2)
- A 2024 case illustrates real-world management with combined endocrine + channelopathy care (Graves’ treated with methimazole plus acetazolamide prophylaxis; low carbohydrate and low salt diet). (brown2024familialhypokalemicperiodic pages 1-2)

### MAXO suggestions (examples)
- Potassium supplementation: **MAXO:0000747 (Potassium supplementation)** (conceptual; align to your MAXO version)
- Carbonic anhydrase inhibitor therapy: **MAXO:0000647 (Carbonic anhydrase inhibitor therapy)** (conceptual)
- Genetic counseling: **MAXO:0000073 (Genetic counseling)** (conceptual)


## 10. Prevention

### Primary/tertiary prevention (trigger avoidance)
Prevention in HypoPP is largely trigger management and individualized prophylaxis:
- Avoiding high-carbohydrate meals, rest after strenuous exercise, alcohol, stressors, and in some individuals high sodium intake is repeatedly emphasized. (statland2018reviewofthe pages 34-39, brown2024familialhypokalemicperiodic pages 1-2)
- Pediatric case literature emphasizes counseling/education; one report explicitly states attacks were prevented via lifestyle and nutritional counseling. (zhou2023anovelcacna1s pages 1-2)

### Genetic counseling and cascade testing
Because inheritance is often autosomal dominant, genetic diagnosis supports counseling and family risk assessment; a pediatric case report notes offspring risk of 50% for inheriting a pathogenic variant (general AD framing). (zhou2023anovelcacna1s pages 5-6)


## 11. Other species / natural disease
This tool-based run did not retrieve OMIA/animal case literature for naturally occurring HypoPP in non-human species; therefore, this section cannot be completed from the available evidence.


## 12. Model organisms / experimental models
Direct model-organism papers were not retrieved in full-text in this run; however, a clinical trial record explicitly cites preclinical rationale for bumetanide based on animal/model evidence in HypoPP (trial background references in the registry entry). (NCT02582476 chunk 2)


## 13. Current applications / real-world implementation

### Emergency and inpatient care
Real-world implementations emphasized by management literature include ECG monitoring during attacks and careful potassium replacement to avoid rebound hyperkalemia. (levitt2008practicalaspectsin pages 6-8, tawil2000randomizedtrialsof pages 3-5)

### Imaging as a clinical and research tool
Whole-body muscle MRI to quantify fat replacement is being applied in observational/natural history work and increasingly used as a biomarker. (holmyildiz2023hypokalemicperiodicparalysis pages 1-2)

### Clinical trials and ongoing research programs
- **NCT07194174** (Rigshospitalet, Denmark; start 2025-10-02; Recruiting): a 24-week prospective study assessing **supervised strength training**; outcomes include 5STS, 6MWT, dynamometry, attack counts, QoL instruments (INQoL, EQ-5D-5L), fatigue, pain, and **MRI Dixon fat fraction**. (NCT07194174 chunk 1)
- **NCT02582476** (UCL; Phase II; terminated): single-dose **bumetanide** vs placebo for induced focal hand-muscle weakness; planned n=12; terminated due to slow enrollment/funding. (NCT02582476 chunk 1)
- **NCT00004802** (dichlorphenamide; Completed; crossover): baseline 8 weeks, then 9-week DCP vs placebo with crossover; enrollment 64. (NCT00004802 chunk 1)


## 14. Figures/tables (visual evidence)
A representative MRI figure and a cohort table were retrieved from the 2023 longitudinal follow-up study, illustrating progression of fat replacement and summarizing phenotype categories (PP/MW/PW). (holmyildiz2023hypokalemicperiodicparalysis media 3d8d3fed, holmyildiz2023hypokalemicperiodicparalysis media 82a46c85)


# Embedded evidence tables

The following evidence tables summarize core disease concepts and treatment evidence extracted in this run.

| Topic | Key points | Key sources (with year, journal, DOI/URL if present) |
|---|---|---|
| Definition | Hypokalemic periodic paralysis (HypoPP) is a rare inherited skeletal muscle channelopathy characterized by recurrent episodes of flaccid muscle weakness/paralysis associated with low serum potassium during attacks; interictal potassium is typically normal. Attacks may be focal or generalized and usually last hours to days. (cristina2022hypokalemicperiodicparalysis pages 1-2, statland2018reviewofthe pages 7-11) | Statland et al., 2018, *Muscle & Nerve*, https://doi.org/10.1002/mus.26009; Cristina & Espadinha, 2022, review, source URL not fully available in context. |
| Inheritance | Primary HypoPP is typically autosomal dominant with incomplete penetrance, including reduced penetrance in some females. Family history is common, though de novo cases can occur. (levitt2008practicalaspectsin pages 6-8, zhou2023anovelcacna1s pages 5-6) | Levitt, 2008, *Journal of Translational Medicine*, https://doi.org/10.1186/1479-5876-6-18; Zhou et al., 2023, *BMC Pediatrics*, https://doi.org/10.1186/s12887-023-04326-1 |
| Common triggers | Recurrent attacks are commonly triggered by high-carbohydrate meals, rest after strenuous exercise, strenuous exercise itself, alcohol, stress/emotional stress; additional reported triggers include high sodium/salt intake, cold exposure, corticosteroids, infections, anesthesia, and thyrotoxicosis in secondary forms. (cristina2022hypokalemicperiodicparalysis pages 1-2, statland2018reviewofthe pages 34-39, statland2018reviewofthe pages 7-11, zhou2023anovelcacna1s pages 2-5, brown2024familialhypokalemicperiodic pages 1-2) | Statland et al., 2018, *Muscle & Nerve*, https://doi.org/10.1002/mus.26009; Cristina & Espadinha, 2022, review; Zhou et al., 2023, *BMC Pediatrics*, https://doi.org/10.1186/s12887-023-04326-1; Brown et al., 2024, *BMC Nephrology*, https://doi.org/10.1186/s12882-024-03749-x |
| Typical onset / attack duration | Age at onset is usually 5–35 years, often first or second decade; attack frequency is often highest from 15–35 years. Mean attack duration is typically >2 hours, and attacks may last hours to days; some series note nocturnal or awakening onset. (statland2018reviewofthe pages 34-39, statland2018reviewofthe pages 7-11, luo2026clinicalfeaturesand pages 2-5) | Statland et al., 2018, *Muscle & Nerve*, https://doi.org/10.1002/mus.26009; Luo et al., 2026, *PeerJ*, https://doi.org/10.7717/peerj.20840 |
| Main causal genes and approximate proportions | CACNA1S is the major causal gene (~60% of kindreds in one review; 70–80% of cases in another review/case synthesis), while SCN4A accounts for ~20% of kindreds or ~10% of cases depending on cohort/ascertainment. CACNA1S-related disease is termed HypoPP type 1; SCN4A-related disease is HypoPP type 2. (statland2018reviewofthe pages 7-11, cammaratascalisi2026covid19infectionand pages 2-4, luo2026clinicalfeaturesand pages 5-6) | Statland et al., 2018, *Muscle & Nerve*, https://doi.org/10.1002/mus.26009; Cammarata-Scalisi et al., 2026, *Boletín Médico del Hospital Infantil de México*, https://doi.org/10.24875/bmhime.m24000089; Luo et al., 2026, *PeerJ*, https://doi.org/10.7717/peerj.20840 |
| Diagnostic criteria elements | Supportive diagnostic criteria include: documented low serum potassium during attacks (<3.5 mEq/L) in at least 2 attacks, or in 1 attack plus an affected relative; alternatively 3 of 6 features such as onset in first/second decade, attack duration >2 h, typical triggers, improvement with potassium, positive family history/genetic confirmation, or positive long exercise test. Other causes of hypokalemia should be excluded and myotonia should be absent except possibly eyelid myotonia. (statland2018reviewofthe pages 34-39) | Statland et al., 2018, *Muscle & Nerve*, https://doi.org/10.1002/mus.26009 |
| Electrophysiology / long exercise test | An abnormal long exercise test supports diagnosis when genetic testing is negative or incomplete. Exercise testing has largely replaced provocative maneuvers; an abnormal compound muscle action potential (CMAP) decrement of ≥40% is reported as supportive. (cristina2022hypokalemicperiodicparalysis pages 1-2, statland2018reviewofthe pages 34-39) | Statland et al., 2018, *Muscle & Nerve*, https://doi.org/10.1002/mus.26009; Cristina & Espadinha, 2022, review. |
| Key complications: permanent weakness / myopathy | Beyond episodic paralysis, many patients develop a variable proximal myopathy or fixed/permanent weakness, which may progress independently of attack frequency. In a 3-year CACNA1S follow-up cohort (n=37), baseline phenotypes were 21 periodic paralysis, 12 mixed weakness, 2 permanent weakness, and 2 asymptomatic; muscle strength declined in 11/37 and MRI fat replacement increased in 27/37, including some patients without attacks during follow-up. (statland2018reviewofthe pages 7-11, holmyildiz2023hypokalemicperiodicparalysis pages 2-4, holmyildiz2023hypokalemicperiodicparalysis pages 1-2, holmyildiz2023hypokalemicperiodicparalysis pages 4-6) | Statland et al., 2018, *Muscle & Nerve*, https://doi.org/10.1002/mus.26009; Holm-Yildiz et al., 2023, *Journal of Neurology*, https://doi.org/10.1007/s00415-023-11964-z |
| Genotype-phenotype note relevant to complications | Calcium-channel (CACNA1S) mutations are associated with higher risk of permanent weakness than sodium-channel mutations in older management literature; response to carbonic anhydrase inhibitors also differs by genotype. (levitt2008practicalaspectsin pages 6-8, statland2018reviewofthe pages 15-20) | Levitt, 2008, *Journal of Translational Medicine*, https://doi.org/10.1186/1479-5876-6-18; Statland et al., 2018, *Muscle & Nerve*, https://doi.org/10.1002/mus.26009 |


*Table: This table compiles key extracted evidence for Hypokalemic Periodic Paralysis, including core disease features, genetics, triggers, diagnosis, and major complications. It is useful as a concise evidence-backed reference for building a disease knowledge base entry.*

| Treatment/Intervention | Use (acute/prophylaxis) | Evidence & key quantitative results | Safety/monitoring | Key citations (with DOI/URL where present) |
|---|---|---|---|---|
| Potassium chloride (oral preferred; IV if needed) | Acute attack treatment | Potassium is the mainstay of acute treatment and typically improves or resolves attacks. Practical dosing guidance from management literature is **0.5–1.0 mEq/kg** for acute attacks; oral KCl is preferred, with IV use when necessary. Supportive diagnostic criteria also include improvement with potassium intake. Potassium remains a cornerstone therapy in reviews/guidelines, and magnesium may be added to reduce renal potassium wasting. (levitt2008practicalaspectsin pages 6-8, statland2018reviewofthe pages 15-20, statland2018reviewofthe pages 34-39) | Monitor ECG and serum potassium closely because rebound hyperkalemia can occur; arrhythmia screening is recommended during attacks. One trial report described a serious safety event from unsupervised massive KCl ingestion (**690 mEq**, serum K+ **9.8 mmol/L**) requiring ICU treatment. (levitt2008practicalaspectsin pages 6-8, tawil2000randomizedtrialsof pages 3-5) | Levitt 2008, *J Transl Med*, https://doi.org/10.1186/1479-5876-6-18 (levitt2008practicalaspectsin pages 6-8); Statland et al. 2018, *Muscle & Nerve*, https://doi.org/10.1002/mus.26009 (statland2018reviewofthe pages 15-20, statland2018reviewofthe pages 34-39); Tawil et al. 2000, *Ann Neurol*, https://doi.org/10.1002/1531-8249(200001)47:1<46::aid-ana9>3.0.co;2-h (tawil2000randomizedtrialsof pages 3-5) |
| Trigger avoidance + potassium prophylaxis when needed | Prophylaxis / tertiary prevention | Behavioral prevention is standard adjunctive care: avoid rest after strenuous exercise, high-carbohydrate meals, and sodium/salt triggers; potassium prophylaxis may help in trigger-prone situations. This is emphasized in management reviews and recent case literature. (levitt2008practicalaspectsin pages 6-8, brown2024familialhypokalemicperiodic pages 1-2) | Individualize to trigger profile; monitor potassium if frequent supplementation is used. (levitt2008practicalaspectsin pages 6-8) | Levitt 2008, *J Transl Med*, https://doi.org/10.1186/1479-5876-6-18 (levitt2008practicalaspectsin pages 6-8); Brown et al. 2024, *BMC Nephrology*, https://doi.org/10.1186/s12882-024-03749-x (brown2024familialhypokalemicperiodic pages 1-2) |
| Acetazolamide (carbonic anhydrase inhibitor) | Preventive / prophylaxis | Long used empirically for attack prevention. In a genotyped cohort (**n=74**), overall response was **46%**; response differed by genotype: **CACNA1S 56% (31/55)** vs **SCN4A 16% (3/19)**, supporting genotype-guided use. Recent case reports continue to use acetazolamide as preventive therapy (e.g., **250 mg twice daily** in one 2024 case). (statland2018reviewofthe pages 15-20, brown2024familialhypokalemicperiodic pages 1-2) | Can worsen symptoms in some genotypes, especially certain **SCN4A** variants; reported worsening variants include **SCN4A R672G/R672S** and **CACNA1S R1239H**. Monitor for paresthesia, fatigue, cognitive adverse effects, dysgeusia, headache, and nephrolithiasis. (statland2018reviewofthe pages 15-20, zhou2023anovelcacna1s pages 5-6, zhang2023casereportscn4a pages 2-3) | Matthews et al. 2011, *Neurology*, https://doi.org/10.1212/wnl.0b013e31823a0cb6 (statland2018reviewofthe pages 15-20); Statland et al. 2018, *Muscle & Nerve*, https://doi.org/10.1002/mus.26009 (statland2018reviewofthe pages 15-20); Brown et al. 2024, *BMC Nephrology*, https://doi.org/10.1186/s12882-024-03749-x (brown2024familialhypokalemicperiodic pages 1-2) |
| Dichlorphenamide (carbonic anhydrase inhibitor; DCP) | Preventive / prophylaxis | Best-supported preventive drug. In randomized placebo-controlled crossover trials, DCP significantly reduced attack burden. In the classic HypoPP trial, **42** subjects were randomized and **34 (81%)** completed both phases; among **13** subjects expressing preference, **11** preferred DCP vs **2** placebo (**p=0.02**). In **17** subjects with attack-rate data for both phases, mean improvement on DCP vs placebo was **0.9 ± 1.4 attacks/week (p=0.02)** and severity-weighted attack-rate improvement was **1.1 ± 1.5 (p=0.01)**; analyses including endpoint subjects strengthened significance (**attack rate p=0.001; severity-weighted p=0.007**). Later reviews note FDA approval and significant reduction in attack frequency/severity. (tawil2000randomizedtrialsof pages 6-8, tawil2000randomizedtrialsof pages 3-5, statland2018reviewofthe pages 15-20, desaphy2021targetedtherapiesfor pages 12-14) | Common adverse effects: paresthesia, fatigue, cognitive symptoms/mental status change, dysgeusia, headache, hypoesthesia, muscle spasms; cognitive effects caused dose reductions and some dropouts. Kidney-stone risk exists; nephrolithiasis screening/monitoring is advisable. (tawil2000randomizedtrialsof pages 6-8, tawil2000randomizedtrialsof pages 3-5, statland2018reviewofthe pages 15-20, tawil2000randomizedtrialsof pages 5-6) | Tawil et al. 2000, *Ann Neurol*, https://doi.org/10.1002/1531-8249(200001)47:1<46::aid-ana9>3.0.co;2-h (tawil2000randomizedtrialsof pages 6-8, tawil2000randomizedtrialsof pages 3-5, tawil2000randomizedtrialsof pages 5-6); Statland et al. 2018, *Muscle & Nerve*, https://doi.org/10.1002/mus.26009 (statland2018reviewofthe pages 15-20); Desaphy et al. 2021, *J Neuromuscul Dis*, https://doi.org/10.3233/jnd-200582 (desaphy2021targetedtherapiesfor pages 12-14) |
| NCT00004802: Phase III randomized, double-blind, placebo-controlled crossover dichlorphenamide study | Clinical trial evidence for prophylaxis | ClinicalTrials.gov record for a Phase III treatment trial in periodic paralyses including HypoPP. Design: **8-week baseline**, randomization to oral DCP or placebo for **9 weeks**, then crossover to the alternate arm; enrollment **64**; completed. Outcomes focused on **weekly attack rate** and episodic weakness frequency, with ACZ-to-DCP dose conversion at **one-fifth** the acetazolamide dose for prior ACZ users. (NCT00004802 chunk 1) | Excluded significant hepatic, renal, cardiac, pulmonary, or thyroid disease and pregnancy; crossover design included clinical monitoring. (NCT00004802 chunk 1) | ClinicalTrials.gov NCT00004802, started 1992-06, completed; record summarized in context (NCT00004802 chunk 1) |
| NCT02582476: Bumetanide in HypoPP | Experimental / proof-of-concept | Phase II randomized, double-blind, placebo-controlled crossover study testing **single-dose bumetanide** vs placebo for an induced focal hand-muscle attack. Planned enrollment **12** genetically confirmed HypoPP participants; primary endpoint was focal attack severity at **1 hour** measured by CMAP amplitude % of peak. Trial was **terminated for slow enrolment/end of funding**. (NCT02582476 chunk 1) | Frequent vitals, serum potassium, labs, AE monitoring up to 7 days; carbonic anhydrase inhibitors withheld **72 h** before visits. (NCT02582476 chunk 1) | ClinicalTrials.gov NCT02582476, University College London, start Jan 2015, primary/completion 2017-05-09 (NCT02582476 chunk 1) |


*Table: This table summarizes acute and preventive treatments for hypokalemic periodic paralysis, including potassium replacement, acetazolamide, dichlorphenamide, genotype-response patterns, and key clinical trial evidence. It is useful as a concise evidence-backed treatment reference for a disease knowledge base entry.*


# Key source URLs (with publication dates as available)
- Statland et al. “Review of the Diagnosis and Treatment of Periodic Paralysis.” *Muscle & Nerve* (Nov 2018). https://doi.org/10.1002/mus.26009 (statland2018reviewofthe pages 15-20, statland2018reviewofthe pages 34-39, statland2018reviewofthe pages 7-11)
- Holm‑Yildiz et al. “Hypokalemic periodic paralysis: a 3-year follow-up study.” *Journal of Neurology* (Sep 2023). https://doi.org/10.1007/s00415-023-11964-z (holmyildiz2023hypokalemicperiodicparalysis pages 1-2)
- Zhou et al. “A novel CACNA1S gene variant in a child with hypokalemic periodic paralysis: a case report and literature review.” *BMC Pediatrics* (Oct 2023). https://doi.org/10.1186/s12887-023-04326-1 (zhou2023anovelcacna1s pages 1-2)
- Brown et al. “Familial hypokalemic periodic paralysis: a case induced by concurrent hyperthyroidism.” *BMC Nephrology* (Sep 2024). https://doi.org/10.1186/s12882-024-03749-x (brown2024familialhypokalemicperiodic pages 1-2)
- Zhang & Xiao. “SCN4A p.R1135H gene variant in combination with thyrotoxicosis causing hypokalemic periodic paralysis.” *Frontiers in Neurology* (Jan 2023). https://doi.org/10.3389/fneur.2022.1078784 (zhang2023casereportscn4a pages 1-2, zhang2023casereportscn4a pages 2-3)
- Tawil et al. “Randomized trials of dichlorphenamide in the periodic paralyses.” *Annals of Neurology* (Jan 2000). https://doi.org/10.1002/1531-8249(200001)47:1<46::aid-ana9>3.0.co;2-h (tawil2000randomizedtrialsof pages 3-5)
- ClinicalTrials.gov: NCT02582476 (start Jan 2015; terminated; completion 2017-05-09). (NCT02582476 chunk 1)
- ClinicalTrials.gov: NCT07194174 (actual start 2025-10-02; recruiting; estimated completion 2026-12-01). (NCT07194174 chunk 1)
- ClinicalTrials.gov: NCT00004802 (start 1992-06; completed; last update estimated 2005-06-24). (NCT00004802 chunk 1)


## Evidence limitations (important for knowledge base population)
- **OMIM/Orphanet/MeSH/ICD/MONDO identifiers** were not retrieved by tools in this run; they should be added by direct database queries.
- **PMIDs** were not available for several sources in the extracted evidence snippets; where PMIDs are required, the DOI/URL-based papers above should be cross-referenced in PubMed to capture PMIDs.
- Modifier genes, epigenetic data, and non-human natural disease models were not identified in the current retrieved set.

References

1. (cristina2022hypokalemicperiodicparalysis pages 1-2): SF Cristina and V Espadinha. Hypokalemic periodic paralysis: a review of pathophysiology, clinical features, and treatment. Unknown journal, 2022.

2. (statland2018reviewofthe pages 7-11): Jeffrey M. Statland, Bertrand Fontaine, Michael G. Hanna, Nicholas E. Johnson, John T. Kissel, Valeria A. Sansone, Perry B. Shieh, Rabi N. Tawil, Jaya Trivedi, Stephen C. Cannon, and Robert C. Griggs. Review of the diagnosis and treatment of periodic paralysis. Muscle & Nerve, 57:522-530, Nov 2018. URL: https://doi.org/10.1002/mus.26009, doi:10.1002/mus.26009. This article has 323 citations and is from a peer-reviewed journal.

3. (zhou2023anovelcacna1s pages 1-2): Wen Zhou, Peilin Zhao, Jian Gao, and Yunjian Zhang. A novel cacna1s gene variant in a child with hypokalemic periodic paralysis: a case report and literature review. BMC Pediatrics, Oct 2023. URL: https://doi.org/10.1186/s12887-023-04326-1, doi:10.1186/s12887-023-04326-1. This article has 14 citations and is from a peer-reviewed journal.

4. (brown2024familialhypokalemicperiodic pages 1-2): Leanne Brown, Zein Alabdin Hannouneh, C. E. Cervantes, J. Sperati, and Mohamad A. Hanouneh. Familial hypokalemic periodic paralysis: a case induced by concurrent hyperthyroidism. BMC Nephrology, Sep 2024. URL: https://doi.org/10.1186/s12882-024-03749-x, doi:10.1186/s12882-024-03749-x. This article has 1 citations and is from a peer-reviewed journal.

5. (luo2026clinicalfeaturesand pages 5-6): Man Luo, Beibei Liu, Junjie Xu, and Danyang Meng. Clinical features and advances in the genetics of periodic paralysis. PeerJ, 14:e20840, Mar 2026. URL: https://doi.org/10.7717/peerj.20840, doi:10.7717/peerj.20840. This article has 1 citations and is from a peer-reviewed journal.

6. (statland2018reviewofthe pages 15-20): Jeffrey M. Statland, Bertrand Fontaine, Michael G. Hanna, Nicholas E. Johnson, John T. Kissel, Valeria A. Sansone, Perry B. Shieh, Rabi N. Tawil, Jaya Trivedi, Stephen C. Cannon, and Robert C. Griggs. Review of the diagnosis and treatment of periodic paralysis. Muscle & Nerve, 57:522-530, Nov 2018. URL: https://doi.org/10.1002/mus.26009, doi:10.1002/mus.26009. This article has 323 citations and is from a peer-reviewed journal.

7. (holmyildiz2023hypokalemicperiodicparalysis pages 1-2): Sonja Holm-Yildiz, Thomas Krag, Nanna Witting, Britt Stævnsbo Pedersen, Tina Dysgaard, Louise Sloth, Jonas Pedersen, Rebecca Kjær, Linda Kannuberg, Julia Dahlqvist, Josefine de Stricker Borch, Tuva Solheim, Freja Fornander, Anne-Sofie Eisum, and John Vissing. Hypokalemic periodic paralysis: a 3-year follow-up study. Journal of Neurology, 270:6057-6063, Sep 2023. URL: https://doi.org/10.1007/s00415-023-11964-z, doi:10.1007/s00415-023-11964-z. This article has 21 citations and is from a domain leading peer-reviewed journal.

8. (cammaratascalisi2026covid19infectionand pages 2-4): Francisco Cammarata-Scalisi, Esteban San Martín, Antonio Cárdenas-Tadich, Maykol Araya-Castillo, Carolina Peralta-Aros, Víctor Olivares, Enrico Bertini, Colin E. Willoughby, and Michele Callea. Covid-19 infection and intense physical activity in hypokalemic periodic paralysis. Boletín Médico del Hospital Infantil de México (English Edition), 82:252-257, Feb 2026. URL: https://doi.org/10.24875/bmhime.m24000089, doi:10.24875/bmhime.m24000089. This article has 0 citations.

9. (levitt2008practicalaspectsin pages 6-8): Jacob O Levitt. Practical aspects in the management of hypokalemic periodic paralysis. Journal of Translational Medicine, 6:18-18, Apr 2008. URL: https://doi.org/10.1186/1479-5876-6-18, doi:10.1186/1479-5876-6-18. This article has 111 citations and is from a peer-reviewed journal.

10. (zhang2023casereportscn4a pages 3-4): Zhi Zhang and Banghui Xiao. Case report: scn4a p.r1135h gene variant in combination with thyrotoxicosis causing hypokalemic periodic paralysis. Frontiers in Neurology, Jan 2023. URL: https://doi.org/10.3389/fneur.2022.1078784, doi:10.3389/fneur.2022.1078784. This article has 4 citations and is from a peer-reviewed journal.

11. (statland2018reviewofthe pages 34-39): Jeffrey M. Statland, Bertrand Fontaine, Michael G. Hanna, Nicholas E. Johnson, John T. Kissel, Valeria A. Sansone, Perry B. Shieh, Rabi N. Tawil, Jaya Trivedi, Stephen C. Cannon, and Robert C. Griggs. Review of the diagnosis and treatment of periodic paralysis. Muscle & Nerve, 57:522-530, Nov 2018. URL: https://doi.org/10.1002/mus.26009, doi:10.1002/mus.26009. This article has 323 citations and is from a peer-reviewed journal.

12. (zhou2023anovelcacna1s pages 2-5): Wen Zhou, Peilin Zhao, Jian Gao, and Yunjian Zhang. A novel cacna1s gene variant in a child with hypokalemic periodic paralysis: a case report and literature review. BMC Pediatrics, Oct 2023. URL: https://doi.org/10.1186/s12887-023-04326-1, doi:10.1186/s12887-023-04326-1. This article has 14 citations and is from a peer-reviewed journal.

13. (zhang2023casereportscn4a pages 1-2): Zhi Zhang and Banghui Xiao. Case report: scn4a p.r1135h gene variant in combination with thyrotoxicosis causing hypokalemic periodic paralysis. Frontiers in Neurology, Jan 2023. URL: https://doi.org/10.3389/fneur.2022.1078784, doi:10.3389/fneur.2022.1078784. This article has 4 citations and is from a peer-reviewed journal.

14. (luo2026clinicalfeaturesand pages 2-5): Man Luo, Beibei Liu, Junjie Xu, and Danyang Meng. Clinical features and advances in the genetics of periodic paralysis. PeerJ, 14:e20840, Mar 2026. URL: https://doi.org/10.7717/peerj.20840, doi:10.7717/peerj.20840. This article has 1 citations and is from a peer-reviewed journal.

15. (NCT07194174 chunk 1): Annica Buss Enegaard. Effect of Physical Training in Individuals With Hypokalemic and Hyperkalemic Periodic Paralysis. Rigshospitalet, Denmark. 2025. ClinicalTrials.gov Identifier: NCT07194174

16. (zhang2023casereportscn4a pages 2-3): Zhi Zhang and Banghui Xiao. Case report: scn4a p.r1135h gene variant in combination with thyrotoxicosis causing hypokalemic periodic paralysis. Frontiers in Neurology, Jan 2023. URL: https://doi.org/10.3389/fneur.2022.1078784, doi:10.3389/fneur.2022.1078784. This article has 4 citations and is from a peer-reviewed journal.

17. (zhou2023anovelcacna1s pages 5-6): Wen Zhou, Peilin Zhao, Jian Gao, and Yunjian Zhang. A novel cacna1s gene variant in a child with hypokalemic periodic paralysis: a case report and literature review. BMC Pediatrics, Oct 2023. URL: https://doi.org/10.1186/s12887-023-04326-1, doi:10.1186/s12887-023-04326-1. This article has 14 citations and is from a peer-reviewed journal.

18. (tawil2000randomizedtrialsof pages 3-5): Rabi Tawil, Michael P. McDermott, Robert Brown, Barbara C. Shapiro, Louis J. Ptacek, Philip G. McManis, Marinos C. Dalakas, Sidney A. Spector, Jerry R. Mendell, Angelika F. Hahn, and Robert C. Griggs. Randomized trials of dichlorphenamide in the periodic paralyses. Annals of Neurology, 47:46-53, Jan 2000. URL: https://doi.org/10.1002/1531-8249(200001)47:1<46::aid-ana9>3.0.co;2-h, doi:10.1002/1531-8249(200001)47:1<46::aid-ana9>3.0.co;2-h. This article has 179 citations and is from a highest quality peer-reviewed journal.

19. (tawil2000randomizedtrialsof pages 6-8): Rabi Tawil, Michael P. McDermott, Robert Brown, Barbara C. Shapiro, Louis J. Ptacek, Philip G. McManis, Marinos C. Dalakas, Sidney A. Spector, Jerry R. Mendell, Angelika F. Hahn, and Robert C. Griggs. Randomized trials of dichlorphenamide in the periodic paralyses. Annals of Neurology, 47:46-53, Jan 2000. URL: https://doi.org/10.1002/1531-8249(200001)47:1<46::aid-ana9>3.0.co;2-h, doi:10.1002/1531-8249(200001)47:1<46::aid-ana9>3.0.co;2-h. This article has 179 citations and is from a highest quality peer-reviewed journal.

20. (NCT02582476 chunk 2):  Bumetanide in Hypokalaemic Periodic Paralysis. University College, London. 2015. ClinicalTrials.gov Identifier: NCT02582476

21. (NCT02582476 chunk 1):  Bumetanide in Hypokalaemic Periodic Paralysis. University College, London. 2015. ClinicalTrials.gov Identifier: NCT02582476

22. (NCT00004802 chunk 1):  Phase III Randomized, Double-Blind, Placebo-Controlled Study of Dichlorphenamide for Periodic Paralyses and Associated Sodium Channel Disorders. National Center for Research Resources (NCRR). 1992. ClinicalTrials.gov Identifier: NCT00004802

23. (holmyildiz2023hypokalemicperiodicparalysis media 3d8d3fed): Sonja Holm-Yildiz, Thomas Krag, Nanna Witting, Britt Stævnsbo Pedersen, Tina Dysgaard, Louise Sloth, Jonas Pedersen, Rebecca Kjær, Linda Kannuberg, Julia Dahlqvist, Josefine de Stricker Borch, Tuva Solheim, Freja Fornander, Anne-Sofie Eisum, and John Vissing. Hypokalemic periodic paralysis: a 3-year follow-up study. Journal of Neurology, 270:6057-6063, Sep 2023. URL: https://doi.org/10.1007/s00415-023-11964-z, doi:10.1007/s00415-023-11964-z. This article has 21 citations and is from a domain leading peer-reviewed journal.

24. (holmyildiz2023hypokalemicperiodicparalysis media 82a46c85): Sonja Holm-Yildiz, Thomas Krag, Nanna Witting, Britt Stævnsbo Pedersen, Tina Dysgaard, Louise Sloth, Jonas Pedersen, Rebecca Kjær, Linda Kannuberg, Julia Dahlqvist, Josefine de Stricker Borch, Tuva Solheim, Freja Fornander, Anne-Sofie Eisum, and John Vissing. Hypokalemic periodic paralysis: a 3-year follow-up study. Journal of Neurology, 270:6057-6063, Sep 2023. URL: https://doi.org/10.1007/s00415-023-11964-z, doi:10.1007/s00415-023-11964-z. This article has 21 citations and is from a domain leading peer-reviewed journal.

25. (holmyildiz2023hypokalemicperiodicparalysis pages 2-4): Sonja Holm-Yildiz, Thomas Krag, Nanna Witting, Britt Stævnsbo Pedersen, Tina Dysgaard, Louise Sloth, Jonas Pedersen, Rebecca Kjær, Linda Kannuberg, Julia Dahlqvist, Josefine de Stricker Borch, Tuva Solheim, Freja Fornander, Anne-Sofie Eisum, and John Vissing. Hypokalemic periodic paralysis: a 3-year follow-up study. Journal of Neurology, 270:6057-6063, Sep 2023. URL: https://doi.org/10.1007/s00415-023-11964-z, doi:10.1007/s00415-023-11964-z. This article has 21 citations and is from a domain leading peer-reviewed journal.

26. (holmyildiz2023hypokalemicperiodicparalysis pages 4-6): Sonja Holm-Yildiz, Thomas Krag, Nanna Witting, Britt Stævnsbo Pedersen, Tina Dysgaard, Louise Sloth, Jonas Pedersen, Rebecca Kjær, Linda Kannuberg, Julia Dahlqvist, Josefine de Stricker Borch, Tuva Solheim, Freja Fornander, Anne-Sofie Eisum, and John Vissing. Hypokalemic periodic paralysis: a 3-year follow-up study. Journal of Neurology, 270:6057-6063, Sep 2023. URL: https://doi.org/10.1007/s00415-023-11964-z, doi:10.1007/s00415-023-11964-z. This article has 21 citations and is from a domain leading peer-reviewed journal.

27. (desaphy2021targetedtherapiesfor pages 12-14): Jean-François Desaphy, Concetta Altamura, Savine Vicart, and Bertrand Fontaine. Targeted therapies for skeletal muscle ion channelopathies: systematic review and steps towards precision medicine. Journal of Neuromuscular Diseases, 8:357-381, Dec 2021. URL: https://doi.org/10.3233/jnd-200582, doi:10.3233/jnd-200582. This article has 46 citations and is from a peer-reviewed journal.

28. (tawil2000randomizedtrialsof pages 5-6): Rabi Tawil, Michael P. McDermott, Robert Brown, Barbara C. Shapiro, Louis J. Ptacek, Philip G. McManis, Marinos C. Dalakas, Sidney A. Spector, Jerry R. Mendell, Angelika F. Hahn, and Robert C. Griggs. Randomized trials of dichlorphenamide in the periodic paralyses. Annals of Neurology, 47:46-53, Jan 2000. URL: https://doi.org/10.1002/1531-8249(200001)47:1<46::aid-ana9>3.0.co;2-h, doi:10.1002/1531-8249(200001)47:1<46::aid-ana9>3.0.co;2-h. This article has 179 citations and is from a highest quality peer-reviewed journal.
