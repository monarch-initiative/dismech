---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-07-23T22:40:01.113596'
end_time: '2026-07-23T22:48:24.687539'
duration_seconds: 503.57
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: NF1 Microdeletion Syndrome
  mondo_id: ''
  category: ''
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 28
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: NF1_Microdeletion_Syndrome-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** NF1 Microdeletion Syndrome
- **MONDO ID:**  (if available)
- **Category:** 

## Research Objectives

Please provide a comprehensive research report on **NF1 Microdeletion Syndrome** covering all of the
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
- **Disease Name:** NF1 Microdeletion Syndrome
- **MONDO ID:**  (if available)
- **Category:** 

## Research Objectives

Please provide a comprehensive research report on **NF1 Microdeletion Syndrome** covering all of the
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


# NF1 Microdeletion Syndrome: Comprehensive Disease-Characteristics Report

## Executive summary

NF1 microdeletion syndrome is a severe, contiguous-gene subtype of neurofibromatosis type 1 (NF1) caused by a constitutional heterozygous deletion at 17q11.2 encompassing **NF1** and neighboring genes. The canonical recurrent type-1 deletion is approximately 1.4 Mb, removes 14 protein-coding genes and four microRNA genes, and constitutes roughly 70–80% of NF1 microdeletions. Large deletions collectively account for approximately 5–11% of molecularly diagnosed NF1, although ascertainment and testing methods affect estimates. Compared with intragenic NF1 pathogenic variants, non-mosaic deletions are associated with earlier and heavier neurofibroma burden, dysmorphism, childhood overgrowth, developmental and learning problems, cardiovascular abnormalities, and higher malignant peripheral nerve sheath tumor (MPNST) risk. (pacot2024correlationbetweenlarge pages 1-2, tritto2024geneticepigeneticeffectsin pages 1-2, kehrersawatzki2017emerginggenotype–phenotyperelationships pages 1-3)

Two important recent developments are: (1) a 2024 human molecular study showing that the deletion changes local three-dimensional chromatin interactions and expression of genes outside the deleted interval; and (2) explicit recognition in 2024 pediatric surveillance recommendations that an NF1 microdeletion involving **SUZ12** is a high-risk cancer-predisposition genotype. (tritto2024geneticepigeneticeffectsin pages 1-2, perrino2024updateonpediatric pages 6-8)

| Domain | Key finding | Quantitative detail | Evidence type/source |
|---|---|---:|---|
| Disease identifiers | NF1 microdeletion syndrome corresponds to chromosome 17q11.2 deletion syndrome, 1.4 Mb; Orphanet term is 17q11 microdeletion syndrome | MONDO:0013357; Orphanet:97685 | Aggregated disease resources plus literature linkage (OpenTargets Search: NF1 microdeletion syndrome, pacot2024correlationbetweenlarge pages 1-2) |
| Definition | Constitutional heterozygous deletion of NF1 and flanking genes causes a generally more severe NF1 subtype | Large deletions account for ~5–11% of NF1 cases | Review/human cohort (tritto2024geneticepigeneticeffectsin pages 1-2, kehrersawatzki2017emerginggenotype–phenotyperelationships pages 1-3) |
| Deletion type 1 | Recurrent type-1 deletion mediated by low-copy repeats; classic severe form | ~1.4 Mb; ~70–80% of NF1 microdeletions | Human cohort/review (pacot2024correlationbetweenlarge pages 1-2, tritto2024geneticepigeneticeffectsin pages 1-2, kehrersawatzki2017emerginggenotype–phenotyperelationships pages 1-3) |
| Deletion type 2 | Recurrent type-2 deletion, often mosaic, mediated by SUZ12/SUZ12P1 recombination | ~1.2 Mb; ~10% of NF1 microdeletions | Human cohort/review (pacot2024correlationbetweenlarge pages 1-2, tritto2024geneticepigeneticeffectsin pages 1-2, kehrersawatzki2017emerginggenotype–phenotyperelationships pages 1-3) |
| Deletion type 3 | Rare recurrent type-3 deletion | ~1.0 Mb; ~1–4% of NF1 microdeletions | Human cohort/review (pacot2024correlationbetweenlarge pages 1-2, tritto2024geneticepigeneticeffectsin pages 1-2, kehrersawatzki2017emerginggenotype–phenotyperelationships pages 1-3) |
| Principal genes | Core deleted interval includes NF1 with clinically relevant co-deleted genes/modifiers | Key genes highlighted: NF1, SUZ12, RNF135, CRLF3, ADAP2 | Human cohort/review/organoid/OpenTargets (OpenTargets Search: NF1 microdeletion syndrome, tritto2024geneticepigeneticeffectsin pages 1-2, kehrersawatzki2017emerginggenotype–phenotyperelationships pages 1-3, wegscheid2021patientderivedipsccerebralorganoid pages 8-9) |
| Epidemiology | NF1 microdeletion syndrome is rare in the population but enriched within NF1 cohorts | Approx. 1 in 60,000 individuals; ~5% of NF1 in one estimate | Review (kehrersawatzki2017emerginggenotype–phenotyperelationships pages 17-18) |
| Severe phenotype | Compared with intragenic NF1 variants, patients more often show dysmorphism, overgrowth, developmental and cognitive problems, and high tumor burden | Reported more often in type-1 than atypical deletions; age-dependent expression noted | Human cohort/review (buki2021genotypephenotypeassociationsin pages 1-2, kehrersawatzki2017emerginggenotype–phenotyperelationships pages 1-3, buki2021genotypephenotypeassociationsin pages 14-15) |
| Malignancy risk | Increased malignant peripheral nerve sheath tumor risk, especially with SUZ12 co-deletion | Lifetime MPNST risk ~16–26% vs ~8–13% in general NF1 | Review/human cohort (pacot2024correlationbetweenlarge pages 1-2, kehrersawatzki2017emerginggenotype–phenotyperelationships pages 1-3) |
| Diagnostics | Copy-number testing is central because sequencing alone can miss the syndrome | MLPA used for efficient detection/classification; chromosomal microarray/aCGH used for confirmation and breakpoint definition | Human cohort/review (buki2021genotypephenotypeassociationsin pages 1-2, buki2021genotypephenotypeassociationsin pages 5-6) |
| Core mechanism | NF1 haploinsufficiency reduces neurofibromin dosage, dysregulating RAS-MAPK signaling; co-deletion of SUZ12 implicates PRC2 biology in tumor risk | NF1 loss is the primary driver; SUZ12 loss linked to higher MPNST susceptibility | Review/human cohort (tritto2024geneticepigeneticeffectsin pages 1-2, kehrersawatzki2017emerginggenotype–phenotyperelationships pages 1-3) |
| Neurodevelopment mechanism | CRLF3 loss contributes to abnormal neurogenesis independent of NF1-driven NSC proliferation effects | Organoid study showed rescue of neuronal maturation defects with RhoA activation | Patient-derived iPSC cerebral organoid study (wegscheid2021patientderivedipsccerebralorganoid pages 8-9, wegscheid2021patientderivedipsccerebralorganoid pages 1-4) |
| 2024 mechanistic update | Beyond haploinsufficiency, a 2024 study showed chromatin reorganization and position effects on flanking genes | 4C-seq identified altered DNA-DNA interactions, including RHOT1 promoter interaction with SLC6A4 and increased SLC6A4 expression | Human molecular study, 2024 (tritto2024geneticepigeneticeffectsin pages 1-2) |
| Surveillance | High-risk NF1 management principles apply; NF1 microdeletion involving SUZ12 is specifically recognized as higher risk | Baseline whole-body MRI recommended after puberty/late adolescence; closer follow-up for high internal tumor burden or DNL | 2024 surveillance guidance (perrino2024updateonpediatric pages 6-8) |
| Treatment | No syndrome-specific curative therapy; care is standard NF1 complication-directed management with tumor surveillance and treatment as indicated | MEK inhibitors are used for NF1 complications such as symptomatic inoperable plexiform neurofibromas, not specifically for the microdeletion itself | Guideline/review/clinical-trial context (perrino2024updateonpediatric pages 6-8, pacot2024correlationbetweenlarge pages 1-2) |


