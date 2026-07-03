---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-22T10:37:51.374247'
end_time: '2026-06-22T10:53:15.006787'
duration_seconds: 923.63
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Mucoepidermoid Carcinoma
  mondo_id: ''
  category: Cancer
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 24
artifact_count: 2
artifact_sources:
  edison_answer_artifacts: 2
artifacts:
- filename: artifact-00.md
  path: Mucoepidermoid_Carcinoma-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: Mucoepidermoid_Carcinoma-deep-research-falcon_artifacts/artifact-01.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-01
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Mucoepidermoid Carcinoma
- **MONDO ID:**  (if available)
- **Category:** Cancer

## Research Objectives

Please provide a comprehensive research report on **Mucoepidermoid Carcinoma** covering all of the
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
- **Disease Name:** Mucoepidermoid Carcinoma
- **MONDO ID:**  (if available)
- **Category:** Cancer

## Research Objectives

Please provide a comprehensive research report on **Mucoepidermoid Carcinoma** covering all of the
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


# Comprehensive Research Report: Mucoepidermoid Carcinoma (MEC)

## 1. DISEASE INFORMATION

### Overview
Mucoepidermoid carcinoma (MEC) is the most common malignant tumor of the salivary glands, accounting for approximately 30-40% of all malignant salivary gland tumors and 10-15% of all salivary gland neoplasms (costa2024molecularaspectsof pages 1-3, wang2024theclinicaloutcome pages 1-2). MEC is a highly heterogeneous neoplasm characterized by the presence of three distinct cell types: mucin-secreting cells, epidermoid (squamous) cells, and cells of intermediate type, with varying architectural formations from cystic structures to solid nests or glandular-like structures (chen2021thecrtc1maml2fusion pages 1-2, costa2024molecularaspectsof pages 1-3).

### Key Identifiers
While specific OMIM, Orphanet, and MONDO identifiers were not explicitly stated in the retrieved literature, MEC is recognized in standard medical nomenclature and classification systems. The disease is classified within the WHO classification of salivary gland tumors (costa2024molecularaspectsof pages 1-3, broseghini2025salivaryglandcancers pages 1-2).

### Synonyms and Alternative Names
The literature consistently refers to this entity as "mucoepidermoid carcinoma" or "MEC." The term "mucoepidermoid" derives from the characteristic cellular composition of the tumor.

### Data Source
The information is derived from both individual patient cohorts and aggregated disease-level resources, including large retrospective studies (e.g., 454-case cohort), genomic profiling databases (118 advanced MEC cases), and molecular characterization studies (wang2024theclinicaloutcome pages 1-2, zerdan2023moleculartargetsin pages 1-2).

---

## 2. ETIOLOGY

### Disease Causal Factors

**Genetic Factors:**
The t(11;19)(q14-21;p12-13) chromosomal translocation resulting in the CRTC1-MAML2 fusion gene is detected in up to 80% of MEC cases and represents a core pathogenic event (chen2021thecrtc1maml2fusion pages 1-2, wang2024theclinicaloutcome pages 1-2). A CRTC1-MAML2 conditional transgenic mouse model produced salivary gland tumors with 100% penetrance that resembled histological and molecular characteristics of human MEC, providing direct evidence that CRTC1-MAML2 is a major oncogenic driver for MEC development and maintenance (chen2021thecrtc1maml2fusion pages 1-2).

Alternative CRTC3-MAML2 fusions occur in up to 6% of cases and are mutually exclusive with CRTC1-MAML2 (chen2021thecrtc1maml2fusion pages 1-2). The t(11;19) translocation is occasionally the sole cytogenetic alteration in MEC salivary gland tumors, suggesting that the acquired CRTC1-MAML2 fusion is an early core event in MEC pathogenesis (chen2021thecrtc1maml2fusion pages 1-2).

**Mechanistic Insights:**
In the CRTC1-MAML2 fusion, the NOTCH-binding domain of MAML2 is replaced by the CREB-binding domain of CRTC1, resulting in disruption of NOTCH signaling and activation of cAMP-responsive target genes (chen2021thecrtc1maml2fusion pages 1-2). Molecular analysis of MEC tumors revealed altered p16-CDK4/6-RB pathway activity as a potential cooperating event in promoting CRTC1-MAML2-induced tumorigenesis (chen2021thecrtc1maml2fusion pages 1-2).

### Risk Factors

**Genetic Risk Factors:**
Specific germline mutations associated with MEC susceptibility are rare. In one genomic study, pathogenic germline mutations in SPINK1 (2%) and FANCG (2%) were identified, which are involved in cancer susceptibility, though their specific contribution to MEC predisposition remains uncertain (wang2024theclinicaloutcome pages 2-3).

**Environmental Risk Factors:**
The literature reviewed did not identify strong environmental risk factors specific to MEC. In one cohort of 454 patients, 95% were nonsmokers and only 5% had a smoking history, suggesting smoking is not a major risk factor (wang2024theclinicaloutcome pages 1-2). Age and anatomic site appear to influence risk: MECs predominantly occurred in females (58% vs 42% males) and in the 4th-5th decades of life, with approximately 64% of cases presenting in patients aged 40-50 years (wang2024theclinicaloutcome pages 1-2).

**Site-Related Risk:**
Minor salivary gland involvement was identified as an independent prognostic factor associated with increased disease-free survival (DFS) in multivariate analysis, suggesting site-specific biological differences (wang2024theclinicaloutcome pages 2-3, wang2024theclinicaloutcome pages 3-4).

### Protective Factors
The literature reviewed did not identify specific genetic or environmental protective factors for MEC.

### Gene-Environment Interactions
No specific gene-environment interactions were reported in the retrieved literature for MEC.

---

## 3. PHENOTYPES

### Clinical Presentation and Histological Features

**Anatomical Distribution:**
The parotid gland is the most frequently affected site (35%), followed by minor salivary glands in the palate (27%) and tongue (6%) (wang2024theclinicaloutcome pages 1-2). Approximately 43% of MECs occur in major salivary glands (parotid, submandibular, sublingual), 49% in minor salivary glands, and 8% in the jawbones (wang2024theclinicaloutcome pages 1-2). MEC can also arise infrequently from other sites such as the lung, pancreas, cervix, and breast (chen2021thecrtc1maml2fusion pages 1-2, ge2024genomicsandtumor pages 1-2).

**Clinical Symptoms:**
- **Asymptomatic presentation:** 55% of patients presented with no overt clinical symptoms (wang2024theclinicaloutcome pages 1-2)
- **Pain:** 27% of patients (wang2024theclinicaloutcome pages 1-2)
- **Rapid growth:** 6% (wang2024theclinicaloutcome pages 1-2)
- **Numbness:** 5% (wang2024theclinicaloutcome pages 1-2)
- **Other symptoms:** Restricted mouth opening (2%), hypophagia (1%), nasal obstruction (1%), ulcer hemorrhage (2%) (wang2024theclinicaloutcome pages 1-2)

**Histological Subtypes:**
Histologically, 66.1% of cases are classical MECs, with multiple variant forms broadening the histologic spectrum:
- Clear cell MEC: 15%
- Warthin-like MEC: 6.8%
- Oncocytic variant: 4.6%
- Sclerosing MEC: 2.6%
- Uni-cystic MEC: 2.4%
- Calcifying MEC: 2.4%
(wang2024theclinicaloutcome pages 1-2, wang2024theclinicaloutcome pages 2-3)

**Histological Grading:**
MEC is classified using multiple grading systems (AFIP, modified Healey, MSK, Brandwein), which stratify tumors into low-grade (LG), intermediate-grade (IG), and high-grade (HG) categories (wang2024theclinicaloutcome pages 1-2, costa2024molecularaspectsof pages 1-3). In low-grade tumors, mucous cells and cystic structures predominate, whereas in high-grade tumors, epidermoid cells are the major component with solid architecture (costa2024molecularaspectsof pages 1-3). High-grade features include perineural infiltration and necrotic areas (costa2024molecularaspectsof pages 1-3).

### Age of Onset
The mean age at diagnosis is 42.65 years (range 7-82 years), with peak incidence in the 4th-5th decades of life (wang2024theclinicaloutcome pages 1-2, costa2024molecularaspectsof pages 1-3).

### Severity and Progression
High-grade MECs are associated with:
- Perineural invasion (13.2%)
- Lymphovascular invasion (15.9%)
- Bone invasion (8.4%)
- Lymph node metastasis (10.6%)
(wang2024theclinicaloutcome pages 1-2, wang2024theclinicaloutcome pages 2-3)

Aggressive growth pattern was observed in 83.9% of MECs (wang2024theclinicaloutcome pages 2-3). The 5-year and 10-year recurrence-free survival (RFS) rates were 91.9% and 82.5%, respectively (wang2024theclinicaloutcome pages 2-3).

### Suggested HPO Terms
- HP:0100013 (Neoplasm of the oral cavity)
- HP:0100799 (Oral cavity mucosal neoplasm)
- HP:0011800 (Midline facial cleft)
- HP:0000704 (Periodontitis)
- HP:0010307 (Stridor)
- HP:0002017 (Nausea and vomiting)
- HP:0012378 (Fatigue)
- HP:0030448 (Soft tissue sarcoma)
- HP:0002721 (Immunodeficiency)

---

## 4. GENETIC/MOLECULAR INFORMATION

### Causal Genes and Pathogenic Variants

A comprehensive summary of genetic and molecular alterations in MEC is provided in the following table:

