---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-19T09:11:39.877776'
end_time: '2026-06-19T09:23:49.857199'
duration_seconds: 729.98
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Late Complement Component Deficiency
  mondo_id: ''
  category: Complex
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 24
artifact_count: 3
artifact_sources:
  edison_answer_artifacts: 3
artifacts:
- filename: artifact-00.md
  path: Late_Complement_Component_Deficiency-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: Late_Complement_Component_Deficiency-deep-research-falcon_artifacts/artifact-01.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-01
- filename: artifact-02.md
  path: Late_Complement_Component_Deficiency-deep-research-falcon_artifacts/artifact-02.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-02
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Late Complement Component Deficiency
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Late Complement Component Deficiency** covering all of the
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
- **Disease Name:** Late Complement Component Deficiency
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Late Complement Component Deficiency** covering all of the
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


# Comprehensive Research Report: Late Complement Component Deficiency

## Executive Summary

Late complement component deficiency (also known as **terminal complement pathway deficiency**) refers to inherited deficiencies affecting complement components C5, C6, C7, C8, or C9, which are essential for formation of the membrane attack complex (MAC; C5b-9). These rare, autosomal recessive disorders confer a dramatically increased susceptibility to invasive infections by *Neisseria* species, particularly *Neisseria meningitidis* (meningococcemia and meningitis) and *Neisseria gonorrhoeae* (disseminated gonococcal infection). The disease is characterized by recurrent, potentially fatal invasive bacterial infections despite the ability to mount antibody responses. Timely diagnosis through complement functional assays (CH50/AH50), specific component measurement, and genetic testing enables lifelong preventive strategies including vaccination, antibiotic prophylaxis, and family screening (brodszki2020europeansocietyfor pages 1-2, shears2022clinicaloutcomeand pages 1-2, balduit2023geneticbasesof pages 1-2, mcmurray2024immunodeficiencycomplementdisorders. pages 1-2, brodszki2020europeansocietyfor pages 10-12).

---

## 1. Disease Information

### Overview

Late complement component deficiency is a group of rare primary immunodeficiencies (PIDs) caused by inherited defects in the terminal complement components C5, C6, C7, C8, or C9. These proteins sequentially assemble the membrane attack complex (MAC or C5b-9), which forms transmembrane pores that lyse Gram-negative bacteria and other target cells (brodszki2020europeansocietyfor pages 1-2, hodeib2020humangeneticsof pages 2-4). 

The complement system comprises over 30 proteins and is organized into three activation pathways—classical, lectin, and alternative—that converge at C3 cleavage and then proceed through a common terminal pathway involving C5 through C9. Complement deficiencies collectively account for approximately 5% of all reported primary immunodeficiencies, though they are likely underdiagnosed (brodszki2020europeansocietyfor pages 1-2). The European Society for Immunodeficiencies (ESID) guideline states: "The complement system is a crucial part of the innate immune system, with multiple membrane-bound and soluble components... Complement deficiencies account for ~5% of PIDs" (brodszki2020europeansocietyfor pages 1-2).

### Synonyms and Alternative Names

- Terminal complement pathway deficiency
- Terminal complement component deficiency
- MAC deficiency (membrane attack complex deficiency)
- C5-C9 deficiency (component-specific)
- Late-acting complement deficiency

### Key Identifiers

**OMIM:** C6 deficiency has OMIM ID **612446** (li2020novelpathogenicmutations pages 1-2). OMIM identifiers for C5, C7, C8, and C9 deficiencies were not definitively confirmed in the retrieved literature, though these disorders are well-characterized genetically.

**Orphanet, ICD-10/11, MeSH, MONDO:** Specific coding details were not available in the retrieved sources. The disease would be classified under broader complement deficiency and immunodeficiency categories.

**Data Source:** Information is derived from aggregated disease-level resources (clinical cohorts, systematic reviews, case series) and molecular genetics studies, not individual patient EHR data (shears2022clinicaloutcomeand pages 1-2, balduit2023geneticbasesof pages 1-2, shears2022clinicaloutcomeand pages 2-5, balduit2023geneticbasesof pages 2-4).

---

## 2. Etiology

### Disease Causal Factors

**Primary Genetic Cause:**  
Late complement component deficiency results from germline mutations in the genes encoding C5 (chromosome 9q33.2), C6 (5p13), C7 (5p13), C8A/C8B (1p32) and C8G (9q34), or C9 (5p14-p12). These mutations lead to absent or severely reduced serum levels of the affected component, disrupting MAC formation (szymanska2024molecularaspectsof pages 1-2, li2020novelpathogenicmutations pages 1-2, brodszki2020europeansocietyfor pages 5-6).

C8 deficiency involves three subunit genes: C8A and C8B (encoding the alpha and beta chains that form a heterodimer) and C8G (encoding the gamma chain). Deficiency of any subunit can cause functional C8 deficiency (brodszki2020europeansocietyfor pages 5-6).

**Mechanistic Basis:**  
The terminal pathway begins when C5 convertase cleaves C5 into C5a (an inflammatory anaphylatoxin) and C5b. C5b binds C6 and C7, forming a complex that inserts into target membranes. C8 then binds, and multiple C9 molecules polymerize to create the lytic MAC pore. Without functional MAC, serum bactericidal activity against pathogenic *Neisseria* is lost, despite intact opsonization and antibody responses (hodeib2020humangeneticsof pages 2-4, szymanska2024molecularaspectsof pages 1-2).

### Risk Factors

**Genetic Risk Factors:**
- **Autosomal recessive inheritance:** All terminal complement deficiencies are inherited in an autosomal recessive pattern (brodszki2020europeansocietyfor pages 1-2, brodszki2020europeansocietyfor pages 5-6).
- **Consanguinity:** In a UK multicenter cohort of 40 patients with terminal complement deficiency, 65% had consanguineous parenthood, and 80% had a family history of the condition (shears2022clinicaloutcomeand pages 1-2, shears2022clinicaloutcomeand pages 2-5).
- **Founder effects:** Strong founder effects exist in specific populations:
  - **C7 deficiency:** 1:400 in Israeli Moroccan Jews (sullivan2026complementdeficiencies pages 1-45, khalil2023thefirstcase pages 1-2)
  - **C6 deficiency:** 1:1400 in African Americans (sullivan2026complementdeficiencies pages 1-45)
  - **C9 deficiency:** 1:1000 in Japanese populations (sullivan2026complementdeficiencies pages 1-45, li2020novelpathogenicmutations pages 1-2)
  
**Environmental/Exposure Risk Factors:**
- Geographic residence in meningitis-endemic areas (e.g., sub-Saharan "meningitis belt") increases exposure risk (hodeib2020humangeneticsof pages 2-4).
- Occupational or social exposure to *Neisseria* (e.g., nursery workers, crowded living conditions) increases infection risk once deficiency is present (brodszki2020europeansocietyfor pages 10-12).

### Protective Factors

No intrinsic protective genetic variants within complement genes have been identified for terminal pathway deficiency. However, **preventive interventions** (vaccination, antibiotic prophylaxis, family screening) markedly reduce disease burden (see Section 12).

### Gene-Environment Interactions

Terminal complement deficiency confers susceptibility, but invasive disease requires environmental exposure to pathogenic *Neisseria*. Vaccination and hygiene measures reduce exposure, demonstrating gene-environment interaction in disease expression (brodszki2020europeansocietyfor pages 10-12).

---

## 3. Phenotypes