*Table: This table condenses the key knowledge-base facts for NF1 microdeletion syndrome, including identifiers, recurrent deletion classes, major co-deleted genes, core clinical risks, mechanisms, diagnostics, surveillance, and treatment framing. It is aligned to the gathered evidence and highlights where 2024 studies added mechanistic and surveillance updates.*

## 1. Disease information

### Definition and category

**Disease name:** NF1 microdeletion syndrome.  
**Category:** rare autosomal-dominant genomic disorder; chromosome 17q11.2 contiguous-gene deletion syndrome; RASopathy; neurocutaneous and tumor-predisposition syndrome.

The preferred definition is a constitutional or mosaic heterozygous deletion encompassing **NF1**, rather than merely an intragenic NF1 deletion. “NF1 deletion syndrome,” “NF1 microdeletion syndrome,” “17q11.2 microdeletion syndrome,” “17q11 microdeletion syndrome,” “NF1 total-gene deletion,” and “chromosome 17q11.2 deletion syndrome, 1.4 Mb” are common alternative terms. The literature sometimes uses *total gene deletion* (TGD), especially in experimental studies. (pacot2024correlationbetweenlarge pages 1-2, wegscheid2021patientderivedipsccerebralorganoid pages 1-4)

### Identifiers

- **MONDO:** MONDO:0013357, *chromosome 17q11.2 deletion syndrome, 1.4 Mb*.
- **Orphanet:** ORPHA:97685, *17q11 microdeletion syndrome*.
- **OMIM:** the broader allelic disorder is NF1, OMIM **162200**; a separate universally applied OMIM phenotype number for the microdeletion subtype was not established in the retrieved evidence.
- **MeSH:** generally indexed under *Neurofibromatosis 1* and *Chromosome Deletion* rather than a dedicated microdeletion heading.
- **ICD-10/ICD-11:** typically coded under NF1/neurofibromatosis; no microdeletion-specific billable code was identified. The copy-number diagnosis should therefore be retained separately in the molecular record.

OpenTargets associates MONDO:0013357 principally with **NF1** and **RNF135**, while ORPHA:97685 is represented as 17q11 microdeletion syndrome. (OpenTargets Search: NF1 microdeletion syndrome)

### Evidence granularity

Most information is aggregated from disease resources, small retrospective cohorts, molecular case series, and reviews—not population-scale EHR data. Key recent primary data include cohorts of 17 and 22 affected individuals and a 2024 qPCR/4C-seq/NGS study. Consequently, precise phenotype frequencies remain less secure than the direction of genotype–phenotype associations. (pacot2024correlationbetweenlarge pages 1-2, tritto2024geneticepigeneticeffectsin pages 1-2, buki2021genotypephenotypeassociationsin pages 1-2)

## 2. Etiology

### Causal genetic factor

The cause is heterozygous loss of **NF1** plus a variable set of flanking genes at chromosome 17q11.2. Recurrent deletion classes are:

- **Type 1:** approximately 1.4 Mb; about 70–80% of deletions; usually germline and non-mosaic; caused by non-allelic homologous recombination (NAHR) between low-copy repeats NF1-REPa and NF1-REPc, classically during maternal meiosis. It removes 14 protein-coding genes and four microRNA genes.
- **Type 2:** approximately 1.2 Mb; roughly 10–20%; mediated by recombination involving **SUZ12** and its pseudogene **SUZ12P1**; frequently postzygotic and therefore mosaic; approximately 13 coding genes are hemizygous.
- **Type 3:** approximately 1.0 Mb; approximately 1–4%; recurrent breakpoints involving NF1-REPb and NF1-REPc.
- **Atypical deletions:** nonrecurrent, variable breakpoints and size. A 2021 cohort documented approximately 0.60–7 Mb deletions and several novel configurations. (pacot2024correlationbetweenlarge pages 1-2, buki2021genotypephenotypeassociationsin pages 1-2, kehrersawatzki2017emerginggenotype–phenotyperelationships pages 1-3, buki2021genotypephenotypeassociationsin pages 14-15)