| Gene/Alteration | Type of Alteration | Frequency (%) | Clinical Significance | Reference Citations |
|---|---|---:|---|---|
| **CRTC1::MAML2 fusion** | Recurrent gene fusion from t(11;19)(q14-21;p12-13); MAML2 rearrangement | Fusion in up to **80%** of MEC across cohorts; **42%** MAML2 rearrangement in 454-case salivary MEC cohort; detected in **11/27** WTS-profiled MECs in the same cohort | Major oncogenic driver of MEC; diagnostically highly characteristic; present in low-, intermediate-, and high-grade tumors; not consistently associated with better prognosis in contemporary cohorts; cooperates with EGFR/AREG and p16-CDK4/6-RB signaling and is therapeutically targetable in preclinical models (chen2021thecrtc1maml2fusion pages 1-2, wang2024theclinicaloutcome pages 1-2, wang2024theclinicaloutcome pages 3-4) | (chen2021thecrtc1maml2fusion pages 1-2, wang2024theclinicaloutcome pages 1-2, wang2024theclinicaloutcome pages 3-4) |
| **CRTC3::MAML2 fusion** | Alternative MAML2-family fusion | Up to **6%** of MEC; mutually exclusive with CRTC1::MAML2 | Supports MEC diagnosis and indicates biologic overlap with canonical MAML2-rearranged MEC; considered a specific recurrent fusion variant | (chen2021thecrtc1maml2fusion pages 1-2) |
| **MAML2 rearrangement (general)** | Structural rearrangement / fusion event | **50–70%** in prior salivary MEC literature; **42%** in 454-case cohort | Key molecular hallmark used in differential diagnosis by FISH/RT-PCR/NGS; important for classification but not fully prognostic on its own | (wang2024theclinicaloutcome pages 1-2, broseghini2025salivaryglandcancers pages 1-2, vrinceanu2024parotidglandtumors pages 1-2) |
| **MAML2 mutation / rearrangement** | Mixed category in genomic datasets including rearrangement and substitution | **12%** in WES/WTS-profiled subset of 26 MECs | Reflects recurrent structural and sequence-level alteration of the locus; reinforces central role of MAML2 pathway in MEC biology | (wang2024theclinicaloutcome pages 2-3) |
| **BAP1** | Somatic mutation / DNA damage-response gene alteration | **15%** in 26-case WES subset; **18.6%** in 118 advanced MEC genomic profiling cohort | Most frequently mutated gene in the 454-case genomic study; recurrently altered in aggressive disease datasets, suggesting relevance to tumor evolution and potential DDR-linked vulnerability | (wang2024theclinicaloutcome pages 1-2, wang2024theclinicaloutcome pages 2-3, zerdan2023moleculartargetsin pages 2-4) |
| **CDKN2A** | Somatic mutation, deletion, or broader genomic alteration | **8%** mutation in 26-case WES subset; **52.5%** genomic alteration in 118 advanced MECs | Strongly associated with aggressive tumor phenotypes; implicates dysregulated cell-cycle control and supports CDK4/6 pathway as a therapeutic axis | (wang2024theclinicaloutcome pages 1-2, wang2024theclinicaloutcome pages 2-3, zerdan2023moleculartargetsin pages 1-2, zerdan2023moleculartargetsin pages 2-4, chen2021thecrtc1maml2fusion pages 1-2) |
| **CDKN2B** | Genomic alteration / likely deletion or mutation | **30.5%** in 118 advanced MECs | Frequently co-altered with CDKN2A, further supporting cell-cycle deregulation as a major feature of advanced MEC | (zerdan2023moleculartargetsin pages 1-2, zerdan2023moleculartargetsin pages 2-4) |
| **TP53** | Somatic mutation / cell-cycle regulatory alteration | **8%** mutation in 26-case WES subset; **40.7%** genomic alteration in 118 advanced MECs | Enriched in aggressive tumor phenotypes; TP53 events superimposed on CRTC1::MAML2 may mark unfavorable prognosis; despite this, many MECs retain wild-type p53, supporting p53-reactivating therapeutic strategies in subsets | (wang2024theclinicaloutcome pages 1-2, wang2024theclinicaloutcome pages 2-3, zerdan2023moleculartargetsin pages 2-4, rodriguezramirez2022p53inhibitsbmi1driven pages 1-3) |
| **MET** | Somatic mutation | **8%** in 26-case WES subset; **0%** in 118 advanced MEC panel for MET alterations reported there | More frequent in aggressive tumor phenotypes in the 454-case study; potential context-dependent actionable RTK alteration though prevalence varies by cohort/platform | (wang2024theclinicaloutcome pages 1-2, wang2024theclinicaloutcome pages 2-3, zerdan2023moleculartargetsin pages 2-4) |
| **PIK3CA** | Somatic mutation / PI3K pathway alteration | **16.9%** in 118 advanced MECs | Common actionable alteration in advanced disease; supports PI3K-AKT-mTOR pathway involvement and potential use of matched targeted therapy | (zerdan2023moleculartargetsin pages 1-2, zerdan2023moleculartargetsin pages 2-4) |
| **PTEN** | Somatic alteration / tumor suppressor loss | **7.6%** in 118 advanced MECs | Supports activation of PI3K-AKT-mTOR signaling; potentially relevant to pathway-directed therapy | (zerdan2023moleculartargetsin pages 1-2, zerdan2023moleculartargetsin pages 2-4) |
| **HRAS** | Somatic mutation / RAS pathway alteration | **14.4%** in 118 advanced MECs | Indicates MAPK pathway involvement in a meaningful subset of advanced MEC; potentially targetable indirectly through pathway strategies | (zerdan2023moleculartargetsin pages 1-2, zerdan2023moleculartargetsin pages 2-4) |
| **KRAS** | Somatic mutation / RAS pathway alteration | **5.1%** overall KRAS alterations; **2.5%** KRAS G12C in 118 advanced MECs | Less common than HRAS but therapeutically relevant because KRAS G12C is a druggable genotype in other cancers | (zerdan2023moleculartargetsin pages 2-4) |
| **RB1** | Deletion or genomic alteration | **3.4%** genomic alteration in 118 advanced MECs; focal deletion reported in one metastatic high-grade tumor | Supports disruption of p16-CDK4/6-RB axis, a major cooperating pathway in MEC tumorigenesis | (zerdan2023moleculartargetsin pages 2-4, wang2024theclinicaloutcome pages 3-4, chen2021thecrtc1maml2fusion pages 1-2) |
| **CCND1** | Genomic alteration | **3.4%** in 118 advanced MECs | Additional evidence for cell-cycle dysregulation and potential CDK4/6 pathway dependency | (zerdan2023moleculartargetsin pages 2-4) |
| **MTAP** | Deletion / genomic alteration | **13.7%** in 118 advanced MECs; deleted with CDKN2A/2B in a recurrent high-grade case | Often co-deleted with CDKN2A/2B; may create therapeutic liabilities linked to methylthioadenosine metabolism / PRMT5-directed strategies in broader oncology | (zerdan2023moleculartargetsin pages 2-4, wang2024theclinicaloutcome pages 3-4) |
| **TERT** | Genomic alteration | **15.0%** in 118 advanced MECs | Suggests telomere maintenance pathway involvement in a subset of advanced MEC | (zerdan2023moleculartargetsin pages 2-4) |
| **BRCA2** | DNA damage-response alteration | **5.9%** in 118 advanced MECs | May indicate homologous recombination defects in a subset; potentially relevant to PARP-inhibitor sensitivity hypotheses | (zerdan2023moleculartargetsin pages 2-4) |
| **ATM** | DNA damage-response alteration | **4.2%** in 118 advanced MECs | Supports occasional DDR pathway disruption | (zerdan2023moleculartargetsin pages 2-4) |
| **BRCA1** | DNA damage-response alteration | **1.7%** in 118 advanced MECs | Rare but potentially actionable DDR-related event | (zerdan2023moleculartargetsin pages 2-4) |
| **PALB2** | DNA damage-response alteration | **0.8%** in 118 advanced MECs | Rare potential homologous recombination-associated event | (zerdan2023moleculartargetsin pages 2-4) |
| **ARID1A** | Chromatin remodeling alteration | **2.5%** in 118 advanced MECs | Suggests chromatin-regulatory disruption in a subset | (zerdan2023moleculartargetsin pages 2-4) |
| **FGFR1** | Receptor tyrosine kinase alteration | **5.1%** in 118 advanced MECs | Potentially targetable RTK event in a minority of cases | (zerdan2023moleculartargetsin pages 2-4) |
| **ERBB2 (HER2) amplification** | Copy-number gain / amplification | **5.9%** amplification in 118 advanced MECs | Actionable in principle with HER2-directed therapy; one of the clearer targetable alterations in advanced salivary cancers | (zerdan2023moleculartargetsin pages 1-2, zerdan2023moleculartargetsin pages 2-4, broseghini2025salivaryglandcancers pages 1-2) |
| **EGFR alteration / AREG-EGFR signaling activation** | Rare genomic alteration; pathway activation by fusion-driven signaling | **0.8%** EGFR genomic alteration in 118 advanced MECs | Even with low alteration frequency, EGFR signaling is biologically important downstream of CRTC1::MAML2; erlotinib showed enhanced preclinical activity when combined with palbociclib | (zerdan2023moleculartargetsin pages 2-4, chen2021thecrtc1maml2fusion pages 1-2) |
| **NOTCH1** | Somatic alteration | **4.2%** in 118 advanced MECs | Indicates occasional involvement of NOTCH pathway biology | (zerdan2023moleculartargetsin pages 2-4) |
| **NOTCH2** | Somatic alteration | **7.6%** in 118 advanced MECs | Additional evidence for NOTCH pathway perturbation in a subset | (zerdan2023moleculartargetsin pages 2-4) |
| **FBXW7** | Somatic mutation | Frequency not stated in cohort summary; identified in fusion-positive poor-prognosis context | Specific FBXW7 events superimposed on CRTC1::MAML2 were associated with unfavorable prognosis in the 454-case study | (wang2024theclinicaloutcome pages 1-2) |
| **EWSR1 rearrangement (general)** | Structural rearrangement / alternative fusion event | **8%** in 454-case cohort | Uncommon but recurrent alternative rearrangement class; important in differential diagnosis and may define molecular subgroups distinct from canonical MAML2-rearranged MEC | (wang2024theclinicaloutcome pages 1-2) |
| **EWSR1::CREM** | Gene fusion | Observed in **1** tumor in 26-case WTS subset | Rare alternative rearrangement detected in MEC; significance still emerging | (wang2024theclinicaloutcome pages 3-4) |
| **EWSR1::ATF1** | Gene fusion | Observed in **1** tumor in 26-case WTS subset | Rare alternative fusion event; may complicate differential diagnosis with other EWSR1-rearranged salivary neoplasms | (wang2024theclinicaloutcome pages 3-4) |
| **SPINK1 (germline)** | Pathogenic germline mutation | **2%** in 26-case WES subset | Cancer-susceptibility finding reported in a small subset; clinical significance for MEC predisposition remains uncertain | (wang2024theclinicaloutcome pages 2-3) |
| **FANCG (germline)** | Pathogenic germline mutation | **2%** in 26-case WES subset | Germline cancer-susceptibility finding of uncertain MEC-specific contribution | (wang2024theclinicaloutcome pages 2-3) |
| **Copy-number amplifications (global)** | CNV amplification burden | **437** amplifications across **26** profiled tumors | Demonstrates substantial structural genomic complexity in a subset of MECs, particularly advanced/high-grade disease | (wang2024theclinicaloutcome pages 3-4) |
| **Copy-number deletions (global)** | CNV deletion burden | **11** deletions across **26** profiled tumors | Deletions include key tumor suppressor and cell-cycle genes, supporting progression biology | (wang2024theclinicaloutcome pages 3-4) |
| **CYSLTR2 / ITM2B / RCBTB2 / RB1 deletions** | Focal deletions in one tumor | Single high-grade metastatic case | Associated with brain-metastatic high-grade MEC in the 26-case genomic subset; may mark aggressive progression biology | (wang2024theclinicaloutcome pages 3-4) |
| **EMT-related transcriptomic program** | Gene-expression / pathway activation rather than discrete mutation | Not expressed as %; enriched in MEC transcriptomic profiling | High EMT scores correlated with poor prognosis and immune activation; highlights molecular heterogeneity beyond DNA alterations | (zou2025systematicidentificationof pages 1-2) |
| **SLC2A1-AS1 and CERS6-AS1** | lncRNA dysregulation | Not expressed as % | Proposed mediators of EMT and tumor immune microenvironment in MEC; candidate biomarkers/targets from recent transcriptomic analysis | (zou2025systematicidentificationof pages 1-2) |


