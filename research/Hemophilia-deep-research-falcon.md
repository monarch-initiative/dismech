---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-20T07:18:04.900000'
end_time: '2026-08-20T07:29:34.697008'
duration_seconds: 689.8
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Hemophilia
  mondo_id: ''
  category: Genetic
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 42
reference_validation:
  total_references: 16
  verified: 16
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 16
  on_topic: 11
  off_topic: 1
  off_topic_references:
  - DOI:10.1177/00185787231222506
  needs_review: true
  validator_version: 0.2.1
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Hemophilia-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Hemophilia
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Hemophilia** covering all of the
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
- **Disease Name:** Hemophilia
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Hemophilia** covering all of the
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


# Hemophilia: comprehensive disease-characteristics report

## Scope and evidence note

This report concerns **congenital hemophilia A and B**, not acquired hemophilia A. Hemophilia A is factor VIII (FVIII) deficiency caused by pathogenic **F8** variants; hemophilia B, or Christmas disease, is factor IX (FIX) deficiency caused by pathogenic **F9** variants. Both are lifelong X-linked bleeding disorders. Acquired hemophilia A is instead an autoimmune FVIII-inhibitor disorder and belongs in the differential diagnosis rather than this genetic entry.

The evidence base combines disease-level resources, peer-reviewed human cohorts, trials, laboratory/in-vitro studies, and animal models. It is **aggregated disease-level evidence**, not an individual electronic health record. DOI URLs and publication dates are supplied because PMID metadata were not consistently exposed by the retrieved records; PMIDs are not guessed.

| Feature | Hemophilia A | Hemophilia B |
|---|---|---|
| Causal gene / protein | **F8** / factor VIII deficiency (OpenTargets Search: hemophilia A,hemophilia B-F8,F9, deshpande2024adenoassociatedvirus–basedgene pages 1-2) | **F9** / factor IX deficiency (wang2024clinicalanalysisand pages 1-2, deshpande2024adenoassociatedvirus–basedgene pages 1-2) |
| Inheritance | X-linked recessive inherited bleeding disorder (zhang2023moleculardiagnosisof pages 1-2, li2023f8geneinversion pages 1-2) | X-linked recessive inherited bleeding disorder (wang2024clinicalanalysisand pages 1-2, arruda2021genetherapyfor pages 2-3) |
| Severity thresholds (shared) | Severe **<1%**, moderate **1–5%**, mild **>5–40%** factor activity (deshpande2024adenoassociatedvirus–basedgene pages 1-2, zhang2023moleculardiagnosisof pages 1-2) | Severe **<1%**, moderate **1–5%**, mild **>5–40%** factor activity (deshpande2024adenoassociatedvirus–basedgene pages 1-2, zhang2023moleculardiagnosisof pages 1-2) |
| Approximate prevalence / incidence | Prevalence about **1 per 10,000** overall; incidence about **1:5,000 male births** (chernyi2024recentadvancesin pages 1-3, arruda2021genetherapyfor pages 2-3) | Prevalence about **1 per 60,000** overall; incidence about **1:30,000 male births** (chernyi2024recentadvancesin pages 1-3, arruda2021genetherapyfor pages 2-3) |
| Common variant classes | Intron 22 inversion is the major severe-HA lesion (~45% of severe cases); also intron 1 inversion, missense, nonsense, frameshift, deletions/insertions (guo2018spectrumofmolecular pages 1-2, zhang2023moleculardiagnosisof pages 1-2, zhang2023moleculardiagnosisof pages 2-3) | Missense variants predominate; also nonsense, frameshift, deletions, deletion-insertions (wang2024clinicalanalysisand pages 1-2, wang2024clinicalanalysisand pages 8-9, wang2024clinicalanalysisand pages 7-8) |
| Inhibitor frequency | About **20–30%** alloantibody/inhibitor prevalence, especially in severe HA (arruda2021genetherapyfor pages 2-3) | About **3–10%** overall in reviews; **6.1%** in one 2024 Chinese real-world cohort (arruda2021genetherapyfor pages 2-3, wang2024clinicalanalysisand pages 1-2) |
| Principal current prophylaxis | Prophylaxis is standard of care; options include standard/extended half-life FVIII and subcutaneous emicizumab for HA (croteau20212021clinicaltrials pages 1-6, croteau20212021clinicaltrials pages 29-32) | Prophylaxis is standard of care; options include standard/extended half-life FIX replacement (croteau20212021clinicaltrials pages 1-6, croteau20212021clinicaltrials pages 29-32) |
| Licensed gene therapy and key phase 3 outcome | **Valoctocogene roxaparvovec (Roctavian/BMN 270)**; phase 3 GENEr8-1 in **134** adults: FVIII activity rose by mean **41.9 U/dL** at weeks 49–52, annualized bleeding rate fell **84.5%** through 104 weeks, FVIII use fell **98.6%**, mean FVIII **18.2 U/dL** at month 36 (levien2024valoctocogeneroxaparvovec pages 2-3, levien2024valoctocogeneroxaparvovec pages 3-5) | **Etranacogene dezaparvovec (Hemgenix/AMT-061)**; phase 3 HOPE-B in **54** adults: mean FIX activity change **34.3 percentage points** at 18 months, **96%** stopped FIX prophylaxis in one review, and ~**94%** remained off prophylaxis at 3 years with FIX ~**38.6 IU/dL** at year 3 (anguela2024hemophiliaband pages 2-3, kaczmarek2024currentandemerging pages 5-5, anguela2024hemophiliaband pages 4-5) |


*Table: This table contrasts the core knowledge-base facts for congenital hemophilia A and B using only previously gathered evidence. It summarizes genetics, severity, epidemiology, inhibitor risk, current prophylaxis, and the main licensed gene-therapy outcomes for quick reference.*

## 1. Disease information

### Definition and classification

Hemophilia is failure of secondary hemostasis caused by inadequate FVIII or FIX activity. The accepted laboratory severity classes are **severe, <1 IU/dL (<1%)**; **moderate, 1–5 IU/dL**; and **mild, >5–40 IU/dL**. Approximately 50–67% of patients with hemophilia A and 33–50% with hemophilia B have severe disease. Severe disease produces recurrent spontaneous bleeding, especially hemarthroses; moderate and mild disease more often manifests after trauma, dental work, or surgery. Women and girls can also be symptomatic owing to low factor levels, skewed X-inactivation, Turner syndrome, homozygosity/compound heterozygosity, or other unusual X-chromosome states. (deshpande2024adenoassociatedvirus–basedgene pages 1-2)

### Identifiers and synonyms

Recommended knowledge-base mappings are:

- **Hemophilia A:** MONDO:0010602; OMIM #306700; Orphanet ORPHA:448; ICD-10-CM D66; MeSH *Hemophilia A*. Open Targets independently identifies MONDO:0010602 and strongly associates it with **F8**. (OpenTargets Search: hemophilia A,hemophilia B-F8,F9)
- **Hemophilia B:** MONDO:0010603; OMIM #306900; Orphanet ORPHA:98878; ICD-10-CM D67; MeSH *Hemophilia B*.
- **Umbrella synonyms:** haemophilia, congenital hemophilia, hereditary factor deficiency.
- **A synonyms:** factor VIII deficiency, classical hemophilia.
- **B synonyms:** factor IX deficiency, Christmas disease.

