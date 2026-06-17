---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-15T21:31:55.134235'
end_time: '2026-06-15T21:45:15.315778'
duration_seconds: 800.18
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Gestational Trophoblastic Neoplasm
  mondo_id: ''
  category: ''
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 41
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Gestational_Trophoblastic_Neoplasm-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Gestational Trophoblastic Neoplasm
- **MONDO ID:**  (if available)
- **Category:** 

## Research Objectives

Please provide a comprehensive research report on **Gestational Trophoblastic Neoplasm** covering all of the
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
- **Disease Name:** Gestational Trophoblastic Neoplasm
- **MONDO ID:**  (if available)
- **Category:** 

## Research Objectives

Please provide a comprehensive research report on **Gestational Trophoblastic Neoplasm** covering all of the
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


# Gestational Trophoblastic Neoplasm (GTN) — Comprehensive Research Report (2023–2024 prioritized)

## Target Disease
- **Disease name:** Gestational Trophoblastic Neoplasm (GTN) (a malignant subset within gestational trophoblastic disease, GTD) (senat2024gestationaltrophoblasticdisease pages 1-4, jinkai2024prognosticatinggestationaltrophoblastic pages 1-2)
- **Category:** Pregnancy-associated trophoblastic malignancies / gynecologic oncology (jinkai2024prognosticatinggestationaltrophoblastic pages 1-2)
- **MONDO / Orphanet:** Not identified in the retrieved sources (limitation of this tool run).

## Executive summary (current understanding)
Gestational trophoblastic neoplasia (GTN) is a spectrum of rare pregnancy-associated malignancies derived from gestational trophoblastic cells and classically includes **invasive mole, choriocarcinoma, placental site trophoblastic tumor (PSTT), and epithelioid trophoblastic tumor (ETT)** (jinkai2024prognosticatinggestationaltrophoblastic pages 1-2, senat2024gestationaltrophoblasticdisease pages 1-4). GTN is typically diagnosed clinically after a pregnancy event—most commonly after a molar pregnancy—using standardized **serial human chorionic gonadotropin (hCG)** criteria and subsequently staged and risk-stratified using **FIGO anatomical staging** and **WHO/FIGO prognostic scoring** (senat2024gestationaltrophoblasticdisease pages 4-7, senat2024gestationaltrophoblasticdisease pages 7-11, jinkai2024prognosticatinggestationaltrophoblastic pages 1-2). Modern treatment achieves very high cure rates overall (>90% in aggregated reports), and immune checkpoint inhibitors have become a major recent development for chemotherapy-resistant disease, including PSTT/ETT subtypes that are relatively chemotherapy resistant (senat2024gestationaltrophoblasticdisease pages 7-11, baas2024immunotherapyforgestational pages 1-2, baas2024immunotherapyforgestational pages 4-5).

## 1. Disease information
### 1.1 What is GTN?
GTN is a malignant subset of GTD that arises from abnormal proliferation/transformation of trophoblast after conception, and can follow **any pregnancy** (molar pregnancy, miscarriage, ectopic pregnancy, or term pregnancy) (senat2024gestationaltrophoblasticdisease pages 4-7, li2023gestationaltrophoblasticneoplasia pages 4-6). In a contemporary GTD review, WHO classification is described as dividing GTD into “tumor-like lesions, molar pregnancies and gestational trophoblastic neoplasms (GTN)” (senat2024gestationaltrophoblasticdisease pages 1-4).

### 1.2 Key concepts/definitions
- **Post-molar GTN (clinical diagnosis):** persistent elevation or rising hCG after molar evacuation (senat2024gestationaltrophoblasticdisease pages 4-7, senat2024gestationaltrophoblasticdisease pages 1-4).
- **Core biomarker concept:** trophoblastic lesions produce **hCG**, enabling sensitive monitoring for diagnosis and treatment response (jinkai2024prognosticatinggestationaltrophoblastic pages 1-2, senat2024gestationaltrophoblasticdisease pages 7-11).

### 1.3 Key identifiers (codes found in retrieved sources)
The retrieved literature contained multiple ICD-10 and ICD-O morphology codes used in epidemiology/registry studies:
- **ICD-10 codes (examples used in studies of GTD/GTN):** O01.0, O01.1, O01.9, D39.1, C58 (roszkowskiUnknownyearincidênciaemortalidade pages 1-10); O01.0, O01.1 (munyakarama2024gestationaltrophoblasticdisease pages 32-36); D39.2 also appeared in one clinical cohort (srijaipracharoen2020reproductiveoutcomesafter pages 1-2).
- **ICD-O morphology codes mapping to GTN entities:** M9100/1 (invasive mole), 9100/3 (choriocarcinoma), 9104/1 (PSTT), 9105/3 (ETT) (srijaipracharoen2020reproductiveoutcomesafter pages 1-2).

**MeSH / ICD-11 / MONDO / Orphanet identifiers:** not present in the retrieved excerpts (limitation).

### 1.4 Synonyms/alternative names
- “Gestational trophoblastic neoplasia” (GTN), “malignant gestational trophoblastic disease,” “persistent trophoblastic disease” (as a post-molar entity), and entity-level diagnoses: invasive mole, gestational choriocarcinoma, PSTT, ETT (senat2024gestationaltrophoblasticdisease pages 4-7, jinkai2024prognosticatinggestationaltrophoblastic pages 1-2, tempfer2023gestationalandnongestational pages 6-7).

### 1.5 Evidence source type
Most GTN characterization here is derived from **aggregated disease-level resources** (guidelines/reviews) (tempfer2023gestationalandnongestational pages 4-5, jinkai2024prognosticatinggestationaltrophoblastic pages 1-2) and supplemented by **trial-level** evidence for immunotherapy (patel2024aphaseii pages 1-3, braga2023immunotherapyinthe pages 4-5) and **registry/observational cohorts** for epidemiology and risk factors (tempfer2023gestationalandnongestational pages 4-5, munyakarama2024gestationaltrophoblasticdisease pages 22-26).

