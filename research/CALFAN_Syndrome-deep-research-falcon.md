---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-04T15:55:49.417867'
end_time: '2026-06-04T16:16:28.894866'
duration_seconds: 1239.48
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: CALFAN Syndrome
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 37
artifact_count: 4
artifact_sources:
  edison_answer_artifacts: 4
artifacts:
- filename: artifact-00.md
  path: CALFAN_Syndrome-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: CALFAN_Syndrome-deep-research-falcon_artifacts/artifact-01.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-01
- filename: artifact-02.md
  path: CALFAN_Syndrome-deep-research-falcon_artifacts/artifact-02.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-02
- filename: artifact-03.md
  path: CALFAN_Syndrome-deep-research-falcon_artifacts/artifact-03.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-03
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** CALFAN Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **CALFAN Syndrome** covering all of the
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
- **Disease Name:** CALFAN Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **CALFAN Syndrome** covering all of the
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


# CALFAN Syndrome (SCYL1-related disease / SCAR21): Disease Characteristics Research Report

## Executive summary
CALFAN syndrome is an ultra-rare autosomal recessive disorder caused by biallelic loss-of-function variants in **SCYL1**, characterized by **infantile/childhood-onset low/normal-γ-glutamyltransferase (GGT) cholestasis and/or recurrent acute liver failure (ALF)**, often **triggered by febrile infections**, with later-onset and variably progressive **neurodegeneration** (cerebellar ataxia, neuropathy) and frequent **skeletal/growth abnormalities**. The foundational cohort identified **7 patients from 5 families**, documenting febrile-triggered hepatic crises in early life and **fibrosis in all patients**, with variable neurologic and skeletal involvement. (lenz2018scyl1variantscause pages 6-7, lenz2018scyl1variantscause pages 1-2)