The A/B entities should remain separate children beneath a congenital hemophilia parent. “Hemophilic arthropathy” is a complication, not a synonymous disease.

## 2. Etiology, risk, protection, and gene–environment interaction

### Causal factors

The primary causes are germline loss-of-function or function-reducing variants in **F8** or **F9**. The resulting low FVIII/FIX activity disrupts intrinsic-tenase amplification and thrombin generation. Open Targets gives **F8–hemophilia A** a high association score (0.918) supported by five literature evidence records, reinforcing that F8 is causal rather than merely correlative. (OpenTargets Search: hemophilia A,hemophilia B-F8,F9)

### Genetic risk factors

- In severe hemophilia A, **F8 intron-22 inversion** accounts for about 45% of cases; intron-1 inversion accounts for approximately 1–2%. Other lesions include missense, nonsense, frameshift, splice, small indel, exon/gene deletion, duplication, and complex structural variants. (zhang2023moleculardiagnosisof pages 1-2, li2023f8geneinversion pages 1-2)
- In a 216-family molecular study, pathogenic F8 variants were found in 209 families (**96.8%**); Inv22 occurred in 89 severe families and Inv1 in five. Nonsense variants significantly increased inhibitor odds. (guo2018spectrumofmolecular pages 1-2)
- In a 2024 hemophilia-B cohort, point variants constituted **84.2%**, missense **63.2%**, and nonsense **24.8%** of identified F9 lesions; large deletions and truncating variants generally produce more severe disease and greater inhibitor risk. (wang2024clinicalanalysisand pages 8-9, wang2024clinicalanalysisand pages 7-8)
- Family history is informative but not required. Only **30.3%** of the 185-patient Chinese hemophilia-B cohort reported a family history, consistent with de novo variants, unrecognized maternal transmission, and incomplete family ascertainment. (wang2024clinicalanalysisand pages 1-2)

These are ordinarily **germline**, not somatic, disorders. Pathogenic variants should be exceptionally rare or absent from gnomAD/other population databases, but frequency alone cannot establish pathogenicity. Classification should use ACMG/AMP criteria, ClinVar/ClinGen evidence, phenotype, segregation, factor activity, RNA studies where appropriate, and functional assays. A VUS must not be used alone for predictive testing.

### Environmental and treatment-related modifiers

No toxin, diet, infection, smoking exposure, or occupation causes congenital hemophilia. Environment chiefly modifies bleeding expression: trauma, surgery, contact sports, intramuscular procedures, antiplatelet/anticoagulant drugs, obesity-related joint loading, delayed treatment, and poor prophylaxis access increase morbidity. Conversely, regular prophylaxis, safe physical activity, normal body mass, dental care, vaccination, early bleed treatment, and multidisciplinary care protect against complications. In one real-world cohort, preventive therapy, absence of treatment delay and inhibitors, and avoidance of high-intensity episodic replacement correlated with better SF-36 scores. (wang2024clinicalanalysisand pages 1-2)

The major gene–environment interaction is **genotype × treatment exposure** in inhibitor formation. Null F8 genotypes create little endogenous antigen and raise alloantibody risk when therapeutic FVIII is introduced; intensive exposure, inflammation, surgery, treatment product, age, ancestry, and immune background can modify that risk. Severe hemophilia A develops inhibitors in roughly **20–30%**, whereas reported hemophilia-B frequencies are approximately **3–10%**. (arruda2021genetherapyfor pages 2-3)

No reproducible “protective allele” is established for routine clinical use. Higher residual factor expression from hypomorphic variants is functionally protective, while timely prophylaxis is the dominant modifiable protective factor.

## 3. Phenotypes

### Core phenotype catalogue

- **Prolonged bleeding after injury/procedure** — symptom/sign; congenital predisposition, but presentation may be neonatal through adulthood depending on severity; episodic and variable. Suggested HPO: **Abnormal bleeding (HP:0001892)** and **Prolonged bleeding after surgery**.
- **Spontaneous bleeding** — severe disease, commonly beginning in infancy or early childhood as mobility increases; recurrent without prophylaxis. HPO: **Spontaneous bleeding (HP:0001890)**.
- **Hemarthrosis** — acute painful swelling, warmth, restricted movement, usually knees, ankles, and elbows; recurrent and strongly severity-dependent. HPO: **Hemarthrosis (HP:0005261)** and **Joint swelling (HP:0001386)**. In a 2024 hemophilia-B cohort, **71.4%** had joint bleeding and 64.4% of those had a target joint; lower-extremity joints predominated. (wang2024clinicalanalysisand pages 1-2)
- **Muscle/soft-tissue hematoma and easy bruising** — episodic; can cause compartment syndrome, neuropathy, or anemia. Suggested HPO: **Easy bruising (HP:0000978)** and **Intramuscular hematoma**.
- **Mucosal/oral bleeding, epistaxis, hematuria and gastrointestinal bleeding** — less characteristic than deep-tissue bleeding but clinically relevant. Suggested HPO: **Epistaxis (HP:0000421)**, **Hematuria (HP:0000790)**, and **Gastrointestinal hemorrhage (HP:0002239)**.
- **Intracranial hemorrhage** — uncommon but life-threatening, especially around birth, trauma, or untreated severe disease. HPO: **Intracranial hemorrhage (HP:0002170)**.
- **Hemophilic arthropathy** — chronic pain, stiffness, synovial hypertrophy, reduced range of motion, contracture, cartilage loss and subchondral bone damage after recurrent or subclinical hemarthrosis. Suggested HPO: **Arthropathy (HP:0003040)**, **Joint pain (HP:0002829)**, **Joint contracture (HP:0001371)** and **Limitation of joint mobility (HP:0001376)**. Severe hemophilia can culminate in ankylosis and contractures. (chernyi2024recentadvancesin pages 1-3)
- **Laboratory abnormalities** — low FVIII:C or FIX:C; typically isolated prolonged aPTT that corrects in a mixing study unless an inhibitor is present; normal platelet count and usually normal PT. HPO: **Reduced factor VIII activity (HP:0003125)** or **Reduced factor IX activity**, and **Prolonged partial thromboplastin time (HP:0003645)**.
- **Inhibitors** — laboratory/immune complication measured by Nijmegen-modified Bethesda assay; produce poor factor recovery and breakthrough bleeding.

### Quality-of-life effects

Bleeding causes pain, exercise restriction, school/work absence, treatment anxiety, loss of independence, disability, and family financial burden. The 2024 cohort documented exercise limitation, missed school, injection distress, economic pressure and home-care burden. Diagnostic delay affected **34.6%** and treatment delay **38.5%**, demonstrating a real-world implementation gap. (wang2024clinicalanalysisand pages 8-9, wang2024clinicalanalysisand pages 7-8)

