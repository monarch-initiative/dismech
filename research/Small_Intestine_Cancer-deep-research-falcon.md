---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-07-15T10:22:46.108981'
end_time: '2026-07-15T10:45:23.691538'
duration_seconds: 1357.58
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Small Intestine Cancer
  mondo_id: ''
  category: ''
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 26
artifact_count: 3
artifact_sources:
  edison_answer_artifacts: 3
artifacts:
- filename: artifact-00.md
  path: Small_Intestine_Cancer-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: Small_Intestine_Cancer-deep-research-falcon_artifacts/artifact-01.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-01
- filename: artifact-02.md
  path: Small_Intestine_Cancer-deep-research-falcon_artifacts/artifact-02.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-02
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Small Intestine Cancer
- **MONDO ID:**  (if available)
- **Category:** 

## Research Objectives

Please provide a comprehensive research report on **Small Intestine Cancer** covering all of the
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
- **Disease Name:** Small Intestine Cancer
- **MONDO ID:**  (if available)
- **Category:** 

## Research Objectives

Please provide a comprehensive research report on **Small Intestine Cancer** covering all of the
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


## Comprehensive Research Report: Small Intestine Cancer (Small Bowel Cancer)

### Target Disease
- **Disease Name:** Small Intestine Cancer / Small Bowel Cancer (SBC)
- **MONDO ID:** Not retrieved from available sources in this run (gap)
- **Category:** Malignant neoplasm of the small intestine; umbrella term spanning multiple histologic entities (adenocarcinoma, neuroendocrine neoplasms, gastrointestinal stromal tumor, lymphoma) (borsotti2025hereditarycolorectalcancer pages 1-2)

---

## 1. Disease Information

### 1.1 Overview and current definition
“Small bowel cancer” (SBC) is a **rare malignancy of the small intestine**. A recent hereditary-syndrome-focused review defines SBC as comprising **four main histologic types: adenocarcinomas, neuroendocrine tumors, stromal tumors (including GIST), and lymphomas** (borsotti2025hereditarycolorectalcancer pages 1-2). In the same source, **adenocarcinoma and neuroendocrine tumors are described as the most common subtypes**, each representing approximately **~40%** of SBC, emphasizing that SBC is better treated as a *group of diseases* rather than a single entity (borsotti2025hereditarycolorectalcancer pages 1-2).

### 1.2 Anatomic distribution
Across SBC broadly, the **duodenum is the most frequently affected site (55–82%)**, followed by the jejunum (11–25%) and ileum (7–17%) (borsotti2025hereditarycolorectalcancer pages 1-2). In Lynch syndrome–associated small bowel cancers, nearly **50% occur in the duodenum** (borsotti2025hereditarycolorectalcancer pages 12-14).

### 1.3 Synonyms and alternative names
Commonly used synonyms in the clinical literature include:
- **Small bowel cancer**, **small intestine cancer**, **small-bowel tumor(s)** (in diagnostic guideline contexts) (pennazio2023smallbowelcapsuleendoscopy pages 8-9, pennazio2023smallbowelcapsuleendoscopy pages 21-21)
- Histology-specific entities: **small bowel adenocarcinoma (SBA)**, **small intestinal neuroendocrine tumor (SiNET; “midgut NET”)**, **small intestine GIST** (borsotti2025hereditarycolorectalcancer pages 1-2, strosberg2024sequencingofsomatostatinreceptor–based pages 1-2, serrano20232023geisguidelines pages 1-3)

### 1.4 Key identifiers (ICD/MeSH/OMIM/Orphanet/MONDO)
- **Not available from the retrieved full-text evidence** in this run. The literature sources accessed here primarily address clinical guidance, epidemiology, and treatment, and did not provide ontology identifiers (borsotti2025hereditarycolorectalcancer pages 1-2, pennazio2023smallbowelcapsuleendoscopy pages 8-9, serrano20232023geisguidelines pages 1-3).

### 1.5 Evidence source type
The information assembled here derives from **aggregated disease-level resources** (guidelines/reviews) and **population-level registry analyses (SEER-based studies)** rather than individual EHR case series (pennazio2023smallbowelcapsuleendoscopy pages 8-9, dasari2025epidemiologyofneuroendocrine pages 5-7, alvarez2024incidenceandsurvival pages 1-2).

---

## 2. Etiology

### 2.1 Disease causal factors and upstream causes
SBC etiology is **heterogeneous and histology-dependent**:
- **Hereditary cancer predisposition syndromes** (e.g., Lynch syndrome, FAP, Peutz–Jeghers syndrome) substantially elevate risk and motivate surveillance strategies (borsotti2025hereditarycolorectalcancer pages 1-2, borsotti2025hereditarycolorectalcancer pages 12-14, macfarland2024pediatriccancerscreening pages 5-6).
- **Molecularly driven mesenchymal oncogenesis in GIST** is dominated by **gain-of-function KIT or PDGFRA receptor tyrosine kinase mutations**, which are described as “crucial drivers” responsible for tumor initiation and evolution across disease course (serrano20232023geisguidelines pages 1-1).

### 2.2 Risk factors
#### 2.2.1 Genetic risk factors (high-confidence)
- **Lynch syndrome (LS/HNPCC)** is caused by germline pathogenic variants in mismatch repair genes **MLH1, MSH2, MSH6, PMS2**, or **EPCAM** deletions (autosomal dominant) (borsotti2025hereditarycolorectalcancer pages 12-14). A recent review reports lifetime small bowel cancer risk in LS as **0.4–12% overall**, and provides gene-stratified cumulative incidence estimates by age 75 (notably **higher for MLH1 and MSH2**) (borsotti2025hereditarycolorectalcancer pages 12-14).
- **Familial adenomatous polyposis (FAP)** is caused by germline pathogenic variants in **APC**; the syndrome features near-universal colorectal cancer risk and is also a basis for duodenal/small bowel surveillance via Spigelman staging (macfarland2024pediatriccancerscreening pages 4-4, borsotti2025hereditarycolorectalcancer pages 12-14).
- **Peutz–Jeghers syndrome (PJS)** is a hereditary GI polyposis/cancer syndrome; pediatric guidance highlights early onset of GI manifestations and recommends small bowel imaging surveillance beginning in childhood (macfarland2024pediatriccancerscreening pages 5-6).
- **Constitutional mismatch repair deficiency (CMMRD)** (biallelic MMR defects; autosomal recessive) is associated with **10–16% small bowel cancer prevalence** in a cited review and requires intensive early surveillance (borsotti2025hereditarycolorectalcancer pages 19-21).
- **MUTYH-associated polyposis (MAP)** warrants proximal small bowel/duodenal surveillance because duodenal cancer risk is described as comparable to FAP (borsotti2025hereditarycolorectalcancer pages 19-21).

