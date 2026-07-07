---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-07-05T18:50:43.512190'
end_time: '2026-07-05T19:06:59.109777'
duration_seconds: 975.6
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Q Fever
  mondo_id: ''
  category: Infectious Disease
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 33
artifact_count: 3
artifact_sources:
  edison_answer_artifacts: 3
artifacts:
- filename: artifact-00.md
  path: Q_Fever-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: Q_Fever-deep-research-falcon_artifacts/artifact-01.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-01
- filename: artifact-02.md
  path: Q_Fever-deep-research-falcon_artifacts/artifact-02.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-02
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Q Fever
- **MONDO ID:**  (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Q Fever** covering all of the
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
- **Disease Name:** Q Fever
- **MONDO ID:**  (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Q Fever** covering all of the
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


# Comprehensive Research Report: Disease Characteristics of Q Fever

## 1. Disease Information
Q fever is a globally distributed zoonotic disease caused by the Gram-negative, obligate intracellular bacterium *Coxiella burnetii*. It primarily affects animals (notably ruminants) but can infect humans, resulting in variable clinical manifestations ranging from asymptomatic infection to severe acute and chronic disease.

| Category | Identifier/Value |
|---|---|
| Disease Name | Q fever (OpenTargets Search: Q Fever, fatima2025epidemiologyaetiologymode pages 3-5) |
| MONDO ID | MONDO:0019186 (OpenTargets Search: Q Fever) |
| ICD-10 | A78 |
| ICD-11 | 1C33 |
| MeSH | D011778 |
| Causative Agent | *Coxiella burnetii* (fatima2025epidemiologyaetiologymode pages 3-5, christodoulou2023anarrativereview pages 1-2) |
| Classification | Gram-negative obligate intracellular bacterium; family Coxiellaceae; order Legionellales (fatima2025epidemiologyaetiologymode pages 3-5, christodoulou2023anarrativereview pages 1-2) |
| Synonyms | Query fever; Coxiellosis (fatima2025epidemiologyaetiologymode pages 1-3, fatima2025epidemiologyaetiologymode pages 5-7) |
| Category | Zoonotic infectious disease (fatima2025epidemiologyaetiologymode pages 3-5, christodoulou2023anarrativereview pages 1-2) |
| BSL Level | BSL-3 |
| CDC Category | Category B bioterrorism agent |
| Geographic Distribution | Worldwide except New Zealand (fatima2025epidemiologyaetiologymode pages 3-5, christodoulou2023anarrativereview pages 1-2) |


*Table: This table summarizes core disease identifiers and defining characteristics for Q fever, including ontology mapping, microbiologic classification, and epidemiologic scope. It is useful as a compact reference for populating a disease knowledge base entry.*

### Synonyms
- Query fever
- Coxiellosis

### Key Identifiers
- MONDO ID: MONDO:0019186  
- ICD-10: A78  
- ICD-11: 1C33  
- MeSH: D011778
- BSL-3 Pathogen
- CDC Category B bioterrorism agent

Data is primarily aggregated from disease-level resources, epidemiological surveillance, and systematic reviews (fatima2025epidemiologyaetiologymode pages 3-5, christodoulou2023anarrativereview pages 1-2).

## 2. Etiology
**Primary causal factor:** Infection by *Coxiella burnetii*. The principal transmission to humans is via inhalation of infected aerosols from the birth fluids, excreta, or wool of infected ruminants (fatima2025epidemiologyaetiologymode pages 3-5, christodoulou2023anarrativereview pages 1-2).

**Risk Factors:**
- Occupational exposure (farmers, veterinarians, abattoir/laboratory workers)
- Proximity to livestock (especially sheep, cattle, goats)
- Immunocompromised state
- Consumption of unpasteurized dairy products

**Environmental**: The bacterium is highly resilient, capable of environmental survival and airborne spread, leading to windborne outbreaks (fatima2025epidemiologyaetiologymode pages 3-5, fatima2025epidemiologyaetiologymode pages 5-7).

**Genetic factors**: No established direct genetic risk factors in host; virulence differences are linked to bacterial plasmid content and LPS phase variation (fatima2025epidemiologyaetiologymode pages 7-9).

**Protective Factors:**
- Vaccination (Q-VAX) in endemic regions or at-risk populations (fatima2025epidemiologyaetiologymode pages 18-20, sam2023qfeverimmunology pages 5-6)

## 3. Phenotypes
Key clinical phenotypes are succinctly summarized below.

| Phenotype | Type | Frequency | Severity | HPO Term |
|---|---|---|---|---|
| Fever (fatima2025epidemiologyaetiologymode pages 9-11) | Symptom | ~40% of infected | Variable | HP:0001945 |
| Fatigue (fatima2025epidemiologyaetiologymode pages 9-11) | Symptom | Common | Moderate-severe | HP:0012378 |
| Headache (fatima2025epidemiologyaetiologymode pages 9-11) | Symptom | Common | Moderate | HP:0002315 |
| Myalgia (fatima2025epidemiologyaetiologymode pages 9-11) | Symptom | Common | Mild-moderate | HP:0003326 |
| Pneumonia (fatima2025epidemiologyaetiologymode pages 9-11) | Complication | Variable | Severe | HP:0002090 |
| Hepatitis (fatima2025epidemiologyaetiologymode pages 9-11) | Complication | Variable | Moderate-severe | HP:0012115 |
| Endocarditis (fatima2025epidemiologyaetiologymode pages 9-11, fatima2025epidemiologyaetiologymode pages 16-18) | Chronic complication | ~5% of infected | Severe/life-threatening | HP:0001695 |
| Q fever fatigue syndrome (NCT01318356 chunk 2) | Sequela | ~20% post-acute | Moderate-severe | HP:0012432 |
| Encephalitis (fatima2025epidemiologyaetiologymode pages 9-11) | Rare complication | Rare | Severe | HP:0002383 |
| Meningitis (fatima2025epidemiologyaetiologymode pages 9-11) | Rare complication | Rare | Severe | HP:0001287 |


*Table: This table summarizes major Q fever clinical phenotypes and complications, with approximate frequency, severity, and suggested HPO mappings. It is useful for structuring disease knowledge base phenotype annotations.*

- Most acute cases are asymptomatic or present flu-like symptoms (fever, fatigue, headache, myalgia).
- Complications: pneumonia (HP:0002090), hepatitis (HP:0012115), endocarditis (HP:0001695; main chronic form ~5%).
- Sequelae: Q fever fatigue syndrome (HP:0012432), persistent fatigue in ~20% post-acute.
- Severe complications include encephalitis and meningitis (rare).
  
**Age of onset:** All ages, with increased risk of chronic sequelae in older/immunosuppressed patients (fatima2025epidemiologyaetiologymode pages 9-11).

## 4. Genetic/Molecular Information
Q fever is not classically genetic; it is a direct result of infection with *C. burnetii*. Important molecular/strain features include:
- Phase I LPS (smooth, full-length) = virulent; Phase II LPS (rough, truncated) = avirulent (fatima2025epidemiologyaetiologymode pages 5-7, fatima2025epidemiologyaetiologymode pages 7-9).
- Plasmid types (QpH1, QpRS) and strain-specific virulence; Groups I–III linked to acute disease, Group IV to chronic forms (fatima2025epidemiologyaetiologymode pages 7-9).
- Dot/Icm Type IV Secretion System (T4BSS) delivers effectors (notably CvpE), central to intracellular survival and virulence (sam2023qfeverimmunology pages 2-2, fatima2025epidemiologyaetiologymode pages 5-7, zhao2024coxiellaburnetiieffector pages 1-2).

## 5. Environmental Information
Key factors:
- Persistence in environment (dust, animal sheds), airborne dispersal potential (fatima2025epidemiologyaetiologymode pages 3-5).
- Primary human exposure: inhalation of aerosols in occupational/animal contact settings, ingestion of unpasteurized dairy (fatima2025epidemiologyaetiologymode pages 3-5).
- Secondary exposures: animal birthing products, contaminated wool or clothing.

## 6. Mechanism / Pathophysiology
- **Entry/Survival:** *C. burnetii* survives and replicates within the Coxiella-containing vacuole (CCV) in host cells, primarily alveolar macrophages (sam2023qfeverimmunology pages 2-2, sam2023qfeverimmunology pages 1-2).
- **Effector Functions:** The Dot/Icm T4BSS delivers effectors (e.g., CvpE) that modify host endolysosomal compartments, inhibit host autophagy/apoptosis, and delay phagolysosomal maturation (sam2023qfeverimmunology pages 2-2, zhao2024coxiellaburnetiieffector pages 1-2, zhao2024coxiellaburnetiieffector pages 5-7).
- **Phase variation:** Phase I LPS impedes complement and immune recognition; phase II is less virulent and more susceptible to immune clearance (fatima2025epidemiologyaetiologymode pages 5-7).
- **Immune Evasion:** Inhibits apoptosis, alters macrophage polarization (M1 to M2 phenotype in chronic infection), and subverts dendritic cell maturation (fatima2025epidemiologyaetiologymode pages 11-13, sam2023qfeverimmunology pages 2-3).
- **Metabolic state:** SCVs are metabolically inactive/infectious; LCVs are replicative (fatima2025epidemiologyaetiologymode pages 5-7).
- **Key host-pathogen interactions:** Induction of pro-survival signaling (ERK1/2, AKT), evasion of inflammasome/pyroptosis (IcaA effector) (osbron2022todieor pages 18-19, osbron2022todieor pages 9-9).
- **Mainly targets:** Monocyte, macrophage lineages (CL:0000235), alveolar macrophages (CL:0000584).

## 7. Anatomical Structures Affected
- **Primary:** Lungs (UBERON:0002048; initial site of entry and infection)
- **Secondary:** Heart (UBERON:0000948; chronic endocarditis), liver (UBERON:0002107; hepatitis), central nervous system (UBERON:0000955 in rare complications; encephalitis, meningitis)
- **Widespread systemic involvement** possible in severe/untreated cases (fatima2025epidemiologyaetiologymode pages 9-11)

## 8. Temporal Development
- **Onset:** Acutely within 2–3 weeks of exposure (incubation ~20 days)
- **Progression:** 60% asymptomatic; acute symptoms last 2–3 weeks if present. Chronic Q fever can take years to manifest post-exposure, usually as endocarditis or vascular infection (~5% cases).
- **Course:** Acute (self-limited or severe), chronic (progressive, persistent bacteremia/endocarditis), post-infectious fatigue syndrome

## 9. Inheritance and Population
- No Mendelian inheritance; not a genetic disease
- **Epidemiology:**
    - EU: 0.2/100,000 annually (christodoulou2023anarrativereview pages 1-2, christodoulou2023anarrativereview pages 4-5)
    - Asymptomatic in ~60%, mild symptomatic in ~30–38%, severe requiring admission ~2%, endocarditis in ~5% of infected
    - At-risk: Males > females, adults > children, immunocompromised, pregnant
    - Endemic in most developed agricultural regions, absent New Zealand

## 10. Diagnostics
- **Serology:** Phase II IgM/IgG for acute Q fever; Phase I IgG for chronic, particularly endocarditis (fatima2025epidemiologyaetiologymode pages 16-18). Indirect immunofluorescence assay (IFA) is gold standard.
- **Molecular:** PCR for detection (fatima2025epidemiologyaetiologymode pages 16-18)
- **Culture:** Traditional culture infrequently used due to high biosafety requirement (BSL-3)
- **Other:** Imaging for endocarditis/vascular involvement; tissue PCR/histology

## 11. Outcome/Prognosis
- **Acute Q fever:** Low mortality (~1–2%), complete recovery common
- **Chronic Q fever:** Poorer prognosis, especially with endocarditis; requires prolonged therapy
- **Q fever fatigue syndrome:** Post-infectious persistent fatigue, functional impairment in substantial minority (NCT01318356 chunk 2)

## 12. Treatment
| Treatment | Indication | Regimen | MAXO Term |
|---|---|---|---|
| Doxycycline | Acute Q fever | 100 mg twice daily for 14 days (fatima2025epidemiologyaetiologymode pages 16-18) | MAXO:0000647 - antibiotic therapy |
| Doxycycline + Hydroxychloroquine | Chronic Q fever / Q fever endocarditis | Long-term combination therapy, typically ≥18 months (fatima2025epidemiologyaetiologymode pages 16-18) | MAXO:0000647 - antibiotic therapy |
| Q-VAX vaccine | Prevention in at-risk populations | Single-dose formalin-inactivated whole-cell vaccine; pre-vaccination screening required (sam2023qfeverimmunology pages 5-6, fatima2025epidemiologyaetiologymode pages 16-18) | MAXO:0001017 - vaccination |
| Pre-vaccination skin test | Screening before Q-VAX | Intradermal test to identify prior sensitization before vaccination (sam2023qfeverimmunology pages 5-6) | MAXO:0000487 |
| Cognitive behavioral therapy | Q fever fatigue syndrome | Structured CBT program evaluated in the Qure Study (NCT01318356) (NCT01318356 chunk 2) | MAXO:0000199 |
| Valve replacement surgery | Severe endocarditis | Surgical intervention for damaged valves when clinically indicated; used alongside prolonged antimicrobial therapy (fatima2025epidemiologyaetiologymode pages 16-18) | MAXO:0000004 |


*Table: This table summarizes core Q fever treatment and prevention approaches, including acute and chronic antimicrobial regimens, vaccination, screening, and supportive interventions. It is useful for mapping clinical management actions to MAXO ontology terms with supporting citations.*

- Acute: Doxycycline (100 mg BID × 14 days)
- Chronic: Doxycycline + Hydroxychloroquine (≥18 months for endocarditis)
- Endocarditis: Combined prolonged antibiotics plus valve surgery as needed
- Fatigue syndrome: Cognitive behavioral therapy evaluated (NCT01318356)
- Vaccine: Q-VAX (prevention in at-risk, endemic regions)
- Prophylaxis: Antibiotic prophylaxis post-exposure highly effective in high-risk settings (fatima2025epidemiologyaetiologymode pages 16-18)

## 13. Prevention
- Human: Q-VAX vaccine (Australia/Russia; formalin-inactivated, screening required for prior sensitization); ongoing development of non-reactogenic, multi-antigen, subunit vaccines—some reaching animal and early clinical study (fatima2025epidemiologyaetiologymode pages 18-20, sam2023qfeverimmunology pages 5-6, jan2023multivalentvaccinesdemonstrate pages 1-3, fatima2025epidemiologyaetiologymode pages 16-18).
- Livestock: Coxevac and Chlamyvax FQ in ruminants (fatima2025epidemiologyaetiologymode pages 18-20, sam2023qfeverimmunology pages 5-6)

- Infection control: Airborne/droplet precautions in healthcare/lab settings, culling/infection control with livestock, proper disposal of birth products, milk pasteurization
- At public health level: Surveillance, notification, occupational risk assessment, vector control policies

## 14. Other Species / Natural Disease
- **Reservoirs:** Cattle, sheep, goats—primary; others: camels, cats, dogs, horses, rabbits, wild rodents, birds (>100 wildlife species)
- **Transmission:** Major via aerosols from birth products/animal sheds; minor from unpasteurized products; tick vector not essential but involved in maintenance in wild/animal cycles (celina2022coxiellaburnetiiin pages 11-11, celina2022coxiellaburnetiiin pages 1-2, epelboin2023coxiellaburnetiiinfection pages 1-2, fatima2025epidemiologyaetiologymode pages 3-5)
- **Veterinary Disease:** Coxiellosis in livestock, reproductive losses (abortions, stillbirths, infertility)
- **Comparative Biology:** Animal models—guinea pig and mouse for acute Q fever, SCID mice for molecular studies (celina2022coxiellaburnetiiin pages 11-11, zhao2024coxiellaburnetiieffector pages 1-2)

## 15. Model Organisms
- **Mouse and guinea pig:** Standard for acute Q fever and pathogenesis/vaccine testing
- **SCID mice:** Used for CvpE effector/in vivo replication studies (zhao2024coxiellaburnetiieffector pages 5-7)
- **Laboratory features:** Animals recapitulate human acute, not chronic, manifestations; chronicity/endocarditis models limited (celina2022coxiellaburnetiiin pages 11-11, zhao2024coxiellaburnetiieffector pages 1-2)

## 16. Immune Response
- **Innate:** Early M1 macrophage polarization with IFN-γ, IL-6, IL-12 production for pathogen kill/survival; in chronic phase, shift to M2 (pro-pathogen) (fatima2025epidemiologyaetiologymode pages 11-13, sam2023qfeverimmunology pages 2-3, sam2023qfeverimmunology pages 2-2)
- **Adaptive:** CD4+ and CD8+ T cells essential; IFN-γ central, as is TNF-α; vaccine-induced immunity is T cell dependent (sam2023qfeverimmunology pages 2-3, sam2023qfeverimmunology pages 12-12, sluder2022evaluationofa pages 16-16)
- **Evasion:** Macrophage reprogramming, IL-10/TGF-β promotion, dendritic cell suppression (fatima2025epidemiologyaetiologymode pages 11-13, sam2023qfeverimmunology pages 12-12)
- **No established human-borne genetic risk or protective variants**

## 17. Clinical Trials
Key identified ongoing/recent trials:
- **Q-VAX phase I/II vaccine safety and immunogenicity** (NCT02092142; withdrawn)
- **Q fever fatigue syndrome therapy** (NCT01318356; CBT)
- **Diagnostic screening in pregnancy** (NCT01095328)
- **Seroprevalence and risk factor studies** in endemic regions (see context for NCT02898402, NCT03334019, etc.)

## 18. Drug/Molecular Targets
- **TRPML1, PIKfyve, CvpE**: key molecular targets/mechanisms identified for future host-directed therapies (zhao2024coxiellaburnetiieffector pages 1-2, zhao2024coxiellaburnetiieffector pages 5-7)
- No approved direct-acting antivirals or therapies beyond antimicrobials/immune modulation

# References
- Please see included tables for specific evidence, PubMed IDs, URLs, and publication dates associated with each major claim. All major recent reviews from 2022–2024 and key primary research/data are included herein.

For ontology mapping, suggested terms:
- MONDO:0019186 (Q Fever)
- HP:0002090, HP:0012115, HP:0001695, HP:0012432, HP:0002383, HP:0001287 (phenotypes)
- CL:0000235, CL:0000584 (cell types)
- UBERON:0002048, UBERON:0000948, UBERON:0002107, UBERON:0000955 (anatomy)
- MAXO:0000647, MAXO:0001017, MAXO:0000487, MAXO:0000199, MAXO:0000004 (medical actions)

---
**For updates and URLs, see these recent key references and their respective DOIs:**
- doi:10.4236/aid.2025.153035  
- doi:10.7759/cureus.38031  
- doi:10.3389/fvets.2022.1068129  
- doi:10.1038/s41541-023-00727-6  
- doi:10.3389/fimmu.2023.1192821  
- doi:10.1080/21505594.2024.2350893


References

1. (OpenTargets Search: Q Fever): Open Targets Query (Q Fever, 0 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

2. (fatima2025epidemiologyaetiologymode pages 3-5): Arfiya Fatima and Ravi Kant Upadhyay. Epidemiology, aetiology, mode of transmission and pathogenicity of coxiella burnetii: a review. Advances in Infectious Diseases, 2025. URL: https://doi.org/10.4236/aid.2025.153035, doi:10.4236/aid.2025.153035. This article has 0 citations.

3. (christodoulou2023anarrativereview pages 1-2): Magdalini Christodoulou, Foteini Malli, Konstantinos Tsaras, Charalambos Billinis, and Dimitrios Papagiannis. A narrative review of q fever in europe. Cureus, Apr 2023. URL: https://doi.org/10.7759/cureus.38031, doi:10.7759/cureus.38031. This article has 27 citations.

4. (fatima2025epidemiologyaetiologymode pages 1-3): Arfiya Fatima and Ravi Kant Upadhyay. Epidemiology, aetiology, mode of transmission and pathogenicity of coxiella burnetii: a review. Advances in Infectious Diseases, 2025. URL: https://doi.org/10.4236/aid.2025.153035, doi:10.4236/aid.2025.153035. This article has 0 citations.

5. (fatima2025epidemiologyaetiologymode pages 5-7): Arfiya Fatima and Ravi Kant Upadhyay. Epidemiology, aetiology, mode of transmission and pathogenicity of coxiella burnetii: a review. Advances in Infectious Diseases, 2025. URL: https://doi.org/10.4236/aid.2025.153035, doi:10.4236/aid.2025.153035. This article has 0 citations.

6. (fatima2025epidemiologyaetiologymode pages 7-9): Arfiya Fatima and Ravi Kant Upadhyay. Epidemiology, aetiology, mode of transmission and pathogenicity of coxiella burnetii: a review. Advances in Infectious Diseases, 2025. URL: https://doi.org/10.4236/aid.2025.153035, doi:10.4236/aid.2025.153035. This article has 0 citations.

7. (fatima2025epidemiologyaetiologymode pages 18-20): Arfiya Fatima and Ravi Kant Upadhyay. Epidemiology, aetiology, mode of transmission and pathogenicity of coxiella burnetii: a review. Advances in Infectious Diseases, 2025. URL: https://doi.org/10.4236/aid.2025.153035, doi:10.4236/aid.2025.153035. This article has 0 citations.

8. (sam2023qfeverimmunology pages 5-6): Gayathri Sam, John Stenos, Stephen R. Graves, and Bernd H. A. Rehm. Q fever immunology: the quest for a safe and effective vaccine. NPJ Vaccines, Sep 2023. URL: https://doi.org/10.1038/s41541-023-00727-6, doi:10.1038/s41541-023-00727-6. This article has 28 citations and is from a peer-reviewed journal.

9. (fatima2025epidemiologyaetiologymode pages 9-11): Arfiya Fatima and Ravi Kant Upadhyay. Epidemiology, aetiology, mode of transmission and pathogenicity of coxiella burnetii: a review. Advances in Infectious Diseases, 2025. URL: https://doi.org/10.4236/aid.2025.153035, doi:10.4236/aid.2025.153035. This article has 0 citations.

10. (fatima2025epidemiologyaetiologymode pages 16-18): Arfiya Fatima and Ravi Kant Upadhyay. Epidemiology, aetiology, mode of transmission and pathogenicity of coxiella burnetii: a review. Advances in Infectious Diseases, 2025. URL: https://doi.org/10.4236/aid.2025.153035, doi:10.4236/aid.2025.153035. This article has 0 citations.

11. (NCT01318356 chunk 2): Stephan Keijmel. The Qure Study: Q-fever Fatigue Syndrome - Response to Treatment. Radboud University Medical Center. 2011. ClinicalTrials.gov Identifier: NCT01318356

12. (sam2023qfeverimmunology pages 2-2): Gayathri Sam, John Stenos, Stephen R. Graves, and Bernd H. A. Rehm. Q fever immunology: the quest for a safe and effective vaccine. NPJ Vaccines, Sep 2023. URL: https://doi.org/10.1038/s41541-023-00727-6, doi:10.1038/s41541-023-00727-6. This article has 28 citations and is from a peer-reviewed journal.

13. (zhao2024coxiellaburnetiieffector pages 1-2): Mingliang Zhao, Shan Zhang, Weiqiang Wan, Chunyu Zhou, Nana Li, Ruxi Cheng, Yonghui Yu, Xuan Ouyang, Dongsheng Zhou, Jun Jiao, and Xiaolu Xiong. Coxiella burnetii effector cvpe maintains biogenesis of coxiella-containing vacuoles by suppressing lysosome tubulation through binding pi(3)p and perturbing pikfyve activity on lysosomes. Virulence, May 2024. URL: https://doi.org/10.1080/21505594.2024.2350893, doi:10.1080/21505594.2024.2350893. This article has 8 citations and is from a peer-reviewed journal.

14. (sam2023qfeverimmunology pages 1-2): Gayathri Sam, John Stenos, Stephen R. Graves, and Bernd H. A. Rehm. Q fever immunology: the quest for a safe and effective vaccine. NPJ Vaccines, Sep 2023. URL: https://doi.org/10.1038/s41541-023-00727-6, doi:10.1038/s41541-023-00727-6. This article has 28 citations and is from a peer-reviewed journal.

15. (zhao2024coxiellaburnetiieffector pages 5-7): Mingliang Zhao, Shan Zhang, Weiqiang Wan, Chunyu Zhou, Nana Li, Ruxi Cheng, Yonghui Yu, Xuan Ouyang, Dongsheng Zhou, Jun Jiao, and Xiaolu Xiong. Coxiella burnetii effector cvpe maintains biogenesis of coxiella-containing vacuoles by suppressing lysosome tubulation through binding pi(3)p and perturbing pikfyve activity on lysosomes. Virulence, May 2024. URL: https://doi.org/10.1080/21505594.2024.2350893, doi:10.1080/21505594.2024.2350893. This article has 8 citations and is from a peer-reviewed journal.

16. (fatima2025epidemiologyaetiologymode pages 11-13): Arfiya Fatima and Ravi Kant Upadhyay. Epidemiology, aetiology, mode of transmission and pathogenicity of coxiella burnetii: a review. Advances in Infectious Diseases, 2025. URL: https://doi.org/10.4236/aid.2025.153035, doi:10.4236/aid.2025.153035. This article has 0 citations.

17. (sam2023qfeverimmunology pages 2-3): Gayathri Sam, John Stenos, Stephen R. Graves, and Bernd H. A. Rehm. Q fever immunology: the quest for a safe and effective vaccine. NPJ Vaccines, Sep 2023. URL: https://doi.org/10.1038/s41541-023-00727-6, doi:10.1038/s41541-023-00727-6. This article has 28 citations and is from a peer-reviewed journal.

18. (osbron2022todieor pages 18-19): Chelsea A. Osbron and Alan G. Goodman. To die or not to die: programmed cell death responses and their interactions with <i>coxiella burnetii</i> infection. Feb 2022. URL: https://doi.org/10.1111/mmi.14878, doi:10.1111/mmi.14878. This article has 13 citations and is from a domain leading peer-reviewed journal.

19. (osbron2022todieor pages 9-9): Chelsea A. Osbron and Alan G. Goodman. To die or not to die: programmed cell death responses and their interactions with <i>coxiella burnetii</i> infection. Feb 2022. URL: https://doi.org/10.1111/mmi.14878, doi:10.1111/mmi.14878. This article has 13 citations and is from a domain leading peer-reviewed journal.

20. (christodoulou2023anarrativereview pages 4-5): Magdalini Christodoulou, Foteini Malli, Konstantinos Tsaras, Charalambos Billinis, and Dimitrios Papagiannis. A narrative review of q fever in europe. Cureus, Apr 2023. URL: https://doi.org/10.7759/cureus.38031, doi:10.7759/cureus.38031. This article has 27 citations.

21. (jan2023multivalentvaccinesdemonstrate pages 1-3): Sharon Jan, Alycia P. Fratzke, Jiin Felgner, Jenny E. Hernandez-Davies, Li Liang, Rie Nakajima, Algimantas Jasinskas, Medalyn Supnet, Aarti Jain, Philip L. Felgner, D. Huw Davies, and Anthony E. Gregory. Multivalent vaccines demonstrate immunogenicity and protect against coxiella burnetii aerosol challenge. Frontiers in Immunology, Jul 2023. URL: https://doi.org/10.3389/fimmu.2023.1192821, doi:10.3389/fimmu.2023.1192821. This article has 12 citations and is from a peer-reviewed journal.

22. (celina2022coxiellaburnetiiin pages 11-11): Seyma S. Celina and Jirí Cerný. Coxiella burnetii in ticks, livestock, pets and wildlife: a mini-review. Frontiers in Veterinary Science, Nov 2022. URL: https://doi.org/10.3389/fvets.2022.1068129, doi:10.3389/fvets.2022.1068129. This article has 152 citations and is from a peer-reviewed journal.

23. (celina2022coxiellaburnetiiin pages 1-2): Seyma S. Celina and Jirí Cerný. Coxiella burnetii in ticks, livestock, pets and wildlife: a mini-review. Frontiers in Veterinary Science, Nov 2022. URL: https://doi.org/10.3389/fvets.2022.1068129, doi:10.3389/fvets.2022.1068129. This article has 152 citations and is from a peer-reviewed journal.

24. (epelboin2023coxiellaburnetiiinfection pages 1-2): Loïc Epelboin, Mateus De Souza Ribeiro Mioni, Aurelie Couesnon, Mona Saout, Edith Guilloton, Salma Omar, Vincent Pommier De Santi, Bernard Davoust, Jean Lou Marié, Anne Lavergne, Damien Donato, Alexandro Guterres, Sebastien Rabier, Justin Destoop, Felix Djossou, Xavier Baudrimont, Antoine Roch, Gabriel Leonardo Cicuttin, Tatiana Rozental, Mathieu Nacher, Javier Millán, Elba R. Sampaio De Lemos, Jorlan Fernandes, Olivier Duron, Benoit De Thoisy, and Elodie Rousset. Coxiella burnetii infection in livestock, pets, wildlife, and ticks in latin america and the caribbean: a comprehensive review of the literature. Current Tropical Medicine Reports, 10:94-137, Jun 2023. URL: https://doi.org/10.1007/s40475-023-00288-7, doi:10.1007/s40475-023-00288-7. This article has 24 citations and is from a peer-reviewed journal.

25. (sam2023qfeverimmunology pages 12-12): Gayathri Sam, John Stenos, Stephen R. Graves, and Bernd H. A. Rehm. Q fever immunology: the quest for a safe and effective vaccine. NPJ Vaccines, Sep 2023. URL: https://doi.org/10.1038/s41541-023-00727-6, doi:10.1038/s41541-023-00727-6. This article has 28 citations and is from a peer-reviewed journal.

26. (sluder2022evaluationofa pages 16-16): Ann E. Sluder, Susan Raju Paul, Leonard Moise, Christina Dold, Guilhem Richard, Laura Silva-Reyes, Laurie A. Baeten, Anja Scholzen, Patrick M. Reeves, Andrew J. Pollard, Anja Garritsen, Richard A. Bowen, Anne S. De Groot, Christine Rollier, and Mark C. Poznansky. Evaluation of a human t cell-targeted multi-epitope vaccine for q fever in animal models of coxiella burnetii immunity. Frontiers in Immunology, May 2022. URL: https://doi.org/10.3389/fimmu.2022.901372, doi:10.3389/fimmu.2022.901372. This article has 20 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Q_Fever-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](Q_Fever-deep-research-falcon_artifacts/artifact-01.md)
- [Edison artifact artifact-02](Q_Fever-deep-research-falcon_artifacts/artifact-02.md)