*Table: This table summarizes the major recurrent genomic and molecular alterations reported in mucoepidermoid carcinoma, including fusion events, somatic mutations, CNVs, and transcriptomic features. It is useful for linking diagnostic markers and biologic drivers to prognosis and potential targeted therapy strategies.*

**Major Gene Fusions:**
- **CRTC1::MAML2:** Present in up to 80% of MECs; represents the major oncogenic driver (chen2021thecrtc1maml2fusion pages 1-2, wang2024theclinicaloutcome pages 1-2, wang2024theclinicaloutcome pages 3-4)
- **CRTC3::MAML2:** Alternative fusion in up to 6% of cases, mutually exclusive with CRTC1::MAML2 (chen2021thecrtc1maml2fusion pages 1-2)
- **EWSR1 rearrangements:** Found in 8% of cases; includes EWSR1::CREM and EWSR1::ATF1 fusions (wang2024theclinicaloutcome pages 1-2, wang2024theclinicaloutcome pages 3-4)

**Most Frequently Mutated Genes:**
- **BAP1:** 15-18.6% (most frequently mutated gene in genomic studies) (wang2024theclinicaloutcome pages 1-2, wang2024theclinicaloutcome pages 2-3, zerdan2023moleculartargetsin pages 2-4)
- **CDKN2A:** 8-52.5% (wang2024theclinicaloutcome pages 1-2, wang2024theclinicaloutcome pages 2-3, zerdan2023moleculartargetsin pages 1-2, zerdan2023moleculartargetsin pages 2-4)
- **CDKN2B:** 30.5% (zerdan2023moleculartargetsin pages 1-2, zerdan2023moleculartargetsin pages 2-4)
- **TP53:** 8-40.7% (wang2024theclinicaloutcome pages 1-2, wang2024theclinicaloutcome pages 2-3, zerdan2023moleculartargetsin pages 2-4)
- **PIK3CA:** 16.9% (zerdan2023moleculartargetsin pages 1-2, zerdan2023moleculartargetsin pages 2-4)
- **HRAS:** 14.4% (zerdan2023moleculartargetsin pages 1-2, zerdan2023moleculartargetsin pages 2-4)
- **MET:** 8% (wang2024theclinicaloutcome pages 1-2, wang2024theclinicaloutcome pages 2-3)

**Variant Classification:**
Mutations in CDKN2A, MET, and TP53 were more frequently found in aggressive tumor phenotypes (wang2024theclinicaloutcome pages 1-2). Specific genetic events (in TP53 and FBXW7) with CRTC1::MAML2 fusion superimposed might be associated with unfavorable prognosis (wang2024theclinicaloutcome pages 1-2).

**Allele Frequency:**
The literature reviewed did not provide specific population allele frequencies for germline variants. The reported frequencies reflect somatic alterations in tumor samples.

**Somatic vs Germline:**
The vast majority of genetic alterations in MEC are somatic. Rare germline variants in SPINK1 and FANCG (each 2%) were identified as cancer susceptibility mutations (wang2024theclinicaloutcome pages 2-3).

**Functional Consequences:**
- **CRTC1-MAML2 fusion:** Disrupts NOTCH signaling and activates cAMP-responsive genes; drives tumorigenesis with 100% penetrance in transgenic models (chen2021thecrtc1maml2fusion pages 1-2)
- **CDKN2A/CDKN2B loss:** Disrupts cell-cycle control via the p16-CDK4/6-RB pathway (chen2021thecrtc1maml2fusion pages 1-2, zerdan2023moleculartargetsin pages 2-4)
- **p53 pathway:** Despite lower mutation frequency than other head and neck cancers, p53 pathway disruption occurs and p53 activation can suppress cancer stem cell properties (rodriguezramirez2022p53inhibitsbmi1driven pages 1-3)

### Modifier Genes
The literature did not explicitly identify specific modifier genes, though cooperating pathway alterations (e.g., p16-CDK4/6-RB, PI3K-AKT-mTOR) suggest modifier effects.

### Epigenetic Information
One study identified long non-coding RNAs (lncRNAs) as potential mediators of epithelial-mesenchymal transition (EMT) and the immune microenvironment. High EMT scores correlated with upregulated EMT and immune response activity, indicating poor prognosis. SLC2A1-AS1 and CERS6-AS1 were identified as potential lncRNA biomarkers (zou2025systematicidentificationof pages 1-2).

### Chromosomal Abnormalities
Copy number analysis revealed 448 CNVs (437 amplifications and 11 deletions) in 26 patients (wang2024theclinicaloutcome pages 3-4). One high-grade tumor with distant metastasis had deletions in CYSLTR2, ITM2B, RCBTB2, and RB1. Another high-grade tumor with local recurrence had deletion of CDKN2A/2B and MTAP genes (wang2024theclinicaloutcome pages 3-4).

---

## 5. ENVIRONMENTAL INFORMATION

### Environmental Factors
The retrieved literature did not identify specific environmental toxins, radiation exposures, or occupational factors as causal in MEC.

### Lifestyle Factors
Among 454 MEC patients, 95% were nonsmokers and only 5% had a smoking history, suggesting smoking is not a major contributing factor (wang2024theclinicaloutcome pages 1-2).

### Infectious Agents
No infectious agents were identified as causative or contributory factors for MEC in the literature reviewed.

---

## 6. MECHANISM / PATHOPHYSIOLOGY

### Molecular Pathways

**CRTC1-MAML2 Fusion-Driven Signaling:**
The CRTC1-MAML2 fusion activates AREG/EGFR signaling, which serves as a critical downstream effector (chen2021thecrtc1maml2fusion pages 1-2). Cotargeting of aberrant p16-CDK4/6-RB signaling and CRTC1-MAML2 fusion-activated AREG/EGFR signaling with the CDK4/6 inhibitor palbociclib and EGFR inhibitor erlotinib produced enhanced antitumor responses in vitro and in vivo (chen2021thecrtc1maml2fusion pages 1-2).

**Dysregulated Cell-Cycle Pathways:**
- **p16-CDK4/6-RB pathway:** Alterations in CDKN2A, CDKN2B, RB1, and CCND1 support disruption of cell-cycle control (chen2021thecrtc1maml2fusion pages 1-2, zerdan2023moleculartargetsin pages 2-4)
- **TP53 pathway:** Although less frequently mutated than in other head and neck cancers, TP53 mutations occur in 8-40.7% of cases (wang2024theclinicaloutcome pages 1-2, zerdan2023moleculartargetsin pages 2-4)