#### 2.2.2 Environmental/lifestyle risk factors
- Not specifically extractable for SBC from the retrieved evidence in this run (gap). The sources obtained focused on hereditary syndromes, diagnostic workup, and histology-specific therapeutics.

### 2.3 Protective factors
- Not specifically extractable for SBC from the retrieved evidence in this run (gap).

### 2.4 Gene–environment interactions
- Not specifically extractable for SBC from the retrieved evidence in this run (gap).

---

## 3. Phenotypes (clinical presentation)

### 3.1 Common clinical presentations
A major diagnostic guideline (ESGE small-bowel capsule endoscopy / device-assisted enteroscopy) highlights that small-bowel tumors are **most often detected during evaluation of “obscure small-bowel bleeding” or “unexplained iron-deficiency anemia”**, while also noting that tumors account for only **~3.5–5%** of such presentations—making these symptoms weak predictors on their own (pennazio2023smallbowelcapsuleendoscopy pages 21-21). 

Additional “increased risk” contexts for underlying small-bowel tumors in that guideline include liver metastases from occult neuroendocrine tumors, advanced melanoma (stage IV), stage III melanoma with positive FOBT, and nonresponsive/complicated celiac disease (pennazio2023smallbowelcapsuleendoscopy pages 21-21).

### 3.2 Phenotype ontology (HPO) suggestions (not exhaustive)
Based on the documented presentations (bleeding/IDA) and typical small-bowel tumor consequences, useful HPO mappings include:
- **Iron deficiency anemia** (HP:0001891)
- **Gastrointestinal hemorrhage / intestinal bleeding** (e.g., HP:0002239)
- **Occult gastrointestinal bleeding** (no single canonical HPO term; may map to GI hemorrhage + laboratory evidence)

Evidence for bleeding/IDA as key presentations is supported by guideline text (pennazio2023smallbowelcapsuleendoscopy pages 21-21).

### 3.3 Quality of life impact
- Not directly quantified in the retrieved SBC-focused evidence; however, chronic bleeding/IDA implies fatigue, reduced functional capacity, and healthcare utilization (inference; not directly cited).

---

## 4. Genetic / Molecular Information

### 4.1 Causal genes (germline predisposition)
High-confidence germline predisposition genes for SBC include:
- **MLH1, MSH2, MSH6, PMS2, EPCAM** (Lynch syndrome) (borsotti2025hereditarycolorectalcancer pages 12-14)
- **APC** (FAP) (macfarland2024pediatriccancerscreening pages 4-4)
- **MUTYH** (MAP) (borsotti2025hereditarycolorectalcancer pages 19-21)

### 4.2 Key somatic drivers and biomarkers by subtype
#### 4.2.1 GIST (small intestine stromal tumor)
- GISTs are typically driven by **KIT or PDGFRA gain-of-function mutations** (serrano20232023geisguidelines pages 1-1).
- A guideline summary indicates **>95% of GISTs express KIT (CD117)** by immunohistochemistry; additional markers include CD34, actin, S-100, and desmin (serrano20232023geisguidelines pages 1-3).
- Molecular classes include **KIT/PDGFRA-mutant vs wild-type**, with WT subdivided into **SDH-deficient vs SDH-competent** (serrano20232023geisguidelines pages 1-3).

#### 4.2.2 Small intestinal neuroendocrine tumor (SiNET)
- SiNETs are commonly **somatostatin receptor (SSTR)–positive**, especially SSTR2 and SSTR5; a 2024 review notes that “most well-differentiated NETs express high levels of somatostatin receptors, particularly subtypes 2 and 5” (strosberg2024sequencingofsomatostatinreceptor–based pages 1-2). A separate review notes **>70% of NET tumor cells overexpress SSTR types 2 and 5** (tan2024gastroenteropancreaticneuroendocrineneoplasms pages 8-9).

#### 4.2.3 Small bowel adenocarcinoma (SBA)
- SBA-specific somatic alteration frequencies were not retrieved in the accessible evidence for this run (gap). The registry-based SBA prognostic model indicates survival is often hampered by late diagnosis but does not detail genomic drivers (borsotti2025hereditarycolorectalcancer pages 1-2).

---

## 5. Mechanism / Pathophysiology

### 5.1 Mechanistic causal chains (subtype-oriented)
- **GIST**: activating **KIT/PDGFRA** signaling drives oncogenesis; downstream effects include sustained proliferation and survival consistent with receptor tyrosine kinase activation pathways (serrano20232023geisguidelines pages 1-1).
- **SiNET**: expression of **SSTR2/SSTR5** provides a mechanistic basis for symptom control (hormone secretion) and tumor growth control with somatostatin analogs, and for targeted radionuclide delivery via PRRT (tan2024gastroenteropancreaticneuroendocrineneoplasms pages 8-9, strosberg2024sequencingofsomatostatinreceptor–based pages 1-2).

### 5.2 Ontology suggestions
#### GO biological process (examples)
- **Receptor tyrosine kinase signaling pathway** (GO:0007169) (GIST driver context) (serrano20232023geisguidelines pages 1-1)
- **Cell proliferation** (GO:0008283)
- **Neuropeptide hormone signaling pathway** (GO:0007218) (NET functional biology; mechanistic mapping supported indirectly via SSTR emphasis) (strosberg2024sequencingofsomatostatinreceptor–based pages 1-2)

#### CL cell types (examples)
- **Interstitial cell of Cajal** (GIST cell-of-origin concept; not directly cited in retrieved evidence—flag as gap)
- **Enteroendocrine cell / neuroendocrine cell** (SiNET; not directly cited in retrieved evidence—flag as gap)

---

## 6. Epidemiology (recent statistics)

### 6.1 Overall frequency
SBC is described as accounting for **~2.3% of all digestive cancers** in the general population (borsotti2025hereditarycolorectalcancer pages 1-2).

