---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-07-01T02:37:19.447028'
end_time: '2026-07-01T03:00:53.273477'
duration_seconds: 1413.83
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Human Papillomavirus Infection
  mondo_id: ''
  category: Infectious Disease
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 62
artifact_count: 3
artifact_sources:
  edison_answer_artifacts: 3
artifacts:
- filename: artifact-00.md
  path: Human_Papillomavirus_Infection-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: Human_Papillomavirus_Infection-deep-research-falcon_artifacts/artifact-01.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-01
- filename: artifact-02.md
  path: Human_Papillomavirus_Infection-deep-research-falcon_artifacts/artifact-02.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-02
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Human Papillomavirus Infection
- **MONDO ID:**  (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Human Papillomavirus Infection** covering all of the
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
- **Disease Name:** Human Papillomavirus Infection
- **MONDO ID:**  (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Human Papillomavirus Infection** covering all of the
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


# Comprehensive Research Report: Human Papillomavirus (HPV) Infection

## 1. Disease Information

### Overview
Human papillomavirus (HPV) is a non-enveloped, double-stranded circular DNA virus belonging to the family Papillomaviridae, with a genome of approximately 8 kilobases (jain2023epidemiologymolecularpathogenesis pages 3-5). It is the most common sexually transmitted viral infection globally, with over 400 identified types and more than 200 characterized variants (wu2024unveilingthemultifaceted pages 1-2, mlynarczykbonikowska2024hpvinfections—classificationpathogenesis pages 1-2). HPV causes approximately 5% of all human cancers worldwide and is implicated in virtually all cervical cancers (99.7%), as well as substantial proportions of anal (71–90%), vaginal (65–74%), vulvar (43–74%), penile (43–63%), and oropharyngeal (10–70%) cancers (mlynarczykbonikowska2024hpvinfections—classificationpathogenesis pages 1-2). Over 80% of sexually active individuals will contract HPV by age 45, though approximately 90% of infections resolve spontaneously within two years (baba2025humanpapillomavirus pages 1-2).

### Key Identifiers and Synonyms

The following table summarizes key disease identifiers, classification schemes, and terminology for HPV infection:

| Identifier Type | Value/Code | Description |
|---|---|---|
| MONDO ID | MONDO:0005161 | Human papilloma virus infection; disease ontology identifier used in aggregated disease knowledge resources and Open Targets disease-target associations (OpenTargets Search: human papillomavirus infectious disease,cervical carcinoma) |
| ICD-10 | B97.7 | Papillomavirus as the cause of diseases classified elsewhere; used when HPV is the etiologic infectious agent rather than the primary lesion diagnosis (OpenTargets Search: human papillomavirus infectious disease,cervical carcinoma) |
| ICD-10 | A63.0 | Anogenital (venereal) warts / condylomata acuminata; typically caused by low-risk HPV, especially types 6 and 11 (maghiar2024skinlesionscaused pages 4-6, branda2024humanpapillomavirus(hpv) pages 7-9) |
| ICD-10 | B07 | Viral warts; includes common cutaneous wart presentations caused by cutaneous HPV types (maghiar2024skinlesionscaused pages 4-6, maghiar2024skinlesionscaused pages 2-4) |
| ICD-11 | 1F9 | Viral infections characterized by skin and mucous membrane lesions; parent infectious-disease grouping under which HPV-related wart disorders are classified in ICD-11 usage contexts (maghiar2024skinlesionscaused pages 4-6) |
| ICD-11 | 1F9Y / specific child codes | Other specified viral infections of skin or mucosa may be used depending on lesion site; HPV-associated neoplasia is coded separately by cancer site (e.g., cervix, anus, oropharynx) rather than by HPV alone (branda2024humanpapillomavirus(hpv) pages 7-9, baba2025humanpapillomavirus pages 10-11) |
| MeSH | D030361 | Papillomavirus Infections; MeSH disease heading for indexing biomedical literature on HPV infection and related manifestations (OpenTargets Search: human papillomavirus infectious disease,cervical carcinoma) |
| Common synonyms | HPV infection | Standard clinical shorthand for infection with human papillomavirus; most common contemporary synonym (jain2023epidemiologymolecularpathogenesis pages 2-3, malik2023trackinghpvinfection pages 1-2) |
| Common synonyms | Human papillomavirus infection | Expanded formal disease name used in reviews and public-health literature (wu2024unveilingthemultifaceted pages 1-2, mlynarczykbonikowska2024hpvinfections—classificationpathogenesis pages 1-2) |
| Common synonyms | Papillomavirus infection | Broader synonym used in classification/pathogenesis literature; may require context to distinguish human from animal papillomavirus infection (mlynarczykbonikowska2024hpvinfections—classificationpathogenesis pages 1-2, bette2024cottontailrabbitpapillomavirus pages 1-2) |
| Common synonyms | Condylomata acuminata | Synonym for anogenital warts, a common low-risk HPV manifestation (maghiar2024skinlesionscaused pages 4-6, branda2024humanpapillomavirus(hpv) pages 7-9) |
| HPV risk classification | High-risk (oncogenic) types | High-risk mucosal types include HPV16, 18, 31, 33, 35, 39, 45, 51, 52, 56, 58, 59, 68; these are linked to cervical, anal, penile, vulvar, vaginal, and oropharyngeal cancers. HPV16 and HPV18 account for most cervical cancers (jain2023epidemiologymolecularpathogenesis pages 2-3, pavelescu2025molecularinsightsinto pages 2-4, mlynarczykbonikowska2024hpvinfections—classificationpathogenesis pages 1-2, jain2023epidemiologymolecularpathogenesis pages 3-5) |
| HPV risk classification | Low-risk types | Low-risk types include HPV6 and HPV11, with additional low-risk mucosal types such as 40, 42, 43, 44, 54, 61, 72, 81, 89; these mainly cause benign lesions such as genital warts and respiratory papillomas (wu2024unveilingthemultifaceted pages 1-2, mlynarczykbonikowska2024hpvinfections—classificationpathogenesis pages 1-2, maghiar2024skinlesionscaused pages 4-6) |
| Taxonomic classification | Alpha papillomavirus | Predominantly infects genital and oral mucosa; includes both low-risk and high-risk mucosal HPV types associated with anogenital lesions and many HPV-related cancers (wu2024unveilingthemultifaceted pages 1-2, jain2023epidemiologymolecularpathogenesis pages 3-5) |
| Taxonomic classification | Beta papillomavirus | Primarily cutaneous; commonly found on skin and implicated in some non-melanoma skin cancers, especially in immunocompromised hosts (wu2024unveilingthemultifaceted pages 1-2, bette2024cottontailrabbitpapillomavirus pages 2-3) |
| Taxonomic classification | Gamma papillomavirus | Primarily associated with cutaneous infection and skin tropism (wu2024unveilingthemultifaceted pages 1-2) |
| Taxonomic classification | Mu papillomavirus | Cutaneous genus associated with skin wart phenotypes (wu2024unveilingthemultifaceted pages 1-2) |
| Taxonomic classification | Nu papillomavirus | Cutaneous genus associated with skin wart phenotypes (wu2024unveilingthemultifaceted pages 1-2) |


*Table: This table summarizes key disease identifiers and classification schemes for human papillomavirus infection, including ontology and coding systems, common synonyms, oncogenic risk groupings, and viral genera. It is useful as a compact reference for mapping HPV across clinical coding, biomedical indexing, and biological classification systems.*

**Common Synonyms:** HPV infection, human papillomavirus infection, papillomavirus infection, condylomata acuminata (for anogenital warts), genital warts, venereal warts, verruca vulgaris (common warts).

---

## 2. Etiology

### Disease Causal Factors
HPV infection is caused by infection with human papillomavirus, a DNA virus transmitted primarily through direct contact with infected skin or mucous membranes, most commonly via sexual contact (maghiar2024skinlesionscaused pages 2-4). The virus targets basal epithelial cells and enters through microabrasions or disruptions in the epithelial barrier (jain2023epidemiologymolecularpathogenesis pages 3-5). Non-sexual transmission routes include perinatal transmission and autoinoculation (jain2023epidemiologymolecularpathogenesis pages 3-5).

### Risk Factors

**Environmental and Behavioral Risk Factors:**
- Multiple sexual partners and early onset of sexual activity (peak infection in teens and twenties) (jain2023epidemiologymolecularpathogenesis pages 2-3, pavelescu2025molecularinsightsinto pages 2-4)
- High parity and early pregnancy (pavelescu2025molecularinsightsinto pages 2-4)
- Long-term oral contraceptive use (pavelescu2025molecularinsightsinto pages 2-4)
- Tobacco smoking and tobacco chewing (pavelescu2025molecularinsightsinto pages 2-4)
- Concurrent sexually transmitted infections, particularly HIV (jain2023epidemiologymolecularpathogenesis pages 2-3)
- Immunosuppression (baba2025humanpapillomavirus pages 1-2)
- Male homosexuality (HPV anal infection prevalence ≥90% in homosexual and HIV-infected men) (jain2023epidemiologymolecularpathogenesis pages 2-3)

**Host Genetic Risk Factors:**
Heritability estimates for cervical carcinoma liability range from 27–29% (olokede2026areviewon pages 6-7). Genome-wide association studies (GWAS) have identified HLA class II loci, particularly HLA-DRB1 and HLA-DQB1, as the strongest genetic determinants of HPV persistence and cervical cancer susceptibility (olokede2026areviewon pages 6-7, olokede2026areviewon pages 1-2). Specific risk alleles include HLA-DRB1*15:01, HLA-DQB1*06:02, HLA-DRB1*13:02, HLA-DQB1*05:02, and HLA-DRB1*03:01 (olokede2026areviewon pages 6-7, pavelescu2025molecularinsightsinto pages 11-13). Additional GWAS loci outside the MHC region include GSDMB (pyroptosis regulation), MUC1 (mucosal barrier), DSG2/CDH1 (epithelial adhesion), and TFAP2A (differentiation pathway) (olokede2026areviewon pages 16-17).

### Protective Factors

**Genetic Protective Factors:**
HLA-DRB1*13:01 and HLA-DQB1*06:03 confer protection through superior binding dynamics for conserved E6/E7 epitopes, facilitating robust Th1 immune responses (olokede2026areviewon pages 6-7). HLA-DRB1*15:03 was associated with decreased risk of persistent high-risk HPV (olokede2026areviewon pages 6-7). Notably, DRB1*1302-positive women had significantly lower cumulative progression rates to CIN3 (2.1% vs 14.0%) over 10 years (li2025biomarkersdifferentiatingregression pages 8-9).

**Environmental Protective Factors:**
- HPV vaccination (most effective preventive measure) (wu2024unveilingthemultifaceted pages 9-10)
- Consistent condom use and limiting sexual partners (wu2024unveilingthemultifaceted pages 9-10)
- Male circumcision (uncircumcised men have greater genital mucosa exposure) (baba2025humanpapillomavirus pages 10-11)

### Gene-Environment Interactions
DNA repair capacity variants interact with tobacco smoke mutagens to influence HPV-driven carcinogenesis, and estrogen receptor polymorphisms (ESR1 PvuII and XbaI variants) interact with exogenous steroid hormones to upregulate viral E6/E7 oncogenes (olokede2026areviewon pages 19-21). Progesterone signaling upregulates DNA methyltransferases (DNMT1, DNMT3B) to promote hypermethylation of tumor suppressor genes (olokede2026areviewon pages 19-21). Vaginal dysbiosis and mucosal barrier dynamics represent additional relevant gene-environment interaction factors (olokede2026areviewon pages 19-21).

---

## 3. Phenotypes

### Clinical Manifestations

**Cutaneous Warts:**
- Common warts (verruca vulgaris), plantar warts, flat warts
- Cutaneous warts affect 7–12% of the population, with higher prevalence in children and adolescents (10–20% annual incidence) (maghiar2024skinlesionscaused pages 2-4)
- HPO terms: HP:0200043 (Verrucae), HP:0010283 (Verruca plana)

**Anogenital Warts (Condylomata Acuminata):**
- Caused primarily by HPV types 6 and 11 (branda2024humanpapillomavirus(hpv) pages 7-9)
- Develop several months after infection; often asymptomatic but may cause itching and bleeding (branda2024humanpapillomavirus(hpv) pages 7-9)
- HPO terms: HP:0030799 (Condylomata acuminata)

**Cervical Intraepithelial Neoplasia (CIN):**
- CIN1: reflects transient infection, low-grade squamous intraepithelial lesion (LSIL) (legaki2026hpvdrivencervicalcarcinogenesis pages 1-2)
- CIN2: variable malignant potential, intermediate-grade lesion (legaki2026hpvdrivencervicalcarcinogenesis pages 1-2, li2025biomarkersdifferentiatingregression pages 6-7)
- CIN3: most significant precursor to invasive cervical cancer (legaki2026hpvdrivencervicalcarcinogenesis pages 1-2)
- HPO terms: HP:0032260 (Cervical intraepithelial neoplasia)

**HPV-Associated Cancers:**
- Cervical cancer (virtually all cases HPV-attributable; HPV16 accounts for 55%, HPV18 for 15%) (jain2023epidemiologymolecularpathogenesis pages 3-5)
- Oropharyngeal squamous cell carcinoma (rising rapidly in developed countries) (baba2025humanpapillomavirus pages 1-2)
- Anal cancer (90% HPV-attributable) (mlynarczykbonikowska2024hpvinfections—classificationpathogenesis pages 1-2)
- Penile, vulvar, and vaginal cancers (baba2025humanpapillomavirus pages 1-2)
- HPO terms: HP:0012126 (Cervical squamous cell carcinoma), HP:0100649 (Neoplasm of the oral cavity)

**Quality of Life Impact:**
HPV-associated cancers impose significant morbidity and mortality. In 2020, cervical cancer alone accounted for 604,127 new cases and 341,831 deaths globally, making it the second most common cancer in women aged 15–44 (jain2023epidemiologymolecularpathogenesis pages 2-3).

---

## 4. Genetic/Molecular Information

### Viral Genome Structure
The HPV genome (~8 kb) consists of early genes (E1, E2, E4, E5, E6, E7) and late genes (L1, L2) (jain2023epidemiologymolecularpathogenesis pages 3-5, bette2024cottontailrabbitpapillomavirus pages 2-3). The early gene products control viral replication, transcription regulation, and cellular transformation, while L1 and L2 encode the viral capsid proteins.

### Oncoproteins and Molecular Mechanisms

The following table summarizes the key molecular mechanisms of HPV oncoproteins:

| Viral Protein | Host Target | Mechanism | Signaling Pathway | Biological Consequence |
|---|---|---|---|---|
| E6 | TP53 (p53) via E6AP/UBE3A | Forms E6–E6AP complex that ubiquitinates and degrades p53 | p53/cell-cycle checkpoint, apoptosis | Loss of G1/S arrest, impaired DNA-damage response, reduced apoptosis, mutation accumulation (martinelli2025molecularmechanismsand pages 4-5, wu2024unveilingthemultifaceted pages 2-3, mlynarczykbonikowska2024hpvinfections—classificationpathogenesis pages 10-11, baba2025humanpapillomavirus pages 4-6) |
| E6 | hTERT promoter/telomerase machinery | Induces hTERT expression and telomerase activation | Telomere maintenance/immortalization | Cellular immortalization and prolonged survival of infected cells (wu2024unveilingthemultifaceted pages 2-3, mlynarczykbonikowska2024hpvinfections—classificationpathogenesis pages 10-11, kao2026theroleof pages 3-5) |
| E6 | PTEN/TSC2 and upstream PI3K regulators | Inactivates PTEN and promotes mTOR signaling, enhancing PI3K/AKT activity | PI3K/AKT/mTOR | Increased proliferation, survival, autophagy inhibition, treatment resistance (baba2025humanpapillomavirus pages 6-8, martinelli2025molecularmechanismsand pages 4-5, pavelescu2025molecularinsightsinto pages 8-10) |
| E6 | β-catenin regulatory axis | Stabilizes/activates nuclear β-catenin and oncogenic transcription | Wnt/β-catenin | Upregulation of c-Myc/cyclin D1, enhanced growth and transformation (baba2025humanpapillomavirus pages 6-8, pavelescu2025molecularinsightsinto pages 8-10) |
| E6 | NOTCH1 and associated control of differentiation | Disrupts NOTCH1 signaling and p53-linked differentiation/senescence programs | Notch signaling | Loss of differentiation, escape from senescence, tumor progression (baba2025humanpapillomavirus pages 6-8, martinelli2025molecularmechanismsand pages 4-5, pavelescu2025molecularinsightsinto pages 8-10) |
| E7 | RB1 (pRb) via LXCXE motif | Binds pocket proteins and promotes pRb degradation/inactivation | pRb/E2F cell-cycle control | Unchecked G1-to-S progression and viral/cellular DNA synthesis (martinelli2025molecularmechanismsand pages 4-5, mlynarczykbonikowska2024hpvinfections—classificationpathogenesis pages 10-11, baba2025humanpapillomavirus pages 4-6) |
| E7 | E2F transcription factors | Releases E2F after pRb inactivation | E2F-driven transcription | Increased S-phase entry, replication gene expression, uncontrolled proliferation (martinelli2025molecularmechanismsand pages 4-5, mlynarczykbonikowska2024hpvinfections—classificationpathogenesis pages 10-11, baba2025humanpapillomavirus pages 4-6) |
| E7 | Centrosome duplication machinery | Perturbs centrosome control and mitotic fidelity | Chromosomal stability/mitotic control | Aneuploidy, chromosomal instability, invasive transformation (martinelli2025molecularmechanismsand pages 5-7) |
| E5 | EGFR | Enhances EGFR signaling and downstream kinase activation | EGFR/MAPK/ERK, PI3K/AKT | Increased proliferation, survival, migration, oncogene induction (including c-Fos) (baba2025humanpapillomavirus pages 6-8, vallejoruiz2024molecularaspectsof pages 2-3, pavelescu2025molecularinsightsinto pages 8-10) |
| E5 | MHC-I trafficking machinery | Retains MHC-I in ER/Golgi and reduces surface antigen presentation | Antigen presentation/immune evasion | Reduced CD8+ T-cell recognition and viral persistence (baba2025humanpapillomavirus pages 6-8, vallejoruiz2024molecularaspectsof pages 2-3) |
| E5 | STING (TMEM173) innate sensing pathway | Interferes with STING signaling and downstream interferon induction | cGAS–STING / innate antiviral response | Blunted interferon response and enhanced immune escape/persistence (vallejoruiz2024molecularaspectsof pages 2-3) |
| APOBEC3B induction in HPV-driven cells | Host genomic DNA (cytidines), linked to E6-driven dysregulation | Cytidine deamination produces APOBEC mutational signatures and hotspot mutations | APOBEC mutagenesis / genomic instability | C→T transition burden, oncogenic mutations (e.g., PIK3CA hotspots), malignant progression (janiszewska2025hpvdrivenoncogenesis—muchmore pages 3-4, janiszewska2025hpvdrivenoncogenesis—muchmore pages 4-6) |


*Table: This table summarizes the major HPV molecular mechanisms most relevant to persistence, immune evasion, and carcinogenesis. It highlights how E5, E6, E7, and APOBEC-associated processes map onto host targets and signaling pathways.*

**E6 Oncoprotein:** E6 forms a complex with E6-associated protein (E6AP/UBE3A), an E3 ubiquitin ligase, to target p53 for proteasomal degradation, eliminating G1/S checkpoint control and DNA damage response (wu2024unveilingthemultifaceted pages 2-3, mlynarczykbonikowska2024hpvinfections—classificationpathogenesis pages 10-11, baba2025humanpapillomavirus pages 4-6). E6 additionally induces hTERT expression for cellular immortalization, activates PI3K/AKT/mTOR signaling (inhibiting autophagy and promoting proliferation), stabilizes Wnt/β-catenin signaling (upregulating c-Myc and cyclin D1), and disrupts Notch1 signaling (baba2025humanpapillomavirus pages 6-8, pavelescu2025molecularinsightsinto pages 8-10). E6 also inhibits extrinsic apoptosis by interacting with FADD and caspase-8 and suppresses IRF-3 to diminish immune responses (wu2024unveilingthemultifaceted pages 2-3).

**E7 Oncoprotein:** E7 binds retinoblastoma protein (pRb) and related pocket proteins (p107, p130) through the LXCXE binding motif, causing their ubiquitination and proteasomal degradation (baba2025humanpapillomavirus pages 4-6). This releases E2F transcription factors, driving S-phase cell cycle progression (martinelli2025molecularmechanismsand pages 4-5, baba2025humanpapillomavirus pages 4-6). E7 also disrupts centrosome duplication leading to chromosomal instability, activates DNA methyltransferases causing aberrant epigenetic modifications, and modulates STAT1, NF-κB, IRF1, and SMAD2/3 transcription factors (martinelli2025molecularmechanismsand pages 4-5, martinelli2025molecularmechanismsand pages 5-7).

**E5 Oncoprotein:** E5 enhances EGFR signaling to activate MAPK/ERK and PI3K/AKT pathways, promoting proliferation and survival (baba2025humanpapillomavirus pages 6-8, vallejoruiz2024molecularaspectsof pages 2-3). E5 mediates immune evasion by retaining MHC-I molecules in the ER/Golgi, reducing antigen presentation, and by interfering with STING signaling to suppress interferon responses (vallejoruiz2024molecularaspectsof pages 2-3).

### Viral Integration and Genomic Instability
HPV integration into the host genome occurs in 70–85% of HPV-positive cancers and represents a critical transition from infection to malignancy (martinelli2025molecularmechanismsand pages 5-7). Integration typically disrupts the E2 gene, removing its suppressive effect on E6/E7 expression and allowing unrestricted oncoprotein activity (kao2026theroleof pages 3-5, janiszewska2025hpvdrivenoncogenesis—muchmore pages 1-3). Integration occurs at fragile sites in the host genome and causes direct genomic instability through disruption of tumor suppressor genes and upregulation of oncogenes (janiszewska2025hpvdrivenoncogenesis—muchmore pages 3-4, martinelli2025molecularmechanismsand pages 5-7).

### APOBEC Mutagenesis
A recently characterized non-canonical mechanism involves APOBEC3B enzymes, which are activated by interferon-mediated immune responses to viral nucleic acids. These enzymes mediate cytidine deamination, generating C→T transition mutations in the host genome that promote malignant transformation (janiszewska2025hpvdrivenoncogenesis—muchmore pages 3-4). E6 oncoprotein expression drives APOBEC3B overexpression through TP53 degradation and TEAD transcription factor activation. APOBEC has been identified as the dominant mutational signature in HPV16+ oropharyngeal cancers, with direct links to oncogenic mutations such as PIK3CA E542K/E545K hotspots (janiszewska2025hpvdrivenoncogenesis—muchmore pages 3-4, janiszewska2025hpvdrivenoncogenesis—muchmore pages 4-6).

### HPV-Derived miRNAs
Five putative HPV16-encoded miRNAs (miR-H1, H2, H3, H5, H6) have been identified, showing low-level expression in cervical lesions (janiszewska2025hpvdrivenoncogenesis—muchmore pages 4-6). These may contribute to immune escape, cell cycle deregulation, and tumor suppressor attenuation, though significant inconsistencies exist between research groups regarding their targets and functional significance (janiszewska2025hpvdrivenoncogenesis—muchmore pages 6-7, janiszewska2025hpvdrivenoncogenesis—muchmore pages 4-6).

### Epigenetic Changes
DNA methylation represents one of the earliest and most clinically informative epigenetic alterations in HPV-driven carcinogenesis (legaki2026hpvdrivencervicalcarcinogenesis pages 4-5). E7 activates DNA methyltransferases causing aberrant hypermethylation of tumor suppressor genes including CDKN2A and CDH1 (olokede2026areviewon pages 16-17, baba2025humanpapillomavirus pages 4-6). Host gene methylation biomarkers including FAM19A4, CADM1, PAX1, and MAL show promise for detecting high-grade intraepithelial lesions (legaki2026hpvdrivencervicalcarcinogenesis pages 1-2, li2025biomarkersdifferentiatingregression pages 8-9). DNMT3B polymorphisms (-149C>T) promote hypermethylation of tumor suppressors (olokede2026areviewon pages 16-17).

---

## 5. Environmental Information and Infectious Agent

### Infectious Agent
**Pathogen:** Human papillomavirus (HPV), Family Papillomaviridae, small non-enveloped DNA virus (NCBI Taxonomy ID: 10566 for HPV16)

HPV is classified into five genera (alpha, beta, gamma, mu, nu), with the alpha genus being most clinically significant for mucosal infections and malignancies (wu2024unveilingthemultifaceted pages 1-2). At least 14 high-risk types (Group 1 carcinogens per IARC) are recognized: HPV 16, 18, 31, 33, 35, 39, 45, 51, 52, 56, 58, 59, and 68 (pavelescu2025molecularinsightsinto pages 2-4). HPV is resistant to many disinfectants and relatively unsusceptible to external conditions (mlynarczykbonikowska2024hpvinfections—classificationpathogenesis pages 1-2).

### Lifestyle and Environmental Cofactors
Tobacco smoking, UV radiation exposure (particularly for beta-HPV-associated cutaneous malignancies), long-term hormonal contraceptive use, and high parity act as cofactors that augment HPV-driven carcinogenesis (pavelescu2025molecularinsightsinto pages 2-4).

---

## 6. Mechanism / Pathophysiology

### Causal Chain: From Infection to Cancer

1. **Initial Infection:** HPV gains access to basal epithelial cells through microabrasions in stratified squamous epithelium (jain2023epidemiologymolecularpathogenesis pages 3-5)
2. **Viral Establishment:** The virus establishes episomal infection in basal cells, maintaining low copy numbers and utilizing host DNA replication machinery (jain2023epidemiologymolecularpathogenesis pages 3-5)
3. **Immune Evasion:** E5 downregulates MHC-I/II and inhibits STING-interferon signaling; E6 suppresses IRF-3; E7 suppresses RIG-I and cGAS-STING pathways (baba2025humanpapillomavirus pages 6-8, vallejoruiz2024molecularaspectsof pages 2-3)
4. **Viral Persistence:** In 10–20% of infected women, immune evasion enables chronic infection lasting years (jain2023epidemiologymolecularpathogenesis pages 2-3)
5. **Genomic Integration:** Viral DNA integrates into host genome at fragile sites (70–85% of HPV+ cancers), disrupting E2 and unleashing constitutive E6/E7 expression (martinelli2025molecularmechanismsand pages 5-7)
6. **Cellular Transformation:** E6-mediated p53 degradation and E7-mediated pRb inactivation abolish cell cycle checkpoints, while APOBEC mutagenesis generates somatic mutations (wu2024unveilingthemultifaceted pages 2-3, baba2025humanpapillomavirus pages 4-6, janiszewska2025hpvdrivenoncogenesis—muchmore pages 3-4)
7. **Malignant Progression:** Accumulated genetic and epigenetic alterations, chromosomal instability, and immune microenvironment remodeling drive progression from CIN to invasive carcinoma (legaki2026hpvdrivencervicalcarcinogenesis pages 1-2, martinelli2025molecularmechanismsand pages 5-7)

### Key Signaling Pathways
- **p53/apoptosis pathway** (GO:0006915 apoptotic process): E6-mediated p53 degradation
- **pRb/E2F/cell cycle** (GO:0007049 cell cycle): E7-mediated pRb inactivation
- **PI3K/AKT/mTOR** (GO:0043491): E6/E7 activation promoting proliferation
- **Wnt/β-catenin** (GO:0060070): E6-mediated β-catenin stabilization
- **MAPK/ERK** (GO:0000165): E5-mediated EGFR activation
- **cGAS-STING/interferon** (GO:0032481): E5-mediated immune suppression
- **DNA damage response** (GO:0006281): E6/E7 hijacking of ATM/ATR, BRCA1, RAD51 (martinelli2025molecularmechanismsand pages 17-18, kao2026theroleof pages 3-5)

### Cell Types Involved
- **Basal keratinocytes** (CL:0000312): Primary target cells for HPV infection
- **Cervical epithelial cells** (CL:0002535): Site of cervical carcinogenesis
- **CD4+ T helper cells** (CL:0000492): Critical for HPV clearance; modulated by HLA-mediated antigen presentation
- **CD8+ cytotoxic T cells** (CL:0000794): Effector cells for eliminating HPV-infected cells

---

## 7. Anatomical Structures Affected

### Organ Level
- **Primary organs:** Uterine cervix (UBERON:0000002), oropharynx (UBERON:0001729), anus (UBERON:0001245), vulva, vagina, penis
- **Secondary involvement:** Regional lymph nodes (metastatic spread), respiratory tract (laryngeal papillomatosis)
- **Body systems:** Reproductive system, integumentary system, upper aerodigestive tract

### Tissue and Cell Level
- **Tissues affected:** Stratified squamous epithelium (mucosal and cutaneous), transformation zone of cervix
- **Specific cell populations:** Basal epithelial cells (primary viral targets), squamous epithelial cells at various differentiation stages

### Localization
HPV infection sites correspond to virus-epithelium tropism. Alpha-HPV types predominantly affect anogenital and oropharyngeal mucosal epithelium, while beta, gamma, mu, and nu types primarily affect cutaneous epithelium (wu2024unveilingthemultifaceted pages 1-2). HPV-associated lesions can be bilateral and multifocal.

---

## 8. Temporal Development

### Onset
- **Age of acquisition:** Peak incidence in sexually active teens and young adults (jain2023epidemiologymolecularpathogenesis pages 2-3)
- **Onset pattern:** Typically insidious; infection is usually asymptomatic, with clinical manifestations developing weeks to years after exposure (branda2024humanpapillomavirus(hpv) pages 7-9)

### Progression
- **Natural history:** Most infections (approximately 90%) resolve spontaneously within 1–2 years through immune clearance (baba2025humanpapillomavirus pages 1-2). Persistent infection with high-risk types over years to decades may progress through CIN1 → CIN2 → CIN3 → invasive carcinoma (legaki2026hpvdrivencervicalcarcinogenesis pages 1-2)
- **Disease duration:** Self-limited in most cases; chronic lifelong in persistent infections
- **Critical period:** The interval between persistent high-risk HPV infection and invasive cancer development typically spans 10–20 years, providing a window for screening and intervention

---

## 9. Inheritance and Population

### Epidemiology
- **Global prevalence:** Approximately 291 million women worldwide carry HPV; estimated 79 million Americans currently infected (pavelescu2025molecularinsightsinto pages 2-4, maghiar2024skinlesionscaused pages 2-4)
- **Incidence:** Approximately 14 million new infections annually in the U.S.; globally, HPV causes approximately 610,000 cancer cases and over 250,000 deaths annually (maghiar2024skinlesionscaused pages 2-4, wu2024unveilingthemultifaceted pages 1-2)
- **Geographic variation:** HPV prevalence is significantly higher in developing regions (42.2%) compared to developed regions (22.6%), with particularly high rates in Sub-Saharan Africa (24%), Latin America, and parts of Asia (jain2023epidemiologymolecularpathogenesis pages 2-3). In 2020, cervical cancer had 604,127 new cases and 341,831 deaths globally (jain2023epidemiologymolecularpathogenesis pages 2-3)

### Host Genetic Architecture
While HPV infection itself is infectious (not inherited), host genetic susceptibility to persistent infection and cancer development follows a polygenic architecture, with heritability estimates of 27–29% for cervical carcinoma liability (olokede2026areviewon pages 6-7). HLA allele frequencies vary dramatically across geographic ancestries, with protective alleles more prevalent in European populations but absent in sub-Saharan African cohorts where cervical cancer burden is highest (olokede2026areviewon pages 6-7).

### Population Demographics
- **Sex ratio:** Both sexes affected; 85% of women and 95% of sexually active men are infected at some point (jain2023epidemiologymolecularpathogenesis pages 2-3)
- **Age distribution:** Bimodal age distribution for HPV prevalence in women, with peaks in young adults and women aged 45+ (pavelescu2025molecularinsightsinto pages 2-4)

---

## 10. Diagnostics

### Clinical Tests
- **Papanicolaou (Pap) smear:** Cytological screening that detects LSIL/HSIL; has significantly reduced cervical cancer incidence but has limited sensitivity (baba2025humanpapillomavirus pages 10-11, wu2024unveilingthemultifaceted pages 9-10)
- **HPV DNA testing:** Detects high-risk HPV nucleic acids via PCR; more accurate and objective than cytology; WHO-endorsed as preferred cervical cancer screening strategy (maghiar2024skinlesionscaused pages 4-6, maghiar2024skinlesionscaused pages 6-7)
- **HPV mRNA PCR:** Reflects active viral transcription and provides prognostic information (baba2025humanpapillomavirus pages 10-11)
- **Colposcopy:** Non-invasive examination using 3–5% acetic acid to identify acetowhite changes and abnormal vascular patterns (branda2024humanpapillomavirus(hpv) pages 7-9)
- **Visual inspection with acetic acid (VIA):** Low-cost screening approach for resource-limited settings (jain2023epidemiologymolecularpathogenesis pages 10-12)
- **Biopsy and histopathology:** Tissue analysis showing papillomatosis, hypergranulosis, acanthosis, and koilocytosis (karaoglan2024unveilingtherole pages 3-4)
- **Immunohistochemistry:** Detection of HPV capsid proteins; p16ink4a overexpression as surrogate marker of high-risk HPV E7 activity (branda2024humanpapillomavirus(hpv) pages 5-6, karaoglan2024unveilingtherole pages 3-4)
- **Next-generation sequencing:** Highly sensitive detection of low-copy-number types and novel variants (karaoglan2024unveilingtherole pages 3-4)

### Biomarkers
- **p16ink4a/Ki-67 dual staining:** Protein biomarkers for high-grade cervical dysplasia detection (branda2024humanpapillomavirus(hpv) pages 5-6)
- **DNA methylation biomarkers:** FAM19A4, CADM1, PAX1, and MAL methylation as promising markers for CIN2+ detection (legaki2026hpvdrivencervicalcarcinogenesis pages 1-2, li2025biomarkersdifferentiatingregression pages 8-9)
- **E6/E7 mRNA expression:** Indicates active viral oncogene transcription (branda2024humanpapillomavirus(hpv) pages 5-6)

### Self-Sampling
Modern guidelines, including 2025 ASCCP recommendations, advocate for self-collected vaginal samples for high-risk HPV testing to improve screening accessibility, with WHO targeting 70% of women screened by 2030 (legaki2026hpvdrivencervicalcarcinogenesis pages 1-2, maghiar2024skinlesionscaused pages 6-7).

---

## 11. Outcome/Prognosis

### Survival and Mortality
- Most HPV infections are self-limited, with ~90% clearing within 2 years (baba2025humanpapillomavirus pages 1-2)
- 10–20% of infected women develop persistent infection with potential for malignant progression (jain2023epidemiologymolecularpathogenesis pages 2-3)
- Cervical cancer: 604,127 new cases and 341,831 deaths globally in 2020 (jain2023epidemiologymolecularpathogenesis pages 2-3)
- HPV-positive oropharyngeal cancer patients demonstrate better clinical prognosis and heightened radiosensitivity compared to HPV-negative counterparts (martinelli2025molecularmechanismsand pages 4-5)
- Approximately 47,200 new HPV-associated cancer cases occur annually in the U.S. (malik2023trackinghpvinfection pages 1-2)

### Prognostic Biomarkers
- HPV genotype (HPV16/18 vs. other high-risk types) (li2025biomarkersdifferentiatingregression pages 6-7)
- HLA alleles: DRB1*1302-positive women had significantly lower cumulative CIN3 progression rates (2.1% vs 14.0% over 10 years) (li2025biomarkersdifferentiatingregression pages 8-9)
- DNA methylation patterns (FAM19A4, miR-124-2, EPB41L3) for CIN2 regression/progression prediction (li2025biomarkersdifferentiatingregression pages 8-9)
- p16/Ki-67 status for CIN2 outcome prediction (li2025biomarkersdifferentiatingregression pages 6-7)

---

## 12. Treatment

The following table provides a comprehensive overview of current and emerging HPV treatment and prevention approaches:

| Category | Intervention | Mechanism/Description | Evidence Level |
|---|---|---|---|
| Physical treatment | Cryotherapy | Liquid nitrogen freezing destroys visible HPV-associated lesions such as warts; commonly used office-based ablative treatment (jain2023epidemiologymolecularpathogenesis pages 12-13, maghiar2024skinlesionscaused pages 6-7) | Established clinical practice / guideline-supported review evidence |
| Physical treatment | LEEP | Loop electrosurgical excision procedure removes cervical transformation-zone tissue and is used for treatment of high-grade cervical intraepithelial lesions (jain2023epidemiologymolecularpathogenesis pages 12-13) | Established clinical practice / guideline-supported review evidence |
| Physical treatment | Electrocautery | Thermal destruction/removal of wart tissue or dysplastic lesions; used for anogenital and cutaneous lesions (jain2023epidemiologymolecularpathogenesis pages 12-13, maghiar2024skinlesionscaused pages 6-7) | Established clinical practice / review evidence |
| Physical treatment | Laser therapy | CO2 or related laser ablation for extensive, refractory, or anatomically difficult lesions (jain2023epidemiologymolecularpathogenesis pages 12-13, maghiar2024skinlesionscaused pages 6-7) | Established clinical practice / review evidence |
| Physical treatment | Surgical excision | Direct removal of resistant or suspicious lesions; effective but may require anesthesia and can scar (maghiar2024skinlesionscaused pages 7-9, maghiar2024skinlesionscaused pages 6-7) | Established clinical practice / review evidence |
| Chemical treatment | Salicylic acid | Topical keratolytic that gradually destroys hyperkeratotic wart tissue; requires repeated application (maghiar2024skinlesionscaused pages 7-9, maghiar2024skinlesionscaused pages 6-7) | Established clinical practice / review evidence |
| Chemical treatment | Cantharidin | Vesicant topical agent that induces blistering and separation of lesion tissue in wart management (maghiar2024skinlesionscaused pages 7-9, maghiar2024skinlesionscaused pages 6-7) | Established clinical practice / review evidence |
| Immunomodulatory | Imiquimod (TLR7 agonist) | Activates TLR7-mediated innate immune signaling to enhance local antiviral immune response; used particularly for anogenital warts (jain2023epidemiologymolecularpathogenesis pages 12-13, OpenTargets Search: human papillomavirus infectious disease,cervical carcinoma) | Approved targeted therapy / OpenTargets-supported association |
| Prophylactic vaccine | Cervarix (bivalent) | L1 virus-like particle vaccine targeting HPV16/18 to prevent acquisition of high-risk infection and cervical precancer/cancer (jain2023epidemiologymolecularpathogenesis pages 12-13, wu2024unveilingthemultifaceted pages 9-10, jain2023epidemiologymolecularpathogenesis pages 10-12) | High-level evidence; licensed vaccine |
| Prophylactic vaccine | Gardasil (quadrivalent) | L1 VLP vaccine targeting HPV6/11/16/18; prevents genital warts and high-risk HPV infection (wu2024unveilingthemultifaceted pages 9-10, jain2023epidemiologymolecularpathogenesis pages 10-12) | High-level evidence; licensed vaccine |
| Prophylactic vaccine | Gardasil 9 (nonavalent) | Expanded L1 VLP vaccine covering HPV6/11/16/18/31/33/45/52/58; broadest currently licensed prophylactic coverage in many settings (jain2023epidemiologymolecularpathogenesis pages 12-13, wu2024unveilingthemultifaceted pages 9-10, jain2023epidemiologymolecularpathogenesis pages 10-12) | High-level evidence; licensed vaccine |
| Prophylactic vaccine | Cecolin | Bivalent prophylactic HPV vaccine included among currently available VLP-based vaccines (jain2023epidemiologymolecularpathogenesis pages 10-12) | Licensed/implementation evidence in reviews |
| Prophylactic vaccine | Cervavax | Quadrivalent prophylactic HPV vaccine included in current vaccine landscape reviews (jain2023epidemiologymolecularpathogenesis pages 12-13, jain2023epidemiologymolecularpathogenesis pages 10-12) | Licensed/implementation evidence in reviews |
| Therapeutic vaccine | Viral vector-based vaccines | Experimental vaccines deliver HPV antigens, usually E6/E7, via viral vectors to induce cell-mediated clearance of infected/transformed cells (branda2024humanpapillomavirus(hpv) pages 5-6, jain2023epidemiologymolecularpathogenesis pages 22-24) | Early-phase/experimental |
| Therapeutic vaccine | DNA-based vaccines | Plasmid/DNA immunization strategies encoding HPV antigens aim to generate cytotoxic T-cell responses against established infection or dysplasia (jain2023epidemiologymolecularpathogenesis pages 22-24) | Early-phase/experimental |
| Chemotherapy | Cisplatin-based combinations | Standard systemic therapy for advanced cervical cancer; combinations with bevacizumab, topotecan, paclitaxel, 5-FU, or bleomycin improve antitumor activity in selected settings (baba2025humanpapillomavirus pages 15-17) | Standard oncology practice / review evidence |
| Immunotherapy | Pembrolizumab | Immune checkpoint inhibitor targeting PD-1; used in HPV-related cancers, especially recurrent/metastatic cervical cancer and other advanced HPV-driven malignancies (maghiar2024skinlesionscaused pages 7-9, baba2025humanpapillomavirus pages 15-17) | Approved/late-stage oncology evidence |
| Immunotherapy | Nivolumab | PD-1 checkpoint blockade investigated/used in HPV-associated cancers to restore antitumor T-cell function (baba2025humanpapillomavirus pages 15-17) | Clinical evidence / advanced oncology use |
| Immunotherapy | Durvalumab | PD-L1 checkpoint inhibitor under study or use in HPV-mediated cancers as immune-restorative therapy (baba2025humanpapillomavirus pages 15-17) | Clinical evidence / advanced oncology use |
| Advanced therapy | siRNA targeting E6/E7 | RNA interference suppresses viral oncogene expression, restoring p53/p21 signaling and inhibiting tumor growth; preclinical LNP-siRNA plus cisplatin data are promising (baba2025humanpapillomavirus pages 15-17) | Preclinical to early translational |
| Advanced therapy | CRISPR/Cas9 targeting E6/E7 | Gene-editing approaches disrupt HPV oncogenes and can trigger tumor cell death or growth arrest in experimental systems (baba2025humanpapillomavirus pages 15-17) | Experimental / preclinical |
| Screening program | Pap smear (cytology) | Cytologic screening detects LSIL/HSIL and has reduced cervical cancer incidence and mortality where implemented (branda2024humanpapillomavirus(hpv) pages 7-9, baba2025humanpapillomavirus pages 10-11, wu2024unveilingthemultifaceted pages 9-10) | Established population screening |
| Screening program | HPV DNA testing | Detects high-risk HPV nucleic acids; more accurate/objective than cytology and now preferred by WHO for cervical screening in many settings (maghiar2024skinlesionscaused pages 4-6, jain2023epidemiologymolecularpathogenesis pages 10-12, maghiar2024skinlesionscaused pages 6-7) | High-level evidence; preferred modern screening |
| Screening program | VIA (visual inspection with acetic acid) | Low-cost screening approach used especially in resource-limited settings to identify acetowhite cervical abnormalities (baba2025humanpapillomavirus pages 10-11, jain2023epidemiologymolecularpathogenesis pages 10-12) | Programmatic/public health screening evidence |


*Table: This table summarizes major current and emerging approaches to HPV treatment, prevention, and screening, spanning lesion-directed therapies, vaccines, systemic cancer treatments, and population screening tools. It is useful for quickly comparing mechanisms and maturity of evidence across interventions.*

### Key Therapeutic Targets (OpenTargets)
OpenTargets analysis (MONDO:0005161) identified three primary drug targets for HPV infection: TLR7 (toll-like receptor 7; highest association score 0.53, with approved drug imiquimod), IFNAR1 (interferon alpha/beta receptor subunit 1), and IFNAR2 (interferon alpha/beta receptor subunit 2) (OpenTargets Search: human papillomavirus infectious disease,cervical carcinoma).

### Emerging Therapies
- **siRNA-based approaches:** ENB101-LNP, encapsulating siRNA against HPV16 E6/E7, combined with cisplatin showed 68.8% tumor inhibition and up to 80% E6/E7 knockdown in xenograft models (baba2025humanpapillomavirus pages 15-17)
- **TCR-engineered T-cell therapies:** Targeting E7 oncoprotein for adoptive cell therapy (baba2025humanpapillomavirus pages 15-17)
- **CRISPR/Cas9 gene editing:** Targeting E6/E7 genomic sequences to induce tumor cell death (baba2025humanpapillomavirus pages 15-17)
- **PARP inhibitors:** E7-mediated upregulation of miR-182 downregulates BRCA1, potentially sensitizing HPV+ cancers to PARP inhibition (martinelli2025molecularmechanismsand pages 17-18)

### Active Clinical Trials
Multiple Phase 3 clinical trials are currently investigating HPV vaccines and treatments, including:
- CERVAVAC® quadrivalent HPV vaccine in HIV-positive women aged 15–25 (NCT06281119; 450 participants)
- Nonavalent HPV vaccine efficacy trial (NCT05668572; 12,000 participants)
- Dose reduction immunobridging studies in African settings (NCT02834637; 930 participants)

MAXO terms: MAXO:0001017 (vaccination), MAXO:0000004 (surgical procedure), MAXO:0010203 (cryotherapy), MAXO:0000647 (chemotherapy)

---

## 13. Prevention

### Primary Prevention
**Vaccination** is the most effective primary prevention strategy. Currently licensed prophylactic vaccines include bivalent (Cervarix: HPV16/18), quadrivalent (Gardasil: HPV6/11/16/18), and nonavalent (Gardasil 9: HPV6/11/16/18/31/33/45/52/58) formulations, as well as Cecolin and Cervavax (jain2023epidemiologymolecularpathogenesis pages 12-13, jain2023epidemiologymolecularpathogenesis pages 10-12). In Australia, HPV prevalence dropped from 22.7% pre-vaccination to 1.5% by 2015 (ashique2023hpvpathogenesisvarious pages 2-4). Countries with robust vaccination programs have witnessed 54–83% declines in high-grade cervical abnormalities and genital warts (jain2023epidemiologymolecularpathogenesis pages 12-13). WHO targets 90% of girls vaccinated by age 15 as part of the cervical cancer elimination strategy (jain2023epidemiologymolecularpathogenesis pages 10-12).

### Secondary Prevention
Screening programs form the backbone of secondary prevention. HPV DNA testing is now endorsed by WHO as the preferred cervical cancer screening strategy over conventional cytology (maghiar2024skinlesionscaused pages 4-6). The WHO Global Strategy targets screening 70% of women at ages 35 and 45 and ensuring 90% of women with cervical disease receive proper treatment (jain2023epidemiologymolecularpathogenesis pages 10-12). Concomitant HPV vaccination and screening has been proposed for faster cervical cancer elimination (wu2024unveilingthemultifaceted pages 9-10).

### Tertiary Prevention
Management of established CIN and HPV-associated cancers through LEEP, surgical excision, chemotherapy, radiation therapy, and immunotherapy (jain2023epidemiologymolecularpathogenesis pages 12-13, baba2025humanpapillomavirus pages 15-17).

---

## 14. Other Species / Natural Disease

### Taxonomy and Comparative Biology
Papillomaviruses exhibit extremely high host species specificity, infecting various species including fish, reptiles, birds, and vertebrates (bette2024cottontailrabbitpapillomavirus pages 1-2). Due to this species restriction, human HPV types cannot infect animals, and animal papillomaviruses cannot infect humans.

**Natural papillomavirus infections in other species:**
- **Cottontail rabbit (Sylvilagus floridanus):** CRPV (Cottontail Rabbit Papillomavirus) causes cutaneous papillomas with high oncogenic potential for progression to squamous cell carcinomas, predominantly on the head and neck (bette2024cottontailrabbitpapillomavirus pages 1-2, bette2024cottontailrabbitpapillomavirus pages 3-5)
- **Domestic rabbit (Oryctolagus cuniculus):** Experimentally susceptible to CRPV infection (bette2024cottontailrabbitpapillomavirus pages 1-2)
- **Canine species:** Canine oral papillomavirus causes papillomas; dogs have immune systems more closely resembling human responses (totain2023developmentofhpv16 pages 7-10)

CRPV E7 inhibits retinoblastoma protein similar to HPV E7, but CRPV E6 differs by binding hDlg/SAP97 rather than p53 (bette2024cottontailrabbitpapillomavirus pages 2-3). Rabbit papillomas and carcinomas closely resemble human HPV-induced tumors (bette2024cottontailrabbitpapillomavirus pages 2-3).

---

## 15. Model Organisms

### Mouse Models
- **TC-1 cells (C57BL/6):** The most commonly used HPV model; C57BL/6 cells expressing HPV16 E6/E7 proteins, used for subcutaneous tumor isograft studies (totain2023developmentofhpv16 pages 1-2). Limitations include restriction to one genetic background and HPV16-only studies.
- **K14-HPV16 transgenic mice:** Express E7 constitutively in skin under keratin 14 promoter; develop immune tolerance, limiting utility for immunotherapy testing (totain2023developmentofhpv16 pages 1-2)
- **HPV16 E6-E7 transgenic mice:** Genetically engineered using CRISPR/Cas9 to express HPV16 E6/E7 in the cervicovaginal tract, spontaneously developing vaginal-cervical intraepithelial neoplasia (xiurong2024geneticallyengineeredmouse pages 9-10)
- **E7inv conditional transgenic mice:** Novel Cre-lox inducible model allowing controlled E7 expression with GFP reporter monitoring (totain2023developmentofhpv16 pages 7-10)

### Rabbit Models
- **CRPV/VX2 model:** VX2 carcinoma cells derived from CRPV-induced squamous cell carcinomas in New Zealand White rabbits, maintained through serial transplantation for nearly 90 years (bette2024cottontailrabbitpapillomavirus pages 16-17). VX2 cells generate metastatic tumors enabling testing of surgical procedures, radiological techniques, chemotherapies, and checkpoint inhibitors in an immunocompetent system (bette2024cottontailrabbitpapillomavirus pages 16-17).
- **CRPV/VX7 model:** Alternative carcinoma cell line for experimental papillomavirus studies (bette2024cottontailrabbitpapillomavirus pages 19-20)

### Dog Models
Beagle dogs have been developed as HPV16 preclinical models since their immune systems more closely resemble human responses and better reproduce inter-individual MHC diversity variations compared to inbred mouse models (totain2023developmentofhpv16 pages 7-10, totain2023developmentofhpv16 pages 1-2). Lentiviral vectors deliver E7/HPV16 transgenes locally in muscle tissue for vaccine efficacy assessment.

### Model Limitations
The TC-1 mouse model, despite being widely used, demonstrated correlations with the clinical failure of the ProCervix therapeutic vaccine: C216 vaccine (similar to ProCervix) induced strong immune responses in both mouse and dog models but failed to adequately eliminate E7-expressing cells, aligning with Phase II clinical trial failure (totain2023developmentofhpv16 pages 7-10, totain2023developmentofhpv16 pages 1-2). This highlights the challenge of translating preclinical immunogenicity to clinical efficacy.

---

## Summary of Ontology Term Suggestions

**MONDO:** MONDO:0005161 (human papilloma virus infection), MONDO:0005647 (anogenital HPV infection)

**HPO Terms:** HP:0200043 (Verrucae), HP:0030799 (Condylomata acuminata), HP:0012126 (Cervical squamous cell carcinoma), HP:0100649 (Neoplasm of oral cavity)

**GO Terms:** GO:0006915 (apoptotic process), GO:0007049 (cell cycle), GO:0043491 (protein kinase B signaling), GO:0060070 (Wnt signaling), GO:0000165 (MAPK cascade), GO:0032481 (regulation of type I interferon production), GO:0006281 (DNA repair)

**CL Terms:** CL:0000312 (keratinocyte), CL:0002535 (epithelial cell of cervix), CL:0000492 (CD4-positive helper T cell), CL:0000794 (CD8-positive cytotoxic T cell)

**UBERON Terms:** UBERON:0000002 (uterine cervix), UBERON:0001729 (oropharynx), UBERON:0001245 (anus)

**CHEBI Terms:** CHEBI:145994 (imiquimod), CHEBI:27899 (cisplatin)

**MAXO Terms:** MAXO:0001017 (vaccination), MAXO:0000004 (surgical procedure), MAXO:0010203 (cryotherapy), MAXO:0000647 (chemotherapy)

---

*This report synthesizes evidence from 21 peer-reviewed publications (2023–2026), OpenTargets disease-target associations, and 13 registered clinical trials. Information is derived primarily from aggregated disease-level resources including systematic reviews, comprehensive narrative reviews, and GWAS studies. All major claims are supported by cited primary literature.*

References

1. (jain2023epidemiologymolecularpathogenesis pages 3-5): Meenu Jain, Dhananjay Yadav, Urmila Jarouliya, Vishal Chavda, Arun Kumar Yadav, Bipin Chaurasia, and Minseok Song. Epidemiology, molecular pathogenesis, immuno-pathogenesis, immune escape mechanisms and vaccine evaluation for hpv-associated carcinogenesis. Pathogens, 12:1380, Nov 2023. URL: https://doi.org/10.3390/pathogens12121380, doi:10.3390/pathogens12121380. This article has 80 citations.

2. (wu2024unveilingthemultifaceted pages 1-2): Meng Wu, Hui Huang, Ying Tang, Xuze Ren, Xinrui Jiang, Man Tian, and Wei Li. Unveiling the multifaceted realm of human papillomavirus: a comprehensive exploration of biology, interactions, and advances in cancer management. Frontiers in Immunology, Aug 2024. URL: https://doi.org/10.3389/fimmu.2024.1430544, doi:10.3389/fimmu.2024.1430544. This article has 18 citations and is from a peer-reviewed journal.

3. (mlynarczykbonikowska2024hpvinfections—classificationpathogenesis pages 1-2): Beata Mlynarczyk-Bonikowska and Lidia Rudnicka. Hpv infections—classification, pathogenesis, and potential new therapies. International Journal of Molecular Sciences, 25:7616, Jul 2024. URL: https://doi.org/10.3390/ijms25147616, doi:10.3390/ijms25147616. This article has 109 citations.

4. (baba2025humanpapillomavirus pages 1-2): Sadaf Khursheed Baba, Shahad Shahdad Eissa Alblooshi, Reem Yaqoob, Shalini Behl, Mansour Al Saleem, Emad A. Rakha, Fayaz Malik, Mayank Singh, Muzafar A. Macha, Mohammed Kalim Akhtar, Walid A. Houry, Ajaz A. Bhat, Asma Al Menhali, Zhi-Ming Zheng, and Sameer Mirza. Human papilloma virus (hpv) mediated cancers: an insightful update. Journal of Translational Medicine, Apr 2025. URL: https://doi.org/10.1186/s12967-025-06470-x, doi:10.1186/s12967-025-06470-x. This article has 79 citations and is from a peer-reviewed journal.

5. (OpenTargets Search: human papillomavirus infectious disease,cervical carcinoma): Open Targets Query (human papillomavirus infectious disease,cervical carcinoma, 6 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

6. (maghiar2024skinlesionscaused pages 4-6): Laura Maghiar, Mircea Sandor, Liliana Sachelarie, Ruxandra Bodog, and Anca Huniadi. Skin lesions caused by hpv—a comprehensive review. Biomedicines, 12:2098, Sep 2024. URL: https://doi.org/10.3390/biomedicines12092098, doi:10.3390/biomedicines12092098. This article has 28 citations.

7. (branda2024humanpapillomavirus(hpv) pages 7-9): Francesco Branda, Grazia Pavia, Alessandra Ciccozzi, Angela Quirino, Nadia Marascio, Simona Gigliotti, Giovanni Matera, Chiara Romano, Chiara Locci, Ilenia Azzena, Noemi Pascale, Daria Sanna, Marco Casu, Giancarlo Ceccarelli, Massimo Ciccozzi, and Fabio Scarpa. Human papillomavirus (hpv) vaccination: progress, challenges, and future directions in global immunization strategies. Vaccines, 12:1293, Nov 2024. URL: https://doi.org/10.3390/vaccines12111293, doi:10.3390/vaccines12111293. This article has 42 citations.

8. (maghiar2024skinlesionscaused pages 2-4): Laura Maghiar, Mircea Sandor, Liliana Sachelarie, Ruxandra Bodog, and Anca Huniadi. Skin lesions caused by hpv—a comprehensive review. Biomedicines, 12:2098, Sep 2024. URL: https://doi.org/10.3390/biomedicines12092098, doi:10.3390/biomedicines12092098. This article has 28 citations.

9. (baba2025humanpapillomavirus pages 10-11): Sadaf Khursheed Baba, Shahad Shahdad Eissa Alblooshi, Reem Yaqoob, Shalini Behl, Mansour Al Saleem, Emad A. Rakha, Fayaz Malik, Mayank Singh, Muzafar A. Macha, Mohammed Kalim Akhtar, Walid A. Houry, Ajaz A. Bhat, Asma Al Menhali, Zhi-Ming Zheng, and Sameer Mirza. Human papilloma virus (hpv) mediated cancers: an insightful update. Journal of Translational Medicine, Apr 2025. URL: https://doi.org/10.1186/s12967-025-06470-x, doi:10.1186/s12967-025-06470-x. This article has 79 citations and is from a peer-reviewed journal.

10. (jain2023epidemiologymolecularpathogenesis pages 2-3): Meenu Jain, Dhananjay Yadav, Urmila Jarouliya, Vishal Chavda, Arun Kumar Yadav, Bipin Chaurasia, and Minseok Song. Epidemiology, molecular pathogenesis, immuno-pathogenesis, immune escape mechanisms and vaccine evaluation for hpv-associated carcinogenesis. Pathogens, 12:1380, Nov 2023. URL: https://doi.org/10.3390/pathogens12121380, doi:10.3390/pathogens12121380. This article has 80 citations.

11. (malik2023trackinghpvinfection pages 1-2): Shiza Malik, Ranjit Sah, Khalid Muhammad, and Yasir Waheed. Tracking hpv infection, associated cancer development, and recent treatment efforts—a comprehensive review. Vaccines, 11:102, Jan 2023. URL: https://doi.org/10.3390/vaccines11010102, doi:10.3390/vaccines11010102. This article has 61 citations.

12. (bette2024cottontailrabbitpapillomavirus pages 1-2): Michael Bette and Robert Mandic. Cottontail rabbit papillomavirus (crpv) related animal models for head and neck cancer research: a comprehensive review of the literature. Viruses, 16:1722, Oct 2024. URL: https://doi.org/10.3390/v16111722, doi:10.3390/v16111722. This article has 0 citations.

13. (pavelescu2025molecularinsightsinto pages 2-4): Luciana Alexandra Pavelescu, Nicoleta Larisa Mititelu-Zafiu, Dana Elena Mindru, Radu Vladareanu, and Antoanela Curici. Molecular insights into hpv-driven cervical cancer: oncoproteins, immune evasion, and epigenetic modifications. Microorganisms, 13:1000, Apr 2025. URL: https://doi.org/10.3390/microorganisms13051000, doi:10.3390/microorganisms13051000. This article has 34 citations.

14. (bette2024cottontailrabbitpapillomavirus pages 2-3): Michael Bette and Robert Mandic. Cottontail rabbit papillomavirus (crpv) related animal models for head and neck cancer research: a comprehensive review of the literature. Viruses, 16:1722, Oct 2024. URL: https://doi.org/10.3390/v16111722, doi:10.3390/v16111722. This article has 0 citations.

15. (olokede2026areviewon pages 6-7): Esther Olokede, Jumobi Abeebat Liasu-Thomas, Verity Ghansah, Bassey Atte Inyang, Damilola Rafiat Lamidi, Blessing Chinonye Okoro, and Adebola Ayisat Effa. A review on genetic epidemiology of host genetic structure, viral persistence, and immunological escape in hpv-mediated cervical carcinogenesis. Journal of Pharma Insights and Research, 4:259-295, Apr 2026. URL: https://doi.org/10.69613/d25y8z24, doi:10.69613/d25y8z24. This article has 0 citations.

16. (olokede2026areviewon pages 1-2): Esther Olokede, Jumobi Abeebat Liasu-Thomas, Verity Ghansah, Bassey Atte Inyang, Damilola Rafiat Lamidi, Blessing Chinonye Okoro, and Adebola Ayisat Effa. A review on genetic epidemiology of host genetic structure, viral persistence, and immunological escape in hpv-mediated cervical carcinogenesis. Journal of Pharma Insights and Research, 4:259-295, Apr 2026. URL: https://doi.org/10.69613/d25y8z24, doi:10.69613/d25y8z24. This article has 0 citations.

17. (pavelescu2025molecularinsightsinto pages 11-13): Luciana Alexandra Pavelescu, Nicoleta Larisa Mititelu-Zafiu, Dana Elena Mindru, Radu Vladareanu, and Antoanela Curici. Molecular insights into hpv-driven cervical cancer: oncoproteins, immune evasion, and epigenetic modifications. Microorganisms, 13:1000, Apr 2025. URL: https://doi.org/10.3390/microorganisms13051000, doi:10.3390/microorganisms13051000. This article has 34 citations.

18. (olokede2026areviewon pages 16-17): Esther Olokede, Jumobi Abeebat Liasu-Thomas, Verity Ghansah, Bassey Atte Inyang, Damilola Rafiat Lamidi, Blessing Chinonye Okoro, and Adebola Ayisat Effa. A review on genetic epidemiology of host genetic structure, viral persistence, and immunological escape in hpv-mediated cervical carcinogenesis. Journal of Pharma Insights and Research, 4:259-295, Apr 2026. URL: https://doi.org/10.69613/d25y8z24, doi:10.69613/d25y8z24. This article has 0 citations.

19. (li2025biomarkersdifferentiatingregression pages 8-9): Xiang Li, Yan Chen, Jing Xiong, Puxiang Chen, Dongdong Zhang, Qing Li, and Peng Zhu. Biomarkers differentiating regression from progression among untreated cervical intraepithelial neoplasia grade 2 lesions. Journal of Advanced Research, 74:391-402, Sep 2025. URL: https://doi.org/10.1016/j.jare.2024.09.009, doi:10.1016/j.jare.2024.09.009. This article has 22 citations and is from a peer-reviewed journal.

20. (wu2024unveilingthemultifaceted pages 9-10): Meng Wu, Hui Huang, Ying Tang, Xuze Ren, Xinrui Jiang, Man Tian, and Wei Li. Unveiling the multifaceted realm of human papillomavirus: a comprehensive exploration of biology, interactions, and advances in cancer management. Frontiers in Immunology, Aug 2024. URL: https://doi.org/10.3389/fimmu.2024.1430544, doi:10.3389/fimmu.2024.1430544. This article has 18 citations and is from a peer-reviewed journal.

21. (olokede2026areviewon pages 19-21): Esther Olokede, Jumobi Abeebat Liasu-Thomas, Verity Ghansah, Bassey Atte Inyang, Damilola Rafiat Lamidi, Blessing Chinonye Okoro, and Adebola Ayisat Effa. A review on genetic epidemiology of host genetic structure, viral persistence, and immunological escape in hpv-mediated cervical carcinogenesis. Journal of Pharma Insights and Research, 4:259-295, Apr 2026. URL: https://doi.org/10.69613/d25y8z24, doi:10.69613/d25y8z24. This article has 0 citations.

22. (legaki2026hpvdrivencervicalcarcinogenesis pages 1-2): Evangelia Legaki, Theofania Lappa, Konstantina-Lida Prasoula, Zoi Kardasi, Emmanouil Kalampokas, Theodoros Kalampokas, Maria G. Roubelakis, Ekaterina Charvalos, and Maria Gazouli. Hpv-driven cervical carcinogenesis: genetic and epigenetic mechanisms and diagnostic approaches. International Journal of Molecular Sciences, 27:803, Jan 2026. URL: https://doi.org/10.3390/ijms27020803, doi:10.3390/ijms27020803. This article has 4 citations.

23. (li2025biomarkersdifferentiatingregression pages 6-7): Xiang Li, Yan Chen, Jing Xiong, Puxiang Chen, Dongdong Zhang, Qing Li, and Peng Zhu. Biomarkers differentiating regression from progression among untreated cervical intraepithelial neoplasia grade 2 lesions. Journal of Advanced Research, 74:391-402, Sep 2025. URL: https://doi.org/10.1016/j.jare.2024.09.009, doi:10.1016/j.jare.2024.09.009. This article has 22 citations and is from a peer-reviewed journal.

24. (martinelli2025molecularmechanismsand pages 4-5): Canio Martinelli, Alfredo Ercoli, Silvana Parisi, Giuseppe Iatì, Stefano Pergolizzi, Luigi Alfano, Francesca Pentimalli, Michelino De Laurentiis, Antonio Giordano, and Salvatore Cortellino. Molecular mechanisms and clinical divergences in hpv-positive cervical vs. oropharyngeal cancers: a critical narrative review. BMC Medicine, Jul 2025. URL: https://doi.org/10.1186/s12916-025-04247-z, doi:10.1186/s12916-025-04247-z. This article has 12 citations and is from a domain leading peer-reviewed journal.

25. (wu2024unveilingthemultifaceted pages 2-3): Meng Wu, Hui Huang, Ying Tang, Xuze Ren, Xinrui Jiang, Man Tian, and Wei Li. Unveiling the multifaceted realm of human papillomavirus: a comprehensive exploration of biology, interactions, and advances in cancer management. Frontiers in Immunology, Aug 2024. URL: https://doi.org/10.3389/fimmu.2024.1430544, doi:10.3389/fimmu.2024.1430544. This article has 18 citations and is from a peer-reviewed journal.

26. (mlynarczykbonikowska2024hpvinfections—classificationpathogenesis pages 10-11): Beata Mlynarczyk-Bonikowska and Lidia Rudnicka. Hpv infections—classification, pathogenesis, and potential new therapies. International Journal of Molecular Sciences, 25:7616, Jul 2024. URL: https://doi.org/10.3390/ijms25147616, doi:10.3390/ijms25147616. This article has 109 citations.

27. (baba2025humanpapillomavirus pages 4-6): Sadaf Khursheed Baba, Shahad Shahdad Eissa Alblooshi, Reem Yaqoob, Shalini Behl, Mansour Al Saleem, Emad A. Rakha, Fayaz Malik, Mayank Singh, Muzafar A. Macha, Mohammed Kalim Akhtar, Walid A. Houry, Ajaz A. Bhat, Asma Al Menhali, Zhi-Ming Zheng, and Sameer Mirza. Human papilloma virus (hpv) mediated cancers: an insightful update. Journal of Translational Medicine, Apr 2025. URL: https://doi.org/10.1186/s12967-025-06470-x, doi:10.1186/s12967-025-06470-x. This article has 79 citations and is from a peer-reviewed journal.

28. (kao2026theroleof pages 3-5): Pei-Yu Kao, Jie-Hong Chen, and Kuo-Hu Chen. The role of hpv and hormone in cervical precancer and cancer: molecular pathophysiology and cell biology of disease and treatment. Oncology Research, 34(6):1-10, Jan 2026. URL: https://doi.org/10.32604/or.2026.078219, doi:10.32604/or.2026.078219. This article has 0 citations and is from a peer-reviewed journal.

29. (baba2025humanpapillomavirus pages 6-8): Sadaf Khursheed Baba, Shahad Shahdad Eissa Alblooshi, Reem Yaqoob, Shalini Behl, Mansour Al Saleem, Emad A. Rakha, Fayaz Malik, Mayank Singh, Muzafar A. Macha, Mohammed Kalim Akhtar, Walid A. Houry, Ajaz A. Bhat, Asma Al Menhali, Zhi-Ming Zheng, and Sameer Mirza. Human papilloma virus (hpv) mediated cancers: an insightful update. Journal of Translational Medicine, Apr 2025. URL: https://doi.org/10.1186/s12967-025-06470-x, doi:10.1186/s12967-025-06470-x. This article has 79 citations and is from a peer-reviewed journal.

30. (pavelescu2025molecularinsightsinto pages 8-10): Luciana Alexandra Pavelescu, Nicoleta Larisa Mititelu-Zafiu, Dana Elena Mindru, Radu Vladareanu, and Antoanela Curici. Molecular insights into hpv-driven cervical cancer: oncoproteins, immune evasion, and epigenetic modifications. Microorganisms, 13:1000, Apr 2025. URL: https://doi.org/10.3390/microorganisms13051000, doi:10.3390/microorganisms13051000. This article has 34 citations.

31. (martinelli2025molecularmechanismsand pages 5-7): Canio Martinelli, Alfredo Ercoli, Silvana Parisi, Giuseppe Iatì, Stefano Pergolizzi, Luigi Alfano, Francesca Pentimalli, Michelino De Laurentiis, Antonio Giordano, and Salvatore Cortellino. Molecular mechanisms and clinical divergences in hpv-positive cervical vs. oropharyngeal cancers: a critical narrative review. BMC Medicine, Jul 2025. URL: https://doi.org/10.1186/s12916-025-04247-z, doi:10.1186/s12916-025-04247-z. This article has 12 citations and is from a domain leading peer-reviewed journal.

32. (vallejoruiz2024molecularaspectsof pages 2-3): Verónica Vallejo-Ruiz, Lourdes Gutiérrez-Xicotencatl, Oscar Medina-Contreras, and Marcela Lizano. Molecular aspects of cervical cancer: a pathogenesis update. Frontiers in Oncology, Mar 2024. URL: https://doi.org/10.3389/fonc.2024.1356581, doi:10.3389/fonc.2024.1356581. This article has 51 citations.

33. (janiszewska2025hpvdrivenoncogenesis—muchmore pages 3-4): J. Janiszewska, ·. M. Kostrzewska‑Poczekaj, ·. M. Wierzbicka, J. C. Brenner, M. Giefing, Ewa Ziętkiewicz, and M. Kostrzewska-Poczekaj. Hpv-driven oncogenesis—much more than the e6 and e7 oncoproteins. Journal of Applied Genetics, 66:63-71, Jun 2025. URL: https://doi.org/10.1007/s13353-024-00883-y, doi:10.1007/s13353-024-00883-y. This article has 35 citations and is from a peer-reviewed journal.

34. (janiszewska2025hpvdrivenoncogenesis—muchmore pages 4-6): J. Janiszewska, ·. M. Kostrzewska‑Poczekaj, ·. M. Wierzbicka, J. C. Brenner, M. Giefing, Ewa Ziętkiewicz, and M. Kostrzewska-Poczekaj. Hpv-driven oncogenesis—much more than the e6 and e7 oncoproteins. Journal of Applied Genetics, 66:63-71, Jun 2025. URL: https://doi.org/10.1007/s13353-024-00883-y, doi:10.1007/s13353-024-00883-y. This article has 35 citations and is from a peer-reviewed journal.

35. (janiszewska2025hpvdrivenoncogenesis—muchmore pages 1-3): J. Janiszewska, ·. M. Kostrzewska‑Poczekaj, ·. M. Wierzbicka, J. C. Brenner, M. Giefing, Ewa Ziętkiewicz, and M. Kostrzewska-Poczekaj. Hpv-driven oncogenesis—much more than the e6 and e7 oncoproteins. Journal of Applied Genetics, 66:63-71, Jun 2025. URL: https://doi.org/10.1007/s13353-024-00883-y, doi:10.1007/s13353-024-00883-y. This article has 35 citations and is from a peer-reviewed journal.

36. (janiszewska2025hpvdrivenoncogenesis—muchmore pages 6-7): J. Janiszewska, ·. M. Kostrzewska‑Poczekaj, ·. M. Wierzbicka, J. C. Brenner, M. Giefing, Ewa Ziętkiewicz, and M. Kostrzewska-Poczekaj. Hpv-driven oncogenesis—much more than the e6 and e7 oncoproteins. Journal of Applied Genetics, 66:63-71, Jun 2025. URL: https://doi.org/10.1007/s13353-024-00883-y, doi:10.1007/s13353-024-00883-y. This article has 35 citations and is from a peer-reviewed journal.

37. (legaki2026hpvdrivencervicalcarcinogenesis pages 4-5): Evangelia Legaki, Theofania Lappa, Konstantina-Lida Prasoula, Zoi Kardasi, Emmanouil Kalampokas, Theodoros Kalampokas, Maria G. Roubelakis, Ekaterina Charvalos, and Maria Gazouli. Hpv-driven cervical carcinogenesis: genetic and epigenetic mechanisms and diagnostic approaches. International Journal of Molecular Sciences, 27:803, Jan 2026. URL: https://doi.org/10.3390/ijms27020803, doi:10.3390/ijms27020803. This article has 4 citations.

38. (martinelli2025molecularmechanismsand pages 17-18): Canio Martinelli, Alfredo Ercoli, Silvana Parisi, Giuseppe Iatì, Stefano Pergolizzi, Luigi Alfano, Francesca Pentimalli, Michelino De Laurentiis, Antonio Giordano, and Salvatore Cortellino. Molecular mechanisms and clinical divergences in hpv-positive cervical vs. oropharyngeal cancers: a critical narrative review. BMC Medicine, Jul 2025. URL: https://doi.org/10.1186/s12916-025-04247-z, doi:10.1186/s12916-025-04247-z. This article has 12 citations and is from a domain leading peer-reviewed journal.

39. (maghiar2024skinlesionscaused pages 6-7): Laura Maghiar, Mircea Sandor, Liliana Sachelarie, Ruxandra Bodog, and Anca Huniadi. Skin lesions caused by hpv—a comprehensive review. Biomedicines, 12:2098, Sep 2024. URL: https://doi.org/10.3390/biomedicines12092098, doi:10.3390/biomedicines12092098. This article has 28 citations.

40. (jain2023epidemiologymolecularpathogenesis pages 10-12): Meenu Jain, Dhananjay Yadav, Urmila Jarouliya, Vishal Chavda, Arun Kumar Yadav, Bipin Chaurasia, and Minseok Song. Epidemiology, molecular pathogenesis, immuno-pathogenesis, immune escape mechanisms and vaccine evaluation for hpv-associated carcinogenesis. Pathogens, 12:1380, Nov 2023. URL: https://doi.org/10.3390/pathogens12121380, doi:10.3390/pathogens12121380. This article has 80 citations.

41. (karaoglan2024unveilingtherole pages 3-4): Beliz Bahar Karaoğlan and Yüksel Ürün. Unveiling the role of human papillomavirus in urogenital carcinogenesis a comprehensive review. Viruses, 16:667, Apr 2024. URL: https://doi.org/10.3390/v16050667, doi:10.3390/v16050667. This article has 13 citations.

42. (branda2024humanpapillomavirus(hpv) pages 5-6): Francesco Branda, Grazia Pavia, Alessandra Ciccozzi, Angela Quirino, Nadia Marascio, Simona Gigliotti, Giovanni Matera, Chiara Romano, Chiara Locci, Ilenia Azzena, Noemi Pascale, Daria Sanna, Marco Casu, Giancarlo Ceccarelli, Massimo Ciccozzi, and Fabio Scarpa. Human papillomavirus (hpv) vaccination: progress, challenges, and future directions in global immunization strategies. Vaccines, 12:1293, Nov 2024. URL: https://doi.org/10.3390/vaccines12111293, doi:10.3390/vaccines12111293. This article has 42 citations.

43. (jain2023epidemiologymolecularpathogenesis pages 12-13): Meenu Jain, Dhananjay Yadav, Urmila Jarouliya, Vishal Chavda, Arun Kumar Yadav, Bipin Chaurasia, and Minseok Song. Epidemiology, molecular pathogenesis, immuno-pathogenesis, immune escape mechanisms and vaccine evaluation for hpv-associated carcinogenesis. Pathogens, 12:1380, Nov 2023. URL: https://doi.org/10.3390/pathogens12121380, doi:10.3390/pathogens12121380. This article has 80 citations.

44. (maghiar2024skinlesionscaused pages 7-9): Laura Maghiar, Mircea Sandor, Liliana Sachelarie, Ruxandra Bodog, and Anca Huniadi. Skin lesions caused by hpv—a comprehensive review. Biomedicines, 12:2098, Sep 2024. URL: https://doi.org/10.3390/biomedicines12092098, doi:10.3390/biomedicines12092098. This article has 28 citations.

45. (jain2023epidemiologymolecularpathogenesis pages 22-24): Meenu Jain, Dhananjay Yadav, Urmila Jarouliya, Vishal Chavda, Arun Kumar Yadav, Bipin Chaurasia, and Minseok Song. Epidemiology, molecular pathogenesis, immuno-pathogenesis, immune escape mechanisms and vaccine evaluation for hpv-associated carcinogenesis. Pathogens, 12:1380, Nov 2023. URL: https://doi.org/10.3390/pathogens12121380, doi:10.3390/pathogens12121380. This article has 80 citations.

46. (baba2025humanpapillomavirus pages 15-17): Sadaf Khursheed Baba, Shahad Shahdad Eissa Alblooshi, Reem Yaqoob, Shalini Behl, Mansour Al Saleem, Emad A. Rakha, Fayaz Malik, Mayank Singh, Muzafar A. Macha, Mohammed Kalim Akhtar, Walid A. Houry, Ajaz A. Bhat, Asma Al Menhali, Zhi-Ming Zheng, and Sameer Mirza. Human papilloma virus (hpv) mediated cancers: an insightful update. Journal of Translational Medicine, Apr 2025. URL: https://doi.org/10.1186/s12967-025-06470-x, doi:10.1186/s12967-025-06470-x. This article has 79 citations and is from a peer-reviewed journal.

47. (ashique2023hpvpathogenesisvarious pages 2-4): Sumel Ashique, Afzal Hussain, Neda Fatima, and Mohammad A. Altamimi. Hpv pathogenesis, various types of vaccines, safety concern, prophylactic and therapeutic applications to control cervical cancer, and future perspective. VirusDisease, 34:172-190, May 2023. URL: https://doi.org/10.1007/s13337-023-00824-z, doi:10.1007/s13337-023-00824-z. This article has 45 citations.

48. (bette2024cottontailrabbitpapillomavirus pages 3-5): Michael Bette and Robert Mandic. Cottontail rabbit papillomavirus (crpv) related animal models for head and neck cancer research: a comprehensive review of the literature. Viruses, 16:1722, Oct 2024. URL: https://doi.org/10.3390/v16111722, doi:10.3390/v16111722. This article has 0 citations.

49. (totain2023developmentofhpv16 pages 7-10): Emmanuelle Totain, Loïc Lindner, Nicolas Martin, Yolande Misseri, Alexandra Iché, Marie-Christine Birling, Tania Sorg, Yann Herault, Alain Bousquet-Melou, Pascale Bouillé, Christine Duthoit, Guillaume Pavlovic, and Severine Boullier. Development of hpv16 mouse and dog models for more accurate prediction of human vaccine efficacy. Laboratory Animal Research, Jun 2023. URL: https://doi.org/10.1186/s42826-023-00166-3, doi:10.1186/s42826-023-00166-3. This article has 2 citations.

50. (totain2023developmentofhpv16 pages 1-2): Emmanuelle Totain, Loïc Lindner, Nicolas Martin, Yolande Misseri, Alexandra Iché, Marie-Christine Birling, Tania Sorg, Yann Herault, Alain Bousquet-Melou, Pascale Bouillé, Christine Duthoit, Guillaume Pavlovic, and Severine Boullier. Development of hpv16 mouse and dog models for more accurate prediction of human vaccine efficacy. Laboratory Animal Research, Jun 2023. URL: https://doi.org/10.1186/s42826-023-00166-3, doi:10.1186/s42826-023-00166-3. This article has 2 citations.

51. (xiurong2024geneticallyengineeredmouse pages 9-10): Du Xiurong, Zhou Xin, Yang Neng, Deng Li, Wang Yanzhou, Ling Kaijian, and Liang Zhiqing. Genetically engineered mouse model of hpv16 e6-e7 with vaginal-cervical intraepithelial neoplasia and decreased immunity. May 2024. URL: https://doi.org/10.1016/j.heliyon.2024.e29881, doi:10.1016/j.heliyon.2024.e29881. This article has 1 citations.

52. (bette2024cottontailrabbitpapillomavirus pages 16-17): Michael Bette and Robert Mandic. Cottontail rabbit papillomavirus (crpv) related animal models for head and neck cancer research: a comprehensive review of the literature. Viruses, 16:1722, Oct 2024. URL: https://doi.org/10.3390/v16111722, doi:10.3390/v16111722. This article has 0 citations.

53. (bette2024cottontailrabbitpapillomavirus pages 19-20): Michael Bette and Robert Mandic. Cottontail rabbit papillomavirus (crpv) related animal models for head and neck cancer research: a comprehensive review of the literature. Viruses, 16:1722, Oct 2024. URL: https://doi.org/10.3390/v16111722, doi:10.3390/v16111722. This article has 0 citations.

## Artifacts

- [Edison artifact artifact-00](Human_Papillomavirus_Infection-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](Human_Papillomavirus_Infection-deep-research-falcon_artifacts/artifact-01.md)
- [Edison artifact artifact-02](Human_Papillomavirus_Infection-deep-research-falcon_artifacts/artifact-02.md)