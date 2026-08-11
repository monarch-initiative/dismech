---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-23T15:37:59.714343'
end_time: '2026-06-23T15:56:31.141446'
duration_seconds: 1111.43
template_file: templates\disease_pathophysiology_research.md
template_variables:
  disease_name: BEST1-Related Dominant Retinopathy
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 40
artifact_count: 3
artifact_sources:
  edison_answer_artifacts: 3
artifacts:
- filename: artifact-00.md
  path: BEST1-Related_Dominant_Retinopathy-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: BEST1-Related_Dominant_Retinopathy-deep-research-falcon_artifacts/artifact-01.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-01
- filename: artifact-02.md
  path: BEST1-Related_Dominant_Retinopathy-deep-research-falcon_artifacts/artifact-02.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-02
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** BEST1-Related Dominant Retinopathy
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **BEST1-Related Dominant Retinopathy** covering all of the
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
- **Disease Name:** BEST1-Related Dominant Retinopathy
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **BEST1-Related Dominant Retinopathy** covering all of the
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


# Comprehensive Research Report: BEST1-Related Dominant Retinopathy

---

## 1. Disease Information

### Overview

BEST1-related dominant retinopathy encompasses a group of inherited retinal dystrophies caused by heterozygous pathogenic variants in the BEST1 gene (formerly VMD2), which encodes bestrophin-1, a calcium-activated chloride channel expressed exclusively in the retinal pigment epithelium (RPE) (amato2023genetherapyin pages 2-3, navinesferrer2022impairedbestrophinchannel pages 1-2). The most common dominant phenotype is Best vitelliform macular dystrophy (BVMD, or Best disease), first described by Dr. Friedrich Best in 1905 (haldrup2025genetherapystrategies pages 3-5). BVMD is characterized by the bilateral accumulation of yellow, lipofuscin-rich vitelliform material beneath the neurosensory retina in the macular region, leading to progressive central visual impairment (beryozkin2024bestdiseaseglobal pages 1-2, bianco2024multimodalimagingin pages 1-2).

Other BEST1-associated dominant retinopathies include adult-onset foveomacular vitelliform dystrophy (AOFVD/AVMD) and autosomal dominant vitreoretinochoroidopathy (ADVIRC) (yang2023best1novelmutation pages 1-2, amato2023genetherapyin pages 1-2). While biallelic BEST1 variants cause autosomal recessive bestrophinopathy (ARB), this report focuses on the dominantly inherited forms.

### Disease Identifiers and Synonyms

The following table summarizes the key identifiers, synonyms, and related phenotypes for BEST1-related dominant retinopathy:

| Identifier Type | Value/ID | Notes |
|---|---|---|
| Preferred disease name | BEST1-related dominant retinopathy | Umbrella term for autosomal-dominant BEST1-associated retinal disease, most commonly Best vitelliform macular dystrophy (BVMD/Best disease); other dominant phenotypes include adult-onset foveomacular vitelliform dystrophy (AOFVD/AVMD) and autosomal dominant vitreoretinochoroidopathy (ADVIRC) (amato2023genetherapyin pages 2-3, yang2023best1novelmutation pages 1-2, beryozkin2024bestdiseaseglobal pages 1-2, amato2023genetherapyin pages 1-2) |
| OMIM disease | 153700 | Best vitelliform macular dystrophy / Best disease; the common dominant BEST1 phenotype (yang2023best1novelmutation pages 1-2, beryozkin2024bestdiseaseglobal pages 1-2) |
| MONDO disease | MONDO_0007931 | Vitelliform macular dystrophy 2; Open Targets links this disease to BEST1 as the top associated target (OpenTargets Search: -BEST1) |
| Orphanet disease | Orphanet_1243 | Best vitelliform macular dystrophy (OpenTargets Search: -BEST1) |
| MeSH | D057826 | Vitelliform Macular Dystrophy; used in the ClinicalTrials.gov natural-history record for BEST1 VMD (NCT05809635 chunk 1) |
| ICD-10 | Not uniquely established from retrieved evidence | BEST1-related dominant retinopathy/BVMD is generally grouped under hereditary retinal dystrophy/macular degeneration coding in practice; a disease-specific ICD-10 code was not confirmed in the retrieved sources |
| Gene symbol | BEST1 | HGNC-approved symbol for bestrophin 1; causative gene for dominant and recessive bestrophinopathies (OpenTargets Search: -BEST1, amato2023genetherapyin pages 2-3, yang2023best1novelmutation pages 1-2) |
| Gene OMIM | 607854 | BEST1 gene entry (formerly VMD2) (yang2023best1novelmutation pages 1-2) |
| Ensembl gene | ENSG00000167995 | Open Targets identifier for BEST1 (OpenTargets Search: -BEST1) |
| Protein | Bestrophin-1 | 585-amino-acid, homopentameric calcium-activated chloride channel expressed in retinal pigment epithelium (RPE) (amato2023genetherapyin pages 2-3, navinesferrer2022impairedbestrophinchannel pages 1-2, amato2023genetherapyin pages 1-2) |
| Chromosomal locus | 11q13 / 11q12-q13.1 | BEST1 is reported at chromosome 11q13 in clinical literature; the interventional trial requires genetic confirmation on chromosome 11q12-q13.1 (nowomiejska2022diseaseexpressioncaused pages 1-2, NCT07185256 chunk 1) |
| Related dominant phenotype | ADVIRC; OMIM 193220; MONDO_0008662 | Autosomal dominant vitreoretinochoroidopathy is another dominant BEST1-associated phenotype (yang2023best1novelmutation pages 1-2, OpenTargets Search: -BEST1) |
| Related dominant phenotype | Adult-onset vitelliform macular dystrophy / AOFVD / AVMD | Adult-onset dominant vitelliform phenotype associated in some cases with BEST1 variants; typically presents after age 40 (yang2023best1novelmutation pages 1-2, amato2023genetherapyin pages 1-2) |
| Related recessive phenotype | ARB; OMIM 611809; MONDO_0012733 | Autosomal recessive bestrophinopathy is part of the BEST1 disease spectrum but is not the dominant form (yang2023best1novelmutation pages 1-2, OpenTargets Search: -BEST1) |
| Related phenotype | Retinitis pigmentosa 50; MONDO_0013175 | BEST1 is also associated with RP50 in curated disease-target resources (OpenTargets Search: -BEST1) |
| Common synonym | Best disease | Widely used synonym for BVMD (yang2023best1novelmutation pages 1-2, beryozkin2024bestdiseaseglobal pages 1-2) |
| Common synonym | BVMD | Standard abbreviation for Best vitelliform macular dystrophy (amato2023genetherapyin pages 2-3, beryozkin2024bestdiseaseglobal pages 1-2) |
| Common synonym | VMD / VMD2-associated disease | Historical nomenclature linked to vitelliform macular dystrophy and the former BEST1 name VMD2 (yang2023best1novelmutation pages 1-2, NCT07185256 chunk 1) |
| Common synonym | Bestrophinopathy / BEST1-related bestrophinopathy | Collective term for the phenotypic spectrum caused by BEST1 variants (amato2023genetherapyin pages 2-3, amato2023genetherapyin pages 1-2) |
| Inheritance | Autosomal dominant with variable expressivity and incomplete/reduced penetrance | Characteristic for BVMD and several other dominant BEST1 phenotypes (grewal2021bestrophinopathiesperspectiveson pages 1-2, beryozkin2024bestdiseaseglobal pages 1-2, nowomiejska2022diseaseexpressioncaused pages 1-2) |


*Table: This table compiles the main disease and gene identifiers used for BEST1-related dominant retinopathy, centered on Best vitelliform macular dystrophy. It also summarizes key synonyms, related BEST1 phenotypes, and inheritance details useful for database curation.*

**Common Synonyms:** Best disease, Best vitelliform macular dystrophy (BVMD), VMD2-associated macular dystrophy, bestrophinopathy, BEST1-related bestrophinopathy.

**Information Sources:** This report synthesizes data from aggregated disease-level resources including OMIM, Orphanet, OpenTargets (OpenTargets Search: -BEST1), ClinicalTrials.gov (NCT05809635 chunk 1, NCT07185256 chunk 1), and primary peer-reviewed literature.