### 6.2 Neuroendocrine neoplasms of the small intestine (US SEER)
A 2025 SEER-based analysis reports a small intestine NET incidence of approximately **1.2 per 100,000**, with mean age at diagnosis **~64 years** and long median survival compared with many other metastatic cancers (dasari2025epidemiologyofneuroendocrine pages 5-7). The broader SEER-based analysis reports small intestine NET incidence **~1.41 per 100,000**, and provides additional prevalence context for NETs overall (dasari2025epidemiologyofneuroendocrine pages 4-5).

### 6.3 Small intestine GIST (US SEER)
A 2024 SEER-based cohort study reports that incidence rates for small intestine GIST increased **2.7% annually** (2000–2019), with the increase mainly in **localized-stage** tumors (alvarez2024incidenceandsurvival pages 1-2).

### 6.4 Survival (selected recent estimates)
- Small intestine NETs: localized disease median OS reported as **15.3 years**, distant-stage median OS **8.2 years** in one SEER-based analysis (dasari2025epidemiologyofneuroendocrine pages 5-7). Another SEER-based summary reports 10-year overall survival of **51.7%** for small bowel NET primary site (dasari2025epidemiologyofneuroendocrine pages 1-2).

---

## 7. Diagnostics

A key ESGE guideline update (published 2023; “Update 2022”) provides an evidence-based framework for small-bowel tumor evaluation:
- **SBCE is recommended as an initial diagnostic tool in suspected small-bowel tumors** in the absence of stenosis or prior resection (pennazio2023smallbowelcapsuleendoscopy pages 8-9).
- If **imaging already demonstrates tumor suspicion**, ESGE recommends **device-assisted enteroscopy (DAE) over capsule endoscopy** (pennazio2023smallbowelcapsuleendoscopy pages 8-9).
- **Biopsy sampling via DAE** is required to resolve uncertain capsule endoscopy diagnoses (pennazio2023smallbowelcapsuleendoscopy pages 8-9).
- For subepithelial masses, confirmation should be obtained using DAE and/or cross-sectional imaging, and cross-sectional imaging is recommended for **staging and operability** when diagnostic certainty is high (pennazio2023smallbowelcapsuleendoscopy pages 8-9).

| Modality | When to use | Typical presentations prompting workup | Advantages | Limitations / risks | Key guideline or review points | Citations |
|---|---|---|---|---|---|---|
| Small-bowel capsule endoscopy (SBCE/CE) | First-line luminal evaluation when a small-bowel tumor is suspected and there is no evidence of stenosis or prior resection; also recommended in patients at increased risk of small-bowel tumors; preferred first-line method for hereditary-syndrome surveillance programs | Obscure small-bowel bleeding, unexplained iron-deficiency anemia, suspected small-bowel tumor, surveillance in hereditary syndromes such as PJS/FAP/selected LS settings | Noninvasive, outpatient, visualizes entire mucosa, high sensitivity, excellent safety profile; reported diagnostic yield up to 91% in hereditary surveillance settings | Cannot biopsy or treat; may miss solitary proximal/protruding lesions; capsule retention about 1-2%; lesion size/location can be imprecise | ESGE recommends SBCE as an initial diagnostic tool in suspected small-bowel tumors without stenosis; not recommended for follow-up of treated tumors due to insufficient data; in hereditary settings it is commonly the primary surveillance test | (pennazio2023smallbowelcapsuleendoscopy pages 8-9, pennazio2023smallbowelcapsuleendoscopy pages 21-21, borsotti2025hereditarycolorectalcancer pages 2-4, pennazio2023smallbowelcapsuleendoscopy pages 4-5, borsotti2025hereditarycolorectalcancer pages 1-2) |
| Device-assisted enteroscopy (DAE; DBE/SBE/spiral) | Use when imaging already suggests tumor, when tissue diagnosis is needed after SBCE, when therapeutic intervention is likely, or to confirm subepithelial lesions | Positive SBCE, suspected mass needing biopsy, high polyp burden/polyps needing resection, obstructive symptoms, hereditary syndrome surveillance with actionable lesions | Direct visualization, biopsy, tattooing, endoscopic therapy/polypectomy, route can be guided by prior SBCE | More invasive, time-consuming, requires sedation/deep sedation, lower complete small-bowel examination rate than SBCE | ESGE prefers DAE over capsule if prior imaging has demonstrated tumor suspicion; biopsy is required for uncertain capsule findings; DBE diagnostic yield improves substantially when preceded by positive SBCE | (pennazio2023smallbowelcapsuleendoscopy pages 8-9, borsotti2025hereditarycolorectalcancer pages 1-2, borsotti2025hereditarycolorectalcancer pages 2-4, borsotti2025hereditarycolorectalcancer pages 4-5, pennazio2023smallbowelcapsuleendoscopy pages 4-5) |
| CT enterography / cross-sectional CT | Complementary test when SBCE may miss protruding lesions or when extraluminal disease, staging, or operability assessment is needed; useful if tumor is suspected on symptoms or endoscopy | Bleeding/IDA with concern for mass, suspected subepithelial lesion, concern for obstruction/stenosis, preoperative staging | Evaluates mural/extramural disease, metastatic spread, operability; complements capsule limitations for masses | Radiation exposure; less sensitive than mucosal endoscopy for subtle superficial lesions; no biopsy | ESGE notes CT enterography can reasonably complement SBCE, particularly when small-bowel tumor is suspected; once diagnostic certainty is high, cross-sectional imaging is recommended for staging and operability assessment | (pennazio2023smallbowelcapsuleendoscopy pages 8-9, pennazio2023smallbowelcapsuleendoscopy pages 4-5) |
| MR enterography / MRI-based small-bowel imaging | Alternative or adjunct cross-sectional imaging, especially in surveillance programs and when repeated imaging is anticipated; used with CE in PJS and other hereditary settings | Hereditary syndrome surveillance, suspected mass/polyp burden, need to localize lesions or assess bowel beyond mucosa | No ionizing radiation; complements CE for localization and burden assessment | Less direct mucosal detail than endoscopy; no biopsy or endoscopic therapy | Reviews of hereditary SBC surveillance recommend combined approaches using CE with CT/MR enterography; PJS protocols may alternate CE and MRI-enterography every 1-3 years | (borsotti2025hereditarycolorectalcancer pages 2-4, borsotti2025hereditarycolorectalcancer pages 19-21, macfarland2024pediatriccancerscreening pages 5-6) |
| Push enteroscopy / routine upper endoscopy-colonoscopy extensions | Targeted use for proximal duodenal/jejunal lesions, especially in FAP/LS where proximal lesions may be reachable by standard upper endoscopy or push techniques | Duodenal polyposis, proximal small-bowel lesions, hereditary syndromes with duodenal risk | Allows direct inspection/biopsy of reachable proximal lesions; integrates with routine surveillance | Limited reach beyond proximal small bowel | In FAP, push enteroscopy is recommended for advanced Spigelman stage disease; in LS, duodenal/distal ileal lesions may be accessible with routine gastroscopy/colonoscopy, so routine jejunoileal screening is generally not recommended except selected high-risk groups | (borsotti2025hereditarycolorectalcancer pages 12-14) |
| Multimodal workup pathway | Best when suspicion remains despite a single negative test or when hereditary risk is present | Persistent obscure bleeding/IDA, positive occult blood with high-risk cancer history, nonresponsive/complicated celiac disease, hereditary syndrome surveillance | Improves detection, localization, histologic confirmation, and treatment planning | Requires coordination and resource availability | Reviews emphasize combining endoscopy, cross-sectional imaging, and genetic risk stratification in tertiary centers; AI-assisted CE/enterography may improve workflow in the future | (borsotti2025hereditarycolorectalcancer pages 22-24, borsotti2025hereditarycolorectalcancer pages 1-2, pennazio2023smallbowelcapsuleendoscopy pages 21-21) |


