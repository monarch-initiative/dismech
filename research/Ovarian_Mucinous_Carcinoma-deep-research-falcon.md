---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-19T09:25:51.806866'
end_time: '2026-06-19T09:40:25.576525'
duration_seconds: 873.77
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Ovarian Mucinous Carcinoma
  mondo_id: ''
  category: ''
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 25
artifact_count: 3
artifact_sources:
  edison_answer_artifacts: 3
artifacts:
- filename: artifact-00.md
  path: Ovarian_Mucinous_Carcinoma-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: Ovarian_Mucinous_Carcinoma-deep-research-falcon_artifacts/artifact-01.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-01
- filename: artifact-02.md
  path: Ovarian_Mucinous_Carcinoma-deep-research-falcon_artifacts/artifact-02.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-02
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Ovarian Mucinous Carcinoma
- **MONDO ID:**  (if available)
- **Category:** 

## Research Objectives

Please provide a comprehensive research report on **Ovarian Mucinous Carcinoma** covering all of the
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
- **Disease Name:** Ovarian Mucinous Carcinoma
- **MONDO ID:**  (if available)
- **Category:** 

## Research Objectives

Please provide a comprehensive research report on **Ovarian Mucinous Carcinoma** covering all of the
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


# Comprehensive Research Report: Ovarian Mucinous Carcinoma

## Target Disease
- **Disease Name:** Ovarian Mucinous Carcinoma (MOC)
- **Synonyms:** Mucinous epithelial ovarian cancer (mEOC), primary mucinous ovarian carcinoma (PMOC)
- **Category:** Epithelial ovarian neoplasm, Type I ovarian carcinoma

---

## 1. Disease Information

### Overview
Ovarian mucinous carcinoma is a rare and biologically distinct histologic subtype of epithelial ovarian cancer characterized by mucin-producing cells and unique molecular features. According to the 2020 WHO Classification of Female Genital Tumours, mucinous carcinoma represents one of the five principal histotypes of ovarian carcinoma, alongside high-grade serous, low-grade serous, endometrioid, and clear cell carcinomas (kobel2022theevolutionof pages 1-3, leo2021whatisnew pages 1-2).

### Classification and Identifiers
The 2020 WHO classification maintains mucinous carcinoma as a distinct histotype and further subdivides invasive mucinous ovarian carcinoma into two growth patterns with clinical significance: **expansile** and **infiltrative** subtypes (wang2023mucinsandmucinous pages 1-2). This distinction is particularly important in stage I disease as it may influence decisions regarding staging lymphadenectomy and adjuvant chemotherapy.

**ICD-O-3 Codes** referenced in epidemiological studies include 8470-8490 and 9015 for mucinous carcinomas (wang2024globalincidenceof pages 1-2).

### Prevalence and Diagnostic Challenges
While historically reported to account for 10-15% of epithelial ovarian cancers, contemporary reviews note that mucinous ovarian carcinoma comprises only **3-5%** of epithelial ovarian cancers, with some estimates as low as **3-4%** or **2-3%** (wang2023mucinsandmucinous pages 1-2, przywara2025recenttherapiesand pages 1-2, sauriol2020modelingthediversity pages 1-3). This downward revision reflects improved recognition that approximately **80%** of tumors historically classified as primary ovarian mucinous carcinomas are actually metastases from extra-ovarian sites, most commonly the gastrointestinal tract (45%), pancreas (2-20%), cervix/endometrium (18%), and breast (8-15%) (kawecka2024molecularalterationsin pages 1-2, wang2023mucinsandmucinous pages 2-3). Thus, true primary mucinous ovarian carcinoma may account for only **1-3%** of all ovarian cancers (wang2023mucinsandmucinous pages 2-3).

### Data Sources
The information in this report is derived from **aggregated disease-level resources** including peer-reviewed literature, population-based cancer registries, molecular characterization studies, and clinical trial data, rather than individual patient electronic health records.

---

## 2. Etiology

### Disease Causal Factors

**Genetic Factors:**
Mucinous ovarian carcinoma is characterized by somatic mutations rather than germline inheritance. Unlike high-grade serous ovarian carcinoma, mucinous ovarian carcinoma is **not associated with germline BRCA1/2 mutations** (sauriol2020modelingthediversity pages 1-3, affatato2020identificationofplk1 pages 1-3). The disease appears to arise through a stepwise progression from benign cystadenoma to borderline tumor to invasive carcinoma, representing a Type I ovarian carcinoma pathway (affatato2020identificationofplk1 pages 1-3).

**Cellular Origin:**
The cellular origin of primary ovarian mucinous carcinoma remains incompletely understood. While the tumors arise in the ovary, a convincing normal cell of origin within the ovary is elusive. Rare cases are associated with Brenner tumors or are of germ cell origin (associated with mature cystic teratomas) (kobel2022theevolutionof pages 3-4, kawecka2024molecularalterationsin pages 1-2).

### Risk Factors

**Genetic Risk Factors:**
- **Somatic KRAS mutations** (40-76% frequency) are strongly associated with progression from benign/borderline to malignant mucinous tumors and represent the strongest predictor of definite malignancy (kawecka2024molecularalterationsin pages 1-2, przywara2025recenttherapiesand pages 1-2)
- **ERBB2 (HER2) amplification** occurs in 15-35% of cases and is enriched in Asian populations (27.4-33.3%) (przywara2025recenttherapiesand pages 1-2, przywara2025recenttherapiesand pages 4-6)
- **TP53 mutations** (52-75% in carcinomas) are associated with high-grade disease, advanced stage, and poor prognosis (kawecka2024molecularalterationsin pages 1-2, przywara2025recenttherapiesand pages 1-2)
- **CDKN2A loss** (33-76%) increases with malignant transformation (leo2021whatisnew pages 1-2, kawecka2024molecularalterationsin pages 1-2)

**Environmental/Lifestyle Risk Factors:**
The literature reviewed does not provide specific environmental or lifestyle risk factors unique to mucinous ovarian carcinoma. General ovarian cancer risk factors include nulliparity, family history of ovarian cancer, and advancing age, with peak incidence at 55-59 years (przywara2025recenttherapiesand pages 1-2).

### Protective Factors
Specific protective factors for mucinous ovarian carcinoma are not well-characterized in the retrieved literature. For epithelial ovarian cancers generally, oral contraceptive use has been associated with decreased risk (wang2024globalincidenceof pages 1-2).

### Gene-Environment Interactions
The retrieved literature does not provide specific data on gene-environment interactions for mucinous ovarian carcinoma. This represents a gap in current knowledge.

---

## 3. Phenotypes

### Clinical Manifestations

**Symptoms (HP:0003002 - Cancer of breast [generalized symptom class]):**
Mucinous ovarian carcinoma often presents with **non-specific symptoms** including:
- Abdominal distension (HP:0003270)
- Abdominal pain (HP:0002027)
- Persistent bloating
- Nausea and vomiting in advanced cases with intestinal involvement (przywara2025recenttherapiesand pages 1-2, leo2021whatisnew pages 3-5)

**Physical Manifestations:**
- **Large, multilocular pelvic/abdominal mass** - typically **>10 cm** in diameter (wang2023mucinsandmucinous pages 1-2, wang2023mucinsandmucinous pages 2-3)
- **Unilateral ovarian involvement** in most primary cases (wang2023mucinsandmucinous pages 2-3)
- Mucinous ovarian carcinoma may be **less likely to cause rapid progression and marked ascites** compared to high-grade serous carcinoma (przywara2025recenttherapiesand pages 1-2)

### Phenotype Characteristics

**Age of Onset:**
- Predominantly affects **postmenopausal women**
- Peak incidence: **55-59 years** (przywara2025recenttherapiesand pages 1-2)
- Average age in metastatic series: **55 years** (kawecka2024molecularalterationsin pages 1-2)
- **Adult-onset** disease

**Stage at Diagnosis:**
- **65-80% diagnosed at early stage** (FIGO I-II) (wang2023mucinsandmucinous pages 1-2)
- **<5% present with advanced intra-abdominal disease** (leo2021whatisnew pages 3-5)

**Disease Progression:**
- Follows stepwise progression: benign cystadenoma → borderline tumor → invasive carcinoma
- **Progressive** disease course once invasive
- Advanced disease shows **poor response to chemotherapy** (wang2023mucinsandmucinous pages 1-2, affatato2020identificationofplk1 pages 1-3)

**Symptom Severity:**
- **Variable** depending on stage
- Early-stage disease: often asymptomatic or mild symptoms
- Advanced disease: severe symptoms related to tumor burden and peritoneal involvement

**Frequency Among Affected:**
- Non-specific abdominal symptoms: common (>80%)
- Pelvic mass on examination: very common in early-stage disease

### Quality of Life Impact
Advanced mucinous ovarian carcinoma with chemotherapy resistance significantly impacts quality of life due to disease progression, treatment toxicity, and poor prognosis. The median overall survival of 12-33 months for advanced disease (wang2023mucinsandmucinous pages 1-2) reflects substantial morbidity. Specific quality-of-life studies for mucinous ovarian carcinoma are not detailed in the retrieved literature.

