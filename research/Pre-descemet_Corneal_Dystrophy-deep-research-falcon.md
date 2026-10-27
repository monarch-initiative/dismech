---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-25T18:55:52.195380'
end_time: '2026-08-25T19:05:20.383526'
duration_seconds: 568.19
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Pre-Descemet Corneal Dystrophy
  mondo_id: ''
  category: Genetic
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 21
reference_validation:
  total_references: 5
  verified: 5
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 2
  quotes_valid: 2
  relevance_assessed: 5
  on_topic: 1
  validator_version: 0.2.1
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Pre-descemet_Corneal_Dystrophy-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Pre-Descemet Corneal Dystrophy
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Pre-Descemet Corneal Dystrophy** covering all of the
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
- **Disease Name:** Pre-Descemet Corneal Dystrophy
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Pre-Descemet Corneal Dystrophy** covering all of the
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


# Pre-Descemet Corneal Dystrophy: Disease Characteristics Report

**Scope note.** “Pre-Descemet corneal dystrophy” (PDCD) is not one genetically uniform disorder. The 2024 International Committee for Classification of Corneal Dystrophies (IC3D) separates poorly defined, usually sporadic PDCD/cornea farinata-like disease (**category 4**) from **punctiform and polychromatic pre-Descemet corneal dystrophy (PPPCD)**, a genetically supported autosomal-dominant disorder caused by **PRDX3** variants (**category 1**). Similar deposits can also occur as a manifestation of **STS deficiency/X-linked ichthyosis**. These entities should not be merged without qualification in a knowledge base. (weiss2024ic3dclassificationof pages 48-49, weiss2024ic3dclassificationof pages 11-12)