*Table: This table summarizes the main diagnostic modalities used for suspected small-bowel tumors, including when each test is typically used, its strengths and limitations, and recent guideline-based recommendations. It is useful for comparing first-line luminal evaluation with confirmatory, therapeutic, and staging approaches.*

---

## 8. Treatment (current applications and real-world implementations)

### 8.1 Surgery
- For **SiNET**, small intestine resection with lymph node removal is recommended; ESMO guidance supports surgery even for locally advanced disease because of risks such as obstruction/ischemia from mesenteric masses (tan2024gastroenteropancreaticneuroendocrineneoplasms pages 8-9).

### 8.2 Somatostatin analogs (SSAs) and PRRT for SiNET
- SSAs (octreotide LAR, lanreotide) are described as **first-line** for SSTR-positive, well-differentiated metastatic gastroenteropancreatic NETs, with low toxicity and tumor growth control (strosberg2024sequencingofsomatostatinreceptor–based pages 4-5).
- **PRRT (e.g., 177Lu-DOTATATE)** is a core real-world theranostic modality for progressive midgut NETs and improves progression-free survival in this population, with ongoing work on sequencing vs other systemic therapies (strosberg2024sequencingofsomatostatinreceptor–based pages 1-2).

### 8.3 Targeted therapy for GIST (approved agents and mutation-informed selection)
The 2023 GEIS guideline states that five TKIs have regulatory approval for metastatic GIST: **imatinib, sunitinib, regorafenib, ripretinib, avapritinib** (serrano20232023geisguidelines pages 1-3). Molecular-genotype–response relationships include:
- KIT exon 11 mutants: **72% objective response** with imatinib; exon 9 mutants: **38% response**, with higher-dose imatinib benefiting exon 9 disease (serrano20232023geisguidelines pages 10-11).
- PDGFRA D842V: resistant to imatinib and most standard therapies (serrano20232023geisguidelines pages 10-11).

These therapies are widely implemented in modern sarcoma/GIST practice and represent one of oncology’s canonical successes of biomarker-driven treatment (serrano20232023geisguidelines pages 1-1).

### MAXO (Medical Action Ontology) suggestions (examples)
- **Surgical resection** (MAXO:0000001; placeholder—exact MAXO ID not retrieved)
- **Endoscopic biopsy** / **endoscopic polypectomy**
- **Somatostatin analog therapy**
- **Peptide receptor radionuclide therapy**
- **Tyrosine kinase inhibitor therapy**

---

## 9. Prevention

### 9.1 High-risk surveillance as secondary prevention
The most evidence-supported “prevention” approach for SBC in current retrieved sources is **surveillance in hereditary syndromes**, using CE, enteroscopy, and cross-sectional imaging with gene-informed stratification (borsotti2025hereditarycolorectalcancer pages 1-2, borsotti2025hereditarycolorectalcancer pages 12-14, macfarland2024pediatriccancerscreening pages 5-6).