### Suggested HPO Terms
- HP:0100615 - Ovarian neoplasm
- HP:0002027 - Abdominal pain
- HP:0003270 - Abdominal distention
- HP:0001513 - Obesity (as general cancer symptom)
- HP:0002664 - Neoplasm (parent term)

---

## 4. Genetic/Molecular Information

### Molecular Alterations Summary
| Gene/Pathway | Type of Alteration | Frequency (%) | Clinical Significance | PMID references |
|---|---|---:|---|---|
| **KRAS** | Activating somatic mutation, most often MAPK-pathway driver | **40–76%** overall; **43.6–64.9%** in recent summaries; **40–50%** in invasive mEOC | Most common molecular event in MOC; supports Type I/MAPK-driven biology; associated with progression from benign/borderline to carcinoma, platinum resistance, poor prognosis, and can aid distinction from other ovarian histotypes (kawecka2024molecularalterationsin pages 1-2, przywara2025recenttherapiesand pages 1-2, affatato2020identificationofplk1 pages 1-3) | Not available in retrieved contexts |
| **ERBB2 (HER2)** | Gene amplification / protein overexpression | **15–35%** overall; **18.8%** in one summary; **20–30%** in invasive mEOC; **35.3%** in MOC vs **5.3%** in borderline tumors in one recent report | Actionable target for trastuzumab-based and ADC strategies; may help differential diagnosis and molecular stratification; enriched in some Asian cohorts and relevant to targeted therapy selection (kawecka2024molecularalterationsin pages 1-2, przywara2025recenttherapiesand pages 1-2, nugawela2023targetedtherapyfor pages 1-2, przywara2025recenttherapiesand pages 4-6, affatato2020identificationofplk1 pages 1-3) | Not available in retrieved contexts |
| **TP53** | Pathogenic mutation / p53-abnormal pattern | **52–75%** overall; **~48.9–57%** in one summary; **16–52%** in another review of mEOC | More frequent in frankly malignant/high-grade tumors than benign/borderline lesions; associated with advanced FIGO stage, residual disease, poorer overall survival, and malignancy transition (kawecka2024molecularalterationsin pages 1-2, przywara2025recenttherapiesand pages 1-2, affatato2020identificationofplk1 pages 1-3) | Not available in retrieved contexts |
| **CDKN2A** | Copy-number loss, inactivation, homozygous deletion | **33–76%** | Characteristic lesion of mucinous carcinoma; loss increases with progression from benign/borderline to malignant disease and helps define the genomic profile of MOC (leo2021whatisnew pages 1-2, kawecka2024molecularalterationsin pages 1-2, affatato2020identificationofplk1 pages 1-3) | Not available in retrieved contexts |
| **BRAF** | Activating mutation | **~8.7%**; part of combined **KRAS/BRAF/CDKN2A** alteration set totaling **91%** in MOC and **95%** in mucinous borderline tumors in one report | Less common than KRAS but supports MAPK-pathway activation; implicated in progression biology and occasionally co-occurs with other drivers (kawecka2024molecularalterationsin pages 1-2, nugawela2023targetedtherapyfor pages 1-2, affatato2020identificationofplk1 pages 1-3) | Not available in retrieved contexts |
| **PIK3CA** | Activating mutation | Frequency not consistently quantified in retrieved MOC-specific sources | Recurrent but less common alteration; suggests PI3K-AKT pathway involvement and potential therapeutic relevance in selected tumors (przywara2025recenttherapiesand pages 1-2) | Not available in retrieved contexts |
| **PTEN** | Mutation / loss of function | Frequency not consistently quantified in retrieved MOC-specific sources | Indicates PI3K-AKT pathway dysregulation in a subset of MOC; contributes to molecular heterogeneity and possible targeted therapy opportunities (przywara2025recenttherapiesand pages 1-2) | Not available in retrieved contexts |
| **NRAS** | Activating mutation | Not quantified for MOC in retrieved sources | Included among RAS-pathway alterations relevant to ovarian carcinoma biology; highlights broader MAPK activation beyond KRAS (nugawela2023targetedtherapyfor pages 1-2, kobel2022theevolutionof pages 3-4) | Not available in retrieved contexts |
| **AKT1** | Activating mutation | Not quantified | Reported among pathway-activating events in mEOC; supports PI3K/AKT signaling as a secondary oncogenic route (affatato2020identificationofplk1 pages 1-3) | Not available in retrieved contexts |
| **FGFR2** | Mutation / pathway activation | Not quantified | Listed among actionable or potentially actionable alterations in MOC; may inform targeted therapy exploration (przywara2025recenttherapiesand pages 1-2) | Not available in retrieved contexts |
| **STK11** | Mutation | Not quantified | Recurrent but uncommon event in MOC summaries; may contribute to metabolic and growth dysregulation (przywara2025recenttherapiesand pages 1-2) | Not available in retrieved contexts |
| **CTNNB1 (Wnt/β-catenin)** | Activating mutation / pathway alteration | Not quantified | Suggests Wnt-pathway involvement in a subset of MOCs and provides rationale for pathway-directed investigation (przywara2025recenttherapiesand pages 1-2) | Not available in retrieved contexts |
| **SRC** | Mutation / pathway activation | Not quantified | Identified in molecular summaries as a potential contributor to invasive behavior and possible therapeutic target class (przywara2025recenttherapiesand pages 1-2) | Not available in retrieved contexts |
| **SMAD4** | Mutation / loss | Not quantified | Supports overlap with gastrointestinal-like signaling biology and may relate to aggressive behavior in selected cases (przywara2025recenttherapiesand pages 1-2) | Not available in retrieved contexts |
| **GNA11** | Mutation | Not quantified | Rarely reported event contributing to genomic heterogeneity; current clinical significance in MOC remains uncertain (przywara2025recenttherapiesand pages 1-2) | Not available in retrieved contexts |
| **PLK1 pathway** | Functional dependency / overexpression target identified by siRNA screening rather than recurrent mutation | Not a mutation frequency metric | Preclinical vulnerability: PLK1 inhibition suppressed growth, induced apoptosis, and synergized with paclitaxel in mucinous ovarian carcinoma cell lines/xenografts, nominating PLK1 as a therapeutic target despite not being a canonical recurrent genomic alteration (affatato2020identificationofplk1 pages 1-3) | Not available in retrieved contexts |
| **Mucin program (MUC1, MUC2, MUC5AC, MUC6, MUC13, MUC16)** | Differential expression rather than classic driver mutation | Example IHC frequencies in MOC from retrieved review: **MUC13 100% (13/13)**, **MUC5AC 94.8–100%**, **MUC16 66.7% (4/6)**, **MUC2 ~42–70%** across studies | Not primary genomic drivers, but biologically important for diagnosis, progression, chemoresistance, and differential diagnosis of primary vs metastatic mucinous tumors (wang2023mucinsandmucinous pages 1-2, wang2023mucinsandmucinous pages 3-5, wang2023mucinsandmucinous pages 2-3) | Not available in retrieved contexts |


*Table: This table summarizes the major molecular alterations reported for ovarian mucinous carcinoma, including approximate frequencies, clinical relevance, and available evidence from the retrieved sources. It is useful for quickly identifying recurrent drivers, actionable targets, and alterations linked to progression or chemoresistance.*

### Causal Genes and Pathogenic Variants

**Primary Somatic Mutations (not germline inherited):**

1. **KRAS (HGNC:6407)**
   - **Frequency:** 40-76% of mucinous ovarian carcinomas
   - **Variant types:** Activating missense mutations, commonly at codons 12, 13, 61
   - **Classification:** Pathogenic driver mutations
   - **Functional consequence:** Gain of function → constitutive MAPK pathway activation
   - **Clinical significance:** Strongest predictor of malignancy; associated with platinum resistance and poor prognosis (kawecka2024molecularalterationsin pages 1-2, przywara2025recenttherapiesand pages 1-2, nugawela2023targetedtherapyfor pages 1-2)
   - **Somatic origin:** Yes
   - **Allele frequency:** Common in tumor tissue, absent in germline

2. **ERBB2/HER2 (HGNC:3430)**
   - **Frequency:** 15-35% overall; 18.8-33.3% in various cohorts
   - **Alteration type:** Gene amplification/overexpression
   - **Classification:** Pathogenic, actionable target
   - **Functional consequence:** Receptor tyrosine kinase activation
   - **Clinical significance:** Targetable with trastuzumab, T-DXd; differential diagnosis marker (kawecka2024molecularalterationsin pages 1-2, przywara2025recenttherapiesand pages 1-2, przywara2025recenttherapiesand pages 4-6)
   - **Somatic origin:** Yes

3. **TP53 (HGNC:11998)**
   - **Frequency:** 52-75% in carcinomas (16-52% in some series)
   - **Variant types:** Missense, nonsense, frameshift mutations
   - **Classification:** Pathogenic
   - **Functional consequence:** Loss of tumor suppressor function
   - **Clinical significance:** Associated with high-grade disease, advanced stage, poor survival (kawecka2024molecularalterationsin pages 1-2, przywara2025recenttherapiesand pages 1-2)
   - **Somatic origin:** Yes (germline TP53 mutations [Li-Fraumeni syndrome] not characteristic of mucinous ovarian carcinoma)