These are pathogenic structural variants causing loss of function/haploinsufficiency. They are germline when present constitutionally, but postzygotic deletions can generate somatic mosaicism. The causal allele is expected to be absent or extremely rare from general-population databases; population allele frequency is not a meaningful carrier-frequency measure for recurrent pathogenic CNVs.

### Risk and modifier factors

The strongest disease risk factor is carrying the deletion. For tumor formation, constitutional NF1 haploinsufficiency is followed by somatic inactivation of the remaining NF1 allele in susceptible cells. Co-deletion of **SUZ12**, encoding a Polycomb repressive complex 2 component, is associated with particularly elevated MPNST risk. Candidate contributors to specific manifestations include **RNF135** for overgrowth/dysmorphism, **ADAP2** for cardiovascular development, and **CRLF3** for neurodevelopment. Additional CNVs and rare RAS-pathway variants may modify expressivity, but these findings are preliminary. (pacot2024correlationbetweenlarge pages 1-2, tritto2024geneticepigeneticeffectsin pages 1-2, kehrersawatzki2017emerginggenotype–phenotyperelationships pages 1-3)

### Environmental, protective, and gene–environment factors

No environmental exposure, infection, toxin, diet, or lifestyle behavior is known to cause the constitutional deletion. No validated genetic or environmental protective factor prevents the syndrome. Ionizing radiation is generally avoided when equivalent non-ionizing surveillance is available because NF1 is a tumor-predisposition disorder, but this is complication-risk management rather than prevention of the deletion. Robust microdeletion-specific gene–environment interactions have not been demonstrated.

## 3. Phenotypes

The phenotype combines ordinary NF1 manifestations with a higher probability of severe developmental, dysmorphic, connective-tissue, cardiovascular, and tumor features. Manifestations are strongly age-dependent; absence in a young child does not predict absence later. (buki2021genotypephenotypeassociationsin pages 1-2, buki2021genotypephenotypeassociationsin pages 14-15)

### Major phenotype groups and ontology suggestions

- **Pigmentary signs:** café-au-lait macules (HP:0000957) and axillary/inguinal freckling (HP:0000997). Usually begin in infancy or early childhood; generally persistent and medically mild, although visible disease may affect psychosocial well-being.
- **Neurofibromas:** cutaneous neurofibromas (HP:0001067), subcutaneous neurofibromas, plexiform neurofibroma (HP:0009732), and spinal/internal neurofibromas. Cutaneous lesions often appear earlier and in larger numbers than in non-deletion NF1; internal tumor burden can be progressive. Non-mosaic deletion patients are enriched for extreme internal tumor volume exceeding 3,000 mL and sometimes more than 1,000 neurofibromas. Pain, disfigurement, neurologic compromise, mobility limitation, and fear of malignancy substantially impair quality of life. (kehrersawatzki2017emerginggenotype–phenotyperelationships pages 1-3, kehrersawatzki2017emerginggenotype–phenotyperelationships pages 17-18)
- **MPNST:** malignant peripheral nerve sheath tumor (HP:0100697). Lifetime risk estimates are approximately **16–26%**, compared with **8–13%** across NF1 more generally. New persistent pain, rapid growth, hardening, neurologic deficit, or altered texture in a pre-existing tumor are concerning. (pacot2024correlationbetweenlarge pages 1-2, kehrersawatzki2017emerginggenotype–phenotyperelationships pages 1-3)
- **Neurodevelopment:** global developmental delay (HP:0001263), intellectual disability (HP:0001249), learning disability (HP:0001328), speech delay (HP:0000750), attention/behavioral problems, and autistic traits. These emerge primarily in childhood, vary from mild learning problems to substantial impairment, and can affect education, independence, and family functioning. (buki2021genotypephenotypeassociationsin pages 1-2, wegscheid2021patientderivedipsccerebralorganoid pages 1-4)
- **Growth and craniofacial morphology:** childhood overgrowth/tall stature (HP:0000098 or age-specific growth terms), macrocephaly (HP:0000256), large hands and feet, and characteristic facial dysmorphism (HP:0001999). Overgrowth may be most prominent in childhood and is more characteristic of type-1 than some atypical deletions. (buki2021genotypephenotypeassociationsin pages 1-2, kehrersawatzki2017emerginggenotype–phenotyperelationships pages 1-3)
- **Musculoskeletal/connective tissue:** muscular hypotonia (HP:0001252), joint hypermobility (HP:0001382), scoliosis (HP:0002650), and bone lesions. Severity is variable; consequences include delayed motor skills, pain, reduced endurance, and orthopedic disability. (kehrersawatzki2017emerginggenotype–phenotyperelationships pages 1-3, buki2021genotypephenotypeassociationsin pages 14-15)
- **Cardiovascular:** congenital heart defects (HP:0001627) and other cardiovascular malformations occur more often than in intragenic NF1 cohorts. NF1-associated hypertension and vasculopathy remain clinically relevant even though they are not unique to the deletion. (pacot2024correlationbetweenlarge pages 1-2, kehrersawatzki2017emerginggenotype–phenotyperelationships pages 1-3)
- **Other conventional NF1 findings:** optic pathway glioma, Lisch nodules, choroidal abnormalities, osseous dysplasia, and endocrine complications may occur, but the retrieved microdeletion evidence does not establish reliable subtype-specific percentages.

A 17-patient pediatric-enriched series found that dysmorphism, macrocephaly, large hands/feet, developmental or learning difficulties, speech problems, and overgrowth were more common than among individuals with intragenic NF1 variants; macrocephaly, neurobehavioral problems, and overgrowth were less frequent in atypical than type-1 deletions. Exact percentages from such small cohorts should not be generalized. (buki2021genotypephenotypeassociationsin pages 1-2)

## 4. Genetic and molecular information

### Principal genes and structural variant classification