| Syndrome | Causal genes / inheritance | Small bowel cancer risk estimates | Suggested surveillance approach | Key citations |
|---|---|---|---|---|
| Lynch syndrome (LS/HNPCC) | Pathogenic variants in **MLH1, MSH2, MSH6, PMS2** or **EPCAM** deletion; **autosomal dominant** | Lifetime small bowel cancer risk reported at **0.4%–12%** overall; cumulative incidence by age 75 reported as **64.7% for MLH1**, **20.1% for MSH2**, **0% for MSH6/PMS2** in the cited review cohort; **~50%** of LS-associated small bowel cancers arise in the **duodenum** (borsotti2025hereditarycolorectalcancer pages 12-14) | Routine **jejunal/ileal screening is generally not recommended**; duodenal/distal ileal lesions may be accessible during routine gastroscopy/colonoscopy; consider more tailored surveillance in **MLH1** carriers; capsule endoscopy has low complication rates (**0%–0.5%**) and reported diagnostic yield up to **8.6%** for asymptomatic small-bowel neoplasms (borsotti2025hereditarycolorectalcancer pages 12-14, borsotti2025hereditarycolorectalcancer pages 1-2) | (borsotti2025hereditarycolorectalcancer pages 1-2, borsotti2025hereditarycolorectalcancer pages 12-14) |
| Familial adenomatous polyposis (FAP) | **APC** pathogenic variants; **autosomal dominant**; de novo cases occur (macfarland2024pediatriccancerscreening pages 4-4) | Elevated small bowel/duodenal cancer risk; duodenal surveillance risk stratified by **Spigelman classification**; jejunal/ileal polyps less well studied (borsotti2025hereditarycolorectalcancer pages 1-2, borsotti2025hereditarycolorectalcancer pages 12-14) | **Push enteroscopy** recommended for **Spigelman III–IV** disease; **double-balloon enteroscopy (DAE)** for high polyp burden; surveillance at **3–6 month intervals** for high-burden disease or **12-month intervals** for minimal disease; multimodal care in tertiary centers emphasized (borsotti2025hereditarycolorectalcancer pages 12-14, borsotti2025hereditarycolorectalcancer pages 1-2) | (borsotti2025hereditarycolorectalcancer pages 1-2, borsotti2025hereditarycolorectalcancer pages 12-14, macfarland2024pediatriccancerscreening pages 4-4) |
| Peutz-Jeghers syndrome (PJS) | **STK11/LKB1** pathogenic variants; typically **autosomal dominant** (syndrome context from screening guidance) | High small bowel polyp/cancer risk; pediatric complication burden notable, with **intussusception >20% by age 10** and **>50% by age 20** (macfarland2024pediatriccancerscreening pages 5-6) | Start GI screening at **age 8 years** with endoscopy/colonoscopy plus small bowel imaging (**video capsule endoscopy or MR enterography**); if polyps are found, repeat every **2–3 years**; some protocols alternate **CE and MRI-E every 1–3 years**; significant polyps **≥15 mm** should undergo **enteroscopy-assisted resection** (borsotti2025hereditarycolorectalcancer pages 19-21, macfarland2024pediatriccancerscreening pages 5-6) | (borsotti2025hereditarycolorectalcancer pages 1-2, borsotti2025hereditarycolorectalcancer pages 19-21, macfarland2024pediatriccancerscreening pages 5-6) |
| Constitutional mismatch repair deficiency (CMMRD) | **Biallelic** mismatch repair gene pathogenic variants; **autosomal recessive** (borsotti2025hereditarycolorectalcancer pages 19-21) | Small bowel cancer prevalence reported at **10%–16%**; median diagnosis age around **28 years** (borsotti2025hereditarycolorectalcancer pages 19-21) | Surveillance includes **annual upper endoscopy** from **age 8** and **capsule endoscopy** from **age 10**; concurrent **push enteroscopy** is recommended because lesions are often duodenal (borsotti2025hereditarycolorectalcancer pages 19-21) | (borsotti2025hereditarycolorectalcancer pages 19-21) |
| MUTYH-associated polyposis (MAP) | **MUTYH** pathogenic variants; usually **autosomal recessive** (syndrome context reflected in guideline-style review) | Duodenal cancer risk described as **comparable to FAP**; risk focus is mainly **proximal small bowel/duodenum** (borsotti2025hereditarycolorectalcancer pages 19-21) | Surveillance limited to **proximal small bowel**; **upper endoscopy with duodenoscopy** starting at **age 25–30 years** in American guidance or **35 years** in European guidance; **polypectomy regardless of size** is recommended because Spigelman staging is less reliable in MAP (borsotti2025hereditarycolorectalcancer pages 19-21) | (borsotti2025hereditarycolorectalcancer pages 19-21) |


*Table: This table summarizes the major hereditary syndromes linked to small bowel cancer, highlighting causal genes, reported risk estimates, and syndrome-specific surveillance/prevention approaches. It is useful for quickly comparing how surveillance differs across Lynch syndrome, FAP, Peutz-Jeghers syndrome, CMMRD, and MAP.*

---

## 10. Other Species / Natural Disease
Not retrieved for small intestine cancer specifically in this run (gap).

---

## 11. Model Organisms
Not retrieved for small intestine cancer specifically in this run (gap).

---

## 12. Recent developments and latest research (emphasis 2023–2024)

Key 2023–2024 developments captured in the retrieved evidence include:
1. **Endoscopic technology integration**: ESGE guidance formalizes pathways that integrate capsule endoscopy, device-assisted enteroscopy, and cross-sectional imaging for suspected small-bowel tumors, clarifying when DAE should supersede capsule endoscopy when a tumor is already suspected on imaging (pennazio2023smallbowelcapsuleendoscopy pages 8-9).
2. **Syndrome-based surveillance modernization**: 2024 AACR Childhood Cancer Predisposition Working Group updates support early initiation of small bowel imaging (capsule endoscopy or MR enterography) in pediatric PJS beginning at age 8, reflecting increasing emphasis on life-course surveillance (macfarland2024pediatriccancerscreening pages 5-6).
3. **Registry-based epidemiology of rare GI malignancies**: 2024–2025 SEER-based analyses provide updated incidence trends and long-horizon survival estimates for small intestine NETs and small intestine GIST, highlighting increasing detection and improving survivorship in some subtypes (dasari2025epidemiologyofneuroendocrine pages 5-7, alvarez2024incidenceandsurvival pages 1-2).
4. **Precision therapeutics maturity in rare tumors**: 2023 GIST guideline synthesis reiterates that KIT/PDGFRA genotype dictates therapeutic selection and outcome, with multiple approved TKIs and genotype-specific resistance patterns informing sequencing (serrano20232023geisguidelines pages 10-11, serrano20232023geisguidelines pages 1-3).

---

## 13. Expert opinion and analysis (authoritative sources)

- **ESGE guideline perspective (2023 Endoscopy)**: emphasizes that small-bowel tumors are rare and often discovered in workups for bleeding/IDA, and that diagnostic certainty should drive escalation from capsule endoscopy to device-assisted enteroscopy and staging imaging (pennazio2023smallbowelcapsuleendoscopy pages 8-9, pennazio2023smallbowelcapsuleendoscopy pages 21-21).
- **GEIS guideline perspective (2023 Therapeutic Advances in Medical Oncology)**: positions GIST as a paradigmatic success of molecularly targeted therapy, explicitly noting that KIT/PDGFRA mutations underpin disease initiation/evolution and that multiple TKIs have transformed outcomes (serrano20232023geisguidelines pages 1-1).
- **Nuclear medicine/NET therapy perspective (2024 Journal of Nuclear Medicine)**: stresses SSTR expression as the biological basis for first-line SSA use and PRRT, while noting that randomized head-to-head sequencing evidence remains limited (strosberg2024sequencingofsomatostatinreceptor–based pages 4-5, strosberg2024sequencingofsomatostatinreceptor–based pages 1-2).

---

## Limitations of this report (evidence gaps)
1. **Ontology identifiers** (MONDO, MeSH, Orphanet, ICD) were **not obtainable** from the retrieved full texts in this tool run.
2. **Small bowel adenocarcinoma (SBA) molecular landscape** (somatic driver frequencies, MSI status rates, actionable alterations) was **not captured** in the accessible evidence.
3. **Environmental/lifestyle risk factors**, protective factors, animal models, and disease-specific QoL statistics were **not retrieved** from the current evidence set.
4. **Image extraction** via the available tooling failed for multiple candidate documents; therefore no figure/table image citations are provided.