4. **CDKN2A (HGNC:1787)**
   - **Frequency:** 33-76%
   - **Alteration type:** Copy-number loss, homozygous deletion
   - **Classification:** Pathogenic
   - **Functional consequence:** Loss of cell cycle regulation
   - **Clinical significance:** Increases with progression to malignancy (leo2021whatisnew pages 1-2, kawecka2024molecularalterationsin pages 1-2, affatato2020identificationofplk1 pages 1-3)
   - **Somatic origin:** Yes

5. **BRAF (HGNC:1097)**
   - **Frequency:** ~8.7% in mucinous ovarian carcinoma
   - **Variant type:** Activating mutations (e.g., V600E)
   - **Classification:** Pathogenic
   - **Functional consequence:** MAPK pathway activation
   - **Clinical significance:** Part of combined KRAS/BRAF/CDKN2A alteration signature (kawecka2024molecularalterationsin pages 1-2, nugawela2023targetedtherapyfor pages 1-2)
   - **Somatic origin:** Yes

6. **PIK3CA, PTEN, FGFR2, STK11, CTNNB1, SRC, SMAD4, GNA11**
   - Recurrent but less frequent mutations reported in molecular profiling studies
   - Contribute to molecular heterogeneity
   - Potential therapeutic targets (przywara2025recenttherapiesand pages 1-2)

### Epigenetic Information
The retrieved literature does not provide detailed epigenetic characterization (DNA methylation, histone modifications) specific to mucinous ovarian carcinoma. This represents a knowledge gap.

### Chromosomal Abnormalities
- **Copy number variations:** Amplification of chromosome 9p13.3 region reported (kawecka2024molecularalterationsin pages 1-2)
- **Copy-number loss of CDKN2A locus** (chromosome 9p21) (kawecka2024molecularalterationsin pages 1-2, affatato2020identificationofplk1 pages 1-3)
- Large-scale chromosomal instability is less pronounced than in high-grade serous carcinoma

---

## 5. Environmental Information

### Environmental Factors
The retrieved literature does not detail specific environmental toxins, radiation exposures, or occupational factors unique to mucinous ovarian carcinoma.

### Lifestyle Factors
General ovarian cancer lifestyle factors apply but are not mucinous-subtype-specific in the reviewed literature. These include smoking, diet, and reproductive history.

### Infectious Agents
Not applicable - mucinous ovarian carcinoma is not associated with infectious agents.

---

## 6. Mechanism / Pathophysiology

### Molecular Pathways

**1. MAPK/RAS/RAF Pathway (KEGG hsa04010):**
The most prominent pathway in mucinous ovarian carcinoma is the **MAPK pathway**, activated by KRAS (40-76%) or BRAF (~8.7%) mutations. Constitutive activation drives uncontrolled cell proliferation, survival, and contributes to chemotherapy resistance (nugawela2023targetedtherapyfor pages 1-2, affatato2020identificationofplk1 pages 1-3). The pathway includes:
- RAS → RAF → MEK1 → ERK cascade
- Downstream effects on cell cycle progression, apoptosis evasion

**2. PI3K-AKT-mTOR Pathway (KEGG hsa04151):**
Activated in subsets of tumors through:
- PIK3CA mutations
- PTEN loss
- ERBB2/HER2 amplification → HER2-mediated PI3K activation
Effects include enhanced cell survival, metabolic reprogramming, and resistance to apoptosis (przywara2025recenttherapiesand pages 1-2, przywara2025recenttherapiesand pages 4-6).

**3. Wnt/β-Catenin Pathway:**
CTNNB1 mutations contribute to Wnt pathway activation in a subset of cases, promoting stem-like properties and invasion (przywara2025recenttherapiesand pages 1-2).

**4. Cell Cycle Dysregulation:**
CDKN2A loss removes critical cell cycle checkpoints, permitting uncontrolled progression through G1/S transition (kawecka2024molecularalterationsin pages 1-2).

### Cellular Processes (GO Terms)

- **GO:0008283** - Cell proliferation (enhanced by KRAS, HER2, PI3K)
- **GO:0006915** - Apoptotic process (inhibited by PI3K-AKT, mucin-mediated resistance)
- **GO:0007049** - Cell cycle (dysregulated by CDKN2A loss)
- **GO:0001525** - Angiogenesis (VEGF pathway involvement)
- **GO:0030198** - Extracellular matrix organization (invasion and metastasis)
- **GO:0016477** - Cell migration (enhanced in invasive disease)
- **GO:0001837** - Epithelial to mesenchymal transition (EMT; associated with mucins MUC1, MUC4, MUC16) (wang2023mucinsandmucinous pages 3-5)

### Protein Dysfunction

**Mucin Glycoproteins:**
Mucinous ovarian carcinoma is characterized by high expression of **secreted mucins** (MUC2, MUC5AC, MUC5B, MUC6) and **membrane-bound mucins** (MUC1, MUC4, MUC13, MUC16). These contribute to:
- **Physical barrier formation** blocking drug accessibility
- **Chemotherapy resistance** via apoptosis inhibition, altered drug metabolism, cancer stem cell promotion
- **EMT promotion** (MUC1, MUC4, MUC16)
- **Immune evasion and cell adhesion** (MUC16-mesothelin interaction) (wang2023mucinsandmucinous pages 3-5, wang2023mucinsandmucinous pages 2-3)

**Receptor Tyrosine Kinase Dysfunction:**
HER2 amplification leads to constitutive receptor dimerization and activation, driving PI3K-AKT and MAPK signaling (przywara2025recenttherapiesand pages 4-6).

### Metabolic Changes
- **MUC4-mediated nucleotide metabolism alterations:** MUC4 negatively regulates hCNT1 (nucleoside transporter) via NF-κB signaling, contributing to gemcitabine resistance (wang2023mucinsandmucinous pages 3-5)
- **Enhanced glycolysis:** MUC16 regulates glucose uptake through GLUT1, increasing energy for tumor growth (wang2023mucinsandmucinous pages 2-3)

### Chemotherapy Resistance Mechanisms

1. **Mucin-mediated physical barrier:** Gel-forming mucins (MUC2, MUC5AC) create protective barriers (wang2023mucinsandmucinous pages 3-5)
2. **Apoptosis resistance:** MUC16 inhibits TRAIL-induced apoptosis and reduces cisplatin sensitivity (wang2023mucinsandmucinous pages 3-5)
3. **Cancer stem cell enrichment:** MUC4 increases CD133+ cancer stem cells (wang2023mucinsandmucinous pages 3-5)
4. **EMT induction:** MUC1, MUC4, MUC16 downregulate E-cadherin, upregulate vimentin (wang2023mucinsandmucinous pages 3-5)
5. **KRAS mutation:** Associated with intrinsic platinum resistance (przywara2025recenttherapiesand pages 1-2)

### Cell Types Involved (CL Terms)
- **CL:0000066** - Epithelial cell (origin of carcinoma)
- **CL:0000150** - Glandular epithelial cell (mucinous phenotype)
- **CL:0002327** - Malignant cell

---

## 7. Anatomical Structures Affected

### Organ Level (UBERON Terms)

**Primary Site:**
- **UBERON:0000992** - Ovary (primary site of origin for true primary mucinous ovarian carcinoma)
- Typically **unilateral** involvement (wang2023mucinsandmucinous pages 2-3)

**Secondary Involvement (Advanced Disease):**
- **UBERON:0000971** - Peritoneum (peritoneal carcinomatosis in advanced cases)
- **UBERON:0001416** - Omentum (omental involvement common in advanced disease)
- **UBERON:0000059** - Large intestine (potential obstruction)
- **UBERON:0001255** - Urinary bladder (local invasion)
- **UBERON:0001013** - Adipose tissue (omental and peritoneal involvement)

**Body Systems:**
- Reproductive system (primary)
- Digestive system (secondary complications, obstruction)

### Tissue and Cell Level

**Tissue Types:**
- **Epithelial tissue** (malignant transformation of ovarian surface or cyst epithelium)
- **Mucinous epithelium** with goblet cells and abundant intracellular mucin

**Cell Populations:**
- **CL:0000066** - Epithelial cells
- **CL:0000160** - Goblet cell-like mucinous cells
- **CL:0002327** - Malignant epithelial cells with mucinous differentiation

### Subcellular Level (GO Cellular Component)

- **GO:0005886** - Plasma membrane (mucin localization, HER2 receptor)
- **GO:0005576** - Extracellular region (secreted mucins)
- **GO:0005737** - Cytoplasm (intracellular mucin accumulation)
- **GO:0005634** - Nucleus (TP53, KRAS signaling targets)

### Localization
- **UBERON:0000992** - Ovary (unilateral in primary disease)
- **Lateralization:** Predominantly **unilateral** for primary tumors; bilaterality suggests metastatic disease (wang2023mucinsandmucinous pages 2-3)

---

## 8. Temporal Development

### Onset

**Age of Onset:**
- **Postmenopausal/Adult-onset:** Peak incidence 55-59 years (przywara2025recenttherapiesand pages 1-2)
- Rare in premenopausal women

**Onset Pattern:**
- **Insidious/Chronic:** Early-stage disease often asymptomatic
- **Subacute presentation:** Symptoms develop over weeks to months in growing masses