## 4. Genetic and molecular information

### Genes and proteins

- **F8**, Xq28, encodes coagulation factor VIII; HGNC symbol F8. FVIII circulates stabilized by von Willebrand factor and, once activated, acts as the FIXa cofactor.
- **F9**, Xq27.1, encodes vitamin-K-dependent factor IX; HGNC symbol F9. Activated FIX combines with FVIIIa, calcium and phospholipid to activate factor X.

Normal circulating FVIII is low abundance (~1 nM) with an 8–12-hour half-life; FIX is ~90 nM with a 19–26-hour half-life. (arruda2021genetherapyfor pages 2-3)

### Variant interpretation and structural abnormalities

Null variants—Inv22/Inv1, large deletion, nonsense, canonical splice and frameshift variants—usually cause severe disease through absent protein. Missense variants frequently retain partial activity and produce moderate/mild disease, although domain-specific exceptions occur. Copy-number variants require MLPA or genome-level detection; a reported partial 0.16-Mb F8 duplication combined with Inv22 preserved an intact transcript and produced no obvious phenotype, illustrating why structural context and RNA confirmation matter. (li2023f8geneinversion pages 1-2)

Routine molecular workflows now identify a causal variant in up to about 97% of hemophilia A families. Inversions should be tested explicitly; sequencing alone can miss them. Rare deep-intronic, regulatory, repetitive, mosaic, or complex rearrangements account for part of the residual unsolved fraction. (guo2018spectrumofmolecular pages 1-2, zhang2023moleculardiagnosisof pages 1-2)

### Modifier genes and epigenetics

HLA class II, cytokine, immune-regulatory, and antigen-processing loci have been studied mainly as **inhibitor-risk modifiers**, but none currently replaces clinical/genotype risk models. Skewed X-chromosome inactivation is the most clinically important epigenetic phenomenon in symptomatic carriers. Disease-specific methylation, histone, single-cell, spatial-transcriptomic, lipidomic, or metabolomic signatures are not validated diagnostic features and should be recorded as research-only.

## 5. Environmental information

Congenital hemophilia has **no infectious, toxic, radiation, pollution, dietary, alcohol, or smoking cause**. Historically, plasma-derived concentrate exposure transmitted HIV, hepatitis B, and hepatitis C; modern recombinant products, donor screening and viral inactivation have greatly reduced this risk. Infections are complications of past treatment rather than etiologic agents.

Lifestyle influences morbidity. Appropriate low-impact exercise and physiotherapy improve strength and joint protection; obesity increases mechanical stress, cardiovascular risk and arthropathy burden. An active Netherlands trial, **NCT05608863**, is testing a two-year virtual coaching/group lifestyle program in approximately 30 overweight/obese people with bleeding disorders, measuring weight, bleeding, factor use and cardiometabolic outcomes. (NCT05608863 chunk 1)

## 6. Mechanism and pathophysiology

### Upstream coagulation defect

The causal chain is:

**F8/F9 pathogenic variant → deficient/dysfunctional FVIII or FIX → impaired intrinsic-tenase activity → inadequate factor-X activation and thrombin burst → weak fibrin clot and rebleeding → deep-tissue hemorrhage/hemarthrosis.**

Suggested GO processes are **blood coagulation (GO:0007596)**, **hemostasis (GO:0007599)**, **factor X activation**, and **fibrin-clot formation**. Relevant cells include hepatocytes for FIX synthesis (**CL:0000182**), liver sinusoidal endothelial cells as principal FVIII-producing cells, platelets (**CL:0000233**), endothelial cells (**CL:0000115**) and synovial macrophages.

### Downstream joint-damage cascade

**Hemarthrosis → erythrocyte breakdown and iron/hemosiderin deposition → reactive oxygen species and chondrocyte apoptosis → macrophage/type-A synoviocyte activation → IL-1β, IL-6 and TNF-α → NF-κB, MMP and ADAMTS activation → synovial hypertrophy/pannus and cartilage degradation → VEGF-driven neovascularization and recurrent bleeding → subchondral bone loss, pain, contracture and disability.** Human hemophilic-joint disease showed approximately fourfold elevated VEGF-A; candidate blood/tissue markers include SDF-1α, MMP-9, ferritin, D-dimer, COMP and collagen-turnover markers. (badulescu2024biomarkersinvolvedin pages 11-13, badulescu2024biomarkersinvolvedin pages 3-5)

TNF-α suppresses proteoglycan/collagen-II synthesis and promotes MMP-1, MMP-3, MMP-13 and ADAMTS4. IL-1β increases iron uptake by fibroblast-like/type-B synoviocytes. Reduced thrombin also diminishes PAR-1-mediated osteoblast proliferation; reduced osteoprotegerin with increased RANK/RANKL shifts remodeling toward osteoclast-mediated resorption. (badulescu2024biomarkersinvolvedin pages 5-6, badulescu2024biomarkersinvolvedin pages 8-10)

Suggested GO terms include **inflammatory response (GO:0006954)**, **reactive oxygen species metabolic process**, **angiogenesis (GO:0001525)**, **extracellular-matrix disassembly**, **chondrocyte apoptotic process**, and **osteoclast differentiation (GO:0030316)**. Relevant cell terms include macrophage **CL:0000235**, fibroblast **CL:0000057**, chondrocyte **CL:0000138**, osteoblast **CL:0000062**, osteoclast **CL:0000092**, synovial fibroblast and vascular endothelial cell.

### Immune involvement and profiling

Therapeutic factor may be internalized by antigen-presenting cells and presented to CD4 T cells, activating B cells and high-affinity neutralizing IgG. Mouse evidence implicates marginal-zone B cells in the initial anti-FVIII response. Immune-tolerance induction succeeds in approximately **60–80%**, leaving a substantial refractory group. (chernyi2024recentadvancesin pages 3-4, badulescu2024biomarkersinvolvedin pages 10-11)

Proteomic/transcriptomic studies of arthropathy remain exploratory; no serum, synovial, proteomic, metabolomic or miRNA signature is sufficiently validated for routine diagnosis or prognosis. Much mechanistic evidence derives from synovectomy specimens, in-vitro synoviocytes, induced hemarthrosis in rodents/dogs, and small human biomarker cohorts, so causality and generalizability remain limited. (badulescu2024biomarkersinvolvedin pages 11-13, badulescu2024biomarkersinvolvedin pages 5-6)

## 7. Anatomical structures affected

The primary functional system is blood/coagulation. Bleeding secondarily affects:

- **Synovial joints:** knees, ankles and elbows most characteristically; also hips, shoulders and wrists. Suggested UBERON: synovial joint **UBERON:0002217**, knee joint, ankle joint and elbow joint.
- **Skeletal muscle and connective tissue:** hematomas and compartment syndromes.
- **Central nervous system:** intracranial/spinal hemorrhage.
- **Mucosa, urinary tract and gastrointestinal tract:** episodic bleeding.
- **Skeleton:** subchondral bone erosion and osteoporosis downstream of chronic arthropathy.
- **Liver:** source/therapeutic target for factor expression rather than a tissue injured by congenital deficiency; critical for AAV gene therapy monitoring.