**PI3K-AKT-mTOR Pathway:**
PIK3CA mutations (16.9%), PTEN alterations (7.6%), and related pathway genes support activation of PI3K-AKT-mTOR signaling (zerdan2023moleculartargetsin pages 1-2, zerdan2023moleculartargetsin pages 2-4). Gene set enrichment analysis identified PI3K-AKT signaling pathway, ECM-receptor interaction, and focal adhesion as enriched in non-progression group (wang2024theclinicaloutcome pages 3-4).

**MAPK Pathway:**
HRAS (14.4%), KRAS (5.1%), and BRAF (1.7%) mutations indicate MAPK pathway involvement in a subset of MECs (zerdan2023moleculartargetsin pages 2-4).

### Cellular Processes

**Cancer Stem Cells (CSCs):**
MEC CSCs are a subset of cells marked by high ALDH enzymatic activity and CD44 expression that are highly tumorigenic and have self-renewal capacity (rodriguezramirez2022p53inhibitsbmi1driven pages 1-3). p53 inhibits Bmi-1-driven self-renewal and defines salivary gland cancer stemness. Although p53 activation does not induce MEC CSC apoptosis, it reduces stemness properties such as self-renewal by regulating Bmi-1 expression and driving CSC towards differentiation (rodriguezramirez2022p53inhibitsbmi1driven pages 1-3). Therapeutic activation of p53 prevented CSC-mediated tumor recurrence in preclinical trials (rodriguezramirez2022p53inhibitsbmi1driven pages 1-3).

**Epithelial-Mesenchymal Transition (EMT):**
Gene set enrichment analysis revealed significant enrichment in EMT pathways in progressive MECs. High EMT scores correlated with upregulated EMT and immune response activity, indicating poor prognosis (zou2025systematicidentificationof pages 1-2). Key genes contributing to the EMT process include Secretogranin II (SCG2), tissue factor pathway inhibitor 2 (TFPI2), and periostin (POSTN) (zou2025systematicidentificationof pages 1-2).

**Cell-Cycle Dysregulation:**
GO enrichment analysis showed mutated genes enriched in nucleosome assembly, chromatin silencing, and regulation of gene silencing (biological processes); nucleosome, keratin filament, nuclear nucleosome (cellular components); and DNA binding, protein heterodimerization activity (molecular functions) in the progression group (wang2024theclinicaloutcome pages 3-4).

### Protein Dysfunction
The CRTC1-MAML2 fusion protein exhibits transforming activity in vitro and serves as an oncogenic driver for MEC establishment and maintenance in vivo (chen2021thecrtc1maml2fusion pages 1-2).

### Metabolic Changes
Specific metabolic alterations were not extensively characterized in the retrieved literature.

### Immune System Involvement
Single-sample gene set enrichment analysis unveiled the tumors' immune infiltration signature, suggesting active antigen presentation and a positive immune response potentially favorable for immunotherapy (zou2025systematicidentificationof pages 1-2). In breast MEC, M2 macrophages and plasma cells were in the high infiltration group, differing from salivary gland MEC (ge2024genomicsandtumor pages 1-2).

### Molecular Profiling

**Transcriptomics:**
RNA sequencing analysis revealed 193 genes were significantly differentially expressed (adjusted P < 0.05) between MEC patients with and without disease progression (wang2024theclinicaloutcome pages 3-4). Among them, 20 transcription factors (TFs) including PAX6, REST, FOS, SP1, CEBPD, SRF, TCF12, NFIC, SIX5, JUND, JUN, ZKSCAN1, FOSL1, STAT1, ETS1, YY1, CEBPB, TBP, and ELF1 were overexpressed in progressive MECs (wang2024theclinicaloutcome pages 3-4).

**Gene Expression Signatures:**
In progressive MECs, genes associated with "HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION," "HALLMARK_TNFA_SIGNALING_VIA_NFKB," "RB_P107_DN.V1_UP," and "HALLMARK_MYC_TARGETS_V1" were upregulated, while those associated with "KRAS.50_UP.V1_DN" and "JAK2_DN.V1_DN" were downregulated (wang2024theclinicaloutcome pages 3-4).

### Suggested Ontology Terms
- **GO Biological Processes:** GO:0006334 (nucleosome assembly), GO:0006342 (chromatin silencing), GO:0016458 (gene silencing), GO:0001525 (angiogenesis), GO:0030198 (extracellular matrix organization), GO:0008283 (cell proliferation)
- **GO Cellular Components:** GO:0000786 (nucleosome), GO:0045095 (keratin filament), GO:0005694 (chromosome)
- **GO Molecular Functions:** GO:0003677 (DNA binding), GO:0046982 (protein heterodimerization activity)
- **CL Cell Types:** CL:0000066 (epithelial cell), CL:0000148 (melanocyte), CL:0000235 (macrophage), CL:0000236 (B cell), CL:0000084 (T cell)

---

## 7. ANATOMICAL STRUCTURES AFFECTED

### Organ Level

**Primary Organs:**
Salivary glands are the primary organs affected. Among 454 MEC cases:
- Major salivary glands: 43% (parotid 35%, submandibular 4%, sublingual 3%)
- Minor salivary glands: 49% (palate 27%, tongue 6%, gingiva 3%, buccal 5%, retromolar region 3%)
- Jawbones (mandibular, maxillary): 8%
(wang2024theclinicaloutcome pages 1-2)

**Secondary Sites:**
MEC can arise in other organs including:
- Lung (pulmonary MEC)
- Pancreas
- Breast (mammary MEC)
- Cervix
- Thyroid
- External auditory canal
(chen2021thecrtc1maml2fusion pages 1-2, ge2024genomicsandtumor pages 1-2)

**Metastatic Sites:**
The lungs are the most common site of distant metastasis (10/21 cases), followed by brain (5/21), neck (3/21), liver (2/21), and bone (1/21) (wang2024theclinicaloutcome pages 1-2).

### Tissue and Cell Level
MEC is composed of epithelial (ductal) cells forming a triad of:
- Mucin-secreting cells (mucous cells)
- Epidermoid cells (squamous cells)
- Intermediate cells
(chen2021thecrtc1maml2fusion pages 1-2, costa2024molecularaspectsof pages 1-3)

The tumor also contains cancer stem cells marked by high ALDH activity and CD44 expression (rodriguezramirez2022p53inhibitsbmi1driven pages 1-3).

### Suggested UBERON Terms
- UBERON:0001723 (tongue)
- UBERON:0001831 (parotid gland)
- UBERON:0001830 (submandibular gland)
- UBERON:0001825 (sublingual gland)
- UBERON:0035841 (minor salivary gland)
- UBERON:0001684 (upper jaw region)
- UBERON:0001685 (lower jaw region)
- UBERON:0002048 (lung)
- UBERON:0001264 (pancreas)
- UBERON:0000310 (breast)

---

## 8. TEMPORAL DEVELOPMENT

### Onset

**Age of Onset:**
- Mean age: 42.65 years (range 7-82 years)
- Peak incidence: 4th-5th decades of life
- Approximately 64% present in patients aged 40-50 years
(wang2024theclinicaloutcome pages 1-2)

**Onset Pattern:**
The literature does not extensively characterize acute vs. chronic onset patterns. Clinical presentation is variable, with 55% asymptomatic at diagnosis (wang2024theclinicaloutcome pages 1-2).

### Progression

**Disease Stages:**
TNM staging distribution in 454 cases:
- Stage I: 50%
- Stage II: 34%
- Stage III: 7%
- Stage IV: 8%
(wang2024theclinicaloutcome pages 1-2)

**Histologic Grading Systems:**
Four grading systems are used (AFIP, Brandwein, MSK, modified Healey), stratifying tumors as low-grade (LG), intermediate-grade (IG), or high-grade (HG). High AFIP grade was independently associated with decreased DFS in multivariate analysis (wang2024theclinicaloutcome pages 2-3, wang2024theclinicaloutcome pages 3-4).

**Progression Rate and Course:**
- Local recurrence: 4.2% (19/454 patients)
- Distant metastasis and death: 4.6% (21/454)
- 5-year RFS: 91.9%
- 10-year RFS: 82.5%
- Average follow-up: 62 months (range 1-116 months)
(wang2024theclinicaloutcome pages 1-2, wang2024theclinicaloutcome pages 2-3)

Patients with disease progression had an average follow-up of 37 months (range 2-114 months) (wang2024theclinicaloutcome pages 2-3).

### Patterns
The literature did not extensively describe remission patterns or critical periods specific to MEC.

---

## 9. INHERITANCE AND POPULATION

### Epidemiology

**Prevalence and Incidence:**
MEC is the most common malignant salivary gland tumor, accounting for 30-40% of all malignant salivary gland tumors (wang2024theclinicaloutcome pages 1-2, chen2021thecrtc1maml2fusion pages 1-2). Salivary gland tumors overall have an estimated global incidence ranging from 0.4 to 13.5 cases per 100,000 population per year (costa2024molecularaspectsof pages 1-3). Salivary gland cancers specifically account for approximately 5% of head and neck cancers, with an annual incidence of 0.57 to 0.69 cases per 100,000 individuals (broseghini2025salivaryglandcancers pages 1-2).

### Genetic Etiology

**Inheritance Pattern:**
MEC is primarily a sporadic cancer without a clear Mendelian inheritance pattern. The CRTC1-MAML2 and other gene fusions are somatic events (chen2021thecrtc1maml2fusion pages 1-2, wang2024theclinicaloutcome pages 1-2).