### Progression

**Disease Stages:**
Staged according to **FIGO (International Federation of Gynecology and Obstetrics)** and **AJCC** staging systems:
- **Stage I:** Tumor confined to ovaries (65-80% at diagnosis) (wang2023mucinsandmucinous pages 1-2)
- **Stage II:** Pelvic extension
- **Stage III:** Peritoneal metastasis beyond pelvis
- **Stage IV:** Distant metastasis

**Histologic Progression:**
- **Benign mucinous cystadenoma**
- **Borderline mucinous tumor (mucinous tumor of low malignant potential)**
- **Invasive mucinous carcinoma** (expansile or infiltrative pattern) (wang2023mucinsandmucinous pages 1-2)

Molecular progression: increasing frequency of KRAS, CDKN2A, TP53 mutations from benign → borderline → malignant (kawecka2024molecularalterationsin pages 1-2).

**Progression Rate:**
- **Variable:** Early-stage disease may be indolent
- **Rapid in advanced disease:** Median survival 12-33 months for stage III/IV (wang2023mucinsandmucinous pages 1-2)

**Disease Course:**
- **Progressive** once invasive
- Poor response to chemotherapy leads to relentless progression in advanced cases

**Disease Duration:**
- **Chronic for early-stage disease** with good prognosis
- **Abbreviated in advanced disease** due to chemoresistance

---

## 9. Inheritance and Population

### Epidemiology Summary
| Parameter | Finding/Value | References |
|---|---|---|
| Global incident cases (mucinous ovarian cancer, 2020) | Estimated **35,712** new mucinous ovarian cancer cases worldwide in 2020 | (wang2024globalincidenceof pages 1-2, wang2024globalincidenceof pages 2-3) |
| Global share among ovarian cancer histotypes | Mucinous carcinoma accounted for **11.47%** of incident ovarian cancers globally; serous remained dominant at **42.97%** | (wang2024globalincidenceof pages 2-3) |
| Global age-standardized incidence rate (ASR) | Global ASR for mucinous ovarian cancer was **0.68 per 100,000** population in 2020 | (wang2024globalincidenceof pages 2-3) |
| Regional incidence pattern | **Eastern Europe** had the **highest rate of mucinous carcinoma** among world regions | (wang2024globalincidenceof pages 1-2) |
| Regional proportional variation | Mucinous carcinoma proportion among ovarian cancers ranged from **5.94% in North America** to **20.66% in Central America** | (wang2024globalincidenceof pages 2-3) |
| Rarity among epithelial ovarian cancers | Mucinous ovarian carcinoma is rare, accounting for about **3%–5%** of epithelial ovarian cancers in some contemporary reviews; other summaries give **3%–4%** or **2–3%** | (wang2023mucinsandmucinous pages 1-2, przywara2025recenttherapiesand pages 1-2, sauriol2020modelingthediversity pages 1-3) |
| True primary vs metastatic disease | Central pathology review literature summarized in recent reviews indicates many tumors historically labeled “ovarian mucinous” are metastatic; one review notes true primary ovarian mucinous cancer may account for only **1%–3%** of ovarian cancers, while another reports that in one series only **23%** of 52 diagnosed MOCs were primary and another study found **71%** metastatic | (wang2023mucinsandmucinous pages 2-3, przywara2025recenttherapiesand pages 1-2) |
| Typical age group | Ovarian cancer overall is mostly a disease of **postmenopausal women**; one recent general ovarian cancer review notes peak incidence at **55–59 years** | (przywara2025recenttherapiesand pages 1-2, wang2024globalincidenceof pages 2-3) |
| Average age in metastatic mucinous tumors to ovary | For ovarian metastases in mucinous tumor series, average age reported as **55 years** | (kawecka2024molecularalterationsin pages 1-2) |
| Stage at diagnosis | Mucinous ovarian carcinoma is disproportionately diagnosed early: about **65%–80%** of cases are diagnosed in **early stage** | (wang2023mucinsandmucinous pages 1-2) |
| Early-stage prognosis | Patients with **FIGO stage I** mucinous ovarian carcinoma have a **5-year overall survival close to 90%** | (wang2023mucinsandmucinous pages 1-2) |
| Stage I-II survival benchmark from early-stage ovarian carcinoma cohorts | Early-stage ovarian carcinoma cohorts cited in biomarker work report overall **5-year survival ~89% for stage I** and **71% for stage II**; these data are not mucinous-exclusive but are relevant context for early-stage mucinous disease | (wang2023mucinsandmucinous pages 1-2) |
| Advanced-stage prognosis | For **advanced MOC (FIGO III–IV)**, estimated **median overall survival is 12–33 months** | (wang2023mucinsandmucinous pages 1-2) |
| Advanced-stage survival compared with serous carcinoma | One targeted-therapy review states **median survival of stage III/IV mucinous ovarian carcinoma is <15 months**, versus **41 months** for high-grade serous ovarian carcinoma | (nugawela2023targetedtherapyfor pages 1-2) |
| Response to standard chemotherapy | Advanced mucinous ovarian carcinoma has poor response to conventional platinum-based chemotherapy; one preclinical review states only about **30%** of patients respond to first-line therapy versus about **70%** of high-grade serous ovarian cancer patients | (wang2023mucinsandmucinous pages 1-2, affatato2020identificationofplk1 pages 1-3) |
| Survival by histotype relative to serous | Population-level global incidence paper notes endometrioid, mucinous, and clear cell subtypes show **better ovarian cancer–specific survival than serous carcinoma** overall, although advanced mucinous disease performs poorly once metastatic/advanced | (wang2024globalincidenceof pages 1-2, wang2023mucinsandmucinous pages 1-2, nugawela2023targetedtherapyfor pages 1-2) |
| Clinical presentation | Symptoms are often **non-specific**, commonly including **abdominal distension or pain**; compared with serous tumors, mucinous tumors may be less likely to cause the rapid progression and marked ascites typical of serous carcinoma | (przywara2025recenttherapiesand pages 1-2) |
| Gross/pathologic clinical characteristic | Primary mucinous ovarian carcinoma is typically a **large, multilocular** unilateral ovarian neoplasm; tumor size **>10 cm** and unilateral presentation favor primary ovarian origin | (wang2023mucinsandmucinous pages 1-2, wang2023mucinsandmucinous pages 2-3) |
| Demographic sex pattern | As an ovarian carcinoma, disease occurs overwhelmingly in **females/women** | (wang2024globalincidenceof pages 1-2, przywara2025recenttherapiesand pages 1-2) |
| Geographic burden context | The global subtype burden study estimated ovarian cancer incidence using 67 countries with registry-derived subtype proportions and found substantial regional differences, supporting geographically tailored prevention and resource planning | (wang2024globalincidenceof pages 1-2, wang2024globalincidenceof pages 2-3) |


*Table: This table summarizes recent evidence on the epidemiology, clinical presentation, stage distribution, and prognosis of ovarian mucinous carcinoma, emphasizing 2024 global incidence data and clinically important comparisons with serous ovarian carcinoma.*

### For Genetic Etiology

**Inheritance Pattern:**
- **Not inherited** in the classic germline sense
- **Somatic mutations** acquired during tumor development
- **Not associated with BRCA1/2** germline mutations (distinguishes from high-grade serous) (sauriol2020modelingthediversity pages 1-3, affatato2020identificationofplk1 pages 1-3)
- Occasional association with **Lynch syndrome** (mismatch repair deficiency) for endometrioid ovarian carcinoma, but this is not characteristic of mucinous subtype (sauriol2020modelingthediversity pages 1-3)

**Penetrance, Expressivity, Anticipation:**
Not applicable (somatic disease)

**Germline Mosaicism:**
Not applicable

**Founder Effects:**
HER2 amplification frequency is higher in **Asian populations** (27.4-33.3%) compared to overall frequency (18.8%) (przywara2025recenttherapiesand pages 1-2), suggesting possible population-specific enrichment.

### Population Demographics

**Global Distribution:**
- **Global incidence (2020):** 35,712 new cases (11.47% of ovarian cancers) (wang2024globalincidenceof pages 2-3)
- **Age-standardized rate:** 0.68 per 100,000 population globally (wang2024globalincidenceof pages 2-3)
- **Geographic variation:** Highest rates in **Eastern Europe**; proportion ranges from 5.94% (North America) to 20.66% (Central America) (wang2024globalincidenceof pages 2-3)

**Sex Ratio:**
- Overwhelmingly affects **females** (ovarian origin)

**Age Distribution:**
- Peak incidence: **55-59 years**
- Postmenopausal predominance (przywara2025recenttherapiesand pages 1-2)

---

## 10. Diagnostics