## 2. Etiology
### 2.1 Disease causal factors (mechanistic overview)
GTN arises from malignant transformation of placental trophoblast, typically after molar pregnancy but also after other gestations (senat2024gestationaltrophoblasticdisease pages 4-7, li2023gestationaltrophoblasticneoplasia pages 4-6). The neoplastic trophoblast’s endocrine function (hCG production) is central to detection and monitoring (jinkai2024prognosticatinggestationaltrophoblastic pages 1-2).

### 2.2 Risk factors (with data where available)
**Maternal age extremes**
- Increased incidence has been reported in patients “under 20 years of age and … over 40 years of age,” and a review notes about **20% of GTNs occur in teenage pregnancies** (senat2024gestationaltrophoblasticdisease pages 4-7).
- A registry-based analysis summarized in one 2024 paper reported increased odds of hydatidiform mole for women <20 (~2×) and >35 (~1.5×) relative to 20–29 years (p=0.02) and higher malignant progression in women >40 (20% vs 13% for <40) (munyakarama2024gestationaltrophoblasticdisease pages 22-26).

**Prior molar pregnancy / complete mole**
- Prior complete hydatidiform mole is emphasized as a strong risk factor for subsequent GTN (senat2024gestationaltrophoblasticdisease pages 4-7).
- Progression rates reported in a 2024 review table: **~7–30% following complete mole vs ~2.5–7.5% following partial mole** (senat2024gestationaltrophoblasticdisease pages 4-7).

**Geography/ethnicity**
- Incidence varies regionally: **0.57–1.1 per 1,000 pregnancies** in Europe/New Zealand/Australia/North America vs **~2 per 1,000** in Japan/Southeast Asia (senat2024gestationaltrophoblasticdisease pages 4-7).
- A 2023 guideline notes over-representation of Black US-American women in registries and about **double incidence in Asian vs Caucasian women** (tempfer2023gestationalandnongestational pages 4-5).

**Lifestyle/nutrition and reproductive history**
- Smoking and dietary carotene deficiency are listed as risk factors in a 2024 GTD review (senat2024gestationaltrophoblasticdisease pages 4-7).
- A 2024 registry-based review excerpt cites associations with cigarette smoking (~2× risk), vitamin A deficiency (1.6×, p=0.05), recurrent abortions (OR 2.8), and infertility history (OR 3.7) (munyakarama2024gestationaltrophoblasticdisease pages 22-26).

### 2.3 Protective factors
Parity may be protective in some analyses (parity ≥1 OR 0.6) (munyakarama2024gestationaltrophoblasticdisease pages 22-26). Robust protective factors were not a focus of the 2023 guideline excerpts or the 2024 GTD pathology review (tempfer2023gestationalandnongestational pages 4-5, senat2024gestationaltrophoblasticdisease pages 4-7).

### 2.4 Gene–environment interactions
Not explicitly characterized in the retrieved excerpts.

## 3. Phenotypes (clinical presentation) + HPO suggestions
### 3.1 Common clinical phenotypes
A 2024 review describes the classic molar-pregnancy/GTD phenotype and common findings:
- **Vaginal bleeding** (most common), sometimes passage of swollen villi (senat2024gestationaltrophoblasticdisease pages 4-7).
- **Uterine enlargement for gestational age**, **theca lutein cysts**, **severe nausea/vomiting (hyperemesis)**, **early pregnancy hypertension**, and **disproportionately high hCG** for gestational age (senat2024gestationaltrophoblasticdisease pages 4-7).
- Theca lutein cyst frequency was reported as **~9–25%** in a review table (senat2024gestationaltrophoblasticdisease pages 4-7).

GTN may be asymptomatic and detected via post-evacuation hCG surveillance, or present with irregular vaginal bleeding and metastatic symptoms depending on site (senat2024gestationaltrophoblasticdisease pages 4-7, li2023gestationaltrophoblasticneoplasia pages 4-6).

### 3.2 Metastatic patterns and severe presentations
- Invasive mole can metastasize “most commonly to the lungs and vagina” (senat2024gestationaltrophoblasticdisease pages 4-7).
- Rare mother–infant metastatic presentations (systematic review of 22 cases) show extreme metastatic burden; in infants: liver 77.35%, lung 72.7%, brain/GI 18.2% (mangla2023gestationaltrophoblasticneoplasia pages 2-4).

### 3.3 Laboratory abnormalities
- **Serum β-hCG elevation** is the key laboratory marker and is used for diagnosis and response monitoring (senat2024gestationaltrophoblasticdisease pages 7-11, jinkai2024prognosticatinggestationaltrophoblastic pages 1-2).

### 3.4 HPO term suggestions (not exhaustive)
- Vaginal bleeding: **HP:0000132**
- Hyperemesis gravidarum / severe vomiting: **HP:0100665** (or vomiting **HP:0002013**)
- Uterine enlargement: **HP:0000134**
- Ovarian cysts (theca lutein cysts): **HP:0000139**
- Elevated circulating chorionic gonadotropin: (closest HPO variants include abnormal laboratory test terms; may require mapping via LOINC rather than HPO)
- Pulmonary metastases / lung nodules: **HP:0031351** (pulmonary nodule) / metastatic neoplasm (broad)

Quality-of-life impacts were not quantified in the retrieved excerpts.

## 4. Genetic / molecular information
### 4.1 Germline predisposition (molar pregnancy context)
A 2024 excerpt lists genetic predisposition genes associated with hydatidiform mole/recurrent mole syndromes, including **NLRP7** and **KHDC3L**, and mentions additional genes (MEI1, TOP6BL, REC114) (munyakarama2024gestationaltrophoblasticdisease pages 22-26). These are primarily relevant to recurrent molar pregnancy risk, which in turn increases GTN risk (munyakarama2024gestationaltrophoblasticdisease pages 22-26).