---

## 2. Etiology

### Disease Causal Factors

BEST1-related dominant retinopathy is a Mendelian genetic disorder caused by heterozygous pathogenic variants in the BEST1 gene located on chromosome 11q12-q13.1 (nowomiejska2022diseaseexpressioncaused pages 1-2, NCT07185256 chunk 1). The disease is exclusively genetic in origin, with no known environmental or infectious causes.

### Genetic Risk Factors

- **Causal Gene:** BEST1 (HGNC symbol; Ensembl: ENSG00000167995; OMIM gene: 607854) (OpenTargets Search: -BEST1, yang2023best1novelmutation pages 1-2).
- **Variant Spectrum:** Over 250–300 individual pathogenic mutations have been identified in BEST1, with the majority being missense variants in functional domains of the protein (grewal2021bestrophinopathiesperspectiveson pages 1-2, nowomiejska2022diseaseexpressioncaused pages 1-2). In an 18-year single-center DNA diagnostics study of over 7,000 inherited retinal dystrophy patients, BEST1 accounted for 7.8% of all disease-causing variants, making it the second most frequently implicated gene after ABCA4 (nowomiejska2022diseaseexpressioncaused pages 1-2).
- **Critical Conserved Domains:** Disease-causing dominant missense mutations cluster in transmembrane domains and the intracellular Ca²⁺-binding domain of the BEST1 protein (beryozkin2024bestdiseaseglobal pages 1-2). Dominant variants specifically cluster around the Ca²⁺-clasp and gating apparatus regions of the ion pore (haldrup2025genetherapystrategies pages 1-3).
- **Inheritance Pattern:** Autosomal dominant with variable expressivity and incomplete penetrance (grewal2021bestrophinopathiesperspectiveson pages 1-2, beryozkin2024bestdiseaseglobal pages 1-2, haldrup2025genetherapystrategies pages 3-5).

### Protective and Environmental Factors

No specific genetic protective factors, modifier genes, or environmental factors that influence disease risk or expression have been conclusively identified for BEST1-related dominant retinopathy in the current literature. The phenotypic variability observed is attributed primarily to the specific pathogenic variant and stochastic biological factors rather than known gene-environment interactions (grewal2021bestrophinopathiesperspectiveson pages 1-2, nowomiejska2022diseaseexpressioncaused pages 1-2).

---

## 3. Phenotypes

### Clinical Features and Staging

BVMD progresses through five classic clinical stages, originally described by Gass and subsequently refined with modern imaging:

| Stage Number | Stage Name | Fundus Appearance | OCT Findings | FAF Findings | Visual Acuity | Clinical Description |
|---|---|---|---|---|---|---|
| 1 | Previtelliform / Subclinical | Fundus may appear normal or show only subtle RPE irregularity; early macular change without classic yellow lesion (bianco2024multimodalimagingin pages 1-2, padhy2026reviewofthe pages 2-4, amato2023genetherapyin pages 2-3, haldrup2025genetherapystrategies pages 3-5) | Subtle OCT abnormalities; early disturbance at the photoreceptor–RPE interdigitation zone; heightened RPE–outer segment reflectance may be present (padhy2026reviewofthe pages 2-4, amato2023genetherapyin pages 2-3) | Near-infrared autofluorescence may help identify early disease; FAF can be minimal or only subtly abnormal before obvious vitelliform deposition (padhy2026reviewofthe pages 2-4, amato2023genetherapyin pages 2-3) | Usually normal or near-normal vision (haldrup2025genetherapystrategies pages 3-5) | Earliest clinically recognized stage; RPE-photoreceptor interaction is already abnormal, but overt lesion formation may not yet be visible on ophthalmoscopy (padhy2026reviewofthe pages 2-4, amato2023genetherapyin pages 2-3) |
| 2 | Vitelliform | Classic yellow, dome-shaped “egg-yolk” lesion in the macula; central vitelliform material beneath the neurosensory retina (bianco2024multimodalimagingin pages 1-2, nowomiejska2022diseaseexpressioncaused pages 1-2, amato2023genetherapyin pages 2-3, haldrup2025genetherapystrategies pages 3-5) | Dome-shaped subretinal hyperreflective material/elevation; raised ellipsoid/interdigitation zones; subretinal deposit corresponding to vitelliform lesion (amato2023genetherapyin pages 2-3, yang2023best1novelmutation pages 4-5) | Marked hyperautofluorescence corresponding to vitelliform material (padhy2026reviewofthe pages 2-4, yang2023best1novelmutation pages 4-5) | Mild visual loss, though many patients still retain good central acuity; symptoms may include photophobia, metamorphopsia, or nyctalopia (haldrup2025genetherapystrategies pages 3-5) | Hallmark stage of BVMD with lipofuscin-rich/unphagocytosed outer segment material accumulation in the macula (bianco2024multimodalimagingin pages 1-2, padhy2026reviewofthe pages 2-4) |
| 3 | Pseudohypopyon | Yellow material gravitates inferiorly within the lesion, creating a fluid level / layered appearance (padhy2026reviewofthe pages 2-4, amato2023genetherapyin pages 2-3, haldrup2025genetherapystrategies pages 3-5) | Layering of vitelliform material within subretinal space; inferior pooling of hyperreflective material (amato2023genetherapyin pages 2-3) | Persistent hyperautofluorescence, often redistributed according to layered material (amato2023genetherapyin pages 2-3, haldrup2025genetherapystrategies pages 3-5) | Variable; often still relatively preserved but may begin to decline (padhy2026reviewofthe pages 2-4, haldrup2025genetherapystrategies pages 3-5) | Transitional stage in which accumulated material separates and settles inferiorly, producing the “pseudohypopyon” appearance (padhy2026reviewofthe pages 2-4, amato2023genetherapyin pages 2-3) |
| 4 | Vitelliruptive / “Scrambled-egg” | Fragmented, irregular, clumped yellow deposits with “scrambled-egg” appearance; lesion disintegration (padhy2026reviewofthe pages 2-4, nowomiejska2022diseaseexpressioncaused pages 1-2, haldrup2025genetherapystrategies pages 3-5, grewal2021bestrophinopathiesperspectiveson pages 1-2) | Clumped/disrupted hyperreflective material; increasing outer retinal disorganization, ONL thinning, and ellipsoid zone disruption (bianco2024multimodalimagingin pages 1-2, amato2023genetherapyin pages 2-3) | Mixed or irregular autofluorescence as material fragments and redistributes (amato2023genetherapyin pages 2-3) | Visual acuity often declines substantially compared with earlier stages (haldrup2025genetherapystrategies pages 3-5) | Represents breakdown/resorption of the vitelliform lesion with increasing photoreceptor dysfunction and structural damage (bianco2024multimodalimagingin pages 1-2, haldrup2025genetherapystrategies pages 3-5) |
| 5 | Atrophic / Fibroatrophic (Atrophic/Fibrotic) | Macular atrophy, fibrosis, or scar-like end-stage lesion; may be complicated by choroidal neovascularization (bianco2024multimodalimagingin pages 1-2, padhy2026reviewofthe pages 2-4, amato2023genetherapyin pages 2-3, haldrup2025genetherapystrategies pages 3-5) | Loss of outer retinal layers with photoreceptor loss, RPE atrophy, and advanced structural collapse; possible fibroatrophic change (padhy2026reviewofthe pages 2-4, amato2023genetherapyin pages 2-3) | Reduced/heterogeneous autofluorescence in atrophic areas; prior hyperautofluorescent material may be lost as atrophy advances (bianco2024multimodalimagingin pages 1-2, amato2023genetherapyin pages 2-3) | Severe, often irreversible visual loss in advanced disease (haldrup2025genetherapystrategies pages 3-5) | End stage characterized by RPE death, photoreceptor loss, and possible CNV or fibrosis; central vision impairment becomes most pronounced (padhy2026reviewofthe pages 2-4, haldrup2025genetherapystrategies pages 3-5) |


*Table: This table summarizes the five classic clinical stages of Best vitelliform macular dystrophy, integrating fundus, OCT, FAF, and functional features. It is useful for disease characterization, differential diagnosis, and structuring natural history or trial-readiness annotations.*

### Key Phenotypic Features