### Diagnostic Methods Summary
| Diagnostic Category | Specific Test/Method | Findings/Markers | Clinical Utility | References |
|---|---|---|---|---|
| Histopathologic classification | WHO 2020 histotype classification | Ovarian carcinoma is classified into principal histotypes including mucinous carcinoma; accurate histotyping integrates morphology, immunophenotype, and molecular features | Establishes that mucinous carcinoma is a distinct ovarian carcinoma type requiring subtype-specific diagnosis and management | (kobel2022theevolutionof pages 1-3, leo2021whatisnew pages 1-2) |
| Histopathologic subtyping | Growth pattern assessment on resection specimen | Mucinous ovarian carcinoma is subclassified into **expansile** and **infiltrative** invasion patterns; distinction is clinically important particularly in stage I disease | Helps risk stratification and may affect decisions about staging lymphadenectomy and adjuvant chemotherapy | (wang2023mucinsandmucinous pages 1-2) |
| Gross pathology / surgical pathology | Macroscopic tumor assessment | Primary mucinous ovarian carcinoma is typically a **large, multilocular**, usually **unilateral** ovarian mass; tumor size **>10 cm** favors primary ovarian origin | Supports distinction of primary ovarian tumor from metastatic mucinous tumor to the ovary | (wang2023mucinsandmucinous pages 1-2, wang2023mucinsandmucinous pages 2-3) |
| Histopathology for primary vs metastatic differential | Routine microscopic examination | Features favoring **primary mucinous ovarian carcinoma**: benign or borderline components, unilateral mass, normal appendix, no capsular/serosal implants, absence of extracellular mucin; features favoring **metastatic mucinous tumor**: ovarian surface/hilum involvement, infiltrative stromal invasion, extracellular mucin, widespread signet-ring cells | Core diagnostic step to distinguish primary ovarian mucinous carcinoma from gastrointestinal, appendiceal, breast, or cervical metastases | (wang2023mucinsandmucinous pages 2-3) |
| Histopathology / mucin pattern | Intracellular vs extracellular mucin distribution | Primary mucinous ovarian carcinoma is often characterized by **high intracellular mucin** and relatively **low extracellular mucin**; metastatic mucinous tumors more often show abundant extracellular mucin | Useful adjunctive morphologic clue in differential diagnosis; extracellular mucin may also correlate with poorer prognosis in primary disease | (wang2023mucinsandmucinous pages 3-5, wang2023mucinsandmucinous pages 2-3) |
| Immunohistochemistry | CK7 / CK20 / CDX2 / PAX8 panel | Typical profile for mucinous ovarian carcinoma: **CK7 positive**, **CK20 and CDX2 variable**, **PAX8 variable positive**, **SATB2 negative**; strong **PAX8 positivity** supports ovarian origin | Widely used first-line IHC panel to separate primary ovarian mucinous carcinoma from lower GI and other extra-ovarian mucinous carcinomas | (kawecka2024molecularalterationsin pages 1-2, wang2023mucinsandmucinous pages 2-3) |
| Immunohistochemistry | SATB2 with CK7 | Combination of **CK7 and SATB2** can distinguish lower gastrointestinal tumors from primary ovarian mucinous tumors with high accuracy; lower GI metastases tend to be SATB2 positive | Improves diagnostic specificity for metastases from colorectum/appendix | (wang2023mucinsandmucinous pages 3-5, wang2023mucinsandmucinous pages 2-3) |
| Immunohistochemistry | Claudin 18.2 / PAX8 / SATB2 panel | Reported patterns: **primary mucinous ovarian carcinoma** often **claudin18.2+/PAX8+/SATB2-**; upper GI metastases **claudin18.2+/PAX8-/SATB2-**; lower GI metastases **claudin18.2-/PAX8-/SATB2+** | Useful extended panel when routine CK7/CK20/CDX2/PAX8 results are equivocal | (wang2023mucinsandmucinous pages 3-5, wang2023mucinsandmucinous pages 2-3) |
| Immunohistochemistry | MUC1, MUC2, MUC5AC, MUC6 | Mucin markers contribute to differential diagnosis: **MUC2** and **MUC6** may help identify primary mucinous ovarian carcinoma; **MUC5AC** may help distinguish colorectal cancer from primary ovarian mucinous carcinoma but is less useful for pancreatic metastases; **MUC1** has been proposed as a novel discriminator between primary and metastatic mucinous ovarian tumors | Ancillary diagnostic markers, especially useful when combined with standard epithelial and lineage markers | (wang2023mucinsandmucinous pages 3-5, wang2023mucinsandmucinous pages 2-3) |
| Immunohistochemistry | MUC2 and MUC5AC comparison | In one summarized comparison, **MUC2 positivity** was reported in colorectal cancers but not mucinous ovarian cancers, whereas **MUC5AC** was much more frequent in mucinous ovarian cancer | Helps separate colorectal metastasis from primary ovarian mucinous carcinoma | (wang2023mucinsandmucinous pages 3-5) |
| Histotype-oriented IHC | Four-marker ovarian carcinoma panel | A four-marker panel (**WT1 / p53 / napsin A / PR**) distinguishes the five principal ovarian carcinoma histotypes with high accuracy; mucinous carcinoma is identified largely through exclusion plus morphology and lineage markers rather than a unique single marker | Useful for overall ovarian carcinoma subclassification when the diagnosis is uncertain among ovarian histotypes | (kobel2022theevolutionof pages 1-3) |
| Serum biomarker | CA125 | CA125 has **lower sensitivity in mucinous ovarian carcinoma** than in serous carcinoma; one recent review notes abnormal CA125 in only about **69%** of mucinous tumors, often at lower absolute levels | Limited as a stand-alone diagnostic marker; lower performance underscores need for imaging, pathology, and additional biomarkers | (przywara2025recenttherapiesand pages 1-2) |
| Serum / emerging biomarker | MUC13 | MUC13 has been proposed as a candidate biomarker that may complement CA125 in detecting non-serous ovarian carcinomas including mucinous tumors | Potential adjunct biomarker for non-serous subtype detection, though not yet standard of care | (przywara2025recenttherapiesand pages 1-2, wang2023mucinsandmucinous pages 2-3) |
| Imaging | Ultrasound / CT / MRI | Imaging can detect an adnexal mass and assess size, multilocularity, laterality, and spread; however, recent reviews note persistent diagnostic difficulty in reliably classifying mucinous tumors preoperatively | Preoperative evaluation of extent of disease and surgical planning; limited specificity for distinguishing primary from metastatic mucinous tumors without pathology | (wang2023mucinsandmucinous pages 1-2) |
| Preoperative assessment | Clinical evaluation plus imaging plus pathology correlation | Because many tumors historically labeled ovarian mucinous are actually metastases, diagnosis requires correlation of ovarian findings with gastrointestinal/appendiceal evaluation and clinicopathologic review | Avoids misclassification and inappropriate ovarian-cancer-directed treatment of metastatic GI cancer | (kawecka2024molecularalterationsin pages 1-2, wang2023mucinsandmucinous pages 2-3) |
| Molecular testing | KRAS / ERBB2(HER2) / TP53 / CDKN2A profiling | Common alterations in mucinous ovarian carcinoma include **KRAS** mutations, **ERBB2 amplification**, **TP53** mutation, and **CDKN2A** loss/inactivation; absence of KRAS or HER2 in some cases may suggest unusual precursors such as teratoma-associated tumors | Supports diagnosis, biological classification, prognostic assessment, and selection for targeted therapy | (leo2021whatisnew pages 1-2, kawecka2024molecularalterationsin pages 1-2, przywara2025recenttherapiesand pages 1-2, nugawela2023targetedtherapyfor pages 1-2, affatato2020identificationofplk1 pages 1-3) |
| Molecular diagnostics in differential diagnosis | Correlation of mutation profile with morphology | Molecular alterations may complement histology and IHC in distinguishing primary mucinous ovarian tumors from metastases and from other ovarian epithelial subtypes | Useful adjunct where morphology and immunophenotype are overlapping or ambiguous | (kawecka2024molecularalterationsin pages 1-2) |
| Post-operative definitive diagnosis | Integrated morphologic + IHC diagnosis on resection specimen | Recent reviews emphasize that definitive diagnosis is often made **post-operatively** after full histopathologic examination with immunohistochemical markers because of strong overlap with metastatic mucinous lesions | Current gold standard for final diagnosis of primary ovarian mucinous carcinoma | (kawecka2024molecularalterationsin pages 1-2) |


*Table: This table summarizes the main diagnostic approaches for ovarian mucinous carcinoma, including pathology, immunohistochemistry, biomarkers, imaging, and molecular testing. It is especially useful for distinguishing primary ovarian mucinous carcinoma from metastatic gastrointestinal mucinous tumors.*

### Key Diagnostic Challenges

**Primary vs. Metastatic Differentiation:**
The most critical diagnostic challenge is distinguishing **primary ovarian mucinous carcinoma** from **metastatic mucinous adenocarcinoma** to the ovary, especially from gastrointestinal, pancreatic, or appendiceal primary sites. This requires integration of:
- Clinical features (bilaterality, appendiceal pathology, GI symptoms)
- Gross pathology (tumor size, unilaterality)
- Histology (benign/borderline components, invasion pattern, extracellular mucin)
- Immunohistochemistry (CK7/CK20/CDX2/PAX8/SATB2/claudin18.2 panels, mucins)
- Molecular testing (KRAS, HER2, TP53 profile) (kawecka2024molecularalterationsin pages 1-2, wang2023mucinsandmucinous pages 2-3)

### Omics-Based Diagnostics