### 4.2 Somatic/molecular alterations in trophoblastic tumors (ETT/precursor lesions)
A 2023 Modern Pathology molecular study distinguished placental site nodule (PSN), atypical PSN (APSN), and ETT using IHC, NanoString transcriptomics, and RNA-seq fusion testing:
- Ki-67 proliferation index increased from PSN (~4.8%) to APSN (~11.7%) to ETT (~20%), with ETT significantly higher (p<0.001) (jeremie2023molecularanalysesof pages 4-5).
- Prior work cited in this study notes **LPCAT1–TERT fusion transcripts** and **TERT amplification** as characteristic of ETT and absent from PSN/PSTT; in this cohort, no APSN harbored LPCAT1–TERT (jeremie2023molecularanalysesof pages 1-3, jeremie2023molecularanalysesof pages 5-6).
- Gene-set enrichments in ETT vs APSN included **DNA damage repair, immortality/stemness, and cell-cycle signaling** (jeremie2023molecularanalysesof pages 1-3, jeremie2023molecularanalysesof pages 4-5).

### 4.3 Immune biomarkers
Expression of PD-1/PD-L1 axis is central to immunotherapy rationale. A 2024 immunotherapy review notes the rationale includes “strong PD-L1 expression by malignant trophoblast” (baas2024immunotherapyforgestational pages 2-3).

## 5. Mechanism / pathophysiology (causal chain) + GO/CL suggestions
### 5.1 Causal chain (high-level)
1) Abnormal conception (often molar pregnancy) → 2) persistent trophoblast proliferation and/or malignant transformation → 3) elevated/plateauing/rising hCG after pregnancy evacuation → 4) local invasion and/or hematogenous metastasis (e.g., lung, vagina; sometimes brain/liver in severe cases) → 5) clinical manifestations (bleeding, metastatic symptoms) (senat2024gestationaltrophoblasticdisease pages 4-7, senat2024gestationaltrophoblasticdisease pages 7-11).

### 5.2 Suggested GO biological process terms (examples)
- **GO:0008283** cell population proliferation
- **GO:0048870** cell motility
- **GO:0001525** angiogenesis
- **GO:0048514** blood vessel morphogenesis
- **GO:0006955** immune response (for immune microenvironment and checkpoint biology)

### 5.3 Suggested CL (Cell Ontology) terms (examples)
- Trophoblast cell: **CL:0000351** (trophoblast cell; broad)
- Syncytiotrophoblast / cytotrophoblast (if needed for subtype mapping)

### 5.4 Suggested UBERON anatomical terms
- Uterus: **UBERON:0000995**
- Placenta: **UBERON:0001987**
- Lung: **UBERON:0002048** (metastatic site)
- Vagina: **UBERON:0000996** (metastatic site)

## 6. Inheritance and population
GTN itself is not classically inherited; however, recurrent molar pregnancy (a major upstream risk state) can have maternal-effect genetic causes (e.g., NLRP7, KHDC3L) (munyakarama2024gestationaltrophoblasticdisease pages 22-26). Population differences include significant geographic variability in incidence and differences by ethnicity as described above (senat2024gestationaltrophoblasticdisease pages 4-7, tempfer2023gestationalandnongestational pages 4-5).

## 7. Diagnostics
### 7.1 Diagnostic criteria (post-molar hCG criteria)
A contemporary review lists FIGO (2000) hCG criteria for diagnosing GTN after molar evacuation:
- **Plateau:** hCG stable (±10%) in **4 determinations over 3 weeks** (senat2024gestationaltrophoblasticdisease pages 4-7).
- **Rise:** hCG increase **>10% in 3 determinations over 2 weeks** (senat2024gestationaltrophoblasticdisease pages 4-7, senat2024gestationaltrophoblasticdisease pages 7-11).
- **Persistence:** detectable hCG **>6 months** after evacuation (senat2024gestationaltrophoblasticdisease pages 4-7, tempfer2023gestationalandnongestational pages 6-7).

### 7.2 Staging and risk stratification
GTN staging integrates FIGO anatomical stage (I–IV) and WHO/FIGO prognostic score (low risk ≤6; high risk ≥7; ultra-high-risk ≥13 in later updates) (senat2024gestationaltrophoblasticdisease pages 7-11, jinkai2024prognosticatinggestationaltrophoblastic pages 1-2). The FIGO/WHO scoring system is noted to be **not applicable to PSTT and ETT** (jinkai2024prognosticatinggestationaltrophoblastic pages 1-2).

A compact reference table is provided below.