- **Vitelliform macular lesion:** Bilateral, yellow, "egg-yolk" appearance at the macula; the hallmark of BVMD (navinesferrer2022impairedbestrophinchannel pages 1-2, bianco2024multimodalimagingin pages 1-2). HPO: HP:0007754 (Macular dystrophy).
- **Reduced visual acuity:** Progressive central vision loss, particularly in advanced stages (haldrup2025genetherapystrategies pages 3-5). HPO: HP:0000572 (Visual loss).
- **Metamorphopsia:** Distortion of central vision reported in some patients (haldrup2025genetherapystrategies pages 3-5, shi2023comprehensivegeneticanalysis pages 5-8). HPO: HP:0012508 (Metamorphopsia).
- **Photophobia:** Reported in vitelliform stage (haldrup2025genetherapystrategies pages 3-5). HPO: HP:0000613 (Photophobia).
- **Nyctalopia (night blindness):** Reported variably (haldrup2025genetherapystrategies pages 3-5, shi2023comprehensivegeneticanalysis pages 5-8). HPO: HP:0000662 (Nyctalopia).
- **Abnormal EOG:** Markedly reduced Arden ratio (≤1.5); pathognomonic (bianco2024multimodalimagingin pages 1-2, haldrup2025genetherapystrategies pages 3-5). HPO: HP:0000495 (Abnormality of the electrooculogram).
- **Lipofuscin accumulation:** Subretinal deposition of lipofuscin and unphagocytosed photoreceptor outer segments (bianco2024multimodalimagingin pages 1-2). HPO: HP:0007807 (Vitelliform (egg-yolk) macular lesion).
- **Choroidal neovascularization (CNV):** May complicate late-stage disease (bianco2024multimodalimagingin pages 1-2, padhy2026reviewofthe pages 2-4). HPO: HP:0011506 (Choroidal neovascularization).
- **Hyperopia and astigmatism:** Associated refractive errors have been reported (haldrup2025genetherapystrategies pages 3-5).

### Phenotype Characteristics

- **Age of onset:** Typically childhood to early adulthood (ages 3–15 years for BVMD); AVMD presents after age 40 (yang2023best1novelmutation pages 1-2, navinesferrer2022impairedbestrophinchannel pages 1-2).
- **Severity:** Highly variable, even among family members carrying the same mutation (grewal2021bestrophinopathiesperspectiveson pages 1-2, yang2023best1novelmutation pages 4-5).
- **Progression:** Slow and unpredictable; not all patients progress through all stages sequentially (amato2023genetherapyin pages 2-3, bianco2024multimodalimagingin pages 1-2).
- **Quality of life:** Central vision loss affects reading, driving, and fine visual tasks; 75% of patients under age 40 maintain visual acuity of 6/12 (20/40) or better in at least one eye (haldrup2025genetherapystrategies pages 3-5).

---

## 4. Genetic/Molecular Information

### Causal Gene

**BEST1** (bestrophin 1): Located on chromosome 11q12-q13.1, comprising 11 exons (of which 10 encode the protein), the gene encodes bestrophin-1, a 585-amino acid, 68 kDa protein that forms a homopentameric calcium-activated chloride channel (CaCC) (amato2023genetherapyin pages 2-3, navinesferrer2022impairedbestrophinchannel pages 1-2, amato2023genetherapyin pages 1-2).

### Pathogenic Variants

- **Variant types:** Predominantly missense variants for dominant forms; nonsense, frameshift, splice-site, and structural variants are more common in recessive disease (haldrup2025genetherapystrategies pages 1-3, nowomiejska2022diseaseexpressioncaused pages 1-2).
- **Variant classification:** Pathogenic and likely pathogenic per ACMG/AMP guidelines; the BIRD-1 clinical trial (NCT07185256) requires ACMG/AMP-classified pathogenic or likely pathogenic variants for enrollment (NCT07185256 chunk 1).
- **Functional consequences:** Three major categories have been identified (amato2023genetherapyin pages 1-2, haldrup2025genetherapystrategies pages 5-7):
  - **Loss of function (LOF):** Destabilized protein, non-functional channels, or reduced function; can occur throughout the gene.
  - **Dominant negative (DN):** Mutant subunits incorporate into pentameric channels and impair overall channel function; since BEST1 forms pentamers containing both wild-type and mutant subunits, even a 4:1 WT:mutant ratio can cause substantial dysfunction (navinesferrer2022impairedbestrophinchannel pages 10-11). This is the most common mechanism in dominant BVMD.
  - **Gain of function (GOF):** Increased or aberrant channel activity; a smaller subset of variants, exemplified by p.Pro77Ser which increases anion permeability (navinesferrer2022impairedbestrophinchannel pages 10-11).
- **Allelic expression imbalance:** At the BEST1 locus, mutant alleles may be transcribed at higher levels than wildtype alleles in human RPE cells, promoting dominant negative effects (haldrup2025genetherapystrategies pages 5-7).
- **Somatic vs. germline:** All described BEST1 pathogenic variants are germline in origin.

### Specific Variant Examples

Multiple specific pathogenic variants have been characterized functionally: R218C shows correct basolateral localization but impaired function; W93C and V9M show intracellular mislocalization; Y85H, Q96R, L100R, Y227N, T6P, L21V, W24C, L224M, T237R, F305S, and V311G show trafficking errors on the cytoplasmic face; S79C, F80L, L82V, and A243T affect membrane domain function (padhy2026reviewofthe pages 2-4).

### Modifier Genes and Epigenetics

No confirmed modifier genes or disease-associated epigenetic changes have been identified specifically for BEST1-related dominant retinopathy in the current literature.

---

## 5. Environmental Information

No environmental factors, lifestyle factors, or infectious agents have been identified as contributing to BEST1-related dominant retinopathy. This is a purely genetic, Mendelian disorder.

---

## 6. Mechanism / Pathophysiology

### Molecular Pathways

Bestrophin-1 functions as a calcium-dependent chloride channel (CaCC) that controls chloride-ion current across the RPE basolateral membrane (haldrup2025genetherapystrategies pages 1-3). The protein's Ca²⁺-clasps regulate calcium-dependent opening and closing through conformational changes. Additionally, bestrophin-1 regulates intracellular calcium signaling, calcium release from endoplasmic reticulum stores, and cell volume homeostasis in RPE cells (haldrup2025genetherapystrategies pages 3-5, amato2023genetherapyin pages 2-3).

**Relevant GO Biological Process terms:**
- GO:0005229 (intracellular calcium activated chloride channel activity)
- GO:0006821 (chloride transport)
- GO:0007601 (visual perception)
- GO:0055085 (transmembrane transport)

### Causal Chain from Initial Trigger to Clinical Manifestation

1. **Initial trigger:** Heterozygous pathogenic variant in BEST1 leads to production of mutant bestrophin-1 subunits (amato2023genetherapyin pages 1-2).
2. **Protein dysfunction:** Mutant subunits incorporate into pentameric channel complexes, causing dominant negative effects (most commonly), loss of function, or gain of function depending on the specific variant (navinesferrer2022impairedbestrophinchannel pages 10-11, haldrup2025genetherapystrategies pages 5-7). Some variants cause protein mislocalization from the basolateral membrane to intracellular compartments (padhy2026reviewofthe pages 2-4).
3. **RPE dysfunction:** Impaired chloride transport disrupts RPE transepithelial potential (measured as reduced EOG light rise), fluid transport, and calcium homeostasis (padhy2026reviewofthe pages 2-4, haldrup2025genetherapystrategies pages 1-3).
4. **RPE-photoreceptor interaction failure:** Loss of normal apposition between RPE apical microvilli and photoreceptor outer segments leads to impaired phagocytosis of shed outer segments (navinesferrer2022impairedbestrophinchannel pages 11-13, bianco2024multimodalimagingin pages 1-2).
5. **Vitelliform material accumulation:** Unphagocytosed photoreceptor outer segments and lipofuscin accumulate in the subretinal space, forming the characteristic vitelliform lesion (bianco2024multimodalimagingin pages 1-2).
6. **Progressive photoreceptor damage:** Cone mosaic changes, outer nuclear layer thinning, and ellipsoid zone disruption develop over time (bianco2024multimodalimagingin pages 1-2).
7. **End-stage disease:** RPE death, photoreceptor loss, geographic atrophy, and potential choroidal neovascularization result in irreversible central vision loss (padhy2026reviewofthe pages 2-4, grewal2021bestrophinopathiesperspectiveson pages 1-2).