Recent literature (2023–2024) includes: (i) a **novel homozygous nonsense SCYL1 variant** in a Bahraini child with recurrent ALF and neurodevelopmental impairment; (ii) a 2023 adult **liver transplantation** case with **3-year** favorable graft outcome and an updated statement that **18 total CALFAN patients** had been reported at that time; and (iii) a 2024 review framing CALFAN as a congenital disorder of intracellular trafficking and providing **MIM: 616719**. (isa2023recurrentacuteliver pages 3-5, youssef2023calfan(lowγglutamyl pages 3-5, szabo2024intracellulartraffickingdefects pages 7-8)

---

## 1. Disease information

### 1.1 Definition and overview
- **Disease**: CALFAN syndrome is defined by the triad of **low/normal-GGT cholestasis**, **acute liver failure**, and **neurodegeneration**, caused by **SCYL1 deficiency**. (lenz2018scyl1variantscause pages 1-2, szabo2024intracellulartraffickingdefects pages 7-8)
- Foundational description emphasizes **infantile onset hepatic crises** with later-onset neurologic manifestations and progressive hepatic fibrosis. (lenz2018scyl1variantscause pages 6-7)

### 1.2 Key identifiers
- **OMIM/MIM**: **MIM: 616719** (reported in a 2024 review). (szabo2024intracellulartraffickingdefects pages 7-8)
- **MONDO, Orphanet, ICD-10/ICD-11, MeSH**: Not identified in the retrieved source set; should be verified in external disease ontologies for knowledge-base normalization. (szabo2024intracellulartraffickingdefects pages 7-8, szabo2024intracellulartraffickingdefects pages 1-2)

### 1.3 Synonyms / alternative names
- **SCYL1-related disease**, **SCYL1 deficiency**, and overlapping label **spinocerebellar ataxia, autosomal recessive type 21 (SCAR21)** appear in the literature. (demir2023coexistenceofspinocerebellar pages 3-4, isa2023recurrentacuteliver pages 3-5)

### 1.4 Evidence source type
The knowledge base for CALFAN syndrome is derived primarily from **individual case reports/series** and **reviews**, rather than population-level EHR cohorts, consistent with its extreme rarity. (lenz2018scyl1variantscause pages 6-7, youssef2023calfan(lowγglutamyl pages 3-5, szabo2024intracellulartraffickingdefects pages 7-8)

| Category | Value | Notes | Evidence |
|---|---|---|---|
| Disease name | CALFAN syndrome | Acronym for low gamma-glutamyl-transferase cholestasis, acute liver failure, and neurodegeneration | (lenz2018scyl1variantscause pages 1-2, szabo2024intracellulartraffickingdefects pages 7-8) |
| Expanded name / defining triad | Low γ-glutamyl-transferase cholestasis, acute liver failure, and neurodegeneration | Core syndrome definition used in primary and review literature | (lenz2018scyl1variantscause pages 1-2, szabo2024intracellulartraffickingdefects pages 7-8) |
| Alternative disease labels | SCYL1-related disease; SCYL1 deficiency; SCAR21 / spinocerebellar ataxia, autosomal recessive 21 | Literature uses both CALFAN and SCAR21 for overlapping SCYL1-related phenotype spectrum | (demir2023coexistenceofspinocerebellar pages 3-4, isa2023recurrentacuteliver pages 3-5) |
| Causal gene | SCYL1 | Encodes SCY1-like pseudokinase 1 | (szabo2024intracellulartraffickingdefects pages 7-8, szabo2024intracellulartraffickingdefects pages 1-2) |
| Molecular etiology | Biallelic pathogenic variants in SCYL1 | Typically homozygous in consanguineous families, though compound heterozygosity is also reported | (lenz2018scyl1variantscause pages 6-7, yadav2026infantileliverfailure pages 6-7) |
| Inheritance | Autosomal recessive | Mendelian recessive disorder | (yadav2026infantileliverfailure pages 10-12, demir2023coexistenceofspinocerebellar pages 3-4) |
| OMIM / MIM | MIM: 616719 | Reported in 2024 review; refers to CALFAN syndrome in provided source context | (szabo2024intracellulartraffickingdefects pages 7-8) |
| MONDO ID | Not identified in provided sources | No MONDO identifier was found in the retrieved evidence | (szabo2024intracellulartraffickingdefects pages 7-8, szabo2024intracellulartraffickingdefects pages 1-2) |
| Orphanet ID | Not identified in provided sources | Not reported in retrieved evidence | (szabo2024intracellulartraffickingdefects pages 7-8, szabo2024intracellulartraffickingdefects pages 1-2) |
| ICD-10 / ICD-11 | Not identified in provided sources | Not reported in retrieved evidence | (szabo2024intracellulartraffickingdefects pages 7-8, szabo2024intracellulartraffickingdefects pages 1-2) |
| MeSH | Not identified in provided sources | Not reported in retrieved evidence | (szabo2024intracellulartraffickingdefects pages 7-8, szabo2024intracellulartraffickingdefects pages 1-2) |
| Key hepatic features | Recurrent low/normal-GGT cholestasis; infantile or early-childhood acute liver failure; hepatomegaly; progressive fibrosis/cirrhosis in some patients | Liver crises are often febrile-illness triggered and may resolve between episodes | (lenz2018scyl1variantscause pages 6-7, lenz2018scyl1variantscause pages 1-2, youssef2023calfan(lowγglutamyl pages 3-5) |
| Key neurologic features | Cerebellar ataxia, tremor, gait disorder, peripheral neuropathy, cerebellar atrophy, developmental delay/language delay, occasional seizures | Neurologic manifestations often appear later than liver disease and may progress despite liver transplant | (lenz2018scyl1variantscause pages 6-7, yadav2026infantileliverfailure pages 8-10, youssef2023calfan(lowγglutamyl pages 3-5, isa2023recurrentacuteliver pages 3-5) |
| Skeletal / growth features | Short stature, scoliosis, vertebral anomalies, hip dysplasia, delayed bone age, other musculoskeletal abnormalities | Variable expressivity across reported patients | (lenz2018scyl1variantscause pages 6-7, yadav2026infantileliverfailure pages 8-10, NCT04653909 chunk 1) |
| Pathobiology summary | Intracellular trafficking disorder involving impaired COPI-mediated Golgi-ER retrograde trafficking and Golgi/vesicle homeostasis | SCYL1 loss is linked to trafficking defects; broader mechanistic work implicates Golgi architecture, endolysosomal distribution, and vesicle secretion | (yadav2026infantileliverfailure pages 6-7, kaeserpebernard2022mtorc1controlsgolgi pages 2-3, kaeserpebernard2022mtorc1controlsgolgi pages 1-2) |
| Typical trigger of hepatic crises | Febrile infection / intercurrent illness | Recurrently emphasized across case series and reviews | (lenz2018scyl1variantscause pages 6-7, isa2023recurrentacuteliver pages 1-3, lenz2018scyl1variantscause pages 1-2) |
| Data source type | Aggregated disease-level literature derived from individual case reports/series and reviews | Evidence base is rare-disease literature rather than EHR-derived population datasets | (lenz2018scyl1variantscause pages 6-7, youssef2023calfan(lowγglutamyl pages 3-5, szabo2024intracellulartraffickingdefects pages 7-8) |


*Table: This table summarizes the main identifiers, synonyms, gene, inheritance pattern, and defining clinical features of CALFAN syndrome from the retrieved evidence. It is useful as a compact normalization reference for a disease knowledge base entry.*

---

## 2. Etiology

### 2.1 Disease causal factors
- **Genetic cause (primary)**: **Biallelic pathogenic variants in SCYL1**. (lenz2018scyl1variantscause pages 6-7, yadav2026infantileliverfailure pages 10-12)
- **Triggering factor (physiologic/environmental)**: **Febrile infections/intercurrent illness** frequently precipitate hepatic crises. (lenz2018scyl1variantscause pages 6-7, isa2023recurrentacuteliver pages 1-3, lenz2018scyl1variantscause pages 1-2)

### 2.2 Risk factors
- **Genetic**: Autosomal recessive inheritance; many reported cases occur in **consanguineous families** (homozygosity), though compound heterozygosity occurs. (yadav2026infantileliverfailure pages 6-7, yadav2026infantileliverfailure pages 10-12)
- **Environmental/clinical**: Febrile illness and intercurrent infections are repeatedly reported as triggers; modifiers (nutritional state, age at first decompensation) are proposed but not quantified in the retrieved evidence. (lenz2018scyl1variantscause pages 6-7, yadav2026infantileliverfailure pages 6-7)

### 2.3 Protective factors
No validated genetic or environmental protective factors were identified in the retrieved sources.

### 2.4 Gene–environment interactions
The best-supported interaction is **fever/infection-triggered decompensation** in a genetically susceptible background (SCYL1 deficiency). (lenz2018scyl1variantscause pages 6-7, isa2023recurrentacuteliver pages 1-3)

---

## 3. Phenotypes (with suggested HPO terms)

Key manifestations span hepatic, neurologic, and skeletal domains with variable expressivity.

### 3.1 Hepatic phenotypes
- **Core hepatic phenotype**: recurrent low/normal-GGT cholestasis or ALF starting in infancy, with crises often triggered by febrile infection. (lenz2018scyl1variantscause pages 6-7, lenz2018scyl1variantscause pages 1-2)
- **Progression**: in the foundational cohort, crises were transient but **fibrosis developed in all**. (lenz2018scyl1variantscause pages 6-7)

### 3.2 Neurologic phenotypes
- Later-onset and variably progressive: microcephaly, developmental/language delay, tremor, gait impairment/ataxia, peripheral neuropathy, cerebellar atrophy; seizures in a minority. (lenz2018scyl1variantscause pages 6-7, yadav2026infantileliverfailure pages 8-10, isa2023recurrentacuteliver pages 3-5)

### 3.3 Skeletal/growth phenotypes
- Short stature/growth retardation, scoliosis, hip dysplasia and other musculoskeletal abnormalities are reported in many patients. (lenz2018scyl1variantscause pages 6-7, yadav2026infantileliverfailure pages 8-10)

| Group | Phenotype description | Suggested HPO term | Typical onset | Frequency / number reported | Key citations |
|---|---|---|---|---|---|
| Hepatic | Recurrent low/normal-GGT cholestasis | HP: Cholestasis | Infancy | Main hepatic presentation in 7/7 patients in the 2018 series; described as recurrent low-GGT cholestasis or acute liver failure | (lenz2018scyl1variantscause pages 6-7, lenz2018scyl1variantscause pages 1-2) |
| Hepatic | Acute liver failure / recurrent acute liver failure, often fever-triggered | HP: Acute hepatic failure | Infancy to early childhood | 7/7 had severe cholestatic liver crises in first 18 months in Lenz 2018; recurrent ALF also documented in later case reports | (lenz2018scyl1variantscause pages 6-7, isa2023recurrentacuteliver pages 1-3, lenz2018scyl1variantscause pages 1-2) |
| Hepatic | Febrile-illness-triggered liver crises | HP: Recurrent fever-triggered episodes (suggest phenotype annotation as recurrent acute hepatic failure triggered by febrile infection) | Infancy to childhood | Trigger emphasized across core series/case reports; in Lenz 2018 crises were triggered by febrile infections | (lenz2018scyl1variantscause pages 6-7, isa2023recurrentacuteliver pages 1-3, lenz2018scyl1variantscause pages 1-2) |
| Hepatic | Hepatomegaly | HP: Hepatomegaly | Infancy | 7/7 in Lenz 2018; also reported in later cases | (lenz2018scyl1variantscause pages 6-7, isa2023recurrentacuteliver pages 1-3) |
| Hepatic | Splenomegaly / hepatosplenomegaly | HP: Splenomegaly | Infancy to childhood | 4/7 in Lenz 2018; hepatosplenomegaly also reported in later single cases | (lenz2018scyl1variantscause pages 6-7, isa2023recurrentacuteliver pages 5-6) |
| Hepatic | Neonatal jaundice | HP: Neonatal jaundice | Neonatal | 3/7 in Lenz 2018 | (lenz2018scyl1variantscause pages 6-7) |
| Hepatic | Liver fibrosis progressing to cirrhosis in some cases | HP: Hepatic fibrosis | Infancy onward | Fibrosis developed in all 7/7 in Lenz 2018; cirrhosis documented in explant after adult liver transplant | (lenz2018scyl1variantscause pages 6-7, youssef2023calfan(lowγglutamyl pages 2-3) |
| Neurologic | Microcephaly | HP: Microcephaly | Infancy/childhood | 6/7 in Lenz 2018 | (lenz2018scyl1variantscause pages 6-7) |
| Neurologic | Mild language delay / speech delay | HP: Delayed speech and language development | Childhood | 6/7 in Lenz 2018; severe speech delay also reported in 2023 Bahraini case | (lenz2018scyl1variantscause pages 6-7, isa2023recurrentacuteliver pages 3-5) |
| Neurologic | Gait abnormality / progressive difficulty walking | HP: Abnormal gait | Childhood | Motor dysfunction in 5/7 in Lenz 2018; progressive gait deterioration in 2023 case | (lenz2018scyl1variantscause pages 6-7, isa2023recurrentacuteliver pages 1-3) |
| Neurologic | Cerebellar ataxia | HP: Cerebellar ataxia | Childhood | Reported across core series and later reviews/cases; often progressive and later-onset than liver disease | (yadav2026infantileliverfailure pages 8-10, demir2023coexistenceofspinocerebellar pages 3-4, isa2023recurrentacuteliver pages 5-6) |
| Neurologic | Tremor / intention tremor | HP: Tremor | Childhood | Present among motor dysfunction features in Lenz 2018 and clearly documented in 2023 case | (lenz2018scyl1variantscause pages 6-7, isa2023recurrentacuteliver pages 3-5, isa2023recurrentacuteliver pages 5-6) |
| Neurologic | Peripheral neuropathy / motor-sensory neuropathy | HP: Peripheral neuropathy | Late childhood to adolescence | Reported as part of progressive neurologic phenotype across reviews and case descriptions | (yadav2026infantileliverfailure pages 8-10, demir2023coexistenceofspinocerebellar pages 3-4) |
| Neurologic | Cerebellar atrophy | HP: Cerebellar atrophy | Childhood to adolescence | Reported in CALFAN/SCYL1 disease and persisted after transplant in adult follow-up case | (youssef2023calfan(lowγglutamyl pages 3-5, demir2023coexistenceofspinocerebellar pages 3-4) |
| Neurologic | Seizures | HP: Seizure | Childhood | 1/7 in Lenz 2018 required transient therapy | (lenz2018scyl1variantscause pages 6-7) |
| Neurologic | Hypotonia | HP: Hypotonia | Childhood | Reported in broader SCYL1/CALFAN phenotype summaries | (yadav2026infantileliverfailure pages 8-10) |
| Neurologic | Optic atrophy | HP: Optic atrophy | Childhood | Reported in broader literature review summaries, not quantified in core 7-patient series excerpt | (yadav2026infantileliverfailure pages 8-10) |
| Skeletal/Other | Short stature / growth retardation | HP: Short stature | Childhood | Skeletal abnormalities in 5/7 in Lenz 2018 included short stature; growth retardation also noted in reviews | (lenz2018scyl1variantscause pages 6-7, szabo2024intracellulartraffickingdefects pages 7-8) |
| Skeletal/Other | Scoliosis / kyphoscoliosis | HP: Scoliosis | Childhood to adolescence | Included among skeletal abnormalities in Lenz 2018; also prominent in rehabilitation case and trial record | (lenz2018scyl1variantscause pages 6-7, NCT04653909 chunk 1, yigit2022theoutcomesof pages 1-2) |
| Skeletal/Other | Hip dysplasia | HP: Hip dysplasia | Childhood | Included among skeletal abnormalities in Lenz 2018; also listed in trial record phenotype summary | (lenz2018scyl1variantscause pages 6-7, NCT04653909 chunk 1) |
| Skeletal/Other | Vertebral anomalies / rib clefting | HP: Abnormality of the vertebral column | Childhood | Reported among skeletal abnormalities in Lenz 2018; vertebral anomalies also summarized in later reviews | (lenz2018scyl1variantscause pages 6-7, yadav2026infantileliverfailure pages 8-10) |
| Skeletal/Other | Delayed bone age | HP: Delayed bone age | Childhood | Reported in later literature review summaries; not quantified in core 7-patient excerpt | (yadav2026infantileliverfailure pages 8-10) |
| Skeletal/Other | Developmental delay / mild intellectual disability / cognitive impairment | HP: Global developmental delay | Childhood | Variable; developmental delay and cognitive issues reported in later cases and trial description, though cognition can be preserved in some patients | (isa2023recurrentacuteliver pages 3-5, NCT04653909 chunk 1) |
| Skeletal/Other | Recurrent respiratory failure / respiratory involvement | HP: Respiratory failure | Childhood | Rare/expanded phenotype reported outside initial core series; trial/case literature indicates musculoskeletal factors may affect respiratory function | (demir2023coexistenceofspinocerebellar pages 3-4, yigit2022theoutcomesof pages 5-6) |


*Table: This table groups reported CALFAN syndrome manifestations into hepatic, neurologic, and skeletal/other domains, with suggested HPO terms, usual timing, and frequencies where the literature provides counts. It is useful for phenotype annotation and disease knowledge base curation.*

Quality-of-life impact is best documented through rehabilitation outcomes (see Treatment/Supportive Care), where functional independence and PedsQL measures improved with physiotherapy in a single case. (yigit2022theoutcomesof pages 2-3)

---

## 4. Genetic / molecular information

### 4.1 Causal gene
- **SCYL1** (SCY1-like pseudokinase 1). (szabo2024intracellulartraffickingdefects pages 7-8, szabo2024intracellulartraffickingdefects pages 1-2)

### 4.2 Pathogenic variants (examples from recent and foundational reports)
- **c.895A>T (p.Lys299Ter)**, homozygous nonsense; described as novel/likely pathogenic in a 2023 case with recurrent ALF and neurodevelopmental impairment. (isa2023recurrentacuteliver pages 3-5, isa2023recurrentacuteliver pages 1-3)
- **c.1567C>T (p.Arg523*)**, homozygous nonsense in a consanguineous family; presented as infantile fever-triggered ALF/cholestasis without initial neurologic signs (reported in a later case-based review). (yadav2026infantileliverfailure pages 6-7)
- **c.745_746insG** (frameshift insertion) reported in a pediatric case with severe hepatic phenotype. (suenera2025acuteonchronica pages 4-6, suenera2025acuteonchronic pages 4-6)

| Paper (year, URL) | Patient count | Inheritance | Variant(s) (HGVS c./p.) | Variant type | Key phenotypes | Outcomes / notes |
|---|---:|---|---|---|---|---|
| Lenz et al. (2018), https://doi.org/10.1038/gim.2017.260 | 7 patients from 5 families | Autosomal recessive; biallelic SCYL1 variants | Specific HGVS variants not extracted in evidence; reported as biallelic SCYL1 variants | Not extracted in evidence | Recurrent low/normal-GGT cholestasis or acute liver failure in infancy; febrile infection-triggered liver crises; hepatomegaly; splenomegaly in some; fibrosis in all reported patients; later variable neurologic phenotype including microcephaly, language delay, motor dysfunction, tremor, gait abnormality; skeletal abnormalities in some (lenz2018scyl1variantscause pages 6-7, lenz2018scyl1variantscause pages 1-2) | One child underwent liver transplantation at 23 months; crises were transient but fibrosis developed (lenz2018scyl1variantscause pages 6-7) |
| Isa et al. (2023), https://doi.org/10.7759/cureus.36249 | 1 | Autosomal recessive; homozygous | c.895A>T; p.Lys299Ter | Nonsense | Recurrent febrile-illness–triggered acute liver failure; hepatomegaly/hepatosplenomegaly; developmental delay; progressive gait deterioration; intention tremor; severe speech delay; mild/moderate intellectual disability; minimal periventricular white matter MRI changes (isa2023recurrentacuteliver pages 3-5, isa2023recurrentacuteliver pages 1-3, isa2023recurrentacuteliver pages 5-6) | Managed supportively; liver transplantation discussed but not performed; variant described as novel and likely pathogenic (isa2023recurrentacuteliver pages 3-5, isa2023recurrentacuteliver pages 7-8) |
| Youssef et al. (2023), https://doi.org/10.1155/2023/3010131 | 1 | SCYL1-associated CALFAN syndrome; inheritance not explicitly extracted in evidence for this case | SCYL1 mutation; specific variant not fully specified in evidence | Not fully extracted in evidence | Infantile-onset recurrent jaundice / pediatric acute liver failure with later neurologic sequelae; explant pathology showed cirrhosis, cholestatic liver injury, and bile ductular proliferation; persistent cerebellar atrophy and neurologic deficits after transplant (youssef2023calfan(lowγglutamyl pages 3-5, youssef2023calfan(lowγglutamyl pages 2-3) | Liver transplantation at age 20; doing well at 3-year follow-up; biliary stricture resolved; no acute cellular rejection reported (youssef2023calfan(lowγglutamyl pages 3-5, youssef2023calfan(lowγglutamyl pages 1-2, youssef2023calfan(lowγglutamyl pages 2-3) |
| Suenera & Navinummapathy (2025), URL not available in retrieved evidence | 1 | Autosomal recessive; homozygous | c.745_746insG; protein consequence not extracted in evidence | Truncating / frameshift insertion | Recurrent pediatric acute liver failure with cholestasis; hepatosplenomegaly; canalicular cholestasis; degeneration and mild fibrosis; evolving neurologic features including cerebellar atrophy and peripheral neuropathy; PFIC-like overlap (suenera2025acuteonchronica pages 4-6, suenera2025acuteonchronic pages 4-6, suenera2025acuteonchronicc pages 4-6) | Supportive/emergency management described (infection control, IV NAC, correction of coagulopathy, fat-soluble vitamins, ursodeoxycholic acid, lactulose); liver transplantation considered for progressive failure (suenera2025acuteonchronica pages 4-6, suenera2025acuteonchronic pages 4-6, suenera2025acuteonchronicd pages 4-6) |
| Yadav et al. (2026), https://doi.org/10.58427/apghn.5.2.2026.86-97 | 1 | Autosomal recessive; homozygous | c.1567C>T; p.Arg523* | Nonsense / null | 9-month-old infant with fever-triggered cholestatic jaundice and acute liver failure; low/normal-GGT cholestasis; no neurologic, neuroimaging, or skeletal abnormalities at presentation; family history of sibling death from infantile liver failure (yadav2026infantileliverfailure pages 6-7) | Emphasized early genomic testing, longitudinal neurologic surveillance, transplant referral when indicated, and recurrence-risk counseling; expands spectrum by showing isolated infantile hepatic presentation initially (yadav2026infantileliverfailure pages 6-7, yadav2026infantileliverfailure pages 10-12) |


*Table: This table summarizes SCYL1 pathogenic variants and associated clinical notes for CALFAN syndrome from the retrieved literature. It highlights reported HGVS changes, inheritance, major phenotypes, and clinically important outcomes such as liver transplantation.*

### 4.3 Functional consequences
The retrieved evidence is consistent with **loss-of-function** (truncating/nonsense/frameshift) as a major mechanism. (isa2023recurrentacuteliver pages 3-5, suenera2025acuteonchronic pages 4-6)

### 4.4 Modifier genes / epigenetics / chromosomal abnormalities
No validated modifier genes, epigenetic signatures, or recurrent chromosomal abnormalities were identified in the retrieved sources.

---

## 5. Environmental information
No established non-genetic causes are implicated; the dominant “environmental” component in the retrieved evidence is **infection/fever as a trigger** for hepatic decompensation. (lenz2018scyl1variantscause pages 6-7, isa2023recurrentacuteliver pages 1-3)

---

## 6. Mechanism / pathophysiology

### 6.1 Current mechanistic understanding (causal chain)
1. **SCYL1 loss-of-function** →
2. **Impaired intracellular trafficking**, especially **COPI-mediated Golgi–ER retrograde trafficking** →
3. Hepatocyte secretory stress and (proposed) **ER stress/unfolded protein response**, culminating in susceptibility to **hepatocellular injury/apoptosis**, particularly during febrile illness →
4. **Recurrent cholestasis/ALF** episodes with cumulative injury leading to **fibrosis/cirrhosis** in some →
5. Later-onset **neurodegeneration** (cerebellar atrophy/ataxia, neuropathy), which may progress independently of liver disease and can persist after transplant. (lenz2018scyl1variantscause pages 1-2, yadav2026infantileliverfailure pages 6-7, youssef2023calfan(lowγglutamyl pages 3-5)

### 6.2 Pathways and cellular processes
- **Vesicular trafficking (Golgi–ER retrograde transport; COPI-related processes)** are central, with SCYL1 acting as a scaffold/regulator. (yadav2026infantileliverfailure pages 6-7, hellicar2021investigatingtherole pages 35-38)
- **mTORC1–SCYL1 axis**: mechanistic cell biology work shows **mTORC1 phosphorylates SCYL1 (Ser754)** to control **Golgi architecture, endolysosomal distribution, and extracellular vesicle secretion**; authors suggest relevance to CALFAN pathophysiology. (kaeserpebernard2022mtorc1controlsgolgi pages 1-2, kaeserpebernard2022mtorc1controlsgolgi pages 7-8)

### 6.3 Suggested ontology terms
- **GO Biological Process** (suggested): COPI-mediated vesicle transport; Golgi-to-ER retrograde transport; ER stress / unfolded protein response; regulation of Golgi organization; autophagy/endolysosomal organization (supported conceptually by trafficking and stress mechanisms described). (yadav2026infantileliverfailure pages 6-7, kaeserpebernard2022mtorc1controlsgolgi pages 1-2)
- **Cell types (CL, suggested)**: hepatocyte; cerebellar Purkinje cell; peripheral neuron/Schwann cell (reflecting hepatic and neurodegenerative involvement; specific CL IDs should be mapped during curation). (yadav2026infantileliverfailure pages 6-7, youssef2023calfan(lowγglutamyl pages 3-5)

### 6.4 Model organisms / experimental systems
- A mechanistic dissertation reports that loss of Scyl1 in mice causes motor neuron disease and cerebellar degeneration and provides biochemical trafficking interaction data (e.g., COPI/COPII interactions). (hellicar2021investigatingtherole pages 106-111, hellicar2021investigatingtherole pages 35-38)

---

## 7. Anatomical structures affected (suggested UBERON)
- **Primary organ**: liver (UBERON: liver). (lenz2018scyl1variantscause pages 6-7, lenz2018scyl1variantscause pages 1-2)
- **Nervous system**: cerebellum (cerebellar atrophy), peripheral nerves (neuropathy). (yadav2026infantileliverfailure pages 8-10, youssef2023calfan(lowγglutamyl pages 3-5)
- **Musculoskeletal system**: spine (scoliosis), hip (hip dysplasia). (lenz2018scyl1variantscause pages 6-7, NCT04653909 chunk 1)
- **Subcellular compartments**: Golgi apparatus, ER–Golgi intermediate compartment, endosomes/lysosomes (based on SCYL1 localization and mTORC1-regulated redistribution). (kaeserpebernard2022mtorc1controlsgolgi pages 1-2, hellicar2021investigatingtherole pages 35-38)

---

## 8. Temporal development
- **Onset**: hepatic disease typically begins in **infancy/early childhood**, with crises reported in the first 18 months in the foundational cohort. (lenz2018scyl1variantscause pages 6-7)
- **Progression**: hepatic crises may be transient with inter-episodic normalization, yet fibrosis can progress; neurologic manifestations often emerge later and may be progressive. (lenz2018scyl1variantscause pages 6-7, yadav2026infantileliverfailure pages 8-10)

---

## 9. Inheritance and population

### 9.1 Inheritance
- **Autosomal recessive**. (yadav2026infantileliverfailure pages 10-12, demir2023coexistenceofspinocerebellar pages 3-4)

### 9.2 Epidemiology and case counts
- No population prevalence/incidence estimates were identified in the retrieved sources.
- A 2023 transplant case report states: **“To date, 18 patients of CALFAN syndrome with SCYL1 mutation including our case have been reported.”** (human case report literature count; not a registry estimate). (youssef2023calfan(lowγglutamyl pages 3-5)
- A later review/case discussion indicates **“fewer than 25 reported cases worldwide”** (summary statement). (yadav2026infantileliverfailure pages 1-3)
- A clinical trial registry entry (single-case physiotherapy study) described CALFAN as ultra-rare with **~11 reported patients** at the time of registration (reflecting contemporaneous knowledge in 2020, not a definitive count). (NCT04653909 chunk 1)

---

## 10. Diagnostics

### 10.1 Clinical/laboratory hallmarks
- **Low-to-normal GGT cholestasis** in the setting of fever-triggered cholestatic hepatitis/ALF is repeatedly emphasized as a key clue. (yadav2026infantileliverfailure pages 8-10, yadav2026infantileliverfailure pages 3-6)
- Episodes can show marked transaminase elevations and coagulopathy; ALF definition includes INR criteria not corrected by vitamin K in at least one report. (yadav2026infantileliverfailure pages 1-3, yadav2026infantileliverfailure pages 3-6)

### 10.2 Genetic testing approach
- **Whole-exome sequencing (WES)** is repeatedly described as diagnostic and is recommended early in infants/children with fever-triggered ALF and low/normal-GGT cholestasis, particularly with consanguinity or family history. (isa2023recurrentacuteliver pages 1-3, yadav2026infantileliverfailure pages 8-10)

### 10.3 Differential diagnosis
Differentials with overlapping presentations include:
- **PFIC** and other low/normal-GGT cholestasis disorders (e.g., bile acid synthesis defects). (yadav2026infantileliverfailure pages 1-3, yadav2026infantileliverfailure pages 3-6)
- **NBAS-related recurrent ALF**, and other fever-triggered genetic ALF causes (e.g., TRMU, LARS1). (yadav2026infantileliverfailure pages 1-3, yadav2026infantileliverfailure pages 3-6)
- **Wilson disease**, **autoimmune hepatitis**, **peroxisomal disorders** and other intracellular trafficking disorders. (suenera2025acuteonchronicd pages 4-6, suenera2025acuteonchronic pages 4-6)

---

## 11. Outcome / prognosis
- **Hepatic course**: crises may resolve but fibrosis can accumulate; in the foundational 7-patient cohort, fibrosis developed in all patients. (lenz2018scyl1variantscause pages 6-7)
- **Neurologic course**: neurodegeneration may be progressive and can persist after liver transplantation. (youssef2023calfan(lowγglutamyl pages 3-5, yadav2026infantileliverfailure pages 8-10)

---

## 12. Treatment

### 12.1 Acute and chronic medical management (supportive)
There is no established disease-modifying therapy in the retrieved sources; care is supportive and trigger-focused.
- Acute crisis measures reported include infection control, correction of coagulopathy, and sometimes IV NAC (example dosing reported in one case report). (suenera2025acuteonchronic pages 4-6, suenera2025acuteonchronicd pages 4-6)
- Chronic measures include nutritional optimization and fat-soluble vitamins, cholestasis-directed therapy, and multidisciplinary follow-up. (yadav2026infantileliverfailure pages 8-10, yadav2026infantileliverfailure pages 10-12)

### 12.2 Liver transplantation
- A 2023 case report describes transplantation at **age 20** with **3-year** favorable follow-up and no reported acute rejection; neurologic deficits persisted. (youssef2023calfan(lowγglutamyl pages 3-5, youssef2023calfan(lowγglutamyl pages 2-3)
- The same report notes three earlier transplants in infancy/early childhood (7–23 months) among reported cases and states **no graft failure** was reported with **8–11 years** follow-up in prior transplant recipients. (youssef2023calfan(lowγglutamyl pages 3-5)

### 12.3 Rehabilitation / physical therapy (real-world implementation)
- **Case report evidence (2022)**: A 12-week trunk stabilization/balance/functional program improved multiple functional and QoL measures (ICARS 47→42; TIS 9→13; WeeFIM 79→83; PedsQL 47.11→52.17; 9-HPT times improved). (yigit2022theoutcomesof pages 2-3, yigit2022theoutcomesof pages 3-4)
- **ClinicalTrials.gov (NCT04653909)**: single-case interventional rehabilitation study (start 2020-03-01; completion 2020-11-17) with outcomes including TIS, ICARS, PedsQL, WeeFIM. (NCT04653909 chunk 1)

**Suggested MAXO terms (curation suggestions)**: physical therapy; rehabilitation therapy; liver transplantation; genetic counseling; supportive care for acute liver failure (mapping to MAXO IDs should be completed during ontology curation). (NCT04653909 chunk 1, youssef2023calfan(lowγglutamyl pages 3-5)

| Management domain | Real-world implementation | Key details / quantitative data | Evidence / outcomes | Citations |
|---|---|---|---|---|
| Acute liver crisis management | Supportive, emergency-focused inpatient care during febrile-triggered cholestatic/ALF episodes | Reported measures include infection control, IV N-acetylcysteine (example dose 100 mg/kg/day in one report), correction of coagulopathy with fresh frozen plasma/platelets, antibiotics when indicated, ursodeoxycholic acid, fat-soluble vitamin supplementation, lactulose as needed, and close monitoring of bilirubin, INR, transaminases, glucose, ammonia, and encephalopathy | Most liver crises can recover with supportive treatment, but fibrosis may accumulate over time; crises are commonly triggered by febrile illnesses/intercurrent infections | (lenz2018scyl1variantscause pages 6-7, suenera2025acuteonchronica pages 4-6, suenera2025acuteonchronic pages 4-6, suenera2025acuteonchronicd pages 4-6, yadav2026infantileliverfailure pages 10-12, lenz2018scyl1variantscause pages 1-2) |
| Chronic hepatic monitoring | Longitudinal hepatology follow-up between crises | Serial liver biochemistry and synthetic function monitoring; nutritional optimization; cholestasis/pruritus management; surveillance for fibrosis/cirrhosis; monitoring for hepatosplenomegaly and growth failure | Lenz et al. reported fibrosis in all 7/7 patients despite transient crises; later reports emphasize chronic surveillance because apparent inter-episodic recovery does not exclude progression | (lenz2018scyl1variantscause pages 6-7, yadav2026infantileliverfailure pages 8-10, yadav2026infantileliverfailure pages 10-12) |
| Neurologic monitoring | Serial neurology assessment and imaging | Ongoing assessment for gait decline, tremor, peripheral neuropathy, speech/language delay, cerebellar ataxia/atrophy; repeat brain MRI may be needed because early imaging can be nondiagnostic | Neurologic progression may continue even when hepatic disease stabilizes or after liver transplantation | (yadav2026infantileliverfailure pages 8-10, youssef2023calfan(lowγglutamyl pages 3-5, isa2023recurrentacuteliver pages 3-5, isa2023recurrentacuteliver pages 7-8) |
| Liver transplantation | Used for progressive/recurrent liver failure not controlled by supportive care | In the foundational cohort, 1 child underwent transplant at 23 months; by 2023 literature review, 3 prior CALFAN patients had undergone transplant in infancy/early childhood at 7, 21, and 23 months; Youssef et al. added a transplant in adulthood at age 20 years | Adult-transplanted patient was doing well at 3-year follow-up; no acute cellular rejection reported; prior transplanted cases reportedly had no graft failure with 8-11 years follow-up; neurologic deficits may persist/progress despite hepatic stabilization | (lenz2018scyl1variantscause pages 6-7, youssef2023calfan(lowγglutamyl pages 3-5, youssef2023calfan(lowγglutamyl pages 1-2, youssef2023calfan(lowγglutamyl pages 2-3) |
| Post-transplant expectations | Hepatic benefit but incomplete extrahepatic rescue | Adult case most recent labs after transplant: TB 2.1 mg/dL, direct bilirubin 0.4 mg/dL, ALP 72 IU/L, ALT 18 IU/L, AST 13 IU/L, GGT 4 U/L; persistent cerebellar atrophy, leg-brace use, and limited expressive language remained | Supports transplant as liver-directed therapy rather than cure of neurodegeneration | (youssef2023calfan(lowγglutamyl pages 3-5, youssef2023calfan(lowγglutamyl pages 2-3) |
| Rehabilitation / physiotherapy (published case report) | Individualized 12-week physical therapy program | 45-minute sessions, 3 days/week; trunk stabilization, balance training, functional exercises, Swiss-ball and perturbation-based training, scoliosis brace/orthosis support, thoracic expansion and diaphragmatic breathing exercises | Quantitative changes: ICARS 47→42; TIS 9→13; WeeFIM 79→83; PedsQL 47.11→52.17; Q-DASH 59→56; 9-HPT right 48.8s→42.9s, left 66.1s→56.4s; thoracic Cobb 34°→36°, lumbar Cobb 32°→21° | (yigit2022theoutcomesof pages 3-4, yigit2022theoutcomesof pages 2-3, yigit2022theoutcomesof pages 1-2, yigit2022theoutcomesof pages 5-6) |
| Rehabilitation / physiotherapy (registered study) | Prospective single-case interventional rehabilitation study | ClinicalTrials.gov NCT04653909; single-group, enrollment=1; start 2020-03-01, primary completion 2020-10-20, study completion 2020-11-17; intervention included abdominal/back strengthening, perturbation training in sitting/standing, functional ADL-simulating exercises, scoliosis stretching/strengthening, and trunk orthoses | Primary outcomes: TIS, ICARS, PedsQL, WeeFIM; secondary: 9-Hole Peg Test and Q-DASH; record describes CALFAN as ultra-rare with ~11 reported patients at time of registration | (NCT04653909 chunk 1) |
| Diagnostic implementation in acute care | Early exome/genomic testing to clarify etiology of indeterminate pediatric ALF / low-GGT cholestasis | Whole-exome sequencing repeatedly enabled diagnosis in reported patients, including urgent-care contexts and cases considered for transplant; suggested especially when fever-triggered recurrent ALF occurs with neurologic signs or consanguinity/family history | Rapid molecular diagnosis informs prognosis, recurrence risk, and transplant decision-making | (isa2023recurrentacuteliver pages 1-3, isa2023recurrentacuteliver pages 7-8, lenz2018scyl1variantscause pages 1-2) |
| Genetic counseling / prevention | Family counseling, cascade testing, reproductive planning | Autosomal recessive inheritance; recurrence-risk counseling recommended; prenatal and preimplantation genetic testing options noted in recent review/case literature; family history of unexplained infantile liver failure is an important clue | No primary prevention for the genetic disorder itself; practical prevention focuses on anticipatory guidance, early evaluation of febrile illnesses, and reproductive counseling for at-risk families | (yadav2026infantileliverfailure pages 6-7, yadav2026infantileliverfailure pages 10-12, isa2023recurrentacuteliver pages 1-3) |
| Tertiary prevention / complication reduction | Avoidance of hepatotoxic stressors and prompt treatment of intercurrent infections | Suggested measures include early treatment/prevention of infections, hydration/nutritional support during illness, avoidance of hepatotoxic drugs, and multidisciplinary follow-up (hepatology, neurology, genetics, rehabilitation) | Intended to reduce severity of recurrent decompensation and preserve function/QoL, though controlled evidence is lacking because of extreme rarity | (suenera2025acuteonchronic pages 4-6, suenera2025acuteonchronicd pages 4-6, yadav2026infantileliverfailure pages 10-12, yigit2022theoutcomesof pages 4-5) |


*Table: This table summarizes current real-world management approaches reported for CALFAN syndrome, including acute liver crisis care, chronic surveillance, transplantation, rehabilitation, and genetic counseling. It also captures the limited quantitative outcome data available from case reports and the single registered rehabilitation study.*

---

## 13. Prevention
- **Primary prevention**: not available for an inherited SCYL1 loss-of-function disorder.
- **Secondary/tertiary prevention (practical)**: anticipatory guidance and rapid evaluation/treatment of febrile illnesses; avoidance of hepatotoxic exposures; longitudinal monitoring for hepatic decompensation and neurologic progression. (yadav2026infantileliverfailure pages 10-12, yadav2026infantileliverfailure pages 8-10)
- **Genetic counseling**: autosomal recessive recurrence-risk counseling and reproductive options (prenatal/preimplantation genetic testing) are recommended in case-based literature. (yadav2026infantileliverfailure pages 6-7, yadav2026infantileliverfailure pages 10-12)

---

## 14. Other species / natural disease
No naturally occurring veterinary CALFAN/SCYL1-deficiency syndrome data were identified in the retrieved sources.

---

## 15. Model organisms
- Evidence from an experimental dissertation indicates mouse Scyl1 loss causes motor neuron disease and cerebellar degeneration and provides trafficking interaction insights (COPI/COPII). (hellicar2021investigatingtherole pages 106-111, hellicar2021investigatingtherole pages 35-38)

---

## Direct quotes from abstracts (available in retrieved evidence)
- Foundational cohort definition: “**SCYL1 variants cause a syndrome with low γ-glutamyl-transferase cholestasis, acute liver failure, and neurodegeneration (CALFAN)**.” (Genetics in Medicine; 2018) (lenz2018scyl1variantscause pages 1-2)
- Trafficking/therapeutic framing: the 2024 review notes it “**explore[s] the emerging knowledge on intracellular trafficking defects and their clinical manifestations** … [and that] **understanding these processes could spark novel therapeutic approaches**.” (Traffic; 2024) (szabo2024intracellulartraffickingdefects pages 1-2)

---

## Notes on evidence gaps and recommended next steps for curation
- **Ontology identifiers** (MONDO/Orphanet/ICD/MeSH) were not present in the retrieved texts; verify in OMIM/Orphanet/MONDO directly.
- **Variant catalog completeness**: the foundational cohort’s specific HGVS variants were not extracted from the available evidence snippets; full-text variant tables should be consulted to populate ClinVar-style variant lists.
- **Epidemiology**: only case-count statements are available; no population prevalence data identified.



References

1. (lenz2018scyl1variantscause pages 6-7): Dominic Lenz, Patricia McClean, Aydan Kansu, Penelope E. Bonnen, Giusy Ranucci, Christian Thiel, Beate K. Straub, Inga Harting, Bader Alhaddad, Bianca Dimitrov, Urania Kotzaeridou, Daniel Wenning, Raffaele Iorio, Ryan W. Himes, Zarife Kuloğlu, Emma L. Blakely, Robert W. Taylor, Thomas Meitinger, Stefan Kölker, Holger Prokisch, Georg F. Hoffmann, Tobias B. Haack, and Christian Staufner. Scyl1 variants cause a syndrome with lowγ-glutamyl-transferase cholestasis, acute liver failure, and neurodegeneration (calfan). Genetics in Medicine, 20:1255-1265, Oct 2018. URL: https://doi.org/10.1038/gim.2017.260, doi:10.1038/gim.2017.260. This article has 78 citations and is from a highest quality peer-reviewed journal.

2. (lenz2018scyl1variantscause pages 1-2): Dominic Lenz, Patricia McClean, Aydan Kansu, Penelope E. Bonnen, Giusy Ranucci, Christian Thiel, Beate K. Straub, Inga Harting, Bader Alhaddad, Bianca Dimitrov, Urania Kotzaeridou, Daniel Wenning, Raffaele Iorio, Ryan W. Himes, Zarife Kuloğlu, Emma L. Blakely, Robert W. Taylor, Thomas Meitinger, Stefan Kölker, Holger Prokisch, Georg F. Hoffmann, Tobias B. Haack, and Christian Staufner. Scyl1 variants cause a syndrome with lowγ-glutamyl-transferase cholestasis, acute liver failure, and neurodegeneration (calfan). Genetics in Medicine, 20:1255-1265, Oct 2018. URL: https://doi.org/10.1038/gim.2017.260, doi:10.1038/gim.2017.260. This article has 78 citations and is from a highest quality peer-reviewed journal.

3. (isa2023recurrentacuteliver pages 3-5): Hasan M Isa, Jawaher F Alkaabi, Wasan H Alhammadi, and Khadija A Marjan. Recurrent acute liver failure in a bahraini child with a novel mutation of spinocerebellar ataxia-21. Cureus, Mar 2023. URL: https://doi.org/10.7759/cureus.36249, doi:10.7759/cureus.36249. This article has 6 citations.

4. (youssef2023calfan(lowγglutamyl pages 3-5): Mariam Youssef, Katherine L. Mascia, Brendan McGuire, Chirag R. Patel, Sameer Al Diffalha, Deepti Dhall, and Goo Lee. Calfan (low γ-glutamyl transpeptidase (ggt) cholestasis, acute liver failure, and neurodegeneration) syndrome: a case report with 3-year follow-up after liver transplantation in early adulthood. Case Reports in Hepatology, 2023:1-5, Jul 2023. URL: https://doi.org/10.1155/2023/3010131, doi:10.1155/2023/3010131. This article has 6 citations.

5. (szabo2024intracellulartraffickingdefects pages 7-8): Luca Szabó, Adam R. Pollio, and Georg Friedrich Vogel. Intracellular trafficking defects in congenital intestinal and hepatic diseases. Traffic, Aug 2024. URL: https://doi.org/10.1111/tra.12954, doi:10.1111/tra.12954. This article has 2 citations and is from a peer-reviewed journal.

6. (szabo2024intracellulartraffickingdefects pages 1-2): Luca Szabó, Adam R. Pollio, and Georg Friedrich Vogel. Intracellular trafficking defects in congenital intestinal and hepatic diseases. Traffic, Aug 2024. URL: https://doi.org/10.1111/tra.12954, doi:10.1111/tra.12954. This article has 2 citations and is from a peer-reviewed journal.

7. (demir2023coexistenceofspinocerebellar pages 3-4): Engin Demir, Ümmühan Öncül, Merve Havan, Ceyda Tuna Kirsaçlioğlu, Fatma Tuba Eminoğlu, Tanil Kendirli, Zarife Kuloğlu, and Aydan Kansu. Coexistence of spinocerebellar ataxia autosomal recessive type 21 and ehlers-danlos syndrome spondylodysplastic type 3 in a patient. Clinical dysmorphology, 32 1:25-28, Nov 2023. URL: https://doi.org/10.1097/mcd.0000000000000435, doi:10.1097/mcd.0000000000000435. This article has 0 citations and is from a peer-reviewed journal.

8. (yadav2026infantileliverfailure pages 6-7): Deepika Yadav, Nishant Wadhwa, and Megha Sharma. Infantile liver failure as the initial manifestation of scyl1-related calfan syndrome: a case report and literature review. Archives of Pediatric Gastroenterology, Hepatology, and Nutrition, 5:86-97, May 2026. URL: https://doi.org/10.58427/apghn.5.2.2026.86-97, doi:10.58427/apghn.5.2.2026.86-97. This article has 0 citations.

9. (yadav2026infantileliverfailure pages 10-12): Deepika Yadav, Nishant Wadhwa, and Megha Sharma. Infantile liver failure as the initial manifestation of scyl1-related calfan syndrome: a case report and literature review. Archives of Pediatric Gastroenterology, Hepatology, and Nutrition, 5:86-97, May 2026. URL: https://doi.org/10.58427/apghn.5.2.2026.86-97, doi:10.58427/apghn.5.2.2026.86-97. This article has 0 citations.

10. (yadav2026infantileliverfailure pages 8-10): Deepika Yadav, Nishant Wadhwa, and Megha Sharma. Infantile liver failure as the initial manifestation of scyl1-related calfan syndrome: a case report and literature review. Archives of Pediatric Gastroenterology, Hepatology, and Nutrition, 5:86-97, May 2026. URL: https://doi.org/10.58427/apghn.5.2.2026.86-97, doi:10.58427/apghn.5.2.2026.86-97. This article has 0 citations.

11. (NCT04653909 chunk 1): Serkan Usgu. The Physiotherapy and Rehabilitation in Calfan Syndrome. Hasan Kalyoncu University. 2020. ClinicalTrials.gov Identifier: NCT04653909

12. (kaeserpebernard2022mtorc1controlsgolgi pages 2-3): Stéphanie Kaeser-Pebernard, Christine Vionnet, Muriel Mari, Devanarayanan Siva Sankar, Zehan Hu, Carole Roubaty, Esther Martínez-Martínez, Huiyuan Zhao, Miguel Spuch-Calvar, Alke Petri-Fink, Gregor Rainer, Florian Steinberg, Fulvio Reggiori, and Jörn Dengjel. Mtorc1 controls golgi architecture and vesicle secretion by phosphorylation of scyl1. Nature Communications, Aug 2022. URL: https://doi.org/10.1038/s41467-022-32487-7, doi:10.1038/s41467-022-32487-7. This article has 35 citations and is from a highest quality peer-reviewed journal.

13. (kaeserpebernard2022mtorc1controlsgolgi pages 1-2): Stéphanie Kaeser-Pebernard, Christine Vionnet, Muriel Mari, Devanarayanan Siva Sankar, Zehan Hu, Carole Roubaty, Esther Martínez-Martínez, Huiyuan Zhao, Miguel Spuch-Calvar, Alke Petri-Fink, Gregor Rainer, Florian Steinberg, Fulvio Reggiori, and Jörn Dengjel. Mtorc1 controls golgi architecture and vesicle secretion by phosphorylation of scyl1. Nature Communications, Aug 2022. URL: https://doi.org/10.1038/s41467-022-32487-7, doi:10.1038/s41467-022-32487-7. This article has 35 citations and is from a highest quality peer-reviewed journal.

14. (isa2023recurrentacuteliver pages 1-3): Hasan M Isa, Jawaher F Alkaabi, Wasan H Alhammadi, and Khadija A Marjan. Recurrent acute liver failure in a bahraini child with a novel mutation of spinocerebellar ataxia-21. Cureus, Mar 2023. URL: https://doi.org/10.7759/cureus.36249, doi:10.7759/cureus.36249. This article has 6 citations.

15. (isa2023recurrentacuteliver pages 5-6): Hasan M Isa, Jawaher F Alkaabi, Wasan H Alhammadi, and Khadija A Marjan. Recurrent acute liver failure in a bahraini child with a novel mutation of spinocerebellar ataxia-21. Cureus, Mar 2023. URL: https://doi.org/10.7759/cureus.36249, doi:10.7759/cureus.36249. This article has 6 citations.

16. (youssef2023calfan(lowγglutamyl pages 2-3): Mariam Youssef, Katherine L. Mascia, Brendan McGuire, Chirag R. Patel, Sameer Al Diffalha, Deepti Dhall, and Goo Lee. Calfan (low γ-glutamyl transpeptidase (ggt) cholestasis, acute liver failure, and neurodegeneration) syndrome: a case report with 3-year follow-up after liver transplantation in early adulthood. Case Reports in Hepatology, 2023:1-5, Jul 2023. URL: https://doi.org/10.1155/2023/3010131, doi:10.1155/2023/3010131. This article has 6 citations.

17. (yigit2022theoutcomesof pages 1-2): Sedat Yigit, Hatice Mutlu Albayrak, Peren Perk Yücel, Serkan Usgu, and Yavuz Yakut. The outcomes of an individualized physical therapy program in calfan syndrome: a case report. Pediatric Physical Therapy, 34:432-437, May 2022. URL: https://doi.org/10.1097/pep.0000000000000903, doi:10.1097/pep.0000000000000903. This article has 3 citations and is from a peer-reviewed journal.

18. (yigit2022theoutcomesof pages 5-6): Sedat Yigit, Hatice Mutlu Albayrak, Peren Perk Yücel, Serkan Usgu, and Yavuz Yakut. The outcomes of an individualized physical therapy program in calfan syndrome: a case report. Pediatric Physical Therapy, 34:432-437, May 2022. URL: https://doi.org/10.1097/pep.0000000000000903, doi:10.1097/pep.0000000000000903. This article has 3 citations and is from a peer-reviewed journal.

19. (yigit2022theoutcomesof pages 2-3): Sedat Yigit, Hatice Mutlu Albayrak, Peren Perk Yücel, Serkan Usgu, and Yavuz Yakut. The outcomes of an individualized physical therapy program in calfan syndrome: a case report. Pediatric Physical Therapy, 34:432-437, May 2022. URL: https://doi.org/10.1097/pep.0000000000000903, doi:10.1097/pep.0000000000000903. This article has 3 citations and is from a peer-reviewed journal.

20. (suenera2025acuteonchronica pages 4-6): DR SUENERA and DR NAVINUMAPATHY. Acute on chronic liver disease in a child with scyl1 mutation: a rare pediatric case report. Unknown journal, 2025.

21. (suenera2025acuteonchronic pages 4-6): DR SUENERA and DR NAVINUMAPATHY. Acute on chronic liver disease in a child with scyl1 mutation: a rare pediatric case report. Unknown journal, 2025.

22. (isa2023recurrentacuteliver pages 7-8): Hasan M Isa, Jawaher F Alkaabi, Wasan H Alhammadi, and Khadija A Marjan. Recurrent acute liver failure in a bahraini child with a novel mutation of spinocerebellar ataxia-21. Cureus, Mar 2023. URL: https://doi.org/10.7759/cureus.36249, doi:10.7759/cureus.36249. This article has 6 citations.

23. (youssef2023calfan(lowγglutamyl pages 1-2): Mariam Youssef, Katherine L. Mascia, Brendan McGuire, Chirag R. Patel, Sameer Al Diffalha, Deepti Dhall, and Goo Lee. Calfan (low γ-glutamyl transpeptidase (ggt) cholestasis, acute liver failure, and neurodegeneration) syndrome: a case report with 3-year follow-up after liver transplantation in early adulthood. Case Reports in Hepatology, 2023:1-5, Jul 2023. URL: https://doi.org/10.1155/2023/3010131, doi:10.1155/2023/3010131. This article has 6 citations.

24. (suenera2025acuteonchronicc pages 4-6): DR SUENERA and DR NAVINUMAPATHY. Acute on chronic liver disease in a child with scyl1 mutation: a rare pediatric case report. Unknown journal, 2025.

25. (suenera2025acuteonchronicd pages 4-6): DR SUENERA and DR NAVINUMAPATHY. Acute on chronic liver disease in a child with scyl1 mutation: a rare pediatric case report. Unknown journal, 2025.

26. (hellicar2021investigatingtherole pages 35-38): JP Hellicar. Investigating the role of scyl1 in the secretory pathway and how its loss causes disease in humans. Unknown journal, 2021.

27. (kaeserpebernard2022mtorc1controlsgolgi pages 7-8): Stéphanie Kaeser-Pebernard, Christine Vionnet, Muriel Mari, Devanarayanan Siva Sankar, Zehan Hu, Carole Roubaty, Esther Martínez-Martínez, Huiyuan Zhao, Miguel Spuch-Calvar, Alke Petri-Fink, Gregor Rainer, Florian Steinberg, Fulvio Reggiori, and Jörn Dengjel. Mtorc1 controls golgi architecture and vesicle secretion by phosphorylation of scyl1. Nature Communications, Aug 2022. URL: https://doi.org/10.1038/s41467-022-32487-7, doi:10.1038/s41467-022-32487-7. This article has 35 citations and is from a highest quality peer-reviewed journal.

28. (hellicar2021investigatingtherole pages 106-111): JP Hellicar. Investigating the role of scyl1 in the secretory pathway and how its loss causes disease in humans. Unknown journal, 2021.

29. (yadav2026infantileliverfailure pages 1-3): Deepika Yadav, Nishant Wadhwa, and Megha Sharma. Infantile liver failure as the initial manifestation of scyl1-related calfan syndrome: a case report and literature review. Archives of Pediatric Gastroenterology, Hepatology, and Nutrition, 5:86-97, May 2026. URL: https://doi.org/10.58427/apghn.5.2.2026.86-97, doi:10.58427/apghn.5.2.2026.86-97. This article has 0 citations.

30. (yadav2026infantileliverfailure pages 3-6): Deepika Yadav, Nishant Wadhwa, and Megha Sharma. Infantile liver failure as the initial manifestation of scyl1-related calfan syndrome: a case report and literature review. Archives of Pediatric Gastroenterology, Hepatology, and Nutrition, 5:86-97, May 2026. URL: https://doi.org/10.58427/apghn.5.2.2026.86-97, doi:10.58427/apghn.5.2.2026.86-97. This article has 0 citations.

31. (yigit2022theoutcomesof pages 3-4): Sedat Yigit, Hatice Mutlu Albayrak, Peren Perk Yücel, Serkan Usgu, and Yavuz Yakut. The outcomes of an individualized physical therapy program in calfan syndrome: a case report. Pediatric Physical Therapy, 34:432-437, May 2022. URL: https://doi.org/10.1097/pep.0000000000000903, doi:10.1097/pep.0000000000000903. This article has 3 citations and is from a peer-reviewed journal.

32. (yigit2022theoutcomesof pages 4-5): Sedat Yigit, Hatice Mutlu Albayrak, Peren Perk Yücel, Serkan Usgu, and Yavuz Yakut. The outcomes of an individualized physical therapy program in calfan syndrome: a case report. Pediatric Physical Therapy, 34:432-437, May 2022. URL: https://doi.org/10.1097/pep.0000000000000903, doi:10.1097/pep.0000000000000903. This article has 3 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](CALFAN_Syndrome-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](CALFAN_Syndrome-deep-research-falcon_artifacts/artifact-01.md)
- [Edison artifact artifact-02](CALFAN_Syndrome-deep-research-falcon_artifacts/artifact-02.md)
- [Edison artifact artifact-03](CALFAN_Syndrome-deep-research-falcon_artifacts/artifact-03.md)