Disease is not intrinsically lateralized. Individual bleeds may be unilateral, whereas chronic target-joint disease may be asymmetric or bilateral. Relevant subcellular locations include extracellular plasma/coagulation complexes, platelet membrane phospholipid surfaces, hepatocyte nucleus after gene transfer, and AAV episomes.

## 8. Temporal development

The molecular defect is congenital and lifelong. Severe disease may present with birth-related cephalohematoma or intracranial bleeding, post-circumcision hemorrhage, or bruising/hemarthrosis when crawling and walking begin. Moderate disease commonly emerges in childhood after trauma; mild disease may remain unrecognized until surgery or adulthood.

The untreated course is episodic bleeding with cumulative progressive damage: first hemarthrosis → recurrent bleed/target joint → chronic synovitis → established arthropathy, contracture and possible joint replacement. Bleeding can enter treatment-induced remission under effective prophylaxis, but the genotype does not spontaneously remit. Primary prophylaxis should begin early—expert guidance identifies **before age two** as the goal—to prevent rather than merely react to joint bleeding. (NCT07437404 chunk 1)

Critical windows are pregnancy/delivery planning, the neonatal period, initiation of mobility, the first factor-exposure days when inhibitors emerge, and early synovitis before irreversible cartilage loss.

## 9. Inheritance and population

Both A and B are X-linked recessive: hemizygous males are usually affected; heterozygous females show variable factor levels and bleeding. An affected male transmits the variant to all daughters and no sons; a heterozygous mother has a 50% chance of transmitting the variant in each pregnancy. Penetrance for a severe pathogenic variant is high in hemizygous males, but expressivity varies with residual activity, inhibitors, treatment and trauma. Anticipation is not a feature. Germline or parental somatic mosaicism can explain apparently de novo disease.

Estimates are approximately **1 hemophilia-A case per 5,000 male births** and **1 hemophilia-B case per 30,000 male births**; recent reviews estimate more than **1.1–1.2 million** affected worldwide, roughly 400,000 with severe disease. Underdiagnosis and survival differences produce major regional variation. (chernyi2024recentadvancesin pages 1-3, deshpande2024adenoassociatedvirus–basedgene pages 1-2)

A 2024 African meta-analysis estimated hemophilia-A prevalence at **6.82 per 100,000 persons** (95% CI 5.16–8.48), emphasizing ascertainment and access disparities. Population ancestry does not biologically restrict disease, but diagnosis and survival are strongly geography-dependent. Consanguinity can permit affected females when an affected father and carrier mother reproduce but is not required.

Among 106 mothers tested in a 2024 hemophilia-B cohort, **84.0%** were molecular carriers; 27.7% had FIX 0.05–0.40 IU/mL and therefore a mild hemophilia-range phenotype. (wang2024clinicalanalysisand pages 8-9)

## 10. Diagnostics

### Clinical and laboratory algorithm

1. Suspect hemophilia from deep-tissue bleeding, hemarthrosis, disproportionate procedural bleeding, or family history.
2. Obtain CBC/platelets, PT/INR, aPTT and fibrinogen. Congenital A/B typically shows normal PT/platelets with prolonged aPTT, although mild disease may have a normal screening aPTT.
3. Perform an aPTT mixing study. Correction favors factor deficiency; failure to correct suggests an inhibitor, lupus anticoagulant, or anticoagulant drug.
4. Measure one-stage and/or chromogenic **FVIII:C and FIX:C**; measure VWF antigen/activity because type 2N or type 3 von Willebrand disease can mimic hemophilia A.
5. If response to factor is poor, quantify inhibitors with the Nijmegen-modified Bethesda assay.
6. Assess joints with Hemophilia Joint Health Score, ultrasound/HEAD-US, and MRI when early synovitis/cartilage damage must be defined. In the 2024 cohort, HJHS correlated with HEAD-US-C (**r=0.542, P<0.001**). (wang2024clinicalanalysisand pages 1-2)

Differentials include von Willebrand disease, factor XI deficiency, combined FV/FVIII deficiency, vitamin-K deficiency, liver disease, disseminated intravascular coagulation, lupus anticoagulant, anticoagulant exposure, platelet disorders and acquired FVIII inhibitor.

### Genetic testing

For hemophilia A, test Inv22 and Inv1, sequence all coding exons/splice boundaries, and use deletion/duplication analysis such as MLPA. For unresolved cases, add RNA analysis, long-read sequencing or WGS to detect deep-intronic and complex structural variants. A 2023 series used inversion assays, NGS and Sanger confirmation and found Inv22, Inv1, missense, nonsense and frameshift lesions; approximately 5% remained unresolved by then-current methods. (zhang2023moleculardiagnosisof pages 1-2, zhang2023moleculardiagnosisof pages 2-3)

For hemophilia B, sequence **F9** plus CNV analysis. Targeted single-gene testing is generally more efficient than WES; WES may miss inversions, deep intronic lesions and CNVs. WGS/long-read sequencing is useful after negative comprehensive testing. CMA, karyotype and FISH are not routine unless a syndromic chromosome abnormality is suspected. Mitochondrial and repeat-expansion testing are not applicable.

Once the familial variant is known, offer cascade testing, factor assays in women and girls, prenatal diagnosis by CVS/amniocentesis, and preimplantation genetic testing for monogenic disease. One report used PGT-M, euploid unaffected embryo transfer, amniocentesis confirmation at 18 weeks, and neonatal FVIII testing. (bai2021casereportidentification pages 7-8)

## 11. Outcome and prognosis

With comprehensive care and safe prophylaxis, survival and quality of life can approach those of unaffected peers; without reliable therapy, fatal hemorrhage and lifelong musculoskeletal disability remain substantial. (marchesini2021recentadvancesin pages 10-12)

Major adverse prognostic factors are severe factor deficiency, intracranial hemorrhage, recurrent hemarthrosis/target joints, inhibitor development, delayed diagnosis or treatment, poor adherence/access, established arthropathy, chronic viral liver disease, and aging-related cardiovascular comorbidity. Inhibitors increase bleeding and complicate surgery. Cardiovascular disease prevalence in US patients has been reported as high as 15%, creating difficult antithrombotic decisions in older adults.

Factor activity, annualized bleeding rate, treated joint bleeds, target-joint count, HJHS, HEAD-US/MRI, inhibitor titer, factor recovery/half-life, pain, school/work participation and validated QoL tools are recommended outcomes. No omics-based prognostic biomarker is validated.

## 12. Treatment and current implementation

### Standard strategy

**Prophylaxis rather than on-demand-only therapy is standard for a severe bleeding phenotype.** Individualize by age, bleeding history, joints, pharmacokinetics, activity, venous access, inhibitor status, preference and local access. Standard- and extended-half-life FVIII/FIX products replace the missing protein; Fc fusion, PEGylation and albumin fusion reduce infusion frequency. (croteau20212021clinicaltrials pages 29-32, croteau20212021clinicaltrials pages 1-6)