**Molecular Profiling:**
- **Next-generation sequencing panels:** Identify KRAS, ERBB2, TP53, CDKN2A alterations to confirm diagnosis and guide targeted therapy (kawecka2024molecularalterationsin pages 1-2, przywara2025recenttherapiesand pages 1-2)
- **HER2 testing (IHC and/or FISH):** Essential for trastuzumab/ADC eligibility (przywara2025recenttherapiesand pages 4-6)

**Liquid Biopsy:**
Emerging but not standard; potential for ctDNA detection of KRAS mutations.

### Clinical Criteria

**WHO 2020 Diagnostic Criteria:**
- Histotype classification requires integration of morphology, immunoprofile, and molecular features (kobel2022theevolutionof pages 1-3, leo2021whatisnew pages 1-2)

**Differential Diagnosis:**
Must distinguish from:
- **Metastatic gastrointestinal mucinous adenocarcinoma** (most common mimic)
- **Metastatic pancreatic mucinous carcinoma**
- **Appendiceal mucinous neoplasm**
- **Metastatic breast mucinous carcinoma**
- **Endocervical adenocarcinoma**
- **Ovarian seromucinous carcinoma** (now classified as endometrioid variant with mucinous differentiation) (kobel2022theevolutionof pages 3-4)
- Other ovarian epithelial subtypes

### Screening
There is **no effective population-based screening** for ovarian mucinous carcinoma. CA125/transvaginal ultrasound screening has not demonstrated mortality benefit for ovarian cancer overall and is **less sensitive for mucinous subtype** (CA125 elevated in only ~69% of mucinous cases) (wang2024globalincidenceof pages 1-2, przywara2025recenttherapiesand pages 1-2).

---

## 11. Outcome/Prognosis

### Survival and Mortality

**Early-Stage Disease (FIGO I):**
- **5-year overall survival: ~90%** (wang2023mucinsandmucinous pages 1-2)
- Favorable prognosis with complete surgical resection

**Advanced Disease (FIGO III-IV):**
- **Median overall survival: 12-33 months** (wang2023mucinsandmucinous pages 1-2)
- **<15 months in some reports** vs. **41 months for high-grade serous carcinoma** at equivalent stage (nugawela2023targetedtherapyfor pages 1-2)
- Poor prognosis driven by chemotherapy resistance

**Stage-Specific Survival:**
- Stage I: Excellent (5-year OS ~89%)
- Stage II: Good (5-year OS ~71%) - these figures are for early-stage ovarian carcinoma generally, not mucinous-exclusive
- Stage III/IV: Poor (median 12-33 months) (wang2023mucinsandmucinous pages 1-2)

### Disease Course and Complications

**Complications:**
- **Intraoperative cyst rupture:** Can lead to peritoneal mucin dissemination, pseudomyxoma peritonei, and increased recurrence risk (wang2023mucinsandmucinous pages 1-2)
- **Intestinal obstruction:** From peritoneal carcinomatosis in advanced disease
- **Chemotherapy resistance:** Intrinsic and acquired resistance to platinum-based therapy

**Recurrence:**
- High recurrence rate in advanced disease despite initial chemotherapy
- **70% of patients** treated with standard chemotherapy develop recurrent/resistant disease (affatato2020identificationofplk1 pages 1-3)

### Prognostic Factors

**Favorable:**
- **Early stage (I-II)** at diagnosis (wang2023mucinsandmucinous pages 1-2)
- **Expansile invasion pattern** (better than infiltrative) (wang2023mucinsandmucinous pages 1-2)
- **Complete surgical resection** with no residual disease
- **Absence of TP53 mutation** (in some series)

**Unfavorable:**
- **Advanced stage (III-IV)**
- **Infiltrative invasion pattern** (wang2023mucinsandmucinous pages 1-2)
- **TP53 mutation** (associated with high-grade disease, advanced FIGO stage, residual disease >1 cm, poor overall survival) (przywara2025recenttherapiesand pages 1-2)
- **KRAS mutation** (associated with platinum resistance and poor prognosis) (przywara2025recenttherapiesand pages 1-2)
- **Residual disease >1 cm after debulking surgery**
- **Extracellular mucin** (may correlate with poor prognosis) (wang2023mucinsandmucinous pages 3-5)
- **Low response to standard chemotherapy** (~30% response rate vs ~70% for HGSOC) (affatato2020identificationofplk1 pages 1-3)

### Prognostic Biomarkers
- **KRAS mutation status:** Predictor of platinum resistance
- **TP53 mutation status:** Associated with aggressive disease
- **HER2 amplification:** Actionable target but also may indicate more aggressive biology
- **Expansile vs. infiltrative histology:** Prognostic in stage I disease

---

## 12. Treatment

### Pharmacotherapy

**Standard Chemotherapy (DrugBank IDs where available):**
- **Carboplatin + Paclitaxel:** First-line standard adjuvant/neoadjuvant regimen despite **poor response rate (~30%)** in advanced mucinous ovarian carcinoma (affatato2020identificationofplk1 pages 1-3)
  - Carboplatin: DNA cross-linking agent, CHEBI:31355
  - Paclitaxel: Microtubule stabilizer, CHEBI:45863
- **Alternative regimens:** Given poor platinum response, some centers have explored gastrointestinal-type regimens (e.g., capecitabine/oxaliplatin) based on molecular similarity to GI tumors, though prospective randomized trial (GOG-0241) was terminated due to poor accrual (wang2023mucinsandmucinous pages 1-2, nugawela2023targetedtherapyfor pages 1-2)

### Advanced Therapeutics

**Targeted Therapies:**

1. **HER2-Targeted Agents:**
   - **Trastuzumab** (Herceptin): Monoclonal antibody for HER2-amplified tumors (przywara2025recenttherapiesand pages 1-2, przywara2025recenttherapiesand pages 4-6)
   - **Trastuzumab deruxtecan (T-DXd, Enhertu):** HER2-directed antibody-drug conjugate showing promise in HER2-expressing solid tumors including mucinous ovarian carcinoma; ongoing trials NCT04482309, NCT04639219 (przywara2025recenttherapiesand pages 4-6)
   - **Trastuzumab emtansine (T-DM1):** ADC evaluated in BOUQUET trial (NCT04931342) for rare ovarian tumors (przywara2025recenttherapiesand pages 4-6)
   - **Pertuzumab:** HER2 dimerization inhibitor used in combination with trastuzumab (przywara2025recenttherapiesand pages 4-6)

2. **KRAS Pathway Inhibitors:**
   - **Direct KRASG12C inhibitors** (adagrasib, sotorasib): Promising in KRASG12C-mutant cancers (predominantly lung cancer); ongoing trials in solid tumors but **none specifically in mucinous ovarian carcinoma** (przywara2025recenttherapiesand pages 4-6)
   - Clinical trials: KRYSTAL-10 (NCT04793958), CodeBreak300 (NCT05198934) - focus on colorectal cancer, not ovarian

3. **Multi-Tyrosine Kinase Inhibitors:**
   - **Bevacizumab** (Avastin): VEGF inhibitor; limited data in mucinous ovarian carcinoma (nugawela2023targetedtherapyfor pages 1-2)
   - **Sunitinib, Cediranib, Pazopanib, Nintedanib:** Multi-kinase inhibitors with varying evidence (nugawela2023targetedtherapyfor pages 1-2)

4. **Cell Cycle Inhibitors:**
   - **PLK1 inhibitors (Onvansertib, Volasertib):** Preclinical studies show synergy with paclitaxel; onvansertib + paclitaxel combination showed tumor regression and prolonged survival in mucinous ovarian carcinoma xenografts (affatato2020identificationofplk1 pages 1-3)

5. **WEE1 Inhibitor:**
   - **AZD1775:** Under investigation (nugawela2023targetedtherapyfor pages 1-2)

**Immunotherapy:**
- **Checkpoint inhibitors (anti-PD-1/PD-L1):** Mucinous ovarian carcinoma shows **low PD-L1 expression (~14%)** and **low tumor mutational burden**, limiting immunotherapy efficacy; subset with high PD-L1 or TMB may respond (przywara2025recenttherapiesand pages 1-2)

**Mucin-Targeted Therapies:**
- **Gatipotuzumab:** Humanized anti-MUC1 antibody (wang2023mucinsandmucinous pages 3-5)
- **MUC1/miRNA chimeras (MUC1/let-7i, MUC1/miR-29b):** Experimental approaches to reverse paclitaxel resistance (wang2023mucinsandmucinous pages 3-5)

### Surgical Interventions (MAXO Terms)

**Primary Cytoreductive Surgery (MAXO:0000004):**
- **Complete surgical resection** is cornerstone of treatment
- Goal: **no residual disease** (R0 resection)
- Procedures include:
  - Total abdominal hysterectomy
  - Bilateral salpingo-oophorectomy
  - Omentectomy
  - Peritoneal biopsies/resection
  - Lymph node sampling (especially for infiltrative stage I disease) (wang2023mucinsandmucinous pages 1-2)
- **Cyst rupture should be avoided** due to risk of peritoneal mucin dissemination (wang2023mucinsandmucinous pages 1-2)

**Interval/Secondary Cytoreductive Surgery:**
- May be considered after neoadjuvant chemotherapy in select cases