### Cell Types Involved

- **Retinal pigment epithelium (RPE):** Primary cell type expressing BEST1 and site of initial pathology. CL:0002586 (retinal pigment epithelial cell).
- **Cone photoreceptors:** Secondary damage from RPE dysfunction, particularly in the macula. CL:0000573 (cone photoreceptor cell).
- **Rod photoreceptors:** May also be affected in later stages. CL:0000604 (rod photoreceptor cell).

### Biochemical Abnormalities

- **Ion channel defect:** Impaired calcium-activated chloride channel activity at the RPE basolateral membrane (amato2023genetherapyin pages 2-3, navinesferrer2022impairedbestrophinchannel pages 10-11).
- **Calcium signaling disruption:** Altered intracellular calcium dynamics in RPE cells (amato2023genetherapyin pages 2-3).
- **Phagocytosis defect:** Impaired photoreceptor outer segment phagocytosis by RPE (navinesferrer2022impairedbestrophinchannel pages 11-13, xu2024ionchannelsresearch pages 4-5).
- **Transepithelial fluid transport deficiency:** Reduced subretinal fluid clearance (xu2024ionchannelsresearch pages 4-5).

---

## 7. Anatomical Structures Affected

### Organ Level

- **Primary organ:** Eye (UBERON:0000970)
- **Primary structure:** Retina (UBERON:0000966), specifically the macula (UBERON:0000053)
- **Body system:** Visual/nervous system

### Tissue and Cell Level

- **Retinal pigment epithelium (RPE):** Primary tissue directly affected; site of bestrophin-1 expression and initial pathology (UBERON:0001782) (amato2023genetherapyin pages 2-3, padhy2026reviewofthe pages 2-4).
- **Photoreceptor layer:** Secondary damage to cone and rod photoreceptors (UBERON:0001789) (bianco2024multimodalimagingin pages 1-2).
- **Subretinal space:** Site of vitelliform material accumulation (bianco2024multimodalimagingin pages 1-2).

### Subcellular Level

- **Basolateral plasma membrane:** Primary localization of bestrophin-1 (GO:0016323) (amato2023genetherapyin pages 2-3, padhy2026reviewofthe pages 2-4).
- **Endoplasmic reticulum:** Secondary localization of bestrophin-1; involved in calcium release regulation (GO:0005783) (amato2023genetherapyin pages 2-3, padhy2026reviewofthe pages 2-4).

### Localization

- **Bilateral involvement:** Typically bilateral and symmetrical, though asymmetric presentation occurs (haldrup2025genetherapystrategies pages 3-5).
- **Macular predominance:** Vitelliform lesions primarily affect the central macula, with some patients showing extramacular deposits (yang2023best1novelmutation pages 1-2, bianco2024multimodalimagingin pages 1-2).

---

## 8. Temporal Development

### Onset

- **Typical age of onset:** Childhood to early adulthood for BVMD (ages 3–15 years); AVMD presents after age 40 (yang2023best1novelmutation pages 1-2, navinesferrer2022impairedbestrophinchannel pages 1-2, nowomiejska2022diseaseexpressioncaused pages 1-2).
- **Onset pattern:** Insidious; pre-vitelliform stage may be detected on imaging before symptoms develop (padhy2026reviewofthe pages 2-4, amato2023genetherapyin pages 2-3).

### Progression

- **Disease course:** Slowly progressive over decades; photoreceptors can remain viable for extended periods despite subretinal material accumulation (amato2023genetherapyin pages 2-3, amato2023genetherapyin pages 6-7).
- **Progression rate:** Highly variable and unpredictable; not all patients progress through all five stages sequentially (bianco2024multimodalimagingin pages 1-2, amato2023genetherapyin pages 2-3).
- **Duration:** Chronic, lifelong condition.
- **Critical periods:** The slow progression provides a wide therapeutic window for gene therapy intervention, as central photoreceptors usually remain viable for decades (amato2023genetherapyin pages 2-3, amato2023genetherapyin pages 6-7).

---

## 9. Inheritance and Population

### Inheritance Pattern

- **Mode:** Autosomal dominant with variable expressivity and incomplete/reduced penetrance (grewal2021bestrophinopathiesperspectiveson pages 1-2, beryozkin2024bestdiseaseglobal pages 1-2, haldrup2025genetherapystrategies pages 3-5).
- **Penetrance:** Incomplete; many BEST1 pathogenic variants show reduced penetrance, meaning not all carriers develop clinical disease (grewal2021bestrophinopathiesperspectiveson pages 1-2).
- **Expressivity:** Highly variable, even within families carrying the same mutation; intrafamilial phenotypic diversity is a hallmark (grewal2021bestrophinopathiesperspectiveson pages 1-2, yang2023best1novelmutation pages 4-5).

### Epidemiology

- **Prevalence estimates:** Widely variable across studies:
  - General estimates range from 1:5,000 to 1:67,000 (grewal2021bestrophinopathiesperspectiveson pages 1-2, navinesferrer2022impairedbestrophinchannel pages 1-2, haldrup2025genetherapystrategies pages 3-5).
  - Israel: 1 in 127,000 overall; 1 in 76,000 among Arab Muslims; 1 in 145,000 among Jews (beryozkin2024bestdiseaseglobal pages 2-3, beryozkin2024bestdiseaseglobal pages 1-2).
  - Denmark: 0.8–1.5 per 100,000 (beryozkin2024bestdiseaseglobal pages 4-7).
  - Northern Sweden: 2 per 10,000 (beryozkin2024bestdiseaseglobal pages 4-7).
  - Minnesota (USA): 1:16,500 to 1:21,000 (beryozkin2024bestdiseaseglobal pages 4-7).
  - BVMD prevalence of approximately 1:50,000 has been cited (nowomiejska2022diseaseexpressioncaused pages 1-2).
- **Population variation:** Higher prevalence in populations with higher consanguinity rates (for recessive forms); Arab Muslim populations in Israel showed higher prevalence than Jewish populations (42% vs. ≤13.6% consanguinity rates) (beryozkin2024bestdiseaseglobal pages 7-8).
- **Founder effects:** Population-specific founder variants have been identified, including a founder variant c.867+97G>A in Chinese patients with ARB (allele frequency 16%) (shi2023comprehensivegeneticanalysis pages 5-8) and a founder variant p.Arg122Pro in Egyptian families (from Elbagoury et al. 2025).

### Sex Ratio

No significant sex predilection has been established for BEST1-related dominant retinopathy; the clinical trials include participants of all sexes (NCT05809635 chunk 1, NCT07185256 chunk 1).

---

## 10. Diagnostics

### Clinical Tests

- **Electrooculogram (EOG):** The hallmark diagnostic test; markedly reduced Arden ratio (typically ≤1.5, pathognomonic) reflecting impaired RPE function (bianco2024multimodalimagingin pages 1-2, nowomiejska2022diseaseexpressioncaused pages 1-2, haldrup2025genetherapystrategies pages 3-5). MAXO: MAXO:0000930 (electrooculography).
- **Full-field electroretinogram (ERG):** Usually normal in BVMD, distinguishing it from other retinal dystrophies; may show progressive amplitude reductions in advanced stages (bianco2024multimodalimagingin pages 1-2, padhy2026reviewofthe pages 2-4).
- **Multifocal ERG (mfERG):** Reduced central ring amplitudes correlating with subretinal fluid (padhy2026reviewofthe pages 2-4).
- **Optical coherence tomography (OCT):** Reveals subretinal hyperreflective material, dome-shaped lesions, outer retinal layer disruption, and cystoid changes; an OCT-based staging system has been developed (bianco2024multimodalimagingin pages 1-2, amato2023genetherapyin pages 2-3). MAXO: MAXO:0010034 (optical coherence tomography).
- **Fundus autofluorescence (FAF):** Intense hyperautofluorescence corresponding to vitelliform deposits; useful for disease monitoring (bianco2024multimodalimagingin pages 1-2, padhy2026reviewofthe pages 2-4, amato2023genetherapyin pages 2-3).
- **Near-infrared fundus autofluorescence (NIR-AF):** Helps identify pre-vitelliform stage changes (padhy2026reviewofthe pages 2-4).
- **Color fundus photography:** Classic "egg-yolk" yellow macular lesion appearance (bianco2024multimodalimagingin pages 1-2, yang2023best1novelmutation pages 4-5).
- **OCT angiography (OCTA):** Emerging role in detecting macular neovascularization, with a higher prevalence of non-exudative CNV in late stages (bianco2024multimodalimagingin pages 1-2).