| Item | Details | Source (PMID/DOI/URL if available) | Year |
|---|---|---|---|
| GTN histologic subtypes | Gestational trophoblastic neoplasia (GTN) comprises **invasive mole, choriocarcinoma, placental site trophoblastic tumour (PSTT), and epithelioid trophoblastic tumour (ETT)**. (jinkai2024prognosticatinggestationaltrophoblastic pages 1-2, senat2024gestationaltrophoblasticdisease pages 1-4) | Lin J-K, Jiang F, Xiang Y. *eClinicalMedicine* 77:102890. DOI: 10.1016/j.eclinm.2024.102890; https://doi.org/10.1016/j.eclinm.2024.102890. Senat H et al. DOI: 10.12775/jehs.2024.59.005; https://doi.org/10.12775/jehs.2024.59.005 | 2024 |
| Post-molar diagnostic hCG criterion: plateau | Post-molar GTN can be diagnosed when **hCG remains within ±10% across 4 determinations over 3 weeks** after evacuation. (senat2024gestationaltrophoblasticdisease pages 4-7) | Senat H et al. DOI: 10.12775/jehs.2024.59.005; https://doi.org/10.12775/jehs.2024.59.005 | 2024 |
| Post-molar diagnostic hCG criterion: rise | Post-molar GTN can be diagnosed when **hCG rises by >10% in 3 determinations over 2 weeks**. (senat2024gestationaltrophoblasticdisease pages 4-7, senat2024gestationaltrophoblasticdisease pages 7-11) | Senat H et al. DOI: 10.12775/jehs.2024.59.005; https://doi.org/10.12775/jehs.2024.59.005 | 2024 |
| Post-molar diagnostic hCG criterion: persistent detectability | Post-molar GTN can be diagnosed when **hCG remains detectable for >6 months after molar evacuation**. (senat2024gestationaltrophoblasticdisease pages 4-7, tempfer2023gestationalandnongestational pages 6-7) | Senat H et al. DOI: 10.12775/jehs.2024.59.005; https://doi.org/10.12775/jehs.2024.59.005. Tempfer C et al. DOI: 10.1055/a-1904-6461; https://doi.org/10.1055/a-1904-6461 | 2024, 2023 |
| Additional GTN diagnostic basis | GTN diagnosis may also be established by **presence of metastases** or **histologic diagnosis** (e.g., invasive mole, choriocarcinoma, PSTT, ETT). (senat2024gestationaltrophoblasticdisease pages 7-11, senat2024gestationaltrophoblasticdisease pages 4-7) | Senat H et al. DOI: 10.12775/jehs.2024.59.005; https://doi.org/10.12775/jehs.2024.59.005 | 2024 |
| FIGO anatomical stage I | **Stage I:** disease confined to the uterus. (senat2024gestationaltrophoblasticdisease pages 7-11) | Senat H et al. DOI: 10.12775/jehs.2024.59.005; https://doi.org/10.12775/jehs.2024.59.005 | 2024 |
| FIGO anatomical stage II | **Stage II:** GTN extends outside the uterus but is limited to genital structures. (senat2024gestationaltrophoblasticdisease pages 7-11) | Senat H et al. DOI: 10.12775/jehs.2024.59.005; https://doi.org/10.12775/jehs.2024.59.005 | 2024 |
| FIGO anatomical stage III | **Stage III:** GTN extends to the lungs, with or without genital tract involvement. (senat2024gestationaltrophoblasticdisease pages 7-11) | Senat H et al. DOI: 10.12775/jehs.2024.59.005; https://doi.org/10.12775/jehs.2024.59.005 | 2024 |
| FIGO anatomical stage IV | **Stage IV:** all other distant metastases. (senat2024gestationaltrophoblasticdisease pages 7-11) | Senat H et al. DOI: 10.12775/jehs.2024.59.005; https://doi.org/10.12775/jehs.2024.59.005 | 2024 |
| WHO/FIGO prognostic score: low risk | **Score 0–6 = low-risk GTN**; typically treated with single-agent chemotherapy. (jinkai2024prognosticatinggestationaltrophoblastic pages 1-2, senat2024gestationaltrophoblasticdisease pages 7-11) | Lin J-K, Jiang F, Xiang Y. DOI: 10.1016/j.eclinm.2024.102890; https://doi.org/10.1016/j.eclinm.2024.102890. Senat H et al. DOI: 10.12775/jehs.2024.59.005; https://doi.org/10.12775/jehs.2024.59.005 | 2024 |
| WHO/FIGO prognostic score: high risk | **Score ≥7 = high-risk GTN**; typically requires multi-agent chemotherapy. (jinkai2024prognosticatinggestationaltrophoblastic pages 1-2, senat2024gestationaltrophoblasticdisease pages 7-11) | Lin J-K, Jiang F, Xiang Y. DOI: 10.1016/j.eclinm.2024.102890; https://doi.org/10.1016/j.eclinm.2024.102890. Senat H et al. DOI: 10.12775/jehs.2024.59.005; https://doi.org/10.12775/jehs.2024.59.005 | 2024 |
| WHO/FIGO prognostic score: ultra-high risk | **Ultra-high-risk** category recognized in later FIGO updates as **score ≥13** or extensive metastasis. (jinkai2024prognosticatinggestationaltrophoblastic pages 1-2) | Lin J-K, Jiang F, Xiang Y. *eClinicalMedicine* 77:102890. DOI: 10.1016/j.eclinm.2024.102890; https://doi.org/10.1016/j.eclinm.2024.102890 | 2024 |
| WHO/FIGO score applicability caveat | The standard FIGO/WHO prognostic scoring system is **not applicable to PSTT and ETT**. (jinkai2024prognosticatinggestationaltrophoblastic pages 1-2) | Lin J-K, Jiang F, Xiang Y. *eClinicalMedicine* 77:102890. DOI: 10.1016/j.eclinm.2024.102890; https://doi.org/10.1016/j.eclinm.2024.102890 | 2024 |
| Core prognostic score variables | FIGO/WHO scoring incorporates factors such as **antecedent pregnancy, interval since index pregnancy, pretreatment hCG, tumour size, site/number of metastases, and prior failed chemotherapy**. (jinkai2024prognosticatinggestationaltrophoblastic pages 1-2, tempfer2023gestationalandnongestational pages 4-5) | Lin J-K, Jiang F, Xiang Y. DOI: 10.1016/j.eclinm.2024.102890; https://doi.org/10.1016/j.eclinm.2024.102890. Tempfer C et al. DOI: 10.1055/a-1904-6461; https://doi.org/10.1055/a-1904-6461 | 2024, 2023 |


*Table: This table summarizes the core clinical classification framework for gestational trophoblastic neoplasia, including diagnostic hCG criteria, FIGO staging, and WHO/FIGO prognostic score cutoffs. It is useful as a compact reference for disease definition, diagnosis, and risk stratification.*

### 7.3 Imaging
- For re-staging or suspected resistance/metastasis, a 2023 guideline excerpt recommends **transvaginal ultrasound**, **CT thorax/abdomen**, and **brain MRI**, with FDG-PET/CT considered when imaging is suspicious for metastasis (tempfer2023gestationalandnongestational pages 6-7).