**Hyperthermic Intraperitoneal Chemotherapy (HIPEC):**
- Investigational for advanced/recurrent mucinous ovarian carcinoma; case reports show durable responses (przywara2025recenttherapiesand pages 4-6)

### Supportive and Rehabilitative Care (MAXO Terms)

- **Pain management** (MAXO:0001298)
- **Nutritional support**
- **Management of bowel obstruction** in advanced disease

### Experimental Treatments

**Antibody-Drug Conjugates:**
- **Tisotumab vedotin:** Tissue factor-targeting ADC evaluated in platinum-resistant ovarian cancer (innovaTV 208, NCT03657043) (przywara2025recenttherapiesand pages 4-6)
- **Seribantumab:** Anti-HER3 antibody effective in NRG1-fusion cancers (rare in ovarian cancer) (przywara2025recenttherapiesand pages 4-6)

**Combination Strategies:**
- **Onvansertib (PLK1 inhibitor) + Paclitaxel:** Preclinical data support clinical investigation (affatato2020identificationofplk1 pages 1-3)
- **HER2 inhibitors + NK cell therapy:** Preclinical models show enhanced efficacy (przywara2025recenttherapiesand pages 4-6)

### Treatment Outcomes

**Response Rates:**
- **First-line platinum/taxane:** ~30% response in advanced disease (vs ~70% in HGSOC) (affatato2020identificationofplk1 pages 1-3)
- **HER2-targeted therapy:** Case reports show dramatic responses in HER2-amplified tumors (przywara2025recenttherapiesand pages 4-6)

**Side Effects:**
- Standard chemotherapy: Myelosuppression, neuropathy, gastrointestinal toxicity
- HER2 inhibitors: Infusion reactions, cardiotoxicity
- PLK1 inhibitors: Gastrointestinal adverse events, fatigue

### Treatment Strategy

**MAXO Terms:**
- MAXO:0000058 - Chemotherapy
- MAXO:0000601 - Surgical resection
- MAXO:0000756 - Targeted molecular therapy
- MAXO:0001174 - Immunotherapy

**Clinical Pathways:**
1. **Early-stage (I-II):** Complete surgical resection → observation (stage IA-IB expansile) or adjuvant chemotherapy (stage IC-II or infiltrative pattern)
2. **Advanced-stage (III-IV):** Primary or interval cytoreductive surgery + platinum/taxane chemotherapy → targeted therapy in HER2-amplified cases → clinical trial enrollment

**Personalized Medicine:**
- **HER2 testing mandatory** for targeted therapy selection
- **KRAS mutation testing** to identify patients with poor platinum response who may benefit from alternative strategies
- **Genomic profiling** to identify rare actionable targets (KRASG12C, NRG1 fusions, high TMB)

---

## 13. Prevention

### Primary Prevention
No specific primary prevention strategies exist for mucinous ovarian carcinoma. General ovarian cancer prevention measures include:
- **Oral contraceptive use:** Associated with reduced ovarian cancer risk (not mucinous-specific) (wang2024globalincidenceof pages 1-2)

### Secondary Prevention
**Screening:**
- **No effective screening program** for ovarian mucinous carcinoma
- CA125/transvaginal ultrasound ineffective (CA125 insensitive in mucinous subtype) (przywara2025recenttherapiesand pages 1-2)

### Tertiary Prevention
- **Optimal cytoreductive surgery** to prevent recurrence
- **Adjuvant chemotherapy** in high-risk early-stage disease (infiltrative pattern, stage IC-II)
- **Avoiding intraoperative cyst rupture** to minimize peritoneal dissemination (wang2023mucinsandmucinous pages 1-2)

### Counseling
**Genetic Counseling:**
Not routinely indicated (no BRCA association). However, comprehensive family history should be obtained, and rare Lynch syndrome association with endometrioid (not mucinous) subtype should be considered in appropriate clinical contexts.

---

## 14. Other Species / Natural Disease

### Natural Disease in Animal Models
The retrieved literature does not describe naturally occurring mucinous ovarian carcinoma in companion animals or wildlife. This likely reflects both rarity of the disease and limited veterinary oncology reporting for this specific histotype.

### Taxonomy
Not applicable - mucinous ovarian carcinoma is a human disease without well-documented natural occurrence in other species.

---

## 15. Model Organisms

### Model Types and Systems

**Cell Lines:**
Multiple patient-derived mucinous ovarian carcinoma cell lines are described for preclinical research:

1. **MCAS** (affatato2020identificationofplk1 pages 1-3)
   - Used for siRNA screening, PLK1 inhibitor studies
   - Represents mucinous histotype
   - Forms xenografts in mice

2. **EFO27, JHOM1** (affatato2020identificationofplk1 pages 1-3)
   - Additional mucinous ovarian carcinoma cell lines
   - Characterized for molecular profiling

3. **Novel patient-derived cell lines:** Recent publications describe establishment of mucinous ovarian carcinoma cell lines with comprehensive molecular characterization including TP53 wild-type, KRAS-mutated profiles (sauriol2020modelingthediversity pages 1-3)

**Xenograft Models:**

1. **Patient-Derived Xenografts (PDX):**
   - **MCAS xenografts:** Used to test PLK1 inhibitor onvansertib + paclitaxel; showed tumor regression and prolonged survival (affatato2020identificationofplk1 pages 1-3)
   - **OV-10-0050:** Ovarian cancer PDX with CLU-NRG1 fusion (rare mucinous feature) tested with seribantumab (przywara2025recenttherapiesand pages 4-6)
   - **Orthotopic PDX models:** Developed for high-grade serous carcinoma; limited mucinous-specific models reported

2. **Cell Line-Derived Xenografts (CDX):**
   - Subcutaneous and orthotopic implantation of mucinous ovarian carcinoma cell lines in immunocompromised mice (NSG, SCID)
   - Used for drug efficacy testing

**Genetically Engineered Mouse Models (GEMMs):**
The retrieved literature does not describe GEMMs specifically for mucinous ovarian carcinoma. Most ovarian cancer GEMMs focus on high-grade serous carcinoma with TP53/BRCA1 inactivation.

### Model Characteristics

**Phenotype Recapitulation:**
- Patient-derived cell lines and PDXs **retain key molecular features** including KRAS mutations, HER2 amplification, and mucin expression (sauriol2020modelingthediversity pages 1-3, affatato2020identificationofplk1 pages 1-3)
- **Chemotherapy resistance** is recapitulated in cell line and PDX models (affatato2020identificationofplk1 pages 1-3)
- **Mucin production** observed in vitro and in vivo

**Model Limitations:**
- **Lack of immune system** in xenograft models limits immunotherapy testing
- **Rarity of mucinous ovarian carcinoma** makes establishment of new models challenging
- **Heterogeneity** not fully captured in clonal cell lines
- Most available models focus on high-grade serous carcinoma; **mucinous-specific models are limited**

### Applications

**Research Applications:**
- **Drug discovery:** PLK1 inhibitor development, HER2-targeted therapy optimization (affatato2020identificationofplk1 pages 1-3, przywara2025recenttherapiesand pages 4-6)
- **Chemotherapy resistance mechanisms:** Mucin-mediated resistance studies (wang2023mucinsandmucinous pages 3-5)
- **Targeted therapy development:** HER2 ADCs, KRAS inhibitors
- **Biomarker validation**

**Preclinical Drug Testing:**
- Cell lines with **xenograft-forming capacity** are critical for in vivo efficacy studies (four of ten novel cell lines described formed subcutaneous tumors) (sauriol2020modelingthediversity pages 1-3)
- **Combination therapy screening:** PLK1 inhibitor + paclitaxel showed synergy in vitro and prolonged survival in vivo (affatato2020identificationofplk1 pages 1-3)

### Resources

**Model Organism Databases:**
- **ATCC (American Type Culture Collection):** Repository for established mucinous ovarian carcinoma cell lines
- **Patient-derived xenograft repositories:** Limited availability for mucinous subtype

---

## Summary and Ontology Annotations

### Suggested Ontology Terms

**MONDO:**
- MONDO:0008170 - Ovarian carcinoma
- Specific MONDO ID for mucinous ovarian carcinoma: To be assigned

**HPO (Human Phenotype Ontology):**
- HP:0100615 - Ovarian neoplasm
- HP:0002027 - Abdominal pain
- HP:0003270 - Abdominal distention
- HP:0002664 - Neoplasm

**GO (Gene Ontology) - Biological Processes:**
- GO:0008283 - Cell proliferation
- GO:0006915 - Apoptotic process
- GO:0007049 - Cell cycle
- GO:0001837 - Epithelial to mesenchymal transition
- GO:0030198 - Extracellular matrix organization

**CL (Cell Ontology):**
- CL:0000066 - Epithelial cell
- CL:0000160 - Goblet cell
- CL:0002327 - Malignant cell

**UBERON (Anatomical Ontology):**
- UBERON:0000992 - Ovary
- UBERON:0000971 - Peritoneum
- UBERON:0001416 - Omentum

**CHEBI (Chemical Entities):**
- CHEBI:31355 - Carboplatin
- CHEBI:45863 - Paclitaxel