### Genetic Testing

- **Recommended approach:** Molecular genetic confirmation is considered the gold standard for Best disease diagnosis due to variable clinical presentation (beryozkin2024bestdiseaseglobal pages 1-2).
- **Gene panels:** IRD panels including BEST1 variant testing are routinely used (NCT07185256 chunk 1).
- **Single gene testing:** Sanger sequencing of BEST1 coding exons (nowomiejska2022diseaseexpressioncaused pages 1-2, shi2023comprehensivegeneticanalysis pages 5-8).
- **Whole exome sequencing (WES):** Used for comprehensive diagnostic screening (beryozkin2024bestdiseaseglobal pages 1-2).
- **Whole genome sequencing (WGS):** Can detect deep intronic variants missed by standard approaches; three deep intronic variants (c.1101-491A>G, c.867+97G>A, c.867+97G>T) were identified through WGS in a Chinese cohort (shi2023comprehensivegeneticanalysis pages 5-8).

### Differential Diagnosis

Conditions to distinguish from BEST1-related dominant retinopathy include:
- Age-related macular degeneration (AMD)
- Adult-onset foveomacular vitelliform dystrophy (pattern dystrophy without BEST1 mutation)
- Central serous chorioretinopathy
- Stargardt disease (ABCA4-related)
- PRPH2-related vitelliform macular dystrophy
- IMPG1/IMPG2-related vitelliform macular dystrophy (OpenTargets Search: -BEST1)

---

## 11. Outcome/Prognosis

### Visual Prognosis

- Most patients experience slow visual decline over decades (amato2023genetherapyin pages 2-3, amato2023genetherapyin pages 6-7).
- Approximately 75% of patients under age 40 maintain best-corrected visual acuity of 6/12 (20/40) or better in at least one eye (haldrup2025genetherapystrategies pages 3-5).
- Visual acuity can range from near-normal to severe impairment depending on disease stage (haldrup2025genetherapystrategies pages 3-5).
- Central photoreceptors usually remain viable for decades despite subretinal material accumulation, providing a wide therapeutic window (amato2023genetherapyin pages 2-3, amato2023genetherapyin pages 6-7).

### Complications

- Choroidal neovascularization (CNV) may develop in late-stage disease, with OCTA studies showing a greater prevalence of non-exudative CNV than previously recognized (bianco2024multimodalimagingin pages 1-2).
- Macular atrophy and fibrosis represent end-stage disease (padhy2026reviewofthe pages 2-4, haldrup2025genetherapystrategies pages 3-5).
- Angle-closure glaucoma is primarily associated with recessive BEST1 disease rather than dominant forms (yang2023best1novelmutation pages 1-2).

### Life Expectancy

BEST1-related dominant retinopathy is not associated with reduced life expectancy; morbidity is limited to progressive visual impairment.

---

## 12. Treatment

### Current Treatments

Currently, no approved curative or disease-modifying treatments exist for any bestrophinopathy (haldrup2025genetherapystrategies pages 7-8, haldrup2025genetherapystrategies pages 1-3). Management is limited to:
- **Supportive care:** Low-vision aids, adaptive technologies, and occupational therapy.
- **Anti-VEGF therapy:** For secondary choroidal neovascularization (CNV) when present.
- **Monitoring:** Regular multimodal imaging follow-up.

### Experimental/Investigational Treatments

#### Gene Therapy

The following clinical trials are currently investigating or characterizing BEST1-related retinopathy for therapeutic development:

| NCT Number | Trial Name/Acronym | Phase | Sponsor | Status | Intervention | Enrollment | Key Details |
|---|---|---|---|---|---|---:|---|
| NCT07185256 | Safety and Tolerability of Subretinally Injected OPGx-BEST1 in Patients With BVMD or ARB / **BIRD-1** | Phase 1b/2a | Opus Genetics, Inc | Recruiting | One-time subretinal injection of **OPGx-BEST1** (codon-optimized full-length **hBEST1** under an RPE-specific/VMD2 promoter); dose exploration at **1.5E9 vg/eye** and **4.5E9 vg/eye** | 10 | First interventional gene-therapy trial identified here for BEST1 bestrophinopathies; open-label basket study in adults with **autosomal-dominant BVMD** or **ARB**; vitrectomy plus subretinal delivery; 5-year follow-up; primary focus on dose-limiting toxicity, procedure/drug-related adverse events; secondary outcomes include OCT, FAF, OCT-A, microperimetry, ETDRS BCVA, low-luminance VA, and PROs. (NCT07185256 chunk 1, NCT07185256 chunk 2) |
| NCT05809635 | Study of BEST1 Vitelliform Macular Dystrophy | Not applicable (Observational natural history study) | Columbia University | Recruiting | Natural history longitudinal assessment; no therapeutic intervention | 52 | Prospective cohort study to define the natural history of **BEST1-associated vitelliform macular dystrophy** and identify structural/functional endpoints for future trials; includes ERG, EOG, OCT, FAF, NIR-AF, qAF, BCVA, MAIA microperimetry, Goldman visual fields, and dark-adapted chromatic perimetry; includes children and adults; multicenter sites in the US, France, and Germany. (NCT05809635 chunk 1) |
| NCT02162953 | Stem Cell Models of Best Disease and Other Retinal Degenerative Diseases | Not applicable (Observational) | Mayo Clinic | Completed | Collection of participant samples to generate stem-cell disease models (iPSC-based modeling) | 48 | Completed observational study designed to develop stem-cell models of Best disease and related retinal degeneration for mechanistic and translational research; useful for mutation-specific modeling rather than direct treatment efficacy testing. (OpenTargets Search: -BEST1) |


*Table: This table summarizes the main clinical studies currently identified for BEST1-related retinopathy, including the ongoing OPGx-BEST1 interventional gene therapy trial and key observational natural history/modeling studies. It is useful for quickly comparing trial purpose, status, intervention type, and outcome focus.*

**OPGx-BEST1 (BIRD-1 trial, NCT07185256):** This is the first interventional gene therapy trial for bestrophinopathies, sponsored by Opus Genetics. OPGx-BEST1 is a codon-optimized full-length human BEST1 transgene under an RPE-specific VMD2 promoter, delivered via subretinal injection. Two dose levels (1.5E9 vg/eye and 4.5E9 vg/eye) are being explored in adults with BVMD or ARB. The trial began enrolling in September 2025 with 5-year follow-up planned (NCT07185256 chunk 1, NCT07185256 chunk 2). MAXO: MAXO:0001001 (gene therapy).

**Preclinical gene augmentation:** AAV-mediated gene augmentation therapy has demonstrated reversal of retinal microdetachments in canine bestrophinopathy models within 4–12 weeks post-injection, with sustained effects up to 245 weeks without inflammatory responses (amato2023genetherapyin pages 6-7, padhy2026reviewofthe pages 6-9). In iPSC-RPE cells, baculovirus and AAV2 vector-delivered wildtype BEST1 rescues calcium-dependent chloride channel function (grewal2021bestrophinopathiesperspectiveson pages 9-11).

#### CRISPR/Cas9 Gene Editing

- Allele-specific CRISPR/Cas9 genome editing has shown proof-of-concept for silencing mutant BEST1 transcripts in hiPSC-RPE cells, with one study demonstrating 96% frameshift efficiency via NHEJ (grewal2021bestrophinopathiesperspectiveson pages 9-11).
- Allele-specific silencing combined with gene augmentation has been proposed as a universal strategy, particularly for gain-of-function variants where gene augmentation alone is insufficient (amato2023genetherapyin pages 4-6).
- Recent work (Milenkovic & Weber 2026) demonstrated that eliminating the mutant BEST1 transcript via allele-specific CRISPR editing led to enhanced BEST1 localization, improved protein stability, and restoration of anion transport function in clonal hiPSC-RPE lines (from milenkovic2026 abstract).