**Germline Findings:**
Rare germline mutations in cancer susceptibility genes SPINK1 (2%) and FANCG (2%) were identified in one genomic study, but their specific role in MEC predisposition is uncertain (wang2024theclinicaloutcome pages 2-3).

### Population Demographics

**Sex Distribution:**
- Female: 58%
- Male: 42%
- Male:female ratio = 1:1.39
(wang2024theclinicaloutcome pages 1-2)

Salivary gland cancers overall show a slight male prevalence globally (broseghini2025salivaryglandcancers pages 1-2).

**Age Distribution:**
Mean age at diagnosis: 42.65 years (range 7-82), with peak incidence in the 4th-5th decades (wang2024theclinicaloutcome pages 1-2).

**Geographic/Ethnic Distribution:**
The literature reviewed did not provide detailed geographic or ethnic distribution data specific to MEC.

---

## 10. DIAGNOSTICS

### Clinical Tests

**Histopathology:**
Microscopic examination reveals the characteristic triad of mucous, intermediate, and squamous cells (chen2021thecrtc1maml2fusion pages 1-2, costa2024molecularaspectsof pages 1-3). Low-grade tumors show predominantly mucous cells and cystic structures, while high-grade tumors are solid with epidermoid cell predominance (costa2024molecularaspectsof pages 1-3).

**Immunohistochemistry:**
- **Cytokeratins (CK AE1/3, CK5/6, CK7, CK14):** Positive and used for cell-type identification (costa2024molecularaspectsof pages 3-5, costa2024molecularaspectsof pages 1-3)
- **p63, p40:** Highlight squamoid and intermediate cells (roden2023theroleof pages 1-2, costa2024molecularaspectsof pages 1-3)
- **MUC4:** Expression patterns vary; highest mean MUC16 score in MEC (177.0 ± 110.0) in one study (costa2024molecularaspectsof pages 3-5)
- **Ki-67:** Marker of cell proliferation, associated with tumor aggressiveness (costa2024molecularaspectsof pages 1-3)
- **CD117/c-Kit:** Overexpressed in some cases (costa2024molecularaspectsof pages 3-5, costa2024molecularaspectsof pages 1-3)

**Histochemistry:**
Mucicarmine staining highlights cytoplasmic mucin (roden2023theroleof pages 1-2).

**Biomarkers:**
Tumor mutation burden (TMB) > 10 was found in 16.9% of MECs. PD-L1 high expression (≥50% staining) was seen in 4.2% of MECs (zerdan2023moleculartargetsin pages 1-2, zerdan2023moleculartargetsin pages 2-4).

### Genetic Testing

**Fluorescence In Situ Hybridization (FISH):**
MAML2 rearrangement detection by FISH is a key diagnostic tool. Break-apart FISH probes detect MAML2 translocation in 42-80% of MECs (wang2024theclinicaloutcome pages 1-2, ge2024genomicsandtumor pages 1-2, vrinceanu2024parotidglandtumors pages 1-2). A case is positive if break-apart signals are identified in ≥20% of tumor nuclei (ge2024genomicsandtumor pages 1-2).

**Reverse Transcription PCR (RT-PCR) and RNA Sequencing:**
RT-PCR and RNA sequencing identify specific fusion partners (CRTC1-MAML2, CRTC3-MAML2) and confirm fusion transcripts (ge2024genomicsandtumor pages 1-2, vrinceanu2024parotidglandtumors pages 1-2).

**Next-Generation Sequencing (NGS):**
Comprehensive genomic profiling using NGS (e.g., FoundationOne CDX) evaluates base substitutions, insertions, deletions, copy number changes, gene fusions, and rearrangements across 324 genes (zerdan2023moleculartargetsin pages 1-2, zerdan2023moleculartargetsin pages 2-4, vrinceanu2024parotidglandtumors pages 1-2). Whole-exome sequencing (WES) and whole-transcriptome sequencing (WTS) have been used to characterize the genomic landscape of MEC (wang2024theclinicaloutcome pages 1-2, wang2024theclinicaloutcome pages 2-3).

**Gene Panels:**
Panels exploring MAML2, CRTC1, CRTC3, EWSR1, and other genes facilitate differential diagnosis (vrinceanu2024parotidglandtumors pages 1-2).

### Imaging Studies
While not extensively detailed in the molecular-focused literature reviewed, ultrasound, CT, and MRI are standard imaging modalities for parotid and salivary gland tumors (vrinceanu2024parotidglandtumors pages 1-2).

### Clinical Criteria
Multiple histologic grading systems (AFIP, modified Healey, MSK, Brandwein) stratify MECs for prognosis (wang2024theclinicaloutcome pages 1-2, costa2024molecularaspectsof pages 1-3).

### Differential Diagnosis
Molecular testing (FISH, RT-PCR, NGS) helps differentiate MEC from other salivary gland tumors with overlapping morphology, such as glandular odontogenic cyst, adenoid cystic carcinoma, and high-grade mucoepidermoid carcinoma vs. other oncocytoid tumors (vrinceanu2024parotidglandtumors pages 1-2).

---

## 11. OUTCOME/PROGNOSIS

### Survival and Mortality

**Recurrence-Free Survival:**
- 5-year RFS: 91.9%
- 10-year RFS: 82.5%
(wang2024theclinicaloutcome pages 2-3)

High-grade (HG) subtype was associated with significantly shorter RFS than low-grade (LG) or intermediate-grade (Int G) subtypes: 5-year RFS 85.9% vs. 95.1% for classical MEC; 77.0% vs. 97.5% for all subtypes (wang2024theclinicaloutcome pages 2-3).

**Overall Outcomes:**
Among 454 patients:
- Alive without relapse: 91.2% (414/454)
- Local recurrence: 4.2% (19/454)
- Distant metastasis and death: 4.6% (21/454)
(wang2024theclinicaloutcome pages 1-2)

**Disease-Free Survival:**
In breast MEC cases, disease-free survival ranged from 20 to 67 months (ge2024genomicsandtumor pages 1-2).

### Morbidity and Function
The literature did not extensively characterize quality-of-life measures or functional outcomes, though major head and neck surgery and radiation can result in high patient morbidity with facial disfigurement (rodriguezramirez2022p53inhibitsbmi1driven pages 1-3).

### Prognostic Factors

**Independent Prognostic Factors (Multivariate Analysis):**
- High AFIP grade (p < 0.001)
- Minor salivary gland site (p = 0.006)
(wang2024theclinicaloutcome pages 2-3, wang2024theclinicaloutcome pages 3-4)

**Univariate Prognostic Factors:**
- Older age
- Clinical symptoms
- High TNM stage
- High-grade tumor
- Improper surgical modality
(wang2024theclinicaloutcome pages 1-2)

**Pathological Features Associated with Recurrence:**
- Cystic component < 20% (p = 0.011)
- Perineural invasion (p = 0.003)
- Necrosis (p < 0.001)
- Mitosis (p < 0.001)
- Anaplasia (p < 0.001)
- Lymphovascular invasion (p < 0.001)
- Bone invasion (p = 0.003)
(wang2024theclinicaloutcome pages 2-3)

**Molecular Prognostic Markers:**
Specific genetic events (TP53 and FBXW7 mutations) with CRTC1::MAML2 fusion superimposed might be associated with unfavorable prognosis (wang2024theclinicaloutcome pages 1-2). High EMT scores correlated with poor prognosis (zou2025systematicidentificationof pages 1-2).

**MAML2 Fusion Status:**
Contemporary studies show no consistent correlation between CRTC1::MAML2 translocation status and lymph node metastasis, recurrence, or histological grade, contrasting with older literature suggesting better prognosis for fusion-positive cases (wang2024theclinicaloutcome pages 1-2, wang2024theclinicaloutcome pages 3-4).

---

## 12. TREATMENT

### Pharmacotherapy

**Standard Chemotherapy:**
Chemotherapy has shown limited benefit for MEC patients, and no effective systemic treatment is currently approved for unresectable, recurrent, or metastatic disease (chen2021thecrtc1maml2fusion pages 1-2, rodriguezramirez2022p53inhibitsbmi1driven pages 1-3, costa2024molecularaspectsof pages 1-3).

**Targeted Therapies (Preclinical/Emerging):**

**CDK4/6 Inhibitors:**
Palbociclib (FDA-approved CDK4/6 inhibitor) showed preclinical activity against MEC, particularly in combination with EGFR inhibitors, based on cooperating p16-CDK4/6-RB pathway dysregulation (chen2021thecrtc1maml2fusion pages 1-2).

**EGFR Inhibitors:**
Erlotinib (FDA-approved EGFR inhibitor) targets AREG/EGFR signaling activated downstream of CRTC1-MAML2. Combination of palbociclib and erlotinib produced enhanced antitumor responses in vitro and in vivo (chen2021thecrtc1maml2fusion pages 1-2).

**p53 Activators:**
MDM2 inhibitors activate p53 signaling by disrupting MDM2-p53 interaction. Therapeutic activation of p53 reduced cancer stem cell fraction, prevented CSC-mediated tumor recurrence in preclinical models, and suppressed stemness without inducing apoptosis (rodriguezramirez2022p53inhibitsbmi1driven pages 1-3).

**PI3K/AKT/mTOR Inhibitors:**
Given PIK3CA mutations in 16.9% of advanced MECs, PI3K pathway inhibitors (e.g., alpelisib) may have utility in molecularly selected patients (zerdan2023moleculartargetsin pages 1-2, zerdan2023moleculartargetsin pages 2-4).