| Phenotype / Clinical Feature | HPO term suggestion | Frequency in affected individuals (with citation) | Age of onset | Severity description | Key notes / mechanism |
|---|---|---|---|---|---|
| Recurrent invasive meningococcal disease (meningococcal sepsis and/or meningitis) | HP:0005381 Recurrent bacterial infections; HP:0002718 Recurrent invasive bacterial infection; HP:0002013 Meningitis; HP:0100806 Sepsis | In a UK multicenter cohort of terminal pathway deficiency, 48% had meningococcal and/or other deep-seated bacterial infection; 45% had meningococcal septicemia and 18% meningococcal meningitis; median number of meningococcal infections was 1 (range 0–5). Reviews note ~40–50% of individuals with MAC-component deficiency experience meningococcal infections, and terminal pathway deficiency confers a 7,000- to 10,000-fold higher risk of invasive meningococcal disease (shears2022clinicaloutcomeand pages 1-2, shears2022clinicaloutcomeand pages 2-5, khalil2023thefirstcase pages 1-2, balduit2023geneticbasesof pages 1-2, hodeib2020humangeneticsof pages 2-4) | Usually childhood to adolescence; median age at first infection 9 years (range 1–25) in the UK cohort, but presentations can occur in adulthood (shears2022clinicaloutcomeand pages 1-2, shears2022clinicaloutcomeand pages 2-5, khalil2023thefirstcase pages 1-2) | Often severe but paradoxically may be less fulminant than properdin/factor D deficiency; 22% required ICU in the UK cohort; recurrence is common without recognition/prevention (shears2022clinicaloutcomeand pages 1-2, shears2022clinicaloutcomeand pages 2-5, sullivan2026complementdeficiencies pages 1-45) | Caused by inability to form membrane attack complex (MAC; C5b-9), impairing serum bactericidal activity against Neisseria meningitidis. Less common serotypes can predominate: among typed UK infections, 43% were serogroup B and 43% serogroup Y, with occasional W and E (shears2022clinicaloutcomeand pages 1-2, shears2022clinicaloutcomeand pages 2-5, khalil2023thefirstcase pages 1-2, hodeib2020humangeneticsof pages 2-4) |
| Recurrent meningococcal meningitis | HP:0001287 Meningitis | In the UK cohort, 18% had meningococcal meningitis; case reports describe repeated episodes, including 3 episodes in a Qatari man with C7 deficiency over time (shears2022clinicaloutcomeand pages 1-2, shears2022clinicaloutcomeand pages 2-5, khalil2023thefirstcase pages 1-2) | Often school age, adolescence, or young adulthood; case reports include onset at ages 7, 18, and 20 years in one patient (khalil2023thefirstcase pages 1-2) | Potentially life-threatening but survivors can recover fully; repeated episodes markedly affect schooling, work, and psychosocial security due to fear of recurrence (inferred from recurrent severe infection burden) (khalil2023thefirstcase pages 1-2, shears2022clinicaloutcomeand pages 1-2) | Reflects failed terminal complement-mediated killing in bloodstream/CSF. Patients may develop meningitis despite prior meningococcal vaccination if the underlying complement defect is unrecognized (khalil2023thefirstcase pages 1-2, balduit2023geneticbasesof pages 2-4) |
| Meningococcal septicemia / fulminant meningococcemia | HP:0100806 Sepsis | 45% in the UK cohort had meningococcal septicemia; septic presentation was a major risk factor for ICU admission (relative risk 16.3 in the cohort analysis) (shears2022clinicaloutcomeand pages 2-5) | Childhood through adulthood; median first infection age 9 years (shears2022clinicaloutcomeand pages 2-5) | High acute severity; 22% of the full cohort required intensive care; can be fatal (shears2022clinicaloutcomeand pages 1-2, shears2022clinicaloutcomeand pages 2-5) | Caused by bloodstream proliferation of Neisseria when MAC-dependent killing fails. Petechial rash and shock may occur, as in reported C7-deficient children with meningococcal sepsis (khalil2023thefirstcase pages 1-2, balduit2023geneticbasesof pages 2-4) |
| Chronic meningococcemia | HP:0002718 Recurrent invasive bacterial infection; HP:0001945 Fever; HP:0000988 Skin rash | Reported as a recognized phenotype of terminal complement deficiency in expert review/teaching materials, but no robust percentage available from the recent cohort literature reviewed here (sullivan2026complementdeficiencies pages 1-45) | Variable; often later childhood to adulthood based on historical phenotype descriptions (sullivan2026complementdeficiencies pages 1-45) | Typically subacute/relapsing rather than fulminant; may impair quality of life through prolonged fever, rash, arthralgia, and repeated healthcare visits (sullivan2026complementdeficiencies pages 1-45) | Represents persistent or recurrent meningococcal bacteremia due to incomplete bacterial clearance in MAC deficiency (sullivan2026complementdeficiencies pages 1-45, hodeib2020humangeneticsof pages 2-4) |
| Meningococcal arthritis / septic arthritis | HP:0001386 Arthritis; HP:0002758 Septic arthritis | 8% had meningococcal arthritis in the UK cohort (shears2022clinicaloutcomeand pages 2-5) | Usually pediatric to young adult, often accompanying invasive infection (shears2022clinicaloutcomeand pages 2-5) | Moderate to severe; joint pain and functional limitation can affect mobility and daily activities during episodes (shears2022clinicaloutcomeand pages 2-5) | May occur as a focal complication of invasive meningococcal infection in terminal pathway deficiency (shears2022clinicaloutcomeand pages 2-5) |
| Disseminated gonococcal infection | HP term not specific; suggest HP:0002718 Recurrent invasive bacterial infection | Recognized hallmark susceptibility in terminal complement deficiency; recent mechanistic review notes individuals lacking terminal complement have >300-fold increased susceptibility to local and disseminated Neisseria gonorrhoeae infection, but disease-specific cohort frequency in inherited deficiency is not well quantified in the retrieved sources (sullivan2026complementdeficiencies pages 1-45, hodeib2020humangeneticsof pages 1-2) | Typically after sexual debut / adolescence or adulthood (sullivan2026complementdeficiencies pages 1-45) | Can be severe and recurrent; may present with bacteremia, arthritis, dermatitis, and hospitalization; important counseling implication for adolescents/adults (sullivan2026complementdeficiencies pages 1-45, hodeib2020humangeneticsof pages 1-2) | MAC is a major defense against pathogenic Neisseria species beyond N. meningitidis. Terminal complement failure impairs gonococcal killing and increases dissemination risk (hodeib2020humangeneticsof pages 1-2) |
| Non-meningococcal deep bacterial infections | HP:0002718 Recurrent invasive bacterial infection | 34% had non-meningococcal sepsis and related serious bacterial infections in the UK cohort, including respiratory infection, pyogenic meningitis, osteomyelitis/septic arthritis, and skin/soft tissue infection (shears2022clinicaloutcomeand pages 2-5) | Variable, from infancy to adulthood (shears2022clinicaloutcomeand pages 2-5) | Variable; can include serious invasive disease, though Neisseria susceptibility remains the dominant phenotype (shears2022clinicaloutcomeand pages 1-2, shears2022clinicaloutcomeand pages 2-5) | Terminal complement defects primarily impair killing of Neisseria, but some patients also develop other invasive bacterial infections, likely reflecting broader compromise in bactericidal activity against select encapsulated/Gram-negative organisms (brodszki2020europeansocietyfor pages 1-2, shears2022clinicaloutcomeand pages 2-5) |
| Asymptomatic carrier state / family-identified disease | No direct HPO disease-feature term; consider HP:0033704 Reduced complement activity | 52% of the UK cohort were asymptomatic and diagnosed because of family history; 80% had an affected family member (shears2022clinicaloutcomeand pages 1-2, shears2022clinicaloutcomeand pages 2-5) | Congenital/genetic, often detected only after a relative is diagnosed (shears2022clinicaloutcomeand pages 1-2, shears2022clinicaloutcomeand pages 2-5) | Clinically silent until first invasive infection; nevertheless high lifelong infection risk mandates prevention planning (shears2022clinicaloutcomeand pages 1-2, shears2022clinicaloutcomeand pages 2-5, brodszki2020europeansocietyfor pages 10-12) | Important knowledge-base phenotype because absence of prior infection does not exclude severe risk. Family screening is therefore a major secondary-prevention strategy (shears2022clinicaloutcomeand pages 1-2, shears2022clinicaloutcomeand pages 2-5, brodszki2020europeansocietyfor pages 10-12) |
| Laboratory phenotype: absent CH50 and AH50 (except some C9-deficient cases may show residual activity) | HP:0012378 Abnormal complement system physiology; HP:0033704 Reduced complement activity | Functional terminal pathway deficiency characteristically shows absent or markedly reduced classical and alternative pathway hemolytic activity; examples include C7-deficient case with classical 0.6%, lectin 0.2%, alternative 0.1% activity (balduit2023geneticbasesof pages 1-2, balduit2023geneticbasesof pages 2-4, sullivan2026complementdeficiencies pages 1-45) | Congenital; detectable at any age once tested | Usually a stable constitutional laboratory abnormality outside periods of consumption from sepsis or inflammatory disease (sullivan2026complementdeficiencies pages 1-45, balduit2023geneticbasesof pages 1-2) | Core diagnostic phenotype caused by failure to assemble C5b-9; often accompanied by absent specific terminal component antigen/protein (e.g., absent C7 on Western blot) (balduit2023geneticbasesof pages 1-2, balduit2023geneticbasesof pages 2-4) |
| Autoimmune manifestations | HP:0002960 Autoimmunity | Much less prominent than in early classical pathway deficiencies; terminal pathway deficiency is described mainly as an infection phenotype. Reviews of complement deficiency note autoimmunity can occur across complement disorders broadly, but recent terminal-pathway cohorts emphasize invasive infection rather than autoimmune disease, and no strong frequency estimate was identified for C5-C9 deficiency specifically (brodszki2020europeansocietyfor pages 1-2, balduit2023geneticbasesof pages 1-2, mcmurray2024immunodeficiencycomplementdisorders. pages 1-2) | Variable / not well defined for terminal pathway deficiency | Usually not the dominant clinical problem in late complement deficiency (brodszki2020europeansocietyfor pages 1-2, mcmurray2024immunodeficiencycomplementdisorders. pages 1-2) | Unlike C1/C2/C4 deficiency, C5-C9 deficiency chiefly disrupts MAC-mediated bacterial lysis, so mechanistic linkage is strongest for Neisseria susceptibility rather than immune-complex autoimmunity (brodszki2020europeansocietyfor pages 1-2, hodeib2020humangeneticsof pages 2-4, mcmurray2024immunodeficiencycomplementdisorders. pages 1-2) |
| Mortality and long-term outcome | HP:0003819 Recurrent infection; HP:0001699 Sudden death not usually applicable; no ideal single HPO term | In the UK cohort, 2/40 patients (5%) had died; one death was directly attributed to complement-deficiency-associated fulminant pneumococcal meningitis in infancy, one to intercurrent COVID-19. Most surviving patients can remain well with vaccination, prophylactic antibiotics, and emergency planning; e.g., a C7-deficient patient remained free of further meningitis over 10 years after preventive management (shears2022clinicaloutcomeand pages 1-2, shears2022clinicaloutcomeand pages 2-5, khalil2023thefirstcase pages 1-2) | Lifelong risk, greatest once exposed to pathogenic Neisseria; can begin in infancy/childhood (shears2022clinicaloutcomeand pages 1-2, shears2022clinicaloutcomeand pages 2-5) | Prognosis improves substantially with diagnosis and prevention, but acute episodes may be fatal or ICU-level severe (shears2022clinicaloutcomeand pages 1-2, shears2022clinicaloutcomeand pages 2-5, brodszki2020europeansocietyfor pages 10-12) | Quality-of-life burden derives from recurrent life-threatening infection risk, repeated vaccination/antibiotic regimens, emergency planning, and family screening obligations; preventive care can markedly reduce recurrence (khalil2023thefirstcase pages 1-2, brodszki2020europeansocietyfor pages 10-12) |