#### Small Molecule Approaches

Small molecule drugs showing promise in preclinical models include: bafilomycin-A1 (slowing POS degradation), valproic acid (accelerating POS degradation), curcumin (enhancing ZO-1 and bestrophin-1 expression and improving phagocytosis), and sodium phenylbutyrate (4PBA) (xu2024ionchannelsresearch pages 4-5).

### Treatment Strategy by Mutation Type

- **LOF and DN mutations:** Amenable to gene augmentation alone, potentially requiring higher doses for stronger dominant negative effects (amato2023genetherapyin pages 1-2, haldrup2025genetherapystrategies pages 8-10).
- **GOF mutations:** Require combination approach: gene silencing (CRISPR or ASO) plus gene augmentation (amato2023genetherapyin pages 4-6).

---

## 13. Prevention

### Primary Prevention

No primary prevention is available, as the disease is caused by germline genetic variants.

### Secondary Prevention (Early Detection)

- **Genetic screening:** Cascade genetic testing of family members of affected individuals is recommended to identify asymptomatic carriers (beryozkin2024bestdiseaseglobal pages 1-2).
- **Carrier screening/preimplantation genetic diagnosis (PGD):** Available for families with known BEST1 mutations for family planning purposes.
- **Genetic counseling:** Essential for affected families given the autosomal dominant inheritance, variable expressivity, and incomplete penetrance (grewal2021bestrophinopathiesperspectiveson pages 1-2). MAXO: MAXO:0000127 (genetic counseling).

### Tertiary Prevention

- Regular ophthalmological monitoring with multimodal imaging (OCT, FAF, EOG) to detect disease progression and complications such as CNV (bianco2024multimodalimagingin pages 1-2, amato2023genetherapyin pages 2-3).
- Prompt anti-VEGF treatment for secondary choroidal neovascularization.

### Natural History Studies

The NCT05809635 natural history study (Columbia University, PI: Stephen Tsang) is currently recruiting to establish the natural course of BEST1 vitelliform macular dystrophy and identify sensitive structural and functional outcome measures for future clinical trials (NCT05809635 chunk 1).

---

## 14. Other Species / Natural Disease

### Canine Bestrophinopathy

Canine multifocal retinopathy (CMR) is a naturally occurring bestrophinopathy identified in multiple dog breeds, representing the most important large animal model for BEST1-related disease (dufour2025caninemodelsof pages 4-5, winkler2020largeanimalmodels pages 11-12):

- **cmr1:** p.Arg25Ter mutation in Great Pyrenees and mastiff breeds (winkler2020largeanimalmodels pages 11-12).
- **cmr2:** p.Gly161Asp mutation in Coton de Tulear (dufour2025caninemodelsof pages 4-5, winkler2020largeanimalmodels pages 11-12).
- **cmr3:** Two mutations in Swedish Lapponian Herder (dufour2025caninemodelsof pages 4-5, winkler2020largeanimalmodels pages 11-12).

**Species:** *Canis lupus familiaris* (NCBI Taxon: 9615).

**Key differences from human disease:** Canine CMR follows autosomal recessive inheritance (unlike the dominant human BVMD), but recapitulates clinical, histological, and molecular features of human bestrophinopathy including multifocal retinal detachments, lipofuscin accumulation, and RPE apical microvilli loss (dufour2025caninemodelsof pages 4-5, winkler2020largeanimalmodels pages 11-12). The retina-wide microdetachment is light-modulated, making it useful as an outcome measure for gene therapy studies (dufour2025caninemodelsof pages 4-5).

**Translational value:** Gene therapy using rAAV2 vectors delivering wildtype BEST1 successfully resolved detachments and restored RPE microvilli for over 207 weeks (approximately 4 years) post-injection in dogs, independent of age or mutation type (winkler2020largeanimalmodels pages 11-12).

---

## 15. Model Organisms

### Mouse Models

- **Best1 knockout mice:** Do not exhibit bestrophinopathy phenotypes or significant chloride current abnormalities, limiting their utility (amato2023genetherapyin pages 6-7, xu2024ionchannelsresearch pages 4-5).
- **Best1 p.W93C knock-in mice:** Display disease features with dominant inheritance, including reduced EOG light-rise and serous retinal detachments, but unexpectedly maintain normal chloride currents (padhy2026reviewofthe pages 6-9, xu2024ionchannelsresearch pages 4-5).
- **Best1 p.Y227N knock-in mice:** Show no ocular abnormalities up to 2 years of age (xu2024ionchannelsresearch pages 4-5).

### iPSC-RPE Models

Patient-derived induced pluripotent stem cell (iPSC)-RPE models represent the most flexible and disease-relevant in vitro system for studying BEST1-related dominant retinopathy (amato2023genetherapyin pages 6-7, xu2024ionchannelsresearch pages 4-5, xu2024ionchannelsresearch pages 14-14):
- Successfully reproduce disease features including BEST1 protein mislocalization, defective chloride conductance, impaired phagocytosis, lipofuscin accumulation, and reduced transepithelial fluid transport (xu2024ionchannelsresearch pages 4-5).
- Particularly valuable for studying dominant BEST1 mutations, since canine models lack dominant genotypes and mouse knockouts show no phenotype (amato2023genetherapyin pages 6-7).
- Used for gene therapy preclinical testing and CRISPR/Cas9 proof-of-concept studies (grewal2021bestrophinopathiesperspectiveson pages 9-11, xu2024ionchannelsresearch pages 14-14).

### Model Limitations

- **Canine models:** Recessive inheritance limits applicability to dominant human disease (xu2024ionchannelsresearch pages 4-5).
- **Mouse models:** Generally poor recapitulation of human phenotype; species-specific differences in RPE physiology limit translational value (amato2023genetherapyin pages 6-7, xu2024ionchannelsresearch pages 4-5).
- **iPSC-RPE:** Two-dimensional cell culture lacks the complex retinal architecture and three-dimensional tissue interactions present in vivo (xu2024ionchannelsresearch pages 4-5).

---

## Summary

BEST1-related dominant retinopathy, most commonly manifesting as Best vitelliform macular dystrophy, is a Mendelian inherited retinal dystrophy caused by heterozygous mutations in BEST1 encoding the bestrophin-1 calcium-activated chloride channel in the RPE. The disease is characterized by progressive vitelliform macular lesions, reduced EOG light rise, and variable visual impairment. With over 250 known pathogenic variants and three distinct molecular mechanisms (loss-of-function, dominant negative, and gain-of-function), the condition shows remarkable genetic and phenotypic heterogeneity. While no approved treatments currently exist, the first gene therapy clinical trial (BIRD-1/NCT07185256) began recruiting in 2025, and multiple preclinical gene therapy and gene editing strategies show considerable promise. The slow disease progression and prolonged photoreceptor viability provide a wide therapeutic window, positioning bestrophinopathies as a particularly attractive target for emerging genetic therapies.

References

1. (amato2023genetherapyin pages 2-3): Alessia Amato, Nida Wongchaisuwat, Andrew Lamborn, Ryan Schmidt, Lesley Everett, Paul Yang, and Mark E. Pennesi. Gene therapy in bestrophinopathies: insights from preclinical studies in preparation for clinical trials. Saudi Journal of Ophthalmology, 37:287-295, Oct 2023. URL: https://doi.org/10.4103/sjopt.sjopt\_175\_23, doi:10.4103/sjopt.sjopt\_175\_23. This article has 9 citations.

2. (navinesferrer2022impairedbestrophinchannel pages 1-2): Arnau Navinés-Ferrer, Sheila Ruiz-Nogales, Rafael Navarro, and Esther Pomares. Impaired bestrophin channel activity in an ipsc-rpe model of best vitelliform macular dystrophy (bvmd) from an early onset patient carrying the p77s dominant mutation. International Journal of Molecular Sciences, 23:7432, Jul 2022. URL: https://doi.org/10.3390/ijms23137432, doi:10.3390/ijms23137432. This article has 8 citations.