**HER2-Directed Therapy:**
ERBB2 amplification in 5.9% of cases suggests HER2-directed therapies (trastuzumab, lapatinib) could benefit select patients (zerdan2023moleculartargetsin pages 1-2, zerdan2023moleculartargetsin pages 2-4).

### Surgical and Interventional

**Surgical Resection:**
All 454 patients in one cohort underwent complete mass resection with lobectomy (wang2024theclinicaloutcome pages 1-2). Surgical treatment is the primary modality and the only effective management for MEC (chen2021thecrtc1maml2fusion pages 1-2).

**Neck Dissection:**
- Ipsilateral neck dissection: 25%
- Bilateral neck dissection: 3%
(wang2024theclinicaloutcome pages 1-2)

### Adjuvant Treatment

**Radiation Therapy:**
- Radiotherapy: 11%
- Chemoradiotherapy: 1%
- I-125 seed implantation: 16%
(wang2024theclinicaloutcome pages 1-2)

Radiation is indicated in selected cases, particularly for high-risk features (chen2021thecrtc1maml2fusion pages 1-2, costa2024molecularaspectsof pages 1-3).

### Immunotherapy

**Checkpoint Inhibitors:**
Tumor mutation burden (TMB) > 10 in 16.9% and PD-L1 high expression in 4.2% suggest a subset of MECs may respond to immune checkpoint inhibitors (zerdan2023moleculartargetsin pages 1-2, zerdan2023moleculartargetsin pages 2-4). Single-sample gene set enrichment analysis suggested active antigen presentation and positive immune response potentially favorable for immunotherapy (zou2025systematicidentificationof pages 1-2).

### Experimental Treatments

**Preclinical Combination Therapy:**
The combination of palbociclib (CDK4/6 inhibitor) and erlotinib (EGFR inhibitor) is a potentially novel combination therapy identified through preclinical studies (chen2021thecrtc1maml2fusion pages 1-2).

**CRTC1-MAML2 Targeting:**
Doxycycline-induced CRTC1-MAML2 knockdown blocked growth of established MEC xenografts, validating the fusion as a therapeutic target, though direct fusion-targeting approaches remain under development (chen2021thecrtc1maml2fusion pages 1-2).

### Suggested MAXO Terms
- MAXO:0000004 (surgical procedure)
- MAXO:0000058 (radiotherapy)
- MAXO:0000127 (chemotherapy)
- MAXO:0001001 (gene therapy)
- MAXO:0000882 (targeted molecular therapy)

---

## 13. PREVENTION

### Primary Prevention
No primary prevention strategies specific to MEC were identified in the literature, as the disease is primarily sporadic without established environmental risk factors.

### Secondary Prevention

**Early Detection:**
Fine-needle aspiration biopsy (FNAB) combined with imaging (MRI, ultrasound) facilitates preoperative diagnosis, though molecular confirmation (FISH, NGS) improves accuracy (vrinceanu2024parotidglandtumors pages 1-2).

### Tertiary Prevention
Adjuvant radiotherapy and close follow-up aim to prevent local recurrence in high-risk cases (wang2024theclinicaloutcome pages 1-2, costa2024molecularaspectsof pages 1-3).

### Genetic Counseling
Given the sporadic nature and lack of established germline predisposition syndromes, genetic counseling is not routinely indicated unless germline susceptibility variants (e.g., SPINK1, FANCG) are identified (wang2024theclinicaloutcome pages 2-3).

---

## 14. OTHER SPECIES / NATURAL DISEASE

### Taxonomy and Natural Disease
The literature reviewed did not identify naturally occurring MEC in other species (companion animals, wildlife). MEC is primarily a human disease.

### Comparative Biology
No comparative pathology data across species were reported in the retrieved literature.

### Transmission
MEC is not a transmissible disease and has no zoonotic potential.

---

## 15. MODEL ORGANISMS

A comprehensive summary of experimental models for MEC research is provided in the following table:

| Model Type | Model Name/Description | Characteristics | Applications | Key Findings | References |
|---|---|---|---|---|---|
| Human MEC cell lines | **UM-HMC-1, UM-HMC-3A, UM-HMC-3B** | Established human salivary MEC cell lines used for CSC and signaling studies; support flow cytometry, sphere assays, gene silencing, drug treatment, and xenografting; used in both subcutaneous and orthotopic murine models (rodriguezramirez2022p53inhibitsbmi1driven pages 1-3) | Cancer stem cell biology, p53/MDM2 pathway studies, self-renewal assays, therapeutic testing, xenograft generation | p53 activation reduced stemness and self-renewal, drove differentiation, and prevented CSC-mediated recurrence in preclinical models; these lines are core experimental tools for MEC biology (rodriguezramirez2022p53inhibitsbmi1driven pages 1-3) | (rodriguezramirez2022p53inhibitsbmi1driven pages 1-3) |
| Human MEC cell lines / xenograft source | **MEC-derived xenograft-compatible cell lines carrying CRTC1-MAML2** | Used in inducible knockdown experiments and as source of established MEC xenografts; fusion-positive context enabled functional validation of the fusion as a driver (chen2021thecrtc1maml2fusion pages 1-2) | Functional validation of oncogenic drivers, target dependency studies, in vivo therapeutic testing | Doxycycline-induced **CRTC1-MAML2** knockdown blocked growth of established MEC xenografts, demonstrating fusion dependency and validating the fusion as a therapeutic target (chen2021thecrtc1maml2fusion pages 1-2) | (chen2021thecrtc1maml2fusion pages 1-2) |
| Cell line-based CSC models | **ALDH-high/CD44-positive MEC CSC fractions derived from UM-HMC lines** | Subpopulation model of tumor-initiating/stem-like MEC cells; assessed with sphere assays and cell-fate analyses; linked to recurrence biology (rodriguezramirez2022p53inhibitsbmi1driven pages 1-3) | Study of self-renewal, plasticity, recurrence mechanisms, CSC-targeted therapy | Supports the concept that CSCs drive progression/recurrence in MEC and that p53 activation can suppress CSC properties without necessarily inducing apoptosis (rodriguezramirez2022p53inhibitsbmi1driven pages 1-3) | (rodriguezramirez2022p53inhibitsbmi1driven pages 1-3) |
| Patient-derived xenograft (PDX) | **Salivary MEC PDX models** | Generated from surgically resected human salivary gland carcinomas; in Aizawa et al., one series of MEC PDXs was successfully established; retained histologic features, transcription profiles, genomic variants, and fusion genes of original tumors (aizawa2023establishmentofexperimental pages 1-2) | Preclinical drug testing, translational modeling, preservation of patient tumor heterogeneity, study of molecular mechanisms | MEC PDXs recapitulated the original tumors and provide a resource for novel therapeutic strategy development (aizawa2023establishmentofexperimental pages 1-2) | (aizawa2023establishmentofexperimental pages 1-2) |
| Orthotopic xenograft | **Orthotopic murine MEC models** | In vivo implantation models using MEC cells/organoids into anatomically relevant sites; used to evaluate tumorigenicity, growth, and recurrence after surgery (rodriguezramirez2022p53inhibitsbmi1driven pages 1-3, aizawa2023establishmentofexperimental pages 1-2) | Tumor growth, recurrence modeling, validation of therapeutic interventions in a microenvironment closer to native salivary tissue | Orthotopic models were used to demonstrate recurrence-preventing effects of p53 activation and to confirm tumorigenicity of organoid-derived models (rodriguezramirez2022p53inhibitsbmi1driven pages 1-3, aizawa2023establishmentofexperimental pages 1-2) | (rodriguezramirez2022p53inhibitsbmi1driven pages 1-3, aizawa2023establishmentofexperimental pages 1-2) |
| Subcutaneous xenograft | **Subcutaneous MEC xenografts** | Standard in vivo transplantation model using MEC cell lines; enables longitudinal tumor growth measurements and therapeutic response evaluation (rodriguezramirez2022p53inhibitsbmi1driven pages 1-3, chen2021thecrtc1maml2fusion pages 1-2) | Drug efficacy studies, tumor maintenance dependency, recurrence biology | Used in both p53-activation studies and CRTC1-MAML2 knockdown studies to show reduced tumor growth and therapeutic vulnerability (rodriguezramirez2022p53inhibitsbmi1driven pages 1-3, chen2021thecrtc1maml2fusion pages 1-2) | (rodriguezramirez2022p53inhibitsbmi1driven pages 1-3, chen2021thecrtc1maml2fusion pages 1-2) |
| Genetically engineered mouse model (GEMM) | **Conditional CRTC1-MAML2 transgenic mouse** | Cre-inducible mouse engineered to express **CRTC1-MAML2**; produced salivary gland tumors with **100% penetrance** that resembled histologic and molecular characteristics of human MEC (chen2021thecrtc1maml2fusion pages 1-2) | Mechanistic dissection of tumor initiation, oncogenic driver validation, testing combination targeted therapy | Provided direct evidence that **CRTC1-MAML2 is a major oncogenic driver** of MEC; revealed cooperating dysregulation of the **p16-CDK4/6-RB** pathway and supported combined **palbociclib + erlotinib** therapy in vitro/in vivo (chen2021thecrtc1maml2fusion pages 1-2) | (chen2021thecrtc1maml2fusion pages 1-2) |
| Patient-derived organoid (PDO) | **MEC PDOs** | In Aizawa et al., one series of patient-derived MEC organoids was established from resected tumors; organoids maintained pathologic and genetic features of the source tumor and could be cryopreserved/recovered (aizawa2023establishmentofexperimental pages 1-2) | Ex vivo biology, personalized drug screening, preservation of subtype-specific fusion and expression features, organoid transplantation | MEC PDOs retained transcriptional profiles, genomic variants, and fusion genes, supporting organoid use as a clinically relevant preclinical platform (aizawa2023establishmentofexperimental pages 1-2) | (aizawa2023establishmentofexperimental pages 1-2) |
| PDX-derived organoid (PDXO) | **MEC PDXOs** | Organoids derived from established MEC PDXs; histologically and genetically similar to original tumors and paired PDXs (aizawa2023establishmentofexperimental pages 1-2) | Scalable ex vivo therapeutic testing, bridging in vivo and in vitro modeling, mechanistic studies | PDXOs preserved salient tumor traits and, together with PDXs/PDOs, form a linked platform for translational MEC research (aizawa2023establishmentofexperimental pages 1-2) | (aizawa2023establishmentofexperimental pages 1-2) |
| Organoid-transplanted animal model | **Orthotopic transplantation of MEC PDOs/PDXOs** | In vivo tumorigenicity assay using organoids implanted orthotopically; tests whether organoids can regenerate tumors resembling parent lesions (aizawa2023establishmentofexperimental pages 1-2) | Functional validation of organoids, tumorigenicity assessment, therapy testing in organoid-derived tumors | Orthotopic transplants from PDOs/PDXOs showed similar histological features as original MEC tumors, validating these models biologically (aizawa2023establishmentofexperimental pages 1-2) | (aizawa2023establishmentofexperimental pages 1-2) |
| Conditionally reprogrammed primary tumor cells | **CR models from primary tumor cells; proposed/used broadly for MEC-related research** | Feeder-cell plus ROCK-inhibitor system enabling rapid proliferation of primary epithelial tumor cells; review literature explicitly notes value for cancer biology, therapeutic target exploration, individualized drug screening, and improvement of patient-derived animal models; relevant to MEC cell growth applications (aizawa2023establishmentofexperimental pages 1-2) | Expansion of primary MEC cells, personalized testing, short-term translational assays, support for PDX development | CR systems are highlighted as a promising platform for studying tumor biology and drug response where classic models are limited; useful conceptually for rare tumors like MEC, though disease-specific standardization remains limited (aizawa2023establishmentofexperimental pages 1-2) | (aizawa2023establishmentofexperimental pages 1-2) |
| Molecularly defined preclinical combination-therapy model | **CRTC1-MAML2–driven MEC models treated with palbociclib + erlotinib** | Uses fusion-driven in vitro and in vivo MEC models, including xenografts and transgenic contexts, to interrogate pathway cooperation (chen2021thecrtc1maml2fusion pages 1-2) | Precision-therapy development, pathway cotargeting, proof-of-concept preclinical intervention | Cotargeting **AREG/EGFR** signaling and **CDK4/6-RB** signaling produced enhanced antitumor responses, identifying a rational combination strategy for MEC (chen2021thecrtc1maml2fusion pages 1-2) | (chen2021thecrtc1maml2fusion pages 1-2) |
| Recurrence model | **Post-resection recurrence model in murine MEC** | Follow-up after tumor resection for up to 250 days in murine MEC models; specifically designed to study disease recurrence (rodriguezramirez2022p53inhibitsbmi1driven pages 1-3) | Recurrence prevention studies, CSC-targeted interventions, longitudinal efficacy assessment | Therapeutic p53 activation prevented CSC-mediated tumor recurrence in preclinical trials, providing a rare disease-relevant recurrence model for MEC (rodriguezramirez2022p53inhibitsbmi1driven pages 1-3) | (rodriguezramirez2022p53inhibitsbmi1driven pages 1-3) |
| Other reported MEC cell line | **YD-15 MEC cells** | Mentioned in unobtainable later literature as a mucoepidermoid carcinoma cell model with enhanced tumor formation after intradermal injection in nude mice; detailed primary evidence was not available in retrieved contexts, so characterization remains limited here | Potential xenograft/tumor formation studies | Evidence in the retrieved corpus is insufficient for detailed annotation; include as a named model of interest requiring direct source confirmation before database use | (rodriguezramirez2022p53inhibitsbmi1driven pages 1-3) |