---

## Summary tables

| Entity | Definition/notes | Approx share or incidence (if in evidence) | Typical location | Key citations |
|---|---|---|---|---|
| SBC umbrella | Small bowel cancer is a rare malignancy of the small intestine comprising four main histologic groups: adenocarcinomas, neuroendocrine tumors, stromal tumors, and lymphomas. Reviews note adenocarcinoma and neuroendocrine tumor are the two most common categories. | Accounts for ~2.3% of digestive cancers; adenocarcinoma and neuroendocrine tumors each represent ~40% of SBC; duodenum is most commonly involved (55–82%), followed by jejunum (11–25%) and ileum (7–17%). | Duodenum most common overall; then jejunum and ileum. | (borsotti2025hereditarycolorectalcancer pages 1-2) |
| SBA | Small bowel adenocarcinoma is the epithelial adenocarcinoma subtype of SBC; prognosis is often limited by late diagnosis and management complexity. In hereditary settings, it can arise through an adenoma-carcinoma sequence, especially in Lynch syndrome. | Included within the ~40% adenocarcinoma share of SBC; SEER-based prognostic study analyzed 2,064 SBA cases diagnosed 2010–2020. | Often duodenal overall; in Lynch syndrome, nearly 50% of small bowel cancers occur in the duodenum. | (borsotti2025hereditarycolorectalcancer pages 1-2, borsotti2025hereditarycolorectalcancer pages 12-14) |
| SiNET | Small intestinal neuroendocrine tumor (midgut/small-bowel NET) is a well-differentiated neuroendocrine neoplasm of the small intestine; commonly SSTR-positive and often slow-growing but prone to mesenteric nodal/liver spread. | Small intestine NET incidence ~1.2–1.41 per 100,000 persons in recent US SEER analyses; small bowel NETs are among the most common GEP-NET sites; 10-year overall survival reported at 51.7% in one SEER-based analysis. | Frequently ileal/midgut; ileal/ileocecal primaries are emphasized in treatment reviews. | (dasari2025epidemiologyofneuroendocrine pages 5-7, dasari2025epidemiologyofneuroendocrine pages 1-2, dasari2025epidemiologyofneuroendocrine pages 4-5, strosberg2024sequencingofsomatostatinreceptor–based pages 1-2) |
| Small intestine GIST | Gastrointestinal stromal tumor is the principal mesenchymal/stromal tumor category of the small intestine, usually driven by KIT or PDGFRA alterations and characterized by KIT (CD117) expression in >95% of cases. | Small intestine is the primary site in ~31% of GISTs; global GIST incidence ~10–15 per million people; small intestine GIST incidence increased by 2.7% annually in SEER 2000–2019. | Small intestine is a major primary site after stomach; may present as multifocal disease in NF1-associated cases. | (serrano20232023geisguidelines pages 1-3, alvarez2024incidenceandsurvival pages 1-2, wang2026targetedtherapyfor pages 1-2) |


*Table: This table summarizes the disease scope of small intestine cancer, highlighting the umbrella category and the major clinically important histologic subtypes. It is useful for orienting a knowledge base entry to the main entities, their approximate frequencies or incidence, and their usual anatomic distribution.*

References

1. (borsotti2025hereditarycolorectalcancer pages 1-2): Edoardo Borsotti, Francesca Laura Nava, Felice Benedicenti, Laura Cini, Andrea Magarotto, Davide Ferrari, Paolo Cantù, Marco Vitellaro, Emanuele Rausa, and Federica Cavalcoli. Hereditary colorectal cancer syndromes: small bowel cancer risk and endoscopic surveillance strategies. Diagnostics, 15:819, Mar 2025. URL: https://doi.org/10.3390/diagnostics15070819, doi:10.3390/diagnostics15070819. This article has 5 citations.

2. (borsotti2025hereditarycolorectalcancer pages 12-14): Edoardo Borsotti, Francesca Laura Nava, Felice Benedicenti, Laura Cini, Andrea Magarotto, Davide Ferrari, Paolo Cantù, Marco Vitellaro, Emanuele Rausa, and Federica Cavalcoli. Hereditary colorectal cancer syndromes: small bowel cancer risk and endoscopic surveillance strategies. Diagnostics, 15:819, Mar 2025. URL: https://doi.org/10.3390/diagnostics15070819, doi:10.3390/diagnostics15070819. This article has 5 citations.

3. (pennazio2023smallbowelcapsuleendoscopy pages 8-9): Marco Pennazio, Emanuele Rondonotti, Edward J. Despott, Xavier Dray, Martin Keuchel, Tom Moreels, David S. Sanders, Cristiano Spada, Cristina Carretero, Pablo Cortegoso Valdivia, Luca Elli, Lorenzo Fuccio, Begona Gonzalez Suarez, Anastasios Koulaouzidis, Lumir Kunovsky, Deirdre McNamara, Helmut Neumann, Enrique Perez-Cuadrado-Martinez, Enrique Perez-Cuadrado-Robles, Stefania Piccirelli, Bruno Rosa, Jean-Christophe Saurin, Reena Sidhu, Ilja Tacheci, Erasmia Vlachou, and Konstantinos Triantafyllou. Small-bowel capsule endoscopy and device-assisted enteroscopy for diagnosis and treatment of small-bowel disorders: european society of gastrointestinal endoscopy (esge) guideline – update 2022. Endoscopy, 55:58-95, Nov 2023. URL: https://doi.org/10.1055/a-1973-3796, doi:10.1055/a-1973-3796. This article has 391 citations and is from a domain leading peer-reviewed journal.