3. (haldrup2025genetherapystrategies pages 3-5): Silja B. Haldrup, Michelle E. McClements, Jasmina Cehajic-Kapetanovic, Thomas J. Corydon, and Robert E. MacLaren. Gene therapy strategies for the treatment of bestrophinopathies. International Journal of Molecular Sciences, 26:9421, Sep 2025. URL: https://doi.org/10.3390/ijms26199421, doi:10.3390/ijms26199421. This article has 2 citations.

4. (beryozkin2024bestdiseaseglobal pages 1-2): Avigail Beryozkin, Ifat Sher, Miriam Ehrenberg, Dinah Zur, Hadas Newman, Libe Gradstein, Francis Simaan, Ygal Rotenstreich, Nitza Goldenberg-Cohen, Irit Bahar, Anat Blumenfeld, Antonio Rivera, Boris Rosin, Iris Deitch-Harel, Ido Perlman, Hadas Mechoulam, Itay Chowers, Rina Leibu, Tamar Ben-Yosef, Eran Pras, Eyal Banin, Dror Sharon, and Samer Khateb. Best disease: global mutations review, genotype–phenotype correlation, and prevalence analysis in the israeli population. Investigative Opthalmology &amp; Visual Science, 65:39, Feb 2024. URL: https://doi.org/10.1167/iovs.65.2.39, doi:10.1167/iovs.65.2.39. This article has 7 citations.

5. (bianco2024multimodalimagingin pages 1-2): Lorenzo Bianco, Alessandro Arrigo, Alessio Antropoli, Alessandro Berni, Andrea Saladino, Manuel AP Vilela, Ahmad M Mansour, Francesco Bandello, and Maurizio Battaglia Parodi. Multimodal imaging in best vitelliform macular dystrophy: literature review and novel insights. European Journal of Ophthalmology, 34:39-51, Mar 2024. URL: https://doi.org/10.1177/11206721231166434, doi:10.1177/11206721231166434. This article has 26 citations and is from a peer-reviewed journal.

6. (yang2023best1novelmutation pages 1-2): Shangying Yang, Zhen Li, Wanyu Cheng, Meijiao Ma, Rui Qi, Xue Rui, Yinghua Ren, Xunlun Sheng, and Weining Rong. Best1 novel mutation causes bestrophinopathies in six families with distinct phenotypic diversity. Molecular Genetics & Genomic Medicine, Nov 2023. URL: https://doi.org/10.1002/mgg3.2095, doi:10.1002/mgg3.2095. This article has 3 citations and is from a peer-reviewed journal.

7. (amato2023genetherapyin pages 1-2): Alessia Amato, Nida Wongchaisuwat, Andrew Lamborn, Ryan Schmidt, Lesley Everett, Paul Yang, and Mark E. Pennesi. Gene therapy in bestrophinopathies: insights from preclinical studies in preparation for clinical trials. Saudi Journal of Ophthalmology, 37:287-295, Oct 2023. URL: https://doi.org/10.4103/sjopt.sjopt\_175\_23, doi:10.4103/sjopt.sjopt\_175\_23. This article has 9 citations.