*Table: This table summarizes the main clinical manifestations and laboratory phenotypes of late/terminal complement component deficiency (C5-C9), with HPO suggestions, frequencies, onset patterns, and mechanistic notes. It is useful for phenotype curation and clinical knowledge-base population.*

### Key Clinical Phenotypes

**Recurrent Invasive Meningococcal Disease** is the hallmark phenotype. Patients have a 7,000- to 10,000-fold increased risk of invasive meningococcal disease compared to the general population (shears2022clinicaloutcomeand pages 1-2). In a large UK multicenter cohort, 48% had a history of meningococcal or other deep-seated bacterial infections, with median age at first infection of 9 years (range 1-25 years) (shears2022clinicaloutcomeand pages 1-2, shears2022clinicaloutcomeand pages 2-5).

**Suggested HPO Terms:**
- HP:0005381 Recurrent bacterial infections
- HP:0002718 Recurrent invasive bacterial infection
- HP:0002013 Meningitis
- HP:0100806 Sepsis
- HP:0012378 Abnormal complement system physiology
- HP:0033704 Reduced complement activity

**Laboratory Phenotype:**  
Absent or markedly reduced CH50 (classical pathway) and AH50 (alternative pathway) hemolytic activity is diagnostic. For example, a C7-deficient patient showed classical pathway activity 0.6%, lectin 0.2%, and alternative 0.1% of normal (balduit2023geneticbasesof pages 1-2, balduit2023geneticbasesof pages 2-4). Western blot or ELISA typically confirms absence of the specific component protein (balduit2023geneticbasesof pages 1-2).

**Age of Onset:**  
Most infections occur in childhood or adolescence, though adult-onset cases are reported. The median age at first infection was 9 years in the UK cohort (shears2022clinicaloutcomeand pages 2-5).

**Severity and Progression:**  
Severity is variable. Acute episodes can be fulminant, requiring intensive care (22% in the UK cohort) (shears2022clinicaloutcomeand pages 2-5). However, many patients remain asymptomatic until first exposure; 52% in the UK cohort were diagnosed only through family screening (shears2022clinicaloutcomeand pages 2-5).

**Quality of Life Impact:**  
Recurrent life-threatening infections, repeated hospitalizations, and fear of meningitis impose substantial psychosocial burden. Prophylactic regimens (vaccinations, daily antibiotics, emergency planning) require lifelong adherence, affecting daily routines and quality of life (khalil2023thefirstcase pages 1-2, brodszki2020europeansocietyfor pages 10-12).

---

## 4. Genetic/Molecular Information

| Gene symbol | Gene location (chromosome) | OMIM ID for deficiency disorder | Inheritance pattern | Common pathogenic variant types | Founder effects and populations affected | Key references with PMIDs |
|---|---|---|---|---|---|---|
| **C5** | 9q33.2 | **C5 deficiency**; OMIM ID not confirmed from available contexts | Autosomal recessive | Missense, nonsense, frameshift/indel, compound heterozygous variants causing reduced/absent serum C5 and absent CH50/AH50; review reports **18 different mutations in >30 families** | No single classic founder effect established in the provided sources; cases reported in families of diverse origins; UK cohort found many affected individuals from consanguineous Asian families, though some antigenically low C5 cases were actually secondary to **CFH/CFI** defects rather than true C5 deficiency | Szymańska 2024 (review; 18 mutations in >30 families) (szymanska2024molecularaspectsof pages 1-2); Hodeib 2020 lists C5 variants associated with IMD susceptibility (hodeib2020humangeneticsof pages 2-4); Shears 2022 cohort clarifies distinction from CFH/CFI-related secondary terminal pathway deficiency (shears2022clinicaloutcomeand pages 1-2, shears2022clinicaloutcomeand pages 2-5); Lizama-Muñoz 2025 family report with **p.Ile238Thr** and novel **p.Gly650Val** (lizamamunoz2025descriptionandphenotype pages 1-2) |
| **C6** | 5p13 | **C6 deficiency**; **OMIM: 612446** | Autosomal recessive | Nonsense, loss-of-function, compound heterozygous variants; complete deficiency (C6Q0) vs subtotal deficiency (C6SD) | Strong founder effect reported historically in people of African ancestry; teaching source notes frequency about **1:1400 in African Americans**; first Chinese pedigree reported with compound heterozygous nonsense variants **p.Arg596Ter** and **p.Arg606Ter** | Li et al. 2020 (first Chinese pedigree; **OMIM 612446**) (li2020novelpathogenicmutations pages 1-2); Brodszki 2020 gene/chromosome/inheritance summary (brodszki2020europeansocietyfor pages 5-6); Shears 2022 UK cohort includes C6-deficient patients (shears2022clinicaloutcomeand pages 1-2, shears2022clinicaloutcomeand pages 2-5); Sullivan teaching review on founder effect/frequency (sullivan2026complementdeficiencies pages 1-45) |
| **C7** | 5p13 | **C7 deficiency**; OMIM ID not confirmed from available contexts | Autosomal recessive | Missense, nonsense, splice-region, regulatory/UTR variants, deletions; can include **functional hemizygosity** from 3'UTR instability plus coding variant; homozygous and compound heterozygous genotypes reported | Well-described founder effect in **Israeli Moroccan Jews**; teaching source notes frequency about **1:400**; Qatar case reports homozygous **p.Gly379Arg**, also observed in Moroccan-origin Israeli Jews | Balduit et al. 2023 systematic review and novel 3'UTR deletion with functional hemizygosity (balduit2023geneticbasesof pages 1-2, balduit2023geneticbasesof pages 2-4); Khalil et al. 2023 Qatar case with **c.1135G>C (p.Gly379Arg)** and founder note (khalil2023thefirstcase pages 1-2); Shears 2022 cohort includes C7 deficiency (shears2022clinicaloutcomeand pages 1-2, shears2022clinicaloutcomeand pages 2-5); Brodszki 2020 gene/chromosome/inheritance summary (brodszki2020europeansocietyfor pages 5-6); Sullivan founder-effect summary (sullivan2026complementdeficiencies pages 1-45) |
| **C8A / C8B / C8G** | **C8A/C8B:** 1p32; **C8G:** 9q34 | **C8 deficiency**; OMIM ID not confirmed from available contexts | Autosomal recessive | Pathogenic variants most often involve **C8B** (beta-chain deficiency) or **C8A/C8G** complex; missense and loss-of-function variants reported; functional deficiency may reflect absent/defective alpha-gamma or beta subunits | No single founder population established in the provided recent sources; UK cohort included multiple C8-deficient families; case literature also describes **C8B** variation such as **c.1625C>T (p.Thr542Ile)** in compound/heterozygous immune-imbalance context | Brodszki 2020 explicitly notes chromosome positions and AR inheritance for **C8α–γ/C8β** (brodszki2020europeansocietyfor pages 5-6); Shears 2022 UK cohort includes C8 deficiency (shears2022clinicaloutcomeand pages 1-2, shears2022clinicaloutcomeand pages 2-5); Mannes et al. 2023 discusses **C8B p.Thr542Ile** and functional impairment context (from search results summarized in conversation) (brodszki2020europeansocietyfor pages 5-6) |
| **C9** | 5p14–p12 | **C9 deficiency**; OMIM ID not confirmed from available contexts | Autosomal recessive | Loss-of-function variants, including complete and partial deficiency; some cases may retain residual hemolytic activity relative to other terminal component defects | Strong founder effect in **Japanese** and other East Asian populations; teaching source notes frequency about **1:1000 in Japanese**; classic high prevalence in Orientals referenced in C6 paper | Brodszki 2020 gene/chromosome/inheritance summary (brodszki2020europeansocietyfor pages 5-6); Sullivan founder-effect summary (**1:1000 Japanese**) (sullivan2026complementdeficiencies pages 1-45); Li et al. 2020 notes contrast with common C9 deficiency in Oriental populations (li2020novelpathogenicmutations pages 1-2) |


*Table: This table summarizes the principal causal genes underlying late/terminal complement component deficiency (C5-C9), including chromosomal location, inheritance, recurrent variant classes, and notable population founder effects. It is useful for genetics-focused disease curation and for prioritizing molecular testing in suspected terminal pathway deficiency.*

### Causal Genes

- **C5 gene (9q33.2):** Encodes complement C5; 41 exons encoding a pre-protein processed into alpha and beta chains (szymanska2024molecularaspectsof pages 1-2, lizamamunoz2025descriptionandphenotype pages 1-2).
- **C6 gene (5p13):** 18 exons; deficiency classified as complete (C6Q0) or subtotal (C6SD) (li2020novelpathogenicmutations pages 1-2).
- **C7 gene (5p13):** Mutations include missense, nonsense, splice-site, and regulatory variants (balduit2023geneticbasesof pages 1-2, balduit2023geneticbasesof pages 2-4).
- **C8A, C8B, C8G genes:** C8A and C8B on 1p32; C8G on 9q34 (brodszki2020europeansocietyfor pages 5-6).
- **C9 gene (5p14-p12):** Encodes the polymerizing component of MAC (brodszki2020europeansocietyfor pages 5-6).

### Pathogenic Variants

A systematic review of C7 deficiency identified diverse mutation types globally (balduit2023geneticbasesof pages 1-2, balduit2023geneticbasesof pages 2-4). Representative pathogenic variants include:

**C5:**
- p.Ile238Thr and p.Gly650Val (compound heterozygous in a family; p.Gly650Val is novel) (lizamamunoz2025descriptionandphenotype pages 1-2)
- p.Y352C, p.A252T, p.Q19X, p.R1482X, p.K372R (hodeib2020humangeneticsof pages 2-4)