- **NF1** encodes neurofibromin, a tumor suppressor and negative regulator of RAS signaling. Its constitutional deletion is pathogenic through haploinsufficiency; tumor initiation generally requires somatic loss/inactivation of the remaining allele.
- **SUZ12** is loss-of-function constrained and encodes a core PRC2 component. Constitutional hemizygosity and subsequent tumor-level PRC2 disruption plausibly explain part of the elevated malignancy risk.
- **RNF135** is implicated in overgrowth and facial dysmorphism; OpenTargets links it to MONDO:0013357.
- **CRLF3** has experimental support for neurodevelopmental effects.
- **ADAP2** is a candidate contributor to cardiovascular abnormalities.
- Other haploinsufficient or biologically plausible interval genes include **ATAD5, OMG, RAB11FIP4, PSMD11, CDK5R1**, and **ASIC2**. (OpenTargets Search: NF1 microdeletion syndrome, tritto2024geneticepigeneticeffectsin pages 1-2, buki2021genotypephenotypeassociationsin pages 14-15, wegscheid2021patientderivedipsccerebralorganoid pages 1-4)

Clinically detected recurrent or atypical deletions encompassing NF1 are classified as pathogenic/likely pathogenic CNVs using ACMG/ClinGen copy-number standards, considering haploinsufficient genes, deletion size, inheritance, and phenotype. The exact genomic coordinates and genome assembly must be recorded; “1.4 Mb deletion” alone is insufficient for atypical cases.

### Modifiers and epigenetics

The 2024 Human Genetics study showed that pathogenesis extends beyond simple dosage loss. In type-1 deletion cells, 4C-seq detected changed breakpoint-flanking DNA contacts, including an acquired interaction between the **RHOT1** promoter and **SLC6A4**, accompanied by increased SLC6A4 expression. The authors’ abstract states that the deletion “leads to changes in the 3D chromatin structure” and “likely causes position effect on the expression of deletion flanking genes.” Rare likely pathogenic RAS-pathway variants were also detected in individuals with incidental features. These results are important but require replication in larger cohorts and disease-relevant tissues. (tritto2024geneticepigeneticeffectsin pages 1-2)

## 5. Environmental information

Environmental factors do not cause NF1 microdeletion syndrome. Smoking, alcohol, diet, exercise, occupational exposures, pollution, and infectious agents have no established etiologic role. Healthy activity, nutrition, sleep, and avoidance of smoking support general health but are not proven to alter the underlying genomic disorder. No zoonotic or transmissible component exists.

## 6. Mechanism and pathophysiology

### Upstream causal chain

**17q11.2 deletion → reduced NF1/neurofibromin dosage → excessive RAS-GTP signaling → increased RAF–MEK–ERK and PI3K–AKT–mTOR activity → altered proliferation, differentiation, and survival.** In peripheral nerve tumors, a second somatic NF1 hit in the Schwann-cell lineage initiates tumor formation; interactions with fibroblasts, mast cells, macrophages, neurons, and extracellular matrix support neurofibroma growth. Suggested GO terms include negative regulation of RAS protein signal transduction (GO:0046580), RAS protein signal transduction (GO:0007265), MAPK cascade (GO:0000165), regulation of cell proliferation (GO:0042127), and peripheral nervous system development (GO:0007422).

### Malignant progression

**Biallelic NF1 loss → plexiform neurofibroma → additional lesions such as CDKN2A loss → ANNUBP → PRC2 disruption through SUZ12/EED loss → broad chromatin dysregulation and MPNST.** Constitutional SUZ12 co-deletion lowers the dosage reserve and is a plausible reason deletion carriers represent a high-risk subgroup. Relevant cell types include Schwann cell (CL:0002573), Schwann-cell precursor/neural-crest derivatives, fibroblast (CL:0000057), mast cell (CL:0000097), and macrophage (CL:0000235). (kehrersawatzki2017emerginggenotype–phenotyperelationships pages 1-3)

### Neurodevelopmental mechanism

Patient-derived cerebral organoids separated NF1-related progenitor proliferation from a **CRLF3–δ-catenin–RhoA** neuronal-maturation pathway. CRLF3 reduction increased immature neurons early, reduced mature neurons later, increased apoptosis, reduced dendritic maturation, and decreased N-cadherin, Rac1, and RhoA activity. Pharmacologic RhoA activation with CN03 rescued maturation and neurite growth. A germline CRLF3 p.Leu389Pro variant was also associated with greater autistic-trait burden in an NF1 cohort. Suggested GO terms include neurogenesis (GO:0022008), neuron differentiation (GO:0030182), dendrite development (GO:0016358), apoptotic process (GO:0006915), and Rho protein signal transduction (GO:0007266). Relevant cell terms include neural stem cell (CL:0000047), neural progenitor cell, and neuron (CL:0000540). (wegscheid2021patientderivedipsccerebralorganoid pages 8-9, wegscheid2021patientderivedipsccerebralorganoid pages 1-4)

### Molecular profiling and advanced technologies

Available approaches include RNA-seq, qPCR, 4C-seq, exome/NGS modifier analysis, RAS/Rac1/RhoA assays, patient-derived iPSC neural cultures, and cerebral organoids. The 2024 chromatin study and 2021 organoid study represent the strongest microdeletion-specific functional evidence retrieved. No validated microdeletion-specific metabolomic, lipidomic, single-cell atlas, or spatial-transcriptomic signature was identified. (tritto2024geneticepigeneticeffectsin pages 1-2, wegscheid2021patientderivedipsccerebralorganoid pages 9-10, wegscheid2021patientderivedipsccerebralorganoid pages 16-17)

## 7. Anatomical structures affected

NF1 microdeletion syndrome is multisystemic:

- **Peripheral nervous system:** peripheral nerves, nerve roots, plexuses, and Schwann-cell lineage; suggested UBERON terms include peripheral nervous system (UBERON:0000010), peripheral nerve (UBERON:0001021), and spinal nerve root.
- **Central nervous system:** brain, optic pathway, and neurodevelopmental circuits; UBERON:0000955 (brain), UBERON:0000966 (retina), and optic nerve terms.
- **Skin/subcutis:** melanocytes and cutaneous peripheral nerves; UBERON:0002097 (skin of body).
- **Skeleton and connective tissue:** vertebral column, long bones, joints, and soft tissue.
- **Cardiovascular system:** heart and blood vessels.
- **Subcellular compartments:** cytosolic RAS signaling machinery, nucleus/chromatin and PRC2, plasma-membrane adhesion complexes, and neuronal cytoskeleton. Suggested GO cellular components include nucleus (GO:0005634), chromatin (GO:0000785), cytoplasm (GO:0005737), plasma membrane (GO:0005886), and dendrite (GO:0030425).