4. (pennazio2023smallbowelcapsuleendoscopy pages 21-21): Marco Pennazio, Emanuele Rondonotti, Edward J. Despott, Xavier Dray, Martin Keuchel, Tom Moreels, David S. Sanders, Cristiano Spada, Cristina Carretero, Pablo Cortegoso Valdivia, Luca Elli, Lorenzo Fuccio, Begona Gonzalez Suarez, Anastasios Koulaouzidis, Lumir Kunovsky, Deirdre McNamara, Helmut Neumann, Enrique Perez-Cuadrado-Martinez, Enrique Perez-Cuadrado-Robles, Stefania Piccirelli, Bruno Rosa, Jean-Christophe Saurin, Reena Sidhu, Ilja Tacheci, Erasmia Vlachou, and Konstantinos Triantafyllou. Small-bowel capsule endoscopy and device-assisted enteroscopy for diagnosis and treatment of small-bowel disorders: european society of gastrointestinal endoscopy (esge) guideline – update 2022. Endoscopy, 55:58-95, Nov 2023. URL: https://doi.org/10.1055/a-1973-3796, doi:10.1055/a-1973-3796. This article has 391 citations and is from a domain leading peer-reviewed journal.

5. (strosberg2024sequencingofsomatostatinreceptor–based pages 1-2): Jonathan R. Strosberg, Taymeyah Al-Toubah, Ghassan El-Haddad, Diane Reidy Lagunes, and Lisa Bodei. Sequencing of somatostatin-receptor–based therapies in neuroendocrine tumor patients. The Journal of Nuclear Medicine, 65:340-348, Jan 2024. URL: https://doi.org/10.2967/jnumed.123.265706, doi:10.2967/jnumed.123.265706. This article has 27 citations.

6. (serrano20232023geisguidelines pages 1-3): César Serrano, Javier Martín-Broto, José Manuel Asencio-Pascual, José Antonio López-Guerrero, Jordi Rubió-Casadevall, Silvia Bagué, Xavier García-del-Muro, Juan Ángel Fernández-Hernández, Luís Herrero, Antonio López-Pousa, Andrés Poveda, and Virginia Martínez-Marín. 2023 geis guidelines for gastrointestinal stromal tumors. Therapeutic Advances in Medical Oncology, Jan 2023. URL: https://doi.org/10.1177/17588359231192388, doi:10.1177/17588359231192388. This article has 156 citations and is from a peer-reviewed journal.

7. (dasari2025epidemiologyofneuroendocrine pages 5-7): Arvind Dasari, Katrine Wallace, Daniel M. Halperin, Jessica Maxwell, Pamela Kunz, Simron Singh, Beth Chasen, and James C. Yao. Epidemiology of neuroendocrine neoplasms in the us. JAMA Network Open, 8:e2515798, Jun 2025. URL: https://doi.org/10.1001/jamanetworkopen.2025.15798, doi:10.1001/jamanetworkopen.2025.15798. This article has 98 citations and is from a peer-reviewed journal.

8. (alvarez2024incidenceandsurvival pages 1-2): Christian S. Alvarez, M. Blanca Piazuelo, Tania Fleitas-Kanonnikoff, Jennifer Ruhl, J. Alejandro Pérez-Fidalgo, and M. Constanza Camargo. Incidence and survival outcomes of gastrointestinal stromal tumors. Aug 2024. URL: https://doi.org/10.1001/jamanetworkopen.2024.28828, doi:10.1001/jamanetworkopen.2024.28828. This article has 54 citations and is from a peer-reviewed journal.

9. (macfarland2024pediatriccancerscreening pages 5-6): Suzanne P. MacFarland, Kerri Becktell, Kami Wolfe Schneider, Roland P. Kuiper, Harry Lesmana, Julia Meade, Kim E. Nichols, Christopher C. Porter, Sharon A. Savage, Kris Ann Schultz, Hamish Scott, Lisa States, Uri Tabori, Chieko Tamura, Gail Tomlinson, Kristin Zelley, Carol Durno, Andrew Bauer, and Sharon E. Plon. Pediatric cancer screening in hereditary gastrointestinal cancer risk syndromes: an update from the aacr childhood cancer predisposition working group. Clinical cancer research : an official journal of the American Association for Cancer Research, 30:4566-4571, Aug 2024. URL: https://doi.org/10.1158/1078-0432.ccr-24-0953, doi:10.1158/1078-0432.ccr-24-0953. This article has 25 citations.

10. (serrano20232023geisguidelines pages 1-1): César Serrano, Javier Martín-Broto, José Manuel Asencio-Pascual, José Antonio López-Guerrero, Jordi Rubió-Casadevall, Silvia Bagué, Xavier García-del-Muro, Juan Ángel Fernández-Hernández, Luís Herrero, Antonio López-Pousa, Andrés Poveda, and Virginia Martínez-Marín. 2023 geis guidelines for gastrointestinal stromal tumors. Therapeutic Advances in Medical Oncology, Jan 2023. URL: https://doi.org/10.1177/17588359231192388, doi:10.1177/17588359231192388. This article has 156 citations and is from a peer-reviewed journal.

11. (macfarland2024pediatriccancerscreening pages 4-4): Suzanne P. MacFarland, Kerri Becktell, Kami Wolfe Schneider, Roland P. Kuiper, Harry Lesmana, Julia Meade, Kim E. Nichols, Christopher C. Porter, Sharon A. Savage, Kris Ann Schultz, Hamish Scott, Lisa States, Uri Tabori, Chieko Tamura, Gail Tomlinson, Kristin Zelley, Carol Durno, Andrew Bauer, and Sharon E. Plon. Pediatric cancer screening in hereditary gastrointestinal cancer risk syndromes: an update from the aacr childhood cancer predisposition working group. Clinical cancer research : an official journal of the American Association for Cancer Research, 30:4566-4571, Aug 2024. URL: https://doi.org/10.1158/1078-0432.ccr-24-0953, doi:10.1158/1078-0432.ccr-24-0953. This article has 25 citations.

12. (borsotti2025hereditarycolorectalcancer pages 19-21): Edoardo Borsotti, Francesca Laura Nava, Felice Benedicenti, Laura Cini, Andrea Magarotto, Davide Ferrari, Paolo Cantù, Marco Vitellaro, Emanuele Rausa, and Federica Cavalcoli. Hereditary colorectal cancer syndromes: small bowel cancer risk and endoscopic surveillance strategies. Diagnostics, 15:819, Mar 2025. URL: https://doi.org/10.3390/diagnostics15070819, doi:10.3390/diagnostics15070819. This article has 5 citations.

13. (tan2024gastroenteropancreaticneuroendocrineneoplasms pages 8-9): Baizhou Tan, Beiyu Zhang, and Hongping Chen. Gastroenteropancreatic neuroendocrine neoplasms: epidemiology, genetics, and treatment. Frontiers in Endocrinology, Sep 2024. URL: https://doi.org/10.3389/fendo.2024.1424839, doi:10.3389/fendo.2024.1424839. This article has 32 citations.