*Table: This table summarizes experimental models used to study mucoepidermoid carcinoma, spanning cell lines, xenografts, organoids, and engineered mice. It highlights what each model captures biologically and how each has been used for mechanistic or therapeutic research.*

### Key Model Systems

**Human Cell Lines:**
- **UM-HMC-1, UM-HMC-3A, UM-HMC-3B:** Established human MEC cell lines used for cancer stem cell biology, p53/MDM2 pathway studies, self-renewal assays, and xenograft generation (rodriguezramirez2022p53inhibitsbmi1driven pages 1-3)

**Genetically Engineered Mouse Model (GEMM):**
A conditional CRTC1-MAML2 transgenic mouse with Cre-inducible expression produced salivary gland tumors with 100% penetrance, providing direct evidence that CRTC1-MAML2 is a major oncogenic driver and enabling mechanistic studies and combination therapy testing (chen2021thecrtc1maml2fusion pages 1-2).

**Patient-Derived Models:**
- **PDX (Patient-Derived Xenografts):** MEC PDXs retain histologic features, transcription profiles, genomic variants, and fusion genes of original tumors (aizawa2023establishmentofexperimental pages 1-2)
- **PDO (Patient-Derived Organoids):** MEC organoids maintain pathologic and genetic features and support ex vivo drug screening (aizawa2023establishmentofexperimental pages 1-2)
- **PDXO (PDX-Derived Organoids):** Bridge in vivo and in vitro modeling (aizawa2023establishmentofexperimental pages 1-2)

**Phenotype Recapitulation:**
MEC models (PDX, PDO, transgenic mice) recapitulate histological features including the triad of mucous, intermediate, and squamous cells, as well as molecular characteristics including CRTC1-MAML2 fusion and cooperating pathway alterations (chen2021thecrtc1maml2fusion pages 1-2, aizawa2023establishmentofexperimental pages 1-2).

**Applications:**
Models are used for drug efficacy studies, CSC biology, recurrence mechanisms, target validation, personalized drug screening, and pathway cotargeting strategies (chen2021thecrtc1maml2fusion pages 1-2, aizawa2023establishmentofexperimental pages 1-2, rodriguezramirez2022p53inhibitsbmi1driven pages 1-3).

**Limitations:**
While MEC models capture key biological features, the rarity of the disease limits the number and diversity of available models. The literature did not extensively discuss aspects of human disease not captured by current models.

---

## SUMMARY

Mucoepidermoid carcinoma is the most common malignant salivary gland tumor, characterized by a heterogeneous cellular composition and variable clinical behavior. The t(11;19) translocation resulting in the CRTC1-MAML2 fusion is detected in up to 80% of cases and represents the major oncogenic driver, as demonstrated by 100% penetrant tumor formation in conditional transgenic mice. Cooperating alterations in the p16-CDK4/6-RB pathway and activation of AREG/EGFR signaling provide rational targets for combination therapy with palbociclib and erlotinib. High-grade tumors and those with specific cooperating mutations (e.g., TP53, FBXW7 with CRTC1::MAML2) have unfavorable prognoses. Surgical resection remains the primary treatment, with limited benefit from conventional chemotherapy. Emerging targeted therapies, p53-activating agents, and immunotherapy approaches (guided by TMB and PD-L1) offer promise. Comprehensive molecular profiling (FISH, NGS) is essential for diagnosis, differential diagnosis, and identification of actionable alterations. Experimental models including cell lines (UM-HMC series), patient-derived xenografts and organoids, and CRTC1-MAML2 transgenic mice provide robust platforms for mechanistic studies and therapeutic development.

---

## REFERENCES

All citations in this report correspond to retrieved paper contexts designated by identifiers (costa2024molecularaspectsof pages 1-3, rodriguezramirez2022p53inhibitsbmi1driven pages 1-3). Key references include:

- **pqac-00000000:** Costa et al. (2024). Molecular Aspects of Mucoepidermoid Carcinoma and Adenoid Cystic Carcinoma of the Salivary Gland. Head and Neck Pathology 18:34. DOI: 10.1007/s12105-024-01629-2
  
- **pqac-00000001:** Wang et al. (2024). The clinical outcome, pathologic spectrum, and genomic landscape for 454 cases of salivary mucoepidermoid carcinoma. NPJ Precision Oncology 8:238. DOI: 10.1038/s41698-024-00735-2

- **pqac-00000002:** Zerdan et al. (2023). Molecular Targets in Salivary Gland Cancers: A Comprehensive Genomic Analysis of 118 Mucoepidermoid Carcinoma Tumors. Biomedicines 11:519. DOI: 10.3390/biomedicines11020519

- **pqac-00000003:** Broseghini et al. (2025). Salivary Gland Cancers in the Era of Molecular Analysis: The Role of Tissue and Liquid Biomarkers. Cancers 17:660. DOI: 10.3390/cancers17040660

- **pqac-00000004:** Roden (2023). The Role of Gene Fusions in Thymic Epithelial Tumors. Cancers 15:5596. DOI: 10.3390/cancers15235596

- **pqac-00000005:** Ge et al. (2024). Genomics and tumor microenvironment of breast mucoepidermoid carcinoma based on whole-exome and RNA sequencing. Diagnostic Pathology 19:15. DOI: 10.1186/s13000-024-01439-8

- **pqac-00000008:** Chen et al. (2021). The CRTC1-MAML2 fusion is the major oncogenic driver in mucoepidermoid carcinoma. JCI Insight 6(7):e139497. DOI: 10.1172/jci.insight.139497