### 7.4 Pathology and molecular diagnostics
- STR genotyping is described as the “gold standard” for correct diagnosis in GTD/GTN contexts (senat2024gestationaltrophoblasticdisease pages 1-4, senat2024gestationaltrophoblasticdisease pages 4-7).
- For chorionic-type intermediate trophoblastic lesions, RNAseq signatures and fusion testing (e.g., LPCAT1–TERT in ETT) can aid triage and classification (jeremie2023molecularanalysesof pages 1-3, jeremie2023molecularanalysesof pages 5-6).

### 7.5 Abstract-quote support (diagnosis/definition)
- Diagnostic concept quote: “Post-molar gestational trophoblast neoplasia (GTN) is a clinical diagnosis based on the observation of a persistent increase or persistently high hCG concentration after evacuation of the mole…” (senat2024gestationaltrophoblasticdisease pages 1-4).

## 8. Treatment (current practice + recent developments)
### 8.1 Standard of care (chemotherapy and surgery)
**Low-risk GTN (FIGO score <7):**
- The 2023 DGGG/OEGGG/SGGG guideline recommends methotrexate (MTX) regimen (e.g., 50 mg IM on days 1,3,5,7 with folic acid on alternating days) as first-line for invasive mole/low-risk GTN, with consolidation cycles after hCG becomes undetectable (tempfer2023gestationalandnongestational pages 7-8, tempfer2023gestationalandnongestational pages 6-7).
- MTX resistance is operationalized as plateaued or rising hCG across serial tests (e.g., “four or more consecutive hCG tests showing plateauing” or rising) with escalation to actinomycin-D or multi-agent therapy (tempfer2023gestationalandnongestational pages 6-7, eichbaum142023clemenstempfer1larschristian pages 6-7).

**High-risk GTN (FIGO score ≥7):**
- First-line recommended regimen is **EMA-CO**; if hCG plateaus/increases, switch to salvage multi-agent regimens (e.g., EMA-EP, BEP, TP-TE, carboplatin/paclitaxel) (tempfer2023gestationalandnongestational pages 7-8, tempfer2023gestationalandnongestational pages 6-7).
- For very high risk (WHO score >12), induction with etoposide + cisplatin for 1–3 cycles is recommended to reduce early hemorrhage-related mortality (tempfer2023gestationalandnongestational pages 7-8, tempfer2023gestationalandnongestational pages 9-10).

**PSTT/ETT:**
- Surgery (simple hysterectomy) is emphasized as preferred/therapy of choice; chemotherapy is suggested if metastases are present (tempfer2023gestationalandnongestational pages 18-19, tempfer2023gestationalandnongestational pages 9-10).

### 8.2 Immunotherapy (major 2023–2024 development; real-world implementation)
**Checkpoint inhibitors are increasingly used for chemoresistant/refractory GTN**.

**Aggregated 2024 review (133 patients):**
A 2024 review identified **133 patients** treated with checkpoint inhibitors (pembrolizumab 23; avelumab 22; camrelizumab 57; toripalimab 15; other anti–PD-1 16). **Complete remission occurred in 85 patients** overall, including **77/118** in high-risk/relapsed/multidrug-resistant and **8/15** in low-risk cases (baas2024immunotherapyforgestational pages 1-2). (Expert analysis: this aggregation suggests meaningful cure potential in otherwise refractory disease, but it is dominated by non-randomized evidence.)

**Avelumab (TROPHIMMUN cohort A; NCT03135769):**
- Phase II trial in single-agent chemotherapy-resistant disease reported **8/15 (53.3%)** hCG normalization; no relapses; mostly grade 1–2 toxicities (braga2023immunotherapyinthe pages 4-5).
- Abstract quote: “Eight patients (53.3%) had hCG normalization… none subsequently relapsed.” (braga2023immunotherapyinthe pages 4-5).

**Dual checkpoint blockade (DART SWOG S1609 cohort; NCT02834013):**
- Prospective phase II basket cohort in refractory GTN (ipilimumab + nivolumab) observed **ORR 75% (3/4)** with **CR 25%**; 6-month PFS 75%; two grade 3 immune-related AEs (arthralgia, colitis) (patel2024aphaseii pages 1-3).
- Abstract quote: “3 of 4 patients responded [ORR = 75%…]” (patel2024aphaseii pages 1-3).

**Camrelizumab + apatinib (phase II; n=20 referenced in review):**
- Objective response 11/20 (55%) with 10 CR; grade 3 toxicities common (e.g., hypertension) (baas2024immunotherapyforgestational pages 4-5).

### 8.3 MAXO suggestions (examples)
- Chemotherapy: **MAXO:0000058** (chemotherapy)
- Methotrexate therapy: **MAXO:0000648** (antimetabolite chemotherapy; if available)
- Actinomycin D therapy: MAXO chemotherapy subtype
- Hysterectomy: **MAXO:0001112** (hysterectomy)
- Immune checkpoint inhibitor therapy: **MAXO:0000942** (immunotherapy; checkpoint blockade)

## 9. Prevention
Primary prevention is limited because causation is tightly linked to conception biology; however, **secondary prevention via surveillance** is central.

**Post-molar surveillance:**
- Weekly hCG monitoring after partial mole until negative on at least two consecutive tests is recommended; persistent disease suggested by rising hCG or hCG persisting >6 months (tempfer2023gestationalandnongestational pages 6-7).
- After completion of chemotherapy and hCG negativization, monthly hCG monitoring for **1 year** is recommended (tempfer2023gestationalandnongestational pages 7-8, tempfer2023gestationalandnongestational pages 18-19).

## 10. Outcome / prognosis
- A recent review states cure rates “exceed 90%” overall (senat2024gestationaltrophoblasticdisease pages 7-11).
- A systematic review on mother–infant metastatic GTN notes historical survival rates “85%–95%” (while also noting lower survival in that extreme subset) (mangla2023gestationaltrophoblasticneoplasia pages 9-10).

## 11. Applications and real-world implementations
### 11.1 Centralized rare-tumor care and guideline-driven management
A 2023 European guideline (DGGG/OEGGG/SGGG) provides structured diagnostic and treatment pathways including standardized hCG monitoring, risk scoring, and escalation algorithms, reflecting real-world implementation in specialty care networks (tempfer2023gestationalandnongestational pages 7-8, tempfer2023gestationalandnongestational pages 6-7).