**C6:**
- p.Arg596Ter and p.Arg606Ter (compound heterozygous nonsense mutations in the first Chinese C6Q0 pedigree) (li2020novelpathogenicmutations pages 1-2)

**C7:**
- p.Gly379Arg (homozygous missense; founder mutation in Moroccan-origin Israeli Jews and reported in Qatar) (khalil2023thefirstcase pages 1-2)
- Novel 3'UTR deletion (c.*99_*101delTCT) causing mRNA instability, leading to functional hemizygosity when combined with coding variant (balduit2023geneticbasesof pages 1-2, balduit2023geneticbasesof pages 2-4)

**C8:**
- p.Thr542Ile in C8B (brodszki2020europeansocietyfor pages 5-6)

**Variant Classification:**  
Pathogenic variants are classified using ACMG/AMP guidelines. Loss-of-function variants (nonsense, frameshift) and missense variants disrupting protein structure/function are typically pathogenic or likely pathogenic (li2020novelpathogenicmutations pages 1-2, lizamamunoz2025descriptionandphenotype pages 1-2).

**Allele Frequency:**  
Terminal complement deficiencies are rare in the general population (prevalence ~0.03%) but enriched in founder populations (brodszki2020europeansocietyfor pages 1-2, sullivan2026complementdeficiencies pages 1-45).

**Somatic vs Germline:**  
All reported cases involve germline mutations; somatic complement deficiency is not a recognized entity for terminal components (balduit2023geneticbasesof pages 1-2, li2020novelpathogenicmutations pages 1-2).

**Functional Consequences:**  
Mutations cause loss of function (reduced or absent protein secretion, misfolding, mRNA instability). The result is absent or nonfunctional MAC assembly (balduit2023geneticbasesof pages 1-2, szymanska2024molecularaspectsof pages 1-2, li2020novelpathogenicmutations pages 1-2).

### Modifier Genes

Secondary terminal pathway deficiency can result from excessive C5 consumption due to mutations in complement regulators (Factor H, Factor I). In the UK cohort, 10/16 patients with low antigenic C5 had underlying CFH or CFI mutations rather than primary C5 deficiency (shears2022clinicaloutcomeand pages 1-2, shears2022clinicaloutcomeand pages 2-5).

---

## 5. Environmental Information

**Environmental Factors:**  
Exposure to *Neisseria meningitidis* or *Neisseria gonorrhoeae* is required for clinical disease expression. Environmental triggers include crowded living conditions, smoking, and prior viral respiratory infections that disrupt mucosal barriers (hodeib2020humangeneticsof pages 2-4).

**Lifestyle Factors:**  
No specific lifestyle factors cause terminal complement deficiency, but behaviors affecting *Neisseria* exposure (sexual activity for gonorrhea, close-contact settings for meningococcus) modulate disease expression.

**Infectious Agents:**  
- *Neisseria meningitidis* (serogroups B, C, Y, W, A, E): Gram-negative diplococcus; primary pathogen (khalil2023thefirstcase pages 1-2, shears2022clinicaloutcomeand pages 2-5, hodeib2020humangeneticsof pages 2-4)
- *Neisseria gonorrhoeae*: Causes disseminated gonococcal infection in terminal deficiency (hodeib2020humangeneticsof pages 1-2)

---

## 6. Mechanism / Pathophysiology

### Molecular Pathways

**Terminal Complement Cascade (KEGG, Reactome pathways):**  
The terminal pathway is initiated by C5 convertase enzymes (C4b2a3b from classical/lectin pathways; C3bBb3b from alternative pathway). C5 convertase cleaves C5 into C5a and C5b. C5b binds sequentially to C6, C7, C8, and multiple C9 molecules, forming the MAC (hodeib2020humangeneticsof pages 2-4, szymanska2024molecularaspectsof pages 1-2).

**Suggested Pathway Terms:**
- Reactome: Complement cascade
- KEGG: hsa04610 Complement and coagulation cascades
- GO:0006958 Complement activation, classical pathway
- GO:0006957 Complement activation, alternative pathway
- GO:0006956 Complement activation

### Cellular Processes

**Impaired Bacterial Lysis:**  
MAC creates transmembrane pores in bacterial membranes, causing osmotic lysis. Without functional MAC, *Neisseria* and other Gram-negative bacteria evade complement-mediated killing despite opsonization (hodeib2020humangeneticsof pages 2-4).

**Inflammatory Signaling:**  
C5a (anaphylatoxin) is still generated if C5 is cleaved, contributing to inflammation. However, in complete C5 deficiency, neither C5a nor MAC is formed (szymanska2024molecularaspectsof pages 1-2).

**Suggested GO Terms:**
- GO:0051603 Proteolysis involved in cellular protein catabolic process (MAC-mediated lysis)
- GO:0006952 Defense response
- GO:0045087 Innate immune response

### Protein Dysfunction

Mutations cause:
- **Absent protein secretion** (nonsense, frameshift)
- **Misfolding and degradation** (missense variants disrupting hydrophobic cores or structural domains)
- **mRNA instability** (UTR mutations) (balduit2023geneticbasesof pages 1-2, lizamamunoz2025descriptionandphenotype pages 1-2)

For example, the p.Ile238Thr C5 variant introduces a polar residue into a hydrophobic core, disrupting folding (lizamamunoz2025descriptionandphenotype pages 1-2).

### Biochemical Abnormalities

**Absent MAC Formation:**  
The core defect is failure to form C5b-9 complexes. Hemolytic assays (CH50, AH50) detect this functional deficiency (balduit2023geneticbasesof pages 1-2, balduit2023geneticbasesof pages 2-4).

**Impaired Serum Bactericidal Activity (SBA):**  
Serum from deficient individuals cannot kill *Neisseria* in vitro, despite normal antibody levels (hodeib2020humangeneticsof pages 2-4, szymanska2024molecularaspectsof pages 1-2).

### Immune System Involvement

**Immunodeficiency Phenotype:**  
Patients have intact adaptive immunity (antibody production, T-cell responses) but lack complement-mediated bacterial killing. This is a selective defect in innate immunity (brodszki2020europeansocietyfor pages 1-2, hodeib2020humangeneticsof pages 2-4).

**Suggested Cell Types (Cell Ontology):**
- CL:0000542 Lymphocyte (adaptive immunity intact)
- CL:0000623 Natural killer cell
- CL:0000235 Macrophage (phagocytosis preserved but complement-enhanced killing impaired)

### Causal Chain

1. **Germline mutation** in C5, C6, C7, C8, or C9 gene
2. **Absent or nonfunctional protein** secretion/stability
3. **Failure to assemble MAC** (C5b-9)
4. **Loss of serum bactericidal activity** against *Neisseria*
5. **Invasive meningococcal or gonococcal infection** upon exposure
6. **Clinical manifestations:** sepsis, meningitis, arthritis, chronic meningococcemia

---

## 7. Anatomical Structures Affected

### Organ Level

**Primary Organs:**
- **Central nervous system:** Meningitis (leptomeninges, brain, spinal cord) (khalil2023thefirstcase pages 1-2, shears2022clinicaloutcomeand pages 2-5)
- **Blood/vascular system:** Septicemia, disseminated intravascular coagulation (shears2022clinicaloutcomeand pages 1-2, shears2022clinicaloutcomeand pages 2-5)

**Secondary Organs:**
- **Joints:** Septic arthritis, meningococcal arthritis (shears2022clinicaloutcomeand pages 2-5)
- **Skin:** Petechial rash, purpura fulminans (khalil2023thefirstcase pages 1-2, balduit2023geneticbasesof pages 2-4)
- **Reproductive system:** Disseminated gonococcal infection (hodeib2020humangeneticsof pages 1-2)

**Suggested UBERON Terms:**
- UBERON:0002423 leptomeninges
- UBERON:0000955 brain
- UBERON:0000178 blood
- UBERON:0000982 skeletal joint
- UBERON:0002097 skin of body

### Tissue and Cell Level

**Cell Populations Targeted by Pathogen:**
- Endothelial cells (sites of *Neisseria* invasion) (hodeib2020humangeneticsof pages 2-4)
- Cells of the meninges and blood-brain barrier

**Suggested Cell Ontology Terms:**
- CL:0000115 Endothelial cell
- CL:0000125 Glial cell (in CNS infection)

### Subcellular Level

MAC normally inserts into bacterial outer membranes. In deficiency, this process fails at the plasma membrane/cell surface level.

**Suggested GO Cellular Component Terms:**
- GO:0005886 Plasma membrane
- GO:0016020 Membrane

---

## 8. Temporal Development

### Onset

**Typical Age of Onset:**  
Usually pediatric to young adult. Median age at first infection was 9 years (range 1-25) in the UK cohort (shears2022clinicaloutcomeand pages 2-5). However, asymptomatic individuals can present at any age upon first *Neisseria* exposure.

**Onset Pattern:**  
Acute (invasive infections develop rapidly) (khalil2023thefirstcase pages 1-2, shears2022clinicaloutcomeand pages 1-2).

### Progression

**Disease Course:**  
Episodic and recurrent. Without diagnosis and prevention, patients may experience multiple meningococcal infections over years (e.g., a Qatar case had 3 episodes at ages 7, 18, and 20) (khalil2023thefirstcase pages 1-2).

**Disease Duration:**  
Chronic lifelong susceptibility (brodszki2020europeansocietyfor pages 10-12).

**Progression Rate:**  
Acute invasive infections; intervals between episodes variable, depending on exposure and prevention measures (shears2022clinicaloutcomeand pages 2-5).