| Entity/status | Inheritance / gene / variant | Hallmark phenotype and course | Strongest evidence / sample | Mechanism confidence | Management | Major gaps |
|---|---|---|---|---|---|---|
| Isolated/classic pre-Descemet corneal dystrophy (PDCD), historically overlapping with cornea farinata; IC3D 2024 treats PDCDs as a group and notes isolated PDCD remains poorly defined / category 4 | No established causal gene for isolated PDCD. Usually sporadic in modern imaging series; heredity unclear. IC3D notes prior overlap with cornea farinata/deep filiform/deep punctiform labels. DOI: https://doi.org/10.1097/ICO.0000000000003420 (2024); https://doi.org/10.1177/1120672119862505 (2020) (weiss2024ic3dclassificationof pages 48-49, alafaleq2020multimodalimagingof pages 1-2, alafaleq2020multimodalimagingof pages 4-6) | Bilateral tiny gray/polymorphic punctiform opacities immediately anterior to Descemet membrane; generally asymptomatic with vision usually unaffected; nonprogressive to slowly progressive. Multimodal imaging suggests deposits throughout the stroma, maximal posteriorly. DOI: https://doi.org/10.1097/ICO.0000000000003420 (2024); https://doi.org/10.1177/1120672119862505 (2020) (weiss2024ic3dclassificationof pages 48-49, alafaleq2020multimodalimagingof pages 1-2, alafaleq2020multimodalimagingof pages 6-9) | IC3D expert synthesis plus retrospective multimodal case series of 8 corneas from 4 unrelated male patients with bilateral disease; SD-OCT showed hyperreflective line anterior to Descemet membrane and IVCM showed extracellular stromal deposits plus enlarged posterior keratocytes. DOI: https://doi.org/10.1097/ICO.0000000000003420 (2024); https://doi.org/10.1177/1120672119862505 (2020) (weiss2024ic3dclassificationof pages 48-49, alafaleq2020multimodalimagingof pages 1-2, alafaleq2020multimodalimagingof pages 2-4) | Moderate for a keratocyte-centered degenerative/deposition process; low for a single molecular cause. Evidence includes ultrastructural vacuoles with electron-dense/lipofuscin-like material and imaging evidence of stromal, not epithelial/endothelial, involvement. DOI: https://doi.org/10.1177/1120672119862505 (2020); https://doi.org/10.1097/ICO.0000000000003420 (2024) (weiss2024ic3dclassificationof pages 48-49, alafaleq2020multimodalimagingof pages 6-9, alafaleq2020multimodalimagingof pages 4-6) | Usually observation/follow-up because vision is typically preserved; diagnosis supported by slit-lamp, IVCM, and anterior-segment OCT. No disease-specific therapy or trial identified. DOI: https://doi.org/10.1177/1120672119862505 (2020); https://doi.org/10.1097/ICO.0000000000003420 (2024) (weiss2024ic3dclassificationof pages 48-49, alafaleq2020multimodalimagingof pages 6-9) | No prevalence/incidence estimates specific to isolated PDCD; no validated gene; little natural-history data; no penetrance estimates; no biomarker, trial, or pathology-standardized management pathway. Distinction from cornea farinata and secondary/systemic causes remains imperfect. (weiss2024ic3dclassificationof pages 48-49, alafaleq2020multimodalimagingof pages 6-9, alafaleq2020multimodalimagingof pages 4-6) |
| Punctiform and polychromatic pre-Descemet corneal dystrophy (PPPCD); genetically supported distinct subtype; IC3D category 1 in 2024 | Autosomal dominant; PRDX3 is the leading causal gene. Recurrent heterozygous PRDX3 c.568G>C (p.Asp190His) identified in 4 of 5 reported families in the 2020 genetic study; PDZD8 c.872+10A>T segregated in 3 of 5 families but was not favored as the main cause. DOI: https://doi.org/10.1016/j.ajo.2019.11.024 (2020); https://doi.org/10.1097/ICO.0000000000003420 (2024) (barrio2020punctiformandpolychromatic pages 1-8, barrio2020punctiformandpolychromatic pages 17-21, barrio2020punctiformandpolychromatic pages 26-30, weiss2024ic3dclassificationof pages 11-12) | Posterior stromal/pre-Descemetic multicolored polychromatic punctiform opacities, usually bilateral; typically asymptomatic and without visual disturbance; cases reported from childhood to late adulthood, often nonprogressive or only mildly progressive. DOI: https://doi.org/10.1016/j.ajo.2019.11.024 (2020); https://doi.org/10.1097/ICO.0000000000003420 (2024) (barrio2020punctiformandpolychromatic pages 1-8, weiss2024ic3dclassificationof pages 48-49, barrio2020punctiformandpolychromatic pages 12-17) | Strongest evidence is the 2020 family-based study: 12 affected individuals from 3 previously unreported families within a larger set of 5 PPPCD families; segregation plus recurrence of PRDX3 p.Asp190His across families. Imaging showed hyperreflective posterior stromal/Descemet-level opacities; only measured biomechanical abnormality was increased corneal stiffness. DOI: https://doi.org/10.1016/j.ajo.2019.11.024 (2020) (barrio2020punctiformandpolychromatic pages 1-8, barrio2020punctiformandpolychromatic pages 17-21, barrio2020punctiformandpolychromatic pages 26-30) | High confidence for a gene-disease relationship relative to other PDCD forms; moderate confidence for mechanism. PRDX3 encodes a mitochondrial antioxidant peroxidase regulating mitochondrial reactive oxygen species, but direct human corneal molecular profiling remains sparse. DOI: https://doi.org/10.1016/j.ajo.2019.11.024 (2020); https://doi.org/10.1097/ICO.0000000000003420 (2024) (barrio2020punctiformandpolychromatic pages 17-21, weiss2024ic3dclassificationof pages 11-12) | Observation and follow-up are usual because visual function is largely preserved; genetic counseling is reasonable given autosomal-dominant inheritance. No targeted therapy or registered clinical trial found. DOI: https://doi.org/10.1016/j.ajo.2019.11.024 (2020); https://doi.org/10.1097/ICO.0000000000003420 (2024) (barrio2020punctiformandpolychromatic pages 1-8, weiss2024ic3dclassificationof pages 48-49) | Extremely small literature base (about 10 families before 2020); prevalence unknown; penetrance and expressivity incompletely quantified; possible locus heterogeneity remains unresolved; uncertain whether extra-corneal crystals in isolated reports indicate a broader systemic process in some families. (barrio2020punctiformandpolychromatic pages 1-8, weiss2024ic3dclassificationof pages 11-12) |
| STS/X-linked ichthyosis-associated pre-Descemet opacities; better viewed as syndromic/secondary pre-Descemet corneal changes rather than primary isolated dystrophy | X-linked recessive STS deficiency. Case report demonstrated complete deletion of all 10 STS exons and flanking sequence failure by PCR in a 34-year-old man with known X-linked ichthyosis. DOI: https://doi.org/10.1186/s12886-017-0423-5 (2017) (shi2017invivoconfocal pages 4-5, shi2017invivoconfocal pages 1-2, shi2017invivoconfocal pages 2-4) | Bilateral tiny pleomorphic gray-brownish posterior stromal opacities anterior to Descemet membrane, with preserved corrected visual acuity (20/20 both eyes after refraction in the reported case); skin dryness/scaling from infancy; stable over 1 year in the published case. DOI: https://doi.org/10.1186/s12886-017-0423-5 (2017) (shi2017invivoconfocal pages 1-2, shi2017invivoconfocal pages 2-4) | Single detailed human case report with slit-lamp, IVCM, dermatologic exam, and molecular confirmation of STS deletion. IVCM showed enlarged activated posterior stromal keratocytes containing regularly distributed hyperreflective particles and additional anterior stromal particles; endothelial cell density remained normal. DOI: https://doi.org/10.1186/s12886-017-0423-5 (2017) (shi2017invivoconfocal pages 4-5, shi2017invivoconfocal pages 1-2, shi2017invivoconfocal pages 2-4) | Moderate for a secondary metabolic/deposition mechanism: authors proposed STS deficiency elevates cholesterol sulfate, causing lysosomal dysfunction and lipid accumulation in keratocytes; however this is based mainly on clinicopathologic inference and one genetically confirmed case. DOI: https://doi.org/10.1186/s12886-017-0423-5 (2017) (shi2017invivoconfocal pages 4-5, shi2017invivoconfocal pages 2-4) | Management centers on recognition of the ocular finding within X-linked ichthyosis, observation, and systemic/genetic counseling; no cornea-specific intervention was needed in the reported case. DOI: https://doi.org/10.1186/s12886-017-0423-5 (2017) (shi2017invivoconfocal pages 4-5, shi2017invivoconfocal pages 1-2) | Evidence limited to isolated cases; unclear prevalence among STS-deficient patients; natural history and treatment thresholds unknown; uncertain whether this should be classified with primary corneal dystrophies or as a manifestation of systemic disease. (weiss2024ic3dclassificationof pages 48-49, shi2017invivoconfocal pages 4-5, shi2017invivoconfocal pages 2-4) |