### 11.2 Immunotherapy in practice
By 2024, checkpoint inhibitor use has expanded from case reports to prospective trials and pooled clinical experience across multiple agents, supporting increasing adoption for chemoresistant GTN and chemotherapy-resistant PSTT/ETT contexts (baas2024immunotherapyforgestational pages 1-2, baas2024immunotherapyforgestational pages 4-5).

## 12. Other species / natural disease
No evidence on naturally occurring GTN in non-human species was identified in the retrieved sources (limitation).

## 13. Model organisms
No specific animal models or engineered model organism systems for GTN were described in the retrieved sources (limitation). The molecular profiling work described was performed on human FFPE specimens with transcriptomic/fusion analyses (jeremie2023molecularanalysesof pages 1-3).

## 14. Expert opinions and analysis (authoritative sources)
- The 2024 immunotherapy review concludes checkpoint inhibitors represent “a new paradigm” and highlights priorities for future research including earlier-line use, chemo combinations, and fertility impact (baas2024immunotherapyforgestational pages 1-2).
- The 2023 German/Austrian/Swiss guideline emphasizes guideline-driven staging and treatment escalation and explicitly includes immunotherapy and molecular diagnostics chapters (tempfer2023gestationalandnongestational pages 4-5, tempfer2023gestationalandnongestational pages 9-10).

## Key recent references (URLs + publication dates)
- Tempfer C et al. **Mar 2023**. *Geburtshilfe und Frauenheilkunde* (DGGG/OEGGG/SGGG guideline). https://doi.org/10.1055/a-1904-6461 (tempfer2023gestationalandnongestational pages 4-5)
- Senat H et al. **Feb 2024**. GTD diagnostic/pathology review. https://doi.org/10.12775/jehs.2024.59.005 (senat2024gestationaltrophoblasticdisease pages 1-4)
- Baas IO et al. **Sep 2024**. Immunotherapy review (133 patients aggregated). https://doi.org/10.1159/000533972 (baas2024immunotherapyforgestational pages 1-2)
- Patel SP et al. **Oct 2024**. DART SWOG S1609 GTN cohort (ipi+nivo). https://doi.org/10.1158/1078-0432.CCR-23-2293 (patel2024aphaseii pages 1-3)

## Notes on limitations of this run
- MONDO/Orphanet and MeSH identifiers were not present in the retrieved excerpts, so they could not be cited directly.
- Model organism and comparative pathology information was not identified in the retrieved corpus.


References

1. (senat2024gestationaltrophoblasticdisease pages 1-4): Hanna Senat, Patrycja Grabowska, Aleksandra Senat, Patrycja Bolla, Aleksandra Madej, and Zuzanna Marczyńska. Gestational trophoblastic disease a contemporary review of diagnostic and pathology. current challenge and future directions for gynecologists and obstetricians. Journal of Education, Health and Sport, 59:73-86, Feb 2024. URL: https://doi.org/10.12775/jehs.2024.59.005, doi:10.12775/jehs.2024.59.005. This article has 1 citations.

2. (jinkai2024prognosticatinggestationaltrophoblastic pages 1-2): Lin Jin-Kai, Jiang Fang, and Xiang Yang. Prognosticating gestational trophoblastic neoplasia: from figo 2000 to future models. eClinicalMedicine, 77:102890, Nov 2024. URL: https://doi.org/10.1016/j.eclinm.2024.102890, doi:10.1016/j.eclinm.2024.102890. This article has 11 citations and is from a peer-reviewed journal.

3. (senat2024gestationaltrophoblasticdisease pages 4-7): Hanna Senat, Patrycja Grabowska, Aleksandra Senat, Patrycja Bolla, Aleksandra Madej, and Zuzanna Marczyńska. Gestational trophoblastic disease a contemporary review of diagnostic and pathology. current challenge and future directions for gynecologists and obstetricians. Journal of Education, Health and Sport, 59:73-86, Feb 2024. URL: https://doi.org/10.12775/jehs.2024.59.005, doi:10.12775/jehs.2024.59.005. This article has 1 citations.

4. (senat2024gestationaltrophoblasticdisease pages 7-11): Hanna Senat, Patrycja Grabowska, Aleksandra Senat, Patrycja Bolla, Aleksandra Madej, and Zuzanna Marczyńska. Gestational trophoblastic disease a contemporary review of diagnostic and pathology. current challenge and future directions for gynecologists and obstetricians. Journal of Education, Health and Sport, 59:73-86, Feb 2024. URL: https://doi.org/10.12775/jehs.2024.59.005, doi:10.12775/jehs.2024.59.005. This article has 1 citations.

5. (baas2024immunotherapyforgestational pages 1-2): Inge O. Baas, Anneke M. Westermann, Benoit You, Pierre-Adrien Bolze, Michael Seckl, and Ehsan Ghorani. Immunotherapy for gestational trophoblastic neoplasia: a new paradigm. Gynecologic and Obstetric Investigation, 89:230-238, Sep 2024. URL: https://doi.org/10.1159/000533972, doi:10.1159/000533972. This article has 49 citations and is from a peer-reviewed journal.

6. (baas2024immunotherapyforgestational pages 4-5): Inge O. Baas, Anneke M. Westermann, Benoit You, Pierre-Adrien Bolze, Michael Seckl, and Ehsan Ghorani. Immunotherapy for gestational trophoblastic neoplasia: a new paradigm. Gynecologic and Obstetric Investigation, 89:230-238, Sep 2024. URL: https://doi.org/10.1159/000533972, doi:10.1159/000533972. This article has 49 citations and is from a peer-reviewed journal.