### Patterns

**Remission:**  
Infection-free periods occur spontaneously but reflect absence of exposure rather than true remission. Effective prevention (vaccination, prophylaxis) markedly extends infection-free survival (khalil2023thefirstcase pages 1-2, brodszki2020europeansocietyfor pages 10-12).

**Critical Periods:**  
Childhood/adolescence (high meningococcal carriage rates in populations). Post-diagnosis preventive management is a critical window for lifelong risk reduction (brodszki2020europeansocietyfor pages 10-12).

---

## 9. Inheritance and Population

### Epidemiology

**Prevalence:**  
Combined prevalence of complement deficiencies (all types) is approximately 0.03% in the general population. Terminal complement deficiencies are rarer than early pathway deficiencies (brodszki2020europeansocietyfor pages 1-2). Founder populations show higher prevalence (see Founder Effects below).

**Incidence:**  
Specific incidence rates not well-defined in recent literature. Underdiagnosis is likely (brodszki2020europeansocietyfor pages 1-2).

### Inheritance Pattern

**Autosomal Recessive:**  
All terminal complement deficiencies (C5-C9) are autosomal recessive. Heterozygotes are typically asymptomatic carriers (brodszki2020europeansocietyfor pages 1-2, li2020novelpathogenicmutations pages 1-2, brodszki2020europeansocietyfor pages 5-6).

**Penetrance:**  
Incomplete penetrance for infection: not all individuals with deficiency develop invasive disease, depending on *Neisseria* exposure. However, lifetime infection risk is very high (shears2022clinicaloutcomeand pages 1-2, shears2022clinicaloutcomeand pages 2-5).

**Expressivity:**  
Variable; some patients have recurrent infections, others remain asymptomatic (shears2022clinicaloutcomeand pages 2-5).

**Genetic Anticipation:**  
Not observed (brodszki2020europeansocietyfor pages 1-2).

**Germline Mosaicism:**  
Not specifically reported for terminal complement deficiencies.

**Founder Effects:**
- **C7 deficiency:** 1:400 in Israeli Moroccan Jews (sullivan2026complementdeficiencies pages 1-45, khalil2023thefirstcase pages 1-2)
- **C6 deficiency:** 1:1400 in African Americans; high prevalence in Western Cape, South Africa (sullivan2026complementdeficiencies pages 1-45, li2020novelpathogenicmutations pages 1-2)
- **C9 deficiency:** 1:1000 in Japanese (sullivan2026complementdeficiencies pages 1-45, li2020novelpathogenicmutations pages 1-2)

**Consanguinity:**  
Strongly associated. In the UK cohort, 65% of patients had consanguineous parents (shears2022clinicaloutcomeand pages 1-2, shears2022clinicaloutcomeand pages 2-5).

**Carrier Frequency:**  
Not precisely quantified in general populations but elevated in founder populations (sullivan2026complementdeficiencies pages 1-45).

### Population Demographics

**Affected Populations:**  
Enriched in populations with founder mutations (Moroccan Jews, African ancestry, Japanese). The UK cohort was 68% Asian (likely Pakistani/Bangladeshi given UK demographics and consanguinity patterns) and 32% white European (shears2022clinicaloutcomeand pages 1-2, shears2022clinicaloutcomeand pages 2-5).

**Geographic Distribution:**  
Worldwide, but recognized clusters in:
- North Africa (C7 in Moroccans)
- Sub-Saharan Africa (C6)
- East Asia (C9 in Japan)
- UK (Asian consanguineous communities)

**Sex Ratio:**  
In the UK cohort, 55% were male, 45% female, consistent with autosomal recessive inheritance (no sex bias expected) (shears2022clinicaloutcomeand pages 1-2, shears2022clinicaloutcomeand pages 2-5).

**Age Distribution:**  
Diagnosed at median age 14 years (range 1-45) in the UK cohort; 52% were asymptomatic at diagnosis (family-screened) (shears2022clinicaloutcomeand pages 2-5).

---

## 10. Diagnostics

### Clinical Tests

**Hemolytic Complement Assays:**
- **CH50 (classical pathway):** Absent or very low (<1% activity typical in terminal deficiency) (balduit2023geneticbasesof pages 1-2, balduit2023geneticbasesof pages 2-4)
- **AH50 (alternative pathway):** Absent or very low (balduit2023geneticbasesof pages 1-2)
- **Suggested LOINC codes:** CH50, AH50 (specific codes require consultation with LOINC database)

**Specific Component Quantification:**
- ELISA or radial immunodiffusion (Ouchterlony) for C5, C6, C7, C8, C9 protein levels (shears2022clinicaloutcomeand pages 1-2, balduit2023geneticbasesof pages 1-2, li2020novelpathogenicmutations pages 1-2)
- Western blot confirms absence of specific component (balduit2023geneticbasesof pages 1-2, balduit2023geneticbasesof pages 2-4)

**Biomarkers:**
- Absent C5, C6, C7, C8, or C9 antigen
- Absent CH50/AH50 activity
- Normal C3, C4 (distinguishes from early pathway or regulatory defects) (sullivan2026complementdeficiencies pages 1-45, balduit2023geneticbasesof pages 1-2)

### Genetic Testing

**Recommended Approach:**  
Genetic testing is increasingly standard after functional diagnosis. Next-generation sequencing (targeted gene panels, whole exome sequencing) identifies pathogenic variants (balduit2023geneticbasesof pages 1-2, li2020novelpathogenicmutations pages 1-2).

**Single Gene Testing:**  
Sanger sequencing of candidate gene (C5, C6, C7, C8A/B/G, C9) based on which component is absent (balduit2023geneticbasesof pages 1-2, balduit2023geneticbasesof pages 2-4, li2020novelpathogenicmutations pages 1-2).

**Whole Exome/Genome Sequencing:**  
Useful when functional testing suggests terminal deficiency but specific component not determined, or for complex cases (li2020novelpathogenicmutations pages 1-2).

**Important Note:**  
Patients with low antigenic C5 may have secondary deficiency from CFH or CFI mutations (excessive consumption). Genetic testing clarifies primary vs. secondary deficiency (shears2022clinicaloutcomeand pages 1-2, shears2022clinicaloutcomeand pages 2-5).

### Clinical Criteria

**Diagnostic Criteria:**
1. Recurrent invasive *Neisseria* infections (especially atypical serotypes)
2. Absent or very low CH50 and AH50
3. Normal C3, C4 (rules out early pathway defects)
4. Absent specific terminal component by ELISA/Western blot
5. Pathogenic variant(s) in corresponding gene

**Differential Diagnosis:**
- **Properdin or Factor D deficiency:** Also predispose to *Neisseria* but affect alternative pathway specifically; AH50 absent, CH50 may be normal or reduced (sullivan2026complementdeficiencies pages 1-45)
- **Secondary complement consumption:** Low C5 from CFH/CFI defects (atypical HUS phenotype may coexist) (shears2022clinicaloutcomeand pages 1-2, shears2022clinicaloutcomeand pages 2-5)
- **Acquired complement deficiency:** Autoantibodies, liver disease (brodszki2020europeansocietyfor pages 1-2)

### Screening

**Family Screening:**  
Strongly recommended for siblings of index cases. In the UK cohort, 80% had a family history, and 52% were asymptomatic (shears2022clinicaloutcomeand pages 1-2, shears2022clinicaloutcomeand pages 2-5, brodszki2020europeansocietyfor pages 10-12).

**Newborn Screening:**  
Not routinely performed for complement deficiency.

**Cascade Screening:**  
After index case diagnosis, test siblings and consider extended family if consanguinity present (brodszki2020europeansocietyfor pages 10-12).

---

## 11. Outcome/Prognosis

### Survival and Mortality

**Mortality:**  
In the UK cohort of 40 patients, 2 (5%) died. One death was directly attributable to fulminant pneumococcal meningitis in a 4-month-old with Factor I deficiency; the other was from COVID-19 in an adult with C8 deficiency (shears2022clinicaloutcomeand pages 1-2, shears2022clinicaloutcomeand pages 2-5).

**Life Expectancy:**  
With modern preventive management (vaccination, prophylaxis), life expectancy can approach normal. Without recognition, recurrent meningococcal infections carry high mortality (khalil2023thefirstcase pages 1-2, brodszki2020europeansocietyfor pages 10-12).

### Morbidity and Function

**Morbidity:**  
Recurrent ICU admissions (22% in UK cohort), potential for neurologic sequelae from meningitis, joint damage from septic arthritis (shears2022clinicaloutcomeand pages 1-2, shears2022clinicaloutcomeand pages 2-5).

**Quality of Life:**  
Burden from lifelong medication adherence, fear of infection, repeated vaccinations, emergency planning. A well-managed C7-deficient patient remained infection-free over 10 years, illustrating good quality of life achievable with prevention (khalil2023thefirstcase pages 1-2).

### Disease Course

**Complications:**  
- Purpura fulminans, DIC (shears2022clinicaloutcomeand pages 1-2)
- Neurologic sequelae from meningitis (deafness, cognitive impairment)
- Septic arthritis
- Death from fulminant sepsis (shears2022clinicaloutcomeand pages 2-5)

**Recovery Potential:**  
Most patients recover fully from individual infection episodes with prompt treatment, though neurologic damage may be permanent (khalil2023thefirstcase pages 1-2, shears2022clinicaloutcomeand pages 1-2).

### Prognostic Factors

**Poor Prognostic Factors:**
- Delay to diagnosis
- Fulminant septicemia (vs. meningitis alone)
- Lack of vaccination/prophylaxis
- Young age (infants more vulnerable) (shears2022clinicaloutcomeand pages 1-2, shears2022clinicaloutcomeand pages 2-5)