*Table: This table contrasts the main evidence-supported forms of pre-Descemet corneal disease: poorly defined isolated PDCD, PRDX3-associated PPPCD, and STS/X-linked ichthyosis-associated pre-Descemet opacities. It summarizes what is established, what is inferred, and where major evidence gaps remain.*

## 1. Disease information

PDCD denotes bilateral, generally noninflammatory deposits in the deep corneal stroma immediately anterior to Descemet membrane. The classic appearance is numerous fine, gray, polymorphic opacities; PPPCD has larger punctiform opacities with a distinctive multicolored or polychromatic appearance. Vision is usually preserved. IC3D describes isolated PDCD as neither a well-defined hereditary dystrophy nor an unequivocal degeneration, whereas PRDX3-associated PPPCD now meets category-1 criteria. (weiss2024ic3dclassificationof pages 48-49, weiss2024ic3dclassificationof pages 11-12)

**Names and synonyms:** pre-Descemet corneal dystrophy; pre-Descemet’s membrane corneal dystrophy; deep filiform dystrophy; deep punctiform dystrophy; cornea farinata (historically overlapping, but now better regarded as a degeneration); punctiform and polychromatic pre-Descemet corneal dystrophy; posterior polychromatic corneal dystrophy. (weiss2024ic3dclassificationof pages 48-49)

**Identifiers:** no confidently validated disease-specific OMIM, Orphanet, MONDO, MeSH, ICD-10, or ICD-11 identifier was established in the retrieved authoritative literature. A knowledge base should therefore retain the label as an IC3D entity and avoid assigning an unverified MONDO ID. Generic coding may fall under corneal dystrophy or corneal opacity, but that is not disease-specific.