Adjuncts include desmopressin for responsive mild hemophilia A, tranexamic acid or aminocaproic acid for oral/mucosal bleeding, topical hemostasis and appropriately planned factor cover for procedures. Avoid desmopressin in hemophilia B. NSAIDs that impair platelets and intramuscular injections should generally be avoided or carefully managed.

Suggested NCIt intervention concepts include **Coagulation Factor VIII**, **Coagulation Factor IX**, **Desmopressin**, **Tranexamic Acid**, **Prophylactic Therapy**, **Monoclonal Antibody Therapy**, **Gene Transfer Therapy**, **Physical Therapy**, **Synovectomy**, and **Joint Replacement**.

### Non-factor and inhibitor therapy

**Emicizumab** is a subcutaneous bispecific FVIIIa mimetic for hemophilia A with or without inhibitors, dosed weekly, every two weeks, or every four weeks. It reduces infusion burden but does not treat hemophilia B. Concurrent high-dose activated prothrombin-complex concentrate can cause thrombosis/thrombotic microangiopathy; laboratory assays also require specialist interpretation. (croteau20212021clinicaltrials pages 1-6)

Acute inhibitor bleeding is treated with recombinant activated FVII, activated prothrombin-complex concentrate, or appropriate factor where low-titer responsiveness remains. Immune-tolerance induction repeatedly exposes FVIII to eradicate inhibitors and succeeds in approximately 60–80%. (chernyi2024recentadvancesin pages 3-4)

Emerging “rebalancing” therapies suppress natural anticoagulants: fitusiran lowers antithrombin by siRNA; concizumab and marstacimab inhibit TFPI. Their attraction is subcutaneous prophylaxis across A/B and inhibitor states, but excessive rebalancing can cause thrombosis. Active programs also include FVIII mimetics such as Mim8. (joshi2024hemostatsinthe pages 22-23)

### Gene therapy: 2023–2024 evidence

**Etranacogene dezaparvovec (Hemgenix)** is a single-dose liver-directed AAV5 vector carrying a codon-optimized hyperactive FIX-Padua transgene. FDA approval was **22 November 2022** and EU authorization **20 February 2023**. In 54 HOPE-B participants, mean FIX activity change was 34.3 percentage points at 18 months; three-year levels were 41.5, 36.7 and 38.6 IU/dL at years 1–3, and **94% remained off prophylaxis** at year three. Expression varied widely, and ALT elevations frequently required immunosuppression. (kaczmarek2024currentandemerging pages 5-5, anguela2024hemophiliaband pages 4-5, anguela2024hemophiliaband pages 2-3)

**Valoctocogene roxaparvovec (Roctavian)** is an AAV5 B-domain-deleted F8 gene therapy, approved in the United States in June 2023. In GENEr8-1 (134 adult men), FVIII rose by mean **41.9 U/dL** at weeks 49–52, treated-bleed rate fell **84.5%** through 104 weeks, factor use fell **98.6%**, and mean FVIII was 18.2 U/dL at month 36. The year-over-year decline in FVIII is a major durability concern. (levien2024valoctocogeneroxaparvovec pages 2-3, levien2024valoctocogeneroxaparvovec pages 3-5)

Current limitations include adult-only eligibility, liver-health requirements, pre-existing anti-AAV antibodies, corticosteroid-treated transaminitis, uncertain decades-long durability, inability to redose the same capsid readily, variable expression, cost, and limited evidence in women, children, inhibitor patients and advanced liver disease.

### Active/recent trials and real-world implementation

- **NCT06224907:** phase 3 valoctocogene roxaparvovec in six Japanese adults with severe hemophilia A; excludes AAV5 antibodies, inhibitors and significant liver disease. (NCT06224907 chunk 2)
- **NCT07437404:** recruiting phase 3 SCT800 recombinant FVIII in 36 previously untreated boys/men with severe A; inhibitor incidence is primary. (NCT07437404 chunk 1)
- **NCT05662319:** active phase 3 subcutaneous fitusiran prophylaxis in 91 adolescent/adult males with severe hemophilia. (NCT05662319 chunk 3)
- **NCT03974113:** phase 2/3 fitusiran in 32 boys aged 1 to <12 years. (NCT03974113 chunk 2)
- **NCT03754790:** long-term phase 3 fitusiran safety/efficacy, 281 participants with A/B, with or without inhibitors.
- **NCT04083781/NCT04082429:** phase 3 concizumab with inhibitors (134 participants) and without inhibitors (156).
- **NCT05685238:** recruiting phase 3 long-term Mim8 study, 451 people with hemophilia A.
- **NCT06922045:** phase 3 STSP-0601 for acute bleeds in 40 A/B patients with inhibitors; primary endpoint is 12-hour effective hemostasis. (NCT06922045 chunk 1)

## 13. Prevention

Primary prevention of the genotype is possible only through informed reproductive choice—not lifestyle modification. Offer nondirective genetic counseling, carrier/cascade testing, PGT-M, prenatal diagnosis and safe delivery planning. Population newborn screening is not standard; targeted neonatal factor testing is appropriate where family history or bleeding raises suspicion.

Secondary prevention means early diagnosis and prophylaxis before recurrent bleeding. Avoid traumatic delivery instrumentation where an affected fetus is possible; give vitamin K subcutaneously/orally or with careful pressure according to specialist protocol; assess suspected neonatal cranial bleeding urgently.

Tertiary prevention includes continuous prophylaxis, prompt bleed treatment, inhibitor surveillance, physiotherapy, safe exercise, weight and dental management, hepatitis A/B immunization, avoidance of platelet-impairing drugs, and specialist factor cover for surgery. Vaccination prevents treatment-associated hepatitis complications but does not prevent hemophilia itself.

## 14. Other species and natural disease

Natural X-linked FVIII/FIX deficiency occurs in dogs, cats, horses and cattle. Hemophilia A has been reported in Boxers, German Shepherd Dogs, German Shorthaired Pointers and mixed breeds. Hemophilia B is documented in at least **26 dog breeds** and three cat breeds, including Cairn Terriers, Hovawarts, German Wirehaired Pointers and British Shorthairs. Reported animal F8/F9 lesions include missense substitutions, promoter nucleotide deletions and LINE-1 insertions. (dodds2022onehealthanimal pages 5-7, dodds2022onehealthanimal pages 11-12, dodds2022onehealthanimal pages 2-4)

Suggested taxa are *Homo sapiens* NCBI:9606, *Canis lupus familiaris* NCBI:9615, *Felis catus* NCBI:9685, *Equus caballus* NCBI:9796 and *Bos taurus* NCBI:9913. Breed VBO mappings should be attached where available. The condition is inherited, **not infectious or zoonotic**, and has no cross-species transmission.

Canine disease closely reproduces spontaneous bleeding, body size, immunity and clinical factor dosing, making dogs valuable for recombinant factor and gene-therapy studies. Purebred inbreeding can amplify pathogenic alleles, making veterinary carrier detection important.

## 15. Model organisms