**Good Prognostic Factors:**
- Early diagnosis (especially via family screening before first infection)
- Comprehensive vaccination
- Adherence to prophylaxis
- Emergency planning (khalil2023thefirstcase pages 1-2, brodszki2020europeansocietyfor pages 10-12)

---

## 12. Treatment

| Intervention type | Specific intervention (MAXO term suggestion where applicable) | Evidence level/source | Timing/indication | Key outcomes or efficacy data | Important notes/warnings |
|---|---|---|---|---|---|
| Vaccination | MenACWY conjugate vaccination (MAXO: meningococcal vaccination) | ESID/ERN RITA guideline; expert review; cohort practice data (brodszki2020europeansocietyfor pages 10-12, shears2022clinicaloutcomeand pages 1-2, shears2022clinicaloutcomeand pages 2-5) | Recommended for all patients with terminal/late complement deficiency at diagnosis and continued with boosters | In the UK multicenter cohort, 39/40 patients (98%) received booster meningococcal vaccination after diagnosis; vaccination is considered a core prevention strategy and older expert teaching notes it may halve meningococcal disease risk, though breakthrough infection can still occur (shears2022clinicaloutcomeand pages 2-5, sullivan2026complementdeficiencies pages 1-45) | Must not be relied on as sole protection; terminal complement deficiency confers very high lifelong meningococcal risk despite vaccination. Booster schedules should follow current national guidance, which changes over time (brodszki2020europeansocietyfor pages 10-12, sullivan2026complementdeficiencies pages 1-45) |
| Vaccination | MenB vaccination (MAXO: meningococcal serogroup B vaccination) | ESID/ERN RITA guideline; recent case reports; expert review (brodszki2020europeansocietyfor pages 10-12, khalil2023thefirstcase pages 1-2, mcmurray2024immunodeficiencycomplementdisorders. pages 1-2) | Recommended together with MenACWY for all patients with complement deficiency | Strongly recommended because serogroup B accounted for 43% of typed meningococcal infections in the UK terminal complement cohort (shears2022clinicaloutcomeand pages 2-5); prevention-focused case management with ongoing vaccination was associated with 10-year infection-free follow-up in a C7-deficient patient (khalil2023thefirstcase pages 1-2) | Breakthrough disease remains possible; patient education about urgent assessment of fever is still necessary after full immunization (brodszki2020europeansocietyfor pages 10-12, khalil2023thefirstcase pages 1-2) |
| Vaccination | Pneumococcal vaccination, preferably conjugate with booster strategy as indicated (MAXO: pneumococcal vaccination) | ESID/ERN RITA guideline; cohort practice data (brodszki2020europeansocietyfor pages 10-12, shears2022clinicaloutcomeand pages 2-5) | Recommended in complement deficiency, especially because invasive encapsulated bacterial infection risk is increased | Guideline emphasizes conjugate pneumococcal vaccination; in the UK cohort, 15% received an extra conjugate pneumococcal vaccine after diagnosis (shears2022clinicaloutcomeand pages 2-5, brodszki2020europeansocietyfor pages 10-12) | More strongly emphasized for broader complement defects such as C3 deficiency, but also appropriate in terminal deficiency because non-meningococcal invasive bacterial infections occur (brodszki2020europeansocietyfor pages 10-12, shears2022clinicaloutcomeand pages 2-5) |
| Vaccination | Haemophilus influenzae type b vaccination (MAXO: Haemophilus influenzae vaccination) | ESID/ERN RITA guideline (brodszki2020europeansocietyfor pages 10-12) | Routine prevention in complement-deficient patients | Recommended as part of enhanced immunization against encapsulated bacteria (brodszki2020europeansocietyfor pages 10-12) | Follow routine and catch-up schedules; no live-vaccine contraindication is noted for complement deficiency generally (brodszki2020europeansocietyfor pages 10-12) |
| Antimicrobial prevention | Continuous antibiotic prophylaxis, typically penicillin/amoxicillin; macrolide alternative when appropriate (MAXO: prophylactic antibiotic therapy) | ESID/ERN RITA guideline; UK cohort; case report follow-up (brodszki2020europeansocietyfor pages 10-12, shears2022clinicaloutcomeand pages 1-2, shears2022clinicaloutcomeand pages 2-5, khalil2023thefirstcase pages 1-2) | Consider for patients with recurrent infections, high exposure risk, or individualized high-risk profiles; often used after diagnosis | In the UK cohort, 70% were taking prophylactic antibiotics (shears2022clinicaloutcomeand pages 1-2); a C7-deficient patient receiving ongoing azithromycin plus quadrivalent vaccination had no further meningitis over 10 years (khalil2023thefirstcase pages 1-2) | Adherence is a major limitation: 22% in the UK cohort admitted noncompliance (shears2022clinicaloutcomeand pages 2-5). Balance benefit against antimicrobial resistance and tailor to local epidemiology/guidelines (brodszki2020europeansocietyfor pages 10-12) |
| Antimicrobial prevention | Standby/emergency antibiotics for immediate use with urgent medical review (MAXO: emergency antibiotic therapy) | ESID/ERN RITA guideline (brodszki2020europeansocietyfor pages 10-12) | For patients not on continuous prophylaxis, and also as part of emergency planning for all diagnosed patients | Intended to reduce delay to treatment of encapsulated bacterial infection; guideline recommends access to emergency antibiotics and prompt medical review (brodszki2020europeansocietyfor pages 10-12) | Must be paired with explicit action plans; antibiotics do not replace urgent clinical assessment for suspected meningococcal disease (brodszki2020europeansocietyfor pages 10-12) |
| Education / self-management | Patient and family education, emergency plan, medical alert identification (MAXO: patient education, emergency care planning) | ESID/ERN RITA guideline (brodszki2020europeansocietyfor pages 10-12) | At diagnosis and reinforced annually | Guideline recommends annual follow-up to update education, vaccination, antibiotics, emergency advice, and family studies; MedicAlert-type identification is recommended to speed recognition in emergencies (brodszki2020europeansocietyfor pages 10-12) | Essential because even vaccinated patients remain at risk for rapidly progressive infection; fever, rash, neck stiffness, or sepsis symptoms require urgent action (brodszki2020europeansocietyfor pages 10-12) |
| Family-based prevention | Cascade/family screening, especially siblings (MAXO: genetic counseling, family member screening) | UK multicenter cohort; ESID/ERN RITA guideline (shears2022clinicaloutcomeand pages 1-2, shears2022clinicaloutcomeand pages 2-5, brodszki2020europeansocietyfor pages 10-12) | At diagnosis of an index case and during follow-up | In the UK cohort, 52% were asymptomatic and diagnosed based on family history, and 80% had an affected family member (shears2022clinicaloutcomeand pages 1-2). Screening therefore identifies high-risk but still healthy relatives before invasive infection occurs (shears2022clinicaloutcomeand pages 2-5) | Particularly important in consanguineous families and autosomal recessive disease; asymptomatic status does not imply low future risk (shears2022clinicaloutcomeand pages 1-2, shears2022clinicaloutcomeand pages 2-5) |
| Monitoring / follow-up | Annual specialist immunology follow-up with review of vaccine status, adherence, infection history, and emergency planning (MAXO: clinical monitoring) | ESID/ERN RITA guideline (brodszki2020europeansocietyfor pages 10-12) | Lifelong | Supports updating boosters, prophylaxis decisions, education, and family studies; helps maintain readiness for infection prevention (brodszki2020europeansocietyfor pages 10-12) | Complement assays can be confounded by consumption during sepsis/autoimmunity; interpretation should consider clinical context (sullivan2026complementdeficiencies pages 1-45, brodszki2020europeansocietyfor pages 10-12) |
| Acute supportive management | Standard urgent treatment of invasive meningococcal infection/sepsis, including ICU care when needed (MAXO: intensive care management, antibacterial therapy) | Human cohort and case reports (shears2022clinicaloutcomeand pages 1-2, shears2022clinicaloutcomeand pages 2-5, khalil2023thefirstcase pages 1-2) | During acute infection | In the UK cohort, 22% required ICU for meningococcal septicemia (shears2022clinicaloutcomeand pages 1-2); severe presentations including meningitis, septicemia, and arthritis occur despite prior unrecognized disease (khalil2023thefirstcase pages 1-2, shears2022clinicaloutcomeand pages 2-5) | Disease can be fulminant; prevention does not eliminate need for rapid recognition and aggressive treatment (shears2022clinicaloutcomeand pages 1-2, shears2022clinicaloutcomeand pages 2-5) |
| Blood product replacement | Fresh frozen plasma in selected severe situations (MAXO: plasma transfusion) | Cohort/teaching evidence (shears2022clinicaloutcomeand pages 2-5, sullivan2026complementdeficiencies pages 1-45) | Rarely used in fulminant infection or special circumstances | Two patients in the UK cohort received FFP for fulminant meningococcemia (shears2022clinicaloutcomeand pages 2-5) | Not standard long-term prevention; logistical limits and transfusion risks apply (sullivan2026complementdeficiencies pages 1-45) |
| Counseling on therapeutic complement blockade | C5 inhibitor risk counseling for patients receiving eculizumab/ravulizumab or analogous terminal complement inhibitors (MAXO: medication risk counseling, meningococcal vaccination, prophylactic antibiotic therapy) | 2024 Lancet review; infection review; mechanistic/clinical literature (brodszki2020europeansocietyfor pages 10-12) | Relevant when late complement deficiency is phenocopied by pharmacologic terminal complement inhibition | Terminal complement blockade markedly increases meningococcal susceptibility; patients on C5 inhibitors must receive meningococcal vaccines and have access to prophylactic antibiotics (brodszki2020europeansocietyfor pages 10-12) | Important distinction: these drugs are treatments for complement overactivation disorders, not inherited terminal component deficiency itself. Vaccination and prophylaxis do not prevent all cases, so symptom vigilance remains necessary (brodszki2020europeansocietyfor pages 10-12) |
| Public health / contacts | Vaccination of close contacts/household members (MAXO: contact vaccination) | ESID/ERN RITA guideline (brodszki2020europeansocietyfor pages 10-12) | When a patient with complement deficiency is identified | Guideline recommends contacts also be vaccinated, adding a layer of indirect protection (brodszki2020europeansocietyfor pages 10-12) | Does not substitute for direct patient immunization and prophylaxis (brodszki2020europeansocietyfor pages 10-12) |