Lesions may be localized, diffuse, unilateral, bilateral, or asymmetric; no syndrome-wide lateralization is expected.

## 8. Temporal development

The deletion is congenital and the disorder is lifelong, but clinical expression is insidious and age dependent. Pigmentary findings often emerge first in infancy. Developmental, speech, behavioral, growth, and congenital cardiovascular features become apparent in early childhood. Plexiform neurofibromas may be congenital or childhood-onset; cutaneous neurofibromas usually accumulate later and can appear earlier and at greater burden in deletion carriers. MPNST risk becomes particularly important from adolescence through adulthood. (pacot2024correlationbetweenlarge pages 1-2, buki2021genotypephenotypeassociationsin pages 1-2)

There are no formal stages for the constitutional syndrome. Tumor evolution can be conceptualized as benign PN → atypical lesion/ANNUBP → MPNST. NF1 itself does not remit. Individual tumors may stabilize, grow, respond to therapy, recur, or transform. Critical intervention windows include early developmental assessment, childhood vision surveillance, recognition of growing plexiform neurofibromas, and rapid investigation of malignant warning symptoms.

## 9. Inheritance and population

The syndrome follows **autosomal-dominant** inheritance. NF1-related manifestations have essentially complete lifetime penetrance, but expressivity is highly variable and age dependent. Clinically unaffected constitutional carriers of a full germline type-1 deletion have not been reported in the reviewed literature. Mosaic type-2 or atypical deletions may be milder depending on tissue distribution. (kehrersawatzki2017emerginggenotype–phenotyperelationships pages 1-3, kehrersawatzki2017emerginggenotype–phenotyperelationships pages 17-18)

Many deletions arise de novo. An affected non-mosaic individual has a theoretical 50% transmission risk in each pregnancy. Parental testing is needed to distinguish de novo occurrence, inherited deletion, and parental mosaicism. Germline mosaicism is possible but poorly quantified. Anticipation, consanguinity, and classic founder effects are not established. Carrier frequency is not ordinarily calculated for this fully penetrant dominant disorder.

Estimated prevalence is approximately **1 in 60,000**, derived from NF1 prevalence near 1:3,000 and microdeletions near 5%; reports place deletions at roughly 4.7–11% of NF1. No reliable annual incidence, geographic enrichment, ethnic predilection, or sex imbalance has been demonstrated. (kehrersawatzki2017emerginggenotype–phenotyperelationships pages 1-3, kehrersawatzki2017emerginggenotype–phenotyperelationships pages 17-18)

## 10. Diagnostics

### Clinical diagnosis

Patients meet the revised clinical framework for NF1 through combinations of café-au-lait macules, freckling, neurofibromas/plexiform neurofibroma, optic pathway glioma, ocular findings, characteristic osseous lesions, an affected parent, or a heterozygous pathogenic NF1 variant. However, early childhood diagnosis can be difficult because many criteria are age dependent. Dysmorphism, overgrowth, developmental delay, congenital heart disease, unusually early neurofibromas, or high tumor load should prompt deletion analysis. (buki2021genotypephenotypeassociationsin pages 1-2, buki2021genotypephenotypeassociationsin pages 14-15)

### Recommended molecular workflow

1. Use an NF1 assay capable of detecting both sequence variants and exon/whole-gene copy-number changes.
2. If sequencing is negative or dosage loss is suspected, perform **MLPA**, validated NGS copy-number analysis, or another dosage assay.
3. Confirm and define the interval with **chromosomal microarray/array-CGH**; this identifies co-deleted genes and atypical extension.
4. Consider breakpoint-specific testing, digital PCR, qPCR, or FISH for confirmation, familial testing, or suspected mosaicism.
5. WGS can define breakpoints and complex rearrangements; WES may detect dosage changes only if the analytical pipeline is validated and is inferior to CMA for defining a contiguous deletion.
6. Conventional karyotyping has low resolution and is not first line. Mitochondrial and repeat-expansion tests are not relevant. (buki2021genotypephenotypeassociationsin pages 1-2, buki2021genotypephenotypeassociationsin pages 5-6)

In the 2021 study, MLPA was used after systematic NF1 sequencing and array-CGH for classification; 17 deletion-positive patients were characterized, including type-1, type-2, mosaic, and novel atypical deletions. The authors describe MLPA as cost-effective, but breakpoint resolution depends on probe density. (buki2021genotypephenotypeassociationsin pages 1-2, buki2021genotypephenotypeassociationsin pages 5-6)

### Clinical evaluation and imaging

Assessment should include skin and neurologic examination, blood pressure, growth and head circumference, developmental/educational screening, ophthalmology, skeletal examination, and cardiovascular evaluation guided by findings. MRI is preferred for symptomatic lesions. In high-risk patients, 2024 recommendations support baseline whole-body MRI after puberty/late adolescence. For painful or growing lesions suspicious for MPNST, regional MRI with diffusion/ADC mapping and **18F-FDG PET/CT** improve characterization; suspicious lesions require multidisciplinary biopsy or resection planning. (perrino2024updateonpediatric pages 6-8)

Differential diagnoses include Legius syndrome/SPRED1, constitutional mismatch-repair deficiency, other RASopathies, isolated café-au-lait macules, segmental/mosaic NF1, and larger or overlapping 17q11.2 CNVs. The distinguishing feature is molecular demonstration of an NF1-containing deletion.

## 11. Outcome and prognosis

NF1 microdeletion syndrome is generally more morbid than NF1 caused by intragenic variants, but individual outcomes remain unpredictable. Major determinants are deletion type and mosaicism, internal/plexiform tumor burden, SUZ12 involvement, neurologic and developmental impairment, cardiovascular disease, and malignant transformation. (pacot2024correlationbetweenlarge pages 1-2, buki2021genotypephenotypeassociationsin pages 1-2)

The most defensible quantitative prognostic statistic is the **16–26% lifetime MPNST risk**, versus approximately 8–13% in general NF1. Non-mosaic patients are more likely to have extreme internal tumor burden. No robust microdeletion-specific five- or ten-year survival curve, life-expectancy estimate, mortality rate, EQ-5D/SF-36 dataset, or validated prognostic calculator was found. (kehrersawatzki2017emerginggenotype–phenotyperelationships pages 1-3)