7. (li2023gestationaltrophoblasticneoplasia pages 4-6): HongYe Li, Meng Sun, Jing Jiang, Bin Shi, BaoHua Wang, Lei Wang, WenXin Wu, and WenYan Wang. Gestational trophoblastic neoplasia with primary lung cancer and mesenchymal tumor of sigmoid colon: a case report and literature review. BMC Women's Health, Feb 2023. URL: https://doi.org/10.1186/s12905-023-02204-7, doi:10.1186/s12905-023-02204-7. This article has 0 citations.

8. (roszkowskiUnknownyearincidênciaemortalidade pages 1-10): I Roszkowski. Incidência e mortalidade por doença trofoblástica gestacional. Unknown journal, Unknown year.

9. (munyakarama2024gestationaltrophoblasticdisease pages 32-36): B Munyakarama. Gestational trophoblastic disease and risk of nontrophoblastic cancer later in life. Unknown journal, 2024.

10. (srijaipracharoen2020reproductiveoutcomesafter pages 1-2): Sunamchok Srijaipracharoen and Siriwan Tangjitgamol. Reproductive outcomes after treatment of patients with gestational trophoblastic neoplasia. Clinical Obstetrics, Gynecology and Reproductive Medicine, Jan 2020. URL: https://doi.org/10.15761/cogrm.1000289, doi:10.15761/cogrm.1000289. This article has 2 citations and is from a peer-reviewed journal.

11. (tempfer2023gestationalandnongestational pages 6-7): Clemens Tempfer, Lars-Christian Horn, Sven Ackermann, Ralf Dittrich, Jens Einenkel, Andreas Günthert, Heidemarie Haase, Jürgen Kratzsch, Michael Kreißl, Stephan Polterauer, Andreas Ebert, Eric Steiner, Falk Thiel, Michael Eichbaum, Tanja Fehm, Martin C. Koch, and Paul Gass. Gestational and non-gestational trophoblastic neoplasia. guideline of the dggg, oeggg and sggg (s2k-level, awmf registry no. 032/049, april 2022). Geburtshilfe und Frauenheilkunde, 83:267-288, Mar 2023. URL: https://doi.org/10.1055/a-1904-6461, doi:10.1055/a-1904-6461. This article has 2 citations and is from a peer-reviewed journal.

12. (tempfer2023gestationalandnongestational pages 4-5): Clemens Tempfer, Lars-Christian Horn, Sven Ackermann, Ralf Dittrich, Jens Einenkel, Andreas Günthert, Heidemarie Haase, Jürgen Kratzsch, Michael Kreißl, Stephan Polterauer, Andreas Ebert, Eric Steiner, Falk Thiel, Michael Eichbaum, Tanja Fehm, Martin C. Koch, and Paul Gass. Gestational and non-gestational trophoblastic neoplasia. guideline of the dggg, oeggg and sggg (s2k-level, awmf registry no. 032/049, april 2022). Geburtshilfe und Frauenheilkunde, 83:267-288, Mar 2023. URL: https://doi.org/10.1055/a-1904-6461, doi:10.1055/a-1904-6461. This article has 2 citations and is from a peer-reviewed journal.

13. (patel2024aphaseii pages 1-3): Sandip P. Patel, Megan Othus, Young Kwang Chae, Michael J. Dennis, Sarah Gordon, David Mutch, Wolfram Samlowski, William R. “Rusty” Robinson, Elad Sharon, Christopher Ryan, Gabby Lopez, Melissa Plets, Charles Blanke, and Razelle Kurzrock. A phase ii basket trial of dual anti–ctla-4 and anti–pd-1 blockade in rare tumors (dart swog 1609 cohort 47) in patients with gestational trophoblastic neoplasia. Clinical Cancer Research, 30:33-38, Oct 2024. URL: https://doi.org/10.1158/1078-0432.ccr-23-2293, doi:10.1158/1078-0432.ccr-23-2293. This article has 24 citations and is from a highest quality peer-reviewed journal.

14. (braga2023immunotherapyinthe pages 4-5): Antonio Braga, Elaine Balthar, Laís Cristhine Santos Souza, Michelle Samora, Matheus Rech, José Mauro Madi, Joffre Amim Junior, Jorge Rezende Filho, Kevin M. Elias, Neil S. Horowitz, Sue Yazaki Sun, and Ross S. Berkowitz. Immunotherapy in the treatment of chemoresistant gestational trophoblastic neoplasia - systematic review with a presentation of the first 4 brazilian cases. Clinics, 78:100260, Jan 2023. URL: https://doi.org/10.1016/j.clinsp.2023.100260, doi:10.1016/j.clinsp.2023.100260. This article has 19 citations and is from a peer-reviewed journal.

15. (munyakarama2024gestationaltrophoblasticdisease pages 22-26): B Munyakarama. Gestational trophoblastic disease and risk of nontrophoblastic cancer later in life. Unknown journal, 2024.

16. (mangla2023gestationaltrophoblasticneoplasia pages 2-4): Mishu Mangla, Emine A. Rahiman, Harpreet Kaur, and Poojitha Kanikaram. Gestational trophoblastic neoplasia with concurrent metastasis to the mother and child: a systematic literature review. Journal of the Turkish German Gynecological Association, 24:206-219, Sep 2023. URL: https://doi.org/10.4274/jtgga.galenos.2023.2023-5-2, doi:10.4274/jtgga.galenos.2023.2023-5-2. This article has 12 citations.

17. (jeremie2023molecularanalysesof pages 4-5): Gaspard Jeremie, Fabienne Allias, Alexis Trecourt, Lucie Gaillot-Durand, Pierre-Adrian Bolze, Françoise DESCOTES, Garance TONDEUR, Jimmy Perrot, Touria Hajri, Benoit YOU, François GOLFIER, Jonathan Lopez, and Mojgan Devouassoux-Shisheboran. Molecular analyses of chorionic-type intermediate trophoblastic lesions: atypical placental site nodules are closer to placental site nodules than epithelioid trophoblastic tumors. Modern pathology : an official journal of the United States and Canadian Academy of Pathology, Inc, 36 1:100046, Jan 2023. URL: https://doi.org/10.1016/j.modpat.2022.100046, doi:10.1016/j.modpat.2022.100046. This article has 24 citations.