*Table: This table summarizes the main prevention and management interventions for late complement component deficiency, with emphasis on vaccination, antibiotic strategies, family screening, and emergency planning. It is useful for translating the literature into actionable clinical knowledge-base entries with ontology-ready intervention labels.*

### Pharmacotherapy

**Prophylactic Antibiotics:**  
Penicillin or amoxicillin is commonly used. Macrolides (azithromycin) are alternatives. In the UK cohort, 70% were on prophylaxis, though 22% admitted noncompliance (shears2022clinicaloutcomeand pages 2-5). A C7-deficient patient on azithromycin plus vaccination remained infection-free for 10 years (khalil2023thefirstcase pages 1-2).

**Suggested MAXO Terms:**
- MAXO:0000756 Prophylactic antibiotic therapy
- MAXO:0001039 Antibacterial therapy

**Acute Treatment:**  
Standard management of meningococcal sepsis (IV ceftriaxone, supportive care, ICU as needed) (khalil2023thefirstcase pages 1-2, shears2022clinicaloutcomeand pages 2-5).

### Advanced Therapeutics

**Fresh Frozen Plasma:**  
Rarely used for acute severe infection (2 patients in UK cohort received FFP for fulminant meningococcemia). Not practical for long-term prevention (shears2022clinicaloutcomeand pages 2-5, sullivan2026complementdeficiencies pages 1-45).

**Gene Therapy / Cell Therapy:**  
Not currently available for terminal complement deficiency. Liver transplantation could theoretically cure (liver produces complement), but not justified for this indication (sullivan2026complementdeficiencies pages 1-45).

### Vaccination

**Meningococcal Vaccines:**  
- **MenACWY conjugate:** Strongly recommended, boosters every 3-5 years (brodszki2020europeansocietyfor pages 10-12)
- **MenB:** Recommended (43% of UK cohort infections were serogroup B) (shears2022clinicaloutcomeand pages 2-5, brodszki2020europeansocietyfor pages 10-12)
- In UK cohort, 98% received booster vaccinations post-diagnosis (shears2022clinicaloutcomeand pages 2-5)

**Pneumococcal Vaccine:**  
Conjugate pneumococcal vaccine recommended (15% received extra dose in UK cohort) (shears2022clinicaloutcomeand pages 2-5, brodszki2020europeansocietyfor pages 10-12).

**Haemophilus influenzae type b:**  
Routine vaccination recommended (brodszki2020europeansocietyfor pages 10-12).

**Efficacy:**  
Vaccination may halve meningococcal disease risk but does not eliminate it. Breakthrough infections occur, so vaccination must be combined with prophylaxis and emergency planning (sullivan2026complementdeficiencies pages 1-45, brodszki2020europeansocietyfor pages 10-12).

**Suggested MAXO Terms:**
- MAXO:0000758 Meningococcal vaccination
- MAXO:0000757 Pneumococcal vaccination
- MAXO:0001309 Haemophilus influenzae vaccination

### Supportive Care

**Emergency Planning:**  
All patients should have:
- MedicAlert or similar identification
- Emergency antibiotic supply
- Written action plan for fever/suspected infection
- Annual review with immunology specialist (brodszki2020europeansocietyfor pages 10-12)

**Suggested MAXO Terms:**
- MAXO:0000011 Patient education
- MAXO:0000004 Emergency care planning

### Treatment Outcomes

**Response Rates:**  
With comprehensive prevention (vaccination + prophylaxis + family screening), the 10-year follow-up of a C7-deficient patient showed no recurrent infections (khalil2023thefirstcase pages 1-2). Mortality is low with modern management (<5% in UK cohort over median follow-up period) (shears2022clinicaloutcomeand pages 2-5).

**Adverse Events:**  
Antibiotic resistance from chronic prophylaxis is a concern. Noncompliance with prophylaxis was 22% in the UK cohort (shears2022clinicaloutcomeand pages 2-5, brodszki2020europeansocietyfor pages 10-12).

---

## 13. Prevention

### Primary Prevention

**Vaccination:**  
MenACWY, MenB, pneumococcal, Hib vaccines reduce infection risk (see Section 12) (brodszki2020europeansocietyfor pages 10-12).

**Antibiotic Prophylaxis:**  
Penicillin or macrolides for high-risk individuals (recurrent infections, endemic areas) (brodszki2020europeansocietyfor pages 10-12).

### Secondary Prevention

**Family Screening:**  
Cascade testing of siblings identifies asymptomatic at-risk individuals before first infection. In UK cohort, 52% were asymptomatic at diagnosis (shears2022clinicaloutcomeand pages 1-2, shears2022clinicaloutcomeand pages 2-5, brodszki2020europeansocietyfor pages 10-12).

### Tertiary Prevention

**Emergency Planning:**  
Rapid recognition and treatment of infections prevents complications (brodszki2020europeansocietyfor pages 10-12).

**Contact Vaccination:**  
Household members and close contacts should also receive meningococcal vaccines (brodszki2020europeansocietyfor pages 10-12).

### Genetic Counseling

Autosomal recessive inheritance counseling for families. Carrier testing for siblings, prenatal/preimplantation diagnosis possible but rarely requested given good outcomes with prevention (brodszki2020europeansocietyfor pages 10-12).

**Suggested MAXO Terms:**
- MAXO:0000503 Genetic counseling
- MAXO:0000009 Family member screening

---

## 14. Other Species / Natural Disease

### Naturally Occurring Disease in Animals

Terminal complement deficiencies have been studied in animal models but are not well-documented as naturally occurring diseases in veterinary medicine. Mice and other mammals have orthologous C5-C9 genes.

**Suggested NCBI Taxon IDs:**
- **Mus musculus (house mouse):** 10090
- **Rattus norvegicus (Norway rat):** 10116

### Comparative Biology

Complement is highly conserved across vertebrates. MAC-mediated bacterial killing is a fundamental defense mechanism in mammals, birds, and fish (brodszki2020europeansocietyfor pages 1-2).

---

## 15. Model Organisms

### Mammalian Models

**Mouse Models:**
- **C5-deficient mice** (spontaneous mutants and knockouts) have impaired bacterial clearance and increased susceptibility to *Neisseria* infection in experimental models (inferred from complement system biology literature).
- **C6-deficient mice** and **C9-deficient mice** have been generated and studied for complement biology.

**Applications:**  
Mouse models enable study of MAC function in bacterial clearance, inflammation, and immune regulation. However, mice do not naturally harbor *Neisseria meningitidis*, limiting translational modeling (general complement biology knowledge).

**Suggested Resources:**
- **MGI (Mouse Genome Informatics):** For C5, C6, C7, C8a, C8b, C8g, C9 knockout/mutant strains
- **IMPC (International Mouse Phenotyping Consortium):** For phenotyping data

### In Vitro Models

**Cell Lines:**  
Human serum bactericidal assays using patient vs. normal serum are standard for assessing functional deficiency (hodeib2020humangeneticsof pages 2-4).

**Organoids / iPSCs:**  
Not specifically reported for terminal complement deficiency modeling.

---

## Conclusions

Late complement component deficiency (C5-C9 deficiency) is a rare, autosomal recessive primary immunodeficiency characterized by absent or nonfunctional membrane attack complex (MAC), leading to markedly increased susceptibility to invasive *Neisseria* infections. The disease presents with recurrent meningococcal meningitis and/or septicemia, often beginning in childhood or adolescence. Diagnosis relies on functional complement assays (absent CH50/AH50) and genetic confirmation of pathogenic variants in C5, C6, C7, C8, or C9 genes. Founder effects exist in Israeli Moroccan Jews (C7), African Americans (C6), and Japanese populations (C9). 

Management requires lifelong preventive strategies including meningococcal (MenACWY, MenB) and pneumococcal vaccination, antibiotic prophylaxis, family screening, and emergency planning. With comprehensive prevention, patients can achieve near-normal life expectancy and quality of life, as demonstrated by a C7-deficient patient remaining infection-free over 10 years with vaccination and azithromycin prophylaxis. Breakthrough infections remain possible, underscoring the need for vigilance and adherence to prevention protocols. This report synthesizes recent (2020-2025) literature, emphasizing genetic bases, clinical phenotypes, diagnostic approaches, and evidence-based management strategies for knowledge base curation (brodszki2020europeansocietyfor pages 1-2, khalil2023thefirstcase pages 1-2, shears2022clinicaloutcomeand pages 1-2, balduit2023geneticbasesof pages 1-2, shears2022clinicaloutcomeand pages 2-5, mcmurray2024immunodeficiencycomplementdisorders. pages 1-2, brodszki2020europeansocietyfor pages 10-12).

---