Functional morbidity can include chronic pain, motor limitation, disfigurement, impaired vision, educational difficulties, reduced employment/independence, and repeated surgery or imaging. Recovery from the genomic syndrome is not possible, but specific complications may improve with surgery, targeted therapy, rehabilitation, educational intervention, and pain management.

## 12. Treatment

There is no treatment that restores the deleted chromosome interval and no therapy approved specifically for NF1 microdeletion syndrome. Management is multidisciplinary and complication directed.

- **Plexiform neurofibroma:** surgical resection when safely feasible and clinically indicated. For symptomatic, inoperable NF1-associated plexiform neurofibromas, MEK inhibition—most established with **selumetinib**—targets downstream RAS–RAF–MEK–ERK signaling. This is an NF1 indication, not a microdeletion-specific therapy; deletion carriers should not be presumed to have a different response without data. Monitor cardiac function, ocular toxicity, gastrointestinal effects, creatine kinase, skin/nail toxicity, and adherence according to the product label and specialist protocols. Suggested MAXO: pharmacotherapy, molecularly targeted therapy, tumor surveillance, MRI, and surgical resection.
- **Suspected ANNUBP/MPNST:** urgent specialist imaging, image-guided biopsy when appropriate, and complete oncologic resection with negative margins when feasible. Chemotherapy and radiotherapy decisions are individualized; the constitutional tumor predisposition and radiation risks require specialist review.
- **Developmental/behavioral morbidity:** early-intervention services, individualized education, neuropsychological assessment, speech-language therapy, occupational therapy, physical therapy, and treatment of ADHD/anxiety when indicated.
- **Pain and functional disease:** multimodal analgesia, physiotherapy, rehabilitation, psychological support, and treatment of the causative tumor or orthopedic lesion.
- **Cardiovascular/orthopedic/ophthalmic complications:** standard specialty treatment tailored to the lesion.

Current NF1 trials include MEK inhibitors and imaging/biomarker strategies, but no retrieved trial was restricted to NF1 microdeletion syndrome. The 2024 recommendations cite **NCT06188741**, evaluating surveillance and early treatment of asymptomatic high-risk plexiform neurofibromas. Investigational cell-free DNA surveillance is not yet standard care. (perrino2024updateonpediatric pages 6-8)

No validated microdeletion-specific pharmacogenomic rule, gene therapy, cell therapy, RNA therapy, or CRISPR treatment is clinically available. The organoid rescue of CRLF3-related defects by RhoA activation is mechanistic proof-of-concept, not a therapeutic recommendation. (wegscheid2021patientderivedipsccerebralorganoid pages 8-9)

## 13. Prevention

### Primary prevention

The deletion cannot be prevented through lifestyle or immunization. Reproductive options after genetic counseling include prenatal diagnosis by chorionic-villus sampling or amniocentesis and preimplantation genetic testing for a known familial deletion. Testing must be designed to detect the family’s CNV and, where relevant, mosaicism.

### Secondary and tertiary prevention

Early molecular confirmation, cascade testing, developmental screening, ophthalmologic surveillance, blood-pressure monitoring, and tumor surveillance can reduce avoidable morbidity. The 2024 high-risk approach recommends baseline whole-body MRI after puberty/late adolescence and closer follow-up when internal tumor burden exceeds **300 mL** or a distinct nodular lesion is present. Patients should be educated to report persistent or nocturnal pain, rapid enlargement, hardening, weakness, sensory change, or functional decline promptly. (perrino2024updateonpediatric pages 6-8)

There is no population newborn-screening program, preventive medication, vaccine, dietary prophylaxis, or environmental intervention specific to NF1 microdeletion syndrome.

## 14. Other species and natural disease

No naturally occurring veterinary syndrome precisely equivalent to the recurrent human 17q11.2 contiguous deletion was identified. **NF1/Nf1** orthologs are evolutionarily conserved in mouse (*Mus musculus*, NCBI Taxon 10090), rat (10116), zebrafish (*Danio rerio*, 7955), and fruit fly (*Drosophila melanogaster*, 7227). Naturally occurring peripheral nerve sheath tumors occur in animals, but they should not be equated with the human microdeletion syndrome without genomic confirmation. There is no zoonotic transmission or cross-species contagion.

## 15. Model organisms and experimental systems

The most disease-specific model is the **patient-derived iPSC cerebral-organoid system** reported in 2021. Lines from three individuals with 1.4-Mb total-gene deletions and one atypical deletion were differentiated into neural stem cells, two-dimensional neurons, and forebrain cerebral organoids. CRLF3 knockdown phenocopied neuronal survival and maturation abnormalities, and RhoA activation rescued key defects. Strengths include human genetic background, developmental cell types, isogenic perturbations, and functional rescue; limitations include immature organoids, lack of vasculature/immune context, small donor numbers, and uncertain translation to cognition in vivo. (wegscheid2021patientderivedipsccerebralorganoid pages 8-9, wegscheid2021patientderivedipsccerebralorganoid pages 1-4, wegscheid2021patientderivedipsccerebralorganoid pages 16-17)

General NF1 models include conditional **Nf1** knockout mice in Schwann-cell or neural-crest lineages, genetically engineered peripheral nerve-sheath tumor models, zebrafish, Drosophila, primary Schwann cells, tumor cell lines, xenografts, and patient-derived tumor models. They are valuable for RAS biology, neurofibroma initiation, cognition, and drug development, but deletion of Nf1 alone does not reproduce haploinsufficiency of the complete human interval. No validated mouse, zebrafish, or fly model carrying a syntenic deletion equivalent to the complete recurrent human 1.4-Mb interval was identified in the retrieved literature.

## Recent research priorities and expert interpretation