The evidence is aggregated disease-level literature—IC3D expert classification, family studies, and small case series—not individual EHR data. The core sources are IC3D Edition 3, published February 2024 ([DOI](https://doi.org/10.1097/ico.0000000000003420)), and the family/genetic study published April 2020 ([DOI](https://doi.org/10.1016/j.ajo.2019.11.024)). PMIDs were not exposed in the retrieved records and should be verified directly in PubMed before database deposition. (barrio2020punctiformandpolychromatic pages 1-8, weiss2024ic3dclassificationof pages 48-49)

## 2. Etiology and risk/protective factors

### Genetic causes

* **PPPCD:** heterozygous **PRDX3 NM_006793.4:c.568G>C, p.(Asp190His)** is the principal reported causal variant. It segregated with disease and was found in four of five evaluated families. Autosomal-dominant transmission is supported. (barrio2020punctiformandpolychromatic pages 17-21, barrio2020punctiformandpolychromatic pages 26-30)
* A rare intronic **PDZD8 c.872+10A>T** variant segregated in three of five families, but PRDX3 was favored as the causal gene. Possible locus heterogeneity remains unresolved. (barrio2020punctiformandpolychromatic pages 1-8, barrio2020punctiformandpolychromatic pages 17-21)
* **Isolated nonpolychromatic PDCD:** no locus or causal gene is established; modern series are often sporadic. (weiss2024ic3dclassificationof pages 48-49, alafaleq2020multimodalimagingof pages 1-2)
* **Syndromic pre-Descemet opacities:** complete deletion of **STS** was demonstrated in a man with X-linked ichthyosis. This is better annotated as a secondary ocular manifestation of STS deficiency than as PRDX3-associated PPPCD. (shi2017invivoconfocal pages 1-2, shi2017invivoconfocal pages 2-4)

Family history is the principal recognized risk indicator for PPPCD. Cases in the genetic series ranged from 8 to 79 years, showing that detectable disease may span much of life. Geographic clustering among Spanish/Spanish-ancestry and Brazilian families was observed, but the sample is too small to establish a founder effect or population-specific risk. (barrio2020punctiformandpolychromatic pages 17-21, barrio2020punctiformandpolychromatic pages 12-17)

### Environmental, lifestyle, infectious, and protective factors

No reproducible toxin, diet, smoking, alcohol, occupational, infectious, or lifestyle cause has been demonstrated. No protective allele, diet, medication, or behavioral intervention is known. Age may affect detectability—classic PDCD is usually recognized after age 30—but PPPCD has been seen by age 3, so age is not a causal exposure. No validated gene–environment interaction exists. (weiss2024ic3dclassificationof pages 48-49)

A report proposing vaccine/surgical stimulation in a person with an ARSG variant is insufficient to establish causation and should not be treated as a recognized PDCD risk factor.

## 3. Phenotypes

| Phenotype | Type and characteristics | Suggested HPO annotation |
|---|---|---|
| Deep stromal corneal opacities | Objective sign; bilateral fine gray/polymorphic deposits immediately anterior to Descemet membrane, usually extending broadly across the cornea | **Corneal opacity, HP:0007957**; bilateral qualifier; posterior/deep stromal location as free-text qualifier |
| Polychromatic punctiform deposits | PPPCD-defining sign; multicolored punctate posterior stromal opacities | Corneal opacity (HP:0007957), punctate/polychromatic morphology qualifier |
| Preserved visual acuity/asymptomatic state | Most common clinical state; one IC3D-cited patient reported glare | “Asymptomatic” should be represented as absence of symptoms rather than a positive HPO phenotype |
| Glare | Rare symptom; frequency cannot be estimated | Glare/photophobia concept if locally supported; do not infer photophobia from glare alone |
| Increased corneal stiffness | Quantitative biomechanical abnormality in the 2020 family study; clinical significance uncertain | No validated disease-specific HPO mapping identified |
| X-linked ichthyosis features | Syndromic STS cases may have generalized dry, coarse, scaling skin | Annotate under X-linked ichthyosis, not primary PPPCD |

PPPCD is typically mild, bilateral, asymptomatic, and nonprogressive or only mildly progressive. Other PDCD/cornea-farinata-like forms may progress slowly. Onset is commonly recognized in adulthood, but childhood PPPCD is documented. No reliable phenotype frequencies beyond “usually” or “typically” are available because published cohorts are extremely small. (weiss2024ic3dclassificationof pages 48-49, barrio2020punctiformandpolychromatic pages 1-8)

No validated EQ-5D, SF-36, PROMIS, or vision-related quality-of-life study exists. Since corrected acuity is generally normal, everyday functional impact is expected to be minimal, although glare or diagnostic anxiety may matter in individual patients. This is clinical inference rather than measured evidence.

## 4. Genetic and molecular information

**PRDX3** encodes mitochondrial peroxiredoxin-3, an antioxidant peroxidase that regulates mitochondrial reactive oxygen species. The recurrent p.Asp190His substitution was novel in the 2020 study, predicted damaging, and had a CADD score of 31. The retrieved record did not provide a defensible ClinVar classification or current gnomAD allele frequency; therefore “pathogenic” should be used only in the disease-association sense supported by segregation and IC3D category 1, not asserted as a current ClinVar/ACMG record without database verification. (barrio2020punctiformandpolychromatic pages 17-21, barrio2020punctiformandpolychromatic pages 12-17)

The variant is germline, heterozygous, and missense. A dominant-negative versus gain-of-function versus haploinsufficiency mechanism has not been experimentally established. No modifier gene, protective allele, chromosomal rearrangement, somatic mutation, methylation signature, histone change, or other disease-specific epigenetic mechanism is known. The PDZD8 intronic allele remains a candidate rather than a confirmed independent cause. (barrio2020punctiformandpolychromatic pages 1-8, barrio2020punctiformandpolychromatic pages 17-21)

For STS-associated disease, the reported lesion was a germline X-chromosomal deletion encompassing all ten exons and flanking sequence. In the reported male it produced the expected X-linked hemizygous deficiency. (shi2017invivoconfocal pages 1-2, shi2017invivoconfocal pages 2-4)

## 5. Environmental information

PDCD/PPPCD is not infectious and is not linked to pollution, radiation, smoking, diet, exercise, alcohol, or occupational exposure. Important acquired mimics include crystalline keratopathy and occupational corneal deposits such as argyrosis; these are differential diagnoses, not proven triggers of inherited PPPCD. No environmental prevention strategy is supported.

## 6. Mechanism and pathophysiology

### PRDX3-associated PPPCD

A biologically plausible chain is:

**germline PRDX3 p.Asp190His → altered mitochondrial peroxide handling in corneal keratocytes → oxidative/proteostatic stress → intracellular and extracellular deposit formation, greatest in posterior stroma → punctiform polychromatic slit-lamp opacities.**

The first step—gene association—is strong; the downstream oxidative/deposition chain is plausible but not directly demonstrated by corneal transcriptomics, proteomics, metabolomics, or functional editing studies. (barrio2020punctiformandpolychromatic pages 17-21, weiss2024ic3dclassificationof pages 11-12)

### Sporadic/classic PDCD

IVCM and ultrastructure support a keratocyte-centered degenerative process. Enlarged posterior keratocytes contain membrane-bound vacuoles with electron-dense, lipofuscin-like material; extracellular particles occur throughout the stroma, with maximal damage anterior to Descemet membrane. Epithelium and endothelium are largely spared. (alafaleq2020multimodalimagingof pages 1-2, alafaleq2020multimodalimagingof pages 6-9, alafaleq2020multimodalimagingof pages 4-6)

The 2020 multimodal study’s abstract concluded that findings were “**in favor of a degenerative process affecting corneal keratocytes with no epithelial or endothelial involvement**.” It also reported that imaging “**reveals that the disorder affects the whole stroma**.” ([DOI](https://doi.org/10.1177/1120672119862505), September 2020). (alafaleq2020multimodalimagingof pages 1-2)

### STS-associated mechanism

A proposed chain is:

**STS deletion → steroid sulfatase deficiency → cholesterol-sulfate accumulation → lysosomal dysfunction/lipid retention in keratocytes → intracellular hyperreflective particles and posterior stromal opacity.**

This mechanism is supported by biochemical plausibility and one genetically confirmed clinical case, not by direct human corneal metabolomics. (shi2017invivoconfocal pages 4-5, shi2017invivoconfocal pages 2-4)

**Suggested ontology terms:** corneal stromal keratocyte (CL term should be curator-verified); corneal stroma and posterior corneal stroma (UBERON); mitochondrion (**GO:0005739**); lysosome (**GO:0005764**); response to oxidative stress (**GO:0006979**); reactive oxygen species metabolic process (**GO:0072593**); lipid storage/lysosomal organization as provisional biological-process annotations. No immune, inflammatory, ischemic, necrotic, or fibrotic mechanism is established.

No disease-specific bulk/single-cell RNA-seq, spatial transcriptomics, proteomics, metabolomics, lipidomics, multi-omics integration, CRISPR screen, or organoid study was found.

## 7. Anatomical structures affected

The disease is restricted predominantly to the **cornea**, especially the deep/posterior stroma immediately anterior to Descemet membrane. Imaging shows lesser deposits and activated keratocytes across anterior and middle stroma as well. Corneal epithelial thickness, Descemet membrane, endothelium, and central corneal thickness are generally normal. (alafaleq2020multimodalimagingof pages 2-4, alafaleq2020multimodalimagingof pages 6-9)

The target cell is the **corneal stromal keratocyte**. Relevant compartments include mitochondria for PRDX3 biology and lysosomal/vacuolar compartments for lipofuscin-like storage. Disease is typically bilateral and broadly distributed, often limbus-to-limbus, although one STS case retained a 2–3-mm clear perilimbal zone. (shi2017invivoconfocal pages 1-2, alafaleq2020multimodalimagingof pages 2-4)

Suggested anatomy annotations are cornea (**UBERON:0000964**), corneal stroma, Descemet membrane as an adjacency landmark, and bilateral eye involvement. No established secondary-organ involvement exists in isolated PPPCD; skin involvement belongs to syndromic STS deficiency. IC3D notes a report of crystals under the lens capsule, leaving open whether rare PPPCD may occasionally be systemic. (weiss2024ic3dclassificationof pages 11-12)

## 8. Temporal development

Classic PDCD is most often recognized after age 30 and develops insidiously. PPPCD can be detected in early childhood and has been documented across ages 3–79. In the 2020 family cohort, affected individuals were 8–79 years old, with mean age 42.9 years. (weiss2024ic3dclassificationof pages 48-49, barrio2020punctiformandpolychromatic pages 12-17)

There is no validated staging system. A practical descriptive sequence is: subclinical deposits detectable by IVCM/OCT; visible punctiform posterior stromal deposits; stable or mildly increasing deposit burden. End-stage corneal decompensation is not characteristic. One STS-associated case remained unchanged at one year. (weiss2024ic3dclassificationof pages 48-49, shi2017invivoconfocal pages 1-2)

The condition is chronic/lifelong once present. Spontaneous remission, relapsing-remitting behavior, critical treatment windows, and treatment-induced remission have not been documented.

## 9. Inheritance and population

PPPCD follows autosomal-dominant inheritance. Penetrance appears substantial in reported pedigrees but has not been quantified; age-dependent ascertainment is possible. Expressivity is variable in deposit burden, age of recognition, and occasional glare, but visual function is usually preserved. Anticipation, germline mosaicism, consanguinity effects, carrier frequency, and sex bias are unknown. (barrio2020punctiformandpolychromatic pages 1-8, weiss2024ic3dclassificationof pages 48-49)

Only about ten families had been reported before the 2020 study. That study evaluated 21 relatives from three additional families, including 12 affected individuals. These counts demonstrate extreme rarity but cannot yield prevalence or incidence. No population-based rate per 100,000 is available. (barrio2020punctiformandpolychromatic pages 1-8)

Spanish/Spanish-ancestry and Brazilian clustering is reported, but founder status has not been established. Both sexes can be affected in autosomal-dominant PPPCD. The male predominance in one four-patient sporadic imaging series cannot establish a sex ratio. (barrio2020punctiformandpolychromatic pages 17-21, alafaleq2020multimodalimagingof pages 1-2)

## 10. Diagnostics

### Clinical and imaging approach

1. **Slit-lamp biomicroscopy:** identify bilateral, fine gray or polychromatic punctiform deposits in posterior stroma immediately anterior to Descemet membrane.
2. **Anterior-segment OCT:** look for hyperreflective particles/line anterior to Descemet membrane; isolated PDCD may also show a thinner line below Bowman layer and particles through the stroma.
3. **In-vivo confocal microscopy:** demonstrate hyperreflective intracellular inclusions in enlarged posterior keratocytes and extracellular stromal deposits; assess preservation of epithelium and endothelium.
4. **Scheimpflug densitometry/specular microscopy:** supportive but not independently diagnostic.
5. **Visual acuity, refraction, pachymetry, and endothelial cell density:** document preserved function and exclude endothelial disease. (barrio2020punctiformandpolychromatic pages 26-30, shi2017invivoconfocal pages 1-2, alafaleq2020multimodalimagingof pages 2-4)

In the STS-associated case, corrected acuity reached 20/20 in both eyes and endothelial densities were 3,347 and 3,095 cells/mm². IVCM localized 2.0–3.4-µm particles within posterior keratocytes at 321–494 µm depth. (shi2017invivoconfocal pages 1-2)

### Genetic testing

For a convincing polychromatic familial phenotype, sequence **PRDX3**, preferably through an inherited corneal-dystrophy panel with deletion/duplication analysis and segregation testing. Targeted testing for c.568G>C is efficient in a known family. WES/WGS is appropriate when PRDX3 testing is negative, the phenotype is atypical, or syndromic findings suggest another diagnosis. In males with ichthyosis, test **STS** by copy-number analysis plus sequencing. CMA may detect a larger Xp22.3 deletion. Karyotyping, FISH, mitochondrial DNA testing, and repeat-expansion assays have no routine role unless another clinical indication exists. (barrio2020punctiformandpolychromatic pages 1-8, shi2017invivoconfocal pages 2-4)

### Differential diagnosis

Important alternatives are cornea farinata; fleck corneal dystrophy; central cloudy dystrophy of François; posterior amorphous corneal dystrophy; Fuchs endothelial corneal dystrophy/cornea guttata; posterior polymorphous corneal dystrophy; crystalline infectious keratopathy; Schnyder corneal dystrophy; cystinosis; drug/toxin or silver deposits; and pre-Descemet opacities secondary to X-linked ichthyosis. Normal endothelium, lack of edema/inflammation, posterior stromal keratocyte localization, polychromasia, and PRDX3 segregation favor PPPCD. (alafaleq2020multimodalimagingof pages 6-9)

There are no universally validated numerical diagnostic criteria. Asymptomatic relatives in a PRDX3-positive family can undergo cascade slit-lamp examination and targeted testing. Population or newborn screening is not indicated.

## 11. Outcome and prognosis

Prognosis is excellent. Most patients remain asymptomatic with preserved corrected acuity, and the disease does not affect survival or life expectancy. No disease-specific mortality, five- or ten-year survival statistic, disability rate, or quality-of-life score exists. (weiss2024ic3dclassificationof pages 48-49, barrio2020punctiformandpolychromatic pages 1-8)

When reduced vision is present, published imaging series attributed it to other conditions such as amblyopia, cataract, or retinal pigment epitheliopathy rather than PDCD. Corneal edema, endothelial failure, recurrent erosions, ulceration, and blindness are not characteristic complications. (alafaleq2020multimodalimagingof pages 6-9)

No validated prognostic biomarker exists. Deposit burden, symptoms, acuity, and serial OCT/IVCM are reasonable monitoring measures, but their predictive value is unproven.

## 12. Treatment

**Standard care is observation and periodic ophthalmic review.** Refractive correction treats coincidental ametropia; glare can be managed symptomatically. Genetic counseling is appropriate for PRDX3-positive families and STS-associated disease. A 2025 case report likewise recommended observation/follow-up and noninvasive imaging. (nicoli2025distrofiacornealpredescemética pages 3-5)

No drug, antioxidant, lysosomal therapy, gene therapy, RNA therapy, cell therapy, PTK, keratoplasty, or other surgery has demonstrated disease-specific benefit. Because deposits are deep and visual acuity is generally preserved, PTK is anatomically inappropriate in routine PPPCD. Corneal transplantation would be considered only for exceptional, proven visually significant stromal opacity after exclusion of other causes; no response rate or recurrence estimate exists.

No relevant interventional ClinicalTrials.gov study or disease-specific NCT identifier was found. Generic patents and experimental gene-editing approaches for other corneal dystrophies do not constitute evidence for PDCD treatment. Suggested NCIT concepts are **Observation**, **Genetic Counseling**, **Visual Acuity Test**, **Optical Coherence Tomography**, and, only if exceptionally indicated, **Corneal Transplantation**; exact NCIT codes should be terminology-service verified.

## 13. Prevention

Primary prevention is unavailable for a germline disorder. No vaccine, prophylactic drug, diet, or exposure avoidance prevents PPPCD. Secondary prevention consists of cascade examination/testing in affected families, allowing early diagnosis and avoidance of unnecessary treatment. Tertiary prevention consists of routine monitoring and treatment of unrelated visual problems.

Genetic counseling should explain autosomal-dominant transmission—nominally a 50% variant-transmission probability from a heterozygous parent—while emphasizing that penetrance and severity are not adequately quantified. Prenatal or preimplantation testing is technically possible once a familial pathogenic variant is confirmed but is rarely proportionate for a usually asymptomatic, non–vision-threatening condition. STS families require X-linked counseling. No population screening or public-health intervention is justified.

## 14. Other species and natural disease

No genetically confirmed natural PRDX3-associated PDCD has been established in another species. A 2022 canine report described bilateral, noninflammatory posterior stromal opacities with hyperreflective deposits within keratocytes and increasing numbers of enlarged deposit-containing keratocytes toward the posterior stroma. The authors judged this “reminiscent of pre-Descemet corneal dystrophy” in humans, but no orthologous mutation was demonstrated; it is therefore a comparative phenocopy, not a validated natural model. Relevant taxonomy is domestic dog, *Canis lupus familiaris* (**NCBI Taxon 9615**). Breed/VBO assignment was not established in the retrieved evidence.

There is no zoonotic or transmissible potential.

## 15. Model organisms

No validated PRDX3 knock-in mouse, rat, zebrafish, invertebrate, organoid, iPSC, or corneal-cell model has been shown to reproduce human PPPCD deposits. Likewise, no STS-deficient model has been validated specifically for the corneal phenotype. The canine observation may help define comparative imaging features but cannot establish causality or therapeutic response.

Priority models would include: (1) a heterozygous **PRDX3 p.Asp190His knock-in** animal; (2) patient-derived keratocytes or iPSC-derived corneal stromal cells; and (3) engineered corneal stromal organoids assessing mitochondrial peroxide handling, keratocyte vacuoles, lipofuscin/lipid deposition, transparency, and biomechanics. These are research recommendations, not currently validated resources.

## Recent developments and evidence-quality assessment

The key recent advance is the February 2024 IC3D reclassification: PRDX3-associated PPPCD is now category 1, while isolated nonpolychromatic PDCD remains category 4. IC3D’s abstract states: “**Pre-Descemet corneal dystrophies include category 1, autosomal dominant, punctiform and polychromatic pre-Descemet corneal dystrophy (PPPCD) (PRDX3 mutations, chromosome 10)**” and notes that it is “**typically asymptomatic**.” ([DOI](https://doi.org/10.1097/ico.0000000000003420), February 2024). (weiss2024ic3dclassificationof pages 48-49)

The foundational genetic evidence remains the April 2020 family study: 12 affected people in three newly reported families, recurrence of PRDX3 p.Asp190His in four of five families evaluated across the study, and significantly increased corneal stiffness as the principal measured biomechanical abnormality. Its main limitations are small sample size, concentration in a few ancestries, prediction rather than direct functional proof, and unresolved locus heterogeneity. (barrio2020punctiformandpolychromatic pages 1-8, barrio2020punctiformandpolychromatic pages 17-21)

Overall, evidence is **moderate-to-strong for PRDX3 as the cause of PPPCD**, **moderate for a keratocyte deposition/degeneration mechanism**, and **very low for epidemiology, quantified natural history, molecular profiling, or treatment efficacy**. The most important database-curation safeguard is to keep PRDX3-associated PPPCD, category-4 isolated PDCD/cornea farinata, and STS-associated syndromic deposits as related but distinct assertions.

References

1. (weiss2024ic3dclassificationof pages 48-49): Jayne S. Weiss, Christopher J. Rapuano, Berthold Seitz, Massimo Busin, Tero T. Kivelä, Nacim Bouheraoua, Cecilie Bredrup, Ken K. Nischal, Harshvardhan Chawla, Vincent Borderie, Kenneth R. Kenyon, Eung Kweon Kim, Hans Ulrik Møller, Francis L. Munier, Tim Berger, and Walter Lisch. Ic3d classification of corneal dystrophies—edition 3. Cornea, 43:466-527, Feb 2024. URL: https://doi.org/10.1097/ico.0000000000003420, doi:10.1097/ico.0000000000003420. This article has 119 citations and is from a peer-reviewed journal.

2. (weiss2024ic3dclassificationof pages 11-12): Jayne S. Weiss, Christopher J. Rapuano, Berthold Seitz, Massimo Busin, Tero T. Kivelä, Nacim Bouheraoua, Cecilie Bredrup, Ken K. Nischal, Harshvardhan Chawla, Vincent Borderie, Kenneth R. Kenyon, Eung Kweon Kim, Hans Ulrik Møller, Francis L. Munier, Tim Berger, and Walter Lisch. Ic3d classification of corneal dystrophies—edition 3. Cornea, 43:466-527, Feb 2024. URL: https://doi.org/10.1097/ico.0000000000003420, doi:10.1097/ico.0000000000003420. This article has 119 citations and is from a peer-reviewed journal.

3. (alafaleq2020multimodalimagingof pages 1-2): Munirah Alafaleq, Cristina Georgeon, Kate Grieve, and Vincent M Borderie. Multimodal imaging of pre-descemet corneal dystrophy. European Journal of Ophthalmology, 30:908-916, Sep 2020. URL: https://doi.org/10.1177/1120672119862505, doi:10.1177/1120672119862505. This article has 9 citations and is from a peer-reviewed journal.

4. (alafaleq2020multimodalimagingof pages 4-6): Munirah Alafaleq, Cristina Georgeon, Kate Grieve, and Vincent M Borderie. Multimodal imaging of pre-descemet corneal dystrophy. European Journal of Ophthalmology, 30:908-916, Sep 2020. URL: https://doi.org/10.1177/1120672119862505, doi:10.1177/1120672119862505. This article has 9 citations and is from a peer-reviewed journal.

5. (alafaleq2020multimodalimagingof pages 6-9): Munirah Alafaleq, Cristina Georgeon, Kate Grieve, and Vincent M Borderie. Multimodal imaging of pre-descemet corneal dystrophy. European Journal of Ophthalmology, 30:908-916, Sep 2020. URL: https://doi.org/10.1177/1120672119862505, doi:10.1177/1120672119862505. This article has 9 citations and is from a peer-reviewed journal.

6. (alafaleq2020multimodalimagingof pages 2-4): Munirah Alafaleq, Cristina Georgeon, Kate Grieve, and Vincent M Borderie. Multimodal imaging of pre-descemet corneal dystrophy. European Journal of Ophthalmology, 30:908-916, Sep 2020. URL: https://doi.org/10.1177/1120672119862505, doi:10.1177/1120672119862505. This article has 9 citations and is from a peer-reviewed journal.

7. (barrio2020punctiformandpolychromatic pages 1-8): Jorge L. Alió del Barrio, Doug D. Chung, Olena Al-Shymali, Alice Barrington, Kavya Jatavallabhula, Vinay S. Swamy, Pilar Yébana, Maria Angélica Henríquez-Recine, Ana Boto-de-los-Bueis, Jorge L. Alió, and Anthony J. Aldave. Punctiform and polychromatic pre-descemet corneal dystrophy: clinical evaluation and identification of the genetic basis. American Journal of Ophthalmology, 212:88-97, Apr 2020. URL: https://doi.org/10.1016/j.ajo.2019.11.024, doi:10.1016/j.ajo.2019.11.024. This article has 12 citations and is from a domain leading peer-reviewed journal.

8. (barrio2020punctiformandpolychromatic pages 17-21): Jorge L. Alió del Barrio, Doug D. Chung, Olena Al-Shymali, Alice Barrington, Kavya Jatavallabhula, Vinay S. Swamy, Pilar Yébana, Maria Angélica Henríquez-Recine, Ana Boto-de-los-Bueis, Jorge L. Alió, and Anthony J. Aldave. Punctiform and polychromatic pre-descemet corneal dystrophy: clinical evaluation and identification of the genetic basis. American Journal of Ophthalmology, 212:88-97, Apr 2020. URL: https://doi.org/10.1016/j.ajo.2019.11.024, doi:10.1016/j.ajo.2019.11.024. This article has 12 citations and is from a domain leading peer-reviewed journal.

9. (barrio2020punctiformandpolychromatic pages 26-30): Jorge L. Alió del Barrio, Doug D. Chung, Olena Al-Shymali, Alice Barrington, Kavya Jatavallabhula, Vinay S. Swamy, Pilar Yébana, Maria Angélica Henríquez-Recine, Ana Boto-de-los-Bueis, Jorge L. Alió, and Anthony J. Aldave. Punctiform and polychromatic pre-descemet corneal dystrophy: clinical evaluation and identification of the genetic basis. American Journal of Ophthalmology, 212:88-97, Apr 2020. URL: https://doi.org/10.1016/j.ajo.2019.11.024, doi:10.1016/j.ajo.2019.11.024. This article has 12 citations and is from a domain leading peer-reviewed journal.

10. (barrio2020punctiformandpolychromatic pages 12-17): Jorge L. Alió del Barrio, Doug D. Chung, Olena Al-Shymali, Alice Barrington, Kavya Jatavallabhula, Vinay S. Swamy, Pilar Yébana, Maria Angélica Henríquez-Recine, Ana Boto-de-los-Bueis, Jorge L. Alió, and Anthony J. Aldave. Punctiform and polychromatic pre-descemet corneal dystrophy: clinical evaluation and identification of the genetic basis. American Journal of Ophthalmology, 212:88-97, Apr 2020. URL: https://doi.org/10.1016/j.ajo.2019.11.024, doi:10.1016/j.ajo.2019.11.024. This article has 12 citations and is from a domain leading peer-reviewed journal.

11. (shi2017invivoconfocal pages 4-5): Hui Shi, Xiao-feng Qi, Tao-tao Liu, Qian Hao, Xiao-hong Li, Ling-ling Liang, Yi-miao Wang, and Zhi-hua Cui. In vivo confocal microscopy of pre-descemet corneal dystrophy associated with x-linked ichthyosis: a case report. BMC Ophthalmology, Mar 2017. URL: https://doi.org/10.1186/s12886-017-0423-5, doi:10.1186/s12886-017-0423-5. This article has 18 citations and is from a peer-reviewed journal.

12. (shi2017invivoconfocal pages 1-2): Hui Shi, Xiao-feng Qi, Tao-tao Liu, Qian Hao, Xiao-hong Li, Ling-ling Liang, Yi-miao Wang, and Zhi-hua Cui. In vivo confocal microscopy of pre-descemet corneal dystrophy associated with x-linked ichthyosis: a case report. BMC Ophthalmology, Mar 2017. URL: https://doi.org/10.1186/s12886-017-0423-5, doi:10.1186/s12886-017-0423-5. This article has 18 citations and is from a peer-reviewed journal.

13. (shi2017invivoconfocal pages 2-4): Hui Shi, Xiao-feng Qi, Tao-tao Liu, Qian Hao, Xiao-hong Li, Ling-ling Liang, Yi-miao Wang, and Zhi-hua Cui. In vivo confocal microscopy of pre-descemet corneal dystrophy associated with x-linked ichthyosis: a case report. BMC Ophthalmology, Mar 2017. URL: https://doi.org/10.1186/s12886-017-0423-5, doi:10.1186/s12886-017-0423-5. This article has 18 citations and is from a peer-reviewed journal.

14. (nicoli2025distrofiacornealpredescemética pages 3-5): CM Nicoli and ES López. Distrofia corneal pre-descemética. Unknown journal, 2025.

## Artifacts

- [Edison artifact artifact-00](Pre-descemet_Corneal_Dystrophy-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 5 |
| Resolved | 5 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 2 |
| Quoted claims found in source | 2 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 5 |
| On topic | 1 |
| Off topic | 0 |

All extracted references resolved successfully.