- **F8- or F9-deficient mice:** inexpensive, genetically tractable models for hemostasis, inhibitor immunology, AAV dose-ranging, CRISPR and tolerance studies. Limitations include small blood volume, species-specific immunity and less spontaneous joint disease than humans.
- **Hemophilia-A rats:** more severe spontaneous bleeding and useful joint/trauma phenotypes; induced hemarthrosis produces C2M, C4M, CTX-II and PRO-C4 changes. (badulescu2024biomarkersinvolvedin pages 11-13)
- **Naturally affected dogs:** large-animal models for pharmacokinetics, surgery, immune tolerance and durable AAV/lentiviral correction. Canine studies have demonstrated sustained phenotypic correction, but cost, colony size and species-specific immunity limit throughput. (dodds2022onehealthanimal pages 11-12)
- **Induced canine hemarthrosis:** reproduces cartilage-turnover changes, including increased CTX-II and COMP. (badulescu2024biomarkersinvolvedin pages 11-13)
- **Nonhuman primates:** mainly safety, biodistribution, liver transduction and dose studies; they generally lack the inherited bleeding phenotype.
- **Patient-derived endothelial/hepatic cells and iPSCs:** useful for variant function, RNA defects, protein secretion and genome editing, but cannot reproduce whole-body bleeding or arthropathy.

A 2022 preclinical lentiviral study achieved stable, nearly lifelong normal-to-supranormal FVIII activity in hemophilia-A mice and normal-range activity in nonhuman primates, illustrating promise while not yet establishing human efficacy. These models also show that vector immunogenicity, pediatric liver growth and long-term genotoxicity are incompletely predicted by animals.

## Key 2023–2024 conclusions and expert analysis

1. The field has shifted from simply preventing fatal bleeding to **near-zero bleeding, preserved joint health and low treatment burden** through individualized prophylaxis.
2. Gene therapy is clinically real, but not yet a universal cure: hemophilia-B FIX expression appears relatively stable through three years, whereas declining FVIII after Roctavian remains a central hemophilia-A problem. (kaczmarek2024currentandemerging pages 5-5, levien2024valoctocogeneroxaparvovec pages 3-5)
3. Real-world inequity remains profound. Diagnostic/treatment delays and limited prophylaxis materially worsen joints and QoL, while lifetime treatment costs have been estimated at USD 20 million or more per patient in high-cost settings. (wang2024clinicalanalysisand pages 1-2, chernyi2024recentadvancesin pages 1-3)
4. Joint disease is both **degenerative and inflammatory**. Iron-driven synovitis, cytokines, angiogenesis and abnormal bone remodeling explain why even subclinical bleeding can create progressive damage. (badulescu2024biomarkersinvolvedin pages 11-13, badulescu2024biomarkersinvolvedin pages 2-3)
5. Molecular diagnosis should be comprehensive and structure-aware: inversion testing plus sequencing and CNV analysis approaches a 97% yield, while WGS/long-read/RNA methods address the residual unsolved fraction. (guo2018spectrumofmolecular pages 1-2, zhang2023moleculardiagnosisof pages 1-2)

### Representative abstract wording

Recent reviews characterize hemophilia as an “X-linked lifelong congenital bleeding disorder” caused by insufficient FVIII or FIX and describe gene therapy as aiming for long-term endogenous factor expression. The 2024 gene-therapy literature calls Hemgenix’s authorization “a significant milestone,” while the Roctavian review describes its approval as “a landmark in HA therapeutics” but emphasizes the need for stable FVIII expression. These are expert-review statements rather than proof of permanent cure; the quantitative trial outcomes and durability limitations above should govern knowledge-base interpretation. (chernyi2024recentadvancesin pages 1-3, kaczmarek2024currentandemerging pages 5-5, levien2024valoctocogeneroxaparvovec pages 3-5)

References

