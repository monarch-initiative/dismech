---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-07-31T17:53:56.137546'
end_time: '2026-07-31T18:02:16.130419'
duration_seconds: 499.99
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Familial Nonmedullary Thyroid Carcinoma
  mondo_id: ''
  category: ''
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 38
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Familial_Nonmedullary_Thyroid_Carcinoma-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Familial Nonmedullary Thyroid Carcinoma
- **MONDO ID:**  (if available)
- **Category:** 

## Research Objectives

Please provide a comprehensive research report on **Familial Nonmedullary Thyroid Carcinoma** covering all of the
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

For each treatment, suggest NCIT (NCI Thesaurus) clinical-intervention terms where applicable.

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
- Ontology term suggestions (HPO, GO, CL, UBERON, CHEBI, NCIT, MONDO) where applicable
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
- Treatment annotations (NCIT terms)
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
- **Disease Name:** Familial Nonmedullary Thyroid Carcinoma
- **MONDO ID:**  (if available)
- **Category:** 

## Research Objectives

Please provide a comprehensive research report on **Familial Nonmedullary Thyroid Carcinoma** covering all of the
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

For each treatment, suggest NCIT (NCI Thesaurus) clinical-intervention terms where applicable.

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
- Ontology term suggestions (HPO, GO, CL, UBERON, CHEBI, NCIT, MONDO) where applicable
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
- Treatment annotations (NCIT terms)
- Evidence items with PMIDs and exact abstract quotes
- Epidemiology, prognosis, diagnostic, and prevention information
- Animal model descriptions with phenotype recapitulation details


# Familial Nonmedullary Thyroid Carcinoma: Disease-Characteristics Report

## Executive summary

Familial nonmedullary thyroid carcinoma (FNMTC) is familial aggregation of follicular-cell-derived thyroid carcinoma—predominantly papillary thyroid carcinoma (PTC)—rather than medullary thyroid carcinoma. The conventional clinical definition is NMTC in at least two first-degree relatives, after excluding a recognized tumor-predisposition syndrome. However, only an estimated 31–38% of two-case families may represent true inherited disease, versus approximately 96% of families with at least three affected members. Thus, ≥3 affected relatives is a more specific research definition. FNMTC comprises roughly 5–15% of NMTC in recent reviews; approximately 5% of familial cases are explained by recognized syndromes, while most nonsyndromic cases remain genetically unresolved. (yang2016familialnonmedullarythyroid pages 13-14, sanchezares2022susceptibilitygenesand pages 1-2, kamani2022geneticsusceptibilityto pages 1-2)

The principal current conclusion is that nonsyndromic FNMTC is not one Mendelian disorder. It is genetically heterogeneous, usually modeled as autosomal-dominant susceptibility with incomplete, age-dependent penetrance and variable expressivity, or as a polygenic trait. No single germline gene explains most isolated families. Confirmed, clinically actionable genes mainly belong to syndromic disease—**APC, PTEN, DICER1, PRKAR1A,** and **WRN**—whereas **FOXE1, SRGAP1, NKX2-1, HABP2, MAP2K5, DUOX2, CHEK2, POT1** and numerous other candidates require family-specific interpretation and, for many, independent replication. (capezzone2021familialnonmedullarythyroid pages 2-4, capezzone2021familialnonmedullarythyroid pages 4-5, sanchezares2022susceptibilitygenesand pages 1-2, kamani2022geneticsusceptibilityto pages 11-12)

## 1. Disease information

### Definition, category, and synonyms

**Category:** rare/familial endocrine malignancy; hereditary cancer predisposition; follicular-cell-derived thyroid carcinoma.

Common labels are **familial nonmedullary thyroid carcinoma**, **familial non-medullary thyroid cancer**, **familial nonmedullary thyroid cancer**, and—when all tumors are papillary—**familial papillary thyroid carcinoma (FPTC)**. FPTC is a subset rather than a complete synonym because follicular, oncocytic/Hürthle-cell, and very rarely anaplastic histologies also occur. Reviews estimate histologic distributions of approximately 85–91% PTC, 6–9.7% follicular carcinoma, and much smaller proportions of Hürthle-cell or anaplastic carcinoma. (yang2016familialnonmedullarythyroid pages 1-2)