14. (dasari2025epidemiologyofneuroendocrine pages 4-5): Arvind Dasari, Katrine Wallace, Daniel M. Halperin, Jessica Maxwell, Pamela Kunz, Simron Singh, Beth Chasen, and James C. Yao. Epidemiology of neuroendocrine neoplasms in the us. JAMA Network Open, 8:e2515798, Jun 2025. URL: https://doi.org/10.1001/jamanetworkopen.2025.15798, doi:10.1001/jamanetworkopen.2025.15798. This article has 98 citations and is from a peer-reviewed journal.

15. (dasari2025epidemiologyofneuroendocrine pages 1-2): Arvind Dasari, Katrine Wallace, Daniel M. Halperin, Jessica Maxwell, Pamela Kunz, Simron Singh, Beth Chasen, and James C. Yao. Epidemiology of neuroendocrine neoplasms in the us. JAMA Network Open, 8:e2515798, Jun 2025. URL: https://doi.org/10.1001/jamanetworkopen.2025.15798, doi:10.1001/jamanetworkopen.2025.15798. This article has 98 citations and is from a peer-reviewed journal.

16. (borsotti2025hereditarycolorectalcancer pages 2-4): Edoardo Borsotti, Francesca Laura Nava, Felice Benedicenti, Laura Cini, Andrea Magarotto, Davide Ferrari, Paolo Cantù, Marco Vitellaro, Emanuele Rausa, and Federica Cavalcoli. Hereditary colorectal cancer syndromes: small bowel cancer risk and endoscopic surveillance strategies. Diagnostics, 15:819, Mar 2025. URL: https://doi.org/10.3390/diagnostics15070819, doi:10.3390/diagnostics15070819. This article has 5 citations.

17. (pennazio2023smallbowelcapsuleendoscopy pages 4-5): Marco Pennazio, Emanuele Rondonotti, Edward J. Despott, Xavier Dray, Martin Keuchel, Tom Moreels, David S. Sanders, Cristiano Spada, Cristina Carretero, Pablo Cortegoso Valdivia, Luca Elli, Lorenzo Fuccio, Begona Gonzalez Suarez, Anastasios Koulaouzidis, Lumir Kunovsky, Deirdre McNamara, Helmut Neumann, Enrique Perez-Cuadrado-Martinez, Enrique Perez-Cuadrado-Robles, Stefania Piccirelli, Bruno Rosa, Jean-Christophe Saurin, Reena Sidhu, Ilja Tacheci, Erasmia Vlachou, and Konstantinos Triantafyllou. Small-bowel capsule endoscopy and device-assisted enteroscopy for diagnosis and treatment of small-bowel disorders: european society of gastrointestinal endoscopy (esge) guideline – update 2022. Endoscopy, 55:58-95, Nov 2023. URL: https://doi.org/10.1055/a-1973-3796, doi:10.1055/a-1973-3796. This article has 391 citations and is from a domain leading peer-reviewed journal.

18. (borsotti2025hereditarycolorectalcancer pages 4-5): Edoardo Borsotti, Francesca Laura Nava, Felice Benedicenti, Laura Cini, Andrea Magarotto, Davide Ferrari, Paolo Cantù, Marco Vitellaro, Emanuele Rausa, and Federica Cavalcoli. Hereditary colorectal cancer syndromes: small bowel cancer risk and endoscopic surveillance strategies. Diagnostics, 15:819, Mar 2025. URL: https://doi.org/10.3390/diagnostics15070819, doi:10.3390/diagnostics15070819. This article has 5 citations.

19. (borsotti2025hereditarycolorectalcancer pages 22-24): Edoardo Borsotti, Francesca Laura Nava, Felice Benedicenti, Laura Cini, Andrea Magarotto, Davide Ferrari, Paolo Cantù, Marco Vitellaro, Emanuele Rausa, and Federica Cavalcoli. Hereditary colorectal cancer syndromes: small bowel cancer risk and endoscopic surveillance strategies. Diagnostics, 15:819, Mar 2025. URL: https://doi.org/10.3390/diagnostics15070819, doi:10.3390/diagnostics15070819. This article has 5 citations.

20. (strosberg2024sequencingofsomatostatinreceptor–based pages 4-5): Jonathan R. Strosberg, Taymeyah Al-Toubah, Ghassan El-Haddad, Diane Reidy Lagunes, and Lisa Bodei. Sequencing of somatostatin-receptor–based therapies in neuroendocrine tumor patients. The Journal of Nuclear Medicine, 65:340-348, Jan 2024. URL: https://doi.org/10.2967/jnumed.123.265706, doi:10.2967/jnumed.123.265706. This article has 27 citations.

21. (serrano20232023geisguidelines pages 10-11): César Serrano, Javier Martín-Broto, José Manuel Asencio-Pascual, José Antonio López-Guerrero, Jordi Rubió-Casadevall, Silvia Bagué, Xavier García-del-Muro, Juan Ángel Fernández-Hernández, Luís Herrero, Antonio López-Pousa, Andrés Poveda, and Virginia Martínez-Marín. 2023 geis guidelines for gastrointestinal stromal tumors. Therapeutic Advances in Medical Oncology, Jan 2023. URL: https://doi.org/10.1177/17588359231192388, doi:10.1177/17588359231192388. This article has 156 citations and is from a peer-reviewed journal.

22. (wang2026targetedtherapyfor pages 1-2): Xiao-Dong Wang, Chun-Hui Shou, Sheng-Chuan Chen, Yan-Yun Hong, Kan-Kai Zhu, Wei-Li Yang, and Ji-Ren Yu. Targeted therapy for advanced gastrointestinal stromal tumors: evolution and future directions. Drug Design, Development and Therapy, Volume 20:1-23, Mar 2026. URL: https://doi.org/10.2147/dddt.s594043, doi:10.2147/dddt.s594043. This article has 1 citations.

## Artifacts

- [Edison artifact artifact-00](Small_Intestine_Cancer-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](Small_Intestine_Cancer-deep-research-falcon_artifacts/artifact-01.md)
- [Edison artifact artifact-02](Small_Intestine_Cancer-deep-research-falcon_artifacts/artifact-02.md)