8. (OpenTargets Search: -BEST1): Open Targets Query (-BEST1, 19 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

9. (NCT05809635 chunk 1): Stephen H. Tsang. Study of BEST1 Vitelliform Macular Dystrophy. Columbia University. 2021. ClinicalTrials.gov Identifier: NCT05809635

10. (nowomiejska2022diseaseexpressioncaused pages 1-2): Katarzyna Nowomiejska, Fadi Nasser, Katarina Stingl, Simone Schimpf‐Linzenbold, Saskia Biskup, Agnieszka Brzozowska, Robert Rejdak, Susanne Kohl, and Eberhart Zrenner. Disease expression caused by different variants in the best1 gene: genotype and phenotype findings in bestrophinopathies. Acta ophthalmologica, 100:e847-e858, Jul 2022. URL: https://doi.org/10.1111/aos.14958, doi:10.1111/aos.14958. This article has 12 citations and is from a domain leading peer-reviewed journal.

11. (NCT07185256 chunk 1):  Safety and Tolerability of Subretinally Injected OPGx-BEST1 in Patients With Best Vitelliform Macular Dystrophy (BVMD) or Autosomal-Recessive Bestrophinopathy (ARB). Opus Genetics, Inc. 2025. ClinicalTrials.gov Identifier: NCT07185256

12. (grewal2021bestrophinopathiesperspectiveson pages 1-2): Simranjeet Singh Grewal, Joseph J. Smith, and Amanda-Jayne F. Carr. Bestrophinopathies: perspectives on clinical disease, bestrophin-1 function and developing therapies. Therapeutic Advances in Ophthalmology, Jan 2021. URL: https://doi.org/10.1177/2515841421997191, doi:10.1177/2515841421997191. This article has 33 citations and is from a peer-reviewed journal.

13. (haldrup2025genetherapystrategies pages 1-3): Silja B. Haldrup, Michelle E. McClements, Jasmina Cehajic-Kapetanovic, Thomas J. Corydon, and Robert E. MacLaren. Gene therapy strategies for the treatment of bestrophinopathies. International Journal of Molecular Sciences, 26:9421, Sep 2025. URL: https://doi.org/10.3390/ijms26199421, doi:10.3390/ijms26199421. This article has 2 citations.

14. (padhy2026reviewofthe pages 2-4): Srikanta Kumar Padhy, Maja Šuštar Habjan, and Paul A. Constable. Review of the clinical electrooculogram - part 2: the bestrophinopathies and modified protocols. Documenta Ophthalmologica, 152:287-307, Mar 2026. URL: https://doi.org/10.1007/s10633-026-10093-y, doi:10.1007/s10633-026-10093-y. This article has 1 citations and is from a peer-reviewed journal.

15. (yang2023best1novelmutation pages 4-5): Shangying Yang, Zhen Li, Wanyu Cheng, Meijiao Ma, Rui Qi, Xue Rui, Yinghua Ren, Xunlun Sheng, and Weining Rong. Best1 novel mutation causes bestrophinopathies in six families with distinct phenotypic diversity. Molecular Genetics & Genomic Medicine, Nov 2023. URL: https://doi.org/10.1002/mgg3.2095, doi:10.1002/mgg3.2095. This article has 3 citations and is from a peer-reviewed journal.

16. (shi2023comprehensivegeneticanalysis pages 5-8): Jie-Feng Shi, Lu Tian, Tengyang Sun, Xiao Zhang, K. Xu, Yue Xie, Xiaoyan Peng, Xin Tang, Zidan Jin, and Yang Li. Comprehensive genetic analysis unraveled the missing heritability and a founder variant of <i>best1</i> in a chinese cohort with autosomal recessive bestrophinopathy. Investigative Opthalmology &amp; Visual Science, 64:37, Sep 2023. URL: https://doi.org/10.1167/iovs.64.12.37, doi:10.1167/iovs.64.12.37. This article has 8 citations.

17. (haldrup2025genetherapystrategies pages 5-7): Silja B. Haldrup, Michelle E. McClements, Jasmina Cehajic-Kapetanovic, Thomas J. Corydon, and Robert E. MacLaren. Gene therapy strategies for the treatment of bestrophinopathies. International Journal of Molecular Sciences, 26:9421, Sep 2025. URL: https://doi.org/10.3390/ijms26199421, doi:10.3390/ijms26199421. This article has 2 citations.

18. (navinesferrer2022impairedbestrophinchannel pages 10-11): Arnau Navinés-Ferrer, Sheila Ruiz-Nogales, Rafael Navarro, and Esther Pomares. Impaired bestrophin channel activity in an ipsc-rpe model of best vitelliform macular dystrophy (bvmd) from an early onset patient carrying the p77s dominant mutation. International Journal of Molecular Sciences, 23:7432, Jul 2022. URL: https://doi.org/10.3390/ijms23137432, doi:10.3390/ijms23137432. This article has 8 citations.

19. (navinesferrer2022impairedbestrophinchannel pages 11-13): Arnau Navinés-Ferrer, Sheila Ruiz-Nogales, Rafael Navarro, and Esther Pomares. Impaired bestrophin channel activity in an ipsc-rpe model of best vitelliform macular dystrophy (bvmd) from an early onset patient carrying the p77s dominant mutation. International Journal of Molecular Sciences, 23:7432, Jul 2022. URL: https://doi.org/10.3390/ijms23137432, doi:10.3390/ijms23137432. This article has 8 citations.

20. (xu2024ionchannelsresearch pages 4-5): Ping Xu, Weisheng Zou, Wenjing Yin, Guifu Chen, Guanjie Gao, and Xiufeng Zhong. Ion channels research in hpsc-rpe cells: bridging benchwork to clinical applications. Journal of Translational Medicine, Nov 2024. URL: https://doi.org/10.1186/s12967-024-05769-5, doi:10.1186/s12967-024-05769-5. This article has 0 citations and is from a peer-reviewed journal.

21. (amato2023genetherapyin pages 6-7): Alessia Amato, Nida Wongchaisuwat, Andrew Lamborn, Ryan Schmidt, Lesley Everett, Paul Yang, and Mark E. Pennesi. Gene therapy in bestrophinopathies: insights from preclinical studies in preparation for clinical trials. Saudi Journal of Ophthalmology, 37:287-295, Oct 2023. URL: https://doi.org/10.4103/sjopt.sjopt\_175\_23, doi:10.4103/sjopt.sjopt\_175\_23. This article has 9 citations.

22. (beryozkin2024bestdiseaseglobal pages 2-3): Avigail Beryozkin, Ifat Sher, Miriam Ehrenberg, Dinah Zur, Hadas Newman, Libe Gradstein, Francis Simaan, Ygal Rotenstreich, Nitza Goldenberg-Cohen, Irit Bahar, Anat Blumenfeld, Antonio Rivera, Boris Rosin, Iris Deitch-Harel, Ido Perlman, Hadas Mechoulam, Itay Chowers, Rina Leibu, Tamar Ben-Yosef, Eran Pras, Eyal Banin, Dror Sharon, and Samer Khateb. Best disease: global mutations review, genotype–phenotype correlation, and prevalence analysis in the israeli population. Investigative Opthalmology &amp; Visual Science, 65:39, Feb 2024. URL: https://doi.org/10.1167/iovs.65.2.39, doi:10.1167/iovs.65.2.39. This article has 7 citations.

23. (beryozkin2024bestdiseaseglobal pages 4-7): Avigail Beryozkin, Ifat Sher, Miriam Ehrenberg, Dinah Zur, Hadas Newman, Libe Gradstein, Francis Simaan, Ygal Rotenstreich, Nitza Goldenberg-Cohen, Irit Bahar, Anat Blumenfeld, Antonio Rivera, Boris Rosin, Iris Deitch-Harel, Ido Perlman, Hadas Mechoulam, Itay Chowers, Rina Leibu, Tamar Ben-Yosef, Eran Pras, Eyal Banin, Dror Sharon, and Samer Khateb. Best disease: global mutations review, genotype–phenotype correlation, and prevalence analysis in the israeli population. Investigative Opthalmology &amp; Visual Science, 65:39, Feb 2024. URL: https://doi.org/10.1167/iovs.65.2.39, doi:10.1167/iovs.65.2.39. This article has 7 citations.

24. (beryozkin2024bestdiseaseglobal pages 7-8): Avigail Beryozkin, Ifat Sher, Miriam Ehrenberg, Dinah Zur, Hadas Newman, Libe Gradstein, Francis Simaan, Ygal Rotenstreich, Nitza Goldenberg-Cohen, Irit Bahar, Anat Blumenfeld, Antonio Rivera, Boris Rosin, Iris Deitch-Harel, Ido Perlman, Hadas Mechoulam, Itay Chowers, Rina Leibu, Tamar Ben-Yosef, Eran Pras, Eyal Banin, Dror Sharon, and Samer Khateb. Best disease: global mutations review, genotype–phenotype correlation, and prevalence analysis in the israeli population. Investigative Opthalmology &amp; Visual Science, 65:39, Feb 2024. URL: https://doi.org/10.1167/iovs.65.2.39, doi:10.1167/iovs.65.2.39. This article has 7 citations.

25. (haldrup2025genetherapystrategies pages 7-8): Silja B. Haldrup, Michelle E. McClements, Jasmina Cehajic-Kapetanovic, Thomas J. Corydon, and Robert E. MacLaren. Gene therapy strategies for the treatment of bestrophinopathies. International Journal of Molecular Sciences, 26:9421, Sep 2025. URL: https://doi.org/10.3390/ijms26199421, doi:10.3390/ijms26199421. This article has 2 citations.

26. (NCT07185256 chunk 2):  Safety and Tolerability of Subretinally Injected OPGx-BEST1 in Patients With Best Vitelliform Macular Dystrophy (BVMD) or Autosomal-Recessive Bestrophinopathy (ARB). Opus Genetics, Inc. 2025. ClinicalTrials.gov Identifier: NCT07185256

27. (padhy2026reviewofthe pages 6-9): Srikanta Kumar Padhy, Maja Šuštar Habjan, and Paul A. Constable. Review of the clinical electrooculogram - part 2: the bestrophinopathies and modified protocols. Documenta Ophthalmologica, 152:287-307, Mar 2026. URL: https://doi.org/10.1007/s10633-026-10093-y, doi:10.1007/s10633-026-10093-y. This article has 1 citations and is from a peer-reviewed journal.

28. (grewal2021bestrophinopathiesperspectiveson pages 9-11): Simranjeet Singh Grewal, Joseph J. Smith, and Amanda-Jayne F. Carr. Bestrophinopathies: perspectives on clinical disease, bestrophin-1 function and developing therapies. Therapeutic Advances in Ophthalmology, Jan 2021. URL: https://doi.org/10.1177/2515841421997191, doi:10.1177/2515841421997191. This article has 33 citations and is from a peer-reviewed journal.

29. (amato2023genetherapyin pages 4-6): Alessia Amato, Nida Wongchaisuwat, Andrew Lamborn, Ryan Schmidt, Lesley Everett, Paul Yang, and Mark E. Pennesi. Gene therapy in bestrophinopathies: insights from preclinical studies in preparation for clinical trials. Saudi Journal of Ophthalmology, 37:287-295, Oct 2023. URL: https://doi.org/10.4103/sjopt.sjopt\_175\_23, doi:10.4103/sjopt.sjopt\_175\_23. This article has 9 citations.

30. (haldrup2025genetherapystrategies pages 8-10): Silja B. Haldrup, Michelle E. McClements, Jasmina Cehajic-Kapetanovic, Thomas J. Corydon, and Robert E. MacLaren. Gene therapy strategies for the treatment of bestrophinopathies. International Journal of Molecular Sciences, 26:9421, Sep 2025. URL: https://doi.org/10.3390/ijms26199421, doi:10.3390/ijms26199421. This article has 2 citations.

31. (dufour2025caninemodelsof pages 4-5): Valérie L. Dufour and Gustavo D. Aguirre. Canine models of inherited retinal diseases: from neglect to well-recognized translational value. Mammalian Genome, 36:500-510, Dec 2025. URL: https://doi.org/10.1007/s00335-024-10091-y, doi:10.1007/s00335-024-10091-y. This article has 5 citations and is from a peer-reviewed journal.

32. (winkler2020largeanimalmodels pages 11-12): Paige A. Winkler, Laurence M. Occelli, and Simon M. Petersen-Jones. Large animal models of inherited retinal degenerations: a review. Cells, 9:882, Apr 2020. URL: https://doi.org/10.3390/cells9040882, doi:10.3390/cells9040882. This article has 94 citations.

33. (xu2024ionchannelsresearch pages 14-14): Ping Xu, Weisheng Zou, Wenjing Yin, Guifu Chen, Guanjie Gao, and Xiufeng Zhong. Ion channels research in hpsc-rpe cells: bridging benchwork to clinical applications. Journal of Translational Medicine, Nov 2024. URL: https://doi.org/10.1186/s12967-024-05769-5, doi:10.1186/s12967-024-05769-5. This article has 0 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](BEST1-Related_Dominant_Retinopathy-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](BEST1-Related_Dominant_Retinopathy-deep-research-falcon_artifacts/artifact-01.md)
- [Edison artifact artifact-02](BEST1-Related_Dominant_Retinopathy-deep-research-falcon_artifacts/artifact-02.md)