The field is moving from a simple “more severe because more genes are deleted” model toward a multilayer model involving gene dosage, tissue mosaicism, second-hit tumor genetics, trans-acting modifiers, and deletion-induced chromatin reorganization. Pacot and colleagues’ 2024 study emphasizes deletion length, co-deleted genes, and background CNVs; Tritto and colleagues add position effects outside the deleted interval; the organoid work gives functional evidence for CRLF3-mediated neurogenesis. Together, these findings support interval-resolved diagnosis and personalized follow-up but do not yet justify gene-specific therapies. (pacot2024correlationbetweenlarge pages 1-2, tritto2024geneticepigeneticeffectsin pages 1-2, wegscheid2021patientderivedipsccerebralorganoid pages 8-9)

Highest-priority research gaps are prospective natural-history cohorts stratified by deletion type and mosaic fraction; standardized age-adjusted phenotype frequencies; microdeletion-specific MEK-inhibitor outcomes; longitudinal MPNST surveillance studies; single-cell/spatial analysis of neural and tumor tissues; and whole-interval animal or isogenic human models.

## Key sources, publication dates, and links

1. Pacot L, et al. *Correlation between large rearrangements and patient phenotypes in NF1 deletion syndrome: an update and review.* **BMC Medical Genomics. March 2024.** DOI: [10.1186/s12920-024-01843-5](https://doi.org/10.1186/s12920-024-01843-5). Human cohort, n=22, plus review. (pacot2024correlationbetweenlarge pages 1-2)
2. Tritto V, et al. *Genetic/epigenetic effects in NF1 microdeletion syndrome: beyond the haploinsufficiency, looking at the contribution of not deleted genes.* **Human Genetics. June 2024;143:775–795.** DOI: [10.1007/s00439-024-02683-0](https://doi.org/10.1007/s00439-024-02683-0). Human qPCR, 4C-seq, and NGS study. (tritto2024geneticepigeneticeffectsin pages 1-2)
3. Perrino MR, et al. *Update on Pediatric Cancer Surveillance Recommendations…* **Clinical Cancer Research. August 2024;30:4834–4843.** DOI: [10.1158/1078-0432.CCR-24-1611](https://doi.org/10.1158/1078-0432.CCR-24-1611). Expert surveillance consensus. (perrino2024updateonpediatric pages 6-8)
4. Büki G, et al. *Genotype-Phenotype Associations in Patients With Type-1, Type-2, and Atypical NF1 Microdeletions.* **Frontiers in Genetics. June 2021;12:673025.** DOI: [10.3389/fgene.2021.673025](https://doi.org/10.3389/fgene.2021.673025). Human cohort, n=17. (buki2021genotypephenotypeassociationsin pages 1-2, buki2021genotypephenotypeassociationsin pages 5-6)
5. Wegscheid ML, et al. *Patient-derived iPSC-cerebral organoid modeling of the 17q11.2 microdeletion syndrome establishes CRLF3 as a critical regulator of neurogenesis.* **Cell Reports. July 6, 2021;36:109315.** DOI: [10.1016/j.celrep.2021.109315](https://doi.org/10.1016/j.celrep.2021.109315). Patient-derived organoid/in-vitro functional study. (wegscheid2021patientderivedipsccerebralorganoid pages 8-9, wegscheid2021patientderivedipsccerebralorganoid pages 1-4)
6. Kehrer-Sawatzki H, et al. *Emerging genotype–phenotype relationships in patients with large NF1 deletions.* **Human Genetics. February 2017;136:349–376.** DOI: [10.1007/s00439-017-1766-y](https://doi.org/10.1007/s00439-017-1766-y). Landmark review and risk synthesis. (kehrersawatzki2017emerginggenotype–phenotyperelationships pages 1-3, kehrersawatzki2017emerginggenotype–phenotyperelationships pages 17-18)

**Evidence caveat:** PMID values were not consistently exposed by the retrieved full-text metadata, so DOI URLs are supplied rather than inventing identifiers. Direct quotations above are limited to wording verifiably present in retrieved abstracts. Microdeletion-specific evidence remains dominated by small cohorts, reviews, and experimental models; general NF1 management recommendations are explicitly identified as extrapolations where applicable.

References

1. (pacot2024correlationbetweenlarge pages 1-2): Laurence Pacot, Milind Girish, Samantha Knight, Gill Spurlock, Vinod Varghese, Manuela Ye, Nick Thomas, Eric Pasmant, and Meena Upadhyaya. Correlation between large rearrangements and patient phenotypes in nf1 deletion syndrome: an update and review. BMC Medical Genomics, Mar 2024. URL: https://doi.org/10.1186/s12920-024-01843-5, doi:10.1186/s12920-024-01843-5. This article has 5 citations and is from a peer-reviewed journal.

2. (tritto2024geneticepigeneticeffectsin pages 1-2): Viviana Tritto, Paola Bettinaglio, Eleonora Mangano, Claudia Cesaretti, Federica Marasca, Chiara Castronovo, Roberta Bordoni, Cristina Battaglia, Veronica Saletti, Valeria Ranzani, Beatrice Bodega, Marica Eoli, Federica Natacci, and Paola Riva. Genetic/epigenetic effects in nf1 microdeletion syndrome: beyond the haploinsufficiency, looking at the contribution of not deleted genes. Human Genetics, 143:775-795, Jun 2024. URL: https://doi.org/10.1007/s00439-024-02683-0, doi:10.1007/s00439-024-02683-0. This article has 3 citations and is from a peer-reviewed journal.

3. (kehrersawatzki2017emerginggenotype–phenotyperelationships pages 1-3): Hildegard Kehrer-Sawatzki, Victor-Felix Mautner, and David N. Cooper. Emerging genotype–phenotype relationships in patients with large nf1 deletions. Human Genetics, 136:349-376, Feb 2017. URL: https://doi.org/10.1007/s00439-017-1766-y, doi:10.1007/s00439-017-1766-y. This article has 260 citations and is from a peer-reviewed journal.

4. (perrino2024updateonpediatric pages 6-8): Melissa R. Perrino, Anirban Das, Sarah R. Scollon, Sarah G. Mitchell, Mary-Louise C. Greer, Marielle E. Yohe, Jordan R. Hansford, Jennifer M. Kalish, Kris Ann P. Schultz, Suzanne P. MacFarland, Wendy K. Kohlmann, Philip J. Lupo, Kara N. Maxwell, Stefan M. Pfister, Rosanna Weksberg, Orli Michaeli, Marjolijn C.J. Jongmans, Gail E. Tomlinson, Jack Brzezinski, Uri Tabori, Gina M. Ney, Karen W. Gripp, Andrea M. Gross, Brigitte C. Widemann, Douglas R. Stewart, Emma R. Woodward, and Christian P. Kratz. Update on pediatric cancer surveillance recommendations for patients with neurofibromatosis type 1, noonan syndrome, cbl syndrome, costello syndrome, and related rasopathies. Clinical Cancer Research, 30:4834-4843, Aug 2024. URL: https://doi.org/10.1158/1078-0432.ccr-24-1611, doi:10.1158/1078-0432.ccr-24-1611. This article has 52 citations and is from a highest quality peer-reviewed journal.

5. (OpenTargets Search: NF1 microdeletion syndrome): Open Targets Query (NF1 microdeletion syndrome, 3 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

6. (wegscheid2021patientderivedipsccerebralorganoid pages 8-9): Michelle L. Wegscheid, Corina Anastasaki, Kelly A. Hartigan, Olivia M. Cobb, Jason B. Papke, Jennifer N. Traber, Stephanie M. Morris, and David H. Gutmann. Patient-derived ipsc-cerebral organoid modeling of the 17q11.2 microdeletion syndrome establishes crlf3 as a critical regulator of neurogenesis. Cell reports, 36:109315-109315, Jul 2021. URL: https://doi.org/10.1016/j.celrep.2021.109315, doi:10.1016/j.celrep.2021.109315. This article has 58 citations and is from a highest quality peer-reviewed journal.

7. (kehrersawatzki2017emerginggenotype–phenotyperelationships pages 17-18): Hildegard Kehrer-Sawatzki, Victor-Felix Mautner, and David N. Cooper. Emerging genotype–phenotype relationships in patients with large nf1 deletions. Human Genetics, 136:349-376, Feb 2017. URL: https://doi.org/10.1007/s00439-017-1766-y, doi:10.1007/s00439-017-1766-y. This article has 260 citations and is from a peer-reviewed journal.

8. (buki2021genotypephenotypeassociationsin pages 1-2): Gergely Büki, Anna Zsigmond, Márta Czakó, Renáta Szalai, Gréta Antal, Viktor Farkas, György Fekete, Dóra Nagy, Márta Széll, Marianna Tihanyi, Béla Melegh, Kinga Hadzsiev, and Judit Bene. Genotype-phenotype associations in patients with type-1, type-2, and atypical nf1 microdeletions. Frontiers in Genetics, Jun 2021. URL: https://doi.org/10.3389/fgene.2021.673025, doi:10.3389/fgene.2021.673025. This article has 26 citations and is from a peer-reviewed journal.

9. (buki2021genotypephenotypeassociationsin pages 14-15): Gergely Büki, Anna Zsigmond, Márta Czakó, Renáta Szalai, Gréta Antal, Viktor Farkas, György Fekete, Dóra Nagy, Márta Széll, Marianna Tihanyi, Béla Melegh, Kinga Hadzsiev, and Judit Bene. Genotype-phenotype associations in patients with type-1, type-2, and atypical nf1 microdeletions. Frontiers in Genetics, Jun 2021. URL: https://doi.org/10.3389/fgene.2021.673025, doi:10.3389/fgene.2021.673025. This article has 26 citations and is from a peer-reviewed journal.

10. (buki2021genotypephenotypeassociationsin pages 5-6): Gergely Büki, Anna Zsigmond, Márta Czakó, Renáta Szalai, Gréta Antal, Viktor Farkas, György Fekete, Dóra Nagy, Márta Széll, Marianna Tihanyi, Béla Melegh, Kinga Hadzsiev, and Judit Bene. Genotype-phenotype associations in patients with type-1, type-2, and atypical nf1 microdeletions. Frontiers in Genetics, Jun 2021. URL: https://doi.org/10.3389/fgene.2021.673025, doi:10.3389/fgene.2021.673025. This article has 26 citations and is from a peer-reviewed journal.

11. (wegscheid2021patientderivedipsccerebralorganoid pages 1-4): Michelle L. Wegscheid, Corina Anastasaki, Kelly A. Hartigan, Olivia M. Cobb, Jason B. Papke, Jennifer N. Traber, Stephanie M. Morris, and David H. Gutmann. Patient-derived ipsc-cerebral organoid modeling of the 17q11.2 microdeletion syndrome establishes crlf3 as a critical regulator of neurogenesis. Cell reports, 36:109315-109315, Jul 2021. URL: https://doi.org/10.1016/j.celrep.2021.109315, doi:10.1016/j.celrep.2021.109315. This article has 58 citations and is from a highest quality peer-reviewed journal.

12. (wegscheid2021patientderivedipsccerebralorganoid pages 9-10): Michelle L. Wegscheid, Corina Anastasaki, Kelly A. Hartigan, Olivia M. Cobb, Jason B. Papke, Jennifer N. Traber, Stephanie M. Morris, and David H. Gutmann. Patient-derived ipsc-cerebral organoid modeling of the 17q11.2 microdeletion syndrome establishes crlf3 as a critical regulator of neurogenesis. Cell reports, 36:109315-109315, Jul 2021. URL: https://doi.org/10.1016/j.celrep.2021.109315, doi:10.1016/j.celrep.2021.109315. This article has 58 citations and is from a highest quality peer-reviewed journal.

13. (wegscheid2021patientderivedipsccerebralorganoid pages 16-17): Michelle L. Wegscheid, Corina Anastasaki, Kelly A. Hartigan, Olivia M. Cobb, Jason B. Papke, Jennifer N. Traber, Stephanie M. Morris, and David H. Gutmann. Patient-derived ipsc-cerebral organoid modeling of the 17q11.2 microdeletion syndrome establishes crlf3 as a critical regulator of neurogenesis. Cell reports, 36:109315-109315, Jul 2021. URL: https://doi.org/10.1016/j.celrep.2021.109315, doi:10.1016/j.celrep.2021.109315. This article has 58 citations and is from a highest quality peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](NF1_Microdeletion_Syndrome-deep-research-falcon_artifacts/artifact-00.md)