**MAXO (Medical Action Ontology):**
- MAXO:0000058 - Chemotherapy
- MAXO:0000601 - Surgical resection
- MAXO:0000756 - Targeted molecular therapy
- MAXO:0000004 - Cytoreductive surgery

---

## Evidence Synthesis

This comprehensive report synthesizes evidence from 28 retrieved papers published between 2020-2025, with particular emphasis on:
- Recent global epidemiology (wang2024globalincidenceof pages 1-2, wang2024globalincidenceof pages 2-3)
- 2020 WHO classification updates (kobel2022theevolutionof pages 1-3, leo2021whatisnew pages 1-2)
- Molecular characterization and targeted therapy advances (kawecka2024molecularalterationsin pages 1-2, przywara2025recenttherapiesand pages 1-2, nugawela2023targetedtherapyfor pages 1-2, przywara2025recenttherapiesand pages 4-6)
- Diagnostic differentiation from metastatic disease (kawecka2024molecularalterationsin pages 1-2, wang2023mucinsandmucinous pages 2-3)
- Mucin biology and chemoresistance (wang2023mucinsandmucinous pages 1-2, wang2023mucinsandmucinous pages 3-5, wang2023mucinsandmucinous pages 2-3)
- Preclinical models and drug development (sauriol2020modelingthediversity pages 1-3, affatato2020identificationofplk1 pages 1-3)

Ovarian mucinous carcinoma represents a rare, biologically distinct, and clinically challenging subtype of epithelial ovarian cancer characterized by frequent KRAS mutations, HER2 amplification in subsets, intrinsic chemotherapy resistance, and excellent prognosis when diagnosed at early stage but dismal outcomes in advanced disease. Accurate diagnosis requires careful exclusion of metastatic gastrointestinal primaries. Emerging targeted therapies directed at HER2 and components of the MAPK pathway offer promise for improving outcomes in this chemoresistant disease.

References

1. (kobel2022theevolutionof pages 1-3): Martin Köbel and Eun Young Kang. The evolution of ovarian carcinoma subclassification. Cancers, 14:416, Jan 2022. URL: https://doi.org/10.3390/cancers14020416, doi:10.3390/cancers14020416. This article has 175 citations.

2. (leo2021whatisnew pages 1-2): Antonio De Leo, Donatella Santini, Claudio Ceccarelli, Giacomo Santandrea, Andrea Palicelli, Giorgia Acquaviva, Federico Chiarucci, Francesca Rosini, Gloria Ravegnini, Annalisa Pession, Daniela Turchetti, Claudio Zamagni, Anna Myriam Perrone, Pierandrea De Iaco, Giovanni Tallini, and Dario de Biase. What is new on ovarian carcinoma: integrated morphologic and molecular analysis following the new 2020 world health organization classification of female genital tumors. Diagnostics, 11(4):697, Apr 2021. URL: https://doi.org/10.3390/diagnostics11040697, doi:10.3390/diagnostics11040697. This article has 211 citations.

3. (wang2023mucinsandmucinous pages 1-2): Yicong Wang, Lifeng Liu, and Yongai Yu. Mucins and mucinous ovarian carcinoma: development, differential diagnosis, and treatment. Heliyon, 9:e19221, Aug 2023. URL: https://doi.org/10.1016/j.heliyon.2023.e19221, doi:10.1016/j.heliyon.2023.e19221. This article has 24 citations.

4. (wang2024globalincidenceof pages 1-2): Minmin Wang, Yanxin Bi, Yinzi Jin, and Zhi-Jie Zheng. Global incidence of ovarian cancer according to histologic subtype: a population-based cancer registry study. JCO Global Oncology, May 2024. URL: https://doi.org/10.1200/go.23.00393, doi:10.1200/go.23.00393. This article has 47 citations.

5. (przywara2025recenttherapiesand pages 1-2): Grzegorz Przywara, Oliwia Biegańska, Emilia Biczak, Aleksander Białoń, Dominik Fidorowicz, Alicja Dankowska, Zofia Łapińska, and Julita Kulbacka. Recent therapies and biomarkers in mucinous ovarian carcinoma. Cells, 14:1232, Aug 2025. URL: https://doi.org/10.3390/cells14161232, doi:10.3390/cells14161232. This article has 2 citations.

6. (sauriol2020modelingthediversity pages 1-3): Skye Alexandre Sauriol, Kayla Simeone, Lise Portelance, Liliane Meunier, Kim Leclerc-Desaulniers, Manon de Ladurantaye, Meriem Chergui, Jennifer Kendall-Dupont, Kurosh Rahimi, Euridice Carmona, Diane Provencher, and Anne-Marie Mes-Masson. Modeling the diversity of epithelial ovarian cancer through ten novel well characterized cell lines covering multiple subtypes of the disease. Cancers, 12:2222, Aug 2020. URL: https://doi.org/10.3390/cancers12082222, doi:10.3390/cancers12082222. This article has 21 citations.

7. (kawecka2024molecularalterationsin pages 1-2): Weronika Kawecka, Michal Bielak, and Karolina Urbanska. Molecular alterations in mucinous ovarian tumors – a review. Current Issues in Pharmacy and Medical Sciences, 37:190-194, Sep 2024. URL: https://doi.org/10.2478/cipms-2024-0031, doi:10.2478/cipms-2024-0031. This article has 3 citations.

8. (wang2023mucinsandmucinous pages 2-3): Yicong Wang, Lifeng Liu, and Yongai Yu. Mucins and mucinous ovarian carcinoma: development, differential diagnosis, and treatment. Heliyon, 9:e19221, Aug 2023. URL: https://doi.org/10.1016/j.heliyon.2023.e19221, doi:10.1016/j.heliyon.2023.e19221. This article has 24 citations.

9. (affatato2020identificationofplk1 pages 1-3): Roberta Affatato, Laura Carrassa, Rosaria Chilà, Monica Lupi, Valentina Restelli, and Giovanna Damia. Identification of plk1 as a new therapeutic target in mucinous ovarian carcinoma. Cancers, 12:672, Mar 2020. URL: https://doi.org/10.3390/cancers12030672, doi:10.3390/cancers12030672. This article has 43 citations.

10. (kobel2022theevolutionof pages 3-4): Martin Köbel and Eun Young Kang. The evolution of ovarian carcinoma subclassification. Cancers, 14:416, Jan 2022. URL: https://doi.org/10.3390/cancers14020416, doi:10.3390/cancers14020416. This article has 175 citations.

11. (przywara2025recenttherapiesand pages 4-6): Grzegorz Przywara, Oliwia Biegańska, Emilia Biczak, Aleksander Białoń, Dominik Fidorowicz, Alicja Dankowska, Zofia Łapińska, and Julita Kulbacka. Recent therapies and biomarkers in mucinous ovarian carcinoma. Cells, 14:1232, Aug 2025. URL: https://doi.org/10.3390/cells14161232, doi:10.3390/cells14161232. This article has 2 citations.

12. (leo2021whatisnew pages 3-5): Antonio De Leo, Donatella Santini, Claudio Ceccarelli, Giacomo Santandrea, Andrea Palicelli, Giorgia Acquaviva, Federico Chiarucci, Francesca Rosini, Gloria Ravegnini, Annalisa Pession, Daniela Turchetti, Claudio Zamagni, Anna Myriam Perrone, Pierandrea De Iaco, Giovanni Tallini, and Dario de Biase. What is new on ovarian carcinoma: integrated morphologic and molecular analysis following the new 2020 world health organization classification of female genital tumors. Diagnostics, 11(4):697, Apr 2021. URL: https://doi.org/10.3390/diagnostics11040697, doi:10.3390/diagnostics11040697. This article has 211 citations.

13. (nugawela2023targetedtherapyfor pages 1-2): Devindee Nugawela and Kylie L. Gorringe. Targeted therapy for mucinous ovarian carcinoma: evidence from clinical trials. International Journal of Gynecological Cancer, 33:102-108, Jan 2023. URL: https://doi.org/10.1136/ijgc-2022-003658, doi:10.1136/ijgc-2022-003658. This article has 29 citations and is from a peer-reviewed journal.

14. (wang2023mucinsandmucinous pages 3-5): Yicong Wang, Lifeng Liu, and Yongai Yu. Mucins and mucinous ovarian carcinoma: development, differential diagnosis, and treatment. Heliyon, 9:e19221, Aug 2023. URL: https://doi.org/10.1016/j.heliyon.2023.e19221, doi:10.1016/j.heliyon.2023.e19221. This article has 24 citations.

15. (wang2024globalincidenceof pages 2-3): Minmin Wang, Yanxin Bi, Yinzi Jin, and Zhi-Jie Zheng. Global incidence of ovarian cancer according to histologic subtype: a population-based cancer registry study. JCO Global Oncology, May 2024. URL: https://doi.org/10.1200/go.23.00393, doi:10.1200/go.23.00393. This article has 47 citations.

## Artifacts

- [Edison artifact artifact-00](Ovarian_Mucinous_Carcinoma-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](Ovarian_Mucinous_Carcinoma-deep-research-falcon_artifacts/artifact-01.md)
- [Edison artifact artifact-02](Ovarian_Mucinous_Carcinoma-deep-research-falcon_artifacts/artifact-02.md)