- **pqac-00000009:** Aizawa et al. (2023). Establishment of experimental salivary gland cancer models using organoid culture and patient-derived xenografting. Cellular Oncology 46:409–421. DOI: 10.1007/s13402-022-00758-6

- **pqac-00000011:** Vrinceanu et al. (2024). Parotid Gland Tumors: Molecular Diagnostic Approaches. International Journal of Molecular Sciences 25:7350. DOI: 10.3390/ijms25137350

- **pqac-00000013:** Zou et al. (2025). Systematic identification of pathological mechanisms, prognostic biomarkers and therapeutic targets by integrating lncRNA expression variation in salivary gland mucoepidermoid carcinoma. Scientific Reports 15:1573. DOI: 10.1038/s41598-025-85535-9

- **pqac-00000014:** Rodriguez-Ramirez et al. (2022). p53 inhibits Bmi-1-driven self-renewal and defines salivary gland cancer stemness. Clinical Cancer Research 28(21):4757–4770. DOI: 10.1158/1078-0432.CCR-22-1357

References

1. (costa2024molecularaspectsof pages 1-3): Raisa Ferreira Costa, Carolinne Alves de Oliveira, Ágatha Nagli de Mello Gomes, Silvia Vanessa Lourenço, and Cláudia Malheiros Coutinho-Camillo. Molecular aspects of mucoepidermoid carcinoma and adenoid cystic carcinoma of the salivary gland. Head and neck pathology, 18 1:34, Apr 2024. URL: https://doi.org/10.1007/s12105-024-01629-2, doi:10.1007/s12105-024-01629-2. This article has 12 citations and is from a peer-reviewed journal.

2. (wang2024theclinicaloutcome pages 1-2): Xi Wang, Jiaying Bai, Jing Yan, and Binbin Li. The clinical outcome, pathologic spectrum, and genomic landscape for 454 cases of salivary mucoepidermoid carcinoma. NPJ Precision Oncology, Oct 2024. URL: https://doi.org/10.1038/s41698-024-00735-2, doi:10.1038/s41698-024-00735-2. This article has 17 citations and is from a peer-reviewed journal.

3. (chen2021thecrtc1maml2fusion pages 1-2): Zirong Chen, Wei Ni, Jian-Liang Li, Shuibin Lin, Xin Zhou, Yuping Sun, Jennifer W. Li, Marino E. Leon, Maria D. Hurtado, Sergei Zolotukhin, Chen Liu, Jianrong Lu, James D. Griffin, Frederic J. Kaye, and Lizi Wu. The crtc1-maml2 fusion is the major oncogenic driver in mucoepidermoid carcinoma. JCI Insight, Apr 2021. URL: https://doi.org/10.1172/jci.insight.139497, doi:10.1172/jci.insight.139497. This article has 78 citations and is from a domain leading peer-reviewed journal.

4. (broseghini2025salivaryglandcancers pages 1-2): Elisabetta Broseghini, Francesca Carosi, Mirea Berti, Samuele Compagno, Anna Ghelardini, Matteo Fermi, Giulia Querzoli, and Daria Maria Filippini. Salivary gland cancers in the era of molecular analysis: the role of tissue and liquid biomarkers. Cancers, 17:660, Feb 2025. URL: https://doi.org/10.3390/cancers17040660, doi:10.3390/cancers17040660. This article has 15 citations.

5. (zerdan2023moleculartargetsin pages 1-2): Maroun Bou Zerdan, Prashanth Ashok Kumar, Daniel Zaccarini, Jeffrey Ross, Richard Huang, and Abirami Sivapiragasam. Molecular targets in salivary gland cancers: a comprehensive genomic analysis of 118 mucoepidermoid carcinoma tumors. Biomedicines, 11:519, Feb 2023. URL: https://doi.org/10.3390/biomedicines11020519, doi:10.3390/biomedicines11020519. This article has 22 citations.

6. (wang2024theclinicaloutcome pages 2-3): Xi Wang, Jiaying Bai, Jing Yan, and Binbin Li. The clinical outcome, pathologic spectrum, and genomic landscape for 454 cases of salivary mucoepidermoid carcinoma. NPJ Precision Oncology, Oct 2024. URL: https://doi.org/10.1038/s41698-024-00735-2, doi:10.1038/s41698-024-00735-2. This article has 17 citations and is from a peer-reviewed journal.

7. (wang2024theclinicaloutcome pages 3-4): Xi Wang, Jiaying Bai, Jing Yan, and Binbin Li. The clinical outcome, pathologic spectrum, and genomic landscape for 454 cases of salivary mucoepidermoid carcinoma. NPJ Precision Oncology, Oct 2024. URL: https://doi.org/10.1038/s41698-024-00735-2, doi:10.1038/s41698-024-00735-2. This article has 17 citations and is from a peer-reviewed journal.

8. (ge2024genomicsandtumor pages 1-2): Yan Ge, Xingtao Lin, Jiao He, Wendan Chen, Danyi Lin, Yihong Zheng, Lingling Yang, Fangping Xu, and Zhi Li. Genomics and tumor microenvironment of breast mucoepidermoid carcinoma based on whole-exome and rna sequencing. Diagnostic Pathology, Jan 2024. URL: https://doi.org/10.1186/s13000-024-01439-8, doi:10.1186/s13000-024-01439-8. This article has 5 citations and is from a peer-reviewed journal.

9. (vrinceanu2024parotidglandtumors pages 1-2): Daniela Vrinceanu, Mihai Dumitru, Miruna Bratiloveanu, Andreea Marinescu, Crenguta Serboiu, Felicia Manole, Dragos Octavian Palade, Adrian Costache, Mariana Costache, and Oana Patrascu. Parotid gland tumors: molecular diagnostic approaches. International Journal of Molecular Sciences, 25:7350, Jul 2024. URL: https://doi.org/10.3390/ijms25137350, doi:10.3390/ijms25137350. This article has 17 citations.

10. (zerdan2023moleculartargetsin pages 2-4): Maroun Bou Zerdan, Prashanth Ashok Kumar, Daniel Zaccarini, Jeffrey Ross, Richard Huang, and Abirami Sivapiragasam. Molecular targets in salivary gland cancers: a comprehensive genomic analysis of 118 mucoepidermoid carcinoma tumors. Biomedicines, 11:519, Feb 2023. URL: https://doi.org/10.3390/biomedicines11020519, doi:10.3390/biomedicines11020519. This article has 22 citations.

11. (rodriguezramirez2022p53inhibitsbmi1driven pages 1-3): Christie Rodriguez-Ramirez, Zhaocheng Zhang, Kristy A. Warner, Alexandra E. Herzog, Andrea Mantesso, Zhixiong Zhang, Eusik Yoon, Shaomeng Wang, Max S. Wicha, and Jacques E. Nör. P53 inhibits bmi-1-driven self-renewal and defines salivary gland cancer stemness. Clinical cancer research : an official journal of the American Association for Cancer Research, 28:4757-4770, Sep 2022. URL: https://doi.org/10.1158/1078-0432.ccr-22-1357, doi:10.1158/1078-0432.ccr-22-1357. This article has 17 citations.

12. (zou2025systematicidentificationof pages 1-2): Yan-ping Zou, Xiao-feng Shan, Jia-xuan Qiu, Yan Geng, Shang Xie, Ruo-lan Xiang, and Zhi-gang Cai. Systematic identification of pathological mechanisms, prognostic biomarkers and therapeutic targets by integrating lncrna expression variation in salivary gland mucoepidermoid carcinoma. Scientific Reports, Jan 2025. URL: https://doi.org/10.1038/s41598-025-85535-9, doi:10.1038/s41598-025-85535-9. This article has 5 citations and is from a peer-reviewed journal.

13. (costa2024molecularaspectsof pages 3-5): Raisa Ferreira Costa, Carolinne Alves de Oliveira, Ágatha Nagli de Mello Gomes, Silvia Vanessa Lourenço, and Cláudia Malheiros Coutinho-Camillo. Molecular aspects of mucoepidermoid carcinoma and adenoid cystic carcinoma of the salivary gland. Head and neck pathology, 18 1:34, Apr 2024. URL: https://doi.org/10.1007/s12105-024-01629-2, doi:10.1007/s12105-024-01629-2. This article has 12 citations and is from a peer-reviewed journal.

14. (roden2023theroleof pages 1-2): Anja C. Roden. The role of gene fusions in thymic epithelial tumors. Cancers, 15:5596, Nov 2023. URL: https://doi.org/10.3390/cancers15235596, doi:10.3390/cancers15235596. This article has 7 citations.

15. (aizawa2023establishmentofexperimental pages 1-2): Yoshihiro Aizawa, Kentaro Takada, Jun Aoyama, Daisuke Sano, Shoji Yamanaka, Masahide Seki, Yuta Kuze, Jordan A. Ramilowski, Ryo Okuda, Yasuharu Ueno, Yusuke Nojima, Yoshiaki Inayama, Hiromitsu Hatakeyama, Takashi Hatano, Hideaki Takahashi, Goshi Nishimura, Satoshi Fujii, Yutaka Suzuki, Hideki Taniguchi, and Nobuhiko Oridate. Establishment of experimental salivary gland cancer models using organoid culture and patient-derived xenografting. Cellular Oncology (Dordrecht), 46:409-421, Dec 2023. URL: https://doi.org/10.1007/s13402-022-00758-6, doi:10.1007/s13402-022-00758-6. This article has 15 citations.

## Artifacts

- [Edison artifact artifact-00](Mucoepidermoid_Carcinoma-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](Mucoepidermoid_Carcinoma-deep-research-falcon_artifacts/artifact-01.md)