1. (OpenTargets Search: hemophilia A,hemophilia B-F8,F9): Open Targets Query (hemophilia A,hemophilia B-F8,F9, 43 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

2. (deshpande2024adenoassociatedvirus–basedgene pages 1-2): Saarang R. Deshpande, Keerthy Joseph, Jiayi Tong, Yong Chen, Allyson Pishko, and Adam Cuker. Adeno-associated virus–based gene therapy for hemophilia a and b: a systematic review and meta-analysis. Nov 2024. URL: https://doi.org/10.1182/bloodadvances.2024014111, doi:10.1182/bloodadvances.2024014111. This article has 30 citations and is from a peer-reviewed journal.

3. (wang2024clinicalanalysisand pages 1-2): Wen Wang, Li Xu, Jingsheng Wu, Weiyong Liu, Jiao Jin, Jing Huang, Zhongjin Xu, Yali Huang, Bai Li, Yufeng Liu, Qing Zhang, Min Zhou, Jie Peng, and Qun Hu. Clinical analysis and quality of life survey of hemophilia b patients in the central and western regions of china. Frontiers in Pediatrics, May 2024. URL: https://doi.org/10.3389/fped.2024.1366990, doi:10.3389/fped.2024.1366990. This article has 3 citations.

4. (zhang2023moleculardiagnosisof pages 1-2): Xialin Zhang, Kun Chen, Sicheng Bian, Gang Wang, Xiuyu Qin, Ruijuan Zhang, and Linhua Yang. Molecular diagnosis of hemophilia a and pathogenesis of novel f8 variants in shanxi, china. Global Medical Genetics, 10:247-262, Sep 2023. URL: https://doi.org/10.1055/s-0043-1774322, doi:10.1055/s-0043-1774322. This article has 3 citations.

5. (li2023f8geneinversion pages 1-2): Shaoying Li, Jianchun He, Liming Chu, Shuai Ren, Wenzhi He, Xiaoyan Ma, Yanchao Wang, Mincong Zhang, Lingyin Kong, Bo Liang, and Qing Li. F8 gene inversion and duplication cause no obvious hemophilia a phenotype. Frontiers in Genetics, Feb 2023. URL: https://doi.org/10.3389/fgene.2023.1098795, doi:10.3389/fgene.2023.1098795. This article has 5 citations and is from a peer-reviewed journal.

6. (arruda2021genetherapyfor pages 2-3): Valder R. Arruda, Jesse Weber, and Benjamin J. Samelson-Jones. Gene therapy for inherited bleeding disorders. Seminars in Thrombosis and Hemostasis, 47:161-173, Feb 2021. URL: https://doi.org/10.1055/s-0041-1722862, doi:10.1055/s-0041-1722862. This article has 29 citations and is from a peer-reviewed journal.

7. (chernyi2024recentadvancesin pages 1-3): Nikita Chernyi, Darina Gavrilova, Mane Saruhanyan, Ezekiel S. Oloruntimehin, Alexander Karabelsky, Evgeny Bezsonov, and Alexander Malogolovkin. Recent advances in gene therapy for hemophilia: projecting the perspectives. Jul 2024. URL: https://doi.org/10.3390/biom14070854, doi:10.3390/biom14070854. This article has 48 citations.

8. (guo2018spectrumofmolecular pages 1-2): Zhiping Guo, Linhua Yang, Xiuyu Qin, Xiue Liu, and Yaofang Zhang. Spectrum of molecular defects in 216 chinese families with hemophilia a: identification of noninversion mutation hot spots and 42 novel mutations. Clinical and Applied Thrombosis/Hemostasis, 24:70-78, Jan 2018. URL: https://doi.org/10.1177/1076029616687848, doi:10.1177/1076029616687848. This article has 26 citations.

9. (zhang2023moleculardiagnosisof pages 2-3): Xialin Zhang, Kun Chen, Sicheng Bian, Gang Wang, Xiuyu Qin, Ruijuan Zhang, and Linhua Yang. Molecular diagnosis of hemophilia a and pathogenesis of novel f8 variants in shanxi, china. Global Medical Genetics, 10:247-262, Sep 2023. URL: https://doi.org/10.1055/s-0043-1774322, doi:10.1055/s-0043-1774322. This article has 3 citations.

10. (wang2024clinicalanalysisand pages 8-9): Wen Wang, Li Xu, Jingsheng Wu, Weiyong Liu, Jiao Jin, Jing Huang, Zhongjin Xu, Yali Huang, Bai Li, Yufeng Liu, Qing Zhang, Min Zhou, Jie Peng, and Qun Hu. Clinical analysis and quality of life survey of hemophilia b patients in the central and western regions of china. Frontiers in Pediatrics, May 2024. URL: https://doi.org/10.3389/fped.2024.1366990, doi:10.3389/fped.2024.1366990. This article has 3 citations.

11. (wang2024clinicalanalysisand pages 7-8): Wen Wang, Li Xu, Jingsheng Wu, Weiyong Liu, Jiao Jin, Jing Huang, Zhongjin Xu, Yali Huang, Bai Li, Yufeng Liu, Qing Zhang, Min Zhou, Jie Peng, and Qun Hu. Clinical analysis and quality of life survey of hemophilia b patients in the central and western regions of china. Frontiers in Pediatrics, May 2024. URL: https://doi.org/10.3389/fped.2024.1366990, doi:10.3389/fped.2024.1366990. This article has 3 citations.

12. (croteau20212021clinicaltrials pages 1-6): Stacy E. Croteau, Michael Wang, and Allison P. Wheeler. <scp>2021</scp> clinical trials update: innovations in hemophilia therapy. American Journal of Hematology, 96:128-144, Nov 2021. URL: https://doi.org/10.1002/ajh.26018, doi:10.1002/ajh.26018. This article has 56 citations and is from a domain leading peer-reviewed journal.

13. (croteau20212021clinicaltrials pages 29-32): Stacy E. Croteau, Michael Wang, and Allison P. Wheeler. <scp>2021</scp> clinical trials update: innovations in hemophilia therapy. American Journal of Hematology, 96:128-144, Nov 2021. URL: https://doi.org/10.1002/ajh.26018, doi:10.1002/ajh.26018. This article has 56 citations and is from a domain leading peer-reviewed journal.

14. (levien2024valoctocogeneroxaparvovec pages 2-3): Terri L. Levien and Danial E. Baker. Valoctocogene roxaparvovec. Hospital Pharmacy, 59:254-263, Jan 2024. URL: https://doi.org/10.1177/00185787231222506, doi:10.1177/00185787231222506. This article has 1 citations and is from a peer-reviewed journal.

15. (levien2024valoctocogeneroxaparvovec pages 3-5): Terri L. Levien and Danial E. Baker. Valoctocogene roxaparvovec. Hospital Pharmacy, 59:254-263, Jan 2024. URL: https://doi.org/10.1177/00185787231222506, doi:10.1177/00185787231222506. This article has 1 citations and is from a peer-reviewed journal.

16. (anguela2024hemophiliaband pages 2-3): Xavier M. Anguela and Katherine A. High. Hemophilia b and gene therapy: a new chapter with etranacogene dezaparvovec. Blood Advances, 8:1796-1803, Apr 2024. URL: https://doi.org/10.1182/bloodadvances.2023010511, doi:10.1182/bloodadvances.2023010511. This article has 54 citations and is from a peer-reviewed journal.

17. (kaczmarek2024currentandemerging pages 5-5): Radoslaw Kaczmarek, Wolfgang Miesbach, Margareth C. Ozelo, and Pratima Chowdary. Current and emerging gene therapies for haemophilia a and b. Haemophilia, 30:12-20, Mar 2024. URL: https://doi.org/10.1111/hae.14984, doi:10.1111/hae.14984. This article has 21 citations and is from a peer-reviewed journal.

18. (anguela2024hemophiliaband pages 4-5): Xavier M. Anguela and Katherine A. High. Hemophilia b and gene therapy: a new chapter with etranacogene dezaparvovec. Blood Advances, 8:1796-1803, Apr 2024. URL: https://doi.org/10.1182/bloodadvances.2023010511, doi:10.1182/bloodadvances.2023010511. This article has 54 citations and is from a peer-reviewed journal.

19. (NCT05608863 chunk 1):  He-move-philia, Lifestyle Intervention for Patients With Hemophilia. Radboud University Medical Center. 2022. ClinicalTrials.gov Identifier: NCT05608863

20. (badulescu2024biomarkersinvolvedin pages 11-13): Oana Viola Badulescu, Dragos-Viorel Scripcariu, Minerva Codruta Badescu, Manuela Ciocoiu, Maria Cristina Vladeanu, Carmen Elena Plesoianu, Andrei Bojan, Dan Iliescu-Halitchi, Razvan Tudor, Bogdan Huzum, Otilia Elena Frasinariu, and Iris Bararu-Bojan. Biomarkers involved in the pathogenesis of hemophilic arthropathy. International Journal of Molecular Sciences, 25:9897, Sep 2024. URL: https://doi.org/10.3390/ijms25189897, doi:10.3390/ijms25189897. This article has 15 citations.

21. (badulescu2024biomarkersinvolvedin pages 3-5): Oana Viola Badulescu, Dragos-Viorel Scripcariu, Minerva Codruta Badescu, Manuela Ciocoiu, Maria Cristina Vladeanu, Carmen Elena Plesoianu, Andrei Bojan, Dan Iliescu-Halitchi, Razvan Tudor, Bogdan Huzum, Otilia Elena Frasinariu, and Iris Bararu-Bojan. Biomarkers involved in the pathogenesis of hemophilic arthropathy. International Journal of Molecular Sciences, 25:9897, Sep 2024. URL: https://doi.org/10.3390/ijms25189897, doi:10.3390/ijms25189897. This article has 15 citations.

22. (badulescu2024biomarkersinvolvedin pages 5-6): Oana Viola Badulescu, Dragos-Viorel Scripcariu, Minerva Codruta Badescu, Manuela Ciocoiu, Maria Cristina Vladeanu, Carmen Elena Plesoianu, Andrei Bojan, Dan Iliescu-Halitchi, Razvan Tudor, Bogdan Huzum, Otilia Elena Frasinariu, and Iris Bararu-Bojan. Biomarkers involved in the pathogenesis of hemophilic arthropathy. International Journal of Molecular Sciences, 25:9897, Sep 2024. URL: https://doi.org/10.3390/ijms25189897, doi:10.3390/ijms25189897. This article has 15 citations.

23. (badulescu2024biomarkersinvolvedin pages 8-10): Oana Viola Badulescu, Dragos-Viorel Scripcariu, Minerva Codruta Badescu, Manuela Ciocoiu, Maria Cristina Vladeanu, Carmen Elena Plesoianu, Andrei Bojan, Dan Iliescu-Halitchi, Razvan Tudor, Bogdan Huzum, Otilia Elena Frasinariu, and Iris Bararu-Bojan. Biomarkers involved in the pathogenesis of hemophilic arthropathy. International Journal of Molecular Sciences, 25:9897, Sep 2024. URL: https://doi.org/10.3390/ijms25189897, doi:10.3390/ijms25189897. This article has 15 citations.

24. (chernyi2024recentadvancesin pages 3-4): Nikita Chernyi, Darina Gavrilova, Mane Saruhanyan, Ezekiel S. Oloruntimehin, Alexander Karabelsky, Evgeny Bezsonov, and Alexander Malogolovkin. Recent advances in gene therapy for hemophilia: projecting the perspectives. Jul 2024. URL: https://doi.org/10.3390/biom14070854, doi:10.3390/biom14070854. This article has 48 citations.

25. (badulescu2024biomarkersinvolvedin pages 10-11): Oana Viola Badulescu, Dragos-Viorel Scripcariu, Minerva Codruta Badescu, Manuela Ciocoiu, Maria Cristina Vladeanu, Carmen Elena Plesoianu, Andrei Bojan, Dan Iliescu-Halitchi, Razvan Tudor, Bogdan Huzum, Otilia Elena Frasinariu, and Iris Bararu-Bojan. Biomarkers involved in the pathogenesis of hemophilic arthropathy. International Journal of Molecular Sciences, 25:9897, Sep 2024. URL: https://doi.org/10.3390/ijms25189897, doi:10.3390/ijms25189897. This article has 15 citations.

26. (NCT07437404 chunk 1):  Efficacy and Safety Evaluation Study of SCT800 in Previously Untreated Hemophilia A Patients.. Sinocelltech Ltd.. 2024. ClinicalTrials.gov Identifier: NCT07437404

27. (bai2021casereportidentification pages 7-8): Haiyan Bai, Xia Xue, Li Tian, Xi Tong Liu, and Qian Li. Case report: identification of a de novo missense mutation in the f8 gene, p.(phe690leu)/c.2070c > a, causing hemophilia a: a case report. Frontiers in Genetics, Mar 2021. URL: https://doi.org/10.3389/fgene.2020.589899, doi:10.3389/fgene.2020.589899. This article has 5 citations and is from a peer-reviewed journal.

28. (marchesini2021recentadvancesin pages 10-12): Emanuela Marchesini, Massimo Morfini, and Leonard Valentino. Recent advances in the treatment of hemophilia: a review. Biologics : Targets & Therapy, 15:221-235, Jun 2021. URL: https://doi.org/10.2147/btt.s252580, doi:10.2147/btt.s252580. This article has 86 citations.

29. (joshi2024hemostatsinthe pages 22-23): Maithili Joshi, Zongmin Zhao, and Samir Mitragotri. Hemostats in the clinic. Bioengineering & Translational Medicine, May 2024. URL: https://doi.org/10.1002/btm2.10673, doi:10.1002/btm2.10673. This article has 8 citations.

30. (NCT06224907 chunk 2):  Phase 3 Study for Efficacy and Safety Outcomes Data in Japanese Patients With Severe Hemophilia A. BioMarin Pharmaceutical. 2023. ClinicalTrials.gov Identifier: NCT06224907

31. (NCT05662319 chunk 3):  A Study to Test a Medicine (Fitusiran) Injected Under the Skin for Preventing Bleeding Episodes in Male Adolescent or Adult Participants With Severe Hemophilia. Sanofi. 2023. ClinicalTrials.gov Identifier: NCT05662319

32. (NCT03974113 chunk 2):  Fitusiran Prophylaxis in Male Pediatric Subjects Aged 1 to Less Than 12 Years With Hemophilia A or B. Genzyme, a Sanofi Company. 2020. ClinicalTrials.gov Identifier: NCT03974113

33. (NCT06922045 chunk 1):  Phase III Clinical Trial of STSP-0601 for Injection in Hemophilia Patients. Jiangsu BioJeTay Biotechnology Co., Ltd.. 2025. ClinicalTrials.gov Identifier: NCT06922045

34. (dodds2022onehealthanimal pages 5-7): W. Jean Dodds. One health: animal models of heritable human bleeding diseases. Animals : an Open Access Journal from MDPI, 13:87, Dec 2022. URL: https://doi.org/10.3390/ani13010087, doi:10.3390/ani13010087. This article has 7 citations.

35. (dodds2022onehealthanimal pages 11-12): W. Jean Dodds. One health: animal models of heritable human bleeding diseases. Animals : an Open Access Journal from MDPI, 13:87, Dec 2022. URL: https://doi.org/10.3390/ani13010087, doi:10.3390/ani13010087. This article has 7 citations.

36. (dodds2022onehealthanimal pages 2-4): W. Jean Dodds. One health: animal models of heritable human bleeding diseases. Animals : an Open Access Journal from MDPI, 13:87, Dec 2022. URL: https://doi.org/10.3390/ani13010087, doi:10.3390/ani13010087. This article has 7 citations.

37. (badulescu2024biomarkersinvolvedin pages 2-3): Oana Viola Badulescu, Dragos-Viorel Scripcariu, Minerva Codruta Badescu, Manuela Ciocoiu, Maria Cristina Vladeanu, Carmen Elena Plesoianu, Andrei Bojan, Dan Iliescu-Halitchi, Razvan Tudor, Bogdan Huzum, Otilia Elena Frasinariu, and Iris Bararu-Bojan. Biomarkers involved in the pathogenesis of hemophilic arthropathy. International Journal of Molecular Sciences, 25:9897, Sep 2024. URL: https://doi.org/10.3390/ijms25189897, doi:10.3390/ijms25189897. This article has 15 citations.

## Artifacts

- [Edison artifact artifact-00](Hemophilia-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 16 |
| Resolved | 16 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 16 |
| On topic | 11 |
| Off topic | 1 |

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `DOI:10.1177/00185787231222506` (5 mentions) - Valoctocogene Roxaparvovec
  - shared terms: none

Weighed against this report's own most characteristic terms: `disease`, `hemophilia`, `gene`, `bleeding`, `fviii`, `clinical`, `variant`, `inhibitor`, `genetic`, `treatment`, `severe`, `activity`, `include`, `prophylaxis`, `fix`, `molecular`, `phenotype`, `therapy`, `model`, `joint`.

All extracted references resolved successfully.
Resolving is not the same as being relevant, though - see the references listed above as possibly off topic.