**Key References:**
- Brodszki et al. 2020: ESID/ERN RITA Complement Guideline (brodszki2020europeansocietyfor pages 1-2, brodszki2020europeansocietyfor pages 10-12)
- Shears et al. 2022: UK multicenter cohort of terminal complement deficiency (shears2022clinicaloutcomeand pages 1-2, shears2022clinicaloutcomeand pages 2-5)
- Balduit et al. 2023: C7 deficiency systematic review and novel mutation (balduit2023geneticbasesof pages 1-2, balduit2023geneticbasesof pages 2-4)
- Khalil et al. 2023: C7 deficiency case with 10-year follow-up (khalil2023thefirstcase pages 1-2)
- Hodeib et al. 2020: Human genetics of meningococcal infections (hodeib2020humangeneticsof pages 2-4)
- Li et al. 2020: First Chinese C6 deficiency pedigree (li2020novelpathogenicmutations pages 1-2)
- Szymańska 2024: C5 deficiency molecular review (szymanska2024molecularaspectsof pages 1-2)
- Lizama-Muñoz et al. 2025: Novel C5 variant family report (lizamamunoz2025descriptionandphenotype pages 1-2)
- McMurray et al. 2024: Complement disorders overview (mcmurray2024immunodeficiencycomplementdisorders. pages 1-2)
- Sullivan 2026: Complement deficiencies teaching resource (sullivan2026complementdeficiencies pages 1-45)

References

1. (brodszki2020europeansocietyfor pages 1-2): Nicholas Brodszki, Ashley Frazer-Abel, Anete S. Grumach, Michael Kirschfink, Jiri Litzman, Elena Perez, Mikko R. J. Seppänen, Kathleen E. Sullivan, and Stephen Jolles. European society for immunodeficiencies (esid) and european reference network on rare primary immunodeficiency, autoinflammatory and autoimmune diseases (ern rita) complement guideline: deficiencies, diagnosis, and management. Journal of Clinical Immunology, 40:576-591, Feb 2020. URL: https://doi.org/10.1007/s10875-020-00754-1, doi:10.1007/s10875-020-00754-1. This article has 117 citations and is from a domain leading peer-reviewed journal.

2. (shears2022clinicaloutcomeand pages 1-2): Annalie Shears, Cathal Steele, Jamie Craig, Stephen Jolles, Sinisa Savic, Rosie Hague, Tanya Coulter, Richard Herriot, and Peter D. Arkwright. Clinical outcome and underlying genetic cause of functional terminal complement pathway deficiencies in a multicenter uk cohort. Journal of Clinical Immunology, 42:665-671, Jan 2022. URL: https://doi.org/10.1007/s10875-022-01213-9, doi:10.1007/s10875-022-01213-9. This article has 5 citations and is from a domain leading peer-reviewed journal.

3. (balduit2023geneticbasesof pages 1-2): Andrea Balduit, Anna Monica Bianco, Alessandro Mangogna, Anna Maria Zicari, Lucia Leonardi, Bianca Laura Cinicola, Martina Capponi, Alberto Tommasini, Chiara Agostinis, Adamo Pio d’Adamo, and Roberta Bulla. Genetic bases of c7 deficiency: systematic review and report of a novel deletion determining functional hemizygosity. Frontiers in Immunology, May 2023. URL: https://doi.org/10.3389/fimmu.2023.1192690, doi:10.3389/fimmu.2023.1192690. This article has 8 citations and is from a peer-reviewed journal.

4. (mcmurray2024immunodeficiencycomplementdisorders. pages 1-2): Jeremy C. McMurray, Brandon J. Schornack, Andrew L. Weskamp, Katherine J. Park, Joshua D. Pollock, W. Grant Day, Aaron T. Brockshus, Douglas E. Beakes, David J. Schwartz, Cecilia P. Mikita, and Luke M. Pittman. Immunodeficiency: complement disorders. Allergy and asthma proceedings, 45 5:305-309, Sep 2024. URL: https://doi.org/10.2500/aap.2024.45.240050, doi:10.2500/aap.2024.45.240050. This article has 23 citations and is from a peer-reviewed journal.

5. (brodszki2020europeansocietyfor pages 10-12): Nicholas Brodszki, Ashley Frazer-Abel, Anete S. Grumach, Michael Kirschfink, Jiri Litzman, Elena Perez, Mikko R. J. Seppänen, Kathleen E. Sullivan, and Stephen Jolles. European society for immunodeficiencies (esid) and european reference network on rare primary immunodeficiency, autoinflammatory and autoimmune diseases (ern rita) complement guideline: deficiencies, diagnosis, and management. Journal of Clinical Immunology, 40:576-591, Feb 2020. URL: https://doi.org/10.1007/s10875-020-00754-1, doi:10.1007/s10875-020-00754-1. This article has 117 citations and is from a domain leading peer-reviewed journal.

6. (hodeib2020humangeneticsof pages 2-4): Stephanie Hodeib, Jethro A. Herberg, Michael Levin, and Vanessa Sancho-Shimizu. Human genetics of meningococcal infections. Human Genetics, 139:961-980, Feb 2020. URL: https://doi.org/10.1007/s00439-020-02128-4, doi:10.1007/s00439-020-02128-4. This article has 40 citations and is from a peer-reviewed journal.

7. (li2020novelpathogenicmutations pages 1-2): Philip H Li, William WY Wong, Evelyn NY Leung, Chak‐sing Lau, and Elaine Au. Novel pathogenic mutations identified in the first chinese pedigree of complete c6 deficiency. Clinical & Translational Immunology, Jul 2020. URL: https://doi.org/10.1002/cti2.1148, doi:10.1002/cti2.1148. This article has 8 citations and is from a peer-reviewed journal.

8. (shears2022clinicaloutcomeand pages 2-5): Annalie Shears, Cathal Steele, Jamie Craig, Stephen Jolles, Sinisa Savic, Rosie Hague, Tanya Coulter, Richard Herriot, and Peter D. Arkwright. Clinical outcome and underlying genetic cause of functional terminal complement pathway deficiencies in a multicenter uk cohort. Journal of Clinical Immunology, 42:665-671, Jan 2022. URL: https://doi.org/10.1007/s10875-022-01213-9, doi:10.1007/s10875-022-01213-9. This article has 5 citations and is from a domain leading peer-reviewed journal.

9. (balduit2023geneticbasesof pages 2-4): Andrea Balduit, Anna Monica Bianco, Alessandro Mangogna, Anna Maria Zicari, Lucia Leonardi, Bianca Laura Cinicola, Martina Capponi, Alberto Tommasini, Chiara Agostinis, Adamo Pio d’Adamo, and Roberta Bulla. Genetic bases of c7 deficiency: systematic review and report of a novel deletion determining functional hemizygosity. Frontiers in Immunology, May 2023. URL: https://doi.org/10.3389/fimmu.2023.1192690, doi:10.3389/fimmu.2023.1192690. This article has 8 citations and is from a peer-reviewed journal.

10. (szymanska2024molecularaspectsof pages 1-2): Hanna Szymańska. Molecular aspects of hereditary complement component c5 deficiency in humans. Polish Annals of Medicine, pages 1-6, Jul 2024. URL: https://doi.org/10.29089/paom/188059, doi:10.29089/paom/188059. This article has 2 citations.

11. (brodszki2020europeansocietyfor pages 5-6): Nicholas Brodszki, Ashley Frazer-Abel, Anete S. Grumach, Michael Kirschfink, Jiri Litzman, Elena Perez, Mikko R. J. Seppänen, Kathleen E. Sullivan, and Stephen Jolles. European society for immunodeficiencies (esid) and european reference network on rare primary immunodeficiency, autoinflammatory and autoimmune diseases (ern rita) complement guideline: deficiencies, diagnosis, and management. Journal of Clinical Immunology, 40:576-591, Feb 2020. URL: https://doi.org/10.1007/s10875-020-00754-1, doi:10.1007/s10875-020-00754-1. This article has 117 citations and is from a domain leading peer-reviewed journal.

12. (sullivan2026complementdeficiencies pages 1-45): Kathleen E. Sullivan. Complement Deficiencies, pages 693-713. Springer Nature Switzerland, Jan 2026. URL: https://doi.org/10.1007/978-3-032-01547-1\_9, doi:10.1007/978-3-032-01547-1\_9. This article has 5 citations.

13. (khalil2023thefirstcase pages 1-2): Sally Mahgoub Khalil, Sami Aqel, Dalal Sideeg Mudawi, Hassan Mobayed, and Maryam Ali Al-Nesf. The first case report of complement component 7 deficiency in qatar and a 10-year follow-up. Frontiers in Immunology, Oct 2023. URL: https://doi.org/10.3389/fimmu.2023.1253301, doi:10.3389/fimmu.2023.1253301. This article has 2 citations and is from a peer-reviewed journal.

14. (hodeib2020humangeneticsof pages 1-2): Stephanie Hodeib, Jethro A. Herberg, Michael Levin, and Vanessa Sancho-Shimizu. Human genetics of meningococcal infections. Human Genetics, 139:961-980, Feb 2020. URL: https://doi.org/10.1007/s00439-020-02128-4, doi:10.1007/s00439-020-02128-4. This article has 40 citations and is from a peer-reviewed journal.

15. (lizamamunoz2025descriptionandphenotype pages 1-2): Asier Lizama-Muñoz, Juan Francisco Gutiérrez-Bautista, Monica Bernal, and Miguel Ángel López-Nevot. Description and phenotype of a novel c5 gene mutation and a novel combination: family report and literature review. Frontiers in Immunology, Jul 2025. URL: https://doi.org/10.3389/fimmu.2025.1605903, doi:10.3389/fimmu.2025.1605903. This article has 0 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Late_Complement_Component_Deficiency-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](Late_Complement_Component_Deficiency-deep-research-falcon_artifacts/artifact-01.md)
- [Edison artifact artifact-02](Late_Complement_Component_Deficiency-deep-research-falcon_artifacts/artifact-02.md)