A useful exact abstract statement from Capezzone et al. (published online October 2020; journal issue 2021) is: **“Familial non-medullary thyroid carcinoma (FNMTC), mainly of papillary histotype (FPTC), is defined by the presence of the disease in two or more first-degree relatives in the absence of other known familial syndromes.”** DOI: [10.1007/s40618-020-01435-x](https://doi.org/10.1007/s40618-020-01435-x). (capezzone2021familialnonmedullarythyroid pages 1-2)

### Identifiers and coding

A definitive dedicated **MONDO**, **OMIM**, **Orphanet**, **MeSH**, ICD-10, or ICD-11 identifier was not established in the retrieved evidence. FNMTC is primarily a clinical familial-aggregation construct, and nonsyndromic disease is genetically heterogeneous rather than a single molecular entity. For production curation, the current releases of these terminologies should therefore be queried directly rather than assigning an unverified identifier. ICD coding ordinarily uses the thyroid malignancy code plus family-history/genetic-susceptibility modifiers; it does not encode the full FNMTC construct. Syndromic cases should additionally receive the identifier for the causal syndrome. (capezzone2021familialnonmedullarythyroid pages 4-5, sanchezares2022susceptibilitygenesand pages 1-2)

The following table provides conservative ontology recommendations; unverified IDs are deliberately not invented.

| Domain | Recommended identifier/ontology term | Annotation/use | Evidence caveat |
|---|---|---|---|
| Disease | Familial non-medullary thyroid carcinoma (FNMTC) | Core disease label for hereditary thyroid carcinoma arising from follicular-cell–derived, non-medullary histologies; typically used for disease-level KB entry | Commonly defined clinically as NMTC in ≥2 first-degree relatives, but many experts note families with only 2 cases may include sporadic clustering; stricter research enrichment often uses ≥3 affected relatives (capezzone2021familialnonmedullarythyroid pages 2-4, yang2016familialnonmedullarythyroid pages 13-14, sanchezares2022susceptibilitygenesand pages 1-2) |
| Disease identifier | MONDO: unverified | MONDO ID should be added only after curation against current MONDO release | A stable MONDO term was not established from available evidence; do not invent ID (sanchezares2022susceptibilitygenesand pages 1-2) |
| Disease identifier | OMIM: heterogeneous trait / unverified disease-level OMIM | OMIM may be better represented through susceptibility loci/genes and syndromic conditions rather than a single definitive nonsyndromic disease entry | Available evidence emphasizes marked genetic heterogeneity and lack of one confirmed driver gene (capezzone2021familialnonmedullarythyroid pages 4-5, kamani2022geneticsusceptibilityto pages 11-12) |
| Disease identifier | MeSH / ICD-10 / ICD-11: use broader thyroid carcinoma terms if needed; FNMTC-specific code unverified | For coding, map to broader non-medullary/differentiated thyroid carcinoma terms with a familial modifier in local schema | FNMTC is mainly a clinical/familial aggregation construct rather than a uniquely coded nosologic entity in available sources (capezzone2021familialnonmedullarythyroid pages 2-4, capezzone2021familialnonmedullarythyroid pages 1-2) |
| Synonym | Familial nonmedullary thyroid carcinoma | Exact synonym/label normalization | Hyphenation varies by source (capezzone2021familialnonmedullarythyroid pages 1-2) |
| Synonym | Familial non-medullary thyroid cancer | Common literature synonym | Often used interchangeably with carcinoma in reviews (capezzone2021familialnonmedullarythyroid pages 2-4, yang2016familialnonmedullarythyroid pages 1-2) |
| Synonym | Familial nonmedullary thyroid cancer | Common synonym for search expansion | Includes papillary-predominant familial disease (yang2016familialnonmedullarythyroid pages 1-2, sanchezares2022susceptibilitygenesand pages 1-2) |
| Synonym | Familial papillary thyroid carcinoma (subset term) | Use when kindred/pathology is specifically papillary thyroid carcinoma | Not synonymous with all FNMTC because follicular and rarer histologies also occur (yang2016familialnonmedullarythyroid pages 1-2, sanchezares2022susceptibilitygenesand pages 1-2) |
| HPO phenotype | Thyroid carcinoma (HPO term recommended; stable ID not asserted here) | Parent malignant phenotype for affected individuals | Most familial tumors are papillary histology; exact HPO ID not asserted to avoid miscoding (yang2016familialnonmedullarythyroid pages 1-2, sanchezares2022susceptibilitygenesand pages 1-2) |
| HPO phenotype | Thyroid nodule (HPO term recommended; stable ID not asserted here) | Captures benign or suspicious nodules found in affected relatives and screening | Benign nodules frequently accompany NS-FNMTC; exact HPO ID not asserted here (NCT01109420 chunk 1, sanchezares2022susceptibilitygenesand pages 1-2) |
| HPO phenotype | Multifocal thyroid carcinoma / multifocal neoplasm (HPO term recommended; stable ID not asserted here) | Important clinicopathologic feature often reported in familial cases | Familial series reported multifocality around 56%; exact HPO wording may require curator choice (cirello2021clinicalandgenetic pages 3-4) |
| HPO phenotype | Lymph node metastasis (HPO term recommended; stable ID not asserted here) | Use for nodal spread, especially cervical lymph nodes | Familial cases often present with more nodal disease/aggressive features, but outcome may remain similar with treatment (yang2016familialnonmedullarythyroid pages 1-2, cirello2021clinicalandgenetic pages 1-2, kamani2022geneticsusceptibilityto pages 1-2) |
| HPO phenotype | Lung metastasis (HPO term recommended; stable ID not asserted here) | Use for distant metastatic spread to lung | Present in a minority of reported familial cases (~7% in one monocentric series) (cirello2021clinicalandgenetic pages 3-4) |
| HPO phenotype | Goiter / multinodular goiter (HPO term recommended; stable ID not asserted here) | Useful for syndromic or non-syndromic familial thyroid disease annotation | Multinodular goiter can co-occur and may be part of some familial definitions in older/pathology literature (sanchezares2022susceptibilitygenesand pages 1-2) |
| Anatomy | UBERON:0002046 thyroid gland | Primary affected organ for FNMTC | Robust stable anatomy term; disease arises from follicular epithelium (sanchezares2022susceptibilitygenesand pages 1-2, kamani2022geneticsusceptibilityto pages 1-2) |
| Anatomy | UBERON cervical lymph node term recommended; stable ID unverified here | Secondary site for regional metastasis annotation | Cervical nodal spread is clinically important, but exact UBERON descendant term not asserted without ontology lookup (cirello2021clinicalandgenetic pages 3-4, kamani2022geneticsusceptibilityto pages 1-2) |
| Cell type | CL:0000501 thyroid follicular cell | Principal cell of origin for non-medullary thyroid carcinoma | Appropriate for papillary/follicular lineage annotation (sanchezares2022susceptibilitygenesand pages 1-2, kamani2022geneticsusceptibilityto pages 1-2) |
| Biological process | GO:0000165 MAPK cascade | Mechanistic pathway annotation for signaling dysregulation | Supported by WGS/pathway analyses implicating MAPK/ERK signaling, though specific causal germline alterations vary by family (srivastava2019wholegenomesequencing pages 5-7, srivastava2019wholegenomesequencing pages 19-21) |
| Biological process | PI3K-AKT signaling pathway (GO/Reactome term recommended; stable GO ID not asserted here) | Complementary pathway annotation for predisposition/mechanism | Central pathway implicated in WGS/network analyses; exact ontology ID not asserted here (srivastava2019wholegenomesequencing pages 5-7, srivastava2019wholegenomesequencing pages 19-21) |
| Biological process | GO:0008283 cell population proliferation | Generic downstream cancer process annotation | Broad downstream consequence rather than FNMTC-specific mechanism (srivastava2019wholegenomesequencing pages 5-7, srivastava2019wholegenomesequencing pages 19-21) |
| Gene | APC | Syndromic FNMTC gene; annotate when thyroid carcinoma occurs with familial adenomatous polyposis/Gardner syndrome | High-confidence syndromic association, not a confirmed common cause of isolated non-syndromic FNMTC (capezzone2021familialnonmedullarythyroid pages 4-5, yang2016familialnonmedullarythyroid pages 2-4, sanchezares2022susceptibilitygenesand pages 1-2) |
| Gene | PTEN | Syndromic FNMTC gene; annotate for Cowden/PTEN hamartoma tumor syndrome | Strong syndromic evidence; actionable in appropriate phenotype context (yang2016familialnonmedullarythyroid pages 2-4, sanchezares2022susceptibilitygenesand pages 1-2) |
| Gene | DICER1 | Syndromic predisposition gene for familial thyroid neoplasia | Relevant especially when other DICER1-spectrum manifestations are present (capezzone2021familialnonmedullarythyroid pages 4-5, sanchezares2022susceptibilitygenesand pages 1-2) |
| Gene | PRKAR1A | Syndromic gene for Carney complex-associated thyroid carcinoma | Use when phenotype supports Carney complex rather than isolated FNMTC (capezzone2021familialnonmedullarythyroid pages 4-5, sanchezares2022susceptibilitygenesand pages 1-2) |
| Gene | WRN | Syndromic gene for Werner syndrome-associated thyroid carcinoma | Rare syndromic association; not typical isolated FNMTC driver (capezzone2021familialnonmedullarythyroid pages 4-5, sanchezares2022susceptibilitygenesand pages 1-2) |
| Gene/locus evidence caveat | FOXE1, HABP2, SRGAP1, TITF1/NKX2.1, MAP2K5, DUOX2, POT1, CHEK2 and others as candidate susceptibility genes/loci | Consider as research/candidate annotations, not definitive disease-gene assertions for routine KB causal field unless separately curated | Reviews emphasize heterogeneity, low-to-moderate penetrance, inconsistent replication, and no single confirmed nonsyndromic driver gene (capezzone2021familialnonmedullarythyroid pages 4-5, yang2016familialnonmedullarythyroid pages 13-14, cirello2021clinicalandgenetic pages 1-2, kamani2022geneticsusceptibilityto pages 11-12) |
| Intervention | NCIT term recommended: Thyroidectomy | Primary definitive local treatment annotation | Total thyroidectomy frequently used in reported familial series; current guidelines generally do not mandate different surgery solely for family history (capezzone2021familialnonmedullarythyroid pages 6-7, cirello2021clinicalandgenetic pages 3-4) |
| Intervention | NCIT term recommended: Radioactive Iodine Therapy | Adjuvant treatment annotation for selected differentiated thyroid cancers | Applied according to standard differentiated thyroid cancer risk stratification rather than FNMTC-specific evidence (sanchezares2022susceptibilitygenesand pages 1-2) |
| Intervention | NCIT term recommended: Thyroid-Stimulating Hormone Suppression Therapy | Postoperative endocrine management annotation | Use as standard differentiated thyroid cancer management; FNMTC-specific modification not established (capezzone2021familialnonmedullarythyroid pages 6-7, sanchezares2022susceptibilitygenesand pages 1-2) |
| Intervention | NCIT term recommended: Kinase Inhibitor Therapy | Targeted systemic treatment annotation for advanced/refractory disease | Because familial and sporadic NMTC share morphology and somatic drivers, similar targeted therapies are currently used when indicated (sanchezares2022susceptibilitygenesand pages 1-2) |
| Screening/implementation | Neck ultrasound surveillance in at-risk relatives | Real-world screening annotation for high-risk families/research cohorts | Evidence is mixed: one prospective cohort found thyroid cancer in 4.6% of screened relatives from families with 2 affected members, and major guidelines do not currently recommend universal genetic screening of at-risk relatives (capezzone2021familialnonmedullarythyroid pages 4-5, NCT01109420 chunk 1, kamani2022geneticsusceptibilityto pages 14-15) |


*Table: This compact table lists practical knowledge-base annotations for familial nonmedullary thyroid carcinoma, including disease labels, suggested ontology terms, syndromic genes, mechanisms, and interventions. It also flags where the evidence is strong versus where identifiers or causal claims remain unverified or heterogeneous.*

### Source granularity

The report synthesizes **aggregated disease-level resources**, peer-reviewed reviews, family cohorts, tumor-series data, WGS analyses, and an observational registry. It is not derived from an individual EHR. One detailed Italian study included 33 unrelated families, 74 affected and 12 unaffected relatives; a separate WGS study examined 23 affected and three unaffected members of five families. (cirello2021clinicalandgenetic pages 1-2, srivastava2019wholegenomesequencing pages 2-5)

## 2. Etiology and risk factors

### Genetic causation

Two etiologic classes should be separated:

1. **Syndromic FNMTC:** thyroid carcinoma is one manifestation of a defined inherited syndrome. Strong gene–syndrome associations include **APC**–familial adenomatous polyposis/Gardner syndrome, **PTEN**–PTEN hamartoma tumor syndrome/Cowden syndrome, **DICER1** tumor-predisposition syndrome, **PRKAR1A**–Carney complex, and **WRN**–Werner syndrome. These are the most actionable germline findings. (capezzone2021familialnonmedullarythyroid pages 4-5, yang2016familialnonmedullarythyroid pages 2-4, sanchezares2022susceptibilitygenesand pages 1-2)
2. **Nonsyndromic FNMTC:** the commoner class, with complex monogenic, oligogenic, or polygenic susceptibility. Linkage regions include TCO/19p13.2, fPTC/PRN/1q21, NMTC1/2q21, MNG1, FTEN, 6q22, and 8q24. Candidate genes include **FOXE1, SRGAP1, NKX2-1, HABP2, MAP2K5, SRRM2, DUOX2, PLCB1, BROX, POT1, ATM, CHEK2, NOP53, NDUFA13, TIMM44, ANXA3, NTN4, SERPINA1, FKBP10, PLEKHG5, P2RX5,** and **SAPCD1**. Most associations are not sufficiently replicated for routine predictive testing. (yang2016familialnonmedullarythyroid pages 1-2, cirello2021clinicalandgenetic pages 2-3, kamani2022geneticsusceptibilityto pages 11-12)

Classic tumor drivers—**BRAF, RAS, RET/PTC, NTRK**, and **PPARG** rearrangements—are generally somatic rather than inherited FNMTC causes. Familial and sporadic tumors share these alterations. (capezzone2021familialnonmedullarythyroid pages 2-4, sanchezares2022susceptibilitygenesand pages 1-2)

### Variant interpretation

* **HABP2 p.Gly534Glu (G534E):** initially proposed as a dominant susceptibility allele, but subsequent studies found inconsistent segregation and association. It should not be treated as a universally pathogenic FNMTC variant. (capezzone2021familialnonmedullarythyroid pages 4-5, yang2016familialnonmedullarythyroid pages 13-14)
* **DUOX2 c.3607A>G, p.Tyr1203His:** reported to co-segregate in one family and estimated as extremely rare—approximately 1/138,000—but absent from all 86 tested members of 33 independent Italian families. This is a family-level candidate, not a validated general cause. (cirello2021clinicalandgenetic pages 2-3, cirello2021clinicalandgenetic pages 1-2)
* **FOXE1:** the strongest repeatedly supported common susceptibility locus, but largely a moderate/low-effect risk locus rather than a highly penetrant diagnostic gene. Reviews describe FOXE1 penetrance as moderate-to-high for selected variants, while many GWAS loci have odds ratios only around 1.2–1.8. (capezzone2021familialnonmedullarythyroid pages 2-4, kamani2022geneticsusceptibilityto pages 14-15, kamani2022geneticsusceptibilityto pages 15-16)
* **CHEK2, POT1, RET, TG, EWSR1** and other rare WGS candidates require segregation, population-frequency, functional, and independent-family validation before ACMG pathogenic classification. One WGS pipeline required MAF <0.1%, CADD-PHRED >10, family segregation, and predicted deleteriousness by ≥60% of in-silico tools; these filters prioritize candidates but do not establish pathogenicity. (srivastava2019wholegenomesequencing pages 5-7, srivastava2019wholegenomesequencing pages 2-5)

No robust disease-wide carrier frequency can be calculated because there is no single causal allele. Population frequency must be reported variant by variant using ancestry-matched gnomAD/TOPMed data at the time of clinical interpretation.

### Environmental, lifestyle, and infectious factors

Family history is the defining risk factor. First-degree relatives have approximately 3-fold risk in a Swedish database analysis, 5.2–5.47-fold risk in another synthesis, and 8–10-fold risk in selected familial analyses; differences reflect case definitions, populations, and ascertainment. More than 90% of familial clusters contain only two affected members. (capezzone2021familialnonmedullarythyroid pages 2-4, capezzone2021familialnonmedullarythyroid pages 1-2, kamani2022geneticsusceptibilityto pages 1-2)

Ionizing radiation, especially childhood neck exposure, is an established risk factor for thyroid carcinoma generally and must be excluded as a shared explanation when classifying a nonsyndromic kindred. No FNMTC-specific quantitative gene–radiation interaction is established. Sex, age, iodine nutrition, obesity, and benign thyroid disease may alter background NMTC risk, but current evidence does not establish them as specific causes of familial clustering. There is no infectious cause and no demonstrated vaccine-preventable trigger. (sanchezares2022susceptibilitygenesand pages 1-2)

### Protective factors and gene–environment interaction

No reproducible protective germline variant, diet, medication, or lifestyle intervention specifically prevents FNMTC. Avoiding unnecessary ionizing radiation is prudent general prevention, but does not eliminate inherited susceptibility. Evidence is insufficient to quantify specific gene–environment interactions. This is a major knowledge gap rather than evidence of no interaction.

## 3. Phenotypes

FNMTC can be asymptomatic until a nodule is detected. The clinical phenotype is otherwise that of differentiated thyroid carcinoma.

* **Thyroid nodule/mass:** clinical sign or imaging finding; often insidious and painless. Benign nodules, follicular adenoma, and multinodular goiter commonly coexist. Suggested HPO: *Thyroid nodule*, *Multinodular goiter*. (NCT01109420 chunk 1, sanchezares2022susceptibilitygenesand pages 1-2)
* **Papillary thyroid carcinoma:** malignant pathologic phenotype, usually classic or follicular variant; >85% of NMTC and 85–91% of familial tumors in summarized series. Suggested HPO: *Thyroid carcinoma*. (yang2016familialnonmedullarythyroid pages 1-2, kamani2022geneticsusceptibilityto pages 1-2)
* **Multifocal/bilateral carcinoma:** pathologic sign, variably frequent and often cited as enriched in familial tumors. In one 43-patient familial series, 56% were multifocal. Suggested HPO: *Multifocal neoplasm*; bilateral thyroid involvement should be separately annotated. (capezzone2021familialnonmedullarythyroid pages 6-7, cirello2021clinicalandgenetic pages 3-4)
* **Extrathyroidal extension:** locally invasive sign; 35% in the same series. Severity ranges from microscopic extension to invasion of neck structures. (cirello2021clinicalandgenetic pages 3-4)
* **Cervical lymph-node metastasis:** regional metastatic sign; 26% in the Italian series. Suggested HPO: *Lymph node metastasis*. (cirello2021clinicalandgenetic pages 3-4)
* **Distant/lung metastasis:** advanced manifestation; lung metastases occurred in 7% of that series. Suggested HPO: *Pulmonary metastasis*. (cirello2021clinicalandgenetic pages 3-4)
* **Hashimoto thyroiditis association:** reported more often in some familial pathology series, but its causal role and frequency are uncertain. (sanchezares2022susceptibilitygenesand pages 1-2)

Age and severity are variable. One clinical cohort had median diagnosis at 44 years, range 8–81 years. Reviews report younger presentation and possible anticipation, but ascertainment and intensified surveillance can produce apparent anticipation. (cirello2021clinicalandgenetic pages 3-4, kamani2022geneticsusceptibilityto pages 2-4)

Quality-of-life effects are primarily those of thyroid cancer and treatment: fear of recurrence, repeated neck imaging and laboratory surveillance, lifelong levothyroxine after total thyroidectomy, and possible hypoparathyroidism, voice impairment, or treatment-related fatigue. Retrieved evidence did not provide validated FNMTC-specific EQ-5D, SF-36, or PROMIS estimates; extrapolation from sporadic differentiated thyroid cancer should be labeled indirect.

## 4. Genetic and molecular information

### Inheritance, penetrance, and expressivity

Nonsyndromic families often appear autosomal dominant, but with incomplete, age-dependent penetrance and marked variable expressivity; polygenic inheritance remains plausible. There is no established role for recessive inheritance, mitochondrial transmission, repeat expansion, germline mosaicism, or consanguinity in typical FNMTC. Founder effects may exist for individual variants but are not a general feature. (capezzone2021familialnonmedullarythyroid pages 2-4, capezzone2021familialnonmedullarythyroid pages 4-5)

Clinical anticipation has been reported, with second generations presenting younger and sometimes more severely. It is not proven to represent a repeat-expansion mechanism; surveillance bias and changing diagnostic intensity are important alternatives. (yang2016familialnonmedullarythyroid pages 1-2, kamani2022geneticsusceptibilityto pages 2-4)

### Epigenetic and telomere findings

Shorter telomere length and imbalance of the telomere–telomerase system have been reported in familial cases and may modify susceptibility. Differential activity of miR-886-3p and miR-20a has also been proposed. These remain research biomarkers, not validated diagnostic tests. No reproducible FNMTC-specific methylation or histone-modification signature is ready for clinical use. (capezzone2021familialnonmedullarythyroid pages 4-5, cirello2021clinicalandgenetic pages 2-3, yang2016familialnonmedullarythyroid pages 13-14)

### Chromosomal abnormalities

Historical linkage regions are susceptibility intervals, not recurrent diagnostic structural variants. Tumor translocations such as RET/PTC and NTRK fusions can occur somatically. Routine constitutional karyotyping, FISH, or chromosomal microarray has low expected yield in isolated FNMTC unless additional congenital or syndromic features suggest a chromosome disorder. (yang2016familialnonmedullarythyroid pages 1-2, cirello2021clinicalandgenetic pages 3-4)

## 5. Environmental information

No toxin, occupational exposure, lifestyle pattern, or pathogen uniquely defines FNMTC. Shared radiation exposure must be considered in clustered families. Smoking and alcohol are not established FNMTC-specific factors; thyroid-cancer associations with body mass, diet, iodine status, and endocrine-disrupting chemicals remain general epidemiologic issues, not demonstrated explanations for familial transmission. Environmental annotations should therefore be represented as general thyroid-cancer modifiers with low disease specificity, not as confirmed FNMTC causes.

## 6. Mechanism and pathophysiology

### Causal chain

A defensible current model is:

**Inherited susceptibility**—a high-penetrance syndromic defect or a family-specific combination of rare and common alleles—**→ altered genome maintenance, developmental transcription, growth-factor signaling, telomere biology, or miRNA regulation → increased probability of acquiring somatic thyroid drivers → constitutive MAPK/ERK and/or PI3K/AKT signaling in thyroid follicular cells → proliferation, survival, clonal expansion, papillary/follicular carcinoma → multifocal local growth, cervical nodal spread, and occasionally distant metastasis.** (srivastava2019wholegenomesequencing pages 5-7, srivastava2019wholegenomesequencing pages 19-21, sanchezares2022susceptibilitygenesand pages 1-2)

Upstream mechanisms depend on the syndrome: PTEN loss releases PI3K–AKT signaling; APC disruption alters Wnt/β-catenin regulation; DICER1 defects impair miRNA processing; PRKAR1A defects dysregulate cAMP–PKA signaling; WRN loss impairs DNA repair and genome stability. In nonsyndromic disease, pathway convergence is clearer than any shared initiating gene.

### Genomic and molecular profiling

WGS of 23 affected and three unaffected individuals from five families reduced 91,427–207,873 raw variants per family to 31 prioritized coding and 39 regulatory-region candidates. Among 210 pathway-mappable genes, receptor-tyrosine-kinase and GPCR networks converged on MAPK/ERK and PI3K/AKT; AKT and ERK1/2 were network hubs. Thyroid cancer enrichment was statistically significant but ranked below many broad cancer functions, underscoring that pathway analysis is hypothesis-generating. (srivastava2019wholegenomesequencing pages 5-7, srivastava2019wholegenomesequencing pages 2-5, srivastava2019wholegenomesequencing pages 16-19, srivastava2019wholegenomesequencing pages 19-21)

Tumor profiling in a familial series assayed **BRAF V600E, RAS, AKT1, PIK3CA, EIF1AX, TERT-promoter** hotspots and **RET/PTC/NTRK** fusions. Familial and sporadic NMTC share morphology and somatic drivers; currently, the same molecularly matched therapies apply. (cirello2021clinicalandgenetic pages 3-4, sanchezares2022susceptibilitygenesand pages 1-2)

No validated FNMTC-specific transcriptomic, proteomic, metabolomic, lipidomic, single-cell, spatial-transcriptomic, or integrated multi-omic signature was identified. These technologies are active in thyroid-cancer research, but familial status has not yet yielded a reproducible clinical classifier.

### Ontology suggestions

* **Cell type:** thyroid follicular cell, **CL:0000501**.
* **Anatomy:** thyroid gland, **UBERON:0002046**; cervical lymph nodes and lung for metastatic sites.
* **Processes:** MAPK cascade, **GO:0000165**; cell population proliferation, **GO:0008283**; PI3K–AKT signaling, DNA-damage response, miRNA processing, telomere maintenance, apoptotic signaling, and cell migration.
* **Subcellular sites:** nucleus for transcription/DNA repair/telomeres; plasma membrane and cytosol for RTK–RAS–MAPK and PI3K–AKT signaling; no FNMTC-specific organelle lesion is established.

## 7. Anatomical structures affected

The primary organ is the **thyroid gland**, specifically follicular epithelium rather than calcitonin-producing parafollicular C cells. Tumors may be unilateral or bilateral and unifocal or multifocal. Regional disease involves the central and lateral cervical lymph nodes; advanced disease may affect lung, bone, or other distant sites. The endocrine system is primary; respiratory, skeletal, and neurologic systems are involved only through local invasion, metastasis, or treatment complications. (capezzone2021familialnonmedullarythyroid pages 6-7, cirello2021clinicalandgenetic pages 3-4)

At the tissue level, affected structures include thyroid follicles, papillary tumor epithelium, tumor stroma, lymphatic vessels, and metastatic lymph-node parenchyma. Relevant GO cellular compartments include nucleus, chromosome/telomere, cytoplasm, plasma membrane, and receptor-signaling complexes.

## 8. Temporal development

Onset is typically insidious and adult, but pediatric and geriatric presentations occur; the documented 8–81-year range demonstrates marked age variability. Earlier onset should increase suspicion of inherited susceptibility, particularly with multicentricity or bilaterality. (capezzone2021familialnonmedullarythyroid pages 6-7, cirello2021clinicalandgenetic pages 3-4)

Course follows differentiated thyroid-cancer staging rather than a separate FNMTC staging system: localized intrathyroidal tumor → regional nodal disease → locally invasive or distant metastatic disease. Many PTCs are indolent, although familial cohorts can show more adverse features at diagnosis. Treatment-induced remission is common; biochemical or structural persistence/recurrence can occur. No credible spontaneous-remission pattern is established.

The critical intervention window is before clinically consequential nodal or distant spread, but overdiagnosis of indolent microcarcinoma is a countervailing harm. That balance explains disagreement over ultrasound screening.

## 9. Inheritance and population

FNMTC accounts for approximately **3–9%, nearly 10%, or 5–15%** of thyroid/NMTC cases across reviews; variation reflects definition and denominator. Syndromic cases account for about **5% of familial disease**, leaving approximately 95% classified as nonsyndromic. FNMTC-specific incidence per 100,000 is not reliably established. (yang2016familialnonmedullarythyroid pages 1-2, capezzone2021familialnonmedullarythyroid pages 1-2, kamani2022geneticsusceptibilityto pages 1-2)

Women predominate, as in sporadic differentiated thyroid cancer. In one familial clinical series, 38/43 patients (88%) were female and five male. This does not establish a universal sex ratio because of referral and family ascertainment. (cirello2021clinicalandgenetic pages 3-4)

No ethnicity is uniquely affected. GWAS effect sizes and rare-variant frequencies differ by ancestry, making ancestry-matched controls essential. No general carrier frequency is meaningful for a genetically heterogeneous trait.

## 10. Diagnostics

### Clinical evaluation

Diagnosis begins with a three-generation pedigree, pathology confirmation in affected relatives, assessment of radiation exposure, and examination for syndromic features. Neck ultrasonography characterizes thyroid nodules and cervical lymph nodes. Suspicious nodules undergo ultrasound-guided fine-needle aspiration; cytology is classified using standard thyroid systems, with molecular testing used for indeterminate nodules where clinically appropriate. Serum TSH guides nodule evaluation but neither TSH nor thyroglobulin diagnoses FNMTC. Post-treatment thyroglobulin and anti-thyroglobulin antibodies are surveillance biomarkers.

Histopathology establishes papillary, follicular, or oncocytic carcinoma and documents multifocality, bilaterality, vascular/capsular invasion, extrathyroidal extension, margins, and nodal status. FNMTC and sporadic tumors cannot usually be distinguished morphologically or by common somatic mutations alone. (cirello2021clinicalandgenetic pages 3-4, sanchezares2022susceptibilitygenesand pages 1-2)

### Genetic testing strategy

1. **If syndromic features are present:** use phenotype-directed germline testing—e.g., **APC, PTEN, DICER1, PRKAR1A, WRN**—with deletion/duplication analysis where appropriate. A multigene hereditary-cancer panel can be efficient when phenotypes overlap. (yang2016familialnonmedullarythyroid pages 2-4, sanchezares2022susceptibilitygenesand pages 1-2)
2. **If apparently isolated nonsyndromic FNMTC:** pre-test counseling should explain that no validated routine predictive panel explains most families. WES/WGS is most appropriate in research or carefully selected ≥3-case families, ideally sequencing multiple affected and unaffected relatives with segregation analysis. (yang2016familialnonmedullarythyroid pages 13-14, srivastava2019wholegenomesequencing pages 2-5, kamani2022geneticsusceptibilityto pages 14-15)
3. **CMA, karyotype, FISH, mitochondrial sequencing, and repeat-expansion testing:** not routine unless another phenotype supplies an independent indication.
4. **Tumor sequencing/liquid biopsy:** useful for therapy selection in advanced disease, not for proving familial causation. A tumor variant requires matched normal testing before it can be called germline.

### Clinical criteria and differential diagnosis

Two first-degree relatives meet the conventional definition, but three affected relatives provide much greater specificity. Differential diagnoses include sporadic coincidental PTC; medullary thyroid carcinoma/MEN2; radiation-associated thyroid cancer; metastasis to thyroid; and syndromic NMTC due to PTEN, APC, DICER1, PRKAR1A, WRN, or other cancer syndromes. (yang2016familialnonmedullarythyroid pages 13-14, sanchezares2022susceptibilitygenesand pages 1-2)

## 11. Outcomes and prognosis

Whether FNMTC is intrinsically more aggressive remains unresolved. Some studies report younger age, larger or multifocal tumors, more extrathyroidal extension, nodal metastases, recurrence, and reduced survival; matched studies find little difference. The Italian series found a significantly more aggressive presentation but **not a worse outcome** after appropriate treatment. Reviews likewise report no consistent mortality or recurrence difference. (yang2016familialnonmedullarythyroid pages 1-2, capezzone2021familialnonmedullarythyroid pages 1-2, cirello2021clinicalandgenetic pages 1-2, kamani2022geneticsusceptibilityto pages 1-2)

Accordingly, no reliable FNMTC-specific 5- or 10-year survival estimate can be supplied from the retrieved evidence. Prognosis should use standard differentiated-thyroid-cancer variables: age, histologic subtype, tumor size, gross extrathyroidal extension, completeness of resection, nodal burden, distant metastasis, radioiodine avidity, thyroglobulin response, and actionable somatic genotype. Family history alone is not a validated basis for assigning a worse stage.

Long-term morbidity is more commonly treatment-related or surveillance-related than disabling tumor burden: hypothyroidism, hypoparathyroidism, recurrent-laryngeal-nerve injury, neck discomfort, salivary effects from radioiodine, anxiety, and financial/psychosocial burden. FNMTC-specific disability and quality-of-life statistics remain insufficient.

## 12. Treatment and applications

FNMTC is treated according to standard differentiated thyroid-cancer risk stratification. Current ATA-aligned reviews do not recommend a different therapeutic approach solely because of family history. (capezzone2021familialnonmedullarythyroid pages 6-7)

* **Surgery:** lobectomy or total thyroidectomy according to tumor size, bilaterality/multifocality, nodal disease, molecular/pathologic risk, and patient preference; therapeutic compartment-oriented neck dissection for proven nodal metastases. In one referral series, 93% underwent total thyroidectomy, but this is not evidence that all FNMTC requires total thyroidectomy. Suggested NCIT: *Thyroidectomy*, *Lobectomy*, *Neck Dissection*. (cirello2021clinicalandgenetic pages 3-4)
* **Radioactive iodine (I-131):** selected after surgery according to recurrence risk and radioiodine avidity, not automatically for familial status. Suggested NCIT: *Radioactive Iodine Therapy*; CHEBI annotation should use the curated iodide/I-131 entity.
* **Levothyroxine/TSH suppression:** replacement after total thyroidectomy and risk-adapted TSH suppression. Suggested NCIT: *Thyroid Hormone Replacement Therapy*, *TSH Suppression Therapy*.
* **Advanced radioiodine-refractory disease:** molecularly selected kinase inhibition follows ordinary DTC practice—RET or NTRK inhibitors for corresponding fusions, BRAF/MEK-directed approaches in appropriate BRAF-altered disease, and multikinase inhibitors for progressive refractory disease. Familial and sporadic tumors currently share these therapeutic rules because their somatic drivers overlap. Suggested NCIT: *Kinase Inhibitor Therapy*, *Targeted Therapy*. (sanchezares2022susceptibilitygenesand pages 1-2)
* **Immunotherapy, gene therapy, cell therapy, RNA therapy, or prophylactic thyroidectomy:** no FNMTC-specific approved indication. Prophylactic thyroidectomy is not recommended for nonsyndromic FNMTC in the manner used for RET-positive MEN2.

There is no established FNMTC pharmacogenomic rule. Somatic genotype guides targeted efficacy; germline findings primarily guide syndrome surveillance rather than drug metabolism.

## 13. Prevention and screening

### Primary prevention

No intervention can remove inherited susceptibility. Avoid unnecessary childhood neck radiation and manage general health risks, but no diet, vaccine, supplement, or prophylactic drug has demonstrated FNMTC prevention.

### Secondary prevention

Routine population ultrasound screening is not recommended. Universal ultrasound screening of all relatives is also controversial: one prospective study found thyroid cancer in **4.6%** of screened at-risk relatives from two-case families, approximately comparable to detection in heavily imaged populations. Major reviews report that ATA, NCCN, and ESMO have not endorsed routine genetic screening of nonsyndromic relatives because evidence is insufficient. (capezzone2021familialnonmedullarythyroid pages 4-5, kamani2022geneticsusceptibilityto pages 2-4, kamani2022geneticsusceptibilityto pages 14-15)

A reasonable expert approach is individualized counseling and clinical neck examination, with lower threshold for ultrasound in families with ≥3 affected members, unusually young onset, aggressive disease, palpable abnormalities, or a known syndrome. Families with only two older-onset micro-PTCs carry substantial risk of coincidental clustering and overdiagnosis. (yang2016familialnonmedullarythyroid pages 13-14, capezzone2021familialnonmedullarythyroid pages 6-7)

### Real-world implementation

The NIDDK prospective observational cohort **NCT01109420, “Clinical and Genetic Studies in Familial Non-medullary Thyroid Cancer,”** began August 12, 2010 and was listed as recruiting with estimated enrollment of 500. It accepts affected families and unaffected relatives, performs family history, examination, laboratory testing and imaging, and annually re-screens unaffected participants without malignant tumors. Objectives include defining natural history, optimizing screening, and identifying susceptibility genes. ClinicalTrials.gov: [NCT01109420](https://clinicaltrials.gov/study/NCT01109420). (NCT01109420 chunk 1)

### Tertiary prevention and counseling

Risk-adapted postoperative surveillance, thyroglobulin monitoring, cervical ultrasound, appropriate radioiodine use, and treatment of persistent/recurrent disease prevent complications. Genetic counseling should address uncertain penetrance, limitations of negative testing, possible incidental findings, and syndrome-specific cancer surveillance. Reproductive testing or preimplantation genetic testing is technically meaningful only when a clearly pathogenic germline variant has been established; it is not appropriate for an unvalidated candidate allele.

## 14. Other species and natural disease

Spontaneous follicular-cell-derived thyroid tumors occur in companion and laboratory animals, but the retrieved literature did not establish a naturally occurring veterinary syndrome orthologous to human nonsyndromic FNMTC. There is no zoonotic transmission. Human susceptibility genes have conserved orthologs in mouse and other vertebrates, but conservation of a pathway does not establish a homologous familial disease.

Suggested taxonomy annotations for general comparative research include *Homo sapiens* (NCBI Taxon 9606), *Mus musculus* (10090), *Rattus norvegicus* (10116), and *Danio rerio* (7955). Breed-specific VBO annotations are not supported for FNMTC.

## 15. Model organisms

No single model faithfully reproduces genetically heterogeneous nonsyndromic FNMTC. Available thyroid-cancer models instead interrogate downstream mechanisms:

* genetically engineered mice expressing thyroid-specific **BRAF V600E**, **RET/PTC**, **RAS**, or altered **PTEN/PI3K** signaling;
* thyroid cancer cell lines and patient-derived cultures/organoids;
* xenograft or patient-derived xenograft models;
* CRISPR knock-in/knockout systems for candidate variants;
* zebrafish models for thyroid development and oncogenic signaling.

These models can reproduce follicular-cell transformation and MAPK/PI3K pathway activation, but generally model a somatic driver or one syndrome—not the incomplete penetrance, polygenic architecture, and within-family variability of human FNMTC. The most informative future design would combine a segregating human germline variant with a thyroid-specific somatic driver and longitudinal assessment of penetrance.

## Recent developments and evidence limitations

The requested 2023–2024 priority yielded limited directly retrievable primary literature. A 2024 report proposed **PAK4** as a susceptibility gene (DOI [10.1089/thy.2023.0564](https://doi.org/10.1089/thy.2023.0564)), but full evidence was unavailable in the retrieved corpus; it should therefore be treated as emerging, not yet independently validated, and not assigned as an established causal gene. The strongest accessible contemporary syntheses were published in 2021–2022, while the ongoing NIH cohort supplies current implementation data.

Three overarching limitations should be retained in the knowledge base: (1) two-case families are contaminated by coincidental sporadic PTC; (2) many candidate-gene reports are single-family or underpowered and lack replication; and (3) screening changes apparent age, tumor size, and aggressiveness. Consequently, reported anticipation, penetrance, and familial–sporadic outcome differences should be annotated with ascertainment-bias qualifiers.

## Key sources and direct abstract quotations

* Capezzone et al., *Journal of Endocrinological Investigation*, published online October 2020/volume 2021, DOI [10.1007/s40618-020-01435-x](https://doi.org/10.1007/s40618-020-01435-x): **“FNMTC is described as a polygenic disorder associated with multiple low- to moderate-penetrance susceptibility genes and incomplete penetrance.”** (capezzone2021familialnonmedullarythyroid pages 1-2)
* Cirello et al., *Frontiers in Endocrinology*, January 2021, DOI [10.3389/fendo.2020.589340](https://doi.org/10.3389/fendo.2020.589340): **“Familial tumors had a statistically significant more aggressive presentation at diagnosis, though not resulting in a worst outcome.”** (cirello2021clinicalandgenetic pages 1-2)
* Sánchez-Ares et al., *Frontiers in Endocrinology*, February 2022, DOI [10.3389/fendo.2022.829103](https://doi.org/10.3389/fendo.2022.829103): **“Non-syndromic familial non-medullary carcinoma has a complex and heterogeneous genetic basis involving several genes and loci with a monogenic or polygenic inheritance model.”** (sanchezares2022susceptibilitygenesand pages 1-2)
* Kamani et al., *Hereditary Cancer in Clinical Practice*, March 2022, DOI [10.1186/s13053-022-00215-3](https://doi.org/10.1186/s13053-022-00215-3): **“The gene(s) responsible for the vast majority of non-syndromic FNMTC cases are yet to be identified.”** (kamani2022geneticsusceptibilityto pages 1-2)

PMIDs were not exposed in the retrieved full-text metadata and therefore are not fabricated here. DOI links provide stable source resolution. The evidence base supports robust disease-level characterization, but not definitive assignment of most nonsyndromic candidate genes as pathogenic.

References

1. (yang2016familialnonmedullarythyroid pages 13-14): Samantha Peiling Yang and Joanne Ngeow. Familial non-medullary thyroid cancer: unraveling the genetic maze. Endocrine-related cancer, 23 12:R577-R595, Dec 2016. URL: https://doi.org/10.1530/erc-16-0067, doi:10.1530/erc-16-0067. This article has 140 citations and is from a domain leading peer-reviewed journal.

2. (sanchezares2022susceptibilitygenesand pages 1-2): María Sánchez-Ares, Soledad Cameselle-García, Ihab Abdulkader-Nallib, Gemma Rodríguez-Carnero, Carolina Beiras-Sarasquete, José Antonio Puñal-Rodríguez, and José Manuel Cameselle-Teijeiro. Susceptibility genes and chromosomal regions associated with non-syndromic familial non-medullary thyroid carcinoma: some pathogenetic and diagnostic keys. Frontiers in Endocrinology, Feb 2022. URL: https://doi.org/10.3389/fendo.2022.829103, doi:10.3389/fendo.2022.829103. This article has 19 citations.

3. (kamani2022geneticsusceptibilityto pages 1-2): Tina Kamani, Parsa Charkhchi, Afshan Zahedi, and Mohammad R. Akbari. Genetic susceptibility to hereditary non-medullary thyroid cancer. Hereditary Cancer in Clinical Practice, Mar 2022. URL: https://doi.org/10.1186/s13053-022-00215-3, doi:10.1186/s13053-022-00215-3. This article has 37 citations and is from a peer-reviewed journal.

4. (capezzone2021familialnonmedullarythyroid pages 2-4): M. Capezzone, E. Robenshtok, E. Robenshtok, S. Cantara, and M. G. Castagna. Familial non-medullary thyroid cancer: a critical review. Journal of Endocrinological Investigation, 44:943-950, Oct 2021. URL: https://doi.org/10.1007/s40618-020-01435-x, doi:10.1007/s40618-020-01435-x. This article has 81 citations and is from a peer-reviewed journal.

5. (capezzone2021familialnonmedullarythyroid pages 4-5): M. Capezzone, E. Robenshtok, E. Robenshtok, S. Cantara, and M. G. Castagna. Familial non-medullary thyroid cancer: a critical review. Journal of Endocrinological Investigation, 44:943-950, Oct 2021. URL: https://doi.org/10.1007/s40618-020-01435-x, doi:10.1007/s40618-020-01435-x. This article has 81 citations and is from a peer-reviewed journal.

6. (kamani2022geneticsusceptibilityto pages 11-12): Tina Kamani, Parsa Charkhchi, Afshan Zahedi, and Mohammad R. Akbari. Genetic susceptibility to hereditary non-medullary thyroid cancer. Hereditary Cancer in Clinical Practice, Mar 2022. URL: https://doi.org/10.1186/s13053-022-00215-3, doi:10.1186/s13053-022-00215-3. This article has 37 citations and is from a peer-reviewed journal.

7. (yang2016familialnonmedullarythyroid pages 1-2): Samantha Peiling Yang and Joanne Ngeow. Familial non-medullary thyroid cancer: unraveling the genetic maze. Endocrine-related cancer, 23 12:R577-R595, Dec 2016. URL: https://doi.org/10.1530/erc-16-0067, doi:10.1530/erc-16-0067. This article has 140 citations and is from a domain leading peer-reviewed journal.

8. (capezzone2021familialnonmedullarythyroid pages 1-2): M. Capezzone, E. Robenshtok, E. Robenshtok, S. Cantara, and M. G. Castagna. Familial non-medullary thyroid cancer: a critical review. Journal of Endocrinological Investigation, 44:943-950, Oct 2021. URL: https://doi.org/10.1007/s40618-020-01435-x, doi:10.1007/s40618-020-01435-x. This article has 81 citations and is from a peer-reviewed journal.

9. (NCT01109420 chunk 1):  Clinical and Genetic Studies in Familial Non-medullary Thyroid Cancer. National Institute of Diabetes and Digestive and Kidney Diseases (NIDDK). 2010. ClinicalTrials.gov Identifier: NCT01109420

10. (cirello2021clinicalandgenetic pages 3-4): Valentina Cirello, Carla Colombo, Olga Karapanou, Gabriele Pogliaghi, Luca Persani, and Laura Fugazzola. Clinical and genetic features of a large monocentric series of familial non-medullary thyroid cancers. Frontiers in Endocrinology, Jan 2021. URL: https://doi.org/10.3389/fendo.2020.589340, doi:10.3389/fendo.2020.589340. This article has 10 citations.

11. (cirello2021clinicalandgenetic pages 1-2): Valentina Cirello, Carla Colombo, Olga Karapanou, Gabriele Pogliaghi, Luca Persani, and Laura Fugazzola. Clinical and genetic features of a large monocentric series of familial non-medullary thyroid cancers. Frontiers in Endocrinology, Jan 2021. URL: https://doi.org/10.3389/fendo.2020.589340, doi:10.3389/fendo.2020.589340. This article has 10 citations.

12. (srivastava2019wholegenomesequencing pages 5-7): Aayushi Srivastava, Abhishek Kumar, Sara Giangiobbe, Elena Bonora, Kari Hemminki, Asta Försti, and Obul Reddy Bandapalli. Whole genome sequencing of familial non-medullary thyroid cancer identifies germline alterations in mapk/erk and pi3k/akt signaling pathways. ArXiv, Oct 2019. URL: https://doi.org/10.20944/preprints201910.0154.v1, doi:10.20944/preprints201910.0154.v1. This article has 34 citations.

13. (srivastava2019wholegenomesequencing pages 19-21): Aayushi Srivastava, Abhishek Kumar, Sara Giangiobbe, Elena Bonora, Kari Hemminki, Asta Försti, and Obul Reddy Bandapalli. Whole genome sequencing of familial non-medullary thyroid cancer identifies germline alterations in mapk/erk and pi3k/akt signaling pathways. ArXiv, Oct 2019. URL: https://doi.org/10.20944/preprints201910.0154.v1, doi:10.20944/preprints201910.0154.v1. This article has 34 citations.

14. (yang2016familialnonmedullarythyroid pages 2-4): Samantha Peiling Yang and Joanne Ngeow. Familial non-medullary thyroid cancer: unraveling the genetic maze. Endocrine-related cancer, 23 12:R577-R595, Dec 2016. URL: https://doi.org/10.1530/erc-16-0067, doi:10.1530/erc-16-0067. This article has 140 citations and is from a domain leading peer-reviewed journal.

15. (capezzone2021familialnonmedullarythyroid pages 6-7): M. Capezzone, E. Robenshtok, E. Robenshtok, S. Cantara, and M. G. Castagna. Familial non-medullary thyroid cancer: a critical review. Journal of Endocrinological Investigation, 44:943-950, Oct 2021. URL: https://doi.org/10.1007/s40618-020-01435-x, doi:10.1007/s40618-020-01435-x. This article has 81 citations and is from a peer-reviewed journal.

16. (kamani2022geneticsusceptibilityto pages 14-15): Tina Kamani, Parsa Charkhchi, Afshan Zahedi, and Mohammad R. Akbari. Genetic susceptibility to hereditary non-medullary thyroid cancer. Hereditary Cancer in Clinical Practice, Mar 2022. URL: https://doi.org/10.1186/s13053-022-00215-3, doi:10.1186/s13053-022-00215-3. This article has 37 citations and is from a peer-reviewed journal.

17. (srivastava2019wholegenomesequencing pages 2-5): Aayushi Srivastava, Abhishek Kumar, Sara Giangiobbe, Elena Bonora, Kari Hemminki, Asta Försti, and Obul Reddy Bandapalli. Whole genome sequencing of familial non-medullary thyroid cancer identifies germline alterations in mapk/erk and pi3k/akt signaling pathways. ArXiv, Oct 2019. URL: https://doi.org/10.20944/preprints201910.0154.v1, doi:10.20944/preprints201910.0154.v1. This article has 34 citations.

18. (cirello2021clinicalandgenetic pages 2-3): Valentina Cirello, Carla Colombo, Olga Karapanou, Gabriele Pogliaghi, Luca Persani, and Laura Fugazzola. Clinical and genetic features of a large monocentric series of familial non-medullary thyroid cancers. Frontiers in Endocrinology, Jan 2021. URL: https://doi.org/10.3389/fendo.2020.589340, doi:10.3389/fendo.2020.589340. This article has 10 citations.

19. (kamani2022geneticsusceptibilityto pages 15-16): Tina Kamani, Parsa Charkhchi, Afshan Zahedi, and Mohammad R. Akbari. Genetic susceptibility to hereditary non-medullary thyroid cancer. Hereditary Cancer in Clinical Practice, Mar 2022. URL: https://doi.org/10.1186/s13053-022-00215-3, doi:10.1186/s13053-022-00215-3. This article has 37 citations and is from a peer-reviewed journal.

20. (kamani2022geneticsusceptibilityto pages 2-4): Tina Kamani, Parsa Charkhchi, Afshan Zahedi, and Mohammad R. Akbari. Genetic susceptibility to hereditary non-medullary thyroid cancer. Hereditary Cancer in Clinical Practice, Mar 2022. URL: https://doi.org/10.1186/s13053-022-00215-3, doi:10.1186/s13053-022-00215-3. This article has 37 citations and is from a peer-reviewed journal.

21. (srivastava2019wholegenomesequencing pages 16-19): Aayushi Srivastava, Abhishek Kumar, Sara Giangiobbe, Elena Bonora, Kari Hemminki, Asta Försti, and Obul Reddy Bandapalli. Whole genome sequencing of familial non-medullary thyroid cancer identifies germline alterations in mapk/erk and pi3k/akt signaling pathways. ArXiv, Oct 2019. URL: https://doi.org/10.20944/preprints201910.0154.v1, doi:10.20944/preprints201910.0154.v1. This article has 34 citations.

## Artifacts

- [Edison artifact artifact-00](Familial_Nonmedullary_Thyroid_Carcinoma-deep-research-falcon_artifacts/artifact-00.md)