18. (jeremie2023molecularanalysesof pages 1-3): Gaspard Jeremie, Fabienne Allias, Alexis Trecourt, Lucie Gaillot-Durand, Pierre-Adrian Bolze, Françoise DESCOTES, Garance TONDEUR, Jimmy Perrot, Touria Hajri, Benoit YOU, François GOLFIER, Jonathan Lopez, and Mojgan Devouassoux-Shisheboran. Molecular analyses of chorionic-type intermediate trophoblastic lesions: atypical placental site nodules are closer to placental site nodules than epithelioid trophoblastic tumors. Modern pathology : an official journal of the United States and Canadian Academy of Pathology, Inc, 36 1:100046, Jan 2023. URL: https://doi.org/10.1016/j.modpat.2022.100046, doi:10.1016/j.modpat.2022.100046. This article has 24 citations.

19. (jeremie2023molecularanalysesof pages 5-6): Gaspard Jeremie, Fabienne Allias, Alexis Trecourt, Lucie Gaillot-Durand, Pierre-Adrian Bolze, Françoise DESCOTES, Garance TONDEUR, Jimmy Perrot, Touria Hajri, Benoit YOU, François GOLFIER, Jonathan Lopez, and Mojgan Devouassoux-Shisheboran. Molecular analyses of chorionic-type intermediate trophoblastic lesions: atypical placental site nodules are closer to placental site nodules than epithelioid trophoblastic tumors. Modern pathology : an official journal of the United States and Canadian Academy of Pathology, Inc, 36 1:100046, Jan 2023. URL: https://doi.org/10.1016/j.modpat.2022.100046, doi:10.1016/j.modpat.2022.100046. This article has 24 citations.

20. (baas2024immunotherapyforgestational pages 2-3): Inge O. Baas, Anneke M. Westermann, Benoit You, Pierre-Adrien Bolze, Michael Seckl, and Ehsan Ghorani. Immunotherapy for gestational trophoblastic neoplasia: a new paradigm. Gynecologic and Obstetric Investigation, 89:230-238, Sep 2024. URL: https://doi.org/10.1159/000533972, doi:10.1159/000533972. This article has 49 citations and is from a peer-reviewed journal.

21. (tempfer2023gestationalandnongestational pages 7-8): Clemens Tempfer, Lars-Christian Horn, Sven Ackermann, Ralf Dittrich, Jens Einenkel, Andreas Günthert, Heidemarie Haase, Jürgen Kratzsch, Michael Kreißl, Stephan Polterauer, Andreas Ebert, Eric Steiner, Falk Thiel, Michael Eichbaum, Tanja Fehm, Martin C. Koch, and Paul Gass. Gestational and non-gestational trophoblastic neoplasia. guideline of the dggg, oeggg and sggg (s2k-level, awmf registry no. 032/049, april 2022). Geburtshilfe und Frauenheilkunde, 83:267-288, Mar 2023. URL: https://doi.org/10.1055/a-1904-6461, doi:10.1055/a-1904-6461. This article has 2 citations and is from a peer-reviewed journal.

22. (eichbaum142023clemenstempfer1larschristian pages 6-7): M Eichbaum14, T Fehm15, and MC Koch16. Clemens tempfer1, lars-christian horn2, sven ackermann3, ralf dittrich4, jens einenkel5, andreas günthert6, heidemarie haase7, jürgen kratzsch8 …. Unknown journal, 2023.

23. (tempfer2023gestationalandnongestational pages 9-10): Clemens Tempfer, Lars-Christian Horn, Sven Ackermann, Ralf Dittrich, Jens Einenkel, Andreas Günthert, Heidemarie Haase, Jürgen Kratzsch, Michael Kreißl, Stephan Polterauer, Andreas Ebert, Eric Steiner, Falk Thiel, Michael Eichbaum, Tanja Fehm, Martin C. Koch, and Paul Gass. Gestational and non-gestational trophoblastic neoplasia. guideline of the dggg, oeggg and sggg (s2k-level, awmf registry no. 032/049, april 2022). Geburtshilfe und Frauenheilkunde, 83:267-288, Mar 2023. URL: https://doi.org/10.1055/a-1904-6461, doi:10.1055/a-1904-6461. This article has 2 citations and is from a peer-reviewed journal.

24. (tempfer2023gestationalandnongestational pages 18-19): Clemens Tempfer, Lars-Christian Horn, Sven Ackermann, Ralf Dittrich, Jens Einenkel, Andreas Günthert, Heidemarie Haase, Jürgen Kratzsch, Michael Kreißl, Stephan Polterauer, Andreas Ebert, Eric Steiner, Falk Thiel, Michael Eichbaum, Tanja Fehm, Martin C. Koch, and Paul Gass. Gestational and non-gestational trophoblastic neoplasia. guideline of the dggg, oeggg and sggg (s2k-level, awmf registry no. 032/049, april 2022). Geburtshilfe und Frauenheilkunde, 83:267-288, Mar 2023. URL: https://doi.org/10.1055/a-1904-6461, doi:10.1055/a-1904-6461. This article has 2 citations and is from a peer-reviewed journal.

25. (mangla2023gestationaltrophoblasticneoplasia pages 9-10): Mishu Mangla, Emine A. Rahiman, Harpreet Kaur, and Poojitha Kanikaram. Gestational trophoblastic neoplasia with concurrent metastasis to the mother and child: a systematic literature review. Journal of the Turkish German Gynecological Association, 24:206-219, Sep 2023. URL: https://doi.org/10.4274/jtgga.galenos.2023.2023-5-2, doi:10.4274/jtgga.galenos.2023.2023-5-2. This article has 12 citations.

## Artifacts

- [Edison artifact artifact-00](Gestational_Trophoblastic_Neoplasm-deep-research-falcon_artifacts/artifact-00.md)